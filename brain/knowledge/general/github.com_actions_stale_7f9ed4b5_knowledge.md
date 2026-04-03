---
id: github.com-actions-stale-7f9ed4b5-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:27.708695
---

# KNOWLEDGE EXTRACT: github.com_actions_stale_7f9ed4b5
> **Extracted on:** 2026-04-01 11:11:01
> **Source:** D:/LongLeo/AI OS CORP/AI OS/core/security/QUARANTINE/KI-BATCH-20260331205007521293/github.com_actions_stale_7f9ed4b5

---

## File: `.eslintignore`
```
# Ignore list
/*

# Do not ignore these folders:
!__tests__/
!src/
```

## File: `.eslintrc.js`
```javascript
// This is a reusable configuration file copied from https://github.com/actions/reusable-workflows/tree/main/reusable-configurations. Please don't make changes to this file as it's the subject of an automatic update.
module.exports = {
  extends: [
    'eslint:recommended',
    'plugin:@typescript-eslint/recommended',
    'plugin:eslint-plugin-jest/recommended',
    'eslint-config-prettier'
  ],
  parser: '@typescript-eslint/parser',
  plugins: ['@typescript-eslint', 'eslint-plugin-node', 'eslint-plugin-jest'],
  rules: {
    '@typescript-eslint/no-require-imports': 'error',
    '@typescript-eslint/no-non-null-assertion': 'off',
    '@typescript-eslint/no-explicit-any': 'off',
    '@typescript-eslint/no-empty-function': 'off',
    '@typescript-eslint/ban-ts-comment': [
      'error',
      {
        'ts-ignore': 'allow-with-description'
      }
    ],
    'no-console': 'error',
    'yoda': 'error',
    'prefer-const': [
      'error',
      {
        destructuring: 'all'
      }
    ],
    'no-control-regex': 'off',
    'no-constant-condition': ['error', {checkLoops: false}],
    'node/no-extraneous-import': 'error'
  },
  overrides: [
    {
      files: ['**/*{test,spec}.ts'],
      rules: {
        '@typescript-eslint/no-unused-vars': 'off',
        'jest/no-standalone-expect': 'off',
        'jest/no-conditional-expect': 'off',
        'no-console': 'off',

      }
    }
  ],
  env: {
    node: true,
    es6: true,
    'jest/globals': true
  }
};
```

## File: `.gitattributes`
```
* text=auto eol=lf
.licenses/** -diff linguist-generated=true
```

## File: `.gitignore`
```
.DS_Store
node_modules/
lib/
__tests__/runner/*
.idea
```

## File: `.licensed.yml`
```yaml
sources:
  npm: true

allowed:
  - apache-2.0
  - bsd-2-clause
  - bsd-3-clause
  - isc
  - mit
  - cc0-1.0
  - unlicense
  - 0bsd

reviewed:
  npm:
    - "@actions/http-client"
```

## File: `.prettierignore`
```
# Ignore list
/*

# Do not ignore these folders:
!__tests__/
!.github/
!src/
```

## File: `.prettierrc.js`
```javascript
// This is a reusable configuration file copied from https://github.com/actions/reusable-workflows/tree/main/reusable-configurations. Please don't make changes to this file as it's the subject of an automatic update.
module.exports = {
  printWidth: 80,
  tabWidth: 2,
  useTabs: false,
  semi: true,
  singleQuote: true,
  trailingComma: 'none',
  bracketSpacing: false,
  arrowParens: 'avoid'
};
```

## File: `.versionrc.json`
```json
{
  "header": "### Actions Stale Changelog\n"
}
```

## File: `CHANGELOG.md`
```markdown
# Changelog

# [10.1.0]

## What's Changed

* Add only-issue-types option to filter issues by type by @Bibo-Joshi in https://github.com/actions/stale/pull/1255

# [10.0.0]

## What's Changed

## Breaking Changes
* Upgrade to node 24 by @salmanmkc in https://github.com/actions/stale/pull/1279
Make sure your runner is on version v2.327.1 or later to ensure compatibility with this release. [Release Notes](https://github.com/actions/runner/releases/tag/v2.327.1)

## Enhancement
- Introducing sort-by option by @suyashgaonkar in https://github.com/actions/stale/pull/1254

## Dependency Upgrades
* Upgrade actions/publish-immutable-action from 0.0.3 to 0.0.4 by @dependabot[bot] in https://github.com/actions/stale/pull/1186
* Upgrade undici from 5.28.4 to 5.28.5 by @dependabot[bot] in https://github.com/actions/stale/pull/1201
* Upgrade @action/cache from 4.0.0 to 4.0.2 by @aparnajyothi-y in https://github.com/actions/stale/pull/1226
* Upgrade @action/cache from 4.0.2 to 4.0.3 by @suyashgaonkar in https://github.com/actions/stale/pull/1233
* Upgrade undici from 5.28.5 to 5.29.0 by @dependabot[bot] in https://github.com/actions/stale/pull/1251
* Upgrade form-data to bring in fix for critical vulnerability by @gowridurgad in https://github.com/actions/stale/pull/1277

## Documentation changes

- Changelog update for recent releases by @suyashgaonkar in https://github.com/actions/stale/pull/1224
- Permissions update in Readme by @ghadimir in https://github.com/actions/stale/pull/1248

# [9.1.0]

## What's Changed
* Documentation update by @Marukome0743 in https://github.com/actions/stale/pull/1116
* Add workflow file for publishing releases to immutable action package by @Jcambass in https://github.com/actions/stale/pull/1179
* Update undici from 5.28.2 to 5.28.4 by @dependabot in https://github.com/actions/stale/pull/1150
* Update actions/checkout from 3 to 4 by @dependabot in https://github.com/actions/stale/pull/1091
* Update actions/publish-action from 0.2.2 to 0.3.0 by @dependabot in https://github.com/actions/stale/pull/1147
* Update ts-jest from 29.1.1 to 29.2.5 by @dependabot in https://github.com/actions/stale/pull/1175
* Update @actions/core from 1.10.1 to 1.11.1 by @dependabot in https://github.com/actions/stale/pull/1191
* Update @types/jest from 29.5.11 to 29.5.14 by @dependabot in https://github.com/actions/stale/pull/1193
* Update @actions/cache from 3.2.2 to 4.0.0 by @dependabot in https://github.com/actions/stale/pull/1194

# [9.0.0]

## Breaking Changes
1. Action is now stateful: If the action ends because of [operations-per-run](https://github.com/actions/stale#operations-per-run) then the next run will start from the first unprocessed issue skipping the issues processed during the previous run(s). The state is reset when all the issues are processed. This should be considered for scheduling workflow runs.
2. Version 9 of this action updated the runtime to Node.js 20. All scripts are now run with Node.js 20 instead of Node.js 16 and are affected by any breaking changes between Node.js 16 and 20.

## What Else Changed
1. Performance optimization that removes unnecessary API calls by @dsame in [#1033](https://github.com/actions/stale/pull/1033/); fixes [#792](https://github.com/actions/stale/issues/792)
2. Logs displaying current GitHub API rate limit by @dsame in [#1032](https://github.com/actions/stale/pull/1032); addresses [#1029](https://github.com/actions/stale/issues/1029)

For more information, please read the [action documentation](https://github.com/actions/stale#readme) and its [section about statefulness](https://github.com/actions/stale#statefulness)



# [4.1.1]

In scope of this release we updated [actions/core to 1.10.0](https://github.com/actions/stale/pull/957) for v4 and [fixed issues operation count](https://github.com/actions/stale/pull/662). 

# [8.0.0]

:warning: This version contains breaking changes :warning:

* New option labels-to-remove-when-stale enables users to specify list of comma delimited labels that will be removed when the issue or PR becomes stale by @panticmilos https://github.com/actions/stale/issues/770
* Skip deleting the branch in the upstream of a forked repo by @dsame https://github.com/actions/stale/pull/913
* abort the build on the error by @dsame in https://github.com/actions/stale/pull/935

# [7.0.0]

:warning: Breaking change :warning:

* Allow daysBeforeStale options to be float by @irega in https://github.com/actions/stale/pull/841
* Use cache in check-dist.yml by @jongwooo in https://github.com/actions/stale/pull/876
* fix print outputs step in existing workflows by @irega in https://github.com/actions/stale/pull/859
* Update issue and PR templates, add/delete workflow files by @IvanZosimov in https://github.com/actions/stale/pull/880
* Update how stale handles exempt items by @johnsudol in https://github.com/actions/stale/pull/874

# [6.0.1]

Update @actions/core to v1.10.0 ([#839](https://github.com/actions/stale/pull/839))

# [6.0.0]

:warning: Breaking change :warning:

Issues/PRs default `close-issue-reason` is now `not_planned`([#789](https://github.com/actions/stale/issues/789))

# [5.1.0]

[Don't process stale issues right after they're marked stale](https://github.com/actions/stale/issues/696)
[Add close-issue-reason option][#764](https://github.com/actions/stale/pull/764)[#772](https://github.com/actions/stale/pull/772)
Various dependabot/dependency updates

## [4.1.0](https://github.com/actions/stale/compare/v3.0.19...v4.1.0) (2021-07-14)

## Features

- [Ability to exempt draft PRs](https://github.com/actions/stale/commit/9912fa74d1c01b5d6187793d97441019cbe325d0)

## [4.0.0](https://github.com/actions/stale/compare/v3.0.19...v4.0.0) (2021-07-14)

### Features

- **options:** simplify config by removing skip stale message options ([#457](https://github.com/actions/stale/issues/457)) ([6ec637d](https://github.com/actions/stale/commit/6ec637d238067ab8cc96c9289dcdac280bbd3f4a)), closes [#405](https://github.com/actions/stale/issues/405) [#455](https://github.com/actions/stale/issues/455)
- **output:** print output parameters ([#458](https://github.com/actions/stale/issues/458)) ([3e6d35b](https://github.com/actions/stale/commit/3e6d35b685f0b2fa1a69be893fa07d3d85e05ee0))

### Bug Fixes

- **dry-run:** forbid mutations in dry-run ([#500](https://github.com/actions/stale/issues/500)) ([f1017f3](https://github.com/actions/stale/commit/f1017f33dd159ea51366375120c3e6981d7c3097)), closes [#499](https://github.com/actions/stale/issues/499)
- **logs:** coloured logs ([#465](https://github.com/actions/stale/issues/465)) ([5fbbfba](https://github.com/actions/stale/commit/5fbbfba142860ea6512549e96e36e3540c314132))
- **operations:** fail fast the current batch to respect the operations limit ([#474](https://github.com/actions/stale/issues/474)) ([5f6f311](https://github.com/actions/stale/commit/5f6f311ca6aa75babadfc7bac6edf5d85fa3f35d)), closes [#466](https://github.com/actions/stale/issues/466)
- **label comparison**: make label comparison case insensitive [#517](https://github.com/actions/stale/pull/517), closes [#516](https://github.com/actions/stale/pull/516)
- **filtering comments by actor could have strange behavior**: "stale" comments are now detected based on if the message is the stale message not _who_ made the comment([#519](https://github.com/actions/stale/pull/519)), fixes [#441](https://github.com/actions/stale/pull/441), [#509](https://github.com/actions/stale/pull/509), [#518](https://github.com/actions/stale/pull/518)

### Breaking Changes

- The options `skip-stale-issue-message` and `skip-stale-pr-message` were removed. Instead, setting the options `stale-issue-message` and `stale-pr-message` will be enough to let the stale workflow add a comment. If the options are unset, a comment will not be added which was the equivalent of setting `skip-stale-issue-message` to `true`.
- The `operations-per-run` option will be more effective. After migrating, you could face a failed-fast process workflow if you let the default value (30) or set it to a small number. In that case, you will see a warning at the end of the logs (if enabled) indicating that the workflow was stopped sooner to avoid consuming too much API calls. In most cases, you can just increase this limit to make sure to process everything in a single run.

```

## File: `CODEOWNERS`
```
* @actions/setup-actions-team
```

## File: `CONTRIBUTING.md`
```markdown
# Building and testing

Install the dependencies.

```bash
$ npm install
```

Build the typescript and package it for distribution.

```bash
$ npm run build && npm run pack
```

Run the tests :heavy_check_mark:

```bash
$ npm test
```

Run the tests and display only the first failing tests :heavy_check_mark:

```bash
$ npm run test:only-errors
```

Run the tests with the watch mode :heavy_check_mark:

```bash
$ npm run test:watch
```

Run the linter and fix (almost) every issue for you :heavy_check_mark:

```bash
$ npm run lint:all:fix
```

# Before creating a PR

## Build and quality checks

Build, lint, package and test everything.

```bash
$ npm run all
```

IMPORTANT:
Be sure to commit the result of:
```bash
$ npm run pack
```
Otherwise PR checks will fail. 

# Release

Based on [standard-version](https://github.com/conventional-changelog/standard-version).

## Define the new version

You can run `npm run release:dry-run` to create a dry-run, or you can directly run `npm run release` to create a new local release.  
It will run `prerelease` beforehand to build and pack everything.

If the `prerelease` succeeded, a bump of version will happen based on the unreleased commits.  
It will:

- Update the _package.json_ version field
- Update the _package-lock.json_ version field
- Update the _CHANGELOG.md_ to include the release notes of the new version
- Create a local tag
- Create a commit

If everything generated seems ok for you, you can push your tag by running `git push --follow-tags origin {your-branch-name}`.
```

## File: `LICENSE`
```
Copyright (c) 2025, cache

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```

## File: `README.md`
```markdown
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
| [repo-token](#repo-token)                                           | PAT for GitHub API authentication                                           | `${{ github.token }}` |
| [days-before-stale](#days-before-stale)                             | Idle number of days before marking issues/PRs stale                         | `60`                  |
| [days-before-issue-stale](#days-before-issue-stale)                 | Override [days-before-stale](#days-before-stale) for issues only            |                       |
| [days-before-pr-stale](#days-before-pr-stale)                       | Override [days-before-stale](#days-before-stale) for PRs only               |                       |
| [days-before-close](#days-before-close)                             | Idle number of days before closing stale issues/PRs                         | `7`                   |
| [days-before-issue-close](#days-before-issue-close)                 | Override [days-before-close](#days-before-close) for issues only            |                       |
| [days-before-pr-close](#days-before-pr-close)                       | Override [days-before-close](#days-before-close) for PRs only               |                       |
| [stale-issue-message](#stale-issue-message)                         | Comment on the staled issues                                                |                       |
| [stale-pr-message](#stale-pr-message)                               | Comment on the staled PRs                                                   |                       |
| [close-issue-message](#close-issue-message)                         | Comment on the staled issues while closed                                   |                       |
| [close-pr-message](#close-pr-message)                               | Comment on the staled PRs while closed                                      |                       |
| [stale-issue-label](#stale-issue-label)                             | Label to apply on staled issues                                             | `Stale`               |
| [close-issue-label](#close-issue-label)                             | Label to apply on closed issues                                             |                       |
| [close-issue-reason](#close-issue-reason)                           | Reason to use when closing issues                                           | `not_planned`         |
| [stale-pr-label](#stale-pr-label)                                   | Label to apply on staled PRs                                                | `Stale`               |
| [close-pr-label](#close-pr-label)                                   | Label to apply on closed PRs                                                |                       |
| [exempt-issue-labels](#exempt-issue-labels)                         | Labels on issues exempted from stale                                        |                       |
| [exempt-pr-labels](#exempt-pr-labels)                               | Labels on PRs exempted from stale                                           |                       |
| [only-labels](#only-labels)                                         | Only issues/PRs with ALL these labels are checked                           |                       |
| [only-issue-labels](#only-issue-labels)                             | Override [only-labels](#only-labels) for issues only                        |                       |
| [only-pr-labels](#only-pr-labels)                                   | Override [only-labels](#only-labels) for PRs only                           |                       |
| [any-of-labels](#any-of-labels)                                     | Only issues/PRs with ANY of these labels are checked                        |                       |
| [any-of-issue-labels](#any-of-issue-labels)                         | Override [any-of-labels](#any-of-labels) for issues only                    |                       |
| [any-of-pr-labels](#any-of-pr-labels)                               | Override [any-of-labels](#any-of-labels) for PRs only                       |                       |
| [operations-per-run](#operations-per-run)                           | Max number of operations per run                                            | `30`                  |
| [remove-stale-when-updated](#remove-stale-when-updated)             | Remove stale label from issues/PRs on updates                               | `true`                |
| [remove-issue-stale-when-updated](#remove-issue-stale-when-updated) | Remove stale label from issues on updates/comments                          |                       |
| [remove-pr-stale-when-updated](#remove-pr-stale-when-updated)       | Remove stale label from PRs on updates/comments                             |                       |
| [labels-to-add-when-unstale](#labels-to-add-when-unstale)           | Add specified labels from issues/PRs when they become unstale               |                       |
| [labels-to-remove-when-stale](#labels-to-remove-when-stale)         | Remove specified labels from issues/PRs when they become stale              |                       |
| [labels-to-remove-when-unstale](#labels-to-remove-when-unstale)     | Remove specified labels from issues/PRs when they become unstale            |                       |
| [debug-only](#debug-only)                                           | Dry-run                                                                     | `false`               |
| [ascending](#ascending)                                             | Order to get issues/PRs                                                     | `false`               |
| [start-date](#start-date)                                           | Skip stale action for issues/PRs created before it                          |                       |
| [delete-branch](#delete-branch)                                     | Delete branch after closing a stale PR                                      | `false`               |
| [exempt-milestones](#exempt-milestones)                             | Milestones on issues/PRs exempted from stale                                |                       |
| [exempt-issue-milestones](#exempt-issue-milestones)                 | Override [exempt-milestones](#exempt-milestones) for issues only            |                       |
| [exempt-pr-milestones](#exempt-pr-milestones)                       | Override [exempt-milestones](#exempt-milestones) for PRs only               |                       |
| [exempt-all-milestones](#exempt-all-milestones)                     | Exempt all issues/PRs with milestones from stale                            | `false`               |
| [exempt-all-issue-milestones](#exempt-all-issue-milestones)         | Override [exempt-all-milestones](#exempt-all-milestones) for issues only    |                       |
| [exempt-all-pr-milestones](#exempt-all-pr-milestones)               | Override [exempt-all-milestones](#exempt-all-milestones) for PRs only       |                       |
| [exempt-assignees](#exempt-assignees)                               | Assignees on issues/PRs exempted from stale                                 |                       |
| [exempt-issue-assignees](#exempt-issue-assignees)                   | Override [exempt-assignees](#exempt-assignees) for issues only              |                       |
| [exempt-pr-assignees](#exempt-pr-assignees)                         | Override [exempt-assignees](#exempt-assignees) for PRs only                 |                       |
| [exempt-all-assignees](#exempt-all-assignees)                       | Exempt all issues/PRs with assignees from stale                             | `false`               |
| [exempt-all-issue-assignees](#exempt-all-issue-assignees)           | Override [exempt-all-assignees](#exempt-all-assignees) for issues only      |                       |
| [exempt-all-pr-assignees](#exempt-all-pr-assignees)                 | Override [exempt-all-assignees](#exempt-all-assignees) for PRs only         |                       |
| [exempt-draft-pr](#exempt-draft-pr)                                 | Skip the stale action for draft PRs                                         | `false`               |
| [enable-statistics](#enable-statistics)                             | Display statistics in the logs                                              | `true`                |
| [ignore-updates](#ignore-updates)                                   | Any update (update/comment) can reset the stale idle time on the issues/PRs | `false`               |
| [ignore-issue-updates](#ignore-issue-updates)                       | Override [ignore-updates](#ignore-updates) for issues only                  |                       |
| [ignore-pr-updates](#ignore-pr-updates)                             | Override [ignore-updates](#ignore-updates) for PRs only                     |                       |
| [include-only-assigned](#include-only-assigned)                     | Process only assigned issues                                                | `false`               |
| [sort-by](#sort-by)                                                 | What to sort issues and PRs by                                              | `created`             |
| [only-issue-types](#only-issue-types)                               | Only issues with a matching type are processed as stale/closed.             |                       |

### List of output options

| Output            | Description                                 |
| ----------------- | ------------------------------------------- |
| staled-issues-prs | List of all staled issues and pull requests |
| closed-issues-prs | List of all closed issues and pull requests |

### Detailed options

#### repo-token

Personal Access Token (PAT) that allows the stale workflow to authenticate and perform API calls to GitHub.  
Under the hood, it uses the [@actions/github](https://www.npmjs.com/package/@actions/github) package.

Default value: `${{ github.token }}`

#### days-before-stale

The idle number of days before marking the issues or the pull requests as stale (by adding a label).  
The issues or the pull requests will be marked as stale if the last update (based on [GitHub issue](https://docs.github.com/en/rest/reference/issues) field `updated_at`) is older than the idle number of days.  
It means that any updates made, or any comments added to the issues or to the pull requests will restart the counter of days before marking as stale.  
However, if you wish to ignore this behaviour so that the creation date (based on [GitHub issue](https://docs.github.com/en/rest/reference/issues) field `created_at`) only matters, you can disable the [ignore-updates](#ignore-updates) option.

If set to a negative number like `-1`, no issues or pull requests will be marked as stale automatically.  
In that case, you can still add the stale label manually to mark as stale.

The label used to stale is defined by these two options:

- [stale-issue-label](#stale-issue-label)
- [stale-pr-label](#stale-pr-label)

A comment can also be added to notify about the stale and is defined by these two options:

- [stale-issue-message](#stale-issue-message)
- [stale-pr-message](#stale-pr-message)

You can fine tune which issues or pull requests should be marked as stale based on the milestones, the assignees, the creation date and the missing/present labels from these options:

- [exempt-issue-labels](#exempt-issue-labels)
- [exempt-pr-labels](#exempt-pr-labels)
- [only-labels](#only-labels)
- [any-of-labels](#any-of-labels)
- [start-date](#start-date)
- [exempt-milestones](#exempt-milestones)
- [exempt-all-milestones](#exempt-all-milestones)
- [exempt-assignees](#exempt-assignees)
- [exempt-all-assignees](#exempt-all-assignees)
- [ignore-updates](#ignore-updates)

Default value: `60`

#### days-before-issue-stale

Useful to override [days-before-stale](#days-before-stale) but only for the idle number of days before marking the issues as stale.

Default value: unset

#### days-before-pr-stale

Useful to override [days-before-stale](#days-before-stale) but only for the idle number of days before marking the pull requests as stale.

Default value: unset

#### days-before-close

The idle number of days before closing the stale issues or the stale pull requests (due to the stale label).  
The issues or the pull requests will be closed if the last update (based on [GitHub issue](https://docs.github.com/en/rest/reference/issues) field `updated_at`) is older than the idle number of days.  
Since adding the stale label will alter the last update date, we can calculate the number of days from this date.

If set to a negative number like `-1`, the issues or the pull requests will never be closed automatically.

The label used to stale is defined by these two options:

- [stale-issue-label](#stale-issue-label)
- [stale-pr-label](#stale-pr-label)

Default value: `7`

#### days-before-issue-close

Override [days-before-close](#days-before-close) but only for the idle number of days before closing the stale issues.

Default value: unset

#### days-before-pr-close

Override [days-before-close](#days-before-close) but only for the idle number of days before closing the stale pull requests.

Default value: unset

#### stale-issue-message

The message that will be added as a comment to the issues when the stale workflow marks it automatically as stale with a label.

You can skip the comment sending by passing an empty string.

Default value: unset  
Required Permission: `issues: write`

#### stale-pr-message

The message that will be added as a comment to the pull requests when the stale workflow marks it automatically as stale with a label.

You can skip the comment sending by passing an empty string.

Default value: unset  
Required Permission: `pull-requests: write`

#### close-issue-message

The message that will be added as a comment to the issues when the stale workflow closes it automatically after being stale for too long.

Default value: unset  
Required Permission: `issues: write`

#### close-pr-message

The message that will be added as a comment to the pull requests when the stale workflow closes it automatically after being stale for too long.

Default value: unset  
Required Permission: `pull-requests: write`

#### stale-issue-label

The label that will be added to the issues when automatically marked as stale.  
If you wish to speedup the stale workflow for the issues, you can add this label manually to mark as stale.

Default value: `Stale`  
Required Permission: `issues: write`

#### close-issue-label

The label that will be added to the issues when closed automatically.  
It will be automatically removed if the issues are no longer closed nor locked.

Default value: unset  
Required Permission: `issues: write`

#### close-issue-reason

Specify the [reason](https://github.blog/changelog/2022-05-19-the-new-github-issues-may-19th-update/) used when closing issues. Valid values are `completed` and `not_planned`.

Default value: `not_planned`

#### stale-pr-label

The label that will be added to the pull requests when automatically marked as stale.  
If you wish to speedup the stale workflow for the pull requests, you can add this label manually to mark as stale.

Default value: `Stale`  
Required Permission: `pull-requests: write`

#### close-pr-label

The label that will be added to the pull requests when closed automatically.  
It will be automatically removed if the pull requests are no longer closed nor locked.

Default value: unset  
Required Permission: `pull-requests: write`

#### exempt-issue-labels

Comma separated list of labels that can be assigned to issues to exclude them from being marked as stale
(e.g: `question,bug`)

If unset (or an empty string), this option will not alter the stale workflow.

Default value: unset

#### exempt-pr-labels

Comma separated list of labels that can be assigned to pull requests to exclude them from being marked as stale
(e.g: `need-help,WIP`)

If unset (or an empty string), this option will not alter the stale workflow.

Default value: unset

#### only-labels

An allow-list of label(s) to only process the issues or the pull requests that contain all these label(s).  
It can be a comma separated list of labels (e.g: `answered,needs-rebase`).

If unset (or an empty string), this option will not alter the stale workflow.

If you wish to only check that the issues or the pull requests contain one of these label(s), use instead [any-of-labels](#any-of-labels).

Default value: unset

#### only-issue-labels

Override [only-labels](#only-labels) but only to process the issues that contain all these label(s).

Default value: unset

#### only-pr-labels

Override [only-labels](#only-labels) but only to process the pull requests that contain all these label(s).

Default value: unset

#### any-of-labels

An allow-list of label(s) to only process the issues or the pull requests that contain one of these label(s).  
It can be a comma separated list of labels (e.g: `answered,needs-rebase`).

If unset (or an empty string), this option will not alter the stale workflow.

If you wish to only check that the issues or the pull requests contain all these label(s), use instead [only-labels](#only-labels).

Default value: unset

#### any-of-issue-labels

Override [any-of-labels](#any-of-labels) but only to process the issues that contain one of these label(s).

Default value: unset

#### any-of-pr-labels

Override [any-of-labels](#any-of-labels) but only to process the pull requests that contain one of these label(s).

Default value: unset

#### operations-per-run

_Context:_  
This action performs some API calls to GitHub to fetch or close issues and pull requests, set or update labels, add comments, delete branches, etc.  
These operations are made in a very short period of time — because the action is very fast to run — and can be numerous based on your project action configuration and the quantity of issues and pull requests within it.  
GitHub has a [rate limit](https://docs.github.com/en/rest/overview/resources-in-the-rest-api#rate-limiting) and if reached will block these API calls for one hour (or API calls from other actions using the same user (a.k.a.: the github-token from the [repo-token](#repo-token) option)).  
This option helps you to stay within the GitHub rate limits, as you can use this option to limit the number of operations for a single run.

_Purpose:_  
This option aims to limit the number of operations made with the GitHub API to avoid reaching the [rate limit](https://docs.github.com/en/rest/overview/resources-in-the-rest-api#rate-limiting).

Based on your project, your GitHub business plan and the date of the cron job you set for this action, you can increase this limit to a higher number.
If you are not sure which is the right value for you or if the default value is good enough, you could enable the logs and look at the end of the stale action.  
If you reached the limit, you will see a warning message in the logs, telling you that you should increase the number of operations.
If you choose not to increase the limit, you might end up with unprocessed issues or pull requests after a stale action run.

When [debugging](#Debugging), you can set it to a much higher number like `1000` since there will be fewer operations made with the GitHub API.  
Only the [actor](#repo-token) and the batch of issues (100 per batch) will consume the operations.

Default value: `30`

#### remove-stale-when-updated

Automatically remove the stale label when the issues or the pull requests are updated (based on [GitHub issue](https://docs.github.com/en/rest/reference/issues) field `updated_at`) or commented.

Default value: `true`  
Required Permission: `issues: write` and `pull-requests: write`

#### remove-issue-stale-when-updated

Override [remove-stale-when-updated](#remove-stale-when-updated) but only to automatically remove the stale label when the issues are updated (based on [GitHub issue](https://docs.github.com/en/rest/reference/issues) field `updated_at`) or commented.

Default value: unset  
Required Permission: `issues: write`

#### remove-pr-stale-when-updated

Override [remove-stale-when-updated](#remove-stale-when-updated) but only to automatically remove the stale label when the pull requests are updated (based on [GitHub issue](https://docs.github.com/en/rest/reference/issues) field `updated_at`) or commented.

Default value: unset

#### labels-to-add-when-unstale

A comma delimited list of labels to add when a stale issue or pull request receives activity and has the [stale-issue-label](#stale-issue-label) or [stale-pr-label](#stale-pr-label) removed from it.

Default value: unset

#### labels-to-remove-when-stale

A comma delimited list of labels to remove when an issue or pull request becomes stale and has the [stale-issue-label](#stale-issue-label) or [stale-pr-label](#stale-pr-label) added to it.

Warning: each label results in a unique API call which can drastically consume the limit of [operations-per-run](#operations-per-run).

Default value: unset  
Required Permission: `pull-requests: write`

#### labels-to-remove-when-unstale

A comma delimited list of labels to remove when a stale issue or pull request receives activity and has the [stale-issue-label](#stale-issue-label) or [stale-pr-label](#stale-pr-label) removed from it.

Warning: each label results in a unique API call which can drastically consume the limit of [operations-per-run](#operations-per-run).

Default value: unset  
Required Permission: `pull-requests: write`

#### debug-only

Run the stale workflow as dry-run.  
No GitHub API calls that can alter your issues and pull requests will happen.  
Useful to debug or when you want to configure the stale workflow safely.

Default value: `false`

#### ascending

Change the order used to fetch the issues and pull requests from GitHub:

- `true` is for ascending.
- `false` is for descending.

It can be useful if your repository is processing so many issues and pull requests that you reach the [operations-per-run](#operations-per-run) limit.  
Based on the order, you could prefer to focus on the new content or on the old content of your repository.

Default value: `false`

#### start-date

The start date is used to ignore the issues and pull requests created before the start date.  
Particularly useful when you wish to add this stale workflow on an existing repository and only wish to stale the new issues and pull requests.

If set, the date must be formatted following the `ISO 8601` or `RFC 2822` standard.

Default value: unset

#### delete-branch

If set to `true`, the stale workflow will automatically delete the GitHub branches related to the pull requests automatically closed by the stale workflow.

Default value: `false`  
Required Permission: `pull-requests: write` and `contents: write`

#### exempt-milestones

A white-list of milestone(s) to only process the issues or the pull requests that does not contain one of these milestone(s).  
It can be a comma separated list of milestones (e.g: `V1,next`).

If unset (or an empty string), this option will not alter the stale workflow.

Default value: unset

#### exempt-issue-milestones

Override [exempt-milestones](#exempt-milestones) but only to process the issues that does not contain one of these milestone(s).

Default value: unset

#### exempt-pr-milestones

Override [exempt-milestones](#exempt-milestones) but only to process the pull requests that does not contain one of these milestone(s).

Default value: unset

#### exempt-all-milestones

If set to `true`, the issues or the pull requests with a milestone will not be marked as stale automatically.

Priority over [exempt-milestones](#exempt-milestones).

Default value: `false`

#### exempt-all-issue-milestones

Override [exempt-all-milestones](#exempt-all-milestones) but only to exempt the issues with a milestone to be marked as stale automatically.

Default value: unset

#### exempt-all-pr-milestones

Override [exempt-all-milestones](#exempt-all-milestones) but only to exempt the pull requests with a milestone to be marked as stale automatically.

Default value: unset

#### exempt-assignees

An allow-list of assignee(s) to only process the issues or the pull requests that does not contain one of these assignee(s).  
It can be a comma separated list of assignees (e.g: `marco,polo`).

If unset (or an empty string), this option will not alter the stale workflow.

Default value: unset

#### exempt-issue-assignees

Override [exempt-assignees](#exempt-assignees) but only to process the issues that does not contain one of these assignee(s).

Default value: unset

#### exempt-pr-assignees

Override [exempt-assignees](#exempt-assignees) but only to process the pull requests that does not contain one of these assignee(s).

Default value: unset

#### exempt-all-assignees

If set to `true`, the issues or the pull requests with an assignee will not be marked as stale automatically.

Priority over [exempt-assignees](#exempt-assignees).

Default value: `false`

#### exempt-all-issue-assignees

Override [exempt-all-assignees](#exempt-all-assignees) but only to exempt the issues with an assignee to be marked as stale automatically.

Default value: unset

#### exempt-all-pr-assignees

Override [exempt-all-assignees](#exempt-all-assignees) but only to exempt the pull requests with an assignee to be marked as stale automatically.

Default value: unset

#### exempt-draft-pr

If set to `true`, the pull requests currently in draft will not be marked as stale automatically.  
⚠️ This option consume one operation per pull request to process because we need to fetch the pull request with the GitHub API to know if it's a draft one or not.

Default value: `false`  
Required Permission: `pull-requests: read`

#### enable-statistics

Collects and display statistics at the end of the stale workflow logs to get a summary of what happened during the run.  
This option is only useful if the debug output secret `ACTIONS_STEP_DEBUG` is set to `true` in your repository to display the logs.

Default value: `true`

#### ignore-updates

The option [days-before-stale](#days-before-stale) will define the number of days before considering the issues or the pull requests as stale.  
In most cases, the purpose of this action is to only stale when necessary so if any update occurs or if a comment is added to them, the counter will restart.  
Nonetheless, if you don't care about this, and you prefer to stick to this number of days no matter the update, you can enable this option.  
Instead of comparing the number of days based on the [GitHub issue](https://docs.github.com/en/rest/reference/issues) field `updated_at`, it will be based on the [GitHub issue](https://docs.github.com/en/rest/reference/issues) field `created_at`.

Default value: `false`

#### ignore-issue-updates

Useful to override [ignore-updates](#ignore-updates) but only to ignore the updates for the issues.

Default value: unset

#### ignore-pr-updates

Useful to override [ignore-updates](#ignore-updates) but only to ignore the updates for the pull requests.

Default value: unset

#### include-only-assigned

If set to `true`, only the issues or the pull requests with an assignee will be marked as stale automatically.

Default value: `false`

#### sort-by

Useful to sort the issues and PRs by the specified field. It accepts `created`, `updated`, `comments`.

Default value: `created`

#### only-issue-types

A comma separated list of allowed issue types. Only issues with a matching type will be processed (e.g.: `bug,question`).

If unset (or an empty string), this option will not alter the stale workflow.

Default value: unset

### Usage

See also [action.yml](./action.yml) for a comprehensive list of all the options.

Basic:

```yaml
name: 'Close stale issues and PRs'
on:
  schedule:
    - cron: '30 1 * * *'

jobs:
  stale:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/stale@v10
        with:
          stale-issue-message: 'Message to comment on stale issues. If none provided, will not mark issues stale'
          stale-pr-message: 'Message to comment on stale PRs. If none provided, will not mark PRs stale'
```

Configure stale timeouts:

```yaml
name: 'Close stale issues and PRs'
on:
  schedule:
    - cron: '30 1 * * *'

jobs:
  stale:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/stale@v10
        with:
          stale-issue-message: 'This issue is stale because it has been open 30 days with no activity. Remove stale label or comment or this will be closed in 5 days.'
          days-before-stale: 30
          days-before-close: 5
```

Configure different stale timeouts but never close a PR:

```yaml
name: 'Close stale issues and PR'
on:
  schedule:
    - cron: '30 1 * * *'

jobs:
  stale:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/stale@v10
        with:
          stale-issue-message: 'This issue is stale because it has been open 30 days with no activity. Remove stale label or comment or this will be closed in 5 days.'
          stale-pr-message: 'This PR is stale because it has been open 45 days with no activity. Remove stale label or comment or this will be closed in 10 days.'
          close-issue-message: 'This issue was closed because it has been stalled for 5 days with no activity.'
          days-before-stale: 30
          days-before-close: 5
          days-before-pr-close: -1
```

Configure different stale timeouts:

```yaml
name: 'Close stale issues and PRs'
on:
  schedule:
    - cron: '30 1 * * *'

jobs:
  stale:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/stale@v10
        with:
          stale-issue-message: 'This issue is stale because it has been open 30 days with no activity. Remove stale label or comment or this will be closed in 5 days.'
          stale-pr-message: 'This PR is stale because it has been open 45 days with no activity. Remove stale label or comment or this will be closed in 10 days.'
          close-issue-message: 'This issue was closed because it has been stalled for 5 days with no activity.'
          close-pr-message: 'This PR was closed because it has been stalled for 10 days with no activity.'
          days-before-issue-stale: 30
          days-before-pr-stale: 45
          days-before-issue-close: 5
          days-before-pr-close: 10
```

Configure labels:

```yaml
name: 'Close stale issues and PRs'
on:
  schedule:
    - cron: '30 1 * * *'

jobs:
  stale:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/stale@v10
        with:
          stale-issue-message: 'Stale issue message'
          stale-pr-message: 'Stale pull request message'
          stale-issue-label: 'no-issue-activity'
          exempt-issue-labels: 'awaiting-approval,work-in-progress'
          stale-pr-label: 'no-pr-activity'
          exempt-pr-labels: 'awaiting-approval,work-in-progress'
          only-labels: 'awaiting-feedback,awaiting-answers'
```

Configure the stale action to only stale issue/PR created after the 18th april 2020:

```yaml
name: 'Close stale issues and PRs'
on:
  schedule:
    - cron: '30 1 * * *'

jobs:
  stale:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/stale@v10
        with:
          start-date: '2020-04-18T00:00:00Z' # ISO 8601 or RFC 2822
```

Avoid stale for specific milestones:

```yaml
name: 'Close stale issues and PRs'
on:
  schedule:
    - cron: '30 1 * * *'

jobs:
  stale:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/stale@v10
        with:
          exempt-issue-milestones: 'future,alpha,beta'
          exempt-pr-milestones: 'bugfix,improvement'
```

Avoid stale for all PR with milestones:

```yaml
name: 'Close stale issues and PRs'
on:
  schedule:
    - cron: '30 1 * * *'

jobs:
  stale:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/stale@v10
        with:
          exempt-all-pr-milestones: true
```

Check stale for specific labels:

```yaml
name: 'Close stale issues and PRs'
on:
  schedule:
    - cron: '30 1 * * *'

jobs:
  stale:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/stale@v10
        with:
          any-of-labels: 'needs-more-info,needs-demo'
          # You can opt for 'only-labels' instead if your use-case requires all labels
          # to be present in the issue/PR
```

Avoid stale for specific assignees:

```yaml
name: 'Close stale issues and PRs'
on:
  schedule:
    - cron: '30 1 * * *'

jobs:
  stale:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/stale@v10
        with:
          exempt-issue-assignees: 'marco,polo'
          exempt-pr-assignees: 'marco'
```

Avoid stale for all PR with assignees:

```yaml
name: 'Close stale issues and PRs'
on:
  schedule:
    - cron: '30 1 * * *'

jobs:
  stale:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/stale@v10
        with:
          exempt-all-pr-assignees: true
```

### Debugging

**Logs:**  
To see the debug output from this action, you must set the secret `ACTIONS_STEP_DEBUG` to `true` in your repository.  
There are many logs, so this can be very helpful!

**Statistics:**  
If the logs are enabled, you can also enable the statistics log which will be visible at the end of the logs once all issues were processed.  
This is very helpful to have a quick understanding of the whole stale workflow.  
Set `enable-statistics` to `true` in your workflow configuration file.

**Dry-run:**  
You can run this action in debug only mode (no actions will be taken on your issues and pull requests) by passing `debug-only` to `true` as an argument to the action.

**More operations:**  
You can increase the maximum number of operations per run by passing `operations-per-run` to `1000` for example which will help you to handle more operations in a single stale workflow run.  
If the `debug-only` option is enabled, this is very helpful because the workflow will (almost) never reach the GitHub API rate, and you will be able to deep-dive into the logs.

**Job frequency:**  
You could change the cron job frequency in the stale workflow to run the stale workflow more often.  
Usually, this is not very helpful though.

### Contributing

We welcome contributions!
Please read the [contributing](CONTRIBUTING.md) file before starting your work.
```

## File: `action.yml`
```yaml
name: 'Close Stale Issues'
description: 'Close issues and pull requests with no recent activity'
author: 'GitHub'
inputs:
  repo-token:
    description: 'Token for the repository. Can be passed in using `{{ secrets.GITHUB_TOKEN }}`.'
    required: false
    default: ${{ github.token }}
  stale-issue-message:
    description: 'The message to post on the issue when tagging it. If none provided, will not mark issues stale.'
    required: false
  stale-pr-message:
    description: 'The message to post on the pull request when tagging it. If none provided, will not mark pull requests stale.'
    required: false
  close-issue-message:
    description: 'The message to post on the issue when closing it. If none provided, will not comment when closing an issue.'
    required: false
  close-pr-message:
    description: 'The message to post on the pull request when closing it. If none provided, will not comment when closing a pull requests.'
    required: false
  days-before-stale:
    description: 'The number of days old an issue or a pull request can be before marking it stale. Set to -1 to never mark issues or pull requests as stale automatically.'
    required: false
    default: '60'
  days-before-issue-stale:
    description: 'The number of days old an issue can be before marking it stale. Set to -1 to never mark issues as stale automatically. Override "days-before-stale" option regarding only the issues.'
    required: false
  days-before-pr-stale:
    description: 'The number of days old a pull request can be before marking it stale. Set to -1 to never mark pull requests as stale automatically. Override "days-before-stale" option regarding only the pull requests.'
    required: false
  days-before-close:
    description: 'The number of days to wait to close an issue or a pull request after it being marked stale. Set to -1 to never close stale issues or pull requests.'
    required: false
    default: '7'
  days-before-issue-close:
    description: 'The number of days to wait to close an issue after it being marked stale. Set to -1 to never close stale issues. Override "days-before-close" option regarding only the issues.'
    required: false
  days-before-pr-close:
    description: 'The number of days to wait to close a pull request after it being marked stale. Set to -1 to never close stale pull requests. Override "days-before-close" option regarding only the pull requests.'
    required: false
  stale-issue-label:
    description: 'The label to apply when an issue is stale.'
    required: false
    default: 'Stale'
  close-issue-label:
    description: 'The label to apply when an issue is closed.'
    required: false
  exempt-issue-labels:
    description: 'The labels that mean an issue is exempt from being marked stale. Separate multiple labels with commas (eg. "label1,label2").'
    default: ''
    required: false
  close-issue-reason:
    description: 'The reason to use when closing an issue.'
    default: 'not_planned'
    required: false
  stale-pr-label:
    description: 'The label to apply when a pull request is stale.'
    default: 'Stale'
    required: false
  close-pr-label:
    description: 'The label to apply when a pull request is closed.'
    required: false
  exempt-pr-labels:
    description: 'The labels that mean a pull request is exempt from being marked as stale. Separate multiple labels with commas (eg. "label1,label2").'
    default: ''
    required: false
  exempt-milestones:
    description: 'The milestones that mean an issue or a pull request is exempt from being marked as stale. Separate multiple milestones with commas (eg. "milestone1,milestone2").'
    default: ''
    required: false
  exempt-issue-milestones:
    description: 'The milestones that mean an issue is exempt from being marked as stale. Separate multiple milestones with commas (eg. "milestone1,milestone2"). Override "exempt-milestones" option regarding only the issues.'
    default: ''
    required: false
  exempt-pr-milestones:
    description: 'The milestones that mean a pull request is exempt from being marked as stale. Separate multiple milestones with commas (eg. "milestone1,milestone2"). Override "exempt-milestones" option regarding only the pull requests.'
    default: ''
    required: false
  exempt-all-milestones:
    description: 'Exempt all issues and pull requests with milestones from being marked as stale. Default to false.'
    default: 'false'
    required: false
  exempt-all-issue-milestones:
    description: 'Exempt all issues with milestones from being marked as stale. Override "exempt-all-milestones" option regarding only the issues.'
    default: ''
    required: false
  exempt-all-pr-milestones:
    description: 'Exempt all pull requests with milestones from being marked as stale. Override "exempt-all-milestones" option regarding only the pull requests.'
    default: ''
    required: false
  only-labels:
    description: 'Only issues or pull requests with all of these labels are checked if stale. Defaults to `` (disabled) and can be a comma-separated list of labels.'
    default: ''
    required: false
  any-of-labels:
    description: 'Only issues or pull requests with at least one of these labels are checked if stale. Defaults to `` (disabled) and can be a comma-separated list of labels.'
    default: ''
    required: false
  any-of-issue-labels:
    description: 'Only issues with at least one of these labels are checked if stale. Defaults to `` (disabled) and can be a comma-separated list of labels. Override "any-of-labels" option regarding only the issues.'
    default: ''
    required: false
  any-of-pr-labels:
    description: 'Only pull requests with at least one of these labels are checked if stale. Defaults to `` (disabled) and can be a comma-separated list of labels. Override "any-of-labels" option regarding only the pull requests.'
    default: ''
    required: false
  only-issue-labels:
    description: 'Only issues with all of these labels are checked if stale. Defaults to `[]` (disabled) and can be a comma-separated list of labels. Override "only-labels" option regarding only the issues.'
    default: ''
    required: false
  only-pr-labels:
    description: 'Only pull requests with all of these labels are checked if stale. Defaults to `[]` (disabled) and can be a comma-separated list of labels. Override "only-labels" option regarding only the pull requests.'
    default: ''
    required: false
  operations-per-run:
    description: 'The maximum number of operations per run, used to control rate limiting (GitHub API CRUD related).'
    default: '30'
    required: false
  remove-stale-when-updated:
    description: 'Remove stale labels from issues and pull requests when they are updated or commented on.'
    default: 'true'
    required: false
  remove-issue-stale-when-updated:
    description: 'Remove stale labels from issues when they are updated or commented on. Override "remove-stale-when-updated" option regarding only the issues.'
    default: ''
    required: false
  remove-pr-stale-when-updated:
    description: 'Remove stale labels from pull requests when they are updated or commented on. Override "remove-stale-when-updated" option regarding only the pull requests.'
    default: ''
    required: false
  debug-only:
    description: 'Run the processor in debug mode without actually performing any operations on live issues.'
    default: 'false'
    required: false
  ascending:
    description: 'The order to get issues or pull requests. Defaults to false, which is descending.'
    default: 'false'
    required: false
  sort-by:
    description: 'What to sort results by. Valid options are `created`, `updated`, and `comments`. Defaults to `created`.'
    default: 'created'
    required: false
  delete-branch:
    description: 'Delete the git branch after closing a stale pull request.'
    default: 'false'
    required: false
  start-date:
    description: 'The date used to skip the stale action on issue/pull request created before it (ISO 8601 or RFC 2822).'
    default: ''
    required: false
  exempt-assignees:
    description: 'The assignees which exempt an issue or a pull request from being marked as stale. Separate multiple assignees with commas (eg. "user1,user2").'
    default: ''
    required: false
  exempt-issue-assignees:
    description: 'The assignees which exempt an issue from being marked as stale. Separate multiple assignees with commas (eg. "user1,user2"). Override "exempt-assignees" option regarding only the issues.'
    default: ''
    required: false
  exempt-pr-assignees:
    description: 'The assignees which exempt a pull request from being marked as stale. Separate multiple assignees with commas (eg. "user1,user2"). Override "exempt-assignees" option regarding only the pull requests.'
    default: ''
    required: false
  exempt-all-assignees:
    description: 'Exempt all issues and pull requests with assignees from being marked as stale. Default to false.'
    default: 'false'
    required: false
  exempt-all-issue-assignees:
    description: 'Exempt all issues with assignees from being marked as stale. Override "exempt-all-assignees" option regarding only the issues.'
    default: ''
    required: false
  exempt-all-pr-assignees:
    description: 'Exempt all pull requests with assignees from being marked as stale. Override "exempt-all-assignees" option regarding only the pull requests.'
    default: ''
    required: false
  exempt-draft-pr:
    description: 'Exempt draft pull requests from being marked as stale. Default to false.'
    default: 'false'
    required: false
  enable-statistics:
    description: 'Display some statistics at the end regarding the stale workflow (only when the logs are enabled).'
    default: 'true'
    required: false
  labels-to-add-when-unstale:
    description: 'A comma delimited list of labels to add when an issue or pull request becomes unstale.'
    default: ''
    required: false
  labels-to-remove-when-stale:
    description: 'A comma delimited list of labels to remove when an issue or pull request becomes stale.'
    default: ''
    required: false
  labels-to-remove-when-unstale:
    description: 'A comma delimited list of labels to remove when an issue or pull request becomes unstale.'
    default: ''
    required: false
  ignore-updates:
    description: 'Any update (update/comment) can reset the stale idle time on the issues and pull requests.'
    default: 'false'
    required: false
  ignore-issue-updates:
    description: 'Any update (update/comment) can reset the stale idle time on the issues. Override "ignore-updates" option regarding only the issues.'
    default: ''
    required: false
  ignore-pr-updates:
    description: 'Any update (update/comment) can reset the stale idle time on the pull requests. Override "ignore-updates" option regarding only the pull requests.'
    default: ''
    required: false
  include-only-assigned:
    description: 'Only the issues or the pull requests with an assignee will be marked as stale automatically.'
    default: 'false'
    required: false
  only-issue-types:
    description: 'Only issues with a matching type are processed as stale/closed. Defaults to `[]` (disabled) and can be a comma-separated list of issue types.'
    default: ''
    required: false
outputs:
  closed-issues-prs:
    description: 'List of all closed issues and pull requests.'
  staled-issues-prs:
    description: 'List of all staled issues and pull requests.'
runs:
  using: 'node24'
  main: 'dist/index.js'
```

## File: `jest.config.js`
```javascript
module.exports = {
  clearMocks: true,
  moduleFileExtensions: ['js', 'ts'],
  testEnvironment: 'node',
  testMatch: ['**/*.test.ts', '**/*.spec.ts'],
  testRunner: 'jest-circus/runner',
  transform: {
    '^.+\\.ts$': 'ts-jest'
  },
  verbose: true
};
```

## File: `package.json`
```json
{
  "name": "stale-action",
  "version": "10.0.0",
  "private": true,
  "description": "Marks old issues and PRs as stale",
  "main": "lib/main.js",
  "scripts": {
    "build": "tsc --project tsconfig.app.json && ncc build",
    "format": "prettier --no-error-on-unmatched-pattern --config  ./.prettierrc.js --write \"**/*.{ts,yml,yaml}\"",
    "format-check": "prettier --no-error-on-unmatched-pattern --config ./.prettierrc.js --check \"**/*.{ts,yml,yaml}\"",
    "lint": "eslint --config ./.eslintrc.js \"**/*.ts\"",
    "lint:fix": "eslint --config ./.eslintrc.js \"**/*.ts\" --fix",
    "lint:all": "npm run format-check && npm run lint",
    "lint:all:fix": "npm run format && npm run lint:fix",
    "test": "jest --config ./jest.config.js",
    "test:only-errors": "jest --reporters jest-silent-reporter --silent",
    "test:watch": "jest --watch --notify --expand",
    "all": "npm run format && npm run lint && npm run build && npm test",
    "all:ci": "npm run format && npm run lint && npm run build && npm run test:only-errors",
    "prerelease": "npm run build",
    "release": "standard-version",
    "release:dry-run": "standard-version --dry-run"
  },
  "repository": {
    "type": "git",
    "url": "git+https://github.com/actions/stale.git"
  },
  "keywords": [
    "actions",
    "node",
    "stale"
  ],
  "engines": {
    "node": "24",
    "npm": ">=7.0.0"
  },
  "author": "GitHub",
  "license": "MIT",
  "dependencies": {
    "@actions/cache": "^5.0.2",
    "@actions/core": "^1.11.1",
    "@actions/github": "^7.0.0",
    "@octokit/core": "^5.2.0",
    "@octokit/plugin-retry": "^4.1.1",
    "lodash.deburr": "^4.1.0",
    "semver": "^7.5.4"
  },
  "devDependencies": {
    "@types/jest": "^29.5.14",
    "@types/lodash.deburr": "^4.1.6",
    "@types/node": "^24.3.1",
    "@types/semver": "^7.5.0",
    "@typescript-eslint/eslint-plugin": "^6.2.1",
    "@typescript-eslint/parser": "^6.2.1",
    "@vercel/ncc": "^0.36.1",
    "ansi-styles": "5.2.0",
    "eslint": "^8.46.0",
    "eslint-config-prettier": "^10.1.8",
    "eslint-plugin-jest": "^27.2.3",
    "eslint-plugin-node": "^11.1.0",
    "jest": "^29.6.2",
    "jest-circus": "^29.5.0",
    "jest-silent-reporter": "^0.5.0",
    "js-yaml": "^4.1.1",
    "prettier": "^2.8.7",
    "standard-version": "^9.3.1",
    "terminal-link": "^2.1.1",
    "ts-jest": "^29.2.5",
    "typescript": "^5.2.2"
  }
}
```

## File: `tsconfig.app.json`
```json
{
  "extends": "./tsconfig.json",
  "exclude": ["node_modules", "**/*.spec.ts"],
  "include": ["src"]
}
```

## File: `tsconfig.json`
```json
{
  "compilerOptions": {
    "target": "es6" /* Specify ECMAScript target version: 'ES3' (default), 'ES5', 'ES2015', 'ES2016', 'ES2017', 'ES2018', 'ES2019' or 'ESNEXT'. */,
    "module": "commonjs" /* Specify module code generation: 'none', 'commonjs', 'amd', 'system', 'umd', 'es2015', or 'ESNext'. */,
    "outDir": "./lib" /* Redirect output structure to the directory. */,
    "strict": true /* Enable all strict type-checking options. */,
    "noImplicitAny": true /* Raise error on expressions and declarations with an implied 'any' type. */,
    "esModuleInterop": true /* Enables emit interoperability between CommonJS and ES Modules via creation of namespace objects for all imports. Implies 'allowSyntheticDefaultImports'. */,
    "useUnknownInCatchVariables": false /* Default catch clause variables as 'unknown' instead of 'any'. */
    //"sourceMap": true
  },
  "include": ["src", "__tests__"]
}
```

## File: `tsconfig.spec.json`
```json
{
  "extends": "./tsconfig.json",
  "include": ["src", "__tests__"],
  "exclude": ["node_modules"]
}
```

## File: `__tests__/any-of-labels.spec.ts`
```typescript
import {Issue} from '../src/classes/issue';
import {IIssue} from '../src/interfaces/issue';
import {IIssuesProcessorOptions} from '../src/interfaces/issues-processor-options';
import {IssuesProcessorMock} from './classes/issues-processor-mock';
import {DefaultProcessorOptions} from './constants/default-processor-options';
import {generateIssue} from './functions/generate-issue';
import {StateMock} from './classes/state-mock';

let issuesProcessorBuilder: IssuesProcessorBuilder;
let issuesProcessor: IssuesProcessorMock;

describe('any-of-labels options', (): void => {
  beforeEach((): void => {
    issuesProcessorBuilder = new IssuesProcessorBuilder();
  });

  test('should stale when not set even if the issue has no label', async (): Promise<void> => {
    expect.assertions(1);
    issuesProcessor = issuesProcessorBuilder
      .emptyAnyOfLabels()
      .issuesOrPrs([{labels: []}])
      .build();

    await issuesProcessor.processIssues();

    expect(issuesProcessor.staleIssues).toHaveLength(1);
  });

  test('should stale when not set even if the issue has a label', async (): Promise<void> => {
    expect.assertions(1);
    issuesProcessor = issuesProcessorBuilder
      .emptyAnyOfLabels()
      .issuesOrPrs([{labels: [{name: 'label'}]}])
      .build();

    await issuesProcessor.processIssues();

    expect(issuesProcessor.staleIssues).toHaveLength(1);
  });

  test('should not stale when set and the issue has no label', async (): Promise<void> => {
    expect.assertions(1);
    issuesProcessor = issuesProcessorBuilder
      .anyOfLabels('dummy-label')
      .issuesOrPrs([{labels: []}])
      .build();

    await issuesProcessor.processIssues();

    expect(issuesProcessor.staleIssues).toHaveLength(0);
  });

  test('should not stale when set and the issue has a different label', async (): Promise<void> => {
    expect.assertions(1);
    issuesProcessor = issuesProcessorBuilder
      .anyOfLabels('dummy-label')
      .issuesOrPrs([
        {
          labels: [
            {
              name: 'label'
            }
          ]
        }
      ])
      .build();

    await issuesProcessor.processIssues();

    expect(issuesProcessor.staleIssues).toHaveLength(0);
  });

  test('should not stale when set and the issue has different labels', async (): Promise<void> => {
    expect.assertions(1);
    issuesProcessor = issuesProcessorBuilder
      .anyOfLabels('dummy-label')
      .issuesOrPrs([
        {
          labels: [
            {
              name: 'label-1'
            },
            {
              name: 'label-2'
            }
          ]
        }
      ])
      .build();

    await issuesProcessor.processIssues();

    expect(issuesProcessor.staleIssues).toHaveLength(0);
  });

  test('should stale when set and the issue has the same label', async (): Promise<void> => {
    expect.assertions(1);
    issuesProcessor = issuesProcessorBuilder
      .anyOfLabels('dummy-label')
      .issuesOrPrs([
        {
          labels: [
            {
              name: 'dummy-label'
            }
          ]
        }
      ])
      .build();

    await issuesProcessor.processIssues();

    expect(issuesProcessor.staleIssues).toHaveLength(1);
  });

  test('should stale when set and the issue has only one of the same label', async (): Promise<void> => {
    expect.assertions(1);
    issuesProcessor = issuesProcessorBuilder
      .anyOfLabels('dummy-label-1,dummy-label-2')
      .issuesOrPrs([
        {
          labels: [
            {
              name: 'dummy-label-1'
            }
          ]
        }
      ])
      .build();

    await issuesProcessor.processIssues();

    expect(issuesProcessor.staleIssues).toHaveLength(1);
  });

  test('should stale when set and the issue has all the same labels', async (): Promise<void> => {
    expect.assertions(1);
    issuesProcessor = issuesProcessorBuilder
      .anyOfLabels('dummy-label-1,dummy-label-2')
      .issuesOrPrs([
        {
          labels: [
            {
              name: 'dummy-label-1'
            },
            {
              name: 'dummy-label-2'
            }
          ]
        }
      ])
      .build();

    await issuesProcessor.processIssues();

    expect(issuesProcessor.staleIssues).toHaveLength(1);
  });
});

describe('any-of-issue-labels option', (): void => {
  beforeEach((): void => {
    issuesProcessorBuilder = new IssuesProcessorBuilder();
  });

  describe('when the any-of-labels options is not set', (): void => {
    beforeEach((): void => {
      issuesProcessorBuilder.emptyAnyOfLabels();
    });

    test('should stale when not set even if the issue has no label', async (): Promise<void> => {
      expect.assertions(1);
      issuesProcessor = issuesProcessorBuilder
        .emptyAnyOfIssueLabels()
        .issues([{labels: []}])
        .build();

      await issuesProcessor.processIssues();

      expect(issuesProcessor.staleIssues).toHaveLength(1);
    });

    test('should stale when not set even if the issue has a label', async (): Promise<void> => {
      expect.assertions(1);
      issuesProcessor = issuesProcessorBuilder
        .emptyAnyOfIssueLabels()
        .issues([{labels: [{name: 'dummy-label'}]}])
        .build();

      await issuesProcessor.processIssues();

      expect(issuesProcessor.staleIssues).toHaveLength(1);
    });

    test('should not stale when set and the issue has no label', async (): Promise<void> => {
      expect.assertions(1);
      issuesProcessor = issuesProcessorBuilder
        .anyOfIssueLabels('dummy-label')
        .issues([{labels: []}])
        .build();

      await issuesProcessor.processIssues();

      expect(issuesProcessor.staleIssues).toHaveLength(0);
    });

    test('should not stale when set and the issue has a different label', async (): Promise<void> => {
      expect.assertions(1);
      issuesProcessor = issuesProcessorBuilder
        .anyOfIssueLabels('dummy-label')
        .issues([
          {
            labels: [
              {
                name: 'label'
              }
            ]
          }
        ])
        .build();

      await issuesProcessor.processIssues();

      expect(issuesProcessor.staleIssues).toHaveLength(0);
    });

    test('should not stale when set and the issue has different labels', async (): Promise<void> => {
      expect.assertions(1);
      issuesProcessor = issuesProcessorBuilder
        .anyOfIssueLabels('dummy-label')
        .issues([
          {
            labels: [
              {
                name: 'label-1'
              },
              {
                name: 'label-2'
              }
            ]
          }
        ])
        .build();

      await issuesProcessor.processIssues();

      expect(issuesProcessor.staleIssues).toHaveLength(0);
    });

    test('should stale when set and the issue has the same label', async (): Promise<void> => {
      expect.assertions(1);
      issuesProcessor = issuesProcessorBuilder
        .anyOfIssueLabels('dummy-label')
        .issues([
          {
            labels: [
              {
                name: 'dummy-label'
              }
            ]
          }
        ])
        .build();

      await issuesProcessor.processIssues();

      expect(issuesProcessor.staleIssues).toHaveLength(1);
    });

    test('should stale when set and the issue has only one of the same label', async (): Promise<void> => {
      expect.assertions(1);
      issuesProcessor = issuesProcessorBuilder
        .anyOfIssueLabels('dummy-label-1,dummy-label-2')
        .issues([
          {
            labels: [
              {
                name: 'dummy-label-1'
              }
            ]
          }
        ])
        .build();

      await issuesProcessor.processIssues();

      expect(issuesProcessor.staleIssues).toHaveLength(1);
    });

    test('should stale when set and the issue has all the same labels', async (): Promise<void> => {
      expect.assertions(1);
      issuesProcessor = issuesProcessorBuilder
        .anyOfIssueLabels('dummy-label-1,dummy-label-2')
        .issues([
          {
            labels: [
              {
                name: 'dummy-label-1'
              },
              {
                name: 'dummy-label-2'
              }
            ]
          }
        ])
        .build();

      await issuesProcessor.processIssues();

      expect(issuesProcessor.staleIssues).toHaveLength(1);
    });
  });

  describe('when the any-of-labels options is set (same as any-of-issue-labels)', (): void => {
    beforeEach((): void => {
      issuesProcessorBuilder.anyOfLabels('dummy-label');
    });

    test('should not stale when not set even if the issue has no label', async (): Promise<void> => {
      expect.assertions(1);
      issuesProcessor = issuesProcessorBuilder
        .emptyAnyOfIssueLabels()
        .issues([{labels: []}])
        .build();

      await issuesProcessor.processIssues();

      expect(issuesProcessor.staleIssues).toHaveLength(0);
    });

    test('should not stale when not set even if the issue has a label', async (): Promise<void> => {
      expect.assertions(1);
      issuesProcessor = issuesProcessorBuilder
        .emptyAnyOfIssueLabels()
        .issues([{labels: [{name: 'label'}]}])
        .build();

      await issuesProcessor.processIssues();

      expect(issuesProcessor.staleIssues).toHaveLength(0);
    });

    test('should not stale when set and the issue has no label', async (): Promise<void> => {
      expect.assertions(1);
      issuesProcessor = issuesProcessorBuilder
        .anyOfIssueLabels('dummy-label')
        .issues([{labels: []}])
        .build();

      await issuesProcessor.processIssues();

      expect(issuesProcessor.staleIssues).toHaveLength(0);
    });

    test('should not stale when set and the issue has a different label', async (): Promise<void> => {
      expect.assertions(1);
      issuesProcessor = issuesProcessorBuilder
        .anyOfIssueLabels('dummy-label')
        .issues([
          {
            labels: [
              {
                name: 'label'
              }
            ]
          }
        ])
        .build();

      await issuesProcessor.processIssues();

      expect(issuesProcessor.staleIssues).toHaveLength(0);
    });

    test('should not stale when set and the issue has different labels', async (): Promise<void> => {
      expect.assertions(1);
      issuesProcessor = issuesProcessorBuilder
        .anyOfIssueLabels('dummy-label')
        .issues([
          {
            labels: [
              {
                name: 'label-1'
              },
              {
                name: 'label-2'
              }
            ]
          }
        ])
        .build();

      await issuesProcessor.processIssues();

      expect(issuesProcessor.staleIssues).toHaveLength(0);
    });

    test('should stale when set and the issue has the same label', async (): Promise<void> => {
      expect.assertions(1);
      issuesProcessor = issuesProcessorBuilder
        .anyOfIssueLabels('dummy-label')
        .issues([
          {
            labels: [
              {
                name: 'dummy-label'
              }
            ]
          }
        ])
        .build();

      await issuesProcessor.processIssues();

      expect(issuesProcessor.staleIssues).toHaveLength(1);
    });

    test('should stale when set and the issue has only one of the same label', async (): Promise<void> => {
      expect.assertions(1);
      issuesProcessor = issuesProcessorBuilder
        .anyOfIssueLabels('dummy-label-1,dummy-label-2')
        .issues([
          {
            labels: [
              {
                name: 'dummy-label-1'
              }
            ]
          }
        ])
        .build();

      await issuesProcessor.processIssues();

      expect(issuesProcessor.staleIssues).toHaveLength(1);
    });

    test('should stale when set and the issue has all the same labels', async (): Promise<void> => {
      expect.assertions(1);
      issuesProcessor = issuesProcessorBuilder
        .anyOfIssueLabels('dummy-label-1,dummy-label-2')
        .issues([
          {
            labels: [
              {
                name: 'dummy-label-1'
              },
              {
                name: 'dummy-label-2'
              }
            ]
          }
        ])
        .build();

      await issuesProcessor.processIssues();

      expect(issuesProcessor.staleIssues).toHaveLength(1);
    });
  });

  describe('when the any-of-labels options is set (different than any-of-issue-labels)', (): void => {
    beforeEach((): void => {
      issuesProcessorBuilder.anyOfLabels('dummy-any-of-label');
    });

    test('should not stale when not set even if the issue has no label', async (): Promise<void> => {
      expect.assertions(1);
      issuesProcessor = issuesProcessorBuilder
        .emptyAnyOfIssueLabels()
        .issues([{labels: []}])
        .build();

      await issuesProcessor.processIssues();

      expect(issuesProcessor.staleIssues).toHaveLength(0);
    });

    test('should not stale when not set even if the issue has a label', async (): Promise<void> => {
      expect.assertions(1);
      issuesProcessor = issuesProcessorBuilder
        .emptyAnyOfIssueLabels()
        .issues([{labels: [{name: 'label'}]}])
        .build();

      await issuesProcessor.processIssues();

      expect(issuesProcessor.staleIssues).toHaveLength(0);
    });

    test('should not stale when set and the issue has no label', async (): Promise<void> => {
      expect.assertions(1);
      issuesProcessor = issuesProcessorBuilder
        .anyOfIssueLabels('dummy-label')
        .issues([{labels: []}])
        .build();

      await issuesProcessor.processIssues();

      expect(issuesProcessor.staleIssues).toHaveLength(0);
    });

    test('should not stale when set and the issue has a different label', async (): Promise<void> => {
      expect.assertions(1);
      issuesProcessor = issuesProcessorBuilder
        .anyOfIssueLabels('dummy-label')
        .issues([
          {
            labels: [
              {
                name: 'label'
              }
            ]
          }
        ])
        .build();

      await issuesProcessor.processIssues();

      expect(issuesProcessor.staleIssues).toHaveLength(0);
    });

    test('should not stale when set and the issue has different labels', async (): Promise<void> => {
      expect.assertions(1);
      issuesProcessor = issuesProcessorBuilder
        .anyOfIssueLabels('dummy-label')
        .issues([
          {
            labels: [
              {
                name: 'label-1'
              },
              {
                name: 'label-2'
              }
            ]
          }
        ])
        .build();

      await issuesProcessor.processIssues();

      expect(issuesProcessor.staleIssues).toHaveLength(0);
    });

    test('should stale when set and the issue has the same label', async (): Promise<void> => {
      expect.assertions(1);
      issuesProcessor = issuesProcessorBuilder
        .anyOfIssueLabels('dummy-label')
        .issues([
          {
            labels: [
              {
                name: 'dummy-label'
              }
            ]
          }
        ])
        .build();

      await issuesProcessor.processIssues();

      expect(issuesProcessor.staleIssues).toHaveLength(1);
    });

    test('should stale when set and the issue has only one of the same label', async (): Promise<void> => {
      expect.assertions(1);
      issuesProcessor = issuesProcessorBuilder
        .anyOfIssueLabels('dummy-label-1,dummy-label-2')
        .issues([
          {
            labels: [
              {
                name: 'dummy-label-1'
              }
            ]
          }
        ])
        .build();

      await issuesProcessor.processIssues();

      expect(issuesProcessor.staleIssues).toHaveLength(1);
    });

    test('should stale when set and the issue has all the same labels', async (): Promise<void> => {
      expect.assertions(1);
      issuesProcessor = issuesProcessorBuilder
        .anyOfIssueLabels('dummy-label-1,dummy-label-2')
        .issues([
          {
            labels: [
              {
                name: 'dummy-label-1'
              },
              {
                name: 'dummy-label-2'
              }
            ]
          }
        ])
        .build();

      await issuesProcessor.processIssues();

      expect(issuesProcessor.staleIssues).toHaveLength(1);
    });
  });
});

describe('any-of-pr-labels option', (): void => {
  beforeEach((): void => {
    issuesProcessorBuilder = new IssuesProcessorBuilder();
  });

  describe('when the any-of-labels options is not set', (): void => {
    beforeEach((): void => {
      issuesProcessorBuilder.emptyAnyOfLabels();
    });

    test('should stale when not set even if the pr has no label', async (): Promise<void> => {
      expect.assertions(1);
      issuesProcessor = issuesProcessorBuilder
        .emptyAnyOfPrLabels()
        .prs([{labels: []}])
        .build();

      await issuesProcessor.processIssues();

      expect(issuesProcessor.staleIssues).toHaveLength(1);
    });

    test('should stale when not set even if the pr has a label', async (): Promise<void> => {
      expect.assertions(1);
      issuesProcessor = issuesProcessorBuilder
        .emptyAnyOfPrLabels()
        .prs([{labels: [{name: 'dummy-label'}]}])
        .build();

      await issuesProcessor.processIssues();

      expect(issuesProcessor.staleIssues).toHaveLength(1);
    });

    test('should not stale when set and the pr has no label', async (): Promise<void> => {
      expect.assertions(1);
      issuesProcessor = issuesProcessorBuilder
        .anyOfPrLabels('dummy-label')
        .prs([{labels: []}])
        .build();

      await issuesProcessor.processIssues();

      expect(issuesProcessor.staleIssues).toHaveLength(0);
    });

    test('should not stale when set and the pr has a different label', async (): Promise<void> => {
      expect.assertions(1);
      issuesProcessor = issuesProcessorBuilder
        .anyOfPrLabels('dummy-label')
        .prs([
          {
            labels: [
              {
                name: 'label'
              }
            ]
          }
        ])
        .build();

      await issuesProcessor.processIssues();

      expect(issuesProcessor.staleIssues).toHaveLength(0);
    });

    test('should not stale when set and the pr has different labels', async (): Promise<void> => {
      expect.assertions(1);
      issuesProcessor = issuesProcessorBuilder
        .anyOfPrLabels('dummy-label')
        .prs([
          {
            labels: [
              {
                name: 'label-1'
              },
              {
                name: 'label-2'
              }
            ]
          }
        ])
        .build();

      await issuesProcessor.processIssues();

      expect(issuesProcessor.staleIssues).toHaveLength(0);
    });

    test('should stale when set and the pr has the same label', async (): Promise<void> => {
      expect.assertions(1);
      issuesProcessor = issuesProcessorBuilder
        .anyOfPrLabels('dummy-label')
        .prs([
          {
            labels: [
              {
                name: 'dummy-label'
              }
            ]
          }
        ])
        .build();

      await issuesProcessor.processIssues();

      expect(issuesProcessor.staleIssues).toHaveLength(1);
    });

    test('should stale when set and the pr has only one of the same label', async (): Promise<void> => {
      expect.assertions(1);
      issuesProcessor = issuesProcessorBuilder
        .anyOfPrLabels('dummy-label-1,dummy-label-2')
        .prs([
          {
            labels: [
              {
                name: 'dummy-label-1'
              }
            ]
          }
        ])
        .build();

      await issuesProcessor.processIssues();

      expect(issuesProcessor.staleIssues).toHaveLength(1);
    });

    test('should stale when set and the pr has all the same labels', async (): Promise<void> => {
      expect.assertions(1);
      issuesProcessor = issuesProcessorBuilder
        .anyOfPrLabels('dummy-label-1,dummy-label-2')
        .prs([
          {
            labels: [
              {
                name: 'dummy-label-1'
              },
              {
                name: 'dummy-label-2'
              }
            ]
          }
        ])
        .build();

      await issuesProcessor.processIssues();

      expect(issuesProcessor.staleIssues).toHaveLength(1);
    });
  });

  describe('when the any-of-labels options is set (same as any-of-pr-labels)', (): void => {
    beforeEach((): void => {
      issuesProcessorBuilder.anyOfLabels('dummy-label');
    });

    test('should not stale when not set even if the pr has no label', async (): Promise<void> => {
      expect.assertions(1);
      issuesProcessor = issuesProcessorBuilder
        .emptyAnyOfPrLabels()
        .prs([{labels: []}])
        .build();

      await issuesProcessor.processIssues();

      expect(issuesProcessor.staleIssues).toHaveLength(0);
    });

    test('should not stale when not set even if the pr has a label', async (): Promise<void> => {
      expect.assertions(1);
      issuesProcessor = issuesProcessorBuilder
        .emptyAnyOfPrLabels()
        .prs([{labels: [{name: 'label'}]}])
        .build();

      await issuesProcessor.processIssues();

      expect(issuesProcessor.staleIssues).toHaveLength(0);
    });

    test('should not stale when set and the pr has no label', async (): Promise<void> => {
      expect.assertions(1);
      issuesProcessor = issuesProcessorBuilder
        .anyOfPrLabels('dummy-label')
        .prs([{labels: []}])
        .build();

      await issuesProcessor.processIssues();

      expect(issuesProcessor.staleIssues).toHaveLength(0);
    });

    test('should not stale when set and the pr has a different label', async (): Promise<void> => {
      expect.assertions(1);
      issuesProcessor = issuesProcessorBuilder
        .anyOfPrLabels('dummy-label')
        .prs([
          {
            labels: [
              {
                name: 'label'
              }
            ]
          }
        ])
        .build();

      await issuesProcessor.processIssues();

      expect(issuesProcessor.staleIssues).toHaveLength(0);
    });

    test('should not stale when set and the pr has different labels', async (): Promise<void> => {
      expect.assertions(1);
      issuesProcessor = issuesProcessorBuilder
        .anyOfPrLabels('dummy-label')
        .prs([
          {
            labels: [
              {
                name: 'label-1'
              },
              {
                name: 'label-2'
              }
            ]
          }
        ])
        .build();

      await issuesProcessor.processIssues();

      expect(issuesProcessor.staleIssues).toHaveLength(0);
    });

    test('should stale when set and the pr has the same label', async (): Promise<void> => {
      expect.assertions(1);
      issuesProcessor = issuesProcessorBuilder
        .anyOfPrLabels('dummy-label')
        .prs([
          {
            labels: [
              {
                name: 'dummy-label'
              }
            ]
          }
        ])
        .build();

      await issuesProcessor.processIssues();

      expect(issuesProcessor.staleIssues).toHaveLength(1);
    });

    test('should stale when set and the pr has only one of the same label', async (): Promise<void> => {
      expect.assertions(1);
      issuesProcessor = issuesProcessorBuilder
        .anyOfPrLabels('dummy-label-1,dummy-label-2')
        .prs([
          {
            labels: [
              {
                name: 'dummy-label-1'
              }
            ]
          }
        ])
        .build();

      await issuesProcessor.processIssues();

      expect(issuesProcessor.staleIssues).toHaveLength(1);
    });

    test('should stale when set and the pr has all the same labels', async (): Promise<void> => {
      expect.assertions(1);
      issuesProcessor = issuesProcessorBuilder
        .anyOfPrLabels('dummy-label-1,dummy-label-2')
        .prs([
          {
            labels: [
              {
                name: 'dummy-label-1'
              },
              {
                name: 'dummy-label-2'
              }
            ]
          }
        ])
        .build();

      await issuesProcessor.processIssues();

      expect(issuesProcessor.staleIssues).toHaveLength(1);
    });
  });

  describe('when the any-of-labels options is set (different than any-of-pr-labels)', (): void => {
    beforeEach((): void => {
      issuesProcessorBuilder.anyOfLabels('dummy-any-of-label');
    });

    test('should not stale when not set even if the pr has no label', async (): Promise<void> => {
      expect.assertions(1);
      issuesProcessor = issuesProcessorBuilder
        .emptyAnyOfPrLabels()
        .prs([{labels: []}])
        .build();

      await issuesProcessor.processIssues();

      expect(issuesProcessor.staleIssues).toHaveLength(0);
    });

    test('should not stale when not set even if the pr has a label', async (): Promise<void> => {
      expect.assertions(1);
      issuesProcessor = issuesProcessorBuilder
        .emptyAnyOfPrLabels()
        .prs([{labels: [{name: 'label'}]}])
        .build();

      await issuesProcessor.processIssues();

      expect(issuesProcessor.staleIssues).toHaveLength(0);
    });

    test('should not stale when set and the pr has no label', async (): Promise<void> => {
      expect.assertions(1);
      issuesProcessor = issuesProcessorBuilder
        .anyOfPrLabels('dummy-label')
        .prs([{labels: []}])
        .build();

      await issuesProcessor.processIssues();

      expect(issuesProcessor.staleIssues).toHaveLength(0);
    });

    test('should not stale when set and the pr has a different label', async (): Promise<void> => {
      expect.assertions(1);
      issuesProcessor = issuesProcessorBuilder
        .anyOfPrLabels('dummy-label')
        .prs([
          {
            labels: [
              {
                name: 'label'
              }
            ]
          }
        ])
        .build();

      await issuesProcessor.processIssues();

      expect(issuesProcessor.staleIssues).toHaveLength(0);
    });

    test('should not stale when set and the pr has different labels', async (): Promise<void> => {
      expect.assertions(1);
      issuesProcessor = issuesProcessorBuilder
        .anyOfPrLabels('dummy-label')
        .prs([
          {
            labels: [
              {
                name: 'label-1'
              },
              {
                name: 'label-2'
              }
            ]
          }
        ])
        .build();

      await issuesProcessor.processIssues();

      expect(issuesProcessor.staleIssues).toHaveLength(0);
    });

    test('should stale when set and the pr has the same label', async (): Promise<void> => {
      expect.assertions(1);
      issuesProcessor = issuesProcessorBuilder
        .anyOfPrLabels('dummy-label')
        .prs([
          {
            labels: [
              {
                name: 'dummy-label'
              }
            ]
          }
        ])
        .build();

      await issuesProcessor.processIssues();

      expect(issuesProcessor.staleIssues).toHaveLength(1);
    });

    test('should stale when set and the pr has only one of the same label', async (): Promise<void> => {
      expect.assertions(1);
      issuesProcessor = issuesProcessorBuilder
        .anyOfPrLabels('dummy-label-1,dummy-label-2')
        .prs([
          {
            labels: [
              {
                name: 'dummy-label-1'
              }
            ]
          }
        ])
        .build();

      await issuesProcessor.processIssues();

      expect(issuesProcessor.staleIssues).toHaveLength(1);
    });

    test('should stale when set and the pr has all the same labels', async (): Promise<void> => {
      expect.assertions(1);
      issuesProcessor = issuesProcessorBuilder
        .anyOfPrLabels('dummy-label-1,dummy-label-2')
        .prs([
          {
            labels: [
              {
                name: 'dummy-label-1'
              },
              {
                name: 'dummy-label-2'
              }
            ]
          }
        ])
        .build();

      await issuesProcessor.processIssues();

      expect(issuesProcessor.staleIssues).toHaveLength(1);
    });
  });
});

class IssuesProcessorBuilder {
  private _options: IIssuesProcessorOptions = {
    ...DefaultProcessorOptions,
    daysBeforeStale: 0
  };
  private _issues: Issue[] = [];

  anyOfLabels(labels: string): IssuesProcessorBuilder {
    this._options.anyOfLabels = labels;

    return this;
  }

  anyOfIssueLabels(labels: string): IssuesProcessorBuilder {
    this._options.anyOfIssueLabels = labels;

    return this;
  }

  anyOfPrLabels(labels: string): IssuesProcessorBuilder {
    this._options.anyOfPrLabels = labels;

    return this;
  }

  emptyAnyOfLabels(): IssuesProcessorBuilder {
    return this.anyOfLabels('');
  }

  emptyAnyOfIssueLabels(): IssuesProcessorBuilder {
    return this.anyOfIssueLabels('');
  }

  emptyAnyOfPrLabels(): IssuesProcessorBuilder {
    return this.anyOfPrLabels('');
  }

  issuesOrPrs(issues: Partial<IIssue>[]): IssuesProcessorBuilder {
    this._issues = issues.map(
      (issue: Readonly<Partial<IIssue>>, index: Readonly<number>): Issue =>
        generateIssue(
          this._options,
          index,
          issue.title ?? 'dummy-title',
          issue.updated_at ?? new Date().toDateString(),
          issue.created_at ?? new Date().toDateString(),
          false,
          !!issue.pull_request,
          issue.labels ? issue.labels.map(label => label.name || '') : []
        )
    );

    return this;
  }

  issues(issues: Partial<IIssue>[]): IssuesProcessorBuilder {
    this.issuesOrPrs(
      issues.map((issue: Readonly<Partial<IIssue>>): Partial<IIssue> => {
        return {
          ...issue,
          pull_request: null
        };
      })
    );

    return this;
  }

  prs(issues: Partial<IIssue>[]): IssuesProcessorBuilder {
    this.issuesOrPrs(
      issues.map((issue: Readonly<Partial<IIssue>>): Partial<IIssue> => {
        return {
          ...issue,
          pull_request: {key: 'value'}
        };
      })
    );

    return this;
  }

  build(): IssuesProcessorMock {
    return new IssuesProcessorMock(
      this._options,
      new StateMock(),
      async p => (p === 1 ? this._issues : []),
      async () => [],
      async () => new Date().toDateString()
    );
  }
}
```

## File: `__tests__/assignees.spec.ts`
```typescript
import {Issue} from '../src/classes/issue';
import {IIssuesProcessorOptions} from '../src/interfaces/issues-processor-options';
import {IssuesProcessorMock} from './classes/issues-processor-mock';
import {DefaultProcessorOptions} from './constants/default-processor-options';
import {generateIssue} from './functions/generate-issue';
import {alwaysFalseStateMock} from './classes/state-mock';

interface ITestData {
  id: number;
  isPullRequest: boolean;
  assignees: string[];
  exemptAllAssignees: boolean;
  exemptAllIssueAssignees: boolean | undefined;
  exemptAllPrAssignees: boolean | undefined;
  exemptAssignees: string;
  exemptIssueAssignees: string;
  exemptPrAssignees: string;
  shouldStale: boolean;
  description: string;
}

describe('assignees options', (): void => {
  let opts: IIssuesProcessorOptions;
  let testIssueList: Issue[];
  let processor: IssuesProcessorMock;

  const setTestIssueList = (
    isPullRequest: boolean,
    assignees: string[],
    id: number
  ) => {
    testIssueList = [
      generateIssue(
        opts,
        id,
        'My first issue',
        '2020-01-01T17:00:00Z',
        '2020-01-01T17:00:00Z',
        false,
        isPullRequest,
        undefined,
        undefined,
        undefined,
        undefined,
        assignees
      )
    ];
  };

  const setProcessor = () => {
    processor = new IssuesProcessorMock(
      opts,
      alwaysFalseStateMock,
      async p => (p === 1 ? testIssueList : []),
      async () => [],
      async () => new Date().toDateString()
    );
  };

  beforeEach((): void => {
    opts = {...DefaultProcessorOptions};
  });

  describe.each`
    id      | isPullRequest | assignees       | exemptAllAssignees | exemptAllIssueAssignees | exemptAllPrAssignees | exemptAssignees | exemptIssueAssignees | exemptPrAssignees | shouldStale | description
    ${100}  | ${false}      | ${[]}           | ${false}           | ${undefined}            | ${undefined}         | ${''}           | ${''}                | ${''}             | ${true}     | ${'when the issue does not have an assignee'}
    ${101}  | ${false}      | ${[]}           | ${true}            | ${undefined}            | ${undefined}         | ${''}           | ${''}                | ${''}             | ${true}     | ${'when the issue does not have an assignee and only exemptAllAssignees is enabled'}
    ${102}  | ${false}      | ${[]}           | ${false}           | ${true}                 | ${undefined}         | ${''}           | ${''}                | ${''}             | ${true}     | ${'when the issue does not have an assignee and only exemptAllIssueAssignees is enabled'}
    ${103}  | ${false}      | ${[]}           | ${false}           | ${undefined}            | ${true}              | ${''}           | ${''}                | ${''}             | ${true}     | ${'when the issue does not have an assignee and only exemptAllPrAssignees is enabled'}
    ${104}  | ${false}      | ${[]}           | ${true}            | ${false}                | ${undefined}         | ${''}           | ${''}                | ${''}             | ${true}     | ${'when the issue does not have an assignee and exemptAllAssignees is enabled and exemptAllIssueAssignees is disabled'}
    ${105}  | ${false}      | ${[]}           | ${true}            | ${true}                 | ${undefined}         | ${''}           | ${''}                | ${''}             | ${true}     | ${'when the issue does not have an assignee and exemptAllAssignees is enabled and exemptAllIssueAssignees is enabled'}
    ${106}  | ${false}      | ${[]}           | ${true}            | ${undefined}            | ${false}             | ${''}           | ${''}                | ${''}             | ${true}     | ${'when the issue does not have an assignee and exemptAllAssignees is enabled and exemptAllPrAssignees is disabled'}
    ${107}  | ${false}      | ${[]}           | ${true}            | ${undefined}            | ${true}              | ${''}           | ${''}                | ${''}             | ${true}     | ${'when the issue does not have an assignee and exemptAllAssignees is enabled and exemptAllPrAssignees is enabled'}
    ${108}  | ${false}      | ${[]}           | ${false}           | ${false}                | ${undefined}         | ${''}           | ${''}                | ${''}             | ${true}     | ${'when the issue does not have an assignee and exemptAllAssignees is disabled and exemptAllIssueAssignees is disabled'}
    ${109}  | ${false}      | ${[]}           | ${false}           | ${true}                 | ${undefined}         | ${''}           | ${''}                | ${''}             | ${true}     | ${'when the issue does not have an assignee and exemptAllAssignees is disabled and exemptAllIssueAssignees is enabled'}
    ${200}  | ${false}      | ${['assignee']} | ${false}           | ${undefined}            | ${false}             | ${''}           | ${''}                | ${''}             | ${true}     | ${'when the issue has an assignee and exemptAllAssignees is disabled and exemptAllPrAssignees is disabled'}
    ${201}  | ${false}      | ${['assignee']} | ${false}           | ${undefined}            | ${true}              | ${''}           | ${''}                | ${''}             | ${true}     | ${'when the issue has an assignee and exemptAllAssignees is disabled and exemptAllPrAssignees is enabled'}
    ${202}  | ${false}      | ${['assignee']} | ${true}            | ${undefined}            | ${undefined}         | ${''}           | ${''}                | ${''}             | ${false}    | ${'when the issue has an assignee and only exemptAllAssignees is enabled'}
    ${203}  | ${false}      | ${['assignee']} | ${false}           | ${true}                 | ${undefined}         | ${''}           | ${''}                | ${''}             | ${false}    | ${'when the issue has an assignee and only exemptAllIssueAssignees is enabled'}
    ${204}  | ${false}      | ${['assignee']} | ${false}           | ${undefined}            | ${true}              | ${''}           | ${''}                | ${''}             | ${true}     | ${'when the issue has an assignee and only exemptAllPrAssignees is enabled'}
    ${205}  | ${false}      | ${['assignee']} | ${true}            | ${false}                | ${undefined}         | ${''}           | ${''}                | ${''}             | ${true}     | ${'when the issue has an assignee and exemptAllAssignees is enabled and exemptAllIssueAssignees is disabled'}
    ${206}  | ${false}      | ${['assignee']} | ${true}            | ${true}                 | ${undefined}         | ${''}           | ${''}                | ${''}             | ${false}    | ${'when the issue has an assignee and exemptAllAssignees is enabled and exemptAllIssueAssignees is enabled'}
    ${207}  | ${false}      | ${['assignee']} | ${true}            | ${undefined}            | ${false}             | ${''}           | ${''}                | ${''}             | ${false}    | ${'when the issue has an assignee and exemptAllAssignees is enabled and exemptAllPrAssignees is disabled'}
    ${208}  | ${false}      | ${['assignee']} | ${true}            | ${undefined}            | ${true}              | ${''}           | ${''}                | ${''}             | ${false}    | ${'when the issue has an assignee and exemptAllAssignees is enabled and exemptAllPrAssignees is enabled'}
    ${209}  | ${false}      | ${['assignee']} | ${false}           | ${false}                | ${undefined}         | ${''}           | ${''}                | ${''}             | ${true}     | ${'when the issue has an assignee and exemptAllAssignees is disabled and exemptAllIssueAssignees is disabled'}
    ${210}  | ${false}      | ${['assignee']} | ${false}           | ${true}                 | ${undefined}         | ${''}           | ${''}                | ${''}             | ${false}    | ${'when the issue has an assignee and exemptAllAssignees is disabled and exemptAllIssueAssignees is enabled'}
    ${211}  | ${false}      | ${['assignee']} | ${false}           | ${undefined}            | ${false}             | ${''}           | ${''}                | ${''}             | ${true}     | ${'when the issue has an assignee and exemptAllAssignees is disabled and exemptAllPrAssignees is disabled'}
    ${212}  | ${false}      | ${['assignee']} | ${false}           | ${undefined}            | ${true}              | ${''}           | ${''}                | ${''}             | ${true}     | ${'when the issue has an assignee and exemptAllAssignees is disabled and exemptAllPrAssignees is enabled'}
    ${213}  | ${false}      | ${['assignee']} | ${false}           | ${undefined}            | ${false}             | ${''}           | ${''}                | ${''}             | ${true}     | ${'when the issue has an assignee and exemptAllAssignees is disabled and exemptAllPrAssignees is disabled'}
    ${300}  | ${false}      | ${['assignee']} | ${false}           | ${undefined}            | ${false}             | ${'bad'}        | ${''}                | ${''}             | ${true}     | ${'when the issue has an assignee and exemptAllAssignees is disabled, exemptAllPrAssignees is disabled and exemptAssignees has a different assignee'}
    ${301}  | ${false}      | ${['assignee']} | ${false}           | ${undefined}            | ${true}              | ${'bad'}        | ${''}                | ${''}             | ${true}     | ${'when the issue has an assignee and exemptAllAssignees is disabled, exemptAllPrAssignees is enabled and exemptAssignees has a different assignee'}
    ${302}  | ${false}      | ${['assignee']} | ${true}            | ${undefined}            | ${undefined}         | ${'bad'}        | ${''}                | ${''}             | ${false}    | ${'when the issue has an assignee and exemptAllAssignees is enabled and exemptAssignees has a different assignee'}
    ${303}  | ${false}      | ${['assignee']} | ${false}           | ${true}                 | ${undefined}         | ${'bad'}        | ${''}                | ${''}             | ${false}    | ${'when the issue has an assignee and exemptAllIssueAssignees is enabled and exemptAssignees has a different assignee'}
    ${304}  | ${false}      | ${['assignee']} | ${false}           | ${undefined}            | ${true}              | ${'bad'}        | ${''}                | ${''}             | ${true}     | ${'when the issue has an assignee and exemptAllPrAssignees is enabled and exemptAssignees has a different assignee'}
    ${305}  | ${false}      | ${['assignee']} | ${true}            | ${false}                | ${undefined}         | ${'bad'}        | ${''}                | ${''}             | ${true}     | ${'when the issue has an assignee and exemptAllAssignees is enabled, exemptAllIssueAssignees is disabled and exemptAssignees has a different assignee'}
    ${306}  | ${false}      | ${['assignee']} | ${true}            | ${true}                 | ${undefined}         | ${'bad'}        | ${''}                | ${''}             | ${false}    | ${'when the issue has an assignee and exemptAllAssignees is enabled, exemptAllIssueAssignees is enabled and exemptAssignees has a different assignee'}
    ${307}  | ${false}      | ${['assignee']} | ${true}            | ${undefined}            | ${false}             | ${'bad'}        | ${''}                | ${''}             | ${false}    | ${'when the issue has an assignee and exemptAllAssignees is enabled, exemptAllPrAssignees is disabled and exemptAssignees has a different assignee'}
    ${308}  | ${false}      | ${['assignee']} | ${true}            | ${undefined}            | ${true}              | ${'bad'}        | ${''}                | ${''}             | ${false}    | ${'when the issue has an assignee and exemptAllAssignees is enabled, exemptAllPrAssignees is enabled and exemptAssignees has a different assignee'}
    ${309}  | ${false}      | ${['assignee']} | ${false}           | ${false}                | ${undefined}         | ${'bad'}        | ${''}                | ${''}             | ${true}     | ${'when the issue has an assignee and exemptAllAssignees is disabled, exemptAllIssueAssignees is disabled and exemptAssignees has a different assignee'}
    ${310}  | ${false}      | ${['assignee']} | ${false}           | ${true}                 | ${undefined}         | ${'bad'}        | ${''}                | ${''}             | ${false}    | ${'when the issue has an assignee and exemptAllAssignees is disabled, exemptAllIssueAssignees is enabled and exemptAssignees has a different assignee'}
    ${311}  | ${false}      | ${['assignee']} | ${false}           | ${undefined}            | ${false}             | ${'bad'}        | ${''}                | ${''}             | ${true}     | ${'when the issue has an assignee and exemptAllAssignees is disabled, exemptAllPrAssignees is disabled and exemptAssignees has a different assignee'}
    ${312}  | ${false}      | ${['assignee']} | ${false}           | ${undefined}            | ${true}              | ${'bad'}        | ${''}                | ${''}             | ${true}     | ${'when the issue has an assignee and exemptAllAssignees is disabled, exemptAllPrAssignees is enabled and exemptAssignees has a different assignee'}
    ${313}  | ${false}      | ${['assignee']} | ${false}           | ${undefined}            | ${false}             | ${'bad'}        | ${''}                | ${''}             | ${true}     | ${'when the issue has an assignee and exemptAllAssignees is disabled, exemptAllPrAssignees is disabled and exemptAssignees has a different assignee'}
    ${400}  | ${false}      | ${['assignee']} | ${false}           | ${undefined}            | ${false}             | ${'assignee'}   | ${''}                | ${''}             | ${false}    | ${'when the issue has an assignee and exemptAllAssignees is disabled, exemptAllPrAssignees is disabled and exemptAssignees has the same assignee'}
    ${401}  | ${false}      | ${['assignee']} | ${false}           | ${undefined}            | ${true}              | ${'assignee'}   | ${''}                | ${''}             | ${false}    | ${'when the issue has an assignee and exemptAllAssignees is disabled, exemptAllPrAssignees is enabled and exemptAssignees has the same assignee'}
    ${402}  | ${false}      | ${['assignee']} | ${true}            | ${undefined}            | ${undefined}         | ${'assignee'}   | ${''}                | ${''}             | ${false}    | ${'when the issue has an assignee and exemptAllAssignees is enabled and exemptAssignees has the same assignee'}
    ${403}  | ${false}      | ${['assignee']} | ${false}           | ${true}                 | ${undefined}         | ${'assignee'}   | ${''}                | ${''}             | ${false}    | ${'when the issue has an assignee and exemptAllIssueAssignees is enabled and exemptAssignees has the same assignee'}
    ${404}  | ${false}      | ${['assignee']} | ${false}           | ${undefined}            | ${true}              | ${'assignee'}   | ${''}                | ${''}             | ${false}    | ${'when the issue has an assignee and exemptAllPrAssignees is enabled and exemptAssignees has the same assignee'}
    ${405}  | ${false}      | ${['assignee']} | ${true}            | ${false}                | ${undefined}         | ${'assignee'}   | ${''}                | ${''}             | ${false}    | ${'when the issue has an assignee and exemptAllAssignees is enabled, exemptAllIssueAssignees is disabled and exemptAssignees has the same assignee'}
    ${406}  | ${false}      | ${['assignee']} | ${true}            | ${true}                 | ${undefined}         | ${'assignee'}   | ${''}                | ${''}             | ${false}    | ${'when the issue has an assignee and exemptAllAssignees is enabled, exemptAllIssueAssignees is enabled and exemptAssignees has the same assignee'}
    ${407}  | ${false}      | ${['assignee']} | ${true}            | ${undefined}            | ${false}             | ${'assignee'}   | ${''}                | ${''}             | ${false}    | ${'when the issue has an assignee and exemptAllAssignees is enabled, exemptAllPrAssignees is disabled and exemptAssignees has the same assignee'}
    ${408}  | ${false}      | ${['assignee']} | ${true}            | ${undefined}            | ${true}              | ${'assignee'}   | ${''}                | ${''}             | ${false}    | ${'when the issue has an assignee and exemptAllAssignees is enabled, exemptAllPrAssignees is enabled and exemptAssignees has the same assignee'}
    ${409}  | ${false}      | ${['assignee']} | ${false}           | ${false}                | ${undefined}         | ${'assignee'}   | ${''}                | ${''}             | ${false}    | ${'when the issue has an assignee and exemptAllAssignees is disabled, exemptAllIssueAssignees is disabled and exemptAssignees has the same assignee'}
    ${410}  | ${false}      | ${['assignee']} | ${false}           | ${true}                 | ${undefined}         | ${'assignee'}   | ${''}                | ${''}             | ${false}    | ${'when the issue has an assignee and exemptAllAssignees is disabled, exemptAllIssueAssignees is enabled and exemptAssignees has the same assignee'}
    ${411}  | ${false}      | ${['assignee']} | ${false}           | ${undefined}            | ${false}             | ${'assignee'}   | ${''}                | ${''}             | ${false}    | ${'when the issue has an assignee and exemptAllAssignees is disabled, exemptAllPrAssignees is disabled and exemptAssignees has the same assignee'}
    ${412}  | ${false}      | ${['assignee']} | ${false}           | ${undefined}            | ${true}              | ${'assignee'}   | ${''}                | ${''}             | ${false}    | ${'when the issue has an assignee and exemptAllAssignees is disabled, exemptAllPrAssignees is enabled and exemptAssignees has the same assignee'}
    ${413}  | ${false}      | ${['assignee']} | ${false}           | ${undefined}            | ${false}             | ${'assignee'}   | ${''}                | ${''}             | ${false}    | ${'when the issue has an assignee and exemptAllAssignees is disabled, exemptAllPrAssignees is disabled and exemptAssignees has the same assignee'}
    ${500}  | ${false}      | ${['assignee']} | ${false}           | ${undefined}            | ${false}             | ${'bad'}        | ${'bad'}             | ${''}             | ${true}     | ${'when the issue has an assignee and exemptAllAssignees is disabled, exemptAllPrAssignees is disabled and exemptAssignees and exemptIssueAssignees has a different assignee'}
    ${501}  | ${false}      | ${['assignee']} | ${false}           | ${undefined}            | ${true}              | ${'bad'}        | ${'bad'}             | ${''}             | ${true}     | ${'when the issue has an assignee and exemptAllAssignees is disabled, exemptAllPrAssignees is enabled and exemptAssignees and exemptIssueAssignees has a different assignee'}
    ${502}  | ${false}      | ${['assignee']} | ${true}            | ${undefined}            | ${undefined}         | ${'bad'}        | ${'bad'}             | ${''}             | ${false}    | ${'when the issue has an assignee and exemptAllAssignees is enabled and exemptAssignees and exemptIssueAssignees has a different assignee'}
    ${503}  | ${false}      | ${['assignee']} | ${false}           | ${true}                 | ${undefined}         | ${'bad'}        | ${'bad'}             | ${''}             | ${false}    | ${'when the issue has an assignee and exemptAllIssueAssignees is enabled and exemptAssignees and exemptIssueAssignees has a different assignee'}
    ${504}  | ${false}      | ${['assignee']} | ${false}           | ${undefined}            | ${true}              | ${'bad'}        | ${'bad'}             | ${''}             | ${true}     | ${'when the issue has an assignee and exemptAllPrAssignees is enabled and exemptAssignees and exemptIssueAssignees has a different assignee'}
    ${505}  | ${false}      | ${['assignee']} | ${true}            | ${false}                | ${undefined}         | ${'bad'}        | ${'bad'}             | ${''}             | ${true}     | ${'when the issue has an assignee and exemptAllAssignees is enabled, exemptAllIssueAssignees is disabled and exemptAssignees and exemptIssueAssignees has a different assignee'}
    ${506}  | ${false}      | ${['assignee']} | ${true}            | ${true}                 | ${undefined}         | ${'bad'}        | ${'bad'}             | ${''}             | ${false}    | ${'when the issue has an assignee and exemptAllAssignees is enabled, exemptAllIssueAssignees is enabled and exemptAssignees and exemptIssueAssignees has a different assignee'}
    ${507}  | ${false}      | ${['assignee']} | ${true}            | ${undefined}            | ${false}             | ${'bad'}        | ${'bad'}             | ${''}             | ${false}    | ${'when the issue has an assignee and exemptAllAssignees is enabled, exemptAllPrAssignees is disabled and exemptAssignees and exemptIssueAssignees has a different assignee'}
    ${508}  | ${false}      | ${['assignee']} | ${true}            | ${undefined}            | ${true}              | ${'bad'}        | ${'bad'}             | ${''}             | ${false}    | ${'when the issue has an assignee and exemptAllAssignees is enabled, exemptAllPrAssignees is enabled and exemptAssignees and exemptIssueAssignees has a different assignee'}
    ${509}  | ${false}      | ${['assignee']} | ${false}           | ${false}                | ${undefined}         | ${'bad'}        | ${'bad'}             | ${''}             | ${true}     | ${'when the issue has an assignee and exemptAllAssignees is disabled, exemptAllIssueAssignees is disabled and exemptAssignees and exemptIssueAssignees has a different assignee'}
    ${510}  | ${false}      | ${['assignee']} | ${false}           | ${true}                 | ${undefined}         | ${'bad'}        | ${'bad'}             | ${''}             | ${false}    | ${'when the issue has an assignee and exemptAllAssignees is disabled, exemptAllIssueAssignees is enabled and exemptAssignees and exemptIssueAssignees has a different assignee'}
    ${511}  | ${false}      | ${['assignee']} | ${false}           | ${undefined}            | ${false}             | ${'bad'}        | ${'bad'}             | ${''}             | ${true}     | ${'when the issue has an assignee and exemptAllAssignees is disabled, exemptAllPrAssignees is disabled and exemptAssignees and exemptIssueAssignees has a different assignee'}
    ${512}  | ${false}      | ${['assignee']} | ${false}           | ${undefined}            | ${true}              | ${'bad'}        | ${'bad'}             | ${''}             | ${true}     | ${'when the issue has an assignee and exemptAllAssignees is disabled, exemptAllPrAssignees is enabled and exemptAssignees and exemptIssueAssignees has a different assignee'}
    ${513}  | ${false}      | ${['assignee']} | ${false}           | ${undefined}            | ${false}             | ${'bad'}        | ${'bad'}             | ${''}             | ${true}     | ${'when the issue has an assignee and exemptAllAssignees is disabled, exemptAllPrAssignees is disabled and exemptAssignees and exemptIssueAssignees has a different assignee'}
    ${600}  | ${false}      | ${['assignee']} | ${false}           | ${undefined}            | ${false}             | ${'bad'}        | ${'assignee'}        | ${''}             | ${false}    | ${'when the issue has an assignee and exemptAllAssignees is disabled, exemptAllPrAssignees is disabled, exemptAssignees has a different assignee and exemptIssueAssignees has the same assignee'}
    ${601}  | ${false}      | ${['assignee']} | ${false}           | ${undefined}            | ${true}              | ${'bad'}        | ${'assignee'}        | ${''}             | ${false}    | ${'when the issue has an assignee and exemptAllAssignees is disabled, exemptAllPrAssignees is enabled, exemptAssignees has a different assignee and exemptIssueAssignees has the same assignee'}
    ${602}  | ${false}      | ${['assignee']} | ${true}            | ${undefined}            | ${undefined}         | ${'bad'}        | ${'assignee'}        | ${''}             | ${false}    | ${'when the issue has an assignee and exemptAllAssignees is enabled, exemptAssignees has a different assignee and exemptIssueAssignees has the same assignee'}
    ${603}  | ${false}      | ${['assignee']} | ${false}           | ${true}                 | ${undefined}         | ${'bad'}        | ${'assignee'}        | ${''}             | ${false}    | ${'when the issue has an assignee and exemptAllIssueAssignees is enabled, exemptAssignees has a different assignee and exemptIssueAssignees has the same assignee'}
    ${604}  | ${false}      | ${['assignee']} | ${false}           | ${undefined}            | ${true}              | ${'bad'}        | ${'assignee'}        | ${''}             | ${false}    | ${'when the issue has an assignee and exemptAllPrAssignees is enabled, exemptAssignees has a different assignee and exemptIssueAssignees has the same assignee'}
    ${605}  | ${false}      | ${['assignee']} | ${true}            | ${false}                | ${undefined}         | ${'bad'}        | ${'assignee'}        | ${''}             | ${false}    | ${'when the issue has an assignee and exemptAllAssignees is enabled, exemptAllIssueAssignees is disabled, exemptAssignees has a different assignee and exemptIssueAssignees has the same assignee'}
    ${606}  | ${false}      | ${['assignee']} | ${true}            | ${true}                 | ${undefined}         | ${'bad'}        | ${'assignee'}        | ${''}             | ${false}    | ${'when the issue has an assignee and exemptAllAssignees is enabled, exemptAllIssueAssignees is enabled, exemptAssignees has a different assignee and exemptIssueAssignees has the same assignee'}
    ${607}  | ${false}      | ${['assignee']} | ${true}            | ${undefined}            | ${false}             | ${'bad'}        | ${'assignee'}        | ${''}             | ${false}    | ${'when the issue has an assignee and exemptAllAssignees is enabled, exemptAllPrAssignees is disabled, exemptAssignees has a different assignee and exemptIssueAssignees has the same assignee'}
    ${608}  | ${false}      | ${['assignee']} | ${true}            | ${undefined}            | ${true}              | ${'bad'}        | ${'assignee'}        | ${''}             | ${false}    | ${'when the issue has an assignee and exemptAllAssignees is enabled, exemptAllPrAssignees is enabled, exemptAssignees has a different assignee and exemptIssueAssignees has the same assignee'}
    ${609}  | ${false}      | ${['assignee']} | ${false}           | ${false}                | ${undefined}         | ${'bad'}        | ${'assignee'}        | ${''}             | ${false}    | ${'when the issue has an assignee and exemptAllAssignees is disabled, exemptAllIssueAssignees is disabled, exemptAssignees has a different assignee and exemptIssueAssignees has the same assignee'}
    ${610}  | ${false}      | ${['assignee']} | ${false}           | ${true}                 | ${undefined}         | ${'bad'}        | ${'assignee'}        | ${''}             | ${false}    | ${'when the issue has an assignee and exemptAllAssignees is disabled, exemptAllIssueAssignees is enabled, exemptAssignees has a different assignee and exemptIssueAssignees has the same assignee'}
    ${611}  | ${false}      | ${['assignee']} | ${false}           | ${undefined}            | ${false}             | ${'bad'}        | ${'assignee'}        | ${''}             | ${false}    | ${'when the issue has an assignee and exemptAllAssignees is disabled, exemptAllPrAssignees is disabled, exemptAssignees has a different assignee and exemptIssueAssignees has the same assignee'}
    ${612}  | ${false}      | ${['assignee']} | ${false}           | ${undefined}            | ${true}              | ${'bad'}        | ${'assignee'}        | ${''}             | ${false}    | ${'when the issue has an assignee and exemptAllAssignees is disabled, exemptAllPrAssignees is enabled, exemptAssignees has a different assignee and exemptIssueAssignees has the same assignee'}
    ${613}  | ${false}      | ${['assignee']} | ${false}           | ${undefined}            | ${false}             | ${'bad'}        | ${'assignee'}        | ${''}             | ${false}    | ${'when the issue has an assignee and exemptAllAssignees is disabled, exemptAllPrAssignees is disabled, exemptAssignees has a different assignee and exemptIssueAssignees has the same assignee'}
    ${700}  | ${false}      | ${['assignee']} | ${false}           | ${undefined}            | ${false}             | ${'bad'}        | ${''}                | ${'bad'}          | ${true}     | ${'when the issue has an assignee and exemptAllAssignees is disabled, exemptAllPrAssignees is disabled and exemptAssignees and exemptPrAssignees has a different assignee'}
    ${701}  | ${false}      | ${['assignee']} | ${false}           | ${undefined}            | ${true}              | ${'bad'}        | ${''}                | ${'bad'}          | ${true}     | ${'when the issue has an assignee and exemptAllAssignees is disabled, exemptAllPrAssignees is enabled and exemptAssignees and exemptPrAssignees has a different assignee'}
    ${702}  | ${false}      | ${['assignee']} | ${true}            | ${undefined}            | ${undefined}         | ${'bad'}        | ${''}                | ${'bad'}          | ${false}    | ${'when the issue has an assignee and exemptAllAssignees is enabled and exemptAssignees and exemptPrAssignees has a different assignee'}
    ${703}  | ${false}      | ${['assignee']} | ${false}           | ${true}                 | ${undefined}         | ${'bad'}        | ${''}                | ${'bad'}          | ${false}    | ${'when the issue has an assignee and exemptAllIssueAssignees is enabled and exemptAssignees and exemptPrAssignees has a different assignee'}
    ${704}  | ${false}      | ${['assignee']} | ${false}           | ${undefined}            | ${true}              | ${'bad'}        | ${''}                | ${'bad'}          | ${true}     | ${'when the issue has an assignee and exemptAllPrAssignees is enabled and exemptAssignees and exemptPrAssignees has a different assignee'}
    ${705}  | ${false}      | ${['assignee']} | ${true}            | ${false}                | ${undefined}         | ${'bad'}        | ${''}                | ${'bad'}          | ${true}     | ${'when the issue has an assignee and exemptAllAssignees is enabled, exemptAllIssueAssignees is disabled and exemptAssignees and exemptPrAssignees has a different assignee'}
    ${706}  | ${false}      | ${['assignee']} | ${true}            | ${true}                 | ${undefined}         | ${'bad'}        | ${''}                | ${'bad'}          | ${false}    | ${'when the issue has an assignee and exemptAllAssignees is enabled, exemptAllIssueAssignees is enabled and exemptAssignees and exemptPrAssignees has a different assignee'}
    ${707}  | ${false}      | ${['assignee']} | ${true}            | ${undefined}            | ${false}             | ${'bad'}        | ${''}                | ${'bad'}          | ${false}    | ${'when the issue has an assignee and exemptAllAssignees is enabled, exemptAllPrAssignees is disabled and exemptAssignees and exemptPrAssignees has a different assignee'}
    ${708}  | ${false}      | ${['assignee']} | ${true}            | ${undefined}            | ${true}              | ${'bad'}        | ${''}                | ${'bad'}          | ${false}    | ${'when the issue has an assignee and exemptAllAssignees is enabled, exemptAllPrAssignees is enabled and exemptAssignees and exemptPrAssignees has a different assignee'}
    ${709}  | ${false}      | ${['assignee']} | ${false}           | ${false}                | ${undefined}         | ${'bad'}        | ${''}                | ${'bad'}          | ${true}     | ${'when the issue has an assignee and exemptAllAssignees is disabled, exemptAllIssueAssignees is disabled and exemptAssignees and exemptPrAssignees has a different assignee'}
    ${710}  | ${false}      | ${['assignee']} | ${false}           | ${true}                 | ${undefined}         | ${'bad'}        | ${''}                | ${'bad'}          | ${false}    | ${'when the issue has an assignee and exemptAllAssignees is disabled, exemptAllIssueAssignees is enabled and exemptAssignees and exemptPrAssignees has a different assignee'}
    ${711}  | ${false}      | ${['assignee']} | ${false}           | ${undefined}            | ${false}             | ${'bad'}        | ${''}                | ${'bad'}          | ${true}     | ${'when the issue has an assignee and exemptAllAssignees is disabled, exemptAllPrAssignees is disabled and exemptAssignees and exemptPrAssignees has a different assignee'}
    ${712}  | ${false}      | ${['assignee']} | ${false}           | ${undefined}            | ${true}              | ${'bad'}        | ${''}                | ${'bad'}          | ${true}     | ${'when the issue has an assignee and exemptAllAssignees is disabled, exemptAllPrAssignees is enabled and exemptAssignees and exemptPrAssignees has a different assignee'}
    ${713}  | ${false}      | ${['assignee']} | ${false}           | ${undefined}            | ${false}             | ${'bad'}        | ${''}                | ${'bad'}          | ${true}     | ${'when the issue has an assignee and exemptAllAssignees is disabled, exemptAllPrAssignees is disabled and exemptAssignees and exemptPrAssignees has a different assignee'}
    ${800}  | ${false}      | ${['assignee']} | ${false}           | ${undefined}            | ${false}             | ${'bad'}        | ${''}                | ${'assignee'}     | ${true}     | ${'when the issue has an assignee and exemptAllAssignees is disabled, exemptAllPrAssignees is disabled, exemptAssignees has a different assignee and exemptPrAssignees has the same assignee'}
    ${801}  | ${false}      | ${['assignee']} | ${false}           | ${undefined}            | ${true}              | ${'bad'}        | ${''}                | ${'assignee'}     | ${true}     | ${'when the issue has an assignee and exemptAllAssignees is disabled, exemptAllPrAssignees is enabled, exemptAssignees has a different assignee and exemptPrAssignees has the same assignee'}
    ${802}  | ${false}      | ${['assignee']} | ${true}            | ${undefined}            | ${undefined}         | ${'bad'}        | ${''}                | ${'assignee'}     | ${false}    | ${'when the issue has an assignee and exemptAllAssignees is enabled, exemptAssignees has a different assignee and exemptPrAssignees has the same assignee'}
    ${803}  | ${false}      | ${['assignee']} | ${false}           | ${true}                 | ${undefined}         | ${'bad'}        | ${''}                | ${'assignee'}     | ${false}    | ${'when the issue has an assignee and exemptAllIssueAssignees is enabled, exemptAssignees has a different assignee and exemptPrAssignees has the same assignee'}
    ${804}  | ${false}      | ${['assignee']} | ${false}           | ${undefined}            | ${true}              | ${'bad'}        | ${''}                | ${'assignee'}     | ${true}     | ${'when the issue has an assignee and exemptAllPrAssignees is enabled, exemptAssignees has a different assignee and exemptPrAssignees has the same assignee'}
    ${805}  | ${false}      | ${['assignee']} | ${true}            | ${false}                | ${undefined}         | ${'bad'}        | ${''}                | ${'assignee'}     | ${true}     | ${'when the issue has an assignee and exemptAllAssignees is enabled, exemptAllIssueAssignees is disabled, exemptAssignees has a different assignee and exemptPrAssignees has the same assignee'}
    ${806}  | ${false}      | ${['assignee']} | ${true}            | ${true}                 | ${undefined}         | ${'bad'}        | ${''}                | ${'assignee'}     | ${false}    | ${'when the issue has an assignee and exemptAllAssignees is enabled, exemptAllIssueAssignees is enabled, exemptAssignees has a different assignee and exemptPrAssignees has the same assignee'}
    ${807}  | ${false}      | ${['assignee']} | ${true}            | ${undefined}            | ${false}             | ${'bad'}        | ${''}                | ${'assignee'}     | ${false}    | ${'when the issue has an assignee and exemptAllAssignees is enabled, exemptAllPrAssignees is disabled, exemptAssignees has a different assignee and exemptPrAssignees has the same assignee'}
    ${808}  | ${false}      | ${['assignee']} | ${true}            | ${undefined}            | ${true}              | ${'bad'}        | ${''}                | ${'assignee'}     | ${false}    | ${'when the issue has an assignee and exemptAllAssignees is enabled, exemptAllPrAssignees is enabled, exemptAssignees has a different assignee and exemptPrAssignees has the same assignee'}
    ${809}  | ${false}      | ${['assignee']} | ${false}           | ${false}                | ${undefined}         | ${'bad'}        | ${''}                | ${'assignee'}     | ${true}     | ${'when the issue has an assignee and exemptAllAssignees is disabled, exemptAllIssueAssignees is disabled, exemptAssignees has a different assignee and exemptPrAssignees has the same assignee'}
    ${810}  | ${false}      | ${['assignee']} | ${false}           | ${true}                 | ${undefined}         | ${'bad'}        | ${''}                | ${'assignee'}     | ${false}    | ${'when the issue has an assignee and exemptAllAssignees is disabled, exemptAllIssueAssignees is enabled, exemptAssignees has a different assignee and exemptPrAssignees has the same assignee'}
    ${811}  | ${false}      | ${['assignee']} | ${false}           | ${undefined}            | ${false}             | ${'bad'}        | ${''}                | ${'assignee'}     | ${true}     | ${'when the issue has an assignee and exemptAllAssignees is disabled, exemptAllPrAssignees is disabled, exemptAssignees has a different assignee and exemptPrAssignees has the same assignee'}
    ${812}  | ${false}      | ${['assignee']} | ${false}           | ${undefined}            | ${true}              | ${'bad'}        | ${''}                | ${'assignee'}     | ${true}     | ${'when the issue has an assignee and exemptAllAssignees is disabled, exemptAllPrAssignees is enabled, exemptAssignees has a different assignee and exemptPrAssignees has the same assignee'}
    ${813}  | ${false}      | ${['assignee']} | ${false}           | ${undefined}            | ${false}             | ${'bad'}        | ${''}                | ${'assignee'}     | ${true}     | ${'when the issue has an assignee and exemptAllAssignees is disabled, exemptAllPrAssignees is disabled, exemptAssignees has a different assignee and exemptPrAssignees has the same assignee'}
    ${900}  | ${false}      | ${['assignee']} | ${false}           | ${undefined}            | ${false}             | ${'assignee'}   | ${'bad'}             | ${''}             | ${true}     | ${'when the issue has an assignee and exemptAllAssignees is disabled, exemptAllPrAssignees is disabled, exemptAssignees has the same assignee and exemptIssueAssignees has a different assignee'}
    ${901}  | ${false}      | ${['assignee']} | ${false}           | ${undefined}            | ${true}              | ${'assignee'}   | ${'bad'}             | ${''}             | ${true}     | ${'when the issue has an assignee and exemptAllAssignees is disabled, exemptAllPrAssignees is enabled, exemptAssignees has the same assignee and exemptIssueAssignees has a different assignee'}
    ${902}  | ${false}      | ${['assignee']} | ${true}            | ${undefined}            | ${undefined}         | ${'assignee'}   | ${'bad'}             | ${''}             | ${false}    | ${'when the issue has an assignee and exemptAllAssignees is enabled, exemptAssignees has the same assignee and exemptIssueAssignees has a different assignee'}
    ${903}  | ${false}      | ${['assignee']} | ${false}           | ${true}                 | ${undefined}         | ${'assignee'}   | ${'bad'}             | ${''}             | ${false}    | ${'when the issue has an assignee and exemptAllIssueAssignees is enabled, exemptAssignees has the same assignee and exemptIssueAssignees has a different assignee'}
    ${904}  | ${false}      | ${['assignee']} | ${false}           | ${undefined}            | ${true}              | ${'assignee'}   | ${'bad'}             | ${''}             | ${true}     | ${'when the issue has an assignee and exemptAllPrAssignees is enabled, exemptAssignees has the same assignee and exemptIssueAssignees has a different assignee'}
    ${905}  | ${false}      | ${['assignee']} | ${true}            | ${false}                | ${undefined}         | ${'assignee'}   | ${'bad'}             | ${''}             | ${true}     | ${'when the issue has an assignee and exemptAllAssignees is enabled, exemptAllIssueAssignees is disabled, exemptAssignees has the same assignee and exemptIssueAssignees has a different assignee'}
    ${906}  | ${false}      | ${['assignee']} | ${true}            | ${true}                 | ${undefined}         | ${'assignee'}   | ${'bad'}             | ${''}             | ${false}    | ${'when the issue has an assignee and exemptAllAssignees is enabled, exemptAllIssueAssignees is enabled, exemptAssignees has the same assignee and exemptIssueAssignees has a different assignee'}
    ${907}  | ${false}      | ${['assignee']} | ${true}            | ${undefined}            | ${false}             | ${'assignee'}   | ${'bad'}             | ${''}             | ${false}    | ${'when the issue has an assignee and exemptAllAssignees is enabled, exemptAllPrAssignees is disabled, exemptAssignees has the same assignee and exemptIssueAssignees has a different assignee'}
    ${908}  | ${false}      | ${['assignee']} | ${true}            | ${undefined}            | ${true}              | ${'assignee'}   | ${'bad'}             | ${''}             | ${false}    | ${'when the issue has an assignee and exemptAllAssignees is enabled, exemptAllPrAssignees is enabled, exemptAssignees has the same assignee and exemptIssueAssignees has a different assignee'}
    ${909}  | ${false}      | ${['assignee']} | ${false}           | ${false}                | ${undefined}         | ${'assignee'}   | ${'bad'}             | ${''}             | ${true}     | ${'when the issue has an assignee and exemptAllAssignees is disabled, exemptAllIssueAssignees is disabled, exemptAssignees has the same assignee and exemptIssueAssignees has a different assignee'}
    ${910}  | ${false}      | ${['assignee']} | ${false}           | ${true}                 | ${undefined}         | ${'assignee'}   | ${'bad'}             | ${''}             | ${false}    | ${'when the issue has an assignee and exemptAllAssignees is disabled, exemptAllIssueAssignees is enabled, exemptAssignees has the same assignee and exemptIssueAssignees has a different assignee'}
    ${911}  | ${false}      | ${['assignee']} | ${false}           | ${undefined}            | ${false}             | ${'assignee'}   | ${'bad'}             | ${''}             | ${true}     | ${'when the issue has an assignee and exemptAllAssignees is disabled, exemptAllPrAssignees is disabled, exemptAssignees has the same assignee and exemptIssueAssignees has a different assignee'}
    ${912}  | ${false}      | ${['assignee']} | ${false}           | ${undefined}            | ${true}              | ${'assignee'}   | ${'bad'}             | ${''}             | ${true}     | ${'when the issue has an assignee and exemptAllAssignees is disabled, exemptAllPrAssignees is enabled, exemptAssignees has the same assignee and exemptIssueAssignees has a different assignee'}
    ${913}  | ${false}      | ${['assignee']} | ${false}           | ${undefined}            | ${false}             | ${'assignee'}   | ${'bad'}             | ${''}             | ${true}     | ${'when the issue has an assignee and exemptAllAssignees is disabled, exemptAllPrAssignees is disabled, exemptAssignees has the same assignee and exemptIssueAssignees has a different assignee'}
    ${1000} | ${false}      | ${['assignee']} | ${false}           | ${undefined}            | ${false}             | ${'assignee'}   | ${'assignee'}        | ${''}             | ${false}    | ${'when the issue has an assignee and exemptAllAssignees is disabled, exemptAllPrAssignees is disabled, exemptAssignees has the same assignee and exemptIssueAssignees has the same assignee'}
    ${1001} | ${false}      | ${['assignee']} | ${false}           | ${undefined}            | ${true}              | ${'assignee'}   | ${'assignee'}        | ${''}             | ${false}    | ${'when the issue has an assignee and exemptAllAssignees is disabled, exemptAllPrAssignees is enabled, exemptAssignees has the same assignee and exemptIssueAssignees has the same assignee'}
    ${1002} | ${false}      | ${['assignee']} | ${true}            | ${undefined}            | ${undefined}         | ${'assignee'}   | ${'assignee'}        | ${''}             | ${false}    | ${'when the issue has an assignee and exemptAllAssignees is enabled, exemptAssignees has the same assignee and exemptIssueAssignees has the same assignee'}
    ${1003} | ${false}      | ${['assignee']} | ${false}           | ${true}                 | ${undefined}         | ${'assignee'}   | ${'assignee'}        | ${''}             | ${false}    | ${'when the issue has an assignee and exemptAllIssueAssignees is enabled, exemptAssignees has the same assignee and exemptIssueAssignees has the same assignee'}
    ${1004} | ${false}      | ${['assignee']} | ${false}           | ${undefined}            | ${true}              | ${'assignee'}   | ${'assignee'}        | ${''}             | ${false}    | ${'when the issue has an assignee and exemptAllPrAssignees is enabled, exemptAssignees has the same assignee and exemptIssueAssignees has the same assignee'}
    ${1005} | ${false}      | ${['assignee']} | ${true}            | ${false}                | ${undefined}         | ${'assignee'}   | ${'assignee'}        | ${''}             | ${false}    | ${'when the issue has an assignee and exemptAllAssignees is enabled, exemptAllIssueAssignees is disabled, exemptAssignees has the same assignee and exemptIssueAssignees has the same assignee'}
    ${1006} | ${false}      | ${['assignee']} | ${true}            | ${true}                 | ${undefined}         | ${'assignee'}   | ${'assignee'}        | ${''}             | ${false}    | ${'when the issue has an assignee and exemptAllAssignees is enabled, exemptAllIssueAssignees is enabled, exemptAssignees has the same assignee and exemptIssueAssignees has the same assignee'}
    ${1007} | ${false}      | ${['assignee']} | ${true}            | ${undefined}            | ${false}             | ${'assignee'}   | ${'assignee'}        | ${''}             | ${false}    | ${'when the issue has an assignee and exemptAllAssignees is enabled, exemptAllPrAssignees is disabled, exemptAssignees has the same assignee and exemptIssueAssignees has the same assignee'}
    ${1008} | ${false}      | ${['assignee']} | ${true}            | ${undefined}            | ${true}              | ${'assignee'}   | ${'assignee'}        | ${''}             | ${false}    | ${'when the issue has an assignee and exemptAllAssignees is enabled, exemptAllPrAssignees is enabled, exemptAssignees has the same assignee and exemptIssueAssignees has the same assignee'}
    ${1009} | ${false}      | ${['assignee']} | ${false}           | ${false}                | ${undefined}         | ${'assignee'}   | ${'assignee'}        | ${''}             | ${false}    | ${'when the issue has an assignee and exemptAllAssignees is disabled, exemptAllIssueAssignees is disabled, exemptAssignees has the same assignee and exemptIssueAssignees has the same assignee'}
    ${1010} | ${false}      | ${['assignee']} | ${false}           | ${true}                 | ${undefined}         | ${'assignee'}   | ${'assignee'}        | ${''}             | ${false}    | ${'when the issue has an assignee and exemptAllAssignees is disabled, exemptAllIssueAssignees is enabled, exemptAssignees has the same assignee and exemptIssueAssignees has the same assignee'}
    ${1011} | ${false}      | ${['assignee']} | ${false}           | ${undefined}            | ${false}             | ${'assignee'}   | ${'assignee'}        | ${''}             | ${false}    | ${'when the issue has an assignee and exemptAllAssignees is disabled, exemptAllPrAssignees is disabled, exemptAssignees has the same assignee and exemptIssueAssignees has the same assignee'}
    ${1012} | ${false}      | ${['assignee']} | ${false}           | ${undefined}            | ${true}              | ${'assignee'}   | ${'assignee'}        | ${''}             | ${false}    | ${'when the issue has an assignee and exemptAllAssignees is disabled, exemptAllPrAssignees is enabled, exemptAssignees has the same assignee and exemptIssueAssignees has the same assignee'}
    ${1013} | ${false}      | ${['assignee']} | ${false}           | ${undefined}            | ${false}             | ${'assignee'}   | ${'assignee'}        | ${''}             | ${false}    | ${'when the issue has an assignee and exemptAllAssignees is disabled, exemptAllPrAssignees is disabled, exemptAssignees has the same assignee and exemptIssueAssignees has the same assignee'}
    ${1100} | ${false}      | ${['assignee']} | ${false}           | ${undefined}            | ${false}             | ${'assignee'}   | ${''}                | ${'bad'}          | ${false}    | ${'when the issue has an assignee and exemptAllAssignees is disabled, exemptAllPrAssignees is disabled, exemptAssignees has the same assignee and exemptPrAssignees has a different assignee'}
    ${1101} | ${false}      | ${['assignee']} | ${false}           | ${undefined}            | ${true}              | ${'assignee'}   | ${''}                | ${'bad'}          | ${false}    | ${'when the issue has an assignee and exemptAllAssignees is disabled, exemptAllPrAssignees is enabled, exemptAssignees has the same assignee and exemptPrAssignees has a different assignee'}
    ${1102} | ${false}      | ${['assignee']} | ${true}            | ${undefined}            | ${undefined}         | ${'assignee'}   | ${''}                | ${'bad'}          | ${false}    | ${'when the issue has an assignee and exemptAllAssignees is enabled, exemptAssignees has the same assignee and exemptPrAssignees has a different assignee'}
    ${1103} | ${false}      | ${['assignee']} | ${false}           | ${true}                 | ${undefined}         | ${'assignee'}   | ${''}                | ${'bad'}          | ${false}    | ${'when the issue has an assignee and exemptAllIssueAssignees is enabled, exemptAssignees has the same assignee and exemptPrAssignees has a different assignee'}
    ${1104} | ${false}      | ${['assignee']} | ${false}           | ${undefined}            | ${true}              | ${'assignee'}   | ${''}                | ${'bad'}          | ${false}    | ${'when the issue has an assignee and exemptAllPrAssignees is enabled, exemptAssignees has the same assignee and exemptPrAssignees has a different assignee'}
    ${1105} | ${false}      | ${['assignee']} | ${true}            | ${false}                | ${undefined}         | ${'assignee'}   | ${''}                | ${'bad'}          | ${false}    | ${'when the issue has an assignee and exemptAllAssignees is enabled, exemptAllIssueAssignees is disabled, exemptAssignees has the same assignee and exemptPrAssignees has a different assignee'}
    ${1106} | ${false}      | ${['assignee']} | ${true}            | ${true}                 | ${undefined}         | ${'assignee'}   | ${''}                | ${'bad'}          | ${false}    | ${'when the issue has an assignee and exemptAllAssignees is enabled, exemptAllIssueAssignees is enabled, exemptAssignees has the same assignee and exemptPrAssignees has a different assignee'}
    ${1107} | ${false}      | ${['assignee']} | ${true}            | ${undefined}            | ${false}             | ${'assignee'}   | ${''}                | ${'bad'}          | ${false}    | ${'when the issue has an assignee and exemptAllAssignees is enabled, exemptAllPrAssignees is disabled, exemptAssignees has the same assignee and exemptPrAssignees has a different assignee'}
    ${1108} | ${false}      | ${['assignee']} | ${true}            | ${undefined}            | ${true}              | ${'assignee'}   | ${''}                | ${'bad'}          | ${false}    | ${'when the issue has an assignee and exemptAllAssignees is enabled, exemptAllPrAssignees is enabled, exemptAssignees has the same assignee and exemptPrAssignees has a different assignee'}
    ${1109} | ${false}      | ${['assignee']} | ${false}           | ${false}                | ${undefined}         | ${'assignee'}   | ${''}                | ${'bad'}          | ${false}    | ${'when the issue has an assignee and exemptAllAssignees is disabled, exemptAllIssueAssignees is disabled, exemptAssignees has the same assignee and exemptPrAssignees has a different assignee'}
    ${1110} | ${false}      | ${['assignee']} | ${false}           | ${true}                 | ${undefined}         | ${'assignee'}   | ${''}                | ${'bad'}          | ${false}    | ${'when the issue has an assignee and exemptAllAssignees is disabled, exemptAllIssueAssignees is enabled, exemptAssignees has the same assignee and exemptPrAssignees has a different assignee'}
    ${1111} | ${false}      | ${['assignee']} | ${false}           | ${undefined}            | ${false}             | ${'assignee'}   | ${''}                | ${'bad'}          | ${false}    | ${'when the issue has an assignee and exemptAllAssignees is disabled, exemptAllPrAssignees is disabled, exemptAssignees has the same assignee and exemptPrAssignees has a different assignee'}
    ${1112} | ${false}      | ${['assignee']} | ${false}           | ${undefined}            | ${true}              | ${'assignee'}   | ${''}                | ${'bad'}          | ${false}    | ${'when the issue has an assignee and exemptAllAssignees is disabled, exemptAllPrAssignees is enabled, exemptAssignees has the same assignee and exemptPrAssignees has a different assignee'}
    ${1113} | ${false}      | ${['assignee']} | ${false}           | ${undefined}            | ${false}             | ${'assignee'}   | ${''}                | ${'bad'}          | ${false}    | ${'when the issue has an assignee and exemptAllAssignees is disabled, exemptAllPrAssignees is disabled, exemptAssignees has the same assignee and exemptPrAssignees has a different assignee'}
    ${1200} | ${false}      | ${['assignee']} | ${false}           | ${undefined}            | ${false}             | ${'assignee'}   | ${''}                | ${'assignee'}     | ${false}    | ${'when the issue has an assignee and exemptAllAssignees is disabled, exemptAllPrAssignees is disabled, exemptAssignees has the same assignee and exemptPrAssignees has the same assignee'}
    ${1201} | ${false}      | ${['assignee']} | ${false}           | ${undefined}            | ${true}              | ${'assignee'}   | ${''}                | ${'assignee'}     | ${false}    | ${'when the issue has an assignee and exemptAllAssignees is disabled, exemptAllPrAssignees is enabled, exemptAssignees has the same assignee and exemptPrAssignees has the same assignee'}
    ${1202} | ${false}      | ${['assignee']} | ${true}            | ${undefined}            | ${undefined}         | ${'assignee'}   | ${''}                | ${'assignee'}     | ${false}    | ${'when the issue has an assignee and exemptAllAssignees is enabled, exemptAssignees has the same assignee and exemptPrAssignees has the same assignee'}
    ${1203} | ${false}      | ${['assignee']} | ${false}           | ${true}                 | ${undefined}         | ${'assignee'}   | ${''}                | ${'assignee'}     | ${false}    | ${'when the issue has an assignee and exemptAllIssueAssignees is enabled, exemptAssignees has the same assignee and exemptPrAssignees has the same assignee'}
    ${1204} | ${false}      | ${['assignee']} | ${false}           | ${undefined}            | ${true}              | ${'assignee'}   | ${''}                | ${'assignee'}     | ${false}    | ${'when the issue has an assignee and exemptAllPrAssignees is enabled, exemptAssignees has the same assignee and exemptPrAssignees has the same assignee'}
    ${1205} | ${false}      | ${['assignee']} | ${true}            | ${false}                | ${undefined}         | ${'assignee'}   | ${''}                | ${'assignee'}     | ${false}    | ${'when the issue has an assignee and exemptAllAssignees is enabled, exemptAllIssueAssignees is disabled, exemptAssignees has the same assignee and exemptPrAssignees has the same assignee'}
    ${1206} | ${false}      | ${['assignee']} | ${true}            | ${true}                 | ${undefined}         | ${'assignee'}   | ${''}                | ${'assignee'}     | ${false}    | ${'when the issue has an assignee and exemptAllAssignees is enabled, exemptAllIssueAssignees is enabled, exemptAssignees has the same assignee and exemptPrAssignees has the same assignee'}
    ${1207} | ${false}      | ${['assignee']} | ${true}            | ${undefined}            | ${false}             | ${'assignee'}   | ${''}                | ${'assignee'}     | ${false}    | ${'when the issue has an assignee and exemptAllAssignees is enabled, exemptAllPrAssignees is disabled, exemptAssignees has the same assignee and exemptPrAssignees has the same assignee'}
    ${1208} | ${false}      | ${['assignee']} | ${true}            | ${undefined}            | ${true}              | ${'assignee'}   | ${''}                | ${'assignee'}     | ${false}    | ${'when the issue has an assignee and exemptAllAssignees is enabled, exemptAllPrAssignees is enabled, exemptAssignees has the same assignee and exemptPrAssignees has the same assignee'}
    ${1209} | ${false}      | ${['assignee']} | ${false}           | ${false}                | ${undefined}         | ${'assignee'}   | ${''}                | ${'assignee'}     | ${false}    | ${'when the issue has an assignee and exemptAllAssignees is disabled, exemptAllIssueAssignees is disabled, exemptAssignees has the same assignee and exemptPrAssignees has the same assignee'}
    ${1210} | ${false}      | ${['assignee']} | ${false}           | ${true}                 | ${undefined}         | ${'assignee'}   | ${''}                | ${'assignee'}     | ${false}    | ${'when the issue has an assignee and exemptAllAssignees is disabled, exemptAllIssueAssignees is enabled, exemptAssignees has the same assignee and exemptPrAssignees has the same assignee'}
    ${1211} | ${false}      | ${['assignee']} | ${false}           | ${undefined}            | ${false}             | ${'assignee'}   | ${''}                | ${'assignee'}     | ${false}    | ${'when the issue has an assignee and exemptAllAssignees is disabled, exemptAllPrAssignees is disabled, exemptAssignees has the same assignee and exemptPrAssignees has the same assignee'}
    ${1212} | ${false}      | ${['assignee']} | ${false}           | ${undefined}            | ${true}              | ${'assignee'}   | ${''}                | ${'assignee'}     | ${false}    | ${'when the issue has an assignee and exemptAllAssignees is disabled, exemptAllPrAssignees is enabled, exemptAssignees has the same assignee and exemptPrAssignees has the same assignee'}
    ${1213} | ${false}      | ${['assignee']} | ${false}           | ${undefined}            | ${false}             | ${'assignee'}   | ${''}                | ${'assignee'}     | ${false}    | ${'when the issue has an assignee and exemptAllAssignees is disabled, exemptAllPrAssignees is disabled, exemptAssignees has the same assignee and exemptPrAssignees has the same assignee'}
    ${1300} | ${true}       | ${[]}           | ${false}           | ${undefined}            | ${undefined}         | ${''}           | ${''}                | ${''}             | ${true}     | ${'when the pull request does not have an assignee'}
    ${1301} | ${true}       | ${[]}           | ${true}            | ${undefined}            | ${undefined}         | ${''}           | ${''}                | ${''}             | ${true}     | ${'when the pull request does not have an assignee and only exemptAllAssignees is enabled'}
    ${1302} | ${true}       | ${[]}           | ${false}           | ${true}                 | ${undefined}         | ${''}           | ${''}                | ${''}             | ${true}     | ${'when the pull request does not have an assignee and only exemptAllIssueAssignees is enabled'}
    ${1303} | ${true}       | ${[]}           | ${false}           | ${undefined}            | ${true}              | ${''}           | ${''}                | ${''}             | ${true}     | ${'when the pull request does not have an assignee and only exemptAllPrAssignees is enabled'}
    ${1304} | ${true}       | ${[]}           | ${true}            | ${false}                | ${undefined}         | ${''}           | ${''}                | ${''}             | ${true}     | ${'when the pull request does not have an assignee and exemptAllAssignees is enabled and exemptAllIssueAssignees is disabled'}
    ${1305} | ${true}       | ${[]}           | ${true}            | ${true}                 | ${undefined}         | ${''}           | ${''}                | ${''}             | ${true}     | ${'when the pull request does not have an assignee and exemptAllAssignees is enabled and exemptAllIssueAssignees is enabled'}
    ${1306} | ${true}       | ${[]}           | ${true}            | ${undefined}            | ${false}             | ${''}           | ${''}                | ${''}             | ${true}     | ${'when the pull request does not have an assignee and exemptAllAssignees is enabled and exemptAllPrAssignees is disabled'}
    ${1307} | ${true}       | ${[]}           | ${true}            | ${undefined}            | ${true}              | ${''}           | ${''}                | ${''}             | ${true}     | ${'when the pull request does not have an assignee and exemptAllAssignees is enabled and exemptAllPrAssignees is enabled'}
    ${1308} | ${true}       | ${[]}           | ${false}           | ${false}                | ${undefined}         | ${''}           | ${''}                | ${''}             | ${true}     | ${'when the pull request does not have an assignee and exemptAllAssignees is disabled and exemptAllIssueAssignees is disabled'}
    ${1309} | ${true}       | ${[]}           | ${false}           | ${true}                 | ${undefined}         | ${''}           | ${''}                | ${''}             | ${true}     | ${'when the pull request does not have an assignee and exemptAllAssignees is disabled and exemptAllIssueAssignees is enabled'}
    ${1400} | ${true}       | ${['assignee']} | ${false}           | ${undefined}            | ${false}             | ${''}           | ${''}                | ${''}             | ${true}     | ${'when the pull request has an assignee and exemptAllAssignees is disabled and exemptAllPrAssignees is disabled'}
    ${1401} | ${true}       | ${['assignee']} | ${false}           | ${undefined}            | ${true}              | ${''}           | ${''}                | ${''}             | ${false}    | ${'when the pull request has an assignee and exemptAllAssignees is disabled and exemptAllPrAssignees is enabled'}
    ${1402} | ${true}       | ${['assignee']} | ${true}            | ${undefined}            | ${undefined}         | ${''}           | ${''}                | ${''}             | ${false}    | ${'when the pull request has an assignee and only exemptAllAssignees is enabled'}
    ${1403} | ${true}       | ${['assignee']} | ${false}           | ${true}                 | ${undefined}         | ${''}           | ${''}                | ${''}             | ${true}     | ${'when the pull request has an assignee and only exemptAllIssueAssignees is enabled'}
    ${1404} | ${true}       | ${['assignee']} | ${false}           | ${undefined}            | ${true}              | ${''}           | ${''}                | ${''}             | ${false}    | ${'when the pull request has an assignee and only exemptAllPrAssignees is enabled'}
    ${1405} | ${true}       | ${['assignee']} | ${true}            | ${false}                | ${undefined}         | ${''}           | ${''}                | ${''}             | ${false}    | ${'when the pull request has an assignee and exemptAllAssignees is enabled and exemptAllIssueAssignees is disabled'}
    ${1406} | ${true}       | ${['assignee']} | ${true}            | ${true}                 | ${undefined}         | ${''}           | ${''}                | ${''}             | ${false}    | ${'when the pull request has an assignee and exemptAllAssignees is enabled and exemptAllIssueAssignees is enabled'}
    ${1407} | ${true}       | ${['assignee']} | ${true}            | ${undefined}            | ${false}             | ${''}           | ${''}                | ${''}             | ${true}     | ${'when the pull request has an assignee and exemptAllAssignees is enabled and exemptAllPrAssignees is disabled'}
    ${1408} | ${true}       | ${['assignee']} | ${true}            | ${undefined}            | ${true}              | ${''}           | ${''}                | ${''}             | ${false}    | ${'when the pull request has an assignee and exemptAllAssignees is enabled and exemptAllPrAssignees is enabled'}
    ${1409} | ${true}       | ${['assignee']} | ${false}           | ${false}                | ${undefined}         | ${''}           | ${''}                | ${''}             | ${true}     | ${'when the pull request has an assignee and exemptAllAssignees is disabled and exemptAllIssueAssignees is disabled'}
    ${1410} | ${true}       | ${['assignee']} | ${false}           | ${true}                 | ${undefined}         | ${''}           | ${''}                | ${''}             | ${true}     | ${'when the pull request has an assignee and exemptAllAssignees is disabled and exemptAllIssueAssignees is enabled'}
    ${1411} | ${true}       | ${['assignee']} | ${false}           | ${undefined}            | ${false}             | ${''}           | ${''}                | ${''}             | ${true}     | ${'when the pull request has an assignee and exemptAllAssignees is disabled and exemptAllPrAssignees is disabled'}
    ${1412} | ${true}       | ${['assignee']} | ${false}           | ${undefined}            | ${true}              | ${''}           | ${''}                | ${''}             | ${false}    | ${'when the pull request has an assignee and exemptAllAssignees is disabled and exemptAllPrAssignees is enabled'}
    ${1413} | ${true}       | ${['assignee']} | ${false}           | ${undefined}            | ${false}             | ${''}           | ${''}                | ${''}             | ${true}     | ${'when the pull request has an assignee and exemptAllAssignees is disabled and exemptAllPrAssignees is disabled'}
    ${1500} | ${true}       | ${['assignee']} | ${false}           | ${undefined}            | ${false}             | ${'bad'}        | ${''}                | ${''}             | ${true}     | ${'when the pull request has an assignee and exemptAllAssignees is disabled, exemptAllPrAssignees is disabled and exemptAssignees has a different assignee'}
    ${1501} | ${true}       | ${['assignee']} | ${false}           | ${undefined}            | ${true}              | ${'bad'}        | ${''}                | ${''}             | ${false}    | ${'when the pull request has an assignee and exemptAllAssignees is disabled, exemptAllPrAssignees is enabled and exemptAssignees has a different assignee'}
    ${1502} | ${true}       | ${['assignee']} | ${true}            | ${undefined}            | ${undefined}         | ${'bad'}        | ${''}                | ${''}             | ${false}    | ${'when the pull request has an assignee and exemptAllAssignees is enabled and exemptAssignees has a different assignee'}
    ${1503} | ${true}       | ${['assignee']} | ${false}           | ${true}                 | ${undefined}         | ${'bad'}        | ${''}                | ${''}             | ${true}     | ${'when the pull request has an assignee and exemptAllIssueAssignees is enabled and exemptAssignees has a different assignee'}
    ${1504} | ${true}       | ${['assignee']} | ${false}           | ${undefined}            | ${true}              | ${'bad'}        | ${''}                | ${''}             | ${false}    | ${'when the pull request has an assignee and exemptAllPrAssignees is enabled and exemptAssignees has a different assignee'}
    ${1505} | ${true}       | ${['assignee']} | ${true}            | ${false}                | ${undefined}         | ${'bad'}        | ${''}                | ${''}             | ${false}    | ${'when the pull request has an assignee and exemptAllAssignees is enabled, exemptAllIssueAssignees is disabled and exemptAssignees has a different assignee'}
    ${1506} | ${true}       | ${['assignee']} | ${true}            | ${true}                 | ${undefined}         | ${'bad'}        | ${''}                | ${''}             | ${false}    | ${'when the pull request has an assignee and exemptAllAssignees is enabled, exemptAllIssueAssignees is enabled and exemptAssignees has a different assignee'}
    ${1507} | ${true}       | ${['assignee']} | ${true}            | ${undefined}            | ${false}             | ${'bad'}        | ${''}                | ${''}             | ${true}     | ${'when the pull request has an assignee and exemptAllAssignees is enabled, exemptAllPrAssignees is disabled and exemptAssignees has a different assignee'}
    ${1508} | ${true}       | ${['assignee']} | ${true}            | ${undefined}            | ${true}              | ${'bad'}        | ${''}                | ${''}             | ${false}    | ${'when the pull request has an assignee and exemptAllAssignees is enabled, exemptAllPrAssignees is enabled and exemptAssignees has a different assignee'}
    ${1509} | ${true}       | ${['assignee']} | ${false}           | ${false}                | ${undefined}         | ${'bad'}        | ${''}                | ${''}             | ${true}     | ${'when the pull request has an assignee and exemptAllAssignees is disabled, exemptAllIssueAssignees is disabled and exemptAssignees has a different assignee'}
    ${1510} | ${true}       | ${['assignee']} | ${false}           | ${true}                 | ${undefined}         | ${'bad'}        | ${''}                | ${''}             | ${true}     | ${'when the pull request has an assignee and exemptAllAssignees is disabled, exemptAllIssueAssignees is enabled and exemptAssignees has a different assignee'}
    ${1511} | ${true}       | ${['assignee']} | ${false}           | ${undefined}            | ${false}             | ${'bad'}        | ${''}                | ${''}             | ${true}     | ${'when the pull request has an assignee and exemptAllAssignees is disabled, exemptAllPrAssignees is disabled and exemptAssignees has a different assignee'}
    ${1513} | ${true}       | ${['assignee']} | ${false}           | ${undefined}            | ${false}             | ${'bad'}        | ${''}                | ${''}             | ${true}     | ${'when the pull request has an assignee and exemptAllAssignees is disabled, exemptAllPrAssignees is disabled and exemptAssignees has a different assignee'}
    ${1600} | ${true}       | ${['assignee']} | ${false}           | ${undefined}            | ${false}             | ${'assignee'}   | ${''}                | ${''}             | ${false}    | ${'when the pull request has an assignee and exemptAllAssignees is disabled, exemptAllPrAssignees is disabled and exemptAssignees has the same assignee'}
    ${1601} | ${true}       | ${['assignee']} | ${false}           | ${undefined}            | ${true}              | ${'assignee'}   | ${''}                | ${''}             | ${false}    | ${'when the pull request has an assignee and exemptAllAssignees is disabled, exemptAllPrAssignees is enabled and exemptAssignees has the same assignee'}
    ${1602} | ${true}       | ${['assignee']} | ${true}            | ${undefined}            | ${undefined}         | ${'assignee'}   | ${''}                | ${''}             | ${false}    | ${'when the pull request has an assignee and exemptAllAssignees is enabled and exemptAssignees has the same assignee'}
    ${1603} | ${true}       | ${['assignee']} | ${false}           | ${true}                 | ${undefined}         | ${'assignee'}   | ${''}                | ${''}             | ${false}    | ${'when the pull request has an assignee and exemptAllIssueAssignees is enabled and exemptAssignees has the same assignee'}
    ${1604} | ${true}       | ${['assignee']} | ${false}           | ${undefined}            | ${true}              | ${'assignee'}   | ${''}                | ${''}             | ${false}    | ${'when the pull request has an assignee and exemptAllPrAssignees is enabled and exemptAssignees has the same assignee'}
    ${1605} | ${true}       | ${['assignee']} | ${true}            | ${false}                | ${undefined}         | ${'assignee'}   | ${''}                | ${''}             | ${false}    | ${'when the pull request has an assignee and exemptAllAssignees is enabled, exemptAllIssueAssignees is disabled and exemptAssignees has the same assignee'}
    ${1606} | ${true}       | ${['assignee']} | ${true}            | ${true}                 | ${undefined}         | ${'assignee'}   | ${''}                | ${''}             | ${false}    | ${'when the pull request has an assignee and exemptAllAssignees is enabled, exemptAllIssueAssignees is enabled and exemptAssignees has the same assignee'}
    ${1607} | ${true}       | ${['assignee']} | ${true}            | ${undefined}            | ${false}             | ${'assignee'}   | ${''}                | ${''}             | ${false}    | ${'when the pull request has an assignee and exemptAllAssignees is enabled, exemptAllPrAssignees is disabled and exemptAssignees has the same assignee'}
    ${1608} | ${true}       | ${['assignee']} | ${true}            | ${undefined}            | ${true}              | ${'assignee'}   | ${''}                | ${''}             | ${false}    | ${'when the pull request has an assignee and exemptAllAssignees is enabled, exemptAllPrAssignees is enabled and exemptAssignees has the same assignee'}
    ${1609} | ${true}       | ${['assignee']} | ${false}           | ${false}                | ${undefined}         | ${'assignee'}   | ${''}                | ${''}             | ${false}    | ${'when the pull request has an assignee and exemptAllAssignees is disabled, exemptAllIssueAssignees is disabled and exemptAssignees has the same assignee'}
    ${1610} | ${true}       | ${['assignee']} | ${false}           | ${true}                 | ${undefined}         | ${'assignee'}   | ${''}                | ${''}             | ${false}    | ${'when the pull request has an assignee and exemptAllAssignees is disabled, exemptAllIssueAssignees is enabled and exemptAssignees has the same assignee'}
    ${1611} | ${true}       | ${['assignee']} | ${false}           | ${undefined}            | ${false}             | ${'assignee'}   | ${''}                | ${''}             | ${false}    | ${'when the pull request has an assignee and exemptAllAssignees is disabled, exemptAllPrAssignees is disabled and exemptAssignees has the same assignee'}
    ${1612} | ${true}       | ${['assignee']} | ${false}           | ${undefined}            | ${true}              | ${'assignee'}   | ${''}                | ${''}             | ${false}    | ${'when the pull request has an assignee and exemptAllAssignees is disabled, exemptAllPrAssignees is enabled and exemptAssignees has the same assignee'}
    ${1613} | ${true}       | ${['assignee']} | ${false}           | ${undefined}            | ${false}             | ${'assignee'}   | ${''}                | ${''}             | ${false}    | ${'when the pull request has an assignee and exemptAllAssignees is disabled, exemptAllPrAssignees is disabled and exemptAssignees has the same assignee'}
    ${1701} | ${true}       | ${['assignee']} | ${false}           | ${undefined}            | ${true}              | ${'bad'}        | ${'bad'}             | ${''}             | ${false}    | ${'when the pull request has an assignee and exemptAllAssignees is disabled, exemptAllPrAssignees is enabled and exemptAssignees and exemptIssueAssignees has a different assignee'}
    ${1702} | ${true}       | ${['assignee']} | ${true}            | ${undefined}            | ${undefined}         | ${'bad'}        | ${'bad'}             | ${''}             | ${false}    | ${'when the pull request has an assignee and exemptAllAssignees is enabled and exemptAssignees and exemptIssueAssignees has a different assignee'}
    ${1703} | ${true}       | ${['assignee']} | ${false}           | ${true}                 | ${undefined}         | ${'bad'}        | ${'bad'}             | ${''}             | ${true}     | ${'when the pull request has an assignee and exemptAllIssueAssignees is enabled and exemptAssignees and exemptIssueAssignees has a different assignee'}
    ${1704} | ${true}       | ${['assignee']} | ${false}           | ${undefined}            | ${true}              | ${'bad'}        | ${'bad'}             | ${''}             | ${false}    | ${'when the pull request has an assignee and exemptAllPrAssignees is enabled and exemptAssignees and exemptIssueAssignees has a different assignee'}
    ${1705} | ${true}       | ${['assignee']} | ${true}            | ${false}                | ${undefined}         | ${'bad'}        | ${'bad'}             | ${''}             | ${false}    | ${'when the pull request has an assignee and exemptAllAssignees is enabled, exemptAllIssueAssignees is disabled and exemptAssignees and exemptIssueAssignees has a different assignee'}
    ${1706} | ${true}       | ${['assignee']} | ${true}            | ${true}                 | ${undefined}         | ${'bad'}        | ${'bad'}             | ${''}             | ${false}    | ${'when the pull request has an assignee and exemptAllAssignees is enabled, exemptAllIssueAssignees is enabled and exemptAssignees and exemptIssueAssignees has a different assignee'}
    ${1707} | ${true}       | ${['assignee']} | ${true}            | ${undefined}            | ${false}             | ${'bad'}        | ${'bad'}             | ${''}             | ${true}     | ${'when the pull request has an assignee and exemptAllAssignees is enabled, exemptAllPrAssignees is disabled and exemptAssignees and exemptIssueAssignees has a different assignee'}
    ${1708} | ${true}       | ${['assignee']} | ${true}            | ${undefined}            | ${true}              | ${'bad'}        | ${'bad'}             | ${''}             | ${false}    | ${'when the pull request has an assignee and exemptAllAssignees is enabled, exemptAllPrAssignees is enabled and exemptAssignees and exemptIssueAssignees has a different assignee'}
    ${1709} | ${true}       | ${['assignee']} | ${false}           | ${false}                | ${undefined}         | ${'bad'}        | ${'bad'}             | ${''}             | ${true}     | ${'when the pull request has an assignee and exemptAllAssignees is disabled, exemptAllIssueAssignees is disabled and exemptAssignees and exemptIssueAssignees has a different assignee'}
    ${1710} | ${true}       | ${['assignee']} | ${false}           | ${true}                 | ${undefined}         | ${'bad'}        | ${'bad'}             | ${''}             | ${true}     | ${'when the pull request has an assignee and exemptAllAssignees is disabled, exemptAllIssueAssignees is enabled and exemptAssignees and exemptIssueAssignees has a different assignee'}
    ${1711} | ${true}       | ${['assignee']} | ${false}           | ${undefined}            | ${false}             | ${'bad'}        | ${'bad'}             | ${''}             | ${true}     | ${'when the pull request has an assignee and exemptAllAssignees is disabled, exemptAllPrAssignees is disabled and exemptAssignees and exemptIssueAssignees has a different assignee'}
    ${1800} | ${true}       | ${['assignee']} | ${true}            | ${undefined}            | ${undefined}         | ${'bad'}        | ${'assignee'}        | ${''}             | ${false}    | ${'when the pull request has an assignee and exemptAllAssignees is enabled, exemptAssignees has a different assignee and exemptIssueAssignees has the same assignee'}
    ${1801} | ${true}       | ${['assignee']} | ${false}           | ${true}                 | ${undefined}         | ${'bad'}        | ${'assignee'}        | ${''}             | ${true}     | ${'when the pull request has an assignee and exemptAllIssueAssignees is enabled, exemptAssignees has a different assignee and exemptIssueAssignees has the same assignee'}
    ${1802} | ${true}       | ${['assignee']} | ${false}           | ${undefined}            | ${true}              | ${'bad'}        | ${'assignee'}        | ${''}             | ${false}    | ${'when the pull request has an assignee and exemptAllPrAssignees is enabled, exemptAssignees has a different assignee and exemptIssueAssignees has the same assignee'}
    ${1803} | ${true}       | ${['assignee']} | ${true}            | ${false}                | ${undefined}         | ${'bad'}        | ${'assignee'}        | ${''}             | ${false}    | ${'when the pull request has an assignee and exemptAllAssignees is enabled, exemptAllIssueAssignees is disabled, exemptAssignees has a different assignee and exemptIssueAssignees has the same assignee'}
    ${1804} | ${true}       | ${['assignee']} | ${true}            | ${true}                 | ${undefined}         | ${'bad'}        | ${'assignee'}        | ${''}             | ${false}    | ${'when the pull request has an assignee and exemptAllAssignees is enabled, exemptAllIssueAssignees is enabled, exemptAssignees has a different assignee and exemptIssueAssignees has the same assignee'}
    ${1805} | ${true}       | ${['assignee']} | ${true}            | ${undefined}            | ${false}             | ${'bad'}        | ${'assignee'}        | ${''}             | ${true}     | ${'when the pull request has an assignee and exemptAllAssignees is enabled, exemptAllPrAssignees is disabled, exemptAssignees has a different assignee and exemptIssueAssignees has the same assignee'}
    ${1806} | ${true}       | ${['assignee']} | ${true}            | ${undefined}            | ${true}              | ${'bad'}        | ${'assignee'}        | ${''}             | ${false}    | ${'when the pull request has an assignee and exemptAllAssignees is enabled, exemptAllPrAssignees is enabled, exemptAssignees has a different assignee and exemptIssueAssignees has the same assignee'}
    ${1807} | ${true}       | ${['assignee']} | ${false}           | ${false}                | ${undefined}         | ${'bad'}        | ${'assignee'}        | ${''}             | ${true}     | ${'when the pull request has an assignee and exemptAllAssignees is disabled, exemptAllIssueAssignees is disabled, exemptAssignees has a different assignee and exemptIssueAssignees has the same assignee'}
    ${1808} | ${true}       | ${['assignee']} | ${false}           | ${true}                 | ${undefined}         | ${'bad'}        | ${'assignee'}        | ${''}             | ${true}     | ${'when the pull request has an assignee and exemptAllAssignees is disabled, exemptAllIssueAssignees is enabled, exemptAssignees has a different assignee and exemptIssueAssignees has the same assignee'}
    ${1809} | ${true}       | ${['assignee']} | ${false}           | ${undefined}            | ${true}              | ${'bad'}        | ${'assignee'}        | ${''}             | ${false}    | ${'when the pull request has an assignee and exemptAllAssignees is disabled, exemptAllPrAssignees is enabled, exemptAssignees has a different assignee and exemptIssueAssignees has the same assignee'}
    ${1810} | ${true}       | ${['assignee']} | ${false}           | ${undefined}            | ${false}             | ${'bad'}        | ${'assignee'}        | ${''}             | ${true}     | ${'when the pull request has an assignee and exemptAllAssignees is disabled, exemptAllPrAssignees is disabled, exemptAssignees has a different assignee and exemptIssueAssignees has the same assignee'}
    ${1900} | ${true}       | ${['assignee']} | ${false}           | ${undefined}            | ${true}              | ${'bad'}        | ${''}                | ${'bad'}          | ${false}    | ${'when the pull request has an assignee and exemptAllAssignees is disabled, exemptAllPrAssignees is enabled and exemptAssignees and exemptPrAssignees has a different assignee'}
    ${1901} | ${true}       | ${['assignee']} | ${true}            | ${undefined}            | ${undefined}         | ${'bad'}        | ${''}                | ${'bad'}          | ${false}    | ${'when the pull request has an assignee and exemptAllAssignees is enabled and exemptAssignees and exemptPrAssignees has a different assignee'}
    ${1902} | ${true}       | ${['assignee']} | ${false}           | ${true}                 | ${undefined}         | ${'bad'}        | ${''}                | ${'bad'}          | ${true}     | ${'when the pull request has an assignee and exemptAllIssueAssignees is enabled and exemptAssignees and exemptPrAssignees has a different assignee'}
    ${1903} | ${true}       | ${['assignee']} | ${false}           | ${undefined}            | ${true}              | ${'bad'}        | ${''}                | ${'bad'}          | ${false}    | ${'when the pull request has an assignee and exemptAllPrAssignees is enabled and exemptAssignees and exemptPrAssignees has a different assignee'}
    ${1904} | ${true}       | ${['assignee']} | ${true}            | ${false}                | ${undefined}         | ${'bad'}        | ${''}                | ${'bad'}          | ${false}    | ${'when the pull request has an assignee and exemptAllAssignees is enabled, exemptAllIssueAssignees is disabled and exemptAssignees and exemptPrAssignees has a different assignee'}
    ${1905} | ${true}       | ${['assignee']} | ${true}            | ${true}                 | ${undefined}         | ${'bad'}        | ${''}                | ${'bad'}          | ${false}    | ${'when the pull request has an assignee and exemptAllAssignees is enabled, exemptAllIssueAssignees is enabled and exemptAssignees and exemptPrAssignees has a different assignee'}
    ${1906} | ${true}       | ${['assignee']} | ${true}            | ${undefined}            | ${false}             | ${'bad'}        | ${''}                | ${'bad'}          | ${true}     | ${'when the pull request has an assignee and exemptAllAssignees is enabled, exemptAllPrAssignees is disabled and exemptAssignees and exemptPrAssignees has a different assignee'}
    ${1907} | ${true}       | ${['assignee']} | ${true}            | ${undefined}            | ${true}              | ${'bad'}        | ${''}                | ${'bad'}          | ${false}    | ${'when the pull request has an assignee and exemptAllAssignees is enabled, exemptAllPrAssignees is enabled and exemptAssignees and exemptPrAssignees has a different assignee'}
    ${1908} | ${true}       | ${['assignee']} | ${false}           | ${false}                | ${undefined}         | ${'bad'}        | ${''}                | ${'bad'}          | ${true}     | ${'when the pull request has an assignee and exemptAllAssignees is disabled, exemptAllIssueAssignees is disabled and exemptAssignees and exemptPrAssignees has a different assignee'}
    ${1909} | ${true}       | ${['assignee']} | ${false}           | ${true}                 | ${undefined}         | ${'bad'}        | ${''}                | ${'bad'}          | ${true}     | ${'when the pull request has an assignee and exemptAllAssignees is disabled, exemptAllIssueAssignees is enabled and exemptAssignees and exemptPrAssignees has a different assignee'}
    ${1910} | ${true}       | ${['assignee']} | ${false}           | ${undefined}            | ${true}              | ${'bad'}        | ${''}                | ${'bad'}          | ${false}    | ${'when the pull request has an assignee and exemptAllAssignees is disabled, exemptAllPrAssignees is enabled and exemptAssignees and exemptPrAssignees has a different assignee'}
    ${1911} | ${true}       | ${['assignee']} | ${false}           | ${undefined}            | ${false}             | ${'bad'}        | ${''}                | ${'bad'}          | ${true}     | ${'when the pull request has an assignee and exemptAllAssignees is disabled, exemptAllPrAssignees is disabled and exemptAssignees and exemptPrAssignees has a different assignee'}
    ${2000} | ${true}       | ${['assignee']} | ${true}            | ${undefined}            | ${undefined}         | ${'bad'}        | ${''}                | ${'assignee'}     | ${false}    | ${'when the pull request has an assignee and exemptAllAssignees is enabled, exemptAssignees has a different assignee and exemptPrAssignees has the same assignee'}
    ${2001} | ${true}       | ${['assignee']} | ${false}           | ${true}                 | ${undefined}         | ${'bad'}        | ${''}                | ${'assignee'}     | ${false}    | ${'when the pull request has an assignee and exemptAllIssueAssignees is enabled, exemptAssignees has a different assignee and exemptPrAssignees has the same assignee'}
    ${2002} | ${true}       | ${['assignee']} | ${false}           | ${undefined}            | ${true}              | ${'bad'}        | ${''}                | ${'assignee'}     | ${false}    | ${'when the pull request has an assignee and exemptAllPrAssignees is enabled, exemptAssignees has a different assignee and exemptPrAssignees has the same assignee'}
    ${2003} | ${true}       | ${['assignee']} | ${true}            | ${false}                | ${undefined}         | ${'bad'}        | ${''}                | ${'assignee'}     | ${false}    | ${'when the pull request has an assignee and exemptAllAssignees is enabled, exemptAllIssueAssignees is disabled, exemptAssignees has a different assignee and exemptPrAssignees has the same assignee'}
    ${2004} | ${true}       | ${['assignee']} | ${true}            | ${true}                 | ${undefined}         | ${'bad'}        | ${''}                | ${'assignee'}     | ${false}    | ${'when the pull request has an assignee and exemptAllAssignees is enabled, exemptAllIssueAssignees is enabled, exemptAssignees has a different assignee and exemptPrAssignees has the same assignee'}
    ${2005} | ${true}       | ${['assignee']} | ${true}            | ${undefined}            | ${false}             | ${'bad'}        | ${''}                | ${'assignee'}     | ${false}    | ${'when the pull request has an assignee and exemptAllAssignees is enabled, exemptAllPrAssignees is disabled, exemptAssignees has a different assignee and exemptPrAssignees has the same assignee'}
    ${2006} | ${true}       | ${['assignee']} | ${true}            | ${undefined}            | ${true}              | ${'bad'}        | ${''}                | ${'assignee'}     | ${false}    | ${'when the pull request has an assignee and exemptAllAssignees is enabled, exemptAllPrAssignees is enabled, exemptAssignees has a different assignee and exemptPrAssignees has the same assignee'}
    ${2007} | ${true}       | ${['assignee']} | ${false}           | ${false}                | ${undefined}         | ${'bad'}        | ${''}                | ${'assignee'}     | ${false}    | ${'when the pull request has an assignee and exemptAllAssignees is disabled, exemptAllIssueAssignees is disabled, exemptAssignees has a different assignee and exemptPrAssignees has the same assignee'}
    ${2008} | ${true}       | ${['assignee']} | ${false}           | ${true}                 | ${undefined}         | ${'bad'}        | ${''}                | ${'assignee'}     | ${false}    | ${'when the pull request has an assignee and exemptAllAssignees is disabled, exemptAllIssueAssignees is enabled, exemptAssignees has a different assignee and exemptPrAssignees has the same assignee'}
    ${2009} | ${true}       | ${['assignee']} | ${false}           | ${undefined}            | ${true}              | ${'bad'}        | ${''}                | ${'assignee'}     | ${false}    | ${'when the pull request has an assignee and exemptAllAssignees is disabled, exemptAllPrAssignees is enabled, exemptAssignees has a different assignee and exemptPrAssignees has the same assignee'}
    ${2010} | ${true}       | ${['assignee']} | ${false}           | ${undefined}            | ${false}             | ${'bad'}        | ${''}                | ${'assignee'}     | ${false}    | ${'when the pull request has an assignee and exemptAllAssignees is disabled, exemptAllPrAssignees is disabled, exemptAssignees has a different assignee and exemptPrAssignees has the same assignee'}
    ${2100} | ${true}       | ${['assignee']} | ${false}           | ${undefined}            | ${true}              | ${'assignee'}   | ${'bad'}             | ${''}             | ${false}    | ${'when the pull request has an assignee and exemptAllAssignees is disabled, exemptAllPrAssignees is enabled, exemptAssignees has the same assignee and exemptIssueAssignees has a different assignee'}
    ${2101} | ${true}       | ${['assignee']} | ${true}            | ${undefined}            | ${undefined}         | ${'assignee'}   | ${'bad'}             | ${''}             | ${false}    | ${'when the pull request has an assignee and exemptAllAssignees is enabled, exemptAssignees has the same assignee and exemptIssueAssignees has a different assignee'}
    ${2102} | ${true}       | ${['assignee']} | ${false}           | ${true}                 | ${undefined}         | ${'assignee'}   | ${'bad'}             | ${''}             | ${false}    | ${'when the pull request has an assignee and exemptAllIssueAssignees is enabled, exemptAssignees has the same assignee and exemptIssueAssignees has a different assignee'}
    ${2103} | ${true}       | ${['assignee']} | ${false}           | ${undefined}            | ${true}              | ${'assignee'}   | ${'bad'}             | ${''}             | ${false}    | ${'when the pull request has an assignee and exemptAllPrAssignees is enabled, exemptAssignees has the same assignee and exemptIssueAssignees has a different assignee'}
    ${2104} | ${true}       | ${['assignee']} | ${true}            | ${false}                | ${undefined}         | ${'assignee'}   | ${'bad'}             | ${''}             | ${false}    | ${'when the pull request has an assignee and exemptAllAssignees is enabled, exemptAllIssueAssignees is disabled, exemptAssignees has the same assignee and exemptIssueAssignees has a different assignee'}
    ${2105} | ${true}       | ${['assignee']} | ${true}            | ${true}                 | ${undefined}         | ${'assignee'}   | ${'bad'}             | ${''}             | ${false}    | ${'when the pull request has an assignee and exemptAllAssignees is enabled, exemptAllIssueAssignees is enabled, exemptAssignees has the same assignee and exemptIssueAssignees has a different assignee'}
    ${2106} | ${true}       | ${['assignee']} | ${true}            | ${undefined}            | ${false}             | ${'assignee'}   | ${'bad'}             | ${''}             | ${false}    | ${'when the pull request has an assignee and exemptAllAssignees is enabled, exemptAllPrAssignees is disabled, exemptAssignees has the same assignee and exemptIssueAssignees has a different assignee'}
    ${2107} | ${true}       | ${['assignee']} | ${true}            | ${undefined}            | ${true}              | ${'assignee'}   | ${'bad'}             | ${''}             | ${false}    | ${'when the pull request has an assignee and exemptAllAssignees is enabled, exemptAllPrAssignees is enabled, exemptAssignees has the same assignee and exemptIssueAssignees has a different assignee'}
    ${2108} | ${true}       | ${['assignee']} | ${false}           | ${false}                | ${undefined}         | ${'assignee'}   | ${'bad'}             | ${''}             | ${false}    | ${'when the pull request has an assignee and exemptAllAssignees is disabled, exemptAllIssueAssignees is disabled, exemptAssignees has the same assignee and exemptIssueAssignees has a different assignee'}
    ${2109} | ${true}       | ${['assignee']} | ${false}           | ${true}                 | ${undefined}         | ${'assignee'}   | ${'bad'}             | ${''}             | ${false}    | ${'when the pull request has an assignee and exemptAllAssignees is disabled, exemptAllIssueAssignees is enabled, exemptAssignees has the same assignee and exemptIssueAssignees has a different assignee'}
    ${2110} | ${true}       | ${['assignee']} | ${false}           | ${undefined}            | ${false}             | ${'assignee'}   | ${'bad'}             | ${''}             | ${false}    | ${'when the pull request has an assignee and exemptAllAssignees is disabled, exemptAllPrAssignees is disabled, exemptAssignees has the same assignee and exemptIssueAssignees has a different assignee'}
    ${2200} | ${true}       | ${['assignee']} | ${false}           | ${undefined}            | ${false}             | ${'assignee'}   | ${'assignee'}        | ${''}             | ${false}    | ${'when the pull request has an assignee and exemptAllAssignees is disabled, exemptAllPrAssignees is disabled, exemptAssignees has the same assignee and exemptIssueAssignees has the same assignee'}
    ${2201} | ${true}       | ${['assignee']} | ${false}           | ${undefined}            | ${true}              | ${'assignee'}   | ${'assignee'}        | ${''}             | ${false}    | ${'when the pull request has an assignee and exemptAllAssignees is disabled, exemptAllPrAssignees is enabled, exemptAssignees has the same assignee and exemptIssueAssignees has the same assignee'}
    ${2202} | ${true}       | ${['assignee']} | ${true}            | ${undefined}            | ${undefined}         | ${'assignee'}   | ${'assignee'}        | ${''}             | ${false}    | ${'when the pull request has an assignee and exemptAllAssignees is enabled, exemptAssignees has the same assignee and exemptIssueAssignees has the same assignee'}
    ${2203} | ${true}       | ${['assignee']} | ${false}           | ${true}                 | ${undefined}         | ${'assignee'}   | ${'assignee'}        | ${''}             | ${false}    | ${'when the pull request has an assignee and exemptAllIssueAssignees is enabled, exemptAssignees has the same assignee and exemptIssueAssignees has the same assignee'}
    ${2204} | ${true}       | ${['assignee']} | ${false}           | ${undefined}            | ${true}              | ${'assignee'}   | ${'assignee'}        | ${''}             | ${false}    | ${'when the pull request has an assignee and exemptAllPrAssignees is enabled, exemptAssignees has the same assignee and exemptIssueAssignees has the same assignee'}
    ${2205} | ${true}       | ${['assignee']} | ${true}            | ${false}                | ${undefined}         | ${'assignee'}   | ${'assignee'}        | ${''}             | ${false}    | ${'when the pull request has an assignee and exemptAllAssignees is enabled, exemptAllIssueAssignees is disabled, exemptAssignees has the same assignee and exemptIssueAssignees has the same assignee'}
    ${2206} | ${true}       | ${['assignee']} | ${true}            | ${true}                 | ${undefined}         | ${'assignee'}   | ${'assignee'}        | ${''}             | ${false}    | ${'when the pull request has an assignee and exemptAllAssignees is enabled, exemptAllIssueAssignees is enabled, exemptAssignees has the same assignee and exemptIssueAssignees has the same assignee'}
    ${2207} | ${true}       | ${['assignee']} | ${true}            | ${undefined}            | ${false}             | ${'assignee'}   | ${'assignee'}        | ${''}             | ${false}    | ${'when the pull request has an assignee and exemptAllAssignees is enabled, exemptAllPrAssignees is disabled, exemptAssignees has the same assignee and exemptIssueAssignees has the same assignee'}
    ${2208} | ${true}       | ${['assignee']} | ${true}            | ${undefined}            | ${true}              | ${'assignee'}   | ${'assignee'}        | ${''}             | ${false}    | ${'when the pull request has an assignee and exemptAllAssignees is enabled, exemptAllPrAssignees is enabled, exemptAssignees has the same assignee and exemptIssueAssignees has the same assignee'}
    ${2209} | ${true}       | ${['assignee']} | ${false}           | ${false}                | ${undefined}         | ${'assignee'}   | ${'assignee'}        | ${''}             | ${false}    | ${'when the pull request has an assignee and exemptAllAssignees is disabled, exemptAllIssueAssignees is disabled, exemptAssignees has the same assignee and exemptIssueAssignees has the same assignee'}
    ${2210} | ${true}       | ${['assignee']} | ${false}           | ${true}                 | ${undefined}         | ${'assignee'}   | ${'assignee'}        | ${''}             | ${false}    | ${'when the pull request has an assignee and exemptAllAssignees is disabled, exemptAllIssueAssignees is enabled, exemptAssignees has the same assignee and exemptIssueAssignees has the same assignee'}
    ${2311} | ${true}       | ${['assignee']} | ${false}           | ${undefined}            | ${false}             | ${'assignee'}   | ${'assignee'}        | ${''}             | ${false}    | ${'when the pull request has an assignee and exemptAllAssignees is disabled, exemptAllPrAssignees is disabled, exemptAssignees has the same assignee and exemptIssueAssignees has the same assignee'}
    ${2312} | ${true}       | ${['assignee']} | ${false}           | ${undefined}            | ${true}              | ${'assignee'}   | ${'assignee'}        | ${''}             | ${false}    | ${'when the pull request has an assignee and exemptAllAssignees is disabled, exemptAllPrAssignees is enabled, exemptAssignees has the same assignee and exemptIssueAssignees has the same assignee'}
    ${2313} | ${true}       | ${['assignee']} | ${false}           | ${undefined}            | ${false}             | ${'assignee'}   | ${'assignee'}        | ${''}             | ${false}    | ${'when the pull request has an assignee and exemptAllAssignees is disabled, exemptAllPrAssignees is disabled, exemptAssignees has the same assignee and exemptIssueAssignees has the same assignee'}
    ${2300} | ${true}       | ${['assignee']} | ${false}           | ${undefined}            | ${false}             | ${'assignee'}   | ${''}                | ${'bad'}          | ${true}     | ${'when the pull request has an assignee and exemptAllAssignees is disabled, exemptAllPrAssignees is disabled, exemptAssignees has the same assignee and exemptPrAssignees has a different assignee'}
    ${2301} | ${true}       | ${['assignee']} | ${false}           | ${undefined}            | ${true}              | ${'assignee'}   | ${''}                | ${'bad'}          | ${false}    | ${'when the pull request has an assignee and exemptAllAssignees is disabled, exemptAllPrAssignees is enabled, exemptAssignees has the same assignee and exemptPrAssignees has a different assignee'}
    ${2302} | ${true}       | ${['assignee']} | ${true}            | ${undefined}            | ${undefined}         | ${'assignee'}   | ${''}                | ${'bad'}          | ${false}    | ${'when the pull request has an assignee and exemptAllAssignees is enabled, exemptAssignees has the same assignee and exemptPrAssignees has a different assignee'}
    ${2303} | ${true}       | ${['assignee']} | ${false}           | ${true}                 | ${undefined}         | ${'assignee'}   | ${''}                | ${'bad'}          | ${true}     | ${'when the pull request has an assignee and exemptAllIssueAssignees is enabled, exemptAssignees has the same assignee and exemptPrAssignees has a different assignee'}
    ${2304} | ${true}       | ${['assignee']} | ${false}           | ${undefined}            | ${true}              | ${'assignee'}   | ${''}                | ${'bad'}          | ${false}    | ${'when the pull request has an assignee and exemptAllPrAssignees is enabled, exemptAssignees has the same assignee and exemptPrAssignees has a different assignee'}
    ${2305} | ${true}       | ${['assignee']} | ${true}            | ${false}                | ${undefined}         | ${'assignee'}   | ${''}                | ${'bad'}          | ${false}    | ${'when the pull request has an assignee and exemptAllAssignees is enabled, exemptAllIssueAssignees is disabled, exemptAssignees has the same assignee and exemptPrAssignees has a different assignee'}
    ${2306} | ${true}       | ${['assignee']} | ${true}            | ${true}                 | ${undefined}         | ${'assignee'}   | ${''}                | ${'bad'}          | ${false}    | ${'when the pull request has an assignee and exemptAllAssignees is enabled, exemptAllIssueAssignees is enabled, exemptAssignees has the same assignee and exemptPrAssignees has a different assignee'}
    ${2307} | ${true}       | ${['assignee']} | ${true}            | ${undefined}            | ${false}             | ${'assignee'}   | ${''}                | ${'bad'}          | ${true}     | ${'when the pull request has an assignee and exemptAllAssignees is enabled, exemptAllPrAssignees is disabled, exemptAssignees has the same assignee and exemptPrAssignees has a different assignee'}
    ${2308} | ${true}       | ${['assignee']} | ${true}            | ${undefined}            | ${true}              | ${'assignee'}   | ${''}                | ${'bad'}          | ${false}    | ${'when the pull request has an assignee and exemptAllAssignees is enabled, exemptAllPrAssignees is enabled, exemptAssignees has the same assignee and exemptPrAssignees has a different assignee'}
    ${2309} | ${true}       | ${['assignee']} | ${false}           | ${false}                | ${undefined}         | ${'assignee'}   | ${''}                | ${'bad'}          | ${true}     | ${'when the pull request has an assignee and exemptAllAssignees is disabled, exemptAllIssueAssignees is disabled, exemptAssignees has the same assignee and exemptPrAssignees has a different assignee'}
    ${2310} | ${true}       | ${['assignee']} | ${false}           | ${true}                 | ${undefined}         | ${'assignee'}   | ${''}                | ${'bad'}          | ${true}     | ${'when the pull request has an assignee and exemptAllAssignees is disabled, exemptAllIssueAssignees is enabled, exemptAssignees has the same assignee and exemptPrAssignees has a different assignee'}
    ${2311} | ${true}       | ${['assignee']} | ${false}           | ${undefined}            | ${true}              | ${'assignee'}   | ${''}                | ${'bad'}          | ${false}    | ${'when the pull request has an assignee and exemptAllAssignees is disabled, exemptAllPrAssignees is enabled, exemptAssignees has the same assignee and exemptPrAssignees has a different assignee'}
    ${2400} | ${true}       | ${['assignee']} | ${false}           | ${undefined}            | ${false}             | ${'assignee'}   | ${''}                | ${'assignee'}     | ${false}    | ${'when the pull request has an assignee and exemptAllAssignees is disabled, exemptAllPrAssignees is disabled, exemptAssignees has the same assignee and exemptPrAssignees has the same assignee'}
    ${2401} | ${true}       | ${['assignee']} | ${false}           | ${undefined}            | ${true}              | ${'assignee'}   | ${''}                | ${'assignee'}     | ${false}    | ${'when the pull request has an assignee and exemptAllAssignees is disabled, exemptAllPrAssignees is enabled, exemptAssignees has the same assignee and exemptPrAssignees has the same assignee'}
    ${2402} | ${true}       | ${['assignee']} | ${true}            | ${undefined}            | ${undefined}         | ${'assignee'}   | ${''}                | ${'assignee'}     | ${false}    | ${'when the pull request has an assignee and exemptAllAssignees is enabled, exemptAssignees has the same assignee and exemptPrAssignees has the same assignee'}
    ${2403} | ${true}       | ${['assignee']} | ${false}           | ${true}                 | ${undefined}         | ${'assignee'}   | ${''}                | ${'assignee'}     | ${false}    | ${'when the pull request has an assignee and exemptAllIssueAssignees is enabled, exemptAssignees has the same assignee and exemptPrAssignees has the same assignee'}
    ${2404} | ${true}       | ${['assignee']} | ${false}           | ${undefined}            | ${true}              | ${'assignee'}   | ${''}                | ${'assignee'}     | ${false}    | ${'when the pull request has an assignee and exemptAllPrAssignees is enabled, exemptAssignees has the same assignee and exemptPrAssignees has the same assignee'}
    ${2405} | ${true}       | ${['assignee']} | ${true}            | ${false}                | ${undefined}         | ${'assignee'}   | ${''}                | ${'assignee'}     | ${false}    | ${'when the pull request has an assignee and exemptAllAssignees is enabled, exemptAllIssueAssignees is disabled, exemptAssignees has the same assignee and exemptPrAssignees has the same assignee'}
    ${2406} | ${true}       | ${['assignee']} | ${true}            | ${true}                 | ${undefined}         | ${'assignee'}   | ${''}                | ${'assignee'}     | ${false}    | ${'when the pull request has an assignee and exemptAllAssignees is enabled, exemptAllIssueAssignees is enabled, exemptAssignees has the same assignee and exemptPrAssignees has the same assignee'}
    ${2407} | ${true}       | ${['assignee']} | ${true}            | ${undefined}            | ${false}             | ${'assignee'}   | ${''}                | ${'assignee'}     | ${false}    | ${'when the pull request has an assignee and exemptAllAssignees is enabled, exemptAllPrAssignees is disabled, exemptAssignees has the same assignee and exemptPrAssignees has the same assignee'}
    ${2408} | ${true}       | ${['assignee']} | ${true}            | ${undefined}            | ${true}              | ${'assignee'}   | ${''}                | ${'assignee'}     | ${false}    | ${'when the pull request has an assignee and exemptAllAssignees is enabled, exemptAllPrAssignees is enabled, exemptAssignees has the same assignee and exemptPrAssignees has the same assignee'}
    ${2409} | ${true}       | ${['assignee']} | ${false}           | ${false}                | ${undefined}         | ${'assignee'}   | ${''}                | ${'assignee'}     | ${false}    | ${'when the pull request has an assignee and exemptAllAssignees is disabled, exemptAllIssueAssignees is disabled, exemptAssignees has the same assignee and exemptPrAssignees has the same assignee'}
    ${2410} | ${true}       | ${['assignee']} | ${false}           | ${true}                 | ${undefined}         | ${'assignee'}   | ${''}                | ${'assignee'}     | ${false}    | ${'when the pull request has an assignee and exemptAllAssignees is disabled, exemptAllIssueAssignees is enabled, exemptAssignees has the same assignee and exemptPrAssignees has the same assignee'}
    ${2411} | ${true}       | ${['assignee']} | ${false}           | ${undefined}            | ${false}             | ${'assignee'}   | ${''}                | ${'assignee'}     | ${false}    | ${'when the pull request has an assignee and exemptAllAssignees is disabled, exemptAllPrAssignees is disabled, exemptAssignees has the same assignee and exemptPrAssignees has the same assignee'}
    ${2412} | ${true}       | ${['assignee']} | ${false}           | ${undefined}            | ${true}              | ${'assignee'}   | ${''}                | ${'assignee'}     | ${false}    | ${'when the pull request has an assignee and exemptAllAssignees is disabled, exemptAllPrAssignees is enabled, exemptAssignees has the same assignee and exemptPrAssignees has the same assignee'}
    ${2413} | ${true}       | ${['assignee']} | ${false}           | ${undefined}            | ${false}             | ${'assignee'}   | ${''}                | ${'assignee'}     | ${false}    | ${'when the pull request has an assignee and exemptAllAssignees is disabled, exemptAllPrAssignees is disabled, exemptAssignees has the same assignee and exemptPrAssignees has the same assignee'}
  `(
    '$description',
    ({
      id,
      isPullRequest,
      assignees,
      exemptAllAssignees,
      exemptAllIssueAssignees,
      exemptAllPrAssignees,
      exemptAssignees,
      exemptIssueAssignees,
      exemptPrAssignees,
      shouldStale
    }: ITestData): void => {
      beforeEach((): void => {
        opts.exemptAllAssignees = exemptAllAssignees;
        opts.exemptAllIssueAssignees = exemptAllIssueAssignees;
        opts.exemptAllPrAssignees = exemptAllPrAssignees;
        opts.exemptAssignees = exemptAssignees;
        opts.exemptIssueAssignees = exemptIssueAssignees;
        opts.exemptPrAssignees = exemptPrAssignees;
        setTestIssueList(isPullRequest, assignees, id);
        setProcessor();
      });

      test(`should${
        shouldStale ? '' : ' not'
      } be marked as stale`, async () => {
        expect.assertions(3);

        await processor.processIssues(1);

        expect(processor.staleIssues).toHaveLength(shouldStale ? 1 : 0);
        expect(processor.closedIssues).toHaveLength(0);
        expect(processor.removedLabelIssues).toHaveLength(0);
      });
    }
  );
});
```

## File: `__tests__/exempt-draft-pr.spec.ts`
```typescript
import {Issue} from '../src/classes/issue';
import {IIssue} from '../src/interfaces/issue';
import {IIssuesProcessorOptions} from '../src/interfaces/issues-processor-options';
import {IPullRequest} from '../src/interfaces/pull-request';
import {IssuesProcessorMock} from './classes/issues-processor-mock';
import {DefaultProcessorOptions} from './constants/default-processor-options';
import {generateIssue} from './functions/generate-issue';
import {alwaysFalseStateMock} from './classes/state-mock';

let issuesProcessorBuilder: IssuesProcessorBuilder;
let issuesProcessor: IssuesProcessorMock;

describe('exempt-draft-pr option', (): void => {
  beforeEach((): void => {
    issuesProcessorBuilder = new IssuesProcessorBuilder();
  });

  describe('when the option "exempt-draft-pr" is disabled', (): void => {
    beforeEach((): void => {
      issuesProcessorBuilder.processDraftPr();
    });

    test('should stale the pull request', async (): Promise<void> => {
      expect.assertions(1);
      issuesProcessor = issuesProcessorBuilder
        .toStalePrs([
          {
            number: 10
          }
        ])
        .build();

      await issuesProcessor.processIssues();

      expect(issuesProcessor.staleIssues).toHaveLength(1);
    });
  });

  describe('when the option "exempt-draft-pr" is enabled', (): void => {
    beforeEach((): void => {
      issuesProcessorBuilder.exemptDraftPr();
    });

    test('should not stale the pull request', async (): Promise<void> => {
      expect.assertions(1);
      issuesProcessor = issuesProcessorBuilder
        .toStalePrs([
          {
            draft: true,
            number: 20
          }
        ])
        .build();

      await issuesProcessor.processIssues();

      expect(issuesProcessor.staleIssues).toHaveLength(0);
    });
  });
});

class IssuesProcessorBuilder {
  private _options: IIssuesProcessorOptions = {
    ...DefaultProcessorOptions
  };
  private _issues: Issue[] = [];

  processDraftPr(): IssuesProcessorBuilder {
    this._options.exemptDraftPr = false;

    return this;
  }

  exemptDraftPr(): IssuesProcessorBuilder {
    this._options.exemptDraftPr = true;

    return this;
  }

  issuesOrPrs(issues: Partial<IIssue>[]): IssuesProcessorBuilder {
    this._issues = issues.map(
      (issue: Readonly<Partial<IIssue>>, index: Readonly<number>): Issue =>
        generateIssue(
          this._options,
          issue.number ?? index,
          issue.title ?? 'dummy-title',
          issue.updated_at ?? new Date().toDateString(),
          issue.created_at ?? new Date().toDateString(),
          !!issue.draft,
          !!issue.pull_request,
          issue.labels ? issue.labels.map(label => label.name || '') : []
        )
    );

    return this;
  }

  prs(issues: Partial<IIssue>[]): IssuesProcessorBuilder {
    this.issuesOrPrs(
      issues.map((issue: Readonly<Partial<IIssue>>): Partial<IIssue> => {
        return {
          ...issue,
          pull_request: {key: 'value'}
        };
      })
    );

    return this;
  }

  toStalePrs(issues: Partial<IIssue>[]): IssuesProcessorBuilder {
    this.prs(
      issues.map((issue: Readonly<Partial<IIssue>>): Partial<IIssue> => {
        return {
          ...issue,
          updated_at: '2020-01-01T17:00:00Z',
          created_at: '2020-01-01T17:00:00Z'
        };
      })
    );

    return this;
  }

  build(): IssuesProcessorMock {
    return new IssuesProcessorMock(
      this._options,
      alwaysFalseStateMock,
      async p => (p === 1 ? this._issues : []),
      async () => [],
      async () => new Date().toDateString(),
      undefined,
      async (): Promise<IPullRequest> => {
        return Promise.resolve({
          number: 0,
          draft: true,
          head: {
            ref: 'ref',
            repo: null
          }
        });
      }
    );
  }
}
```

## File: `__tests__/main.spec.ts`
```typescript
import * as github from '@actions/github';
import {Issue} from '../src/classes/issue';
import {IComment} from '../src/interfaces/comment';
import {IIssuesProcessorOptions} from '../src/interfaces/issues-processor-options';
import {IssuesProcessorMock} from './classes/issues-processor-mock';
import {DefaultProcessorOptions} from './constants/default-processor-options';
import {generateIssue} from './functions/generate-issue';
import {alwaysFalseStateMock} from './classes/state-mock';

test('processing an issue with no label will make it stale and close it, if it is old enough only if days-before-close is set to 0', async () => {
  const opts: IIssuesProcessorOptions = {
    ...DefaultProcessorOptions,
    daysBeforeClose: 0
  };
  const TestIssueList: Issue[] = [
    generateIssue(opts, 1, 'An issue with no label', '2020-01-01T17:00:00Z')
  ];
  const processor = new IssuesProcessorMock(
    opts,
    alwaysFalseStateMock,
    async p => (p === 1 ? TestIssueList : []),
    async () => [],
    async () => new Date().toDateString()
  );

  // process our fake issue list
  await processor.processIssues(1);

  expect(processor.staleIssues).toHaveLength(1);
  expect(processor.closedIssues).toHaveLength(1);
});

test('processing an issue with no label and a start date as ECMAScript epoch in seconds being before the issue creation date will not make it stale nor close it when it is old enough and days-before-close is set to 0', async () => {
  expect.assertions(2);
  const january2000 = 946681200000;
  const opts: IIssuesProcessorOptions = {
    ...DefaultProcessorOptions,
    daysBeforeClose: 0,
    startDate: january2000.toString()
  };
  const TestIssueList: Issue[] = [
    generateIssue(
      opts,
      1,
      'An issue with no label',
      '2020-01-01T17:00:00Z',
      '2020-01-01T17:00:00Z'
    )
  ];
  const processor = new IssuesProcessorMock(
    opts,
    alwaysFalseStateMock,
    async p => (p === 1 ? TestIssueList : []),
    async () => [],
    async () => new Date().toDateString()
  );

  // process our fake issue list
  await processor.processIssues(1);

  expect(processor.staleIssues.length).toStrictEqual(0);
  expect(processor.closedIssues.length).toStrictEqual(0);
});

test('processing an issue with no label and a start date as ECMAScript epoch in seconds being after the issue creation date will not make it stale nor close it when it is old enough and days-before-close is set to 0', async () => {
  expect.assertions(2);
  const january2021 = 1609455600000;
  const opts: IIssuesProcessorOptions = {
    ...DefaultProcessorOptions,
    daysBeforeClose: 0,
    startDate: january2021.toString()
  };
  const TestIssueList: Issue[] = [
    generateIssue(
      opts,
      1,
      'An issue with no label',
      '2020-01-01T17:00:00Z',
      '2020-01-01T17:00:00Z'
    )
  ];
  const processor = new IssuesProcessorMock(
    opts,
    alwaysFalseStateMock,
    async p => (p === 1 ? TestIssueList : []),
    async () => [],
    async () => new Date().toDateString()
  );

  // process our fake issue list
  await processor.processIssues(1);

  expect(processor.staleIssues.length).toStrictEqual(0);
  expect(processor.closedIssues.length).toStrictEqual(0);
});

test('processing an issue with no label and a start date as ECMAScript epoch in milliseconds being before the issue creation date will not make it stale nor close it when it is old enough and days-before-close is set to 0', async () => {
  expect.assertions(2);
  const january2000 = 946681200000000;
  const opts: IIssuesProcessorOptions = {
    ...DefaultProcessorOptions,
    daysBeforeClose: 0,
    startDate: january2000.toString()
  };
  const TestIssueList: Issue[] = [
    generateIssue(
      opts,
      1,
      'An issue with no label',
      '2020-01-01T17:00:00Z',
      '2020-01-01T17:00:00Z'
    )
  ];
  const processor = new IssuesProcessorMock(
    opts,
    alwaysFalseStateMock,
    async p => (p === 1 ? TestIssueList : []),
    async () => [],
    async () => new Date().toDateString()
  );

  // process our fake issue list
  await processor.processIssues(1);

  expect(processor.staleIssues.length).toStrictEqual(0);
  expect(processor.closedIssues.length).toStrictEqual(0);
});

test('processing an issue with no label and a start date as ECMAScript epoch in milliseconds being after the issue creation date will not make it stale nor close it when it is old enough and days-before-close is set to 0', async () => {
  expect.assertions(2);
  const january2021 = 1609455600000;
  const opts: IIssuesProcessorOptions = {
    ...DefaultProcessorOptions,
    daysBeforeClose: 0,
    startDate: january2021.toString()
  };
  const TestIssueList: Issue[] = [
    generateIssue(
      opts,
      1,
      'An issue with no label',
      '2020-01-01T17:00:00Z',
      '2020-01-01T17:00:00Z'
    )
  ];
  const processor = new IssuesProcessorMock(
    opts,
    alwaysFalseStateMock,
    async p => (p === 1 ? TestIssueList : []),
    async () => [],
    async () => new Date().toDateString()
  );

  // process our fake issue list
  await processor.processIssues(1);

  expect(processor.staleIssues.length).toStrictEqual(0);
  expect(processor.closedIssues.length).toStrictEqual(0);
});

test('processing an issue with no label and a start date as ISO 8601 being before the issue creation date will make it stale and close it when it is old enough and days-before-close is set to 0', async () => {
  expect.assertions(2);
  const january2000 = '2000-01-01T00:00:00Z';
  const opts: IIssuesProcessorOptions = {
    ...DefaultProcessorOptions,
    daysBeforeClose: 0,
    startDate: january2000.toString()
  };
  const TestIssueList: Issue[] = [
    generateIssue(
      opts,
      1,
      'An issue with no label',
      '2020-01-01T17:00:00Z',
      '2020-01-01T17:00:00Z'
    )
  ];
  const processor = new IssuesProcessorMock(
    opts,
    alwaysFalseStateMock,
    async p => (p === 1 ? TestIssueList : []),
    async () => [],
    async () => new Date().toDateString()
  );

  // process our fake issue list
  await processor.processIssues(1);

  expect(processor.staleIssues.length).toStrictEqual(1);
  expect(processor.closedIssues.length).toStrictEqual(1);
});

test('processing an issue with no label and a start date as ISO 8601 being after the issue creation date will not make it stale nor close it when it is old enough and days-before-close is set to 0', async () => {
  expect.assertions(2);
  const january2021 = '2021-01-01T00:00:00Z';
  const opts: IIssuesProcessorOptions = {
    ...DefaultProcessorOptions,
    daysBeforeClose: 0,
    startDate: january2021.toString()
  };
  const TestIssueList: Issue[] = [
    generateIssue(
      opts,
      1,
      'An issue with no label',
      '2020-01-01T17:00:00Z',
      '2020-01-01T17:00:00Z'
    )
  ];
  const processor = new IssuesProcessorMock(
    opts,
    alwaysFalseStateMock,
    async p => (p === 1 ? TestIssueList : []),
    async () => [],
    async () => new Date().toDateString()
  );

  // process our fake issue list
  await processor.processIssues(1);

  expect(processor.staleIssues.length).toStrictEqual(0);
  expect(processor.closedIssues.length).toStrictEqual(0);
});

test('processing an issue with no label and a start date as RFC 2822 being before the issue creation date will make it stale and close it when it is old enough and days-before-close is set to 0', async () => {
  expect.assertions(2);
  const january2000 = 'January 1, 2000 00:00:00';
  const opts: IIssuesProcessorOptions = {
    ...DefaultProcessorOptions,
    daysBeforeClose: 0,
    startDate: january2000.toString()
  };
  const TestIssueList: Issue[] = [
    generateIssue(
      opts,
      1,
      'An issue with no label',
      '2020-01-01T17:00:00Z',
      '2020-01-01T17:00:00Z'
    )
  ];
  const processor = new IssuesProcessorMock(
    opts,
    alwaysFalseStateMock,
    async p => (p === 1 ? TestIssueList : []),
    async () => [],
    async () => new Date().toDateString()
  );

  // process our fake issue list
  await processor.processIssues(1);

  expect(processor.staleIssues.length).toStrictEqual(1);
  expect(processor.closedIssues.length).toStrictEqual(1);
});

test('processing an issue with no label and a start date as RFC 2822 being after the issue creation date will not make it stale nor close it when it is old enough and days-before-close is set to 0', async () => {
  expect.assertions(2);
  const january2021 = 'January 1, 2021 00:00:00';
  const opts: IIssuesProcessorOptions = {
    ...DefaultProcessorOptions,
    daysBeforeClose: 0,
    startDate: january2021.toString()
  };
  const TestIssueList: Issue[] = [
    generateIssue(
      opts,
      1,
      'An issue with no label',
      '2020-01-01T17:00:00Z',
      '2020-01-01T17:00:00Z'
    )
  ];
  const processor = new IssuesProcessorMock(
    opts,
    alwaysFalseStateMock,
    async p => (p === 1 ? TestIssueList : []),
    async () => [],
    async () => new Date().toDateString()
  );

  // process our fake issue list
  await processor.processIssues(1);

  expect(processor.staleIssues.length).toStrictEqual(0);
  expect(processor.closedIssues.length).toStrictEqual(0);
});

test('processing an issue with no label will make it stale and close it, if it is old enough only if days-before-close is set to > 0 and days-before-issue-close is set to 0', async () => {
  const opts: IIssuesProcessorOptions = {
    ...DefaultProcessorOptions,
    daysBeforeClose: 1,
    daysBeforeIssueClose: 0
  };
  const TestIssueList: Issue[] = [
    generateIssue(opts, 1, 'An issue with no label', '2020-01-01T17:00:00Z')
  ];
  const processor = new IssuesProcessorMock(
    opts,
    alwaysFalseStateMock,
    async p => (p === 1 ? TestIssueList : []),
    async () => [],
    async () => new Date().toDateString()
  );

  // process our fake issue list
  await processor.processIssues(1);

  expect(processor.staleIssues).toHaveLength(1);
  expect(processor.closedIssues).toHaveLength(1);
  expect(processor.deletedBranchIssues).toHaveLength(0);
});

test('processing an issue with no label will make it stale and not close it, if it is old enough only if days-before-close is set to > 0 and days-before-issue-close is set to > 0', async () => {
  const opts: IIssuesProcessorOptions = {
    ...DefaultProcessorOptions,
    daysBeforeClose: 1,
    daysBeforeIssueClose: 1
  };
  const TestIssueList: Issue[] = [
    generateIssue(opts, 1, 'An issue with no label', '2020-01-01T17:00:00Z')
  ];
  const processor = new IssuesProcessorMock(
    opts,
    alwaysFalseStateMock,
    async p => (p === 1 ? TestIssueList : []),
    async () => [],
    async () => new Date().toDateString()
  );

  // process our fake issue list
  await processor.processIssues(1);

  expect(processor.staleIssues).toHaveLength(1);
  expect(processor.closedIssues).toHaveLength(0);
});

test('processing an issue with no label will make it stale and not close it if days-before-close is set to > 0', async () => {
  const opts: IIssuesProcessorOptions = {
    ...DefaultProcessorOptions,
    daysBeforeClose: 15
  };
  const TestIssueList: Issue[] = [
    generateIssue(opts, 1, 'An issue with no label', '2020-01-01T17:00:00Z')
  ];
  const processor = new IssuesProcessorMock(
    opts,
    alwaysFalseStateMock,
    async p => (p === 1 ? TestIssueList : []),
    async () => [],
    async () => new Date().toDateString()
  );

  // process our fake issue list
  await processor.processIssues(1);

  expect(processor.staleIssues).toHaveLength(1);
  expect(processor.closedIssues).toHaveLength(0);
});

test('processing an issue with no label will make it stale and not close it if days-before-close is set to -1 and days-before-issue-close is set to > 0', async () => {
  const opts: IIssuesProcessorOptions = {
    ...DefaultProcessorOptions,
    daysBeforeClose: -1,
    daysBeforeIssueClose: 15
  };
  const TestIssueList: Issue[] = [
    generateIssue(opts, 1, 'An issue with no label', '2020-01-01T17:00:00Z')
  ];
  const processor = new IssuesProcessorMock(
    opts,
    alwaysFalseStateMock,
    async p => (p === 1 ? TestIssueList : []),
    async () => [],
    async () => new Date().toDateString()
  );

  // process our fake issue list
  await processor.processIssues(1);

  expect(processor.staleIssues).toHaveLength(1);
  expect(processor.closedIssues).toHaveLength(0);
});

test('processing an issue with no label will not make it stale if days-before-stale is set to -1', async () => {
  const opts: IIssuesProcessorOptions = {
    ...DefaultProcessorOptions,
    staleIssueMessage: '',
    daysBeforeStale: -1
  };
  const TestIssueList: Issue[] = [
    generateIssue(opts, 1, 'An issue with no label', '2020-01-01T17:00:00Z')
  ];
  const processor = new IssuesProcessorMock(
    opts,
    alwaysFalseStateMock,
    async p => (p === 1 ? TestIssueList : []),
    async () => [],
    async () => new Date().toDateString()
  );

  // process our fake issue list
  await processor.processIssues(1);

  expect(processor.staleIssues).toHaveLength(0);
  expect(processor.closedIssues).toHaveLength(0);
});

test('processing an issue with no label will not make it stale if days-before-stale and days-before-issue-stale are set to -1', async () => {
  const opts: IIssuesProcessorOptions = {
    ...DefaultProcessorOptions,
    staleIssueMessage: '',
    daysBeforeStale: -1,
    daysBeforeIssueStale: -1
  };
  const TestIssueList: Issue[] = [
    generateIssue(opts, 1, 'An issue with no label', '2020-01-01T17:00:00Z')
  ];
  const processor = new IssuesProcessorMock(
    opts,
    alwaysFalseStateMock,
    async p => (p === 1 ? TestIssueList : []),
    async () => [],
    async () => new Date().toDateString()
  );

  // process our fake issue list
  await processor.processIssues(1);

  expect(processor.staleIssues).toHaveLength(0);
  expect(processor.closedIssues).toHaveLength(0);
});

test('processing an issue with no label will make it stale but not close it', async () => {
  // issue should be from 2 days ago so it will be
  // stale but not close-able, based on default settings
  const issueDate = new Date();
  issueDate.setDate(issueDate.getDate() - 2);
  const TestIssueList: Issue[] = [
    generateIssue(
      DefaultProcessorOptions,
      1,
      'An issue with no label',
      issueDate.toDateString()
    )
  ];
  const processor = new IssuesProcessorMock(
    DefaultProcessorOptions,
    alwaysFalseStateMock,
    async p => (p === 1 ? TestIssueList : []),
    async () => [],
    async () => new Date().toDateString()
  );

  // process our fake issue list
  await processor.processIssues(1);

  expect(processor.staleIssues).toHaveLength(1);
  expect(processor.closedIssues).toHaveLength(0);
});

test('processing a stale issue will close it', async () => {
  const opts: IIssuesProcessorOptions = {
    ...DefaultProcessorOptions,
    daysBeforeClose: 30
  };
  const TestIssueList: Issue[] = [
    generateIssue(
      opts,
      1,
      'A stale issue that should be closed',
      '2020-01-01T17:00:00Z',
      '2020-01-01T17:00:00Z',
      false,
      false,
      ['Stale']
    )
  ];
  const processor = new IssuesProcessorMock(
    opts,
    alwaysFalseStateMock,
    async p => (p === 1 ? TestIssueList : []),
    async () => [],
    async () => new Date().toDateString()
  );

  // process our fake issue list
  await processor.processIssues(1);

  expect(processor.staleIssues).toHaveLength(0);
  expect(processor.closedIssues).toHaveLength(1);
});

test('processing a stale issue containing a space in the label will close it', async () => {
  const opts: IIssuesProcessorOptions = {
    ...DefaultProcessorOptions,
    staleIssueLabel: 'state: stale'
  };
  const TestIssueList: Issue[] = [
    generateIssue(
      opts,
      1,
      'A stale issue that should be closed',
      '2020-01-01T17:00:00Z',
      '2020-01-01T17:00:00Z',
      false,
      false,
      ['state: stale']
    )
  ];
  const processor = new IssuesProcessorMock(
    opts,
    alwaysFalseStateMock,
    async p => (p === 1 ? TestIssueList : []),
    async () => [],
    async () => new Date().toDateString()
  );

  // process our fake issue list
  await processor.processIssues(1);

  expect(processor.staleIssues).toHaveLength(0);
  expect(processor.closedIssues).toHaveLength(1);
});

test('processing a stale issue containing a slash in the label will close it', async () => {
  const opts: IIssuesProcessorOptions = {
    ...DefaultProcessorOptions,
    staleIssueLabel: 'lifecycle/stale'
  };
  const TestIssueList: Issue[] = [
    generateIssue(
      opts,
      1,
      'A stale issue that should be closed',
      '2020-01-01T17:00:00Z',
      '2020-01-01T17:00:00Z',
      false,
      false,
      ['lifecycle/stale']
    )
  ];
  const processor = new IssuesProcessorMock(
    opts,
    alwaysFalseStateMock,
    async p => (p === 1 ? TestIssueList : []),
    async () => [],
    async () => new Date().toDateString()
  );

  // process our fake issue list
  await processor.processIssues(1);

  expect(processor.staleIssues).toHaveLength(0);
  expect(processor.closedIssues).toHaveLength(1);
});

test('processing a stale issue will close it when days-before-issue-stale override days-before-stale', async () => {
  const opts: IIssuesProcessorOptions = {
    ...DefaultProcessorOptions,
    daysBeforeClose: 30,
    daysBeforeIssueStale: 30
  };
  const TestIssueList: Issue[] = [
    generateIssue(
      opts,
      1,
      'A stale issue that should be closed',
      '2020-01-01T17:00:00Z',
      '2020-01-01T17:00:00Z',
      false,
      false,
      ['Stale']
    )
  ];
  const processor = new IssuesProcessorMock(
    opts,
    alwaysFalseStateMock,
    async p => (p === 1 ? TestIssueList : []),
    async () => [],
    async () => new Date().toDateString()
  );

  // process our fake issue list
  await processor.processIssues(1);

  expect(processor.staleIssues).toHaveLength(0);
  expect(processor.closedIssues).toHaveLength(1);
});

test('processing a stale PR will close it', async () => {
  const opts: IIssuesProcessorOptions = {
    ...DefaultProcessorOptions,
    daysBeforeClose: 30
  };
  const TestIssueList: Issue[] = [
    generateIssue(
      opts,
      1,
      'A stale PR that should be closed',
      '2020-01-01T17:00:00Z',
      '2020-01-01T17:00:00Z',
      false,
      true,
      ['Stale']
    )
  ];
  const processor = new IssuesProcessorMock(
    opts,
    alwaysFalseStateMock,
    async p => (p === 1 ? TestIssueList : []),
    async () => [],
    async () => new Date().toDateString()
  );

  // process our fake issue list
  await processor.processIssues(1);

  expect(processor.staleIssues).toHaveLength(0);
  expect(processor.closedIssues).toHaveLength(1);
});

test('processing a stale PR will close it when days-before-pr-stale override days-before-stale', async () => {
  const opts: IIssuesProcessorOptions = {
    ...DefaultProcessorOptions,
    daysBeforeClose: 30,
    daysBeforePrClose: 30
  };
  const TestIssueList: Issue[] = [
    generateIssue(
      opts,
      1,
      'A stale PR that should be closed',
      '2020-01-01T17:00:00Z',
      '2020-01-01T17:00:00Z',
      false,
      true,
      ['Stale']
    )
  ];
  const processor = new IssuesProcessorMock(
    opts,
    alwaysFalseStateMock,
    async p => (p === 1 ? TestIssueList : []),
    async () => [],
    async () => new Date().toDateString()
  );

  // process our fake issue list
  await processor.processIssues(1);

  expect(processor.staleIssues).toHaveLength(0);
  expect(processor.closedIssues).toHaveLength(1);
});

test('processing a stale issue will close it even if configured not to mark as stale', async () => {
  const opts = {
    ...DefaultProcessorOptions,
    daysBeforeStale: -1,
    staleIssueMessage: ''
  };
  const TestIssueList: Issue[] = [
    generateIssue(
      opts,
      1,
      'An issue with no label',
      '2020-01-01T17:00:00Z',
      '2020-01-01T17:00:00Z',
      false,
      false,
      ['Stale']
    )
  ];
  const processor = new IssuesProcessorMock(
    opts,
    alwaysFalseStateMock,
    async p => (p === 1 ? TestIssueList : []),
    async () => [],
    async () => new Date().toDateString()
  );

  // process our fake issue list
  await processor.processIssues(1);

  expect(processor.staleIssues).toHaveLength(0);
  expect(processor.closedIssues).toHaveLength(1);
});

test('processing a stale issue will close it even if configured not to mark as stale when days-before-issue-stale override days-before-stale', async () => {
  const opts = {
    ...DefaultProcessorOptions,
    daysBeforeStale: 0,
    daysBeforeIssueStale: -1,
    staleIssueMessage: ''
  };
  const TestIssueList: Issue[] = [
    generateIssue(
      opts,
      1,
      'An issue with no label',
      '2020-01-01T17:00:00Z',
      '2020-01-01T17:00:00Z',
      false,
      false,
      ['Stale']
    )
  ];
  const processor = new IssuesProcessorMock(
    opts,
    alwaysFalseStateMock,
    async p => (p === 1 ? TestIssueList : []),
    async () => [],
    async () => new Date().toDateString()
  );

  // process our fake issue list
  await processor.processIssues(1);

  expect(processor.staleIssues).toHaveLength(0);
  expect(processor.closedIssues).toHaveLength(1);
});

test('processing a stale PR will close it even if configured not to mark as stale', async () => {
  const opts = {
    ...DefaultProcessorOptions,
    daysBeforeStale: -1,
    stalePrMessage: ''
  };
  const TestIssueList: Issue[] = [
    generateIssue(
      opts,
      1,
      'An issue with no label',
      '2020-01-01T17:00:00Z',
      '2020-01-01T17:00:00Z',
      false,
      true,
      ['Stale']
    )
  ];
  const processor = new IssuesProcessorMock(
    opts,
    alwaysFalseStateMock,
    async p => (p === 1 ? TestIssueList : []),
    async () => [],
    async () => new Date().toDateString()
  );

  // process our fake issue list
  await processor.processIssues(1);

  expect(processor.staleIssues).toHaveLength(0);
  expect(processor.closedIssues).toHaveLength(1);
});

test('processing a stale PR will close it even if configured not to mark as stale when days-before-pr-stale override days-before-stale', async () => {
  const opts = {
    ...DefaultProcessorOptions,
    daysBeforeStale: 0,
    daysBeforePrStale: -1,
    stalePrMessage: ''
  };
  const TestIssueList: Issue[] = [
    generateIssue(
      opts,
      1,
      'An issue with no label',
      '2020-01-01T17:00:00Z',
      '2020-01-01T17:00:00Z',
      false,
      true,
      ['Stale']
    )
  ];
  const processor = new IssuesProcessorMock(
    opts,
    alwaysFalseStateMock,
    async p => (p === 1 ? TestIssueList : []),
    async () => [],
    async () => new Date().toDateString()
  );

  // process our fake issue list
  await processor.processIssues(1);

  expect(processor.staleIssues).toHaveLength(0);
  expect(processor.closedIssues).toHaveLength(1);
});

test('closed issues will not be marked stale', async () => {
  const TestIssueList: Issue[] = [
    generateIssue(
      DefaultProcessorOptions,
      1,
      'A closed issue that will not be marked',
      '2020-01-01T17:00:00Z',
      '2020-01-01T17:00:00Z',
      false,
      false,
      [],
      true
    )
  ];
  const processor = new IssuesProcessorMock(
    DefaultProcessorOptions,
    alwaysFalseStateMock,
    async p => (p === 1 ? TestIssueList : []),
    async () => []
  );

  // process our fake issue list
  await processor.processIssues(1);

  expect(processor.staleIssues).toHaveLength(0);
  expect(processor.closedIssues).toHaveLength(0);
});

test('stale closed issues will not be closed', async () => {
  const TestIssueList: Issue[] = [
    generateIssue(
      DefaultProcessorOptions,
      1,
      'A stale closed issue',
      '2020-01-01T17:00:00Z',
      '2020-01-01T17:00:00Z',
      false,
      false,
      ['Stale'],
      true
    )
  ];
  const processor = new IssuesProcessorMock(
    DefaultProcessorOptions,
    alwaysFalseStateMock,
    async p => (p === 1 ? TestIssueList : []),
    async () => [],
    async () => new Date().toDateString()
  );

  // process our fake issue list
  await processor.processIssues(1);

  expect(processor.staleIssues).toHaveLength(0);
  expect(processor.closedIssues).toHaveLength(0);
});

test('closed prs will not be marked stale', async () => {
  const TestIssueList: Issue[] = [
    generateIssue(
      DefaultProcessorOptions,
      1,
      'A closed PR that will not be marked',
      '2020-01-01T17:00:00Z',
      '2020-01-01T17:00:00Z',
      false,
      true,
      [],
      true
    )
  ];
  const processor = new IssuesProcessorMock(
    DefaultProcessorOptions,
    alwaysFalseStateMock,
    async p => (p === 1 ? TestIssueList : []),
    async () => [],
    async () => new Date().toDateString()
  );

  // process our fake issue list
  await processor.processIssues(1);

  expect(processor.staleIssues).toHaveLength(0);
  expect(processor.closedIssues).toHaveLength(0);
});

test('stale closed prs will not be closed', async () => {
  const TestIssueList: Issue[] = [
    generateIssue(
      DefaultProcessorOptions,
      1,
      'A stale closed PR that will not be closed again',
      '2020-01-01T17:00:00Z',
      '2020-01-01T17:00:00Z',
      false,
      true,
      ['Stale'],
      true
    )
  ];
  const processor = new IssuesProcessorMock(
    DefaultProcessorOptions,
    alwaysFalseStateMock,
    async p => (p === 1 ? TestIssueList : []),
    async () => [],
    async () => new Date().toDateString()
  );

  // process our fake issue list
  await processor.processIssues(1);

  expect(processor.staleIssues).toHaveLength(0);
  expect(processor.closedIssues).toHaveLength(0);
});

test('locked issues will not be marked stale', async () => {
  const TestIssueList: Issue[] = [
    generateIssue(
      DefaultProcessorOptions,
      1,
      'A locked issue that will not be stale',
      '2020-01-01T17:00:00Z',
      '2020-01-01T17:00:00Z',
      false,
      false,
      [],
      false,
      true
    )
  ];
  const processor = new IssuesProcessorMock(
    DefaultProcessorOptions,
    alwaysFalseStateMock,
    async p => (p === 1 ? TestIssueList : [])
  );

  // process our fake issue list
  await processor.processIssues(1);

  expect(processor.staleIssues).toHaveLength(0);
  expect(processor.closedIssues).toHaveLength(0);
});

test('stale locked issues will not be closed', async () => {
  const TestIssueList: Issue[] = [
    generateIssue(
      DefaultProcessorOptions,
      1,
      'A stale locked issue that will not be closed',
      '2020-01-01T17:00:00Z',
      '2020-01-01T17:00:00Z',
      false,
      false,
      ['Stale'],
      false,
      true
    )
  ];
  const processor = new IssuesProcessorMock(
    DefaultProcessorOptions,
    alwaysFalseStateMock,
    async p => (p === 1 ? TestIssueList : []),
    async () => [],
    async () => new Date().toDateString()
  );

  // process our fake issue list
  await processor.processIssues(1);

  expect(processor.staleIssues).toHaveLength(0);
  expect(processor.closedIssues).toHaveLength(0);
});

test('locked prs will not be marked stale', async () => {
  const TestIssueList: Issue[] = [
    generateIssue(
      DefaultProcessorOptions,
      1,
      'A locked PR that will not be marked stale',
      '2020-01-01T17:00:00Z',
      '2020-01-01T17:00:00Z',
      false,
      true,
      [],
      false,
      true
    )
  ];
  const processor = new IssuesProcessorMock(
    DefaultProcessorOptions,
    alwaysFalseStateMock,
    async p => (p === 1 ? TestIssueList : [])
  );

  // process our fake issue list
  await processor.processIssues(1);

  expect(processor.staleIssues).toHaveLength(0);
  expect(processor.closedIssues).toHaveLength(0);
});

test('stale locked prs will not be closed', async () => {
  const TestIssueList: Issue[] = [
    generateIssue(
      DefaultProcessorOptions,
      1,
      'A stale locked PR that will not be closed',
      '2020-01-01T17:00:00Z',
      '2020-01-01T17:00:00Z',
      false,
      true,
      ['Stale'],
      false,
      true
    )
  ];
  const processor = new IssuesProcessorMock(
    DefaultProcessorOptions,
    alwaysFalseStateMock,
    async p => (p === 1 ? TestIssueList : []),
    async () => [],
    async () => new Date().toDateString()
  );

  // process our fake issue list
  await processor.processIssues(1);

  expect(processor.staleIssues).toHaveLength(0);
  expect(processor.closedIssues).toHaveLength(0);
});

test('exempt issue labels will not be marked stale', async () => {
  expect.assertions(3);
  const opts = {...DefaultProcessorOptions};
  opts.exemptIssueLabels = 'Exempt';
  const TestIssueList: Issue[] = [
    generateIssue(
      opts,
      1,
      'My first issue',
      '2020-01-01T17:00:00Z',
      '2020-01-01T17:00:00Z',
      false,
      false,
      ['Exempt']
    )
  ];
  const processor = new IssuesProcessorMock(
    opts,
    alwaysFalseStateMock,
    async p => (p === 1 ? TestIssueList : []),
    async () => [],
    async () => new Date().toDateString()
  );

  // process our fake issue list
  await processor.processIssues(1);

  expect(processor.staleIssues.length).toStrictEqual(0);
  expect(processor.closedIssues.length).toStrictEqual(0);
  expect(processor.removedLabelIssues.length).toStrictEqual(0);
});

test('exempt issue labels will not be marked stale (multi issue label with spaces)', async () => {
  const opts = {...DefaultProcessorOptions};
  opts.exemptIssueLabels = 'Exempt, Cool, None';
  const TestIssueList: Issue[] = [
    generateIssue(
      opts,
      1,
      'My first issue',
      '2020-01-01T17:00:00Z',
      '2020-01-01T17:00:00Z',
      false,
      false,
      ['Cool']
    )
  ];
  const processor = new IssuesProcessorMock(
    opts,
    alwaysFalseStateMock,
    async p => (p === 1 ? TestIssueList : []),
    async () => [],
    async () => new Date().toDateString()
  );

  // process our fake issue list
  await processor.processIssues(1);

  expect(processor.staleIssues).toHaveLength(0);
  expect(processor.closedIssues).toHaveLength(0);
});

test('exempt issue labels will not be marked stale (multi issue label)', async () => {
  const opts = {...DefaultProcessorOptions};
  opts.exemptIssueLabels = 'Exempt,Cool,None';
  const TestIssueList: Issue[] = [
    generateIssue(
      opts,
      1,
      'My first issue',
      '2020-01-01T17:00:00Z',
      '2020-01-01T17:00:00Z',
      false,
      false,
      ['Cool']
    )
  ];
  const processor = new IssuesProcessorMock(
    opts,
    alwaysFalseStateMock,
    async p => (p === 1 ? TestIssueList : []),
    async () => [],
    async () => new Date().toDateString()
  );

  // process our fake issue list
  await processor.processIssues(1);

  expect(processor.staleIssues).toHaveLength(0);
  expect(processor.closedIssues).toHaveLength(0);
  expect(processor.removedLabelIssues).toHaveLength(0);
});

test('exempt pr labels will not be marked stale', async () => {
  const opts = {...DefaultProcessorOptions};
  opts.exemptIssueLabels = 'Cool';
  const TestIssueList: Issue[] = [
    generateIssue(
      opts,
      1,
      'My first issue',
      '2020-01-01T17:00:00Z',
      '2020-01-01T17:00:00Z',
      false,
      false,
      ['Cool']
    ),
    generateIssue(
      opts,
      2,
      'My first PR',
      '2020-01-01T17:00:00Z',
      '2020-01-01T17:00:00Z',
      false,
      true,
      ['Cool']
    ),
    generateIssue(
      opts,
      3,
      'Another issue',
      '2020-01-01T17:00:00Z',
      '2020-01-01T17:00:00Z',
      false,
      false
    )
  ];
  const processor = new IssuesProcessorMock(
    opts,
    alwaysFalseStateMock,
    async p => (p === 1 ? TestIssueList : []),
    async () => [],
    async () => new Date().toDateString()
  );

  // process our fake issue list
  await processor.processIssues(1);

  expect(processor.staleIssues).toHaveLength(2); // PR should get processed even though it has an exempt **issue** label
});

test('stale issues should not be closed if days is set to -1', async () => {
  const opts = {...DefaultProcessorOptions};
  opts.daysBeforeClose = -1;
  const TestIssueList: Issue[] = [
    generateIssue(
      opts,
      1,
      'My first issue',
      '2020-01-01T17:00:00Z',
      '2020-01-01T17:00:00Z',
      false,
      false,
      ['Stale']
    ),
    generateIssue(
      opts,
      2,
      'My first PR',
      '2020-01-01T17:00:00Z',
      '2020-01-01T17:00:00Z',
      false,
      true,
      ['Stale']
    ),
    generateIssue(
      opts,
      3,
      'Another issue',
      '2020-01-01T17:00:00Z',
      '2020-01-01T17:00:00Z',
      false,
      false,
      ['Stale']
    )
  ];
  const processor = new IssuesProcessorMock(
    opts,
    alwaysFalseStateMock,
    async p => (p === 1 ? TestIssueList : []),
    async () => [],
    async () => new Date().toDateString()
  );

  // process our fake issue list
  await processor.processIssues(1);

  expect(processor.closedIssues).toHaveLength(0);
  expect(processor.removedLabelIssues).toHaveLength(0);
});

test('stale label should be removed if a comment was added to a stale issue', async () => {
  const opts = {...DefaultProcessorOptions, removeStaleWhenUpdated: true};
  const TestIssueList: Issue[] = [
    generateIssue(
      opts,
      1,
      'An issue that should un-stale',
      '2020-01-01T17:00:00Z',
      '2020-01-01T17:00:00Z',
      false,
      false,
      ['Stale']
    )
  ];
  const processor = new IssuesProcessorMock(
    opts,
    alwaysFalseStateMock,
    async p => (p === 1 ? TestIssueList : []),
    async () => [
      {
        user: {
          login: 'notme',
          type: 'User'
        },
        body: 'Body'
      }
    ], // return a fake comment to indicate there was an update
    async () => new Date().toDateString()
  );

  // process our fake issue list
  await processor.processIssues(1);

  expect(processor.closedIssues).toHaveLength(0);
  expect(processor.staleIssues).toHaveLength(0);
  expect(processor.removedLabelIssues).toHaveLength(1);
});

test('when the option "labelsToAddWhenUnstale" is set, the labels should be added when unstale', async () => {
  expect.assertions(4);
  const opts = {
    ...DefaultProcessorOptions,
    removeStaleWhenUpdated: true,
    labelsToAddWhenUnstale: 'test'
  };
  const TestIssueList: Issue[] = [
    generateIssue(
      opts,
      1,
      'An issue that should have labels added to it when unstale',
      '2020-01-01T17:00:00Z',
      '2020-01-01T17:00:00Z',
      false,
      false,
      ['Stale']
    )
  ];
  const processor = new IssuesProcessorMock(
    opts,
    alwaysFalseStateMock,
    async p => (p === 1 ? TestIssueList : []),
    async () => [
      {
        user: {
          login: 'notme',
          type: 'User'
        },
        body: 'Body'
      }
    ], // return a fake comment to indicate there was an update
    async () => new Date().toDateString()
  );

  // process our fake issue list
  await processor.processIssues(1);

  expect(processor.closedIssues).toHaveLength(0);
  expect(processor.staleIssues).toHaveLength(0);
  // Stale should have been removed
  expect(processor.removedLabelIssues).toHaveLength(1);
  // Some label should have been added
  expect(processor.addedLabelIssues).toHaveLength(1);
});

test('when the option "labelsToRemoveWhenStale" is set, the labels should be removed when stale', async () => {
  expect.assertions(3);
  const opts = {
    ...DefaultProcessorOptions,
    removeStaleWhenUpdated: true,
    labelsToRemoveWhenStale: 'test'
  };
  const TestIssueList: Issue[] = [
    generateIssue(
      opts,
      1,
      'An issue that should have labels removed to it when stale',
      '2020-01-01T17:00:00Z',
      '2020-01-01T17:00:00Z',
      false,
      false,
      ['Stale', 'test']
    )
  ];
  const processor = new IssuesProcessorMock(
    opts,
    alwaysFalseStateMock,
    async p => (p === 1 ? TestIssueList : []),
    async () => [
      {
        user: {
          login: 'notme',
          type: 'User'
        },
        body: 'Body'
      }
    ], // return a fake comment to indicate there was an update
    async () => new Date().toDateString()
  );

  // process our fake issue list
  await processor.processIssues(1);

  expect(processor.closedIssues).toHaveLength(0);
  expect(processor.staleIssues).toHaveLength(0);
  // test label should have been removed
  expect(processor.removedLabelIssues).toHaveLength(1);
});

test('stale label should not be removed if a comment was added by the bot (and the issue should be closed)', async () => {
  const opts = {...DefaultProcessorOptions, removeStaleWhenUpdated: true};
  github.context.actor = 'abot';
  const TestIssueList: Issue[] = [
    generateIssue(
      opts,
      1,
      'An issue that should stay stale',
      '2020-01-01T17:00:00Z',
      '2020-01-01T17:00:00Z',
      false,
      false,
      ['Stale']
    )
  ];
  const processor = new IssuesProcessorMock(
    opts,
    alwaysFalseStateMock,
    async p => (p === 1 ? TestIssueList : []),
    async () => [
      {
        user: {
          login: 'abot',
          type: 'User'
        },
        body: 'This issue is stale'
      }
    ], // return a fake comment to indicate there was an update by the bot
    async () => new Date().toDateString()
  );

  // process our fake issue list
  await processor.processIssues(1);

  expect(processor.closedIssues).toHaveLength(1);
  expect(processor.staleIssues).toHaveLength(0);
  expect(processor.removedLabelIssues).toHaveLength(0);
});

test('stale label containing a space should be removed if a comment was added to a stale issue', async () => {
  const opts: IIssuesProcessorOptions = {
    ...DefaultProcessorOptions,
    removeStaleWhenUpdated: true,
    staleIssueLabel: 'stat: stale'
  };
  const TestIssueList: Issue[] = [
    generateIssue(
      opts,
      1,
      'An issue that should un-stale',
      '2020-01-01T17:00:00Z',
      '2020-01-01T17:00:00Z',
      false,
      false,
      ['stat: stale']
    )
  ];
  const processor = new IssuesProcessorMock(
    opts,
    alwaysFalseStateMock,
    async p => (p === 1 ? TestIssueList : []),
    async () => [{user: {login: 'notme', type: 'User'}, body: 'Body'}], // return a fake comment to indicate there was an update
    async () => new Date().toDateString()
  );

  // process our fake issue list
  await processor.processIssues(1);

  expect(processor.closedIssues).toHaveLength(0);
  expect(processor.staleIssues).toHaveLength(0);
  expect(processor.removedLabelIssues).toHaveLength(1);
});

test('stale issues should not be closed until after the closed number of days', async () => {
  const opts = {...DefaultProcessorOptions};
  opts.daysBeforeStale = 5; // stale after 5 days
  opts.daysBeforeClose = 1; // closes after 6 days
  const lastUpdate = new Date();
  lastUpdate.setDate(lastUpdate.getDate() - 5);
  const TestIssueList: Issue[] = [
    generateIssue(
      opts,
      1,
      'An issue that should be marked stale but not closed',
      lastUpdate.toString(),
      lastUpdate.toString(),
      false
    )
  ];
  const processor = new IssuesProcessorMock(
    opts,
    alwaysFalseStateMock,
    async p => (p === 1 ? TestIssueList : []),
    async () => [],
    async () => new Date().toDateString()
  );

  // process our fake issue list
  await processor.processIssues(1);

  expect(processor.closedIssues).toHaveLength(0);
  expect(processor.removedLabelIssues).toHaveLength(0);
  expect(processor.staleIssues).toHaveLength(1);
});

test('stale issues should be closed if the closed nubmer of days (additive) is also passed', async () => {
  const opts = {...DefaultProcessorOptions};
  opts.daysBeforeStale = 5; // stale after 5 days
  opts.daysBeforeClose = 1; // closes after 6 days
  const lastUpdate = new Date();
  lastUpdate.setDate(lastUpdate.getDate() - 7);
  const TestIssueList: Issue[] = [
    generateIssue(
      opts,
      1,
      'An issue that should be stale and closed',
      lastUpdate.toString(),
      lastUpdate.toString(),
      false,
      false,
      ['Stale']
    )
  ];
  const processor = new IssuesProcessorMock(
    opts,
    alwaysFalseStateMock,
    async p => (p === 1 ? TestIssueList : []),
    async () => [],
    async () => new Date().toDateString()
  );

  // process our fake issue list
  await processor.processIssues(1);

  expect(processor.closedIssues).toHaveLength(1);
  expect(processor.removedLabelIssues).toHaveLength(0);
  expect(processor.staleIssues).toHaveLength(0);
});

test('stale issues should not be closed until after the closed number of days (long)', async () => {
  const opts = {...DefaultProcessorOptions};
  opts.daysBeforeStale = 5; // stale after 5 days
  opts.daysBeforeClose = 20; // closes after 25 days
  const lastUpdate = new Date();
  lastUpdate.setDate(lastUpdate.getDate() - 10);
  const TestIssueList: Issue[] = [
    generateIssue(
      opts,
      1,
      'An issue that should be marked stale but not closed',
      lastUpdate.toString(),
      lastUpdate.toString(),
      false
    )
  ];
  const processor = new IssuesProcessorMock(
    opts,
    alwaysFalseStateMock,
    async p => (p === 1 ? TestIssueList : []),
    async () => [],
    async () => new Date().toDateString()
  );

  // process our fake issue list
  await processor.processIssues(1);

  expect(processor.closedIssues).toHaveLength(0);
  expect(processor.removedLabelIssues).toHaveLength(0);
  expect(processor.staleIssues).toHaveLength(1);
});

test('skips stale message on issues when stale-issue-message is empty', async () => {
  const opts = {...DefaultProcessorOptions};
  opts.daysBeforeStale = 5; // stale after 5 days
  opts.daysBeforeClose = 20; // closes after 25 days
  opts.staleIssueMessage = '';
  const lastUpdate = new Date();
  lastUpdate.setDate(lastUpdate.getDate() - 10);
  const TestIssueList: Issue[] = [
    generateIssue(
      opts,
      1,
      'An issue that should be marked stale but not closed',
      lastUpdate.toString(),
      lastUpdate.toString(),
      false
    )
  ];
  const processor = new IssuesProcessorMock(
    opts,
    alwaysFalseStateMock,
    async p => (p === 1 ? TestIssueList : []),
    async () => [],
    async () => new Date().toDateString()
  );

  // for sake of testing, mocking private function
  const markSpy = jest.spyOn(processor as any, '_markStale');

  await processor.processIssues(1);

  // issue should be staled
  expect(processor.closedIssues).toHaveLength(0);
  expect(processor.removedLabelIssues).toHaveLength(0);
  expect(processor.staleIssues).toHaveLength(1);

  // comment should not be created
  expect(markSpy).toHaveBeenCalledWith(
    TestIssueList[0],
    opts.staleIssueMessage,
    opts.staleIssueLabel,
    // this option is skipMessage
    true
  );
});

test('send stale message on issues when stale-issue-message is not empty', async () => {
  const opts = {...DefaultProcessorOptions};
  opts.daysBeforeStale = 5; // stale after 5 days
  opts.daysBeforeClose = 20; // closes after 25 days
  opts.staleIssueMessage = 'dummy issue message';
  const lastUpdate = new Date();
  lastUpdate.setDate(lastUpdate.getDate() - 10);
  const TestIssueList: Issue[] = [
    generateIssue(
      opts,
      1,
      'An issue that should be marked stale but not closed',
      lastUpdate.toString(),
      lastUpdate.toString(),
      false
    )
  ];
  const processor = new IssuesProcessorMock(
    opts,
    alwaysFalseStateMock,
    async p => (p === 1 ? TestIssueList : []),
    async () => [],
    async () => new Date().toDateString()
  );

  // for sake of testing, mocking private function
  const markSpy = jest.spyOn(processor as any, '_markStale');

  await processor.processIssues(1);

  // issue should be staled
  expect(processor.closedIssues).toHaveLength(0);
  expect(processor.removedLabelIssues).toHaveLength(0);
  expect(processor.staleIssues).toHaveLength(1);

  // comment should not be created
  expect(markSpy).toHaveBeenCalledWith(
    TestIssueList[0],
    opts.staleIssueMessage,
    opts.staleIssueLabel,
    // this option is skipMessage
    false
  );
});

test('skips stale message on prs when stale-pr-message is empty', async () => {
  const opts = {...DefaultProcessorOptions};
  opts.daysBeforeStale = 5; // stale after 5 days
  opts.daysBeforeClose = 20; // closes after 25 days
  opts.stalePrMessage = '';
  const lastUpdate = new Date();
  lastUpdate.setDate(lastUpdate.getDate() - 10);
  const TestIssueList: Issue[] = [
    generateIssue(
      opts,
      1,
      'An issue that should be marked stale but not closed',
      lastUpdate.toString(),
      lastUpdate.toString(),
      false,
      true
    )
  ];
  const processor = new IssuesProcessorMock(
    opts,
    alwaysFalseStateMock,
    async p => (p === 1 ? TestIssueList : []),
    async () => [],
    async () => new Date().toDateString()
  );

  // for sake of testing, mocking private function
  const markSpy = jest.spyOn(processor as any, '_markStale');

  await processor.processIssues(1);

  // issue should be staled
  expect(processor.closedIssues).toHaveLength(0);
  expect(processor.removedLabelIssues).toHaveLength(0);
  expect(processor.staleIssues).toHaveLength(1);

  // comment should not be created
  expect(markSpy).toHaveBeenCalledWith(
    TestIssueList[0],
    opts.stalePrMessage,
    opts.stalePrLabel,
    // this option is skipMessage
    true
  );
});

test('send stale message on prs when stale-pr-message is not empty', async () => {
  const opts = {...DefaultProcessorOptions};
  opts.daysBeforeStale = 5; // stale after 5 days
  opts.daysBeforeClose = 20; // closes after 25 days
  opts.stalePrMessage = 'dummy pr message';
  const lastUpdate = new Date();
  lastUpdate.setDate(lastUpdate.getDate() - 10);
  const TestIssueList: Issue[] = [
    generateIssue(
      opts,
      1,
      'An issue that should be marked stale but not closed',
      lastUpdate.toString(),
      lastUpdate.toString(),
      false,
      true
    )
  ];
  const processor = new IssuesProcessorMock(
    opts,
    alwaysFalseStateMock,
    async p => (p === 1 ? TestIssueList : []),
    async () => [],
    async () => new Date().toDateString()
  );

  // for sake of testing, mocking private function
  const markSpy = jest.spyOn(processor as any, '_markStale');

  await processor.processIssues(1);

  // issue should be staled
  expect(processor.closedIssues).toHaveLength(0);
  expect(processor.removedLabelIssues).toHaveLength(0);
  expect(processor.staleIssues).toHaveLength(1);

  // comment should not be created
  expect(markSpy).toHaveBeenCalledWith(
    TestIssueList[0],
    opts.stalePrMessage,
    opts.stalePrLabel,
    // this option is skipMessage
    false
  );
});

test('git branch is deleted when option is enabled', async () => {
  const opts = {...DefaultProcessorOptions, deleteBranch: true};
  const isPullRequest = true;
  const TestIssueList: Issue[] = [
    generateIssue(
      opts,
      1,
      'An issue that should have its branch deleted',
      '2020-01-01T17:00:00Z',
      '2020-01-01T17:00:00Z',
      false,
      isPullRequest,
      ['Stale']
    )
  ];
  const processor = new IssuesProcessorMock(
    opts,
    alwaysFalseStateMock,
    async p => (p === 1 ? TestIssueList : []),
    async () => [],
    async () => new Date().toDateString()
  );

  await processor.processIssues(1);

  expect(processor.closedIssues).toHaveLength(1);
  expect(processor.removedLabelIssues).toHaveLength(0);
  expect(processor.staleIssues).toHaveLength(0);
  expect(processor.deletedBranchIssues).toHaveLength(1);
});

test('git branch is not deleted when issue is not pull request', async () => {
  const opts = {...DefaultProcessorOptions, deleteBranch: true};
  const isPullRequest = false;
  const TestIssueList: Issue[] = [
    generateIssue(
      opts,
      1,
      'An issue that should not have its branch deleted',
      '2020-01-01T17:00:00Z',
      '2020-01-01T17:00:00Z',
      false,
      isPullRequest,
      ['Stale']
    )
  ];
  const processor = new IssuesProcessorMock(
    opts,
    alwaysFalseStateMock,
    async p => (p === 1 ? TestIssueList : []),
    async () => [],
    async () => new Date().toDateString()
  );

  await processor.processIssues(1);

  expect(processor.closedIssues).toHaveLength(1);
  expect(processor.removedLabelIssues).toHaveLength(0);
  expect(processor.staleIssues).toHaveLength(0);
  expect(processor.deletedBranchIssues).toHaveLength(0);
});

test('an issue without a milestone will be marked as stale', async () => {
  expect.assertions(3);
  const TestIssueList: Issue[] = [
    generateIssue(
      DefaultProcessorOptions,
      1,
      'My first issue',
      '2020-01-01T17:00:00Z',
      '2020-01-01T17:00:00Z',
      false,
      false,
      undefined,
      undefined,
      undefined,
      ''
    )
  ];
  const processor = new IssuesProcessorMock(
    DefaultProcessorOptions,
    alwaysFalseStateMock,
    async p => (p === 1 ? TestIssueList : []),
    async () => [],
    async () => new Date().toDateString()
  );

  // process our fake issue list
  await processor.processIssues(1);

  expect(processor.staleIssues.length).toStrictEqual(1);
  expect(processor.closedIssues.length).toStrictEqual(0);
  expect(processor.removedLabelIssues.length).toStrictEqual(0);
});

test('an issue without an exempted milestone will be marked as stale', async () => {
  expect.assertions(3);
  const opts = {...DefaultProcessorOptions};
  opts.exemptMilestones = 'Milestone1';
  const TestIssueList: Issue[] = [
    generateIssue(
      opts,
      1,
      'My first issue',
      '2020-01-01T17:00:00Z',
      '2020-01-01T17:00:00Z',
      false,
      false,
      undefined,
      undefined,
      undefined,
      'Milestone'
    )
  ];
  const processor = new IssuesProcessorMock(
    opts,
    alwaysFalseStateMock,
    async p => (p === 1 ? TestIssueList : []),
    async () => [],
    async () => new Date().toDateString()
  );

  // process our fake issue list
  await processor.processIssues(1);

  expect(processor.staleIssues.length).toStrictEqual(1);
  expect(processor.closedIssues.length).toStrictEqual(0);
  expect(processor.removedLabelIssues.length).toStrictEqual(0);
});

test('an issue with an exempted milestone will not be marked as stale', async () => {
  expect.assertions(3);
  const opts = {...DefaultProcessorOptions};
  opts.exemptMilestones = 'Milestone1';
  const TestIssueList: Issue[] = [
    generateIssue(
      opts,
      1,
      'My first issue',
      '2020-01-01T17:00:00Z',
      '2020-01-01T17:00:00Z',
      false,
      false,
      undefined,
      undefined,
      undefined,
      'Milestone1'
    )
  ];
  const processor = new IssuesProcessorMock(
    opts,
    alwaysFalseStateMock,
    async p => (p === 1 ? TestIssueList : []),
    async () => [],
    async () => new Date().toDateString()
  );

  // process our fake issue list
  await processor.processIssues(1);

  expect(processor.staleIssues.length).toStrictEqual(0);
  expect(processor.closedIssues.length).toStrictEqual(0);
  expect(processor.removedLabelIssues.length).toStrictEqual(0);
});

test('an issue with an exempted milestone will not be marked as stale (multi milestones with spaces)', async () => {
  expect.assertions(3);
  const opts = {...DefaultProcessorOptions};
  opts.exemptMilestones = 'Milestone1, Milestone2';
  const TestIssueList: Issue[] = [
    generateIssue(
      opts,
      1,
      'My first issue',
      '2020-01-01T17:00:00Z',
      '2020-01-01T17:00:00Z',
      false,
      false,
      undefined,
      undefined,
      undefined,
      'Milestone2'
    )
  ];
  const processor = new IssuesProcessorMock(
    opts,
    alwaysFalseStateMock,
    async p => (p === 1 ? TestIssueList : []),
    async () => [],
    async () => new Date().toDateString()
  );

  // process our fake issue list
  await processor.processIssues(1);

  expect(processor.staleIssues.length).toStrictEqual(0);
  expect(processor.closedIssues.length).toStrictEqual(0);
  expect(processor.removedLabelIssues.length).toStrictEqual(0);
});

test('an issue with an exempted milestone will not be marked as stale (multi milestones without spaces)', async () => {
  expect.assertions(3);
  const opts = {...DefaultProcessorOptions};
  opts.exemptMilestones = 'Milestone1,Milestone2';
  const TestIssueList: Issue[] = [
    generateIssue(
      opts,
      1,
      'My first issue',
      '2020-01-01T17:00:00Z',
      '2020-01-01T17:00:00Z',
      false,
      false,
      undefined,
      undefined,
      undefined,
      'Milestone2'
    )
  ];
  const processor = new IssuesProcessorMock(
    opts,
    alwaysFalseStateMock,
    async p => (p === 1 ? TestIssueList : []),
    async () => [],
    async () => new Date().toDateString()
  );

  // process our fake issue list
  await processor.processIssues(1);

  expect(processor.staleIssues.length).toStrictEqual(0);
  expect(processor.closedIssues.length).toStrictEqual(0);
  expect(processor.removedLabelIssues.length).toStrictEqual(0);
});

test('an issue with an exempted milestone but without an exempted issue milestone will not be marked as stale', async () => {
  expect.assertions(3);
  const opts = {...DefaultProcessorOptions};
  opts.exemptMilestones = 'Milestone1';
  opts.exemptIssueMilestones = '';
  const TestIssueList: Issue[] = [
    generateIssue(
      opts,
      1,
      'My first issue',
      '2020-01-01T17:00:00Z',
      '2020-01-01T17:00:00Z',
      false,
      false,
      undefined,
      undefined,
      undefined,
      'Milestone1'
    )
  ];
  const processor = new IssuesProcessorMock(
    opts,
    alwaysFalseStateMock,
    async p => (p === 1 ? TestIssueList : []),
    async () => [],
    async () => new Date().toDateString()
  );

  // process our fake issue list
  await processor.processIssues(1);

  expect(processor.staleIssues.length).toStrictEqual(0);
  expect(processor.closedIssues.length).toStrictEqual(0);
  expect(processor.removedLabelIssues.length).toStrictEqual(0);
});

test('an issue with an exempted milestone but with another exempted issue milestone will be marked as stale', async () => {
  expect.assertions(3);
  const opts = {...DefaultProcessorOptions};
  opts.exemptMilestones = 'Milestone1';
  opts.exemptIssueMilestones = 'Milestone2';
  const TestIssueList: Issue[] = [
    generateIssue(
      opts,
      1,
      'My first issue',
      '2020-01-01T17:00:00Z',
      '2020-01-01T17:00:00Z',
      false,
      false,
      undefined,
      undefined,
      undefined,
      'Milestone1'
    )
  ];
  const processor = new IssuesProcessorMock(
    opts,
    alwaysFalseStateMock,
    async p => (p === 1 ? TestIssueList : []),
    async () => [],
    async () => new Date().toDateString()
  );

  // process our fake issue list
  await processor.processIssues(1);

  expect(processor.staleIssues.length).toStrictEqual(1);
  expect(processor.closedIssues.length).toStrictEqual(0);
  expect(processor.removedLabelIssues.length).toStrictEqual(0);
});

test('an issue with an exempted milestone and with an exempted issue milestone will not be marked as stale', async () => {
  expect.assertions(3);
  const opts = {...DefaultProcessorOptions};
  opts.exemptMilestones = 'Milestone1';
  opts.exemptIssueMilestones = 'Milestone1';
  const TestIssueList: Issue[] = [
    generateIssue(
      opts,
      1,
      'My first issue',
      '2020-01-01T17:00:00Z',
      '2020-01-01T17:00:00Z',
      false,
      false,
      undefined,
      undefined,
      undefined,
      'Milestone1'
    )
  ];
  const processor = new IssuesProcessorMock(
    opts,
    alwaysFalseStateMock,
    async p => (p === 1 ? TestIssueList : []),
    async () => [],
    async () => new Date().toDateString()
  );

  // process our fake issue list
  await processor.processIssues(1);

  expect(processor.staleIssues.length).toStrictEqual(0);
  expect(processor.closedIssues.length).toStrictEqual(0);
  expect(processor.removedLabelIssues.length).toStrictEqual(0);
});

test('processing an issue opened since 2 days and with the option "daysBeforeIssueStale" at 3 will not make it stale', async () => {
  expect.assertions(2);
  const opts: IIssuesProcessorOptions = {
    ...DefaultProcessorOptions,
    daysBeforeStale: 10,
    daysBeforeIssueStale: 3
  };
  const issueDate = new Date();
  issueDate.setDate(issueDate.getDate() - 2);
  const TestIssueList: Issue[] = [
    generateIssue(opts, 1, 'An issue with no label', issueDate.toDateString())
  ];
  const processor = new IssuesProcessorMock(
    opts,
    alwaysFalseStateMock,
    async p => (p === 1 ? TestIssueList : []),
    async () => [],
    async () => new Date().toDateString()
  );

  // process our fake issue list
  await processor.processIssues(1);

  expect(processor.staleIssues).toHaveLength(0);
  expect(processor.closedIssues).toHaveLength(0);
});

test('processing an issue opened since 2 days and with the option "daysBeforeIssueStale" at 2 will make it stale', async () => {
  expect.assertions(2);
  const opts: IIssuesProcessorOptions = {
    ...DefaultProcessorOptions,
    daysBeforeStale: 10,
    daysBeforeIssueStale: 2
  };
  const issueDate = new Date();
  issueDate.setDate(issueDate.getDate() - 2);
  const TestIssueList: Issue[] = [
    generateIssue(opts, 1, 'An issue with no label', issueDate.toDateString())
  ];
  const processor = new IssuesProcessorMock(
    opts,
    alwaysFalseStateMock,
    async p => (p === 1 ? TestIssueList : []),
    async () => [],
    async () => new Date().toDateString()
  );

  // process our fake issue list
  await processor.processIssues(1);

  expect(processor.staleIssues).toHaveLength(1);
  expect(processor.closedIssues).toHaveLength(0);
});

test('processing an issue opened since 2 days and with the option "daysBeforeIssueStale" at 1 will make it stale', async () => {
  expect.assertions(2);
  const opts: IIssuesProcessorOptions = {
    ...DefaultProcessorOptions,
    daysBeforeStale: 10,
    daysBeforeIssueStale: 1
  };
  const issueDate = new Date();
  issueDate.setDate(issueDate.getDate() - 2);
  const TestIssueList: Issue[] = [
    generateIssue(opts, 1, 'An issue with no label', issueDate.toDateString())
  ];
  const processor = new IssuesProcessorMock(
    opts,
    alwaysFalseStateMock,
    async p => (p === 1 ? TestIssueList : []),
    async () => [],
    async () => new Date().toDateString()
  );

  // process our fake issue list
  await processor.processIssues(1);

  expect(processor.staleIssues).toHaveLength(1);
  expect(processor.closedIssues).toHaveLength(0);
});

test('processing an issue opened since 1 hour and with the option "daysBeforeIssueStale" at 0.1666666667 (4 hours) will not make it stale', async () => {
  expect.assertions(2);
  const opts: IIssuesProcessorOptions = {
    ...DefaultProcessorOptions,
    daysBeforeStale: 10,
    daysBeforeIssueStale: 0.1666666667
  };
  const issueDate = new Date();
  issueDate.setHours(issueDate.getHours() - 1);
  const TestIssueList: Issue[] = [
    generateIssue(opts, 1, 'An issue with no label', issueDate.toISOString())
  ];
  const processor = new IssuesProcessorMock(
    opts,
    alwaysFalseStateMock,
    async p => (p === 1 ? TestIssueList : []),
    async () => [],
    async () => new Date().toISOString()
  );

  // process our fake issue list
  await processor.processIssues(1);

  expect(processor.staleIssues).toHaveLength(0);
  expect(processor.closedIssues).toHaveLength(0);
});

test('processing an issue opened since 4 hours and with the option "daysBeforeIssueStale" at 0.1666666667 (4 hours) will make it stale', async () => {
  expect.assertions(2);
  const opts: IIssuesProcessorOptions = {
    ...DefaultProcessorOptions,
    daysBeforeStale: 10,
    daysBeforeIssueStale: 0.1666666667
  };
  const issueDate = new Date();
  issueDate.setHours(issueDate.getHours() - 4);
  issueDate.setMinutes(issueDate.getMinutes() - 1); // Make it slightly older than 4 hours
  const TestIssueList: Issue[] = [
    generateIssue(opts, 1, 'An issue with no label', issueDate.toISOString())
  ];
  const processor = new IssuesProcessorMock(
    opts,
    alwaysFalseStateMock,
    async p => (p === 1 ? TestIssueList : []),
    async () => [],
    async () => new Date().toISOString()
  );

  // process our fake issue list
  await processor.processIssues(1);

  expect(processor.staleIssues).toHaveLength(1);
  expect(processor.closedIssues).toHaveLength(0);
});

test('processing an issue opened since 5 hours and with the option "daysBeforeIssueStale" at 0.1666666667 (4 hours) will make it stale', async () => {
  expect.assertions(2);
  const opts: IIssuesProcessorOptions = {
    ...DefaultProcessorOptions,
    daysBeforeStale: 10,
    daysBeforeIssueStale: 0.1666666667
  };
  const issueDate = new Date();
  issueDate.setHours(issueDate.getHours() - 5);
  const TestIssueList: Issue[] = [
    generateIssue(opts, 1, 'An issue with no label', issueDate.toISOString())
  ];
  const processor = new IssuesProcessorMock(
    opts,
    alwaysFalseStateMock,
    async p => (p === 1 ? TestIssueList : []),
    async () => [],
    async () => new Date().toISOString()
  );

  // process our fake issue list
  await processor.processIssues(1);

  expect(processor.staleIssues).toHaveLength(1);
  expect(processor.closedIssues).toHaveLength(0);
});

test('processing a pull request opened since 2 days and with the option "daysBeforePrStale" at 3 will not make it stale', async () => {
  expect.assertions(2);
  const opts: IIssuesProcessorOptions = {
    ...DefaultProcessorOptions,
    daysBeforeStale: 10,
    daysBeforePrStale: 3
  };
  const issueDate = new Date();
  issueDate.setDate(issueDate.getDate() - 2);
  const TestIssueList: Issue[] = [
    generateIssue(
      opts,
      1,
      'A pull request with no label',
      issueDate.toDateString(),
      issueDate.toDateString(),
      false,
      true
    )
  ];
  const processor = new IssuesProcessorMock(
    opts,
    alwaysFalseStateMock,
    async p => (p === 1 ? TestIssueList : []),
    async () => [],
    async () => new Date().toDateString()
  );

  // process our fake issue list
  await processor.processIssues(1);

  expect(processor.staleIssues).toHaveLength(0);
  expect(processor.closedIssues).toHaveLength(0);
});

test('processing a pull request opened since 2 days and with the option "daysBeforePrStale" at 2 will make it stale', async () => {
  expect.assertions(2);
  const opts: IIssuesProcessorOptions = {
    ...DefaultProcessorOptions,
    daysBeforeStale: 10,
    daysBeforePrStale: 2
  };
  const issueDate = new Date();
  issueDate.setDate(issueDate.getDate() - 2);
  const TestIssueList: Issue[] = [
    generateIssue(
      opts,
      1,
      'A pull request with no label',
      issueDate.toDateString(),
      issueDate.toDateString(),
      false,
      true
    )
  ];
  const processor = new IssuesProcessorMock(
    opts,
    alwaysFalseStateMock,
    async p => (p === 1 ? TestIssueList : []),
    async () => [],
    async () => new Date().toDateString()
  );

  // process our fake issue list
  await processor.processIssues(1);

  expect(processor.staleIssues).toHaveLength(1);
  expect(processor.closedIssues).toHaveLength(0);
});

test('processing a pull request opened since 2 days and with the option "daysBeforePrStale" at 1 will make it stale', async () => {
  expect.assertions(2);
  const opts: IIssuesProcessorOptions = {
    ...DefaultProcessorOptions,
    daysBeforeStale: 10,
    daysBeforePrStale: 1
  };
  const issueDate = new Date();
  issueDate.setDate(issueDate.getDate() - 2);
  const TestIssueList: Issue[] = [
    generateIssue(
      opts,
      1,
      'A pull request with no label',
      issueDate.toDateString(),
      issueDate.toDateString(),
      false,
      true
    )
  ];
  const processor = new IssuesProcessorMock(
    opts,
    alwaysFalseStateMock,
    async p => (p === 1 ? TestIssueList : []),
    async () => [],
    async () => new Date().toDateString()
  );

  // process our fake issue list
  await processor.processIssues(1);

  expect(processor.staleIssues).toHaveLength(1);
  expect(processor.closedIssues).toHaveLength(0);
});

test('processing a pull request opened since 1 hour and with the option "daysBeforePrStale" at 0.1666666667 (4 hours) will not make it stale', async () => {
  expect.assertions(2);
  const opts: IIssuesProcessorOptions = {
    ...DefaultProcessorOptions,
    daysBeforeStale: 10,
    daysBeforePrStale: 0.1666666667
  };
  const issueDate = new Date();
  issueDate.setHours(issueDate.getHours() - 1);
  const TestIssueList: Issue[] = [
    generateIssue(
      opts,
      1,
      'A pull request with no label',
      issueDate.toISOString(),
      issueDate.toISOString(),
      false,
      true
    )
  ];
  const processor = new IssuesProcessorMock(
    opts,
    alwaysFalseStateMock,
    async p => (p === 1 ? TestIssueList : []),
    async () => [],
    async () => new Date().toISOString()
  );

  // process our fake issue list
  await processor.processIssues(1);

  expect(processor.staleIssues).toHaveLength(0);
  expect(processor.closedIssues).toHaveLength(0);
});

test('processing a pull request opened since 4 hours and with the option "daysBeforePrStale" at 0.1666666667 (4 hours) will make it stale', async () => {
  expect.assertions(2);
  const opts: IIssuesProcessorOptions = {
    ...DefaultProcessorOptions,
    daysBeforeStale: 10,
    daysBeforePrStale: 0.1666666667
  };
  const issueDate = new Date();
  issueDate.setHours(issueDate.getHours() - 4);
  issueDate.setMinutes(issueDate.getMinutes() - 1); // Make it slightly older than 4 hours
  const TestIssueList: Issue[] = [
    generateIssue(
      opts,
      1,
      'A pull request with no label',
      issueDate.toISOString(),
      issueDate.toISOString(),
      false,
      true
    )
  ];
  const processor = new IssuesProcessorMock(
    opts,
    alwaysFalseStateMock,
    async p => (p === 1 ? TestIssueList : []),
    async () => [],
    async () => new Date().toISOString()
  );

  // process our fake issue list
  await processor.processIssues(1);

  expect(processor.staleIssues).toHaveLength(1);
  expect(processor.closedIssues).toHaveLength(0);
});

test('processing a pull request opened since 5 hours and with the option "daysBeforePrStale" at 0.1666666667 (4 hours) will make it stale', async () => {
  expect.assertions(2);
  const opts: IIssuesProcessorOptions = {
    ...DefaultProcessorOptions,
    daysBeforeStale: 10,
    daysBeforePrStale: 0.1666666667
  };
  const issueDate = new Date();
  issueDate.setHours(issueDate.getHours() - 5);
  const TestIssueList: Issue[] = [
    generateIssue(
      opts,
      1,
      'A pull request with no label',
      issueDate.toISOString(),
      issueDate.toISOString(),
      false,
      true
    )
  ];
  const processor = new IssuesProcessorMock(
    opts,
    alwaysFalseStateMock,
    async p => (p === 1 ? TestIssueList : []),
    async () => [],
    async () => new Date().toISOString()
  );

  // process our fake issue list
  await processor.processIssues(1);

  expect(processor.staleIssues).toHaveLength(1);
  expect(processor.closedIssues).toHaveLength(0);
});

test('processing a previously closed issue with a close label will remove the close label', async () => {
  expect.assertions(1);
  const opts: IIssuesProcessorOptions = {
    ...DefaultProcessorOptions,
    closeIssueLabel: 'close',
    staleIssueLabel: 'stale'
  };
  const now: Date = new Date();
  const oneWeekAgo: Date = new Date(now.setDate(now.getDate() - 7));
  const TestIssueList: Issue[] = [
    generateIssue(
      opts,
      1,
      'An opened issue with a close label',
      oneWeekAgo.toDateString(),
      now.toDateString(),
      false,
      false,
      ['close'],
      false,
      false
    )
  ];
  const processor = new IssuesProcessorMock(
    opts,
    alwaysFalseStateMock,
    async p => (p === 1 ? TestIssueList : []),
    async () => [],
    async () => new Date().toDateString()
  );

  // process our fake issue list
  await processor.processIssues(1);

  expect(processor.removedLabelIssues).toHaveLength(1);
});

test('processing a closed issue with a close label will not remove the close label', async () => {
  expect.assertions(1);
  const opts: IIssuesProcessorOptions = {
    ...DefaultProcessorOptions,
    closeIssueLabel: 'close',
    staleIssueLabel: 'stale'
  };
  const now: Date = new Date();
  const oneWeekAgo: Date = new Date(now.setDate(now.getDate() - 7));
  const TestIssueList: Issue[] = [
    generateIssue(
      opts,
      1,
      'A closed issue with a close label',
      oneWeekAgo.toDateString(),
      now.toDateString(),
      false,
      false,
      ['close'],
      true,
      false
    )
  ];
  const processor = new IssuesProcessorMock(
    opts,
    alwaysFalseStateMock,
    async p => (p === 1 ? TestIssueList : []),
    async () => [],
    async () => new Date().toDateString()
  );

  // process our fake issue list
  await processor.processIssues(1);

  expect(processor.removedLabelIssues).toHaveLength(0);
});

test('processing a locked issue with a close label will not remove the close label', async () => {
  expect.assertions(1);
  const opts: IIssuesProcessorOptions = {
    ...DefaultProcessorOptions,
    closeIssueLabel: 'close',
    staleIssueLabel: 'stale'
  };
  const now: Date = new Date();
  const oneWeekAgo: Date = new Date(now.setDate(now.getDate() - 7));
  const TestIssueList: Issue[] = [
    generateIssue(
      opts,
      1,
      'A closed issue with a close label',
      oneWeekAgo.toDateString(),
      now.toDateString(),
      false,
      false,
      ['close'],
      false,
      true
    )
  ];
  const processor = new IssuesProcessorMock(
    opts,
    alwaysFalseStateMock,
    async p => (p === 1 ? TestIssueList : []),
    async () => [],
    async () => new Date().toDateString()
  );

  // process our fake issue list
  await processor.processIssues(1);

  expect(processor.removedLabelIssues).toHaveLength(0);
});

test('processing an issue stale since less than the daysBeforeStale with a stale label created after daysBeforeClose should close the issue', async () => {
  expect.assertions(3);
  const opts: IIssuesProcessorOptions = {
    ...DefaultProcessorOptions,
    staleIssueLabel: 'stale-label',
    daysBeforeStale: 30,
    daysBeforeClose: 7,
    closeIssueMessage: 'close message',
    removeStaleWhenUpdated: false
  };
  const now: Date = new Date();
  const updatedAt: Date = new Date(now.setDate(now.getDate() - 9));
  const labelCreatedAt: Date = new Date(now.setDate(now.getDate() - 17));
  const TestIssueList: Issue[] = [
    generateIssue(
      opts,
      1,
      'A real issue example; see https://github.com/actions/stale/issues/351',
      updatedAt.toDateString(),
      new Date(2021, 0, 16).toDateString(),
      false,
      false,
      ['stale-label'], // This was the problem for the user BTW, the issue was re-opened without removing the previous stale label
      false,
      false
    )
  ];
  const processor = new IssuesProcessorMock(
    opts,
    alwaysFalseStateMock,
    async p => (p === 1 ? TestIssueList : []),
    async (): Promise<IComment[]> => Promise.resolve([]),
    async () => labelCreatedAt.toDateString()
  );

  // process our fake issue list
  await processor.processIssues(1);

  expect(processor.removedLabelIssues).toHaveLength(0);
  expect(processor.deletedBranchIssues).toHaveLength(0);
  expect(processor.closedIssues).toHaveLength(1); // Expected at 0 by the user
});

test('processing an issue stale since less than the daysBeforeStale without a stale label should close the issue', async () => {
  expect.assertions(3);
  const opts: IIssuesProcessorOptions = {
    ...DefaultProcessorOptions,
    staleIssueLabel: 'stale-label',
    daysBeforeStale: 30,
    daysBeforeClose: 7,
    closeIssueMessage: 'close message',
    removeStaleWhenUpdated: false
  };
  const now: Date = new Date();
  const updatedAt: Date = new Date(now.setDate(now.getDate() - 9));
  const TestIssueList: Issue[] = [
    generateIssue(
      opts,
      1,
      'A real issue example; see https://github.com/actions/stale/issues/351 but without the old stale label from the previous close',
      updatedAt.toDateString(),
      new Date(2021, 0, 16).toDateString(),
      false,
      false,
      [],
      false,
      false
    )
  ];
  const processor = new IssuesProcessorMock(
    opts,
    alwaysFalseStateMock,
    async p => (p === 1 ? TestIssueList : []),
    async (): Promise<IComment[]> => Promise.resolve([]),
    async () => new Date().toDateString()
  );

  // process our fake issue list
  await processor.processIssues(1);

  expect(processor.removedLabelIssues).toHaveLength(0);
  expect(processor.deletedBranchIssues).toHaveLength(0);
  expect(processor.closedIssues).toHaveLength(0);
});

test('processing a pull request to be stale with the "stalePrMessage" option set will send a PR comment', async () => {
  expect.assertions(3);
  const opts: IIssuesProcessorOptions = {
    ...DefaultProcessorOptions,
    stalePrMessage: 'This PR is stale',
    daysBeforeStale: 10,
    daysBeforePrStale: 1
  };
  const issueDate = new Date();
  issueDate.setDate(issueDate.getDate() - 2);
  const TestIssueList: Issue[] = [
    generateIssue(
      opts,
      1,
      'A pull request with no label and a stale message',
      issueDate.toDateString(),
      issueDate.toDateString(),
      false,
      true
    )
  ];
  const processor = new IssuesProcessorMock(
    opts,
    alwaysFalseStateMock,
    async p => (p === 1 ? TestIssueList : []),
    async () => [],
    async () => new Date().toDateString()
  );

  // process our fake issue list
  await processor.processIssues(1);

  expect(processor.staleIssues).toHaveLength(1);
  expect(processor.closedIssues).toHaveLength(0);
  expect(processor.statistics?.addedPullRequestsCommentsCount).toStrictEqual(1);
});

test('processing a pull request to be stale with the "stalePrMessage" option set to empty will not send a PR comment', async () => {
  expect.assertions(3);
  const opts: IIssuesProcessorOptions = {
    ...DefaultProcessorOptions,
    stalePrMessage: '',
    daysBeforeStale: 10,
    daysBeforePrStale: 1
  };
  const issueDate = new Date();
  issueDate.setDate(issueDate.getDate() - 2);
  const TestIssueList: Issue[] = [
    generateIssue(
      opts,
      1,
      'A pull request with no label and a stale message',
      issueDate.toDateString(),
      issueDate.toDateString(),
      false,
      true
    )
  ];
  const processor = new IssuesProcessorMock(
    opts,
    alwaysFalseStateMock,
    async p => (p === 1 ? TestIssueList : []),
    async () => [],
    async () => new Date().toDateString()
  );

  // process our fake issue list
  await processor.processIssues(1);

  expect(processor.staleIssues).toHaveLength(1);
  expect(processor.closedIssues).toHaveLength(0);
  expect(processor.statistics?.addedPullRequestsCommentsCount).toStrictEqual(0);
});

test('processing an issue with the "includeOnlyAssigned" option and nonempty assignee list will stale the issue', async () => {
  const issueDate = new Date();
  issueDate.setDate(issueDate.getDate() - 2);

  const opts: IIssuesProcessorOptions = {
    ...DefaultProcessorOptions,
    staleIssueLabel: 'This issue is stale',
    includeOnlyAssigned: true
  };

  const TestIssueList: Issue[] = [
    generateIssue(
      opts,
      1,
      'An issue with no label',
      issueDate.toDateString(),
      issueDate.toDateString(),
      false,
      false,
      [],
      false,
      false,
      undefined,
      ['assignee1']
    )
  ];
  const processor = new IssuesProcessorMock(
    opts,
    alwaysFalseStateMock,
    async p => (p === 1 ? TestIssueList : []),
    async () => [],
    async () => new Date().toDateString()
  );

  // process our fake issue list
  await processor.processIssues(1);

  expect(processor.staleIssues).toHaveLength(1);
  expect(processor.closedIssues).toHaveLength(0);
});

test('processing an issue with the "includeOnlyAssigned" option set and no assignees will not stale the issue', async () => {
  const issueDate = new Date();
  issueDate.setDate(issueDate.getDate() - 2);

  const opts: IIssuesProcessorOptions = {
    ...DefaultProcessorOptions,
    staleIssueLabel: 'This issue is stale',
    includeOnlyAssigned: true
  };

  const TestIssueList: Issue[] = [
    generateIssue(opts, 1, 'An issue with no label', issueDate.toDateString())
  ];
  const processor = new IssuesProcessorMock(
    opts,
    alwaysFalseStateMock,
    async p => (p === 1 ? TestIssueList : []),
    async () => [],
    async () => new Date().toDateString()
  );

  // process our fake issue list
  await processor.processIssues(1);

  expect(processor.staleIssues).toHaveLength(0);
  expect(processor.closedIssues).toHaveLength(0);
});
```

## File: `__tests__/milestones.spec.ts`
```typescript
import {Issue} from '../src/classes/issue';
import {IIssuesProcessorOptions} from '../src/interfaces/issues-processor-options';
import {IssuesProcessorMock} from './classes/issues-processor-mock';
import {DefaultProcessorOptions} from './constants/default-processor-options';
import {generateIssue} from './functions/generate-issue';
import {alwaysFalseStateMock} from './classes/state-mock';

interface ITestData {
  isPullRequest: boolean;
  milestone: string;
  name: string;
  shouldStale: boolean;
}

describe('milestones options', (): void => {
  let opts: IIssuesProcessorOptions;
  let testIssueList: Issue[];
  let processor: IssuesProcessorMock;

  const setTestIssueList = (
    isPullRequest: boolean,
    milestone: string | undefined
  ) => {
    testIssueList = [
      generateIssue(
        opts,
        1,
        'My first issue',
        '2020-01-01T17:00:00Z',
        '2020-01-01T17:00:00Z',
        false,
        isPullRequest,
        undefined,
        undefined,
        undefined,
        milestone
      )
    ];
  };

  const setProcessor = () => {
    processor = new IssuesProcessorMock(
      opts,
      alwaysFalseStateMock,
      async p => (p === 1 ? testIssueList : []),
      async () => [],
      async () => new Date().toDateString()
    );
  };

  beforeEach((): void => {
    opts = {...DefaultProcessorOptions};
  });

  describe('when all the issues and pull requests milestones should not exempt', (): void => {
    beforeEach((): void => {
      opts.exemptAllMilestones = false;
    });

    describe.each`
      isPullRequest | milestone            | name                                     | shouldStale
      ${false}      | ${''}                | ${'the issue does not have a milestone'} | ${true}
      ${false}      | ${'dummy-milestone'} | ${'the issue does have a milestone'}     | ${true}
      ${true}       | ${''}                | ${'the PR does not have a milestone'}    | ${true}
      ${true}       | ${'dummy-milestone'} | ${'the PR does have a milestone'}        | ${true}
    `(
      'when $name',
      ({isPullRequest, milestone, shouldStale}: ITestData): void => {
        beforeEach((): void => {
          setTestIssueList(isPullRequest, milestone);
          setProcessor();
        });

        test(`should${
          shouldStale ? '' : ' not'
        } be marked as stale`, async () => {
          expect.assertions(3);

          await processor.processIssues(1);

          expect(processor.staleIssues.length).toStrictEqual(
            shouldStale ? 1 : 0
          );
          expect(processor.closedIssues.length).toStrictEqual(0);
          expect(processor.removedLabelIssues.length).toStrictEqual(0);
        });
      }
    );

    describe('when all the issues milestones are not configured to exempt', (): void => {
      beforeEach((): void => {
        opts.exemptAllIssueMilestones = undefined;
      });

      describe.each`
        isPullRequest | milestone            | name                                     | shouldStale
        ${false}      | ${''}                | ${'the issue does not have a milestone'} | ${true}
        ${false}      | ${'dummy-milestone'} | ${'the issue does have a milestone'}     | ${true}
        ${true}       | ${''}                | ${'the PR does not have a milestone'}    | ${true}
        ${true}       | ${'dummy-milestone'} | ${'the PR does have a milestone'}        | ${true}
      `(
        'when $name',
        ({isPullRequest, milestone, shouldStale}: ITestData): void => {
          beforeEach((): void => {
            setTestIssueList(isPullRequest, milestone);
            setProcessor();
          });

          test(`should${
            shouldStale ? '' : ' not'
          } be marked as stale`, async () => {
            expect.assertions(3);

            await processor.processIssues(1);

            expect(processor.staleIssues.length).toStrictEqual(
              shouldStale ? 1 : 0
            );
            expect(processor.closedIssues.length).toStrictEqual(0);
            expect(processor.removedLabelIssues.length).toStrictEqual(0);
          });
        }
      );

      describe('when all the issues and pull requests milestones should exempt a specific milestone', (): void => {
        beforeEach((): void => {
          opts.exemptMilestones = 'dummy-milestone';
        });

        describe.each`
          isPullRequest | milestone                         | name                                                                            | shouldStale
          ${false}      | ${''}                             | ${'the issue does not have a milestone'}                                        | ${true}
          ${false}      | ${'dummy-milestone-not-exempted'} | ${'the issue does have a milestone but not matching the specific exempted one'} | ${true}
          ${false}      | ${'dummy-milestone'}              | ${'the issue does have a milestone matching the specific exempted one'}         | ${false}
          ${true}       | ${''}                             | ${'the PR does not have a milestone'}                                           | ${true}
          ${true}       | ${'dummy-milestone-not-exempted'} | ${'the PR does have a milestone but not matching the specific exempted one'}    | ${true}
          ${true}       | ${'dummy-milestone'}              | ${'the PR does have a milestone matching the specific exempted one'}            | ${false}
        `(
          'when $name',
          ({isPullRequest, milestone, shouldStale}: ITestData): void => {
            beforeEach((): void => {
              setTestIssueList(isPullRequest, milestone);
              setProcessor();
            });

            test(`should${
              shouldStale ? '' : ' not'
            } be marked as stale`, async () => {
              expect.assertions(3);

              await processor.processIssues(1);

              expect(processor.staleIssues.length).toStrictEqual(
                shouldStale ? 1 : 0
              );
              expect(processor.closedIssues.length).toStrictEqual(0);
              expect(processor.removedLabelIssues.length).toStrictEqual(0);
            });
          }
        );

        describe('when all the issues milestones should exempt a specific milestone', (): void => {
          beforeEach((): void => {
            opts.exemptIssueMilestones = 'dummy-issue-milestone';
          });

          describe.each`
            isPullRequest | milestone                         | name                                                                                  | shouldStale
            ${false}      | ${''}                             | ${'the issue does not have a milestone'}                                              | ${true}
            ${false}      | ${'dummy-milestone-not-exempted'} | ${'the issue does have a milestone but not matching the specific issue exempted one'} | ${true}
            ${false}      | ${'dummy-issue-milestone'}        | ${'the issue does have a milestone matching the specific issue exempted one'}         | ${false}
            ${false}      | ${'dummy-milestone'}              | ${'the issue does have a milestone matching the specific exempted one'}               | ${true}
            ${true}       | ${''}                             | ${'the PR does not have a milestone'}                                                 | ${true}
            ${true}       | ${'dummy-milestone-not-exempted'} | ${'the PR does have a milestone but not matching the specific issue exempted one'}    | ${true}
            ${true}       | ${'dummy-issue-milestone'}        | ${'the PR does have a milestone matching the specific issue exempted one'}            | ${true}
            ${true}       | ${'dummy-milestone'}              | ${'the PR does have a milestone matching the specific exempted one'}                  | ${false}
          `(
            'when $name',
            ({isPullRequest, milestone, shouldStale}: ITestData): void => {
              beforeEach((): void => {
                setTestIssueList(isPullRequest, milestone);
                setProcessor();
              });

              test(`should${
                shouldStale ? '' : ' not'
              } be marked as stale`, async () => {
                expect.assertions(3);

                await processor.processIssues(1);

                expect(processor.staleIssues.length).toStrictEqual(
                  shouldStale ? 1 : 0
                );
                expect(processor.closedIssues.length).toStrictEqual(0);
                expect(processor.removedLabelIssues.length).toStrictEqual(0);
              });
            }
          );
        });

        describe('when all the pull requests milestones should exempt a specific milestone', (): void => {
          beforeEach((): void => {
            opts.exemptPrMilestones = 'dummy-pull-request-milestone';
          });

          describe.each`
            isPullRequest | milestone                         | name                                                                                         | shouldStale
            ${false}      | ${''}                             | ${'the issue does not have a milestone'}                                                     | ${true}
            ${false}      | ${'dummy-milestone-not-exempted'} | ${'the issue does have a milestone but not matching the specific pull request exempted one'} | ${true}
            ${false}      | ${'dummy-pull-request-milestone'} | ${'the issue does have a milestone matching the specific pull request exempted one'}         | ${true}
            ${false}      | ${'dummy-milestone'}              | ${'the issue does have a milestone matching the specific exempted one'}                      | ${false}
            ${true}       | ${''}                             | ${'the PR does not have a milestone'}                                                        | ${true}
            ${true}       | ${'dummy-milestone-not-exempted'} | ${'the PR does have a milestone but not matching the specific pull request exempted one'}    | ${true}
            ${true}       | ${'dummy-pull-request-milestone'} | ${'the PR does have a milestone matching the specific pull request exempted one'}            | ${false}
            ${true}       | ${'dummy-milestone'}              | ${'the PR does have a milestone matching the specific exempted one'}                         | ${true}
          `(
            'when $name',
            ({isPullRequest, milestone, shouldStale}: ITestData): void => {
              beforeEach((): void => {
                setTestIssueList(isPullRequest, milestone);
                setProcessor();
              });

              test(`should${
                shouldStale ? '' : ' not'
              } be marked as stale`, async () => {
                expect.assertions(3);

                await processor.processIssues(1);

                expect(processor.staleIssues.length).toStrictEqual(
                  shouldStale ? 1 : 0
                );
                expect(processor.closedIssues.length).toStrictEqual(0);
                expect(processor.removedLabelIssues.length).toStrictEqual(0);
              });
            }
          );
        });
      });

      describe('when all the issues and pull requests milestones should exempt some milestones', (): void => {
        beforeEach((): void => {
          opts.exemptMilestones = 'dummy-milestone1, dummy-milestone2';
        });

        describe.each`
          isPullRequest | milestone                         | name                                                                            | shouldStale
          ${false}      | ${''}                             | ${'the issue does not have a milestone'}                                        | ${true}
          ${false}      | ${'dummy-milestone-not-exempted'} | ${'the issue does have a milestone but not matching the specific exempted one'} | ${true}
          ${false}      | ${'dummy-milestone2'}             | ${'the issue does have a milestone matching the specific exempted one'}         | ${false}
          ${true}       | ${''}                             | ${'the PR does not have a milestone'}                                           | ${true}
          ${true}       | ${'dummy-milestone-not-exempted'} | ${'the PR does have a milestone but not matching the specific exempted one'}    | ${true}
          ${true}       | ${'dummy-milestone2'}             | ${'the PR does have a milestone matching the specific exempted one'}            | ${false}
        `(
          'when $name',
          ({isPullRequest, milestone, shouldStale}: ITestData): void => {
            beforeEach((): void => {
              setTestIssueList(isPullRequest, milestone);
              setProcessor();
            });

            test(`should${
              shouldStale ? '' : ' not'
            } be marked as stale`, async () => {
              expect.assertions(3);

              await processor.processIssues(1);

              expect(processor.staleIssues.length).toStrictEqual(
                shouldStale ? 1 : 0
              );
              expect(processor.closedIssues.length).toStrictEqual(0);
              expect(processor.removedLabelIssues.length).toStrictEqual(0);
            });
          }
        );

        describe('when all the issues milestones should exempt a specific milestone', (): void => {
          beforeEach((): void => {
            opts.exemptIssueMilestones =
              'dummy-issue-milestone1, dummy-issue-milestone2';
          });

          describe.each`
            isPullRequest | milestone                         | name                                                                                  | shouldStale
            ${false}      | ${''}                             | ${'the issue does not have a milestone'}                                              | ${true}
            ${false}      | ${'dummy-milestone-not-exempted'} | ${'the issue does have a milestone but not matching the specific issue exempted one'} | ${true}
            ${false}      | ${'dummy-issue-milestone2'}       | ${'the issue does have a milestone matching the specific issue exempted one'}         | ${false}
            ${false}      | ${'dummy-milestone2'}             | ${'the issue does have a milestone matching the specific exempted one'}               | ${true}
            ${true}       | ${''}                             | ${'the PR does not have a milestone'}                                                 | ${true}
            ${true}       | ${'dummy-milestone-not-exempted'} | ${'the PR does have a milestone but not matching the specific issue exempted one'}    | ${true}
            ${true}       | ${'dummy-issue-milestone2'}       | ${'the PR does have a milestone matching the specific issue exempted one'}            | ${true}
            ${true}       | ${'dummy-milestone2'}             | ${'the PR does have a milestone matching the specific exempted one'}                  | ${false}
          `(
            'when $name',
            ({isPullRequest, milestone, shouldStale}: ITestData): void => {
              beforeEach((): void => {
                setTestIssueList(isPullRequest, milestone);
                setProcessor();
              });

              test(`should${
                shouldStale ? '' : ' not'
              } be marked as stale`, async () => {
                expect.assertions(3);

                await processor.processIssues(1);

                expect(processor.staleIssues.length).toStrictEqual(
                  shouldStale ? 1 : 0
                );
                expect(processor.closedIssues.length).toStrictEqual(0);
                expect(processor.removedLabelIssues.length).toStrictEqual(0);
              });
            }
          );
        });

        describe('when all the pull requests milestones should exempt a specific milestone', (): void => {
          beforeEach((): void => {
            opts.exemptPrMilestones =
              'dummy-pull-request-milestone1, dummy-pull-request-milestone2';
          });

          describe.each`
            isPullRequest | milestone                          | name                                                                                         | shouldStale
            ${false}      | ${''}                              | ${'the issue does not have a milestone'}                                                     | ${true}
            ${false}      | ${'dummy-milestone-not-exempted'}  | ${'the issue does have a milestone but not matching the specific pull request exempted one'} | ${true}
            ${false}      | ${'dummy-pull-request-milestone2'} | ${'the issue does have a milestone matching the specific pull request exempted one'}         | ${true}
            ${false}      | ${'dummy-milestone2'}              | ${'the issue does have a milestone matching the specific exempted one'}                      | ${false}
            ${true}       | ${''}                              | ${'the PR does not have a milestone'}                                                        | ${true}
            ${true}       | ${'dummy-milestone-not-exempted'}  | ${'the PR does have a milestone but not matching the specific pull request exempted one'}    | ${true}
            ${true}       | ${'dummy-pull-request-milestone2'} | ${'the PR does have a milestone matching the specific pull request exempted one'}            | ${false}
            ${true}       | ${'dummy-milestone2'}              | ${'the PR does have a milestone matching the specific exempted one'}                         | ${true}
          `(
            'when $name',
            ({isPullRequest, milestone, shouldStale}: ITestData): void => {
              beforeEach((): void => {
                setTestIssueList(isPullRequest, milestone);
                setProcessor();
              });

              test(`should${
                shouldStale ? '' : ' not'
              } be marked as stale`, async () => {
                expect.assertions(3);

                await processor.processIssues(1);

                expect(processor.staleIssues.length).toStrictEqual(
                  shouldStale ? 1 : 0
                );
                expect(processor.closedIssues.length).toStrictEqual(0);
                expect(processor.removedLabelIssues.length).toStrictEqual(0);
              });
            }
          );
        });
      });
    });

    describe('when all the issues milestones should not exempt', (): void => {
      beforeEach((): void => {
        opts.exemptAllIssueMilestones = false;
      });

      describe.each`
        isPullRequest | milestone            | name                                     | shouldStale
        ${false}      | ${''}                | ${'the issue does not have a milestone'} | ${true}
        ${false}      | ${'dummy-milestone'} | ${'the issue does have a milestone'}     | ${true}
        ${true}       | ${''}                | ${'the PR does not have a milestone'}    | ${true}
        ${true}       | ${'dummy-milestone'} | ${'the PR does have a milestone'}        | ${true}
      `(
        'when $name',
        ({isPullRequest, milestone, shouldStale}: ITestData): void => {
          beforeEach((): void => {
            setTestIssueList(isPullRequest, milestone);
            setProcessor();
          });

          test(`should${
            shouldStale ? '' : ' not'
          } be marked as stale`, async () => {
            expect.assertions(3);

            await processor.processIssues(1);

            expect(processor.staleIssues.length).toStrictEqual(
              shouldStale ? 1 : 0
            );
            expect(processor.closedIssues.length).toStrictEqual(0);
            expect(processor.removedLabelIssues.length).toStrictEqual(0);
          });
        }
      );

      describe('when all the issues and pull requests milestones should exempt a specific milestone', (): void => {
        beforeEach((): void => {
          opts.exemptMilestones = 'dummy-milestone';
        });

        describe.each`
          isPullRequest | milestone                         | name                                                                            | shouldStale
          ${false}      | ${''}                             | ${'the issue does not have a milestone'}                                        | ${true}
          ${false}      | ${'dummy-milestone-not-exempted'} | ${'the issue does have a milestone but not matching the specific exempted one'} | ${true}
          ${false}      | ${'dummy-milestone'}              | ${'the issue does have a milestone matching the specific exempted one'}         | ${false}
          ${true}       | ${''}                             | ${'the PR does not have a milestone'}                                           | ${true}
          ${true}       | ${'dummy-milestone-not-exempted'} | ${'the PR does have a milestone but not matching the specific exempted one'}    | ${true}
          ${true}       | ${'dummy-milestone'}              | ${'the PR does have a milestone matching the specific exempted one'}            | ${false}
        `(
          'when $name',
          ({isPullRequest, milestone, shouldStale}: ITestData): void => {
            beforeEach((): void => {
              setTestIssueList(isPullRequest, milestone);
              setProcessor();
            });

            test(`should${
              shouldStale ? '' : ' not'
            } be marked as stale`, async () => {
              expect.assertions(3);

              await processor.processIssues(1);

              expect(processor.staleIssues.length).toStrictEqual(
                shouldStale ? 1 : 0
              );
              expect(processor.closedIssues.length).toStrictEqual(0);
              expect(processor.removedLabelIssues.length).toStrictEqual(0);
            });
          }
        );

        describe('when all the issues milestones should exempt a specific milestone', (): void => {
          beforeEach((): void => {
            opts.exemptIssueMilestones = 'dummy-issue-milestone';
          });

          describe.each`
            isPullRequest | milestone                         | name                                                                                  | shouldStale
            ${false}      | ${''}                             | ${'the issue does not have a milestone'}                                              | ${true}
            ${false}      | ${'dummy-milestone-not-exempted'} | ${'the issue does have a milestone but not matching the specific issue exempted one'} | ${true}
            ${false}      | ${'dummy-issue-milestone'}        | ${'the issue does have a milestone matching the specific issue exempted one'}         | ${false}
            ${false}      | ${'dummy-milestone'}              | ${'the issue does have a milestone matching the specific exempted one'}               | ${true}
            ${true}       | ${''}                             | ${'the PR does not have a milestone'}                                                 | ${true}
            ${true}       | ${'dummy-milestone-not-exempted'} | ${'the PR does have a milestone but not matching the specific issue exempted one'}    | ${true}
            ${true}       | ${'dummy-issue-milestone'}        | ${'the PR does have a milestone matching the specific issue exempted one'}            | ${true}
            ${true}       | ${'dummy-milestone'}              | ${'the PR does have a milestone matching the specific exempted one'}                  | ${false}
          `(
            'when $name',
            ({isPullRequest, milestone, shouldStale}: ITestData): void => {
              beforeEach((): void => {
                setTestIssueList(isPullRequest, milestone);
                setProcessor();
              });

              test(`should${
                shouldStale ? '' : ' not'
              } be marked as stale`, async () => {
                expect.assertions(3);

                await processor.processIssues(1);

                expect(processor.staleIssues.length).toStrictEqual(
                  shouldStale ? 1 : 0
                );
                expect(processor.closedIssues.length).toStrictEqual(0);
                expect(processor.removedLabelIssues.length).toStrictEqual(0);
              });
            }
          );
        });

        describe('when all the pull requests milestones should exempt a specific milestone', (): void => {
          beforeEach((): void => {
            opts.exemptPrMilestones = 'dummy-pull-request-milestone';
          });

          describe.each`
            isPullRequest | milestone                         | name                                                                                         | shouldStale
            ${false}      | ${''}                             | ${'the issue does not have a milestone'}                                                     | ${true}
            ${false}      | ${'dummy-milestone-not-exempted'} | ${'the issue does have a milestone but not matching the specific pull request exempted one'} | ${true}
            ${false}      | ${'dummy-pull-request-milestone'} | ${'the issue does have a milestone matching the specific pull request exempted one'}         | ${true}
            ${false}      | ${'dummy-milestone'}              | ${'the issue does have a milestone matching the specific exempted one'}                      | ${false}
            ${true}       | ${''}                             | ${'the PR does not have a milestone'}                                                        | ${true}
            ${true}       | ${'dummy-milestone-not-exempted'} | ${'the PR does have a milestone but not matching the specific pull request exempted one'}    | ${true}
            ${true}       | ${'dummy-pull-request-milestone'} | ${'the PR does have a milestone matching the specific pull request exempted one'}            | ${false}
            ${true}       | ${'dummy-milestone'}              | ${'the PR does have a milestone matching the specific exempted one'}                         | ${true}
          `(
            'when $name',
            ({isPullRequest, milestone, shouldStale}: ITestData): void => {
              beforeEach((): void => {
                setTestIssueList(isPullRequest, milestone);
                setProcessor();
              });

              test(`should${
                shouldStale ? '' : ' not'
              } be marked as stale`, async () => {
                expect.assertions(3);

                await processor.processIssues(1);

                expect(processor.staleIssues.length).toStrictEqual(
                  shouldStale ? 1 : 0
                );
                expect(processor.closedIssues.length).toStrictEqual(0);
                expect(processor.removedLabelIssues.length).toStrictEqual(0);
              });
            }
          );
        });
      });

      describe('when all the issues and pull requests milestones should exempt some milestones', (): void => {
        beforeEach((): void => {
          opts.exemptMilestones = 'dummy-milestone1, dummy-milestone2';
        });

        describe.each`
          isPullRequest | milestone                         | name                                                                            | shouldStale
          ${false}      | ${''}                             | ${'the issue does not have a milestone'}                                        | ${true}
          ${false}      | ${'dummy-milestone-not-exempted'} | ${'the issue does have a milestone but not matching the specific exempted one'} | ${true}
          ${false}      | ${'dummy-milestone2'}             | ${'the issue does have a milestone matching the specific exempted one'}         | ${false}
          ${true}       | ${''}                             | ${'the PR does not have a milestone'}                                           | ${true}
          ${true}       | ${'dummy-milestone-not-exempted'} | ${'the PR does have a milestone but not matching the specific exempted one'}    | ${true}
          ${true}       | ${'dummy-milestone2'}             | ${'the PR does have a milestone matching the specific exempted one'}            | ${false}
        `(
          'when $name',
          ({isPullRequest, milestone, shouldStale}: ITestData): void => {
            beforeEach((): void => {
              setTestIssueList(isPullRequest, milestone);
              setProcessor();
            });

            test(`should${
              shouldStale ? '' : ' not'
            } be marked as stale`, async () => {
              expect.assertions(3);

              await processor.processIssues(1);

              expect(processor.staleIssues.length).toStrictEqual(
                shouldStale ? 1 : 0
              );
              expect(processor.closedIssues.length).toStrictEqual(0);
              expect(processor.removedLabelIssues.length).toStrictEqual(0);
            });
          }
        );

        describe('when all the issues milestones should exempt a specific milestone', (): void => {
          beforeEach((): void => {
            opts.exemptIssueMilestones =
              'dummy-issue-milestone1, dummy-issue-milestone2';
          });

          describe.each`
            isPullRequest | milestone                         | name                                                                                  | shouldStale
            ${false}      | ${''}                             | ${'the issue does not have a milestone'}                                              | ${true}
            ${false}      | ${'dummy-milestone-not-exempted'} | ${'the issue does have a milestone but not matching the specific issue exempted one'} | ${true}
            ${false}      | ${'dummy-issue-milestone2'}       | ${'the issue does have a milestone matching the specific issue exempted one'}         | ${false}
            ${false}      | ${'dummy-milestone2'}             | ${'the issue does have a milestone matching the specific exempted one'}               | ${true}
            ${true}       | ${''}                             | ${'the PR does not have a milestone'}                                                 | ${true}
            ${true}       | ${'dummy-milestone-not-exempted'} | ${'the PR does have a milestone but not matching the specific issue exempted one'}    | ${true}
            ${true}       | ${'dummy-issue-milestone2'}       | ${'the PR does have a milestone matching the specific issue exempted one'}            | ${true}
            ${true}       | ${'dummy-milestone2'}             | ${'the PR does have a milestone matching the specific exempted one'}                  | ${false}
          `(
            'when $name',
            ({isPullRequest, milestone, shouldStale}: ITestData): void => {
              beforeEach((): void => {
                setTestIssueList(isPullRequest, milestone);
                setProcessor();
              });

              test(`should${
                shouldStale ? '' : ' not'
              } be marked as stale`, async () => {
                expect.assertions(3);

                await processor.processIssues(1);

                expect(processor.staleIssues.length).toStrictEqual(
                  shouldStale ? 1 : 0
                );
                expect(processor.closedIssues.length).toStrictEqual(0);
                expect(processor.removedLabelIssues.length).toStrictEqual(0);
              });
            }
          );
        });

        describe('when all the pull requests milestones should exempt a specific milestone', (): void => {
          beforeEach((): void => {
            opts.exemptPrMilestones =
              'dummy-pull-request-milestone1, dummy-pull-request-milestone2';
          });

          describe.each`
            isPullRequest | milestone                          | name                                                                                         | shouldStale
            ${false}      | ${''}                              | ${'the issue does not have a milestone'}                                                     | ${true}
            ${false}      | ${'dummy-milestone-not-exempted'}  | ${'the issue does have a milestone but not matching the specific pull request exempted one'} | ${true}
            ${false}      | ${'dummy-pull-request-milestone2'} | ${'the issue does have a milestone matching the specific pull request exempted one'}         | ${true}
            ${false}      | ${'dummy-milestone2'}              | ${'the issue does have a milestone matching the specific exempted one'}                      | ${false}
            ${true}       | ${''}                              | ${'the PR does not have a milestone'}                                                        | ${true}
            ${true}       | ${'dummy-milestone-not-exempted'}  | ${'the PR does have a milestone but not matching the specific pull request exempted one'}    | ${true}
            ${true}       | ${'dummy-pull-request-milestone2'} | ${'the PR does have a milestone matching the specific pull request exempted one'}            | ${false}
            ${true}       | ${'dummy-milestone2'}              | ${'the PR does have a milestone matching the specific exempted one'}                         | ${true}
          `(
            'when $name',
            ({isPullRequest, milestone, shouldStale}: ITestData): void => {
              beforeEach((): void => {
                setTestIssueList(isPullRequest, milestone);
                setProcessor();
              });

              test(`should${
                shouldStale ? '' : ' not'
              } be marked as stale`, async () => {
                expect.assertions(3);

                await processor.processIssues(1);

                expect(processor.staleIssues.length).toStrictEqual(
                  shouldStale ? 1 : 0
                );
                expect(processor.closedIssues.length).toStrictEqual(0);
                expect(processor.removedLabelIssues.length).toStrictEqual(0);
              });
            }
          );
        });
      });
    });

    describe('when all the issues milestones should exempt', (): void => {
      beforeEach((): void => {
        opts.exemptAllIssueMilestones = true;
      });

      describe.each`
        isPullRequest | milestone            | name                                     | shouldStale
        ${false}      | ${''}                | ${'the issue does not have a milestone'} | ${true}
        ${false}      | ${'dummy-milestone'} | ${'the issue does have a milestone'}     | ${false}
        ${true}       | ${''}                | ${'the PR does not have a milestone'}    | ${true}
        ${true}       | ${'dummy-milestone'} | ${'the PR does have a milestone'}        | ${true}
      `(
        'when $name',
        ({isPullRequest, milestone, shouldStale}: ITestData): void => {
          beforeEach((): void => {
            setTestIssueList(isPullRequest, milestone);
            setProcessor();
          });

          test(`should${
            shouldStale ? '' : ' not'
          } be marked as stale`, async () => {
            expect.assertions(3);

            await processor.processIssues(1);

            expect(processor.staleIssues.length).toStrictEqual(
              shouldStale ? 1 : 0
            );
            expect(processor.closedIssues.length).toStrictEqual(0);
            expect(processor.removedLabelIssues.length).toStrictEqual(0);
          });
        }
      );

      describe('when all the issues and pull requests milestones should exempt a specific milestone', (): void => {
        beforeEach((): void => {
          opts.exemptMilestones = 'dummy-milestone';
        });

        describe.each`
          isPullRequest | milestone                         | name                                                                            | shouldStale
          ${false}      | ${''}                             | ${'the issue does not have a milestone'}                                        | ${true}
          ${false}      | ${'dummy-milestone-not-exempted'} | ${'the issue does have a milestone but not matching the specific exempted one'} | ${false}
          ${false}      | ${'dummy-milestone'}              | ${'the issue does have a milestone matching the specific exempted one'}         | ${false}
          ${true}       | ${''}                             | ${'the PR does not have a milestone'}                                           | ${true}
          ${true}       | ${'dummy-milestone-not-exempted'} | ${'the PR does have a milestone but not matching the specific exempted one'}    | ${true}
          ${true}       | ${'dummy-milestone'}              | ${'the PR does have a milestone matching the specific exempted one'}            | ${false}
        `(
          'when $name',
          ({isPullRequest, milestone, shouldStale}: ITestData): void => {
            beforeEach((): void => {
              setTestIssueList(isPullRequest, milestone);
              setProcessor();
            });

            test(`should${
              shouldStale ? '' : ' not'
            } be marked as stale`, async () => {
              expect.assertions(3);

              await processor.processIssues(1);

              expect(processor.staleIssues.length).toStrictEqual(
                shouldStale ? 1 : 0
              );
              expect(processor.closedIssues.length).toStrictEqual(0);
              expect(processor.removedLabelIssues.length).toStrictEqual(0);
            });
          }
        );

        describe('when all the issues milestones should exempt a specific milestone', (): void => {
          beforeEach((): void => {
            opts.exemptIssueMilestones = 'dummy-issue-milestone';
          });

          describe.each`
            isPullRequest | milestone                         | name                                                                                  | shouldStale
            ${false}      | ${''}                             | ${'the issue does not have a milestone'}                                              | ${true}
            ${false}      | ${'dummy-milestone-not-exempted'} | ${'the issue does have a milestone but not matching the specific issue exempted one'} | ${false}
            ${false}      | ${'dummy-issue-milestone'}        | ${'the issue does have a milestone matching the specific issue exempted one'}         | ${false}
            ${false}      | ${'dummy-milestone'}              | ${'the issue does have a milestone matching the specific exempted one'}               | ${false}
            ${true}       | ${''}                             | ${'the PR does not have a milestone'}                                                 | ${true}
            ${true}       | ${'dummy-milestone-not-exempted'} | ${'the PR does have a milestone but not matching the specific issue exempted one'}    | ${true}
            ${true}       | ${'dummy-issue-milestone'}        | ${'the PR does have a milestone matching the specific issue exempted one'}            | ${true}
            ${true}       | ${'dummy-milestone'}              | ${'the PR does have a milestone matching the specific exempted one'}                  | ${false}
          `(
            'when $name',
            ({isPullRequest, milestone, shouldStale}: ITestData): void => {
              beforeEach((): void => {
                setTestIssueList(isPullRequest, milestone);
                setProcessor();
              });

              test(`should${
                shouldStale ? '' : ' not'
              } be marked as stale`, async () => {
                expect.assertions(3);

                await processor.processIssues(1);

                expect(processor.staleIssues.length).toStrictEqual(
                  shouldStale ? 1 : 0
                );
                expect(processor.closedIssues.length).toStrictEqual(0);
                expect(processor.removedLabelIssues.length).toStrictEqual(0);
              });
            }
          );
        });

        describe('when all the pull requests milestones should exempt a specific milestone', (): void => {
          beforeEach((): void => {
            opts.exemptPrMilestones = 'dummy-pull-request-milestone';
          });

          describe.each`
            isPullRequest | milestone                         | name                                                                                         | shouldStale
            ${false}      | ${''}                             | ${'the issue does not have a milestone'}                                                     | ${true}
            ${false}      | ${'dummy-milestone-not-exempted'} | ${'the issue does have a milestone but not matching the specific pull request exempted one'} | ${false}
            ${false}      | ${'dummy-pull-request-milestone'} | ${'the issue does have a milestone matching the specific pull request exempted one'}         | ${false}
            ${false}      | ${'dummy-milestone'}              | ${'the issue does have a milestone matching the specific exempted one'}                      | ${false}
            ${true}       | ${''}                             | ${'the PR does not have a milestone'}                                                        | ${true}
            ${true}       | ${'dummy-milestone-not-exempted'} | ${'the PR does have a milestone but not matching the specific pull request exempted one'}    | ${true}
            ${true}       | ${'dummy-pull-request-milestone'} | ${'the PR does have a milestone matching the specific pull request exempted one'}            | ${false}
            ${true}       | ${'dummy-milestone'}              | ${'the PR does have a milestone matching the specific exempted one'}                         | ${true}
          `(
            'when $name',
            ({isPullRequest, milestone, shouldStale}: ITestData): void => {
              beforeEach((): void => {
                setTestIssueList(isPullRequest, milestone);
                setProcessor();
              });

              test(`should${
                shouldStale ? '' : ' not'
              } be marked as stale`, async () => {
                expect.assertions(3);

                await processor.processIssues(1);

                expect(processor.staleIssues.length).toStrictEqual(
                  shouldStale ? 1 : 0
                );
                expect(processor.closedIssues.length).toStrictEqual(0);
                expect(processor.removedLabelIssues.length).toStrictEqual(0);
              });
            }
          );
        });
      });

      describe('when all the issues and pull requests milestones should exempt some milestones', (): void => {
        beforeEach((): void => {
          opts.exemptMilestones = 'dummy-milestone1, dummy-milestone2';
        });

        describe.each`
          isPullRequest | milestone                         | name                                                                            | shouldStale
          ${false}      | ${''}                             | ${'the issue does not have a milestone'}                                        | ${true}
          ${false}      | ${'dummy-milestone-not-exempted'} | ${'the issue does have a milestone but not matching the specific exempted one'} | ${false}
          ${false}      | ${'dummy-milestone2'}             | ${'the issue does have a milestone matching the specific exempted one'}         | ${false}
          ${true}       | ${''}                             | ${'the PR does not have a milestone'}                                           | ${true}
          ${true}       | ${'dummy-milestone-not-exempted'} | ${'the PR does have a milestone but not matching the specific exempted one'}    | ${true}
          ${true}       | ${'dummy-milestone2'}             | ${'the PR does have a milestone matching the specific exempted one'}            | ${false}
        `(
          'when $name',
          ({isPullRequest, milestone, shouldStale}: ITestData): void => {
            beforeEach((): void => {
              setTestIssueList(isPullRequest, milestone);
              setProcessor();
            });

            test(`should${
              shouldStale ? '' : ' not'
            } be marked as stale`, async () => {
              expect.assertions(3);

              await processor.processIssues(1);

              expect(processor.staleIssues.length).toStrictEqual(
                shouldStale ? 1 : 0
              );
              expect(processor.closedIssues.length).toStrictEqual(0);
              expect(processor.removedLabelIssues.length).toStrictEqual(0);
            });
          }
        );

        describe('when all the issues milestones should exempt a specific milestone', (): void => {
          beforeEach((): void => {
            opts.exemptIssueMilestones =
              'dummy-issue-milestone1, dummy-issue-milestone2';
          });

          describe.each`
            isPullRequest | milestone                         | name                                                                                  | shouldStale
            ${false}      | ${''}                             | ${'the issue does not have a milestone'}                                              | ${true}
            ${false}      | ${'dummy-milestone-not-exempted'} | ${'the issue does have a milestone but not matching the specific issue exempted one'} | ${false}
            ${false}      | ${'dummy-issue-milestone2'}       | ${'the issue does have a milestone matching the specific issue exempted one'}         | ${false}
            ${false}      | ${'dummy-milestone2'}             | ${'the issue does have a milestone matching the specific exempted one'}               | ${false}
            ${true}       | ${''}                             | ${'the PR does not have a milestone'}                                                 | ${true}
            ${true}       | ${'dummy-milestone-not-exempted'} | ${'the PR does have a milestone but not matching the specific issue exempted one'}    | ${true}
            ${true}       | ${'dummy-issue-milestone2'}       | ${'the PR does have a milestone matching the specific issue exempted one'}            | ${true}
            ${true}       | ${'dummy-milestone2'}             | ${'the PR does have a milestone matching the specific exempted one'}                  | ${false}
          `(
            'when $name',
            ({isPullRequest, milestone, shouldStale}: ITestData): void => {
              beforeEach((): void => {
                setTestIssueList(isPullRequest, milestone);
                setProcessor();
              });

              test(`should${
                shouldStale ? '' : ' not'
              } be marked as stale`, async () => {
                expect.assertions(3);

                await processor.processIssues(1);

                expect(processor.staleIssues.length).toStrictEqual(
                  shouldStale ? 1 : 0
                );
                expect(processor.closedIssues.length).toStrictEqual(0);
                expect(processor.removedLabelIssues.length).toStrictEqual(0);
              });
            }
          );
        });

        describe('when all the pull requests milestones should exempt a specific milestone', (): void => {
          beforeEach((): void => {
            opts.exemptPrMilestones =
              'dummy-pull-request-milestone1, dummy-pull-request-milestone2';
          });

          describe.each`
            isPullRequest | milestone                          | name                                                                                         | shouldStale
            ${false}      | ${''}                              | ${'the issue does not have a milestone'}                                                     | ${true}
            ${false}      | ${'dummy-milestone-not-exempted'}  | ${'the issue does have a milestone but not matching the specific pull request exempted one'} | ${false}
            ${false}      | ${'dummy-pull-request-milestone2'} | ${'the issue does have a milestone matching the specific pull request exempted one'}         | ${false}
            ${false}      | ${'dummy-milestone2'}              | ${'the issue does have a milestone matching the specific exempted one'}                      | ${false}
            ${true}       | ${''}                              | ${'the PR does not have a milestone'}                                                        | ${true}
            ${true}       | ${'dummy-milestone-not-exempted'}  | ${'the PR does have a milestone but not matching the specific pull request exempted one'}    | ${true}
            ${true}       | ${'dummy-pull-request-milestone2'} | ${'the PR does have a milestone matching the specific pull request exempted one'}            | ${false}
            ${true}       | ${'dummy-milestone2'}              | ${'the PR does have a milestone matching the specific exempted one'}                         | ${true}
          `(
            'when $name',
            ({isPullRequest, milestone, shouldStale}: ITestData): void => {
              beforeEach((): void => {
                setTestIssueList(isPullRequest, milestone);
                setProcessor();
              });

              test(`should${
                shouldStale ? '' : ' not'
              } be marked as stale`, async () => {
                expect.assertions(3);

                await processor.processIssues(1);

                expect(processor.staleIssues.length).toStrictEqual(
                  shouldStale ? 1 : 0
                );
                expect(processor.closedIssues.length).toStrictEqual(0);
                expect(processor.removedLabelIssues.length).toStrictEqual(0);
              });
            }
          );
        });
      });
    });

    describe('when all the pull requests milestones are not configured to exempt', (): void => {
      beforeEach((): void => {
        opts.exemptAllPrMilestones = undefined;
      });

      describe.each`
        isPullRequest | milestone            | name                                     | shouldStale
        ${false}      | ${''}                | ${'the issue does not have a milestone'} | ${true}
        ${false}      | ${'dummy-milestone'} | ${'the issue does have a milestone'}     | ${true}
        ${true}       | ${''}                | ${'the PR does not have a milestone'}    | ${true}
        ${true}       | ${'dummy-milestone'} | ${'the PR does have a milestone'}        | ${true}
      `(
        'when $name',
        ({isPullRequest, milestone, shouldStale}: ITestData): void => {
          beforeEach((): void => {
            setTestIssueList(isPullRequest, milestone);
            setProcessor();
          });

          test(`should${
            shouldStale ? '' : ' not'
          } be marked as stale`, async () => {
            expect.assertions(3);

            await processor.processIssues(1);

            expect(processor.staleIssues.length).toStrictEqual(
              shouldStale ? 1 : 0
            );
            expect(processor.closedIssues.length).toStrictEqual(0);
            expect(processor.removedLabelIssues.length).toStrictEqual(0);
          });
        }
      );

      describe('when all the issues and pull requests milestones should exempt a specific milestone', (): void => {
        beforeEach((): void => {
          opts.exemptMilestones = 'dummy-milestone';
        });

        describe.each`
          isPullRequest | milestone                         | name                                                                            | shouldStale
          ${false}      | ${''}                             | ${'the issue does not have a milestone'}                                        | ${true}
          ${false}      | ${'dummy-milestone-not-exempted'} | ${'the issue does have a milestone but not matching the specific exempted one'} | ${true}
          ${false}      | ${'dummy-milestone'}              | ${'the issue does have a milestone matching the specific exempted one'}         | ${false}
          ${true}       | ${''}                             | ${'the PR does not have a milestone'}                                           | ${true}
          ${true}       | ${'dummy-milestone-not-exempted'} | ${'the PR does have a milestone but not matching the specific exempted one'}    | ${true}
          ${true}       | ${'dummy-milestone'}              | ${'the PR does have a milestone matching the specific exempted one'}            | ${false}
        `(
          'when $name',
          ({isPullRequest, milestone, shouldStale}: ITestData): void => {
            beforeEach((): void => {
              setTestIssueList(isPullRequest, milestone);
              setProcessor();
            });

            test(`should${
              shouldStale ? '' : ' not'
            } be marked as stale`, async () => {
              expect.assertions(3);

              await processor.processIssues(1);

              expect(processor.staleIssues.length).toStrictEqual(
                shouldStale ? 1 : 0
              );
              expect(processor.closedIssues.length).toStrictEqual(0);
              expect(processor.removedLabelIssues.length).toStrictEqual(0);
            });
          }
        );

        describe('when all the issues milestones should exempt a specific milestone', (): void => {
          beforeEach((): void => {
            opts.exemptIssueMilestones = 'dummy-issue-milestone';
          });

          describe.each`
            isPullRequest | milestone                         | name                                                                                  | shouldStale
            ${false}      | ${''}                             | ${'the issue does not have a milestone'}                                              | ${true}
            ${false}      | ${'dummy-milestone-not-exempted'} | ${'the issue does have a milestone but not matching the specific issue exempted one'} | ${true}
            ${false}      | ${'dummy-issue-milestone'}        | ${'the issue does have a milestone matching the specific issue exempted one'}         | ${false}
            ${false}      | ${'dummy-milestone'}              | ${'the issue does have a milestone matching the specific exempted one'}               | ${true}
            ${true}       | ${''}                             | ${'the PR does not have a milestone'}                                                 | ${true}
            ${true}       | ${'dummy-milestone-not-exempted'} | ${'the PR does have a milestone but not matching the specific issue exempted one'}    | ${true}
            ${true}       | ${'dummy-issue-milestone'}        | ${'the PR does have a milestone matching the specific issue exempted one'}            | ${true}
            ${true}       | ${'dummy-milestone'}              | ${'the PR does have a milestone matching the specific exempted one'}                  | ${false}
          `(
            'when $name',
            ({isPullRequest, milestone, shouldStale}: ITestData): void => {
              beforeEach((): void => {
                setTestIssueList(isPullRequest, milestone);
                setProcessor();
              });

              test(`should${
                shouldStale ? '' : ' not'
              } be marked as stale`, async () => {
                expect.assertions(3);

                await processor.processIssues(1);

                expect(processor.staleIssues.length).toStrictEqual(
                  shouldStale ? 1 : 0
                );
                expect(processor.closedIssues.length).toStrictEqual(0);
                expect(processor.removedLabelIssues.length).toStrictEqual(0);
              });
            }
          );
        });

        describe('when all the pull requests milestones should exempt a specific milestone', (): void => {
          beforeEach((): void => {
            opts.exemptPrMilestones = 'dummy-pull-request-milestone';
          });

          describe.each`
            isPullRequest | milestone                         | name                                                                                         | shouldStale
            ${false}      | ${''}                             | ${'the issue does not have a milestone'}                                                     | ${true}
            ${false}      | ${'dummy-milestone-not-exempted'} | ${'the issue does have a milestone but not matching the specific pull request exempted one'} | ${true}
            ${false}      | ${'dummy-pull-request-milestone'} | ${'the issue does have a milestone matching the specific pull request exempted one'}         | ${true}
            ${false}      | ${'dummy-milestone'}              | ${'the issue does have a milestone matching the specific exempted one'}                      | ${false}
            ${true}       | ${''}                             | ${'the PR does not have a milestone'}                                                        | ${true}
            ${true}       | ${'dummy-milestone-not-exempted'} | ${'the PR does have a milestone but not matching the specific pull request exempted one'}    | ${true}
            ${true}       | ${'dummy-pull-request-milestone'} | ${'the PR does have a milestone matching the specific pull request exempted one'}            | ${false}
            ${true}       | ${'dummy-milestone'}              | ${'the PR does have a milestone matching the specific exempted one'}                         | ${true}
          `(
            'when $name',
            ({isPullRequest, milestone, shouldStale}: ITestData): void => {
              beforeEach((): void => {
                setTestIssueList(isPullRequest, milestone);
                setProcessor();
              });

              test(`should${
                shouldStale ? '' : ' not'
              } be marked as stale`, async () => {
                expect.assertions(3);

                await processor.processIssues(1);

                expect(processor.staleIssues.length).toStrictEqual(
                  shouldStale ? 1 : 0
                );
                expect(processor.closedIssues.length).toStrictEqual(0);
                expect(processor.removedLabelIssues.length).toStrictEqual(0);
              });
            }
          );
        });
      });

      describe('when all the issues and pull requests milestones should exempt some milestones', (): void => {
        beforeEach((): void => {
          opts.exemptMilestones = 'dummy-milestone1, dummy-milestone2';
        });

        describe.each`
          isPullRequest | milestone                         | name                                                                            | shouldStale
          ${false}      | ${''}                             | ${'the issue does not have a milestone'}                                        | ${true}
          ${false}      | ${'dummy-milestone-not-exempted'} | ${'the issue does have a milestone but not matching the specific exempted one'} | ${true}
          ${false}      | ${'dummy-milestone2'}             | ${'the issue does have a milestone matching the specific exempted one'}         | ${false}
          ${true}       | ${''}                             | ${'the PR does not have a milestone'}                                           | ${true}
          ${true}       | ${'dummy-milestone-not-exempted'} | ${'the PR does have a milestone but not matching the specific exempted one'}    | ${true}
          ${true}       | ${'dummy-milestone2'}             | ${'the PR does have a milestone matching the specific exempted one'}            | ${false}
        `(
          'when $name',
          ({isPullRequest, milestone, shouldStale}: ITestData): void => {
            beforeEach((): void => {
              setTestIssueList(isPullRequest, milestone);
              setProcessor();
            });

            test(`should${
              shouldStale ? '' : ' not'
            } be marked as stale`, async () => {
              expect.assertions(3);

              await processor.processIssues(1);

              expect(processor.staleIssues.length).toStrictEqual(
                shouldStale ? 1 : 0
              );
              expect(processor.closedIssues.length).toStrictEqual(0);
              expect(processor.removedLabelIssues.length).toStrictEqual(0);
            });
          }
        );

        describe('when all the issues milestones should exempt a specific milestone', (): void => {
          beforeEach((): void => {
            opts.exemptIssueMilestones =
              'dummy-issue-milestone1, dummy-issue-milestone2';
          });

          describe.each`
            isPullRequest | milestone                         | name                                                                                  | shouldStale
            ${false}      | ${''}                             | ${'the issue does not have a milestone'}                                              | ${true}
            ${false}      | ${'dummy-milestone-not-exempted'} | ${'the issue does have a milestone but not matching the specific issue exempted one'} | ${true}
            ${false}      | ${'dummy-issue-milestone2'}       | ${'the issue does have a milestone matching the specific issue exempted one'}         | ${false}
            ${false}      | ${'dummy-milestone2'}             | ${'the issue does have a milestone matching the specific exempted one'}               | ${true}
            ${true}       | ${''}                             | ${'the PR does not have a milestone'}                                                 | ${true}
            ${true}       | ${'dummy-milestone-not-exempted'} | ${'the PR does have a milestone but not matching the specific issue exempted one'}    | ${true}
            ${true}       | ${'dummy-issue-milestone2'}       | ${'the PR does have a milestone matching the specific issue exempted one'}            | ${true}
            ${true}       | ${'dummy-milestone2'}             | ${'the PR does have a milestone matching the specific exempted one'}                  | ${false}
          `(
            'when $name',
            ({isPullRequest, milestone, shouldStale}: ITestData): void => {
              beforeEach((): void => {
                setTestIssueList(isPullRequest, milestone);
                setProcessor();
              });

              test(`should${
                shouldStale ? '' : ' not'
              } be marked as stale`, async () => {
                expect.assertions(3);

                await processor.processIssues(1);

                expect(processor.staleIssues.length).toStrictEqual(
                  shouldStale ? 1 : 0
                );
                expect(processor.closedIssues.length).toStrictEqual(0);
                expect(processor.removedLabelIssues.length).toStrictEqual(0);
              });
            }
          );
        });

        describe('when all the pull requests milestones should exempt a specific milestone', (): void => {
          beforeEach((): void => {
            opts.exemptPrMilestones =
              'dummy-pull-request-milestone1, dummy-pull-request-milestone2';
          });

          describe.each`
            isPullRequest | milestone                          | name                                                                                         | shouldStale
            ${false}      | ${''}                              | ${'the issue does not have a milestone'}                                                     | ${true}
            ${false}      | ${'dummy-milestone-not-exempted'}  | ${'the issue does have a milestone but not matching the specific pull request exempted one'} | ${true}
            ${false}      | ${'dummy-pull-request-milestone2'} | ${'the issue does have a milestone matching the specific pull request exempted one'}         | ${true}
            ${false}      | ${'dummy-milestone2'}              | ${'the issue does have a milestone matching the specific exempted one'}                      | ${false}
            ${true}       | ${''}                              | ${'the PR does not have a milestone'}                                                        | ${true}
            ${true}       | ${'dummy-milestone-not-exempted'}  | ${'the PR does have a milestone but not matching the specific pull request exempted one'}    | ${true}
            ${true}       | ${'dummy-pull-request-milestone2'} | ${'the PR does have a milestone matching the specific pull request exempted one'}            | ${false}
            ${true}       | ${'dummy-milestone2'}              | ${'the PR does have a milestone matching the specific exempted one'}                         | ${true}
          `(
            'when $name',
            ({isPullRequest, milestone, shouldStale}: ITestData): void => {
              beforeEach((): void => {
                setTestIssueList(isPullRequest, milestone);
                setProcessor();
              });

              test(`should${
                shouldStale ? '' : ' not'
              } be marked as stale`, async () => {
                expect.assertions(3);

                await processor.processIssues(1);

                expect(processor.staleIssues.length).toStrictEqual(
                  shouldStale ? 1 : 0
                );
                expect(processor.closedIssues.length).toStrictEqual(0);
                expect(processor.removedLabelIssues.length).toStrictEqual(0);
              });
            }
          );
        });
      });
    });

    describe('when all the pull requests milestones should not exempt', (): void => {
      beforeEach((): void => {
        opts.exemptAllPrMilestones = false;
      });

      describe.each`
        isPullRequest | milestone            | name                                     | shouldStale
        ${false}      | ${''}                | ${'the issue does not have a milestone'} | ${true}
        ${false}      | ${'dummy-milestone'} | ${'the issue does have a milestone'}     | ${true}
        ${true}       | ${''}                | ${'the PR does not have a milestone'}    | ${true}
        ${true}       | ${'dummy-milestone'} | ${'the PR does have a milestone'}        | ${true}
      `(
        'when $name',
        ({isPullRequest, milestone, shouldStale}: ITestData): void => {
          beforeEach((): void => {
            setTestIssueList(isPullRequest, milestone);
            setProcessor();
          });

          test(`should${
            shouldStale ? '' : ' not'
          } be marked as stale`, async () => {
            expect.assertions(3);

            await processor.processIssues(1);

            expect(processor.staleIssues.length).toStrictEqual(
              shouldStale ? 1 : 0
            );
            expect(processor.closedIssues.length).toStrictEqual(0);
            expect(processor.removedLabelIssues.length).toStrictEqual(0);
          });
        }
      );

      describe('when all the issues and pull requests milestones should exempt a specific milestone', (): void => {
        beforeEach((): void => {
          opts.exemptMilestones = 'dummy-milestone';
        });

        describe.each`
          isPullRequest | milestone                         | name                                                                            | shouldStale
          ${false}      | ${''}                             | ${'the issue does not have a milestone'}                                        | ${true}
          ${false}      | ${'dummy-milestone-not-exempted'} | ${'the issue does have a milestone but not matching the specific exempted one'} | ${true}
          ${false}      | ${'dummy-milestone'}              | ${'the issue does have a milestone matching the specific exempted one'}         | ${false}
          ${true}       | ${''}                             | ${'the PR does not have a milestone'}                                           | ${true}
          ${true}       | ${'dummy-milestone-not-exempted'} | ${'the PR does have a milestone but not matching the specific exempted one'}    | ${true}
          ${true}       | ${'dummy-milestone'}              | ${'the PR does have a milestone matching the specific exempted one'}            | ${false}
        `(
          'when $name',
          ({isPullRequest, milestone, shouldStale}: ITestData): void => {
            beforeEach((): void => {
              setTestIssueList(isPullRequest, milestone);
              setProcessor();
            });

            test(`should${
              shouldStale ? '' : ' not'
            } be marked as stale`, async () => {
              expect.assertions(3);

              await processor.processIssues(1);

              expect(processor.staleIssues.length).toStrictEqual(
                shouldStale ? 1 : 0
              );
              expect(processor.closedIssues.length).toStrictEqual(0);
              expect(processor.removedLabelIssues.length).toStrictEqual(0);
            });
          }
        );

        describe('when all the issues milestones should exempt a specific milestone', (): void => {
          beforeEach((): void => {
            opts.exemptIssueMilestones = 'dummy-issue-milestone';
          });

          describe.each`
            isPullRequest | milestone                         | name                                                                                  | shouldStale
            ${false}      | ${''}                             | ${'the issue does not have a milestone'}                                              | ${true}
            ${false}      | ${'dummy-milestone-not-exempted'} | ${'the issue does have a milestone but not matching the specific issue exempted one'} | ${true}
            ${false}      | ${'dummy-issue-milestone'}        | ${'the issue does have a milestone matching the specific issue exempted one'}         | ${false}
            ${false}      | ${'dummy-milestone'}              | ${'the issue does have a milestone matching the specific exempted one'}               | ${true}
            ${true}       | ${''}                             | ${'the PR does not have a milestone'}                                                 | ${true}
            ${true}       | ${'dummy-milestone-not-exempted'} | ${'the PR does have a milestone but not matching the specific issue exempted one'}    | ${true}
            ${true}       | ${'dummy-issue-milestone'}        | ${'the PR does have a milestone matching the specific issue exempted one'}            | ${true}
            ${true}       | ${'dummy-milestone'}              | ${'the PR does have a milestone matching the specific exempted one'}                  | ${false}
          `(
            'when $name',
            ({isPullRequest, milestone, shouldStale}: ITestData): void => {
              beforeEach((): void => {
                setTestIssueList(isPullRequest, milestone);
                setProcessor();
              });

              test(`should${
                shouldStale ? '' : ' not'
              } be marked as stale`, async () => {
                expect.assertions(3);

                await processor.processIssues(1);

                expect(processor.staleIssues.length).toStrictEqual(
                  shouldStale ? 1 : 0
                );
                expect(processor.closedIssues.length).toStrictEqual(0);
                expect(processor.removedLabelIssues.length).toStrictEqual(0);
              });
            }
          );
        });

        describe('when all the pull requests milestones should exempt a specific milestone', (): void => {
          beforeEach((): void => {
            opts.exemptPrMilestones = 'dummy-pull-request-milestone';
          });

          describe.each`
            isPullRequest | milestone                         | name                                                                                         | shouldStale
            ${false}      | ${''}                             | ${'the issue does not have a milestone'}                                                     | ${true}
            ${false}      | ${'dummy-milestone-not-exempted'} | ${'the issue does have a milestone but not matching the specific pull request exempted one'} | ${true}
            ${false}      | ${'dummy-pull-request-milestone'} | ${'the issue does have a milestone matching the specific pull request exempted one'}         | ${true}
            ${false}      | ${'dummy-milestone'}              | ${'the issue does have a milestone matching the specific exempted one'}                      | ${false}
            ${true}       | ${''}                             | ${'the PR does not have a milestone'}                                                        | ${true}
            ${true}       | ${'dummy-milestone-not-exempted'} | ${'the PR does have a milestone but not matching the specific pull request exempted one'}    | ${true}
            ${true}       | ${'dummy-pull-request-milestone'} | ${'the PR does have a milestone matching the specific pull request exempted one'}            | ${false}
            ${true}       | ${'dummy-milestone'}              | ${'the PR does have a milestone matching the specific exempted one'}                         | ${true}
          `(
            'when $name',
            ({isPullRequest, milestone, shouldStale}: ITestData): void => {
              beforeEach((): void => {
                setTestIssueList(isPullRequest, milestone);
                setProcessor();
              });

              test(`should${
                shouldStale ? '' : ' not'
              } be marked as stale`, async () => {
                expect.assertions(3);

                await processor.processIssues(1);

                expect(processor.staleIssues.length).toStrictEqual(
                  shouldStale ? 1 : 0
                );
                expect(processor.closedIssues.length).toStrictEqual(0);
                expect(processor.removedLabelIssues.length).toStrictEqual(0);
              });
            }
          );
        });
      });

      describe('when all the issues and pull requests milestones should exempt some milestones', (): void => {
        beforeEach((): void => {
          opts.exemptMilestones = 'dummy-milestone1, dummy-milestone2';
        });

        describe.each`
          isPullRequest | milestone                         | name                                                                            | shouldStale
          ${false}      | ${''}                             | ${'the issue does not have a milestone'}                                        | ${true}
          ${false}      | ${'dummy-milestone-not-exempted'} | ${'the issue does have a milestone but not matching the specific exempted one'} | ${true}
          ${false}      | ${'dummy-milestone2'}             | ${'the issue does have a milestone matching the specific exempted one'}         | ${false}
          ${true}       | ${''}                             | ${'the PR does not have a milestone'}                                           | ${true}
          ${true}       | ${'dummy-milestone-not-exempted'} | ${'the PR does have a milestone but not matching the specific exempted one'}    | ${true}
          ${true}       | ${'dummy-milestone2'}             | ${'the PR does have a milestone matching the specific exempted one'}            | ${false}
        `(
          'when $name',
          ({isPullRequest, milestone, shouldStale}: ITestData): void => {
            beforeEach((): void => {
              setTestIssueList(isPullRequest, milestone);
              setProcessor();
            });

            test(`should${
              shouldStale ? '' : ' not'
            } be marked as stale`, async () => {
              expect.assertions(3);

              await processor.processIssues(1);

              expect(processor.staleIssues.length).toStrictEqual(
                shouldStale ? 1 : 0
              );
              expect(processor.closedIssues.length).toStrictEqual(0);
              expect(processor.removedLabelIssues.length).toStrictEqual(0);
            });
          }
        );

        describe('when all the issues milestones should exempt a specific milestone', (): void => {
          beforeEach((): void => {
            opts.exemptIssueMilestones =
              'dummy-issue-milestone1, dummy-issue-milestone2';
          });

          describe.each`
            isPullRequest | milestone                         | name                                                                                  | shouldStale
            ${false}      | ${''}                             | ${'the issue does not have a milestone'}                                              | ${true}
            ${false}      | ${'dummy-milestone-not-exempted'} | ${'the issue does have a milestone but not matching the specific issue exempted one'} | ${true}
            ${false}      | ${'dummy-issue-milestone2'}       | ${'the issue does have a milestone matching the specific issue exempted one'}         | ${false}
            ${false}      | ${'dummy-milestone2'}             | ${'the issue does have a milestone matching the specific exempted one'}               | ${true}
            ${true}       | ${''}                             | ${'the PR does not have a milestone'}                                                 | ${true}
            ${true}       | ${'dummy-milestone-not-exempted'} | ${'the PR does have a milestone but not matching the specific issue exempted one'}    | ${true}
            ${true}       | ${'dummy-issue-milestone2'}       | ${'the PR does have a milestone matching the specific issue exempted one'}            | ${true}
            ${true}       | ${'dummy-milestone2'}             | ${'the PR does have a milestone matching the specific exempted one'}                  | ${false}
          `(
            'when $name',
            ({isPullRequest, milestone, shouldStale}: ITestData): void => {
              beforeEach((): void => {
                setTestIssueList(isPullRequest, milestone);
                setProcessor();
              });

              test(`should${
                shouldStale ? '' : ' not'
              } be marked as stale`, async () => {
                expect.assertions(3);

                await processor.processIssues(1);

                expect(processor.staleIssues.length).toStrictEqual(
                  shouldStale ? 1 : 0
                );
                expect(processor.closedIssues.length).toStrictEqual(0);
                expect(processor.removedLabelIssues.length).toStrictEqual(0);
              });
            }
          );
        });

        describe('when all the pull requests milestones should exempt a specific milestone', (): void => {
          beforeEach((): void => {
            opts.exemptPrMilestones =
              'dummy-pull-request-milestone1, dummy-pull-request-milestone2';
          });

          describe.each`
            isPullRequest | milestone                          | name                                                                                         | shouldStale
            ${false}      | ${''}                              | ${'the issue does not have a milestone'}                                                     | ${true}
            ${false}      | ${'dummy-milestone-not-exempted'}  | ${'the issue does have a milestone but not matching the specific pull request exempted one'} | ${true}
            ${false}      | ${'dummy-pull-request-milestone2'} | ${'the issue does have a milestone matching the specific pull request exempted one'}         | ${true}
            ${false}      | ${'dummy-milestone2'}              | ${'the issue does have a milestone matching the specific exempted one'}                      | ${false}
            ${true}       | ${''}                              | ${'the PR does not have a milestone'}                                                        | ${true}
            ${true}       | ${'dummy-milestone-not-exempted'}  | ${'the PR does have a milestone but not matching the specific pull request exempted one'}    | ${true}
            ${true}       | ${'dummy-pull-request-milestone2'} | ${'the PR does have a milestone matching the specific pull request exempted one'}            | ${false}
            ${true}       | ${'dummy-milestone2'}              | ${'the PR does have a milestone matching the specific exempted one'}                         | ${true}
          `(
            'when $name',
            ({isPullRequest, milestone, shouldStale}: ITestData): void => {
              beforeEach((): void => {
                setTestIssueList(isPullRequest, milestone);
                setProcessor();
              });

              test(`should${
                shouldStale ? '' : ' not'
              } be marked as stale`, async () => {
                expect.assertions(3);

                await processor.processIssues(1);

                expect(processor.staleIssues.length).toStrictEqual(
                  shouldStale ? 1 : 0
                );
                expect(processor.closedIssues.length).toStrictEqual(0);
                expect(processor.removedLabelIssues.length).toStrictEqual(0);
              });
            }
          );
        });
      });
    });

    describe('when all the pull requests milestones should exempt', (): void => {
      beforeEach((): void => {
        opts.exemptAllPrMilestones = true;
      });

      describe.each`
        isPullRequest | milestone            | name                                     | shouldStale
        ${false}      | ${''}                | ${'the issue does not have a milestone'} | ${true}
        ${false}      | ${'dummy-milestone'} | ${'the issue does have a milestone'}     | ${true}
        ${true}       | ${''}                | ${'the PR does not have a milestone'}    | ${true}
        ${true}       | ${'dummy-milestone'} | ${'the PR does have a milestone'}        | ${false}
      `(
        'when $name',
        ({isPullRequest, milestone, shouldStale}: ITestData): void => {
          beforeEach((): void => {
            setTestIssueList(isPullRequest, milestone);
            setProcessor();
          });

          test(`should${
            shouldStale ? '' : ' not'
          } be marked as stale`, async () => {
            expect.assertions(3);

            await processor.processIssues(1);

            expect(processor.staleIssues.length).toStrictEqual(
              shouldStale ? 1 : 0
            );
            expect(processor.closedIssues.length).toStrictEqual(0);
            expect(processor.removedLabelIssues.length).toStrictEqual(0);
          });
        }
      );

      describe('when all the issues and pull requests milestones should exempt a specific milestone', (): void => {
        beforeEach((): void => {
          opts.exemptMilestones = 'dummy-milestone';
        });

        describe.each`
          isPullRequest | milestone                         | name                                                                            | shouldStale
          ${false}      | ${''}                             | ${'the issue does not have a milestone'}                                        | ${true}
          ${false}      | ${'dummy-milestone-not-exempted'} | ${'the issue does have a milestone but not matching the specific exempted one'} | ${true}
          ${false}      | ${'dummy-milestone'}              | ${'the issue does have a milestone matching the specific exempted one'}         | ${false}
          ${true}       | ${''}                             | ${'the PR does not have a milestone'}                                           | ${true}
          ${true}       | ${'dummy-milestone-not-exempted'} | ${'the PR does have a milestone but not matching the specific exempted one'}    | ${false}
          ${true}       | ${'dummy-milestone'}              | ${'the PR does have a milestone matching the specific exempted one'}            | ${false}
        `(
          'when $name',
          ({isPullRequest, milestone, shouldStale}: ITestData): void => {
            beforeEach((): void => {
              setTestIssueList(isPullRequest, milestone);
              setProcessor();
            });

            test(`should${
              shouldStale ? '' : ' not'
            } be marked as stale`, async () => {
              expect.assertions(3);

              await processor.processIssues(1);

              expect(processor.staleIssues.length).toStrictEqual(
                shouldStale ? 1 : 0
              );
              expect(processor.closedIssues.length).toStrictEqual(0);
              expect(processor.removedLabelIssues.length).toStrictEqual(0);
            });
          }
        );

        describe('when all the issues milestones should exempt a specific milestone', (): void => {
          beforeEach((): void => {
            opts.exemptIssueMilestones = 'dummy-issue-milestone';
          });

          describe.each`
            isPullRequest | milestone                         | name                                                                                  | shouldStale
            ${false}      | ${''}                             | ${'the issue does not have a milestone'}                                              | ${true}
            ${false}      | ${'dummy-milestone-not-exempted'} | ${'the issue does have a milestone but not matching the specific issue exempted one'} | ${true}
            ${false}      | ${'dummy-issue-milestone'}        | ${'the issue does have a milestone matching the specific issue exempted one'}         | ${false}
            ${false}      | ${'dummy-milestone'}              | ${'the issue does have a milestone matching the specific exempted one'}               | ${true}
            ${true}       | ${''}                             | ${'the PR does not have a milestone'}                                                 | ${true}
            ${true}       | ${'dummy-milestone-not-exempted'} | ${'the PR does have a milestone but not matching the specific issue exempted one'}    | ${false}
            ${true}       | ${'dummy-issue-milestone'}        | ${'the PR does have a milestone matching the specific issue exempted one'}            | ${false}
            ${true}       | ${'dummy-milestone'}              | ${'the PR does have a milestone matching the specific exempted one'}                  | ${false}
          `(
            'when $name',
            ({isPullRequest, milestone, shouldStale}: ITestData): void => {
              beforeEach((): void => {
                setTestIssueList(isPullRequest, milestone);
                setProcessor();
              });

              test(`should${
                shouldStale ? '' : ' not'
              } be marked as stale`, async () => {
                expect.assertions(3);

                await processor.processIssues(1);

                expect(processor.staleIssues.length).toStrictEqual(
                  shouldStale ? 1 : 0
                );
                expect(processor.closedIssues.length).toStrictEqual(0);
                expect(processor.removedLabelIssues.length).toStrictEqual(0);
              });
            }
          );
        });

        describe('when all the pull requests milestones should exempt a specific milestone', (): void => {
          beforeEach((): void => {
            opts.exemptPrMilestones = 'dummy-pull-request-milestone';
          });

          describe.each`
            isPullRequest | milestone                         | name                                                                                         | shouldStale
            ${false}      | ${''}                             | ${'the issue does not have a milestone'}                                                     | ${true}
            ${false}      | ${'dummy-milestone-not-exempted'} | ${'the issue does have a milestone but not matching the specific pull request exempted one'} | ${true}
            ${false}      | ${'dummy-pull-request-milestone'} | ${'the issue does have a milestone matching the specific pull request exempted one'}         | ${true}
            ${false}      | ${'dummy-milestone'}              | ${'the issue does have a milestone matching the specific exempted one'}                      | ${false}
            ${true}       | ${''}                             | ${'the PR does not have a milestone'}                                                        | ${true}
            ${true}       | ${'dummy-milestone-not-exempted'} | ${'the PR does have a milestone but not matching the specific pull request exempted one'}    | ${false}
            ${true}       | ${'dummy-pull-request-milestone'} | ${'the PR does have a milestone matching the specific pull request exempted one'}            | ${false}
            ${true}       | ${'dummy-milestone'}              | ${'the PR does have a milestone matching the specific exempted one'}                         | ${false}
          `(
            'when $name',
            ({isPullRequest, milestone, shouldStale}: ITestData): void => {
              beforeEach((): void => {
                setTestIssueList(isPullRequest, milestone);
                setProcessor();
              });

              test(`should${
                shouldStale ? '' : ' not'
              } be marked as stale`, async () => {
                expect.assertions(3);

                await processor.processIssues(1);

                expect(processor.staleIssues.length).toStrictEqual(
                  shouldStale ? 1 : 0
                );
                expect(processor.closedIssues.length).toStrictEqual(0);
                expect(processor.removedLabelIssues.length).toStrictEqual(0);
              });
            }
          );
        });
      });

      describe('when all the issues and pull requests milestones should exempt some milestones', (): void => {
        beforeEach((): void => {
          opts.exemptMilestones = 'dummy-milestone1, dummy-milestone2';
        });

        describe.each`
          isPullRequest | milestone                         | name                                                                            | shouldStale
          ${false}      | ${''}                             | ${'the issue does not have a milestone'}                                        | ${true}
          ${false}      | ${'dummy-milestone-not-exempted'} | ${'the issue does have a milestone but not matching the specific exempted one'} | ${true}
          ${false}      | ${'dummy-milestone2'}             | ${'the issue does have a milestone matching the specific exempted one'}         | ${false}
          ${true}       | ${''}                             | ${'the PR does not have a milestone'}                                           | ${true}
          ${true}       | ${'dummy-milestone-not-exempted'} | ${'the PR does have a milestone but not matching the specific exempted one'}    | ${false}
          ${true}       | ${'dummy-milestone2'}             | ${'the PR does have a milestone matching the specific exempted one'}            | ${false}
        `(
          'when $name',
          ({isPullRequest, milestone, shouldStale}: ITestData): void => {
            beforeEach((): void => {
              setTestIssueList(isPullRequest, milestone);
              setProcessor();
            });

            test(`should${
              shouldStale ? '' : ' not'
            } be marked as stale`, async () => {
              expect.assertions(3);

              await processor.processIssues(1);

              expect(processor.staleIssues.length).toStrictEqual(
                shouldStale ? 1 : 0
              );
              expect(processor.closedIssues.length).toStrictEqual(0);
              expect(processor.removedLabelIssues.length).toStrictEqual(0);
            });
          }
        );

        describe('when all the issues milestones should exempt a specific milestone', (): void => {
          beforeEach((): void => {
            opts.exemptIssueMilestones =
              'dummy-issue-milestone1, dummy-issue-milestone2';
          });

          describe.each`
            isPullRequest | milestone                         | name                                                                                  | shouldStale
            ${false}      | ${''}                             | ${'the issue does not have a milestone'}                                              | ${true}
            ${false}      | ${'dummy-milestone-not-exempted'} | ${'the issue does have a milestone but not matching the specific issue exempted one'} | ${true}
            ${false}      | ${'dummy-issue-milestone2'}       | ${'the issue does have a milestone matching the specific issue exempted one'}         | ${false}
            ${false}      | ${'dummy-milestone2'}             | ${'the issue does have a milestone matching the specific exempted one'}               | ${true}
            ${true}       | ${''}                             | ${'the PR does not have a milestone'}                                                 | ${true}
            ${true}       | ${'dummy-milestone-not-exempted'} | ${'the PR does have a milestone but not matching the specific issue exempted one'}    | ${false}
            ${true}       | ${'dummy-issue-milestone2'}       | ${'the PR does have a milestone matching the specific issue exempted one'}            | ${false}
            ${true}       | ${'dummy-milestone2'}             | ${'the PR does have a milestone matching the specific exempted one'}                  | ${false}
          `(
            'when $name',
            ({isPullRequest, milestone, shouldStale}: ITestData): void => {
              beforeEach((): void => {
                setTestIssueList(isPullRequest, milestone);
                setProcessor();
              });

              test(`should${
                shouldStale ? '' : ' not'
              } be marked as stale`, async () => {
                expect.assertions(3);

                await processor.processIssues(1);

                expect(processor.staleIssues.length).toStrictEqual(
                  shouldStale ? 1 : 0
                );
                expect(processor.closedIssues.length).toStrictEqual(0);
                expect(processor.removedLabelIssues.length).toStrictEqual(0);
              });
            }
          );
        });

        describe('when all the pull requests milestones should exempt a specific milestone', (): void => {
          beforeEach((): void => {
            opts.exemptPrMilestones =
              'dummy-pull-request-milestone1, dummy-pull-request-milestone2';
          });

          describe.each`
            isPullRequest | milestone                          | name                                                                                         | shouldStale
            ${false}      | ${''}                              | ${'the issue does not have a milestone'}                                                     | ${true}
            ${false}      | ${'dummy-milestone-not-exempted'}  | ${'the issue does have a milestone but not matching the specific pull request exempted one'} | ${true}
            ${false}      | ${'dummy-pull-request-milestone2'} | ${'the issue does have a milestone matching the specific pull request exempted one'}         | ${true}
            ${false}      | ${'dummy-milestone2'}              | ${'the issue does have a milestone matching the specific exempted one'}                      | ${false}
            ${true}       | ${''}                              | ${'the PR does not have a milestone'}                                                        | ${true}
            ${true}       | ${'dummy-milestone-not-exempted'}  | ${'the PR does have a milestone but not matching the specific pull request exempted one'}    | ${false}
            ${true}       | ${'dummy-pull-request-milestone2'} | ${'the PR does have a milestone matching the specific pull request exempted one'}            | ${false}
            ${true}       | ${'dummy-milestone2'}              | ${'the PR does have a milestone matching the specific exempted one'}                         | ${false}
          `(
            'when $name',
            ({isPullRequest, milestone, shouldStale}: ITestData): void => {
              beforeEach((): void => {
                setTestIssueList(isPullRequest, milestone);
                setProcessor();
              });

              test(`should${
                shouldStale ? '' : ' not'
              } be marked as stale`, async () => {
                expect.assertions(3);

                await processor.processIssues(1);

                expect(processor.staleIssues.length).toStrictEqual(
                  shouldStale ? 1 : 0
                );
                expect(processor.closedIssues.length).toStrictEqual(0);
                expect(processor.removedLabelIssues.length).toStrictEqual(0);
              });
            }
          );
        });
      });
    });
  });

  describe('when all the issues and pull requests milestones should exempt', (): void => {
    beforeEach((): void => {
      opts.exemptAllMilestones = true;
    });

    describe.each`
      isPullRequest | milestone            | name                                     | shouldStale
      ${false}      | ${''}                | ${'the issue does not have a milestone'} | ${true}
      ${false}      | ${'dummy-milestone'} | ${'the issue does have a milestone'}     | ${false}
      ${true}       | ${''}                | ${'the PR does not have a milestone'}    | ${true}
      ${true}       | ${'dummy-milestone'} | ${'the PR does have a milestone'}        | ${false}
    `(
      'when $name',
      ({isPullRequest, milestone, shouldStale}: ITestData): void => {
        beforeEach((): void => {
          setTestIssueList(isPullRequest, milestone);
          setProcessor();
        });

        test(`should${
          shouldStale ? '' : ' not'
        } be marked as stale`, async () => {
          expect.assertions(3);

          await processor.processIssues(1);

          expect(processor.staleIssues.length).toStrictEqual(
            shouldStale ? 1 : 0
          );
          expect(processor.closedIssues.length).toStrictEqual(0);
          expect(processor.removedLabelIssues.length).toStrictEqual(0);
        });
      }
    );

    describe('when all the issues milestones are not configured to exempt', (): void => {
      beforeEach((): void => {
        opts.exemptAllIssueMilestones = undefined;
      });

      describe.each`
        isPullRequest | milestone            | name                                     | shouldStale
        ${false}      | ${''}                | ${'the issue does not have a milestone'} | ${true}
        ${false}      | ${'dummy-milestone'} | ${'the issue does have a milestone'}     | ${false}
        ${true}       | ${''}                | ${'the PR does not have a milestone'}    | ${true}
        ${true}       | ${'dummy-milestone'} | ${'the PR does have a milestone'}        | ${false}
      `(
        'when $name',
        ({isPullRequest, milestone, shouldStale}: ITestData): void => {
          beforeEach((): void => {
            setTestIssueList(isPullRequest, milestone);
            setProcessor();
          });

          test(`should${
            shouldStale ? '' : ' not'
          } be marked as stale`, async () => {
            expect.assertions(3);

            await processor.processIssues(1);

            expect(processor.staleIssues.length).toStrictEqual(
              shouldStale ? 1 : 0
            );
            expect(processor.closedIssues.length).toStrictEqual(0);
            expect(processor.removedLabelIssues.length).toStrictEqual(0);
          });
        }
      );

      describe('when all the issues and pull requests milestones should exempt a specific milestone', (): void => {
        beforeEach((): void => {
          opts.exemptMilestones = 'dummy-milestone';
        });

        describe.each`
          isPullRequest | milestone                         | name                                                                            | shouldStale
          ${false}      | ${''}                             | ${'the issue does not have a milestone'}                                        | ${true}
          ${false}      | ${'dummy-milestone-not-exempted'} | ${'the issue does have a milestone but not matching the specific exempted one'} | ${false}
          ${false}      | ${'dummy-milestone'}              | ${'the issue does have a milestone matching the specific exempted one'}         | ${false}
          ${true}       | ${''}                             | ${'the PR does not have a milestone'}                                           | ${true}
          ${true}       | ${'dummy-milestone-not-exempted'} | ${'the PR does have a milestone but not matching the specific exempted one'}    | ${false}
          ${true}       | ${'dummy-milestone'}              | ${'the PR does have a milestone matching the specific exempted one'}            | ${false}
        `(
          'when $name',
          ({isPullRequest, milestone, shouldStale}: ITestData): void => {
            beforeEach((): void => {
              setTestIssueList(isPullRequest, milestone);
              setProcessor();
            });

            test(`should${
              shouldStale ? '' : ' not'
            } be marked as stale`, async () => {
              expect.assertions(3);

              await processor.processIssues(1);

              expect(processor.staleIssues.length).toStrictEqual(
                shouldStale ? 1 : 0
              );
              expect(processor.closedIssues.length).toStrictEqual(0);
              expect(processor.removedLabelIssues.length).toStrictEqual(0);
            });
          }
        );

        describe('when all the issues milestones should exempt a specific milestone', (): void => {
          beforeEach((): void => {
            opts.exemptIssueMilestones = 'dummy-issue-milestone';
          });

          describe.each`
            isPullRequest | milestone                         | name                                                                                  | shouldStale
            ${false}      | ${''}                             | ${'the issue does not have a milestone'}                                              | ${true}
            ${false}      | ${'dummy-milestone-not-exempted'} | ${'the issue does have a milestone but not matching the specific issue exempted one'} | ${false}
            ${false}      | ${'dummy-issue-milestone'}        | ${'the issue does have a milestone matching the specific issue exempted one'}         | ${false}
            ${false}      | ${'dummy-milestone'}              | ${'the issue does have a milestone matching the specific exempted one'}               | ${false}
            ${true}       | ${''}                             | ${'the PR does not have a milestone'}                                                 | ${true}
            ${true}       | ${'dummy-milestone-not-exempted'} | ${'the PR does have a milestone but not matching the specific issue exempted one'}    | ${false}
            ${true}       | ${'dummy-issue-milestone'}        | ${'the PR does have a milestone matching the specific issue exempted one'}            | ${false}
            ${true}       | ${'dummy-milestone'}              | ${'the PR does have a milestone matching the specific exempted one'}                  | ${false}
          `(
            'when $name',
            ({isPullRequest, milestone, shouldStale}: ITestData): void => {
              beforeEach((): void => {
                setTestIssueList(isPullRequest, milestone);
                setProcessor();
              });

              test(`should${
                shouldStale ? '' : ' not'
              } be marked as stale`, async () => {
                expect.assertions(3);

                await processor.processIssues(1);

                expect(processor.staleIssues.length).toStrictEqual(
                  shouldStale ? 1 : 0
                );
                expect(processor.closedIssues.length).toStrictEqual(0);
                expect(processor.removedLabelIssues.length).toStrictEqual(0);
              });
            }
          );
        });

        describe('when all the pull requests milestones should exempt a specific milestone', (): void => {
          beforeEach((): void => {
            opts.exemptPrMilestones = 'dummy-pull-request-milestone';
          });

          describe.each`
            isPullRequest | milestone                         | name                                                                                         | shouldStale
            ${false}      | ${''}                             | ${'the issue does not have a milestone'}                                                     | ${true}
            ${false}      | ${'dummy-milestone-not-exempted'} | ${'the issue does have a milestone but not matching the specific pull request exempted one'} | ${false}
            ${false}      | ${'dummy-pull-request-milestone'} | ${'the issue does have a milestone matching the specific pull request exempted one'}         | ${false}
            ${false}      | ${'dummy-milestone'}              | ${'the issue does have a milestone matching the specific exempted one'}                      | ${false}
            ${true}       | ${''}                             | ${'the PR does not have a milestone'}                                                        | ${true}
            ${true}       | ${'dummy-milestone-not-exempted'} | ${'the PR does have a milestone but not matching the specific pull request exempted one'}    | ${false}
            ${true}       | ${'dummy-pull-request-milestone'} | ${'the PR does have a milestone matching the specific pull request exempted one'}            | ${false}
            ${true}       | ${'dummy-milestone'}              | ${'the PR does have a milestone matching the specific exempted one'}                         | ${false}
          `(
            'when $name',
            ({isPullRequest, milestone, shouldStale}: ITestData): void => {
              beforeEach((): void => {
                setTestIssueList(isPullRequest, milestone);
                setProcessor();
              });

              test(`should${
                shouldStale ? '' : ' not'
              } be marked as stale`, async () => {
                expect.assertions(3);

                await processor.processIssues(1);

                expect(processor.staleIssues.length).toStrictEqual(
                  shouldStale ? 1 : 0
                );
                expect(processor.closedIssues.length).toStrictEqual(0);
                expect(processor.removedLabelIssues.length).toStrictEqual(0);
              });
            }
          );
        });
      });

      describe('when all the issues and pull requests milestones should exempt some milestones', (): void => {
        beforeEach((): void => {
          opts.exemptMilestones = 'dummy-milestone1, dummy-milestone2';
        });

        describe.each`
          isPullRequest | milestone                         | name                                                                            | shouldStale
          ${false}      | ${''}                             | ${'the issue does not have a milestone'}                                        | ${true}
          ${false}      | ${'dummy-milestone-not-exempted'} | ${'the issue does have a milestone but not matching the specific exempted one'} | ${false}
          ${false}      | ${'dummy-milestone2'}             | ${'the issue does have a milestone matching the specific exempted one'}         | ${false}
          ${true}       | ${''}                             | ${'the PR does not have a milestone'}                                           | ${true}
          ${true}       | ${'dummy-milestone-not-exempted'} | ${'the PR does have a milestone but not matching the specific exempted one'}    | ${false}
          ${true}       | ${'dummy-milestone2'}             | ${'the PR does have a milestone matching the specific exempted one'}            | ${false}
        `(
          'when $name',
          ({isPullRequest, milestone, shouldStale}: ITestData): void => {
            beforeEach((): void => {
              setTestIssueList(isPullRequest, milestone);
              setProcessor();
            });

            test(`should${
              shouldStale ? '' : ' not'
            } be marked as stale`, async () => {
              expect.assertions(3);

              await processor.processIssues(1);

              expect(processor.staleIssues.length).toStrictEqual(
                shouldStale ? 1 : 0
              );
              expect(processor.closedIssues.length).toStrictEqual(0);
              expect(processor.removedLabelIssues.length).toStrictEqual(0);
            });
          }
        );

        describe('when all the issues milestones should exempt a specific milestone', (): void => {
          beforeEach((): void => {
            opts.exemptIssueMilestones =
              'dummy-issue-milestone1, dummy-issue-milestone2';
          });

          describe.each`
            isPullRequest | milestone                         | name                                                                                  | shouldStale
            ${false}      | ${''}                             | ${'the issue does not have a milestone'}                                              | ${true}
            ${false}      | ${'dummy-milestone-not-exempted'} | ${'the issue does have a milestone but not matching the specific issue exempted one'} | ${false}
            ${false}      | ${'dummy-issue-milestone2'}       | ${'the issue does have a milestone matching the specific issue exempted one'}         | ${false}
            ${false}      | ${'dummy-milestone2'}             | ${'the issue does have a milestone matching the specific exempted one'}               | ${false}
            ${true}       | ${''}                             | ${'the PR does not have a milestone'}                                                 | ${true}
            ${true}       | ${'dummy-milestone-not-exempted'} | ${'the PR does have a milestone but not matching the specific issue exempted one'}    | ${false}
            ${true}       | ${'dummy-issue-milestone2'}       | ${'the PR does have a milestone matching the specific issue exempted one'}            | ${false}
            ${true}       | ${'dummy-milestone2'}             | ${'the PR does have a milestone matching the specific exempted one'}                  | ${false}
          `(
            'when $name',
            ({isPullRequest, milestone, shouldStale}: ITestData): void => {
              beforeEach((): void => {
                setTestIssueList(isPullRequest, milestone);
                setProcessor();
              });

              test(`should${
                shouldStale ? '' : ' not'
              } be marked as stale`, async () => {
                expect.assertions(3);

                await processor.processIssues(1);

                expect(processor.staleIssues.length).toStrictEqual(
                  shouldStale ? 1 : 0
                );
                expect(processor.closedIssues.length).toStrictEqual(0);
                expect(processor.removedLabelIssues.length).toStrictEqual(0);
              });
            }
          );
        });

        describe('when all the pull requests milestones should exempt a specific milestone', (): void => {
          beforeEach((): void => {
            opts.exemptPrMilestones =
              'dummy-pull-request-milestone1, dummy-pull-request-milestone2';
          });

          describe.each`
            isPullRequest | milestone                          | name                                                                                         | shouldStale
            ${false}      | ${''}                              | ${'the issue does not have a milestone'}                                                     | ${true}
            ${false}      | ${'dummy-milestone-not-exempted'}  | ${'the issue does have a milestone but not matching the specific pull request exempted one'} | ${false}
            ${false}      | ${'dummy-pull-request-milestone2'} | ${'the issue does have a milestone matching the specific pull request exempted one'}         | ${false}
            ${false}      | ${'dummy-milestone2'}              | ${'the issue does have a milestone matching the specific exempted one'}                      | ${false}
            ${true}       | ${''}                              | ${'the PR does not have a milestone'}                                                        | ${true}
            ${true}       | ${'dummy-milestone-not-exempted'}  | ${'the PR does have a milestone but not matching the specific pull request exempted one'}    | ${false}
            ${true}       | ${'dummy-pull-request-milestone2'} | ${'the PR does have a milestone matching the specific pull request exempted one'}            | ${false}
            ${true}       | ${'dummy-milestone2'}              | ${'the PR does have a milestone matching the specific exempted one'}                         | ${false}
          `(
            'when $name',
            ({isPullRequest, milestone, shouldStale}: ITestData): void => {
              beforeEach((): void => {
                setTestIssueList(isPullRequest, milestone);
                setProcessor();
              });

              test(`should${
                shouldStale ? '' : ' not'
              } be marked as stale`, async () => {
                expect.assertions(3);

                await processor.processIssues(1);

                expect(processor.staleIssues.length).toStrictEqual(
                  shouldStale ? 1 : 0
                );
                expect(processor.closedIssues.length).toStrictEqual(0);
                expect(processor.removedLabelIssues.length).toStrictEqual(0);
              });
            }
          );
        });
      });
    });

    describe('when all the issues milestones should not exempt', (): void => {
      beforeEach((): void => {
        opts.exemptAllIssueMilestones = false;
      });

      describe.each`
        isPullRequest | milestone            | name                                     | shouldStale
        ${false}      | ${''}                | ${'the issue does not have a milestone'} | ${true}
        ${false}      | ${'dummy-milestone'} | ${'the issue does have a milestone'}     | ${true}
        ${true}       | ${''}                | ${'the PR does not have a milestone'}    | ${true}
        ${true}       | ${'dummy-milestone'} | ${'the PR does have a milestone'}        | ${false}
      `(
        'when $name',
        ({isPullRequest, milestone, shouldStale}: ITestData): void => {
          beforeEach((): void => {
            setTestIssueList(isPullRequest, milestone);
            setProcessor();
          });

          test(`should${
            shouldStale ? '' : ' not'
          } be marked as stale`, async () => {
            expect.assertions(3);

            await processor.processIssues(1);

            expect(processor.staleIssues.length).toStrictEqual(
              shouldStale ? 1 : 0
            );
            expect(processor.closedIssues.length).toStrictEqual(0);
            expect(processor.removedLabelIssues.length).toStrictEqual(0);
          });
        }
      );

      describe('when all the issues and pull requests milestones should exempt a specific milestone', (): void => {
        beforeEach((): void => {
          opts.exemptMilestones = 'dummy-milestone';
        });

        describe.each`
          isPullRequest | milestone                         | name                                                                            | shouldStale
          ${false}      | ${''}                             | ${'the issue does not have a milestone'}                                        | ${true}
          ${false}      | ${'dummy-milestone-not-exempted'} | ${'the issue does have a milestone but not matching the specific exempted one'} | ${true}
          ${false}      | ${'dummy-milestone'}              | ${'the issue does have a milestone matching the specific exempted one'}         | ${false}
          ${true}       | ${''}                             | ${'the PR does not have a milestone'}                                           | ${true}
          ${true}       | ${'dummy-milestone-not-exempted'} | ${'the PR does have a milestone but not matching the specific exempted one'}    | ${false}
          ${true}       | ${'dummy-milestone'}              | ${'the PR does have a milestone matching the specific exempted one'}            | ${false}
        `(
          'when $name',
          ({isPullRequest, milestone, shouldStale}: ITestData): void => {
            beforeEach((): void => {
              setTestIssueList(isPullRequest, milestone);
              setProcessor();
            });

            test(`should${
              shouldStale ? '' : ' not'
            } be marked as stale`, async () => {
              expect.assertions(3);

              await processor.processIssues(1);

              expect(processor.staleIssues.length).toStrictEqual(
                shouldStale ? 1 : 0
              );
              expect(processor.closedIssues.length).toStrictEqual(0);
              expect(processor.removedLabelIssues.length).toStrictEqual(0);
            });
          }
        );

        describe('when all the issues milestones should exempt a specific milestone', (): void => {
          beforeEach((): void => {
            opts.exemptIssueMilestones = 'dummy-issue-milestone';
          });

          describe.each`
            isPullRequest | milestone                         | name                                                                                  | shouldStale
            ${false}      | ${''}                             | ${'the issue does not have a milestone'}                                              | ${true}
            ${false}      | ${'dummy-milestone-not-exempted'} | ${'the issue does have a milestone but not matching the specific issue exempted one'} | ${true}
            ${false}      | ${'dummy-issue-milestone'}        | ${'the issue does have a milestone matching the specific issue exempted one'}         | ${false}
            ${false}      | ${'dummy-milestone'}              | ${'the issue does have a milestone matching the specific exempted one'}               | ${true}
            ${true}       | ${''}                             | ${'the PR does not have a milestone'}                                                 | ${true}
            ${true}       | ${'dummy-milestone-not-exempted'} | ${'the PR does have a milestone but not matching the specific issue exempted one'}    | ${false}
            ${true}       | ${'dummy-issue-milestone'}        | ${'the PR does have a milestone matching the specific issue exempted one'}            | ${false}
            ${true}       | ${'dummy-milestone'}              | ${'the PR does have a milestone matching the specific exempted one'}                  | ${false}
          `(
            'when $name',
            ({isPullRequest, milestone, shouldStale}: ITestData): void => {
              beforeEach((): void => {
                setTestIssueList(isPullRequest, milestone);
                setProcessor();
              });

              test(`should${
                shouldStale ? '' : ' not'
              } be marked as stale`, async () => {
                expect.assertions(3);

                await processor.processIssues(1);

                expect(processor.staleIssues.length).toStrictEqual(
                  shouldStale ? 1 : 0
                );
                expect(processor.closedIssues.length).toStrictEqual(0);
                expect(processor.removedLabelIssues.length).toStrictEqual(0);
              });
            }
          );
        });

        describe('when all the pull requests milestones should exempt a specific milestone', (): void => {
          beforeEach((): void => {
            opts.exemptPrMilestones = 'dummy-pull-request-milestone';
          });

          describe.each`
            isPullRequest | milestone                         | name                                                                                         | shouldStale
            ${false}      | ${''}                             | ${'the issue does not have a milestone'}                                                     | ${true}
            ${false}      | ${'dummy-milestone-not-exempted'} | ${'the issue does have a milestone but not matching the specific pull request exempted one'} | ${true}
            ${false}      | ${'dummy-pull-request-milestone'} | ${'the issue does have a milestone matching the specific pull request exempted one'}         | ${true}
            ${false}      | ${'dummy-milestone'}              | ${'the issue does have a milestone matching the specific exempted one'}                      | ${false}
            ${true}       | ${''}                             | ${'the PR does not have a milestone'}                                                        | ${true}
            ${true}       | ${'dummy-milestone-not-exempted'} | ${'the PR does have a milestone but not matching the specific pull request exempted one'}    | ${false}
            ${true}       | ${'dummy-pull-request-milestone'} | ${'the PR does have a milestone matching the specific pull request exempted one'}            | ${false}
            ${true}       | ${'dummy-milestone'}              | ${'the PR does have a milestone matching the specific exempted one'}                         | ${false}
          `(
            'when $name',
            ({isPullRequest, milestone, shouldStale}: ITestData): void => {
              beforeEach((): void => {
                setTestIssueList(isPullRequest, milestone);
                setProcessor();
              });

              test(`should${
                shouldStale ? '' : ' not'
              } be marked as stale`, async () => {
                expect.assertions(3);

                await processor.processIssues(1);

                expect(processor.staleIssues.length).toStrictEqual(
                  shouldStale ? 1 : 0
                );
                expect(processor.closedIssues.length).toStrictEqual(0);
                expect(processor.removedLabelIssues.length).toStrictEqual(0);
              });
            }
          );
        });
      });

      describe('when all the issues and pull requests milestones should exempt some milestones', (): void => {
        beforeEach((): void => {
          opts.exemptMilestones = 'dummy-milestone1, dummy-milestone2';
        });

        describe.each`
          isPullRequest | milestone                         | name                                                                            | shouldStale
          ${false}      | ${''}                             | ${'the issue does not have a milestone'}                                        | ${true}
          ${false}      | ${'dummy-milestone-not-exempted'} | ${'the issue does have a milestone but not matching the specific exempted one'} | ${true}
          ${false}      | ${'dummy-milestone2'}             | ${'the issue does have a milestone matching the specific exempted one'}         | ${false}
          ${true}       | ${''}                             | ${'the PR does not have a milestone'}                                           | ${true}
          ${true}       | ${'dummy-milestone-not-exempted'} | ${'the PR does have a milestone but not matching the specific exempted one'}    | ${false}
          ${true}       | ${'dummy-milestone2'}             | ${'the PR does have a milestone matching the specific exempted one'}            | ${false}
        `(
          'when $name',
          ({isPullRequest, milestone, shouldStale}: ITestData): void => {
            beforeEach((): void => {
              setTestIssueList(isPullRequest, milestone);
              setProcessor();
            });

            test(`should${
              shouldStale ? '' : ' not'
            } be marked as stale`, async () => {
              expect.assertions(3);

              await processor.processIssues(1);

              expect(processor.staleIssues.length).toStrictEqual(
                shouldStale ? 1 : 0
              );
              expect(processor.closedIssues.length).toStrictEqual(0);
              expect(processor.removedLabelIssues.length).toStrictEqual(0);
            });
          }
        );

        describe('when all the issues milestones should exempt a specific milestone', (): void => {
          beforeEach((): void => {
            opts.exemptIssueMilestones =
              'dummy-issue-milestone1, dummy-issue-milestone2';
          });

          describe.each`
            isPullRequest | milestone                         | name                                                                                  | shouldStale
            ${false}      | ${''}                             | ${'the issue does not have a milestone'}                                              | ${true}
            ${false}      | ${'dummy-milestone-not-exempted'} | ${'the issue does have a milestone but not matching the specific issue exempted one'} | ${true}
            ${false}      | ${'dummy-issue-milestone2'}       | ${'the issue does have a milestone matching the specific issue exempted one'}         | ${false}
            ${false}      | ${'dummy-milestone2'}             | ${'the issue does have a milestone matching the specific exempted one'}               | ${true}
            ${true}       | ${''}                             | ${'the PR does not have a milestone'}                                                 | ${true}
            ${true}       | ${'dummy-milestone-not-exempted'} | ${'the PR does have a milestone but not matching the specific issue exempted one'}    | ${false}
            ${true}       | ${'dummy-issue-milestone2'}       | ${'the PR does have a milestone matching the specific issue exempted one'}            | ${false}
            ${true}       | ${'dummy-milestone2'}             | ${'the PR does have a milestone matching the specific exempted one'}                  | ${false}
          `(
            'when $name',
            ({isPullRequest, milestone, shouldStale}: ITestData): void => {
              beforeEach((): void => {
                setTestIssueList(isPullRequest, milestone);
                setProcessor();
              });

              test(`should${
                shouldStale ? '' : ' not'
              } be marked as stale`, async () => {
                expect.assertions(3);

                await processor.processIssues(1);

                expect(processor.staleIssues.length).toStrictEqual(
                  shouldStale ? 1 : 0
                );
                expect(processor.closedIssues.length).toStrictEqual(0);
                expect(processor.removedLabelIssues.length).toStrictEqual(0);
              });
            }
          );
        });

        describe('when all the pull requests milestones should exempt a specific milestone', (): void => {
          beforeEach((): void => {
            opts.exemptPrMilestones =
              'dummy-pull-request-milestone1, dummy-pull-request-milestone2';
          });

          describe.each`
            isPullRequest | milestone                          | name                                                                                         | shouldStale
            ${false}      | ${''}                              | ${'the issue does not have a milestone'}                                                     | ${true}
            ${false}      | ${'dummy-milestone-not-exempted'}  | ${'the issue does have a milestone but not matching the specific pull request exempted one'} | ${true}
            ${false}      | ${'dummy-pull-request-milestone2'} | ${'the issue does have a milestone matching the specific pull request exempted one'}         | ${true}
            ${false}      | ${'dummy-milestone2'}              | ${'the issue does have a milestone matching the specific exempted one'}                      | ${false}
            ${true}       | ${''}                              | ${'the PR does not have a milestone'}                                                        | ${true}
            ${true}       | ${'dummy-milestone-not-exempted'}  | ${'the PR does have a milestone but not matching the specific pull request exempted one'}    | ${false}
            ${true}       | ${'dummy-pull-request-milestone2'} | ${'the PR does have a milestone matching the specific pull request exempted one'}            | ${false}
            ${true}       | ${'dummy-milestone2'}              | ${'the PR does have a milestone matching the specific exempted one'}                         | ${false}
          `(
            'when $name',
            ({isPullRequest, milestone, shouldStale}: ITestData): void => {
              beforeEach((): void => {
                setTestIssueList(isPullRequest, milestone);
                setProcessor();
              });

              test(`should${
                shouldStale ? '' : ' not'
              } be marked as stale`, async () => {
                expect.assertions(3);

                await processor.processIssues(1);

                expect(processor.staleIssues.length).toStrictEqual(
                  shouldStale ? 1 : 0
                );
                expect(processor.closedIssues.length).toStrictEqual(0);
                expect(processor.removedLabelIssues.length).toStrictEqual(0);
              });
            }
          );
        });
      });
    });

    describe('when all the issues milestones should exempt', (): void => {
      beforeEach((): void => {
        opts.exemptAllIssueMilestones = true;
      });

      describe.each`
        isPullRequest | milestone            | name                                     | shouldStale
        ${false}      | ${''}                | ${'the issue does not have a milestone'} | ${true}
        ${false}      | ${'dummy-milestone'} | ${'the issue does have a milestone'}     | ${false}
        ${true}       | ${''}                | ${'the PR does not have a milestone'}    | ${true}
        ${true}       | ${'dummy-milestone'} | ${'the PR does have a milestone'}        | ${false}
      `(
        'when $name',
        ({isPullRequest, milestone, shouldStale}: ITestData): void => {
          beforeEach((): void => {
            setTestIssueList(isPullRequest, milestone);
            setProcessor();
          });

          test(`should${
            shouldStale ? '' : ' not'
          } be marked as stale`, async () => {
            expect.assertions(3);

            await processor.processIssues(1);

            expect(processor.staleIssues.length).toStrictEqual(
              shouldStale ? 1 : 0
            );
            expect(processor.closedIssues.length).toStrictEqual(0);
            expect(processor.removedLabelIssues.length).toStrictEqual(0);
          });
        }
      );

      describe('when all the issues and pull requests milestones should exempt a specific milestone', (): void => {
        beforeEach((): void => {
          opts.exemptMilestones = 'dummy-milestone';
        });

        describe.each`
          isPullRequest | milestone                         | name                                                                            | shouldStale
          ${false}      | ${''}                             | ${'the issue does not have a milestone'}                                        | ${true}
          ${false}      | ${'dummy-milestone-not-exempted'} | ${'the issue does have a milestone but not matching the specific exempted one'} | ${false}
          ${false}      | ${'dummy-milestone'}              | ${'the issue does have a milestone matching the specific exempted one'}         | ${false}
          ${true}       | ${''}                             | ${'the PR does not have a milestone'}                                           | ${true}
          ${true}       | ${'dummy-milestone-not-exempted'} | ${'the PR does have a milestone but not matching the specific exempted one'}    | ${false}
          ${true}       | ${'dummy-milestone'}              | ${'the PR does have a milestone matching the specific exempted one'}            | ${false}
        `(
          'when $name',
          ({isPullRequest, milestone, shouldStale}: ITestData): void => {
            beforeEach((): void => {
              setTestIssueList(isPullRequest, milestone);
              setProcessor();
            });

            test(`should${
              shouldStale ? '' : ' not'
            } be marked as stale`, async () => {
              expect.assertions(3);

              await processor.processIssues(1);

              expect(processor.staleIssues.length).toStrictEqual(
                shouldStale ? 1 : 0
              );
              expect(processor.closedIssues.length).toStrictEqual(0);
              expect(processor.removedLabelIssues.length).toStrictEqual(0);
            });
          }
        );

        describe('when all the issues milestones should exempt a specific milestone', (): void => {
          beforeEach((): void => {
            opts.exemptIssueMilestones = 'dummy-issue-milestone';
          });

          describe.each`
            isPullRequest | milestone                         | name                                                                                  | shouldStale
            ${false}      | ${''}                             | ${'the issue does not have a milestone'}                                              | ${true}
            ${false}      | ${'dummy-milestone-not-exempted'} | ${'the issue does have a milestone but not matching the specific issue exempted one'} | ${false}
            ${false}      | ${'dummy-issue-milestone'}        | ${'the issue does have a milestone matching the specific issue exempted one'}         | ${false}
            ${false}      | ${'dummy-milestone'}              | ${'the issue does have a milestone matching the specific exempted one'}               | ${false}
            ${true}       | ${''}                             | ${'the PR does not have a milestone'}                                                 | ${true}
            ${true}       | ${'dummy-milestone-not-exempted'} | ${'the PR does have a milestone but not matching the specific issue exempted one'}    | ${false}
            ${true}       | ${'dummy-issue-milestone'}        | ${'the PR does have a milestone matching the specific issue exempted one'}            | ${false}
            ${true}       | ${'dummy-milestone'}              | ${'the PR does have a milestone matching the specific exempted one'}                  | ${false}
          `(
            'when $name',
            ({isPullRequest, milestone, shouldStale}: ITestData): void => {
              beforeEach((): void => {
                setTestIssueList(isPullRequest, milestone);
                setProcessor();
              });

              test(`should${
                shouldStale ? '' : ' not'
              } be marked as stale`, async () => {
                expect.assertions(3);

                await processor.processIssues(1);

                expect(processor.staleIssues.length).toStrictEqual(
                  shouldStale ? 1 : 0
                );
                expect(processor.closedIssues.length).toStrictEqual(0);
                expect(processor.removedLabelIssues.length).toStrictEqual(0);
              });
            }
          );
        });

        describe('when all the pull requests milestones should exempt a specific milestone', (): void => {
          beforeEach((): void => {
            opts.exemptPrMilestones = 'dummy-pull-request-milestone';
          });

          describe.each`
            isPullRequest | milestone                         | name                                                                                         | shouldStale
            ${false}      | ${''}                             | ${'the issue does not have a milestone'}                                                     | ${true}
            ${false}      | ${'dummy-milestone-not-exempted'} | ${'the issue does have a milestone but not matching the specific pull request exempted one'} | ${false}
            ${false}      | ${'dummy-pull-request-milestone'} | ${'the issue does have a milestone matching the specific pull request exempted one'}         | ${false}
            ${false}      | ${'dummy-milestone'}              | ${'the issue does have a milestone matching the specific exempted one'}                      | ${false}
            ${true}       | ${''}                             | ${'the PR does not have a milestone'}                                                        | ${true}
            ${true}       | ${'dummy-milestone-not-exempted'} | ${'the PR does have a milestone but not matching the specific pull request exempted one'}    | ${false}
            ${true}       | ${'dummy-pull-request-milestone'} | ${'the PR does have a milestone matching the specific pull request exempted one'}            | ${false}
            ${true}       | ${'dummy-milestone'}              | ${'the PR does have a milestone matching the specific exempted one'}                         | ${false}
          `(
            'when $name',
            ({isPullRequest, milestone, shouldStale}: ITestData): void => {
              beforeEach((): void => {
                setTestIssueList(isPullRequest, milestone);
                setProcessor();
              });

              test(`should${
                shouldStale ? '' : ' not'
              } be marked as stale`, async () => {
                expect.assertions(3);

                await processor.processIssues(1);

                expect(processor.staleIssues.length).toStrictEqual(
                  shouldStale ? 1 : 0
                );
                expect(processor.closedIssues.length).toStrictEqual(0);
                expect(processor.removedLabelIssues.length).toStrictEqual(0);
              });
            }
          );
        });
      });

      describe('when all the issues and pull requests milestones should exempt some milestones', (): void => {
        beforeEach((): void => {
          opts.exemptMilestones = 'dummy-milestone1, dummy-milestone2';
        });

        describe.each`
          isPullRequest | milestone                         | name                                                                            | shouldStale
          ${false}      | ${''}                             | ${'the issue does not have a milestone'}                                        | ${true}
          ${false}      | ${'dummy-milestone-not-exempted'} | ${'the issue does have a milestone but not matching the specific exempted one'} | ${false}
          ${false}      | ${'dummy-milestone2'}             | ${'the issue does have a milestone matching the specific exempted one'}         | ${false}
          ${true}       | ${''}                             | ${'the PR does not have a milestone'}                                           | ${true}
          ${true}       | ${'dummy-milestone-not-exempted'} | ${'the PR does have a milestone but not matching the specific exempted one'}    | ${false}
          ${true}       | ${'dummy-milestone2'}             | ${'the PR does have a milestone matching the specific exempted one'}            | ${false}
        `(
          'when $name',
          ({isPullRequest, milestone, shouldStale}: ITestData): void => {
            beforeEach((): void => {
              setTestIssueList(isPullRequest, milestone);
              setProcessor();
            });

            test(`should${
              shouldStale ? '' : ' not'
            } be marked as stale`, async () => {
              expect.assertions(3);

              await processor.processIssues(1);

              expect(processor.staleIssues.length).toStrictEqual(
                shouldStale ? 1 : 0
              );
              expect(processor.closedIssues.length).toStrictEqual(0);
              expect(processor.removedLabelIssues.length).toStrictEqual(0);
            });
          }
        );

        describe('when all the issues milestones should exempt a specific milestone', (): void => {
          beforeEach((): void => {
            opts.exemptIssueMilestones =
              'dummy-issue-milestone1, dummy-issue-milestone2';
          });

          describe.each`
            isPullRequest | milestone                         | name                                                                                  | shouldStale
            ${false}      | ${''}                             | ${'the issue does not have a milestone'}                                              | ${true}
            ${false}      | ${'dummy-milestone-not-exempted'} | ${'the issue does have a milestone but not matching the specific issue exempted one'} | ${false}
            ${false}      | ${'dummy-issue-milestone2'}       | ${'the issue does have a milestone matching the specific issue exempted one'}         | ${false}
            ${false}      | ${'dummy-milestone2'}             | ${'the issue does have a milestone matching the specific exempted one'}               | ${false}
            ${true}       | ${''}                             | ${'the PR does not have a milestone'}                                                 | ${true}
            ${true}       | ${'dummy-milestone-not-exempted'} | ${'the PR does have a milestone but not matching the specific issue exempted one'}    | ${false}
            ${true}       | ${'dummy-issue-milestone2'}       | ${'the PR does have a milestone matching the specific issue exempted one'}            | ${false}
            ${true}       | ${'dummy-milestone2'}             | ${'the PR does have a milestone matching the specific exempted one'}                  | ${false}
          `(
            'when $name',
            ({isPullRequest, milestone, shouldStale}: ITestData): void => {
              beforeEach((): void => {
                setTestIssueList(isPullRequest, milestone);
                setProcessor();
              });

              test(`should${
                shouldStale ? '' : ' not'
              } be marked as stale`, async () => {
                expect.assertions(3);

                await processor.processIssues(1);

                expect(processor.staleIssues.length).toStrictEqual(
                  shouldStale ? 1 : 0
                );
                expect(processor.closedIssues.length).toStrictEqual(0);
                expect(processor.removedLabelIssues.length).toStrictEqual(0);
              });
            }
          );
        });

        describe('when all the pull requests milestones should exempt a specific milestone', (): void => {
          beforeEach((): void => {
            opts.exemptPrMilestones =
              'dummy-pull-request-milestone1, dummy-pull-request-milestone2';
          });

          describe.each`
            isPullRequest | milestone                          | name                                                                                         | shouldStale
            ${false}      | ${''}                              | ${'the issue does not have a milestone'}                                                     | ${true}
            ${false}      | ${'dummy-milestone-not-exempted'}  | ${'the issue does have a milestone but not matching the specific pull request exempted one'} | ${false}
            ${false}      | ${'dummy-pull-request-milestone2'} | ${'the issue does have a milestone matching the specific pull request exempted one'}         | ${false}
            ${false}      | ${'dummy-milestone2'}              | ${'the issue does have a milestone matching the specific exempted one'}                      | ${false}
            ${true}       | ${''}                              | ${'the PR does not have a milestone'}                                                        | ${true}
            ${true}       | ${'dummy-milestone-not-exempted'}  | ${'the PR does have a milestone but not matching the specific pull request exempted one'}    | ${false}
            ${true}       | ${'dummy-pull-request-milestone2'} | ${'the PR does have a milestone matching the specific pull request exempted one'}            | ${false}
            ${true}       | ${'dummy-milestone2'}              | ${'the PR does have a milestone matching the specific exempted one'}                         | ${false}
          `(
            'when $name',
            ({isPullRequest, milestone, shouldStale}: ITestData): void => {
              beforeEach((): void => {
                setTestIssueList(isPullRequest, milestone);
                setProcessor();
              });

              test(`should${
                shouldStale ? '' : ' not'
              } be marked as stale`, async () => {
                expect.assertions(3);

                await processor.processIssues(1);

                expect(processor.staleIssues.length).toStrictEqual(
                  shouldStale ? 1 : 0
                );
                expect(processor.closedIssues.length).toStrictEqual(0);
                expect(processor.removedLabelIssues.length).toStrictEqual(0);
              });
            }
          );
        });
      });
    });

    describe('when all the pull requests milestones are not configured to exempt', (): void => {
      beforeEach((): void => {
        opts.exemptAllPrMilestones = undefined;
      });

      describe.each`
        isPullRequest | milestone            | name                                     | shouldStale
        ${false}      | ${''}                | ${'the issue does not have a milestone'} | ${true}
        ${false}      | ${'dummy-milestone'} | ${'the issue does have a milestone'}     | ${false}
        ${true}       | ${''}                | ${'the PR does not have a milestone'}    | ${true}
        ${true}       | ${'dummy-milestone'} | ${'the PR does have a milestone'}        | ${false}
      `(
        'when $name',
        ({isPullRequest, milestone, shouldStale}: ITestData): void => {
          beforeEach((): void => {
            setTestIssueList(isPullRequest, milestone);
            setProcessor();
          });

          test(`should${
            shouldStale ? '' : ' not'
          } be marked as stale`, async () => {
            expect.assertions(3);

            await processor.processIssues(1);

            expect(processor.staleIssues.length).toStrictEqual(
              shouldStale ? 1 : 0
            );
            expect(processor.closedIssues.length).toStrictEqual(0);
            expect(processor.removedLabelIssues.length).toStrictEqual(0);
          });
        }
      );

      describe('when all the issues and pull requests milestones should exempt a specific milestone', (): void => {
        beforeEach((): void => {
          opts.exemptMilestones = 'dummy-milestone';
        });

        describe.each`
          isPullRequest | milestone                         | name                                                                            | shouldStale
          ${false}      | ${''}                             | ${'the issue does not have a milestone'}                                        | ${true}
          ${false}      | ${'dummy-milestone-not-exempted'} | ${'the issue does have a milestone but not matching the specific exempted one'} | ${false}
          ${false}      | ${'dummy-milestone'}              | ${'the issue does have a milestone matching the specific exempted one'}         | ${false}
          ${true}       | ${''}                             | ${'the PR does not have a milestone'}                                           | ${true}
          ${true}       | ${'dummy-milestone-not-exempted'} | ${'the PR does have a milestone but not matching the specific exempted one'}    | ${false}
          ${true}       | ${'dummy-milestone'}              | ${'the PR does have a milestone matching the specific exempted one'}            | ${false}
        `(
          'when $name',
          ({isPullRequest, milestone, shouldStale}: ITestData): void => {
            beforeEach((): void => {
              setTestIssueList(isPullRequest, milestone);
              setProcessor();
            });

            test(`should${
              shouldStale ? '' : ' not'
            } be marked as stale`, async () => {
              expect.assertions(3);

              await processor.processIssues(1);

              expect(processor.staleIssues.length).toStrictEqual(
                shouldStale ? 1 : 0
              );
              expect(processor.closedIssues.length).toStrictEqual(0);
              expect(processor.removedLabelIssues.length).toStrictEqual(0);
            });
          }
        );

        describe('when all the issues milestones should exempt a specific milestone', (): void => {
          beforeEach((): void => {
            opts.exemptIssueMilestones = 'dummy-issue-milestone';
          });

          describe.each`
            isPullRequest | milestone                         | name                                                                                  | shouldStale
            ${false}      | ${''}                             | ${'the issue does not have a milestone'}                                              | ${true}
            ${false}      | ${'dummy-milestone-not-exempted'} | ${'the issue does have a milestone but not matching the specific issue exempted one'} | ${false}
            ${false}      | ${'dummy-issue-milestone'}        | ${'the issue does have a milestone matching the specific issue exempted one'}         | ${false}
            ${false}      | ${'dummy-milestone'}              | ${'the issue does have a milestone matching the specific exempted one'}               | ${false}
            ${true}       | ${''}                             | ${'the PR does not have a milestone'}                                                 | ${true}
            ${true}       | ${'dummy-milestone-not-exempted'} | ${'the PR does have a milestone but not matching the specific issue exempted one'}    | ${false}
            ${true}       | ${'dummy-issue-milestone'}        | ${'the PR does have a milestone matching the specific issue exempted one'}            | ${false}
            ${true}       | ${'dummy-milestone'}              | ${'the PR does have a milestone matching the specific exempted one'}                  | ${false}
          `(
            'when $name',
            ({isPullRequest, milestone, shouldStale}: ITestData): void => {
              beforeEach((): void => {
                setTestIssueList(isPullRequest, milestone);
                setProcessor();
              });

              test(`should${
                shouldStale ? '' : ' not'
              } be marked as stale`, async () => {
                expect.assertions(3);

                await processor.processIssues(1);

                expect(processor.staleIssues.length).toStrictEqual(
                  shouldStale ? 1 : 0
                );
                expect(processor.closedIssues.length).toStrictEqual(0);
                expect(processor.removedLabelIssues.length).toStrictEqual(0);
              });
            }
          );
        });

        describe('when all the pull requests milestones should exempt a specific milestone', (): void => {
          beforeEach((): void => {
            opts.exemptPrMilestones = 'dummy-pull-request-milestone';
          });

          describe.each`
            isPullRequest | milestone                         | name                                                                                         | shouldStale
            ${false}      | ${''}                             | ${'the issue does not have a milestone'}                                                     | ${true}
            ${false}      | ${'dummy-milestone-not-exempted'} | ${'the issue does have a milestone but not matching the specific pull request exempted one'} | ${false}
            ${false}      | ${'dummy-pull-request-milestone'} | ${'the issue does have a milestone matching the specific pull request exempted one'}         | ${false}
            ${false}      | ${'dummy-milestone'}              | ${'the issue does have a milestone matching the specific exempted one'}                      | ${false}
            ${true}       | ${''}                             | ${'the PR does not have a milestone'}                                                        | ${true}
            ${true}       | ${'dummy-milestone-not-exempted'} | ${'the PR does have a milestone but not matching the specific pull request exempted one'}    | ${false}
            ${true}       | ${'dummy-pull-request-milestone'} | ${'the PR does have a milestone matching the specific pull request exempted one'}            | ${false}
            ${true}       | ${'dummy-milestone'}              | ${'the PR does have a milestone matching the specific exempted one'}                         | ${false}
          `(
            'when $name',
            ({isPullRequest, milestone, shouldStale}: ITestData): void => {
              beforeEach((): void => {
                setTestIssueList(isPullRequest, milestone);
                setProcessor();
              });

              test(`should${
                shouldStale ? '' : ' not'
              } be marked as stale`, async () => {
                expect.assertions(3);

                await processor.processIssues(1);

                expect(processor.staleIssues.length).toStrictEqual(
                  shouldStale ? 1 : 0
                );
                expect(processor.closedIssues.length).toStrictEqual(0);
                expect(processor.removedLabelIssues.length).toStrictEqual(0);
              });
            }
          );
        });
      });

      describe('when all the issues and pull requests milestones should exempt some milestones', (): void => {
        beforeEach((): void => {
          opts.exemptMilestones = 'dummy-milestone1, dummy-milestone2';
        });

        describe.each`
          isPullRequest | milestone                         | name                                                                            | shouldStale
          ${false}      | ${''}                             | ${'the issue does not have a milestone'}                                        | ${true}
          ${false}      | ${'dummy-milestone-not-exempted'} | ${'the issue does have a milestone but not matching the specific exempted one'} | ${false}
          ${false}      | ${'dummy-milestone2'}             | ${'the issue does have a milestone matching the specific exempted one'}         | ${false}
          ${true}       | ${''}                             | ${'the PR does not have a milestone'}                                           | ${true}
          ${true}       | ${'dummy-milestone-not-exempted'} | ${'the PR does have a milestone but not matching the specific exempted one'}    | ${false}
          ${true}       | ${'dummy-milestone2'}             | ${'the PR does have a milestone matching the specific exempted one'}            | ${false}
        `(
          'when $name',
          ({isPullRequest, milestone, shouldStale}: ITestData): void => {
            beforeEach((): void => {
              setTestIssueList(isPullRequest, milestone);
              setProcessor();
            });

            test(`should${
              shouldStale ? '' : ' not'
            } be marked as stale`, async () => {
              expect.assertions(3);

              await processor.processIssues(1);

              expect(processor.staleIssues.length).toStrictEqual(
                shouldStale ? 1 : 0
              );
              expect(processor.closedIssues.length).toStrictEqual(0);
              expect(processor.removedLabelIssues.length).toStrictEqual(0);
            });
          }
        );

        describe('when all the issues milestones should exempt a specific milestone', (): void => {
          beforeEach((): void => {
            opts.exemptIssueMilestones =
              'dummy-issue-milestone1, dummy-issue-milestone2';
          });

          describe.each`
            isPullRequest | milestone                         | name                                                                                  | shouldStale
            ${false}      | ${''}                             | ${'the issue does not have a milestone'}                                              | ${true}
            ${false}      | ${'dummy-milestone-not-exempted'} | ${'the issue does have a milestone but not matching the specific issue exempted one'} | ${false}
            ${false}      | ${'dummy-issue-milestone2'}       | ${'the issue does have a milestone matching the specific issue exempted one'}         | ${false}
            ${false}      | ${'dummy-milestone2'}             | ${'the issue does have a milestone matching the specific exempted one'}               | ${false}
            ${true}       | ${''}                             | ${'the PR does not have a milestone'}                                                 | ${true}
            ${true}       | ${'dummy-milestone-not-exempted'} | ${'the PR does have a milestone but not matching the specific issue exempted one'}    | ${false}
            ${true}       | ${'dummy-issue-milestone2'}       | ${'the PR does have a milestone matching the specific issue exempted one'}            | ${false}
            ${true}       | ${'dummy-milestone2'}             | ${'the PR does have a milestone matching the specific exempted one'}                  | ${false}
          `(
            'when $name',
            ({isPullRequest, milestone, shouldStale}: ITestData): void => {
              beforeEach((): void => {
                setTestIssueList(isPullRequest, milestone);
                setProcessor();
              });

              test(`should${
                shouldStale ? '' : ' not'
              } be marked as stale`, async () => {
                expect.assertions(3);

                await processor.processIssues(1);

                expect(processor.staleIssues.length).toStrictEqual(
                  shouldStale ? 1 : 0
                );
                expect(processor.closedIssues.length).toStrictEqual(0);
                expect(processor.removedLabelIssues.length).toStrictEqual(0);
              });
            }
          );
        });

        describe('when all the pull requests milestones should exempt a specific milestone', (): void => {
          beforeEach((): void => {
            opts.exemptPrMilestones =
              'dummy-pull-request-milestone1, dummy-pull-request-milestone2';
          });

          describe.each`
            isPullRequest | milestone                          | name                                                                                         | shouldStale
            ${false}      | ${''}                              | ${'the issue does not have a milestone'}                                                     | ${true}
            ${false}      | ${'dummy-milestone-not-exempted'}  | ${'the issue does have a milestone but not matching the specific pull request exempted one'} | ${false}
            ${false}      | ${'dummy-pull-request-milestone2'} | ${'the issue does have a milestone matching the specific pull request exempted one'}         | ${false}
            ${false}      | ${'dummy-milestone2'}              | ${'the issue does have a milestone matching the specific exempted one'}                      | ${false}
            ${true}       | ${''}                              | ${'the PR does not have a milestone'}                                                        | ${true}
            ${true}       | ${'dummy-milestone-not-exempted'}  | ${'the PR does have a milestone but not matching the specific pull request exempted one'}    | ${false}
            ${true}       | ${'dummy-pull-request-milestone2'} | ${'the PR does have a milestone matching the specific pull request exempted one'}            | ${false}
            ${true}       | ${'dummy-milestone2'}              | ${'the PR does have a milestone matching the specific exempted one'}                         | ${false}
          `(
            'when $name',
            ({isPullRequest, milestone, shouldStale}: ITestData): void => {
              beforeEach((): void => {
                setTestIssueList(isPullRequest, milestone);
                setProcessor();
              });

              test(`should${
                shouldStale ? '' : ' not'
              } be marked as stale`, async () => {
                expect.assertions(3);

                await processor.processIssues(1);

                expect(processor.staleIssues.length).toStrictEqual(
                  shouldStale ? 1 : 0
                );
                expect(processor.closedIssues.length).toStrictEqual(0);
                expect(processor.removedLabelIssues.length).toStrictEqual(0);
              });
            }
          );
        });
      });
    });

    describe('when all the pull requests milestones should not exempt', (): void => {
      beforeEach((): void => {
        opts.exemptAllPrMilestones = false;
      });

      describe.each`
        isPullRequest | milestone            | name                                     | shouldStale
        ${false}      | ${''}                | ${'the issue does not have a milestone'} | ${true}
        ${false}      | ${'dummy-milestone'} | ${'the issue does have a milestone'}     | ${false}
        ${true}       | ${''}                | ${'the PR does not have a milestone'}    | ${true}
        ${true}       | ${'dummy-milestone'} | ${'the PR does have a milestone'}        | ${true}
      `(
        'when $name',
        ({isPullRequest, milestone, shouldStale}: ITestData): void => {
          beforeEach((): void => {
            setTestIssueList(isPullRequest, milestone);
            setProcessor();
          });

          test(`should${
            shouldStale ? '' : ' not'
          } be marked as stale`, async () => {
            expect.assertions(3);

            await processor.processIssues(1);

            expect(processor.staleIssues.length).toStrictEqual(
              shouldStale ? 1 : 0
            );
            expect(processor.closedIssues.length).toStrictEqual(0);
            expect(processor.removedLabelIssues.length).toStrictEqual(0);
          });
        }
      );

      describe('when all the issues and pull requests milestones should exempt a specific milestone', (): void => {
        beforeEach((): void => {
          opts.exemptMilestones = 'dummy-milestone';
        });

        describe.each`
          isPullRequest | milestone                         | name                                                                            | shouldStale
          ${false}      | ${''}                             | ${'the issue does not have a milestone'}                                        | ${true}
          ${false}      | ${'dummy-milestone-not-exempted'} | ${'the issue does have a milestone but not matching the specific exempted one'} | ${false}
          ${false}      | ${'dummy-milestone'}              | ${'the issue does have a milestone matching the specific exempted one'}         | ${false}
          ${true}       | ${''}                             | ${'the PR does not have a milestone'}                                           | ${true}
          ${true}       | ${'dummy-milestone-not-exempted'} | ${'the PR does have a milestone but not matching the specific exempted one'}    | ${true}
          ${true}       | ${'dummy-milestone'}              | ${'the PR does have a milestone matching the specific exempted one'}            | ${false}
        `(
          'when $name',
          ({isPullRequest, milestone, shouldStale}: ITestData): void => {
            beforeEach((): void => {
              setTestIssueList(isPullRequest, milestone);
              setProcessor();
            });

            test(`should${
              shouldStale ? '' : ' not'
            } be marked as stale`, async () => {
              expect.assertions(3);

              await processor.processIssues(1);

              expect(processor.staleIssues.length).toStrictEqual(
                shouldStale ? 1 : 0
              );
              expect(processor.closedIssues.length).toStrictEqual(0);
              expect(processor.removedLabelIssues.length).toStrictEqual(0);
            });
          }
        );

        describe('when all the issues milestones should exempt a specific milestone', (): void => {
          beforeEach((): void => {
            opts.exemptIssueMilestones = 'dummy-issue-milestone';
          });

          describe.each`
            isPullRequest | milestone                         | name                                                                                  | shouldStale
            ${false}      | ${''}                             | ${'the issue does not have a milestone'}                                              | ${true}
            ${false}      | ${'dummy-milestone-not-exempted'} | ${'the issue does have a milestone but not matching the specific issue exempted one'} | ${false}
            ${false}      | ${'dummy-issue-milestone'}        | ${'the issue does have a milestone matching the specific issue exempted one'}         | ${false}
            ${false}      | ${'dummy-milestone'}              | ${'the issue does have a milestone matching the specific exempted one'}               | ${false}
            ${true}       | ${''}                             | ${'the PR does not have a milestone'}                                                 | ${true}
            ${true}       | ${'dummy-milestone-not-exempted'} | ${'the PR does have a milestone but not matching the specific issue exempted one'}    | ${true}
            ${true}       | ${'dummy-issue-milestone'}        | ${'the PR does have a milestone matching the specific issue exempted one'}            | ${true}
            ${true}       | ${'dummy-milestone'}              | ${'the PR does have a milestone matching the specific exempted one'}                  | ${false}
          `(
            'when $name',
            ({isPullRequest, milestone, shouldStale}: ITestData): void => {
              beforeEach((): void => {
                setTestIssueList(isPullRequest, milestone);
                setProcessor();
              });

              test(`should${
                shouldStale ? '' : ' not'
              } be marked as stale`, async () => {
                expect.assertions(3);

                await processor.processIssues(1);

                expect(processor.staleIssues.length).toStrictEqual(
                  shouldStale ? 1 : 0
                );
                expect(processor.closedIssues.length).toStrictEqual(0);
                expect(processor.removedLabelIssues.length).toStrictEqual(0);
              });
            }
          );
        });

        describe('when all the pull requests milestones should exempt a specific milestone', (): void => {
          beforeEach((): void => {
            opts.exemptPrMilestones = 'dummy-pull-request-milestone';
          });

          describe.each`
            isPullRequest | milestone                         | name                                                                                         | shouldStale
            ${false}      | ${''}                             | ${'the issue does not have a milestone'}                                                     | ${true}
            ${false}      | ${'dummy-milestone-not-exempted'} | ${'the issue does have a milestone but not matching the specific pull request exempted one'} | ${false}
            ${false}      | ${'dummy-pull-request-milestone'} | ${'the issue does have a milestone matching the specific pull request exempted one'}         | ${false}
            ${false}      | ${'dummy-milestone'}              | ${'the issue does have a milestone matching the specific exempted one'}                      | ${false}
            ${true}       | ${''}                             | ${'the PR does not have a milestone'}                                                        | ${true}
            ${true}       | ${'dummy-milestone-not-exempted'} | ${'the PR does have a milestone but not matching the specific pull request exempted one'}    | ${true}
            ${true}       | ${'dummy-pull-request-milestone'} | ${'the PR does have a milestone matching the specific pull request exempted one'}            | ${false}
            ${true}       | ${'dummy-milestone'}              | ${'the PR does have a milestone matching the specific exempted one'}                         | ${true}
          `(
            'when $name',
            ({isPullRequest, milestone, shouldStale}: ITestData): void => {
              beforeEach((): void => {
                setTestIssueList(isPullRequest, milestone);
                setProcessor();
              });

              test(`should${
                shouldStale ? '' : ' not'
              } be marked as stale`, async () => {
                expect.assertions(3);

                await processor.processIssues(1);

                expect(processor.staleIssues.length).toStrictEqual(
                  shouldStale ? 1 : 0
                );
                expect(processor.closedIssues.length).toStrictEqual(0);
                expect(processor.removedLabelIssues.length).toStrictEqual(0);
              });
            }
          );
        });
      });

      describe('when all the issues and pull requests milestones should exempt some milestones', (): void => {
        beforeEach((): void => {
          opts.exemptMilestones = 'dummy-milestone1, dummy-milestone2';
        });

        describe.each`
          isPullRequest | milestone                         | name                                                                            | shouldStale
          ${false}      | ${''}                             | ${'the issue does not have a milestone'}                                        | ${true}
          ${false}      | ${'dummy-milestone-not-exempted'} | ${'the issue does have a milestone but not matching the specific exempted one'} | ${false}
          ${false}      | ${'dummy-milestone2'}             | ${'the issue does have a milestone matching the specific exempted one'}         | ${false}
          ${true}       | ${''}                             | ${'the PR does not have a milestone'}                                           | ${true}
          ${true}       | ${'dummy-milestone-not-exempted'} | ${'the PR does have a milestone but not matching the specific exempted one'}    | ${true}
          ${true}       | ${'dummy-milestone2'}             | ${'the PR does have a milestone matching the specific exempted one'}            | ${false}
        `(
          'when $name',
          ({isPullRequest, milestone, shouldStale}: ITestData): void => {
            beforeEach((): void => {
              setTestIssueList(isPullRequest, milestone);
              setProcessor();
            });

            test(`should${
              shouldStale ? '' : ' not'
            } be marked as stale`, async () => {
              expect.assertions(3);

              await processor.processIssues(1);

              expect(processor.staleIssues.length).toStrictEqual(
                shouldStale ? 1 : 0
              );
              expect(processor.closedIssues.length).toStrictEqual(0);
              expect(processor.removedLabelIssues.length).toStrictEqual(0);
            });
          }
        );

        describe('when all the issues milestones should exempt a specific milestone', (): void => {
          beforeEach((): void => {
            opts.exemptIssueMilestones =
              'dummy-issue-milestone1, dummy-issue-milestone2';
          });

          describe.each`
            isPullRequest | milestone                         | name                                                                                  | shouldStale
            ${false}      | ${''}                             | ${'the issue does not have a milestone'}                                              | ${true}
            ${false}      | ${'dummy-milestone-not-exempted'} | ${'the issue does have a milestone but not matching the specific issue exempted one'} | ${false}
            ${false}      | ${'dummy-issue-milestone2'}       | ${'the issue does have a milestone matching the specific issue exempted one'}         | ${false}
            ${false}      | ${'dummy-milestone2'}             | ${'the issue does have a milestone matching the specific exempted one'}               | ${false}
            ${true}       | ${''}                             | ${'the PR does not have a milestone'}                                                 | ${true}
            ${true}       | ${'dummy-milestone-not-exempted'} | ${'the PR does have a milestone but not matching the specific issue exempted one'}    | ${true}
            ${true}       | ${'dummy-issue-milestone2'}       | ${'the PR does have a milestone matching the specific issue exempted one'}            | ${true}
            ${true}       | ${'dummy-milestone2'}             | ${'the PR does have a milestone matching the specific exempted one'}                  | ${false}
          `(
            'when $name',
            ({isPullRequest, milestone, shouldStale}: ITestData): void => {
              beforeEach((): void => {
                setTestIssueList(isPullRequest, milestone);
                setProcessor();
              });

              test(`should${
                shouldStale ? '' : ' not'
              } be marked as stale`, async () => {
                expect.assertions(3);

                await processor.processIssues(1);

                expect(processor.staleIssues.length).toStrictEqual(
                  shouldStale ? 1 : 0
                );
                expect(processor.closedIssues.length).toStrictEqual(0);
                expect(processor.removedLabelIssues.length).toStrictEqual(0);
              });
            }
          );
        });

        describe('when all the pull requests milestones should exempt a specific milestone', (): void => {
          beforeEach((): void => {
            opts.exemptPrMilestones =
              'dummy-pull-request-milestone1, dummy-pull-request-milestone2';
          });

          describe.each`
            isPullRequest | milestone                          | name                                                                                         | shouldStale
            ${false}      | ${''}                              | ${'the issue does not have a milestone'}                                                     | ${true}
            ${false}      | ${'dummy-milestone-not-exempted'}  | ${'the issue does have a milestone but not matching the specific pull request exempted one'} | ${false}
            ${false}      | ${'dummy-pull-request-milestone2'} | ${'the issue does have a milestone matching the specific pull request exempted one'}         | ${false}
            ${false}      | ${'dummy-milestone2'}              | ${'the issue does have a milestone matching the specific exempted one'}                      | ${false}
            ${true}       | ${''}                              | ${'the PR does not have a milestone'}                                                        | ${true}
            ${true}       | ${'dummy-milestone-not-exempted'}  | ${'the PR does have a milestone but not matching the specific pull request exempted one'}    | ${true}
            ${true}       | ${'dummy-pull-request-milestone2'} | ${'the PR does have a milestone matching the specific pull request exempted one'}            | ${false}
            ${true}       | ${'dummy-milestone2'}              | ${'the PR does have a milestone matching the specific exempted one'}                         | ${true}
          `(
            'when $name',
            ({isPullRequest, milestone, shouldStale}: ITestData): void => {
              beforeEach((): void => {
                setTestIssueList(isPullRequest, milestone);
                setProcessor();
              });

              test(`should${
                shouldStale ? '' : ' not'
              } be marked as stale`, async () => {
                expect.assertions(3);

                await processor.processIssues(1);

                expect(processor.staleIssues.length).toStrictEqual(
                  shouldStale ? 1 : 0
                );
                expect(processor.closedIssues.length).toStrictEqual(0);
                expect(processor.removedLabelIssues.length).toStrictEqual(0);
              });
            }
          );
        });
      });
    });

    describe('when all the pull requests milestones should exempt', (): void => {
      beforeEach((): void => {
        opts.exemptAllPrMilestones = true;
      });

      describe.each`
        isPullRequest | milestone            | name                                     | shouldStale
        ${false}      | ${''}                | ${'the issue does not have a milestone'} | ${true}
        ${false}      | ${'dummy-milestone'} | ${'the issue does have a milestone'}     | ${false}
        ${true}       | ${''}                | ${'the PR does not have a milestone'}    | ${true}
        ${true}       | ${'dummy-milestone'} | ${'the PR does have a milestone'}        | ${false}
      `(
        'when $name',
        ({isPullRequest, milestone, shouldStale}: ITestData): void => {
          beforeEach((): void => {
            setTestIssueList(isPullRequest, milestone);
            setProcessor();
          });

          test(`should${
            shouldStale ? '' : ' not'
          } be marked as stale`, async () => {
            expect.assertions(3);

            await processor.processIssues(1);

            expect(processor.staleIssues.length).toStrictEqual(
              shouldStale ? 1 : 0
            );
            expect(processor.closedIssues.length).toStrictEqual(0);
            expect(processor.removedLabelIssues.length).toStrictEqual(0);
          });
        }
      );

      describe('when all the issues and pull requests milestones should exempt a specific milestone', (): void => {
        beforeEach((): void => {
          opts.exemptMilestones = 'dummy-milestone';
        });

        describe.each`
          isPullRequest | milestone                         | name                                                                            | shouldStale
          ${false}      | ${''}                             | ${'the issue does not have a milestone'}                                        | ${true}
          ${false}      | ${'dummy-milestone-not-exempted'} | ${'the issue does have a milestone but not matching the specific exempted one'} | ${false}
          ${false}      | ${'dummy-milestone'}              | ${'the issue does have a milestone matching the specific exempted one'}         | ${false}
          ${true}       | ${''}                             | ${'the PR does not have a milestone'}                                           | ${true}
          ${true}       | ${'dummy-milestone-not-exempted'} | ${'the PR does have a milestone but not matching the specific exempted one'}    | ${false}
          ${true}       | ${'dummy-milestone'}              | ${'the PR does have a milestone matching the specific exempted one'}            | ${false}
        `(
          'when $name',
          ({isPullRequest, milestone, shouldStale}: ITestData): void => {
            beforeEach((): void => {
              setTestIssueList(isPullRequest, milestone);
              setProcessor();
            });

            test(`should${
              shouldStale ? '' : ' not'
            } be marked as stale`, async () => {
              expect.assertions(3);

              await processor.processIssues(1);

              expect(processor.staleIssues.length).toStrictEqual(
                shouldStale ? 1 : 0
              );
              expect(processor.closedIssues.length).toStrictEqual(0);
              expect(processor.removedLabelIssues.length).toStrictEqual(0);
            });
          }
        );

        describe('when all the issues milestones should exempt a specific milestone', (): void => {
          beforeEach((): void => {
            opts.exemptIssueMilestones = 'dummy-issue-milestone';
          });

          describe.each`
            isPullRequest | milestone                         | name                                                                                  | shouldStale
            ${false}      | ${''}                             | ${'the issue does not have a milestone'}                                              | ${true}
            ${false}      | ${'dummy-milestone-not-exempted'} | ${'the issue does have a milestone but not matching the specific issue exempted one'} | ${false}
            ${false}      | ${'dummy-issue-milestone'}        | ${'the issue does have a milestone matching the specific issue exempted one'}         | ${false}
            ${false}      | ${'dummy-milestone'}              | ${'the issue does have a milestone matching the specific exempted one'}               | ${false}
            ${true}       | ${''}                             | ${'the PR does not have a milestone'}                                                 | ${true}
            ${true}       | ${'dummy-milestone-not-exempted'} | ${'the PR does have a milestone but not matching the specific issue exempted one'}    | ${false}
            ${true}       | ${'dummy-issue-milestone'}        | ${'the PR does have a milestone matching the specific issue exempted one'}            | ${false}
            ${true}       | ${'dummy-milestone'}              | ${'the PR does have a milestone matching the specific exempted one'}                  | ${false}
          `(
            'when $name',
            ({isPullRequest, milestone, shouldStale}: ITestData): void => {
              beforeEach((): void => {
                setTestIssueList(isPullRequest, milestone);
                setProcessor();
              });

              test(`should${
                shouldStale ? '' : ' not'
              } be marked as stale`, async () => {
                expect.assertions(3);

                await processor.processIssues(1);

                expect(processor.staleIssues.length).toStrictEqual(
                  shouldStale ? 1 : 0
                );
                expect(processor.closedIssues.length).toStrictEqual(0);
                expect(processor.removedLabelIssues.length).toStrictEqual(0);
              });
            }
          );
        });

        describe('when all the pull requests milestones should exempt a specific milestone', (): void => {
          beforeEach((): void => {
            opts.exemptPrMilestones = 'dummy-pull-request-milestone';
          });

          describe.each`
            isPullRequest | milestone                         | name                                                                                         | shouldStale
            ${false}      | ${''}                             | ${'the issue does not have a milestone'}                                                     | ${true}
            ${false}      | ${'dummy-milestone-not-exempted'} | ${'the issue does have a milestone but not matching the specific pull request exempted one'} | ${false}
            ${false}      | ${'dummy-pull-request-milestone'} | ${'the issue does have a milestone matching the specific pull request exempted one'}         | ${false}
            ${false}      | ${'dummy-milestone'}              | ${'the issue does have a milestone matching the specific exempted one'}                      | ${false}
            ${true}       | ${''}                             | ${'the PR does not have a milestone'}                                                        | ${true}
            ${true}       | ${'dummy-milestone-not-exempted'} | ${'the PR does have a milestone but not matching the specific pull request exempted one'}    | ${false}
            ${true}       | ${'dummy-pull-request-milestone'} | ${'the PR does have a milestone matching the specific pull request exempted one'}            | ${false}
            ${true}       | ${'dummy-milestone'}              | ${'the PR does have a milestone matching the specific exempted one'}                         | ${false}
          `(
            'when $name',
            ({isPullRequest, milestone, shouldStale}: ITestData): void => {
              beforeEach((): void => {
                setTestIssueList(isPullRequest, milestone);
                setProcessor();
              });

              test(`should${
                shouldStale ? '' : ' not'
              } be marked as stale`, async () => {
                expect.assertions(3);

                await processor.processIssues(1);

                expect(processor.staleIssues.length).toStrictEqual(
                  shouldStale ? 1 : 0
                );
                expect(processor.closedIssues.length).toStrictEqual(0);
                expect(processor.removedLabelIssues.length).toStrictEqual(0);
              });
            }
          );
        });
      });

      describe('when all the issues and pull requests milestones should exempt some milestones', (): void => {
        beforeEach((): void => {
          opts.exemptMilestones = 'dummy-milestone1, dummy-milestone2';
        });

        describe.each`
          isPullRequest | milestone                         | name                                                                            | shouldStale
          ${false}      | ${''}                             | ${'the issue does not have a milestone'}                                        | ${true}
          ${false}      | ${'dummy-milestone-not-exempted'} | ${'the issue does have a milestone but not matching the specific exempted one'} | ${false}
          ${false}      | ${'dummy-milestone2'}             | ${'the issue does have a milestone matching the specific exempted one'}         | ${false}
          ${true}       | ${''}                             | ${'the PR does not have a milestone'}                                           | ${true}
          ${true}       | ${'dummy-milestone-not-exempted'} | ${'the PR does have a milestone but not matching the specific exempted one'}    | ${false}
          ${true}       | ${'dummy-milestone2'}             | ${'the PR does have a milestone matching the specific exempted one'}            | ${false}
        `(
          'when $name',
          ({isPullRequest, milestone, shouldStale}: ITestData): void => {
            beforeEach((): void => {
              setTestIssueList(isPullRequest, milestone);
              setProcessor();
            });

            test(`should${
              shouldStale ? '' : ' not'
            } be marked as stale`, async () => {
              expect.assertions(3);

              await processor.processIssues(1);

              expect(processor.staleIssues.length).toStrictEqual(
                shouldStale ? 1 : 0
              );
              expect(processor.closedIssues.length).toStrictEqual(0);
              expect(processor.removedLabelIssues.length).toStrictEqual(0);
            });
          }
        );

        describe('when all the issues milestones should exempt a specific milestone', (): void => {
          beforeEach((): void => {
            opts.exemptIssueMilestones =
              'dummy-issue-milestone1, dummy-issue-milestone2';
          });

          describe.each`
            isPullRequest | milestone                         | name                                                                                  | shouldStale
            ${false}      | ${''}                             | ${'the issue does not have a milestone'}                                              | ${true}
            ${false}      | ${'dummy-milestone-not-exempted'} | ${'the issue does have a milestone but not matching the specific issue exempted one'} | ${false}
            ${false}      | ${'dummy-issue-milestone2'}       | ${'the issue does have a milestone matching the specific issue exempted one'}         | ${false}
            ${false}      | ${'dummy-milestone2'}             | ${'the issue does have a milestone matching the specific exempted one'}               | ${false}
            ${true}       | ${''}                             | ${'the PR does not have a milestone'}                                                 | ${true}
            ${true}       | ${'dummy-milestone-not-exempted'} | ${'the PR does have a milestone but not matching the specific issue exempted one'}    | ${false}
            ${true}       | ${'dummy-issue-milestone2'}       | ${'the PR does have a milestone matching the specific issue exempted one'}            | ${false}
            ${true}       | ${'dummy-milestone2'}             | ${'the PR does have a milestone matching the specific exempted one'}                  | ${false}
          `(
            'when $name',
            ({isPullRequest, milestone, shouldStale}: ITestData): void => {
              beforeEach((): void => {
                setTestIssueList(isPullRequest, milestone);
                setProcessor();
              });

              test(`should${
                shouldStale ? '' : ' not'
              } be marked as stale`, async () => {
                expect.assertions(3);

                await processor.processIssues(1);

                expect(processor.staleIssues.length).toStrictEqual(
                  shouldStale ? 1 : 0
                );
                expect(processor.closedIssues.length).toStrictEqual(0);
                expect(processor.removedLabelIssues.length).toStrictEqual(0);
              });
            }
          );
        });

        describe('when all the pull requests milestones should exempt a specific milestone', (): void => {
          beforeEach((): void => {
            opts.exemptPrMilestones =
              'dummy-pull-request-milestone1, dummy-pull-request-milestone2';
          });

          describe.each`
            isPullRequest | milestone                          | name                                                                                         | shouldStale
            ${false}      | ${''}                              | ${'the issue does not have a milestone'}                                                     | ${true}
            ${false}      | ${'dummy-milestone-not-exempted'}  | ${'the issue does have a milestone but not matching the specific pull request exempted one'} | ${false}
            ${false}      | ${'dummy-pull-request-milestone2'} | ${'the issue does have a milestone matching the specific pull request exempted one'}         | ${false}
            ${false}      | ${'dummy-milestone2'}              | ${'the issue does have a milestone matching the specific exempted one'}                      | ${false}
            ${true}       | ${''}                              | ${'the PR does not have a milestone'}                                                        | ${true}
            ${true}       | ${'dummy-milestone-not-exempted'}  | ${'the PR does have a milestone but not matching the specific pull request exempted one'}    | ${false}
            ${true}       | ${'dummy-pull-request-milestone2'} | ${'the PR does have a milestone matching the specific pull request exempted one'}            | ${false}
            ${true}       | ${'dummy-milestone2'}              | ${'the PR does have a milestone matching the specific exempted one'}                         | ${false}
          `(
            'when $name',
            ({isPullRequest, milestone, shouldStale}: ITestData): void => {
              beforeEach((): void => {
                setTestIssueList(isPullRequest, milestone);
                setProcessor();
              });

              test(`should${
                shouldStale ? '' : ' not'
              } be marked as stale`, async () => {
                expect.assertions(3);

                await processor.processIssues(1);

                expect(processor.staleIssues.length).toStrictEqual(
                  shouldStale ? 1 : 0
                );
                expect(processor.closedIssues.length).toStrictEqual(0);
                expect(processor.removedLabelIssues.length).toStrictEqual(0);
              });
            }
          );
        });
      });
    });
  });
});
```

## File: `__tests__/only-issue-types.spec.ts`
```typescript
import {Issue} from '../src/classes/issue';
import {IIssuesProcessorOptions} from '../src/interfaces/issues-processor-options';
import {IssuesProcessorMock} from './classes/issues-processor-mock';
import {DefaultProcessorOptions} from './constants/default-processor-options';
import {generateIssue} from './functions/generate-issue';
import {alwaysFalseStateMock} from './classes/state-mock';

describe('only-issue-types option', () => {
  test('should only process issues with allowed type', async () => {
    const opts: IIssuesProcessorOptions = {
      ...DefaultProcessorOptions,
      onlyIssueTypes: 'bug,question'
    };
    const TestIssueList: Issue[] = [
      generateIssue(
        opts,
        1,
        'A bug',
        '2020-01-01T17:00:00Z',
        '2020-01-01T17:00:00Z',
        false,
        false,
        [],
        false,
        false,
        undefined,
        [],
        'bug'
      ),
      generateIssue(
        opts,
        2,
        'A feature',
        '2020-01-01T17:00:00Z',
        '2020-01-01T17:00:00Z',
        false,
        false,
        [],
        false,
        false,
        undefined,
        [],
        'feature'
      ),
      generateIssue(
        opts,
        3,
        'A question',
        '2020-01-01T17:00:00Z',
        '2020-01-01T17:00:00Z',
        false,
        false,
        [],
        false,
        false,
        undefined,
        [],
        'question'
      )
    ];
    const processor = new IssuesProcessorMock(
      opts,
      alwaysFalseStateMock,
      async p => (p === 1 ? TestIssueList : []),
      async () => [],
      async () => new Date().toDateString()
    );
    await processor.processIssues(1);
    expect(processor.staleIssues.map(i => i.title)).toEqual([
      'A bug',
      'A question'
    ]);
  });

  test('should process all issues if onlyIssueTypes is unset', async () => {
    const opts: IIssuesProcessorOptions = {
      ...DefaultProcessorOptions,
      onlyIssueTypes: ''
    };
    const TestIssueList: Issue[] = [
      generateIssue(
        opts,
        1,
        'A bug',
        '2020-01-01T17:00:00Z',
        '2020-01-01T17:00:00Z',
        false,
        false,
        [],
        false,
        false,
        undefined,
        [],
        'bug'
      ),
      generateIssue(
        opts,
        2,
        'A feature',
        '2020-01-01T17:00:00Z',
        '2020-01-01T17:00:00Z',
        false,
        false,
        [],
        false,
        false,
        undefined,
        [],
        'feature'
      )
    ];
    const processor = new IssuesProcessorMock(
      opts,
      alwaysFalseStateMock,
      async p => (p === 1 ? TestIssueList : []),
      async () => [],
      async () => new Date().toDateString()
    );
    await processor.processIssues(1);
    expect(processor.staleIssues.map(i => i.title)).toEqual([
      'A bug',
      'A feature'
    ]);
  });
});
```

## File: `__tests__/only-labels.spec.ts`
```typescript
import {Issue} from '../src/classes/issue';
import {IIssue} from '../src/interfaces/issue';
import {IIssuesProcessorOptions} from '../src/interfaces/issues-processor-options';
import {IssuesProcessorMock} from './classes/issues-processor-mock';
import {DefaultProcessorOptions} from './constants/default-processor-options';
import {generateIssue} from './functions/generate-issue';
import {alwaysFalseStateMock} from './classes/state-mock';

let issuesProcessorBuilder: IssuesProcessorBuilder;
let issuesProcessor: IssuesProcessorMock;

describe('only-labels options', (): void => {
  beforeEach((): void => {
    issuesProcessorBuilder = new IssuesProcessorBuilder();
  });

  test('should stale when not set even if the issue has no label', async (): Promise<void> => {
    expect.assertions(1);
    issuesProcessor = issuesProcessorBuilder
      .emptyOnlyLabels()
      .issuesOrPrs([{labels: []}])
      .build();

    await issuesProcessor.processIssues();

    expect(issuesProcessor.staleIssues).toHaveLength(1);
  });

  test('should stale when not set even if the issue has a label', async (): Promise<void> => {
    expect.assertions(1);
    issuesProcessor = issuesProcessorBuilder
      .emptyOnlyLabels()
      .issuesOrPrs([{labels: [{name: 'label'}]}])
      .build();

    await issuesProcessor.processIssues();

    expect(issuesProcessor.staleIssues).toHaveLength(1);
  });

  test('should not stale when set and the issue has no label', async (): Promise<void> => {
    expect.assertions(1);
    issuesProcessor = issuesProcessorBuilder
      .onlyLabels('dummy-label')
      .issuesOrPrs([{labels: []}])
      .build();

    await issuesProcessor.processIssues();

    expect(issuesProcessor.staleIssues).toHaveLength(0);
  });

  test('should not stale when set and the issue has a different label', async (): Promise<void> => {
    expect.assertions(1);
    issuesProcessor = issuesProcessorBuilder
      .onlyLabels('dummy-label')
      .issuesOrPrs([
        {
          labels: [
            {
              name: 'label'
            }
          ]
        }
      ])
      .build();

    await issuesProcessor.processIssues();

    expect(issuesProcessor.staleIssues).toHaveLength(0);
  });

  test('should not stale when set and the issue has different labels', async (): Promise<void> => {
    expect.assertions(1);
    issuesProcessor = issuesProcessorBuilder
      .onlyLabels('dummy-label')
      .issuesOrPrs([
        {
          labels: [
            {
              name: 'label-1'
            },
            {
              name: 'label-2'
            }
          ]
        }
      ])
      .build();

    await issuesProcessor.processIssues();

    expect(issuesProcessor.staleIssues).toHaveLength(0);
  });

  test('should stale when set and the issue has the same label', async (): Promise<void> => {
    expect.assertions(1);
    issuesProcessor = issuesProcessorBuilder
      .onlyLabels('dummy-label')
      .issuesOrPrs([
        {
          labels: [
            {
              name: 'dummy-label'
            }
          ]
        }
      ])
      .build();

    await issuesProcessor.processIssues();

    expect(issuesProcessor.staleIssues).toHaveLength(1);
  });

  test('should not stale when set and the issue has only one of the same label', async (): Promise<void> => {
    expect.assertions(1);
    issuesProcessor = issuesProcessorBuilder
      .onlyLabels('dummy-label-1,dummy-label-2')
      .issuesOrPrs([
        {
          labels: [
            {
              name: 'dummy-label-1'
            }
          ]
        }
      ])
      .build();

    await issuesProcessor.processIssues();

    expect(issuesProcessor.staleIssues).toHaveLength(0);
  });

  test('should stale when set and the issue has all the same labels', async (): Promise<void> => {
    expect.assertions(1);
    issuesProcessor = issuesProcessorBuilder
      .onlyLabels('dummy-label-1,dummy-label-2')
      .issuesOrPrs([
        {
          labels: [
            {
              name: 'dummy-label-1'
            },
            {
              name: 'dummy-label-2'
            }
          ]
        }
      ])
      .build();

    await issuesProcessor.processIssues();

    expect(issuesProcessor.staleIssues).toHaveLength(1);
  });
});

describe('only-issue-labels option', (): void => {
  beforeEach((): void => {
    issuesProcessorBuilder = new IssuesProcessorBuilder();
  });

  describe('when the only-labels options is not set', (): void => {
    beforeEach((): void => {
      issuesProcessorBuilder.emptyOnlyLabels();
    });

    test('should stale when not set even if the issue has no label', async (): Promise<void> => {
      expect.assertions(1);
      issuesProcessor = issuesProcessorBuilder
        .emptyOnlyIssueLabels()
        .issues([{labels: []}])
        .build();

      await issuesProcessor.processIssues();

      expect(issuesProcessor.staleIssues).toHaveLength(1);
    });

    test('should stale when not set even if the issue has a label', async (): Promise<void> => {
      expect.assertions(1);
      issuesProcessor = issuesProcessorBuilder
        .emptyOnlyIssueLabels()
        .issues([{labels: [{name: 'dummy-label'}]}])
        .build();

      await issuesProcessor.processIssues();

      expect(issuesProcessor.staleIssues).toHaveLength(1);
    });

    test('should not stale when set and the issue has no label', async (): Promise<void> => {
      expect.assertions(1);
      issuesProcessor = issuesProcessorBuilder
        .onlyIssueLabels('dummy-label')
        .issues([{labels: []}])
        .build();

      await issuesProcessor.processIssues();

      expect(issuesProcessor.staleIssues).toHaveLength(0);
    });

    test('should not stale when set and the issue has a different label', async (): Promise<void> => {
      expect.assertions(1);
      issuesProcessor = issuesProcessorBuilder
        .onlyIssueLabels('dummy-label')
        .issues([
          {
            labels: [
              {
                name: 'label'
              }
            ]
          }
        ])
        .build();

      await issuesProcessor.processIssues();

      expect(issuesProcessor.staleIssues).toHaveLength(0);
    });

    test('should not stale when set and the issue has different labels', async (): Promise<void> => {
      expect.assertions(1);
      issuesProcessor = issuesProcessorBuilder
        .onlyIssueLabels('dummy-label')
        .issues([
          {
            labels: [
              {
                name: 'label-1'
              },
              {
                name: 'label-2'
              }
            ]
          }
        ])
        .build();

      await issuesProcessor.processIssues();

      expect(issuesProcessor.staleIssues).toHaveLength(0);
    });

    test('should stale when set and the issue has the same label', async (): Promise<void> => {
      expect.assertions(1);
      issuesProcessor = issuesProcessorBuilder
        .onlyIssueLabels('dummy-label')
        .issues([
          {
            labels: [
              {
                name: 'dummy-label'
              }
            ]
          }
        ])
        .build();

      await issuesProcessor.processIssues();

      expect(issuesProcessor.staleIssues).toHaveLength(1);
    });

    test('should not stale when set and the issue has only one of the same label', async (): Promise<void> => {
      expect.assertions(1);
      issuesProcessor = issuesProcessorBuilder
        .onlyIssueLabels('dummy-label-1,dummy-label-2')
        .issues([
          {
            labels: [
              {
                name: 'dummy-label-1'
              }
            ]
          }
        ])
        .build();

      await issuesProcessor.processIssues();

      expect(issuesProcessor.staleIssues).toHaveLength(0);
    });

    test('should stale when set and the issue has all the same labels', async (): Promise<void> => {
      expect.assertions(1);
      issuesProcessor = issuesProcessorBuilder
        .onlyIssueLabels('dummy-label-1,dummy-label-2')
        .issues([
          {
            labels: [
              {
                name: 'dummy-label-1'
              },
              {
                name: 'dummy-label-2'
              }
            ]
          }
        ])
        .build();

      await issuesProcessor.processIssues();

      expect(issuesProcessor.staleIssues).toHaveLength(1);
    });
  });

  describe('when the only-labels options is set (same as only-issue-labels)', (): void => {
    beforeEach((): void => {
      issuesProcessorBuilder.onlyLabels('dummy-label');
    });

    test('should not stale when not set even if the issue has no label', async (): Promise<void> => {
      expect.assertions(1);
      issuesProcessor = issuesProcessorBuilder
        .emptyOnlyIssueLabels()
        .issues([{labels: []}])
        .build();

      await issuesProcessor.processIssues();

      expect(issuesProcessor.staleIssues).toHaveLength(0);
    });

    test('should not stale when not set even if the issue has a label', async (): Promise<void> => {
      expect.assertions(1);
      issuesProcessor = issuesProcessorBuilder
        .emptyOnlyIssueLabels()
        .issues([{labels: [{name: 'label'}]}])
        .build();

      await issuesProcessor.processIssues();

      expect(issuesProcessor.staleIssues).toHaveLength(0);
    });

    test('should not stale when set and the issue has no label', async (): Promise<void> => {
      expect.assertions(1);
      issuesProcessor = issuesProcessorBuilder
        .onlyIssueLabels('dummy-label')
        .issues([{labels: []}])
        .build();

      await issuesProcessor.processIssues();

      expect(issuesProcessor.staleIssues).toHaveLength(0);
    });

    test('should not stale when set and the issue has a different label', async (): Promise<void> => {
      expect.assertions(1);
      issuesProcessor = issuesProcessorBuilder
        .onlyIssueLabels('dummy-label')
        .issues([
          {
            labels: [
              {
                name: 'label'
              }
            ]
          }
        ])
        .build();

      await issuesProcessor.processIssues();

      expect(issuesProcessor.staleIssues).toHaveLength(0);
    });

    test('should not stale when set and the issue has different labels', async (): Promise<void> => {
      expect.assertions(1);
      issuesProcessor = issuesProcessorBuilder
        .onlyIssueLabels('dummy-label')
        .issues([
          {
            labels: [
              {
                name: 'label-1'
              },
              {
                name: 'label-2'
              }
            ]
          }
        ])
        .build();

      await issuesProcessor.processIssues();

      expect(issuesProcessor.staleIssues).toHaveLength(0);
    });

    test('should stale when set and the issue has the same label', async (): Promise<void> => {
      expect.assertions(1);
      issuesProcessor = issuesProcessorBuilder
        .onlyIssueLabels('dummy-label')
        .issues([
          {
            labels: [
              {
                name: 'dummy-label'
              }
            ]
          }
        ])
        .build();

      await issuesProcessor.processIssues();

      expect(issuesProcessor.staleIssues).toHaveLength(1);
    });

    test('should not stale when set and the issue has only one of the same label', async (): Promise<void> => {
      expect.assertions(1);
      issuesProcessor = issuesProcessorBuilder
        .onlyIssueLabels('dummy-label-1,dummy-label-2')
        .issues([
          {
            labels: [
              {
                name: 'dummy-label-1'
              }
            ]
          }
        ])
        .build();

      await issuesProcessor.processIssues();

      expect(issuesProcessor.staleIssues).toHaveLength(0);
    });

    test('should stale when set and the issue has all the same labels', async (): Promise<void> => {
      expect.assertions(1);
      issuesProcessor = issuesProcessorBuilder
        .onlyIssueLabels('dummy-label-1,dummy-label-2')
        .issues([
          {
            labels: [
              {
                name: 'dummy-label-1'
              },
              {
                name: 'dummy-label-2'
              }
            ]
          }
        ])
        .build();

      await issuesProcessor.processIssues();

      expect(issuesProcessor.staleIssues).toHaveLength(1);
    });
  });

  describe('when the only-labels options is set (different than only-issue-labels)', (): void => {
    beforeEach((): void => {
      issuesProcessorBuilder.onlyLabels('dummy-only-label');
    });

    test('should not stale when not set even if the issue has no label', async (): Promise<void> => {
      expect.assertions(1);
      issuesProcessor = issuesProcessorBuilder
        .emptyOnlyIssueLabels()
        .issues([{labels: []}])
        .build();

      await issuesProcessor.processIssues();

      expect(issuesProcessor.staleIssues).toHaveLength(0);
    });

    test('should not stale when not set even if the issue has a label', async (): Promise<void> => {
      expect.assertions(1);
      issuesProcessor = issuesProcessorBuilder
        .emptyOnlyIssueLabels()
        .issues([{labels: [{name: 'label'}]}])
        .build();

      await issuesProcessor.processIssues();

      expect(issuesProcessor.staleIssues).toHaveLength(0);
    });

    test('should not stale when set and the issue has no label', async (): Promise<void> => {
      expect.assertions(1);
      issuesProcessor = issuesProcessorBuilder
        .onlyIssueLabels('dummy-label')
        .issues([{labels: []}])
        .build();

      await issuesProcessor.processIssues();

      expect(issuesProcessor.staleIssues).toHaveLength(0);
    });

    test('should not stale when set and the issue has a different label', async (): Promise<void> => {
      expect.assertions(1);
      issuesProcessor = issuesProcessorBuilder
        .onlyIssueLabels('dummy-label')
        .issues([
          {
            labels: [
              {
                name: 'label'
              }
            ]
          }
        ])
        .build();

      await issuesProcessor.processIssues();

      expect(issuesProcessor.staleIssues).toHaveLength(0);
    });

    test('should not stale when set and the issue has different labels', async (): Promise<void> => {
      expect.assertions(1);
      issuesProcessor = issuesProcessorBuilder
        .onlyIssueLabels('dummy-label')
        .issues([
          {
            labels: [
              {
                name: 'label-1'
              },
              {
                name: 'label-2'
              }
            ]
          }
        ])
        .build();

      await issuesProcessor.processIssues();

      expect(issuesProcessor.staleIssues).toHaveLength(0);
    });

    test('should stale when set and the issue has the same label', async (): Promise<void> => {
      expect.assertions(1);
      issuesProcessor = issuesProcessorBuilder
        .onlyIssueLabels('dummy-label')
        .issues([
          {
            labels: [
              {
                name: 'dummy-label'
              }
            ]
          }
        ])
        .build();

      await issuesProcessor.processIssues();

      expect(issuesProcessor.staleIssues).toHaveLength(1);
    });

    test('should not stale when set and the issue has only one of the same label', async (): Promise<void> => {
      expect.assertions(1);
      issuesProcessor = issuesProcessorBuilder
        .onlyIssueLabels('dummy-label-1,dummy-label-2')
        .issues([
          {
            labels: [
              {
                name: 'dummy-label-1'
              }
            ]
          }
        ])
        .build();

      await issuesProcessor.processIssues();

      expect(issuesProcessor.staleIssues).toHaveLength(0);
    });

    test('should stale when set and the issue has all the same labels', async (): Promise<void> => {
      expect.assertions(1);
      issuesProcessor = issuesProcessorBuilder
        .onlyIssueLabels('dummy-label-1,dummy-label-2')
        .issues([
          {
            labels: [
              {
                name: 'dummy-label-1'
              },
              {
                name: 'dummy-label-2'
              }
            ]
          }
        ])
        .build();

      await issuesProcessor.processIssues();

      expect(issuesProcessor.staleIssues).toHaveLength(1);
    });
  });
});

describe('only-pr-labels option', (): void => {
  beforeEach((): void => {
    issuesProcessorBuilder = new IssuesProcessorBuilder();
  });

  describe('when the only-labels options is not set', (): void => {
    beforeEach((): void => {
      issuesProcessorBuilder.emptyOnlyLabels();
    });

    test('should stale when not set even if the pr has no label', async (): Promise<void> => {
      expect.assertions(1);
      issuesProcessor = issuesProcessorBuilder
        .emptyOnlyPrLabels()
        .prs([{labels: []}])
        .build();

      await issuesProcessor.processIssues();

      expect(issuesProcessor.staleIssues).toHaveLength(1);
    });

    test('should stale when not set even if the pr has a label', async (): Promise<void> => {
      expect.assertions(1);
      issuesProcessor = issuesProcessorBuilder
        .emptyOnlyPrLabels()
        .prs([{labels: [{name: 'dummy-label'}]}])
        .build();

      await issuesProcessor.processIssues();

      expect(issuesProcessor.staleIssues).toHaveLength(1);
    });

    test('should not stale when set and the pr has no label', async (): Promise<void> => {
      expect.assertions(1);
      issuesProcessor = issuesProcessorBuilder
        .onlyPrLabels('dummy-label')
        .prs([{labels: []}])
        .build();

      await issuesProcessor.processIssues();

      expect(issuesProcessor.staleIssues).toHaveLength(0);
    });

    test('should not stale when set and the pr has a different label', async (): Promise<void> => {
      expect.assertions(1);
      issuesProcessor = issuesProcessorBuilder
        .onlyPrLabels('dummy-label')
        .prs([
          {
            labels: [
              {
                name: 'label'
              }
            ]
          }
        ])
        .build();

      await issuesProcessor.processIssues();

      expect(issuesProcessor.staleIssues).toHaveLength(0);
    });

    test('should not stale when set and the pr has different labels', async (): Promise<void> => {
      expect.assertions(1);
      issuesProcessor = issuesProcessorBuilder
        .onlyPrLabels('dummy-label')
        .prs([
          {
            labels: [
              {
                name: 'label-1'
              },
              {
                name: 'label-2'
              }
            ]
          }
        ])
        .build();

      await issuesProcessor.processIssues();

      expect(issuesProcessor.staleIssues).toHaveLength(0);
    });

    test('should stale when set and the pr has the same label', async (): Promise<void> => {
      expect.assertions(1);
      issuesProcessor = issuesProcessorBuilder
        .onlyPrLabels('dummy-label')
        .prs([
          {
            labels: [
              {
                name: 'dummy-label'
              }
            ]
          }
        ])
        .build();

      await issuesProcessor.processIssues();

      expect(issuesProcessor.staleIssues).toHaveLength(1);
    });

    test('should not stale when set and the pr has only one of the same label', async (): Promise<void> => {
      expect.assertions(1);
      issuesProcessor = issuesProcessorBuilder
        .onlyPrLabels('dummy-label-1,dummy-label-2')
        .prs([
          {
            labels: [
              {
                name: 'dummy-label-1'
              }
            ]
          }
        ])
        .build();

      await issuesProcessor.processIssues();

      expect(issuesProcessor.staleIssues).toHaveLength(0);
    });

    test('should stale when set and the pr has all the same labels', async (): Promise<void> => {
      expect.assertions(1);
      issuesProcessor = issuesProcessorBuilder
        .onlyPrLabels('dummy-label-1,dummy-label-2')
        .prs([
          {
            labels: [
              {
                name: 'dummy-label-1'
              },
              {
                name: 'dummy-label-2'
              }
            ]
          }
        ])
        .build();

      await issuesProcessor.processIssues();

      expect(issuesProcessor.staleIssues).toHaveLength(1);
    });
  });

  describe('when the only-labels options is set (same as only-pr-labels)', (): void => {
    beforeEach((): void => {
      issuesProcessorBuilder.onlyLabels('dummy-label');
    });

    test('should not stale when not set even if the pr has no label', async (): Promise<void> => {
      expect.assertions(1);
      issuesProcessor = issuesProcessorBuilder
        .emptyOnlyPrLabels()
        .prs([{labels: []}])
        .build();

      await issuesProcessor.processIssues();

      expect(issuesProcessor.staleIssues).toHaveLength(0);
    });

    test('should not stale when not set even if the pr has a label', async (): Promise<void> => {
      expect.assertions(1);
      issuesProcessor = issuesProcessorBuilder
        .emptyOnlyPrLabels()
        .prs([{labels: [{name: 'label'}]}])
        .build();

      await issuesProcessor.processIssues();

      expect(issuesProcessor.staleIssues).toHaveLength(0);
    });

    test('should not stale when set and the pr has no label', async (): Promise<void> => {
      expect.assertions(1);
      issuesProcessor = issuesProcessorBuilder
        .onlyPrLabels('dummy-label')
        .prs([{labels: []}])
        .build();

      await issuesProcessor.processIssues();

      expect(issuesProcessor.staleIssues).toHaveLength(0);
    });

    test('should not stale when set and the pr has a different label', async (): Promise<void> => {
      expect.assertions(1);
      issuesProcessor = issuesProcessorBuilder
        .onlyPrLabels('dummy-label')
        .prs([
          {
            labels: [
              {
                name: 'label'
              }
            ]
          }
        ])
        .build();

      await issuesProcessor.processIssues();

      expect(issuesProcessor.staleIssues).toHaveLength(0);
    });

    test('should not stale when set and the pr has different labels', async (): Promise<void> => {
      expect.assertions(1);
      issuesProcessor = issuesProcessorBuilder
        .onlyPrLabels('dummy-label')
        .prs([
          {
            labels: [
              {
                name: 'label-1'
              },
              {
                name: 'label-2'
              }
            ]
          }
        ])
        .build();

      await issuesProcessor.processIssues();

      expect(issuesProcessor.staleIssues).toHaveLength(0);
    });

    test('should stale when set and the pr has the same label', async (): Promise<void> => {
      expect.assertions(1);
      issuesProcessor = issuesProcessorBuilder
        .onlyPrLabels('dummy-label')
        .prs([
          {
            labels: [
              {
                name: 'dummy-label'
              }
            ]
          }
        ])
        .build();

      await issuesProcessor.processIssues();

      expect(issuesProcessor.staleIssues).toHaveLength(1);
    });

    test('should not stale when set and the pr has only one of the same label', async (): Promise<void> => {
      expect.assertions(1);
      issuesProcessor = issuesProcessorBuilder
        .onlyPrLabels('dummy-label-1,dummy-label-2')
        .prs([
          {
            labels: [
              {
                name: 'dummy-label-1'
              }
            ]
          }
        ])
        .build();

      await issuesProcessor.processIssues();

      expect(issuesProcessor.staleIssues).toHaveLength(0);
    });

    test('should stale when set and the pr has all the same labels', async (): Promise<void> => {
      expect.assertions(1);
      issuesProcessor = issuesProcessorBuilder
        .onlyPrLabels('dummy-label-1,dummy-label-2')
        .prs([
          {
            labels: [
              {
                name: 'dummy-label-1'
              },
              {
                name: 'dummy-label-2'
              }
            ]
          }
        ])
        .build();

      await issuesProcessor.processIssues();

      expect(issuesProcessor.staleIssues).toHaveLength(1);
    });
  });

  describe('when the only-labels options is set (different than only-pr-labels)', (): void => {
    beforeEach((): void => {
      issuesProcessorBuilder.onlyLabels('dummy-only-label');
    });

    test('should not stale when not set even if the pr has no label', async (): Promise<void> => {
      expect.assertions(1);
      issuesProcessor = issuesProcessorBuilder
        .emptyOnlyPrLabels()
        .prs([{labels: []}])
        .build();

      await issuesProcessor.processIssues();

      expect(issuesProcessor.staleIssues).toHaveLength(0);
    });

    test('should not stale when not set even if the pr has a label', async (): Promise<void> => {
      expect.assertions(1);
      issuesProcessor = issuesProcessorBuilder
        .emptyOnlyPrLabels()
        .prs([{labels: [{name: 'label'}]}])
        .build();

      await issuesProcessor.processIssues();

      expect(issuesProcessor.staleIssues).toHaveLength(0);
    });

    test('should not stale when set and the pr has no label', async (): Promise<void> => {
      expect.assertions(1);
      issuesProcessor = issuesProcessorBuilder
        .onlyPrLabels('dummy-label')
        .prs([{labels: []}])
        .build();

      await issuesProcessor.processIssues();

      expect(issuesProcessor.staleIssues).toHaveLength(0);
    });

    test('should not stale when set and the pr has a different label', async (): Promise<void> => {
      expect.assertions(1);
      issuesProcessor = issuesProcessorBuilder
        .onlyPrLabels('dummy-label')
        .prs([
          {
            labels: [
              {
                name: 'label'
              }
            ]
          }
        ])
        .build();

      await issuesProcessor.processIssues();

      expect(issuesProcessor.staleIssues).toHaveLength(0);
    });

    test('should not stale when set and the pr has different labels', async (): Promise<void> => {
      expect.assertions(1);
      issuesProcessor = issuesProcessorBuilder
        .onlyPrLabels('dummy-label')
        .prs([
          {
            labels: [
              {
                name: 'label-1'
              },
              {
                name: 'label-2'
              }
            ]
          }
        ])
        .build();

      await issuesProcessor.processIssues();

      expect(issuesProcessor.staleIssues).toHaveLength(0);
    });

    test('should stale when set and the pr has the same label', async (): Promise<void> => {
      expect.assertions(1);
      issuesProcessor = issuesProcessorBuilder
        .onlyPrLabels('dummy-label')
        .prs([
          {
            labels: [
              {
                name: 'dummy-label'
              }
            ]
          }
        ])
        .build();

      await issuesProcessor.processIssues();

      expect(issuesProcessor.staleIssues).toHaveLength(1);
    });

    test('should not stale when set and the pr has only one of the same label', async (): Promise<void> => {
      expect.assertions(1);
      issuesProcessor = issuesProcessorBuilder
        .onlyPrLabels('dummy-label-1,dummy-label-2')
        .prs([
          {
            labels: [
              {
                name: 'dummy-label-1'
              }
            ]
          }
        ])
        .build();

      await issuesProcessor.processIssues();

      expect(issuesProcessor.staleIssues).toHaveLength(0);
    });

    test('should stale when set and the pr has all the same labels', async (): Promise<void> => {
      expect.assertions(1);
      issuesProcessor = issuesProcessorBuilder
        .onlyPrLabels('dummy-label-1,dummy-label-2')
        .prs([
          {
            labels: [
              {
                name: 'dummy-label-1'
              },
              {
                name: 'dummy-label-2'
              }
            ]
          }
        ])
        .build();

      await issuesProcessor.processIssues();

      expect(issuesProcessor.staleIssues).toHaveLength(1);
    });
  });
});

class IssuesProcessorBuilder {
  private _options: IIssuesProcessorOptions = {
    ...DefaultProcessorOptions,
    daysBeforeStale: 0
  };
  private _issues: Issue[] = [];

  onlyLabels(labels: string): IssuesProcessorBuilder {
    this._options.onlyLabels = labels;

    return this;
  }

  onlyIssueLabels(labels: string): IssuesProcessorBuilder {
    this._options.onlyIssueLabels = labels;

    return this;
  }

  onlyPrLabels(labels: string): IssuesProcessorBuilder {
    this._options.onlyPrLabels = labels;

    return this;
  }

  emptyOnlyLabels(): IssuesProcessorBuilder {
    return this.onlyLabels('');
  }

  emptyOnlyIssueLabels(): IssuesProcessorBuilder {
    return this.onlyIssueLabels('');
  }

  emptyOnlyPrLabels(): IssuesProcessorBuilder {
    return this.onlyPrLabels('');
  }

  issuesOrPrs(issues: Partial<IIssue>[]): IssuesProcessorBuilder {
    this._issues = issues.map(
      (issue: Readonly<Partial<IIssue>>, index: Readonly<number>): Issue =>
        generateIssue(
          this._options,
          index,
          issue.title ?? 'dummy-title',
          issue.updated_at ?? new Date().toDateString(),
          issue.created_at ?? new Date().toDateString(),
          false,
          !!issue.pull_request,
          issue.labels ? issue.labels.map(label => label.name || '') : []
        )
    );

    return this;
  }

  issues(issues: Partial<IIssue>[]): IssuesProcessorBuilder {
    this.issuesOrPrs(
      issues.map((issue: Readonly<Partial<IIssue>>): Partial<IIssue> => {
        return {
          ...issue,
          pull_request: null
        };
      })
    );

    return this;
  }

  prs(issues: Partial<IIssue>[]): IssuesProcessorBuilder {
    this.issuesOrPrs(
      issues.map((issue: Readonly<Partial<IIssue>>): Partial<IIssue> => {
        return {
          ...issue,
          pull_request: {key: 'value'}
        };
      })
    );

    return this;
  }

  build(): IssuesProcessorMock {
    return new IssuesProcessorMock(
      this._options,
      alwaysFalseStateMock,
      async p => (p === 1 ? this._issues : []),
      async () => [],
      async () => new Date().toDateString()
    );
  }
}
```

## File: `__tests__/operations-per-run.spec.ts`
```typescript
import {Issue} from '../src/classes/issue';
import {IIssuesProcessorOptions} from '../src/interfaces/issues-processor-options';
import {IsoDateString} from '../src/types/iso-date-string';
import {IssuesProcessorMock} from './classes/issues-processor-mock';
import {DefaultProcessorOptions} from './constants/default-processor-options';
import {generateIssue} from './functions/generate-issue';
import {alwaysFalseStateMock, StateMock} from './classes/state-mock';

describe('operations-per-run option', (): void => {
  let sut: SUT;

  beforeEach((): void => {
    sut = new SUT();
  });

  describe('when one issue should be stale within 10 days and updated 20 days ago', (): void => {
    beforeEach((): void => {
      sut.staleIn(10).newIssue().updated(20);
    });

    describe('when the operations per run option is set to 1', (): void => {
      beforeEach((): void => {
        sut.operationsPerRun(1);
      });

      it('should consume 1 operation (stale label)', async () => {
        expect.assertions(2);

        await sut.test();

        expect(sut.processor.staleIssues).toHaveLength(1);
        expect(
          sut.processor.operations.getConsumedOperationsCount()
        ).toStrictEqual(1);
      });
    });
  });

  describe('when one issue should be stale within 10 days and updated 20 days ago and a comment should be added when stale', (): void => {
    beforeEach((): void => {
      sut.staleIn(10).commentOnStale().newIssue().updated(20);
    });

    describe('when the operations per run option is set to 2', (): void => {
      beforeEach((): void => {
        sut.operationsPerRun(2);
      });

      it('should consume 2 operations (stale label, comment)', async () => {
        expect.assertions(2);

        await sut.test();

        expect(sut.processor.staleIssues).toHaveLength(1);
        expect(
          sut.processor.operations.getConsumedOperationsCount()
        ).toStrictEqual(2);
      });
    });

    // Special case were we continue the issue processing even if the operations per run is reached
    describe('when the operations per run option is set to 1', (): void => {
      beforeEach((): void => {
        sut.operationsPerRun(1);
      });

      it('should consume 2 operations (stale label, comment)', async () => {
        expect.assertions(2);

        await sut.test();

        expect(sut.processor.staleIssues).toHaveLength(1);
        expect(
          sut.processor.operations.getConsumedOperationsCount()
        ).toStrictEqual(2);
      });
    });
  });

  describe('when two issues should be stale within 10 days and updated 20 days ago and a comment should be added when stale', (): void => {
    beforeEach((): void => {
      sut.staleIn(10).commentOnStale();
      sut.newIssue().updated(20);
      sut.newIssue().updated(20);
    });

    describe('when the operations per run option is set to 3', (): void => {
      beforeEach((): void => {
        sut.operationsPerRun(3);
      });

      it('should consume 4 operations (stale label, comment)', async () => {
        expect.assertions(2);

        await sut.test();

        expect(sut.processor.staleIssues).toHaveLength(2);
        expect(
          sut.processor.operations.getConsumedOperationsCount()
        ).toStrictEqual(4);
      });
    });

    describe('when the operations per run option is set to 2', (): void => {
      beforeEach((): void => {
        sut.operationsPerRun(2);
      });

      it('should consume 2 operations (stale label, comment) and stop', async () => {
        expect.assertions(2);

        await sut.test();

        expect(sut.processor.staleIssues).toHaveLength(1);
        expect(
          sut.processor.operations.getConsumedOperationsCount()
        ).toStrictEqual(2);
      });
    });

    // Special case were we continue the issue processing even if the operations per run is reached
    describe('when the operations per run option is set to 1', (): void => {
      beforeEach((): void => {
        sut.operationsPerRun(1);
      });

      it('should consume 2 operations (stale label, comment) and stop', async () => {
        expect.assertions(2);

        await sut.test();

        expect(sut.processor.staleIssues).toHaveLength(1);
        expect(
          sut.processor.operations.getConsumedOperationsCount()
        ).toStrictEqual(2);
      });
    });
  });
});

class SUT {
  processor!: IssuesProcessorMock;
  private _opts: IIssuesProcessorOptions = {
    ...DefaultProcessorOptions,
    staleIssueMessage: ''
  };
  private _testIssueList: Issue[] = [];
  private _sutIssues: SUTIssue[] = [];

  newIssue(): SUTIssue {
    const sutIssue: SUTIssue = new SUTIssue();
    this._sutIssues.push(sutIssue);

    return sutIssue;
  }

  staleIn(days: number): SUT {
    this._updateOptions({
      daysBeforeIssueStale: days
    });

    return this;
  }

  commentOnStale(): SUT {
    this._updateOptions({
      staleIssueMessage: 'Dummy stale issue message'
    });

    return this;
  }

  operationsPerRun(count: number): SUT {
    this._updateOptions({
      operationsPerRun: count
    });

    return this;
  }

  async test(): Promise<number> {
    return this._setTestIssueList()._setProcessor();
  }

  private _updateOptions(opts: Partial<IIssuesProcessorOptions>): SUT {
    this._opts = {...this._opts, ...opts};

    return this;
  }

  private _setTestIssueList(): SUT {
    this._testIssueList = this._sutIssues.map((sutIssue: SUTIssue): Issue => {
      return generateIssue(
        this._opts,
        1,
        'My first issue',
        sutIssue.updatedAt,
        sutIssue.updatedAt,
        false
      );
    });

    return this;
  }

  private async _setProcessor(): Promise<number> {
    this.processor = new IssuesProcessorMock(
      this._opts,
      alwaysFalseStateMock,
      async p => (p === 1 ? this._testIssueList : []),
      async () => [],
      async () => new Date().toDateString()
    );

    return this.processor.processIssues(1);
  }
}

class SUTIssue {
  updatedAt: IsoDateString = '2020-01-01T17:00:00Z';

  updated(daysAgo: number): SUTIssue {
    const today = new Date();
    today.setDate(today.getDate() - daysAgo);
    this.updatedAt = today.toISOString();

    return this;
  }
}
```

## File: `__tests__/remove-stale-when-updated-label-events.spec.ts`
```typescript
import {Issue} from '../src/classes/issue';
import {IIssuesProcessorOptions} from '../src/interfaces/issues-processor-options';
import {IssuesProcessorMock} from './classes/issues-processor-mock';
import {DefaultProcessorOptions} from './constants/default-processor-options';
import {generateIssue} from './functions/generate-issue';
import {alwaysFalseStateMock} from './classes/state-mock';
import {IState} from '../src/interfaces/state/state';
import {IIssueEvent} from '../src/interfaces/issue-event';
import {IssuesProcessor} from '../src/classes/issues-processor';

describe('remove-stale-when-updated with stale label events', (): void => {
  const markedStaleOn = '2025-01-01T00:00:00Z';
  const updatedAt = '2025-01-01T00:01:00Z';

  let options: IIssuesProcessorOptions;

  beforeEach((): void => {
    options = {
      ...DefaultProcessorOptions,
      removeStaleWhenUpdated: true
    };
  });

  const buildIssue = (): Issue =>
    generateIssue(
      options,
      1,
      'dummy-title',
      updatedAt,
      markedStaleOn,
      false,
      false,
      ['Stale']
    );

  const buildEvents = (): IIssueEvent[] => [
    {
      event: 'labeled',
      created_at: markedStaleOn,
      label: {name: 'Stale'}
    }
  ];

  test('does not remove stale label when only stale label events occurred', async (): Promise<void> => {
    expect.assertions(1);
    const issue = buildIssue();

    const processor = new IssuesProcessorMock(
      options,
      alwaysFalseStateMock,
      async p => (p === 1 ? [issue] : []),
      async () => [],
      async () => ({creationDate: markedStaleOn, events: buildEvents()}),
      async () => true
    );

    await processor.processIssues();

    expect(processor.removedLabelIssues).toHaveLength(0);
  });

  test('removes stale label when updates are not just stale label events', async (): Promise<void> => {
    expect.assertions(1);
    const issue = buildIssue();

    const processor = new IssuesProcessorMock(
      options,
      alwaysFalseStateMock,
      async p => (p === 1 ? [issue] : []),
      async () => [],
      async () => ({creationDate: markedStaleOn, events: buildEvents()}),
      async () => false
    );

    await processor.processIssues();

    expect(processor.removedLabelIssues).toHaveLength(1);
  });
});

class TestIssuesProcessor extends IssuesProcessor {
  constructor(
    options: IIssuesProcessorOptions,
    state: IState,
    events: IIssueEvent[]
  ) {
    super(options, state);
    const client = {
      rest: {
        issues: {
          listEvents: {
            endpoint: {
              merge: () => ({})
            }
          }
        }
      },
      paginate: {
        iterator: async function* () {
          yield {data: events};
        }
      }
    };
    (this as any).client = client;
  }

  async callhasOnlyStaleLabelingEventsSince(
    issue: Issue,
    sinceDate: string,
    staleLabel: string,
    events: IIssueEvent[]
  ): Promise<boolean> {
    return this.hasOnlyStaleLabelingEventsSince(
      issue,
      sinceDate,
      staleLabel,
      events
    );
  }
}

describe('hasOnlyStaleLabelingEventsSince', (): void => {
  const staleLabel = 'Stale';
  const sinceDate = '2025-01-01T00:00:00Z';
  const originalRepo = process.env.GITHUB_REPOSITORY;

  let options: IIssuesProcessorOptions;

  beforeEach((): void => {
    process.env.GITHUB_REPOSITORY = 'owner/repo';
    options = {
      ...DefaultProcessorOptions,
      staleIssueLabel: staleLabel,
      removeStaleWhenUpdated: true
    };
  });

  afterEach((): void => {
    if (originalRepo === undefined) {
      delete process.env.GITHUB_REPOSITORY;
    } else {
      process.env.GITHUB_REPOSITORY = originalRepo;
    }
  });

  const buildIssue = (): Issue =>
    generateIssue(
      options,
      1,
      'dummy-title',
      '2025-01-01T00:02:00Z',
      sinceDate,
      false,
      false,
      [staleLabel]
    );

  test('returns true when only stale label events exist after the since date', async (): Promise<void> => {
    expect.assertions(1);
    const issue = buildIssue();
    const events: IIssueEvent[] = [
      // Event before the sinceDate should be ignored.
      {
        event: 'labeled',
        created_at: '2024-12-31T23:59:00Z',
        label: {name: staleLabel}
      },
      {
        event: 'labeled',
        created_at: '2025-01-01T00:00:10Z',
        label: {name: staleLabel}
      }
    ];
    const processor = new TestIssuesProcessor(
      options,
      alwaysFalseStateMock,
      events
    );
    const result = await processor.callhasOnlyStaleLabelingEventsSince(
      issue,
      sinceDate,
      staleLabel,
      events
    );

    expect(result).toBe(true);
  });

  test('returns false when a non-stale label event exists after the since date', async (): Promise<void> => {
    expect.assertions(1);
    const issue = buildIssue();
    const events: IIssueEvent[] = [
      {
        event: 'labeled',
        created_at: '2025-01-01T00:00:10Z',
        label: {name: 'other-label'}
      }
    ];
    const processor = new TestIssuesProcessor(
      options,
      alwaysFalseStateMock,
      events
    );
    const result = await processor.callhasOnlyStaleLabelingEventsSince(
      issue,
      sinceDate,
      staleLabel,
      events
    );

    expect(result).toBe(false);
  });

  test('returns false when stale label is removed after the since date', async (): Promise<void> => {
    expect.assertions(1);
    const issue = buildIssue();
    const events: IIssueEvent[] = [
      {
        event: 'unlabeled',
        created_at: '2025-01-01T00:00:10Z',
        label: {name: staleLabel}
      }
    ];
    const processor = new TestIssuesProcessor(
      options,
      alwaysFalseStateMock,
      events
    );
    const result = await processor.callhasOnlyStaleLabelingEventsSince(
      issue,
      sinceDate,
      staleLabel,
      events
    );

    expect(result).toBe(false);
  });

  test('returns false when a non-label event exists after the since date', async (): Promise<void> => {
    expect.assertions(1);
    const issue = buildIssue();
    const events: IIssueEvent[] = [
      {
        event: 'commented',
        created_at: '2025-01-01T00:00:10Z',
        label: {name: staleLabel}
      }
    ];
    const processor = new TestIssuesProcessor(
      options,
      alwaysFalseStateMock,
      events
    );
    const result = await processor.callhasOnlyStaleLabelingEventsSince(
      issue,
      sinceDate,
      staleLabel,
      events
    );

    expect(result).toBe(false);
  });

  test('includes events that occur exactly at the since date boundary', async (): Promise<void> => {
    expect.assertions(1);
    const issue = buildIssue();
    const events: IIssueEvent[] = [
      {
        event: 'labeled',
        created_at: sinceDate,
        label: {name: staleLabel}
      }
    ];
    const processor = new TestIssuesProcessor(
      options,
      alwaysFalseStateMock,
      events
    );
    const result = await processor.callhasOnlyStaleLabelingEventsSince(
      issue,
      sinceDate,
      staleLabel,
      events
    );

    expect(result).toBe(true);
  });
});
```

## File: `__tests__/remove-stale-when-updated.spec.ts`
```typescript
import {Issue} from '../src/classes/issue';
import {IIssue} from '../src/interfaces/issue';
import {IIssuesProcessorOptions} from '../src/interfaces/issues-processor-options';
import {ILabel} from '../src/interfaces/label';
import {IssuesProcessorMock} from './classes/issues-processor-mock';
import {DefaultProcessorOptions} from './constants/default-processor-options';
import {generateIssue} from './functions/generate-issue';
import {alwaysFalseStateMock} from './classes/state-mock';

let issuesProcessorBuilder: IssuesProcessorBuilder;
let issuesProcessor: IssuesProcessorMock;

/**
 * @description
 * Assuming there is a comment on the issue
 */
describe('remove-stale-when-updated option', (): void => {
  beforeEach((): void => {
    issuesProcessorBuilder = new IssuesProcessorBuilder();
  });

  describe('when the option "remove-stale-when-updated" is disabled', (): void => {
    beforeEach((): void => {
      issuesProcessorBuilder.keepStaleWhenUpdated();
    });

    test('should not remove the stale label on the issue', async (): Promise<void> => {
      expect.assertions(1);
      issuesProcessor = issuesProcessorBuilder.staleIssues([{}]).build();

      await issuesProcessor.processIssues();

      expect(issuesProcessor.removedLabelIssues).toHaveLength(0);
    });

    test('should not remove the stale label on the pull request', async (): Promise<void> => {
      expect.assertions(1);
      issuesProcessor = issuesProcessorBuilder.stalePrs([{}]).build();

      await issuesProcessor.processIssues();

      expect(issuesProcessor.removedLabelIssues).toHaveLength(0);
    });
  });

  describe('when the option "remove-stale-when-updated" is enabled', (): void => {
    beforeEach((): void => {
      issuesProcessorBuilder.removeStaleWhenUpdated();
    });

    test('should remove the stale label on the issue', async (): Promise<void> => {
      expect.assertions(1);
      issuesProcessor = issuesProcessorBuilder.staleIssues([{}]).build();

      await issuesProcessor.processIssues();

      expect(issuesProcessor.removedLabelIssues).toHaveLength(1);
    });

    test('should remove the stale label on the pull request', async (): Promise<void> => {
      expect.assertions(1);
      issuesProcessor = issuesProcessorBuilder.stalePrs([{}]).build();

      await issuesProcessor.processIssues();

      expect(issuesProcessor.removedLabelIssues).toHaveLength(1);
    });
  });
});

describe('remove-issue-stale-when-updated option', (): void => {
  beforeEach((): void => {
    issuesProcessorBuilder = new IssuesProcessorBuilder();
  });

  describe('when the option "remove-stale-when-updated" is disabled', (): void => {
    beforeEach((): void => {
      issuesProcessorBuilder.keepStaleWhenUpdated();
    });

    describe('when the option "remove-issue-stale-when-updated" is unset', (): void => {
      beforeEach((): void => {
        issuesProcessorBuilder.unsetIssueStaleWhenUpdated();
      });

      test('should not remove the stale label on the issue', async (): Promise<void> => {
        expect.assertions(1);
        issuesProcessor = issuesProcessorBuilder.staleIssues([{}]).build();

        await issuesProcessor.processIssues();

        expect(issuesProcessor.removedLabelIssues).toHaveLength(0);
      });

      test('should not remove the stale label on the pull request', async (): Promise<void> => {
        expect.assertions(1);
        issuesProcessor = issuesProcessorBuilder.stalePrs([{}]).build();

        await issuesProcessor.processIssues();

        expect(issuesProcessor.removedLabelIssues).toHaveLength(0);
      });
    });

    describe('when the option "remove-issue-stale-when-updated" is disabled', (): void => {
      beforeEach((): void => {
        issuesProcessorBuilder.keepIssueStaleWhenUpdated();
      });

      test('should not remove the stale label on the issue', async (): Promise<void> => {
        expect.assertions(1);
        issuesProcessor = issuesProcessorBuilder.staleIssues([{}]).build();

        await issuesProcessor.processIssues();

        expect(issuesProcessor.removedLabelIssues).toHaveLength(0);
      });

      test('should not remove the stale label on the pull request', async (): Promise<void> => {
        expect.assertions(1);
        issuesProcessor = issuesProcessorBuilder.stalePrs([{}]).build();

        await issuesProcessor.processIssues();

        expect(issuesProcessor.removedLabelIssues).toHaveLength(0);
      });
    });

    describe('when the option "remove-issue-stale-when-updated" is enabled', (): void => {
      beforeEach((): void => {
        issuesProcessorBuilder.removeIssueStaleWhenUpdated();
      });

      test('should remove the stale label on the issue', async (): Promise<void> => {
        expect.assertions(1);
        issuesProcessor = issuesProcessorBuilder.staleIssues([{}]).build();

        await issuesProcessor.processIssues();

        expect(issuesProcessor.removedLabelIssues).toHaveLength(1);
      });

      test('should not remove the stale label on the pull request', async (): Promise<void> => {
        expect.assertions(1);
        issuesProcessor = issuesProcessorBuilder
          .stalePrs([{draft: true}])
          .build();

        await issuesProcessor.processIssues();

        expect(issuesProcessor.removedLabelIssues).toHaveLength(0);
      });
    });
  });

  describe('when the option "remove-stale-when-updated" is enabled', (): void => {
    beforeEach((): void => {
      issuesProcessorBuilder.removeStaleWhenUpdated();
    });

    describe('when the option "remove-issue-stale-when-updated" is unset', (): void => {
      beforeEach((): void => {
        issuesProcessorBuilder.unsetIssueStaleWhenUpdated();
      });

      test('should remove the stale label on the issue', async (): Promise<void> => {
        expect.assertions(1);
        issuesProcessor = issuesProcessorBuilder.staleIssues([{}]).build();

        await issuesProcessor.processIssues();

        expect(issuesProcessor.removedLabelIssues).toHaveLength(1);
      });

      test('should remove the stale label on the pull request', async (): Promise<void> => {
        expect.assertions(1);
        issuesProcessor = issuesProcessorBuilder.stalePrs([{}]).build();

        await issuesProcessor.processIssues();

        expect(issuesProcessor.removedLabelIssues).toHaveLength(1);
      });
    });

    describe('when the option "remove-issue-stale-when-updated" is disabled', (): void => {
      beforeEach((): void => {
        issuesProcessorBuilder.keepIssueStaleWhenUpdated();
      });

      test('should not remove the stale label on the issue', async (): Promise<void> => {
        expect.assertions(1);
        issuesProcessor = issuesProcessorBuilder.staleIssues([{}]).build();

        await issuesProcessor.processIssues();

        expect(issuesProcessor.removedLabelIssues).toHaveLength(0);
      });

      test('should remove the stale label on the pull request', async (): Promise<void> => {
        expect.assertions(1);
        issuesProcessor = issuesProcessorBuilder.stalePrs([{}]).build();

        await issuesProcessor.processIssues();

        expect(issuesProcessor.removedLabelIssues).toHaveLength(1);
      });
    });

    describe('when the option "remove-issue-stale-when-updated" is enabled', (): void => {
      beforeEach((): void => {
        issuesProcessorBuilder.removeIssueStaleWhenUpdated();
      });

      test('should remove the stale label on the issue', async (): Promise<void> => {
        expect.assertions(1);
        issuesProcessor = issuesProcessorBuilder.staleIssues([{}]).build();

        await issuesProcessor.processIssues();

        expect(issuesProcessor.removedLabelIssues).toHaveLength(1);
      });

      test('should remove the stale label on the pull request', async (): Promise<void> => {
        expect.assertions(1);
        issuesProcessor = issuesProcessorBuilder.stalePrs([{}]).build();

        await issuesProcessor.processIssues();

        expect(issuesProcessor.removedLabelIssues).toHaveLength(1);
      });
    });
  });
});

describe('remove-pr-stale-when-updated option', (): void => {
  beforeEach((): void => {
    issuesProcessorBuilder = new IssuesProcessorBuilder();
  });

  describe('when the option "remove-stale-when-updated" is disabled', (): void => {
    beforeEach((): void => {
      issuesProcessorBuilder.keepStaleWhenUpdated();
    });

    describe('when the option "remove-pr-stale-when-updated" is unset', (): void => {
      beforeEach((): void => {
        issuesProcessorBuilder.unsetPrStaleWhenUpdated();
      });

      test('should not remove the stale label on the issue', async (): Promise<void> => {
        expect.assertions(1);
        issuesProcessor = issuesProcessorBuilder.staleIssues([{}]).build();

        await issuesProcessor.processIssues();

        expect(issuesProcessor.removedLabelIssues).toHaveLength(0);
      });

      test('should not remove the stale label on the pull request', async (): Promise<void> => {
        expect.assertions(1);
        issuesProcessor = issuesProcessorBuilder.stalePrs([{}]).build();

        await issuesProcessor.processIssues();

        expect(issuesProcessor.removedLabelIssues).toHaveLength(0);
      });
    });

    describe('when the option "remove-pr-stale-when-updated" is disabled', (): void => {
      beforeEach((): void => {
        issuesProcessorBuilder.keepPrStaleWhenUpdated();
      });

      test('should not remove the stale label on the issue', async (): Promise<void> => {
        expect.assertions(1);
        issuesProcessor = issuesProcessorBuilder.staleIssues([{}]).build();

        await issuesProcessor.processIssues();

        expect(issuesProcessor.removedLabelIssues).toHaveLength(0);
      });

      test('should not remove the stale label on the pull request', async (): Promise<void> => {
        expect.assertions(1);
        issuesProcessor = issuesProcessorBuilder.stalePrs([{}]).build();

        await issuesProcessor.processIssues();

        expect(issuesProcessor.removedLabelIssues).toHaveLength(0);
      });
    });

    describe('when the option "remove-pr-stale-when-updated" is enabled', (): void => {
      beforeEach((): void => {
        issuesProcessorBuilder.removePrStaleWhenUpdated();
      });

      test('should not remove the stale label on the issue', async (): Promise<void> => {
        expect.assertions(1);
        issuesProcessor = issuesProcessorBuilder.staleIssues([{}]).build();

        await issuesProcessor.processIssues();

        expect(issuesProcessor.removedLabelIssues).toHaveLength(0);
      });

      test('should remove the stale label on the pull request', async (): Promise<void> => {
        expect.assertions(1);
        issuesProcessor = issuesProcessorBuilder.stalePrs([{}]).build();

        await issuesProcessor.processIssues();

        expect(issuesProcessor.removedLabelIssues).toHaveLength(1);
      });
    });
  });

  describe('when the option "remove-stale-when-updated" is enabled', (): void => {
    beforeEach((): void => {
      issuesProcessorBuilder.removeStaleWhenUpdated();
    });

    describe('when the option "remove-pr-stale-when-updated" is unset', (): void => {
      beforeEach((): void => {
        issuesProcessorBuilder.unsetPrStaleWhenUpdated();
      });

      test('should remove the stale label on the issue', async (): Promise<void> => {
        expect.assertions(1);
        issuesProcessor = issuesProcessorBuilder.staleIssues([{}]).build();

        await issuesProcessor.processIssues();

        expect(issuesProcessor.removedLabelIssues).toHaveLength(1);
      });

      test('should remove the stale label on the pull request', async (): Promise<void> => {
        expect.assertions(1);
        issuesProcessor = issuesProcessorBuilder.stalePrs([{}]).build();

        await issuesProcessor.processIssues();

        expect(issuesProcessor.removedLabelIssues).toHaveLength(1);
      });
    });

    describe('when the option "remove-pr-stale-when-updated" is disabled', (): void => {
      beforeEach((): void => {
        issuesProcessorBuilder.keepPrStaleWhenUpdated();
      });

      test('should remove the stale label on the issue', async (): Promise<void> => {
        expect.assertions(1);
        issuesProcessor = issuesProcessorBuilder.staleIssues([{}]).build();

        await issuesProcessor.processIssues();

        expect(issuesProcessor.removedLabelIssues).toHaveLength(1);
      });

      test('should not remove the stale label on the pull request', async (): Promise<void> => {
        expect.assertions(1);
        issuesProcessor = issuesProcessorBuilder.stalePrs([{}]).build();

        await issuesProcessor.processIssues();

        expect(issuesProcessor.removedLabelIssues).toHaveLength(0);
      });
    });

    describe('when the option "remove-pr-stale-when-updated" is enabled', (): void => {
      beforeEach((): void => {
        issuesProcessorBuilder.removePrStaleWhenUpdated();
      });

      test('should remove the stale label on the issue', async (): Promise<void> => {
        expect.assertions(1);
        issuesProcessor = issuesProcessorBuilder.staleIssues([{}]).build();

        await issuesProcessor.processIssues();

        expect(issuesProcessor.removedLabelIssues).toHaveLength(1);
      });

      test('should remove the stale label on the pull request', async (): Promise<void> => {
        expect.assertions(1);
        issuesProcessor = issuesProcessorBuilder.stalePrs([{}]).build();

        await issuesProcessor.processIssues();

        expect(issuesProcessor.removedLabelIssues).toHaveLength(1);
      });
    });
  });
});

class IssuesProcessorBuilder {
  private _options: IIssuesProcessorOptions = {
    ...DefaultProcessorOptions
  };
  private _issues: Issue[] = [];

  keepStaleWhenUpdated(): IssuesProcessorBuilder {
    this._options.removeStaleWhenUpdated = false;

    return this;
  }

  removeStaleWhenUpdated(): IssuesProcessorBuilder {
    this._options.removeStaleWhenUpdated = true;

    return this;
  }

  unsetIssueStaleWhenUpdated(): IssuesProcessorBuilder {
    delete this._options.removeIssueStaleWhenUpdated;

    return this;
  }

  keepIssueStaleWhenUpdated(): IssuesProcessorBuilder {
    this._options.removeIssueStaleWhenUpdated = false;

    return this;
  }

  removeIssueStaleWhenUpdated(): IssuesProcessorBuilder {
    this._options.removeIssueStaleWhenUpdated = true;

    return this;
  }

  unsetPrStaleWhenUpdated(): IssuesProcessorBuilder {
    delete this._options.removePrStaleWhenUpdated;

    return this;
  }

  keepPrStaleWhenUpdated(): IssuesProcessorBuilder {
    this._options.removePrStaleWhenUpdated = false;

    return this;
  }

  removePrStaleWhenUpdated(): IssuesProcessorBuilder {
    this._options.removePrStaleWhenUpdated = true;

    return this;
  }

  issuesOrPrs(issues: Partial<IIssue>[]): IssuesProcessorBuilder {
    this._issues = issues.map(
      (issue: Readonly<Partial<IIssue>>, index: Readonly<number>): Issue =>
        generateIssue(
          this._options,
          index,
          issue.title ?? 'dummy-title',
          issue.updated_at ?? new Date().toDateString(),
          issue.created_at ?? new Date().toDateString(),
          !!issue.draft,
          !!issue.pull_request,
          issue.labels ? issue.labels.map(label => label.name || '') : []
        )
    );

    return this;
  }

  issues(issues: Partial<IIssue>[]): IssuesProcessorBuilder {
    this.issuesOrPrs(
      issues.map((issue: Readonly<Partial<IIssue>>): Partial<IIssue> => {
        return {
          ...issue,
          pull_request: null
        };
      })
    );

    return this;
  }

  staleIssues(issues: Partial<IIssue>[]): IssuesProcessorBuilder {
    this.issues(
      issues.map((issue: Readonly<Partial<IIssue>>): Partial<IIssue> => {
        return {
          ...issue,
          updated_at: '2020-01-01T17:00:00Z',
          created_at: '2020-01-01T17:00:00Z',
          labels: issue.labels?.map((label: Readonly<ILabel>): ILabel => {
            return {
              ...label,
              name: 'Stale'
            };
          }) ?? [
            {
              name: 'Stale'
            }
          ]
        };
      })
    );

    return this;
  }

  prs(issues: Partial<IIssue>[]): IssuesProcessorBuilder {
    this.issuesOrPrs(
      issues.map((issue: Readonly<Partial<IIssue>>): Partial<IIssue> => {
        return {
          ...issue,
          pull_request: {key: 'value'}
        };
      })
    );

    return this;
  }

  stalePrs(issues: Partial<IIssue>[]): IssuesProcessorBuilder {
    this.prs(
      issues.map((issue: Readonly<Partial<IIssue>>): Partial<IIssue> => {
        const o = {
          ...issue,
          updated_at: '2020-01-01T17:00:00Z',
          created_at: '2020-01-01T17:00:00Z',
          labels: issue.labels?.map((label: Readonly<ILabel>): ILabel => {
            return {
              ...label,
              name: 'Stale'
            };
          }) ?? [
            {
              name: 'Stale'
            }
          ]
        };
        return o;
      })
    );

    return this;
  }

  build(): IssuesProcessorMock {
    return new IssuesProcessorMock(
      this._options,
      alwaysFalseStateMock,
      async p => (p === 1 ? this._issues : []),
      async () => [
        {
          user: {
            login: 'notme',
            type: 'User'
          },
          body: 'body'
        }
      ],
      async () => new Date().toDateString()
    );
  }
}
```

## File: `__tests__/state.spec.ts`
```typescript
import {IStateStorage} from '../src/interfaces/state/state-storage';
import {IIssuesProcessorOptions} from '../src/interfaces/issues-processor-options';
import {DefaultProcessorOptions} from './constants/default-processor-options';
import {Issue} from '../src/classes/issue';
import {generateIssue} from './functions/generate-issue';
import {IssuesProcessorMock} from './classes/issues-processor-mock';
import {IssueID, State} from '../src/classes/state/state';
import {IState} from '../src/interfaces/state/state';
import * as core from '@actions/core';

const stateStorage: IStateStorage = {
  restore(): Promise<string> {
    return Promise.resolve('');
  },
  save(serializedState: string): Promise<void> {
    return Promise.resolve();
  }
};

const getProcessedIssuesIDs = (state: IState): Set<IssueID> =>
  (state as unknown as {processedIssuesIDs: Set<IssueID>}).processedIssuesIDs;

describe('state', (): void => {
  let debugSpy: jest.SpyInstance;
  let infoSpy: jest.SpyInstance;
  let warningSpy: jest.SpyInstance;
  beforeEach(() => {
    debugSpy = jest.spyOn(core, 'debug');
    infoSpy = jest.spyOn(core, 'info');
    warningSpy = jest.spyOn(core, 'warning');
  });

  afterEach(() => {
    jest.resetAllMocks();
    jest.clearAllMocks();
  });

  it('rehydrate/persist should not be called during processing', async () => {
    const opts: IIssuesProcessorOptions = {
      ...DefaultProcessorOptions,
      daysBeforeClose: 0
    };
    const TestIssueList: Issue[] = [
      generateIssue(opts, 1, 'An issue with no label', '2020-01-01T17:00:00Z')
    ];
    const state = new State(stateStorage, opts);
    const restoreSpy = jest.spyOn(stateStorage, 'restore');
    const saveSpy = jest.spyOn(stateStorage, 'save');
    const processor = new IssuesProcessorMock(
      opts,
      state,
      async p => (p === 1 ? TestIssueList : []),
      async () => [],
      async () => new Date().toDateString()
    );

    await processor.processIssues(1);
    expect(restoreSpy).toHaveBeenCalledTimes(0);
    expect(saveSpy).toHaveBeenCalledTimes(0);
  });

  it('state should be marked with the processed issue', async () => {
    const opts: IIssuesProcessorOptions = {
      ...DefaultProcessorOptions,
      daysBeforeClose: 0
    };
    const testIssue1 = generateIssue(
      opts,
      1,
      'An issue with no label',
      '2020-01-01T17:00:00Z'
    );
    const TestIssueList: Issue[] = [testIssue1];
    const state = new State(stateStorage, opts);
    const addIssueToProcessedSpy = jest.spyOn(state, 'addIssueToProcessed');
    const processor = new IssuesProcessorMock(
      opts,
      state,
      async p => (p === 1 ? TestIssueList : []),
      async () => [],
      async () => new Date().toDateString()
    );

    await processor.processIssues(1);
    expect(addIssueToProcessedSpy).toHaveBeenCalledTimes(1);
    expect(addIssueToProcessedSpy).toHaveBeenCalledWith(testIssue1);

    expect(debugSpy).toHaveBeenCalledWith('state: reset');
    expect(debugSpy).toHaveBeenCalledWith('state: mark 1 as processed');
  });

  it('issueProcessor should skip the issue marked as proceeded', async () => {
    const opts: IIssuesProcessorOptions = {
      ...DefaultProcessorOptions,
      daysBeforeClose: 0
    };
    const testIssue1 = generateIssue(
      opts,
      1,
      'An issue with no label',
      '2020-01-01T17:00:00Z'
    );
    const testIssue2 = generateIssue(
      opts,
      2,
      'An issue with no label',
      '2020-01-01T17:00:00Z'
    );
    const TestIssueList: Issue[] = [testIssue1, testIssue2];
    const state = new State(stateStorage, opts);
    state.addIssueToProcessed(testIssue1);
    debugSpy.mockClear();
    const addIssueToProcessedSpy = jest.spyOn(state, 'addIssueToProcessed');
    const isIssueProcessedSpy = jest.spyOn(state, 'isIssueProcessed');
    const processor = new IssuesProcessorMock(
      opts,
      state,
      async p => (p === 1 ? TestIssueList : []),
      async () => [],
      async () => new Date().toDateString()
    );

    await processor.processIssues(1);
    expect(addIssueToProcessedSpy).toHaveBeenCalledTimes(1);
    expect(addIssueToProcessedSpy).toHaveBeenCalledWith(testIssue2);
    expect(isIssueProcessedSpy).toHaveBeenCalledTimes(2);
    expect(isIssueProcessedSpy).toHaveBeenCalledWith(testIssue1);
    expect(isIssueProcessedSpy).toHaveBeenCalledWith(testIssue2);
    expect(processor.staleIssues.length).toStrictEqual(1);
    expect(processor.closedIssues.length).toStrictEqual(1);

    expect(debugSpy).toHaveBeenCalledWith('state: reset');
    expect(debugSpy).toHaveBeenCalledWith('state: mark 2 as processed');
  });

  it('state should not be reset if not all issues are proceeded', async () => {
    const opts: IIssuesProcessorOptions = {
      ...DefaultProcessorOptions,
      operationsPerRun: 1,
      daysBeforeClose: 0
    };
    const testIssue1 = generateIssue(
      opts,
      1,
      'An issue with no label',
      '2020-01-01T17:00:00Z'
    );
    const testIssue2 = generateIssue(
      opts,
      2,
      'An issue with no label',
      '2020-01-01T17:00:00Z'
    );
    const TestIssueList: Issue[] = [testIssue1, testIssue2];
    const state = new State(stateStorage, opts);
    const resetSpy = jest.spyOn(state, 'reset');
    const processor = new IssuesProcessorMock(
      opts,
      state,
      async p => (p === 1 ? TestIssueList : []),
      async () => [],
      async () => new Date().toDateString()
    );

    await processor.processIssues(1);
    // make sure not all issues are proceeded
    expect(warningSpy.mock.calls[2][0]).toContain(
      'No more operations left! Exiting...'
    );

    expect(resetSpy).toHaveBeenCalledTimes(0);
    expect(debugSpy).toHaveBeenCalledWith('state: mark 1 as processed');
  });

  it('state should be reset if all issues are proceeded', async () => {
    const opts: IIssuesProcessorOptions = {
      ...DefaultProcessorOptions,
      daysBeforeClose: 0
    };
    const testIssue1 = generateIssue(
      opts,
      1,
      'An issue with no label',
      '2020-01-01T17:00:00Z'
    );
    const testIssue2 = generateIssue(
      opts,
      2,
      'An issue with no label',
      '2020-01-01T17:00:00Z'
    );
    const TestIssueList: Issue[] = [testIssue1, testIssue2];
    const state = new State(stateStorage, opts);
    const resetSpy = jest.spyOn(state, 'reset');
    const processor = new IssuesProcessorMock(
      opts,
      state,
      async p => (p === 1 ? TestIssueList : []),
      async () => [],
      async () => new Date().toDateString()
    );

    await processor.processIssues(1);
    // make sure all issues are proceeded
    expect(infoSpy.mock.calls[71][0]).toContain(
      'No more issues found to process. Exiting...'
    );

    expect(resetSpy).toHaveBeenCalledTimes(1);
    expect(debugSpy).toHaveBeenCalledWith('state: mark 1 as processed');
    expect(debugSpy).toHaveBeenCalledWith('state: mark 2 as processed');
  });
});
```

## File: `__tests__/updates-reset-stale.spec.ts`
```typescript
import {Issue} from '../src/classes/issue';
import {IIssuesProcessorOptions} from '../src/interfaces/issues-processor-options';
import {IsoDateString} from '../src/types/iso-date-string';
import {IssuesProcessorMock} from './classes/issues-processor-mock';
import {DefaultProcessorOptions} from './constants/default-processor-options';
import {generateIssue} from './functions/generate-issue';
import {alwaysFalseStateMock} from './classes/state-mock';

describe('ignore-updates options', (): void => {
  let sut: SUT;

  beforeEach((): void => {
    sut = new SUT();
  });

  describe('when the issue should be stale within 10 days and was created 20 days ago and updated 5 days ago', (): void => {
    beforeEach((): void => {
      sut.toIssue().staleIn(10).created(20).updated(5);
    });

    describe('when the ignore updates option is disabled', (): void => {
      beforeEach((): void => {
        sut.staleOnUpdates();
      });

      it('should not stale the issue', async () => {
        expect.assertions(3);

        await sut.test();

        expect(sut.processor.staleIssues).toHaveLength(0);
        expect(sut.processor.closedIssues).toHaveLength(0);
        expect(sut.processor.removedLabelIssues).toHaveLength(0);
      });

      describe('when the ignore issue updates option is enabled', (): void => {
        beforeEach((): void => {
          sut.ignoreIssueUpdates();
        });

        it('should stale the issue', async () => {
          expect.assertions(3);

          await sut.test();

          expect(sut.processor.staleIssues).toHaveLength(1);
          expect(sut.processor.closedIssues).toHaveLength(0);
          expect(sut.processor.removedLabelIssues).toHaveLength(0);
        });
      });

      describe('when the ignore issue updates option is disabled', (): void => {
        beforeEach((): void => {
          sut.staleOnIssueUpdates();
        });

        it('should not stale the issue', async () => {
          expect.assertions(3);

          await sut.test();

          expect(sut.processor.staleIssues).toHaveLength(0);
          expect(sut.processor.closedIssues).toHaveLength(0);
          expect(sut.processor.removedLabelIssues).toHaveLength(0);
        });
      });

      describe('when the ignore issue updates option is unset', (): void => {
        beforeEach((): void => {
          sut.unsetIgnoreIssueUpdates();
        });

        it('should not stale the issue', async () => {
          expect.assertions(3);

          await sut.test();

          expect(sut.processor.staleIssues).toHaveLength(0);
          expect(sut.processor.closedIssues).toHaveLength(0);
          expect(sut.processor.removedLabelIssues).toHaveLength(0);
        });
      });
    });

    describe('when the ignore updates option is enabled', (): void => {
      beforeEach((): void => {
        sut.ignoreUpdates();
      });

      it('should stale the issue', async () => {
        expect.assertions(3);

        await sut.test();

        expect(sut.processor.staleIssues).toHaveLength(1);
        expect(sut.processor.closedIssues).toHaveLength(0);
        expect(sut.processor.removedLabelIssues).toHaveLength(0);
      });

      describe('when the ignore issue updates option is enabled', (): void => {
        beforeEach((): void => {
          sut.ignoreIssueUpdates();
        });

        it('should stale the issue', async () => {
          expect.assertions(3);

          await sut.test();

          expect(sut.processor.staleIssues).toHaveLength(1);
          expect(sut.processor.closedIssues).toHaveLength(0);
          expect(sut.processor.removedLabelIssues).toHaveLength(0);
        });
      });

      describe('when the ignore issue updates option is disabled', (): void => {
        beforeEach((): void => {
          sut.staleOnIssueUpdates();
        });

        it('should not stale the issue', async () => {
          expect.assertions(3);

          await sut.test();

          expect(sut.processor.staleIssues).toHaveLength(0);
          expect(sut.processor.closedIssues).toHaveLength(0);
          expect(sut.processor.removedLabelIssues).toHaveLength(0);
        });
      });

      describe('when the ignore issue updates option is unset', (): void => {
        beforeEach((): void => {
          sut.unsetIgnoreIssueUpdates();
        });

        it('should stale the issue', async () => {
          expect.assertions(3);

          await sut.test();

          expect(sut.processor.staleIssues).toHaveLength(1);
          expect(sut.processor.closedIssues).toHaveLength(0);
          expect(sut.processor.removedLabelIssues).toHaveLength(0);
        });
      });
    });
  });

  describe('when the issue should be stale within 10 days and was created 20 days ago and updated 15 days ago', (): void => {
    beforeEach((): void => {
      sut.toIssue().staleIn(10).created(20).updated(15);
    });

    describe('when the ignore updates option is disabled', (): void => {
      beforeEach((): void => {
        sut.staleOnUpdates();
      });

      it('should stale the issue', async () => {
        expect.assertions(3);

        await sut.test();

        expect(sut.processor.staleIssues).toHaveLength(1);
        expect(sut.processor.closedIssues).toHaveLength(0);
        expect(sut.processor.removedLabelIssues).toHaveLength(0);
      });

      describe('when the ignore issue updates option is enabled', (): void => {
        beforeEach((): void => {
          sut.ignoreIssueUpdates();
        });

        it('should stale the issue', async () => {
          expect.assertions(3);

          await sut.test();

          expect(sut.processor.staleIssues).toHaveLength(1);
          expect(sut.processor.closedIssues).toHaveLength(0);
          expect(sut.processor.removedLabelIssues).toHaveLength(0);
        });
      });

      describe('when the ignore issue updates option is disabled', (): void => {
        beforeEach((): void => {
          sut.staleOnIssueUpdates();
        });

        it('should stale the issue', async () => {
          expect.assertions(3);

          await sut.test();

          expect(sut.processor.staleIssues).toHaveLength(1);
          expect(sut.processor.closedIssues).toHaveLength(0);
          expect(sut.processor.removedLabelIssues).toHaveLength(0);
        });
      });

      describe('when the ignore issue updates option is unset', (): void => {
        beforeEach((): void => {
          sut.unsetIgnoreIssueUpdates();
        });

        it('should stale the issue', async () => {
          expect.assertions(3);

          await sut.test();

          expect(sut.processor.staleIssues).toHaveLength(1);
          expect(sut.processor.closedIssues).toHaveLength(0);
          expect(sut.processor.removedLabelIssues).toHaveLength(0);
        });
      });
    });

    describe('when the ignore updates option is enabled', (): void => {
      beforeEach((): void => {
        sut.ignoreUpdates();
      });

      it('should stale the issue', async () => {
        expect.assertions(3);

        await sut.test();

        expect(sut.processor.staleIssues).toHaveLength(1);
        expect(sut.processor.closedIssues).toHaveLength(0);
        expect(sut.processor.removedLabelIssues).toHaveLength(0);
      });

      describe('when the ignore issue updates option is enabled', (): void => {
        beforeEach((): void => {
          sut.ignoreIssueUpdates();
        });

        it('should stale the issue', async () => {
          expect.assertions(3);

          await sut.test();

          expect(sut.processor.staleIssues).toHaveLength(1);
          expect(sut.processor.closedIssues).toHaveLength(0);
          expect(sut.processor.removedLabelIssues).toHaveLength(0);
        });
      });

      describe('when the ignore issue updates option is disabled', (): void => {
        beforeEach((): void => {
          sut.staleOnIssueUpdates();
        });

        it('should stale the issue', async () => {
          expect.assertions(3);

          await sut.test();

          expect(sut.processor.staleIssues).toHaveLength(1);
          expect(sut.processor.closedIssues).toHaveLength(0);
          expect(sut.processor.removedLabelIssues).toHaveLength(0);
        });
      });

      describe('when the ignore issue updates option is unset', (): void => {
        beforeEach((): void => {
          sut.unsetIgnoreIssueUpdates();
        });

        it('should stale the issue', async () => {
          expect.assertions(3);

          await sut.test();

          expect(sut.processor.staleIssues).toHaveLength(1);
          expect(sut.processor.closedIssues).toHaveLength(0);
          expect(sut.processor.removedLabelIssues).toHaveLength(0);
        });
      });
    });
  });

  describe('when the pull request should be stale within 10 days and was created 20 days ago and updated 5 days ago', (): void => {
    beforeEach((): void => {
      sut.toPullRequest().staleIn(10).created(20).updated(5);
    });

    describe('when the ignore updates option is disabled', (): void => {
      beforeEach((): void => {
        sut.staleOnUpdates();
      });

      it('should not stale the pull request', async () => {
        expect.assertions(3);

        await sut.test();

        expect(sut.processor.staleIssues).toHaveLength(0);
        expect(sut.processor.closedIssues).toHaveLength(0);
        expect(sut.processor.removedLabelIssues).toHaveLength(0);
      });

      describe('when the ignore pull request updates option is enabled', (): void => {
        beforeEach((): void => {
          sut.ignorePullRequestUpdates();
        });

        it('should stale the pull request', async () => {
          expect.assertions(3);

          await sut.test();

          expect(sut.processor.staleIssues).toHaveLength(1);
          expect(sut.processor.closedIssues).toHaveLength(0);
          expect(sut.processor.removedLabelIssues).toHaveLength(0);
        });
      });

      describe('when the ignore pull request updates option is disabled', (): void => {
        beforeEach((): void => {
          sut.staleOnPullRequestUpdates();
        });

        it('should not stale the pull request', async () => {
          expect.assertions(3);

          await sut.test();

          expect(sut.processor.staleIssues).toHaveLength(0);
          expect(sut.processor.closedIssues).toHaveLength(0);
          expect(sut.processor.removedLabelIssues).toHaveLength(0);
        });
      });

      describe('when the ignore pull request updates option is unset', (): void => {
        beforeEach((): void => {
          sut.unsetIgnorePullRequestUpdates();
        });

        it('should not stale the pull request', async () => {
          expect.assertions(3);

          await sut.test();

          expect(sut.processor.staleIssues).toHaveLength(0);
          expect(sut.processor.closedIssues).toHaveLength(0);
          expect(sut.processor.removedLabelIssues).toHaveLength(0);
        });
      });
    });

    describe('when the ignore updates option is enabled', (): void => {
      beforeEach((): void => {
        sut.ignoreUpdates();
      });

      it('should stale the pull request', async () => {
        expect.assertions(3);

        await sut.test();

        expect(sut.processor.staleIssues).toHaveLength(1);
        expect(sut.processor.closedIssues).toHaveLength(0);
        expect(sut.processor.removedLabelIssues).toHaveLength(0);
      });

      describe('when the ignore pull request updates option is enabled', (): void => {
        beforeEach((): void => {
          sut.ignorePullRequestUpdates();
        });

        it('should stale the pull request', async () => {
          expect.assertions(3);

          await sut.test();

          expect(sut.processor.staleIssues).toHaveLength(1);
          expect(sut.processor.closedIssues).toHaveLength(0);
          expect(sut.processor.removedLabelIssues).toHaveLength(0);
        });
      });

      describe('when the ignore pull request updates option is disabled', (): void => {
        beforeEach((): void => {
          sut.staleOnPullRequestUpdates();
        });

        it('should not stale the pull request', async () => {
          expect.assertions(3);

          await sut.test();

          expect(sut.processor.staleIssues).toHaveLength(0);
          expect(sut.processor.closedIssues).toHaveLength(0);
          expect(sut.processor.removedLabelIssues).toHaveLength(0);
        });
      });

      describe('when the ignore pull request updates option is unset', (): void => {
        beforeEach((): void => {
          sut.unsetIgnorePullRequestUpdates();
        });

        it('should stale the pull request', async () => {
          expect.assertions(3);

          await sut.test();

          expect(sut.processor.staleIssues).toHaveLength(1);
          expect(sut.processor.closedIssues).toHaveLength(0);
          expect(sut.processor.removedLabelIssues).toHaveLength(0);
        });
      });
    });
  });

  describe('when the pull request should be stale within 10 days and was created 20 days ago and updated 15 days ago', (): void => {
    beforeEach((): void => {
      sut.toPullRequest().staleIn(10).created(20).updated(15);
    });

    describe('when the ignore updates option is disabled', (): void => {
      beforeEach((): void => {
        sut.staleOnUpdates();
      });

      it('should stale the pull request', async () => {
        expect.assertions(3);

        await sut.test();

        expect(sut.processor.staleIssues).toHaveLength(1);
        expect(sut.processor.closedIssues).toHaveLength(0);
        expect(sut.processor.removedLabelIssues).toHaveLength(0);
      });

      describe('when the ignore pull request updates option is enabled', (): void => {
        beforeEach((): void => {
          sut.ignorePullRequestUpdates();
        });

        it('should stale the pull request', async () => {
          expect.assertions(3);

          await sut.test();

          expect(sut.processor.staleIssues).toHaveLength(1);
          expect(sut.processor.closedIssues).toHaveLength(0);
          expect(sut.processor.removedLabelIssues).toHaveLength(0);
        });
      });

      describe('when the ignore pull request updates option is disabled', (): void => {
        beforeEach((): void => {
          sut.staleOnPullRequestUpdates();
        });

        it('should stale the pull request', async () => {
          expect.assertions(3);

          await sut.test();

          expect(sut.processor.staleIssues).toHaveLength(1);
          expect(sut.processor.closedIssues).toHaveLength(0);
          expect(sut.processor.removedLabelIssues).toHaveLength(0);
        });
      });

      describe('when the ignore pull request updates option is unset', (): void => {
        beforeEach((): void => {
          sut.unsetIgnorePullRequestUpdates();
        });

        it('should stale the pull request', async () => {
          expect.assertions(3);

          await sut.test();

          expect(sut.processor.staleIssues).toHaveLength(1);
          expect(sut.processor.closedIssues).toHaveLength(0);
          expect(sut.processor.removedLabelIssues).toHaveLength(0);
        });
      });
    });

    describe('when the ignore updates option is enabled', (): void => {
      beforeEach((): void => {
        sut.ignoreUpdates();
      });

      it('should stale the pull request', async () => {
        expect.assertions(3);

        await sut.test();

        expect(sut.processor.staleIssues).toHaveLength(1);
        expect(sut.processor.closedIssues).toHaveLength(0);
        expect(sut.processor.removedLabelIssues).toHaveLength(0);
      });

      describe('when the ignore pull request updates option is enabled', (): void => {
        beforeEach((): void => {
          sut.ignorePullRequestUpdates();
        });

        it('should stale the pull request', async () => {
          expect.assertions(3);

          await sut.test();

          expect(sut.processor.staleIssues).toHaveLength(1);
          expect(sut.processor.closedIssues).toHaveLength(0);
          expect(sut.processor.removedLabelIssues).toHaveLength(0);
        });
      });

      describe('when the ignore pull request updates option is disabled', (): void => {
        beforeEach((): void => {
          sut.staleOnPullRequestUpdates();
        });

        it('should stale the pull request', async () => {
          expect.assertions(3);

          await sut.test();

          expect(sut.processor.staleIssues).toHaveLength(1);
          expect(sut.processor.closedIssues).toHaveLength(0);
          expect(sut.processor.removedLabelIssues).toHaveLength(0);
        });
      });

      describe('when the ignore pull request updates option is unset', (): void => {
        beforeEach((): void => {
          sut.unsetIgnorePullRequestUpdates();
        });

        it('should stale the pull request', async () => {
          expect.assertions(3);

          await sut.test();

          expect(sut.processor.staleIssues).toHaveLength(1);
          expect(sut.processor.closedIssues).toHaveLength(0);
          expect(sut.processor.removedLabelIssues).toHaveLength(0);
        });
      });
    });
  });
});

class SUT {
  processor!: IssuesProcessorMock;
  private _opts: IIssuesProcessorOptions = {...DefaultProcessorOptions};
  private _isPullRequest = false;
  private _createdAt: IsoDateString = '2020-01-01T17:00:00Z';
  private _updatedAt: IsoDateString = '2020-01-01T17:00:00Z';
  private _testIssueList: Issue[] = [];

  toIssue(): SUT {
    this._isPullRequest = false;

    return this;
  }

  toPullRequest(): SUT {
    this._isPullRequest = true;

    return this;
  }

  staleIn(days: number): SUT {
    this._updateOptions({
      daysBeforeIssueStale: days,
      daysBeforePrStale: days
    });

    return this;
  }

  created(daysAgo: number): SUT {
    const today = new Date();
    today.setDate(today.getDate() - daysAgo);
    this._createdAt = today.toISOString();

    return this;
  }

  updated(daysAgo: number): SUT {
    const today = new Date();
    today.setDate(today.getDate() - daysAgo);
    this._updatedAt = today.toISOString();

    return this;
  }

  ignoreUpdates(): SUT {
    this._updateOptions({
      ignoreUpdates: true
    });

    return this;
  }

  staleOnUpdates(): SUT {
    this._updateOptions({
      ignoreUpdates: false
    });

    return this;
  }

  ignoreIssueUpdates(): SUT {
    this._updateOptions({
      ignoreIssueUpdates: true
    });

    return this;
  }

  staleOnIssueUpdates(): SUT {
    this._updateOptions({
      ignoreIssueUpdates: false
    });

    return this;
  }

  unsetIgnoreIssueUpdates(): SUT {
    this._updateOptions({
      ignoreIssueUpdates: undefined
    });

    return this;
  }

  ignorePullRequestUpdates(): SUT {
    this._updateOptions({
      ignorePrUpdates: true
    });

    return this;
  }

  staleOnPullRequestUpdates(): SUT {
    this._updateOptions({
      ignorePrUpdates: false
    });

    return this;
  }

  unsetIgnorePullRequestUpdates(): SUT {
    this._updateOptions({
      ignorePrUpdates: undefined
    });

    return this;
  }

  async test(): Promise<number> {
    return this._setTestIssueList()._setProcessor();
  }

  private _updateOptions(opts: Partial<IIssuesProcessorOptions>): SUT {
    this._opts = {...this._opts, ...opts};

    return this;
  }

  private _setTestIssueList(): SUT {
    this._testIssueList = [
      generateIssue(
        this._opts,
        1,
        'My first issue',
        this._updatedAt,
        this._createdAt,
        false,
        this._isPullRequest
      )
    ];

    return this;
  }

  private async _setProcessor(): Promise<number> {
    this.processor = new IssuesProcessorMock(
      this._opts,
      alwaysFalseStateMock,
      async p => (p === 1 ? this._testIssueList : []),
      async () => [],
      async () => new Date().toDateString()
    );

    return this.processor.processIssues(1);
  }
}
```

## File: `__tests__/classes/issues-processor-mock.ts`
```typescript
import {Issue} from '../../src/classes/issue';
import {IssuesProcessor} from '../../src/classes/issues-processor';
import {IComment} from '../../src/interfaces/comment';
import {IIssuesProcessorOptions} from '../../src/interfaces/issues-processor-options';
import {IPullRequest} from '../../src/interfaces/pull-request';
import {IState} from '../../src/interfaces/state/state';
import {IIssueEvent} from '../../src/interfaces/issue-event';

export class IssuesProcessorMock extends IssuesProcessor {
  constructor(
    options: IIssuesProcessorOptions,
    state: IState,
    getIssues?: (page: number) => Promise<Issue[]>,
    listIssueComments?: (
      issue: Issue,
      sinceDate: string
    ) => Promise<IComment[]>,
    getLabelCreationDate?: (
      issue: Issue,
      label: string
    ) =>
      | Promise<string | undefined>
      | Promise<{creationDate?: string; events: IIssueEvent[]}>,
    hasOnlyStaleLabelingEventsSince?: (
      issue: Issue,
      sinceDate: string,
      staleLabel: string,
      events: IIssueEvent[]
    ) => Promise<boolean>,
    getPullRequest?: (issue: Issue) => Promise<IPullRequest | undefined | void>
  ) {
    super(options, state);

    if (getIssues) {
      this.getIssues = getIssues;
    }

    if (listIssueComments) {
      this.listIssueComments = listIssueComments;
    }

    if (getLabelCreationDate) {
      this.getLabelCreationDate = async (
        issue: Issue,
        label: string
      ): Promise<{creationDate?: string; events: IIssueEvent[]}> => {
        const result = await getLabelCreationDate(issue, label);
        if (typeof result === 'string' || typeof result === 'undefined') {
          return {creationDate: result, events: []};
        }

        return result;
      };
    }

    if (hasOnlyStaleLabelingEventsSince) {
      this.hasOnlyStaleLabelingEventsSince = hasOnlyStaleLabelingEventsSince;
    }

    if (getPullRequest) {
      this.getPullRequest = getPullRequest;
    }
  }
}
```

## File: `__tests__/classes/state-mock.ts`
```typescript
import {IState} from '../../src/interfaces/state/state';
import {IIssue} from '../../src/interfaces/issue';

export class StateMock implements IState {
  // eslint-disable-next-line @typescript-eslint/no-unused-vars
  addIssueToProcessed(issue: IIssue) {}

  // eslint-disable-next-line @typescript-eslint/no-unused-vars
  isIssueProcessed(issue: IIssue) {
    return false;
  }

  persist(): Promise<void> {
    return Promise.resolve(undefined);
  }

  restore(): Promise<void> {
    return Promise.resolve(undefined);
  }

  reset() {}
}

export const alwaysFalseStateMock = new StateMock();
```

## File: `__tests__/constants/default-processor-options.ts`
```typescript
import {IIssuesProcessorOptions} from '../../src/interfaces/issues-processor-options';

// Default options for use in tests.
// Mirrors the defaults defined in action.yml
export const DefaultProcessorOptions: IIssuesProcessorOptions = Object.freeze({
  repoToken: 'none',
  staleIssueMessage: 'This issue is stale',
  stalePrMessage: 'This PR is stale',
  closeIssueMessage: 'This issue is being closed',
  closePrMessage: 'This PR is being closed',
  daysBeforeStale: 1,
  daysBeforeIssueStale: NaN,
  daysBeforePrStale: NaN,
  daysBeforeClose: 30,
  daysBeforeIssueClose: NaN,
  daysBeforePrClose: NaN,
  staleIssueLabel: 'Stale',
  closeIssueLabel: '',
  exemptIssueLabels: '',
  stalePrLabel: 'Stale',
  closePrLabel: '',
  exemptPrLabels: '',
  onlyLabels: '',
  onlyIssueLabels: '',
  onlyPrLabels: '',
  anyOfLabels: '',
  anyOfIssueLabels: '',
  anyOfPrLabels: '',
  operationsPerRun: 100,
  debugOnly: true,
  removeStaleWhenUpdated: false,
  removeIssueStaleWhenUpdated: undefined,
  removePrStaleWhenUpdated: undefined,
  ascending: false,
  sortBy: 'created',
  deleteBranch: false,
  startDate: '',
  exemptMilestones: '',
  exemptIssueMilestones: '',
  exemptPrMilestones: '',
  exemptAllMilestones: false,
  exemptAllIssueMilestones: undefined,
  exemptAllPrMilestones: undefined,
  exemptAssignees: '',
  exemptIssueAssignees: '',
  exemptPrAssignees: '',
  exemptAllAssignees: false,
  exemptAllIssueAssignees: undefined,
  exemptAllPrAssignees: undefined,
  enableStatistics: true,
  labelsToRemoveWhenStale: '',
  labelsToRemoveWhenUnstale: '',
  labelsToAddWhenUnstale: '',
  ignoreUpdates: false,
  ignoreIssueUpdates: undefined,
  ignorePrUpdates: undefined,
  exemptDraftPr: false,
  closeIssueReason: 'not_planned',
  includeOnlyAssigned: false
});
```

## File: `__tests__/functions/generate-iissue.ts`
```typescript
import {IIssue} from '../../src/interfaces/issue';

export function generateIIssue(
  partialIssue?: Readonly<Partial<IIssue>>
): IIssue {
  return {
    milestone: undefined,
    assignees: [],
    labels: [],
    created_at: new Date().toISOString(),
    updated_at: new Date().toISOString(),
    draft: false,
    number: Math.round(Math.random() * 5000),
    pull_request: null,
    title: 'dummy-title',
    locked: false,
    state: 'dummy-state',
    ...partialIssue
  };
}
```

## File: `__tests__/functions/generate-issue.ts`
```typescript
import {Issue} from '../../src/classes/issue';
import {IUserAssignee} from '../../src/interfaces/assignee';
import {IIssuesProcessorOptions} from '../../src/interfaces/issues-processor-options';
import {IsoDateString} from '../../src/types/iso-date-string';

export function generateIssue(
  options: IIssuesProcessorOptions,
  id: number,
  title: string,
  updatedAt: IsoDateString,
  createdAt: IsoDateString = updatedAt,
  draft = false,
  isPullRequest = false,
  labels: string[] = [],
  isClosed = false,
  isLocked = false,
  milestone: string | undefined = undefined,
  assignees: string[] = [],
  issue_type?: string
): Issue {
  return new Issue(options, {
    number: id,
    labels: labels.map(l => {
      return {name: l};
    }),
    title,
    created_at: createdAt,
    updated_at: updatedAt,
    draft: draft,
    pull_request: isPullRequest ? {} : null,
    state: isClosed ? 'closed' : 'open',
    locked: isLocked,
    milestone: milestone
      ? {
          title: milestone
        }
      : undefined,
    assignees: assignees.map((assignee: Readonly<string>): IUserAssignee => {
      return {
        login: assignee,
        type: 'User'
      };
    }),
    ...(issue_type ? {type: {name: issue_type}} : {})
  });
}
```

## File: `brain/knowledge/docs_legacy/contributors.md`
```markdown
# Contributors

### Checkin

- Do check in source (src)
- Do not check in build output (lib)
- Do not check in node_modules
```

## File: `src/main.ts`
```typescript
import * as core from '@actions/core';
import {IssuesProcessor} from './classes/issues-processor';
import {isValidDate} from './functions/dates/is-valid-date';
import {IIssuesProcessorOptions} from './interfaces/issues-processor-options';
import {Issue} from './classes/issue';
import {getStateInstance} from './services/state.service';

async function _run(): Promise<void> {
  try {
    const args = _getAndValidateArgs();

    const state = getStateInstance(args);
    await state.restore();

    const issueProcessor: IssuesProcessor = new IssuesProcessor(args, state);

    const rateLimitAtStart = await issueProcessor.getRateLimit();
    if (rateLimitAtStart) {
      core.debug(
        `Github API rate status: limit=${rateLimitAtStart.limit}, used=${rateLimitAtStart.used}, remaining=${rateLimitAtStart.remaining}`
      );
    }

    await issueProcessor.processIssues();

    const rateLimitAtEnd = await issueProcessor.getRateLimit();

    if (rateLimitAtEnd) {
      core.debug(
        `Github API rate status: limit=${rateLimitAtEnd.limit}, used=${rateLimitAtEnd.used}, remaining=${rateLimitAtEnd.remaining}`
      );

      if (rateLimitAtStart)
        core.info(
          `Github API rate used: ${
            rateLimitAtStart.remaining - rateLimitAtEnd.remaining
          }`
        );

      core.info(
        `Github API rate remaining: ${rateLimitAtEnd.remaining}; reset at: ${rateLimitAtEnd.reset}`
      );
    }

    await state.persist();

    await processOutput(
      issueProcessor.staleIssues,
      issueProcessor.closedIssues
    );
  } catch (error) {
    core.error(error);
    core.setFailed(error.message);
  }
}

function _getAndValidateArgs(): IIssuesProcessorOptions {
  const args: IIssuesProcessorOptions = {
    repoToken: core.getInput('repo-token'),
    staleIssueMessage: core.getInput('stale-issue-message'),
    stalePrMessage: core.getInput('stale-pr-message'),
    closeIssueMessage: core.getInput('close-issue-message'),
    closePrMessage: core.getInput('close-pr-message'),
    daysBeforeStale: parseFloat(
      core.getInput('days-before-stale', {required: true})
    ),
    daysBeforeIssueStale: parseFloat(core.getInput('days-before-issue-stale')),
    daysBeforePrStale: parseFloat(core.getInput('days-before-pr-stale')),
    daysBeforeClose: parseInt(
      core.getInput('days-before-close', {required: true})
    ),
    daysBeforeIssueClose: parseInt(core.getInput('days-before-issue-close')),
    daysBeforePrClose: parseInt(core.getInput('days-before-pr-close')),
    staleIssueLabel: core.getInput('stale-issue-label', {required: true}),
    closeIssueLabel: core.getInput('close-issue-label'),
    exemptIssueLabels: core.getInput('exempt-issue-labels'),
    stalePrLabel: core.getInput('stale-pr-label', {required: true}),
    closePrLabel: core.getInput('close-pr-label'),
    exemptPrLabels: core.getInput('exempt-pr-labels'),
    onlyLabels: core.getInput('only-labels'),
    onlyIssueLabels: core.getInput('only-issue-labels'),
    onlyPrLabels: core.getInput('only-pr-labels'),
    anyOfLabels: core.getInput('any-of-labels'),
    anyOfIssueLabels: core.getInput('any-of-issue-labels'),
    anyOfPrLabels: core.getInput('any-of-pr-labels'),
    operationsPerRun: parseInt(
      core.getInput('operations-per-run', {required: true})
    ),
    removeStaleWhenUpdated: !(
      core.getInput('remove-stale-when-updated') === 'false'
    ),
    removeIssueStaleWhenUpdated: _toOptionalBoolean(
      'remove-issue-stale-when-updated'
    ),
    removePrStaleWhenUpdated: _toOptionalBoolean(
      'remove-pr-stale-when-updated'
    ),
    debugOnly: core.getInput('debug-only') === 'true',
    ascending: core.getInput('ascending') === 'true',
    sortBy: _processParamtoString(core.getInput('sort-by')),
    deleteBranch: core.getInput('delete-branch') === 'true',
    startDate:
      core.getInput('start-date') !== ''
        ? core.getInput('start-date')
        : undefined,
    exemptMilestones: core.getInput('exempt-milestones'),
    exemptIssueMilestones: core.getInput('exempt-issue-milestones'),
    exemptPrMilestones: core.getInput('exempt-pr-milestones'),
    exemptAllMilestones: core.getInput('exempt-all-milestones') === 'true',
    exemptAllIssueMilestones: _toOptionalBoolean('exempt-all-issue-milestones'),
    exemptAllPrMilestones: _toOptionalBoolean('exempt-all-pr-milestones'),
    exemptAssignees: core.getInput('exempt-assignees'),
    exemptIssueAssignees: core.getInput('exempt-issue-assignees'),
    exemptPrAssignees: core.getInput('exempt-pr-assignees'),
    exemptAllAssignees: core.getInput('exempt-all-assignees') === 'true',
    exemptAllIssueAssignees: _toOptionalBoolean('exempt-all-issue-assignees'),
    exemptAllPrAssignees: _toOptionalBoolean('exempt-all-pr-assignees'),
    enableStatistics: core.getInput('enable-statistics') === 'true',
    labelsToRemoveWhenStale: core.getInput('labels-to-remove-when-stale'),
    labelsToRemoveWhenUnstale: core.getInput('labels-to-remove-when-unstale'),
    labelsToAddWhenUnstale: core.getInput('labels-to-add-when-unstale'),
    ignoreUpdates: core.getInput('ignore-updates') === 'true',
    ignoreIssueUpdates: _toOptionalBoolean('ignore-issue-updates'),
    ignorePrUpdates: _toOptionalBoolean('ignore-pr-updates'),
    exemptDraftPr: core.getInput('exempt-draft-pr') === 'true',
    closeIssueReason: core.getInput('close-issue-reason'),
    includeOnlyAssigned: core.getInput('include-only-assigned') === 'true',
    onlyIssueTypes: core.getInput('only-issue-types')
  };

  for (const numberInput of ['days-before-stale']) {
    if (isNaN(parseFloat(core.getInput(numberInput)))) {
      const errorMessage = `Option "${numberInput}" did not parse to a valid float`;
      core.setFailed(errorMessage);
      throw new Error(errorMessage);
    }
  }

  for (const numberInput of ['days-before-close', 'operations-per-run']) {
    if (isNaN(parseInt(core.getInput(numberInput)))) {
      const errorMessage = `Option "${numberInput}" did not parse to a valid integer`;
      core.setFailed(errorMessage);
      throw new Error(errorMessage);
    }
  }

  for (const optionalDateInput of ['start-date']) {
    // Ignore empty dates because it is considered as the right type for a default value (so a valid one)
    if (core.getInput(optionalDateInput) !== '') {
      if (!isValidDate(new Date(core.getInput(optionalDateInput)))) {
        const errorMessage = `Option "${optionalDateInput}" did not parse to a valid date`;
        core.setFailed(errorMessage);
        throw new Error(errorMessage);
      }
    }
  }

  const validCloseReasons = ['', 'completed', 'not_planned'];
  if (!validCloseReasons.includes(args.closeIssueReason)) {
    const errorMessage = `Unrecognized close-issue-reason "${
      args.closeIssueReason
    }", valid values are: ${validCloseReasons.filter(Boolean).join(', ')}`;
    core.setFailed(errorMessage);
    throw new Error(errorMessage);
  }

  return args;
}

async function processOutput(
  staledIssues: Issue[],
  closedIssues: Issue[]
): Promise<void> {
  core.setOutput('staled-issues-prs', JSON.stringify(staledIssues));
  core.setOutput('closed-issues-prs', JSON.stringify(closedIssues));
}

/**
 * @description
 * From an argument name, get the value as an optional boolean
 * This is very useful for all the arguments that override others
 * It will allow us to easily use the original one when the return value is `undefined`
 * Which is different from `true` or `false` that consider the argument as set
 *
 * @param {Readonly<string>} argumentName The name of the argument to check
 *
 * @returns {boolean | undefined} The value matching the given argument name
 */
function _toOptionalBoolean(
  argumentName: Readonly<string>
): boolean | undefined {
  const argument: string = core.getInput(argumentName);

  if (argument === 'true') {
    return true;
  } else if (argument === 'false') {
    return false;
  }

  return undefined;
}

function _processParamtoString(
  sortByValueInput: string
): 'created' | 'updated' | 'comments' {
  return sortByValueInput === 'updated'
    ? 'updated'
    : sortByValueInput === 'comments'
    ? 'comments'
    : 'created';
}

void _run();
```

## File: `src/classes/assignees.spec.ts`
```typescript
import {DefaultProcessorOptions} from '../../__tests__/constants/default-processor-options';
import {generateIIssue} from '../../__tests__/functions/generate-iissue';
import {IIssue} from '../interfaces/issue';
import {IIssuesProcessorOptions} from '../interfaces/issues-processor-options';
import {Assignees} from './assignees';
import {Issue} from './issue';

describe('Assignees', (): void => {
  let assignees: Assignees;
  let optionsInterface: IIssuesProcessorOptions;
  let issue: Issue;
  let issueInterface: IIssue;

  beforeEach((): void => {
    optionsInterface = {
      ...DefaultProcessorOptions,
      exemptAllAssignees: false
    };
    issueInterface = generateIIssue();
  });

  describe('shouldExemptAssignees()', (): void => {
    describe('when the given issue is not a pull request', (): void => {
      beforeEach((): void => {
        issueInterface.pull_request = undefined;
      });

      describe('when the given options are not configured to exempt an assignee', (): void => {
        beforeEach((): void => {
          optionsInterface.exemptAssignees = '';
        });

        describe('when the given options are not configured to exempt an issue with an assignee', (): void => {
          beforeEach((): void => {
            optionsInterface.exemptIssueAssignees = '';
          });

          describe('when the given issue does not have an assignee', (): void => {
            beforeEach((): void => {
              issueInterface.assignees = [];
            });

            it('should return false', (): void => {
              expect.assertions(1);
              issue = new Issue(optionsInterface, issueInterface);
              assignees = new Assignees(optionsInterface, issue);

              const result = assignees.shouldExemptAssignees();

              expect(result).toStrictEqual(false);
            });
          });

          describe('when the given issue does have an assignee', (): void => {
            beforeEach((): void => {
              issueInterface.assignees = [
                {
                  login: 'dummy-login',
                  type: 'User'
                }
              ];
            });

            it('should return false', (): void => {
              expect.assertions(1);
              issue = new Issue(optionsInterface, issueInterface);
              assignees = new Assignees(optionsInterface, issue);

              const result = assignees.shouldExemptAssignees();

              expect(result).toStrictEqual(false);
            });
          });
        });

        describe('when the given options are configured to exempt an issue with an assignee', (): void => {
          beforeEach((): void => {
            optionsInterface.exemptIssueAssignees =
              'dummy-exempt-issue-assignee';
          });

          describe('when the given issue does not have an assignee', (): void => {
            beforeEach((): void => {
              issueInterface.assignees = [];
            });

            it('should return false', (): void => {
              expect.assertions(1);
              issue = new Issue(optionsInterface, issueInterface);
              assignees = new Assignees(optionsInterface, issue);

              const result = assignees.shouldExemptAssignees();

              expect(result).toStrictEqual(false);
            });
          });

          describe('when the given issue does have an assignee different than the exempt issue assignee', (): void => {
            beforeEach((): void => {
              issueInterface.assignees = [
                {
                  login: 'dummy-login',
                  type: 'User'
                }
              ];
            });

            it('should return false', (): void => {
              expect.assertions(1);
              issue = new Issue(optionsInterface, issueInterface);
              assignees = new Assignees(optionsInterface, issue);

              const result = assignees.shouldExemptAssignees();

              expect(result).toStrictEqual(false);
            });
          });

          describe('when the given issue does have an assignee equaling the exempt issue assignee', (): void => {
            beforeEach((): void => {
              issueInterface.assignees = [
                {
                  login: 'dummy-exempt-issue-assignee',
                  type: 'User'
                }
              ];
            });

            it('should return true', (): void => {
              expect.assertions(1);
              issue = new Issue(optionsInterface, issueInterface);
              assignees = new Assignees(optionsInterface, issue);

              const result = assignees.shouldExemptAssignees();

              expect(result).toStrictEqual(true);
            });
          });
        });
      });

      describe('when the given options are configured to exempt an assignee', (): void => {
        beforeEach((): void => {
          optionsInterface.exemptAssignees = 'dummy-exempt-assignee';
        });

        describe('when the given options are not configured to exempt an issue with an assignee', (): void => {
          beforeEach((): void => {
            optionsInterface.exemptIssueAssignees = '';
          });

          describe('when the given issue does not have an assignee', (): void => {
            beforeEach((): void => {
              issueInterface.assignees = [];
            });

            it('should return false', (): void => {
              expect.assertions(1);
              issue = new Issue(optionsInterface, issueInterface);
              assignees = new Assignees(optionsInterface, issue);

              const result = assignees.shouldExemptAssignees();

              expect(result).toStrictEqual(false);
            });
          });

          describe('when the given issue does have an assignee different than the exempt assignee', (): void => {
            beforeEach((): void => {
              issueInterface.assignees = [
                {
                  login: 'dummy-login',
                  type: 'User'
                }
              ];
            });

            it('should return false', (): void => {
              expect.assertions(1);
              issue = new Issue(optionsInterface, issueInterface);
              assignees = new Assignees(optionsInterface, issue);

              const result = assignees.shouldExemptAssignees();

              expect(result).toStrictEqual(false);
            });
          });

          describe('when the given issue does have an assignee equaling the exempt assignee', (): void => {
            beforeEach((): void => {
              issueInterface.assignees = [
                {
                  login: 'dummy-exempt-assignee',
                  type: 'User'
                }
              ];
            });

            it('should return true', (): void => {
              expect.assertions(1);
              issue = new Issue(optionsInterface, issueInterface);
              assignees = new Assignees(optionsInterface, issue);

              const result = assignees.shouldExemptAssignees();

              expect(result).toStrictEqual(true);
            });
          });
        });

        describe('when the given options are configured to exempt an issue with an assignee', (): void => {
          beforeEach((): void => {
            optionsInterface.exemptIssueAssignees =
              'dummy-exempt-issue-assignee';
          });

          describe('when the given issue does not have an assignee', (): void => {
            beforeEach((): void => {
              issueInterface.assignees = [];
            });

            it('should return false', (): void => {
              expect.assertions(1);
              issue = new Issue(optionsInterface, issueInterface);
              assignees = new Assignees(optionsInterface, issue);

              const result = assignees.shouldExemptAssignees();

              expect(result).toStrictEqual(false);
            });
          });

          describe('when the given issue does have an assignee different than the exempt issue assignee', (): void => {
            beforeEach((): void => {
              issueInterface.assignees = [
                {
                  login: 'dummy-login',
                  type: 'User'
                }
              ];
            });

            it('should return false', (): void => {
              expect.assertions(1);
              issue = new Issue(optionsInterface, issueInterface);
              assignees = new Assignees(optionsInterface, issue);

              const result = assignees.shouldExemptAssignees();

              expect(result).toStrictEqual(false);
            });
          });

          describe('when the given issue does have an assignee equaling the exempt issue assignee', (): void => {
            beforeEach((): void => {
              issueInterface.assignees = [
                {
                  login: 'dummy-exempt-issue-assignee',
                  type: 'User'
                }
              ];
            });

            it('should return true', (): void => {
              expect.assertions(1);
              issue = new Issue(optionsInterface, issueInterface);
              assignees = new Assignees(optionsInterface, issue);

              const result = assignees.shouldExemptAssignees();

              expect(result).toStrictEqual(true);
            });
          });

          describe('when the given issue does have an assignee different than the exempt assignee', (): void => {
            beforeEach((): void => {
              issueInterface.assignees = [
                {
                  login: 'dummy-login',
                  type: 'User'
                }
              ];
            });

            it('should return false', (): void => {
              expect.assertions(1);
              issue = new Issue(optionsInterface, issueInterface);
              assignees = new Assignees(optionsInterface, issue);

              const result = assignees.shouldExemptAssignees();

              expect(result).toStrictEqual(false);
            });
          });

          describe('when the given issue does have an assignee equaling the exempt assignee', (): void => {
            beforeEach((): void => {
              issueInterface.assignees = [
                {
                  login: 'dummy-exempt-assignee',
                  type: 'User'
                }
              ];
            });

            it('should return false', (): void => {
              expect.assertions(1);
              issue = new Issue(optionsInterface, issueInterface);
              assignees = new Assignees(optionsInterface, issue);

              const result = assignees.shouldExemptAssignees();

              expect(result).toStrictEqual(false);
            });
          });
        });
      });

      describe('when the given options are configured to exempt all assignees', (): void => {
        beforeEach((): void => {
          optionsInterface.exemptAllAssignees = true;
        });

        describe('when the given issue does not have an assignee', (): void => {
          beforeEach((): void => {
            issueInterface.assignees = [];
          });

          it('should return false', (): void => {
            expect.assertions(1);
            issue = new Issue(optionsInterface, issueInterface);
            assignees = new Assignees(optionsInterface, issue);

            const result = assignees.shouldExemptAssignees();

            expect(result).toStrictEqual(false);
          });
        });

        describe('when the given issue does have an assignee', (): void => {
          beforeEach((): void => {
            issueInterface.assignees = [
              {
                login: 'dummy-exempt-assignee',
                type: 'User'
              }
            ];
          });

          it('should return true', (): void => {
            expect.assertions(1);
            issue = new Issue(optionsInterface, issueInterface);
            assignees = new Assignees(optionsInterface, issue);

            const result = assignees.shouldExemptAssignees();

            expect(result).toStrictEqual(true);
          });
        });

        describe('when the given options are not configured to exempt all issue assignees', (): void => {
          beforeEach((): void => {
            optionsInterface.exemptAllIssueAssignees = false;
          });

          describe('when the given issue does not have an assignee', (): void => {
            beforeEach((): void => {
              issueInterface.assignees = [];
            });

            it('should return false', (): void => {
              expect.assertions(1);
              issue = new Issue(optionsInterface, issueInterface);
              assignees = new Assignees(optionsInterface, issue);

              const result = assignees.shouldExemptAssignees();

              expect(result).toStrictEqual(false);
            });
          });

          describe('when the given issue does have an assignee', (): void => {
            beforeEach((): void => {
              issueInterface.assignees = [
                {
                  login: 'dummy-exempt-assignee',
                  type: 'User'
                }
              ];
            });

            it('should return false', (): void => {
              expect.assertions(1);
              issue = new Issue(optionsInterface, issueInterface);
              assignees = new Assignees(optionsInterface, issue);

              const result = assignees.shouldExemptAssignees();

              expect(result).toStrictEqual(false);
            });
          });
        });

        describe('when the given options are configured to exempt all issue assignees', (): void => {
          beforeEach((): void => {
            optionsInterface.exemptAllIssueAssignees = true;
          });

          describe('when the given issue does not have an assignee', (): void => {
            beforeEach((): void => {
              issueInterface.assignees = [];
            });

            it('should return false', (): void => {
              expect.assertions(1);
              issue = new Issue(optionsInterface, issueInterface);
              assignees = new Assignees(optionsInterface, issue);

              const result = assignees.shouldExemptAssignees();

              expect(result).toStrictEqual(false);
            });
          });

          describe('when the given issue does have an assignee', (): void => {
            beforeEach((): void => {
              issueInterface.assignees = [
                {
                  login: 'dummy-exempt-issue-assignee',
                  type: 'User'
                }
              ];
            });

            it('should return true', (): void => {
              expect.assertions(1);
              issue = new Issue(optionsInterface, issueInterface);
              assignees = new Assignees(optionsInterface, issue);

              const result = assignees.shouldExemptAssignees();

              expect(result).toStrictEqual(true);
            });
          });
        });
      });
    });

    describe('when the given issue is a pull request', (): void => {
      beforeEach((): void => {
        issueInterface.pull_request = {};
      });

      describe('when the given options are not configured to exempt an assignee', (): void => {
        beforeEach((): void => {
          optionsInterface.exemptAssignees = '';
        });

        describe('when the given options are not configured to exempt a pull request with an assignee', (): void => {
          beforeEach((): void => {
            optionsInterface.exemptPrAssignees = '';
          });

          describe('when the given pull request does not have an assignee', (): void => {
            beforeEach((): void => {
              issueInterface.assignees = [];
            });

            it('should return false', (): void => {
              expect.assertions(1);
              issue = new Issue(optionsInterface, issueInterface);
              assignees = new Assignees(optionsInterface, issue);

              const result = assignees.shouldExemptAssignees();

              expect(result).toStrictEqual(false);
            });
          });

          describe('when the given pull request does have an assignee', (): void => {
            beforeEach((): void => {
              issueInterface.assignees = [
                {
                  login: 'dummy-login',
                  type: 'User'
                }
              ];
            });

            it('should return false', (): void => {
              expect.assertions(1);
              issue = new Issue(optionsInterface, issueInterface);
              assignees = new Assignees(optionsInterface, issue);

              const result = assignees.shouldExemptAssignees();

              expect(result).toStrictEqual(false);
            });
          });
        });

        describe('when the given options are configured to exempt a pull request with an assignee', (): void => {
          beforeEach((): void => {
            optionsInterface.exemptPrAssignees = 'dummy-exempt-pr-assignee';
          });

          describe('when the given pull request does not have an assignee', (): void => {
            beforeEach((): void => {
              issueInterface.assignees = [];
            });

            it('should return false', (): void => {
              expect.assertions(1);
              issue = new Issue(optionsInterface, issueInterface);
              assignees = new Assignees(optionsInterface, issue);

              const result = assignees.shouldExemptAssignees();

              expect(result).toStrictEqual(false);
            });
          });

          describe('when the given pull request does have an assignee different than the exempt pull request assignee', (): void => {
            beforeEach((): void => {
              issueInterface.assignees = [
                {
                  login: 'dummy-login',
                  type: 'User'
                }
              ];
            });

            it('should return false', (): void => {
              expect.assertions(1);
              issue = new Issue(optionsInterface, issueInterface);
              assignees = new Assignees(optionsInterface, issue);

              const result = assignees.shouldExemptAssignees();

              expect(result).toStrictEqual(false);
            });
          });

          describe('when the given pull request does have an assignee equaling the exempt pull request assignee', (): void => {
            beforeEach((): void => {
              issueInterface.assignees = [
                {
                  login: 'dummy-exempt-pr-assignee',
                  type: 'User'
                }
              ];
            });

            it('should return true', (): void => {
              expect.assertions(1);
              issue = new Issue(optionsInterface, issueInterface);
              assignees = new Assignees(optionsInterface, issue);

              const result = assignees.shouldExemptAssignees();

              expect(result).toStrictEqual(true);
            });
          });
        });
      });

      describe('when the given options are configured to exempt an assignee', (): void => {
        beforeEach((): void => {
          optionsInterface.exemptAssignees = 'dummy-exempt-assignee';
        });

        describe('when the given options are not configured to exempt a pull request with an assignee', (): void => {
          beforeEach((): void => {
            optionsInterface.exemptPrAssignees = '';
          });

          describe('when the given pull request does not have an assignee', (): void => {
            beforeEach((): void => {
              issueInterface.assignees = [];
            });

            it('should return false', (): void => {
              expect.assertions(1);
              issue = new Issue(optionsInterface, issueInterface);
              assignees = new Assignees(optionsInterface, issue);

              const result = assignees.shouldExemptAssignees();

              expect(result).toStrictEqual(false);
            });
          });

          describe('when the given pull request does have an assignee different than the exempt assignee', (): void => {
            beforeEach((): void => {
              issueInterface.assignees = [
                {
                  login: 'dummy-login',
                  type: 'User'
                }
              ];
            });

            it('should return false', (): void => {
              expect.assertions(1);
              issue = new Issue(optionsInterface, issueInterface);
              assignees = new Assignees(optionsInterface, issue);

              const result = assignees.shouldExemptAssignees();

              expect(result).toStrictEqual(false);
            });
          });

          describe('when the given pull request does have an assignee equaling the exempt assignee', (): void => {
            beforeEach((): void => {
              issueInterface.assignees = [
                {
                  login: 'dummy-exempt-assignee',
                  type: 'User'
                }
              ];
            });

            it('should return true', (): void => {
              expect.assertions(1);
              issue = new Issue(optionsInterface, issueInterface);
              assignees = new Assignees(optionsInterface, issue);

              const result = assignees.shouldExemptAssignees();

              expect(result).toStrictEqual(true);
            });
          });
        });

        describe('when the given options are configured to exempt a pull request with an assignee', (): void => {
          beforeEach((): void => {
            optionsInterface.exemptPrAssignees = 'dummy-exempt-pr-assignee';
          });

          describe('when the given pull request does not have an assignee', (): void => {
            beforeEach((): void => {
              issueInterface.assignees = [];
            });

            it('should return false', (): void => {
              expect.assertions(1);
              issue = new Issue(optionsInterface, issueInterface);
              assignees = new Assignees(optionsInterface, issue);

              const result = assignees.shouldExemptAssignees();

              expect(result).toStrictEqual(false);
            });
          });

          describe('when the given pull request does have an assignee different than the exempt pull request assignee', (): void => {
            beforeEach((): void => {
              issueInterface.assignees = [
                {
                  login: 'dummy-login',
                  type: 'User'
                }
              ];
            });

            it('should return false', (): void => {
              expect.assertions(1);
              issue = new Issue(optionsInterface, issueInterface);
              assignees = new Assignees(optionsInterface, issue);

              const result = assignees.shouldExemptAssignees();

              expect(result).toStrictEqual(false);
            });
          });

          describe('when the given pull request does have an assignee equaling the exempt pull request assignee', (): void => {
            beforeEach((): void => {
              issueInterface.assignees = [
                {
                  login: 'dummy-exempt-pr-assignee',
                  type: 'User'
                }
              ];
            });

            it('should return true', (): void => {
              expect.assertions(1);
              issue = new Issue(optionsInterface, issueInterface);
              assignees = new Assignees(optionsInterface, issue);

              const result = assignees.shouldExemptAssignees();

              expect(result).toStrictEqual(true);
            });
          });

          describe('when the given pull request does have an assignee different than the exempt assignee', (): void => {
            beforeEach((): void => {
              issueInterface.assignees = [
                {
                  login: 'dummy-login',
                  type: 'User'
                }
              ];
            });

            it('should return false', (): void => {
              expect.assertions(1);
              issue = new Issue(optionsInterface, issueInterface);
              assignees = new Assignees(optionsInterface, issue);

              const result = assignees.shouldExemptAssignees();

              expect(result).toStrictEqual(false);
            });
          });

          describe('when the given pull request does have an assignee equaling the exempt assignee', (): void => {
            beforeEach((): void => {
              issueInterface.assignees = [
                {
                  login: 'dummy-exempt-assignee',
                  type: 'User'
                }
              ];
            });

            it('should return false', (): void => {
              expect.assertions(1);
              issue = new Issue(optionsInterface, issueInterface);
              assignees = new Assignees(optionsInterface, issue);

              const result = assignees.shouldExemptAssignees();

              expect(result).toStrictEqual(false);
            });
          });
        });
      });

      describe('when the given options are configured to exempt all assignees', (): void => {
        beforeEach((): void => {
          optionsInterface.exemptAllAssignees = true;
        });

        describe('when the given pull request does not have an assignee', (): void => {
          beforeEach((): void => {
            issueInterface.assignees = [];
          });

          it('should return false', (): void => {
            expect.assertions(1);
            issue = new Issue(optionsInterface, issueInterface);
            assignees = new Assignees(optionsInterface, issue);

            const result = assignees.shouldExemptAssignees();

            expect(result).toStrictEqual(false);
          });
        });

        describe('when the given pull request does have an assignee', (): void => {
          beforeEach((): void => {
            issueInterface.assignees = [
              {
                login: 'dummy-exempt-assignee',
                type: 'User'
              }
            ];
          });

          it('should return true', (): void => {
            expect.assertions(1);
            issue = new Issue(optionsInterface, issueInterface);
            assignees = new Assignees(optionsInterface, issue);

            const result = assignees.shouldExemptAssignees();

            expect(result).toStrictEqual(true);
          });
        });

        describe('when the given options are not configured to exempt all pull request assignees', (): void => {
          beforeEach((): void => {
            optionsInterface.exemptAllPrAssignees = false;
          });

          describe('when the given pull request does not have an assignee', (): void => {
            beforeEach((): void => {
              issueInterface.assignees = [];
            });

            it('should return false', (): void => {
              expect.assertions(1);
              issue = new Issue(optionsInterface, issueInterface);
              assignees = new Assignees(optionsInterface, issue);

              const result = assignees.shouldExemptAssignees();

              expect(result).toStrictEqual(false);
            });
          });

          describe('when the given pull request does have an assignee', (): void => {
            beforeEach((): void => {
              issueInterface.assignees = [
                {
                  login: 'dummy-exempt-assignee',
                  type: 'User'
                }
              ];
            });

            it('should return false', (): void => {
              expect.assertions(1);
              issue = new Issue(optionsInterface, issueInterface);
              assignees = new Assignees(optionsInterface, issue);

              const result = assignees.shouldExemptAssignees();

              expect(result).toStrictEqual(false);
            });
          });
        });

        describe('when the given options are configured to exempt all pull request assignees', (): void => {
          beforeEach((): void => {
            optionsInterface.exemptAllPrAssignees = true;
          });

          describe('when the given pull request does not have an assignee', (): void => {
            beforeEach((): void => {
              issueInterface.assignees = [];
            });

            it('should return false', (): void => {
              expect.assertions(1);
              issue = new Issue(optionsInterface, issueInterface);
              assignees = new Assignees(optionsInterface, issue);

              const result = assignees.shouldExemptAssignees();

              expect(result).toStrictEqual(false);
            });
          });

          describe('when the given pull request does have an assignee', (): void => {
            beforeEach((): void => {
              issueInterface.assignees = [
                {
                  login: 'dummy-exempt-issue-assignee',
                  type: 'User'
                }
              ];
            });

            it('should return true', (): void => {
              expect.assertions(1);
              issue = new Issue(optionsInterface, issueInterface);
              assignees = new Assignees(optionsInterface, issue);

              const result = assignees.shouldExemptAssignees();

              expect(result).toStrictEqual(true);
            });
          });
        });
      });
    });
  });
});
```

## File: `src/classes/assignees.ts`
```typescript
import deburr from 'lodash.deburr';
import {Option} from '../enums/option';
import {wordsToList} from '../functions/words-to-list';
import {Assignee} from '../interfaces/assignee';
import {IIssuesProcessorOptions} from '../interfaces/issues-processor-options';
import {Issue} from './issue';
import {IssueLogger} from './loggers/issue-logger';
import {LoggerService} from '../services/logger.service';

type CleanAssignee = string;

export class Assignees {
  private readonly _options: IIssuesProcessorOptions;
  private readonly _issue: Issue;
  private readonly _issueLogger: IssueLogger;

  constructor(options: Readonly<IIssuesProcessorOptions>, issue: Issue) {
    this._options = options;
    this._issue = issue;
    this._issueLogger = new IssueLogger(issue);
  }

  private static _cleanAssignee(assignee: Readonly<string>): CleanAssignee {
    return deburr(assignee.toLowerCase());
  }

  shouldExemptAssignees(): boolean {
    if (!this._issue.hasAssignees) {
      this._issueLogger.info('This $$type has no assignee');
      this._logSkip();

      return false;
    }

    if (this._shouldExemptAllAssignees()) {
      this._issueLogger.info(
        LoggerService.white('└──'),
        'Skipping this $$type because it has an exempt assignee'
      );

      return true;
    }

    const exemptAssignees: string[] = this._getExemptAssignees();

    if (exemptAssignees.length === 0) {
      this._issueLogger.info(
        LoggerService.white('├──'),
        `No assignee option was specified to skip the stale process for this $$type`
      );
      this._logSkip();

      return false;
    }

    this._issueLogger.info(
      LoggerService.white('├──'),
      `Found ${LoggerService.cyan(exemptAssignees.length)} assignee${
        exemptAssignees.length > 1 ? 's' : ''
      } that can exempt stale on this $$type`
    );

    const hasExemptAssignee: boolean = exemptAssignees.some(
      (exemptAssignee: Readonly<string>): boolean =>
        this._hasAssignee(exemptAssignee)
    );

    if (!hasExemptAssignee) {
      this._issueLogger.info(
        LoggerService.white('├──'),
        'No assignee on this $$type can exempt the stale process'
      );
      this._logSkip();
    } else {
      this._issueLogger.info(
        LoggerService.white('└──'),
        'Skipping this $$type because it has an exempt assignee'
      );
    }

    return hasExemptAssignee;
  }

  private _getExemptAssignees(): string[] {
    return this._issue.isPullRequest
      ? this._getExemptPullRequestAssignees()
      : this._getExemptIssueAssignees();
  }

  private _getExemptIssueAssignees(): string[] {
    if (this._options.exemptIssueAssignees === '') {
      this._issueLogger.info(
        LoggerService.white('├──'),
        `The option ${this._issueLogger.createOptionLink(
          Option.ExemptIssueAssignees
        )} is disabled. No specific assignee can skip the stale process for this $$type`
      );

      if (this._options.exemptAssignees === '') {
        this._issueLogger.info(
          LoggerService.white('├──'),
          `The option ${this._issueLogger.createOptionLink(
            Option.ExemptAssignees
          )} is disabled. No specific assignee can skip the stale process for this $$type`
        );

        return [];
      }

      const exemptAssignees: string[] = wordsToList(
        this._options.exemptAssignees
      );

      this._issueLogger.info(
        LoggerService.white('├──'),
        `The option ${this._issueLogger.createOptionLink(
          Option.ExemptAssignees
        )} is set. ${LoggerService.cyan(exemptAssignees.length)} assignee${
          exemptAssignees.length === 1 ? '' : 's'
        } can skip the stale process for this $$type`
      );

      return exemptAssignees;
    }

    const exemptAssignees: string[] = wordsToList(
      this._options.exemptIssueAssignees
    );

    this._issueLogger.info(
      LoggerService.white('├──'),
      `The option ${this._issueLogger.createOptionLink(
        Option.ExemptIssueAssignees
      )} is set. ${LoggerService.cyan(exemptAssignees.length)} assignee${
        exemptAssignees.length === 1 ? '' : 's'
      } can skip the stale process for this $$type`
    );

    return exemptAssignees;
  }

  private _getExemptPullRequestAssignees(): string[] {
    if (this._options.exemptPrAssignees === '') {
      this._issueLogger.info(
        LoggerService.white('├──'),
        `The option ${this._issueLogger.createOptionLink(
          Option.ExemptPrAssignees
        )} is disabled. No specific assignee can skip the stale process for this $$type`
      );

      if (this._options.exemptAssignees === '') {
        this._issueLogger.info(
          LoggerService.white('├──'),
          `The option ${this._issueLogger.createOptionLink(
            Option.ExemptAssignees
          )} is disabled. No specific assignee can skip the stale process for this $$type`
        );

        return [];
      }

      const exemptAssignees: string[] = wordsToList(
        this._options.exemptAssignees
      );

      this._issueLogger.info(
        LoggerService.white('├──'),
        `The option ${this._issueLogger.createOptionLink(
          Option.ExemptAssignees
        )} is set. ${LoggerService.cyan(exemptAssignees.length)} assignee${
          exemptAssignees.length === 1 ? '' : 's'
        } can skip the stale process for this $$type`
      );

      return exemptAssignees;
    }

    const exemptAssignees: string[] = wordsToList(
      this._options.exemptPrAssignees
    );

    this._issueLogger.info(
      LoggerService.white('├──'),
      `The option ${this._issueLogger.createOptionLink(
        Option.ExemptPrAssignees
      )} is set. ${LoggerService.cyan(exemptAssignees.length)} assignee${
        exemptAssignees.length === 1 ? '' : 's'
      } can skip the stale process for this $$type`
    );

    return exemptAssignees;
  }

  private _hasAssignee(assignee: Readonly<string>): boolean {
    const cleanAssignee: CleanAssignee = Assignees._cleanAssignee(assignee);

    return this._issue.assignees.some(
      (issueAssignee: Readonly<Assignee>): boolean => {
        const isSameAssignee: boolean =
          cleanAssignee === Assignees._cleanAssignee(issueAssignee.login);

        if (isSameAssignee) {
          this._issueLogger.info(
            LoggerService.white('├──'),
            `@${issueAssignee.login} is assigned on this $$type and is an exempt assignee`
          );
        }

        return isSameAssignee;
      }
    );
  }

  private _shouldExemptAllAssignees(): boolean {
    return this._issue.isPullRequest
      ? this._shouldExemptAllPullRequestAssignees()
      : this._shouldExemptAllIssueAssignees();
  }

  private _shouldExemptAllIssueAssignees(): boolean {
    if (this._options.exemptAllIssueAssignees === true) {
      this._issueLogger.info(
        `The option ${this._issueLogger.createOptionLink(
          Option.ExemptAllIssueAssignees
        )} is enabled. Any assignee on this $$type will skip the stale process`
      );

      return true;
    } else if (this._options.exemptAllIssueAssignees === false) {
      this._issueLogger.info(
        `The option ${this._issueLogger.createOptionLink(
          Option.ExemptAllIssueAssignees
        )} is disabled. Only some specific assignees on this $$type will skip the stale process`
      );

      return false;
    }

    this._logExemptAllAssigneesOption();

    return this._options.exemptAllAssignees;
  }

  private _shouldExemptAllPullRequestAssignees(): boolean {
    if (this._options.exemptAllPrAssignees === true) {
      this._issueLogger.info(
        `The option ${this._issueLogger.createOptionLink(
          Option.ExemptAllPrAssignees
        )} is enabled. Any assignee on this $$type will skip the stale process`
      );

      return true;
    } else if (this._options.exemptAllPrAssignees === false) {
      this._issueLogger.info(
        `The option ${this._issueLogger.createOptionLink(
          Option.ExemptAllPrAssignees
        )} is disabled. Only some specific assignees on this $$type will skip the stale process`
      );

      return false;
    }

    this._logExemptAllAssigneesOption();

    return this._options.exemptAllAssignees;
  }

  private _logExemptAllAssigneesOption(): void {
    if (this._options.exemptAllAssignees) {
      this._issueLogger.info(
        `The option ${this._issueLogger.createOptionLink(
          Option.ExemptAllAssignees
        )} is enabled. Any assignee on this $$type will skip the stale process`
      );
    } else {
      this._issueLogger.info(
        `The option ${this._issueLogger.createOptionLink(
          Option.ExemptAllAssignees
        )} is disabled. Only some specific assignees on this $$type will skip the stale process`
      );
    }
  }

  private _logSkip(): void {
    this._issueLogger.info(
      LoggerService.white('└──'),
      'Skip the assignees checks'
    );
  }
}
```

## File: `src/classes/exempt-draft-pull-request.ts`
```typescript
import {Option} from '../enums/option';
import {IIssuesProcessorOptions} from '../interfaces/issues-processor-options';
import {IPullRequest} from '../interfaces/pull-request';
import {LoggerService} from '../services/logger.service';
import {Issue} from './issue';
import {IssueLogger} from './loggers/issue-logger';

export class ExemptDraftPullRequest {
  private readonly _options: IIssuesProcessorOptions;
  private readonly _issue: Issue;
  private readonly _issueLogger: IssueLogger;

  constructor(options: Readonly<IIssuesProcessorOptions>, issue: Issue) {
    this._options = options;
    this._issue = issue;
    this._issueLogger = new IssueLogger(issue);
  }

  async shouldExemptDraftPullRequest(
    // keep this for backward compatibility
    // eslint-disable-next-line @typescript-eslint/no-unused-vars
    pullRequestCallback: () => Promise<IPullRequest | undefined | void>
  ): Promise<boolean> {
    if (this._issue.isPullRequest) {
      if (this._options.exemptDraftPr) {
        this._issueLogger.info(
          `The option ${this._issueLogger.createOptionLink(
            Option.ExemptDraftPr
          )} is enabled`
        );

        /* This code was used until Jun 15 2022 - it is unclear why they had to call API for getting pull request
        const pullRequest: IPullRequest | undefined | void =
          await pullRequestCallback();

        if (pullRequest?.draft === true) {
         */
        if (this._issue?.draft === true) {
          this._issueLogger.info(
            LoggerService.white('└──'),
            `Skip the $$type draft checks`
          );

          return true;
        } else {
          this._issueLogger.info(
            LoggerService.white('└──'),
            `Continuing the process for this $$type because it is not a draft`
          );
        }
      }
    }

    return false;
  }
}
```

## File: `src/classes/ignore-updates.spec.ts`
```typescript
/* eslint jest/no-identical-title: "off" */
import {DefaultProcessorOptions} from '../../__tests__/constants/default-processor-options';
import {generateIIssue} from '../../__tests__/functions/generate-iissue';
import {IIssue} from '../interfaces/issue';
import {IIssuesProcessorOptions} from '../interfaces/issues-processor-options';
import {IgnoreUpdates} from './ignore-updates';
import {Issue} from './issue';

describe('IgnoreUpdates', (): void => {
  let ignoreUpdates: IgnoreUpdates;
  let optionsInterface: IIssuesProcessorOptions;
  let issue: Issue;
  let issueInterface: IIssue;

  beforeEach((): void => {
    optionsInterface = {
      ...DefaultProcessorOptions,
      ignoreIssueUpdates: true
    };
    issueInterface = generateIIssue();
  });

  describe('shouldIgnoreUpdates()', (): void => {
    describe('when the given issue is not a pull request', (): void => {
      beforeEach((): void => {
        issueInterface.pull_request = undefined;
      });

      describe('when the given options are configured to reset the stale on updates', (): void => {
        beforeEach((): void => {
          optionsInterface.ignoreUpdates = false;
        });

        describe('when the given options are not configured to reset the issue stale on updates', (): void => {
          beforeEach((): void => {
            delete optionsInterface.ignoreIssueUpdates;
          });

          it('should return false', (): void => {
            expect.assertions(1);
            issue = new Issue(optionsInterface, issueInterface);
            ignoreUpdates = new IgnoreUpdates(optionsInterface, issue);

            const result = ignoreUpdates.shouldIgnoreUpdates();

            expect(result).toStrictEqual(false);
          });
        });

        describe('when the given options are configured to reset the issue stale on updates', (): void => {
          beforeEach((): void => {
            optionsInterface.ignoreIssueUpdates = false;
          });

          it('should return false', (): void => {
            expect.assertions(1);
            issue = new Issue(optionsInterface, issueInterface);
            ignoreUpdates = new IgnoreUpdates(optionsInterface, issue);

            const result = ignoreUpdates.shouldIgnoreUpdates();

            expect(result).toStrictEqual(false);
          });
        });

        describe('when the given options are configured to not reset the issue stale on updates', (): void => {
          beforeEach((): void => {
            optionsInterface.ignoreIssueUpdates = true;
          });

          it('should return true', (): void => {
            expect.assertions(1);
            issue = new Issue(optionsInterface, issueInterface);
            ignoreUpdates = new IgnoreUpdates(optionsInterface, issue);

            const result = ignoreUpdates.shouldIgnoreUpdates();

            expect(result).toStrictEqual(true);
          });
        });
      });

      describe('when the given options are configured to reset the stale on updates', (): void => {
        beforeEach((): void => {
          optionsInterface.ignoreUpdates = true;
        });

        describe('when the given options are not configured to reset the issue stale on updates', (): void => {
          beforeEach((): void => {
            delete optionsInterface.ignoreIssueUpdates;
          });

          it('should return true', (): void => {
            expect.assertions(1);
            issue = new Issue(optionsInterface, issueInterface);
            ignoreUpdates = new IgnoreUpdates(optionsInterface, issue);

            const result = ignoreUpdates.shouldIgnoreUpdates();

            expect(result).toStrictEqual(true);
          });
        });

        describe('when the given options are configured to reset the issue stale on updates', (): void => {
          beforeEach((): void => {
            optionsInterface.ignoreIssueUpdates = false;
          });

          it('should return false', (): void => {
            expect.assertions(1);
            issue = new Issue(optionsInterface, issueInterface);
            ignoreUpdates = new IgnoreUpdates(optionsInterface, issue);

            const result = ignoreUpdates.shouldIgnoreUpdates();

            expect(result).toStrictEqual(false);
          });
        });

        describe('when the given options are configured to not reset the issue stale on updates', (): void => {
          beforeEach((): void => {
            optionsInterface.ignoreIssueUpdates = true;
          });

          it('should return true', (): void => {
            expect.assertions(1);
            issue = new Issue(optionsInterface, issueInterface);
            ignoreUpdates = new IgnoreUpdates(optionsInterface, issue);

            const result = ignoreUpdates.shouldIgnoreUpdates();

            expect(result).toStrictEqual(true);
          });
        });
      });
    });

    describe('when the given issue is a pull request', (): void => {
      beforeEach((): void => {
        issueInterface.pull_request = {};
      });

      describe('when the given options are configured to reset the stale on updates', (): void => {
        beforeEach((): void => {
          optionsInterface.ignoreUpdates = false;
        });

        describe('when the given options are not configured to reset the pull request stale on updates', (): void => {
          beforeEach((): void => {
            delete optionsInterface.ignorePrUpdates;
          });

          it('should return false', (): void => {
            expect.assertions(1);
            issue = new Issue(optionsInterface, issueInterface);
            ignoreUpdates = new IgnoreUpdates(optionsInterface, issue);

            const result = ignoreUpdates.shouldIgnoreUpdates();

            expect(result).toStrictEqual(false);
          });
        });

        describe('when the given options are configured to reset the pull request stale on updates', (): void => {
          beforeEach((): void => {
            optionsInterface.ignorePrUpdates = false;
          });

          it('should return false', (): void => {
            expect.assertions(1);
            issue = new Issue(optionsInterface, issueInterface);
            ignoreUpdates = new IgnoreUpdates(optionsInterface, issue);

            const result = ignoreUpdates.shouldIgnoreUpdates();

            expect(result).toStrictEqual(false);
          });
        });

        describe('when the given options are configured to not reset the pull request stale on updates', (): void => {
          beforeEach((): void => {
            optionsInterface.ignorePrUpdates = true;
          });

          it('should return true', (): void => {
            expect.assertions(1);
            issue = new Issue(optionsInterface, issueInterface);
            ignoreUpdates = new IgnoreUpdates(optionsInterface, issue);

            const result = ignoreUpdates.shouldIgnoreUpdates();

            expect(result).toStrictEqual(true);
          });
        });
      });

      describe('when the given options are configured to not reset the stale on updates', (): void => {
        beforeEach((): void => {
          optionsInterface.ignoreUpdates = true;
        });

        describe('when the given options are not configured to reset the pull request stale on updates', (): void => {
          beforeEach((): void => {
            delete optionsInterface.ignorePrUpdates;
          });

          it('should return true', (): void => {
            expect.assertions(1);
            issue = new Issue(optionsInterface, issueInterface);
            ignoreUpdates = new IgnoreUpdates(optionsInterface, issue);

            const result = ignoreUpdates.shouldIgnoreUpdates();

            expect(result).toStrictEqual(true);
          });
        });

        describe('when the given options are configured to reset the pull request stale on updates', (): void => {
          beforeEach((): void => {
            optionsInterface.ignorePrUpdates = false;
          });

          it('should return false', (): void => {
            expect.assertions(1);
            issue = new Issue(optionsInterface, issueInterface);
            ignoreUpdates = new IgnoreUpdates(optionsInterface, issue);

            const result = ignoreUpdates.shouldIgnoreUpdates();

            expect(result).toStrictEqual(false);
          });
        });

        describe('when the given options are configured to not reset the pull request stale on updates', (): void => {
          beforeEach((): void => {
            optionsInterface.ignorePrUpdates = true;
          });

          it('should return true', (): void => {
            expect.assertions(1);
            issue = new Issue(optionsInterface, issueInterface);
            ignoreUpdates = new IgnoreUpdates(optionsInterface, issue);

            const result = ignoreUpdates.shouldIgnoreUpdates();

            expect(result).toStrictEqual(true);
          });
        });
      });
    });
  });
});
```

## File: `src/classes/ignore-updates.ts`
```typescript
import {Option} from '../enums/option';
import {IIssuesProcessorOptions} from '../interfaces/issues-processor-options';
import {Issue} from './issue';
import {IssueLogger} from './loggers/issue-logger';

export class IgnoreUpdates {
  private readonly _options: IIssuesProcessorOptions;
  private readonly _issue: Issue;
  private readonly _issueLogger: IssueLogger;

  constructor(options: Readonly<IIssuesProcessorOptions>, issue: Issue) {
    this._options = options;
    this._issue = issue;
    this._issueLogger = new IssueLogger(issue);
  }

  shouldIgnoreUpdates(): boolean {
    return this._shouldIgnoreUpdates();
  }

  private _shouldIgnoreUpdates(): boolean {
    return this._issue.isPullRequest
      ? this._shouldIgnorePullRequestUpdates()
      : this._shouldIgnoreIssueUpdates();
  }

  private _shouldIgnorePullRequestUpdates(): boolean {
    if (this._options.ignorePrUpdates === true) {
      this._issueLogger.info(
        `The option ${this._issueLogger.createOptionLink(
          Option.IgnorePrUpdates
        )} is enabled. The stale counter will ignore any updates or comments on this $$type and will use the creation date as a reference ignoring any kind of update`
      );

      return true;
    } else if (this._options.ignorePrUpdates === false) {
      this._issueLogger.info(
        `The option ${this._issueLogger.createOptionLink(
          Option.IgnorePrUpdates
        )} is disabled. The stale counter will take into account updates and comments on this $$type to avoid to stale when there is some update`
      );

      return false;
    }

    this._logIgnoreUpdates();

    return this._options.ignoreUpdates;
  }

  private _shouldIgnoreIssueUpdates(): boolean {
    if (this._options.ignoreIssueUpdates === true) {
      this._issueLogger.info(
        `The option ${this._issueLogger.createOptionLink(
          Option.IgnoreIssueUpdates
        )} is enabled. The stale counter will ignore any updates or comments on this $$type and will use the creation date as a reference ignoring any kind of update`
      );

      return true;
    } else if (this._options.ignoreIssueUpdates === false) {
      this._issueLogger.info(
        `The option ${this._issueLogger.createOptionLink(
          Option.IgnoreIssueUpdates
        )} is disabled. The stale counter will take into account updates and comments on this $$type to avoid to stale when there is some update`
      );

      return false;
    }

    this._logIgnoreUpdates();

    return this._options.ignoreUpdates;
  }

  private _logIgnoreUpdates(): void {
    if (this._options.ignoreUpdates) {
      this._issueLogger.info(
        `The option ${this._issueLogger.createOptionLink(
          Option.IgnoreUpdates
        )} is enabled. The stale counter will ignore any updates or comments on this $$type and will use the creation date as a reference ignoring any kind of update`
      );
    } else {
      this._issueLogger.info(
        `The option ${this._issueLogger.createOptionLink(
          Option.IgnoreUpdates
        )} is disabled. The stale counter will take into account updates and comments on this $$type to avoid to stale when there is some update`
      );
    }
  }
}
```

## File: `src/classes/issue.spec.ts`
```typescript
import {IUserAssignee} from '../interfaces/assignee';
import {IIssue} from '../interfaces/issue';
import {IIssuesProcessorOptions} from '../interfaces/issues-processor-options';
import {ILabel} from '../interfaces/label';
import {IMilestone} from '../interfaces/milestone';
import {Issue} from './issue';

describe('Issue', (): void => {
  let issue: Issue;
  let optionsInterface: IIssuesProcessorOptions;
  let issueInterface: IIssue;

  beforeEach((): void => {
    optionsInterface = {
      ascending: false,
      sortBy: 'created',
      closeIssueLabel: '',
      closeIssueMessage: '',
      closePrLabel: '',
      closePrMessage: '',
      daysBeforeClose: 0,
      daysBeforeIssueClose: 0,
      daysBeforeIssueStale: 0,
      daysBeforePrClose: 0,
      daysBeforePrStale: 0,
      daysBeforeStale: 0,
      debugOnly: false,
      deleteBranch: false,
      exemptIssueLabels: '',
      exemptPrLabels: '',
      onlyLabels: '',
      onlyIssueLabels: '',
      onlyPrLabels: '',
      anyOfLabels: '',
      anyOfIssueLabels: '',
      anyOfPrLabels: '',
      operationsPerRun: 0,
      removeStaleWhenUpdated: false,
      removeIssueStaleWhenUpdated: undefined,
      removePrStaleWhenUpdated: undefined,
      repoToken: '',
      staleIssueMessage: '',
      stalePrMessage: '',
      startDate: undefined,
      stalePrLabel: 'dummy-stale-pr-label',
      staleIssueLabel: 'dummy-stale-issue-label',
      exemptMilestones: '',
      exemptIssueMilestones: '',
      exemptPrMilestones: '',
      exemptAllMilestones: false,
      exemptAllIssueMilestones: undefined,
      exemptAllPrMilestones: undefined,
      exemptAssignees: '',
      exemptIssueAssignees: '',
      exemptPrAssignees: '',
      exemptAllAssignees: false,
      exemptAllIssueAssignees: undefined,
      exemptAllPrAssignees: undefined,
      enableStatistics: false,
      labelsToRemoveWhenStale: '',
      labelsToRemoveWhenUnstale: '',
      labelsToAddWhenUnstale: '',
      ignoreUpdates: false,
      ignoreIssueUpdates: undefined,
      ignorePrUpdates: undefined,
      exemptDraftPr: false,
      closeIssueReason: '',
      includeOnlyAssigned: false
    };
    issueInterface = {
      title: 'dummy-title',
      number: 8,
      created_at: 'dummy-created-at',
      updated_at: 'dummy-updated-at',
      draft: false,
      labels: [
        {
          name: 'dummy-name'
        }
      ],
      pull_request: {},
      state: 'dummy-state',
      locked: false,
      milestone: {
        title: 'dummy-milestone'
      },
      assignees: [
        {
          login: 'dummy-login',
          type: 'User'
        }
      ]
    };
    issue = new Issue(optionsInterface, issueInterface);
  });

  describe('constructor()', (): void => {
    it('should set the title with the given issue title', (): void => {
      expect.assertions(1);

      expect(issue.title).toStrictEqual('dummy-title');
    });

    it('should set the number with the given issue number', (): void => {
      expect.assertions(1);

      expect(issue.number).toStrictEqual(8);
    });

    it('should set the created_at with the given issue created_at', (): void => {
      expect.assertions(1);

      expect(issue.created_at).toStrictEqual('dummy-created-at');
    });

    it('should set the updated_at with the given issue updated_at', (): void => {
      expect.assertions(1);

      expect(issue.updated_at).toStrictEqual('dummy-updated-at');
    });

    it('should set the labels with the given issue labels', (): void => {
      expect.assertions(1);

      expect(issue.labels).toStrictEqual([
        {
          name: 'dummy-name'
        } as ILabel
      ]);
    });

    it('should set the pull_request with the given issue pull_request', (): void => {
      expect.assertions(1);

      expect(issue.pull_request).toStrictEqual({});
    });

    it('should set the state with the given issue state', (): void => {
      expect.assertions(1);

      expect(issue.state).toStrictEqual('dummy-state');
    });

    it('should set the locked with the given issue locked', (): void => {
      expect.assertions(1);

      expect(issue.locked).toStrictEqual(false);
    });

    it('should set the milestone with the given issue milestone', (): void => {
      expect.assertions(1);

      expect(issue.milestone).toStrictEqual({
        title: 'dummy-milestone'
      } as IMilestone);
    });

    it('should set the assignees with the given issue assignees', (): void => {
      expect.assertions(1);

      expect(issue.assignees).toStrictEqual([
        {
          login: 'dummy-login',
          type: 'User'
        } as IUserAssignee
      ]);
    });

    describe('when the given issue does not contains the stale label', (): void => {
      beforeEach((): void => {
        issueInterface.pull_request = undefined;
        issueInterface.labels = [];
        issue = new Issue(optionsInterface, issueInterface);
      });

      it('should set the isStale to false', (): void => {
        expect.assertions(1);

        expect(issue.isStale).toStrictEqual(false);
      });
    });

    describe('when the given issue contains the stale label', (): void => {
      beforeEach((): void => {
        issueInterface.pull_request = undefined;
        issueInterface.labels = [
          {
            name: 'dummy-stale-issue-label'
          } as ILabel
        ];
        issue = new Issue(optionsInterface, issueInterface);
      });

      it('should set the isStale to true', (): void => {
        expect.assertions(1);

        expect(issue.isStale).toStrictEqual(true);
      });
    });
  });

  describe('get isPullRequest', (): void => {
    describe('when the issue pull_request is not set', (): void => {
      beforeEach((): void => {
        issueInterface.pull_request = undefined;
        issue = new Issue(optionsInterface, issueInterface);
      });

      it('should return false', (): void => {
        expect.assertions(1);

        const result = issue.isPullRequest;

        expect(result).toStrictEqual(false);
      });
    });

    describe('when the issue pull_request is set', (): void => {
      beforeEach((): void => {
        issueInterface.pull_request = {};
        issue = new Issue(optionsInterface, issueInterface);
      });

      it('should return true', (): void => {
        expect.assertions(1);

        const result = issue.isPullRequest;

        expect(result).toStrictEqual(true);
      });
    });
  });

  describe('get staleLabel', (): void => {
    describe('when the issue is not a pull request', (): void => {
      beforeEach((): void => {
        issueInterface.pull_request = undefined;
        issue = new Issue(optionsInterface, issueInterface);
      });

      it('should return the issue stale label', (): void => {
        expect.assertions(1);

        const result = issue.staleLabel;

        expect(result).toStrictEqual('dummy-stale-issue-label');
      });
    });

    describe('when the given issue is a pull request', (): void => {
      beforeEach((): void => {
        issueInterface.pull_request = {};
        issue = new Issue(optionsInterface, issueInterface);
      });

      it('should return the pull request stale label', (): void => {
        expect.assertions(1);

        const result = issue.staleLabel;

        expect(result).toStrictEqual('dummy-stale-pr-label');
      });
    });
  });

  describe('get hasAssignees', (): void => {
    describe('when the issue has no assignee', (): void => {
      beforeEach((): void => {
        issueInterface.assignees = [];
        issue = new Issue(optionsInterface, issueInterface);
      });

      it('should return false', (): void => {
        expect.assertions(1);

        const result = issue.hasAssignees;

        expect(result).toStrictEqual(false);
      });
    });

    describe('when the issue has at least one assignee', (): void => {
      beforeEach((): void => {
        issueInterface.assignees = [
          {
            login: 'dummy-login',
            type: 'User'
          }
        ];
        issue = new Issue(optionsInterface, issueInterface);
      });

      it('should return true', (): void => {
        expect.assertions(1);

        const result = issue.hasAssignees;

        expect(result).toStrictEqual(true);
      });
    });
  });
});
```

## File: `src/classes/issue.ts`
```typescript
import {isLabeled} from '../functions/is-labeled';
import {isPullRequest} from '../functions/is-pull-request';
import {Assignee} from '../interfaces/assignee';
import {IIssue, OctokitIssue} from '../interfaces/issue';
import {IIssuesProcessorOptions} from '../interfaces/issues-processor-options';
import {ILabel} from '../interfaces/label';
import {IMilestone} from '../interfaces/milestone';
import {IsoDateString} from '../types/iso-date-string';
import {Operations} from './operations';

export class Issue implements IIssue {
  readonly title: string;
  readonly number: number;
  created_at: IsoDateString;
  updated_at: IsoDateString;
  readonly draft: boolean;
  readonly labels: ILabel[];
  readonly pull_request: object | null | undefined;
  readonly state: string | 'closed' | 'open';
  readonly locked: boolean;
  readonly milestone?: IMilestone | null;
  readonly assignees: Assignee[];
  isStale: boolean;
  markedStaleThisRun: boolean;
  operations = new Operations();
  private readonly _options: IIssuesProcessorOptions;
  readonly issue_type?: string;

  constructor(
    options: Readonly<IIssuesProcessorOptions>,
    issue: Readonly<OctokitIssue> | Readonly<IIssue>
  ) {
    this._options = options;
    this.title = issue.title;
    this.number = issue.number;
    this.created_at = issue.created_at;
    this.updated_at = issue.updated_at;
    this.draft = Boolean(issue.draft);
    this.labels = mapLabels(issue.labels);
    this.pull_request = issue.pull_request;
    this.state = issue.state;
    this.locked = issue.locked;
    this.milestone = issue.milestone;
    this.assignees = issue.assignees || [];
    this.isStale = isLabeled(this, this.staleLabel);
    this.markedStaleThisRun = false;

    if (
      typeof (issue as any).type === 'object' &&
      (issue as any).type !== null
    ) {
      this.issue_type = (issue as any).type.name;
    } else {
      this.issue_type = undefined;
    }
  }

  get isPullRequest(): boolean {
    return isPullRequest(this);
  }

  get staleLabel(): string {
    return this._getStaleLabel();
  }

  get hasAssignees(): boolean {
    return this.assignees.length > 0;
  }

  private _getStaleLabel(): string {
    return this.isPullRequest
      ? this._options.stalePrLabel
      : this._options.staleIssueLabel;
  }
}

function mapLabels(labels: (string | ILabel)[] | ILabel[]): ILabel[] {
  return labels.map(label => {
    if (typeof label == 'string') {
      return {
        name: label
      };
    }
    return label;
  });
}
```

## File: `src/classes/issues-processor.ts`
```typescript
import * as core from '@actions/core';
import {context, getOctokit} from '@actions/github';
import {GitHub} from '@actions/github/lib/utils';
import {Option} from '../enums/option';
import {getHumanizedDate} from '../functions/dates/get-humanized-date';
import {isDateMoreRecentThan} from '../functions/dates/is-date-more-recent-than';
import {isValidDate} from '../functions/dates/is-valid-date';
import {isBoolean} from '../functions/is-boolean';
import {isLabeled} from '../functions/is-labeled';
import {cleanLabel} from '../functions/clean-label';
import {shouldMarkWhenStale} from '../functions/should-mark-when-stale';
import {wordsToList} from '../functions/words-to-list';
import {IComment} from '../interfaces/comment';
import {IIssueEvent} from '../interfaces/issue-event';
import {IIssuesProcessorOptions} from '../interfaces/issues-processor-options';
import {IPullRequest} from '../interfaces/pull-request';
import {Assignees} from './assignees';
import {IgnoreUpdates} from './ignore-updates';
import {ExemptDraftPullRequest} from './exempt-draft-pull-request';
import {Issue} from './issue';
import {IssueLogger} from './loggers/issue-logger';
import {Logger} from './loggers/logger';
import {Milestones} from './milestones';
import {StaleOperations} from './stale-operations';
import {Statistics} from './statistics';
import {LoggerService} from '../services/logger.service';
import {OctokitIssue} from '../interfaces/issue';
import {retry} from '@octokit/plugin-retry';
import {IState} from '../interfaces/state/state';
import {IRateLimit} from '../interfaces/rate-limit';
import {RateLimit} from './rate-limit';
import {getSortField} from '../functions/get-sort-field';

/***
 * Handle processing of issues for staleness/closure.
 */

export class IssuesProcessor {
  private static _updatedSince(timestamp: string, num_days: number): boolean {
    const daysInMillis = 1000 * 60 * 60 * 24 * num_days;
    const millisSinceLastUpdated =
      new Date().getTime() - new Date(timestamp).getTime();

    return millisSinceLastUpdated <= daysInMillis;
  }

  private static _endIssueProcessing(issue: Issue): void {
    const consumedOperationsCount: number =
      issue.operations.getConsumedOperationsCount();

    if (consumedOperationsCount > 0) {
      const issueLogger: IssueLogger = new IssueLogger(issue);

      issueLogger.info(
        LoggerService.cyan(consumedOperationsCount),
        `operation${
          consumedOperationsCount > 1 ? 's' : ''
        } consumed for this $$type`
      );
    }
  }

  private static _getCloseLabelUsedOptionName(
    issue: Readonly<Issue>
  ): Option.ClosePrLabel | Option.CloseIssueLabel {
    return issue.isPullRequest ? Option.ClosePrLabel : Option.CloseIssueLabel;
  }

  readonly operations: StaleOperations;
  readonly client: InstanceType<typeof GitHub>;
  readonly options: IIssuesProcessorOptions;
  readonly staleIssues: Issue[] = [];
  readonly closedIssues: Issue[] = [];
  readonly deletedBranchIssues: Issue[] = [];
  readonly removedLabelIssues: Issue[] = [];
  readonly addedLabelIssues: Issue[] = [];
  readonly addedCloseCommentIssues: Issue[] = [];
  readonly statistics: Statistics | undefined;
  private readonly _logger: Logger = new Logger();
  private readonly state: IState;

  constructor(options: IIssuesProcessorOptions, state: IState) {
    this.options = options;
    this.state = state;
    this.client = getOctokit(this.options.repoToken, undefined, retry);
    this.operations = new StaleOperations(this.options);

    this._logger.info(
      LoggerService.yellow(`Starting the stale action process...`)
    );

    if (this.options.debugOnly) {
      this._logger.warning(
        LoggerService.yellowBright(`Executing in debug mode!`)
      );
      this._logger.warning(
        LoggerService.yellowBright(
          `The debug output will be written but no issues/PRs will be processed.`
        )
      );
    }

    if (this.options.enableStatistics) {
      this.statistics = new Statistics();
    }
  }

  async processIssues(page: Readonly<number> = 1): Promise<number> {
    // get the next batch of issues
    const issues: Issue[] = await this.getIssues(page);

    if (issues.length <= 0) {
      this._logger.info(
        LoggerService.green(`No more issues found to process. Exiting...`)
      );
      this.statistics
        ?.setOperationsCount(this.operations.getConsumedOperationsCount())
        .logStats();

      this.state.reset();

      return this.operations.getRemainingOperationsCount();
    } else {
      this._logger.info(
        `${LoggerService.yellow(
          'Processing the batch of issues '
        )} ${LoggerService.cyan(`#${page}`)} ${LoggerService.yellow(
          ' containing '
        )} ${LoggerService.cyan(issues.length)} ${LoggerService.yellow(
          ` issue${issues.length > 1 ? 's' : ''}...`
        )}`
      );
    }

    const labelsToRemoveWhenStale: string[] = wordsToList(
      this.options.labelsToRemoveWhenStale
    );

    const labelsToAddWhenUnstale: string[] = wordsToList(
      this.options.labelsToAddWhenUnstale
    );
    const labelsToRemoveWhenUnstale: string[] = wordsToList(
      this.options.labelsToRemoveWhenUnstale
    );

    for (const issue of issues.values()) {
      // Stop the processing if no more operations remains
      if (!this.operations.hasRemainingOperations()) {
        break;
      }

      const issueLogger: IssueLogger = new IssueLogger(issue);
      if (this.state.isIssueProcessed(issue)) {
        issueLogger.info(
          '           $$type skipped due being processed during the previous run'
        );
        continue;
      }
      await issueLogger.grouping(`$$type #${issue.number}`, async () => {
        await this.processIssue(
          issue,
          labelsToAddWhenUnstale,
          labelsToRemoveWhenUnstale,
          labelsToRemoveWhenStale
        );
      });
      this.state.addIssueToProcessed(issue);
    }

    if (!this.operations.hasRemainingOperations()) {
      this._logger.warning(
        LoggerService.yellowBright(`No more operations left! Exiting...`)
      );
      this._logger.warning(
        `${LoggerService.yellowBright(
          'If you think that not enough issues were processed you could try to increase the quantity related to the '
        )} ${this._logger.createOptionLink(
          Option.OperationsPerRun
        )} ${LoggerService.yellowBright(
          ' option which is currently set to '
        )} ${LoggerService.cyan(this.options.operationsPerRun)}`
      );
      this.statistics
        ?.setOperationsCount(this.operations.getConsumedOperationsCount())
        .logStats();

      return 0;
    }

    this._logger.info(
      `${LoggerService.green('Batch ')} ${LoggerService.cyan(
        `#${page}`
      )} ${LoggerService.green(' processed.')}`
    );

    // Do the next batch
    return this.processIssues(page + 1);
  }

  async processIssue(
    issue: Issue,
    labelsToAddWhenUnstale: Readonly<string>[],
    labelsToRemoveWhenUnstale: Readonly<string>[],
    labelsToRemoveWhenStale: Readonly<string>[]
  ): Promise<void> {
    this.statistics?.incrementProcessedItemsCount(issue);

    const issueLogger: IssueLogger = new IssueLogger(issue);
    issueLogger.info(
      `Found this $$type last updated at: ${LoggerService.cyan(
        issue.updated_at
      )}`
    );

    // calculate string based messages for this issue
    const staleMessage: string = issue.isPullRequest
      ? this.options.stalePrMessage
      : this.options.staleIssueMessage;
    const closeMessage: string = issue.isPullRequest
      ? this.options.closePrMessage
      : this.options.closeIssueMessage;
    const staleLabel: string = issue.isPullRequest
      ? this.options.stalePrLabel
      : this.options.staleIssueLabel;
    const closeLabel: string = issue.isPullRequest
      ? this.options.closePrLabel
      : this.options.closeIssueLabel;
    const skipMessage = issue.isPullRequest
      ? this.options.stalePrMessage.length === 0
      : this.options.staleIssueMessage.length === 0;
    const daysBeforeStale: number = issue.isPullRequest
      ? this._getDaysBeforePrStale()
      : this._getDaysBeforeIssueStale();

    if (issue.state === 'closed') {
      issueLogger.info(`Skipping this $$type because it is closed`);
      IssuesProcessor._endIssueProcessing(issue);
      return; // Don't process closed issues
    }

    if (issue.locked) {
      issueLogger.info(`Skipping this $$type because it is locked`);
      IssuesProcessor._endIssueProcessing(issue);
      return; // Don't process locked issues
    }

    if (this._isIncludeOnlyAssigned(issue)) {
      issueLogger.info(
        `Skipping this $$type because its assignees list is empty`
      );
      IssuesProcessor._endIssueProcessing(issue);
      return; // If the issue has an 'include-only-assigned' option set, process only issues with nonempty assignees list
    }

    if (this.options.onlyIssueTypes) {
      const allowedTypes = this.options.onlyIssueTypes
        .split(',')
        .map(t => t.trim().toLowerCase())
        .filter(Boolean);
      const issueType = (issue.issue_type || '').toLowerCase();
      if (!allowedTypes.includes(issueType)) {
        issueLogger.info(
          `Skipping this $$type because its type ('${
            issue.issue_type
          }') is not in onlyIssueTypes (${allowedTypes.join(', ')})`
        );
        IssuesProcessor._endIssueProcessing(issue);
        return;
      }
    }

    const onlyLabels: string[] = wordsToList(this._getOnlyLabels(issue));

    if (onlyLabels.length > 0) {
      issueLogger.info(
        `The option ${issueLogger.createOptionLink(
          Option.OnlyLabels
        )} was specified to only process issues and pull requests with all those labels (${LoggerService.cyan(
          onlyLabels.length
        )})`
      );

      const hasAllWhitelistedLabels: boolean = onlyLabels.every(
        (label: Readonly<string>): boolean => {
          return isLabeled(issue, label);
        }
      );

      if (!hasAllWhitelistedLabels) {
        issueLogger.info(
          LoggerService.white('└──'),
          `Skipping this $$type because it doesn't have all the required labels`
        );

        IssuesProcessor._endIssueProcessing(issue);
        return; // Don't process issues without all of the required labels
      } else {
        issueLogger.info(
          LoggerService.white('├──'),
          `All the required labels are present on this $$type`
        );
        issueLogger.info(
          LoggerService.white('└──'),
          `Continuing the process for this $$type`
        );
      }
    } else {
      issueLogger.info(
        `The option ${issueLogger.createOptionLink(
          Option.OnlyLabels
        )} was not specified`
      );
      issueLogger.info(
        LoggerService.white('└──'),
        `Continuing the process for this $$type`
      );
    }

    issueLogger.info(
      `Days before $$type stale: ${LoggerService.cyan(daysBeforeStale)}`
    );

    const shouldMarkAsStale: boolean = shouldMarkWhenStale(daysBeforeStale);

    // Try to remove the close label when not close/locked issue or PR
    await this._removeCloseLabel(issue, closeLabel);

    if (this.options.startDate) {
      const startDate: Date = new Date(this.options.startDate);
      const createdAt: Date = new Date(issue.created_at);

      issueLogger.info(
        `A start date was specified for the ${getHumanizedDate(
          startDate
        )} (${LoggerService.cyan(this.options.startDate)})`
      );

      // Expecting that GitHub will always set a creation date on the issues and PRs
      // But you never know!
      if (!isValidDate(createdAt)) {
        IssuesProcessor._endIssueProcessing(issue);
        core.setFailed(
          new Error(`Invalid issue field: "created_at". Expected a valid date`)
        );
      }

      issueLogger.info(
        `$$type created the ${getHumanizedDate(
          createdAt
        )} (${LoggerService.cyan(issue.created_at)})`
      );

      if (!isDateMoreRecentThan(createdAt, startDate)) {
        issueLogger.info(
          `Skipping this $$type because it was created before the specified start date`
        );

        IssuesProcessor._endIssueProcessing(issue);
        return; // Don't process issues which were created before the start date
      }
    }

    if (issue.isStale) {
      issueLogger.info(`This $$type includes a stale label`);
    } else {
      issueLogger.info(`This $$type does not include a stale label`);
    }

    const exemptLabels: string[] = wordsToList(
      issue.isPullRequest
        ? this.options.exemptPrLabels
        : this.options.exemptIssueLabels
    );

    const hasExemptLabel = exemptLabels.some((exemptLabel: Readonly<string>) =>
      isLabeled(issue, exemptLabel)
    );

    if (hasExemptLabel) {
      issueLogger.info(
        `Skipping this $$type because it contains an exempt label, see ${issueLogger.createOptionLink(
          issue.isPullRequest ? Option.ExemptPrLabels : Option.ExemptIssueLabels
        )} for more details`
      );
      IssuesProcessor._endIssueProcessing(issue);
      return; // Don't process exempt issues
    }

    const anyOfLabels: string[] = wordsToList(this._getAnyOfLabels(issue));

    if (anyOfLabels.length > 0) {
      issueLogger.info(
        `The option ${issueLogger.createOptionLink(
          Option.AnyOfLabels
        )} was specified to only process the issues and pull requests with one of those labels (${LoggerService.cyan(
          anyOfLabels.length
        )})`
      );

      const hasOneOfWhitelistedLabels: boolean = anyOfLabels.some(
        (label: Readonly<string>): boolean => {
          return isLabeled(issue, label);
        }
      );

      if (!hasOneOfWhitelistedLabels) {
        issueLogger.info(
          LoggerService.white('└──'),
          `Skipping this $$type because it doesn't have one of the required labels`
        );
        IssuesProcessor._endIssueProcessing(issue);
        return; // Don't process issues without any of the required labels
      } else {
        issueLogger.info(
          LoggerService.white('├──'),
          `One of the required labels is present on this $$type`
        );
        issueLogger.info(
          LoggerService.white('└──'),
          `Continuing the process for this $$type`
        );
      }
    } else {
      issueLogger.info(
        `The option ${issueLogger.createOptionLink(
          Option.AnyOfLabels
        )} was not specified`
      );
      issueLogger.info(
        LoggerService.white('└──'),
        `Continuing the process for this $$type`
      );
    }

    const milestones: Milestones = new Milestones(this.options, issue);

    if (milestones.shouldExemptMilestones()) {
      IssuesProcessor._endIssueProcessing(issue);
      return; // Don't process exempt milestones
    }

    const assignees: Assignees = new Assignees(this.options, issue);

    if (assignees.shouldExemptAssignees()) {
      IssuesProcessor._endIssueProcessing(issue);
      return; // Don't process exempt assignees
    }

    // Ignore draft PR
    // Note that this check is so far below because it cost one read operation
    // So it's simply better to do all the stale checks which don't cost more operation before this one
    const exemptDraftPullRequest: ExemptDraftPullRequest =
      new ExemptDraftPullRequest(this.options, issue);

    if (
      await exemptDraftPullRequest.shouldExemptDraftPullRequest(
        async (): Promise<IPullRequest | undefined | void> => {
          return this.getPullRequest(issue);
        }
      )
    ) {
      IssuesProcessor._endIssueProcessing(issue);
      return; // Don't process draft PR
    }

    // Determine if this issue needs to be marked stale first
    if (!issue.isStale) {
      issueLogger.info(`This $$type is not stale`);

      const shouldIgnoreUpdates: boolean = new IgnoreUpdates(
        this.options,
        issue
      ).shouldIgnoreUpdates();

      // Should this issue be marked as stale?
      let shouldBeStale: boolean;

      // Ignore the last update and only use the creation date
      if (shouldIgnoreUpdates) {
        shouldBeStale = !IssuesProcessor._updatedSince(
          issue.created_at,
          daysBeforeStale
        );
      }
      // Use the last update to check if we need to stale
      else {
        shouldBeStale = !IssuesProcessor._updatedSince(
          issue.updated_at,
          daysBeforeStale
        );
      }

      if (shouldBeStale) {
        if (shouldIgnoreUpdates) {
          issueLogger.info(
            `This $$type should be stale based on the creation date the ${getHumanizedDate(
              new Date(issue.created_at)
            )} (${LoggerService.cyan(issue.created_at)})`
          );
        } else {
          issueLogger.info(
            `This $$type should be stale based on the last update date the ${getHumanizedDate(
              new Date(issue.updated_at)
            )} (${LoggerService.cyan(issue.updated_at)})`
          );
        }

        if (shouldMarkAsStale) {
          issueLogger.info(
            `This $$type should be marked as stale based on the option ${issueLogger.createOptionLink(
              this._getDaysBeforeStaleUsedOptionName(issue)
            )} (${LoggerService.cyan(daysBeforeStale)})`
          );
          await this._markStale(issue, staleMessage, staleLabel, skipMessage);
          issue.isStale = true; // This issue is now considered stale
          issue.markedStaleThisRun = true;
          issueLogger.info(`This $$type is now stale`);
        } else {
          issueLogger.info(
            `This $$type should not be marked as stale based on the option ${issueLogger.createOptionLink(
              this._getDaysBeforeStaleUsedOptionName(issue)
            )} (${LoggerService.cyan(daysBeforeStale)})`
          );
        }
      } else {
        if (shouldIgnoreUpdates) {
          issueLogger.info(
            `This $$type should not be stale based on the creation date the ${getHumanizedDate(
              new Date(issue.created_at)
            )} (${LoggerService.cyan(issue.created_at)})`
          );
        } else {
          issueLogger.info(
            `This $$type should not be stale based on the last update date the ${getHumanizedDate(
              new Date(issue.updated_at)
            )} (${LoggerService.cyan(issue.updated_at)})`
          );
        }
      }
    }

    // Process the issue if it was marked stale
    if (issue.isStale) {
      issueLogger.info(`This $$type is already stale`);
      await this._processStaleIssue(
        issue,
        staleLabel,
        staleMessage,
        labelsToAddWhenUnstale,
        labelsToRemoveWhenUnstale,
        labelsToRemoveWhenStale,
        closeMessage,
        closeLabel
      );
    }

    IssuesProcessor._endIssueProcessing(issue);
  }

  // Grab comments for an issue since a given date
  async listIssueComments(
    issue: Readonly<Issue>,
    sinceDate: Readonly<string>
  ): Promise<IComment[]> {
    // Find any comments since date on the given issue
    try {
      this._consumeIssueOperation(issue);
      this.statistics?.incrementFetchedItemsCommentsCount();
      const comments = await this.client.rest.issues.listComments({
        owner: context.repo.owner,
        repo: context.repo.repo,
        issue_number: issue.number,
        since: sinceDate
      });
      return comments.data;
    } catch (error) {
      this._logger.error(`List issue comments error: ${error.message}`);
      return Promise.resolve([]);
    }
  }

  // grab issues from github in batches of 100
  async getIssues(page: number): Promise<Issue[]> {
    try {
      this.operations.consumeOperation();
      const issueResult = await this.client.rest.issues.listForRepo({
        owner: context.repo.owner,
        repo: context.repo.repo,
        state: 'open',
        per_page: 100,
        direction: this.options.ascending ? 'asc' : 'desc',
        sort: getSortField(this.options.sortBy),
        page
      });
      this.statistics?.incrementFetchedItemsCount(issueResult.data.length);

      return issueResult.data.map(
        (issue): Issue =>
          new Issue(this.options, issue as Readonly<OctokitIssue>)
      );
    } catch (error) {
      throw Error(`Getting issues was blocked by the error: ${error.message}`);
    }
  }

  // returns the creation date of a given label on an issue (or nothing if no label existed)
  ///see https://developer.github.com/v3/activity/events/
  async getLabelCreationDate(
    issue: Issue,
    label: string
  ): Promise<{creationDate?: string; events: IIssueEvent[]}> {
    const issueLogger: IssueLogger = new IssueLogger(issue);

    issueLogger.info(`Checking for label on this $$type`);

    this._consumeIssueOperation(issue);
    this.statistics?.incrementFetchedItemsEventsCount();
    const options = this.client.rest.issues.listEvents.endpoint.merge({
      owner: context.repo.owner,
      repo: context.repo.repo,
      per_page: 100,
      issue_number: issue.number
    });

    const events: IIssueEvent[] = await this.client.paginate(options);

    const reversedEvents = events.reverse();

    const staleLabeledEvent = reversedEvents.find(
      event =>
        event.event === 'labeled' &&
        cleanLabel(event.label.name) === cleanLabel(label)
    );

    if (!staleLabeledEvent) {
      // Must be old rather than labeled
      return {creationDate: undefined, events};
    }

    return {creationDate: staleLabeledEvent.created_at, events};
  }

  protected async hasOnlyStaleLabelingEventsSince(
    issue: Issue,
    sinceDate: string,
    staleLabel: string,
    events: IIssueEvent[]
  ): Promise<boolean> {
    const issueLogger: IssueLogger = new IssueLogger(issue);

    issueLogger.info(
      `Checking if only stale label added events on $$type since: ${LoggerService.cyan(
        sinceDate
      )}`
    );

    if (!sinceDate) {
      return false;
    }

    const sinceTimestamp = new Date(sinceDate).getTime();
    if (Number.isNaN(sinceTimestamp)) {
      return false;
    }

    const relevantEvents = events.filter(event => {
      const eventTimestamp = new Date(event.created_at).getTime();
      return !Number.isNaN(eventTimestamp) && eventTimestamp >= sinceTimestamp;
    });

    if (relevantEvents.length === 0) {
      return false;
    }

    return relevantEvents.every(event => {
      if (event.event !== 'labeled') {
        return false;
      }

      return cleanLabel(event.label.name) === cleanLabel(staleLabel);
    });
  }

  async getPullRequest(issue: Issue): Promise<IPullRequest | undefined | void> {
    const issueLogger: IssueLogger = new IssueLogger(issue);

    try {
      this._consumeIssueOperation(issue);
      this.statistics?.incrementFetchedPullRequestsCount();

      const pullRequest = await this.client.rest.pulls.get({
        owner: context.repo.owner,
        repo: context.repo.repo,
        pull_number: issue.number
      });

      return pullRequest.data;
    } catch (error) {
      issueLogger.error(`Error when getting this $$type: ${error.message}`);
    }
  }

  async getRateLimit(): Promise<IRateLimit | undefined> {
    const logger: Logger = new Logger();

    try {
      const rateLimitResult = await this.client.rest.rateLimit.get();
      return new RateLimit(rateLimitResult.data.rate);
    } catch (error: unknown) {
      const status = (error as {status?: number})?.status;
      const message = (error as {message?: string})?.message ?? String(error);

      if (status === 404 && message.includes('Rate limiting is not enabled')) {
        logger.warning(
          'Rate limiting is not enabled on this instance. Proceeding without rate limit checks.'
        );
        return undefined;
      }

      logger.error(`Error when getting rateLimit: ${message}`);
    }
  }

  // handle all of the stale issue logic when we find a stale issue
  private async _processStaleIssue(
    issue: Issue,
    staleLabel: string,
    staleMessage: string,
    labelsToAddWhenUnstale: Readonly<string>[],
    labelsToRemoveWhenUnstale: Readonly<string>[],
    labelsToRemoveWhenStale: Readonly<string>[],
    closeMessage?: string,
    closeLabel?: string
  ) {
    const issueLogger: IssueLogger = new IssueLogger(issue);
    const {creationDate, events} = await this.getLabelCreationDate(
      issue,
      staleLabel
    );
    const markedStaleOn: string = creationDate || issue.updated_at;
    issueLogger.info(
      `$$type marked stale on: ${LoggerService.cyan(markedStaleOn)}`
    );

    const issueHasCommentsSinceStale: boolean = await this._hasCommentsSince(
      issue,
      markedStaleOn,
      staleMessage
    );
    issueLogger.info(
      `$$type has been commented on: ${LoggerService.cyan(
        issueHasCommentsSinceStale
      )}`
    );

    const daysBeforeClose: number = issue.isPullRequest
      ? this._getDaysBeforePrClose()
      : this._getDaysBeforeIssueClose();

    issueLogger.info(
      `Days before $$type close: ${LoggerService.cyan(daysBeforeClose)}`
    );

    const shouldRemoveStaleWhenUpdated: boolean =
      this._shouldRemoveStaleWhenUpdated(issue);

    issueLogger.info(
      `The option ${issueLogger.createOptionLink(
        this._getRemoveStaleWhenUpdatedUsedOptionName(issue)
      )} is: ${LoggerService.cyan(shouldRemoveStaleWhenUpdated)}`
    );

    if (shouldRemoveStaleWhenUpdated) {
      issueLogger.info(`The stale label should not be removed`);
    } else {
      issueLogger.info(
        `The stale label should be removed if all conditions met`
      );
    }

    if (issue.markedStaleThisRun) {
      issueLogger.info(`marked stale this run, so don't check for updates`);
      await this._removeLabelsOnStatusTransition(
        issue,
        labelsToRemoveWhenStale,
        Option.LabelsToRemoveWhenStale
      );
    }

    // The issue.updated_at and markedStaleOn are not always exactly in sync (they can be off by a second or 2)
    // isDateMoreRecentThan makes sure they are not the same date within a certain tolerance (15 seconds in this case)
    let issueHasUpdateSinceStale = isDateMoreRecentThan(
      new Date(issue.updated_at),
      new Date(markedStaleOn),
      15
    );

    // Check if the only update was the stale label being added
    if (
      issueHasUpdateSinceStale &&
      shouldRemoveStaleWhenUpdated &&
      !issue.markedStaleThisRun
    ) {
      const onlyStaleLabelAdded = await this.hasOnlyStaleLabelingEventsSince(
        issue,
        markedStaleOn,
        staleLabel,
        events
      );

      if (onlyStaleLabelAdded) {
        issueHasUpdateSinceStale = false;
        issueLogger.info(
          `Ignoring $$type update since only the stale label was added`
        );
      }
    }

    issueLogger.info(
      `$$type has been updated since it was marked stale: ${LoggerService.cyan(
        issueHasUpdateSinceStale
      )}`
    );

    // Should we un-stale this issue?
    if (
      shouldRemoveStaleWhenUpdated &&
      (issueHasUpdateSinceStale || issueHasCommentsSinceStale) &&
      !issue.markedStaleThisRun
    ) {
      issueLogger.info(
        `Remove the stale label since the $$type has been updated and the workflow should remove the stale label when updated`
      );
      await this._removeStaleLabel(issue, staleLabel);

      // Are there labels to remove or add when an issue is no longer stale?
      await this._removeLabelsOnStatusTransition(
        issue,
        labelsToRemoveWhenUnstale,
        Option.LabelsToRemoveWhenUnstale
      );
      await this._addLabelsWhenUnstale(issue, labelsToAddWhenUnstale);

      issueLogger.info(`Skipping the process since the $$type is now un-stale`);

      return; // Nothing to do because it is no longer stale
    }

    // Now start closing logic
    if (daysBeforeClose < 0) {
      return; // Nothing to do because we aren't closing stale issues
    }

    const issueHasUpdateInCloseWindow: boolean = IssuesProcessor._updatedSince(
      issue.updated_at,
      daysBeforeClose
    );
    issueLogger.info(
      `$$type has been updated in the last ${daysBeforeClose} days: ${LoggerService.cyan(
        issueHasUpdateInCloseWindow
      )}`
    );

    if (!issueHasCommentsSinceStale && !issueHasUpdateInCloseWindow) {
      issueLogger.info(
        `Closing $$type because it was last updated on: ${LoggerService.cyan(
          issue.updated_at
        )}`
      );
      await this._closeIssue(issue, closeMessage, closeLabel);

      if (this.options.deleteBranch && issue.pull_request) {
        issueLogger.info(
          `Deleting the branch since the option ${issueLogger.createOptionLink(
            Option.DeleteBranch
          )} is enabled`
        );
        await this._deleteBranch(issue);
        this.deletedBranchIssues.push(issue);
      }
    } else {
      issueLogger.info(
        `Stale $$type is not old enough to close yet (hasComments? ${issueHasCommentsSinceStale}, hasUpdate? ${issueHasUpdateInCloseWindow})`
      );
    }
  }

  // checks to see if a given issue is still stale (has had activity on it)
  private async _hasCommentsSince(
    issue: Issue,
    sinceDate: string,
    staleMessage: string
  ): Promise<boolean> {
    const issueLogger: IssueLogger = new IssueLogger(issue);

    issueLogger.info(
      `Checking for comments on $$type since: ${LoggerService.cyan(sinceDate)}`
    );

    if (!sinceDate) {
      return true;
    }

    // find any comments since the date
    const comments = await this.listIssueComments(issue, sinceDate);

    const filteredComments = comments.filter(
      comment =>
        comment.user?.type === 'User' &&
        comment.body?.toLowerCase() !== staleMessage.toLowerCase()
    );

    issueLogger.info(
      `Comments that are not the stale comment or another bot: ${LoggerService.cyan(
        filteredComments.length
      )}`
    );

    // if there are any user comments returned
    return filteredComments.length > 0;
  }

  // Mark an issue as stale with a comment and a label
  private async _markStale(
    issue: Issue,
    staleMessage: string,
    staleLabel: string,
    skipMessage: boolean
  ): Promise<void> {
    const issueLogger: IssueLogger = new IssueLogger(issue);

    issueLogger.info(`Marking this $$type as stale`);
    this.staleIssues.push(issue);

    // if the issue is being marked stale, the updated date should be changed to right now
    // so that close calculations work correctly
    const newUpdatedAtDate: Date = new Date();
    issue.updated_at = newUpdatedAtDate.toString();

    if (!skipMessage) {
      try {
        this._consumeIssueOperation(issue);
        this.statistics?.incrementAddedItemsComment(issue);

        if (!this.options.debugOnly) {
          await this.client.rest.issues.createComment({
            owner: context.repo.owner,
            repo: context.repo.repo,
            issue_number: issue.number,
            body: staleMessage
          });
        }
      } catch (error) {
        issueLogger.error(`Error when creating a comment: ${error.message}`);
      }
    }

    try {
      this._consumeIssueOperation(issue);
      this.statistics?.incrementAddedItemsLabel(issue);
      this.statistics?.incrementStaleItemsCount(issue);

      if (!this.options.debugOnly) {
        await this.client.rest.issues.addLabels({
          owner: context.repo.owner,
          repo: context.repo.repo,
          issue_number: issue.number,
          labels: [staleLabel]
        });
      }
    } catch (error) {
      issueLogger.error(`Error when adding a label: ${error.message}`);
    }
  }

  // Close an issue based on staleness
  private async _closeIssue(
    issue: Issue,
    closeMessage?: string,
    closeLabel?: string
  ): Promise<void> {
    const issueLogger: IssueLogger = new IssueLogger(issue);

    issueLogger.info(`Closing $$type for being stale`);
    this.closedIssues.push(issue);

    if (closeMessage) {
      try {
        this._consumeIssueOperation(issue);
        this.statistics?.incrementAddedItemsComment(issue);
        this.addedCloseCommentIssues.push(issue);

        if (!this.options.debugOnly) {
          await this.client.rest.issues.createComment({
            owner: context.repo.owner,
            repo: context.repo.repo,
            issue_number: issue.number,
            body: closeMessage
          });
        }
      } catch (error) {
        issueLogger.error(`Error when creating a comment: ${error.message}`);
      }
    }

    if (closeLabel) {
      try {
        this._consumeIssueOperation(issue);
        this.statistics?.incrementAddedItemsLabel(issue);

        if (!this.options.debugOnly) {
          await this.client.rest.issues.addLabels({
            owner: context.repo.owner,
            repo: context.repo.repo,
            issue_number: issue.number,
            labels: [closeLabel]
          });
        }
      } catch (error) {
        issueLogger.error(`Error when adding a label: ${error.message}`);
      }
    }

    try {
      this._consumeIssueOperation(issue);
      this.statistics?.incrementClosedItemsCount(issue);

      if (!this.options.debugOnly) {
        await this.client.rest.issues.update({
          owner: context.repo.owner,
          repo: context.repo.repo,
          issue_number: issue.number,
          state: 'closed',
          state_reason: (this.options.closeIssueReason || undefined) as
            | 'completed'
            | 'reopened'
            | 'not_planned'
            | null
            | undefined
        });
      }
    } catch (error) {
      issueLogger.error(`Error when updating this $$type: ${error.message}`);
    }
  }

  // Delete the branch on closed pull request
  private async _deleteBranch(issue: Issue): Promise<void> {
    const issueLogger: IssueLogger = new IssueLogger(issue);

    issueLogger.info(`Delete
    branch from closed $
    $type
    -
    ${issue.title}`);

    const pullRequest: IPullRequest | undefined | void =
      await this.getPullRequest(issue);

    if (!pullRequest) {
      issueLogger.info(
        `Not deleting this branch as no pull request was found for this $$type`
      );
      return;
    }

    const branch = pullRequest.head.ref;

    if (
      pullRequest.head.repo === null ||
      pullRequest.head.repo.full_name ===
        `${context.repo.owner}/${context.repo.repo}`
    ) {
      issueLogger.info(
        `Deleting the branch "${LoggerService.cyan(branch)}" from closed $$type`
      );

      try {
        this._consumeIssueOperation(issue);
        this.statistics?.incrementDeletedBranchesCount();

        if (!this.options.debugOnly) {
          await this.client.rest.git.deleteRef({
            owner: context.repo.owner,
            repo: context.repo.repo,
            ref: `heads/${branch}`
          });
        }
      } catch (error) {
        issueLogger.error(
          `Error when deleting the branch "${LoggerService.cyan(
            branch
          )}" from $$type: ${error.message}`
        );
      }
    } else {
      issueLogger.warning(
        `Deleting the branch "${LoggerService.cyan(
          branch
        )}" has skipped because it belongs to other repo ${
          pullRequest.head.repo.full_name
        }`
      );
    }
  }

  // Remove a label from an issue or a pull request
  private async _removeLabel(
    issue: Issue,
    label: string,
    isSubStep: Readonly<boolean> = false
  ): Promise<void> {
    const issueLogger: IssueLogger = new IssueLogger(issue);

    issueLogger.info(
      `${
        isSubStep ? LoggerService.white('├── ') : ''
      }Removing the label "${LoggerService.cyan(label)}" from this $$type...`
    );
    this.removedLabelIssues.push(issue);

    try {
      this._consumeIssueOperation(issue);
      this.statistics?.incrementDeletedItemsLabelsCount(issue);

      if (!this.options.debugOnly) {
        await this.client.rest.issues.removeLabel({
          owner: context.repo.owner,
          repo: context.repo.repo,
          issue_number: issue.number,
          name: label
        });
      }

      issueLogger.info(
        `${
          isSubStep ? LoggerService.white('└── ') : ''
        }The label "${LoggerService.cyan(label)}" was removed`
      );
    } catch (error) {
      issueLogger.error(
        `${
          isSubStep ? LoggerService.white('└── ') : ''
        }Error when removing the label: "${LoggerService.cyan(error.message)}"`
      );
    }
  }

  private _getDaysBeforeIssueStale(): number {
    return isNaN(this.options.daysBeforeIssueStale)
      ? this.options.daysBeforeStale
      : this.options.daysBeforeIssueStale;
  }

  private _getDaysBeforePrStale(): number {
    return isNaN(this.options.daysBeforePrStale)
      ? this.options.daysBeforeStale
      : this.options.daysBeforePrStale;
  }

  private _getDaysBeforeIssueClose(): number {
    return isNaN(this.options.daysBeforeIssueClose)
      ? this.options.daysBeforeClose
      : this.options.daysBeforeIssueClose;
  }

  private _getDaysBeforePrClose(): number {
    return isNaN(this.options.daysBeforePrClose)
      ? this.options.daysBeforeClose
      : this.options.daysBeforePrClose;
  }

  private _getOnlyLabels(issue: Issue): string {
    if (issue.isPullRequest) {
      if (this.options.onlyPrLabels !== '') {
        return this.options.onlyPrLabels;
      }
    } else {
      if (this.options.onlyIssueLabels !== '') {
        return this.options.onlyIssueLabels;
      }
    }

    return this.options.onlyLabels;
  }

  private _isIncludeOnlyAssigned(issue: Issue): boolean {
    return this.options.includeOnlyAssigned && !issue.hasAssignees;
  }

  private _getAnyOfLabels(issue: Issue): string {
    if (issue.isPullRequest) {
      if (this.options.anyOfPrLabels !== '') {
        return this.options.anyOfPrLabels;
      }
    } else {
      if (this.options.anyOfIssueLabels !== '') {
        return this.options.anyOfIssueLabels;
      }
    }

    return this.options.anyOfLabels;
  }

  private _shouldRemoveStaleWhenUpdated(issue: Issue): boolean {
    if (issue.isPullRequest) {
      if (isBoolean(this.options.removePrStaleWhenUpdated)) {
        return this.options.removePrStaleWhenUpdated;
      }

      return this.options.removeStaleWhenUpdated;
    }

    if (isBoolean(this.options.removeIssueStaleWhenUpdated)) {
      return this.options.removeIssueStaleWhenUpdated;
    }

    return this.options.removeStaleWhenUpdated;
  }

  private async _removeLabelsOnStatusTransition(
    issue: Issue,
    removeLabels: Readonly<string>[],
    staleStatus: Option
  ): Promise<void> {
    if (!removeLabels.length) {
      return;
    }

    const issueLogger: IssueLogger = new IssueLogger(issue);

    issueLogger.info(
      `Removing all the labels specified via the ${this._logger.createOptionLink(
        staleStatus
      )} option.`
    );

    for (const label of removeLabels.values()) {
      await this._removeLabel(issue, label);
    }
  }

  private async _addLabelsWhenUnstale(
    issue: Issue,
    labelsToAdd: Readonly<string>[]
  ): Promise<void> {
    if (!labelsToAdd.length) {
      return;
    }

    const issueLogger: IssueLogger = new IssueLogger(issue);

    issueLogger.info(
      `Adding all the labels specified via the ${this._logger.createOptionLink(
        Option.LabelsToAddWhenUnstale
      )} option.`
    );

    this.addedLabelIssues.push(issue);

    try {
      this._consumeIssueOperation(issue);
      this.statistics?.incrementAddedItemsLabel(issue);
      if (!this.options.debugOnly) {
        await this.client.rest.issues.addLabels({
          owner: context.repo.owner,
          repo: context.repo.repo,
          issue_number: issue.number,
          labels: labelsToAdd
        });
      }
    } catch (error) {
      this._logger.error(
        `Error when adding labels after updated from stale: ${error.message}`
      );
    }
  }

  private async _removeStaleLabel(
    issue: Issue,
    staleLabel: Readonly<string>
  ): Promise<void> {
    const issueLogger: IssueLogger = new IssueLogger(issue);

    issueLogger.info(
      `The $$type is no longer stale. Removing the stale label...`
    );

    await this._removeLabel(issue, staleLabel);
    this.statistics?.incrementUndoStaleItemsCount(issue);
  }

  private async _removeCloseLabel(
    issue: Issue,
    closeLabel: Readonly<string | undefined>
  ): Promise<void> {
    const issueLogger: IssueLogger = new IssueLogger(issue);

    issueLogger.info(
      `The $$type is not closed nor locked. Trying to remove the close label...`
    );

    if (!closeLabel) {
      issueLogger.info(
        LoggerService.white('├──'),
        `The ${issueLogger.createOptionLink(
          IssuesProcessor._getCloseLabelUsedOptionName(issue)
        )} option was not set`
      );
      issueLogger.info(
        LoggerService.white('└──'),
        `Skipping the removal of the close label`
      );

      return Promise.resolve();
    }

    if (isLabeled(issue, closeLabel)) {
      issueLogger.info(
        LoggerService.white('├──'),
        `The $$type has a close label "${LoggerService.cyan(
          closeLabel
        )}". Removing the close label...`
      );

      await this._removeLabel(issue, closeLabel, true);
      this.statistics?.incrementDeletedCloseItemsLabelsCount(issue);
    } else {
      issueLogger.info(
        LoggerService.white('└──'),
        `There is no close label on this $$type. Skipping`
      );

      return Promise.resolve();
    }
  }

  private _consumeIssueOperation(issue: Readonly<Issue>): void {
    this.operations.consumeOperation();
    issue.operations.consumeOperation();
  }

  private _getDaysBeforeStaleUsedOptionName(
    issue: Readonly<Issue>
  ):
    | Option.DaysBeforeStale
    | Option.DaysBeforeIssueStale
    | Option.DaysBeforePrStale {
    return issue.isPullRequest
      ? this._getDaysBeforePrStaleUsedOptionName()
      : this._getDaysBeforeIssueStaleUsedOptionName();
  }

  private _getDaysBeforeIssueStaleUsedOptionName():
    | Option.DaysBeforeStale
    | Option.DaysBeforeIssueStale {
    return isNaN(this.options.daysBeforeIssueStale)
      ? Option.DaysBeforeStale
      : Option.DaysBeforeIssueStale;
  }

  private _getDaysBeforePrStaleUsedOptionName():
    | Option.DaysBeforeStale
    | Option.DaysBeforePrStale {
    return isNaN(this.options.daysBeforePrStale)
      ? Option.DaysBeforeStale
      : Option.DaysBeforePrStale;
  }

  private _getRemoveStaleWhenUpdatedUsedOptionName(
    issue: Readonly<Issue>
  ):
    | Option.RemovePrStaleWhenUpdated
    | Option.RemoveStaleWhenUpdated
    | Option.RemoveIssueStaleWhenUpdated {
    if (issue.isPullRequest) {
      if (isBoolean(this.options.removePrStaleWhenUpdated)) {
        return Option.RemovePrStaleWhenUpdated;
      }

      return Option.RemoveStaleWhenUpdated;
    }

    if (isBoolean(this.options.removeIssueStaleWhenUpdated)) {
      return Option.RemoveIssueStaleWhenUpdated;
    }

    return Option.RemoveStaleWhenUpdated;
  }
}
```

## File: `src/classes/milestones.spec.ts`
```typescript
import {DefaultProcessorOptions} from '../../__tests__/constants/default-processor-options';
import {generateIIssue} from '../../__tests__/functions/generate-iissue';
import {IIssue} from '../interfaces/issue';
import {IIssuesProcessorOptions} from '../interfaces/issues-processor-options';
import {Issue} from './issue';
import {Milestones} from './milestones';

describe('Milestones', (): void => {
  let milestones: Milestones;
  let optionsInterface: IIssuesProcessorOptions;
  let issue: Issue;
  let issueInterface: IIssue;

  beforeEach((): void => {
    optionsInterface = {...DefaultProcessorOptions, exemptAllMilestones: false};
    issueInterface = generateIIssue();
  });

  describe('shouldExemptMilestones()', (): void => {
    describe('when the given issue is not a pull request', (): void => {
      beforeEach((): void => {
        issueInterface.pull_request = undefined;
      });

      describe('when the given options are not configured to exempt a milestone', (): void => {
        beforeEach((): void => {
          optionsInterface.exemptMilestones = '';
        });

        describe('when the given options are not configured to exempt an issue milestone', (): void => {
          beforeEach((): void => {
            optionsInterface.exemptIssueMilestones = '';
          });

          describe('when the given issue does not have a milestone', (): void => {
            beforeEach((): void => {
              issueInterface.milestone = undefined;
            });

            it('should return false', (): void => {
              expect.assertions(1);
              issue = new Issue(optionsInterface, issueInterface);
              milestones = new Milestones(optionsInterface, issue);

              const result = milestones.shouldExemptMilestones();

              expect(result).toStrictEqual(false);
            });
          });

          describe('when the given issue does have a milestone', (): void => {
            beforeEach((): void => {
              issueInterface.milestone = {
                title: 'dummy-title'
              };
            });

            it('should return false', (): void => {
              expect.assertions(1);
              issue = new Issue(optionsInterface, issueInterface);
              milestones = new Milestones(optionsInterface, issue);

              const result = milestones.shouldExemptMilestones();

              expect(result).toStrictEqual(false);
            });
          });
        });

        describe('when the given options are configured to exempt an issue milestone', (): void => {
          beforeEach((): void => {
            optionsInterface.exemptIssueMilestones =
              'dummy-exempt-issue-milestone';
          });

          describe('when the given issue does not have a milestone', (): void => {
            beforeEach((): void => {
              issueInterface.milestone = undefined;
            });

            it('should return false', (): void => {
              expect.assertions(1);
              issue = new Issue(optionsInterface, issueInterface);
              milestones = new Milestones(optionsInterface, issue);

              const result = milestones.shouldExemptMilestones();

              expect(result).toStrictEqual(false);
            });
          });

          describe('when the given issue does have a milestone different than the exempt issue milestone', (): void => {
            beforeEach((): void => {
              issueInterface.milestone = {
                title: 'dummy-title'
              };
            });

            it('should return false', (): void => {
              expect.assertions(1);
              issue = new Issue(optionsInterface, issueInterface);
              milestones = new Milestones(optionsInterface, issue);

              const result = milestones.shouldExemptMilestones();

              expect(result).toStrictEqual(false);
            });
          });

          describe('when the given issue does have a milestone equaling the exempt issue milestone', (): void => {
            beforeEach((): void => {
              issueInterface.milestone = {
                title: 'dummy-exempt-issue-milestone'
              };
            });

            it('should return true', (): void => {
              expect.assertions(1);
              issue = new Issue(optionsInterface, issueInterface);
              milestones = new Milestones(optionsInterface, issue);

              const result = milestones.shouldExemptMilestones();

              expect(result).toStrictEqual(true);
            });
          });
        });
      });

      describe('when the given options are configured to exempt a milestone', (): void => {
        beforeEach((): void => {
          optionsInterface.exemptMilestones = 'dummy-exempt-milestone';
        });

        describe('when the given options are not configured to exempt an issue milestone', (): void => {
          beforeEach((): void => {
            optionsInterface.exemptIssueMilestones = '';
          });

          describe('when the given issue does not have a milestone', (): void => {
            beforeEach((): void => {
              issueInterface.milestone = undefined;
            });

            it('should return false', (): void => {
              expect.assertions(1);
              issue = new Issue(optionsInterface, issueInterface);
              milestones = new Milestones(optionsInterface, issue);

              const result = milestones.shouldExemptMilestones();

              expect(result).toStrictEqual(false);
            });
          });

          describe('when the given issue does have a milestone different than the exempt milestone', (): void => {
            beforeEach((): void => {
              issueInterface.milestone = {
                title: 'dummy-title'
              };
            });

            it('should return false', (): void => {
              expect.assertions(1);
              issue = new Issue(optionsInterface, issueInterface);
              milestones = new Milestones(optionsInterface, issue);

              const result = milestones.shouldExemptMilestones();

              expect(result).toStrictEqual(false);
            });
          });

          describe('when the given issue does have a milestone equaling the exempt milestone', (): void => {
            beforeEach((): void => {
              issueInterface.milestone = {
                title: 'dummy-exempt-milestone'
              };
            });

            it('should return true', (): void => {
              expect.assertions(1);
              issue = new Issue(optionsInterface, issueInterface);
              milestones = new Milestones(optionsInterface, issue);

              const result = milestones.shouldExemptMilestones();

              expect(result).toStrictEqual(true);
            });
          });
        });

        describe('when the given options are configured to exempt an issue milestone', (): void => {
          beforeEach((): void => {
            optionsInterface.exemptIssueMilestones =
              'dummy-exempt-issue-milestone';
          });

          describe('when the given issue does not have a milestone', (): void => {
            beforeEach((): void => {
              issueInterface.milestone = undefined;
            });

            it('should return false', (): void => {
              expect.assertions(1);
              issue = new Issue(optionsInterface, issueInterface);
              milestones = new Milestones(optionsInterface, issue);

              const result = milestones.shouldExemptMilestones();

              expect(result).toStrictEqual(false);
            });
          });

          describe('when the given issue does have a milestone different than the exempt issue milestone', (): void => {
            beforeEach((): void => {
              issueInterface.milestone = {
                title: 'dummy-title'
              };
            });

            it('should return false', (): void => {
              expect.assertions(1);
              issue = new Issue(optionsInterface, issueInterface);
              milestones = new Milestones(optionsInterface, issue);

              const result = milestones.shouldExemptMilestones();

              expect(result).toStrictEqual(false);
            });
          });

          describe('when the given issue does have a milestone equaling the exempt issue milestone', (): void => {
            beforeEach((): void => {
              issueInterface.milestone = {
                title: 'dummy-exempt-issue-milestone'
              };
            });

            it('should return true', (): void => {
              expect.assertions(1);
              issue = new Issue(optionsInterface, issueInterface);
              milestones = new Milestones(optionsInterface, issue);

              const result = milestones.shouldExemptMilestones();

              expect(result).toStrictEqual(true);
            });
          });

          describe('when the given issue does have a milestone different than the exempt milestone', (): void => {
            beforeEach((): void => {
              issueInterface.milestone = {
                title: 'dummy-title'
              };
            });

            it('should return false', (): void => {
              expect.assertions(1);
              issue = new Issue(optionsInterface, issueInterface);
              milestones = new Milestones(optionsInterface, issue);

              const result = milestones.shouldExemptMilestones();

              expect(result).toStrictEqual(false);
            });
          });

          describe('when the given issue does have a milestone equaling the exempt milestone', (): void => {
            beforeEach((): void => {
              issueInterface.milestone = {
                title: 'dummy-exempt-milestone'
              };
            });

            it('should return false', (): void => {
              expect.assertions(1);
              issue = new Issue(optionsInterface, issueInterface);
              milestones = new Milestones(optionsInterface, issue);

              const result = milestones.shouldExemptMilestones();

              expect(result).toStrictEqual(false);
            });
          });
        });
      });

      describe('when the given options are configured to exempt all milestones', (): void => {
        beforeEach((): void => {
          optionsInterface.exemptAllMilestones = true;
        });

        describe('when the given issue does not have a milestone', (): void => {
          beforeEach((): void => {
            issueInterface.milestone = undefined;
          });

          it('should return false', (): void => {
            expect.assertions(1);
            issue = new Issue(optionsInterface, issueInterface);
            milestones = new Milestones(optionsInterface, issue);

            const result = milestones.shouldExemptMilestones();

            expect(result).toStrictEqual(false);
          });
        });

        describe('when the given issue does have a milestone', (): void => {
          beforeEach((): void => {
            issueInterface.milestone = {
              title: 'dummy-exempt-issue-milestone'
            };
          });

          it('should return true', (): void => {
            expect.assertions(1);
            issue = new Issue(optionsInterface, issueInterface);
            milestones = new Milestones(optionsInterface, issue);

            const result = milestones.shouldExemptMilestones();

            expect(result).toStrictEqual(true);
          });
        });

        describe('when the given options are not configured to exempt all issue milestones', (): void => {
          beforeEach((): void => {
            optionsInterface.exemptAllIssueMilestones = false;
          });

          describe('when the given issue does not have a milestone', (): void => {
            beforeEach((): void => {
              issueInterface.milestone = undefined;
            });

            it('should return false', (): void => {
              expect.assertions(1);
              issue = new Issue(optionsInterface, issueInterface);
              milestones = new Milestones(optionsInterface, issue);

              const result = milestones.shouldExemptMilestones();

              expect(result).toStrictEqual(false);
            });
          });

          describe('when the given issue does have a milestone', (): void => {
            beforeEach((): void => {
              issueInterface.milestone = {
                title: 'dummy-exempt-milestone'
              };
            });

            it('should return false', (): void => {
              expect.assertions(1);
              issue = new Issue(optionsInterface, issueInterface);
              milestones = new Milestones(optionsInterface, issue);

              const result = milestones.shouldExemptMilestones();

              expect(result).toStrictEqual(false);
            });
          });
        });

        describe('when the given options are configured to exempt all issue milestones', (): void => {
          beforeEach((): void => {
            optionsInterface.exemptAllIssueMilestones = true;
          });

          describe('when the given issue does not have a milestone', (): void => {
            beforeEach((): void => {
              issueInterface.milestone = undefined;
            });

            it('should return false', (): void => {
              expect.assertions(1);
              issue = new Issue(optionsInterface, issueInterface);
              milestones = new Milestones(optionsInterface, issue);

              const result = milestones.shouldExemptMilestones();

              expect(result).toStrictEqual(false);
            });
          });

          describe('when the given issue does have a milestone', (): void => {
            beforeEach((): void => {
              issueInterface.milestone = {
                title: 'dummy-exempt-issue-milestone'
              };
            });

            it('should return true', (): void => {
              expect.assertions(1);
              issue = new Issue(optionsInterface, issueInterface);
              milestones = new Milestones(optionsInterface, issue);

              const result = milestones.shouldExemptMilestones();

              expect(result).toStrictEqual(true);
            });
          });
        });
      });
    });

    describe('when the given issue is a pull request', (): void => {
      beforeEach((): void => {
        issueInterface.pull_request = {};
      });

      describe('when the given options are not configured to exempt a milestone', (): void => {
        beforeEach((): void => {
          optionsInterface.exemptMilestones = '';
        });

        describe('when the given options are not configured to exempt a pull request milestone', (): void => {
          beforeEach((): void => {
            optionsInterface.exemptPrMilestones = '';
          });

          describe('when the given pull request does not have a milestone', (): void => {
            beforeEach((): void => {
              issueInterface.milestone = undefined;
            });

            it('should return false', (): void => {
              expect.assertions(1);
              issue = new Issue(optionsInterface, issueInterface);
              milestones = new Milestones(optionsInterface, issue);

              const result = milestones.shouldExemptMilestones();

              expect(result).toStrictEqual(false);
            });
          });

          describe('when the given pull request does have a milestone', (): void => {
            beforeEach((): void => {
              issueInterface.milestone = {
                title: 'dummy-title'
              };
            });

            it('should return false', (): void => {
              expect.assertions(1);
              issue = new Issue(optionsInterface, issueInterface);
              milestones = new Milestones(optionsInterface, issue);

              const result = milestones.shouldExemptMilestones();

              expect(result).toStrictEqual(false);
            });
          });
        });

        describe('when the given options are configured to exempt a pull request milestone', (): void => {
          beforeEach((): void => {
            optionsInterface.exemptPrMilestones = 'dummy-exempt-pr-milestone';
          });

          describe('when the given pull request does not have a milestone', (): void => {
            beforeEach((): void => {
              issueInterface.milestone = undefined;
            });

            it('should return false', (): void => {
              expect.assertions(1);
              issue = new Issue(optionsInterface, issueInterface);
              milestones = new Milestones(optionsInterface, issue);

              const result = milestones.shouldExemptMilestones();

              expect(result).toStrictEqual(false);
            });
          });

          describe('when the given pull request does have a milestone different than the exempt pull request milestone', (): void => {
            beforeEach((): void => {
              issueInterface.milestone = {
                title: 'dummy-title'
              };
            });

            it('should return false', (): void => {
              expect.assertions(1);
              issue = new Issue(optionsInterface, issueInterface);
              milestones = new Milestones(optionsInterface, issue);

              const result = milestones.shouldExemptMilestones();

              expect(result).toStrictEqual(false);
            });
          });

          describe('when the given pull request does have a milestone equaling the exempt pull request milestone', (): void => {
            beforeEach((): void => {
              issueInterface.milestone = {
                title: 'dummy-exempt-pr-milestone'
              };
            });

            it('should return true', (): void => {
              expect.assertions(1);
              issue = new Issue(optionsInterface, issueInterface);
              milestones = new Milestones(optionsInterface, issue);

              const result = milestones.shouldExemptMilestones();

              expect(result).toStrictEqual(true);
            });
          });
        });
      });

      describe('when the given options are configured to exempt a milestone', (): void => {
        beforeEach((): void => {
          optionsInterface.exemptMilestones = 'dummy-exempt-milestone';
        });

        describe('when the given options are not configured to exempt a pull request milestone', (): void => {
          beforeEach((): void => {
            optionsInterface.exemptPrMilestones = '';
          });

          describe('when the given pull request does not have a milestone', (): void => {
            beforeEach((): void => {
              issueInterface.milestone = undefined;
            });

            it('should return false', (): void => {
              expect.assertions(1);
              issue = new Issue(optionsInterface, issueInterface);
              milestones = new Milestones(optionsInterface, issue);

              const result = milestones.shouldExemptMilestones();

              expect(result).toStrictEqual(false);
            });
          });

          describe('when the given pull request does have a milestone different than the exempt milestone', (): void => {
            beforeEach((): void => {
              issueInterface.milestone = {
                title: 'dummy-title'
              };
            });

            it('should return false', (): void => {
              expect.assertions(1);
              issue = new Issue(optionsInterface, issueInterface);
              milestones = new Milestones(optionsInterface, issue);

              const result = milestones.shouldExemptMilestones();

              expect(result).toStrictEqual(false);
            });
          });

          describe('when the given pull request does have a milestone equaling the exempt milestone', (): void => {
            beforeEach((): void => {
              issueInterface.milestone = {
                title: 'dummy-exempt-milestone'
              };
            });

            it('should return true', (): void => {
              expect.assertions(1);
              issue = new Issue(optionsInterface, issueInterface);
              milestones = new Milestones(optionsInterface, issue);

              const result = milestones.shouldExemptMilestones();

              expect(result).toStrictEqual(true);
            });
          });
        });

        describe('when the given options are configured to exempt a pull request milestone', (): void => {
          beforeEach((): void => {
            optionsInterface.exemptPrMilestones = 'dummy-exempt-pr-milestone';
          });

          describe('when the given pull request does not have a milestone', (): void => {
            beforeEach((): void => {
              issueInterface.milestone = undefined;
            });

            it('should return false', (): void => {
              expect.assertions(1);
              issue = new Issue(optionsInterface, issueInterface);
              milestones = new Milestones(optionsInterface, issue);

              const result = milestones.shouldExemptMilestones();

              expect(result).toStrictEqual(false);
            });
          });

          describe('when the given pull request does have a milestone different than the exempt pull request milestone', (): void => {
            beforeEach((): void => {
              issueInterface.milestone = {
                title: 'dummy-title'
              };
            });

            it('should return false', (): void => {
              expect.assertions(1);
              issue = new Issue(optionsInterface, issueInterface);
              milestones = new Milestones(optionsInterface, issue);

              const result = milestones.shouldExemptMilestones();

              expect(result).toStrictEqual(false);
            });
          });

          describe('when the given pull request does have a milestone equaling the exempt pull request milestone', (): void => {
            beforeEach((): void => {
              issueInterface.milestone = {
                title: 'dummy-exempt-pr-milestone'
              };
            });

            it('should return true', (): void => {
              expect.assertions(1);
              issue = new Issue(optionsInterface, issueInterface);
              milestones = new Milestones(optionsInterface, issue);

              const result = milestones.shouldExemptMilestones();

              expect(result).toStrictEqual(true);
            });
          });

          describe('when the given pull request does have a milestone different than the exempt milestone', (): void => {
            beforeEach((): void => {
              issueInterface.milestone = {
                title: 'dummy-title'
              };
            });

            it('should return false', (): void => {
              expect.assertions(1);
              issue = new Issue(optionsInterface, issueInterface);
              milestones = new Milestones(optionsInterface, issue);

              const result = milestones.shouldExemptMilestones();

              expect(result).toStrictEqual(false);
            });
          });

          describe('when the given pull request does have a milestone equaling the exempt milestone', (): void => {
            beforeEach((): void => {
              issueInterface.milestone = {
                title: 'dummy-exempt-milestone'
              };
            });

            it('should return false', (): void => {
              expect.assertions(1);
              issue = new Issue(optionsInterface, issueInterface);
              milestones = new Milestones(optionsInterface, issue);

              const result = milestones.shouldExemptMilestones();

              expect(result).toStrictEqual(false);
            });
          });
        });
      });

      describe('when the given options are configured to exempt all milestones', (): void => {
        beforeEach((): void => {
          optionsInterface.exemptAllMilestones = true;
        });

        describe('when the given pull request does not have a milestone', (): void => {
          beforeEach((): void => {
            issueInterface.milestone = undefined;
          });

          it('should return false', (): void => {
            expect.assertions(1);
            issue = new Issue(optionsInterface, issueInterface);
            milestones = new Milestones(optionsInterface, issue);

            const result = milestones.shouldExemptMilestones();

            expect(result).toStrictEqual(false);
          });
        });

        describe('when the given pull request does have a milestone', (): void => {
          beforeEach((): void => {
            issueInterface.milestone = {
              title: 'dummy-exempt-pr-milestone'
            };
          });

          it('should return true', (): void => {
            expect.assertions(1);
            issue = new Issue(optionsInterface, issueInterface);
            milestones = new Milestones(optionsInterface, issue);

            const result = milestones.shouldExemptMilestones();

            expect(result).toStrictEqual(true);
          });
        });

        describe('when the given options are not configured to exempt all pull request milestones', (): void => {
          beforeEach((): void => {
            optionsInterface.exemptAllPrMilestones = false;
          });

          describe('when the given pull request does not have a milestone', (): void => {
            beforeEach((): void => {
              issueInterface.milestone = undefined;
            });

            it('should return false', (): void => {
              expect.assertions(1);
              issue = new Issue(optionsInterface, issueInterface);
              milestones = new Milestones(optionsInterface, issue);

              const result = milestones.shouldExemptMilestones();

              expect(result).toStrictEqual(false);
            });
          });

          describe('when the given pull request does have a milestone', (): void => {
            beforeEach((): void => {
              issueInterface.milestone = {
                title: 'dummy-exempt-milestone'
              };
            });

            it('should return false', (): void => {
              expect.assertions(1);
              issue = new Issue(optionsInterface, issueInterface);
              milestones = new Milestones(optionsInterface, issue);

              const result = milestones.shouldExemptMilestones();

              expect(result).toStrictEqual(false);
            });
          });
        });

        describe('when the given options are configured to exempt all pull request milestones', (): void => {
          beforeEach((): void => {
            optionsInterface.exemptAllPrMilestones = true;
          });

          describe('when the given pull request does not have a milestone', (): void => {
            beforeEach((): void => {
              issueInterface.milestone = undefined;
            });

            it('should return false', (): void => {
              expect.assertions(1);
              issue = new Issue(optionsInterface, issueInterface);
              milestones = new Milestones(optionsInterface, issue);

              const result = milestones.shouldExemptMilestones();

              expect(result).toStrictEqual(false);
            });
          });

          describe('when the given pull request does have a milestone', (): void => {
            beforeEach((): void => {
              issueInterface.milestone = {
                title: 'dummy-exempt-pr-milestone'
              };
            });

            it('should return true', (): void => {
              expect.assertions(1);
              issue = new Issue(optionsInterface, issueInterface);
              milestones = new Milestones(optionsInterface, issue);

              const result = milestones.shouldExemptMilestones();

              expect(result).toStrictEqual(true);
            });
          });
        });
      });
    });
  });
});
```

## File: `src/classes/milestones.ts`
```typescript
import deburr from 'lodash.deburr';
import {Option} from '../enums/option';
import {wordsToList} from '../functions/words-to-list';
import {IIssuesProcessorOptions} from '../interfaces/issues-processor-options';
import {Issue} from './issue';
import {IssueLogger} from './loggers/issue-logger';
import {LoggerService} from '../services/logger.service';

type CleanMilestone = string;

export class Milestones {
  private static _cleanMilestone(milestone: Readonly<string>): CleanMilestone {
    return deburr(milestone.toLowerCase());
  }

  private readonly _options: IIssuesProcessorOptions;
  private readonly _issue: Issue;
  private readonly _issueLogger: IssueLogger;

  constructor(options: Readonly<IIssuesProcessorOptions>, issue: Issue) {
    this._options = options;
    this._issue = issue;
    this._issueLogger = new IssueLogger(issue);
  }

  shouldExemptMilestones(): boolean {
    if (!this._issue.milestone) {
      this._issueLogger.info('This $$type has no milestone');
      this._logSkip();

      return false;
    }

    if (this._shouldExemptAllMilestones()) {
      this._issueLogger.info(
        LoggerService.white('└──'),
        'Skipping this $$type because it has a milestone'
      );

      return true;
    }

    const exemptMilestones: string[] = this._getExemptMilestones();

    if (exemptMilestones.length === 0) {
      this._issueLogger.info(
        LoggerService.white('├──'),
        `No milestone option was specified to skip the stale process for this $$type`
      );
      this._logSkip();

      return false;
    }

    this._issueLogger.info(
      LoggerService.white('├──'),
      `Found ${LoggerService.cyan(exemptMilestones.length)} milestone${
        exemptMilestones.length > 1 ? 's' : ''
      } that can exempt stale on this $$type`
    );

    const hasExemptMilestone: boolean = exemptMilestones.some(
      (exemptMilestone: Readonly<string>): boolean =>
        this._hasMilestone(exemptMilestone)
    );

    if (!hasExemptMilestone) {
      this._issueLogger.info(
        LoggerService.white('├──'),
        'No milestone on this $$type can exempt the stale process'
      );
      this._logSkip();
    } else {
      this._issueLogger.info(
        LoggerService.white('└──'),
        'Skipping this $$type because it has an exempt milestone'
      );
    }

    return hasExemptMilestone;
  }

  private _getExemptMilestones(): string[] {
    return this._issue.isPullRequest
      ? this._getExemptPullRequestMilestones()
      : this._getExemptIssueMilestones();
  }

  private _getExemptIssueMilestones(): string[] {
    if (this._options.exemptIssueMilestones === '') {
      this._issueLogger.info(
        LoggerService.white('├──'),
        `The option ${this._issueLogger.createOptionLink(
          Option.ExemptIssueMilestones
        )} is disabled. No specific milestone can skip the stale process for this $$type`
      );

      if (this._options.exemptMilestones === '') {
        this._issueLogger.info(
          LoggerService.white('├──'),
          `The option ${this._issueLogger.createOptionLink(
            Option.ExemptMilestones
          )} is disabled. No specific milestone can skip the stale process for this $$type`
        );

        return [];
      }

      const exemptMilestones: string[] = wordsToList(
        this._options.exemptMilestones
      );

      this._issueLogger.info(
        LoggerService.white('├──'),
        `The option ${this._issueLogger.createOptionLink(
          Option.ExemptMilestones
        )} is set. ${LoggerService.cyan(exemptMilestones.length)} milestone${
          exemptMilestones.length === 1 ? '' : 's'
        } can skip the stale process for this $$type`
      );

      return exemptMilestones;
    }

    const exemptMilestones: string[] = wordsToList(
      this._options.exemptIssueMilestones
    );

    this._issueLogger.info(
      LoggerService.white('├──'),
      `The option ${this._issueLogger.createOptionLink(
        Option.ExemptIssueMilestones
      )} is set. ${LoggerService.cyan(exemptMilestones.length)} milestone${
        exemptMilestones.length === 1 ? '' : 's'
      } can skip the stale process for this $$type`
    );

    return exemptMilestones;
  }

  private _getExemptPullRequestMilestones(): string[] {
    if (this._options.exemptPrMilestones === '') {
      this._issueLogger.info(
        LoggerService.white('├──'),
        `The option ${this._issueLogger.createOptionLink(
          Option.ExemptPrMilestones
        )} is disabled. No specific milestone can skip the stale process for this $$type`
      );

      if (this._options.exemptMilestones === '') {
        this._issueLogger.info(
          LoggerService.white('├──'),
          `The option ${this._issueLogger.createOptionLink(
            Option.ExemptMilestones
          )} is disabled. No specific milestone can skip the stale process for this $$type`
        );

        return [];
      }

      const exemptMilestones: string[] = wordsToList(
        this._options.exemptMilestones
      );

      this._issueLogger.info(
        LoggerService.white('├──'),
        `The option ${this._issueLogger.createOptionLink(
          Option.ExemptMilestones
        )} is set. ${LoggerService.cyan(exemptMilestones.length)} milestone${
          exemptMilestones.length === 1 ? '' : 's'
        } can skip the stale process for this $$type`
      );

      return exemptMilestones;
    }

    const exemptMilestones: string[] = wordsToList(
      this._options.exemptPrMilestones
    );

    this._issueLogger.info(
      LoggerService.white('├──'),
      `The option ${this._issueLogger.createOptionLink(
        Option.ExemptPrMilestones
      )} is set. ${LoggerService.cyan(exemptMilestones.length)} milestone${
        exemptMilestones.length === 1 ? '' : 's'
      } can skip the stale process for this $$type`
    );

    return exemptMilestones;
  }

  private _hasMilestone(milestone: Readonly<string>): boolean {
    if (!this._issue.milestone) {
      return false;
    }

    const cleanMilestone: CleanMilestone =
      Milestones._cleanMilestone(milestone);

    const isSameMilestone: boolean =
      cleanMilestone ===
      Milestones._cleanMilestone(this._issue.milestone.title);

    if (isSameMilestone) {
      this._issueLogger.info(
        LoggerService.white('├──'),
        `The milestone "${LoggerService.cyan(
          milestone
        )}" is set on this $$type and is an exempt milestone`
      );
    }

    return isSameMilestone;
  }

  private _shouldExemptAllMilestones(): boolean {
    if (this._issue.milestone) {
      return this._issue.isPullRequest
        ? this._shouldExemptAllPullRequestMilestones()
        : this._shouldExemptAllIssueMilestones();
    }

    return false;
  }

  private _shouldExemptAllIssueMilestones(): boolean {
    if (this._options.exemptAllIssueMilestones === true) {
      this._issueLogger.info(
        `The option ${this._issueLogger.createOptionLink(
          Option.ExemptAllIssueMilestones
        )} is enabled. Any milestone on this $$type will skip the stale process`
      );

      return true;
    } else if (this._options.exemptAllIssueMilestones === false) {
      this._issueLogger.info(
        `The option ${this._issueLogger.createOptionLink(
          Option.ExemptAllIssueMilestones
        )} is disabled. Only some specific milestones on this $$type will skip the stale process`
      );

      return false;
    }

    this._logExemptAllMilestonesOption();

    return this._options.exemptAllMilestones;
  }

  private _shouldExemptAllPullRequestMilestones(): boolean {
    if (this._options.exemptAllPrMilestones === true) {
      this._issueLogger.info(
        `The option ${this._issueLogger.createOptionLink(
          Option.ExemptAllPrMilestones
        )} is enabled. Any milestone on this $$type will skip the stale process`
      );

      return true;
    } else if (this._options.exemptAllPrMilestones === false) {
      this._issueLogger.info(
        `The option ${this._issueLogger.createOptionLink(
          Option.ExemptAllPrMilestones
        )} is disabled. Only some specific milestones on this $$type will skip the stale process`
      );

      return false;
    }

    this._logExemptAllMilestonesOption();

    return this._options.exemptAllMilestones;
  }

  private _logExemptAllMilestonesOption(): void {
    if (this._options.exemptAllMilestones) {
      this._issueLogger.info(
        `The option ${this._issueLogger.createOptionLink(
          Option.ExemptAllMilestones
        )} is enabled. Any milestone on this $$type will skip the stale process`
      );
    } else {
      this._issueLogger.info(
        `The option ${this._issueLogger.createOptionLink(
          Option.ExemptAllMilestones
        )} is disabled. Only some specific milestones on this $$type will skip the stale process`
      );
    }
  }

  private _logSkip(): void {
    this._issueLogger.info(
      LoggerService.white('└──'),
      'Skip the milestones checks'
    );
  }
}
```

## File: `src/classes/operations.spec.ts`
```typescript
import {Operations} from './operations';

describe('Operations', (): void => {
  let operations: Operations;

  describe('consumeOperation()', (): void => {
    beforeEach((): void => {
      operations = new Operations();
    });

    it('should increase the count of operation consume by 1', (): void => {
      expect.assertions(1);
      operations.consumeOperation();

      const result = operations.getConsumedOperationsCount();

      expect(result).toStrictEqual(1);
    });
  });

  describe('consumeOperations()', (): void => {
    beforeEach((): void => {
      operations = new Operations();
    });

    it('should increase the count of operation consume by the provided quantity', (): void => {
      expect.assertions(1);
      operations.consumeOperations(8);

      const result = operations.getConsumedOperationsCount();

      expect(result).toStrictEqual(8);
    });
  });

  describe('getConsumedOperationsCount()', (): void => {
    beforeEach((): void => {
      operations = new Operations();
    });

    it('should return 0 by default', (): void => {
      expect.assertions(1);

      const result = operations.getConsumedOperationsCount();

      expect(result).toStrictEqual(0);
    });
  });
});
```

## File: `src/classes/operations.ts`
```typescript
export class Operations {
  protected _operationsConsumed = 0;

  consumeOperation(): Operations {
    return this.consumeOperations(1);
  }

  consumeOperations(quantity: Readonly<number>): Operations {
    this._operationsConsumed += quantity;

    return this;
  }

  getConsumedOperationsCount(): number {
    return this._operationsConsumed;
  }
}
```

## File: `src/classes/rate-limit.ts`
```typescript
import {IRateLimit, OctokitRateLimit} from '../interfaces/rate-limit';

export class RateLimit implements IRateLimit {
  readonly limit: number;
  readonly remaining: number;
  readonly reset: Date;
  readonly used: number;

  constructor(rateLimit: Readonly<OctokitRateLimit>) {
    this.limit = rateLimit.limit;
    this.remaining = rateLimit.remaining;
    this.used = rateLimit.used;
    this.reset = new Date(rateLimit.reset * 1000);
  }
}
```

## File: `src/classes/stale-operations.spec.ts`
```typescript
import {DefaultProcessorOptions} from '../../__tests__/constants/default-processor-options';
import {IIssuesProcessorOptions} from '../interfaces/issues-processor-options';
import {StaleOperations} from './stale-operations';

interface IHasRemainingOperationsMatrix {
  operationsPerRun: number;
  consumeOperations: number;
  hasRemainingOperations: number;
}

interface IGetRemainingOperationsCountMatrix {
  operationsPerRun: number;
  consumeOperations: number;
  getRemainingOperationsCount: number;
}

describe('StaleOperations', (): void => {
  let operations: StaleOperations;
  let options: IIssuesProcessorOptions;

  beforeEach((): void => {
    options = {...DefaultProcessorOptions};
  });

  describe('consumeOperation()', (): void => {
    beforeEach((): void => {
      operations = new StaleOperations(options);
    });

    it('should increase the count of operation consume by 1', (): void => {
      expect.assertions(1);
      operations.consumeOperation();

      const result = operations.getConsumedOperationsCount();

      expect(result).toStrictEqual(1);
    });
  });

  describe('consumeOperations()', (): void => {
    beforeEach((): void => {
      operations = new StaleOperations(options);
    });

    it('should increase the count of operation consume by the provided quantity', (): void => {
      expect.assertions(1);
      operations.consumeOperations(8);

      const result = operations.getConsumedOperationsCount();

      expect(result).toStrictEqual(8);
    });
  });

  describe('getConsumedOperationsCount()', (): void => {
    beforeEach((): void => {
      operations = new StaleOperations(options);
    });

    it('should return 0 by default', (): void => {
      expect.assertions(1);

      const result = operations.getConsumedOperationsCount();

      expect(result).toStrictEqual(0);
    });
  });

  describe('hasRemainingOperations()', (): void => {
    beforeEach((): void => {
      operations = new StaleOperations(options);
    });

    describe.each`
      operationsPerRun | consumeOperations | hasRemainingOperations
      ${1}             | ${1}              | ${false}
      ${2}             | ${1}              | ${true}
    `(
      'when the operations per run is $operationsPerRun and $consumeOperations operations were consumed',
      ({
        operationsPerRun,
        consumeOperations,
        hasRemainingOperations
      }: IHasRemainingOperationsMatrix): void => {
        beforeEach((): void => {
          options.operationsPerRun = operationsPerRun;
          operations = new StaleOperations(options);
        });

        it(`should return ${hasRemainingOperations}`, (): void => {
          expect.assertions(1);
          operations.consumeOperations(consumeOperations);

          const result = operations.hasRemainingOperations();

          expect(result).toStrictEqual(hasRemainingOperations);
        });
      }
    );
  });

  describe('getRemainingOperationsCount()', (): void => {
    beforeEach((): void => {
      operations = new StaleOperations(options);
    });

    describe.each`
      operationsPerRun | consumeOperations | getRemainingOperationsCount
      ${1}             | ${1}              | ${0}
      ${2}             | ${1}              | ${1}
    `(
      'when the operations per run is $operationsPerRun and $consumeOperations operations were consumed',
      ({
        operationsPerRun,
        consumeOperations,
        getRemainingOperationsCount
      }: IGetRemainingOperationsCountMatrix): void => {
        beforeEach((): void => {
          options.operationsPerRun = operationsPerRun;
          operations = new StaleOperations(options);
        });

        it(`should return ${getRemainingOperationsCount}`, (): void => {
          expect.assertions(1);
          operations.consumeOperations(consumeOperations);

          const result = operations.getRemainingOperationsCount();

          expect(result).toStrictEqual(getRemainingOperationsCount);
        });
      }
    );
  });
});
```

## File: `src/classes/stale-operations.ts`
```typescript
import {IIssuesProcessorOptions} from '../interfaces/issues-processor-options';
import {Operations} from './operations';

export class StaleOperations extends Operations {
  private readonly _options: IIssuesProcessorOptions;

  constructor(options: Readonly<IIssuesProcessorOptions>) {
    super();
    this._options = options;
  }

  hasRemainingOperations(): boolean {
    return this._operationsConsumed < this._options.operationsPerRun;
  }

  getRemainingOperationsCount(): number {
    return this._options.operationsPerRun - this._operationsConsumed;
  }
}
```

## File: `src/classes/statistics.ts`
```typescript
import {Issue} from './issue';
import {Logger} from './loggers/logger';
import {LoggerService} from '../services/logger.service';

interface IGroupValue {
  name: string;
  count: number;
}

export class Statistics {
  private readonly _logger: Logger = new Logger();
  processedIssuesCount = 0;
  processedPullRequestsCount = 0;
  staleIssuesCount = 0;
  stalePullRequestsCount = 0;
  undoStaleIssuesCount = 0;
  undoStalePullRequestsCount = 0;
  operationsCount = 0;
  closedIssuesCount = 0;
  closedPullRequestsCount = 0;
  deletedIssuesLabelsCount = 0;
  deletedPullRequestsLabelsCount = 0;
  deletedCloseIssuesLabelsCount = 0;
  deletedClosePullRequestsLabelsCount = 0;
  deletedBranchesCount = 0;
  addedIssuesLabelsCount = 0;
  addedPullRequestsLabelsCount = 0;
  addedIssuesCommentsCount = 0;
  addedPullRequestsCommentsCount = 0;
  fetchedItemsCount = 0;
  fetchedItemsEventsCount = 0;
  fetchedItemsCommentsCount = 0;
  fetchedPullRequestsCount = 0;

  incrementProcessedItemsCount(
    issue: Readonly<Issue>,
    increment: Readonly<number> = 1
  ): Statistics {
    if (issue.isPullRequest) {
      return this._incrementProcessedPullRequestsCount(increment);
    }

    return this._incrementProcessedIssuesCount(increment);
  }

  incrementStaleItemsCount(
    issue: Readonly<Issue>,
    increment: Readonly<number> = 1
  ): Statistics {
    if (issue.isPullRequest) {
      return this._incrementStalePullRequestsCount(increment);
    }

    return this._incrementStaleIssuesCount(increment);
  }

  incrementUndoStaleItemsCount(
    issue: Readonly<Issue>,
    increment: Readonly<number> = 1
  ): Statistics {
    if (issue.isPullRequest) {
      return this._incrementUndoStalePullRequestsCount(increment);
    }

    return this._incrementUndoStaleIssuesCount(increment);
  }

  setOperationsCount(operationsCount: Readonly<number>): Statistics {
    this.operationsCount = operationsCount;

    return this;
  }

  incrementClosedItemsCount(
    issue: Readonly<Issue>,
    increment: Readonly<number> = 1
  ): Statistics {
    if (issue.isPullRequest) {
      return this._incrementClosedPullRequestsCount(increment);
    }

    return this._incrementClosedIssuesCount(increment);
  }

  incrementDeletedItemsLabelsCount(
    issue: Readonly<Issue>,
    increment: Readonly<number> = 1
  ): Statistics {
    if (issue.isPullRequest) {
      return this._incrementDeletedPullRequestsLabelsCount(increment);
    }

    return this._incrementDeletedIssuesLabelsCount(increment);
  }

  incrementDeletedCloseItemsLabelsCount(
    issue: Readonly<Issue>,
    increment: Readonly<number> = 1
  ): Statistics {
    if (issue.isPullRequest) {
      return this._incrementDeletedClosePullRequestsLabelsCount(increment);
    }

    return this._incrementDeletedCloseIssuesLabelsCount(increment);
  }

  incrementDeletedBranchesCount(increment: Readonly<number> = 1): Statistics {
    this.deletedBranchesCount += increment;

    return this;
  }

  incrementAddedItemsLabel(
    issue: Readonly<Issue>,
    increment: Readonly<number> = 1
  ): Statistics {
    if (issue.isPullRequest) {
      return this._incrementAddedPullRequestsLabel(increment);
    }

    return this._incrementAddedIssuesLabel(increment);
  }

  incrementAddedItemsComment(
    issue: Readonly<Issue>,
    increment: Readonly<number> = 1
  ): Statistics {
    if (issue.isPullRequest) {
      return this._incrementAddedPullRequestsComment(increment);
    }

    return this._incrementAddedIssuesComment(increment);
  }

  incrementFetchedItemsCount(increment: Readonly<number> = 1): Statistics {
    this.fetchedItemsCount += increment;

    return this;
  }

  incrementFetchedItemsEventsCount(
    increment: Readonly<number> = 1
  ): Statistics {
    this.fetchedItemsEventsCount += increment;

    return this;
  }

  incrementFetchedItemsCommentsCount(
    increment: Readonly<number> = 1
  ): Statistics {
    this.fetchedItemsCommentsCount += increment;

    return this;
  }

  incrementFetchedPullRequestsCount(
    increment: Readonly<number> = 1
  ): Statistics {
    this.fetchedPullRequestsCount += increment;

    return this;
  }

  logStats(): Statistics {
    this._logger.info(LoggerService.yellow(LoggerService.bold(`Statistics:`)));
    this._logProcessedIssuesAndPullRequestsCount();
    this._logStaleIssuesAndPullRequestsCount();
    this._logUndoStaleIssuesAndPullRequestsCount();
    this._logClosedIssuesAndPullRequestsCount();
    this._logDeletedIssuesAndPullRequestsLabelsCount();
    this._logDeletedCloseIssuesAndPullRequestsLabelsCount();
    this._logDeletedBranchesCount();
    this._logAddedIssuesAndPullRequestsLabelsCount();
    this._logAddedIssuesAndPullRequestsCommentsCount();
    this._logFetchedItemsCount();
    this._logFetchedItemsEventsCount();
    this._logFetchedItemsCommentsCount();
    this._logFetchedPullRequestsCount();
    this._logOperationsCount();

    return this;
  }

  private _incrementProcessedIssuesCount(
    increment: Readonly<number> = 1
  ): Statistics {
    this.processedIssuesCount += increment;

    return this;
  }

  private _incrementProcessedPullRequestsCount(
    increment: Readonly<number> = 1
  ): Statistics {
    this.processedPullRequestsCount += increment;

    return this;
  }

  private _incrementStaleIssuesCount(
    increment: Readonly<number> = 1
  ): Statistics {
    this.staleIssuesCount += increment;

    return this;
  }

  private _incrementStalePullRequestsCount(
    increment: Readonly<number> = 1
  ): Statistics {
    this.stalePullRequestsCount += increment;

    return this;
  }

  private _incrementUndoStaleIssuesCount(
    increment: Readonly<number> = 1
  ): Statistics {
    this.undoStaleIssuesCount += increment;

    return this;
  }

  private _incrementUndoStalePullRequestsCount(
    increment: Readonly<number> = 1
  ): Statistics {
    this.undoStalePullRequestsCount += increment;

    return this;
  }

  private _incrementClosedIssuesCount(
    increment: Readonly<number> = 1
  ): Statistics {
    this.closedIssuesCount += increment;

    return this;
  }

  private _incrementClosedPullRequestsCount(
    increment: Readonly<number> = 1
  ): Statistics {
    this.closedPullRequestsCount += increment;

    return this;
  }

  private _incrementDeletedIssuesLabelsCount(
    increment: Readonly<number> = 1
  ): Statistics {
    this.deletedIssuesLabelsCount += increment;

    return this;
  }

  private _incrementDeletedPullRequestsLabelsCount(
    increment: Readonly<number> = 1
  ): Statistics {
    this.deletedPullRequestsLabelsCount += increment;

    return this;
  }

  private _incrementDeletedCloseIssuesLabelsCount(
    increment: Readonly<number> = 1
  ): Statistics {
    this.deletedCloseIssuesLabelsCount += increment;

    return this;
  }

  private _incrementDeletedClosePullRequestsLabelsCount(
    increment: Readonly<number> = 1
  ): Statistics {
    this.deletedClosePullRequestsLabelsCount += increment;

    return this;
  }

  private _incrementAddedIssuesLabel(
    increment: Readonly<number> = 1
  ): Statistics {
    this.addedIssuesLabelsCount += increment;

    return this;
  }

  private _incrementAddedPullRequestsLabel(
    increment: Readonly<number> = 1
  ): Statistics {
    this.addedPullRequestsLabelsCount += increment;

    return this;
  }

  private _incrementAddedIssuesComment(
    increment: Readonly<number> = 1
  ): Statistics {
    this.addedIssuesCommentsCount += increment;

    return this;
  }

  private _incrementAddedPullRequestsComment(
    increment: Readonly<number> = 1
  ): Statistics {
    this.addedPullRequestsCommentsCount += increment;

    return this;
  }

  private _logProcessedIssuesAndPullRequestsCount(): void {
    this._logGroup('Processed items', [
      {
        name: 'Processed issues',
        count: this.processedIssuesCount
      },
      {
        name: 'Processed PRs',
        count: this.processedPullRequestsCount
      }
    ]);
  }

  private _logStaleIssuesAndPullRequestsCount(): void {
    this._logGroup('New stale items', [
      {
        name: 'New stale issues',
        count: this.staleIssuesCount
      },
      {
        name: 'New stale PRs',
        count: this.stalePullRequestsCount
      }
    ]);
  }

  private _logUndoStaleIssuesAndPullRequestsCount(): void {
    this._logGroup('No longer stale items', [
      {
        name: 'No longer stale issues',
        count: this.undoStaleIssuesCount
      },
      {
        name: 'No longer stale PRs',
        count: this.undoStalePullRequestsCount
      }
    ]);
  }

  private _logClosedIssuesAndPullRequestsCount(): void {
    this._logGroup('Closed items', [
      {
        name: 'Closed issues',
        count: this.closedIssuesCount
      },
      {
        name: 'Closed PRs',
        count: this.closedPullRequestsCount
      }
    ]);
  }

  private _logDeletedIssuesAndPullRequestsLabelsCount(): void {
    this._logGroup('Deleted items labels', [
      {
        name: 'Deleted issues labels',
        count: this.deletedIssuesLabelsCount
      },
      {
        name: 'Deleted PRs labels',
        count: this.deletedPullRequestsLabelsCount
      }
    ]);
  }

  private _logDeletedCloseIssuesAndPullRequestsLabelsCount(): void {
    this._logGroup('Deleted close items labels', [
      {
        name: 'Deleted close issues labels',
        count: this.deletedCloseIssuesLabelsCount
      },
      {
        name: 'Deleted close PRs labels',
        count: this.deletedClosePullRequestsLabelsCount
      }
    ]);
  }

  private _logDeletedBranchesCount(): void {
    this._logCount('Deleted branches', this.deletedBranchesCount);
  }

  private _logAddedIssuesAndPullRequestsLabelsCount(): void {
    this._logGroup('Added items labels', [
      {
        name: 'Added issues labels',
        count: this.addedIssuesLabelsCount
      },
      {
        name: 'Added PRs labels',
        count: this.addedPullRequestsLabelsCount
      }
    ]);
  }

  private _logAddedIssuesAndPullRequestsCommentsCount(): void {
    this._logGroup('Added items comments', [
      {
        name: 'Added issues comments',
        count: this.addedIssuesCommentsCount
      },
      {
        name: 'Added PRs comments',
        count: this.addedPullRequestsCommentsCount
      }
    ]);
  }

  private _logFetchedItemsCount(): void {
    this._logCount('Fetched items', this.fetchedItemsCount);
  }

  private _logFetchedItemsEventsCount(): void {
    this._logCount('Fetched items events', this.fetchedItemsEventsCount);
  }

  private _logFetchedItemsCommentsCount(): void {
    this._logCount('Fetched items comments', this.fetchedItemsCommentsCount);
  }

  private _logFetchedPullRequestsCount(): void {
    this._logCount('Fetched pull requests', this.fetchedPullRequestsCount);
  }

  private _logOperationsCount(): void {
    this._logCount('Operations performed', this.operationsCount);
  }

  private _logCount(name: Readonly<string>, count: Readonly<number>): void {
    if (count > 0) {
      this._logger.info(`${name}:`, LoggerService.cyan(count));
    }
  }

  private _logGroup(groupName: Readonly<string>, values: IGroupValue[]): void {
    if (this._isGroupValuesPartiallySet(values)) {
      this._logCount(groupName, this._getGroupValuesTotalCount(values));

      this._logGroupValues(values);
    } else {
      // Only one value will be display
      for (const value of values) {
        this._logCount(value.name, value.count);
      }
    }
  }

  /**
   * @private
   * @description
   * If there is a least two elements with a valid count then it's partially set
   * Useful to defined if we should display the values as a group or not
   *
   * @param {IGroupValue[]} values The list of group values to check
   */
  private _isGroupValuesPartiallySet(values: IGroupValue[]): boolean {
    return (
      values
        .map((value: Readonly<IGroupValue>): boolean => {
          return value.count > 0;
        })
        .filter((isSet: Readonly<boolean>): boolean => isSet).length >= 2
    );
  }

  private _getGroupValuesTotalCount(values: IGroupValue[]): number {
    return values.reduce(
      (count: Readonly<number>, value: Readonly<IGroupValue>): number => {
        return count + value.count;
      },
      0
    );
  }

  private _getAllGroupValuesSet(values: IGroupValue[]): IGroupValue[] {
    return values.filter((value: Readonly<IGroupValue>): boolean => {
      return value.count > 0;
    });
  }

  private _logGroupValues(values: IGroupValue[]): void {
    const onlyValuesSet: IGroupValue[] = this._getAllGroupValuesSet(values);
    const longestValue: number = this._getLongestGroupValue(onlyValuesSet);

    for (const [index, value] of onlyValuesSet.entries()) {
      const prefix = index === onlyValuesSet.length - 1 ? '└──' : '├──';

      this._logCount(
        `${LoggerService.white(prefix)} ${value.name.padEnd(
          longestValue,
          ' '
        )}`,
        value.count
      );
    }
  }

  private _getLongestGroupValue(values: IGroupValue[]): number {
    return values.reduce(
      (
        longestValue: Readonly<number>,
        value: Readonly<IGroupValue>
      ): number => {
        return value.name.length > longestValue
          ? value.name.length
          : longestValue;
      },
      0
    );
  }
}
```

## File: `src/classes/loggers/issue-logger.spec.ts`
```typescript
import {DefaultProcessorOptions} from '../../../__tests__/constants/default-processor-options';
import {generateIIssue} from '../../../__tests__/functions/generate-iissue';
import {Issue} from '../issue';
import {IssueLogger} from './issue-logger';
import * as core from '@actions/core';

describe('IssueLogger', (): void => {
  let issue: Issue;
  let issueLogger: IssueLogger;
  let message: string;

  let coreWarningSpy: jest.SpyInstance;

  describe('warning()', (): void => {
    beforeEach((): void => {
      message = 'dummy-message';
      issue = new Issue(
        DefaultProcessorOptions,
        generateIIssue({
          number: 8
        })
      );
      issueLogger = new IssueLogger(issue);

      coreWarningSpy = jest.spyOn(core, 'warning').mockImplementation();
    });

    it('should log a warning with the given message and with the issue number as prefix', (): void => {
      expect.assertions(3);

      issueLogger.warning(message);

      expect(coreWarningSpy).toHaveBeenCalledTimes(1);
      expect(coreWarningSpy).toHaveBeenCalledWith(
        expect.stringContaining('[#8]')
      );
      expect(coreWarningSpy).toHaveBeenCalledWith(
        expect.stringContaining('dummy-message')
      );
    });
  });

  describe('info()', (): void => {
    let coreInfoSpy: jest.SpyInstance;

    beforeEach((): void => {
      message = 'dummy-message';
      issue = new Issue(
        DefaultProcessorOptions,
        generateIIssue({
          number: 8
        })
      );
      issueLogger = new IssueLogger(issue);

      coreInfoSpy = jest.spyOn(core, 'info').mockImplementation();
    });

    it('should log an information with the given message and with the issue number as prefix', (): void => {
      expect.assertions(3);

      issueLogger.info(message);

      expect(coreInfoSpy).toHaveBeenCalledTimes(1);
      expect(coreInfoSpy).toHaveBeenCalledWith(expect.stringContaining('[#8]'));
      expect(coreInfoSpy).toHaveBeenCalledWith(
        expect.stringContaining('dummy-message')
      );
    });
  });

  describe('error()', (): void => {
    let coreErrorSpy: jest.SpyInstance;

    beforeEach((): void => {
      message = 'dummy-message';
      issue = new Issue(
        DefaultProcessorOptions,
        generateIIssue({
          number: 8
        })
      );
      issueLogger = new IssueLogger(issue);

      coreErrorSpy = jest.spyOn(core, 'error').mockImplementation();
    });

    it('should log an error with the given message and with the issue number as prefix', (): void => {
      expect.assertions(3);

      issueLogger.error(message);

      expect(coreErrorSpy).toHaveBeenCalledTimes(1);
      expect(coreErrorSpy).toHaveBeenCalledWith(
        expect.stringContaining('[#8]')
      );
      expect(coreErrorSpy).toHaveBeenCalledWith(
        expect.stringContaining('dummy-message')
      );
    });
  });

  it('should prefix the message with the issue number', (): void => {
    expect.assertions(3);
    message = 'dummy-message';
    issue = new Issue(
      DefaultProcessorOptions,
      generateIIssue({
        number: 123
      })
    );
    issueLogger = new IssueLogger(issue);
    coreWarningSpy = jest.spyOn(core, 'warning').mockImplementation();

    issueLogger.warning(message);

    expect(coreWarningSpy).toHaveBeenCalledTimes(1);
    expect(coreWarningSpy).toHaveBeenCalledWith(
      expect.stringContaining('[#123]')
    );
    expect(coreWarningSpy).toHaveBeenCalledWith(
      expect.stringContaining('dummy-message')
    );
  });

  it.each`
    pull_request      | replacement
    ${{key: 'value'}} | ${'pull request'}
    ${{}}             | ${'pull request'}
    ${null}           | ${'issue'}
    ${undefined}      | ${'issue'}
  `(
    'should replace the special tokens "$$type" with the corresponding type',
    ({pull_request, replacement}): void => {
      expect.assertions(3);
      message = 'The $$type will stale! $$type will soon be closed!';
      issue = new Issue(
        DefaultProcessorOptions,
        generateIIssue({
          number: 8,
          pull_request
        })
      );
      issueLogger = new IssueLogger(issue);
      coreWarningSpy = jest.spyOn(core, 'warning').mockImplementation();

      issueLogger.warning(message);

      expect(coreWarningSpy).toHaveBeenCalledTimes(1);
      expect(coreWarningSpy).toHaveBeenCalledWith(
        expect.stringContaining(`[#8]`)
      );
      expect(coreWarningSpy).toHaveBeenCalledWith(
        expect.stringContaining(
          `The ${replacement} will stale! ${replacement} will soon be closed!`
        )
      );
    }
  );

  it.each`
    pull_request      | replacement
    ${{key: 'value'}} | ${'Pull request'}
    ${{}}             | ${'Pull request'}
    ${null}           | ${'Issue'}
    ${undefined}      | ${'Issue'}
  `(
    'should replace the special token "$$type" with the corresponding type with first letter as uppercase',
    ({pull_request, replacement}): void => {
      expect.assertions(3);
      message = '$$type will stale';
      issue = new Issue(
        DefaultProcessorOptions,
        generateIIssue({
          number: 8,
          pull_request
        })
      );
      issueLogger = new IssueLogger(issue);
      coreWarningSpy = jest.spyOn(core, 'warning').mockImplementation();

      issueLogger.warning(message);

      expect(coreWarningSpy).toHaveBeenCalledTimes(1);
      expect(coreWarningSpy).toHaveBeenCalledWith(
        expect.stringContaining(`[#8]`)
      );
      expect(coreWarningSpy).toHaveBeenCalledWith(
        expect.stringContaining(`${replacement} will stale`)
      );
    }
  );
});
```

## File: `src/classes/loggers/issue-logger.ts`
```typescript
import {Issue} from '../issue';
import {Logger} from './logger';
import {LoggerService} from '../../services/logger.service';

/**
 * @description
 * Each log will prefix the message with the issue number
 *
 * @example
 * warning('No stale') => "[#123] No stale"
 *
 * Each log method can have special tokens:
 * - $$type => will replace this by either "pull request" or "issue" depending of the type of issue
 *
 * @example
 * warning('The $$type will stale') => "The pull request will stale"
 */
export class IssueLogger extends Logger {
  private readonly _issue: Issue;

  constructor(issue: Issue) {
    super();
    this._issue = issue;
  }

  warning(...message: string[]): void {
    super.warning(this._format(...message));
  }

  info(...message: string[]): void {
    super.info(this._format(...message));
  }

  error(...message: string[]): void {
    super.error(this._format(...message));
  }

  async grouping(message: string, fn: () => Promise<void>): Promise<void> {
    return super.grouping(this._format(message), fn);
  }

  private _replaceTokens(message: Readonly<string>): string {
    return this._replaceTypeToken(message);
  }

  private _replaceTypeToken(message: Readonly<string>): string {
    return message
      .replace(
        /^\$\$type/,
        this._issue.isPullRequest ? 'Pull request' : 'Issue'
      )
      .replace(
        /\$\$type/g,
        this._issue.isPullRequest ? 'pull request' : 'issue'
      );
  }

  private _prefixWithIssueNumber(message: Readonly<string>): string {
    return `${this._getPrefix()} ${message}`;
  }

  private _getIssueNumber(): number {
    return this._issue.number;
  }

  private _format(...message: string[]): string {
    return this._prefixWithIssueNumber(this._replaceTokens(message.join(' ')));
  }

  private _getPrefix(): string {
    return this._issue.isPullRequest
      ? this._getPullRequestPrefix()
      : this._getIssuePrefix();
  }

  private _getIssuePrefix(): string {
    return LoggerService.red(`[#${this._getIssueNumber()}]`);
  }

  private _getPullRequestPrefix(): string {
    return LoggerService.blue(`[#${this._getIssueNumber()}]`);
  }
}
```

## File: `src/classes/loggers/logger.spec.ts`
```typescript
import {Logger} from './logger';
import * as core from '@actions/core';

describe('Logger', (): void => {
  let logger: Logger;

  beforeEach((): void => {
    logger = new Logger();
  });

  describe('warning()', (): void => {
    let message: string;

    let coreWarningSpy: jest.SpyInstance;

    beforeEach((): void => {
      message = 'dummy-message';

      coreWarningSpy = jest.spyOn(core, 'warning').mockImplementation();
    });

    it('should log a warning with the given message', (): void => {
      expect.assertions(2);

      logger.warning(message);

      expect(coreWarningSpy).toHaveBeenCalledTimes(1);
      expect(coreWarningSpy).toHaveBeenCalledWith(
        expect.stringContaining('dummy-message')
      );
    });
  });

  describe('info()', (): void => {
    let message: string;

    let coreInfoSpy: jest.SpyInstance;

    beforeEach((): void => {
      message = 'dummy-message';

      coreInfoSpy = jest.spyOn(core, 'info').mockImplementation();
    });

    it('should log an information with the given message', (): void => {
      expect.assertions(2);

      logger.info(message);

      expect(coreInfoSpy).toHaveBeenCalledTimes(1);
      expect(coreInfoSpy).toHaveBeenCalledWith(
        expect.stringContaining('dummy-message')
      );
    });
  });

  describe('error()', (): void => {
    let message: string;

    let coreErrorSpy: jest.SpyInstance;

    beforeEach((): void => {
      message = 'dummy-message';

      coreErrorSpy = jest.spyOn(core, 'error').mockImplementation();
    });

    it('should log an error with the given message', (): void => {
      expect.assertions(2);

      logger.error(message);

      expect(coreErrorSpy).toHaveBeenCalledTimes(1);
      expect(coreErrorSpy).toHaveBeenCalledWith(
        expect.stringContaining('dummy-message')
      );
    });
  });
});
```

## File: `src/classes/loggers/logger.ts`
```typescript
import * as core from '@actions/core';
import terminalLink from 'terminal-link';
import {Option} from '../../enums/option';
import {LoggerService} from '../../services/logger.service';

export class Logger {
  warning(...message: string[]): void {
    core.warning(LoggerService.whiteBright(message.join(' ')));
  }

  info(...message: string[]): void {
    core.info(LoggerService.whiteBright(message.join(' ')));
  }

  error(...message: string[]): void {
    core.error(LoggerService.whiteBright(message.join(' ')));
  }

  async grouping(message: string, fn: () => Promise<void>): Promise<void> {
    return core.group(LoggerService.whiteBright(message), fn);
  }

  createLink(name: Readonly<string>, link: Readonly<string>): string {
    return terminalLink(name, link);
  }

  createOptionLink(option: Readonly<Option>): string {
    return LoggerService.magenta(
      this.createLink(option, `https://github.com/actions/stale#${option}`)
    );
  }
}
```

## File: `src/classes/state/state-cache-storage.ts`
```typescript
import {IStateStorage} from '../../interfaces/state/state-storage';
import fs from 'fs';
import path from 'path';
import os from 'os';
import * as core from '@actions/core';
import {context, getOctokit} from '@actions/github';
import {retry as octokitRetry} from '@octokit/plugin-retry';
import * as cache from '@actions/cache';

const CACHE_KEY = '_state';
const STATE_FILE = 'state.txt';
const STALE_DIR = '56acbeaa-1fef-4c79-8f84-7565e560fb03';

const mkTempDir = (): string => {
  const tmpDir = path.join(os.tmpdir(), STALE_DIR);
  fs.mkdirSync(tmpDir, {recursive: true});
  return tmpDir;
};

const unlinkSafely = (filePath: string) => {
  try {
    fs.unlinkSync(filePath);
  } catch (foo) {
    /* ignore */
  }
};

const getOctokitClient = () => {
  const token = core.getInput('repo-token');
  return getOctokit(token, undefined, octokitRetry);
};

const checkIfCacheExists = async (cacheKey: string): Promise<boolean> => {
  const client = getOctokitClient();
  try {
    const cachesResult = await client.rest.actions.getActionsCacheList({
      owner: context.repo.owner,
      repo: context.repo.repo,
      key: cacheKey // prefix matching
    });
    const caches: Array<{key?: string}> =
      cachesResult.data['actions_caches'] || [];
    return caches.some(cache => cache['key'] === cacheKey);
  } catch (error) {
    core.debug(`Error checking if cache exist: ${error.message}`);
  }
  return false;
};
const resetCacheWithOctokit = async (cacheKey: string): Promise<void> => {
  const client = getOctokitClient();
  core.debug(`remove cache "${cacheKey}"`);
  try {
    await client.rest.actions.deleteActionsCacheByKey({
      owner: context.repo.owner,
      repo: context.repo.repo,
      key: cacheKey
    });
  } catch (error) {
    if (error.status) {
      core.warning(
        `Error delete ${cacheKey}: [${error.status}] ${
          error.message || 'Unknown reason'
        }`
      );
    } else {
      throw error;
    }
  }
};
export class StateCacheStorage implements IStateStorage {
  async save(serializedState: string): Promise<void> {
    const tmpDir = mkTempDir();
    const filePath = path.join(tmpDir, STATE_FILE);
    fs.writeFileSync(filePath, serializedState);

    try {
      const cacheExists = await checkIfCacheExists(CACHE_KEY);
      if (cacheExists) {
        await resetCacheWithOctokit(CACHE_KEY);
      }
      const fileSize = fs.statSync(filePath).size;

      if (fileSize === 0) {
        core.info(`the state will be removed`);
        return;
      }

      await cache.saveCache([path.dirname(filePath)], CACHE_KEY);
    } catch (error) {
      core.warning(
        `Saving the state was not successful due to "${
          error.message || 'unknown reason'
        }"`
      );
    } finally {
      unlinkSafely(filePath);
    }
  }

  async restore(): Promise<string> {
    const tmpDir = mkTempDir();
    const filePath = path.join(tmpDir, STATE_FILE);
    unlinkSafely(filePath);
    try {
      const cacheExists = await checkIfCacheExists(CACHE_KEY);
      if (!cacheExists) {
        core.info(
          'The saved state was not found, the process starts from the first issue.'
        );
        return '';
      }

      await cache.restoreCache([path.dirname(filePath)], CACHE_KEY);

      if (!fs.existsSync(filePath)) {
        core.warning(
          'Unknown error when unpacking the cache, the process starts from the first issue.'
        );
        return '';
      }
      return fs.readFileSync(path.join(tmpDir, STATE_FILE), {
        encoding: 'utf8'
      });
    } catch (error) {
      core.warning(
        `Restoring the state was not successful due to "${
          error.message || 'unknown reason'
        }"`
      );
      return '';
    }
  }
}
```

## File: `src/classes/state/state.spec.ts`
```typescript
import {IssueID, State} from './state';
import {IIssuesProcessorOptions} from '../../interfaces/issues-processor-options';
import {IIssue} from '../../interfaces/issue';
import {IState} from '../../interfaces/state/state';
import * as core from '@actions/core';

const mockStorage = {
  save: () => Promise.resolve(),
  restore: () => Promise.resolve('')
};

const getProcessedIssuesIDs = (state: IState): Set<IssueID> =>
  (state as unknown as {processedIssuesIDs: Set<IssueID>}).processedIssuesIDs;

describe('State', () => {
  let debugSpy: jest.SpyInstance;
  let infoSpy: jest.SpyInstance;
  let warningSpy: jest.SpyInstance;
  beforeEach(() => {
    debugSpy = jest.spyOn(core, 'debug');
    infoSpy = jest.spyOn(core, 'info');
    warningSpy = jest.spyOn(core, 'warning');
  });

  afterEach(() => {
    jest.resetAllMocks();
    jest.clearAllMocks();
  });

  describe('initializing and resetting', () => {
    it('new state should not contain any issues marked as proceeded', async () => {
      const state = new State(
        mockStorage,
        {} as unknown as IIssuesProcessorOptions
      );
      expect(getProcessedIssuesIDs(state)).toEqual(new Set());
      expect(debugSpy).not.toHaveBeenCalled();
    });
    it('reset state should not contain any issues marked as proceeded', async () => {
      const state = new State(
        mockStorage,
        {} as unknown as IIssuesProcessorOptions
      );
      state.addIssueToProcessed({number: 1} as unknown as IIssue);
      expect(getProcessedIssuesIDs(state)).not.toEqual(new Set());
      state.reset();
      expect(getProcessedIssuesIDs(state)).toEqual(new Set());
      expect(debugSpy).toHaveBeenCalledTimes(2);
      expect(debugSpy).toHaveBeenCalledWith('state: reset');
    });
  });
  describe('marking as proceeded', () => {
    it('state marked with issues 1,2,3 as proceeded should report the as proceeded', async () => {
      const state = new State(
        mockStorage,
        {} as unknown as IIssuesProcessorOptions
      );
      state.addIssueToProcessed({number: 1} as unknown as IIssue);
      state.addIssueToProcessed({number: 2} as unknown as IIssue);
      state.addIssueToProcessed({number: 3} as unknown as IIssue);
      expect(getProcessedIssuesIDs(state)).toEqual(new Set([1, 2, 3]));
      expect(
        state.isIssueProcessed({number: 1} as unknown as IIssue)
      ).toBeTruthy();
      expect(
        state.isIssueProcessed({number: 2} as unknown as IIssue)
      ).toBeTruthy();
      expect(
        state.isIssueProcessed({number: 3} as unknown as IIssue)
      ).toBeTruthy();
      expect(
        state.isIssueProcessed({number: 0} as unknown as IIssue)
      ).toBeFalsy();
      expect(
        state.isIssueProcessed({number: 4} as unknown as IIssue)
      ).toBeFalsy();
      expect(debugSpy).toHaveBeenCalledTimes(3);
      expect(debugSpy).toHaveBeenCalledWith('state: mark 1 as processed');
      expect(debugSpy).toHaveBeenCalledWith('state: mark 2 as processed');
      expect(debugSpy).toHaveBeenCalledWith('state: mark 3 as processed');
    });
  });
  describe('persisting', () => {
    it('[1,2,3] should be serialized and persisted as to "1|2|3|', async () => {
      const mockStorage = {
        save: jest.fn().mockReturnValue(Promise.resolve()),
        async restore(): Promise<string> {
          return '';
        }
      };
      const state = new State(
        mockStorage,
        {} as unknown as IIssuesProcessorOptions
      );
      state.addIssueToProcessed({number: 1} as unknown as IIssue);
      state.addIssueToProcessed({number: 2} as unknown as IIssue);
      state.addIssueToProcessed({number: 3} as unknown as IIssue);
      await state.persist();
      expect(mockStorage.save).toHaveBeenCalledTimes(1);
      expect(mockStorage.save).toHaveBeenCalledWith('1|2|3');
      expect(infoSpy).toHaveBeenCalledTimes(1);
      expect(infoSpy).toHaveBeenCalledWith(
        'state: persisting info about 3 issue(s)'
      );
    });
  });
  describe('rehydrating', () => {
    it('"1|2|3" should be rehydrate to the IState with issues 1,2,3 marked as proceeded', async () => {
      const mockStorage = {
        save: () => Promise.resolve(),
        restore: () => Promise.resolve('1|2|3')
      };
      const state = new State(
        mockStorage,
        {} as unknown as IIssuesProcessorOptions
      );
      await state.restore();
      const processedIssuesIDs = (
        state as unknown as {processedIssuesIDs: Set<IssueID>}
      ).processedIssuesIDs;
      expect(processedIssuesIDs).toEqual(new Set([1, 2, 3]));
      expect(infoSpy).toHaveBeenCalledTimes(1);
      expect(infoSpy).toHaveBeenCalledWith(
        'state: restored with info about 3 issue(s)'
      );
    });
  });
  describe('debugOnly', () => {
    it('state should persisted if debugOnly not set', () => {
      const mockStorage = {
        save: jest.fn().mockReturnValue(Promise.resolve()),
        async restore(): Promise<string> {
          return '';
        }
      };
      const state = new State(
        mockStorage,
        {} as unknown as IIssuesProcessorOptions
      );
      state.persist();
      expect(mockStorage.save).toHaveBeenCalledTimes(1);
    });
    it('state should not be persisted if debugOnly set true', () => {
      const mockStorage = {
        save: jest.fn().mockReturnValue(Promise.resolve()),
        async restore(): Promise<string> {
          return '';
        }
      };
      const state = new State(mockStorage, {
        debugOnly: true
      } as unknown as IIssuesProcessorOptions);
      state.persist();
      expect(mockStorage.save).not.toHaveBeenCalled();
      expect(warningSpy).toHaveBeenCalledTimes(1);
      expect(warningSpy).toHaveBeenCalledWith(
        'The state is not persisted in the debug mode'
      );
    });
  });
});
```

## File: `src/classes/state/state.ts`
```typescript
import {IState} from '../../interfaces/state/state';
import * as core from '@actions/core';
import {IIssuesProcessorOptions} from '../../interfaces/issues-processor-options';
import {IStateStorage} from '../../interfaces/state/state-storage';
import {IIssue} from '../../interfaces/issue';

export type IssueID = number;

export class NoStateError extends Error {}

export class State implements IState {
  /**
   * @private don't mutate in the debug mode
   */
  private readonly debug: boolean;
  private readonly processedIssuesIDs: Set<IssueID>;
  private readonly stateStorage: IStateStorage;

  constructor(stateStorage: IStateStorage, options: IIssuesProcessorOptions) {
    this.debug = options.debugOnly;
    this.processedIssuesIDs = new Set();
    this.stateStorage = stateStorage;
  }

  isIssueProcessed(issue: IIssue) {
    return this.processedIssuesIDs.has(issue.number);
  }

  addIssueToProcessed(issue: IIssue) {
    core.debug(`state: mark ${issue.number} as processed`);
    this.processedIssuesIDs.add(issue.number);
  }

  reset() {
    core.debug('state: reset');
    this.processedIssuesIDs.clear();
  }

  private deserialize(serialized: string) {
    const issueIDs = serialized
      .split('|')
      .map(id => parseInt(id))
      .filter(i => !isNaN(i));
    this.processedIssuesIDs.clear();
    issueIDs.forEach(issueID => this.processedIssuesIDs.add(issueID));
  }

  private get serialized(): string {
    return Array.from(this.processedIssuesIDs).join('|');
  }

  async persist(): Promise<void> {
    if (this.debug) {
      core.warning('The state is not persisted in the debug mode');
      return;
    }
    core.info(
      `state: persisting info about ${this.processedIssuesIDs.size} issue(s)`
    );
    return this.stateStorage.save(this.serialized);
  }

  async restore(): Promise<void> {
    this.reset();
    const serialized = await this.stateStorage.restore();
    this.deserialize(serialized);
    if (this.processedIssuesIDs.size > 0)
      core.info(
        `state: restored with info about ${this.processedIssuesIDs.size} issue(s)`
      );
  }
}
```

## File: `src/enums/issue-type.ts`
```typescript
export enum IssueType {
  Issue = 'issue',
  PullRequest = 'pr'
}
```

## File: `src/enums/option.ts`
```typescript
export enum Option {
  RepoToken = 'repo-token',
  StaleIssueMessage = 'stale-issue-message',
  StalePrMessage = 'stale-pr-message',
  CloseIssueMessage = 'close-issue-message',
  ClosePrMessage = 'close-pr-message',
  DaysBeforeStale = 'days-before-stale',
  DaysBeforeIssueStale = 'days-before-issue-stale',
  DaysBeforePrStale = 'days-before-pr-stale',
  DaysBeforeClose = 'days-before-close',
  DaysBeforeIssueClose = 'days-before-issue-close',
  DaysBeforePrClose = 'days-before-pr-close',
  StaleIssueLabel = 'stale-issue-label',
  CloseIssueLabel = 'close-issue-label',
  ExemptIssueLabels = 'exempt-issue-labels',
  StalePrLabel = 'stale-pr-label',
  ClosePrLabel = 'close-pr-label',
  ExemptPrLabels = 'exempt-pr-labels',
  OnlyLabels = 'only-labels',
  OnlyIssueLabels = 'only-issue-labels',
  OnlyPrLabels = 'only-pr-labels',
  AnyOfLabels = 'any-of-labels',
  OperationsPerRun = 'operations-per-run',
  RemoveStaleWhenUpdated = 'remove-stale-when-updated',
  RemoveIssueStaleWhenUpdated = 'remove-issue-stale-when-updated',
  RemovePrStaleWhenUpdated = 'remove-pr-stale-when-updated',
  DebugOnly = 'debug-only',
  Ascending = 'ascending',
  SortBy = 'sort-by',
  DeleteBranch = 'delete-branch',
  StartDate = 'start-date',
  ExemptMilestones = 'exempt-milestones',
  ExemptIssueMilestones = 'exempt-issue-milestones',
  ExemptPrMilestones = 'exempt-pr-milestones',
  ExemptAllMilestones = 'exempt-all-milestones',
  ExemptAllIssueMilestones = 'exempt-all-issue-milestones',
  ExemptAllPrMilestones = 'exempt-all-pr-milestones',
  ExemptAssignees = 'exempt-assignees',
  ExemptIssueAssignees = 'exempt-issue-assignees',
  ExemptPrAssignees = 'exempt-pr-assignees',
  ExemptAllAssignees = 'exempt-all-assignees',
  ExemptAllIssueAssignees = 'exempt-all-issue-assignees',
  ExemptAllPrAssignees = 'exempt-all-pr-assignees',
  EnableStatistics = 'enable-statistics',
  LabelsToRemoveWhenStale = 'labels-to-remove-when-stale',
  LabelsToRemoveWhenUnstale = 'labels-to-remove-when-unstale',
  LabelsToAddWhenUnstale = 'labels-to-add-when-unstale',
  IgnoreUpdates = 'ignore-updates',
  IgnoreIssueUpdates = 'ignore-issue-updates',
  IgnorePrUpdates = 'ignore-pr-updates',
  ExemptDraftPr = 'exempt-draft-pr',
  CloseIssueReason = 'close-issue-reason',
  OnlyIssueTypes = 'only-issue-types'
}
```

## File: `src/functions/clean-label.ts`
```typescript
import deburr from 'lodash.deburr';
import {CleanLabel} from '../types/clean-label';

/**
 * @description
 * Clean a label by lowercasing it and deburring it for consistency
 *
 * @param {string} label A raw GitHub label
 *
 * @return {string} A lowercased, deburred version of the passed in label
 */
export function cleanLabel(label?: Readonly<string>): CleanLabel {
  return deburr(label?.toLowerCase());
}
```

## File: `src/functions/get-sort-field.ts`
```typescript
type sortOptions = 'created' | 'updated' | 'comments';
export function getSortField(sortOption: sortOptions): sortOptions {
  return sortOption === 'updated'
    ? 'updated'
    : sortOption === 'comments'
    ? 'comments'
    : 'created';
}
```

## File: `src/functions/is-boolean.spec.ts`
```typescript
import {isBoolean} from './is-boolean';

describe('isBoolean()', (): void => {
  describe.each([0, 1, undefined, null, ''])(
    'when the given value is not a boolean',
    (value): void => {
      it('should return false', (): void => {
        expect.assertions(1);

        const result = isBoolean(value);

        expect(result).toStrictEqual(false);
      });
    }
  );

  describe.each([false, true])(
    'when the given value is a boolean',
    (value): void => {
      it('should return true', (): void => {
        expect.assertions(1);

        const result = isBoolean(value);

        expect(result).toStrictEqual(true);
      });
    }
  );
});
```

## File: `src/functions/is-boolean.ts`
```typescript
export function isBoolean(value: unknown): value is boolean {
  return value === true || value === false;
}
```

## File: `src/functions/is-labeled.spec.ts`
```typescript
import {Issue} from '../classes/issue';
import {isLabeled} from './is-labeled';

describe('isLabeled()', (): void => {
  let issue: Issue;
  let label: string;

  describe('when the given issue contains no label', (): void => {
    beforeEach((): void => {
      issue = {
        labels: []
      } as unknown as Issue;
    });

    describe('when the given label is a simple label', (): void => {
      beforeEach((): void => {
        label = 'label';
      });

      it('should return false', (): void => {
        expect.assertions(1);

        const result = isLabeled(issue, label);

        expect(result).toStrictEqual(false);
      });
    });
  });

  describe('when the given issue contains a simple label', (): void => {
    beforeEach((): void => {
      issue = {
        labels: [
          {
            name: 'label'
          }
        ]
      } as Issue;
    });

    describe('when the given label is a simple label', (): void => {
      beforeEach((): void => {
        label = 'label';
      });

      it('should return true', (): void => {
        expect.assertions(1);

        const result = isLabeled(issue, label);

        expect(result).toStrictEqual(true);
      });
    });
  });

  describe('when the given issue contains a kebab case label', (): void => {
    beforeEach((): void => {
      issue = {
        labels: [
          {
            name: 'kebab-case-label'
          }
        ]
      } as Issue;
    });

    describe('when the given label is a kebab case label', (): void => {
      beforeEach((): void => {
        label = 'kebab-case-label';
      });

      it('should return true', (): void => {
        expect.assertions(1);

        const result = isLabeled(issue, label);

        expect(result).toStrictEqual(true);
      });
    });
  });

  describe('when the given issue contains a multiple word label', (): void => {
    beforeEach((): void => {
      issue = {
        labels: [
          {
            name: 'label like a sentence'
          }
        ]
      } as Issue;
    });

    describe('when the given label is a multiple word label', (): void => {
      beforeEach((): void => {
        label = 'label like a sentence';
      });

      it('should return true', (): void => {
        expect.assertions(1);

        const result = isLabeled(issue, label);

        expect(result).toStrictEqual(true);
      });
    });
  });

  describe('when the given issue contains a multiple word label with %20 spaces', (): void => {
    beforeEach((): void => {
      issue = {
        labels: [
          {
            name: 'label%20like%20a%20sentence'
          }
        ]
      } as Issue;
    });

    describe('when the given label is a multiple word label with %20 spaces', (): void => {
      beforeEach((): void => {
        label = 'label%20like%20a%20sentence';
      });

      it('should return true', (): void => {
        expect.assertions(1);

        const result = isLabeled(issue, label);

        expect(result).toStrictEqual(true);
      });
    });
  });

  describe('when the given issue contains a label wih diacritical marks', (): void => {
    beforeEach((): void => {
      issue = {
        labels: [
          {
            name: 'déjà vu'
          }
        ]
      } as Issue;
    });

    describe('when the given issue contains a label', (): void => {
      beforeEach((): void => {
        label = 'deja vu';
      });

      it('should return true', (): void => {
        expect.assertions(1);

        const result = isLabeled(issue, label);

        expect(result).toStrictEqual(true);
      });
    });

    describe('when the given issue contains an uppercase label', (): void => {
      beforeEach((): void => {
        label = 'DEJA VU';
      });

      it('should return true', (): void => {
        expect.assertions(1);

        const result = isLabeled(issue, label);

        expect(result).toStrictEqual(true);
      });
    });

    describe('when the given issue contains a label wih diacritical marks', (): void => {
      beforeEach((): void => {
        label = 'déjà vu';
      });

      it('should return true', (): void => {
        expect.assertions(1);

        const result = isLabeled(issue, label);

        expect(result).toStrictEqual(true);
      });
    });
  });
});
```

## File: `src/functions/is-labeled.ts`
```typescript
import {Issue} from '../classes/issue';
import {ILabel} from '../interfaces/label';
import {cleanLabel} from './clean-label';

/**
 * @description
 * Check if the given label is listed as a label of the given issue
 *
 * @param {Readonly<Issue>} issue A GitHub issue containing some labels
 * @param {Readonly<string>} label The label to check the presence with
 *
 * @return {boolean} Return true when the given label is also in the given issue labels
 */
export function isLabeled(
  issue: Readonly<Issue>,
  label: Readonly<string>
): boolean {
  return !!issue.labels.find((issueLabel: Readonly<ILabel>): boolean => {
    return cleanLabel(label) === cleanLabel(issueLabel.name);
  });
}
```

## File: `src/functions/is-pull-request.spec.ts`
```typescript
import {Issue} from '../classes/issue';
import {isPullRequest} from './is-pull-request';

describe('isPullRequest()', (): void => {
  let issue: Issue;

  describe('when the given issue has an undefined pull request', (): void => {
    beforeEach((): void => {
      issue = {
        pull_request: undefined
      } as Issue;
    });

    it('should return false', (): void => {
      expect.assertions(1);

      const result = isPullRequest(issue);

      expect(result).toStrictEqual(false);
    });
  });

  describe('when the given issue has a null pull request', (): void => {
    beforeEach((): void => {
      issue = {
        pull_request: null
      } as Issue;
    });

    it('should return false', (): void => {
      expect.assertions(1);

      const result = isPullRequest(issue);

      expect(result).toStrictEqual(false);
    });
  });

  describe.each([{}, true])(
    'when the given issue has pull request',
    (value): void => {
      beforeEach((): void => {
        issue = {
          pull_request: value
        } as Issue;
      });

      it('should return true', (): void => {
        expect.assertions(1);

        const result = isPullRequest(issue);

        expect(result).toStrictEqual(true);
      });
    }
  );
});
```

## File: `src/functions/is-pull-request.ts`
```typescript
import {Issue} from '../classes/issue';

export function isPullRequest(issue: Readonly<Issue>): boolean {
  return !!issue.pull_request;
}
```

## File: `src/functions/should-mark-when-stale.spec.ts`
```typescript
import {shouldMarkWhenStale} from './should-mark-when-stale';

describe('shouldMarkWhenStale()', (): void => {
  let daysBeforeStale: number;

  describe('when the given number of days indicate that it should be stalled', (): void => {
    beforeEach((): void => {
      daysBeforeStale = -1;
    });

    it('should return false', (): void => {
      expect.assertions(1);

      const result = shouldMarkWhenStale(daysBeforeStale);

      expect(result).toStrictEqual(false);
    });
  });

  describe('when the given number of days indicate that it should be stalled today', (): void => {
    beforeEach((): void => {
      daysBeforeStale = 0;
    });

    it('should return true', (): void => {
      expect.assertions(1);

      const result = shouldMarkWhenStale(daysBeforeStale);

      expect(result).toStrictEqual(true);
    });
  });

  describe('when the given number of days indicate that it should be stalled tomorrow', (): void => {
    beforeEach((): void => {
      daysBeforeStale = 1;
    });

    it('should return true', (): void => {
      expect.assertions(1);

      const result = shouldMarkWhenStale(daysBeforeStale);

      expect(result).toStrictEqual(true);
    });
  });
});
```

## File: `src/functions/should-mark-when-stale.ts`
```typescript
export function shouldMarkWhenStale(
  daysBeforeStale: Readonly<number>
): boolean {
  return daysBeforeStale >= 0;
}
```

## File: `src/functions/words-to-list.spec.ts`
```typescript
import {wordsToList} from './words-to-list';

describe('wordsToList()', (): void => {
  let words: string;

  describe('when the given words is empty', (): void => {
    beforeEach((): void => {
      words = '';
    });

    it('should return an empty list of words', (): void => {
      expect.assertions(1);

      const result = wordsToList(words);

      expect(result).toStrictEqual([]);
    });
  });

  describe('when the given words is a simple word', (): void => {
    beforeEach((): void => {
      words = 'word';
    });

    it('should return a list of one word', (): void => {
      expect.assertions(1);

      const result = wordsToList(words);

      expect(result).toStrictEqual(['word']);
    });
  });

  describe('when the given words is a word with extra spaces before and after', (): void => {
    beforeEach((): void => {
      words = '   word   ';
    });

    it('should return a list of one word and remove all spaces before and after', (): void => {
      expect.assertions(1);

      const result = wordsToList(words);

      expect(result).toStrictEqual(['word']);
    });
  });

  describe('when the given words is a kebab case word', (): void => {
    beforeEach((): void => {
      words = 'kebab-case-word';
    });

    it('should return a list of one word', (): void => {
      expect.assertions(1);

      const result = wordsToList(words);

      expect(result).toStrictEqual(['kebab-case-word']);
    });
  });

  describe('when the given words is two kebab case words separated with a comma', (): void => {
    beforeEach((): void => {
      words = 'kebab-case-word-1,kebab-case-word-2';
    });

    it('should return a list of two words', (): void => {
      expect.assertions(1);

      const result = wordsToList(words);

      expect(result).toStrictEqual(['kebab-case-word-1', 'kebab-case-word-2']);
    });
  });

  describe('when the given words is a multiple word word', (): void => {
    beforeEach((): void => {
      words = 'word like a sentence';
    });

    it('should return a list of one word', (): void => {
      expect.assertions(1);

      const result = wordsToList(words);

      expect(result).toStrictEqual(['word like a sentence']);
    });
  });

  describe('when the given words is two multiple word words separated with a comma', (): void => {
    beforeEach((): void => {
      words = 'word like a sentence, another word like a sentence';
    });

    it('should return a list of two words', (): void => {
      expect.assertions(1);

      const result = wordsToList(words);

      expect(result).toStrictEqual([
        'word like a sentence',
        'another word like a sentence'
      ]);
    });
  });

  describe('when the given words is a multiple word word with %20 spaces', (): void => {
    beforeEach((): void => {
      words = 'word%20like%20a%20sentence';
    });

    it('should return a list of one word', (): void => {
      expect.assertions(1);

      const result = wordsToList(words);

      expect(result).toStrictEqual(['word%20like%20a%20sentence']);
    });
  });

  describe('when the given words is two multiple word words with %20 spaces separated with a comma', (): void => {
    beforeEach((): void => {
      words = 'word%20like%20a%20sentence,another%20word%20like%20a%20sentence';
    });

    it('should return a list of two words', (): void => {
      expect.assertions(1);

      const result = wordsToList(words);

      expect(result).toStrictEqual([
        'word%20like%20a%20sentence',
        'another%20word%20like%20a%20sentence'
      ]);
    });
  });
});
```

## File: `src/functions/words-to-list.ts`
```typescript
/**
 * @description
 * Transform a string of comma separated words
 * to an array of words
 *
 * @example
 * wordsToList('label') => ['label']
 * wordsToList('label,label') => ['label', 'label']
 * wordsToList('kebab-label') => ['kebab-label']
 * wordsToList('kebab%20label') => ['kebab%20label']
 * wordsToList('label with words') => ['label with words']
 *
 * @param {Readonly<string>} words A string of comma separated words
 *
 * @return {string[]} A list of words
 */
export function wordsToList(words: Readonly<string>): string[] {
  if (!words.length) {
    return [];
  }

  return words.split(',').map((word: Readonly<string>): string => word.trim());
}
```

## File: `src/functions/dates/get-humanized-date.spec.ts`
```typescript
import {getHumanizedDate} from './get-humanized-date';

describe('getHumanizedDate()', (): void => {
  let date: Date;

  describe('when the given date is the 1st of april 2020', (): void => {
    beforeEach((): void => {
      date = new Date(2020, 3, 1);
    });

    it('should return the date formatted as DD-MM-YYYY', (): void => {
      expect.assertions(1);

      const result = getHumanizedDate(date);

      expect(result).toStrictEqual('01-04-2020');
    });
  });

  describe('when the given date is the 18st of december 2020', (): void => {
    beforeEach((): void => {
      date = new Date(2020, 11, 18);
    });

    it('should return the date formatted as DD-MM-YYYY', (): void => {
      expect.assertions(1);

      const result = getHumanizedDate(date);

      expect(result).toStrictEqual('18-12-2020');
    });
  });
});
```

## File: `src/functions/dates/get-humanized-date.ts`
```typescript
import {HumanizedDate} from '../../types/humanized-date';

export function getHumanizedDate(date: Readonly<Date>): HumanizedDate {
  const year: number = date.getFullYear();
  let month = `${date.getMonth() + 1}`;
  let day = `${date.getDate()}`;

  if (month.length < 2) {
    month = `0${month}`;
  }

  if (day.length < 2) {
    day = `0${day}`;
  }

  return [day, month, year].join('-');
}
```

## File: `src/functions/dates/is-date-more-recent-than.spec.ts`
```typescript
import {isDateEqualTo, isDateMoreRecentThan} from './is-date-more-recent-than';

describe('isDateMoreRecentThan()', (): void => {
  let date: Date;
  let comparedDate: Date;

  describe('when the given date is older than the compared date', (): void => {
    beforeEach((): void => {
      date = new Date(2020, 0, 20);
      comparedDate = new Date(2021, 0, 20);
    });

    it('should return false', (): void => {
      expect.assertions(1);

      const result = isDateMoreRecentThan(date, comparedDate);

      expect(result).toStrictEqual(false);
    });
  });

  describe('when the given date is equal to the compared date', (): void => {
    beforeEach((): void => {
      date = new Date(2020, 0, 20);
      comparedDate = new Date(2020, 0, 20);
    });

    it('should return false', (): void => {
      expect.assertions(1);

      const result = isDateMoreRecentThan(date, comparedDate);

      expect(result).toStrictEqual(false);
    });
  });

  describe('when the given date is more recent than the compared date', (): void => {
    beforeEach((): void => {
      date = new Date(2021, 0, 20);
      comparedDate = new Date(2020, 0, 20);
    });

    it('should return true', (): void => {
      expect.assertions(1);

      const result = isDateMoreRecentThan(date, comparedDate);

      expect(result).toStrictEqual(true);
    });
  });

  describe('date equality', (): void => {
    it('should correctly compare a before date outside tolerance', (): void => {
      const aDate = new Date('2022-09-09T13:00:00');
      const otherDate = new Date('2022-09-09T14:00:00');
      expect(isDateEqualTo(aDate, otherDate, 60)).toBe(false);
    });

    it('should correctly compare a before date inside tolerance', (): void => {
      const aDate = new Date('2022-09-09T13:00:00');
      const otherDate = new Date('2022-09-09T13:00:42');
      expect(isDateEqualTo(aDate, otherDate, 60)).toBe(true);
    });

    it('should correctly compare an after date outside tolerance', (): void => {
      const aDate = new Date('2022-09-09T13:00:00');
      const otherDate = new Date('2022-09-09T12:00:00');
      expect(isDateEqualTo(aDate, otherDate, 60)).toBe(false);
    });

    it('should correctly compare an after date inside tolerance', (): void => {
      const aDate = new Date('2022-09-09T13:00:00');
      const otherDate = new Date('2022-09-09T12:59:42');
      expect(isDateEqualTo(aDate, otherDate, 60)).toBe(true);
    });

    it('should correctly compare an exactly equal date', (): void => {
      const aDate = new Date('2022-09-09T13:00:00');
      const otherDate = new Date('2022-09-09T13:00:00');
      expect(isDateEqualTo(aDate, otherDate, 60)).toBe(true);
    });
  });

  describe('date comparison with tolerances', (): void => {
    it('should correctly compare a before date outside tolerance', (): void => {
      const aDate = new Date('2022-09-09T13:00:00');
      const otherDate = new Date('2022-09-09T14:00:00');
      expect(isDateMoreRecentThan(aDate, otherDate)).toBe(false);
    });

    it('should correctly compare a before date inside tolerance', (): void => {
      const aDate = new Date('2022-09-09T13:00:00');
      const otherDate = new Date('2022-09-09T13:00:42');
      expect(isDateMoreRecentThan(aDate, otherDate, 60)).toBe(false); // considered equal here
    });

    it('should correctly compare an after date outside tolerance', (): void => {
      const aDate = new Date('2022-09-09T13:00:00');
      const otherDate = new Date('2022-09-09T12:00:00');
      expect(isDateMoreRecentThan(aDate, otherDate, 60)).toBe(true);
    });

    it('should correctly compare an after date inside tolerance', (): void => {
      const aDate = new Date('2022-09-09T13:00:00');
      const otherDate = new Date('2022-09-09T12:59:42');
      expect(isDateMoreRecentThan(aDate, otherDate, 60)).toBe(false); // considered equal here
    });

    it('should correctly compare an exactly equal date', (): void => {
      const aDate = new Date('2022-09-09T13:00:00');
      const otherDate = new Date('2022-09-09T13:00:00');
      expect(isDateMoreRecentThan(aDate, otherDate, 60)).toBe(false);
    });
  });
});
```

## File: `src/functions/dates/is-date-more-recent-than.ts`
```typescript
/// returns false if the dates are equal within the `equalityToleranceInSeconds` number of seconds
/// otherwise returns true if `comparedDate` is after `date`

export function isDateMoreRecentThan(
  date: Readonly<Date>,
  comparedDate: Readonly<Date>,
  equalityToleranceInSeconds = 0
): boolean {
  if (equalityToleranceInSeconds > 0) {
    const areDatesEqual = isDateEqualTo(
      date,
      comparedDate,
      equalityToleranceInSeconds
    );

    return !areDatesEqual && date > comparedDate;
  }

  return date > comparedDate;
}

export function isDateEqualTo(
  date: Date,
  otherDate: Date,
  toleranceInSeconds: number
): boolean {
  const timestamp = date.getTime();
  const otherTimestamp = otherDate.getTime();
  const deltaInSeconds = Math.abs(timestamp - otherTimestamp) / 1000;
  return deltaInSeconds <= toleranceInSeconds;
}
```

## File: `src/functions/dates/is-valid-date.spec.ts`
```typescript
import {isValidDate} from './is-valid-date';

describe('isValidDate()', (): void => {
  let date: Date;

  describe('when the given date is an invalid date', (): void => {
    beforeEach((): void => {
      date = new Date('16-04-1994');
    });

    it('should return false', (): void => {
      expect.assertions(1);

      const result = isValidDate(date);

      expect(result).toStrictEqual(false);
    });
  });

  describe('when the given date is a new date', (): void => {
    beforeEach((): void => {
      date = new Date();
    });

    it('should return true', (): void => {
      expect.assertions(1);

      const result = isValidDate(date);

      expect(result).toStrictEqual(true);
    });
  });

  describe('when the given date is an ISO and valid date', (): void => {
    beforeEach((): void => {
      date = new Date('2011-04-22T13:33:48Z');
    });

    it('should return true', (): void => {
      expect.assertions(1);

      const result = isValidDate(date);

      expect(result).toStrictEqual(true);
    });
  });

  describe('when the given date is an ISO with ms and valid date', (): void => {
    beforeEach((): void => {
      date = new Date('2011-10-05T14:48:00.000Z');
    });

    it('should return true', (): void => {
      expect.assertions(1);

      const result = isValidDate(date);

      expect(result).toStrictEqual(true);
    });
  });
});
```

## File: `src/functions/dates/is-valid-date.ts`
```typescript
/**
 * @description
 * Check if a date is valid
 *
 * @see
 * https://stackoverflow.com/a/1353711/4440414
 *
 * @param {Readonly<Date>} date The date to check
 *
 * @returns {boolean} true when the given date is valid
 */
export function isValidDate(date: Readonly<Date>): boolean {
  if (Object.prototype.toString.call(date) === '[object Date]') {
    return !isNaN(date.getTime());
  }

  return false;
}
```

## File: `src/interfaces/assignee.ts`
```typescript
// @todo improve to include the notion of team?
interface IAssignee {
  type: string;
}

export interface IUserAssignee extends IAssignee {
  login: string;
  type: 'User' | string;
}

export type Assignee = IUserAssignee;
```

## File: `src/interfaces/comment.ts`
```typescript
import {IUser} from './user';

export interface IComment {
  user: IUser | null;
  body?: string;
}
```

## File: `src/interfaces/issue-event.ts`
```typescript
import {ILabel} from './label';

export interface IIssueEvent {
  created_at: string;
  event: string;
  label: ILabel;
}
```

## File: `src/interfaces/issue.ts`
```typescript
import {IsoDateString} from '../types/iso-date-string';
import {Assignee} from './assignee';
import {ILabel} from './label';
import {IMilestone} from './milestone';
import {components} from '@octokit/openapi-types';
export interface IIssue {
  title: string;
  number: number;
  created_at: IsoDateString;
  updated_at: IsoDateString;
  draft: boolean;
  labels: ILabel[];
  pull_request?: object | null;
  state: string;
  locked: boolean;
  milestone?: IMilestone | null;
  assignees?: Assignee[] | null;
  issue_type?: string;
}

export type OctokitIssue = components['schemas']['issue'];
```

## File: `src/interfaces/issues-processor-options.ts`
```typescript
import {IsoOrRfcDateString} from '../types/iso-or-rfc-date-string';

export interface IIssuesProcessorOptions {
  repoToken: string;
  staleIssueMessage: string;
  stalePrMessage: string;
  closeIssueMessage: string;
  closePrMessage: string;
  daysBeforeStale: number;
  daysBeforeIssueStale: number; // Could be NaN
  daysBeforePrStale: number; // Could be NaN
  daysBeforeClose: number;
  daysBeforeIssueClose: number; // Could be NaN
  daysBeforePrClose: number; // Could be NaN
  staleIssueLabel: string;
  closeIssueLabel: string;
  exemptIssueLabels: string;
  stalePrLabel: string;
  closePrLabel: string;
  exemptPrLabels: string;
  onlyLabels: string;
  onlyIssueLabels: string;
  onlyPrLabels: string;
  anyOfLabels: string;
  anyOfIssueLabels: string;
  anyOfPrLabels: string;
  operationsPerRun: number;
  removeStaleWhenUpdated: boolean;
  removeIssueStaleWhenUpdated: boolean | undefined;
  removePrStaleWhenUpdated: boolean | undefined;
  debugOnly: boolean;
  ascending: boolean;
  sortBy: 'created' | 'updated' | 'comments';
  deleteBranch: boolean;
  startDate: IsoOrRfcDateString | undefined; // Should be ISO 8601 or RFC 2822
  exemptMilestones: string;
  exemptIssueMilestones: string;
  exemptPrMilestones: string;
  exemptAllMilestones: boolean;
  exemptAllIssueMilestones: boolean | undefined;
  exemptAllPrMilestones: boolean | undefined;
  exemptAssignees: string;
  exemptIssueAssignees: string;
  exemptPrAssignees: string;
  exemptAllAssignees: boolean;
  exemptAllIssueAssignees: boolean | undefined;
  exemptAllPrAssignees: boolean | undefined;
  enableStatistics: boolean;
  labelsToRemoveWhenStale: string;
  labelsToRemoveWhenUnstale: string;
  labelsToAddWhenUnstale: string;
  ignoreUpdates: boolean;
  ignoreIssueUpdates: boolean | undefined;
  ignorePrUpdates: boolean | undefined;
  exemptDraftPr: boolean;
  closeIssueReason: string;
  includeOnlyAssigned: boolean;
  onlyIssueTypes?: string;
}
```

## File: `src/interfaces/label.ts`
```typescript
export interface ILabel {
  name?: string;
}
```

## File: `src/interfaces/milestone.ts`
```typescript
export interface IMilestone {
  title: string;
}
```

## File: `src/interfaces/pull-request.ts`
```typescript
export interface IPullRequest {
  number: number;
  head: {
    ref: string;
    repo: {
      full_name: string;
    } | null;
  };
  draft?: boolean;
}
```

## File: `src/interfaces/rate-limit.ts`
```typescript
import {components} from '@octokit/openapi-types';

export interface IRateLimit {
  limit: number;
  used: number;
  remaining: number;
  reset: Date;
}

export type OctokitRateLimit = components['schemas']['rate-limit'];
```

## File: `src/interfaces/user.ts`
```typescript
export interface IUser {
  type: string | 'User';
  login: string;
}
```

## File: `src/interfaces/state/state-storage.ts`
```typescript
export interface IStateStorage {
  save(serializedState: string): Promise<void>;
  restore(): Promise<string>;
}
```

## File: `src/interfaces/state/state.ts`
```typescript
import {IIssue} from '../issue';

export interface IState {
  isIssueProcessed(issue: IIssue): boolean;
  addIssueToProcessed(issue: IIssue): void;
  reset(): void;
  persist(): Promise<void>;
  restore(): Promise<void>;
}
```

## File: `src/services/logger.service.ts`
```typescript
import styles, {Modifier, ForegroundColor} from 'ansi-styles';

type Message = string | number | boolean;

export class LoggerService {
  static whiteBright(message: Readonly<Message>): string {
    return this._format(message, 'whiteBright');
  }

  static yellowBright(message: Readonly<Message>): string {
    return this._format(message, 'yellowBright');
  }

  static magenta(message: Readonly<Message>): string {
    return this._format(message, 'magenta');
  }

  static cyan(message: Readonly<Message>): string {
    return this._format(message, 'cyan');
  }

  static yellow(message: Readonly<Message>): string {
    return this._format(message, 'yellow');
  }

  static white(message: Readonly<Message>): string {
    return this._format(message, 'white');
  }

  static green(message: Readonly<Message>): string {
    return this._format(message, 'green');
  }

  static red(message: Readonly<Message>): string {
    return this._format(message, 'red');
  }

  static blue(message: Readonly<Message>): string {
    return this._format(message, 'blue');
  }

  static bold(message: Readonly<Message>): string {
    return this._format(message, 'bold');
  }

  private static _format(
    message: Readonly<Message>,
    style: keyof Modifier | keyof ForegroundColor
  ): string {
    return `${styles[style].open}${message}${styles[style].close}`;
  }
}
```

## File: `src/services/state.service.ts`
```typescript
import {IState} from '../interfaces/state/state';
import {State} from '../classes/state/state';
import {IIssuesProcessorOptions} from '../interfaces/issues-processor-options';
import {StateCacheStorage} from '../classes/state/state-cache-storage';

export const getStateInstance = (options: IIssuesProcessorOptions): IState => {
  const storage = new StateCacheStorage();
  return new State(storage, options);
};
```

## File: `src/types/clean-label.ts`
```typescript
export type CleanLabel = string;
```

## File: `src/types/humanized-date.ts`
```typescript
export type HumanizedDate = string;
```

## File: `src/types/iso-date-string.ts`
```typescript
export type IsoDateString = string;
```

## File: `src/types/iso-or-rfc-date-string.ts`
```typescript
export type IsoOrRfcDateString = string;
```

