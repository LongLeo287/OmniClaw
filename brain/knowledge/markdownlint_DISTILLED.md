---
id: markdownlint
type: knowledge
owner: OA_Triage
---
# markdownlint
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: package.json
```json
{
  "name": "markdownlint-cli2",
  "version": "0.22.0",
  "description": "A fast, flexible, configuration-based command-line interface for linting Markdown/CommonMark files with the `markdownlint` library",
  "author": {
    "name": "David Anson",
    "url": "https://dlaa.me/"
  },
  "license": "MIT",
  "type": "module",
  "exports": {
    ".": "./markdownlint-cli2.mjs",
    "./markdownlint": "./export-markdownlint.mjs",
    "./markdownlint/helpers": "./export-markdownlint-helpers.mjs",
    "./markdownlint/promise": "./export-markdownlint-promise.mjs",
    "./parsers": "./parsers/parsers.mjs",
    "./parsers/jsonc": "./parsers/jsonc-parse.mjs",
    "./parsers/toml": "./parsers/toml-parse.mjs",
    "./parsers/yaml": "./parsers/yaml-parse.mjs"
  },
  "bin": {
    "markdownlint-cli2": "markdownlint-cli2-bin.mjs"
  },
  "homepage": "https://github.com/DavidAnson/markdownlint-cli2",
  "repository": {
    "type": "git",
    "url": "git+https://github.com/DavidAnson/markdownlint-cli2.git"
  },
  "bugs": "https://github.com/DavidAnson/markdownlint-cli2/issues",
  "funding": "https://github.com/sponsors/DavidAnson",
  "scripts": {
    "build-docker-image": "VERSION=$(node -e \"process.stdout.write(require('./package.json').version)\") && docker build -t davidanson/markdownlint-cli2:v$VERSION -f docker/Dockerfile --label org.opencontainers.image.version=v$VERSION .",
    "build-docker-image-rules": "VERSION=$(node -e \"process.stdout.write(require('./package.json').version)\") && docker build -t davidanson/markdownlint-cli2-rules:v$VERSION -f docker/Dockerfile-rules --build-arg VERSION=v$VERSION --label org.opencontainers.image.version=v$VERSION .",
    "ci": "npm-run-all --continue-on-error --parallel test-cover lint schema && git diff --exit-code",
    "lint": "eslint --max-warnings 0",
    "lint-dockerfile": "docker run --rm -i hadolint/hadolint:latest-alpine < docker/Dockerfile",
    "lint-watch": "git ls-files | entr npm run lint",
    "playwright-install-bare": "npm run playwright-install-npm && playwright install",
    "playwright-install-npm": "npm install --no-save playwright@1.58.2",
    "playwright-test": "playwright test --config ./webworker/playwright.config.mjs",
    "playwright-test-docker": "docker run --rm --volume $PWD:/home/workdir --workdir /home/workdir --ipc=host mcr.microsoft.com/playwright:v1.58.2 npm run playwright-test",
    "schema": "cpy ./node_modules/markdownlint/schema/markdownlint-config-schema.json ./schema --flat",
    "test": "ava --timeout=1m test/append-to-array-test.mjs test/constants-test.mjs test/fs-virtual-test.mjs test/markdownlint-cli2-test.mjs test/markdownlint-cli2-test-exec.mjs test/markdownlint-cli2-test-exports.mjs test/markdownlint-cli2-test-formatters.mjs test/markdownlint-cli2-test-fs.mjs test/markdownlint-cli2-test-main.mjs test/merge-options-test.mjs",
    "test-cover": "c8 --100 npm test",
    "test-docker-hub-image": "VERSION=$(node -e \"process.stdout.write(require('./package.json').version)\") && docker image rm davidanson/markdownlint-cli2:v$VERSION davidanson/markdownlint-cli2:latest || true && docker run --rm -v $PWD:/workdir davidanson/markdownlint-cli2:v$VERSION \"*.md\" && docker run --rm -v $PWD:/workdir davidanson/markdownlint-cli2:latest \"*.md\"",
    "test-docker-hub-image-rules": "VERSION=$(node -e \"process.stdout.write(require('./package.json').version)\") && docker image rm davidanson/markdownlint-cli2-rules:v$VERSION davidanson/markdownlint-cli2-rules:latest || true && docker run --rm -v $PWD:/workdir davidanson/markdownlint-cli2-rules:v$VERSION \"*.md\" && docker run --rm -v $PWD:/workdir davidanson/markdownlint-cli2-rules:latest \"*.md\"",
    "test-docker-image": "VERSION=$(node -e \"process.stdout.write(require('./package.json').version)\") && docker run --rm -v $PWD:/workdir davidanson/markdownlint-cli2:v$VERSION \"*.md\"",
    "test-docker-image-rules": "VERSION=$(node -e \"process.stdout.write(require('./package.json').version)\") && docker run --rm -v $PWD:/workdir davidanson/markdownlint-cli2-rules:v$VERSION \"*.md\"",
    "test-invoke-as-cli": "markdownlint-cli2 CHANGELOG.md",
    "test-watch": "git ls-files | entr npm run test",
    "update-snapshots": "ava --timeout=1m --update-snapshots test/markdownlint-cli2-test-exec.mjs test/markdownlint-cli2-test-exports.mjs test/markdownlint-cli2-test-formatters.mjs test/markdownlint-cli2-test-fs.mjs test/markdownlint-cli2-test-main.mjs",
    "webworker": "cd webworker && webpack --mode none",
    "webworker-install": "npm install --no-save path-browserify setimmediate stream-browserify util webpack-cli && cpy ./node_modules/setimmediate/setImmediate.js ./webworker --flat --rename=setImmediate.cjs"
  },
  "engines": {
    "node": ">=20"
  },
  "files": [
    "append-to-array.mjs",
    "CHANGELOG.md",
    "constants.mjs",
    "export-markdownlint.mjs",
    "export-markdownlint-helpers.mjs",
    "export-markdownlint-promise.mjs",
    "LICENSE",
    "markdownlint-cli2.mjs",
    "markdownlint-cli2-bin.mjs",
    "merge-options.mjs",
    "parsers/parsers.mjs",
    "parsers/jsonc-parse.mjs",
    "parsers/toml-parse.mjs",
    "parsers/yaml-parse.mjs",
    "README.md",
    "schema/markdownlint-cli2-config-schema.json",
    "schema/markdownlint-config-schema.json",
    "schema/ValidatingConfiguration.md"
  ],
  "dependencies": {
    "globby": "16.1.1",
    "js-yaml": "4.1.1",
    "jsonc-parser": "3.3.1",
    "jsonpointer": "5.0.1",
    "markdownlint": "0.40.0",
    "markdownlint-cli2-formatter-default": "0.0.6",
    "markdown-it": "14.1.1",
    "micromatch": "4.0.8",
    "smol-toml": "1.6.0"
  },
  "devDependencies": {
    "@eslint/js": "10.0.1",
    "@playwright/test": "1.58.2",
    "@stylistic/eslint-plugin": "5.10.0",
    "ajv": "8.18.0",
    "ava": "7.0.0",
    "c8": "11.0.0",
    "cpy": "13.2.1",
    "cpy-cli": "7.0.0",
    "eslint": "10.1.0",
    "eslint-plugin-jsdoc": "62.8.0",
    "eslint-plugin-n": "17.24.0",
    "eslint-plugin-unicorn": "63.0.0",
    "execa": "9.6.1",
    "markdown-it-emoji": "3.0.0",
    "markdown-it-for-inline": "2.0.1",
    "markdownlint-cli2-formatter-codequality": "0.0.7",
    "markdownlint-cli2-formatter-json": "0.0.9",
    "markdownlint-cli2-formatter-junit": "0.0.14",
    "markdownlint-cli2-formatter-pretty": "0.0.10",
    "markdownlint-cli2-formatter-sarif": "0.0.4",
    "markdownlint-cli2-formatter-summarize": "0.0.8",
    "markdownlint-cli2-formatter-template": "0.0.4",
    "markdownlint-rule-extended-ascii": "0.2.1",
    "npm-run-all": "4.1.5",
    "terminal-link": "5.0.0"
  },
  "keywords": [
    "markdown",
    "lint",
    "cli",
    "md",
    "CommonMark",
    "markdownlint"
  ]
}

```

