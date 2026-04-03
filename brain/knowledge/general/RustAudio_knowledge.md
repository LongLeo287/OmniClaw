---
id: rustaudio-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:31:10.542909
---

# KNOWLEDGE EXTRACT: RustAudio
> **Extracted on:** 2026-03-30 17:53:02
> **Source:** RustAudio

---

## File: `cpal.md`
```markdown
# 📦 RustAudio/cpal [🔖 PENDING/APPROVE]
🔗 https://github.com/RustAudio/cpal


## Meta
- **Stars:** ⭐ 3615 | **Forks:** 🍴 490
- **Language:** Rust | **License:** Apache-2.0
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Cross-platform audio I/O library in pure Rust

## README (trích đầu)
```
# CPAL - Cross-Platform Audio Library

[![Actions Status](https://github.com/RustAudio/cpal/workflows/cpal/badge.svg)](https://github.com/RustAudio/cpal/actions)
[![Crates.io](https://img.shields.io/crates/v/cpal.svg)](https://crates.io/crates/cpal) [![docs.rs](https://docs.rs/cpal/badge.svg)](https://docs.rs/cpal/)

Low-level library for audio input and output in pure Rust.

## Minimum Supported Rust Version (MSRV)

The minimum Rust version required depends on which audio backend and features you're using, as each platform has different dependencies:

- **AAudio (Android):** Rust **1.82**
- **ALSA (Linux/BSD):** Rust **1.82**
- **CoreAudio (macOS/iOS):** Rust **1.80**
- **JACK (Linux/BSD/macOS/Windows):** Rust **1.82**
- **PipeWire (Linux/BSD):** Rust **1.82**
- **PulseAudio (Linux/BSD):** Rust **1.88**
- **WASAPI/ASIO (Windows):** Rust **1.82**
- **WASM (`wasm32-unknown`):** Rust **1.82**
- **WASM (`wasm32-wasip1`):** Rust **1.78**
- **WASM (`audioworklet`):** Rust **nightly** (requires `-Zbuild-std` for atomics support)

## Supported Platforms

This library currently supports the following:

- Enumerate supported audio hosts.
- Enumerate all available audio devices.
- Get the current default input and output devices.
- Enumerate known supported input and output stream formats for a device.
- Get the current default input and output stream formats for a device.
- Build and run input and output PCM streams on a chosen device with a given stream format.

Currently, supported platforms include:

- Android (via AAudio)
- BSD (via ALSA by default, JACK, PipeWire or PulseAudio optionally)
- Emscripten
- iOS (via CoreAudio)
- Linux (via ALSA by default, JACK, PipeWire or PulseAudio optionally)
- macOS (via CoreAudio by default, JACK optionally)
- WebAssembly (via Web Audio API or Audio Worklet)
- Windows (via WASAPI by default, ASIO or JACK optionally)

Note that on Linux, the ALSA development files are required for building (even when using JACK, PipeWire or PulseAudio). These are provided as part of the `libasound2-dev` package on Debian and Ubuntu distributions and `alsa-lib-devel` on Fedora.

## Compiling for WebAssembly

If you are interested in using CPAL with WebAssembly, please see [this guide](https://github.com/RustAudio/cpal/wiki/Setting-up-a-new-CPAL-WASM-project) in our Wiki which walks through setting up a new project from scratch. Some of the examples in this repository also provide working configurations that you can use as reference.

## Optional Features

| Feature | Platform | Description |
|---------|----------|-------------|
| `audio_thread_priority` | Linux, BSD, Windows | Raises the audio callback thread to real-time priority for lower latency and fewer glitches. On Linux, requires `rtkit` or appropriate user permissions (`limits.conf` or capabilities). |
| `asio` | Windows | ASIO backend for low-latency audio, bypassing the Windows audio stack. Requires ASIO drivers and LLVM/Clang. See the [ASIO setup guide](#asio-on-windows). 
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

