---
id: mpalmer-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:29:09.815921
---

# KNOWLEDGE EXTRACT: mpalmer
> **Extracted on:** 2026-03-30 17:43:02
> **Source:** mpalmer

---

## File: `action-validator.md`
```markdown
# 📦 mpalmer/action-validator [🔖 PENDING/APPROVE]
🔗 https://github.com/mpalmer/action-validator


## Meta
- **Stars:** ⭐ 367 | **Forks:** 🍴 33
- **Language:** Rust | **License:** GPL-3.0
- **Last updated:** 2026-03-24
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Tool to validate GitHub Action and Workflow YAML files

## README (trích đầu)
```
The `action-validator` is a standalone tool designed to "lint" the YAML files
used to define GitHub Actions and Workflows. It ensures that they are well-formed,
by checking them against published JSON schemas, and it makes sure that any
globs used in `paths` / `paths-ignore` match at least one file in the repo.

The intended use case for `action-validator` is in Git pre-commit hooks and
similar situations.


# Funding Development

I am currently experimenting with ways to fund development of new features in `action-validator`.
You can find more details of this approach at [the `action-validator` code fund page](https://hezmatt.org/~mpalmer/code-fund.html).


# Installation

We have many ways to install `action-validator`.

## Pre-built binaries

The [GitHub releases](https://github.com/mpalmer/action-validator/releases)
have some pre-built binaries -- just download and put them in your path. If a
binary for your platform isn't available, let me know and I'll see what I can
figure out.


## Using cargo

If you've got a Rust toolchain installed, running `cargo install action-validator` should give you the latest release.


## Using asdf

If you're a proponent of the [asdf tool](https://asdf-vm.com/), then you can
use that to install and manage `action-validator`:

```shell
asdf plugin add action-validator
# or
asdf plugin add action-validator https://github.com/mpalmer/action-validator.git
```

Install/configure action-validator:

```shell
# Show all installable versions
asdf list-all action-validator

# Install specific version
asdf install action-validator latest

# Set a version globally (on your ~/.tool-versions file)
asdf set -u action-validator latest

# Now action-validator commands are available
action-validator --help
```


# Using mise

If you are a passionate user of [mise](https://github.com/jdx/mise), then you can use that to install and manage `action-validator`:

No need to declare the plugin, it's already known by mise.

Install/configure action-validator:

```shell
# Show all installable versions
mise ls-remote action-validator

# Install specific version
mise install action-validator@latest

# Set a version globally (on your ~/.tool-versions or .mise.toml file)
mise use -g action-validator@latest

# Now action-validator commands are available
action-validator --help
```


## Using NPM

Node users can install the latest version using NPM:

> ℹ️ The `@action-validator/core` package can be used directly within Node.js applications.

```sh
npm install -g @action-validator/core @action-validator/cli --save-dev
```

## Building from the repo

If you want to build locally, you'll need to:

1. Checkout the git repository somewhere;

1. Grab the `SchemaStore` submodule, by running `git submodule init && git submodule update`;

1. Install a [Rust](https://rust-lang.org) toolchain; and then

1. run `cargo build`.


# Usage

Couldn't be simpler: just pass a file to the program:

```shell
action-validator .github/workflows/build.yml
```

Use `
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

