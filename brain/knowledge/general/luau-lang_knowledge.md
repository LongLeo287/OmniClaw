---
id: luau-lang-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:29:06.186049
---

# KNOWLEDGE EXTRACT: luau-lang
> **Extracted on:** 2026-03-30 17:42:03
> **Source:** luau-lang

---

## File: `luau.md`
```markdown
# 📦 luau-lang/luau [🔖 PENDING/APPROVE]
🔗 https://github.com/luau-lang/luau
🌐 https://luau.org

## Meta
- **Stars:** ⭐ 5380 | **Forks:** 🍴 546
- **Language:** C++ | **License:** MIT
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
A small, fast, and embeddable programming language based on Lua with a gradual type system.

## README (trích đầu)
```
Luau ![CI](https://github.com/luau-lang/luau/actions/workflows/build.yml/badge.svg) [![codecov](https://codecov.io/gh/luau-lang/luau/branch/master/graph/badge.svg)](https://codecov.io/gh/luau-lang/luau)
====

Luau (lowercase u, /ˈlu.aʊ/) is a fast, small, safe, gradually typed embeddable scripting language derived from [Lua](https://lua.org).

It is designed to be backwards compatible with Lua 5.1, as well as incorporating [some features](https://luau.org/compatibility) from future Lua releases, but also expands the feature set (most notably with type annotations and a state-of-the-art type inference system). Luau is largely implemented from scratch, with the language runtime being a very heavily modified version of Lua 5.1 runtime, with completely rewritten interpreter and other [performance innovations](https://luau.org/performance). The runtime mostly preserves Lua 5.1 API, so existing bindings should be more or less compatible with a few caveats.

Luau is used by Roblox game developers to write game code, and by Roblox engineers to implement large parts of the user-facing application code as well as portions of the editor (Roblox Studio) as plugins. Roblox chose to open-source Luau to foster collaboration within the Roblox community as well as to allow other companies and communities to benefit from the ongoing language and runtime innovation. More recently, Luau has seen adoption in games like Alan Wake 2, Farming Simulator 2025, Second Life, and Warframe.

This repository hosts source code for the language implementation and associated tooling. Documentation for the language is available at https://luau.org/ and accepts contributions via [site repository](https://github.com/luau-lang/site); the language is evolved through RFCs that are located in [rfcs repository](https://github.com/luau-lang/rfcs).

# Usage

Luau is an embeddable programming language, but it also comes with two command-line tools by default, `luau` and `luau-analyze`.

`luau` is a command-line REPL and can also run input files. Note that REPL runs in a sandboxed environment and as such doesn't have access to the underlying file system except for ability to `require` modules.

`luau-analyze` is a command-line type checker and linter; given a set of input files, it produces errors/warnings according to the file configuration, which can be customized by using `--!` comments in the files or [`.luaurc`](https://rfcs.luau.org/config-luaurc) files. For details, please refer to our [type checking](https://luau.org/typecheck) and [linting](https://luau.org/lint) documentation. Our community maintains a language server frontend for `luau-analyze` called [luau-lsp](https://github.com/JohnnyMorganz/luau-lsp) for use with text editors.

# Installation

You can install and run Luau by downloading the compiled binaries from [a recent release](https://github.com/luau-lang/luau/releases); note that `luau` and `luau-analyze` binaries from the archives will need to be added to PATH or copied
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

