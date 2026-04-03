---
id: async-profiler-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:18:51.059581
---

# KNOWLEDGE EXTRACT: async-profiler
> **Extracted on:** 2026-03-30 17:29:12
> **Source:** async-profiler

---

## File: `async-profiler.md`
```markdown
# 📦 async-profiler/async-profiler [🔖 PENDING/APPROVE]
🔗 https://github.com/async-profiler/async-profiler
🌐 https://github.com/async-profiler/async-profiler/releases

## Meta
- **Stars:** ⭐ 8935 | **Forks:** 🍴 969
- **Language:** C++ | **License:** Apache-2.0
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Sampling CPU and HEAP profiler for Java featuring AsyncGetCallTrace + perf_events

## README (trích đầu)
```
# Async-profiler

This project is a low overhead sampling profiler for Java
that does not suffer from the [Safepoint bias problem](http://psy-lob-saw.blogspot.ru/2016/02/why-most-sampling-java-profilers-are.html).
It features HotSpot-specific API to collect stack traces
and to track memory allocations. The profiler works with
OpenJDK and other Java runtimes based on the HotSpot JVM.

Unlike traditional Java profilers, async-profiler monitors non-Java threads
(e.g., GC and JIT compiler threads) and shows native and kernel frames in stack traces.

What can be profiled:

- CPU time
- Allocations in Java Heap
- Native memory allocations and leaks
- Contended locks
- Hardware and software performance counters like cache misses, page faults, context switches
- and [more](brain/knowledge/docs_legacy/ProfilingModes.md).

See our [3 hours playlist](https://www.youtube.com/playlist?list=PLNCLTEx3B8h4Yo_WvKWdLvI9mj1XpTKBr)
to learn about more features.

# Download

### Stable release: [4.3](https://github.com/async-profiler/async-profiler/releases/tag/v4.3)

- Linux x64: [async-profiler-4.3-linux-x64.tar.gz](https://github.com/async-profiler/async-profiler/releases/download/v4.3/async-profiler-4.3-linux-x64.tar.gz)
- Linux arm64: [async-profiler-4.3-linux-arm64.tar.gz](https://github.com/async-profiler/async-profiler/releases/download/v4.3/async-profiler-4.3-linux-arm64.tar.gz)
- macOS arm64/x64: [async-profiler-4.3-macos.zip](https://github.com/async-profiler/async-profiler/releases/download/v4.3/async-profiler-4.3-macos.zip)
- Profile converters: [jfr-converter.jar](https://github.com/async-profiler/async-profiler/releases/download/v4.3/jfr-converter.jar)

### Nightly builds

[The most recent binaries](https://github.com/async-profiler/async-profiler/releases/tag/nightly) corresponding
to the latest successful commit in `master`.

For a build corresponding to one of the previous commits, go to
[Nightly Builds](https://github.com/async-profiler/async-profiler/actions/workflows/test-and-publish-nightly.yml),
click the desired build and scroll down to the artifacts section. These binaries are kept for 30 days.

# Quick start

In a typical use case, profiling a Java application is just a matter of a running `asprof` with a PID of a
running Java process.

```
$ asprof -d 30 -f flamegraph.html <PID>
```

The above command translates to: run profiler for 30 seconds and save results to `flamegraph.html`
as an interactive [Flame Graph](brain/knowledge/docs_legacy/FlamegraphInterpretation.md) that can be viewed in a browser.

[![FlameGraph](/.assets/images/flamegraph.png)](https://htmlpreview.github.io/?https://github.com/async-profiler/async-profiler/blob/master/.assets/html/flamegraph.html)

Find more details in the [Getting started guide](brain/knowledge/docs_legacy/GettingStarted.md).

# Building

### Build status

[![Build Status](https://github.com/async-profiler/async-profiler/actions/workflows/test-and-publish-nightly.yml/badge.svg?branch=master)](https://github.com/async-profiler/async-profiler/actions/workflows/test-and-pu
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

