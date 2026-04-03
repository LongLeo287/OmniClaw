---
id: mlua-rs-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:29:08.891323
---

# KNOWLEDGE EXTRACT: mlua-rs
> **Extracted on:** 2026-03-30 17:42:53
> **Source:** mlua-rs

---

## File: `mlua.md`
```markdown
# 📦 mlua-rs/mlua [🔖 PENDING/APPROVE]
🔗 https://github.com/mlua-rs/mlua


## Meta
- **Stars:** ⭐ 2643 | **Forks:** 🍴 197
- **Language:** Rust | **License:** NOASSERTION
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
High level Lua 5.5/5.4/5.3/5.2/5.1 (including LuaJIT) and Luau bindings to Rust with async/await support

## README (trích đầu)
```
# mlua
[![Build Status]][github-actions] [![Latest Version]][crates.io] [![API Documentation]][docs.rs] [![Coverage Status]][codecov.io] ![MSRV]

[Build Status]: https://github.com/mlua-rs/mlua/workflows/CI/badge.svg
[github-actions]: https://github.com/mlua-rs/mlua/actions
[Latest Version]: https://img.shields.io/crates/v/mlua.svg
[crates.io]: https://crates.io/crates/mlua
[API Documentation]: https://docs.rs/mlua/badge.svg
[docs.rs]: https://docs.rs/mlua
[Coverage Status]: https://codecov.io/gh/mlua-rs/mlua/branch/main/graph/badge.svg?token=99339FS1CG
[codecov.io]: https://codecov.io/gh/mlua-rs/mlua
[MSRV]: https://img.shields.io/badge/rust-1.79+-brightgreen.svg?&logo=rust

[Guided Tour] | [Benchmarks] | [FAQ]

[Guided Tour]: examples/guided_tour.rs
[Benchmarks]: https://github.com/khvzak/script-bench-rs
[FAQ]: FAQ.md

## The main branch is the development version of `mlua`. Please see the [v0.11](https://github.com/mlua-rs/mlua/tree/v0.11) branch for the stable versions of `mlua`.

`mlua` is a set of bindings to the [Lua](https://www.lua.org) programming language for Rust with a goal of providing a
_safe_ (as much as possible), high level, easy to use, practical and flexible API.

Started as an `rlua` fork, `mlua` supports Lua 5.5, 5.4, 5.3, 5.2, 5.1 (including LuaJIT) and [Luau] and allows writing native Lua modules in Rust as well as using Lua in a standalone mode.

`mlua` is tested on Windows/macOS/Linux including module mode in [GitHub Actions] on `x86_64` platforms and cross-compilation to `aarch64` (other targets are also supported).

WebAssembly (WASM) is supported through the `wasm32-unknown-emscripten` target for all Lua/Luau versions excluding JIT.

[GitHub Actions]: https://github.com/mlua-rs/mlua/actions
[Luau]: https://luau.org

## Usage

### Feature flags

`mlua` uses feature flags to reduce the number of dependencies and compiled code, and allow choosing only the required set of features.
Below is a list of the available feature flags. By default `mlua` does not enable any features.

* `lua55`: enable Lua [5.5] support
* `lua54`: enable Lua [5.4] support
* `lua53`: enable Lua [5.3] support
* `lua52`: enable Lua [5.2] support
* `lua51`: enable Lua [5.1] support
* `luajit`: enable [LuaJIT] support
* `luajit52`: enable [LuaJIT] support with partial compatibility with Lua 5.2
* `luau`: enable [Luau] support (auto vendored mode)
* `luau-jit`: enable [Luau] support with JIT backend.
* `luau-vector4`: enable [Luau] support with 4-dimensional vector.
* `vendored`: build static Lua(JIT) libraries from sources during `mlua` compilation using [lua-src] or [luajit-src]
* `module`: enable module mode (building loadable `cdylib` library for Lua)
* `async`: enable async/await support (any executor can be used, eg. [tokio] or [async-std])
* `send`: make `mlua::Lua: Send + Sync` (adds [`Send`] requirement to `mlua::Function` and `mlua::UserData`)
* `error-send`: make `mlua:Error: Send + Sync`
* `serde`: add serialization and deserialization supp
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

