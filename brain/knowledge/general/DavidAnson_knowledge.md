---
id: davidanson-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:16.698629
---

# KNOWLEDGE EXTRACT: DavidAnson
> **Extracted on:** 2026-03-30 17:35:45
> **Source:** DavidAnson

---

## File: `markdownlint-cli2.md`
```markdown
# 📦 DavidAnson/markdownlint-cli2 [🔖 PENDING/APPROVE]
🔗 https://github.com/DavidAnson/markdownlint-cli2


## Meta
- **Stars:** ⭐ 737 | **Forks:** 🍴 68
- **Language:** JavaScript | **License:** MIT
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
A fast, flexible, configuration-based command-line interface for linting Markdown/CommonMark files with the markdownlint library

## README (trích đầu)
```
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
- --fix           updates files to resolve 
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

