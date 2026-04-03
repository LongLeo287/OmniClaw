---
id: jaemk-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:55.804074
---

# KNOWLEDGE EXTRACT: jaemk
> **Extracted on:** 2026-03-30 17:38:11
> **Source:** jaemk

---

## File: `cached.md`
```markdown
# 📦 jaemk/cached [🔖 PENDING/APPROVE]
🔗 https://github.com/jaemk/cached


## Meta
- **Stars:** ⭐ 1974 | **Forks:** 🍴 109
- **Language:** Rust | **License:** MIT
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Rust cache structures and easy function memoization

## README (trích đầu)
```
# cached

[![Build Status](https://github.com/jaemk/cached/actions/workflows/build.yml/badge.svg)](https://github.com/jaemk/cached/actions/workflows/build.yml)
[![crates.io](https://img.shields.io/crates/v/cached.svg)](https://crates.io/crates/cached)
[![docs](https://docs.rs/cached/badge.svg)](https://docs.rs/cached)

> Caching structures and simplified function memoization

`cached` provides implementations of several caching structures as well as a handy macros
for defining memoized functions.

Memoized functions defined using [`#[cached]`](proc_macro::cached)/[`#[once]`](proc_macro::once)/[`#[io_cached]`](proc_macro::io_cached)/[`cached!`](crate::macros) macros are thread-safe with the backing
function-cache wrapped in a mutex/rwlock, or externally synchronized in the case of `#[io_cached]`.
By default, the function-cache is **not** locked for the duration of the function's execution, so initial (on an empty cache)
concurrent calls of long-running functions with the same arguments will each execute fully and each overwrite
the memoized value as they complete. This mirrors the behavior of Python's `functools.lru_cache`. To synchronize the execution and caching
of un-cached arguments, specify `#[cached(sync_writes = "default")]` / `#[once(sync_writes = true)]` (not supported by `#[io_cached]`.

- See [`cached::stores` docs](https://docs.rs/cached/latest/cached/stores/index.html) cache stores available.
- See [`proc_macro`](https://docs.rs/cached/latest/cached/proc_macro/index.html) for more procedural macro examples.
- See [`macros`](https://docs.rs/cached/latest/cached/macros/index.html) for more declarative macro examples.

**Features**

- `default`: Include `proc_macro`, `ahash`, and `time_stores` features
- `proc_macro`: Include proc macros
- `ahash`: Enable the optional `ahash` hasher as default hashing algorithm.
- `async`: Include support for async functions and async cache stores
- `async_tokio_rt_multi_thread`: Enable `tokio`'s optional `rt-multi-thread` feature.
- `redis_store`: Include Redis cache store
- `redis_smol`: Include async Redis support using `smol` and `smol` tls support, implies `redis_store` and `async`
- `redis_tokio`: Include async Redis support using `tokio` and `tokio` tls support, implies `redis_store` and `async`
- `redis_connection_manager`: Enable the optional `connection-manager` feature of `redis`. Any async redis caches created
                              will use a connection manager instead of a `MultiplexedConnection`
- `redis_ahash`: Enable the optional `ahash` feature of `redis`
- `disk_store`: Include disk cache store
- `wasm`: Enable WASM support. Note that this feature is incompatible with `tokio`'s multi-thread
   runtime (`async_tokio_rt_multi_thread`) and all Redis features (`redis_store`, `redis_smol`, `redis_tokio`, `redis_ahash`)
- `time_stores`: Include time-based cache stores ([`TimedCache`], [`TimedSizedCache`], and [`stores::ExpiringSizedCache`]).
   Disable this feature when targeting envi
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

