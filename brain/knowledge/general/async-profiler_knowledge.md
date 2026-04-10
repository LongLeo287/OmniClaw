# Knowledge Dump for async-profiler

## File: .licenserc.yaml
```
header:
  - paths:
      - 'src/jattach'
    license:
      content: |
        Copyright The jattach authors
        SPDX-License-Identifier: Apache-2.0

    comment: on-failure

  - paths:
      - 'src'
      - 'test'
    paths-ignore:
      - 'src/jattach'
      - 'src/res'
      - '**/MANIFEST.MF'
    license:
      content: |
        Copyright The async-profiler authors
        SPDX-License-Identifier: Apache-2.0

    comment: on-failure

```

## File: changelog.md
```
# Changelog

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
 - Integrate async-profiler events with JDK Flight Recordings

### Improvements
 - Use RDTSC for JFR timestamps when possible
 - Show line numbers and bci in Flame Graphs
 - jfr2flame can produce Allocation and Lock flame graphs
 - Flame Graph title depends on the event and `--total`
 - Include profiler logs and native library list in JFR output
 - Lock profiling no longer requires JVM symbols
 - Better container support
 - Native function profiler can count the specified argument
 - An option to group threads by scheduling policy
 - An option to prepend library name to native symbols

### Notes
 - macOS build is provided as a fat binary that works both on x86-64 and ARM64
 - 32-bit binaries are no longer shipped. It is still possible to build them from sources
 - Dropped JDK 6 support (may still work though)

## [2.0] - 2021-03-14

### Features
 - Profile multiple events together (cpu + alloc + lock)
 - HTML 5 Flame Graphs: faster rendering, smaller size
 - JFR v2 output format, compatible with FlightRecorder API
 - JFR to Flame Graph converter
 - Automatically turn profiling on/off at `--begin`/`--end` functions
 - Time-to-safepoint profiling: `--ttsp`

### Improvements
 - Unlimited frame buffer. Removed `-b` option and 64K stack traces limit
 - Additional JFR events: OS, CPU, and JVM information; CPU load
 - Record bytecode indices / line numbers
 - Native stack traces for Java events
 - Improved CLI experience
 - Better error handling; an option to log warnings/errors to a dedicated stream
 - Reduced the amount of unknown stack traces

### Changes
 - Removed non-ASL code. No more CDDL license

## [1.8.4] - 2021-02-24

### Improvements
 - Smaller and faster agent library

### Bug fixes
 - Fixed JDK 7 crash during wall-clock profiling

## [1.8.3] - 2021-01-06

### Improvements
 - libasyncProfiler.dylib symlink on macOS

### Bug fixes
 - Fixed possible deadlock on non-HotSpot JVMs
 - Gracefully stop profiler when terminating JVM
 - Fixed GetStackTrace problem after RedefineClasses

## [1.8.2] - 2020-11-02

### Improvements
 - AArch64 build is now provided out of the box
 - Compatibility with JDK 15 and JDK 16

### Bug fixes
 - More careful native stack walking in wall-clock mode
 - `resume` command is not compatible with JFR format
 - Wrong allocation sizes on JDK 8u262

## [1.8.1] - 2020-09-05

### Improvements
 - Possibility to specify application name instead of `pid` (contributed by @yuzawa-san)

### Bug fixes
 - Fixed long attach time and slow class loading on JDK 8
 - `UnsatisfiedLinkError` during Java method profiling
 - Avoid reading `/proc/kallsyms` when `--all-user` is specified

## [1.8] - 2020-08-10

### Features
 - Converters between different output formats:
   - JFR -> nflx (FlameScope)
   - Collapsed stacks -> HTML 5 Flame Graph

### Improvements
 - `profiler.sh` no longer requires bash (contributed by @cfstras)
 - Fixed long attach time and slow class loading on JDK 8
 - Fixed deadlocks in wall-clock profiling mode
 - Per-thread reverse Flame Graph and Call Tree
 - ARM build now works with ARM and THUMB flavors of JDK

### Changes
 - Release package is extracted into a separate folder

## [1.7.1] - 2020-05-14

### Features
 - LBR call stack support (available since Haswell)

### Improvements
 - `--filter` to profile only specified thread IDs in wall-clock mode
 - `--safe-mode` to disable selected stack recovery techniques

## [1.7] - 2020-03-17

### Features
 - Profile invocations of arbitrary Java methods
 - Filter stack traces by the given name pattern
 - Java API to filter monitored threads
 - `--cstack`/`--no-cstack` option

### Improvements
 - Thread names and Java thread IDs in JFR output
 - Wall clock profiler distinguishes RUNNABLE vs. SLEEPING threads
 - Stable profiling interval in wall clock mode
 - C++ function names as events, e.g. `-e VMThread::execute`
 - `check` command to test event availability
 - Allow shading of AsyncProfiler API
 - Enable CPU profiling on WSL
 - Enable allocation profiling on Zing
 - Reduce the amount of `unknown_Java` samples

## [1.6] - 2019-09-09

### Features
 - Pause/resume profiling
 - Allocation profiling support for JDK 12, 13 (contributed by @rraptorr)

### Improvements
 - Include all AsyncGetCallTrace failures in the profile
 - Parse symbols of JNI libraries loaded in runtime
 - The agent autodetects output format by the file extension
 - Output file name patterns: `%p` and `%t`
 - `-g` option to print method signatures
 - `-j` can increase the maximum Java stack depth
 - Allocaton sampling rate can be adjusted with `-i`
 - Improved reliability on macOS

### Changes
 - `-f` file names are now relative to the current shell directory

## [1.5] - 2019-01-08

### Features
 - Wall-clock profiler: `-e wall`
 - `-e itimer` mode for systems that do not support perf_events
 - Native stack traces on macOS
 - Support for Zing runtime, except allocation profiling

### Improvements
 - `--all-user` option to allow profiling with restricted
   `perf_event_paranoid` (contributed by @jpbempel)
 - `-a` option to annotate method names
 - Improved attach to containerized and chroot'ed JVMs
 - Native function profiling now accepts non-public symbols
 - Better mapping of Java thread names (contributed by @KirillTim)

### Changes
 - Changed default profiling engine on macOS
 - Fixed the order of stack frames in JFR format

## [1.4] - 2018-06-24

### Features
 - Interactive Call tree and Backtrace tree in HTML format (contributed by @rpulle)
 - Experimental support for Java Flight Recorder (JFR) compatible output

### Improvements
 - Added units: `ms`, `us`, `s` and multipliers: `K`, `M`, `G` for interval argument
 - API and command-line option `-v` for profiler version
 - Allow profiling containerized JVMs on older kernels

### Changes
 - Default CPU sampling interval reduced to 10 ms
 - Changed the text format of flat profile

## [1.3] - 2018-05-13

### Features
 - Profiling of native functions, e.g. malloc

### Improvements
 - JDK 9, 10, 11 support for heap profiling with accurate stack traces
 - `root` can now profile Java processes of any user
 - `-j` option for limiting Java stack depth

## [1.2] - 2018-03-05

### Features
 - Produce SVG files out of the box; flamegraph.pl is no longer needed
 - Profile ReentrantLock contention
 - Java API

### Improvements
 - Allocation and Lock profiler now works on JDK 7, too
 - Faster dumping of results

### Changes
 - `total` counter of allocation profiler now measures heap pressure (like JMC)

## [1.1] - 2017-12-03

### Features
 - Linux Perf Events profiling: CPU cycles, cache misses, branch misses, page faults, context switches etc.
 - Kernel tracepoints support
 - Contended monitor (aka intrinsic lock) profiling
 - Individual thread profiles

### Improvements
 - Profiler can engage at JVM start and automatically dump results on exit
 - `list` command-line option to list supported events
 - Automatically find target process ID with `jps` tool
 - An option to include counter value in `collapsed` output
 - Friendly class names in allocation profile
 - Split allocations in new TLAB vs. outside TLAB

### Changes
 - Replaced `-m` modes with `-e` events
 - Interval changed from `int` to `long`

## [1.0] - 2017-10-09

### Features
 - CPU profiler without Safepoint bias
 - Lightweight Allocation profiler
 - Java, native and kernel stack traces
 - FlameGraph compatible output

```

## File: CMakeLists.txt
```
cmake_minimum_required(VERSION 3.22)
project(async-profiler)

set(CMAKE_CXX_STANDARD 11)
# -fno-omit-frame-pointer -fvisibility=hidden -Wl,-z,defs -fwhole-program -momit-leaf-frame-pointer
add_library(async-profiler
        ./src/arguments.cpp
        ./src/flameGraph.cpp
        ./src/profiler.cpp
        ./src/trap.cpp
        ./src/stackWalker.cpp
        ./src/symbols_macos.cpp
        ./src/tsc.cpp
        ./src/j9Ext.cpp
        ./src/codeCache.cpp
        ./src/itimer.cpp
        ./src/wallClock.cpp
        ./src/stackFrame_x64.cpp
        ./src/j9StackTraces.cpp
        ./src/mutex.cpp
        ./src/flightRecorder.cpp
        ./src/javaApi.cpp
        ./src/j9WallClock.cpp
        ./src/stackFrame_arm.cpp
        ./src/instrument.cpp
        ./src/j9ObjectSampler.cpp
        ./src/os_linux.cpp
        ./src/lockTracer.cpp
        ./src/dictionary.cpp
        ./src/fdtransferClient_linux.cpp
        ./src/perfEvents_linux.cpp
        ./src/linearAllocator.cpp
        ./src/stackFrame_i386.cpp
        ./src/stackFrame_ppc64.cpp
        ./src/jfrMetadata.cpp
        ./src/threadFilter.cpp
        ./src/dwarf.cpp
        ./src/log.cpp
        ./src/objectSampler.cpp
        ./src/os_macos.cpp
        ./src/stackFrame_aarch64.cpp
        ./src/engine.cpp
        ./src/vmStructs.cpp
        ./src/symbols_linux.cpp
        ./src/frameName.cpp
        ./src/vmEntry.cpp
        ./src/callTraceStorage.cpp
        ./src/allocTracer.cpp
        )
target_compile_options(async-profiler PRIVATE -fno-omit-frame-pointer -fvisibility=hidden -Wl,-z,defs -fwhole-program -momit-leaf-frame-pointer -fPIC)
target_compile_definitions(async-profiler PRIVATE PROFILER_VERSION=\"0.0.0\")
target_include_directories(async-profiler PRIVATE
        ./src
        ./src/res
        ./src/helper
        /usr/lib/jvm/java-11-openjdk-amd64/include
        /usr/lib/jvm/java-11-openjdk-amd64/include/linux)

# -DPROFILER_VERSION=\"2.9.0.2\" -I/usr/lib/jvm/java-11-openjdk-amd64/include -Isrc/res -Isrc/helper -I/usr/lib/jvm/java-11-openjdk-amd64/include/linux -fPIC -shared -o

```

## File: README.md
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
- and [more](docs/ProfilingModes.md).

See our [3 hours playlist](https://www.youtube.com/playlist?list=PLNCLTEx3B8h4Yo_WvKWdLvI9mj1XpTKBr)
to learn about more features.

# Download

### Stable release: [4.2.1](https://github.com/async-profiler/async-profiler/releases/tag/v4.2.1)

- Linux x64: [async-profiler-4.2.1-linux-x64.tar.gz](https://github.com/async-profiler/async-profiler/releases/download/v4.2.1/async-profiler-4.2.1-linux-x64.tar.gz)
- Linux arm64: [async-profiler-4.2.1-linux-arm64.tar.gz](https://github.com/async-profiler/async-profiler/releases/download/v4.2.1/async-profiler-4.2.1-linux-arm64.tar.gz)
- macOS arm64/x64: [async-profiler-4.2.1-macos.zip](https://github.com/async-profiler/async-profiler/releases/download/v4.2.1/async-profiler-4.2.1-macos.zip)
- Profile converters: [jfr-converter.jar](https://github.com/async-profiler/async-profiler/releases/download/v4.2.1/jfr-converter.jar)

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

## File: _GIT_INGEST.md
```
# OmniClaw Repo Plow: CIV_FETCHED_async-profiler_205444



================================================
FILE: CHANGELOG.md
================================================
# Changelog

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
 - #982: Sampl

================================================
FILE: CMakeLists.txt
================================================
cmake_minimum_required(VERSION 3.22)
project(async-profiler)

set(CMAKE_CXX_STANDARD 11)
# -fno-omit-frame-pointer -fvisibility=hidden -Wl,-z,defs -fwhole-program -momit-leaf-frame-pointer
add_library(async-profiler
        ./src/arguments.cpp
        ./src/flameGraph.cpp
        ./src/profiler.cpp
        ./src/trap.cpp
        ./src/stackWalker.cpp
        ./src/symbols_macos.cpp
        ./src/tsc.cpp
        ./src/j9Ext.cpp
        ./src/codeCache.cpp
        ./src/itimer.cpp
        ./src/wallClock.cpp
        ./src/stackFrame_x64.cpp
        ./src/j9StackTraces.cpp
        ./src/mutex.cpp
        ./src/flightRecorder.cpp
        ./src/javaApi.cpp
        ./src/j9WallClock.cpp
        ./src/stackFrame_arm.cpp
        ./src/instrument.cpp
        ./src/j9ObjectSampler.cpp
        ./src/os_linux.cpp
        ./src/lockTracer.cpp
        ./src/dictionary.cpp
        ./src/fdtransferClient_linux.cpp
        ./src/perfEvents_linux.cpp
        ./src/linearAllocator.cpp
        ./src/stackFrame_i386.cpp
        ./src/stackFrame_ppc64.cpp
        ./src/jfrMetadata.cpp
        ./src/threadFilter.cpp
        ./src/dwarf.cpp
        ./src/log.cpp
        ./src/objectSampler.cpp
        ./src/os_macos.cpp
        ./src/stackFrame_aarch64.cpp
        ./src/engine.cpp
        ./src/vmStructs.cpp
        ./src/symbols_linux.cpp
        ./src/frameName.cpp
        ./src/vmEntry.cpp
        ./src/callTraceStorage.cpp
        ./src/allocTracer.cpp
        )
target_compile_options(async-profiler PRIVATE -fno-omit-frame-pointer -fvisibility=hidden -Wl,-z,defs -fwhole-program -momit-leaf-frame-pointer -fPIC)
target_compile_definitions(async-profiler PRIVATE PROFILER_VERSION=\"0.0.0\")
target_include_directories(async-profiler PRIVATE
        ./src
        ./src/res
        ./src/helper
        /usr/lib/jvm/java-11-openjdk-amd64/include
        /usr/lib/jvm/java-11-openjdk-amd64/include/linux)

# -DPROFILER_VERSION=\"2.9.0.2\" -I/usr/lib/jvm/java-11-openjdk-amd64/include -Isrc/res -Isrc/helper -I/usr/lib/jvm/java-11-openjdk-amd64/include/linux -fPIC -shared -o


================================================
FILE: README.md
================================================
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

### Stable release: [4.2.1](https://github.com/async-profiler/async-profiler/releases/tag/v4.2.1)

- Linux x64: [async-profiler-4.2.1-linux-x64.tar.gz](https://github.com/async-profiler/async-profiler/releases/download/v4.2.1/async-profiler-4.2.1-linux-x64.tar.gz)
- Linux arm64: [async-profiler-4.2.1-linux-arm64.tar.gz](https://github.com/async-profiler/async-profiler/releases/download/v4.2.1/async-profiler-4.2.1-linux-arm64.tar.gz)
- macOS arm64/x64: [async-profiler-4.2.1-macos.zip](https://github.com/async-profiler/async-profiler/releases/download/v4.2.1/async-profiler-4.2.1-macos.zip)
- Profile converters: [jfr-converter.jar](https://github.com/async-profiler/async-profiler/releases/download/v4.2.1/jfr-converter.jar)

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


================================================
FILE: docs\AdvancedStacktraceFeatures.md
================================================
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


================================================
FILE: docs\ConverterUsage.md
================================================
# Converter Usage

async-profiler provides `jfrconv` utility to convert between different profile output formats.
`jfrconv` can be found at the same location as the `asprof` binary. Converter is also available
as a standalone Java application: [`jfr-converter.jar`](https://github.com/async-profiler/async-profiler/releases/download/v4.2.1/jfr-converter.jar).

## Supported conversions

| Source    | html | collapsed | pprof | pb.gz | heatmap | otlp |
| --------- | ---- | --------- | ----- | ----- | ------- | ---- |
| jfr       | ✅   | ✅        | ✅    | ✅    | ✅      | ✅   |
| html      | ✅   | ✅        | ❌    | ❌    | ❌      | ❌   |
| collapsed | ✅   | ✅        | ❌    | ❌    | ❌      | ❌   |

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
    --highlight REGEX  Highlight frames matching the given

================================================
FILE: docs\CpuSamplingEngines.md
================================================
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


================================================
FILE: docs\FlamegraphInterpretation.md
================================================
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


================================================
FILE: docs\GettingStarted.md
================================================
# Getting started guide

## Before profiling

As of Linux 4.6, capturing kernel call stacks using `perf_events` from a non-root
process requires setting two kernel parameters. You can set them using sysctl as follows:

```
# sysctl kernel.perf_event_paranoid=1
# sysctl kernel.kptr_restrict=0
```

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


================================================
FILE: docs\Heatmap.md
================================================
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


================================================
FILE: docs\IntegratingAsyncProfiler.md
================================================
# Integrating async-profiler

## Launching as an agent

If you need to profile some code as soon as the JVM starts up, instead of using `asprof`,
it is possible to attach async-profiler as an agent on the command line. For example:

```
$ java -agentpath:/path/to/libasyncProfiler.so=start,event=cpu,file=profile.html ...
```

Agent library is configured through the JVMTI argument interface.
The format of the arguments string is described
[in the source code](https://github.com/async-profiler/async-profiler/blob/v4.2.1/src/arguments.cpp#L39).
`asprof` actually converts command line arguments to that format.

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


================================================
FILE: docs\JfrVisualization.md
================================================
# JFR Visualization

JFR recordings produced by async-profiler can be viewed using multiple options explained below.

## Built-in converter

async-profiler provides a built-in converter `jfrconv` which can be used to convert `jfr` output
to a flame graph or one of the other supported formats. More details on the built-in converter usage
can be found [here](ConverterUsage.md).

## JMC

[JDK Mission Control](https://www.oracle.com/java/technologies/jdk-mission-control.html) (JMC)
is a popular GUI tool to analyze JFR recordings.
It has been originally developed to work in conjunction with the JDK Flight Recorder,
however, async-profiler recordings are also fully compatible with JMC.

When viewing async-profiler recordings in JMC, information on some tabs may be missing.
Developers are typically interested in the following sections:

- Java Application
  - Method Profiling
  - Memory
  - Lock Instances
- JVM Internals
  - TLAB Allocations

## IntelliJ IDEA

IntelliJ IDEA Ultimate has built-in JFR viewer that works perfectly with async-profiler recordings.
For the Community Edition, there is an open-source profiler [plugin](https://plugins.jetbrains.com/plugin/20937-java-jfr-profiler)
that allows you to profile Java applications with JFR and async-profiler as well as
open JFR files obtained outside IDE.

## JFR command line tool

JDK distributions include the `jfr` command line utility to filter, summarize and output
flight recording files into human-readable format. The
[official documentation](https://docs.oracle.com/en/java/javase/21/docs/specs/man/jfr.html)
provides complete information on how to manipulate the contents and translate it as per
developers' needs to debug performance issues with their Java applications.


================================================
FILE: docs\OutputFormats.md
================================================
# Output Formats

async-profiler currently supports the following output formats:

- `collapsed` - This is a collection of call stacks, where each line is a semicolon separated list of frames followed
  by a counter. This is used by the FlameGraph script to generate the FlameGraph visualization of the profile data.

  ```
  FileConverter.main;FileConverter.convertFile;FileConverter.saveResult 21
  FileConverter.main;FileConverter.convertFile;FileConverter.saveResult;java/io/DataOutputStream.writeInt 1
  FileConverter.main;FileConverter.convertFile;FileConverter.saveResult;java/io/DataOutputStream.writeInt;java/io/ByteArrayOutputStream.write 5
  FileConverter.main;FileConverter.convertFile;FileConverter.saveResult;java/io/DataOutputStream.writeUTF;java/io/DataOutputStream.writeUTF 12
  FileConverter.main;FileConverter.convertFile;FileConverter.saveResult;java/io/DataOutputStream.writeUTF;java/io/DataOutputStream.writeUTF;java/lang/String.length 3
  FileConverter.main;FileConverter.convertFile;FileConverter.saveResult;java/io/DataOutputStream.writeUTF;java/io/DataOutputStream.writeUTF;java/io/DataOutputStream.write 6
  start_thread;thread_native_entry;Thread::call_run;VMThread::run;VMThread::inner_execute;VMThread::evaluate_operation;VM_Operation::evaluate;VM_GenCollectForAllocation::doit;GenCollectedHeap::satisfy_failed_allocation;GenCollectedHeap::do_collection;GenCollectedHeap::collect_generation;DefNewGeneration::collect;DefNewGeneration::FastEvacuateFollowersClosure::do_void 12
  start_thread;thread_native_entry;Thread::call_run;VMThread::run;VMThread::inner_execute;VMThread::evaluate_operation;VM_Operation::evaluate;VM_GenCollectForAllocation::doit;GenCollectedHeap::satisfy_failed_allocation;GenCollectedHeap::do_collection;GenCollectedHeap::collect_generation;DefNewGeneration::collect;DefNewGeneration::FastEvacuateFollowersClosure::do_void;void ContiguousSpace::oop_since_save_marks_iterate<DefNewScanClosure> 1
  ```

- `flamegraph` - FlameGraph is a hierarchical representation of call traces of the profiled software in a color coded
  format. Read more on the [interpretation](FlamegraphInterpretation.md) of FlameGraphs.
  [![FlameGraph](/.assets/images/flamegraph.png)](https://htmlpreview.github.io/?https://github.com/async-profiler/async-profiler/blob/master/.assets/html/flamegraph.html)

- `tree` - Profile output generated in HTML format showing a tree view of resource usage beginning with the call stack
  with the highest resource usage and then showing other call stacks in descending order of resource usage. Expanding a
  parent frame follows the same hierarchical representation within that frame.
  ![Tree](/.assets/images/treeview_example.png)

- `text` - If no output format is specified with `-o` and filename has no extension provided, profiled output is
  generated in text format.

  ```
  --- Execution profile ---
  Total samples       : 733

  --- 8208 bytes (19.58%), 1 sample
  [ 0] byte[]
  [ 1] java.util.jar.Manifest$FastInputStream.<init>
  [ 2] java.util.jar.Manifest$FastInputStream.<init>
  [ 3] java.util.jar.Manifest.read
  [ 4] java.util.jar.Manifest.<init>
  [ 5] java.util.jar.Manifest.<init>
  [ 6] java.util.jar.JarFile.getManifestFromReference
  [ 7] java.util.jar.JarFile.getManifest
  [ 8] jdk.internal.loader.URLClassPath$JarLoader$2.getManifest
  [ 9] jdk.internal.loader.BuiltinClassLoader.defineClass
  [10] jdk.internal.loader.BuiltinClassLoader.findClassOnClassPathOrNull
  [11] jdk.internal.loader.BuiltinClassLoader.loadClassOrNull
  [12] jdk.internal.loader.BuiltinClassLoader.loadClass
  [13] jdk.internal.loader.ClassLoaders$AppClassLoader.loadClass
  [14] java.lang.ClassLoader.loadClass
  [15] java.lang.Class.forName0
  [16] java.lang.Class.forName
  [17] sun.launcher.LauncherHelper.loadMainClass
  [18] sun.launcher.LauncherHelper.checkAndLoadMain
  ```

- `jfr` - profile format used by the JDK Flight Recorder. The `jfr` format collects data
  about the JVM as well as the Java application running on it. async-profiler can generate output in `jfr` format
  compatible with tools capable of viewing and analyzing `jfr` files. JDK Mission Control (JMC) and Intellij IDEA are
  some of many options to visualize `jfr` files. More details [here](JfrVisualization.md).

- `otlp` - OpenTelemetry protocol format for [profiling data](https://opentelemetry.io/blog/2024/profiling).
  Experimental feature: backward-incompatible changes may happen in future releases of async-profiler.


================================================
FILE: docs\ProfilerOptions.md
================================================
# Profiler options

The below tables list the profiler options available with `asprof` and also when
[launching as an agent](IntegratingAsyncProfiler.md#launching-as-an-agent).
Some tables are output specific, which means some options are applicable to only one or more output formats but not all.

```
Usage: asprof [action] [options] [PID]
```

## Actions

The below options are `action`s for async-profiler and common for both `asprof` binary and when launching as an agent.

| Option    | Description                                                                                                                                                                                     |
| --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `start`   | Start profiling in semi-automatic mode, i.e. profiler will run until `stop` command is explicitly called.                                                                                       |
| `resume`  | Start or resume earlier profiling session that has been stopped. All the collected data remains valid. The profiling options are not preserved between sessions, and should be specified again. |
| `stop`    | Stop profiling and print the report.                                                                                                                                                            |
| `dump`    | Dump collected data without stopping profiling session.                                                                                                                                         |
| `status`  | Print profiling status: whether profiler is active and for how long.                                                                                                                            |
| `metrics` | Print profiler metrics in Prometheus format.                                                                                                                                                    |
| `list`    | Show the list of profiling events available for the target process specified with PID.                                                                                                          |

## Options applicable to any output format

| asprof               | Launch as agent    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| -------------------- | ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `-o fmt`             | `fmt`              | Specifies what information to dump when profiling ends. For various dump option details, please refer to [Dump Option Appendix](#dump-option).                                                                                                                                                                                                                                                                                                                                                                                              |
| `-d N`               | N/A                | asprof-only option designed for interactive use. It is a shortcut for running 3 actions: start, sleep for N seconds, stop. If no `start`, `resume`, `stop` or `status` option is given, the profiler will run for the specified period of time and then automatically stop.<br>Example: `asprof -d 30 <pid>`                                                                                                                                                                                                                                |
| `--timeout N`        | `timeout=N`        | The profiling duration, in seconds. The profiler will run for the specified period of time and then automatically stop.<br>Example: `java -agentpath:/path/to/libasyncProfiler.so=start,event=cpu,timeout=30,file=profile.html <application>`                                 

================================================
FILE: docs\ProfilingInContainer.md
================================================
# Profiling Java in a container

async-profiler provides the ability to profile Java processes running in a Docker or LXC
container both from within a container and from the host system.

When profiling from the host, `pid` should be the Java process ID in the host
namespace. Use `ps aux | grep java` or `docker top <container>` to find
the process ID.

async-profiler should be run from the host by a privileged user - it will
automatically switch to the proper pid/mount namespace and change
user credentials to match the target process. Also make sure that
the target container can access `libasyncProfiler.so` by the same
absolute path as on the host. Alternatively, specify `--libpath` option
to override path to `libasyncProfiler.so` in a container.

By default, Docker container restricts the access to `perf_event_open`
syscall. There are 3 alternatives to allow profiling in a container:

1. You can modify the [seccomp profile](https://docs.docker.com/engine/security/seccomp/)
   or disable it altogether with `--security-opt seccomp=unconfined` option. In
   addition, `--cap-add SYS_ADMIN` may be required.
2. You can use "fdtransfer": see the help for `--fdtransfer`.
3. Last, you may fall back to `-e ctimer` profiling mode, see [Troubleshooting](Troubleshooting.md).


================================================
FILE: docs\ProfilingModes.md
================================================
# Profiling modes

Besides CPU time, async-profiler provides various other profiling modes such as `Allocation`, `Wall Clock`, `Java Method`
and even a `Multiple Events` profiling mode.

## CPU profiling

In this mode, profiler collects stack trace samples that include **Java** methods,
**native** calls, **JVM** code and **kernel** functions.

The general approach is receiving call stacks generated by `perf_events`
and matching them up with call stacks generated by `AsyncGetCallTrace`,
in order to produce an accurate profile of both Java and native code.
Additionally, async-profiler provides a workaround to recover stack traces
in some [corner cases](https://bugs.openjdk.java.net/browse/JDK-8178287)
where `AsyncGetCallTrace` fails.

This approach has the following advantages compared to using `perf_events`
directly with a Java agent that translates addresses to Java method names:

- Does not require `-XX:+PreserveFramePointer`, which introduces
  performance overhead that can be sometimes as high as 10%.

- Does not require starting JVM with an agent for translating Java code addresses
  to method names.

- Displays interpreter frames.

- Does not produce large intermediate files (perf.data) for further processing in
  user space scripts.

If you wish to resolve frames within `libjvm`, the [debug symbols](#installing-debug-symbols) are required.

## ALLOCATION profiling

The profiler can be configured to collect call sites where the largest amount
of heap memory is allocated.

async-profiler does not use intrusive techniques like bytecode instrumentation
or expensive DTrace probes which have significant performance impact.
It also does not affect Escape Analysis or prevent from JIT optimizations
like allocation elimination. Only actual heap allocations are measured.

The profiler features TLAB-driven sampling. It relies on HotSpot-specific
callbacks to receive two kinds of notifications:

- when an object is allocated in a newly created TLAB;
- when an object is allocated on a slow path outside TLAB.

Sampling interval can be adjusted with `--alloc` option.
For example, `--alloc 500k` will take one sample after 500 KB of allocated
space on average. Prior to JDK 11, intervals less than TLAB size will not take effect.

In allocation profiling mode, the top frame of every call trace is the class
of the allocated object, and the counter is the heap pressure (the total size
of allocated TLABs or objects outside TLAB).

### Installing Debug Symbols

Prior to JDK 11, the allocation profiler required HotSpot debug symbols.
Some OpenJDK distributions (Amazon Corretto, Liberica JDK, Azul Zulu)
already have them embedded in `libjvm.so`, other OpenJDK builds typically
provide debug symbols in a separate package. For example, to install
OpenJDK debug symbols on Debian / Ubuntu, run:

```
# apt install openjdk-17-dbg
```

(replace `17` with the desired version of JDK).

On CentOS, RHEL and some other RPM-based distributions, this could be done with
[debuginfo-install](http://man7.org/linux/man-pages/man1/debuginfo-install.1.html) utility:

```
# debuginfo-install java-1.8.0-openjdk
```

On Gentoo, the `icedtea` OpenJDK package can be built with the per-package setting
`FEATURES="nostrip"` to retain symbols.

The `gdb` tool can be used to verify if debug symbols are properly installed for the `libjvm` library.
For example, on Linux:

```
$ gdb $JAVA_HOME/lib/server/libjvm.so -ex 'info address UseG1GC'
```

This command's output will either contain `Symbol "UseG1GC" is at 0xxxxx`
or `No symbol "UseG1GC" in current context`.

## Native memory leaks

The profiling mode `nativemem` records `malloc`, `realloc`, `calloc` and `free` calls
with the addresses, so that allocations can be matched with frees. This helps to focus
the profile report only on unfreed allocations, which are the likely to be a source of a memory leak.

Example:

```
asprof start -e nativemem -f app.jfr <YourApp>
# or
asprof start --nativemem N -f app.jfr <YourApp>
# or if only allocation calls are interesting, do not collect free calls:
asprof start --nativemem N --nofree -f app.jfr <YourApp>

asprof stop <YourApp>
```

Now we need to process the jfr file, to find native memory leaks:

```
# --total for bytes, default counts invocations.
jfrconv --total --nativemem --leak app.jfr app-leak.html

# No leak analysis, include all native allocations:
jfrconv --total --nativemem app.jfr app-malloc.html
```

When `--leak` option is used, the generated flame graph will show allocations without matching `free` calls.

![nativemem flamegraph](../.assets/images/nativemem_flamegraph.png)

To avoid bias towards youngest allocations not freed by the end of the profiling session,
leak profiler ignores tail allocations made in the last 10% of the profiling period.
Tail length can be altered with `--tail` option that accepts `ratio` or `percent%` as an argument.
For example, to ignore allocations in the last 2 minutes of a 10 minutes profile, use

```
jfrconv --nativemem -

================================================
FILE: docs\ProfilingNonJavaApplications.md
================================================
# Profiling Non-Java applications

The scope of profiling non-Java applications is limited to the case when profiler is controlled
programmatically from the process being profiled or with `LD_PRELOAD`. It is worth noting that
[dynamic attach](IntegratingAsyncProfiler.md#launching-as-an-agent)
which is available for Java is not supported for non-Java profiling.

## LD_PRELOAD

async-profiler can be injected into a native application through the `LD_PRELOAD` mechanism:

```
LD_PRELOAD=/path/to/libasyncProfiler.so ASPROF_COMMAND=start,event=cpu,file=profile.jfr NativeApp [args]
```

All basic functionality remains the same. Profiler can run in `cpu`, `wall`, `nativemem` and other perf_events
modes. Flame Graph and JFR output formats are supported, although JFR files will obviously lack
Java-specific events.

See [Profiling Modes](ProfilingModes.md) for more examples.

## Controlling async-profiler via the C API

Similar to the
[Java API](IntegratingAsyncProfiler.md#using-java-api),
there is a C API for using profiler inside a native application.

Header file for the API is bundled in the async-profiler release package under [`include/asprof.h`](../src/asprof.h).

To use it in a C/C++ application, include the mentioned `asprof.h`. Below is an example showing how to invoke async-profiler with the API:

```
#include "asprof.h"
#include <dlfcn.h>
#include <stdio.h>
#include <stdlib.h>

void test_output_callback(const char* buffer, size_t size) {
    fwrite(buffer, sizeof(char), size, stderr);
}

int main() {
    void* lib = dlopen("/path/to/libasyncProfiler.so", RTLD_NOW);
    if (lib == NULL) {
        printf("%s\n", dlerror());
        exit(1);
    }

    asprof_init_t asprof_init = (asprof_init_t)dlsym(lib, "asprof_init");
    asprof_execute_t asprof_execute = (asprof_execute_t)dlsym(lib, "asprof_execute");
    asprof_error_str_t asprof_error_str = (asprof_error_str_t)dlsym(lib, "asprof_error_str");

    if (asprof_init == NULL || asprof_execute == NULL || asprof_error_str == NULL) {
        printf("%s\n", dlerror());
        dlclose(lib);
        exit(1);
    }

    asprof_init();

    printf("Starting profiler\n");

    char cmd[] = "start,event=cpu,loglevel=debug,file=profile.jfr";
    asprof_error_t err = asprof_execute(cmd, test_output_callback);
    if (err != NULL) {
        fprintf(stderr, "%s\n", asprof_error_str(err));
        exit(1);
    }

    // ... some meaningful work ...

    printf("Stopping profiler\n");

    err = asprof_execute("stop", test_output_callback);
    if (err != NULL) {
        fprintf(stderr, "%s\n", asprof_error_str(err));
        exit(1);
    }

    return 0;
}
```

## Unstable APIs

These APIs are unstable and might change or be removed in the next version of async-profiler.

### Advanced Sampling

The `asprof_get_thread_local_data` function returns a pointer to async-profiler's
thread-local data structure. The structure is guaranteed to live as long as the thread.

The returned structure contains a pointer that increments every time there is a sample. This gives
native code an easy way to detect when a sample event had occurred, and to log metadata about what the
program was doing when the event happened.


================================================
FILE: docs\StackWalkingModes.md
================================================
# Stack Walking Modes

## Frame Pointer

`Frame Pointer (FP)` stack walking is a technique for collecting call stacks by tracking frame pointers in memory.
Each function call maintains a pointer to its caller's stack frame, creating a linked chain that can be traversed
to reconstruct the program's execution path. It's particularly efficient as it is very fast compared to other
stack walking methods introducing less overhead but requires code to be compiled with frame
pointers enabled (`-fno-omit-frame-pointer`).

Before async-profiler 4.2, Frame Pointer was the default stack walking mode.
Since version 4.2, the default was changed to [VM Structs](#vm-structs).

## DWARF

DWARF stack walking is a method to reconstruct call stacks using unwinding information embedded in executables
(typically in `.eh_frame` section). Unlike frame-pointer-based unwinding, it works reliably even with optimized code
where frame pointers are omitted.

DWARF unwinding requires extra memory (e.g. the lookup table for `libjvm.so` is about 2MB).
It is also slower than the traditional FP-based stack walker, but it's still fast enough for on-the-fly unwinding
due to being signal safe in async-profiler.

The feature can be enabled with the option `--cstack dwarf` (or its agent equivalent `cstack=dwarf`).

## LBR

Modern Intel CPUs can profile branch instructions, including `call`s and `ret`s, and store their source and destination
addresses (Last Branch Records) in hardware registers. Starting from Haswell, CPU can match these addresses to form a
branch stack. This branch stack will be effectively a call chain automatically collected by the hardware.

LBR stacks are not always complete or accurate, but they still appear much more helpful comparing to FP-based stack
walking, when a native library is compiled with omitted frame pointers. It works only with hardware events like
`-e cycles` (`instructions`, `cache-misses` etc.) and the maximum call chain depth is 32 (hardware limit).

The feature can be enabled with the option `--cstack lbr` (or its agent equivalent `cstack=lbr`).

## VM Structs

async-profiler can leverage JVM internal structures to replicate the logic of Java stack walking
in the profiler itself without depending on the unstable JVM API.

This mode of stack walking has been introduced in async-profiler due to issues with `AsyncCallGetTrace`.
AsyncGetCallTrace (AGCT) is a non-standard extension of HotSpot JVM to obtain Java stack traces outside safepoints.
async-profiler had been relying on AGCT heavily, and it even got its name after this function.

`AsyncGetCallTrace` being non-API, was never supported in OpenJDK well enough, it did not receive enough testing, it was
broken several times even in minor JDK updates, e.g. [JDK-8307549](https://bugs.openjdk.org/browse/JDK-8307549).

AsyncGetCallTrace is notorious for its inability to walk Java stack in different corner cases. There is a long-standing
bug [JDK-8178287](https://bugs.openjdk.org/browse/JDK-8178287) with several examples. But the worst aspect is that
AsyncGetCallTrace can crash JVM, and there is no reliable way to get around this outside the JVM.

Due to issues with AGCT from time to time, including random crashes and missing stack traces,
`vm` stack walking mode based on HotSpot VM Structs was introduced in async-profiler.
`vm` stack walker has the following advantages:

- Fully enclosed by the crash protection based on `setjmp`/`longjmp`.
- Can show all frames: Java, native and JVM stubs throughout the whole stack.
- Provides additional information on each frame, like JIT compilation type.

The feature can be enabled with the option `--cstack vm` (or its agent equivalent `cstack=vm`).
Since async-profiler 4.2, this is the default mode when running on the HotSpot JVM.

Another variant of this option: `--cstack vmx` activates an "expert" unwinding based on VM Structs.
With this option, async-profiler collects mixed stack traces that have Java and native frames interleaved.

The maximum stack depth for `vm` or `vmx` stack walking is controlled with `-j depth` option.


================================================
FILE: docs\Troubleshooting.md
================================================
# Troubleshooting

## Error Messages

### perf_event mmap failed: Operation not permitted

Profiler allocates 8 kB perf_event buffer for each thread of the target process.
The above error may appear if the total size of perf_event buffers (`8 * threads` kB)
exceeds locked memory limit. This limit is comprised of `ulimit -l` plus
the value of `kernel.perf_event_mlock_kb` sysctl multiplied by the number of CPU cores.
For example, on a 16-core machine, `ulimit -l 65536` and `kernel.perf_event_mlock_kb=516`
is enough for profiling `(65536 + 516*16) / 8 = 9224` threads.
If an application has more threads, increase one of the above limits, or native stacks
will not be collected for some threads.

A privileged process is not subject to the locked memory limit.

### Failed to change credentials to match the target process: Operation not permitted

Due to limitation of HotSpot Dynamic Attach mechanism, the profiler must be run
by exactly the same user (and group) as the owner of target JVM process.
If profiler is run by a different user, it will try to automatically change
current user and group. This will likely succeed for `root`, but not for
other users, resulting in the above error.

### Could not start attach mechanism: No such file or directory

The profiler cannot establish communication with the target JVM through UNIX domain socket.
Usually this happens in one of the following cases:

1. Attach socket `/tmp/.java_pidNNN` has been deleted. It is a common
   practice to clean `/tmp` automatically with some scheduled script.
   Configure the cleanup software to exclude `.java_pid*` files from deletion.

   - How to check: run `lsof -p PID | grep java_pid`. If it lists a socket file, but the file does not exist, then this is exactly
     the described problem.

2. JVM is started with `-XX:+DisableAttachMechanism` option.
3. `/tmp` directory of Java process is not physically the same directory
   as `/tmp` of your shell, because Java is running in a container or in
   `chroot` environment. `asprof` attempts to solve this automatically,
   but it might lack the required permissions to do so.
   - Check `strace asprof PID jcmd`
4. JVM is busy and cannot reach a safepoint. For instance,
   JVM is in the middle of long-running garbage collection.
   - How to check: run `kill -3 PID`. Healthy JVM process should print
     a thread dump and heap info in its console.

### Target JVM failed to load libasyncProfiler.so

The connection with the target JVM has been established, but JVM is unable to load profiler shared library.
Make sure the user of JVM process has permissions to access `libasyncProfiler.so` by exactly the same absolute path.
For more information see [#78](https://github.com/async-profiler/async-profiler/issues/78).

### Perf events unavailable

`perf_event_open()` syscall has failed. Typical reasons include:

1. `/proc/sys/kernel/perf_event_paranoid` is set to restricted mode (>=2).
2. seccomp disables `perf_event_open` API in a container.
3. OS runs under a hypervisor that does not virtualize performance counters.
4. perf_event_open API is not supported on this system, e.g. WSL.

<br>For permissions-related reasons (such as 1 and 2), using `--fdtransfer` while running the profiler
as a privileged user may solve the issue.

If changing the configuration is not possible, you may fall back to
`-e ctimer` profiling mode. It is similar to `cpu` mode, but does not
require perf_events support. As a drawback, there will be no kernel
stack traces.

### No AllocTracer symbols found. Are JDK debug symbols installed?

The OpenJDK debug symbols are required for allocation profiling for applications developed
with JDK prior to 11. See [Installing Debug Symbols](ProfilingModes.md#installing-debug-symbols) for more
details. If the error message persists after a successful installation of the debug symbols,
it is possible that the JDK was upgraded when installing the debug symbols.
In this case, profiling any Java process which had started prior to the installation
will continue to display this message, since the process had loaded
the older version of the JDK which lacked debug symbols.
Restarting the affected Java processes should resolve the issue.

### VMStructs unavailable. Unsupported JVM?

JVM shared library does not export `gHotSpotVMStructs*` symbols -
apparently this is not a HotSpot JVM. Sometimes the same message
can be also caused by an incorrectly built JDK
(see [#218](https://github.com/async-profiler/async-profiler/issues/218)).
In these cases installing JDK debug symbols may solve the problem.

### Could not parse symbols from <libname.so>

Async-profiler was unable to parse non-Java function names because of
the corrupted contents in `/proc/[pid]/maps`. The problem is known to
occur in a container when running Ubuntu with Linux kernel 5.x.
This is the OS bug, see <https://bugs.launchpad.net/ubuntu/+source/linux/+bug/1843018>.

### Could not open output file

Output file is written by the target JVM proc

================================================
FILE: src\api\one\profiler\Agent.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package one.profiler;

import javax.management.ObjectName;
import java.lang.management.ManagementFactory;

public class Agent {

    public static void premain(String args) throws Exception {
        agentmain(args);
    }

    public static void agentmain(String args) throws Exception {
        AsyncProfiler profiler = AsyncProfiler.getInstance();
        ManagementFactory.getPlatformMBeanServer().registerMBean(
                profiler,
                new ObjectName(AsyncProfilerMXBean.OBJECT_NAME));
        if (args != null && !args.isEmpty()) {
            profiler.execute(args);
        }
    }
}


================================================
FILE: src\api\one\profiler\AsyncProfiler.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package one.profiler;

import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;

/**
 * Java API for in-process profiling. Serves as a wrapper around
 * async-profiler native library. This class is a singleton.
 * The first call to {@link #getInstance()} initiates loading of
 * libasyncProfiler.so.
 */
public class AsyncProfiler implements AsyncProfilerMXBean {
    private static AsyncProfiler instance;

    private AsyncProfiler() {
    }

    public static AsyncProfiler getInstance() {
        return getInstance(null);
    }

    public static synchronized AsyncProfiler getInstance(String libPath) {
        if (instance != null) {
            return instance;
        }

        AsyncProfiler profiler = new AsyncProfiler();
        if (libPath != null) {
            System.load(libPath);
        } else {
            try {
                // No need to load library, if it has been preloaded with -agentpath
                profiler.getVersion();
            } catch (UnsatisfiedLinkError e) {
                String libraryPath = System.getProperty("one.profiler.libraryPath");
                if (libraryPath != null && !libraryPath.isEmpty()) {
                    System.load(new File(libraryPath).getAbsolutePath());
                } else {
                    File file = extractEmbeddedLib();
                    if (file != null) {
                        try {
                            System.load(file.getAbsolutePath());
                        } finally {
                            file.delete();
                        }
                    } else {
                        System.loadLibrary("asyncProfiler");
                    }
                }

            }
        }

        instance = profiler;
        return profiler;
    }

    private static File extractEmbeddedLib() {
        String resourceName = "/" + getPlatformTag() + "/libasyncProfiler.so";
        InputStream in = AsyncProfiler.class.getResourceAsStream(resourceName);
        if (in == null) {
            return null;
        }

        try {
            String extractPath = System.getProperty("one.profiler.extractPath");
            File file = File.createTempFile("libasyncProfiler-", ".so",
                    extractPath == null || extractPath.isEmpty() ? null : new File(extractPath));
            try (FileOutputStream out = new FileOutputStream(file)) {
                byte[] buf = new byte[32000];
                for (int bytes; (bytes = in.read(buf)) >= 0; ) {
                    out.write(buf, 0, bytes);
                }
            }
            return file;
        } catch (IOException e) {
            throw new IllegalStateException(e);
        } finally {
            try {
                in.close();
            } catch (IOException e) {
                // ignore
            }
        }
    }

    private static String getPlatformTag() {
        String os = System.getProperty("os.name").toLowerCase();
        String arch = System.getProperty("os.arch").toLowerCase();
        if (os.contains("linux")) {
            if (arch.equals("amd64") || arch.equals("x86_64") || arch.contains("x64")) {
                return "linux-x64";
            } else if (arch.equals("aarch64") || arch.contains("arm64")) {
                return "linux-arm64";
            } else if (arch.equals("aarch32") || arch.contains("arm")) {
                return "linux-arm32";
            } else if (arch.contains("86")) {
                return "linux-x86";
            } else if (arch.contains("ppc64")) {
                return "linux-ppc64le";
            }
        } else if (os.contains("mac")) {
            return "macos";
        }
        throw new UnsupportedOperationException("Unsupported platform: " + os + "-" + arch);
    }

    /**
     * Start profiling
     *
     * @param event    Profiling event, see {@link Events}
     * @param interval Sampling interval, e.g. nanoseconds for Events.CPU
     * @throws IllegalStateException If profiler is already running
     */
    @Override
    public void start(String event, long interval) throws IllegalStateException {
        if (event == null) {
            throw new NullPointerException();
        }
        start0(event, interval, true);
    }

    /**
     * Start or resume profiling without resetting collected data.
     * Note that event and interval may change since the previous profiling session.
     *
     * @param event    Profiling event, see {@link Events}
     * @param interval Sampling interval, e.g. nanoseconds for Events.CPU
     * @throws IllegalStateException If profiler is already running
     */
    @Override
    public void resume(String event, long interval) throws IllegalStateException {
        if (event == null) {
            throw new NullPointerException();
        }
        start0(event, interval, false);
    }

    /**
     * Stop profi

================================================
FILE: src\api\one\profiler\AsyncProfilerMXBean.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package one.profiler;

/**
 * AsyncProfiler interface for JMX server.
 * How to register AsyncProfiler MBean:
 *
 * <pre>{@code
 *     ManagementFactory.getPlatformMBeanServer().registerMBean(
 *             AsyncProfiler.getInstance(),
 *             new ObjectName("one.profiler:type=AsyncProfiler")
 *     );
 * }</pre>
 */
public interface AsyncProfilerMXBean {
    String OBJECT_NAME = "one.profiler:type=AsyncProfiler";

    void start(String event, long interval) throws IllegalStateException;
    void resume(String event, long interval) throws IllegalStateException;
    void stop() throws IllegalStateException;

    long getSamples();
    String getVersion();

    String execute(String command) throws IllegalArgumentException, IllegalStateException, java.io.IOException;

    String dumpCollapsed(Counter counter);
    String dumpTraces(int maxTraces);
    String dumpFlat(int maxMethods);
    byte[] dumpOtlp();
}


================================================
FILE: src\api\one\profiler\Counter.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package one.profiler;

/**
 * Which metrics to use when generating profile in collapsed stack traces format.
 */
public enum Counter {
    SAMPLES,
    TOTAL
}


================================================
FILE: src\api\one\profiler\Events.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package one.profiler;

/**
 * Predefined event names to use in {@link AsyncProfiler#start(String, long)}
 */
public class Events {
    public static final String CPU    = "cpu";
    public static final String ALLOC  = "alloc";
    public static final String LOCK   = "lock";
    public static final String WALL   = "wall";
    public static final String CTIMER = "ctimer";
    public static final String ITIMER = "itimer";
}


================================================
FILE: src\converter\Main.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

import one.convert.*;

import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;

public class Main {

    public static void main(String[] argv) throws Exception {
        Arguments args = new Arguments(argv);
        if (args.help || args.files.isEmpty()) {
            usage();
            return;
        }

        if (args.files.size() == 1) {
            args.files.add(".");
        }

        int fileCount = args.files.size() - 1;
        String lastFile = args.files.get(fileCount);
        boolean isDirectory = new File(lastFile).isDirectory();

        if (args.output == null) {
            int ext;
            if (!isDirectory && (ext = lastFile.lastIndexOf('.')) > 0) {
                args.output = lastFile.substring(ext + 1);
            } else {
                args.output = "html";
            }
        }

        for (int i = 0; i < fileCount; i++) {
            String input = args.files.get(i);
            String output = isDirectory ? new File(lastFile, replaceExt(input, args.output)).getPath() : lastFile;

            System.out.print("Converting " + getFileName(input) + " -> " + getFileName(output) + " ");
            System.out.flush();

            long startTime = System.nanoTime();
            convert(input, output, args);
            long endTime = System.nanoTime();

            System.out.print("# " + (endTime - startTime) / 1000000 / 1000.0 + " s\n");
        }
    }

    public static void convert(String input, String output, Arguments args) throws IOException {
        if (isJfr(input)) {
            if ("html".equals(args.output) || "collapsed".equals(args.output)) {
                JfrToFlame.convert(input, output, args);
            } else if ("pprof".equals(args.output) || "pb".equals(args.output) || args.output.endsWith("gz")) {
                JfrToPprof.convert(input, output, args);
            } else if ("heatmap".equals(args.output)) {
                JfrToHeatmap.convert(input, output, args);
            } else if ("otlp".equals(args.output)) {
                JfrToOtlp.convert(input, output, args);
            } else {
                throw new IllegalArgumentException("Unrecognized output format: " + args.output);
            }
        } else {
            FlameGraph.convert(input, output, args);
        }
    }

    public static FlameGraph parseFlameGraph(String input, Arguments args) throws IOException {
        if (isJfr(input)) {
            return JfrToFlame.parse(input, args);
        } else {
            return FlameGraph.parse(input, args);
        }
    }

    private static String getFileName(String fileName) {
        return fileName.substring(fileName.lastIndexOf(File.separatorChar) + 1);
    }

    private static String replaceExt(String fileName, String output) {
        String ext = "heatmap".equals(output) ? "html" : output;
        int slash = fileName.lastIndexOf(File.separatorChar);
        int dot = fileName.lastIndexOf('.');
        return dot > slash ? fileName.substring(slash + 1, dot + 1) + ext : fileName.substring(slash + 1) + '.' + ext;
    }

    private static boolean isJfr(String fileName) throws IOException {
        if (fileName.endsWith(".jfr")) {
            return true;
        } else if (fileName.endsWith(".collapsed") || fileName.endsWith(".txt") || fileName.endsWith(".csv")) {
            return false;
        }
        byte[] buf = new byte[4];
        try (FileInputStream fis = new FileInputStream(fileName)) {
            return fis.read(buf) == 4 && buf[0] == 'F' && buf[1] == 'L' && buf[2] == 'R' && buf[3] == 0;
        }
    }

    private static void usage() {
        System.out.print("Usage: jfrconv [options] <input> [<input>...] <output>\n" +
                "\n" +
                "Conversion options:\n" +
                "  -o --output FORMAT    Output format: html, collapsed, pprof, pb.gz, heatmap, otlp\n" +
                "  -I --include REGEX    Include only stacks with the specified frames\n" +
                "  -X --exclude REGEX    Exclude stacks with the specified frames\n" +
                "\n" +
                "JFR options:\n" +
                "     --cpu              CPU profile (ExecutionSample)\n" +
                "     --cpu-time         CPU profile (CPUTimeSample)\n" +
                "     --wall             Wall clock profile\n" +
                "     --alloc            Allocation profile\n" +
                "     --live             Live object profile\n" +
                "     --nativemem        malloc profile\n" +
                "     --leak             Only include memory leaks in nativemem\n" +
                "     --tail RATIO       Ignore tail allocations for leak profiling (10% by default)\n" +
                "     --lock             Lock contention profile\n" +
                "     --nativelock       Native (pthread) lock contention profile\n" +
                "     --trace    

================================================
FILE: src\converter\one\convert\Arguments.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package one.convert;

import java.lang.reflect.Field;
import java.lang.reflect.Modifier;
import java.util.*;
import java.util.regex.Pattern;

public class Arguments {
    public String title;
    public String highlight;
    public String output;
    public String state;
    public Pattern include;
    public Pattern exclude;
    public double minwidth;
    public double grain;
    public double tail = 0.1;
    public int skip;
    public boolean help;
    public boolean reverse;
    public boolean inverted;
    public boolean cpu;
    public boolean cpuTime;
    public boolean wall;
    public boolean alloc;
    public boolean nativemem;
    public boolean nativelock;
    public boolean leak;
    public boolean live;
    public boolean lock;
    public boolean trace;
    public boolean threads;
    public boolean classify;
    public boolean total;
    public boolean lines;
    public boolean bci;
    public boolean simple;
    public boolean norm;
    public boolean dot;
    public long from;
    public long to;
    public long latency = -1;
    public final List<String> files = new ArrayList<>();

    public Arguments(String... args) {
        for (int i = 0; i < args.length; i++) {
            String arg = args[i];
            String fieldName;
            if (arg.startsWith("--")) {
                fieldName = toCamelCase(arg.substring(2));
            } else if (arg.startsWith("-") && arg.length() == 2) {
                fieldName = alias(arg.charAt(1));
            } else {
                files.add(arg);
                continue;
            }

            try {
                Field f = Arguments.class.getDeclaredField(fieldName);
                if ((f.getModifiers() & (Modifier.PRIVATE | Modifier.STATIC | Modifier.FINAL)) != 0) {
                    throw new IllegalArgumentException(arg);
                }

                Class<?> type = f.getType();
                if (type == String.class) {
                    f.set(this, args[++i]);
                } else if (type == boolean.class) {
                    f.setBoolean(this, true);
                } else if (type == int.class) {
                    f.setInt(this, Integer.parseInt(args[++i]));
                } else if (type == double.class) {
                    f.setDouble(this, parseRatio(args[++i]));
                } else if (type == long.class) {
                    f.setLong(this, parseTimestamp(args[++i]));
                } else if (type == Pattern.class) {
                    f.set(this, Pattern.compile(args[++i]));
                }
            } catch (NoSuchFieldException | IllegalAccessException e) {
                throw new IllegalArgumentException(arg);
            }
        }
    }

    private static String alias(char c) {
        switch (c) {
            case 'h':
                return "help";
            case 'o':
                return "output";
            case 'r':
                return "reverse";
            case 'i':
                return "inverted";
            case 'I':
                return "include";
            case 'X':
                return "exclude";
            case 't':
                return "threads";
            case 's':
                return "state";
            default:
                return String.valueOf(c);
        }
    }

    private static String toCamelCase(String name) {
        for (int i; (i = name.lastIndexOf('-', name.length() - 2)) >= 0; ) {
            name = name.substring(0, i) + Character.toUpperCase(name.charAt(i + 1)) + name.substring(i + 2);
        }
        return name;
    }

    // Absolute floating point value or percentage followed by %
    private static double parseRatio(String value) {
        if (value.endsWith("%")) {
            return Double.parseDouble(value.substring(0, value.length() - 1)) / 100;
        }
        return Double.parseDouble(value);
    }

    // Milliseconds or HH:mm:ss.S or yyyy-MM-dd'T'HH:mm:ss.S
    private static long parseTimestamp(String time) {
        if (time.indexOf(':') < 0) {
            return Long.parseLong(time);
        }

        GregorianCalendar cal = new GregorianCalendar();
        StringTokenizer st = new StringTokenizer(time, "-:.T");

        if (time.indexOf('T') > 0) {
            cal.set(Calendar.YEAR, Integer.parseInt(st.nextToken()));
            cal.set(Calendar.MONTH, Integer.parseInt(st.nextToken()) - 1);
            cal.set(Calendar.DAY_OF_MONTH, Integer.parseInt(st.nextToken()));
        }
        cal.set(Calendar.HOUR_OF_DAY, st.hasMoreTokens() ? Integer.parseInt(st.nextToken()) : 0);
        cal.set(Calendar.MINUTE, st.hasMoreTokens() ? Integer.parseInt(st.nextToken()) : 0);
        cal.set(Calendar.SECOND, st.hasMoreTokens() ? Integer.parseInt(st.nextToken()) : 0);
        cal.set(Calendar.MILLISECOND, st.hasMoreTokens() ? Integer.parseInt(st.nextToken()) : 0);

        return cal.getTimeInMillis();
    }
}


================================================
FILE: src\converter\one\convert\BidirectionalIndex.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package one.convert;

import java.util.ArrayList;

public class BidirectionalIndex<T> extends Index<T> {
    private final ArrayList<T> reverseIndex;

    public BidirectionalIndex(Class<T> cls, T empty) {
        this(cls, empty, 256);
    }

    public BidirectionalIndex(Class<T> cls, T empty, int initialCapacity) {
        super(cls, empty, initialCapacity);
        this.reverseIndex = new ArrayList<>(initialCapacity);
        this.reverseIndex.add(empty);
    }

    @Override
    public int index(T key) {
        assert super.size() == reverseIndex.size();
        int idx = super.index(key);
        if (idx < reverseIndex.size()) {
            // Key already exists
            return idx;
        }
        assert idx == reverseIndex.size();
        reverseIndex.add(key);
        return idx;
    }

    public T getKey(int idx) {
        return reverseIndex.get(idx);
    }
}


================================================
FILE: src\converter\one\convert\CallStack.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package one.convert;

import java.util.Arrays;

public class CallStack {
    String[] names = new String[16];
    byte[] types = new byte[16];
    int size;

    public void push(String name, byte type) {
        if (size >= names.length) {
            names = Arrays.copyOf(names, size * 2);
            types = Arrays.copyOf(types, size * 2);
        }
        names[size] = name;
        types[size] = type;
        size++;
    }

    public void pop() {
        size--;
    }

    public void clear() {
        size = 0;
    }
}


================================================
FILE: src\converter\one\convert\Classifier.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package one.convert;

import one.jfr.StackTrace;

import static one.convert.Frame.*;

abstract class Classifier {

    enum Category {
        GC("[gc]", TYPE_CPP),
        JIT("[jit]", TYPE_CPP),
        VM("[vm]", TYPE_CPP),
        VTABLE_STUBS("[vtable_stubs]", TYPE_NATIVE),
        NATIVE("[native]", TYPE_NATIVE),
        INTERPRETER("[Interpreter]", TYPE_NATIVE),
        C1_COMP("[c1_comp]", TYPE_C1_COMPILED),
        C2_COMP("[c2_comp]", TYPE_INLINED),
        ADAPTER("[c2i_adapter]", TYPE_INLINED),
        CLASS_INIT("[class_init]", TYPE_CPP),
        CLASS_LOAD("[class_load]", TYPE_CPP),
        CLASS_RESOLVE("[class_resolve]", TYPE_CPP),
        CLASS_VERIFY("[class_verify]", TYPE_CPP),
        LAMBDA_INIT("[lambda_init]", TYPE_CPP);

        final String title;
        final byte type;

        Category(String title, byte type) {
            this.title = title;
            this.type = type;
        }
    }

    public Category getCategory(StackTrace stackTrace) {
        long[] methods = stackTrace.methods;
        byte[] types = stackTrace.types;

        Category category;
        if ((category = detectGcJit(methods, types)) == null &&
                (category = detectClassLoading(methods, types)) == null) {
            category = detectOther(methods, types);
        }
        return category;
    }

    private Category detectGcJit(long[] methods, byte[] types) {
        boolean vmThread = false;
        for (int i = types.length; --i >= 0; ) {
            if (types[i] == TYPE_CPP) {
                switch (getMethodName(methods[i], types[i])) {
                    case "CompileBroker::compiler_thread_loop":
                        return Category.JIT;
                    case "GCTaskThread::run":
                    case "WorkerThread::run":
                        return Category.GC;
                    case "java_start":
                    case "thread_native_entry":
                        vmThread = true;
                        break;
                }
            } else if (types[i] != TYPE_NATIVE) {
                break;
            }
        }
        return vmThread ? Category.VM : null;
    }

    private Category detectClassLoading(long[] methods, byte[] types) {
        for (int i = 0; i < methods.length; i++) {
            String methodName = getMethodName(methods[i], types[i]);
            if (methodName.equals("Verifier::verify")) {
                return Category.CLASS_VERIFY;
            } else if (methodName.startsWith("InstanceKlass::initialize")) {
                return Category.CLASS_INIT;
            } else if (methodName.startsWith("LinkResolver::") ||
                    methodName.startsWith("InterpreterRuntime::resolve") ||
                    methodName.startsWith("SystemDictionary::resolve")) {
                return Category.CLASS_RESOLVE;
            } else if (methodName.endsWith("ClassLoader.loadClass")) {
                return Category.CLASS_LOAD;
            } else if (methodName.endsWith("LambdaMetafactory.metafactory") ||
                    methodName.endsWith("LambdaMetafactory.altMetafactory")) {
                return Category.LAMBDA_INIT;
            } else if (methodName.endsWith("table stub")) {
                return Category.VTABLE_STUBS;
            } else if (methodName.equals("Interpreter")) {
                return Category.INTERPRETER;
            } else if (methodName.startsWith("I2C/C2I")) {
                return i + 1 < types.length && types[i + 1] == TYPE_INTERPRETED ? Category.INTERPRETER : Category.ADAPTER;
            }
        }
        return null;
    }

    private Category detectOther(long[] methods, byte[] types) {
        boolean inJava = true;
        for (int i = 0; i < types.length; i++) {
            switch (types[i]) {
                case TYPE_INTERPRETED:
                    return inJava ? Category.INTERPRETER : Category.NATIVE;
                case TYPE_JIT_COMPILED:
                    return inJava ? Category.C2_COMP : Category.NATIVE;
                case TYPE_INLINED:
                    inJava = true;
                    break;
                case TYPE_NATIVE: {
                    String methodName = getMethodName(methods[i], types[i]);
                    if (methodName.startsWith("JVM_") || methodName.startsWith("Unsafe_") ||
                            methodName.startsWith("MHN_") || methodName.startsWith("jni_")) {
                        return Category.VM;
                    }
                    switch (methodName) {
                        case "call_stub":
                        case "deoptimization":
                        case "unknown_Java":
                        case "not_walkable_Java":
                        case "InlineCacheBuffer":
                            return Category.VM;
                    }
                    if (methodName.endsWith("_arraycopy") || methodName.contains("pthread_cond")) {


================================================
FILE: src\converter\one\convert\FlameGraph.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package one.convert;

import java.io.*;
import java.nio.charset.StandardCharsets;
import java.util.Arrays;
import java.util.Comparator;
import java.util.StringTokenizer;
import java.util.regex.Pattern;

import static one.convert.Frame.*;
import static one.convert.ResourceProcessor.*;

public class FlameGraph implements Comparator<Frame> {
    private static final Frame[] EMPTY_FRAME_ARRAY = {};
    private static final String[] FRAME_SUFFIX = {"_[0]", "_[j]", "_[i]", "", "", "_[k]", "_[1]"};
    private static final byte HAS_SUFFIX = (byte) 0x80;
    private static final int FLUSH_THRESHOLD = 15000;
    private static final Pattern TID_FRAME_PATTERN = Pattern.compile("\\[(.* )?tid=\\d+]");

    private final Arguments args;
    private final Index<String> cpool = new Index<>(String.class, "");
    private final Frame root = new Frame(0, TYPE_NATIVE);
    private final StringBuilder outbuf = new StringBuilder(FLUSH_THRESHOLD + 1000);

    private String title = "Flame Graph";
    private int[] order;
    private int depth;
    private int lastLevel;
    private long lastX;
    private long lastTotal;
    private long mintotal;

    public FlameGraph(Arguments args) {
        this.args = args;
    }

    public void parseCollapsed(Reader in) throws IOException {
        CallStack stack = new CallStack();

        try (BufferedReader br = new BufferedReader(in)) {
            for (String line; (line = br.readLine()) != null; ) {
                int space = line.lastIndexOf(' ');
                if (space <= 0) continue;

                long ticks = Long.parseLong(line.substring(space + 1));

                for (int from = 0, to; from < space; from = to + 1) {
                    if ((to = line.indexOf(';', from)) < 0) to = space;
                    String name = line.substring(from, to);
                    byte type = detectType(name);
                    if ((type & HAS_SUFFIX) != 0) {
                        name = name.substring(0, name.length() - 4);
                        type ^= HAS_SUFFIX;
                    }
                    stack.push(name, type);
                }

                addSample(stack, ticks);
                stack.clear();
            }
        }
    }

    public void parseHtml(Reader in) throws IOException {
        Frame[] levels = new Frame[128];
        int level = 0;
        long total = 0;
        boolean needRebuild = args.reverse || args.include != null || args.exclude != null;

        try (BufferedReader br = new BufferedReader(in)) {
            for (String line; !(line = br.readLine()).startsWith("const cpool"); ) {
                if (line.startsWith("<h1")) {
                    title = line.substring(line.indexOf('>') + 1, line.lastIndexOf("</h1>"));
                }
            }
            br.readLine();

            String s = "";
            for (String line; (line = br.readLine()).startsWith("'"); ) {
                String packed = unescape(line.substring(1, line.lastIndexOf('\'')));
                s = s.substring(0, packed.charAt(0) - ' ').concat(packed.substring(1));
                cpool.put(s, cpool.size());
            }

            while (!br.readLine().isEmpty()) ;

            for (String line; !(line = br.readLine()).isEmpty(); ) {
                StringTokenizer st = new StringTokenizer(line.substring(2, line.length() - 1), ",");
                int nameAndType = Integer.parseInt(st.nextToken());

                char func = line.charAt(0);
                if (func == 'f') {
                    level = Integer.parseInt(st.nextToken());
                    st.nextToken();
                } else if (func == 'u') {
                    level++;
                } else if (func != 'n') {
                    throw new IllegalStateException("Unexpected line: " + line);
                }

                if (st.hasMoreTokens()) {
                    total = Long.parseLong(st.nextToken());
                }

                int titleIndex = nameAndType >>> 3;
                byte type = (byte) (nameAndType & 7);
                if (st.hasMoreTokens() && (type <= TYPE_INLINED || type >= TYPE_C1_COMPILED)) {
                    type = TYPE_JIT_COMPILED;
                }

                Frame f = level > 0 || needRebuild ? new Frame(titleIndex, type) : root;
                f.self = f.total = total;
                if (st.hasMoreTokens()) f.inlined = Long.parseLong(st.nextToken());
                if (st.hasMoreTokens()) f.c1 = Long.parseLong(st.nextToken());
                if (st.hasMoreTokens()) f.interpreted = Long.parseLong(st.nextToken());

                if (level > 0) {
                    Frame parent = levels[level - 1];
                    parent.put(f.key, f);
                    parent.self -= total;
                    depth = Math.max(depth, level);
                }
                if (level >= levels.length) {
                    levels = Arrays.copy

================================================
FILE: src\converter\one\convert\Frame.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package one.convert;

import java.util.HashMap;

public class Frame extends HashMap<Integer, Frame> {
    public static final byte TYPE_INTERPRETED = 0;
    public static final byte TYPE_JIT_COMPILED = 1;
    public static final byte TYPE_INLINED = 2;
    public static final byte TYPE_NATIVE = 3;
    public static final byte TYPE_CPP = 4;
    public static final byte TYPE_KERNEL = 5;
    public static final byte TYPE_C1_COMPILED = 6;

    private static final int TYPE_SHIFT = 28;

    final int key;
    long total;
    long self;
    long inlined, c1, interpreted;

    private Frame(int key) {
        this.key = key;
    }

    Frame(int titleIndex, byte type) {
        this(titleIndex | type << TYPE_SHIFT);
    }

    Frame getChild(int titleIndex, byte type) {
        return super.computeIfAbsent(titleIndex | type << TYPE_SHIFT, Frame::new);
    }

    int getTitleIndex() {
        return key & ((1 << TYPE_SHIFT) - 1);
    }

    byte getType() {
        if (inlined * 3 >= total) {
            return TYPE_INLINED;
        } else if (c1 * 2 >= total) {
            return TYPE_C1_COMPILED;
        } else if (interpreted * 2 >= total) {
            return TYPE_INTERPRETED;
        } else {
            return (byte) (key >>> TYPE_SHIFT);
        }
    }

    int depth(long cutoff) {
        int depth = 0;
        if (size() > 0) {
            for (Frame child : values()) {
                if (child.total >= cutoff) {
                    depth = Math.max(depth, child.depth(cutoff));
                }
            }
        }
        return depth + 1;
    }
}


================================================
FILE: src\converter\one\convert\Index.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package one.convert;

import java.lang.reflect.Array;
import java.util.HashMap;

/**
 * Container which records the index of appearance of the value it holds.
 * <p>
 * Allows retrieving the index of a given object in constant time, as well as
 * an ordered list of all values seen.
 * <p>
 * The object at index 0 is always the empty object.
 *
 * @param <T> type of the objects held in the container.
 */
public class Index<T> extends HashMap<T, Integer> {
    private final Class<T> cls;

    public Index(Class<T> cls, T empty) {
        this(cls, empty, 256);
    }

    public Index(Class<T> cls, T empty, int initialCapacity) {
        super(initialCapacity);
        this.cls = cls;
        super.put(empty, 0);
    }

    public int index(T key) {
        Integer index = super.get(key);
        if (index != null) {
            return index;
        } else {
            int newIndex = super.size();
            super.put(key, newIndex);
            return newIndex;
        }
    }

    @SuppressWarnings("unchecked")
    public T[] keys() {
        T[] result = (T[]) Array.newInstance(cls, size());
        for (Entry<T, Integer> entry : entrySet()) {
            result[entry.getValue()] = entry.getKey();
        }
        return result;
    }
}


================================================
FILE: src\converter\one\convert\JfrConverter.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package one.convert;

import one.jfr.*;
import one.jfr.event.*;

import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.util.BitSet;
import java.util.Map;
import java.util.regex.Pattern;

import static one.convert.Frame.*;

public abstract class JfrConverter extends Classifier {
    protected final JfrReader jfr;
    protected final Arguments args;
    protected final EventCollector collector;
    protected Dictionary<String> methodNames;

    public JfrConverter(JfrReader jfr, Arguments args) {
        this.jfr = jfr;
        this.args = args;

        EventCollector collector = createCollector(args);
        this.collector = args.nativemem && args.leak ? new MallocLeakAggregator(collector, args.tail) : collector;
    }

    public void convert() throws IOException {
        TimeIntervals timeIntervals = readLatencyTimeIntervals();

        jfr.stopAtNewChunk = true;
        while (jfr.hasMoreChunks()) {
            // Reset method dictionary, since new chunk may have different IDs
            methodNames = new Dictionary<>();

            collector.beforeChunk();
            collectEvents(timeIntervals);
            collector.afterChunk();

            convertChunk();
        }

        if (collector.finish()) {
            convertChunk();
        }
    }

    protected final TimeIntervals readLatencyTimeIntervals() throws IOException {
        if (args.latency < 0) return null;

        TimeIntervals.Builder intervalsBuilder = new TimeIntervals.Builder();
        boolean foundMethodTrace = false; // We'll throw an exception if none is found

        jfr.stopAtNewChunk = true;
        while (jfr.hasMoreChunks()) {
            long minLatencyTicks = args.latency * jfr.ticksPerSec / 1000;
            MethodTrace event;
            while ((event = jfr.readEvent(MethodTrace.class)) != null) {
                foundMethodTrace = true;
                if (event.duration >= minLatencyTicks) {
                    intervalsBuilder.add(jfr.eventTimeToNanos(event.time), jfr.eventTimeToNanos(event.time + event.duration));
                }
            }
        }
        jfr.rewind();

        if (!foundMethodTrace) {
            throw new RuntimeException("No jdk.MethodTrace events found");
        }
        return intervalsBuilder.build();
    }

    protected EventCollector createCollector(Arguments args) {
        return new EventAggregator(args.threads, args.grain);
    }

    protected void collectEvents(TimeIntervals timeIntervals) throws IOException {
        // args.nativemem ? MallocEvent.class should always be first for the leak detection feature
        Class<? extends Event> eventClass = args.nativemem ? MallocEvent.class
                : args.nativelock ? NativeLockEvent.class
                : args.live ? LiveObject.class
                : args.alloc ? AllocationSample.class
                : args.lock ? ContendedLock.class
                : args.trace ? MethodTrace.class
                : ExecutionSample.class;

        BitSet threadStates = null;
        if (args.state != null) {
            threadStates = new BitSet();
            for (String state : args.state.toUpperCase().split(",")) {
                threadStates.set(toThreadState(state));
            }
        } else if (args.cpu) {
            threadStates = getThreadStates(true);
        } else if (args.wall) {
            threadStates = getThreadStates(false);
        } else if (args.cpuTime) {
            threadStates = new BitSet();
            threadStates.set(ExecutionSample.CPU_TIME_SAMPLE);
        }

        long startTicks = args.from != 0 ? toTicks(args.from) : Long.MIN_VALUE;
        long endTicks = args.to != 0 ? toTicks(args.to) : Long.MAX_VALUE;

        for (Event event; (event = jfr.readEvent(eventClass)) != null; ) {
            if (event.time >= startTicks && event.time <= endTicks) {
                if (threadStates == null || threadStates.get(((ExecutionSample) event).threadState)) {
                    if (timeIntervals == null || timeIntervals.contains(jfr.eventTimeToNanos(event.time))) {
                        collector.collect(event);
                    }
                }
            }
        }
    }

    protected void convertChunk() {
        // To be overridden in subclasses
    }

    protected boolean excludeStack(int stackId, int threadId, long classId) {
        Pattern include = args.include;
        Pattern exclude = args.exclude;
        if (include == null && exclude == null) {
            return false;
        }

        if (args.threads) {
            String threadName = getThreadName(threadId);
            if (exclude != null && exclude.matcher(threadName).matches()) {
                return true;
            }
            if (include != null && include.matcher(threadName).matches()) {
                if (exclude == null) return false;
                include = null;
            }
        

================================================
FILE: src\converter\one\convert\JfrToFlame.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package one.convert;

import one.jfr.JfrReader;
import one.jfr.StackTrace;
import one.jfr.event.AllocationSample;
import one.jfr.event.Event;

import java.io.IOException;
import java.io.OutputStream;
import java.io.PrintStream;

import static one.convert.Frame.*;

/**
 * Converts .jfr output to HTML Flame Graph.
 */
public class JfrToFlame extends JfrConverter {
    private final FlameGraph fg;

    public JfrToFlame(JfrReader jfr, Arguments args) {
        super(jfr, args);
        this.fg = new FlameGraph(args);
    }

    @Override
    protected void convertChunk() {
        collector.forEach(new AggregatedEventVisitor() {
            final CallStack stack = new CallStack();

            @Override
            public void visit(Event event, long value) {
                StackTrace stackTrace = jfr.stackTraces.get(event.stackTraceId);
                if (stackTrace != null) {
                    Arguments args = JfrToFlame.this.args;
                    long[] methods = stackTrace.methods;
                    byte[] types = stackTrace.types;
                    int[] locations = stackTrace.locations;

                    if (args.threads) {
                        stack.push(getThreadName(event.tid), TYPE_NATIVE);
                    }
                    if (args.classify) {
                        Classifier.Category category = getCategory(stackTrace);
                        stack.push(category.title, category.type);
                    }
                    for (int i = methods.length; --i >= 0; ) {
                        String methodName = getMethodName(methods[i], types[i]);
                        int location;
                        if (args.lines && (location = locations[i] >>> 16) != 0) {
                            methodName += ":" + location;
                        } else if (args.bci && (location = locations[i] & 0xffff) != 0) {
                            methodName += "@" + location;
                        }
                        stack.push(methodName, types[i]);
                    }
                    long classId = event.classId();
                    if (classId != 0) {
                        stack.push(getClassName(classId), (event instanceof AllocationSample)
                                && ((AllocationSample) event).tlabSize == 0 ? TYPE_KERNEL : TYPE_INLINED);
                    }

                    fg.addSample(stack, value);
                    stack.clear();
                }
            }
        });
    }

    public void dump(OutputStream out) throws IOException {
        fg.dump(out);
    }

    public static FlameGraph parse(String input, Arguments args) throws IOException {
        try (JfrReader jfr = new JfrReader(input)) {
            JfrToFlame converter = new JfrToFlame(jfr, args);
            converter.convert();
            return converter.fg;
        }
    }

    public static void convert(String input, String output, Arguments args) throws IOException {
        FlameGraph fg = parse(input, args);
        try (PrintStream out = new PrintStream(output, "UTF-8")) {
            fg.dump(out);
        }
    }
}


================================================
FILE: src\converter\one\convert\JfrToHeatmap.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package one.convert;

import one.heatmap.Heatmap;
import one.jfr.Dictionary;
import one.jfr.JfrReader;
import one.jfr.StackTrace;
import one.jfr.event.AllocationSample;
import one.jfr.event.ContendedLock;
import one.jfr.event.Event;
import one.jfr.event.EventCollector;

import java.io.*;

import static one.convert.Frame.TYPE_INLINED;
import static one.convert.Frame.TYPE_KERNEL;

public class JfrToHeatmap extends JfrConverter {
    private final Heatmap heatmap;

    public JfrToHeatmap(JfrReader jfr, Arguments args) {
        super(jfr, args);
        this.heatmap = new Heatmap(args, this);
    }

    @Override
    protected EventCollector createCollector(Arguments args) {
        return new EventCollector() {
            @Override
            public void collect(Event event) {
                int classId = 0;
                byte type = 0;
                if (event instanceof AllocationSample) {
                    classId = ((AllocationSample) event).classId;
                    type = ((AllocationSample) event).tlabSize == 0 ? TYPE_KERNEL : TYPE_INLINED;
                } else if (event instanceof ContendedLock) {
                    classId = ((ContendedLock) event).classId;
                    type = TYPE_KERNEL;
                }

                long msFromStart = (event.time - jfr.chunkStartTicks) * 1_000 / jfr.ticksPerSec;
                long timeMs = jfr.chunkStartNanos / 1_000_000 + msFromStart;

                heatmap.addEvent(event.stackTraceId, event.tid, classId, type, timeMs);
            }

            @Override
            public void beforeChunk() {
                heatmap.beforeChunk();
                jfr.stackTraces.forEach(new Dictionary.Visitor<StackTrace>() {
                    @Override
                    public void visit(long key, StackTrace trace) {
                        heatmap.addStack(key, trace.methods, trace.locations, trace.types, trace.methods.length);
                    }
                });
            }

            @Override
            public void afterChunk() {
                jfr.stackTraces.clear();
            }

            @Override
            public boolean finish() {
                heatmap.finish(jfr.startNanos / 1_000_000);
                return false;
            }

            @Override
            public void forEach(Visitor visitor) {
                throw new AssertionError("Should not be called");
            }
        };
    }

    public void dump(OutputStream out) throws IOException {
        try (PrintStream ps = new PrintStream(out, false, "UTF-8")) {
            heatmap.dump(ps);
        }
    }

    public static void convert(String input, String output, Arguments args) throws IOException {
        JfrToHeatmap converter;
        try (JfrReader jfr = new JfrReader(input)) {
            converter = new JfrToHeatmap(jfr, args);
            converter.convert();
        }
        try (OutputStream out = new BufferedOutputStream(new FileOutputStream(output))) {
            converter.dump(out);
        }
    }
}


================================================
FILE: src\converter\one\convert\JfrToOtlp.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package one.convert;

import static one.convert.OtlpConstants.*;

import one.jfr.JfrReader;
import one.jfr.StackTrace;
import one.jfr.event.Event;
import one.jfr.event.EventCollector;
import one.proto.Proto;

import java.io.FileOutputStream;
import java.io.IOException;
import java.io.OutputStream;
import java.util.*;

/**
 * Converts .jfr output to OpenTelemetry protocol.
 */
public class JfrToOtlp extends JfrConverter {
    // Size in bytes to be allocated in the buffer to hold the varint containing the length of the message
    private static final int MSG_LARGE = 5;
    private static final int MSG_SMALL = 1;

    private final Index<String> stringPool = new Index<>(String.class, "");
    private final Index<String> functionPool = new Index<>(String.class, "");
    private final Index<Line> linePool = new Index<>(Line.class, Line.EMPTY);
    private final Index<KeyValue> attributesPool = new Index<>(KeyValue.class, KeyValue.EMPTY);
    private final Index<IntArray> stacksPool = new Index<>(IntArray.class, IntArray.EMPTY);
    private final int threadNameIndex = stringPool.index(OTLP_THREAD_NAME);

    private final Proto proto = new Proto(1024);

    public JfrToOtlp(JfrReader jfr, Arguments args) {
        super(jfr, args);
    }

    public void dump(OutputStream out) throws IOException {
        out.write(proto.buffer(), 0, proto.size());
    }

    @Override
    public void convert() throws IOException {
        long rpMark = proto.startField(PROFILES_DATA_resource_profiles, MSG_LARGE);
        long spMark = proto.startField(RESOURCE_PROFILES_scope_profiles, MSG_LARGE);
        super.convert();
        proto.commitField(spMark);
        proto.commitField(rpMark);

        writeProfileDictionary();
    }

    @Override
    protected void convertChunk() {
        List<SampleInfo> samplesInfo = new ArrayList<>();
        collector.forEach(new OtlpEventToSampleVisitor(samplesInfo));

        long pMark = proto.startField(SCOPE_PROFILES_profiles, MSG_LARGE);

        long sttMark = proto.startField(PROFILE_sample_type, MSG_SMALL);
        proto.field(VALUE_TYPE_type_strindex, stringPool.index(getValueType()));
        proto.field(VALUE_TYPE_unit_strindex,
                    stringPool.index(args.total ? getTotalUnits() : getSampleUnits()));
        proto.commitField(sttMark);

        proto.fieldFixed64(PROFILE_time_unix_nano, jfr.chunkStartNanos);
        proto.field(PROFILE_duration_nanos, jfr.chunkDurationNanos());

        writeSamples(samplesInfo, !args.total /* samples */);

        proto.commitField(pMark);
    }

    private void writeSamples(List<SampleInfo> samplesInfo, boolean samples) {
        for (SampleInfo si : samplesInfo) {
            long sMark = proto.startField(PROFILE_samples, MSG_SMALL);
            proto.field(SAMPLE_stack_index, si.stackIndex);
            proto.field(SAMPLE_values, samples ? si.samples : si.value);
            proto.field(SAMPLE_attribute_indices, si.threadNameAttributeIndex);
            proto.fieldFixed64(SAMPLE_timestamps_unix_nano, si.timeNanos);
            proto.commitField(sMark);
        }
    }

    private void writeProfileDictionary() {
        long profilesDictionaryMark = proto.startField(PROFILES_DATA_dictionary, MSG_LARGE);

        // Mapping[0] must be a default mapping according to the spec
        long mMark = proto.startField(PROFILES_DICTIONARY_mapping_table, MSG_SMALL);
        proto.commitField(mMark);

        for (String name : functionPool.keys()) {
            long fMark = proto.startField(PROFILES_DICTIONARY_function_table, MSG_SMALL);
            proto.field(FUNCTION_name_strindex, stringPool.index(name));
            proto.commitField(fMark);
        }

        for (Line line : linePool.keys()) {
            long locMark = proto.startField(PROFILES_DICTIONARY_location_table, MSG_SMALL);
            proto.field(LOCATION_mapping_index, 0);

            long lineMark = proto.startField(LOCATION_line, MSG_SMALL);
            proto.field(LINE_function_index, line.functionIdx);
            proto.field(LINE_lines, line.lineNumber);
            proto.commitField(lineMark);

            proto.commitField(locMark);
        }

        for (IntArray stack : stacksPool.keys()) {
            long stackMark = proto.startField(PROFILES_DICTIONARY_stack_table, MSG_LARGE);
            long locationIndicesMark = proto.startField(STACK_location_indices, MSG_LARGE);
            for (int locationIdx : stack.array) {
                proto.writeInt(locationIdx);
            }
            proto.commitField(locationIndicesMark);
            proto.commitField(stackMark);
        }

        for (String s : stringPool.keys()) {
            proto.field(PROFILES_DICTIONARY_string_table, s);
        }

        for (KeyValue kv : attributesPool.keys()) {
            long aMark = proto.startField(PROFILES_DICTIONARY_attribute_table, MSG_LARGE);
            proto.field(KEY_VALUE_A

================================================
FILE: src\converter\one\convert\JfrToPprof.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package one.convert;

import one.jfr.JfrReader;
import one.jfr.StackTrace;
import one.jfr.event.Event;
import one.proto.Proto;

import java.io.FileOutputStream;
import java.io.IOException;
import java.io.OutputStream;
import java.util.zip.GZIPOutputStream;

/**
 * Converts .jfr output to <a href="https://github.com/google/pprof">pprof</a>.
 */
public class JfrToPprof extends JfrConverter {
    private final Proto profile = new Proto(100000);
    private final Index<String> strings = new Index<>(String.class, "");
    private final Index<String> functions = new Index<>(String.class, "");
    private final Index<Long> locations = new Index<>(Long.class, 0L);

    public JfrToPprof(JfrReader jfr, Arguments args) {
        super(jfr, args);

        profile.field(1, valueType(getValueType(), args.total ? getTotalUnits() : getSampleUnits()))
                .field(13, strings.index("Produced by async-profiler"));
    }

    @Override
    protected void convertChunk() {
        collector.forEach(new AggregatedEventVisitor() {
            final Proto s = new Proto(100);

            @Override
            public void visit(Event event, long value) {
                if (excludeStack(event.stackTraceId, event.tid, event.classId())) {
                    return;
                }
                profile.field(2, sample(s, event, value));
                s.reset();
            }
        });
    }

    public void dump(OutputStream out) throws IOException {
        profile.field(3, mapping(1, 0, Long.MAX_VALUE, "async-profiler"));

        Long[] locations = this.locations.keys();
        for (int i = 1; i < locations.length; i++) {
            profile.field(4, location(i, locations[i]));
        }

        String[] functions = this.functions.keys();
        for (int i = 1; i < functions.length; i++) {
            profile.field(5, function(i, functions[i]));
        }

        String[] strings = this.strings.keys();
        for (String string : strings) {
            profile.field(6, string);
        }

        profile.field(9, jfr.startNanos)
                .field(10, jfr.durationNanos());

        out.write(profile.buffer(), 0, profile.size());
    }

    private Proto sample(Proto s, Event event, long value) {
        long packedLocations = s.startField(1, 3);

        long classId = event.classId();
        if (classId != 0) {
            int function = functions.index(getClassName(classId));
            s.writeInt(locations.index((long) function << 16));
        }

        StackTrace stackTrace = jfr.stackTraces.get(event.stackTraceId);
        if (stackTrace != null) {
            long[] methods = stackTrace.methods;
            byte[] types = stackTrace.types;
            int[] lines = stackTrace.locations;
            for (int i = 0; i < methods.length; i++) {
                String methodName = getMethodName(methods[i], types[i]);
                int function = functions.index(methodName);
                s.writeInt(locations.index((long) function << 16 | lines[i] >>> 16));
            }
        }

        s.commitField(packedLocations);
        s.field(2, value);

        if (args.threads && event.tid != 0) {
            s.field(3, label("thread", getThreadName(event.tid)));
        }
        if (args.classify && stackTrace != null) {
            s.field(3, label("category", getCategory(stackTrace).title));
        }

        return s;
    }

    private Proto valueType(String type, String unit) {
        return new Proto(16)
                .field(1, strings.index(type))
                .field(2, strings.index(unit));
    }

    private Proto label(String key, String str) {
        return new Proto(16)
                .field(1, strings.index(key))
                .field(2, strings.index(str));
    }

    private Proto mapping(int id, long start, long limit, String fileName) {
        return new Proto(16)
                .field(1, id)
                .field(2, start)
                .field(3, limit)
                .field(5, strings.index(fileName));
    }

    private Proto location(int id, long location) {
        return new Proto(16)
                .field(1, id)
                .field(4, line((int) (location >>> 16), (int) location & 0xffff));
    }

    private Proto line(int functionId, int line) {
        return new Proto(16)
                .field(1, functionId)
                .field(2, line);
    }

    private Proto function(int id, String name) {
        return new Proto(16)
                .field(1, id)
                .field(2, strings.index(name));
    }

    public static void convert(String input, String output, Arguments args) throws IOException {
        JfrToPprof converter;
        try (JfrReader jfr = new JfrReader(input)) {
            converter = new JfrToPprof(jfr, args);
            converter.convert();
        }
        try (FileOutputStream fos = new FileOutputStream(output);
             OutputS

================================================
FILE: src\converter\one\convert\OtlpConstants.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package one.convert;

final class OtlpConstants {

    static final String OTLP_THREAD_NAME = "thread.name";

    static final int
            PROFILES_DICTIONARY_mapping_table = 1,
            PROFILES_DICTIONARY_location_table = 2,
            PROFILES_DICTIONARY_function_table = 3,
            PROFILES_DICTIONARY_string_table = 5,
            PROFILES_DICTIONARY_attribute_table = 6,
            PROFILES_DICTIONARY_stack_table = 7;

    static final int
            PROFILES_DATA_resource_profiles = 1,
            PROFILES_DATA_dictionary = 2;

    static final int RESOURCE_PROFILES_scope_profiles = 2;

    static final int SCOPE_PROFILES_profiles = 2;

    static final int
            PROFILE_sample_type = 1,
            PROFILE_samples = 2,
            PROFILE_time_unix_nano = 3,
            PROFILE_duration_nanos = 4;

    static final int
            VALUE_TYPE_type_strindex = 1,
            VALUE_TYPE_unit_strindex = 2,
            VALUE_TYPE_aggregation_temporality = 3;

    static final int
            SAMPLE_stack_index = 1,
            SAMPLE_values = 2,
            SAMPLE_attribute_indices = 3,
            SAMPLE_timestamps_unix_nano = 5;

    static final int
            STACK_location_indices = 1;

    static final int
            LOCATION_mapping_index = 1,
            LOCATION_line = 3;

    static final int
            LINE_function_index = 1,
            LINE_lines = 2;

    static final int FUNCTION_name_strindex = 1;

    static final int
            KEY_VALUE_AND_UNIT_key_strindex = 1,
            KEY_VALUE_AND_UNIT_value = 2;

    static final int ANY_VALUE_string_value = 1;
}


================================================
FILE: src\converter\one\convert\ResourceProcessor.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package one.convert;

import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintStream;

public class ResourceProcessor {

    public static String getResource(String name) {
        try (InputStream stream = ResourceProcessor.class.getResourceAsStream(name)) {
            if (stream == null) {
                throw new IOException("No resource found");
            }

            ByteArrayOutputStream result = new ByteArrayOutputStream();
            byte[] buffer = new byte[32768];
            for (int length; (length = stream.read(buffer)) != -1; ) {
                result.write(buffer, 0, length);
            }
            return result.toString("UTF-8");
        } catch (IOException e) {
            throw new IllegalStateException("Can't load resource with name " + name);
        }
    }

    public static String printTill(PrintStream out, String data, String till) {
        int index = data.indexOf(till);
        out.print(data.substring(0, index));
        return data.substring(index + till.length());
    }

}


================================================
FILE: src\converter\one\convert\TimeIntervals.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package one.convert;

import java.util.Map;
import java.util.NavigableMap;
import java.util.TreeMap;
import java.util.Arrays;

public final class TimeIntervals {
    private final long[] startIntervals;
    private final long[] endIntervals;

    private TimeIntervals(long[] startIntervals, long[] endIntervals) {
        this.startIntervals = startIntervals;
        this.endIntervals = endIntervals;
    }

    public boolean contains(long instant) {
        int searchOut = Arrays.binarySearch(startIntervals, instant);
        if (searchOut >= 0) {
            return true;
        }

        int insertionPoint = -(searchOut + 1); // First element greater than instant
        if (insertionPoint == 0) {
            return false; // First interval start is greater than instant
        }
        int startIndex = insertionPoint - 1;
        return instant <= endIntervals[startIndex];
    }

    public static final class Builder {
        // No overlapping intervals
        private final TreeMap<Long, Long> timeIntervals = new TreeMap<>();

        public void add(long startInstant, long endInstant) {
            if (startInstant > endInstant) {
                throw new IllegalArgumentException("'startInstant' should not be after 'endInstant'");
            }

            // Are there shorter intervals which overlap with the new interval?
            NavigableMap<Long, Long> view = timeIntervals.subMap(startInstant, true /* inclusive */, endInstant, true /* inclusive */);
            Map.Entry<Long, Long> last = view.pollLastEntry();
            if (last != null) {
                endInstant = Long.max(last.getValue(), endInstant);
            }
            view.clear();

            // Perhaps the end of the interval before 'view' ends after startInstant?
            Map.Entry<Long, Long> floor = timeIntervals.floorEntry(startInstant);
            if (floor != null) {
                long floorEnd = floor.getValue();
                if (floorEnd >= startInstant) {
                    timeIntervals.remove(floor.getKey());
                    startInstant = floor.getKey();
                    endInstant = Long.max(endInstant, floorEnd);
                }
            }

            timeIntervals.put(startInstant, endInstant);
        }

        public TimeIntervals build() {
            long[] startIntervals = new long[timeIntervals.size()];
            long[] endIntervals = new long[timeIntervals.size()];
            int index = 0;
            for (Map.Entry<Long, Long> entry : timeIntervals.entrySet()) {
                startIntervals[index] = entry.getKey();
                endIntervals[index] = entry.getValue();
                ++index;
            }
            return new TimeIntervals(startIntervals, endIntervals);
        }
    }
}


================================================
FILE: src\converter\one\heatmap\Heatmap.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package one.heatmap;

import java.io.IOException;
import java.io.PrintStream;
import java.util.*;
import java.util.regex.Pattern;

import one.convert.*;
import one.jfr.DictionaryInt;

public class Heatmap {

    // TODO: should be probably an argument,
    // but there is a good chance that changing it will have some side effects
    public static final int BLOCK_DURATION_MS = 20;

    private final Arguments args;
    private State state;
    private long startMs;

    public Heatmap(Arguments args, JfrConverter converter) {
        this.args = args;
        this.state = new State(converter, args, BLOCK_DURATION_MS);
    }

    public void addEvent(int stackTraceId, int threadId, int classId, byte type, long timeMs) {
        state.addEvent(stackTraceId, threadId, classId, type, timeMs);
    }

    public void addStack(long id, long[] methods, int[] locations, byte[] types, int size) {
        state.addStack(id, methods, locations, types, size);
    }

    public void beforeChunk() {
        state.methodCache.clear();
        state.includeCache.clear();
    }

    public void finish(long startMs) {
        this.startMs = startMs;
        state.methodCache.clear();
        state.stackTracesCache.clear();
        state.includeCache.clear();
    }

    private EvaluationContext evaluate() {
        State state = this.state;
        this.state = null;
        return new EvaluationContext(
                state.sampleList.samples(),
                state.methods,
                state.stackTracesRemap.orderedTraces(),
                state.symbolTable.keys()
        );
    }

    private void compressMethods(HtmlOut out, Method[] methods) {
        out.writeVar(methods.length);
        for (Method method : methods) {
            out.writeVar(method.className);
            out.writeVar(method.methodName);
            out.write18(method.location & 0xffff);
            out.write18(method.location >>> 16);
            out.write6(method.type);
        }
    }

    public void dump(PrintStream stream) throws IOException {
        if (state.sampleList.getRecordsCount() == 0) {
            // Need a better way to handle this, but we should not throw an exception
            stream.println("No samples found");
            return;
        }

        EvaluationContext evaluationContext = evaluate();

        String tail = ResourceProcessor.getResource("/heatmap.html");

        tail = ResourceProcessor.printTill(stream, tail, "/*executionsHeatmap:*/");
        HtmlOut out = new HtmlOut(stream);
        stream.print('S');
        printHeatmap(out, evaluationContext);
        stream.print('E');

        tail = ResourceProcessor.printTill(stream, tail, "/*methods:*/");
        out.reset();
        stream.print('S');
        printMethods(out, evaluationContext);
        stream.print('E');

        tail = ResourceProcessor.printTill(stream, tail, "/*title:*/");
        stream.print(args.title != null ? args.title : "Heatmap");

        tail = ResourceProcessor.printTill(stream, tail, "/*startMs:*/0");
        stream.print(startMs);

        tail = ResourceProcessor.printTill(stream, tail, "/*cpool:*/");
        printConstantPool(stream, evaluationContext);

        stream.print(tail);
    }

    private void printHeatmap(final HtmlOut out, EvaluationContext context) {
        int veryStart = out.pos();
        int wasPos = out.pos();

        // calculates methods frequency during building the tree
        int[] stackChunksBuffer = buildLz78TreeAndPrepareData(context);

        // gives methods new ids, more frequent (in tree's data) methods will have lower id
        renameMethodsByFrequency(context);

        // writes "starts" - ids of methods that indicates a start of a next stack trace
        writeStartMethods(out, context);
        wasPos = debugStep("start methods", out, wasPos, veryStart);

        // writes block sizes, compressed by huffman algorithm
        writeBlockSizes(out, context);
        wasPos = debugStep("stack sizes", out, wasPos, veryStart);

        // NOTE: destroys internal state!
        SynonymTable synonymTable = context.nodeTree.extractSynonymTable();
        synonymTable.calculateSynonyms();
        // writes frequent lz tree nodes as a synonyms table
        writeSynonymsTable(out, synonymTable);
        wasPos = debugStep("tree synonyms", out, wasPos, veryStart);

        // writes lz tree with two pairs of var-ints: [parent node id] + [method id of this node]
        writeTree(out, synonymTable, context);
        wasPos = debugStep("tree body", out, wasPos, veryStart);

        // calculate counts for the next synonyms table, that will be used for samples
        int chunksCount = calculateSamplesSynonyms(synonymTable, context, stackChunksBuffer);
        // writes frequent lz tree nodes as a synonyms table (for sample chunks)
        writeSynonymsTable(out, synonymTable);
        wasPos = debugStep("sample

================================================
FILE: src\converter\one\heatmap\HtmlOut.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package one.heatmap;

import java.io.PrintStream;

public class HtmlOut {

    private final PrintStream out;

    private int pos;

    public HtmlOut(PrintStream out) {
        this.out = out;
    }

    public int pos() {
        return pos;
    }

    public void reset() {
        pos = 0;
    }

    public void nextByte(int c) {
        switch (c) {
            case 0:
                c = 127;
                break;
            case '\r':
                c = 126;
                break;
            case '&':
                c = 125;
                break;
            case '<':
                c = 124;
                break;
            case '>':
                c = 123;
                break;
        }
        out.write(c);
        pos++;
    }

    public void writeVar(long v) {
        while (v >= 61) {
            int b = 61 + (int) (v % 61);
            nextByte(b);
            v /= 61;
        }
        nextByte((int) v);
    }

    public void write6(int v) {
        if ((v & ~0x3F) != 0) {
            throw new IllegalArgumentException("Value " + v + " is out of bounds");
        }
        nextByte(v);
    }

    public void write18(int v) {
        if ((v & ~0x3FFFF) != 0) {
            throw new IllegalArgumentException("Value " + v + " is out of bounds");
        }
        for (int i = 0; i < 3; i++) {
            nextByte(v & 0x3F);
            v >>>= 6;
        }
    }

    public void write30(int v) {
        if ((v & ~0x3FFFFFFF) != 0) {
            throw new IllegalArgumentException("Value " + v + " is out of bounds");
        }
        for (int i = 0; i < 5; i++) {
            nextByte(v & 0x3F);
            v >>>= 6;
        }
    }
}


================================================
FILE: src\converter\one\heatmap\HuffmanEncoder.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package one.heatmap;

import java.util.Arrays;
import java.util.PriorityQueue;

public class HuffmanEncoder {

    private final long[] decodeTable;   // 8 bit for bits count, 56 value
    private final long[] encodeTable;   // 8 bit for bits count, 56 bits

    private int data;
    private int bits;

    // log2(123^9) = 62.4826305481 > 62 bits, 0.7% space lost, but it is expensive to decode (no support for int64 in js)
    // log2(123^4) = 27.7700580214 > 27 bits, 2.8% space lost, but it is cheap to decode (using one int32)
    private static final int MAX_BITS = 27;
    public final int[] values = new int[4]; // 0..122

    public HuffmanEncoder(int[] frequencies, int maxFrequencyIndex) {
        PriorityQueue<Node> minHeap = new PriorityQueue<>(maxFrequencyIndex + 1);
        for (int i = 0; i <= maxFrequencyIndex; i++) {
            int frequency = frequencies[i];
            if (frequency == 0) {
                continue;
            }
            minHeap.add(new Node(frequency, i));
        }

        while (minHeap.size() > 1) {
            Node left = minHeap.remove();
            Node right = minHeap.remove();

            minHeap.add(new Node(left, right));
        }

        long[] decodeTable = new long[maxFrequencyIndex + 1];
        minHeap.remove().fillTable(decodeTable, 0);
        Arrays.sort(decodeTable);
        for (int i = 0; i < decodeTable.length; i++) {
            if (decodeTable[i] != 0) {
                if (i != 0) {
                    long[] nextDecodeTable = new long[decodeTable.length - i];
                    System.arraycopy(decodeTable, i, nextDecodeTable, 0, nextDecodeTable.length);
                    decodeTable = nextDecodeTable;
                }
                break;
            }
        }
        this.decodeTable = decodeTable;

        encodeTable = new long[maxFrequencyIndex + 1];
        encodeTable[(int) decodeTable[0]] = decodeTable[0] & 0xFF00_0000_0000_0000L;
        long code = 0;

        for (int i = 1; i < decodeTable.length; i++) {
            long decodePrev = decodeTable[i - 1];
            long decodeNow = decodeTable[i];

            long prevCount = decodePrev >>> 56;
            long nowCount = decodeNow >>> 56;

            code = (code + 1) << (nowCount - prevCount);

            int value = (int) decodeNow;
            encodeTable[value] = nowCount << 56 | code;
        }
    }

    public boolean append(int value) {
        boolean hasOverflow = false;

        long v = encodeTable[value];
        int bits = (int) (v >>> 56);
        for (long i = 1L << (bits - 1); i > 0; i >>>= 1) {
            this.data = this.data << 1 | ((v & i) == 0 ? 0 : 1);
            if (++this.bits == MAX_BITS) {
                hasOverflow = true;
                flush();
            }
        }

        return hasOverflow;
    }

    public boolean flushIfNeed() {
        if (bits == 0) {
            return false;
        }
        this.data = this.data << (MAX_BITS - bits);
        flush();
        return true;
    }

    public void flush() {
        data = Integer.reverse(data) >>> 5;

        values[3] = data % 123;
        data /= 123;
        values[2] = data % 123;
        data /= 123;
        values[1] = data % 123;
        data /= 123;
        values[0] = data;
        data = 0;

        bits = 0;
    }

    public long[] calculateOutputTable() {
        return decodeTable;
    }

    private static class Node implements Comparable<Node> {
        final int frequency;
        final int value;

        Node left, right;

        Node(int frequency, int value) {
            this.frequency = frequency;
            this.value = value;
        }

        public Node(Node left, Node right) {
            this.left = left;
            this.right = right;
            this.frequency = left.frequency + right.frequency;
            this.value = -1;
        }

        public void fillTable(long[] table, long bitsCount) {
            if (value >= 0) {
                table[value] = bitsCount | value;
                return;
            }
            left.fillTable(table, bitsCount + 0x0100_0000_0000_0000L);
            right.fillTable(table, bitsCount + 0x0100_0000_0000_0000L);
        }

        @Override
        public int compareTo(Node o) {
            // frequencies are strictly positive
            return frequency - o.frequency;
        }
    }

}


================================================
FILE: src\converter\one\heatmap\LzNodeTree.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package one.heatmap;

import java.util.Arrays;

public class LzNodeTree {

    private static final int INITIAL_CAPACITY = 2 * 1024 * 1024;

    // hash(methodId << 32 | parentNodeId) -> methodId << 32 | parentNodeId
    private long[] keys;    // reused by SynonymTable
    // hash(methodId << 32 | parentNodeId) -> childNodeId
    private int[] values;  // can be reused after buildLz78TreeAndPrepareData

    // (nodeId - 1) -> methodId << 32 | parentNodeId
    private long[] outputData;              // can be reused after writeTree:130!
    // nodeId -> childrenCount
    private int[] childrenCount;    // reused by SynonymTable
    // nodeId -> parentNodeId << 32 | lengthToRoot
    private long[] lengthToRoot;

    private int storageSize = 0;
    private int nodesCount = 1;

    public LzNodeTree() {
        keys = new long[INITIAL_CAPACITY];
        values = new int[INITIAL_CAPACITY];

        outputData = new long[INITIAL_CAPACITY / 2];
        childrenCount = new int[INITIAL_CAPACITY / 2];
        lengthToRoot = new long[INITIAL_CAPACITY / 2];
    }

    public int appendChild(int parentNode, int methodId) {
        long method = (long) methodId << 32;
        long key = method | parentNode;

        int mask = keys.length - 1;
        int i = hashCode(key) & mask;
        while (true) {
            long k = keys[i];
            if (k == 0) {
                break;
            }
            if (k == key) {
                return values[i];
            }
            i = (i + 1) & mask;
        }

        if (nodesCount >= outputData.length) {
            outputData = Arrays.copyOf(outputData, nodesCount + nodesCount / 2);
            childrenCount = Arrays.copyOf(childrenCount, nodesCount + nodesCount / 2);
            lengthToRoot = Arrays.copyOf(lengthToRoot, nodesCount + nodesCount / 2);
        }

        lengthToRoot[nodesCount] = ((int) lengthToRoot[parentNode] + 1) | ((long) parentNode << 32);
        outputData[nodesCount - 1] = key;
        keys[i] = key;
        values[i] = nodesCount;

        if (nodesCount * 2 > keys.length) {
            resize(keys.length * 2);
        }
        nodesCount++;

        childrenCount[parentNode]--; // negotiation for better sort

        return 0;
    }

    public long[] treeData() {
        return outputData;
    }

    public int treeDataSize() {
        return nodesCount - 1;
    }

    public int extractParentId(long treeElement) {
        return (int) treeElement;
    }

    public int extractMethodId(long treeElement) {
        return (int) (treeElement >>> 32);
    }

    public void markNodeAsLastlyUsed(int nodeId) {
        long ltr = lengthToRoot[nodeId];
        int parent = (int) (ltr >>> 32);
        if (parent >= 0) {
            lengthToRoot[nodeId] = ltr | 0x8000000000000000L;
            do {
                ltr = lengthToRoot[parent];
                lengthToRoot[parent] = ltr | 0xC000000000000000L;
                parent = (int) (ltr >>> 32);
            } while (parent > 0);
        }
    }

    // destroys values
    public void compactTree(int[] remapAsWell, int fromIndex, int toIndex) {
        int[] mappings = values;
        mappings[0] = 0;
        int nodes = 1;
        int storageSize = 0;
        for (int oldNodeID = 1; oldNodeID < nodesCount; oldNodeID++) {
            long ltr = lengthToRoot[oldNodeID];
            if (ltr >= 0) {
                // unused
                continue;
            }
            if ((ltr & 0x4000000000000000L) == 0) {
                storageSize += (int) ltr;
            }
            mappings[oldNodeID] = nodes;
            childrenCount[nodes] = childrenCount[oldNodeID];
            long out = outputData[oldNodeID - 1];
            long outMethod = 0xFFFFFFFF00000000L & out;
            int oldParent = (int) out;
            outputData[nodes - 1] = outMethod | mappings[oldParent];
            nodes++;
        }
        for (int i = fromIndex; i < toIndex; i++) {
            remapAsWell[i] = mappings[remapAsWell[i]];
        }
        this.storageSize = storageSize;
        this.nodesCount = nodes;
    }

    // destroys keys and childrenCount arrays
    public SynonymTable extractSynonymTable() {
        return new SynonymTable(keys, childrenCount, nodesCount);
    }

    public int storageSize() {
        return storageSize;
    }

    public int nodesCount() {
        return nodesCount;
    }

    private void resize(int newCapacity) {
        long[] newKeys = new long[newCapacity];
        int[] newValues = new int[newCapacity];
        int mask = newKeys.length - 1;

        for (int i = 0; i < keys.length; i++) {
            if (keys[i] != 0) {
                for (int j = hashCode(keys[i]) & mask; ; j = (j + 1) & mask) {
                    if (newKeys[j] == 0) {
                        newKeys[j] = keys[i];
                        newValues[j] = values[i];
                        break;
                 

================================================
FILE: src\converter\one\heatmap\Method.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package one.heatmap;

import one.convert.Frame;

public class Method {

    public static final Method EMPTY = new Method(0, 0, -1, (byte) 0, false);

    public final int className;
    public final int methodName;
    public final int location;
    public final byte type;
    public final boolean start;

    public int frequency;
    // An identifier based on frequency ordering, more frequent methods will get a lower ID
    public int frequencyBasedId;
    public int index;

    Method(int className, int methodName, int location, byte type, boolean start) {
        this.className = className;
        this.methodName = methodName;
        this.location = location;
        this.type = type;
        this.start = start;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;

        Method method = (Method) o;

        if (className != method.className) return false;
        if (methodName != method.methodName) return false;
        if (location != method.location) return false;
        if (type != method.type) return false;
        return start == method.start;
    }

    @Override
    public int hashCode() {
        int result = className;
        result = 31 * result + methodName;
        result = 31 * result + location;
        result = 31 * result + (int) type;
        result = 31 * result + (start ? 1 : 0);
        return result;
    }
}


================================================
FILE: src\converter\one\heatmap\SampleList.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package one.heatmap;

import java.util.Arrays;

public class SampleList {

    private static final int DEFAULT_SAMPLES_COUNT = 10_000_000;

    private final long blockDurationMs;

    // highest 32 bits for time block index, lowest 32 bits for stack id
    private long[] data = new long[DEFAULT_SAMPLES_COUNT];

    private long initialTime = 0;
    private int recordsCount = 0;

    public SampleList(long blockDurationMs) {
        this.blockDurationMs = blockDurationMs;
    }

    public void add(int stackId, long timeMs) {
        if (initialTime == 0) {
            initialTime = timeMs;
            data[recordsCount++] = stackId;
            return;
        }
        if (recordsCount >= data.length) {
            data = Arrays.copyOf(data, data.length * 3 / 2);
        }

        int currentTimeBlock = (int) ((timeMs - initialTime) / blockDurationMs);
        data[recordsCount++] = (long) currentTimeBlock << 32 | stackId;
    }

    public Result samples() {
        Arrays.sort(data, 0, recordsCount);

        int firstBlockId = (int) (data[0] >> 32);
        int lastBlockId = (int) (data[recordsCount - 1] >> 32);

        int blocksCount = lastBlockId - firstBlockId + 1;

        int[] blockSizes = new int[blocksCount];
        int[] stackIds = new int[recordsCount];

        int stackIdsPos = 0;
        int currentBlockIndex = 0;
        int currentBlockSize = 0;
        int currentBlockId = firstBlockId;

        outer:
        while (stackIdsPos < stackIds.length) {
            long currentData = data[stackIdsPos];
            int blockId = (int) (currentData >> 32);
            while (currentBlockId != blockId) {
                blockSizes[currentBlockIndex++] = currentBlockSize;
                currentBlockSize = 0;
                currentBlockId++;
                if (currentBlockId > lastBlockId) {
                    break outer;
                }
            }

            currentBlockSize++;
            stackIds[stackIdsPos++] = (int) currentData - 1;
        }

        if (currentBlockId <= lastBlockId) {
            blockSizes[currentBlockIndex] = currentBlockSize;
        }

        return new Result(blockSizes, stackIds);
    }

    public int getRecordsCount() {
        return recordsCount;
    }

    public static class Result {
        public final int[] blockSizes;
        public final int[] stackIds;

        public Result(int[] blockSizes, int[] stackIds) {
            this.blockSizes = blockSizes;
            this.stackIds = stackIds;
        }
    }

}


================================================
FILE: src\converter\one\heatmap\StackStorage.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package one.heatmap;

import java.util.Arrays;

public final class StackStorage {

    private static final int INITIAL_CAPACITY = 16 * 1024;

    private int size;

    // highest 32 bits for index, lowest 32 bits for hash
    private long[] meta;

    // ordered incrementally
    private int[][] values;

    public StackStorage() {
        this(INITIAL_CAPACITY);
    }

    public StackStorage(int initialCapacity) {
        meta = new long[initialCapacity * 2];
        values = new int[initialCapacity][];
    }

    public int[] get(int id) {
        return values[id - 1];
    }

    public int index(int[] input, int inputSize) {
        int mask = meta.length - 1;
        int targetHash = murmur(input, inputSize);
        int i = targetHash & mask;
        for (long currentMeta = meta[i]; currentMeta != 0; currentMeta = meta[i]) {
            if ((int) currentMeta == targetHash) {
                int index = (int) (currentMeta >>> 32);
                if (equals(input, inputSize, values[index])) {
                    return index + 1;
                }
            }
            i = (i + 1) & mask;
        }

        values[size] = Arrays.copyOf(input, inputSize);
        meta[i] = (long) size << 32 | (targetHash & 0xFFFFFFFFL);
        size++;

        if (size * 2 > values.length) {
            resize(values.length * 2);
        }

        return size;
    }

    public int[][] orderedTraces() {
        return Arrays.copyOf(values, size);
    }

    private void resize(int newCapacity) {
        long[] newMeta = new long[newCapacity * 2];
        int mask = newMeta.length - 1;

        for (long m : meta) {
            if (m != 0) {
                int hashCode = (int) m;
                for (int j = hashCode & mask; ; j = (j + 1) & mask) {
                    if (newMeta[j] == 0) {
                        newMeta[j] = m;
                        break;
                    }
                }
            }
        }

        meta = newMeta;
        values = Arrays.copyOf(values, newCapacity);
    }

    private boolean equals(int[] a, int size, int[] b) {
        if (b.length != size) return false;
        for (int i = 0; i < size; ++i) {
            if (a[i] != b[i]) return false;
        }
        return true;
    }

    private static int murmur(int[] data, int size) {
        int m = 0x5bd1e995;
        int h = 0x9747b28c ^ size;

        for (int i = 0; i < size; i++) {
            int k = data[i];
            k *= m;
            k ^= k >>> 24;
            k *= m;
            h *= m;
            h ^= k;
        }

        h ^= h >>> 13;
        h *= m;
        h ^= h >>> 15;

        return h;
    }
}


================================================
FILE: src\converter\one\heatmap\SynonymTable.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package one.heatmap;

import java.util.Arrays;

public class SynonymTable {

    private final long[] synonyms;
    private final int[] childrenCountOrNodeSynonym;
    private final int nodesCount;

    private int synonymsCount;

    public SynonymTable(long[] synonyms, int[] childrenCount, int nodesCount) {
        this.synonyms = synonyms;
        this.childrenCountOrNodeSynonym = childrenCount;
        this.nodesCount = nodesCount;
    }

    public void calculateSynonyms() {
        int[] childrenCount = childrenCountOrNodeSynonym;
        for (int i = 0; i < nodesCount; i++) {
            synonyms[i] = (long) childrenCount[i] << 32 | i;
        }

        Arrays.sort(synonyms, 0, nodesCount);

        synonymsCount = Math.min(61 * 61, nodesCount);

        int[] nodeSynonyms = childrenCountOrNodeSynonym;
        for (int i = 0; i < nodesCount; i++) {
            nodeSynonyms[i] = synonymsCount + i;
        }
        for (int i = 0; i < synonymsCount; i++) {
            nodeSynonyms[(int) synonyms[i]] = i;
        }
    }

    public int synonymsCount() {
        return synonymsCount;
    }

    public int synonymAt(int synonymIndex) {
        return (int) synonyms[synonymIndex] + synonymsCount;
    }

    public int nodeIdOrSynonym(int node) {
        return childrenCountOrNodeSynonym[node];
    }

    public int[] reset() {
        int[] childrenCount = childrenCountOrNodeSynonym;
        Arrays.fill(childrenCount, 0, nodesCount, 0);
        return childrenCount;
    }
}


================================================
FILE: src\converter\one\jfr\ClassRef.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package one.jfr;

public class ClassRef {
    public final long name;

    public ClassRef(long name) {
        this.name = name;
    }
}


================================================
FILE: src\converter\one\jfr\Dictionary.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package one.jfr;

import java.util.Arrays;

/**
 * Fast and compact long->Object map.
 */
public class Dictionary<T> {
    private static final int INITIAL_CAPACITY = 16;

    private long[] keys;
    private Object[] values;
    private int size;

    public Dictionary() {
        this(INITIAL_CAPACITY);
    }

    public Dictionary(int initialCapacity) {
        this.keys = new long[initialCapacity];
        this.values = new Object[initialCapacity];
    }

    public void clear() {
        Arrays.fill(keys, 0);
        Arrays.fill(values, null);
        size = 0;
    }

    public int size() {
       return size;
    }

    // key[i]==0 is used to signal that the i-th position is unset.
    // Thus, we map key=key+1, so the user can still use key=0.
    private static long remapKey(long key) {
        if (key < 0) {
            throw new IllegalArgumentException("Negative keys not allowed");
        }
        return key + 1;
    }

    public void put(long key, T value) {
        key = remapKey(key);

        int mask = keys.length - 1;
        int i = hashCode(key) & mask;
        while (keys[i] != 0) {
            if (keys[i] == key) {
                values[i] = value;
                return;
            }
            i = (i + 1) & mask;
        }
        keys[i] = key;
        values[i] = value;

        if (++size * 2 > keys.length) {
            resize(keys.length * 2);
        }
    }

    @SuppressWarnings("unchecked")
    public T get(long key) {
        key = remapKey(key);

        int mask = keys.length - 1;
        int i = hashCode(key) & mask;
        while (keys[i] != key && keys[i] != 0) {
            i = (i + 1) & mask;
        }
        return (T) values[i];
    }

    @SuppressWarnings("unchecked")
    public void forEach(Visitor<T> visitor) {
        for (int i = 0; i < keys.length; i++) {
            if (keys[i] != 0) {
                // Map key back, see remapKey
                visitor.visit(keys[i] - 1, (T) values[i]);
            }
        }
    }

    public int preallocate(int count) {
        if (count * 2 > keys.length) {
            resize(Integer.highestOneBit(count * 4 - 1));
        }
        return count;
    }

    private void resize(int newCapacity) {
        long[] newKeys = new long[newCapacity];
        Object[] newValues = new Object[newCapacity];
        int mask = newKeys.length - 1;

        for (int i = 0; i < keys.length; i++) {
            if (keys[i] != 0) {
                for (int j = hashCode(keys[i]) & mask; ; j = (j + 1) & mask) {
                    if (newKeys[j] == 0) {
                        newKeys[j] = keys[i];
                        newValues[j] = values[i];
                        break;
                    }
                }
            }
        }

        keys = newKeys;
        values = newValues;
    }

    private static int hashCode(long key) {
        key *= 0xc6a4a7935bd1e995L;
        return (int) (key ^ (key >>> 32));
    }

    public interface Visitor<T> {
        void visit(long key, T value);
    }
}


================================================
FILE: src\converter\one\jfr\DictionaryInt.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package one.jfr;

import java.util.Arrays;

/**
 * Fast and compact long->int map.
 */
public class DictionaryInt {
    private static final int INITIAL_CAPACITY = 16;

    private long[] keys;
    private int[] values;
    private int size;

    public DictionaryInt() {
        this(INITIAL_CAPACITY);
    }

    public DictionaryInt(int initialCapacity) {
        this.keys = new long[initialCapacity];
        this.values = new int[initialCapacity];
    }

    public void clear() {
        Arrays.fill(keys, 0);
        Arrays.fill(values, 0);
        size = 0;
    }

    public void put(long key, int value) {
        if (key == 0) {
            throw new IllegalArgumentException("Zero key not allowed");
        }

        int mask = keys.length - 1;
        int i = hashCode(key) & mask;
        while (keys[i] != 0) {
            if (keys[i] == key) {
                values[i] = value;
                return;
            }
            i = (i + 1) & mask;
        }
        keys[i] = key;
        values[i] = value;

        if (++size * 2 > keys.length) {
            resize(keys.length * 2);
        }
    }

    public int get(long key) {
        int mask = keys.length - 1;
        int i = hashCode(key) & mask;
        while (keys[i] != key) {
            if (keys[i] == 0) {
                throw new IllegalArgumentException("No such key: " + key);
            }
            i = (i + 1) & mask;
        }
        return values[i];
    }

    public int get(long key, int notFound) {
        int mask = keys.length - 1;
        int i = hashCode(key) & mask;
        while (keys[i] != key) {
            if (keys[i] == 0) {
                return notFound;
            }
            i = (i + 1) & mask;
        }
        return values[i];
    }

    public void forEach(Visitor visitor) {
        for (int i = 0; i < keys.length; i++) {
            if (keys[i] != 0) {
                visitor.visit(keys[i], values[i]);
            }
        }
    }

    public int preallocate(int count) {
        if (count * 2 > keys.length) {
            resize(Integer.highestOneBit(count * 4 - 1));
        }
        return count;
    }

    private void resize(int newCapacity) {
        long[] newKeys = new long[newCapacity];
        int[] newValues = new int[newCapacity];
        int mask = newKeys.length - 1;

        for (int i = 0; i < keys.length; i++) {
            if (keys[i] != 0) {
                for (int j = hashCode(keys[i]) & mask; ; j = (j + 1) & mask) {
                    if (newKeys[j] == 0) {
                        newKeys[j] = keys[i];
                        newValues[j] = values[i];
                        break;
                    }
                }
            }
        }

        keys = newKeys;
        values = newValues;
    }

    private static int hashCode(long key) {
        key *= 0xc6a4a7935bd1e995L;
        return (int) (key ^ (key >>> 32));
    }

    public interface Visitor {
        void visit(long key, int value);
    }
}


================================================
FILE: src\converter\one\jfr\Element.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package one.jfr;

class Element {

    void addChild(Element e) {
    }
}


================================================
FILE: src\converter\one\jfr\JfrClass.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package one.jfr;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;

public class JfrClass extends Element {
    final int id;
    final boolean simpleType;
    final String name;
    final List<JfrField> fields;

    JfrClass(Map<String, String> attributes) {
        this.id = Integer.parseInt(attributes.get("id"));
        this.simpleType = "true".equals(attributes.get("simpleType"));
        this.name = attributes.get("name");
        this.fields = new ArrayList<>(2);
    }

    @Override
    void addChild(Element e) {
        if (e instanceof JfrField) {
            fields.add((JfrField) e);
        }
    }

    public JfrField field(String name) {
        for (JfrField field : fields) {
            if (field.name.equals(name)) {
                return field;
            }
        }
        return null;
    }
}


================================================
FILE: src\converter\one\jfr\JfrField.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package one.jfr;

import java.util.Map;

public class JfrField extends Element {
    final String name;
    final int type;
    final boolean constantPool;

    JfrField(Map<String, String> attributes) {
        this.name = attributes.get("name");
        this.type = Integer.parseInt(attributes.get("class"));
        this.constantPool = "true".equals(attributes.get("constantPool"));
    }
}


================================================
FILE: src\converter\one\jfr\JfrReader.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package one.jfr;

import one.jfr.event.*;

import java.io.Closeable;
import java.io.IOException;
import java.lang.reflect.Constructor;
import java.nio.ByteBuffer;
import java.nio.ByteOrder;
import java.nio.channels.FileChannel;
import java.nio.charset.StandardCharsets;
import java.nio.file.Paths;
import java.nio.file.StandardOpenOption;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * Parses JFR output produced by async-profiler.
 */
public class JfrReader implements Closeable {
    private static final int BUFFER_SIZE = 2 * 1024 * 1024;
    private static final int CHUNK_HEADER_SIZE = 68;
    private static final int CHUNK_SIGNATURE = 0x464c5200;

    private static final byte STATE_NEW_CHUNK = 0;
    private static final byte STATE_READING = 1;
    private static final byte STATE_EOF = 2;
    private static final byte STATE_INCOMPLETE = 3;

    private final FileChannel ch;
    private ByteBuffer buf;
    private final long fileSize;
    private long filePosition;
    private byte state;

    public long startNanos = Long.MAX_VALUE;
    public long endNanos = Long.MIN_VALUE;
    public long startTicks = Long.MAX_VALUE;
    public long chunkStartNanos;
    public long chunkEndNanos;
    public long chunkStartTicks;
    public long ticksPerSec;
    public double nanosPerTick;
    public boolean stopAtNewChunk;

    public final Dictionary<JfrClass> types = new Dictionary<>();
    public final Map<String, JfrClass> typesByName = new HashMap<>();
    public final Dictionary<String> threads = new Dictionary<>();
    public final Dictionary<Long> javaThreads = new Dictionary<>();
    public final Dictionary<ClassRef> classes = new Dictionary<>();
    public final Dictionary<String> strings = new Dictionary<>();
    public final Dictionary<byte[]> symbols = new Dictionary<>();
    public final Dictionary<MethodRef> methods = new Dictionary<>();
    public final Dictionary<StackTrace> stackTraces = new Dictionary<>();
    public final Map<String, String> settings = new HashMap<>();
    public final Map<String, Map<Integer, String>> enums = new HashMap<>();

    private final Dictionary<Constructor<? extends Event>> customEvents = new Dictionary<>();

    private int executionSample;
    private int nativeMethodSample;
    private int wallClockSample;
    private int methodTrace;
    private int allocationInNewTLAB;
    private int allocationOutsideTLAB;
    private int allocationSample;
    private int liveObject;
    private int monitorEnter;
    private int threadPark;
    private int activeSetting;
    private int malloc;
    private int free;
    private int cpuTimeSample;
    private int nativeLock;
    private boolean hasWallTimeSpan;

    public JfrReader(String fileName) throws IOException {
        this.ch = FileChannel.open(Paths.get(fileName), StandardOpenOption.READ);
        this.buf = ByteBuffer.allocateDirect(BUFFER_SIZE);
        this.fileSize = ch.size();

        buf.flip();
        ensureBytes(CHUNK_HEADER_SIZE);
        if (!readChunk(0)) {
            throw new IOException("Incomplete JFR file");
        }
    }

    public JfrReader(ByteBuffer buf) throws IOException {
        this.ch = null;
        this.buf = buf;
        this.fileSize = buf.limit();

        buf.order(ByteOrder.BIG_ENDIAN);
        if (!readChunk(0)) {
            throw new IOException("Incomplete JFR file");
        }
    }

    @Override
    public void close() throws IOException {
        if (ch != null) {
            ch.close();
        }
    }

    public boolean eof() {
        return state >= STATE_EOF;
    }

    public boolean incomplete() {
        return state == STATE_INCOMPLETE;
    }

    public long durationNanos() {
        return endNanos - startNanos;
    }

    public long chunkDurationNanos() {
        return chunkEndNanos - chunkStartNanos;
    }

    public <E extends Event> void registerEvent(String name, Class<E> eventClass) {
        JfrClass type = typesByName.get(name);
        if (type != null) {
            try {
                customEvents.put(type.id, eventClass.getConstructor(JfrReader.class));
            } catch (NoSuchMethodException e) {
                throw new IllegalArgumentException("No suitable constructor found");
            }
        }
    }

    // Similar to eof(), but parses the next chunk header
    public boolean hasMoreChunks() throws IOException {
        return state == STATE_NEW_CHUNK ? readChunk(buf.position()) : state == STATE_READING;
    }

    public List<Event> readAllEvents() throws IOException {
        return readAllEvents(null);
    }

    public <E extends Event> List<E> readAllEvents(Class<E> cls) throws IOException {
        ArrayList<E> events = new ArrayList<>();
        for (E event; (event = readEvent(cls)) != null; ) {
            events.add(event);
        }
        Collections

================================================
FILE: src\converter\one\jfr\MethodRef.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package one.jfr;

public class MethodRef {
    public final long cls;
    public final long name;
    public final long sig;

    public MethodRef(long cls, long name, long sig) {
        this.cls = cls;
        this.name = name;
        this.sig = sig;
    }
}


================================================
FILE: src\converter\one\jfr\StackTrace.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package one.jfr;

public class StackTrace {
    public final long[] methods;
    public final byte[] types;
    public final int[] locations;

    public StackTrace(long[] methods, byte[] types, int[] locations) {
        this.methods = methods;
        this.types = types;
        this.locations = locations;
    }
}


================================================
FILE: src\converter\one\jfr\event\AllocationSample.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package one.jfr.event;

public class AllocationSample extends Event {
    public final int classId;
    public final long allocationSize;
    public final long tlabSize;

    public AllocationSample(long time, int tid, int stackTraceId, int classId, long allocationSize, long tlabSize) {
        super(time, tid, stackTraceId);
        this.classId = classId;
        this.allocationSize = allocationSize;
        this.tlabSize = tlabSize;
    }

    @Override
    public int hashCode() {
        return classId * 127 + stackTraceId + (tlabSize == 0 ? 17 : 0);
    }

    @Override
    public boolean sameGroup(Event o) {
        if (o instanceof AllocationSample) {
            AllocationSample a = (AllocationSample) o;
            return classId == a.classId && (tlabSize == 0) == (a.tlabSize == 0);
        }
        return false;
    }

    @Override
    public long classId() {
        return classId;
    }

    @Override
    public long value() {
        return tlabSize != 0 ? tlabSize : allocationSize;
    }
}


================================================
FILE: src\converter\one\jfr\event\ContendedLock.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package one.jfr.event;

public class ContendedLock extends Event {
    public final long duration;
    public final int classId;

    public ContendedLock(long time, int tid, int stackTraceId, long duration, int classId) {
        super(time, tid, stackTraceId);
        this.duration = duration;
        this.classId = classId;
    }

    @Override
    public int hashCode() {
        return classId * 127 + stackTraceId;
    }

    @Override
    public boolean sameGroup(Event o) {
        if (o instanceof ContendedLock) {
            ContendedLock c = (ContendedLock) o;
            return classId == c.classId;
        }
        return false;
    }

    @Override
    public long classId() {
        return classId;
    }

    @Override
    public long value() {
        return duration;
    }
}


================================================
FILE: src\converter\one\jfr\event\CPULoad.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package one.jfr.event;

import one.jfr.JfrReader;

public class CPULoad extends Event {
    public final float jvmUser;
    public final float jvmSystem;
    public final float machineTotal;

    public CPULoad(JfrReader jfr) {
        super(jfr.getVarlong(), 0, 0);
        this.jvmUser = jfr.getFloat();
        this.jvmSystem = jfr.getFloat();
        this.machineTotal = jfr.getFloat();
    }
}


================================================
FILE: src\converter\one\jfr\event\Event.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package one.jfr.event;

import java.lang.reflect.Field;

public abstract class Event implements Comparable<Event> {
    public final long time;
    public final int tid;
    public final int stackTraceId;

    protected Event(long time, int tid, int stackTraceId) {
        this.time = time;
        this.tid = tid;
        this.stackTraceId = stackTraceId;
    }

    @Override
    public int compareTo(Event o) {
        return Long.compare(time, o.time);
    }

    @Override
    public int hashCode() {
        return stackTraceId;
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder(getClass().getSimpleName())
                .append("{time=").append(time)
                .append(",tid=").append(tid)
                .append(",stackTraceId=").append(stackTraceId);
        for (Field f : getClass().getDeclaredFields()) {
            try {
                sb.append(',').append(f.getName()).append('=').append(f.get(this));
            } catch (ReflectiveOperationException e) {
                break;
            }
        }
        return sb.append('}').toString();
    }

    public boolean sameGroup(Event o) {
        return getClass() == o.getClass();
    }

    public long classId() {
        return 0;
    }

    public long samples() {
        return 1;
    }

    public long value() {
        return 1;
    }
}


================================================
FILE: src\converter\one\jfr\event\EventAggregator.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package one.jfr.event;

public class EventAggregator implements EventCollector {
    private static final int INITIAL_CAPACITY = 1024;

    private final boolean threads;
    private final double grain;
    private Event[] keys;
    private long[] samples;
    private long[] values;
    private int size;
    private double fraction;

    public EventAggregator(boolean threads, double grain) {
        this.threads = threads;
        this.grain = grain;

        beforeChunk();
    }

    public int size() {
        return size;
    }

    @Override
    public void collect(Event e) {
        collect(e, e.samples(), e.value());
    }

    public void collect(Event e, long samples, long value) {
        int mask = keys.length - 1;
        int i = hashCode(e) & mask;
        while (keys[i] != null) {
            if (sameGroup(keys[i], e)) {
                this.samples[i] += samples;
                this.values[i] += value;
                return;
            }
            i = (i + 1) & mask;
        }

        this.keys[i] = e;
        this.samples[i] = samples;
        this.values[i] = value;

        if (++size * 2 > keys.length) {
            resize(keys.length * 2);
        }
    }

    @Override
    public void beforeChunk() {
        if (keys == null || size > 0) {
            keys = new Event[INITIAL_CAPACITY];
            samples = new long[INITIAL_CAPACITY];
            values = new long[INITIAL_CAPACITY];
            size = 0;
        }
    }

    @Override
    public void afterChunk() {
        if (grain > 0) {
            coarsen(grain);
        }
    }

    @Override
    public boolean finish() {
        keys = null;
        samples = null;
        values = null;
        return false;
    }

    @Override
    public void forEach(Visitor visitor) {
        if (size > 0) {
            for (int i = 0; i < keys.length; i++) {
                if (keys[i] != null) {
                    visitor.visit(keys[i], samples[i], values[i]);
                }
            }
        }
    }

    public void coarsen(double grain) {
        fraction = 0;

        for (int i = 0; i < keys.length; i++) {
            if (keys[i] != null) {
                long s0 = samples[i];
                long s1 = round(s0 / grain);
                if (s1 == 0) {
                    keys[i] = null;
                    size--;
                }
                samples[i] = s1;
                values[i] = (long) (values[i] * ((double) s1 / s0));
            }
        }
    }

    private long round(double d) {
        long r = (long) d;
        if ((fraction += d - r) >= 1.0) {
            fraction -= 1.0;
            r++;
        }
        return r;
    }

    private int hashCode(Event e) {
        return e.hashCode() + (threads ? e.tid * 31 : 0);
    }

    private boolean sameGroup(Event e1, Event e2) {
        return e1.stackTraceId == e2.stackTraceId && (!threads || e1.tid == e2.tid) && e1.sameGroup(e2);
    }

    private void resize(int newCapacity) {
        Event[] newKeys = new Event[newCapacity];
        long[] newSamples = new long[newCapacity];
        long[] newValues = new long[newCapacity];
        int mask = newKeys.length - 1;

        for (int i = 0; i < keys.length; i++) {
            if (keys[i] != null) {
                for (int j = hashCode(keys[i]) & mask; ; j = (j + 1) & mask) {
                    if (newKeys[j] == null) {
                        newKeys[j] = keys[i];
                        newSamples[j] = samples[i];
                        newValues[j] = values[i];
                        break;
                    }
                }
            }
        }

        keys = newKeys;
        samples = newSamples;
        values = newValues;
    }
}


================================================
FILE: src\converter\one\jfr\event\EventCollector.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package one.jfr.event;

public interface EventCollector {

    void collect(Event e);

    void beforeChunk();

    void afterChunk();

    // Returns true if this collector has remaining data to process
    boolean finish();

    void forEach(Visitor visitor);

    interface Visitor {
        void visit(Event event, long samples, long value);
    }
}


================================================
FILE: src\converter\one\jfr\event\ExecutionSample.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package one.jfr.event;

public class ExecutionSample extends Event {
    // Synthetic thread state to distinguish samples converted from jdk.CPUTimeSample event.
    // A small constant suitable for BitSet, does not clash with any existing thread state.
    public static final int CPU_TIME_SAMPLE = 254;

    public final int threadState;
    public final int samples;

    public ExecutionSample(long time, int tid, int stackTraceId, int threadState, int samples) {
        super(time, tid, stackTraceId);
        this.threadState = threadState;
        this.samples = samples;
    }

    @Override
    public long samples() {
        return samples;
    }

    @Override
    public long value() {
        return samples;
    }
}


================================================
FILE: src\converter\one\jfr\event\GCHeapSummary.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package one.jfr.event;

import one.jfr.JfrReader;

public class GCHeapSummary extends Event {
    public final int gcId;
    public final boolean afterGC;
    public final long committed;
    public final long reserved;
    public final long used;

    public GCHeapSummary(JfrReader jfr) {
        super(jfr.getVarlong(), 0, 0);
        this.gcId = jfr.getVarint();
        this.afterGC = jfr.getVarint() > 0;
        long start = jfr.getVarlong();
        long committedEnd = jfr.getVarlong();
        this.committed = jfr.getVarlong();
        long reservedEnd = jfr.getVarlong();
        this.reserved = jfr.getVarlong();
        this.used = jfr.getVarlong();
    }
}


================================================
FILE: src\converter\one\jfr\event\LiveObject.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package one.jfr.event;

public class LiveObject extends Event {
    public final int classId;
    public final long allocationSize;
    public final long allocationTime;

    public LiveObject(long time, int tid, int stackTraceId, int classId, long allocationSize, long allocationTime) {
        super(time, tid, stackTraceId);
        this.classId = classId;
        this.allocationSize = allocationSize;
        this.allocationTime = allocationTime;
    }

    @Override
    public int hashCode() {
        return classId * 127 + stackTraceId;
    }

    @Override
    public boolean sameGroup(Event o) {
        if (o instanceof LiveObject) {
            LiveObject a = (LiveObject) o;
            return classId == a.classId;
        }
        return false;
    }

    @Override
    public long classId() {
        return classId;
    }

    @Override
    public long value() {
        return allocationSize;
    }
}


================================================
FILE: src\converter\one\jfr\event\MallocEvent.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package one.jfr.event;

public class MallocEvent extends Event {
    public final long address;
    public final long size;

    public MallocEvent(long time, int tid, int stackTraceId, long address, long size) {
        super(time, tid, stackTraceId);
        this.address = address;
        this.size = size;
    }

    @Override
    public long value() {
        return size;
    }
}


================================================
FILE: src\converter\one\jfr\event\MallocLeakAggregator.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package one.jfr.event;

import java.util.List;
import java.util.ArrayList;
import java.util.Map;
import java.util.HashMap;

public class MallocLeakAggregator implements EventCollector {
    private final EventCollector wrapped;
    private final double tail;
    private final Map<Long, MallocEvent> addresses;
    private List<MallocEvent> events;
    private long minTime = Long.MAX_VALUE;
    private long maxTime = Long.MIN_VALUE;

    public MallocLeakAggregator(EventCollector wrapped, double tail) {
        if (tail < 0.0 || tail > 1.0) {
            throw new IllegalArgumentException("tail must be between 0 and 1");
        }
        this.wrapped = wrapped;
        this.tail = tail;
        this.addresses = new HashMap<>();
    }

    @Override
    public void collect(Event e) {
        events.add((MallocEvent) e);
        minTime = Math.min(minTime, e.time);
        maxTime = Math.max(maxTime, e.time);
    }

    @Override
    public void beforeChunk() {
        events = new ArrayList<>();
    }

    @Override
    public void afterChunk() {
        events.sort(null);

        for (MallocEvent e : events) {
            if (e.size > 0) {
                addresses.put(e.address, e);
            } else {
                addresses.remove(e.address);
            }
        }

        events = null;
    }

    @Override
    public boolean finish() {
        // Ignore tail allocations made in the last N% of profiling session:
        // they are too young to be considered a leak
        long timeCutoff = (long) (minTime * tail + maxTime * (1.0 - tail));

        wrapped.beforeChunk();
        for (Event e : addresses.values()) {
            if (e.time <= timeCutoff) {
                wrapped.collect(e);
            }
        }
        wrapped.afterChunk();

        // Free memory before the final conversion
        addresses.clear();
        return true;
    }

    @Override
    public void forEach(Visitor visitor) {
        wrapped.forEach(visitor);
    }
}


================================================
FILE: src\converter\one\jfr\event\MethodTrace.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package one.jfr.event;

public class MethodTrace extends Event {
    public final int method;
    public final long duration;

    public MethodTrace(long time, int tid, int stackTraceId, int method, long duration) {
        super(time, tid, stackTraceId);
        this.method = method;
        this.duration = duration;
    }

    @Override
    public int hashCode() {
        return method * 127 + stackTraceId;
    }

    @Override
    public boolean sameGroup(Event o) {
        if (o instanceof MethodTrace) {
            MethodTrace c = (MethodTrace) o;
            return method == c.method;
        }
        return false;
    }

    @Override
    public long value() {
        return duration;
    }
}


================================================
FILE: src\converter\one\jfr\event\NativeLockEvent.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package one.jfr.event;

public class NativeLockEvent extends Event {
    public final long address;
    public final long duration;

    public NativeLockEvent(long time, int tid, int stackTraceId, long address, long duration) {
        super(time, tid, stackTraceId);
        this.address = address;
        this.duration = duration;
    }

    @Override
    public long value() {
        return duration;
    }
}


================================================
FILE: src\converter\one\jfr\event\ObjectCount.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package one.jfr.event;

import one.jfr.JfrReader;

public class ObjectCount extends Event {
    public final int gcId;
    public final int classId;
    public final long count;
    public final long totalSize;

    public ObjectCount(JfrReader jfr) {
        super(jfr.getVarlong(), 0, 0);
        this.gcId = jfr.getVarint();
        this.classId = jfr.getVarint();
        this.count = jfr.getVarlong();
        this.totalSize = jfr.getVarlong();
    }
}


================================================
FILE: src\converter\one\jfr\event\ProcessSample.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package one.jfr.event;

import one.jfr.JfrReader;

public class ProcessSample extends Event {
    public final int pid;
    public final int ppid;
    public final String name;
    public final String cmdLine;
    public final int uid;
    public final byte state;
    public final long processStartTime;
    public final float cpuUser;
    public final float cpuSystem;
    public final float cpuPercent;
    public final int threads;
    public final long vmSize;
    public final long vmRss;
    public final long rssAnon;
    public final long rssFiles;
    public final long rssShmem;
    public final long minorFaults;
    public final long majorFaults;
    public final long ioRead;
    public final long ioWrite;

    public ProcessSample(JfrReader jfr) {
        super(jfr.getVarlong(), 0, 0);
        this.pid = jfr.getVarint();
        this.ppid = jfr.getVarint();
        this.name = jfr.getString();
        this.cmdLine = jfr.getString();
        this.uid = jfr.getVarint();
        this.state = jfr.getByte();
        this.processStartTime = jfr.getVarlong();
        this.cpuUser = jfr.getFloat();
        this.cpuSystem = jfr.getFloat();
        this.cpuPercent = jfr.getFloat();
        this.threads = jfr.getVarint();
        this.vmSize = jfr.getVarlong();
        this.vmRss = jfr.getVarlong();
        this.rssAnon = jfr.getVarlong();
        this.rssFiles = jfr.getVarlong();
        this.rssShmem = jfr.getVarlong();
        this.minorFaults = jfr.getVarlong();
        this.majorFaults = jfr.getVarlong();
        this.ioRead = jfr.getVarlong();
        this.ioWrite = jfr.getVarlong();
    }
}


================================================
FILE: src\converter\one\proto\Proto.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package one.proto;

import java.nio.charset.StandardCharsets;
import java.util.Arrays;

/**
 * Simplified implementation of Protobuf writer, capable of encoding
 * varints, doubles, ASCII strings and embedded messages
 */
public class Proto {
    private byte[] buf;
    private int pos;

    public Proto(int capacity) {
        this.buf = new byte[capacity];
    }

    public byte[] buffer() {
        return buf;
    }

    public int size() {
        return pos;
    }

    public void reset() {
        pos = 0;
    }

    public Proto field(int index, int n) {
        tag(index, 0);
        writeInt(n);
        return this;
    }

    public Proto field(int index, long n) {
        tag(index, 0);
        writeLong(n);
        return this;
    }

    public Proto fieldFixed64(int index, long n) {
        tag(index, 1);
        writeFixed64(n);
        return this;
    }

    public Proto field(int index, double d) {
        tag(index, 1);
        writeDouble(d);
        return this;
    }

    public Proto field(int index, String s) {
        tag(index, 2);
        byte[] bytes = s.getBytes(StandardCharsets.UTF_8);
        writeBytes(bytes, 0, bytes.length);
        return this;
    }

    public Proto field(int index, byte[] bytes) {
        tag(index, 2);
        writeBytes(bytes, 0, bytes.length);
        return this;
    }

    public Proto field(int index, Proto proto) {
        tag(index, 2);
        writeBytes(proto.buf, 0, proto.pos);
        return this;
    }

    // 32 bits for the start position
    // 32 bits for the max length byte count
    public long startField(int index, int maxLenByteCount) {
        tag(index, 2);
        ensureCapacity(maxLenByteCount);
        pos += maxLenByteCount;
        return ((long) pos << 32) | maxLenByteCount;
    }

    public void commitField(long mark) {
        int messageStart = (int) (mark >> 32);
        int maxLenByteCount = (int) mark;

        int actualLength = pos - messageStart;
        if (actualLength >= 1L << (7 * maxLenByteCount)) {
            throw new IllegalArgumentException("Field too large");
        }

        int lenBytesStart = messageStart - maxLenByteCount;
        for (int i = 0; i < maxLenByteCount - 1; ++i) {
            buf[lenBytesStart + i] = (byte) (0x80 | actualLength);
            actualLength >>>= 7;
        }
        buf[lenBytesStart + maxLenByteCount - 1] = (byte) actualLength;
    }

    public void writeInt(int n) {
        int length = n == 0 ? 1 : (38 - Integer.numberOfLeadingZeros(n)) / 7;
        ensureCapacity(length);

        while ((n >>> 7) != 0) {
            buf[pos++] = (byte) (0x80 | (n & 0x7f));
            n >>>= 7;
        }
        buf[pos++] = (byte) n;
    }

    public void writeLong(long n) {
        int length = n == 0 ? 1 : (70 - Long.numberOfLeadingZeros(n)) / 7;
        ensureCapacity(length);

        while ((n >>> 7) != 0) {
            buf[pos++] = (byte) (0x80 | (n & 0x7f));
            n >>>= 7;
        }
        buf[pos++] = (byte) n;
    }

    public void writeDouble(double d) {
        writeFixed64(Double.doubleToRawLongBits(d));
    }

    public void writeFixed64(long n) {
        ensureCapacity(8);
        buf[pos] = (byte) n;
        buf[pos + 1] = (byte) (n >>> 8);
        buf[pos + 2] = (byte) (n >>> 16);
        buf[pos + 3] = (byte) (n >>> 24);
        buf[pos + 4] = (byte) (n >>> 32);
        buf[pos + 5] = (byte) (n >>> 40);
        buf[pos + 6] = (byte) (n >>> 48);
        buf[pos + 7] = (byte) (n >>> 56);
        pos += 8;
    }

    public void writeBytes(byte[] bytes, int offset, int length) {
        writeInt(length);
        ensureCapacity(length);
        System.arraycopy(bytes, offset, buf, pos, length);
        pos += length;
    }

    private void tag(int index, int type) {
        ensureCapacity(1);
        buf[pos++] = (byte) (index << 3 | type);
    }

    private void ensureCapacity(int length) {
        if (pos + length > buf.length) {
            int newLength = buf.length * 2;
            buf = Arrays.copyOf(buf, newLength < 0 ? 0x7ffffff0 : Math.max(newLength, pos + length));
        }
    }
}


================================================
FILE: src\helper\one\profiler\Instrument.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package one.profiler;

/**
 * Instrumentation helper for Java method profiling.
 */
public class Instrument {

    private Instrument() {
    }

    public static native void recordEntry();

    public static void recordExit(long startTimeNs, long minLatency) {
        if (System.nanoTime() - startTimeNs >= minLatency) {
            recordExit0(startTimeNs);
        }
    }

    // Overload used when latency=0, we don't call recordExit0
    // directly to have the same number of additional frames as
    // the standard path.
    public static void recordExit(long startTimeNs) {
        recordExit0(startTimeNs);
    }

    public static native void recordExit0(long startTimeNs);
}


================================================
FILE: src\helper\one\profiler\JfrSync.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package one.profiler;

import jdk.jfr.Configuration;
import jdk.jfr.FlightRecorder;
import jdk.jfr.FlightRecorderListener;
import jdk.jfr.Recording;
import jdk.jfr.RecordingState;

import java.io.IOException;
import java.nio.file.NoSuchFileException;
import java.nio.file.Paths;
import java.text.ParseException;
import java.util.StringTokenizer;

/**
 * Synchronize async-profiler recording with an existing JFR recording.
 */
class JfrSync implements FlightRecorderListener {
    // Keep in sync with EventMask
    private static final int EM_CPU            = 1;
    private static final int EM_ALLOC          = 2;
    private static final int EM_LOCK           = 4;

    // Keep in sync with EVENT_MASK_SIZE in C++
    private static final int EVENT_MASK_SIZE = 7;

    // Keep in sync with JfrOption
    private static final int NO_SYSTEM_INFO  = 1;
    private static final int NO_SYSTEM_PROPS = 2;
    private static final int NO_NATIVE_LIBS  = 4;
    private static final int NO_CPU_LOAD     = 8;
    private static final int NO_HEAP_SUMMARY = 16;

    private static volatile Recording masterRecording;

    private JfrSync() {
    }

    static {
        FlightRecorder.addListener(new JfrSync());
    }

    @Override
    public void recordingStateChanged(Recording recording) {
        if (recording == masterRecording && recording.getState() == RecordingState.STOPPED) {
            masterRecording = null;
            stopProfiler();
        }
    }

    public static void start(String fileName, String settings, int eventMask) throws IOException, ParseException {
        Recording recording;
        if (settings.startsWith("+")) {
            recording = new Recording();
            for (StringTokenizer st = new StringTokenizer(settings, "+"); st.hasMoreTokens(); ) {
                recording.enable(st.nextToken());
            }
        } else {
            try {
                recording = new Recording(Configuration.getConfiguration(settings));
            } catch (NoSuchFileException e) {
                recording = new Recording(Configuration.create(Paths.get(settings)));
            }
            disableBuiltinEvents(recording, eventMask);
        }

        masterRecording = recording;

        recording.setDestination(Paths.get(fileName));
        recording.setToDisk(true);
        recording.setDumpOnExit(true);
        recording.start();
    }

    public static void stop() {
        Recording recording = masterRecording;
        if (recording != null) {
            // Disable state change notification before stopping
            masterRecording = null;
            recording.stop();
        }
    }

    private static void disableBuiltinEvents(Recording recording, int eventMask) {
        if ((eventMask & EM_CPU) != 0) {
            recording.disable("jdk.ExecutionSample");
            recording.disable("jdk.NativeMethodSample");
        }
        if ((eventMask & EM_ALLOC) != 0) {
            recording.disable("jdk.ObjectAllocationInNewTLAB");
            recording.disable("jdk.ObjectAllocationOutsideTLAB");
            recording.disable("jdk.ObjectAllocationSample");
            recording.disable("jdk.OldObjectSample");
        }
        if ((eventMask & EM_LOCK) != 0) {
            recording.disable("jdk.JavaMonitorEnter");
            recording.disable("jdk.ThreadPark");
        }
        // No built-in event related to EM_WALL
        // No built-in event related to EM_NATIVEMEM
        // No built-in event related to EM_NATIVELOCK
        // No need to disable built-in event related to EM_METHOD_TRACE

        eventMask >>>= EVENT_MASK_SIZE;
        // Shifted JfrOption values
        if ((eventMask & NO_SYSTEM_INFO) != 0) {
            recording.disable("jdk.OSInformation");
            recording.disable("jdk.CPUInformation");
            recording.disable("jdk.JVMInformation");
        }
        if ((eventMask & NO_SYSTEM_PROPS) != 0) {
            recording.disable("jdk.InitialSystemProperty");
        }
        if ((eventMask & NO_NATIVE_LIBS) != 0) {
            recording.disable("jdk.NativeLibrary");
        }
        if ((eventMask & NO_CPU_LOAD) != 0) {
            recording.disable("jdk.CPULoad");
        }
        if ((eventMask & NO_HEAP_SUMMARY) != 0) {
            recording.disable("jdk.GCHeapSummary");
        }
    }

    private static native void stopProfiler();

    // JNI helper
    static Integer box(int n) {
        return n;
    }
}


================================================
FILE: src\helper\one\profiler\LockTracer.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package one.profiler;

/**
 * Helper class to call JNI RegisterNatives in a trusted context.
 */
class LockTracer {

    private LockTracer() {
    }

    // Workaround for JDK-8238460: we need to construct at least two frames
    // belonging to the bootstrap class loader for RegisterNatives not to emit a warning.
    static void setEntry(long entry) {
        setEntry0(entry);
    }

    private static native void setEntry0(long entry);
}


================================================
FILE: src\helper\one\profiler\Server.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package one.profiler;

import com.sun.net.httpserver.HttpExchange;
import com.sun.net.httpserver.HttpHandler;
import com.sun.net.httpserver.HttpServer;

import java.io.IOException;
import java.net.InetSocketAddress;
import java.net.URI;
import java.nio.charset.StandardCharsets;
import java.util.concurrent.Executor;
import java.util.concurrent.atomic.AtomicInteger;

class Server extends Thread implements Executor, HttpHandler {
    private static final String[] COMMANDS = "start,resume,stop,dump,check,status,metrics,list,version".split(",");

    private final HttpServer server;
    private final AtomicInteger threadNum = new AtomicInteger();

    private Server(String address) throws IOException {
        super("Async-profiler Server");
        setDaemon(true);

        int p = address.lastIndexOf(':');
        InetSocketAddress socketAddress = p >= 0
                ? new InetSocketAddress(address.substring(0, p), Integer.parseInt(address.substring(p + 1)))
                : new InetSocketAddress(Integer.parseInt(address));

        server = HttpServer.create(socketAddress, 0);
        server.createContext("/", this);
        server.setExecutor(this);
    }

    public static void start(String address) throws IOException {
        new Server(address).start();
    }

    @Override
    public void run() {
        server.start();
    }

    @Override
    public void execute(Runnable command) {
        Thread t = new Thread(command, "Async-profiler Request #" + threadNum.incrementAndGet());
        t.setDaemon(false);
        t.start();
    }

    @Override
    public void handle(HttpExchange exchange) throws IOException {
        try {
            String command = getCommand(exchange.getRequestURI());
            if (command == null) {
                sendResponse(exchange, 404, "Unknown command");
            } else if (command.isEmpty()) {
                sendResponse(exchange, 200, "Async-profiler server");
            } else {
                String response = execute0(command);
                sendResponse(exchange, 200, response);
            }
        } catch (IllegalArgumentException e) {
            sendResponse(exchange, 400, e.getMessage());
        } catch (Exception e) {
            sendResponse(exchange, 500, e.getMessage());
        } finally {
            exchange.close();
        }
    }

    private String getCommand(URI uri) {
        String path = uri.getPath();
        if (path.startsWith("/")) {
            if ((path = path.substring(1)).isEmpty()) {
                return "";
            }
            for (String command : COMMANDS) {
                if (path.startsWith(command)) {
                    String query = uri.getQuery();
                    return query == null ? path : path + ',' + query.replace('&', ',');
                }
            }
        }
        return null;
    }

    private void sendResponse(HttpExchange exchange, int code, String body) throws IOException {
        String contentType = body.startsWith("<!DOCTYPE html>") ? "text/html; charset=utf-8" : "text/plain";
        exchange.getResponseHeaders().add("Content-Type", contentType);

        byte[] bodyBytes = body.getBytes(StandardCharsets.UTF_8);
        exchange.sendResponseHeaders(code, bodyBytes.length);
        exchange.getResponseBody().write(bodyBytes);
    }

    private native String execute0(String command) throws IllegalArgumentException, IllegalStateException, IOException;
}


================================================
FILE: test\one\profiler\test\Arch.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package one.profiler.test;

public enum Arch {
    X64,
    X86,
    ARM64,
    ARM32,
    PPC64LE,
    RISCV64,
    LOONGARCH64
}


================================================
FILE: test\one\profiler\test\Assert.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package one.profiler.test;

import java.util.function.BiPredicate;
import java.util.logging.Level;
import java.util.logging.Logger;

public class Assert {
    enum Comparison {
        GT(">", (a, b) -> a > b),
        GTE(">=", (a, b) -> a >= b),
        LT("<", (a, b) -> a < b),
        LTE("<=", (a, b) -> a <= b),
        EQ("==", Double::equals),
        NE("!=", (a, b) -> !Double.isNaN(a) && !Double.isNaN(b) && !a.equals(b));

        public final String operator;
        public final BiPredicate<Double, Double> comparator;

        Comparison(String operator, BiPredicate<Double, Double> comparator) {
            this.operator = operator;
            this.comparator = comparator;
        }
    }

    private static final Logger log = Logger.getLogger(Assert.class.getName());

    private static void assertComparison(Comparison comparison, double left, double right, @SuppressWarnings("unused") String message) {
        boolean asserted = !comparison.comparator.test(left, right);

        // message parameter will be part of the source code line.
        String assertionMessage = String.format("%s %s %s\n%s", left, comparison.operator, right, SourceCode.tryGet(2));
        log.log(Level.FINE, String.format("isAsserted %s: %s", asserted, assertionMessage));
        if (asserted) {
            throw new AssertionError("Expected " + assertionMessage);
        }
    }

    public static void isEqual(double left, double right) {
        assertComparison(Comparison.EQ, left, right, null);
    }

    public static void isEqual(double left, double right, String message) {
        assertComparison(Comparison.EQ, left, right, message);
    }

    public static void isNotEqual(double left, double right) {
        assertComparison(Comparison.NE, left, right, null);
    }

    public static void isNotEqual(double left, double right, String message) {
        assertComparison(Comparison.NE, left, right, message);
    }

    public static void isGreater(double left, double right) {
        assertComparison(Comparison.GT, left, right, null);
    }

    public static void isGreater(double left, double right, String message) {
        assertComparison(Comparison.GT, left, right, message);
    }

    public static void isGreaterOrEqual(double left, double right) {
        assertComparison(Comparison.GTE, left, right, null);
    }

    public static void isGreaterOrEqual(double left, double right, String message) {
        assertComparison(Comparison.GTE, left, right, message);
    }

    public static void isLess(double left, double right) {
        assertComparison(Comparison.LT, left, right, null);
    }

    public static void isLess(double left, double right, String message) {
        assertComparison(Comparison.LT, left, right, message);
    }

    public static void isLessOrEqual(double left, double right) {
        assertComparison(Comparison.LTE, left, right, null);
    }

    public static void isLessOrEqual(double left, double right, String message) {
        assertComparison(Comparison.LTE, left, right, message);
    }
}


================================================
FILE: test\one\profiler\test\Jvm.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package one.profiler.test;

public enum Jvm {
    HOTSPOT,
    HOTSPOT_C2,
    ZING,
    OPENJ9
}


================================================
FILE: test\one\profiler\test\Os.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package one.profiler.test;

public enum Os {
    LINUX,
    MACOS,
    WINDOWS;

    public String getLibExt() {
        switch (this) {
            case LINUX:
                return "so";
            case MACOS:
                return "dylib";
            case WINDOWS:
                return "dll";
            default:
                throw new AssertionError();
        }
    }
}


================================================
FILE: test\one\profiler\test\Output.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package one.profiler.test;

import one.convert.Arguments;
import one.convert.FlameGraph;
import one.convert.JfrToFlame;

import java.io.*;
import java.util.Arrays;
import java.util.regex.Pattern;
import java.util.stream.Stream;

public class Output {
    private final String[] lines;

    public Output(String[] lines) {
        this.lines = lines;
    }

    @Override
    public String toString() {
        return String.join("\n", lines);
    }

    public Stream<String> stream() {
        return Arrays.stream(lines);
    }

    public Stream<String> stream(String regex) {
        Pattern pattern = Pattern.compile(regex);
        return Arrays.stream(lines).filter(s -> pattern.matcher(s).find());
    }

    public boolean contains(String regex) {
        return stream(regex).findAny().isPresent();
    }

    public boolean containsExact(String string) {
        return stream().anyMatch(s -> s.contains(string));
    }

    public long samples(String regex) {
        return stream(regex).mapToLong(Output::extractSamples).sum();
    }

    public long total() {
        return stream().mapToLong(Output::extractSamples).sum();
    }

    public double ratio(String regex) {
        long total = 0;
        long matched = 0;
        Pattern pattern = Pattern.compile(regex);

        for (String s : lines) {
            long samples = extractSamples(s);
            total += samples;
            matched += pattern.matcher(s).find() ? samples : 0;
        }
        return (double) matched / total;
    }

    public Output convertFlameToCollapsed() throws IOException {
        FlameGraph fg = new FlameGraph(new Arguments("-o", "collapsed"));
        try (StringReader in = new StringReader(toString())) {
            fg.parseHtml(in);
        }

        try (ByteArrayOutputStream outputStream = new ByteArrayOutputStream()) {
            fg.dump(outputStream);
            return new Output(outputStream.toString("UTF-8").split(System.lineSeparator()));
        }
    }

    public static Output convertJfrToCollapsed(String input, String... args) throws IOException {
        Arguments arguments = new Arguments(args);
        arguments.output = "collapsed";
        FlameGraph fg = JfrToFlame.parse(input, arguments);

        try (ByteArrayOutputStream outputStream = new ByteArrayOutputStream()) {
            fg.dump(outputStream);
            return new Output(outputStream.toString("UTF-8").split(System.lineSeparator()));
        }
    }

    public Output filter(String regex) {
        return new Output(stream(regex).toArray(String[]::new));
    }

    private static long extractSamples(String s) {
        return Long.parseLong(s.substring(s.lastIndexOf(' ') + 1));
    }
}


================================================
FILE: test\one\profiler\test\RunnableTest.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package one.profiler.test;

import java.lang.reflect.Method;

public class RunnableTest {
    private final Method m;
    private final Test test;

    RunnableTest(Method m, Test test) {
        this.m = m;
        this.test = test;
    }

    public Method method() {
        return m;
    }

    public Test test() {
        return test;
    }

    public String testName() {
        return test.nameSuffix().isEmpty()
            ? className() + '.' + m.getName()
            : className() + '.' + m.getName() + '/' + test.nameSuffix();
    }

    public String className() {
        return m.getDeclaringClass().getSimpleName();
    }

    public String testInfo() {
        return testName() +
                (!test().args().isEmpty() ? " (args: " + test().args() + ")": "") +
                (!test().agentArgs().isEmpty() ? " (agentArgs: " + test().agentArgs() + ")": "") +
                (test().inputs().length > 0 ? " (inputs: [" + String.join(" ", test().inputs()) + "])" : "");
    }
}


================================================
FILE: test\one\profiler\test\Runner.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package one.profiler.test;

import java.io.File;
import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Modifier;
import java.util.*;
import java.util.logging.Handler;
import java.util.logging.Level;
import java.util.logging.Logger;

public class Runner {
    private static final Logger log = Logger.getLogger(Runner.class.getName());

    private static final Os currentOs = detectOs();
    private static final Arch currentArch = detectArch();
    private static final int currentJvmVersion = detectJvmVersion();
    private static final Jvm currentJvm = detectJvm();

    private static final String logDir = System.getProperty("logDir", "");

    private static Os detectOs() {
        String os = System.getProperty("os.name").toLowerCase();
        if (os.contains("linux")) {
            return Os.LINUX;
        } else if (os.contains("mac")) {
            return Os.MACOS;
        } else if (os.contains("windows")) {
            return Os.WINDOWS;
        }
        throw new IllegalStateException("Unknown OS type");
    }

    private static Arch detectArch() {
        String arch = System.getProperty("os.arch");
        if (arch.contains("x86_64") || arch.contains("amd64")) {
            return Arch.X64;
        } else if (arch.contains("aarch64")) {
            return Arch.ARM64;
        } else if (arch.contains("arm")) {
            return Arch.ARM32;
        } else if (arch.contains("ppc64le")) {
            return Arch.PPC64LE;
        } else if (arch.contains("riscv64")) {
            return Arch.RISCV64;
        } else if (arch.contains("loongarch64")) {
            return Arch.LOONGARCH64;
        } else if (arch.endsWith("86")) {
            return Arch.X86;
        }
        throw new IllegalStateException("Unknown CPU architecture");
    }

    private static Jvm detectJvm() {
        // Example javaHome: /usr/lib/jvm/amazon-corretto-17.0.8.7.1-linux-x64
        File javaHome = new File(System.getProperty("java.home"));

        // Look for OpenJ9-specific file
        File[] files = new File(javaHome, "lib").listFiles();
        if (files != null) {
            for (File file : files) {
                if (file.getName().equals("J9TraceFormat.dat")) {
                    return Jvm.OPENJ9;
                }
            }
        }

        // Strip /jre from JDK 8 path
        if (currentJvmVersion <= 8) {
            javaHome = javaHome.getParentFile();
        }

        // Workaround for Contents/Home on macOS
        if (currentOs == Os.MACOS) {
            javaHome = javaHome.getParentFile();
        }

        // Look for Zing-specific file
        if (new File(javaHome, "etc/zing").exists()) {
            return Jvm.ZING;
        }

        if (!new File(System.getProperty("java.home"), "lib/" + System.mapLibraryName("jvmcicompiler")).exists()) {
            return Jvm.HOTSPOT_C2;
        }

        return Jvm.HOTSPOT;
    }

    private static int detectJvmVersion() {
        String prop = System.getProperty("java.vm.specification.version");
        if (prop.startsWith("1.")) {
            prop = prop.substring(2);
        }
        return Integer.parseInt(prop);
    }

    private static boolean applicable(Test test) {
        Os[] os = test.os();
        Arch[] arch = test.arch();
        Jvm[] jvm = test.jvm();
        int[] jvmVer = test.jvmVer();
        return (os.length == 0 || Arrays.asList(os).contains(currentOs)) &&
                (arch.length == 0 || Arrays.asList(arch).contains(currentArch)) &&
                (jvm.length == 0 || Arrays.asList(jvm).contains(currentJvm) || (currentJvm == Jvm.HOTSPOT_C2 && Arrays.asList(jvm).contains(Jvm.HOTSPOT))) &&
                (jvmVer.length == 0 || (currentJvmVersion >= jvmVer[0] && currentJvmVersion <= jvmVer[jvmVer.length - 1]));
    }

    private static TestResult run(RunnableTest rt, TestDeclaration decl) {
        if (!rt.test().enabled() || decl.skips(rt.method())) {
            return TestResult.skipDisabled();
        }
        if (!applicable(rt.test())) {
            return TestResult.skipConfigMismatch();
        }

        log.log(Level.INFO, "Running " + rt.testInfo() + "...");

        String testLogDir = logDir.isEmpty() ? null : logDir + '/' + rt.testName();
        try (TestProcess p = new TestProcess(rt.test(), currentOs, currentJvm, testLogDir)) {
            Object holder = (rt.method().getModifiers() & Modifier.STATIC) == 0 ?
                    rt.method().getDeclaringClass().getDeclaredConstructor().newInstance() : null;
            rt.method().invoke(holder, p);
        } catch (InvocationTargetException e) {
            if (e.getTargetException() instanceof NoClassDefFoundError) {
                return TestResult.skipMissingJar();
            }
            return TestResult.fail(e.getTargetException());
        } catch (Throwable e) {
            return TestResult.fail(e);
        }

        return TestRe

================================================
FILE: test\one\profiler\test\SourceCode.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package one.profiler.test;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class SourceCode {
    public static String tryGet(int ignoreFrames) {
        return tryGet(new Exception(), ignoreFrames + 1);
    }

    public static String tryGet(Throwable e, int ignoreFrames) {
        StackTraceElement[] stackTrace = e.getStackTrace();

        if (stackTrace.length > ignoreFrames) {
            StackTraceElement element = stackTrace[ignoreFrames];
            String className = element.getClassName();
            String filePath = getFilePath(className);

            return getSourceCodeAt(filePath, element.getLineNumber());
        }
        return "No stack trace available";
    }

    private static String getFilePath(String className) {
        int dollar = className.lastIndexOf('$');
        if (dollar >= 0) {
            className = className.substring(0, dollar);
        }
        return "test/" + className.replace('.', '/') + ".java";
    }

    private static String getSourceCodeAt(String filePath, int lineNumber) {
        String result = "\t>  " + filePath + ":" + lineNumber;

        try (BufferedReader reader = new BufferedReader(new FileReader(filePath))) {
            String line;
            int currentLine = 1;

            while ((line = reader.readLine()) != null) {
                if (currentLine == lineNumber) {
                    return result + "\n\t>  " + line.trim();
                }
                currentLine++;
            }
        } catch (IOException ex) {
            return "Error reading source file: " + ex.getMessage();
        }

        return result;
    }
}


================================================
FILE: test\one\profiler\test\Test.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package one.profiler.test;

import java.lang.annotation.ElementType;
import java.lang.annotation.Repeatable;
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;
import java.lang.annotation.Target;

@Target(ElementType.METHOD)
@Retention(RetentionPolicy.RUNTIME)
@Repeatable(Tests.class)
public @interface Test {

    String[] sh() default {};

    Class<?> mainClass() default Test.class;

    String args() default "";

    String agentArgs() default "";

    String jvmArgs() default "";

    String[] env() default {};

    boolean debugNonSafepoints() default false;

    boolean output() default false;

    boolean error() default false;

    Os[] os() default {};

    Arch[] arch() default {};

    Jvm[] jvm() default {};

    int[] jvmVer() default {};

    boolean enabled() default true;

    // Optional inputs to the test method.
    String[] inputs() default {};

    String nameSuffix() default "";
}


================================================
FILE: test\one\profiler\test\TestDeclaration.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package one.profiler.test;

import java.io.File;
import java.lang.reflect.Method;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.HashSet;
import java.util.List;
import java.util.Set;
import java.util.logging.Level;
import java.util.logging.Logger;
import java.util.regex.Pattern;
import java.util.stream.Collectors;

public class TestDeclaration {
    private static final Logger log = Logger.getLogger(TestDeclaration.class.getName());

    private final List<String> allDirs;
    private final List<Pattern> includeGlobs;
    private final List<Pattern> skipGlobs;

    public TestDeclaration(List<String> allDirs, List<String> globs, List<String> skipGlobs) {
        this.allDirs = allDirs;
        this.includeGlobs = filterFromGlobs(globs);
        this.skipGlobs = filterFromGlobs(skipGlobs);

        log.log(Level.FINE, "Test Directories: " + allDirs);
        log.log(Level.FINE, "Test Filters: " + globs);
        log.log(Level.FINE, "Skip Filters: " + skipGlobs);
    }

    public static TestDeclaration parse(String[] args) {
        // Glob filters matching "ClassName.methodName".
        List<String> filters = Arrays.asList(args);

        List<String> skipFilters = new ArrayList<>();
        String skipProperty = System.getProperty("skip");
        if (skipProperty != null && !skipProperty.isEmpty()) {
            skipFilters.addAll(Arrays.asList(skipProperty.split(" ")));
        }

        List<String> allTestDirs = new ArrayList<>();
        File[] files = new File("test/test").listFiles();
        if (files != null) {
            for (File file : files) {
                if (file.isDirectory() && !file.getName().startsWith(".")) {
                    allTestDirs.add(file.getName());
                }
            }
        }

        return new TestDeclaration(allTestDirs, filters, skipFilters);
    }

    private List<RunnableTest> getRunnableTests(String dir) {
        String className = "test." + dir + "." + Character.toUpperCase(dir.charAt(0)) + dir.substring(1) + "Tests";
        try {
            List<RunnableTest> rts = new ArrayList<>();
            for (Method m : Class.forName(className).getMethods()) {
                if (includes(m)) {
                    for (Test t : m.getAnnotationsByType(Test.class)) {
                        rts.add(new RunnableTest(m, t));
                    }
                }
            }
            return rts;
        } catch (ClassNotFoundException e) {
            throw new RuntimeException(e);
        }
    }

    public List<RunnableTest> getRunnableTests() {
        return allDirs.stream()
            .flatMap(dir -> getRunnableTests(dir).stream())
            .sorted(Comparator.comparing(RunnableTest::testName))
            .collect(Collectors.toList());
    }

    public boolean includes(Method m) {
        return includeGlobs.isEmpty() || matches(m, includeGlobs);
    }

    public boolean skips(Method m) {
        return !skipGlobs.isEmpty() && matches(m, skipGlobs);
    }

    private static boolean matches(Method m, List<Pattern> patterns) {
        String name = m.getDeclaringClass().getSimpleName() + '.' + m.getName();
        return patterns.stream().anyMatch(p -> p.matcher(name).matches());
    }

    private static Pattern filterFrom(String s) {
        if (s.startsWith("*") && s.endsWith("*")) {
            // contains.
            return Pattern.compile(".*" + Pattern.quote(s.substring(1, s.length() - 1)) + ".*");
        }
        if (s.startsWith("*")) {
            // ends with.
            return Pattern.compile(".*" + Pattern.quote(s.substring(1)) + "$");
        }
        if (s.endsWith("*")) {
            // starts with.
            return Pattern.compile("^" + Pattern.quote(s.substring(0, s.length() - 1)) + ".*");
        }

        // equals
        return Pattern.compile("^" + Pattern.quote(s) + "$");
    }

    private List<Pattern> filterFromGlobs(List<String> globs) {
        Set<String> result = new HashSet<>();
        for (String g : globs) {
            if (allDirs.contains(g)) {
                // Convert test directory name to class name.
                result.add(g.substring(0, 1).toUpperCase() + g.substring(1).toLowerCase() + "Tests.*");
            } else if (g.contains(".") || g.contains("*")) {
                result.add(g);
            } else if (Character.isUpperCase(g.charAt(0))) {
                // Looks like class name.
                result.add(g + ".*");
            } else if (Character.isLowerCase(g.charAt(0))) {
                // Looks like method name.
                result.add("*." + g);
            } else {
                throw new RuntimeException("Unknown glob type: " + g);
            }
        }
        return result.stream().map(TestDeclaration::filterFrom).collect(Collectors.toList());
    }
}


================================================
FILE: test\one\profiler\test\TestProcess.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package one.profiler.test;

import java.io.*;
import java.lang.invoke.MethodHandle;
import java.lang.invoke.MethodHandles;
import java.lang.invoke.MethodType;
import java.lang.reflect.Field;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.nio.file.StandardCopyOption;
import java.util.*;
import java.util.concurrent.TimeUnit;
import java.util.concurrent.TimeoutException;
import java.util.logging.Level;
import java.util.logging.Logger;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.stream.Stream;

public class TestProcess implements Closeable {
    private static final Logger log = Logger.getLogger(TestProcess.class.getName());

    public static final String STDOUT = "%out";
    public static final String STDERR = "%err";
    public static final String PROFOUT = "%pout";
    public static final String PROFERR = "%perr";
    public static final String LIBPROF = "%lib";
    public static final String TESTBIN = "%testbin";
    public static final String TESTLIB = "%testlib";

    private static final String JAVA_HOME = System.getProperty("java.home");

    private static final Pattern filePattern = Pattern.compile("(%[a-z][a-z0-9_]*)(\\.[a-z]+)?");

    private static final MethodHandle pid = getPidHandle();

    private static MethodHandle getPidHandle() {
        // JDK 9+
        try {
            return MethodHandles.publicLookup().findVirtual(Process.class, "pid", MethodType.methodType(long.class));
        } catch (ReflectiveOperationException e) {
            // fallback
        }

        // JDK 8
        try {
            Field f = Class.forName("java.lang.UNIXProcess").getDeclaredField("pid");
            f.setAccessible(true);
            return MethodHandles.lookup().unreflectGetter(f).asType(MethodType.methodType(long.class, Process.class));
        } catch (ReflectiveOperationException e) {
            throw new IllegalStateException("Unsupported API", e);
        }
    }

    private final Test test;
    private final Os currentOs;
    private final Jvm currentJvm;
    private final String logDir;
    private final String[] inputs;
    private final Process p;
    private final Map<String, File> tmpFiles = new HashMap<>();
    private final int timeout = 30;

    public TestProcess(Test test, Os currentOs, Jvm currentJvm, String logDir) throws Exception {
        this.test = test;
        this.currentOs = currentOs;
        this.currentJvm = currentJvm;
        this.logDir = logDir;
        this.inputs = test.inputs();

        List<String> cmd = buildCommandLine(test);
        log.log(Level.FINE, "Running " + String.join(" ", cmd));

        ProcessBuilder pb = new ProcessBuilder(cmd).inheritIO();
        if (test.output()) {
            pb.redirectOutput(createTempFile(STDOUT));
        }
        if (test.error()) {
            pb.redirectError(createTempFile(STDERR));
        }

        for (String env : test.env()) {
            String[] keyValue = env.split("=", 2);
            if (keyValue.length == 2) {
                pb.environment().put(keyValue[0], substituteFiles(keyValue[1]));
            }
        }
        pb.environment().put("TEST_JAVA_HOME", JAVA_HOME);

        this.p = pb.start();

        if (cmd.get(0).endsWith("java")) {
            // Give the JVM some time to initialize
            Thread.sleep(700);
        }
    }

    public Test test() {
        return this.test;
    }

    public String[] inputs() {
        return this.inputs;
    }

    public Os currentOs() {
        return this.currentOs;
    }

    public Jvm currentJvm() {
        return this.currentJvm;
    }

    public String profilerLibPath() {
        return "build/lib/libasyncProfiler." + currentOs.getLibExt();
    }

    public String testBinPath() {
        return "build/test/bin";
    }

    public String testLibPath() {
        return "build/test/lib";
    }

    private List<String> buildCommandLine(Test test) {
        List<String> cmd = new ArrayList<>();

        String[] sh = test.sh();
        if (sh.length > 0) {
            cmd.add("/bin/sh");
            cmd.add("-e");
            cmd.add("-c");
            cmd.add(substituteFiles(String.join(";", sh)));
        } else {
            cmd.add(System.getProperty("java.home") + "/bin/java");
            cmd.add("-cp");
            cmd.add(System.getProperty("java.class.path"));
            if (test.debugNonSafepoints()) {
                cmd.add("-XX:+UnlockDiagnosticVMOptions");
                cmd.add("-XX:+DebugNonSafepoints");
            }
            cmd.add("-Done.profiler.libraryPath=" + System.getProperty("one.profiler.libraryPath", profilerLibPath()));
            cmd.add("-Djava.library.path=" + testLibPath());
            cmd.add("-ea");
            addArgs(cmd, test.jvmArgs());
            if (!test.agentArgs().isEmpty()) {
                cmd.add("-agentp

================================================
FILE: test\one\profiler\test\TestResult.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package one.profiler.test;

public class TestResult {
    private final TestStatus status;
    private final Throwable throwable;

    private TestResult(TestStatus status, Throwable throwable) {
        if ((status == TestStatus.FAIL) ^ (throwable != null)) {
            throw new IllegalArgumentException();
        }

        this.status = status;
        this.throwable = throwable;
    }

    public TestStatus status() {
        return status;
    }

    public Throwable throwable() {
        return throwable;
    }

    public static TestResult skipConfigMismatch() {
        return new TestResult(TestStatus.SKIP_CONFIG_MISMATCH, null);
    }

    public static TestResult skipDisabled() {
        return new TestResult(TestStatus.SKIP_DISABLED, null);
    }

    public static TestResult skipMissingJar() {
        return new TestResult(TestStatus.SKIP_MISSING_JAR, null);
    }

    public static TestResult pass() {
        return new TestResult(TestStatus.PASS, null);
    }

    public static TestResult fail(Throwable t) {
        return new TestResult(TestStatus.FAIL, t);
    }
}


================================================
FILE: test\one\profiler\test\Tests.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package one.profiler.test;

import java.lang.annotation.ElementType;
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;
import java.lang.annotation.Target;

@Retention(RetentionPolicy.RUNTIME)
@Target(ElementType.METHOD)
public @interface Tests {
    Test[] value();
}


================================================
FILE: test\one\profiler\test\TestStatus.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package one.profiler.test;

public enum TestStatus {
    PASS,
    FAIL,
    SKIP_DISABLED,
    SKIP_CONFIG_MISMATCH,
    SKIP_MISSING_JAR,
}


================================================
FILE: test\stubs\com\google\protobuf\ByteString.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package com.google.protobuf;

public abstract class ByteString {}


================================================
FILE: test\stubs\com\google\protobuf\CodedInputStream.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package com.google.protobuf;

public abstract class CodedInputStream {}


================================================
FILE: test\stubs\com\google\protobuf\GeneratedMessageV3.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package com.google.protobuf;

public abstract class GeneratedMessageV3 {}


================================================
FILE: test\stubs\com\google\protobuf\InvalidProtocolBufferException.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package com.google.protobuf;

public class InvalidProtocolBufferException extends java.io.IOException {}


================================================
FILE: test\stubs\com\google\protobuf\MessageOrBuilder.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package com.google.protobuf;

public interface MessageOrBuilder {}


================================================
FILE: test\stubs\com\google\protobuf\ProtocolStringList.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package com.google.protobuf;

public interface ProtocolStringList extends java.util.List<String> {}


================================================
FILE: test\test\alloc\AllocTests.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package test.alloc;

import one.jfr.JfrReader;
import one.jfr.StackTrace;
import one.jfr.event.AllocationSample;
import one.profiler.test.*;

import java.io.File;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.nio.file.StandardCopyOption;
import java.util.List;

public class AllocTests {

    @Test(mainClass = MapReader.class, jvmArgs = "-XX:+UseG1GC -Xmx1g -Xms1g", jvm = Jvm.HOTSPOT)
    public void alloc(TestProcess p) throws Exception {
        Output out = p.profile("-e cpu -d 3 -o collapsed");
        assert out.contains("G1RemSet::");

        out = p.profile("--alloc 1 -d 3 -o collapsed");
        assert out.contains("java/io/BufferedReader.readLine;");
        assert out.contains("java/lang/String.split;");
        assert out.contains("java/lang/String.trim;");
        assert out.contains("java\\.lang\\.String\\[]");
    }

    @Test(mainClass = MapReaderOpt.class, jvmArgs = "-XX:+UseParallelGC -Xmx1g -Xms1g", jvm = {Jvm.HOTSPOT, Jvm.ZING})
    public void allocTotal(TestProcess p) throws Exception {
        Output out = p.profile("-e alloc -d 3 -o collapsed --total");
        assert out.samples("java.util.HashMap\\$Node\\[]") > 1_000_000;

        out = p.profile("stop -o flamegraph --total");
        out = out.convertFlameToCollapsed();
        assert out.contains("java\\.lang\\.Long");
        assert out.contains("java\\.util\\.HashMap\\$Node\\[]");
    }

    @Test(mainClass = Hello.class, agentArgs = "start,event=alloc,alloc=1,cstack=fp,flamegraph,file=%f", jvmArgs = "-XX:+UseG1GC -XX:-UseTLAB")
    public void startup(TestProcess p) throws Exception {
        Output out = p.waitForExit("%f");
        out = out.convertFlameToCollapsed();
        assert out.contains("JNI_CreateJavaVM");
        assert out.contains("java/lang/ClassLoader\\.loadClass");
        assert out.contains("java\\.lang\\.Class");
        assert out.contains("java\\.lang\\.Thread");
        assert out.contains("java\\.lang\\.String");
        assert out.contains("int\\[]");
    }

    @Test(mainClass = MapReaderOpt.class, agentArgs = "start,event=G1CollectedHeap::humongous_obj_allocate", jvmArgs = "-XX:+UseG1GC -XX:G1HeapRegionSize=1M -Xmx4g -Xms4g", os = Os.LINUX)
    public void humongous(TestProcess p) throws Exception {
        Thread.sleep(1000);
        Output out = p.profile("stop -o collapsed");
        assert out.contains("java/io/ByteArrayOutputStream.toByteArray;");
        assert out.contains("G1CollectedHeap::humongous_obj_allocate");
    }

    @Test(mainClass = MapReaderOpt.class, jvmVer = {11, Integer.MAX_VALUE})
    public void objectSamplerWtihDifferentAsprofs(TestProcess p) throws Exception {
        Output out = p.profile("-e alloc -d 3 -o collapsed");
        // _[k] suffix in collapsed output corresponds to jdk.ObjectAllocationOutsideTLAB, which means alloc tracer is being used
        assert !out.contains("_\\[k\\]"); // we are using alloc tracer instead of object sampler, should definitely not happen on first profiling call
        File asprofCopy = File.createTempFile(new File(p.profilerLibPath()).getName(), null);
        asprofCopy.deleteOnExit();
        Files.copy(Paths.get(p.profilerLibPath()), asprofCopy.toPath(), StandardCopyOption.REPLACE_EXISTING);
        Output outWithCopy = p.profile(String.format("--libpath %s -e alloc -d 3 -o collapsed", asprofCopy.getAbsolutePath()));
        assert !outWithCopy.contains("_\\[k\\]"); // first instance of profiler has not properly relinquished the can_generate_sampled_object_alloc_events capability.
    }

    // Without liveness tracking, results won't change except for the sampling
    // error.
    @Test(mainClass = RandomBlockRetainer.class, jvmVer = {11, Integer.MAX_VALUE}, args = "1.0", agentArgs = "start,alloc=1k,total,file=%f,collapsed", nameSuffix = "1.0")
    @Test(mainClass = RandomBlockRetainer.class, jvmVer = {11, Integer.MAX_VALUE}, args = "0.0", agentArgs = "start,alloc=1k,total,file=%f,collapsed,live", nameSuffix = "0.0+live")
    @Test(mainClass = RandomBlockRetainer.class, jvmVer = {11, Integer.MAX_VALUE}, args = "0.1", agentArgs = "start,alloc=1k,total,file=%f,collapsed,live", nameSuffix = "0.1+live")
    @Test(mainClass = RandomBlockRetainer.class, jvmVer = {11, Integer.MAX_VALUE}, args = "1.0", agentArgs = "start,alloc=1k,total,file=%f,collapsed,live", nameSuffix = "1.0+live")
    public void liveness(TestProcess p) throws Exception {
        final long TOTAL_BYTES = 50000000;
        final double tolerance = 0.10;

        // keepChance = live ? args() : 1.0, which is equal to args().
        final double keepChance = Double.parseDouble(p.test().args());

        Output out = p.waitForExit("%f");
        long totalBytes = out.filter("RandomBlockRetainer\\.alloc").samples("byte\\[\\]");

        final double lowerLimit = (keepChance - tolerance) * TOTAL_BYTES;
        final double upperLimit = (keepChance + tolerance) * TOTAL

================================================
FILE: test\test\alloc\Hello.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package test.alloc;

/**
 * How many objects are created when running "Hello World" application?
 * Where are these objects are created?
 * <p>
 * async-profiler can trace every single created object -
 * just run allocation profiling with G1 GC and TLAB disabled:
 * `java -XX:+UseG1GC -XX:-UseTLAB -agentlib:asyncProfiler=start,event=alloc,file=alloc.html`
 * <p>
 * Add `cstack=fp` option to include native stack traces.
 */
public class Hello {

    public static void main(String[] args) {
        System.out.println("It works!");
    }
}


================================================
FILE: test\test\alloc\MapReader.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package test.alloc;

import java.io.BufferedReader;
import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.nio.charset.StandardCharsets;
import java.util.Base64;
import java.util.HashMap;
import java.util.Map;
import java.util.concurrent.ThreadLocalRandom;

public class MapReader {
    private final byte[] input;

    public MapReader(int size) throws IOException {
        this.input = generate(size);
    }

    private static byte[] generate(int size) throws IOException {
        ByteArrayOutputStream out = new ByteArrayOutputStream(size * 17);
        for (int i = 0; i < size; i++) {
            int length = ThreadLocalRandom.current().nextInt(1, 9);
            byte[] b = new byte[length];
            ThreadLocalRandom.current().nextBytes(b);
            String key = Base64.getEncoder().encodeToString(b);
            long value = ThreadLocalRandom.current().nextLong(1000000);
            out.write((key + ": " + value + "\n").getBytes(StandardCharsets.ISO_8859_1));
        }
        return out.toByteArray();
    }

    public Map<String, Long> readMap(InputStream in) throws IOException {
        Map<String, Long> map = new HashMap<>();

        try (BufferedReader br = new BufferedReader(new InputStreamReader(in))) {
            for (String line; (line = br.readLine()) != null; ) {
                String[] kv = line.split(":", 2);
                String key = kv[0].trim();
                String value = kv[1].trim();
                map.put(key, Long.parseLong(value));
            }
        }

        return map;
    }

    public void benchmark() throws IOException {
        while (true) {
            long start = System.nanoTime();
            readMap(new ByteArrayInputStream(input));
            long end = System.nanoTime();
            System.out.println((end - start) / 1e9);
        }
    }

    public static void main(String[] args) throws Exception {
        new MapReader(2000000).benchmark();
    }
}


================================================
FILE: test\test\alloc\MapReaderOpt.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package test.alloc;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;

public class MapReaderOpt extends MapReader {

    public MapReaderOpt(int size) throws IOException {
        super(size);
    }

    @Override
    public Map<String, Long> readMap(InputStream in) throws IOException {
        Map<String, Long> map = new HashMap<>();

        try (BufferedReader br = new BufferedReader(new InputStreamReader(in))) {
            for (String line; (line = br.readLine()) != null; ) {
                int sep = line.indexOf(':');
                String key = trim(line, 0, sep);
                String value = trim(line, sep + 1, line.length());
                map.put(key, Long.parseLong(value));
            }
        }

        return map;
    }

    private static String trim(String line, int from, int to) {
        while (from < to && line.charAt(from) <= ' ') {
            from++;
        }
        while (to > from && line.charAt(to - 1) <= ' ') {
            to--;
        }
        return line.substring(from, to);
    }

    public static void main(String[] args) throws Exception {
        new MapReaderOpt(2000000).benchmark();
    }
}


================================================
FILE: test\test\alloc\RandomBlockRetainer.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package test.alloc;

import java.util.ArrayList;
import java.util.List;

public class RandomBlockRetainer {
    public static void main(String[] args) throws Exception {
        double keepChance = 0.5;
        if (args.length > 0) {
            try {
                keepChance = Double.parseDouble(args[0]);
            } catch (NumberFormatException e) {
                System.err.println("Invalid keepChance value. Using default value of 0.5.");
            }
        }

        // Set up a list to hold large objects and keep them in memory.
        List<byte[]> rooter = new ArrayList<>();

        final int TOTAL_BLOCKS = 500; // Has to be less than LiveRefs::MAX_REFS for testing purposes.
        final int BLOCK_SIZE = 100 * 1000;

        for (int i = 0; i < TOTAL_BLOCKS; i++) {
            byte[] block = i % 2 == 0 ? alloc1(BLOCK_SIZE) : alloc2(BLOCK_SIZE);

            if (Math.random() <= keepChance) {
                // Keep a reference to prevent the block from being garbage collected
                rooter.add(block);
            }
        }

        System.gc();
    }

    private static byte[] alloc1(int size) {
        return new byte[size];
    }

    private static byte[] alloc2(int size) {
        return new byte[size];
    }
}


================================================
FILE: test\test\api\ApiTests.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package test.api;

import one.profiler.test.Output;
import one.profiler.test.Test;
import one.profiler.test.TestProcess;

public class ApiTests {

    @Test(mainClass = DumpCollapsed.class, output = true)
    public void flat(TestProcess p) throws Exception {
        Output out = p.waitForExit(TestProcess.STDOUT);
        assert out.contains("BusyLoops.method1;");
        assert out.contains("BusyLoops.method2;");
        assert out.contains("BusyLoops.method3;");
    }

    @Test(mainClass = DumpOtlp.class)
    public void otlp(TestProcess p) throws Exception {
        p.waitForExit();
        assert p.exitCode() == 0;
    }

    @Test(mainClass = StopResume.class, output = true)
    public void stopResume(TestProcess p) throws Exception {
        Output out = p.waitForExit(TestProcess.STDOUT);
        assert !out.contains("BusyLoops.method1");
        assert out.contains("BusyLoops.method2");
        assert !out.contains("BusyLoops.method3");
    }

    @Test(mainClass = MetricsTest.class)
    public void metrics(TestProcess p) throws Exception {
        p.waitForExit();
        assert p.exitCode() == 0;
    }

    @Test(
        mainClass = JavaAgent.class,
        output = true,
        jvmArgs = "-javaagent:build/jar/async-profiler.jar=start,event=cpu,interval=1ms,file=%f.collapsed"
    )
    public void javaAgent(TestProcess p) throws Exception {
        Output out = p.waitForExit(TestProcess.STDOUT);
        assert p.exitCode() == 0;
        assert out.contains("async-profiler version: \\d+");
        Output profile = p.readFile("%f");
        assert profile.contains("BusyLoops.method1;");
        assert profile.contains("BusyLoops.method2;");
        assert profile.contains("BusyLoops.method3;");
    }
}


================================================
FILE: test\test\api\BusyLoops.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package test.api;

import java.security.SecureRandom;
import java.time.Instant;

class BusyLoops {

    static long method1() {
        long result = 0;
        for (int i = 0; i < 1_000_000; i++) {
            result += Integer.toString(i).hashCode();
        }
        return result;
    }

    static long method2() {
        long iterations = 0;
        Instant end = Instant.now().plusMillis(100);
        while (Instant.now().isBefore(end)) {
            iterations++;
        }
        return iterations;
    }

    static long method3() {
        long iterations = 0;
        SecureRandom r = new SecureRandom();
        while ((r.nextInt() % 1_000_000) != 0) {
            iterations++;
        }
        return iterations;
    }
}


================================================
FILE: test\test\api\DumpCollapsed.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package test.api;

import one.profiler.AsyncProfiler;
import one.profiler.Counter;
import one.profiler.Events;

public class DumpCollapsed extends BusyLoops {

    public static void main(String[] args) throws Exception {
        AsyncProfiler.getInstance().start(Events.CPU, 1_000_000);

        for (int i = 0; i < 5; i++) {
            method1();
            method2();
            method3();
        }

        String profile = AsyncProfiler.getInstance().dumpCollapsed(Counter.SAMPLES);
        System.out.println(profile);
    }
}


================================================
FILE: test\test\api\DumpOtlp.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package test.api;

import java.nio.ByteBuffer;
import one.profiler.AsyncProfiler;
import one.profiler.Counter;
import one.profiler.Events;

public class DumpOtlp extends BusyLoops {

    public static void main(String[] args) throws Exception {
        AsyncProfiler.getInstance().start(Events.CPU, 1_000_000);

        for (int i = 0; i < 5; i++) {
            method1();
            method2();
            method3();
        }

        // TODO: Should we test this further?
        byte[] profile = AsyncProfiler.getInstance().dumpOtlp();
        System.out.println(profile.length);
    }
}


================================================
FILE: test\test\api\JavaAgent.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package test.api;

import one.profiler.Counter;

import javax.management.MBeanServer;
import javax.management.ObjectName;
import java.lang.management.ManagementFactory;

public class JavaAgent {

    public static void main(String[] args) throws Exception {
        MBeanServer mbs = ManagementFactory.getPlatformMBeanServer();
        ObjectName obj = new ObjectName("one.profiler:type=AsyncProfiler");

        String version = (String) mbs.getAttribute(obj, "Version");
        System.out.println(String.format("async-profiler version: %s", version));

        for (int i = 0; i < 3; i++) {
            BusyLoops.method1();
            BusyLoops.method2();
            BusyLoops.method3();
        }

        String profile = (String) mbs.invoke(
                obj,
                "dumpCollapsed",
                new String[] { Counter.SAMPLES.name() },
                new String[] { String.class.getName() }
            );
        System.out.println(profile);
    }
}


================================================
FILE: test\test\api\MetricsTest.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */
package test.api;

import java.util.HashSet;
import one.profiler.AsyncProfiler;

public class MetricsTest {

    static void doStuff() {}

    public static void main(String[] args) throws Exception {
        AsyncProfiler profiler = AsyncProfiler.getInstance();
        profiler.execute("start,trace=test.api.MetricsTest.doStuff,features=stats,jfr,file=/dev/null");

        doStuff();
        doStuff();
        doStuff();

        String metrics = profiler.execute("metrics");
        for (String line : metrics.split("\n")) {
            String[] pair = line.split(" ");
            assert pair.length == 2 : line;
            if (pair[1].startsWith("0")) {
                assert "samples_skipped_total".equals(pair[0]) || "calltracestorage_overflows_total".equals(pair[0]) : line;
            }

            if (pair[0].equals("samples_total")) {
                assert pair[1].equals("3") : line;
            }
        }

        // Should be found since we used features=stats
        assert metrics.contains("stackwalk_ns_total") : metrics;
    }
}


================================================
FILE: test\test\api\StopResume.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package test.api;

import one.profiler.AsyncProfiler;
import one.profiler.Events;

public class StopResume extends BusyLoops {

    public static void main(String[] args) throws Exception {

        for (int i = 0; i < 5; i++) {
            method1();
            AsyncProfiler.getInstance().resume(Events.CPU, 1_000_000);
            method2();
            AsyncProfiler.getInstance().stop();
            method3();
        }

        String profile = AsyncProfiler.getInstance().dumpTraces(100);
        System.out.println(profile);
    }
}


================================================
FILE: test\test\c\CTests.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package test.c;

import one.profiler.test.Output;
import one.profiler.test.Test;
import one.profiler.test.TestProcess;

import java.io.File;

public class CTests {

    @Test(sh = "%testbin/native_api %api_file.jfr", output = true)
    @Test(sh = "%testbin/native_api %api_file.jfr", env = {"ASPROF_COMMAND=start,cpu,file=%preload_file.jfr"},
            output = true, nameSuffix = "fake-preload")
    public void nativeApi(TestProcess p) throws Exception {
        Output out = p.waitForExit(TestProcess.STDOUT);
        assert p.exitCode() == 0;
        assert out.contains("Starting profiler");
        assert out.contains("Stopping profiler");
        assert p.getFile("%api_file").length() > 0;

        File preloadFile = p.getFile("%preload_file");
        assert preloadFile == null || preloadFile.length() == 0;
    }
}


================================================
FILE: test\test\comptask\ComptaskTests.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package test.comptask;

import one.profiler.test.*;

public class ComptaskTests {
    @Test(
        mainClass = Main.class,
        agentArgs = "start,features=comptask,collapsed,interval=1ms,file=%f",
        jvmArgs = "-Xcomp",
        jvm = Jvm.HOTSPOT_C2
    )
    public void testCompTask(TestProcess p) throws Exception {
        Output out = p.waitForExit("%f");
        assert p.exitCode() == 0;
        assert out.contains(";Compiler::compile_method;(java|sun|jdk)/[^;]+[^;/]\\.[^;/]+;");
        assert out.contains(";C2Compiler::compile_method;(java|sun|jdk)/[^;]+[^;/]\\.[^;/]+;");
    }
}


================================================
FILE: test\test\comptask\Main.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package test.comptask;

public class Main {
    private static final long RUN_DURATION_MS = 1000;

    public static void main(String[] args) throws Exception {
        long start = System.nanoTime();
        long end = start + RUN_DURATION_MS * 1_000_000;
        while (System.nanoTime() < end) {}
    }
}


================================================
FILE: test\test\cpu\CpuBurner.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package test.cpu;

import java.util.Random;

public class CpuBurner {
    private static final Random random = new Random();

    static void burn() {
        long n = random.nextLong();
        if (Long.toString(n).hashCode() == 0) {
            System.out.println(n);
        }
    }

    public static void main(String[] args) {
        while (true) {
            burn();
        }
    }
}


================================================
FILE: test\test\cpu\CpuTests.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package test.cpu;

import java.io.File;
import java.io.IOException;
import java.lang.ProcessBuilder.Redirect;

import one.profiler.test.Assert;
import one.profiler.test.Os;
import one.profiler.test.Output;
import one.profiler.test.Test;
import one.profiler.test.TestProcess;

public class CpuTests {

    private static void assertCloseTo(long value, long target, String message) {
        Assert.isGreaterOrEqual(value, target * 0.75, message);
        Assert.isLessOrEqual(value, target * 1.25, message);
    }

    private static void pinCpu(TestProcess p, int cpu) throws Exception {
        String[] tasksetCmd = {"taskset", "-acp", String.valueOf(cpu), String.valueOf(p.pid())};
        ProcessBuilder cpuPinPb = new ProcessBuilder(tasksetCmd)
            .redirectError(Redirect.INHERIT)
            .redirectOutput(new File("/dev/null"));
        if (cpuPinPb.start().waitFor() != 0) {
            throw new RuntimeException("Could not set CPU list for the test process");
        }
    }

    @Test(mainClass = CpuBurner.class, os = Os.LINUX)
    public void ctimerTotal(TestProcess p) throws Exception {
        Output out = p.profile("-d 2 -e ctimer -i 100ms --total -o collapsed");
        assertCloseTo(out.total(), 2_000_000_000, "ctimer total should match profiling duration");

        out = p.profile("-d 2 -e ctimer -i 1us --total -o collapsed");
        assertCloseTo(out.total(), 2_000_000_000, "ctimer total should not depend on the profiling interval");
    }

    @Test(mainClass = CpuBurner.class)
    public void itimerTotal(TestProcess p) throws Exception {
        Output out = p.profile("-d 2 -e itimer -i 100ms --total -o collapsed");
        assertCloseTo(out.total(), 2_000_000_000, "itimer total should match profiling duration");
    }

    @Test(mainClass = CpuBurner.class, os = Os.LINUX)
    public void perfEventsTargetCpuEventsCount(TestProcess p) throws Exception {
        pinCpu(p, 0);

        Output outWrongCpu = p.profile("-d 2 -e cpu-clock -i 100ms --total -o collapsed --target-cpu 1");
        Assert.isEqual(outWrongCpu.total(), 0, "perf_events total should be 0 when the wrong CPU is targeted");

        Output outRightCpu = p.profile("-d 2 -e cpu-clock -i 100ms --total -o collapsed --target-cpu 0");
        assertCloseTo(outRightCpu.total(), 2_000_000_000, "perf_events total should match profiling duration");
    }

    @Test(mainClass = CpuBurner.class, os = Os.LINUX)
    public void perfEventsRecordCpuEventsCount(TestProcess p) throws Exception {
        pinCpu(p, 1);

        Output output = p.profile("-d 2 -e cpu-clock -i 100ms --total -o collapsed --record-cpu");
        assert output.contains("\\[CPU-1\\]");
        assert !output.contains("\\[CPU-0\\]");

        output = p.profile("-d 2 -e cpu-clock -i 100ms --total -o collapsed --record-cpu --all-user");
        assert output.contains("\\[CPU-1\\]");
        assert !output.contains("\\[CPU-0\\]");
    }

    @Test(mainClass = CpuBurner.class, os = Os.LINUX)
    public void perfEventsTargetCpuWithFdtransferEventsCount(TestProcess p) throws Exception {
        pinCpu(p, 0);

        Output outWrongCpu = p.profile("-d 2 -e cpu-clock -i 100ms --total -o collapsed --target-cpu 1 --fdtransfer");
        Assert.isEqual(outWrongCpu.total(), 0, "perf_events total should be 0 when the wrong CPU is targeted");

        Output outRightCpu = p.profile("-d 2 -e cpu-clock -i 100ms --total -o collapsed --target-cpu 0 --fdtransfer");
        assertCloseTo(outRightCpu.total(), 2_000_000_000, "perf_events total should match profiling duration");
    }

    @Test(mainClass = CpuBurner.class, os = Os.LINUX)
    public void itimerDoesNotSupportTargetCpu(TestProcess p) throws Exception {
        try {
            Output out = p.profile("-e itimer --target-cpu 1");
            throw new IllegalStateException("Profiling should have failed");
        } catch (IOException expectedException) {}
    }

    @Test(mainClass = CpuBurner.class, os = Os.LINUX)
    public void ctimerDoesNotSupportTargetCpu(TestProcess p) throws Exception {
        try {
            Output out = p.profile("-e ctimer --target-cpu 1");
            throw new IllegalStateException("Profiling should have failed");
        } catch (IOException expectedException) {}
    }

    @Test(mainClass = CpuBurner.class, os = Os.LINUX)
    public void itimerDoesNotSupportRecordCpu(TestProcess p) throws Exception {
        try {
            Output out = p.profile("-e itimer --record-cpu");
            throw new IllegalStateException("Profiling should have failed");
        } catch (IOException expectedException) {}
    }

    @Test(mainClass = CpuBurner.class, os = Os.LINUX)
    public void ctimerDoesNotSupportRecordCpu(TestProcess p) throws Exception {
        try {
            Output out = p.profile("-e ctimer --record-cpu");
            throw new IllegalStateException("Profiling should have failed");
        } catch

================================================
FILE: test\test\cstack\CstackTests.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package test.cstack;

import one.profiler.test.Jvm;
import one.profiler.test.Os;
import one.profiler.test.Output;
import one.profiler.test.Test;
import one.profiler.test.TestProcess;
import test.smoke.Cpu;

public class CstackTests {
    private static final String PROFILE_COMMAND = "-e cpu -i 10ms -d 1 -o collapsed -a ";

    @Test(mainClass = LongInitializer.class)
    public void asyncGetCallTrace(TestProcess p) throws Exception {
        Output out = p.profile(PROFILE_COMMAND + "--cstack no");
        assert !out.contains(";readBytes");
        assert out.contains("LongInitializer.main_\\[j]");

        out = p.profile(PROFILE_COMMAND + "--cstack fp");
        assert out.contains(";readBytes");
        assert out.contains("LongInitializer.main_\\[j]");
    }

    @Test(mainClass = LongInitializer.class, jvm = Jvm.HOTSPOT, os = Os.LINUX)
    public void vmStructs(TestProcess p) throws Exception {
        Output out = p.profile(PROFILE_COMMAND + "--cstack vm");
        assert out.contains(";readBytes");
        assert out.contains("LongInitializer.main_\\[0]");
        assert !out.contains("InstanceKlass::initialize");
        assert !out.contains("call_stub");
        assert !out.contains("JavaMain");

        out = p.profile(PROFILE_COMMAND + "--cstack vmx");
        assert out.contains(";readBytes");
        assert out.contains("LongInitializer.main_\\[0]");
        assert out.contains("InstanceKlass::initialize");
        assert out.contains("call_stub");
        assert out.contains("JavaMain");
    }

    @Test(mainClass = Cpu.class, jvm = Jvm.HOTSPOT, agentArgs = "start,event=cpu,interval=1ms")
    public void saneNativeStack(TestProcess p) throws Exception {
        Thread.sleep(2000);
        Output out = p.profile("stop -o flamegraph").convertFlameToCollapsed();

        assert out.contains("^test/smoke/Cpu.main");
        assert out.contains("CompileBroker::");
        assert out.contains("Java_java_io_");

        // No JVM frames before start_thread
        assert !out.contains("CompileBroker::.*;start_thread");

        // No duplicated native frames
        assert !out.contains("Java_java_io_.*;Java_java_io_");
    }
}


================================================
FILE: test\test\cstack\LongInitializer.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package test.cstack;

import java.io.FileInputStream;
import java.util.Arrays;

public class LongInitializer {

    static class InnerClass {
        static {
            byte[] bytes = new byte[16];
            byte[] empty = new byte[16];
            try (FileInputStream fis = new FileInputStream("/dev/urandom")) {
                long count = 0;
                while (fis.read(bytes) > 0 && !Arrays.equals(bytes, empty)) {
                    count++;
                }
                System.out.println("You are lucky! " + count);
            } catch (Exception e) {
                throw new IllegalStateException(e);
            }
        }
    }

    public static void main(String[] args) throws Exception {
        Class.forName(InnerClass.class.getName());
    }
}


================================================
FILE: test\test\instrument\CpuBurner.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package test.instrument;

import java.time.Duration;
import java.util.Random;

public class CpuBurner {
    private static final Random random = new Random();

    static void burn(Duration duration) {
        long start = System.nanoTime();
        while (System.nanoTime() - start < duration.toNanos()) {
            long n = random.nextLong();
            if (Long.toString(n).hashCode() == 0) {
                System.out.println(n);
            }
        }
    }

    public static void main(String[] args) throws InterruptedException {
        Thread t1 = new Thread(() -> {
            burn(Duration.ofMillis(500));
            burn(Duration.ofMillis(10));
        }, "thread1");
        Thread t2 = new Thread(() -> {
            burn(Duration.ofMillis(300));
            burn(Duration.ofMillis(30));
            burn(Duration.ofMillis(150));
        }, "thread2");
        Thread t3 = new Thread(() -> burn(Duration.ofMillis(50)), "thread3");
        Thread t4 = new Thread(() -> burn(Duration.ofMillis(10)), "thread4");
        t1.start();
        t2.start();
        t3.start();
        t4.start();
        t1.join();
        t2.join();
        t3.join();
        t4.join();
    }
}


================================================
FILE: test\test\instrument\CpuBurnerManyTargets.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package test.instrument;

import java.time.Duration;
import java.util.Random;

public class CpuBurnerManyTargets {

    static void burn1(Duration duration) {
        CpuBurner.burn(duration);
    }

    static void burn2(Duration duration) {
        CpuBurner.burn(duration);
    }

    public static void main(String[] args) throws InterruptedException {
        Thread t1 = new Thread(() -> burn1(Duration.ofMillis(50)), "thread1");
        Thread t2 = new Thread(() -> burn2(Duration.ofMillis(10)), "thread2");
        t1.start();
        t2.start();
    }
}


================================================
FILE: test\test\instrument\InstrumentTests.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package test.instrument;

import one.profiler.test.*;

import jdk.jfr.consumer.RecordedEvent;
import jdk.jfr.consumer.RecordingFile;
import java.time.Duration;
import java.io.*;
import java.nio.file.Files;
import java.util.HashMap;


// Append '-Xlog:redefine+class+exceptions*' to jvmArgs for more detailed
// reports from verification errors.
public class InstrumentTests {

    private static final String MAIN_METHOD_SEGMENT = "^test\\/instrument\\/Recursive\\.main";
    private static final String RECURSIVE_METHOD_SEGMENT = ";test\\/instrument\\/Recursive\\.recursive";

    @Test(
        mainClass = CpuBurner.class,
        agentArgs = "start,threads,event=test.instrument.CpuBurner.burn,collapsed,file=%f",
        jvmArgs   = "-Xverify:all",
        output    = true,
        error     = true
    )
    public void instrument(TestProcess p) throws Exception {
        Output out = p.waitForExit("%f");
        assertNoVerificationErrors(p);
        assert p.exitCode() == 0;

        assertAllCallsRecorded(out);
    }

    @Test(
        mainClass = CpuBurner.class,
        agentArgs = "start,threads,event=test.instrument.CpuBurner.burn(Ljava/time/Duration;)V,collapsed,file=%f",
        jvmArgs   = "-Xverify:all",
        output    = true,
        error     = true
    )
    public void instrumentSignature(TestProcess p) throws Exception {
        Output out = p.waitForExit("%f");
        assertNoVerificationErrors(p);
        assert p.exitCode() == 0;

        assertAllCallsRecorded(out);
    }

    @Test(
        mainClass = CpuBurner.class,
        agentArgs = "start,threads,event=test.instrument.CpuBurner.burn()V,collapsed,file=%f",
        jvmArgs   = "-Xverify:all",
        output    = true,
        error     = true
    )
    public void instrumentWrongSignature(TestProcess p) throws Exception {
        Output out = p.waitForExit("%f");
        assertNoVerificationErrors(p);
        assert p.exitCode() == 0;

        assert !out.contains("CpuBurner\\.burn");
    }

    // Smoke test: if any validation failure happens Instrument::BytecodeRewriter has a bug
    @Test(
        mainClass = CpuBurner.class,
        agentArgs = "start,event=*.*,collapsed,file=%f",
        jvmArgs   = "-Xverify:all",
        output    = true,
        error     = true
    )
    public void instrumentAll(TestProcess p) throws Exception {
        Output out = p.waitForExit("%f");
        assertNoVerificationErrors(p);
        assert p.exitCode() == 0;

        assert out.contains("java\\/lang\\/Thread\\.run ");
        assert out.contains("java\\/lang\\/String\\.<init> ");
    }

    @Test(
        mainClass = CpuBurner.class,
        agentArgs = "start,event=*.<init>,collapsed,file=%f",
        jvmArgs   = "-Xverify:all",
        output    = true,
        error     = true
    )
    public void instrumentAllInit(TestProcess p) throws Exception {
        Output out = p.waitForExit("%f");
        assertNoVerificationErrors(p);
        assert p.exitCode() == 0;

        assert !out.contains("java\\/lang\\/Thread\\.run ");
        assert out.contains("java\\/lang\\/Thread\\.<init> ");
        assert out.contains("java\\/lang\\/String\\.<init> ");
    }

    @Test(
        mainClass = CpuBurner.class,
        agentArgs = "start,event=java.lang.*.<init>,collapsed,file=%f",
        jvmArgs   = "-Xverify:all",
        output    = true,
        error     = true
    )
    public void instrumentAllJavaLangInit(TestProcess p) throws Exception {
        Output out = p.waitForExit("%f");
        assertNoVerificationErrors(p);
        assert p.exitCode() == 0;

        assert !out.contains("java\\/lang\\/Thread\\.run ");
        assert out.contains("java\\/lang\\/Thread\\.<init> ");
        assert out.contains("java\\/lang\\/String\\.<init> ");
    }

    @Test(
        mainClass = CpuBurner.class,
        agentArgs = "start,event=java.lang.Thread.<in*,collapsed,file=%f",
        jvmArgs   = "-Xverify:all",
        output    = true,
        error     = true
    )
    public void instrumentThreadInitWildcard(TestProcess p) throws Exception {
        Output out = p.waitForExit("%f");
        assertNoVerificationErrors(p);
        assert p.exitCode() == 0;

        assert !out.contains("java\\/lang\\/Thread\\.run ");
        assert !out.contains("java\\/lang\\/String\\.<init> ");
        assert out.contains("java\\/lang\\/Thread\\.<init> ");
    }

    @Test(
        mainClass = CpuBurner.class,
        agentArgs = "start,event=java.lang.Thread.*,collapsed,file=%f",
        jvmArgs   = "-Xverify:all",
        output    = true,
        error     = true
    )
    public void instrumentAllMethodsInClass(TestProcess p) throws Exception {
        Output out = p.waitForExit("%f");
        assertNoVerificationErrors(p);
        assert p.exitCode() == 0;

        assert out.contains("java\\/lang\\/Thread\\.run ");
        assert out.contains("java\\/lang\\/Thread\\.<init>

================================================
FILE: test\test\instrument\MethodTracingStop.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package test.instrument;

import one.profiler.*;

import java.time.Duration;
import java.util.Random;

public class MethodTracingStop {

    private static void func1() {}

    public static void main(String[] args) throws Exception {
        AsyncProfiler profiler = AsyncProfiler.getInstance();

        // Phase 1: latency profiling
        profiler.execute("start,trace=test.instrument.MethodTracingStop.func1");
        profiler.stop();

        // Phase 2: profile another method
        profiler.execute("start,trace=test.instrument.AnotherClass.func2");
        func1();
        String output = profiler.dumpCollapsed(Counter.SAMPLES);
        profiler.stop();

        // If output is not empty, the instrumentation from the previous
        // call wasn't properly cleared. That's wrong.
        assert output.isEmpty() : output;
    }
}


================================================
FILE: test\test\instrument\Recursive.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package test.instrument;

import java.time.Duration;
import java.util.Random;

public class Recursive {
    private static final long MAX_RECURSION = 3;

    static void recursive(long recursionCount) throws InterruptedException {
        if (recursionCount > MAX_RECURSION) return;
        Thread.sleep((MAX_RECURSION - recursionCount) * 200);
        recursive(recursionCount+1);
    }

    public static void main(String[] args) throws InterruptedException {
        recursive(0);
    }
}


================================================
FILE: test\test\jfr\CpuLoad.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package test.jfr;

public class CpuLoad {

    private static void sleep(long millis) {
        try {
            Thread.sleep(millis);
        } catch (InterruptedException e) {
            throw new RuntimeException(e);
        }
    }

    private static long cpuLoad() {
        long count = 0;
        for (int i = 0; i < 100_000; i++) {
            count += System.getProperties().hashCode();
        }
        return count;
    }

    private static void normalCpuLoad() {
        long startTime = System.currentTimeMillis();

        while (System.currentTimeMillis() - startTime < 4000) {
            cpuLoad();
            sleep(20);
        }
    }

    private static void cpuSpike() {
        long startTime = System.currentTimeMillis();

        while (System.currentTimeMillis() - startTime < 500) {
            cpuLoad();
        }
    }

    public static void main(String[] args) throws Exception {
        Thread thread = new Thread(CpuLoad::normalCpuLoad);
        thread.start();

        sleep(2000);
        cpuSpike();
        thread.join();
    }
}


================================================
FILE: test\test\jfr\JfrCpuProfiling.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package test.jfr;

public class JfrCpuProfiling {
    private static volatile int value;

    private static void method1() {
        long startTime = System.currentTimeMillis();
        while (System.currentTimeMillis() - startTime < 10) {
            value +=  System.getProperties().hashCode();
        }
    }

    public static void main(String[] args) throws Exception {
        while (true) {
            method1();
        }
    }
}


================================================
FILE: test\test\jfr\JfrMultiModeProfiling.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package test.jfr;

import java.lang.management.ManagementFactory;
import java.lang.management.ThreadInfo;
import java.lang.management.ThreadMXBean;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Date;
import java.util.List;
import java.util.Map;
import java.util.Random;
import java.util.concurrent.CompletableFuture;
import java.util.concurrent.ConcurrentHashMap;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.ThreadLocalRandom;
import java.util.concurrent.TimeUnit;

/**
 * Process to simulate lock contention and allocate objects.
 */
public class JfrMultiModeProfiling {
    private static final Object lock = new Object();

    private static volatile Object sink;
    private static int count = 0;
    private static final List<byte[]> holder = new ArrayList<>();

    private static final ThreadMXBean tmx = ManagementFactory.getThreadMXBean();
    private static final Map<Long, Boolean> threadIds = new ConcurrentHashMap<>();

    static {
        tmx.setThreadContentionMonitoringEnabled(true);
    }

    public static void main(String[] args) throws InterruptedException {
        ExecutorService executor = Executors.newFixedThreadPool(2);
        List<CompletableFuture<Void>> futures = new ArrayList<>();

        for (int i = 0; i < 10; i++) {
            futures.add(CompletableFuture.runAsync(JfrMultiModeProfiling::cpuIntensiveIncrement, executor));
        }
        allocate();
        futures.forEach(CompletableFuture::join);

        long[] ids = threadIds.keySet().stream().mapToLong(Long::longValue).toArray();
        Arrays.stream(tmx.getThreadInfo(ids)).mapToLong(ThreadInfo::getBlockedTime).forEach(System.out::println);

        executor.shutdown();
        executor.awaitTermination(10, TimeUnit.SECONDS);
    }

    private static void cpuIntensiveIncrement() {
        threadIds.putIfAbsent(Thread.currentThread().getId(), Boolean.TRUE);

        for (int i = 0; i < 100_000; i++) {
            synchronized (lock) {
                count += System.getProperties().hashCode();
            }
        }
    }

    private static void allocate() {
        long start = System.currentTimeMillis();
        Random random = ThreadLocalRandom.current();
        while (System.currentTimeMillis() - start <= 1000) {
            if (random.nextBoolean()) {
                sink = new byte[65536];
            } else {
                sink = String.format("some string: %s, some number: %d", new Date(), random.nextInt());
            }
            if (holder.size() < 100_000) {
                holder.add(new byte[1]);
            }
        }
    }
}


================================================
FILE: test\test\jfr\JfrTests.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package test.jfr;

import jdk.jfr.consumer.RecordedEvent;
import jdk.jfr.consumer.RecordingFile;
import one.profiler.test.Assert;
import one.profiler.test.Os;
import one.profiler.test.Output;
import one.profiler.test.Test;
import one.profiler.test.TestProcess;
import test.alloc.Hello;

import java.time.Instant;
import java.time.temporal.ChronoUnit;
import java.util.*;

public class JfrTests {

    @Test(mainClass = CpuLoad.class, agentArgs = "start,event=cpu,file=%profile.jfr")
    public void cpuLoad(TestProcess p) throws Exception {
        p.waitForExit();
        assert p.exitCode() == 0;

        String jfrOutPath = p.getFilePath("%profile");
        String spikePattern = "test/jfr/CpuLoad.cpuSpike.*";
        String normalLoadPattern = "test/jfr/CpuLoad.normalCpuLoad.*";

        Output out = Output.convertJfrToCollapsed(jfrOutPath, "--to", "1500");
        assert !out.contains(spikePattern);
        assert out.contains(normalLoadPattern);

        out = Output.convertJfrToCollapsed(jfrOutPath,"--from", "1500", "--to", "3500");
        assert out.contains(spikePattern);
        assert out.contains(normalLoadPattern);

        out = Output.convertJfrToCollapsed(jfrOutPath,"--from", "3500");
        assert !out.contains(spikePattern);
        assert out.contains(normalLoadPattern);
    }

    @Test(mainClass = CpuLoad.class, agentArgs = "start,event=cpu,wall,record-cpu,file=%profile.jfr", os = Os.LINUX)
    public void recordCpuMultiEngine(TestProcess p) throws Exception {
        p.waitForExit();
        assert p.exitCode() == 0;

        Output out = Output.convertJfrToCollapsed(p.getFilePath("%profile"), "--wall");
        assert !out.contains("^CPU-\\d+;");

        out = Output.convertJfrToCollapsed(p.getFilePath("%profile"), "--cpu");
        assert out.contains("^CPU-\\d+;");
    }

    /**
     * Test to validate JDK APIs to parse Cpu profiling JFR output
     *
     * @param p The test process to profile with.
     * @throws Exception Any exception thrown during profiling JFR output parsing.
     */
    @Test(mainClass = JfrCpuProfiling.class)
    public void parseRecording(TestProcess p) throws Exception {
        p.profile("-d 3 -e cpu -f %f.jfr");
        StringBuilder builder = new StringBuilder();
        try (RecordingFile recordingFile = new RecordingFile(p.getFile("%f").toPath())) {
            while (recordingFile.hasMoreEvents()) {
                RecordedEvent event = recordingFile.readEvent();
                builder.append(event);
            }
        }

        String parsedOut = builder.toString();
        assert parsedOut.contains("jdk.ExecutionSample");
        assert parsedOut.contains("test.jfr.JfrCpuProfiling.method1()");
    }

    /**
     * Test to validate JDK APIs to parse Multimode profiling JFR output
     *
     * @param p The test process to profile with.
     * @throws Exception Any exception thrown during profiling JFR output parsing.
     */
    @Test(mainClass = JfrMultiModeProfiling.class, agentArgs = "start,event=cpu,alloc,lock=0,quiet,jfr,file=%f", output = true)
    public void parseMultiModeRecording(TestProcess p) throws Exception {
        Output output = p.waitForExit(TestProcess.STDOUT);
        assert p.exitCode() == 0;

        long totalLockDurationMillis = output.stream().mapToLong(Long::parseLong).sum();

        double jfrTotalLockDurationMillis = 0;
        Map<String, Integer> eventsCount = new HashMap<>();
        try (RecordingFile recordingFile = new RecordingFile(p.getFile("%f").toPath())) {
            while (recordingFile.hasMoreEvents()) {
                RecordedEvent event = recordingFile.readEvent();
                String eventName = event.getEventType().getName();
                if (eventName.equals("jdk.JavaMonitorEnter")) {
                    jfrTotalLockDurationMillis += event.getDuration().toNanos() / 1_000_000.0;
                }
                eventsCount.put(eventName, eventsCount.getOrDefault(eventName, 0) + 1);
            }
        }

        Assert.isGreater(eventsCount.get("jdk.ExecutionSample"), 50);
        Assert.isGreater(eventsCount.get("jdk.JavaMonitorEnter"), 10);
        Assert.isGreater(jfrTotalLockDurationMillis / totalLockDurationMillis, 0.80);
        Assert.isGreater(eventsCount.get("jdk.ObjectAllocationInNewTLAB"), 50);
    }

    /**
     * Test to validate profiling output with "--all" flag without event override.
     *
     * @param p The test process to profile with.
     * @throws Exception Any exception thrown during profiling JFR output parsing.
     */
    @Test(mainClass = JfrMultiModeProfiling.class, agentArgs = "start,all,file=%f.jfr", nameSuffix = "noOverride")
    @Test(mainClass = JfrMultiModeProfiling.class, agentArgs = "start,all,alloc=262143,file=%f.jfr", nameSuffix = "overrideAlloc")
    public void allModeNoEventOverride(TestProcess p) throws Exception {
        p.waitForExit();
        assert p.ex

================================================
FILE: test\test\jfr\Ttsp.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package test.jfr;

import java.lang.management.ManagementFactory;
import java.lang.reflect.Field;
import sun.misc.Unsafe;

public class Ttsp {
    private static final long RUN_DURATION_MS = 3_000;
    private static final long SAFEPOINT_INTERVAL_MS = 200;
    private static final long MEMORY_SIZE = 500 * 1024 * 1024;

    static void requestSafepoint() {
        ManagementFactory.getThreadMXBean().dumpAllThreads(false, false);
    }

    static Unsafe getUnsafe() {
        try {
            Field f = Unsafe.class.getDeclaredField("theUnsafe");
            f.setAccessible(true);
            return (Unsafe) f.get(null);
        } catch (Exception exception) {
            throw new RuntimeException(exception);
        }
    }

    static void delaySafepoint() {
        Unsafe unsafe = getUnsafe();
        long address = unsafe.allocateMemory(MEMORY_SIZE);

        long value = 0;
        while (!Thread.interrupted()) {
            unsafe.setMemory(address, MEMORY_SIZE, (byte) (value++ % Byte.MAX_VALUE + 1));
        }

        unsafe.freeMemory(address);
    }

    public static void main(String[] args) throws Exception {
        long start = System.nanoTime();
        long end = start + RUN_DURATION_MS * 1_000_000;

        Thread safepointerDelayerThread = new Thread(Ttsp::delaySafepoint);
        safepointerDelayerThread.start();

        while (System.nanoTime() < end) {
            requestSafepoint();
            Thread.sleep(SAFEPOINT_INTERVAL_MS);
        }

        safepointerDelayerThread.interrupt();
        safepointerDelayerThread.join();
    }
}


================================================
FILE: test\test\jfrconverter\JfrconverterTests.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package test.jfrconverter;

import test.otlp.CpuBurner;
import one.convert.*;
import one.jfr.JfrReader;
import one.jfr.event.Event;
import one.jfr.event.EventCollector;
import one.jfr.StackTrace;
import one.profiler.test.*;

// Simple smoke tests for JFR converter. The output is not inspected for errors,
// we only verify that the conversion completes successfully.
public class JfrconverterTests {

    @Test(mainClass = CpuBurner.class, agentArgs = "start,jfr,all,file=%f")
    public void heatmapConversion(TestProcess p) throws Exception {
        Output out = p.waitForExit("%f");
        assert p.exitCode() == 0;
        JfrToHeatmap.convert(p.getFilePath("%f"), "/dev/null", new Arguments("--alloc"));
        JfrToHeatmap.convert(p.getFilePath("%f"), "/dev/null", new Arguments("--cpu"));
    }

    @Test(mainClass = CpuBurner.class, agentArgs = "start,jfr,all,file=%f")
    public void flamegraphConversion(TestProcess p) throws Exception {
        Output out = p.waitForExit("%f");
        assert p.exitCode() == 0;
        JfrToFlame.convert(p.getFilePath("%f"), "/dev/null", new Arguments());
        JfrToFlame.convert(p.getFilePath("%f"), "/dev/null", new Arguments("--alloc"));
    }

    @Test(mainClass = Tracer.class, agentArgs = "start,jfr,wall,trace=test.jfrconverter.Tracer.traceMethod,file=%f")
    public void latencyFilter(TestProcess p) throws Exception {
        Output out = p.waitForExit("%f");
        assert p.exitCode() == 0;

        try (JfrReader jfr = new JfrReader(p.getFilePath("%f"))) {
            boolean[] found = new boolean[4];
            long minLatency = Tracer.TRACE_DURATION_MS - 10; // just to be sure
            JfrConverter converter = new JfrConverter(jfr, new Arguments("--wall", "--latency", minLatency + "")) {
                protected void convertChunk() {
                    collector.forEach(new EventCollector.Visitor() {
                        public void visit(Event event, long samples, long value) {
                            found[0] = true;

                            StackTrace stackTrace = jfr.stackTraces.get(event.stackTraceId);
                            if (stackTrace == null) return;

                            long[] methods = stackTrace.methods;
                            byte[] types = stackTrace.types;
                            for (int i = methods.length; --i >= 0; ) {
                                String methodName = getMethodName(methods[i], types[i]);
                                if (!methodName.startsWith("test/jfrconverter/Tracer.showcase")) continue;

                                int idx = Integer.parseInt(methodName.charAt(methodName.length() - 1) + "");
                                found[idx] = true;
                                break;
                            }
                        }
                    });
                }
            };
            converter.convert();

            assert found[0] : "No events found!";
            assert found[1];
            assert found[2];
            assert !found[3];
        }
    }
}


================================================
FILE: test\test\jfrconverter\Tracer.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package test.jfrconverter;

import java.util.concurrent.CountDownLatch;

final class Tracer {

    static final long TRACE_DURATION_MS = 500;
    private static final long SLEEP_DURATION_MS = 200;

    private static void traceMethod(CountDownLatch latch) throws InterruptedException {
        latch.await();
    }

    private static void showcase1() throws InterruptedException {
        Thread.sleep(SLEEP_DURATION_MS);
    }

    private static void showcase2() throws InterruptedException {
        Thread.sleep(SLEEP_DURATION_MS);
    }

    private static void showcase3() throws InterruptedException {
        Thread.sleep(SLEEP_DURATION_MS);
    }

    public static void main(String[] args) throws InterruptedException {
        CountDownLatch latch1 = new CountDownLatch(1);
        long startNanos = System.nanoTime();
        Thread t1 = new Thread(() -> {
            try {
                traceMethod(latch1);
            } catch (InterruptedException exception) {}
        }, "thread1");
        t1.start();

        // While traceMethod is waiting, we can do some stuff and expect to see it
        // as part of the trace
        showcase1();
        showcase2();

        while (System.nanoTime() - startNanos < TRACE_DURATION_MS * 1_000_000) {
            Thread.sleep(50);
        }
        latch1.countDown();
        t1.join();

        CountDownLatch latch2 = new CountDownLatch(1);
        Thread t2 = new Thread(() -> {
            try {
                traceMethod(latch2);
            } catch (InterruptedException exception) {}
        }, "thread2");
        t2.start();

        // This should be filtered away, we won't let the trace last enough
        showcase3();

        latch2.countDown();
        t2.join();
    }
}


================================================
FILE: test\test\kernel\KernelTests.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package test.kernel;

import one.profiler.test.Output;
import one.profiler.test.Test;
import one.profiler.test.TestProcess;
import one.profiler.test.Os;

import java.io.IOException;

public class KernelTests {

    @Test(mainClass = ListFiles.class, os = Os.LINUX)
    public void kernel(TestProcess p) throws Exception {
        Output out = p.profile("-e cpu-clock -d 3 -i 1ms -o collapsed");
        Output err = p.readFile(TestProcess.PROFERR);
        assert out.contains("test/kernel/ListFiles.listFiles;java/io/File");
        assert err.contains("Kernel symbols are unavailable") || out.contains("(sys|SyS)_getdents");

        out = p.profile("stop -o flamegraph");
        out = out.convertFlameToCollapsed();
        assert out.contains("java/io/File.list");
        assert err.contains("Kernel symbols are unavailable") || out.contains("(sys|SyS)_getdents");
    }

    @Test(mainClass = ListFiles.class, os = Os.LINUX)
    public void fdtransfer(TestProcess p) throws Exception {
        p.profile("-e cpu -d 3 -i 1ms -o collapsed -f %f --fdtransfer", true);
        Output out = p.readFile("%f");
        assert out.contains("test/kernel/ListFiles.listFiles;java/io/File");
        assert out.contains("(sys|SyS)_getdents");
    }

    @Test(mainClass = ListFiles.class, os = Os.LINUX)
    public void kprobe(TestProcess p) throws Exception {
        p.profile("-e kprobe:fd_install -d 2 -o collapsed -f %f --fdtransfer", true);
        Output out = p.readFile("%f");
        assert out.contains("java/io/File.list;.+;fd_install_\\[k]");
    }

    @Test(mainClass = ListFiles.class, os = {Os.MACOS, Os.WINDOWS})
    public void notLinux(TestProcess p) throws Exception {
        try {
            p.profile("-e cpu -d 3 -i 1ms -o collapsed -f %f --fdtransfer");
            throw new AssertionError("FdTransferClient should succeed on Linux only");
        } catch (IOException e) {
            assert p.readFile(TestProcess.PROFERR).contains("Failed to initialize FdTransferClient");
        }
    }
}


================================================
FILE: test\test\kernel\ListFiles.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package test.kernel;

import java.io.File;

public class ListFiles {
    private static volatile int value;

    private static void listFiles() {
        for (String s : new File("/").list()) {
            value += s.hashCode();
        }
    }

    public static void main(String[] args) {
        while (true) {
            listFiles();
        }
    }
}


================================================
FILE: test\test\lock\DatagramTest.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package test.lock;

import java.net.InetSocketAddress;
import java.nio.Buffer;
import java.nio.ByteBuffer;
import java.nio.channels.DatagramChannel;
import java.util.concurrent.Executor;
import java.util.concurrent.Executors;
import java.util.concurrent.atomic.AtomicLong;

/**
 * This test sends UDP datagrams in 10 threads simultaneously
 * and calculates the total throughput (packets/s).
 * <p>
 * The default DatagramChannel in Java NIO demonstrates poor performance
 * because of the synchronized block inside send() method.
 * <p>
 * Use async-profiler's lock profiling mode (-e lock)
 * to find the source of lock contention.
 */
public class DatagramTest {
    private static final AtomicLong totalPackets = new AtomicLong();
    private static DatagramChannel ch;

    public static void sendLoop() {
        final ByteBuffer buf = ByteBuffer.allocateDirect(1000);
        final InetSocketAddress remoteAddr = new InetSocketAddress("127.0.0.1", 5556);

        try {
            for (int i = 0; ; i++) {
                ((Buffer) buf).clear();
                ch.send(buf, remoteAddr);
                totalPackets.incrementAndGet();
                if ((i % 1000) == 0) {
                    Thread.yield();  // give other threads chance to acquire a lock
                }
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public static void main(String[] args) throws Exception {
        ch = DatagramChannel.open();
        ch.bind(new InetSocketAddress(0));
        ch.configureBlocking(false);

        Executor pool = Executors.newCachedThreadPool();
        for (int i = 0; i < 10; i++) {
            pool.execute(DatagramTest::sendLoop);
        }
    }
}


================================================
FILE: test\test\lock\LockTests.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package test.lock;

import one.profiler.test.Output;
import one.profiler.test.Test;
import one.profiler.test.TestProcess;

public class LockTests {

    @Test(mainClass = DatagramTest.class, debugNonSafepoints = true, jvmVer = {11, Integer.MAX_VALUE})
    public void datagramSocketLock(TestProcess p) throws Exception {
        Output out = p.profile("-e cpu -d 3 -o collapsed --cstack dwarf");
        assert out.ratio("(ReentrantLock.lock|ReentrantLock.unlock)") > 0.1;
        assert out.contains("ReentrantLock.lock");
        assert out.contains("ReentrantLock.unlock");
        assert out.contains("Unsafe.park");
        assert out.contains("Unsafe.unpark");
        out = p.profile("-e lock -d 3 -o collapsed");
        assert out.contains("sun/nio/ch/DatagramChannelImpl.send");
    }
}


================================================
FILE: test\test\nativelock\AllNativeLocks.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package test.nativelock;

import java.util.ArrayList;
import java.util.List;

public class AllNativeLocks {

    public static void main(String[] args) throws InterruptedException {
        final boolean once = args.length > 0 && args[0].equals("once");

        NativeLock.class.getName();
        Thread.sleep(500);

        if (once) {
            runAllLockTypesOnce();
        } else {
            while (true) {
                runAllLockTypesOnce();
                Thread.sleep(100);
            }
        }
    }

    private static void runAllLockTypesOnce() throws InterruptedException {
        List<Thread> threads = new ArrayList<>();

        for (int i = 0; i < 2; i++) {
            Thread t = new Thread(() -> NativeLock.mutexContentionThread());
            threads.add(t);
            t.start();
        }

        for (int i = 0; i < 2; i++) {
            Thread t = new Thread(() -> NativeLock.rdlockContentionThread());
            threads.add(t);
            t.start();
        }

        for (int i = 0; i < 2; i++) {
            Thread t = new Thread(() -> NativeLock.wrlockContentionThread());
            threads.add(t);
            t.start();
        }

        for (Thread t : threads) {
            t.join();
        }
    }
}


================================================
FILE: test\test\nativelock\NativeLock.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package test.nativelock;

public class NativeLock {
    static {
        System.loadLibrary("jninativelocks");
    }

    public static native void mutexContentionThread();
    public static native void rdlockContentionThread();
    public static native void wrlockContentionThread();
}


================================================
FILE: test\test\nativelock\NativelockTests.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package test.nativelock;

import one.profiler.test.Os;
import one.profiler.test.Output;
import one.profiler.test.Test;
import one.profiler.test.TestProcess;

public class NativelockTests {

    @Test(mainClass = AllNativeLocks.class)
    public void canAsprofTraceAllLockTypes(TestProcess p) throws Exception {
        Output out = p.profile("-e nativelock -d 3 -o collapsed");
        assert out.contains("pthread_mutex_lock_hook") : "No mutex samples captured";
        assert out.contains("pthread_rwlock_rdlock_hook") : "No rdlock samples captured";
        assert out.contains("pthread_rwlock_wrlock_hook") : "No wrlock samples captured";
    }

    @Test(mainClass = AllNativeLocks.class, agentArgs = "start,nativelock,collapsed,file=%f", args = "once")
    public void canAgentTraceAllLockTypes(TestProcess p) throws Exception {
        Output out = p.waitForExit("%f");
        assert out.contains("pthread_mutex_lock_hook") : "No mutex samples captured in agent mode";
        assert out.contains("pthread_rwlock_rdlock_hook") : "No rdlock samples captured in agent mode";
        assert out.contains("pthread_rwlock_wrlock_hook") : "No wrlock samples captured in agent mode";
    }

    @Test(mainClass = AllNativeLocks.class, os = Os.LINUX, args = "once", env = { "LD_PRELOAD=%lib", "ASPROF_COMMAND=start,nativelock,file=%f.jfr" })
    public void ldpreloadAllLockTypes(TestProcess p) throws Exception {
        p.waitForExit();
        Output out = Output.convertJfrToCollapsed(p.getFilePath("%f"), "--nativelock");
        assert out.contains("pthread_mutex_lock_hook") : "No mutex samples captured with LD_PRELOAD";
        assert out.contains("pthread_rwlock_rdlock_hook") : "No rdlock samples captured with LD_PRELOAD";
        assert out.contains("pthread_rwlock_wrlock_hook") : "No wrlock samples captured with LD_PRELOAD";
    }

    @Test(sh = "LD_PRELOAD=%lib ASPROF_COMMAND=start,nativelock,file=%f.jfr %testbin/native_lock_contention", os = Os.LINUX)
    public void nativeAllLockContention(TestProcess p) throws Exception {
        p.waitForExit();
        Output out = Output.convertJfrToCollapsed(p.getFilePath("%f"), "--nativelock");
        assert out.contains("pthread_mutex_lock_hook") : "No mutex samples captured in pure native test";
        assert out.contains("pthread_rwlock_rdlock_hook") : "No rdlock samples captured in pure native test";
        assert out.contains("pthread_rwlock_wrlock_hook") : "No wrlock samples captured in pure native test";
    }
}


================================================
FILE: test\test\nativemem\CallsAllNoLeak.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package test.nativemem;

public class CallsAllNoLeak {

    private static final int NUM_THREADS = 8; // Number of threads

    private static final int MALLOC_SIZE = 1999993; // Prime size, useful in assertions.
    private static final int CALLOC_SIZE = 2000147;
    private static final int REALLOC_SIZE = 30000170;
    private static final int POSIX_MEMALIGN_SIZE = 30000193;
    private static final int ALIGNED_ALLOC_SIZE = 30002016;

    private static void doMallocRealloc() {
        long ptr = Native.malloc(MALLOC_SIZE);
        long reallocd = Native.realloc(ptr, REALLOC_SIZE);
        Native.free(reallocd);
    }

    private static void doCalloc() {
        long ptr = Native.calloc(1, CALLOC_SIZE);
        Native.free(ptr);
    }

    private static void doPosixMemalign() {
        long ptr = Native.posixMemalign(16, POSIX_MEMALIGN_SIZE);
        Native.free(ptr);
    }

    private static void doAlignedAlloc() {
        long ptr = Native.alignedAlloc(16, ALIGNED_ALLOC_SIZE);
        Native.free(ptr);
    }

    private static void do_work(boolean once) {
        try {
            do {
                doMallocRealloc();
                doCalloc();
                doPosixMemalign();
                doAlignedAlloc();

                Thread.sleep(1);
            } while (!once);
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
            System.err.println("Thread interrupted: " + Thread.currentThread().getName());
        }
    }

    public static void main(String[] args) throws InterruptedException {
        final boolean once = args.length > 0 && args[0].equals("once");

        final Thread[] threads = new Thread[NUM_THREADS];
        for (int i = 0; i < NUM_THREADS; i++) {
            threads[i] = new Thread(() -> do_work(once), "MemoryTask-" + i);
            threads[i].start();
        }

        for (Thread thread : threads) {
            thread.join();
        }
    }
}


================================================
FILE: test\test\nativemem\CallsMallocCalloc.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package test.nativemem;

public class CallsMallocCalloc {

    private static final int MALLOC_SIZE = 1999993; // Prime size, useful in assertions.
    private static final int CALLOC_SIZE = 2000147;

    public static void main(String[] args) throws InterruptedException {
        final boolean once = args.length > 0 && args[0].equals("once");

        do {
            Native.malloc(MALLOC_SIZE);
            Native.calloc(1, CALLOC_SIZE);

            // allocate every 1 second.
            Thread.sleep(1000);
        } while (!once);
    }
}


================================================
FILE: test\test\nativemem\CallsRealloc.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package test.nativemem;

public class CallsRealloc {

    private static final int MALLOC_SIZE = 1999993; // Prime size, useful in assertions.
    private static final int REALLOC_SIZE = 30000170;

    public static void main(String[] args) throws InterruptedException {
        final boolean once = args.length > 0 && args[0].equals("once");

        do {
            long addr = Native.malloc(MALLOC_SIZE);
            long reallocd = Native.realloc(addr, REALLOC_SIZE);

            // allocate every 1 second.
            Thread.sleep(1000);
        } while (!once);
    }
}


================================================
FILE: test\test\nativemem\Native.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package test.nativemem;

public class Native {
    static {
        System.loadLibrary("jnimalloc");
    }

    public static native long malloc(long size);

    public static native long realloc(long addr, long size);

    public static native long calloc(long num, long size);

    public static native long free(long addr);

    public static native long posixMemalign(long alignment, long size);

    public static native long alignedAlloc(long alignment, long size);
}


================================================
FILE: test\test\nativemem\NativememTests.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package test.nativemem;

import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import one.jfr.JfrReader;
import one.jfr.event.MallocEvent;

import one.profiler.test.Assert;
import one.profiler.test.Os;
import one.profiler.test.Output;
import one.profiler.test.Test;
import one.profiler.test.TestProcess;

public class NativememTests {

    private static final int MALLOC_SIZE = 1999993;
    private static final int MALLOC_DYN_SIZE = 2000003;
    private static final int CALLOC_SIZE = 2000147;
    private static final int REALLOC_SIZE = 30000170;
    private static final int POSIX_MEMALIGN_SIZE = 30000193;
    private static final int ALIGNED_ALLOC_SIZE = 30002016;

    @Test(mainClass = CallsMallocCalloc.class, agentArgs = "start,nativemem,total,cstack=fp,collapsed,file=%f", args = "once", nameSuffix = "FP")
    @Test(mainClass = CallsMallocCalloc.class, agentArgs = "start,nativemem,total,cstack=vm,collapsed,file=%f", args = "once", nameSuffix = "VM")
    public void canAgentTraceMallocCalloc(TestProcess p) throws Exception {
        Output out = p.waitForExit("%f");

        Assert.isEqual(out.samples("Java_test_nativemem_Native_malloc"), MALLOC_SIZE);
        Assert.isEqual(out.samples("Java_test_nativemem_Native_calloc"), CALLOC_SIZE);
    }

    @Test(mainClass = CallsMallocCalloc.class, agentArgs = "start,nativemem=10000000,total,collapsed,file=%f", args = "once")
    public void canAgentFilterMallocCalloc(TestProcess p) throws Exception {
        Output out = p.waitForExit("%f");
        Assert.isEqual(out.samples("Java_test_nativemem_Native_malloc"), 0);
        Assert.isEqual(out.samples("Java_test_nativemem_Native_calloc"), 0);
    }

    @Test(mainClass = CallsMallocCalloc.class)
    public void canAsprofTraceMallocCalloc(TestProcess p) throws Exception {
        Output out = p.profile("-e nativemem --total -o collapsed -d 2");
        long samplesMalloc = out.samples("Java_test_nativemem_Native_malloc");
        long samplesCalloc = out.samples("Java_test_nativemem_Native_calloc");

        Assert.isGreater(samplesMalloc, 0);
        Assert.isGreater(samplesCalloc, 0);
        Assert.isEqual(samplesMalloc % MALLOC_SIZE, 0);
        Assert.isEqual(samplesCalloc % CALLOC_SIZE, 0);
    }

    @Test(mainClass = CallsRealloc.class, agentArgs = "start,nativemem,total,collapsed,file=%f", args = "once")
    public void canAgentTraceRealloc(TestProcess p) throws Exception {
        Output out = p.waitForExit("%f");

        Assert.isEqual(out.samples("Java_test_nativemem_Native_malloc"), MALLOC_SIZE);
        Assert.isEqual(out.samples("Java_test_nativemem_Native_realloc"), REALLOC_SIZE);
    }

    @Test(mainClass = CallsRealloc.class)
    public void canAsprofTraceRealloc(TestProcess p) throws Exception {
        Output out = p.profile("-e nativemem --total -o collapsed -d 2");
        long samplesMalloc = out.samples("Java_test_nativemem_Native_malloc");
        long samplesRealloc = out.samples("Java_test_nativemem_Native_realloc");

        Assert.isGreater(samplesMalloc, 0);
        Assert.isGreater(samplesRealloc, 0);
        Assert.isEqual(samplesMalloc % MALLOC_SIZE, 0);
        Assert.isEqual(samplesRealloc % REALLOC_SIZE, 0);
    }

    @Test(mainClass = CallsAllNoLeak.class)
    public void canAsprofTraceAllNoLeak(TestProcess p) throws Exception {
        Output out = p.profile("-e nativemem --total -o collapsed -d 2");

        long samplesMalloc = out.samples("Java_test_nativemem_Native_malloc");
        long samplesCalloc = out.samples("Java_test_nativemem_Native_calloc");
        long samplesRealloc = out.samples("Java_test_nativemem_Native_realloc");
        long samplesPosixMemalign = out.samples("Java_test_nativemem_Native_posixMemalign");
        long samplesAlignedAlloc = out.samples("Java_test_nativemem_Native_alignedAlloc");

        Assert.isGreater(samplesMalloc, 0);
        Assert.isGreater(samplesCalloc, 0);
        Assert.isGreater(samplesRealloc, 0);
        Assert.isGreater(samplesPosixMemalign, 0);
        Assert.isGreater(samplesAlignedAlloc, 0);

        Assert.isEqual(samplesMalloc % MALLOC_SIZE, 0);
        Assert.isEqual(samplesCalloc % CALLOC_SIZE, 0);
        Assert.isEqual(samplesRealloc % REALLOC_SIZE, 0);
        Assert.isEqual(samplesPosixMemalign % POSIX_MEMALIGN_SIZE, 0);
        Assert.isEqual(samplesAlignedAlloc % ALIGNED_ALLOC_SIZE, 0);
    }

    private static Map<Long, Long> assertNoLeaks(TestProcess p) throws Exception {
        p.waitForExit();
        String filename = p.getFilePath("%f");

        boolean nofree = Arrays.asList(p.inputs()).contains("nofree");
        boolean hasFree = false;
        Map<Long, Long> sizeCounts = new HashMap<>();

        try (JfrReader r = new JfrReader(filename)) {
            List<MallocEvent> events = r.readAllEvents(MallocEvent.class);
            assert !events.isEmpty() : "No MallocEvent 

================================================
FILE: test\test\nonjava\JavaClass.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package test.nonjava;

public class JavaClass {

    public static double cpuHeavyTask() {
        double sum = 0;
        for (int i = 0; i < 100000; i++) {
            sum += Math.sqrt(Math.random());
            sum += Math.pow(Math.random(), Math.random());
        }
        return sum;
    }
}


================================================
FILE: test\test\nonjava\NonjavaTests.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package test.nonjava;

import one.profiler.test.Output;
import one.profiler.test.Test;
import one.profiler.test.TestProcess;

public class NonjavaTests {

    // jvm is loaded before the profiling session is started
    @Test(sh = "%testbin/non_java_app 1 %s.collapsed", output = true)
    public void jvmFirst(TestProcess p) throws Exception {
        p.waitForExit();
        assert p.exitCode() == 0;

        Output out = p.readFile("%s");
        assert out.contains("cpuHeavyTask");
    }

    // jvm is loaded after the profiling session is started
    @Test(sh = "%testbin/non_java_app 2 %s.collapsed", output = true)
    public void profilerFirst(TestProcess p) throws Exception {
        p.waitForExit();
        assert p.exitCode() == 0;

        Output out = p.readFile("%s");
        assert !out.contains("cpuHeavyTask");
    }

    // jvm is loaded between two profiling sessions
    @Test(sh = "%testbin/non_java_app 3 %f.collapsed %s.collapsed", output = true)
    public void jvmInBetween(TestProcess p) throws Exception {
        p.waitForExit();
        assert p.exitCode() == 0;

        Output out = p.readFile("%f");
        assert out.contains("nativeBurnCpu");
        assert !out.contains("cpuHeavyTask");

        out = p.readFile("%s");
        assert out.contains("nativeBurnCpu");
        assert out.contains("cpuHeavyTask");
    }

    // jvm is loaded before the profiling session is started on a different thread
    @Test(sh = "%testbin/non_java_app 4 %s.collapsed", output = true)
    public void differentThread(TestProcess p) throws Exception {
        p.waitForExit();
        assert p.exitCode() == 0;

        Output out = p.readFile("%s");
        assert out.contains("cpuHeavyTask");
    }
}


================================================
FILE: test\test\otlp\CpuBurner.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package test.otlp;

import java.lang.Thread;
import java.time.Duration;
import java.time.Instant;
import java.util.Random;

public class CpuBurner {
    private static final Random RANDOM = new Random();
    static final Duration TEST_DURATION = Duration.ofSeconds(1);

    static void burn() {
        long n = RANDOM.nextLong();
        if (Long.toString(n).hashCode() == 0) {
            System.out.println(n);
        }
    }

    public static void main(String[] args) throws InterruptedException {
        Thread worker = new Thread(() -> {
            Instant start = Instant.now();
            while (Duration.between(start, Instant.now()).compareTo(TEST_DURATION) < 0) {
                burn();
            }
        }, "CpuBurnerWorker");
        worker.start();
        worker.join();
    }
}


================================================
FILE: test\test\otlp\OtlpProfileTimeTest.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */
package test.otlp;

import one.profiler.AsyncProfiler;
import one.profiler.Events;
import io.opentelemetry.proto.profiles.v1development.*;

public class OtlpProfileTimeTest {

    public static void main(String[] args) throws Exception {
        AsyncProfiler profiler = AsyncProfiler.getInstance();
        profiler.start(Events.CPU, 1_000_000);

        Profile profile1 = dumpAndGetProfile(profiler);
        long timeNano1 = profile1.getTimeUnixNano();
        long durationNano1 = profile1.getDurationNano();

        Thread.sleep(100);

        Profile profile2 = dumpAndGetProfile(profiler);
        long timeNano2 = profile2.getTimeUnixNano();
        long durationNano2 = profile2.getDurationNano();

        assert timeNano1 == timeNano2 : String.format("%d, %d", timeNano1, timeNano2);
        assert durationNano2 - durationNano1 >= 100_000_000L : String.format("%d, %d", durationNano2, durationNano1);

        profiler.stop();
        profiler.start(Events.CPU, 1_000_000);

        Profile profile3 = dumpAndGetProfile(profiler);
        long timeNano3 = profile3.getTimeUnixNano();

        assert timeNano3 > timeNano1 : String.format("%d, %d", timeNano3, timeNano1);

        profiler.stop();
    }

    public static Profile dumpAndGetProfile(AsyncProfiler profiler) throws Exception {
        byte[] dump = profiler.dumpOtlp();
        ProfilesData data = ProfilesData.parseFrom(dump);
        return data.getResourceProfiles(0).getScopeProfiles(0).getProfiles(0);
    }
}


================================================
FILE: test\test\otlp\OtlpTests.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package test.otlp;

import java.io.ByteArrayOutputStream;
import java.nio.file.Path;
import java.nio.file.Files;
import java.util.*;
import java.util.stream.Collectors;
import java.time.*;

import one.convert.JfrToOtlp;
import one.convert.Arguments;
import one.jfr.JfrReader;
import one.profiler.test.*;

import io.opentelemetry.proto.common.v1.AnyValue;
import io.opentelemetry.proto.profiles.v1development.*;

public class OtlpTests {
    @Test(mainClass = CpuBurner.class, agentArgs = "start,otlp,event=itimer,file=%f.pb")
    public void sampleType(TestProcess p) throws Exception {
        ProfilesData profilesData = waitAndGetProfilesData(p);

        ValueType sampleType = getProfile(profilesData, 0).getSampleType();
        assertString(profilesData.getDictionary().getStringTable(sampleType.getTypeStrindex()), "itimer");
        assertString(profilesData.getDictionary().getStringTable(sampleType.getUnitStrindex()), "count");
    }

    @Test(mainClass = CpuBurner.class, agentArgs = "start,otlp,event=itimer,total,file=%f.pb")
    public void sampleTypeTotal(TestProcess p) throws Exception {
        ProfilesData profilesData = waitAndGetProfilesData(p);

        ValueType sampleType = getProfile(profilesData, 0).getSampleType();
        assertString(profilesData.getDictionary().getStringTable(sampleType.getTypeStrindex()), "itimer");
        assertString(profilesData.getDictionary().getStringTable(sampleType.getUnitStrindex()), "ns");
    }

    private static void assertString(String actual, String expected) {
        assert expected.equals(actual) : actual;
    }

    @Test(mainClass = CpuBurner.class, agentArgs = "start,otlp,threads,file=%f.pb")
    public void threadName(TestProcess p) throws Exception {
        ProfilesData profilesData = waitAndGetProfilesData(p);
        checkThreadNames(getProfile(profilesData, 0), profilesData.getDictionary());
    }

    @Test(mainClass = CpuBurner.class, agentArgs = "start,jfr,file=%f")
    public void threadNameFromJfr(TestProcess p) throws Exception {
        Output out = p.waitForExit("%f");
        assert p.exitCode() == 0;

        ProfilesData profilesData = profilesDataFromJfr(p.getFilePath("%f"), new Arguments("--cpu", "--output", "otlp"));
        checkThreadNames(getProfile(profilesData, 0), profilesData.getDictionary());
    }

    private static void checkThreadNames(Profile profile, ProfilesDictionary dictionary) {
        Set<String> threadNames = new HashSet<>();
        for (Sample sample : profile.getSamplesList()) {
            Optional<AnyValue> threadName = getAttribute(sample, dictionary, "thread.name");
            if (!threadName.isPresent()) continue;
            threadNames.add(threadName.get().getStringValue());
        }
        assert threadNames.stream().anyMatch(name -> name.contains("CpuBurnerWorker")) : "CpuBurner thread not found: " + threadNames;
    }

    @Test(mainClass = CpuBurner.class, agentArgs = "start,otlp,file=%f.pb")
    public void samples(TestProcess p) throws Exception {
        ProfilesData profilesData = waitAndGetProfilesData(p);
        checkSamples(getProfile(profilesData, 0), profilesData.getDictionary());
    }

    @Test(mainClass = CpuBurner.class, agentArgs = "start,jfr,file=%f")
    public void samplesFromJfr(TestProcess p) throws Exception {
        Output out = p.waitForExit("%f");
        assert p.exitCode() == 0;

        ProfilesData profilesData = profilesDataFromJfr(p.getFilePath("%f"), new Arguments("--cpu", "--output", "otlp"));
        checkSamples(getProfile(profilesData, 0), profilesData.getDictionary());
    }

    private static void checkSamples(Profile profile, ProfilesDictionary dictionary) {
        Output collapsed = toCollapsed(profile, dictionary);
        assert collapsed.containsExact("test/otlp/CpuBurner.lambda$main$0;test/otlp/CpuBurner.burn") : collapsed;
    }

    @Test(mainClass = OtlpProfileTimeTest.class)
    public void profileTime(TestProcess p) throws Exception {
        classpathCheck();

        p.waitForExit();
        assert p.exitCode() == 0;
    }

    @Test(mainClass = CpuBurner.class, agentArgs = "start,jfr,file=%f")
    public void profileTimeFromJfr(TestProcess p) throws Exception {
        Output out = p.waitForExit("%f");
        assert p.exitCode() == 0;

        ProfilesData profilesData = profilesDataFromJfr(p.getFilePath("%f"), new Arguments("--cpu", "--output", "otlp"));
        Profile profile = getProfile(profilesData, 0);
        Instant before = Instant.now()
                                .minus(CpuBurner.TEST_DURATION)
                                .minus(Duration.ofSeconds(10)); // just to be sure
        Instant actual = Instant.ofEpochSecond(0, profile.getTimeUnixNano());
        assert actual.isAfter(before) : actual;
    }

    private static ProfilesData waitAndGetProfilesData(TestProcess p) throws Exception {
        p.waitForExit();
        assert p.exit

================================================
FILE: test\test\pmu\Dictionary.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package test.pmu;

import java.util.concurrent.ThreadLocalRandom;

/**
 * This demo shows the importance of hardware performance counters.
 * Two tests (test16K and test8M) execute the same number of
 * operations, however, test16K completes much quicker than test8M.
 * <p>
 * CPU profiling shows no difference between two tests,
 * but cache-misses profiling highlights test8M
 * as the problematic method.
 */
public class Dictionary {

    private static void testRandomRead(long[] array, int bound) {
        long startTime = System.nanoTime();

        for (long i = 0; i < Integer.MAX_VALUE; i++) {
            int index = ThreadLocalRandom.current().nextInt(bound);
            array[index]++;
        }

        long endTime = System.nanoTime();
        System.out.printf("Time spent: %.3f\n", (endTime - startTime) / 1e9);
    }

    public static void test16K() {
        long[] array = new long[8 * 1024 * 1024];
        testRandomRead(array, 16384);
    }

    public static void test8M() {
        long[] array = new long[8 * 1024 * 1024];
        testRandomRead(array, 8 * 1024 * 1024);
    }

    public static void main(String[] args) {
        new Thread(Dictionary::test16K).start();
        new Thread(Dictionary::test8M).start();
    }
}


================================================
FILE: test\test\pmu\PmuTests.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package test.pmu;

import one.profiler.test.Arch;
import one.profiler.test.Output;

import java.io.IOException;

import one.profiler.test.Assert;
import one.profiler.test.Test;
import one.profiler.test.TestProcess;
import one.profiler.test.Os;

public class PmuTests {

    @Test(mainClass = Dictionary.class, os = Os.LINUX)
    public void cycles(TestProcess p) throws Exception {
        try {
            p.profile("-e ref-cycles -d 3 -o collapsed -f %f");
            Output out = p.readFile("%f");
            // We are skipping the test in one case, for more details: https://github.com/actions/runner-images/issues/11689
            if (out.total() == 0 &&
                    System.getProperty("os.arch").contains("aarch64") &&
                    "true".equals(System.getenv("GITHUB_ACTIONS"))) {
                System.out.println("Skipping the test PmuTests.cycles on ARM64 in GitHub Actions as no samples have been collected");
                return;
            }

            Assert.isGreater(out.ratio("test/pmu/Dictionary.test16K"), 0.4);
            Assert.isGreater(out.ratio("test/pmu/Dictionary.test8M"), 0.4);
        } catch (Exception e) {
            if (!p.readFile(TestProcess.PROFERR).contains("Perf events unavailable")) {
                throw e;
            }
        }
    }

    @Test(mainClass = Dictionary.class, os = Os.LINUX, arch = {Arch.X64, Arch.X86})
    public void cacheMisses(TestProcess p) throws Exception {
        try {
            p.profile("-e cache-misses -d 3 -o collapsed -f %f");

            // TODO: https://github.com/async-profiler/async-profiler/issues/1588
            //  It was observed on certain system configuration that the 'cache-misses' event will not be collected,
            //  both async-profiler & perf are failing to collect samples & reporting 0 with no obvious cause,
            //  the test is marked as pass if such a condition is encountered until that is root caused
            if (p.getFile("%f").length() != 0) {
                Output out = p.readFile("%f");
                Assert.isLess(out.ratio("test/pmu/Dictionary.test16K"), 0.2);
                Assert.isGreater(out.ratio("test/pmu/Dictionary.test8M"), 0.8);
            }
        } catch (Exception e) {
            if (!p.readFile(TestProcess.PROFERR).contains("Perf events unavailable")) {
                throw e;
            }
        }
    }

    @Test(mainClass = Dictionary.class, os = Os.MACOS)
    public void pmuIncompatible(TestProcess p) throws Exception {
        try {
            p.profile("-e cache-misses -d 3 -o collapsed -f %f");
            throw new AssertionError("PerfEvents should succeed on Linux only");
        } catch (IOException e) {
            assert p.readFile(TestProcess.PROFERR).contains("PerfEvents are not supported on this platform");
        }
    }
}


================================================
FILE: test\test\proc\BasicApp.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package test.proc;

import java.util.ArrayList;
import java.util.List;
import java.util.Random;


public class BasicApp {
    private static final Random random = new Random();

    public static long[] fibUpToLongMax() {
        List<Long> tmp = new ArrayList<>();

        long a = 0L;
        long b = 1L;
        tmp.add(a);
        tmp.add(b);

        while (true) {
            try {
                long next = Math.addExact(a, b);
                tmp.add(next);
                a = b;
                b = next;
            } catch (ArithmeticException overflow) {
                break;
            }
        }

        long[] result = new long[tmp.size()];
        for (int i = 0; i < tmp.size(); i++) {
            result[i] = tmp.get(i);
        }
        return result;
    }

    public static void main(String[] args) throws Exception {
        while (true) {
            long[] fib = fibUpToLongMax();
            int randIndex = random.nextInt(fib.length);
            if (randIndex % 31 == -1) {
                System.out.print(fib[randIndex]);
            }
        }
    }
}


================================================
FILE: test\test\proc\CpuIntensiveApp.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package test.proc;

public class CpuIntensiveApp {

    public static void main(String[] args) throws Exception {
        long start = System.currentTimeMillis();
        while (System.currentTimeMillis() - start < 12000) {
            for (int i = 0; i < 1000000; i++) {
                Math.sqrt(Math.random() * 1000000);
            }
        }
    }
}


================================================
FILE: test\test\proc\IoIntensiveApp.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package test.proc;

import java.util.Random;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.ByteBuffer;
import java.nio.channels.FileChannel;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.StandardOpenOption;


public class IoIntensiveApp {
    private static final Random random = new Random();
    private static final int BLOCK = 64 * 1024 * 1024;

    public static void main(String[] args) throws Exception {
        Path tmp = Files.createTempFile("proc-test", ".tmp");

        // burn some cpu to pass the min cpu % threshold
        new Thread(() -> {
            while (true) {
                long n = random.nextLong();
                if (Long.toString(n).hashCode() == 0) {
                    System.out.println(n);
                }
            }
        }).start();

        // write
        byte[] payload = new byte[BLOCK];
        random.nextBytes(payload);

        try (FileChannel ch = FileChannel.open(tmp, StandardOpenOption.CREATE, StandardOpenOption.WRITE,
                StandardOpenOption.DSYNC)) {
            ByteBuffer buf = ByteBuffer.wrap(payload);
            while (buf.hasRemaining()) {
                ch.write(buf);
            }

            ch.force(true);
        }

        // read
        try (FileChannel f = FileChannel.open(tmp, StandardOpenOption.READ)) {
            ByteBuffer b = ByteBuffer.allocate(BLOCK);
            f.read(b);
        }

        Thread.sleep(20000);
    }
}


================================================
FILE: test\test\proc\ManyProcessApp.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package test.proc;

import java.util.ArrayList;
import java.util.List;

public class ManyProcessApp {

    public static void main(String[] args) throws Exception {
        List<Process> procs = new ArrayList<>();

        for (int i = 0; i < 5000; i++) {
            ProcessBuilder pb = new ProcessBuilder("sleep", "10");
            procs.add(pb.start());
        }

        for (Process p : procs) {
            p.waitFor();
        }

        Thread.sleep(3000);
    }
}


================================================
FILE: test\test\proc\MemoryIntensiveApp.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package test.proc;

import java.util.ArrayList;
import java.util.List;

public class MemoryIntensiveApp {

    public static void main(String[] args) throws Exception {
        List<byte[]> memory = new ArrayList<>();
        for (int i = 0; i < 100; i++) {
            memory.add(new byte[1024 * 1024]); // 1MB each
            Thread.sleep(100);
        }

        Thread.sleep(5000);
    }
}


================================================
FILE: test\test\proc\MultiThreadApp.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package test.proc;

import java.util.concurrent.CountDownLatch;

public class MultiThreadApp {
    public static void main(String[] args) throws Exception {
        int threadCount = 8;
        CountDownLatch latch = new CountDownLatch(threadCount);

        for (int i = 0; i < threadCount; i++) {
            final int threadId = i;
            new Thread(() -> {
                try {

                    long start = System.currentTimeMillis();
                    while (System.currentTimeMillis() - start < 12000) {
                        for (int j = 0; j < 1000000; j++) {
                            Math.sqrt(Math.random() * 1000000);
                        }
                    }

                    Thread.sleep(8000);
                } catch (InterruptedException e) {
                    Thread.currentThread().interrupt();
                } finally {
                    latch.countDown();
                }
            }, "WorkerThread-" + threadId).start();
        }

        latch.await();
    }
}


================================================
FILE: test\test\proc\ProcTests.java
================================================
/*
 * Copyright the async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package test.proc;

import one.jfr.JfrReader;
import one.jfr.event.ProcessSample;
import one.profiler.test.*;

import java.io.IOException;
import java.util.List;
import java.util.stream.Collectors;
import java.util.Comparator;

public class ProcTests {

    @Test(mainClass = BasicApp.class, os = Os.LINUX)
    public void basicProcessSampling(TestProcess p) throws Exception {
        p.profile("--proc 1 -d 3 -f %f.jfr");
        try (JfrReader jfr = new JfrReader(p.getFilePath("%f"))) {
            List<ProcessSample> events = jfr.readAllEvents(ProcessSample.class);
            assert !events.isEmpty();

            List<ProcessSample> appSamples = events.stream()
                    .filter(e -> e.cmdLine != null && e.cmdLine.contains("BasicApp"))
                    .collect(Collectors.toList());

            Assert.isEqual(appSamples.size(), 2); // We discard the first sample
        }
    }

// TODO(issue-1432): Re-enable after tiered integration tests are supported.
//     @Test(mainClass = BasicApp.class, os = Os.LINUX)
    public void processSamplingWithZeroSamplingPeriod(TestProcess p) throws Exception {
        p.profile("--proc 0 -d 2 -f %f.jfr");
        try (JfrReader jfr = new JfrReader(p.getFilePath("%f"))) {
            List<ProcessSample> events = jfr.readAllEvents(ProcessSample.class);

            assert events.isEmpty();
        }
    }

//     @Test(mainClass = BasicApp.class, os = Os.LINUX)
    public void processEvenSamplingInterval(TestProcess p) throws Exception {
        long startTime = System.currentTimeMillis();
        p.profile("--proc 2 -d 8 -f %f.jfr");

        try (JfrReader jfr = new JfrReader(p.getFilePath("%f"))) {
            List<ProcessSample> events = jfr.readAllEvents(ProcessSample.class);

            List<ProcessSample> appSamples = events.stream()
                    .filter(e -> e.cmdLine != null && e.cmdLine.contains("BasicApp"))
                    .collect(Collectors.toList());

            Assert.isEqual(appSamples.size(), 3);
        }
    }

//     @Test(mainClass = BasicApp.class, os = Os.LINUX)
    public void processSamplingWithAllMode(TestProcess p) throws Exception {
        p.profile("--all -d 60 -f %f.jfr", false, 61);
        try (JfrReader jfr = new JfrReader(p.getFilePath("%f"))) {
            List<ProcessSample> procEvents = jfr.readAllEvents(ProcessSample.class);
            assert !procEvents.isEmpty();
        }
    }

//     @Test(mainClass = BasicApp.class, os = Os.LINUX)
    public void validateProcessFields(TestProcess p) throws Exception {
        p.profile("--proc 1 -d 5 -f %f.jfr");
        try (JfrReader jfr = new JfrReader(p.getFilePath("%f"))) {
            List<ProcessSample> events = jfr.readAllEvents(ProcessSample.class);
            assert !events.isEmpty();

            ProcessSample sample = events.stream()
                    .filter(e -> e.cmdLine != null && e.cmdLine.contains("BasicApp"))
                    .findAny()
                    .orElse(null);

            assert sample != null;

            Assert.isGreater(sample.pid, 0);
            Assert.isGreaterOrEqual(sample.ppid, 0);
            assert sample.name != null && !sample.name.isEmpty();
            assert sample.cmdLine != null;
            Assert.isGreaterOrEqual(sample.uid, 0);
            Assert.isNotEqual(sample.state, 0);
            Assert.isGreater(sample.processStartTime, 0);
            Assert.isGreater(sample.cpuUser, 0);
            Assert.isGreater(sample.cpuSystem, 0);
            Assert.isGreater(sample.cpuPercent, 0);
            Assert.isGreater(sample.threads, 0);
            Assert.isGreaterOrEqual(sample.vmSize, 0);
            Assert.isGreaterOrEqual(sample.vmRss, 0);
            Assert.isGreaterOrEqual(sample.rssAnon, 0);
            Assert.isGreaterOrEqual(sample.rssFiles, 0);
            Assert.isGreaterOrEqual(sample.rssShmem, 0);
            Assert.isGreaterOrEqual(sample.minorFaults, 0);
            Assert.isGreaterOrEqual(sample.majorFaults, 0);
            Assert.isGreaterOrEqual(sample.ioRead, 0);
            Assert.isGreaterOrEqual(sample.ioWrite, 0);
        }
    }

//     @Test(mainClass = IoIntensiveApp.class, os = Os.LINUX)
    public void validateIoStats(TestProcess p) throws Exception {
        p.profile("--proc 1 -d 8 -f %f.jfr");
        try (JfrReader jfr = new JfrReader(p.getFilePath("%f"))) {
            List<ProcessSample> events = jfr.readAllEvents(ProcessSample.class);
            assert !events.isEmpty();

            ProcessSample sample = events.stream()
                    .filter(e -> e.cmdLine != null && e.cmdLine.contains("IoIntensiveApp"))
                    .max(Comparator.comparingLong(e -> e.time))
                    .orElse(null);

            assert sample != null;

            Assert.isGreaterOrEqual(sample.ioRead, 0);
            Assert.isGreaterOrEqual(sample.ioWrite, 64 * 1024);
        }
    }

//     @Test(main

================================================
FILE: test\test\proc\ShortLivedApp.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package test.proc;

import java.util.ArrayList;
import java.util.List;

public class ShortLivedApp {

    private static final String[] DD_CMD = {"timeout", "2", "dd", "if=/dev/zero", "of=/dev/null", "bs=1M", "status=none"};

    public static void main(String[] args) throws Exception {
        while (true) {
            for (int i = 0; i < 10; i++) {
                new ProcessBuilder(DD_CMD).start();
            }
            Thread.sleep(500);
        }
    }
}


================================================
FILE: test\test\recovery\CodingIntrinsics.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package test.recovery;

import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.Arrays;
import java.util.Base64;
import java.util.Random;
import java.util.zip.Adler32;
import java.util.zip.CRC32;
import java.util.zip.Checksum;

/**
 * This test runs popular checksum and digest algorithms
 * that have corresponding compiler intrinsics in HotSpot JVM.
 * These intrinsics do not maintain common frame layout
 * and thus are tricky for stack unwinding.
 */
public class CodingIntrinsics {
    static volatile long sink;

    public static void main(String[] args) {
        byte[][] arrays = new byte[1025][];

        Random random = new Random(123);
        for (int i = 0; i < arrays.length; i++) {
            arrays[i] = new byte[i];
            random.nextBytes(arrays[i]);
        }

        for (int i = 0; i < arrays.length; i++) {
            runTest(arrays[i]);
        }
    }

    static void runTest(byte[] input) {
        for (Codec codec : CODECS) {
            sink = runTestWithCodec(codec, input, 10_000);
        }
    }

    static long runTestWithCodec(Codec codec, byte[] input, int count) {
        long n = 0;
        for (int i = 0; i < count; i++) {
            byte[] output = codec.encode(input);
            n += output.length;
            if (output.length <= 16) {
                n += Arrays.hashCode(output);
            }
        }
        return n;
    }

    interface Codec {
        byte[] encode(byte[] input);
    }

    static final Codec[] CODECS = new Codec[]{
            input -> Base64.getEncoder().encode(input),
            input -> checksum(input, new CRC32()),
            input -> checksum(input, new Adler32()),
            input -> digest(input, "MD5"),
            input -> digest(input, "SHA-1"),
            // async-profiler cannot easily unwind sha256_implCompress intrinsic
            // on x86 machines that support AVX2 but not SHA instruction set.
            isArm64() ? input -> digest(input, "SHA-256") : input -> input
    };

    static boolean isArm64() {
        String arch = System.getProperty("os.arch").toLowerCase();
        return arch.equals("aarch64") || arch.contains("arm64");
    }

    static byte[] checksum(byte[] input, Checksum checksum) {
        checksum.update(input, 0, input.length);
        long value = checksum.getValue();
        return new byte[]{
                (byte) (value >>> 24),
                (byte) (value >>> 16),
                (byte) (value >>> 8),
                (byte) value
        };
    }

    static byte[] digest(byte[] input, String algorithm) {
        try {
            MessageDigest md = MessageDigest.getInstance(algorithm);
            return md.digest(input);
        } catch (NoSuchAlgorithmException e) {
            throw new RuntimeException(e);
        }
    }
}


================================================
FILE: test\test\recovery\Numbers.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package test.recovery;

/**
 * In this test, a large amount of time is spent inside the vtable stub
 * and inside the method prologue/epilogue.
 * <p>
 * Most sampling profilers, including AsyncGetCallTrace-based,
 * fail to traverse Java stack in these cases.
 * See https://bugs.openjdk.java.net/browse/JDK-8178287
 */
public class Numbers {
    static volatile double x;

    public static void main(String[] args) {
        loop(123, 45.67, 890L, 33.3f, 999, 787878L, 10.11f, 777L, 0);
    }

    private static void loop(Number... numbers) {
        while (true) {
            x = avg(numbers);
        }
    }

    private static double avg(Number... numbers) {
        double sum = 0;
        for (Number n : numbers) {
            sum += n.doubleValue();
        }
        return sum / numbers.length;
    }
}


================================================
FILE: test\test\recovery\RecoveryTests.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package test.recovery;

import one.profiler.test.Jvm;
import one.profiler.test.Output;
import one.profiler.test.Assert;
import one.profiler.test.Test;
import one.profiler.test.TestProcess;
import one.profiler.test.Arch;

public class RecoveryTests {

    @Test(mainClass = StringBuilderTest.class, jvmArgs = "-XX:UseAVX=2", arch = {Arch.X64, Arch.X86}, debugNonSafepoints = true)
    public void stringBuilder(TestProcess p) throws Exception {
        Output out = p.profile("-d 3 -e cpu --cstack fp -o collapsed");
        Assert.isGreater(out.ratio("StringBuilder.delete;"), 0.8);
        Assert.isGreater(out.ratio("arraycopy"), 0.8);
        Assert.isLess(out.ratio("unknown_Java"), 0.01);

        out = p.profile("-d 2 -e cpu -i 1ms -o collapsed");
        Assert.isGreater(out.ratio("StringBuilderTest.main;java/lang/StringBuilder.delete;"), 0.8);
        Assert.isLess(out.ratio("unknown|break_compiled"), 0.005);
    }

    @Test(
        mainClass = StringBuilderTest.class,
        debugNonSafepoints = true,
        arch = {Arch.ARM64, Arch.ARM32},
        jvm = Jvm.HOTSPOT,
        // C2 often loses PcDesc mapping from arraycopy intrinsic to the original bytecode
        // For now the test is disabled until a solution is found, JDK-8368867
        jvmVer = {8, 17}
    )
    public void stringBuilderArm(TestProcess p) throws Exception {
        Output out = p.profile("-d 3 -e cpu --cstack fp -o collapsed");
        Assert.isGreater(out.ratio("(forward|foward|backward)_copy_longs"), 0.8); // there's a typo on some JDK versions

        out = p.profile("-d 2 -e cpu -i 1ms -o collapsed");
        Assert.isGreater(out.ratio("StringBuilderTest.main;java/lang/StringBuilder.delete;"), 0.8);
        Assert.isLess(out.ratio("unknown|break_compiled"), 0.005);
    }

    @Test(mainClass = Numbers.class, jvm = Jvm.HOTSPOT, debugNonSafepoints = true)
    public void numbers(TestProcess p) throws Exception {
        Output out = p.profile("-d 3 -e cpu --cstack fp -o collapsed");
        if (p.currentJvm() == Jvm.HOTSPOT_C2) Assert.isGreater(out.ratio("vtable stub"), 0.01);
        Assert.isGreater(out.ratio("Numbers.loop"), 0.8);

        out = p.profile("-d 2 -e cpu -i 1ms -o collapsed");
        Assert.isGreater(out.ratio("Numbers.main;test/recovery/Numbers.loop"), 0.8);
        Assert.isGreater(out.ratio("Numbers.main;test/recovery/Numbers.loop;test/recovery/Numbers.avg"), 0.5);
        Assert.isLess(out.ratio("unknown|break_compiled"), 0.005);
    }

    @Test(mainClass = Suppliers.class, jvm = Jvm.HOTSPOT, debugNonSafepoints = true)
    public void suppliers(TestProcess p) throws Exception {
        Output out = p.profile("-d 3 -e cpu --cstack fp -o collapsed");
        if (p.currentJvm() == Jvm.HOTSPOT_C2) Assert.isGreater(out.ratio("itable stub"), 0.01);
        Assert.isGreater(out.ratio("Suppliers.loop"), 0.5);

        out = p.profile("-d 2 -e cpu -i 1ms -o collapsed");
        Assert.isGreater(out.ratio("Suppliers.main;test/recovery/Suppliers.loop"), 0.5);
        Assert.isLess(out.ratio("unknown|break_compiled"), 0.005);
    }

    @Test(mainClass = CodingIntrinsics.class, debugNonSafepoints = true, arch = {Arch.ARM64, Arch.X64})
    public void intrinsics(TestProcess p) throws Exception {
        Output out = p.profile("-d 3 -e cpu -i 1ms -o collapsed");
        Assert.isLess(out.ratio("^\\[unknown"), 0.01, "No more than 1% of unknown frames");
        Assert.isLess(out.ratio("^[^ ;]+(;[^ ;]+)? "), 0.01, "No more than 1% of short stacks");
    }

    // Verify that System.currentTimeMillis() intrinsic is unwound correctly
    // TODO: Enable test on JDK 11 after fixing #1653
    @Test(mainClass = TimeLoop.class, jvm = Jvm.HOTSPOT, jvmVer = {17, Integer.MAX_VALUE}, debugNonSafepoints = true)
    public void currentTimeMillis(TestProcess p) throws Exception {
        Output out = p.profile("-d 3 -e cpu -o collapsed");
        Assert.isLess(out.ratio("^\\[unknown"), 0.01, "No more than 1% of unknown frames");
        Assert.isLess(out.ratio("^\\[break_"), 0.01, "No more than 1% of broken stacks");
        Assert.isLess(out.ratio("^\\[vdso]"), 0.01, "vDSO should have symbol information");
    }
}


================================================
FILE: test\test\recovery\StringBuilderTest.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package test.recovery;

/**
 * This demo shows that most sampling profilers are misleading.
 * The given program appends 5 symbols to the end of StringBuilder
 * and deletes 5 symbols from the beginning of StringBuilder.
 * <p>
 * The real bottleneck here is delete(), since it involves moving
 * of 1 million characters. However, safepoint-based profilers
 * will display Thread.isAlive() as the hottest method.
 * JFR will not report anything useful at all, since it cannot
 * traverse stack traces when JVM is running System.arraycopy().
 */
public class StringBuilderTest {

    public static void main(String[] args) {
        StringBuilder sb = new StringBuilder();
        sb.append(new char[1_000_000]);

        do {
            sb.append(12345);
            sb.delete(0, 5);
        } while (Thread.currentThread().isAlive());
    }
}


================================================
FILE: test\test\recovery\Suppliers.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package test.recovery;

import java.util.function.Supplier;

/**
 * In this test, a large amount of time is spent inside the itable stub.
 * <p>
 * Most sampling profilers, including AsyncGetCallTrace-based,
 * fail to traverse Java stack in these cases.
 * See https://bugs.openjdk.java.net/browse/JDK-8178287
 */
public class Suppliers {

    public static void main(String[] args) {
        Supplier[] suppliers = {
                () -> 0,
                () -> 1.0,
                () -> "abc",
                () -> true
        };

        while (true) {
            loop(suppliers);
        }
    }

    private static void loop(Supplier[] suppliers) {
        for (int i = 0; i >= 0; i++) {
            suppliers[i % suppliers.length].get();
        }
    }
}


================================================
FILE: test\test\recovery\TimeLoop.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package test.recovery;

public class TimeLoop {

    public static void main(String[] args) throws InterruptedException {
        long busyTime = 100;
        long idleTime = 100;

        while (true) {
            long startTime = System.currentTimeMillis();
            while (System.currentTimeMillis() - startTime < busyTime) {
                // Burn CPU
            }
            Thread.sleep(idleTime);
        }
    }
}


================================================
FILE: test\test\smoke\Alloc.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package test.smoke;

import java.util.Random;
import java.util.concurrent.ThreadLocalRandom;

public class Alloc implements Runnable {
    static volatile Object sink;

    public static void main(String[] args) {
        new Thread(new Alloc(), "AllocThread-1").start();
        new Thread(new Alloc(), "AllocThread-2").start();
    }

    @Override
    public void run() {
        Random random = ThreadLocalRandom.current();
        while (true) {
            allocate(random);
        }
    }

    private static void allocate(Random random) {
        if (random.nextBoolean()) {
            sink = new int[128 * 1000];
        } else {
            sink = new Integer[128 * 1000];
        }
    }
}


================================================
FILE: test\test\smoke\Cpu.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package test.smoke;

import java.io.File;

public class Cpu {
    private static volatile int value;

    private static void method1() {
        for (int i = 0; i < 1000000; i++) {
            value++;
        }
    }

    private static void method2() {
        for (int i = 0; i < 1000000; i++) {
            value++;
        }
    }

    private static void method3() throws Exception {
        long startTime = System.nanoTime();
        while (System.nanoTime() - startTime < 2_700_000) {
            for (String s : new File("/").list()) {
                value += s.hashCode();
            }
        }
    }

    public static void main(String[] args) throws Exception {
        System.out.println("Starting...");
        while (true) {
            method1();
            method2();
            method3();
        }
    }
}


================================================
FILE: test\test\smoke\LoadLibrary.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package test.smoke;

import java.lang.management.ClassLoadingMXBean;
import java.lang.management.ManagementFactory;

public class LoadLibrary {

    public static void main(String[] args) throws Exception {
        for (int i = 0; i < 20; i++) {
            Thread.sleep(100);
        }

        // Late load of libmanagement.so
        ClassLoadingMXBean bean = ManagementFactory.getClassLoadingMXBean();

        long n = 0;
        while (n >= 0) {
            n += bean.getLoadedClassCount();
            n += bean.getTotalLoadedClassCount();
            n += bean.getUnloadedClassCount();
        }
    }
}


================================================
FILE: test\test\smoke\SmokeTests.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package test.smoke;

import one.profiler.test.Output;
import one.profiler.test.Test;
import one.profiler.test.TestProcess;

public class SmokeTests {

    @Test(mainClass = Cpu.class)
    public void cpu(TestProcess p) throws Exception {
        Output out = p.profile("-d 3 -e cpu -o collapsed");
        assert out.contains("test/smoke/Cpu.main;test/smoke/Cpu.method1");
        assert out.contains("test/smoke/Cpu.main;test/smoke/Cpu.method2");
        assert out.contains("test/smoke/Cpu.main;test/smoke/Cpu.method3;java/io/File");
    }

    @Test(mainClass = Alloc.class)
    public void alloc(TestProcess p) throws Exception {
        Output out = p.profile("-d 3 -e alloc -o collapsed -t");
        assert out.contains("\\[AllocThread-1 tid=[0-9]+];.*Alloc.allocate;.*java.lang.Integer\\[]");
        assert out.contains("\\[AllocThread-2 tid=[0-9]+];.*Alloc.allocate;.*int\\[]");
    }

    @Test(mainClass = Threads.class, agentArgs = "start,event=cpu,collapsed,threads,file=%f")
    public void threads(TestProcess p) throws Exception {
        Output out = p.waitForExit("%f");
        assert out.contains("\\[ThreadEarlyEnd tid=[0-9]+];.*Threads.methodForThreadEarlyEnd;.*");
        assert out.contains("\\[RenamedThread tid=[0-9]+];.*Threads.methodForRenamedThread;.*");
    }

    @Test(mainClass = LoadLibrary.class)
    public void loadLibrary(TestProcess p) throws Exception {
        p.profile("-f %f -o collapsed -d 4 -i 1ms");
        Output out = p.readFile("%f");
        assert out.contains("Java_sun_management");
    }
}


================================================
FILE: test\test\smoke\Threads.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package test.smoke;

import java.math.BigInteger;

public class Threads {

    public static void main(String[] args) {
        new Thread(new Runnable() {
            @Override
            public void run() {
                methodForThreadEarlyEnd();
            }
        }, "ThreadEarlyEnd").start();

        new Thread(new Runnable() {
            @Override
            public void run() {
                Thread.currentThread().setName("RenamedThread");
                methodForRenamedThread();
            }
        }, "ThreadWillBeRenamed").start();
    }

    static void methodForThreadEarlyEnd() {
        long now = System.currentTimeMillis();
        BigInteger counter = BigInteger.ZERO;
        while (System.currentTimeMillis() - now < 300) {
            counter = counter.nextProbablePrime();
        }
    }

    static void methodForRenamedThread() {
        long now = System.currentTimeMillis();
        BigInteger counter = BigInteger.ZERO;
        while (System.currentTimeMillis() - now < 1000) {
            counter = counter.nextProbablePrime();
        }
    }
}


================================================
FILE: test\test\stackwalker\StackGenerator.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package test.stackwalker;

public class StackGenerator {

    public static native double largeFrame();

    public static native double deepFrame();

    public static native double leafFrame();

    public static native double largeInnerFrame();

    static {
        System.loadLibrary("jninativestacks");
    }

    public static void main(String[] args) {
        if (args.length != 1) {
            System.err.println("Usage: java StackGenerator <largeFrame|deepFrame|leafFrame>");
            System.exit(1);
        }

        if (args[0].equals("largeFrame")) {
            largeFrame();
        } else if (args[0].equals("deepFrame")) {
            deepFrame();
        } else if (args[0].equals("leafFrame")) {
            leafFrame();
        } else if (args[0].equals("largeInnerFrame")) {
            largeInnerFrame();
        } else {
            System.err.println("Unknown test: " + args[0]);
            System.exit(1);
        }
    }
}


================================================
FILE: test\test\stackwalker\StackwalkerTests.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package test.stackwalker;

import one.profiler.test.Output;
import one.profiler.test.Test;
import one.profiler.test.TestProcess;

public class StackwalkerTests {

    private static final String FRAME = "([^\\[;]+;)";
    private static final String OPTIONAL_FRAME = FRAME + "?";

    @Test(mainClass = StackGenerator.class, jvmArgs = "-Xss5m", args = "largeFrame",
            agentArgs = "start,event=cpu,cstack=vmx,file=%f.jfr", nameSuffix = "VMX")
    @Test(mainClass = StackGenerator.class, jvmArgs = "-Xss5m", args = "largeFrame",
            agentArgs = "start,event=cpu,cstack=vm,file=%f.jfr", nameSuffix = "VM")
    public void largeFrame(TestProcess p) throws Exception {
        p.waitForExit();
        assert p.exitCode() == 0;
        Output output = Output.convertJfrToCollapsed(p.getFilePath("%f"));
        assert output.contains("test/stackwalker/StackGenerator.main[^;]*;" +
                "test/stackwalker/StackGenerator.largeFrame[^;]*;" +
                "Java_test_stackwalker_StackGenerator_largeFrame;" +
                "doCpuTask");
    }

    @Test(mainClass = StackGenerator.class, jvmArgs = "-Xss5m", args = "deepFrame",
            agentArgs = "start,event=cpu,cstack=vmx,file=%f.jfr", nameSuffix = "VMX")
    @Test(mainClass = StackGenerator.class, jvmArgs = "-Xss5m", args = "deepFrame",
            agentArgs = "start,event=cpu,cstack=vm,file=%f.jfr", nameSuffix = "VM")
    public void deepStack(TestProcess p) throws Exception {
        p.waitForExit();
        assert p.exitCode() == 0;
        Output output = Output.convertJfrToCollapsed(p.getFilePath("%f"));
        // Cannot reach stack bottom because of the MAX_WALK_SIZE hard limit
        assert output.contains("^break_[^;]+;" +
                "Java_test_stackwalker_StackGenerator_deepFrame;" +
                "generateDeepStack[^;]*;" +
                "generateDeepStack[^;]*;" +
                "generateDeepStack[^;]*;" +
                "generateDeepStack[^;]*;" +
                "generateDeepStack[^;]*;" +
                "generateDeepStack[^;]*;" +
                "generateDeepStack[^;]*;" +
                "doCpuTask");
    }

    @Test(mainClass = StackGenerator.class, jvmArgs = "-Xss5m", args = "leafFrame",
            agentArgs = "start,event=cpu,cstack=vmx,file=%f.jfr")
    public void normalStackVMX(TestProcess p) throws Exception {
        p.waitForExit();
        assert p.exitCode() == 0;
        Output output = Output.convertJfrToCollapsed(p.getFilePath("%f"));
        assert output.contains("^" +
                FRAME +          // Platform-dependent root frame
                OPTIONAL_FRAME + // Platform-dependent
                OPTIONAL_FRAME + // ThreadJavaMain frame could be missing in JDK 8
                "JavaMain;" +
                OPTIONAL_FRAME + // JDK 22 added "invokeStaticMainWithArgs" function
                "jni_CallStaticVoidMethod;" +
                "jni_invoke_static;" +
                "JavaCalls::call_helper;" +
                FRAME +
                "test/stackwalker/StackGenerator.main_\\[0\\];" +
                "test/stackwalker/StackGenerator.leafFrame_\\[0\\];" +
                "Java_test_stackwalker_StackGenerator_leafFrame;" +
                "doCpuTask");
    }

    @Test(mainClass = StackGenerator.class, jvmArgs = "-Xss5m", args = "leafFrame",
            agentArgs = "start,event=cpu,cstack=vm,file=%f.jfr")
    public void normalStackVM(TestProcess p) throws Exception {
        p.waitForExit();
        assert p.exitCode() == 0;
        Output output = Output.convertJfrToCollapsed(p.getFilePath("%f"));
        assert output.contains("^test/stackwalker/StackGenerator.main_\\[0\\];" +
                "test/stackwalker/StackGenerator.leafFrame_\\[0\\];" +
                "Java_test_stackwalker_StackGenerator_leafFrame;" +
                "doCpuTask");
    }

    @Test(mainClass = StackGenerator.class, jvmArgs = "-Xss5m", args = "largeInnerFrame",
            agentArgs = "start,event=cpu,cstack=vm,file=%f.jfr")
    public void largeInnerFrameVM(TestProcess p) throws Exception {
        p.waitForExit();
        assert p.exitCode() == 0;

        Output output = Output.convertJfrToCollapsed(p.getFilePath("%f"));
        assert !output.contains("Java_test_stackwalker_StackGenerator_largeInnerFrame;unknown;largeInnerFrameFinal");
    }
}


================================================
FILE: test\test\vmstructs\VmstructsTests.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package test.vmstructs;

import one.profiler.test.Output;
import one.profiler.test.Test;
import one.profiler.test.TestProcess;
import test.smoke.Alloc;

public class VmstructsTests {

    @Test(mainClass = Alloc.class, jvmArgs = "-XX:StartFlightRecording=filename=%f.jfr,settings=profile")
    public void jnienv(TestProcess p) throws Exception {
        Output out = p.profile("-d 2 --wall 50ms -F jnienv -o collapsed");
        assert out.contains("Alloc.allocate");
    }

    @Test(mainClass = Alloc.class, jvmArgs = "-XX:StartFlightRecording=filename=%f.jfr,settings=profile",
            agentArgs = "start,wall=50ms,features=jnienv")
    public void jnienvAgent(TestProcess p) throws Exception {
        Thread.sleep(2000);
        Output out = p.profile("stop -o collapsed");
        assert out.contains("Alloc.allocate");
    }
}


================================================
FILE: test\test\vtable\VtableTests.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package test.vtable;

import one.profiler.test.*;
import test.recovery.Numbers;
import test.recovery.Suppliers;

public class VtableTests {

    @Test(mainClass = Numbers.class, jvm = Jvm.HOTSPOT_C2)
    public void vtableStubs(TestProcess p) throws Exception {
        Output out = p.profile("-d 3 -e cpu -i 1ms -F vtable -o collapsed");
        assert out.contains("Numbers.avg;vtable stub;java.lang.Integer_\\[i]");
        assert out.contains("Numbers.avg;vtable stub;java.lang.Long_\\[i]");
    }

    @Test(mainClass = Suppliers.class, jvm = Jvm.HOTSPOT_C2)
    public void itableStubs(TestProcess p) throws Exception {
        Output out = p.profile("-d 3 -e cpu -i 1ms -F comptask,vtable -o collapsed");
        assert out.contains("Suppliers.loop;itable stub;test.recovery.Suppliers[^_]+_\\[i]");
    }
}


================================================
FILE: test\test\wall\BusyClient.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package test.wall;

import java.io.InputStream;
import java.net.Socket;

class BusyClient extends Thread {

    @Override
    public void run() {
        try {
            byte[] buf = new byte[4096];

            Socket s = new Socket(SocketTest.HOST, SocketTest.PORT);

            InputStream in = s.getInputStream();
            while (in.read(buf) >= 0) {
                // keep reading
            }
            System.out.println(Thread.currentThread().getName() + " stopped");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}


================================================
FILE: test\test\wall\IdleClient.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package test.wall;

import java.io.InputStream;
import java.net.Socket;

class IdleClient extends Thread {

    @Override
    public void run() {
        try {
            byte[] buf = new byte[4096];

            Socket s = new Socket(SocketTest.HOST, SocketTest.PORT);

            InputStream in = s.getInputStream();
            while (in.read(buf) >= 0) {
                // keep reading
            }
            System.out.println(Thread.currentThread().getName() + " stopped");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}


================================================
FILE: test\test\wall\SocketTest.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package test.wall;

import java.io.OutputStream;
import java.net.ServerSocket;
import java.util.concurrent.ThreadLocalRandom;

/**
 * This test starts two similar clients. The code of the clients
 * is the same, except that BusyClient constantly receives new data,
 * while IdleClient does almost nothing but waiting for incoming data.
 * <p>
 * Most sampling profilers will not make difference between
 * BusyClient and IdleClient, because JVM does not know whether
 * a native method consumes CPU or just waits inside a blocking call.
 */
public class SocketTest {
    public static final String HOST = "127.0.0.1";
    public static final int PORT = 1234;

    public static void main(String[] args) throws Exception {
        ServerSocket s = new ServerSocket(PORT);

        new IdleClient().start();
        OutputStream idleClient = s.accept().getOutputStream();

        new BusyClient().start();
        OutputStream busyClient = s.accept().getOutputStream();

        byte[] buf = new byte[4096];
        ThreadLocalRandom.current().nextBytes(buf);

        for (int i = 0; ; i++) {
            if ((i % 10_000_000) == 0) {
                idleClient.write(buf, 0, 1);
            } else {
                busyClient.write(buf);
            }
        }
    }
}


================================================
FILE: test\test\wall\WallTests.java
================================================
/*
 * Copyright The async-profiler authors
 * SPDX-License-Identifier: Apache-2.0
 */

package test.wall;

import one.profiler.test.Output;
import one.profiler.test.Assert;
import one.profiler.test.Test;
import one.profiler.test.TestProcess;

public class WallTests {

    @Test(mainClass = SocketTest.class)
    public void cpuWall(TestProcess p) throws Exception {
        Output out = p.profile("-e cpu -d 3 -o collapsed");
        Assert.isGreater(out.ratio("test/wall/SocketTest.main"), 0.25);
        Assert.isGreater(out.ratio("test/wall/BusyClient.run"), 0.25);
        Assert.isLess(out.ratio("test/wall/IdleClient.run"), 0.05);

        out = p.profile("-e wall -d 3 -o collapsed");
        long s1 = out.samples("test/wall/SocketTest.main");
        long s2 = out.samples("test/wall/BusyClient.run");
        long s3 = out.samples("test/wall/IdleClient.run");
        assert s1 > 10 && s2 > 10 && s3 > 10;
        assert Math.abs(s1 - s2) < 5 && Math.abs(s2 - s3) < 5 && Math.abs(s3 - s1) < 5;
    }
}

```

## File: .assets\html\flamegraph.html
```
<!DOCTYPE html>
<html lang='en'>
<head>
<meta charset='utf-8'>
<style>
	body {margin: 0; padding: 10px 10px 22px 10px; background-color: #ffffff}
	h1 {margin: 5px 0 0 0; font-size: 18px; font-weight: normal; text-align: center}
	header {margin: -22px 0 6px 0}
	button {border: none; background: none; width: 24px; height: 24px; cursor: pointer; margin: 0; padding: 2px 0 0 0; text-align: center}
	button:hover {background-color: #ffffe0; outline: 1px solid #ffc000; border-radius: 4px}
	dl {margin: 0 4px 8px 4px}
	dt {margin: 1px; padding: 2px 0; font-weight: bold}
	dd {margin: 1px; padding: 2px 4px}
	dl.frames {float: left; width: 160px}
	dl.hotkeys {clear: left; border-top: 1px solid #666666}
	dl.hotkeys > dt {float: left; clear: left; width: 158px; margin-right: 4px; text-align: right}
	dl.hotkeys > dd {float: left}
	p {position: fixed; bottom: 0; margin: 0; padding: 2px 3px 2px 3px; outline: 1px solid #ffc000; display: none; overflow: hidden; white-space: nowrap; background-color: #ffffe0}
	a {color: #0366d6}
	#legend {padding: 4px; border-radius: 4px; background: #ffffe0; border: 1px solid #666666; display: none}
	#hl {position: absolute; display: none; overflow: hidden; white-space: nowrap; pointer-events: none; background-color: #ffffe0; outline: 1px solid #ffc000; height: 15px}
	#hl span {padding: 0 3px 0 3px}
	#status {left: 0}
	#match {right: 0}
	#reset {cursor: pointer}
	#canvas {width: 100%; height: 576px}
</style>
</head>
<body style='font: 12px Verdana, sans-serif'>
<h1>CPU profile</h1>
<header style='float: left'>
<button id='inverted' title='Invert (I)'><svg xmlns='http://www.w3.org/2000/svg' width='20' height='20' viewBox='0 0 392 392'><path d='M196,36 L316,156 L76,156 Z' fill='#004d80'/><path d='M196,356 L76,236 L316,236 Z' fill='#004d80'/><path d='M196,54 L298,156 L94,156 Z' fill='#ff8d40'/><path d='M196,338 L94,236 L298,236 Z' fill='#40b2ff'/><rect x='94' y='188' width='204' height='16' fill='#004d80'/></svg></button>
<button id='search' title='Search (Ctrl+F)'><svg xmlns='http://www.w3.org/2000/svg' width='20' height='20' viewBox='-39.3 -39.3 471.1 471.1'><circle cx='147.7' cy='147.8' r='125.9' fill='#fff'/><path fill='#40b2ff' d='M370.7 348.7c0 1.4-1.6 6.3-7.2 12.3-6.2 6.7-12.5 9.8-14.7 9.8h-.1c-19.5-1.6-62-43.2-109.6-106.8 9.2-7.2 17.5-15.5 24.6-24.6 63.6 47.6 105.2 90.2 106.8 109.6z'/><path fill='#ff8d40' d='M208.7 86.9l-14.5 14.5c-17.1 17.1-46.5 5-46.5-19.3V61.6c-49 0-88.4 40.8-86.1 90.2 2 43.9 38.1 80 82 82 49.5 2.3 90.2-37.2 90.2-86.1 0-23.7-9.6-45.2-25.1-60.8z'/><path fill='#004d80' d='M276.1 221c12.3-21.5 19.5-46.5 19.5-73.2C295.6 66.3 229.2.1 147.7.1S0 66.3 0 147.9s66.3 147.7 147.7 147.7c26.6 0 51.5-7.1 73.2-19.5 39.8 53.3 91.9 113.5 126.1 116.4 12.3.5 22.9-6.7 32.8-16.7 5.2-5.6 13.8-16.9 12.8-28.8-2.9-34.1-63.1-86.2-116.4-126.1zM147.7 273.8c-69.5 0-125.9-56.5-125.9-125.9S78.3 21.9 147.7 21.9 273.6 78.4 273.6 147.8s-56.4 126-125.9 126zm215.9 87.2c-6.2 6.7-12.4 9.8-14.7 9.8h-.1c-19.5-1.6-62-43.2-109.6-106.8 9.2-7.2 17.5-15.5 24.6-24.6 63.6 47.6 105.2 90.2 106.8 109.6 0 1.4-1.6 6.3-7.2 12.4z'/></svg></button>
<button id='info'><svg xmlns='http://www.w3.org/2000/svg' width='20' height='20' viewBox='0 0 20 20'><circle cx='10' cy='10' r='8' stroke='#004d80' fill='none'/><path d='M10 5.5c-1.25 0-2.25 1-2.25 2.25H9a1.25 1.25 0 0 1 2.5 0c0 .65-.55 1-1 1.2-.7.35-1.25.85-1.25 1.8V11h1.5v-.25c0-.37.29-.65.68-.83.73-.34 1.32-.87 1.32-2.17 0-1.25-1.5-2.25-2.75-2.25' fill='#ff8d40' stroke='#ff8d40' stroke-width='.6' stroke-linecap='round' stroke-linejoin='round'/><circle cx='10' cy='13.5' r='1.2' fill='#ff8d40'/></svg></button>
</header>
<header style='float: right'>Produced by <a href='https://github.com/async-profiler/async-profiler'>async-profiler</a></header>
<div id='legend' style='position: absolute'>
<dl class='frames'>
	<dt>Frame types</dt>
	<dd style='background-color: #e17d00'>Kernel</dd>
	<dd style='background-color: #e15a5a'>Native</dd>
	<dd style='background-color: #c8c83c'>C++ (VM)</dd>
	<dd style='background-color: #50e150'>Java compiled</dd>
	<dd style='background-color: #cce880'>Java compiled by C1</dd>
	<dd style='background-color: #50cccc'>Inlined</dd>
	<dd style='background-color: #b2e1b2'>Interpreted</dd>
</dl>
<dl class='frames'>
	<dt>Allocation profile</dt>
	<dd style='background-color: #50cccc'>Allocated class</dd>
	<dd style='background-color: #e17d00'>Allocation outside TLAB</dd>
	<dt>Lock profile</dt>
	<dd style='background-color: #50cccc'>Lock class</dd>
	<dt>&nbsp;</dt>
	<dt>Search</dt>
	<dd style='background-color: #ee00ee'>Matches regexp</dd>
</dl>
<dl class='hotkeys'>
	<dt>Click frame</dt><dd>Zoom into frame</dd>
	<dt>Alt+Click</dt><dd>Remove stack</dd>
	<dt>0</dt><dd>Reset zoom</dd>
	<dt>I</dt><dd>Invert graph</dd>
	<dt>Ctrl+F</dt><dd>Search</dd>
	<dt>N</dt><dd>Next match</dd>
	<dt>Shift+N</dt><dd>Previous match</dd>
	<dt>Esc</dt><dd>Cancel search</dd>
</dl>
</div>
<canvas id='canvas'></canvas>
<div id='hl'><span></span></div>
<p id='status'></p>
<p id='match'>Matched: <span id='matchval'></span> <span id='reset' title='Clear'>&#x274c;</span></p>
<script>
	// Copyright The async-profiler authors
	// SPDX-License-Identifier: Apache-2.0
	'use strict';
	let root, px, pattern;
	let level0 = 0, left0 = 0, width0 = 0;
	let nav = [], navIndex, matchval;
	let inverted = false;
	const levels = Array(36);
	for (let h = 0; h < levels.length; h++) {
		levels[h] = [];
	}

	const canvas = document.getElementById('canvas');
	const c = canvas.getContext('2d');
	const hl = document.getElementById('hl');
	const status = document.getElementById('status');

	const canvasWidth = canvas.offsetWidth;
	const canvasHeight = canvas.offsetHeight;
	canvas.style.width = canvasWidth + 'px';
	canvas.width = canvasWidth * (devicePixelRatio || 1);
	canvas.height = canvasHeight * (devicePixelRatio || 1);
	if (devicePixelRatio) c.scale(devicePixelRatio, devicePixelRatio);
	c.font = document.body.style.font;

	const palette = [
		[0xb2e1b2, 20, 20, 20],
		[0x50e150, 30, 30, 30],
		[0x50cccc, 30, 30, 30],
		[0xe15a5a, 30, 40, 40],
		[0xc8c83c, 30, 30, 10],
		[0xe17d00, 30, 30,  0],
		[0xcce880, 20, 20, 20],
	];

	function getColor(p) {
		const v = Math.random();
		return '#' + (p[0] + ((p[1] * v) << 16 | (p[2] * v) << 8 | (p[3] * v))).toString(16);
	}

	function f(key, level, left, width, inln, c1, int) {
		levels[level0 = level].push({level, left: left0 += left, width: width0 = width || width0,
			color: getColor(palette[key & 7]), title: cpool[key >>> 3],
			details: (int ? ', int=' + int : '') + (c1 ? ', c1=' + c1 : '') + (inln ? ', inln=' + inln : '')
		});
	}

	function u(key, width, inln, c1, int) {
		f(key, level0 + 1, 0, width, inln, c1, int)
	}

	function n(key, width, inln, c1, int) {
		f(key, level0, width0, width, inln, c1, int)
	}

	function samples(n) {
		return n === 1 ? '1 sample' : n.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ',') + ' samples';
	}

	function pct(a, b) {
		return a >= b ? '100' : (100 * a / b).toFixed(2);
	}

	function findFrame(frames, x) {
		let left = 0;
		let right = frames.length - 1;

		while (left <= right) {
			const mid = (left + right) >>> 1;
			const f = frames[mid];

			if (f.left > x) {
				right = mid - 1;
			} else if (f.left + f.width <= x) {
				left = mid + 1;
			} else {
				return f;
			}
		}

		if (frames[left] && (frames[left].left - x) * px < 0.5) return frames[left];
		if (frames[right] && (x - (frames[right].left + frames[right].width)) * px < 0.5) return frames[right];

		return null;
	}

	function removeStack(left, width) {
		for (let h = 0; h < levels.length; h++) {
			const frames = levels[h], newFrames = [];
			for (let i = 0; i < frames.length; i++) {
				const f = frames[i];
				if (f.left >= left + width) {
					f.left -= width;
				} else if (f.left + f.width > left) {
					if ((f.width -= width) <= 0 && h) continue;
				}
				newFrames.push(f);
			}
			levels[h] = newFrames;
		}
	}

	function search(r) {
		if (r === true && (r = prompt('Enter regexp to search:', '')) === null) {
			return;
		}

		pattern = r ? RegExp(r) : undefined;
		const matched = render(root, nav = []);
		navIndex = -1;
		document.getElementById('matchval').textContent = matchval = pct(matched, root.width) + '%';
		document.getElementById('match').style.display = r ? 'inline-block' : 'none';
	}

	function render(newRoot, nav) {
		if (root) {
			c.fillStyle = '#ffffff';
			c.fillRect(0, 0, canvasWidth, canvasHeight);
		}

		root = newRoot || levels[0][0];
		px = canvasWidth / root.width;

		const x0 = root.left;
		const x1 = x0 + root.width;
		const marked = [];

		function mark(f) {
			return marked[f.left] || (marked[f.left] = f);
		}

		function totalMarked() {
			let total = 0;
			let left = 0;
			Object.keys(marked).sort(function(a, b) { return a - b; }).forEach(function(x) {
				if (+x >= left) {
					const m = marked[x];
					if (nav) nav.push(m);
					total += m.width;
					left = +x + m.width;
				}
			});
			return total;
		}

		function drawFrame(f, y) {
			if (f.left < x1 && f.left + f.width > x0) {
				c.fillStyle = pattern && f.title.match(pattern) && mark(f) ? '#ee00ee' : f.color;
				c.fillRect((f.left - x0) * px, y, f.width * px, 15);

				if (f.width * px >= 21) {
					const chars = Math.floor(f.width * px / 7);
					const title = f.title.length <= chars ? f.title : f.title.substring(0, chars - 2) + '..';
					c.fillStyle = '#000000';
					c.fillText(title, Math.max(f.left - x0, 0) * px + 3, y + 12, f.width * px - 6);
				}

				if (f.level < root.level) {
					c.fillStyle = 'rgba(255, 255, 255, 0.5)';
					c.fillRect((f.left - x0) * px, y, f.width * px, 15);
				}
			}
		}

		for (let h = 0; h < levels.length; h++) {
			const y = inverted ? h * 16 : canvasHeight - (h + 1) * 16;
			const frames = levels[h];
			for (let i = 0; i < frames.length; i++) {
				drawFrame(frames[i], y);
			}
		}

		return totalMarked();
	}

	function unpack(cpool) {
		for (let i = 1; i < cpool.length; i++) {
			cpool[i] = cpool[i - 1].substring(0, cpool[i].charCodeAt(0) - 32) + cpool[i].substring(1);
		}
	}

	canvas.onmousemove = function() {
		const h = Math.floor((inverted ? event.offsetY : (canvasHeight - event.offsetY)) / 16);
		if (h >= 0 && h < levels.length) {
			const f = findFrame(levels[h], event.offsetX / px + root.left);
			if (f) {
				if (f !== root) getSelection().removeAllRanges();
				hl.style.left = (Math.max(f.left - root.left, 0) * px + canvas.offsetLeft) + 'px';
				hl.style.width = (Math.min(f.width, root.width) * px) + 'px';
				hl.style.top = ((inverted ? h * 16 : canvasHeight - (h + 1) * 16) + canvas.offsetTop) + 'px';
				hl.firstChild.textContent = f.title;
				hl.style.display = 'block';
				canvas.title = f.title + '\n(' + samples(f.width) + f.details + ', ' + pct(f.width, levels[0][0].width) + '%)';
				canvas.style.cursor = 'pointer';
				canvas.onclick = function() {
					if (event.altKey && h >= root.level && h > 0) {
						removeStack(f.left, f.width);
						root.width > f.width ? render(root) : render();
					} else if (f !== root) {
						render(f);
					}
					canvas.onmousemove();
				};
				status.textContent = 'Function: ' + canvas.title;
				status.style.display = 'inline-block';
				return;
			}
		}
		canvas.onmouseout();
	}

	canvas.onmouseout = function() {
		hl.style.display = 'none';
		status.style.display = 'none';
		canvas.title = '';
		canvas.style.cursor = '';
		canvas.onclick = null;
	}

	canvas.ondblclick = function() {
		getSelection().selectAllChildren(hl);
	}

	document.getElementById('inverted').onclick = function() {
		inverted = !inverted;
		render();
	}

	document.getElementById('search').onclick = function() {
		search(true);
	}

	document.getElementById('reset').onclick = function() {
		search(false);
	}

	const btnInfo = document.getElementById('info');
	const legend = document.getElementById('legend');

	btnInfo.onmouseover = function() {
		legend.style.left = (btnInfo.offsetLeft + 24) + 'px';
		legend.style.top = (btnInfo.offsetTop + 24) + 'px';
		legend.style.display = 'block';
	}

	btnInfo.onmouseout = function() {
		legend.style.display = 'none';
	}

	window.onkeydown = function(event) {
		if ((event.ctrlKey || event.metaKey) && event.key === 'f') {
			event.preventDefault();
			search(true);
			return false;
		} else if (event.key === 'Escape') {
			search(false);
		} else if ((event.key === 'n' || event.key === 'N') && nav.length > 0) {
			navIndex = (navIndex + (event.shiftKey ? nav.length - 1 : 1)) % nav.length;
			render(nav[navIndex]);
			document.getElementById('matchval').textContent = matchval + ' (' + (navIndex + 1) + ' of ' + nav.length + ')';
			window.scroll(0, inverted ? root.level * 16 : canvasHeight - (root.level + 1) * 16);
			canvas.onmousemove();
			return false;
		} else if (event.key === 'i') {
			canvas.onmouseout();
			document.getElementById('inverted').onclick();
			return false;
		} else if (event.key === '0') {
			canvas.onmouseout();
			root = levels[0][0];
			search(false);
			return false;
		}
	}

const cpool = [
'all',
' C2Compiler::compile_method',
'!ompilation::Compilation',
'-compile_java_method',
'5method',
'-emit_code_body',
'&e::Code_Gen',
'+mpile',
')Optimize',
'\'Broker::compiler_thread_loop',
'/invoke_compiler_on_method',
'\'r::compile_method',
'"ntiguousSpace::allocate',
' DefNewGeneration::FastEvacuateFollowersClosure::do_void',
'2collect',
'4py_to_survivor_space',
' GenCollectedHeap::collect_generation',
'2do_collection',
'2satisfy_failed_allocation',
'#eration::promote',
' InstanceKlass::allocate_objArray',
'"terpreterRuntime::anewarray',
' JVM_ArrayCopy',
'!avaThread::run',
'$_sun_nio_ch_FileDispatcherImpl_read0',
' Matcher::match',
'!emAllocator::allocate',
' ObjArrayAllocator::initialize',
'!ffsetTableContigSpace::allocate',
' Parse::Parse',
'\'do_all_blocks',
'*call',
'*one_block',
'/ytecode',
'%Generator::generate',
'!haseCFG::do_global_code_motion',
'*global_code_motion',
'*schedule_late',
'4ocal',
'&haitin::Register_Allocate',
'.Split',
'.build_ifg_physical',
'.elide_copy',
'.interfere_with_live',
'.merge_multidefs',
'.post_allocate_copy_removal',
'%IdealLoop::Dominators',
'0build_and_optimize',
'6loop_early',
';late',
';tree',
'0optimize',
'0remix_address_expressions',
'0split_if_with_blocks',
'D_post',
'Fre',
'&terGVN::optimize',
'.subsume_node',
'.transform_old',
'%Live::add_liveout',
'+compute',
'%MacroExpand::expand_macro_nodes',
'!redictedCallGenerator::generate',
' TenuredGeneration::allocate',
'!hread::call_run',
' VMThread::evaluate_operation',
'*inner_execute',
'*run',
'"_GenCollectForAllocation::doit',
'#Operation::evaluate',
' __GI_read',
'"handle_mm_fault',
'"memcpy_sse2_unaligned_erms',
'%set_avx2_unaligned_erms',
' aci_CopyRight',
'!sm_exc_page_fault',
' clear_huge_page',
'&page_erms',
'&subpage',
'"one3',
'!opy_page_to_iter',
'%user_enhanced_fast_string',
' demo8/FileConverter$$Lambda$3.0x00007ffab9001000.apply',
'<4.0x00007ffab9001240.applyAsInt',
'4Entry.<init>',
':equals',
':hashCode',
'3.convertFile',
';List',
'4main',
'4readInput',
'4saveResult',
'!o_huge_pmd_anonymous_page',
'#syscall_64',
'#user_addr_fault',
' entry_SYSCALL_64_after_hwframe',
'!xc_page_fault',
' filemap_read',
' handle_mm_fault',
' java/io/BufferedReader.fill',
'7readLine',
')yteArrayOutputStream.ensureCapacity',
'>toByteArray',
'>write',
'(DataOutputStream.write',
'>Int',
'>UTF',
'(InputStreamReader.read',
'%lang/Integer.parseInt',
'*String.<init>',
'1decodeASCII',
'1hashCode',
'1length',
'1substring',
'0Latin1.hashCode',
'7newString',
'0UTF16.compress',
'+ystem$2.decodeASCII',
'0.arraycopy',
'*ThreadLocal.get',
'%nio/charset/CharsetDecoder.decode',
')file/Files.readAllLines',
'%util/ArrayList$ArrayListSpliterator.tryAdvance',
'3.add',
'4grow',
'4sort',
'/s.copyOf',
'7Range',
'1sort',
'*Comparator$$Lambda$5.0x00007ffab90494b0.compare',
'4.lambda$comparingInt$7b0bb60$1',
'*HashMap$Node.<init>',
'1.hash',
'2newNode',
'2put',
'5Val',
'2resize',
'.Set.add',
'*TimSort.binarySort',
'2mergeAt',
'7Collapse',
'7ForceCollapse',
'7Hi',
'7Lo',
'2sort',
'*stream/AbstractPipeline.copyInto',
'JWithCancel',
'Bevaluate',
'BwrapAndCopyInto',
'1Collectors$$Lambda$7.0x00007ffab904a268.accept',
'1DistinctOps$1$2.accept',
'Aend',
'1ReduceOps$3ReducingSink.accept',
';ReduceOp.evaluateSequential',
'3ferencePipeline$3$1.accept',
'B.collect',
'CforEachWithCancel',
'1Sink$ChainedReference.end',
'2liceOps$1$1.accept',
'2ortedOps$RefSortingSink.accept',
'Jend',
'!long_disjoint_arraycopy',
' ksys_read',
' new_sync_read',
' oop_arraycopy',
' start_thread',
'!un/nio/ch/ChannelInputStream.read',
'+FileChannelImpl.read',
'/DispatcherImpl.read',
'B0',
'+IOUtil.read',
'6IntoNativeBuffer',
'+Util.getTemporaryDirectBuffer',
')s/StreamDecoder.implRead',
'9read',
'=Bytes',
'+UTF_8$Decoder.decodeArrayLoop',
'?Loop',
' thread_native_entry',
' vfs_read',
'!oid ContiguousSpace::oop_since_save_marks_iterate<DefNewScanClosure>',
'%OopOopIterateDispatch<DefNewScanClosure>::Table::oop_oop_iterate<InstanceKlass, narrowOop>',
'fObjArrayKlass, narrowOop>',
'AYoungerGenClosure>::Table::oop_oop_iterate<InstanceKlass, narrowOop>'
];
unpack(cpool);

n(3,584)
f(635,1,1,178)
u(1323)
u(1428)
u(516)
u(188,70)
u(76)
f(84,7,2,68)
f(12,8,2,63)
u(60)
u(52,36)
f(204,11,3,2)
n(284,7)
u(292)
f(300,13,1,2)
n(308,4)
f(316,11,4,24)
f(324,12,6,2)
n(332,9)
f(348,13,5,4)
f(356,12,4,2)
n(364)
u(340)
f(484,12,2,3)
u(476)
f(68,10,3,23)
f(412,11,2,16)
f(380,12,1,15)
f(372,13,1,3)
n(388,2)
n(396)
n(404)
n(428,5)
f(436,14,1,2)
n(444)
u(420)
f(452,11,2,3)
u(468)
f(460,13,1,2)
f(492,11,2)
u(452)
u(468)
f(276,10,2,4)
u(236)
u(244)
u(260)
u(268)
u(252)
f(500,16,1,3)
f(500,17,1,2)
u(276)
u(236)
u(244)
u(260)
u(268)
u(252)
f(92,8,2,3)
u(20)
u(36)
u(28)
f(44,12,1,2)
f(540,5,2,108)
u(532)
u(524)
u(556)
u(548)
u(148)
u(140)
u(132)
u(116)
u(108)
f(1444,15,12,50)
f(1452,16,1,22)
f(124,17,2,20)
f(156,18,10,8)
f(228,19,2,2)
n(508)
n(605)
u(773)
u(757)
u(789)
u(573)
u(741)
u(613)
u(629)
u(621)
f(579,18,2)
f(1460,16,2,27)
f(124,17,11,16)
f(156,18,13,3)
u(605)
u(773)
u(757)
u(789)
u(573)
u(741)
u(613)
u(629)
u(621)
f(1468,15,3,46)
f(124,16,19,27)
f(100,17,10,4)
n(156,13)
f(228,18,1,2)
n(605,10)
u(773)
u(757)
u(789)
u(573)
u(741)
u(613)
u(629)
f(621,26,1,9)
f(713,1,9,405)
u(697)
u(705,229)
f(1241,4,1,228)
u(1177)
u(1225)
u(1185)
u(1161)
u(1169)
u(1249,107)
f(977,11,2,105)
f(1233,12,2,103,2,0,0)
u(657,13)
f(674,14,4,9,8,0,0)
f(866,15,1,3)
u(866)
f(906,15,3,5,4,0,0)
u(906,3,2,0,0)
u(922)
f(1018,18,1,2)
f(922,16,2)
f(1201,13,2,90,2,0,0)
u(1098,87,57,0,0)
u(1074,87,59,0,0)
u(1057,4)
u(689)
f(890,18,1,3)
f(914,19,1,2)
f(1082,16,2,83,59,1,0)
f(682,17,41,2)
n(1066,17)
u(1050)
f(1089,17,17,23,0,0,2)
f(1265,14,23,3)
u(1273)
u(985)
u(985)
u(993)
u(993)
u(1009)
u(1008)
u(172)
u(164)
u(212)
u(220)
u(587)
u(605)
u(773)
u(757)
u(789)
u(573)
u(741)
u(613)
u(629)
u(621)
f(1257,10,3,121)
u(1209)
u(1257)
u(1281)
f(1001,14,1,117)
u(1025)
u(1153)
u(1105,21,0,1,0)
f(1034,18,13,4)
u(1042)
f(666,20,1,3)
f(1315,18,3,4)
f(1121,17,4,73)
u(1113)
u(1137,16)
f(1034,20,14,2,1,0,0)
u(1042)
f(1145,19,2,57,0,2,1)
f(1033,20,54,3)
u(1042)
u(666)
f(1129,17,3,23)
u(1113)
u(1137)
f(1033,20,18,5,1,0,0)
u(1042)
u(666)
f(1218,14,5,3,1,0,0)
u(1194,3,1,0,0)
u(986,3,1,0,0)
f(985,17,1,2)
u(993)
u(993)
u(1009)
u(1008)
u(172)
u(164)
u(212)
u(220)
f(721,3,2,107)
u(969)
u(969)
f(801,6,4,97)
u(801,97,0,0,1)
f(793,8,77,14)
u(857,14,1,0,0)
u(1393,14,1,0,0)
f(1385,11,1,13)
u(961,3)
u(1417)
u(1409)
u(938)
u(882)
f(1401,12,3,10,2,0,0)
u(1329,10,3,0,0)
u(1329,10,3,0,0)
u(1329,10,3,0,0)
u(1337,10,3,1,0)
f(1361,17,2,8,2,0,0)
u(1361,8,2,0,0)
u(1369,6)
u(1345)
u(1353)
u(195)
u(563)
u(765)
u(749)
f(1301,26,1,5)
u(1437)
f(1309,28,1,4)
u(781)
f(645,30,1,3)
u(653)
f(1378,19,3,2)
u(954)
u(1291)
f(874,8,2,6,5,0,0)
u(874,6,5,0,0)
u(930,6,5,0,0)
f(985,6,6)
u(985)
u(993)
u(993)
u(1009)
u(1008,6,0,1,4)
f(172,12,2,4)
u(164)
u(212)
u(220)
u(587)
f(605,17,1,3)
u(773)
u(757)
u(789)
u(573)
u(741)
u(613)
u(629)
u(621)
f(729,3,3,69,0,2,1)
f(817,4,21,2)
u(1009)
u(945)
u(179)
u(595)
f(842,4,2,8,5,0,0)
f(826,5,1,7,5,0,0)
f(809,6,5,2)
u(1008,2,0,0,1)
f(849,4,2,38)
u(849,38,0,0,2)
f(834,6,12,23,21,0,0)
f(826,7,6,17,15,1,0)
f(898,6,17,3)

search();
</script></body></html>

```

## File: .github\workflows\build.yml
```
name: build-template

on:
  workflow_call:
    inputs:
      platform:
        type: string
        required: true
      runner:
        type: string
        required: true
      container-image:
        type: string
        required: false

env:
  build_java_distribution: corretto
  build_java_version: 11

permissions:
  contents: read

jobs:
  build:
    runs-on: ${{ inputs.runner }}
    container:
      image: ${{ inputs.container-image && format('public.ecr.aws/async-profiler/asprof-builder-{0}', inputs.container-image) || '' }}
    name: "build and unit test (${{ inputs.platform }})"
    steps:
      - name: Run container setup
        if: inputs.container-image != ''
        run: "[ ! -f /root/setup.sh ] || /root/setup.sh"
      - name: Setup Java
        uses: actions/setup-java@v4
        with:
          distribution: ${{ env.build_java_distribution }}
          java-version: ${{ env.build_java_version }}
      - name: Checkout sources
        uses: actions/checkout@v4
      - name: Build and unit test
        id: build
        run: |
          set -x
          HASH=${GITHUB_SHA:0:7}
          case "${{ inputs.platform }}" in
            macos*)
              brew install gcovr
              make COMMIT_TAG=$HASH FAT_BINARY=true release coverage -j
            ;;
            *)
              make COMMIT_TAG=$HASH CC=/usr/local/musl/bin/musl-gcc release coverage -j
              echo "debug_archive=$(find . -type f -name "async-profiler-*-debug*" -exec basename {} \;)" >> $GITHUB_OUTPUT
            ;;
          esac
          echo "archive=$(find . -type f -name "async-profiler-*" -not -name "*-debug*" -exec basename {} \;)" >> $GITHUB_OUTPUT
        shell: bash
        env:
          GITHUB_SHA: ${{ github.sha }}
      - name: Set artifact name
        id: set_artifact_name
        run: echo "artifact_name=async-profiler-${{ inputs.platform }}-${GITHUB_SHA:0:7}" >> $GITHUB_OUTPUT
        shell: bash
        env:
          GITHUB_SHA: ${{ github.sha }}
      - name: Upload binaries
        uses: actions/upload-artifact@v4
        with:
          name: ${{ steps.set_artifact_name.outputs.artifact_name }}
          path: ${{ steps.build.outputs.archive }}
          if-no-files-found: error
      - name: Upload debug info
        uses: actions/upload-artifact@v4
        if: inputs.platform != 'macos'
        with:
          name: ${{ steps.set_artifact_name.outputs.artifact_name }}-debug
          path: ${{ steps.build.outputs.debug_archive }}
          if-no-files-found: error
      - name: Upload coverage report
        uses: actions/upload-artifact@v4
        with:
          name: test-coverage-${{ inputs.platform }}
          path: build/test/coverage/
          if-no-files-found: error

```

## File: .github\workflows\clang-tidy-review.yml
```
name: clang-tidy-review

on:
  workflow_run:
    workflows:
    - code-check
    types:
    - completed

jobs:
  clang-tidy-results:
    if: github.event.workflow_run.event == 'pull_request' && github.event.workflow_run.conclusion == 'success'
    runs-on: ubuntu-latest
    container:
      image: "public.ecr.aws/async-profiler/asprof-code-check:latest"
    permissions:
      pull-requests: write
      contents: write
      actions: read
    steps:
    - name: Download code-check artifacts
      uses: actions/download-artifact@v4
      with:
        run-id: ${{ github.event.workflow_run.id }}
        github-token: ${{ secrets.GITHUB_TOKEN }}
        name: code-check-artifacts
        path: /tmp/code-check-artifacts/
    - name: Read PR information
      id: pr_info
      run: |
        cd /tmp/code-check-artifacts
        echo "pr_id=$(cat pr-id.txt)" >> "$GITHUB_OUTPUT"
        echo "pr_head_repo=$(cat pr-head-repo.txt)" >> "$GITHUB_OUTPUT"
        echo "pr_head_sha=$(cat pr-head-sha.txt)" >> "$GITHUB_OUTPUT"
    - uses: actions/checkout@v4
      with:
        repository: ${{ steps.pr_info.outputs.pr_head_repo }}
        ref: ${{ steps.pr_info.outputs.pr_head_sha }}
        persist-credentials: false
    - name: Run clang-tidy-pr-comments action
      uses: platisd/clang-tidy-pr-comments@v1
      with:
        github_token: ${{ secrets.GITHUB_TOKEN }}
        clang_tidy_fixes: /tmp/code-check-artifacts/clang-tidy-fixes.yml
        pull_request_id: ${{ steps.pr_info.outputs.pr_id }}
        python_path: python
        auto_resolve_conversations: true
        suggestions_per_comment: 100

```

## File: .github\workflows\code-check.yml
```
name: code-check

on:
  - pull_request

concurrency:
  group: ${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: true

permissions:
  contents: read

jobs:
  cpp-lint:
    runs-on: ubuntu-latest
    container:
      image: "public.ecr.aws/async-profiler/asprof-code-check:latest"
    steps:
      - uses: actions/checkout@v4
        with:
          ref: ${{ github.event.pull_request.head.sha }}
          fetch-depth: 0
      - name: Mark repo as safe for Git
        run: git config --global --add safe.directory $GITHUB_WORKSPACE
      - name: Fetch base branch
        run: |
          git remote add upstream "https://github.com/${{ github.event.pull_request.base.repo.full_name }}"
          git fetch --no-tags --no-recurse-submodules upstream "${{ github.event.pull_request.base.ref }}"
      - name: Create artifacts directory
        run: |
          mkdir code-check-artifacts/
          echo "${{ github.event.number }}" > code-check-artifacts/pull-request-id.txt
      - name: Run clang-tidy
        run: |
          set pipefail
          make cpp-lint-diff \
            DIFF_BASE="$(git merge-base HEAD "upstream/${{ github.event.pull_request.base.ref }}")" \
            CLANG_TIDY_ARGS_EXTRA="-export-fixes code-check-artifacts/clang-tidy-fixes.yml"
        shell: bash
      - name: Save PR information
        run: |
          echo "${{ github.event.number }}" > code-check-artifacts/pr-id.txt
          echo "${{ github.event.pull_request.head.repo.full_name }}" > code-check-artifacts/pr-head-repo.txt
          echo "${{ github.event.pull_request.head.sha }}" > code-check-artifacts/pr-head-sha.txt
      - name: Upload artifacts
        uses: actions/upload-artifact@v4
        with:
          name: code-check-artifacts
          path: code-check-artifacts/

```

## File: .github\workflows\integ.yml
```
name: integration-test-template

on:
  workflow_call:
    inputs:
      test-platform:
        type: string
        required: true
      platform:
        type: string
        required: true
      architecture:
        type: string
        required: false
      java-version:
        type: string
        required: true
      java-distribution:
        type: string
        required: false
        default: "corretto"
      runner:
        type: string
        required: true
      container-image:
        type: string
        required: false
      container-volumes:
        type: string
        required: false
      use-builtin-jdk:
        type: boolean
        required: false
        default: false
      retry-count:
        type: number
        required: false
        default: 0

permissions:
  contents: read

jobs:
  integration-test:
    runs-on: ${{ inputs.runner }}
    container:
      image: ${{ inputs.container-image && format('public.ecr.aws/async-profiler/asprof-builder-{0}', inputs.container-image) || '' }}
      options: --privileged
      volumes: ${{ fromJSON(inputs.container-volumes || '[]') }}
    name: "${{ inputs.test-platform }}, ${{ inputs.java-distribution }} ${{ inputs.java-version }}"
    steps:
      - name: Run container setup
        if: inputs.container-image != ''
        run: "[ ! -f /root/setup.sh ] || /root/setup.sh"
      - name: Setup Java
        uses: actions/setup-java@v4
        # https://github.com/actions/setup-java/issues/678#issuecomment-2446279753
        if: ${{ !inputs.use-builtin-jdk }}
        with:
          distribution: ${{ inputs.java-distribution }}
          java-version: ${{ inputs.java-version }}
          architecture: ${{ inputs.architecture }}
      - name: Checkout sources
        uses: actions/checkout@v4
      - name: Set variables
        id: set_variables
        run: |
          echo "short_sha=${GITHUB_SHA:0:7}" >> $GITHUB_OUTPUT
          echo "artifact_name=async-profiler-${{ inputs.platform }}-${GITHUB_SHA:0:7}" >> $GITHUB_OUTPUT
        shell: bash
        env:
          GITHUB_SHA: ${{ github.sha }}
      - name: Download async-profiler release artifact
        uses: actions/download-artifact@v4
        with:
          name: ${{ steps.set_variables.outputs.artifact_name }}
          path: async_profiler_release
      - name: Download async-profiler JAR artifacts
        uses: actions/download-artifact@v4
        with:
          name: async-profiler-jars
          path: jar_artifacts
      - name: Extract async-profiler artifact
        id: extract_artifact
        run: |
          release_archive=$(basename $(find async_profiler_release -type f -iname "async-profiler-*" ))
          case "${{ inputs.runner }}" in
            macos*)
              unzip async_profiler_release/$release_archive
            ;;
            *)
              tar xvf async_profiler_release/$release_archive
            ;;
          esac
          echo "jars_directory=jar_artifacts" >> $GITHUB_OUTPUT
          echo "release_directory=$(basename $(find . -type d -iname "async-profiler-*" ))" >> $GITHUB_OUTPUT
      - name: Download Protobuf Java runtime
        run: |
          mkdir -p test/deps
          cd test/deps
          curl -L -O "https://repo1.maven.org/maven2/com/google/protobuf/protobuf-java/$PB_JAVA_VERSION/protobuf-java-$PB_JAVA_VERSION.jar"
        env:
          PB_JAVA_VERSION: "4.31.1"
      - name: Run integration tests
        run: |
          mkdir -p build/jar
          cp ${{ steps.extract_artifact.outputs.jars_directory }}/* build/jar
          make build/test.jar
          cp -r ${{ steps.extract_artifact.outputs.release_directory }}/bin build
          cp -r ${{ steps.extract_artifact.outputs.release_directory }}/lib build
          make test-java RETRY_COUNT=${{ inputs.retry-count }} -j
      - name: Upload integration test logs
        uses: actions/upload-artifact@v4
        if: always()
        with:
          name: integration-test-logs-${{ inputs.test-platform }}-${{ inputs.java-version }}-${{ steps.set_variables.outputs.short_sha }}
          path: |
            build/test/logs/
            hs_err*.log

```

## File: .github\workflows\linters.yml
```
name: lint

on:
  - push
  - pull_request

concurrency:
  group: ${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: true

permissions:
  contents: read

jobs:
  license-header:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Check license headers
        uses: apache/skywalking-eyes/header@v0.6.0
  markdown:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Install prettier
        run: |
          npm install -g prettier@3.4.2
          make check-md
  eof-newline:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: EOF newline check
        env:
          offenders_path: /tmp/eof_newline_offenders.txt
        run: |
          find . -path './.git' -prune -o -exec file --mime-type {} + | grep 'text/' | awk -F: '{print $1}' | while read -r file; do
            # Read last byte and verify it's a newline
            if [ -s "$file" ] && [ "$(tail -c1 "$file" | wc -l)" -eq 0 ]; then
              echo "$file" >> "$offenders_path"
            fi
          done
          if [ -s "$offenders_path" ]; then
            cat "$offenders_path"
            exit 1
          fi
  trailing-spaces:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Trailing spaces check
        env:
          offenders_path: /tmp/trailing_space_offenders.txt
        run: |
          grep -rIlE --exclude-dir=.git '[[:blank:]]+$' . > "$offenders_path" || true
          if [ -s "$offenders_path" ]; then
            cat "$offenders_path"
            exit 1
          fi

```

## File: .github\workflows\pyroscope-release.yml
```
name: Release Workflow

on:
  push:
    tags:
      - "v*.*.*.*"

permissions:
  contents: read

jobs:
  build-linux:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        include:
          - platform: "linux/amd64"
            name: "amd64"
          - platform: "linux/arm64"
            name: "arm64"
    steps:
      - name: Checkout code
        uses: actions/checkout@11bd71901bbe5b1630ceea73d27597364c9af683 # v4.2.2
        with:
          persist-credentials: 'false'

      - name: Set up QEMU
        uses: docker/setup-qemu-action@29109295f81e9208d7d86ff1c6c12d2833863392 # v3.6.0

      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@b5ca514318bd6ebac0fb2aedd5d36ec1b5c232a2 # v3.10.0

      - run: echo ${GITHUB_REF} | grep $(make version)
        env:
          GITHUB_REF: ${{ github.ref }}

      - name: Build and Export Linux Binaries
        run: docker buildx build --platform=${{ matrix.platform }} --output=. .

      - name: Upload Release Artifacts
        uses: actions/upload-artifact@ea165f8d65b6e75b540449e92b4886f43607fa02 # v4.6.2
        with:
          name: ${{ matrix.name }}-linux-binaries
          path: '*.tar.gz'

  build-macos:
    runs-on: macos-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@11bd71901bbe5b1630ceea73d27597364c9af683 # v4.2.2
        with:
          persist-credentials: 'false'

      - name: Set up JDK
        uses: actions/setup-java@c5195efecf7bdfc987ee8bae7a71cb8b11521c00 # v4.7.1
        with:
          distribution: 'adopt'
          java-version: '11'

      - name: Make release
        run: FAT_BINARY=true make release

      - name: Upload Release Artifacts
        uses: actions/upload-artifact@ea165f8d65b6e75b540449e92b4886f43607fa02 # v4.6.2
        with:
          name: macos-binaries
          path: '*.zip'

  create-release:
    needs: [build-linux, build-macos]
    runs-on: ubuntu-latest
    permissions:
      contents: write
    steps:
      - name: Download Artifacts
        uses: actions/download-artifact@d3f86a106a0bac45b974a628896c90dbdf5c8093 # v4.3.0
      - name: Create Release
        uses: softprops/action-gh-release@da05d552573ad5aba039eaac05058a918a7bf631 # v2.2.2
        with:
          files: |
            amd64-linux-binaries/*.tar.gz
            arm64-linux-binaries/*.tar.gz
            macos-binaries/*.zip
          prerelease: false
          draft: true
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}

```

## File: .github\workflows\test-and-publish-nightly.yml
```
name: CI

on:  # We are very liberal in terms of triggering builds. This should be revisited if we start seeing a lot of queueing
  - push
  - pull_request

concurrency:
  group: ${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: true

permissions:
  contents: read

jobs:
  build-jars:
    runs-on: ubuntu-latest
    name: build / jars
    steps:
      - name: Checkout sources
        uses: actions/checkout@v4
      - name: Build JARs
        run: make jar
      - name: Upload JARs
        uses: actions/upload-artifact@v4
        with:
          name: async-profiler-jars
          path: build/jar/*
          if-no-files-found: error

  build-linux-arm64:
    name: build / linux-arm64
    uses: ./.github/workflows/build.yml
    with:
      platform: linux-arm64
      runner: ubuntu-24.04-arm
      container-image: "arm:latest"

  build-linux-x64:
    name: build / linux-x64
    uses: ./.github/workflows/build.yml
    with:
      platform: linux-x64
      runner: ubuntu-latest
      container-image: x86:latest

  build-macos:
    name: build / macos
    uses: ./.github/workflows/build.yml
    with:
      platform: macos
      runner: macos-15

  integ-linux-x64:
    name: integ / linux-x64
    needs: build-linux-x64
    strategy:
      fail-fast: false
      matrix:
        test-platform: [linux-x64]
        java-version: [8, 11, 17, 21, 25]
        java-distribution: [corretto]
        container-image: [x86:latest]
        include:
          - test-platform: linux-x64-alpine
            container-image: alpine:corretto-11
            use-builtin-jdk: true
            java-distribution: corretto
            java-version: 11
          - test-platform: linux-x64-AL2
            container-image: amazonlinux:2
            # GHA provides Node.js by attaching a volume to the container. The container path is
            # '/__e/node20', and it's not writable unless we override it via 'container.volumes'.
            container-volumes: '["/tmp/node20:/__e/node20"]'
            java-version: 11
            java-distribution: corretto
          - test-platform: linux-x64-AL2023
            container-image: amazonlinux:2023
            java-version: 11
            java-distribution: corretto
          - test-platform: linux-x64-alpaquita
            container-image: alpaquita:x86_64-liberica-21
            use-builtin-jdk: true
            java-distribution: liberica
            java-version: 21
    uses: ./.github/workflows/integ.yml
    with:
      platform: linux-x64
      test-platform: ${{ matrix.test-platform }}
      runner: ubuntu-latest
      container-image: ${{ matrix.container-image }}
      container-volumes: ${{ matrix.container-volumes || '' }}
      java-version: ${{ matrix.java-version }}
      java-distribution: ${{ matrix.java-distribution }}
      use-builtin-jdk: ${{ matrix.use-builtin-jdk || false }}

  integ-linux-arm64:
    name: integ / linux-arm64
    needs: build-linux-arm64
    strategy:
      fail-fast: false
      matrix:
        test-platform: [linux-arm64]
        java-version: [8, 11, 17, 21, 25]
        java-distribution: [corretto]
        container-image: [arm:latest]
    uses: ./.github/workflows/integ.yml
    with:
      platform: linux-arm64
      test-platform: ${{ matrix.test-platform }}
      runner: ubuntu-24.04-arm
      container-image: ${{ matrix.container-image }}
      container-volumes: ${{ matrix.container-volumes || '' }}
      java-version: ${{ matrix.java-version }}
      java-distribution: ${{ matrix.java-distribution }}

  integ-macos:
    name: integ / macos
    needs: build-macos
    strategy:
      fail-fast: false
      matrix:
        include:
          - runner: macos-15
            test-platform: macos-arm64
            java-version: "11"
          - runner: macos-15
            test-platform: macos-arm64
            java-version: "21"
          - runner: macos-15-intel
            test-platform: macos-x64
            java-version: "17"
            architecture: x64
            retry-count: 1
    uses: ./.github/workflows/integ.yml
    with:
      platform: macos
      test-platform: ${{ matrix.test-platform }}
      runner: ${{ matrix.runner }}
      java-version: ${{ matrix.java-version }}
      architecture: ${{ matrix.architecture || '' }}
      retry-count: ${{ matrix.retry-count || 0 }}

  publish-only-on-push:
    if: github.repository == 'async-profiler/async-profiler' && github.event_name == 'push' && github.ref == 'refs/heads/master'
    permissions:
      contents: write
    name: publish (nightly)
    runs-on: ubuntu-latest
    needs: [build-jars, integ-linux-x64, integ-linux-arm64, integ-macos]
    steps:
      - name: Download async-profiler binaries and jars
        uses: actions/download-artifact@v4
        with:
          pattern: 'async-profiler-*'
          merge-multiple: 'true'
      - name: Delete previous release and publish new release
        uses: actions/github-script@v7
        with:
          result-encoding: string
          script: |
            const fs = require('fs').promises;
            const commonOptions = {
              owner: "async-profiler",
              repo: "async-profiler",
            };
            let previousRelease = undefined;
            try {
              previousRelease = await github.rest.repos.getReleaseByTag({
                ...commonOptions,
                tag: "nightly",
              });
            } catch (e) {
              console.log("No previous nightly release");
              // ignore, there was no previous nightly release
            }
            if (previousRelease !== undefined) {
              // delete previous release and nightly tag
              await github.rest.repos.deleteRelease({
                ...commonOptions,
                release_id: previousRelease.data.id,
              });
              await github.rest.git.deleteRef({...commonOptions, ref: "tags/nightly"});
            }
            // create draft release
            const newReleaseId = (await github.rest.repos.createRelease({
              ...commonOptions,
              tag_name: "nightly",
              target_commitish: "${{ github.sha }}",
              name: "Nightly builds",
              body: "Async-profiler binaries published automatically from the latest sources in `master` upon a successful build.",
              prerelease: true,
              draft: true,
            })).data.id;
            // upload binaries and jars to draft release
            for (const archiveName of await fs.readdir(process.cwd())) {
              await github.rest.repos.uploadReleaseAsset({
                ...commonOptions,
                release_id: newReleaseId,
                name: archiveName,
                data: await fs.readFile(archiveName),
              });
            }
            // publish release
            await github.rest.repos.updateRelease({
              ...commonOptions,
              release_id: newReleaseId,
              draft: false,
            });

```

## File: docs\advancedstacktracefeatures.md
```
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

## File: docs\converterusage.md
```
# Converter Usage

async-profiler provides `jfrconv` utility to convert between different profile output formats.
`jfrconv` can be found at the same location as the `asprof` binary. Converter is also available
as a standalone Java application: [`jfr-converter.jar`](https://github.com/async-profiler/async-profiler/releases/download/v4.2.1/jfr-converter.jar).

## Supported conversions

| Source    | html | collapsed | pprof | pb.gz | heatmap | otlp |
| --------- | ---- | --------- | ----- | ----- | ------- | ---- |
| jfr       | ✅   | ✅        | ✅    | ✅    | ✅      | ✅   |
| html      | ✅   | ✅        | ❌    | ❌    | ❌      | ❌   |
| collapsed | ✅   | ✅        | ❌    | ❌    | ❌      | ❌   |

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

#### Flame Graph options

To add a custom title to the generated Flame Graph, use `--title`, which has the default value `Flame Graph`:

```
jfrconv --cpu foo.jfr foo.html -r --title "Custom Title"
```

### Other formats

`jfrconv` supports converting a JFR file to `collapsed`, `pprof`, `pb.gz` and `heatmap` formats as well.

## Standalone converter examples

Standalone converter jar is provided in
[Download](https://github.com/async-profiler/async-profiler/?tab=readme-ov-file#Download).
It accepts the same parameters as `jfrconv`.

Below is an example usage:

```
java -jar jfr-converter.jar --cpu foo.jfr --reverse --title "Application CPU profile"
```

```

## File: docs\cpusamplingengines.md
```
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

## File: docs\flamegraphinterpretation.md
```
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

## File: docs\gettingstarted.md
```
# Getting started guide

## Before profiling

As of Linux 4.6, capturing kernel call stacks using `perf_events` from a non-root
process requires setting two kernel parameters. You can set them using sysctl as follows:

```
# sysctl kernel.perf_event_paranoid=1
# sysctl kernel.kptr_restrict=0
```

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

## File: docs\heatmap.md
```
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

## File: docs\integratingasyncprofiler.md
```
# Integrating async-profiler

## Launching as an agent

If you need to profile some code as soon as the JVM starts up, instead of using `asprof`,
it is possible to attach async-profiler as an agent on the command line. For example:

```
$ java -agentpath:/path/to/libasyncProfiler.so=start,event=cpu,file=profile.html ...
```

Agent library is configured through the JVMTI argument interface.
The format of the arguments string is described
[in the source code](https://github.com/async-profiler/async-profiler/blob/v4.2.1/src/arguments.cpp#L39).
`asprof` actually converts command line arguments to that format.

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

## File: docs\jfrvisualization.md
```
# JFR Visualization

JFR recordings produced by async-profiler can be viewed using multiple options explained below.

## Built-in converter

async-profiler provides a built-in converter `jfrconv` which can be used to convert `jfr` output
to a flame graph or one of the other supported formats. More details on the built-in converter usage
can be found [here](ConverterUsage.md).

## JMC

[JDK Mission Control](https://www.oracle.com/java/technologies/jdk-mission-control.html) (JMC)
is a popular GUI tool to analyze JFR recordings.
It has been originally developed to work in conjunction with the JDK Flight Recorder,
however, async-profiler recordings are also fully compatible with JMC.

When viewing async-profiler recordings in JMC, information on some tabs may be missing.
Developers are typically interested in the following sections:

- Java Application
  - Method Profiling
  - Memory
  - Lock Instances
- JVM Internals
  - TLAB Allocations

## IntelliJ IDEA

IntelliJ IDEA Ultimate has built-in JFR viewer that works perfectly with async-profiler recordings.
For the Community Edition, there is an open-source profiler [plugin](https://plugins.jetbrains.com/plugin/20937-java-jfr-profiler)
that allows you to profile Java applications with JFR and async-profiler as well as
open JFR files obtained outside IDE.

## JFR command line tool

JDK distributions include the `jfr` command line utility to filter, summarize and output
flight recording files into human-readable format. The
[official documentation](https://docs.oracle.com/en/java/javase/21/docs/specs/man/jfr.html)
provides complete information on how to manipulate the contents and translate it as per
developers' needs to debug performance issues with their Java applications.

```

## File: docs\outputformats.md
```
# Output Formats

async-profiler currently supports the following output formats:

- `collapsed` - This is a collection of call stacks, where each line is a semicolon separated list of frames followed
  by a counter. This is used by the FlameGraph script to generate the FlameGraph visualization of the profile data.

  ```
  FileConverter.main;FileConverter.convertFile;FileConverter.saveResult 21
  FileConverter.main;FileConverter.convertFile;FileConverter.saveResult;java/io/DataOutputStream.writeInt 1
  FileConverter.main;FileConverter.convertFile;FileConverter.saveResult;java/io/DataOutputStream.writeInt;java/io/ByteArrayOutputStream.write 5
  FileConverter.main;FileConverter.convertFile;FileConverter.saveResult;java/io/DataOutputStream.writeUTF;java/io/DataOutputStream.writeUTF 12
  FileConverter.main;FileConverter.convertFile;FileConverter.saveResult;java/io/DataOutputStream.writeUTF;java/io/DataOutputStream.writeUTF;java/lang/String.length 3
  FileConverter.main;FileConverter.convertFile;FileConverter.saveResult;java/io/DataOutputStream.writeUTF;java/io/DataOutputStream.writeUTF;java/io/DataOutputStream.write 6
  start_thread;thread_native_entry;Thread::call_run;VMThread::run;VMThread::inner_execute;VMThread::evaluate_operation;VM_Operation::evaluate;VM_GenCollectForAllocation::doit;GenCollectedHeap::satisfy_failed_allocation;GenCollectedHeap::do_collection;GenCollectedHeap::collect_generation;DefNewGeneration::collect;DefNewGeneration::FastEvacuateFollowersClosure::do_void 12
  start_thread;thread_native_entry;Thread::call_run;VMThread::run;VMThread::inner_execute;VMThread::evaluate_operation;VM_Operation::evaluate;VM_GenCollectForAllocation::doit;GenCollectedHeap::satisfy_failed_allocation;GenCollectedHeap::do_collection;GenCollectedHeap::collect_generation;DefNewGeneration::collect;DefNewGeneration::FastEvacuateFollowersClosure::do_void;void ContiguousSpace::oop_since_save_marks_iterate<DefNewScanClosure> 1
  ```

- `flamegraph` - FlameGraph is a hierarchical representation of call traces of the profiled software in a color coded
  format. Read more on the [interpretation](FlamegraphInterpretation.md) of FlameGraphs.
  [![FlameGraph](/.assets/images/flamegraph.png)](https://htmlpreview.github.io/?https://github.com/async-profiler/async-profiler/blob/master/.assets/html/flamegraph.html)

- `tree` - Profile output generated in HTML format showing a tree view of resource usage beginning with the call stack
  with the highest resource usage and then showing other call stacks in descending order of resource usage. Expanding a
  parent frame follows the same hierarchical representation within that frame.
  ![Tree](/.assets/images/treeview_example.png)

- `text` - If no output format is specified with `-o` and filename has no extension provided, profiled output is
  generated in text format.

  ```
  --- Execution profile ---
  Total samples       : 733

  --- 8208 bytes (19.58%), 1 sample
  [ 0] byte[]
  [ 1] java.util.jar.Manifest$FastInputStream.<init>
  [ 2] java.util.jar.Manifest$FastInputStream.<init>
  [ 3] java.util.jar.Manifest.read
  [ 4] java.util.jar.Manifest.<init>
  [ 5] java.util.jar.Manifest.<init>
  [ 6] java.util.jar.JarFile.getManifestFromReference
  [ 7] java.util.jar.JarFile.getManifest
  [ 8] jdk.internal.loader.URLClassPath$JarLoader$2.getManifest
  [ 9] jdk.internal.loader.BuiltinClassLoader.defineClass
  [10] jdk.internal.loader.BuiltinClassLoader.findClassOnClassPathOrNull
  [11] jdk.internal.loader.BuiltinClassLoader.loadClassOrNull
  [12] jdk.internal.loader.BuiltinClassLoader.loadClass
  [13] jdk.internal.loader.ClassLoaders$AppClassLoader.loadClass
  [14] java.lang.ClassLoader.loadClass
  [15] java.lang.Class.forName0
  [16] java.lang.Class.forName
  [17] sun.launcher.LauncherHelper.loadMainClass
  [18] sun.launcher.LauncherHelper.checkAndLoadMain
  ```

- `jfr` - profile format used by the JDK Flight Recorder. The `jfr` format collects data
  about the JVM as well as the Java application running on it. async-profiler can generate output in `jfr` format
  compatible with tools capable of viewing and analyzing `jfr` files. JDK Mission Control (JMC) and Intellij IDEA are
  some of many options to visualize `jfr` files. More details [here](JfrVisualization.md).

- `otlp` - OpenTelemetry protocol format for [profiling data](https://opentelemetry.io/blog/2024/profiling).
  Experimental feature: backward-incompatible changes may happen in future releases of async-profiler.

```

## File: docs\profileroptions.md
```
# Profiler options

The below tables list the profiler options available with `asprof` and also when
[launching as an agent](IntegratingAsyncProfiler.md#launching-as-an-agent).
Some tables are output specific, which means some options are applicable to only one or more output formats but not all.

```
Usage: asprof [action] [options] [PID]
```

## Actions

The below options are `action`s for async-profiler and common for both `asprof` binary and when launching as an agent.

| Option    | Description                                                                                                                                                                                     |
| --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `start`   | Start profiling in semi-automatic mode, i.e. profiler will run until `stop` command is explicitly called.                                                                                       |
| `resume`  | Start or resume earlier profiling session that has been stopped. All the collected data remains valid. The profiling options are not preserved between sessions, and should be specified again. |
| `stop`    | Stop profiling and print the report.                                                                                                                                                            |
| `dump`    | Dump collected data without stopping profiling session.                                                                                                                                         |
| `status`  | Print profiling status: whether profiler is active and for how long.                                                                                                                            |
| `metrics` | Print profiler metrics in Prometheus format.                                                                                                                                                    |
| `list`    | Show the list of profiling events available for the target process specified with PID.                                                                                                          |

## Options applicable to any output format

| asprof               | Launch as agent    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| -------------------- | ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `-o fmt`             | `fmt`              | Specifies what information to dump when profiling ends. For various dump option details, please refer to [Dump Option Appendix](#dump-option).                                                                                                                                                                                                                                                                                                                                                                                              |
| `-d N`               | N/A                | asprof-only option designed for interactive use. It is a shortcut for running 3 actions: start, sleep for N seconds, stop. If no `start`, `resume`, `stop` or `status` option is given, the profiler will run for the specified period of time and then automatically stop.<br>Example: `asprof -d 30 <pid>`                                                                                                                                                                                                                                |
| `--timeout N`        | `timeout=N`        | The profiling duration, in seconds. The profiler will run for the specified period of time and then automatically stop.<br>Example: `java -agentpath:/path/to/libasyncProfiler.so=start,event=cpu,timeout=30,file=profile.html <application>`                                                                                                                                                                                                                                                                                               |
| `-e --event EVENT`   | `event=EVENT`      | The profiling event: `cpu`, `alloc`, `nativemem`, `lock`, `cache-misses` etc. Use `list` to see the complete list of available events.<br>Please refer to [Profiling Modes](ProfilingModes.md) for additional information.                                                                                                                                                                                                                                                                                                                  |
| `-i --interval N`    | `interval=N`       | Interval has different meaning depending on the event. For CPU profiling, it's CPU time in nanoseconds. In wall clock mode, it's wall clock time. For Java method profiling or native function profiling, it's number of calls. For PMU profiling, it's number of events. Time intervals may be followed by `s` for seconds, `ms` for milliseconds, `us` for microseconds or `ns` for nanoseconds.<br>Example: `asprof -e cpu -i 5ms 8983`                                                                                                  |
| `--alloc N`          | `alloc=N`          | Allocation profiling interval in bytes or in other units, if N is followed by `k` (kilobytes), `m` (megabytes), or `g` (gigabytes).                                                                                                                                                                                                                                                                                                                                                                                                         |
| `--live`             | `live`             | Retain allocation samples with live objects only (object that have not been collected by the end of profiling session). Useful for finding Java heap memory leaks.                                                                                                                                                                                                                                                                                                                                                                          |
| `--nativemem N`      | `nativemem=N`      | Native memory allocation profiling. N, if specified is the interval in bytes or in other units, if N is followed by `k` (kilobytes), `m` (megabytes), or `g` (gigabytes). Default N is 0.                                                                                                                                                                                                                                                                                                                                                   |
| `--nofree`           | `nofree`           | Will not record free calls in native memory allocation profiling. This is relevant when tracking memory leaks is not important and there are lots of free calls.                                                                                                                                                                                                                                                                                                                                                                            |
| `--trace METHOD[:T]` | `trace=METHOD[:T]` | Java method to be traced, optionally followed by a latency threshold.<br>Example: `--trace my.pkg.Class.Method:50ms`.<br>Latency threshold defaults to 0 (all calls are profiled). Can be used multiple times.                                                                                                                                                                                                                                                                                                                              |
| `--lock TIME`        | `lock=TIME`        | In lock profiling mode, sample contended locks whenever total lock wait time overflows the specified threshold.                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `--nativelock TIME`  | `nativelock=TIME ` | In native lock profiling mode, sample contended pthread locks (mutex/rwlock) whenever total lock wait time overflows the specified threshold.                                                                                                                                                                                                                                                                                                                                                                                               |
| `--wall INTERVAL`    | `wall=INTERVAL`    | Wall clock profiling interval. Use this option instead of `-e wall` to enable wall clock profiling with another event, typically `cpu`.<br>Example: `asprof -e cpu --wall 100ms -f combined.jfr 8983`.                                                                                                                                                                                                                                                                                                                                      |
| `--proc INTERVAL`    | `proc=INTERVAL`    | Collect statistics about other processes in the system. Default sampling interval is 30s.                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `-j N`               | `jstackdepth=N`    | Sets the maximum stack depth. The default is 2048.<br>Example: `asprof -j 30 8983`                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `-I PATTERN`         | `include=PATTERN`  | Filter stack traces by the given pattern(s). `-I` defines the name pattern that _must_ be present in the stack traces. `-I` can be specified multiple times. A pattern may begin or end with a star `*` that denotes any (possibly empty) sequence of characters.<br>Example: `asprof -I 'Primes.*' -I 'java/*' 8983`                                                                                                                                                                                                                       |
| `-X PATTERN`         | `exclude=PATTERN`  | Filter stack traces by the given pattern(s). `-X` defines the name pattern that _must not_ occur in any of stack traces in the output. `-X` can be specified multiple times. A pattern may begin or end with a star `*` that denotes any (possibly empty) sequence of characters.<br>Example: `asprof -X '*Unsafe.park*' 8983`                                                                                                                                                                                                              |
| `-L level`           | `loglevel=level`   | Log level: `debug`, `info`, `warn`, `error` or `none`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `-F features`        | `features=LIST`    | Comma separated (or `+` separated when launching as an agent) list of stack walking features. Supported features are:<ul><li>`stats` - log stack walking performance stats.</li><li>`vtable` - display targets of megamorphic virtual calls as an extra frame on top of `vtable stub` or `itable stub`.</li><li>`comptask` - display current compilation task (a Java method being compiled) in a JIT compiler stack trace.</li><li>`pcaddr` - display instruction addresses .</li></ul>More details [here](AdvancedStacktraceFeatures.md). |
| `-f FILENAME`        | `file`             | The file name to dump the profile information to.<br>`%p` in the file name is expanded to the PID of the target JVM;<br>`%t` - to the timestamp;<br>`%n{MAX}` - to the sequence number;<br>`%{ENV}` - to the value of the given environment variable.<br>Example: `asprof -o collapsed -f /tmp/traces-%t.txt 8983`                                                                                                                                                                                                                          |
| `--loop TIME`        | `loop=TIME`        | Run profiler in a loop (continuous profiling). The argument is either a clock time (`hh:mm:ss`) or a loop duration in `s`econds, `m`inutes, `h`ours, or `d`ays. Make sure the filename includes a timestamp pattern, or the output will be overwritten on each iteration.<br>Example: `asprof --loop 1h -f /var/log/profile-%t.jfr 8983`                                                                                                                                                                                                    |
| `--all-user`         | `alluser`          | Include only user-mode events. This option is helpful when kernel profiling is restricted by `perf_event_paranoid` settings.                                                                                                                                                                                                                                                                                                                                                                                                                |
| `--sched`            | `sched`            | Group threads by Linux-specific scheduling policy: BATCH/IDLE/OTHER.                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `--cstack MODE`      | `cstack=MODE`      | How to walk native frames (C stack). Possible modes are `fp` (Frame Pointer), `dwarf` (DWARF unwind info), `lbr` (Last Branch Record, available on Haswell since Linux 4.1), `vm`, `vmx` (HotSpot VM Structs) and `no` (do not collect C stack).<br><br>By default, C stack is shown in cpu, ctimer, wall-clock and perf-events profiles. Java-level events like `alloc` and `lock` collect only Java stack.                                                                                                                                |
| `--signal NUM`       | `signal=NUM`       | Use alternative signal for cpu or wall clock profiling. To change both signals, specify two numbers separated by a slash: `--signal SIGCPU/SIGWALL`.                                                                                                                                                                                                                                                                                                                                                                                        |
| `--clock SOURCE`     | `clock=SOURCE`     | Clock source for JFR timestamps: `tsc` (default) or `monotonic` (equivalent for `CLOCK_MONOTONIC`).                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `--begin function`   | `begin=FUNCTION`   | Automatically start profiling when the specified native function is executed.                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `--end function`     | `end=FUNCTION`     | Automatically stop profiling when the specified native function is executed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `--ttsp`             | `ttsp`             | Time-to-safepoint profiling. An alias for `--begin SafepointSynchronize::begin --end RuntimeService::record_safepoint_synchronized`.<br>It is not a separate event type, but rather a constraint. Whatever event type you choose (e.g. `cpu` or `wall`), the profiler will work as usual, except that only events between the safepoint request and the start of the VM operation will be recorded.                                                                                                                                         |
| `--nostop`           | `nostop`           | Record profiling window between `--begin` and `--end`, but do not stop profiling outside window.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `--libpath PATH`     | `libpath=PATH`     | Full path to `libasyncProfiler.so` (useful when profiling a container from the host).                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `--filter FILTER`    | `filter=FILTER`    | In the wall-clock profiling mode, profile only threads with the specified ids.<br>Example: `asprof -e wall -d 30 --filter 120-127,132,134 Computey`                                                                                                                                                                                                                                                                                                                                                                                         |
| `--fdtransfer`       | `fdtransfer`       | Run a background process that provides access to perf_events to an unprivileged process. `--fdtransfer` is useful for profiling a process in a container (which lacks access to perf_events) from the host.<br>See [Profiling Java in a container](ProfilingInContainer.md).                                                                                                                                                                                                                                                                |
| `--target-cpu`       | `target-cpu`       | In perf_events profiling mode, instruct the profiler to only sample threads running on the specified CPU, defaults to -1.<br>Example: `asprof --target-cpu 3`.                                                                                                                                                                                                                                                                                                                                                                              |
| `--record-cpu`       | `record-cpu`       | In perf_events profiling mode, instruct the profiler to capture which CPU a sample was taken on.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `-v --version`       | `version`          | Prints the version of profiler library. If PID is specified, gets the version of the library loaded into the given process.                                                                                                                                                                                                                                                                                                                                                                                                                 |

## Options applicable to JFR output only

| asprof              | Launch as agent    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ------------------- | ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `--chunksize N`     | `chunksize=N`      | Approximate size for a single JFR chunk. A new chunk will be started whenever specified size is reached. The default `chunksize` is 100MB.<br>Example: `asprof -f profile.jfr --chunksize 100m 8983`                                                                                                                                                                                                                                              |
| `--chunktime N`     | `chunktime=N`      | Approximate time limit for a single JFR chunk. A new chunk will be started whenever specified time limit is reached. The default `chunktime` is 1 hour.<br>Example: `asprof -f profile.jfr --chunktime 1h 8983`                                                                                                                                                                                                                                   |
| `--jfropts OPTIONS` | `jfropts=OPTIONS`  | Comma separated list of JFR recording options. Currently, the only available option is `mem` supported on Linux 3.17+. `mem` enables accumulating events in memory instead of flushing synchronously to a file.                                                                                                                                                                                                                                   |
| `--jfrsync CONFIG`  | `jfrsync[=CONFIG]` | Start Java Flight Recording with the given configuration synchronously with the profiler. The output .jfr file will include all regular JFR events, except that execution samples will be obtained from async-profiler. This option implies `-o jfr`.<br>`CONFIG` is a predefined JFR profile or a JFR configuration file (.jfc) or a list of JFR events started with `+`.<br><br>Example: `asprof -e cpu --jfrsync profile -f combined.jfr 8983` |
| `--all`             | `all`              | Shorthand for enabling `cpu`, `wall`, `alloc`, `live`, `nativemem` and `lock` profiling simultaneously. This can be combined with `--alloc 2m --lock 10ms` etc. to pass custom interval/threshold. It is also possible to combine it with `-e` argument to change the type of event being collected (default is `cpu`). This is not recommended for production, especially for continuous profiling.                                              |

## Options applicable to FlameGraph and Tree view outputs only

| asprof               | Launch as agent    | Description                                                                                                                                                                       |
| -------------------- | ------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `--title TITLE`      | `title=TITLE`      | Custom title of a FlameGraph.<br>Example: `asprof -f profile.html --title "Sample CPU profile" 8983`                                                                              |
| `--minwidth PERCENT` | `minwidth=PERCENT` | Minimum frame width as a percentage. Smaller frames will not be visible.<br>Example: `asprof -f profile.html --minwidth 0.5 8983`                                                 |
| `--reverse`          | `reverse`          | Reverse stack traces (defaults to icicle graph).<br>Example: `asprof -f profile.html --reverse 8983`                                                                              |
| `--inverted`         | `inverted`         | Toggles the layout for reversed stacktraces from icicle to flamegraph and for default stacktraces from flamegraph to icicle.<br>Example: `asprof -f profile.html --inverted 8983` |

Notice that `--reverse` and `--inverted` are orthogonal settings. By default, flamegraphs grow from bottom to top (because flames grow from bottom to top). The outermost frames (e.g. the `main()` function) are shown at the bottom while the innermost, leaf frames are shown at the top. If such a flame graph is mirrored on the y-axis, it becomes an icicle graph (icicles grow top-down). The default setting for this layout can be toggled with the `--inverted` option when the graph is created or changed later with the `Invert` button which is located in the upper-left corner of the generated HTML page, when the graph is displayed.

By default, async-profiler merges stack traces starting from the outermost (e.g. `main()`) frames and displays them from bottom to top in a flamegraph. The `--reverse` option can be used to create reverse stack traces, i.e. merge them starting with the innermost, leaf frames. By default, reversed stack traces are displayed from top to bottom as icicle graphs. The default layout setting for both, normal and reversed stack traces can be changed with the `--inverted` option.

## Options applicable to any output format except JFR

| asprof         | Launch as agent | Description                                                                                                                                                                                                                                |
| -------------- | --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `-t --threads` | `threads`       | Profile threads separately. Each stack trace will end with a frame that denotes a single thread.<br>Example: `asprof -t 8983`                                                                                                              |
| `-s --simple`  | `simple`        | Print simple class names instead of fully qualified names.                                                                                                                                                                                 |
| `-n --norm`    | `norm`          | Normalize names of hidden classes / lambdas.                                                                                                                                                                                               |
| `-g --sig`     | `sig`           | Print method signatures.                                                                                                                                                                                                                   |
| `-l --lib`     | `lib`           | Prepend library names to symbols, e.g. ``libjvm.so`JVM_DefineClassWithSource``.                                                                                                                                                            |
| `--total`      | `total`         | Count the total value of the collected metric instead of the number of samples, e.g. total allocation size.                                                                                                                                |
| `-a --ann`     | `ann`           | Annotate JIT compiled methods with `_[j]`, inlined methods with `_[i]`, interpreted methods with `_[0]` and C1 compiled methods with `_[1]`. FlameGraph and Tree view will color frames depending on their type regardless of this option. |

## Appendix

### Dump Option

`-o fmt` - specifies what information to dump when profiling ends.
`fmt` can be one of the following options:

- `traces[=N]` - dump call traces (at most N samples);
- `flat[=N]` - dump flat profile (top N hot methods);
  - can be combined with `traces`, e.g. `traces=200,flat=200`
- `jfr` - dump events in JDK Flight Recorder format readable by JDK Mission Control.
- `collapsed` - dump collapsed call traces in the format used by
  [FlameGraph](https://github.com/brendangregg/FlameGraph) script. This is
  a collection of call stacks, where each line is a semicolon separated list
  of frames followed by a counter.
- `flamegraph` - produce Flame Graph in HTML format.
- `tree` - produce Call Tree in HTML format.
  - `--reverse` option will generate backtrace view.
- `otlp` - dump events in OpenTelemetry format.

It is possible to specify multiple dump options at the same time.

```

## File: docs\profilingincontainer.md
```
# Profiling Java in a container

async-profiler provides the ability to profile Java processes running in a Docker or LXC
container both from within a container and from the host system.

When profiling from the host, `pid` should be the Java process ID in the host
namespace. Use `ps aux | grep java` or `docker top <container>` to find
the process ID.

async-profiler should be run from the host by a privileged user - it will
automatically switch to the proper pid/mount namespace and change
user credentials to match the target process. Also make sure that
the target container can access `libasyncProfiler.so` by the same
absolute path as on the host. Alternatively, specify `--libpath` option
to override path to `libasyncProfiler.so` in a container.

By default, Docker container restricts the access to `perf_event_open`
syscall. There are 3 alternatives to allow profiling in a container:

1. You can modify the [seccomp profile](https://docs.docker.com/engine/security/seccomp/)
   or disable it altogether with `--security-opt seccomp=unconfined` option. In
   addition, `--cap-add SYS_ADMIN` may be required.
2. You can use "fdtransfer": see the help for `--fdtransfer`.
3. Last, you may fall back to `-e ctimer` profiling mode, see [Troubleshooting](Troubleshooting.md).

```

## File: docs\profilingmodes.md
```
# Profiling modes

Besides CPU time, async-profiler provides various other profiling modes such as `Allocation`, `Wall Clock`, `Java Method`
and even a `Multiple Events` profiling mode.

## CPU profiling

In this mode, profiler collects stack trace samples that include **Java** methods,
**native** calls, **JVM** code and **kernel** functions.

The general approach is receiving call stacks generated by `perf_events`
and matching them up with call stacks generated by `AsyncGetCallTrace`,
in order to produce an accurate profile of both Java and native code.
Additionally, async-profiler provides a workaround to recover stack traces
in some [corner cases](https://bugs.openjdk.java.net/browse/JDK-8178287)
where `AsyncGetCallTrace` fails.

This approach has the following advantages compared to using `perf_events`
directly with a Java agent that translates addresses to Java method names:

- Does not require `-XX:+PreserveFramePointer`, which introduces
  performance overhead that can be sometimes as high as 10%.

- Does not require starting JVM with an agent for translating Java code addresses
  to method names.

- Displays interpreter frames.

- Does not produce large intermediate files (perf.data) for further processing in
  user space scripts.

If you wish to resolve frames within `libjvm`, the [debug symbols](#installing-debug-symbols) are required.

## ALLOCATION profiling

The profiler can be configured to collect call sites where the largest amount
of heap memory is allocated.

async-profiler does not use intrusive techniques like bytecode instrumentation
or expensive DTrace probes which have significant performance impact.
It also does not affect Escape Analysis or prevent from JIT optimizations
like allocation elimination. Only actual heap allocations are measured.

The profiler features TLAB-driven sampling. It relies on HotSpot-specific
callbacks to receive two kinds of notifications:

- when an object is allocated in a newly created TLAB;
- when an object is allocated on a slow path outside TLAB.

Sampling interval can be adjusted with `--alloc` option.
For example, `--alloc 500k` will take one sample after 500 KB of allocated
space on average. Prior to JDK 11, intervals less than TLAB size will not take effect.

In allocation profiling mode, the top frame of every call trace is the class
of the allocated object, and the counter is the heap pressure (the total size
of allocated TLABs or objects outside TLAB).

### Installing Debug Symbols

Prior to JDK 11, the allocation profiler required HotSpot debug symbols.
Some OpenJDK distributions (Amazon Corretto, Liberica JDK, Azul Zulu)
already have them embedded in `libjvm.so`, other OpenJDK builds typically
provide debug symbols in a separate package. For example, to install
OpenJDK debug symbols on Debian / Ubuntu, run:

```
# apt install openjdk-17-dbg
```

(replace `17` with the desired version of JDK).

On CentOS, RHEL and some other RPM-based distributions, this could be done with
[debuginfo-install](http://man7.org/linux/man-pages/man1/debuginfo-install.1.html) utility:

```
# debuginfo-install java-1.8.0-openjdk
```

On Gentoo, the `icedtea` OpenJDK package can be built with the per-package setting
`FEATURES="nostrip"` to retain symbols.

The `gdb` tool can be used to verify if debug symbols are properly installed for the `libjvm` library.
For example, on Linux:

```
$ gdb $JAVA_HOME/lib/server/libjvm.so -ex 'info address UseG1GC'
```

This command's output will either contain `Symbol "UseG1GC" is at 0xxxxx`
or `No symbol "UseG1GC" in current context`.

## Native memory leaks

The profiling mode `nativemem` records `malloc`, `realloc`, `calloc` and `free` calls
with the addresses, so that allocations can be matched with frees. This helps to focus
the profile report only on unfreed allocations, which are the likely to be a source of a memory leak.

Example:

```
asprof start -e nativemem -f app.jfr <YourApp>
# or
asprof start --nativemem N -f app.jfr <YourApp>
# or if only allocation calls are interesting, do not collect free calls:
asprof start --nativemem N --nofree -f app.jfr <YourApp>

asprof stop <YourApp>
```

Now we need to process the jfr file, to find native memory leaks:

```
# --total for bytes, default counts invocations.
jfrconv --total --nativemem --leak app.jfr app-leak.html

# No leak analysis, include all native allocations:
jfrconv --total --nativemem app.jfr app-malloc.html
```

When `--leak` option is used, the generated flame graph will show allocations without matching `free` calls.

![nativemem flamegraph](../.assets/images/nativemem_flamegraph.png)

To avoid bias towards youngest allocations not freed by the end of the profiling session,
leak profiler ignores tail allocations made in the last 10% of the profiling period.
Tail length can be altered with `--tail` option that accepts `ratio` or `percent%` as an argument.
For example, to ignore allocations in the last 2 minutes of a 10 minutes profile, use

```
jfrconv --nativemem --leak --tail 20% app.jfr app-leak.html
```

The overhead of `nativemem` profiling depends on the number of native allocations,
but is usually small enough even for production use. If required, the overhead can be reduced
by configuring the profiling interval. E.g. if you add `nativemem=1m` profiler option,
allocation samples will be limited to at most one sample per allocated megabyte.

### Using LD_PRELOAD for finding native memory leaks

Similar to Java applications, `nativemem` mode can be also used with [non-Java processes](ProfilingNonJavaApplications.md).

Run an application with `nativemem` profiler that dumps recordings in JFR format every 10 minutes:

```
LD_PRELOAD=/path/to/libasyncProfiler.so ASPROF_COMMAND=start,nativemem,total,loop=10m,cstack=dwarf,file=profile-%t.jfr NativeApp [args]
```

Then run `jfrconv` to generate memory leak report as a flame graph:

```
jfrconv --total --nativemem --leak <profile>.jfr <profile>-leak.html
```

## Wall-clock profiling

`-e wall` option tells async-profiler to sample all threads equally every given
period of time regardless of thread status: Running, Sleeping or Blocked.
For instance, this can be helpful when profiling application start-up time.

Wall-clock profiler is most useful in per-thread mode: `-t`.

Example: `asprof -e wall -t -i 50ms -f result.html 8983`

## Lock profiling

`-e lock` option tells async-profiler to measure lock contention in the profiled application. Lock profiling can help
developers understand lock acquisition patterns, lock contention (when threads have to wait to acquire locks), time
spent waiting for locks and which code paths are blocked due to locks.

In lock profiling mode, the top frame is the class of lock/monitor, and the counter is number of nanoseconds it took to
enter this lock/monitor.

Example: `asprof -e lock -t -i 5ms -f result.html 8983`

## Native lock profiling

`--nativelock` option tells async-profiler to measure pthread lock contention in the profiled application.
Native lock profiling can help developers understand pthread lock acquisition patterns, lock contention (when threads
have to wait to acquire native locks), time spent waiting for pthread mutexes and read-write locks, and which code paths
are blocked due to native synchronization primitives.

Native lock profiling works by intercepting calls to:

- [`pthread_mutex_lock`](https://man7.org/linux/man-pages/man3/pthread_mutex_lock.3p.html)
- [`pthread_rwlock_rdlock`](https://man7.org/linux/man-pages/man3/pthread_rwlock_rdlock.3p.html)
- [`pthread_rwlock_wrlock`](https://man7.org/linux/man-pages/man3/pthread_rwlock_wrlock.3p.html)

In this mode, the top frame shows the native function that experienced contention (e.g., pthread_mutex_lock_hook),
and the counter represents the number of nanoseconds threads spent waiting to acquire the lock.

Key differences from Java lock profiling:

- Profiles native pthread locks instead of Java monitors.
- Works with C/C++ applications and native libraries used by Java applications.
- Captures contention in native code paths that Java lock profiling cannot see.

Example: `asprof --nativelock 5ms -t -f result.html 8983`

## Java method profiling

`-e ClassName.methodName` option instruments the given Java method
in order to record all invocations of this method with the stack traces.

Example: `-e java.util.Properties.getProperty` will profile all places
where `getProperty` method is called from.

Only non-native Java methods are supported. To profile a native method,
use hardware breakpoint event instead, e.g. `-e Java_java_lang_Throwable_fillInStackTrace`

**Be aware** that if you attach async-profiler at runtime, the first instrumentation
of a non-native Java method may cause the [deoptimization](https://github.com/openjdk/jdk/blob/bf2e9ee9d321ed289466b2410f12ad10504d01a2/src/hotspot/share/prims/jvmtiRedefineClasses.cpp#L4092-L4096)
of all compiled methods. The subsequent instrumentation flushes only the _dependent code_.

The massive CodeCache flush doesn't occur if attaching async-profiler as an agent.

### Latency profiling

Please refer to our blog post on [latency profiling](https://github.com/async-profiler/async-profiler/discussions/1497)
to know more about this profiling mode.

## Native function profiling

Here are some useful native functions to profile:

- `G1CollectedHeap::humongous_obj_allocate` - trace _humongous allocations_ of the G1 GC,
- `JVM_StartThread` - trace creation of new Java threads,
- `Java_java_lang_ClassLoader_defineClass1` - trace class loading.

## Multiple events

It is possible to profile CPU, allocations, and locks at the same time.
Instead of CPU, you may choose any other execution event: wall-clock,
perf event, tracepoint, Java method, etc.

The only output format that supports multiple events together is JFR.
The recording will contain the following event types:

- `jdk.ExecutionSample`
- `jdk.ObjectAllocationInNewTLAB` (alloc)
- `jdk.ObjectAllocationOutsideTLAB` (alloc)
- `jdk.JavaMonitorEnter` (lock)
- `jdk.ThreadPark` (lock)

To start profiling cpu + allocations + locks together, specify

```
asprof -e cpu,alloc,lock -f profile.jfr ...
```

or use `--alloc` and `--lock` parameters with the desired threshold:

```
asprof -e cpu --alloc 2m --lock 10ms -f profile.jfr ...
```

The same, when starting profiler as an agent:

```
-agentpath:/path/to/libasyncProfiler.so=start,event=cpu,alloc=2m,lock=10ms,file=profile.jfr
```

### Multi-event profiling using `--all`

The `--all` flag offers a way to simultaneously enable predefined collection of common profiling events. By default, `--all` activates profiling for `cpu`, `wall`, `alloc`, `live`, `lock` and `nativemem`.

**Important consideration**

While the `--all` flag can be useful for development environments to get a wide overview, it is not recommended to enable this in production, especially for continuous profiling. Users are invited to select carefully what to profile and with what settings.

**Sample command:**

This command enables the default set of events included in `--all`:

```
asprof --all -f profile.jfr
```

or combine it with `--alloc`/`--wall`/`--lock`/`--nativemem` options to override individual settings. For example:

```
asprof --all --alloc 2m --lock 10ms -f profile.jfr
```

The same, when starting profiler as an agent:

```
-agentpath:/path/to/libasyncProfiler.so=start,all,alloc=2m,lock=10ms,file=profile.jfr
```

Instead of `cpu`, it is possible to override the `--all` parameter with any other event type of your choice. For instance, the following command will profile `cycles` along with ` wall`, `alloc`, `live`, `lock` and `nativemem`:

```
asprof --all -e cycles -f profile.jfr
```

## Continuous profiling

Continuous profiling is a means by which an application can be profiled
continuously and dump profile results every specified time period.
It is a very effective technique in finding performance degradations proactively
and efficiently. Continuous profiling helps users to understand performance
differences between versions of the same application. Recent outputs can
be compared with continuous profiling output history to find differences
and optimize the changes introduced in case of performance degradations.
aysnc-profiler provides the ability to continously profile an application with
the `loop` option. Make sure the filename includes a timestamp pattern, or the
output will be overwritten on each iteration.

```
asprof --loop 1h -f /var/log/profile-%t.jfr 8983
```

## perf event types supported on Linux

| Usage                                     | Description                                                                                                                                                                                                                                        |
| ----------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Predefined:                               |                                                                                                                                                                                                                                                    |
| `-e cpu-clock`                            | High-resolution per-CPU timer. Similar to `-e cpu` but forces using perf_events.                                                                                                                                                                   |
| `-e page-faults`                          | Software page faults                                                                                                                                                                                                                               |
| `-e context-switches`                     | Context switches                                                                                                                                                                                                                                   |
| `-e cycles`                               | Total CPU cycles                                                                                                                                                                                                                                   |
| `-e ref-cycles`                           | CPU reference cycles, not affected by CPU frequency scaling                                                                                                                                                                                        |
| `-e instructions`                         | Retired CPU instructions                                                                                                                                                                                                                           |
| `-e cache-references`                     | Cache accesses (usually Last Level Cache, but may depend on the architecture)                                                                                                                                                                      |
| `-e cache-misses`                         | Cache accesses requiring fetching data from a higher-level cache or main memory                                                                                                                                                                    |
| `-e branch-instructions`                  | Retired branch instructions                                                                                                                                                                                                                        |
| `-e branch-misses`                        | Mispredicted branch instructions                                                                                                                                                                                                                   |
| `-e bus-cycles`                           | Bus cycles                                                                                                                                                                                                                                         |
| `-e L1-dcache-load-misses`                | Cache misses on Level 1 Data Cache                                                                                                                                                                                                                 |
| `-e LLC-load-misses`                      | Cache misses on the Last Level Cache                                                                                                                                                                                                               |
| `-e dTLB-load-misses`                     | Data load misses on the Translation Lookaside Buffer                                                                                                                                                                                               |
| Breakpoint:                               |                                                                                                                                                                                                                                                    |
| `-e mem:<addr>`                           | Breakpoint on a decimal or hex (0x) address                                                                                                                                                                                                        |
| `-e mem:<func>`                           | Breakpoint on a public or a private symbol                                                                                                                                                                                                         |
| `-e mem:<func>[+<offset>][/<len>][:rwx>]` | Breakpoint on a symbol or an address with offset, length and read/write/exec. Address, offset and length can be hex or dec. The format of `mem` event is the same as in [`perf-record`](https://man7.org/linux/man-pages/man1/perf-record.1.html). |
| `-e <symbol>`                             | Equivalent to an execution breakpoint on a symbol: `mem:<symbol>:x`. Example: `-e strcmp` will trace all calls of native `strcmp` function.                                                                                                        |
| Tracepoint:                               |                                                                                                                                                                                                                                                    |
| `-e trace:<id>`                           | Kernel tracepoint with the given numeric id                                                                                                                                                                                                        |
| `-e <tracepoint>`                         | Kernel tracepoint with the specified name. Example: `-e syscalls:sys_enter_open` will trace all `open` syscalls.                                                                                                                                   |
| Probes:                                   |                                                                                                                                                                                                                                                    |
| `-e kprobe:<func>[+<offset>]`             | Kernel probe. Example: `-e kprobe:do_sys_open`.                                                                                                                                                                                                    |
| `-e kretprobe:<func>[+<offset>]`          | Kernel return probe. Example: `-e kretprobe:do_sys_open`.                                                                                                                                                                                          |
| `-e uprobe:<func>[+<offset>]`             | Userspace probe. Example: `-e uprobe:/usr/lib64/libc-2.17.so+0x114790`.                                                                                                                                                                            |
| `-e uretprobe:<func>[+<offset>]`          | Userspace return probe                                                                                                                                                                                                                             |
| PMU:                                      |                                                                                                                                                                                                                                                    |
| `-e r<NNN>`                               | Architecture-specific PMU event with the given number. Example: `-e r4d2` selects `MEM_LOAD_L3_HIT_RETIRED.XSNP_HITM` event, which corresponds to event 0xd2, umask 0x4.                                                                           |
| `-e <pmu descriptor>`                     | PMU event descriptor. Example: `-e cpu/cache-misses/`, `-e cpu/event=0xd2,umask=4/`. The same syntax can be used for uncore and vendor-specific events, e.g. `amd_l3/event=0x01,umask=0x80/`                                                       |

```

## File: docs\profilingnonjavaapplications.md
```
# Profiling Non-Java applications

The scope of profiling non-Java applications is limited to the case when profiler is controlled
programmatically from the process being profiled or with `LD_PRELOAD`. It is worth noting that
[dynamic attach](IntegratingAsyncProfiler.md#launching-as-an-agent)
which is available for Java is not supported for non-Java profiling.

## LD_PRELOAD

async-profiler can be injected into a native application through the `LD_PRELOAD` mechanism:

```
LD_PRELOAD=/path/to/libasyncProfiler.so ASPROF_COMMAND=start,event=cpu,file=profile.jfr NativeApp [args]
```

All basic functionality remains the same. Profiler can run in `cpu`, `wall`, `nativemem` and other perf_events
modes. Flame Graph and JFR output formats are supported, although JFR files will obviously lack
Java-specific events.

See [Profiling Modes](ProfilingModes.md) for more examples.

## Controlling async-profiler via the C API

Similar to the
[Java API](IntegratingAsyncProfiler.md#using-java-api),
there is a C API for using profiler inside a native application.

Header file for the API is bundled in the async-profiler release package under [`include/asprof.h`](../src/asprof.h).

To use it in a C/C++ application, include the mentioned `asprof.h`. Below is an example showing how to invoke async-profiler with the API:

```
#include "asprof.h"
#include <dlfcn.h>
#include <stdio.h>
#include <stdlib.h>

void test_output_callback(const char* buffer, size_t size) {
    fwrite(buffer, sizeof(char), size, stderr);
}

int main() {
    void* lib = dlopen("/path/to/libasyncProfiler.so", RTLD_NOW);
    if (lib == NULL) {
        printf("%s\n", dlerror());
        exit(1);
    }

    asprof_init_t asprof_init = (asprof_init_t)dlsym(lib, "asprof_init");
    asprof_execute_t asprof_execute = (asprof_execute_t)dlsym(lib, "asprof_execute");
    asprof_error_str_t asprof_error_str = (asprof_error_str_t)dlsym(lib, "asprof_error_str");

    if (asprof_init == NULL || asprof_execute == NULL || asprof_error_str == NULL) {
        printf("%s\n", dlerror());
        dlclose(lib);
        exit(1);
    }

    asprof_init();

    printf("Starting profiler\n");

    char cmd[] = "start,event=cpu,loglevel=debug,file=profile.jfr";
    asprof_error_t err = asprof_execute(cmd, test_output_callback);
    if (err != NULL) {
        fprintf(stderr, "%s\n", asprof_error_str(err));
        exit(1);
    }

    // ... some meaningful work ...

    printf("Stopping profiler\n");

    err = asprof_execute("stop", test_output_callback);
    if (err != NULL) {
        fprintf(stderr, "%s\n", asprof_error_str(err));
        exit(1);
    }

    return 0;
}
```

## Unstable APIs

These APIs are unstable and might change or be removed in the next version of async-profiler.

### Advanced Sampling

The `asprof_get_thread_local_data` function returns a pointer to async-profiler's
thread-local data structure. The structure is guaranteed to live as long as the thread.

The returned structure contains a pointer that increments every time there is a sample. This gives
native code an easy way to detect when a sample event had occurred, and to log metadata about what the
program was doing when the event happened.

```

## File: docs\stackwalkingmodes.md
```
# Stack Walking Modes

## Frame Pointer

`Frame Pointer (FP)` stack walking is a technique for collecting call stacks by tracking frame pointers in memory.
Each function call maintains a pointer to its caller's stack frame, creating a linked chain that can be traversed
to reconstruct the program's execution path. It's particularly efficient as it is very fast compared to other
stack walking methods introducing less overhead but requires code to be compiled with frame
pointers enabled (`-fno-omit-frame-pointer`).

Before async-profiler 4.2, Frame Pointer was the default stack walking mode.
Since version 4.2, the default was changed to [VM Structs](#vm-structs).

## DWARF

DWARF stack walking is a method to reconstruct call stacks using unwinding information embedded in executables
(typically in `.eh_frame` section). Unlike frame-pointer-based unwinding, it works reliably even with optimized code
where frame pointers are omitted.

DWARF unwinding requires extra memory (e.g. the lookup table for `libjvm.so` is about 2MB).
It is also slower than the traditional FP-based stack walker, but it's still fast enough for on-the-fly unwinding
due to being signal safe in async-profiler.

The feature can be enabled with the option `--cstack dwarf` (or its agent equivalent `cstack=dwarf`).

## LBR

Modern Intel CPUs can profile branch instructions, including `call`s and `ret`s, and store their source and destination
addresses (Last Branch Records) in hardware registers. Starting from Haswell, CPU can match these addresses to form a
branch stack. This branch stack will be effectively a call chain automatically collected by the hardware.

LBR stacks are not always complete or accurate, but they still appear much more helpful comparing to FP-based stack
walking, when a native library is compiled with omitted frame pointers. It works only with hardware events like
`-e cycles` (`instructions`, `cache-misses` etc.) and the maximum call chain depth is 32 (hardware limit).

The feature can be enabled with the option `--cstack lbr` (or its agent equivalent `cstack=lbr`).

## VM Structs

async-profiler can leverage JVM internal structures to replicate the logic of Java stack walking
in the profiler itself without depending on the unstable JVM API.

This mode of stack walking has been introduced in async-profiler due to issues with `AsyncCallGetTrace`.
AsyncGetCallTrace (AGCT) is a non-standard extension of HotSpot JVM to obtain Java stack traces outside safepoints.
async-profiler had been relying on AGCT heavily, and it even got its name after this function.

`AsyncGetCallTrace` being non-API, was never supported in OpenJDK well enough, it did not receive enough testing, it was
broken several times even in minor JDK updates, e.g. [JDK-8307549](https://bugs.openjdk.org/browse/JDK-8307549).

AsyncGetCallTrace is notorious for its inability to walk Java stack in different corner cases. There is a long-standing
bug [JDK-8178287](https://bugs.openjdk.org/browse/JDK-8178287) with several examples. But the worst aspect is that
AsyncGetCallTrace can crash JVM, and there is no reliable way to get around this outside the JVM.

Due to issues with AGCT from time to time, including random crashes and missing stack traces,
`vm` stack walking mode based on HotSpot VM Structs was introduced in async-profiler.
`vm` stack walker has the following advantages:

- Fully enclosed by the crash protection based on `setjmp`/`longjmp`.
- Can show all frames: Java, native and JVM stubs throughout the whole stack.
- Provides additional information on each frame, like JIT compilation type.

The feature can be enabled with the option `--cstack vm` (or its agent equivalent `cstack=vm`).
Since async-profiler 4.2, this is the default mode when running on the HotSpot JVM.

Another variant of this option: `--cstack vmx` activates an "expert" unwinding based on VM Structs.
With this option, async-profiler collects mixed stack traces that have Java and native frames interleaved.

The maximum stack depth for `vm` or `vmx` stack walking is controlled with `-j depth` option.

```

## File: docs\troubleshooting.md
```
# Troubleshooting

## Error Messages

### perf_event mmap failed: Operation not permitted

Profiler allocates 8 kB perf_event buffer for each thread of the target process.
The above error may appear if the total size of perf_event buffers (`8 * threads` kB)
exceeds locked memory limit. This limit is comprised of `ulimit -l` plus
the value of `kernel.perf_event_mlock_kb` sysctl multiplied by the number of CPU cores.
For example, on a 16-core machine, `ulimit -l 65536` and `kernel.perf_event_mlock_kb=516`
is enough for profiling `(65536 + 516*16) / 8 = 9224` threads.
If an application has more threads, increase one of the above limits, or native stacks
will not be collected for some threads.

A privileged process is not subject to the locked memory limit.

### Failed to change credentials to match the target process: Operation not permitted

Due to limitation of HotSpot Dynamic Attach mechanism, the profiler must be run
by exactly the same user (and group) as the owner of target JVM process.
If profiler is run by a different user, it will try to automatically change
current user and group. This will likely succeed for `root`, but not for
other users, resulting in the above error.

### Could not start attach mechanism: No such file or directory

The profiler cannot establish communication with the target JVM through UNIX domain socket.
Usually this happens in one of the following cases:

1. Attach socket `/tmp/.java_pidNNN` has been deleted. It is a common
   practice to clean `/tmp` automatically with some scheduled script.
   Configure the cleanup software to exclude `.java_pid*` files from deletion.

   - How to check: run `lsof -p PID | grep java_pid`. If it lists a socket file, but the file does not exist, then this is exactly
     the described problem.

2. JVM is started with `-XX:+DisableAttachMechanism` option.
3. `/tmp` directory of Java process is not physically the same directory
   as `/tmp` of your shell, because Java is running in a container or in
   `chroot` environment. `asprof` attempts to solve this automatically,
   but it might lack the required permissions to do so.
   - Check `strace asprof PID jcmd`
4. JVM is busy and cannot reach a safepoint. For instance,
   JVM is in the middle of long-running garbage collection.
   - How to check: run `kill -3 PID`. Healthy JVM process should print
     a thread dump and heap info in its console.

### Target JVM failed to load libasyncProfiler.so

The connection with the target JVM has been established, but JVM is unable to load profiler shared library.
Make sure the user of JVM process has permissions to access `libasyncProfiler.so` by exactly the same absolute path.
For more information see [#78](https://github.com/async-profiler/async-profiler/issues/78).

### Perf events unavailable

`perf_event_open()` syscall has failed. Typical reasons include:

1. `/proc/sys/kernel/perf_event_paranoid` is set to restricted mode (>=2).
2. seccomp disables `perf_event_open` API in a container.
3. OS runs under a hypervisor that does not virtualize performance counters.
4. perf_event_open API is not supported on this system, e.g. WSL.

<br>For permissions-related reasons (such as 1 and 2), using `--fdtransfer` while running the profiler
as a privileged user may solve the issue.

If changing the configuration is not possible, you may fall back to
`-e ctimer` profiling mode. It is similar to `cpu` mode, but does not
require perf_events support. As a drawback, there will be no kernel
stack traces.

### No AllocTracer symbols found. Are JDK debug symbols installed?

The OpenJDK debug symbols are required for allocation profiling for applications developed
with JDK prior to 11. See [Installing Debug Symbols](ProfilingModes.md#installing-debug-symbols) for more
details. If the error message persists after a successful installation of the debug symbols,
it is possible that the JDK was upgraded when installing the debug symbols.
In this case, profiling any Java process which had started prior to the installation
will continue to display this message, since the process had loaded
the older version of the JDK which lacked debug symbols.
Restarting the affected Java processes should resolve the issue.

### VMStructs unavailable. Unsupported JVM?

JVM shared library does not export `gHotSpotVMStructs*` symbols -
apparently this is not a HotSpot JVM. Sometimes the same message
can be also caused by an incorrectly built JDK
(see [#218](https://github.com/async-profiler/async-profiler/issues/218)).
In these cases installing JDK debug symbols may solve the problem.

### Could not parse symbols from <libname.so>

Async-profiler was unable to parse non-Java function names because of
the corrupted contents in `/proc/[pid]/maps`. The problem is known to
occur in a container when running Ubuntu with Linux kernel 5.x.
This is the OS bug, see <https://bugs.launchpad.net/ubuntu/+source/linux/+bug/1843018>.

### Could not open output file

Output file is written by the target JVM process, not by the profiler script.
Make sure the path specified in `-f` option is correct and is accessible by the JVM.

## Known Limitations

- No Java stacks will be collected if `-XX:MaxJavaStackTraceDepth` is zero
  or negative. The exception is `--cstack vm` mode, which does not take
  `MaxJavaStackTraceDepth` into account.

- Too short profiling interval may cause continuous interruption of heavy
  system calls like `clone()`, so that it will never complete;
  see [#97](https://github.com/async-profiler/async-profiler/issues/97).
  The workaround is simply to increase the interval.

- When agent is not loaded at JVM startup (by using -agentpath option) it is
  highly recommended to use `-XX:+UnlockDiagnosticVMOptions -XX:+DebugNonSafepoints` JVM flags.
  Without those flags the profiler will still work correctly but results might be
  less accurate. For example, without `-XX:+DebugNonSafepoints` there is a high chance
  that simple inlined methods will not appear in the profile. When the agent is attached at runtime,
  `CompiledMethodLoad` JVMTI event enables debug info, but only for methods compiled after attaching.

- On most Linux systems, `perf_events` captures call stacks with a maximum depth
  of 127 frames. On recent Linux kernels, this can be configured using
  `sysctl kernel.perf_event_max_stack` or by writing to the
  `/proc/sys/kernel/perf_event_max_stack` file.

- You will not see the non-Java frames _preceding_ the Java frames on the
  stack, unless `--cstack vmx` is specified.
  For example, if `start_thread` called `JavaMain` and then your Java
  code started running, you will not see the first two frames in the resulting
  stack. On the other hand, you _will_ see non-Java frames (user and kernel)
  invoked by your Java code.

- macOS profiling is limited to user space code only.

```

## File: src\res\flame.html
```
<!DOCTYPE html>
<html lang='en'>
<head>
<meta charset='utf-8'>
<style>
	body {margin: 0; padding: 10px 10px 22px 10px; background-color: #ffffff}
	h1 {margin: 5px 0 0 0; font-size: 18px; font-weight: normal; text-align: center}
	header {margin: -22px 0 6px 0}
	button {border: none; background: none; width: 24px; height: 24px; cursor: pointer; margin: 0; padding: 2px 0 0 0; text-align: center}
	button:hover {background-color: #ffffe0; outline: 1px solid #ffc000; border-radius: 4px}
	dl {margin: 0 4px 8px 4px}
	dt {margin: 1px; padding: 2px 0; font-weight: bold}
	dd {margin: 1px; padding: 2px 4px}
	dl.frames {float: left; width: 160px}
	dl.hotkeys {clear: left; border-top: 1px solid #666666}
	dl.hotkeys > dt {float: left; clear: left; width: 158px; margin-right: 4px; text-align: right}
	dl.hotkeys > dd {float: left}
	p {position: fixed; bottom: 0; margin: 0; padding: 2px 3px 2px 3px; outline: 1px solid #ffc000; display: none; overflow: hidden; white-space: nowrap; background-color: #ffffe0}
	a {color: #0366d6}
	#legend {padding: 4px; border-radius: 4px; background: #ffffe0; border: 1px solid #666666; display: none}
	#hl {position: absolute; display: none; overflow: hidden; white-space: nowrap; pointer-events: none; background-color: #ffffe0; outline: 1px solid #ffc000; height: 15px}
	#hl span {padding: 0 3px 0 3px}
	#status {left: 0}
	#match {right: 0}
	#reset {cursor: pointer}
	#canvas {width: 100%; height: /*height:*/300px}
</style>
</head>
<body style='font: 12px Verdana, sans-serif'>
<h1>/*title:*/</h1>
<header style='float: left'>
<button id='inverted' title='Invert (I)'><svg xmlns='http://www.w3.org/2000/svg' width='20' height='20' viewBox='0 0 392 392'><path d='M196,36 L316,156 L76,156 Z' fill='#004d80'/><path d='M196,356 L76,236 L316,236 Z' fill='#004d80'/><path d='M196,54 L298,156 L94,156 Z' fill='#ff8d40'/><path d='M196,338 L94,236 L298,236 Z' fill='#40b2ff'/><rect x='94' y='188' width='204' height='16' fill='#004d80'/></svg></button>
<button id='search' title='Search (Ctrl+F)'><svg xmlns='http://www.w3.org/2000/svg' width='20' height='20' viewBox='-39.3 -39.3 471.1 471.1'><circle cx='147.7' cy='147.8' r='125.9' fill='#fff'/><path fill='#40b2ff' d='M370.7 348.7c0 1.4-1.6 6.3-7.2 12.3-6.2 6.7-12.5 9.8-14.7 9.8h-.1c-19.5-1.6-62-43.2-109.6-106.8 9.2-7.2 17.5-15.5 24.6-24.6 63.6 47.6 105.2 90.2 106.8 109.6z'/><path fill='#ff8d40' d='M208.7 86.9l-14.5 14.5c-17.1 17.1-46.5 5-46.5-19.3V61.6c-49 0-88.4 40.8-86.1 90.2 2 43.9 38.1 80 82 82 49.5 2.3 90.2-37.2 90.2-86.1 0-23.7-9.6-45.2-25.1-60.8z'/><path fill='#004d80' d='M276.1 221c12.3-21.5 19.5-46.5 19.5-73.2C295.6 66.3 229.2.1 147.7.1S0 66.3 0 147.9s66.3 147.7 147.7 147.7c26.6 0 51.5-7.1 73.2-19.5 39.8 53.3 91.9 113.5 126.1 116.4 12.3.5 22.9-6.7 32.8-16.7 5.2-5.6 13.8-16.9 12.8-28.8-2.9-34.1-63.1-86.2-116.4-126.1zM147.7 273.8c-69.5 0-125.9-56.5-125.9-125.9S78.3 21.9 147.7 21.9 273.6 78.4 273.6 147.8s-56.4 126-125.9 126zm215.9 87.2c-6.2 6.7-12.4 9.8-14.7 9.8h-.1c-19.5-1.6-62-43.2-109.6-106.8 9.2-7.2 17.5-15.5 24.6-24.6 63.6 47.6 105.2 90.2 106.8 109.6 0 1.4-1.6 6.3-7.2 12.4z'/></svg></button>
<button id='info'><svg xmlns='http://www.w3.org/2000/svg' width='20' height='20' viewBox='0 0 20 20'><circle cx='10' cy='10' r='8' stroke='#004d80' fill='none'/><path d='M10 5.5c-1.25 0-2.25 1-2.25 2.25H9a1.25 1.25 0 0 1 2.5 0c0 .65-.55 1-1 1.2-.7.35-1.25.85-1.25 1.8V11h1.5v-.25c0-.37.29-.65.68-.83.73-.34 1.32-.87 1.32-2.17 0-1.25-1.5-2.25-2.75-2.25' fill='#ff8d40' stroke='#ff8d40' stroke-width='.6' stroke-linecap='round' stroke-linejoin='round'/><circle cx='10' cy='13.5' r='1.2' fill='#ff8d40'/></svg></button>
</header>
<header style='float: right'>Produced by <a href='https://github.com/async-profiler/async-profiler'>async-profiler</a></header>
<div id='legend' style='position: absolute'>
<dl class='frames'>
	<dt>Frame types</dt>
	<dd style='background-color: #e17d00'>Kernel</dd>
	<dd style='background-color: #e15a5a'>Native</dd>
	<dd style='background-color: #c8c83c'>C++ (VM)</dd>
	<dd style='background-color: #50e150'>Java compiled</dd>
	<dd style='background-color: #cce880'>Java compiled by C1</dd>
	<dd style='background-color: #50cccc'>Inlined</dd>
	<dd style='background-color: #b2e1b2'>Interpreted</dd>
</dl>
<dl class='frames'>
	<dt>Allocation profile</dt>
	<dd style='background-color: #50cccc'>Allocated class</dd>
	<dd style='background-color: #e17d00'>Allocation outside TLAB</dd>
	<dt>Lock profile</dt>
	<dd style='background-color: #50cccc'>Lock class</dd>
	<dt>&nbsp;</dt>
	<dt>Search</dt>
	<dd style='background-color: #ee00ee'>Matches regexp</dd>
</dl>
<dl class='hotkeys'>
	<dt>Click frame</dt><dd>Zoom into frame</dd>
	<dt>Alt+Click</dt><dd>Remove stack</dd>
	<dt>0</dt><dd>Reset zoom</dd>
	<dt>I</dt><dd>Invert graph</dd>
	<dt>Ctrl+F</dt><dd>Search</dd>
	<dt>N</dt><dd>Next match</dd>
	<dt>Shift+N</dt><dd>Previous match</dd>
	<dt>Esc</dt><dd>Cancel search</dd>
</dl>
</div>
<canvas id='canvas'></canvas>
<div id='hl'><span></span></div>
<p id='status'></p>
<p id='match'>Matched: <span id='matchval'></span> <span id='reset' title='Clear'>&#x274c;</span></p>
<script>
	// Copyright The async-profiler authors
	// SPDX-License-Identifier: Apache-2.0
	'use strict';
	let root, px, pattern;
	let level0 = 0, left0 = 0, width0 = 0;
	let nav = [], navIndex, matchval;
	let inverted = /*inverted:*/false;
	const levels = Array(/*depth:*/0);
	for (let h = 0; h < levels.length; h++) {
		levels[h] = [];
	}

	const canvas = document.getElementById('canvas');
	const c = canvas.getContext('2d');
	const hl = document.getElementById('hl');
	const status = document.getElementById('status');

	const canvasWidth = canvas.offsetWidth;
	const canvasHeight = canvas.offsetHeight;
	canvas.style.width = canvasWidth + 'px';
	canvas.width = canvasWidth * (devicePixelRatio || 1);
	canvas.height = canvasHeight * (devicePixelRatio || 1);
	if (devicePixelRatio) c.scale(devicePixelRatio, devicePixelRatio);
	c.font = document.body.style.font;

	const palette = [
		[0xb2e1b2, 20, 20, 20],
		[0x50e150, 30, 30, 30],
		[0x50cccc, 30, 30, 30],
		[0xe15a5a, 30, 40, 40],
		[0xc8c83c, 30, 30, 10],
		[0xe17d00, 30, 30,  0],
		[0xcce880, 20, 20, 20],
	];

	function getColor(p) {
		const v = Math.random();
		return '#' + (p[0] + ((p[1] * v) << 16 | (p[2] * v) << 8 | (p[3] * v))).toString(16);
	}

	function f(key, level, left, width, inln, c1, int) {
		levels[level0 = level].push({level, left: left0 += left, width: width0 = width || width0,
			color: getColor(palette[key & 7]), title: cpool[key >>> 3],
			details: (int ? ', int=' + int : '') + (c1 ? ', c1=' + c1 : '') + (inln ? ', inln=' + inln : '')
		});
	}

	function u(key, width, inln, c1, int) {
		f(key, level0 + 1, 0, width, inln, c1, int)
	}

	function n(key, width, inln, c1, int) {
		f(key, level0, width0, width, inln, c1, int)
	}

	function samples(n) {
		return n === 1 ? '1 sample' : n.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ',') + ' samples';
	}

	function pct(a, b) {
		return a >= b ? '100' : (100 * a / b).toFixed(2);
	}

	function findFrame(frames, x) {
		let left = 0;
		let right = frames.length - 1;

		while (left <= right) {
			const mid = (left + right) >>> 1;
			const f = frames[mid];

			if (f.left > x) {
				right = mid - 1;
			} else if (f.left + f.width <= x) {
				left = mid + 1;
			} else {
				return f;
			}
		}

		if (frames[left] && (frames[left].left - x) * px < 0.5) return frames[left];
		if (frames[right] && (x - (frames[right].left + frames[right].width)) * px < 0.5) return frames[right];

		return null;
	}

	function removeStack(left, width) {
		for (let h = 0; h < levels.length; h++) {
			const frames = levels[h], newFrames = [];
			for (let i = 0; i < frames.length; i++) {
				const f = frames[i];
				if (f.left >= left + width) {
					f.left -= width;
				} else if (f.left + f.width > left) {
					if ((f.width -= width) <= 0 && h) continue;
				}
				newFrames.push(f);
			}
			levels[h] = newFrames;
		}
	}

	function search(r) {
		if (r === true && (r = prompt('Enter regexp to search:', '')) === null) {
			return;
		}

		pattern = r ? RegExp(r) : undefined;
		const matched = render(root, nav = []);
		navIndex = -1;
		document.getElementById('matchval').textContent = matchval = pct(matched, root.width) + '%';
		document.getElementById('match').style.display = r ? 'inline-block' : 'none';
	}

	function render(newRoot, nav) {
		if (root) {
			c.fillStyle = '#ffffff';
			c.fillRect(0, 0, canvasWidth, canvasHeight);
		}

		root = newRoot || levels[0][0];
		px = canvasWidth / root.width;

		const x0 = root.left;
		const x1 = x0 + root.width;
		const marked = [];

		function mark(f) {
			return marked[f.left] || (marked[f.left] = f);
		}

		function totalMarked() {
			let total = 0;
			let left = 0;
			Object.keys(marked).sort(function(a, b) { return a - b; }).forEach(function(x) {
				if (+x >= left) {
					const m = marked[x];
					if (nav) nav.push(m);
					total += m.width;
					left = +x + m.width;
				}
			});
			return total;
		}

		function drawFrame(f, y) {
			if (f.left < x1 && f.left + f.width > x0) {
				c.fillStyle = pattern && f.title.match(pattern) && mark(f) ? '#ee00ee' : f.color;
				c.fillRect((f.left - x0) * px, y, f.width * px, 15);

				if (f.width * px >= 21) {
					const chars = Math.floor(f.width * px / 7);
					const title = f.title.length <= chars ? f.title : f.title.substring(0, chars - 2) + '..';
					c.fillStyle = '#000000';
					c.fillText(title, Math.max(f.left - x0, 0) * px + 3, y + 12, f.width * px - 6);
				}

				if (f.level < root.level) {
					c.fillStyle = 'rgba(255, 255, 255, 0.5)';
					c.fillRect((f.left - x0) * px, y, f.width * px, 15);
				}
			}
		}

		for (let h = 0; h < levels.length; h++) {
			const y = inverted ? h * 16 : canvasHeight - (h + 1) * 16;
			const frames = levels[h];
			for (let i = 0; i < frames.length; i++) {
				drawFrame(frames[i], y);
			}
		}

		return totalMarked();
	}

	function unpack(cpool) {
		for (let i = 1; i < cpool.length; i++) {
			cpool[i] = cpool[i - 1].substring(0, cpool[i].charCodeAt(0) - 32) + cpool[i].substring(1);
		}
	}

	canvas.onmousemove = function() {
		const h = Math.floor((inverted ? event.offsetY : (canvasHeight - event.offsetY)) / 16);
		if (h >= 0 && h < levels.length) {
			const f = findFrame(levels[h], event.offsetX / px + root.left);
			if (f) {
				if (f !== root) getSelection().removeAllRanges();
				hl.style.left = (Math.max(f.left - root.left, 0) * px + canvas.offsetLeft) + 'px';
				hl.style.width = (Math.min(f.width, root.width) * px) + 'px';
				hl.style.top = ((inverted ? h * 16 : canvasHeight - (h + 1) * 16) + canvas.offsetTop) + 'px';
				hl.firstChild.textContent = f.title;
				hl.style.display = 'block';
				canvas.title = f.title + '\n(' + samples(f.width) + f.details + ', ' + pct(f.width, levels[0][0].width) + '%)';
				canvas.style.cursor = 'pointer';
				canvas.onclick = function() {
					if (event.altKey && h >= root.level && h > 0) {
						removeStack(f.left, f.width);
						root.width > f.width ? render(root) : render();
					} else if (f !== root) {
						render(f);
					}
					canvas.onmousemove();
				};
				status.textContent = 'Function: ' + canvas.title;
				status.style.display = 'inline-block';
				return;
			}
		}
		canvas.onmouseout();
	}

	canvas.onmouseout = function() {
		hl.style.display = 'none';
		status.style.display = 'none';
		canvas.title = '';
		canvas.style.cursor = '';
		canvas.onclick = null;
	}

	canvas.ondblclick = function() {
		getSelection().selectAllChildren(hl);
	}

	document.getElementById('inverted').onclick = function() {
		inverted = !inverted;
		render();
	}

	document.getElementById('search').onclick = function() {
		search(true);
	}

	document.getElementById('reset').onclick = function() {
		search(false);
	}

	const btnInfo = document.getElementById('info');
	const legend = document.getElementById('legend');

	btnInfo.onmouseover = function() {
		legend.style.left = (btnInfo.offsetLeft + 24) + 'px';
		legend.style.top = (btnInfo.offsetTop + 24) + 'px';
		legend.style.display = 'block';
	}

	btnInfo.onmouseout = function() {
		legend.style.display = 'none';
	}

	window.onkeydown = function(event) {
		if ((event.ctrlKey || event.metaKey) && event.key === 'f') {
			event.preventDefault();
			search(true);
			return false;
		} else if (event.key === 'Escape') {
			search(false);
		} else if ((event.key === 'n' || event.key === 'N') && nav.length > 0) {
			navIndex = (navIndex + (event.shiftKey ? nav.length - 1 : 1)) % nav.length;
			render(nav[navIndex]);
			document.getElementById('matchval').textContent = matchval + ' (' + (navIndex + 1) + ' of ' + nav.length + ')';
			window.scroll(0, inverted ? root.level * 16 : canvasHeight - (root.level + 1) * 16);
			canvas.onmousemove();
			return false;
		} else if (event.key === 'i') {
			canvas.onmouseout();
			document.getElementById('inverted').onclick();
			return false;
		} else if (event.key === '0') {
			canvas.onmouseout();
			root = levels[0][0];
			search(false);
			return false;
		}
	}

const cpool = [
/*cpool:*/
];
unpack(cpool);

/*frames:*/
search(/*highlight:*/);
</script></body></html>

```

## File: src\res\heatmap.html
```
<!DOCTYPE html>
<html lang='en'>
<head>
<meta charset='utf-8'>
<style>
	body {
		margin: 0;
		padding: 4px 8px 24px;
		background-color: #ffffff;
		overflow-y: scroll
	}
	h1 {
		margin: 5px 0 0 0;
		font-size: 18px;
		font-weight: normal;
		text-align: center
	}
	header {
		margin: -24px 0 5px 0;
		line-height: 24px
	}
	button {
		font: 12px sans-serif;
		cursor: pointer
	}
	p {
		margin: 5px 0 5px 0
	}
	a {
		color: #0366d6
	}
	#hl {
		position: absolute;
		display: none;
		overflow: hidden;
		white-space: nowrap;
		pointer-events: none;
		background-color: #ffffe0;
		outline: 1px solid #ffc000;
		height: 15px
	}
	#preview_wrapper {
		position: absolute;
		display: none;
		background-color: #ffffe0;
		outline: 1px solid #ffc000;
		pointer-events: none;
	}
	#hl span {
		padding: 0 3px 0 3px
	}
	#status {
		overflow: hidden;
		white-space: nowrap
	}
	#match {
		overflow: hidden;
		white-space: nowrap;
		display: none;
		float: right;
		text-align: right
	}
	#reset {
		cursor: pointer
	}
	#canvas {
		width: 100%;
		height: 300px;
	}
	.selectionPart {
		position: absolute;
		display: none;
		pointer-events: none;
		box-sizing: border-box;
	}
	.sel {
		background-color: #dada0040
	}
	.act {
		background-color: #00da0040
	}
	.dif {
		background-color: #00dada40
	}
	.top {
		border-top: .1px solid #000
	}
	.left {
		border-left: .1px solid #000
	}
	.bottom {
		border-bottom: .1px solid #000
	}
	.right {
		border-right: .1px solid #000
	}
	#info-tooltip {
		display: none;
		position: absolute;
		top: 10px;
		right: 48px;
		width: 204px;
		border: 1px solid #666666;
		background: #ffffe0;
		border-radius: 8px;
		padding: 4px
	}
	#heatmap-height-line {
		text-decoration: #0366d6 dashed underline;
		cursor: pointer;
		font-family: monospace
	}
	#heatmap-info {
		cursor: help
	}
	#heatmap-info:hover ~ #info-tooltip {
		display: block
	}
	.toolbarIcon {
		width: 24px;
		height: 24px;
		margin-top: 4px;
		margin-bottom: 4px;
		display: flex;
		justify-content: center;
		align-items: center;
	}
	.toolbarSelected {
		background-color: #cccccc;
		outline: 1px solid #999999;
		border-radius: 4px;
	}
	.toolbarIcon:hover {
		background-color: #ffffe0;
		outline: 1px solid #ffc000;
		border-radius: 4px;
	}
	.bordered {
		outline: 1px solid #999999;
	}
	.colortip {
		width: 100px;
		box-sizing: border-box;
		padding: 4px;
		background: linear-gradient(var(--c1), var(--c2))
	}
	.status {
		position: fixed;
		bottom: 0;
		padding: 2px 4px;
		background-color: #ffffe0;
		border-top: 1px solid #ffc000;
		border-left: 1px solid #ffc000;
		border-right: 1px solid #ffc000;
	}
</style>
</head>
<body style='font: 12px Verdana, sans-serif'>
<div class='bordered' style="display: flex">
	<div class='bordered' style="width: 20px; margin-right: 1px; padding: 2px; float: left; background-color: #efefef; writing-mode: vertical-rl; transform: scale(-1); text-align: center; user-select: none">
		<pre id="heatmap-height-line"> 1 sec : 20 ms </pre>
	</div>

	<div id='heatmap-canvas-container' style="width: 100%; position: relative" autofocus>
		<div id='heatmap-canvas-wrapper' style='overflow: hidden; width: 100%; font-size: 0; padding-bottom: 1px'>
			<canvas id='heatmap-canvas' style='height: 314px'></canvas>
		</div>

		<div id='middleActive' class='selectionPart top bottom act'><span></span></div>
		<div id='leftActive' class='selectionPart top left bottom act'><span></span></div>
		<div id='rightActive' class='selectionPart top right bottom act'><span></span></div>
		<div id='leftMiddleActive' class='selectionPart right'><span></span></div>
		<div id='rightMiddleActive' class='selectionPart left'><span></span></div>

		<div id='middleSelection' class='selectionPart top bottom sel'><span></span></div>
		<div id='leftSelection' class='selectionPart top left bottom sel'><span></span></div>
		<div id='rightSelection' class='selectionPart top right bottom sel'><span></span></div>
		<div id='leftMiddleSelection' class='selectionPart right'><span></span></div>
		<div id='rightMiddleSelection' class='selectionPart left'><span></span></div>

		<div id='middleDiff' class='selectionPart top bottom dif'><span></span></div>
		<div id='leftDiff' class='selectionPart top left bottom dif'><span></span></div>
		<div id='rightDiff' class='selectionPart top right bottom dif'><span></span></div>
		<div id='leftMiddleDiff' class='selectionPart right'><span></span></div>
		<div id='rightMiddleDiff' class='selectionPart left'><span></span></div>
	</div>

	<div class='bordered' style="user-select: none; background-color: #efefef; padding: 2px; margin-left: 1px">
		<div id="heatmap-info" class="toolbarIcon"><svg height="20px" width="20px" viewBox="0 0 392.598 392.598"><path style="fill:#FFFFFF;" d="M274.457,148.234c0.194,17.131-5.236,33.358-15.515,46.933c-23.984,32-36.784,68.331-36.784,104.921 v1.164h-51.911c-0.065-37.107-12.929-73.956-37.107-106.537c-12.735-15.386-17.455-32.065-15.321-49.842 c5.624-45.834,39.822-70.917,74.343-74.925C237.026,67.879,274.457,103.693,274.457,148.234z"></path><rect style="fill:#40b2ff;" x="170.311" y="323.038" width="51.846" height="47.774"></rect><path style="fill:#ff8d40;" d="M196.299,91.604c-0.905,0-1.939,0-2.844,0.065c-17.842,0.84-33.681,10.279-43.442,24.178h42.408 c6.012,0,10.925,4.848,10.925,10.925s-4.848,10.925-10.925,10.925h-51.588c-0.453,2.651-0.84,5.301-1.034,8.016 c-0.259,4.719,0.129,9.244,1.099,13.77h25.988c6.012,0,10.925,4.848,10.925,10.925c0,6.012-4.848,10.925-10.925,10.925h-16.356 c0.065,0.129,0.129,0.323,0.323,0.388c22.238,30.061,35.943,63.418,40.016,97.681h10.796c3.943-34.263,17.519-67.556,39.952-97.358 c7.37-9.826,11.313-21.463,11.313-33.875C252.865,117.075,227.523,91.604,196.299,91.604z"></path><path style="fill:#004d80;" d="M196.299,36.137c6.012,0,10.925-4.848,10.925-10.925V10.925C207.224,4.913,202.376,0,196.299,0 c-6.012,0-10.925,4.848-10.925,10.925v14.287C185.374,31.289,190.287,36.137,196.299,36.137z"></path> <path style="fill:#004d80;" d="M333.543,137.309h-14.287c-6.012,0-10.925,4.848-10.925,10.925c0,6.012,4.849,10.925,10.925,10.925 h14.287c6.012,0,10.925-4.848,10.925-10.925S339.556,137.309,333.543,137.309z"></path> <path style="fill:#004d80;" d="M73.277,137.309H59.055c-6.012,0-10.925,4.848-10.925,10.925c0,6.012,4.848,10.925,10.925,10.925 h14.287c6.012,0,10.925-4.848,10.925-10.925C84.202,142.158,79.289,137.309,73.277,137.309z"></path> <path style="fill:#004d80;" d="M285.64,43.507l-10.15,10.149c-4.267,4.267-4.267,11.119,0,15.45c4.267,4.267,11.119,4.267,15.451,0 l10.15-10.149c4.267-4.267,4.267-11.119,0-15.451C296.824,39.176,289.907,39.176,285.64,43.507z"></path> <path style="fill:#004d80;" d="M101.657,227.491l-10.085,10.02c-4.267,4.267-4.267,11.119,0,15.451 c4.267,4.331,11.119,4.267,15.451,0l10.02-10.02c4.267-4.267,4.267-11.119,0-15.451 C112.776,223.224,105.859,223.224,101.657,227.491z"></path> <path style="fill:#004d80;" d="M290.941,227.491c-4.267-4.267-11.119-4.267-15.451,0c-4.267,4.267-4.267,11.119,0,15.451 l10.15,10.149c4.267,4.267,11.119,4.267,15.451,0s4.267-11.119,0-15.451L290.941,227.491z"></path> <path style="fill:#004d80;" d="M101.657,68.978c4.267,4.267,11.119,4.267,15.451,0c4.267-4.267,4.267-11.119,0-15.451l-10.02-10.02 c-4.267-4.267-11.119-4.267-15.451,0c-4.267,4.267-4.267,11.119,0,15.451L101.657,68.978z"></path> <path style="fill:#004d80;" d="M191.257,48.097c-51.2,2.457-92.962,44.606-95.095,95.806c-1.034,23.208,5.818,45.188,19.523,63.741 c21.463,28.962,32.84,61.414,32.84,93.996v80.032c0,6.012,4.848,10.925,10.925,10.925h73.632c6.012,0,10.925-4.848,10.925-10.925 l0.065-81.584c0-31.935,11.184-63.677,32.388-91.798c13.123-17.455,20.04-38.141,20.04-60.057 C296.436,91.345,248.921,45.253,191.257,48.097z M222.093,370.812h-51.846v-47.774h51.846L222.093,370.812L222.093,370.812z M258.941,195.168c-23.984,32-36.784,68.331-36.784,104.921v1.164h-51.911c-0.065-37.107-12.929-73.956-37.107-106.537 c-12.735-15.386-17.455-32.065-15.321-49.842c5.624-45.834,39.822-70.917,74.343-74.925c44.865-2.069,82.295,33.745,82.295,78.287 C274.651,165.366,269.22,181.592,258.941,195.168z"></path></svg></div>
		<div id="search" class="toolbarIcon" title="Search by Regex [Ctrl + F]"><svg height="20px" width="20px" viewBox="-39.26 -39.26 471.13 471.13" xml:space="preserve" fill="#000000" stroke="#000000" stroke-width="0.00392609"><path style="fill:#FFFFFF;" d="M273.713,147.774c0,69.495-56.501,125.931-125.931,125.931c-69.495,0-125.931-56.501-125.931-125.931 c0-69.495,56.501-125.931,125.931-125.931C217.212,21.843,273.713,78.344,273.713,147.774z"></path><path style="fill:#40b2ff;" d="M370.747,348.695c0,1.422-1.616,6.271-7.176,12.283c-6.206,6.659-12.477,9.762-14.739,9.762h-0.065 c-19.459-1.616-61.996-43.184-109.576-106.796c0-0.065,0-0.065,0-0.129c9.18-7.24,17.455-15.515,24.63-24.63 c0.065,0,0.065,0,0.129,0C327.564,286.699,369.131,329.301,370.747,348.695z"></path><path style="fill:#ff8d40;" d="M208.679,86.877l-14.481,14.481c-17.131,17.131-46.545,5.042-46.545-19.265V61.6 c-49.002,0-88.372,40.792-86.109,90.246c2.004,43.895,38.141,80.032,82.036,82.036c49.455,2.263,90.246-37.172,90.246-86.109 C233.956,124.049,224.323,102.522,208.679,86.877z"></path><path style="fill:#004d80;" d="M276.105,220.954c12.347-21.527,19.459-46.545,19.459-73.18c0-81.455-66.327-147.717-147.846-147.717 S0,66.32,0,147.904s66.327,147.717,147.717,147.717c26.57,0,51.523-7.111,73.18-19.459 c39.822,53.333,91.863,113.519,126.061,116.364c12.283,0.517,22.885-6.723,32.776-16.743c5.172-5.624,13.77-16.937,12.8-28.768 C389.624,312.881,329.438,260.776,276.105,220.954z M147.717,273.77c-69.495,0-125.931-56.501-125.931-125.931 S78.287,21.908,147.717,21.908s125.931,56.501,125.931,125.931S217.212,273.77,147.717,273.77z M363.572,360.978 c-6.206,6.659-12.412,9.762-14.739,9.762h-0.065c-19.459-1.616-61.996-43.184-109.576-106.796c0-0.065,0-0.065,0-0.129 c9.18-7.24,17.455-15.515,24.63-24.63c0.065,0,0.065,0,0.129,0c63.612,47.58,105.18,90.182,106.796,109.576 C370.747,350.118,369.131,354.966,363.572,360.978z"></path></svg></div>
		<div id="filter" class="toolbarIcon" title="Filter by Regex [Shift + Ctrl + F]"><svg height="16px" width="16px" viewBox="0 0 392.541 392.541"><path style="fill:#FFFFFF;" d="M219.345,344.911V190.988c0-2.909,1.164-5.689,3.232-7.758L367.386,39.586 c3.814-3.814,3.426-7.434,2.392-9.891c-1.487-3.62-6.012-7.887-13.834-7.887H36.137c-7.822,0-12.347,4.267-13.834,7.887 c-1.034,2.392-1.422,6.077,2.392,9.891L169.503,183.23c2.069,2.004,3.232,4.848,3.232,7.758v174.093L219.345,344.911z"></path><path style="fill:#40b2ff;" d="M59.733,43.594L91.41,75.012c0.065,0,0.259,0,0.323,0h97.228c6.012,0,10.925,4.848,10.925,10.925 c0,6.012-4.848,10.925-10.925,10.925h-75.636l22.044,21.786h31.741c6.012,0,10.925,4.848,10.925,10.925 c0,6.012-4.848,10.925-10.925,10.925h-9.826l38.853,38.335l136.21-135.176L59.733,43.594L59.733,43.594z"></path><path style="fill:#004d80;" d="M356.008,0.022H36.137c-30.578,0-47.968,33.487-26.828,55.079l141.705,140.412v186.053 c0.065,7.111,7.564,13.382,15.192,10.02l68.396-29.543c4.008-1.681,6.594-5.624,6.594-10.02V195.513l141.64-140.412 C404.234,33.767,388.008,0.022,356.008,0.022z M367.45,39.586L222.642,183.23c-2.069,2.004-3.232,4.848-3.232,7.758v153.923 l-46.61,20.105V190.988c0-2.909-1.164-5.689-3.232-7.758L24.759,39.586c-8.339-8.792,1.099-18.295,11.442-17.778h319.806 C367.45,21.485,375.337,32.41,367.45,39.586z"></path></svg></div>
		<div id="flame-diff-reverse" class="toolbarIcon" title="Reverse Diff [Ctrl + R]"><svg height="16px" width="16px" viewBox="0 0 392.598 392.598"><path style="fill:#004d80;" d="M382.488,286.384c-3.62-3.62-9.438-4.267-13.77-1.422c-30.19,20.105-65.552,30.707-102.077,30.707 c-45.64,0-88.76-16.485-122.634-46.61l23.725-23.725c7.37-8.21,1.487-18.166-7.758-18.618H40.96 c-6.012,0-10.925,4.848-10.925,10.925v118.95c0.517,10.279,12.024,14.222,18.618,7.758l24.76-24.76 c37.947,34.263,86.626,53.01,138.085,53.01c55.143,0,125.285-23.014,172.154-92.444 C386.69,295.822,386.108,290.069,382.488,286.384z M211.692,370.747c-49.325,0-95.741-19.265-130.586-54.109 c-4.073-4.073-11.378-4.073-15.451,0L51.95,330.343v-81.842h81.778l-13.059,13.059c-4.202,4.59-4.461,10.99,0,15.451 c39.046,39.047,90.893,60.509,146.036,60.509c21.85,0,43.378-3.426,63.806-10.02C297.219,355.426,255.651,370.747,211.692,370.747z "></path><path style="fill:#004d80;" d="M248.605,123.475L224.88,147.2c-7.37,8.21-1.487,18.166,7.758,18.618h119.014 c6.012,0,10.925-4.848,10.925-10.925V35.943c-0.517-10.279-12.024-14.222-18.618-7.758l-24.76,24.76 C281.122,18.683,232.508,0,180.985,0C125.841,0,55.829,23.014,8.831,92.444c-2.909,4.331-2.327,10.02,1.422,13.77 c3.62,3.62,9.438,4.267,13.77,1.422C54.213,87.531,89.575,76.929,126.1,76.929C171.611,76.865,214.795,93.349,248.605,123.475z M180.92,21.786c49.325,0,95.741,19.265,130.586,54.109c4.073,4.073,11.378,4.073,15.451,0l13.705-13.705v81.778h-81.778 l13.059-13.059c4.202-4.59,4.461-10.99,0-15.451c-39.046-39.046-90.893-60.509-146.036-60.509c-21.851,0-43.378,3.426-63.806,10.02 C95.393,37.107,136.96,21.786,180.92,21.786z"></path><path style="fill:#ff8d40;" d="M340.661,62.255L326.956,75.96c-4.073,4.073-11.378,4.073-15.451,0 c-34.844-34.844-81.261-54.109-130.586-54.109c-43.96,0-85.592,15.192-118.82,43.248c20.428-6.659,41.891-10.02,63.806-10.02 c55.143,0,107.055,21.463,146.036,60.509c4.461,4.396,4.202,10.796,0,15.451l-13.059,12.994h81.778L340.661,62.255L340.661,62.255z"></path><path style="fill:#40b2ff;" d="M81.041,316.638c34.844,34.844,81.261,54.109,130.586,54.109c43.96,0,85.592-15.192,118.82-43.249 c-20.428,6.659-41.891,10.02-63.806,10.02c-55.143,0-107.055-21.463-146.036-60.509c-4.461-4.396-4.202-10.796,0-15.451 l13.059-13.059H51.95v81.778l13.705-13.705C69.728,312.566,76.968,312.566,81.041,316.638z"></path></svg></div>

		<div id="flame-mode-flame" class="toolbarIcon toolbarSelected" style="margin-top: 16px" title="FlameGraph [Ctrl + 1]">
			<svg height="20px" width="20px" viewBox="0 0 20 20"><rect x="0" y="0" style="fill:#ff8d40;" width="20" height="4"></rect><rect x="0" y="5" style="fill:#40b2ff;" width="10" height="4"></rect><rect x="11" y="5" style="fill:#ff8d40;" width="8" height="4"></rect><rect x="0" y="10" style="fill:#40b2ff;" width="8" height="4"></rect><rect x="11" y="10" style="fill:#ff8d40;" width="4" height="4"></rect><rect x="0" y="15" style="fill:#40b2ff;" width="4" height="4"></rect><rect x="5" y="15" style="fill:#ff8d40;" width="2" height="4"></rect></svg>
		</div>
		<div id="flame-mode-reversed" class="toolbarIcon" title="Reversed FlameGraph [Ctrl + 2]">
			<svg height="20px" width="20px" viewBox="0 0 20 20"><rect x="0" y="0" style="fill:#ff8d40;" width="6" height="4"></rect><rect x="7" y="0" style="fill:#ff8d40;" width="5" height="4"></rect><rect x="13" y="0" style="fill:#ff8d40;" width="4" height="4"></rect><rect x="18" y="0" style="fill:#ff8d40;" width="2" height="4"></rect><rect x="0" y="5" style="fill:#ff8d40;" width="6" height="4"></rect><rect x="7" y="5" style="fill:#40b2ff;" width="5" height="4"></rect><rect x="13" y="5" style="fill:#ff8d40;" width="4" height="4"></rect><rect x="18" y="5" style="fill:#40b2ff;" width="2" height="4"></rect><rect x="0" y="10" style="fill:#ff8d40;" width="4" height="4"></rect><rect x="7" y="10" style="fill:#40b2ff;" width="2" height="4"></rect><rect x="13" y="10" style="fill:#40b2ff;" width="4" height="4"></rect><rect x="13" y="15" style="fill:#ff8d40;" width="2" height="4"></rect></svg>
		</div>
		<div id="flame-mode-methods" class="toolbarIcon" title="Methods List [Ctrl + 3]">
			<svg height="20px" width="20px" viewBox="0 0 20 20"><rect x="0" y="0" style="fill:#ff8d40;" width="20" height="4"></rect><rect x="0" y="5" style="fill:#40b2ff;" width="16" height="4"></rect><rect x="0" y="10" style="fill:#ff8d40;" width="8" height="4"></rect><rect x="0" y="15" style="fill:#40b2ff;" width="4" height="4"></rect></svg>
		</div>

		<div id="info-tooltip">
			<div style="float:left">
				<div style="padding: 4px;">Frame types:</div>
				<div class="colortip" style="--c1:#b2e1b2;--c2:#c6f5c6">Interpreted</div>
				<div class="colortip" style="--c1:#50e150;--c2:#6eff6e">JIT-Compiled</div>
				<div class="colortip" style="--c1:#50cccc;--c2:#6eeaea">Inlined</div>
				<div class="colortip" style="--c1:#e15a5a;--c2:#ff8282">Native</div>
				<div class="colortip" style="--c1:#c8c83c;--c2:#e6e646">C++</div>
				<div class="colortip" style="--c1:#e17d00;--c2:#ff9b00">Kernel</div>
				<div class="colortip" style="--c1:#cce880;--c2:#e0fc94">C1-Compiled</div>
			</div>
			<div style="float:left; margin-left: 4px">
				<div style="padding: 4px;">Special colors:</div>
				<div class="colortip" style="--c1:#40b2ff;--c2:#40b2ff">Matches regexp</div>
				<div class="colortip" style="--c1:#ffdd33;--c2:#ffdd33">New frames</div>
				<div class="colortip" style="--c1:#66e0f0;--c2:#66e0f0">Same frames</div>
				<div class="colortip" style="--c1:#42ff8e;--c2:#ccffe0">Less frames</div>
				<div class="colortip" style="--c1:#ff8d40;--c2:#ffe0cc">More frames</div>
			</div>
			<div style="float:left; margin-top: 4px; width: 100%; border: 1px solid #666666; border-radius: 2px; padding: 2px; box-sizing: border-box;">
				Shift + Click - Select range<br>
				Ctrl + Click - Compare<br>
				<br>
				Ctrl + F - Search<br>
				Shift + Ctrl + F - Filter<br>
				Ctrl + R - Switch Diff<br>
				<br>
				Ctrl + 1 - Select FlameGraph mode<br>
				Ctrl + 2 - Select Reversed FlameGraph mode<br>
				Ctrl + 3 - Select Methods List mode<br>
			</div>
		</div>
	</div>
</div>
<div style="display:none">
	<pre id="executionsHeatmap">/*executionsHeatmap:*/</pre>
</div>
<div style="display:none">
	<pre id="methods">/*methods:*/</pre>
</div>
<span class="status" style="border-right: none; border-top-left-radius: 4px; right:0;">
	<span id="produced">Produced by <a href='https://github.com/async-profiler/async-profiler'>async-profiler</a>&nbsp;</span>
	<span id='match' style="display: none">Matched: <span id='matchval'></span>&nbsp;<span id='reset' title='Clear'>&#x274c;</span></span>
</span>
<h1 id="title">/*title:*/</h1>
<canvas id='canvas'></canvas>
<div id='hl'><span></span></div>
<div id='preview_wrapper'><canvas id='preview'></canvas></div>

<span id='status' class="status" style="border-left: none; border-top-right-radius: 4px; display: none; left:0;">&nbsp;</span>
<script>
	// Copyright The async-profiler authors
	// SPDX-License-Identifier: Apache-2.0
	'use strict';

	let dR, dG, dB;
	let dRs, dGs, dBs;
	let dRdg, dGdg, dBdg;
	let dRdl, dGdl, dBdl;

	function setH(H) {
		const dX = Math.round(256 - Math.abs(H % 2 - 1) * 256);
		switch (H | 0) {
			case 0:
				dR = 256; dG = dX; dB = 0;
				break;
			case 1:
				dR = dX; dG = 256; dB = 0;
				break;
			case 2:
				dR = 0; dG = 256; dB = dX;
				break;
			case 3:
				dR = 0; dG = dX; dB = 256;
				break;
			case 4:
				dR = dX; dG = 0; dB = 256;
				break;
			case 5:
				dR = 256; dG = 0; dB = dX;
				break;
		}
	}

	setH(0.4);

	dRdg = dR;
	dGdg = dG;
	dBdg = dB;

	setH(2.4);

	dRdl = dR;
	dGdl = dG;
	dBdl = dB;

	setH(3.4);

	dRs = dR;
	dGs = dG;
	dBs = dB;

	setH(0.4);

	let root, rootLevel, px, pattern;
	let showFound = false;
	let filterFrames = false;
	const levels = [];

	const canvas = document.getElementById('canvas');
	let c = canvas.getContext('2d');
	const hl = document.getElementById('hl');
	const preview_wrapper = document.getElementById('preview_wrapper')
	const status = document.getElementById('status');

	const canvasWidth = canvas.offsetWidth;
	let canvasHeight = canvas.offsetHeight;
	canvas.style.width = canvasWidth + 'px';
	canvas.width = canvasWidth * (devicePixelRatio || 1);
	canvas.height = canvasHeight * (devicePixelRatio || 1);
	if (devicePixelRatio) c.scale(devicePixelRatio, devicePixelRatio);
	c.font = document.body.style.font;

	let lastRenderFrom = 0;
	let lastRenderTo = 0;
	let lastBaseRenderFrom = 0;
	let lastBaseRenderTo = 0;
	let renderFunc = renderSelfDominators;
	let renderFuncDiff = renderTracesDiff;

	for (let mode of ['flame-mode-flame', 'flame-mode-reversed', 'flame-mode-methods']) {
		document.getElementById(mode).onclick = () => {
			selectMode(mode);
		};
	}

	document.getElementById('flame-diff-reverse').onclick = () => {
		if (heatDiffSample1 !== -1) {
			renderWrapperDiff(lastBaseRenderFrom, lastBaseRenderTo, lastRenderFrom, lastRenderTo);
		}
	};

	document.getElementById('search').onclick = () => {
		search(true);
	};

	document.getElementById('filter').onclick = () => {
		search(true, true);
	};

	const palette = [
		[0xb2e1b2, 20, 20, 20],
		[0x20d120, 50, 45, 50],
		[0x50cccc, 30, 30, 30],
		[0xe15a5a, 30, 40, 40],
		[0xc8c83c, 30, 30, 10],
		[0xe17d00, 30, 30, 0],
		[0xcce880, 20, 20, 20]
	];

	function getColorStable(p, i) {
		i = Math.imul(i, 0xcc9e2d51);
		i = Math.imul((i << 15) | (i >> 17), 0x1b873593) >>> 24;

		const v1 = (p[1] * i) >>> 8;
		const v2 = (p[2] * i) >>> 8;
		const v3 = (p[3] * i) >>> 8;
		return '#' + (p[0] + (v1 << 16 | v2 << 8 | v3)).toString(16);
	}

	function samples(n) {
		return n === 1 ? '1 sample' : n.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ',') + ' samples';
	}

	function pct(a, b) {
		return a >= b ? '100' : (100 * a / b).toFixed(2);
	}

	function findFrameIndex(frames, x) {
		let left = 0;
		let right = frames.length - 1;

		while (left <= right) {
			const mid = (left + right) >>> 1;
			const f = frames[mid];

			if (f.left > x) {
				right = mid - 1;
			} else if (f.left + f.width <= x) {
				left = mid + 1;
			} else {
				return mid;
			}
		}

		if (frames[left] && (frames[left].left - x) * px < 0.5) return left;
		if (frames[right] && (x - (frames[right].left + frames[right].width)) * px < 0.5) return right;

		return -1;
	}

	function findFramesBetween(frames, xFrom, xTo) {
		const result = [];
		let left = 0;
		let right = frames.length - 1;

		while (left <= right) {
			const mid = (left + right) >>> 1;
			const f = frames[mid];

			if (f.left > xFrom) {
				right = mid - 1;
			} else if (f.left + f.width <= xFrom) {
				left = mid + 1;
			} else {
				left = mid;
				break;
			}
		}
		for (let i = left; i < frames.length; i++) {
			const f = frames[i];
			if (f.left > xTo) {
				break;
			}
			result.push(f);
		}

		return result;
	}

	function findFrame(frames, x) {
		const index = findFrameIndex(frames, x);
		if (index === -1) {
			return null;
		}
		return frames[index];
	}

	function findNextFrame(frames, x) {
		const index = findFrameIndex(frames, x) + 1;
		if (index === 0 || index >= frames.length) {
			return null;
		}
		return frames[index];
	}

	function findPrevFame(frames, x) {
		const index = findFrameIndex(frames, x) - 1;
		if (index < 0) {
			return null;
		}
		return frames[index];
	}

	const marked = [];

	function render(newRoot, newLevel, minLevel) {
		minLevel = minLevel || 0;
		if (root && minLevel === 0) {
			c.fillStyle = '#ffffff';
			c.fillRect(0, 0, canvasWidth, canvasHeight);
		}

		root = newRoot || levels[0][0];
		rootLevel = newLevel || 0;
		px = canvasWidth / root.width;

		const x0 = root.left;
		const x1 = x0 + root.width;

		if (minLevel === 0) {
			marked.length = 0;
		}

		function mark(f) {
			return marked[f.left] >= f.width || (marked[f.left] = f.width);
		}

		function totalMarked() {
			let total = 0;
			let left = 0;
			Object.keys(marked).sort(function (a, b) {
				return a - b;
			}).forEach(function (x) {
				if (+x >= left) {
					total += marked[x];
					left = +x + marked[x];
				}
			});
			return total;
		}

		function drawFrame(f, y, alpha) {
			if (f.left < x1 && f.left + f.width > x0) {
				let match = showFound && pattern(f.method) && mark(f);
				const fw = f.width * px;
				if (fw < 0.1) {
					return;
				}
				c.fillStyle = match ? '#40b2ff' : f.color;
				c.fillRect((f.left - x0) * px, y, fw, 15);
				if (fw >= 21) {
					const chars = Math.floor(fw / 7);
					const title = f.title.length <= chars ? f.title : f.title.substring(0, chars - 2) + '..';
					c.fillStyle = '#000000';
					c.fillText(title, Math.max(f.left - x0, 0) * px + 3, y + 12, fw - 6);
				}

				if (alpha) {
					c.fillStyle = 'rgba(255, 255, 255, 0.25)';
					c.fillRect((f.left - x0) * px, y, fw, 15);
				}
			}
		}

		for (let h = minLevel; h < levels.length; h++) {
			const y = h * 16;
			const frames = levels[h];
			for (let f of frames) {
				drawFrame(f, y, h < rootLevel);
			}
		}

		return totalMarked();
	}

	let previewX = -1;
	let previewY = -1;

	function showPreview() {

		const w = 500;
		const h = 15 * 16;
		const s = 50;
		const dx = w / s / 2;

		preview_wrapper.style.left = (canvas.offsetLeft + Math.max(0, previewX - w - 8) - 4) + 'px';
		preview_wrapper.style.top = (previewY + canvas.offsetTop - h - 16) + 'px';
		preview_wrapper.style.display = 'block';

		let xFrom = (previewX - dx) / px + root.left;
		let xTo = (previewX + dx) / px + root.left;
		if (xFrom < 0) {
			xTo -= xFrom;
			xFrom = 0;
		}
		const preview = document.getElementById('preview');
		preview.style.width = w + "px"
		preview.style.height = h + "px";
		preview.width = w * (devicePixelRatio || 1);
		preview.height = h * (devicePixelRatio || 1);
		const c = preview.getContext('2d');
		if (devicePixelRatio) c.scale(devicePixelRatio, devicePixelRatio);
		c.font = document.body.style.font;
		c.fillStyle = '#ffffff';
		c.fillRect(0, 0, w, h);
		for (let i = 0; i < 15; i++) {
			const level = Math.floor(previewY / 16) + i - 7;
			if (level < 0 || level >= levels.length) {
				continue;
			}
			const frames = findFramesBetween(levels[level], xFrom, xTo);
			const x0 = xFrom;
			for (let f of frames) {
				const fw = f.width * s * px;
				c.fillStyle = f.color;
				c.fillRect((f.left - x0) * s * px, i * 16, fw, 15);
				if (fw >= 21) {
					const chars = Math.floor(fw / 7);
					const title = f.title.length <= chars ? f.title : f.title.substring(0, chars - 2) + '..';
					c.fillStyle = '#000000';
					c.fillText(title, (f.left - x0) * s * px + 3, i * 16 + 12, fw - 6);
				}
			}
		}
		c.strokeRect(0, 7 * 16, w, 16);
	}

	canvas.onmousemove = function (e) {
		previewX = e.offsetX;
		previewY = e.offsetY;
		if (e.shiftKey) {
			showPreview();
		} else {
			preview_wrapper.style.display = 'none';
		}

		const h = Math.floor(e.offsetY / 16);
		if (h >= 0 && h < levels.length) {
			const f = findFrame(levels[h], e.offsetX / px + root.left);
			if (f) {
				hl.style.left = (Math.max(f.left - root.left, 0) * px + canvas.offsetLeft) + 'px';
				hl.style.width = (Math.min(f.width, root.width) * px) + 'px';
				hl.style.top = (h * 16 + canvas.offsetTop) + 'px';
				hl.firstChild.textContent = f.title;
				hl.style.display = 'block';
				let details = f.details || '';
				canvas.title = f.title + '\n(' + samples(f.width) + details + ', ' + pct(f.width, levels[0][0].width) + '%)';
				canvas.style.cursor = 'pointer';
				canvas.onclick = function (e) {
					if (e.shiftKey) {
						e.preventDefault();
						searchForMethod(f.method);
						canvas.onmousemove(e);
						return;
					}

					if (e.ctrlKey) {
						const n = e.shiftKey ? findPrevFame(levels[h], e.offsetX / px + root.left) : findNextFrame(levels[h], e.offsetX / px + root.left);
						if (n) {
							render(n, h);
						}
						canvas.onmousemove(e);
						return;
					}

					if (f !== root) {
						render(f, h);
						canvas.onmousemove(e);
					}
				};
				status.textContent = 'Function: ' + canvas.title;
				status.style.display = 'inline';
				return;
			}
		}
		canvas.onmouseout();
	}

	canvas.onmouseout = function (e) {
		hl.style.display = 'none';
		status.textContent = '\xa0';
		status.style.display = 'none';
		canvas.title = '';
		canvas.style.cursor = '';
		canvas.onclick = '';
		if (e !== undefined) {
			preview_wrapper.style.display = 'none';
			previewX = previewY = -1;
		}
	}

	document.getElementById('reset').onclick = function () {
		search(false);
	}

	class DataBuffer {
		data;
		pos = 1;

		constructor(encodedData) {
			this.data = encodedData;
		}

		nextVarInt() {
			let res = 0;
			let shift = 1;
			let b;
			do {
				b = this.byteAt(this.pos++);
				res += (b % 61) * shift;
				shift *= 61;
			} while (b >= 61);
			return res;
		}

		nextBase123() {
			return (Math.imul(this.byteAt(this.pos++), 1860867)	// 123^3
				+ Math.imul(this.byteAt(this.pos++), 15129)     // 123^2
				+ Math.imul(this.byteAt(this.pos++), 123)       // 123^1
				+ this.byteAt(this.pos++)) | 0;                 // 123^0
		}

		byteAt(pos) {
			const c = this.data.charCodeAt(pos);
			switch (c) {
				case 127:
					return 0;
				case 126:
					return 13;
				case 125:
					return 38;
				case 124:
					return 60;
				case 123:
					return 62;
			}
			return c;
		}

		nextInt6() {
			return this.byteAt(this.pos++);
		}

		nextInt18() {
			return this.nextInt6() | this.nextInt6() << 6 | this.nextInt6() << 12;
		}

		int30(pos) {
			let p = pos * 5;
			if (p < 0) {
				p += this.data.length - 1;
			}
			return this.byteAt(p++) << 0
				| this.byteAt(p++) << 6
				| this.byteAt(p++) << 12
				| this.byteAt(p++) << 18
				| this.byteAt(p++) << 24;
		}
	}

	function decodeExecutions(data) {
		const samplesCount = data.int30(-1);
		const chunksCount = data.int30(-2);
		const storageSize = data.int30(-3);
		const blocksCount = data.int30(-4);
		const lz78RecordsCount = data.int30(-5);

		const starts = new Set();
		const startMethodsCount = data.nextVarInt();
		for (let i = 0; i < startMethodsCount; i++) {
			starts.add(data.nextVarInt());
		}

		// NOTE: All dynamic allocations should be done before this line
		const buffer = new ArrayBuffer((4 + 4 + 4 + 4 + 4) * lz78RecordsCount);
		const lz78RootMethods = new Uint32Array(buffer, 0, lz78RecordsCount);
		const lz78CurrentMethods = new Uint32Array(buffer, lz78RecordsCount * 4, lz78RecordsCount);
		const lz78Parents = new Uint32Array(buffer, lz78RecordsCount * 8, lz78RecordsCount);
		const lz78Sizes = new Uint32Array(buffer, lz78RecordsCount * 12, lz78RecordsCount);
		const lz78Refs = new Uint32Array(buffer, lz78RecordsCount * 16, lz78RecordsCount);

		const storageMarksIntsCount = (storageSize >> 5) + 1;
		const sampleMarksIntsCount = (samplesCount >> 5) + 1;
		const returnBuffer = new ArrayBuffer(4 * samplesCount + 4 * chunksCount + 8 * storageSize + 8 * blocksCount + 16 * zoomToGroupSize.length + 4 * storageMarksIntsCount + 4 * sampleMarksIntsCount);
		const sampleToChunkEnds = new Uint32Array(returnBuffer, 0, samplesCount);
		const chunksToStorage = new Uint32Array(returnBuffer, 4 * samplesCount, chunksCount);
		const storage = new Uint32Array(returnBuffer, 4 * samplesCount + 4 * chunksCount, storageSize);
		const storageSizes = new Uint32Array(returnBuffer, 4 * samplesCount + 4 * chunksCount + 4 * storageSize, storageSize);
		const counts = new Int32Array(returnBuffer, 4 * samplesCount + 4 * chunksCount + 8 * storageSize, blocksCount);
		const foundCounts = new Int32Array(returnBuffer, 4 * samplesCount + 4 * chunksCount + 8 * storageSize + 4 * blocksCount, blocksCount);
		const maxCounts = new Uint32Array(returnBuffer, 4 * samplesCount + 4 * chunksCount + 8 * storageSize + 8 * blocksCount, zoomToGroupSize.length);
		const searchMaxCounts = new Uint32Array(returnBuffer, 4 * samplesCount + 4 * chunksCount + 8 * storageSize + 8 * blocksCount + 4 * zoomToGroupSize.length, zoomToGroupSize.length);
		const minCounts = new Uint32Array(returnBuffer, 4 * samplesCount + 4 * chunksCount + 8 * storageSize + 8 * blocksCount + 8 * zoomToGroupSize.length, zoomToGroupSize.length);
		const searchMinCounts = new Uint32Array(returnBuffer, 4 * samplesCount + 4 * chunksCount + 8 * storageSize + 8 * blocksCount + 12 * zoomToGroupSize.length, zoomToGroupSize.length);
		const marks = new Uint32Array(returnBuffer, 4 * samplesCount + 4 * chunksCount + 8 * storageSize + 8 * blocksCount + 16 * zoomToGroupSize.length, storageMarksIntsCount);
		const sampleMarks = new Uint32Array(returnBuffer, 4 * samplesCount + 4 * chunksCount + 8 * storageSize + 8 * blocksCount + 16 * zoomToGroupSize.length + 4 * storageMarksIntsCount, sampleMarksIntsCount);

		const huffmanTableSize = data.nextVarInt();
		const huffmanMaxBits = data.nextVarInt();

		const huffmanValues = new Uint32Array(huffmanTableSize);
		const huffmanCounts = new Uint32Array(huffmanMaxBits + 1);
		for (let i = 0; i < huffmanTableSize; i++) {
			huffmanValues[i] = data.nextVarInt();
			huffmanCounts[data.nextVarInt()]++;
		}

		if (huffmanMaxBits === 0) {
			counts.fill(huffmanValues[0]);
		} else {
			let firstHuffmanCodeForCount = 0;
			let currentHuffmanCode = 0;
			let currentCountPos = 1;
			let valuesPos = 0;

			let block = 0;
			a:while (true) {
				let bits = data.nextBase123();

				for (let i = 0; i < 27; i++) {      // 27 bits per symbol
					currentHuffmanCode |= bits & 1;
					bits >>>= 1;
					let count = huffmanCounts[currentCountPos];

					let nextHuffmanCodeForCount = firstHuffmanCodeForCount + count;
					if (nextHuffmanCodeForCount > currentHuffmanCode) {
						counts[block] = huffmanValues[valuesPos + currentHuffmanCode - firstHuffmanCodeForCount];
						if (++block >= blocksCount) {
							break a;
						}
						firstHuffmanCodeForCount = 0;
						currentHuffmanCode = 0;
						currentCountPos = 1;
						valuesPos = 0;
					} else {
						firstHuffmanCodeForCount = nextHuffmanCodeForCount << 1;
						currentHuffmanCode <<= 1;
						currentCountPos++;
						valuesPos += count;
					}
				}
			}
		}

		let synonymsCount = data.nextVarInt();
		const synonyms = new Uint32Array(synonymsCount);
		for (let i = 0; i < synonymsCount; i++) {
			synonyms[i] = data.nextVarInt();
		}

		let totalCount = 0;
		for (let c = 0; c < counts.length; c++) {
			totalCount += counts[c];
			counts[c] = totalCount;
		}

		calculateMinMax(counts, minCounts, maxCounts);

		for (let recordId = 1; recordId < lz78RecordsCount; recordId++) {
			const prevChunkId = data.nextVarInt();
			const addMethodId = data.nextVarInt();

			const lzPrevRecordId = (prevChunkId < synonymsCount ? synonyms[prevChunkId] : prevChunkId) - synonymsCount;

			// 0 bit for starts, 1 bit for leafs
			const prevFlags = lz78RootMethods[lzPrevRecordId];
			lz78RootMethods[lzPrevRecordId] = prevFlags & 1;   // not a leaf anymore
			lz78RootMethods[recordId] = lzPrevRecordId === 0
				? (starts.has(addMethodId) ? 3 : 2)
				: (prevFlags | 2);  // leaf for now

			lz78CurrentMethods[recordId] = addMethodId;
			lz78Parents[recordId] = lzPrevRecordId;
			lz78Sizes[recordId] = lz78Sizes[lzPrevRecordId] + 1;
		}

		let pos = 0;
		for (let rid = 1; rid < lz78RecordsCount; rid++) {
			const flags = lz78RootMethods[rid];
			if (flags & 2) {    // leaf
				const storagePos = lz78Refs[rid];
				if (storagePos === 0) {
					let recordId = rid;
					let size = lz78Sizes[recordId];
					do {
						storageSizes[pos] = size--;
						storage[pos] = lz78CurrentMethods[recordId];
						pos++;
						lz78Refs[recordId] = pos;
						recordId = lz78Parents[recordId];
					} while (recordId !== 0 && lz78Refs[recordId] === 0);

					while (recordId !== 0) {
						storageSizes[pos] = size--;
						storage[pos] = lz78CurrentMethods[recordId];
						pos++;
						recordId = lz78Parents[recordId];
					}
				}
			}
		}

		synonymsCount = data.nextVarInt();
		for (let i = 0; i < synonymsCount; i++) {
			synonyms[i] = data.nextVarInt();
		}

		let sample = 0;
		for (let chunk = 0; chunk < chunksCount; chunk++) {
			const chunkId = data.nextVarInt();
			let recordId = (chunkId < synonymsCount ? synonyms[chunkId] : chunkId) - synonymsCount;
			const flags = lz78RootMethods[recordId];
			chunksToStorage[chunk] = recordId;
			if (flags & 1) {    // start of the next sample
				if (sample !== 0) {
					sampleToChunkEnds[sample - 1] = chunk;
				}
				sample++;
			}
		}
		if (pos > storage.length) {
			throw "storage is too low";
		}
		sampleToChunkEnds[sample - 1] = chunksCount;

		for (let chunk = 0; chunk < chunksCount; chunk++) {
			const recordId = chunksToStorage[chunk];
			if (lz78Refs[recordId] === 0) {
				throw recordId + " has no storagePos";
			}
			chunksToStorage[chunk] = lz78Refs[recordId] - 1;
		}

		return {
			sampleToChunkEnds: sampleToChunkEnds,
			chunksToStorage: chunksToStorage,
			storage: storage,
			storageSizes: storageSizes,
			counts: counts,
			foundCounts: foundCounts,
			maxCounts: maxCounts,
			searchMaxCounts: searchMaxCounts,
			minCounts: minCounts,
			searchMinCounts: searchMinCounts,
			marks: marks,
			sampleMarks: sampleMarks,
		};
	}

	class HeatmapCollection extends DataBuffer {

		minimalTimeSquare = 20; // hardcoded for now
		squaresBetweenMarks = 20; // hardcoded forever)

		zoom;
		timeSquareScale;
		timeSquareRowsCount;

		blocksData;

		constructor(encodedData) {
			super(encodedData);

			this.blocksData = decodeExecutions(this);
			this.data = undefined;
		}

		currentTimeSquareMs() {
			return this.minimalTimeSquare * this.timeSquareScale;
		}

		startBlock() {
			const timeSquareMs = this.currentTimeSquareMs();
			const timeBlockMs = timeSquareMs * this.timeSquareRowsCount * this.squaresBetweenMarks;
			return Math.floor(startMs % timeBlockMs / timeSquareMs);
		}

		count() {
			const timeSquaresCountInMarkBlock = this.timeSquareRowsCount * this.squaresBetweenMarks;
			const scaledTimeSquaresCount = Math.ceil(this.blocksData.counts.length / this.timeSquareScale) + this.startBlock();
			return Math.ceil(scaledTimeSquaresCount / timeSquaresCountInMarkBlock) * timeSquaresCountInMarkBlock;
		}

		setZoom(z) {
			this.zoom = z;
			this.timeSquareScale = zoomToGroupSize[z];
			this.timeSquareRowsCount = zoomToHeight[z];
		}

		max(search) {
			return search ? this.blocksData.searchMaxCounts[this.zoom] : this.blocksData.maxCounts[this.zoom];
		}

		min(search) {
			return search ? this.blocksData.searchMinCounts[this.zoom] : this.blocksData.minCounts[this.zoom];
		}
	}

	function claimHtml(id) {
		let e = document.getElementById(id);
		let r = e.innerHTML;
		e.remove();
		return r;
	}

	function methodName(className, methodName, bci, line, type) {
		const locationSuffix = line === 0 ? (bci === 0 ? "" : ("@" + bci)) : (":" + line);

		if (methodName === '') {
			return className + locationSuffix;
		}
		if (className === '') {
			return methodName + locationSuffix;
		}
		if (type >= 3 && type <= 5) {
			return methodName + locationSuffix;
		}

		return className + "." + methodName + locationSuffix;
	}

	function readMethods(data) {
		data.nextInt6();
		const count = data.nextVarInt();
		const names = [];
		const colors = [];
		const bcis = new Array(count + 1);

		names.push(methodName("all", "", 0, 0, 3));
		colors.push(getColorStable(palette[3], 0));

		for (let i = 0; i < count; i++) {
			const className = data.nextVarInt();
			const name = data.nextVarInt();
			const bci = data.nextInt18();
			const line = data.nextInt18();
			const type = data.nextInt6();

			const noline = bci === 0xffff && line === 0xffff;

			names.push(methodName(cpool[className], cpool[name], noline ? 0 : bci, noline ? 0 : line, type));
			colors.push(getColorStable(palette[type], i + 1));
			bcis[i + 1] = noline ? "" : ", bci: " + bci;
		}

		return {n: names, c: colors, b: bcis};
	}

	let sq = 5;
	let sqPx = sq;
	let sqScale = 1;
	const canvasScrollPadding = 200;
	const taskMaxTimeMs = 8;
	let canvasTimeHeight = 12;
	let canvasTimeHeightPx = 12;
	let startMs = /*startMs:*/0;

	const zoomToGroupSize = [
		1,              // 20 ms
		50,             // 1 s
		50 * 5,         // 5 s
	];
	const zoomToHeight = [
		50,
		60,
		60,
	];
	const zoomToText = [
		' 1 sec : 20 ms ',
		' 1 min : 1 sec ',
		' 5 min : 5 sec ',
		' 1 hr  : 1 min '
	];

	const currentHeatmap = new HeatmapCollection(claimHtml("executionsHeatmap"));
	let cpool = [/*cpool:*/];
	const methods = readMethods(new DataBuffer(claimHtml("methods")));
	cpool = null;

	let heatLastSample = -1;
	let heatActiveSample1 = -1;
	let heatActiveSample2 = -1;
	let heatDiffSample1 = -1;
	let heatDiffSample2 = -1;
	let highlightStart = -1;
	let highlightEnd = -1;

	const titleText = document.getElementById("title").textContent;
	document.getElementById("title").style.display = 'none';
	document.title = titleText;

	const heatCanvas = document.getElementById('heatmap-canvas');
	const heatCanvasWrapper = document.getElementById('heatmap-canvas-wrapper');
	const heatCanvasContainer = document.getElementById('heatmap-canvas-container');

	let heatC;
	let prevDx = -1000000000;

	const timeOptionsShort = {
		hour: '2-digit',
		minute: '2-digit',
		second: '2-digit',
		hourCycle: 'h23',
		fractionalSecondDigits: 2
	};

	const timeOptionsTiny = {
		hour: '2-digit',
		minute: '2-digit',
		second: '2-digit',
		hourCycle: 'h23'
	};

	const timeOptionsTinyWithTZ = {
		hour: '2-digit',
		minute: '2-digit',
		second: '2-digit',
		hourCycle: 'h23',
		timeZoneName: 'short'
	};

	let currentTimezone = localStorage.getItem('heatmap-timezone') || 'Local';

	function formatTime(ms, options) {
		const date = new Date(ms);
		if (currentTimezone === 'UTC') {
			return date.toLocaleTimeString(undefined, {...options, timeZone: 'UTC'});
		} else {
			return date.toLocaleTimeString(undefined, options);
		}
	}

	function getCount(counts, i) {
		if (i < 0 || counts.length === 0) {
			return 0;
		}
		return counts[Math.min(i, counts.length - 1)];
	}

	let bgInterval = null;
	let bgTasks = [];
	let cooldownTime = 0;
	let nextTask = 0;

	function addTask(id, iteration, afterFrame) {
		if (!afterFrame) afterFrame = function () {};

		for (let t of bgTasks) {
			if (t.id === id) {
				t.f = iteration;
				t.a = afterFrame;
				return;
			}
		}

		bgTasks.push({id: id, f: iteration, a: afterFrame});
		if (bgTasks.length === 1) {
			bgInterval = setInterval(function () {
				let start = performance.now();
				if (start <= cooldownTime) {
					return;
				}
				let overflow = false;
				do {
					let task = bgTasks[nextTask];
					let runAgain;
					try {
						runAgain = task.f();
					} catch (e) {
						console.error(e);
						bgTasks.length = 0;
						clearInterval(bgInterval);
						nextTask = 0;
						return;
					}

					if (runAgain) {
						nextTask++;
					} else {
						bgTasks.splice(nextTask, 1);
						if (bgTasks.length === 0) {
							clearInterval(bgInterval);
							nextTask = 0;
							return;
						}
					}

					if (nextTask >= bgTasks.length) {
						nextTask = 0;
						overflow = true;
					}
				} while (performance.now() - start < taskMaxTimeMs);

				for (let q = 0; q < overflow ? bgTasks.length : nextTask; q++) {
					bgTasks[q].a();
				}
			})
		}
	}

	function sort(array, start, end, values, bit) {
		while (true) {
			switch (end - start) {
				case 0:
				case 1:
					return;
				case 2: {
					let a = array[start];
					let b = array[start + 1];
					if (values[a] < values[b]) {
						array[start] = b;
						array[start + 1] = a;
					}
					return;
				}
			}

			let left = start;
			let right = end;

			while (true) {
				while (left < right) {
					let v = values[array[left]];
					if ((v & bit) !== 0) {
						left++;
					} else {
						break;
					}
				}
				while (left < right) {
					let v = values[array[right - 1]];
					if ((v & bit) === 0) {
						right--;
					} else {
						break;
					}
				}

				if (left < right) {
					right--;
					let l = array[left];
					array[left] = array[right];
					array[right] = l;
					left++;
				} else {
					bit >>= 1;
					if (bit === 0) {
						return;
					}
					if (end - left > right - start) {
						if (right - start > 1) {
							sort(array, start, right, values, bit);
						}
						start = left;
					} else {
						if (end - left > 1) {
							sort(array, left, end, values, bit);
						}
						end = right;
					}
					break;
				}
			}
		}
	}

	function allocateHugeArray() {
		// Note: it is very random huge number that relies on malloc laziness
		// real pre-calculation is both non-performant and fragile
		return new Uint32Array(100 * 1024 * 1024);
	}

	function renderWrapper(from, to) {
		lastRenderFrom = from;
		lastRenderTo = to;
		renderFunc(from, to);
	}

	function renderWrapperDiff(from, to, baseFrom, baseTo) {
		lastRenderFrom = from;
		lastRenderTo = to;
		lastBaseRenderFrom = baseFrom;
		lastBaseRenderTo = baseTo;
		renderFuncDiff(from, to, baseFrom, baseTo);
	}

	function reselect() {
		if (heatDiffSample1 === -1) {
			renderFunc(lastRenderFrom, lastRenderTo);
		} else {
			renderFuncDiff(lastRenderFrom, lastRenderTo, lastBaseRenderFrom, lastBaseRenderTo);
		}
	}

	function selectMode(mode) {
		switch (mode) {
			case 'flame-mode-flame':
				renderFunc = renderTraces;
				renderFuncDiff = renderTracesDiff;
				break;
			case 'flame-mode-reversed':
				renderFunc = renderTracesReversed;
				renderFuncDiff = renderTracesReversedDiff;
				break;
			case 'flame-mode-methods':
				renderFunc = renderSelfDominators;
				renderFuncDiff = renderSelfDominatorsDiff;
				break;
		}
		for (let m of ['flame-mode-flame', 'flame-mode-reversed', 'flame-mode-methods']) {
			document.getElementById(m).classList.remove('toolbarSelected');
		}
		document.getElementById(mode).classList.add('toolbarSelected');
		reselect();
	}

	function diffColor(count, baseCount, minDiff, maxDiff) {
		if (baseCount === 0) {
			return "#ffdd33";
		}
		if (baseCount === count) {
			return '#66e0f0';
		}
		if (baseCount > count) {
			const ratio = (baseCount - count) / minDiff;
			const ratioM = (ratio * 96 + 16) | 0;
			const C = 255 - Math.abs(255 - (ratioM << 1));
			const m = (255 - ratioM) - (C >> 1);

			return 'rgb(' + (((dRdl * C) >> 8) + m) + ',' + (((dGdl * C) >> 8) + m) + ',' + (((dBdl * C) >> 8) + m) + ')';
		}

		const ratio = (count - baseCount) / maxDiff;
		const ratioM = (ratio * 96 + 16) | 0;
		const C = 255 - Math.abs(255 - (ratioM << 1));
		const m = (255 - ratioM) - (C >> 1);

		return 'rgb(' + (((dRdg * C) >> 8) + m) + ',' + (((dGdg * C) >> 8) + m) + ',' + (((dBdg * C) >> 8) + m) + ')';
	}

	function prepareRender() {
		root = undefined;
		rootLevel = 0;
		c.fillStyle = '#ffffff';
		c.fillRect(0, 0, canvasWidth, canvasHeight);
		hl.style.display = 'none';
		addTask('flame', function () {
			return false;
		});
	}

	function renderTraces(from, to) {
		prepareRender();
		addTask('flamePrepare', () => {
			let [framesBuffer, sampleToChunkPos, sampleToStorageDelta, longSamplesBuffer] = prepareFrames(from, to);
			let nextFramesBuffer = allocateHugeArray();

			levels.length = 0;

			let levelToRedraw = 0;

			const ctx = {
				frames: framesBuffer,
				nextFrames: nextFramesBuffer,
				sampleToChunkPos: sampleToChunkPos,
				sampleToStorageDelta: sampleToStorageDelta,
				longSamplesBuffer: longSamplesBuffer,
				level: 0,
				chunksToStorage: currentHeatmap.blocksData.chunksToStorage,
				storage: currentHeatmap.blocksData.storage,
				sampleToChunkEnds: currentHeatmap.blocksData.sampleToChunkEnds,
				storageSizes: currentHeatmap.blocksData.storageSizes,
				methodsBuffer: new Uint32Array(methods.c.length + 1),
				methodsBufferTheOnlyChunks: new Uint32Array(methods.c.length + 1),
				methodsBufferLongSamples: new Uint32Array(methods.c.length + 1),
				methodsBufferDirectSamples: new Uint32Array(methods.c.length + 1),

				startX: 0,
				theOnlyChunksCount: 0,
				longSamplesChunksCount: 0,
				directSamplesCount: 0,

				framesPointer: 0,
				nextFramesPointer: 0,
				nextFramesCount: 0,
				methodsMapFirstPos: 0,
			};

			addTask('flame', () => {
					ctx.level = levels.length;
					const roots = nextFrames(ctx);
					if (roots.length === 0) {
						if (levels.length === 0) {
							levels.push([{left: 0, width: 0, color: methods.c[0], title: methods.n[0], method: 0}]);
						}
						renderWithMatch(levels.length * 16, root, rootLevel);
						return false;
					}

					const tmp = ctx.nextFrames;
					ctx.nextFrames = ctx.frames;
					ctx.frames = tmp;

					levels.push(roots);

					return true;
				},
				() => {
					renderWithMatch(4096, root, rootLevel, levelToRedraw);
					levelToRedraw = levels.length;
				});
			return false;
		});
	}

	function renderTracesDiff(from, to, baseFrom, baseTo) {
		prepareRender();
		let [framesBuffer, sampleToChunkPos, sampleToStorageDelta] = prepareFramesDiff(from, to, baseFrom, baseTo);
		let nextFramesBuffer = allocateHugeArray();

		levels.length = 0;

		let levelToRedraw = 0;

		let minDiff = 1;
		let maxDiff = 1;
		const ctx = {
			frames: framesBuffer,
			nextFrames: nextFramesBuffer,
			sampleToChunkPos: sampleToChunkPos,
			sampleToStorageDelta: sampleToStorageDelta,
			level: 0,
			chunksToStorage: currentHeatmap.blocksData.chunksToStorage,
			storage: currentHeatmap.blocksData.storage,
			sampleToChunkEnds: currentHeatmap.blocksData.sampleToChunkEnds,
			storageSizes: currentHeatmap.blocksData.storageSizes,

			methodsBuffer: new Uint32Array(methods.c.length + 1),
			methodsBufferTheOnlyChunks: new Uint32Array(methods.c.length + 1),
			methodsBufferDirectSamples: new Uint32Array(methods.c.length + 1),
			baseMethodsBuffer: new Uint32Array(methods.c.length + 1),
			baseMethodsBufferTheOnlyChunks: new Uint32Array(methods.c.length + 1),
			baseMethodsBufferDirectSamples: new Uint32Array(methods.c.length + 1),

			startX: 0,
			theOnlyChunksCount: 0,
			directSamplesCount: 0,
			baseTheOnlyChunksCount: 0,
			baseDirectSamplesCount: 0,

			framesPointer: 0,
			nextFramesPointer: 0,
			nextFramesCount: 0,
			methodsMapFirstPos: 0,
		};

		addTask('flame', function () {
				ctx.level = levels.length;
				const roots = nextFramesDiff(ctx);
				if (roots.length === 0) {
					if (levels.length === 0) {
						levels.push([{left: 0, width: 0, color: methods.c[0], title: methods.n[0], method: 0}]);
					}
					renderWithMatch(levels.length * 16, root, rootLevel);
					return false;
				}

				for (let root of roots) {
					if (root.baseWidth >= root.width) {
						minDiff = Math.max(minDiff, root.baseWidth - root.width);
					} else {
						maxDiff = Math.max(maxDiff, root.width - root.baseWidth);
					}
				}

				for (let root of roots) {
					root.color = diffColor(root.width, root.baseWidth, minDiff, maxDiff);
					root.title = root.title + " (" + root.width + "/" + root.baseWidth + ")";
				}

				const tmpBuffer = ctx.nextFrames;
				ctx.nextFrames = ctx.frames;
				ctx.frames = tmpBuffer;

				levels.push(roots);
				return true;
			},
			function () {
				renderWithMatch(4096, root, rootLevel, levelToRedraw);
				levelToRedraw = levels.length;
			});
	}

	function renderTracesReversed(from, to) {
		prepareRender();
		addTask('flamePrepare', () => {
			let [framesBuffer, sampleToChunkPos, sampleToStorageDelta, longSamplesBuffer] = prepareFramesReversed(from, to);
			let nextFramesBuffer = allocateHugeArray();

			levels.length = 0;

			let levelToRedraw = 0;

			const ctx = {
				frames: framesBuffer,
				nextFrames: nextFramesBuffer,
				sampleToChunkPos: sampleToChunkPos,
				sampleToStorageDelta: sampleToStorageDelta,
				longSamplesBuffer: longSamplesBuffer,
				level: 0,
				chunksToStorage: currentHeatmap.blocksData.chunksToStorage,
				storage: currentHeatmap.blocksData.storage,
				sampleToChunkEnds: currentHeatmap.blocksData.sampleToChunkEnds,
				storageSizes: currentHeatmap.blocksData.storageSizes,
				methodsBuffer: new Uint32Array(methods.c.length + 1),
				methodsBufferTheOnlyChunks: new Uint32Array(methods.c.length + 1),
				methodsBufferDirectSamples: new Uint32Array(methods.c.length + 1),

				startX: 0,
				theOnlyChunksCount: 0,
				directSamplesCount: 0,

				framesPointer: 0,
				nextFramesPointer: 0,
				nextFramesCount: 0,
				methodsMapFirstPos: 0,
			};

			addTask('flame', () => {
					ctx.level = levels.length;
					const roots = nextFramesReversed(ctx);
					if (roots.length === 0) {
						if (levels.length === 0) {
							levels.push([{left: 0, width: 0, color: methods.c[0], title: methods.n[0], method: 0}]);
						}
						renderWithMatch(levels.length * 16, root, rootLevel);
						return false;
					}

					const tmp = ctx.nextFrames;
					ctx.nextFrames = ctx.frames;
					ctx.frames = tmp;

					levels.push(roots);

					return true;
				},
				() => {
					renderWithMatch(4096, root, rootLevel, levelToRedraw);
					levelToRedraw = levels.length;
				});
			return false;
		});
	}

	function renderTracesReversedDiff(from, to, baseFrom, baseTo) {
		prepareRender();
		let [framesBuffer, sampleToChunkPos, sampleToStorageDelta] = prepareFramesReversedDiff(from, to, baseFrom, baseTo);
		let nextFramesBuffer = allocateHugeArray();

		levels.length = 0;

		let levelToRedraw = 0;

		let minDiff = 1;
		let maxDiff = 1;
		const ctx = {
			frames: framesBuffer,
			nextFrames: nextFramesBuffer,
			sampleToChunkPos: sampleToChunkPos,
			sampleToStorageDelta: sampleToStorageDelta,
			level: 0,
			chunksToStorage: currentHeatmap.blocksData.chunksToStorage,
			storage: currentHeatmap.blocksData.storage,
			sampleToChunkEnds: currentHeatmap.blocksData.sampleToChunkEnds,
			storageSizes: currentHeatmap.blocksData.storageSizes,

			methodsBuffer: new Uint32Array(methods.c.length + 1),
			methodsBufferTheOnlyChunks: new Uint32Array(methods.c.length + 1),
			methodsBufferDirectSamples: new Uint32Array(methods.c.length + 1),
			baseMethodsBuffer: new Uint32Array(methods.c.length + 1),
			baseMethodsBufferTheOnlyChunks: new Uint32Array(methods.c.length + 1),
			baseMethodsBufferDirectSamples: new Uint32Array(methods.c.length + 1),

			startX: 0,
			theOnlyChunksCount: 0,
			directSamplesCount: 0,
			baseTheOnlyChunksCount: 0,
			baseDirectSamplesCount: 0,

			framesPointer: 0,
			nextFramesPointer: 0,
			nextFramesCount: 0,
			methodsMapFirstPos: 0,
		};

		addTask('flame', function () {
				ctx.level = levels.length;
				const roots = nextFramesReversedDiff(ctx);
				if (roots.length === 0) {
					if (levels.length === 0) {
						levels.push([{left: 0, width: 0, color: methods.c[0], title: methods.n[0], method: 0}]);
					}
					renderWithMatch(levels.length * 16, root, rootLevel);
					return false;
				}

				for (let root of roots) {
					if (root.baseWidth >= root.width) {
						minDiff = Math.max(minDiff, root.baseWidth - root.width);
					} else {
						maxDiff = Math.max(maxDiff, root.width - root.baseWidth);
					}
				}

				for (let root of roots) {
					root.color = diffColor(root.width, root.baseWidth, minDiff, maxDiff);
					root.title = root.title + " (" + root.width + "/" + root.baseWidth + ")";
				}

				const tmpBuffer = ctx.nextFrames;
				ctx.nextFrames = ctx.frames;
				ctx.frames = tmpBuffer;

				levels.push(roots);
				return true;
			},
			function () {
				renderWithMatch(4096, root, rootLevel, levelToRedraw);
				levelToRedraw = levels.length;
			});
	}

	function renderSelfDominators(from, to) {
		prepareRender();
		addTask('flamePrepare', () => {
			const chunksToStorage = currentHeatmap.blocksData.chunksToStorage;
			const sampleToChunkEnds = currentHeatmap.blocksData.sampleToChunkEnds;
			const storage = currentHeatmap.blocksData.storage;
			const counts = currentHeatmap.blocksData.counts;

			const countBeforeFirstBlock = getCount(counts, from - 1);
			const countAtLastBlock = getCount(counts, to);

			const methodsCount = new Uint32Array(methods.c.length);
			const methodsBuffer = new Uint32Array(methods.c.length);
			let methodsInBuffer = 0;
			let maxCount = 0;

			for (let sampleIndex = countBeforeFirstBlock; sampleIndex < countAtLastBlock; sampleIndex++) {
				const chunkEndPos = sampleToChunkEnds[sampleIndex];
				const storagePos = chunksToStorage[chunkEndPos - 1];
				const method = storage[storagePos];
				const oldCount = methodsCount[method]++;
				if (isNaN(oldCount)) {
					throw "old count is nan";
				}
				if (oldCount === 0) {
					methodsBuffer[methodsInBuffer++] = method;
				}
				maxCount = Math.max(maxCount, oldCount);
			}

			sort(methodsBuffer, 0, methodsInBuffer, methodsCount, 1 << (31 - Math.clz32(maxCount + 1)));
			levels.length = 0;
			for (let i = 0; i < methodsInBuffer; i++) {
				const method = methodsBuffer[i];
				levels.push([{
					left: 0,
					width: methodsCount[method],
					color: methods.c[method],
					title: methods.n[method],
					method: method
				}]);
			}
			renderWithMatch(levels.length * 16, root, rootLevel);
			return false;
		});
	}

	function renderSelfDominatorsDiff(from, to, baseFrom, baseTo) {
		prepareRender();
		addTask('flamePrepare', () => {
			const chunksToStorage = currentHeatmap.blocksData.chunksToStorage;
			const sampleToChunkEnds = currentHeatmap.blocksData.sampleToChunkEnds;
			const storage = currentHeatmap.blocksData.storage;
			const counts = currentHeatmap.blocksData.counts;

			const countBeforeFirstBlock = getCount(counts, from - 1);
			const countAtLastBlock = getCount(counts, to);

			const baseCountBeforeFirstBlock = getCount(counts, baseFrom - 1);
			const baseCountAtLastBlock = getCount(counts, baseTo);

			const methodsCount = new Uint32Array(methods.c.length);
			const baseMethodsCount = new Uint32Array(methods.c.length);
			const methodsBuffer = new Uint32Array(methods.c.length);
			let methodsInBuffer = 0;
			let maxCount = 1;
			let minDiff = 1;
			let maxDiff = 1;

			for (let sampleIndex = countBeforeFirstBlock; sampleIndex < countAtLastBlock; sampleIndex++) {
				const chunkEndPos = sampleToChunkEnds[sampleIndex];
				const storagePos = chunksToStorage[chunkEndPos - 1];
				const method = storage[storagePos];
				const oldCount = methodsCount[method]++;
				if (oldCount === 0) {
					methodsBuffer[methodsInBuffer++] = method;
				}
				maxCount = Math.max(maxCount, oldCount);
			}

			for (let sampleIndex = baseCountBeforeFirstBlock; sampleIndex < baseCountAtLastBlock; sampleIndex++) {
				const chunkEndPos = sampleToChunkEnds[sampleIndex];
				const storagePos = chunksToStorage[chunkEndPos - 1];
				const method = storage[storagePos];
				const oldCount = baseMethodsCount[method]++;
				if (oldCount === 0 && methodsCount[method] === 0) {
					methodsBuffer[methodsInBuffer++] = method;
				}
			}

			for (let i = 0; i < methodsInBuffer; i++) {
				const method = methodsBuffer[i];
				const count = methodsCount[method];
				const baseCount = baseMethodsCount[method];

				if (baseCount > count) {
					minDiff = Math.max(minDiff, baseCount - count);
				} else {
					maxDiff = Math.max(maxDiff, count - baseCount);
				}
			}

			sort(methodsBuffer, 0, methodsInBuffer, methodsCount, 1 << (31 - Math.clz32(maxCount)));

			levels.length = 0;
			for (let i = 0; i < methodsInBuffer; i++) {
				const method = methodsBuffer[i];
				const count = methodsCount[method];
				const baseCount = baseMethodsCount[method];
				const title = methods.n[method] + " (" + count + "/" + baseCount + ")"

				let color = diffColor(count, baseCount, minDiff, maxDiff);
				levels.push([{left: 0, width: count, color: color, title: title, method: method}]);
			}
			renderWithMatch(levels.length * 16, root, rootLevel);
			return false;
		});
	}

	function prepareFrames(from, to) {
		const chunksToStorage = currentHeatmap.blocksData.chunksToStorage;
		const sampleToChunkEnds = currentHeatmap.blocksData.sampleToChunkEnds;
		const storageSizes = currentHeatmap.blocksData.storageSizes;
		const counts = currentHeatmap.blocksData.counts;

		const countBeforeFirstBlock = getCount(counts, from - 1);
		const countAtLastBlock = getCount(counts, to);

		const theOnlyChunksBuffer = allocateHugeArray();
		const firstChunkPosOfLongSamplesBuffer = allocateHugeArray();
		const sampleToChunkPos = new Uint32Array(sampleToChunkEnds.length);
		const sampleToStorageDelta = new Uint32Array(sampleToChunkEnds.length);
		const firstChunkPosOfLongSamples = new Uint32Array(storageSizes.length);
		const theOnlyChunks = new Uint32Array(storageSizes.length);

		let theOnlyChunksBufferPos = 0;

		let firstChunkPosOfLongSamplesPos = 0;
		let totalCountLongSamples = 0;
		let count = 0;
		for (let sampleIndex = countBeforeFirstBlock; sampleIndex < countAtLastBlock; sampleIndex++) {
			if (filterOut(sampleIndex)) {
				continue;
			}
			count++;
			const chunkPos = sampleToChunkEnds[sampleIndex - 1] || 0;
			const chunkEndPos = sampleToChunkEnds[sampleIndex];
			const storagePos = chunksToStorage[chunkPos];
			if (chunkPos + 1 === chunkEndPos) {
				if (theOnlyChunks[storagePos]++ === 0) {
					theOnlyChunksBuffer[theOnlyChunksBufferPos++] = storagePos;
				}
			} else {
				if (firstChunkPosOfLongSamples[storagePos]++ === 0) {
					firstChunkPosOfLongSamplesBuffer[firstChunkPosOfLongSamplesPos++] = storagePos;
				}
				totalCountLongSamples++;
			}
		}

		const framesBuffer = allocateHugeArray();
		framesBuffer[0] = count === 0 ? 0 : 1;    // frames count on this level

		framesBuffer[1] = 0;    // methodId
		framesBuffer[2] = 0;    // x
		framesBuffer[3] = count;
		framesBuffer[4] = theOnlyChunksBufferPos;
		framesBuffer[5] = firstChunkPosOfLongSamplesPos;
		framesBuffer[6] = 0;    // direct samples count

		let framesBufferPos = 7;

		for (let storagePosIndex = 0; storagePosIndex < theOnlyChunksBufferPos; storagePosIndex++) {
			const storagePos = theOnlyChunksBuffer[storagePosIndex];
			framesBuffer[framesBufferPos++] = storagePos;
			framesBuffer[framesBufferPos++] = theOnlyChunks[storagePos];
		}

		const longSamplesBuffer = new Uint32Array(totalCountLongSamples);
		let longSamplesBufferPos = 0;
		for (let storagePosIndex = 0; storagePosIndex < firstChunkPosOfLongSamplesPos; storagePosIndex++) {
			const storagePos = firstChunkPosOfLongSamplesBuffer[storagePosIndex];
			const count = firstChunkPosOfLongSamples[storagePos];
			framesBuffer[framesBufferPos++] = storagePos;
			framesBuffer[framesBufferPos++] = count;
			framesBuffer[framesBufferPos++] = longSamplesBufferPos;

			firstChunkPosOfLongSamples[storagePos] = longSamplesBufferPos;
			longSamplesBufferPos += count;
		}

		for (let sampleIndex = countBeforeFirstBlock; sampleIndex < countAtLastBlock; sampleIndex++) {
			if (filterOut(sampleIndex)) {
				continue;
			}
			const chunkPos = sampleToChunkEnds[sampleIndex - 1] || 0;
			const chunkEndPos = sampleToChunkEnds[sampleIndex];
			const storagePos = chunksToStorage[chunkPos];
			if (chunkPos + 1 !== chunkEndPos) {
				longSamplesBuffer[firstChunkPosOfLongSamples[storagePos]++] = sampleIndex;
			}
		}

		return [framesBuffer, sampleToChunkPos, sampleToStorageDelta, longSamplesBuffer];
	}

	function prepareFramesDiff(from, to, baseFrom, baseTo) {
		const chunksToStorage = currentHeatmap.blocksData.chunksToStorage;
		const sampleToChunkEnds = currentHeatmap.blocksData.sampleToChunkEnds;
		const storageSizes = currentHeatmap.blocksData.storageSizes;
		const counts = currentHeatmap.blocksData.counts;

		const countBeforeFirstBlock = getCount(counts, from - 1);
		const countAtLastBlock = getCount(counts, to);

		const baseCountBeforeFirstBlock = getCount(counts, baseFrom - 1);
		const baseCountAtLastBlock = getCount(counts, baseTo);

		const theOnlyChunksBuffer = allocateHugeArray();
		const sampleToChunkPos = new Uint32Array(sampleToChunkEnds.length);
		const sampleToStorageDelta = new Uint32Array(sampleToChunkEnds.length);
		const theOnlyChunks = new Uint32Array(storageSizes.length);
		const baseTheOnlyChunks = new Uint32Array(storageSizes.length);

		let theOnlyChunksBufferPos = 0;
		let singleSamplesCount = 0;
		let count = 0;
		for (let sampleIndex = countBeforeFirstBlock; sampleIndex < countAtLastBlock; sampleIndex++) {
			if (filterOut(sampleIndex)) {
				continue;
			}
			count++;
			const chunkPos = sampleToChunkEnds[sampleIndex - 1] || 0;
			const chunkEndPos = sampleToChunkEnds[sampleIndex];
			if (chunkPos + 1 === chunkEndPos) {
				const storagePos = chunksToStorage[chunkPos];
				if (theOnlyChunks[storagePos]++ === 0) {
					theOnlyChunksBuffer[theOnlyChunksBufferPos++] = storagePos;
				}
			} else {
				singleSamplesCount++;
			}
		}

		const theOnlyChunksCount = theOnlyChunksBufferPos;
		let baseSingleSamplesCount = 0;
		let baseCount = 0;
		for (let sampleIndex = baseCountBeforeFirstBlock; sampleIndex < baseCountAtLastBlock; sampleIndex++) {
			if (filterOut(sampleIndex)) {
				continue;
			}
			baseCount++;
			const chunkPos = sampleToChunkEnds[sampleIndex - 1] || 0;
			const chunkEndPos = sampleToChunkEnds[sampleIndex];
			if (chunkPos + 1 === chunkEndPos) {
				const storagePos = chunksToStorage[chunkPos];
				if (baseTheOnlyChunks[storagePos]++ === 0) {
					theOnlyChunksBuffer[theOnlyChunksBufferPos++] = storagePos;
				}
			} else {
				baseSingleSamplesCount++;
			}
		}

		const framesBuffer = allocateHugeArray();
		framesBuffer[0] = 1;    // frames count on this level

		framesBuffer[1] = 0;    // methodId
		framesBuffer[2] = 0;    // x
		framesBuffer[3] = count;
		framesBuffer[4] = theOnlyChunksCount;
		framesBuffer[5] = singleSamplesCount;
		framesBuffer[6] = baseCount;
		framesBuffer[7] = theOnlyChunksBufferPos - theOnlyChunksCount;
		framesBuffer[8] = baseSingleSamplesCount;

		let framesBufferPos = 9;

		for (let storagePosIndex = 0; storagePosIndex < theOnlyChunksCount; storagePosIndex++) {
			const storagePos = theOnlyChunksBuffer[storagePosIndex];
			framesBuffer[framesBufferPos++] = storagePos;
			framesBuffer[framesBufferPos++] = theOnlyChunks[storagePos];
		}

		for (let sampleIndex = countBeforeFirstBlock; sampleIndex < countAtLastBlock; sampleIndex++) {
			if (filterOut(sampleIndex)) {
				continue;
			}
			const chunkPos = sampleToChunkEnds[sampleIndex - 1] || 0;
			const chunkEndPos = sampleToChunkEnds[sampleIndex];
			if (chunkPos + 1 !== chunkEndPos) {
				sampleToChunkPos[sampleIndex] = chunkPos;

				const storagePos = chunksToStorage[chunkPos];
				sampleToStorageDelta[sampleIndex] = storageSizes[storagePos] | 0x80000000;

				framesBuffer[framesBufferPos++] = sampleIndex;
			}
		}

		for (let storagePosIndex = theOnlyChunksCount; storagePosIndex < theOnlyChunksBufferPos; storagePosIndex++) {
			const storagePos = theOnlyChunksBuffer[storagePosIndex];
			framesBuffer[framesBufferPos++] = storagePos;
			framesBuffer[framesBufferPos++] = baseTheOnlyChunks[storagePos];
		}

		for (let sampleIndex = baseCountBeforeFirstBlock; sampleIndex < baseCountAtLastBlock; sampleIndex++) {
			if (filterOut(sampleIndex)) {
				continue;
			}
			const chunkPos = sampleToChunkEnds[sampleIndex - 1] || 0;
			const chunkEndPos = sampleToChunkEnds[sampleIndex];
			if (chunkPos + 1 !== chunkEndPos) {
				if (sampleToStorageDelta[sampleIndex] === 0) {
					sampleToChunkPos[sampleIndex] = chunkPos;

					const storagePos = chunksToStorage[chunkPos];
					sampleToStorageDelta[sampleIndex] = storageSizes[storagePos];
				}
				framesBuffer[framesBufferPos++] = sampleIndex;
			}
		}

		return [framesBuffer, sampleToChunkPos, sampleToStorageDelta];
	}

	function prepareFramesReversed(from, to) {
		const chunksToStorage = currentHeatmap.blocksData.chunksToStorage;
		const sampleToChunkEnds = currentHeatmap.blocksData.sampleToChunkEnds;
		const storageSizes = currentHeatmap.blocksData.storageSizes;
		const counts = currentHeatmap.blocksData.counts;

		const countBeforeFirstBlock = getCount(counts, from - 1);
		const countAtLastBlock = getCount(counts, to);

		const theOnlyChunksBuffer = allocateHugeArray();
		const sampleToChunkPos = new Uint32Array(sampleToChunkEnds.length);
		const sampleToStorageDelta = new Uint32Array(sampleToChunkEnds.length);
		const theOnlyChunks = new Uint32Array(storageSizes.length);

		let theOnlyChunksBufferPos = 0;
		let singleSamplesCount = 0;
		let count = 0;
		for (let sampleIndex = countBeforeFirstBlock; sampleIndex < countAtLastBlock; sampleIndex++) {
			if (filterOut(sampleIndex)) {
				continue;
			}
			count++;
			const chunkPos = sampleToChunkEnds[sampleIndex - 1] || 0;
			const chunkEndPos = sampleToChunkEnds[sampleIndex];
			if (chunkPos === chunkEndPos - 1) {
				const storagePos = chunksToStorage[chunkPos];
				if (theOnlyChunks[storagePos]++ === 0) {
					theOnlyChunksBuffer[theOnlyChunksBufferPos++] = storagePos;
				}
			} else {
				singleSamplesCount++;
			}
		}

		const framesBuffer = allocateHugeArray();
		framesBuffer[0] = count === 0 ? 0 : 1;    // frames count on this level

		framesBuffer[1] = 0;    // methodId
		framesBuffer[2] = 0;    // x
		framesBuffer[3] = count;
		framesBuffer[4] = theOnlyChunksBufferPos;
		framesBuffer[5] = singleSamplesCount;    // direct samples count

		let framesBufferPos = 6;

		for (let storagePosIndex = 0; storagePosIndex < theOnlyChunksBufferPos; storagePosIndex++) {
			const storagePos = theOnlyChunksBuffer[storagePosIndex];
			framesBuffer[framesBufferPos++] = storagePos;
			framesBuffer[framesBufferPos++] = theOnlyChunks[storagePos];
		}

		for (let sampleIndex = countBeforeFirstBlock; sampleIndex < countAtLastBlock; sampleIndex++) {
			if (filterOut(sampleIndex)) {
				continue;
			}
			const chunkPos = sampleToChunkEnds[sampleIndex - 1] || 0;
			const chunkEndPos = sampleToChunkEnds[sampleIndex];
			if (chunkPos !== chunkEndPos - 1) {
				sampleToChunkPos[sampleIndex] = chunkEndPos - 1;
				sampleToStorageDelta[sampleIndex] = 0;

				framesBuffer[framesBufferPos++] = sampleIndex;
			}
		}

		return [framesBuffer, sampleToChunkPos, sampleToStorageDelta];
	}

	function prepareFramesReversedDiff(from, to, baseFrom, baseTo) {
		const chunksToStorage = currentHeatmap.blocksData.chunksToStorage;
		const sampleToChunkEnds = currentHeatmap.blocksData.sampleToChunkEnds;
		const storageSizes = currentHeatmap.blocksData.storageSizes;
		const counts = currentHeatmap.blocksData.counts;

		const countBeforeFirstBlock = getCount(counts, from - 1);
		const countAtLastBlock = getCount(counts, to);

		const baseCountBeforeFirstBlock = getCount(counts, baseFrom - 1);
		const baseCountAtLastBlock = getCount(counts, baseTo);

		const theOnlyChunksBuffer = allocateHugeArray();
		const sampleToChunkPos = new Uint32Array(sampleToChunkEnds.length);
		const sampleToStorageDelta = new Uint32Array(sampleToChunkEnds.length);
		const theOnlyChunks = new Uint32Array(storageSizes.length);
		const baseTheOnlyChunks = new Uint32Array(storageSizes.length);

		let theOnlyChunksBufferPos = 0;
		let singleSamplesCount = 0;
		let count = 0;
		for (let sampleIndex = countBeforeFirstBlock; sampleIndex < countAtLastBlock; sampleIndex++) {
			if (filterOut(sampleIndex)) {
				continue;
			}
			count++;
			const chunkPos = sampleToChunkEnds[sampleIndex - 1] || 0;
			const chunkEndPos = sampleToChunkEnds[sampleIndex];
			if (chunkPos + 1 === chunkEndPos) {
				const storagePos = chunksToStorage[chunkPos];
				if (theOnlyChunks[storagePos]++ === 0) {
					theOnlyChunksBuffer[theOnlyChunksBufferPos++] = storagePos;
				}
			} else {
				singleSamplesCount++;
			}
		}

		const theOnlyChunksCount = theOnlyChunksBufferPos;
		let baseSingleSamplesCount = 0;
		let baseCount = 0;
		for (let sampleIndex = baseCountBeforeFirstBlock; sampleIndex < baseCountAtLastBlock; sampleIndex++) {
			if (filterOut(sampleIndex)) {
				continue;
			}
			baseCount++;
			const chunkPos = sampleToChunkEnds[sampleIndex - 1] || 0;
			const chunkEndPos = sampleToChunkEnds[sampleIndex];
			if (chunkPos + 1 === chunkEndPos) {
				const storagePos = chunksToStorage[chunkPos];
				if (baseTheOnlyChunks[storagePos]++ === 0) {
					theOnlyChunksBuffer[theOnlyChunksBufferPos++] = storagePos;
				}
			} else {
				baseSingleSamplesCount++;
			}
		}

		const framesBuffer = allocateHugeArray();
		framesBuffer[0] = 1;    // frames count on this level

		framesBuffer[1] = 0;    // methodId
		framesBuffer[2] = 0;    // x
		framesBuffer[3] = count;
		framesBuffer[4] = theOnlyChunksCount;
		framesBuffer[5] = singleSamplesCount;
		framesBuffer[6] = baseCount;
		framesBuffer[7] = theOnlyChunksBufferPos - theOnlyChunksCount;
		framesBuffer[8] = baseSingleSamplesCount;

		let framesBufferPos = 9;

		for (let storagePosIndex = 0; storagePosIndex < theOnlyChunksCount; storagePosIndex++) {
			const storagePos = theOnlyChunksBuffer[storagePosIndex];
			framesBuffer[framesBufferPos++] = storagePos;
			framesBuffer[framesBufferPos++] = theOnlyChunks[storagePos];
		}

		for (let sampleIndex = countBeforeFirstBlock; sampleIndex < countAtLastBlock; sampleIndex++) {
			if (filterOut(sampleIndex)) {
				continue;
			}
			const chunkPos = sampleToChunkEnds[sampleIndex - 1] || 0;
			const chunkEndPos = sampleToChunkEnds[sampleIndex];
			if (chunkPos + 1 !== chunkEndPos) {
				sampleToChunkPos[sampleIndex] = chunkEndPos - 1;
				sampleToStorageDelta[sampleIndex] = 0x80000000;

				framesBuffer[framesBufferPos++] = sampleIndex;
			}
		}

		for (let storagePosIndex = theOnlyChunksCount; storagePosIndex < theOnlyChunksBufferPos; storagePosIndex++) {
			const storagePos = theOnlyChunksBuffer[storagePosIndex];
			framesBuffer[framesBufferPos++] = storagePos;
			framesBuffer[framesBufferPos++] = baseTheOnlyChunks[storagePos];
		}

		for (let sampleIndex = baseCountBeforeFirstBlock; sampleIndex < baseCountAtLastBlock; sampleIndex++) {
			if (filterOut(sampleIndex)) {
				continue;
			}
			const chunkPos = sampleToChunkEnds[sampleIndex - 1] || 0;
			const chunkEndPos = sampleToChunkEnds[sampleIndex];
			if (chunkPos + 1 !== chunkEndPos) {
				if (sampleToStorageDelta[sampleIndex] === 0) {
					sampleToChunkPos[sampleIndex] = chunkEndPos - 1;
					sampleToStorageDelta[sampleIndex] = 0x80000000;
				}
				framesBuffer[framesBufferPos++] = sampleIndex;
			}
		}

		return [framesBuffer, sampleToChunkPos, sampleToStorageDelta];
	}

	function filterOut(sample) {
		if (!filterFrames) {
			return false;
		}
		const sampleMarks = currentHeatmap.blocksData.sampleMarks;
		return (sampleMarks[sample >> 5] & (1 << (sample & 31))) === 0;
	}

	function nextFrames(ctx) {
		const frames = ctx.frames;
		const nextFrames = ctx.nextFrames;

		ctx.startX = 0;
		ctx.theOnlyChunksCount = 0;
		ctx.longSamplesChunksCount = 0;
		ctx.directSamplesCount = 0;

		ctx.nextFramesPointer = 1; // one reserved to place nextFramesCount
		ctx.nextFramesCount = 0;

		let fp = 0;
		const framesCount = frames[fp++];

		const roots = new Array(framesCount);
		for (let frame = 0; frame < framesCount; frame++) {
			const methodId = frames[fp++];
			const x = frames[fp++];
			const childrenCount = frames[fp++];

			ctx.startX = x;
			ctx.theOnlyChunksCount = frames[fp++];
			ctx.longSamplesChunksCount = frames[fp++];
			ctx.directSamplesCount = frames[fp++];

			roots[frame] = {
				left: x,
				width: childrenCount,
				color: methods.c[methodId],
				title: methods.n[methodId],
				details: methods.b[methodId],
				method: methodId
			};

			ctx.framesPointer = fp;
			ctx.methodsMapFirstPos = ctx.nextFrames.length;
			processFrame(ctx)
			fp = ctx.framesPointer;
		}

		nextFrames[0] = ctx.nextFramesCount;

		return roots;
	}

	function nextFramesDiff(ctx) {
		const frames = ctx.frames;
		const nextFrames = ctx.nextFrames;

		ctx.startX = 0;
		ctx.theOnlyChunksCount = 0;
		ctx.directSamplesCount = 0;

		ctx.nextFramesPointer = 1; // one reserved to place nextFramesCount
		ctx.nextFramesCount = 0;

		let fp = 0;
		const framesCount = frames[fp++];

		const roots = new Array(framesCount);
		for (let frame = 0; frame < framesCount; frame++) {
			const methodId = frames[fp++];
			let x = frames[fp++];

			const childrenCount = frames[fp++];
			const theOnlyChunksCount = frames[fp++];
			const directSamplesCount = frames[fp++];

			const baseChildrenCount = frames[fp++];
			const baseTheOnlyChunksCount = frames[fp++];
			const baseDirectSamplesCount = frames[fp++];

			ctx.startX = x;
			ctx.theOnlyChunksCount = theOnlyChunksCount;
			ctx.directSamplesCount = directSamplesCount;
			ctx.baseChildrenCount = baseChildrenCount;
			ctx.baseTheOnlyChunksCount = baseTheOnlyChunksCount;
			ctx.baseDirectSamplesCount = baseDirectSamplesCount;

			roots[frame] = {
				left: x,
				width: childrenCount,
				baseWidth: baseChildrenCount,
				color: methods.c[methodId],
				title: methods.n[methodId],
				details: methods.b[methodId],
				method: methodId,
			};

			ctx.framesPointer = fp;
			ctx.methodsMapFirstPos = ctx.nextFrames.length;
			processFrameDiff(ctx)
			fp = ctx.framesPointer;
		}

		nextFrames[0] = ctx.nextFramesCount;

		return roots;
	}

	function nextFramesReversed(ctx) {
		const frames = ctx.frames;
		const nextFrames = ctx.nextFrames;

		ctx.startX = 0;
		ctx.theOnlyChunksCount = 0;
		ctx.directSamplesCount = 0;

		ctx.nextFramesPointer = 1; // one reserved to place nextFramesCount
		ctx.nextFramesCount = 0;

		let fp = 0;
		const framesCount = frames[fp++];

		const roots = new Array(framesCount);
		for (let frame = 0; frame < framesCount; frame++) {
			const methodId = frames[fp++];
			const x = frames[fp++];
			const childrenCount = frames[fp++];

			ctx.startX = x;
			ctx.theOnlyChunksCount = frames[fp++];
			ctx.directSamplesCount = frames[fp++];

			roots[frame] = {
				left: x,
				width: childrenCount,
				color: methods.c[methodId],
				title: methods.n[methodId],
				details: methods.b[methodId],
				method: methodId
			};

			ctx.framesPointer = fp;
			ctx.methodsMapFirstPos = ctx.nextFrames.length;
			processFrameReversed(ctx)
			fp = ctx.framesPointer;
		}

		nextFrames[0] = ctx.nextFramesCount;

		return roots;
	}

	function nextFramesReversedDiff(ctx) {
		const frames = ctx.frames;
		const nextFrames = ctx.nextFrames;

		ctx.startX = 0;
		ctx.theOnlyChunksCount = 0;
		ctx.directSamplesCount = 0;

		ctx.nextFramesPointer = 1; // one reserved to place nextFramesCount
		ctx.nextFramesCount = 0;

		let fp = 0;
		const framesCount = frames[fp++];

		const roots = new Array(framesCount);
		for (let frame = 0; frame < framesCount; frame++) {
			const methodId = frames[fp++];
			let x = frames[fp++];

			const childrenCount = frames[fp++];
			const theOnlyChunksCount = frames[fp++];
			const directSamplesCount = frames[fp++];

			const baseChildrenCount = frames[fp++];
			const baseTheOnlyChunksCount = frames[fp++];
			const baseDirectSamplesCount = frames[fp++];

			ctx.startX = x;
			ctx.theOnlyChunksCount = theOnlyChunksCount;
			ctx.directSamplesCount = directSamplesCount;
			ctx.baseChildrenCount = baseChildrenCount;
			ctx.baseTheOnlyChunksCount = baseTheOnlyChunksCount;
			ctx.baseDirectSamplesCount = baseDirectSamplesCount;

			roots[frame] = {
				left: x,
				width: childrenCount,
				baseWidth: baseChildrenCount,
				color: methods.c[methodId],
				title: methods.n[methodId],
				details: methods.b[methodId],
				method: methodId,
			};

			ctx.framesPointer = fp;
			ctx.methodsMapFirstPos = ctx.nextFrames.length;
			processFrameReversedDiff(ctx)
			fp = ctx.framesPointer;
		}

		nextFrames[0] = ctx.nextFramesCount;

		return roots;
	}

	function processFrame(ctx) {
		const startFramesPointer = ctx.framesPointer;

		// the main idea is to go through the samples and calculate total amount of samples for every method, using method buffers
		let totalChildren = 0;
		// calculates count of each method in methodsBufferTheOnlyChunks (for the-only-one-chunk samples)
		totalChildren += prepareTheOnlyChunks(ctx);
		// calculates count of each method in methodsBufferLongSamples (for long samples, that shares the first chunk)
		totalChildren += prepareLongSamplesChunks(ctx);
		// calculates count of each method in methodsBufferDirectSamples (for direct samples, expanded to list of methods)
		totalChildren += prepareDirectSamples(ctx);

		if (totalChildren === 0) {
			return;
		}

		// frames are sorted from more frequent to less frequent
		sortFramesForWrite(ctx);
		// writes frames data and reserves place for splitting samples between methods
		writeNextFrames(ctx);

		// the main idea is to go through the samples again and split them by methods into prepared buffer
		ctx.framesPointer = startFramesPointer;
		// splits the-only-one-chunk samples, skips finished samples
		splitTheOnlyChunks(ctx);
		// splits long samples, unpacks finished chunks to direct samples
		splitLongSamplesChunks(ctx);
		// splits direct samples, skips finished samples
		splitDirectSamples(ctx);

		// cleans buffers and moves nextFramesPointer
		cleanupMethodBuffers(ctx);

		const methodCount = ctx.nextFrames.length - ctx.methodsMapFirstPos;
		ctx.nextFramesCount += methodCount;
	}

	function processFrameDiff(ctx) {
		const startFramesPointer = ctx.framesPointer;

		// the main idea is to go through the samples and calculate total amount of samples for every method, using method buffers
		let totalChildren = 0;
		// calculates count of each method in methodsBufferTheOnlyChunks (for the-only-one-chunk samples)
		totalChildren += prepareTheOnlyChunks(ctx);

		// NOTE: there is no support for long samples from several chunks for diffs, they are split to direct samples.
		// It gives only 10% performance, so it is not critical for any practical case of using diffs.

		// calculates count of each method in methodsBufferDirectSamples (for direct samples, expanded to list of methods)
		totalChildren += prepareDirectSamplesDiff(ctx);

		const startBaseFramesPointer = ctx.framesPointer;
		// calculates count of each method in baseMethodsBufferTheOnlyChunks (for the-only-one-chunk samples of base)
		prepareBaseTheOnlyChunks(ctx);
		// calculates count of each method in baseMethodsBufferDirectSamples (for direct samples of base, expanded to list of methods)
		prepareBaseDirectSamples(ctx);

		if (totalChildren === 0) {
			return;
		}

		const endFramesPointer = ctx.framesPointer;

		// frames are sorted from more frequent to less frequent
		sortFramesForWrite(ctx);
		// writes frames data and reserves place for splitting samples between methods
		writeNextFramesDiff(ctx);

		// the main idea is to go through the samples again and split them by methods into prepared buffer
		// we need to start from base methods to handle the case when the same sample contained both in base and current
		ctx.framesPointer = startBaseFramesPointer;
		splitBaseTheOnlyChunks(ctx);
		splitBaseDirectSamples(ctx);

		// the main idea is to go through the samples again and split them by methods into prepared buffer
		ctx.framesPointer = startFramesPointer;
		// splits the-only-one-chunk samples, skips finished samples
		splitTheOnlyChunks(ctx);
		// splits direct samples, skips finished samples
		splitDirectSamplesDiff(ctx);

		// cleans buffers and moves nextFramesPointer
		cleanupMethodBuffersDiff(ctx);

		const methodCount = ctx.nextFrames.length - ctx.methodsMapFirstPos;
		ctx.nextFramesCount += methodCount;
		ctx.framesPointer = endFramesPointer;
	}

	function processFrameReversed(ctx) {
		const startFramesPointer = ctx.framesPointer;

		// the main idea is to go through the samples and calculate total amount of samples for every method, using method buffers
		let totalChildren = 0;
		// calculates count of each method in methodsBufferTheOnlyChunks (for the-only-one-chunk samples)
		totalChildren += prepareTheOnlyChunksReversed(ctx);
		// calculates count of each method in methodsBufferDirectSamples (for direct samples, expanded to list of methods)
		totalChildren += prepareDirectSamplesReversed(ctx);

		if (totalChildren === 0) {
			return;
		}

		// frames are sorted from more frequent to less frequent
		sortFramesForWrite(ctx);
		// writes frames data and reserves place for splitting samples between methods
		writeNextFramesReversed(ctx);

		// the main idea is to go through the samples again and split them by methods into prepared buffer
		ctx.framesPointer = startFramesPointer;
		// splits the-only-one-chunk samples, skips finished samples
		splitTheOnlyChunksReversed(ctx);
		// splits direct samples, skips finished samples
		splitDirectSamplesReversed(ctx);

		// cleans buffers and moves nextFramesPointer
		cleanupMethodBuffersReversed(ctx);

		const methodCount = ctx.nextFrames.length - ctx.methodsMapFirstPos;
		ctx.nextFramesCount += methodCount;
	}

	function processFrameReversedDiff(ctx) {
		const startFramesPointer = ctx.framesPointer;

		// the main idea is to go through the samples and calculate total amount of samples for every method, using method buffers
		let totalChildren = 0;
		// calculates count of each method in methodsBufferTheOnlyChunks (for the-only-one-chunk samples)
		totalChildren += prepareTheOnlyChunksReversed(ctx);

		// calculates count of each method in methodsBufferDirectSamples (for direct samples, expanded to list of methods)
		totalChildren += prepareDirectSamplesReversedDiff(ctx);

		const startBaseFramesPointer = ctx.framesPointer;
		// calculates count of each method in baseMethodsBufferTheOnlyChunks (for the-only-one-chunk samples of base)
		prepareBaseTheOnlyChunksReversed(ctx);
		// calculates count of each method in baseMethodsBufferDirectSamples (for direct samples of base, expanded to list of methods)
		prepareBaseDirectSamplesReversed(ctx);

		if (totalChildren === 0) {
			return;
		}

		const endFramesPointer = ctx.framesPointer;

		// frames are sorted from more frequent to less frequent
		sortFramesForWrite(ctx);
		// writes frames data and reserves place for splitting samples between methods
		writeNextFramesDiff(ctx);

		// the main idea is to go through the samples again and split them by methods into prepared buffer
		// we need to start from base methods to handle the case when the same sample contained both in base and current
		ctx.framesPointer = startBaseFramesPointer;
		splitBaseTheOnlyChunksReversed(ctx);
		splitBaseDirectSamplesReversed(ctx);

		// the main idea is to go through the samples again and split them by methods into prepared buffer
		ctx.framesPointer = startFramesPointer;
		// splits the-only-one-chunk samples, skips finished samples
		splitTheOnlyChunksReversed(ctx);
		// splits direct samples, skips finished samples
		splitDirectSamplesReversedDiff(ctx);

		// cleans buffers and moves nextFramesPointer
		cleanupMethodBuffersDiff(ctx);

		const methodCount = ctx.nextFrames.length - ctx.methodsMapFirstPos;
		ctx.nextFramesCount += methodCount;
		ctx.framesPointer = endFramesPointer;
	}

	function prepareTheOnlyChunks(ctx) {
		const frames = ctx.frames;
		const nextFrames = ctx.nextFrames;
		const level = ctx.level;
		const storage = ctx.storage;
		const storageSizes = ctx.storageSizes;
		const methodsBuffer = ctx.methodsBuffer;
		const methodsBufferTheOnlyChunks = ctx.methodsBufferTheOnlyChunks;

		const theOnlyChunksCount = ctx.theOnlyChunksCount;

		const levelPlusOne = level + 1;

		let fp = ctx.framesPointer;
		let methodsMapFirstPos = ctx.methodsMapFirstPos;

		let children = 0;
		for (let child = 0; child < theOnlyChunksCount; child++) {
			const storagePos = frames[fp++];
			const count = frames[fp++];
			const size = storageSizes[storagePos];
			if (size === level) {
				continue;
			}
			const methodId = storage[storagePos + size - levelPlusOne];

			if ((methodsBuffer[methodId] += count) === count) {
				nextFrames[--methodsMapFirstPos] = methodId;
			}
			methodsBufferTheOnlyChunks[methodId]++;

			children++;
		}

		ctx.framesPointer = fp;
		ctx.methodsMapFirstPos = methodsMapFirstPos;

		return children;
	}

	function prepareTheOnlyChunksReversed(ctx) {
		const frames = ctx.frames;
		const nextFrames = ctx.nextFrames;
		const level = ctx.level;
		const storage = ctx.storage;
		const storageSizes = ctx.storageSizes;
		const methodsBuffer = ctx.methodsBuffer;
		const methodsBufferTheOnlyChunks = ctx.methodsBufferTheOnlyChunks;

		const theOnlyChunksCount = ctx.theOnlyChunksCount;

		let fp = ctx.framesPointer;
		let methodsMapFirstPos = ctx.methodsMapFirstPos;

		let children = 0;
		for (let child = 0; child < theOnlyChunksCount; child++) {
			const storagePos = frames[fp++];
			const count = frames[fp++];
			const size = storageSizes[storagePos];
			if (size === level) {
				continue;
			}
			const methodId = storage[storagePos + level];

			if ((methodsBuffer[methodId] += count) === count) {
				nextFrames[--methodsMapFirstPos] = methodId;
			}
			methodsBufferTheOnlyChunks[methodId]++;

			children++;
		}

		ctx.framesPointer = fp;
		ctx.methodsMapFirstPos = methodsMapFirstPos;

		return children;
	}

	function prepareBaseTheOnlyChunks(ctx) {
		const frames = ctx.frames;
		const level = ctx.level;
		const storage = ctx.storage;
		const storageSizes = ctx.storageSizes;
		const methodsBuffer = ctx.methodsBuffer;
		const baseMethodsBuffer = ctx.baseMethodsBuffer;
		const baseMethodsBufferTheOnlyChunks = ctx.baseMethodsBufferTheOnlyChunks;

		const baseTheOnlyChunksCount = ctx.baseTheOnlyChunksCount;

		const levelPlusOne = level + 1;

		let fp = ctx.framesPointer;

		for (let child = 0; child < baseTheOnlyChunksCount; child++) {
			const storagePos = frames[fp++];
			const count = frames[fp++];
			const size = storageSizes[storagePos];
			if (size === level) {
				continue;
			}
			const methodId = storage[storagePos + size - levelPlusOne];

			if (methodsBuffer[methodId] !== 0) {
				baseMethodsBuffer[methodId] += count;
				baseMethodsBufferTheOnlyChunks[methodId]++;
			}
		}

		ctx.framesPointer = fp;
	}

	function prepareBaseTheOnlyChunksReversed(ctx) {
		const frames = ctx.frames;
		const level = ctx.level;
		const storage = ctx.storage;
		const storageSizes = ctx.storageSizes;
		const methodsBuffer = ctx.methodsBuffer;
		const baseMethodsBuffer = ctx.baseMethodsBuffer;
		const baseMethodsBufferTheOnlyChunks = ctx.baseMethodsBufferTheOnlyChunks;

		const baseTheOnlyChunksCount = ctx.baseTheOnlyChunksCount;

		let fp = ctx.framesPointer;

		for (let child = 0; child < baseTheOnlyChunksCount; child++) {
			const storagePos = frames[fp++];
			const count = frames[fp++];
			const size = storageSizes[storagePos];
			if (size === level) {
				continue;
			}
			const methodId = storage[storagePos + level];

			if (methodsBuffer[methodId] !== 0) {
				baseMethodsBuffer[methodId] += count;
				baseMethodsBufferTheOnlyChunks[methodId]++;
			}
		}

		ctx.framesPointer = fp;
	}

	function prepareLongSamplesChunks(ctx) {
		const frames = ctx.frames;
		const nextFrames = ctx.nextFrames;
		const longSamplesBuffer = ctx.longSamplesBuffer;
		const level = ctx.level;
		const chunksToStorage = ctx.chunksToStorage;
		const storage = ctx.storage;
		const sampleToChunkEnds = ctx.sampleToChunkEnds;
		const storageSizes = ctx.storageSizes;
		const methodsBuffer = ctx.methodsBuffer;
		const methodsBufferLongSamples = ctx.methodsBufferLongSamples;
		const methodsBufferDirectSamples = ctx.methodsBufferDirectSamples;

		const longSamplesChunksCount = ctx.longSamplesChunksCount;

		const levelPlusOne = level + 1;
		let children = 0;

		let fp = ctx.framesPointer;
		let methodsMapFirstPos = ctx.methodsMapFirstPos;

		for (let child = 0; child < longSamplesChunksCount; child++) {
			const storagePos = frames[fp++];
			const count = frames[fp++];
			const longSamplesBufferPos = frames[fp++];
			const size = storageSizes[storagePos];
			if (size === level) {
				for (let child = longSamplesBufferPos + count - 1; child >= longSamplesBufferPos; child--) {
					const sampleIndex = longSamplesBuffer[child];

					const chunkPos = (sampleToChunkEnds[sampleIndex - 1] || 0) + 1;

					const storagePos = chunksToStorage[chunkPos];
					const methodId = storage[storagePos + storageSizes[storagePos] - 1];

					if (methodsBuffer[methodId]++ === 0) {
						nextFrames[--methodsMapFirstPos] = methodId;
					}

					methodsBufferDirectSamples[methodId]++;
					children++;
				}
				continue;
			}
			const methodId = storage[storagePos + size - levelPlusOne];

			if ((methodsBuffer[methodId] += count) === count) {
				nextFrames[--methodsMapFirstPos] = methodId;
			}
			methodsBufferLongSamples[methodId]++;

			children++;
		}

		ctx.framesPointer = fp;
		ctx.methodsMapFirstPos = methodsMapFirstPos;

		return children;
	}

	function prepareDirectSamples(ctx) {
		const frames = ctx.frames;
		const nextFrames = ctx.nextFrames;
		const sampleToChunkPos = ctx.sampleToChunkPos;
		const sampleToStorageDelta = ctx.sampleToStorageDelta;
		const level = ctx.level;
		const chunksToStorage = ctx.chunksToStorage;
		const storage = ctx.storage;
		const methodsBuffer = ctx.methodsBuffer;
		const methodsBufferDirectSamples = ctx.methodsBufferDirectSamples;

		const directSamplesCount = ctx.directSamplesCount;

		let children = 0;

		let fp = ctx.framesPointer;
		let methodsMapFirstPos = ctx.methodsMapFirstPos;

		for (let child = 0; child < directSamplesCount; child++) {
			const sampleIndex = frames[fp++];
			const storageDelta = sampleToStorageDelta[sampleIndex] - level;
			if (storageDelta <= 0) {
				continue;
			}

			const chunkPos = sampleToChunkPos[sampleIndex];
			const storageStartPos = chunksToStorage[chunkPos];

			const storagePos = storageStartPos + storageDelta - 1;

			const methodId = storage[storagePos];

			if (methodsBuffer[methodId]++ === 0) {
				nextFrames[--methodsMapFirstPos] = methodId;
			}
			methodsBufferDirectSamples[methodId]++;

			children++;
		}

		ctx.framesPointer = fp;
		ctx.methodsMapFirstPos = methodsMapFirstPos;

		return children;
	}

	function prepareDirectSamplesDiff(ctx) {
		const frames = ctx.frames;
		const nextFrames = ctx.nextFrames;
		const sampleToChunkPos = ctx.sampleToChunkPos;
		const sampleToStorageDelta = ctx.sampleToStorageDelta;
		const level = ctx.level;
		const chunksToStorage = ctx.chunksToStorage;
		const storage = ctx.storage;
		const methodsBuffer = ctx.methodsBuffer;
		const methodsBufferDirectSamples = ctx.methodsBufferDirectSamples;

		const directSamplesCount = ctx.directSamplesCount;

		let children = 0;

		let fp = ctx.framesPointer;
		let methodsMapFirstPos = ctx.methodsMapFirstPos;

		for (let child = 0; child < directSamplesCount; child++) {
			const sampleIndex = frames[fp++];
			const storageDelta = (sampleToStorageDelta[sampleIndex] & 0x7fffffff) - level;
			if (storageDelta <= 0) {
				continue;
			}

			const chunkPos = sampleToChunkPos[sampleIndex]
			const storageStartPos = chunksToStorage[chunkPos];

			const storagePos = storageStartPos + storageDelta - 1;

			const methodId = storage[storagePos];

			if (methodsBuffer[methodId]++ === 0) {
				nextFrames[--methodsMapFirstPos] = methodId;
			}
			methodsBufferDirectSamples[methodId]++;

			children++;
		}

		ctx.framesPointer = fp;
		ctx.methodsMapFirstPos = methodsMapFirstPos;

		return children;
	}

	function prepareDirectSamplesReversed(ctx) {
		const frames = ctx.frames;
		const nextFrames = ctx.nextFrames;
		const sampleToChunkPos = ctx.sampleToChunkPos;
		const sampleToStorageDelta = ctx.sampleToStorageDelta;
		const level = ctx.level;
		const chunksToStorage = ctx.chunksToStorage;
		const storageSizes = ctx.storageSizes;
		const storage = ctx.storage;
		const methodsBuffer = ctx.methodsBuffer;
		const methodsBufferDirectSamples = ctx.methodsBufferDirectSamples;

		const directSamplesCount = ctx.directSamplesCount;

		let children = 0;

		let fp = ctx.framesPointer;
		let methodsMapFirstPos = ctx.methodsMapFirstPos;

		for (let child = 0; child < directSamplesCount; child++) {
			const sampleIndex = frames[fp++];
			const storageDelta = level - sampleToStorageDelta[sampleIndex];

			const chunkPos = sampleToChunkPos[sampleIndex];
			const storageStartPos = chunksToStorage[chunkPos];
			if (storageSizes[storageStartPos] <= storageDelta) {
				continue;
			}

			const methodId = storage[storageStartPos + storageDelta];

			if (methodsBuffer[methodId]++ === 0) {
				nextFrames[--methodsMapFirstPos] = methodId;
			}
			methodsBufferDirectSamples[methodId]++;

			children++;
		}

		ctx.framesPointer = fp;
		ctx.methodsMapFirstPos = methodsMapFirstPos;

		return children;
	}

	function prepareDirectSamplesReversedDiff(ctx) {
		const frames = ctx.frames;
		const nextFrames = ctx.nextFrames;
		const sampleToChunkPos = ctx.sampleToChunkPos;
		const sampleToStorageDelta = ctx.sampleToStorageDelta;
		const level = ctx.level;
		const chunksToStorage = ctx.chunksToStorage;
		const storageSizes = ctx.storageSizes;
		const storage = ctx.storage;
		const methodsBuffer = ctx.methodsBuffer;
		const methodsBufferDirectSamples = ctx.methodsBufferDirectSamples;

		const directSamplesCount = ctx.directSamplesCount;

		let children = 0;

		let fp = ctx.framesPointer;
		let methodsMapFirstPos = ctx.methodsMapFirstPos;

		for (let child = 0; child < directSamplesCount; child++) {
			const sampleIndex = frames[fp++];
			const storageDelta = level - (sampleToStorageDelta[sampleIndex] & 0x7fffffff);

			const chunkPos = sampleToChunkPos[sampleIndex];
			const storageStartPos = chunksToStorage[chunkPos];
			if (storageSizes[storageStartPos] <= storageDelta) {
				continue;
			}

			const methodId = storage[storageStartPos + storageDelta];

			if (methodsBuffer[methodId]++ === 0) {
				nextFrames[--methodsMapFirstPos] = methodId;
			}
			methodsBufferDirectSamples[methodId]++;

			children++;
		}

		ctx.framesPointer = fp;
		ctx.methodsMapFirstPos = methodsMapFirstPos;

		return children;
	}

	function prepareBaseDirectSamples(ctx) {
		const frames = ctx.frames;
		const sampleToChunkPos = ctx.sampleToChunkPos;
		const sampleToStorageDelta = ctx.sampleToStorageDelta;
		const level = ctx.level;
		const chunksToStorage = ctx.chunksToStorage;
		const storage = ctx.storage;
		const methodsBuffer = ctx.methodsBuffer;
		const baseMethodsBuffer = ctx.baseMethodsBuffer;
		const baseMethodsBufferDirectSamples = ctx.baseMethodsBufferDirectSamples;

		const baseDirectSamplesCount = ctx.baseDirectSamplesCount;

		let fp = ctx.framesPointer;

		for (let child = 0; child < baseDirectSamplesCount; child++) {
			const sampleIndex = frames[fp++];
			const storageDelta = (sampleToStorageDelta[sampleIndex] & 0x7fffffff) - level;
			if (storageDelta <= 0) {
				continue;
			}

			const chunkPos = sampleToChunkPos[sampleIndex];
			const storageStartPos = chunksToStorage[chunkPos];

			const storagePos = storageStartPos + storageDelta - 1;

			const methodId = storage[storagePos];

			if (methodsBuffer[methodId] !== 0) {
				baseMethodsBuffer[methodId]++;
				baseMethodsBufferDirectSamples[methodId]++;
			}
		}

		ctx.framesPointer = fp;
	}

	function prepareBaseDirectSamplesReversed(ctx) {
		const frames = ctx.frames;
		const sampleToChunkPos = ctx.sampleToChunkPos;
		const sampleToStorageDelta = ctx.sampleToStorageDelta;
		const level = ctx.level;
		const chunksToStorage = ctx.chunksToStorage;
		const storage = ctx.storage;
		const storageSizes = ctx.storageSizes;
		const methodsBuffer = ctx.methodsBuffer;
		const baseMethodsBuffer = ctx.baseMethodsBuffer;
		const baseMethodsBufferDirectSamples = ctx.baseMethodsBufferDirectSamples;

		const baseDirectSamplesCount = ctx.baseDirectSamplesCount;

		let fp = ctx.framesPointer;

		for (let child = 0; child < baseDirectSamplesCount; child++) {
			const sampleIndex = frames[fp++];
			const storageDelta = level - (sampleToStorageDelta[sampleIndex] & 0x7fffffff);

			const chunkPos = sampleToChunkPos[sampleIndex];
			const storageStartPos = chunksToStorage[chunkPos];
			if (storageSizes[storageStartPos] <= storageDelta) {
				continue;
			}

			const methodId = storage[storageStartPos + storageDelta];
			if (methodsBuffer[methodId] !== 0) {
				baseMethodsBuffer[methodId]++;
				baseMethodsBufferDirectSamples[methodId]++;
			}
		}

		ctx.framesPointer = fp;
	}

	function sortFramesForWrite(ctx) {
		const nextFrames = ctx.nextFrames;
		const methodsBuffer = ctx.methodsBuffer;
		const methodsMapFirstPos = ctx.methodsMapFirstPos;

		let maxCount = 0;
		for (let i = methodsMapFirstPos; i < nextFrames.length; i++) {
			maxCount = Math.max(maxCount, methodsBuffer[nextFrames[i]]);
		}

		sort(nextFrames, methodsMapFirstPos, nextFrames.length, methodsBuffer, 1 << (31 - Math.clz32(maxCount)));
	}

	function writeNextFrames(ctx) {
		const nextFrames = ctx.nextFrames;
		const methodsBuffer = ctx.methodsBuffer;
		const methodsBufferTheOnlyChunks = ctx.methodsBufferTheOnlyChunks;
		const methodsBufferLongSamples = ctx.methodsBufferLongSamples;
		const methodsBufferDirectSamples = ctx.methodsBufferDirectSamples;

		const methodsMapFirstPos = ctx.methodsMapFirstPos;

		let np = ctx.nextFramesPointer;
		let x = ctx.startX;

		for (let i = methodsMapFirstPos; i < nextFrames.length; i++) {
			const methodId = nextFrames[i];
			const count = methodsBuffer[methodId];
			const theOnlyChunksCountForMethod = methodsBufferTheOnlyChunks[methodId];
			const longSamplesChunksCountForMethod = methodsBufferLongSamples[methodId];
			const directSamplesCount = methodsBufferDirectSamples[methodId];

			nextFrames[np++] = methodId;
			nextFrames[np++] = x;
			nextFrames[np++] = count;
			nextFrames[np++] = theOnlyChunksCountForMethod;
			nextFrames[np++] = longSamplesChunksCountForMethod;
			nextFrames[np++] = directSamplesCount;

			x += count;
			methodsBufferTheOnlyChunks[methodId] = np;
			np += theOnlyChunksCountForMethod * 2;
			methodsBufferLongSamples[methodId] = np;
			np += longSamplesChunksCountForMethod * 3;
			methodsBufferDirectSamples[methodId] = np;
			np += directSamplesCount;
		}
	}

	function writeNextFramesReversed(ctx) {
		const nextFrames = ctx.nextFrames;
		const methodsBuffer = ctx.methodsBuffer;
		const methodsBufferTheOnlyChunks = ctx.methodsBufferTheOnlyChunks;
		const methodsBufferDirectSamples = ctx.methodsBufferDirectSamples;

		const methodsMapFirstPos = ctx.methodsMapFirstPos;

		let np = ctx.nextFramesPointer;
		let x = ctx.startX;

		for (let i = methodsMapFirstPos; i < nextFrames.length; i++) {
			const methodId = nextFrames[i];
			const count = methodsBuffer[methodId];
			const theOnlyChunksCountForMethod = methodsBufferTheOnlyChunks[methodId];
			const directSamplesCount = methodsBufferDirectSamples[methodId];

			nextFrames[np++] = methodId;
			nextFrames[np++] = x;
			nextFrames[np++] = count;
			nextFrames[np++] = theOnlyChunksCountForMethod;
			nextFrames[np++] = directSamplesCount;

			x += count;
			methodsBufferTheOnlyChunks[methodId] = np;
			np += theOnlyChunksCountForMethod * 2;
			methodsBufferDirectSamples[methodId] = np;
			np += directSamplesCount;
		}
	}

	function writeNextFramesDiff(ctx) {
		const nextFrames = ctx.nextFrames;
		const methodsBuffer = ctx.methodsBuffer;
		const methodsBufferTheOnlyChunks = ctx.methodsBufferTheOnlyChunks;
		const methodsBufferDirectSamples = ctx.methodsBufferDirectSamples;
		const baseMethodsBuffer = ctx.baseMethodsBuffer;
		const baseMethodsBufferTheOnlyChunks = ctx.baseMethodsBufferTheOnlyChunks;
		const baseMethodsBufferDirectSamples = ctx.baseMethodsBufferDirectSamples;

		const methodsMapFirstPos = ctx.methodsMapFirstPos;

		let np = ctx.nextFramesPointer;
		let x = ctx.startX;

		for (let i = methodsMapFirstPos; i < nextFrames.length; i++) {
			const methodId = nextFrames[i];
			const count = methodsBuffer[methodId];
			const theOnlyChunksCount = methodsBufferTheOnlyChunks[methodId];
			const directSamplesCount = methodsBufferDirectSamples[methodId];

			const baseCount = baseMethodsBuffer[methodId];
			const baseTheOnlyChunksCount = baseMethodsBufferTheOnlyChunks[methodId];
			const baseDirectSamplesCount = baseMethodsBufferDirectSamples[methodId];

			nextFrames[np++] = methodId;
			nextFrames[np++] = x;

			nextFrames[np++] = count;
			nextFrames[np++] = theOnlyChunksCount;
			nextFrames[np++] = directSamplesCount;

			nextFrames[np++] = baseCount;
			nextFrames[np++] = baseTheOnlyChunksCount;
			nextFrames[np++] = baseDirectSamplesCount;

			x += count;

			methodsBufferTheOnlyChunks[methodId] = np;
			np += theOnlyChunksCount * 2;

			methodsBufferDirectSamples[methodId] = np;
			np += directSamplesCount;

			baseMethodsBufferTheOnlyChunks[methodId] = np;
			np += baseTheOnlyChunksCount * 2;

			baseMethodsBufferDirectSamples[methodId] = np;
			np += baseDirectSamplesCount;
		}
	}

	function splitTheOnlyChunks(ctx) {
		const frames = ctx.frames;
		const nextFrames = ctx.nextFrames;
		const level = ctx.level;
		const storage = ctx.storage;
		const storageSizes = ctx.storageSizes;
		const methodsBufferTheOnlyChunks = ctx.methodsBufferTheOnlyChunks;

		const theOnlyChunksCount = ctx.theOnlyChunksCount;
		const levelPlusOne = level + 1;

		let fp = ctx.framesPointer;
		for (let child = 0; child < theOnlyChunksCount; child++) {
			const storagePos = frames[fp++];
			const count = frames[fp++];
			const size = storageSizes[storagePos];
			if (size === level) {
				continue;
			}

			const methodId = storage[storagePos + size - levelPlusOne];

			nextFrames[methodsBufferTheOnlyChunks[methodId]++] = storagePos;
			nextFrames[methodsBufferTheOnlyChunks[methodId]++] = count;
		}
		ctx.framesPointer = fp;
	}

	function splitTheOnlyChunksReversed(ctx) {
		const frames = ctx.frames;
		const nextFrames = ctx.nextFrames;
		const level = ctx.level;
		const storage = ctx.storage;
		const storageSizes = ctx.storageSizes;
		const methodsBufferTheOnlyChunks = ctx.methodsBufferTheOnlyChunks;

		const theOnlyChunksCount = ctx.theOnlyChunksCount;

		let fp = ctx.framesPointer;
		for (let child = 0; child < theOnlyChunksCount; child++) {
			const storagePos = frames[fp++];
			const count = frames[fp++];
			const size = storageSizes[storagePos];
			if (size === level) {
				continue;
			}

			const methodId = storage[storagePos + level];

			nextFrames[methodsBufferTheOnlyChunks[methodId]++] = storagePos;
			nextFrames[methodsBufferTheOnlyChunks[methodId]++] = count;
		}
		ctx.framesPointer = fp;
	}

	function splitBaseTheOnlyChunks(ctx) {
		const frames = ctx.frames;
		const nextFrames = ctx.nextFrames;
		const level = ctx.level;
		const storage = ctx.storage;
		const storageSizes = ctx.storageSizes;
		const methodsBuffer = ctx.methodsBuffer;
		const baseMethodsBufferTheOnlyChunks = ctx.baseMethodsBufferTheOnlyChunks;

		const baseTheOnlyChunksCount = ctx.baseTheOnlyChunksCount;
		const levelPlusOne = level + 1;

		let fp = ctx.framesPointer;
		for (let child = 0; child < baseTheOnlyChunksCount; child++) {
			const storagePos = frames[fp++];
			const count = frames[fp++];
			const size = storageSizes[storagePos];
			if (size === level) {
				continue;
			}

			const methodId = storage[storagePos + size - levelPlusOne];

			if (methodsBuffer[methodId] !== 0) {
				nextFrames[baseMethodsBufferTheOnlyChunks[methodId]++] = storagePos;
				nextFrames[baseMethodsBufferTheOnlyChunks[methodId]++] = count;
			}
		}
		ctx.framesPointer = fp;
	}

	function splitBaseTheOnlyChunksReversed(ctx) {
		const frames = ctx.frames;
		const nextFrames = ctx.nextFrames;
		const level = ctx.level;
		const storage = ctx.storage;
		const storageSizes = ctx.storageSizes;
		const methodsBuffer = ctx.methodsBuffer;
		const baseMethodsBufferTheOnlyChunks = ctx.baseMethodsBufferTheOnlyChunks;

		const baseTheOnlyChunksCount = ctx.baseTheOnlyChunksCount;

		let fp = ctx.framesPointer;
		for (let child = 0; child < baseTheOnlyChunksCount; child++) {
			const storagePos = frames[fp++];
			const count = frames[fp++];
			const size = storageSizes[storagePos];
			if (size === level) {
				continue;
			}

			const methodId = storage[storagePos + level];

			if (methodsBuffer[methodId] !== 0) {
				nextFrames[baseMethodsBufferTheOnlyChunks[methodId]++] = storagePos;
				nextFrames[baseMethodsBufferTheOnlyChunks[methodId]++] = count;
			}
		}
		ctx.framesPointer = fp;
	}

	function splitLongSamplesChunks(ctx) {
		const frames = ctx.frames;
		const nextFrames = ctx.nextFrames;
		const sampleToChunkPos = ctx.sampleToChunkPos;
		const sampleToStorageDelta = ctx.sampleToStorageDelta;
		const longSamplesBuffer = ctx.longSamplesBuffer;
		const level = ctx.level;
		const chunksToStorage = ctx.chunksToStorage;
		const storage = ctx.storage;
		const sampleToChunkEnds = ctx.sampleToChunkEnds;
		const storageSizes = ctx.storageSizes;
		const methodsBufferLongSamples = ctx.methodsBufferLongSamples;
		const methodsBufferDirectSamples = ctx.methodsBufferDirectSamples;

		const longSamplesChunksCount = ctx.longSamplesChunksCount;

		const levelPlusOne = level + 1;

		let fp = ctx.framesPointer;
		for (let child = 0; child < longSamplesChunksCount; child++) {
			const storagePos = frames[fp++];
			const count = frames[fp++];
			const longSamplesBufferPos = frames[fp++];
			const size = storageSizes[storagePos];
			if (size === level) {
				for (let child = longSamplesBufferPos + count - 1; child >= longSamplesBufferPos; child--) {
					const sampleIndex = longSamplesBuffer[child];

					let chunkPos = (sampleToChunkEnds[sampleIndex - 1] || 0) + 1;
					const storagePos = chunksToStorage[chunkPos];
					const storageSize = storageSizes[storagePos];
					sampleToChunkPos[sampleIndex] = chunkPos;
					sampleToStorageDelta[sampleIndex] = storageSize + levelPlusOne;
					let storageDelta = sampleToStorageDelta[sampleIndex] - levelPlusOne;
					if (storageDelta === 1) {
						const chunkEnd = sampleToChunkEnds[sampleIndex] || chunksToStorage.length;
						if (++chunkPos !== chunkEnd) {
							sampleToChunkPos[sampleIndex] = chunkPos;
							const storagePos = chunksToStorage[chunkPos];
							storageDelta = storageSizes[storagePos];
							sampleToStorageDelta[sampleIndex] = storageDelta + levelPlusOne;
						}
					}

					const methodId = storage[storagePos + storageSize - 1];

					nextFrames[methodsBufferDirectSamples[methodId]++] = sampleIndex;
				}
				continue;
			}

			const methodId = storage[storagePos + size - levelPlusOne];

			nextFrames[methodsBufferLongSamples[methodId]++] = storagePos;
			nextFrames[methodsBufferLongSamples[methodId]++] = count;
			nextFrames[methodsBufferLongSamples[methodId]++] = longSamplesBufferPos;
		}
		ctx.framesPointer = fp;
	}

	function splitDirectSamples(ctx) {
		const frames = ctx.frames;
		const nextFrames = ctx.nextFrames;
		const sampleToChunkPos = ctx.sampleToChunkPos;
		const sampleToStorageDelta = ctx.sampleToStorageDelta;
		const level = ctx.level;
		const chunksToStorage = ctx.chunksToStorage;
		const storage = ctx.storage;
		const sampleToChunkEnds = ctx.sampleToChunkEnds;
		const storageSizes = ctx.storageSizes;
		const methodsBufferDirectSamples = ctx.methodsBufferDirectSamples;

		const directSamplesCount = ctx.directSamplesCount;

		const levelPlusOne = level + 1;

		let fp = ctx.framesPointer;
		for (let child = 0; child < directSamplesCount; child++) {
			const sampleIndex = frames[fp++];
			let storageDelta = sampleToStorageDelta[sampleIndex] - level;
			if (storageDelta <= 0) {
				continue;
			}
			let chunkPos = sampleToChunkPos[sampleIndex];
			const storageStartPos = chunksToStorage[chunkPos];

			const storagePos = storageStartPos + storageDelta - 1;

			if (storageDelta === 1) {
				const chunkEnd = sampleToChunkEnds[sampleIndex] || chunksToStorage.length;
				if (++chunkPos !== chunkEnd) {
					sampleToChunkPos[sampleIndex] = chunkPos;
					const storagePos = chunksToStorage[chunkPos];
					storageDelta = storageSizes[storagePos];
					sampleToStorageDelta[sampleIndex] = storageDelta + levelPlusOne;
				}
			}

			const methodId = storage[storagePos];

			nextFrames[methodsBufferDirectSamples[methodId]++] = sampleIndex;
		}
		ctx.framesPointer = fp;
	}

	function splitDirectSamplesDiff(ctx) {
		const frames = ctx.frames;
		const nextFrames = ctx.nextFrames;
		const level = ctx.level;
		const storage = ctx.storage;
		const storageSizes = ctx.storageSizes;
		const sampleToStorageDelta = ctx.sampleToStorageDelta;
		const sampleToChunkPos = ctx.sampleToChunkPos;
		const chunksToStorage = ctx.chunksToStorage;
		const sampleToChunkEnds = ctx.sampleToChunkEnds;
		const methodsBufferDirectSamples = ctx.methodsBufferDirectSamples;

		const directSamplesCount = ctx.directSamplesCount;
		const levelPlusOne = level + 1;

		let fp = ctx.framesPointer;

		for (let child = 0; child < directSamplesCount; child++) {
			const sampleIndex = frames[fp++];
			let storageDelta = (sampleToStorageDelta[sampleIndex] & 0x7fffffff) - level;
			if (storageDelta <= 0) {
				sampleToStorageDelta[sampleIndex] = 0;
				continue;
			}
			let chunkPos = sampleToChunkPos[sampleIndex];
			const storageStartPos = chunksToStorage[chunkPos];

			const storagePos = storageStartPos + storageDelta - 1;

			if (storageDelta === 1) {
				const chunkEnd = sampleToChunkEnds[sampleIndex] || chunksToStorage.length;
				if (++chunkPos !== chunkEnd) {
					sampleToChunkPos[sampleIndex] = chunkPos;
					const storagePos = chunksToStorage[chunkPos];
					storageDelta = storageSizes[storagePos];
					sampleToStorageDelta[sampleIndex] = (storageDelta + levelPlusOne) | 0x80000000;
				}
			}

			const methodId = storage[storagePos];

			nextFrames[methodsBufferDirectSamples[methodId]++] = sampleIndex;
		}
		ctx.framesPointer = fp;
	}

	function splitDirectSamplesReversed(ctx) {
		const frames = ctx.frames;
		const nextFrames = ctx.nextFrames;
		const sampleToChunkPos = ctx.sampleToChunkPos;
		const sampleToStorageDelta = ctx.sampleToStorageDelta;
		const level = ctx.level;
		const chunksToStorage = ctx.chunksToStorage;
		const storage = ctx.storage;
		const sampleToChunkEnds = ctx.sampleToChunkEnds;
		const storageSizes = ctx.storageSizes;
		const methodsBufferDirectSamples = ctx.methodsBufferDirectSamples;

		const directSamplesCount = ctx.directSamplesCount;

		const levelPlusOne = level + 1;

		let fp = ctx.framesPointer;
		for (let child = 0; child < directSamplesCount; child++) {
			const sampleIndex = frames[fp++];
			const storageDelta = level - sampleToStorageDelta[sampleIndex];

			let chunkPos = sampleToChunkPos[sampleIndex];
			const storageStartPos = chunksToStorage[chunkPos];
			const storageSize = storageSizes[storageStartPos];
			if (storageSize <= storageDelta) {
				continue;
			}

			const storagePos = storageStartPos + storageDelta;

			if (storageDelta + 1 === storageSize) {
				const chunkStart = sampleToChunkEnds[sampleIndex - 1] || 0;
				if (--chunkPos >= chunkStart) {
					sampleToChunkPos[sampleIndex] = chunkPos;
					sampleToStorageDelta[sampleIndex] = levelPlusOne;
				}
			}

			const methodId = storage[storagePos];

			nextFrames[methodsBufferDirectSamples[methodId]++] = sampleIndex;
		}
		ctx.framesPointer = fp;
	}

	function splitDirectSamplesReversedDiff(ctx) {
		const frames = ctx.frames;
		const nextFrames = ctx.nextFrames;
		const level = ctx.level;
		const storage = ctx.storage;
		const storageSizes = ctx.storageSizes;
		const sampleToStorageDelta = ctx.sampleToStorageDelta;
		const sampleToChunkPos = ctx.sampleToChunkPos;
		const chunksToStorage = ctx.chunksToStorage;
		const sampleToChunkEnds = ctx.sampleToChunkEnds;
		const methodsBufferDirectSamples = ctx.methodsBufferDirectSamples;

		const directSamplesCount = ctx.directSamplesCount;
		const levelPlusOne = level + 1;

		let fp = ctx.framesPointer;

		for (let child = 0; child < directSamplesCount; child++) {
			const sampleIndex = frames[fp++];
			const delta = sampleToStorageDelta[sampleIndex] & 0x7fffffff;
			const storageDelta = level - delta;

			let chunkPos = sampleToChunkPos[sampleIndex];
			const storageStartPos = chunksToStorage[chunkPos];
			const storageSize = storageSizes[storageStartPos];
			if (storageSize <= storageDelta) {
				sampleToStorageDelta[sampleIndex] = delta;
				continue;
			}

			const storagePos = storageStartPos + storageDelta;

			if (storageDelta + 1 === storageSize) {
				const chunkStart = sampleToChunkEnds[sampleIndex - 1] || 0;
				if (--chunkPos >= chunkStart) {
					sampleToChunkPos[sampleIndex] = chunkPos;
					sampleToStorageDelta[sampleIndex] = levelPlusOne | 0x80000000;
				}
			}

			const methodId = storage[storagePos];

			nextFrames[methodsBufferDirectSamples[methodId]++] = sampleIndex;
		}
		ctx.framesPointer = fp;
	}

	function splitBaseDirectSamples(ctx) {
		const frames = ctx.frames;
		const nextFrames = ctx.nextFrames;
		const sampleToChunkPos = ctx.sampleToChunkPos;
		const sampleToStorageDelta = ctx.sampleToStorageDelta;
		const level = ctx.level;
		const chunksToStorage = ctx.chunksToStorage;
		const storage = ctx.storage;
		const sampleToChunkEnds = ctx.sampleToChunkEnds;
		const storageSizes = ctx.storageSizes;
		const methodsBuffer = ctx.methodsBuffer;
		const baseMethodsBufferDirectSamples = ctx.baseMethodsBufferDirectSamples;

		const baseDirectSamplesCount = ctx.baseDirectSamplesCount;

		const levelPlusOne = level + 1;

		let fp = ctx.framesPointer;

		for (let child = 0; child < baseDirectSamplesCount; child++) {
			const sampleIndex = frames[fp++];
			const baseStorageDelta = sampleToStorageDelta[sampleIndex];
			let storageDelta = (baseStorageDelta & 0x7fffffff) - level;
			if (storageDelta <= 0) {
				continue;
			}

			let chunkPos = sampleToChunkPos[sampleIndex];
			const storageStartPos = chunksToStorage[chunkPos];

			const storagePos = storageStartPos + storageDelta - 1;

			if (storageDelta === 1 &&
				// will be done for this sample by not-based step
				(baseStorageDelta & 0x80000000) === 0) {
				const chunkEnd = sampleToChunkEnds[sampleIndex] || chunksToStorage.length;
				if (++chunkPos !== chunkEnd) {
					sampleToChunkPos[sampleIndex] = chunkPos;
					const storagePos = chunksToStorage[chunkPos];
					storageDelta = storageSizes[storagePos];
					sampleToStorageDelta[sampleIndex] = storageDelta + levelPlusOne;
				}
			}

			const methodId = storage[storagePos];

			if (methodsBuffer[methodId] !== 0) {
				nextFrames[baseMethodsBufferDirectSamples[methodId]++] = sampleIndex;
			}
		}
		ctx.framesPointer = fp;
	}

	function splitBaseDirectSamplesReversed(ctx) {
		const frames = ctx.frames;
		const nextFrames = ctx.nextFrames;
		const sampleToChunkPos = ctx.sampleToChunkPos;
		const sampleToStorageDelta = ctx.sampleToStorageDelta;
		const level = ctx.level;
		const chunksToStorage = ctx.chunksToStorage;
		const storage = ctx.storage;
		const sampleToChunkEnds = ctx.sampleToChunkEnds;
		const storageSizes = ctx.storageSizes;
		const methodsBuffer = ctx.methodsBuffer;
		const baseMethodsBufferDirectSamples = ctx.baseMethodsBufferDirectSamples;

		const baseDirectSamplesCount = ctx.baseDirectSamplesCount;

		const levelPlusOne = level + 1;

		let fp = ctx.framesPointer;

		for (let child = 0; child < baseDirectSamplesCount; child++) {
			const sampleIndex = frames[fp++];
			const baseStorageDelta = sampleToStorageDelta[sampleIndex];
			const storageDelta = level - (baseStorageDelta & 0x7fffffff);

			let chunkPos = sampleToChunkPos[sampleIndex];
			const storageStartPos = chunksToStorage[chunkPos];
			const storageSize = storageSizes[storageStartPos];
			if (storageSize <= storageDelta) {
				continue;
			}

			const storagePos = storageStartPos + storageDelta;

			if (storageDelta + 1 === storageSize &&
				// will be done for this sample by not-based step
				(baseStorageDelta & 0x80000000) === 0) {
				const chunkStart = sampleToChunkEnds[sampleIndex - 1] || 0;
				if (--chunkPos >= chunkStart) {
					sampleToChunkPos[sampleIndex] = chunkPos;
					sampleToStorageDelta[sampleIndex] = levelPlusOne;
				}
			}

			const methodId = storage[storagePos];

			if (methodsBuffer[methodId] !== 0) {
				nextFrames[baseMethodsBufferDirectSamples[methodId]++] = sampleIndex;
			}
		}
		ctx.framesPointer = fp;
	}

	function cleanupMethodBuffers(ctx) {
		const nextFrames = ctx.nextFrames;
		const methodsBuffer = ctx.methodsBuffer;
		const methodsBufferTheOnlyChunks = ctx.methodsBufferTheOnlyChunks;
		const methodsBufferLongSamples = ctx.methodsBufferLongSamples;
		const methodsBufferDirectSamples = ctx.methodsBufferDirectSamples;

		let np = ctx.nextFramesPointer;
		let methodsMapFirstPos = ctx.methodsMapFirstPos;
		for (let i = methodsMapFirstPos; i < nextFrames.length; i++) {
			const methodId = nextFrames[np];

			methodsBuffer[methodId] = 0;
			methodsBufferTheOnlyChunks[methodId] = 0;
			methodsBufferLongSamples[methodId] = 0;
			methodsBufferDirectSamples[methodId] = 0;

			np += nextFrames[np + 3] * 2 + nextFrames[np + 4] * 3 + nextFrames[np + 5] + 6;
		}
		ctx.nextFramesPointer = np;
	}

	function cleanupMethodBuffersReversed(ctx) {
		const nextFrames = ctx.nextFrames;
		const methodsBuffer = ctx.methodsBuffer;
		const methodsBufferTheOnlyChunks = ctx.methodsBufferTheOnlyChunks;
		const methodsBufferDirectSamples = ctx.methodsBufferDirectSamples;

		let np = ctx.nextFramesPointer;
		let methodsMapFirstPos = ctx.methodsMapFirstPos;
		for (let i = methodsMapFirstPos; i < nextFrames.length; i++) {
			const methodId = nextFrames[np];

			methodsBuffer[methodId] = 0;
			methodsBufferTheOnlyChunks[methodId] = 0;
			methodsBufferDirectSamples[methodId] = 0;

			np += nextFrames[np + 3] * 2 + nextFrames[np + 4] + 5;
		}
		ctx.nextFramesPointer = np;
	}

	function cleanupMethodBuffersDiff(ctx) {
		const nextFrames = ctx.nextFrames;
		const methodsBuffer = ctx.methodsBuffer;
		const methodsBufferTheOnlyChunks = ctx.methodsBufferTheOnlyChunks;
		const methodsBufferDirectSamples = ctx.methodsBufferDirectSamples;
		const baseMethodsBuffer = ctx.baseMethodsBuffer;
		const baseMethodsBufferTheOnlyChunks = ctx.baseMethodsBufferTheOnlyChunks;
		const baseMethodsBufferDirectSamples = ctx.baseMethodsBufferDirectSamples;

		let np = ctx.nextFramesPointer;
		let methodsMapFirstPos = ctx.methodsMapFirstPos;
		for (let i = methodsMapFirstPos; i < nextFrames.length; i++) {
			const methodId = nextFrames[np];

			methodsBuffer[methodId] = 0;
			methodsBufferTheOnlyChunks[methodId] = 0;
			methodsBufferDirectSamples[methodId] = 0;

			baseMethodsBuffer[methodId] = 0;
			baseMethodsBufferTheOnlyChunks[methodId] = 0;
			baseMethodsBufferDirectSamples[methodId] = 0;

			np += (nextFrames[np + 3] + nextFrames[np + 6]) * 2 + (nextFrames[np + 4] + nextFrames[np + 7]) + 8;
		}
		ctx.nextFramesPointer = np;
	}

	function renderWithMatch(newCanvasHeight, root, level, minLevel) {
		newCanvasHeight = Math.min(16384 / (devicePixelRatio || 1), newCanvasHeight) | 0;
		if (canvasHeight !== newCanvasHeight) {
			canvasHeight = newCanvasHeight;
			canvas.style.height = canvasHeight + 'px';
			canvas.height = canvasHeight * (devicePixelRatio || 1);
			c = canvas.getContext('2d');
			if (devicePixelRatio) c.scale(devicePixelRatio, devicePixelRatio);
			c.font = document.body.style.font;
		}
		const matched = render(root, level, minLevel);
		displayMatched(matched);
	}

	function redrawHeatSamplesImpl(from, to, dx) {
		const startBlock = currentHeatmap.startBlock();

		const scale = currentHeatmap.timeSquareScale;
		const max = currentHeatmap.max(showFound);
		const min = currentHeatmap.min(showFound);
		const delta = Math.max(1, max - min);
		const counts = showFound ? currentHeatmap.blocksData.foundCounts : currentHeatmap.blocksData.counts;

		const r = showFound ? dRs : dR;
		const g = showFound ? dGs : dG;
		const b = showFound ? dBs : dB;

		for (let index = from; index <= to; index++) {
			let color;
			const firstCountsIndex = (index - startBlock) * scale;
			const afterLastCountsIndex = firstCountsIndex + scale;
			if (afterLastCountsIndex <= 0 || firstCountsIndex >= counts.length) {
				color = '#ddd';
			} else {
				const countBeforeFirstBlock = getCount(counts, firstCountsIndex - 1);
				const countAtLastBlock = getCount(counts, afterLastCountsIndex - 1);
				const count = countAtLastBlock - countBeforeFirstBlock;
				if (count === 0) {
					color = '#fff';
				} else {
					let ratio = Math.max(0, (count - min) / delta);
					const ratioM = (ratio * 192 + 24) | 0;

					const C = 255 - Math.abs(255 - (ratioM << 1));
					const m = (255 - ratioM) - (C >> 1);
					color = 'rgb(' + (((r * C) >> 8) + m) + ',' + (((g * C) >> 8) + m) + ',' + (((b * C) >> 8) + m) + ')';
				}
			}
			heatC.fillStyle = color;

			let x = Math.floor(index / currentHeatmap.timeSquareRowsCount);
			let y = index % currentHeatmap.timeSquareRowsCount;
			heatC.fillRect(x * sq - dx, y * sq + canvasTimeHeight, sq, sq);
		}

		let fromBlock = Math.floor(from / currentHeatmap.squaresBetweenMarks / currentHeatmap.timeSquareRowsCount) - 1;
		let toBlock = Math.ceil(to / currentHeatmap.squaresBetweenMarks / currentHeatmap.timeSquareRowsCount);

		let markPixels = currentHeatmap.squaresBetweenMarks * sq;

		heatC.fillStyle = '#fff';
		heatC.fillRect(
			fromBlock * markPixels - dx,
			0,
			(toBlock - fromBlock + 1) * markPixels,
			canvasTimeHeight
		);

		heatC.beginPath();
		heatC.moveTo(fromBlock * markPixels - dx + 0.5, canvasTimeHeight + 0.5);
		heatC.lineTo(toBlock * markPixels - dx + 0.5, canvasTimeHeight + 0.5);
		heatC.stroke();

		heatC.fillStyle = '#000';

		let groupSize = currentHeatmap.timeSquareRowsCount;
		let oneBlockMs = currentHeatmap.currentTimeSquareMs();
		let oneGroupMs = oneBlockMs * groupSize;
		let oneMarkMs = oneGroupMs * currentHeatmap.squaresBetweenMarks;
		for (let markIndex = fromBlock; markIndex <= toBlock; markIndex++) {
			let origin = Math.floor(startMs / oneMarkMs) * oneMarkMs;
			let ms = origin + markIndex * oneMarkMs;
			let markOffset = markIndex * markPixels - dx;

			let title = formatTime(ms, currentTimezone === 'UTC' ? timeOptionsTinyWithTZ : timeOptionsTiny);
			let x = markOffset + 4;
			heatC.fillText(title, x, canvasTimeHeight - 1, markPixels);

			heatC.beginPath();
			heatC.moveTo(markOffset + 0.5, canvasTimeHeight - 2 * sqScale + 0.5);
			heatC.lineTo(markOffset + 0.5, canvasTimeHeight + 2 * sqScale + 0.5);
			heatC.stroke();
		}
	}

	function redrawHeatSamples(from, to) {
		let dx = Math.floor((heatCanvasContainer.scrollLeft - canvasScrollPadding) * sqScale);

		from = Math.max(from, currentHeatmap.timeSquareRowsCount * Math.floor(dx / sq));
		to = Math.min(to, currentHeatmap.timeSquareRowsCount * Math.ceil((dx + heatCanvas.width) / sq));
		redrawHeatSamplesImpl(from, to, dx);
	}

	function redrawHeatMap() {
		redrawHeatSamples(0, (1 + currentHeatmap.count() / currentHeatmap.timeSquareRowsCount | 0) * currentHeatmap.timeSquareRowsCount);
	}

	function fillCanvasWithEvents(zoom) {
		currentHeatmap.setZoom(zoom);

		const m = devicePixelRatio || 1;
		sqScale = m;
		sqPx = 5;
		sq = Math.floor(sqPx * m);
		sqPx = sq / m;
		canvasTimeHeight = sq * 2 + 2;
		canvasTimeHeightPx = canvasTimeHeight / m;

		const widthPx = canvasScrollPadding + heatCanvasContainer.offsetWidth + canvasScrollPadding;
		const heightPx = sqPx * currentHeatmap.timeSquareRowsCount + canvasTimeHeightPx;

		const heatWidthPx = Math.max(20, Math.ceil(currentHeatmap.count() / currentHeatmap.timeSquareRowsCount)) * sqPx;
		heatCanvasWrapper.style.width = heatWidthPx + 'px';
		if (heatCanvasContainer.offsetWidth > heatWidthPx) {
			heatCanvasContainer.style.overflowX = 'hidden';
		} else {
			heatCanvasContainer.style.overflowX = 'scroll';
		}

		heatCanvas.width = Math.ceil(widthPx * m);
		heatCanvas.height = Math.ceil(heightPx * m);
		heatCanvas.style.width = widthPx + 'px';
		heatCanvas.style.height = heightPx + 'px';

		heatC = heatCanvas.getContext('2d');
		heatC.font = sq * 2 + 'px Verdana, sans-serif';
		heatC.lineWidth = 1;
		heatC.strokeStyle = '#000';

		document.getElementById('heatmap-height-line').textContent = zoomToText[currentHeatmap.zoom];
		redrawHeatMap();
	}

	function search(r, filter) {
		filter = filter || false;
		if (r && (r = prompt('Enter regexp to ' + (filter ? 'filter' : 'search') + ':', '')) === null) {
			return;
		}
		const wasFilter = filterFrames;
		filterFrames = filter;
		if (!r) {
			showFound = false;
			pattern = undefined;
			redrawHeatMap();
			if (wasFilter === filterFrames) {
				searchOnFlame();
			} else {
				reselect();
			}
			return;
		}

		const regex = RegExp(r)
		pattern = method => regex.test(methods.n[method]);
		showFound = true;
		const matchedMethods = new Set();
		for (let index = methods.c.length - 1; index >= 0; index--) {
			if (regex.test(methods.n[index])) {
				matchedMethods.add(index);
			}
		}

		const storage = currentHeatmap.blocksData.storage;
		const storageSizes = currentHeatmap.blocksData.storageSizes;
		const marks = currentHeatmap.blocksData.marks;
		marks.fill(0);
		for (let storagePos = storage.length - 1; storagePos >= 0;) {
			if (matchedMethods.has(storage[storagePos])) {
				marks[storagePos >> 5] |= 1 << (storagePos & 31);
				storagePos--;
				while (storagePos >= 0 && storageSizes[storagePos] !== 1) {
					marks[storagePos >> 5] |= 1 << (storagePos & 31);
					storagePos--;
				}
			} else {
				storagePos--;
			}
		}

		searchForMarks();
		if (filterFrames || wasFilter) {
			reselect();
		} else {
			searchOnFlame();
		}
	}

	function searchForMethod(methodId) {
		showFound = true;
		pattern = function (method) {
			return method === methodId;
		}
		const storage = currentHeatmap.blocksData.storage;
		const storageSizes = currentHeatmap.blocksData.storageSizes;
		const marks = currentHeatmap.blocksData.marks;
		marks.fill(0);
		for (let storagePos = storage.length - 1; storagePos >= 0;) {
			if (storage[storagePos] === methodId) {
				marks[storagePos >> 5] |= 1 << (storagePos & 31);
				storagePos--;
				while (storagePos >= 0 && storageSizes[storagePos] !== 1) {
					marks[storagePos >> 5] |= 1 << (storagePos & 31);
					storagePos--;
				}
			} else {
				storagePos--;
			}
		}

		searchForMarks();
		searchOnFlame();
	}

	function searchOnFlame() {
		const matched = render(root, rootLevel);
		displayMatched(matched);
	}

	function displayMatched(matched) {
		if (showFound) {
			document.getElementById('matchval').textContent = pct(matched, root.width) + '%';
			document.getElementById('match').style.display = 'inline-block';
			document.getElementById('produced').style.display = 'none';
		} else {
			document.getElementById('match').style.display = 'none';
			document.getElementById('produced').style.display = 'inherit';
		}
	}

	function searchForMarks() {
		const found = currentHeatmap.blocksData.foundCounts;
		const maxCounts = currentHeatmap.blocksData.searchMaxCounts;
		const minCounts = currentHeatmap.blocksData.searchMinCounts;

		searchForMarksStep();
		calculateMinMax(found, minCounts, maxCounts);
		redrawHeatMap();
	}

	function searchForMarksStep() {
		const counts = currentHeatmap.blocksData.counts;
		const chunksToStorage = currentHeatmap.blocksData.chunksToStorage;
		const sampleToChunkEnds = currentHeatmap.blocksData.sampleToChunkEnds;
		const found = currentHeatmap.blocksData.foundCounts;
		const marks = currentHeatmap.blocksData.marks;
		const sampleMarks = currentHeatmap.blocksData.sampleMarks;

		sampleMarks.fill(0);
		let sample = 0;
		let chunk = 0;
		let foundCount = 0;
		for (let block = 0; block < counts.length; block++) {
			const count = counts[block];
			for (; sample < count; sample++) {
				const chunkEnd = sampleToChunkEnds[sample];
				for (; chunk < chunkEnd; chunk++) {
					const storagePos = chunksToStorage[chunk];
					if ((marks[storagePos >> 5] & (1 << (storagePos & 31))) !== 0) {
						sampleMarks[sample >> 5] |= 1 << (sample & 31);
						foundCount++;
						chunk = chunkEnd;
						break;
					}
				}
			}
			found[block] = foundCount;
		}
	}

	function calculateMinMax(counts, minCounts, maxCounts) {
		for (let zi = 0; zi < zoomToGroupSize.length; zi++) {
			const z = zoomToGroupSize[zi];
			let max = 0;
			let min = 0x7fffffff;
			let prev = 0;
			for (let i = z - 1; i < counts.length; i += z) {
				const f = counts[i];
				const diff = f - prev;
				if (diff !== 0) {
					max = Math.max(max, diff);
					min = Math.min(min, diff);
				}
				prev = f;
			}
			const diff = counts[counts.length - 1] - prev;
			max = Math.max(max, diff);
			min = Math.min(min, max);
			maxCounts[zi] = max;
			minCounts[zi] = min;
		}
	}

	function calculateInitialZoom() {
		const width = Math.floor(heatCanvasContainer.offsetWidth / sq / (devicePixelRatio || 1));

		let z = 0;
		for (; z < zoomToGroupSize.length - 1; z++) {
			if (currentHeatmap.blocksData.counts.length / (zoomToGroupSize[z] * zoomToHeight[z]) < width) {
				break;
			}
		}
		return z;
	}

	function renderHeatmap() {
		let dx = heatCanvasContainer.scrollLeft - canvasScrollPadding;
		heatCanvas.style.transform = 'translate(' + dx + 'px, 0px)';

		fillCanvasWithEvents(calculateInitialZoom());

		renderWrapper(0, currentHeatmap.blocksData.counts.length - 1);
	}

	heatCanvasContainer.addEventListener('scroll', function () {
		let dx = Math.floor((heatCanvasContainer.scrollLeft - canvasScrollPadding) * sqScale);
		let dxPx = dx / sqScale;
		heatCanvas.style.transform = 'translate(' + dxPx + 'px, 0px)';
		let delta = Math.abs(dx - prevDx);
		if (delta >= heatCanvas.width) {
			redrawHeatMap();
		} else {
			heatC.drawImage(heatCanvas, prevDx - dx, 0);
			if (prevDx < dx) {
				let from = currentHeatmap.timeSquareRowsCount * Math.floor((prevDx + heatCanvas.width) / sq);
				let to = currentHeatmap.timeSquareRowsCount * Math.ceil((dx + heatCanvas.width) / sq);
				redrawHeatSamplesImpl(from, to, dx);
			} else {
				let from = currentHeatmap.timeSquareRowsCount * Math.floor(dx / sq);
				let to = currentHeatmap.timeSquareRowsCount * Math.ceil(prevDx / sq);
				redrawHeatSamplesImpl(from, to, dx);
			}
		}
		prevDx = dx;
		cooldownTime = performance.now() + 500;
	});

	document.getElementById('heatmap-height-line').onclick = function () {
		fillCanvasWithEvents((zoomToGroupSize.length + currentHeatmap.zoom - 1) % (zoomToGroupSize.length));
		highlightStart = highlightEnd = heatDiffSample1 = heatDiffSample2 = heatActiveSample1 = heatActiveSample2 = -1;
		for (let suffix of ['Selection', 'Diff', 'Active']) {
			for (let prefix of ['left', 'leftMiddle', 'middle', 'rightMiddle', 'right']) {
				document.getElementById(prefix + suffix).style.display = 'none';
			}
		}
	}

	function callHighlightRedraw(start, end, suffix) {
		let left = document.getElementById('left' + suffix);
		let leftMiddle = document.getElementById('leftMiddle' + suffix);
		let middle = document.getElementById('middle' + suffix);
		let rightMiddle = document.getElementById('rightMiddle' + suffix);
		let right = document.getElementById('right' + suffix);

		let x1 = Math.floor(start / currentHeatmap.timeSquareRowsCount);
		let y1 = start % currentHeatmap.timeSquareRowsCount;
		let x2 = Math.floor(end / currentHeatmap.timeSquareRowsCount);
		let y2 = end % currentHeatmap.timeSquareRowsCount;

		let veryStartX = x1 * sqPx;
		let veryStartY = y1 * sqPx;
		let veryEndX = x2 * sqPx;
		let px = 1 / sqScale;
		let singleElementWidth = sqPx + px;

		let topPadding = canvasTimeHeightPx;

		if (x1 === x2) {
			left.style.display = 'none';
			right.style.display = 'none';

			for (let b of [middle, leftMiddle, rightMiddle]) {
				b.style.left = veryStartX + 'px';
				b.style.top = topPadding + veryStartY + 'px';
				b.style.width = singleElementWidth + 'px';
				b.style.height = (y2 - y1 + 1) * sqPx + px + 'px';
				b.style.display = 'block';
			}
		} else {
			left.style.left = veryStartX + 'px';
			left.style.top = topPadding + veryStartY + 'px';
			left.style.width = singleElementWidth + 'px';
			left.style.height = (currentHeatmap.timeSquareRowsCount - y1) * sqPx + px + 'px';
			left.style.display = 'block';

			leftMiddle.style.left = veryStartX + 'px';
			leftMiddle.style.top = topPadding + 'px';
			leftMiddle.style.width = singleElementWidth + 'px';
			leftMiddle.style.height = y1 * sqPx + px + 'px';
			leftMiddle.style.display = 'block';

			rightMiddle.style.left = veryEndX + 'px';
			rightMiddle.style.top = topPadding + (y2 + 1) * sqPx + 'px';
			rightMiddle.style.width = sqPx + px + 'px';
			rightMiddle.style.height = (currentHeatmap.timeSquareRowsCount - y2 - 1) * sqPx + px + 'px';
			rightMiddle.style.display = 'block';

			right.style.left = veryEndX + 'px';
			right.style.top = topPadding + 'px';
			right.style.width = sqPx + px + 'px';
			right.style.height = (y2 + 1) * sqPx + px + 'px';
			right.style.display = 'block';

			if (x2 - x1 === 1) {
				middle.style.display = 'none';
			} else {
				middle.style.left = veryStartX + sqPx + px + 'px';
				middle.style.top = topPadding + 'px';
				middle.style.width = (x2 - x1 - 1) * sqPx - px + 'px';
				middle.style.height = currentHeatmap.timeSquareRowsCount * sqPx + px + 'px';
				middle.style.display = 'block';
			}
		}
	}

	function callSelectionRedraw(sample, shiftPressed, ctrlPressed) {
		if (ctrlPressed) {
			highlightStart = sample;
			highlightEnd = sample + Math.abs(heatActiveSample1 - heatActiveSample2);
		} else if (shiftPressed && heatActiveSample1 !== -1) {
			highlightStart = Math.min(heatActiveSample1, sample);
			highlightEnd = Math.max(heatActiveSample1, sample);
		} else {
			highlightStart = highlightEnd = sample;
		}

		callHighlightRedraw(highlightStart, highlightEnd, 'Selection');

		const index = (sample - currentHeatmap.startBlock()) * currentHeatmap.timeSquareScale;
		const counts = currentHeatmap.blocksData.counts;
		const foundCounts = currentHeatmap.blocksData.foundCounts;
		if (index >= 0 && index < counts.length) {
			const countBeforeFirstBlock = getCount(counts, index - 1);
			const countAtLastBlock = getCount(counts, index + currentHeatmap.timeSquareScale - 1);
			const searchCountBeforeFirstBlock = getCount(foundCounts, index - 1);
			const searchCountAtLastBlock = getCount(foundCounts, index + currentHeatmap.timeSquareScale - 1);

			const total = countAtLastBlock - countBeforeFirstBlock;
			const searchTotal = searchCountAtLastBlock - searchCountBeforeFirstBlock;
			const max = currentHeatmap.max(false);
			const totalText = "total: " + total + " (" + Math.floor(total / max * 100) + "%)";
			const searchText = showFound
				? "; match: " + searchTotal + " (" + Math.floor(searchTotal / Math.max(currentHeatmap.max(true), 1) * 100) + "%)"
				: "";
			status.textContent = totalText + searchText;
			status.style.display = 'inline';
		} else {
			status.style.display = 'none';
		}
		const ms = Math.floor(startMs / currentHeatmap.currentTimeSquareMs()) * currentHeatmap.currentTimeSquareMs() + currentHeatmap.minimalTimeSquare * index;
		heatCanvas.title = formatTime(ms, timeOptionsShort);
	}

	function callActiveRedraw(sample, shiftPressed, ctrlPressed) {
		if (ctrlPressed) {
			let minSelected = Math.min(heatActiveSample1, heatActiveSample2);
			let maxSelected = Math.max(heatActiveSample1, heatActiveSample2);

			heatDiffSample1 = highlightStart;
			heatDiffSample2 = highlightEnd;

			callHighlightRedraw(highlightStart, highlightEnd, 'Diff');
			renderWrapperDiff(
				(minSelected - currentHeatmap.startBlock()) * currentHeatmap.timeSquareScale,
				(maxSelected - currentHeatmap.startBlock() + 1) * currentHeatmap.timeSquareScale - 1,
				(heatDiffSample1 - currentHeatmap.startBlock()) * currentHeatmap.timeSquareScale,
				(heatDiffSample2 - currentHeatmap.startBlock() + 1) * currentHeatmap.timeSquareScale - 1
			);
		} else {
			heatDiffSample1 = -1;
			heatDiffSample2 = -1;
			if (shiftPressed && heatActiveSample1 !== -1) {
				heatActiveSample2 = sample;
			} else {
				heatActiveSample1 = heatActiveSample2 = sample;
			}

			let minSelected = Math.min(heatActiveSample1, heatActiveSample2);
			let maxSelected = Math.max(heatActiveSample1, heatActiveSample2);

			callHighlightRedraw(highlightStart, highlightEnd, 'Diff');
			callHighlightRedraw(minSelected, maxSelected, 'Active');
			renderWrapper(
				(minSelected - currentHeatmap.startBlock()) * currentHeatmap.timeSquareScale,
				(maxSelected - currentHeatmap.startBlock() + 1) * currentHeatmap.timeSquareScale - 1
			);
		}
	}

	function updateSelectionArea(delta, endOnly, diff) {
		highlightStart = -1;
		highlightEnd = -1;
		if (diff) {
			if (heatDiffSample1 === -1) {
				let minSelected = Math.min(heatActiveSample1, heatActiveSample2);
				let maxSelected = Math.max(heatActiveSample1, heatActiveSample2);
				heatDiffSample1 = minSelected + delta;
				heatDiffSample2 = maxSelected + delta;
			} else {
				if (!endOnly) {
					heatDiffSample1 += delta;
				}
				heatDiffSample2 += delta;
			}
			let min = Math.min(heatDiffSample1, heatDiffSample2);
			let max = Math.max(heatDiffSample1, heatDiffSample2);
			callHighlightRedraw(min, max, 'Diff');
		} else {
			if (!endOnly) {
				heatActiveSample1 += delta;
			}
			heatActiveSample2 += delta;
			let minSelected = Math.min(heatActiveSample1, heatActiveSample2);
			let maxSelected = Math.max(heatActiveSample1, heatActiveSample2);

			callHighlightRedraw(minSelected, maxSelected, 'Active');
			callHighlightRedraw(highlightStart, highlightEnd, 'Selection');
			if (heatDiffSample1 === -1) {
				callHighlightRedraw(minSelected, maxSelected, 'Diff');
			}
		}
		let minSelected = Math.min(heatActiveSample1, heatActiveSample2);
		let maxSelected = Math.max(heatActiveSample1, heatActiveSample2);

		if (heatDiffSample1 === -1) {
			renderWrapper(
				(minSelected - currentHeatmap.startBlock()) * currentHeatmap.timeSquareScale,
				(maxSelected - currentHeatmap.startBlock() + 1) * currentHeatmap.timeSquareScale - 1
			);
		} else {
			let min = Math.min(heatDiffSample1, heatDiffSample2);
			let max = Math.max(heatDiffSample1, heatDiffSample2);
			renderWrapperDiff(
				(minSelected - currentHeatmap.startBlock()) * currentHeatmap.timeSquareScale,
				(maxSelected - currentHeatmap.startBlock() + 1) * currentHeatmap.timeSquareScale - 1,
				(min - currentHeatmap.startBlock()) * currentHeatmap.timeSquareScale,
				(max - currentHeatmap.startBlock() + 1) * currentHeatmap.timeSquareScale - 1
			);
		}
	}

	window.addEventListener('keydown', e => {
		if (e.key === 'Shift') {
			callSelectionRedraw(heatLastSample, true, e.ctrlKey);
		} else if (e.key === 'Control') {
			callSelectionRedraw(heatLastSample, e.shiftKey, true);
		}
	});

	window.addEventListener('keyup', e => {
		if (e.key === 'Shift') {
			callSelectionRedraw(heatLastSample, false, e.ctrlKey);
		} else if (e.key === 'Control') {
			callSelectionRedraw(heatLastSample, e.shiftKey, false);
		}
	});

	window.addEventListener('keydown', e => {
		switch (e.key) {
			case 'ArrowUp':
				updateSelectionArea(-1, e.shiftKey, e.ctrlKey);
				break;
			case 'ArrowDown':
				updateSelectionArea(+1, e.shiftKey, e.ctrlKey);
				break;
			case 'ArrowLeft':
				updateSelectionArea(-currentHeatmap.timeSquareRowsCount, e.shiftKey, e.ctrlKey);
				break;
			case 'ArrowRight':
				updateSelectionArea(+currentHeatmap.timeSquareRowsCount, e.shiftKey, e.ctrlKey);
				break;
			case '1':
				selectMode('flame-mode-flame');
				break;
			case '2':
				selectMode('flame-mode-reversed');
				break;
			case '3':
				selectMode('flame-mode-methods');
				break;
			case 'r':
			case 'R':
				if (!e.ctrlKey) {
					return;
				}
				if (heatDiffSample1 !== -1) {
					renderWrapperDiff(lastBaseRenderFrom, lastBaseRenderTo, lastRenderFrom, lastRenderTo);
				}
				break;
			case 'f':
			case 'F':
				if (!e.ctrlKey) {
					return;
				}
				search(true, e.shiftKey);
				break;
			case 'Escape':
				search(false);
				break;
			default:
				return;
		}
		e.preventDefault();
	});

	window.onkeydown = function (e) {
		if (e.keyCode === 16) {
			if (previewX !== -1 && previewY !== -1) {
				showPreview();
			}
		}
	}

	window.onkeyup = function (e) {
		if (!e.shiftKey) {
			preview_wrapper.style.display = 'none';
		}
	}

	let moved = false;
	heatCanvas.onmousemove = function (event) {
		heatCanvas.style.cursor = event.offsetY < canvasTimeHeightPx ? 'pointer' : '';
		let x = Math.floor((event.offsetX + heatCanvasContainer.scrollLeft - canvasScrollPadding) / sqPx);
		let y = Math.floor(Math.max(0, event.offsetY - canvasTimeHeightPx) / sqPx);
		if (y >= currentHeatmap.timeSquareRowsCount) {
			y = currentHeatmap.timeSquareRowsCount - 1;
		}
		heatLastSample = x * currentHeatmap.timeSquareRowsCount + y;
		if ((event.buttons & 1) === 1) {
			callSelectionRedraw(heatLastSample, true, event.ctrlKey);
		} else {
			callSelectionRedraw(heatLastSample, event.shiftKey, event.ctrlKey);
		}
		moved = true;
	}

	heatCanvas.onmouseout = function () {
		status.style.display = 'none';
	};

	heatCanvas.onmousedown = function (event) {
		if (event.offsetY < canvasTimeHeightPx) {
			moved = false;
			return;
		}

		let x = Math.floor((event.offsetX + heatCanvasContainer.scrollLeft - canvasScrollPadding) / sqPx);
		let y = Math.floor(Math.max(0, event.offsetY - canvasTimeHeightPx) / sqPx);
		let sample = x * currentHeatmap.timeSquareRowsCount + y;

		callActiveRedraw(sample, event.shiftKey, event.ctrlKey);
		moved = false;
	};

	heatCanvas.onmouseup = function (event) {
		if (moved) {
			let x = Math.floor((event.offsetX + heatCanvasContainer.scrollLeft - canvasScrollPadding) / sqPx);
			let y = Math.floor(Math.max(0, event.offsetY - canvasTimeHeightPx) / sqPx);
			let sample = x * currentHeatmap.timeSquareRowsCount + y;

			callActiveRedraw(sample, true, event.ctrlKey);
		}
	};

	heatCanvas.onclick = function (event) {
		if (event.offsetY < canvasTimeHeightPx && !moved) {
			currentTimezone = currentTimezone === 'Local' ? 'UTC' : 'Local';
			localStorage.setItem('heatmap-timezone', currentTimezone);
			redrawHeatMap();
		}
	};

	renderHeatmap();
	// first render of dominators
	renderFunc = renderTraces;
</script>
</body>
</html>

```

## File: src\res\tree.html
```
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Tree view</title>
    <meta charset="utf-8" />
    <style>
      html,
      body,
      div,
      span,
      a,
      code,
      ul,
      li {
        margin: 0;
        padding: 0;
        border: 0;
        font: inherit;
        vertical-align: baseline;
      }
      body {
        line-height: 140%;
        font-family: Arial;
        background: white;
        font-size: 15px;
      }
      ul {
        list-style: none;
      }

      .tree li {
        list-style-type: none;
        position: relative;
        white-space: nowrap;
      }
      .tree ul {
        margin-left: 20px;
        padding-left: 0;
      }
      .tree li ul {
        display: none;
      }
      .tree li.open > ul {
        display: block;
      }
      .tree li div:before,
      .tree li div:after {
        position: absolute;
        content: "";
        top: 0;
        bottom: 0;
        margin: auto;
        background: #252527;
      }
      .tree li div:before {
        width: 10px;
        height: 2px;
        left: -1px;
      }
      .tree li div:after {
        width: 2px;
        height: 10px;
        left: 3px;
      }
      .tree li div:hover:after,
      .tree li div:hover:before {
        background: #00ac4f;
      }
      .tree li.open > div:after {
        display: none;
      }
      .tree li > div {
        padding-left: 17px;
        position: relative;
        display: inline;
        cursor: pointer;
        color: black;
        text-decoration: none;
      }
      .tree li > div:first-word {
        font-weight: bold;
      }
      /* no children ul */
      .o:after,
      .o:before {
        display: none !important;
      }
      .sc {
        text-decoration-color: black;
        font-weight: bold;
        background-color: #d9d9d9;
      }
      input {
        height: 36px;
        padding: 0 14px;
        border-radius: 4px;
        background: white;
        font-size: 16px;
        border: 1px solid #2023281a;
      }
      button {
        height: 36px;
        border: none;
        background: none;
        border-radius: 4px;
        cursor: pointer;
        white-space: nowrap;
      }
      button:hover {
        color: #00ac4f;
      }
      .button_outlined {
        color: black;
        font-size: 15px;
        padding: 0 12px;
        background: white;
        border: 1px solid #2023281a;
        display: flex;
        align-items: center;
        gap: 8px;
      }
      .total-count {
        color: #5e5e5e;
        font-weight: bold;
        font-size: 14px;
      }
      .p {
        font-weight: bold;
      }
      .header {
        display: flex;
        position: fixed;
        top: 0;
        left: 0;
        gap: 16px;
        flex-direction: row;
        z-index: 100;
        padding: 8px 20px;
        background: #f5f5f5;
        align-items: center;
        box-sizing: border-box;
        width: 100%;
      }
      .icon_gray {
        color: #b7b7b7;
      }
      .header-actions {
        display: flex;
        flex-direction: row;
        align-items: center;
        gap: 8px;
        flex: 1;
      }
      .header-item {
        display: flex;
        flex-direction: row;
        align-items: center;
        gap: 8px;
      }
      .view-type {
        display: flex;
        gap: 8px;
        flex-direction: row;
        font-weight: bold;
        margin-top: 4px;
        align-items: center;
      }
      .view-type__decoration {
        display: flex;
        gap: 8px;
      }
      .header-item_search {
        gap: 8px;
        flex: 1;
      }
      .search-input {
        flex: 1;
      }
      .title {
        font-size: 16px;
      }
      .wrapper {
        padding: 70px 20px 10px;
        background: white;
        border-top: 1px solid #e9e9e9;
      }

      .child-count {
        border: 1px solid #abb1c1;
        border-radius: 3px;
        padding: 0 5px;
        color: #7d8089;
      }

      .t0,
      .t1,
      .t2,
      .t3,
      .t4,
      .t5,
      .t6 {
        font-family: SFMono-Regular,Consolas,Liberation Mono,Menlo,Courier,monospace;
      }
      .t0 {color: #3A6F38;}
      .t1 {color: #05B505;}
      .t2 {color: #006A7C;}
      .t3 {color: #9B0000;}
      .t4 {color: #A7A718;}
      .t5 {color: #CC5200;}
      .t6 {color: #7C8F45;}
      @media only screen and (max-width: 968px) {
        .only-desktop {
          display: none;
        }
      }
    </style>
<script>
function treeView(opt) {
	var tree = document.querySelectorAll('ul.tree div:not(:last-child)');
	for(var i = 0; i < tree.length; i++){
		var parent = tree[i].parentElement;
		var classList = parent.classList;
		if(opt == 0) {
			classList.add('open');
		} else {
			classList.remove('open');
		}
	}
}
function openParent(p,t) {
	if(p.parentElement.classList.contains('tree')) {
		return;
	}
	p.parentElement.classList.add('open');
	openParent(p.parentElement,t);
}
function search() {
	var tree = document.querySelectorAll('ul.tree span');
	var check = document.getElementById('check');
	for(var i = 0; i < tree.length; i++){
		tree[i].classList.remove('sc');
		if(tree[i].innerHTML.includes(document.getElementById('search').value)) {
			tree[i].classList.add('sc');
			openParent(tree[i].parentElement,tree);
		}
	}
}
function openUL(n) {
	var children = n.children;
	if(children.length == 1) {
		openNode(children[0]);
	}
}
function openNode(n) {
	var children = n.children;
	for(var i = 0; i < children.length; i++){
		if(children[i].nodeName == 'UL') {
			n.classList.add('open');
			openUL(children[i]);
		}
	}
}
function addClickActions() {
var tree = document.querySelectorAll('ul.tree div:not(:last-child)');
for(var i = 0; i < tree.length; i++){
	tree[i].addEventListener('click', function(e) {
		var parent = e.target.parentElement;
		var classList = parent.classList;
		if(classList.contains('open')) {
			classList.remove('open');
			var opensubs = parent.querySelectorAll(':scope .open');
			for(var i = 0; i < opensubs.length; i++){
				opensubs[i].classList.remove('open');
			}
		} else {
			if(e.altKey) {
				classList.add('open');
				var opensubs = parent.querySelectorAll('li');
				for(var i = 0; i < opensubs.length; i++){
					opensubs[i].classList.add('open');
				}
			} else {
				openNode(parent);
			}
		}
	});
}
}
</script>
  </head>
  <body>
    <div class="header">
      <div class="title">
        <div class="view-type">
          <span class="view-type__decoration only-desktop">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M9 17H5C3.89543 17 3 16.1046 3 15V3" stroke="#A2A2A2" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
              <path d="M9 7H3" stroke="#A2A2A2" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
              <path fill-rule="evenodd" clip-rule="evenodd" d="M21 8.5V5C21 4.17157 20.3284 3.5 19.5 3.5H17.4381C17.1071 3.5 16.7975 3.33616 16.6113 3.06243L16.1863 2.43757C16.0001 2.16383 15.6905 1.99999 15.3594 2H13.5C12.6716 2 12 2.67157 12 3.5V8.5C12 9.32843 12.6716 10 13.5 10H19.5C20.3284 10 21 9.32843 21 8.5Z" stroke="#A2A2A2" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
              <path fill-rule="evenodd" clip-rule="evenodd" d="M21 19.5V16C21 15.1716 20.3284 14.5 19.5 14.5H17.4381C17.1071 14.5 16.7975 14.3362 16.6113 14.0624L16.1863 13.4376C16.0001 13.1638 15.6905 13 15.3594 13H13.5C12.6716 13 12 13.6716 12 14.5V19.5C12 20.3284 12.6716 21 13.5 21H19.5C20.3284 21 21 20.3284 21 19.5Z" stroke="#A2A2A2" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
            </svg>
            <span>/*title:*/ view</span>
          </span>
          <span class="total-count">total /*type:*/: /*count:*/</span>
        </div>
      </div>
      <div class="header-actions">
        <div class="header-item">
          <button alt="Collapse All" type="button" onclick="treeView(0)" class="button_outlined">Expand All</button>
          <button alt="Expand All" type="button" onclick="treeView(1)" class="button_outlined">Collapse All</button>
        </div>
        <div class="header-item header-item_search">
          <input class="search-input" type="text" id="search" value="" placeholder="Search..." size="35" onkeypress="if(event.keyCode == 13) search()"/>
        </div>
      </div>
    </div>
    <div class="wrapper">
      <ul class="tree">
        /*tree:*/
        <script>
          addClickActions();
        </script>
      </ul>
    </div>
  </body>
</html>

```

