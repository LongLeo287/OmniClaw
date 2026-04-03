---
id: tomwright-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:31:22.580304
---

# KNOWLEDGE EXTRACT: TomWright
> **Extracted on:** 2026-03-30 17:54:19
> **Source:** TomWright

---

## File: `dasel.md`
```markdown
# 📦 TomWright/dasel [🔖 PENDING/APPROVE]
🔗 https://github.com/TomWright/dasel
🌐 https://daseldocs.tomwright.me

## Meta
- **Stars:** ⭐ 7887 | **Forks:** 🍴 164
- **Language:** Go | **License:** MIT
- **Last updated:** 2026-03-24
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Select, put and delete data from JSON, TOML, YAML, XML, INI, HCL and CSV files with a single tool. Also available as a go mod.

## README (trích đầu)
```
[![Gitbook](https://badges.aleen42.com/src/gitbook_1.svg)](https://daseldocs.tomwright.me)
[![Go Report Card](https://goreportcard.com/badge/github.com/tomwright/dasel/v3)](https://goreportcard.com/report/github.com/tomwright/dasel/v3)
[![PkgGoDev](https://pkg.go.dev/badge/github.com/tomwright/dasel)](https://pkg.go.dev/github.com/tomwright/dasel/v3)
![Test](https://github.com/TomWright/dasel/workflows/Test/badge.svg)
![Build](https://github.com/TomWright/dasel/workflows/Build/badge.svg)
[![codecov](https://codecov.io/gh/TomWright/dasel/branch/master/graph/badge.svg)](https://codecov.io/gh/TomWright/dasel)
[![Mentioned in Awesome Go](https://awesome.re/mentioned-badge.svg)](https://github.com/avelino/awesome-go)
![GitHub Downloads](https://img.shields.io/github/downloads/TomWright/dasel/total)
![Homebrew Formula Downloads](https://img.shields.io/homebrew/installs/dy/dasel?label=brew%20installs)
![GitHub License](https://img.shields.io/github/license/TomWright/dasel)
[![GitHub tag (latest by date)](https://img.shields.io/github/v/tag/TomWright/dasel?label=latest%20release)](https://github.com/TomWright/dasel/releases/latest)
[![Homebrew tag (latest by date)](https://img.shields.io/homebrew/v/dasel)](https://formulae.brew.sh/formula/dasel)

<div align="center">
    <img src="./daselgopher.png" alt="Dasel mascot" width="250"/>
</div>

# Dasel

Dasel (short for **Data-Select**) is a command-line tool and library for querying, modifying, and transforming data structures such as JSON, YAML, TOML, XML, and CSV.

It provides a consistent, powerful syntax to traverse and update data — making it useful for developers, DevOps, and data wrangling tasks.

---

## Features

* **Multi-format support**: JSON, YAML, TOML, XML, CSV, HCL, INI.
* **Unified query syntax**: Access data in any format with the same selectors.
* **Query & search**: Extract values, lists, or structures with intuitive syntax.
* **Modify in place**: Update, insert, or delete values directly in structured files.
* **Convert between formats**: Seamlessly transform data from JSON → YAML, TOML → JSON, etc.
* **Script-friendly**: Simple CLI integration for shell scripts and pipelines.
* **Library support**: Import and use in Go projects.

---

## Installation

### Homebrew (macOS/Linux)

```sh
brew install dasel
```

### Go Install

```sh
go install github.com/tomwright/dasel/v3/cmd/dasel@master
```

### Prebuilt Binaries

Prebuilt binaries are available on the [Releases](https://github.com/TomWright/dasel/releases) page for Linux, macOS, and Windows.

### None of the above?

See the [installation docs](https://daseldocs.tomwright.me/getting-started/installation) for more options.

---

## Basic Usage

### Selecting Values

By default, Dasel evaluates the final selector and prints the result.

```sh
echo '{"foo": {"bar": "baz"}}' | dasel -i json 'foo.bar'
# Output: "baz"
```

### Modifying Values

Update values inline:

```sh
echo '{"foo": {"bar": "baz"}}' | dasel -i json 'foo.bar = "bong"'
# Ou
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

