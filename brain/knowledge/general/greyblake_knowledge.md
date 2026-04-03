---
id: greyblake-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:49.498701
---

# KNOWLEDGE EXTRACT: greyblake
> **Extracted on:** 2026-03-30 17:38:02
> **Source:** greyblake

---

## File: `whatlang-rs.md`
```markdown
# 📦 greyblake/whatlang-rs [🔖 PENDING/APPROVE]
🔗 https://github.com/greyblake/whatlang-rs
🌐 https://whatlang.org/

## Meta
- **Stars:** ⭐ 1063 | **Forks:** 🍴 120
- **Language:** Rust | **License:** MIT
- **Last updated:** 2026-03-21
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Natural language detection library for Rust. Try demo online: https://whatlang.org/

## README (trích đầu)
```
<p align="center"><img width="160" src="https://raw.githubusercontent.com/greyblake/whatlang-rs/master/misc/logo/whatlang-logo.svg" alt="Whatlang - rust library for natural language detection"></p>

<h1 align="center">Whatlang</h1>

<p align="center">Natural language detection for Rust with focus on simplicity and performance.</p>
<p align="center"><a href="https://whatlang.org/" target="_blank">Try online demo.</a></p>

<p align="center">
<a href="https://github.com/greyblake/whatlang-rs/actions/workflows/ci.yml" rel="nofollow"><img src="https://github.com/greyblake/whatlang-rs/actions/workflows/ci.yml/badge.svg" alt="Build Status"></a>
<a href="https://raw.githubusercontent.com/greyblake/whatlang-rs/master/LICENSE" rel="nofollow"><img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="License"></a>
<a href="https://docs.rs/whatlang" rel="nofollow"><img src="https://docs.rs/whatlang/badge.svg" alt="Documentation"></a>
<p>

[![Stand With Ukraine](https://raw.githubusercontent.com/vshymanskyy/StandWithUkraine/main/banner2-direct.svg)](https://stand-with-ukraine.pp.ua/)

## Content
* [Features](#features)
* [Get started](#get-started)
* [Who uses Whatlang?](#who-uses-whatlang)
* [Documentation](https://docs.rs/whatlang)
* [Supported languages](https://github.com/greyblake/whatlang-rs/blob/master/SUPPORTED_LANGUAGES.md)
* [Feature toggles](#feature-toggles)
* [How does it work?](#how-does-it-work)
* [Make tasks](#make-tasks)
* [Comparison with alternatives](#comparison-with-alternatives)
* [Ports and clones](#ports-and-clones)
* [Donations](#donations)
* [Derivation](#derivation)
* [License](#license)
* [Contributors](#contributors)


## Features
* Supports [70 languages](https://github.com/greyblake/whatlang-rs/blob/master/SUPPORTED_LANGUAGES.md)
* 100% written in Rust
* Lightweight, fast and simple
* Recognizes not only a language, but also a script (Latin, Cyrillic, etc)
* Provides reliability information

## Get started

Example:

```rust
use whatlang::{detect, Lang, Script};

fn main() {
    let text = "Ĉu vi ne volas eklerni Esperanton? Bonvolu! Estas unu de la plej bonaj aferoj!";

    let info = detect(text).unwrap();
    assert_eq!(info.lang(), Lang::Epo);
    assert_eq!(info.script(), Script::Latin);
    assert_eq!(info.confidence(), 1.0);
    assert!(info.is_reliable());
}
```

For more details (e.g. how to blacklist some languages) please check the [documentation](https://docs.rs/whatlang).

## Who uses Whatlang?

Whatlang is used within the following big projects as direct or indirect dependency for language recognition.
You're gonna be in a great company using Whatlang:

* [Sonic](https://github.com/valeriansaliou/sonic) - fast, lightweight and schema-less search backend in Rust.
* [Meilisearch](https://github.com/meilisearch) - an open-source, easy-to-use, blazingly fast, and hyper-relevant search engine built in Rust.

## Feature toggles

| Feature     | Description                                                           
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

