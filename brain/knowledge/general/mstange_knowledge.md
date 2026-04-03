---
id: mstange-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:29:09.973974
---

# KNOWLEDGE EXTRACT: mstange
> **Extracted on:** 2026-03-30 17:43:07
> **Source:** mstange

---

## File: `samply.md`
```markdown
# 📦 mstange/samply [🔖 PENDING/APPROVE]
🔗 https://github.com/mstange/samply


## Meta
- **Stars:** ⭐ 4035 | **Forks:** 🍴 90
- **Language:** Rust | **License:** Apache-2.0
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Command-line sampling profiler for macOS, Linux, and Windows

## README (trích đầu)
```
# samply

samply is a command line CPU profiler which uses the [Firefox profiler](https://profiler.firefox.com/) as its UI.

samply works on macOS, Linux, and Windows.

In order to profile the execution of `./my-application`, prepend `samply record` to the command invocation:

```sh
samply record ./my-application my-arguments
```

On Linux, samply uses perf events. You can grant temporary access by running:

```sh
echo '-1' | sudo tee /proc/sys/kernel/perf_event_paranoid
```

On Windows, you can use `samply record -a` to record all processes. You'll usually also want to use some symbol servers, most importantly the Microsoft Symbol Server so that you can see symbols for Windows libraries. Here's a command which supports symbols for Windows, Firefox and Chrome:

```
samply record -a --windows-symbol-server https://msdl.microsoft.com/download/symbols --breakpad-symbol-server https://symbols.mozilla.org/try/ --windows-symbol-server https://chromium-browser-symsrv.commondatastorage.googleapis.com
```

## Installation

You have the following options to install samply:

### Install prebuilt binaries via shell script

macOS/Linux:

```sh
curl --proto '=https' --tlsv1.2 -LsSf https://github.com/mstange/samply/releases/download/samply-v0.13.1/samply-installer.sh | sh
```

Windows:

```sh
powershell -ExecutionPolicy Bypass -c "irm https://github.com/mstange/samply/releases/download/samply-v0.13.1/samply-installer.ps1 | iex"
```

### Install from crates.io with cargo

```sh
cargo install --locked samply
```

### Build from source

```sh
git clone https://github.com/mstange/samply
cd samply
cargo build --release
./target/release/samply ...
```

## Description

```sh
samply record ./my-application my-arguments
```

This spawns `./my-application my-arguments` in a subprocess and records a profile of its execution. When the command finishes, samply opens
[profiler.firefox.com](https://profiler.firefox.com/) in your default browser, loads the recorded profile in it, and starts a local webserver which serves symbol information and source code.

Then you can inspect the profile. And you can upload it.

Here's an example: https://share.firefox.dev/3j3PJoK

This is a profile of [dump_syms](https://github.com/mozilla/dump_syms), running on macOS, recorded as follows:

```
samply record ./dump_syms ~/mold-opt-libxul.so > /dev/null
```

You can see which functions were running for how long. You can see flame graphs and timelines. You can double-click functions in the call tree to open the source view, and see which lines of code were sampled how many times.

All data is kept locally (on disk and in RAM) until you choose to upload your profile.

samply is a sampling profiler and collects stack traces, per thread, at some sampling interval (the default 1000Hz, i.e. 1ms). On macOS and Windows, both on- and off-cpu samples are collected (so you can see under which stack you were blocking on a lock, for example). On Linux, only on-cpu samples are collected at the moment.

O
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

