---
id: repo-fetched-async-profiler-132147-132220
type: knowledge
owner: OA
registered_at: 2026-04-05T03:33:35.811475
tags: ["auto-cloned", "oa-assimilated"]
---

# FETCHED_async-profiler_132147_132220

## Assimilation Report
Auto-cloned repository: FETCHED_async-profiler_132147_132220

## Application for OmniClaw
No structural integration blueprint provided.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
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
- and [more](docs/ProfilingModes.md).

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
as an interactive [Flame Graph](docs/FlamegraphInterpretation.md) that can be viewed in a browser.

[![FlameGraph](/.assets/images/flamegraph.png)](https://htmlpreview.github.io/?https://github.com/async-profiler/async-profiler/blob/master/.assets/html/flamegraph.html)

Find more details in the [Getting started guide](docs/GettingStarted.md).

# Building

### Build status

[![Build Status](https://github.com/async-profiler/async-profiler/actions/workflows/test-and-publish-nightly.yml/badge.svg?branch=master)](https://github.com/async-profiler/async-profiler/actions/workflows/test-and-publish-nightly.yml)

### Minimum requirements

- make
- GCC 7.5.0+ or Clang 7.0.0+
- Static version of libstdc++ (e.g. on Amazon Linux 2023: `yum install libstdc++-static`)
- JDK 11+

### How to build

Make sure `gcc`, `g++` and `java` are available on the `PATH`.
Navigate to the root directory with async-profiler sources and run `make`.
async-profiler launcher will be available at `build/bin/asprof`.

Other Makefile targets:

- `make test` - run unit and integration tests;
- `make release` - package async-profiler binaries as `.tar.gz` (Linux) or `.zip` (macOS).

### Supported platforms

|           | Officially maintained builds | Other available ports                     |
| --------- | ---------------------------- | ----------------------------------------- |
| **Linux** | x64, arm64                   | x86, arm32, ppc64le, riscv64, loongarch64 |
| **macOS** | x64, arm64                   |                                           |

# Documentation

## Basic usage

- [Getting Started](docs/GettingStarted.md)
- [Profiler Options](docs/ProfilerOptions.md)
- [Profiling Modes](docs/ProfilingModes.md)
- [Integrating async-profiler](docs/IntegratingAsyncProfiler.md)
- [Profiling In Container](docs/ProfilingInContainer.md)

## Profiler output

- [Output Formats](docs/OutputFormats.md)
- [FlameGraph Interpretation](docs/FlamegraphInterpretation.md)
- [JFR Visualization](docs/JfrVisualization.md)
- [Converter Usage](docs/ConverterUsage.md)
- [Heatmap](docs/Heatmap.md)

## Advanced usage

- [CPU Sampling Engines](docs/CpuSamplingEngines.md)
- [Stack Walking Modes](docs/StackWalkingModes.md)
- [Advanced Stacktrace Features](docs/AdvancedStacktraceFeatures.md)
- [Profiling Non-Java Applications](docs/ProfilingNonJavaApplications.md)

## Troubleshooting

For known issues faced while running async-profiler and their detailed troubleshooting,
please refer [here](docs/Troubleshooting.md).

```

### File: CHANGELOG.md
```md
# Changelog

## [4.3]

### Features

 - #1547: Native lock profiling
 - #1566: Filter cpu/wall profiles by latency
 - #1568: Expose async-profiler metrics in Prometheus format
 - #1628: async-profiler.jar as Java agent; remote control via JMX

### Improvements

 - #1140: FlameGraph improvements: legend, hot keys, new toolbar icons
 - #1530: Timezone switcher between Local and UTC time in Heatmaps
 - #1582: Support `--include`/`--exclude` options for JFR to Heatmap/OTLP/pprof conversion
 - #1624: Compatibility with OTLP v1.9.0
 - #1629: Harden crash protection in StackWalker

### Breaking changes

 - #1277: New `timeSpan` field in WallClockSample events
 - #1518: Deprecate `check` command
 - #1590: Support compilation on modern JDKs. Drop JDK 7 support

### Bug fixes

 - #1599: Workaround for the kernel PERF_EVENT_IOC_REFRESH bug
 - #1596: Do not block any signals during execution of a custom crash handler
 - #1584: JfrReader loops on corrupted recordings
 - #1555: Parse FlameGraph title from HTML input
 - #1621: `loop` and `timeout` options do not work together
 - #1641: Unwind vDSO correctly on Linux-ARM64
 - #1648: Fix stop sequence in Profiler::start
 - #1575: Fix CodeCache memory leak in lock profiling while looping
 - #1558: Fix record-cpu bug when kernel stacks are not available
 - #1651: Do not record CPU frame for non-perf samples
 - #1614, #1615, #1617, #1623: Fix races related to VM termination

## [4.2.1] - 2025-11-22

### Bug fixes

 - #1599: Workaround for the kernel PERF_EVENT_IOC_REFRESH bug
 - #1596: Do not block any signals during execution of a custom crash handler

## [4.2] - 2025-10-20

### Features

 - Java Method Tracing and Latency Profiling
   * #1421: Latency profiling
   * #1435: Allow wildcards in Instrument profiling engine
   * #1499: `--trace` option with per-method latency threshold
 - System-wide process sampling on Linux
   * #1411: `--proc` option to record `profiler.ProcessSample` events
 - VMStructs stack walker by default
   * #1539: Use VMStructs stack walking mode by default
   * #1537: Support `comptask` and `vtable` features
   * #1517: Use JavaFrameAnchor to find top Java frame
   * #1449: Special handling of prologue and epilogue of compiled methods

### Improvements

 - #1475: Add `CPUTimeSample` event support to jfrconv
 - #1414: Per-thread flamegraph option in JFR heatmap converter
 - #1526: Expose JfrReader dictionary that maps osThreadId to javaThreadId
 - #1448: Thread name in OpenTelemetry output
 - #1413: Add `time_nanos` and `duration_nanos` to OTLP profiles
 - #1450: Unwind dylib stubs as empty frames on macOS
 - #1416: Add synthetic symbols for Mach-O stubs/trampolines
 - Allow cross-compilation for 32-bit platforms

### Bug fixes

 - #1515: Fix UnsatisfiedLinkError when tmpdir is set to a relative path
 - #1500: Detect if `calloc` calls `malloc` for nativemem profiling
 - #1427: Re-implement SafeAccess crash protection
 - #1417: Two wall-clock profilers interfere with each other

### Project Infrastructure

 - #1527: GHA: replace macos-13 with macos-15-intel
 - #1510: Add option to retry tests
 - #1508: Add more GHA jobs to cover JDK versions on ARM
 - #1502: Fix job dependencies between integration tests and builds
 - #1466: Add Liberica JDK on Alpaquita Linux to the CI
 - Made integration tests more stable overall

## [4.1] - 2025-07-21

### Features
 - Experimental support for the OpenTelemetry profiling signal
   * #1188: OTLP output format and `dumpOtlp` Java API
   * #1336: JFR to OTLP converter
 - JDK 25 support
   * #1222: Update VMStructs for JDK 25
 - Productize native memory profiling
   * #1193: Full `nativemem` support on macOS
   * #1254: Fixed Nativemem tests on Alpine
   * #1269: Native memory profiling now works with `jemalloc`
   * #1323: `nativemem` shows allocations inside async-profiler itself

### Improvements
 - #1174: Detect JVM in non-Java application and attach to it
 - #1223: Native API to add custom events in JFR recording
 - #1259: `--all` option to collect all possible events simultaneously
 - #1286: Record which CPU a sample was taken on
 - #1299: Skip last 10% allocations for leak detection
 - #1300: Allow profiling kprobes/uprobes with `--fdtransfer`
 - #1366: Rewrite `jfrconv` executable to shell
 - #1400: Unwind checksum and digest intrinsics on ARM64
 - #1357, #1389: VMStructs-based stack unwinding for `alloc` and `nativemem` profiling

### Bug fixes
 - #1251: `--ttsp` option does not work on Alpine
 - #1264: Guard hook installation with dlopen/dlclose
 - #1319: SIGSEGV in PerfEvents::walk
 - #1350: Disable JFR OldObjectSample event in jfrsync mode
 - #1358: Do not dereference jmethodIDs on JDK 26
 - #1374: Correctly check if profiler is preloaded
 - #1380: Workaround clang type promotion bug
 - #1387: JFR writer crashes when using cstack=vmx
 - #1393: Improve stack walking termination logic: no endless `unknown` frames
 - Stack unwinding fixes for ARM64

### Project Infrastructure
 - #1129: Command-line option to filter tests
 - #1262: Include `asprof.h` in async-profiler release package
 - #1271: Release additional binaries with debug symbols
 - #1274: Add Corretto 8 to the test matrix
 - #1246, #1226: Run tests on Amazon Linux and Alpine Linux
 - #1360: Auto-generated clang-tidy review comments
 - #1373: Save all generated test logs for debug purposes
 - Fixed flaky tests (#1282, #1307, #1376)

## [4.0] - 2025-04-08

### Features
 - #895, #905: `jfrconv` binary and numerous converter enhancements
 - #944: Interactive Heatmap
 - #1064: Native memory leak profiler
 - #1002: An option to display instruction addresses
 - #1007: Optimize wall clock profiling
 - #1073: Productize VMStructs-based stack walker: `--cstack vm/vmx`
 - #1169: C API for accessing thread-local profiling context

### Improvements
 - #923: Support JDK 23+
 - #952: Solve musl and glibc compatibility issues; link `libstdc++` statically
 - #955: `--libpath` option to specify path to `libasyncProfiler.so` in a container
 - #1018: `--grain` converter option to coarsen flame graphs
 - #1046: `--nostop` option to continue profiling outside `--begin`/`--end` window
 - #1178: `--inverted` option to flip flame graphs vertically
 - #1009: Allows collecting allocation and live object traces at the same time
 - #925: An option to accumulate JFR events in memory instead of flushing to a file
 - #929: Load symbols from debuginfod cache
 - #982: Sample contended locks by overflowing interval bucket
 - #993: Filter native frames in allocation profile
 - #896: FlameGraph: `Alt+Click` to remove stacks
 - #1097: FlameGraph: `N`/`Shift+N` to navigate through search results
 - #1182: Retain by-thread grouping when reversing FlameGraph
 - #1167: Log when no samples are collected
 - #1044: Fall back to `ctimer` for CPU profiling when perf_events are unavailable
 - #1068: Count missed samples when estimating total CPU time in `ctimer` mode
 - #1142: Use counter-timer register for timestamps on ARM64
 - #1123: Support `clock=tsc` without a JVM
 - #1070: Demangle Rust v0 symbols
 - #1007: Use `ExecutionSample` event for CPU profiling and `WallClockSample` for Wall clock profiling
 - #1011: Obtain `can_generate_sampled_object_alloc_events` JVMTI capability only when needed
 - #1013: Intercept java.util.concurrent locks more efficiently
 - #759: Discover available profiling signal automatically
 - #884: Record event timestamps early
 - #885: Print error message if JVM fails to load libasyncProfiler
 - #892: Resolve tracepoint id in `asprof`
 - Suppress dynamic attach warning on JDK 21+

### Bug fixes
 - #1143: Crash on macOS when using thread filter
 - #1125: Fixed parsing concurrently loaded libraries
 - #1095: jfr print fails when a recording has empty pools
 - #1084: Fixed Logging related races
 - #1074: Parse both .rela.dyn and .rela.plt sections
 - #1003: Support both tracefs and debugfs for kernel tracepoints
 - #986: Profiling output respects loglevel
 - #981: Avoid JVM crash by deleting JNI refs after `GetMethodDeclaringClass`
 - #934: Fix crash on Zing in a native thread
 - #843: Fix race between parsing and concurrent unloading of shared libraries
 - #1147, #1151: Deadlocks with jemalloc and tcmalloc profilers
 - Stack walking fixes for ARM64
 - Converter fixes for `jfrsync` profiles
 - Fixed parsing non-PIC executables and shared objects with non-standard section layout
 - Fixed recursion in `pthread_create` when using native profiling API
 - Fixed crashes on Alpine when profiling native apps
 - Fixed warnings with `-Xcheck:jni`
 - Fixed "Unsupported JVM" on OpenJ9 JDK 21
 - Fixed DefineClass crash on OpenJ9
 - JfrReader should handle custom events properly
 - Handle truncated JFRs

### Project Infrastructure
 - Restructure and update documentation
 - Implement test framework; add new integration tests
 - Unit test framework for C++ code
 - Run CI on all supported platforms
 - Test multiple JDK versions in CI
 - Add GHA to validate license headers
 - Add Markdown checker and formatter
 - Add Issue and Pull Request templates
 - Add Contributing Guidelines and Code of Conduct
 - Run static analyzer and fix found issues (#1034, #1039, #1049, #1051, #1098)
 - Provide Dockerfile for building async-profiler release packages
 - Publish nightly builds automatically

## [3.0] - 2024-01-20

### Features
 - #724: Binary launcher `asprof`
 - #751: Profile non-Java processes
 - #795: AsyncGetCallTrace replacement
 - #719: Classify execution samples into categories in JFR converter
 - #855: `ctimer` mode for accurate profiling without perf_events
 - #740: Profile CPU + Wall clock together
 - #736: Show targets of vtable/itable calls
 - #777: Show JIT compilation task
 - #644: RISC-V port
 - #770: LoongArch64 port

### Improvements
 - #733: Make the same `libasyncProfiler` work with both glibc and musl
 - #734: Support raw PMU event descriptors
 - #759: Configure alternative profiling signal
 - #761: Parse dynamic linking structures
 - #723: `--clock` option to select JFR timestamp source
 - #750: `--jfrsync` may specify a list of JFR events
 - #849: Parse concatenated multi-chunk JFRs
 - #833: Time-to-safepoint JFR event
 - #832: Normalize names of hidden classes / lambdas
 - #864: Reduce size of HTML Flame Graph
 - #783: Shutdown asprof gracefully on SIGTERM
 - Better demangling of C++ and Rust symbols
 - DWARF unwinding for ARM64
 - `JfrReader` can parse in-memory buffer
 - Support custom events in `JfrReader`
 - An option to read JFR file by chunks
 - Record `GCHeapSummary` events in JFR

### Bug fixes
 - Workaround macOS crashes in SafeFetch
 - Fixed attach to OpenJ9 on macOS
 - Support `UseCompressedObjectHeaders` aka Lilliput
 - Fixed allocation profiling on JDK 20.0.x
 - Fixed context-switches profiling
 - Prefer ObjectSampler to TLAB hooks for allocation profiling
 - Improved accuracy of ObjectSampler in `--total` mode
 - Make Flame Graph status line and search results always visible
 - `loop` and `timeout` options did not work in some modes
 - Restart interrupted poll/epoll_wait syscalls
 - Fixed stack unwinding issues on ARM64
 - Workaround for stale jmethodIDs
 - Calculate ELF base address correctly
 - Do not dump redundant threads in a JFR chunk
 - `check` action prints result to a file
 - Annotate JFR unit types with `@ContentType`

## [2.9] - 2022-11-27

### Features
 - Java Heap leak profiler
 - `meminfo` command to print profiler's memory usage
 - Profiler API with embedded agent as a Maven artifact

### Improvements
 - `--include`/`--exclude` options in the FlameGraph converter
 - `--simple` and `--dot` options in jfr2flame converter
 - An option for agressive recovery of `[unknown_Java]` stack traces
 - Do not truncate signatures in collapsed format
 - Display inlined frames under a runtime stub

### Bug fixes
 - Profiler did not work with Homebrew JDK
 - Fixed allocation profiling on Zing
 - Various `jfrsync` fixes
 - Symbol parsing fixes
 - Attaching to a container on Linux 3.x could fail

## [2.8.3] - 2022-07-16

### Improvements
 - Support virtualized ARM64 macOS
 - A switch to generate auxiliary events by async-profiler or FlightRecorder in jfrsync mode

### Bug fixes
 - Could not recreate perf_events after the first failure
 - Handle different versions of Zing properly
 - Do not call System.loadLibrary, when libasyncProfiler is preloaded

## [2.8.2] - 2022-07-13

### Bug fixes
 - The same .so works with glibc and musl
 - dlopen hook did not work on Arch Linux
 - Fixed JDK 7 crash
 - Fixed CPU profiling on Zing

### Changes
 - Mark interpreted frames with `_[0]` in collapsed output
 - Double click selects a method name on a flame graph

## [2.8.1] - 2022-06-10

### Improvements
 - JFR to pprof converter (contributed by @NeQuissimus)
 - JFR converter improvements: time range, collapsed output, pattern highlighting
 - `%n` pattern in file names; limit number of output files
 - `--lib` to customize profiler library path in a container
 - `profiler.sh list` command now works without PID

### Bug fixes
 - Fixed crashes related to continuous profiling
 - Fixed Alpine/musl compatibility issues
 - Fixed incomplete collapsed output due to weird locale settings
 - Workaround for JDK-8185348

## [2.8] - 2022-05-09

### Features
 - Mark top methods as interpreted, compiled (C1/C2), or inlined
 - JVM TI based allocation profiling for JDK 11+
 - Embedded HTTP management server

### Improvements
 - Re-implemented stack recovery for better reliability
 - Add `loglevel` argument
 - Do not mmap perf page in `--all-user` mode
 - Distinguish runnable/sleeping threads in OpenJ9 wall-clock profiler
 - `--cpu` converter option to extract CPU profile from the wall-clock output

## [2.7] - 2022-02-14

### Features
 - Experimental support for OpenJ9 VM
 - DWARF stack unwinding

### Improvements
 - Better handling of VM threads (fixed missing JIT threads)
 - More reliable recovery from `not_walkable` AGCT failures
 - Do not accept unknown agent arguments

## [2.6] - 2022-01-09

### Features
 - Continuous profiling; `loop` and `timeout` options

### Improvements
 - Reliability improvements: avoid certain crashes and deadlocks
 - Smaller and faster agent library
 - Minor `jfr` and `jfrsync` enhancements (see the commit log)

## [2.5.1] - 2021-12-05

### Bug fixes
 - Prevent early unloading of libasyncProfiler.so
 - Read kernel symbols only for perf_events
 - Escape backslashes in flame graphs
 - Avoid duplicate categories in `jfrsync` mode
 - Fixed stack overflow in RedefineClasses
 - Fixed deadlock when flushing JFR

### Improvements
 - Support OpenJDK C++ Interpreter (aka Zero)
 - Allow reading incomplete JFR recordings

## [2.5] - 2021-10-01

### Features
 - macOS/ARM64 (aka Apple M1) port
 - PPC64LE port (contributed by @ghaug)
 - Profile low-privileged processes with perf_events (contributed by @Jongy)
 - Raw PMU events; kprobes & uprobes
 - Dump results in the middle of profiling session
 - Chunked JFR; support JFR files larger than 2 GB
 - Integrate async-profiler events with JDK F
... [TRUNCATED]
```

### File: CODE_OF_CONDUCT.md
```md
## Code of Conduct
This project has adopted the [Amazon Open Source Code of Conduct](https://aws.github.io/code-of-conduct).
For more information see the [Code of Conduct FAQ](https://aws.github.io/code-of-conduct-faq) or contact
opensource-codeofconduct@amazon.com with any additional questions or comments.

```

### File: CONTRIBUTING.md
```md
# Contributing Guidelines

Thank you for your interest in contributing to our project. Whether it's a bug report, new feature, correction, or additional
documentation, we greatly value feedback and contributions from our community.

Please read through this document before submitting any issues or pull requests to ensure we have all the necessary
information to effectively respond to your bug report or contribution.


## Security issue notifications
If you discover a potential security issue in this project we ask that you notify AWS/Amazon Security via our [vulnerability reporting page](http://aws.amazon.com/security/vulnerability-reporting/). Please do **not** create a public GitHub issue.


## Reporting Bugs/Feature Requests

We welcome you to use the GitHub issue tracker to report bugs or suggest features.

When filing an issue, please check [existing open](https://github.com/async-profiler/async-profiler/issues), or [recently closed](https://github.com/async-profiler/async-profiler/issues?q=is%3Aissue+is%3Aclosed), issues to make sure somebody else hasn't already
reported the issue. Please try to include as much information as you can. Details like these are incredibly useful:

* A reproducible test case or series of steps
* The version of our code being used
* Any modifications you've made relevant to the bug
* Anything unusual about your environment or deployment


## Contributing via Pull Requests
Contributions via pull requests are much appreciated. Before sending us a pull request, please ensure that:

1. You are working against the latest source on the *master* branch.
2. You check existing open, and recently merged, pull requests to make sure someone else hasn't addressed the problem already.
3. You open an issue to discuss any significant work - we would hate for your time to be wasted.

To send us a pull request, please:

1. Fork the repository.
2. Modify the source; please focus on the specific change you are contributing. If you also reformat all the code, it will be hard for us to focus on your change.
3. Ensure local tests pass.
4. Commit to your fork using clear commit messages.
5. Send us a pull request, answering any default questions in the pull request interface.
6. Pay attention to any automated CI failures reported in the pull request, and stay involved in the conversation.

GitHub provides additional document on [forking a repository](https://help.github.com/articles/fork-a-repo/) and
[creating a pull request](https://help.github.com/articles/creating-a-pull-request/).


## Finding contributions to work on
Looking at the existing issues is a great way to find something to contribute on. As our projects, by default, use the default GitHub issue labels (enhancement/bug/duplicate/help wanted/invalid/question/wontfix), looking at any ['help wanted'](https://github.com/async-profiler/async-profiler/labels/help%20wanted) issues is a great place to start.


## Code of Conduct
This project has adopted the [Amazon Open Source Code of Conduct](https://aws.github.io/code-of-conduct).
For more information see the [Code of Conduct FAQ](https://aws.github.io/code-of-conduct-faq) or contact
opensource-codeofconduct@amazon.com with any additional questions or comments.


## Licensing

See the [LICENSE](LICENSE) file for our project's licensing. We will ask you to confirm the licensing of your contribution.

```

### File: SECURITY.md
```md
## Reporting Security Issues

We take all security reports seriously.
When we receive such reports,
we will investigate and subsequently address
any potential vulnerabilities as quickly as possible.
If you discover a potential security issue in this project,
please notify AWS/Amazon Security via our [vulnerability reporting page](http://aws.amazon.com/security/vulnerability-reporting/).
Please do *not* create a public GitHub issue in this project.

```

### File: VETTING_REPORT.md
```md
---
title: Auto Vetting Report for async_profiler
date: 2026-04-05
analyst: civ_vetting_pipeline
status: AUTO_VETTED
---

# Auto-Vetted Repository
This repository was automatically swept and vetted by the batch processor. Only documentation remains.

```

### File: .github\PULL_REQUEST_TEMPLATE.md
```md
### Description


### Related issues


### Motivation and context


### How has this been tested?


---

By submitting this pull request, I confirm that my contribution is made under the terms of the [Apache 2.0 license].

[Apache 2.0 license]: https://www.apache.org/licenses/LICENSE-2.0

```

### File: docs\AdvancedStacktraceFeatures.md
```md
# Advanced Stacktrace Features

## Display JIT compilation task

Async-profiler samples JIT compiler threads just the same way as Java threads, and hence can show
CPU percentage spent on JIT compilation. At the same time, Java methods are different:
some take more resources to compile, other take less. Furthermore, there are cases when
a bug in C2 compiler causes a JIT thread to stuck in an infinite loop consuming 100% CPU.
Async-profiler can highlight which particular Java methods take most CPU time to compile.

![](/.assets/images/comptask_feature.png)

The feature can be enabled with the option `-F comptask` (or its agent equivalent `features=comptask`).

## Display actual implementation in vtable

In some applications, a significant amount of CPU time is spent on dispatching megamorphic virtual/interface calls.
async-profiler shows a pseudo-frame on top of v/itable stub with the actual type of object the virtual method is
called on. This should make clear the proportion of different receivers for the particular call site.

![](/.assets/images/vtable_feature.png)

The feature can be enabled with the option `-F vtable` (or its agent equivalent `features=vtable`).

## Display instruction addresses

Sometimes, for low-level performance analysis, it is important to know where exactly
CPU time is spent inside a method. As an intermediate step to the instruction-level
profiling, async-profiler provides an option to record PC address of the currently
running method for each execution sample. In this case, each stack trace will include
a synthetic frame with the address at the top of every stack trace.

![](/.assets/images/pcaddr_feature.png)

The feature can be enabled with the option `-F pcaddr` (or its agent equivalent `features=pcaddr`).

```

### File: docs\ConverterUsage.md
```md
# Converter Usage

async-profiler provides `jfrconv` utility to convert between different profile output formats.
`jfrconv` can be found at the same location as the `asprof` binary. Converter is also available
as a standalone Java application: [`jfr-converter.jar`](https://github.com/async-profiler/async-profiler/releases/latest/download/jfr-converter.jar).

## Supported conversions

The tool can convert several source formats into various outputs. The conversion capabilities are summarized below:

| Source format | to html | to collapsed | to pprof | to pb.gz | to heatmap | to otlp |
| ------------- | ------- | ------------ | -------- | -------- | ---------- | ------- |
| jfr           | ✅      | ✅           | ✅       | ✅       | ✅         | ✅      |
| html          | ✅      | ✅           | ❌       | ❌       | ❌         | ❌      |
| collapsed     | ✅      | ✅           | ❌       | ❌       | ❌         | ❌      |

## Usage

```
jfrconv [options] <input> [<input>...] <output>
```

The output format specified can be only one at a time for conversion from one format to another.

```
Conversion options:
  -o --output FORMAT, -o can be omitted if the output file extension unambiguously determines the format, e.g. profile.collapsed

  FORMAT can be any of the following:
  # collapsed: This is a collection of call stacks, where each line is a  semicolon separated
               list of frames followed by a counter. This is used by the FlameGraph script to
               generate the FlameGraph visualization of the profile data.

  # html: FlameGraph is a hierarchical representation of call traces of the profiled
          software in a color coded format that helps to identify a particular resource
          usage like CPU and memory for the application.

  # pprof: pprof is a profiling visualization and analysis tool from Google. More details on
           pprof on the official github page https://github.com/google/pprof.

  # pb.gz: This is a compressed version of pprof output.

  # heatmap: A single page interactive heatmap that allows to explore profiling events
             on a timeline.

  # otlp: OpenTelemetry profile format.

Differential Flame Graph:
  --diff <base-profile> <new-profile>

JFR options:
    --cpu              Generate only CPU profile during conversion
    --cpu-time         Generate only CPU profile, using CPUTimeSample events
    --wall             Generate only Wall clock profile during conversion
    --alloc            Generate only Allocation profile during conversion
    --live             Build allocation profile from live objects only during conversion
    --nativemem        Generate native memory allocation profile
    --leak             Only include memory leaks in nativemem
    --tail RATIO       Ignore tail allocations for leak profiling (10% by default)
    --lock             Generate only lock contention profile during conversion
    --nativelock       Generate only native (pthread) lock contention profile
    --trace            Convert only MethodTrace events
 -t --threads          Split stack traces by threads
 -s --state LIST       Filter thread states: runnable, sleeping, default. State name is case insensitive
                       and can be abbreviated, e.g. -s r
    --classify         Classify samples into predefined categories
    --total            Accumulate total value (time, bytes, etc.) instead of samples
    --lines            Show line numbers
    --bci              Show bytecode indices
    --simple           Simple class names instead of fully qualified names
    --norm             Normalize names of hidden classes/lambdas, e.g. Original JFR transforms
                       lambda names to something like pkg.ClassName$$Lambda+0x00007f8177090218/543846639
                       which gets normalized to pkg.ClassName$$Lambda
    --dot              Dotted class names, e.g. java.lang.String instead of java/lang/String
    --from TIME        Start time in ms (absolute or relative)
    --to TIME          End time in ms (absolute or relative)
                       TIME can be:
                       # an absolute timestamp specified in millis since epoch;
                       # an absolute time in hh:mm:ss or yyyy-MM-dd'T'hh:mm:ss format;
                       # a relative time from the beginning of recording;
                       # a relative time from the end of recording (a negative number).
    --latency MS       Retain only samples within MethodTraces of at least MS milliseconds

Flame Graph options:
    --title STRING     Convert to Flame Graph with provided title
    --minwidth X       Skip frames smaller than X%
    --grain X          Coarsen Flame Graph to the given grain size
    --skip N           Skip N bottom frames
 -r --reverse          Reverse stack traces (defaults to icicle graph)
 -i --inverted         Toggles the layout for reversed stacktraces from icicle to flamegraph
                       and for default stacktraces from flamegraph to icicle
 -I --include REGEX    Include only stacks with the specified frames, e.g. -I 'MyApplication\.main' -I 'VMThread.*'
 -X --exclude REGEX    Exclude stacks with the specified frames, e.g. -X '.*pthread_cond_(wait|timedwait).*'
    --highlight REGEX  Highlight frames matching the given pattern
```

See the [profiler options documentation](ProfilerOptions.md#options-applicable-to-flamegraph-and-tree-view-outputs-only) for details on the `--reverse` and `--inverted` options.

## jfrconv examples

`jfrconv` utility is provided in `bin` directory of the async-profiler package.
It requires JRE to be installed on the system.

### Generate Flame Graph from JFR

If no output file is specified, it defaults to a Flame Graph output.

```
jfrconv foo.jfr
```

Profiling in JFR mode allows multi-mode profiling. So the command above will generate a Flame Graph
output, however, for a multi-mode profile output with both `cpu` and `wall-clock` events, the
Flame Graph will have an aggregation of both in the view. Such a view wouldn't make much sense and
hence it is advisable to use JFR conversion filter options like `--cpu` to filter out events
during a conversion.

```
jfrconv --cpu foo.jfr

# which is equivalent to:
# jfrconv --cpu -o html foo.jfr foo.html
```

for HTML output as HTML is the default format for conversion from JFR.

### Flame Graph options

To add a custom title to the generated Flame Graph, use `--title`, which has the default value `Flame Graph`:

```
jfrconv --cpu foo.jfr foo.html -r --title "Custom Title"
```

### Differential Flame Graph

To find performance regressions, it may be useful to compare current profile
to a previous one that serves as a baseline. Differential Flame Graph
visualizes such a comparsion with a special color scheme:

- Red color denotes frames with more samples comparing to the baseline (i.e. regression);
- Blue is for frames with less samples;
- Yellow are new frames that were absent in the baseline.

The more intense the color, the larger the delta.
For each different frame, the delta value is displayed in a tooltip.

![](/.assets/images/flamegraph_diff.png)

Differential Flame Graph takes the shape of the current profile:
all frames have exactly the same size as in the normal Flame Graph.
This means, frames that exist only in the base profile will not be visible.
To see such frames, create another differential Flame Graph,
swapping the base and the current input file.

To create differential Flame Graph, run `jfrconv --diff` with two input files:
basline profile and new profile. Both files can be in JFR, HTML, or collapsed format.
Other converter options work as usual.

```
jfrconv --cpu --diff baseline.jfr new.jfr diff.html
```

Output file name is optional. If omitted, `jfrconv` takes the name
of the second input file, replacing its extension with `.diff.html`.

## Standalone converter examples

Standalone converter jar is provided in
[Download](https://github.com/async-profiler/async-profiler/?tab=readme-ov-file#Download).
It accepts the same parameters as `jfrconv`.

Below is an example usage:

```
java -jar jfr-converter.jar --cpu foo.jfr --reverse --title "Application CPU profile"
```

```

### File: docs\CpuSamplingEngines.md
```md
# CPU Sampling Engines

Async-profiler has three options for CPU profiling: `-e cpu`, `-e itimer` and `-e ctimer`.

## cpu

`cpu` mode measures CPU time spent by the running threads. For example,
if an application uses 2 cpu cores, each with 30% utilization, and the sampling interval is
10ms, then the profiler will collect about `2 * 0.3 * 100 = 60` samples per second.
In other words, 1 profiling sample means that one CPU core was actively running for N nanoseconds,
where N is the profiling interval.

On Linux, `cpu` mode relies on [perf_events](https://man7.org/linux/man-pages/man2/perf_event_open.2.html).
One `perf_event` descriptor is created for each running thread and configured to generate a signal
every `N` nanoseconds of CPU time. This is the most accurate CPU sampler available in async-profiler
and the only one that can obtain kernel stack traces. It, however, comes with certain restrictions.

Most importantly, OS configuration may limit access to `perf_events` API, e.g.,
by `kernel.perf_event_paranoid` sysctl or by seccomp (which is often the case in a Docker container).
If `perf_events` are available, but kernel symbols are hidden (e.g., by `kernel.kptr_resitrct` setting),
async-profiler continues to use `perf_events`, emits a warning and does not show kernel stack traces.

Another important thing to consider is that `cpu` sampling engine allocates a descriptor per thread.
This means, if an application has too many threads and OS limit for the maximum number of open descriptors
(`ulimit -n`) is too low, an application may run out of file descriptors. The workaround
is to simply increase file descriptor limit.

## itimer

`itimer` mode is based on [setitimer(ITIMER_PROF)](https://man7.org/linux/man-pages/man2/setitimer.2.html)
syscall, which ideally generates a signal every given interval of CPU time consumed by the process.
Ideally, both `itimer` and `cpu` should collect the same number of samples. Typically,
profiles indeed look very similar. However, in [some cases](https://github.com/golang/go/issues/14434),
`cpu` profile appears more accurate, since a signal is delivered exactly to the thread
that overflowed a hardware counter. In contrast, `itimer` has the following limitations:

- Only one `itimer` signal can be delivered to a process at a time.
- Signals are not distributed evenly between running threads.
- Sampling resolution is limited by the size of [jiffies](https://man7.org/linux/man-pages/man7/time.7.html).

`itimer` profiles may be even less accurate on macOS, where `itimer` signals are often biased
towards system calls.

The main advantage of `itimer` is that it works in containers and does not consume file descriptors.

## ctimer

`ctimer` is a Linux-specific alternative for `cpu` profiling mode to overcome limitations
of `perf_events`, such as `perf_event_paraniod` setting, seccomp restriction or a low limit
for the number of open file descriptors. `ctimer` mode relies on
[timer_create](https://man7.org/linux/man-pages/man2/timer_create.2.html) API.
It combines benefits of `-e cpu` and `-e itimer`, except that it does not allow collecting kernel stacks.

Like with `itimer`, `ctimer` resolution is limited by the size of the jiffy -
kernel `HZ` constant, which is typically equal to 100 or 250, meaning that the minimum supported
profiling interval is 10ms or 4ms respectively.

## Summary

Here is a summary of advantages and drawbacks of all CPU profiling engines:

| Attribute                         | cpu (perf_events) | itimer | ctimer |
| --------------------------------- | :---------------: | :----: | :----: |
| Can collect kernel stack traces   |        ✅         |   ❌   |   ❌   |
| High resolution                   |        ✅         |   ❌   |   ❌   |
| Accuracy / fairness               |        ✅         |   ❌   |   🆗   |
| Works in containers by default    |        ❌         |   ✅   |   ✅   |
| Does not consume file descriptors |        ❌         |   ✅   |   ✅   |
| macOS support                     |        ❌         |   ✅   |   ❌   |

When using `-e cpu` on Linux, async-profiler automatically checks for `perf_events` availability
by trying to create a dummy perf_event. If kernel-space profiling is not available,
async-profiler transparently falls back to `ctimer` mode. To force using `perf_events`
for user-space only profiling, specify `-e cpu-clock --all-user` instead of `-e cpu`.

The actual profiling engine (`perf_events`, `ctimer`, etc.) is now recorded in `jfr` output.

```

### File: docs\FlamegraphInterpretation.md
```md
# FlameGraph interpretation

To interpret a flame graph, the best way forward is to understand how it is created.

## Example application to profile

Let's take the below example:

```
main() {
     // some business logic
    func3() {
        // some business logic
        func7();
    }

    // some business logic
    func4();

    // some business logic
    func1() {
        // some business logic
        func5();
    }

    // some business logic
    func2() {
        // some business logic
        func6() {
            // some business logic
            func8(); // cpu intensive work here
    }
}
```

## Profiler sampling

Profiling starts by taking samples `X` times per second. Whenever a sample is taken,
the current call stack for it is saved. The diagram below shows the unsorted sampling view
before the sorting and aggregation takes place.

![](/.assets/images/ProfilerSamplings.png)

Below are the sampling numbers:

- `func3()->func7()`: 3 samples
- `func4()`: 1 sample
- `func1()->func5()`: 2 samples
- `func2()->func8()`: 4 samples
- `func2()->func6()`: 1 sample

## Sorting samples

Samples are then alphabetically sorted at the base level just after root (or main method) of the application.

![](/.assets/images/SortedSamplings.png)

Note that X-axis is no longer a timeline. Flame graph does not preserve information
on _when_ a particular stack trace was taken, it only indicates _how often_
a stack trace was observed during profiling.

## Aggregated view

The blocks for the same functions at each level of stack depth are then stitched together
to get an aggregated view of the flame graph.
![](/.assets/images/AggregatedView.png)

In this example, except `func4()`, no other function actually consumes
any resource at the base level of stack depth. `func5()`, `func6()`,
`func7()` and `func8()` are the ones consuming resources, with `func8()`
being a likely candidate for performance optimization.

CPU utilization is the most common use case for flame graphs, however,
there are other modes of profiling like allocation profiling to view
heap utilization and wall-clock profiling to view latency.

[More on various modes of profiling](ProfilingModes.md)

## Understanding FlameGraph colors

Color is another flame graph dimension that may be used to encode additional information
about each frame. Colors may have different meaning in various flame graph implementations.
async-profiler uses the following palette to differentiate frame types:

![](/.assets/images/flamegraph_colors.png)

```

### File: docs\GettingStarted.md
```md
# Getting started guide

## Before profiling

As of Linux 4.6, capturing kernel call stacks using `perf_events` from a non-root
process requires setting two kernel parameters. You can set them using sysctl as follows:

```
# sysctl kernel.perf_event_paranoid=1
# sysctl kernel.kptr_restrict=0
```

For better profiling accuracy, it is [recommended](Troubleshooting.md#known-limitations)
to start the JVM with `-XX:+UnlockDiagnosticVMOptions -XX:+DebugNonSafepoints` flags,
unless async-profiler is loaded at JVM startup.

## Find a process to profile

Common ways to find the target process include using
[`jps`](https://docs.oracle.com/en/java/javase/21/docs/specs/man/jps.html) and
[`pgrep`](https://man7.org/linux/man-pages/man1/pgrep.1.html).
For example, to list all Java process IDs with their full command lines, run
`pgrep -a java`. The next section includes an example using `jps`.

## Start profiling

async-profiler works in the context of the target Java application,
i.e. it runs as an agent in the process being profiled.
`asprof` is a tool to attach and control the agent.

A typical workflow would be to launch your Java application, attach
the agent and start profiling, exercise your performance scenario, and
then stop profiling. The agent's output, including the profiling results, will
be displayed on the console where you've started `asprof`.

Example:

```
$ jps
9234 Jps
8983 Computey
$ asprof start 8983
$ asprof stop 8983
```

The following may be used in lieu of the `pid` (8983):

- The keyword `jps`, which will find `pid` automatically, if there is a single Java process running in the system.
- The application name as it appears in the `jps` output: e.g. `Computey`

Alternatively, you may specify `-d` (duration) argument to profile
the application for a fixed period of time with a single command.

```
$ asprof -d 30 8983
```

By default, the profiling frequency is 100Hz (every 10ms of CPU time).
Here is a sample output of `asprof`:

```
--- Execution profile ---
Total samples:           687
Unknown (native):        1 (0.15%)

--- 6790000000 (98.84%) ns, 679 samples
  [ 0] Primes.isPrime
  [ 1] Primes.primesThread
  [ 2] Primes.access$000
  [ 3] Primes$1.run
  [ 4] java.lang.Thread.run

... a lot of output omitted for brevity ...

          ns  percent  samples  top
  ----------  -------  -------  ---
  6790000000   98.84%      679  Primes.isPrime
    40000000    0.58%        4  __do_softirq

... more output omitted ...
```

This indicates that the hottest method was `Primes.isPrime`, and the hottest
call stack leading to it comes from `Primes.primesThread`.

## Other use cases

- [Launching as an agent](IntegratingAsyncProfiler.md#launching-as-an-agent)
- [Java API](IntegratingAsyncProfiler.md#using-java-api)
- [IntelliJ IDEA](IntegratingAsyncProfiler.md#intellij-idea)

## FlameGraph visualization

async-profiler provides out-of-the-box [Flame Graph](https://www.brendangregg.com/flamegraphs.html) support.
Specify `-o flamegraph` argument to dump profiling results as an interactive HTML Flame Graph.
Also, Flame Graph output format will be chosen automatically if the target filename ends with `.html`.

```
$ jps
9234 Jps
8983 Computey
$ asprof -d 30 -f /tmp/flamegraph.html 8983
```

[![Example](/.assets/images/flamegraph.png)](https://htmlpreview.github.io/?https://github.com/async-profiler/async-profiler/blob/master/.assets/html/flamegraph.html)

The flame graph html can be opened in any browser of your choice for further interpretation.

Please refer to [Interpreting a Flame Graph](FlamegraphInterpretation.md)
to understand more on how to interpret a Flame Graph.

```

### File: docs\Heatmap.md
```md
# Heatmap

Problems to be solved with a profiler can be divided into two large categories:

1. Optimization of overall resource usage.
2. Troubleshooting of intermittent performance issues.

While flame graphs are handy for the first type of problems, they are not very helpful
for analyzing transient anomalies because they provide an aggregated view that lacks
any timeline information. To address the second type of problems, async-profiler offers
a converter from JFR format to an interactive heatmap in the form of a single-page HTML file.

Heatmap is an alternative representation of profile data that preserves timestamps
of particular samples. Essentially, it's a two-dimensional timeline composed of
colored blocks. Each block represents a short period of time (usually in the range of
milliseconds to seconds) with its color being the third dimension: the more intense
the color, the more events happened in a given period of time.

![](/.assets/images/heatmap.png)

The idea of heatmaps was borrowed from [FlameScope](https://github.com/Netflix/flamescope),
however, FlameScope targets short profiling intervals up to a few minutes, whereas
async-profiler implementation is capable of visualizing 24-hour recordings
with the granularity of 20 milliseconds. Moreover, heatmaps produced by async-profiler
are serverless: they are standalone self-contained HTML files that can be easily shared
and viewed without additional software besides a browser.

## Heatmap features

### Whole day profile

Heatmaps are optimized for information density. Full day of continuous profiling
can be presented on a single image, where an engineer can spot regular activity
patterns as well as anomalies at a glance.

Heatmaps are also optimized for footprint. Specialized compression algorithms
can pack 1 GB original JFR recording to an HTML page of 10-15 MB in size.

![](/.assets/images/heatmap1.png)

### Scale / zoom

Depending on the recording duration and level of detail you are interested in,
you can switch between 3 available scales. On the largest scale, each vertical line
represents 5 minutes of wall clock time, with each square corresponding to
5 second interval. On the finest scale, each square corresponds to 20 milliseconds,
allowing you to analyze profiling samples with a high resolution.

![](/.assets/images/heatmap2.png)

### Instant flame graphs

A click on any heatmap square displays a flame graph for this specific time interval.

![](/.assets/images/heatmap3.png)

Hold mouse button to select an arbitrary time range on a heatmap.
A flame graph for the given time range will be built automatically.

![](/.assets/images/heatmap4.png)

### Compare time ranges

Select target time range as described above. Holding `Ctrl` key,
move mouse pointer to choose another time range that will serve as a baseline.
You will then get a differential flame graph highlighting stacks
that were seen more often in the target time range comparing to the baseline.

![](/.assets/images/heatmap5.png)

### Search

Press `Ctrl+F` and enter a regex to search on the entire heatmap.
Time intervals containing matched stacks will be highlighted on a heatmap in blue.
Matching frames, if any, will be also highlighted on a flame graph.

`Ctrl+Shift+F` does the same, except that a flame graph will
retain stacks with matching frames only. All other stacks will be filtered out.

![](/.assets/images/heatmap6.png)

## Producing heatmaps

Heatmaps can only be generated from recordings in JFR format.
Run [`jfrconv`](ConverterUsage.md) tool with `-o heatmap` option.

Standard `jfrconv` options (`--cpu`, `--alloc`, `--from`/`--to`, `--simple`, etc.)
are also applicable to heatmaps.

Example:

```
jfrconv --cpu -o heatmap profiler.jfr heatmap-cpu.html
```

```

### File: docs\IntegratingAsyncProfiler.md
```md
# Integrating async-profiler

## Launching as an agent

If you need to profile some code as soon as the JVM starts up, instead of using `asprof`,
it is possible to attach async-profiler as an agent on the command line. For example:

```
$ java -agentpath:/path/to/libasyncProfiler.so=start,event=cpu,file=profile.html ...
```

On macOS, the library name is `libasyncProfiler.dylib` instead of `libasyncProfiler.so`.

Agent library is configured through the JVMTI argument interface.
The argument string is a comma-separated list of [profiler options](ProfilerOptions.md):

```
option[=value],option[=value]...
```

`asprof` internally converts command line arguments to the above format and attaches
`libasyncProfiler.so` agent to a running process.

Another important use of attaching async-profiler as an agent is for continuous profiling.

## Using Java API

async-profiler can be controlled programmatically using Java API. The corresponding Java library
is published to Maven Central. You can [include it](https://mvnrepository.com/artifact/tools.profiler/async-profiler/latest)
just like any other Maven dependency:

```
<dependency>
    <groupId>tools.profiler</groupId>
    <artifactId>async-profiler</artifactId>
    <version>X.Y</version>
</dependency>
```

### Example usage with the API

```
AsyncProfiler profiler = AsyncProfiler.getInstance();
```

The above gives us an instance of `AsyncProfiler` object which can be further used to start
actual profiling.

```
profiler.execute("start,jfr,event=cpu,file=/path/to/%p.jfr");
// do some meaningful work
profiler.execute("stop");
```

`%p` equates to the PID of the process. Filename may include other placeholders which
can be found in [Profiler Options](ProfilerOptions.md).
`file` should be specified only once, either in
`start` command with `jfr` output or in `stop` command with any other format.

## Intellij IDEA

Intellij IDEA comes bundled with async-profiler, which can be further configured to our needs
by selecting the `Java Profiler` menu option at `Settings/Preferences > Build, Execution, Deployment`.
Agent options can be modified for the specific use cases and also `Collect native calls` can be checked
to monitor non-java threads and native frames in Java stack traces.

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
