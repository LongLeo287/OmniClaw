---
id: tikv-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:31:22.249315
---

# KNOWLEDGE EXTRACT: tikv
> **Extracted on:** 2026-03-30 17:54:18
> **Source:** tikv

---

## File: `pprof-rs.md`
```markdown
# 📦 tikv/pprof-rs [🔖 PENDING/APPROVE]
🔗 https://github.com/tikv/pprof-rs


## Meta
- **Stars:** ⭐ 1607 | **Forks:** 🍴 136
- **Language:** Rust | **License:** Apache-2.0
- **Last updated:** 2026-03-25
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
A Rust CPU profiler implemented with the help of backtrace-rs

## README (trích đầu)
```
# pprof

`pprof` is a cpu profiler that can be easily integrated into a rust program.

[![Actions Status](https://github.com/tikv/pprof-rs/workflows/build/badge.svg)](https://github.com/tikv/pprof-rs/actions)
[![Crates.io](https://img.shields.io/crates/v/pprof.svg)](https://crates.io/crates/pprof)
[![Dependency Status](https://deps.rs/repo/github/tikv/pprof-rs/status.svg)](https://deps.rs/repo/github/tikv/pprof-rs)
[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2Ftikv%2Fpprof-rs.svg?type=shield)](https://app.fossa.com/projects/git%2Bgithub.com%2Ftikv%2Fpprof-rs?ref=badge_shield)

## Usage

First, get a guard to start profiling. Profiling will continue until this guard was dropped.

```rust
let guard = pprof::ProfilerGuardBuilder::default().frequency(1000).blocklist(&["libc", "libgcc", "pthread", "vdso"]).build().unwrap();
```

During the profiling time, you can get a report with the guard.

```rust
if let Ok(report) = guard.report().build() {
    println!("report: {:?}", &report);
};
```

`Debug` was implemented for `Report`. It will print a human-readable stack counter report. Here is an example:

```
FRAME: backtrace::backtrace::trace::h3e91a3123a3049a5 -> FRAME: pprof::profiler::perf_signal_handler::h7b995c4ab2e66493 -> FRAME: Unknown -> FRAME: prime_number::is_prime_number::h70653a2633b88023 -> FRAME: prime_number::main::h47f1058543990c8b -> FRAME: std::rt::lang_start::{{closure}}::h4262e250f8024b06 -> FRAME: std::rt::lang_start_internal::{{closure}}::h812f70926ebbddd0 -> std::panicking::try::do_call::h3210e2ce6a68897b -> FRAME: __rust_maybe_catch_panic -> FRAME: std::panicking::try::h28c2e2ec1c3871ce -> std::panic::catch_unwind::h05e542185e35aabf -> std::rt::lang_start_internal::hd7efcfd33686f472 -> FRAME: main -> FRAME: __libc_start_main -> FRAME: _start -> FRAME: Unknown -> THREAD: prime_number 1217
FRAME: backtrace::backtrace::trace::h3e91a3123a3049a5 -> FRAME: pprof::profiler::perf_signal_handler::h7b995c4ab2e66493 -> FRAME: Unknown -> FRAME: alloc::alloc::box_free::h82cea48ed688e081 -> FRAME: prime_number::main::h47f1058543990c8b -> FRAME: std::rt::lang_start::{{closure}}::h4262e250f8024b06 -> FRAME: std::rt::lang_start_internal::{{closure}}::h812f70926ebbddd0 -> std::panicking::try::do_call::h3210e2ce6a68897b -> FRAME: __rust_maybe_catch_panic -> FRAME: std::panicking::try::h28c2e2ec1c3871ce -> std::panic::catch_unwind::h05e542185e35aabf -> std::rt::lang_start_internal::hd7efcfd33686f472 -> FRAME: main -> FRAME: __libc_start_main -> FRAME: _start -> FRAME: Unknown -> THREAD: prime_number 1
FRAME: backtrace::backtrace::trace::h3e91a3123a3049a5 -> FRAME: pprof::profiler::perf_signal_handler::h7b995c4ab2e66493 -> FRAME: Unknown -> FRAME: prime_number::main::h47f1058543990c8b -> FRAME: std::rt::lang_start::{{closure}}::h4262e250f8024b06 -> FRAME: std::rt::lang_start_internal::{{closure}}::h812f70926ebbddd0 -> std::panicking::try::do_call::h3210e2ce6a68897b -> FRAME: __rust_maybe_catch_panic -> FRAME: std::panicking::t
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

