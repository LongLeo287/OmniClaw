---
id: yamafaktory-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:32:47.511412
---

# KNOWLEDGE EXTRACT: yamafaktory
> **Extracted on:** 2026-03-30 18:01:24
> **Source:** yamafaktory

---

## File: `jql.md`
```markdown
# 📦 yamafaktory/jql [🔖 PENDING/APPROVE]
🔗 https://github.com/yamafaktory/jql
🌐 https://crates.io/crates/jql

## Meta
- **Stars:** ⭐ 1663 | **Forks:** 🍴 31
- **Language:** Rust | **License:** Apache-2.0
- **Last updated:** 2026-03-24
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
A JSON Query Language CLI tool

## README (trích đầu)
```
![jql](jql.svg)

---

[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/yamafaktory/jql/ci.yml?branch=main&logo=github&style=flat-square)](https://github.com/yamafaktory/jql/actions/workflows/ci.yml)
[![Crates.io](https://img.shields.io/crates/v/jql?style=flat-square)](https://crates.io/crates/jql)
[![Docs.rs](https://img.shields.io/docsrs/jql-parser?label=jql-parser%20docs&style=flat-square)](https://docs.rs/jql-parser/latest/jql_parser/)
[![Docs.rs](https://img.shields.io/docsrs/jql-runner?label=jql-runner%20docs&style=flat-square)](https://docs.rs/jql-runner/latest/jql_runner/)

`jql` is a JSON Query Language tool built with Rust 🦀.

Pronounce it as **jackal** 🐺.

## 📜 Philosophy

- ⚡Be fast
- 🪶 Stay lightweight
- 🎮 Keep its features as simple as possible
- 🧠 Avoid redundancy
- 💡 Provide meaningful error messages
- 🍰 Eat JSON as input, process, output JSON back

## 🚀 Installation

### Alpine Linux

The package is maintained by @jirutka.

```sh
apk add jql
```

### Archlinux

The AUR package is maintained by @barklan.

```sh
yay -S jql
```

### Cargo

```sh
cargo install jql
```

### Cargo Binstall

```sh
cargo binstall jql
```

### Fedora

```sh
dnf install jql
```

### FreeBSD

```sh
pkg install jql
```

### Homebrew

```sh
brew install jql
```

### Nix

```sh
nix-env -i jql
```

### openSUSE

```sh
zypper install jql
```

### Manual installation from GitHub

Compiled binary versions are automatically uploaded to GitHub when a new release is made. You can install `jql` manually by [downloading a release](https://github.com/yamafaktory/jql/releases).

## 🛠️ Usage

To make a selection from a JSON input, `jql` expects a **query** as a sequence of **tokens**.

To be fully compliant with the JSON format, `jql` always expect key selectors to be **double-quoted**, see [The JavaScript Object Notation (JSON) Data Interchange Format](https://tools.ietf.org/html/rfc8259#section-13).

```json
{
  ".valid": 1337,
  "": "yeah!",
  "\"": "yup, valid too!"
}
```

Consequently, to be shell compliant, a query must be either enclosed by single quotation marks or every inner double quotation mark must be escaped.

### Separators

#### Group separator

Group separators build up an array from sub-queries.

**JSON input**

```json
{ "a": 1, "b": 2, "c": 3 }
```

**Query**

```sh
'"a","b","c"'
```

**JSON output**

```json
[1, 2, 3]
```

### Selectors

#### Arrays

##### Array index selector

Indexes can be used in arbitrary order.

**JSON input**

```json
[1, 2, 3]
```

**Query**

```sh
'[2,1]'
```

**JSON output**

```json
[3, 2]
```

##### Array range selector

Range can be in natural order `[0:2]`, reversed `[2:0]`, without lower `[:2]` or upper bound `[0:]`.

**JSON input**

```json
[1, 2, 3]
```

**Query**

```sh
'[2:1]'
```

**JSON output**

```json
[3, 2]
```

##### Lens selector

Lens can be a combination of one or more selectors with or an optional value, a value being any of **boolean** | **null** | **number** | **string**.

```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