### File: README.md
```md
# markdownlint-cli2

> A fast, flexible, configuration-based command-line interface for linting
> Markdown/CommonMark files with the `markdownlint` library

[![npm version][npm-image]][npm-url]
[![License][license-image]][license-url]

## Install

As a global CLI:

```bash
npm install markdownlint-cli2 --global
```

As a development dependency of the current [Node.js][nodejs] package:

```bash
npm install markdownlint-cli2 --save-dev
```

As a [Docker][docker] container image:

```bash
docker pull davidanson/markdownlint-cli2
```

As a global CLI with [Homebrew][homebrew]:

```bash
brew install markdownlint-cli2
```

As a [GitHub Action][github-action] via
[`markdownlint-cli2-action`][markdownlint-cli2-action]:

```yaml
- name: markdownlint-cli2-action
  uses: DavidAnson/markdownlint-cli2-action@main
```

## Overview

- [`markdownlint`][markdownlint] is a library for linting [Markdown][markdown]/
  [CommonMark][commonmark] files on [Node.js][nodejs] using the
  [markdown-it][markdown-it] parser.
- [`markdownlint-cli`][markdownlint-cli] is a traditional command-line interface
  for `markdownlint`.
- [`markdownlint-cli2`][markdownlint-cli2] is a slightly unconventional
  command-line interface for `markdownlint`.
- `markdownlint-cli2` is configuration-based and prioritizes speed and
  simplicity.
- `markdownlint-cli2` supports all the features of `markdownlint-cli` (sometimes
  a little differently).
- [`vscode-markdownlint`][vscode-markdownlint] is a `markdownlint` extension for
  the [Visual Studio Code editor][vscode].
- `markdownlint-cli2` is designed to work well in conjunction with
  `vscode-markdownlint`.
- More about the [motivation for `markdownlint-cli2`][markdownlint-cli2-blog].

## Use

### Command Line

```text
markdownlint-cli2 vX.Y.Z (markdownlint vX.Y.Z)
https://github.com/DavidAnson/markdownlint-cli2

Syntax: markdownlint-cli2 glob0 [glob1] [...] [globN] [--config file] [--configPointer pointer] [--fix] [--format] [--help] [--no-globs]

Glob expressions (from the globby library):
- * matches any number of characters, but not /
- ? matches a single character, but not /
- ** matches any number of characters, including /
- {} allows for a comma-separated list of "or" expressions
- ! or # at the beginning of a pattern negate the match
- : at the beginning identifies a literal file path
- - as a glob represents standard input (stdin)

Dot-only glob:
- The command "markdownlint-cli2 ." would lint every file in the current directory tree which is probably not intended
- Instead, it is mapped to "markdownlint-cli2 *.{md,markdown}" which lints all Markdown files in the current directory
- To lint every file in the current directory tree, the command "markdownlint-cli2 **" can be used instead

Optional parameters:
- --config        specifies the path to a configuration file to define the base configuration
- --configPointer specifies a JSON Pointer to a configuration object within the --config file
- --fix           updates files to resolve fixable issues (can be overridden in configuration)
- --format        reads standard input (stdin), applies fixes, writes standard output (stdout)
- --help          writes this message to the console and exits without doing anything else
- --no-globs      ignores the "globs" property if present in the top-level options object

Configuration via:
- .markdownlint-cli2.jsonc
- .markdownlint-cli2.yaml
- .markdownlint-cli2.cjs or .markdownlint-cli2.mjs
- .markdownlint.jsonc or .markdownlint.json
- .markdownlint.yaml or .markdownlint.yml
- .markdownlint.cjs or .markdownlint.mjs

