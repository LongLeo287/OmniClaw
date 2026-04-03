---
id: rusticstuff-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:31:10.555903
---

# KNOWLEDGE EXTRACT: rusticstuff
> **Extracted on:** 2026-03-30 17:53:02
> **Source:** rusticstuff

---

## File: `simdutf8.md`
```markdown
# 📦 rusticstuff/simdutf8 [🔖 PENDING/APPROVE]
🔗 https://github.com/rusticstuff/simdutf8


## Meta
- **Stars:** ⭐ 591 | **Forks:** 🍴 31
- **Language:** Rust | **License:** NOASSERTION
- **Last updated:** 2026-03-20
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
SIMD-accelerated UTF-8 validation for Rust.

## README (trích đầu)
```
[![CI](https://github.com/rusticstuff/simdutf8/actions/workflows/ci.yml/badge.svg)](https://github.com/rusticstuff/simdutf8/actions/workflows/ci.yml)
[![crates.io](https://img.shields.io/crates/v/simdutf8.svg)](https://crates.io/crates/simdutf8)
[![docs.rs](https://docs.rs/simdutf8/badge.svg)](https://docs.rs/simdutf8)

# simdutf8 – High-speed UTF-8 validation

Blazingly fast API-compatible UTF-8 validation for Rust using SIMD extensions, based on the implementation from
[simdjson](https://github.com/simdjson/simdjson). Originally ported to Rust by the developers of [simd-json.rs](https://simd-json.rs), but now heavily improved.

## Status
This library has been thoroughly tested with sample data as well as fuzzing and there are no known bugs.

## Features
* `basic` API for the fastest validation, optimized for valid UTF-8
* `compat` API as a fully compatible replacement for `std::str::from_utf8()`
* 🆕 AVX 512 support on modern x86/x86-64 CPUs since Rust 1.89
* Supports AVX 2 and SSE 4.2 implementations on x86 and x86-64
* ARM64 (aarch64) SIMD is supported since Rust 1.61
* WASM (wasm32) SIMD is supported
* 🆕 armv7 NEON support with the `armv7_neon` feature on nightly Rust
* x86-64: Up to 23 times faster than the std library on valid non-ASCII, up to four times faster on ASCII
* aarch64: Up to eleven times faster than the std library on valid non-ASCII, up to four times faster on ASCII (Apple Silicon)
* Faster than the original simdjson implementation
* Selects the fastest implementation at runtime based on CPU support (on x86)
* Falls back to the excellent std implementation if SIMD extensions are not supported
* Written in pure Rust
* No-std support

## Quick start
Add the dependency to your Cargo.toml file:
```toml
[dependencies]
simdutf8 = "0.1.5"
```

Use `simdutf8::basic::from_utf8()` as a drop-in replacement for `std::str::from_utf8()`.

```rust
use simdutf8::basic::from_utf8;

println!("{}", from_utf8(b"I \xE2\x9D\xA4\xEF\xB8\x8F UTF-8!").unwrap());
```

If you need detailed information on validation failures, use `simdutf8::compat::from_utf8()`
instead.

```rust
use simdutf8::compat::from_utf8;

let err = from_utf8(b"I \xE2\x9D\xA4\xEF\xB8 UTF-8!").unwrap_err();
assert_eq!(err.valid_up_to(), 5);
assert_eq!(err.error_len(), Some(2));
```

## APIs

### Basic flavor
Use the `basic` API flavor for maximum speed. It is fastest on valid UTF-8, but only checks
for errors after processing the whole byte sequence and does not provide detailed information if the data
is not valid UTF-8. `simdutf8::basic::Utf8Error` is a zero-sized error struct.

### Compat flavor
The `compat` flavor is fully API-compatible with `std::str::from_utf8()`. In particular, `simdutf8::compat::from_utf8()`
returns a `simdutf8::compat::Utf8Error`, which has `valid_up_to()` and `error_len()` methods. The first is useful for
verification of streamed data. The second is useful e.g. for replacing invalid byte sequences with a replacement character.

It also fails early: errors 
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

