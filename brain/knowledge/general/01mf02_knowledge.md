---
id: 01mf02-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:18:37.663803
---

# KNOWLEDGE EXTRACT: 01mf02
> **Extracted on:** 2026-03-30 17:28:59
> **Source:** 01mf02

---

## File: `jaq.md`
```markdown
# 📦 01mf02/jaq [🔖 PENDING/APPROVE]
🔗 https://github.com/01mf02/jaq


## Meta
- **Stars:** ⭐ 3446 | **Forks:** 🍴 106
- **Language:** Rust | **License:** MIT
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
A jq clone focussed on correctness, speed, and simplicity

## README (trích đầu)
```
# jaq

![Build status](https://github.com/01mf02/jaq/actions/workflows/check.yml/badge.svg)
[![Crates.io](https://img.shields.io/crates/v/jaq-core.svg)](https://crates.io/crates/jaq-core)
[![Documentation](https://docs.rs/jaq-core/badge.svg)](https://docs.rs/jaq-core)
[![Rust 1.69+](https://img.shields.io/badge/rust-1.69+-orange.svg)](https://www.rust-lang.org)

jaq (pronounced /ʒaːk/, like *Jacques*[^jacques]) is a clone of
the JSON data processing tool [`jq`](https://jqlang.github.io/jq/).
It has a few features not present in `jq`, such as
support for the data formats YAML, CBOR, TOML, and XML.
jaq has an own [manual](https://gedenkt.at/jaq/manual/).
You can try jaq on the [playground](https://gedenkt.at/jaq/).

jaq is two things at a time:

- A command-line program, `jaq`, that can be used as drop-in replacement for `jq`.
- A library, [`jaq-core`](https://docs.rs/jaq-core/),
  that can be used to compile and run jq programs inside of Rust programs.
  Compared to the `jq` API, `jaq-core`
  can be safely used in multi-threaded environments and
  supports [arbitrary data types beyond JSON](https://docs.rs/jaq-core/latest/jaq_core/val/trait.ValT.html).

jaq focuses on three goals:

* **Correctness**:
  jaq aims to provide a more correct and predictable implementation of jq,
  while preserving compatibility with jq in most cases.
* **Performance**:
  I created jaq originally because I was bothered by
  [the long start-up time of jq 1.6](https://github.com/jqlang/jq/issues/1411),
  which amounts to about 50ms on my machine.
  This can be particularly seen when processing a large number of small files.
  Although the startup time has been vastly improved in jq 1.7,
  jaq is still faster than jq on many other [benchmarks](#performance).
* **Simplicity**:
  jaq aims to have a simple and small implementation, in order to
  reduce the potential for bugs and to
  facilitate contributions.

[^jacques]: I wanted to create a tool that should be discreet and obliging, like a good waiter.
  And when I think of a typical name for a (French) waiter, to my mind comes "Jacques".
  Later, I found out about the old French word *jacquet*, meaning "squirrel",
  which makes for a nice *ex post* inspiration for the name.
  And finally, the
  [Jacquard machine](https://en.wikipedia.org/wiki/Jacquard_machine)
  was an important predecessor of the modern computer,
  automating weaving with punched cards as early as 1804.



# Installation


## Binaries

You can download binaries for Linux, Mac, and Windows on the [releases page](https://github.com/01mf02/jaq/releases).
On a Linux system, you can download it using the following commands:

    $ curl -fsSL https://github.com/01mf02/jaq/releases/latest/download/jaq-$(uname -m)-unknown-linux-musl -o jaq && chmod +x jaq

You may also install jaq using [homebrew](https://formulae.brew.sh/formula/jaq) on macOS or Linux:

    $ brew install jaq
    $ brew install --HEAD jaq # latest development version

[![Packaging status](https:
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