Cross-platform compatibility:
- UNIX and Windows shells expand globs according to different rules; quoting arguments is recommended
- Some Windows shells don't handle single-quoted (') arguments well; double-quote (") is recommended
- Shells that expand globs do not support negated patterns (!node_modules); quoting is required here
- Some UNIX shells parse exclamation (!) in double-quotes; hashtag (#) is recommended in these cases
- The path separator is forward slash (/) on all platforms; backslash (\) is automatically converted
- On any platform, passing the parameter "--" causes all remaining parameters to be treated literally

The most compatible syntax for cross-platform support:
$ markdownlint-cli2 "**/*.md" "#node_modules"
```

For scenarios where it is preferable to specify glob expressions in a
configuration file, the `globs` property of `.markdownlint-cli2.jsonc`, `.yaml`,
`.cjs`, or `.mjs` may be used instead of (or in addition to) passing
`glob0 ... globN` on the command-line.

As shown above, a typical command-line for `markdownlint-cli2` looks something
like:

```bash
markdownlint-cli2 "**/*.md" "#node_modules"
```

Because sharing the same configuration between "normal" and "fix" modes is
common, the `--fix` argument can be used to default the `fix` property (see
below) to `true` (though it can still be overridden by a configuration file):

```bash
markdownlint-cli2 --fix "**/*.md" "#node_modules"
```

In cases where it is not convenient to store a configuration file in the root
of a project, the `--config` argument can be used to provide a path to any
supported configuration file/format:

```bash
markdownlint-cli2 --config "config/.markdownlint-cli2.jsonc" "**/*.md" "#node_modules"
```

The configuration file name should be (or end with) one of the supported names
above. For example, `.markdownlint.json` or `example.markdownlint-cli2.jsonc`.
Alternatively, the configuration file name should have a supported extension
like `.jsonc`, `.yaml`, `.mjs`, or `.toml` and its kind (see below) will be
inferred. The configuration file will be loaded, parsed, and applied as a base
configuration for the current directory - which will then be handled normally.

The `--configPointer` argument allows the use of [JSON Pointer][json-pointer]
syntax to identify a sub-object within the configuration file specified by
`--config` (see above). This argument can be used with any configuration file
type and makes it possible to nest configuration data within another file like
`package.json` or `pyproject.toml` (e.g., via `/key` or `/key/subkey`).

For example, a `package.json` file like this:

```json
{
  "...": "...",
  "markdownlint-cli2": {
    "config": {
      "no-multiple-blanks": false
    },
    "noProgress": true
  }
}
```

Could be used like this:

```bash
markdownlint-cli2 --config package.json --configPointer /markdownlint-cli2 "*.md"
```

And a `pyproject.toml` file like this:

```toml
[project]
# ...

[tool.markdownlint-cli2]
noProgress = true

[tool.markdownlint-cli2.config]
no-multiple-blanks = false
```

Could be used like this:

```bash
markdownlint-cli2 --config pyproject.toml --configPointer /tool/markdownlint-cli2 "*.md"
```

**Note**: The [TOML][toml] format is supported by `--config`, `--configPointer`,
and the `extends` configuration property, but *not* for per-directory overrides.

### Container Image

A container image [`davidanson/markdownlint-cli2`][docker-hub-markdownlint-cli2]
can also be used (e.g., as part of a CI pipeline):

```bash
docker run -v $PWD:/workdir davidanson/markdownlint-cli2:v0.22.0 "**/*.md" "#node_modules"
```

Notes:

- As when using the [command line][command-line], glob patterns are passed as
  arguments.
- This image is built on the official [Node.js Docker image][nodejs-docker].
  Per security best practices, the [default user `node`][nodejs-docker-non-root]
  runs with restricted permissions. If it is necessary to run as `root`, pass
  the `-u root` option when invoking `docker`.
- By default, `markdownlint-cli2` will execute within the `/workdir` directory
  *inside the container*. So, as shown above, [bind mount][docker-bind-mounts]
  the project's directory there.
  - A custom working directory can be specified with Docker's `-w` flag:

    ```bash
    docker run -w /myfolder -v $PWD:/myfolder davidanson/markdownlint-cli2:v0.22.0 "**/*.md" "#node_modules"
    ```

For convenience, the container image
[`davidanson/markdownlint-cli2-rules`][docker-hub-markdownlint-cli2-rules]
includes the latest versions of custom rules published to npm with the tag
[`markdownlint-rule`][markdownlint-rule]. These rules are installed globally
onto the base image `davidanson/markdownlint-cli2`.

**Note**: This container image exists for convenience and is not an endorsement
of the rules within.

### Output Formatters

In addition to (or instead of) the default behavior of writing a list of all
issues to the standard error (`stderr`) device, custom output formatters can be
configured to produce a variety of outputs like:

- [List of issues (default)][formatter-default]
- [List of issues with color and links][formatter-pretty]
- [GitLab Code Quality report file][formatter-codequality]
- [JSON file][formatter-json]
- [JUnit XML file][formatter-junit]
- [Static Analysis Results Interchange Format/SARIF file][formatter-sarif]
- [Summary of issues found][formatter-summarize]
- [Flexible string template][formatter-template] supporting:
  - Azure Pipelines Task command LogIssue format
  - GitHub Actions workflow commands format

[formatter-default]: ./formatter-default/README.md
[formatter-codequality]: ./formatter-codequality/README.md
[formatter-json]: ./formatter-json/README.md
[formatter-junit]: ./formatter-junit/README.md
[formatter-pretty]: ./formatter-pretty/README.md
[formatter-sarif]: ./formatter-sarif/README.md
[formatter-summarize]: ./formatter-summarize/README.md
[formatter-template]: ./formatter-template/README.md

For more information, refer to the documentation for the `outputFormatters`
parameter below.

### Exit Codes

- `0`: Linting was successful and there were no errors (there may be warnings)
- `1`: Linting was successful and there were errors (and possibly warnings)
- `2`: Linting was not successful due to a problem or failure

### Formatting

Some editors implement document formatting by invoking an external program,
passing the text of the current document on standard input (`stdin`), and
reading the formatted result from standard output (`stdout`). This scenario is
supported by the `--format` command-line parameter. When `--format` is set:

- Globs and other input sources are ignored
- The `--fix` parameter is implicitly set
- The exit code `1` is not used

## Rule List

- See the [Rules / Aliases][markdownlint-rules-aliases] and
  [Tags][markdownlint-rules-tags] sections of the `markdownlint` documentation.

## Glob expressions

- Globbing is performed by the [globby][globby] library; refer to that
  documentation for more information and examples.

## Configuration

- See the [Configuration][markdownlint-configuration] section of the
  `markdownlint` documentation for information about the inline comment syntax
  for enabling and disabling rules with HTML comments.
- In general, glob expressions should match files under the current directory;
  the configuration for that directory will apply to the entire tree.
  - When glob expressions match files *not* under the current directory,
    configuration for the current directory is applied to the closest common
    parent directory.
- Paths beginning with `~` are resolved relative to the user's home directory
  (typically `$HOME` on UNIX and `%USERPROFILE%` on Windows)
- There are two kinds of configuration file (both detailed below):
  - Configuration files like `.markdownlint-cli2.*` allow complete control of
    `markdownlint-cli2` behavior and are also used by `vscode-markdownlint`.
    - If multiple of these files are present in the same directory, only one is
      used according to the following precedence:
      1. `.markdownlint-cli2.jsonc`
      2. `.markdownlint-cli2.yaml`
      3. `.markdownlint-cli2.cjs`
      4. `.markdownlint-cli2.mjs`
  - Configuration files like `.markdownlint.*` allow control over only the
    `markdownlint` `config` object and tend to be supported more broadly (such
    as by `markdownlint-cli`).
    - If multiple of these files are present in the same directory, only one is
      used according to the following precedence:
      1. `.markdownlint.jsonc`
      2. `.markdownlint.json`
      3. `.markdownlint.yaml`
      4. `.markdownlint.yml`
      5. `.markdownlint.cjs`
      6. `.markdownlint.mjs`
  - Both configuration file types can appear in any directory and will override
    configuration defined in the project root or any directories in between.
- The VS Code extension includes a [JSON Schema][json-schema] definition for the
  `JSON(C)` configuration files described below. This adds auto-complete and can
  make it easier to define proper structure.
- See [markdownlint-cli2-config-schema.json][markdownlint-cli2-config-schema]
  for that schema and [ValidatingConfiguration.md][validating-configuration] for
  ways to use it to validate configuration files.

### `.markdownlint-cli2.jsonc`

- The format of this file is a [JSONC][jsonc] object similar to the
  [`markdownlint` `options` object][markdownlint-options].
- Valid properties are:
  - `config`: [`markdownlint` `config` object][markdownlint-config] to configure
    rules for this part of the directory tree
    - If a `.markdownlint.{jsonc,json,yaml,yml,cjs,mjs}` file (see below) is
      present in the same directory, it overrides the value of this property
    - If the `config` object contains an `extends` property, it will be resolved
      the same as `.markdownlint.{jsonc,json,yaml,yml,cjs,mjs}` (see below)
  - `customRules`: `Array` of `String`s (or `Array`s of `String`s) of module
    names/paths of [custom rules][markdownlint-custom-rules] to load and use
    when linting
    - Relative paths are resolved based on the location of the `JSONC` file
    - Search [`markdownlint-rule` on npm][markdownlint-rule]
  - `fix`: `Boolean` value to enable fixing of linting errors reported by rules
    that emit fix information
    - Fixes are made directly to the relevant file(s); no backup is created
  - `frontMatter`: `String` defining the [`RegExp`][regexp] used to match and
    ignore any [front matter][front-matter] at the beginning of a document
    - The `String` is passed as the `pattern` parameter to the
      [`RegExp` constructor][regexp-constructor]
    - For example: `(^---\s*$[^]*?^---\s*$)(\r\n|\r|\n|$)`
  - `gitignore`: `Boolean` or `String` value to automatically ignore files
    referenced by `.gitignore` (or similar) when linting
    - When the value `true` is specified, all `.gitignore` files in the tree
      *and up to the repository root* are used (default `git` behavior)
    - When a `String` value is specified, that glob pattern is used to identify
      the set of ignore files to use
      - The value `**/.gitignore` corresponds to the `Boolean` value `true` *but
        does not use `.gitignore` files up to the repository root*
      - The value `.gitignore` uses only the file in the root of the tree;
        this is usually equivalent and can be much faster for large trees
    - This top-leve
... [TRUNCATED]
```

### File: .markdownlint.json
```json
{
  "code-block-style": {
    "style": "fenced"
  },
  "code-fence-style": {
    "style": "backtick"
  },
  "emphasis-style": {
    "style": "asterisk"
  },
  "fenced-code-language": {
    "allowed_languages": [
      "bash",
      "html",
      "javascript",
      "json",
      "markdown",
      "text",
      "toml",
      "xml",
      "yaml"
    ],
    "language_only": true
  },
  "heading-style": {
    "style": "atx"
  },
  "hr-style": {
    "style": "---"
  },
  "line-length": {
    "strict": true,
    "code_blocks": false
  },
  "link-image-style": {
    "autolink": false,
    "inline": false,
    "collapsed": false,
    "shortcut": false
  },
  "no-duplicate-heading": {
    "siblings_only": true
  },
  "ol-prefix": {
    "style": "ordered"
  },
  "proper-names": {
    "code_blocks": false,
    "names": [
      "CommonMark",
      "JavaScript",
      "Markdown",
      "markdown-it",
      "markdownlint",
      "markdownlint-cli2",
      "Node.js"
    ]
  },
  "strong-style": {
    "style": "asterisk"
  },
  "table-pipe-style": {
    "style": "leading_and_trailing"
  },
  "ul-style": {
    "style": "dash"
  }
}

```

### File: .pre-commit-hooks.yaml
```yaml
- id: markdownlint-cli2
  name: markdownlint-cli2
  description: "Checks the style of Markdown/CommonMark files."
  entry: markdownlint-cli2
  language: node
  types: [markdown]
- id: markdownlint-cli2-docker
  name: markdownlint-cli2-docker
  description: "Checks the style of Markdown/CommonMark files."
  entry: davidanson/markdownlint-cli2:v0.22.0
  language: docker_image
  types: [markdown]
- id: markdownlint-cli2-rules-docker
  name: markdownlint-cli2-rules-docker
  description: "Checks the style of Markdown/CommonMark files."
  entry: davidanson/markdownlint-cli2-rules:v0.22.0
  language: docker_image
  types: [markdown]

```

### File: CHANGELOG.md
```md
# Changelog

## 0.22.0

- Make `--config` parameter more flexible
- Support TOML with `--config` parameter
- Add `--configPointer` parameter
- Update dependencies

## 0.21.0

- Refactor options/configuration file loading
- Update dependencies

## 0.20.0

- Update dependencies

## 0.19.1

- Update `--format` to avoid trailing newline
- Update dependencies

## 0.19.0

- Add `--format` parameter for editor integration
- Update output formatters for severity `warning`
- Explicitly version Docker containers for `pre-commit`
- Update dependencies (including `markdownlint`)

## 0.18.1

- Update dependencies (including `markdownlint`)

## 0.18.0

- Use user ID in Docker containers for security
- Update dependencies (including `markdownlint`)
- Remove support for end-of-life Node 18

## 0.17.2

- Update dependencies (including `markdownlint`)

## 0.17.1

- Update dependencies (including `markdownlint`)

## 0.17.0

- Convert to ECMAScript modules
- Use import() when loading modules
- Update dependencies (including `markdownlint`)

## 0.16.0

- Try not to use require for modules (due to Node 22.12)
- Update dependencies (EXcluding `markdownlint`)

## 0.15.0

- Add support for `stdin` input via `-` glob
- Add output formatter based on string templates
- Update dependencies (including `markdownlint`)

## 0.14.0

- Handle `--` parameter per POSIX convention
- Add support for glob to `gitignore` configuration
- Update dependencies (including `markdownlint`)

## 0.13.0

- Add `noBanner` and `gitignore` configuration options
- Reduce install size by switching to `js-yaml` package
- Add more detail to some error messages
- Export JSONC/YAML parsers for reuse
- Update dependencies (including `markdownlint`)

## 0.12.1

- Update JSONC parsing to handle trailing commas
- Add documentation links to JSON schema
- Update dependencies

## 0.12.0

- Remove deprecated `markdownlint-cli2-config` entry point
  - Use `markdownlint-cli2 --config ...` instead
- Remove deprecated `markdownlint-cli2-fix` entry point
  - Use `markdownlint-cli2 --fix ...` instead
- Add `--help` and `--no-globs` parameters
- Improve and document included JSON schemas
- Update dependencies (including `markdownlint`)

## 0.11.0

- Add `modulePaths` configuration option
- Update dependencies (including `markdownlint`)
- Remove support for end-of-life Node 16

## 0.10.0

- Add `showFound` configuration option
- Add `.markdownlint-cli2.jsonc` config schema
- Update dependencies (including `markdownlint`)

## 0.9.2

- Remove `npm-shrinkwrap.json` entirely to avoid `npm` failures

## 0.9.1

- Remove `devDependencies` from `npm-shrinkwrap.json` to avoid `npm` failures

## 0.9.0

- Add support for Node.js's `package.json` as a configuration file source
- Add output formatter for Static Analysis Results Interchange Format/SARIF
- Bundle `npm-shrinkwrap.json` for reproducible/faster installs
- Update dependencies (including `markdownlint`)

## 0.8.1

- Handle `--config` edge case

## 0.8.0

- Add support for `--config` and `--fix` parameters
- Update dependencies (including `markdownlint`)
- Remove support for end-of-life Node 14

## 0.7.1

- Update dependencies (including `markdownlint`)

## 0.7.0

- Add support for `extends` in `config` property of `.markdownlint-cli2.*` files
- Build and publish `davidanson/markdownlint-cli2-rules` Docker container image
- Update dependencies (including `markdownlint`)

## 0.6.0

- Update dependencies (including `markdownlint`)

## 0.5.1

- Update dependencies

## 0.5.0

- New rules
- Support modules (MJS) everywhere
- Include dotfiles

## 0.4.0

- New rules
- Async custom rules
- Explicit config
- CJS (breaking)

## 0.3.2

- Extensibility/Windows/consistency improvements

## 0.3.1

- Extensibility tweaks

## 0.3.0

- Add Docker container
- Update dependencies

## 0.2.0

- Improve handling of Windows paths using backslash

## 0.1.3

- Support rule collections

## 0.1.2

- Update use of `require` to be more flexible

## 0.1.1

- Restore previous use of `require`

## 0.1.0

- Simplify use of `require`
- Increment minor version

## 0.0.15

- Improve extensibility

## 0.0.14

- Update dependencies (including `markdownlint`)

## 0.0.13

- Add `markdownlint-cli2-fix` command

## 0.0.12

- Update dependencies (including `markdownlint`)

## 0.0.11

- Improve performance of `fix`
- Update banner

## 0.0.10

- Improve performance and configuration

## 0.0.9

- Improve configuration file handling

## 0.0.8

- Support `.markdownlint-cli2.yaml`
- Add progress

## 0.0.7

- Support `.markdownlint-cli2.js` and `.markdownlint.js`

## 0.0.6

- Improve handling of very large directory trees

## 0.0.5

- Improve support for ignoring files

## 0.0.4

- Support output formatters and `markdown-it` plugins

## 0.0.3

- Feature parity with `markdownlint-cli`

## 0.0.2

- Initial release

```

### File: CONTRIBUTING.md
```md
# Contributing

Interested in contributing? Great! Here are some suggestions to make it a good
experience:

Start by [opening an issue][github-issues], whether to identify a problem or
suggest a change. That issue should be used to discuss the situation and agree
on a plan of action before writing code or sending a pull request. Maybe the
problem isn't really a problem, or maybe there are other things to consider. If
so, it's best to realize that before spending time and effort writing code that
may not get used.

Match the coding style of the files you edit. Although everyone has their own
preferences and opinions, a pull request is not the right forum to debate them.

Package versions for `dependencies` and `devDependencies` should be specified
exactly (also known as "pinning"). The short explanation is that doing otherwise
eventually leads to inconsistent behavior and broken functionality. (See [Why I
pin dependency versions in Node.js packages][version-pinning] for a longer
explanation.)

Add tests for all new/changed functionality. Test positive and negative
scenarios. Try to break the code now, or else it will get broken later.

Run tests via `npm test`. Lint by running `npm run lint`. Run the continuous
integration suite via `npm run ci`. CI tests must pass on all platforms with
100% code coverage.

Pull requests should contain a single commit that addresses a single issue.

Open pull requests against the `next` branch. Include the text "(fixes #??)." at
the end of the commit message so it will be associated with the corresponding
issue. Once merged, the tag `fixed in next` will be added to the issue. When the
commit is merged to the `main` branch during the release process, the issue will
get closed automatically. (See [the GitHub documentation][linking-pull-request]
for details.)

Please refrain from using slang or meaningless placeholder words. Sample content
can be "text", "code", "heading", or the like. Sample URLs should use
[example.com][example-com] which is safe for this purpose. Profanity is not
allowed.

In order to maintain the permissive MIT license this project uses, all
contributions must be your own and released under that license. Code you add
should be an original work and should not be copied from elsewhere. Taking code
from a different project, Stack Overflow, or the like is not allowed. The use of
tools such as GitHub Copilot, ChatGPT, LLMs (large language models), etc. that
incorporate code from other projects is not allowed.

Thank you!

[example-com]: https://en.wikipedia.org/wiki/Example.com
[github-issues]: https://github.com/DavidAnson/markdownlint-cli2/issues
[linking-pull-request]: https://docs.github.com/en/github/managing-your-work-on-github/linking-a-pull-request-to-an-issue#linking-a-pull-request-to-an-issue-using-a-keyword
[version-pinning]: https://dlaa.me/blog/post/versionpinning

```

### File: .github\dictionary.txt
```txt
Async
Changelog
CJS
CLI
CodeClimate
CommonJS
CommonMark
config
dotfiles
formatter
formatters
Formatters
GitLab
Globbing
globby
Homebrew
JSON
JSONC
JUnit
LLMs
LogIssue
markdownlint-cli2
markdownlint-cli2-formatter-codequality
markdownlint-cli2-formatter-default
markdownlint-cli2-formatter-json
markdownlint-cli2-formatter-junit
markdownlint-cli2-formatter-pretty
markdownlint-cli2-formatter-sarif
markdownlint-cli2-formatter-summarize
markdownlint-cli2-formatter-template
npm
parsers
POSIX
pre-commit
SARIF
schemas
subdirectories
syntaxes
TOML
YAML

```

### File: doc\OutputFormatters.md
```md
# Output Formatters

`markdownlint-cli2` lets you customize its output by specifying one or more
output formatters in its [configuration file][configuration-file]. Output
formatters can be defined by scripts within a project or imported from a package
([keyword `markdownlint-cli2-formatter` on npm][markdownlint-cli2-formatter]).

## Authoring

Output formatters are called after linting is done and are passed arguments that
include the results, logging functions, and formatter parameters. They are
expected to return a `Promise` that resolves when output formatting is complete
or `void` if execution completes synchronously.

Output formatters export a function like:

```javascript
module.exports = (options, params) => { ... }
```

Where `options` is an object that looks like:

- `directory`: `String` that identifies the base directory for relative paths
  (using POSIX syntax)
- `results`: `Array` of [`markdownlint` `LintError` objects][markdownlint-d-ts],
  each with an added `String` property `fileName` containing a relative path
- `logMessage`: `Function` that takes a single `String` argument and logs it to
  standard output
- `logError`: `Function` that takes a single `String` argument and logs it to
  standard error

And `params` is an object containing formatter parameters from configuration.

For a `.markdownlint-cli2.jsonc` like:

```json
{
  "outputFormatters": [
    [ "markdownlint-cli2-formatter-json", { "name": "custom-name.json", "spaces": 1 } ]
  ]
}
```

`params` would be:

```json
{
  "name": "custom-name.json",
  "spaces": 1
}
```

## Examples

- [Default formatter][formatter-default]
- [Code Quality formatter][formatter-codequality]
- [JUnit formatter][formatter-junit]
- [SARIF formatter][formatter-sarif]

[configuration-file]: https://github.com/DavidAnson/markdownlint-cli2#configuration
[formatter-default]: ../formatter-default/markdownlint-cli2-formatter-default.js
[formatter-codequality]: ../formatter-codequality/markdownlint-cli2-formatter-codequality.js
[formatter-junit]: ../formatter-junit/markdownlint-cli2-formatter-junit.js
[formatter-sarif]: ../formatter-sarif/markdownlint-cli2-formatter-sarif.js
[markdownlint-cli2-formatter]: https://www.npmjs.com/search?q=keywords:markdownlint-cli2-formatter
[markdownlint-d-ts]: https://github.com/DavidAnson/markdownlint/blob/v0.40.0/lib/markdownlint.d.mts

```

### File: schema\markdownlint-cli2-config-schema.json
```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "$id": "https://raw.githubusercontent.com/DavidAnson/markdownlint-cli2/v0.22.0/schema/markdownlint-cli2-config-schema.json",
  "title": "markdownlint-cli2 configuration schema",
  "type": "object",
  "properties": {
    "$schema": {
      "description": "JSON Schema URI (expected by some editors)",
      "type": "string",
      "default": "https://raw.githubusercontent.com/DavidAnson/markdownlint-cli2/v0.22.0/schema/markdownlint-cli2-config-schema.json"
    },
    "config": {
      "description": "markdownlint configuration schema : https://github.com/DavidAnson/markdownlint/blob/v0.40.0/schema/.markdownlint.jsonc",
      "$ref": "https://raw.githubusercontent.com/DavidAnson/markdownlint/v0.40.0/schema/markdownlint-config-schema.json",
      "default": {}
    },
    "customRules": {
      "description": "Module names or paths of custom rules to load and use when linting : https://github.com/DavidAnson/markdownlint-cli2/blob/v0.22.0/README.md#markdownlint-cli2jsonc",
      "type": "array",
      "default": [],
      "items": {
        "description": "Module name or path of a custom rule",
        "type": "string",
        "minLength": 1
      }
    },
    "fix": {
      "description": "Whether to enable fixing of linting errors reported by rules that emit fix information : https://github.com/DavidAnson/markdownlint-cli2/blob/v0.22.0/README.md#markdownlint-cli2jsonc",
      "type": "boolean",
      "default": false
    },
    "frontMatter": {
      "description": "Regular expression used to match and ignore any front matter at the beginning of a document : https://github.com/DavidAnson/markdownlint-cli2/blob/v0.22.0/README.md#markdownlint-cli2jsonc",
      "type": "string",
      "minLength": 1,
      "default": ""
    },
    "gitignore": {
      "description": "Whether to ignore files referenced by .gitignore (or glob expression) (only valid at the root) : https://github.com/DavidAnson/markdownlint-cli2/blob/v0.22.0/README.md#markdownlint-cli2jsonc",
      "type": [
        "boolean",
        "string"
      ],
      "default": false
    },
    "globs": {
      "description": "Glob expressions to include when linting (only valid at the root) : https://github.com/DavidAnson/markdownlint-cli2/blob/v0.22.0/README.md#markdownlint-cli2jsonc",
      "type": "array",
      "default": [],
      "items": {
        "description": "Glob expression of files to lint",
        "type": "string",
        "minLength": 1
      }
    },
    "ignores": {
      "description": "Glob expressions to ignore when linting : https://github.com/DavidAnson/markdownlint-cli2/blob/v0.22.0/README.md#markdownlint-cli2jsonc",
      "type": "array",
      "default": [],
      "items": {
        "description": "Glob expression of files to ignore",
        "type": "string",
        "minLength": 1
      }
    },
    "markdownItPlugins": {
      "description": "markdown-it plugins to load and use when linting : https://github.com/DavidAnson/markdownlint-cli2/blob/v0.22.0/README.md#markdownlint-cli2jsonc",
      "type": "array",
      "default": [],
      "items": {
        "description": "Name or path of a markdown-it plugin followed by parameters",
        "type": "array",
        "items": [
          {
            "description": "Name or path of a markdown-it plugin",
            "type": "string",
            "minLength": 1
          },
          {
            "description": "Parameter(s) to pass to the markdown-it plugin"
          }
        ],
        "minItems": 1
      }
    },
    "modulePaths": {
      "description": "Additional paths to resolve module locations from : https://github.com/DavidAnson/markdownlint-cli2/blob/v0.22.0/README.md#markdownlint-cli2jsonc",
      "type": "array",
      "default": [],
      "items": {
        "description": "Path to resolve module locations from",
        "type": "string",
        "minLength": 1
      }
    },
    "noBanner": {
      "description": "Whether to disable the display of the banner message and version numbers on stdout (only valid at the root) : https://github.com/DavidAnson/markdownlint-cli2/blob/v0.22.0/README.md#markdownlint-cli2jsonc",
      "type": "boolean",
      "default": false
    },
    "noInlineConfig": {
      "description": "Whether to disable support of HTML comments within Markdown content : https://github.com/DavidAnson/markdownlint-cli2/blob/v0.22.0/README.md#markdownlint-cli2jsonc",
      "type": "boolean",
      "default": false
    },
    "noProgress": {
      "description": "Whether to disable the display of progress on stdout (only valid at the root) : https://github.com/DavidAnson/markdownlint-cli2/blob/v0.22.0/README.md#markdownlint-cli2jsonc",
      "type": "boolean",
      "default": false
    },
    "outputFormatters": {
      "description": "Output formatters to load and use to customize markdownlint-cli2 output (only valid at the root) : https://github.com/DavidAnson/markdownlint-cli2/blob/v0.22.0/README.md#markdownlint-cli2jsonc",
      "type": "array",
      "default": [],
      "items": {
        "description": "Name or path of an output formatter followed by parameters",
        "type": "array",
        "items": [
          {
            "description": "Name or path of an output formatter",
            "type": "string",
            "minLength": 1
          },
          {
            "description": "Parameter(s) to pass to the output formatter"
          }
        ],
        "minItems": 1
      }
    },
    "showFound": {
      "description": "Whether to show the list of found files on stdout (only valid at the root) : https://github.com/DavidAnson/markdownlint-cli2/blob/v0.22.0/README.md#markdownlint-cli2jsonc",
      "type": "boolean",
      "default": false
    }
  },
  "additionalProperties": false
}

```

### File: schema\markdownlint-config-schema.json
```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "$id": "https://raw.githubusercontent.com/DavidAnson/markdownlint/v0.40.0/schema/markdownlint-config-schema.json",
  "title": "markdownlint configuration schema",
  "type": "object",
  "properties": {
    "$schema": {
      "description": "JSON Schema URI (expected by some editors)",
      "type": "string",
      "default": "https://raw.githubusercontent.com/DavidAnson/markdownlint/v0.40.0/schema/markdownlint-config-schema.json"
    },
    "default": {
      "description": "Default state for all rules",
      "oneOf": [
        {
          "type": "boolean"
        },
        {
          "enum": [
            "error",
            "warning"
          ]
        }
      ],
      "default": true
    },
    "extends": {
      "description": "Path to configuration file to extend",
      "type": [
        "string",
        "null"
      ],
      "default": null
    },
    "MD001": {
      "description": "MD001/heading-increment : Heading levels should only increment by one level at a time : https://github.com/DavidAnson/markdownlint/blob/v0.40.0/doc/md001.md",
      "oneOf": [
        {
          "type": "boolean"
        },
        {
          "enum": [
            "error",
            "warning"
          ]
        },
        {
          "type": "object",
          "additionalProperties": false,
          "properties": {
            "enabled": {
              "description": "Whether to enable the rule",
              "type": "boolean",
              "default": true
            },
            "severity": {
              "description": "Rule severity",
              "type": "string",
              "enum": [
                "error",
                "warning"
              ],
              "default": "error"
            },
            "front_matter_title": {
              "description": "RegExp for matching title in front matter",
              "type": "string",
              "default": "^\\s*title\\s*[:=]"
            }
          }
        }
      ],
      "default": true
    },
    "heading-increment": {
      "description": "MD001/heading-increment : Heading levels should only increment by one level at a time : https://github.com/DavidAnson/markdownlint/blob/v0.40.0/doc/md001.md",
      "oneOf": [
        {
          "type": "boolean"
        },
        {
          "enum": [
            "error",
            "warning"
          ]
        },
        {
          "type": "object",
          "additionalProperties": false,
          "properties": {
            "enabled": {
              "description": "Whether to enable the rule",
              "type": "boolean",
              "default": true
            },
            "severity": {
              "description": "Rule severity",
              "type": "string",
              "enum": [
                "error",
                "warning"
              ],
              "default": "error"
            },
            "front_matter_title": {
              "description": "RegExp for matching title in front matter",
              "type": "string",
              "default": "^\\s*title\\s*[:=]"
            }
          }
        }
      ],
      "default": true
    },
    "MD003": {
      "description": "MD003/heading-style : Heading style : https://github.com/DavidAnson/markdownlint/blob/v0.40.0/doc/md003.md",
      "oneOf": [
        {
          "type": "boolean"
        },
        {
          "enum": [
            "error",
            "warning"
          ]
        },
        {
          "type": "object",
          "additionalProperties": false,
          "properties": {
            "enabled": {
              "description": "Whether to enable the rule",
              "type": "boolean",
              "default": true
            },
            "severity": {
              "description": "Rule severity",
              "type": "string",
              "enum": [
                "error",
                "warning"
              ],
              "default": "error"
            },
            "style": {
              "description": "Heading style",
              "type": "string",
              "enum": [
                "consistent",
                "atx",
                "atx_closed",
                "setext",
                "setext_with_atx",
                "setext_with_atx_closed"
              ],
              "default": "consistent"
            }
          }
        }
      ],
      "default": true
    },
    "heading-style": {
      "description": "MD003/heading-style : Heading style : https://github.com/DavidAnson/markdownlint/blob/v0.40.0/doc/md003.md",
      "oneOf": [
        {
          "type": "boolean"
        },
        {
          "enum": [
            "error",
            "warning"
          ]
        },
        {
          "type": "object",
          "additionalProperties": false,
          "properties": {
            "enabled": {
              "description": "Whether to enable the rule",
              "type": "boolean",
              "default": true
            },
            "severity": {
              "description": "Rule severity",
              "type": "string",
              "enum": [
                "error",
                "warning"
              ],
              "default": "error"
            },
            "style": {
              "description": "Heading style",
              "type": "string",
              "enum": [
                "consistent",
                "atx",
                "atx_closed",
                "setext",
                "setext_with_atx",
                "setext_with_atx_closed"
              ],
              "default": "consistent"
            }
          }
        }
      ],
      "default": true
    },
    "MD004": {
      "description": "MD004/ul-style : Unordered list style : https://github.com/DavidAnson/markdownlint/blob/v0.40.0/doc/md004.md",
      "oneOf": [
        {
          "type": "boolean"
        },
        {
          "enum": [
            "error",
            "warning"
          ]
        },
        {
          "type": "object",
          "additionalProperties": false,
          "properties": {
            "enabled": {
              "description": "Whether to enable the rule",
              "type": "boolean",
              "default": true
            },
            "severity": {
              "description": "Rule severity",
              "type": "string",
              "enum": [
                "error",
                "warning"
              ],
              "default": "error"
            },
            "style": {
              "description": "List style",
              "type": "string",
              "enum": [
                "consistent",
                "asterisk",
                "plus",
                "dash",
                "sublist"
              ],
              "default": "consistent"
            }
          }
        }
      ],
      "default": true
    },
    "ul-style": {
      "description": "MD004/ul-style : Unordered list style : https://github.com/DavidAnson/markdownlint/blob/v0.40.0/doc/md004.md",
      "oneOf": [
        {
          "type": "boolean"
        },
        {
          "enum": [
            "error",
            "warning"
          ]
        },
        {
          "type": "object",
          "additionalProperties": false,
          "properties": {
            "enabled": {
              "description": "Whether to enable the rule",
              "type": "boolean",
              "default": true
            },
            "severity": {
              "description": "Rule severity",
              "type": "string",
              "enum": [
                "error",
                "warning"
              ],
              "default": "error"
            },
            "style": {
              "description": "List style",
              "type": "string",
              "enum": [
                "consistent",
                "asterisk",
                "plus",
                "dash",
                "sublist"
              ],
              "default": "consistent"
            }
          }
        }
      ],
      "default": true
    },
    "MD005": {
      "description": "MD005/list-indent : Inconsistent indentation for list items at the same level : https://github.com/DavidAnson/markdownlint/blob/v0.40.0/doc/md005.md",
      "oneOf": [
        {
          "type": "boolean"
        },
        {
          "enum": [
            "error",
            "warning"
          ]
        },
        {
          "type": "object",
          "additionalProperties": false,
          "properties": {
            "enabled": {
              "description": "Whether to enable the rule",
              "type": "boolean",
              "default": true
            },
            "severity": {
              "description": "Rule severity",
              "type": "string",
              "enum": [
                "error",
                "warning"
              ],
              "default": "error"
            }
          }
        }
      ],
      "default": true
    },
    "list-indent": {
      "description": "MD005/list-indent : Inconsistent indentation for list items at the same level : https://github.com/DavidAnson/markdownlint/blob/v0.40.0/doc/md005.md",
      "oneOf": [
        {
          "type": "boolean"
        },
        {
          "enum": [
            "error",
            "warning"
          ]
        },
        {
          "type": "object",
          "additionalProperties": false,
          "properties": {
            "enabled": {
              "description": "Whether to enable the rule",
              "type": "boolean",
              "default": true
            },
            "severity": {
              "description": "Rule severity",
              "type": "string",
              "enum": [
                "error",
                "warning"
              ],
              "default": "error"
            }
          }
        }
      ],
      "default": true
    },
    "MD007": {
      "description": "MD007/ul-indent : Unordered list indentation : https://github.com/DavidAnson/markdownlint/blob/v0.40.0/doc/md007.md",
      "oneOf": [
        {
          "type": "boolean"
        },
        {
          "enum": [
            "error",
            "warning"
          ]
        },
        {
          "type": "object",
          "additionalProperties": false,
          "properties": {
            "enabled": {
              "description": "Whether to enable the rule",
              "type": "boolean",
              "default": true
            },
            "severity": {
              "description": "Rule severity",
              "type": "string",
              "enum": [
                "error",
                "warning"
              ],
              "default": "error"
            },
            "indent": {
              "description": "Spaces for indent",
              "type": "integer",
              "minimum": 1,
              "default": 2
            },
            "start_indented": {
              "description": "Whether to indent the first level of the list",
              "type": "boolean",
              "default": false
            },
            "start_indent": {
              "description": "Spaces for first level indent (when start_indented is set)",
              "type": "integer",
              "minimum": 1,
              "default": 2
            }
          }
        }
      ],
      "default": true
    },
    "ul-indent": {
      "description": "MD007/ul-indent : Unordered list indentation : https://github.com/DavidAnson/markdownlint/blob/v0.40.0/doc/md007.md",
      "oneOf": [
        {
          "type": "boolean"
        },
        {
          "enum": [
            "error",
            "warning"
          ]
        },
        {
          "type": "object",
          "additionalProperties": false,
          "properties": {
            "enabled": {
              "description": "Whether to enable the rule",
              "type": "boolean",
              "default": true
            },
            "severity": {
              "description": "Rule severity",
              "type": "string",
              "enum": [
                "error",
                "warning"
              ],
              "default": "error"
            },
            "indent": {
              "description": "Spaces for indent",
              "type": "integer",
              "minimum": 1,
              "default": 2
            },
            "start_indented": {
              "description": "Whether to indent the first level of the list",
              "type": "boolean",
              "default": false
            },
            "start_indent": {
              "description": "Spaces for first level indent (when start_indented is set)",
              "type": "integer",
              "minimum": 1,
              "default": 2
            }
          }
        }
      ],
      "default": true
    },
    "MD009": {
      "description": "MD009/no-trailing-spaces : Trailing spaces : https://github.com/DavidAnson/markdownlint/blob/v0.40.0/doc/md009.md",
      "oneOf": [
        {
          "type": "boolean"
        },
        {
          "enum": [
            "error",
            "warning"
          ]
        },
        {
          "type": "object",
          "additionalProperties": false,
          "properties": {
            "enabled": {
              "description": "Whether to enable the rule",
              "type": "boolean",
              "default": true
            },
            "severity": {
              "description": "Rule severity",
              "type": "string",
              "enum": [
                "error",
                "warning"
              ],
              "default": "error"
            },
            "br_spaces": {
              "description": "Spaces for line break",
              "type": "integer",
              "minimum": 0,
              "default": 2
            },
            "code_blocks": {
              "description": "Include code blocks",
              "type": "boolean",
              "default": false
            },
            "list_item_empty_lines": {
              "description": "Allow spaces for empty lines in list items",
              "type": "boolean",
              "default": false
            },
            "strict": {
              "description": "Include unnecessary breaks",
              "type": "boolean",
              "default": false
            }
          }
        }
      ],
      "default": true
    },
    "no-trailing-spaces": {
      "description": "MD009/no-trailing-spaces : Trailing spaces : https://github.com/DavidAnson/markdownlint/blob/v0.40.0/doc/md009.md",
      "oneOf": [
        {
          "type": "boolean"
        },
        {
          "enum": [
            "error",
            "warning"
          ]
        },
        {
          "type": "object",
          "additionalProperties": false,
          "properties": {
            "enabled": {
            
... [TRUNCATED]
```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
