---
id: github.com-release-it-release-it-375942bd-knowledg
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:17.318732
---

# KNOWLEDGE EXTRACT: github.com_release-it_release-it_375942bd
> **Extracted on:** 2026-04-01 09:37:02
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007520313/github.com_release-it_release-it_375942bd

---

## File: `.env.test`
```
GITHUB_TOKEN="1"
GITLAB_TOKEN="1"
```

## File: `.gitignore`
```
.DS_Store
.idea
.vscode
*.log

node_modules
tmp
.npmrc
```

## File: `.npmrc`
```
save-exact=true
engine-strict=true
```

## File: `.nvmrc`
```
20
```

## File: `.prettierrc.json`
```json
{
  "printWidth": 120,
  "singleQuote": true,
  "proseWrap": "always",
  "trailingComma": "none",
  "arrowParens": "avoid"
}
```

## File: `.release-it.json`
```json
{
  "$schema": "./schema/release-it.json",
  "hooks": {
    "after:init": ["npm run lint", "npm run knip", "npm run knip -- --production", "npm test"]
  },
  "github": {
    "tokenRef": "GITHUB_TOKEN_RELEASE_IT",
    "release": true,
    "releaseNotes": {
      "commit": "* ${commit.subject} (${sha}){ - thanks @${author.login}!}",
      "excludeMatches": ["webpro"]
    },
    "comments": {
      "submit": true
    }
  }
}
```

## File: `CHANGELOG.md`
```markdown
# Changelog

This document lists breaking changes for each major release.

See the GitHub Releases page for detailed changelogs: [https://github.com/release-it/release-it/releases][1]

## v20 (2026-03-24)

- Upgraded `undici` from v6 to v7 to resolve security vulnerabilities.
- Upgraded `proxy-agent` from v6 to v7 to fix DEP0169 (`url.parse()` deprecation).
- Migrated from deprecated `inquirer` to `@inquirer/prompts`.
- Bumped `engines.node` to minimum Node.js v20.19.0 (was v20.12.0).

## v19 (2025-04-18)

- No breaking changes (dependency party)

## v18 (2025-01-06)

- Removed support for Node.js v18.

## v17 (2023-11-11)

- Removed support for Node.js v16.

## v16 (2023-07-05)

- Removed support for Node.js v14.

## v15 (2022-04-30)

- Removed support for Node.js v10 and v12.
- Removed support for GitLab v12.4 and lower.
- Removed anonymous metrics (and the option to disable it).
- Programmatic usage and plugins only through ES Module syntax (`import`)

Use release-it v14 in legacy environments.

## v14 (2020-09-03)

- Removed `global` property from plugins. Use `this.config[key]` instead.
- Removed deprecated `npm.access` option. Set this in `package.json` instead.

## v13 (2020-03-07)

- Dropped support for Node v8
- Dropped support for GitLab v11.6 and lower.
- Deprecated `scripts` are removed (in favor of [hooks][2]).
- Removed deprecated `--non-interactive` (`-n`) argument. Use `--ci` instead.
- Removed old `%s` and `[REV_RANGE]` syntax in command substitutions. Use `${version}` and `${latestTag}` instead.

## v12 (2019-05-03)

- The `--follow-tags` argument for `git push` has been moved to the default configuration. This is only a breaking
  change if `git.pushArgs` was not empty (it was empty by default).

## v11

- The custom `conventional-changelog` increment (e.g. `"increment": "conventional:angular"`) with additional script
  configuration is replaced with a plugin. Please see [conventional changelog][3] how to use this plugin.
- The `pkgFiles` option has been removed. If there's a need to bump other files than what `npm version` bumps, it should
  be (part of) a plugin.
- By default, the latest version was derived from the latest Git tag. From v11, if the repo has a `package.json` then
  that `version` is used instead. The `use` option has been removed. Also see [latest version][4].
- `scripts.changelog` has been moved to `git.changelog`

## v10

- Dropped support for Node v6
- Deprecated options from v9 are removed, the `dist.repo` config in particular (also see [distribution repository][5]
  for alternatives).
- Drop the `--debug` flag. `DEBUG=release-it:* ...` still works.

## v9

There should be no breaking changes, but there have been major internal refactorings and an improved UI. A bunch of new
features and bug fixes have been implemented. Last but not least, the configuration structure is changed significantly.
For this (backwards compatible) change, deprecation warnings are shown, and configurations must be migrated with the
next major release (v10).

- All "command hooks" have been moved to `scripts.*`, and some have been renamed.
- All `src.*` options have been moved to `git.*` (and `scripts.*`).
- The `dist.repo` configuration and functionality has been removed.

## v8

- Drop the `--force` flag. It's only use was to move a Git tag.

## v7

- No longer adds untracked files to release commit. (#230)

## v6

- Default value for `requireCleanWorkingDir` is now `true` (previously: `false`). (#173)
- Skip prompt (interactive) if corresponding task (non-interactive) is disabled. E.g. `npm.publish: false` will also not
  show "publish" prompt.

## v5

- Drop support for Node v4.

[Release notes for v5][6]

## v4

- Use `shell.exec` for build commands by default (previously this required a `!` prefix).

[Release notes for v4][7]

## v3

- Configuration filename must be `.release-it.json` (previously `.release.json`).
- Refactored configuration structure in this file (and the CLI arguments with it).

[Release notes for v3][8]

## v2

- Build command is executed before git commit/push.
- Configuration options are better organized. Most of them are backwards compatible with a deprecation notice.

[Release notes for v2][9]

## v1

Initial major release.

[Release notes for v1][10]

[1]: https://github.com/release-it/release-it/releases
[2]: https://github.com/release-it/release-it#hooks
[3]: https://github.com/release-it/release-it/blob/main/docs/changelog.md#conventional-changelog
[4]: https://github.com/release-it/release-it#latest-version
[5]: https://github.com/release-it/release-it/blob/main/docs/recipes/distribution-repo.md
[6]: https://github.com/release-it/release-it/releases/tag/5.0.0-beta.0
[7]: https://github.com/release-it/release-it/releases/tag/4.0.0-rc.0
[8]: https://github.com/release-it/release-it/releases/tag/3.0.0
[9]: https://github.com/release-it/release-it/releases/tag/2.0.0
[10]: https://github.com/release-it/release-it/releases/tag/1.0.0
```

## File: `LICENSE`
```
MIT License

Copyright (c) 2018 Lars Kappert

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## File: `README.md`
```markdown
# Release It! 🚀

🚀 Generic CLI tool to automate versioning and package publishing-related tasks:

<img align="right" src="./docs/assets/release-it.svg?raw=true" height="280" />

- Bump version (in e.g. `package.json`)
- [Git commit, tag, push][1]
- Execute any (test or build) commands using [hooks][2]
- [Create release at GitHub][3] or [GitLab][4]
- [Generate changelog][5]
- [Publish to npm][6]
- [Manage pre-releases][7]
- Extend with [plugins][8]
- Release from any [CI/CD environment][9]

Use release-it for version management and publish to anywhere with its versatile configuration, a powerful plugin
system, and hooks to execute any command you need to test, build, and/or publish your project.

[![Action Status][11]][10] [![npm version][13]][12]

Are you using release-it at work? Please consider [sponsoring me][14]!

## Installation

Although release-it is a **generic** release tool, most projects use it for projects with npm packages. The recommended
way to install release-it uses npm and adds some minimal configuration to get started:

```bash
npm init release-it
```

Alternatively, install it manually, and add the `release` script to `package.json`:

```bash
npm install -D release-it
```

```json
{
  "name": "my-package",
  "version": "1.0.0",
  "scripts": {
    "release": "release-it"
  },
  "devDependencies": {
    "release-it": "^20.0.0"
  }
}
```

## Usage

Run release-it from the root of the project using either `npm run` or `npx`:

```bash
npm run release
npx release-it
```

You will be prompted to select the new version, and more prompts will follow based on your configuration.

## Yarn & pnpm

- Using Yarn? Please see the [npm section on Yarn][15].
- Using pnpm? Please see [release-it-pnpm][16].

## Monorepos

Using a monorepo? Please see this [monorepo recipe][17].

## Global Installation

Per-project installation as shown above is recommended, but global installs are supported as well:

- From npm: `npm install -g release-it`
- From Homebrew: `brew install release-it`

## Containerized

Use [Release It! - Containerized][18] to run it in any environment as a standardized container without the need for a
Node environment. Thanks [Juan Carlos][19]!

## Videos, articles & examples

Here's a list of interesting external resources:

- Video: [How to use GitHub Actions & Release-It to Easily Release Your Code][20]
- Article: [Monorepo Semantic Releases][21] ([repo][22])

Want to add yours to the list? Just open a pull request!

## Configuration

Out of the box, release-it has sane defaults, and [plenty of options][23] to configure it. Most projects use a
`.release-it.json` file in the project root, or a `release-it` property in `package.json`.

Here's a quick example `.release-it.json`:

```json
{
  "$schema": "https://unpkg.com/release-it@20/schema/release-it.json",
  "git": {
    "commitMessage": "chore: release v${version}"
  },
  "github": {
    "release": true
  }
}
```

→ See [Configuration][24] for more details.

## Interactive vs. CI mode

By default, release-it is **interactive** and allows you to confirm each task before execution:

<img src="./docs/assets/release-it-interactive.gif?raw=true" height="290" />

By using the `--ci` option, the process is fully automated without prompts. The configured tasks will be executed as
demonstrated in the first animation above. In a Continuous Integration (CI) environment, this non-interactive mode is
activated automatically.

Use `--only-version` to use a prompt only to determine the version, and automate the rest.

## Latest version

How does release-it determine the latest version?

1. For projects with a `package.json`, its `version` will be used (see [npm][25] to skip this).
2. Otherwise, release-it uses the latest Git tag to determine which version should be released.
3. As a last resort, `0.0.0` will be used as the latest version.

Alternatively, a plugin can be used to override this (e.g. to manage a `VERSION` or `composer.json` file):

- [@release-it/bumper][26] to read from or bump the version in any file
- [@release-it/conventional-changelog][27] to get a recommended bump based on commit messages
- [release-it-calver-plugin][28] to use CalVer (Calendar Versioning)

Add the `--release-version` flag to print the **next** version without releasing anything.

## Git

Git projects are supported well by release-it, automating the tasks to stage, commit, tag and push releases to any Git
remote.

→ See [Git][29] for more details.

## npmjs.com Releases

As of July 2025, GitHub and GitLab CI workflows can now use npm's [Trusted Publishing][30] OpenID Connect (OIDC)
integration for secure, token-free publishing from CI/CD. This eliminates long-lived tokens and automatically generates
provenance attestations. See [docs/npm.md][31] for details.

## GitHub Releases

GitHub projects can have releases attached to Git tags, containing release notes and assets. There are two ways to add
[GitHub releases][32] in your release-it flow:

1. Automated (requires a `GITHUB_TOKEN`)
2. Manual (using the GitHub web interface with pre-populated fields)

→ See [GitHub Releases][33] for more details.

## GitLab Releases

GitLab projects can have releases attached to Git tags, containing release notes and assets. To automate [GitLab
releases][34]:

- Configure `gitlab.release: true`
- Obtain a [personal access token][35] (release-it needs the `api` and `self_rotate` scopes).
- Make sure the token is [available as an environment variable][36].

→ See [GitLab Releases][37] for more details.

## Changelog

By default, release-it generates a changelog, to show and help select a version for the new release. Additionally, this
changelog serves as the release notes for the GitHub or GitLab release.

The [default command][23] is based on `git log ...`. This setting (`git.changelog`) can be overridden. To further
customize the release notes for the GitHub or GitLab release, there's `github.releaseNotes` or `gitlab.releaseNotes`.
Make sure any of these commands output the changelog to `stdout`. Note that release-it by default is agnostic to commit
message conventions. Plugins are available for:

- GitHub and GitLab Releases
- auto-changelog
- Conventional Changelog
- Keep A Changelog
- git-cliff

To print the changelog without releasing anything, add the `--changelog` flag.

→ See [Changelog][38] for more details.

## Publish to npm

With a `package.json` in the current directory, release-it will let `npm` bump the version in `package.json` (and
`package-lock.json` if present), and publish to the npm registry.

→ See [Publish to npm][25] for more details.

## Manage pre-releases

With release-it, it's easy to create pre-releases: a version of your software that you want to make available, while
it's not in the stable semver range yet. Often "alpha", "beta", and "rc" (release candidate) are used as identifiers for
pre-releases. An example pre-release version is `2.0.0-beta.0`.

→ See [Manage pre-releases][39] for more details.

## Update or re-run existing releases

Use `--no-increment` to not increment the last version, but update the last existing tag/version.

This may be helpful in cases where the version was already incremented. Here are a few example scenarios:

- To update or publish a (draft) GitHub Release for an existing Git tag.
- Publishing to npm succeeded, but pushing the Git tag to the remote failed. Then use
  `release-it --no-increment --no-npm` to skip the `npm publish` and try pushing the same Git tag again.

## Hooks

Use script hooks to run shell commands at any moment during the release process (such as `before:init` or
`after:release`).

The format is `[prefix]:[hook]` or `[prefix]:[plugin]:[hook]`:

| part   | value                                       |
| ------ | ------------------------------------------- |
| prefix | `before` or `after`                         |
| plugin | `version`, `git`, `npm`, `github`, `gitlab` |
| hook   | `init`, `bump`, `release`                   |

Use the optional `:plugin` part in the middle to hook into a life cycle method exactly before or after any plugin.

The core plugins include `version`, `git`, `npm`, `github`, `gitlab`.

Note that hooks like `after:git:release` will not run when either the `git push` failed, or when it is configured not to
be executed (e.g. `git.push: false`). See [execution order][40] for more details on execution order of plugin lifecycle
methods.

All commands can use configuration variables (like template strings). An array of commands can also be provided, they
will run one after another. Some example release-it configuration:

```json
{
  "hooks": {
    "before:init": ["npm run lint", "npm test"],
    "after:my-plugin:bump": "./bin/my-script.sh",
    "after:bump": "npm run build",
    "after:git:release": "echo After git push, before github release",
    "after:release": "echo Successfully released ${name} v${version} to ${repo.repository}."
  }
}
```

The variables can be found in the [default configuration][23]. Additionally, the following variables are exposed:

```text
version
latestVersion
changelog
name
repo.remote, repo.protocol, repo.host, repo.owner, repo.repository, repo.project
branchName
releaseUrl
```

All variables are available in all hooks. The only exception is that the additional variables listed above are not yet
available in the `init` hook.

Use `--verbose` to log the output of the commands.

For the sake of verbosity, the full list of hooks is actually: `init`, `beforeBump`, `bump`, `beforeRelease`, `release`
or `afterRelease`. However, hooks like `before:beforeRelease` look weird and are usually not useful in practice.

Note that arguments need to be quoted properly when used from the command line:

```bash
release-it --'hooks.after:release="echo Successfully released ${name} v${version} to ${repo.repository}."'
```

Using @inquirer/prompts inside custom hook scripts might cause issues (since release-it also uses this itself).

## Dry Runs

Use `--dry-run` to show the interactivity and the commands it _would_ execute.

→ See [Dry Runs][41] for more details.

## Troubleshooting & debugging

- With `release-it --verbose` (or `-V`), release-it prints the output of every user-defined [hook][2].
- With `release-it -VV`, release-it also prints the output of every internal command.
- Use `NODE_DEBUG=release-it:* release-it [...]` to print configuration and more error details.

Use `verbose: 2` in a configuration file to have the equivalent of `-VV` on the command line.

## Plugins

Since v11, release-it can be extended in many, many ways. Here are some plugins:

| Plugin                                    | Description                                                                                 |
| ----------------------------------------- | ------------------------------------------------------------------------------------------- |
| [@release-it/bumper][26]                  | Read & write the version from/to any file                                                   |
| [@release-it/conventional-changelog][27]  | Provides recommended bump, conventional-changelog, and updates `CHANGELOG.md`               |
| [@release-it/keep-a-changelog][42]        | Maintain CHANGELOG.md using the Keep a Changelog standards                                  |
| [@release-it-plugins/lerna-changelog][43] | Integrates lerna-changelog into the release-it pipeline                                     |
| [@jcamp-code/release-it-changelogen][44]  | Use [@unjs/changelogen][45] for versioning and changelog                                    |
| [@release-it-plugins/workspaces][46]      | Releases each of your projects configured workspaces                                        |
| [release-it-calver-plugin][28]            | Enables Calendar Versioning (calver) with release-it                                        |
| [@grupoboticario/news-fragments][47]      | An easy way to generate your changelog file                                                 |
| [@j-ulrich/release-it-regex-bumper][48]   | Regular expression based version read/write plugin for release-it                           |
| [@jcamp-code/release-it-dotnet][49]       | Use .csproj or .props file for versioning, automate NuGet publishing                        |
| [release-it-pnpm][16]                     | Add basic support for pnpm workspaces, integrates with [bumpp][50] and [changelogithub][51] |
| [changesets-release-it-plugin][52]        | Combine [Changesets][53] changelog management with release-it                               |
| [release-it-gitea][54]                    | Gitea plugin to create Gitea releases and upload attachments                                |
| [release-it-beautiful-changelog][55]      | Generate beautiful changelogs using conventional commits by [@unjs/changelogen][45]         |

Internally, release-it uses its own plugin architecture (for Git, GitHub, GitLab, npm).

→ See all [release-it plugins on npm][56].

→ See [plugins][57] for documentation to write plugins.

## Use release-it programmatically

While mostly used as a CLI tool, release-it can be used as a dependency to integrate in your own scripts. See [use
release-it programmatically][58] for example code.

## Projects using release-it

- [AdonisJs][59]
- [Axios][60]
- [Chakra UI][61]
- [Halo][62]
- [hosts][63]
- [js-cookie][64]
- [jQuery][65]
- [Madge][66]
- [Metalsmith][67]
- [n8n][68]
- [Node-Redis][69]
- [React Native Paper][70]
- [Readability.js][71]
- [Redux][72]
- [Saleor][73]
- [Semantic UI React][74]
- [tabler-icons][75]
- Swagger ([swagger-ui][76] + [swagger-editor][77])
- [Repositories that depend on release-it][78]
- GitHub search for [path:\*\*/.release-it.json][79]

## Node.js version support

The latest major version is v20, supporting Node.js 20 and up:

| release-it | Node.js  |
| :--------: | :------- |
|    v20     | v20.19.0 |
|    v19     | v20.12.0 |
|    v18     | v20      |
|    v17     | v18      |
|    v16     | v16      |
|    v15     | v14      |

Also see [CHANGELOG.md][80] for dates and details.

## Links

- See [CHANGELOG.md][80] for major/breaking updates, and [releases][81] for a detailed version history.
- To **contribute**, please read [CONTRIBUTING.md][82] first.
- Please [open an issue][83] if anything is missing or unclear in this documentation.

## License

[MIT][84]

Are you using release-it at work? Please consider [sponsoring me][14]!

[1]: #git
[2]: #hooks
[3]: #github-releases
[4]: #gitlab-releases
[5]: #changelog
[6]: #publish-to-npm
[7]: #manage-pre-releases
[8]: #plugins
[9]: ./docs/ci.md
[10]: https://github.com/release-it/release-it/actions
[11]: https://github.com/release-it/release-it/workflows/Cross-OS%20Tests/badge.svg
[12]: https://www.npmjs.com/package/release-it
[13]: https://badge.fury.io/js/release-it.svg
[14]: https://github.com/sponsors/webpro
[15]: ./docs/npm.md#yarn
[16]: https://github.com/hyoban/release-it-pnpm
[17]: ./docs/recipes/monorepo.md
[18]: https://github.com/juancarlosjr97/release-it-containerized
[19]: https://github.com/juancarlosjr97
[20]: https://www.youtube.com/watch?v=7pBcuT7j_A0
[21]: https://medium.com/valtech-ch/monorepo-semantic-releases-db114811efa5
[22]: https://github.com/b12k/monorepo-semantic-releases
[23]: ./config/release-it.json
[24]: ./docs/configuration.md
[25]: ./docs/npm.md
[26]: https://github.com/release-it/bumper
[27]: https://github.com/release-it/conventional-changelog
[28]: https://github.com/casmith/release-it-calver-plugin
[29]: ./docs/git.md
[30]: https://docs.npmjs.com/trusted-publishers
[31]: ./docs/npm.md#trusted-publishing-oidc
[32]: https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases
[33]: ./docs/github-releases.md
[34]: https://docs.gitlab.com/api/releases/
[35]: https://gitlab.com/profile/personal_access_tokens
[36]: ./docs/environment-variables.md
[37]: ./docs/gitlab-releases.md
[38]: ./docs/changelog.md
[39]: ./docs/pre-releases.md
[40]: ./docs/plugins.md#execution-order
[41]: ./docs/dry-runs.md
[42]: https://github.com/release-it/keep-a-changelog
[43]: https://github.com/release-it-plugins/lerna-changelog
[44]: https://github.com/jcamp-code/release-it-changelogen
[45]: https://github.com/unjs/changelogen
[46]: https://github.com/release-it-plugins/workspaces
[47]: https://github.com/grupoboticario/news-fragments
[48]: https://github.com/j-ulrich/release-it-regex-bumper
[49]: https://github.com/jcamp-code/release-it-dotnet
[50]: https://github.com/antfu/bumpp
[51]: https://github.com/antfu/changelogithub
[52]: https://www.npmjs.com/package/changesets-release-it-plugin
[53]: https://github.com/changesets/changesets
[54]: https://github.com/lib-pack/release-it-gitea
[55]: https://github.com/mohammadGh/release-it-beautiful-changelog
[56]: https://www.npmjs.com/search?q=keywords:release-it-plugin
[57]: ./docs/plugins.md
[58]: ./docs/recipes/programmatic.md
[59]: https://github.com/adonisjs/core
[60]: https://github.com/axios/axios
[61]: https://github.com/chakra-ui/chakra-ui
[62]: https://github.com/halo-dev/halo
[63]: https://github.com/StevenBlack/hosts
[64]: https://github.com/js-cookie/js-cookie
[65]: https://github.com/jquery/jquery
[66]: https://github.com/pahen/madge
[67]: https://github.com/metalsmith/metalsmith
[68]: https://github.com/n8n-io/n8n
[69]: https://github.com/redis/node-redis
[70]: https://github.com/callstack/react-native-paper
[71]: https://github.com/mozilla/readability
[72]: https://github.com/reduxjs/redux
[73]: https://github.com/saleor/saleor
[74]: https://github.com/Semantic-Org/Semantic-UI-React
[75]: https://github.com/tabler/tabler-icons
[76]: https://github.com/swagger-api/swagger-ui
[77]: https://github.com/swagger-api/swagger-editor
[78]: https://github.com/release-it/release-it/network/dependents
[79]: https://github.com/search?q=path%3A**%2F.release-it.json&type=code
[80]: ./CHANGELOG.md
[81]: https://github.com/release-it/release-it/releases
[82]: ./.github/CONTRIBUTING.md
[83]: https://github.com/release-it/release-it/issues/new
[84]: ./LICENSE
```

## File: `eslint.config.mjs`
```
import _import from 'eslint-plugin-import-x';
import globals from 'globals';
import js from '@eslint/js';

export default [
  js.configs.recommended,
  {
    plugins: {
      import: _import
    },
    languageOptions: {
      globals: {
        ...globals.node,
        ...globals.es6
      },
      ecmaVersion: 2020,
      sourceType: 'module'
    },
    rules: {
      'no-unused-vars': ['error', { caughtErrors: 'none' }],
      'import/no-unresolved': [2, { ignore: ['@octokit/rest', '@octokit/request-error', 'c12'] }],
      'import/order': [2, { 'newlines-between': 'never' }]
    }
  }
];
```

## File: `knip.json`
```json
{
  "project": ["bin/*.js!", "lib/**/*.js!"]
}
```

## File: `package.json`
```json
{
  "name": "release-it",
  "version": "20.0.0-1",
  "description": "Generic CLI tool to automate versioning and package publishing-related tasks.",
  "keywords": [
    "build",
    "changelog",
    "commit",
    "distribution",
    "git",
    "github",
    "gitlab",
    "interactive",
    "ci",
    "npm",
    "publish",
    "push",
    "release",
    "release-it",
    "repository",
    "script",
    "shell",
    "tag",
    "tool",
    "version",
    "semver",
    "plugin"
  ],
  "repository": {
    "type": "git",
    "url": "https://github.com/release-it/release-it.git"
  },
  "homepage": "https://github.com/release-it/release-it#readme",
  "bugs": "https://github.com/release-it/release-it/issues",
  "funding": [
    {
      "type": "github",
      "url": "https://github.com/sponsors/webpro"
    },
    {
      "type": "opencollective",
      "url": "https://opencollective.com/webpro"
    }
  ],
  "bin": {
    "release-it": "bin/release-it.js"
  },
  "type": "module",
  "exports": {
    ".": {
      "types": "./types/index.d.ts",
      "import": "./lib/index.js",
      "require": "./lib/index.js"
    },
    "./package.json": "./package.json",
    "./test/util/index.js": "./test/util/index.js"
  },
  "files": [
    "bin",
    "config",
    "lib",
    "test",
    "schema",
    "types"
  ],
  "types": "./types/index.d.ts",
  "scripts": {
    "knip": "knip",
    "lint": "eslint lib test",
    "format": "prettier --write eslint.config.mjs \"{lib,test}/**/*.js\"",
    "docs": "remark README.md 'docs/**/*.md' '.github/*.md' -o",
    "test": "node --env-file=.env.test --test && installed-check",
    "release": "./bin/release-it.js"
  },
  "author": {
    "email": "lars@webpro.nl",
    "name": "Lars Kappert"
  },
  "license": "MIT",
  "dependencies": {
    "@inquirer/prompts": "8.3.2",
    "@nodeutils/defaults-deep": "1.1.0",
    "@octokit/rest": "22.0.1",
    "@phun-ky/typeof": "2.0.3",
    "async-retry": "1.3.3",
    "c12": "3.3.3",
    "ci-info": "^4.4.0",
    "eta": "4.5.1",
    "git-url-parse": "16.1.0",
    "issue-parser": "7.0.1",
    "lodash.merge": "4.6.2",
    "mime-types": "3.0.2",
    "new-github-release-url": "2.0.0",
    "open": "11.0.0",
    "ora": "9.3.0",
    "os-name": "7.0.0",
    "proxy-agent": "7.0.0",
    "semver": "7.7.4",
    "tinyglobby": "0.2.15",
    "undici": "7.24.5",
    "url-join": "5.0.0",
    "wildcard-match": "5.1.4",
    "yargs-parser": "22.0.0"
  },
  "devDependencies": {
    "@eslint/js": "10.0.1",
    "@octokit/request-error": "7.1.0",
    "@types/node": "24.10.9",
    "eslint": "10.1.0",
    "eslint-plugin-import-x": "4.16.2",
    "globals": "17.4.0",
    "installed-check": "10.0.1",
    "knip": "6.0.5",
    "mentoss": "0.13.0",
    "mock-stdio": "1.0.3",
    "prettier": "3.8.1",
    "remark-cli": "12.0.1",
    "remark-preset-webpro": "2.1.1",
    "tar": "7.5.13",
    "typescript": "6.0.2"
  },
  "overrides": {
    "pac-resolver": "7.0.1",
    "socks": "2.8.3",
    "glob": "13.0.0"
  },
  "engines": {
    "node": "^20.19.0 || ^22.13.0 || >=24.0.0"
  },
  "remarkConfig": {
    "plugins": [
      "preset-webpro"
    ]
  }
}
```

## File: `config/release-it.json`
```json
{
  "hooks": {},
  "git": {
    "changelog": "git log --pretty=format:\"* %s (%h)\" ${from}...${to}",
    "requireCleanWorkingDir": true,
    "requireBranch": false,
    "requireUpstream": true,
    "requireCommits": false,
    "requireCommitsFail": true,
    "commitsPath": "",
    "addUntrackedFiles": false,
    "commit": true,
    "commitMessage": "Release ${version}",
    "commitArgs": [],
    "tag": true,
    "tagExclude": null,
    "tagName": null,
    "tagMatch": null,
    "getLatestTagFromAllRefs": false,
    "tagAnnotation": "Release ${version}",
    "tagArgs": [],
    "push": true,
    "pushArgs": ["--follow-tags"],
    "pushRepo": ""
  },
  "npm": {
    "publish": true,
    "publishPath": ".",
    "publishArgs": [],
    "publishPackageManager": "npm",
    "tag": null,
    "otp": null,
    "ignoreVersion": false,
    "allowSameVersion": false,
    "versionArgs": [],
    "skipChecks": false,
    "timeout": 10
  },
  "github": {
    "release": false,
    "releaseName": "Release ${version}",
    "releaseNotes": null,
    "autoGenerate": false,
    "preRelease": false,
    "draft": false,
    "tokenRef": "GITHUB_TOKEN",
    "assets": null,
    "host": null,
    "timeout": 0,
    "proxy": null,
    "skipChecks": false,
    "web": false,
    "comments": {
      "submit": false,
      "issue": ":rocket: _This issue has been resolved in v${version}. See [${releaseName}](${releaseUrl}) for release notes._",
      "pr": ":rocket: _This pull request is included in v${version}. See [${releaseName}](${releaseUrl}) for release notes._"
    }
  },
  "gitlab": {
    "release": false,
    "releaseName": "Release ${version}",
    "releaseNotes": null,
    "milestones": [],
    "tokenRef": "GITLAB_TOKEN",
    "tokenHeader": "Private-Token",
    "certificateAuthorityFile": null,
    "secure": false,
    "assets": null,
    "useIdsForUrls": false,
    "useGenericPackageRepositoryForAssets": false,
    "genericPackageRepositoryName": "release-it",
    "origin": null,
    "skipChecks": false
  }
}
```

## File: `docs/changelog.md`
```markdown
# Changelog

By default, release-it generates a changelog, to show and help select a version for the new release. It contains all
commits since the latest tag.

The [default command][1] is based on `git log ...`. This setting (`git.changelog`) can be overridden. Make sure any of
these commands output the changelog to `stdout`.

- [GitHub and GitLab Releases][2]
- [auto-changelog][3]
- [Conventional Changelog][4]
- [Keep A Changelog][5]
- [git-cliff][6]

Some projects keep their changelog in e.g. `CHANGELOG.md` or `history.md`. To auto-update this file and include this in
the release commit, the recommended configuration is to do this in the `after:bump` hook (see example below).

## GitHub and GitLab Releases

The output of `git.changelog` also serves as the release notes for the [GitHub][7] or [GitLab release][8]. To customize
the release notes for the GitHub or GitLab release, use `github.releaseNotes` or `gitlab.releaseNotes`. Make sure any of
these commands output the changelog to `stdout`.

## Auto-changelog

For a more rich changelog (e.g. with headers, sections), a (Handlebars) template can be used to generate the changelog.
For this, [auto-changelog][9] is a great companion to release-it:

```json
{
  "git": {
    "changelog": "npx auto-changelog --stdout --commit-limit false -u --template https://raw.githubusercontent.com/release-it/release-it/main/templates/changelog-compact.hbs"
  },
  "hooks": {
    "after:bump": "npx auto-changelog -p"
  }
}
```

With this `git.changelog`, the changelog preview is based on the `changelog-compact.hbs` template file.

Additionally, `hooks.after:bump` will update the `CHANGELOG.md` with each release to get included with the release
commit. This can be omitted if the project does not keep a `CHANGELOG.md` or similar.

See the [auto-changelog recipe][10] for an example setup and template.

## Conventional Changelog

If your project follows conventions, such as the [Angular commit guidelines][11], the
[@release-it/conventional-changelog][12] plugin is useful.

```bash
npm install @release-it/conventional-changelog --save-dev
```

Use this plugin to get the recommended bump based on the commit messages.

Additionally, it can generate a conventional changelog, and optionally update the `CHANGELOG.md` file in the process.

```json
{
  "plugins": {
    "@release-it/conventional-changelog": {
      "preset": "angular",
      "infile": "CHANGELOG.md"
    }
  }
}
```

## Keep A Changelog

If your project follows the [Keep a Changelog][13] conventions, the [@release-it/keep-a-changelog][14] plugin is useful.
It updates the `CHANGELOG.md` file according to the convention of using human-readable items and an "Unreleased"
section.

The GitHub releases section could then be used for either a copy of this changelog, or for a log of commits
(`github.releaseNotes: "git log ..."`).

```bash
npm install @release-it/keep-a-changelog --save-dev
```

This plugin updates `CHANGELOG.md` file according to

```json
{
  "plugins": {
    "@release-it/keep-a-changelog": {
      "filename": "CHANGELOG.md"
    }
  }
}
```

## Git-cliff

Git-cliff is a customizable changelog generator that follows Conventional Commit specifications. Similar to
auto-changelog, it can be used as a companion to release-it.

See the [git-cliff recipe][15] for an example setup.

[1]: ../config/release-it.json
[2]: #github-and-gitlab-releases
[3]: #auto-changelog
[4]: #conventional-changelog
[5]: #keep-a-changelog
[6]: https://github.com/orhun/git-cliff
[7]: ./github-releases.md
[8]: ./gitlab-releases.md
[9]: https://github.com/CookPete/auto-changelog
[10]: ./recipes/auto-changelog.md
[11]: https://github.com/angular/angular.js/blob/master/DEVELOPERS.md#commits
[12]: https://github.com/release-it/conventional-changelog
[13]: https://keepachangelog.com
[14]: https://github.com/release-it/keep-a-changelog
[15]: ./recipes/git-cliff.md
```

## File: `docs/ci.md`
```markdown
# Continuous Integration environments

As release-it is increasingly used from CI/CD environments such as Travis, Circle CI or GitHub Actions, this page
outlines some popular ways to configure this. Do you have additional successful integrations, or experiencing issues
with the existing ones below, feel free to [open a ticket][1].

## Contents

- [Git][2]
- [GitHub Actions][3]
- [npm][4]
- [GitHub & GitLab Releases][5]
- [GitLab CI][6]

## Git

In order to push the release commit and tag back to the remote, the CI/CD environment should be authenticated with the
original host (e.g. GitHub). Also see [Git][7].

### SSH (recommended)

When using an `SSH` url (such as `git@github.com:user/repo.git`), add the public key to the CI/CD environment.

### HTTPS

When using an `HTTPS` url (such as `https://github.com/user/project.git`), things are slightly more complicated. For
GitHub, add the `GITHUB_TOKEN` token to the CI/CD environment. Then make sure to add this token as a password in the
origin url before running release-it. An example is this `.travis.yml` section:

```yaml
script:
  - git remote rm origin
  - git remote add origin https://[user]:${GITHUB_TOKEN}@github.com/[user]/[project].git
  - git symbolic-ref HEAD refs/heads/main
```

Replace `[user]` and `[project]` with the actual values.

## GitHub Actions

To run release-it from a GitHub Action, here's an example job (fragment) to configure a Git user (to push the release
commit), and expose `NPM_TOKEN` for publishing to the npm registry and `GITHUB_TOKEN` for the GitHub Release:

```yaml
jobs:
  release:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
        with:
          fetch-depth: 0
      - name: git config
        run: |
          git config user.name "${GITHUB_ACTOR}"
          git config user.email "${GITHUB_ACTOR}@users.noreply.github.com"
      - run: npm install
      - run: npm run release
        env:
          NPM_TOKEN: ${{ secrets.NPM_TOKEN }}
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

The `fetch-depth: 0` option is only necessary when the Git history is required e.g. if using a plugin such as
[@release-it/conventional-changelog][8].

If you enjoy watching a video, [David from Kodaps][9] created a great walk-through including setting up npm and GitHub
tokens: [How to use GitHub Actions & Release-It to Easily Release Your Code][10]

## npm

To publish a package to the (or any) npm registry from within a CI or CD environment such as Travis or Circle, make the
`NPM_TOKEN` available in the `.npmrc` file. This file should look like this before release-it attempts to publish the
package:

```text
//registry.npmjs.org/:_authToken=$NPM_TOKEN
```

One way to achieve this is to set the `NPM_TOKEN` in the CI environment, and from a script do:

```bash
npm config set //registry.npmjs.org/:_authToken $NPM_TOKEN
```

This will create/update the `.npmrc` file and add the token there. Ideally you should either `.gitignore` this file,
otherwise you might end up committing it to your repo if you are using release-it's `git` options.

Since release-it executes `npm whoami` as a [prerequisite check][11], which does not seem to respect the `.npmrc` file,
the `--npm.skipChecks` argument can be used.

- [Creating and viewing authentication tokens][12]
- [Using (private) packages in a CI/CD workflow][13]

### Travis

Here's an example fragment of what to add to `.travis.yml`:

```yaml
deploy:
  script:
    - echo "//registry.npmjs.org/:_authToken=$NPM_TOKEN" > .npmrc
    - npm run release
```

### Circle

In short, here's the relevant fragment from `.circleci/config.yml`:

```yaml
jobs:
  deploy:
    steps:
      - attach_workspace:
          at: ~/repo
      - run:
          name: Authenticate with registry
          command: npm config set //registry.npmjs.org/:_authToken $NPM_TOKEN
```

During the release process, your project's `package.json` will be updated to bump the version. You will need to setup
CircleCI with a non read-only SSH key pair from your Github account if you want it to be able to push that change back
to the repo.

See [Publishing npm Packages Using CircleCI][14] for more details.

## GitHub & GitLab Releases

Make sure the `GITHUB_TOKEN` or `GITLAB_TOKEN` environment variable is set in the CI/CD environment to publish (or
draft) [GitHub][15] or [GitLab releases][16]. This works the same as on your local machine.

## GitLab CI

### SSH (recommended)

When using release-it with GitLab CI and SSH, make sure the following requirements are met:

- `git` and `ssh` as packages are installed in the job
- `npm install` is run beforehand
- Environment variables contain `GITLAB_TOKEN`, `SSH_PRIVATE_KEY`, `CI_EMAIL` and `CI_USER`
- A user with permissions to write to protected branches or deploy key (env var) is added to the repo

### Alpine

The following example shows a pipeline that first installs Git and OpenSSH to Alpine, adds the SSH private key to the
SSH agent, configures SSH, and eventually executes release-it:

```yaml
before_script:
  - apk add --no-cache git openssh
  - eval `ssh-agent -s`
  - echo "${SSH_PRIVATE_KEY}" | tr -d '\r' | ssh-add - > /dev/null # add ssh key
  - mkdir -p ~/.ssh
  - chmod 700 ~/.ssh
  - '[[ -f /.dockerenv ]] && echo -e "Host *\n\tStrictHostKeyChecking no\n\n" > ~/.ssh/config'
  - git checkout $CI_COMMIT_REF_NAME
  - git remote set-url origin "git@gitlab.com:$CI_PROJECT_PATH.git"
  - git config --global user.name "${CI_USERNAME}"
  - git config --global user.email "${CI_EMAIL}"
  - npm install
script:
  - npx release-it --ci
```

Note: the `git remote set-url` could also be set with the `git.pushRepo` option in the release-it configuration.

### Error: tag already exists

Some people have reported an issue when using GitLab CI (in [#573][17]):

> ERROR fatal: tag vX.X.X already exists

Here is an example script sequence for GitLab to mitigate the issue:

```bash
- git pull origin $CI_COMMIT_REF_NAME
- npm run release
```

Specifically, make sure to `fetch` with the `--prune-tags` argument before release-it tries to create the Git tag:

```json
{
  "hooks": {
    "before:init": "git fetch --prune --prune-tags origin"
  }
}
```

[1]: https://github.com/release-it/release-it/issues
[2]: #git
[3]: #github-actions
[4]: #npm
[5]: #github--gitlab-releases
[6]: #gitlab-ci
[7]: ./git.md
[8]: https://github.com/release-it/conventional-changelog
[9]: https://twitter.com/KodapsAcademy
[10]: https://www.youtube.com/watch?v=7pBcuT7j_A0
[11]: ./npm.md#prerequisite-checks
[12]: https://docs.npmjs.com/creating-and-viewing-authentication-tokens
[13]: https://docs.npmjs.com/using-private-packages-in-a-ci-cd-workflow
[14]: https://circleci.com/blog/publishing-npm-packages-using-circleci-2-0/
[15]: https://github.com/release-it/release-it#github-releases
[16]: https://github.com/release-it/release-it#gitlab-releases
[17]: https://github.com/release-it/release-it/issues/573
```

## File: `docs/configuration.md`
```markdown
# Configuration

Out of the box, release-it has sane defaults. See the [configuration options][1] to configure it.

Put only the options to override in a configuration file. Here is a list of file names where release-it looks for
configuration in the root of the project:

- `.release-it.json`
- `.release-it.ts`
- `.release-it.js` (or `.cjs`; export the configuration object: `module.exports = {}`)
- `.release-it.yaml` (or `.yml`)
- `.release-it.toml`
- `package.json` (in the `release-it` property)

Use `--config path/release-it.json` to use another configuration file location.

An example `.release-it.json`:

```json
{
  "$schema": "https://unpkg.com/release-it@20/schema/release-it.json",
  "git": {
    "commitMessage": "chore: release v${version}"
  },
  "github": {
    "release": true
  }
}
```

The configuration can also be stored in a `release-it` property in `package.json`:

```json
{
  "name": "my-package",
  "devDependencies": {
    "release-it": "*"
  },
  "release-it": {
    "github": {
      "release": true
    }
  }
}
```

Typescript config files are supported, providing typing hints to the config:

```ts
import type { Config } from 'release-it';

export default {
  git: {
    commit: true,
    tag: true,
    push: true
  },
  github: {
    release: true
  },
  npm: {
    publish: true
  }
} satisfies Config;
```

Or, use YAML in `.release-it.yml`:

```yaml
git:
  requireCleanWorkingDir: false
```

TOML is also supported in `.release-it.toml`:

```toml
[hooks]
"before:init" = "npm test"
```

## Configuration options

Release-it has [plenty of options][2]. See the following tables for plugin configuration options:

- [Git][3]
- [npm][4]
- [GitHub][5]
- [GitLab][6]

### Extend Configuration

You can extend a configuration from a remote source using the `extends` option. The following formats are supported:

- `github:owner/repo`: Get the config from the default branch (main) in the repo at Github.
- `github:owner/repo#tag`: Get the config from the specified tag in the repo at Github.
- `github:owner/repo:subdir#tag`: Get the config from the specified tag in the repo sub dir at Github.

And support other schema, either `gitlab:`, `bitbucket:`, or `https:`.

For example, to extend a configuration from a GitHub repository:

```json
{
  "$schema": "https://unpkg.com/release-it@20/schema/release-it.json",
  "extends": "github:release-it/release-it-configuration"
}
```

Get more information at [c12 documents][7].

## Setting options via CLI

Any option can also be set on the command-line, and will have highest priority. Example:

```bash
release-it minor --git.requireBranch=main --github.release
```

Boolean arguments can be negated by using the `no-` prefix:

```bash
release-it --no-npm.publish
```

Also plugin options can be set from the command line:

```bash
release-it --no-plugins.@release-it/keep-a-changelog.strictLatest
```

[1]: #configuration-options
[2]: ../config/release-it.json
[3]: ./git.md#configuration-options
[4]: ./npm.md#configuration-options
[5]: ./github-releases.md#configuration-options
[6]: ./gitlab-releases.md#configuration-options
[7]: https://github.com/unjs/c12?tab=readme-ov-file#extending-configuration
```

## File: `docs/dry-runs.md`
```markdown
# Dry Runs

To show the interactivity and the commands it _would_ execute:

```bash
release-it --dry-run
```

Note that read-only commands are still executed (`$ ...`), while potentially writing/mutating commands are not
(`! ...`):

```bash
$ git rev-parse --git-dir
.git
! git add package.json
! git commit --message="Release 0.8.3"
```

To print the next version without releasing anything, use the `--release-version` flag.

To print the changelog without releasing anything, use the `--changelog` flag.
```

## File: `docs/environment-variables.md`
```markdown
# Environment Variables

For GitHub or GitLab releases, make sure the token is available as an environment variable. Example:

```bash
export GITHUB_TOKEN="f941e0..."
```

In macOS or Linux, this can be added to e.g. `~/.profile`, so it's available everytime the shell is used.

## dotenv

Another solution, that works in every environment (Windows, macOS, Linux), is to use an `.env` file and a package like
[dotenv-cli][1]:

In the `.env` file:

```bash
GITHUB_TOKEN="f941e0..."
```

Install the `dotenv-cli` package as a `devDependency`:

```bash
npm install -D dotenv-cli
```

Prefix the release-it script like so:

```json
{
  "scripts": {
    "release": "dotenv release-it --"
  }
}
```

## Read from input

Not used often, but this script asks for the token everytime a `npm run release` is invoked:

```json
{
  "scripts": {
    "release": "read -p 'GITHUB_TOKEN: ' GITHUB_TOKEN && export GITHUB_TOKEN=$GITHUB_TOKEN && release-it"
  }
}
```

## Notes

- Do not check the token into the Git repository.
- Do not check the `.env` file into the Git repository (add it to `.gitignore`). A convention is to use a `.env.example`
  file with dummy values and add this to the repository.
- Do not put the actual token in the release-it configuration. It will be read from the `GITHUB_TOKEN` environment
  variable. To use something different, use e.g. `github.tokenRef="RELEASE_IT_GITHUB_TOKEN"` (or `gitlab.tokenRef`).

All of the above is the same for `GITLAB_TOKEN`.

[1]: https://github.com/entropitor/dotenv-cli#readme
```

## File: `docs/git.md`
```markdown
# Git

The Git plugin in release-it, by default, does the following:

1. [Prerequisite checks][1]
2. \[Files may be updated by other plugins and/or user commands/hooks]
3. `git add . --update`
4. `git commit -m "[git.commitMessage]"`
5. `git tag --annotate --message="[git.tagAnnotation]" [git.tagName]`
6. `git push [git.pushArgs] [git.pushRepo]`

When not in CI mode, release-it will ask for confirmation before each of the commit, tag, and push steps.

Configure the `[git.*]` options to modify the commands accordingly. See [all options and their default values][2].

The minimum required version of Git is v2.0.0.

## Configuration options

| Option                        | Description                                                              |
| :---------------------------- | :----------------------------------------------------------------------- |
| `git.changelog`               | Changelog generation command                                             |
| `git.requireCleanWorkingDir`  | Require that all file changes are committed                              |
| `git.requireBranch`           | Require that the release is on a particular branch name                  |
| `git.requireUpstream`         | Require that an upstream remote exists.                                  |
| `git.requireCommits`          | Stop the process if there are no commits since the previous release      |
| `git.requireCommitsFail`      | If there are no commits, continue but use exit code `0`                  |
| `git.commitsPath`             | The path to the directory that should be included in the release changes |
| `git.addUntrackedFiles`       | Add untracked files to the release commit                                |
| `git.commit`                  | If `false`, skip the commit release step                                 |
| `git.commitMessage`           | The message to add to the commit step                                    |
| `git.commitArgs`              | Provide extra arguments to `git commit`                                  |
| `git.tag`                     | If `false`, skip the tag release step                                    |
| `git.tagExclude`              | Override the normal behavior to find the latest tag                      |
| `git.tagName`                 | Custom tag name, which may not be the same as the (prefixed) version     |
| `git.tagMatch`                | Override the normal matching behavior to find the latest tag             |
| `git.getLatestTagFromAllRefs` | Consider all tags (directly reachable or not, sorted by version)         |
| `git.tagAnnotation`           | Message string for annotating the Git tag                                |
| `git.tagArgs`                 | Provide extra arguments to `git tag`                                     |
| `git.push`                    | If `false`, skip the push release step                                   |
| `git.pushArgs`                | Provided extra arguments to `git push`                                   |
| `git.pushRepo`                | Remote name or Git URL to push the release to (default `origin`)         |

## Git remotes

SSH keys and Git remotes are assumed to be configured correctly. If a manual `git push` from the command line works,
release-it should be able to do the same.

The following help pages might be useful:

- [Connecting to GitHub with SSH][3]
- [Managing remote repositories][4] (GitHub)
- [Configure SSH and two-step verification][5] (Bitbucket)
- [GitLab and SSH keys][6]

## Remote repository

By default, `release-it` uses branch's tracking information, unless there isn't any, in which case it defaults to
`"origin"` as the remote name to push to. Use `git.pushRepo` to override this with a different remote name, or a
different git url.

## Tag Name

Use `git.tagName` to set a custom tag, not strictly equal to the (prefixed) version. When the latest tag has the `v`
prefix, it will be used again. No need to configure `git.tagName: "v${version}"` in this case.

Examples:

- `--git.tagName=${branchName}-${version}`
- `--git.tagName=${repo.project}-${version}`
- `--git.tagName=${npm.name}@${version}`

## Tag Match

Use `git.tagMatch` to override the normal matching behavior to find the latest tag. For instance, when doing a major
release to find and set the latest major tag, and include all commits in the changelog since this matching tag. Note
that this represents a [glob][7] (not a regex):

Example: `git.tagMatch: "[0-9]*.[0-9]*.[0-9]*"`

This could also be useful when using a plugin to determine the next tag:

Example: `git.tagMatch: "[0-9][0-9].[0-1][0-9].[0-9]*"`

## Tag Exclude

Use `git.tagExclude` to override the normal behavior to find the latest tag. For example when doing a major release and
you want to exclude any sort of pre-releases, use `*[-]*`, as this would exclude everything with a hyphen, which is
normally used exclusively in pre-releases.

Example: `git.tagExclude: *[-]*`

Note that `git.tagExclude` has no effect when `git.getLatestTagFromAllRefs: true`. See the next section [use all refs to
determine latest tag][8] for more details.

## Use all refs to determine latest tag

By default, Git determines the latest tag using [`git describe`][9], which finds the most recent tag _that is reachable
from a commit._ If you wish to consider all tags, e.g. to include tags that point to sibling commits on different
branches, then set `git.getLatestTagFromAllRefs: true` (the default is `false`).

![Determine latest tag from all refs][10]

In the above illustration, releasing from `develop` and incrementing the semver `rc` modifier, when
`git.getLatestTagFromAllRefs: false` (the default), the latest tag is `v1.1.0-rc1`, because that is the most recent tag
reachable from the current commit (the red circle on `develop`). The version to release will therefore be `v1.1.0-rc2`.

Setting `git.getLatestTagFromAllRefs: true` considers all tags (sorting them by version), whether directly reachable or
not. In which case, the latest tag is `v1.1.0` from `main`, and the new version to release is `v1.2.0-rc1`.

## Extra arguments

In case extra arguments should be provided to Git, these options are available:

- `git.commitArgs`
- `git.tagArgs`
- `git.pushArgs`

For example, use `"git.commitArgs": ["-S"]` to sign commits (also see [#35][11]).

Note that `["--follow-tags"]` is the default for `pushArgs` (re-add this manually if necessary). Example with multiple
arguments for `git push`:

```bash
release-it minor --git.pushArgs=--follow-tags --git.pushArgs=--force
```

## Skip Git steps

To skip the Git steps entirely (for instance, if you only want to `npm publish`), this shorthand is available:

```bash
release-it --no-git
```

Use e.g. `git.tag: false` or `--no-git.tag` to skip a single step.

## Untracked files

By default, untracked files are not added to the release commit. Use `git.addUntrackedFiles: true` to override this
behavior.

## Prerequisite checks

### Required branch

This is disabled by default, but release-it can exit the process when the current branch is not as configured:

```json
{
  "git": {
    "requireBranch": "main"
  }
}
```

Use an array to allow releases from more branch names. Wildcards are also allowed (e.g. `release/*`).

### Clean working directory

The working directory should be clean (i.e. `git status` should say something like this:

```bash
$ git status
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean
```

Make sure to commit, stash, or revert the changes before running release-it. In case the currently staged changes should
be committed with the release commit, use `--no-git.requireCleanWorkingDir` or configure
`"git.requireCleanWorkingDir": false`.

### Upstream branch

If no upstream branch is known to Git, it does not know where to push the release commit and tag to, and halts.

Use `--no-git.requireUpstream` to add `--set-upstream [remote] [branch]` to the `git push` command, where `[remote]` is
the value of `git.pushRepo` ("origin" by default, if no upstream branch), and `[branch]` is the name of the current
branch. So if the current branch is `next` then the full command that release-it will execute becomes
`git push --follow-tags --set-upstream origin next`.

Configure `pushRepo` with either a remote name or a Git url to push the release to that remote instead of `origin`.

Disabling `git.requireUpstream` is useful when releasing from a different branch (that is not yet tracking cq present on
a remote). Or similar, when releasing a (new) project that did not push to the remote before. Please note that in
general you should not need this, as it is considered a best practice to release from the `main` branch only. Here is an
example use case and how it can be handled using release-it:

- After a major release (v2), a bug is found and a fix released in v2.0.1.
- The fix should be backported to v1, so a branch "v1" is made and the fix is cherry-picked.
- The release of v1.x.x can be done while still in this branch using `release-it --no-git.requireUpstream`.

### No commits

By default, release-it does not check the number of commits upfront to prevent "empty" releases. Configure
`"git.requireCommits": true` to exit the release-it process if there are no commits since the latest tag.

Also see the [Require Commits][12] recipe(s).

## Further customizations

In case you need even more customizations, here is some inspiration:

```json
{
  "git": {
    "commitMessage": "chore(release): cut the v${version} release",
    "push": false
  },
  "hooks": {
    "after:bump": ["npm run build"],
    "after:release": "git push origin HEAD"
  }
}
```

Since the `after:release` hook runs after the Git commands, the `git.push` can be disabled, and replaced by a custom
script.

[1]: #prerequisite-checks
[2]: ../config/release-it.json
[3]: https://docs.github.com/en/authentication/connecting-to-github-with-ssh
[4]: https://docs.github.com/en/get-started/getting-started-with-git/managing-remote-repositories
[5]: https://support.atlassian.com/bitbucket-cloud/docs/configure-ssh-and-two-step-verification/
[6]: https://docs.gitlab.com/user/ssh/
[7]: https://code.visualstudio.com/docs/editor/glob-patterns
[8]: #use-all-refs-to-determine-latest-tag
[9]: https://git-scm.com/docs/git-describe
[10]: assets/git-version-from-all-refs.svg
[11]: https://github.com/release-it/release-it/issues/350
[12]: ./recipes/require-commits.md
```

## File: `docs/github-releases.md`
```markdown
# GitHub Releases

<img align="right" src="./assets/github-release.png?raw=true" width="350" style="border:red;">

The "releases" page on GitHub projects links to a page containing the project's history, or changelog. Releases are
attached to an existing Git tag, so make sure the [Git part][1] is configured correctly.

Unsurprisingly, release-it uses this feature extensively ([release-it's releases page][2]).

See the screenshot on the right for an overview of what release-it automates.

To add [GitHub releases][3] in your release-it flow, there are two options:

1. Automated. This requires a personal access token.
2. Manual. The GitHub web interface will be opened with pre-populated fields.

## Configuration options

| Option                   | Description                                                                     |
| :----------------------- | :------------------------------------------------------------------------------ |
| `github.release`         | Set to `false` to skip the GitHub publish step                                  |
| `github.releaseName`     | Set the release name (default: `Release ${version}`)                            |
| `github.releaseNotes`    | Override the release notes with custom notes                                    |
| `github.autoGenerate`    | Let GitHub generate release notes (overrides other notes!)                      |
| `github.preRelease`      | Set the release to a pre-release status                                         |
| `github.draft`           | Set the release to a draft status                                               |
| `github.tokenRef`        | GitHub token environment variable name (default: `GITHUB_TOKEN`)                |
| `github.assets`          | Glob pattern path to assets to add to the GitHub release                        |
| `github.host`            | Use a different host from what would be derived from the Git URL                |
| `github.timeout`         | Timeout duration to wait for a response from the GitHub API                     |
| `github.proxy`           | If the release is performed behind a proxy, set this to string of the proxy URL |
| `github.skipChecks`      | Skip checks on `GITHUB_TOKEN` environment variable and user permissions         |
| `github.web`             | Explicitly override checking if the `GITHUB_TOKEN` is set                       |
| `github.comments.submit` | Submit a comment to each merged PR and closed issue part of the release         |
| `github.comments.issue`  | The text to add to the associated closed issues                                 |
| `github.comments.pr`     | The text to add to the associated merged pull requests                          |

## Automated

To automate the release (using the GitHub REST API), the following needs to be configured:

- Configure `github.release: true`
- Obtain a [personal access token][4] (release-it only needs "repo" access; no "admin" or other scopes).
- Make sure the token is [available as an environment variable][5].

Do not put the actual token in the release-it configuration. It will be read from the `GITHUB_TOKEN` environment
variable. You can change this variable name by setting the `github.tokenRef` option to something else.

Optionally, release-it can automatically [submit comments][6] to the merged pull requests and closed tickets to notify
people in which release the fix or feature is included.

## Manual

In this mode, release-it will open the default browser pointed at the GitHub web interface with the fields pre-populated
(like the screenshot above). The data can be modified and assets can be uploaded before publishing the release.

- Configure `github.release: true`
- This mode is enabled automatically when the `GITHUB_TOKEN` environment variable is not set.
- Set `github.web: true` explicitly to override this `GITHUB_TOKEN` check.
- Use `github.autoGenerate: true` to let GitHub generate release notes.

In non-interactive CI mode (using `--ci` or in a CI environment), release-it will not open a browser, but instead print
the url to the GitHub web interface (including data to pre-populate the fields).

## Git

A GitHub release requires the corresponding Git tag to be present on the remote (release-it creates and pushes this tag
automatically). Thus, in addition to the `GITHUB_TOKEN`, a public SSH key is required to push the Git tag to the remote
repository. See [Git remotes][7] (and [CI: Git][8]) for more information.

## Prerequisite checks

First, release-it will check whether the `GITHUB_TOKEN` environment variable is set. If not, it will fall back to [open
the web interface][9] to publish a release (and skip the next checks). If the token is set, it will authenticate, and
verify whether the current user is a collaborator and authorized to publish a release.

To skip these checks, use `github.skipChecks`.

## Release name

The default release name is `Release ${version}`. However, many projects are more creative here. It can be set from the
command-line directly: `--github.releaseName="Arcade Silver"`.

## Release notes

By default, the output of `git.changelog` is used for the GitHub release notes. This is the printed `Changelog: ...`
when release-it boots. This can be overridden with the `github.releaseNotes` option to customize the release notes for
the GitHub release. This will be invoked just before the actual GitHub release itself.

The value can either be a string or a function but a function is only supported when configuring release-it using
`.release-it.js` or `.release-it.cjs` file.

When the value is a string, it's executed as a shell script. Make sure it outputs to `stdout`. An example:

```json
{
  "github": {
    "release": true,
    "releaseNotes": "generate-release-notes.sh --from=${latestTag} --to=${tagName}"
  }
}
```

Another example using `--no-merges` to omit merge commits:

```json
{
  "github": {
    "release": true,
    "releaseNotes": "git log --no-merges --pretty=format:\"* %s %h\" ${latestTag}...main"
  }
}
```

### Function

When the value is a function, it's executed with a single `context` parameter that contains the plugin context. The
function can also be `async`. Make sure that it returns a string value. An example:

```js
{
  github: {
    release: true,
    releaseNotes(context) {
      // Remove the first, redundant line with version and date.
      return context.changelog.split('\n').slice(1).join('\n');
    }
  }
}
```

Use `--github.autoGenerate` to have GitHub auto-generate the release notes (does not work with `web: true`).

See [Changelog][10] for more information about generating changelogs/release notes.

### Object

Use an object to switch from the `releaseNotes` as a command string to commits fetched by the GitHub Octokit API and
rendered using the provided template. Example:

```json
{
  "github": {
    "releaseNotes": {
      "commit": "* ${commit.subject} (${sha}){ - thanks @${author.login}!}",
      "excludeMatches": ["webpro"]
    }
  }
}
```

Placeholders have syntax `${place.holder}`. Blocks surrounded by `{` and `}` are rendered only if each placeholder
inside is replaced with a value and that value is not in `excludeMatches`.

Here's an excerpt of an example object that is the context of the `releaseNotes.commit` template:

```json
{
  "sha": "2e8c8ac65fa9e05fc170d08913d7fbac2b2bd876",
  "commit": {
    "author": { "name": "Lars Kappert", "email": "lars@webpro.nl", "date": "2025-01-06T21:15:33Z" },
    "committer": { "name": "Lars Kappert", "email": "lars@webpro.nl", "date": "2025-01-06T21:15:33Z" },
    "message": "Add platform-specific entries to metro plugin",
    "url": "https://api.github.com/repos/webpro-nl/knip/git/commits/2e8c8ac65fa9e05fc170d08913d7fbac2b2bd876",
    "comment_count": 0,
    "verification": { "verified": false, "reason": "unsigned", "signature": null, "payload": null, "verified_at": null }
  },
  "url": "https://api.github.com/repos/webpro-nl/knip/commits/2e8c8ac65fa9e05fc170d08913d7fbac2b2bd876",
  "html_url": "https://github.com/webpro-nl/knip/commit/2e8c8ac65fa9e05fc170d08913d7fbac2b2bd876",
  "comments_url": "https://api.github.com/repos/webpro-nl/knip/commits/2e8c8ac65fa9e05fc170d08913d7fbac2b2bd876/comments",
  "author": { "login": "webpro", "id": 456426, "html_url": "https://github.com/webpro" },
  "committer": { "login": "webpro", "id": 456426, "avatar_url": "https://avatars.githubusercontent.com/u/456426?v=4" },
  "parents": []
}
```

The GitHub plugin adds `commit.subject` which is only the first line of `commit.message` (which is potentially multiple
lines especially for merge commits).

See [REST API: Compare two commits][11] for the full specs of this object.

## Attach binary assets

To upload binary release assets with a GitHub release (such as compiled executables, minified scripts, documentation),
provide one or more glob patterns for the `github.assets` option. After the release, the assets are available to
download from the GitHub release page. Example:

```json
{
  "github": {
    "release": true,
    "assets": ["dist/*.zip"]
  }
}
```

## Pre-release

If the release is a pre-release (according to semver), release-it automatically sets `github.preRelease` to `true`. This
can also be set manually.

## Draft

In case the release should not be made public yet, set `github.draft: true`.

## Host

Use a different host from what would be derived from the Git url (e.g. when using GitHub Enterprise).

By default, the GitHub API host is [https://api.github.com][12]. Setting `github.host` to `"private.example.org"` would
result in release-it using [https://private.example.org/api/v3][13].

## Proxy

In case release are done from behind a proxy, set `github.proxy` using a string to a proxy address like
`"http://proxy:8080"`.

## Update the latest release

The latest GitHub release can be updated, e.g. to update the releases notes, add release assets, or toggle the `draft`
status.

- Use `--no-increment` to skip updating the version.
- Use `--no-git` to skip Git commit, tag, push (when the tag is already there).
- Use `--no-npm` to skip publishing to npm (if there's a `package.json`).
- Use `--github.update` to update the GitHub release.

Use the other options to update the release, such as `--github.assets` to add assets. Note that the `draft` and
`preRelease` options are `false` by default, but can be set explicitly using e.g. `--no-github.draft` or
`--github.draft`.

Example command to add assets and explicitly toggle the draft status to "published":

```bash
release-it --no-increment --no-git --github.release --github.update --github.assets=*.zip --no-github.draft
```

## Project Non-Latest Release

To do a release that isn't the latest release on your GitHub project e.g for support releases, you can set
`github.makeLatest` to `false`.

## Create GitHub Discussion

To auto-create GitHub Discussion for the release on your GitHub project, you can set:

`github.discussionCategoryName` to `[discussion category name]`

## Comments

To submit a comment to each merged pull requests and closed issue that is part of the release, set
`github.comments.submit` to `true`. Here are the default settings:

```json
{
  "github": {
    "comments": {
      "submit": false,
      "issue": ":rocket: _This issue has been resolved in v${version}. See [${releaseName}](${releaseUrl}) for release notes._",
      "pr": ":rocket: _This pull request is included in v${version}. See [${releaseName}](${releaseUrl}) for release notes._"
    }
  }
}
```

Example comment:

\:rocket: _This issue has been resolved in v15.10.0. See [Release 15.10.0][14] for release notes._

This only works with `github.release: true` and not with [manual release via the web interface][9].

Since this is an experimental feature, it's disabled by default for now. Set `github.comments: true` to enable.

[1]: ./git.md
[2]: https://github.com/release-it/release-it/releases
[3]: https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases
[4]: https://github.com/settings/tokens/new?scopes=repo&description=release-it
[5]: ./environment-variables.md
[6]: #comments
[7]: ./git.md#git-remotes
[8]: ./ci.md#git
[9]: #manual
[10]: ./changelog.md
[11]: https://docs.github.com/en/rest/commits/commits?apiVersion=2022-11-28#compare-two-commits
[12]: https://api.github.com
[13]: https://private.example.org/api/v3
[14]: https://github.com/release-it/release-it/releases/tag/15.10.0
```

## File: `docs/gitlab-releases.md`
```markdown
# GitLab Releases

For this feature, at least GitLab v11.7 is required. GitLab 11.7 introduces [Releases][1] to create release entries
(much like GitHub), including release assets. Releases are attached to an existing Git tag, so make sure the [Git
part][2] is configured correctly.

[GitLab releases][1] work just like GitHub releases:

- Configure `gitlab.release: true`.
- Obtain a [personal access token][3] (release-it needs the `api` and `self_rotate` scopes).
- Make sure the token is [available as an environment variable][4].

GitLab Releases do not support pre-releases or drafts.

## Configuration options

| Option                               | Description                                                                 |
| :----------------------------------- | :-------------------------------------------------------------------------- |
| `gitlab.release`                     | Set to `false` to skip the GitLab publish step                              |
| `gitlab.releaseName`                 | Set the release name (default: `Release ${version}`)                        |
| `gitlab.releaseNotes`                | Override the release notes with custom notes                                |
| `gitlab.milestones`                  | Associate one or more milestones with a GitLab release                      |
| `gitlab.tokenRef`                    | GitLab token environment variable name (default: `GITLAB_TOKEN`)            |
| `gitlab.tokenHeader`                 | HTTP header name for the GitLab token (default: `Private-Token`)            |
| `gitlab.certificateAuthorityFile`    | Path of the GitLab CA file for self-hosted installations                    |
| `gitlab.certificateAuthorityFileRef` | GitLab CA file environment variable name (default: `CI_SERVER_TLS_CA_FILE`) |
| `gitlab.secure`                      | Flag to disable server certificate verification (default: `false`)          |
| `gitlab.assets`                      | Glob pattern path to assets to add to the GitLab release                    |
| `gitlab.origin`                      | Base URL to use for the GitLab API (default: `https://${repo.host}`)        |
| `gitlab.skipChecks`                  | Skip checks on `GITLAB_TOKEN` environment variable and milestone(s)         |

## Prerequisite checks

First, release-it will check whether the `GITLAB_TOKEN` environment variable is set. Otherwise it will throw an error
and exit. Then, it will authenticate, and verify whether the current user is a collaborator and authorized to publish a
release.

To skip these checks, use `gitlab.skipChecks`.

## Release notes

By default, the output of `git.changelog` is used for the GitLab release notes. This is the printed `Changelog: ...`
when release-it boots. This can be overridden with the `gitlab.releaseNotes` option to customize the release notes for
the GitLab release. This will be invoked just before the actual GitLab release itself.

The value can either be a string or a function but a function is only supported when configuring release-it using
`.release-it.js` or `.release-it.cjs` file.

When the value is a string, it's executed as a shell script. Make sure it outputs to `stdout`. An example:

```json
{
  "gitlab": {
    "release": true,
    "releaseNotes": "generate-release-notes.sh ${latestVersion} ${version}"
  }
}
```

When the value is a function, it's executed with a single `context` parameter that contains the plugin context. The
function can also be `async`. Make sure that it returns a string value. An example:

```js
{
  gitlab: {
    release: true,
    releaseNotes(context) {
      // Remove the first, redundant line with version and date.
      return context.changelog.split('\n').slice(1).join('\n');
    }
  }
}
```

See [Changelog][5] for more information about generating changelogs/release notes.

## Milestones

To associate one or more milestones with a GitLab release, set the `gitlab.milestones` option to an array of the titles
of the corresponding milestones, for example:

```json
{
  "gitlab": {
    "release": true,
    "milestones": ["${version}"]
  }
}
```

Note that creating a GitLab release will fail if one of the given milestones does not exist. release-it will check this
before doing the release. To skip this check, use `gitlab.skipChecks`.

## Attach binary assets

To upload binary release assets with a GitLab release (such as compiled executables, minified scripts, documentation),
provide one or more glob patterns for the `gitlab.assets` option. After the release, the assets are available to
download from the project's releases page. Example:

```json
{
  "gitlab": {
    "release": true,
    "assets": ["dist/*.dmg"]
  }
}
```

Version 17.2 of Gitlab [started enforcing a new URL format][6] for uploaded assets. If you are using this version (or
later), you should set the `useIdsForUrls` flag to `true`:

```json
{
  "gitlab": {
    "release": true,
    "useIdsForUrls": true,
    "assets": ["dist/*.dmg"]
  }
}
```

### Asset Location

By default release assets are uploaded to the project's Markdown uploads API. If you want to use GitLab's Generic
packages Repository set `useGenericPackageRepositoryForAssets` flag to true. `useIdsForUrls` is ignored from this API.
You can set the package name to be uploaded to using `genericPackageRepositoryName` by default the name is `release-it`.

```json
{
  "gitlab": {
    "release": true,
    "useGenericPackageRepositoryForAssets": true,
    "genericPackageRepositoryName": "release-it",
    "assets": ["dist/*.dmg"]
  }
}
```

## Origin

The `origin` can be set to a string such as `"http://example.org:3000"` to use a different origin from what would be
derived from the Git url (e.g. to use `http` over the default `https://${repo.host}`).

## Private CA Authority

If you're running your own GitLab instance with an HTTPS certificate issued by a private certificate Authority, you can
specify the root CA certificate with `certificateAuthorityFile` or `certificateAuthorityFileRef`, for example:

```json
{
  "gitlab": {
    "release": true,
    "tokenHeader": "PRIVATE-TOKEN",
    "certificateAuthorityFile": "./my-root-ca.crt"
  }
}
```

If not explicitly set, the environment variable `CI_SERVER_TLS_CA_FILE` is used by default.

Alternatively, if you want to disable the server certificate verification against the list of supplied CAs, you can set
the `secure` flag to false:

```json
{
  "gitlab": {
    "release": true,
    "tokenHeader": "PRIVATE-TOKEN",
    "secure": false
  }
}
```

The `secure` option is passed down to the `fetch` agent as the `connect.rejectUnauthorized` option.

## Update the latest release

The latest GitLab release can be updated, e.g. to update the releases notes or add release assets.

- Use `--no-increment` to skip updating the version.
- Use `--no-git` to skip Git actions.
- Use `--no-npm` to skip publishing to npm if there's a `package.json`.

Use the other options to update the release, such as `--gitlab.assets` to add assets.

Example command to add assets to the latest release:

```bash
release-it --no-increment --no-git --gitlab.release --gitlab.assets=*.zip
```

[1]: https://docs.gitlab.com/api/releases/
[2]: ./git.md
[3]: https://docs.gitlab.com/user/profile/personal_access_tokens/
[4]: ./environment-variables.md
[5]: ./changelog.md
[6]: https://gitlab.com/gitlab-org/gitlab/-/merge_requests/156939
```

## File: `docs/npm.md`
```markdown
# Publish to npm

With a `package.json` in the current directory, release-it will let `npm` bump the version in `package.json` (and
`package-lock.json` if present), and publish to the npm registry.

- If only the publish step should be skipped, use `npm.publish: false`.
- If `package.json` should be ignored, its version should not be bumped, and nothing should be published to npm, use
  `--no-npm` or `"npm": false` in the release-it configuration.

## Configuration options

| Option                      | Description                                                                          |
| :-------------------------- | :----------------------------------------------------------------------------------- |
| `npm.publish`               | Set to `false` to skip the npm publish step                                          |
| `npm.publishPath`           | Publish only a specific folder (e.g. `dist`)                                         |
| `npm.publishArgs`           | In case extra arguments should be provided to npm for the publish operation          |
| `npm.publishPackageManager` | Use `pnpm` or `bun` to publish (default: `npm`)                                      |
| `npm.tag`                   | Use e.g. `npm.tag=beta` to tag the package in the npm repository                     |
| `npm.otp`                   | The one-time password (OTP) can be provided from the command line (`npm.otp=123456`) |
| `npm.ignoreVersion`         | When set to `true`, ignore the `version` from `package.json`                         |
| `npm.allowSameVersion`      | Allow new version to be the same value as the current version                        |
| `npm.versionArgs`           | In case extra arguments should be provided to npm for the versioning operation       |
| `npm.skipChecks`            | Skip checks on whether the npm registry is up and the user permissions               |
| `npm.timeout`               | Timeout duration to wait for a response from the npm registry                        |

## Prerequisite checks

To prevent issues later in the process, release-it first checks whether the npm registry is up, the user is
authenticated with npm and is a collaborator for the current package.

Some instances of npm registries, such as Nexus, do not support `npm ping`, `npm whoami` and/or `npm access`. If the
error is a `E400` or `E404`, release-it will give a warning but continue.

To skip these checks, use `npm.skipChecks`.

## Skip publish

To bump the version in `package.json` with the release, but not publish to the registry:

```json
{
  "npm": {
    "publish": false
  }
}
```

In case there is a `package.json`, but no npm-related tasks should be executed, use `"npm": false` (or `--no-npm`).

## Ignore version

To ignore the `version` from `package.json`, (and use the latest Git tag instead):

```json
{
  "npm": {
    "ignoreVersion": true
  }
}
```

Or `--npm.ignoreVersion` from the command line.

## Tags

Use e.g. `--npm.tag=beta` to tag the package in the npm repository. With the `--preRelease=beta` shorthand, the npm
dist-tag will have the same value (unless `--npm.tag` is used to override this). The default tag is "latest".

For a pre-release, the default tag is "next". The tag will be derived from the pre-release version (e.g. version
`2.0.0-alpha.3` will result in tag "alpha"), unless overridden by setting `npm.tag`.

## Public scoped packages

A [scoped package][1] (e.g. `@user/package`) is either public or private. By default, `npm publish` will publish a
scoped package as private. Note that scoped packages require a paid account.

In order to publish a scoped package to the public registry, specify this at the root of `package.json`:

```json
{
  "publishConfig": {
    "access": "public"
  }
}
```

The default value for private packages is `"restricted"`.

## Publish to private registry

The default registry is [https://registry.npmjs.org][2]. The publish to another registry, update or set the
`publishConfig` in `package.json`. For example:

```json
{
  "publishConfig": {
    "registry": "https://npm.pkg.github.com"
  }
}
```

## Config public path of registry

The default public path is `/package`. To customize an alternative path, update or set the `publishConfig`. For example,
if a third-party tool such as `Verdaccio` is used to build a private server to proxy npm registry, then the URL address
of the web user interface is `http://{{host}}-/web/detail/{{packageName}}`:

```json
{
  "publishConfig": {
    "publicPath": "/-/web/detail"
  }
}
```

## Yarn

Using Yarn? It adds or overwrites global environment variable(s), causing authentication issues or not being able to
publish. Set the `publishConfig.registry` value so release-it will use the `--registry` argument with this value for
each `npm` command.

```json
{
  "publishConfig": {
    "registry": "https://registry.npmjs.org"
  }
}
```

## Two-factor authentication

In case two-factor authentication (2FA) is enabled for the package, release-it will ask for the one-time password (OTP).

The OTP can be provided from the command line (`--npm.otp=123456`). However, providing the OTP without a prompt
basically defeats the purpose of 2FA (also, the OTP expires after a short period).

## Publish path

Use `npm.publishPath` to publish only a specific folder. For example, set `npm.publishPath` to `"dist"`. The default
value is the current (root) folder (`"."`).

## Extra arguments

Use `npm.versionArgs` and/or `npm.publishArgs` to pass extra arguments to `npm version` and `npm publish`, respectively.
Example:

```json
{
  "npm": {
    "versionArgs": ["--allow-same-version", "--workspaces-update=false"],
    "publishArgs": ["--include-workspace-root"]
  }
}
```

Use `npm.allowSameVersion` to prevent throwing error when setting the new version to the same value as the current
version. This option may become deprecated, it is recommended to use `versionArgs` for this.

## Monorepos

Monorepos do not require extra configuration, but release-it handles only one package at a time. Also see how [Git steps
can be skipped][3]. This is useful if, for instance, tagging the Git repo should be skipped.

To bump multiple `package.json` files in a monorepo to the same version, use the [@release-it/bumper][4] plugin.

Also see this [monorepo recipe][5].

For Yarn workspaces, see the [release-it-yarn-workspaces][6] plugin.

## Trusted Publishing (OIDC)

npm's [Trusted Publishing][7] uses OpenID Connect (OIDC) for secure, token-free publishing from CI/CD. This eliminates
long-lived tokens and automatically generates provenance attestations.

Note that none of these steps are optional.

### Step 1: configure npmjs.com

1. Log into npmjs.com
2. Navigate to your package's "Settings" tab
3. Click the button under **Select your publisher** and fill out the form.

### Step 2: configure `release-it`

When using Trusted Publishing, you **must** configure release-it to **skip npm authentication checks** (see [#1244][8]):

```json
{
  "npm": {
    "skipChecks": true
  }
}
```

### Step 3: configure your publishing workflow

You'll need to

- add `id-token: write` and
- remove your `NODE_AUTH_TOKEN`
- add a step to upgrade `npm` to at least v11.5.1

```yaml
# GitHub Actions example
jobs:
  release:
    runs-on: ubuntu-latest
    permissions:
      contents: write # For git operations
      id-token: write # < REQUIRED FOR OIDC

    steps:
      - uses: actions/checkout
      - uses: actions/setup-node
        with:
          node-version: 'lts/*'
          registry-url: 'https://registry.npmjs.org'

      # OIDC requires npm v11.5.1 or later
      # Node.js v20 comes with v10.8, so we need to update it:
      - run: npm install -g npm@latest
      - run: npm ci
      - run: npx release-it --ci
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          # Delete your NPM_TOKEN/NODE_AUTH_TOKEN -- you don't need it!
```

## Miscellaneous

- When `npm version` fails, the release is aborted (except when using [`--no-increment`][9]).
- Learn how to [authenticate and publish from a CI/CD environment][10].
- The `"private": true` setting in package.json will be respected, and `release-it` will skip this step.
- Getting an `ENEEDAUTH` error while a manual `npm publish` works? Please see [#95][11].

[1]: https://docs.npmjs.com/about-scopes
[2]: https://registry.npmjs.org
[3]: ./git.md#skip-git-steps
[4]: https://github.com/release-it/bumper
[5]: ./recipes/monorepo.md
[6]: https://github.com/release-it-plugins/workspaces
[7]: https://docs.npmjs.com/trusted-publishers
[8]: https://github.com/release-it/release-it/issues/1244#issuecomment-3217898680
[9]: ../README.md#update-or-re-run-existing-releases
[10]: ./ci.md#npm
[11]: https://github.com/release-it/release-it/issues/95#issuecomment-344919384
```

## File: `docs/plugins.md`
```markdown
# Plugins

release-it is a pluggable task runner. If it can either be written in Node.js, or executed from the shell, it can be
integrated in the release-it process.

## Contents

- [Overview][1]
- [Using a plugin][2]
- [Creating a plugin][3]
- [Available & example plugins][4]

### Overview

Plugins allow additional and custom actions in the release process, such as:

- Publish the package to any registry (this is language-agnostic, e.g. Ruby, Python, ...).
- Implement a different strategy to generate changelogs and/or release notes.
- Trigger web hooks (e.g. post a message to a Slack channel).
- Use a different VCS, such as Mercurial (example: [@release-it/mercurial][5]).
- Use Node.js directly (instead of executing shell scripts configured in `hooks.*`).
- Replace existing plugins. For instance, integrate with the npm registry using their [programmatic API][6] (as opposed
  to calling `npm publish` in a child process like release-it itself does).

Internally, release-it uses its own plugin architecture and includes the following plugins:

- `git`
- `github`
- `gitlab`
- `npm`
- `version`

Each plugin has a different responsibility, and each enables itself:

- The `git` plugin is enabled if the current directory contains a `.git` directory.
- The `github` plugin becomes active if `github.release` is `true`.
- The `gitlab` plugin is enabled only if `gitlab.release` is `true`.
- The `npm` plugin looks for a `package.json` in the current directory.
- The `version` plugin is always enabled (it increments the version and prompts for it if needed).

## Using a plugin

Plugins are local to the project, or external npm packages. Plugin configuration consists of a module name with options.
This example uses the `release-it-plugin` module and is configured in `package.json`:

```json
{
  "devDependencies": {
    "release-it": "*",
    "release-it-plugin": "*"
  },
  "release-it": {
    "github": {
      "release": true
    },
    "plugins": {
      "release-it-plugin": {
        "key": "value"
      }
    }
  }
}
```

Alternatively, here's a `release-it-plugin` as a local module:

```json
{
  "plugins": {
    "./scripts/release-it-plugin.js": {
      "key": "value"
    }
  }
}
```

## Creating a plugin

To create a plugin, extend the `Plugin` class, and implement one or more release-cycle methods. See the "interface"
below (where none of the methods is required). Any of these methods can be `async`. See this [test helper][7] to get an
idea of the methods a release-it plugin can implement.

Note that `release-it` should be a `peerDependency` (and probably also a `devDependency` to use its helpers in the
plugin tests). Here's an example `package.json`:

```json
{
  "name": "release-it-plugin",
  "version": "1.0.0",
  "description": "My release-it plugin",
  "main": "index.js",
  "peerDependencies": {
    "release-it": "^14.2.0"
  },
  "devDependencies": {
    "release-it": "^14.2.0"
  }
}
```

Or see the [plugin-starterkit][8] for a good start.

### Example

This minimal example reads the current version from a `VERSION` file, and bumps it once the new version is known.

```js
class MyPlugin extends Plugin {
  getLatestVersion() {
    return fs.readFileSync('./VERSION', 'utf8').trim();
  }
  bump(version) {
    this.version = version;
    fs.writeFileSync('./VERSION', version);
  }
}
```

This plugin has made itself responsible for providing the latest version by implementing the `getLatestVersion` method.
Also, it writes the new version in the `./VERSION` file during the release process.

In the context of the whole release process, this may also be relevant for other plugins:

- If the `npm` plugin is enabled, that plugin will bump `package.json` with the return value of `getLatestVersion`.
- If the `git` plugin is enabled, its `beforeRelease` method will stage the changes so the updated `./VERSION` will be
  part of the release commit.

Since order matters here, the release-cycle methods of internal plugins are executed _after_ other plugins. Except for
the `release` and `afterRelease` methods at the end.

## API

- [Interface overview][9]
- [Static methods][10]
- [Release-cycle methods][11]
- [Getter methods][12]
- [Helper methods][13]
- [Execution Order][14]

### Interface overview

```js
class Plugin {
  static isEnabled() {}
  static disablePlugin() {}
  getInitialOptions() {}
  init() {}
  getName() {}
  getLatestVersion() {}
  getIncrement() {}
  getIncrementedVersionCI() {}
  getIncrementedVersion() {}
  beforeBump() {}
  bump() {}
  beforeRelease() {}
  release() {}
  afterRelease();
}
```

Note that any of the methods in the plugin can be `async` except for `disablePlugin()`. In the method signatures below
this is implied everywhere (e.g. `→ Boolean` means it should return a boolean, or a promise resolving to a boolean).

### Static methods

#### isEnabled() → Boolean

By default, a plugin is always enabled. Override the static `isEnabled` method to enable the plugin based on specific
conditions, such as plugin configuration or the presence of a file or directory.

#### disablePlugin() → String

In case a plugin replaces a core plugin, it should be disabled by returning the name of the core plugin. Return a string
(or array of strings) containing the plugin name (one or more of `version`, `git`, `github`, `gitlab`, `npm`).

### Release-cycle methods

Implement release-cycle methods to execute logic during the release process. All methods are run async, so `async/await`
can be used freely.

Make sure any method returns `false` when it's disabled or skipped, in order to skip the execution of the
`after:[plugin]:[method]` hook. this is especially relevant for the `release` method.

#### init()

Implement `init` to validate prerequisites, and gather application or package details such as the current version.

#### beforeBump()

Implement `beforeBump` to prepare things, gather and/or output interesting information for the user, such as a changelog
or other details to help the user confirm the release will be executed properly.

#### bump(version)

Implement `bump` to increment the version in manifests or other files containing the version of the application or
package (e.g. `package.json` for Node.js modules).

#### beforeRelease()

Implement `beforeRelease` to perform tasks that should happen after the bump, and stage things before the `release`.

#### release()

Implement `release` for the main flow of the plugin. This is where the "steps" should be declared (see [step][15] in
class API), resulting in prompts (interactive) or spinners (non-interactive) that will execute tasks for confirmed
steps.

#### afterRelease()

Implement `afterRelease` to provide details about a successful release, e.g. a link to the release page.

## Getter methods

Implement any of the following methods to be ahead of any core plugin and use that during the release process instead.

#### getName() → String

Provide the name of the package being released.

#### getLatestVersion() → SemVer

Implement `getLatestVersion` and return the latest version prior to the current release, so release-it can determine the
next version.

#### getInitialOptions(options, pluginName) → Object

By default, every plugin receives the options configured in `options[pluginName]`. For instance, the core `npm` plugin
receives the options under the `npm` property in the configuration. Other plugins receive the options as they are
configured in the `plugins` section. However, if a plugin requires additional options from other plugins, the
`getInitialOptions` is useful:

```js
getInitialOptions(options, pluginName) {
  return Object.assign({}, options[pluginName], {
    tagName: options.git.tagName,
  });
}
```

#### Internal getter methods

The following methods are mostly internal methods that normally should not be implemented in any plugin, but in rare
cases this might be useful.

##### getIncrement({ latestVersion, increment, isPreRelease, preReleaseId }) → String

Implement `getIncrement` to override the increment used by `getIncrementedVersionCI` by providing `major`, `minor` or
`patch`, otherwise staying with Version.js's default logics.

##### getIncrementedVersionCI({ latestVersion, increment, isPreRelease, preReleaseId }) → SemVer

Implement `getIncrementedVersionCI` to provide the next version without prompting the user (i.e. determine the next
version based on the provided `increment` value). This method exists to provide the next `version` to other elements of
the release process early on, such as the introduction text.

##### getIncrementedVersion({ latestVersion, increment, isPreRelease, preReleaseId }) → SemVer

Implement `getIncrementedVersion` to provide the next version, and prompt the user if this can't be determined
automatically.

### Helper methods

The `Plugin` class exposes helper methods, here's an overview:

#### this.setContext(context) → void

Set additional data local to the plugin during runtime.

#### this.getContext() → Object

Get the plugin options extended with additional runtime data set with `setContext`.

#### this.registerPrompts(...prompts) → void

Register one or more prompts and allow the user to confirm actions or provide details.

A prompt object looks like this:

```js
{
  type: 'confirm',
  name: 'my-prompt',
  message: 'Are you sure?'
}
```

Under the hood, [Inquirer.js][16] is used. See [Inquirer.js/#objects][17] for more details.

#### this.step() → Promise

Display a prompt or a spinner during the `release` release-cycle method. This automatically shows a prompt if
interactive, or a spinner in CI (non-interactive) mode.

```js
await this.step({
  enabled: true,
  task: () => this.doTask(),
  label: 'Doing task',
  prompt: 'my-prompt'
});
```

If the prompt receives a "No" from the user, the `task` callback is not executed.

#### this.exec() → Promise

Execute commands in the child process (i.e. the shell). This is used extensively by release-it to execute `git` and
`npm` commands. Be aware of cross-OS compatibility.

Use template variables to render replacements. For instance, the command `git log ${latestTag}...HEAD` becomes
`git log v1.2.3...HEAD` before being executed. The replacements are all configuration options (with the default values
in [config/release-it.json][18]), plus the following additional variables:

```text
version
latestVersion
latestTag
changelog
name
repo.remote, repo.protocol, repo.host, repo.owner, repo.repository, repo.project
```

The additional variables are available in every release-cycle method, except `init`.

Note that in dry runs, commands are **not** executed as they may contain write operations. Read-only operations should
add the `write: false` option to run in dry mode:

```js
this.exec('git log', { options: { write: false } });
```

#### this.debug() → void

Insert `this.debug(...)` statements to log interesting details when `NODE_DEBUG=release-it:* release-it ...` is used.
The output is namespaced automatically (e.g. `release-it:foo My log output`).

#### this.log() → void

Use `this.log.[verbose|warn|error|log|info]` to log and inform the user about what's going on in the release process.

### Execution order

Assuming there are two plugins configured, "PluginA" and "PluginB":

```json
{
  "plugins": {
    "PluginA": {},
    "PluginB": {}
  }
}
```

First, the `init` method is executed for `PluginA`, then `PluginB`, and then the core plugins: `npm` → `git` → `github`
→ `gitlab` → `version`.

Then the same for `getName` and `getLatestVersion`. For these getter methods, the value of the first plugin that returns
something is used throughout the release process. This allows a plugin to be ahead of core plugins.

After this, the `beforeBump`, `bump` and `beforeRelease` methods are executed for each plugin in the same order.

And finally, for `release` and `afterRelease` the order is reversed, so that tasks can be executed after release-it core
plugins are done. Examples include to trigger deployment hooks, or send a notification to indicate a successfull release
or deployment.

Here's an example:

- If the `npm` plugin is enabled, `npm.getName()` is the first plugin/method that returns something (the `name` from
  `package.json` is used in this case).
- If this plugin is not enabled, `getName` of the next plugin is invoked (e.g. the `git` plugin will infer the name from
  the remote Git url), etcetera.
- The methods of custom plugins are invoked first, so they can override the `name`, `latestVersion`, `repo`, and
  `changelog` values that would otherwise be taken from the core plugins.

## Available & example plugins

- All packages tagged with [`"release-it-plugin"` on npm][19].
- Recipe: [my-version][20] - example plugin
- [Internal release-it plugins][21]

[1]: #overview
[2]: #using-a-plugin
[3]: #creating-a-plugin
[4]: #available--example-plugins
[5]: https://github.com/release-it/mercurial
[6]: https://github.com/npm/libnpm
[7]: https://github.com/release-it/release-it/blob/main/test/util/index.js#L54
[8]: https://github.com/release-it/plugin-starterkit
[9]: #interface-overview
[10]: #static-methods
[11]: #release-cycle-methods
[12]: #getter-methods
[13]: #helper-methods
[14]: #execution-order
[15]: #thisstep--promise
[16]: https://github.com/SBoudrias/Inquirer.js
[17]: https://github.com/SBoudrias/Inquirer.js/#objects
[18]: ../config/release-it.json
[19]: https://www.npmjs.com/search?q=keywords:release-it-plugin
[20]: https://github.com/release-it/release-it/blob/main/docs/recipes/my-version.md
[21]: https://github.com/release-it/release-it/tree/main/lib/plugin
```

## File: `docs/pre-releases.md`
```markdown
# Manage pre-releases

With release-it, it's easy to create pre-releases: a version of your software that you want to make available, while
it's not in the stable semver range yet. Often "alpha", "beta", and "rc" (release candidate) are used as identifier for
pre-releases.

An example. The `awesome-pkg` is at version 1.3.0, and work is done for a new major update. To publish the latest beta
of the new major version:

```bash
release-it major --preRelease=beta
```

This will tag and release version `2.0.0-beta.0`. Notes:

- A normal `npm install` of `awesome-pkg` will still be at version 1.3.0.
- The [npm tag][1] will be "beta", install it using `npm install awesome-pkg@beta`
- A GitHub release will be marked as a "Pre-release".

The above command is actually a shortcut for:

```bash
release-it premajor --preReleaseId=beta --npm.tag=beta --github.preRelease
```

Consecutive beta releases (`2.0.0-beta.1` and so on):

```bash
release-it --preRelease
```

And when ready to release the next phase (e.g. release candidate, in this case `2.0.0-rc.0`):

```bash
release-it --preRelease=rc
```

And eventually, for `2.0.0`:

```bash
release-it major
```

<img src="./assets/release-it-prerelease.gif?raw=true" height="524">

When all commits since the latest major tag should be added to the changelog, use `--git.tagExclude`:

```bash
release-it major --git.tagExclude='*[-]*'
```

This will find the latest major matching tag, excluding the pre-release tags, which normally include `-` in their name.

Let's go back to when the latest release was `2.0.0-rc.0`. We added new features, which we don't want in the v2 release
yet, but instead in a later v2.1. A new pre-release id can be made for the minor release after in `2.1.0-alpha.0`:

```bash
release-it preminor --preRelease=alpha
```

Use `--preReleaseBase=1` to start counting at `1`. The first example at `1.3.0` will now bump to `2.0.0-beta.1` instead:

```bash
release-it major --preRelease=beta --preReleaseBase=1
```

Notes:

- Pre-releases work in tandem with [recommended bumps][2].
- You can still override individual options, e.g. `release-it --preRelease=rc --npm.tag=next`.
- See [semver.org][3] for more details about semantic versioning.

[1]: https://docs.npmjs.com/cli/dist-tag
[2]: https://github.com/release-it/conventional-changelog
[3]: http://semver.org
```

## File: `docs/dev/README.md`
```markdown
# External dependencies & APIs

## GitHub

- [octokit/rest.js][1]
- [repos.createRelease][2]
- [repos.uploadReleaseAsset][3]

## GitLab

- [GitLab API][4]
- [Releases API][5]
- [Upload a file][6]
- [Create a new release][7]

### Docker

- [Install GitLab with Docker][8]
- [GitLab Docker images][9]

To run the nightly build of GitLab:

```bash
docker run --hostname localhost --publish 443:443 --publish 80:80 --publish 22:22 --name gitlab --restart always --volume config:/etc/gitlab --volume logs:/var/log/gitlab --volume data:/var/opt/gitlab gitlab/gitlab-ce:nightly
```

[1]: https://github.com/octokit/rest.js
[2]: https://octokit.github.io/rest.js/#repos-create-release
[3]: https://octokit.github.io/rest.js/#repos-upload-release-asset
[4]: https://docs.gitlab.com/api/rest/
[5]: https://docs.gitlab.com/api/releases/
[6]: https://docs.gitlab.com/api/project_markdown_uploads/
[7]: https://docs.gitlab.com/api/releases/#create-a-release
[8]: https://docs.gitlab.com/install/docker/installation/
[9]: https://hub.docker.com/r/gitlab/gitlab-ce/
```

## File: `docs/dev/asciinema-to-svg`
```
asciinema rec release-it.cast
cat release-it.cast | svg-term --out release-it.svg --padding 10
```

## File: `docs/recipes/auto-changelog.md`
```markdown
# Auto-changelog

Please refer to [auto-changelog documentation][1] for more details and usage.

## Config

Add auto-changelog to the project:

```bash
npm install --save-dev auto-changelog
```

Example configuration in the release-it config:

```json
{
  "git": {
    "changelog": "npx auto-changelog --stdout --commit-limit false --unreleased --template https://raw.githubusercontent.com/release-it/release-it/main/templates/changelog-compact.hbs"
  },
  "hooks": {
    "after:bump": "npx auto-changelog -p"
  }
}
```

## Template

This is basically a copy of the [default auto-changelog template][2]. However, the title is removed, and the `releases`
iterator has a `{{#if @first}}` block to only show commits within the unreleased tag:

```handlebars
{{#each releases}}
  {{#if @first}}
    {{#each merges}}
      - {{{message}}}{{#if href}} [`#{{id}}`]({{href}}){{/if}}
    {{/each}}
    {{#each fixes}}
      - {{{commit.subject}}}{{#each fixes}}{{#if href}} [`#{{id}}`]({{href}}){{/if}}{{/each}}
    {{/each}}
    {{#each commits}}
      - {{#if breaking}}**Breaking change:** {{/if}}{{{subject}}}{{#if href}} [`{{shorthash}}`]({{href}}){{/if}}
    {{/each}}
  {{/if}}
{{/each}}
```

The template above [changelog-compact.hbs][3] can also be used directly from here:

```json
{
  "git": {
    "changelog": "npx auto-changelog --stdout --commit-limit false --unreleased --template https://raw.githubusercontent.com/release-it/release-it/main/templates/changelog-compact.hbs"
  },
  "hooks": {
    "after:bump": "npx auto-changelog -p"
  }
}
```

Projects without a `package.json` that need to generate a `CHANGELOG.md` compatible with [https://keepachangelog.com][4]
can use this example:

```json
{
  "git": {
    "changelog": "npx auto-changelog --stdout --commit-limit false --unreleased --template https://raw.githubusercontent.com/release-it/release-it/main/templates/changelog-compact.hbs"
  },
  "hooks": {
    "after:bump": "npx auto-changelog --commit-limit false --template https://raw.githubusercontent.com/release-it/release-it/main/templates/keepachangelog.hbs"
  }
}
```

[1]: https://github.com/CookPete/auto-changelog
[2]: https://github.com/CookPete/auto-changelog/blob/master/templates/compact.hbs
[3]: ../../templates/changelog-compact.hbs
[4]: https://keepachangelog.com
```

## File: `docs/recipes/distribution-repo.md`
```markdown
# Distribution repository

Some projects use a distribution repository. Generated files (such as compiled assets or documentation) can be
distributed to a separate repository. Or to a separate branch, such as a `gh-pages`. Some examples include [shim
repositories][1] and a separate [packaged Angular.js repository][2] for distribution on npm and Bower.

The `dist.repo` setting is deprecated since [v9.8.0][3], and removed in v10. However, publishing a seperate distribution
can still be achieved. There are many solutions to this, here are some basic examples for inspiration.

## Separate distribution repo

This technique is largely depending on [npm-version][4].

In `.release-it.json` of the source repo:

```json
{
  "hooks": {
    "before:init": "git clone https://github.com/example/dist-repo .stage",
    "after:release": "cd .stage && npm version ${version} && cd -"
  }
}
```

In `package.json` of dist repo:

```json
{
  "name": "my-dist-package",
  "version": "1.0.0",
  "scripts": {
    "version": "echo copy ../dist/files > ./files && git add . --all",
    "postversion": "git push --follow-tags"
  }
}
```

- Clones the dist repo to `./.stage`.
- Runs `npm version`, which automatically runs the `version` and `postversion` scripts.

## Distribution branch in same repo

A single repository, with e.g. a `dist` or `gh-pages` branch. In `package.json`:

```json
{
  "name": "my-package",
  "version": "1.0.0",
  "release-it": {
    "npm": {
      "publish": false
    },
    "hooks": {
      "before:init": "git clone https://github.com/my/my-package -b dist .stage",
      "before:release": "npm run build",
      "after:release": "cd .stage && git add . --all && git commit -m 'Updated!' && git push && cd -"
    }
  }
}
```

- Clone itself to `./.stage` while checking out the `dist` branch.
- Execute `npm run build` to generate distribution files (into `./.stage`)
- Stage all files, commit and push back to origin.

[1]: https://github.com/components
[2]: https://github.com/angular/bower-angular
[3]: https://github.com/release-it/release-it/releases/tag/9.8.0
[4]: https://docs.npmjs.com/cli/version.html
```

## File: `docs/recipes/git-cliff.md`
```markdown
# Git-cliff

Please refer to [git-cliff documentation][1] for more details and usage.

## Config

Add git-cliff to the project:

```bash
npm install --save-dev git-cliff
```

Git-cliff has the ability to use the Conventional Commits convention to automatically set the package version.
Release-it allows the user to select the version that should be released. Therefore, it may be helpful to generate the
changelog from the version in the `package.json` that was bumped by release-it.

```sh
#!/usr/bin/env bash

NODE_VERSION=$(node -p -e "require('./package.json').version")

if [ "$1" = "stdout" ]; then
    npm exec git-cliff -o - --unreleased --tag $NODE_VERSION
else
    npm exec git-cliff -o './CHANGELOG.md' --tag $NODE_VERSION
fi
```

Example configuration in the release-it config:

```json
{
  "hooks": {
    "after:bump": "./changelog.sh"
  },
  "github": {
    "releaseNotes": "./changelog.sh stdout"
  }
}
```

## Template

Git-cliff uses Tera as a templating language, which is inspired by Jinja2 and Django templates.

See [git-cliff syntax docs][2] for more information.

## Monorepos

Git-cliff has a `--include-path` flag to scope changes to a specific directory path.

See [git-cliff monorepo docs][3] for more information.

[1]: https://github.com/orhun/git-cliff
[2]: https://git-cliff.org/docs/templating/examples
[3]: https://git-cliff.org/docs/usage/monorepos
```

## File: `docs/recipes/monorepo.md`
```markdown
# Monorepo

Although release-it was not originally designed for monorepos, certain workflows with multiple workspaces can still be
installed.

If all workspaces should be bumped to the same version and are published at the same time, then follow the two steps in
this guide.

- A single `npm run release` to publish each package, finishing with a run for the monorepo root.
- Each package will be published one after another separately.
- The `version` in each `package.json` will be bumped.
- All internal packages in `dependencies` and `devDependencies` will be bumped to the same version.

There is nothing fancy going on, this works with existing solutions. I did not test this with the conventional-changelog
plugin. Currently using this setup myself in the [7-docs][1] monorepo. See [this commit][2] that follows this guide.

## 1. Configure root/monorepo

- Install the bumper plugin: `npm install -D @release-it/bumper`
- Order the `workspaces` so a workspace depending on another comes after it. See the examples below.
- Add a `release` script to run the `release` script of all workspaces and end with itself.
- Make sure it contains `git.requireCleanWorkingDir: false` (to include all updated `package.json` files)
- Make sure to add `npm.publish: false` here if the root should not be published.
- Add e.g. `github.release: true` and/or other changelog related tasks to the root config.

Example:

```json
{
  "name": "root-package",
  "version": "1.0.0",
  "workspaces": ["packages/a", "packages/b", "packages/c"],
  "scripts": {
    "release": "npm run release --workspaces && release-it"
  },
  "release-it": {
    "git": {
      "requireCleanWorkingDir": false
    }
  }
}
```

## 2. Configure each workspace

- Add a `"release": "release-it"` script to each workspace's `package.json`.
- Add a `release-it` config (either to `package.json` or in `.release-it.json`)
- Make sure it contains `git: false`
- Add `@release-it/bumper` config if it has internal dependencies so these `dependencies` or `devDependencies` will be
  automatically bumped during the release-it process.

### Without internal dependencies

Example for a workspace without internal dependencies:

```json
{
  "name": "package-a",
  "version": "1.0.0",
  "scripts": {
    "release": "release-it"
  },
  "dependencies": {},
  "release-it": {
    "git": false
  }
}
```

### With internal dependencies

Example for a workspace with internal dependencies:

```json
{
  "name": "package-c",
  "version": "1.0.0",
  "scripts": {
    "release": "release-it"
  },
  "dependencies": {
    "package-a": "1.0.0"
  },
  "devDependencies": {
    "package-b": "1.0.0"
  },
  "release-it": {
    "git": false,
    "plugins": {
      "@release-it/bumper": {
        "out": {
          "file": "package.json",
          "path": ["dependencies.package-a", "devDependencies.package-b"]
        }
      }
    }
  }
}
```

[1]: https://github.com/7-docs/7-docs
[2]: https://github.com/7-docs/7-docs/commit/128df8b8f3b39f0e5e27edf4fb0a1a732300ddbc
```

## File: `docs/recipes/my-version.md`
```markdown
# Example plugin: my-version

This example reads a `VERSION` file, bumps it, and publishes to a package repository. It is only enabled if the
`./VERSION` file actually exists.

```javascript
import { Plugin } from 'release-it';
import fs from 'fs';
import path from 'path';

const prompts = {
  publish: {
    type: 'confirm',
    message: context => `Publish version ${context.version} of ${context.name}?`
  }
};

class MyVersionPlugin extends Plugin {
  constructor(...args) {
    super(...args);
    this.registerPrompts(prompts);
    this.setContext({ versionFile: path.resolve('./VERSION') });
  }
  static isEnabled() {
    try {
      fs.accessSync('./VERSION');
      return true;
    } catch (err) {}
    return false;
  }
  init() {
    const data = fs.readFileSync(this.versionFile);
    const latestVersion = data.toString().trim();
    this.setContext({ latestVersion });
  }
  getPackageName() {
    return this.config.getContext('name');
  }
  getLatestVersion() {
    return this.getContext('latestVersion');
  }
  bump(version) {
    this.setContext({ version });
    fs.writeFileSync(this.getContext('versionFile'), version);
  }
  async release() {
    await this.step({ task: () => this.publish(), label: 'Publish with pkg-manager', prompt: 'publish' });
  }
  publish() {
    // <insert command to publish>, example: await this.exec('pkg-manager publish');
    this.isReleased = true;
  }
  afterRelease() {
    if (this.isReleased) {
      const name = this.getPackageName();
      const { version } = this.getContext();
      this.log.log(`🔗 https://registry.example.org/${name}/${version}`);
    }
  }
}

export default MyVersionPlugin;
```

To add this plugin to a project, use this configuration:

```json
{
  "plugins": {
    "my-version": {
      "unused": "option"
    }
  }
}
```
```

## File: `docs/recipes/programmatic.md`
```markdown
# Use release-it programmatically

From Node.js scripts, release-it can also be used as a dependency:

```js
import release from 'release-it';

release(options).then(output => {
  console.log(output);
  // { version, latestVersion, name, changelog }
});
```
```

## File: `docs/recipes/require-commits.md`
```markdown
# Require Commits

By default, release-it does not check the number of commits upfront. Configure `"git.requireCommits": true` to exit the
release-it process if there are no commits since the latest tag.

### Using `hooks.before:init` as well?

It is a good idea to verify things are working properly (e.g. by running tests) before releasing the project. However,
the check enabled by `git.requireCommits` occurs after `hooks.before:init` (as the former is part of the Git plugin). In
case time-consuming scripts are defined in `hooks.before:init` and things should be sped up, consider either moving the
scripts to `hooks.after:init`, or adding a custom shell script like this:

```json
{
  "hooks": {
    "before:init": [
      "if [ \"$(git log $(git describe --tags --abbrev=0)..HEAD)\" = \"\" ]; then exit 1; fi;",
      "npm test"
    ]
  }
}
```

Or even take it upfront like this:

```bash
[ "$(git rev-list $(git describe --tags --abbrev=0)..HEAD --count)" = "0" ] || release-it
```
```

## File: `lib/args.js`
```javascript
import parseArgs from 'yargs-parser';

const aliases = {
  c: 'config',
  d: 'dry-run',
  h: 'help',
  i: 'increment',
  v: 'version',
  V: 'verbose'
};

const booleanOptions = [
  'dry-run',
  'ci',
  'git',
  'npm',
  'github',
  'gitlab',
  'git.addUntrackedFiles',
  'git.requireCleanWorkingDir',
  'git.requireUpstream',
  'git.requireCommits',
  'git.requireCommitsFail',
  'git.commit',
  'git.tag',
  'git.push',
  'git.getLatestTagFromAllRefs',
  'git.skipChecks',
  'github.release',
  'github.autoGenerate',
  'github.preRelease',
  'github.draft',
  'github.skipChecks',
  'github.web',
  'github.comments.submit',
  'gitlab.release',
  'gitlab.autoGenerate',
  'gitlab.preRelease',
  'gitlab.draft',
  'gitlab.useIdsForUrls',
  'gitlab.useGenericPackageRepositoryForAssets',
  'gitlab.skipChecks',
  'npm.publish',
  'npm.ignoreVersion',
  'npm.allowSameVersion',
  'npm.skipChecks'
];

export const parseCliArguments = args => {
  const options = parseArgs(args, {
    boolean: booleanOptions,
    alias: aliases,
    configuration: {
      'parse-numbers': false,
      'camel-case-expansion': false
    }
  });
  if (options.V) {
    options.verbose = typeof options.V === 'boolean' ? options.V : options.V.length;
    delete options.V;
  }
  options.increment = options._[0] || options.i;
  return options;
};
```

## File: `lib/cli.js`
```javascript
import { readJSON } from './util.js';
import runTasks from './index.js';

const pkg = readJSON(new URL('../package.json', import.meta.url));

const helpText = `Release It! v${pkg.version}

  Usage: release-it <increment> [options]

  Use e.g. "release-it minor" directly as shorthand for "release-it --increment=minor".

  -c --config            Path to local configuration options [default: ".release-it.json"]
  -d --dry-run           Do not touch or write anything, but show the commands
  -h --help              Print this help
  -i --increment         Increment "major", "minor", "patch", or "pre*" version; or specify version [default: "patch"]
     --ci                No prompts, no user interaction; activated automatically in CI environments
     --only-version      Prompt only for version, no further interaction
  -v --version           Print release-it version number
     --release-version   Print version number to be released
     --changelog         Print changelog for the version to be released
  -V --verbose           Verbose output (user hooks output)
  -VV                    Extra verbose output (also internal commands output)

For more details, please see https://github.com/release-it/release-it`;

/** @internal */
export const version = () => console.log(`v${pkg.version}`);

/** @internal */
export const help = () => console.log(helpText);

export default async options => {
  if (options.version) {
    version();
  } else if (options.help) {
    help();
  } else {
    return runTasks(options);
  }
  return Promise.resolve();
};
```

## File: `lib/config.js`
```javascript
import util from 'node:util';
import assert from 'node:assert';
import { isCI } from 'ci-info';
import defaultsDeep from '@nodeutils/defaults-deep';
import { isObjectStrict } from '@phun-ky/typeof';
import merge from 'lodash.merge';
import { loadConfig as loadC12 } from 'c12';
import { get, getSystemInfo, readJSON } from './util.js';

const debug = util.debug('release-it:config');
const defaultConfig = readJSON(new URL('../config/release-it.json', import.meta.url));

class Config {
  constructor(config = {}) {
    this.constructorConfig = config;
    this.contextOptions = {};
    debug({ system: getSystemInfo() });
  }

  async init() {
    await loadOptions(this.constructorConfig).then(({ options, localConfig }) => {
      this._options = options;
      this._localConfig = localConfig;
      debug(this._options);
    });
  }

  getContext(path) {
    const context = merge({}, this.options, this.contextOptions);
    return path ? get(context, path) : context;
  }

  setContext(options) {
    debug(options);
    merge(this.contextOptions, options);
  }

  setCI(value = true) {
    this.options.ci = value;
  }

  get defaultConfig() {
    return defaultConfig;
  }

  get isDryRun() {
    return Boolean(this.options['dry-run']);
  }

  get isIncrement() {
    return this.options.increment !== false;
  }

  get isVerbose() {
    return Boolean(this.options.verbose);
  }

  get verbosityLevel() {
    return this.options.verbose;
  }

  get isDebug() {
    return debug.enabled;
  }

  get isCI() {
    return Boolean(this.options.ci) || this.isReleaseVersion || this.isChangelog;
  }

  get isPromptOnlyVersion() {
    return this.options['only-version'];
  }

  get isReleaseVersion() {
    return Boolean(this.options['release-version']);
  }

  get isChangelog() {
    return Boolean(this.options['changelog']);
  }

  get options() {
    assert(this._options, `The "options" not resolve yet`);
    return this._options;
  }

  get localConfig() {
    assert(this._localConfig, `The "localConfig" not resolve yet`);
    return this._localConfig;
  }
}

async function loadOptions(constructorConfig) {
  const localConfig = await loadLocalConfig(constructorConfig);
  const merged = defaultsDeep(
    {},
    constructorConfig,
    {
      ci: isCI
    },
    localConfig,
    defaultConfig
  );
  const expanded = expandPreReleaseShorthand(merged);

  return {
    options: expanded,
    localConfig
  };
}

function expandPreReleaseShorthand(options) {
  const { increment, preRelease, preReleaseId, snapshot, preReleaseBase } = options;
  const isPreRelease = Boolean(preRelease) || Boolean(snapshot);
  const inc = snapshot ? 'prerelease' : increment;
  const preId = typeof preRelease === 'string' ? preRelease : typeof snapshot === 'string' ? snapshot : preReleaseId;
  options.version = {
    increment: inc,
    isPreRelease,
    preReleaseId: preId,
    preReleaseBase
  };
  if (typeof snapshot === 'string' && options.git) {
    // Pre set and hard code some options
    options.git.tagMatch = `0.0.0-${snapshot}.[0-9]*`;
    options.git.getLatestTagFromAllRefs = true;
    options.git.requireBranch = '!main';
    options.git.requireUpstream = false;
    options.npm.ignoreVersion = true;
  }
  return options;
}

async function loadLocalConfig(constructorConfig) {
  const file = resolveFile();
  const dir = resolveDir();
  const extend = resolveExtend();
  const defaultConfig = resolveDefaultConfig();

  if (file === false) return {};

  const resolvedConfig = await loadC12({
    name: 'release-it',
    configFile: file,
    packageJson: true,
    rcFile: false,
    envName: false,
    cwd: dir,
    extend,
    defaultConfig
  }).catch(() => {
    throw new Error(`Invalid configuration file at ${file}`);
  });

  debug('Loaded local config', resolvedConfig.config);
  return isObjectStrict(resolvedConfig.config) ? resolvedConfig.config : {};

  function resolveFile() {
    if (constructorConfig.config === false) return false;

    if (constructorConfig.config === true) return '.release-it';

    return constructorConfig.config ?? '.release-it';
  }

  function resolveDir() {
    return constructorConfig.configDir ?? process.cwd();
  }

  function resolveExtend() {
    return constructorConfig.extends === false ? false : undefined;
  }

  function resolveDefaultConfig() {
    return {
      extends: constructorConfig.extends === false ? undefined : constructorConfig.extends
    };
  }
}

export default Config;
```

## File: `lib/index.js`
```javascript
import { getPlugins } from './plugin/factory.js';
import Logger from './log.js';
import Config from './config.js';
import Shell from './shell.js';
import Prompt from './prompt.js';
import Spinner from './spinner.js';
import { reduceUntil, parseVersion, castArray } from './util.js';

const runTasks = async (opts, di) => {
  let container = {};

  try {
    Object.assign(container, di);
    container.config = container.config || new Config(opts);
    await container.config.init();

    const { config } = container;
    const { isCI, isVerbose, verbosityLevel, isDryRun, isChangelog, isReleaseVersion } = config;

    container.log = container.log || new Logger({ isCI, isVerbose, verbosityLevel, isDryRun });
    container.spinner = container.spinner || new Spinner({ container, config });
    container.prompt = container.prompt || new Prompt({ container: { config } });
    container.shell = container.shell || new Shell({ container });

    const { log, shell, spinner } = container;

    const options = config.getContext();

    const { hooks } = options;

    const runHook = async (...name) => {
      const scripts = hooks[name.join(':')];
      if (!scripts || !scripts.length) return;
      const context = config.getContext();
      const external = true;
      for (const script of castArray(scripts)) {
        const task = () => shell.exec(script, { external }, context);
        await spinner.show({ task, label: script, context, external });
      }
    };

    const runLifeCycleHook = async (plugin, name, ...args) => {
      if (plugin === plugins.at(0)) await runHook('before', name);
      await runHook('before', plugin.namespace, name);
      const willHookRun = (await plugin[name](...args)) !== false;
      if (willHookRun) {
        await runHook('after', plugin.namespace, name);
      }
      if (plugin === plugins.at(-1)) await runHook('after', name);
    };

    const [internal, external] = await getPlugins(config, container);
    let plugins = [...external, ...internal];

    for (const plugin of plugins) {
      await runLifeCycleHook(plugin, 'init');
    }

    const { increment, isPreRelease, preReleaseId, preReleaseBase } = options.version;

    const name = await reduceUntil(plugins, plugin => plugin.getName());
    const latestVersion = (await reduceUntil(plugins, plugin => plugin.getLatestVersion())) || '0.0.0';
    const changelog = await reduceUntil(plugins, plugin => plugin.getChangelog(latestVersion));

    if (isChangelog) {
      if (changelog) {
        console.log(changelog);
        process.exit(0);
      } else {
        log.warn('No changelog found');
        process.exit(1);
      }
    }

    const incrementBase = { latestVersion, increment, isPreRelease, preReleaseId, preReleaseBase };

    const { snapshot } = config.options;
    if (snapshot && (!incrementBase.latestVersion.startsWith('0.0.0') || incrementBase.latestVersion === '0.0.0')) {
      // Reading the latest version first allows to increment the final counter, fake it if it's not a snapshot:
      incrementBase.latestVersion = `0.0.0-0`;
    }

    let version;
    if (config.isIncrement) {
      incrementBase.increment = await reduceUntil(plugins, plugin => plugin.getIncrement(incrementBase));
      version = await reduceUntil(plugins, plugin => plugin.getIncrementedVersionCI(incrementBase));
    } else {
      version = latestVersion;
    }

    config.setContext({ name, latestVersion, version, changelog });

    if (!isReleaseVersion) {
      const action = config.isIncrement ? 'release' : 'update';
      const suffix = version && config.isIncrement ? `${latestVersion}...${version}` : `currently at ${latestVersion}`;
      log.obtrusive(`🚀 Let's ${action} ${name} (${suffix})`);
      log.preview({ title: 'changelog', text: changelog });
    }

    if (config.isIncrement) {
      version = version || (await reduceUntil(plugins, plugin => plugin.getIncrementedVersion(incrementBase)));
    }

    if (isReleaseVersion) {
      if (version) {
        console.log(version);
        process.exit(0);
      } else {
        log.warn(`No new version to release`);
        process.exit(1);
      }
    }

    if (version) {
      config.setContext(parseVersion(version));

      if (config.isPromptOnlyVersion) {
        config.setCI(true);
      }

      for (const hook of ['beforeBump', 'bump', 'beforeRelease']) {
        for (const plugin of plugins) {
          const args = hook === 'bump' ? [version] : [];
          await runLifeCycleHook(plugin, hook, ...args);
        }
      }

      plugins = [...internal, ...external];

      for (const hook of ['release', 'afterRelease']) {
        for (const plugin of plugins) {
          await runLifeCycleHook(plugin, hook);
        }
      }
    } else {
      log.obtrusive(`No new version to release`);
    }

    log.log(`🏁 Done (in ${Math.floor(process.uptime())}s.)`);

    return {
      name,
      changelog,
      latestVersion,
      version
    };
  } catch (err) {
    const { log } = container;

    const errorMessage = err.message || err;
    const logger = log || console;

    err.cause === 'INFO' ? logger.info(errorMessage) : logger.error(errorMessage);

    throw err;
  }
};

export default runTasks;

export { default as Config } from './config.js';

export { default as Plugin } from './plugin/Plugin.js';
```

## File: `lib/log.js`
```javascript
import { EOL } from 'node:os';
import { styleText } from 'node:util';
import { isObjectLoose } from '@phun-ky/typeof';
import { upperFirst } from './util.js';

class Logger {
  constructor({ isCI = true, isVerbose = false, verbosityLevel = 0, isDryRun = false } = {}) {
    this.isCI = isCI;
    this.isVerbose = isVerbose;
    this.verbosityLevel = verbosityLevel;
    this.isDryRun = isDryRun;
  }

  shouldLog(isExternal) {
    return this.verbosityLevel === 2 || (this.isVerbose && isExternal);
  }

  log(...args) {
    console.log(...args);
  }

  error(...args) {
    console.error([styleText('red', 'ERROR'), ...args].join(' '));
  }

  info(...args) {
    console.error(styleText('gray', args.join(' ')));
  }

  warn(...args) {
    console.error([styleText('yellow', 'WARNING'), ...args].join(' '));
  }

  verbose(...args) {
    const { isExternal } = isObjectLoose(args.at(-1)) ? args.at(-1) : {};
    if (this.shouldLog(isExternal)) {
      console.error(...args.filter(str => typeof str === 'string'));
    }
  }

  exec(...args) {
    const { isDryRun: isExecutedInDryRun, isExternal, isCached } = isObjectLoose(args.at(-1)) ? args.at(-1) : {};
    if (this.shouldLog(isExternal) || this.isDryRun) {
      const prefix = isExecutedInDryRun == null ? '$' : '!';
      const command = args
        .map(cmd => (typeof cmd === 'string' ? cmd : Array.isArray(cmd) ? cmd.join(' ') : ''))
        .join(' ');
      const message = [prefix, command, isCached ? '[cached]' : ''].join(' ').trim();
      console.error(message);
    }
  }

  obtrusive(...args) {
    if (!this.isCI) this.log();
    this.log(...args);
    if (!this.isCI) this.log();
  }

  preview({ title, text }) {
    if (text) {
      const header = styleText('bold', upperFirst(title));
      const body = text.replace(new RegExp(EOL + EOL, 'g'), EOL);
      this.obtrusive(`${header}:${EOL}${body}`);
    } else {
      this.obtrusive(`Empty ${title.toLowerCase()}`);
    }
  }
}

export default Logger;
```

## File: `lib/prompt.js`
```javascript
import { confirm, input, select } from '@inquirer/prompts';

const types = { confirm, input, list: select };

class Prompt {
  constructor({ container }) {
    this.createPrompt = container.createPrompt;
    this.prompts = {};
  }

  register(pluginPrompts, namespace = 'default') {
    this.prompts[namespace] = this.prompts[namespace] || {};
    Object.assign(this.prompts[namespace], pluginPrompts);
  }

  async show({ enabled = true, prompt: promptName, namespace = 'default', task, context }) {
    if (!enabled) return false;

    const prompt = this.prompts[namespace][promptName];
    const options = {
      message: prompt.message(context)
    };

    if ('default' in prompt) options.default = prompt.default;
    if ('choices' in prompt) options.choices = prompt.choices(context);
    if ('transformer' in prompt) options.transformer = prompt.transformer(context);
    if ('validate' in prompt) options.validate = prompt.validate;
    if ('pageSize' in prompt) options.pageSize = prompt.pageSize;

    const answer = await (this.createPrompt
      ? this.createPrompt(prompt.type, options)
      : types[prompt.type](options));

    const doExecute = prompt.type === 'confirm' ? answer : true;

    return doExecute && task ? await task(answer) : false;
  }
}

export default Prompt;
```

## File: `lib/shell.js`
```javascript
import util from 'node:util';
import { spawn, exec } from 'node:child_process';
import { format } from './util.js';

const debug = util.debug('release-it:shell');

const noop = Promise.resolve();

class Shell {
  constructor({ container }) {
    this.log = container.log;
    this.config = container.config;
    this.cache = new Map();
  }

  exec(command, options = {}, context = {}) {
    if (!command || !command.length) return;
    return typeof command === 'string'
      ? this.execFormattedCommand(format(command, context), options)
      : this.execFormattedCommand(command, options);
  }

  async execFormattedCommand(command, options = {}) {
    const { isDryRun } = this.config;
    const isWrite = options.write !== false;
    const isExternal = options.external === true;
    const cacheKey = typeof command === 'string' ? command : command.join(' ');
    const isCached = !isExternal && this.cache.has(cacheKey);

    if (isDryRun && isWrite) {
      this.log.exec(command, { isDryRun });
      return noop;
    }

    this.log.exec(command, { isExternal, isCached });

    if (isCached) {
      return this.cache.get(cacheKey);
    }

    const result =
      typeof command === 'string'
        ? this.execStringCommand(command, options, { isExternal })
        : this.execWithArguments(command, options, { isExternal });

    if (!isExternal && !this.cache.has(cacheKey)) {
      this.cache.set(cacheKey, result);
    }

    return result;
  }

  execStringCommand(command, options, { isExternal }) {
    return new Promise((resolve, reject) => {
      const execOptions = options.env ? { env: options.env } : {};
      const proc = exec(command, execOptions, (err, stdout, stderr) => {
        stdout = stdout.toString().trimEnd();
        const code = !err ? 0 : err === 'undefined' ? 1 : err.code;
        debug({ command, options, code, stdout, stderr });
        if (code === 0) {
          resolve(stdout);
        } else {
          reject(new Error(stderr || stdout));
        }
      });
      proc.stdout.on('data', stdout => this.log.verbose(stdout.toString().trimEnd(), { isExternal }));
      proc.stderr.on('data', stderr => this.log.verbose(stderr.toString().trimEnd(), { isExternal }));
    });
  }

  async execWithArguments(command, options = {}, { isExternal } = {}) {
    const [program, ...programArgs] = command;
    const isInteractive = options.interactive === true;

    try {
      return await new Promise((resolve, reject) => {
        const spawnOptions = {
          stdio: isInteractive ? 'inherit' : ['inherit', 'pipe', 'pipe'],
          env: options.env,
          ...options
        };
        delete spawnOptions.interactive;

        const proc =
          process.platform === 'win32' && /^(npm|yarn|pnpm)$/.test(program)
            ? spawn(command.join(' '), [], { ...spawnOptions, shell: true })
            : spawn(program, programArgs, spawnOptions);

        let stdout = '';
        let stderr = '';

        if (!isInteractive) {
          proc.stdout.on('data', data => {
            stdout += data.toString();
          });

          proc.stderr.on('data', data => {
            stderr += data.toString();
          });
        }

        proc.on('close', code => {
          stdout = stdout === '""' ? '' : stdout;
          if (!isInteractive) this.log.verbose(stdout, { isExternal });
          debug({ command, options, stdout, stderr });

          if (code === 0) {
            resolve((stdout || stderr).trim());
          } else {
            if (stdout && !isInteractive) {
              this.log.log(`\n${stdout}`);
            }
            debug({ code, command, options, stdout, stderr });
            reject(new Error(stderr || stdout || `Process exited with code ${code}`));
          }
        });

        proc.on('error', err => {
          debug(err);
          reject(new Error(err.message));
        });
      });
    } catch (err) {
      debug(err);
      return Promise.reject(err);
    }
  }
}

export default Shell;
```

## File: `lib/spinner.js`
```javascript
import { oraPromise } from 'ora';
import { format } from './util.js';

const noop = Promise.resolve();

class Spinner {
  constructor({ container = {} } = {}) {
    this.config = container.config;
    this.ora = container.ora || oraPromise;
  }
  show({ enabled = true, task, label, external = false, context }) {
    if (!enabled) return noop;

    const { config } = this;
    this.isSpinnerDisabled = !config.isCI || config.isVerbose || config.isDryRun || config.isDebug;
    this.canForce = !config.isCI && !config.isVerbose && !config.isDryRun && !config.isDebug;

    const awaitTask = task();

    if (!this.isSpinnerDisabled || (external && this.canForce)) {
      const text = format(label, context);
      this.ora(awaitTask, text);
    }

    return awaitTask;
  }
}

export default Spinner;
```

## File: `lib/util.js`
```javascript
import fs, { close, openSync, statSync, utimesSync, accessSync } from 'node:fs'; // need import fs here due to test stubbing
import util from 'node:util';
import { EOL } from 'node:os';
import gitUrlParse from 'git-url-parse';
import semver from 'semver';
import osName from 'os-name';
import { Eta } from 'eta';
import Log from './log.js';

const debug = util.debug('release-it:shell');

const eta = new Eta({
  autoEscape: false,
  useWith: true,
  tags: ['${', '}'],
  parse: { interpolate: '' },
  rmWhitespace: false,
  autoTrim: false
});

const wait = ms => new Promise(resolve => setTimeout(resolve, ms));

const before = (n, func) => {
  var result;
  if (typeof func != 'function') {
    throw new TypeError('Missing argument for `func`');
  }
  n = parseInt(n);
  return function () {
    if (--n > 0) {
      result = func.apply(this, arguments);
    }
    if (n <= 1) {
      func = undefined;
    }
    return result;
  };
};
const tryStatFile = filePath => {
  try {
    return statSync(filePath);
  } catch (e) {
    debug(e);
    return null;
  }
};

/** @internal */
export const execOpts = {
  stdio: process.env.NODE_DEBUG && process.env.NODE_DEBUG.indexOf('release-it') === 0 ? 'pipe' : []
};

export const readJSON = file => JSON.parse(fs.readFileSync(file, 'utf8'));

const pkg = readJSON(new URL('../package.json', import.meta.url));

export const getSystemInfo = () => {
  return {
    'release-it': pkg.version,
    node: process.version,
    os: osName()
  };
};

export const format = (template = '', context = {}) => {
  if (!template || typeof template !== 'string') return '';
  if (!context || context === null || template.indexOf('${') === -1) return template;
  const log = new Log();
  try {
    return eta.renderString(template, context);
  } catch (error) {
    log.error(`Unable to render template with context:\n${template}\n${JSON.stringify(context)}`);
    log.error(error);
    throw error;
  }
};

export const truncateLines = (input, maxLines = 10, surplusText = null) => {
  const lines = input.split(EOL);
  const surplus = lines.length - maxLines;
  const output = lines.slice(0, maxLines).join(EOL);
  return surplus > 0 ? (surplusText ? `${output}${surplusText}` : `${output}${EOL}...and ${surplus} more`) : output;
};

export const rejectAfter = (ms, error) =>
  wait(ms).then(() => {
    throw error;
  });

export const parseGitUrl = remoteUrl => {
  if (!remoteUrl) return { host: null, owner: null, project: null, protocol: null, remote: null, repository: null };
  const normalizedUrl = (remoteUrl || '')
    .replace(/^[A-Z]:\\\\/, 'file://') // Assume file protocol for Windows drive letters
    .replace(/^\//, 'file://') // Assume file protocol if only /path is given
    .replace(/\\+/g, '/'); // Replace forward with backslashes
  const parsedUrl = gitUrlParse(normalizedUrl);
  const { resource: host, name: project, protocol, href: remote } = parsedUrl;
  const owner = protocol === 'file' ? parsedUrl.owner.split('/').at(-1) : parsedUrl.owner?.replace(/^\/+/, ''); // Fix owner for file protocol
  const repository = `${owner}/${project}`;
  return { host, owner, project, protocol, remote, repository };
};

export const reduceUntil = async (collection, fn) => {
  let result;
  for (const item of collection) {
    if (result) break;
    result = await fn(item);
  }
  return result;
};

export const hasAccess = path => {
  try {
    accessSync(path);
    return true;
  } catch (err) {
    return false;
  }
};

export const parseVersion = raw => {
  if (raw == null) return { version: raw, isPreRelease: false, preReleaseId: null };
  const version = semver.valid(raw) ? raw : semver.coerce(raw);
  if (!version) return { version: raw, isPreRelease: false, preReleaseId: null };
  const parsed = semver.parse(version);
  const isPreRelease = parsed.prerelease.length > 0;
  const preReleaseId = isPreRelease && isNaN(parsed.prerelease[0]) ? parsed.prerelease[0] : null;
  return {
    version: version.toString(),
    isPreRelease,
    preReleaseId
  };
};

export const e = (message, docs, fail = true) => {
  const error = new Error(docs ? `${message}${EOL}Documentation: ${docs}${EOL}` : message);
  error.code = fail ? 1 : 0;
  error.cause = fail ? 'ERROR' : 'INFO';
  return error;
};

/** @internal */
export const touch = (path, callback) => {
  const stat = tryStatFile(path);
  if (stat && stat.isDirectory()) {
    // don't error just exit
    return;
  }

  const fd = openSync(path, 'a');
  close(fd);
  const now = new Date();
  const mtime = now;
  const atime = now;
  utimesSync(path, atime, mtime);
  if (callback) {
    callback();
  }
};

export const fixArgs = args => (args ? (typeof args === 'string' ? args.split(' ') : args) : []);

// Remove npm_config_* variables set by others (e.g. pnpm) that npm warns about
export const getNpmEnv = () => {
  const env = { ...process.env };
  const removeVars = new Set([
    'npm_config_npm_globalconfig',
    'npm_config_verify_deps_before_run',
    'npm_config_overrides',
    'npm_config__jsr_registry'
  ]);
  for (const key of Object.keys(env)) if (removeVars.has(key.toLowerCase())) delete env[key];
  return env;
};

export const upperFirst = string => {
  return string ? string.charAt(0).toUpperCase() + string.slice(1) : '';
};

export const castArray = arr => {
  return Array.isArray(arr) ? arr : [arr];
};

export const once = fn => {
  return before(2, fn);
};

export const pick = (object, keys) => {
  return keys.reduce((obj, key) => {
    if (object && Object.prototype.hasOwnProperty.call(object, key)) {
      obj[key] = object[key];
    }
    return obj;
  }, {});
};

const parsePath = path => {
  const result = [];
  const regex = /[^.[\]]+|\[(?:(\d+)|["'](.+?)["'])\]/g;
  let match;

  while ((match = regex.exec(path)) !== null) {
    result.push(match[1] ?? match[2] ?? match[0]);
  }

  return result;
};

export const get = (obj, path, defaultValue = undefined) => {
  if (!path || typeof path !== 'string') {
    return defaultValue;
  }

  try {
    const keys = parsePath(path);
    return keys.reduce((acc, key) => acc?.[key], obj) ?? defaultValue;
  } catch {
    return defaultValue;
  }
};
```

## File: `lib/plugin/GitBase.js`
```javascript
import { EOL } from 'node:os';
import { format, parseGitUrl } from '../util.js';
import Plugin from './Plugin.js';

const options = { write: false };
const changelogFallback = 'git log --pretty=format:"* %s (%h)"';

class GitBase extends Plugin {
  async init() {
    const remoteUrl = await this.getRemoteUrl();
    await this.fetch(remoteUrl);

    const branchName = await this.getBranchName();
    const repo = parseGitUrl(remoteUrl);
    this.setContext({ remoteUrl, branchName, repo });
    this.config.setContext({ remoteUrl, branchName, repo });

    const latestTag = await this.getLatestTagName();
    const secondLatestTag = !this.config.isIncrement ? await this.getSecondLatestTagName(latestTag) : null;
    const tagTemplate = this.options.tagName || ((latestTag || '').match(/^v/) ? 'v${version}' : '${version}');
    this.config.setContext({ latestTag, secondLatestTag, tagTemplate });
  }

  getName() {
    const repo = this.getContext('repo');
    return repo.project;
  }

  getLatestVersion() {
    const { tagTemplate, latestTag } = this.config.getContext();
    const prefix = format(tagTemplate.replace(/\$\{version\}/, ''), this.config.getContext());
    return latestTag ? latestTag.replace(prefix, '').replace(/^v/, '') : null;
  }

  async getCommitsSinceLatestTag(commitsPath = '') {
    const latestTagName = await this.getLatestTagName();
    const ref = latestTagName ? `${latestTagName}..HEAD` : 'HEAD';
    return this.exec(`git rev-list ${ref} --count ${commitsPath ? `-- ${commitsPath}` : ''}`, { options }).then(Number);
  }

  async getChangelog() {
    const { snapshot } = this.config.getContext();
    const { latestTag, secondLatestTag } = this.config.getContext();
    const context = { latestTag, from: latestTag, to: 'HEAD' };
    const { changelog, commit } = this.options;
    if (!changelog) return null;

    if (latestTag && !this.config.isIncrement) {
      if ((await this.getCommitsSinceLatestTag()) === 0) {
        context.from = secondLatestTag;
        context.to = `${latestTag}^1`;
      } else if (commit === false) {
        context.to = 'HEAD^1';
      }
    }

    // For now, snapshots do not get a changelog, as it often goes haywire (easy to add to release manually)
    if (snapshot) return '';

    if (!context.from && changelog.includes('${from}')) {
      return this.exec(changelogFallback);
    }

    return this.exec(changelog, { context, options });
  }

  bump(version) {
    const { tagTemplate } = this.config.getContext();
    const context = Object.assign(this.config.getContext(), { version });
    const tagName = format(tagTemplate, context) || version;
    this.setContext({ version });
    this.config.setContext({ tagName });
  }

  isRemoteName(remoteUrlOrName) {
    return remoteUrlOrName && !remoteUrlOrName.includes('/');
  }

  async getRemoteUrl() {
    const remoteNameOrUrl = this.options.pushRepo || (await this.getRemote()) || 'origin';
    return this.isRemoteName(remoteNameOrUrl)
      ? this.exec(`git remote get-url ${remoteNameOrUrl}`, { options }).catch(() =>
          this.exec(`git config --get remote.${remoteNameOrUrl}.url`, { options }).catch(() => null)
        )
      : remoteNameOrUrl;
  }

  async getRemote() {
    const branchName = await this.getBranchName();
    return branchName ? await this.getRemoteForBranch(branchName) : null;
  }

  getBranchName() {
    return this.exec('git rev-parse --abbrev-ref HEAD', { options }).catch(() => null);
  }

  getRemoteForBranch(branch) {
    return this.exec(`git config --get branch.${branch}.remote`, { options }).catch(() => null);
  }

  fetch(remoteUrl) {
    return this.exec('git fetch').catch(err => {
      this.debug(err);
      throw new Error(`Unable to fetch from ${remoteUrl}${EOL}${err.message}`);
    });
  }

  getLatestTagName() {
    const context = Object.assign({}, this.config.getContext(), { version: '*' });
    const match = format(this.options.tagMatch || this.options.tagName || '${version}', context);
    const exclude = this.options.tagExclude ? ` --exclude=${format(this.options.tagExclude, context)}` : '';
    if (this.options.getLatestTagFromAllRefs) {
      return this.exec(
        `git -c "versionsort.suffix=-" for-each-ref --count=1 --sort=-v:refname --format="%(refname:short)" refs/tags/${match}`,
        { options }
      ).then(
        stdout => stdout || null,
        () => null
      );
    } else {
      return this.exec(`git describe --tags --match=${match} --abbrev=0${exclude}`, { options }).then(
        stdout => stdout || null,
        () => null
      );
    }
  }

  async getSecondLatestTagName(latestTag) {
    const sha = await this.exec(`git rev-list ${latestTag || '--skip=1'} --tags --max-count=1`, {
      options
    });
    return this.exec(`git describe --tags --abbrev=0 "${sha}^"`, { options }).catch(() => null);
  }
}

export default GitBase;
```

## File: `lib/plugin/GitRelease.js`
```javascript
import { pick, readJSON } from '../util.js';
import GitBase from './GitBase.js';

const defaultConfig = readJSON(new URL('../../config/release-it.json', import.meta.url));

class GitRelease extends GitBase {
  static isEnabled(options) {
    return options.release;
  }

  getInitialOptions(options) {
    const baseOptions = super.getInitialOptions(...arguments);
    const git = options.git || defaultConfig.git;
    const gitOptions = pick(git, [
      'tagExclude',
      'tagName',
      'tagMatch',
      'getLatestTagFromAllRefs',
      'pushRepo',
      'changelog',
      'commit'
    ]);

    return Object.assign({}, gitOptions, baseOptions);
  }

  get token() {
    const { tokenRef } = this.options;
    return process.env[tokenRef] || null;
  }

  async beforeRelease() {
    const { releaseNotes: script } = this.options;
    const { changelog } = this.config.getContext();
    const releaseNotes =
      typeof script === 'function' || typeof script === 'string' ? await this.processReleaseNotes(script) : changelog;
    this.setContext({ releaseNotes });
    if (releaseNotes !== changelog) {
      this.log.preview({ title: 'release notes', text: releaseNotes });
    }
  }

  async processReleaseNotes(script) {
    if (typeof script === 'function') {
      const ctx = Object.assign({}, this.config.getContext(), { [this.namespace]: this.getContext() });
      return script(ctx);
    }

    if (typeof script === 'string') {
      return this.exec(script);
    }
  }

  afterRelease() {
    const { isReleased, releaseUrl, discussionUrl } = this.getContext();
    if (isReleased) {
      this.log.log(`🔗 ${releaseUrl}`);
    }
    if (discussionUrl) {
      this.log.log(`🔗 ${discussionUrl}`);
    }
  }
}

export default GitRelease;
```

## File: `lib/plugin/Plugin.js`
```javascript
import { debug } from 'node:util';
import merge from 'lodash.merge';
import { get } from '../util.js';

class Plugin {
  static isEnabled() {
    return true;
  }

  static disablePlugin() {
    return null;
  }

  constructor({ namespace, options = {}, container = {} } = {}) {
    this.namespace = namespace;
    this.options = Object.freeze(this.getInitialOptions(options, namespace));
    this.context = {};
    this.config = container.config;
    this.log = container.log;
    this.shell = container.shell;
    this.spinner = container.spinner;
    this.prompt = container.prompt;
    this.debug = debug(`release-it:${namespace}`);
  }

  getInitialOptions(options, namespace) {
    return options[namespace] || {};
  }

  init() {}
  getName() {}
  getLatestVersion() {}
  getChangelog() {}
  getIncrement() {}
  getIncrementedVersionCI() {}
  getIncrementedVersion() {}
  beforeBump() {}
  bump() {}
  beforeRelease() {}
  release() {}
  afterRelease() {}

  getContext(path) {
    const context = merge({}, this.options, this.context);

    return path ? get(context, path) : context;
  }

  setContext(context) {
    merge(this.context, context);
  }

  exec(command, { options, context = {} } = {}) {
    const ctx = Object.assign(context, this.config.getContext(), { [this.namespace]: this.getContext() });
    return this.shell.exec(command, options, ctx);
  }

  registerPrompts(prompts) {
    this.prompt.register(prompts, this.namespace);
  }

  async showPrompt(options) {
    options.namespace = this.namespace;
    return this.prompt.show(options);
  }

  step(options) {
    const context = Object.assign({}, this.config.getContext(), { [this.namespace]: this.getContext() });
    const opts = Object.assign({}, options, { context });
    const isException = this.config.isPromptOnlyVersion && ['incrementList', 'publish', 'otp'].includes(opts.prompt);
    return this.config.isCI && !isException ? this.spinner.show(opts) : this.showPrompt(opts);
  }
}

export default Plugin;
```

## File: `lib/plugin/factory.js`
```javascript
import url from 'node:url';
import path from 'node:path';
import util from 'node:util';
import { createRequire } from 'node:module';
import { castArray } from '../util.js';
import Version from './version/Version.js';
import Git from './git/Git.js';
import GitLab from './gitlab/GitLab.js';
import GitHub from './github/GitHub.js';
import npm from './npm/npm.js';

const debug = util.debug('release-it:plugins');

const pluginNames = ['npm', 'git', 'github', 'gitlab', 'version'];

const plugins = {
  version: Version,
  git: Git,
  gitlab: GitLab,
  github: GitHub,
  npm: npm
};

const load = async pluginName => {
  let plugin;
  try {
    const module = await import(pluginName);
    plugin = module.default;
  } catch (err) {
    debug(err);
    try {
      const module = await import(path.join(process.cwd(), pluginName));
      plugin = module.default;
    } catch (err) {
      debug(err);
      // In some cases or tests we might need to support legacy `require.resolve`
      const require = createRequire(process.cwd());
      const module = await import(url.pathToFileURL(require.resolve(pluginName, { paths: [process.cwd()] })));
      plugin = module.default;
    }
  }
  return [getPluginName(pluginName), plugin];
};

/** @internal */
export const getPluginName = pluginName => {
  if (pluginName.startsWith('.')) {
    return path.parse(pluginName).name;
  }

  return pluginName;
};

export let getPlugins = async (config, container) => {
  const context = config.getContext();
  const disabledPlugins = [];
  const enabledExternalPlugins = [];
  if (context.plugins) {
    for (const [pluginName, pluginConfig] of Object.entries(context.plugins)) {
      const [name, Plugin] = await load(pluginName);
      const [namespace, options] = pluginConfig.length === 2 ? pluginConfig : [name, pluginConfig];

      config.setContext({ [namespace]: options });

      if (await Plugin.isEnabled(options)) {
        const instance = new Plugin({ namespace, options: config.getContext(), container });
        debug({ namespace, options: instance.options });
        enabledExternalPlugins.push(instance);

        disabledPlugins.push(...pluginNames.filter(p => castArray(Plugin.disablePlugin(options)).includes(p)));
      }
    }
  }

  const enabledPlugins = await pluginNames.reduce(async (result, plugin) => {
    if (plugin in plugins && !disabledPlugins.includes(plugin)) {
      const Plugin = plugins[plugin];
      const pluginOptions = context[plugin];
      if (await Plugin.isEnabled(pluginOptions)) {
        const instance = new Plugin({ namespace: plugin, options: context, container });
        debug({ namespace: plugin, options: instance.options });
        (await result).push(instance);
      }
    }
    return result;
  }, []);

  return [enabledPlugins, enabledExternalPlugins];
};
```

## File: `lib/plugin/git/Git.js`
```javascript
import { EOL } from 'node:os';
import { spawn } from 'node:child_process';
import matcher from 'wildcard-match';
import { format, e, fixArgs, once, castArray } from '../../util.js';
import GitBase from '../GitBase.js';
import prompts from './prompts.js';

const noop = Promise.resolve();
const invalidPushRepoRe = /^\S+@/;
const options = { write: false };

const docs = 'https://git.io/release-it-git';

async function isGitRepo() {
  return await new Promise(resolve => {
    const process = spawn('git', ['rev-parse', '--git-dir']);
    process.on('close', code => resolve(code === 0));
    process.on('error', () => resolve(false));
  });
}

class Git extends GitBase {
  constructor(...args) {
    super(...args);
    this.registerPrompts(prompts);
  }

  static async isEnabled(options) {
    return options !== false && (await isGitRepo());
  }

  async init() {
    if (this.options.requireBranch && !(await this.isRequiredBranch(this.options.requireBranch))) {
      throw e(`Must be on branch ${this.options.requireBranch}`, docs);
    }
    if (this.options.requireCleanWorkingDir && !(await this.isWorkingDirClean())) {
      throw e(`Working dir must be clean.${EOL}Please stage and commit your changes.`, docs);
    }

    await super.init();

    const remoteUrl = this.getContext('remoteUrl');
    if (this.options.push && !remoteUrl) {
      throw e(`Could not get remote Git url.${EOL}Please add a remote repository.`, docs);
    }
    if (this.options.requireUpstream && !(await this.hasUpstreamBranch())) {
      throw e(`No upstream configured for current branch.${EOL}Please set an upstream branch.`, docs);
    }
    if (this.options.requireCommits && (await this.getCommitsSinceLatestTag(this.options.commitsPath)) === 0) {
      throw e(`There are no commits since the latest tag.`, docs, this.options.requireCommitsFail);
    }
  }

  rollback() {
    this.log.info('Rolling back changes...');
    const { tagName } = this.config.getContext();
    const { isCommitted, isTagged } = this.getContext();
    if (isTagged) {
      this.log.info(`Deleting local tag ${tagName}`);
      this.exec(`git tag --delete ${tagName}`);
    }

    this.log.info(`Resetting local changes made`);
    this.exec(`git reset --hard HEAD${isCommitted ? '~1' : ''}`);
  }

  enableRollback() {
    this.rollbackOnce = once(this.rollback.bind(this));
    process.on('SIGINT', this.rollbackOnce);
    process.on('exit', this.rollbackOnce);
  }

  disableRollback() {
    if (this.rollbackOnce) {
      process.removeListener('SIGINT', this.rollbackOnce);
      process.removeListener('exit', this.rollbackOnce);
    }
  }

  async beforeRelease() {
    if (this.options.commit) {
      if (this.options.requireCleanWorkingDir) {
        this.enableRollback();
      }
      const changeSet = await this.status();
      this.log.preview({ title: 'changeset', text: changeSet });
      await this.stageDir();
    }
  }

  async release() {
    const { commit, tag, push } = this.options;
    await this.step({ enabled: commit, task: () => this.commit(), label: 'Git commit', prompt: 'commit' });
    await this.step({ enabled: tag, task: () => this.tag(), label: 'Git tag', prompt: 'tag' });
    return !!(await this.step({ enabled: push, task: () => this.push(), label: 'Git push', prompt: 'push' }));
  }

  async isRequiredBranch() {
    const branch = await this.getBranchName();
    const requiredBranches = castArray(this.options.requireBranch);
    const [branches, negated] = requiredBranches.reduce(
      ([p, n], b) => (b.startsWith('!') ? [p, [...n, b.slice(1)]] : [[...p, b], n]),
      [[], []]
    );
    return (
      (branches.length > 0 ? matcher(branches)(branch) : true) &&
      (negated.length > 0 ? !matcher(negated)(branch) : true)
    );
  }

  async hasUpstreamBranch() {
    const ref = await this.exec('git symbolic-ref HEAD', { options });
    const branch = await this.exec(`git for-each-ref --format="%(upstream:short)" ${ref}`, { options }).catch(
      () => null
    );
    return Boolean(branch);
  }

  tagExists(tag) {
    return this.exec(`git show-ref --tags --quiet --verify -- refs/tags/${tag}`, { options }).then(
      () => true,
      () => false
    );
  }

  isWorkingDirClean() {
    return this.exec('git diff --quiet HEAD', { options }).then(
      () => true,
      () => false
    );
  }

  async getUpstreamArgs(pushRepo) {
    if (pushRepo && !this.isRemoteName(pushRepo)) {
      // Use (only) `pushRepo` if it's configured and looks like a url
      return [pushRepo];
    } else if (!(await this.hasUpstreamBranch())) {
      // Start tracking upstream branch (`pushRepo` is a name if set)
      return ['--set-upstream', pushRepo || 'origin', await this.getBranchName()];
    } else if (pushRepo && !invalidPushRepoRe.test(pushRepo)) {
      return [pushRepo];
    } else {
      return [];
    }
  }

  stage(file) {
    if (!file || !file.length) return noop;
    const files = castArray(file);
    return this.exec(['git', 'add', ...files]).catch(err => {
      this.log.warn(`Could not stage ${files}`);
      this.debug(err);
    });
  }

  stageDir({ baseDir = '.' } = {}) {
    const { addUntrackedFiles } = this.options;
    return this.exec(['git', 'add', baseDir, addUntrackedFiles ? '--all' : '--update']);
  }

  reset(file) {
    const files = castArray(file);
    return this.exec(['git', 'checkout', 'HEAD', '--', ...files]).catch(err => {
      this.log.warn(`Could not reset ${files}`);
      this.debug(err);
    });
  }

  status() {
    return this.exec('git status --short --untracked-files=no', { options }).catch(() => null);
  }

  commit({ message = this.options.commitMessage, args = this.options.commitArgs } = {}) {
    const msg = format(message, this.config.getContext());
    const commitMessageArgs = msg ? ['--message', msg] : [];
    return this.exec(['git', 'commit', ...commitMessageArgs, ...fixArgs(args)]).then(
      () => this.setContext({ isCommitted: true }),
      err => {
        this.debug(err);
        if (/nothing (added )?to commit/.test(err) || /nichts zu committen/.test(err)) {
          this.log.warn('No changes to commit. The latest commit will be tagged.');
        } else {
          throw new Error(err);
        }
      }
    );
  }

  tag({ name, annotation = this.options.tagAnnotation, args = this.options.tagArgs } = {}) {
    const message = format(annotation, this.config.getContext());
    const tagName = name || this.config.getContext('tagName');
    return this.exec(['git', 'tag', '--annotate', '--message', message, ...fixArgs(args), tagName])
      .then(() => this.setContext({ isTagged: true }))
      .catch(err => {
        const { latestTag, tagName } = this.config.getContext();
        if (/tag '.+' already exists/.test(err) && latestTag === tagName) {
          this.log.warn(`Tag "${tagName}" already exists`);
        } else {
          throw err;
        }
      });
  }

  async push({ args = this.options.pushArgs } = {}) {
    const { pushRepo } = this.options;
    const upstreamArgs = await this.getUpstreamArgs(pushRepo);
    try {
      const push = await this.exec(['git', 'push', ...fixArgs(args), ...upstreamArgs]);
      this.disableRollback();
      return push;
    } catch (error) {
      if (this.config.getContext('isReleased')) {
        this.disableRollback();
        this.log.error(error.message || error);
        this.log.warn('The package might have been released, but git push failed.');
        return;
      }

      try {
        await this.rollbackTagPush();
      } catch (tagError) {
        this.log.warn(`An error was encountered when trying to rollback the tag on the remote: ${tagError.message}`);
      }

      throw error;
    }
  }

  async rollbackTagPush() {
    const { isTagged } = this.getContext();
    if (isTagged) {
      const { tagName } = this.config.getContext();
      this.log.info(`Rolling back remote tag push ${tagName}`);
      await this.exec(`git push origin --delete ${tagName}`);
    }
  }

  afterRelease() {
    this.disableRollback();
  }
}

export default Git;
```

## File: `lib/plugin/git/prompts.js`
```javascript
import { format, truncateLines, fixArgs } from '../../util.js';

export default {
  commit: {
    type: 'confirm',
    message: context => {
      if (fixArgs(context.git.commitArgs).includes('--amend')) return 'Amend commit?';
      return `Commit (${truncateLines(format(context.git.commitMessage, context), 1, ' [...]')})?`;
    },
    default: true
  },
  tag: {
    type: 'confirm',
    message: context => `Tag (${format(context.tagName, context)})?`,
    default: true
  },
  push: {
    type: 'confirm',
    message: () => 'Push?',
    default: true
  }
};
```

## File: `lib/plugin/github/GitHub.js`
```javascript
import { createReadStream, statSync } from 'node:fs';
import path from 'node:path';
import open from 'open';
import { Octokit } from '@octokit/rest';
import { glob } from 'tinyglobby';
import mime from 'mime-types';
import retry from 'async-retry';
import newGithubReleaseUrl from 'new-github-release-url';
import { ProxyAgent } from 'proxy-agent';
import { format, parseVersion, readJSON, e, castArray } from '../../util.js';
import Release from '../GitRelease.js';
import prompts from './prompts.js';
import { getCommitsFromChangelog, getResolvedIssuesFromChangelog, searchQueries } from './util.js';

/**
 * @typedef {import('@octokit/rest').RestEndpointMethodTypes['repos']['createRelease']['parameters']} CreateReleaseOptions
 */

const pkg = readJSON(new URL('../../../package.json', import.meta.url));

const docs = 'https://git.io/release-it-github';

const RETRY_CODES = [408, 413, 429, 500, 502, 503, 504, 521, 522, 524];

const DEFAULT_RETRY_MIN_TIMEOUT = 1000;

const parseErrormsg = err => {
  let msg = err;
  if (err instanceof Error) {
    const { status, message } = err;
    const headers = err.response ? err.response.headers : {};
    msg = `${headers?.status || status} (${message})`;
  }
  return msg;
};

const truncateBody = body => {
  // https://github.com/release-it/release-it/issues/965
  if (body && body.length >= 124000) return body.substring(0, 124000) + '...';
  return body;
};

class GitHub extends Release {
  constructor(...args) {
    super(...args);
    this.registerPrompts(prompts);
  }

  async init() {
    await super.init();

    const { skipChecks, tokenRef, web, update, assets } = this.options;

    if (!this.token || web) {
      if (!web) {
        this.log.warn(`Environment variable "${tokenRef}" is required for automated GitHub Releases.`);
        this.log.warn('Falling back to web-based GitHub Release.');
      }
      this.setContext({ isWeb: true });
      return;
    }

    if (web && assets) {
      this.log.warn('Assets are not included in web-based releases.');
    }

    if (!skipChecks) {
      // If we're running on GitHub Actions, we can skip the authentication and
      // collaborator checks. Ref: https://bit.ly/2vsyRzu
      if (process.env.GITHUB_ACTIONS) {
        this.setContext({ username: process.env.GITHUB_ACTOR });
      } else {
        if (!(await this.isAuthenticated())) {
          throw e(`Could not authenticate with GitHub using environment variable "${tokenRef}".`, docs);
        }

        if (!(await this.isCollaborator())) {
          const { repository } = this.getContext('repo');
          const { username } = this.getContext();
          throw e(`User ${username} is not a collaborator for ${repository}.`, docs);
        }
      }
    }

    if (update) {
      const { latestTag } = this.config.getContext();
      try {
        const { id, upload_url, tag_name } = await this.getLatestRelease();
        if (latestTag === tag_name) {
          this.setContext({ isUpdate: true, isReleased: true, releaseId: id, upload_url });
        } else {
          this.setContext({ isUpdate: false });
        }
      } catch (error) {
        this.setContext({ isUpdate: false });
      }
      if (!this.getContext('isUpdate')) {
        this.log.warn(`GitHub release for tag ${latestTag} was not found. Creating new release.`);
      }
    }
  }

  async isAuthenticated() {
    if (this.config.isDryRun) return true;
    try {
      this.log.verbose('octokit users#getAuthenticated');
      const { data } = await this.client.users.getAuthenticated();
      this.setContext({ username: data.login });
      return true;
    } catch (err) {
      this.debug(err);
      return false;
    }
  }

  async isCollaborator() {
    if (this.config.isDryRun) return true;
    const { owner, project: repo } = this.getContext('repo');
    const { username } = this.getContext();
    try {
      const options = { owner, repo, username };
      this.log.verbose(`octokit repos#checkCollaborator (${username})`);
      await this.client.repos.checkCollaborator(options);
      return true;
    } catch (err) {
      this.debug(err);
      return false;
    }
  }

  async release() {
    const { assets } = this.options;
    const { isWeb, isUpdate } = this.getContext();
    const { isCI } = this.config;

    const type = isUpdate ? 'update' : 'create';
    const publishMethod = `${type}Release`;

    if (isWeb) {
      const task = () => this.createWebRelease();
      return this.step({ task, label: 'Generating link to GitHub Release web interface', prompt: 'release' });
    } else if (isCI) {
      await this.step({ task: () => this[publishMethod](), label: `GitHub ${type} release` });
      await this.step({ enabled: assets, task: () => this.uploadAssets(), label: 'GitHub upload assets' });
      return this.step({
        task: () => (isUpdate ? Promise.resolve() : this.commentOnResolvedItems()),
        label: 'GitHub comment on resolved items'
      });
    } else {
      const release = async () => {
        await this[publishMethod]();
        await this.uploadAssets();
        return isUpdate ? Promise.resolve(true) : this.commentOnResolvedItems();
      };
      return this.step({ task: release, label: `GitHub ${type} release`, prompt: 'release' });
    }
  }

  handleError(err, bail) {
    const message = parseErrormsg(err);
    const githubError = new Error(message);
    this.log.verbose(err.errors);
    this.debug(err);
    if (!RETRY_CODES.includes(err.status)) {
      return bail(githubError);
    }
    throw githubError;
  }

  get client() {
    if (this._client) return this._client;
    const { proxy, timeout } = this.options;
    const repo = this.getContext('repo');
    const host = this.options.host || repo.host;
    const isGitHub = host === 'github.com';
    const baseUrl = `https://${isGitHub ? 'api.github.com' : host}${isGitHub ? '' : '/api/v3'}`;
    const options = {
      baseUrl,
      auth: `token ${this.token}`,
      userAgent: `release-it/${pkg.version}`,
      log: this.config.isDebug ? console : {},
      request: {
        timeout
      }
    };

    if (proxy) {
      options.request.agent = new ProxyAgent(proxy);
    }

    const client = new Octokit(options);

    this._client = client;
    return client;
  }

  async getLatestRelease() {
    const { owner, project: repo } = this.getContext('repo');
    try {
      const options = { owner, repo };
      this.debug(options);
      const response = await this.client.repos.listReleases({ owner, repo, per_page: 1, page: 1 });
      this.debug(response.data[0]);
      return response.data[0];
    } catch (err) {
      return this.handleError(err, () => {});
    }
  }

  async getOctokitReleaseOptions(options = {}) {
    const { owner, project: repo } = this.getContext('repo');
    const {
      releaseName,
      draft = false,
      preRelease = false,
      autoGenerate = false,
      makeLatest = true,
      discussionCategoryName = undefined
    } = this.options;
    const { tagName } = this.config.getContext();
    const { version, releaseNotes, isUpdate } = this.getContext();
    const { isPreRelease } = parseVersion(version);
    const name = format(releaseName, this.config.getContext());
    const releaseNotesObject = this.options.releaseNotes;

    const body = autoGenerate
      ? isUpdate
        ? null
        : ''
      : truncateBody(releaseNotesObject?.commit ? await this.renderReleaseNotes(releaseNotesObject) : releaseNotes);

    /**
     * @type {CreateReleaseOptions}
     */
    const contextOptions = {
      owner,
      make_latest: makeLatest.toString(),
      repo,
      tag_name: tagName,
      name,
      body,
      draft,
      prerelease: isPreRelease || preRelease,
      generate_release_notes: autoGenerate,
      discussion_category_name: discussionCategoryName
    };
    return Object.assign(options, contextOptions);
  }

  retry(fn) {
    const { retryMinTimeout } = this.options;
    return retry(fn, {
      retries: 2,
      minTimeout: typeof retryMinTimeout === 'number' ? retryMinTimeout : DEFAULT_RETRY_MIN_TIMEOUT
    });
  }

  async createRelease() {
    const options = await this.getOctokitReleaseOptions();
    const { isDryRun } = this.config;

    this.log.exec(`octokit repos.createRelease "${options.name}" (${options.tag_name})`, { isDryRun });

    if (isDryRun) {
      this.setContext({ isReleased: true, releaseUrl: this.getReleaseUrlFallback(options.tag_name) });
      return true;
    }

    return this.retry(async bail => {
      try {
        this.debug(options);
        const response = await this.client.repos.createRelease(options);
        this.debug(response.data);
        const { html_url, upload_url, id, discussion_url } = response.data;
        this.setContext({
          isReleased: true,
          releaseId: id,
          releaseUrl: html_url,
          upload_url,
          discussionUrl: discussion_url
        });
        this.config.setContext({
          isReleased: true,
          releaseId: id,
          releaseUrl: html_url,
          upload_url,
          discussionUrl: discussion_url
        });
        this.log.verbose(`octokit repos.createRelease: done (${response.headers.location})`);
        return response.data;
      } catch (err) {
        return this.handleError(err, bail);
      }
    });
  }

  uploadAsset(filePath) {
    const url = this.getContext('upload_url');
    const name = path.basename(filePath);
    const contentType = mime.contentType(name) || 'application/octet-stream';
    const contentLength = statSync(filePath).size;

    return this.retry(async bail => {
      try {
        const options = {
          url,
          data: createReadStream(filePath),
          name,
          headers: {
            'content-type': contentType,
            'content-length': contentLength
          }
        };
        this.debug(options);
        const response = await this.client.repos.uploadReleaseAsset(options);
        this.debug(response.data);
        this.log.verbose(`octokit repos.uploadReleaseAsset: done (${response.data.browser_download_url})`);
        return response.data;
      } catch (err) {
        return this.handleError(err, bail);
      }
    });
  }

  uploadAssets() {
    const { assets } = this.options;
    const { isReleased } = this.getContext();
    const context = this.config.getContext();
    const { isDryRun } = this.config;

    const patterns = castArray(assets).map(pattern => format(pattern, context));

    this.log.exec('octokit repos.uploadReleaseAssets', patterns, { isDryRun });

    if (!assets || !isReleased) {
      return true;
    }

    return glob(patterns).then(files => {
      if (!files.length) {
        this.log.warn(`octokit repos.uploadReleaseAssets: did not find "${assets}" relative to ${process.cwd()}`);
      }

      if (isDryRun) return Promise.resolve();

      return Promise.all(files.map(filePath => this.uploadAsset(filePath)));
    });
  }

  getReleaseUrlFallback(tagName) {
    const { host, repository } = this.getContext('repo');
    return `https://${host}/${repository}/releases/tag/${tagName}`;
  }

  async generateWebUrl() {
    const repo = this.getContext('repo');
    const host = this.options.host || repo.host;
    const isGitHub = host === 'github.com';
    const options = await this.getOctokitReleaseOptions();
    const url = newGithubReleaseUrl({
      user: options.owner,
      repo: options.repo,
      tag: options.tag_name,
      isPrerelease: options.prerelease,
      title: options.name,
      body: options.body
    });
    return isGitHub ? url : url.replace('github.com', host);
  }

  async createWebRelease() {
    const { isCI } = this.config;
    const { tagName } = this.config.getContext();
    const url = await this.generateWebUrl();
    if (isCI) {
      this.setContext({ isReleased: true, releaseUrl: url });
    } else {
      const isWindows = process.platform === 'win32';
      if (isWindows) this.log.info(`Opening ${url}`);
      await open(url, { wait: isWindows });
      this.setContext({ isReleased: true, releaseUrl: this.getReleaseUrlFallback(tagName) });
    }
  }

  async updateRelease() {
    const { isDryRun } = this.config;
    const release_id = this.getContext('releaseId');
    const options = await this.getOctokitReleaseOptions({ release_id });

    this.log.exec(`octokit repos.updateRelease (${options.tag_name})`, { isDryRun });

    if (isDryRun) return true;

    return this.retry(async bail => {
      try {
        this.debug(options);
        const response = await this.client.repos.updateRelease(options);
        this.setContext({ releaseUrl: response.data.html_url });
        this.debug(response.data);
        this.log.verbose(`octokit repos.updateRelease: done (${response.headers.location})`);
        return true;
      } catch (err) {
        return this.handleError(err, bail);
      }
    });
  }

  async commentOnResolvedItems() {
    const { isDryRun } = this.config;
    const { host, owner, project: repo } = this.getContext('repo');
    const changelog = this.config.getContext('changelog');
    const { comments } = this.options;
    const { submit, issue, pr } = comments ?? {};
    const context = this.getContext();

    if (!submit || !changelog) return true;

    const shas = getCommitsFromChangelog(changelog);
    const searchResults = await Promise.all(searchQueries(this.client, owner, repo, shas));
    const mergedPullRequests = searchResults.flatMap(items => items.map(item => ({ type: 'pr', number: item.number })));

    const hostURL = 'https://' + (this.options.host || host);
    const resolvedIssues = getResolvedIssuesFromChangelog(hostURL, owner, repo, changelog);

    for (const item of [...resolvedIssues, ...mergedPullRequests]) {
      const { type, number } = item;
      const comment = format(format(type === 'pr' ? pr : issue, context), context);
      const url = `${hostURL}/${owner}/${repo}/${type === 'pr' ? 'pull' : 'issues'}/${number}`;

      if (isDryRun) {
        this.log.exec(`octokit issues.createComment (${url})`, { isDryRun });
        return Promise.resolve();
      }

      try {
        await this.client.issues.createComment({ owner, repo, issue_number: number, body: comment });
        this.log.log(`● Commented on ${url}`);
      } catch (error) {
        this.log.log(`✕ Failed to comment on ${url}`);
      }
    }
  }

  async getCommits() {
    const { owner, project: repo } = this.getContext('repo');
    const { latestTag } = this.config.getContext();
    this.debug({ owner, repo, base: latestTag, head: 'HEAD' });
    const { data } = await this.client.repos.compareCommits({ owner, repo, base: latestTag, head: 'HEAD' });
    return data.commits;
  }

  async renderReleaseNotes(releaseNotes) {
    const { commit: template, excludeMatches = [] } = releaseNotes;
    const commits = await this.getCommits();

    if (this.options.commit || !this.config.isIncrement) commits.pop();

    return commits
      .map(commit => {
        commit.commit.subject = commit.commit.message.split('\n')[0];
        const partial = template.replace(/(?<!\$)\{((?:[^{}]|\${[^}]+})+)\}/g, (_, block) => {
          const rendered = format(block, commit);
          return excludeMatches.some(match => rendered.includes(match)) ? '' : rendered;
        });
        return format(partial, commit);
      })
      .join('\n');
  }
}

export default GitHub;
```

## File: `lib/plugin/github/prompts.js`
```javascript
import { format } from '../../util.js';

const message = context => {
  const { isPreRelease, github } = context;
  const { releaseName, update } = github;
  const name = format(releaseName, context);
  return `${update ? 'Update' : 'Create a'} ${isPreRelease ? 'pre-' : ''}release on GitHub (${name})?`;
};

export default {
  release: {
    type: 'confirm',
    message,
    default: true
  }
};
```

## File: `lib/plugin/github/util.js`
```javascript
// Totally much borrowed from https://github.com/semantic-release/github/blob/master/lib/success.js
import issueParser from 'issue-parser';

/** @internal */
export const getSearchQueries = (base, commits, separator = '+') => {
  const encodedSeparator = encodeURIComponent(separator);

  return commits.reduce((searches, commit) => {
    const lastSearch = searches[searches.length - 1];
    if (lastSearch && encodeURIComponent(lastSearch).length + commit.length <= 256 - encodedSeparator.length) {
      searches[searches.length - 1] = `${lastSearch}${separator}${commit}`;
    } else {
      searches.push(`${base}${separator}${commit}`);
    }

    return searches;
  }, []);
};

export const searchQueries = (client, owner, repo, shas) =>
  getSearchQueries(`repo:${owner}/${repo}+type:pr+is:merged`, shas).map(
    async q => (await client.search.issuesAndPullRequests({ q, advanced_search: true })).data.items
  );

export const getCommitsFromChangelog = changelog => {
  const regex = /\(([a-f0-9]{7,})\)/i;
  return changelog.split('\n').flatMap(message => {
    const match = message.match(regex);
    if (match) return match[1];
    return [];
  });
};

export const getResolvedIssuesFromChangelog = (host, owner, repo, changelog) => {
  const parser = issueParser('github', { hosts: [host] });
  return changelog
    .split('\n')
    .map(parser)
    .flatMap(parsed => parsed.actions.close)
    .filter(action => !action.slug || action.slug === `${owner}/${repo}`)
    .map(action => ({ type: 'issue', number: parseInt(action.issue, 10) }));
};
```

## File: `lib/plugin/gitlab/GitLab.js`
```javascript
import path from 'node:path';
import fs from 'node:fs'; // import fs here so it can be stubbed in tests
import { readFile } from 'node:fs/promises';
import { glob } from 'tinyglobby';
import { Agent } from 'undici';
import Release from '../GitRelease.js';
import { format, e, castArray } from '../../util.js';
import prompts from './prompts.js';

const docs = 'https://git.io/release-it-gitlab';

const noop = Promise.resolve();

class GitLab extends Release {
  constructor(...args) {
    super(...args);
    this.registerPrompts(prompts);
    this.assets = [];
    const { secure } = this.options;
    const certificateAuthorityFileRef = this.options.certificateAuthorityFileRef || 'CI_SERVER_TLS_CA_FILE';
    const certificateAuthorityFile =
      this.options.certificateAuthorityFile || process.env[certificateAuthorityFileRef] || null;
    this.certificateAuthorityOption = {};

    const needsCustomAgent = Boolean(secure === false || certificateAuthorityFile);

    if (needsCustomAgent) {
      this.certificateAuthorityOption.dispatcher = new Agent({
        connect: {
          rejectUnauthorized: secure,
          ca: certificateAuthorityFile ? fs.readFileSync(certificateAuthorityFile) : undefined
        }
      });
    }
  }

  async init() {
    await super.init();

    const { skipChecks, tokenRef, tokenHeader } = this.options;
    const { repo } = this.getContext();
    const hasJobToken = (tokenHeader || '').toLowerCase() === 'job-token';
    const origin = this.options.origin || `https://${repo.host}`;
    this.setContext({
      id: encodeURIComponent(repo.repository),
      origin,
      baseUrl: `${origin}/api/v4`
    });

    if (skipChecks) return;

    if (!this.token) {
      throw e(`Environment variable "${tokenRef}" is required for GitLab releases.`, docs);
    }

    if (!hasJobToken) {
      if (!(await this.isAuthenticated())) {
        throw e(`Could not authenticate with GitLab using environment variable "${tokenRef}".`, docs);
      }
      if (!(await this.isCollaborator())) {
        const { user, repo } = this.getContext();
        throw e(`User ${user.username} is not a collaborator for ${repo.repository}.`, docs);
      }
    }
  }

  async isAuthenticated() {
    if (this.config.isDryRun) return true;
    const endpoint = `user`;
    try {
      const { id, username } = await this.request(endpoint, { method: 'GET' });
      this.setContext({ user: { id, username } });
      return true;
    } catch (err) {
      this.debug(err);
      return false;
    }
  }

  async isCollaborator() {
    if (this.config.isDryRun) return true;
    const { id, user } = this.getContext();
    const endpoint = `projects/${id}/members/all/${user.id}`;
    try {
      const { access_level } = await this.request(endpoint, { method: 'GET' });
      return access_level && access_level >= 30;
    } catch (err) {
      this.debug(err);
      return false;
    }
  }

  async beforeRelease() {
    await super.beforeRelease();
    await this.checkReleaseMilestones();
  }

  async checkReleaseMilestones() {
    if (this.options.skipChecks) return;

    const releaseMilestones = this.getReleaseMilestones();
    if (releaseMilestones.length < 1) {
      return;
    }

    this.log.exec(`gitlab releases#checkReleaseMilestones`);

    const { id } = this.getContext();
    const endpoint = `projects/${id}/milestones`;
    const requests = releaseMilestones.map(milestone => {
      const options = {
        method: 'GET',
        searchParams: {
          title: milestone,
          include_parent_milestones: true
        }
      };
      return this.request(endpoint, options).then(response => {
        if (!Array.isArray(response)) {
          const { baseUrl } = this.getContext();
          throw new Error(
            `Unexpected response from ${baseUrl}/${endpoint}. Expected an array but got: ${JSON.stringify(response)}`
          );
        }
        if (response.length === 0) {
          const error = new Error(`Milestone '${milestone}' does not exist.`);
          this.log.warn(error.message);
          throw error;
        }
        this.log.verbose(`gitlab releases#checkReleaseMilestones: milestone '${milestone}' exists`);
      });
    });
    try {
      await Promise.allSettled(requests).then(results => {
        for (const result of results) {
          if (result.status === 'rejected') {
            throw e('Missing one or more milestones in GitLab. Creating a GitLab release will fail.', docs);
          }
        }
      });
    } catch (err) {
      this.debug(err);
      throw err;
    }
    this.log.verbose('gitlab releases#checkReleaseMilestones: done');
  }

  getReleaseMilestones() {
    const { milestones } = this.options;
    return (milestones || []).map(milestone => format(milestone, this.config.getContext()));
  }

  async release() {
    const glRelease = () => this.createRelease();
    const glUploadAssets = () => this.uploadAssets();

    if (this.config.isCI) {
      await this.step({ enabled: this.options.assets, task: glUploadAssets, label: 'GitLab upload assets' });
      return await this.step({ task: glRelease, label: 'GitLab release' });
    } else {
      const release = () => glUploadAssets().then(() => glRelease());
      return await this.step({ task: release, label: 'GitLab release', prompt: 'release' });
    }
  }

  async request(endpoint, options) {
    const { baseUrl } = this.getContext();
    this.debug(Object.assign({ url: `${baseUrl}/${endpoint}` }, options));
    const method = (options.method || 'POST').toLowerCase();
    const { tokenHeader } = this.options;
    const url = `${baseUrl}/${endpoint}${options.searchParams ? `?${new URLSearchParams(options.searchParams)}` : ''}`;
    const headers = {
      'user-agent': 'webpro/release-it',
      [tokenHeader]: this.token
    };
    // When using fetch() with FormData bodies, we should not set the Content-Type header.
    // See: https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest_API/Using_FormData_Objects#sending_files_using_a_formdata_object
    if (!(options.body instanceof FormData)) {
      headers['Content-Type'] = typeof options.json !== 'undefined' ? 'application/json' : 'text/plain';
    }
    const requestOptions = {
      method,
      headers,
      ...this.certificateAuthorityOption
    };

    try {
      const response = await fetch(
        url,
        options.json || options.body
          ? {
              ...requestOptions,
              body: options.json ? JSON.stringify(options.json) : options.body
            }
          : requestOptions
      );

      if (!response.ok) {
        const body = await response.json();
        throw new Error(body.error);
      }

      const body = await response.json();
      this.debug(body);
      return body;
    } catch (err) {
      this.debug(err);
      throw err;
    }
  }

  async createRelease() {
    const { releaseName } = this.options;
    const { tagName, branchName, git: { tagAnnotation } = {} } = this.config.getContext();
    const { id, releaseNotes, repo, origin } = this.getContext();
    const { isDryRun } = this.config;
    const name = format(releaseName, this.config.getContext());
    const tagMessage = format(tagAnnotation, this.config.getContext());
    const description = releaseNotes || '-';
    const releaseUrl = `${origin}/${repo.repository}/-/releases/${tagName}`;
    const releaseMilestones = this.getReleaseMilestones();

    this.log.exec(`gitlab releases#createRelease "${name}" (${tagName})`, { isDryRun });

    if (isDryRun) {
      this.setContext({ isReleased: true, releaseUrl });
      return true;
    }

    const endpoint = `projects/${id}/releases`;
    const options = {
      json: {
        name,
        ref: branchName,
        tag_name: tagName,
        tag_message: tagMessage,
        description
      }
    };

    if (this.assets.length) {
      options.json.assets = {
        links: this.assets
      };
    }

    if (releaseMilestones.length) {
      options.json.milestones = releaseMilestones;
    }

    try {
      const body = await this.request(endpoint, options);
      const releaseUrlSelf = body._links?.self ?? releaseUrl;
      this.log.verbose('gitlab releases#createRelease: done');
      this.setContext({ isReleased: true, releaseUrl: releaseUrlSelf });
      this.config.setContext({ isReleased: true, releaseUrl: releaseUrlSelf });
      return true;
    } catch (err) {
      this.debug(err);
      throw err;
    }
  }

  async uploadAsset(filePath) {
    const name = path.basename(filePath);
    const { useIdsForUrls, useGenericPackageRepositoryForAssets, genericPackageRepositoryName } = this.options;
    const { id, origin, repo, version, baseUrl } = this.getContext();

    const endpoint = useGenericPackageRepositoryForAssets
      ? `projects/${id}/packages/generic/${genericPackageRepositoryName}/${version}/${name}`
      : `projects/${id}/uploads`;

    if (useGenericPackageRepositoryForAssets) {
      const options = {
        method: 'PUT',
        body: await readFile(filePath)
      };

      try {
        const body = await this.request(endpoint, options);
        if (!(body.message && body.message == '201 Created')) {
          throw new Error(`GitLab asset upload failed`);
        }
        this.log.verbose(`gitlab releases#uploadAsset: done (${endpoint})`);
        this.assets.push({
          name,
          url: `${baseUrl}/${endpoint}`
        });
      } catch (err) {
        this.debug(err);
        throw err;
      }
    } else {
      const body = new FormData();
      const rawData = await readFile(filePath);
      body.set('file', new Blob([rawData]), name);
      const options = { body };

      try {
        const body = await this.request(endpoint, options);
        this.log.verbose(`gitlab releases#uploadAsset: done (${body.url})`);
        this.assets.push({
          name,
          url: useIdsForUrls ? `${origin}${body.full_path}` : `${origin}/${repo.repository}${body.url}`
        });
      } catch (err) {
        this.debug(err);
        throw err;
      }
    }
  }

  uploadAssets() {
    const { assets } = this.options;
    const { isDryRun } = this.config;
    const context = this.config.getContext();

    const patterns = castArray(assets).map(pattern => format(pattern, context));

    this.log.exec('gitlab releases#uploadAssets', patterns, { isDryRun });

    if (!assets) {
      return noop;
    }

    return glob(patterns).then(files => {
      if (!files.length) {
        this.log.warn(`gitlab releases#uploadAssets: could not find "${assets}" relative to ${process.cwd()}`);
      }

      if (isDryRun) return Promise.resolve();

      return Promise.all(files.map(filePath => this.uploadAsset(filePath)));
    });
  }
}

export default GitLab;
```

## File: `lib/plugin/gitlab/prompts.js`
```javascript
import { format } from '../../util.js';

export default {
  release: {
    type: 'confirm',
    message: context => `Create a release on GitLab (${format(context.gitlab.releaseName, context)})?`,
    default: true
  }
};
```

## File: `lib/plugin/npm/npm.js`
```javascript
import path from 'node:path';
import semver from 'semver';
import urlJoin from 'url-join';
import Plugin from '../Plugin.js';
import { hasAccess, rejectAfter, parseVersion, readJSON, e, fixArgs, getNpmEnv } from '../../util.js';
import prompts from './prompts.js';

const docs = 'https://git.io/release-it-npm';

const getOptions = () => ({ write: false, env: getNpmEnv() });

const MANIFEST_PATH = './package.json';
const DEFAULT_TAG = 'latest';
const DEFAULT_TAG_PRERELEASE = 'next';
const NPM_BASE_URL = 'https://www.npmjs.com';
const NPM_PUBLIC_PATH = '/package';
const DEFAULT_TIMEOUT = 10;

class npm extends Plugin {
  static isEnabled(options) {
    return hasAccess(MANIFEST_PATH) && options !== false;
  }

  constructor(...args) {
    super(...args);
    this.registerPrompts(prompts);
  }

  async init() {
    const { name, version: latestVersion, private: isPrivate, publishConfig } = readJSON(path.resolve(MANIFEST_PATH));
    this.setContext({ name, latestVersion, private: isPrivate, publishConfig });
    this.config.setContext({ npm: { name } });

    const { publish, skipChecks } = this.options;

    const timeout = Number(this.options.timeout ?? DEFAULT_TIMEOUT) * 1000;

    if (publish === false || isPrivate) return;

    if (skipChecks) return;

    const validations = Promise.all([this.isRegistryUp(), this.isAuthenticated(), this.getLatestRegistryVersion()]);

    await Promise.race([validations, rejectAfter(timeout, e(`Timed out after ${timeout}ms.`, docs))]);

    const [isRegistryUp, isAuthenticated, latestVersionInRegistry] = await validations;

    if (!isRegistryUp) {
      throw e(`Unable to reach npm registry (timed out after ${timeout}ms).`, docs);
    }

    if (!isAuthenticated) {
      throw e('Not authenticated with npm. Please `npm login` and try again.', docs);
    }

    if (!(await this.isCollaborator())) {
      const { username } = this.getContext();
      throw e(`User ${username} is not a collaborator for ${name}.`, docs);
    }

    if (!latestVersionInRegistry) {
      this.log.warn('No version found in npm registry. Assuming new package.');
    } else {
      if (!semver.eq(latestVersion, latestVersionInRegistry)) {
        this.log.warn(
          `Latest version in registry (${latestVersionInRegistry}) does not match package.json (${latestVersion}).`
        );
      }
    }
  }

  getName() {
    return this.getContext('name');
  }

  getLatestVersion() {
    return this.options.ignoreVersion ? null : this.getContext('latestVersion');
  }

  async bump(version) {
    const tag = this.options.tag || (await this.resolveTag(version));
    this.setContext({ version, tag });

    if (!this.config.isIncrement) return false;

    const { versionArgs, allowSameVersion } = this.options;
    const args = [
      version,
      '--no-git-tag-version',
      '--workspaces=false',
      allowSameVersion && '--allow-same-version',
      ...fixArgs(versionArgs)
    ];
    const task = () => this.exec(`npm version ${args.filter(Boolean).join(' ')}`, { options: getOptions() });
    return this.spinner.show({ task, label: 'npm version' });
  }

  release() {
    if (this.options.publish === false) return false;
    if (this.getContext('private')) return false;
    const publish = () => this.publish({ otpCallback });
    const otpCallback =
      this.config.isCI && !this.config.isPromptOnlyVersion ? null : task => this.step({ prompt: 'otp', task });
    return this.step({ task: publish, label: 'npm publish', prompt: 'publish' });
  }

  isRegistryUp() {
    const registry = this.getRegistry();
    const registryArg = registry ? ` --registry ${registry}` : '';
    return this.exec(`npm ping${registryArg}`, { options: getOptions() }).then(
      () => true,
      err => {
        if (/code E40[04]|404.*(ping not found|No content for path)/.test(err)) {
          this.log.warn('Ignoring response from unsupported `npm ping` command.');
          return true;
        }
        return false;
      }
    );
  }

  isAuthenticated() {
    const registry = this.getRegistry();
    const registryArg = registry ? ` --registry ${registry}` : '';
    return this.exec(`npm whoami${registryArg}`, { options: getOptions() }).then(
      output => {
        const username = output ? output.trim() : null;
        this.setContext({ username });
        return true;
      },
      err => {
        this.debug(err);
        if (/code E40[04]/.test(err)) {
          this.log.warn('Ignoring response from unsupported `npm whoami` command.');
          return true;
        }
        return false;
      }
    );
  }

  async isCollaborator() {
    const registry = this.getRegistry();
    const registryArg = registry ? ` --registry ${registry}` : '';
    const name = this.getName();
    const { username } = this.getContext();
    if (username === undefined) return true;
    if (username === null) return false;

    try {
      let npmVersion = await this.exec('npm --version', { options: getOptions() });

      let accessCommand;
      if (semver.gt(npmVersion, '9.0.0')) {
        accessCommand = 'npm access list collaborators --json';
      } else {
        accessCommand = 'npm access ls-collaborators';
      }

      const output = await this.exec(`${accessCommand} ${name}${registryArg}`, { options: getOptions() });

      try {
        const collaborators = JSON.parse(output);
        const permissions = collaborators[username];
        return permissions && permissions.includes('write');
      } catch (err) {
        this.debug(err);
        return false;
      }
    } catch (err) {
      this.debug(err);
      if (/code E400/.test(err)) {
        this.log.warn('Ignoring response from unsupported `npm access` command.');
      } else {
        this.log.warn(`Unable to verify if user ${username} is a collaborator for ${name}.`);
      }
      return true;
    }
  }

  async getLatestRegistryVersion() {
    const registry = this.getRegistry();
    const registryArg = registry ? ` --registry ${registry}` : '';
    const name = this.getName();
    const latestVersion = this.getLatestVersion();
    const tag = await this.resolveTag(latestVersion);
    return this.exec(`npm show ${name}@${tag} version${registryArg}`, { options: getOptions() }).catch(() => null);
  }

  getRegistryDistTags() {
    return this.exec(`npm view ${this.getName()} dist-tags --json`, { options: getOptions() }).then(
      output => {
        try {
          return JSON.parse(output);
        } catch (err) {
          this.debug(err);
          return {};
        }
      },
      () => ({})
    );
  }

  async getRegistryPreReleaseTags() {
    const tags = await this.getRegistryDistTags();
    return Object.keys(tags).filter(tag => tag !== DEFAULT_TAG);
  }

  getPackageUrl() {
    const baseUrl = this.getRegistry() || NPM_BASE_URL;
    const publicPath = this.getPublicPath() || NPM_PUBLIC_PATH;
    return urlJoin(baseUrl, publicPath, this.getName());
  }

  getRegistry() {
    const { publishConfig } = this.getContext();
    const registries = publishConfig
      ? publishConfig.registry
        ? [publishConfig.registry]
        : Object.keys(publishConfig)
            .filter(key => key.endsWith('registry'))
            .map(key => publishConfig[key])
      : [];
    return registries[0];
  }

  getPublicPath() {
    const { publishConfig } = this.getContext();
    return (publishConfig && publishConfig.publicPath) ?? '';
  }

  async guessPreReleaseTag() {
    const distTags = await this.getRegistryDistTags();
    const latestVersion = this.getLatestVersion();
    const match = Object.entries(distTags).find(
      ([tag, version]) => tag !== DEFAULT_TAG && version === latestVersion
    );
    if (match) return match[0];

    const [tag] = Object.keys(distTags).filter(tag => tag !== DEFAULT_TAG);
    if (tag) return tag;

    this.log.warn(`Unable to get pre-release tag(s) from npm registry. Using "${DEFAULT_TAG_PRERELEASE}".`);
    return DEFAULT_TAG_PRERELEASE;
  }

  async resolveTag(version) {
    const { tag } = this.options;
    const { isPreRelease, preReleaseId } = parseVersion(version);
    if (!isPreRelease) {
      return DEFAULT_TAG;
    } else {
      return tag || preReleaseId || (await this.guessPreReleaseTag());
    }
  }

  async publish({ otp = this.options.otp, otpCallback } = {}) {
    const publishPackageManager = this.options.publishPackageManager || 'npm';
    const { publishPath = '.', publishArgs } = this.options;
    const { private: isPrivate, tag = DEFAULT_TAG } = this.getContext();
    const otpArgs = otp ? ['--otp', otp] : [];
    const dryRunArg = this.config.isDryRun ? '--dry-run' : '';
    const registry = this.getRegistry();
    const registryArg = registry ? `--registry ${registry}` : '';
    if (isPrivate) {
      this.log.warn('Skip publish: package is private.');
      return false;
    }
    const args = [
      publishPath,
      '--tag',
      tag,
      publishPackageManager === 'npm' && '--workspaces=false',
      ...otpArgs,
      dryRunArg,
      registryArg,
      ...fixArgs(publishArgs)
    ].filter(Boolean);
    const isInteractive = !this.config.isCI;
    return this.exec([publishPackageManager, 'publish', ...args], {
      options: { ...getOptions(), interactive: isInteractive }
    })
      .then(() => {
        this.setContext({ isReleased: true });
        this.config.setContext({ isReleased: true });
      })
      .catch(err => {
        this.debug(err);
        if (this.config.isDryRun && /publish over the previously published version/.test(err)) {
          return Promise.resolve();
        }

        if (/one-time pass/.test(err)) {
          if (otp != null) {
            this.log.warn('The provided OTP is incorrect or has expired.');
          }
          if (otpCallback) {
            return otpCallback(otp => this.publish({ otp, otpCallback }));
          }
        }
        throw err;
      });
  }

  afterRelease() {
    const { isReleased } = this.getContext();
    if (isReleased) {
      this.log.log(`🔗 ${this.getPackageUrl()}`);
    }
  }
}

export default npm;
```

## File: `lib/plugin/npm/prompts.js`
```javascript
export default {
  publish: {
    type: 'confirm',
    message: context =>
      `Publish ${context.npm.name}${context.npm.tag === 'latest' ? '' : `@${context.npm.tag}`} to npm?`,
    default: true
  },
  otp: {
    type: 'input',
    message: () => `Please enter OTP for npm:`
  }
};
```

## File: `lib/plugin/version/Version.js`
```javascript
import { styleText } from 'node:util';
import semver from 'semver';
import Plugin from '../Plugin.js';

const RELEASE_TYPES = ['patch', 'minor', 'major'];
const PRERELEASE_TYPES = ['prepatch', 'preminor', 'premajor'];
const CONTINUATION_TYPES = ['prerelease', 'pre'];
const ALL_RELEASE_TYPES = [...RELEASE_TYPES, ...PRERELEASE_TYPES, ...CONTINUATION_TYPES];

const CHOICES = {
  latestIsPreRelease: [CONTINUATION_TYPES[0], ...RELEASE_TYPES],
  preRelease: PRERELEASE_TYPES,
  default: [...RELEASE_TYPES, ...PRERELEASE_TYPES]
};

const EXIT = Symbol('exit');

const getIncrementChoices = context => {
  const { latestIsPreRelease, isPreRelease, preReleaseId, preReleaseBase } = context.version;
  const types = latestIsPreRelease ? CHOICES.latestIsPreRelease : isPreRelease ? CHOICES.preRelease : CHOICES.default;
  const choices = types.map(increment => ({
    name: `${increment} (${semver.inc(context.latestVersion, increment, preReleaseId, preReleaseBase)})`,
    value: increment
  }));
  const otherChoice = {
    name: 'Other, please specify...',
    value: null
  };
  const exitChoice = {
    name: 'Exit',
    value: EXIT
  };
  return [...choices, otherChoice, exitChoice];
};

const versionTransformer = context => input =>
  semver.valid(input)
    ? semver.gt(input, context.latestVersion)
      ? styleText('green', input)
      : styleText('red', input)
    : styleText(['red', 'bold'], input);

const prompts = {
  incrementList: {
    type: 'list',
    message: () => 'Select increment (next version):',
    choices: context => getIncrementChoices(context),
    pageSize: 9
  },
  version: {
    type: 'input',
    message: () => `Please enter a valid version:`,
    transformer: context => versionTransformer(context),
    validate: input => !!semver.valid(input) || 'The version must follow the semver standard.'
  }
};

class Version extends Plugin {
  constructor(...args) {
    super(...args);
    this.registerPrompts(prompts);
  }

  getIncrement(options) {
    return options.increment;
  }

  getIncrementedVersionCI(options) {
    return this.incrementVersion(options);
  }

  async getIncrementedVersion(options) {
    const { isCI } = this.config;
    const version = this.incrementVersion(options);
    return version || (isCI ? null : await this.promptIncrementVersion(options));
  }

  promptIncrementVersion(options) {
    return new Promise(resolve => {
      this.step({
        prompt: 'incrementList',
        task: increment => {
          if (increment === EXIT) process.exit(0);
          return increment
            ? resolve(this.incrementVersion(Object.assign({}, options, { increment })))
            : this.step({ prompt: 'version', task: resolve });
        }
      });
    });
  }

  isPreRelease(version) {
    return Boolean(semver.prerelease(version));
  }

  isValid(version) {
    return Boolean(semver.valid(version));
  }

  incrementVersion({ latestVersion, increment, isPreRelease, preReleaseId, preReleaseBase }) {
    if (increment === false) return latestVersion;

    const latestIsPreRelease = this.isPreRelease(latestVersion);
    const isValidVersion = this.isValid(increment);

    if (latestVersion) {
      this.setContext({ latestIsPreRelease });
    }

    if (isValidVersion && semver.gte(increment, latestVersion)) {
      return increment;
    }

    if (isPreRelease && !increment && latestIsPreRelease) {
      return semver.inc(latestVersion, 'prerelease', preReleaseId, preReleaseBase);
    }

    if (this.config.isCI && !increment) {
      if (isPreRelease) {
        return semver.inc(latestVersion, 'prepatch', preReleaseId, preReleaseBase);
      } else {
        return semver.inc(latestVersion, 'patch');
      }
    }

    const normalizedType = RELEASE_TYPES.includes(increment) && isPreRelease ? `pre${increment}` : increment;
    if (ALL_RELEASE_TYPES.includes(normalizedType)) {
      return semver.inc(latestVersion, normalizedType, preReleaseId, preReleaseBase);
    }

    const coercedVersion = !isValidVersion && semver.coerce(increment);
    if (coercedVersion) {
      this.log.warn(`Coerced invalid semver version "${increment}" into "${coercedVersion}".`);
      return coercedVersion.toString();
    }
  }
}

export default Version;
```

## File: `schema/git.json`
```json
{
  "$schema": "http://json-schema.org/draft-07/schema",
  "$id": "release-it#git",
  "title": "JSON schema for release-it Git configuration",
  "type": "object",
  "additionalItems": false,
  "properties": {
    "changelog": {
      "type": "string",
      "default": "git log --pretty=format:\"* %s (%h)\" ${from}...${to}"
    },
    "requireCleanWorkingDir": {
      "type": "boolean",
      "default": true
    },
    "requireBranch": {
      "oneOf": [
        { "type": "boolean", "enum": [false] },
        { "type": "string" },
        { "type": "array", "items": { "type": "string" } }
      ],
      "default": false
    },
    "requireUpstream": {
      "type": "boolean",
      "default": true
    },
    "requireCommits": {
      "type": "boolean",
      "default": false
    },
    "requireCommitsFail": {
      "type": "boolean",
      "default": true
    },
    "commitsPath": {
      "type": "string",
      "default": ""
    },
    "addUntrackedFiles": {
      "type": "boolean",
      "default": false
    },
    "commit": {
      "type": "boolean",
      "default": true
    },
    "commitArgs": {
      "type": "array",
      "uniqueItems": true,
      "items": {
        "type": "string"
      },
      "default": []
    },
    "commitMessage": {
      "type": "string",
      "default": null
    },
    "tag": {
      "type": "boolean",
      "default": true
    },
    "tagExclude": {
      "type": "string",
      "default": null
    },
    "tagMatch": {
      "type": "string",
      "default": null
    },
    "getLatestTagFromAllRefs": {
      "type": "boolean",
      "default": false
    },
    "tagAnnotation": {
      "type": "string",
      "default": "Release ${version}"
    },
    "tagArgs": {
      "type": "array",
      "uniqueItems": true,
      "items": {
        "type": "string"
      },
      "default": []
    },
    "push": {
      "type": "boolean",
      "default": true
    },
    "pushArgs": {
      "type": "array",
      "uniqueItems": true,
      "items": {
        "type": "string"
      },
      "default": ["--follow-tags"]
    },
    "pushRepo": {
      "type": "string",
      "default": ""
    }
  }
}
```

## File: `schema/github.json`
```json
{
  "$schema": "http://json-schema.org/draft-07/schema",
  "$id": "release-it#github",
  "title": "JSON schema for release-it github configuration",
  "type": "object",
  "additionalItems": false,
  "properties": {
    "release": {
      "type": "boolean",
      "default": false
    },
    "releaseName": {
      "type": "string",
      "default": "Release ${version}"
    },
    "releaseNotes": {
      "anyOf": [
        { "type": ["string", "null"] },
        {
          "type": "object",
          "properties": {
            "commit": {
              "type": "string"
            },
            "excludeMatches": {
              "type": "array",
              "items": {
                "type": "string"
              },
              "default": []
            }
          }
        }
      ],
      "default": null
    },
    "autoGenerate": {
      "type": "boolean",
      "default": false
    },
    "makeLatest": {
      "anyOf": [{ "type": "boolean" }, { "const": "legacy" }],
      "default": true
    },
    "preRelease": {
      "type": "boolean",
      "default": false
    },
    "draft": {
      "type": "boolean",
      "default": false
    },
    "discussionCategoryName": {
      "$comment": "Create discussion of the specified category and link to the GitHub Release",
      "type": "string"
    },
    "tokenRef": {
      "type": "string",
      "default": "GITHUB_TOKEN"
    },
    "assets": {
      "default": null
    },
    "host": {
      "type": "string",
      "default": null
    },
    "timeout": {
      "type": "integer",
      "default": 0
    },
    "proxy": {
      "type": "string",
      "default": null
    },
    "skipChecks": {
      "type": "boolean",
      "default": false
    },
    "web": {
      "type": "boolean",
      "default": false
    },
    "comments": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "submit": {
          "type": "boolean",
          "default": false
        },
        "issue": {
          "type": "string",
          "default": ":rocket: _This issue has been resolved in v${version}. See [${releaseName}](${releaseUrl}) for release notes._"
        },
        "pr": {
          "type": "string",
          "default": ":rocket: _This pull request is included in v${version}. See [${releaseName}](${releaseUrl}) for release notes._"
        }
      }
    }
  }
}
```

## File: `schema/gitlab.json`
```json
{
  "$schema": "http://json-schema.org/draft-07/schema",
  "$id": "release-it#gitlab",
  "title": "JSON schema for release-it gitlab configuration",
  "type": "object",
  "additionalItems": false,
  "properties": {
    "release": {
      "type": "boolean",
      "default": false
    },
    "releaseName": {
      "type": "string",
      "default": "Release ${version}"
    },
    "releaseNotes": {
      "default": null
    },
    "autoGenerate": {
      "type": "boolean",
      "default": false
    },
    "preRelease": {
      "type": "boolean",
      "default": false
    },
    "draft": {
      "type": "boolean",
      "default": false
    },
    "milestones": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "default": []
    },
    "tokenRef": {
      "type": "string",
      "default": "GITLAB_TOKEN"
    },
    "tokenHeader": {
      "type": "string",
      "default": "Private-Token"
    },
    "certificateAuthorityFile": {
      "default": null
    },
    "certificateAuthorityFileRef": {
      "type": "string",
      "default": "CI_SERVER_TLS_CA_FILE"
    },
    "secure": {
      "default": false
    },
    "assets": {
      "default": null
    },
    "useIdsForUrls": {
      "type": "boolean",
      "default": false
    },
    "useGenericPackageRepositoryForAssets": {
      "type": "boolean",
      "default": false
    },
    "genericPackageRepositoryName": {
       "type": "string",
       "default": "release-it"
    },
    "origin": {
      "type": "string",
      "default": null
    },
    "skipChecks": {
      "type": "boolean",
      "default": false
    }
  }
}
```

## File: `schema/npm.json`
```json
{
  "$schema": "http://json-schema.org/draft-07/schema",
  "$id": "release-it#npm",
  "title": "JSON schema for release-it npm configuration",
  "type": "object",
  "additionalItems": false,
  "properties": {
    "publish": {
      "type": "boolean",
      "default": true
    },
    "publishPath": {
      "type": "string",
      "default": "."
    },
    "publishArgs": {
      "type": "array",
      "uniqueItems": true,
      "items": {
        "type": "string"
      },
      "default": []
    },
    "publishPackageManager": {
      "type": "string",
      "default": "npm"
    },
    "tag": {
      "type": "string",
      "default": null
    },
    "otp": {
      "type": "string",
      "default": null
    },
    "ignoreVersion": {
      "type": "boolean",
      "default": false
    },
    "allowSameVersion": {
      "type": "boolean",
      "default": false
    },
    "versionArgs": {
      "type": "array",
      "uniqueItems": true,
      "items": {
        "type": "string"
      },
      "default": []
    },
    "skipChecks": {
      "type": "boolean",
      "default": false
    },
    "timeout": {
      "type": "integer",
      "default": 10
    }
  }
}
```

## File: `schema/release-it.json`
```json
{
  "$schema": "http://json-schema.org/draft-07/schema",
  "$id": "release-it#release-it",
  "title": "JSON schema for release-it configuration",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "$schema": {
      "type": "string",
      "description": "The JSON schema version used to validate this configuration file"
    },
    "extends": {
      "type": "string",
      "description": "URL that specifies a configuration to extend"
    },
    "hooks": {
      "type": "object",
      "additionalProperties": true,
      "patternProperties": {
        "^(before|after):((version|git|npm|github|gitlab):)?(init|bump|release)$": {
          "if": {
            "type": "array"
          },
          "then": {
            "type": "array",
            "items": {
              "type": "string"
            }
          },
          "else": {
            "type": "string"
          }
        }
      }
    },
    "plugins": {
      "type": "object",
      "additionalProperties": true
    },
    "git": {
      "$comment": "Boolean or git config object",
      "if": {
        "type": "object"
      },
      "then": {
        "$ref": "./git.json"
      },
      "else": {
        "type": "boolean",
        "default": false
      }
    },
    "npm": {
      "$comment": "Boolean or npm config object",
      "if": {
        "type": "object"
      },
      "then": {
        "$ref": "./npm.json"
      },
      "else": {
        "type": "boolean",
        "default": false
      }
    },
    "github": {
      "$comment": "Boolean or github config object",
      "if": {
        "type": "object"
      },
      "then": {
        "$ref": "./github.json"
      },
      "else": {
        "type": "boolean",
        "default": false
      }
    },
    "gitlab": {
      "$comment": "Boolean or gitlab config object",
      "if": {
        "type": "object"
      },
      "then": {
        "$ref": "./gitlab.json"
      },
      "else": {
        "type": "boolean",
        "default": false
      }
    }
  }
}
```

## File: `templates/changelog-compact.hbs`
```
{{#each releases}}
  {{#if @first}}
    {{#each merges}}
      - {{{message}}}{{#if href}} [`#{{id}}`]({{href}}){{/if}}
    {{/each}}
    {{#each fixes}}
      - {{{commit.subject}}}{{#each fixes}}{{#if href}} [`#{{id}}`]({{href}}){{/if}}{{/each}}
    {{/each}}
    {{#each commits}}
      - {{#if breaking}}**Breaking change:** {{/if}}{{{subject}}}{{#if href}} [`{{shorthash}}`]({{href}}){{/if}}
    {{/each}}
  {{/if}}
{{/each}}
```

## File: `templates/keepachangelog.hbs`
```
# Changelog

{{#each releases}}
  {{#if href}}
    ## [{{title}}]({{href}}){{#if tag}} ({{isoDate}}){{/if}}
  {{else}}
    ## {{title}}{{#if tag}} ({{isoDate}}){{/if}}
  {{/if}}

  {{#if summary}}
    {{summary}}
  {{/if}}

  {{#each merges}}
    - {{message}} {{#if href}}[`#{{id}}`]({{href}}){{/if}}
  {{/each}}
  {{#each fixes}}
    - {{commit.subject}}{{#each fixes}} {{#if href}}[`#{{id}}`]({{href}}){{/if}}{{/each}}
  {{/each}}
  {{#each commits}}
    - {{#if breaking}}**Breaking change:** {{/if}}{{subject}} {{#if href}}[`{{shorthash}}`]({{href}}){{/if}}
  {{/each}}

{{/each}}
```

## File: `test/args.js`
```javascript
import test from 'node:test';
import assert from 'node:assert/strict';
import { parseCliArguments } from '../lib/args.js';

test('should parse boolean arguments', () => {
  const args = [
    '--dry-run=false',
    '--ci',
    '--github=false',
    '--no-npm',
    '--git.addUntrackedFiles=true',
    '--git.commit=false',
    '--no-git.tag',
    '--git.commitMessage=test'
  ];

  const result = parseCliArguments(args);

  assert.equal(result['dry-run'], false);
  assert.equal(result.ci, true);
  assert.equal(result.github, false);
  assert.equal(result.npm, false);
  assert.equal(result.git.addUntrackedFiles, true);
  assert.equal(result.git.commit, false);
  assert.equal(result.git.tag, false);
  assert.equal(result.git.commitMessage, 'test');
});
```

## File: `test/cli.js`
```javascript
import test from 'node:test';
import assert from 'node:assert/strict';
import mockStdIo from 'mock-stdio';
import { version, help } from '../lib/cli.js';
import { readJSON } from '../lib/util.js';

const pkg = readJSON(new URL('../package.json', import.meta.url));

test('should print version', () => {
  mockStdIo.start();
  version();
  const { stdout } = mockStdIo.end();
  assert.equal(stdout, `v${pkg.version}\n`);
});

test('should print help', () => {
  mockStdIo.start();
  help();
  const { stdout } = mockStdIo.end();
  assert.match(stdout, new RegExp(`Release It!.+${pkg.version}`));
});
```

## File: `test/config.js`
```javascript
import test, { describe, before, after, afterEach } from 'node:test';
import assert from 'node:assert/strict';
import { isCI } from 'ci-info';
import Config from '../lib/config.js';
import { readJSON } from '../lib/util.js';
import { mockFetch } from './util/mock.js';
import { createTarBlobByRawContents } from './util/fetch.js';

const defaultConfig = readJSON(new URL('../config/release-it.json', import.meta.url));
const projectConfig = readJSON(new URL('../.release-it.json', import.meta.url));

const localConfig = { github: { release: true } };

describe('config', async () => {
  test("should read this project's own configuration", async () => {
    const config = new Config();
    await config.init();
    assert.deepEqual(config.constructorConfig, {});
    assert.deepEqual(config.localConfig, projectConfig);
    assert.deepEqual(config.defaultConfig, defaultConfig);
  });

  test('should contain default values', async () => {
    const config = new Config({ configDir: './test/stub/config/default' });
    await config.init();
    assert.deepEqual(config.constructorConfig, { configDir: './test/stub/config/default' });
    assert.deepEqual(config.localConfig, localConfig);
    assert.deepEqual(config.defaultConfig, defaultConfig);
  });

  test('should merge provided options', async () => {
    const config = new Config({
      configDir: './test/stub/config/merge',
      increment: '1.0.0',
      verbose: true,
      github: {
        release: true
      }
    });
    await config.init();
    const { options } = config;
    assert.equal(config.isVerbose, true);
    assert.equal(config.isDryRun, false);
    assert.equal(options.increment, '1.0.0');
    assert.equal(options.git.push, false);
    assert.equal(options.github.release, true);
  });

  test('should set CI mode', async () => {
    const config = new Config({ ci: true });
    await config.init();
    assert.equal(config.isCI, true);
  });

  test('should detect CI mode', async () => {
    const config = new Config();
    await config.init();
    assert.equal(config.options.ci, isCI);
    assert.equal(config.isCI, isCI);
  });

  test('should override --no-npm.publish', async () => {
    const config = new Config({ npm: { publish: false } });
    await config.init();
    assert.equal(config.options.npm.publish, false);
  });

  test('should read YAML config', async () => {
    const config = new Config({ configDir: './test/stub/config/yaml' });
    await config.init();
    assert.deepEqual(config.options.foo, { bar: 1 });
  });

  test('should read YML config', async () => {
    const config = new Config({ configDir: './test/stub/config/yml' });
    await config.init();
    assert.deepEqual(config.options.foo, { bar: 1 });
  });

  test('should read TOML config', async () => {
    const config = new Config({ configDir: './test/stub/config/toml' });
    await config.init();
    assert.deepEqual(config.options.foo, { bar: 1 });
  });

  test('should throw if provided config file is invalid (cosmiconfig exception)', async () => {
    await assert.rejects(async () => {
      const config = new Config({ config: './test/stub/config/invalid-config-txt' });
      await config.init();
    }, /Invalid configuration file at/);
  });

  test('should throw if provided config file is invalid (no object)', async () => {
    await assert.rejects(async () => {
      const config = new Config({ config: './test/stub/config/invalid-config-rc' });
      await config.init();
    }, /Invalid configuration file at/);
  });

  test('should not set default increment (for CI mode)', async () => {
    const config = new Config({ ci: true });
    await config.init();
    assert.equal(config.options.version.increment, undefined);
  });

  test('should not set default increment (for interactive mode)', async () => {
    const config = new Config({ ci: false });
    await config.init();
    assert.equal(config.options.version.increment, undefined);
  });

  test('should expand pre-release shortcut', async () => {
    const config = new Config({ increment: 'major', preRelease: 'beta' });
    await config.init();
    assert.deepEqual(config.options.version, {
      increment: 'major',
      isPreRelease: true,
      preReleaseBase: undefined,
      preReleaseId: 'beta'
    });
  });

  test('should expand pre-release shortcut (preRelease boolean)', async () => {
    const config = new Config({ ci: true, preRelease: true });
    await config.init();
    assert.deepEqual(config.options.version, {
      increment: undefined,
      isPreRelease: true,
      preReleaseBase: undefined,
      preReleaseId: undefined
    });
  });

  test('should expand pre-release shortcut (without increment)', async () => {
    const config = new Config({ ci: false, preRelease: 'alpha' });
    await config.init();
    assert.deepEqual(config.options.version, {
      increment: undefined,
      isPreRelease: true,
      preReleaseBase: undefined,
      preReleaseId: 'alpha'
    });
  });

  test('should expand pre-release shortcut (including increment and npm.tag)', async () => {
    const config = new Config({ increment: 'minor', preRelease: 'rc' });
    await config.init();
    assert.deepEqual(config.options.version, {
      increment: 'minor',
      isPreRelease: true,
      preReleaseBase: undefined,
      preReleaseId: 'rc'
    });
  });

  test('should use pre-release base', async () => {
    const config = new Config({ increment: 'minor', preRelease: 'next', preReleaseBase: '1' });
    await config.init();
    assert.deepEqual(config.options.version, {
      increment: 'minor',
      isPreRelease: true,
      preReleaseBase: '1',
      preReleaseId: 'next'
    });
  });

  test('should expand pre-release shortcut (snapshot)', async () => {
    const config = new Config({ snapshot: 'feat' });
    await config.init();
    assert.deepEqual(config.options.version, {
      increment: 'prerelease',
      isPreRelease: true,
      preReleaseBase: undefined,
      preReleaseId: 'feat'
    });
    assert.equal(config.options.git.tagMatch, '0.0.0-feat.[0-9]*');
    assert.equal(config.options.git.getLatestTagFromAllRefs, true);
  });
});

describe('fetch extended configuration', () => {
  const [mocker, server] = mockFetch('https://api.github.com');

  before(() => {
    mocker.mockGlobal();
  });

  afterEach(() => {
    mocker.clearAll();
  });

  after(() => {
    mocker.unmockGlobal();
  });

  test('should fetch extended configuration with default file and default branch', async () => {
    const extendedConfiguration = {
      git: {
        commitMessage: 'Released version ${version}'
      }
    };

    server.head('/repos/release-it/release-it-configuration/tarball/main', {
      status: 200,
      headers: {}
    });

    server.get('/repos/release-it/release-it-configuration/tarball/main', {
      status: 200,
      body: await new Response(
        createTarBlobByRawContents({
          '.release-it.json': JSON.stringify(extendedConfiguration)
        })
      ).arrayBuffer()
    });

    const config = new Config({
      extends: 'github:release-it/release-it-configuration'
    });
    await config.init();

    assert(mocker.allRoutesCalled());

    assert.equal(config.options.git.commitMessage, extendedConfiguration.git.commitMessage);
  });

  test('should fetch extended configuration with default file and specific tag', async () => {
    const extendedConfiguration = {
      git: {
        commitMessage: 'Released version ${version}'
      }
    };

    server.head('/repos/release-it/release-it-configuration/tarball/1.0.0', {
      status: 200,
      headers: {}
    });

    server.get('/repos/release-it/release-it-configuration/tarball/1.0.0', {
      status: 200,
      body: await new Response(
        createTarBlobByRawContents({
          '.release-it.json': JSON.stringify(extendedConfiguration)
        })
      ).arrayBuffer()
    });

    const config = new Config({
      extends: 'github:release-it/release-it-configuration#1.0.0'
    });
    await config.init();

    assert(mocker.allRoutesCalled());

    assert.equal(config.options.git.commitMessage, extendedConfiguration.git.commitMessage);
  });

  test('should fetch extended configuration with sub dir and specific tag', async () => {
    const extendedConfiguration = {
      git: {
        commitMessage: 'Released version ${version}'
      }
    };

    const extendedSubConfiguration = {
      git: {
        commitMessage: 'Released pkg version ${version}'
      }
    };

    server.head('/repos/release-it/release-it-configuration/tarball/1.0.0', {
      status: 200,
      headers: {}
    });

    server.get('/repos/release-it/release-it-configuration/tarball/1.0.0', {
      status: 200,
      body: await new Response(
        createTarBlobByRawContents({
          '.release-it.json': JSON.stringify(extendedConfiguration),
          'sub/.release-it.json': JSON.stringify(extendedSubConfiguration)
        })
      ).arrayBuffer()
    });

    const config = new Config({
      extends: 'github:release-it/release-it-configuration/sub#1.0.0'
    });
    await config.init();

    assert(mocker.allRoutesCalled());

    assert.equal(config.options.git.commitMessage, extendedSubConfiguration.git.commitMessage);
  });

  test('should fetch extended configuration with custom file and default branch', async () => {
    const extendedConfiguration = {
      git: {
        commitMessage: 'Released version ${version}'
      }
    };

    const extendedSubConfiguration = {
      git: {
        commitMessage: 'Released pkg version ${version}'
      }
    };

    server.head('/repos/release-it/release-it-configuration/tarball/main', {
      status: 200,
      headers: {}
    });

    server.get('/repos/release-it/release-it-configuration/tarball/main', {
      status: 200,
      body: await new Response(
        createTarBlobByRawContents({
          '.release-it.json': JSON.stringify(extendedConfiguration),
          'sub/.release-it.json': JSON.stringify(extendedSubConfiguration)
        })
      ).arrayBuffer()
    });

    const config = new Config({
      extends: 'github:release-it/release-it-configuration/sub'
    });
    await config.init();

    assert(mocker.allRoutesCalled());

    assert.equal(config.options.git.commitMessage, extendedSubConfiguration.git.commitMessage);
  });
});
```

## File: `test/git.init.js`
```javascript
import childProcess from 'node:child_process';
import test, { beforeEach, describe } from 'node:test';
import { mkdirSync } from 'node:fs';
import assert from 'node:assert/strict';
import Shell from '../lib/shell.js';
import Git from '../lib/plugin/git/Git.js';
import { execOpts, readJSON } from '../lib/util.js';
import sh from './util/sh.js';
import { factory } from './util/index.js';
import { mkTmpDir, gitAdd } from './util/helpers.js';

describe('git.init', () => {
  const { git } = readJSON(new URL('../config/release-it.json', import.meta.url));

  let bare;
  let target;
  beforeEach(() => {
    bare = mkTmpDir();
    target = mkTmpDir();
    process.chdir(bare);
    sh.exec(`git init --bare .`, execOpts);
    sh.exec(`git clone ${bare} ${target}`, execOpts);
    process.chdir(target);
    gitAdd('line', 'file', 'Add file');
  });

  test('should throw if on wrong branch', async () => {
    const options = { git: { requireBranch: 'dev' } };
    const gitClient = await factory(Git, { options });
    childProcess.execSync('git remote remove origin', execOpts);
    await assert.rejects(gitClient.init(), /Must be on branch dev/);
  });

  test('should throw if on negated branch', async () => {
    const options = { git: { requireBranch: '!main' } };
    const gitClient = await factory(Git, { options });
    sh.exec('git checkout -b main', execOpts);
    await assert.rejects(gitClient.init(), /Must be on branch !main/);
  });

  test('should not throw if required branch matches', async () => {
    const options = { git: { requireBranch: 'ma?*' } };
    const gitClient = await factory(Git, { options });
    await assert.doesNotReject(gitClient.init());
  });

  test('should not throw if one of required branch matches', async () => {
    const options = { git: { requireBranch: ['release/*', 'hotfix/*'] } };
    const gitClient = await factory(Git, { options });
    childProcess.execSync('git checkout -b release/v1', execOpts);
    await assert.doesNotReject(gitClient.init());
  });

  test('should throw if there is no remote Git url', async () => {
    const gitClient = await factory(Git, { options: { git } });
    childProcess.execSync('git remote remove origin', execOpts);
    await assert.rejects(gitClient.init(), /Could not get remote Git url/);
  });

  test('should throw if working dir is not clean', async () => {
    const gitClient = await factory(Git, { options: { git } });
    childProcess.execSync('rm file', execOpts);
    await assert.rejects(gitClient.init(), /Working dir must be clean/);
  });

  test('should throw if no upstream is configured', async () => {
    const gitClient = await factory(Git, { options: { git } });
    childProcess.execSync('git checkout -b foo', execOpts);
    await assert.rejects(gitClient.init(), /No upstream configured for current branch/);
  });

  test('should throw if there are no commits', async () => {
    const options = { git: { requireCommits: true } };
    const gitClient = await factory(Git, { options });
    childProcess.execSync('git tag 1.0.0', execOpts);
    await assert.rejects(gitClient.init(), /There are no commits since the latest tag/);
  });

  test('should not throw if there are commits', async () => {
    const options = { git: { requireCommits: true } };
    const gitClient = await factory(Git, { options });
    childProcess.execSync('git tag 1.0.0', execOpts);
    gitAdd('line', 'file', 'Add file');
    await assert.doesNotReject(gitClient.init(), 'There are no commits since the latest tag');
  });

  test('should fail (exit code 1) if there are no commits', async () => {
    const options = { git: { requireCommits: true } };
    const gitClient = await factory(Git, { options });
    childProcess.execSync('git tag 1.0.0', execOpts);
    await assert.rejects(gitClient.init(), { code: 1 });
  });

  test('should not fail (exit code 0) if there are no commits', async () => {
    const options = { git: { requireCommits: true, requireCommitsFail: false } };
    const gitClient = await factory(Git, { options });
    childProcess.execSync('git tag 1.0.0', execOpts);
    await assert.rejects(gitClient.init(), { code: 0 });
  });

  test('should throw if there are no commits in specified path', async () => {
    const options = { git: { requireCommits: true, commitsPath: 'dir' } };
    const gitClient = await factory(Git, { options });
    mkdirSync('dir', { recursive: true });
    sh.exec('git tag 1.0.0', execOpts);
    await assert.rejects(gitClient.init(), { message: /^There are no commits since the latest tag/ });
  });

  test('should not throw if there are commits in specified path', async () => {
    const options = { git: { requireCommits: true, commitsPath: 'dir' } };
    const gitClient = await factory(Git, { options });
    sh.exec('git tag 1.0.0', execOpts);
    gitAdd('line', 'dir/file', 'Add file');
    await assert.doesNotReject(gitClient.init());
  });

  test('should not throw if there are no tags', async () => {
    const options = { git: { requireCommits: true } };
    const gitClient = await factory(Git, { options });
    gitAdd('line', 'file', 'Add file');
    await assert.doesNotReject(gitClient.init());
  });

  test('should not throw if origin remote is renamed', async () => {
    childProcess.execSync('git remote rename origin upstream', execOpts);
    const gitClient = await factory(Git);
    await assert.doesNotReject(gitClient.init());
  });

  test('should detect and include version prefix ("v")', async () => {
    const gitClient = await factory(Git, { options: { git } });
    childProcess.execSync('git tag v1.0.0', execOpts);
    await gitClient.init();
    await gitClient.bump('1.0.1');
    assert.equal(gitClient.config.getContext('tagName'), 'v1.0.1');
  });

  test('should detect and exclude version prefix', async () => {
    const gitClient = await factory(Git, { options: { git } });
    childProcess.execSync('git tag 1.0.0', execOpts);
    await gitClient.init();
    await gitClient.bump('1.0.1');
    assert.equal(gitClient.config.getContext('tagName'), '1.0.1');
  });

  test('should detect and exclude version prefix (configured)', async () => {
    const gitClient = await factory(Git, { options: { git: { tagName: 'v${version}' } } });
    childProcess.execSync('git tag 1.0.0', execOpts);
    await gitClient.init();
    await gitClient.bump('1.0.1');
    assert.equal(gitClient.config.getContext('tagName'), 'v1.0.1');
  });

  test('should honor custom tagName configuration', async () => {
    const gitClient = await factory(Git, { options: { git: { tagName: 'TAGNAME-${repo.project}-v${version}' } } });
    childProcess.execSync('git tag 1.0.0', execOpts);
    await gitClient.init();
    await gitClient.bump('1.0.1');
    const { project } = gitClient.getContext('repo');
    assert.equal(gitClient.config.getContext('tagName'), `TAGNAME-${project}-v1.0.1`);
  });

  test('should get the latest tag after fetch', async () => {
    const shell = await factory(Shell);
    const gitClient = await factory(Git, { container: { shell } });
    const other = mkTmpDir();
    childProcess.execSync('git push', execOpts);
    childProcess.execSync(`git clone ${bare} ${other}`, execOpts);

    process.chdir(other);
    childProcess.execSync('git tag 1.0.0', execOpts);
    childProcess.execSync('git push --tags', execOpts);
    process.chdir(target);
    await gitClient.init();
    assert.equal(gitClient.config.getContext('latestTag'), '1.0.0');
  });

  test('should get the latest custom tag after fetch when tagName is configured', async () => {
    const shell = await factory(Shell);
    const gitClient = await factory(Git, {
      options: { git: { tagName: 'TAGNAME-v${version}' } },
      container: { shell }
    });
    const other = mkTmpDir();
    childProcess.execSync('git push', execOpts);
    childProcess.execSync(`git clone ${bare} ${other}`, execOpts);
    process.chdir(other);
    childProcess.execSync('git tag TAGNAME-OTHER-v2.0.0', execOpts);
    childProcess.execSync('git tag TAGNAME-v1.0.0', execOpts);
    childProcess.execSync('git tag TAGNAME-OTHER-v2.0.2', execOpts);
    childProcess.execSync('git push --tags', execOpts);
    process.chdir(target);
    await gitClient.init();
    assert.equal(gitClient.config.getContext('latestTag'), 'TAGNAME-v1.0.0');
  });

  test('should get the latest tag based on tagMatch', async () => {
    const shell = await factory(Shell);
    const gitClient = await factory(Git, {
      options: { git: { tagMatch: '[0-9][0-9]\\.[0-1][0-9]\\.[0-9]*' } },
      container: { shell }
    });
    childProcess.execSync('git tag 1.0.0', execOpts);
    childProcess.execSync('git tag 21.04.3', execOpts);
    childProcess.execSync('git tag 1.0.1', execOpts);
    childProcess.execSync('git push --tags', execOpts);
    await gitClient.init();
    assert.equal(gitClient.config.getContext('latestTag'), '21.04.3');
  });

  test('should get the latest tag based on tagExclude', async () => {
    const shell = await factory(Shell);
    const gitClient = await factory(Git, {
      options: { git: { tagExclude: '*[-]*' } },
      container: { shell }
    });
    childProcess.execSync('git tag 1.0.0', execOpts);
    childProcess.execSync('git commit --allow-empty -m "commit 1"', execOpts);
    childProcess.execSync('git tag 1.0.1-rc.0', execOpts);
    childProcess.execSync('git tag 1.0.1', execOpts);
    childProcess.execSync('git commit --allow-empty -m "commit 2"', execOpts);
    childProcess.execSync('git tag 1.1.0-rc.0', execOpts);
    childProcess.execSync('git push --tags', execOpts);
    await gitClient.init();
    assert.equal(gitClient.config.getContext('latestTag'), '1.0.1');
  });

  test('should generate correct changelog', async () => {
    const gitClient = await factory(Git, { options: { git } });
    childProcess.execSync('git tag 1.0.0', execOpts);
    gitAdd('line', 'file', 'Add file');
    gitAdd('line', 'file', 'Add file');
    await gitClient.init();
    const changelog = await gitClient.getChangelog();
    assert.match(changelog, /\* Add file \(\w{7}\)\n\* Add file \(\w{7}\)/);
  });

  test('should get the full changelog since latest major tag', async () => {
    const shell = await factory(Shell);
    const gitClient = await factory(Git, {
      options: { git: { tagMatch: '[0-9]\\.[0-9]\\.[0-9]', changelog: git.changelog } },
      container: { shell }
    });
    childProcess.execSync('git tag 1.0.0', execOpts);
    gitAdd('line', 'file', 'Add file');
    childProcess.execSync('git tag 2.0.0-rc.0', execOpts);
    gitAdd('line', 'file', 'Add file');
    childProcess.execSync('git tag 2.0.0-rc.1', execOpts);
    gitAdd('line', 'file', 'Add file');
    await gitClient.init();
    assert.equal(gitClient.config.getContext('latestTag'), '1.0.0');
    const changelog = await gitClient.getChangelog();
    assert.match(changelog, /\* Add file \(\w{7}\)\n\* Add file \(\w{7}\)\n\* Add file \(\w{7}\)/);
  });
});
```

## File: `test/git.js`
```javascript
import test, { beforeEach, describe } from 'node:test';
import assert from 'node:assert/strict';
import { EOL } from 'node:os';
import childProcess from 'node:child_process';
import { appendFileSync } from 'node:fs';
import Git from '../lib/plugin/git/Git.js';
import { execOpts, touch } from '../lib/util.js';
import sh from './util/sh.js';
import { factory } from './util/index.js';
import { mkTmpDir, readFile, gitAdd } from './util/helpers.js';

describe('git', () => {
  beforeEach(() => {
    const tmp = mkTmpDir();
    process.chdir(tmp);
  });

  test('should return whether repo has upstream branch', async () => {
    const gitClient = await factory(Git);
    childProcess.execSync('git init', execOpts);
    gitAdd('line', 'file', 'Add file');
    assert.equal(await gitClient.hasUpstreamBranch(), false);
  });

  test('should return branch name', async () => {
    const gitClient = await factory(Git);
    childProcess.execSync('git init', execOpts);
    assert.equal(await gitClient.getBranchName(), null);
    childProcess.execSync('git checkout -b feat', execOpts);
    gitAdd('line', 'file', 'Add file');
    assert.equal(await gitClient.getBranchName(), 'feat');
  });

  test('should return whether tag exists and if working dir is clean', async () => {
    const gitClient = await factory(Git);
    childProcess.execSync('git init', execOpts);
    assert.equal(await gitClient.tagExists('1.0.0'), false);
    touch('file');
    assert.equal(await gitClient.isWorkingDirClean(), false);
    gitAdd('line', 'file', 'Add file');
    childProcess.execSync('git tag 1.0.0', execOpts);
    assert(await gitClient.tagExists('1.0.0'));
    assert(await gitClient.isWorkingDirClean());
  });

  test('should throw if tag exists', async () => {
    const gitClient = await factory(Git);
    childProcess.execSync('git init', execOpts);
    touch('file');
    gitAdd('line', 'file', 'Add file');
    childProcess.execSync('git tag 0.0.2', execOpts);
    gitClient.config.setContext({ latestTag: '0.0.1', tagName: '0.0.2' });
    await assert.rejects(gitClient.tag({ name: '0.0.2' }), /fatal: tag '0\.0\.2' already exists/);
  });

  test('should only warn if tag exists intentionally', async t => {
    const gitClient = await factory(Git);
    const warn = t.mock.method(gitClient.log, 'warn');
    childProcess.execSync('git init', execOpts);
    touch('file');
    gitAdd('line', 'file', 'Add file');
    childProcess.execSync('git tag 1.0.0', execOpts);
    gitClient.config.setContext({ latestTag: '1.0.0', tagName: '1.0.0' });
    await assert.doesNotReject(gitClient.tag());
    assert.equal(warn.mock.callCount(), 1);
    assert.equal(warn.mock.calls[0].arguments[0], 'Tag "1.0.0" already exists');
  });

  test('should return the remote url', async () => {
    childProcess.execSync(`git init`, execOpts);
    {
      const options = { git: { pushRepo: 'origin' } };
      const gitClient = await factory(Git, { options });
      assert.equal(await gitClient.getRemoteUrl(), null);
      childProcess.execSync(`git remote add origin foo`, execOpts);
      assert.equal(await gitClient.getRemoteUrl(), 'foo');
    }
    {
      const options = { git: { pushRepo: 'another' } };
      const gitClient = await factory(Git, { options });
      assert.equal(await gitClient.getRemoteUrl(), null);
      childProcess.execSync(`git remote add another bar`, execOpts);
      assert.equal(await gitClient.getRemoteUrl(), 'bar');
    }
    {
      const options = { git: { pushRepo: 'git://github.com/webpro/release-it.git' } };
      const gitClient = await factory(Git, { options });
      assert.equal(await gitClient.getRemoteUrl(), 'git://github.com/webpro/release-it.git');
    }
  });

  test('should return the non-origin remote', async () => {
    const bare = mkTmpDir();
    childProcess.execSync(`git init --bare ${bare}`, execOpts);
    childProcess.execSync(`git clone ${bare} .`, execOpts);
    gitAdd('line', 'file', 'Add file');
    childProcess.execSync('git remote rename origin upstream', execOpts);
    const gitClient = await factory(Git);
    assert.equal(await gitClient.getRemoteUrl(), bare);
  });

  test('should stage, commit, tag and push', async () => {
    const bare = mkTmpDir();
    childProcess.execSync(`git init --bare ${bare}`, execOpts);
    childProcess.execSync(`git clone ${bare} .`, execOpts);
    const version = '1.2.3';
    gitAdd(`{"version":"${version}"}`, 'package.json', 'Add package.json');
    {
      const gitClient = await factory(Git);
      childProcess.execSync(`git tag ${version}`, execOpts);
      assert.equal(await gitClient.getLatestTagName(), version);
    }
    {
      const gitClient = await factory(Git);
      gitAdd('line', 'file', 'Add file');
      childProcess.execSync('npm --no-git-tag-version version patch', execOpts);
      await gitClient.stage('package.json');
      await gitClient.commit({ message: `Release v1.2.4` });
      await gitClient.tag({ name: 'v1.2.4', annotation: 'Release v1.2.4' });
      assert.equal(await gitClient.getLatestTagName(), 'v1.2.4');
      await gitClient.push();
      const stdout = childProcess.execSync('git status -uno', { encoding: 'utf-8' });
      assert.match(stdout, /nothing to commit/);
    }
  });

  test('should commit, tag and push with extra args', async t => {
    const bare = mkTmpDir();
    childProcess.execSync(`git init --bare ${bare}`, execOpts);
    childProcess.execSync(`git clone ${bare} .`, execOpts);
    gitAdd('line', 'file', 'Add file');
    const options = { git: { commitArgs: '-S', tagArgs: ['-T', 'foo'], pushArgs: ['-U', 'bar', '-V'] } };
    const gitClient = await factory(Git, { options });
    const stub = t.mock.method(gitClient.shell, 'exec', () => Promise.resolve());
    await gitClient.stage('package.json');
    await gitClient.commit({ message: `Release v1.2.4` });
    await gitClient.tag({ name: 'v1.2.4', annotation: 'Release v1.2.4' });
    await gitClient.push();
    assert(stub.mock.calls[1].arguments[0].includes('-S'));
    assert.equal(stub.mock.calls[2].arguments[0][5], '-T');
    assert.equal(stub.mock.calls[2].arguments[0][6], 'foo');
    assert(stub.mock.calls.at(-1).arguments[0].join(' ').includes('-U bar -V'));
  });

  test('should amend commit without message if not provided', async t => {
    const bare = mkTmpDir();
    childProcess.execSync(`git init --bare ${bare}`, execOpts);
    childProcess.execSync(`git clone ${bare} .`, execOpts);
    gitAdd('line', 'file', 'Add file');
    const options = { git: { commitArgs: ['--amend', '--no-edit', '--no-verify'] } };
    const gitClient = await factory(Git, { options });
    const exec = t.mock.method(gitClient.shell, 'exec', () => Promise.resolve());
    await gitClient.stage('package.json');
    await gitClient.commit();
    assert.deepEqual(exec.mock.calls[1].arguments[0], ['git', 'commit', '--amend', '--no-edit', '--no-verify']);
  });

  test('should commit and tag with quoted characters', async () => {
    const bare = mkTmpDir();
    childProcess.execSync(`git init --bare ${bare}`, execOpts);
    childProcess.execSync(`git clone ${bare} .`, execOpts);
    const gitClient = await factory(Git, {
      options: { git: { commitMessage: 'Release ${version}', tagAnnotation: 'Release ${version}\n\n${changelog}' } }
    });
    touch('file');
    const changelog = `- Foo's${EOL}- "$bar"${EOL}- '$baz'${EOL}- foo`;
    gitClient.config.setContext({ version: '1.0.0', changelog });

    await gitClient.stage('file');
    await gitClient.commit();
    await gitClient.tag({ name: '1.0.0' });
    await gitClient.push();
    {
      const stdout = childProcess.execSync('git log -1 --format=%s', { encoding: 'utf-8' });
      assert.equal(stdout.trim(), 'Release 1.0.0');
    }
    {
      const stdout = childProcess.execSync('git tag -n99', { encoding: 'utf-8' });
      assert.equal(
        stdout.trim(),
        `1.0.0           Release 1.0.0\n    \n    - Foo's\n    - "$bar"\n    - '$baz'\n    - foo`
      );
    }
  });

  test('should push to origin', async t => {
    const bare = mkTmpDir();
    childProcess.execSync(`git init --bare ${bare}`, execOpts);
    childProcess.execSync(`git clone ${bare} .`, execOpts);
    gitAdd('line', 'file', 'Add file');
    const gitClient = await factory(Git);
    const spy = t.mock.method(gitClient.shell, 'exec');
    await gitClient.push();
    assert.deepEqual(spy.mock.calls.at(-1).arguments[0], ['git', 'push']);
    const stdout = childProcess.execSync('git ls-tree -r HEAD --name-only', {
      cwd: bare,
      encoding: 'utf-8'
    });
    assert.equal(stdout.trim(), 'file');
  });

  test('should push to tracked upstream branch', async t => {
    const bare = mkTmpDir();
    childProcess.execSync(`git init --bare ${bare}`, execOpts);
    childProcess.execSync(`git clone ${bare} .`, execOpts);
    childProcess.execSync(`git remote rename origin upstream`, execOpts);
    gitAdd('line', 'file', 'Add file');
    const gitClient = await factory(Git);
    const spy = t.mock.method(gitClient.shell, 'exec');
    await gitClient.push();
    assert.deepEqual(spy.mock.calls.at(-1).arguments[0], ['git', 'push']);
    const stdout = childProcess.execSync('git ls-tree -r HEAD --name-only', {
      cwd: bare,
      encoding: 'utf-8'
    });
    assert.equal(stdout.trim(), 'file');
  });

  test('should push to repo url', async t => {
    const bare = mkTmpDir();
    childProcess.execSync(`git init --bare ${bare}`, execOpts);
    childProcess.execSync(`git clone ${bare} .`, execOpts);
    gitAdd('line', 'file', 'Add file');
    const options = { git: { pushRepo: 'https://host/repo.git' } };
    const gitClient = await factory(Git, { options });
    const spy = t.mock.method(gitClient.shell, 'exec');
    try {
      await gitClient.push();
    } catch (err) {
      assert.deepEqual(spy.mock.calls.at(-1).arguments[0], ['git', 'push', 'https://host/repo.git']);
    }
  });

  test('should push to remote name (not "origin")', async t => {
    const bare = mkTmpDir();
    childProcess.execSync(`git init --bare ${bare}`, execOpts);
    childProcess.execSync(`git clone ${bare} .`, execOpts);
    gitAdd('line', 'file', 'Add file');
    childProcess.execSync(
      `git remote add upstream ${childProcess.execSync('git config --get remote.origin.url', {
        encoding: 'utf-8'
      })}`,
      execOpts
    );
    const options = { git: { pushRepo: 'upstream' } };
    const gitClient = await factory(Git, { options });
    const spy = t.mock.method(gitClient.shell, 'exec');
    await gitClient.push();
    assert.deepEqual(spy.mock.calls.at(-1).arguments[0], ['git', 'push', 'upstream']);
    const stdout = childProcess.execSync('git ls-tree -r HEAD --name-only', {
      cwd: bare,
      encoding: 'utf-8'
    });
    assert.equal(stdout.trim(), 'file');

    {
      childProcess.execSync(`git checkout -b foo`, execOpts);
      gitAdd('line', 'file', 'Add file');
      await gitClient.push();
      assert.deepEqual(spy.mock.calls.at(-1).arguments[0], ['git', 'push', '--set-upstream', 'upstream', 'foo']);
      assert.match(
        await spy.mock.calls.at(-1).result,
        /branch .?foo.? set up to track (remote branch .?foo.? from .?upstream.?|.?upstream\/foo.?)/i
      );
    }
  });

  test('should return repo status', async () => {
    const gitClient = await factory(Git);
    childProcess.execSync('git init', execOpts);
    gitAdd('line', 'file1', 'Add file');

    appendFileSync('file1', 'line');

    appendFileSync('file2', 'line');
    childProcess.execSync('git add file2', execOpts);
    assert.equal(await gitClient.status(), ' M file1\nA  file2');
  });

  test('should reset files', async t => {
    const gitClient = await factory(Git);
    childProcess.execSync('git init', execOpts);
    gitAdd('line', 'file', 'Add file');

    appendFileSync('file', 'line');
    assert.match(await readFile('file'), /^line\s*line\s*$/);
    await gitClient.reset('file');
    assert.match(await readFile('file'), /^line\s*$/);
    const warn = t.mock.method(gitClient.log, 'warn');
    await gitClient.reset(['file2, file3']);
    assert.match(warn.mock.calls[0].arguments[0], /Could not reset file2, file3/);
  });

  test('should roll back when cancelled', async t => {
    childProcess.execSync('git init', execOpts);
    childProcess.execSync(`git remote add origin file://foo`, execOpts);
    const version = '1.2.3';
    gitAdd(`{"version":"${version}"}`, 'package.json', 'Add package.json');
    const options = { git: { requireCleanWorkingDir: true, commit: true, tag: true, tagName: 'v${version}' } };
    const gitClient = await factory(Git, { options });
    const exec = t.mock.method(gitClient.shell, 'execFormattedCommand');
    childProcess.execSync(`git tag ${version}`, execOpts);
    gitAdd('line', 'file', 'Add file');

    await gitClient.init();

    childProcess.execSync('npm --no-git-tag-version version patch', execOpts);

    gitClient.bump('1.2.4');
    await gitClient.beforeRelease();
    await gitClient.stage('package.json');
    await gitClient.commit({ message: 'Add this' });
    await gitClient.tag();
    await gitClient.rollbackOnce();

    assert.equal(exec.mock.calls[11].arguments[0], 'git tag --delete v1.2.4');
    assert.equal(exec.mock.calls[12].arguments[0], 'git reset --hard HEAD~1');
  });

  // To get this test to pass, I had to switch between spawnsync and execsync somehow
  test('should remove remote tag when push to branch failed', async t => {
    childProcess.execSync('git init', execOpts);
    childProcess.execSync(`git remote add origin file://foo`, execOpts);
    sh.exec(`git remote update`, execOpts);
    const version = '1.2.3';
    gitAdd(`{"version":"${version}"}`, 'package.json', 'Add package.json');
    const options = { git: { requireCleanWorkingDir: true, commit: true, tag: true, tagName: 'v${version}' } };
    const gitClient = await factory(Git, { options });
    const exec = t.mock.method(gitClient.shell, 'execFormattedCommand');
    sh.exec(`git push`, execOpts);
    sh.exec(`git checkout HEAD~1`, execOpts);
    gitAdd('line', 'file', 'Add file');

    await gitClient.init();

    childProcess.execSync('npm --no-git-tag-version version patch', execOpts);

    gitClient.bump('1.2.4');
    await gitClient.beforeRelease();
    await gitClient.stage('package.json');
    await gitClient.commit({ message: 'Add this' });
    await gitClient.tag();
    try {
      await gitClient.push();
    } catch (e) {
      // push would fail with an error since HEAD is behind origin
    }
    assert.equal(exec.mock.calls[15].arguments[0], 'git push origin --delete v1.2.4');
  });

  test('should skip rollback when push fails but package is already published', async t => {
    childProcess.execSync('git init', execOpts);
    childProcess.execSync(`git remote add origin file://foo`, execOpts);
    sh.exec(`git remote update`, execOpts);
    const version = '1.2.3';
    gitAdd(`{"version":"${version}"}`, 'package.json', 'Add package.json');
    const options = { git: { requireCleanWorkingDir: true, commit: true, tag: true, tagName: 'v${version}' } };
    const gitClient = await factory(Git, { options });
    const exec = t.mock.method(gitClient.shell, 'execFormattedCommand');
    const warn = t.mock.method(gitClient.log, 'warn');
    sh.exec(`git push`, execOpts);
    sh.exec(`git checkout HEAD~1`, execOpts);
    gitAdd('line', 'file', 'Add file');

    await gitClient.init();

    childProcess.execSync('npm --no-git-tag-version version patch', execOpts);

    gitClient.bump('1.2.4');
    await gitClient.beforeRelease();
    await gitClient.stage('package.json');
    await gitClient.commit({ message: 'Add this' });
    await gitClient.tag();

    gitClient.config.setContext({ isReleased: true });

    await gitClient.push();

    const execCalls = exec.mock.calls.map(c => c.arguments[0]);
    assert.equal(execCalls.includes('git push origin --delete v1.2.4'), false);
    assert(warn.mock.calls.some(c => /git push failed/.test(c.arguments[0])));
  });

  test('should not touch existing history when rolling back', async t => {
    childProcess.execSync('git init', execOpts);
    const version = '1.2.3';
    gitAdd(`{"version":"${version}"}`, 'package.json', 'Add package.json');
    const options = { git: { requireCleanWorkingDir: true, commit: true, tag: true } };
    const gitClient = await factory(Git, { options });
    childProcess.execSync(`git tag ${version}`, execOpts);

    const exec = t.mock.method(gitClient.shell, 'execFormattedCommand');
    gitClient.config.setContext({ version: '1.2.4' });
    await gitClient.beforeRelease();
    await gitClient.commit();
    await gitClient.rollbackOnce();

    assert.equal(exec.mock.calls[3].arguments[0], 'git reset --hard HEAD');
  });

  test.skip('should not roll back with risky config', async () => {
    childProcess.execSync('git init', execOpts);
    const options = { git: { requireCleanWorkingDir: false, commit: true, tag: true } };
    const gitClient = await factory(Git, { options });
    await gitClient.beforeRelease();
    assert.equal('rollbackOnce' in gitClient, false);
  });

  test('should return latest tag from default branch (not parent commit)', async () => {
    childProcess.execSync('git init', execOpts);

    {
      const options = { git: { getLatestTagFromAllRefs: true } };
      const gitClient = await factory(Git, { options });
      gitAdd('main', 'file', 'Add file in main');
      const defaultBranchName = await gitClient.getBranchName();
      const developBranchName = 'develop';
      const featureBranchPrefix = 'feature';
      await gitClient.tag({ name: '1.0.0' });
      childProcess.execSync(`git branch ${developBranchName} ${defaultBranchName}`, execOpts);
      childProcess.execSync(`git checkout -b ${featureBranchPrefix}/first ${developBranchName}`, execOpts);
      gitAdd('feature/1', 'file', 'Update file in feature branch (1)');
      childProcess.execSync(`git checkout ${developBranchName}`, execOpts);
      childProcess.execSync(`git merge --no-ff ${featureBranchPrefix}/first`, execOpts);
      await gitClient.tag({ name: '1.1.0-rc.1' });
      childProcess.execSync(`git checkout ${defaultBranchName}`, execOpts);
      childProcess.execSync(`git merge --no-ff ${developBranchName}`, execOpts);
      await gitClient.tag({ name: '1.1.0' });
      childProcess.execSync(`git checkout -b ${featureBranchPrefix}/second ${developBranchName}`, execOpts);
      gitAdd('feature/2', 'file', 'Update file again, in feature branch (2)');
      childProcess.execSync(`git checkout ${developBranchName}`, execOpts);
      childProcess.execSync(`git merge --no-ff ${featureBranchPrefix}/second`, execOpts);
      assert.equal(await gitClient.getLatestTagName(), '1.1.0');
    }

    {
      const options = { git: { getLatestTagFromAllRefs: false } };
      const gitClient = await factory(Git, { options });
      assert.equal(await gitClient.getLatestTagName(), '1.1.0-rc.1');
    }
  });
});
```

## File: `test/github.js`
```javascript
import test, { describe, before, after, afterEach } from 'node:test';
import assert from 'node:assert/strict';
import { RequestError } from '@octokit/request-error';
import GitHub from '../lib/plugin/github/GitHub.js';
import { getSearchQueries } from '../lib/plugin/github/util.js';
import { factory, runTasks } from './util/index.js';
import {
  interceptAuthentication,
  interceptCollaborator,
  interceptListReleases,
  interceptCreate,
  interceptUpdate,
  interceptAsset
} from './stub/github.js';
import { mockFetch } from './util/mock.js';

describe('github', () => {
  const tokenRef = 'GITHUB_TOKEN';
  const pushRepo = 'git://github.com/user/repo';
  const host = 'github.com';
  const git = { changelog: '' };
  const requestErrorOptions = { request: { url: '', headers: {} }, response: { headers: {} } };

  const [mocker, api, assets, example, custom] = mockFetch([
    'https://api.github.com',
    'https://uploads.github.com',
    'https://github.example.org/api/v3',
    'https://custom.example.org/api/v3'
  ]);

  before(() => {
    mocker.mockGlobal();
  });

  afterEach(() => {
    mocker.clearAll();
  });

  after(() => {
    mocker.unmockGlobal();
  });

  test('should check token and perform checks', async () => {
    const tokenRef = 'MY_GITHUB_TOKEN';
    const options = { github: { release: true, tokenRef, pushRepo } };
    const github = await factory(GitHub, { options });

    interceptAuthentication(api);
    interceptCollaborator(api);
    await assert.doesNotReject(github.init());
  });

  test('should check token and warn', async () => {
    const tokenRef = 'MY_GITHUB_TOKEN';
    const options = { github: { release: true, tokenRef, pushRepo } };
    const github = await factory(GitHub, { options });
    delete process.env[tokenRef];

    await assert.doesNotReject(github.init());

    assert.equal(
      github.log.warn.mock.calls[0].arguments[0],
      'Environment variable "MY_GITHUB_TOKEN" is required for automated GitHub Releases.'
    );
    assert.equal(github.log.warn.mock.calls[1].arguments[0], 'Falling back to web-based GitHub Release.');
  });

  test('should release and upload assets', async t => {
    const options = {
      git,
      github: {
        pushRepo,
        tokenRef,
        release: true,
        releaseName: 'Release ${tagName}',
        releaseNotes: 'echo Custom notes',
        assets: 'test/resources/file-v${version}.txt'
      }
    };
    const github = await factory(GitHub, { options });

    const original = github.shell.exec.bind(github.shell);
    t.mock.method(github.shell, 'exec', (...args) => {
      if (args[0] === 'git log --pretty=format:"* %s (%h)" ${from}...${to}') return Promise.resolve('');
      if (args[0] === 'git describe --tags --match=* --abbrev=0') return Promise.resolve('2.0.1');
      return original(...args);
    });

    interceptAuthentication(api);
    interceptCollaborator(api);
    interceptCreate(api, { body: { tag_name: '2.0.2', name: 'Release 2.0.2', body: 'Custom notes' } });
    interceptAsset(assets, { body: '*' });

    await runTasks(github);

    const { isReleased, releaseUrl } = github.getContext();
    assert(isReleased);
    assert.equal(releaseUrl, 'https://github.com/user/repo/releases/tag/2.0.2');
  });

  test('should create a pre-release and draft release notes', async t => {
    const options = {
      git,
      github: {
        pushRepo,
        tokenRef,
        release: true,
        releaseName: 'Release ${tagName}',
        preRelease: true,
        draft: true
      }
    };
    const github = await factory(GitHub, { options });

    const original = github.shell.exec.bind(github.shell);
    t.mock.method(github.shell, 'exec', (...args) => {
      if (args[0] === 'git log --pretty=format:"* %s (%h)" ${from}...${to}') return Promise.resolve('');
      if (args[0] === 'git describe --tags --match=* --abbrev=0') return Promise.resolve('2.0.1');
      return original(...args);
    });

    interceptAuthentication(api);
    interceptCollaborator(api);
    interceptCreate(api, { body: { tag_name: '2.0.2', name: 'Release 2.0.2', prerelease: true, draft: true } });

    await runTasks(github);

    const { isReleased, releaseUrl } = github.getContext();
    assert(isReleased);
    assert.equal(releaseUrl, 'https://github.com/user/repo/releases/tag/2.0.2');
  });

  test('should create auto-generated release notes', async t => {
    const options = {
      git,
      github: {
        pushRepo,
        tokenRef,
        release: true,
        releaseName: 'Release ${tagName}',
        autoGenerate: true
      }
    };
    const github = await factory(GitHub, { options });

    const original = github.shell.exec.bind(github.shell);
    t.mock.method(github.shell, 'exec', (...args) => {
      if (args[0] === 'git describe --tags --match=* --abbrev=0') return Promise.resolve('2.0.1');
      return original(...args);
    });

    interceptAuthentication(api);
    interceptCollaborator(api);
    interceptCreate(api, {
      body: { tag_name: '2.0.2', name: 'Release 2.0.2', generate_release_notes: true, body: '' }
    });

    await runTasks(github);

    const { isReleased, releaseUrl } = github.getContext();
    assert(isReleased);
    assert.equal(releaseUrl, 'https://github.com/user/repo/releases/tag/2.0.2');
  });

  test('should update release and upload assets', async t => {
    const asset = 'file1';
    const options = {
      increment: false,
      git,
      github: {
        update: true,
        pushRepo,
        tokenRef,
        release: true,
        releaseName: 'Release ${tagName}',
        releaseNotes: 'echo Custom notes',
        assets: `test/resources/${asset}`
      }
    };
    const github = await factory(GitHub, { options });

    const original = github.shell.exec.bind(github.shell);
    t.mock.method(github.shell, 'exec', (...args) => {
      if (args[0] === 'git log --pretty=format:"* %s (%h)" ${from}...${to}') return Promise.resolve('');
      if (args[0] === 'git describe --tags --match=* --abbrev=0') return Promise.resolve('2.0.1');
      if (args[0] === 'git rev-list 2.0.1 --tags --max-count=1') return Promise.resolve('a123456');
      if (args[0] === 'git describe --tags --match=* --abbrev=0') return Promise.resolve('2.0.1');
      return original(...args);
    });

    interceptAuthentication(api);
    interceptCollaborator(api);
    interceptListReleases(api, { tag_name: '2.0.1' });
    interceptUpdate(api, { body: { tag_name: '2.0.1', name: 'Release 2.0.1', body: 'Custom notes' } });
    interceptAsset(assets, { body: asset });

    await runTasks(github);

    const { isReleased, releaseUrl } = github.getContext();
    assert(isReleased);
    assert.equal(releaseUrl, 'https://github.com/user/repo/releases/tag/2.0.1');
  });

  test('should create custom release notes using releaseNotes function', async t => {
    const options = {
      git,
      github: {
        pushRepo,
        tokenRef,
        release: true,
        releaseName: 'Release ${tagName}',
        releaseNotes(context) {
          return `Custom notes for tag ${context.tagName}`;
        }
      }
    };
    const github = await factory(GitHub, { options });

    const original = github.shell.exec.bind(github.shell);
    t.mock.method(github.shell, 'exec', (...args) => {
      if (args[0] === 'git describe --tags --match=* --abbrev=0') return Promise.resolve('2.0.1');
      return original(...args);
    });

    interceptAuthentication(api);
    interceptCollaborator(api);
    interceptCreate(api, {
      body: { tag_name: '2.0.2', name: 'Release 2.0.2', body: 'Custom notes for tag 2.0.2' }
    });

    await runTasks(github);

    const { isReleased, releaseUrl } = github.getContext();
    assert(isReleased);
    assert.equal(releaseUrl, 'https://github.com/user/repo/releases/tag/2.0.2');
  });

  test('should create new release for unreleased tag', async t => {
    const options = {
      increment: false,
      git,
      github: {
        update: true,
        pushRepo,
        tokenRef,
        release: true,
        releaseName: 'Release ${tagName}',
        releaseNotes: 'echo Custom notes'
      }
    };
    const github = await factory(GitHub, { options });

    const original = github.shell.exec.bind(github.shell);
    t.mock.method(github.shell, 'exec', (...args) => {
      if (args[0] === 'git log --pretty=format:"* %s (%h)" ${from}...${to}') return Promise.resolve('');
      if (args[0] === 'git describe --tags --match=* --abbrev=0') return Promise.resolve('2.0.1');
      if (args[0] === 'git rev-list 2.0.1 --tags --max-count=1') return Promise.resolve('b123456');
      if (args[0] === 'git describe --tags --abbrev=0 "b123456^"') return Promise.resolve('2.0.1');
      return original(...args);
    });

    interceptAuthentication(api);
    interceptCollaborator(api);
    interceptListReleases(api, { tag_name: '2.0.0' });
    interceptCreate(api, { body: { tag_name: '2.0.1', name: 'Release 2.0.1', body: 'Custom notes' } });

    await runTasks(github);

    const { isReleased, releaseUrl } = github.getContext();
    assert(isReleased);
    assert.equal(releaseUrl, 'https://github.com/user/repo/releases/tag/2.0.1');
  });

  test('should release to enterprise host', async t => {
    const options = { git, github: { tokenRef, pushRepo: 'git://github.example.org/user/repo' } };
    const github = await factory(GitHub, { options });

    const original = github.shell.exec.bind(github.shell);
    t.mock.method(github.shell, 'exec', (...args) => {
      if (args[0] === 'git remote get-url origin') return Promise.resolve(`https://github.example.org/user/repo`);
      if (args[0] === 'git config --get remote.origin.url')
        return Promise.resolve('https://github.example.org/user/repo');
      if (args[0] === 'git describe --tags --match=* --abbrev=0') return Promise.resolve('1.0.0');
      return original(...args);
    });

    interceptAuthentication(example);
    interceptCollaborator(example);
    interceptCreate(example, {
      api: 'https://github.example.org/api/v3',
      host: 'github.example.org',
      body: { tag_name: '1.0.1' }
    });

    await runTasks(github);

    const { isReleased, releaseUrl } = github.getContext();
    assert(isReleased);
    assert.equal(releaseUrl, 'https://github.example.org/user/repo/releases/tag/1.0.1');
  });

  test('should release to alternative host and proxy', async t => {
    const options = {
      git,
      github: {
        tokenRef,
        pushRepo: `git://custom.example.org/user/repo`,
        host: 'custom.example.org',
        proxy: 'http://proxy:8080'
      }
    };
    const github = await factory(GitHub, { options });

    const original = github.shell.exec.bind(github.shell);
    t.mock.method(github.shell, 'exec', (...args) => {
      if (args[0] === 'git log --pretty=format:"* %s (%h)" ${from}...${to}') return Promise.resolve('');
      if (args[0] === 'git describe --tags --match=* --abbrev=0') return Promise.resolve('1.0.0');
      return original(...args);
    });

    interceptAuthentication(custom);
    interceptCollaborator(custom);
    interceptCreate(custom, {
      api: 'https://custom.example.org/api/v3',
      host: 'custom.example.org',
      body: { tag_name: '1.0.1' }
    });

    await runTasks(github);

    const { isReleased, releaseUrl } = github.getContext();
    assert(isReleased);
    assert.equal(releaseUrl, 'https://custom.example.org/user/repo/releases/tag/1.0.1');
    assert.equal(github.options.proxy, 'http://proxy:8080');
  });

  test('should release to git.pushRepo', async t => {
    const options = { git: { pushRepo: 'upstream', changelog: '' }, github: { tokenRef, skipChecks: true } };
    const github = await factory(GitHub, { options });

    const original = github.shell.exec.bind(github.shell);
    t.mock.method(github.shell, 'exec', (...args) => {
      if (args[0] === 'git log --pretty=format:"* %s (%h)" ${from}...${to}') return Promise.resolve('');
      if (args[0] === 'git describe --tags --match=* --abbrev=0') return Promise.resolve('1.0.0');
      if (args[0] === 'git remote get-url upstream') return Promise.resolve('https://custom.example.org/user/repo');
      return original(...args);
    });

    interceptCreate(custom, {
      api: 'https://custom.example.org/api/v3',
      host: 'custom.example.org',
      body: { tag_name: '1.0.1' }
    });

    await runTasks(github);

    const { isReleased, releaseUrl } = github.getContext();
    assert(isReleased);
    assert.equal(releaseUrl, 'https://custom.example.org/user/repo/releases/tag/1.0.1');
  });

  const testSkipOnActions = process.env.GITHUB_ACTIONS ? test.skip : test;

  testSkipOnActions('should throw for unauthenticated user', async t => {
    const options = { github: { tokenRef, pushRepo, host } };
    const github = await factory(GitHub, { options });

    const getAuthenticated = t.mock.method(github.client.users, 'getAuthenticated', () => {
      throw new RequestError('Bad credentials', 401, requestErrorOptions);
    });

    await assert.rejects(runTasks(github), {
      message: /Could not authenticate with GitHub using environment variable "GITHUB_TOKEN"/
    });

    assert.equal(getAuthenticated.mock.callCount(), 1);
  });

  testSkipOnActions('should throw for non-collaborator', async t => {
    const options = { github: { tokenRef, pushRepo, host } };
    const github = await factory(GitHub, { options });

    t.mock.method(github.client.repos, 'checkCollaborator', () => {
      throw new RequestError('HttpError', 401, requestErrorOptions);
    });

    interceptAuthentication(api, { username: 'john' });

    await assert.rejects(runTasks(github), /User john is not a collaborator for user\/repo/);
  });

  test('should skip authentication and collaborator checks when running on GitHub Actions', async t => {
    const { GITHUB_ACTIONS, GITHUB_ACTOR } = process.env;
    if (!GITHUB_ACTIONS) {
      process.env.GITHUB_ACTIONS = 1;
      process.env.GITHUB_ACTOR = 'webpro';
    }

    const options = { github: { tokenRef } };
    const github = await factory(GitHub, { options });
    const authStub = t.mock.method(github, 'isAuthenticated');
    const collaboratorStub = t.mock.method(github, 'isCollaborator');

    await assert.doesNotReject(github.init());

    assert.equal(authStub.mock.callCount(), 0);
    assert.equal(collaboratorStub.mock.callCount(), 0);
    assert.equal(github.getContext('username'), process.env.GITHUB_ACTOR);

    if (!GITHUB_ACTIONS) {
      process.env.GITHUB_ACTIONS = GITHUB_ACTIONS || '';
      process.env.GITHUB_ACTOR = GITHUB_ACTOR || '';
    }
  });

  test('should handle octokit client error (without retries)', async t => {
    const github = await factory(GitHub, { options: { github: { tokenRef, pushRepo, host } } });
    const createRelease = t.mock.method(github.client.repos, 'createRelease', () => {
      throw new RequestError('Not found', 404, requestErrorOptions);
    });

    interceptAuthentication(api);
    interceptCollaborator(api);

    await assert.rejects(runTasks(github), /404 \(Not found\)/);

    assert.equal(createRelease.mock.callCount(), 1);
  });

  test('should handle octokit client error (with retries)', async t => {
    const options = { github: { tokenRef, pushRepo, host, retryMinTimeout: 0 } };
    const github = await factory(GitHub, { options });

    const createRelease = t.mock.method(github.client.repos, 'createRelease', () => {
      throw new RequestError('Request failed', 500, requestErrorOptions);
    });

    interceptAuthentication(api);
    interceptCollaborator(api);

    await assert.rejects(runTasks(github), /500 \(Request failed\)/);

    assert.equal(createRelease.mock.callCount(), 3);
  });

  test('should not call octokit client in dry run', async t => {
    const options = {
      'dry-run': true,
      git,
      github: { tokenRef, pushRepo, releaseName: 'R ${version}', assets: ['*'] }
    };
    const github = await factory(GitHub, { options });

    const get = t.mock.getter(github, 'client');
    const original = github.shell.exec.bind(github.shell);
    t.mock.method(github.shell, 'exec', (...args) => {
      if (args[0] === 'git log --pretty=format:"* %s (%h)" ${from}...${to}') return Promise.resolve('');
      if (args[0] === 'git describe --tags --match=* --abbrev=0') return Promise.resolve('v1.0.0');
      return original(...args);
    });

    await runTasks(github);

    assert.equal(get.mock.callCount(), 0);
    assert.equal(github.log.exec.mock.calls[1].arguments[0], 'octokit repos.createRelease "R 1.0.1" (v1.0.1)');
    assert.equal(github.log.exec.mock.calls.at(-1).arguments[0], 'octokit repos.uploadReleaseAssets');
    const { isReleased, releaseUrl } = github.getContext();
    assert(isReleased);
    assert.equal(releaseUrl, 'https://github.com/user/repo/releases/tag/v1.0.1');
  });

  test('should generate GitHub web release url', async t => {
    const options = {
      github: {
        pushRepo,
        release: true,
        web: true,
        releaseName: 'Release ${tagName}',
        releaseNotes: 'echo Custom notes'
      }
    };
    const github = await factory(GitHub, { options });

    const original = github.shell.exec.bind(github.shell);
    t.mock.method(github.shell, 'exec', (...args) => {
      if (args[0] === 'git log --pretty=format:"* %s (%h)" ${from}...${to}') return Promise.resolve('');
      if (args[0] === 'git describe --tags --match=* --abbrev=0') return Promise.resolve('2.0.1');
      return original(...args);
    });

    await runTasks(github);

    const { isReleased, releaseUrl } = github.getContext();
    assert(isReleased);
    assert.equal(
      releaseUrl,
      'https://github.com/user/repo/releases/new?tag=2.0.2&title=Release+2.0.2&body=Custom+notes&prerelease=false'
    );
  });

  test('should generate GitHub web release url for enterprise host', async t => {
    const options = {
      git,
      github: {
        pushRepo: 'git@custom.example.org:user/repo',
        release: true,
        web: true,
        host: 'custom.example.org',
        releaseName: 'The Launch',
        releaseNotes: 'echo It happened'
      }
    };
    const github = await factory(GitHub, { options });

    const original = github.shell.exec.bind(github.shell);
    t.mock.method(github.shell, 'exec', (...args) => {
      if (args[0] === 'git log --pretty=format:"* %s (%h)" ${from}...${to}') return Promise.resolve('');
      if (args[0] === 'git describe --tags --match=* --abbrev=0') return Promise.resolve('2.0.1');
      return original(...args);
    });

    await runTasks(github);

    const { isReleased, releaseUrl } = github.getContext();
    assert(isReleased);
    assert.equal(
      releaseUrl,
      'https://custom.example.org/user/repo/releases/new?tag=2.0.2&title=The+Launch&body=It+happened&prerelease=false'
    );
  });

  test.skip('should truncate long body', async t => {
    const releaseNotes = 'a'.repeat(125001);
    const body = 'a'.repeat(124000) + '...';
    const options = {
      git,
      github: {
        pushRepo,
        tokenRef,
        release: true,
        releaseName: 'Release ${tagName}',
        releaseNotes: 'echo ' + releaseNotes
      }
    };
    const github = await factory(GitHub, { options });

    const original = github.shell.exec.bind(github.shell);
    t.mock.method(github.shell, 'exec', (...args) => {
      if (args[0] === 'git log --pretty=format:"* %s (%h)" ${from}...${to}') return Promise.resolve('');
      if (args[0] === 'git describe --tags --match=* --abbrev=0') return Promise.resolve('2.0.1');
      return original(...args);
    });

    interceptAuthentication(api);
    interceptCollaborator(api);
    interceptCreate(api, { body: { tag_name: '2.0.2', name: 'Release 2.0.2', body } });

    await runTasks(github);

    const { isReleased, releaseUrl } = github.getContext();
    assert(isReleased);
    assert.equal(releaseUrl, 'https://github.com/user/repo/releases/tag/2.0.2');
  });

  test('should generate search queries correctly', () => {
    const generateCommit = () => Math.random().toString(36).substring(2, 9);
    const base = 'repo:owner/repo+type:pr+is:merged';
    const commits = Array.from({ length: 5 }, generateCommit);
    const separator = '+';

    const result = getSearchQueries(base, commits, separator);

    // Test case 1: Check if all commits are included in the search queries
    const allCommitsIncluded = commits.every(commit => result.some(query => query.includes(commit)));
    assert(allCommitsIncluded, 'All commits should be included in the search queries');

    assert.equal(
      commits.every(commit => result.some(query => query.includes(commit))),
      true
    );

    // Test case 2: Check if the function respects the 256 character limit
    const manyCommits = Array.from({ length: 100 }, generateCommit);
    const longResult = getSearchQueries(base, manyCommits, separator);
    assert(longResult.length > 1, 'Many commits should be split into multiple queries');
    assert(
      longResult.every(query => encodeURIComponent(query).length <= 256),
      'Each query should not exceed 256 characters after encoding'
    );
  });

  test('should create auto-generated discussion', async t => {
    const options = {
      git,
      github: {
        pushRepo,
        tokenRef,
        release: true,
        releaseName: 'Release ${tagName}',
        autoGenerate: false,
        discussionCategoryName: 'Announcement'
      }
    };
    const github = await factory(GitHub, { options });
    const original = github.shell.exec.bind(github.shell);
    t.mock.method(github.shell, 'exec', (...args) => {
      if (args[0] === 'git describe --tags --match=* --abbrev=0') return Promise.resolve('2.0.1');
      return original(...args);
    });

    interceptAuthentication(api);
    interceptCollaborator(api);
    interceptCreate(api, {
      body: {
        tag_name: '2.0.2',
        name: 'Release 2.0.2',
        generate_release_notes: false,
        body: null,
        discussion_category_name: 'Announcement'
      }
    });

    await runTasks(github);

    const { isReleased, releaseUrl, discussionUrl } = github.getContext();
    assert(isReleased);
    assert.equal(releaseUrl, 'https://github.com/user/repo/releases/tag/2.0.2');
    assert.equal(discussionUrl, 'https://github.com/user/repo/discussions/1');
  });
});
```

## File: `test/gitlab.js`
```javascript
import fs from 'node:fs';
import test, { before, after, afterEach, beforeEach, describe } from 'node:test';
import assert from 'node:assert/strict';
import { Agent } from 'undici';
import Git from '../lib/plugin/git/Git.js';
import GitLab from '../lib/plugin/gitlab/GitLab.js';
import { GitlabTestServer } from './util/https-server/server.js';
import { factory, runTasks } from './util/index.js';
import {
  interceptUser,
  interceptCollaborator,
  interceptPublish,
  interceptAsset,
  interceptAssetGeneric,
  interceptMilestones,
  interceptMembers
} from './stub/gitlab.js';
import { mockFetch } from './util/mock.js';

describe('GitLab', () => {
  const tokenHeader = 'Private-Token';
  const tokenRef = 'GITLAB_TOKEN';
  const certificateAuthorityFileRef = 'CI_SERVER_TLS_CA_FILE';

  const [mocker, api, example, local] = mockFetch([
    'https://gitlab.com/api/v4',
    'https://gitlab.example.org/api/v4',
    'https://localhost:3000/api/v4'
  ]);

  before(() => {
    mocker.mockGlobal();
  });

  let originalEnv;
  beforeEach(() => {
    originalEnv = process.env;
    process.env = { ...originalEnv };

    process.env[tokenRef] = '123';
  });

  afterEach(() => {
    if (originalEnv !== undefined) process.env = originalEnv;
    mocker.clearAll();
  });

  after(() => {
    mocker.unmockGlobal();
  });

  test('should validate token', async () => {
    const tokenRef = 'MY_GITLAB_TOKEN';
    const pushRepo = 'https://gitlab.com/user/repo';
    const options = { gitlab: { release: true, tokenRef, tokenHeader, pushRepo } };
    const gitlab = await factory(GitLab, { options });
    delete process.env[tokenRef];

    await assert.rejects(gitlab.init(), /Environment variable "MY_GITLAB_TOKEN" is required for GitLab releases/);

    process.env[tokenRef] = '123';

    interceptUser(api, { headers: { 'private-token': '123' } });
    interceptCollaborator(api, { headers: { 'private-token': '123' } });
    await assert.doesNotReject(gitlab.init());
  });

  test('should support CI Job token header', async () => {
    const tokenRef = 'CI_JOB_TOKEN';
    const tokenHeader = 'Job-Token';
    process.env[tokenRef] = 'j0b-t0k3n';
    const pushRepo = 'https://gitlab.com/user/repo';
    const options = { git: { pushRepo }, gitlab: { release: true, tokenRef, tokenHeader } };
    const gitlab = await factory(GitLab, { options });

    interceptPublish(api, { headers: { 'job-token': '1' } });

    await assert.doesNotReject(gitlab.init());

    delete process.env[tokenRef];
  });

  test('should upload assets and release', async t => {
    const pushRepo = 'https://gitlab.com/user/repo';
    const options = {
      git: { pushRepo },
      gitlab: {
        tokenRef,
        release: true,
        releaseName: 'Release ${version}',
        releaseNotes: 'echo Custom notes',
        assets: 'test/resources/file-v${version}.txt',
        milestones: ['${version}', '${latestVersion} UAT']
      }
    };
    const gitlab = await factory(GitLab, { options });
    t.mock.method(gitlab, 'getLatestVersion', () => Promise.resolve('2.0.0'));

    const git = await factory(Git);
    const ref = (await git.getBranchName()) ?? 'HEAD';

    interceptUser(api);
    interceptCollaborator(api);
    interceptMilestones(api, { query: { title: '2.0.1' }, milestones: [{ id: 17, iid: 3, title: '2.0.1' }] });
    interceptMilestones(api, { query: { title: '2.0.0 UAT' }, milestones: [{ id: 42, iid: 4, title: '2.0.0 UAT' }] });
    interceptAsset(api);
    interceptPublish(api, {
      body: {
        name: 'Release 2.0.1',
        ref,
        tag_name: '2.0.1',
        tag_message: 'Release 2.0.1',
        description: 'Custom notes',
        assets: {
          links: [
            { name: 'file-v2.0.1.txt', url: `${pushRepo}/uploads/7e8bec1fe27cc46a4bc6a91b9e82a07c/file-v2.0.1.txt` }
          ]
        },
        milestones: ['2.0.1', '2.0.0 UAT']
      }
    });

    await runTasks(gitlab);

    assert.equal(gitlab.assets[0].url, `${pushRepo}/uploads/7e8bec1fe27cc46a4bc6a91b9e82a07c/file-v2.0.1.txt`);
    const { isReleased, releaseUrl } = gitlab.getContext();
    assert(isReleased);
    assert.equal(releaseUrl, `${pushRepo}/-/releases/2.0.1`);
  });

  test('should upload assets with ID-based URLs', async t => {
    const host = 'https://gitlab.com';
    const pushRepo = `${host}/user/repo`;
    const options = {
      git: { pushRepo },
      gitlab: {
        tokenRef,
        release: true,
        assets: 'test/resources/file-v${version}.txt',
        useIdsForUrls: true
      }
    };

    const gitlab = await factory(GitLab, { options });
    t.mock.method(gitlab, 'getLatestVersion', () => Promise.resolve('2.0.0'));

    interceptUser(api);
    interceptCollaborator(api);
    interceptAsset(api);
    interceptPublish(api);

    await runTasks(gitlab);

    assert.equal(
      gitlab.assets[0].url,
      `${host}/-/project/1234/uploads/7e8bec1fe27cc46a4bc6a91b9e82a07c/file-v2.0.1.txt`
    );
  });

  test('should upload assets to generic repo', async t => {
    const host = 'https://gitlab.com';
    const pushRepo = `${host}/user/repo`;
    const options = {
      git: { pushRepo },
      gitlab: {
        tokenRef,
        release: true,
        assets: 'test/resources/file-v${version}.txt',
        useGenericPackageRepositoryForAssets: true,
        genericPackageRepositoryName: 'release-it'
      }
    };
    const gitlab = await factory(GitLab, { options });
    t.mock.method(gitlab, 'getLatestVersion', () => Promise.resolve('2.0.0'));

    interceptUser(api);
    interceptCollaborator(api);
    interceptAssetGeneric(api);
    interceptPublish(api);

    await runTasks(gitlab);

    assert.equal(
      gitlab.assets[0].url,
      `${host}/api/v4/projects/user%2Frepo/packages/generic/release-it/2.0.1/file-v2.0.1.txt`
    );
  });

  test('should throw when release milestone is missing', async t => {
    const pushRepo = 'https://gitlab.com/user/repo';
    const options = {
      git: { pushRepo },
      gitlab: {
        tokenRef,
        release: true,
        milestones: ['${version}', '${latestVersion} UAT']
      }
    };
    const gitlab = await factory(GitLab, { options });
    t.mock.method(gitlab, 'getLatestVersion', () => Promise.resolve('2.0.0'));

    interceptUser(api);
    interceptCollaborator(api);
    interceptMilestones(api, { query: { title: '2.0.1' }, milestones: [{ id: 17, iid: 3, title: '2.0.1' }] });
    interceptMilestones(api, { query: { title: '2.0.0 UAT' }, milestones: [] });

    await assert.rejects(
      runTasks(gitlab),
      /Missing one or more milestones in GitLab. Creating a GitLab release will fail./
    );
  });

  test('should release to self-managed host', async t => {
    const host = 'https://gitlab.example.org';
    const options = {
      git: { pushRepo: `${host}/user/repo` },
      gitlab: { releaseName: 'Release ${version}', releaseNotes: 'echo readme', tokenRef }
    };
    const gitlab = await factory(GitLab, { options });
    t.mock.method(gitlab, 'getLatestVersion', () => Promise.resolve('1.0.0'));

    interceptUser(example);
    interceptCollaborator(example);
    interceptPublish(example);

    await runTasks(gitlab);

    const { origin, baseUrl } = gitlab.getContext();
    assert.equal(origin, host);
    assert.equal(baseUrl, `${host}/api/v4`);
  });

  test('should release to sub-grouped repo', async () => {
    const options = { gitlab: { tokenRef }, git: { pushRepo: 'git@gitlab.com:group/sub-group/repo.git' } };
    const gitlab = await factory(GitLab, { options });

    interceptUser(api, { owner: 'sub-group' });
    interceptCollaborator(api, { owner: 'sub-group', group: 'group' });
    interceptPublish(api, { owner: 'group', project: 'sub-group%2Frepo' });

    await runTasks(gitlab);

    const { isReleased, releaseUrl } = gitlab.getContext();
    assert(isReleased);
    assert.match(releaseUrl, /https:\/\/gitlab.com\/group\/sub-group(\/|%2F)repo\/-\/releases\//);
  });

  test('should throw for unauthenticated user', async () => {
    const host = 'https://gitlab.com';
    const pushRepo = `${host}/user/repo`;
    const options = { gitlab: { tokenRef, pushRepo, host } };
    const gitlab = await factory(GitLab, { options });

    api.get('/user', { status: 401 });

    await assert.rejects(
      runTasks(gitlab),
      /Could not authenticate with GitLab using environment variable "GITLAB_TOKEN"/
    );
  });

  test('should throw for non-collaborator', async () => {
    const host = 'https://gitlab.com';
    const pushRepo = `${host}/john/repo`;
    const options = { gitlab: { tokenRef, pushRepo, host } };
    const gitlab = await factory(GitLab, { options });

    interceptMembers(api, { owner: 'emma' });
    interceptUser(api, { owner: 'john' });

    await assert.rejects(runTasks(gitlab), /User john is not a collaborator for john\/repo/);
  });

  test('should throw for insufficient access level', async () => {
    const host = 'https://gitlab.com';
    const pushRepo = `${host}/john/repo`;
    const options = { gitlab: { tokenRef, pushRepo, host } };
    const gitlab = await factory(GitLab, { options });

    interceptMembers(api, { owner: 'john', access_level: 10 });
    interceptUser(api, { owner: 'john' });

    await assert.rejects(runTasks(gitlab), /User john is not a collaborator for john\/repo/);
  });

  test('should not make requests in dry run', async t => {
    const [host, owner, repo] = ['https://gitlab.example.org', 'user', 'repo'];
    const pushRepo = `${host}/${owner}/${repo}`;
    const options = { 'dry-run': true, git: { pushRepo }, gitlab: { releaseName: 'R', tokenRef } };
    const gitlab = await factory(GitLab, { options });
    t.mock.method(gitlab, 'getLatestVersion', () => Promise.resolve('1.0.0'));

    await runTasks(gitlab);

    const { isReleased, releaseUrl } = gitlab.getContext();

    assert.equal(gitlab.log.exec.mock.calls[2].arguments[0], 'gitlab releases#uploadAssets');
    assert.equal(gitlab.log.exec.mock.calls[3].arguments[0], 'gitlab releases#createRelease "R" (1.0.1)');
    assert(isReleased);
    assert.equal(releaseUrl, `${pushRepo}/-/releases/1.0.1`);
  });

  test('should skip checks', async () => {
    const options = { gitlab: { tokenRef, skipChecks: true, release: true, milestones: ['v1.0.0'] } };
    const gitlab = await factory(GitLab, { options });

    await assert.doesNotReject(gitlab.init());
    await assert.doesNotReject(gitlab.beforeRelease());

    assert.equal(
      gitlab.log.exec.mock.calls
        .flatMap(call => call.arguments)
        .filter(entry => /checkReleaseMilestones/.test(entry[0])).length,
      0
    );
  });

  test('should not create fetch agent', async () => {
    const options = { gitlab: {} };
    const gitlab = await factory(GitLab, { options });

    assert.deepEqual(gitlab.certificateAuthorityOption, {});
  });

  test('should create fetch agent if secure == false', async () => {
    const options = { gitlab: { secure: false } };
    const gitlab = await factory(GitLab, { options });
    const { dispatcher } = gitlab.certificateAuthorityOption;

    assert(dispatcher instanceof Agent, "Fetch dispatcher should be an instance of undici's Agent class");

    const kOptions = Object.getOwnPropertySymbols(dispatcher).find(symbol => symbol.description === 'options');
    assert.deepEqual(dispatcher[kOptions].connect, { rejectUnauthorized: false, ca: undefined });
  });

  test('should create fetch agent if certificateAuthorityFile', async t => {
    const readFileSync = t.mock.method(fs, 'readFileSync', () => 'test certificate');

    const options = { gitlab: { certificateAuthorityFile: 'cert.crt' } };
    const gitlab = await factory(GitLab, { options });
    const { dispatcher } = gitlab.certificateAuthorityOption;

    assert(dispatcher instanceof Agent, "Fetch dispatcher should be an instance of undici's Agent class");

    const kOptions = Object.getOwnPropertySymbols(dispatcher).find(symbol => symbol.description === 'options');
    assert.deepEqual(dispatcher[kOptions].connect, { rejectUnauthorized: undefined, ca: 'test certificate' });

    readFileSync.mock.restore();
  });

  test('should create fetch agent if CI_SERVER_TLS_CA_FILE env is set', async t => {
    const readFileSync = t.mock.method(fs, 'readFileSync', () => 'test certificate');
    process.env[certificateAuthorityFileRef] = 'ca.crt';

    const options = { gitlab: {} };
    const gitlab = await factory(GitLab, { options });
    const { dispatcher } = gitlab.certificateAuthorityOption;

    assert(dispatcher instanceof Agent, "Fetch dispatcher should be an instance of undici's Agent class");

    const kOptions = Object.getOwnPropertySymbols(dispatcher).find(symbol => symbol.description === 'options');
    assert.deepEqual(dispatcher[kOptions].connect, { rejectUnauthorized: undefined, ca: 'test certificate' });

    readFileSync.mock.restore();
  });

  test('should create fetch agent if certificateAuthorityFileRef env is set', async t => {
    const readFileSync = t.mock.method(fs, 'readFileSync', () => 'test certificate');
    process.env['GITLAB_CA_FILE'] = 'custom-ca.crt';

    const options = { gitlab: { certificateAuthorityFileRef: 'GITLAB_CA_FILE' } };
    const gitlab = await factory(GitLab, { options });
    const { dispatcher } = gitlab.certificateAuthorityOption;

    assert(dispatcher instanceof Agent, "Fetch dispatcher should be an instance of undici's Agent class");

    const kOptions = Object.getOwnPropertySymbols(dispatcher).find(symbol => symbol.description === 'options');
    assert.deepEqual(dispatcher[kOptions].connect, { rejectUnauthorized: undefined, ca: 'test certificate' });

    readFileSync.mock.restore();
  });

  test('should throw for insecure connections to self-hosted instances', async t => {
    const host = 'https://localhost:3000';

    const options = {
      git: { pushRepo: `${host}/user/repo` },
      gitlab: { host, tokenRef, origin: host }
    };
    const gitlab = await factory(GitLab, { options });
    const server = new GitlabTestServer();

    t.after(async () => {
      await server.stop();
    });

    await server.run();

    await assert.rejects(gitlab.init(), /Could not authenticate with GitLab using environment variable "GITLAB_TOKEN"/);
  });

  test('should succesfully connect to self-hosted instance if insecure connection allowed', async t => {
    const host = 'https://localhost:3000';

    const options = {
      git: { pushRepo: `${host}/user/repo` },
      gitlab: {
        host,
        tokenRef,
        origin: host,
        secure: false
      }
    };
    const gitlab = await factory(GitLab, { options });
    const server = new GitlabTestServer();

    t.after(async () => {
      await server.stop();
    });

    await server.run();

    interceptUser(local);
    interceptCollaborator(local);

    await assert.doesNotReject(gitlab.init());
  });

  test('should succesfully connect to self-hosted instance with valid CA file', async t => {
    const host = 'https://localhost:3000';

    const options = {
      git: { pushRepo: `${host}/user/repo` },
      gitlab: {
        host,
        tokenRef,
        origin: host,
        certificateAuthorityFile: 'test/util/https-server/client/my-private-root-ca.cert.pem'
      }
    };
    const gitlab = await factory(GitLab, { options });
    const server = new GitlabTestServer();

    t.after(async () => {
      await server.stop();
    });

    await server.run();

    interceptUser(local);
    interceptCollaborator(local);

    await assert.doesNotReject(gitlab.init());
  });
});
```

## File: `test/log.js`
```javascript
import { EOL } from 'node:os';
import test, { describe } from 'node:test';
import assert from 'node:assert/strict';
import { stripVTControlCharacters } from 'node:util';
import mockStdIo from 'mock-stdio';
import Log from '../lib/log.js';

describe('log', () => {
  test('should write to stdout', () => {
    const log = new Log();
    mockStdIo.start();
    log.log('foo');
    const { stdout, stderr } = mockStdIo.end();
    assert.equal(stdout, 'foo\n');
    assert.equal(stderr, '');
  });

  test('should write to stderr', () => {
    const log = new Log();
    mockStdIo.start();
    log.error('foo');
    const { stdout, stderr } = mockStdIo.end();
    assert.equal(stdout, '');
    assert.equal(stripVTControlCharacters(stderr), 'ERROR foo\n');
  });

  test('should print info', () => {
    const log = new Log();
    mockStdIo.start();
    log.info('foo');
    const { stderr } = mockStdIo.end();
    assert.equal(stripVTControlCharacters(stderr), 'foo\n');
  });

  test('should print a warning', () => {
    const log = new Log();
    mockStdIo.start();
    log.warn('foo');
    const { stderr } = mockStdIo.end();
    assert.equal(stripVTControlCharacters(stderr), 'WARNING foo\n');
  });

  test('should print verbose', () => {
    const log = new Log({ isVerbose: true, verbosityLevel: 2 });
    mockStdIo.start();
    log.verbose('foo');
    const { stderr } = mockStdIo.end();
    assert.equal(stderr, 'foo\n');
  });

  test('should print external scripts verbose', () => {
    const log = new Log({ isVerbose: true });
    mockStdIo.start();
    log.verbose('foo', { isExternal: true });
    const { stderr } = mockStdIo.end();
    assert.equal(stderr, 'foo\n');
  });

  test('should always print external scripts verbose', () => {
    const log = new Log({ isVerbose: true, verbosityLevel: 2 });
    mockStdIo.start();
    log.verbose('foo', { isExternal: true });
    const { stderr } = mockStdIo.end();
    assert.equal(stderr, 'foo\n');
  });

  test('should not print verbose by default', () => {
    const log = new Log();
    mockStdIo.start();
    log.verbose('foo');
    const { stderr } = mockStdIo.end();
    assert.equal(stderr, '');
  });

  test('should not print command execution by default', () => {
    const log = new Log();
    mockStdIo.start();
    log.exec('foo');
    const { stderr } = mockStdIo.end();
    assert.equal(stderr.trim(), '');
  });

  test('should print command execution (verbose)', () => {
    const log = new Log({ isVerbose: true, verbosityLevel: 2 });
    mockStdIo.start();
    log.exec('foo');
    const { stderr } = mockStdIo.end();
    assert.equal(stderr.trim(), '$ foo');
  });

  test('should print command execution (verbose/dry run)', () => {
    const log = new Log({ isVerbose: true });
    mockStdIo.start();
    log.exec('foo', { isDryRun: true, isExternal: true });
    const { stderr } = mockStdIo.end();
    assert.equal(stderr.trim(), '! foo');
  });

  test('should print command execution (verbose/external)', () => {
    const log = new Log({ isVerbose: true });
    mockStdIo.start();
    log.exec('foo', { isExternal: true });
    const { stderr } = mockStdIo.end();
    assert.equal(stderr.trim(), '$ foo');
  });

  test('should print command execution (dry run)', () => {
    const log = new Log({ isDryRun: true });
    mockStdIo.start();
    log.exec('foo');
    const { stderr } = mockStdIo.end();
    assert.equal(stderr, '$ foo\n');
  });

  test('should print command execution (read-only)', () => {
    const log = new Log({ isDryRun: true });
    mockStdIo.start();
    log.exec('foo', 'bar', false);
    const { stderr } = mockStdIo.end();
    assert.equal(stderr, '$ foo bar\n');
  });

  test('should print command execution (write)', () => {
    const log = new Log({ isDryRun: true });
    mockStdIo.start();
    log.exec('foo', '--arg n', { isDryRun: true });
    const { stderr } = mockStdIo.end();
    assert.equal(stderr, '! foo --arg n\n');
  });

  test('should print obtrusive', () => {
    const log = new Log({ isCI: false });
    mockStdIo.start();
    log.obtrusive('spacious');
    const { stdout } = mockStdIo.end();
    assert.equal(stdout, '\nspacious\n\n');
  });

  test('should not print obtrusive in CI mode', () => {
    const log = new Log({ isCI: true });
    mockStdIo.start();
    log.obtrusive('normal');
    const { stdout } = mockStdIo.end();
    assert.equal(stdout, 'normal\n');
  });

  test('should print preview', () => {
    const log = new Log();
    mockStdIo.start();
    log.preview({ title: 'title', text: 'changelog' });
    const { stdout } = mockStdIo.end();
    assert.equal(stripVTControlCharacters(stdout), `Title:${EOL}changelog\n`);
  });
});
```

## File: `test/npm.js`
```javascript
import { join } from 'node:path';
import test, { describe } from 'node:test';
import assert from 'node:assert/strict';
import { writeFileSync } from 'node:fs';
import npm from '../lib/plugin/npm/npm.js';
import { factory, runTasks } from './util/index.js';
import { mkTmpDir, getArgs } from './util/helpers.js';

describe('npm', async () => {
  test('should return npm package url', async () => {
    const options = { npm: { name: 'my-cool-package' } };
    const npmClient = await factory(npm, { options });
    assert.equal(npmClient.getPackageUrl(), 'https://www.npmjs.com/package/my-cool-package');
  });

  test('should return npm package url (custom registry)', async () => {
    const options = { npm: { name: 'my-cool-package', publishConfig: { registry: 'https://registry.example.org/' } } };
    const npmClient = await factory(npm, { options });
    assert.equal(npmClient.getPackageUrl(), 'https://registry.example.org/package/my-cool-package');
  });

  test('should return npm package url (custom publicPath)', async () => {
    const options = { npm: { name: 'my-cool-package', publishConfig: { publicPath: '/custom/public-path' } } };
    const npmClient = await factory(npm, { options });
    assert.equal(npmClient.getPackageUrl(), 'https://www.npmjs.com/custom/public-path/my-cool-package');
  });

  test('should return npm package url (custom registry and publicPath)', async () => {
    const options = {
      npm: {
        name: 'my-cool-package',
        publishConfig: { registry: 'https://registry.example.org/', publicPath: '/custom/public-path' }
      }
    };
    const npmClient = await factory(npm, { options });
    assert.equal(npmClient.getPackageUrl(), 'https://registry.example.org/custom/public-path/my-cool-package');
  });

  test('should return default tag', async () => {
    const npmClient = await factory(npm);
    const tag = await npmClient.resolveTag();
    assert.equal(tag, 'latest');
  });

  test('should resolve default tag for pre-release', async t => {
    const npmClient = await factory(npm);
    t.mock.method(npmClient, 'getRegistryDistTags', () => ({}));
    const tag = await npmClient.resolveTag('1.0.0-0');
    assert.equal(tag, 'next');
  });

  test('should guess tag from registry for pre-release matching current version', async t => {
    const npmClient = await factory(npm);
    npmClient.setContext({ latestVersion: '1.0.0-0' });
    t.mock.method(npmClient, 'getRegistryDistTags', () => ({ latest: '0.9.0', alpha: '1.0.0-alpha.1', next: '1.0.0-0' }));
    const tag = await npmClient.resolveTag('1.0.0-1');
    assert.equal(tag, 'next');
  });

  test('should guess first pre-release tag from registry when no version match', async t => {
    const npmClient = await factory(npm);
    t.mock.method(npmClient, 'getRegistryDistTags', () => ({ latest: '0.9.0', alpha: '1.0.0-alpha.1' }));
    const tag = await npmClient.resolveTag('1.0.0-0');
    assert.equal(tag, 'alpha');
  });

  test('should derive tag from pre-release version', async () => {
    const npmClient = await factory(npm);
    const tag = await npmClient.resolveTag('1.0.2-alpha.3');
    assert.equal(tag, 'alpha');
  });

  test('should use provided (default) tag even for pre-release', async t => {
    const options = { npm: { tag: 'latest' } };
    const npmClient = await factory(npm, { options });
    t.mock.method(npmClient.shell, 'exec', () => Promise.resolve());
    await npmClient.bump('1.0.0-next.0');
    assert.equal(npmClient.getContext('tag'), 'latest');
  });

  test('should throw when `npm version` fails', async t => {
    const npmClient = await factory(npm);
    t.mock.method(npmClient.shell, 'exec', () =>
      Promise.reject(new Error('npm ERR! Version not changed, might want --allow-same-version'))
    );
    await assert.rejects(npmClient.bump('1.0.0-next.0'), { message: /Version not changed/ });
  });

  test('should return first pre-release tag from package in registry when resolving tag without pre-id', async t => {
    const npmClient = await factory(npm);
    const response = { latest: '1.4.1', alpha: '2.0.0-alpha.1', beta: '2.0.0-beta.3' };
    t.mock.method(npmClient.shell, 'exec', () => Promise.resolve(JSON.stringify(response)));
    assert.equal(await npmClient.resolveTag('2.0.0-5'), 'alpha');
  });

  test('should return default pre-release tag when resolving tag without pre-id', async t => {
    const npmClient = await factory(npm);
    const response = {
      latest: '1.4.1'
    };
    t.mock.method(npmClient.shell, 'exec', () => Promise.resolve(JSON.stringify(response)));
    assert.equal(await npmClient.resolveTag('2.0.0-0'), 'next');
  });

  test('should handle erroneous output when resolving tag without pre-id', async t => {
    const npmClient = await factory(npm);
    t.mock.method(npmClient.shell, 'exec', () => Promise.resolve(''));
    assert.equal(await npmClient.resolveTag('2.0.0-0'), 'next');
  });

  test('should handle errored request when resolving tag without pre-id', async t => {
    const npmClient = await factory(npm);
    t.mock.method(npmClient.shell, 'exec', () => Promise.resolve());
    assert.equal(await npmClient.resolveTag('2.0.0-0'), 'next');
  });

  test('should add registry to commands when specified', async t => {
    const npmClient = await factory(npm);
    npmClient.setContext({ publishConfig: { registry: 'registry.example.org' } });
    const exec = t.mock.method(npmClient.shell, 'exec', command => {
      if (command === 'npm whoami --registry registry.example.org') return Promise.resolve('john');
      const re = /npm access (list collaborators --json|ls-collaborators) release-it --registry registry.example.org/;
      if (re.test(command)) return Promise.resolve(JSON.stringify({ john: ['write'] }));
      return Promise.resolve();
    });

    await runTasks(npmClient);
    const commands = exec.mock.calls.map(c => c.arguments[0]);
    assert(commands.includes('npm ping --registry registry.example.org'));
    assert(commands.includes('npm whoami --registry registry.example.org'));
    assert(commands.some(c => /npm show release-it@[a-z]+ version --registry registry\.example\.org/.test(c)));
  });

  test('should not throw when executing tasks', async t => {
    const npmClient = await factory(npm);
    t.mock.method(npmClient.shell, 'exec', command => {
      if (command === 'npm whoami') return Promise.resolve('john');
      const re = /npm access (list collaborators --json|ls-collaborators) release-it/;
      if (re.test(command)) return Promise.resolve(JSON.stringify({ john: ['write'] }));
      return Promise.resolve();
    });
    await assert.doesNotReject(runTasks(npmClient));
  });

  test('should throw if npm is down', async t => {
    const npmClient = await factory(npm);
    t.mock.method(npmClient.shell, 'exec', command => {
      if (command === 'npm ping') return Promise.reject();
      return Promise.resolve();
    });
    await assert.rejects(runTasks(npmClient), { message: /^Unable to reach npm registry/ });
  });

  test('should not throw if npm returns 400/404 for unsupported ping/whoami/access', async t => {
    const npmClient = await factory(npm);
    const exec = t.mock.method(npmClient.shell, 'exec', () => Promise.resolve());
    const pingError = "npm ERR! code E404\nnpm ERR! 404 Package '--ping' not found : ping";
    const whoamiError = "npm ERR! code E404\nnpm ERR! 404 Package '--whoami' not found : whoami";
    const accessError = 'npm ERR! code E400\nnpm ERR! 400 Bad Request - GET https://npm.example.org/-/collaborators';
    exec.mock.mockImplementationOnce(() => Promise.reject(new Error(pingError)), 0);
    exec.mock.mockImplementationOnce(() => Promise.reject(new Error(whoamiError)), 1);
    exec.mock.mockImplementationOnce(() => Promise.reject(new Error(accessError)), 2);
    await runTasks(npmClient);
    assert.deepEqual(exec.mock.calls.at(-1).arguments[0], [
      'npm',
      'publish',
      '.',
      '--tag',
      'latest',
      '--workspaces=false'
    ]);
  });

  test('should not throw if npm returns 400 for unsupported ping/whoami/access', async t => {
    const npmClient = await factory(npm);
    const exec = t.mock.method(npmClient.shell, 'exec', () => Promise.resolve());
    const pingError = 'npm ERR! code E400\nnpm ERR! 400 Bad Request - GET https://npm.example.org/-/ping?write=true';
    const whoamiError = 'npm ERR! code E400\nnpm ERR! 400 Bad Request - GET https://npm.example.org/-/whoami';
    const accessError = 'npm ERR! code E400\nnpm ERR! 400 Bad Request - GET https://npm.example.org/-/collaborators';
    exec.mock.mockImplementationOnce(() => Promise.reject(new Error(pingError)), 0);
    exec.mock.mockImplementationOnce(() => Promise.reject(new Error(whoamiError)), 1);
    exec.mock.mockImplementationOnce(() => Promise.reject(new Error(accessError)), 2);
    await runTasks(npmClient);
    assert.deepEqual(exec.mock.calls.at(-1).arguments[0], [
      'npm',
      'publish',
      '.',
      '--tag',
      'latest',
      '--workspaces=false'
    ]);
  });

  test('should throw if user is not authenticated', async t => {
    const npmClient = await factory(npm);
    const exec = t.mock.method(npmClient.shell, 'exec', () => Promise.resolve());
    exec.mock.mockImplementationOnce(() => Promise.reject(), 1);
    await assert.rejects(runTasks(npmClient), { message: /^Not authenticated with npm/ });
  });

  test('should throw if user is not a collaborator (v9)', async t => {
    const npmClient = await factory(npm);
    t.mock.method(npmClient.shell, 'exec', command => {
      if (command === 'npm whoami') return Promise.resolve('ada');
      if (command === 'npm --version') return Promise.resolve('9.2.0');
      if (command === 'npm access list collaborators --json release-it')
        return Promise.resolve(JSON.stringify({ john: ['write'] }));
      return Promise.resolve();
    });
    await assert.rejects(runTasks(npmClient), { message: /^User ada is not a collaborator for release-it/ });
  });

  test('should throw if user is not a collaborator (v8)', async t => {
    const npmClient = await factory(npm);

    t.mock.method(npmClient.shell, 'exec', command => {
      if (command === 'npm whoami') return Promise.resolve('ada');
      if (command === 'npm --version') return Promise.resolve('8.2.0');
      const re = /npm access (list collaborators --json|ls-collaborators) release-it/;
      if (re.test(command)) return Promise.resolve(JSON.stringify({ john: ['write'] }));
      return Promise.resolve();
    });

    await assert.rejects(runTasks(npmClient), { message: /^User ada is not a collaborator for release-it/ });
  });

  test('should not throw if user is not a collaborator on a new package', async t => {
    const npmClient = await factory(npm);

    t.mock.method(npmClient.shell, 'exec', command => {
      if (command === 'npm whoami') return Promise.resolve('ada');
      const re = /npm access (list collaborators --json|ls-collaborators) release-it/;
      const message =
        'npm ERR! code E404\nnpm ERR! 404 Not Found - GET https://registry.npmjs.org/-/package/release-it/collaborators?format=cli - File not found';
      if (re.test(command)) return Promise.reject(new Error(message));
      return Promise.resolve();
    });

    await assert.doesNotReject(runTasks(npmClient));
  });

  test('should handle 2FA and publish with OTP', async t => {
    const npmClient = await factory(npm);
    npmClient.setContext({ name: 'pkg' });

    const exec = t.mock.method(npmClient.shell, 'exec');

    exec.mock.mockImplementationOnce(() => Promise.reject(new Error('Initial error with one-time pass.')), 0);
    exec.mock.mockImplementationOnce(() => Promise.reject(new Error('The provided one-time pass is incorrect.')), 1);
    exec.mock.mockImplementationOnce(() => Promise.resolve(), 2);

    await npmClient.publish({
      otpCallback: () =>
        npmClient.publish({
          otp: '123',
          otpCallback: () => npmClient.publish({ otp: '123456' })
        })
    });

    assert.equal(exec.mock.callCount(), 3);
    assert.deepEqual(exec.mock.calls[0].arguments[0], ['npm', 'publish', '.', '--tag', 'latest', '--workspaces=false']);
    assert.deepEqual(exec.mock.calls[1].arguments[0], [
      'npm',
      'publish',
      '.',
      '--tag',
      'latest',
      '--workspaces=false',
      '--otp',
      '123'
    ]);
    assert.deepEqual(exec.mock.calls[2].arguments[0], [
      'npm',
      'publish',
      '.',
      '--tag',
      'latest',
      '--workspaces=false',
      '--otp',
      '123456'
    ]);

    assert.equal(npmClient.log.warn.mock.callCount(), 1);
    assert.equal(npmClient.log.warn.mock.calls[0].arguments[0], 'The provided OTP is incorrect or has expired.');
  });

  test('should publish', async t => {
    const npmClient = await factory(npm);
    const exec = t.mock.method(npmClient.shell, 'exec', command => {
      if (command === 'npm whoami') return Promise.resolve('john');
      const re = /npm access (list collaborators --json|ls-collaborators) release-it/;
      if (re.test(command)) return Promise.resolve(JSON.stringify({ john: ['write'] }));
      return Promise.resolve();
    });
    await runTasks(npmClient);
    assert.deepEqual(exec.mock.calls.at(-1).arguments[0], [
      'npm',
      'publish',
      '.',
      '--tag',
      'latest',
      '--workspaces=false'
    ]);
  });

  test('should use extra publish arguments', async t => {
    const options = { npm: { skipChecks: true, publishArgs: '--registry=http://my-internal-registry.local' } };
    const npmClient = await factory(npm, { options });
    const exec = t.mock.method(npmClient.shell, 'exec', () => Promise.resolve());
    await runTasks(npmClient);
    assert.deepEqual(exec.mock.calls.at(-1).arguments[0], [
      'npm',
      'publish',
      '.',
      '--tag',
      'latest',
      '--workspaces=false',
      '--registry=http://my-internal-registry.local'
    ]);
  });

  test('should skip checks', async () => {
    const options = { npm: { skipChecks: true } };
    const npmClient = await factory(npm, { options });
    await assert.doesNotReject(npmClient.init());
  });

  test('should publish to a different/scoped registry', async t => {
    const tmp = mkTmpDir();
    process.chdir(tmp);
    writeFileSync(
      join(tmp, 'package.json'),
      JSON.stringify({
        name: '@my-scope/my-pkg',
        version: '1.0.0',
        publishConfig: {
          access: 'public',
          '@my-scope:registry': 'https://gitlab.com/api/v4/projects/my-scope%2Fmy-pkg/packages/npm/'
        }
      })
    );
    const options = { npm };
    const npmClient = await factory(npm, { options });
    const exec = t.mock.method(npmClient.shell, 'exec', command => {
      const cmd = 'npm whoami --registry https://gitlab.com/api/v4/projects/my-scope%2Fmy-pkg/packages/npm/';
      if (command === cmd) return Promise.resolve('john');
      const re =
        /npm access (list collaborators --json|ls-collaborators) @my-scope\/my-pkg --registry https:\/\/gitlab\.com\/api\/v4\/projects\/my-scope%2Fmy-pkg\/packages\/npm\//;
      if (re.test(command)) return Promise.resolve(JSON.stringify({ john: ['write'] }));
      return Promise.resolve();
    });
    await runTasks(npmClient);

    assert.deepEqual(getArgs(exec, 'npm'), [
      'npm ping --registry https://gitlab.com/api/v4/projects/my-scope%2Fmy-pkg/packages/npm/',
      'npm whoami --registry https://gitlab.com/api/v4/projects/my-scope%2Fmy-pkg/packages/npm/',
      'npm show @my-scope/my-pkg@latest version --registry https://gitlab.com/api/v4/projects/my-scope%2Fmy-pkg/packages/npm/',
      'npm --version',
      'npm version 1.0.1 --no-git-tag-version --workspaces=false',
      'npm publish . --tag latest --workspaces=false --registry https://gitlab.com/api/v4/projects/my-scope%2Fmy-pkg/packages/npm/'
    ]);
  });

  test('should not publish when `npm version` fails', async t => {
    const tmp = mkTmpDir();
    process.chdir(tmp);
    writeFileSync(join(tmp, 'package.json'), JSON.stringify({ name: '@my-scope/my-pkg', version: '1.0.0' }));
    const options = { npm };
    const npmClient = await factory(npm, { options });

    const exec = t.mock.method(npmClient.shell, 'exec', command => {
      if (command === 'npm whoami') return Promise.resolve('john');
      const re = /npm access (list collaborators --json|ls-collaborators) @my-scope\/my-pkg/;
      if (re.test(command)) return Promise.resolve(JSON.stringify({ john: ['write'] }));
      if (command === 'npm version 1.0.1 --no-git-tag-version --workspaces=false')
        return Promise.reject('npm ERR! Version not changed, might want --allow-same-version');
      return Promise.resolve();
    });

    await assert.rejects(runTasks(npmClient), /Version not changed/);

    assert.deepEqual(getArgs(exec, 'npm'), [
      'npm ping',
      'npm whoami',
      'npm show @my-scope/my-pkg@latest version',
      'npm --version',
      'npm version 1.0.1 --no-git-tag-version --workspaces=false'
    ]);
  });

  test('should add allow-same-version argument', async t => {
    const options = { npm: { skipChecks: true, allowSameVersion: true } };
    const npmClient = await factory(npm, { options });

    const exec = t.mock.method(npmClient.shell, 'exec', () => Promise.resolve());

    await runTasks(npmClient);
    const versionArgs = getArgs(exec, 'npm version');
    assert.match(versionArgs[0], / --allow-same-version/);
  });

  test('should add version arguments', async t => {
    const options = { npm: { skipChecks: true, versionArgs: ['--workspaces-update=false', '--allow-same-version'] } };
    const npmClient = await factory(npm, { options });
    const exec = t.mock.method(npmClient.shell, 'exec', () => Promise.resolve());
    await runTasks(npmClient);
    const versionArgs = getArgs(exec, 'npm version');
    assert.match(versionArgs[0], / --workspaces-update=false --allow-same-version/);
  });
});
```

## File: `test/plugin-name.js`
```javascript
import test from 'node:test';
import assert from 'node:assert/strict';
import { getPluginName } from '../lib/plugin/factory.js';

test('pluginName can return correct name for variants', async () => {
  assert.equal(getPluginName('plain-plugin'), 'plain-plugin');
  assert.equal(getPluginName('@some/scoped-plugin'), '@some/scoped-plugin');
  assert.equal(getPluginName('@some/nested/scoped-plugin'), '@some/nested/scoped-plugin');
  assert.equal(getPluginName('./relative-plugin.cjs'), 'relative-plugin');
});
```

## File: `test/plugins.js`
```javascript
import { resolve, join } from 'node:path';
import childProcess from 'node:child_process';
import fs, { appendFileSync, mkdirSync } from 'node:fs';
import test, { afterEach, describe } from 'node:test';
import assert from 'node:assert/strict';
import Config from '../lib/config.js';
import { execOpts, parseGitUrl } from '../lib/util.js';
import runTasks from '../lib/index.js';
import MyPlugin from './stub/plugin.js';
import ReplacePlugin from './stub/plugin-replace.js';
import ContextPlugin from './stub/plugin-context.js';
import { getArgs, mkTmpDir } from './util/helpers.js';
import ShellStub from './stub/shell.js';
import { LogStub, SpinnerStub } from './util/index.js';

describe('plugins', () => {
  const testConfig = {
    ci: true,
    config: false
  };

  const log = new LogStub();
  const spinner = new SpinnerStub();

  const getContainer = options => {
    const config = new Config(Object.assign({}, testConfig, options));
    const shell = new ShellStub({ container: { log, config } });
    return { log, spinner, config, shell };
  };

  childProcess.execSync('npm link', execOpts);

  afterEach(() => {
    log.resetCalls();
  });

  test('should instantiate plugins and execute all release-cycle methods', async () => {
    const pluginDir = mkTmpDir();
    const dir = mkTmpDir();
    process.chdir(pluginDir);

    appendFileSync(
      join(pluginDir, 'package.json'),
      JSON.stringify({ name: 'my-plugin', version: '1.0.0', type: 'module' })
    );
    childProcess.execSync(`npm link release-it`, execOpts);
    const content = "import { Plugin } from 'release-it'; " + MyPlugin.toString() + '; export default MyPlugin;';

    appendFileSync(join(pluginDir, 'index.js'), content);
    process.chdir(dir);
    mkdirSync(resolve('my/plugin'), { recursive: true });
    process.chdir('my/plugin');

    appendFileSync(join(dir, 'my', 'plugin', 'index.js'), content);
    process.chdir(dir);

    appendFileSync(join(dir, 'package.json'), JSON.stringify({ name: 'project', version: '1.0.0', type: 'module' }));
    childProcess.execSync(`npm install ${pluginDir}`, execOpts);
    childProcess.execSync(`npm link release-it`, execOpts);

    const config = {
      plugins: {
        'my-plugin': {
          name: 'foo'
        },
        './my/plugin/index.js': [
          'named-plugin',
          {
            name: 'bar'
          }
        ]
      }
    };
    const container = getContainer(config);

    const result = await runTasks({}, container);

    assert.deepEqual(
      container.log.info.mock.calls.map(call => call.arguments),
      [
        ['my-plugin:foo:init'],
        ['named-plugin:bar:init'],
        ['my-plugin:foo:getName'],
        ['my-plugin:foo:getLatestVersion'],
        ['my-plugin:foo:getIncrement'],
        ['my-plugin:foo:getIncrementedVersionCI'],
        ['named-plugin:bar:getIncrementedVersionCI'],
        ['my-plugin:foo:beforeBump'],
        ['named-plugin:bar:beforeBump'],
        ['my-plugin:foo:bump:1.3.0'],
        ['named-plugin:bar:bump:1.3.0'],
        ['my-plugin:foo:beforeRelease'],
        ['named-plugin:bar:beforeRelease'],
        ['my-plugin:foo:release'],
        ['named-plugin:bar:release'],
        ['my-plugin:foo:afterRelease'],
        ['named-plugin:bar:afterRelease']
      ]
    );

    assert.deepEqual(result, {
      changelog: undefined,
      name: 'new-project-name',
      latestVersion: '1.2.3',
      version: '1.3.0'
    });
  });

  test('should instantiate plugins and execute all release-cycle methods for scoped plugins', async () => {
    const pluginDir = mkTmpDir();
    const dir = mkTmpDir();
    process.chdir(pluginDir);

    fs.writeFileSync(
      join(pluginDir, 'package.json'),
      JSON.stringify({ name: '@scoped/my-plugin', version: '1.0.0', type: 'module' })
    );
    childProcess.execSync(`npm link release-it`, execOpts);
    const content = "import { Plugin } from 'release-it'; " + MyPlugin.toString() + '; export default MyPlugin;';

    fs.writeFileSync(join(pluginDir, 'index.js'), content);
    process.chdir(dir);

    fs.writeFileSync(join(dir, 'package.json'), JSON.stringify({ name: 'project', version: '1.0.0', type: 'module' }));
    childProcess.execSync(`npm install ${pluginDir}`, execOpts);
    childProcess.execSync(`npm link release-it`, execOpts);

    const config = {
      plugins: {
        '@scoped/my-plugin': {
          name: 'foo'
        }
      }
    };
    const container = getContainer(config);

    const result = await runTasks({}, container);

    assert.deepEqual(
      container.log.info.mock.calls.map(call => call.arguments),
      [
        ['@scoped/my-plugin:foo:init'],
        ['@scoped/my-plugin:foo:getName'],
        ['@scoped/my-plugin:foo:getLatestVersion'],
        ['@scoped/my-plugin:foo:getIncrement'],
        ['@scoped/my-plugin:foo:getIncrementedVersionCI'],
        ['@scoped/my-plugin:foo:beforeBump'],
        ['@scoped/my-plugin:foo:bump:1.3.0'],
        ['@scoped/my-plugin:foo:beforeRelease'],
        ['@scoped/my-plugin:foo:release'],
        ['@scoped/my-plugin:foo:afterRelease']
      ]
    );

    assert.deepEqual(result, {
      changelog: undefined,
      name: 'new-project-name',
      latestVersion: '1.2.3',
      version: '1.3.0'
    });
  });

  test('should disable core plugins', async () => {
    const dir = mkTmpDir();
    process.chdir(dir);

    fs.appendFileSync(join(dir, 'package.json'), JSON.stringify({ name: 'project', version: '1.0.0' }));
    const content =
      "import { Plugin } from 'release-it'; " + ReplacePlugin.toString() + '; export default ReplacePlugin;';

    fs.appendFileSync(join(dir, 'replace-plugin.mjs'), content);
    childProcess.execSync(`npm link release-it`, execOpts);

    const config = {
      plugins: {
        './replace-plugin.mjs': {}
      }
    };
    const container = getContainer(config);

    const result = await runTasks({}, container);

    assert.deepEqual(result, {
      changelog: undefined,
      name: undefined,
      latestVersion: '0.0.0',
      version: undefined
    });
  });

  test('should expose context to execute commands', async t => {
    const dir = mkTmpDir();
    process.chdir(dir);

    fs.appendFileSync(
      join(dir, 'package.json'),
      JSON.stringify({ name: 'pkg-name', version: '1.0.0', type: 'module' })
    );
    const content =
      "import { Plugin } from 'release-it'; " + ContextPlugin.toString() + '; export default ContextPlugin;';

    fs.appendFileSync(join(dir, 'context-plugin.js'), content);
    childProcess.execSync(`npm link release-it`, execOpts);

    const repo = parseGitUrl('https://github.com/user/pkg');

    const container = getContainer({ plugins: { './context-plugin.js': {} } });
    const exec = t.mock.method(container.shell, 'execFormattedCommand');

    container.config.setContext({ repo });
    container.config.setContext({ tagName: '1.0.1' });

    await runTasks({}, container);

    const pluginExecArgs = getArgs(exec, 'echo');

    assert.deepEqual(pluginExecArgs, [
      'echo false',
      'echo false',
      `echo pkg-name user 1.0.0 1.0.1`,
      `echo pkg-name user 1.0.0 1.0.1`,
      `echo user pkg user/pkg 1.0.1`,
      `echo user pkg user/pkg 1.0.1`,
      `echo user pkg user/pkg 1.0.1`,
      `echo user pkg user/pkg 1.0.1`,
      `echo pkg 1.0.0 1.0.1 1.0.1`,
      `echo pkg 1.0.0 1.0.1 1.0.1`,
      `echo pkg 1.0.0 1.0.1 1.0.1`,
      `echo pkg 1.0.0 1.0.1 1.0.1`
    ]);
  });
});
```

## File: `test/prompt.js`
```javascript
import test from 'node:test';
import assert from 'node:assert/strict';
import Prompt from '../lib/prompt.js';
import Config from '../lib/config.js';
import git from '../lib/plugin/git/prompts.js';
import github from '../lib/plugin/github/prompts.js';
import gitlab from '../lib/plugin/gitlab/prompts.js';
import npm from '../lib/plugin/npm/prompts.js';
import { factory } from './util/index.js';

const prompts = { git, github, gitlab, npm };

const yes = () => Promise.resolve(true);
const no = () => Promise.resolve(false);

test('should not create prompt if disabled', async t => {
  const task = t.mock.fn();
  const createPrompt = t.mock.fn(yes);
  const prompt = await factory(Prompt, { container: { createPrompt } });
  prompt.register(prompts.git);
  await prompt.show({ enabled: false, prompt: 'push', task });
  assert.equal(createPrompt.mock.callCount(), 0);
  assert.equal(task.mock.callCount(), 0);
});

test('should create prompt', async t => {
  const createPrompt = t.mock.fn(yes);
  const prompt = await factory(Prompt, { container: { createPrompt } });
  prompt.register(prompts.git);
  await prompt.show({ prompt: 'push' });
  assert.equal(createPrompt.mock.callCount(), 1);
  assert.equal(createPrompt.mock.calls[0].arguments[0], 'confirm');
  assert.deepEqual(createPrompt.mock.calls[0].arguments[1], {
    message: 'Push?',
    default: true
  });
});

[
  ['git', 'commit', 'Commit (Release 1.0.0)?'],
  ['git', 'tag', 'Tag (1.0.0)?'],
  ['git', 'push', 'Push?'],
  ['github', 'release', 'Create a pre-release on GitHub (Release 1.0.0)?'],
  ['gitlab', 'release', 'Create a release on GitLab (Release 1.0.0)?'],
  ['npm', 'publish', 'Publish my-pkg@next to npm?'],
  ['npm', 'otp', 'Please enter OTP for npm:']
].map(async ([namespace, prompt, message]) => {
  test(`should create prompt and render template message (${namespace}.${prompt})`, async t => {
    const createPrompt = t.mock.fn(yes);
    const config = new Config({
      isPreRelease: true,
      git: { tagName: 'v${version}' },
      npm: { name: 'my-pkg', tag: 'next' }
    });
    await config.init();
    config.setContext({ version: '1.0.0', tagName: '1.0.0' });
    const p = await factory(Prompt, { container: { createPrompt } });
    p.register(prompts[namespace], namespace);
    await p.show({ namespace, prompt, context: config.getContext() });
    assert.equal(createPrompt.mock.callCount(), 1);
    assert.equal(createPrompt.mock.calls[0].arguments[1].message, message);
  });
});

test('should execute task after positive answer', async t => {
  const task = t.mock.fn();
  const createPrompt = t.mock.fn(yes);
  const prompt = await factory(Prompt, { container: { createPrompt } });
  prompt.register(prompts.git);
  await prompt.show({ prompt: 'push', task });
  assert.equal(createPrompt.mock.callCount(), 1);
  assert.equal(task.mock.callCount(), 1);
  assert.equal(task.mock.calls[0].arguments[0], true);
});

test('should not execute task after negative answer', async t => {
  const task = t.mock.fn();
  const createPrompt = t.mock.fn(no);
  const prompt = await factory(Prompt, { container: { createPrompt } });
  prompt.register(prompts.git);
  await prompt.show({ prompt: 'push', task });
  assert.equal(createPrompt.mock.callCount(), 1);
  assert.equal(task.mock.callCount(), 0);
});
```

## File: `test/shell.js`
```javascript
import childProcess from 'node:child_process';
import test, { describe } from 'node:test';
import assert from 'node:assert/strict';
import Shell from '../lib/shell.js';
import { factory } from './util/index.js';

describe('shell', async () => {
  const cwd = childProcess.execSync('pwd', { encoding: 'utf8' }).trim();

  const shell = await factory(Shell);

  test('exec', async () => {
    assert.equal(await shell.exec('echo bar'), 'bar');
  });

  test('exec (with context)', async () => {
    const exec = cmd => shell.exec(cmd, { verbose: false }, shell.config.getContext());
    assert.equal(await exec(''), undefined);
    assert.equal(await exec('pwd'), cwd);
    assert.equal(await exec('echo ${git.pushArgs}'), '--follow-tags');
    assert.equal(await exec('echo -*- ${github.tokenRef} -*-'), '-*- GITHUB_TOKEN -*-');
  });

  test('exec (with args)', async () => {
    assert.equal(await shell.exec([]), undefined);
    assert.equal(await shell.exec(['pwd']), cwd);
    assert.equal(await shell.exec(['echo', 'a', 'b']), 'a b');
    assert.equal(await shell.exec(['echo', '"a"']), '"a"');
  });

  test('exec (dry-run/read-only)', async () => {
    const shell = await factory(Shell, { options: { 'dry-run': true } });
    {
      const actual = await shell.exec('pwd', { write: false });
      assert.equal(actual, cwd);
      assert.equal(shell.log.exec.mock.callCount(), 1);
      assert.equal(shell.log.exec.mock.calls[0].arguments[0], 'pwd');
    }
    {
      const actual = await shell.exec('pwd');
      assert.equal(actual, undefined);
      assert.equal(shell.log.exec.mock.callCount(), 2);
      assert.equal(shell.log.exec.mock.calls[1].arguments[0], 'pwd');
      assert.deepEqual(shell.log.exec.mock.calls[1].arguments.at(-1), { isDryRun: true });
    }
  });

  test('exec (verbose)', async () => {
    const shell = await factory(Shell, { options: { verbose: true } });
    const actual = await shell.exec('echo foo');
    assert.equal(shell.log.exec.mock.calls[0].arguments[0], 'echo foo');
    assert.equal(shell.log.exec.mock.callCount(), 1);
    assert.equal(shell.log.verbose.mock.calls[0].arguments[0], 'foo');
    assert.equal(shell.log.verbose.mock.callCount(), 1);
    assert.equal(actual, 'foo');
  });

  test('should cache results of command execution', async () => {
    const shell = await factory(Shell);
    const result1 = await shell.exec('echo foo');
    const result2 = await shell.exec('echo foo');
    assert(result1 === result2);
    assert.deepEqual(
      shell.log.exec.mock.calls.map(call => call.arguments),
      [
        ['echo foo', { isExternal: false, isCached: false }],
        ['echo foo', { isExternal: false, isCached: true }]
      ]
    );
  });

  test('should bail out on failed command execution', async () => {
    const shell = new Shell({ container: {} });
    await assert.rejects(shell.exec('foo'));
  });
});
```

## File: `test/spinner.js`
```javascript
import test from 'node:test';
import assert from 'node:assert/strict';
import Spinner from '../lib/spinner.js';
import Config from '../lib/config.js';

const getConfig = async options => {
  const testConfig = {
    ci: false,
    config: false
  };
  const config = new Config(Object.assign({}, testConfig, options));
  await config.init();

  return config;
};

test('should not show spinner and not execute task if disabled', async t => {
  const ora = t.mock.fn();
  const task = t.mock.fn();
  const spinner = new Spinner({ container: { ora } });
  await spinner.show({ enabled: false, task });
  assert.equal(task.mock.callCount(), 0);
  assert.equal(ora.mock.callCount(), 0);
});

test('should show spinner and run task by default', async t => {
  const ora = t.mock.fn();
  const task = t.mock.fn(() => Promise.resolve());
  const label = 'foo';
  const config = await getConfig({ ci: true });
  const spinner = new Spinner({ container: { ora, config } });
  await spinner.show({ task, label });
  assert.equal(task.mock.callCount(), 1);
  assert.equal(ora.mock.callCount(), 1);
  assert.equal(ora.mock.calls[0].arguments[0], task.mock.calls[0].result);
  assert.equal(ora.mock.calls[0].arguments[1], label);
});

test('should run task, but not show spinner if interactive', async t => {
  const ora = t.mock.fn();
  const task = t.mock.fn(() => Promise.resolve());
  const config = await getConfig({ ci: false });
  const spinner = new Spinner({ container: { ora, config } });
  await spinner.show({ task });
  assert.equal(task.mock.callCount(), 1);
  assert.equal(ora.mock.callCount(), 0);
});

test('should run task and show spinner if interactive, but external', async t => {
  const ora = t.mock.fn();
  const task = t.mock.fn(() => Promise.resolve());
  const config = await getConfig({ ci: false });
  const spinner = new Spinner({ container: { ora, config } });
  await spinner.show({ task, external: true });
  assert.equal(task.mock.callCount(), 1);
  assert.equal(ora.mock.callCount(), 1);
});
```

## File: `test/tasks.interactive.js`
```javascript
import path from 'node:path';
import { renameSync } from 'node:fs';
import childProcess from 'node:child_process';
import test, { afterEach, after, before, beforeEach, describe, mock } from 'node:test';
import assert from 'node:assert/strict';
import Prompt from '../lib/prompt.js';
import Config from '../lib/config.js';
import runTasks from '../lib/index.js';
import Git from '../lib/plugin/git/Git.js';
import { execOpts } from '../lib/util.js';
import { mkTmpDir, gitAdd, getArgs } from './util/helpers.js';
import ShellStub from './stub/shell.js';
import { interceptPublish as interceptGitLabPublish } from './stub/gitlab.js';
import { interceptCreate as interceptGitHubCreate } from './stub/github.js';
import { factory, LogStub, SpinnerStub } from './util/index.js';
import { mockFetch } from './util/mock.js';
import { createTarBlobByRawContents } from './util/fetch.js';

describe('tasks.interactive', () => {
  const [mocker, github, gitlab] = mockFetch(['https://api.github.com', 'https://gitlab.com/api/v4']);

  before(() => {
    mocker.mockGlobal();
  });

  afterEach(() => {
    mocker.clearAll();
    createPrompt.mock.resetCalls();
    log.resetCalls();
  });

  after(() => {
    mocker.unmockGlobal();
  });

  const testConfig = {
    ci: false,
    config: false
  };

  const getHooks = plugins => {
    const hooks = {};
    ['before', 'after'].forEach(prefix => {
      plugins.forEach(ns => {
        ['init', 'beforeBump', 'bump', 'beforeRelease', 'release', 'afterRelease'].forEach(lifecycle => {
          hooks[`${prefix}:${lifecycle}`] = `echo ${prefix}:${lifecycle}`;
          hooks[`${prefix}:${ns}:${lifecycle}`] = `echo ${prefix}:${ns}:${lifecycle}`;
        });
      });
    });
    return hooks;
  };

  const log = new LogStub();
  const spinner = new SpinnerStub();

  const createPrompt = mock.fn((type, options) => {
    if (type === 'list') return options.choices[0].value;
    if (type === 'input') return '0.0.1';
    return true;
  });

  const defaultCreatePrompt = createPrompt;

  const getContainer = (options, promptFn = defaultCreatePrompt) => {
    const config = new Config(Object.assign({}, testConfig, options));
    const shell = new ShellStub({ container: { log, config } });
    const prompt = new Prompt({ container: { createPrompt: promptFn } });
    return { log, spinner, config, shell, prompt };
  };

  let bare;
  let target;
  beforeEach(async () => {
    bare = mkTmpDir();
    target = mkTmpDir();
    process.chdir(bare);
    childProcess.execSync(`git init --bare .`, execOpts);
    childProcess.execSync(`git clone ${bare} ${target}`, execOpts);
    process.chdir(target);
    gitAdd('line', 'file', 'Add file');
  });

  test('should run tasks without throwing errors', async () => {
    renameSync('.git', 'foo');
    const { name, latestVersion, version } = await runTasks({}, getContainer());
    assert.equal(version, '0.0.1');
    assert(log.obtrusive.mock.calls[0].arguments[0].includes(`release ${name} (currently at ${latestVersion})`));
    assert.match(log.log.mock.calls.at(-1).arguments[0], /Done \(in [0-9]+s\.\)/);
  });

  test('should run tasks using extended configuration', async t => {
    renameSync('.git', 'foo');

    const validationExtendedConfiguration = "echo 'extended_configuration'";

    github.head('/repos/release-it/release-it-configuration/tarball/main', {
      status: 200,
      headers: {}
    });

    github.get('/repos/release-it/release-it-configuration/tarball/main', {
      status: 200,
      body: await new Response(
        createTarBlobByRawContents({
          '.release-it.json': JSON.stringify({
            hooks: {
              'before:init': validationExtendedConfiguration
            }
          })
        })
      ).arrayBuffer()
    });

    const config = {
      $schema: 'https://unpkg.com/release-it@20/schema/release-it.json',
      extends: 'github:release-it/release-it-configuration',
      config: true
    };

    const container = getContainer(config);

    const exec = t.mock.method(container.shell, 'execFormattedCommand');

    const { name, latestVersion, version } = await runTasks({}, container);

    const commands = getArgs(exec, 'echo');

    assert(commands.includes(validationExtendedConfiguration));

    assert.equal(version, '0.0.1');
    assert(log.obtrusive.mock.calls[0].arguments[0].includes(`release ${name} (currently at ${latestVersion})`));
    assert.match(log.log.mock.calls.at(-1).arguments[0], /Done \(in [0-9]+s\.\)/);
  });

  test('should run tasks not using extended configuration as it is not a string', async () => {
    renameSync('.git', 'foo');

    const config = {
      $schema: 'https://unpkg.com/release-it@20/schema/release-it.json',
      extends: false
    };

    const container = getContainer(config);

    const { name, latestVersion, version } = await runTasks({}, container);

    assert.equal(version, '0.0.1');
    assert(log.obtrusive.mock.calls[0].arguments[0].includes(`release ${name} (currently at ${latestVersion})`));
    assert.match(log.log.mock.calls.at(-1).arguments[0], /Done \(in [0-9]+s\.\)/);
  });

  test('should not run hooks for disabled release-cycle methods', async t => {
    const hooks = getHooks(['version', 'git', 'github', 'gitlab', 'npm']);

    const container = getContainer({
      hooks,
      git: { push: false },
      github: { release: false },
      gitlab: { release: false },
      npm: { publish: false }
    });

    const exec = t.mock.method(container.shell, 'execFormattedCommand');

    await runTasks({}, container);

    const commands = getArgs(exec, 'echo');

    assert(commands.includes('echo before:init'));
    assert(commands.includes('echo after:afterRelease'));

    assert(!commands.includes('echo after:git:release'));
    assert(!commands.includes('echo after:github:release'));
    assert(!commands.includes('echo after:gitlab:release'));
    assert(!commands.includes('echo after:npm:release'));
  });

  test('should not run hooks for cancelled release-cycle methods', async t => {
    const pkgName = path.basename(target);
    gitAdd(`{"name":"${pkgName}","version":"1.0.0"}`, 'package.json', 'Add package.json');
    childProcess.execSync('git tag 1.0.0', execOpts);

    const hooks = getHooks(['version', 'git', 'github', 'gitlab', 'npm']);
    const rejectAll = mock.fn(() => false);

    const container = getContainer(
      {
        increment: 'minor',
        hooks,
        github: { release: true, skipChecks: true },
        gitlab: { release: true, skipChecks: true },
        npm: { publish: true, skipChecks: true }
      },
      rejectAll
    );

    const exec = t.mock.method(container.shell, 'execFormattedCommand');

    await runTasks({}, container);

    const commands = getArgs(exec, 'echo');

    assert(commands.includes('echo before:init'));
    assert(commands.includes('echo after:afterRelease'));
    assert(commands.includes('echo after:git:bump'));
    assert(commands.includes('echo after:npm:bump'));

    assert(!commands.includes('echo after:git:release'));
    assert(!commands.includes('echo after:github:release'));
    assert(!commands.includes('echo after:gitlab:release'));
    assert(!commands.includes('echo after:npm:release'));
  });

  test('should run "after:*:release" plugin hooks', async t => {
    const project = path.basename(bare);
    const pkgName = path.basename(target);
    const owner = path.basename(path.dirname(bare));
    gitAdd(`{"name":"${pkgName}","version":"1.0.0"}`, 'package.json', 'Add package.json');
    childProcess.execSync('git tag 1.0.0', execOpts);
    const sha = gitAdd('line', 'file', 'More file');

    const git = await factory(Git);
    const ref = (await git.getBranchName()) ?? 'HEAD';

    interceptGitHubCreate(github, {
      owner,
      project,
      body: { tag_name: '1.1.0', name: 'Release 1.1.0', body: `* More file (${sha})` }
    });

    interceptGitLabPublish(gitlab, {
      owner,
      project,
      body: {
        name: 'Release 1.1.0',
        ref,
        tag_name: '1.1.0',
        tag_message: 'Release 1.1.0',
        description: `* More file (${sha})`
      }
    });

    const hooks = getHooks(['version', 'git', 'github', 'gitlab', 'npm']);

    const container = getContainer({
      increment: 'minor',
      hooks,
      github: { release: true, pushRepo: `https://github.com/${owner}/${project}`, skipChecks: true },
      gitlab: { release: true, pushRepo: `https://gitlab.com/${owner}/${project}`, skipChecks: true },
      npm: { name: pkgName, skipChecks: true }
    });

    const exec = t.mock.method(container.shell, 'execFormattedCommand');

    await runTasks({}, container);

    const commands = getArgs(exec, 'echo');

    assert(commands.includes('echo after:git:bump'));
    assert(commands.includes('echo after:npm:bump'));
    assert(commands.includes('echo after:git:release'));
    assert(commands.includes('echo after:github:release'));
    assert(commands.includes('echo after:gitlab:release'));
    assert(commands.includes('echo after:npm:release'));
  });

  test('should show only version prompt', async () => {
    const config = { ci: false, 'only-version': true };
    await runTasks({}, getContainer(config));
    assert.equal(createPrompt.mock.callCount(), 1);
    assert.equal(createPrompt.mock.calls[0].arguments[0], 'list');
  });
});
```

## File: `test/tasks.js`
```javascript
import path from 'node:path';
import childProcess from 'node:child_process';
import { appendFileSync, mkdirSync, renameSync } from 'node:fs';
import test, { after, afterEach, before, beforeEach, describe } from 'node:test';
import assert from 'node:assert/strict';
import semver from 'semver';
import Config from '../lib/config.js';
import runTasks from '../lib/index.js';
import Git from '../lib/plugin/git/Git.js';
import { execOpts } from '../lib/util.js';
import { mkTmpDir, gitAdd, getArgs } from './util/helpers.js';
import ShellStub from './stub/shell.js';
import {
  interceptUser as interceptGitLabUser,
  interceptCollaborator as interceptGitLabCollaborator,
  interceptPublish as interceptGitLabPublish,
  interceptAsset as interceptGitLabAsset
} from './stub/gitlab.js';
import {
  interceptAuthentication as interceptGitHubAuthentication,
  interceptCollaborator as interceptGitHubCollaborator,
  interceptCreate as interceptGitHubCreate,
  interceptAsset as interceptGitHubAsset
} from './stub/github.js';
import { factory, LogStub, SpinnerStub } from './util/index.js';
import { mockFetch } from './util/mock.js';

describe('tasks', () => {
  const rootDir = new URL('..', import.meta.url);

  const [mocker, github, assets, gitlab] = mockFetch([
    'https://api.github.com',
    'https://uploads.github.com',
    'https://gitlab.com/api/v4'
  ]);

  const npmMajorVersion = semver.major(process.env.npm_config_user_agent?.match(/npm\/([^ ]+)/)?.[1] ?? '10.0.0');

  const testConfig = {
    ci: true,
    config: false
  };

  const log = new LogStub();
  const spinner = new SpinnerStub();

  const getContainer = options => {
    const config = new Config(Object.assign({}, testConfig, options));
    const shell = new ShellStub({ container: { log, config } });
    return { log, spinner, config, shell };
  };

  before(() => {
    mocker.mockGlobal();
  });

  let bare;
  let target;
  beforeEach(async () => {
    bare = mkTmpDir();
    target = mkTmpDir();
    process.chdir(bare);
    childProcess.execSync(`git init --bare .`, execOpts);
    childProcess.execSync(`git clone ${bare} ${target}`, execOpts);
    process.chdir(target);
    gitAdd('line', 'file', 'Add file');
  });

  afterEach(() => {
    mocker.clearAll();
    log.resetCalls();
  });

  after(() => {
    mocker.unmockGlobal();
  });

  test('should run tasks without throwing errors', async () => {
    renameSync('.git', 'foo');
    const { name, latestVersion, version } = await runTasks({}, getContainer());
    assert(log.obtrusive.mock.calls[0].arguments[0].includes(`release ${name} (${latestVersion}...${version})`));
    assert.match(log.log.mock.calls.at(-1).arguments[0], /Done \(in [0-9]+s\.\)/);
  });

  test('should run tasks without package.json', async () => {
    childProcess.execSync('git tag 1.0.0', execOpts);
    gitAdd('line', 'file', 'Add file');
    const { name } = await runTasks({}, getContainer({ increment: 'major', git: { commit: false } }));
    assert(log.obtrusive.mock.calls[0].arguments[0].includes(`release ${name} (1.0.0...2.0.0)`));
    assert.match(log.log.mock.calls.at(-1).arguments[0], /Done \(in [0-9]+s\.\)/);
    assert.equal(log.warn.mock.callCount(), 0);
    const stdout = childProcess.execSync('git describe --tags --match=* --abbrev=0', {
      encoding: 'utf-8'
    });
    assert.equal(stdout.trim(), '2.0.0');
  });

  test('should disable plugins', async () => {
    gitAdd('{"name":"my-package","version":"1.2.3"}', 'package.json', 'Add package.json');
    childProcess.execSync('git tag 1.2.3', execOpts);
    gitAdd('line', 'file', 'Add file');
    const container = getContainer({ increment: 'minor', git: false, npm: false });
    const { latestVersion, version } = await runTasks({}, container);
    assert.equal(latestVersion, '0.0.0');
    assert.equal(version, '0.1.0');
    assert.match(log.log.mock.calls.at(-1).arguments[0], /Done \(in [0-9]+s\.\)/);
  });

  test('should run tasks with minimal config and without any warnings/errors', async () => {
    gitAdd('{"name":"my-package","version":"1.2.3"}', 'package.json', 'Add package.json');
    childProcess.execSync('git tag 1.2.3', execOpts);
    gitAdd('line', 'file', 'More file');
    await runTasks({}, getContainer({ increment: 'patch' }));
    assert(log.obtrusive.mock.calls[0].arguments[0].includes('release my-package (1.2.3...1.2.4)'));
    assert.match(log.log.mock.calls.at(-1).arguments[0], /Done \(in [0-9]+s\.\)/);
    const stdout = childProcess.execSync('git describe --tags --match=* --abbrev=0', { encoding: 'utf-8' });
    assert.equal(stdout.trim(), '1.2.4');
  });

  test('should use pkg.version', async () => {
    gitAdd('{"name":"my-package","version":"1.2.3"}', 'package.json', 'Add package.json');
    await runTasks({}, getContainer({ increment: 'minor' }));
    assert(log.obtrusive.mock.calls[0].arguments[0].includes('release my-package (1.2.3...1.3.0)'));
    assert.match(log.log.mock.calls.at(-1).arguments[0], /Done \(in [0-9]+s\.\)/);
    const stdout = childProcess.execSync('git describe --tags --match=* --abbrev=0', { encoding: 'utf-8' });
    assert.equal(stdout.trim(), '1.3.0');
  });

  test('should use pkg.version (in sub dir) w/o tagging repo', async t => {
    gitAdd('{"name":"root-package","version":"1.0.0"}', 'package.json', 'Add package.json');
    childProcess.execSync('git tag 1.0.0', execOpts);
    mkdirSync('my-package');
    process.chdir('my-package');
    gitAdd('{"name":"my-package","version":"1.2.3"}', 'package.json', 'Add package.json');
    const container = getContainer({ increment: 'minor', git: { tag: false } });
    const exec = t.mock.method(container.shell, 'exec');
    await runTasks({}, container);
    assert(log.obtrusive.mock.calls[0].arguments[0].endsWith('release my-package (1.2.3...1.3.0)'));
    assert.match(log.log.mock.calls.at(-1).arguments[0], /Done \(in [0-9]+s\.\)/);
    const stdout = childProcess.execSync('git describe --tags --match=* --abbrev=0', { encoding: 'utf-8' });
    assert.equal(stdout.trim(), '1.0.0');
    const npmArgs = getArgs(exec, 'npm');
    assert.equal(npmArgs[5], 'npm version 1.3.0 --no-git-tag-version --workspaces=false');
  });

  test('should ignore version in pkg.version and use git tag instead', async () => {
    gitAdd('{"name":"my-package","version":"0.0.0"}', 'package.json', 'Add package.json');
    childProcess.execSync('git tag 1.1.1', execOpts);
    gitAdd('line', 'file', 'More file');
    await runTasks({}, getContainer({ increment: 'minor', npm: { ignoreVersion: true } }));
    assert(log.obtrusive.mock.calls[0].arguments[0].includes('release my-package (1.1.1...1.2.0)'));
    assert.match(log.log.mock.calls.at(-1).arguments[0], /Done \(in [0-9]+s\.\)/);
    const stdout = childProcess.execSync('git describe --tags --match=* --abbrev=0', { encoding: 'utf-8' });
    assert.equal(stdout.trim(), '1.2.0');
  });

  test('should release all the things (basic)', async t => {
    const project = path.basename(bare);
    const pkgName = path.basename(target);
    const owner = path.basename(path.dirname(bare));
    gitAdd(`{"name":"${pkgName}","version":"1.0.0"}`, 'package.json', 'Add package.json');
    childProcess.execSync('git tag 1.0.0', execOpts);
    const sha = gitAdd('line', 'file', 'More file');

    interceptGitHubAuthentication(github);
    interceptGitHubCollaborator(github, { owner, project });
    interceptGitHubCreate(github, {
      owner,
      project,
      body: { tag_name: '1.0.1', name: 'Release 1.0.1', body: `* More file (${sha})`, prerelease: false }
    });

    const container = getContainer({
      github: { release: true, pushRepo: `https://github.com/${owner}/${project}` },
      npm: { name: pkgName }
    });

    const exec = t.mock.method(container.shell, 'exec');

    await runTasks({}, container);

    const npmArgs = getArgs(exec, 'npm');

    assert.deepEqual(npmArgs, [
      'npm ping',
      'npm whoami',
      `npm show ${pkgName}@latest version`,
      'npm --version',
      `npm access ${npmMajorVersion >= 9 ? 'list collaborators --json' : 'ls-collaborators'} ${pkgName}`,
      'npm version 1.0.1 --no-git-tag-version --workspaces=false',
      'npm publish . --tag latest --workspaces=false'
    ]);

    assert(log.obtrusive.mock.calls[0].arguments[0].endsWith(`release ${pkgName} (1.0.0...1.0.1)`));
    assert(log.log.mock.calls[0].arguments[0].endsWith(`https://www.npmjs.com/package/${pkgName}`));
    assert(log.log.mock.calls[1].arguments[0].endsWith(`https://github.com/${owner}/${project}/releases/tag/1.0.1`));
  });

  test('should release with correct tag name', async t => {
    const project = path.basename(bare);
    const pkgName = path.basename(target);
    const owner = path.basename(path.dirname(bare));
    const stdout = childProcess.execSync('git rev-parse --abbrev-ref HEAD', { encoding: 'utf-8' });
    const branchName = stdout.trim();
    gitAdd(`{"name":"${pkgName}","version":"1.0.0"}`, 'package.json', 'Add package.json');
    childProcess.execSync(`git tag ${pkgName}-${branchName}-1.0.0`, execOpts);
    const sha = gitAdd('line', 'file', 'More file');

    interceptGitHubCreate(github, {
      owner,
      project,
      body: {
        tag_name: `${pkgName}-${branchName}-1.0.1`,
        name: 'Release 1.0.1',
        body: `* More file (${sha})`,
        prerelease: false
      }
    });

    const container = getContainer({
      git: { tagName: '${npm.name}-${branchName}-${version}' },
      github: { release: true, skipChecks: true, pushRepo: `https://github.com/${owner}/${project}` }
    });

    const exec = t.mock.method(container.shell, 'exec');

    await runTasks({}, container);

    const gitArgs = getArgs(exec, 'git');

    assert(gitArgs.includes(`git tag --annotate --message Release 1.0.1 ${pkgName}-${branchName}-1.0.1`));
    assert(
      log.log.mock.calls[1].arguments[0].endsWith(`/${owner}/${project}/releases/tag/${pkgName}-${branchName}-1.0.1`)
    );
  });

  test('should release all the things (pre-release, github, gitlab)', async t => {
    const project = path.basename(bare);
    const pkgName = path.basename(target);
    const owner = path.basename(path.dirname(bare));
    const url = `https://gitlab.com/${owner}/${project}`;
    gitAdd(`{"name":"${pkgName}","version":"1.0.0"}`, 'package.json', 'Add package.json');
    childProcess.execSync('git tag v1.0.0', execOpts);
    const sha = gitAdd('line', 'file', 'More file');
    childProcess.execSync('git push --follow-tags', execOpts);
    const git = await factory(Git);
    const ref = (await git.getBranchName()) ?? 'HEAD';

    interceptGitHubAuthentication(github);
    interceptGitHubCollaborator(github, { owner, project });
    interceptGitHubAsset(assets, { owner, project, body: 'lineline' });
    interceptGitHubCreate(github, {
      owner,
      project,
      body: {
        tag_name: 'v1.1.0-alpha.0',
        name: 'Release 1.1.0-alpha.0',
        body: `Notes for ${pkgName} [v1.1.0-alpha.0]: ${sha}`,
        prerelease: true
      }
    });

    interceptGitLabUser(gitlab, { owner });
    interceptGitLabCollaborator(gitlab, { owner, project });
    interceptGitLabAsset(gitlab, { owner, project });
    interceptGitLabPublish(gitlab, {
      owner,
      project,
      body: {
        name: 'Release 1.1.0-alpha.0',
        ref,
        tag_name: 'v1.1.0-alpha.0',
        tag_message: `${owner} ${owner}/${project} ${project}`,
        description: `Notes for ${pkgName}: ${sha}`,
        assets: {
          links: [
            {
              name: 'file',
              url: `${url}/uploads/7e8bec1fe27cc46a4bc6a91b9e82a07c/file`
            }
          ]
        }
      }
    });

    const container = getContainer({
      increment: 'minor',
      preRelease: 'alpha',
      git: {
        changelog: 'git log --pretty=format:%h ${latestTag}...HEAD',
        commitMessage: 'Release ${version} for ${name} (from ${latestVersion})',
        tagAnnotation: '${repo.owner} ${repo.repository} ${repo.project}'
      },
      github: {
        release: true,
        pushRepo: `https://github.com/${owner}/${project}`,
        releaseNotes: 'echo Notes for ${name} [v${version}]: ${changelog}',
        assets: ['file']
      },
      gitlab: {
        release: true,
        pushRepo: url,
        releaseNotes: 'echo Notes for ${name}: ${changelog}',
        assets: ['file']
      },
      npm: { name: pkgName }
    });

    const exec = t.mock.method(container.shell, 'exec');

    process.env['GITLAB_TOKEN'] = '123';

    await runTasks({}, container);

    const npmArgs = getArgs(exec, 'npm');

    assert.deepEqual(npmArgs, [
      'npm ping',
      'npm whoami',
      `npm show ${pkgName}@latest version`,
      'npm --version',
      `npm access ${npmMajorVersion >= 9 ? 'list collaborators --json' : 'ls-collaborators'} ${pkgName}`,
      'npm version 1.1.0-alpha.0 --no-git-tag-version --workspaces=false',
      'npm publish . --tag alpha --workspaces=false'
    ]);

    const commitMessage = childProcess.execSync('git log --oneline --format=%B -n 1 HEAD', {
      encoding: 'utf-8'
    });
    assert.equal(commitMessage.trim(), `Release 1.1.0-alpha.0 for ${pkgName} (from 1.0.0)`);

    const tagName = childProcess.execSync('git describe --tags --match=* --abbrev=0', { encoding: 'utf-8' });
    assert.equal(tagName.trim(), 'v1.1.0-alpha.0');

    const tagAnnotation = childProcess.execSync('git for-each-ref refs/tags/v1.1.0-alpha.0 --format="%(contents)"', {
      encoding: 'utf-8'
    });
    assert.equal(tagAnnotation.trim(), `${owner} ${owner}/${project} ${project}`);

    assert(log.obtrusive.mock.calls[0].arguments[0].endsWith(`release ${pkgName} (1.0.0...1.1.0-alpha.0)`));
    assert(log.log.mock.calls[0].arguments[0].endsWith(`https://www.npmjs.com/package/${pkgName}`));
    assert(log.log.mock.calls[1].arguments[0].endsWith(`/${owner}/${project}/releases/tag/v1.1.0-alpha.0`));
    assert(log.log.mock.calls[2].arguments[0].endsWith(`/${project}/-/releases/v1.1.0-alpha.0`));
    assert.match(log.log.mock.calls.at(-1).arguments[0], /Done \(in [0-9]+s\.\)/);
  });

  test('should publish pre-release without pre-id with different npm.tag', async t => {
    const pkgName = path.basename(target);
    gitAdd(`{"name":"${pkgName}","version":"1.0.0"}`, 'package.json', 'Add package.json');
    childProcess.execSync('git tag v1.0.0', execOpts);

    const container = getContainer({ increment: 'major', preRelease: true, npm: { name: pkgName, tag: 'next' } });
    const exec = t.mock.method(container.shell, 'exec');

    await runTasks({}, container);

    const npmArgs = getArgs(exec, 'npm');
    assert.deepEqual(npmArgs, [
      'npm ping',
      'npm whoami',
      `npm show ${pkgName}@latest version`,
      'npm --version',
      `npm access ${npmMajorVersion >= 9 ? 'list collaborators --json' : 'ls-collaborators'} ${pkgName}`,
      'npm version 2.0.0-0 --no-git-tag-version --workspaces=false',
      'npm publish . --tag next --workspaces=false'
    ]);

    const stdout = childProcess.execSync('git describe --tags --match=* --abbrev=0', { encoding: 'utf-8' });
    assert.equal(stdout.trim(), 'v2.0.0-0');
    assert(log.obtrusive.mock.calls[0].arguments[0].endsWith(`release ${pkgName} (1.0.0...2.0.0-0)`));
    assert(log.log.mock.calls[0].arguments[0].endsWith(`https://www.npmjs.com/package/${pkgName}`));
    assert.match(log.log.mock.calls.at(-1).arguments[0], /Done \(in [0-9]+s\.\)/);
  });

  test('should handle private package correctly, bump lockfile', async t => {
    const pkgName = path.basename(target);
    gitAdd(`{"name":"${pkgName}","version":"1.0.0","private":true}`, 'package.json', 'Add package.json');
    gitAdd(`{"name":"${pkgName}","version":"1.0.0","private":true}`, 'package-lock.json', 'Add package-lock.json');

    const container = getContainer({ npm: { name: pkgName, private: true } });
    const exec = t.mock.method(container.shell, 'exec');

    await runTasks({}, container);

    const npmArgs = getArgs(exec, 'npm');
    assert.deepEqual(npmArgs, ['npm version 1.0.1 --no-git-tag-version --workspaces=false']);
    assert(log.obtrusive.mock.calls[0].arguments[0].endsWith(`release ${pkgName} (1.0.0...1.0.1)`));
    assert.equal(log.warn.length, 0);
    assert.match(log.log.mock.calls[0].arguments[0], /Done \(in [0-9]+s\.\)/);
  });

  test('should initially publish non-private scoped npm package privately', async t => {
    const pkgName = path.basename(target);
    gitAdd(`{"name":"@scope/${pkgName}","version":"1.0.0"}`, 'package.json', 'Add package.json');

    const container = getContainer({ npm: { name: pkgName } });

    const original = container.shell.exec.bind(container.shell);
    const exec = t.mock.method(container.shell, 'exec', (...args) => {
      if (args[0] === `npm show @scope/${pkgName}@latest version`) return Promise.reject();
      return original(...args);
    });

    await runTasks({}, container);

    const npmArgs = getArgs(exec, 'npm');
    assert.equal(npmArgs[6], 'npm publish . --tag latest --workspaces=false');
  });

  test('should use pkg.publishConfig.registry', async t => {
    const pkgName = path.basename(target);
    const registry = 'https://my-registry.example.org';

    gitAdd(
      JSON.stringify({
        name: pkgName,
        version: '1.2.3',
        publishConfig: { registry }
      }),
      'package.json',
      'Add package.json'
    );

    const container = getContainer();

    const exec = t.mock.method(container.shell, 'exec');

    await runTasks({}, container);

    const npmArgs = getArgs(exec, 'npm');
    assert.equal(npmArgs[0], `npm ping --registry ${registry}`);
    assert.equal(npmArgs[1], `npm whoami --registry ${registry}`);
    assert(container.log.log.mock.calls[0].arguments[0].endsWith(`${registry}/package/${pkgName}`));
  });

  test('should propagate errors', async () => {
    const config = {
      hooks: {
        'before:init': 'some-failing-command'
      }
    };
    const container = getContainer(config);

    await assert.rejects(runTasks({}, container), { message: /some-failing-command/ });

    assert.equal(log.error.mock.callCount(), 1);
  });

  test('should use custom changelog command with context', async t => {
    const project = path.basename(bare);
    const owner = path.basename(path.dirname(bare));
    childProcess.execSync('git tag v1.0.0', execOpts);
    gitAdd('line', 'file', 'More file');

    interceptGitHubAuthentication(github);
    interceptGitHubCollaborator(github, { owner, project });
    interceptGitHubCreate(github, {
      owner,
      project,
      body: {
        tag_name: 'v1.1.0',
        name: 'Release 1.1.0',
        body: 'custom-changelog-generator --from=v1.0.0 --to=v1.1.0',
        draft: false,
        prerelease: false
      }
    });

    const container = getContainer({
      increment: 'minor',
      github: {
        release: true,
        releaseNotes: 'echo custom-changelog-generator --from=${latestTag} --to=${tagName}',
        pushRepo: `https://github.com/${owner}/${project}`
      }
    });

    const exec = t.mock.method(container.shell, 'execStringCommand');

    await runTasks({}, container);

    const command = exec.mock.calls
      .map(call => call.arguments)
      .find(([command]) => command.includes('custom-changelog-generator'));

    assert.equal(command[0], 'echo custom-changelog-generator --from=v1.0.0 --to=v1.1.0');
  });

  test('should run all hooks', async t => {
    gitAdd(`{"name":"hooked","version":"1.0.0","type":"module"}`, 'package.json', 'Add package.json');
    childProcess.execSync(`npm install ${rootDir}`, execOpts);
    const plugin = "import { Plugin } from 'release-it'; class MyPlugin extends Plugin {}; export default MyPlugin;";

    appendFileSync('my-plugin.js', plugin);
    const hooks = {};
    ['before', 'after'].forEach(prefix => {
      ['version', 'git', 'npm', 'my-plugin'].forEach(ns => {
        ['init', 'beforeBump', 'bump', 'beforeRelease', 'release', 'afterRelease'].forEach(cycle => {
          hooks[`${prefix}:${cycle}`] = `echo ${prefix}:${cycle}`;
          hooks[`${prefix}:${ns}:${cycle}`] = `echo ${prefix}:${ns}:${cycle}`;
        });
      });
    });
    const container = getContainer({
      plugins: { './my-plugin.js': {} },
      git: { requireCleanWorkingDir: false },
      hooks
    });
    const exec = t.mock.method(container.shell, 'execFormattedCommand');

    await runTasks({}, container);

    const commands = getArgs(exec, 'echo');

    assert.deepEqual(commands, [
      'echo before:init',
      'echo before:my-plugin:init',
      'echo after:my-plugin:init',
      'echo before:npm:init',
      'echo after:npm:init',
      'echo before:git:init',
      'echo after:git:init',
      'echo before:version:init',
      'echo after:version:init',
      'echo after:init',
      'echo before:beforeBump',
      'echo before:my-plugin:beforeBump',
      'echo after:my-plugin:beforeBump',
      'echo before:npm:beforeBump',
      'echo after:npm:beforeBump',
      'echo before:git:beforeBump',
      'echo after:git:beforeBump',
      'echo before:version:beforeBump',
      'echo after:version:beforeBump',
      'echo after:beforeBump',
      'echo before:bump',
      'echo before:my-plugin:bump',
      'echo after:my-plugin:bump',
      'echo before:npm:bump',
      'echo after:npm:bump',
      'echo before:git:bump',
      'echo after:git:bump',
      'echo before:version:bump',
      'echo after:version:bump',
      'echo after:bump',
      'echo before:beforeRelease',
      'echo before:my-plugin:beforeRelease',
      'echo after:my-plugin:beforeRelease',
      'echo before:npm:beforeRelease',
      'echo after:npm:beforeRelease',
      'echo before:git:beforeRelease',
      'echo after:git:beforeRelease',
      'echo before:version:beforeRelease',
      'echo after:version:beforeRelease',
      'echo after:beforeRelease',
      'echo before:release',
      'echo before:npm:release',
      'echo after:npm:release',
      'echo before:git:release',
      'echo after:git:release',
      'echo before:version:release',
      'echo after:version:release',
      'echo before:my-plugin:release',
      'echo after:my-plugin:release',
      'echo after:release',
      'echo before:afterRelease',
      'echo before:npm:afterRelease',
      'echo after:npm:afterRelease',
      'echo before:git:afterRelease',
      'echo after:git:afterRelease',
      'echo before:version:afterRelease',
      'echo after:version:afterRelease',
      'echo before:my-plugin:afterRelease',
      'echo after:my-plugin:afterRelease',
      'echo after:afterRelease'
    ]);
  });
});
```

## File: `test/utils.js`
```javascript
import { EOL } from 'node:os';
import test from 'node:test';
import assert from 'node:assert/strict';
import { stripVTControlCharacters } from 'node:util';
import mockStdIo from 'mock-stdio';
import { format, truncateLines, parseGitUrl, parseVersion, get } from '../lib/util.js';

test('format', () => {
  assert.equal(format('release v${version}', { version: '1.0.0' }), 'release v1.0.0');
  assert.equal(format('release v${version} (${name})', { version: '1.0.0', name: 'foo' }), 'release v1.0.0 (foo)');
  assert.equal(format('release v${version} (${name})', { version: '1.0.0', name: 'foo' }), 'release v1.0.0 (foo)');
});

test('format (throw)', () => {
  mockStdIo.start();
  assert.throws(() => format('release v${foo}', { version: '1.0.0' }), /foo is not defined/);
  const { stdout, stderr } = mockStdIo.end();
  assert.equal(stdout, '');
  assert.match(
    stripVTControlCharacters(stderr),
    /ERROR Unable to render template with context:\s+release v\${foo}\s+{"version":"1\.0\.0"}\s+ERROR ReferenceError: foo is not defined/
  );
});

test('truncateLines', () => {
  const input = `1${EOL}2${EOL}3${EOL}4${EOL}5${EOL}6`;
  assert.equal(truncateLines(input), input);
  assert.equal(truncateLines(input, 3), `1${EOL}2${EOL}3${EOL}...and 3 more`);
  assert.equal(truncateLines(input, 1, '...'), `1...`);
});

test('parseGitUrl', () => {
  assert.deepEqual(parseGitUrl('https://github.com/webpro/release-it.git'), {
    host: 'github.com',
    owner: 'webpro',
    project: 'release-it',
    protocol: 'https',
    remote: 'https://github.com/webpro/release-it.git',
    repository: 'webpro/release-it'
  });

  assert.deepEqual(parseGitUrl('git@gitlab.com:org/sub-group/repo-in-sub-group.git'), {
    host: 'gitlab.com',
    owner: 'org/sub-group',
    project: 'repo-in-sub-group',
    protocol: 'ssh',
    remote: 'git@gitlab.com:org/sub-group/repo-in-sub-group.git',
    repository: 'org/sub-group/repo-in-sub-group'
  });

  assert.deepEqual(parseGitUrl('git@github.com:org/example.com.git'), {
    host: 'github.com',
    owner: 'org',
    project: 'example.com',
    protocol: 'ssh',
    remote: 'git@github.com:org/example.com.git',
    repository: 'org/example.com'
  });

  assert.deepEqual(parseGitUrl('file://Users/john/doe/owner/project'), {
    host: 'users',
    owner: 'owner',
    project: 'project',
    protocol: 'file',
    remote: 'file://users/john/doe/owner/project',
    repository: 'owner/project'
  });

  assert.deepEqual(parseGitUrl('/Users/john/doe/owner/project'), {
    host: 'users',
    owner: 'owner',
    project: 'project',
    protocol: 'file',
    remote: 'file://users/john/doe/owner/project',
    repository: 'owner/project'
  });

  assert.deepEqual(parseGitUrl('C:\\\\Users\\john\\doe\\owner\\project'), {
    host: 'users',
    owner: 'owner',
    project: 'project',
    protocol: 'file',
    remote: 'file://users/john/doe/owner/project',
    repository: 'owner/project'
  });
});

test('parseVersion', () => {
  assert.deepEqual(parseVersion(), { version: undefined, isPreRelease: false, preReleaseId: null });
  assert.deepEqual(parseVersion(0), { version: '0.0.0', isPreRelease: false, preReleaseId: null });
  assert.deepEqual(parseVersion(1), { version: '1.0.0', isPreRelease: false, preReleaseId: null });
  assert.deepEqual(parseVersion('1'), { version: '1.0.0', isPreRelease: false, preReleaseId: null });
  assert.deepEqual(parseVersion('1.0'), { version: '1.0.0', isPreRelease: false, preReleaseId: null });
  assert.deepEqual(parseVersion('1.0.0'), { version: '1.0.0', isPreRelease: false, preReleaseId: null });
  assert.deepEqual(parseVersion('1.0.0-0'), { version: '1.0.0-0', isPreRelease: true, preReleaseId: null });
  assert.deepEqual(parseVersion('1.0.0-next.1'), { version: '1.0.0-next.1', isPreRelease: true, preReleaseId: 'next' });
  assert.deepEqual(parseVersion('21.04.1'), { version: '21.04.1', isPreRelease: false, preReleaseId: null });
});

const sample = {
  root: {
    level1: {
      level2: {
        value: 'nested'
      },
      array: [
        { id: 1, data: 'first' },
        { id: 2, data: 'second' }
      ],
      'key.with.dot': {
        special: true
      }
    },
    mixed: [{ deep: { value: 100 } }, { deep: { value: 200 } }]
  }
};

test('get: accesses a simple nested property', () => {
  assert.equal(get(sample, 'root.level1.level2.value'), 'nested');
});

test('get: accesses array elements by index', () => {
  assert.equal(get(sample, 'root.level1.array[0].data'), 'first');
  assert.equal(get(sample, 'root.level1.array[1].id'), 2);
});

test('get: accesses keys with dots using bracket notation', () => {
  assert.equal(get(sample, 'root.level1["key.with.dot"].special'), true);
});

test('get: navigates mixed objects and arrays', () => {
  assert.equal(get(sample, 'root.mixed[0].deep.value'), 100);
  assert.equal(get(sample, 'root.mixed[1].deep.value'), 200);
});

test('get: returns default value for non-existent properties', () => {
  assert.equal(get(sample, 'root.level1.unknown', 'default'), 'default');
  assert.equal(get(sample, 'root.level1.array[10].id', null), null);
});

test('get: handles empty path and null/undefined objects', () => {
  assert.equal(get(sample, '', 'default'), 'default');
  assert.equal(get(null, 'any.path', 'default'), 'default');
  assert.equal(get(undefined, 'any.path', 'default'), 'default');
});
```

## File: `test/version.js`
```javascript
import test, { describe } from 'node:test';
import assert from 'node:assert/strict';
import Version from '../lib/plugin/version/Version.js';
import { factory, runTasks } from './util/index.js';

describe('version', () => {
  test('isValidVersion', async () => {
    const v = await factory(Version);
    assert.equal(v.isValid('1.0.0'), true);
    assert.equal(v.isValid(1.0), false);
  });

  test('isPreRelease', async () => {
    const v = await factory(Version);
    assert.equal(v.isPreRelease('1.0.0-beta.0'), true);
    assert.equal(v.isPreRelease('1.0.0'), false);
  });

  test('should return the same version in both interactive and ci mode', async () => {
    const v = await factory(Version);
    const options = { latestVersion: '2.0.0-beta.1', increment: null, preReleaseId: 'rc', isPreRelease: true };
    const resultInteractiveMode = await v.getIncrementedVersion(options);
    assert.equal(resultInteractiveMode, '2.0.0-rc.0');
    const resultCiMode = v.getIncrementedVersionCI(options);
    assert.equal(resultInteractiveMode, resultCiMode);
  });

  test('should increment latest version', async () => {
    const v = await factory(Version);
    const latestVersion = '1.0.0';
    assert.equal(v.incrementVersion({ latestVersion, increment: false }), '1.0.0');
    assert.equal(v.incrementVersion({ latestVersion, increment: 'foo' }), undefined);
    assert.equal(v.incrementVersion({ latestVersion, increment: 'patsj' }), undefined);
    assert.equal(v.incrementVersion({ latestVersion, increment: 'a.b.c' }), undefined);
    assert.equal(v.incrementVersion({ latestVersion, increment: '0.9.0' }), undefined);
    assert.equal(v.incrementVersion({ latestVersion, increment: '1.1.0' }), '1.1.0');
    assert.equal(v.incrementVersion({ latestVersion, increment: 'major' }), '2.0.0');
    assert.equal(v.incrementVersion({ latestVersion, increment: '2.0.0-beta.1' }), '2.0.0-beta.1');
  });

  test('should not increment latest version in interactive mode', async () => {
    const v = await factory(Version, { options: { ci: false } });
    const latestVersion = '1.0.0';
    assert.equal(v.incrementVersion({ latestVersion, increment: null }), undefined);
    assert.equal(v.incrementVersion({ latestVersion, increment: false }), '1.0.0');
  });

  test('should always set increment version in CI mode', async () => {
    const v = await factory(Version, { options: { ci: true } });
    const latestVersion = '1.0.0';
    assert.equal(v.getIncrementedVersionCI({ latestVersion, increment: false }), '1.0.0');
    assert.equal(v.getIncrementedVersionCI({ latestVersion, increment: null }), '1.0.1');
    assert.equal(v.getIncrementedVersionCI({ latestVersion, increment: '1.1.0' }), '1.1.0');
    assert.equal(v.getIncrementedVersionCI({ latestVersion, increment: 'major' }), '2.0.0');
  });

  test('should increment latest version (coerce)', async () => {
    const v = await factory(Version);
    assert.equal(v.incrementVersion({ increment: '1.2' }), '1.2.0');
    assert.equal(v.incrementVersion({ increment: '1' }), '1.0.0');
    assert.equal(v.incrementVersion({ increment: 'v1.2.0.0' }), '1.2.0');
  });

  test('should increment version (pre-release continuation)', async () => {
    const v = await factory(Version);
    assert.equal(v.incrementVersion({ latestVersion: '1.2.3-alpha.0', increment: 'prepatch' }), '1.2.4-0');
  });

  test('should increment version (prepatch)', async () => {
    const v = await factory(Version);
    assert.equal(
      v.incrementVersion({ latestVersion: '1.2.3', increment: 'prepatch', preReleaseId: 'alpha' }),
      '1.2.4-alpha.0'
    );
  });

  test('should increment version (normalized)', async () => {
    const v = await factory(Version);
    assert.equal(
      v.incrementVersion({ latestVersion: '1.2.3', increment: 'patch', preReleaseId: 'alpha', isPreRelease: true }),
      '1.2.4-alpha.0'
    );
  });

  test('should increment version (prepatch on prerelease version)', async () => {
    const v = await factory(Version);
    assert.equal(
      v.incrementVersion({ latestVersion: '1.2.3-alpha.5', increment: 'prepatch', preReleaseId: 'next' }),
      '1.2.4-next.0'
    );
  });

  test('should increment version (normalized on prerelease version)', async () => {
    const v = await factory(Version);
    assert.equal(
      v.incrementVersion({
        latestVersion: '1.2.3-alpha.5',
        increment: 'patch',
        preReleaseId: 'next',
        isPreRelease: true
      }),
      '1.2.4-next.0'
    );
  });

  test('should increment version (prerelease)', async () => {
    const v = await factory(Version);
    assert.equal(
      v.incrementVersion({ latestVersion: '1.2.3', increment: 'prerelease', preReleaseId: 'alpha' }),
      '1.2.4-alpha.0'
    );
  });

  test('should increment version (prerelease cont.)', async () => {
    const v = await factory(Version);
    assert.equal(v.incrementVersion({ latestVersion: '1.2.3-alpha.0', increment: 'prerelease' }), '1.2.3-alpha.1');
  });

  test('should increment version (preReleaseId continuation)', async () => {
    const v = await factory(Version);
    assert.equal(
      v.incrementVersion({ latestVersion: '1.2.3-alpha.0', increment: 'prerelease', preReleaseId: 'alpha' }),
      '1.2.3-alpha.1'
    );
  });

  test('should increment version (prepatch/preReleaseId continuation)', async () => {
    const v = await factory(Version);
    const options = {
      latestVersion: '1.2.3-beta.0',
      increment: 'prerelease',
      preReleaseId: 'beta',
      isPreRelease: true
    };
    assert.equal(v.incrementVersion(options), '1.2.3-beta.1');
  });

  test('should increment version (preReleaseId w/o preRelease)', async () => {
    const v = await factory(Version);
    assert.equal(
      v.incrementVersion({ latestVersion: '1.2.3-alpha.0', increment: 'patch', preReleaseId: 'alpha' }),
      '1.2.3'
    );
  });

  test('should increment version (non-numeric prepatch continuation)', async () => {
    const v = await factory(Version);
    assert.equal(v.incrementVersion({ latestVersion: '1.2.3-alpha', increment: 'prerelease' }), '1.2.3-alpha.0');
  });

  test('should increment version (patch release after pre-release)', async () => {
    const v = await factory(Version);
    assert.equal(v.incrementVersion({ latestVersion: '1.2.3-alpha.1', increment: 'patch' }), '1.2.3');
  });

  test('should increment version and start at base 1', async () => {
    const v = await factory(Version);
    assert.equal(
      v.incrementVersion({
        latestVersion: '1.3.0',
        increment: 'major',
        isPreRelease: true,
        preReleaseId: 'beta',
        preReleaseBase: '1'
      }),
      '2.0.0-beta.1'
    );
  });

  test('should increment prerelease version and ignore prelease base 1', async () => {
    const v = await factory(Version);
    assert.equal(
      v.incrementVersion({
        latestVersion: '1.2.3-alpha.5',
        increment: 'prerelease',
        preReleaseId: 'alpha',
        isPreRelease: true,
        preReleaseBase: '1'
      }),
      '1.2.3-alpha.6'
    );
  });

  test('should run tasks without errors', async t => {
    const options = { version: { increment: 'minor' } };
    const v = await factory(Version, { options });
    const getIncrement = t.mock.method(v, 'getIncrement');
    const getIncrementedVersionCI = t.mock.method(v, 'getIncrementedVersionCI');
    const incrementVersion = t.mock.method(v, 'incrementVersion');

    await runTasks(v);

    assert.equal(getIncrement.mock.callCount(), 1);
    assert.deepEqual(getIncrement.mock.calls[0].arguments[0], { increment: 'minor' });
    assert.equal(getIncrementedVersionCI.mock.callCount(), 1);
    assert.deepEqual(getIncrementedVersionCI.mock.calls[0].arguments[0], {
      latestVersion: '1.0.0',
      increment: 'minor',
      isPreRelease: false,
      preReleaseId: null
    });
    assert.equal(await incrementVersion.mock.calls[0].result, '1.1.0');
    assert.equal(incrementVersion.mock.callCount(), 1);
    assert.deepEqual(incrementVersion.mock.calls[0].arguments[0], {
      latestVersion: '1.0.0',
      increment: 'minor',
      isPreRelease: false,
      preReleaseId: null
    });
    assert.equal(incrementVersion.mock.calls[0].result, '1.1.0');
    const { latestVersion, version, isPreRelease, preReleaseId } = v.config.getContext();
    assert.equal(latestVersion, '1.0.0');
    assert.equal(version, '1.1.0');
    assert.equal(isPreRelease, false);
    assert.equal(preReleaseId, null);
  });
});
```

## File: `test/resources/file-v2.0.1.txt`
```
*
```

## File: `test/resources/file-v2.0.2.txt`
```
*
```

## File: `test/resources/file1`
```
file1
```

## File: `test/stub/github.js`
```javascript
export const interceptAuthentication = (server, { username = 'john' } = {}) => {
  server.get('/user', { status: 200, body: { login: username } });
};

export const interceptCollaborator = (server, { owner = 'user', project = 'repo', username = 'john' } = {}) => {
  server.get(`/repos/${owner}/${project}/collaborators/${username}`, { status: 204 });
};

export const interceptListReleases = (
  server,
  { host = 'github.com', owner = 'user', project = 'repo', tag_name } = {}
) => {
  server.get(`/repos/${owner}/${project}/releases?per_page=1&page=1`, {
    status: 200,
    body: [
      {
        id: 1,
        upload_url: `https://uploads.${host}/repos/${owner}/${project}/releases/1/assets{?name,label}`,
        html_url: `https://${host}/${owner}/${project}/releases/tag/${tag_name}`,
        tag_name,
        target_commitish: 'main',
        name: `Release ${tag_name}`,
        body: 'Description of the release',
        draft: false,
        prerelease: false
      }
    ]
  });
};

export const interceptCreate = (
  server,
  {
    api = 'https://api.github.com',
    host = 'github.com',
    owner = 'user',
    project = 'repo',
    body: {
      tag_name,
      name = '',
      body = null,
      prerelease = false,
      draft = false,
      generate_release_notes = false,
      make_latest = 'true',
      discussion_category_name = undefined
    }
  } = {}
) => {
  const id = 1;
  server.post(
    {
      url: `/repos/${owner}/${project}/releases`,
      body: { tag_name, name, body, prerelease, draft, generate_release_notes, make_latest, discussion_category_name }
    },
    {
      status: 200,
      body: {
        id,
        tag_name,
        name,
        body,
        prerelease,
        draft,
        generate_release_notes,
        upload_url: `https://uploads.${host}/repos/${owner}/${project}/releases/${id}/assets{?name,label}`,
        html_url: `https://${host}/${owner}/${project}/releases/tag/${tag_name}`,
        discussion_url: discussion_category_name ? `https://${host}/${owner}/${project}/discussions/${id}` : undefined
      },
      headers: { location: `${api}/repos/${owner}/${project}/releases/${id}` }
    }
  );
};

export const interceptUpdate = (
  server,
  {
    host = 'github.com',
    owner = 'user',
    project = 'repo',
    body: {
      tag_name,
      name = '',
      body = null,
      prerelease = false,
      draft = false,
      generate_release_notes = false,
      make_latest = 'true',
      discussion_category_name = undefined
    }
  } = {}
) => {
  server.patch(
    {
      url: `/repos/${owner}/${project}/releases/1`,
      body: {
        tag_name,
        name,
        body,
        draft,
        prerelease,
        generate_release_notes,
        make_latest,
        discussion_category_name
      }
    },
    {
      status: 200,
      body: {
        id: 1,
        tag_name,
        name,
        body,
        prerelease,
        draft,
        generate_release_notes,
        upload_url: `https://uploads.${host}/repos/${owner}/${project}/releases/1/assets{?name,label}`,
        html_url: `https://${host}/${owner}/${project}/releases/tag/${tag_name}`
      }
    }
  );
};

export const interceptAsset = (
  server,
  { api = 'https://api.github.com', host = 'github.com', owner = 'user', project = 'repo', tagName } = {}
) => {
  server.post(
    {
      url: `/repos/${owner}/${project}/releases/1/assets`
    },
    request => {
      const id = 1;
      const url = new URL(request.url);
      const name = url.searchParams.get('name');
      return {
        status: 200,
        body: {
          id,
          url: `${api}/repos/${owner}/${project}/releases/assets/${id}`,
          name,
          label: '',
          state: 'uploaded',
          size: request.headers['content-length'],
          browser_download_url: `https://${host}/${owner}/${project}/releases/download/${tagName}/${name}`
        }
      };
    }
  );
};
```

## File: `test/stub/gitlab.js`
```javascript
export const interceptMembers = (server, { owner = 'emma' } = {}) => {
  server.get(`/projects/john%2Frepo/members/all/1`, { status: 200, username: owner });
};

export const interceptUser = (server, { owner = 'user' } = {}, options = {}) => {
  server.get({ url: '/user', ...options }, { status: 200, body: { id: 1, username: owner } });
};

export const interceptCollaborator = (
  server,
  { owner = 'user', project = 'repo', group, userId = 1 } = {},
  options = {}
) =>
  server.get(
    {
      url: `/projects/${group ? `${group}%2F` : ''}${owner}%2F${project}/members/all/${userId}`,
      ...options
    },
    {
      status: 200,
      body: { id: userId, username: owner, access_level: 30 }
    }
  );

export const interceptPublish = (server, { owner = 'user', project = 'repo', body } = {}) =>
  server.post(
    { url: `/projects/${owner}%2F${project}/releases`, body },
    {
      status: 200,
      body: {
        _links: {
          self: `https://gitlab.com/${owner}/${project}/-/releases/${body?.tag_name ?? '1.0.0'}`
        }
      }
    }
  );

export const interceptMilestones = (server, { owner = 'user', project = 'repo', query = {}, milestones = [] } = {}) =>
  server.get(
    {
      url: `/projects/${owner}%2F${project}/milestones`,
      query: {
        include_parent_milestones: 'true',
        ...query
      }
    },
    {
      status: 200,
      body: milestones
    }
  );

export const interceptAsset = (server, { owner = 'user', project = 'repo' } = {}) =>
  server.post(
    {
      url: `/projects/${owner}%2F${project}/uploads`
    },
    async request => {
      const formData = await request.formData();
      const { name } = formData.get('file');
      return {
        status: 200,
        body: {
          alt: name,
          url: `/uploads/7e8bec1fe27cc46a4bc6a91b9e82a07c/${name}`,
          full_path: `/-/project/1234/uploads/7e8bec1fe27cc46a4bc6a91b9e82a07c/${name}`,
          markdown: `[${name}](/uploads/7e8bec1fe27cc46a4bc6a91b9e82a07c/${name})`,
          _links: {
            self: `https://gitlab.com/${owner}/${project}/-/releases/${name}`
          }
        }
      };
    }
  );

export const interceptAssetGeneric = (server, { owner = 'user', project = 'repo' } = {}) =>
  server.put(
    {
      url: `/projects/${owner}%2F${project}/packages/generic/release-it/2.0.1/file-v2.0.1.txt`
    },
    {
      status: 200,
      body: {
        message: '201 Created'
      }
    }
  );
```

## File: `test/stub/plugin-context.js`
```javascript
import Plugin from '../../lib/plugin/Plugin.js';

class ContextPlugin extends Plugin {
  init() {
    const context = this.config.getContext();
    this.exec(`echo ${context.version.isPreRelease}`);
    this.exec('echo ${version.isPreRelease}');
  }
  beforeBump() {
    const context = this.config.getContext();
    this.exec(`echo ${context.name} ${context.repo.owner} ${context.latestVersion} ${context.version}`);
    this.exec('echo ${name} ${repo.owner} ${latestVersion} ${version}');
  }
  bump(version) {
    const repo = this.config.getContext('repo');
    this.exec(`echo ${repo.owner} ${repo.project} ${repo.repository} ${version}`);
    this.exec('echo ${repo.owner} ${repo.project} ${repo.repository} ${version}');
  }
  beforeRelease() {
    const { repo, tagName } = this.config.getContext();
    this.exec(`echo ${repo.owner} ${repo.project} ${repo.repository} ${tagName}`);
    this.exec('echo ${repo.owner} ${repo.project} ${repo.repository} ${tagName}');
  }
  release() {
    const { repo, latestVersion, version, tagName } = this.config.getContext();
    this.exec(`echo ${repo.project} ${latestVersion} ${version} ${tagName}`);
    this.exec('echo ${repo.project} ${latestVersion} ${version} ${tagName}');
  }
  afterRelease() {
    const { repo, latestVersion, version, tagName } = this.config.getContext();
    this.exec(`echo ${repo.project} ${latestVersion} ${version} ${tagName}`);
    this.exec('echo ${repo.project} ${latestVersion} ${version} ${tagName}');
  }
}

export default ContextPlugin;
```

## File: `test/stub/plugin-replace.js`
```javascript
import Plugin from '../../lib/plugin/Plugin.js';

class ReplacePlugin extends Plugin {
  static disablePlugin() {
    return ['version', 'git', 'npm'];
  }
}

export default ReplacePlugin;
```

## File: `test/stub/plugin.js`
```javascript
import Plugin from '../../lib/plugin/Plugin.js';

class MyPlugin extends Plugin {
  init() {
    this.log.info(`${this.namespace}:${this.getContext('name')}:init`);
  }
  getName() {
    this.log.info(`${this.namespace}:${this.getContext('name')}:getName`);
    return 'new-project-name';
  }
  getLatestVersion() {
    this.log.info(`${this.namespace}:${this.getContext('name')}:getLatestVersion`);
    return '1.2.3';
  }
  getIncrement() {
    this.log.info(`${this.namespace}:${this.getContext('name')}:getIncrement`);
    return 'minor';
  }
  getIncrementedVersionCI() {
    this.log.info(`${this.namespace}:${this.getContext('name')}:getIncrementedVersionCI`);
  }
  beforeBump() {
    this.log.info(`${this.namespace}:${this.getContext('name')}:beforeBump`);
  }
  bump(version) {
    this.log.info(`${this.namespace}:${this.getContext('name')}:bump:${version}`);
  }
  beforeRelease() {
    this.log.info(`${this.namespace}:${this.getContext('name')}:beforeRelease`);
  }
  release() {
    this.log.info(`${this.namespace}:${this.getContext('name')}:release`);
  }
  afterRelease() {
    this.log.info(`${this.namespace}:${this.getContext('name')}:afterRelease`);
  }
}

export default MyPlugin;
```

## File: `test/stub/shell.js`
```javascript
import util from 'node:util';
import Shell from '../../lib/shell.js';

const debug = util.debug('release-it:shell-stub');

class ShellStub extends Shell {
  exec(command) {
    const cmd = Array.isArray(command) ? command.join(' ') : command;
    if (/^(npm (ping|publish|show)|git fetch)/.test(cmd)) {
      debug(cmd);
      return Promise.resolve();
    }
    if (/^npm whoami/.test(cmd)) {
      debug(cmd);
      return Promise.resolve('john');
    }
    if (/^npm access/.test(cmd)) {
      debug(cmd);
      return Promise.resolve(JSON.stringify({ john: ['write'] }));
    }
    return super.exec(...arguments);
  }
}

export default ShellStub;
```

## File: `test/stub/config/invalid-config-rc`
```
foo=bar
```

## File: `test/stub/config/invalid-config-txt`
```
foo
bar\baz
```

## File: `test/stub/config/default/.release-it.json`
```json
{
  "github": {
    "release": true
  }
}
```

## File: `test/stub/config/merge/.release-it.json`
```json
{
  "github": {
    "release": true
  }
}
```

## File: `test/stub/config/merge/package.json`
```json
{
  "release-it": {
    "git": {
      "push": false
    }
  }
}
```

## File: `test/stub/config/remote/.release-it.json`
```json
{
  "git": {
    "commitMessage": "Released version ${version}"
  }
}
```

## File: `test/stub/config/remote/sub/.release-it.json`
```json
{
  "git": {
    "commitMessage": "Released with version ${version}"
  }
}
```

## File: `test/stub/config/toml/.release-it.toml`
```
[foo]
bar=1
```

## File: `test/stub/config/yaml/.release-it.yaml`
```yaml
foo:
  bar: 1
```

## File: `test/stub/config/yml/.release-it.yml`
```yaml
foo:
  bar: 1
```

## File: `test/util/fetch.js`
```javascript
import { Readable } from 'node:stream';
import { create as createTar } from 'tar';
import { appendFile, mkTmpDir } from './helpers.js';

export function createTarBlob(dir) {
  const stream = new Readable({
    read() {}
  });

  createTar(
    {
      gzip: true,
      portable: true,
      sync: false,
      cwd: dir
    },
    ['.']
  )
    .on('data', chunk => stream.push(chunk))
    .on('end', () => stream.push(null));

  return stream;
}

export function createTarBlobByRawContents(contents) {
  const dir = mkTmpDir();
  for (const [key, value] of Object.entries(contents)) {
    appendFile(value, key, dir);
  }

  return createTarBlob(dir);
}
```

## File: `test/util/helpers.js`
```javascript
import { appendFileSync, mkdirSync, mkdtempSync, promises } from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import childProcess from 'node:child_process';
import { execOpts } from '../../lib/util.js';

const mkTmpDir = () => {
  const dir = mkdtempSync(path.join(os.tmpdir(), 'release-it-'));
  return dir;
};

const readFile = file => promises.readFile(path.resolve(file), 'utf8');

const gitAdd = (content, filePath, message) => {
  appendFile(content, filePath);
  childProcess.execSync(`git add ${filePath}`, execOpts);
  const stdout = childProcess.execSync(`git commit -m "${message}"`, { encoding: 'utf-8' });
  const match = stdout.match(/\[.+([a-z0-9]{7})\]/);
  return match ? match[1] : null;
};

const getArgs = (fn, prefix) =>
  fn.mock.calls
    .map(call => call.arguments[0])
    .map(arg => (typeof arg !== 'string' ? arg.join(' ') : arg))
    .filter(cmd => cmd.startsWith(prefix))
    .map(cmd => cmd.trim());

const appendFile = (content, filePath, cwd) => {
  filePath = path.resolve(cwd ?? '', filePath);
  const dirPath = path.dirname(filePath);

  if (dirPath) {
    mkdirSync(dirPath, { mode: parseInt('0777', 8), recursive: true });
  }

  appendFileSync(filePath, content);
};

export { mkTmpDir, readFile, gitAdd, getArgs, appendFile };
```

## File: `test/util/index.js`
```javascript
import { mock } from 'node:test';
import semver from 'semver';
import { parseVersion } from '../../lib/util.js';
import Config from '../../lib/config.js';
import ShellStub from '../stub/shell.js';
import Prompt from '../../lib/prompt.js';

const noop = Promise.resolve();

export class LogStub {
  constructor() {
    this.log = mock.fn();
    this.error = mock.fn();
    this.info = mock.fn();
    this.warn = mock.fn();
    this.verbose = mock.fn();
    this.exec = mock.fn();
    this.obtrusive = mock.fn();
    this.preview = mock.fn();
  }
  resetCalls() {
    this.log.mock.resetCalls();
    this.error.mock.resetCalls();
    this.info.mock.resetCalls();
    this.warn.mock.resetCalls();
    this.verbose.mock.resetCalls();
    this.exec.mock.resetCalls();
    this.obtrusive.mock.resetCalls();
    this.preview.mock.resetCalls();
  }
}

export class SpinnerStub {
  show({ enabled = true, task }) {
    return enabled ? task() : noop;
  }
}

export let factory = async (Definition, { namespace, options = {}, container = {} } = {}) => {
  options = Object.assign({}, { ci: true, verbose: false, 'dry-run': false, debug: false }, options);
  const ns = namespace || Definition.name.toLowerCase();
  container.config = container.config || new Config(Object.assign({ config: false }, options));
  container.log = new LogStub();
  await container.config.init();

  container.spinner = new SpinnerStub();
  container.shell = container.shell || new ShellStub({ container });

  container.prompt = container.prompt || new Prompt({ container });
  container.shell.cache = { set: () => {}, has: () => false };

  return new Definition({
    namespace: ns,
    options,
    container
  });
};

const getIncrement = plugin =>
  plugin.getIncrement(plugin.options) || plugin.getContext('increment') || plugin.config.getContext('increment');

const getVersion = async (plugin, options) => {
  const { latestVersion, increment } = options;
  return (
    (await plugin.getIncrementedVersionCI(options)) ||
    (await plugin.getIncrementedVersion(options)) ||
    (increment !== false ? semver.inc(latestVersion, increment || 'patch') : latestVersion)
  );
};

export let runTasks = async plugin => {
  await plugin.init();

  const name = (await plugin.getName()) || '__test__';
  const latestVersion = (await plugin.getLatestVersion()) || '1.0.0';
  const latestTag = plugin.config.getContext('latestTag');
  const changelog = (await plugin.getChangelog(latestVersion)) || null;
  const increment = getIncrement(plugin);

  plugin.config.setContext({ name, latestVersion, latestTag, changelog });

  const { preRelease } = plugin.config.options;
  const isPreRelease = Boolean(preRelease);
  const preReleaseId = typeof preRelease === 'string' ? preRelease : null;
  const version = await getVersion(plugin, { latestVersion, increment, isPreRelease, preReleaseId });

  plugin.config.setContext(parseVersion(version));

  await plugin.beforeBump();
  await plugin.bump(version);

  const tagName = plugin.config.getContext('tagName') || version;
  plugin.config.setContext({ tagName });

  await plugin.beforeRelease();
  await plugin.release();
  await plugin.afterRelease();

  return {
    name,
    latestVersion,
    version
  };
};
```

## File: `test/util/mock.js`
```javascript
import { MockServer, FetchMocker } from 'mentoss';

export const mockFetch = baseUrls => {
  const servers = [baseUrls].flat().map(url => new MockServer(url));

  const mocker = new FetchMocker({
    servers
  });

  return [mocker, ...servers];
};
```

## File: `test/util/sh.js`
```javascript
import { spawnSync } from 'node:child_process';

const getCommandAndArgs = input => {
  if (typeof input !== 'string' || !input.trim()) {
    throw new Error('Invalid input: expected a non-empty string.');
  }

  const [command, ...args] = input.trim().split(/\s+/);

  return [command, args];
};

const exec = (command, opts = { stdio: 'inherit' }) => {
  const [cmd, args] = getCommandAndArgs(command);
  return spawnSync(cmd, args, opts);
};

export default { getCommandAndArgs, exec };
```

## File: `test/util/https-server/gen-cert.sh`
```bash
#!/bin/bash

# Generate client and server self-signed HTTPS certificates
# Adapted from:
# https://stackoverflow.com/questions/19665863/how-do-i-use-a-self-signed-certificate-for-a-https-node-js-server/24749608#24749608

FQDN=$1

if [ -z "$FQDN" ]; then
  echo -e "\nError: Missing required parameter for domain name.\n"
  echo -e "Usage:\n\t./gen-cert.sh <DOMAIN_NAME>\n"
  exit 1
fi;

# make directories to work from
mkdir -p server/ client/ all/

# Create your very own Root Certificate Authority
openssl genrsa \
  -out all/my-private-root-ca.privkey.pem \
  2048

# Self-sign your Root Certificate Authority
# Since this is private, the details can be as bogus as you like
openssl req \
  -x509 \
  -new \
  -nodes \
  -key all/my-private-root-ca.privkey.pem \
  -days 1024 \
  -out all/my-private-root-ca.cert.pem \
  -subj "/C=US/ST=Utah/L=Provo/O=ACME Signing Authority Inc/CN=example.com"

# Create a Device Certificate for each domain,
# such as example.com, *.example.com, awesome.example.com
# NOTE: You MUST match CN to the domain name or ip address you want to use
openssl genrsa \
  -out all/privkey.pem \
  2048

# Create a request from your Device, which your Root CA will sign
openssl req -new \
  -key all/privkey.pem \
  -out all/csr.pem \
  -subj "/C=US/ST=Utah/L=Provo/O=ACME Tech Inc/CN=${FQDN}"

# Sign the request from Device with your Root CA
openssl x509 \
  -req -in all/csr.pem \
  -CA all/my-private-root-ca.cert.pem \
  -CAkey all/my-private-root-ca.privkey.pem \
  -CAcreateserial \
  -out all/cert.pem \
  -days 500

# Put things in their proper place
rsync -a all/{privkey,cert}.pem server/
cat all/cert.pem > server/fullchain.pem         # we have no intermediates in this case
rsync -a all/my-private-root-ca.cert.pem server/
rsync -a all/my-private-root-ca.cert.pem client/

# create DER format crt for iOS Mobile Safari, etc
openssl x509 -outform der -in all/my-private-root-ca.cert.pem -out client/my-private-root-ca.crt

rm -r all
```

## File: `test/util/https-server/server.js`
```javascript
import { createServer } from 'node:https';
import { readFileSync } from 'node:fs';
import { join } from 'node:path';
import { debug } from 'node:util';
import { fileURLToPath } from 'node:url';

/**
 * @typedef {import('http').IncomingMessage} IncomingMessage
 * @typedef {import('http').ServerResponse} ServerResponse
 * @typedef {ServerResponse & { req: IncomingMessage;}} RequestResponse
 * @typedef {import('https').ServerOptions} ServerOptions
 */

const DIRNAME = getDirname();

/** @type {ServerOptions} */
const options = {
  key: readFileSync(join(DIRNAME, './server/privkey.pem')),
  cert: readFileSync(join(DIRNAME, './server/fullchain.pem'))
};

/**
 * Basic https server to use for the Gitlab tests.
 * Uses a self-signed HTTPS certificate to allow testing gitlab release options
 * like `insecure` or `certificateAuthorityFile`.
 *
 * The certicates were generated using the gen-cert.sh script in this folder
 * with the following command:
 *
 *   `./gen-cert.sh localhost`
 *
 */
export class GitlabTestServer {
  constructor() {
    this.server = createServer(options, (req, res) => this._requestHandler(req, res));
    this.debug = debug('release-it:gitlab-test-server');
  }

  /**
   * Starts the server with the given port and host
   *
   * @param {number} [port]
   * @param {string} [host]
   * @returns {Promise<void>}
   */
  run(port = 3000, host) {
    return new Promise((resolve, reject) => {
      if (this.server.listening) {
        resolve();
        return;
      }

      this.server.listen(port, host, () => {
        const address = this.server.address();
        this.debug('Server listening on https://' + address.address + ':' + address.port);
        resolve();
      });

      this.server.on('error', e => {
        if (e.code === 'EADDRINUSE') {
          reject(e);
          return;
        }

        this.debug(e.message);
      });
    });
  }

  /**
   * Closes the server
   *
   * @returns {Promise<void>}
   */
  stop() {
    return new Promise((resolve, reject) => {
      if (!this.server.listening) {
        resolve();
        return;
      }

      this.server.removeAllListeners();

      this.server.close(err => {
        if (err) {
          reject(err);
          return;
        }

        this.debug('Server successfully closed.');
        resolve();
      });
    });
  }

  /**
   * @private
   *
   * Server's main request handler
   *
   * @param {IncomingMessage} req
   * @param {RequestResponse} res
   * @returns {void}
   */
  _requestHandler(req, res) {
    if (req.url === '/api/v4/user') {
      this._json(res, { id: '1234', username: 'release_bot' });
      return;
    }

    if (req.url.startsWith('/api/v4/projects') && req.url.endsWith('/members/all/1234')) {
      this._json(res, { access_level: 50 });
      return;
    }

    this._text(res, 'Ok');
  }

  /**
   * @private
   *
   * Sends out a JSON response
   *
   * @param {RequestResponse} res
   * @param {object} payload
   */
  _json(res, payload) {
    res.writeHead(200, { 'content-type': 'application/json' });
    res.end(JSON.stringify(payload));
  }

  /**
   * @private
   *
   * Sends out a text response
   *
   * @param {RequestResponse} res
   * @param {string} message
   */
  _text(res, message) {
    res.writeHead(200, { 'content-type': 'text/plan' });
    res.end(message);
  }
}

function getDirname() {
  if (import.meta.dirname) return import.meta.dirname;

  return fileURLToPath(new URL('.', import.meta.url));
}
```

## File: `test/util/https-server/client/my-private-root-ca.cert.pem`
```
-----BEGIN CERTIFICATE-----
MIIDrzCCApegAwIBAgIUUAyKcu86WuJQd1fdlHsXkCl1mYMwDQYJKoZIhvcNAQEL
BQAwZzELMAkGA1UEBhMCVVMxDTALBgNVBAgMBFV0YWgxDjAMBgNVBAcMBVByb3Zv
MSMwIQYDVQQKDBpBQ01FIFNpZ25pbmcgQXV0aG9yaXR5IEluYzEUMBIGA1UEAwwL
ZXhhbXBsZS5jb20wHhcNMjQxMjExMTMxMzIyWhcNMjcxMDAxMTMxMzIyWjBnMQsw
CQYDVQQGEwJVUzENMAsGA1UECAwEVXRhaDEOMAwGA1UEBwwFUHJvdm8xIzAhBgNV
BAoMGkFDTUUgU2lnbmluZyBBdXRob3JpdHkgSW5jMRQwEgYDVQQDDAtleGFtcGxl
LmNvbTCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAKlp3Kz278oyTDY4
+1iNv1xMzWCJBWf7YxyYkXACVvZzUqgwxotNwAE/kE131HgpBJnu7HsDdS8nLy80
mDkFCGmqEuVZMDaMGtcz3HJSklESjxYM1VNgifz2IlNmoaidNehFkCi1rz6cLMR0
rEZpi98EbVZGl3n0vDD0eEZF5QQn/eDwclt/aKVBVLcQxo6MHhQdaK85a1uNyUU3
HPUYiyPGVn9oX9PGcOpYFomJoBdg3sUVk32xKCUf15+uqVchdtyGFW/bp5KSBCnB
QD0TzN+SgBHnVTzIfoi8WY56uuwnYauvT4fRh8SfkV91BzHBtWSbulNTfTUzgWhs
VvCGw7ECAwEAAaNTMFEwHQYDVR0OBBYEFC4qTshaPoBie1ukhhM0KBi95NzJMB8G
A1UdIwQYMBaAFC4qTshaPoBie1ukhhM0KBi95NzJMA8GA1UdEwEB/wQFMAMBAf8w
DQYJKoZIhvcNAQELBQADggEBAB+fRdUHgqwpTWRfF+jQB4Af75HTfp6hgemUjapI
eZn/OugS75/jfJt9npVsHl/aa63GL/W6kQShoMVOhrYqW52J1TSsLKZR2L7sv0ji
KYfakv+aLkRKewPoVadsCL8GUmaCByE9mwlhmmZprkjDmA3hWsjEM5lyg7qleJ0k
V32FVysdhLLnftt2SJB7lyoTujhkNAjJhLT/0Qr8t59v0sViPtL8532jSXqE1GK+
zncsJDK7v2VEuurz1lPTRY6tPQOJ1Qt8vUzDH/ugcc5JPBEuHhjjrd5K65lxnGNw
lnPHIS7FJm1OMkuatQXomNuuoWDPyM7fuVyGUUpmlkbpJsg=
-----END CERTIFICATE-----
```

## File: `test/util/https-server/server/cert.pem`
```
-----BEGIN CERTIFICATE-----
MIIDRjCCAi4CFGCNNJXfcHchSO1xHnWt5wcENGznMA0GCSqGSIb3DQEBCwUAMGcx
CzAJBgNVBAYTAlVTMQ0wCwYDVQQIDARVdGFoMQ4wDAYDVQQHDAVQcm92bzEjMCEG
A1UECgwaQUNNRSBTaWduaW5nIEF1dGhvcml0eSBJbmMxFDASBgNVBAMMC2V4YW1w
bGUuY29tMB4XDTI0MTIxMTEzMTMyMloXDTI2MDQyNTEzMTMyMlowWDELMAkGA1UE
BhMCVVMxDTALBgNVBAgMBFV0YWgxDjAMBgNVBAcMBVByb3ZvMRYwFAYDVQQKDA1B
Q01FIFRlY2ggSW5jMRIwEAYDVQQDDAlsb2NhbGhvc3QwggEiMA0GCSqGSIb3DQEB
AQUAA4IBDwAwggEKAoIBAQC1+BYy7XcJoIAHqPcU7f74Dp/6N6f/hjLTADMIT1OO
49W3Rrc6xbJjeLsiTD0Rj9Z/9CSI7Vh/AOLoW7OGMOZkJZNRw8L9lc14ZDB1FAcJ
ITn8c9d0d0YltbxUOq509wEP6GSxYCqYZlvAjeyYADRW5PnP82n6MRMW9Ve5y50s
ijeaVk120je5zKvQTd0IR9rXf8K3M8CmnlEVuuf4+uXvg0gUsGvSSkBxPVGeUQHM
/zRxj/I8WYCewb9Qs2TSJjgnFsfUCF6C3xs/T8p4vJ8PxeLs6GNcQhhtNH0q7Wxa
IV4cdrXkxPi6YS8ph1WErqNR2pdsCA5bUNTCT32vPjr/AgMBAAEwDQYJKoZIhvcN
AQELBQADggEBACu1hC1yvFKF6nEjz4mdTmVIyqktfkQX4+5edpSCLM0UhOmQ9Tm3
3NnQ06YhPnAkiXLiyKxoCGqulgh1B1+3Ii0/ttDq4D4HIEVMwT5Hmko3vppUkJD7
aIacmTKxGFrtF+p1hIDXmAAYFUB2bWDgVvba2z70DkbffJBOwe/+2+hOgFXI5x3+
IJuF0bYKRlFG0yvVX+ooWAaKmCSR4reCsjWNuP7KBBJv15GZLKfHPjDUuxW3u43/
ZmyBM+1Fs91jt0v5w1dIDF0z1pxwbaRJ3w1M1kEU8i6/q+1YaahYvdeaa0jsdSsy
kpz3YhZtb324TKmjfUFMzYvfcoR8IYDkekQ=
-----END CERTIFICATE-----
```

## File: `test/util/https-server/server/fullchain.pem`
```
-----BEGIN CERTIFICATE-----
MIIDRjCCAi4CFGCNNJXfcHchSO1xHnWt5wcENGznMA0GCSqGSIb3DQEBCwUAMGcx
CzAJBgNVBAYTAlVTMQ0wCwYDVQQIDARVdGFoMQ4wDAYDVQQHDAVQcm92bzEjMCEG
A1UECgwaQUNNRSBTaWduaW5nIEF1dGhvcml0eSBJbmMxFDASBgNVBAMMC2V4YW1w
bGUuY29tMB4XDTI0MTIxMTEzMTMyMloXDTI2MDQyNTEzMTMyMlowWDELMAkGA1UE
BhMCVVMxDTALBgNVBAgMBFV0YWgxDjAMBgNVBAcMBVByb3ZvMRYwFAYDVQQKDA1B
Q01FIFRlY2ggSW5jMRIwEAYDVQQDDAlsb2NhbGhvc3QwggEiMA0GCSqGSIb3DQEB
AQUAA4IBDwAwggEKAoIBAQC1+BYy7XcJoIAHqPcU7f74Dp/6N6f/hjLTADMIT1OO
49W3Rrc6xbJjeLsiTD0Rj9Z/9CSI7Vh/AOLoW7OGMOZkJZNRw8L9lc14ZDB1FAcJ
ITn8c9d0d0YltbxUOq509wEP6GSxYCqYZlvAjeyYADRW5PnP82n6MRMW9Ve5y50s
ijeaVk120je5zKvQTd0IR9rXf8K3M8CmnlEVuuf4+uXvg0gUsGvSSkBxPVGeUQHM
/zRxj/I8WYCewb9Qs2TSJjgnFsfUCF6C3xs/T8p4vJ8PxeLs6GNcQhhtNH0q7Wxa
IV4cdrXkxPi6YS8ph1WErqNR2pdsCA5bUNTCT32vPjr/AgMBAAEwDQYJKoZIhvcN
AQELBQADggEBACu1hC1yvFKF6nEjz4mdTmVIyqktfkQX4+5edpSCLM0UhOmQ9Tm3
3NnQ06YhPnAkiXLiyKxoCGqulgh1B1+3Ii0/ttDq4D4HIEVMwT5Hmko3vppUkJD7
aIacmTKxGFrtF+p1hIDXmAAYFUB2bWDgVvba2z70DkbffJBOwe/+2+hOgFXI5x3+
IJuF0bYKRlFG0yvVX+ooWAaKmCSR4reCsjWNuP7KBBJv15GZLKfHPjDUuxW3u43/
ZmyBM+1Fs91jt0v5w1dIDF0z1pxwbaRJ3w1M1kEU8i6/q+1YaahYvdeaa0jsdSsy
kpz3YhZtb324TKmjfUFMzYvfcoR8IYDkekQ=
-----END CERTIFICATE-----
```

## File: `test/util/https-server/server/my-private-root-ca.cert.pem`
```
-----BEGIN CERTIFICATE-----
MIIDrzCCApegAwIBAgIUUAyKcu86WuJQd1fdlHsXkCl1mYMwDQYJKoZIhvcNAQEL
BQAwZzELMAkGA1UEBhMCVVMxDTALBgNVBAgMBFV0YWgxDjAMBgNVBAcMBVByb3Zv
MSMwIQYDVQQKDBpBQ01FIFNpZ25pbmcgQXV0aG9yaXR5IEluYzEUMBIGA1UEAwwL
ZXhhbXBsZS5jb20wHhcNMjQxMjExMTMxMzIyWhcNMjcxMDAxMTMxMzIyWjBnMQsw
CQYDVQQGEwJVUzENMAsGA1UECAwEVXRhaDEOMAwGA1UEBwwFUHJvdm8xIzAhBgNV
BAoMGkFDTUUgU2lnbmluZyBBdXRob3JpdHkgSW5jMRQwEgYDVQQDDAtleGFtcGxl
LmNvbTCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAKlp3Kz278oyTDY4
+1iNv1xMzWCJBWf7YxyYkXACVvZzUqgwxotNwAE/kE131HgpBJnu7HsDdS8nLy80
mDkFCGmqEuVZMDaMGtcz3HJSklESjxYM1VNgifz2IlNmoaidNehFkCi1rz6cLMR0
rEZpi98EbVZGl3n0vDD0eEZF5QQn/eDwclt/aKVBVLcQxo6MHhQdaK85a1uNyUU3
HPUYiyPGVn9oX9PGcOpYFomJoBdg3sUVk32xKCUf15+uqVchdtyGFW/bp5KSBCnB
QD0TzN+SgBHnVTzIfoi8WY56uuwnYauvT4fRh8SfkV91BzHBtWSbulNTfTUzgWhs
VvCGw7ECAwEAAaNTMFEwHQYDVR0OBBYEFC4qTshaPoBie1ukhhM0KBi95NzJMB8G
A1UdIwQYMBaAFC4qTshaPoBie1ukhhM0KBi95NzJMA8GA1UdEwEB/wQFMAMBAf8w
DQYJKoZIhvcNAQELBQADggEBAB+fRdUHgqwpTWRfF+jQB4Af75HTfp6hgemUjapI
eZn/OugS75/jfJt9npVsHl/aa63GL/W6kQShoMVOhrYqW52J1TSsLKZR2L7sv0ji
KYfakv+aLkRKewPoVadsCL8GUmaCByE9mwlhmmZprkjDmA3hWsjEM5lyg7qleJ0k
V32FVysdhLLnftt2SJB7lyoTujhkNAjJhLT/0Qr8t59v0sViPtL8532jSXqE1GK+
zncsJDK7v2VEuurz1lPTRY6tPQOJ1Qt8vUzDH/ugcc5JPBEuHhjjrd5K65lxnGNw
lnPHIS7FJm1OMkuatQXomNuuoWDPyM7fuVyGUUpmlkbpJsg=
-----END CERTIFICATE-----
```

## File: `test/util/https-server/server/privkey.pem`
```
-----BEGIN PRIVATE KEY-----
MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQC1+BYy7XcJoIAH
qPcU7f74Dp/6N6f/hjLTADMIT1OO49W3Rrc6xbJjeLsiTD0Rj9Z/9CSI7Vh/AOLo
W7OGMOZkJZNRw8L9lc14ZDB1FAcJITn8c9d0d0YltbxUOq509wEP6GSxYCqYZlvA
jeyYADRW5PnP82n6MRMW9Ve5y50sijeaVk120je5zKvQTd0IR9rXf8K3M8CmnlEV
uuf4+uXvg0gUsGvSSkBxPVGeUQHM/zRxj/I8WYCewb9Qs2TSJjgnFsfUCF6C3xs/
T8p4vJ8PxeLs6GNcQhhtNH0q7WxaIV4cdrXkxPi6YS8ph1WErqNR2pdsCA5bUNTC
T32vPjr/AgMBAAECggEAHeLCZpfYmpSpIljuR5o063GfdZ1pco6MT1ozh3Rb0VZ6
9bBgDH+Gpk6gUWg7CWTZwkcLLw/oHme7XJUe/XWPiTggo2em4TYWumSeDsR8yVOT
LfKqmp6yPyRDa4P9vgkJPB8bVoRoSoJZJF1K08YI0pKlsrEUITqpG3as8z9NL5C1
65QdpCwiRjLnM6b7k93Vxa8xOnj51iDXV9uqGASCYmU+uoHG8HU8RzbVI4Xi/RCr
PszmOi6AMtWPpzH2jDPiYnv96K50O/cOm/n3obuySdH0qeGR37sx94F82iCyiowo
Ij+iU8VYK6gu27z811ehSlk3/4ey8ArlHvVew3TkqQKBgQD+K70baVqolcGfkDQY
zgZ+4YlmncDrdhd0anHUEC15l7uPPHFBxrQlzRVTjhHCKn1sQTj/41isUWQAvcRR
ZzjI+YaHQvvzJCSX6c113IWeemCcuTxenW6G/5BHJxOPddFnrcAAoeHhcNvni/CZ
WrInTIcWn7eY5MMaxa4ELUoKRwKBgQC3R1R9be3BY36wPYcPkTZFxRAn2o7/Z2Ft
MDbrddDZt12F7cuD8YnipI7TkJLQTXmg6P7u2XexcEyAUy2J+jdgfpM0N/HXu3Su
YeYXHJfyGUK6bTlQT+trNuEyX5K7h2IbBstvH9A4PXEZPQ2I3aPZk3WsL630cMo6
tbTy0o3tiQKBgQCv11qxSCXsVA7scTtZnc9ooGgKkkERpVV8uNefOsH7STn9UneY
Zfvj2wpSEAvBJNw4tLbWcVa7gGOLD75uAteKUvb7RSBBilO2tY3raHEYvtlwE8bs
PkZlJxGN6D7kFUKWU+JtjZFUAlxgyLPfpJt0DMG4qS6/nCROtUw6n4qFqQKBgB2S
JrGuIORI91HcO4Rpe4Y6S2cCvnu65F9HnjTTZ4UZLr/DJEj/ma21u02rT+TH+03Z
CfjjoYpBgjZaNUjD1Fd/VKTiOeUC28qfBQ7JkEKBjOCjatHocyVzT1ZfUT9skoml
yQD+8wt/7lWSIjLo/9zFDAFiGAEOibJ7Sty62CdxAoGBAJLwVkDCT3yylDRqm2YC
1uYh/xGLW4F/Jj7PjGNrSYClkbxPTpd4Nfa8EyZmUUya1rsfK1njXZKbwwpa2fbE
+QVpXB18vaMW3hU7u63JDpLv2pCm91myPMQsF3xMc/S1vFAOWmXetYWax4/xiG2M
SW4m9mBkzzF/2SpxQd9xy1Jx
-----END PRIVATE KEY-----
```

## File: `types/config.d.ts`
```typescript
import { Hooks } from './hooks';

export interface Config {
  hooks?: Hooks;

  plugins?: Record<string, Record<string, any>>;

  git?: {
    /** @default "git log --pretty=format:\"* %s (%h)\" ${from}...${to}" */
    changelog?: string;

    /** @default true */
    requireCleanWorkingDir?: boolean;

    /** @default false */
    requireBranch?: false | string;

    /** @default true */
    requireUpstream?: boolean;

    /** @default false */
    requireCommits?: boolean;

    /** @default true */
    requireCommitsFail?: boolean;

    /** @default "" */
    commitsPath?: string;

    /** @default false */
    addUntrackedFiles?: boolean;

    /** @default true */
    commit?: boolean;

    /** @default "Release ${version}" */
    commitMessage?: string;

    commitArgs?: Array<any>;

    /** @default true */
    tag?: boolean;

    /** @default null */
    tagExclude?: any;

    /** @default null */
    tagName?: any;

    /** @default null */
    tagMatch?: any;

    /** @default false */
    getLatestTagFromAllRefs?: boolean;

    /** @default "Release ${version}" */
    tagAnnotation?: string;

    tagArgs?: Array<any>;

    /** @default true */
    push?: boolean;

    /** @default ["--follow-tags"] */
    pushArgs?: Array<string>;

    /** @default "" */
    pushRepo?: string;
  };

  npm?: {
    /** @default true */
    publish?: boolean;

    /** @default "." */
    publishPath?: string;

    publishArgs?: Array<any>;

    /** @default "npm" */
    publishPackageManager?: 'npm' | 'pnpm' | 'bun';

    /** @default null */
    tag?: any;

    /** @default null */
    otp?: any;

    /** @default false */
    ignoreVersion?: boolean;

    /** @default false */
    allowSameVersion?: boolean;

    versionArgs?: Array<any>;

    /** @default false */
    skipChecks?: boolean;

    /** @default 10 */
    timeout?: number;
  };

  github?: {
    /** @default false */
    release?: boolean;

    /** @default "Release ${version}" */
    releaseName?: string;

    /** @default null */
    releaseNotes?: string | null | (() => string | Promise<string>) | { commit?: string; excludeMatches?: string[] };

    /** @default false */
    autoGenerate?: boolean;

    /** @default false */
    preRelease?: boolean;

    /** @default false */
    draft?: boolean;

    /** @default "GITHUB_TOKEN" */
    tokenRef?: string;

    /** @default null */
    assets?: any;

    /** @default null */
    host?: any;

    /** @default 0 */
    timeout?: number;

    /** @default null */
    proxy?: any;

    /**
     * @default true
     * 'legacy' - Github determines the latest release based on the release creation date and higher semantic version.
     * See https://docs.github.com/en/rest/releases/releases?apiVersion=latest#create-a-release
     */
    makeLatest?: boolean | 'legacy';

    /** @default false */
    discussionCategoryName?: boolean | string;

    /** @default false */
    skipChecks?: boolean;

    /** @default false */
    web?: boolean;

    comments?: {
      /** @default false */
      submit?: boolean;

      /** @default ":rocket?: _This issue has been resolved in v${version}. See [${releaseName}](${releaseUrl}) for release notes._" */
      issue?: string;

      /** @default ":rocket?: _This pull request is included in v${version}. See [${releaseName}](${releaseUrl}) for release notes._" */
      pr?: string;
    };
  };

  gitlab?: {
    /** @default false */
    release?: boolean;

    /** @default "Release ${version}" */
    releaseName?: string;

    /** @default null */
    releaseNotes?: any;

    milestones?: Array<any>;

    /** @default "GITLAB_TOKEN" */
    tokenRef?: string;

    /** @default "Private-Token" */
    tokenHeader?: string;

    /** @default null */
    certificateAuthorityFile?: any;

    /** @default false */
    secure?: boolean;

    /** @default null */
    assets?: any;

    /** @default false */
    useIdsForUrls?: boolean;

    /** @default false */
    useGenericPackageRepositoryForAssets?: boolean;

    /** @default "release-it" */
    genericPackageRepositoryName?: string;

    /** @default null */
    origin?: any;

    /** @default false */
    skipChecks?: boolean;
  };
}
```

## File: `types/hooks.d.ts`
```typescript
export type HookPrefix = 'before' | 'after';
export type InternalPlugin = 'version' | 'git' | 'npm' | 'github' | 'gitlab';
export type HookName = 'init' | 'bump' | 'release';

export type Hooks = {
  ['before:init']?: string | string[];
  ['before:bump']?: string | string[];
  ['before:release']?: string | string[];
  ['after:init']?: string | string[];
  ['after:bump']?: string | string[];
  ['after:release']?: string | string[];

  ['before:version:init']?: string | string[];
  ['before:version:bump']?: string | string[];
  ['before:version:release']?: string | string[];
  ['after:version:init']?: string | string[];
  ['after:version:bump']?: string | string[];
  ['after:version:release']?: string | string[];

  ['before:git:init']?: string | string[];
  ['before:git:bump']?: string | string[];
  ['before:git:release']?: string | string[];
  ['after:git:init']?: string | string[];
  ['after:git:bump']?: string | string[];
  ['after:git:release']?: string | string[];

  ['before:npm:init']?: string | string[];
  ['before:npm:bump']?: string | string[];
  ['before:npm:release']?: string | string[];
  ['after:npm:init']?: string | string[];
  ['after:npm:bump']?: string | string[];
  ['after:npm:release']?: string | string[];

  ['before:github:init']?: string | string[];
  ['before:github:bump']?: string | string[];
  ['before:github:release']?: string | string[];
  ['after:github:init']?: string | string[];
  ['after:github:bump']?: string | string[];
  ['after:github:release']?: string | string[];

  ['before:gitlab:init']?: string | string[];
  ['before:gitlab:bump']?: string | string[];
  ['before:gitlab:release']?: string | string[];
  ['after:gitlab:init']?: string | string[];
  ['after:gitlab:bump']?: string | string[];
  ['after:gitlab:release']?: string | string[];
};
```

## File: `types/index.d.ts`
```typescript
declare module 'release-it';

export type { Config } from './config.d';
```

