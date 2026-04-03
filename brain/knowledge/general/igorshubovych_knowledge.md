---
id: igorshubovych-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:53.070541
---

# KNOWLEDGE EXTRACT: igorshubovych
> **Extracted on:** 2026-03-30 17:38:09
> **Source:** igorshubovych

---

## File: `markdownlint-cli.md`
```markdown
# 📦 igorshubovych/markdownlint-cli [🔖 PENDING/APPROVE]
🔗 https://github.com/igorshubovych/markdownlint-cli


## Meta
- **Stars:** ⭐ 1033 | **Forks:** 🍴 101
- **Language:** JavaScript | **License:** MIT
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
MarkdownLint Command Line Interface

## README (trích đầu)
```
# markdownlint-cli

[![GitHub Actions Build Status][actions-badge]][actions-url]

> Command Line Interface for [MarkdownLint][markdownlint]

## Installation

```bash
npm install -g markdownlint-cli
```

On macOS you can install via [Homebrew](https://brew.sh/):

```bash
brew install markdownlint-cli
```

## Usage

```bash
markdownlint --help

Usage: markdownlint [options] [files|directories|globs...]

MarkdownLint Command Line Interface

Arguments:
  files|directories|globs                    files, directories, and/or globs to lint

Options:
  -V, --version                              output the version number
  -c, --config <configFile>                  configuration file (JSON, JSONC, JS, YAML, or TOML)
  --configPointer <pointer>                  JSON Pointer to object within configuration file (default: "")
  -d, --dot                                  include files/folders with a dot (for example `.github`)
  -f, --fix                                  fix basic issues (does not work with STDIN)
  -i, --ignore <file|directory|glob>         file(s) to ignore/exclude (default: [])
  -j, --json                                 write issues in json format
  -o, --output <outputFile>                  write issues to file (no console)
  -p, --ignore-path <file>                   path to file with ignore pattern(s)
  -q, --quiet                                do not write issues to STDOUT
  -r, --rules <file|directory|glob|package>  include custom rule files (default: [])
  -s, --stdin                                read from STDIN (does not work with files)
  --enable <rules...>                        Enable certain rules, e.g. --enable MD013 MD041 --
  --disable <rules...>                       Disable certain rules, e.g. --disable MD013 MD041 --
  -h, --help                                 display help for command
```

Or run using [Docker](https://www.docker.com) and [GitHub Packages](https://github.com/features/packages):

```bash
docker run -v $PWD:/workdir ghcr.io/igorshubovych/markdownlint-cli:latest "*.md"
```

> **Note**
> Because `--enable` and `--disable` are [variadic arguments that accept multiple values][commander-variadic], it is necessary to end the list by passing `--` before the `<files|directories|globs>` argument like so: `markdownlint --disable MD013 -- README.md`.

### Globbing

`markdownlint-cli` supports advanced globbing patterns like `**/*.md` ([more information][globprimer]).
With shells like Bash, it may be necessary to quote globs so they are not interpreted by the shell.
For example, `--ignore *.md` would be expanded by Bash to `--ignore a.md b.md ...` before invoking `markdownlint-cli`, causing it to ignore only the first file because `--ignore` takes a single parameter (though it can be used multiple times).
Quoting the glob like `--ignore '*.md'` passes it through unexpanded and ignores the set of files.

#### Globbing examples

To lint all Markdown files in a Node.js project (excluding dependencies), the following 
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

