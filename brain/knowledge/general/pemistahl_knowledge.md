---
id: pemistahl-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:29:20.271398
---

# KNOWLEDGE EXTRACT: pemistahl
> **Extracted on:** 2026-03-30 17:50:58
> **Source:** pemistahl

---

## File: `grex-js.md`
```markdown
# 📦 pemistahl/grex-js [🔖 PENDING/APPROVE]
🔗 https://github.com/pemistahl/grex-js
🌐 https://pemistahl.github.io/grex-js/

## Meta
- **Stars:** ⭐ 183 | **Forks:** 🍴 2
- **Language:** JavaScript | **License:** Apache-2.0
- **Last updated:** 2026-01-10
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
A JavaScript / WebAssembly library for generating regular expressions from user-provided test cases

## README (trích đầu)
```
<div align="center">

  ![grex](logo.png)

  <br>

  [![build](https://github.com/pemistahl/grex-js/actions/workflows/build.yml/badge.svg)](https://github.com/pemistahl/grex-js/actions/workflows/build.yml)
  [![docs](https://doxdox.org/images/badge-flat.svg)](https://doxdox.org/pemistahl/grex-js/master)
  [![npm](https://img.shields.io/badge/npm-1.0.2-red?logo=npm)](https://www.npmjs.com/package/@pemistahl/grex)
  [![demo](https://img.shields.io/badge/-Demo%20Website-orange?logo=HTML5&labelColor=white)](https://pemistahl.github.io/grex-js/)
  [![wasm](https://img.shields.io/badge/-WebAssembly-blueviolet?logo=WebAssembly&labelColor=white)](https://webassembly.org/)
  [![license](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://www.apache.org/licenses/LICENSE-2.0)
</div>

<br>

## 1. What does this library do?

*grex* is a library that is meant to simplify the often complicated and tedious 
task of creating regular expressions. It does so by automatically generating a 
single regular expression from user-provided test cases. The resulting
expression is guaranteed to match the test cases which it was generated from.

This project has started as a [Rust port](https://github.com/pemistahl/grex) of 
the JavaScript tool [*regexgen*](https://github.com/devongovett/regexgen) 
written by [Devon Govett](https://github.com/devongovett). Although a lot of 
further useful features could be added to it, its development was apparently 
ceased several years ago. The Rust library offers new features and extended 
Unicode support. By compiling it to [WebAssembly](https://webassembly.org) (WASM), 
these improvements are now back in the browser and in [Node.js](https://nodejs.org/en/about).
This repository here contains only the compiled WASM modules and the generated
JavaScript bindings. They have been created from the Rust source code with the help
of [`wasm-pack`](https://github.com/pemistahl/grex#7-webassembly-support).

The philosophy of this project is to generate the most specific regular expression
possible by default which exactly matches the given input only and nothing else.
With the use of preprocessing methods, more generalized expressions can be created.

The produced expressions are [Perl-compatible regular expressions](https://www.pcre.org).
They are mostly compatible with JavaScript's 
[`RegExp`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp)
implementation but not all PCRE features are supported. An alternative is the [`XRegExp`](https://xregexp.com)
library which virtually supports the entire PCRE feature set. Other regular expression parsers or 
respective libraries from other programming languages have not been tested so far, 
but they ought to be mostly compatible as well.

There is a [demo website](https://pemistahl.github.io/grex-js/) available where you can give grex a try.

![demo website](https://raw.githubusercontent.com/pemistahl/grex-js/main/website.jpg)

## 2. Do I still need
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `grex.md`
```markdown
# 📦 pemistahl/grex [🔖 PENDING/APPROVE]
🔗 https://github.com/pemistahl/grex
🌐 https://pemistahl.github.io/grex-js/

## Meta
- **Stars:** ⭐ 8072 | **Forks:** 🍴 187
- **Language:** Rust | **License:** Apache-2.0
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
A command-line tool and Rust library with Python bindings for generating regular expressions from user-provided test cases

## README (trích đầu)
```
<div align="center">

  ![grex](https://raw.githubusercontent.com/pemistahl/grex/main/logo.png)

  <br>

  [![rust build status](https://github.com/pemistahl/grex/actions/workflows/rust-build.yml/badge.svg)](https://github.com/pemistahl/grex/actions/workflows/rust-build.yml)
  [![python build status](https://github.com/pemistahl/grex/actions/workflows/python-build.yml/badge.svg)](https://github.com/pemistahl/grex/actions/workflows/python-build.yml)
  [![docs.rs](https://docs.rs/grex/badge.svg)](https://docs.rs/grex)
  [![codecov](https://codecov.io/gh/pemistahl/grex/branch/main/graph/badge.svg)](https://codecov.io/gh/pemistahl/grex)
  [![dependency status](https://deps.rs/crate/grex/1.4.6/status.svg)](https://deps.rs/crate/grex/1.4.6)
  [![demo](https://img.shields.io/badge/-Demo%20Website-orange?logo=HTML5&labelColor=white)](https://pemistahl.github.io/grex-js/)
  
  [![downloads](https://img.shields.io/crates/d/grex.svg)](https://crates.io/crates/grex)
  [![crates.io](https://img.shields.io/crates/v/grex.svg)](https://crates.io/crates/grex)
  [![lib.rs](https://img.shields.io/badge/lib.rs-v1.4.6-blue)](https://lib.rs/crates/grex)
  ![supported Python versions](https://img.shields.io/badge/Python-%3E%3D%203.12-blue?logo=Python&logoColor=yellow)
  [![pypi](https://img.shields.io/badge/PYPI-v1.0.2-blue?logo=PyPI&logoColor=yellow)](https://pypi.org/project/grex)
  [![license](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://www.apache.org/licenses/LICENSE-2.0)

  [![Linux 64-bit Download](https://img.shields.io/badge/Linux%2064bit%20Download-v1.4.6-blue?logo=Linux)](https://github.com/pemistahl/grex/releases/download/v1.4.6/grex-v1.4.6-x86_64-unknown-linux-musl.tar.gz)
  [![Linux ARM64 Download](https://img.shields.io/badge/Linux%20ARM64%20Download-v1.4.6-blue?logo=Linux)](https://github.com/pemistahl/grex/releases/download/v1.4.6/grex-v1.4.6-aarch64-unknown-linux-musl.tar.gz)  
  
  [![MacOS 64-bit Download](https://img.shields.io/badge/macOS%2064bit%20Download-v1.4.6-blue?logo=Apple)](https://github.com/pemistahl/grex/releases/download/v1.4.6/grex-v1.4.6-x86_64-apple-darwin.tar.gz)
  [![MacOS ARM64 Download](https://img.shields.io/badge/macOS%20ARM64%20Download-v1.4.6-blue?logo=Apple)](https://github.com/pemistahl/grex/releases/download/v1.4.6/grex-v1.4.6-aarch64-apple-darwin.tar.gz)
  
  [![Windows 64-bit Download](https://img.shields.io/badge/Windows%2064bit%20Download-v1.4.6-blue?logo=Windows)](https://github.com/pemistahl/grex/releases/download/v1.4.6/grex-v1.4.6-x86_64-pc-windows-msvc.zip)
  [![Windows ARM64 Download](https://img.shields.io/badge/Windows%20ARM64%20Download-v1.4.6-blue?logo=Windows)](https://github.com/pemistahl/grex/releases/download/v1.4.6/grex-v1.4.6-aarch64-pc-windows-msvc.zip)
</div>

<br>

![grex demo](https://raw.githubusercontent.com/pemistahl/grex/main/demo.gif)

<br>

## 1. What does this tool do?

*grex* is a library as well as a command-line utility that is meant to simplify the often 
complica
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

