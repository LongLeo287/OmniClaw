---
id: github.com-rustaudio-cpal-70183466-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:18.704834
---

# KNOWLEDGE EXTRACT: github.com_RustAudio_cpal_70183466
> **Extracted on:** 2026-04-01 12:01:49
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007521662/github.com_RustAudio_cpal_70183466

---

## File: `.gitignore`
```
/target
/Cargo.lock
.cargo/
.DS_Store
recorded.wav
rls*.log
/.direnv
!/examples/audioworklet-beep/.cargo/

```

## File: `CHANGELOG.md`
```markdown
# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- `DeviceBusy` error variant to `SupportedStreamConfigsError`, `DefaultStreamConfigError`, and
  `BuildStreamError` for retryable device access errors (EBUSY, EAGAIN).
- `StreamConfig` now implements `Copy`.
- `StreamTrait::buffer_size()` to query the stream's current buffer size in frames per callback.
- `device_by_id` is now dispatched to each backend's implementation, allowing to override it.
- **ALSA**: `device_by_id` now accepts PCM shorthand names such as `hw:0,0` and `plughw:foo`.
- **PipeWire**: New host for Linux and some BSDs using the PipeWire API.
- **PulseAudio**: New host for Linux and some BSDs using the PulseAudio API.

### Changed

- Public error enums are now marked `#[non_exhaustive]` to allow adding variants without
  SemVer-breaking changes.
- `DeviceTrait::build_*_stream` now takes `StreamConfig` by value instead of `&StreamConfig`
- **AAudio**: Device names now include the device type suffix (e.g. "Speaker (Builtin Speaker)")
  for easier identification when enumerating devices.
- **AAudio**: `supported_input_configs` and `supported_output_configs` now return an error for
  direction-mismatched devices (e.g. querying input configs on an output-only device) instead of
  silently returning an empty list.
- **AAudio**: Bump MSRV to 1.85.
- **AAudio**: Buffers with default sizes are now dynamically tuned.
- **ALSA**: Device disconnection now stops the stream with `StreamError::DeviceNotAvailable` instead of looping.
- **ALSA**: Polling errors trigger underrun recovery instead of looping.
- **ALSA**: Try to resume from hardware after a system suspend.
- **ALSA**: Loop partial reads and writes to completion.
- **ALSA**: Prevent reentrancy issues with non-reentrant plugins and devices.
- **ASIO**: `Device::driver`, `asio_streams`, and `current_callback_flag` are no longer `pub`.
- **ASIO**: Timestamps now include driver-reported hardware latency.
- **ASIO**: Hardware latency is now re-queried when the driver reports `kAsioLatenciesChanged`.
- **ASIO**: Stream error callback now receives `StreamError::BufferUnderrun` on `kAsioResyncRequest`.
- **ASIO**: Stream error callback now receives `StreamError::StreamInvalidated` when the driver reports a sample rate change (`sampleRateDidChange`) of 1 Hz or more from the configured rate.
- **CoreAudio**: Timestamps now include device latency and safety offset.
- **JACK**: Timestamps now use the precise hardware deadline.
- **Linux/BSD**: Default host in order from first to last available now is: PipeWire, PulseAudio, ALSA.
- **WASAPI**: Timestamps now include hardware pipeline latency.
- **WebAudio**: Bump MSRV to 1.85.
- **WebAudio**: Timestamps now include base and output latency.
- **WebAudio**: Initial buffer scheduling offset now scales with buffer duration.

### Fixed

- Reintroduce `audio_thread_priority` feature.
- Fix numeric overflows in calls to create `StreamInstant` in ASIO, CoreAudio and JACK.
- **AAudio**: Fix thread lock when a stream is dropped before it fully starts.
- **AAudio**: Fix invalid capture and playback timestamps.
- **ALSA**: Fix capture stream hanging or spinning on overruns.
- **ALSA**: Fix non-monotonic `StreamInstant` during stream startup.
- **ALSA**: Fix spurious timestamp errors during stream startup.
- **ALSA**: Fix spurious timeout errors during polling.
- **ALSA**: Fix rare panics when dropping the stream is interrupted.
- **ALSA**: Fix timestamp overflows on 32-bit platforms.
- **ASIO**: Fix enumeration returning only the first device when using `collect`.
- **ASIO**: Fix device enumeration and stream creation failing when called from spawned threads.
- **ASIO**: Fix buffer size not resizing when the driver reports `kAsioBufferSizeChange`.
- **ASIO**: Fix latency not updating when the driver reports `kAsioLatenciesChanged`.
- **ASIO**: Fix distortion when buggy drivers fire the buffer callback multiple times per cycle.
- **CoreAudio**: Fix undefined behaviour and silent failure in loopback device creation.
- **Emscripten**: Fix build failure introduced by newer `wasm-bindgen` versions.
- **JACK**: Fix input capture timestamp using callback execution time instead of cycle start.

## [0.17.3] - 2026-02-18

### Changed

- Reverted SemVer-breaking `DeviceBusy` error variant addition.

### Fixed

- **ASIO**: Fix linker errors.

## [0.17.2] - 2026-02-08 [YANKED]

### Added

- `DeviceBusy` error variant for retriable device access errors (EBUSY, EAGAIN).
- **ALSA**: `Debug` implementations for `Host`, `Device`, `Stream`, and internal types.
- **ALSA**: Example demonstrating ALSA error suppression during enumeration.
- **ALSA**: Support for native DSD playback.
- **WASAPI**: Enable as-necessary resampling in the WASAPI server process.

### Changed

- Bump overall MSRV to 1.78.
- **ALSA**: Update `alsa` dependency to 0.11.
- **ALSA**: Bump MSRV to 1.82.
- **CoreAudio**: Update `core-audio-rs` dependency to 0.14.

### Fixed

- **ALSA**: Enumerating input and output devices no longer interferes with each other.
- **ALSA**: Device handles are no longer exclusively held between operations.
- **ALSA**: Reduce Valgrind memory leak reports from ALSA global configuration cache.
- **ALSA**: Fix possible race condition on drop.
- **ALSA**: Fix audio callback stalling when start threshold is not met.

## [0.17.1] - 2026-01-04

### Added

- **ALSA**: `Default` implementation for `Device` (returns the ALSA "default" device).
- **CI**: Checks default/no-default/all feature sets with platform-dependent MSRV for JACK.

### Changed

- **ALSA**: Devices now report direction from hint metadata and physical hardware probing.

### Fixed

- **ALSA**: Device enumeration now includes both hints and physical cards.
- **JACK**: No longer builds on iOS.
- **WASM**: WasmBindgen no longer crashes (regression from 0.17.0).

## [0.17.0] - 2025-12-20

### Added

- `DeviceTrait::id` method that returns a stable audio device ID.
- `HostTrait::device_by_id` to select a device by its stable ID.
- `Display` and `FromStr` implementations for `HostId`.
- Support for custom `Host`s, `Device`s, and `Stream`s.
- `Sample::bits_per_sample` method.
- `Copy` implementation to `InputCallbackInfo` and `OutputCallbackInfo`.
- `StreamError::StreamInvalidated` variant for when stream must be rebuilt.
- `StreamError::BufferUnderrun` variant for buffer underrun/overrun notifications.
- `Hash` implementation to `Device` for all backends.
- **AAudio**: `Send` and `Sync` implementations to `Stream`.
- **AAudio**: Support for 12 and 24 kHz sample rates.
- **ALSA**: `I24` and `U24` sample format support (24-bit samples stored in 4 bytes).
- **ALSA**: Support for 12, 24, 352.8, 384, 705.6, and 768 kHz sample rates.
- **ALSA**: `Eq` and `PartialEq` implementations to `Device`.
- **CI**: Native ARM64 Linux support in GitHub Actions.
- **CoreAudio**: `i8`, `i32` and `I24` sample format support (24-bit samples stored in 4 bytes).
- **CoreAudio**: Support for loopback recording (recording system audio output) on macOS > 14.6.
- **CoreAudio**: `Send` implementation to `Stream`.
- **Emscripten**: `BufferSize::Fixed` validation against supported range.
- **iOS**: Complete AVAudioSession integration for device enumeration and buffer size control.
- **JACK**: Support for macOS and Windows platforms.
- **JACK**: `BufferSize::Fixed` validation to reject requests that don't match server buffer size.
- **WASAPI**: Expose `IMMDevice` from WASAPI host Device.
- **WASAPI**: `I24` and `U24` sample format support (24-bit samples stored in 4 bytes).
- **WASAPI**: `Send` and `Sync` implementations to `Stream`.
- **WebAudio**: `Send` and `Sync` implementations to `Stream`.
- **WebAudio**: `BufferSize::Fixed` validation against supported range.

### Changed

- MSRV depends on the platform and at minimum 1.77.
- Set examples to Rust 2021.
- `SampleRate` from struct to `u32` type alias.
- Update `audio_thread_priority` to 0.34.
- Migrate CHANGELOG to [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) format.
- **AAudio**: Configure buffer to ensure consistent callback buffer sizes.
- **AAudio**: Buffer size range detection to query the AudioService property correctly.
- **ALSA**: Improve `BufferSize::Fixed` precision and audio callback performance.
- **ALSA**: `BufferSize::Default` to use the device defaults.
- **ALSA**: Card enumeration to work like `aplay -L` does.
- **ALSA**: Update `alsa` to 0.10.
- **ALSA**: Pass `silent=true` to `PCM.try_recover`, so it doesn't write to stderr.
- **ALSA**: Report buffer underruns/overruns via `StreamError::BufferUnderrun`.
- **ASIO**: Share `sys::Asio` instance across all `Host` instances.
- **CI**: Fix cargo publish to trigger on GitHub releases instead of every master commit.
- **CI**: Replace cargo install commands with cached tool installation for faster builds.
- **CI**: Update actions to latest versions (checkout@v5, rust-cache@v2).
- **CI**: Verify compatibility with windows crates since v0.59.
- **CI**: Test platforms on appropriate MSRV per backend.
- **CI**: Fix `cargo update` syntax for compatibility with Cargo 1.70 (use `-p` flag instead of positional argument).
- **CoreAudio**: `Device::supported_configs` to return a single element containing the available sample rate range when all elements have the same `mMinimum` and `mMaximum` values.
- **CoreAudio**: Default audio device detection to be lazy when building a stream, instead of during device enumeration.
- **CoreAudio**: Configure device buffer to ensure predictable callback buffer sizes.
- **CoreAudio**: Remove `Clone` implementation from `Stream`.
- **JACK**: Use `StreamError::StreamInvalidated` for JACK server sample rate changes.
- **JACK**: Report buffer underruns/overruns via `StreamError::BufferUnderrun`.
- **WASAPI**: Update `windows` to >= 0.59, <= 0.62.

### Fixed

- **ALSA**: Format selection to probe hardware endianness instead of assuming native byte order.
- **ALSA**: Data race in stream shutdown.
- **ASIO**: Handling for `kAsioResetRequest` message to prevent driver UI becoming unresponsive.
- **ASIO**: Buffer silencing logic to work with non-conformant drivers (e.g., FL Studio ASIO).
- **CoreAudio**: Timestamp accuracy.
- **CoreAudio**: Segfaults when enumerating devices.
- **CoreAudio**: Undefined behavior related to null pointers and aligned reads.
- **CoreAudio**: Unnecessary microphone permission requests when using output devices only.
- **iOS**: Example by properly activating audio session.

### Removed

- **WebAudio**: Optional `wee-alloc` feature for security reasons.

## [0.16.0] - 2025-06-07

### Added

- Optional `supports_input`/`output` methods to `DeviceTrait`.
- 384000Hz to `COMMON_SAMPLE_RATES`.
- Constructors for `InputCallbackInfo`, `OutputCallbackInfo` and `StreamInstant`.
- `Default` impl for `Host`.
- `PartialOrd`, `Ord` and `Hash` implementations for `SampleFormat`.
- `Clone`, `PartialEq`, `Eq` and `Hash` implementations for all error enums.
- **ASIO**: Support for int24.

### Changed

- **AAudio**: Migrate from `oboe` to `ndk::audio`. **NOTE:** This raises the minimum Android API version to 26 (Android 8/Oreo).
- **AAudio**: Improve device names.
- **ALSA**: Set realtime priority for stream threads.
- **ALSA**: Improved card enumeration.
- **CoreAudio**: Update `coreaudio-rs` dependency to 0.13.
- **JACK**: Update `jack` dependency to 0.13.
- **WASAPI**: Set realtime priority for stream threads.

### Fixed

- **ALSA**: Don't panic when handling invalid stream timestamps.
- **ALSA**: Fix infinite loop on broken pipes.
- **ASIO**: Fix build failure on Windows.
- **CoreAudio**: Fix callback being called after dropping the stream.
- **CoreAudio**: Fix non-default audio output.
- **CoreAudio**: Fix handling of integer input formats.
- **WASAPI**: Fixed memory leak.
- **WASAPI**: Remove usage of `eval`.

## [0.15.3] - 2024-03-04

### Added

- `try_with_sample_rate`, a non-panicking variant of `with_sample_rate`.
- `#[must_use]` attribute to struct `platform::Stream`.
- `Copy` implementation to enum `SupportedBufferSize` and struct `SupportedStreamConfigRange`.
- `Clone` implementation to `platform::Device`.

### Changed

- **AAudio**: Update `jni` dependency to 0.21.
- **AAudio**: Update `oboe` dependency to 0.6.
- **AAudio**: Update `ndk` dependency to 0.8 and disable `default-features`.
- **ALSA**: Update `alsa` dependency to 0.9.
- **CI**: Update actions, use Android 30 API level in CI, remove `asmjs-unknown-emscripten` target.
- **Examples**: Migrate wasm example to `trunk`, improve syth-thones example.
- **WASAPI**: Update `windows` dependency to v0.54.
- **WebAudio**: Update `wasm-bindgen` to 0.2.89.

### Fixed

- **WebAudio**: Crash on web/wasm when `atomics` flag is enabled.

### Removed

- `parking_lot` dependency in favor of the std library.

## [0.15.2] - 2023-03-30

### Added

- **WebAudio**: Support for multichannel output streams.

### Changed

- **WASAPI**: Update `windows` dependency.

### Fixed

- **WASAPI**: Fix some thread panics.

## [0.15.1] - 2023-03-14

### Added

- **AAudio**: Feature `oboe-shared-stdcxx` to enable `shared-stdcxx` on `oboe` for Android support.

### Changed

- **CoreAudio**: Switch `mach` dependency to `mach2`.

### Removed

- `thiserror` dependency.

## [0.15.0] - 2023-01-29

### Added

- **CoreAudio**: Disconnection detection on Mac OS.

### Changed

- Switch to the `dasp_sample` crate for the sample trait.
- Adopt edition 2021.
- **AAudio**: Update `oboe` dependency.
- **AAudio**: Update `alsa` dependency.
- **CoreAudio**: Update `coreaudio-sys` dependency.
- **Emscripten**: Switch to `web-sys` on the emscripten target.
- **JACK**: Update `jack` dependency.
- **WASAPI**: Update `windows-rs` dependency.

## [0.14.2] - 2022-12-02

### Removed

- `nix` dependency.

## [0.14.1] - 2022-10-23

### Added

- **ALSA**: Support for the 0.6.1 release of `alsa-rs`.
- **NetBSD**: Platform support.

### Changed

- **CI**: Various improvements.

### Fixed

- **ASIO**: Feature broken in 0.14.0.

## [0.14.0] - 2022-08-22

### Changed

- Update `parking_lot` and `once_cell` dependencies.
- **AAudio**: Turn `ndk-glue` into a dev-dependency and use `ndk-context` instead.
- **AAudio**: Update `ndk` and `ndk-glue` dependencies.
- **JACK**: Update `jack` dependency.
- **WASAPI**: Switch to `windows-rs` crate.

## [0.13.5] - 2022-01-28

### Changed

- Faster sample format conversion.
- **AAudio**: Update `ndk`, `oboe`, and `ndk-glue` dependencies.
- **ALSA**: Update `alsa` and `nix` dependencies.
- **JACK**: Update `jack` dependency.

## [0.13.4] - 2021-08-08

### Changed

- **AAudio**: Update `jni` dependency.
- **ALSA**: Improve stream setup parameters.
- **CoreAudio**: Update `core-foundation-sys` dependency.
- **JACK**: Update `rust-jack` dependency.
- **WASAPI**: Allow both threading models and switch the default to STA.

## [0.13.3] - 2021-03-29

### Added

- Give each thread a unique name.

### Fixed

- **ALSA**: Fix distortion regression on some configs.

## [0.13.2] - 2021-03-16

### Changed

- **AAudio**: Update `ndk`, `nix`, `oboe`, and `jni` dependencies.

## [0.13.1] - 2020-11-08

### Changed

- Update `parking_lot` dependency.

### Fixed

- **WASAPI**: Don't panic when device is plugged out on Windows.

## [0.13.0] - 2020-10-28

### Added

- **AAudio**: Android support via `oboe-rs`.
- **CI**: Android APK build and CI job.

## [0.12.1] - 2020-07-23

### Fixed

- **ASIO**: Bugfix release to get the asio feature working again.

## [0.12.0] - 2020-07-09

### Added

- `build_input/output_stream_raw` methods allowing for dynamically handling sample format type.
- `InputCallbackInfo` and `OutputCallbackInfo` types and update expected user data callback function signature to provide these.
- **DragonFly BSD**: Platform support.

### Changed

- Large refactor removing the blocking EventLoop API.
- Rename many `Format` types to `StreamConfig`:
  - `Format` type's `data_type` field renamed to `sample_format`.
  - `Shape` -> `StreamConfig` - The configuration input required to build a stream.
  - `Format` -> `SupportedStreamConfig` - Describes a single supported stream configuration.
  - `SupportedFormat` -> `SupportedStreamConfigRange` - Describes a range of supported configurations.
  - `Device::default_input/output_format` -> `Device::default_input/output_config`.
  - `Device::supported_input/output_formats` -> `Device::supported_input/output_configs`.
  - `Device::SupportedInput/OutputFormats` -> `Device::SupportedInput/OutputConfigs`.
  - `SupportedFormatsError` -> `SupportedStreamConfigsError`.
  - `DefaultFormatError` -> `DefaultStreamConfigError`.
  - `BuildStreamError::FormatNotSupported` -> `BuildStreamError::StreamConfigNotSupported`.
- **WASAPI**: Address deprecated use of `mem::uninitialized`.

### Removed

- `UnknownTypeBuffer` in favour of specifying sample type.

## [0.11.0] - 2019-12-11

### Added

- Name to `HostId`.
- **WASAPI**: `winbase` winapi feature to solve windows compile error issues.

### Changed

- Remove many uses of `std::mem::uninitialized`.
- Panic on stream ID overflow rather than returning an error.
- Move errors into a separate module.
- Switch from `failure` to `thiserror` for error handling.
- **ALSA**: Use `snd_pcm_hw_params_set_buffer_time_near` rather than `set_buffer_time_max`.
- **CI**: Lots of improvements.
- **Examples**: Use `ringbuffer` crate in feedback example.

### Fixed

- **ALSA**: Fix some underruns that could occur.
- **WASAPI**: Fix capture logic.

## [0.10.0] - 2019-07-05

### Added

- New Host API, adding support for alternative audio APIs.
- `StreamEvent` type to allow users to handle stream callback errors.
- **ASIO**: ASIO host, available under Windows.

### Changed

- Remove sleep loop on macOS in favour of using a `Condvar`.
- Overhaul error handling throughout the crate.
- Remove `panic!` from OutputBuffer Deref impl as it is no longer necessary.
- **ALSA**: Remove unnecessary Mutex in favour of channels.
- **CoreAudio**: Update `core-foundation-sys` and `coreaudio-rs` dependencies.
- **WASAPI**: Remove unnecessary Mutex in favour of channels.

## [0.9.0] - 2019-06-06

### Added

- **ALSA**: Error handling for unknown device errors.
- **Emscripten**: `default_output_format` implementation.

### Changed

- Better buffer handling.

### Fixed

- Logic error in frame/sample size.
- **WASAPI**: Fix resuming a paused stream.

## [0.8.2] - 2018-07-03

### Added

- `Display` and `Error` implementations for `DefaultFormatError`.

### Changed

- Upgrade `lazy_static` dependency.

## [0.8.1] - 2018-04-01

### Fixed

- **CoreAudio**: Handling of non-default sample rates for input streams.

## [0.8.0] - 2018-02-15

### Added

- `Device::supported_{input/output}_formats` methods.
- `Device::default_{input/output}_format` methods.
- `default_{input/output}_device` functions.
- `StreamData` type for handling either input or output streams in `EventLoop::run` callback.
- **ALSA**: Input stream support.
- **CoreAudio**: Input stream support.
- **Examples**: `record_wav.rs` example that records 3 seconds to `$CARGO_MANIFEST_DIR/recorded.wav` using default input device.
- **WASAPI**: Input stream support.

### Changed

- Replace usage of `Voice` with `Stream` throughout the crate.
- **Examples**: Update `enumerate.rs` example to display default input/output devices and formats.

### Removed

- `Endpoint` in favour of `Device` for supporting both input and output streams.

## [0.7.0] - 2018-02-04

### Added

- **CoreAudio**: `Endpoint` and `Format` enumeration for macOS.
- **CoreAudio**: Format handling for `build_voice` method.

### Changed

- Rename `ChannelsCount` to `ChannelCount`.
- Rename `SamplesRate` to `SampleRate`.
- Rename the `min_samples_rate` field of `SupportedFormat` to `min_sample_rate`.
- Rename the `with_max_samples_rate()` method of `SupportedFormat` to `with_max_sample_rate()`.
- Rename the `samples_rate` field of `Format` to `sample_rate`.
- Changed the type of the `channels` field of the `SupportedFormat` struct from `Vec<ChannelPosition>` to `ChannelCount` (an alias to `u16`).

### Removed

- Unused ChannelPosition API.

## [0.6.0] - 2017-12-11

### Added

- Improvements to the crate documentation.
- **ALSA**: `pause` and `play` support.

### Changed

- **CoreAudio**: Reduced the number of allocations.
- **Emscripten**: Backend to consume less CPU.

### Fixed

- **CoreAudio**: Fixes for macOS build (#186, #189).

## [0.5.1] - 2017-10-21

### Added

- `Sample::to_i16()`, `Sample::to_u16()` and `Sample::from` methods.

## [0.5.0] - 2017-10-21

### Added

- `EventLoop::build_voice`, `EventLoop::destroy_voice`, `EventLoop::play`, and `EventLoop::pause` methods.
- `VoiceId` struct that is now used to identify a voice owned by an `EventLoop`.

### Changed

- `EventLoop::run()` to take a callback that is called whenever a voice requires sound data.
- `supported_formats()` to produce a list of `SupportedFormat` instead of `Format`. A `SupportedFormat` must then be turned into a `Format` in order to build a voice.

### Removed

- Dependency on the `futures` library.
- `Voice` and `SamplesStream` types.

## [0.4.6] - 2017-10-11

### Added

- **iOS**: Minimal support.

### Changed

- Run rustfmt on the code.

### Fixed

- **BSD**: Fixes for *BSDs.

### Removed

- `get_` prefix of methods.

## [0.4.5] - 2017-04-29

### Changed

- Simplify the Cargo.toml.
- **ALSA**: Bump alsa-sys version number.
- **ALSA**: Mark alsa-sys as linking to alsa.

### Fixed

- **CoreAudio**: SampleStream also holds on to the AudioUnit so it is not dropped.
- **CoreAudio**: Fix for loop in EventLoop::run being optimised out in a release build on macOS.

### Removed

- Stop publishing on gh-pages.

## [0.4.4] - 2017-02-04

### Fixed

- **ALSA**: Pass period instead of buffer to snd_pcm_sw_params_set_avail_min.

## [0.4.3] - 2017-02-01

### Fixed

- **ALSA**: Set sw_params_set_avail_min based on get_params buffer size.

## [0.4.2] - 2017-01-19

### Added

- **CoreAudio**: coreaudio-rs dependency for i686-apple-darwin.

### Deprecated

- Mark deprecated functions as deprecated.

## [0.4.1] - 2016-11-16

### Added

- **ALSA**: Implement play and pause.
- **CoreAudio**: Implement play/pause.

### Fixed

- **WASAPI**: Fix compilation on windows.

## [0.4.0] - 2016-10-01

### Changed

- **ALSA**: Update to futures 0.1.1.
- **WASAPI**: Update to futures 0.1.1.

### Fixed

- **CoreAudio**: Do not lock inner twice. Fixes bug in osx futures 0.1.1 update.
- **CoreAudio**: Try fix the OSX code with futures.

## [0.3.1] - 2016-08-20

### Added

- **WASAPI**: Some documentation to the winapi implementation.

### Changed

- **ALSA**: Bump alsa-sys to 0.1.

### Fixed

- Fix #126.
- Fix most warnings.

## [0.3.0] - 2016-08-12

### Added

- **CoreAudio**: Update backend to new futures-rs oriented design.

### Changed

- Update documentation.
- Use a max buffer size in order to avoid problems.
- Update deps.
- **ALSA**: Make it work on Linux.
- **Null**: Update the null implementation.

## [0.2.12] - 2016-07-10

### Added

- **CoreAudio**: Add get_period to Voice.

### Changed

- **CoreAudio**: Update to coreaudio-rs 0.5.0.

### Fixed

- **CoreAudio**: Correct implementation of get_pending_samples.
- **CoreAudio**: Return correct Voice period.

## [0.2.11] - 2016-04-25

### Fixed

- Be more relaxed with c_void.

## [0.2.10] - 2016-04-22

### Added

- **ALSA**: Add pollfd.

### Fixed

- **ALSA**: Fix underflow detection.
- **Android**: Fix the android build.
- **Android**: Add ARM target.

## [0.2.9] - 2016-01-28

### Added

- **CoreAudio**: Add support for U16/I16 PCM formats.
- **CoreAudio**: Implement some missing functions.

### Changed

- Handle channels positionning.
- Update Cargo.toml after the previous changes.
- Allow for building for mipsel targets.
- **ALSA**: Use correct ALSA channels.
- **CoreAudio**: Implementation cleanup.
- **CoreAudio**: Make Voice Send/Sync.
- **CoreAudio**: Set sample rate to 44100.
- **Examples**: Update the beep example.

### Fixed

- **ALSA**: Fix underflow bug on linux.
- **CI**: Fix for travis build.
- **CoreAudio**: Fix compilation on OSX with the new API for coreaudio-rs.
- **CoreAudio**: Return correct length of buffer, stub unimpl funcs.
- **CoreAudio**: Restore CoreAudio support after API overhaul.
- **Examples**: Add some sane error messages.
- **Examples**: Improve error reporting in beep example.

### Removed

- Do not use a wildcard version number.
- **CoreAudio**: Revert "Add support for U16/I16 PCM formats" (was causing issues).

## [0.2.8] - 2015-11-10

### Changed

- Libc 0.2.
- **WASAPI**: Update winapi.

### Fixed

- **WASAPI**: Catch another 'device not found' error code.

## [0.2.7] - 2015-09-27

### Added

- `Voice::get_period()` method.

## [0.2.6] - 2015-09-22

### Fixed

- **ALSA**: Make sure that all writes succeed.
- **ALSA**: Make the implementation more robust by recovering from underruns.

## [0.2.5] - 2015-09-22

### Added

- `Voice::get_pending_samples` method.

## [0.2.4] - 2015-09-22

### Added

- `endpoint::get_name()` method.
- **Examples**: An enumerate example.
- **WASAPI**: Device name support.

### Changed

- **ALSA**: Correctly enumerate supported formats.

### Fixed

- **ALSA**: Various fixes.
- **ALSA**: Use the correct format.
- **ALSA**: Use the correct device name when enumerating formats.
- **WASAPI**: Fix bug and filter out devices that are not "Output".

## [0.2.3] - 2015-09-22

### Added

- `#[inline]` attributes.
- `underflow()` method to Voice.

### Changed

- Store the format in the public `Voice` struct.
- **WASAPI**: General cleanup.
- **WASAPI**: Update winapi dependency.

### Fixed

- **WASAPI**: Fix the hack in the implementation.

### Removed

- Unused extern crate libc.

## [0.2.2] - 2015-09-11

### Added

- `UnknownBufferType::len()` method.

### Fixed

- **Null**: Restore the null implementation and compile it every time.

## [0.2.1] - 2015-09-10

### Changed

- Handle channels positionning.
- Update Cargo.toml after the previous changes.
- **Examples**: Update the beep example.

### Fixed

- **ALSA**: Fix compilation.

## [0.2.0] - 2015-09-01

### Added

- Proper error handling.
- Supported formats enumeration.
- `endpoint::get_name()` method.

### Changed

- **ALSA**: Make it compile again.
- **WASAPI**: Enable 32bits samples.
- **WASAPI**: Better error handling in format detection.
- **WASAPI**: Now decoding the format from the WAVEFORMAT returned by the winapi.
- **WASAPI**: Handle F32 formats in Voice::new.
- **WASAPI**: Use the format passed as parameter in Voice::new.
- **WASAPI**: Correctly enumerate audio devices (core + wasapi).

### Fixed

- Fix doctests.
- Add more detailed message to panic.

### Removed

- Conversion system.
- Use of box syntax.

## [0.1.2] - 2015-07-22

### Fixed

- **ALSA**: Correct reported sample format.
- **WASAPI**: Fix samples signs on win32.

## [0.1.1] - 2015-07-20

### Fixed

- Fix the version in the README.
- **WASAPI**: Fix the win32 build.

## [0.1.0] - 2015-07-11

### Added

- Bump to 0.1.0.

## [0.0.23] - 2015-07-04

### Fixed

- **WASAPI**: Fix platform-specific dependencies with MSVC.

## [0.0.22] - 2015-06-24

### Fixed

- **ALSA**: Calls to a single ALSA channel are not thread safe.

## [0.0.21] - 2015-06-05

### Changed

- **Examples**: Simplify beep example.
- **WASAPI**: Use shiny new COM.

## [0.0.20] - 2015-04-20

### Changed

- Rustup and version bumps.
- **ALSA**: Remove integer suffixes in alsa-sys.

## [0.0.19] - 2015-04-04

### Changed

- Update for Rustc 1.0.0 beta.

## [0.0.18] - 2015-03-30

### Changed

- Update for change in rustc and winapi.

## [0.0.17] - 2015-03-26

### Changed

- Rustup.
- **ALSA**: Publish alsa-sys before cpal.

## [0.0.16] - 2015-03-25

### Added

- **CoreAudio**: OSX support via the Apple Core Audio, Audio Unit C API. Only supports f32 so far.
- **CoreAudio**: Coreaudio bindings.

### Changed

- Rustup.

### Fixed

- **CI**: Fix travis build.
- **CoreAudio**: Fixed callback to send proper buffersize, removed code in lib where sampleformat affected buffersize.
- **CoreAudio**: Properly shutdown the AudioUnit on drop.

### Removed

- **CoreAudio**: Removed core_audio-sys local bindings in favour of new coreaudio-rs crate.

## [0.0.15] - 2015-02-22

### Changed

- Bump version.
- Update for rustc.

## [0.0.14] - 2015-02-19

### Changed

- Update for rustc.
- **ALSA**: Bump alsa-sys version.
- **ALSA**: Clean up alsa-sys.
- **CI**: Automatically publish on crates.io on successful builds.
- **CI**: Publish alsa-sys too.

## [0.0.13] - 2015-02-12

### Changed

- Update with libc version.

## [0.0.12] - 2015-01-29

### Changed

- Bump version number.

## [0.0.11] - 2015-01-29

### Changed

- Update for rustc.

## [0.0.10] - 2015-01-20

### Added

- **Null**: "null" implementation for platforms that aren't supported.

### Changed

- Changed integer suffix from 'u' to 'us'.
- Bump version number (multiple times).
- Update for rust-1.0 alpha.
- **WASAPI**: Update for winapi.

## [0.0.8] - 2015-01-08

### Changed

- Bump version number.
- Update for Rustc.

## [0.0.7] - 2015-01-05

### Changed

- Update for rustc.

## [0.0.6] - 2014-12-30

### Added

- `#[must_use]` marker for Buffer.

### Changed

- Bump version number.
- Update for changes in rustc.

## [0.0.5] - 2014-12-23

### Added

- `play()` and `pause()` functions.
- Implement f32 to i16 and f32 to u16 conversions.
- Tests for convert_samples_rate.
- Tests for convert_channels.

### Changed

- Cleanup convert_samples_rate.
- Cleanup convert_channels.

### Fixed

- **CI**: Fix the appveyor build.

## [0.0.4] - 2014-12-20

### Changed

- Update for rustc.

## [0.0.3] - 2014-12-17

### Added

- Link to documentation.
- Some documentation.
- Fixes and tests for samples conversions.
- All samples formats.
- Samples formats conversions.
- **CI**: Automatic gh-pages deployment in travis.

### Changed

- Bump version number.
- Improve documentation.
- Use Cow for formats conversions to avoid an allocation and copy.

### Fixed

- Minor README update.
- **CI**: Remove old section from travis.yml.
- **CI**: Fix travis.yml.

### Removed

- Rename `Channel` to `Voice`.

## [0.0.2] - 2014-12-17

### Added

- Basic API.
- Some documentation.
- Keywords.
- Some formats-related functions.
- Some basic data conversion.
- Some samples rate conversions.
- Variable input format system.
- Samples iterator.
- **ALSA**: Basic implementation.
- **ALSA**: alsa-sys library.
- **CI**: Appveyor file.
- **CI**: Config for rust-ci in travis.
- **Examples**: Draft for example music playing.
- **Examples**: Semi-working WASAPI example.
- **WASAPI**: Destructor for wasapi::Channel.

### Changed

- Bump version number.
- Buffer now always has the u8 format.
- Modify API to use a "samples" iterator.
- Change player architecture to avoid data losses.
- Minor nitpicking.
- Update for rustc.
- **ALSA**: Use the official winapi crate.
- **ALSA**: More tweaks for alsa-sys.
- **ALSA**: Minor tweaks in Cargo.toml files.
- **Examples**: Replace example by a smaller one.
- **Examples**: Replace example by a sinusoid generator.
- **Examples**: Rename example to "beep".

### Fixed

- Fix warnings.
- Fix PCM formats conversions not working.
- Fix issue when calling `buffer.samples()` multiple times with the same buffer.
- Sound output now works correctly.
- Minor fixes.
- **WASAPI**: Revert "Switch to retep998/winapi".

### Removed

- Switch back to using buffers.
- Remove old code.

## [0.0.1] - 2014-12-11

### Added

- Initial commit.

[Unreleased]: https://github.com/RustAudio/cpal/compare/v0.17.3...HEAD
[0.17.3]: https://github.com/RustAudio/cpal/compare/v0.17.2...v0.17.3
[0.17.2]: https://github.com/RustAudio/cpal/compare/v0.17.1...v0.17.2
[0.17.1]: https://github.com/RustAudio/cpal/compare/v0.17.0...v0.17.1
[0.17.0]: https://github.com/RustAudio/cpal/compare/v0.16.0...v0.17.0
[0.16.0]: https://github.com/RustAudio/cpal/compare/v0.15.3...v0.16.0
[0.15.3]: https://github.com/RustAudio/cpal/compare/v0.15.2...v0.15.3
[0.15.2]: https://github.com/RustAudio/cpal/compare/v0.15.1...v0.15.2
[0.15.1]: https://github.com/RustAudio/cpal/compare/v0.15.0...v0.15.1
[0.15.0]: https://github.com/RustAudio/cpal/compare/v0.14.2...v0.15.0
[0.14.2]: https://github.com/RustAudio/cpal/compare/v0.14.1...v0.14.2
[0.14.1]: https://github.com/RustAudio/cpal/compare/v0.14.0...v0.14.1
[0.14.0]: https://github.com/RustAudio/cpal/compare/v0.13.5...v0.14.0
[0.13.5]: https://github.com/RustAudio/cpal/compare/v0.13.4...v0.13.5
[0.13.4]: https://github.com/RustAudio/cpal/compare/v0.13.3...v0.13.4
[0.13.3]: https://github.com/RustAudio/cpal/compare/v0.13.2...v0.13.3
[0.13.2]: https://github.com/RustAudio/cpal/compare/v0.13.1...v0.13.2
[0.13.1]: https://github.com/RustAudio/cpal/compare/v0.13.0...v0.13.1
[0.13.0]: https://github.com/RustAudio/cpal/compare/v0.12.1...v0.13.0
[0.12.1]: https://github.com/RustAudio/cpal/compare/v0.12.0...v0.12.1
[0.12.0]: https://github.com/RustAudio/cpal/compare/v0.11.0...v0.12.0
[0.11.0]: https://github.com/RustAudio/cpal/compare/v0.10.0...v0.11.0
[0.10.0]: https://github.com/RustAudio/cpal/compare/v0.9.0...v0.10.0
[0.9.0]: https://github.com/RustAudio/cpal/compare/v0.8.2...v0.9.0
[0.8.2]: https://github.com/RustAudio/cpal/compare/v0.8.1...v0.8.2
[0.8.1]: https://github.com/RustAudio/cpal/compare/v0.8.0...v0.8.1
[0.8.0]: https://github.com/RustAudio/cpal/compare/v0.7.0...v0.8.0
[0.7.0]: https://github.com/RustAudio/cpal/compare/v0.6.0...v0.7.0
[0.6.0]: https://github.com/RustAudio/cpal/compare/v0.5.1...v0.6.0
[0.5.1]: https://github.com/RustAudio/cpal/compare/v0.5.0...v0.5.1
[0.5.0]: https://github.com/RustAudio/cpal/compare/v0.4.6...v0.5.0
[0.4.6]: https://github.com/RustAudio/cpal/compare/v0.4.5...v0.4.6
[0.4.5]: https://github.com/RustAudio/cpal/compare/v0.4.4...v0.4.5
[0.4.4]: https://github.com/RustAudio/cpal/compare/v0.4.3...v0.4.4
[0.4.3]: https://github.com/RustAudio/cpal/compare/v0.4.2...v0.4.3
[0.4.2]: https://github.com/RustAudio/cpal/compare/v0.4.1...v0.4.2
[0.4.1]: https://github.com/RustAudio/cpal/compare/v0.4.0...v0.4.1
[0.4.0]: https://github.com/RustAudio/cpal/compare/v0.3.1...v0.4.0
[0.3.1]: https://github.com/RustAudio/cpal/compare/v0.3.0...v0.3.1
[0.3.0]: https://github.com/RustAudio/cpal/compare/v0.2.12...v0.3.0
[0.2.12]: https://github.com/RustAudio/cpal/compare/v0.2.11...v0.2.12
[0.2.11]: https://github.com/RustAudio/cpal/compare/v0.2.10...v0.2.11
[0.2.10]: https://github.com/RustAudio/cpal/compare/v0.2.9...v0.2.10
[0.2.9]: https://github.com/RustAudio/cpal/compare/v0.2.8...v0.2.9
[0.2.8]: https://github.com/RustAudio/cpal/compare/v0.2.7...v0.2.8
[0.2.7]: https://github.com/RustAudio/cpal/compare/v0.2.6...v0.2.7
[0.2.6]: https://github.com/RustAudio/cpal/compare/v0.2.5...v0.2.6
[0.2.5]: https://github.com/RustAudio/cpal/compare/v0.2.4...v0.2.5
[0.2.4]: https://github.com/RustAudio/cpal/compare/v0.2.3...v0.2.4
[0.2.3]: https://github.com/RustAudio/cpal/compare/v0.2.2...v0.2.3
[0.2.2]: https://github.com/RustAudio/cpal/compare/v0.2.1...v0.2.2
[0.2.1]: https://github.com/RustAudio/cpal/compare/v0.2.0...v0.2.1
[0.2.0]: https://github.com/RustAudio/cpal/compare/v0.1.2...v0.2.0
[0.1.2]: https://github.com/RustAudio/cpal/compare/v0.1.1...v0.1.2
[0.1.1]: https://github.com/RustAudio/cpal/compare/v0.1.0...v0.1.1
[0.1.0]: https://github.com/RustAudio/cpal/compare/v0.0.23...v0.1.0
[0.0.23]: https://github.com/RustAudio/cpal/compare/v0.0.22...v0.0.23
[0.0.22]: https://github.com/RustAudio/cpal/compare/v0.0.21...v0.0.22
[0.0.21]: https://github.com/RustAudio/cpal/compare/v0.0.20...v0.0.21
[0.0.20]: https://github.com/RustAudio/cpal/compare/v0.0.19...v0.0.20
[0.0.19]: https://github.com/RustAudio/cpal/compare/v0.0.18...v0.0.19
[0.0.18]: https://github.com/RustAudio/cpal/compare/v0.0.17...v0.0.18
[0.0.17]: https://github.com/RustAudio/cpal/compare/v0.0.16...v0.0.17
[0.0.16]: https://github.com/RustAudio/cpal/compare/v0.0.15...v0.0.16
[0.0.15]: https://github.com/RustAudio/cpal/compare/v0.0.14...v0.0.15
[0.0.14]: https://github.com/RustAudio/cpal/compare/v0.0.13...v0.0.14
[0.0.13]: https://github.com/RustAudio/cpal/compare/v0.0.12...v0.0.13
[0.0.12]: https://github.com/RustAudio/cpal/compare/v0.0.11...v0.0.12
[0.0.11]: https://github.com/RustAudio/cpal/compare/v0.0.10...v0.0.11
[0.0.10]: https://github.com/RustAudio/cpal/compare/v0.0.8...v0.0.10
[0.0.8]: https://github.com/RustAudio/cpal/compare/v0.0.7...v0.0.8
[0.0.7]: https://github.com/RustAudio/cpal/compare/v0.0.6...v0.0.7
[0.0.6]: https://github.com/RustAudio/cpal/compare/v0.0.5...v0.0.6
[0.0.5]: https://github.com/RustAudio/cpal/compare/v0.0.4...v0.0.5
[0.0.4]: https://github.com/RustAudio/cpal/compare/v0.0.3...v0.0.4
[0.0.3]: https://github.com/RustAudio/cpal/compare/v0.0.2...v0.0.3
[0.0.2]: https://github.com/RustAudio/cpal/compare/v0.0.1...v0.0.2
[0.0.1]: https://github.com/RustAudio/cpal/releases/tag/v0.0.1
```

## File: `CONTRIBUTING.md`
```markdown
# Contributing to cpal

## AI Policy

*In the event of a conflict, this policy supersedes the [rust.audio community guidelines](https://rust.audio/community/ai/) for cpal contributions.*

cpal does not prescribe which tools contributors use. What matters is the quality of the work and the understanding behind it.
Disclosure of AI assistance is generally not required.

### Quality standard

A contribution assisted by AI is held to exactly the same bar as one written by hand. Contributors must understand the problem, the domain, the solution, and the implementation. This applies to code, tests, documentation, commit messages, issues, pull requests, reviews, and discussions alike.

### Cross-platform development

Few contributors have access to every supported target. An AI-assisted implementation for a platform you cannot test is welcome, provided it is clearly labeled as unverified. This signals reviewers that platform-specific validation is needed, not that the work is done.

### Documentation

AI-generated documentation tends to be verbose. Human editing is expected to trim it to what is necessary. Do not document code that is self-explanatory, and avoid comments that risk drifting out of sync with the implementation.

### Copyright and licensing

Contributors are responsible for ensuring their work complies with copyright and IP law. cpal primarily abstracts over publicly documented system audio SDKs, which limits exposure, but does not remove the contributor's responsibility.

We place no restrictions on use of this codebase as AI training data beyond what the Apache 2.0 license already provides.

### Enforcement

Enforcement actions may be taken at the sole discretion of the maintainers, immediately and without prior notice. Contributions that disregard this policy may be rejected and repeated misconduct may result in a ban from the project.
```

## File: `Cargo.toml`
```
[package]
name = "cpal"
version = "0.18.0"
description = "Low-level cross-platform audio I/O library in pure Rust."
repository = "https://github.com/RustAudio/cpal"
documentation = "https://docs.rs/cpal"
license = "Apache-2.0"
keywords = ["audio", "sound"]
edition = "2021"
rust-version = "1.78"

[features]
# Audio thread priority elevation
# Raises the audio callback thread to real-time priority for lower latency and fewer glitches
# Requires: On Linux, either rtkit or appropriate user permissions (e.g. limits.conf or capabilities)
# Platform: Linux, DragonFly BSD, FreeBSD, NetBSD, Windows
audio_thread_priority = ["dep:audio_thread_priority"]

# ASIO backend for Windows
# Provides low-latency audio I/O by bypassing the Windows audio stack
# Requires: ASIO drivers and LLVM/Clang for build-time bindings
# See README for detailed setup instructions
asio = [
    "dep:asio-sys",
    "dep:num-traits",
]

# Audio Worklet backend for WebAssembly
# Provides lower-latency web audio processing compared to default Web Audio API
# Requires: Build with atomics support and Cross-Origin headers for SharedArrayBuffer
# Platform: WebAssembly (wasm32-unknown-unknown)
audioworklet = [
    "wasm-bindgen",
    "web-sys/Blob",
    "web-sys/BlobPropertyBag",
    "web-sys/Url",
    "web-sys/AudioWorklet",
    "web-sys/AudioWorkletNode",
    "web-sys/AudioWorkletNodeOptions",
]

# Support for user-defined custom hosts, devices, and streams
# Allows integration with audio systems not natively supported by CPAL
# See examples/custom.rs for usage
# Platform: All platforms
custom = []

# JACK Audio Connection Kit backend
# Provides low-latency connections between applications and audio hardware
# Requires: JACK server and client libraries installed on the system
# Platform: Linux, DragonFly BSD, FreeBSD, NetBSD, macOS, Windows
# Note: JACK must be installed separately on all platforms
jack = ["dep:jack"]

# PipeWire backend
# Provides audio I/O on Linux and some BSDs via the PipeWire multimedia server
# Requires: PipeWire server and client libraries installed on the system
# Platform: Linux, DragonFly BSD, FreeBSD, NetBSD
pipewire = ["dep:pipewire"]

# PulseAudio backend
# Provides audio I/O support on Linux and some BSDs using the PulseAudio sound server
# Requires: PulseAudio server and client libraries installed on the system
# Platform: Linux, DragonFly BSD, FreeBSD, NetBSD
pulseaudio = ["dep:pulseaudio", "dep:futures"]

# WebAssembly backend using wasm-bindgen
# Enables the Web Audio API backend for browser-based audio
# Required for any WebAssembly audio support
# Platform: WebAssembly (wasm32-unknown-unknown)
# Note: This is typically enabled automatically when targeting wasm32
wasm-bindgen = ["dep:wasm-bindgen", "dep:wasm-bindgen-futures"]

[dependencies]
dasp_sample = "0.11"

[dev-dependencies]
anyhow = "1.0"
hound = "3.5"
ringbuf = "0.4"
clap = { version = ">=4.0, <=4.5.57", features = ["derive"] }

# Support a range of versions in order to avoid duplication of this crate. Make sure to test all
# versions when bumping to a new release, and only increase the minimum when absolutely necessary.
# When updating this, also update the "windows-version" matrix in the CI workflow.
[target.'cfg(target_os = "windows")'.dependencies]
windows = { version = ">=0.59, <=0.62", features = [
    "Win32_Media_Audio",
    "Win32_Foundation",
    "Win32_Devices_Properties",
    "Win32_Media_KernelStreaming",
    "Win32_System_Com_StructuredStorage",
    "Win32_System_Threading",
    "Win32_Security",
    "Win32_System_SystemServices",
    "Win32_System_Variant",
    "Win32_Media_Multimedia",
    "Win32_UI_Shell_PropertiesSystem",
] }
audio_thread_priority = { version = "0.34", optional = true }
asio-sys = { version = "0.3.0", path = "asio-sys", optional = true }
num-traits = { version = "0.2", optional = true }
jack = { version = "0.13", optional = true }

[target.'cfg(any(target_os = "linux", target_os = "dragonfly", target_os = "freebsd", target_os = "netbsd"))'.dependencies]
alsa = "0.11"
libc = "0.2"
audio_thread_priority = { version = "0.34", optional = true }
jack = { version = "0.13", optional = true }
pulseaudio = { version = "0.3", optional = true }
futures = { version = "0.3", optional = true }
pipewire = { version = "0.9", optional = true, features = ["v0_3_53"] }

[target.'cfg(target_vendor = "apple")'.dependencies]
mach2 = "0.5"
coreaudio-rs = { version = "0.14", default-features = false, features = [
    "core_audio",
    "audio_toolbox",
] }
objc2-core-audio = { version = "0.3", default-features = false, features = [
    "std",
    "AudioHardware",
    "AudioHardwareDeprecated",
    "objc2",
    "objc2-foundation",
] }
objc2-audio-toolbox = { version = "0.3", default-features = false, features = [
    "std",
    "AUComponent",
    "AudioUnitProperties",
] }
objc2-core-audio-types = { version = "0.3", default-features = false, features = [
    "std",
    "CoreAudioBaseTypes",
] }
objc2-core-foundation = { version = "0.3" }
objc2-foundation = { version = "0.3" }
objc2 = { version = "0.6" }

[target.'cfg(target_os = "macos")'.dependencies]
jack = { version = "0.13", optional = true }

[target.'cfg(target_os = "ios")'.dependencies]
objc2-avf-audio = { version = "0.3", default-features = false, features = [
    "std",
    "AVAudioSession",
] }

[target.'cfg(target_os = "emscripten")'.dependencies]
wasm-bindgen = { version = "0.2" }
wasm-bindgen-futures = "0.4"
js-sys = { version = "0.3" }
web-sys = { version = "0.3", features = [
    "AudioContext",
    "AudioContextOptions",
    "AudioBuffer",
    "AudioBufferSourceNode",
    "AudioNode",
    "AudioDestinationNode",
    "Window",
    "AudioContextState",
] }

[target.'cfg(all(target_arch = "wasm32", target_os = "unknown"))'.dependencies]
wasm-bindgen = { version = "0.2", optional = true }
wasm-bindgen-futures = { version = "0.4", optional = true }
js-sys = { version = "0.3" }
web-sys = { version = "0.3", features = [
    "AudioContext",
    "AudioContextOptions",
    "AudioBuffer",
    "AudioBufferSourceNode",
    "AudioNode",
    "AudioDestinationNode",
    "Window",
    "AudioContextState",
] }

[target.'cfg(target_os = "android")'.dependencies]
ndk = { version = "0.9", default-features = false, features = [
    "audio",
    "api-level-26",
] }
ndk-context = "0.1"
jni = "0.21"
num-derive = "0.4"
num-traits = "0.2"

[[example]]
name = "beep"

[[example]]
name = "enumerate"

[[example]]
name = "feedback"

[[example]]
name = "record_wav"

[[example]]
name = "synth_tones"

[package.metadata.docs.rs]
all-features = true
rustdoc-args = ["--cfg", "docsrs"]
targets = [
    "x86_64-unknown-linux-gnu",
    "x86_64-pc-windows-msvc",
    "x86_64-apple-darwin",
    "aarch64-apple-darwin",
    "aarch64-apple-ios",
    "wasm32-unknown-unknown",
    "wasm32-unknown-emscripten",
    "aarch64-linux-android",
    "x86_64-unknown-freebsd",
    "x86_64-unknown-netbsd",
    "x86_64-unknown-dragonfly",
]
```

## File: `Cross.toml`
```
[target.armv7-unknown-linux-gnueabihf]
dockerfile = "Dockerfile"

[target.armv7-unknown-linux-gnueabihf.env]
passthrough = ["RUSTFLAGS"]
```

## File: `Dockerfile`
```
ARG CROSS_BASE_IMAGE
FROM $CROSS_BASE_IMAGE

ENV PKG_CONFIG_ALLOW_CROSS=1
ENV PKG_CONFIG_PATH=/usr/lib/arm-linux-gnueabihf/pkgconfig/

RUN dpkg --add-architecture armhf && \
    apt-get update && \
    apt-get install libasound2-dev:armhf -y && \
    apt-get install libjack-jackd2-dev:armhf libjack-jackd2-0:armhf -y
# TODO: now the cross-rs is based on ubuntu:20.04, so it does not contain pipewire-0.3-dev
```

## File: `LICENSE`
```
                                 Apache License
                           Version 2.0, January 2004
                        http://www.apache.org/licenses/

   TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

   1. Definitions.

      "License" shall mean the terms and conditions for use, reproduction,
      and distribution as defined by Sections 1 through 9 of this document.

      "Licensor" shall mean the copyright owner or entity authorized by
      the copyright owner that is granting the License.

      "Legal Entity" shall mean the union of the acting entity and all
      other entities that control, are controlled by, or are under common
      control with that entity. For the purposes of this definition,
      "control" means (i) the power, direct or indirect, to cause the
      direction or management of such entity, whether by contract or
      otherwise, or (ii) ownership of fifty percent (50%) or more of the
      outstanding shares, or (iii) beneficial ownership of such entity.

      "You" (or "Your") shall mean an individual or Legal Entity
      exercising permissions granted by this License.

      "Source" form shall mean the preferred form for making modifications,
      including but not limited to software source code, documentation
      source, and configuration files.

      "Object" form shall mean any form resulting from mechanical
      transformation or translation of a Source form, including but
      not limited to compiled object code, generated documentation,
      and conversions to other media types.

      "Work" shall mean the work of authorship, whether in Source or
      Object form, made available under the License, as indicated by a
      copyright notice that is included in or attached to the work
      (an example is provided in the Appendix below).

      "Derivative Works" shall mean any work, whether in Source or Object
      form, that is based on (or derived from) the Work and for which the
      editorial revisions, annotations, elaborations, or other modifications
      represent, as a whole, an original work of authorship. For the purposes
      of this License, Derivative Works shall not include works that remain
      separable from, or merely link (or bind by name) to the interfaces of,
      the Work and Derivative Works thereof.

      "Contribution" shall mean any work of authorship, including
      the original version of the Work and any modifications or additions
      to that Work or Derivative Works thereof, that is intentionally
      submitted to Licensor for inclusion in the Work by the copyright owner
      or by an individual or Legal Entity authorized to submit on behalf of
      the copyright owner. For the purposes of this definition, "submitted"
      means any form of electronic, verbal, or written communication sent
      to the Licensor or its representatives, including but not limited to
      communication on electronic mailing lists, source code control systems,
      and issue tracking systems that are managed by, or on behalf of, the
      Licensor for the purpose of discussing and improving the Work, but
      excluding communication that is conspicuously marked or otherwise
      designated in writing by the copyright owner as "Not a Contribution."

      "Contributor" shall mean Licensor and any individual or Legal Entity
      on behalf of whom a Contribution has been received by Licensor and
      subsequently incorporated within the Work.

   2. Grant of Copyright License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      copyright license to reproduce, prepare Derivative Works of,
      publicly display, publicly perform, sublicense, and distribute the
      Work and such Derivative Works in Source or Object form.

   3. Grant of Patent License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      (except as stated in this section) patent license to make, have made,
      use, offer to sell, sell, import, and otherwise transfer the Work,
      where such license applies only to those patent claims licensable
      by such Contributor that are necessarily infringed by their
      Contribution(s) alone or by combination of their Contribution(s)
      with the Work to which such Contribution(s) was submitted. If You
      institute patent litigation against any entity (including a
      cross-claim or counterclaim in a lawsuit) alleging that the Work
      or a Contribution incorporated within the Work constitutes direct
      or contributory patent infringement, then any patent licenses
      granted to You under this License for that Work shall terminate
      as of the date such litigation is filed.

   4. Redistribution. You may reproduce and distribute copies of the
      Work or Derivative Works thereof in any medium, with or without
      modifications, and in Source or Object form, provided that You
      meet the following conditions:

      (a) You must give any other recipients of the Work or
          Derivative Works a copy of this License; and

      (b) You must cause any modified files to carry prominent notices
          stating that You changed the files; and

      (c) You must retain, in the Source form of any Derivative Works
          that You distribute, all copyright, patent, trademark, and
          attribution notices from the Source form of the Work,
          excluding those notices that do not pertain to any part of
          the Derivative Works; and

      (d) If the Work includes a "NOTICE" text file as part of its
          distribution, then any Derivative Works that You distribute must
          include a readable copy of the attribution notices contained
          within such NOTICE file, excluding those notices that do not
          pertain to any part of the Derivative Works, in at least one
          of the following places: within a NOTICE text file distributed
          as part of the Derivative Works; within the Source form or
          documentation, if provided along with the Derivative Works; or,
          within a display generated by the Derivative Works, if and
          wherever such third-party notices normally appear. The contents
          of the NOTICE file are for informational purposes only and
          do not modify the License. You may add Your own attribution
          notices within Derivative Works that You distribute, alongside
          or as an addendum to the NOTICE text from the Work, provided
          that such additional attribution notices cannot be construed
          as modifying the License.

      You may add Your own copyright statement to Your modifications and
      may provide additional or different license terms and conditions
      for use, reproduction, or distribution of Your modifications, or
      for any such Derivative Works as a whole, provided Your use,
      reproduction, and distribution of the Work otherwise complies with
      the conditions stated in this License.

   5. Submission of Contributions. Unless You explicitly state otherwise,
      any Contribution intentionally submitted for inclusion in the Work
      by You to the Licensor shall be under the terms and conditions of
      this License, without any additional terms or conditions.
      Notwithstanding the above, nothing herein shall supersede or modify
      the terms of any separate license agreement you may have executed
      with Licensor regarding such Contributions.

   6. Trademarks. This License does not grant permission to use the trade
      names, trademarks, service marks, or product names of the Licensor,
      except as required for reasonable and customary use in describing the
      origin of the Work and reproducing the content of the NOTICE file.

   7. Disclaimer of Warranty. Unless required by applicable law or
      agreed to in writing, Licensor provides the Work (and each
      Contributor provides its Contributions) on an "AS IS" BASIS,
      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
      implied, including, without limitation, any warranties or conditions
      of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A
      PARTICULAR PURPOSE. You are solely responsible for determining the
      appropriateness of using or redistributing the Work and assume any
      risks associated with Your exercise of permissions under this License.

   8. Limitation of Liability. In no event and under no legal theory,
      whether in tort (including negligence), contract, or otherwise,
      unless required by applicable law (such as deliberate and grossly
      negligent acts) or agreed to in writing, shall any Contributor be
      liable to You for damages, including any direct, indirect, special,
      incidental, or consequential damages of any character arising as a
      result of this License or out of the use or inability to use the
      Work (including but not limited to damages for loss of goodwill,
      work stoppage, computer failure or malfunction, or any and all
      other commercial damages or losses), even if such Contributor
      has been advised of the possibility of such damages.

   9. Accepting Warranty or Additional Liability. While redistributing
      the Work or Derivative Works thereof, You may choose to offer,
      and charge a fee for, acceptance of support, warranty, indemnity,
      or other liability obligations and/or rights consistent with this
      License. However, in accepting such obligations, You may act only
      on Your own behalf and on Your sole responsibility, not on behalf
      of any other Contributor, and only if You agree to indemnify,
      defend, and hold each Contributor harmless for any liability
      incurred by, or claims asserted against, such Contributor by reason
      of your accepting any such warranty or additional liability.

   END OF TERMS AND CONDITIONS

   APPENDIX: How to apply the Apache License to your work.

      To apply the Apache License to your work, attach the following
      boilerplate notice, with the fields enclosed by brackets "[]"
      replaced with your own identifying information. (Don't include
      the brackets!)  The text should be enclosed in the appropriate
      comment syntax for the file format. We also recommend that a
      file or class name and description of purpose be included on the
      same "printed page" as the copyright notice for easier
      identification within third-party archives.

   Copyright [yyyy] [name of copyright owner]

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
```

## File: `README.md`
```markdown
# CPAL - Cross-Platform Audio Library

[![Actions Status](https://github.com/RustAudio/cpal/workflows/cpal/badge.svg)](https://github.com/RustAudio/cpal/actions)
[![Crates.io](https://img.shields.io/crates/v/cpal.svg)](https://crates.io/crates/cpal) [![docs.rs](https://docs.rs/cpal/badge.svg)](https://docs.rs/cpal/)

Low-level library for audio input and output in pure Rust.

## Minimum Supported Rust Version (MSRV)

The minimum Rust version required depends on which audio backend and features you're using, as each platform has different dependencies:

- **AAudio (Android):** Rust **1.85**
- **ALSA (Linux/BSD):** Rust **1.82**
- **CoreAudio (macOS/iOS):** Rust **1.80**
- **JACK (Linux/BSD/macOS/Windows):** Rust **1.82**
- **PipeWire (Linux/BSD):** Rust **1.85**
- **PulseAudio (Linux/BSD):** Rust **1.88**
- **WASAPI/ASIO (Windows):** Rust **1.82**
- **WASM (`wasm32-unknown`):** Rust **1.85**
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
| `asio` | Windows | ASIO backend for low-latency audio, bypassing the Windows audio stack. Requires ASIO drivers and LLVM/Clang. See the [ASIO setup guide](#asio-on-windows). |
| `audioworklet` | WebAssembly (`wasm32-unknown-unknown`) | Audio Worklet backend for lower-latency web audio than the default Web Audio API, running audio on a dedicated thread. Requires atomics support (`RUSTFLAGS="-C target-feature=+atomics,+bulk-memory,+mutable-globals"`) and `Cross-Origin` headers for `SharedArrayBuffer`. See the `audioworklet-beep` example. |
| `custom` | All | User-defined host implementations for audio systems not natively supported by CPAL. See `examples/custom.rs`. |
| `jack` | Linux, BSD, macOS, Windows | JACK Audio Connection Kit backend for pro-audio routing and inter-application connectivity. Requires `libjack-jackd2-dev` (Debian/Ubuntu) or `jack-devel` (Fedora). |
| `pipewire` | Linux, BSD | PipeWire media server backend. Requires `libpipewire-0.3-dev` (Debian/Ubuntu) or `pipewire-devel` (Fedora). |
| `pulseaudio` | Linux, BSD | PulseAudio sound server backend. Requires `libpulse-dev` (Debian/Ubuntu) or `pulseaudio-libs-devel` (Fedora). |
| `wasm-bindgen` | WebAssembly (`wasm32-unknown-unknown`) | Web Audio API backend for browser-based audio; required for any WebAssembly audio support. See the `wasm-beep` example. |

See the [beep example](examples/beep.rs) for selecting the host at runtime.

## ASIO on Windows

### Locating the ASIO SDK

The location of ASIO SDK is exposed to CPAL by setting the `CPAL_ASIO_DIR` environment variable.

The build script will try to find the ASIO SDK by following these steps in order:

1. Check if `CPAL_ASIO_DIR` is set and if so use the path to point to the SDK.
2. Check if the ASIO SDK is already installed in the temporary directory, if so use that and set the path of `CPAL_ASIO_DIR` to the output of `std::env::temp_dir().join("asio_sdk")`.
3. If the ASIO SDK is not already installed, download it from <https://www.steinberg.net/asiosdk> and install it in the temporary directory. The path of `CPAL_ASIO_DIR` will be set to the output of `std::env::temp_dir().join("asio_sdk")`.

In an ideal situation you don't need to worry about this step.

### Preparing the Build Environment

1. **Install LLVM/Clang**: `bindgen`, the library used to generate bindings to the C++ SDK, requires clang. Download and install LLVM from <http://releases.llvm.org/download.html> under the "Pre-Built Binaries" section.

2. **Set LIBCLANG_PATH**: Add the LLVM `bin` directory to a `LIBCLANG_PATH` environment variable. If you installed LLVM to the default directory, this should work in the command prompt:
   ```
   setx LIBCLANG_PATH "C:\Program Files\LLVM\bin"
   ```

3. **Install ASIO Drivers** (optional for testing): If you don't have any ASIO devices or drivers available, you can download and install ASIO4ALL from <http://www.asio4all.org/>. Be sure to enable the "offline" feature during installation.

4. **Visual Studio**: The build script assumes Microsoft Visual Studio is installed. It will try to find `vcvarsall.bat` and execute it with the right host and target architecture. If needed, you can manually execute it:
   ```
   "C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\VC\Auxiliary\Build\vcvarsall.bat" amd64
   ```
   For more information see the [vcvarsall.bat documentation](https://docs.microsoft.com/en-us/cpp/build/building-on-the-command-line).

### Using ASIO in Your Application

1. **Enable the feature** in your `Cargo.toml`:
   ```toml
   cpal = { version = "*", features = ["asio"] }
   ```

2. **Select the ASIO host** in your code:
   ```rust
   let host = cpal::host_from_id(cpal::HostId::Asio)
       .expect("failed to initialise ASIO host");
   ```

### Troubleshooting

If you encounter compilation errors from `asio-sys` or `bindgen`:
- Verify `CPAL_ASIO_DIR` is set correctly
- Try running `cargo clean`
- Ensure LLVM/Clang is properly installed and `LIBCLANG_PATH` is set

### Cross-Compilation

When Windows is the host and target OS, the build script supports all cross-compilation targets supported by the MSVC compiler.

It is also possible to compile Windows applications with ASIO support on Linux and macOS using the MinGW-w64 toolchain.

**Requirements:**
- Include the MinGW-w64 include directory in your `CPLUS_INCLUDE_PATH` environment variable
- Include the LLVM include directory in your `CPLUS_INCLUDE_PATH` environment variable

**Example for macOS** (targeting `x86_64-pc-windows-gnu` with `mingw-w64` installed via brew):
```
export CPLUS_INCLUDE_PATH="$CPLUS_INCLUDE_PATH:/opt/homebrew/Cellar/mingw-w64/11.0.1/toolchain-x86_64/x86_64-w64-mingw32/include"
```

## Troubleshooting

### No Default Device Available

If you receive errors about no default input or output device:

- **Linux/PipeWire:** Check that PipeWire is running: `pw-cli info`
- **Linux/PulseAudio:** Check that PulseAudio is running: `pulseaudio --check`
- **macOS:** Check System Preferences > Sound for available devices
- **Mobile (iOS/Android):** Ensure your app has microphone/audio permissions
- **Windows:** Verify your audio device is enabled in Sound Settings

## ALSA, PipeWire, and PulseAudio

When PipeWire or PulseAudio is running, it holds the ALSA `default` device exclusively. A second stream attempting to open it via the ALSA backend will fail with a `DeviceBusy` error. To route audio through the sound server via ALSA, use the bridge devices `pipewire` or `pulse` instead of `default`. Better yet, use the `pipewire` or `pulseaudio` cpal features for native integration.

Reserve `hw:` and `plughw:` device names for targets that have no sound server. On those targets, ensure the user is a member of the `audio` group if the system does not grant audio device access automatically via `logind`.

### Buffer Size Issues

`BufferSize::Default` uses the system-configured device default, which on **ALSA** can range from a PipeWire quantum (typically 1024 frames) to `u32::MAX` on misconfigured or exotic hardware. A very deep buffer causes samples to be consumed far faster than audible playback, making audio appear to fast-forward ahead of actual output.

Configure the system and/or request a fixed size in your application:

| System | File | Setting |
|--------|------|---------|
| ALSA | `~/.asoundrc` or `/etc/asound.conf` | `buffer_size`, `periods` * `period_size` |
| PipeWire | `~/.config/pipewire/pipewire.conf.d/` | `default.clock.quantum` |
| PulseAudio | `~/.config/pulse/daemon.conf` | `default-fragments` * `default-fragment-size-msec` |

```rust
config.buffer_size = cpal::BufferSize::Fixed(1024);
```

Query `device.default_output_config()?.buffer_size()` for valid ranges. Smaller buffers reduce latency but increase CPU load and the risk of glitches.

### Build Errors

If you are unable to build the library:

- Verify you have installed the required development libraries, as documented above
- **ASIO on Windows:** Verify `LIBCLANG_PATH` is set and LLVM is installed

## Examples

CPAL comes with several examples in `examples/`.

Run an example with:
```bash
cargo run --example beep
```

For platform-specific features, enable the relevant features:
```bash
cargo run --example beep --features asio        # Windows ASIO backend
cargo run --example beep --features jack        # JACK backend
cargo run --example beep --features pipewire    # PipeWire backend
cargo run --example beep --features pulseaudio  # PulseAudio backend
```

## Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## Resources

- **Documentation:** [docs.rs/cpal](https://docs.rs/cpal)
- **Examples:** [examples/](examples/) directory in this repository
- **Discord:** Join the [#cpal channel](https://discord.gg/vPmmSgJSPV) for questions and discussion
- **GitHub:** [Report issues](https://github.com/RustAudio/cpal/issues) and [view source code](https://github.com/RustAudio/cpal)
- **RustAudio:** Part of the [RustAudio organization](https://github.com/RustAudio)

## License

Licensed under the Apache License, Version 2.0. See [LICENSE](LICENSE) for details.
```

## File: `UPGRADING.md`
```markdown
# Upgrading from v0.17 to v0.18

This guide covers breaking changes requiring code updates. See [CHANGELOG.md](CHANGELOG.md) for the complete list of changes and improvements.

## Breaking Changes Checklist

- [ ] Add wildcard arms to exhaustive `match` expressions on cpal error enums
- [ ] Optionally handle the new `DeviceBusy` variant for retryable device errors
- [ ] Change `build_*_stream` call sites to pass `StreamConfig` by value (drop the `&`)
- [ ] For custom hosts, change `DeviceTrait` implementations to accept `StreamConfig` by value.

## 1. Error enums are now `#[non_exhaustive]`

**What changed:** Public error enums in `cpal` are now marked `#[non_exhaustive]`.

```rust
// Before (v0.17)
match device.default_output_config() {
    Ok(config) => config,
    Err(DefaultStreamConfigError::DeviceNotAvailable) => panic!("device gone"),
    Err(DefaultStreamConfigError::StreamTypeNotSupported) => panic!("unsupported"),
    Err(DefaultStreamConfigError::BackendSpecific { err }) => panic!("{err}"),
}

// After (v0.18)
loop {
    match device.default_output_config() {
        Ok(config) => break config,
        Err(DefaultStreamConfigError::DeviceBusy) => {
            std::thread::sleep(std::time::Duration::from_millis(100));
        }
        Err(DefaultStreamConfigError::DeviceNotAvailable) => panic!("device gone"),
        Err(DefaultStreamConfigError::StreamTypeNotSupported) => panic!("unsupported"),
        Err(DefaultStreamConfigError::BackendSpecific { err }) => panic!("{err}"),
        Err(_) => panic!("unknown error"),
    }
}
```

**Why:** This lets cpal add new variants in future minor releases without a SemVer-breaking change.

## 2. New `DeviceBusy` variant

**What changed:** On ALSA, `EBUSY`/`EAGAIN` errors from device open calls now produce `DeviceBusy` instead of `DeviceNotAvailable`. This may be added to other hosts in the future.

**Why:** Unlike `DeviceNotAvailable` (device is gone), `DeviceBusy` signals a transient condition. Retrying after a short delay may succeed, as shown in the example above.

## 3. `StreamConfig` is now passed by value

**What changed:** `StreamConfig` now implements `Copy`, and all `DeviceTrait` stream-building methods accept it by value.

```rust
// Before (v0.17)
let stream = device.build_output_stream(&config, data_fn, err_fn, None)?;

// After (v0.18)
let stream = device.build_output_stream(config, data_fn, err_fn, None)?;
```

**Impact:** Remove the `&` at every `build_*_stream` call site. Because `StreamConfig` is `Copy`, you can reuse the same binding across multiple calls without cloning.

If you implement `DeviceTrait` on your own type (via the `custom` feature), update your `build_input_stream_raw` and `build_output_stream_raw` signatures from `config: &StreamConfig` to `config: StreamConfig`. Any `config.clone()` calls before `move` closures can also be removed.

---

# Upgrading from v0.16 to v0.17

## Breaking Changes Checklist

- [ ] Replace `SampleRate(n)` with plain `n` values
- [ ] Update `windows` crate to >= 0.59, <= 0.62 (Windows only)
- [ ] Update `alsa` crate to 0.11 (Linux only)
- [ ] Remove `wee_alloc` feature from Wasm builds (if used)
- [ ] Wrap CoreAudio streams in `Arc` if you were cloning them (macOS only)
- [ ] Handle `BuildStreamError::StreamConfigNotSupported` for `BufferSize::Fixed` (JACK, strict validation)
- [ ] Update device name matching if using ALSA (Linux only)

**Recommended migrations:**
- [ ] Replace deprecated `device.name()` calls with `device.description()` or `device.id()`

---

## 1. SampleRate is now a u32 type alias

**What changed:** `SampleRate` changed from a struct to a `u32` type alias.

```rust
// Before (v0.16)
use cpal::SampleRate;
let config = StreamConfig {
    channels: 2,
    sample_rate: SampleRate(44100),
    buffer_size: BufferSize::Default,
};

// After (v0.17)
let config = StreamConfig {
    channels: 2,
    sample_rate: 44100,
    buffer_size: BufferSize::Default,
};
```

**Impact:** Remove `SampleRate()` constructor calls. The type is now just `u32`, so use integer literals or variables directly.

## 2. Device::name() deprecated (soft deprecation)

**What changed:** `Device::name()` is deprecated in favor of `id()` and `description()`.

```rust
// Old (still works but shows deprecation warning)
let name = device.name()?;

// New: For user-facing display
let desc = device.description()?;
println!("Device: {}", desc);  // or desc.name() for just the name

// New: For stable identification and persistence
let id = device.id()?;
let id_string = id.to_string();  // Save this
// Later...
let device = host.device_by_id(&id_string.parse()?)?;
```

**Impact:** Deprecation warnings only. The old API still works in v0.17. Update when convenient to prepare for future versions.

**Why:** Separates stable device identification (`id()`) from human-readable names (`description()`).

## 3. CoreAudio Stream no longer Clone (macOS)

**What changed:** On macOS, `Stream` no longer implements `Clone`. Use `Arc` instead.

```rust
// Before (v0.16) - macOS only
let stream = device.build_output_stream(&config, data_fn, err_fn, None)?;
let stream_clone = stream.clone();

// After (v0.17) - all platforms
let stream = Arc::new(device.build_output_stream(&config, data_fn, err_fn, None)?);
let stream_clone = Arc::clone(&stream);
```

**Why:** Removed as part of making `Stream` implement `Send` on macOS.

## 4. BufferSize behavior changes

### BufferSize::Default now uses host defaults

**What changed:** `BufferSize::Default` now defers to the audio host/device defaults instead of applying cpal's opinionated defaults.

**Impact:** Buffer sizes may differ from v0.16, affecting latency characteristics:
- **Latency will vary** based on host/device defaults (which may be lower, higher, or similar)
- **May underrun or have different latency** depending on what the host chooses
- **Better integration** with system audio configuration: cpal now respects configured settings instead of imposing its own buffers. For example, on ALSA, PipeWire quantum settings (via the pipewire-alsa device) are now honored instead of being overridden.

**Migration:** If you experience underruns, fast-forwarding behavior or need specific latency, use `BufferSize::Fixed(size)` instead of relying on possibly misconfigured system defaults.

**Platform-specific notes:**
- **ALSA:** Previously used cpal's hardcoded 25ms periods / 100ms buffer, now uses device defaults
- **All platforms:** Default buffer sizes now match what the host audio system expects

### BufferSize::Fixed validation changes

**What changed:** Several backends now have different validation behavior for `BufferSize::Fixed`:

- **ALSA:** Now uses `set_buffer_size_near()` for improved hardware compatibility with devices requiring byte-alignment, power-of-two sizes, or other alignment constraints (was: exact size via `set_buffer_size()`, which would reject unsupported sizes)
- **JACK:** Must exactly match server buffer size (was: silently ignored)
- **Emscripten/WebAudio:** Validates min/max range
- **ASIO:** Stricter lower bound validation

```rust
// Handle validation errors
let mut config = StreamConfig {
    channels: 2,
    sample_rate: 44100,
    buffer_size: BufferSize::Fixed(512),
};

match device.build_output_stream(&config, data_fn, err_fn, None) {
    Ok(stream) => { /* success */ },
    Err(BuildStreamError::StreamConfigNotSupported) => {
        config.buffer_size = BufferSize::Default;  // Fallback
        device.build_output_stream(&config, data_fn, err_fn, None)?
    },
    Err(e) => return Err(e),
}
```

**JACK users:** Use `BufferSize::Default` to automatically match the server's configured size.

## 5. Dependency updates

Update these dependencies if you use them directly:

```toml
[dependencies]
cpal = "0.17"

# Platform-specific (if used directly):
alsa = "0.11"  # Linux only
windows = { version = ">=0.59, <=0.62" }  # Windows only
audio_thread_priority = "0.34"  # All platforms
```

## 6. ALSA device enumeration changed (Linux)

**What changed:** Device enumeration now returns all devices from `aplay -L`. v0.16 had a regression that only returned card names, missing all device variants.

* v0.16: Only card names ("Loopback", "HDA Intel PCH")
* v0.17: All aplay -L devices (default, hw:CARD=X,DEV=Y, plughw:, front:, surround51:, etc.)

**Impact:** Many more devices will be enumerated. Device names/IDs will be much more detailed. Update any code that matches specific ALSA device names.

## 7. Wasm wee_alloc feature removed

**What changed:** The optional `wee_alloc` feature was removed for security reasons.

```toml
# Before (v0.16)
cpal = { version = "0.16", features = ["wasm-bindgen", "wee_alloc"] }

# After (v0.17)
cpal = { version = "0.17", features = ["wasm-bindgen"] }
```

## Notable Non-Breaking Improvements

v0.17 also includes significant improvements that don't require code changes:

- **Stable device IDs:** New `device.id()` returns persistent device identifiers that survive reboots/reconnections. Use `host.device_by_id()` to reliably select saved devices.
- **Streams are Send+Sync everywhere:** All platforms now support moving/sharing streams across threads
- **24-bit sample formats:** Added `I24`/`U24` support on ALSA, CoreAudio, WASAPI, ASIO
- **Custom host support:** Implement your own `Host`/`Device`/`Stream` for proprietary platforms
- **Predictable buffer sizes:** CoreAudio and AAudio now ensure consistent callback buffer sizes
- **Expanded sample rate support:** ALSA supports 12, 24, 352.8, 384, 705.6, and 768 kHz
- **WASAPI advanced interop:** Exposed `IMMDevice` for Windows COM interop scenarios
- **Platform improvements:** macOS loopback recording (14.6+), improved ALSA audio callback performance, improved timestamp accuracy, iOS AVAudioSession integration, JACK on all platforms

See [CHANGELOG.md](CHANGELOG.md) for complete details and [examples/](examples/) for updated usage patterns.

---

## Getting Help

- Full details: [CHANGELOG.md](CHANGELOG.md)
- Examples: [examples/](examples/)
- Issues: https://github.com/RustAudio/cpal/issues
```

## File: `build.rs`
```rust
use std::env;

const CPAL_ASIO_DIR: &str = "CPAL_ASIO_DIR";

fn main() {
    println!("cargo:rerun-if-env-changed={CPAL_ASIO_DIR}");
    if env::var(CPAL_ASIO_DIR).is_ok() {
        println!("cargo:rustc-cfg=asio");
    }
}
```

## File: `rustfmt.toml`
```
edition = "2021"
```

## File: `asio-sys/.gitignore`
```
/target
Cargo.lock
```

## File: `asio-sys/CHANGELOG.md`
```markdown
# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Added `Driver::latencies()`
- `asio_message` now dispatches `kAsioResyncRequest` and `kAsioLatenciesChanged` to callbacks
  instead of silently ignoring them
- `sample_rate_did_change` now dispatches `AsioDriverEvent::SampleRateChanged` to registered
  callbacks when the reported rate differs from the last known rate

### Changed
- `Driver::add_message_callback` and `Driver::remove_message_callback` replaced by
  `Driver::add_event_callback` and `Driver::remove_event_callback`
- `MessageCallback` renamed to `DriverEventCallback`, and `MessageCallbackId` renamed to
  `DriverEventCallbackId`. `DriverEventCallback` wraps `Fn(AsioDriverEvent) -> bool` where
  `AsioDriverEvent` is a new enum covering both `asioMessage` selector events and
  `sampleRateDidChange` notifications
- `CallbackId` renamed to `BufferCallbackId`
- Public-facing `c_long` fields and return types replaced with `i32`
- Public-facing `c_double` parameters and return types replaced with `f64`.
- `Driver::latencies()` now returns `Latencies { input, output }`.
- `Driver::buffersize_range()` now returns `BufferSizeRange { min, max }`.
- `CallbackInfo::system_time` is now `u64` nanoseconds.
- `AsioError::ASE_NoMemory` renamed to `AsioError::NoMemory`.
- `AsioTime::reserved`, `AsioTimeInfo::reserved`, `AsioTimeCode::future` fields made private.
- `asio_import` module is now `pub(crate)`; raw bindgen types are no longer public API
- `asio_message` delegates `kAsioSelectorSupported` for unknown selectors to registered
  callbacks, so each host decides which capabilities it opts into

### Fixed
- `Asio::load_driver` now returns `LoadDriverError::LoadDriverFailed` instead of panicking when the 
  driver name contains a null byte
- Fixed TOCTOU race condition when creating streams concurrently
- `Driver::set_sample_rate` now performs a dummy buffer cycle and driver reload when
  the driver does not apply the rate change immediately, as required by some drivers
  (e.g. Steinberg)
- Fixed `asio_message` not advertising `kAsioSelectorSupported` itself as a supported selector
- Fixed data race where `channels`, `latencies`, `sample_rate`, and related query methods could
  call ASIO concurrently during `set_sample_rate`'s teardown/reload

### Removed
- Removed unused `SampleRate` struct
- `DriverState` is no longer part of the public API

## [0.2.6] - 2026-02-18

### Fixed
- Link `advapi32` to resolve Windows Registry API symbols

## [0.2.5] - 2026-01-04

### Fixed
- Fixed ASIO SDK discovery on case sensitive filesystems

## [0.2.4] - 2025-12-20

### Fixed
- Fixed docs.rs documentation build by generating stub bindings when building for docs.rs
- Fixed buffer switch detection to work correctly with non-conformant ASIO drivers

## [0.2.3] - 2025-12-12

### Added
- Added `edition = "2021"` and `rust-version = "1.70"` to Cargo.toml
- Added README.md with usage documentation
- Added CHANGELOG.md following Keep a Changelog format
- Added rustfmt.toml for consistent formatting

### Changed
- Update `bindgen` to 0.72
- Update `cc` to 1.2
- Update `parse_cfg` to 4.1
- Update enumerate example to use `pub type SampleRate = u32` instead of `pub struct SampleRate(pub u32)` for consistency with cpal

### Fixed
- Fix linker flags for MinGW cross-compilation
- Add `packed(4)` to representation of ASIO time structs in bindings
- Fix handling for `kAsioResetRequest` message to prevent driver UI becoming unresponsive
- Fix timeinfo flags type

## [0.2.2] - 2024-03-04

### Added
- Automate ASIO SDK download during build (no longer requires manual download)
- Add support for `CPAL_ASIO_DIR` environment variable to use local SDK

### Changed
- Update `bindgen` to 0.59
- Switch to `once_cell` from `lazy_static`
- Improve build script error messages and SDK detection
- Clean up build script structure
- Re-run build script when `CPAL_ASIO_DIR` changes

### Fixed
- Fix segmentation fault during build on some systems
- Fix various compiler warnings
- Fix typos in code and comments

## [0.2.1] - 2021-11-26

### Changed
- Update `bindgen` to 0.56

### Fixed
- Fix some typos and warnings

## [0.2.0] - 2020-07-22

### Changed
- Update repository URL to https://github.com/RustAudio/cpal/

## [0.1.0] - 2020-07-22

Initial release.

### Added
- FFI bindings to Steinberg ASIO SDK
- Automatic binding generation using bindgen
- Support for MSVC toolchain on Windows
- Basic error types: `AsioError`, `LoadDriverError`

[Unreleased]: https://github.com/RustAudio/cpal/compare/asio-sys-v0.2.6...HEAD
[0.2.6]: https://github.com/RustAudio/cpal/compare/asio-sys-v0.2.5...asio-sys-v0.2.6
[0.2.5]: https://github.com/RustAudio/cpal/compare/asio-sys-v0.2.4...asio-sys-v0.2.5
[0.2.4]: https://github.com/RustAudio/cpal/compare/asio-sys-v0.2.3...asio-sys-v0.2.4
[0.2.3]: https://github.com/RustAudio/cpal/compare/asio-sys-v0.2.2...asio-sys-v0.2.3
[0.2.2]: https://github.com/RustAudio/cpal/compare/asio-sys-v0.2.1...asio-sys-v0.2.2
[0.2.1]: https://github.com/RustAudio/cpal/compare/asio-sys-v0.2.0...asio-sys-v0.2.1
[0.2.0]: https://github.com/RustAudio/cpal/compare/asio-sys-v0.1.0...asio-sys-v0.2.0
[0.1.0]: https://github.com/RustAudio/cpal/releases/tag/asio-sys-v0.1.0
```

## File: `asio-sys/Cargo.toml`
```
[package]
name = "asio-sys"
version = "0.3.0"
authors = ["Tom Gowan <tomrgowan@gmail.com>"]
description = "Low-level interface and binding generation for the steinberg ASIO SDK."
repository = "https://github.com/RustAudio/cpal/"
documentation = "https://docs.rs/asio-sys"
license = "Apache-2.0"
keywords = ["audio", "sound", "asio", "steinberg"]
edition = "2021"
rust-version = "1.82"

[build-dependencies]
bindgen = "0.72"
walkdir = "2"
cc = "1.2"
parse_cfg = "4.1"

[dependencies]
num-derive = "0.4"
num-traits = "0.2"

[package.metadata.docs.rs]
default-target = "x86_64-pc-windows-msvc"
targets = []
```

## File: `asio-sys/README.md`
```markdown
# asio-sys

[![Crates.io](https://img.shields.io/crates/v/asio-sys.svg)](https://crates.io/crates/asio-sys)
[![Documentation](https://docs.rs/asio-sys/badge.svg)](https://docs.rs/asio-sys)
[![License](https://img.shields.io/crates/l/asio-sys.svg)](https://github.com/RustAudio/cpal/blob/master/LICENSE)

Low-level Rust bindings for the [Steinberg ASIO SDK](https://www.steinberg.net/developers/).

ASIO (Audio Stream Input/Output) is a low-latency audio API for Windows that provides direct hardware access, bypassing the Windows audio stack for minimal latency.

## Overview

`asio-sys` provides raw FFI bindings to the ASIO SDK, automatically generated using [bindgen](https://rust-lang.github.io/rust-bindgen/). This crate is used by [cpal](https://crates.io/crates/cpal)'s ASIO backend to provide low-latency audio on Windows.

**Note:** Most users should use [cpal](https://crates.io/crates/cpal)'s safe, cross-platform API rather than using `asio-sys` directly.

## Features

- Automatic binding generation from ASIO SDK headers
- Low-level access to ASIO driver functionality
- Support for both MSVC and MinGW toolchains
- Automated ASIO SDK download and setup during build

## Requirements

### Windows

- **LLVM/Clang**: Required for bindgen to generate bindings
  - Install via [LLVM downloads](https://releases.llvm.org/) or `choco install llvm`
- **ASIO SDK**: Automatically downloaded during build from Steinberg
  - Or set `CPAL_ASIO_DIR` environment variable to point to a local SDK

### Build Dependencies

- `bindgen` - Generates Rust bindings from C/C++ headers
- `cc` - Compiles the ASIO SDK C++ files
- `walkdir` - Finds SDK files

## Usage

Add to your `Cargo.toml`:

```toml
[dependencies]
asio-sys = "0.2"
```

### Example

```rust
use asio_sys as sys;

fn main() {
    // Load ASIO driver
    let driver_name = "ASIO4ALL v2"; // Your ASIO driver name

    unsafe {
        // Initialize ASIO
        let drivers = sys::get_driver_names();
        println!("Available drivers: {drivers:?}");

        // Load a driver
        match sys::load_asio_driver(driver_name) {
            Ok(driver) => println!("Loaded driver: {driver_name}"),
            Err(e) => eprintln!("Failed to load driver: {e:?}"),
        }
    }
}
```

## Environment Variables

- `CPAL_ASIO_DIR`: Path to ASIO SDK directory (optional)
  - If not set, the SDK is automatically downloaded during build
  - Example: `set CPAL_ASIO_DIR=C:\path\to\asiosdk`

## Platform Support

- **Windows** (MSVC and MinGW)
  - x86_64 (64-bit)
  - i686 (32-bit)

ASIO is Windows-only. This crate will not build on other platforms.

## Safety

This crate provides raw FFI bindings to C++ code. Almost all functions are `unsafe` and require careful handling:

- Memory management is manual
- Callbacks must be properly synchronized
- Driver state must be carefully managed
- See [ASIO SDK documentation](https://www.steinberg.net/developers/) for details

## License

Licensed under the Apache License, Version 2.0. See [LICENSE](../LICENSE) for details.

The ASIO SDK is owned by Steinberg Media Technologies GmbH. Users must comply with Steinberg's licensing terms.

## Contributing

Contributions are welcome! Please submit issues and pull requests to the [cpal repository](https://github.com/RustAudio/cpal).

## Resources

- [ASIO SDK Documentation](https://www.steinberg.net/developers/)
- [cpal Documentation](https://docs.rs/cpal)
- [RustAudio Community](https://github.com/RustAudio)
- [Discord](https://discord.gg/vPmmSgJSPV): #cpal Channel
```

## File: `asio-sys/asio_stub_bindings.rs`
```rust
// Stub bindings for docs.rs
// These are minimal type and function definitions to allow documentation generation
// without requiring the actual ASIO SDK.

use std::os::raw::{c_char, c_double, c_void};

// On Windows (the only platform where ASIO actually runs), c_long is i32.
// On non-Windows platforms (for docs.rs and local testing), redefine c_long as i32 to match.
#[cfg(target_os = "windows")]
use std::os::raw::c_long;
#[cfg(not(target_os = "windows"))]
type c_long = i32;

pub type ASIOBool = c_long;
pub type ASIOError = c_long;
pub type ASIOSampleRate = c_double;

#[repr(C)]
#[derive(Debug, Copy, Clone)]
pub struct ASIOSamples {
    pub hi: u32,
    pub lo: u32,
}

#[repr(C)]
#[derive(Debug, Copy, Clone)]
pub struct ASIOTimeStamp {
    pub hi: u32,
    pub lo: u32,
}

#[repr(C)]
#[derive(Debug, Copy, Clone)]
pub struct ASIODriverInfo {
    pub asioVersion: c_long,
    pub driverVersion: c_long,
    pub name: [c_char; 32],
    pub errorMessage: [c_char; 124],
    pub sysRef: *mut c_void,
}

#[repr(C)]
#[derive(Debug, Copy, Clone)]
pub struct ASIOChannelInfo {
    pub channel: c_long,
    pub isInput: ASIOBool,
    pub isActive: ASIOBool,
    pub channelGroup: c_long,
    pub type_: c_long,
    pub name: [c_char; 32],
}

#[repr(C)]
#[derive(Debug, Copy, Clone)]
pub struct ASIOBufferInfo {
    pub isInput: ASIOBool,
    pub channelNum: c_long,
    pub buffers: [*mut c_void; 2],
}

#[repr(C)]
#[derive(Debug, Copy, Clone)]
pub struct ASIOCallbacks {
    pub bufferSwitch: *const c_void,
    pub sampleRateDidChange: *const c_void,
    pub asioMessage: *const c_void,
    pub bufferSwitchTimeInfo: *const c_void,
}

#[repr(C)]
#[derive(Debug, Copy, Clone)]
pub struct AsioTimeInfo {
    pub speed: c_double,
    pub systemTime: ASIOTimeStamp,
    pub samplePosition: ASIOSamples,
    pub sampleRate: ASIOSampleRate,
    pub flags: c_long,
    pub reserved: [c_char; 12],
}

#[repr(C)]
#[derive(Debug, Copy, Clone)]
pub struct ASIOTimeCode {
    pub speed: c_double,
    pub timeCodeSamples: ASIOSamples,
    pub flags: c_long,
    pub future: [c_char; 64],
}

#[repr(C)]
#[derive(Debug, Copy, Clone)]
pub struct ASIOTime {
    pub reserved: [c_long; 4],
    pub timeInfo: AsioTimeInfo,
    pub timeCode: ASIOTimeCode,
}

#[repr(transparent)]
#[derive(Debug, Copy, Clone)]
pub struct AsioTimeInfoFlags(pub u32);

impl AsioTimeInfoFlags {
    pub const kSystemTimeValid: Self = Self(1);
    pub const kSamplePositionValid: Self = Self(1 << 1);
}

impl std::ops::BitOr for AsioTimeInfoFlags {
    type Output = Self;
    fn bitor(self, rhs: Self) -> Self {
        Self(self.0 | rhs.0)
    }
}

#[repr(transparent)]
#[derive(Debug, Copy, Clone)]
pub struct ASIOTimeCodeFlags(pub u32);

// Stub functions (will never be called on docs.rs)
#[no_mangle]
pub unsafe extern "C" fn ASIOInit(_info: *mut ASIODriverInfo) -> ASIOError {
    0
}
#[no_mangle]
pub unsafe extern "C" fn ASIOExit() -> ASIOError {
    0
}
#[no_mangle]
pub unsafe extern "C" fn ASIOStart() -> ASIOError {
    0
}
#[no_mangle]
pub unsafe extern "C" fn ASIOStop() -> ASIOError {
    0
}
#[no_mangle]
pub unsafe extern "C" fn ASIOGetChannels(_ins: *mut c_long, _outs: *mut c_long) -> ASIOError {
    0
}
#[no_mangle]
pub unsafe extern "C" fn ASIOGetLatencies(
    _in_latency: *mut c_long,
    _out_latency: *mut c_long,
) -> ASIOError {
    0
}
#[no_mangle]
pub unsafe extern "C" fn ASIOGetChannelInfo(_info: *mut ASIOChannelInfo) -> ASIOError {
    0
}
#[no_mangle]
pub unsafe extern "C" fn ASIOCreateBuffers(
    _infos: *mut ASIOBufferInfo,
    _num: c_long,
    _size: c_long,
    _callbacks: *mut ASIOCallbacks,
) -> ASIOError {
    0
}
#[no_mangle]
pub unsafe extern "C" fn ASIODisposeBuffers() -> ASIOError {
    0
}
#[no_mangle]
pub unsafe extern "C" fn ASIOGetBufferSize(
    _min: *mut c_long,
    _max: *mut c_long,
    _pref: *mut c_long,
    _gran: *mut c_long,
) -> ASIOError {
    0
}
#[no_mangle]
pub unsafe extern "C" fn ASIOGetSamplePosition(
    _pos: *mut ASIOSamples,
    _stamp: *mut ASIOTimeStamp,
) -> ASIOError {
    0
}
#[no_mangle]
pub unsafe extern "C" fn ASIOOutputReady() -> ASIOError {
    0
}

#[no_mangle]
pub unsafe extern "C" fn get_driver_names(_names: *mut *mut c_char, _max: c_long) -> c_long {
    0
}
#[no_mangle]
pub unsafe extern "C" fn load_asio_driver(_name: *mut c_char) -> bool {
    false
}
#[no_mangle]
pub unsafe extern "C" fn remove_current_driver() {}
#[no_mangle]
pub unsafe extern "C" fn get_sample_rate(_rate: *mut c_double) -> ASIOError {
    0
}
#[no_mangle]
pub unsafe extern "C" fn set_sample_rate(_rate: c_double) -> ASIOError {
    0
}
#[no_mangle]
pub unsafe extern "C" fn can_sample_rate(_rate: c_double) -> ASIOError {
    0
}
```

## File: `asio-sys/build.rs`
```rust
extern crate bindgen;
extern crate cc;
extern crate parse_cfg;
extern crate walkdir;

use parse_cfg::*;
use std::env;
use std::path::{Path, PathBuf};
use std::process::Command;
use walkdir::WalkDir;

const CPAL_ASIO_DIR: &str = "CPAL_ASIO_DIR";
const ASIO_SDK_URL: &str = "https://www.steinberg.net/asiosdk";

const ASIO_HEADER: &str = "asio.h";
const ASIO_SYS_HEADER: &str = "asiosys.h";
const ASIO_DRIVERS_HEADER: &str = "asiodrivers.h";

/// Checks if the host OS is Windows
fn host_os_is_windows() -> bool {
    std::env::consts::OS == "windows"
}

/// Checks if the target env is MSVC
fn is_msvc() -> bool {
    let target: Target = std::env::var("TARGET")
        .expect("Target not set.")
        .parse()
        .expect("Unable to parse target.");

    let target_env = match target {
        Target::Triple { env, .. } => env,
        Target::Cfg(_) => panic!("cfg targets not supported"),
    };

    if let Some(env) = target_env {
        env.contains("msvc")
    } else {
        false
    }
}

fn main() {
    // When building on docs.rs, skip the actual build and generate stub bindings
    if std::env::var("DOCS_RS").is_ok() {
        println!("cargo:warning=Building for docs.rs - generating stub bindings");
        let out_dir = PathBuf::from(env::var("OUT_DIR").expect("bad path"));
        create_stub_bindings(&out_dir);
        return;
    }

    println!("cargo:rerun-if-env-changed={}", CPAL_ASIO_DIR);

    // ASIO SDK directory
    let cpal_asio_dir = get_asio_dir();
    println!("cargo:rerun-if-changed={}", cpal_asio_dir.display());

    // Directory where bindings and library are created
    let out_dir = PathBuf::from(env::var("OUT_DIR").expect("bad path"));

    // Check if library exists,
    // if it doesn't create it
    let mut lib_path = out_dir.clone();
    lib_path.push("libasio.a");
    if !lib_path.exists() {
        if is_msvc() {
            invoke_vcvars_if_not_set();
        }
        create_lib(&cpal_asio_dir);
    }

    // Print out links to needed libraries
    println!("cargo:rustc-link-lib=dylib=advapi32");
    println!("cargo:rustc-link-lib=dylib=ole32");
    println!("cargo:rustc-link-lib=dylib=user32");
    println!("cargo:rustc-link-search={}", out_dir.display());
    println!("cargo:rustc-link-lib=static=asio");
    println!("cargo:rustc-cfg=asio");

    // Check if bindings exist
    // If they don't create them
    let mut binding_path = out_dir.clone();
    binding_path.push("asio_bindings.rs");
    if !binding_path.exists() {
        if is_msvc() {
            invoke_vcvars_if_not_set();
        }
        create_bindings(&cpal_asio_dir);
    }
}

fn create_lib(cpal_asio_dir: &Path) {
    let mut cpp_paths: Vec<PathBuf> = Vec::new();
    let mut host_dir = cpal_asio_dir.to_path_buf();
    let mut pc_dir = cpal_asio_dir.to_path_buf();
    let mut common_dir = cpal_asio_dir.to_path_buf();
    host_dir.push("host");
    common_dir.push("common");
    pc_dir.push("host/pc");

    // Gathers cpp files from directories
    let walk_a_dir = |dir_to_walk, paths: &mut Vec<PathBuf>| {
        for entry in WalkDir::new(dir_to_walk).max_depth(1) {
            let entry = match entry {
                Err(e) => {
                    println!("error: {}", e);
                    continue;
                }
                Ok(entry) => entry,
            };
            match entry.path().extension().and_then(|s| s.to_str()) {
                None => continue,
                Some("cpp") => {
                    // Skip macos bindings
                    if entry.path().file_name().unwrap().to_str() == Some("asiodrvr.cpp") {
                        continue;
                    }
                    paths.push(entry.path().to_path_buf())
                }
                Some(_) => continue,
            };
        }
    };

    // Get all cpp files for building SDK library
    walk_a_dir(host_dir, &mut cpp_paths);
    walk_a_dir(pc_dir, &mut cpp_paths);
    walk_a_dir(common_dir, &mut cpp_paths);

    // build the asio lib
    cc::Build::new()
        .include(format!("{}/{}", cpal_asio_dir.display(), "host"))
        .include(format!("{}/{}", cpal_asio_dir.display(), "common"))
        .include(format!("{}/{}", cpal_asio_dir.display(), "host/pc"))
        .include("asio-link/helpers.hpp")
        .file("asio-link/helpers.cpp")
        .files(cpp_paths)
        .cpp(true)
        .compile("libasio.a");
}

/// Creates stub bindings for docs.rs
///
/// Since docs.rs builds in a sandboxed environment without network access
/// and cannot cross-compile Windows MSVC targets with C++ dependencies,
/// we generate minimal stub bindings that allow documentation to be built.
fn create_stub_bindings(out_dir: &Path) {
    let stub_content = include_str!("asio_stub_bindings.rs");
    let binding_path = out_dir.join("asio_bindings.rs");
    std::fs::write(&binding_path, stub_content).expect("Failed to write stub bindings");
}

fn create_bindings(cpal_asio_dir: &PathBuf) {
    let mut asio_header = None;
    let mut asio_sys_header = None;
    let mut asio_drivers_header = None;

    // Recursively walk given cpal dir to find required headers
    for entry in WalkDir::new(cpal_asio_dir) {
        let entry = match entry {
            Err(_) => continue,
            Ok(entry) => entry,
        };
        let file_name = match entry.path().file_name().and_then(|s| s.to_str()) {
            None => continue,
            Some(file_name) => file_name,
        };

        match file_name {
            ASIO_HEADER => asio_header = Some(entry.path().to_path_buf()),
            ASIO_SYS_HEADER => asio_sys_header = Some(entry.path().to_path_buf()),
            ASIO_DRIVERS_HEADER => asio_drivers_header = Some(entry.path().to_path_buf()),
            _ => (),
        }
    }

    macro_rules! header_or_panic {
        ($opt_header:expr, $FILE_NAME:expr) => {
            match $opt_header.as_ref() {
                None => {
                    panic!(
                        "Could not find {} in {}: {}",
                        $FILE_NAME,
                        CPAL_ASIO_DIR,
                        cpal_asio_dir.display()
                    );
                }
                Some(path) => path.to_str().expect("Could not convert path to str"),
            }
        };
    }

    // Only continue if found all headers that we need
    let asio_header = header_or_panic!(asio_header, ASIO_HEADER);
    let asio_sys_header = header_or_panic!(asio_sys_header, ASIO_SYS_HEADER);
    let asio_drivers_header = header_or_panic!(asio_drivers_header, ASIO_DRIVERS_HEADER);

    // The bindgen::Builder is the main entry point
    // to bindgen, and lets you build up options for
    // the resulting bindings.
    let bindings = bindgen::Builder::default()
        // The input header we would like to generate
        // bindings for.
        .header(asio_header)
        .header(asio_sys_header)
        .header(asio_drivers_header)
        .header("asio-link/helpers.hpp")
        .clang_arg("-x")
        .clang_arg("c++")
        .clang_arg("-std=c++14")
        .clang_arg(format!("-I{}/{}", cpal_asio_dir.display(), "host/pc"))
        .clang_arg(format!("-I{}/{}", cpal_asio_dir.display(), "host"))
        .clang_arg(format!("-I{}/{}", cpal_asio_dir.display(), "common"))
        // Need to whitelist to avoid binding tp c++ std::*
        .allowlist_type("AsioDrivers")
        .allowlist_type("AsioDriver")
        .allowlist_type("ASIOTime")
        .allowlist_type("ASIOTimeInfo")
        .allowlist_type("ASIODriverInfo")
        .allowlist_type("ASIOBufferInfo")
        .allowlist_type("ASIOCallbacks")
        .allowlist_type("ASIOSamples")
        .allowlist_type("ASIOSampleType")
        .allowlist_type("ASIOSampleRate")
        .allowlist_type("ASIOChannelInfo")
        .allowlist_type("AsioTimeInfoFlags")
        .allowlist_type("ASIOTimeCodeFlags")
        .allowlist_function("ASIOGetChannels")
        .allowlist_function("ASIOGetChannelInfo")
        .allowlist_function("ASIOGetBufferSize")
        .allowlist_function("ASIOGetLatencies")
        .allowlist_function("ASIOGetSamplePosition")
        .allowlist_function("ASIOOutputReady")
        .allowlist_function("get_sample_rate")
        .allowlist_function("set_sample_rate")
        .allowlist_function("can_sample_rate")
        .allowlist_function("ASIOInit")
        .allowlist_function("ASIOCreateBuffers")
        .allowlist_function("ASIOStart")
        .allowlist_function("ASIOStop")
        .allowlist_function("ASIODisposeBuffers")
        .allowlist_function("ASIOExit")
        .allowlist_function("load_asio_driver")
        .allowlist_function("remove_current_driver")
        .allowlist_function("get_driver_names")
        .bitfield_enum("AsioTimeInfoFlags")
        .bitfield_enum("ASIOTimeCodeFlags")
        // Finish the builder and generate the bindings.
        .generate()
        // Unwrap the Result and panic on failure.
        .expect("Unable to generate bindings");

    // Write the bindings to the $OUT_DIR/bindings.rs file.
    let out_path = PathBuf::from(env::var("OUT_DIR").expect("bad path"));

    bindings
        .write_to_file(out_path.join("asio_bindings.rs"))
        .expect("Couldn't write bindings!");
}

/// Gets the ASIO SDK directory
///
/// If the CPAL_ASIO_DIR env var is set, it will use that.
///
/// If not set, it will check the temp directory for the ASIO SDK.
///
/// If not found, it will download the ASIO SDK to the temp directory.
///
/// It will then move the contents of the inner directory to the temp directory.
///
/// It will then return the path to the ASIO SDK directory.
fn get_asio_dir() -> PathBuf {
    // Check if CPAL_ASIO_DIR env var is set
    if let Ok(path) = env::var(CPAL_ASIO_DIR) {
        println!("CPAL_ASIO_DIR is set at {path}");
        return PathBuf::from(path);
    }

    // If not set, check temp directory for ASIO SDK, maybe it is previously downloaded
    let temp_dir = env::temp_dir();
    let asio_dir = temp_dir.join("asio_sdk");
    if asio_dir.exists() {
        println!("CPAL_ASIO_DIR is set at {}", asio_dir.display());
        return asio_dir;
    }

    // If not found, download ASIO SDK using PowerShell's Invoke-WebRequest
    println!("CPAL_ASIO_DIR is not set or contents are cached downloading from {ASIO_SDK_URL}",);

    download_asio_sdk_to_temp_dir(&temp_dir);

    // Move the contents of the inner directory to asio_dir
    for entry in walkdir::WalkDir::new(&temp_dir).min_depth(1).max_depth(1) {
        let entry = entry.unwrap();
        if entry.file_type().is_dir()
            && entry
                .file_name()
                .to_string_lossy()
                .to_lowercase()
                .starts_with("asio")
        {
            std::fs::rename(entry.path(), &asio_dir).expect("Failed to rename directory");
            break;
        }
    }
    println!("CPAL_ASIO_DIR is set at {}", asio_dir.display());
    asio_dir
}

/// Downloads the ASIO SDK to the temp directory of the host OS
///
/// It uses powershell's Invoke-WebRequest on Windows and curl on other platforms to download the SDK.
///
/// It then extracts the SDK using powershell's Expand-Archive on Windows and unzip on other platforms.
fn download_asio_sdk_to_temp_dir(temp_dir: &Path) {
    let asio_zip_path = temp_dir.join("asio_sdk.zip");
    if host_os_is_windows() {
        let status = Command::new("powershell")
            .args([
                "-NoProfile",
                "-Command",
                &format!(
                    "Invoke-WebRequest -Uri {ASIO_SDK_URL} -OutFile {}",
                    asio_zip_path.display()
                ),
            ])
            .status()
            .expect("Failed to execute PowerShell command");

        if !status.success() {
            panic!("Failed to download ASIO SDK");
        }
        println!("Downloaded ASIO SDK successfully");

        // Unzip using PowerShell's Expand-Archive
        println!("Extracting ASIO SDK..");
        let status = Command::new("powershell")
            .args([
                "-NoProfile",
                "-Command",
                &format!(
                    "Expand-Archive -Path {} -DestinationPath {} -Force",
                    asio_zip_path.display(),
                    temp_dir.display()
                ),
            ])
            .status()
            .expect("Failed to execute PowerShell command for extracting ASIO SDK");

        if !status.success() {
            panic!("Failed to extract ASIO SDK");
        }
    } else {
        let status = Command::new("sh")
            .arg("-c")
            .arg(&format!(
                "curl -L --fail --output {} {}",
                asio_zip_path.display(),
                "https://www.steinberg.net/asiosdk" // Replace with the actual ASIO SDK URL
            ))
            .status()
            .expect("Failed to execute curl command");

        if !status.success() {
            panic!("Failed to download ASIO SDK");
        }
        println!("Downloaded ASIO SDK successfully");

        // Extract using `unzip`
        println!("Extracting ASIO SDK..");
        let status = Command::new("unzip")
            .args([
                "-o",
                asio_zip_path.to_str().unwrap(),
                "-d",
                temp_dir.to_str().unwrap(),
            ])
            .status()
            .expect("Failed to execute unzip command for extracting ASIO SDK");

        if !status.success() {
            panic!("Failed to extract ASIO SDK");
        }
    }
}

/// Invokes `vcvarsall.bat` to initialize the environment for building with MSVC
///
/// This function is only meant to be called when the host OS is Windows.
fn invoke_vcvars_if_not_set() {
    if vcvars_set() {
        return;
    }
    println!("VCINSTALLDIR is not set. Attempting to invoke vcvarsall.bat..");

    println!("Invoking vcvarsall.bat..");
    println!("Determining system architecture..");

    let arch_arg = determine_vcvarsall_bat_arch_arg();
    println!(
        "Host architecture is detected as {}.",
        std::env::consts::ARCH
    );
    println!("Architecture argument for vcvarsall.bat will be used as: {arch_arg}.");

    let vcvars_all_bat_path = search_vcvars_all_bat();

    println!(
        "Found vcvarsall.bat at {}. Initializing environment..",
        vcvars_all_bat_path.display()
    );

    // Invoke vcvarsall.bat
    let output = Command::new("cmd")
        .args([
            "/c",
            vcvars_all_bat_path.to_str().unwrap(),
            &arch_arg,
            "&&",
            "set",
        ])
        .output()
        .expect("Failed to execute command");

    for line in String::from_utf8_lossy(&output.stdout).lines() {
        // Filters the output of vcvarsall.bat to only include lines of the form "VARNAME=VALUE"
        let parts: Vec<&str> = line.splitn(2, '=').collect();
        if parts.len() == 2 {
            env::set_var(parts[0], parts[1]);
            println!("{}={}", parts[0], parts[1]);
        }
    }
}

/// Checks if vcvarsall.bat has been invoked
/// Assumes that it is very unlikely that the user would set `VCINSTALLDIR` manually
fn vcvars_set() -> bool {
    env::var("VCINSTALLDIR").is_ok()
}

/// Searches for vcvarsall.bat in the default installation directories
///
/// If it is not found, it will search for it in the Program Files directories
///
/// If it is still not found, it will panic.
fn search_vcvars_all_bat() -> PathBuf {
    if let Some(path) = guess_vcvars_all_bat() {
        return path;
    }

    // Define search paths for vcvarsall.bat based on architecture
    let paths = &[
        // Visual Studio 2022+
        "C:\\Program Files\\Microsoft Visual Studio\\",
        // <= Visual Studio 2019
        "C:\\Program Files (x86)\\Microsoft Visual Studio\\",
    ];

    // Search for vcvarsall.bat using walkdir
    println!("Searching for vcvarsall.bat in {paths:?}");

    let mut found = None;

    for path in paths.iter() {
        for entry in WalkDir::new(path)
            .into_iter()
            .filter_map(Result::ok)
            .filter(|e| !e.file_type().is_dir())
        {
            if entry.path().ends_with("vcvarsall.bat") {
                found.replace(entry.path().to_path_buf());
            }
        }
    }

    match found {
        Some(path) => path,
        None => panic!(
            "Could not find vcvarsall.bat. Please install the latest version of Visual Studio."
        ),
    }
}

/// Guesses the location of vcvarsall.bat by searching it with certain heuristics.
///
/// It is meant to be executed before a top level search over Microsoft Visual Studio directories
/// to ensure faster execution in CI environments.
fn guess_vcvars_all_bat() -> Option<PathBuf> {
    /// Checks if a string is a year
    fn is_year(s: Option<&str>) -> Option<String> {
        let Some(s) = s else {
            return None;
        };

        if s.len() == 4 && s.chars().all(|c| c.is_ascii_digit()) {
            Some(s.to_string())
        } else {
            None
        }
    }

    /// Checks if a string is an edition of Visual Studio
    fn is_edition(s: Option<&str>) -> Option<String> {
        let Some(s) = s else {
            return None;
        };

        let editions = ["Enterprise", "Professional", "Community", "Express"];
        if editions.contains(&s) {
            Some(s.to_string())
        } else {
            None
        }
    }

    /// Constructs a path to vcvarsall.bat based on a base path
    fn construct_path(base: &Path) -> Option<PathBuf> {
        let mut constructed = base.to_path_buf();
        for entry in WalkDir::new(&constructed).max_depth(1) {
            let entry = match entry {
                Err(_) => continue,
                Ok(entry) => entry,
            };
            if let Some(year) = is_year(entry.path().file_name().and_then(|s| s.to_str())) {
                constructed = constructed.join(year);
                for entry in WalkDir::new(&constructed).max_depth(1) {
                    let entry = match entry {
                        Err(_) => continue,
                        Ok(entry) => entry,
                    };
                    if let Some(edition) =
                        is_edition(entry.path().file_name().and_then(|s| s.to_str()))
                    {
                        constructed = constructed
                            .join(edition)
                            .join("VC")
                            .join("Auxiliary")
                            .join("Build")
                            .join("vcvarsall.bat");

                        return Some(constructed);
                    }
                }
            }
        }
        None
    }

    let vs_2022_and_onwards_base = PathBuf::from("C:\\Program Files\\Microsoft Visual Studio\\");
    let vs_2019_and_2017_base = PathBuf::from("C:\\Program Files (x86)\\Microsoft Visual Studio\\");

    construct_path(&vs_2022_and_onwards_base).map_or_else(
        || construct_path(&vs_2019_and_2017_base).map_or_else(|| None, Some),
        Some,
    )
}

/// Determines the right argument to pass to `vcvarsall.bat` based on the host and target architectures.
///
/// Windows on ARM is not supporting 32 bit arm processors.
/// Because of this there is no native or cross compilation is supported for 32 bit arm processors.
fn determine_vcvarsall_bat_arch_arg() -> String {
    let host_architecture = std::env::consts::ARCH;
    let target_architecture = std::env::var("CARGO_CFG_TARGET_ARCH").expect("Target not set.");

    let arch_arg = if target_architecture == "x86_64" {
        if host_architecture == "x86" {
            // Arg for cross compilation from x86 to x64
            "x86_amd64"
        } else if host_architecture == "x86_64" {
            // Arg for native compilation from x64 to x64
            "amd64"
        } else if host_architecture == "aarch64" {
            // Arg for cross compilation from arm64 to amd64
            "arm64_amd64"
        } else {
            panic!("Unsupported host architecture {}", host_architecture);
        }
    } else if target_architecture == "x86" {
        if host_architecture == "x86" {
            // Arg for native compilation from x86 to x86
            "x86"
        } else if host_architecture == "x86_64" {
            // Arg for cross compilation from x64 to x86
            "amd64_x86"
        } else if host_architecture == "aarch64" {
            // Arg for cross compilation from arm64 to x86
            "arm64_x86"
        } else {
            panic!("Unsupported host architecture {}", host_architecture);
        }
    } else if target_architecture == "arm" {
        if host_architecture == "x86" {
            // Arg for cross compilation from x86 to arm
            "x86_arm"
        } else if host_architecture == "x86_64" {
            // Arg for cross compilation from x64 to arm
            "amd64_arm"
        } else if host_architecture == "aarch64" {
            // Arg for cross compilation from arm64 to arm
            "arm64_arm"
        } else {
            panic!("Unsupported host architecture {}", host_architecture);
        }
    } else if target_architecture == "aarch64" {
        if host_architecture == "x86" {
            // Arg for cross compilation from x86 to arm
            "x86_arm64"
        } else if host_architecture == "x86_64" {
            // Arg for cross compilation from x64 to arm
            "amd64_arm64"
        } else if host_architecture == "aarch64" {
            // Arg for native compilation from arm64 to arm64
            "arm64"
        } else {
            panic!("Unsupported host architecture {}", host_architecture);
        }
    } else {
        panic!("Unsupported target architecture.");
    };

    arch_arg.to_owned()
}
```

## File: `asio-sys/rustfmt.toml`
```
edition = "2021"
```

## File: `asio-sys/asio-link/helpers.cpp`
```cpp
#include "helpers.hpp"
#include <stdio.h>

extern "C" ASIOError get_sample_rate(double * rate){
	return ASIOGetSampleRate(reinterpret_cast<ASIOSampleRate *>(rate));
}

extern "C" ASIOError set_sample_rate(double rate){
	return ASIOSetSampleRate(rate);
}

extern "C" ASIOError can_sample_rate(double rate){
	return ASIOCanSampleRate(rate);
}

extern AsioDrivers* asioDrivers;
bool loadAsioDriver(char *name);

extern "C" bool load_asio_driver(char * name){
	return loadAsioDriver(name);
}

extern "C" void remove_current_driver() {
	asioDrivers->removeCurrentDriver();
}
extern "C" long get_driver_names(char **names, long maxDrivers) {
	AsioDrivers ad;
	return ad.getDriverNames(names, maxDrivers);
}
```

## File: `asio-sys/asio-link/helpers.hpp`
```
#pragma once
#include "asiodrivers.h"
#include "asio.h"

// Helper function to wrap confusing preprocessor
extern "C" ASIOError get_sample_rate(double * rate);

// Helper function to wrap confusing preprocessor
extern "C" ASIOError set_sample_rate(double rate);

// Helper function to wrap confusing preprocessor
extern "C" ASIOError can_sample_rate(double rate);

extern "C" bool load_asio_driver(char * name);
extern "C" void remove_current_driver();
extern "C" long get_driver_names(char **names, long maxDrivers);
```

## File: `asio-sys/examples/enumerate.rs`
```rust
/* This example aims to produce the same behaviour
 * as the enumerate example in cpal
 * by Tom Gowan
 */

extern crate asio_sys as sys;

// This is the same data that enumerate
// is trying to find
// Basically these are stubbed versions
//
// Format that each sample has.
#[derive(Clone, Copy, Debug, PartialEq, Eq)]
pub enum SampleFormat {
    // The value 0 corresponds to 0.
    I16,
    // The value 0 corresponds to 32768.
    U16,
    // The boundaries are (-1.0, 1.0).
    F32,
}
// Number of channels.
pub type ChannelCount = u16;

// The number of samples processed per second for a single channel of audio.
pub type SampleRate = u32;

#[derive(Debug, Clone, PartialEq, Eq)]
pub struct Format {
    pub channels: ChannelCount,
    pub sample_rate: SampleRate,
    pub data_type: SampleFormat,
}

fn main() {
    let asio = sys::Asio::new();
    for name in asio.driver_names() {
        println!("Driver: {:?}", name);
        let driver = asio.load_driver(&name).expect("failed to load driver");
        let channels = driver
            .channels()
            .expect("failed to retrieve channel counts");
        let sample_rate = driver
            .sample_rate()
            .expect("failed to retrieve sample rate");
        let in_fmt = Format {
            channels: channels.ins as _,
            sample_rate: sample_rate as _,
            data_type: SampleFormat::F32,
        };
        let out_fmt = Format {
            channels: channels.outs as _,
            sample_rate: sample_rate as _,
            data_type: SampleFormat::F32,
        };
        println!("  Input {:?}", in_fmt);
        println!("  Output {:?}", out_fmt);
    }
}
```

## File: `asio-sys/examples/test.rs`
```rust
extern crate asio_sys as sys;

fn main() {
    let asio = sys::Asio::new();
    for driver in asio.driver_names() {
        println!("Driver: {}", driver);
        let driver = asio.load_driver(&driver).expect("failed to load drivers");
        println!(
            "  Channels: {:?}",
            driver.channels().expect("failed to get channels")
        );
        println!(
            "  Sample rate: {:?}",
            driver.sample_rate().expect("failed to get sample rate")
        );
    }
}
```

## File: `asio-sys/src/lib.rs`
```rust
#![allow(non_camel_case_types)]

#[macro_use]
extern crate num_derive;
extern crate num_traits;

pub mod bindings;
pub use bindings::errors::{AsioError, LoadDriverError};
pub use bindings::*;
```

## File: `asio-sys/src/bindings/asio_import.rs`
```rust
#![allow(non_upper_case_globals)]
#![allow(non_camel_case_types)]
#![allow(non_snake_case)]
#![allow(dead_code)]
#![allow(clippy::missing_safety_doc)]

include!(concat!(env!("OUT_DIR"), "/asio_bindings.rs"));
```

## File: `asio-sys/src/bindings/errors.rs`
```rust
use std::error::Error;
use std::fmt;

/// Errors that might occur during `Asio::load_driver`.
#[derive(Clone, Debug)]
pub enum LoadDriverError {
    LoadDriverFailed,
    DriverAlreadyExists,
    InitializationFailed(AsioError),
}

/// General errors returned by ASIO.
#[derive(Clone, Debug)]
pub enum AsioError {
    NoDrivers,
    HardwareMalfunction,
    InvalidInput,
    BadMode,
    HardwareStuck,
    NoRate,
    NoMemory,
    InvalidBufferSize,
    UnknownError,
}

#[derive(Debug)]
pub enum AsioErrorWrapper {
    ASE_OK = 0,               // This value will be returned whenever the call succeeded
    ASE_SUCCESS = 0x3f4847a0, // unique success return value for ASIOFuture calls
    ASE_NotPresent = -1000,   // hardware input or output is not present or available
    ASE_HWMalfunction,        // hardware is malfunctioning (can be returned by any ASIO function)
    ASE_InvalidParameter,     // input parameter invalid
    ASE_InvalidMode,          // hardware is in a bad mode or used in a bad mode
    ASE_SPNotAdvancing,       // hardware is not running when sample position is inquired
    ASE_NoClock,              // sample clock or rate cannot be determined or is not present
    ASE_NoMemory,             // not enough memory for completing the request
    Invalid,
}

impl fmt::Display for LoadDriverError {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        match *self {
            LoadDriverError::LoadDriverFailed => {
                write!(
                    f,
                    "ASIO `loadDriver` function returned `false` indicating failure"
                )
            }
            LoadDriverError::InitializationFailed(ref err) => {
                write!(f, "{err}")
            }
            LoadDriverError::DriverAlreadyExists => {
                write!(f, "ASIO only supports loading one driver at a time")
            }
        }
    }
}

impl fmt::Display for AsioError {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        match *self {
            AsioError::NoDrivers => {
                write!(f, "hardware input or output is not present or available")
            }
            AsioError::HardwareMalfunction => write!(
                f,
                "hardware is malfunctioning (can be returned by any ASIO function)"
            ),
            AsioError::InvalidInput => write!(f, "input parameter invalid"),
            AsioError::BadMode => write!(f, "hardware is in a bad mode or used in a bad mode"),
            AsioError::HardwareStuck => write!(
                f,
                "hardware is not running when sample position is inquired"
            ),
            AsioError::NoRate => write!(
                f,
                "sample clock or rate cannot be determined or is not present"
            ),
            AsioError::NoMemory => write!(f, "not enough memory for completing the request"),
            AsioError::InvalidBufferSize => write!(f, "buffersize out of range for device"),
            AsioError::UnknownError => write!(f, "Error not in SDK"),
        }
    }
}

impl Error for LoadDriverError {}
impl Error for AsioError {}

impl From<AsioError> for LoadDriverError {
    fn from(err: AsioError) -> Self {
        LoadDriverError::InitializationFailed(err)
    }
}

macro_rules! asio_result {
    ($e:expr) => {{
        let res = { $e };
        match res {
            r if r == AsioErrorWrapper::ASE_OK as i32 => Ok(()),
            r if r == AsioErrorWrapper::ASE_SUCCESS as i32 => Ok(()),
            r if r == AsioErrorWrapper::ASE_NotPresent as i32 => Err(AsioError::NoDrivers),
            r if r == AsioErrorWrapper::ASE_HWMalfunction as i32 => {
                Err(AsioError::HardwareMalfunction)
            }
            r if r == AsioErrorWrapper::ASE_InvalidParameter as i32 => Err(AsioError::InvalidInput),
            r if r == AsioErrorWrapper::ASE_InvalidMode as i32 => Err(AsioError::BadMode),
            r if r == AsioErrorWrapper::ASE_SPNotAdvancing as i32 => Err(AsioError::HardwareStuck),
            r if r == AsioErrorWrapper::ASE_NoClock as i32 => Err(AsioError::NoRate),
            r if r == AsioErrorWrapper::ASE_NoMemory as i32 => Err(AsioError::NoMemory),
            _ => Err(AsioError::UnknownError),
        }
    }};
}
```

## File: `asio-sys/src/bindings/mod.rs`
```rust
pub(crate) mod asio_import;
#[macro_use]
pub mod errors;

use self::errors::{AsioError, AsioErrorWrapper, LoadDriverError};
use num_traits::FromPrimitive;

use std::ffi::{CStr, CString};
use std::os::raw::{c_char, c_double, c_void};
use std::ptr::null_mut;
use std::sync::{
    atomic::{AtomicBool, AtomicU32, AtomicU64, Ordering},
    Arc, Mutex, MutexGuard, Weak,
};
use std::time::Duration;

// On Windows (where ASIO actually runs), c_long is i32.
// On non-Windows platforms (for docs.rs and local testing), redefine c_long as i32 to match.
#[cfg(target_os = "windows")]
use std::os::raw::c_long;
#[cfg(not(target_os = "windows"))]
type c_long = i32;

// Bindings import
use self::asio_import as ai;

/// A handle to the ASIO API.
///
/// There should only be one instance of this type at any point in time.
#[derive(Debug, Default)]
pub struct Asio {
    // Keeps track of whether or not a driver is already loaded.
    //
    // This is necessary as ASIO only supports one `Driver` at a time.
    loaded_driver: Mutex<Weak<DriverInner>>,
}

/// A handle to a single ASIO driver.
///
/// Creating an instance of this type loads and initialises the driver.
///
/// Dropping all `Driver` instances will automatically dispose of any resources and de-initialise
/// the driver.
#[derive(Clone, Debug)]
pub struct Driver {
    inner: Arc<DriverInner>,
}

// Contains the state associated with a `Driver`.
//
// This state may be shared between multiple `Driver` handles representing the same underlying
// driver. Only when the last `Driver` is dropped will the `Drop` implementation for this type run
// and the necessary driver resources will be de-allocated and unloaded.
//
// The same could be achieved by returning an `Arc<Driver>` from the `Host::load_driver` API,
// however the `DriverInner` abstraction is required in order to allow for the `Driver::destroy`
// method to exist safely. By wrapping the `Arc<DriverInner>` in the `Driver` type, we can make
// sure the user doesn't `try_unwrap` the `Arc` and invalidate the `Asio` instance's weak pointer.
// This would allow for instantiation of a separate driver before the existing one is destroyed,
// which is disallowed by ASIO.
#[derive(Debug)]
struct DriverInner {
    state: Mutex<DriverState>,
    // The unique name associated with this driver.
    name: String,
    // Track whether or not the driver has been destroyed.
    //
    // This allows for the user to manually destroy the driver and handle any errors if they wish.
    //
    // In the case that the driver has been manually destroyed this flag will be set to `true`
    // indicating to the `drop` implementation that there is nothing to be done.
    destroyed: bool,
}

/// All possible states of an ASIO `Driver` instance.
///
/// Mapped to the finite state machine in the ASIO SDK docs.
#[derive(Clone, Copy, Debug, Eq, Hash, PartialEq)]
pub(crate) enum DriverState {
    Initialized,
    Prepared,
    Running,
}

/// Amount of input and output channels available.
#[derive(Clone, Copy, Debug, Eq, Hash, PartialEq)]
pub struct Channels {
    pub ins: i32,
    pub outs: i32,
}

/// Hardware latency in frames for the input and output streams.
#[derive(Clone, Copy, Debug, Eq, Hash, PartialEq)]
pub struct Latencies {
    pub input: i32,
    pub output: i32,
}

/// Minimum and maximum supported buffer sizes in frames.
#[derive(Clone, Copy, Debug, Eq, Hash, PartialEq)]
pub struct BufferSizeRange {
    pub min: i32,
    pub max: i32,
}

/// Information provided to the BufferCallback.
#[derive(Debug)]
pub struct CallbackInfo {
    pub buffer_index: i32,
    /// System time at the start of this buffer period, in nanoseconds.
    pub system_time: u64,
    pub callback_flag: u32,
}

/// Holds the pointer to the callbacks that come from cpal
struct BufferCallback(Box<dyn FnMut(&CallbackInfo) + Send>);

/// Input and Output streams.
///
/// There is only ever max one input and one output.
///
/// Only one is required.
pub struct AsioStreams {
    pub input: Option<AsioStream>,
    pub output: Option<AsioStream>,
}

/// A stream to ASIO.
///
/// Contains the buffers.
pub struct AsioStream {
    /// A Double buffer per channel
    pub buffer_infos: Vec<AsioBufferInfo>,
    /// Size of each buffer
    pub buffer_size: i32,
}

/// All the possible types from ASIO.
/// This is a direct copy of the ASIOSampleType
/// inside ASIO SDK.
#[derive(Debug, FromPrimitive)]
#[repr(C)]
pub enum AsioSampleType {
    ASIOSTInt16MSB = 0,
    ASIOSTInt24MSB = 1, // used for 20 bits as well
    ASIOSTInt32MSB = 2,
    ASIOSTFloat32MSB = 3, // IEEE 754 32 bit float
    ASIOSTFloat64MSB = 4, // IEEE 754 64 bit double float

    // these are used for 32 bit data buffer, with different alignment of the data inside
    // 32 bit PCI bus systems can be more easily used with these
    ASIOSTInt32MSB16 = 8,  // 32 bit data with 16 bit alignment
    ASIOSTInt32MSB18 = 9,  // 32 bit data with 18 bit alignment
    ASIOSTInt32MSB20 = 10, // 32 bit data with 20 bit alignment
    ASIOSTInt32MSB24 = 11, // 32 bit data with 24 bit alignment

    ASIOSTInt16LSB = 16,
    ASIOSTInt24LSB = 17, // used for 20 bits as well
    ASIOSTInt32LSB = 18,
    ASIOSTFloat32LSB = 19, // IEEE 754 32 bit float, as found on Intel x86 architecture
    ASIOSTFloat64LSB = 20, // IEEE 754 64 bit double float, as found on Intel x86 architecture

    // these are used for 32 bit data buffer, with different alignment of the data inside
    // 32 bit PCI bus systems can more easily used with these
    ASIOSTInt32LSB16 = 24, // 32 bit data with 18 bit alignment
    ASIOSTInt32LSB18 = 25, // 32 bit data with 18 bit alignment
    ASIOSTInt32LSB20 = 26, // 32 bit data with 20 bit alignment
    ASIOSTInt32LSB24 = 27, // 32 bit data with 24 bit alignment

    //	ASIO DSD format.
    ASIOSTDSDInt8LSB1 = 32, // DSD 1 bit data, 8 samples per byte. First sample in Least significant bit.
    ASIOSTDSDInt8MSB1 = 33, // DSD 1 bit data, 8 samples per byte. First sample in Most significant bit.
    ASIOSTDSDInt8NER8 = 40, // DSD 8 bit data, 1 sample per byte. No Endianness required.

    ASIOSTLastEntry,
}

/// Gives information about buffers
/// Receives pointers to buffers
#[derive(Debug, Copy, Clone)]
#[repr(C, packed(4))]
pub struct AsioBufferInfo {
    /// 0 for output 1 for input
    pub is_input: i32,
    /// Which channel. Starts at 0
    pub channel_num: i32,
    /// Pointer to each half of the double buffer.
    pub buffers: [*mut c_void; 2],
}

/// Callbacks that ASIO calls
#[repr(C, packed(4))]
struct AsioCallbacks {
    buffer_switch: extern "C" fn(double_buffer_index: c_long, direct_process: c_long) -> (),
    sample_rate_did_change: extern "C" fn(s_rate: c_double) -> (),
    asio_message: extern "C" fn(
        selector: c_long,
        value: c_long,
        message: *mut (),
        opt: *mut c_double,
    ) -> c_long,
    buffer_switch_time_info: extern "C" fn(
        params: *mut ai::ASIOTime,
        double_buffer_index: c_long,
        direct_process: c_long,
    ) -> *mut ai::ASIOTime,
}

static ASIO_CALLBACKS: AsioCallbacks = AsioCallbacks {
    buffer_switch,
    sample_rate_did_change,
    asio_message,
    buffer_switch_time_info,
};

/// All the possible types from ASIO.
/// This is a direct copy of the asioMessage selectors
/// inside ASIO SDK.
#[rustfmt::skip]
#[derive(Clone, Copy, Debug, FromPrimitive)]
#[repr(C)]
pub enum AsioMessageSelectors {
    kAsioSelectorSupported = 1, // selector in <value>, returns 1L if supported,
                                // 0 otherwise
    kAsioEngineVersion,         // returns engine (host) asio implementation version,
                                // 2 or higher
    kAsioResetRequest,          // request driver reset. if accepted, this
                                // will close the driver (ASIO_Exit() ) and
                                // re-open it again (ASIO_Init() etc). some
                                // drivers need to reconfigure for instance
                                // when the sample rate changes, or some basic
                                // changes have been made in ASIO_ControlPanel().
                                // returns 1L; note the request is merely passed
                                // to the application, there is no way to determine
                                // if it gets accepted at this time (but it usually
                                // will be).
    kAsioBufferSizeChange,      // not yet supported, will currently always return 0L.
                                // for now, use kAsioResetRequest instead.
                                // once implemented, the new buffer size is expected
                                // in <value>, and on success returns 1L
    kAsioResyncRequest,         // the driver went out of sync, such that
                                // the timestamp is no longer valid. this
                                // is a request to re-start the engine and
                                // slave devices (sequencer). returns 1 for ok,
                                // 0 if not supported.
    kAsioLatenciesChanged,      // the drivers latencies have changed. The engine
                                // will refetch the latencies.
    kAsioSupportsTimeInfo,      // if host returns true here, it will expect the
                                // callback bufferSwitchTimeInfo to be called instead
                                // of bufferSwitch
    kAsioSupportsTimeCode,      //
    kAsioMMCCommand,            // unused - value: number of commands, message points to mmc commands
    kAsioSupportsInputMonitor,  // kAsioSupportsXXX return 1 if host supports this
    kAsioSupportsInputGain,     // unused and undefined
    kAsioSupportsInputMeter,    // unused and undefined
    kAsioSupportsOutputGain,    // unused and undefined
    kAsioSupportsOutputMeter,   // unused and undefined
    kAsioOverload,              // driver detected an overload
    kAsioNumMessageSelectors,   // sentinel value equal to the number of defined selectors
}

/// Events dispatched to registered driver event callbacks.
#[derive(Clone, Copy, Debug)]
pub enum AsioDriverEvent {
    /// A message from the ASIO driver's `asioMessage` callback.
    ///
    /// `selector` identifies the message type; `value` is the raw payload passed by the driver.
    /// For [`AsioMessageSelectors::kAsioSelectorSupported`] queries, `value` is the selector being
    /// queried. Return `true` to advertise support for it, `false` to decline. For other selectors,
    /// the return value is ignored.
    Message {
        selector: AsioMessageSelectors,
        value: i32,
    },

    /// The ASIO driver reported a sample rate change.
    ///
    /// Only dispatched when the reported rate differs from the last known rate, so spurious
    /// `sampleRateDidChange` calls (e.g. on AES/EBU sync status changes where the rate has not
    /// actually changed) are suppressed.
    SampleRateChanged(f64),
}

/// A rust-usable version of the `ASIOTime` type that does not contain a binary blob for fields.
#[repr(C, packed(4))]
pub struct AsioTime {
    /// Must be `0`.
    reserved: [i32; 4],
    /// Required.
    pub time_info: AsioTimeInfo,
    /// Optional, evaluated if (time_code.flags & ktcValid).
    pub time_code: AsioTimeCode,
}

/// A rust-compatible version of the `ASIOTimeInfo` type that does not contain a binary blob for
/// fields.
#[repr(C, packed(4))]
pub struct AsioTimeInfo {
    /// Absolute speed (1. = nominal).
    pub speed: c_double,
    /// System time related to sample_position, in nanoseconds.
    ///
    /// On Windows, must be derived from timeGetTime().
    pub system_time: ai::ASIOTimeStamp,
    /// Sample position since `ASIOStart()`.
    pub sample_position: ai::ASIOSamples,
    /// Current rate, unsigned.
    pub sample_rate: AsioSampleRate,
    /// See `AsioTimeInfoFlags`.
    pub flags: i32,
    /// Must be `0`.
    reserved: [c_char; 12],
}

/// A rust-compatible version of the `ASIOTimeCode` type that does not use a binary blob for its
/// fields.
#[repr(C, packed(4))]
pub struct AsioTimeCode {
    /// Speed relation (fraction of nominal speed) optional.
    ///
    /// Set to 0. or 1. if not supported.
    pub speed: c_double,
    /// Time in samples unsigned.
    pub time_code_samples: ai::ASIOSamples,
    /// See `ASIOTimeCodeFlags`.
    pub flags: i32,
    /// Set to `0`.
    future: [c_char; 64],
}

/// A rust-compatible version of the `ASIOSampleRate` type that does not use a binary blob for its
/// fields.
pub type AsioSampleRate = f64;

// A helper type to simplify retrieval of available buffer sizes.
#[derive(Default)]
struct BufferSizes {
    min: c_long,
    max: c_long,
    pref: c_long,
    grans: c_long,
}

/// Identifies a buffer callback registered via [`Driver::add_callback`].
#[derive(Clone, Copy, Debug, PartialEq, Eq)]
pub struct BufferCallbackId(usize);

/// A global way to access all the callbacks.
///
/// This is required because of how ASIO calls the `buffer_switch` function with no data
/// parameters.
static BUFFER_CALLBACK: Mutex<Vec<(BufferCallbackId, BufferCallback)>> = Mutex::new(Vec::new());

/// Used to identify when to clear buffers.
static CALLBACK_FLAG: AtomicU32 = AtomicU32::new(0);

/// Indicates that ASIOOutputReady should be called
static CALL_OUTPUT_READY: AtomicBool = AtomicBool::new(false);
static CURRENT_SAMPLE_RATE: AtomicU64 = AtomicU64::new(0);

/// Identifies a driver event callback registered via [`Driver::add_event_callback`].
#[derive(Clone, Copy, Debug, PartialEq, Eq)]
pub struct DriverEventCallbackId(usize);

struct DriverEventCallback(Arc<dyn Fn(AsioDriverEvent) -> bool + Send + Sync>);

/// A global registry for ASIO driver event callbacks.
static DRIVER_EVENT_CALLBACKS: Mutex<Vec<(DriverEventCallbackId, DriverEventCallback)>> =
    Mutex::new(Vec::new());

impl Asio {
    /// Initialise the ASIO API.
    pub fn new() -> Self {
        Self::default()
    }

    /// Returns the name for each available driver.
    ///
    /// This is used at the start to allow the user to choose which driver they want.
    pub fn driver_names(&self) -> Vec<String> {
        // The most drivers we can take
        const MAX_DRIVERS: usize = 100;
        // Max length for divers name
        const MAX_DRIVER_NAME_LEN: usize = 32;

        // 2D array of driver names set to 0.
        let mut driver_names: [[c_char; MAX_DRIVER_NAME_LEN]; MAX_DRIVERS] =
            [[0; MAX_DRIVER_NAME_LEN]; MAX_DRIVERS];
        // Pointer to each driver name.
        let mut driver_name_ptrs: [*mut i8; MAX_DRIVERS] = [null_mut(); MAX_DRIVERS];
        for (ptr, name) in driver_name_ptrs.iter_mut().zip(&mut driver_names[..]) {
            *ptr = (*name).as_mut_ptr();
        }

        unsafe {
            let num_drivers =
                ai::get_driver_names(driver_name_ptrs.as_mut_ptr(), MAX_DRIVERS as i32);
            (0..num_drivers)
                .map(|i| driver_name_to_utf8(&driver_names[i as usize]).to_string())
                .collect()
        }
    }

    /// If a driver has already been loaded, this will return that driver.
    ///
    /// Returns `None` if no driver is currently loaded.
    ///
    /// This can be useful to check before calling `load_driver` as ASIO only supports loading a
    /// single driver at a time.
    pub fn loaded_driver(&self) -> Option<Driver> {
        self.loaded_driver
            .lock()
            .expect("failed to acquire loaded driver lock")
            .upgrade()
            .map(|inner| Driver { inner })
    }

    /// Load a driver from the given name.
    ///
    /// Driver names compatible with this method can be produced via the `asio.driver_names()`
    /// method.
    ///
    /// NOTE: Despite many requests from users, ASIO only supports loading a single driver at a
    /// time. Calling this method while a previously loaded `Driver` instance exists will result in
    /// an error. That said, if this method is called with the name of a driver that has already
    /// been loaded, that driver will be returned successfully.
    pub fn load_driver(&self, driver_name: &str) -> Result<Driver, LoadDriverError> {
        // Hold the lock for the entire operation to prevent a TOCTOU race where two threads
        // both pass the "no driver loaded" check and then both call load_asio_driver.
        let mut loaded = self
            .loaded_driver
            .lock()
            .expect("failed to acquire loaded driver lock");

        // Check whether or not a driver is already loaded.
        if let Some(inner) = loaded.upgrade() {
            let driver = Driver { inner };
            if driver.name() == driver_name {
                return Ok(driver);
            } else {
                return Err(LoadDriverError::DriverAlreadyExists);
            }
        }

        // Make owned CString to send to load driver
        let driver_name_cstring =
            CString::new(driver_name).map_err(|_| LoadDriverError::LoadDriverFailed)?;
        let mut driver_info = std::mem::MaybeUninit::<ai::ASIODriverInfo>::uninit();

        unsafe {
            match ai::load_asio_driver(driver_name_cstring.as_ptr() as *mut i8) {
                false => Err(LoadDriverError::LoadDriverFailed),
                true => {
                    // Initialize ASIO.
                    asio_result!(ai::ASIOInit(driver_info.as_mut_ptr()))?;
                    let _driver_info = driver_info.assume_init();
                    let mut rate: c_double = 0.0;
                    let _ = asio_result!(ai::get_sample_rate(&mut rate));
                    if rate > 0.0 {
                        CURRENT_SAMPLE_RATE.store(rate.to_bits(), Ordering::Release);
                    }
                    let state = Mutex::new(DriverState::Initialized);
                    let name = driver_name.to_string();
                    let destroyed = false;
                    let inner = Arc::new(DriverInner {
                        name,
                        state,
                        destroyed,
                    });
                    *loaded = Arc::downgrade(&inner);
                    let driver = Driver { inner };
                    Ok(driver)
                }
            }
        }
    }
}

impl BufferCallback {
    /// Calls the inner callback.
    fn run(&mut self, callback_info: &CallbackInfo) {
        let cb = &mut self.0;
        cb(callback_info);
    }
}

impl Driver {
    /// The name used to uniquely identify this driver.
    pub fn name(&self) -> &str {
        &self.inner.name
    }

    /// Returns the number of input and output channels available on the driver.
    pub fn channels(&self) -> Result<Channels, AsioError> {
        let _guard = self.inner.lock_state();
        let mut ins: c_long = 0;
        let mut outs: c_long = 0;
        unsafe {
            asio_result!(ai::ASIOGetChannels(&mut ins, &mut outs))?;
        }
        Ok(Channels { ins, outs })
    }

    /// Get the input and output hardware latency in frames.
    pub fn latencies(&self) -> Result<Latencies, AsioError> {
        let _guard = self.inner.lock_state();
        let mut input_latency: c_long = 0;
        let mut output_latency: c_long = 0;
        unsafe {
            asio_result!(ai::ASIOGetLatencies(
                &mut input_latency,
                &mut output_latency
            ))?;
        }
        Ok(Latencies {
            input: input_latency,
            output: output_latency,
        })
    }

    /// Get the min and max supported buffersize of the driver.
    pub fn buffersize_range(&self) -> Result<BufferSizeRange, AsioError> {
        let _guard = self.inner.lock_state();
        let buffer_sizes = asio_get_buffer_sizes()?;
        Ok(BufferSizeRange {
            min: buffer_sizes.min,
            max: buffer_sizes.max,
        })
    }

    /// Get current sample rate of the driver.
    pub fn sample_rate(&self) -> Result<f64, AsioError> {
        let _guard = self.inner.lock_state();
        let mut rate: c_double = 0.0;
        unsafe {
            asio_result!(ai::get_sample_rate(&mut rate))?;
        }
        Ok(rate)
    }

    /// Can the driver accept the given sample rate.
    pub fn can_sample_rate(&self, sample_rate: f64) -> Result<bool, AsioError> {
        let _guard = self.inner.lock_state();
        unsafe {
            match asio_result!(ai::can_sample_rate(sample_rate)) {
                Ok(()) => Ok(true),
                Err(AsioError::NoRate) => Ok(false),
                Err(err) => Err(err),
            }
        }
    }

    /// Set the sample rate for the driver.
    pub fn set_sample_rate(&self, sample_rate: f64) -> Result<(), AsioError> {
        let actual = {
            let _guard = self.inner.lock_state();
            unsafe { asio_result!(ai::set_sample_rate(sample_rate))? };
            let mut actual: c_double = 0.0;
            unsafe { asio_result!(ai::get_sample_rate(&mut actual))? };
            actual
        };

        // Check whether the driver applied the rate immediately.
        if (actual - sample_rate).abs() < 1.0 {
            CURRENT_SAMPLE_RATE.store(actual.to_bits(), Ordering::Release);
            return Ok(());
        }

        // Some ASIO drivers (e.g. Steinberg) do not apply a rate change until after a
        // complete buffer-creation cycle (CreateBuffers -> Start -> Stop -> DisposeBuffers),
        // followed by a full driver teardown and reload.
        let mut dummy_infos = prepare_buffer_infos(false, 1);
        let buffer_size = self.create_buffers(&mut dummy_infos, None)?;

        // Start briefly so the driver reconfigures its hardware clock.
        self.start()?;

        // Wait for one full buffer to be processed: this guarantees the driver has
        // applied the rate change to the hardware clock before we stop it.
        let buffer_duration = Duration::from_secs_f64(buffer_size as f64 / sample_rate);
        std::thread::sleep(buffer_duration);

        self.stop()?;
        self.dispose_buffers()?;

        // Full teardown so the driver is reset to a clean state. Some drivers
        // (e.g. Steinberg) return errors from ASIOGetChannels after DisposeBuffers
        // unless the driver is fully exited and reloaded.
        {
            let mut state = self.inner.lock_state();
            unsafe {
                let _ = asio_result!(ai::ASIOExit());
                ai::remove_current_driver();
            }
            std::thread::sleep(buffer_duration);

            // Safety: the name was validated as null-free when the driver was first loaded.
            let name_cstring = CString::new(self.inner.name.as_str())
                .expect("driver name already stored must not contain null bytes");
            unsafe {
                if !ai::load_asio_driver(name_cstring.as_ptr() as *mut i8) {
                    return Err(AsioError::NoDrivers);
                }
                let mut driver_info = std::mem::MaybeUninit::<ai::ASIODriverInfo>::uninit();
                asio_result!(ai::ASIOInit(driver_info.as_mut_ptr()))?;
            }
            *state = DriverState::Initialized;

            // Set the rate again on the freshly initialized driver.
            unsafe { asio_result!(ai::set_sample_rate(sample_rate))? };

            let mut actual: c_double = 0.0;
            unsafe { asio_result!(ai::get_sample_rate(&mut actual))? };
            if (actual - sample_rate).abs() >= 1.0 {
                return Err(AsioError::NoRate);
            }

            CURRENT_SAMPLE_RATE.store(actual.to_bits(), Ordering::Release);
        }
        Ok(())
    }

    /// Get the current data type of the driver's input stream.
    ///
    /// This queries a single channel's type assuming all channels have the same sample type.
    pub fn input_data_type(&self) -> Result<AsioSampleType, AsioError> {
        let _guard = self.inner.lock_state();
        stream_data_type(true)
    }

    /// Get the current data type of the driver's output stream.
    ///
    /// This queries a single channel's type assuming all channels have the same sample type.
    pub fn output_data_type(&self) -> Result<AsioSampleType, AsioError> {
        let _guard = self.inner.lock_state();
        stream_data_type(false)
    }

    /// Ask ASIO to allocate the buffers and give the callback pointers.
    ///
    /// This will destroy any already allocated buffers.
    ///
    /// If buffersize is None then the preferred buffer size from ASIO is used,
    /// otherwise the desired buffersize is used if the requested size is within
    /// the range of accepted buffersizes for the device.
    fn create_buffers(
        &self,
        buffer_infos: &mut [AsioBufferInfo],
        buffer_size: Option<i32>,
    ) -> Result<c_long, AsioError> {
        let num_channels = buffer_infos.len();

        let mut state = self.inner.lock_state();

        // Retrieve the available buffer sizes.
        let buffer_sizes = asio_get_buffer_sizes()?;
        if buffer_sizes.pref <= 0 {
            panic!(
                "`ASIOGetBufferSize` produced unusable preferred buffer size of {}",
                buffer_sizes.pref,
            );
        }

        let buffer_size = match buffer_size {
            Some(v) => {
                if v <= buffer_sizes.max {
                    v
                } else {
                    return Err(AsioError::InvalidBufferSize);
                }
            }
            None => buffer_sizes.pref,
        };

        CALL_OUTPUT_READY.store(
            asio_result!(unsafe { ai::ASIOOutputReady() }).is_ok(),
            Ordering::Release,
        );

        // Ensure the driver is in the `Initialized` state.
        if let DriverState::Running = *state {
            state.stop()?;
        }
        if let DriverState::Prepared = *state {
            state.dispose_buffers()?;
        }
        unsafe {
            asio_result!(ai::ASIOCreateBuffers(
                buffer_infos.as_mut_ptr() as *mut _,
                num_channels as i32,
                buffer_size,
                &ASIO_CALLBACKS as *const _ as *mut _,
            ))?;
        }
        *state = DriverState::Prepared;

        Ok(buffer_size)
    }

    /// Creates the streams.
    ///
    /// `buffer_size` sets the desired buffer_size. If None is passed in, then the
    /// default buffersize for the device is used.
    ///
    /// Both input and output streams need to be created together as a single slice of
    /// `ASIOBufferInfo`.
    fn create_streams(
        &self,
        mut input_buffer_infos: Vec<AsioBufferInfo>,
        mut output_buffer_infos: Vec<AsioBufferInfo>,
        buffer_size: Option<i32>,
    ) -> Result<AsioStreams, AsioError> {
        let (input, output) = match (
            input_buffer_infos.is_empty(),
            output_buffer_infos.is_empty(),
        ) {
            // Both stream exist.
            (false, false) => {
                // Create one continuous slice of buffers.
                let split_point = input_buffer_infos.len();
                let mut all_buffer_infos = input_buffer_infos;
                all_buffer_infos.append(&mut output_buffer_infos);
                // Create the buffers. On success, split the output and input again.
                let buffer_size = self.create_buffers(&mut all_buffer_infos, buffer_size)?;
                let output_buffer_infos = all_buffer_infos.split_off(split_point);
                let input_buffer_infos = all_buffer_infos;
                let input = Some(AsioStream {
                    buffer_infos: input_buffer_infos,
                    buffer_size,
                });
                let output = Some(AsioStream {
                    buffer_infos: output_buffer_infos,
                    buffer_size,
                });
                (input, output)
            }
            // Just input
            (false, true) => {
                let buffer_size = self.create_buffers(&mut input_buffer_infos, buffer_size)?;
                let input = Some(AsioStream {
                    buffer_infos: input_buffer_infos,
                    buffer_size,
                });
                let output = None;
                (input, output)
            }
            // Just output
            (true, false) => {
                let buffer_size = self.create_buffers(&mut output_buffer_infos, buffer_size)?;
                let input = None;
                let output = Some(AsioStream {
                    buffer_infos: output_buffer_infos,
                    buffer_size,
                });
                (input, output)
            }
            // Impossible
            (true, true) => unreachable!("Trying to create streams without preparing"),
        };
        Ok(AsioStreams { input, output })
    }

    /// Prepare the input stream.
    ///
    /// Because only the latest call to ASIOCreateBuffers is relevant this call will destroy all
    /// past active buffers and recreate them.
    ///
    /// For this reason we take the output stream if it exists.
    ///
    /// `num_channels` is the desired number of input channels.
    ///
    /// `buffer_size` sets the desired buffer_size. If None is passed in, then the
    /// default buffersize for the device is used.
    ///
    /// This returns a full AsioStreams with both input and output if output was active.
    pub fn prepare_input_stream(
        &self,
        output: Option<AsioStream>,
        num_channels: usize,
        buffer_size: Option<i32>,
    ) -> Result<AsioStreams, AsioError> {
        let input_buffer_infos = prepare_buffer_infos(true, num_channels);
        let output_buffer_infos = output.map(|output| output.buffer_infos).unwrap_or_default();
        self.create_streams(input_buffer_infos, output_buffer_infos, buffer_size)
    }

    /// Prepare the output stream.
    ///
    /// Because only the latest call to ASIOCreateBuffers is relevant this call will destroy all
    /// past active buffers and recreate them.
    ///
    /// For this reason we take the input stream if it exists.
    ///
    /// `num_channels` is the desired number of output channels.
    ///
    /// `buffer_size` sets the desired buffer_size. If None is passed in, then the
    /// default buffersize for the device is used.
    ///
    /// This returns a full AsioStreams with both input and output if input was active.
    pub fn prepare_output_stream(
        &self,
        input: Option<AsioStream>,
        num_channels: usize,
        buffer_size: Option<i32>,
    ) -> Result<AsioStreams, AsioError> {
        let input_buffer_infos = input.map(|input| input.buffer_infos).unwrap_or_default();
        let output_buffer_infos = prepare_buffer_infos(false, num_channels);
        self.create_streams(input_buffer_infos, output_buffer_infos, buffer_size)
    }

    /// Releases buffers allocations.
    ///
    /// This will `stop` the stream if the driver is `Running`.
    ///
    /// No-op if no buffers are allocated.
    pub fn dispose_buffers(&self) -> Result<(), AsioError> {
        self.inner.dispose_buffers_inner()
    }

    /// Starts ASIO streams playing.
    ///
    /// The driver must be in the `Prepared` state
    ///
    /// If called successfully, the driver will be in the `Running` state.
    ///
    /// No-op if already `Running`.
    pub fn start(&self) -> Result<(), AsioError> {
        let mut state = self.inner.lock_state();
        if let DriverState::Running = *state {
            return Ok(());
        }
        unsafe {
            asio_result!(ai::ASIOStart())?;
        }
        *state = DriverState::Running;
        Ok(())
    }

    /// Stops ASIO streams playing.
    ///
    /// No-op if the state is not `Running`.
    ///
    /// If the state was `Running` and the stream is stopped successfully, the driver will be in
    /// the `Prepared` state.
    pub fn stop(&self) -> Result<(), AsioError> {
        self.inner.stop_inner()
    }

    /// Adds a callback to the list of active callbacks.
    ///
    /// The given function receives the index of the buffer currently ready for processing.
    ///
    /// Returns an ID uniquely associated with the given callback so that it may be removed later.
    pub fn add_callback<F>(&self, callback: F) -> BufferCallbackId
    where
        F: 'static + FnMut(&CallbackInfo) + Send,
    {
        let mut bc = BUFFER_CALLBACK.lock().unwrap();
        let id = bc
            .last()
            .map(|&(id, _)| BufferCallbackId(id.0.checked_add(1).expect("stream ID overflowed")))
            .unwrap_or(BufferCallbackId(0));
        let cb = BufferCallback(Box::new(callback));
        bc.push((id, cb));
        id
    }

    /// Remove the callback with the given ID.
    pub fn remove_callback(&self, rem_id: BufferCallbackId) {
        let mut bc = BUFFER_CALLBACK.lock().unwrap();
        bc.retain(|&(id, _)| id != rem_id);
    }

    /// Consumes and destroys the `Driver`, stopping the streams if they are running and releasing
    /// any associated resources.
    ///
    /// Returns `Ok(true)` if the driver was successfully destroyed.
    ///
    /// Returns `Ok(false)` if the driver was not destroyed because another handle to the driver
    /// still exists.
    ///
    /// Returns `Err` if some switching driver states failed or if ASIO returned an error on exit.
    pub fn destroy(self) -> Result<bool, AsioError> {
        let Driver { inner } = self;
        match Arc::try_unwrap(inner) {
            Err(_) => Ok(false),
            Ok(mut inner) => {
                inner.destroy_inner()?;
                Ok(true)
            }
        }
    }

    /// Register a callback to receive ASIO driver events.
    ///
    /// The callback receives an [`AsioDriverEvent`] and returns a `bool`. The return value is
    /// meaningful only for [`AsioDriverEvent::Message`] with selector
    /// [`AsioMessageSelectors::kAsioSelectorSupported`]: return `true` to advertise support for
    /// the queried selector, `false` to decline. For all other events the return value is ignored.
    ///
    /// Returns an ID uniquely associated with the given callback so that it may be removed later.
    pub fn add_event_callback<F>(&self, callback: F) -> DriverEventCallbackId
    where
        F: Fn(AsioDriverEvent) -> bool + Send + Sync + 'static,
    {
        let mut dcb = DRIVER_EVENT_CALLBACKS.lock().unwrap();
        let id = dcb
            .last()
            .map(|&(id, _)| {
                DriverEventCallbackId(
                    id.0.checked_add(1)
                        .expect("DriverEventCallbackId overflowed"),
                )
            })
            .unwrap_or(DriverEventCallbackId(0));

        let cb = DriverEventCallback(Arc::new(callback));
        dcb.push((id, cb));
        id
    }

    /// Remove the event callback with the given ID.
    pub fn remove_event_callback(&self, rem_id: DriverEventCallbackId) {
        let mut dcb = DRIVER_EVENT_CALLBACKS.lock().unwrap();
        dcb.retain(|&(id, _)| id != rem_id);
    }
}

impl DriverState {
    fn stop(&mut self) -> Result<(), AsioError> {
        if let DriverState::Running = *self {
            unsafe {
                asio_result!(ai::ASIOStop())?;
            }
            *self = DriverState::Prepared;
        }
        Ok(())
    }

    fn dispose_buffers(&mut self) -> Result<(), AsioError> {
        if let DriverState::Initialized = *self {
            return Ok(());
        }
        if let DriverState::Running = *self {
            self.stop()?;
        }
        unsafe {
            asio_result!(ai::ASIODisposeBuffers())?;
        }
        *self = DriverState::Initialized;
        Ok(())
    }

    fn destroy(&mut self) -> Result<(), AsioError> {
        if let DriverState::Running = *self {
            self.stop()?;
        }
        if let DriverState::Prepared = *self {
            self.dispose_buffers()?;
        }
        unsafe {
            asio_result!(ai::ASIOExit())?;
            ai::remove_current_driver();
        }
        Ok(())
    }
}

impl DriverInner {
    fn lock_state(&self) -> MutexGuard<'_, DriverState> {
        self.state.lock().expect("failed to lock `DriverState`")
    }

    fn stop_inner(&self) -> Result<(), AsioError> {
        let mut state = self.lock_state();
        state.stop()
    }

    fn dispose_buffers_inner(&self) -> Result<(), AsioError> {
        let mut state = self.lock_state();
        state.dispose_buffers()
    }

    fn destroy_inner(&mut self) -> Result<(), AsioError> {
        {
            let mut state = self.lock_state();
            state.destroy()?;

            // Clear any existing stream callbacks.
            if let Ok(mut bcs) = BUFFER_CALLBACK.lock() {
                bcs.clear();
            }
        }

        // Signal that the driver has been destroyed.
        self.destroyed = true;

        Ok(())
    }
}

impl Drop for DriverInner {
    fn drop(&mut self) {
        if !self.destroyed {
            // We probably shouldn't `panic!` in the destructor? We also shouldn't ignore errors
            // though either.
            self.destroy_inner().ok();
        }
    }
}

unsafe impl Send for AsioStream {}

/// Used by the input and output stream creation process.
fn prepare_buffer_infos(is_input: bool, n_channels: usize) -> Vec<AsioBufferInfo> {
    let is_input = if is_input { 1 } else { 0 };
    (0..n_channels)
        .map(|ch| AsioBufferInfo {
            is_input,
            channel_num: ch as i32,
            // To be filled by ASIOCreateBuffers.
            buffers: [std::ptr::null_mut(); 2],
        })
        .collect()
}

/// Retrieve the minimum, maximum and preferred buffer sizes along with the available
/// buffer size granularity.
fn asio_get_buffer_sizes() -> Result<BufferSizes, AsioError> {
    let mut b = BufferSizes::default();
    unsafe {
        let res = ai::ASIOGetBufferSize(&mut b.min, &mut b.max, &mut b.pref, &mut b.grans);
        asio_result!(res)?;
    }
    Ok(b)
}

/// Retrieve the `ASIOChannelInfo` associated with the channel at the given index on either the
/// input or output stream (`true` for input).
fn asio_channel_info(channel: c_long, is_input: bool) -> Result<ai::ASIOChannelInfo, AsioError> {
    let mut channel_info = ai::ASIOChannelInfo {
        // Which channel we are querying
        channel,
        // Was it input or output
        isInput: if is_input { 1 } else { 0 },
        // Was it active
        isActive: 0,
        channelGroup: 0,
        // The sample type
        type_: 0,
        name: [0 as c_char; 32],
    };
    unsafe {
        asio_result!(ai::ASIOGetChannelInfo(&mut channel_info))?;
        Ok(channel_info)
    }
}

/// Retrieve the data type of either the input or output stream.
///
/// If `is_input` is true, this will be queried on the input stream.
fn stream_data_type(is_input: bool) -> Result<AsioSampleType, AsioError> {
    let channel_info = asio_channel_info(0, is_input)?;
    Ok(FromPrimitive::from_i32(channel_info.type_).expect("unknown `ASIOSampletype` value"))
}

/// ASIO uses null terminated c strings for driver names.
///
/// This converts to utf8.
fn driver_name_to_utf8(bytes: &[c_char]) -> std::borrow::Cow<'_, str> {
    unsafe { CStr::from_ptr(bytes.as_ptr()).to_string_lossy() }
}

/// Convert an `ASIOTimeStamp` (high and low 32-bit halves) to a `u64` nanosecond value.
#[inline]
fn asio_timestamp_to_nanos(ts: ai::ASIOTimeStamp) -> u64 {
    (ts.hi as u64) << 32 | ts.lo as u64
}

/// Indicates the stream sample rate has changed.
extern "C" fn sample_rate_did_change(s_rate: c_double) {
    let old_bits = CURRENT_SAMPLE_RATE.load(Ordering::Acquire);
    if s_rate.to_bits() != old_bits {
        CURRENT_SAMPLE_RATE.store(s_rate.to_bits(), Ordering::Release);
        dispatch_event(AsioDriverEvent::SampleRateChanged(s_rate));
    }
}

const ASIO_VERSION: c_long = 2;

/// Dispatch `event` to all registered driver event callbacks.
///
/// Returns `true` if any callback returns `true`. All callbacks are always called so that
/// notification side-effects (e.g. stream invalidation) reach every registered listener.
fn dispatch_event(event: AsioDriverEvent) -> bool {
    let callbacks: Vec<_> = {
        let lock = DRIVER_EVENT_CALLBACKS.lock().unwrap();
        lock.iter().map(|(_, cb)| cb.0.clone()).collect()
    };
    callbacks
        .iter()
        .fold(false, |handled, cb| cb(event) || handled)
}

/// Message callback for ASIO to notify of certain events.
extern "C" fn asio_message(
    selector: c_long,
    value: c_long,
    _message: *mut (),
    _opt: *mut c_double,
) -> c_long {
    match AsioMessageSelectors::from_i64(selector as i64) {
        Some(AsioMessageSelectors::kAsioSelectorSupported) => {
            // For selectors that asio-sys itself always handles, advertise support
            // unconditionally. For all others, delegate to registered callbacks so
            // each host can opt-in.
            match AsioMessageSelectors::from_i64(value as i64) {
                Some(AsioMessageSelectors::kAsioSelectorSupported)
                | Some(AsioMessageSelectors::kAsioResetRequest)
                | Some(AsioMessageSelectors::kAsioEngineVersion)
                | Some(AsioMessageSelectors::kAsioResyncRequest)
                | Some(AsioMessageSelectors::kAsioLatenciesChanged)
                | Some(AsioMessageSelectors::kAsioSupportsTimeInfo) => true as c_long,
                _ => dispatch_event(AsioDriverEvent::Message {
                    selector: AsioMessageSelectors::kAsioSelectorSupported,
                    value,
                }) as c_long,
            }
        }

        Some(AsioMessageSelectors::kAsioResetRequest) => {
            // The driver requests a full teardown and reinitialisation. Cannot be performed
            // here as this callback is invoked from within the driver; notify the host to
            // defer the reset to a safe point.
            dispatch_event(AsioDriverEvent::Message {
                selector: AsioMessageSelectors::kAsioResetRequest,
                value,
            });
            true as c_long
        }

        Some(AsioMessageSelectors::kAsioResyncRequest) => {
            // The driver encountered non-fatal data loss (e.g. a timestamp discontinuity).
            // Notify the host so it can handle the gap appropriately.
            dispatch_event(AsioDriverEvent::Message {
                selector: AsioMessageSelectors::kAsioResyncRequest,
                value,
            });
            true as c_long
        }

        Some(AsioMessageSelectors::kAsioLatenciesChanged) => {
            // The driver latencies have changed; have them re-queried.
            dispatch_event(AsioDriverEvent::Message {
                selector: AsioMessageSelectors::kAsioLatenciesChanged,
                value,
            });
            true as c_long
        }

        Some(AsioMessageSelectors::kAsioEngineVersion) => {
            // Return the supported ASIO version of the host application. If a host application
            // does not implement this selector, ASIO 1.0 is assumed by the driver.
            ASIO_VERSION
        }

        Some(AsioMessageSelectors::kAsioSupportsTimeInfo) => {
            // Informs the driver whether the asioCallbacks.bufferSwitchTimeInfo() callback is
            // supported. For compatibility with ASIO 1.0 drivers the host application should
            // always support the "old" bufferSwitch method, too, which we do.
            true as c_long
        }

        // For all other selectors, delegate to registered callbacks.
        Some(other) => dispatch_event(AsioDriverEvent::Message {
            selector: other,
            value,
        }) as c_long,

        None => false as c_long, // Unrecognised selector.
    }
}

/// Similar to buffer switch but with time info.
///
/// If only `buffer_switch` is called by the driver instead, the `buffer_switch` callback will
/// create the necessary timing info and call this function.
///
/// TODO: Provide some access to `ai::ASIOTime` once CPAL gains support for time stamps.
extern "C" fn buffer_switch_time_info(
    time: *mut ai::ASIOTime,
    double_buffer_index: c_long,
    _direct_process: c_long,
) -> *mut ai::ASIOTime {
    // This lock is probably unavoidable, but locks in the audio stream are not great.
    let mut bcs = BUFFER_CALLBACK.lock().unwrap();
    let asio_time: &mut AsioTime = unsafe { &mut *(time as *mut AsioTime) };
    // Alternates: 0, 1, 0, 1, ...
    let callback_flag = CALLBACK_FLAG.fetch_xor(1, Ordering::Relaxed);

    let callback_info = CallbackInfo {
        buffer_index: double_buffer_index,
        system_time: asio_timestamp_to_nanos(asio_time.time_info.system_time),
        callback_flag,
    };
    for &mut (_, ref mut bc) in bcs.iter_mut() {
        bc.run(&callback_info);
    }

    if CALL_OUTPUT_READY.load(Ordering::Acquire) {
        unsafe { ai::ASIOOutputReady() };
    }

    time
}

/// This is called by ASIO.
///
/// Here we run the callback for each stream.
///
/// `double_buffer_index` is either `0` or `1`  indicating which buffer to fill.
extern "C" fn buffer_switch(double_buffer_index: c_long, direct_process: c_long) {
    // Emulate the time info provided by the `buffer_switch_time_info` callback.
    // This is an attempt at matching the behaviour in `hostsample.cpp` from the SDK.
    let mut time = unsafe {
        let mut time: AsioTime = std::mem::zeroed();
        let res = ai::ASIOGetSamplePosition(
            &mut time.time_info.sample_position,
            &mut time.time_info.system_time,
        );
        if let Ok(()) = asio_result!(res) {
            time.time_info.flags = (ai::AsioTimeInfoFlags::kSystemTimeValid
                | ai::AsioTimeInfoFlags::kSamplePositionValid)
                // Context about the cast:
                //
                // Cast was required to successfully compile with MinGW-w64.
                //
                // The flags defined will not create a value that exceeds the maximum value of an i32.
                // The flags are intended to be non-negative, so the sign bit will not be used.
                // The c_uint (flags) is being cast to i32 which is safe as long as the actual value fits within the i32 range, which is true in this case.
                //
                // The actual flags in asio sdk are defined as:
                // typedef enum AsioTimeInfoFlags
                // {
                //	kSystemTimeValid        = 1,            // must always be valid
                //	kSamplePositionValid    = 1 << 1,       // must always be valid
                //	kSampleRateValid        = 1 << 2,
                //	kSpeedValid             = 1 << 3,
                //
                //	kSampleRateChanged      = 1 << 4,
                //	kClockSourceChanged     = 1 << 5
                // } AsioTimeInfoFlags;
                .0 as _;
        }
        time
    };

    // Actual processing happens within the `buffer_switch_time_info` callback.
    let asio_time_ptr = &mut time as *mut AsioTime as *mut ai::ASIOTime;
    buffer_switch_time_info(asio_time_ptr, double_buffer_index, direct_process);
}

#[test]
fn check_type_sizes() {
    assert_eq!(
        std::mem::size_of::<AsioSampleRate>(),
        std::mem::size_of::<ai::ASIOSampleRate>()
    );
    assert_eq!(
        std::mem::size_of::<AsioTimeCode>(),
        std::mem::size_of::<ai::ASIOTimeCode>()
    );
    assert_eq!(
        std::mem::size_of::<AsioTimeInfo>(),
        std::mem::size_of::<ai::AsioTimeInfo>(),
    );
    assert_eq!(
        std::mem::size_of::<AsioTime>(),
        std::mem::size_of::<ai::ASIOTime>()
    );
}
```

## File: `examples/beep.rs`
```rust
//! Plays a simple 440 Hz sine wave (beep) tone.
//!
//! This example demonstrates:
//! - Selecting audio hosts (with optional JACK support on Linux)
//! - Selecting devices by ID or using the default output device
//! - Querying the default output configuration
//! - Building and running an output stream with typed samples
//! - Generating audio data in the stream callback
//!
//! Run with: `cargo run --example beep`
//! With JACK (Linux): `cargo run --example beep --features jack -- --jack`
//! With specific device: `cargo run --example beep -- --device "wasapi:device_id"`

use clap::Parser;
use cpal::{
    traits::{DeviceTrait, HostTrait, StreamTrait},
    FromSample, HostUnavailable, Sample, SizedSample, I24,
};

#[derive(Parser, Debug)]
#[command(version, about = "CPAL beep example", long_about = None)]
struct Opt {
    /// The audio device to use
    #[arg(short, long)]
    device: Option<String>,

    /// Use the JACK host. Requires `--features jack`.
    #[arg(long, default_value_t = false)]
    jack: bool,

    /// Use the PulseAudio host. Requires `--features pulseaudio`.
    #[arg(long, default_value_t = false)]
    pulseaudio: bool,

    /// Use the Pipewire host. Requires `--features pipewire`
    #[arg(long, default_value_t = false)]
    pipewire: bool,
}

fn main() -> anyhow::Result<()> {
    let opt = Opt::parse();

    // Jack/PulseAudio support must be enabled at compile time, and is
    // only available on some platforms.
    #[allow(unused_mut, unused_assignments)]
    let mut jack_host_id = Err(HostUnavailable);
    #[allow(unused_mut, unused_assignments)]
    let mut pulseaudio_host_id = Err(HostUnavailable);
    #[allow(unused_mut, unused_assignments)]
    let mut pipewire_host_id = Err(HostUnavailable);
    #[cfg(any(
        target_os = "linux",
        target_os = "dragonfly",
        target_os = "freebsd",
        target_os = "netbsd"
    ))]
    {
        #[cfg(feature = "jack")]
        {
            jack_host_id = Ok(cpal::HostId::Jack);
        }

        #[cfg(feature = "pulseaudio")]
        {
            pulseaudio_host_id = Ok(cpal::HostId::PulseAudio);
        }
        #[cfg(feature = "pipewire")]
        {
            pipewire_host_id = Ok(cpal::HostId::PipeWire);
        }
    }

    // Manually check for flags. Can be passed through cargo with -- e.g.
    // cargo run --release --example beep --features jack -- --jack
    let host = if opt.jack {
        jack_host_id
            .and_then(cpal::host_from_id)
            .expect("make sure `--features jack` is specified, and the platform is supported")
    } else if opt.pulseaudio {
        pulseaudio_host_id
            .and_then(cpal::host_from_id)
            .expect("make sure `--features pulseaudio` is specified, and the platform is supported")
    } else if opt.pipewire {
        pipewire_host_id
            .and_then(cpal::host_from_id)
            .expect("make sure `--features pipewire` is specified, and the platform is supported")
    } else {
        cpal::default_host()
    };

    let device = if let Some(device) = opt.device {
        let id = &device.parse().expect("failed to parse device id");
        host.device_by_id(id)
    } else {
        host.default_output_device()
    }
    .expect("failed to find output device");
    println!("Output device: {}", device.id()?);

    let config = device.default_output_config().unwrap();
    println!("Default output config: {config:?}");

    match config.sample_format() {
        cpal::SampleFormat::I8 => run::<i8>(&device, config.into()),
        cpal::SampleFormat::I16 => run::<i16>(&device, config.into()),
        cpal::SampleFormat::I24 => run::<I24>(&device, config.into()),
        cpal::SampleFormat::I32 => run::<i32>(&device, config.into()),
        // cpal::SampleFormat::I48 => run::<I48>(&device, config.into()),
        cpal::SampleFormat::I64 => run::<i64>(&device, config.into()),
        cpal::SampleFormat::U8 => run::<u8>(&device, config.into()),
        cpal::SampleFormat::U16 => run::<u16>(&device, config.into()),
        // cpal::SampleFormat::U24 => run::<U24>(&device, config.into()),
        cpal::SampleFormat::U32 => run::<u32>(&device, config.into()),
        // cpal::SampleFormat::U48 => run::<U48>(&device, config.into()),
        cpal::SampleFormat::U64 => run::<u64>(&device, config.into()),
        cpal::SampleFormat::F32 => run::<f32>(&device, config.into()),
        cpal::SampleFormat::F64 => run::<f64>(&device, config.into()),
        sample_format => panic!("Unsupported sample format '{sample_format}'"),
    }
}

pub fn run<T>(device: &cpal::Device, config: cpal::StreamConfig) -> Result<(), anyhow::Error>
where
    T: SizedSample + FromSample<f32>,
{
    let sample_rate = config.sample_rate as f32;
    let channels = config.channels as usize;

    // Produce a sinusoid of maximum amplitude.
    let mut sample_clock = 0f32;
    let mut next_value = move || {
        sample_clock = (sample_clock + 1.0) % sample_rate;
        (sample_clock * 440.0 * 2.0 * std::f32::consts::PI / sample_rate).sin()
    };

    let err_fn = |err| eprintln!("an error occurred on stream: {err}");

    let stream = device.build_output_stream(
        config,
        move |data: &mut [T], _: &cpal::OutputCallbackInfo| {
            write_data(data, channels, &mut next_value)
        },
        err_fn,
        None,
    )?;
    stream.play()?;

    std::thread::sleep(std::time::Duration::from_millis(1000));

    Ok(())
}

fn write_data<T>(output: &mut [T], channels: usize, next_sample: &mut dyn FnMut() -> f32)
where
    T: Sample + FromSample<f32>,
{
    for frame in output.chunks_mut(channels) {
        let value: T = T::from_sample(next_sample());
        for sample in frame.iter_mut() {
            *sample = value;
        }
    }
}
```

## File: `examples/custom.rs`
```rust
use std::sync::{
    atomic::{AtomicBool, Ordering},
    Arc,
};

use cpal::{
    traits::{DeviceTrait, HostTrait, StreamTrait},
    DeviceDescription, DeviceDescriptionBuilder,
};
use cpal::{FromSample, Sample};

#[allow(dead_code)]
#[derive(Clone)] // Clone, Send+Sync are required
struct MyHost;

#[derive(Clone)] // Clone, Send+Sync are required
struct MyDevice;

// Only Send+Sync is needed
struct MyStream {
    controls: Arc<StreamControls>,
    // option is needed since joining a thread takes ownership,
    // and we want to do that on drop (gives us &mut self, not self)
    handle: Option<std::thread::JoinHandle<()>>,
}

struct StreamControls {
    exit: AtomicBool,
    pause: AtomicBool,
}

impl HostTrait for MyHost {
    type Device = MyDevice;
    type Devices = std::iter::Once<MyDevice>;

    fn is_available() -> bool {
        true
    }

    fn devices(&self) -> Result<Self::Devices, cpal::DevicesError> {
        Ok(std::iter::once(MyDevice))
    }

    fn default_input_device(&self) -> Option<Self::Device> {
        None
    }

    fn default_output_device(&self) -> Option<Self::Device> {
        Some(MyDevice)
    }
}

impl DeviceTrait for MyDevice {
    type SupportedInputConfigs = std::iter::Empty<cpal::SupportedStreamConfigRange>;
    type SupportedOutputConfigs = std::iter::Once<cpal::SupportedStreamConfigRange>;
    type Stream = MyStream;

    fn name(&self) -> Result<String, cpal::DeviceNameError> {
        Ok(String::from("custom"))
    }

    fn description(&self) -> Result<DeviceDescription, cpal::DeviceNameError> {
        Ok(DeviceDescriptionBuilder::new("Custom Device".to_string()).build())
    }

    fn id(&self) -> Result<cpal::DeviceId, cpal::DeviceIdError> {
        Err(cpal::DeviceIdError::UnsupportedPlatform)
    }

    fn supported_input_configs(
        &self,
    ) -> Result<Self::SupportedInputConfigs, cpal::SupportedStreamConfigsError> {
        Ok(std::iter::empty())
    }

    fn supported_output_configs(
        &self,
    ) -> Result<Self::SupportedOutputConfigs, cpal::SupportedStreamConfigsError> {
        Ok(std::iter::once(cpal::SupportedStreamConfigRange::new(
            2,
            44100,
            44100,
            cpal::SupportedBufferSize::Unknown,
            cpal::SampleFormat::F32,
        )))
    }

    fn default_input_config(
        &self,
    ) -> Result<cpal::SupportedStreamConfig, cpal::DefaultStreamConfigError> {
        Err(cpal::DefaultStreamConfigError::StreamTypeNotSupported)
    }

    fn default_output_config(
        &self,
    ) -> Result<cpal::SupportedStreamConfig, cpal::DefaultStreamConfigError> {
        Ok(cpal::SupportedStreamConfig::new(
            2,
            44100,
            cpal::SupportedBufferSize::Unknown,
            cpal::SampleFormat::I16,
        ))
    }

    fn build_input_stream_raw<D, E>(
        &self,
        _: cpal::StreamConfig,
        _: cpal::SampleFormat,
        _: D,
        _: E,
        _: Option<std::time::Duration>,
    ) -> Result<Self::Stream, cpal::BuildStreamError>
    where
        D: FnMut(&cpal::Data, &cpal::InputCallbackInfo) + Send + 'static,
        E: FnMut(cpal::StreamError) + Send + 'static,
    {
        Err(cpal::BuildStreamError::StreamConfigNotSupported)
    }

    // this is the meat of a custom device impl.
    // you're expected to repeatedly call `data_callback` and provide it with a buffer of samples,
    // as well as a stream timestamp.
    // a proper impl would also check the stream config and sample format, as well as handle errors
    fn build_output_stream_raw<D, E>(
        &self,
        _: cpal::StreamConfig,
        _: cpal::SampleFormat,
        mut data_callback: D,
        _: E,
        _: Option<std::time::Duration>,
    ) -> Result<Self::Stream, cpal::BuildStreamError>
    where
        D: FnMut(&mut cpal::Data, &cpal::OutputCallbackInfo) + Send + 'static,
        E: FnMut(cpal::StreamError) + Send + 'static,
    {
        let controls = Arc::new(StreamControls {
            exit: AtomicBool::new(false),
            pause: AtomicBool::new(true), // streams are expected to start out paused by default
        });

        let thread_controls = controls.clone();
        let handle = std::thread::spawn(move || {
            let start = std::time::Instant::now();
            let mut buffer = [0.0_f32; 4096];
            while !thread_controls.exit.load(Ordering::Relaxed) {
                std::thread::sleep(std::time::Duration::from_secs_f32(
                    buffer.len() as f32 / 44100.0,
                ));
                // continue if paused
                if thread_controls.pause.load(Ordering::Relaxed) {
                    continue;
                }

                // data is cpal's way of having a type erased buffer.
                // you're expected to provide a raw pointer, the amount of samples, and the sample format of the buffer
                let mut data = unsafe {
                    cpal::Data::from_parts(
                        buffer.as_mut_ptr().cast(),
                        buffer.len(),
                        cpal::SampleFormat::F32,
                    )
                };

                let duration = std::time::Instant::now().duration_since(start);
                let secs = duration.as_nanos() / 1_000_000_000;
                let subsec_nanos = duration.as_nanos() - secs * 1_000_000_000;
                let stream_instant = cpal::StreamInstant::new(secs as _, subsec_nanos as _);
                let timestamp = cpal::OutputStreamTimestamp {
                    callback: stream_instant,
                    playback: stream_instant,
                };
                data_callback(&mut data, &cpal::OutputCallbackInfo::new(timestamp));

                let avg = buffer.iter().sum::<f32>() / buffer.len() as f32;
                println!("avg: {avg}");
            }
        });

        Ok(MyStream {
            controls,
            handle: Some(handle),
        })
    }
}

impl StreamTrait for MyStream {
    fn play(&self) -> Result<(), cpal::PlayStreamError> {
        self.controls.pause.store(false, Ordering::Relaxed);
        Ok(())
    }

    fn pause(&self) -> Result<(), cpal::PauseStreamError> {
        self.controls.pause.store(true, Ordering::Relaxed);
        Ok(())
    }
}

// streams are expected to stop when dropped
impl Drop for MyStream {
    fn drop(&mut self) {
        self.controls.exit.store(true, Ordering::Relaxed);
        let _ = self.handle.take().unwrap().join();
    }
}

#[cfg(feature = "custom")]
fn main() {
    let custom_host = cpal::platform::CustomHost::from_host(MyHost);
    // alternatively, use cpal::platform::CustomDevice and skip enumerating devices
    let host = cpal::Host::from(custom_host); // this host can be passed to rodio or any other crate that uses cpal

    let device = host.default_output_device().unwrap();
    let config = device.default_output_config().unwrap();

    let stream = make_stream(&device, config.into()).unwrap();
    stream.play().unwrap();
    std::thread::sleep(std::time::Duration::from_millis(4000));
}

#[cfg(not(feature = "custom"))]
fn main() {
    panic!("please run with -F custom to try this example")
}

// rest of this example is mostly based off of synth_tones.rs

pub enum Waveform {
    Sine,
    Square,
    Saw,
    Triangle,
}

pub struct Oscillator {
    pub sample_rate: f32,
    pub waveform: Waveform,
    pub current_sample_index: f32,
    pub frequency_hz: f32,
}

impl Oscillator {
    fn advance_sample(&mut self) {
        self.current_sample_index = (self.current_sample_index + 1.0) % self.sample_rate;
    }

    fn set_waveform(&mut self, waveform: Waveform) {
        self.waveform = waveform;
    }

    fn calculate_sine_output_from_freq(&self, freq: f32) -> f32 {
        let two_pi = 2.0 * std::f32::consts::PI;
        (self.current_sample_index * freq * two_pi / self.sample_rate).sin()
    }

    fn is_multiple_of_freq_above_nyquist(&self, multiple: f32) -> bool {
        self.frequency_hz * multiple > self.sample_rate / 2.0
    }

    fn sine_wave(&mut self) -> f32 {
        self.advance_sample();
        self.calculate_sine_output_from_freq(self.frequency_hz)
    }

    fn generative_waveform(&mut self, harmonic_index_increment: i32, gain_exponent: f32) -> f32 {
        self.advance_sample();
        let mut output = 0.0;
        let mut i = 1;
        while !self.is_multiple_of_freq_above_nyquist(i as f32) {
            let gain = 1.0 / (i as f32).powf(gain_exponent);
            output += gain * self.calculate_sine_output_from_freq(self.frequency_hz * i as f32);
            i += harmonic_index_increment;
        }
        output
    }

    fn square_wave(&mut self) -> f32 {
        self.generative_waveform(2, 1.0)
    }

    fn saw_wave(&mut self) -> f32 {
        self.generative_waveform(1, 1.0)
    }

    fn triangle_wave(&mut self) -> f32 {
        self.generative_waveform(2, 2.0)
    }

    fn tick(&mut self) -> f32 {
        match self.waveform {
            Waveform::Sine => self.sine_wave(),
            Waveform::Square => self.square_wave(),
            Waveform::Saw => self.saw_wave(),
            Waveform::Triangle => self.triangle_wave(),
        }
    }
}

pub fn make_stream(
    device: &cpal::Device,
    config: cpal::StreamConfig,
) -> Result<cpal::Stream, anyhow::Error> {
    let num_channels = config.channels as usize;
    let mut oscillator = Oscillator {
        waveform: Waveform::Sine,
        sample_rate: config.sample_rate as f32,
        current_sample_index: 0.0,
        frequency_hz: 440.0,
    };
    let err_fn = |err| eprintln!("Error building output sound stream: {err}");

    let time_at_start = std::time::Instant::now();
    println!("Time at start: {time_at_start:?}");

    let stream = device.build_output_stream(
        config,
        move |output: &mut [f32], _: &cpal::OutputCallbackInfo| {
            // for 0-1s play sine, 1-2s play square, 2-3s play saw, 3-4s play triangle_wave
            let time_since_start = std::time::Instant::now()
                .duration_since(time_at_start)
                .as_secs_f32();
            if time_since_start < 1.0 {
                oscillator.set_waveform(Waveform::Sine);
            } else if time_since_start < 2.0 {
                oscillator.set_waveform(Waveform::Triangle);
            } else if time_since_start < 3.0 {
                oscillator.set_waveform(Waveform::Square);
            } else if time_since_start < 4.0 {
                oscillator.set_waveform(Waveform::Saw);
            } else {
                oscillator.set_waveform(Waveform::Sine);
            }
            process_frame(output, &mut oscillator, num_channels)
        },
        err_fn,
        None,
    )?;

    Ok(stream)
}

fn process_frame<SampleType>(
    output: &mut [SampleType],
    oscillator: &mut Oscillator,
    num_channels: usize,
) where
    SampleType: Sample + FromSample<f32>,
{
    for frame in output.chunks_mut(num_channels) {
        let value: SampleType = SampleType::from_sample(oscillator.tick());

        // copy the same value to all channels
        for sample in frame.iter_mut() {
            *sample = value;
        }
    }
}
```

## File: `examples/enumerate.rs`
```rust
//! Enumerates all available audio hosts, devices, and their supported configurations.
//!
//! This example demonstrates:
//! - Querying available audio hosts on the system
//! - Enumerating all audio devices for each host
//! - Retrieving device IDs for persistent identification
//! - Getting device descriptions with metadata
//! - Listing supported input and output stream configurations
//!
//! Run with: `cargo run --example enumerate`

extern crate anyhow;
extern crate cpal;

use cpal::traits::{DeviceTrait, HostTrait};

fn main() -> Result<(), anyhow::Error> {
    // To print raw ALSA errors to stderr during enumeration, comment out the line below:
    #[cfg(target_os = "linux")]
    let _silence_alsa_errors = alsa::Output::local_error_handler()?;

    println!("Supported hosts:\n  {:?}", cpal::ALL_HOSTS);
    let available_hosts = cpal::available_hosts();
    println!("Available hosts:\n  {available_hosts:?}");

    for host_id in available_hosts {
        println!("{}", host_id.name());
        let host = cpal::host_from_id(host_id)?;

        let default_in = host
            .default_input_device()
            .map(|dev| dev.id().unwrap())
            .map(|id| id.to_string());
        let default_out = host
            .default_output_device()
            .map(|dev| dev.id().unwrap())
            .map(|id| id.to_string());
        println!("  Default Input Device:\n    {default_in:?}");
        println!("  Default Output Device:\n    {default_out:?}");

        let devices = host.devices()?;
        println!("  Devices: ");
        for (device_index, device) in devices.enumerate() {
            let id = device
                .id()
                .map_or("Unknown ID".to_string(), |id| id.to_string());
            if let Ok(desc) = device.description() {
                println!("  {}. {id} ({})", device_index + 1, desc);
            } else {
                println!("  {}. {id}", device_index + 1);
            }

            // Input configs
            if let Ok(conf) = device.default_input_config() {
                println!("    Default input stream config:\n      {conf:?}");
            }
            let input_configs = match device.supported_input_configs() {
                Ok(f) => f.collect(),
                Err(e) => {
                    println!("    Error getting supported input configs: {e:?}");
                    Vec::new()
                }
            };
            if !input_configs.is_empty() {
                println!("    All supported input stream configs:");
                for (config_index, config) in input_configs.into_iter().enumerate() {
                    println!(
                        "      {}.{}. {:?}",
                        device_index + 1,
                        config_index + 1,
                        config
                    );
                }
            }

            // Output configs
            if let Ok(conf) = device.default_output_config() {
                println!("    Default output stream config:\n      {conf:?}");
            }
            let output_configs = match device.supported_output_configs() {
                Ok(f) => f.collect(),
                Err(e) => {
                    println!("    Error getting supported output configs: {e:?}");
                    Vec::new()
                }
            };
            if !output_configs.is_empty() {
                println!("    All supported output stream configs:");
                for (config_index, config) in output_configs.into_iter().enumerate() {
                    println!(
                        "      {}.{}. {:?}",
                        device_index + 1,
                        config_index + 1,
                        config
                    );
                }
            }
        }
    }

    Ok(())
}
```

## File: `examples/feedback.rs`
```rust
//! Feeds back the input stream directly into the output stream.
//!
//! Assumes that the input and output devices can use the same stream configuration and that they
//! support the f32 sample format.
//!
//! Uses a delay of `LATENCY_MS` milliseconds in case the default input and output streams are not
//! precisely synchronised.

use clap::Parser;
use cpal::{
    traits::{DeviceTrait, HostTrait, StreamTrait},
    HostUnavailable,
};
use ringbuf::{
    traits::{Consumer, Producer, Split},
    HeapRb,
};

#[derive(Parser, Debug)]
#[command(version, about = "CPAL feedback example", long_about = None)]
struct Opt {
    /// The input audio device to use
    #[arg(short, long, value_name = "IN")]
    input_device: Option<String>,

    /// The output audio device to use
    #[arg(short, long, value_name = "OUT")]
    output_device: Option<String>,

    /// Specify the delay between input and output
    #[arg(short, long, value_name = "DELAY_MS", default_value_t = 150.0)]
    latency: f32,

    /// Use the JACK host. Requires `--features jack`.
    #[arg(long, default_value_t = false)]
    jack: bool,

    /// Use the PulseAudio host. Requires `--features pulseaudio`.
    #[arg(long, default_value_t = false)]
    pulseaudio: bool,
}

fn main() -> anyhow::Result<()> {
    let opt = Opt::parse();

    // Jack/PulseAudio support must be enabled at compile time, and is
    // only available on some platforms.
    #[allow(unused_mut, unused_assignments)]
    let mut jack_host_id = Err(HostUnavailable);
    #[allow(unused_mut, unused_assignments)]
    let mut pulseaudio_host_id = Err(HostUnavailable);

    #[cfg(any(
        target_os = "linux",
        target_os = "dragonfly",
        target_os = "freebsd",
        target_os = "netbsd"
    ))]
    {
        #[cfg(feature = "jack")]
        {
            jack_host_id = Ok(cpal::HostId::Jack);
        }

        #[cfg(feature = "pulseaudio")]
        {
            pulseaudio_host_id = Ok(cpal::HostId::PulseAudio);
        }
    }

    // Manually check for flags. Can be passed through cargo with -- e.g.
    // cargo run --release --example beep --features jack -- --jack
    let host = if opt.jack {
        jack_host_id
            .and_then(cpal::host_from_id)
            .expect("make sure `--features jack` is specified, and the platform is supported")
    } else if opt.pulseaudio {
        pulseaudio_host_id
            .and_then(cpal::host_from_id)
            .expect("make sure `--features pulseaudio` is specified, and the platform is supported")
    } else {
        cpal::default_host()
    };

    // Find devices.
    let input_device = if let Some(device) = opt.input_device {
        let id = &device.parse().expect("failed to parse input device id");
        host.device_by_id(id)
    } else {
        host.default_input_device()
    }
    .expect("failed to find input device");

    let output_device = if let Some(device) = opt.output_device {
        let id = &device.parse().expect("failed to parse output device id");
        host.device_by_id(id)
    } else {
        host.default_output_device()
    }
    .expect("failed to find output device");

    println!("Using input device: \"{}\"", input_device.id()?);
    println!("Using output device: \"{}\"", output_device.id()?);

    // We'll try and use the same configuration between streams to keep it simple.
    let config: cpal::StreamConfig = input_device.default_input_config()?.into();

    // Create a delay in case the input and output devices aren't synced.
    let latency_frames = (opt.latency / 1_000.0) * config.sample_rate as f32;
    let latency_samples = latency_frames as usize * config.channels as usize;

    // The buffer to share samples
    let ring = HeapRb::<f32>::new(latency_samples * 2);
    let (mut producer, mut consumer) = ring.split();

    // Fill the samples with 0.0 equal to the length of the delay.
    for _ in 0..latency_samples {
        // The ring buffer has twice as much space as necessary to add latency here,
        // so this should never fail
        producer.try_push(0.0).unwrap();
    }

    let input_data_fn = move |data: &[f32], _: &cpal::InputCallbackInfo| {
        let mut output_fell_behind = false;
        for &sample in data {
            if producer.try_push(sample).is_err() {
                output_fell_behind = true;
            }
        }
        if output_fell_behind {
            eprintln!("output stream fell behind: try increasing latency");
        }
    };

    let output_data_fn = move |data: &mut [f32], _: &cpal::OutputCallbackInfo| {
        let mut input_fell_behind = false;
        for sample in data {
            *sample = match consumer.try_pop() {
                Some(s) => s,
                None => {
                    input_fell_behind = true;
                    0.0
                }
            };
        }
        if input_fell_behind {
            eprintln!("input stream fell behind: try increasing latency");
        }
    };

    // Build streams.
    println!("Attempting to build both streams with f32 samples and `{config:?}`.");
    let input_stream = input_device.build_input_stream(config, input_data_fn, err_fn, None)?;
    let output_stream = output_device.build_output_stream(config, output_data_fn, err_fn, None)?;
    println!("Successfully built streams.");

    // Play the streams.
    println!(
        "Starting the input and output streams with `{}` milliseconds of latency.",
        opt.latency
    );
    input_stream.play()?;
    output_stream.play()?;

    // Run for 10 seconds before closing.
    println!("Playing for 10 seconds... ");
    std::thread::sleep(std::time::Duration::from_secs(10));
    drop(input_stream);
    drop(output_stream);
    println!("Done!");
    Ok(())
}

fn err_fn(err: cpal::StreamError) {
    eprintln!("an error occurred on stream: {err}");
}
```

## File: `examples/record_wav.rs`
```rust
//! Records a WAV file (roughly 3 seconds long) using the default input device and config.
//!
//! The input data is recorded to "$CARGO_MANIFEST_DIR/recorded.wav".

use clap::Parser;
use cpal::traits::{DeviceTrait, HostTrait, StreamTrait};
use cpal::{FromSample, HostUnavailable, Sample};
use std::fs::File;
use std::io::BufWriter;
use std::sync::{Arc, Mutex};

#[derive(Parser, Debug)]
#[command(version, about = "CPAL record_wav example", long_about = None)]
struct Opt {
    /// The audio device to use.
    #[arg(short, long)]
    device: Option<String>,

    /// How long to record, in seconds
    #[arg(long, default_value_t = 3)]
    duration: u64,

    /// Use the JACK host. Requires `--features jack`.
    #[arg(long, default_value_t = false)]
    jack: bool,

    /// Use the PulseAudio host. Requires `--features pulseaudio`.
    #[arg(long, default_value_t = false)]
    pulseaudio: bool,

    /// Use the Pipewire host. Requires `--features pipewire`
    #[arg(long, default_value_t = false)]
    pipewire: bool,
}

fn main() -> Result<(), anyhow::Error> {
    let opt = Opt::parse();

    // Jack/PulseAudio support must be enabled at compile time, and is
    // only available on some platforms.
    #[allow(unused_mut, unused_assignments)]
    let mut jack_host_id = Err(HostUnavailable);
    #[allow(unused_mut, unused_assignments)]
    let mut pulseaudio_host_id = Err(HostUnavailable);
    #[allow(unused_mut, unused_assignments)]
    let mut pipewire_host_id = Err(HostUnavailable);
    #[cfg(any(
        target_os = "linux",
        target_os = "dragonfly",
        target_os = "freebsd",
        target_os = "netbsd"
    ))]
    {
        #[cfg(feature = "jack")]
        {
            jack_host_id = Ok(cpal::HostId::Jack);
        }

        #[cfg(feature = "pulseaudio")]
        {
            pulseaudio_host_id = Ok(cpal::HostId::PulseAudio);
        }
        #[cfg(feature = "pipewire")]
        {
            pipewire_host_id = Ok(cpal::HostId::PipeWire);
        }
    }

    // Manually check for flags. Can be passed through cargo with -- e.g.
    // cargo run --release --example record_wav --features jack -- --jack
    let host = if opt.jack {
        jack_host_id
            .and_then(cpal::host_from_id)
            .expect("make sure `--features jack` is specified, and the platform is supported")
    } else if opt.pulseaudio {
        pulseaudio_host_id
            .and_then(cpal::host_from_id)
            .expect("make sure `--features pulseaudio` is specified, and the platform is supported")
    } else if opt.pipewire {
        pipewire_host_id
            .and_then(cpal::host_from_id)
            .expect("make sure `--features pipewire` is specified, and the platform is supported")
    } else {
        cpal::default_host()
    };

    // Set up the input device and stream with the default input config.
    let device = if let Some(device) = opt.device {
        let id = &device.parse().expect("failed to parse input device id");
        host.device_by_id(id)
    } else {
        host.default_input_device()
    }
    .expect("failed to find input device");

    println!("Input device: {}", device.id()?);

    let config = if device.supports_input() {
        device.default_input_config()
    } else {
        device.default_output_config()
    }
    .expect("Failed to get default input/output config");
    println!("Default input/output config: {config:?}");

    // The WAV file we're recording to.
    const PATH: &str = concat!(env!("CARGO_MANIFEST_DIR"), "/recorded.wav");
    let spec = wav_spec_from_config(&config);
    let writer = hound::WavWriter::create(PATH, spec)?;
    let writer = Arc::new(Mutex::new(Some(writer)));

    // A flag to indicate that recording is in progress.
    println!("Begin recording...");

    // Run the input stream on a separate thread.
    let writer_2 = writer.clone();

    let err_fn = move |err| {
        eprintln!("an error occurred on stream: {err}");
    };

    let stream = match config.sample_format() {
        cpal::SampleFormat::I8 => device.build_input_stream(
            config.into(),
            move |data, _: &_| write_input_data::<i8, i8>(data, &writer_2),
            err_fn,
            None,
        )?,
        cpal::SampleFormat::I16 => device.build_input_stream(
            config.into(),
            move |data, _: &_| write_input_data::<i16, i16>(data, &writer_2),
            err_fn,
            None,
        )?,
        cpal::SampleFormat::I32 => device.build_input_stream(
            config.into(),
            move |data, _: &_| write_input_data::<i32, i32>(data, &writer_2),
            err_fn,
            None,
        )?,
        cpal::SampleFormat::F32 => device.build_input_stream(
            config.into(),
            move |data, _: &_| write_input_data::<f32, f32>(data, &writer_2),
            err_fn,
            None,
        )?,
        sample_format => {
            return Err(anyhow::Error::msg(format!(
                "Unsupported sample format '{sample_format}'"
            )))
        }
    };

    stream.play()?;

    // Let recording go for roughly three seconds.
    std::thread::sleep(std::time::Duration::from_secs(opt.duration));
    drop(stream);
    writer.lock().unwrap().take().unwrap().finalize()?;
    println!("Recording {PATH} complete!");
    Ok(())
}

fn sample_format(format: cpal::SampleFormat) -> hound::SampleFormat {
    if format.is_dsd() {
        panic!("DSD formats cannot be written to WAV files");
    } else if format.is_float() {
        hound::SampleFormat::Float
    } else {
        hound::SampleFormat::Int
    }
}

fn wav_spec_from_config(config: &cpal::SupportedStreamConfig) -> hound::WavSpec {
    hound::WavSpec {
        channels: config.channels() as _,
        sample_rate: config.sample_rate() as _,
        bits_per_sample: (config.sample_format().sample_size() * 8) as _,
        sample_format: sample_format(config.sample_format()),
    }
}

type WavWriterHandle = Arc<Mutex<Option<hound::WavWriter<BufWriter<File>>>>>;

fn write_input_data<T, U>(input: &[T], writer: &WavWriterHandle)
where
    T: Sample,
    U: Sample + hound::Sample + FromSample<T>,
{
    if let Ok(mut guard) = writer.try_lock() {
        if let Some(writer) = guard.as_mut() {
            for &sample in input.iter() {
                let sample: U = U::from_sample(sample);
                writer.write_sample(sample).ok();
            }
        }
    }
}
```

## File: `examples/synth_tones.rs`
```rust
/* This example expose parameter to pass generator of sample.
Good starting point for integration of cpal into your application.
*/

extern crate anyhow;
extern crate clap;
extern crate cpal;

use cpal::{
    traits::{DeviceTrait, HostTrait, StreamTrait},
    SizedSample, I24, U24,
};
use cpal::{FromSample, Sample};

fn main() -> anyhow::Result<()> {
    let stream = stream_setup_for()?;
    stream.play()?;
    std::thread::sleep(std::time::Duration::from_millis(4000));
    Ok(())
}

pub enum Waveform {
    Sine,
    Square,
    Saw,
    Triangle,
}

pub struct Oscillator {
    pub sample_rate: f32,
    pub waveform: Waveform,
    pub current_sample_index: f32,
    pub frequency_hz: f32,
}

impl Oscillator {
    fn advance_sample(&mut self) {
        self.current_sample_index = (self.current_sample_index + 1.0) % self.sample_rate;
    }

    fn set_waveform(&mut self, waveform: Waveform) {
        self.waveform = waveform;
    }

    fn calculate_sine_output_from_freq(&self, freq: f32) -> f32 {
        let two_pi = 2.0 * std::f32::consts::PI;
        (self.current_sample_index * freq * two_pi / self.sample_rate).sin()
    }

    fn is_multiple_of_freq_above_nyquist(&self, multiple: f32) -> bool {
        self.frequency_hz * multiple > self.sample_rate / 2.0
    }

    fn sine_wave(&mut self) -> f32 {
        self.advance_sample();
        self.calculate_sine_output_from_freq(self.frequency_hz)
    }

    fn generative_waveform(&mut self, harmonic_index_increment: i32, gain_exponent: f32) -> f32 {
        self.advance_sample();
        let mut output = 0.0;
        let mut i = 1;
        while !self.is_multiple_of_freq_above_nyquist(i as f32) {
            let gain = 1.0 / (i as f32).powf(gain_exponent);
            output += gain * self.calculate_sine_output_from_freq(self.frequency_hz * i as f32);
            i += harmonic_index_increment;
        }
        output
    }

    fn square_wave(&mut self) -> f32 {
        self.generative_waveform(2, 1.0)
    }

    fn saw_wave(&mut self) -> f32 {
        self.generative_waveform(1, 1.0)
    }

    fn triangle_wave(&mut self) -> f32 {
        self.generative_waveform(2, 2.0)
    }

    fn tick(&mut self) -> f32 {
        match self.waveform {
            Waveform::Sine => self.sine_wave(),
            Waveform::Square => self.square_wave(),
            Waveform::Saw => self.saw_wave(),
            Waveform::Triangle => self.triangle_wave(),
        }
    }
}

pub fn stream_setup_for() -> Result<cpal::Stream, anyhow::Error>
where
{
    let (_host, device, config) = host_device_setup()?;

    match config.sample_format() {
        cpal::SampleFormat::I8 => make_stream::<i8>(&device, config.into()),
        cpal::SampleFormat::I16 => make_stream::<i16>(&device, config.into()),
        cpal::SampleFormat::I24 => make_stream::<I24>(&device, config.into()),
        cpal::SampleFormat::I32 => make_stream::<i32>(&device, config.into()),
        cpal::SampleFormat::I64 => make_stream::<i64>(&device, config.into()),
        cpal::SampleFormat::U8 => make_stream::<u8>(&device, config.into()),
        cpal::SampleFormat::U16 => make_stream::<u16>(&device, config.into()),
        cpal::SampleFormat::U24 => make_stream::<U24>(&device, config.into()),
        cpal::SampleFormat::U32 => make_stream::<u32>(&device, config.into()),
        cpal::SampleFormat::U64 => make_stream::<u64>(&device, config.into()),
        cpal::SampleFormat::F32 => make_stream::<f32>(&device, config.into()),
        cpal::SampleFormat::F64 => make_stream::<f64>(&device, config.into()),
        sample_format => Err(anyhow::Error::msg(format!(
            "Unsupported sample format '{sample_format}'"
        ))),
    }
}

pub fn host_device_setup(
) -> Result<(cpal::Host, cpal::Device, cpal::SupportedStreamConfig), anyhow::Error> {
    let host = cpal::default_host();

    let device = host
        .default_output_device()
        .ok_or_else(|| anyhow::Error::msg("Default output device is not available"))?;
    println!("Output device: {}", device.id()?);

    let config = device.default_output_config()?;
    println!("Default output config: {config:?}");

    Ok((host, device, config))
}

pub fn make_stream<T>(
    device: &cpal::Device,
    config: cpal::StreamConfig,
) -> Result<cpal::Stream, anyhow::Error>
where
    T: SizedSample + FromSample<f32>,
{
    let num_channels = config.channels as usize;
    let mut oscillator = Oscillator {
        waveform: Waveform::Sine,
        sample_rate: config.sample_rate as f32,
        current_sample_index: 0.0,
        frequency_hz: 440.0,
    };
    let err_fn = |err| eprintln!("Error building output sound stream: {err}");

    let time_at_start = std::time::Instant::now();
    println!("Time at start: {time_at_start:?}");

    let stream = device.build_output_stream(
        config,
        move |output: &mut [T], _: &cpal::OutputCallbackInfo| {
            // for 0-1s play sine, 1-2s play square, 2-3s play saw, 3-4s play triangle_wave
            let time_since_start = std::time::Instant::now()
                .duration_since(time_at_start)
                .as_secs_f32();
            if time_since_start < 1.0 {
                oscillator.set_waveform(Waveform::Sine);
            } else if time_since_start < 2.0 {
                oscillator.set_waveform(Waveform::Triangle);
            } else if time_since_start < 3.0 {
                oscillator.set_waveform(Waveform::Square);
            } else if time_since_start < 4.0 {
                oscillator.set_waveform(Waveform::Saw);
            } else {
                oscillator.set_waveform(Waveform::Sine);
            }
            process_frame(output, &mut oscillator, num_channels)
        },
        err_fn,
        None,
    )?;

    Ok(stream)
}

fn process_frame<SampleType>(
    output: &mut [SampleType],
    oscillator: &mut Oscillator,
    num_channels: usize,
) where
    SampleType: Sample + FromSample<f32>,
{
    for frame in output.chunks_mut(num_channels) {
        let value: SampleType = SampleType::from_sample(oscillator.tick());

        // copy the same value to all channels
        for sample in frame.iter_mut() {
            *sample = value;
        }
    }
}
```

## File: `examples/android/.gitignore`
```
/target
/Cargo.lock
.cargo/
.DS_Store
recorded.wav
rls*.log
```

## File: `examples/android/Cargo.toml`
```
[package]
name = "android"
version = "0.1.0"
edition = "2021"

[dependencies]
cpal = { path = "../../" }
anyhow = "1.0"
ndk-glue = "0.7"

[lib]
name = "android"
path = "src/lib.rs"
crate-type = ["cdylib"]

[package.metadata.android]
# Specifies the package property of the manifest.
package = "com.foo.bar"

# Specifies the array of targets to build for.
build_targets = [ "armv7-linux-androideabi", "aarch64-linux-android", "i686-linux-android", "x86_64-linux-android" ]

# Name for final APK file.
# Defaults to package name.
apk_name = "myapp"

[package.metadata.android.sdk]
min_sdk_version = 26
target_sdk_version = 30
max_sdk_version = 29
```

## File: `examples/android/README.md`
```markdown
## How to install

```sh
rustup target add aarch64-linux-android armv7-linux-androideabi i686-linux-android x86_64-linux-android
```

## How to build apk

```sh
# Builds the project in release mode and places it into a `apk` file.
cargo apk build --release
```

more information at: https://github.com/rust-mobile/cargo-apk
```

## File: `examples/android/src/lib.rs`
```rust
#![allow(dead_code)]

extern crate anyhow;
extern crate cpal;

use cpal::{
    traits::{DeviceTrait, HostTrait, StreamTrait},
    SizedSample, I24,
};
use cpal::{FromSample, Sample};

#[cfg_attr(target_os = "android", ndk_glue::main(backtrace = "full"))]
fn main() {
    let host = cpal::default_host();

    let device = host
        .default_output_device()
        .expect("failed to find output device");

    let config = device.default_output_config().unwrap();

    match config.sample_format() {
        cpal::SampleFormat::I8 => run::<i8>(&device, config.into()).unwrap(),
        cpal::SampleFormat::I16 => run::<i16>(&device, config.into()).unwrap(),
        cpal::SampleFormat::I24 => run::<I24>(&device, config.into()).unwrap(),
        cpal::SampleFormat::I32 => run::<i32>(&device, config.into()).unwrap(),
        // cpal::SampleFormat::I48 => run::<I48>(&device, config.into()).unwrap(),
        cpal::SampleFormat::I64 => run::<i64>(&device, config.into()).unwrap(),
        cpal::SampleFormat::U8 => run::<u8>(&device, config.into()).unwrap(),
        cpal::SampleFormat::U16 => run::<u16>(&device, config.into()).unwrap(),
        // cpal::SampleFormat::U24 => run::<U24>(&device, config.into()).unwrap(),
        cpal::SampleFormat::U32 => run::<u32>(&device, config.into()).unwrap(),
        // cpal::SampleFormat::U48 => run::<U48>(&device, config.into()).unwrap(),
        cpal::SampleFormat::U64 => run::<u64>(&device, config.into()).unwrap(),
        cpal::SampleFormat::F32 => run::<f32>(&device, config.into()).unwrap(),
        cpal::SampleFormat::F64 => run::<f64>(&device, config.into()).unwrap(),
        sample_format => panic!("Unsupported sample format '{sample_format}'"),
    }
}

fn run<T>(device: &cpal::Device, config: cpal::StreamConfig) -> Result<(), anyhow::Error>
where
    T: SizedSample + FromSample<f32>,
{
    let sample_rate = config.sample_rate as f32;
    let channels = config.channels as usize;

    // Produce a sinusoid of maximum amplitude.
    let mut sample_clock = 0f32;
    let mut next_value = move || {
        sample_clock = (sample_clock + 1.0) % sample_rate;
        (sample_clock * 440.0 * 2.0 * std::f32::consts::PI / sample_rate).sin()
    };

    let err_fn = |err| eprintln!("an error occurred on stream: {}", err);

    let stream = device.build_output_stream(
        config,
        move |data: &mut [T], _: &cpal::OutputCallbackInfo| {
            write_data(data, channels, &mut next_value)
        },
        err_fn,
        None,
    )?;
    stream.play()?;

    std::thread::sleep(std::time::Duration::from_millis(1000));

    Ok(())
}

fn write_data<T>(output: &mut [T], channels: usize, next_sample: &mut dyn FnMut() -> f32)
where
    T: Sample + FromSample<f32>,
{
    for frame in output.chunks_mut(channels) {
        let value: T = T::from_sample(next_sample());
        for sample in frame.iter_mut() {
            *sample = value;
        }
    }
}
```

## File: `examples/audioworklet-beep/.gitignore`
```
Cargo.lock
/dist
/target
```

## File: `examples/audioworklet-beep/Cargo.toml`
```
[package]
name = "audioworklet-beep"
description = "cpal beep example for WebAssembly on an AudioWorklet"
version = "0.1.0"
edition = "2021"
authors = ["Ian Kettlewell <ian.kettlewell@gmail.com>"]

[lib]
crate-type = ["cdylib"]

[profile.release]
# This makes the compiled code faster and smaller, but it makes compiling slower,
# so it's only enabled in release mode.
lto = true

[dependencies]
cpal = { path = "../..", features = ["wasm-bindgen", "audioworklet"] }
# `gloo` is a utility crate which improves ergonomics over direct `web-sys` usage.
gloo = "0.11"

# The `wasm-bindgen` crate provides the bare minimum functionality needed
# to interact with JavaScript.
wasm-bindgen = "0.2"

# The `console_error_panic_hook` crate provides better debugging of panics by
# logging them with `console.error`.
console_error_panic_hook = "0.1"

# The `web-sys` crate allows you to interact with the various browser APIs,
# like the DOM.
[dependencies.web-sys]
version = "0.3"
features = ["console", "MouseEvent"]
```

## File: `examples/audioworklet-beep/README.md`
```markdown
## How to install

This example requires a nightly version of Rust to enable WebAssembly atomics and to recompile the standard library with atomics enabled.

Note the flags set to configure that in .cargo/config.toml.

This allows Rust to used shared memory and have the audio thread directly read / write to shared memory like a native platform.

To use shared memory the browser requires a specific 'CORS' configuration on the server-side.

Note the flags set to configure that in Trunk.toml.

[trunk](https://trunkrs.dev/) is used to build and serve the example.

```sh
cargo install --locked trunk
# -- or --
cargo binstall trunk
```

## How to run in debug mode

```sh
# Builds the project and opens it in a new browser tab. Auto-reloads when the project changes.
trunk serve --open
```

## How to build in release mode

```sh
# Builds the project in release mode and places it into the `dist` folder.
trunk build --release
```

## What does each file do?

* `Cargo.toml` contains the standard Rust metadata. You put your Rust dependencies in here. You must change this file with your details (name, description, version, authors, categories)

* The `src` folder contains your Rust code.
```

## File: `examples/audioworklet-beep/Trunk.toml`
```
[build]
target = "index.html"
dist = "dist"

[serve.headers]
# see ./assets/_headers for more documentation
"cross-origin-embedder-policy" = "require-corp"
"cross-origin-opener-policy" = "same-origin"
"cross-origin-resource-policy" = "same-site"
```

## File: `examples/audioworklet-beep/index.html`
```html
<!DOCTYPE html>
<html>

<head>
  <meta charset="UTF-8">
  <title>cpal AudioWorklet beep example</title>
</head>

<body>
  <input id="play" type="button" value="beep" />
  <input id="stop" type="button" value="stop" />
</body>

</html>
```

## File: `examples/audioworklet-beep/rust-toolchain.toml`
```
[toolchain]
channel = "nightly"
```

## File: `examples/audioworklet-beep/src/lib.rs`
```rust
use std::{cell::Cell, rc::Rc};

use cpal::{
    traits::{DeviceTrait, HostTrait, StreamTrait},
    Stream,
};
use wasm_bindgen::prelude::*;
use web_sys::console;

// This is like the `main` function, except for JavaScript.
#[wasm_bindgen(start)]
pub fn main_js() -> Result<(), JsValue> {
    // This provides better error messages in debug mode.
    // It's disabled in release mode, so it doesn't bloat up the file size.
    #[cfg(debug_assertions)]
    console_error_panic_hook::set_once();

    let document = gloo::utils::document();
    let play_button = document.get_element_by_id("play").unwrap();
    let stop_button = document.get_element_by_id("stop").unwrap();

    // stream needs to be referenced from the "play" and "stop" closures
    let stream = Rc::new(Cell::new(None));

    // set up play button
    {
        let stream = stream.clone();
        let closure = Closure::<dyn FnMut(_)>::new(move |_event: web_sys::MouseEvent| {
            stream.set(Some(beep()));
        });
        play_button
            .add_event_listener_with_callback("mousedown", closure.as_ref().unchecked_ref())?;
        closure.forget();
    }

    // set up stop button
    {
        let closure = Closure::<dyn FnMut(_)>::new(move |_event: web_sys::MouseEvent| {
            // stop the stream by dropping it
            stream.take();
        });
        stop_button
            .add_event_listener_with_callback("mousedown", closure.as_ref().unchecked_ref())?;
        closure.forget();
    }

    Ok(())
}

fn beep() -> Stream {
    let host =
        cpal::host_from_id(cpal::HostId::AudioWorklet).expect("AudioWorklet host not available");

    let device = host
        .default_output_device()
        .expect("failed to find a default output device");
    let config = device.default_output_config().unwrap();

    match config.sample_format() {
        cpal::SampleFormat::F32 => run::<f32>(&device, config.into()),
        cpal::SampleFormat::I16 => run::<i16>(&device, config.into()),
        cpal::SampleFormat::U16 => run::<u16>(&device, config.into()),
        _ => panic!("unsupported sample format"),
    }
}

fn run<T>(device: &cpal::Device, config: cpal::StreamConfig) -> Stream
where
    T: cpal::Sample + cpal::SizedSample + cpal::FromSample<f32>,
{
    let sample_rate = config.sample_rate as f32;
    let channels = config.channels as usize;

    // Produce a sinusoid of maximum amplitude.
    let mut sample_clock = 0f32;
    let mut next_value = move || {
        sample_clock = (sample_clock + 1.0) % sample_rate;
        (sample_clock * 440.0 * 2.0 * std::f32::consts::PI / sample_rate).sin()
    };

    let err_fn = |err| console::error_1(&format!("an error occurred on stream: {}", err).into());

    let stream = device
        .build_output_stream(
            config,
            move |data: &mut [T], _| write_data(data, channels, &mut next_value),
            err_fn,
            None,
        )
        .unwrap();
    stream.play().unwrap();
    stream
}

fn write_data<T>(output: &mut [T], channels: usize, next_sample: &mut dyn FnMut() -> f32)
where
    T: cpal::Sample + cpal::FromSample<f32>,
{
    for frame in output.chunks_mut(channels) {
        let sample = next_sample();
        let value = T::from_sample::<f32>(sample);
        for sample in frame.iter_mut() {
            *sample = value;
        }
    }
}
```

## File: `examples/ios-feedback/Cargo.toml`
```
[package]
name = "cpal-ios-example"
version = "0.1.0"
authors = ["Michael Hills <mhills@gmail.com>"]
edition = "2021"

[lib]
name = "cpal_ios_example"
crate-type = ["staticlib"]

[dependencies]
cpal = { path = "../.." }
anyhow = "1.0"
ringbuf = "0.4"
```

## File: `examples/ios-feedback/README.md`
```markdown
# iOS Feedback Example

This example is an Xcode project that exercises both input and output
audio streams. Audio samples are read in from your microphone and then
routed to your audio output device with a small but noticeable delay,
so you can verify it is working correctly.

To build the example you will need to install `cargo-lipo`. While not
necessary for building iOS binaries, it is used to build a universal
binary (x86 for simulator and aarch64 for device.)

```
cargo install cargo-lipo
```

Then open the XCode project and click run. A hook in the iOS application
lifecycle calls into the Rust code to start the input/output feedback
loop and immediately returns back control.

Before calling into Rust, the AVAudioSession category is configured.
This is important for controlling how audio is shared with the rest
of the system when your app is in the foreground. One example is
controlling whether other apps can play music in the background.
More information [here](https://developer.apple.com/library/archive/documentation/Audio/Conceptual/AudioSessionProgrammingGuide/AudioSessionCategoriesandModes/AudioSessionCategoriesandModes.html#//apple_ref/doc/uid/TP40007875-CH10).

```

## File: `examples/ios-feedback/build_rust_deps.sh`
```bash
#!/bin/sh

set -e

PATH=$PATH:$HOME/.cargo/bin
if [[ -n "${DEVELOPER_SDK_DIR:-}" ]]; then
  # Assume we're in Xcode, which means we're probably cross-compiling.
  # In this case, we need to add an extra library search path for build scripts and proc-macros,
  # which run on the host instead of the target.
  # (macOS Big Sur does not have linkable libraries in /usr/lib/.)
  export LIBRARY_PATH="${DEVELOPER_SDK_DIR}/MacOSX.sdk/usr/lib:${LIBRARY_PATH:-}"
fi

# If you want your build to run faster, add a "--targets x86_64-apple-ios" for just using the ios simulator.
if [ -n "${IOS_TARGETS}" ]; then
    cargo lipo --targets "${IOS_TARGETS}"
else
    cargo lipo
fi
```

## File: `examples/ios-feedback/cpal-ios-example.xcodeproj/project.pbxproj`
```
// !$*UTF8*$!
{
	archiveVersion = 1;
	classes = {
	};
	objectVersion = 50;
	objects = {

/* Begin PBXBuildFile section */
		57AB5AF3252767460040DE8C /* AVFoundation.framework in Frameworks */ = {isa = PBXBuildFile; fileRef = 57AB5AF2252767460040DE8C /* AVFoundation.framework */; };
		57AB5B07252769700040DE8C /* ViewController.m in Sources */ = {isa = PBXBuildFile; fileRef = 57AB5AFE252769700040DE8C /* ViewController.m */; };
		57AB5B08252769700040DE8C /* LaunchScreen.storyboard in Resources */ = {isa = PBXBuildFile; fileRef = 57AB5AFF252769700040DE8C /* LaunchScreen.storyboard */; };
		57AB5B09252769700040DE8C /* Main.storyboard in Resources */ = {isa = PBXBuildFile; fileRef = 57AB5B01252769700040DE8C /* Main.storyboard */; };
		57AB5B0A252769700040DE8C /* main.m in Sources */ = {isa = PBXBuildFile; fileRef = 57AB5B03252769700040DE8C /* main.m */; };
		57AB5B0B252769700040DE8C /* AppDelegate.m in Sources */ = {isa = PBXBuildFile; fileRef = 57AB5B04252769700040DE8C /* AppDelegate.m */; };
/* End PBXBuildFile section */

/* Begin PBXContainerItemProxy section */
		57AB5AEE252766820040DE8C /* PBXContainerItemProxy */ = {
			isa = PBXContainerItemProxy;
			containerPortal = 57AB5AC2252762C00040DE8C /* Project object */;
			proxyType = 1;
			remoteGlobalIDString = 57AB5AE9252766240040DE8C;
			remoteInfo = cargo_ios;
		};
/* End PBXContainerItemProxy section */

/* Begin PBXFileReference section */
		57AB5ACA252762C10040DE8C /* cpal-ios-example.app */ = {isa = PBXFileReference; explicitFileType = wrapper.application; includeInIndex = 0; path = "cpal-ios-example.app"; sourceTree = BUILT_PRODUCTS_DIR; };
		57AB5AF2252767460040DE8C /* AVFoundation.framework */ = {isa = PBXFileReference; lastKnownFileType = wrapper.framework; name = AVFoundation.framework; path = System/Library/Frameworks/AVFoundation.framework; sourceTree = SDKROOT; };
		57AB5AFD252769700040DE8C /* AppDelegate.h */ = {isa = PBXFileReference; fileEncoding = 4; lastKnownFileType = sourcecode.c.h; path = AppDelegate.h; sourceTree = "<group>"; };
		57AB5AFE252769700040DE8C /* ViewController.m */ = {isa = PBXFileReference; fileEncoding = 4; lastKnownFileType = sourcecode.c.objc; path = ViewController.m; sourceTree = "<group>"; };
		57AB5B00252769700040DE8C /* Base */ = {isa = PBXFileReference; lastKnownFileType = file.storyboard; name = Base; path = Base.lproj/LaunchScreen.storyboard; sourceTree = "<group>"; };
		57AB5B02252769700040DE8C /* Base */ = {isa = PBXFileReference; lastKnownFileType = file.storyboard; name = Base; path = Base.lproj/Main.storyboard; sourceTree = "<group>"; };
		57AB5B03252769700040DE8C /* main.m */ = {isa = PBXFileReference; fileEncoding = 4; lastKnownFileType = sourcecode.c.objc; path = main.m; sourceTree = "<group>"; };
		57AB5B04252769700040DE8C /* AppDelegate.m */ = {isa = PBXFileReference; fileEncoding = 4; lastKnownFileType = sourcecode.c.objc; path = AppDelegate.m; sourceTree = "<group>"; };
		57AB5B05252769700040DE8C /* Info.plist */ = {isa = PBXFileReference; fileEncoding = 4; lastKnownFileType = text.plist.xml; path = Info.plist; sourceTree = "<group>"; };
		57AB5B06252769700040DE8C /* ViewController.h */ = {isa = PBXFileReference; fileEncoding = 4; lastKnownFileType = sourcecode.c.h; path = ViewController.h; sourceTree = "<group>"; };
/* End PBXFileReference section */

/* Begin PBXFrameworksBuildPhase section */
		57AB5AC7252762C10040DE8C /* Frameworks */ = {
			isa = PBXFrameworksBuildPhase;
			buildActionMask = 2147483647;
			files = (
				57AB5AF3252767460040DE8C /* AVFoundation.framework in Frameworks */,
			);
			runOnlyForDeploymentPostprocessing = 0;
		};
/* End PBXFrameworksBuildPhase section */

/* Begin PBXGroup section */
		57AB5AC1252762C00040DE8C = {
			isa = PBXGroup;
			children = (
				57AB5AFC252769700040DE8C /* ios-src */,
				57AB5ACB252762C10040DE8C /* Products */,
				57AB5AF1252767460040DE8C /* Frameworks */,
			);
			sourceTree = "<group>";
		};
		57AB5ACB252762C10040DE8C /* Products */ = {
			isa = PBXGroup;
			children = (
				57AB5ACA252762C10040DE8C /* cpal-ios-example.app */,
			);
			name = Products;
			sourceTree = "<group>";
		};
		57AB5AF1252767460040DE8C /* Frameworks */ = {
			isa = PBXGroup;
			children = (
				57AB5AF2252767460040DE8C /* AVFoundation.framework */,
			);
			name = Frameworks;
			sourceTree = "<group>";
		};
		57AB5AFC252769700040DE8C /* ios-src */ = {
			isa = PBXGroup;
			children = (
				57AB5AFD252769700040DE8C /* AppDelegate.h */,
				57AB5B04252769700040DE8C /* AppDelegate.m */,
				57AB5B06252769700040DE8C /* ViewController.h */,
				57AB5AFE252769700040DE8C /* ViewController.m */,
				57AB5AFF252769700040DE8C /* LaunchScreen.storyboard */,
				57AB5B01252769700040DE8C /* Main.storyboard */,
				57AB5B05252769700040DE8C /* Info.plist */,
				57AB5B03252769700040DE8C /* main.m */,
			);
			path = "ios-src";
			sourceTree = "<group>";
		};
/* End PBXGroup section */

/* Begin PBXLegacyTarget section */
		57AB5AE9252766240040DE8C /* cargo_ios */ = {
			isa = PBXLegacyTarget;
			buildArgumentsString = build_rust_deps.sh;
			buildConfigurationList = 57AB5AEA252766240040DE8C /* Build configuration list for PBXLegacyTarget "cargo_ios" */;
			buildPhases = (
			);
			buildToolPath = /bin/sh;
			buildWorkingDirectory = .;
			dependencies = (
			);
			name = cargo_ios;
			passBuildSettingsInEnvironment = 1;
			productName = cargo_ios;
		};
/* End PBXLegacyTarget section */

/* Begin PBXNativeTarget section */
		57AB5AC9252762C10040DE8C /* cpal-ios-example */ = {
			isa = PBXNativeTarget;
			buildConfigurationList = 57AB5AE3252762C30040DE8C /* Build configuration list for PBXNativeTarget "cpal-ios-example" */;
			buildPhases = (
				57AB5AC6252762C10040DE8C /* Sources */,
				57AB5AC7252762C10040DE8C /* Frameworks */,
				57AB5AC8252762C10040DE8C /* Resources */,
			);
			buildRules = (
			);
			dependencies = (
				57AB5AEF252766820040DE8C /* PBXTargetDependency */,
			);
			name = "cpal-ios-example";
			productName = "cpal-ios-example";
			productReference = 57AB5ACA252762C10040DE8C /* cpal-ios-example.app */;
			productType = "com.apple.product-type.application";
		};
/* End PBXNativeTarget section */

/* Begin PBXProject section */
		57AB5AC2252762C00040DE8C /* Project object */ = {
			isa = PBXProject;
			attributes = {
				LastUpgradeCheck = 1200;
				TargetAttributes = {
					57AB5AC9252762C10040DE8C = {
						CreatedOnToolsVersion = 12.0.1;
					};
					57AB5AE9252766240040DE8C = {
						CreatedOnToolsVersion = 12.0.1;
					};
				};
			};
			buildConfigurationList = 57AB5AC5252762C00040DE8C /* Build configuration list for PBXProject "cpal-ios-example" */;
			compatibilityVersion = "Xcode 9.3";
			developmentRegion = en;
			hasScannedForEncodings = 0;
			knownRegions = (
				en,
				Base,
			);
			mainGroup = 57AB5AC1252762C00040DE8C;
			productRefGroup = 57AB5ACB252762C10040DE8C /* Products */;
			projectDirPath = "";
			projectRoot = "";
			targets = (
				57AB5AC9252762C10040DE8C /* cpal-ios-example */,
				57AB5AE9252766240040DE8C /* cargo_ios */,
			);
		};
/* End PBXProject section */

/* Begin PBXResourcesBuildPhase section */
		57AB5AC8252762C10040DE8C /* Resources */ = {
			isa = PBXResourcesBuildPhase;
			buildActionMask = 2147483647;
			files = (
				57AB5B09252769700040DE8C /* Main.storyboard in Resources */,
				57AB5B08252769700040DE8C /* LaunchScreen.storyboard in Resources */,
			);
			runOnlyForDeploymentPostprocessing = 0;
		};
/* End PBXResourcesBuildPhase section */

/* Begin PBXSourcesBuildPhase section */
		57AB5AC6252762C10040DE8C /* Sources */ = {
			isa = PBXSourcesBuildPhase;
			buildActionMask = 2147483647;
			files = (
				57AB5B0A252769700040DE8C /* main.m in Sources */,
				57AB5B0B252769700040DE8C /* AppDelegate.m in Sources */,
				57AB5B07252769700040DE8C /* ViewController.m in Sources */,
			);
			runOnlyForDeploymentPostprocessing = 0;
		};
/* End PBXSourcesBuildPhase section */

/* Begin PBXTargetDependency section */
		57AB5AEF252766820040DE8C /* PBXTargetDependency */ = {
			isa = PBXTargetDependency;
			target = 57AB5AE9252766240040DE8C /* cargo_ios */;
			targetProxy = 57AB5AEE252766820040DE8C /* PBXContainerItemProxy */;
		};
/* End PBXTargetDependency section */

/* Begin PBXVariantGroup section */
		57AB5AFF252769700040DE8C /* LaunchScreen.storyboard */ = {
			isa = PBXVariantGroup;
			children = (
				57AB5B00252769700040DE8C /* Base */,
			);
			name = LaunchScreen.storyboard;
			sourceTree = "<group>";
		};
		57AB5B01252769700040DE8C /* Main.storyboard */ = {
			isa = PBXVariantGroup;
			children = (
				57AB5B02252769700040DE8C /* Base */,
			);
			name = Main.storyboard;
			sourceTree = "<group>";
		};
/* End PBXVariantGroup section */

/* Begin XCBuildConfiguration section */
		57AB5AE1252762C30040DE8C /* Debug */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
				ALWAYS_SEARCH_USER_PATHS = NO;
				CLANG_ANALYZER_NONNULL = YES;
				CLANG_ANALYZER_NUMBER_OBJECT_CONVERSION = YES_AGGRESSIVE;
				CLANG_CXX_LANGUAGE_STANDARD = "gnu++14";
				CLANG_CXX_LIBRARY = "libc++";
				CLANG_ENABLE_MODULES = YES;
				CLANG_ENABLE_OBJC_ARC = YES;
				CLANG_ENABLE_OBJC_WEAK = YES;
				CLANG_WARN_BLOCK_CAPTURE_AUTORELEASING = YES;
				CLANG_WARN_BOOL_CONVERSION = YES;
				CLANG_WARN_COMMA = YES;
				CLANG_WARN_CONSTANT_CONVERSION = YES;
				CLANG_WARN_DEPRECATED_OBJC_IMPLEMENTATIONS = YES;
				CLANG_WARN_DIRECT_OBJC_ISA_USAGE = YES_ERROR;
				CLANG_WARN_DOCUMENTATION_COMMENTS = YES;
				CLANG_WARN_EMPTY_BODY = YES;
				CLANG_WARN_ENUM_CONVERSION = YES;
				CLANG_WARN_INFINITE_RECURSION = YES;
				CLANG_WARN_INT_CONVERSION = YES;
				CLANG_WARN_NON_LITERAL_NULL_CONVERSION = YES;
				CLANG_WARN_OBJC_IMPLICIT_RETAIN_SELF = YES;
				CLANG_WARN_OBJC_LITERAL_CONVERSION = YES;
				CLANG_WARN_OBJC_ROOT_CLASS = YES_ERROR;
				CLANG_WARN_QUOTED_INCLUDE_IN_FRAMEWORK_HEADER = YES;
				CLANG_WARN_RANGE_LOOP_ANALYSIS = YES;
				CLANG_WARN_STRICT_PROTOTYPES = YES;
				CLANG_WARN_SUSPICIOUS_MOVE = YES;
				CLANG_WARN_UNGUARDED_AVAILABILITY = YES_AGGRESSIVE;
				CLANG_WARN_UNREACHABLE_CODE = YES;
				CLANG_WARN__DUPLICATE_METHOD_MATCH = YES;
				COPY_PHASE_STRIP = NO;
				DEBUG_INFORMATION_FORMAT = dwarf;
				ENABLE_STRICT_OBJC_MSGSEND = YES;
				ENABLE_TESTABILITY = YES;
				"EXCLUDED_ARCHS[sdk=*]" = arm64;
				GCC_C_LANGUAGE_STANDARD = gnu11;
				GCC_DYNAMIC_NO_PIC = NO;
				GCC_NO_COMMON_BLOCKS = YES;
				GCC_OPTIMIZATION_LEVEL = 0;
				GCC_PREPROCESSOR_DEFINITIONS = (
					"DEBUG=1",
					"$(inherited)",
				);
				GCC_WARN_64_TO_32_BIT_CONVERSION = YES;
				GCC_WARN_ABOUT_RETURN_TYPE = YES_ERROR;
				GCC_WARN_UNDECLARED_SELECTOR = YES;
				GCC_WARN_UNINITIALIZED_AUTOS = YES_AGGRESSIVE;
				GCC_WARN_UNUSED_FUNCTION = YES;
				GCC_WARN_UNUSED_VARIABLE = YES;
				IPHONEOS_DEPLOYMENT_TARGET = 12.0;
				MTL_ENABLE_DEBUG_INFO = INCLUDE_SOURCE;
				MTL_FAST_MATH = YES;
				ONLY_ACTIVE_ARCH = YES;
				SDKROOT = iphoneos;
			};
			name = Debug;
		};
		57AB5AE2252762C30040DE8C /* Release */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
				ALWAYS_SEARCH_USER_PATHS = NO;
				CLANG_ANALYZER_NONNULL = YES;
				CLANG_ANALYZER_NUMBER_OBJECT_CONVERSION = YES_AGGRESSIVE;
				CLANG_CXX_LANGUAGE_STANDARD = "gnu++14";
				CLANG_CXX_LIBRARY = "libc++";
				CLANG_ENABLE_MODULES = YES;
				CLANG_ENABLE_OBJC_ARC = YES;
				CLANG_ENABLE_OBJC_WEAK = YES;
				CLANG_WARN_BLOCK_CAPTURE_AUTORELEASING = YES;
				CLANG_WARN_BOOL_CONVERSION = YES;
				CLANG_WARN_COMMA = YES;
				CLANG_WARN_CONSTANT_CONVERSION = YES;
				CLANG_WARN_DEPRECATED_OBJC_IMPLEMENTATIONS = YES;
				CLANG_WARN_DIRECT_OBJC_ISA_USAGE = YES_ERROR;
				CLANG_WARN_DOCUMENTATION_COMMENTS = YES;
				CLANG_WARN_EMPTY_BODY = YES;
				CLANG_WARN_ENUM_CONVERSION = YES;
				CLANG_WARN_INFINITE_RECURSION = YES;
				CLANG_WARN_INT_CONVERSION = YES;
				CLANG_WARN_NON_LITERAL_NULL_CONVERSION = YES;
				CLANG_WARN_OBJC_IMPLICIT_RETAIN_SELF = YES;
				CLANG_WARN_OBJC_LITERAL_CONVERSION = YES;
				CLANG_WARN_OBJC_ROOT_CLASS = YES_ERROR;
				CLANG_WARN_QUOTED_INCLUDE_IN_FRAMEWORK_HEADER = YES;
				CLANG_WARN_RANGE_LOOP_ANALYSIS = YES;
				CLANG_WARN_STRICT_PROTOTYPES = YES;
				CLANG_WARN_SUSPICIOUS_MOVE = YES;
				CLANG_WARN_UNGUARDED_AVAILABILITY = YES_AGGRESSIVE;
				CLANG_WARN_UNREACHABLE_CODE = YES;
				CLANG_WARN__DUPLICATE_METHOD_MATCH = YES;
				COPY_PHASE_STRIP = NO;
				DEBUG_INFORMATION_FORMAT = "dwarf-with-dsym";
				ENABLE_NS_ASSERTIONS = NO;
				ENABLE_STRICT_OBJC_MSGSEND = YES;
				GCC_C_LANGUAGE_STANDARD = gnu11;
				GCC_NO_COMMON_BLOCKS = YES;
				GCC_WARN_64_TO_32_BIT_CONVERSION = YES;
				GCC_WARN_ABOUT_RETURN_TYPE = YES_ERROR;
				GCC_WARN_UNDECLARED_SELECTOR = YES;
				GCC_WARN_UNINITIALIZED_AUTOS = YES_AGGRESSIVE;
				GCC_WARN_UNUSED_FUNCTION = YES;
				GCC_WARN_UNUSED_VARIABLE = YES;
				IPHONEOS_DEPLOYMENT_TARGET = 12.0;
				MTL_ENABLE_DEBUG_INFO = NO;
				MTL_FAST_MATH = YES;
				SDKROOT = iphoneos;
				VALIDATE_PRODUCT = YES;
			};
			name = Release;
		};
		57AB5AE4252762C30040DE8C /* Debug */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
				ASSETCATALOG_COMPILER_GLOBAL_ACCENT_COLOR_NAME = AccentColor;
				CODE_SIGN_STYLE = Automatic;
				INFOPLIST_FILE = "ios-src/Info.plist";
				IPHONEOS_DEPLOYMENT_TARGET = 12.0;
				LD_RUNPATH_SEARCH_PATHS = (
					"$(inherited)",
					"@executable_path/Frameworks",
				);
				LIBRARY_SEARCH_PATHS = target/universal/debug;
				OTHER_LDFLAGS = "-lcpal_ios_example";
				OTHER_LIBTOOLFLAGS = "";
				PRODUCT_BUNDLE_IDENTIFIER = "cpal.cpal-ios-example";
				PRODUCT_NAME = "$(TARGET_NAME)";
				TARGETED_DEVICE_FAMILY = "1,2";
			};
			name = Debug;
		};
		57AB5AE5252762C30040DE8C /* Release */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
				ASSETCATALOG_COMPILER_GLOBAL_ACCENT_COLOR_NAME = AccentColor;
				CODE_SIGN_STYLE = Automatic;
				INFOPLIST_FILE = "ios-src/Info.plist";
				IPHONEOS_DEPLOYMENT_TARGET = 12.0;
				LD_RUNPATH_SEARCH_PATHS = (
					"$(inherited)",
					"@executable_path/Frameworks",
				);
				LIBRARY_SEARCH_PATHS = target/universal/release;
				OTHER_LDFLAGS = "-lcpal_ios_example";
				OTHER_LIBTOOLFLAGS = "";
				PRODUCT_BUNDLE_IDENTIFIER = "cpal.cpal-ios-example";
				PRODUCT_NAME = "$(TARGET_NAME)";
				TARGETED_DEVICE_FAMILY = "1,2";
			};
			name = Release;
		};
		57AB5AEB252766240040DE8C /* Debug */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
				CODE_SIGN_STYLE = Automatic;
				DEBUGGING_SYMBOLS = YES;
				DEBUG_INFORMATION_FORMAT = dwarf;
				GCC_GENERATE_DEBUGGING_SYMBOLS = YES;
				GCC_OPTIMIZATION_LEVEL = 0;
				OTHER_CFLAGS = "";
				OTHER_LDFLAGS = "";
				PRODUCT_NAME = "$(TARGET_NAME)";
			};
			name = Debug;
		};
		57AB5AEC252766240040DE8C /* Release */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
				CODE_SIGN_STYLE = Automatic;
				DEBUG_INFORMATION_FORMAT = "dwarf-with-dsym";
				OTHER_CFLAGS = "";
				OTHER_LDFLAGS = "";
				PRODUCT_NAME = "$(TARGET_NAME)";
			};
			name = Release;
		};
/* End XCBuildConfiguration section */

/* Begin XCConfigurationList section */
		57AB5AC5252762C00040DE8C /* Build configuration list for PBXProject "cpal-ios-example" */ = {
			isa = XCConfigurationList;
			buildConfigurations = (
				57AB5AE1252762C30040DE8C /* Debug */,
				57AB5AE2252762C30040DE8C /* Release */,
			);
			defaultConfigurationIsVisible = 0;
			defaultConfigurationName = Release;
		};
		57AB5AE3252762C30040DE8C /* Build configuration list for PBXNativeTarget "cpal-ios-example" */ = {
			isa = XCConfigurationList;
			buildConfigurations = (
				57AB5AE4252762C30040DE8C /* Debug */,
				57AB5AE5252762C30040DE8C /* Release */,
			);
			defaultConfigurationIsVisible = 0;
			defaultConfigurationName = Release;
		};
		57AB5AEA252766240040DE8C /* Build configuration list for PBXLegacyTarget "cargo_ios" */ = {
			isa = XCConfigurationList;
			buildConfigurations = (
				57AB5AEB252766240040DE8C /* Debug */,
				57AB5AEC252766240040DE8C /* Release */,
			);
			defaultConfigurationIsVisible = 0;
			defaultConfigurationName = Release;
		};
/* End XCConfigurationList section */
	};
	rootObject = 57AB5AC2252762C00040DE8C /* Project object */;
}
```

## File: `examples/ios-feedback/cpal-ios-example.xcodeproj/project.xcworkspace/contents.xcworkspacedata`
```
<?xml version="1.0" encoding="UTF-8"?>
<Workspace
   version = "1.0">
   <FileRef
      location = "self:">
   </FileRef>
</Workspace>
```

## File: `examples/ios-feedback/cpal-ios-example.xcodeproj/project.xcworkspace/xcshareddata/IDEWorkspaceChecks.plist`
```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>IDEDidComputeMac32BitWarning</key>
	<true/>
</dict>
</plist>
```

## File: `examples/ios-feedback/cpal-ios-example.xcodeproj/xcuserdata/mikeh.xcuserdatad/xcschemes/xcschememanagement.plist`
```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>SchemeUserState</key>
	<dict>
		<key>cargo_ios.xcscheme_^#shared#^_</key>
		<dict>
			<key>orderHint</key>
			<integer>0</integer>
		</dict>
		<key>cpal-ios-example.xcscheme_^#shared#^_</key>
		<dict>
			<key>orderHint</key>
			<integer>1</integer>
		</dict>
	</dict>
</dict>
</plist>
```

## File: `examples/ios-feedback/ios-src/AppDelegate.h`
```c
//
//  AppDelegate.h
//  cpal-ios-example
//
//  Created by Michael Hills on 2/10/20.
//

#import <UIKit/UIKit.h>

@interface AppDelegate : UIResponder <UIApplicationDelegate>

@property (strong, nonatomic) UIWindow *window;

@end

```

## File: `examples/ios-feedback/ios-src/AppDelegate.m`
```
//
//  AppDelegate.m
//  cpal-ios-example
//
//  Created by Michael Hills on 2/10/20.
//

#import "AppDelegate.h"
@import AVFoundation;

void rust_ios_main(void);


@interface AppDelegate ()

@end

@implementation AppDelegate



- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
    // Override point for customization after application launch.

    // It is necessary to access the sharedInstance so that calls to AudioSessionGetProperty
    // will work.
    AVAudioSession *session = AVAudioSession.sharedInstance;
    // Setting up the category is not necessary, but generally advised.
    // Since this demo records and plays, lets use AVAudioSessionCategoryPlayAndRecord.
    // Also default to speaker as defaulting to the phone earpiece would be unusual.
    // Allowing bluetooth should direct audio to your bluetooth headset.
    NSError *categoryError = nil;
    BOOL isSetCategorySuccess = [session setCategory:AVAudioSessionCategoryPlayAndRecord
                                         withOptions:AVAudioSessionCategoryOptionDefaultToSpeaker | AVAudioSessionCategoryOptionAllowBluetooth
                                               error:&categoryError];
    if (isSetCategorySuccess) {
        NSError *activateError = nil;
        BOOL isActivateSuccess = [session setActive:YES error:&activateError];

        if (isActivateSuccess) {
            NSLog(@"Calling rust_ios_main()");
            rust_ios_main();
        } else {
            NSLog(@"Failed to activate audio session: %@", activateError);
        }
    } else {
        NSLog(@"Failed to set category: %@", categoryError);
    }

    return YES;
}

@end
```

## File: `examples/ios-feedback/ios-src/Info.plist`
```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>CFBundleDevelopmentRegion</key>
	<string>$(DEVELOPMENT_LANGUAGE)</string>
	<key>CFBundleExecutable</key>
	<string>$(EXECUTABLE_NAME)</string>
	<key>CFBundleIdentifier</key>
	<string>$(PRODUCT_BUNDLE_IDENTIFIER)</string>
	<key>CFBundleInfoDictionaryVersion</key>
	<string>6.0</string>
	<key>CFBundleName</key>
	<string>$(PRODUCT_NAME)</string>
	<key>CFBundlePackageType</key>
	<string>$(PRODUCT_BUNDLE_PACKAGE_TYPE)</string>
	<key>CFBundleShortVersionString</key>
	<string>1.0</string>
	<key>CFBundleVersion</key>
	<string>1</string>
	<key>LSRequiresIPhoneOS</key>
	<true/>
	<key>UIApplicationSupportsIndirectInputEvents</key>
	<true/>
	<key>UILaunchStoryboardName</key>
	<string>LaunchScreen</string>
	<key>UIMainStoryboardFile</key>
	<string>Main</string>
	<key>UIRequiredDeviceCapabilities</key>
	<array>
		<string>armv7</string>
	</array>
	<key>UISupportedInterfaceOrientations</key>
	<array>
		<string>UIInterfaceOrientationPortrait</string>
		<string>UIInterfaceOrientationLandscapeLeft</string>
		<string>UIInterfaceOrientationLandscapeRight</string>
	</array>
	<key>NSMicrophoneUsageDescription</key>
	<string>cpal feedback demo</string>
	<key>UISupportedInterfaceOrientations~ipad</key>
	<array>
		<string>UIInterfaceOrientationPortrait</string>
		<string>UIInterfaceOrientationPortraitUpsideDown</string>
		<string>UIInterfaceOrientationLandscapeLeft</string>
		<string>UIInterfaceOrientationLandscapeRight</string>
	</array>
</dict>
</plist>
```

## File: `examples/ios-feedback/ios-src/ViewController.h`
```c
//
//  ViewController.h
//  cpal-ios-example
//
//  Created by Michael Hills on 2/10/20.
//

#import <UIKit/UIKit.h>

@interface ViewController : UIViewController


@end

```

## File: `examples/ios-feedback/ios-src/ViewController.m`
```
//
//  ViewController.m
//  cpal-ios-example
//
//  Created by Michael Hills on 2/10/20.
//

#import "ViewController.h"

@interface ViewController ()

@end

@implementation ViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    // Do any additional setup after loading the view.
}


@end
```

## File: `examples/ios-feedback/ios-src/main.m`
```
//
//  main.m
//  cpal-ios-example
//
//  Created by Michael Hills on 2/10/20.
//

#import <UIKit/UIKit.h>
#import "AppDelegate.h"

int main(int argc, char * argv[]) {
    NSString * appDelegateClassName;
    @autoreleasepool {
        // Setup code that might create autoreleased objects goes here.
        appDelegateClassName = NSStringFromClass([AppDelegate class]);
    }
    return UIApplicationMain(argc, argv, nil, appDelegateClassName);
}
```

## File: `examples/ios-feedback/ios-src/Base.lproj/LaunchScreen.storyboard`
```
<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<document type="com.apple.InterfaceBuilder3.CocoaTouch.Storyboard.XIB" version="3.0" toolsVersion="13122.16" targetRuntime="iOS.CocoaTouch" propertyAccessControl="none" useAutolayout="YES" launchScreen="YES" useTraitCollections="YES" useSafeAreas="YES" colorMatched="YES" initialViewController="01J-lp-oVM">
    <dependencies>
        <plugIn identifier="com.apple.InterfaceBuilder.IBCocoaTouchPlugin" version="13104.12"/>
        <capability name="Safe area layout guides" minToolsVersion="9.0"/>
        <capability name="documents saved in the Xcode 8 format" minToolsVersion="8.0"/>
    </dependencies>
    <scenes>
        <!--View Controller-->
        <scene sceneID="EHf-IW-A2E">
            <objects>
                <viewController id="01J-lp-oVM" sceneMemberID="viewController">
                    <view key="view" contentMode="scaleToFill" id="Ze5-6b-2t3">
                        <rect key="frame" x="0.0" y="0.0" width="375" height="667"/>
                        <autoresizingMask key="autoresizingMask" widthSizable="YES" heightSizable="YES"/>
                        <color key="backgroundColor" xcode11CocoaTouchSystemColor="systemBackgroundColor" cocoaTouchSystemColor="whiteColor"/>
                        <viewLayoutGuide key="safeArea" id="6Tk-OE-BBY"/>
                    </view>
                </viewController>
                <placeholder placeholderIdentifier="IBFirstResponder" id="iYj-Kq-Ea1" userLabel="First Responder" sceneMemberID="firstResponder"/>
            </objects>
            <point key="canvasLocation" x="53" y="375"/>
        </scene>
    </scenes>
</document>
```

## File: `examples/ios-feedback/ios-src/Base.lproj/Main.storyboard`
```
<?xml version="1.0" encoding="UTF-8"?>
<document type="com.apple.InterfaceBuilder3.CocoaTouch.Storyboard.XIB" version="3.0" toolsVersion="13122.16" targetRuntime="iOS.CocoaTouch" propertyAccessControl="none" useAutolayout="YES" useTraitCollections="YES" useSafeAreas="YES" colorMatched="YES" initialViewController="BYZ-38-t0r">
    <dependencies>
        <plugIn identifier="com.apple.InterfaceBuilder.IBCocoaTouchPlugin" version="13104.12"/>
        <capability name="Safe area layout guides" minToolsVersion="9.0"/>
        <capability name="documents saved in the Xcode 8 format" minToolsVersion="8.0"/>
    </dependencies>
    <scenes>
        <!--View Controller-->
        <scene sceneID="tne-QT-ifu">
            <objects>
                <viewController id="BYZ-38-t0r" customClass="ViewController" customModuleProvider="" sceneMemberID="viewController">
                    <view key="view" contentMode="scaleToFill" id="8bC-Xf-vdC">
                        <rect key="frame" x="0.0" y="0.0" width="375" height="667"/>
                        <autoresizingMask key="autoresizingMask" widthSizable="YES" heightSizable="YES"/>
                        <color key="backgroundColor" xcode11CocoaTouchSystemColor="systemBackgroundColor" cocoaTouchSystemColor="whiteColor"/>
                        <viewLayoutGuide key="safeArea" id="6Tk-OE-BBY"/>
                    </view>
                </viewController>
                <placeholder placeholderIdentifier="IBFirstResponder" id="dkx-z0-nzr" sceneMemberID="firstResponder"/>
            </objects>
        </scene>
    </scenes>
</document>
```

## File: `examples/ios-feedback/src/feedback.rs`
```rust
//! Feeds back the input stream directly into the output stream.
//!
//! Assumes that the input and output devices can use the same stream configuration and that they
//! support the f32 sample format.
//!
//! Uses a delay of `LATENCY_MS` milliseconds in case the default input and output streams are not
//! precisely synchronised.

extern crate anyhow;
extern crate cpal;
extern crate ringbuf;

use cpal::traits::{DeviceTrait, HostTrait, StreamTrait};
use ringbuf::{
    traits::{Consumer, Producer, Split},
    HeapRb,
};

const LATENCY_MS: f32 = 1000.0;

pub fn run_example() -> Result<(), anyhow::Error> {
    let host = cpal::default_host();

    // Default devices.
    let input_device = host
        .default_input_device()
        .expect("failed to get default input device");
    let output_device = host
        .default_output_device()
        .expect("failed to get default output device");
    println!("Using default input device: \"{}\"", input_device.name()?);
    println!("Using default output device: \"{}\"", output_device.name()?);

    // We'll try and use the same configuration between streams to keep it simple.
    let config: cpal::StreamConfig = input_device.default_input_config()?.into();

    // Create a delay in case the input and output devices aren't synced.
    let latency_frames = (LATENCY_MS / 1_000.0) * config.sample_rate as f32;
    let latency_samples = latency_frames as usize * config.channels as usize;

    // The buffer to share samples
    let ring = HeapRb::<f32>::new(latency_samples * 2);
    let (mut producer, mut consumer) = ring.split();

    // Fill the samples with 0.0 equal to the length of the delay.
    for _ in 0..latency_samples {
        // The ring buffer has twice as much space as necessary to add latency here,
        // so this should never fail
        producer.try_push(0.0).unwrap();
    }

    let input_data_fn = move |data: &[f32], _: &cpal::InputCallbackInfo| {
        let mut output_fell_behind = false;
        for &sample in data {
            if producer.try_push(sample).is_err() {
                output_fell_behind = true;
            }
        }
        if output_fell_behind {
            eprintln!("output stream fell behind: try increasing latency");
        }
    };

    let output_data_fn = move |data: &mut [f32], _: &cpal::OutputCallbackInfo| {
        let mut input_fell_behind = false;
        for sample in data {
            *sample = match consumer.try_pop() {
                Some(s) => s,
                None => {
                    input_fell_behind = true;
                    0.0
                }
            };
        }
        if input_fell_behind {
            eprintln!("input stream fell behind: try increasing latency");
        }
    };

    // Build streams.
    println!(
        "Attempting to build both streams with f32 samples and `{:?}`.",
        config
    );
    println!("Setup input stream");
    let input_stream = input_device.build_input_stream(config, input_data_fn, err_fn, None)?;
    println!("Setup output stream");
    let output_stream = output_device.build_output_stream(config, output_data_fn, err_fn, None)?;
    println!("Successfully built streams.");

    // Play the streams.
    println!(
        "Starting the input and output streams with `{}` milliseconds of latency.",
        LATENCY_MS
    );
    input_stream.play()?;
    output_stream.play()?;

    // for the purposes of this demo, leak these so that after returning the audio units will
    // keep running
    std::mem::forget(input_stream);
    std::mem::forget(output_stream);
    Ok(())
}

fn err_fn(err: cpal::StreamError) {
    eprintln!("an error occurred on stream: {}", err);
}
```

## File: `examples/ios-feedback/src/lib.rs`
```rust
mod feedback;

#[no_mangle]
pub extern "C" fn rust_ios_main() {
    feedback::run_example().unwrap();
}
```

## File: `examples/wasm-beep/.gitignore`
```
Cargo.lock
/dist
/target
```

## File: `examples/wasm-beep/Cargo.toml`
```
[package]
name = "wasm-beep"
description = "cpal beep example for WebAssembly"
version = "0.1.0"
edition = "2021"
rust-version = "1.85"

[lib]
crate-type = ["cdylib"]

[profile.release]
# This makes the compiled code faster and smaller, but it makes compiling slower,
# so it's only enabled in release mode.
lto = true

[dependencies]
cpal = { path = "../..", features = ["wasm-bindgen"] }

# `gloo` is a utility crate which improves ergonomics over direct `web-sys` usage.
gloo = "0.11"

# The `wasm-bindgen` crate provides the bare minimum functionality needed
# to interact with JavaScript.
wasm-bindgen = "0.2"

# The `console_error_panic_hook` crate provides better debugging of panics by
# logging them with `console.error`.
console_error_panic_hook = "0.1"

# The `web-sys` crate allows you to interact with the various browser APIs,
# like the DOM.
[dependencies.web-sys]
version = "0.3"
features = ["console", "MouseEvent"]
```

## File: `examples/wasm-beep/README.md`
```markdown
## How to install

[trunk](https://trunkrs.dev/) is used to build and serve the example.
```sh
cargo install --locked trunk
# -- or --
cargo binstall trunk
```

## How to run in debug mode

```sh
# Builds the project and opens it in a new browser tab. Auto-reloads when the project changes.
trunk serve --open
```

## How to build in release mode

```sh
# Builds the project in release mode and places it into the `dist` folder.
trunk build --release
```

## What does each file do?

* `Cargo.toml` contains the standard Rust metadata. You put your Rust dependencies in here. You must change this file with your details (name, description, version, authors, categories)

* The `src` folder contains your Rust code.
```

## File: `examples/wasm-beep/index.html`
```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <title>cpal beep example</title>
  </head>
  <body>
    <input id="play" type="button" value="beep"/>
    <input id="stop" type="button" value="stop"/>
  </body>
</html>
```

## File: `examples/wasm-beep/src/lib.rs`
```rust
use std::{cell::Cell, rc::Rc};

use cpal::{
    traits::{DeviceTrait, HostTrait, StreamTrait},
    Stream,
};
use wasm_bindgen::prelude::*;
use web_sys::console;

// This is like the `main` function, except for JavaScript.
#[wasm_bindgen(start)]
pub fn main_js() -> Result<(), JsValue> {
    // This provides better error messages in debug mode.
    // It's disabled in release mode, so it doesn't bloat up the file size.
    #[cfg(debug_assertions)]
    console_error_panic_hook::set_once();

    let document = gloo::utils::document();
    let play_button = document.get_element_by_id("play").unwrap();
    let stop_button = document.get_element_by_id("stop").unwrap();

    // stream needs to be referenced from the "play" and "stop" closures
    let stream = Rc::new(Cell::new(None));

    // set up play button
    {
        let stream = stream.clone();
        let closure = Closure::<dyn FnMut(_)>::new(move |_event: web_sys::MouseEvent| {
            stream.set(Some(beep()));
        });
        play_button
            .add_event_listener_with_callback("mousedown", closure.as_ref().unchecked_ref())?;
        closure.forget();
    }

    // set up stop button
    {
        let closure = Closure::<dyn FnMut(_)>::new(move |_event: web_sys::MouseEvent| {
            // stop the stream by dropping it
            stream.take();
        });
        stop_button
            .add_event_listener_with_callback("mousedown", closure.as_ref().unchecked_ref())?;
        closure.forget();
    }

    Ok(())
}

fn beep() -> Stream {
    let host = cpal::default_host();
    let device = host
        .default_output_device()
        .expect("failed to find a default output device");
    let config = device.default_output_config().unwrap();

    match config.sample_format() {
        cpal::SampleFormat::F32 => run::<f32>(&device, config.into()),
        cpal::SampleFormat::I16 => run::<i16>(&device, config.into()),
        cpal::SampleFormat::U16 => run::<u16>(&device, config.into()),
        _ => panic!("unsupported sample format"),
    }
}

fn run<T>(device: &cpal::Device, config: cpal::StreamConfig) -> Stream
where
    T: cpal::Sample + cpal::SizedSample + cpal::FromSample<f32>,
{
    let sample_rate = config.sample_rate as f32;
    let channels = config.channels as usize;

    // Produce a sinusoid of maximum amplitude.
    let mut sample_clock = 0f32;
    let mut next_value = move || {
        sample_clock = (sample_clock + 1.0) % sample_rate;
        (sample_clock * 440.0 * 2.0 * 3.141592 / sample_rate).sin()
    };

    let err_fn = |err| console::error_1(&format!("an error occurred on stream: {}", err).into());

    let stream = device
        .build_output_stream(
            config,
            move |data: &mut [T], _| write_data(data, channels, &mut next_value),
            err_fn,
            None,
        )
        .unwrap();
    stream.play().unwrap();
    stream
}

fn write_data<T>(output: &mut [T], channels: usize, next_sample: &mut dyn FnMut() -> f32)
where
    T: cpal::Sample + cpal::FromSample<f32>,
{
    for frame in output.chunks_mut(channels) {
        let sample = next_sample();
        let value = T::from_sample::<f32>(sample);
        for sample in frame.iter_mut() {
            *sample = value;
        }
    }
}
```

## File: `src/device_description.rs`
```rust
//! Device metadata and description types.
//!
//! This module provides structured information about audio devices including manufacturer,
//! device type, interface type, and connection details. Not all backends provide complete
//! information - availability depends on platform capabilities.

use std::fmt;

use crate::ChannelCount;

/// Describes an audio device with structured metadata.
///
/// This type provides structured information about an audio device beyond just its name.
/// Availability depends on the host implementation and platform capabilities.
#[derive(Debug, Clone, PartialEq, Eq)]
pub struct DeviceDescription {
    /// Human-readable device name
    name: String,

    /// Device manufacturer or vendor name
    manufacturer: Option<String>,

    /// Driver name
    driver: Option<String>,

    /// Categorization of device type
    device_type: DeviceType,

    /// Connection/interface type
    interface_type: InterfaceType,

    /// Direction: input, output, or duplex
    direction: DeviceDirection,

    /// Physical address or connection identifier
    address: Option<String>,

    /// Additional description lines with non-structured, detailed information.
    extended: Vec<String>,
}

/// Categorization of audio device types.
///
/// This describes the kind of audio device (speaker, microphone, headset, etc.)
/// regardless of how it connects to the system.
#[derive(Debug, Clone, Copy, PartialEq, Eq, Hash, Default)]
#[non_exhaustive]
pub enum DeviceType {
    /// Speaker (built-in or external)
    Speaker,

    /// Microphone (built-in or external)
    Microphone,

    /// Headphones (audio output only)
    Headphones,

    /// Headset (combined headphones + microphone)
    Headset,

    /// Earpiece (phone-style speaker, typically for voice calls)
    Earpiece,

    /// Handset (telephone-style handset with speaker and microphone)
    Handset,

    /// Hearing aid device
    HearingAid,

    /// Docking station audio
    Dock,

    /// Radio/TV tuner
    Tuner,

    /// Virtual/loopback device (software audio routing)
    Virtual,

    /// Unknown or unclassified device type
    #[default]
    Unknown,
}

/// How the device connects to the system (interface/connection type).
///
/// This describes the physical or logical connection between the audio device
/// and the computer system.
#[derive(Debug, Clone, Copy, PartialEq, Eq, Hash, Default)]
#[non_exhaustive]
pub enum InterfaceType {
    /// Built-in to the system (integrated audio chipset)
    BuiltIn,

    /// USB connection
    Usb,

    /// Bluetooth wireless connection
    Bluetooth,

    /// PCI or PCIe card (internal sound card)
    Pci,

    /// FireWire connection (IEEE 1394)
    FireWire,

    /// Thunderbolt connection
    Thunderbolt,

    /// HDMI connection
    Hdmi,

    /// Line-level analog connection (line in/out, aux)
    Line,

    /// S/PDIF digital audio interface
    Spdif,

    /// Network connection (Dante, AVB, AirPlay, IP audio, etc.)
    Network,

    /// Virtual/loopback connection (software audio routing, not physical hardware)
    Virtual,

    /// DisplayPort audio
    DisplayPort,

    /// Aggregate device (combines multiple devices)
    Aggregate,

    /// Unknown connection type
    #[default]
    Unknown,
}

/// The direction(s) that a device supports.
#[derive(Debug, Clone, Copy, PartialEq, Eq, Hash, Default)]
#[non_exhaustive]
pub enum DeviceDirection {
    /// Input only (capture/recording)
    Input,

    /// Output only (playback/rendering)
    Output,

    /// Both input and output
    Duplex,

    /// Direction unknown or not yet determined
    #[default]
    Unknown,
}

impl DeviceDescription {
    /// Returns the human-readable device name.
    ///
    /// This is always available and is the primary user-facing identifier.
    pub fn name(&self) -> &str {
        &self.name
    }

    /// Returns the manufacturer/vendor name if available.
    pub fn manufacturer(&self) -> Option<&str> {
        self.manufacturer.as_deref()
    }

    /// Returns the driver name if available.
    pub fn driver(&self) -> Option<&str> {
        self.driver.as_deref()
    }

    /// Returns the device type categorization.
    pub fn device_type(&self) -> DeviceType {
        self.device_type
    }

    /// Returns the interface/connection type.
    pub fn interface_type(&self) -> InterfaceType {
        self.interface_type
    }

    /// Returns the device direction.
    pub fn direction(&self) -> DeviceDirection {
        self.direction
    }

    /// Returns whether this device supports audio input (capture).
    ///
    /// This is a convenience method that checks if direction is `Input` or `Duplex`.
    pub fn supports_input(&self) -> bool {
        matches!(
            self.direction,
            DeviceDirection::Input | DeviceDirection::Duplex
        )
    }

    /// Returns whether this device supports audio output (playback).
    ///
    /// This is a convenience method that checks if direction is `Output` or `Duplex`.
    pub fn supports_output(&self) -> bool {
        matches!(
            self.direction,
            DeviceDirection::Output | DeviceDirection::Duplex
        )
    }

    /// Returns the physical address or connection identifier if available.
    pub fn address(&self) -> Option<&str> {
        self.address.as_deref()
    }

    /// Returns additional description lines with detailed information.
    pub fn extended(&self) -> &[String] {
        &self.extended
    }
}

impl fmt::Display for DeviceDescription {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(f, "{}", self.name)?;

        if let Some(mfr) = &self.manufacturer {
            write!(f, " ({})", mfr)?;
        }

        if self.device_type != DeviceType::Unknown {
            write!(f, " [{}]", self.device_type)?;
        }

        if self.interface_type != InterfaceType::Unknown {
            write!(f, " via {}", self.interface_type)?;
        }

        Ok(())
    }
}

impl fmt::Display for DeviceType {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        match self {
            DeviceType::Speaker => write!(f, "Speaker"),
            DeviceType::Microphone => write!(f, "Microphone"),
            DeviceType::Headphones => write!(f, "Headphones"),
            DeviceType::Headset => write!(f, "Headset"),
            DeviceType::Earpiece => write!(f, "Earpiece"),
            DeviceType::Handset => write!(f, "Handset"),
            DeviceType::HearingAid => write!(f, "Hearing Aid"),
            DeviceType::Dock => write!(f, "Dock"),
            DeviceType::Tuner => write!(f, "Tuner"),
            DeviceType::Virtual => write!(f, "Virtual"),
            _ => write!(f, "Unknown"),
        }
    }
}

impl fmt::Display for InterfaceType {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        match self {
            InterfaceType::BuiltIn => write!(f, "Built-in"),
            InterfaceType::Usb => write!(f, "USB"),
            InterfaceType::Bluetooth => write!(f, "Bluetooth"),
            InterfaceType::Pci => write!(f, "PCI"),
            InterfaceType::FireWire => write!(f, "FireWire"),
            InterfaceType::Thunderbolt => write!(f, "Thunderbolt"),
            InterfaceType::Hdmi => write!(f, "HDMI"),
            InterfaceType::Line => write!(f, "Line"),
            InterfaceType::Spdif => write!(f, "S/PDIF"),
            InterfaceType::Network => write!(f, "Network"),
            InterfaceType::Virtual => write!(f, "Virtual"),
            InterfaceType::DisplayPort => write!(f, "DisplayPort"),
            InterfaceType::Aggregate => write!(f, "Aggregate"),
            _ => write!(f, "Unknown"),
        }
    }
}

impl fmt::Display for DeviceDirection {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        match self {
            DeviceDirection::Input => write!(f, "Input"),
            DeviceDirection::Output => write!(f, "Output"),
            DeviceDirection::Duplex => write!(f, "Duplex"),
            _ => write!(f, "Unknown"),
        }
    }
}

/// Builder for constructing a `DeviceDescription`.
///
/// This is primarily used by host implementations and custom hosts
/// to gradually build up device descriptions with available metadata.
#[derive(Debug, Clone)]
pub struct DeviceDescriptionBuilder {
    name: String,
    manufacturer: Option<String>,
    driver: Option<String>,
    device_type: DeviceType,
    interface_type: InterfaceType,
    direction: DeviceDirection,
    address: Option<String>,
    extended: Vec<String>,
}

impl DeviceDescriptionBuilder {
    /// Creates a new builder with the device name (required).
    pub fn new(name: impl Into<String>) -> Self {
        Self {
            name: name.into(),
            manufacturer: None,
            driver: None,
            device_type: DeviceType::default(),
            interface_type: InterfaceType::default(),
            direction: DeviceDirection::default(),
            address: None,
            extended: Vec::new(),
        }
    }

    /// Sets the manufacturer name.
    pub fn manufacturer(mut self, manufacturer: impl Into<String>) -> Self {
        self.manufacturer = Some(manufacturer.into());
        self
    }

    /// Sets the driver name.
    pub fn driver(mut self, driver: impl Into<String>) -> Self {
        self.driver = Some(driver.into());
        self
    }

    /// Sets the device type.
    pub fn device_type(mut self, device_type: DeviceType) -> Self {
        self.device_type = device_type;
        self
    }

    /// Sets the interface type.
    pub fn interface_type(mut self, interface_type: InterfaceType) -> Self {
        self.interface_type = interface_type;
        self
    }

    /// Sets the device direction.
    pub fn direction(mut self, direction: DeviceDirection) -> Self {
        self.direction = direction;
        self
    }

    /// Sets the physical address.
    pub fn address(mut self, address: impl Into<String>) -> Self {
        self.address = Some(address.into());
        self
    }

    /// Sets the description lines.
    pub fn extended(mut self, lines: Vec<String>) -> Self {
        self.extended = lines;
        self
    }

    /// Adds a single description line.
    pub fn add_extended_line(mut self, line: impl Into<String>) -> Self {
        self.extended.push(line.into());
        self
    }

    /// Builds the [`DeviceDescription`].
    pub fn build(self) -> DeviceDescription {
        DeviceDescription {
            name: self.name,
            manufacturer: self.manufacturer,
            driver: self.driver,
            device_type: self.device_type,
            interface_type: self.interface_type,
            direction: self.direction,
            address: self.address,
            extended: self.extended,
        }
    }
}

/// Determines device direction from input/output capabilities.
pub(crate) fn direction_from_caps(has_input: bool, has_output: bool) -> DeviceDirection {
    match (has_input, has_output) {
        (true, true) => DeviceDirection::Duplex,
        (true, false) => DeviceDirection::Input,
        (false, true) => DeviceDirection::Output,
        (false, false) => DeviceDirection::Unknown,
    }
}

/// Determines device direction from input/output channel counts.
#[allow(dead_code)]
pub(crate) fn direction_from_counts(
    input_channels: Option<ChannelCount>,
    output_channels: Option<ChannelCount>,
) -> DeviceDirection {
    let has_input = input_channels.map(|n| n > 0).unwrap_or(false);
    let has_output = output_channels.map(|n| n > 0).unwrap_or(false);
    direction_from_caps(has_input, has_output)
}
```

## File: `src/error.rs`
```rust
use std::error::Error;
use std::fmt::{Display, Formatter};

/// The requested host, although supported on this platform, is unavailable.
#[derive(Copy, Clone, Debug, PartialEq, Eq, Hash)]
pub struct HostUnavailable;

impl Display for HostUnavailable {
    fn fmt(&self, f: &mut Formatter<'_>) -> std::fmt::Result {
        f.write_str("the requested host is unavailable")
    }
}

impl Error for HostUnavailable {}

/// Some error has occurred that is specific to the backend from which it was produced.
///
/// This error is often used as a catch-all in cases where:
///
/// - It is unclear exactly what error might be produced by the backend API.
/// - It does not make sense to add a variant to the enclosing error type.
/// - No error was expected to occur at all, but we return an error to avoid the possibility of a
///   `panic!` caused by some unforeseen or unknown reason.
///
/// **Note:** If you notice a `BackendSpecificError` that you believe could be better handled in a
/// cross-platform manner, please create an issue at <https://github.com/RustAudio/cpal/issues>
/// with details about your use case, the backend you're using, and the error message. Or submit
/// a pull request with a patch that adds the necessary error variant to the appropriate error enum.
#[derive(Clone, Debug, PartialEq, Eq, Hash)]
pub struct BackendSpecificError {
    pub description: String,
}

impl Display for BackendSpecificError {
    fn fmt(&self, f: &mut Formatter<'_>) -> std::fmt::Result {
        write!(
            f,
            "A backend-specific error has occurred: {}",
            self.description
        )
    }
}

impl Error for BackendSpecificError {}

/// An error that might occur while attempting to enumerate the available devices on a system.
#[derive(Clone, Debug, PartialEq, Eq, Hash)]
#[non_exhaustive]
pub enum DevicesError {
    /// See the [`BackendSpecificError`] docs for more information about this error variant.
    BackendSpecific { err: BackendSpecificError },
}

impl Display for DevicesError {
    fn fmt(&self, f: &mut Formatter<'_>) -> std::fmt::Result {
        match self {
            Self::BackendSpecific { err } => err.fmt(f),
        }
    }
}

impl Error for DevicesError {}

impl From<BackendSpecificError> for DevicesError {
    fn from(err: BackendSpecificError) -> Self {
        Self::BackendSpecific { err }
    }
}

/// An error that may occur while attempting to retrieve a device ID.
#[derive(Clone, Debug, Eq, PartialEq)]
#[non_exhaustive]
pub enum DeviceIdError {
    /// See the [`BackendSpecificError`] docs for more information about this error variant.
    BackendSpecific {
        err: BackendSpecificError,
    },
    UnsupportedPlatform,
}

impl Display for DeviceIdError {
    fn fmt(&self, f: &mut Formatter<'_>) -> std::fmt::Result {
        match self {
            Self::BackendSpecific { err } => err.fmt(f),
            Self::UnsupportedPlatform => f.write_str("Device IDs are unsupported for this OS"),
        }
    }
}

impl Error for DeviceIdError {}

impl From<BackendSpecificError> for DeviceIdError {
    fn from(err: BackendSpecificError) -> Self {
        Self::BackendSpecific { err }
    }
}

/// An error that may occur while attempting to retrieve a device name.
#[derive(Clone, Debug, PartialEq, Eq, Hash)]
#[non_exhaustive]
pub enum DeviceNameError {
    /// See the [`BackendSpecificError`] docs for more information about this error variant.
    BackendSpecific { err: BackendSpecificError },
}

impl Display for DeviceNameError {
    fn fmt(&self, f: &mut Formatter<'_>) -> std::fmt::Result {
        match self {
            Self::BackendSpecific { err } => err.fmt(f),
        }
    }
}

impl Error for DeviceNameError {}

impl From<BackendSpecificError> for DeviceNameError {
    fn from(err: BackendSpecificError) -> Self {
        Self::BackendSpecific { err }
    }
}

/// Error that can happen when enumerating the list of supported formats.
#[derive(Clone, Debug, PartialEq, Eq, Hash)]
#[non_exhaustive]
pub enum SupportedStreamConfigsError {
    /// The device no longer exists. This can happen if the device is disconnected while the
    /// program is running.
    DeviceNotAvailable,
    /// The device is temporarily busy. This can happen when another application or stream
    /// is using the device. Retrying may succeed.
    DeviceBusy,
    /// We called something the C-Layer did not understand
    InvalidArgument,
    /// See the [`BackendSpecificError`] docs for more information about this error variant.
    BackendSpecific { err: BackendSpecificError },
}

impl Display for SupportedStreamConfigsError {
    fn fmt(&self, f: &mut Formatter<'_>) -> std::fmt::Result {
        match self {
            Self::BackendSpecific { err } => err.fmt(f),
            Self::DeviceNotAvailable => f.write_str("The requested device is no longer available. For example, it has been unplugged."),
            Self::DeviceBusy => f.write_str("The requested device is temporarily busy. Another application or stream may be using it."),
            Self::InvalidArgument => f.write_str("Invalid argument passed to the backend. For example, this happens when trying to read capture capabilities when the device does not support it.")
        }
    }
}

impl Error for SupportedStreamConfigsError {}

impl From<BackendSpecificError> for SupportedStreamConfigsError {
    fn from(err: BackendSpecificError) -> Self {
        Self::BackendSpecific { err }
    }
}

/// May occur when attempting to request the default input or output stream format from a [`Device`](crate::Device).
#[derive(Clone, Debug, PartialEq, Eq, Hash)]
#[non_exhaustive]
pub enum DefaultStreamConfigError {
    /// The device no longer exists. This can happen if the device is disconnected while the
    /// program is running.
    DeviceNotAvailable,
    /// The device is temporarily busy. This can happen when another application or stream
    /// is using the device. Retrying after a short delay may succeed.
    DeviceBusy,
    /// Returned if e.g. the default input format was requested on an output-only audio device.
    StreamTypeNotSupported,
    /// See the [`BackendSpecificError`] docs for more information about this error variant.
    BackendSpecific { err: BackendSpecificError },
}

impl Display for DefaultStreamConfigError {
    fn fmt(&self, f: &mut Formatter<'_>) -> std::fmt::Result {
        match self {
            Self::BackendSpecific { err } => err.fmt(f),
            Self::DeviceNotAvailable => f.write_str(
                "The requested device is no longer available. For example, it has been unplugged.",
            ),
            Self::DeviceBusy => f.write_str(
                "The requested device is temporarily busy. Another application or stream may be using it.",
            ),
            Self::StreamTypeNotSupported => {
                f.write_str("The requested stream type is not supported by the device.")
            }
        }
    }
}

impl Error for DefaultStreamConfigError {}

impl From<BackendSpecificError> for DefaultStreamConfigError {
    fn from(err: BackendSpecificError) -> Self {
        Self::BackendSpecific { err }
    }
}
/// Error that can happen when creating a [`Stream`](crate::Stream).
#[derive(Clone, Debug, PartialEq, Eq, Hash)]
#[non_exhaustive]
pub enum BuildStreamError {
    /// The device no longer exists. This can happen if the device is disconnected while the
    /// program is running.
    DeviceNotAvailable,
    /// The device is temporarily busy. This can happen when another application or stream
    /// is using the device. Retrying may succeed.
    DeviceBusy,
    /// The specified stream configuration is not supported.
    StreamConfigNotSupported,
    /// We called something the C-Layer did not understand
    ///
    /// On ALSA device functions called with a feature they do not support will yield this. E.g.
    /// Trying to use capture capabilities on an output only format yields this.
    InvalidArgument,
    /// Occurs if adding a new Stream ID would cause an integer overflow.
    StreamIdOverflow,
    /// See the [`BackendSpecificError`] docs for more information about this error variant.
    BackendSpecific { err: BackendSpecificError },
}

impl Display for BuildStreamError {
    fn fmt(&self, f: &mut Formatter<'_>) -> std::fmt::Result {
        match self {
            Self::BackendSpecific { err } => err.fmt(f),
            Self::DeviceNotAvailable => f.write_str(
                "The requested device is no longer available. For example, it has been unplugged.",
            ),
            Self::DeviceBusy => f.write_str(
                "The requested device is temporarily busy. Another application or stream may be using it.",
            ),
            Self::StreamConfigNotSupported => {
                f.write_str("The requested stream configuration is not supported by the device.")
            }
            Self::InvalidArgument => f.write_str(
                "The requested device does not support this capability (invalid argument)",
            ),
            Self::StreamIdOverflow => f.write_str("Adding a new stream ID would cause an overflow"),
        }
    }
}

impl Error for BuildStreamError {}

impl From<BackendSpecificError> for BuildStreamError {
    fn from(err: BackendSpecificError) -> Self {
        Self::BackendSpecific { err }
    }
}

/// Errors that might occur when calling [`Stream::play()`](crate::traits::StreamTrait::play).
///
/// As of writing this, only macOS may immediately return an error while calling this method. This
/// is because both the alsa and wasapi backends only enqueue these commands and do not process
/// them immediately.
#[derive(Clone, Debug, PartialEq, Eq, Hash)]
#[non_exhaustive]
pub enum PlayStreamError {
    /// The device associated with the stream is no longer available.
    DeviceNotAvailable,
    /// See the [`BackendSpecificError`] docs for more information about this error variant.
    BackendSpecific { err: BackendSpecificError },
}

impl Display for PlayStreamError {
    fn fmt(&self, f: &mut Formatter<'_>) -> std::fmt::Result {
        match self {
            Self::BackendSpecific { err } => err.fmt(f),
            Self::DeviceNotAvailable => {
                f.write_str("the device associated with the stream is no longer available")
            }
        }
    }
}

impl Error for PlayStreamError {}

impl From<BackendSpecificError> for PlayStreamError {
    fn from(err: BackendSpecificError) -> Self {
        Self::BackendSpecific { err }
    }
}

/// Errors that might occur when calling [`Stream::pause()`](crate::traits::StreamTrait::pause).
///
/// As of writing this, only macOS may immediately return an error while calling this method. This
/// is because both the alsa and wasapi backends only enqueue these commands and do not process
/// them immediately.
#[derive(Clone, Debug, PartialEq, Eq, Hash)]
#[non_exhaustive]
pub enum PauseStreamError {
    /// The device associated with the stream is no longer available.
    DeviceNotAvailable,
    /// See the [`BackendSpecificError`] docs for more information about this error variant.
    BackendSpecific { err: BackendSpecificError },
}

impl Display for PauseStreamError {
    fn fmt(&self, f: &mut Formatter<'_>) -> std::fmt::Result {
        match self {
            Self::BackendSpecific { err } => err.fmt(f),
            Self::DeviceNotAvailable => {
                f.write_str("the device associated with the stream is no longer available")
            }
        }
    }
}

impl Error for PauseStreamError {}

impl From<BackendSpecificError> for PauseStreamError {
    fn from(err: BackendSpecificError) -> Self {
        Self::BackendSpecific { err }
    }
}

/// Errors that might occur while a stream is running.
#[derive(Clone, Debug, PartialEq, Eq, Hash)]
#[non_exhaustive]
pub enum StreamError {
    /// The device no longer exists. This can happen if the device is disconnected while the
    /// program is running.
    DeviceNotAvailable,

    /// The stream configuration is no longer valid and must be rebuilt.
    StreamInvalidated,

    /// Buffer underrun or overrun occurred, causing a potential audio glitch.
    BufferUnderrun,

    /// See the [`BackendSpecificError`] docs for more information about this error variant.
    BackendSpecific { err: BackendSpecificError },
}

impl Display for StreamError {
    fn fmt(&self, f: &mut Formatter<'_>) -> std::fmt::Result {
        match self {
            Self::BackendSpecific { err } => err.fmt(f),
            Self::StreamInvalidated => {
                f.write_str("The stream configuration is no longer valid and must be rebuilt.")
            }
            Self::BufferUnderrun => f.write_str("Buffer underrun/overrun occurred."),
            Self::DeviceNotAvailable => f.write_str(
                "The requested device is no longer available. For example, it has been unplugged.",
            ),
        }
    }
}

impl Error for StreamError {}

impl From<BackendSpecificError> for StreamError {
    fn from(err: BackendSpecificError) -> Self {
        Self::BackendSpecific { err }
    }
}
```

## File: `src/lib.rs`
```rust
//! # How to use cpal
//!
//! Here are some concepts cpal exposes:
//!
//! - A [`Host`] provides access to the available audio devices on the system.
//!   Some platforms have more than one host available, but every platform supported by CPAL has at
//!   least one [default_host] that is guaranteed to be available.
//! - A [`Device`] is an audio device that may have any number of input and
//!   output streams.
//! - A [`Stream`] is an open flow of audio data. Input streams allow you to
//!   receive audio data, output streams allow you to play audio data. You must choose which
//!   [Device] will run your stream before you can create one. Often, a default device can be
//!   retrieved via the [Host].
//!
//! The first step is to initialise the [`Host`]:
//!
//! ```
//! use cpal::traits::HostTrait;
//! let host = cpal::default_host();
//! ```
//!
//! Then choose an available [`Device`]. The easiest way is to use the default input or output
//! `Device` via the [`default_input_device()`] or [`default_output_device()`] methods on `host`.
//!
//! Alternatively, you can enumerate all the available devices with the [`devices()`] method.
//! Beware that the `default_*_device()` functions return an `Option<Device>` in case no device
//! is available for that stream type on the system.
//!
//! ```no_run
//! # use cpal::traits::HostTrait;
//! # let host = cpal::default_host();
//! let device = host.default_output_device().expect("no output device available");
//! ```
//!
//! Before we can create a stream, we must decide what the configuration of the audio stream is
//! going to be.
//! You can query all the supported configurations with the
//! [`supported_input_configs()`] and [`supported_output_configs()`] methods.
//! These produce a list of [`SupportedStreamConfigRange`] structs which can later be turned into
//! actual [`SupportedStreamConfig`] structs.
//!
//! If you don't want to query the list of configs,
//! you can also build your own [`StreamConfig`] manually, but doing so could lead to an error when
//! building the stream if the config is not supported by the device.
//!
//! > **Note**: the `supported_input/output_configs()` methods
//! > could return an error for example if the device has been disconnected.
//!
//! ```no_run
//! use cpal::traits::{DeviceTrait, HostTrait};
//! # let host = cpal::default_host();
//! # let device = host.default_output_device().unwrap();
//! let mut supported_configs_range = device.supported_output_configs()
//!     .expect("error while querying configs");
//! let supported_config = supported_configs_range.next()
//!     .expect("no supported config?!")
//!     .with_max_sample_rate();
//! ```
//!
//! Now that we have everything for the stream, we are ready to create it from our selected device:
//!
//! ```no_run
//! use cpal::Data;
//! use cpal::traits::{DeviceTrait, HostTrait, StreamTrait};
//! # let host = cpal::default_host();
//! # let device = host.default_output_device().unwrap();
//! # let config = device.default_output_config().unwrap().into();
//! let stream = device.build_output_stream(
//!     config,
//!     move |data: &mut [f32], _: &cpal::OutputCallbackInfo| {
//!         // react to stream events and read or write stream data here.
//!     },
//!     move |err| {
//!         // react to errors here.
//!     },
//!     None // None=blocking, Some(Duration)=timeout
//! );
//! ```
//!
//! While the stream is running, the selected audio device will periodically call the data callback
//! that was passed to the function. For input streams, the callback receives `&`[`Data`] containing
//! captured audio samples. For output streams, the callback receives `&mut`[`Data`] to be filled
//! with audio samples for playback.
//!
//! > **Note**: Creating and running a stream will *not* block the thread. On modern platforms, the
//! > given callback is called by a dedicated, high-priority thread responsible for delivering
//! > audio data to the system's audio device in a timely manner. On older platforms that only
//! > provide a blocking API (e.g. ALSA), CPAL will create a thread in order to consistently
//! > provide non-blocking behaviour (currently this is a thread per stream, but this may change to
//! > use a single thread for all streams). *If this is an issue for your platform or design,
//! > please share your issue and use-case with the CPAL team on the GitHub issue tracker for
//! > consideration.*
//!
//! In this example, we simply fill the given output buffer with silence.
//!
//! ```no_run
//! use cpal::{Data, Sample, SampleFormat, FromSample};
//! use cpal::traits::{DeviceTrait, HostTrait, StreamTrait};
//! # let host = cpal::default_host();
//! # let device = host.default_output_device().unwrap();
//! # let supported_config = device.default_output_config().unwrap();
//! let err_fn = |err| eprintln!("an error occurred on the output audio stream: {}", err);
//! let sample_format = supported_config.sample_format();
//! let config = supported_config.into();
//! let stream = match sample_format {
//!     SampleFormat::F32 => device.build_output_stream(config, write_silence::<f32>, err_fn, None),
//!     SampleFormat::I16 => device.build_output_stream(config, write_silence::<i16>, err_fn, None),
//!     SampleFormat::U16 => device.build_output_stream(config, write_silence::<u16>, err_fn, None),
//!     sample_format => panic!("Unsupported sample format '{sample_format}'")
//! }.unwrap();
//!
//! fn write_silence<T: Sample>(data: &mut [T], _: &cpal::OutputCallbackInfo) {
//!     for sample in data.iter_mut() {
//!         *sample = Sample::EQUILIBRIUM;
//!     }
//! }
//! ```
//!
//! Not all platforms automatically run the stream upon creation. To ensure the stream has started,
//! we can use [`Stream::play`](traits::StreamTrait::play).
//!
//! ```no_run
//! # use cpal::traits::{DeviceTrait, HostTrait, StreamTrait};
//! # let host = cpal::default_host();
//! # let device = host.default_output_device().unwrap();
//! # let supported_config = device.default_output_config().unwrap();
//! # let sample_format = supported_config.sample_format();
//! # let config = supported_config.into();
//! # let data_fn = move |_data: &mut cpal::Data, _: &cpal::OutputCallbackInfo| {};
//! # let err_fn = move |_err| {};
//! # let stream = device.build_output_stream_raw(config, sample_format, data_fn, err_fn, None).unwrap();
//! stream.play().unwrap();
//! ```
//!
//! Some devices support pausing the audio stream. This can be useful for saving energy in moments
//! of silence.
//!
//! ```no_run
//! # use cpal::traits::{DeviceTrait, HostTrait, StreamTrait};
//! # let host = cpal::default_host();
//! # let device = host.default_output_device().unwrap();
//! # let supported_config = device.default_output_config().unwrap();
//! # let sample_format = supported_config.sample_format();
//! # let config = supported_config.into();
//! # let data_fn = move |_data: &mut cpal::Data, _: &cpal::OutputCallbackInfo| {};
//! # let err_fn = move |_err| {};
//! # let stream = device.build_output_stream_raw(config, sample_format, data_fn, err_fn, None).unwrap();
//! stream.pause().unwrap();
//! ```
//!
//! [`default_input_device()`]: traits::HostTrait::default_input_device
//! [`default_output_device()`]: traits::HostTrait::default_output_device
//! [`devices()`]: traits::HostTrait::devices
//! [`supported_input_configs()`]: traits::DeviceTrait::supported_input_configs
//! [`supported_output_configs()`]: traits::DeviceTrait::supported_output_configs

#![cfg_attr(docsrs, feature(doc_cfg))]

// Extern crate declarations with `#[macro_use]` must unfortunately be at crate root.
#[cfg(all(
    target_arch = "wasm32",
    any(target_os = "emscripten", feature = "wasm-bindgen")
))]
extern crate js_sys;
#[cfg(all(
    target_arch = "wasm32",
    any(target_os = "emscripten", feature = "wasm-bindgen")
))]
extern crate wasm_bindgen;
#[cfg(all(
    target_arch = "wasm32",
    any(target_os = "emscripten", feature = "wasm-bindgen")
))]
extern crate web_sys;

#[cfg(all(
    target_arch = "wasm32",
    any(target_os = "emscripten", feature = "wasm-bindgen")
))]
use wasm_bindgen::prelude::*;

pub use device_description::{
    DeviceDescription, DeviceDescriptionBuilder, DeviceDirection, DeviceType, InterfaceType,
};
pub use error::*;
pub use platform::{
    available_hosts, default_host, host_from_id, Device, Devices, Host, HostId, Stream,
    SupportedInputConfigs, SupportedOutputConfigs, ALL_HOSTS,
};
pub use samples_formats::{FromSample, Sample, SampleFormat, SizedSample, I24, U24};
use std::convert::TryInto;
use std::time::Duration;

pub mod device_description;
mod error;
mod host;
pub mod platform;
mod samples_formats;
pub mod traits;

/// Iterator of devices wrapped in a filter to only include certain device types
pub type DevicesFiltered<I> = std::iter::Filter<I, fn(&<I as Iterator>::Item) -> bool>;

/// A host's device iterator yielding only *input* devices.
pub type InputDevices<I> = DevicesFiltered<I>;

/// A host's device iterator yielding only *output* devices.
pub type OutputDevices<I> = DevicesFiltered<I>;

/// Number of channels.
pub type ChannelCount = u16;

/// The number of samples processed per second for a single channel of audio.
pub type SampleRate = u32;

/// A frame represents one sample for each channel. For example, with stereo audio,
/// one frame contains two samples (left and right channels).
pub type FrameCount = u32;

/// A stable identifier for an audio device across all supported platforms.
///
/// Device IDs should remain stable across application restarts and can be serialized using `Display`/`FromStr`.
///
/// A device ID consists of a [`HostId`] identifying the audio backend and a device-specific identifier string.
///
/// # Example
///
/// ```no_run
/// use cpal::traits::{HostTrait, DeviceTrait};
/// use cpal::DeviceId;
/// use std::str::FromStr;
///
/// let host = cpal::default_host();
/// let device = host.default_output_device().unwrap();
/// let device_id = device.id().unwrap();
///
/// // Serialize to string (e.g., for storage in config file)
/// let id_string = device_id.to_string();
/// println!("Device ID: {}", id_string); // e.g., "wasapi:device_identifier"
///
/// // Deserialize from string
/// match DeviceId::from_str(&id_string) {
///     Ok(parsed_id) => {
///         // Retrieve the device by its ID
///         if let Some(device) = host.device_by_id(&parsed_id) {
///             println!("Found device: {:?}", device.id());
///         }
///     }
///     Err(e) => eprintln!("Failed to parse device ID: {}", e),
/// }
/// ```
#[derive(Clone, Debug, PartialEq, Eq, Hash)]
pub struct DeviceId(pub crate::platform::HostId, pub String);

impl std::fmt::Display for DeviceId {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        write!(f, "{}:{}", self.0, self.1)
    }
}

impl std::str::FromStr for DeviceId {
    type Err = DeviceIdError;

    fn from_str(s: &str) -> Result<Self, Self::Err> {
        let (host_str, device_str) = s.split_once(':').ok_or(DeviceIdError::BackendSpecific {
            err: BackendSpecificError {
                description: format!(
                    "Failed to parse device ID from: {s}\nCheck if format matches \"host:device_id\""
                ),
            },
        })?;

        let host_id = crate::platform::HostId::from_str(host_str)
            .map_err(|_| DeviceIdError::UnsupportedPlatform)?;

        Ok(DeviceId(host_id, device_str.to_string()))
    }
}

/// The buffer size requests the callback size for audio streams.
///
/// This controls the approximate size of the audio buffer passed to your callback.
/// The actual callback size depends on the host/platform implementation and hardware
/// constraints, and may differ from or vary around the requested size.
///
/// ## Callback Size Expectations
///
/// When you specify [`BufferSize::Fixed(x)`], you are **requesting** that callbacks
/// receive approximately `x` frames of audio data. However, **no guarantees can be
/// made** about the actual callback size:
///
/// - The host may round to hardware-supported values
/// - Different devices have different constraints
/// - The callback size may vary between calls (especially on mobile platforms)
/// - The actual size might be larger or smaller than requested
///
/// ## Latency Considerations
///
/// [`BufferSize::Default`] uses the host's default buffer size, which may be
/// surprisingly large, leading to higher latency. If low latency is desired,
/// [`BufferSize::Fixed`] should be used with a small value in accordance with
/// the [`SupportedBufferSize`] range from [`SupportedStreamConfig`].
///
/// Smaller buffer sizes reduce latency but may increase CPU usage and risk audio
/// dropouts if the callback cannot process audio quickly enough.
///
/// # Example
///
/// ```no_run
/// use cpal::traits::{DeviceTrait, HostTrait};
/// use cpal::{BufferSize, SupportedBufferSize};
///
/// let host = cpal::default_host();
/// let device = host.default_output_device().unwrap();
/// let config = device.default_output_config().unwrap();
///
/// // Check supported buffer size range
/// match config.buffer_size() {
///     SupportedBufferSize::Range { min, max } => {
///         println!("Buffer size range: {} - {}", min, max);
///         // Request a small buffer for low latency
///         let mut stream_config = config.config();
///         stream_config.buffer_size = BufferSize::Fixed(256);
///     }
///     SupportedBufferSize::Unknown => {
///         // Platform doesn't expose buffer size control
///         println!("Buffer size cannot be queried on this platform");
///     }
/// }
/// ```
///
/// [`BufferSize::Default`]: BufferSize::Default
/// [`BufferSize::Fixed`]: BufferSize::Fixed
/// [`BufferSize::Fixed(x)`]: BufferSize::Fixed
/// [`SupportedBufferSize`]: SupportedStreamConfig::buffer_size
/// [`SupportedStreamConfig`]: SupportedStreamConfig
#[derive(Clone, Copy, Debug, Eq, PartialEq)]
pub enum BufferSize {
    Default,
    Fixed(FrameCount),
}

#[cfg(all(
    target_arch = "wasm32",
    any(target_os = "emscripten", feature = "wasm-bindgen")
))]
impl wasm_bindgen::describe::WasmDescribe for BufferSize {
    fn describe() {
        <Option<FrameCount> as wasm_bindgen::describe::WasmDescribe>::describe();
    }
}

#[cfg(all(
    target_arch = "wasm32",
    any(target_os = "emscripten", feature = "wasm-bindgen")
))]
impl wasm_bindgen::convert::IntoWasmAbi for BufferSize {
    type Abi = <Option<FrameCount> as wasm_bindgen::convert::IntoWasmAbi>::Abi;

    fn into_abi(self) -> Self::Abi {
        match self {
            Self::Default => None,
            Self::Fixed(fc) => Some(fc),
        }
        .into_abi()
    }
}

#[cfg(all(
    target_arch = "wasm32",
    any(target_os = "emscripten", feature = "wasm-bindgen")
))]
impl wasm_bindgen::convert::FromWasmAbi for BufferSize {
    type Abi = <Option<FrameCount> as wasm_bindgen::convert::FromWasmAbi>::Abi;

    unsafe fn from_abi(js: Self::Abi) -> Self {
        match Option::<FrameCount>::from_abi(js) {
            None => Self::Default,
            Some(fc) => Self::Fixed(fc),
        }
    }
}

/// The set of parameters used to describe how to open a stream.
///
/// The sample format is omitted in favour of using a sample type.
///
/// See also [`BufferSize`] for details on buffer size behavior and latency considerations.
#[cfg_attr(
    all(
        target_arch = "wasm32",
        any(target_os = "emscripten", feature = "wasm-bindgen")
    ),
    wasm_bindgen
)]
#[derive(Clone, Debug, Eq, PartialEq, Copy)]
pub struct StreamConfig {
    pub channels: ChannelCount,
    pub sample_rate: SampleRate,
    pub buffer_size: BufferSize,
}

/// Describes the minimum and maximum supported buffer size for the device
#[derive(Clone, Copy, Debug, Eq, PartialEq)]
pub enum SupportedBufferSize {
    Range {
        min: FrameCount,
        max: FrameCount,
    },
    /// In the case that the platform provides no way of getting the default
    /// buffer size before starting a stream.
    Unknown,
}

/// Describes a range of supported stream configurations, retrieved via the
/// [`Device::supported_input/output_configs`](traits::DeviceTrait#required-methods) method.
#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub struct SupportedStreamConfigRange {
    pub(crate) channels: ChannelCount,
    /// Minimum value for the sample rate of the supported formats.
    pub(crate) min_sample_rate: SampleRate,
    /// Maximum value for the sample rate of the supported formats.
    pub(crate) max_sample_rate: SampleRate,
    /// Buffer size ranges supported by the device
    pub(crate) buffer_size: SupportedBufferSize,
    /// Type of data expected by the device.
    pub(crate) sample_format: SampleFormat,
}

/// Common iterator types used by backend implementations.
///
/// All backends use these same concrete iterator types for supported stream configurations.
#[allow(dead_code)]
pub(crate) mod iter {
    use super::SupportedStreamConfigRange;

    /// Iterator type for supported input stream configurations.
    ///
    /// This is the iterator type returned by all backend implementations of
    /// [`DeviceTrait::supported_input_configs`](crate::traits::DeviceTrait::supported_input_configs).
    pub type SupportedInputConfigs = std::vec::IntoIter<SupportedStreamConfigRange>;

    /// Iterator type for supported output stream configurations.
    ///
    /// This is the iterator type returned by all backend implementations of
    /// [`DeviceTrait::supported_output_configs`](crate::traits::DeviceTrait::supported_output_configs).
    pub type SupportedOutputConfigs = std::vec::IntoIter<SupportedStreamConfigRange>;
}

/// Describes a single supported stream configuration, retrieved via either a
/// [`SupportedStreamConfigRange`] instance or one of the
/// [`Device::default_input/output_config`](traits::DeviceTrait#required-methods) methods.
#[derive(Debug, Clone, PartialEq, Eq)]
pub struct SupportedStreamConfig {
    channels: ChannelCount,
    sample_rate: SampleRate,
    buffer_size: SupportedBufferSize,
    sample_format: SampleFormat,
}

/// A buffer of dynamically typed audio data, passed to raw stream callbacks.
///
/// Raw input stream callbacks receive `&Data`, while raw output stream callbacks expect `&mut Data`.
#[cfg_attr(target_os = "emscripten", wasm_bindgen)]
#[derive(Debug)]
pub struct Data {
    data: *mut (),
    len: usize,
    sample_format: SampleFormat,
}

/// A monotonic time instance associated with a stream, retrieved from either:
///
/// 1. A timestamp provided to the stream's underlying audio data callback or
/// 2. The same time source used to generate timestamps for a stream's underlying audio data
///    callback.
///
/// `StreamInstant` represents a duration since an unspecified origin point. The origin
/// is guaranteed to occur at or before the stream starts, and remains consistent for the
/// lifetime of that stream. Different streams may have different origins.
///
/// ## Host `StreamInstant` Sources
///
/// | Host | Source |
/// | ---- | ------ |
/// | alsa | `snd_pcm_status_get_htstamp` |
/// | asio | `timeGetTime` |
/// | coreaudio | `mach_absolute_time` |
/// | emscripten | `AudioContext.getOutputTimestamp` |
/// | pulseaudio | `std::time::Instant` |
/// | wasapi | `QueryPerformanceCounter` |
#[derive(Copy, Clone, Debug, Eq, Hash, PartialEq, PartialOrd, Ord)]
pub struct StreamInstant {
    secs: i64,
    nanos: u32,
}

/// A timestamp associated with a call to an input stream's data callback.
#[derive(Copy, Clone, Debug, Eq, Hash, PartialEq)]
pub struct InputStreamTimestamp {
    /// The instant the stream's data callback was invoked.
    pub callback: StreamInstant,
    /// The instant that data was captured from the device.
    ///
    /// E.g. The instant data was read from an ADC.
    pub capture: StreamInstant,
}

/// A timestamp associated with a call to an output stream's data callback.
#[derive(Copy, Clone, Debug, Eq, Hash, PartialEq)]
pub struct OutputStreamTimestamp {
    /// The instant the stream's data callback was invoked.
    pub callback: StreamInstant,
    /// The predicted instant that data written will be delivered to the device for playback.
    ///
    /// E.g. The instant data will be played by a DAC.
    pub playback: StreamInstant,
}

/// Information relevant to a single call to the user's input stream data callback.
#[derive(Copy, Clone, Debug, Eq, Hash, PartialEq)]
pub struct InputCallbackInfo {
    timestamp: InputStreamTimestamp,
}

/// Information relevant to a single call to the user's output stream data callback.
#[cfg_attr(target_os = "emscripten", wasm_bindgen)]
#[derive(Copy, Clone, Debug, Eq, Hash, PartialEq)]
pub struct OutputCallbackInfo {
    timestamp: OutputStreamTimestamp,
}

impl SupportedStreamConfig {
    pub fn new(
        channels: ChannelCount,
        sample_rate: SampleRate,
        buffer_size: SupportedBufferSize,
        sample_format: SampleFormat,
    ) -> Self {
        Self {
            channels,
            sample_rate,
            buffer_size,
            sample_format,
        }
    }

    pub fn channels(&self) -> ChannelCount {
        self.channels
    }

    pub fn sample_rate(&self) -> SampleRate {
        self.sample_rate
    }

    pub fn buffer_size(&self) -> &SupportedBufferSize {
        &self.buffer_size
    }

    pub fn sample_format(&self) -> SampleFormat {
        self.sample_format
    }

    pub fn config(&self) -> StreamConfig {
        StreamConfig {
            channels: self.channels,
            sample_rate: self.sample_rate,
            buffer_size: BufferSize::Default,
        }
    }
}

impl StreamInstant {
    /// The amount of time elapsed from another instant to this one.
    ///
    /// Returns `None` if `earlier` is later than self.
    pub fn duration_since(&self, earlier: &Self) -> Option<Duration> {
        if self < earlier {
            None
        } else {
            (self.as_nanos() - earlier.as_nanos())
                .try_into()
                .ok()
                .map(Duration::from_nanos)
        }
    }

    /// Returns the instant in time after the given duration has passed.
    ///
    /// Returns `None` if the resulting instant would exceed the bounds of the underlying data
    /// structure.
    pub fn add(&self, duration: Duration) -> Option<Self> {
        self.as_nanos()
            .checked_add(duration.as_nanos() as i128)
            .and_then(Self::from_nanos_i128)
    }

    /// Returns the instant in time one `duration` ago.
    ///
    /// Returns `None` if the resulting instant would underflow. As a result, it is important to
    /// consider that on some platforms the [`StreamInstant`] may begin at `0` from the moment the
    /// source stream is created.
    pub fn sub(&self, duration: Duration) -> Option<Self> {
        self.as_nanos()
            .checked_sub(duration.as_nanos() as i128)
            .and_then(Self::from_nanos_i128)
    }

    fn as_nanos(&self) -> i128 {
        (self.secs as i128 * 1_000_000_000) + self.nanos as i128
    }

    #[allow(dead_code)]
    fn from_nanos(nanos: i64) -> Self {
        let secs = nanos / 1_000_000_000;
        let subsec_nanos = nanos - secs * 1_000_000_000;
        Self::new(secs, subsec_nanos as u32)
    }

    #[allow(dead_code)]
    fn from_nanos_i128(nanos: i128) -> Option<Self> {
        let secs = nanos / 1_000_000_000;
        if secs > i64::MAX as i128 || secs < i64::MIN as i128 {
            None
        } else {
            let subsec_nanos = nanos - secs * 1_000_000_000;
            debug_assert!(subsec_nanos < u32::MAX as i128);
            Some(Self::new(secs as i64, subsec_nanos as u32))
        }
    }

    #[allow(dead_code)]
    fn from_secs_f64(secs: f64) -> crate::StreamInstant {
        let s = secs.floor() as i64;
        let ns = ((secs - s as f64) * 1_000_000_000.0) as u32;
        Self::new(s, ns)
    }

    pub fn new(secs: i64, nanos: u32) -> Self {
        StreamInstant { secs, nanos }
    }
}

impl InputCallbackInfo {
    pub fn new(timestamp: InputStreamTimestamp) -> Self {
        Self { timestamp }
    }

    /// The timestamp associated with the call to an input stream's data callback.
    pub fn timestamp(&self) -> InputStreamTimestamp {
        self.timestamp
    }
}

impl OutputCallbackInfo {
    pub fn new(timestamp: OutputStreamTimestamp) -> Self {
        Self { timestamp }
    }

    /// The timestamp associated with the call to an output stream's data callback.
    pub fn timestamp(&self) -> OutputStreamTimestamp {
        self.timestamp
    }
}

// Note: Data does not implement `is_empty()` because it always contains a valid audio buffer
// by design. The buffer may contain silence, but it is never structurally empty.
#[allow(clippy::len_without_is_empty)]
impl Data {
    /// Constructor for host implementations to use.
    ///
    /// # Safety
    /// The following requirements must be met in order for the safety of `Data`'s API.
    /// - The `data` pointer must point to the first sample in the slice containing all samples.
    /// - The `len` must describe the length of the buffer as a number of samples in the expected
    ///   format specified via the `sample_format` argument.
    /// - The `sample_format` must correctly represent the underlying sample data delivered/expected
    ///   by the stream.
    pub unsafe fn from_parts(data: *mut (), len: usize, sample_format: SampleFormat) -> Self {
        Data {
            data,
            len,
            sample_format,
        }
    }

    /// The sample format of the internal audio data.
    pub fn sample_format(&self) -> SampleFormat {
        self.sample_format
    }

    /// The full length of the buffer in samples.
    ///
    /// The returned length is the same length as the slice of type `T` that would be returned via
    /// [`as_slice`](Self::as_slice) given a sample type that matches the inner sample format.
    pub fn len(&self) -> usize {
        self.len
    }

    /// The raw slice of memory representing the underlying audio data as a slice of bytes.
    ///
    /// It is up to the user to interpret the slice of memory based on [`Data::sample_format`].
    pub fn bytes(&self) -> &[u8] {
        let len = self.len * self.sample_format.sample_size();
        // The safety of this block relies on correct construction of the `Data` instance.
        // See the unsafe `from_parts` constructor for these requirements.
        unsafe { std::slice::from_raw_parts(self.data as *const u8, len) }
    }

    /// The raw slice of memory representing the underlying audio data as a slice of bytes.
    ///
    /// It is up to the user to interpret the slice of memory based on [`Data::sample_format`].
    pub fn bytes_mut(&mut self) -> &mut [u8] {
        let len = self.len * self.sample_format.sample_size();
        // The safety of this block relies on correct construction of the `Data` instance. See
        // the unsafe `from_parts` constructor for these requirements.
        unsafe { std::slice::from_raw_parts_mut(self.data as *mut u8, len) }
    }

    /// Access the data as a slice of sample type `T`.
    ///
    /// Returns `None` if the sample type does not match the expected sample format.
    pub fn as_slice<T>(&self) -> Option<&[T]>
    where
        T: SizedSample,
    {
        if T::FORMAT == self.sample_format {
            // The safety of this block relies on correct construction of the `Data` instance. See
            // the unsafe `from_parts` constructor for these requirements.
            unsafe { Some(std::slice::from_raw_parts(self.data as *const T, self.len)) }
        } else {
            None
        }
    }

    /// Access the data as a slice of sample type `T`.
    ///
    /// Returns `None` if the sample type does not match the expected sample format.
    pub fn as_slice_mut<T>(&mut self) -> Option<&mut [T]>
    where
        T: SizedSample,
    {
        if T::FORMAT == self.sample_format {
            // The safety of this block relies on correct construction of the `Data` instance. See
            // the unsafe `from_parts` constructor for these requirements.
            unsafe {
                Some(std::slice::from_raw_parts_mut(
                    self.data as *mut T,
                    self.len,
                ))
            }
        } else {
            None
        }
    }
}

impl SupportedStreamConfigRange {
    pub fn new(
        channels: ChannelCount,
        min_sample_rate: SampleRate,
        max_sample_rate: SampleRate,
        buffer_size: SupportedBufferSize,
        sample_format: SampleFormat,
    ) -> Self {
        Self {
            channels,
            min_sample_rate,
            max_sample_rate,
            buffer_size,
            sample_format,
        }
    }

    pub fn channels(&self) -> ChannelCount {
        self.channels
    }

    pub fn min_sample_rate(&self) -> SampleRate {
        self.min_sample_rate
    }

    pub fn max_sample_rate(&self) -> SampleRate {
        self.max_sample_rate
    }

    pub fn buffer_size(&self) -> &SupportedBufferSize {
        &self.buffer_size
    }

    pub fn sample_format(&self) -> SampleFormat {
        self.sample_format
    }

    /// Retrieve a [`SupportedStreamConfig`] with the given sample rate and buffer size.
    ///
    /// # Panics
    ///
    /// Panics if the given `sample_rate` is outside the range specified within
    /// this [`SupportedStreamConfigRange`] instance. For a non-panicking
    /// variant, use [`try_with_sample_rate`](#method.try_with_sample_rate).
    pub fn with_sample_rate(self, sample_rate: SampleRate) -> SupportedStreamConfig {
        self.try_with_sample_rate(sample_rate)
            .expect("sample rate out of range")
    }

    /// Retrieve a [`SupportedStreamConfig`] with the given sample rate and buffer size.
    ///
    /// Returns `None` if the given sample rate is outside the range specified
    /// within this [`SupportedStreamConfigRange`] instance.
    pub fn try_with_sample_rate(self, sample_rate: SampleRate) -> Option<SupportedStreamConfig> {
        if self.min_sample_rate <= sample_rate && sample_rate <= self.max_sample_rate {
            Some(SupportedStreamConfig {
                channels: self.channels,
                sample_rate,
                sample_format: self.sample_format,
                buffer_size: self.buffer_size,
            })
        } else {
            None
        }
    }

    /// Turns this [`SupportedStreamConfigRange`] into a [`SupportedStreamConfig`] corresponding to the maximum sample rate.
    #[inline]
    pub fn with_max_sample_rate(self) -> SupportedStreamConfig {
        SupportedStreamConfig {
            channels: self.channels,
            sample_rate: self.max_sample_rate,
            sample_format: self.sample_format,
            buffer_size: self.buffer_size,
        }
    }

    /// A comparison function which compares two [`SupportedStreamConfigRange`]s in terms of their priority of
    /// use as a default stream format.
    ///
    /// Some backends do not provide a default stream format for their audio devices. In these
    /// cases, CPAL attempts to decide on a reasonable default format for the user. To do this we
    /// use the "greatest" of all supported stream formats when compared with this method.
    ///
    /// SupportedStreamConfigs are prioritised by the following heuristics:
    ///
    /// **Channels**:
    ///
    /// - Stereo
    /// - Mono
    /// - Max available channels
    ///
    /// **Sample format**:
    /// - f32
    /// - i16
    /// - u16
    ///
    /// **Sample rate**:
    ///
    /// - 44100 (cd quality)
    /// - Max sample rate
    pub fn cmp_default_heuristics(&self, other: &Self) -> std::cmp::Ordering {
        use std::cmp::Ordering::Equal;
        use SampleFormat::{F32, I16, I24, I32, U16, U24, U32};

        let cmp_stereo = (self.channels == 2).cmp(&(other.channels == 2));
        if cmp_stereo != Equal {
            return cmp_stereo;
        }

        let cmp_mono = (self.channels == 1).cmp(&(other.channels == 1));
        if cmp_mono != Equal {
            return cmp_mono;
        }

        let cmp_channels = self.channels.cmp(&other.channels);
        if cmp_channels != Equal {
            return cmp_channels;
        }

        let cmp_f32 = (self.sample_format == F32).cmp(&(other.sample_format == F32));
        if cmp_f32 != Equal {
            return cmp_f32;
        }

        let cmp_i32 = (self.sample_format == I32).cmp(&(other.sample_format == I32));
        if cmp_i32 != Equal {
            return cmp_i32;
        }

        let cmp_u32 = (self.sample_format == U32).cmp(&(other.sample_format == U32));
        if cmp_u32 != Equal {
            return cmp_u32;
        }

        let cmp_i24 = (self.sample_format == I24).cmp(&(other.sample_format == I24));
        if cmp_i24 != Equal {
            return cmp_i24;
        }

        let cmp_u24 = (self.sample_format == U24).cmp(&(other.sample_format == U24));
        if cmp_u24 != Equal {
            return cmp_u24;
        }

        let cmp_i16 = (self.sample_format == I16).cmp(&(other.sample_format == I16));
        if cmp_i16 != Equal {
            return cmp_i16;
        }

        let cmp_u16 = (self.sample_format == U16).cmp(&(other.sample_format == U16));
        if cmp_u16 != Equal {
            return cmp_u16;
        }

        const HZ_44100: SampleRate = 44_100;
        let r44100_in_self = self.min_sample_rate <= HZ_44100 && HZ_44100 <= self.max_sample_rate;
        let r44100_in_other =
            other.min_sample_rate <= HZ_44100 && HZ_44100 <= other.max_sample_rate;
        let cmp_r44100 = r44100_in_self.cmp(&r44100_in_other);
        if cmp_r44100 != Equal {
            return cmp_r44100;
        }

        self.max_sample_rate.cmp(&other.max_sample_rate)
    }
}

#[test]
fn test_cmp_default_heuristics() {
    let mut formats = [
        SupportedStreamConfigRange {
            buffer_size: SupportedBufferSize::Range { min: 256, max: 512 },
            channels: 2,
            min_sample_rate: 1,
            max_sample_rate: 96000,
            sample_format: SampleFormat::F32,
        },
        SupportedStreamConfigRange {
            buffer_size: SupportedBufferSize::Range { min: 256, max: 512 },
            channels: 1,
            min_sample_rate: 1,
            max_sample_rate: 96000,
            sample_format: SampleFormat::F32,
        },
        SupportedStreamConfigRange {
            buffer_size: SupportedBufferSize::Range { min: 256, max: 512 },
            channels: 2,
            min_sample_rate: 1,
            max_sample_rate: 96000,
            sample_format: SampleFormat::I16,
        },
        SupportedStreamConfigRange {
            buffer_size: SupportedBufferSize::Range { min: 256, max: 512 },
            channels: 2,
            min_sample_rate: 1,
            max_sample_rate: 96000,
            sample_format: SampleFormat::U16,
        },
        SupportedStreamConfigRange {
            buffer_size: SupportedBufferSize::Range { min: 256, max: 512 },
            channels: 2,
            min_sample_rate: 1,
            max_sample_rate: 22050,
            sample_format: SampleFormat::F32,
        },
    ];

    formats.sort_by(|a, b| a.cmp_default_heuristics(b));

    // lowest-priority first:
    assert_eq!(formats[0].sample_format(), SampleFormat::F32);
    assert_eq!(formats[0].min_sample_rate(), 1);
    assert_eq!(formats[0].max_sample_rate(), 96000);
    assert_eq!(formats[0].channels(), 1);

    assert_eq!(formats[1].sample_format(), SampleFormat::U16);
    assert_eq!(formats[1].min_sample_rate(), 1);
    assert_eq!(formats[1].max_sample_rate(), 96000);
    assert_eq!(formats[1].channels(), 2);

    assert_eq!(formats[2].sample_format(), SampleFormat::I16);
    assert_eq!(formats[2].min_sample_rate(), 1);
    assert_eq!(formats[2].max_sample_rate(), 96000);
    assert_eq!(formats[2].channels(), 2);

    assert_eq!(formats[3].sample_format(), SampleFormat::F32);
    assert_eq!(formats[3].min_sample_rate(), 1);
    assert_eq!(formats[3].max_sample_rate(), 22050);
    assert_eq!(formats[3].channels(), 2);

    assert_eq!(formats[4].sample_format(), SampleFormat::F32);
    assert_eq!(formats[4].min_sample_rate(), 1);
    assert_eq!(formats[4].max_sample_rate(), 96000);
    assert_eq!(formats[4].channels(), 2);
}

impl From<SupportedStreamConfig> for StreamConfig {
    fn from(conf: SupportedStreamConfig) -> Self {
        conf.config()
    }
}

// If a backend does not provide an API for retrieving supported formats, we query it with a bunch
// of commonly used rates. This is always the case for WASAPI and is sometimes the case for ALSA.
#[allow(dead_code)]
pub(crate) const COMMON_SAMPLE_RATES: &[SampleRate] = &[
    5512, 8000, 11025, 12000, 16000, 22050, 24000, 32000, 44100, 48000, 64000, 88200, 96000,
    176400, 192000, 352800, 384000, 705600, 768000, 1411200, 1536000,
];

#[test]
fn test_stream_instant() {
    let a = StreamInstant::new(2, 0);
    let b = StreamInstant::new(-2, 0);
    let min = StreamInstant::new(i64::MIN, 0);
    let max = StreamInstant::new(i64::MAX, 0);
    assert_eq!(
        a.sub(Duration::from_secs(1)),
        Some(StreamInstant::new(1, 0))
    );
    assert_eq!(
        a.sub(Duration::from_secs(2)),
        Some(StreamInstant::new(0, 0))
    );
    assert_eq!(
        a.sub(Duration::from_secs(3)),
        Some(StreamInstant::new(-1, 0))
    );
    assert_eq!(min.sub(Duration::from_secs(1)), None);
    assert_eq!(
        b.add(Duration::from_secs(1)),
        Some(StreamInstant::new(-1, 0))
    );
    assert_eq!(
        b.add(Duration::from_secs(2)),
        Some(StreamInstant::new(0, 0))
    );
    assert_eq!(
        b.add(Duration::from_secs(3)),
        Some(StreamInstant::new(1, 0))
    );
    assert_eq!(max.add(Duration::from_secs(1)), None);
}
```

## File: `src/samples_formats.rs`
```rust
//! Audio sample format types and conversions.
//!
//! # Byte Order
//!
//! All multi-byte sample formats use the native endianness of the target platform.
//! CPAL handles any necessary conversions when interfacing with hardware that uses
//! a different byte order.

use std::{fmt::Display, mem};
#[cfg(all(
    target_arch = "wasm32",
    any(target_os = "emscripten", feature = "wasm-bindgen")
))]
use wasm_bindgen::prelude::*;

pub use dasp_sample::{FromSample, Sample};

/// 24-bit signed integer sample type.
///
/// Represents 24-bit audio with range `-(1 << 23)..=((1 << 23) - 1)`.
///
/// **Note:** While representing 24-bit audio, this format uses 4 bytes (i32) of storage
/// with the most significant byte unused. Use [`SampleFormat::bits_per_sample`] to get
/// the actual bit depth (24) vs [`SampleFormat::sample_size`] for storage size (4 bytes).
pub use dasp_sample::I24;

/// 24-bit unsigned integer sample type.
///
/// Represents 24-bit audio with range `0..=((1 << 24) - 1)`, with origin at `1 << 23 == 8388608`.
///
/// **Note:** While representing 24-bit audio, this format uses 4 bytes (u32) of storage
/// with the most significant byte unused. Use [`SampleFormat::bits_per_sample`] to get
/// the actual bit depth (24) vs [`SampleFormat::sample_size`] for storage size (4 bytes).
pub use dasp_sample::U24;

// I48 and U48 are not currently supported by cpal but available in dasp_sample:
// pub use dasp_sample::{I48, U48};

/// Format that each sample has. Usually, this corresponds to the sampling
/// depth of the audio source. For example, 16 bit quantized samples can be
/// encoded in `i16` or `u16`. Note that the quantized sampling depth is not
/// directly visible for formats where [`is_float`] is true.
///
/// Also note that the backend must support the encoding of the quantized
/// samples in the given format, as there is no generic transformation from one
/// format into the other done inside the frontend-library code. You can query
/// the supported formats by using [`supported_input_configs`].
///
/// A good rule of thumb is to use [`SampleFormat::I16`] as this covers typical
/// music (WAV, MP3) as well as typical audio input devices on most platforms,
///
/// [`is_float`]: SampleFormat::is_float
/// [`supported_input_configs`]: crate::traits::DeviceTrait::supported_input_configs
#[cfg_attr(
    all(
        target_arch = "wasm32",
        any(target_os = "emscripten", feature = "wasm-bindgen")
    ),
    wasm_bindgen
)]
#[derive(Clone, Copy, Debug, PartialEq, Eq, PartialOrd, Ord, Hash)]
#[non_exhaustive]
pub enum SampleFormat {
    /// `i8` with a valid range of `i8::MIN..=i8::MAX` with `0` being the origin.
    I8,

    /// `i16` with a valid range of `i16::MIN..=i16::MAX` with `0` being the origin.
    I16,

    /// `I24` with a valid range of `-(1 << 23)..=((1 << 23) - 1)` with `0` being the origin.
    ///
    /// This format uses 4 bytes of storage but only 24 bits are significant.
    I24,

    /// `i32` with a valid range of `i32::MIN..=i32::MAX` with `0` being the origin.
    I32,

    // /// `I48` with a valid range of '-(1 << 47)..(1 << 47)' with `0` being the origin
    // I48,
    /// `i64` with a valid range of `i64::MIN..=i64::MAX` with `0` being the origin.
    I64,

    /// `u8` with a valid range of `u8::MIN..=u8::MAX` with `1 << 7 == 128` being the origin.
    U8,

    /// `u16` with a valid range of `u16::MIN..=u16::MAX` with `1 << 15 == 32768` being the origin.
    U16,

    /// `U24` with a valid range of `0..=((1 << 24) - 1)` with `1 << 23 == 8388608` being the origin.
    ///
    /// This format uses 4 bytes of storage but only 24 bits are significant.
    U24,

    /// `u32` with a valid range of `u32::MIN..=u32::MAX` with `1 << 31` being the origin.
    U32,

    /// `U48` with a valid range of '0..(1 << 48)' with `1 << 47` being the origin
    // U48,

    /// `u64` with a valid range of `u64::MIN..=u64::MAX` with `1 << 63` being the origin.
    U64,

    /// `f32` with a valid range of `-1.0..=1.0` with `0.0` being the origin.
    F32,

    /// `f64` with a valid range of `-1.0..=1.0` with `0.0` being the origin.
    F64,

    /// DSD 1-bit stream in u8 container (8 bits = 8 DSD samples) with 0x69 being the silence byte pattern.
    DsdU8,

    /// DSD 1-bit stream in u16 container (16 bits = 16 DSD samples) with 0x69 being the silence byte pattern.
    DsdU16,

    /// DSD 1-bit stream in u32 container (32 bits = 32 DSD samples) with 0x69 being the silence byte pattern.
    DsdU32,
}

impl SampleFormat {
    /// Returns the size in bytes of a sample of this format. This corresponds to
    /// the internal size of the rust primitives that are used to represent this
    /// sample format (e.g., i24 has size of i32).
    #[inline]
    #[must_use]
    pub fn sample_size(&self) -> usize {
        match *self {
            SampleFormat::I8 => mem::size_of::<i8>(),
            SampleFormat::U8 => mem::size_of::<u8>(),
            SampleFormat::I16 => mem::size_of::<i16>(),
            SampleFormat::U16 => mem::size_of::<u16>(),
            SampleFormat::I24 => mem::size_of::<i32>(),
            SampleFormat::U24 => mem::size_of::<i32>(),
            SampleFormat::I32 => mem::size_of::<i32>(),
            SampleFormat::U32 => mem::size_of::<u32>(),
            // SampleFormat::I48 => mem::size_of::<i64>(),
            // SampleFormat::U48 => mem::size_of::<i64>(),
            SampleFormat::I64 => mem::size_of::<i64>(),
            SampleFormat::U64 => mem::size_of::<u64>(),
            SampleFormat::F32 => mem::size_of::<f32>(),
            SampleFormat::F64 => mem::size_of::<f64>(),
            SampleFormat::DsdU8 => mem::size_of::<u8>(),
            SampleFormat::DsdU16 => mem::size_of::<u16>(),
            SampleFormat::DsdU32 => mem::size_of::<u32>(),
        }
    }

    /// Returns the number of bits of a sample of this format. Note that this is
    /// not necessarily the same as the size of the primitive used to represent
    /// this sample format (e.g., I24 has size of i32 but 24 bits per sample).
    #[inline]
    #[must_use]
    pub fn bits_per_sample(&self) -> u32 {
        match *self {
            SampleFormat::I8 => i8::BITS,
            SampleFormat::U8 => u8::BITS,
            SampleFormat::I16 => i16::BITS,
            SampleFormat::U16 => u16::BITS,
            SampleFormat::I24 => 24,
            SampleFormat::U24 => 24,
            SampleFormat::I32 => i32::BITS,
            SampleFormat::U32 => u32::BITS,
            // SampleFormat::I48 => 48,
            // SampleFormat::U48 => 48,
            SampleFormat::I64 => i64::BITS,
            SampleFormat::U64 => u64::BITS,
            SampleFormat::F32 => 32,
            SampleFormat::F64 => 64,
            SampleFormat::DsdU8 | SampleFormat::DsdU16 | SampleFormat::DsdU32 => 1,
        }
    }

    #[inline]
    #[must_use]
    pub fn is_int(&self) -> bool {
        matches!(
            *self,
            SampleFormat::I8
                | SampleFormat::I16
                | SampleFormat::I24
                | SampleFormat::I32
                // | SampleFormat::I48
                | SampleFormat::I64
        )
    }

    #[inline]
    #[must_use]
    pub fn is_uint(&self) -> bool {
        matches!(
            *self,
            SampleFormat::U8
                | SampleFormat::U16
                | SampleFormat::U24
                | SampleFormat::U32
                // | SampleFormat::U48
                | SampleFormat::U64
        )
    }

    #[inline]
    #[must_use]
    pub fn is_float(&self) -> bool {
        matches!(*self, SampleFormat::F32 | SampleFormat::F64)
    }

    #[inline]
    #[must_use]
    pub fn is_dsd(&self) -> bool {
        matches!(
            *self,
            SampleFormat::DsdU8 | SampleFormat::DsdU16 | SampleFormat::DsdU32
        )
    }
}

impl Display for SampleFormat {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        match *self {
            SampleFormat::I8 => "i8",
            SampleFormat::I16 => "i16",
            SampleFormat::I24 => "i24",
            SampleFormat::I32 => "i32",
            // SampleFormat::I48 => "i48",
            SampleFormat::I64 => "i64",
            SampleFormat::U8 => "u8",
            SampleFormat::U16 => "u16",
            SampleFormat::U24 => "u24",
            SampleFormat::U32 => "u32",
            // SampleFormat::U48 => "u48",
            SampleFormat::U64 => "u64",
            SampleFormat::F32 => "f32",
            SampleFormat::F64 => "f64",
            SampleFormat::DsdU8 => "dsdu8",
            SampleFormat::DsdU16 => "dsdu16",
            SampleFormat::DsdU32 => "dsdu32",
        }
        .fmt(f)
    }
}

/// A [`Sample`] type with a known corresponding [`SampleFormat`].
///
/// This trait is automatically implemented for all primitive sample types and provides
/// a way to determine the [`SampleFormat`] at compile time.
///
/// # Example
///
/// ```
/// use cpal::SizedSample;
///
/// assert_eq!(i16::FORMAT, cpal::SampleFormat::I16);
/// assert_eq!(f32::FORMAT, cpal::SampleFormat::F32);
/// ```
pub trait SizedSample: Sample {
    /// The corresponding [`SampleFormat`] for this sample type.
    const FORMAT: SampleFormat;
}

impl SizedSample for i8 {
    const FORMAT: SampleFormat = SampleFormat::I8;
}

impl SizedSample for i16 {
    const FORMAT: SampleFormat = SampleFormat::I16;
}

impl SizedSample for I24 {
    const FORMAT: SampleFormat = SampleFormat::I24;
}

impl SizedSample for i32 {
    const FORMAT: SampleFormat = SampleFormat::I32;
}

// impl SizedSample for I48 {
//     const FORMAT: SampleFormat = SampleFormat::I48;
// }

impl SizedSample for i64 {
    const FORMAT: SampleFormat = SampleFormat::I64;
}

impl SizedSample for u8 {
    const FORMAT: SampleFormat = SampleFormat::U8;
}

impl SizedSample for u16 {
    const FORMAT: SampleFormat = SampleFormat::U16;
}

impl SizedSample for U24 {
    const FORMAT: SampleFormat = SampleFormat::U24;
}

impl SizedSample for u32 {
    const FORMAT: SampleFormat = SampleFormat::U32;
}

// impl SizedSample for U48 {
//     const FORMAT: SampleFormat = SampleFormat::U48;
// }

impl SizedSample for u64 {
    const FORMAT: SampleFormat = SampleFormat::U64;
}

impl SizedSample for f32 {
    const FORMAT: SampleFormat = SampleFormat::F32;
}

impl SizedSample for f64 {
    const FORMAT: SampleFormat = SampleFormat::F64;
}
```

## File: `src/traits.rs`
```rust
//! The suite of traits allowing CPAL to abstract over hosts, devices, event loops and stream IDs.
//!
//! # Custom Host Implementations
//!
//! When implementing custom hosts with the `custom` feature, use the [`assert_stream_send!`](crate::assert_stream_send)
//! and [`assert_stream_sync!`](crate::assert_stream_sync) macros to verify your `Stream` type meets CPAL's requirements.

use std::time::Duration;

use crate::{
    BuildStreamError, Data, DefaultStreamConfigError, DeviceDescription, DeviceId, DeviceIdError,
    DeviceNameError, DevicesError, InputCallbackInfo, InputDevices, OutputCallbackInfo,
    OutputDevices, PauseStreamError, PlayStreamError, SampleFormat, SizedSample, StreamConfig,
    StreamError, SupportedStreamConfig, SupportedStreamConfigRange, SupportedStreamConfigsError,
};

/// A [`Host`] provides access to the available audio devices on the system.
///
/// Each platform may have a number of available hosts depending on the system, each with their own
/// pros and cons.
///
/// For example, WASAPI is the standard audio host API that ships with the Windows operating
/// system. However, due to historical limitations with respect to performance and flexibility,
/// Steinberg created the ASIO API providing better audio device support for pro audio and
/// low-latency applications. As a result, it is common for some devices and device capabilities to
/// only be available via ASIO, while others are only available via WASAPI.
///
/// Another great example is the Linux platform. While the ALSA host API is the lowest-level API
/// available to almost all distributions of Linux, its flexibility is limited as it requires that
/// each process have exclusive access to the devices with which they establish streams. PulseAudio
/// is another popular host API that aims to solve this issue by providing user-space mixing,
/// however it has its own limitations w.r.t. low-latency and high-performance audio applications.
/// JACK is yet another host API that is more suitable to pro-audio applications, however it is
/// less readily available by default in many Linux distributions and is known to be tricky to
/// set up.
///
/// [`Host`]: crate::Host
pub trait HostTrait {
    /// The type used for enumerating available devices by the host.
    type Devices: Iterator<Item = Self::Device>;
    /// The `Device` type yielded by the host.
    type Device: DeviceTrait;

    /// Whether or not the host is available on the system.
    fn is_available() -> bool;

    /// An iterator yielding all [`Device`](DeviceTrait)s currently available to the host on the system.
    ///
    /// Can be empty if the system does not support audio in general.
    fn devices(&self) -> Result<Self::Devices, DevicesError>;

    /// Fetches a [`Device`](DeviceTrait) based on a [`DeviceId`] if available
    ///
    /// Returns `None` if no device matching the id is found
    fn device_by_id(&self, id: &DeviceId) -> Option<Self::Device> {
        self.devices()
            .ok()?
            .find(|device| device.id().ok().as_ref() == Some(id))
    }

    /// The default input audio device on the system.
    ///
    /// Returns `None` if no input device is available.
    fn default_input_device(&self) -> Option<Self::Device>;

    /// The default output audio device on the system.
    ///
    /// Returns `None` if no output device is available.
    fn default_output_device(&self) -> Option<Self::Device>;

    /// An iterator yielding all `Device`s currently available to the system that support one or more
    /// input stream formats.
    ///
    /// Can be empty if the system does not support audio input.
    fn input_devices(&self) -> Result<InputDevices<Self::Devices>, DevicesError> {
        Ok(self.devices()?.filter(DeviceTrait::supports_input))
    }

    /// An iterator yielding all `Device`s currently available to the system that support one or more
    /// output stream formats.
    ///
    /// Can be empty if the system does not support audio output.
    fn output_devices(&self) -> Result<OutputDevices<Self::Devices>, DevicesError> {
        Ok(self.devices()?.filter(DeviceTrait::supports_output))
    }
}

/// A device that is capable of audio input and/or output.
///
/// Please note that `Device`s may become invalid if they get disconnected. Therefore, all the
/// methods that involve a device return a `Result` allowing the user to handle this case.
pub trait DeviceTrait {
    /// The iterator type yielding supported input stream formats.
    type SupportedInputConfigs: Iterator<Item = SupportedStreamConfigRange>;
    /// The iterator type yielding supported output stream formats.
    type SupportedOutputConfigs: Iterator<Item = SupportedStreamConfigRange>;
    /// The stream type created by [`build_input_stream_raw`] and [`build_output_stream_raw`].
    ///
    /// [`build_input_stream_raw`]: Self::build_input_stream_raw
    /// [`build_output_stream_raw`]: Self::build_output_stream_raw
    type Stream: StreamTrait;

    /// The human-readable name of the device.
    #[deprecated(
        since = "0.17.0",
        note = "Use `description()` for comprehensive device information including name, \
                manufacturer, and device type. Use `id()` for a unique, stable device identifier \
                that persists across reboots and reconnections."
    )]
    fn name(&self) -> Result<String, DeviceNameError> {
        self.description().map(|desc| desc.name().to_string())
    }

    /// Structured description of the device with metadata.
    ///
    /// This returns a [`DeviceDescription`] containing structured information about the device,
    /// including name, manufacturer (if available), device type, bus type, and other
    /// platform-specific metadata.
    ///
    /// For simple string representation, use `device.description().to_string()` or
    /// `device.description().name()`.
    fn description(&self) -> Result<DeviceDescription, DeviceNameError>;

    /// The ID of the device.
    ///
    /// This ID uniquely identifies the device on the host. It should be stable across program
    /// runs, device disconnections, and system reboots where possible.
    fn id(&self) -> Result<DeviceId, DeviceIdError>;

    /// True if the device supports audio input, otherwise false
    fn supports_input(&self) -> bool {
        self.supported_input_configs()
            .is_ok_and(|mut iter| iter.next().is_some())
    }

    /// True if the device supports audio output, otherwise false
    fn supports_output(&self) -> bool {
        self.supported_output_configs()
            .is_ok_and(|mut iter| iter.next().is_some())
    }

    /// An iterator yielding formats that are supported by the backend.
    ///
    /// Can return an error if the device is no longer valid (e.g. it has been disconnected).
    fn supported_input_configs(
        &self,
    ) -> Result<Self::SupportedInputConfigs, SupportedStreamConfigsError>;

    /// An iterator yielding output stream formats that are supported by the device.
    ///
    /// Can return an error if the device is no longer valid (e.g. it has been disconnected).
    fn supported_output_configs(
        &self,
    ) -> Result<Self::SupportedOutputConfigs, SupportedStreamConfigsError>;

    /// The default input stream format for the device.
    fn default_input_config(&self) -> Result<SupportedStreamConfig, DefaultStreamConfigError>;

    /// The default output stream format for the device.
    fn default_output_config(&self) -> Result<SupportedStreamConfig, DefaultStreamConfigError>;

    /// Create an input stream.
    ///
    /// # Parameters
    ///
    /// * `config` - The stream configuration including sample rate, channels, and buffer size.
    /// * `data_callback` - Called periodically with captured audio data. The callback receives
    ///   a slice of samples in the format `T` and timing information.
    /// * `error_callback` - Called when a stream error occurs (e.g., device disconnected).
    /// * `timeout` - Optional timeout for backend operations. `None` indicates blocking behavior,
    ///   `Some(duration)` sets a maximum wait time. Not all backends support timeouts.
    fn build_input_stream<T, D, E>(
        &self,
        config: StreamConfig,
        mut data_callback: D,
        error_callback: E,
        timeout: Option<Duration>,
    ) -> Result<Self::Stream, BuildStreamError>
    where
        T: SizedSample,
        D: FnMut(&[T], &InputCallbackInfo) + Send + 'static,
        E: FnMut(StreamError) + Send + 'static,
    {
        self.build_input_stream_raw(
            config,
            T::FORMAT,
            move |data, info| {
                data_callback(
                    data.as_slice()
                        .expect("host supplied incorrect sample type"),
                    info,
                )
            },
            error_callback,
            timeout,
        )
    }

    /// Create an output stream.
    ///
    /// # Parameters
    ///
    /// * `config` - The stream configuration including sample rate, channels, and buffer size.
    /// * `data_callback` - Called periodically to fill the output buffer. The callback receives
    ///   a mutable slice of samples in the format `T` to be filled with audio data, along with
    ///   timing information.
    /// * `error_callback` - Called when a stream error occurs (e.g., device disconnected).
    /// * `timeout` - Optional timeout for backend operations. `None` indicates blocking behavior,
    ///   `Some(duration)` sets a maximum wait time. Not all backends support timeouts.
    fn build_output_stream<T, D, E>(
        &self,
        config: StreamConfig,
        mut data_callback: D,
        error_callback: E,
        timeout: Option<Duration>,
    ) -> Result<Self::Stream, BuildStreamError>
    where
        T: SizedSample,
        D: FnMut(&mut [T], &OutputCallbackInfo) + Send + 'static,
        E: FnMut(StreamError) + Send + 'static,
    {
        self.build_output_stream_raw(
            config,
            T::FORMAT,
            move |data, info| {
                data_callback(
                    data.as_slice_mut()
                        .expect("host supplied incorrect sample type"),
                    info,
                )
            },
            error_callback,
            timeout,
        )
    }

    /// Create a dynamically typed input stream.
    ///
    /// This method allows working with sample data as raw bytes, useful when the sample
    /// format is determined at runtime. For compile-time known formats, prefer
    /// [`build_input_stream`](Self::build_input_stream).
    ///
    /// # Parameters
    ///
    /// * `config` - The stream configuration including sample rate, channels, and buffer size.
    /// * `sample_format` - The sample format of the audio data.
    /// * `data_callback` - Called periodically with captured audio data as a [`Data`] buffer.
    /// * `error_callback` - Called when a stream error occurs (e.g., device disconnected).
    /// * `timeout` - Optional timeout for backend operations. `None` indicates blocking behavior,
    ///   `Some(duration)` sets a maximum wait time. Not all backends support timeouts.
    fn build_input_stream_raw<D, E>(
        &self,
        config: StreamConfig,
        sample_format: SampleFormat,
        data_callback: D,
        error_callback: E,
        timeout: Option<Duration>,
    ) -> Result<Self::Stream, BuildStreamError>
    where
        D: FnMut(&Data, &InputCallbackInfo) + Send + 'static,
        E: FnMut(StreamError) + Send + 'static;

    /// Create a dynamically typed output stream.
    ///
    /// This method allows working with sample data as raw bytes, useful when the sample
    /// format is determined at runtime. For compile-time known formats, prefer
    /// [`build_output_stream`](Self::build_output_stream).
    ///
    /// # Parameters
    ///
    /// * `config` - The stream configuration including sample rate, channels, and buffer size.
    /// * `sample_format` - The sample format of the audio data.
    /// * `data_callback` - Called periodically to fill the output buffer with audio data as
    ///   a mutable [`Data`] buffer.
    /// * `error_callback` - Called when a stream error occurs (e.g., device disconnected).
    /// * `timeout` - Optional timeout for backend operations. `None` indicates blocking behavior,
    ///   `Some(duration)` sets a maximum wait time. Not all backends support timeouts.
    fn build_output_stream_raw<D, E>(
        &self,
        config: StreamConfig,
        sample_format: SampleFormat,
        data_callback: D,
        error_callback: E,
        timeout: Option<Duration>,
    ) -> Result<Self::Stream, BuildStreamError>
    where
        D: FnMut(&mut Data, &OutputCallbackInfo) + Send + 'static,
        E: FnMut(StreamError) + Send + 'static;
}

/// A stream created from [`Device`](DeviceTrait), with methods to control playback.
pub trait StreamTrait {
    /// Run the stream.
    ///
    /// Note: Not all platforms automatically run the stream upon creation, so it is important to
    /// call `play` after creation if it is expected that the stream should run immediately.
    fn play(&self) -> Result<(), PlayStreamError>;

    /// Some devices support pausing the audio stream. This can be useful for saving energy in
    /// moments of silence.
    ///
    /// Note: Not all devices support suspending the stream at the hardware level. This method may
    /// fail in these cases.
    fn pause(&self) -> Result<(), PauseStreamError>;

    /// Query the stream's buffer size in frames per callback invocation.
    ///
    /// Returns the platform's best estimate of the number of frames per callback.
    ///
    /// - [`crate::BufferSize::Fixed`]: the actual callback size after hardware negotiation, which may
    ///   differ from the requested value due to hardware constraints.
    /// - [`crate::BufferSize::Default`]: the system-configured callback size (e.g. ALSA period,
    ///   JACK buffer size, AAudio burst size). This reflects the typical callback size, not a
    ///   guaranteed upper bound.
    ///
    /// Returns `None` if the platform cannot report a meaningful estimate — for example, before
    /// the first callback has fired, or on platforms that do not expose this information.
    ///
    /// Applications should use this value to size pre-allocated buffers or estimate latency, but
    /// must always use the actual frame count passed to each individual callback invocation.
    fn buffer_size(&self) -> Option<crate::FrameCount> {
        None
    }
}

/// Compile-time assertion that a stream type implements [`Send`].
///
/// Custom host implementations should use this macro to verify their `Stream` type
/// can be safely transferred between threads, as required by CPAL's API.
///
/// # Example
///
/// ```
/// use cpal::assert_stream_send;
/// struct MyStream { /* ... */ }
/// assert_stream_send!(MyStream);
/// ```
#[macro_export]
macro_rules! assert_stream_send {
    ($t:ty) => {
        const fn _assert_stream_send<T: Send>() {}
        const _: () = _assert_stream_send::<$t>();
    };
}

/// Compile-time assertion that a stream type implements [`Sync`].
///
/// Custom host implementations should use this macro to verify their `Stream` type
/// can be safely shared between threads, as required by CPAL's API.
///
/// # Example
///
/// ```
/// use cpal::assert_stream_sync;
/// struct MyStream { /* ... */ }
/// assert_stream_sync!(MyStream);
/// ```
#[macro_export]
macro_rules! assert_stream_sync {
    ($t:ty) => {
        const fn _assert_stream_sync<T: Sync>() {}
        const _: () = _assert_stream_sync::<$t>();
    };
}
```

## File: `src/host/com.rs`
```rust
//! Handles COM initialization and cleanup.

use std::io::Error as IoError;
use std::marker::PhantomData;

use windows::Win32::Foundation::RPC_E_CHANGED_MODE;
use windows::Win32::System::Com::{CoInitializeEx, CoUninitialize, COINIT_APARTMENTTHREADED};

thread_local!(static COM_INITIALIZED: ComInitialized = {
    unsafe {
        // Try to initialize COM with STA by default to avoid compatibility issues with the ASIO
        // backend (where CoInitialize() is called by the ASIO SDK) or winit (where drag and drop
        // requires STA).
        // This call can fail with RPC_E_CHANGED_MODE if another library initialized COM with MTA.
        // That's OK though since COM ensures thread-safety/compatibility through marshalling when
        // necessary.
        let result = CoInitializeEx(None, COINIT_APARTMENTTHREADED);
        if result.is_ok() || result == RPC_E_CHANGED_MODE {
            ComInitialized {
                result,
                _ptr: PhantomData,
            }
        } else {
            // COM initialization failed in another way, something is really wrong.
            panic!(
                "Failed to initialize COM: {}",
                IoError::from_raw_os_error(result.0)
            );
        }
    }
});

/// RAII object that guards the fact that COM is initialized.
///
// We store a raw pointer because it's the only way at the moment to remove `Send`/`Sync` from the
// object.
struct ComInitialized {
    result: windows::core::HRESULT,
    _ptr: PhantomData<*mut ()>,
}

impl Drop for ComInitialized {
    fn drop(&mut self) {
        // Need to avoid calling CoUninitialize() if CoInitializeEx failed since it may have
        // returned RPC_E_MODE_CHANGED - which is OK, see above.
        if self.result.is_ok() {
            unsafe { CoUninitialize() };
        }
    }
}

/// Ensures that COM is initialized in this thread.
#[inline]
pub fn com_initialized() {
    COM_INITIALIZED.with(|_| {});
}
```

## File: `src/host/mod.rs`
```rust
use crate::{Sample, SampleFormat, I24, U24};

#[cfg(target_os = "android")]
pub(crate) mod aaudio;
#[cfg(any(
    target_os = "linux",
    target_os = "dragonfly",
    target_os = "freebsd",
    target_os = "netbsd"
))]
pub(crate) mod alsa;
#[cfg(all(windows, feature = "asio"))]
pub(crate) mod asio;
#[cfg(all(
    feature = "wasm-bindgen",
    feature = "audioworklet",
    target_feature = "atomics"
))]
pub(crate) mod audioworklet;
#[cfg(windows)]
pub(crate) mod com;
#[cfg(any(target_os = "macos", target_os = "ios"))]
pub(crate) mod coreaudio;
#[cfg(target_os = "emscripten")]
pub(crate) mod emscripten;
#[cfg(all(
    feature = "jack",
    any(
        target_os = "linux",
        target_os = "dragonfly",
        target_os = "freebsd",
        target_os = "netbsd",
        target_os = "macos",
        target_os = "windows",
    )
))]
pub(crate) mod jack;
#[cfg(all(
    any(
        target_os = "linux",
        target_os = "dragonfly",
        target_os = "freebsd",
        target_os = "netbsd",
    ),
    feature = "pipewire"
))]
pub(crate) mod pipewire;
#[cfg(all(
    any(
        target_os = "linux",
        target_os = "dragonfly",
        target_os = "freebsd",
        target_os = "netbsd"
    ),
    feature = "pulseaudio"
))]
pub(crate) mod pulseaudio;
#[cfg(windows)]
pub(crate) mod wasapi;
#[cfg(all(target_arch = "wasm32", feature = "wasm-bindgen"))]
pub(crate) mod webaudio;

#[cfg(feature = "custom")]
pub(crate) mod custom;
#[cfg(not(any(
    windows,
    target_os = "linux",
    target_os = "dragonfly",
    target_os = "freebsd",
    target_os = "netbsd",
    target_os = "macos",
    target_os = "ios",
    target_os = "emscripten",
    target_os = "android",
    all(target_arch = "wasm32", feature = "wasm-bindgen"),
)))]
pub(crate) mod null;

// Fill a buffer with equilibrium values for any sample format.
// Works with any buffer size, even if not perfectly aligned to sample boundaries.
#[allow(unused)]
pub(crate) fn fill_with_equilibrium(buffer: &mut [u8], sample_format: SampleFormat) {
    macro_rules! fill_typed {
        ($sample_type:ty) => {{
            let sample_size = std::mem::size_of::<$sample_type>();

            debug_assert_eq!(
                buffer.len() % sample_size,
                0,
                "Buffer size must be aligned to sample size for format {:?}",
                sample_format
            );

            let num_samples = buffer.len() / sample_size;
            let equilibrium = <$sample_type as Sample>::EQUILIBRIUM;

            // Safety: We verified the buffer size is correctly aligned for the sample type
            let samples = unsafe {
                std::slice::from_raw_parts_mut(
                    buffer.as_mut_ptr() as *mut $sample_type,
                    num_samples,
                )
            };

            for sample in samples {
                *sample = equilibrium;
            }
        }};
    }
    const DSD_SILENCE_BYTE: u8 = 0x69;

    match sample_format {
        SampleFormat::I8 => fill_typed!(i8),
        SampleFormat::I16 => fill_typed!(i16),
        SampleFormat::I24 => fill_typed!(I24),
        SampleFormat::I32 => fill_typed!(i32),
        // SampleFormat::I48 => fill_typed!(I48),
        SampleFormat::I64 => fill_typed!(i64),
        SampleFormat::U8 => fill_typed!(u8),
        SampleFormat::U16 => fill_typed!(u16),
        SampleFormat::U24 => fill_typed!(U24),
        SampleFormat::U32 => fill_typed!(u32),
        // SampleFormat::U48 => fill_typed!(U48),
        SampleFormat::U64 => fill_typed!(u64),
        SampleFormat::F32 => fill_typed!(f32),
        SampleFormat::F64 => fill_typed!(f64),
        SampleFormat::DsdU8 | SampleFormat::DsdU16 | SampleFormat::DsdU32 => {
            buffer.fill(DSD_SILENCE_BYTE)
        }
    }
}
```

## File: `src/host/aaudio/convert.rs`
```rust
use std::convert::TryInto;
use std::time::Duration;

extern crate ndk;

use crate::{
    BackendSpecificError, BuildStreamError, PauseStreamError, PlayStreamError, StreamError,
    StreamInstant,
};

pub fn to_stream_instant(duration: Duration) -> StreamInstant {
    StreamInstant::new(
        duration.as_secs().try_into().unwrap(),
        duration.subsec_nanos(),
    )
}

pub fn stream_instant(stream: &ndk::audio::AudioStream) -> StreamInstant {
    let ts = stream
        .timestamp(ndk::audio::Clockid::Monotonic)
        .unwrap_or(ndk::audio::Timestamp {
            frame_position: 0,
            time_nanoseconds: 0,
        });
    to_stream_instant(Duration::from_nanos(ts.time_nanoseconds as u64))
}

impl From<ndk::audio::AudioError> for StreamError {
    fn from(error: ndk::audio::AudioError) -> Self {
        use self::ndk::audio::AudioError::*;
        match error {
            Disconnected | Unavailable => Self::DeviceNotAvailable,
            e => (BackendSpecificError {
                description: e.to_string(),
            })
            .into(),
        }
    }
}

impl From<ndk::audio::AudioError> for PlayStreamError {
    fn from(error: ndk::audio::AudioError) -> Self {
        use self::ndk::audio::AudioError::*;
        match error {
            Disconnected | Unavailable => Self::DeviceNotAvailable,
            e => (BackendSpecificError {
                description: e.to_string(),
            })
            .into(),
        }
    }
}

impl From<ndk::audio::AudioError> for PauseStreamError {
    fn from(error: ndk::audio::AudioError) -> Self {
        use self::ndk::audio::AudioError::*;
        match error {
            Disconnected | Unavailable => Self::DeviceNotAvailable,
            e => (BackendSpecificError {
                description: e.to_string(),
            })
            .into(),
        }
    }
}

impl From<ndk::audio::AudioError> for BuildStreamError {
    fn from(error: ndk::audio::AudioError) -> Self {
        use self::ndk::audio::AudioError::*;
        match error {
            Disconnected | Unavailable => Self::DeviceNotAvailable,
            NoFreeHandles => Self::StreamIdOverflow,
            InvalidFormat | InvalidRate => Self::StreamConfigNotSupported,
            IllegalArgument => Self::InvalidArgument,
            e => (BackendSpecificError {
                description: e.to_string(),
            })
            .into(),
        }
    }
}
```

## File: `src/host/aaudio/java_interface.rs`
```rust
mod audio_features;
mod audio_manager;
mod definitions;
mod devices_info;
mod utils;

pub use self::definitions::*;
```

## File: `src/host/aaudio/mod.rs`
```rust
//! AAudio backend implementation.
//!
//! Default backend on Android.

use std::cmp;
use std::convert::TryInto;
use std::sync::atomic::{AtomicI32, Ordering};
use std::sync::{Arc, Mutex};
use std::time::{Duration, Instant};
use std::vec::IntoIter as VecIntoIter;

extern crate ndk;

use convert::{stream_instant, to_stream_instant};
use java_interface::{AudioDeviceInfo, AudioManager};

use crate::traits::{DeviceTrait, HostTrait, StreamTrait};
use crate::{
    BackendSpecificError, BufferSize, BuildStreamError, Data, DefaultStreamConfigError,
    DeviceDescription, DeviceDescriptionBuilder, DeviceDirection, DeviceId, DeviceIdError,
    DeviceNameError, DeviceType, DevicesError, InputCallbackInfo, InputStreamTimestamp,
    InterfaceType, OutputCallbackInfo, OutputStreamTimestamp, PauseStreamError, PlayStreamError,
    SampleFormat, StreamConfig, StreamError, SupportedBufferSize, SupportedStreamConfig,
    SupportedStreamConfigRange, SupportedStreamConfigsError,
};

mod convert;
mod java_interface;

use self::ndk::audio::AudioStream;
use java_interface::AudioDeviceType as AndroidDeviceType;

impl From<AndroidDeviceType> for DeviceType {
    fn from(device_type: AndroidDeviceType) -> Self {
        match device_type {
            AndroidDeviceType::BuiltinSpeaker
            | AndroidDeviceType::BuiltinSpeakerSafe
            | AndroidDeviceType::BleSpeaker => DeviceType::Speaker,

            AndroidDeviceType::BuiltinMic => DeviceType::Microphone,

            AndroidDeviceType::WiredHeadphones => DeviceType::Headphones,

            AndroidDeviceType::WiredHeadset
            | AndroidDeviceType::UsbHeadset
            | AndroidDeviceType::BleHeadset
            | AndroidDeviceType::BluetoothSCO => DeviceType::Headset,

            AndroidDeviceType::BuiltinEarpiece => DeviceType::Earpiece,

            AndroidDeviceType::HearingAid => DeviceType::HearingAid,

            AndroidDeviceType::Dock => DeviceType::Dock,

            AndroidDeviceType::Fm | AndroidDeviceType::FmTuner | AndroidDeviceType::TvTuner => {
                DeviceType::Tuner
            }

            AndroidDeviceType::RemoteSubmix => DeviceType::Virtual,

            _ => DeviceType::Unknown,
        }
    }
}

impl From<AndroidDeviceType> for InterfaceType {
    fn from(device_type: AndroidDeviceType) -> Self {
        match device_type {
            AndroidDeviceType::UsbDevice
            | AndroidDeviceType::UsbAccessory
            | AndroidDeviceType::UsbHeadset => InterfaceType::Usb,

            AndroidDeviceType::BluetoothA2DP
            | AndroidDeviceType::BluetoothSCO
            | AndroidDeviceType::BleHeadset
            | AndroidDeviceType::BleSpeaker
            | AndroidDeviceType::BleBroadcast => InterfaceType::Bluetooth,

            AndroidDeviceType::Hdmi | AndroidDeviceType::HdmiArc | AndroidDeviceType::HdmiEarc => {
                InterfaceType::Hdmi
            }

            AndroidDeviceType::LineAnalog
            | AndroidDeviceType::LineDigital
            | AndroidDeviceType::AuxLine => InterfaceType::Line,

            AndroidDeviceType::BuiltinEarpiece
            | AndroidDeviceType::BuiltinMic
            | AndroidDeviceType::BuiltinSpeaker
            | AndroidDeviceType::BuiltinSpeakerSafe => InterfaceType::BuiltIn,

            AndroidDeviceType::Ip => InterfaceType::Network,

            AndroidDeviceType::RemoteSubmix => InterfaceType::Virtual,

            _ => InterfaceType::Unknown,
        }
    }
}

// constants from android.media.AudioFormat
const CHANNEL_OUT_MONO: i32 = 4;
const CHANNEL_OUT_STEREO: i32 = 12;

// Android Java API supports up to 8 channels
// TODO: more channels available in native AAudio
// Maps channel masks to their corresponding channel counts
const CHANNEL_CONFIGS: [(i32, u16); 2] = [(CHANNEL_OUT_MONO, 1), (CHANNEL_OUT_STEREO, 2)];

const SAMPLE_RATES: [i32; 15] = [
    5512, 8000, 11025, 12000, 16000, 22050, 24000, 32000, 44100, 48000, 64000, 88200, 96000,
    176_400, 192_000,
];

/// The same default for blocking operations as Oboe uses
const DEFAULT_TIMEOUT_NANOS: i64 = 2_000_000_000;

pub struct Host;
#[derive(Clone)]
pub struct Device(Option<AudioDeviceInfo>);

/// Stream wraps AudioStream in Arc<Mutex<>> to provide Send + Sync semantics.
///
/// While the underlying ndk::audio::AudioStream is neither Send nor Sync in ndk 0.9.0
/// (see https://developer.android.com/ndk/guides/audio/aaudio/aaudio#thread-safety),
/// we wrap it in a mutex to enable safe concurrent access and manually implement Send + Sync.
///
/// # Safety
///
/// This is safe because:
/// - AAudio functions are designed to be called from any thread (the Android docs state
///   "AAudio is not thread-safe" meaning it lacks internal locking, not that it's unsafe)
/// - Audio callbacks are called on a dedicated AAudio thread and don't access Stream
/// - The Mutex ensures exclusive access for control operations (play, pause)
/// - The pointer in AudioStream (NonNull<AAudioStreamStruct>) is valid for the lifetime
///   of the stream and AAudio C API functions are thread-safe at the C level
#[derive(Clone)]
pub struct Stream {
    inner: Arc<Mutex<AudioStream>>,
    direction: DeviceDirection,
}

// SAFETY: AudioStream can be safely sent between threads. The AAudio C API is thread-safe
// for moving stream ownership between threads. The NonNull pointer remains valid.
unsafe impl Send for Stream {}

// SAFETY: AudioStream can be safely shared between threads when protected by a Mutex.
// All operations on the stream go through the mutex, ensuring exclusive access.
unsafe impl Sync for Stream {}

// Compile-time assertion that Stream is Send and Sync
crate::assert_stream_send!(Stream);
crate::assert_stream_sync!(Stream);

/// State for dynamic buffer tuning on output streams.
#[derive(Default)]
struct BufferTuningState {
    previous_underrun_count: AtomicI32,
    capacity: AtomicI32,
    mixer_bursts: AtomicI32,
}

pub use crate::iter::{SupportedInputConfigs, SupportedOutputConfigs};
pub type Devices = std::vec::IntoIter<Device>;

impl Host {
    pub fn new() -> Result<Self, crate::HostUnavailable> {
        Ok(Host)
    }
}

impl HostTrait for Host {
    type Devices = Devices;
    type Device = Device;

    fn is_available() -> bool {
        true
    }

    fn devices(&self) -> Result<Self::Devices, DevicesError> {
        if let Ok(devices) = AudioDeviceInfo::request(DeviceDirection::Duplex) {
            Ok(devices
                .into_iter()
                .map(|d| Device(Some(d)))
                .collect::<Vec<_>>()
                .into_iter())
        } else {
            Ok(vec![Device(None)].into_iter())
        }
    }

    fn default_input_device(&self) -> Option<Self::Device> {
        Some(Device(None))
    }

    fn default_output_device(&self) -> Option<Self::Device> {
        Some(Device(None))
    }
}

fn buffer_size_range() -> SupportedBufferSize {
    if let Ok(min_buffer_size) = AudioManager::get_frames_per_buffer() {
        SupportedBufferSize::Range {
            min: min_buffer_size as u32,
            max: i32::MAX as u32,
        }
    } else {
        SupportedBufferSize::Unknown
    }
}

fn default_supported_configs() -> VecIntoIter<SupportedStreamConfigRange> {
    const FORMATS: [SampleFormat; 2] = [SampleFormat::I16, SampleFormat::F32];

    let buffer_size = buffer_size_range();
    let mut output = Vec::with_capacity(SAMPLE_RATES.len() * CHANNEL_CONFIGS.len() * FORMATS.len());
    for sample_format in &FORMATS {
        for (_channel_mask, channel_count) in &CHANNEL_CONFIGS {
            for sample_rate in &SAMPLE_RATES {
                output.push(SupportedStreamConfigRange {
                    channels: *channel_count,
                    min_sample_rate: *sample_rate as u32,
                    max_sample_rate: *sample_rate as u32,
                    buffer_size,
                    sample_format: *sample_format,
                });
            }
        }
    }

    output.into_iter()
}

fn device_supported_configs(device: &AudioDeviceInfo) -> VecIntoIter<SupportedStreamConfigRange> {
    let sample_rates = if !device.sample_rates.is_empty() {
        device.sample_rates.as_slice()
    } else {
        &SAMPLE_RATES
    };

    const ALL_CHANNELS: [i32; 2] = [1, 2];
    let channel_counts = if !device.channel_counts.is_empty() {
        device.channel_counts.as_slice()
    } else {
        &ALL_CHANNELS
    };

    const ALL_FORMATS: [SampleFormat; 2] = [SampleFormat::I16, SampleFormat::F32];
    let formats = if !device.formats.is_empty() {
        device.formats.as_slice()
    } else {
        &ALL_FORMATS
    };

    let buffer_size = buffer_size_range();
    let mut output = Vec::with_capacity(sample_rates.len() * channel_counts.len() * formats.len());
    for sample_rate in sample_rates {
        for channel_count in channel_counts {
            assert!(*channel_count > 0);
            if *channel_count > 2 {
                // could be supported by the device
                // TODO: more channels available in native AAudio
                continue;
            }
            for format in formats {
                output.push(SupportedStreamConfigRange {
                    channels: cmp::min(*channel_count as u16, 2u16),
                    min_sample_rate: *sample_rate as u32,
                    max_sample_rate: *sample_rate as u32,
                    buffer_size,
                    sample_format: *format,
                });
            }
        }
    }

    output.into_iter()
}

fn configure_for_device(
    builder: ndk::audio::AudioStreamBuilder,
    device: &Device,
    config: StreamConfig,
) -> ndk::audio::AudioStreamBuilder {
    let mut builder = if let Some(info) = &device.0 {
        builder.device_id(info.id)
    } else {
        builder
    };
    builder = builder.sample_rate(config.sample_rate.try_into().unwrap());

    // Following the pattern from Oboe and Google's AAudio, we let AAudio choose the optimal
    // callback size dynamically by default. See
    // - https://developer.android.com/ndk/reference/group/audio#aaudiostreambuilder_setframesperdatacallback
    // - https://developer.android.com/ndk/guides/audio/audio-latency#buffer-size
    if let BufferSize::Fixed(size) = config.buffer_size {
        // For fixed sizes, the user explicitly wants control over the callback size.
        builder = builder
            .frames_per_data_callback(size as i32)
            .buffer_capacity_in_frames(2 * size as i32);
    }

    builder
}

fn build_input_stream<D, E>(
    device: &Device,
    config: StreamConfig,
    mut data_callback: D,
    mut error_callback: E,
    builder: ndk::audio::AudioStreamBuilder,
    sample_format: SampleFormat,
) -> Result<Stream, BuildStreamError>
where
    D: FnMut(&Data, &InputCallbackInfo) + Send + 'static,
    E: FnMut(StreamError) + Send + 'static,
{
    let builder = configure_for_device(builder, device, config);
    let created = Instant::now();
    let channel_count = config.channels as i32;
    let stream = builder
        .data_callback(Box::new(move |stream, data, num_frames| {
            let cb_info = InputCallbackInfo {
                timestamp: InputStreamTimestamp {
                    callback: to_stream_instant(created.elapsed()),
                    capture: stream_instant(stream),
                },
            };
            (data_callback)(
                &unsafe {
                    Data::from_parts(
                        data as *mut _,
                        (num_frames * channel_count).try_into().unwrap(),
                        sample_format,
                    )
                },
                &cb_info,
            );
            ndk::audio::AudioCallbackResult::Continue
        }))
        .error_callback(Box::new(move |_stream, error| {
            (error_callback)(StreamError::from(error))
        }))
        .open_stream()?;

    // SAFETY: Stream implements Send + Sync (see unsafe impl below). Arc<Mutex<AudioStream>>
    // is safe because the Mutex provides exclusive access and AudioStream's thread safety
    // is documented in the AAudio C API.
    #[allow(clippy::arc_with_non_send_sync)]
    Ok(Stream {
        inner: Arc::new(Mutex::new(stream)),
        direction: DeviceDirection::Input,
    })
}

fn build_output_stream<D, E>(
    device: &Device,
    config: StreamConfig,
    mut data_callback: D,
    mut error_callback: E,
    builder: ndk::audio::AudioStreamBuilder,
    sample_format: SampleFormat,
) -> Result<Stream, BuildStreamError>
where
    D: FnMut(&mut Data, &OutputCallbackInfo) + Send + 'static,
    E: FnMut(StreamError) + Send + 'static,
{
    let builder = configure_for_device(builder, device, config);
    let created = Instant::now();
    let channel_count = config.channels as i32;
    let tune_dynamically = config.buffer_size == BufferSize::Default;

    let tuning = Arc::new(BufferTuningState::default());
    let tuning_for_callback = tuning.clone();

    let stream = builder
        .data_callback(Box::new(move |stream, data, num_frames| {
            // Deliver audio data to user callback
            let cb_info = OutputCallbackInfo {
                timestamp: OutputStreamTimestamp {
                    callback: to_stream_instant(created.elapsed()),
                    playback: stream_instant(stream),
                },
            };
            (data_callback)(
                &mut unsafe {
                    Data::from_parts(
                        data as *mut _,
                        (num_frames * channel_count).try_into().unwrap(),
                        sample_format,
                    )
                },
                &cb_info,
            );

            // Dynamic buffer tuning for output streams
            // See: https://developer.android.com/ndk/guides/audio/aaudio/aaudio#tuning-buffers
            if tune_dynamically {
                let underrun_count = stream.x_run_count();
                let previous = tuning_for_callback
                    .previous_underrun_count
                    .load(Ordering::Relaxed);

                if underrun_count > previous {
                    // The number of frames per burst can vary dynamically
                    let mut burst_size = stream.frames_per_burst();
                    if burst_size <= 0 {
                        burst_size = 256; // fallback from AAudio documentation
                    } else if burst_size < 16 {
                        burst_size = 16; // floor from Oboe
                    }

                    let new_mixer_bursts = tuning_for_callback
                        .mixer_bursts
                        .load(Ordering::Relaxed)
                        .saturating_add(1);
                    let mut buffer_size = burst_size * new_mixer_bursts;

                    let buffer_capacity = tuning_for_callback.capacity.load(Ordering::Relaxed);
                    if buffer_size > buffer_capacity {
                        buffer_size = buffer_capacity;
                    }

                    if stream.set_buffer_size_in_frames(buffer_size).is_ok() {
                        tuning_for_callback
                            .mixer_bursts
                            .store(new_mixer_bursts, Ordering::Relaxed);
                    }

                    tuning_for_callback
                        .previous_underrun_count
                        .store(underrun_count, Ordering::Relaxed);
                }
            }

            ndk::audio::AudioCallbackResult::Continue
        }))
        .error_callback(Box::new(move |_stream, error| {
            (error_callback)(StreamError::from(error))
        }))
        .open_stream()?;

    // After stream opens, query and cache the values
    let capacity = stream.buffer_capacity_in_frames();
    tuning.capacity.store(capacity, Ordering::Relaxed);

    let mixer_bursts = match AudioManager::get_mixer_bursts() {
        Ok(bursts) => bursts.max(0),
        Err(_) => {
            let burst_size = stream.frames_per_burst();
            if burst_size > 0 {
                stream.buffer_size_in_frames() / burst_size
            } else {
                0 // defer to dynamic tuning
            }
        }
    };
    tuning.mixer_bursts.store(mixer_bursts, Ordering::Relaxed);

    // SAFETY: Stream implements Send + Sync (see unsafe impl below). Arc<Mutex<AudioStream>>
    // is safe because the Mutex provides exclusive access and AudioStream's thread safety
    // is documented in the AAudio C API.
    #[allow(clippy::arc_with_non_send_sync)]
    Ok(Stream {
        inner: Arc::new(Mutex::new(stream)),
        direction: DeviceDirection::Output,
    })
}

impl DeviceTrait for Device {
    type SupportedInputConfigs = SupportedInputConfigs;
    type SupportedOutputConfigs = SupportedOutputConfigs;
    type Stream = Stream;

    fn name(&self) -> Result<String, DeviceNameError> {
        match &self.0 {
            None => Ok("default".to_string()),
            Some(info) => {
                let name = if info.address.is_empty() {
                    format!("{}:{:?}", info.product_name, info.device_type)
                } else {
                    format!(
                        "{}:{:?}:{}",
                        info.product_name, info.device_type, info.address
                    )
                };
                Ok(name)
            }
        }
    }

    fn description(&self) -> Result<DeviceDescription, DeviceNameError> {
        match &self.0 {
            None => Ok(DeviceDescriptionBuilder::new("Default Device".to_string()).build()),
            Some(info) => {
                let device_type: DeviceType = info.device_type.into();
                let name = match device_type {
                    DeviceType::Unknown => info.product_name.clone(),
                    _ => format!("{} ({})", info.product_name, device_type),
                };
                let mut builder = DeviceDescriptionBuilder::new(name)
                    .device_type(device_type)
                    .interface_type(info.device_type.into())
                    .direction(info.direction);

                // Add address if not empty
                if !info.address.is_empty() {
                    builder = builder.address(info.address.clone());
                }

                Ok(builder.build())
            }
        }
    }

    fn id(&self) -> Result<DeviceId, DeviceIdError> {
        let device_str = match &self.0 {
            None => "-1".to_string(), // Default device
            Some(info) => info.id.to_string(),
        };
        Ok(DeviceId(crate::platform::HostId::AAudio, device_str))
    }

    fn supported_input_configs(
        &self,
    ) -> Result<Self::SupportedInputConfigs, SupportedStreamConfigsError> {
        if let Some(info) = &self.0 {
            // Output-only devices do not support input
            if matches!(info.direction, DeviceDirection::Output) {
                return Err(SupportedStreamConfigsError::BackendSpecific {
                    err: BackendSpecificError {
                        description: "output-only device does not support input".to_string(),
                    },
                });
            }
            Ok(device_supported_configs(info))
        } else {
            Ok(default_supported_configs())
        }
    }

    fn supported_output_configs(
        &self,
    ) -> Result<Self::SupportedOutputConfigs, SupportedStreamConfigsError> {
        if let Some(info) = &self.0 {
            // Input-only devices do not support output
            if matches!(info.direction, DeviceDirection::Input) {
                return Err(SupportedStreamConfigsError::BackendSpecific {
                    err: BackendSpecificError {
                        description: "input-only device does not support output".to_string(),
                    },
                });
            }
            Ok(device_supported_configs(info))
        } else {
            Ok(default_supported_configs())
        }
    }

    fn default_input_config(&self) -> Result<SupportedStreamConfig, DefaultStreamConfigError> {
        let mut configs: Vec<_> = self.supported_input_configs().unwrap().collect();
        configs.sort_by(|a, b| b.cmp_default_heuristics(a));
        let config = configs
            .into_iter()
            .next()
            .ok_or(DefaultStreamConfigError::StreamTypeNotSupported)?
            .with_max_sample_rate();
        Ok(config)
    }

    fn default_output_config(&self) -> Result<SupportedStreamConfig, DefaultStreamConfigError> {
        let mut configs: Vec<_> = self.supported_output_configs().unwrap().collect();
        configs.sort_by(|a, b| b.cmp_default_heuristics(a));
        let config = configs
            .into_iter()
            .next()
            .ok_or(DefaultStreamConfigError::StreamTypeNotSupported)?
            .with_max_sample_rate();
        Ok(config)
    }

    fn build_input_stream_raw<D, E>(
        &self,
        config: StreamConfig,
        sample_format: SampleFormat,
        data_callback: D,
        error_callback: E,
        _timeout: Option<Duration>,
    ) -> Result<Self::Stream, BuildStreamError>
    where
        D: FnMut(&Data, &InputCallbackInfo) + Send + 'static,
        E: FnMut(StreamError) + Send + 'static,
    {
        let format = match sample_format {
            SampleFormat::I16 => ndk::audio::AudioFormat::PCM_I16,
            SampleFormat::F32 => ndk::audio::AudioFormat::PCM_Float,
            sample_format => {
                return Err(BackendSpecificError {
                    description: format!("{} format is not supported on Android.", sample_format),
                }
                .into())
            }
        };
        let channel_count = match config.channels {
            1 => 1,
            2 => 2,
            channels => {
                // TODO: more channels available in native AAudio
                return Err(BackendSpecificError {
                    description: format!(
                        "{} channels are not supported yet (only 1 or 2).",
                        channels
                    ),
                }
                .into());
            }
        };

        let builder = ndk::audio::AudioStreamBuilder::new()?
            .direction(ndk::audio::AudioDirection::Input)
            .channel_count(channel_count)
            .format(format);

        build_input_stream(
            self,
            config,
            data_callback,
            error_callback,
            builder,
            sample_format,
        )
    }

    fn build_output_stream_raw<D, E>(
        &self,
        config: StreamConfig,
        sample_format: SampleFormat,
        data_callback: D,
        error_callback: E,
        _timeout: Option<Duration>,
    ) -> Result<Self::Stream, BuildStreamError>
    where
        D: FnMut(&mut Data, &OutputCallbackInfo) + Send + 'static,
        E: FnMut(StreamError) + Send + 'static,
    {
        let format = match sample_format {
            SampleFormat::I16 => ndk::audio::AudioFormat::PCM_I16,
            SampleFormat::F32 => ndk::audio::AudioFormat::PCM_Float,
            sample_format => {
                return Err(BackendSpecificError {
                    description: format!("{} format is not supported on Android.", sample_format),
                }
                .into())
            }
        };
        let channel_count = match config.channels {
            1 => 1,
            2 => 2,
            channels => {
                // TODO: more channels available in native AAudio
                return Err(BackendSpecificError {
                    description: format!(
                        "{} channels are not supported yet (only 1 or 2).",
                        channels
                    ),
                }
                .into());
            }
        };

        let builder = ndk::audio::AudioStreamBuilder::new()?
            .direction(ndk::audio::AudioDirection::Output)
            .channel_count(channel_count)
            .format(format);

        build_output_stream(
            self,
            config,
            data_callback,
            error_callback,
            builder,
            sample_format,
        )
    }
}

impl StreamTrait for Stream {
    fn play(&self) -> Result<(), PlayStreamError> {
        let stream = self.inner.lock().unwrap();

        stream.request_start().map_err(PlayStreamError::from)?;
        stream
            .wait_for_state_change(
                ndk::audio::AudioStreamState::Starting,
                DEFAULT_TIMEOUT_NANOS,
            )
            .map(|_| ())
            .map_err(PlayStreamError::from)
    }

    fn pause(&self) -> Result<(), PauseStreamError> {
        match self.direction {
            DeviceDirection::Output => {
                let stream = self.inner.lock().unwrap();

                stream.request_pause().map_err(PauseStreamError::from)?;
                stream
                    .wait_for_state_change(
                        ndk::audio::AudioStreamState::Pausing,
                        DEFAULT_TIMEOUT_NANOS,
                    )
                    .map(|_| ())
                    .map_err(PauseStreamError::from)
            }
            _ => Err(BackendSpecificError {
                description: "Pause only supported on output streams.".to_owned(),
            }
            .into()),
        }
    }

    fn buffer_size(&self) -> Option<crate::FrameCount> {
        let stream = self.inner.lock().ok()?;

        // frames_per_data_callback is only set for BufferSize::Fixed; for Default AAudio
        // schedules callbacks at the burst size, so that is the best available estimate.
        let frames = match stream.frames_per_data_callback() {
            Some(size) if size > 0 => size,
            _ => stream.frames_per_burst(),
        };
        if frames > 0 {
            Some(frames as crate::FrameCount)
        } else {
            None
        }
    }
}
```

## File: `src/host/aaudio/java_interface/audio_features.rs`
```rust
use super::{
    utils::{
        get_context, get_package_manager, has_system_feature, with_attached, JNIEnv, JObject,
        JResult,
    },
    PackageManager,
};

/**
 * The Android audio features
 */
#[derive(Debug, Clone, Copy, PartialEq, Eq, Hash)]
pub enum AudioFeature {
    LowLatency,
    Output,
    Pro,
    Microphone,
    Midi,
}

impl From<AudioFeature> for &'static str {
    fn from(feature: AudioFeature) -> Self {
        use AudioFeature::*;
        match feature {
            LowLatency => PackageManager::FEATURE_AUDIO_LOW_LATENCY,
            Output => PackageManager::FEATURE_AUDIO_OUTPUT,
            Pro => PackageManager::FEATURE_AUDIO_PRO,
            Microphone => PackageManager::FEATURE_MICROPHONE,
            Midi => PackageManager::FEATURE_MIDI,
        }
    }
}

impl AudioFeature {
    /**
     * Check availability of an audio feature using Android Java API
     */
    pub fn has(&self) -> Result<bool, String> {
        let context = get_context();

        with_attached(context, |env, activity| {
            try_check_system_feature(env, &activity, (*self).into())
        })
        .map_err(|error| error.to_string())
    }
}

fn try_check_system_feature<'j>(
    env: &mut JNIEnv<'j>,
    activity: &JObject<'j>,
    feature: &str,
) -> JResult<bool> {
    let package_manager = get_package_manager(env, activity)?;

    has_system_feature(env, &package_manager, feature)
}
```

## File: `src/host/aaudio/java_interface/audio_manager.rs`
```rust
use super::{
    utils::{
        get_context, get_property, get_system_property, get_system_service, with_attached, JNIEnv,
        JObject, JResult,
    },
    AudioManager, Context,
};

impl AudioManager {
    /// Get the frames per buffer using Android Java API
    pub fn get_frames_per_buffer() -> Result<i32, String> {
        let context = get_context();

        with_attached(context, |env, context| get_frames_per_buffer(env, &context))
            .map_err(|error| error.to_string())
    }

    /// Get the AAudio mixer burst count from system property
    pub fn get_mixer_bursts() -> Result<i32, String> {
        let context = get_context();

        with_attached(context, |env, _context| get_mixer_bursts(env))
            .map_err(|error| error.to_string())
    }
}

fn get_frames_per_buffer<'j>(env: &mut JNIEnv<'j>, context: &JObject<'j>) -> JResult<i32> {
    let audio_manager = get_system_service(env, context, Context::AUDIO_SERVICE)?;

    let frames_per_buffer = get_property(
        env,
        &audio_manager,
        AudioManager::PROPERTY_OUTPUT_FRAMES_PER_BUFFER,
    )?;

    let frames_per_buffer_string = String::from(env.get_string(&frames_per_buffer)?);

    // TODO: Use jni::errors::Error::ParseFailed instead of jni::errors::Error::JniCall once jni > v0.21.1 is released
    frames_per_buffer_string
        .parse::<i32>()
        .map_err(|_| jni::errors::Error::JniCall(jni::errors::JniError::Unknown))
}

fn get_mixer_bursts<'j>(env: &mut JNIEnv<'j>) -> JResult<i32> {
    let mixer_bursts = get_system_property(env, "aaudio.mixer_bursts", "2")?;

    let mixer_bursts_string = String::from(env.get_string(&mixer_bursts)?);

    // TODO: Use jni::errors::Error::ParseFailed instead of jni::errors::Error::JniCall once jni > v0.21.1 is released
    mixer_bursts_string
        .parse::<i32>()
        .map_err(|_| jni::errors::Error::JniCall(jni::errors::JniError::Unknown))
}
```

## File: `src/host/aaudio/java_interface/definitions.rs`
```rust
use num_derive::FromPrimitive;

use crate::{DeviceDirection, SampleFormat};

pub(crate) struct Context;

impl Context {
    pub const AUDIO_SERVICE: &'static str = "audio";
}

pub(crate) struct PackageManager;

impl PackageManager {
    pub const FEATURE_AUDIO_LOW_LATENCY: &'static str = "android.hardware.audio.low_latency";
    pub const FEATURE_AUDIO_OUTPUT: &'static str = "android.hardware.audio.output";
    pub const FEATURE_AUDIO_PRO: &'static str = "android.hardware.audio.pro";
    pub const FEATURE_MICROPHONE: &'static str = "android.hardware.microphone";
    pub const FEATURE_MIDI: &'static str = "android.software.midi";
}

pub(crate) struct AudioManager;

impl AudioManager {
    pub const PROPERTY_OUTPUT_FRAMES_PER_BUFFER: &'static str =
        "android.media.property.OUTPUT_FRAMES_PER_BUFFER";

    pub const GET_DEVICES_INPUTS: i32 = 1 << 0;
    pub const GET_DEVICES_OUTPUTS: i32 = 1 << 1;
    pub const GET_DEVICES_ALL: i32 = Self::GET_DEVICES_INPUTS | Self::GET_DEVICES_OUTPUTS;
}

/**
 * The Android audio device info
 */
#[derive(Debug, Clone)]
pub struct AudioDeviceInfo {
    /**
     * Device identifier
     */
    pub id: i32,

    /**
     * The type of device
     */
    pub device_type: AudioDeviceType,

    /**
     * The device can be used for playback and/or capture
     */
    pub direction: DeviceDirection,

    /**
     * Device address
     */
    pub address: String,

    /**
     * Device product name
     */
    pub product_name: String,

    /**
     * Available channel configurations
     */
    pub channel_counts: Vec<i32>,

    /**
     * Supported sample rates
     */
    pub sample_rates: Vec<i32>,

    /**
     * Supported audio formats
     */
    pub formats: Vec<SampleFormat>,
}

/**
 * The type of audio device
 */
#[derive(Debug, Clone, Copy, FromPrimitive)]
#[non_exhaustive]
#[repr(i32)]
pub enum AudioDeviceType {
    Unknown = 0,
    AuxLine = 19,
    BleBroadcast = 30,
    BleHeadset = 26,
    BleSpeaker = 27,
    BluetoothA2DP = 8,
    BluetoothSCO = 7,
    BuiltinEarpiece = 1,
    BuiltinMic = 15,
    BuiltinSpeaker = 2,
    BuiltinSpeakerSafe = 24,
    Bus = 21,
    Dock = 13,
    Fm = 14,
    FmTuner = 16,
    Hdmi = 9,
    HdmiArc = 10,
    HdmiEarc = 29,
    HearingAid = 23,
    Ip = 20,
    LineAnalog = 5,
    LineDigital = 6,
    RemoteSubmix = 25,
    Telephony = 18,
    TvTuner = 17,
    UsbAccessory = 12,
    UsbDevice = 11,
    UsbHeadset = 22,
    WiredHeadphones = 4,
    WiredHeadset = 3,
    Unsupported = -1,
}

/// Converts DeviceDirection to Android AudioManager device flags.
pub(super) fn android_device_flags(direction: DeviceDirection) -> i32 {
    match direction {
        DeviceDirection::Input => AudioManager::GET_DEVICES_INPUTS,
        DeviceDirection::Output => AudioManager::GET_DEVICES_OUTPUTS,
        _ => AudioManager::GET_DEVICES_ALL,
    }
}

impl SampleFormat {
    pub(crate) const ENCODING_PCM_16BIT: i32 = 2;
    //pub(crate) const ENCODING_PCM_8BIT: i32 = 3;
    pub(crate) const ENCODING_PCM_FLOAT: i32 = 4;

    pub(crate) fn from_encoding(encoding: i32) -> Option<SampleFormat> {
        match encoding {
            SampleFormat::ENCODING_PCM_16BIT => Some(SampleFormat::I16),
            SampleFormat::ENCODING_PCM_FLOAT => Some(SampleFormat::F32),
            _ => None,
        }
    }
}
```

## File: `src/host/aaudio/java_interface/devices_info.rs`
```rust
use num_traits::FromPrimitive;

use crate::{DeviceDirection, SampleFormat};

use super::{
    android_device_flags,
    utils::{
        call_method_no_args_ret_bool, call_method_no_args_ret_char_sequence,
        call_method_no_args_ret_int, call_method_no_args_ret_int_array,
        call_method_no_args_ret_string, get_context, get_devices, get_system_service,
        with_attached, JNIEnv, JObject, JResult,
    },
    AudioDeviceInfo, AudioDeviceType, Context,
};

impl AudioDeviceInfo {
    /**
     * Request audio devices using Android Java API
     */
    pub fn request(direction: DeviceDirection) -> Result<Vec<AudioDeviceInfo>, String> {
        let context = get_context();

        with_attached(context, |env, context| {
            let sdk_version = env
                .get_static_field("android/os/Build$VERSION", "SDK_INT", "I")?
                .i()?;

            if sdk_version >= 23 {
                try_request_devices_info(env, &context, direction)
            } else {
                Err(jni::errors::Error::MethodNotFound {
                    name: "".into(),
                    sig: "".into(),
                })
            }
        })
        .map_err(|error| error.to_string())
    }
}

fn try_request_devices_info<'j>(
    env: &mut JNIEnv<'j>,
    context: &JObject<'j>,
    direction: DeviceDirection,
) -> JResult<Vec<AudioDeviceInfo>> {
    let audio_manager = get_system_service(env, context, Context::AUDIO_SERVICE)?;

    let devices = get_devices(env, &audio_manager, android_device_flags(direction))?;

    let length = env.get_array_length(&devices)?;

    (0..length)
        .map(|index| {
            let device = env.get_object_array_element(&devices, index)?;
            let id = call_method_no_args_ret_int(env, &device, "getId")?;
            let address = call_method_no_args_ret_string(env, &device, "getAddress")?;
            let address = String::from(env.get_string(&address)?);
            let product_name =
                call_method_no_args_ret_char_sequence(env, &device, "getProductName")?;
            let product_name = String::from(env.get_string(&product_name)?);
            let device_type =
                FromPrimitive::from_i32(call_method_no_args_ret_int(env, &device, "getType")?)
                    .unwrap_or(AudioDeviceType::Unsupported);

            let is_source = call_method_no_args_ret_bool(env, &device, "isSource")?;
            let is_sink = call_method_no_args_ret_bool(env, &device, "isSink")?;
            let direction = crate::device_description::direction_from_caps(is_source, is_sink);
            let channel_counts =
                call_method_no_args_ret_int_array(env, &device, "getChannelCounts")?;
            let sample_rates = call_method_no_args_ret_int_array(env, &device, "getSampleRates")?;
            let formats = call_method_no_args_ret_int_array(env, &device, "getEncodings")?
                .into_iter()
                .filter_map(SampleFormat::from_encoding)
                .collect::<Vec<_>>();

            Ok(AudioDeviceInfo {
                id,
                address,
                product_name,
                device_type,
                direction,
                channel_counts,
                sample_rates,
                formats,
            })
        })
        .collect::<Result<Vec<_>, _>>()
}
```

## File: `src/host/aaudio/java_interface/utils.rs`
```rust
use jni::sys::jobject;
use ndk_context::AndroidContext;
use std::sync::Arc;

pub use jni::Executor;

pub use jni::{
    errors::Result as JResult,
    objects::{JIntArray, JObject, JObjectArray, JString},
    JNIEnv, JavaVM,
};

pub fn get_context() -> AndroidContext {
    ndk_context::android_context()
}

pub fn with_attached<F, R>(context: AndroidContext, closure: F) -> JResult<R>
where
    for<'j> F: FnOnce(&mut JNIEnv<'j>, JObject<'j>) -> JResult<R>,
{
    let vm = Arc::new(unsafe { JavaVM::from_raw(context.vm().cast())? });
    let context = context.context();
    let context = unsafe { JObject::from_raw(context as jobject) };
    Executor::new(vm).with_attached(|env| closure(env, context))
}

pub fn call_method_no_args_ret_int_array<'j>(
    env: &mut JNIEnv<'j>,
    subject: &JObject<'j>,
    method: &str,
) -> JResult<Vec<i32>> {
    let array: JIntArray = env.call_method(subject, method, "()[I", &[])?.l()?.into();

    let length = env.get_array_length(&array)?;
    let mut values = Vec::with_capacity(length as usize);

    env.get_int_array_region(array, 0, values.as_mut())?;

    Ok(values)
}

pub fn call_method_no_args_ret_int<'j>(
    env: &mut JNIEnv<'j>,
    subject: &JObject<'j>,
    method: &str,
) -> JResult<i32> {
    env.call_method(subject, method, "()I", &[])?.i()
}

pub fn call_method_no_args_ret_bool<'j>(
    env: &mut JNIEnv<'j>,
    subject: &JObject<'j>,
    method: &str,
) -> JResult<bool> {
    env.call_method(subject, method, "()Z", &[])?.z()
}

pub fn call_method_no_args_ret_string<'j>(
    env: &mut JNIEnv<'j>,
    subject: &JObject<'j>,
    method: &str,
) -> JResult<JString<'j>> {
    Ok(env
        .call_method(subject, method, "()Ljava/lang/String;", &[])?
        .l()?
        .into())
}

pub fn call_method_no_args_ret_char_sequence<'j>(
    env: &mut JNIEnv<'j>,
    subject: &JObject<'j>,
    method: &str,
) -> JResult<JString<'j>> {
    let cseq = env
        .call_method(subject, method, "()Ljava/lang/CharSequence;", &[])?
        .l()?;

    Ok(env
        .call_method(&cseq, "toString", "()Ljava/lang/String;", &[])?
        .l()?
        .into())
}

pub fn call_method_string_arg_ret_bool<'j>(
    env: &mut JNIEnv<'j>,
    subject: &JObject<'j>,
    name: &str,
    arg: impl AsRef<str>,
) -> JResult<bool> {
    env.call_method(
        subject,
        name,
        "(Ljava/lang/String;)Z",
        &[(&env.new_string(arg)?).into()],
    )?
    .z()
}

pub fn call_method_string_arg_ret_string<'j>(
    env: &mut JNIEnv<'j>,
    subject: &JObject<'j>,
    name: &str,
    arg: impl AsRef<str>,
) -> JResult<JString<'j>> {
    Ok(env
        .call_method(
            subject,
            name,
            "(Ljava/lang/String;)Ljava/lang/String;",
            &[(&env.new_string(arg)?).into()],
        )?
        .l()?
        .into())
}

pub fn call_method_string_arg_ret_object<'j>(
    env: &mut JNIEnv<'j>,
    subject: &JObject<'j>,
    method: &str,
    arg: &str,
) -> JResult<JObject<'j>> {
    env.call_method(
        subject,
        method,
        "(Ljava/lang/String;)Ljava/lang/Object;",
        &[(&env.new_string(arg)?).into()],
    )?
    .l()
}

pub fn get_package_manager<'j>(
    env: &mut JNIEnv<'j>,
    subject: &JObject<'j>,
) -> JResult<JObject<'j>> {
    env.call_method(
        subject,
        "getPackageManager",
        "()Landroid/content/pm/PackageManager;",
        &[],
    )?
    .l()
}

pub fn has_system_feature<'j>(
    env: &mut JNIEnv<'j>,
    subject: &JObject<'j>,
    name: &str,
) -> JResult<bool> {
    call_method_string_arg_ret_bool(env, subject, "hasSystemFeature", name)
}

pub fn get_system_service<'j>(
    env: &mut JNIEnv<'j>,
    subject: &JObject<'j>,
    name: &str,
) -> JResult<JObject<'j>> {
    call_method_string_arg_ret_object(env, subject, "getSystemService", name)
}

pub fn get_property<'j>(
    env: &mut JNIEnv<'j>,
    subject: &JObject<'j>,
    name: &str,
) -> JResult<JString<'j>> {
    call_method_string_arg_ret_string(env, subject, "getProperty", name)
}

/// Read an Android system property
pub fn get_system_property<'j>(
    env: &mut JNIEnv<'j>,
    name: &str,
    default_value: &str,
) -> JResult<JString<'j>> {
    Ok(env
        .call_static_method(
            "android/os/SystemProperties",
            "get",
            "(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;",
            &[
                (&env.new_string(name)?).into(),
                (&env.new_string(default_value)?).into(),
            ],
        )?
        .l()?
        .into())
}

pub fn get_devices<'j>(
    env: &mut JNIEnv<'j>,
    subject: &JObject<'j>,
    flags: i32,
) -> JResult<JObjectArray<'j>> {
    env.call_method(
        subject,
        "getDevices",
        "(I)[Landroid/media/AudioDeviceInfo;",
        &[flags.into()],
    )?
    .l()
    .map(From::from)
}
```

## File: `src/host/alsa/enumerate.rs`
```rust
use std::collections::HashSet;

use super::{alsa, Device, Host};
use crate::{BackendSpecificError, DeviceDirection, DevicesError};

const HW_PREFIX: &str = "hw";
const PLUGHW_PREFIX: &str = "plughw";

/// Information about a physical device
struct PhysicalDevice {
    card_index: u32,
    card_name: Option<String>,
    device_index: u32,
    device_name: Option<String>,
    direction: DeviceDirection,
}

/// Iterator over available ALSA PCM devices (physical hardware and virtual/plugin devices).
pub type Devices = std::vec::IntoIter<Device>;

impl Host {
    /// Enumerates all available ALSA PCM devices (physical hardware and virtual/plugin devices).
    ///
    /// We enumerate both ALSA hints and physical devices because:
    /// - Hints provide virtual devices, user configs, and card-specific devices with metadata
    /// - Physical probing provides traditional numeric naming (hw:CARD=0,DEV=0) for compatibility
    pub(super) fn enumerate_devices(&self) -> Result<Devices, DevicesError> {
        let mut devices = Vec::new();
        let mut seen_pcm_ids = HashSet::new();

        let physical_devices = physical_devices();

        // Add all hint devices, including virtual devices
        if let Ok(hints) = alsa::device_name::HintIter::new_str(None, "pcm") {
            for hint in hints {
                if let Some(pcm_id) = hint.name {
                    // Per ALSA docs (https://alsa-project.org/alsa-doc/alsa-lib/group___hint.html),
                    // NULL IOID means both Input/Output. Whether a stream can actually open in a
                    // given direction can only be determined by attempting to open it.
                    let direction = hint.direction.map_or(DeviceDirection::Duplex, Into::into);
                    let device = Device {
                        pcm_id,
                        desc: hint.desc,
                        direction,
                        _context: self.inner.clone(),
                    };

                    seen_pcm_ids.insert(device.pcm_id.clone());
                    devices.push(device);
                }
            }
        }

        // Add hw:/plughw: for all physical devices with numeric index (traditional naming)
        for phys_dev in physical_devices {
            for prefix in [HW_PREFIX, PLUGHW_PREFIX] {
                let pcm_id = format!(
                    "{}:CARD={},DEV={}",
                    prefix, phys_dev.card_index, phys_dev.device_index
                );

                if seen_pcm_ids.insert(pcm_id.clone()) {
                    devices.push(Device {
                        pcm_id,
                        desc: Some(format_device_description(&phys_dev, prefix)),
                        direction: phys_dev.direction,
                        _context: self.inner.clone(),
                    });
                }
            }
        }

        Ok(devices.into_iter())
    }
}

/// Formats device description in ALSA style: "Card Name, Device Name\nPurpose"
fn format_device_description(phys_dev: &PhysicalDevice, prefix: &str) -> String {
    // "Card Name, Device Name" or variations
    let first_line = match (&phys_dev.card_name, &phys_dev.device_name) {
        (Some(card), Some(device)) => format!("{}, {}", card, device),
        (Some(card), None) => card.clone(),
        (None, Some(device)) => device.clone(),
        (None, None) => format!("Card {}", phys_dev.card_index),
    };

    // ALSA standard description
    let second_line = match prefix {
        HW_PREFIX => "Direct hardware device without any conversions",
        PLUGHW_PREFIX => "Hardware device with all software conversions",
        _ => "",
    };

    format!("{}\n{}", first_line, second_line)
}

fn physical_devices() -> Vec<PhysicalDevice> {
    let mut devices = Vec::new();
    for card in alsa::card::Iter::new().filter_map(Result::ok) {
        let card_index = card.get_index() as u32;
        let ctl = match alsa::Ctl::new(&format!("{}:{}", HW_PREFIX, card_index), false) {
            Ok(ctl) => ctl,
            Err(_) => continue,
        };
        let card_name = ctl
            .card_info()
            .ok()
            .and_then(|info| info.get_name().ok().map(|s| s.to_string()));

        for device_index in alsa::ctl::DeviceIter::new(&ctl) {
            let device_index = device_index as u32;
            let playback_info = ctl
                .pcm_info(device_index, 0, alsa::Direction::Playback)
                .ok();
            let capture_info = ctl.pcm_info(device_index, 0, alsa::Direction::Capture).ok();

            let (direction, device_name) = match (&playback_info, &capture_info) {
                (Some(p_info), Some(_c_info)) => (
                    DeviceDirection::Duplex,
                    p_info.get_name().ok().map(|s| s.to_string()),
                ),
                (Some(p_info), None) => (
                    DeviceDirection::Output,
                    p_info.get_name().ok().map(|s| s.to_string()),
                ),
                (None, Some(c_info)) => (
                    DeviceDirection::Input,
                    c_info.get_name().ok().map(|s| s.to_string()),
                ),
                (None, None) => {
                    // Device doesn't exist - skip
                    continue;
                }
            };

            let device_name = device_name.unwrap_or_else(|| format!("Device {}", device_index));
            devices.push(PhysicalDevice {
                card_index,
                card_name: card_name.clone(),
                device_index,
                device_name: Some(device_name),
                direction,
            });
        }
    }

    devices
}

impl From<alsa::Error> for DevicesError {
    fn from(err: alsa::Error) -> Self {
        let err: BackendSpecificError = err.into();
        err.into()
    }
}

impl From<alsa::Direction> for DeviceDirection {
    fn from(direction: alsa::Direction) -> Self {
        match direction {
            alsa::Direction::Playback => DeviceDirection::Output,
            alsa::Direction::Capture => DeviceDirection::Input,
        }
    }
}
```

## File: `src/host/alsa/mod.rs`
```rust
//! ALSA backend implementation.
//!
//! Default backend on Linux and BSD systems.

extern crate alsa;
extern crate libc;

use std::{
    cmp,
    sync::{
        atomic::{AtomicBool, AtomicUsize, Ordering},
        Arc,
    },
    thread::{self, JoinHandle},
    time::Duration,
    vec::IntoIter as VecIntoIter,
};

use self::alsa::poll::Descriptors;
pub use self::enumerate::Devices;

use crate::{
    host::fill_with_equilibrium,
    iter::{SupportedInputConfigs, SupportedOutputConfigs},
    traits::{DeviceTrait, HostTrait, StreamTrait},
    BackendSpecificError, BufferSize, BuildStreamError, ChannelCount, Data,
    DefaultStreamConfigError, DeviceDescription, DeviceDescriptionBuilder, DeviceDirection,
    DeviceId, DeviceIdError, DeviceNameError, DevicesError, FrameCount, InputCallbackInfo,
    OutputCallbackInfo, PauseStreamError, PlayStreamError, SampleFormat, SampleRate, StreamConfig,
    StreamError, SupportedBufferSize, SupportedStreamConfig, SupportedStreamConfigRange,
    SupportedStreamConfigsError,
};

mod enumerate;

// ALSA Buffer Size Behavior
// =========================
//
// ## ALSA Latency Model
//
// **Hardware vs Software Buffer**: ALSA maintains a software buffer in memory that feeds
// a hardware buffer in the audio device. Audio latency is determined by how much data
// sits in the software buffer before being transferred to hardware.
//
// **Period-Based Transfer**: ALSA transfers data in chunks called "periods". When one
// period worth of data has been consumed by hardware, ALSA triggers a callback to refill
// that period in the software buffer.
//
// ## BufferSize::Fixed Behavior
//
// When `BufferSize::Fixed(x)` is specified, cpal attempts to configure the period size
// to approximately `x` frames to achieve the requested callback size. However, the
// actual callback size may differ from the request:
//
// - ALSA may round the period size to hardware-supported values
// - Different devices have different period size constraints
// - The callback size is not guaranteed to exactly match the request
// - If the requested size cannot be accommodated, ALSA will choose the nearest
//   supported configuration
//
// This mirrors the behavior documented in the cpal API where `BufferSize::Fixed(x)`
// requests but does not guarantee a specific callback size.
//
// ## BufferSize::Default Behavior
//
// When `BufferSize::Default` is specified, cpal does NOT set explicit period size or
// period count constraints, allowing the device/driver to choose sensible defaults.
//
// **Why not set defaults?** Different audio systems have different behaviors:
//
// - **Native ALSA hardware**: Typically chooses reasonable defaults (e.g., 512-2048
//   frame periods with 2-4 periods)
//
// - **PipeWire-ALSA plugin**: Allocates a large ring buffer (~1M frames at 48kHz) but
//   uses small periods (512-1024 frames). Critically, if you request `set_periods(2)`
//   without specifying period size, PipeWire calculates period = buffer/2, resulting
//   in pathologically large periods (~524K frames = 10 seconds). See issues #1029 and
//   #1036.
//
// By not constraining period configuration, PipeWire-ALSA can use its optimized defaults
// (small periods with many-period buffer), while native ALSA hardware uses its own defaults.
//
// **Startup latency**: Regardless of buffer size, cpal uses double-buffering for startup
// (start_threshold = 2 periods), ensuring low latency even with large multi-period ring
// buffers.

const DEFAULT_DEVICE: &str = "default";

// Some ALSA plugins (e.g. alsaequal, certain USB drivers) are not reentrant.
static ALSA_OPEN_MUTEX: std::sync::Mutex<()> = std::sync::Mutex::new(());

// TODO: Not yet defined in rust-lang/libc crate
const LIBC_ENOTSUPP: libc::c_int = 524;

/// The default Linux and BSD host type.
#[derive(Debug, Clone)]
pub struct Host {
    inner: Arc<AlsaContext>,
}

impl Host {
    pub fn new() -> Result<Self, crate::HostUnavailable> {
        let inner = AlsaContext::new().map_err(|_| crate::HostUnavailable)?;
        Ok(Host {
            inner: Arc::new(inner),
        })
    }
}

impl HostTrait for Host {
    type Devices = Devices;
    type Device = Device;

    fn is_available() -> bool {
        // Assume ALSA is always available on Linux and BSD.
        true
    }

    fn devices(&self) -> Result<Self::Devices, DevicesError> {
        self.enumerate_devices()
    }

    fn device_by_id(&self, id: &crate::DeviceId) -> Option<Self::Device> {
        let canonical_id = crate::DeviceId(id.0, canonical_pcm_id(&id.1));
        self.devices()
            .ok()?
            .find(|d| d.id().ok().as_ref() == Some(&canonical_id))
    }

    fn default_input_device(&self) -> Option<Self::Device> {
        Some(Device::default())
    }

    fn default_output_device(&self) -> Option<Self::Device> {
        Some(Device::default())
    }
}

/// Global count of active ALSA context instances.
static ALSA_CONTEXT_COUNT: AtomicUsize = AtomicUsize::new(0);

/// ALSA backend context shared between `Host`, `Device`, and `Stream` via `Arc`.
#[derive(Debug)]
pub(super) struct AlsaContext;

impl AlsaContext {
    fn new() -> Result<Self, alsa::Error> {
        // Initialize global ALSA config cache on first context creation.
        if ALSA_CONTEXT_COUNT.fetch_add(1, Ordering::SeqCst) == 0 {
            alsa::config::update()?;
        }
        Ok(Self)
    }
}

impl Drop for AlsaContext {
    fn drop(&mut self) {
        // Free the global ALSA config cache when the last context is dropped.
        if ALSA_CONTEXT_COUNT.fetch_sub(1, Ordering::SeqCst) == 1 {
            let _ = alsa::config::update_free_global();
        }
    }
}

impl DeviceTrait for Device {
    type SupportedInputConfigs = SupportedInputConfigs;
    type SupportedOutputConfigs = SupportedOutputConfigs;
    type Stream = Stream;

    // ALSA overrides name() to return pcm_id directly instead of from description
    fn name(&self) -> Result<String, DeviceNameError> {
        Device::name(self)
    }

    fn description(&self) -> Result<DeviceDescription, DeviceNameError> {
        Device::description(self)
    }

    fn id(&self) -> Result<DeviceId, DeviceIdError> {
        Device::id(self)
    }

    // Override trait defaults to avoid opening devices during enumeration.
    //
    // ALSA does not guarantee transactional cleanup on failed snd_pcm_open(). Opening plugins like
    // alsaequal that fail with EPERM can leak FDs, poisoning the ALSA backend for the process
    // lifetime (subsequent device opens fail with EBUSY until process exit).
    fn supports_input(&self) -> bool {
        matches!(
            self.direction,
            DeviceDirection::Input | DeviceDirection::Duplex
        )
    }

    fn supports_output(&self) -> bool {
        matches!(
            self.direction,
            DeviceDirection::Output | DeviceDirection::Duplex
        )
    }

    fn supported_input_configs(
        &self,
    ) -> Result<Self::SupportedInputConfigs, SupportedStreamConfigsError> {
        Device::supported_input_configs(self)
    }

    fn supported_output_configs(
        &self,
    ) -> Result<Self::SupportedOutputConfigs, SupportedStreamConfigsError> {
        Device::supported_output_configs(self)
    }

    fn default_input_config(&self) -> Result<SupportedStreamConfig, DefaultStreamConfigError> {
        Device::default_input_config(self)
    }

    fn default_output_config(&self) -> Result<SupportedStreamConfig, DefaultStreamConfigError> {
        Device::default_output_config(self)
    }

    fn build_input_stream_raw<D, E>(
        &self,
        conf: StreamConfig,
        sample_format: SampleFormat,
        data_callback: D,
        error_callback: E,
        timeout: Option<Duration>,
    ) -> Result<Self::Stream, BuildStreamError>
    where
        D: FnMut(&Data, &InputCallbackInfo) + Send + 'static,
        E: FnMut(StreamError) + Send + 'static,
    {
        let stream_inner =
            self.build_stream_inner(conf, sample_format, alsa::Direction::Capture)?;
        let stream = Self::Stream::new_input(
            Arc::new(stream_inner),
            data_callback,
            error_callback,
            timeout,
        );
        Ok(stream)
    }

    fn build_output_stream_raw<D, E>(
        &self,
        conf: StreamConfig,
        sample_format: SampleFormat,
        data_callback: D,
        error_callback: E,
        timeout: Option<Duration>,
    ) -> Result<Self::Stream, BuildStreamError>
    where
        D: FnMut(&mut Data, &OutputCallbackInfo) + Send + 'static,
        E: FnMut(StreamError) + Send + 'static,
    {
        let stream_inner =
            self.build_stream_inner(conf, sample_format, alsa::Direction::Playback)?;
        let stream = Self::Stream::new_output(
            Arc::new(stream_inner),
            data_callback,
            error_callback,
            timeout,
        );
        Ok(stream)
    }
}

#[derive(Debug)]
struct TriggerSender(libc::c_int);

#[derive(Debug)]
struct TriggerReceiver(libc::c_int);

impl TriggerSender {
    fn wakeup(&self) {
        let buf = 1u64;
        loop {
            let ret = unsafe { libc::write(self.0, &buf as *const u64 as *const _, 8) };
            if ret == 8 {
                return;
            }
            // write() can be interrupted by a signal before writing any bytes; retry.
            assert_eq!(ret, -1, "wakeup: unexpected return value {ret}");
            if std::io::Error::last_os_error().kind() != std::io::ErrorKind::Interrupted {
                panic!("wakeup: {}", std::io::Error::last_os_error());
            }
        }
    }
}

impl TriggerReceiver {
    fn clear_pipe(&self) {
        let mut out = 0u64;
        loop {
            let ret = unsafe { libc::read(self.0, &mut out as *mut u64 as *mut _, 8) };
            if ret == 8 {
                return;
            }
            // read() can be interrupted by a signal before reading any bytes; retry.
            assert_eq!(ret, -1, "clear_pipe: unexpected return value {ret}");
            if std::io::Error::last_os_error().kind() != std::io::ErrorKind::Interrupted {
                panic!("clear_pipe: {}", std::io::Error::last_os_error());
            }
        }
    }
}

fn trigger() -> (TriggerSender, Arc<TriggerReceiver>) {
    let mut fds = [0, 0];
    match unsafe { libc::pipe(fds.as_mut_ptr()) } {
        0 => (TriggerSender(fds[1]), Arc::new(TriggerReceiver(fds[0]))),
        _ => panic!("Could not create pipe"),
    }
}

impl Drop for TriggerSender {
    fn drop(&mut self) {
        unsafe {
            libc::close(self.0);
        }
    }
}

impl Drop for TriggerReceiver {
    fn drop(&mut self) {
        unsafe {
            libc::close(self.0);
        }
    }
}

#[derive(Clone, Debug)]
pub struct Device {
    pcm_id: String,
    desc: Option<String>,
    direction: DeviceDirection,
    _context: Arc<AlsaContext>,
}

impl PartialEq for Device {
    fn eq(&self, other: &Self) -> bool {
        self.pcm_id == other.pcm_id
    }
}

impl Eq for Device {}

impl std::hash::Hash for Device {
    fn hash<H: std::hash::Hasher>(&self, state: &mut H) {
        self.pcm_id.hash(state);
    }
}

impl Device {
    fn build_stream_inner(
        &self,
        conf: StreamConfig,
        sample_format: SampleFormat,
        stream_type: alsa::Direction,
    ) -> Result<StreamInner, BuildStreamError> {
        // Validate buffer size if Fixed is specified. This is necessary because
        // `set_period_size_near()` with `ValueOr::Nearest` will accept ANY value and return the
        // "nearest" supported value, which could be wildly different (e.g., requesting 4096 frames
        // might return 512 frames if that's "nearest").
        if let BufferSize::Fixed(requested_size) = conf.buffer_size {
            // Note: We use `default_input_config`/`default_output_config` to get the buffer size
            // range. This queries the CURRENT device (`self.pcm_id`), not the default device. The
            // buffer size range is the same across all format configurations for a given device
            // (see `supported_configs()`).
            let supported_config = match stream_type {
                alsa::Direction::Capture => self.default_input_config(),
                alsa::Direction::Playback => self.default_output_config(),
            };
            if let Ok(config) = supported_config {
                if let SupportedBufferSize::Range { min, max } = config.buffer_size {
                    if !(min..=max).contains(&requested_size) {
                        return Err(BuildStreamError::StreamConfigNotSupported);
                    }
                }
            }
        }

        let open_result = {
            let _guard = ALSA_OPEN_MUTEX.lock().unwrap_or_else(|e| e.into_inner());
            alsa::pcm::PCM::new(&self.pcm_id, stream_type, true).map_err(|e| (e, e.errno()))
        };
        let handle = match open_result {
            Err((_, libc::ENOENT))
            | Err((_, libc::EPERM))
            | Err((_, libc::ENODEV))
            | Err((_, LIBC_ENOTSUPP)) => return Err(BuildStreamError::DeviceNotAvailable),
            Err((_, libc::EBUSY)) | Err((_, libc::EAGAIN)) => {
                return Err(BuildStreamError::DeviceBusy)
            }
            Err((_, libc::EINVAL)) => return Err(BuildStreamError::InvalidArgument),
            Err((e, _)) => return Err(e.into()),
            Ok(handle) => handle,
        };

        let can_pause = set_hw_params_from_format(&handle, conf, sample_format)?;
        let period_samples = set_sw_params_from_format(&handle, conf, stream_type)?;

        handle.prepare()?;

        let num_descriptors = handle.count();
        if num_descriptors == 0 {
            let description = "poll descriptor count for stream was 0".to_string();
            let err = BackendSpecificError { description };
            return Err(err.into());
        }

        // Check to see if we can retrieve valid timestamps from the device.
        // Related: https://bugs.freedesktop.org/show_bug.cgi?id=88503
        let ts = handle.status()?.get_htstamp();
        let creation_instant = std::time::Instant::now();
        let use_hw_timestamps = !(ts.tv_sec == 0 && ts.tv_nsec == 0);

        if let alsa::Direction::Capture = stream_type {
            handle.start()?;
        }

        // Pre-compute a period-sized buffer filled with silence values.
        let period_frames = period_samples / conf.channels as usize;
        let frame_size = sample_format.sample_size() * conf.channels as usize;
        let period_bytes = period_frames * frame_size;
        let mut silence_template = vec![0u8; period_bytes].into_boxed_slice();

        // Only fill buffer for unsigned formats that don't have a zero value for silence.
        if sample_format.is_uint() {
            fill_with_equilibrium(&mut silence_template, sample_format);
        }

        let stream_inner = StreamInner {
            dropping: AtomicBool::new(false),
            channel: handle,
            sample_format,
            num_descriptors,
            conf,
            period_samples,
            period_frames,
            frame_size,
            silence_template,
            can_pause,
            creation_instant,
            use_hw_timestamps,
            _context: self._context.clone(),
        };

        Ok(stream_inner)
    }

    fn name(&self) -> Result<String, DeviceNameError> {
        Ok(self.pcm_id.clone())
    }

    fn description(&self) -> Result<DeviceDescription, DeviceNameError> {
        let name = self
            .desc
            .as_ref()
            .and_then(|desc| desc.lines().next())
            .unwrap_or(&self.pcm_id)
            .to_string();

        let mut builder = DeviceDescriptionBuilder::new(name)
            .driver(self.pcm_id.clone())
            .direction(self.direction);

        if let Some(ref desc) = self.desc {
            let lines = desc
                .lines()
                .map(|line| line.trim().to_string())
                .filter(|line| !line.is_empty())
                .collect();
            builder = builder.extended(lines);
        }

        Ok(builder.build())
    }

    fn id(&self) -> Result<DeviceId, DeviceIdError> {
        Ok(DeviceId(crate::platform::HostId::Alsa, self.pcm_id.clone()))
    }

    fn supported_configs(
        &self,
        stream_t: alsa::Direction,
    ) -> Result<VecIntoIter<SupportedStreamConfigRange>, SupportedStreamConfigsError> {
        let open_result = {
            let _guard = ALSA_OPEN_MUTEX.lock().unwrap_or_else(|e| e.into_inner());
            alsa::pcm::PCM::new(&self.pcm_id, stream_t, true).map_err(|e| (e, e.errno()))
        };
        let pcm = match open_result {
            Err((_, libc::ENOENT))
            | Err((_, libc::EPERM))
            | Err((_, libc::ENODEV))
            | Err((_, LIBC_ENOTSUPP)) => {
                return Err(SupportedStreamConfigsError::DeviceNotAvailable)
            }
            Err((_, libc::EBUSY)) | Err((_, libc::EAGAIN)) => {
                return Err(SupportedStreamConfigsError::DeviceBusy)
            }
            Err((_, libc::EINVAL)) => return Err(SupportedStreamConfigsError::InvalidArgument),
            Err((e, _)) => return Err(e.into()),
            Ok(pcm) => pcm,
        };

        let hw_params = alsa::pcm::HwParams::any(&pcm)?;

        // Test both LE and BE formats to detect what the hardware actually supports.
        // LE is listed first as it's the common case for most audio hardware.
        // Hardware reports its supported formats regardless of CPU endianness.
        const FORMATS: [(SampleFormat, alsa::pcm::Format); 23] = [
            (SampleFormat::I8, alsa::pcm::Format::S8),
            (SampleFormat::U8, alsa::pcm::Format::U8),
            (SampleFormat::I16, alsa::pcm::Format::S16LE),
            (SampleFormat::I16, alsa::pcm::Format::S16BE),
            (SampleFormat::U16, alsa::pcm::Format::U16LE),
            (SampleFormat::U16, alsa::pcm::Format::U16BE),
            (SampleFormat::I24, alsa::pcm::Format::S24LE),
            (SampleFormat::I24, alsa::pcm::Format::S24BE),
            (SampleFormat::U24, alsa::pcm::Format::U24LE),
            (SampleFormat::U24, alsa::pcm::Format::U24BE),
            (SampleFormat::I32, alsa::pcm::Format::S32LE),
            (SampleFormat::I32, alsa::pcm::Format::S32BE),
            (SampleFormat::U32, alsa::pcm::Format::U32LE),
            (SampleFormat::U32, alsa::pcm::Format::U32BE),
            (SampleFormat::F32, alsa::pcm::Format::FloatLE),
            (SampleFormat::F32, alsa::pcm::Format::FloatBE),
            (SampleFormat::F64, alsa::pcm::Format::Float64LE),
            (SampleFormat::F64, alsa::pcm::Format::Float64BE),
            (SampleFormat::DsdU8, alsa::pcm::Format::DSDU8),
            (SampleFormat::DsdU16, alsa::pcm::Format::DSDU16LE),
            (SampleFormat::DsdU16, alsa::pcm::Format::DSDU16BE),
            (SampleFormat::DsdU32, alsa::pcm::Format::DSDU32LE),
            (SampleFormat::DsdU32, alsa::pcm::Format::DSDU32BE),
            //SND_PCM_FORMAT_IEC958_SUBFRAME_LE,
            //SND_PCM_FORMAT_IEC958_SUBFRAME_BE,
            //SND_PCM_FORMAT_MU_LAW,
            //SND_PCM_FORMAT_A_LAW,
            //SND_PCM_FORMAT_IMA_ADPCM,
            //SND_PCM_FORMAT_MPEG,
            //SND_PCM_FORMAT_GSM,
            //SND_PCM_FORMAT_SPECIAL,
            //SND_PCM_FORMAT_S24_3LE,
            //SND_PCM_FORMAT_S24_3BE,
            //SND_PCM_FORMAT_U24_3LE,
            //SND_PCM_FORMAT_U24_3BE,
            //SND_PCM_FORMAT_S20_3LE,
            //SND_PCM_FORMAT_S20_3BE,
            //SND_PCM_FORMAT_U20_3LE,
            //SND_PCM_FORMAT_U20_3BE,
            //SND_PCM_FORMAT_S18_3LE,
            //SND_PCM_FORMAT_S18_3BE,
            //SND_PCM_FORMAT_U18_3LE,
            //SND_PCM_FORMAT_U18_3BE,
        ];

        // Collect supported formats, deduplicating since we test both LE and BE variants.
        // If hardware supports both endiannesses (rare), we only report the format once.
        let mut supported_formats = Vec::new();
        for &(sample_format, alsa_format) in FORMATS.iter() {
            if hw_params.test_format(alsa_format).is_ok()
                && !supported_formats.contains(&sample_format)
            {
                supported_formats.push(sample_format);
            }
        }

        let min_rate = hw_params.get_rate_min()?;
        let max_rate = hw_params.get_rate_max()?;

        let sample_rates = if min_rate == max_rate || hw_params.test_rate(min_rate + 1).is_ok() {
            vec![(min_rate, max_rate)]
        } else {
            let mut rates = Vec::new();
            for &sample_rate in crate::COMMON_SAMPLE_RATES.iter() {
                if hw_params.test_rate(sample_rate).is_ok() {
                    rates.push((sample_rate, sample_rate));
                }
            }

            if rates.is_empty() {
                vec![(min_rate, max_rate)]
            } else {
                rates
            }
        };

        let min_channels = hw_params.get_channels_min()?;
        let max_channels = hw_params.get_channels_max()?;

        let max_channels = cmp::min(max_channels, 32); // TODO: limiting to 32 channels or too much stuff is returned
        let supported_channels = (min_channels..max_channels + 1)
            .filter_map(|num| {
                if hw_params.test_channels(num).is_ok() {
                    Some(num as ChannelCount)
                } else {
                    None
                }
            })
            .collect::<Vec<_>>();

        let (min_buffer_size, max_buffer_size) = hw_params_buffer_size_min_max(&hw_params);
        let buffer_size_range = SupportedBufferSize::Range {
            min: min_buffer_size,
            max: max_buffer_size,
        };

        let mut output = Vec::with_capacity(
            supported_formats.len() * supported_channels.len() * sample_rates.len(),
        );
        for &sample_format in supported_formats.iter() {
            for &channels in supported_channels.iter() {
                for &(min_rate, max_rate) in sample_rates.iter() {
                    output.push(SupportedStreamConfigRange {
                        channels,
                        min_sample_rate: min_rate,
                        max_sample_rate: max_rate,
                        buffer_size: buffer_size_range,
                        sample_format,
                    });
                }
            }
        }

        Ok(output.into_iter())
    }

    fn supported_input_configs(
        &self,
    ) -> Result<SupportedInputConfigs, SupportedStreamConfigsError> {
        self.supported_configs(alsa::Direction::Capture)
    }

    fn supported_output_configs(
        &self,
    ) -> Result<SupportedOutputConfigs, SupportedStreamConfigsError> {
        self.supported_configs(alsa::Direction::Playback)
    }

    // ALSA does not offer default stream formats, so instead we compare all supported formats by
    // the `SupportedStreamConfigRange::cmp_default_heuristics` order and select the greatest.
    fn default_config(
        &self,
        stream_t: alsa::Direction,
    ) -> Result<SupportedStreamConfig, DefaultStreamConfigError> {
        let mut formats: Vec<_> = {
            match self.supported_configs(stream_t) {
                Err(SupportedStreamConfigsError::DeviceNotAvailable) => {
                    return Err(DefaultStreamConfigError::DeviceNotAvailable);
                }
                Err(SupportedStreamConfigsError::DeviceBusy) => {
                    return Err(DefaultStreamConfigError::DeviceBusy);
                }
                Err(SupportedStreamConfigsError::InvalidArgument) => {
                    // this happens sometimes when querying for input and output capabilities, but
                    // the device supports only one
                    return Err(DefaultStreamConfigError::StreamTypeNotSupported);
                }
                Err(SupportedStreamConfigsError::BackendSpecific { err }) => {
                    return Err(err.into());
                }
                Ok(fmts) => fmts.collect(),
            }
        };

        formats.sort_by(|a, b| a.cmp_default_heuristics(b));

        match formats.into_iter().next_back() {
            Some(f) => {
                let min_r = f.min_sample_rate;
                let max_r = f.max_sample_rate;
                let mut format = f.with_max_sample_rate();
                const HZ_44100: SampleRate = 44_100;
                if min_r <= HZ_44100 && HZ_44100 <= max_r {
                    format.sample_rate = HZ_44100;
                }
                Ok(format)
            }
            None => Err(DefaultStreamConfigError::StreamTypeNotSupported),
        }
    }

    fn default_input_config(&self) -> Result<SupportedStreamConfig, DefaultStreamConfigError> {
        self.default_config(alsa::Direction::Capture)
    }

    fn default_output_config(&self) -> Result<SupportedStreamConfig, DefaultStreamConfigError> {
        self.default_config(alsa::Direction::Playback)
    }
}

impl Default for Device {
    fn default() -> Self {
        // "default" is a virtual ALSA device that redirects to the configured default. We cannot
        // determine its actual capabilities without opening it, so we return Unknown direction.
        Self {
            pcm_id: DEFAULT_DEVICE.to_owned(),
            desc: Some("Default Audio Device".to_string()),
            direction: DeviceDirection::Unknown,
            _context: Arc::new(
                AlsaContext::new().expect("Failed to initialize ALSA configuration"),
            ),
        }
    }
}

#[derive(Debug)]
struct StreamInner {
    // Flag used to check when to stop polling, regardless of the state of the stream
    // (e.g. broken due to a disconnected device).
    dropping: AtomicBool,

    // The ALSA channel.
    channel: alsa::pcm::PCM,

    // When converting between file descriptors and `snd_pcm_t`, this is the number of
    // file descriptors that this `snd_pcm_t` uses.
    num_descriptors: usize,

    // Format of the samples.
    sample_format: SampleFormat,

    // The configuration used to open this stream.
    conf: StreamConfig,

    // Cached values for performance in audio callback hot path
    period_samples: usize,
    period_frames: usize,
    frame_size: usize,
    silence_template: Box<[u8]>,

    #[allow(dead_code)]
    // Whether or not the hardware supports pausing the stream.
    // TODO: We need an API to expose this. See #197, #284.
    can_pause: bool,

    // Whether to attempt hardware timestamps via `get_htstamp` / `get_trigger_htstamp`.
    //
    // When `true`, hardware timestamps are tried first on every callback and we fall back silently
    // to `creation_instant` if they are transiently unavailable; e.g. the PulseAudio ALSA plugin
    // returns `(0, 0)` for the first several periods after the stream is triggered.
    use_hw_timestamps: bool,

    // Timestamp origin used by the fallback path. Faster without `Option`.
    creation_instant: std::time::Instant,

    // Keep ALSA context alive to prevent premature ALSA config cleanup
    _context: Arc<AlsaContext>,
}

// Assume that the ALSA library is built with thread safe option.
unsafe impl Sync for StreamInner {}

#[derive(Debug)]
pub struct Stream {
    /// The high-priority audio processing thread calling callbacks.
    /// Option used for moving out in destructor.
    thread: Option<JoinHandle<()>>,

    /// Handle to the underlying stream for playback controls.
    inner: Arc<StreamInner>,

    /// Used to signal to stop processing.
    trigger: TriggerSender,

    /// Keeps the read end of the self-pipe alive for the lifetime of the Stream, so that
    /// `trigger.wakeup()` never writes to a closed pipe, even if the worker exited early.
    _rx: Arc<TriggerReceiver>,
}

// Compile-time assertion that Stream is Send and Sync
crate::assert_stream_send!(Stream);
crate::assert_stream_sync!(Stream);

struct StreamWorkerContext {
    descriptors: Box<[libc::pollfd]>,
    transfer_buffer: Box<[u8]>,
    poll_timeout: i32,
}

impl StreamWorkerContext {
    fn new(poll_timeout: &Option<Duration>, stream: &StreamInner, rx: &TriggerReceiver) -> Self {
        let poll_timeout: i32 = if let Some(d) = poll_timeout {
            d.as_millis().try_into().unwrap()
        } else {
            -1 // Don't timeout, wait forever.
        };

        // Pre-allocate buffer to exactly one period size with proper equilibrium values.
        let transfer_buffer = stream.silence_template.clone();

        // Pre-allocate and initialize descriptors vector: 1 for self-pipe + stream.num_descriptors
        // for ALSA. The descriptor count is constant for the lifetime of stream parameters, and
        // poll() overwrites revents on each call, so we only need to set up fd and events once.
        let total_descriptors = 1 + stream.num_descriptors;
        let mut descriptors = vec![
            libc::pollfd {
                fd: 0,
                events: 0,
                revents: 0
            };
            total_descriptors
        ]
        .into_boxed_slice();

        // Set up self-pipe descriptor at index 0
        descriptors[0] = libc::pollfd {
            fd: rx.0,
            events: libc::POLLIN,
            revents: 0,
        };

        // Set up ALSA descriptors starting at index 1
        let filled = stream
            .channel
            .fill(&mut descriptors[1..])
            .expect("Failed to fill ALSA descriptors");
        debug_assert_eq!(filled, stream.num_descriptors);

        Self {
            descriptors,
            transfer_buffer,
            poll_timeout,
        }
    }
}

fn input_stream_worker(
    rx: Arc<TriggerReceiver>,
    stream: &StreamInner,
    data_callback: &mut (dyn FnMut(&Data, &InputCallbackInfo) + Send + 'static),
    error_callback: &mut (dyn FnMut(StreamError) + Send + 'static),
    timeout: Option<Duration>,
) {
    boost_current_thread_priority(stream.conf.buffer_size, stream.conf.sample_rate);

    let mut ctxt = StreamWorkerContext::new(&timeout, stream, &rx);
    loop {
        if stream.dropping.load(Ordering::Acquire) {
            return;
        }
        let result = match poll_for_period(&rx, stream, &mut ctxt) {
            Ok(Poll::Pending) => continue,
            Ok(Poll::Ready {
                status,
                delay_frames,
            }) => process_input(
                stream,
                &mut ctxt.transfer_buffer,
                status,
                delay_frames,
                data_callback,
            ),
            Err(err) => Err(err),
        };
        if let Err(err) = result {
            match err {
                StreamError::BufferUnderrun => {
                    error_callback(StreamError::BufferUnderrun);
                    if let Err(err) = stream.channel.prepare() {
                        error_callback(err.into());
                    } else if let Err(err) = stream.channel.start() {
                        error_callback(err.into());
                    }
                }
                StreamError::DeviceNotAvailable => {
                    error_callback(StreamError::DeviceNotAvailable);
                    return;
                }
                err => error_callback(err),
            }
        }
    }
}

fn output_stream_worker(
    rx: Arc<TriggerReceiver>,
    stream: &StreamInner,
    data_callback: &mut (dyn FnMut(&mut Data, &OutputCallbackInfo) + Send + 'static),
    error_callback: &mut (dyn FnMut(StreamError) + Send + 'static),
    timeout: Option<Duration>,
) {
    boost_current_thread_priority(stream.conf.buffer_size, stream.conf.sample_rate);

    let mut ctxt = StreamWorkerContext::new(&timeout, stream, &rx);

    loop {
        if stream.dropping.load(Ordering::Acquire) {
            return;
        }
        let result = match poll_for_period(&rx, stream, &mut ctxt) {
            Ok(Poll::Pending) => continue,
            Ok(Poll::Ready {
                status,
                delay_frames,
            }) => process_output(
                stream,
                &mut ctxt.transfer_buffer,
                status,
                delay_frames,
                data_callback,
            ),
            Err(err) => Err(err),
        };
        if let Err(err) = result {
            match err {
                StreamError::BufferUnderrun => {
                    error_callback(StreamError::BufferUnderrun);
                    if let Err(err) = stream.channel.prepare() {
                        error_callback(err.into());
                    }
                    // No need to call start() for output streams after prepare();
                    // ALSA automatically restarts them when the buffer is refilled
                    // and the stream is triggered again.
                }
                StreamError::DeviceNotAvailable => {
                    error_callback(StreamError::DeviceNotAvailable);
                    return;
                }
                err => error_callback(err),
            }
        }
    }
}

#[cfg(feature = "audio_thread_priority")]
fn boost_current_thread_priority(buffer_size: BufferSize, sample_rate: SampleRate) {
    use audio_thread_priority::promote_current_thread_to_real_time;

    let buffer_size = if let BufferSize::Fixed(buffer_size) = buffer_size {
        buffer_size
    } else {
        // if the buffer size isn't fixed, let audio_thread_priority choose a sensible default value
        0
    };

    if let Err(err) = promote_current_thread_to_real_time(buffer_size, sample_rate) {
        eprintln!("Failed to promote audio thread to real-time priority: {err}");
    }
}

#[cfg(not(feature = "audio_thread_priority"))]
fn boost_current_thread_priority(_: BufferSize, _: SampleRate) {}

/// Attempt hardware resume from a suspend event (`ESTRPIPE`).
fn try_resume(channel: &alsa::PCM) -> Result<Poll, StreamError> {
    match channel.resume() {
        // device resumed successfully and will continue running on its own
        Ok(()) => Ok(Poll::Pending),
        // device is still resuming; poll again until it is ready.
        Err(e) if e.errno() == libc::EAGAIN => Ok(Poll::Pending),
        // hardware does not support soft resume
        Err(e) if e.errno() == libc::ENOSYS => Err(StreamError::BufferUnderrun),
        Err(e) => Err(e.into()),
    }
}

enum Poll {
    Pending,
    Ready {
        status: alsa::pcm::Status,
        delay_frames: usize,
    },
}

// This block is shared between both input and output stream worker functions.
fn poll_for_period(
    rx: &TriggerReceiver,
    stream: &StreamInner,
    ctxt: &mut StreamWorkerContext,
) -> Result<Poll, StreamError> {
    let StreamWorkerContext {
        ref mut descriptors,
        ref poll_timeout,
        ..
    } = *ctxt;

    let res = alsa::poll::poll(descriptors, *poll_timeout)?;
    if res == 0 {
        // poll() returned 0: either a timeout or a spurious wakeup. Nothing to do.
        return Ok(Poll::Pending);
    }

    if descriptors[0].revents != 0 {
        // Self-pipe fired: the stream is being dropped. Clear the pipe and let the
        // worker loop detect the dropping flag on the next iteration.
        rx.clear_pipe();
        return Ok(Poll::Pending);
    }

    let revents = stream.channel.revents(&descriptors[1..])?;
    // No events: spurious wakeup, poll again.
    if revents.is_empty() {
        return Ok(Poll::Pending);
    }
    // POLLHUP/POLLNVAL: the device has been disconnected.
    if revents.intersects(alsa::poll::Flags::HUP | alsa::poll::Flags::NVAL) {
        return Err(StreamError::DeviceNotAvailable);
    }
    // POLLERR signals an xrun or suspend; avail() below returns EPIPE/ESTRPIPE accordingly.
    // POLLIN/POLLOUT: data is ready, fall through to process it.

    let status = stream.channel.status()?;
    let avail_frames = match stream.channel.avail() {
        // Xrun: recover via prepare() (+ start() for capture, handled by the worker).
        Err(err) if err.errno() == libc::EPIPE => return Err(StreamError::BufferUnderrun),
        // Suspend: try hardware resume first; fall back to prepare() if unsupported.
        Err(err) if err.errno() == libc::ESTRPIPE => return try_resume(&stream.channel),
        res => res,
    }? as usize;
    let delay_frames = match status.get_delay() {
        d if d < 0 => 0,
        d => d as usize,
    };
    let available_samples = avail_frames * stream.conf.channels as usize;

    // ALSA can have spurious wakeups where poll returns but avail < avail_min.
    // This is documented to occur with dmix (timer-driven) and other plugins.
    // Verify we have room for at least one full period before processing.
    // See: https://bugzilla.kernel.org/show_bug.cgi?id=202499
    if available_samples < stream.period_samples {
        return Ok(Poll::Pending);
    }

    Ok(Poll::Ready {
        status,
        delay_frames,
    })
}

// Read input data from ALSA and deliver it to the user.
fn process_input(
    stream: &StreamInner,
    buffer: &mut [u8],
    status: alsa::pcm::Status,
    delay_frames: usize,
    data_callback: &mut (dyn FnMut(&Data, &InputCallbackInfo) + Send + 'static),
) -> Result<(), StreamError> {
    let mut frames_read = 0;
    while frames_read < stream.period_frames {
        match stream
            .channel
            .io_bytes()
            .readi(&mut buffer[frames_read * stream.frame_size..])
        {
            Ok(n) => frames_read += n,
            Err(err) if err.errno() == libc::EPIPE || err.errno() == libc::ESTRPIPE => {
                // EPIPE = xrun, ESTRPIPE = hardware suspend. Both require prepare()+restart;
                // attempting resume mid-loop with a partial transfer in the ring buffer is unsafe.
                return Err(StreamError::BufferUnderrun);
            }
            Err(err) if err.errno() == libc::ENODEV => return Err(StreamError::DeviceNotAvailable),
            Err(err) => return Err(err.into()),
        }
    }
    let data = buffer.as_mut_ptr() as *mut ();
    let data = unsafe { Data::from_parts(data, stream.period_samples, stream.sample_format) };
    let callback = if stream.use_hw_timestamps {
        stream_timestamp_hardware(&status)
            .or_else(|_| stream_timestamp_fallback(stream.creation_instant))
    } else {
        stream_timestamp_fallback(stream.creation_instant)
    }?;
    let delay_duration = frames_to_duration(delay_frames, stream.conf.sample_rate);
    let capture = callback
        .sub(delay_duration)
        .ok_or_else(|| BackendSpecificError {
            description: "`capture` is earlier than representation supported by `StreamInstant`"
                .to_string(),
        })?;
    let timestamp = crate::InputStreamTimestamp { callback, capture };
    let info = crate::InputCallbackInfo { timestamp };
    data_callback(&data, &info);

    Ok(())
}

// Request data from the user's function and write it via ALSA.
fn process_output(
    stream: &StreamInner,
    buffer: &mut [u8],
    status: alsa::pcm::Status,
    delay_frames: usize,
    data_callback: &mut (dyn FnMut(&mut Data, &OutputCallbackInfo) + Send + 'static),
) -> Result<(), StreamError> {
    // Buffer is always pre-filled with equilibrium, user overwrites what they want
    buffer.copy_from_slice(&stream.silence_template);
    {
        let data = buffer.as_mut_ptr() as *mut ();
        let mut data =
            unsafe { Data::from_parts(data, stream.period_samples, stream.sample_format) };
        let callback = if stream.use_hw_timestamps {
            stream_timestamp_hardware(&status)
                .or_else(|_| stream_timestamp_fallback(stream.creation_instant))
        } else {
            stream_timestamp_fallback(stream.creation_instant)
        }?;
        let delay_duration = frames_to_duration(delay_frames, stream.conf.sample_rate);
        let playback = callback
            .add(delay_duration)
            .ok_or_else(|| BackendSpecificError {
                description: "`playback` occurs beyond representation supported by `StreamInstant`"
                    .to_string(),
            })?;
        let timestamp = crate::OutputStreamTimestamp { callback, playback };
        let info = crate::OutputCallbackInfo { timestamp };
        data_callback(&mut data, &info);
    }

    let mut frames_written = 0;
    while frames_written < stream.period_frames {
        match stream
            .channel
            .io_bytes()
            .writei(&buffer[frames_written * stream.frame_size..])
        {
            Ok(n) => frames_written += n,
            Err(err) if err.errno() == libc::EPIPE || err.errno() == libc::ESTRPIPE => {
                // EPIPE = xrun, ESTRPIPE = hardware suspend. Both require prepare()+restart;
                // attempting resume mid-loop with a partial transfer in the ring buffer is unsafe.
                return Err(StreamError::BufferUnderrun);
            }
            Err(err) if err.errno() == libc::ENODEV => return Err(StreamError::DeviceNotAvailable),
            Err(err) => return Err(err.into()),
        }
    }
    Ok(())
}

// Use hardware timestamps from ALSA.
//
// This ensures accurate timestamps based on actual hardware timing.
#[inline]
fn stream_timestamp_hardware(
    status: &alsa::pcm::Status,
) -> Result<crate::StreamInstant, BackendSpecificError> {
    let trigger_ts = status.get_trigger_htstamp();
    // trigger_htstamp records when the PCM stream started.
    // On the first few callbacks, it might not have been set yet,
    // which would yield a huge positive nanos nd cause non-monotonicity
    // once it is set. Bail out and let the caller use the fallback.
    // See https://github.com/RustAudio/cpal/issues/710
    if trigger_ts.tv_sec == 0 && trigger_ts.tv_nsec == 0 {
        return Err(BackendSpecificError {
            description: "trigger_htstamp not yet set".to_string(),
        });
    }
    let ts = status.get_htstamp();
    let nanos = timespec_diff_nanos(ts, trigger_ts);
    if nanos < 0 {
        let description = format!(
            "get_htstamp `{}.{}` was earlier than get_trigger_htstamp `{}.{}`",
            ts.tv_sec, ts.tv_nsec, trigger_ts.tv_sec, trigger_ts.tv_nsec
        );
        return Err(BackendSpecificError { description });
    }
    Ok(crate::StreamInstant::from_nanos(nanos))
}

// Use elapsed duration since stream creation as fallback when hardware timestamps are unavailable.
//
// This ensures positive values that are compatible with our `StreamInstant` representation.
#[inline]
fn stream_timestamp_fallback(
    creation: std::time::Instant,
) -> Result<crate::StreamInstant, BackendSpecificError> {
    let now = std::time::Instant::now();
    let duration = now.duration_since(creation);
    crate::StreamInstant::from_nanos_i128(duration.as_nanos() as i128).ok_or(BackendSpecificError {
        description: "stream duration has exceeded `StreamInstant` representation".to_string(),
    })
}

// Adapted from `timestamp2ns` here:
// https://fossies.org/linux/alsa-lib/test/audio_time.c
#[inline]
#[allow(clippy::unnecessary_cast)]
fn timespec_to_nanos(ts: libc::timespec) -> i64 {
    ts.tv_sec as i64 * 1_000_000_000 + ts.tv_nsec as i64
}

// Adapted from `timediff` here:
// https://fossies.org/linux/alsa-lib/test/audio_time.c
#[inline]
fn timespec_diff_nanos(a: libc::timespec, b: libc::timespec) -> i64 {
    timespec_to_nanos(a) - timespec_to_nanos(b)
}

// Convert the given duration in frames at the given sample rate to a `std::time::Duration`.
#[inline]
fn frames_to_duration(frames: usize, rate: crate::SampleRate) -> std::time::Duration {
    let secsf = frames as f64 / rate as f64;
    let secs = secsf as u64;
    let nanos = ((secsf - secs as f64) * 1_000_000_000.0) as u32;
    std::time::Duration::new(secs, nanos)
}

impl Stream {
    fn new_input<D, E>(
        inner: Arc<StreamInner>,
        mut data_callback: D,
        mut error_callback: E,
        timeout: Option<Duration>,
    ) -> Stream
    where
        D: FnMut(&Data, &InputCallbackInfo) + Send + 'static,
        E: FnMut(StreamError) + Send + 'static,
    {
        let (tx, rx) = trigger();
        let rx_thread = rx.clone();
        let stream = inner.clone();
        let thread = thread::Builder::new()
            .name("cpal_alsa_in".to_owned())
            .spawn(move || {
                input_stream_worker(
                    rx_thread,
                    &stream,
                    &mut data_callback,
                    &mut error_callback,
                    timeout,
                );
            })
            .unwrap();
        Self {
            thread: Some(thread),
            inner,
            trigger: tx,
            _rx: rx,
        }
    }

    fn new_output<D, E>(
        inner: Arc<StreamInner>,
        mut data_callback: D,
        mut error_callback: E,
        timeout: Option<Duration>,
    ) -> Stream
    where
        D: FnMut(&mut Data, &OutputCallbackInfo) + Send + 'static,
        E: FnMut(StreamError) + Send + 'static,
    {
        let (tx, rx) = trigger();
        let rx_thread = rx.clone();
        let stream = inner.clone();
        let thread = thread::Builder::new()
            .name("cpal_alsa_out".to_owned())
            .spawn(move || {
                output_stream_worker(
                    rx_thread,
                    &stream,
                    &mut data_callback,
                    &mut error_callback,
                    timeout,
                );
            })
            .unwrap();
        Self {
            thread: Some(thread),
            inner,
            trigger: tx,
            _rx: rx,
        }
    }
}

impl Drop for Stream {
    fn drop(&mut self) {
        self.inner.dropping.store(true, Ordering::Release);
        self.trigger.wakeup();
        if let Some(handle) = self.thread.take() {
            let _ = handle.join();
        }
    }
}

impl StreamTrait for Stream {
    fn play(&self) -> Result<(), PlayStreamError> {
        self.inner.channel.pause(false).ok();
        Ok(())
    }
    fn pause(&self) -> Result<(), PauseStreamError> {
        self.inner.channel.pause(true).ok();
        Ok(())
    }
    fn buffer_size(&self) -> Option<FrameCount> {
        Some(self.inner.period_frames as FrameCount)
    }
}

// Convert ALSA frames to FrameCount, clamping to valid range.
// ALSA Frames are i64 (64-bit) or i32 (32-bit).
fn clamp_frame_count(buffer_size: alsa::pcm::Frames) -> FrameCount {
    buffer_size.max(1).try_into().unwrap_or(FrameCount::MAX)
}

fn hw_params_buffer_size_min_max(hw_params: &alsa::pcm::HwParams) -> (FrameCount, FrameCount) {
    let min_buf = hw_params
        .get_buffer_size_min()
        .map(clamp_frame_count)
        .unwrap_or(1);
    let max_buf = hw_params
        .get_buffer_size_max()
        .map(clamp_frame_count)
        .unwrap_or(FrameCount::MAX);
    (min_buf, max_buf)
}

fn init_hw_params<'a>(
    pcm_handle: &'a alsa::pcm::PCM,
    config: StreamConfig,
    sample_format: SampleFormat,
) -> Result<alsa::pcm::HwParams<'a>, BackendSpecificError> {
    let hw_params = alsa::pcm::HwParams::any(pcm_handle)?;
    hw_params.set_access(alsa::pcm::Access::RWInterleaved)?;

    // Determine which endianness the hardware actually supports for this format.
    // We prefer native endian (no conversion needed) but fall back to the opposite
    // endian if that's all the hardware supports (e.g., LE USB DAC on BE system).
    let alsa_format = sample_format_to_alsa_format(&hw_params, sample_format)?;
    hw_params.set_format(alsa_format)?;

    hw_params.set_rate(config.sample_rate, alsa::ValueOr::Nearest)?;
    hw_params.set_channels(config.channels as u32)?;
    Ok(hw_params)
}

/// Convert SampleFormat to the appropriate alsa::pcm::Format based on what the hardware supports.
/// Prefers native endian, falls back to non-native if that's all the hardware supports.
fn sample_format_to_alsa_format(
    hw_params: &alsa::pcm::HwParams,
    sample_format: SampleFormat,
) -> Result<alsa::pcm::Format, BackendSpecificError> {
    use alsa::pcm::Format;

    // For each sample format, define (native_endian_format, opposite_endian_format) pairs
    let (native, opposite) = match sample_format {
        SampleFormat::I8 => return Ok(Format::S8), // No endianness
        SampleFormat::U8 => return Ok(Format::U8), // No endianness
        #[cfg(target_endian = "little")]
        SampleFormat::I16 => (Format::S16LE, Format::S16BE),
        #[cfg(target_endian = "big")]
        SampleFormat::I16 => (Format::S16BE, Format::S16LE),
        #[cfg(target_endian = "little")]
        SampleFormat::U16 => (Format::U16LE, Format::U16BE),
        #[cfg(target_endian = "big")]
        SampleFormat::U16 => (Format::U16BE, Format::U16LE),
        #[cfg(target_endian = "little")]
        SampleFormat::I24 => (Format::S24LE, Format::S24BE),
        #[cfg(target_endian = "big")]
        SampleFormat::I24 => (Format::S24BE, Format::S24LE),
        #[cfg(target_endian = "little")]
        SampleFormat::U24 => (Format::U24LE, Format::U24BE),
        #[cfg(target_endian = "big")]
        SampleFormat::U24 => (Format::U24BE, Format::U24LE),
        #[cfg(target_endian = "little")]
        SampleFormat::I32 => (Format::S32LE, Format::S32BE),
        #[cfg(target_endian = "big")]
        SampleFormat::I32 => (Format::S32BE, Format::S32LE),
        #[cfg(target_endian = "little")]
        SampleFormat::U32 => (Format::U32LE, Format::U32BE),
        #[cfg(target_endian = "big")]
        SampleFormat::U32 => (Format::U32BE, Format::U32LE),
        #[cfg(target_endian = "little")]
        SampleFormat::F32 => (Format::FloatLE, Format::FloatBE),
        #[cfg(target_endian = "big")]
        SampleFormat::F32 => (Format::FloatBE, Format::FloatLE),
        #[cfg(target_endian = "little")]
        SampleFormat::F64 => (Format::Float64LE, Format::Float64BE),
        #[cfg(target_endian = "big")]
        SampleFormat::F64 => (Format::Float64BE, Format::Float64LE),
        SampleFormat::DsdU8 => return Ok(Format::DSDU8),
        #[cfg(target_endian = "little")]
        SampleFormat::DsdU16 => (Format::DSDU16LE, Format::DSDU16BE),
        #[cfg(target_endian = "big")]
        SampleFormat::DsdU16 => (Format::DSDU16BE, Format::DSDU16LE),
        #[cfg(target_endian = "little")]
        SampleFormat::DsdU32 => (Format::DSDU32LE, Format::DSDU32BE),
        #[cfg(target_endian = "big")]
        SampleFormat::DsdU32 => (Format::DSDU32BE, Format::DSDU32LE),
        _ => {
            return Err(BackendSpecificError {
                description: format!("Sample format '{sample_format}' is not supported"),
            })
        }
    };

    // Try native endian first (optimal - no conversion needed)
    if hw_params.test_format(native).is_ok() {
        return Ok(native);
    }

    // Fall back to opposite endian if hardware only supports that
    if hw_params.test_format(opposite).is_ok() {
        return Ok(opposite);
    }

    Err(BackendSpecificError {
        description: format!(
            "Sample format '{sample_format}' is not supported by hardware in any endianness"
        ),
    })
}

fn set_hw_params_from_format(
    pcm_handle: &alsa::pcm::PCM,
    config: StreamConfig,
    sample_format: SampleFormat,
) -> Result<bool, BackendSpecificError> {
    let hw_params = init_hw_params(pcm_handle, config, sample_format)?;

    // When BufferSize::Fixed(x) is specified, we configure double-buffering with
    // buffer_size = 2x and period_size = x. This provides consistent low-latency
    // behavior across different ALSA implementations and hardware.
    if let BufferSize::Fixed(buffer_frames) = config.buffer_size {
        hw_params.set_buffer_size_near((2 * buffer_frames) as alsa::pcm::Frames)?;
        hw_params
            .set_period_size_near(buffer_frames as alsa::pcm::Frames, alsa::ValueOr::Nearest)?;
    }

    // Apply hardware parameters
    pcm_handle.hw_params(&hw_params)?;

    // For BufferSize::Default, constrain to device's configured period with 2-period buffering.
    // PipeWire-ALSA picks a good period size but pairs it with many periods (huge buffer).
    // We need to re-initialize hw_params and set BOTH period and buffer to constrain properly.
    if config.buffer_size == BufferSize::Default {
        if let Ok(period) = hw_params.get_period_size() {
            // Re-initialize hw_params to clear previous constraints
            let hw_params = init_hw_params(pcm_handle, config, sample_format)?;

            // Set both period (to device's chosen value) and buffer (to 2 periods)
            hw_params.set_period_size_near(period, alsa::ValueOr::Nearest)?;
            hw_params.set_buffer_size_near(2 * period)?;

            // Re-apply with new constraints
            pcm_handle.hw_params(&hw_params)?;
        }
    }

    Ok(hw_params.can_pause())
}

fn set_sw_params_from_format(
    pcm_handle: &alsa::pcm::PCM,
    config: StreamConfig,
    stream_type: alsa::Direction,
) -> Result<usize, BackendSpecificError> {
    let sw_params = pcm_handle.sw_params_current()?;

    let period_samples = {
        let (buffer, period) = pcm_handle.get_params()?;
        if buffer == 0 {
            return Err(BackendSpecificError {
                description: "initialization resulted in a null buffer".to_string(),
            });
        }
        let start_threshold = match stream_type {
            alsa::Direction::Playback => {
                // Start playback when 2 periods are filled. This ensures consistent low-latency
                // startup regardless of total buffer size (whether 2 or more periods).
                2 * period
            }
            alsa::Direction::Capture => 1,
        };
        sw_params.set_start_threshold(start_threshold as alsa::pcm::Frames)?;
        sw_params.set_avail_min(period as alsa::pcm::Frames)?;

        period as usize * config.channels as usize
    };

    sw_params.set_tstamp_mode(true)?;
    sw_params.set_tstamp_type(alsa::pcm::TstampType::MonotonicRaw)?;

    // tstamp_type param cannot be changed after the device is opened.
    // The default tstamp_type value on most Linux systems is "monotonic",
    // let's try to use it if setting the tstamp_type fails.
    if pcm_handle.sw_params(&sw_params).is_err() {
        sw_params.set_tstamp_type(alsa::pcm::TstampType::Monotonic)?;
        pcm_handle.sw_params(&sw_params)?;
    }

    Ok(period_samples)
}

fn canonical_pcm_id(pcm_id: &str) -> String {
    if let Some((prefix, rest)) = pcm_id.split_once(':') {
        let (card_str, device_str) = match rest.split_once(',') {
            Some((c, d)) => (c.trim(), d.trim()),
            None => (rest.trim(), "0"),
        };
        if !card_str.contains('=') {
            if let Ok(device) = device_str.parse::<u32>() {
                return format!("{prefix}:CARD={card_str},DEV={device}");
            }
        }
    }
    pcm_id.to_owned()
}

impl From<alsa::Error> for BackendSpecificError {
    fn from(err: alsa::Error) -> Self {
        Self {
            description: err.to_string(),
        }
    }
}

impl From<alsa::Error> for BuildStreamError {
    fn from(err: alsa::Error) -> Self {
        let err: BackendSpecificError = err.into();
        err.into()
    }
}

impl From<alsa::Error> for SupportedStreamConfigsError {
    fn from(err: alsa::Error) -> Self {
        let err: BackendSpecificError = err.into();
        err.into()
    }
}

impl From<alsa::Error> for PlayStreamError {
    fn from(err: alsa::Error) -> Self {
        let err: BackendSpecificError = err.into();
        err.into()
    }
}

impl From<alsa::Error> for PauseStreamError {
    fn from(err: alsa::Error) -> Self {
        let err: BackendSpecificError = err.into();
        err.into()
    }
}

impl From<alsa::Error> for StreamError {
    fn from(err: alsa::Error) -> Self {
        let err: BackendSpecificError = err.into();
        err.into()
    }
}
```

## File: `src/host/asio/device.rs`
```rust
pub use crate::iter::{SupportedInputConfigs, SupportedOutputConfigs};

use super::sys;
use crate::host::com;
use crate::ChannelCount;
use crate::DefaultStreamConfigError;
use crate::DeviceDescription;
use crate::DeviceDescriptionBuilder;
use crate::DeviceId;
use crate::DeviceIdError;
use crate::DeviceNameError;
use crate::DevicesError;
use crate::FrameCount;
use crate::SampleFormat;
use crate::SampleRate;
use crate::SupportedBufferSize;
use crate::SupportedStreamConfig;
use crate::SupportedStreamConfigRange;
use crate::SupportedStreamConfigsError;

use std::hash::{Hash, Hasher};
use std::sync::atomic::AtomicU32;
use std::sync::{Arc, Mutex};

/// A ASIO Device
#[derive(Clone)]
pub struct Device {
    name: String,

    // Metadata cached during enumeration
    channels_in: ChannelCount,
    channels_out: ChannelCount,
    sample_rate: SampleRate,
    buffer_size_min: FrameCount,
    buffer_size_max: FrameCount,
    input_sample_format: Option<SampleFormat>,
    output_sample_format: Option<SampleFormat>,
    supported_sample_rates: Vec<SampleRate>,

    // Input and/or Output stream.
    // A driver can only have one of each.
    // They need to be created at the same time.
    pub(super) asio_streams: Arc<Mutex<sys::AsioStreams>>,
    pub(super) current_callback_flag: Arc<AtomicU32>,
}

/// All available devices.
pub struct Devices {
    asio: Arc<sys::Asio>,
    drivers: std::vec::IntoIter<String>,
    current_driver: Option<sys::Driver>,
}

impl PartialEq for Device {
    fn eq(&self, other: &Self) -> bool {
        self.name == other.name
    }
}

impl Eq for Device {}

impl Hash for Device {
    fn hash<H: Hasher>(&self, state: &mut H) {
        self.name.hash(state);
    }
}

impl Device {
    pub fn description(&self) -> Result<DeviceDescription, DeviceNameError> {
        let direction = crate::device_description::direction_from_counts(
            Some(self.channels_in),
            Some(self.channels_out),
        );

        Ok(DeviceDescriptionBuilder::new(self.name.clone())
            .driver(self.name.clone())
            .direction(direction)
            .build())
    }

    pub fn id(&self) -> Result<DeviceId, DeviceIdError> {
        Ok(DeviceId(crate::platform::HostId::Asio, self.name.clone()))
    }

    /// Gets the supported input configs.
    /// TODO currently only supports the default.
    /// Need to find all possible configs.
    pub fn supported_input_configs(
        &self,
    ) -> Result<SupportedInputConfigs, SupportedStreamConfigsError> {
        let default = self
            .default_input_config()
            .map_err(|_| SupportedStreamConfigsError::DeviceNotAvailable)?;
        Ok(self.configs_for(default).into_iter())
    }

    /// Gets the supported output configs.
    /// TODO currently only supports the default.
    /// Need to find all possible configs.
    pub fn supported_output_configs(
        &self,
    ) -> Result<SupportedOutputConfigs, SupportedStreamConfigsError> {
        let default = self
            .default_output_config()
            .map_err(|_| SupportedStreamConfigsError::DeviceNotAvailable)?;
        Ok(self.configs_for(default).into_iter())
    }

    /// Returns the default input config
    pub fn default_input_config(&self) -> Result<SupportedStreamConfig, DefaultStreamConfigError> {
        self.default_config(self.channels_in, self.input_sample_format)
    }

    /// Returns the default output config
    pub fn default_output_config(&self) -> Result<SupportedStreamConfig, DefaultStreamConfigError> {
        self.default_config(self.channels_out, self.output_sample_format)
    }

    fn default_config(
        &self,
        channels: ChannelCount,
        sample_format: Option<SampleFormat>,
    ) -> Result<SupportedStreamConfig, DefaultStreamConfigError> {
        if channels == 0 {
            return Err(DefaultStreamConfigError::StreamTypeNotSupported);
        }
        let sample_format =
            sample_format.ok_or(DefaultStreamConfigError::StreamTypeNotSupported)?;
        Ok(SupportedStreamConfig {
            channels,
            sample_rate: self.sample_rate,
            buffer_size: SupportedBufferSize::Range {
                min: self.buffer_size_min,
                max: self.buffer_size_max,
            },
            sample_format,
        })
    }

    fn configs_for(&self, default: SupportedStreamConfig) -> Vec<SupportedStreamConfigRange> {
        let mut configs = Vec::with_capacity(default.channels as usize);
        for &rate in &self.supported_sample_rates {
            for channels in 1..=default.channels {
                configs.push(SupportedStreamConfigRange {
                    channels,
                    min_sample_rate: rate,
                    max_sample_rate: rate,
                    buffer_size: default.buffer_size,
                    sample_format: default.sample_format,
                });
            }
        }
        configs
    }
}

impl Devices {
    pub fn new(asio: Arc<sys::Asio>) -> Result<Self, DevicesError> {
        // Make sure that COM is initialized.
        com::com_initialized();
        let drivers = asio.driver_names().into_iter();
        Ok(Self {
            asio,
            drivers,
            current_driver: None,
        })
    }
}

impl Iterator for Devices {
    type Item = Device;

    /// Enumerate devices by briefly loading each driver to capture its metadata.
    fn next(&mut self) -> Option<Device> {
        // Drop the previously loaded driver before attempting to load the next one.
        self.current_driver = None;

        loop {
            match self.drivers.next() {
                Some(name) => match self.asio.load_driver(&name) {
                    Ok(driver) => {
                        let Ok(channels) = driver.channels() else {
                            continue;
                        };
                        if channels.ins == 0 && channels.outs == 0 {
                            continue;
                        }

                        // Some drivers (e.g. Realtek ASIO) return 0 for sample_rate() until a
                        // stream is active. Treat 0 as "not yet known" rather than skipping.
                        let sample_rate = driver.sample_rate().unwrap_or(0.0);

                        let Ok(buffer_size_range) = driver.buffersize_range() else {
                            continue;
                        };

                        let input_sample_format = driver
                            .input_data_type()
                            .ok()
                            .and_then(|t| convert_data_type(&t));
                        let output_sample_format = driver
                            .output_data_type()
                            .ok()
                            .and_then(|t| convert_data_type(&t));

                        let supported_sample_rates: Vec<SampleRate> = crate::COMMON_SAMPLE_RATES
                            .iter()
                            .copied()
                            .filter(|&r| driver.can_sample_rate(r.into()).unwrap_or(false))
                            .collect();

                        self.current_driver = Some(driver);

                        let asio_streams = Arc::new(Mutex::new(sys::AsioStreams {
                            input: None,
                            output: None,
                        }));

                        return Some(Device {
                            name,
                            channels_in: channels.ins as ChannelCount,
                            channels_out: channels.outs as ChannelCount,
                            sample_rate: sample_rate as SampleRate,
                            buffer_size_min: buffer_size_range.min as FrameCount,
                            buffer_size_max: buffer_size_range.max as FrameCount,
                            input_sample_format,
                            output_sample_format,
                            supported_sample_rates,
                            asio_streams,
                            // Initialize with sentinel value so it never matches global flag state (0 or 1).
                            current_callback_flag: Arc::new(AtomicU32::new(u32::MAX)),
                        });
                    }
                    // A different driver is already loaded (e.g. an active Stream holds it). Stop
                    // cleanly rather than spinning through the rest of the list.
                    Err(sys::LoadDriverError::DriverAlreadyExists) => return None,
                    // Driver failed to load for its own reasons; skip and try the next.
                    Err(_) => continue,
                },
                None => return None,
            }
        }
    }
}

pub(crate) fn convert_data_type(ty: &sys::AsioSampleType) -> Option<SampleFormat> {
    let fmt = match *ty {
        sys::AsioSampleType::ASIOSTInt16MSB => SampleFormat::I16,
        sys::AsioSampleType::ASIOSTInt16LSB => SampleFormat::I16,
        sys::AsioSampleType::ASIOSTInt24MSB => SampleFormat::I24,
        sys::AsioSampleType::ASIOSTInt24LSB => SampleFormat::I24,
        sys::AsioSampleType::ASIOSTInt32MSB => SampleFormat::I32,
        sys::AsioSampleType::ASIOSTInt32LSB => SampleFormat::I32,
        sys::AsioSampleType::ASIOSTFloat32MSB => SampleFormat::F32,
        sys::AsioSampleType::ASIOSTFloat32LSB => SampleFormat::F32,
        sys::AsioSampleType::ASIOSTFloat64MSB => SampleFormat::F64,
        sys::AsioSampleType::ASIOSTFloat64LSB => SampleFormat::F64,
        _ => return None,
    };
    Some(fmt)
}
```

## File: `src/host/asio/mod.rs`
```rust
//! ASIO backend implementation.
//!
//! ASIO is available on Windows with the `asio` feature.
//! See the project README for setup instructions.

extern crate asio_sys as sys;

use crate::host::com;
use crate::traits::{DeviceTrait, HostTrait, StreamTrait};
use crate::{
    BuildStreamError, Data, DefaultStreamConfigError, DeviceDescription, DeviceId, DeviceIdError,
    DeviceNameError, DevicesError, InputCallbackInfo, OutputCallbackInfo, PauseStreamError,
    PlayStreamError, SampleFormat, StreamConfig, StreamError, SupportedStreamConfig,
    SupportedStreamConfigsError,
};

pub use self::device::{Device, Devices, SupportedInputConfigs, SupportedOutputConfigs};
pub use self::stream::Stream;
use std::sync::{Arc, OnceLock};
use std::time::Duration;

mod device;
mod stream;

/// Global ASIO instance shared across all Host instances.
///
/// ASIO only supports loading a single driver at a time globally, so all Host instances
/// must share the same underlying sys::Asio wrapper to properly coordinate driver access.
static GLOBAL_ASIO: OnceLock<Arc<sys::Asio>> = OnceLock::new();

/// The host for ASIO.
#[derive(Debug)]
pub struct Host {
    asio: Arc<sys::Asio>,
}

impl Host {
    pub fn new() -> Result<Self, crate::HostUnavailable> {
        com::com_initialized();
        let asio = GLOBAL_ASIO
            .get_or_init(|| Arc::new(sys::Asio::new()))
            .clone();
        let host = Host { asio };
        Ok(host)
    }
}

impl HostTrait for Host {
    type Devices = Devices;
    type Device = Device;

    fn is_available() -> bool {
        true
        //unimplemented!("check how to do this using asio-sys")
    }

    fn devices(&self) -> Result<Self::Devices, DevicesError> {
        Devices::new(self.asio.clone())
    }

    fn default_input_device(&self) -> Option<Self::Device> {
        // ASIO has no concept of a default device, so just use the first.
        self.input_devices().ok().and_then(|mut ds| ds.next())
    }

    fn default_output_device(&self) -> Option<Self::Device> {
        // ASIO has no concept of a default device, so just use the first.
        self.output_devices().ok().and_then(|mut ds| ds.next())
    }
}

impl DeviceTrait for Device {
    type SupportedInputConfigs = SupportedInputConfigs;
    type SupportedOutputConfigs = SupportedOutputConfigs;
    type Stream = Stream;

    fn description(&self) -> Result<DeviceDescription, DeviceNameError> {
        Device::description(self)
    }

    fn id(&self) -> Result<DeviceId, DeviceIdError> {
        Device::id(self)
    }

    fn supported_input_configs(
        &self,
    ) -> Result<Self::SupportedInputConfigs, SupportedStreamConfigsError> {
        Device::supported_input_configs(self)
    }

    fn supported_output_configs(
        &self,
    ) -> Result<Self::SupportedOutputConfigs, SupportedStreamConfigsError> {
        Device::supported_output_configs(self)
    }

    fn default_input_config(&self) -> Result<SupportedStreamConfig, DefaultStreamConfigError> {
        Device::default_input_config(self)
    }

    fn default_output_config(&self) -> Result<SupportedStreamConfig, DefaultStreamConfigError> {
        Device::default_output_config(self)
    }

    fn build_input_stream_raw<D, E>(
        &self,
        config: StreamConfig,
        sample_format: SampleFormat,
        data_callback: D,
        error_callback: E,
        timeout: Option<Duration>,
    ) -> Result<Self::Stream, BuildStreamError>
    where
        D: FnMut(&Data, &InputCallbackInfo) + Send + 'static,
        E: FnMut(StreamError) + Send + 'static,
    {
        Device::build_input_stream_raw(
            self,
            config,
            sample_format,
            data_callback,
            error_callback,
            timeout,
        )
    }

    fn build_output_stream_raw<D, E>(
        &self,
        config: StreamConfig,
        sample_format: SampleFormat,
        data_callback: D,
        error_callback: E,
        timeout: Option<Duration>,
    ) -> Result<Self::Stream, BuildStreamError>
    where
        D: FnMut(&mut Data, &OutputCallbackInfo) + Send + 'static,
        E: FnMut(StreamError) + Send + 'static,
    {
        Device::build_output_stream_raw(
            self,
            config,
            sample_format,
            data_callback,
            error_callback,
            timeout,
        )
    }
}

impl StreamTrait for Stream {
    fn play(&self) -> Result<(), PlayStreamError> {
        Stream::play(self)
    }

    fn pause(&self) -> Result<(), PauseStreamError> {
        Stream::pause(self)
    }

    fn buffer_size(&self) -> Option<crate::FrameCount> {
        Stream::buffer_size(self)
    }
}
```

## File: `src/host/asio/stream.rs`
```rust
extern crate asio_sys as sys;
extern crate num_traits;

use crate::host::com;
use crate::I24;

use self::num_traits::{FromPrimitive, PrimInt};
use super::Device;
use crate::{
    BackendSpecificError, BufferSize, BuildStreamError, Data, InputCallbackInfo,
    OutputCallbackInfo, PauseStreamError, PlayStreamError, SampleFormat, StreamConfig, StreamError,
};
use std::sync::atomic::{AtomicBool, AtomicUsize, Ordering};
use std::sync::{Arc, Mutex};
use std::time::Duration;

pub struct Stream {
    playing: Arc<AtomicBool>,
    // Ensure the `Driver` does not terminate until the last stream is dropped.
    driver: Arc<sys::Driver>,
    #[allow(dead_code)]
    asio_streams: Arc<Mutex<sys::AsioStreams>>,
    callback_id: sys::BufferCallbackId,
    driver_event_callback_id: sys::DriverEventCallbackId,
}

// Compile-time assertion that Stream is Send and Sync
crate::assert_stream_send!(Stream);
crate::assert_stream_sync!(Stream);

impl Stream {
    pub fn play(&self) -> Result<(), PlayStreamError> {
        self.playing.store(true, Ordering::Release);
        Ok(())
    }

    pub fn pause(&self) -> Result<(), PauseStreamError> {
        self.playing.store(false, Ordering::Release);
        Ok(())
    }

    pub fn buffer_size(&self) -> Option<crate::FrameCount> {
        let streams = self.asio_streams.lock().ok()?;
        streams
            .output
            .as_ref()
            .or(streams.input.as_ref())
            .map(|s| s.buffer_size as crate::FrameCount)
    }
}

impl Device {
    pub fn build_input_stream_raw<D, E>(
        &self,
        config: StreamConfig,
        sample_format: SampleFormat,
        mut data_callback: D,
        error_callback: E,
        _timeout: Option<Duration>,
    ) -> Result<Stream, BuildStreamError>
    where
        D: FnMut(&Data, &InputCallbackInfo) + Send + 'static,
        E: FnMut(StreamError) + Send + 'static,
    {
        com::com_initialized();
        let description = self
            .description()
            .map_err(|_| BuildStreamError::DeviceNotAvailable)?;
        let driver = super::GLOBAL_ASIO
            .get()
            .ok_or(BuildStreamError::DeviceNotAvailable)?
            .load_driver(description.name())
            .map_err(load_driver_err)?;

        let stream_type = driver.input_data_type().map_err(build_stream_err)?;

        // Ensure that the desired sample type is supported.
        let expected_sample_format = super::device::convert_data_type(&stream_type)
            .ok_or(BuildStreamError::StreamConfigNotSupported)?;
        if sample_format != expected_sample_format {
            return Err(BuildStreamError::StreamConfigNotSupported);
        }

        let num_channels = config.channels;
        let buffer_size = self.get_or_create_input_stream(&driver, config, sample_format)?;
        let cpal_num_samples = buffer_size * num_channels as usize;

        // Create the buffer depending on the size of the data type.
        let len_bytes = cpal_num_samples * sample_format.sample_size();
        let mut interleaved = vec![0u8; len_bytes];

        // Query hardware input latency (order matters: needs buffers created above).
        // Wrapped in Arc<AtomicUsize> so the message callback can update it on
        // kAsioLatenciesChanged without touching the buffer callback.
        let hardware_input_latency = Arc::new(AtomicUsize::new(
            driver
                .latencies()
                .map(|latencies| latencies.input.max(0) as usize)
                .unwrap_or(0),
        ));

        let driver_event_callback_id = self.add_event_callback(
            &driver,
            error_callback,
            Arc::clone(&hardware_input_latency),
            true,
        );

        let stream_playing = Arc::new(AtomicBool::new(false));
        let playing = Arc::clone(&stream_playing);
        let asio_streams = self.asio_streams.clone();
        let mut current_buffer_size = buffer_size as i32;
        let mut last_buffer_index: i32 = -1;

        // Set the input callback.
        // This is most performance critical part of the ASIO bindings.
        let callback_id = driver.add_callback(move |callback_info| unsafe {
            // If not playing return early.
            if !playing.load(Ordering::Acquire) {
                return;
            }

            // Guard against non-conformant drivers (e.g. Focusrite USB ASIO, ReaRoute) that
            // fire the buffer callback multiple times per buffer cycle with the same buffer
            // index.
            if callback_info.buffer_index == last_buffer_index {
                return;
            }
            last_buffer_index = callback_info.buffer_index;

            // There is 0% chance of lock contention the host only locks when recreating streams.
            let stream_lock = asio_streams.lock().unwrap();
            let asio_stream = match stream_lock.input {
                Some(ref asio_stream) => asio_stream,
                None => return,
            };

            // Resize the buffer only when the driver issues a buffer size change request.
            // In normal operation this branch is never taken.
            if asio_stream.buffer_size != current_buffer_size {
                current_buffer_size = asio_stream.buffer_size;
                interleaved.resize(
                    current_buffer_size as usize
                        * num_channels as usize
                        * sample_format.sample_size(),
                    0,
                );
            }

            let hardware_input_latency = hardware_input_latency.load(Ordering::Relaxed);

            /// 1. Write from the ASIO buffer to the interleaved CPAL buffer.
            /// 2. Deliver the CPAL buffer to the user callback.
            #[allow(clippy::too_many_arguments)]
            unsafe fn process_input_callback<A, D, F>(
                data_callback: &mut D,
                interleaved: &mut [u8],
                asio_stream: &sys::AsioStream,
                asio_info: &sys::CallbackInfo,
                sample_rate: crate::SampleRate,
                format: SampleFormat,
                from_endianness: F,
                hardware_latency_frames: usize,
            ) where
                A: Copy,
                D: FnMut(&Data, &InputCallbackInfo) + Send + 'static,
                F: Fn(A) -> A,
            {
                // 1. Write the ASIO channels to the CPAL buffer.
                let interleaved: &mut [A] = cast_slice_mut(interleaved);
                let n_frames = asio_stream.buffer_size as usize;
                let n_channels = interleaved.len() / n_frames;
                let buffer_index = asio_info.buffer_index as usize;
                for ch_ix in 0..n_channels {
                    let asio_channel =
                        asio_channel_slice::<A>(asio_stream, buffer_index, ch_ix, None);
                    for (frame, s_asio) in interleaved.chunks_mut(n_channels).zip(asio_channel) {
                        frame[ch_ix] = from_endianness(*s_asio);
                    }
                }

                // 2. Deliver the interleaved buffer to the callback.
                apply_input_callback_to_data::<A, _>(
                    data_callback,
                    interleaved,
                    asio_info,
                    sample_rate,
                    format,
                    hardware_latency_frames,
                );
            }

            match (&stream_type, sample_format) {
                (&sys::AsioSampleType::ASIOSTInt16LSB, SampleFormat::I16) => {
                    process_input_callback::<i16, _, _>(
                        &mut data_callback,
                        &mut interleaved,
                        asio_stream,
                        callback_info,
                        config.sample_rate,
                        SampleFormat::I16,
                        from_le,
                        hardware_input_latency,
                    );
                }
                (&sys::AsioSampleType::ASIOSTInt16MSB, SampleFormat::I16) => {
                    process_input_callback::<i16, _, _>(
                        &mut data_callback,
                        &mut interleaved,
                        asio_stream,
                        callback_info,
                        config.sample_rate,
                        SampleFormat::I16,
                        from_be,
                        hardware_input_latency,
                    );
                }

                (&sys::AsioSampleType::ASIOSTFloat32LSB, SampleFormat::F32) => {
                    process_input_callback::<u32, _, _>(
                        &mut data_callback,
                        &mut interleaved,
                        asio_stream,
                        callback_info,
                        config.sample_rate,
                        SampleFormat::F32,
                        from_le,
                        hardware_input_latency,
                    );
                }
                (&sys::AsioSampleType::ASIOSTFloat32MSB, SampleFormat::F32) => {
                    process_input_callback::<u32, _, _>(
                        &mut data_callback,
                        &mut interleaved,
                        asio_stream,
                        callback_info,
                        config.sample_rate,
                        SampleFormat::F32,
                        from_be,
                        hardware_input_latency,
                    );
                }

                (&sys::AsioSampleType::ASIOSTInt32LSB, SampleFormat::I32) => {
                    process_input_callback::<i32, _, _>(
                        &mut data_callback,
                        &mut interleaved,
                        asio_stream,
                        callback_info,
                        config.sample_rate,
                        SampleFormat::I32,
                        from_le,
                        hardware_input_latency,
                    );
                }
                (&sys::AsioSampleType::ASIOSTInt32MSB, SampleFormat::I32) => {
                    process_input_callback::<i32, _, _>(
                        &mut data_callback,
                        &mut interleaved,
                        asio_stream,
                        callback_info,
                        config.sample_rate,
                        SampleFormat::I32,
                        from_be,
                        hardware_input_latency,
                    );
                }

                (&sys::AsioSampleType::ASIOSTFloat64LSB, SampleFormat::F64) => {
                    process_input_callback::<u64, _, _>(
                        &mut data_callback,
                        &mut interleaved,
                        asio_stream,
                        callback_info,
                        config.sample_rate,
                        SampleFormat::F64,
                        from_le,
                        hardware_input_latency,
                    );
                }
                (&sys::AsioSampleType::ASIOSTFloat64MSB, SampleFormat::F64) => {
                    process_input_callback::<u64, _, _>(
                        &mut data_callback,
                        &mut interleaved,
                        asio_stream,
                        callback_info,
                        config.sample_rate,
                        SampleFormat::F64,
                        from_be,
                        hardware_input_latency,
                    );
                }

                (&sys::AsioSampleType::ASIOSTInt24LSB, SampleFormat::I24) => {
                    process_input_callback_i24(
                        &mut data_callback,
                        &mut interleaved,
                        asio_stream,
                        callback_info,
                        config.sample_rate,
                        true,
                        hardware_input_latency,
                    );
                }
                (&sys::AsioSampleType::ASIOSTInt24MSB, SampleFormat::I24) => {
                    process_input_callback_i24(
                        &mut data_callback,
                        &mut interleaved,
                        asio_stream,
                        callback_info,
                        config.sample_rate,
                        false,
                        hardware_input_latency,
                    );
                }

                unsupported_format_pair => unreachable!(
                    "`build_input_stream_raw` should have returned with unsupported \
                     format {:?}",
                    unsupported_format_pair
                ),
            }
        });

        let driver = Arc::new(driver);
        let asio_streams = self.asio_streams.clone();

        driver.start().map_err(build_stream_err)?;

        Ok(Stream {
            playing: stream_playing,
            driver,
            asio_streams,
            callback_id,
            driver_event_callback_id,
        })
    }

    pub fn build_output_stream_raw<D, E>(
        &self,
        config: StreamConfig,
        sample_format: SampleFormat,
        mut data_callback: D,
        error_callback: E,
        _timeout: Option<Duration>,
    ) -> Result<Stream, BuildStreamError>
    where
        D: FnMut(&mut Data, &OutputCallbackInfo) + Send + 'static,
        E: FnMut(StreamError) + Send + 'static,
    {
        com::com_initialized();
        let description = self
            .description()
            .map_err(|_| BuildStreamError::DeviceNotAvailable)?;
        let driver = super::GLOBAL_ASIO
            .get()
            .ok_or(BuildStreamError::DeviceNotAvailable)?
            .load_driver(description.name())
            .map_err(load_driver_err)?;

        let stream_type = driver.output_data_type().map_err(build_stream_err)?;

        // Ensure that the desired sample type is supported.
        let expected_sample_format = super::device::convert_data_type(&stream_type)
            .ok_or(BuildStreamError::StreamConfigNotSupported)?;
        if sample_format != expected_sample_format {
            return Err(BuildStreamError::StreamConfigNotSupported);
        }

        let num_channels = config.channels;
        let buffer_size = self.get_or_create_output_stream(&driver, config, sample_format)?;
        let cpal_num_samples = buffer_size * num_channels as usize;

        // Create the buffer depending on data type.
        let len_bytes = cpal_num_samples * sample_format.sample_size();
        let mut interleaved = vec![0u8; len_bytes];
        let current_callback_flag = self.current_callback_flag.clone();

        // Query hardware output latency (order matters: needs buffers created above).
        // Wrapped in Arc<AtomicUsize> so the message callback can update it on
        // kAsioLatenciesChanged without touching the buffer callback.
        let hardware_output_latency = Arc::new(AtomicUsize::new(
            driver
                .latencies()
                .map(|latencies| latencies.output.max(0) as usize)
                .unwrap_or(0),
        ));

        let driver_event_callback_id = self.add_event_callback(
            &driver,
            error_callback,
            Arc::clone(&hardware_output_latency),
            false,
        );

        let stream_playing = Arc::new(AtomicBool::new(false));
        let playing = Arc::clone(&stream_playing);
        let asio_streams = self.asio_streams.clone();
        let mut current_buffer_size = buffer_size as i32;
        let mut last_buffer_index: i32 = -1;

        let callback_id = driver.add_callback(move |callback_info| unsafe {
            // If not playing, return early.
            if !playing.load(Ordering::Acquire) {
                return;
            }

            // Guard against non-conformant drivers (e.g. Focusrite USB ASIO, ReaRoute) that
            // fire the buffer callback multiple times per buffer cycle with the same buffer
            // index.
            if callback_info.buffer_index == last_buffer_index {
                return;
            }
            last_buffer_index = callback_info.buffer_index;

            // There is 0% chance of lock contention the host only locks when recreating streams.
            let mut stream_lock = asio_streams.lock().unwrap();
            let asio_stream = match stream_lock.output {
                Some(ref mut asio_stream) => asio_stream,
                None => return,
            };

            // Resize the buffer only when the driver issues a buffer size change request.
            // In normal operation this branch is never taken.
            if asio_stream.buffer_size != current_buffer_size {
                current_buffer_size = asio_stream.buffer_size;
                interleaved.resize(
                    current_buffer_size as usize
                        * num_channels as usize
                        * sample_format.sample_size(),
                    0,
                );
            }

            let hardware_output_latency = hardware_output_latency.load(Ordering::Relaxed);

            // Silence the ASIO buffer that is about to be used.
            //
            // Check if any other callbacks have already silenced the buffer associated with
            // the current callback. The flag is updated once per buffer switch.
            let silence =
                current_callback_flag.load(Ordering::Acquire) != callback_info.callback_flag;

            if silence {
                current_callback_flag.store(callback_info.callback_flag, Ordering::Release);
            }

            /// 1. Render the given callback to the given buffer of interleaved samples.
            /// 2. If required, silence the ASIO buffer.
            /// 3. Finally, write the interleaved data to the non-interleaved ASIO buffer,
            ///    performing endianness conversions as necessary.
            #[allow(clippy::too_many_arguments)]
            unsafe fn process_output_callback<A, D, F>(
                data_callback: &mut D,
                interleaved: &mut [u8],
                silence_asio_buffer: bool,
                asio_stream: &mut sys::AsioStream,
                asio_info: &sys::CallbackInfo,
                sample_rate: crate::SampleRate,
                format: SampleFormat,
                mix_samples: F,
                hardware_latency_frames: usize,
            ) where
                A: Copy,
                D: FnMut(&mut Data, &OutputCallbackInfo) + Send + 'static,
                F: Fn(A, A) -> A,
            {
                let interleaved: &mut [A] = cast_slice_mut(interleaved);
                apply_output_callback_to_data::<A, _>(
                    data_callback,
                    interleaved,
                    asio_info,
                    sample_rate,
                    format,
                    hardware_latency_frames,
                );
                let n_channels = interleaved.len() / asio_stream.buffer_size as usize;
                let buffer_index = asio_info.buffer_index as usize;

                // Write interleaved samples to ASIO channels, one channel at a time.
                for ch_ix in 0..n_channels {
                    let asio_channel =
                        asio_channel_slice_mut::<A>(asio_stream, buffer_index, ch_ix, None);
                    if silence_asio_buffer {
                        asio_channel.align_to_mut::<u8>().1.fill(0);
                    }
                    for (frame, s_asio) in interleaved.chunks(n_channels).zip(asio_channel) {
                        *s_asio = mix_samples(*s_asio, frame[ch_ix]);
                    }
                }
            }

            match (sample_format, &stream_type) {
                (SampleFormat::I16, &sys::AsioSampleType::ASIOSTInt16LSB) => {
                    process_output_callback::<i16, _, _>(
                        &mut data_callback,
                        &mut interleaved,
                        silence,
                        asio_stream,
                        callback_info,
                        config.sample_rate,
                        SampleFormat::I16,
                        |old_sample, new_sample| {
                            from_le(old_sample).saturating_add(new_sample).to_le()
                        },
                        hardware_output_latency,
                    );
                }
                (SampleFormat::I16, &sys::AsioSampleType::ASIOSTInt16MSB) => {
                    process_output_callback::<i16, _, _>(
                        &mut data_callback,
                        &mut interleaved,
                        silence,
                        asio_stream,
                        callback_info,
                        config.sample_rate,
                        SampleFormat::I16,
                        |old_sample, new_sample| {
                            from_be(old_sample).saturating_add(new_sample).to_be()
                        },
                        hardware_output_latency,
                    );
                }
                (SampleFormat::F32, &sys::AsioSampleType::ASIOSTFloat32LSB) => {
                    process_output_callback::<u32, _, _>(
                        &mut data_callback,
                        &mut interleaved,
                        silence,
                        asio_stream,
                        callback_info,
                        config.sample_rate,
                        SampleFormat::F32,
                        |old_sample, new_sample| {
                            (f32::from_bits(from_le(old_sample)) + f32::from_bits(new_sample))
                                .to_bits()
                                .to_le()
                        },
                        hardware_output_latency,
                    );
                }

                (SampleFormat::F32, &sys::AsioSampleType::ASIOSTFloat32MSB) => {
                    process_output_callback::<u32, _, _>(
                        &mut data_callback,
                        &mut interleaved,
                        silence,
                        asio_stream,
                        callback_info,
                        config.sample_rate,
                        SampleFormat::F32,
                        |old_sample, new_sample| {
                            (f32::from_bits(from_be(old_sample)) + f32::from_bits(new_sample))
                                .to_bits()
                                .to_be()
                        },
                        hardware_output_latency,
                    );
                }

                (SampleFormat::I32, &sys::AsioSampleType::ASIOSTInt32LSB) => {
                    process_output_callback::<i32, _, _>(
                        &mut data_callback,
                        &mut interleaved,
                        silence,
                        asio_stream,
                        callback_info,
                        config.sample_rate,
                        SampleFormat::I32,
                        |old_sample, new_sample| {
                            from_le(old_sample).saturating_add(new_sample).to_le()
                        },
                        hardware_output_latency,
                    );
                }
                (SampleFormat::I32, &sys::AsioSampleType::ASIOSTInt32MSB) => {
                    process_output_callback::<i32, _, _>(
                        &mut data_callback,
                        &mut interleaved,
                        silence,
                        asio_stream,
                        callback_info,
                        config.sample_rate,
                        SampleFormat::I32,
                        |old_sample, new_sample| {
                            from_be(old_sample).saturating_add(new_sample).to_be()
                        },
                        hardware_output_latency,
                    );
                }

                (SampleFormat::F64, &sys::AsioSampleType::ASIOSTFloat64LSB) => {
                    process_output_callback::<u64, _, _>(
                        &mut data_callback,
                        &mut interleaved,
                        silence,
                        asio_stream,
                        callback_info,
                        config.sample_rate,
                        SampleFormat::F64,
                        |old_sample, new_sample| {
                            (f64::from_bits(from_le(old_sample)) + f64::from_bits(new_sample))
                                .to_bits()
                                .to_le()
                        },
                        hardware_output_latency,
                    );
                }

                (SampleFormat::F64, &sys::AsioSampleType::ASIOSTFloat64MSB) => {
                    process_output_callback::<u64, _, _>(
                        &mut data_callback,
                        &mut interleaved,
                        silence,
                        asio_stream,
                        callback_info,
                        config.sample_rate,
                        SampleFormat::F64,
                        |old_sample, new_sample| {
                            (f64::from_bits(from_be(old_sample)) + f64::from_bits(new_sample))
                                .to_bits()
                                .to_be()
                        },
                        hardware_output_latency,
                    );
                }

                (SampleFormat::I24, &sys::AsioSampleType::ASIOSTInt24LSB) => {
                    process_output_callback_i24::<_>(
                        &mut data_callback,
                        &mut interleaved,
                        silence,
                        true,
                        asio_stream,
                        callback_info,
                        config.sample_rate,
                        hardware_output_latency,
                    );
                }

                (SampleFormat::I24, &sys::AsioSampleType::ASIOSTInt24MSB) => {
                    process_output_callback_i24::<_>(
                        &mut data_callback,
                        &mut interleaved,
                        silence,
                        false,
                        asio_stream,
                        callback_info,
                        config.sample_rate,
                        hardware_output_latency,
                    );
                }

                unsupported_format_pair => unreachable!(
                    "`build_output_stream_raw` should have returned with unsupported \
                     format {:?}",
                    unsupported_format_pair
                ),
            }
        });

        let driver = Arc::new(driver);
        let asio_streams = self.asio_streams.clone();

        driver.start().map_err(build_stream_err)?;

        Ok(Stream {
            playing: stream_playing,
            driver,
            asio_streams,
            callback_id,
            driver_event_callback_id,
        })
    }

    /// Create a new CPAL Input Stream.
    ///
    /// If there is no existing ASIO Input Stream it will be created.
    ///
    /// On success, the buffer size of the stream is returned.
    fn get_or_create_input_stream(
        &self,
        driver: &sys::Driver,
        config: StreamConfig,
        sample_format: SampleFormat,
    ) -> Result<usize, BuildStreamError> {
        let num_asio_channels = self
            .default_input_config()
            .map_err(|_| BuildStreamError::StreamConfigNotSupported)?
            .channels;
        check_config(driver, config, sample_format, num_asio_channels)?;
        let num_channels = config.channels as usize;
        let mut streams = self.asio_streams.lock().unwrap();

        let buffer_size = match config.buffer_size {
            BufferSize::Fixed(v) => Some(v as i32),
            BufferSize::Default => None,
        };

        // Either create a stream if thers none or had back the
        // size of the current one.
        match streams.input {
            Some(ref input) => Ok(input.buffer_size as usize),
            None => {
                let output = streams.output.take();
                driver
                    .prepare_input_stream(output, num_channels, buffer_size)
                    .map(|new_streams| {
                        let bs = match new_streams.input {
                            Some(ref inp) => inp.buffer_size as usize,
                            None => unreachable!(),
                        };
                        *streams = new_streams;
                        bs
                    })
                    .map_err(|_| BuildStreamError::DeviceNotAvailable)
            }
        }
    }

    /// Create a new CPAL Output Stream.
    ///
    /// If there is no existing ASIO Output Stream it will be created.
    fn get_or_create_output_stream(
        &self,
        driver: &sys::Driver,
        config: StreamConfig,
        sample_format: SampleFormat,
    ) -> Result<usize, BuildStreamError> {
        let num_asio_channels = self
            .default_output_config()
            .map_err(|_| BuildStreamError::StreamConfigNotSupported)?
            .channels;
        check_config(driver, config, sample_format, num_asio_channels)?;
        let num_channels = config.channels as usize;
        let mut streams = self.asio_streams.lock().unwrap();

        let buffer_size = match config.buffer_size {
            BufferSize::Fixed(v) => Some(v as i32),
            BufferSize::Default => None,
        };

        // Either create a stream if thers none or had back the
        // size of the current one.
        match streams.output {
            Some(ref output) => Ok(output.buffer_size as usize),
            None => {
                let input = streams.input.take();
                driver
                    .prepare_output_stream(input, num_channels, buffer_size)
                    .map(|new_streams| {
                        let bs = match new_streams.output {
                            Some(ref out) => out.buffer_size as usize,
                            None => unreachable!(),
                        };
                        *streams = new_streams;
                        bs
                    })
                    .map_err(|_| BuildStreamError::DeviceNotAvailable)
            }
        }
    }

    fn add_event_callback<E>(
        &self,
        driver: &sys::Driver,
        error_callback: E,
        hardware_latency: Arc<AtomicUsize>,
        is_input: bool,
    ) -> sys::DriverEventCallbackId
    where
        E: FnMut(StreamError) + Send + 'static,
    {
        let error_callback_shared = Arc::new(Mutex::new(error_callback));
        let configured_sample_rate = driver.sample_rate().ok().filter(|&r| r > 0.0);
        let driver_for_latency = driver.clone();
        let asio_streams_for_event = self.asio_streams.clone();

        driver.add_event_callback(move |event| {
            match event {
                sys::AsioDriverEvent::Message {
                    selector: msg,
                    value,
                } => match msg {
                    sys::AsioMessageSelectors::kAsioSelectorSupported => {
                        // Signal which selectors this stream opts into.
                        matches!(
                            sys::AsioMessageSelectors::from_i64(value as i64),
                            Some(sys::AsioMessageSelectors::kAsioBufferSizeChange)
                        )
                    }
                    sys::AsioMessageSelectors::kAsioResetRequest => {
                        if let Ok(mut cb) = error_callback_shared.lock() {
                            cb(StreamError::StreamInvalidated);
                        }
                        false
                    }
                    sys::AsioMessageSelectors::kAsioResyncRequest => {
                        if let Ok(mut cb) = error_callback_shared.lock() {
                            cb(StreamError::BufferUnderrun);
                        }
                        false
                    }
                    sys::AsioMessageSelectors::kAsioLatenciesChanged => {
                        if let Ok(latencies) = driver_for_latency.latencies() {
                            let latency = if is_input {
                                latencies.input
                            } else {
                                latencies.output
                            };
                            hardware_latency.store(latency.max(0) as usize, Ordering::Relaxed);
                        }
                        false
                    }
                    sys::AsioMessageSelectors::kAsioBufferSizeChange => {
                        if value > 0 {
                            if let Ok(mut streams) = asio_streams_for_event.lock() {
                                let stream = if is_input {
                                    streams.input.as_mut()
                                } else {
                                    streams.output.as_mut()
                                };
                                if let Some(s) = stream {
                                    s.buffer_size = value;
                                }
                            }
                        }
                        true
                    }
                    _ => false,
                },
                sys::AsioDriverEvent::SampleRateChanged(new_rate) => {
                    if let Some(rate) = configured_sample_rate {
                        if (new_rate - rate).abs() >= 1.0 {
                            if let Ok(mut cb) = error_callback_shared.lock() {
                                cb(StreamError::StreamInvalidated);
                            }
                        }
                    }
                    false
                }
            }
        })
    }
}

impl Drop for Stream {
    fn drop(&mut self) {
        self.driver.remove_callback(self.callback_id);
        self.driver
            .remove_event_callback(self.driver_event_callback_id);
    }
}

// Convert the given duration in frames at the given sample rate to a `std::time::Duration`.
#[inline]
fn frames_to_duration(frames: usize, rate: crate::SampleRate) -> std::time::Duration {
    let secsf = frames as f64 / rate as f64;
    let secs = secsf as u64;
    let nanos = ((secsf - secs as f64) * 1_000_000_000.0) as u32;
    std::time::Duration::new(secs, nanos)
}

/// Check whether or not the desired config is supported by the stream.
///
/// Checks sample rate, data type, number of channels, and buffer size.
fn check_config(
    driver: &sys::Driver,
    config: StreamConfig,
    sample_format: SampleFormat,
    num_asio_channels: u16,
) -> Result<(), BuildStreamError> {
    let StreamConfig {
        channels,
        sample_rate,
        buffer_size,
    } = config;

    // Validate buffer size if `Fixed` is specified. This is necessary because ASIO's
    // `create_buffers` only validates the upper bound (returns `InvalidBufferSize` if > max) but
    // does NOT validate the lower bound. Passing a buffer size below min would be accepted but
    // behavior is unspecified.
    if let BufferSize::Fixed(requested_size) = buffer_size {
        let range = driver.buffersize_range().map_err(build_stream_err)?;
        let requested_size_i32 = requested_size as i32;
        if !(range.min..=range.max).contains(&requested_size_i32) {
            return Err(BuildStreamError::StreamConfigNotSupported);
        }
    }

    // Try and set the sample rate to what the user selected.
    let sample_rate = sample_rate.into();
    if sample_rate != driver.sample_rate().map_err(build_stream_err)? {
        if driver
            .can_sample_rate(sample_rate)
            .map_err(build_stream_err)?
        {
            driver
                .set_sample_rate(sample_rate)
                .map_err(build_stream_err)?;
        } else {
            return Err(BuildStreamError::StreamConfigNotSupported);
        }
    }
    // unsigned formats are not supported by asio
    match sample_format {
        SampleFormat::I16 | SampleFormat::I24 | SampleFormat::I32 | SampleFormat::F32 => (),
        _ => return Err(BuildStreamError::StreamConfigNotSupported),
    }
    if channels > num_asio_channels {
        return Err(BuildStreamError::StreamConfigNotSupported);
    }
    Ok(())
}

/// Cast a byte slice into a mutable slice of desired type.
///
/// Safety: it's up to the caller to ensure that the input slice has valid bit representations.
unsafe fn cast_slice_mut<T>(v: &mut [u8]) -> &mut [T] {
    debug_assert!(v.len() % std::mem::size_of::<T>() == 0);
    std::slice::from_raw_parts_mut(v.as_mut_ptr() as *mut T, v.len() / std::mem::size_of::<T>())
}

/// Helper function to convert from little endianness.
fn from_le<T: PrimInt>(t: T) -> T {
    T::from_le(t)
}

/// Helper function to convert from little endianness.
fn from_be<T: PrimInt>(t: T) -> T {
    T::from_be(t)
}

/// Shorthand for retrieving the asio buffer slice associated with a channel.
///
/// The channel length is automatically inferred from the buffer size or some
/// value can be passed to enforce a certain length (for odd sized sample formats)
unsafe fn asio_channel_slice<T>(
    asio_stream: &sys::AsioStream,
    buffer_index: usize,
    channel_index: usize,
    requested_channel_length: Option<usize>,
) -> &[T] {
    let channel_length = requested_channel_length.unwrap_or(asio_stream.buffer_size as usize);
    let buff_ptr: *const T =
        asio_stream.buffer_infos[channel_index].buffers[buffer_index] as *const _;
    std::slice::from_raw_parts(buff_ptr, channel_length)
}

/// Shorthand for retrieving the asio buffer slice associated with a channel.
///
/// The channel length is automatically inferred from the buffer size or some
/// value can be passed to enforce a certain length (for odd sized sample formats)
unsafe fn asio_channel_slice_mut<T>(
    asio_stream: &mut sys::AsioStream,
    buffer_index: usize,
    channel_index: usize,
    requested_channel_length: Option<usize>,
) -> &mut [T] {
    let channel_length = requested_channel_length.unwrap_or(asio_stream.buffer_size as usize);
    let buff_ptr: *mut T = asio_stream.buffer_infos[channel_index].buffers[buffer_index] as *mut _;
    std::slice::from_raw_parts_mut(buff_ptr, channel_length)
}

fn load_driver_err(e: sys::LoadDriverError) -> BuildStreamError {
    match e {
        sys::LoadDriverError::LoadDriverFailed | sys::LoadDriverError::DriverAlreadyExists => {
            BuildStreamError::DeviceNotAvailable
        }
        sys::LoadDriverError::InitializationFailed(asio_err) => build_stream_err(asio_err),
    }
}

fn build_stream_err(e: sys::AsioError) -> BuildStreamError {
    match e {
        sys::AsioError::NoDrivers | sys::AsioError::HardwareMalfunction => {
            BuildStreamError::DeviceNotAvailable
        }
        sys::AsioError::InvalidInput | sys::AsioError::BadMode => BuildStreamError::InvalidArgument,
        err => {
            let description = format!("{}", err);
            BackendSpecificError { description }.into()
        }
    }
}

/// Convert i24 bytes to i32
fn i24_bytes_to_i32(i24_bytes: &[u8; 3], little_endian: bool) -> i32 {
    let sample = if little_endian {
        i32::from_le_bytes([i24_bytes[0], i24_bytes[1], i24_bytes[2], 0u8])
    } else {
        i32::from_le_bytes([i24_bytes[2], i24_bytes[1], i24_bytes[0], 0u8])
    };
    if sample & 0x800000 != 0 {
        sample | -0x1000000
    } else {
        sample
    }
}

#[allow(clippy::too_many_arguments)]
unsafe fn process_output_callback_i24<D>(
    data_callback: &mut D,
    interleaved: &mut [u8],
    silence_asio_buffer: bool,
    little_endian: bool,
    asio_stream: &mut sys::AsioStream,
    asio_info: &sys::CallbackInfo,
    sample_rate: crate::SampleRate,
    hardware_latency_frames: usize,
) where
    D: FnMut(&mut Data, &OutputCallbackInfo) + Send + 'static,
{
    let format = SampleFormat::I24;
    let interleaved: &mut [I24] = cast_slice_mut(interleaved);
    apply_output_callback_to_data::<I24, _>(
        data_callback,
        interleaved,
        asio_info,
        sample_rate,
        format,
        hardware_latency_frames,
    );

    // Size of samples in the ASIO buffer (has to be 3 in this case)
    let asio_sample_size_bytes = 3;
    let n_channels = interleaved.len() / asio_stream.buffer_size as usize;
    let buffer_index = asio_info.buffer_index as usize;

    // Write interleaved samples to ASIO channels, one channel at a time.
    for ch_ix in 0..n_channels {
        // Take channel as u8 array ([u8; 3] packets to represent i24)
        let asio_channel = asio_channel_slice_mut(
            asio_stream,
            buffer_index,
            ch_ix,
            Some(asio_stream.buffer_size as usize * asio_sample_size_bytes),
        );

        if silence_asio_buffer {
            asio_channel.align_to_mut::<u8>().1.fill(0);
        }

        // Fill in every channel from the interleaved vector
        for (channel_sample, sample_in_buffer) in asio_channel
            .chunks_mut(asio_sample_size_bytes)
            .zip(interleaved.iter().skip(ch_ix).step_by(n_channels))
        {
            // Add samples from buffer if no silence was applied, otherwise just overwrite
            let result = if silence_asio_buffer {
                sample_in_buffer.inner()
            } else {
                let sample = i24_bytes_to_i32(
                    &[channel_sample[0], channel_sample[1], channel_sample[2]],
                    little_endian,
                );
                (sample_in_buffer.inner() + sample).clamp(-8388608, 8388607)
            };
            let bytes = result.to_le_bytes();
            if little_endian {
                channel_sample[0] = bytes[0];
                channel_sample[1] = bytes[1];
                channel_sample[2] = bytes[2];
            } else {
                channel_sample[2] = bytes[0];
                channel_sample[1] = bytes[1];
                channel_sample[0] = bytes[2];
            }
        }
    }
}

unsafe fn process_input_callback_i24<D>(
    data_callback: &mut D,
    interleaved: &mut [u8],
    asio_stream: &sys::AsioStream,
    asio_info: &sys::CallbackInfo,
    sample_rate: crate::SampleRate,
    little_endian: bool,
    hardware_latency_frames: usize,
) where
    D: FnMut(&Data, &InputCallbackInfo) + Send + 'static,
{
    let format = SampleFormat::I24;

    // 1. Write the ASIO channels to the CPAL buffer.
    let interleaved: &mut [I24] = cast_slice_mut(interleaved);
    let n_frames = asio_stream.buffer_size as usize;
    let n_channels = interleaved.len() / n_frames;
    let buffer_index = asio_info.buffer_index as usize;
    let asio_sample_size_bytes = 3;

    for ch_ix in 0..n_channels {
        let asio_channel = asio_channel_slice::<u8>(
            asio_stream,
            buffer_index,
            ch_ix,
            Some(n_frames * asio_sample_size_bytes),
        );
        for (channel_sample, sample_in_buffer) in asio_channel
            .chunks(asio_sample_size_bytes)
            .zip(interleaved.iter_mut().skip(ch_ix).step_by(n_channels))
        {
            let sample = i24_bytes_to_i32(
                &[channel_sample[0], channel_sample[1], channel_sample[2]],
                little_endian,
            );
            *sample_in_buffer = I24::new(sample).unwrap();
        }
    }

    // 2. Deliver the interleaved buffer to the callback.
    apply_input_callback_to_data::<I24, _>(
        data_callback,
        interleaved,
        asio_info,
        sample_rate,
        format,
        hardware_latency_frames,
    );
}

/// Apply the output callback to the interleaved buffer.
unsafe fn apply_output_callback_to_data<A, D>(
    data_callback: &mut D,
    interleaved: &mut [A],
    asio_info: &sys::CallbackInfo,
    sample_rate: crate::SampleRate,
    sample_format: SampleFormat,
    hardware_latency_frames: usize,
) where
    A: Copy,
    D: FnMut(&mut Data, &OutputCallbackInfo) + Send + 'static,
{
    let mut data = Data::from_parts(
        interleaved.as_mut_ptr() as *mut (),
        interleaved.len(),
        sample_format,
    );
    let callback = crate::StreamInstant::from_nanos_i128(asio_info.system_time as i128)
        .expect("`system_time` out of range of `StreamInstant` representation");
    let delay = frames_to_duration(hardware_latency_frames, sample_rate);
    let playback = callback
        .add(delay)
        .expect("`playback` occurs beyond representation supported by `StreamInstant`");
    let timestamp = crate::OutputStreamTimestamp { callback, playback };
    let info = OutputCallbackInfo { timestamp };
    data_callback(&mut data, &info);
}

/// Apply the input callback to the interleaved buffer.
unsafe fn apply_input_callback_to_data<A, D>(
    data_callback: &mut D,
    interleaved: &mut [A],
    asio_info: &sys::CallbackInfo,
    sample_rate: crate::SampleRate,
    format: SampleFormat,
    hardware_latency_frames: usize,
) where
    A: Copy,
    D: FnMut(&Data, &InputCallbackInfo) + Send + 'static,
{
    let data = Data::from_parts(
        interleaved.as_mut_ptr() as *mut (),
        interleaved.len(),
        format,
    );
    let callback = crate::StreamInstant::from_nanos_i128(asio_info.system_time as i128)
        .expect("`system_time` out of range of `StreamInstant` representation");
    let delay = frames_to_duration(hardware_latency_frames, sample_rate);
    let capture = callback
        .sub(delay)
        .expect("`capture` occurs before origin of alsa `StreamInstant`");
    let timestamp = crate::InputStreamTimestamp { callback, capture };
    let info = InputCallbackInfo { timestamp };
    data_callback(&data, &info);
}
```

## File: `src/host/audioworklet/dependent_module.rs`
```rust
// This file is based on code from:
//   https://github.com/rustwasm/wasm-bindgen/blob/main/examples/wasm-audio-worklet/src/dependent_module.rs
//
// The original code is licensed under either of:
//   - MIT license (https://opensource.org/licenses/MIT)
//   - Apache License, Version 2.0 (https://www.apache.org/licenses/LICENSE-2.0)
// at your option.
//
// Copyright (c) 2017-2024 The wasm-bindgen Developers
//
// This file incorporates code from the above source under the Apache License, Version 2.0 license.
// Please see the original repository for more details.
//
// See this issue for a further explanation of what this file does: https://github.com/rustwasm/wasm-bindgen/issues/3019

use js_sys::{wasm_bindgen, Array, JsString};
use wasm_bindgen::prelude::*;
use web_sys::{Blob, BlobPropertyBag, Url};

// This is a not-so-clean approach to get the current bindgen ES module URL
// in Rust. This will fail at run time on bindgen targets not using ES modules.
#[wasm_bindgen]
extern "C" {
    #[wasm_bindgen]
    type ImportMeta;

    #[wasm_bindgen(method, getter)]
    fn url(this: &ImportMeta) -> JsString;

    #[wasm_bindgen(thread_local_v2, js_namespace = import, js_name = meta)]
    static IMPORT_META: ImportMeta;
}

pub fn on_the_fly(code: &str) -> Result<String, JsValue> {
    // Generate the import of the bindgen ES module, assuming `--target web`.
    let header = format!(
        "import init, * as bindgen from '{}';\n\n",
        IMPORT_META.with(ImportMeta::url),
    );

    let options = BlobPropertyBag::new();
    options.set_type("text/javascript");
    Url::create_object_url_with_blob(&Blob::new_with_str_sequence_and_options(
        &Array::of2(&JsValue::from(header.as_str()), &JsValue::from(code)),
        &options,
    )?)
}

// dependent_module! takes a local file name to a JS module as input and
// returns a URL to a slightly modified module in run time. This modified module
// has an additional import statement in the header that imports the current
// bindgen JS module under the `bindgen` alias, and the separate init function.
// How this URL is produced does not matter for the macro user. on_the_fly
// creates a blob URL in run time. A better, more sophisticated solution
// would add wasm_bindgen support to put such a module in pkg/ during build time
// and return a URL to this file instead (described in #3019).
#[macro_export]
macro_rules! dependent_module {
    ($file_name:expr) => {
        $crate::host::audioworklet::dependent_module::on_the_fly(include_str!($file_name))
    };
}
```

## File: `src/host/audioworklet/mod.rs`
```rust
//! Audio Worklet backend implementation.
//!
//! Available on WebAssembly with the `audioworklet` feature. Requires atomics support.
//! See the `audioworklet-beep` example for setup instructions.

mod dependent_module;
use js_sys::wasm_bindgen;

use crate::dependent_module;
use wasm_bindgen::prelude::*;

use crate::traits::{DeviceTrait, HostTrait, StreamTrait};
use crate::{
    BackendSpecificError, BuildStreamError, ChannelCount, Data, DefaultStreamConfigError,
    DeviceDescription, DeviceDescriptionBuilder, DeviceId, DeviceIdError, DeviceNameError,
    DevicesError, InputCallbackInfo, OutputCallbackInfo, PauseStreamError, PlayStreamError,
    SampleFormat, SampleRate, StreamConfig, StreamError, SupportedBufferSize,
    SupportedStreamConfig, SupportedStreamConfigRange, SupportedStreamConfigsError,
};

use std::time::Duration;

/// Content is false if the iterator is empty.
pub struct Devices(bool);

#[derive(Clone, Debug, PartialEq, Eq, Hash)]
pub struct Device;

pub struct Host;

pub struct Stream {
    audio_context: web_sys::AudioContext,
}

pub use crate::iter::{SupportedInputConfigs, SupportedOutputConfigs};

const MIN_CHANNELS: ChannelCount = 1;
const MAX_CHANNELS: ChannelCount = 32;
const MIN_SAMPLE_RATE: SampleRate = 8_000;
const MAX_SAMPLE_RATE: SampleRate = 96_000;
const DEFAULT_SAMPLE_RATE: SampleRate = 44_100;
const SUPPORTED_SAMPLE_FORMAT: SampleFormat = SampleFormat::F32;

impl Host {
    pub fn new() -> Result<Self, crate::HostUnavailable> {
        if Self::is_available() {
            Ok(Host)
        } else {
            Err(crate::HostUnavailable)
        }
    }
}

impl HostTrait for Host {
    type Devices = Devices;
    type Device = Device;

    fn is_available() -> bool {
        if let Some(window) = web_sys::window() {
            let has_audio_worklet =
                js_sys::Reflect::has(&window, &JsValue::from_str("AudioWorklet")).unwrap_or(false);

            let cross_origin_isolated =
                js_sys::Reflect::get(&window, &JsValue::from_str("crossOriginIsolated"))
                    .ok()
                    .and_then(|v| v.as_bool())
                    .unwrap_or(false);

            has_audio_worklet && cross_origin_isolated
        } else {
            false
        }
    }

    fn devices(&self) -> Result<Self::Devices, DevicesError> {
        Devices::new()
    }

    fn default_input_device(&self) -> Option<Self::Device> {
        // TODO
        None
    }

    fn default_output_device(&self) -> Option<Self::Device> {
        Some(Device)
    }
}

impl Devices {
    fn new() -> Result<Self, DevicesError> {
        Ok(Self::default())
    }
}

impl DeviceTrait for Device {
    type SupportedInputConfigs = SupportedInputConfigs;
    type SupportedOutputConfigs = SupportedOutputConfigs;
    type Stream = Stream;

    #[inline]
    fn description(&self) -> Result<DeviceDescription, DeviceNameError> {
        Ok(DeviceDescriptionBuilder::new("Default Device".to_string())
            .direction(crate::DeviceDirection::Output)
            .build())
    }

    #[inline]
    fn id(&self) -> Result<DeviceId, DeviceIdError> {
        Ok(DeviceId(
            crate::platform::HostId::AudioWorklet,
            "default".to_string(),
        ))
    }

    #[inline]
    fn supported_input_configs(
        &self,
    ) -> Result<Self::SupportedInputConfigs, SupportedStreamConfigsError> {
        // TODO
        Ok(Vec::new().into_iter())
    }

    #[inline]
    fn supported_output_configs(
        &self,
    ) -> Result<Self::SupportedOutputConfigs, SupportedStreamConfigsError> {
        let buffer_size = SupportedBufferSize::Unknown;

        // In actuality the number of supported channels cannot be fully known until
        // the browser attempts to initialized the AudioWorklet.

        let configs: Vec<_> = (MIN_CHANNELS..=MAX_CHANNELS)
            .map(|channels| SupportedStreamConfigRange {
                channels,
                min_sample_rate: MIN_SAMPLE_RATE,
                max_sample_rate: MAX_SAMPLE_RATE,
                buffer_size,
                sample_format: SUPPORTED_SAMPLE_FORMAT,
            })
            .collect();
        Ok(configs.into_iter())
    }

    #[inline]
    fn default_input_config(&self) -> Result<SupportedStreamConfig, DefaultStreamConfigError> {
        // TODO
        Err(DefaultStreamConfigError::StreamTypeNotSupported)
    }

    #[inline]
    fn default_output_config(&self) -> Result<SupportedStreamConfig, DefaultStreamConfigError> {
        const EXPECT: &str = "expected at least one valid webaudio stream config";
        let config = self
            .supported_output_configs()
            .expect(EXPECT)
            .max_by(|a, b| a.cmp_default_heuristics(b))
            .unwrap()
            .with_sample_rate(DEFAULT_SAMPLE_RATE);

        Ok(config)
    }

    fn build_input_stream_raw<D, E>(
        &self,
        _config: StreamConfig,
        _sample_format: SampleFormat,
        _data_callback: D,
        _error_callback: E,
        _timeout: Option<Duration>,
    ) -> Result<Self::Stream, BuildStreamError>
    where
        D: FnMut(&Data, &InputCallbackInfo) + Send + 'static,
        E: FnMut(StreamError) + Send + 'static,
    {
        // TODO
        Err(BuildStreamError::StreamConfigNotSupported)
    }

    /// Create an output stream.
    fn build_output_stream_raw<D, E>(
        &self,
        config: StreamConfig,
        sample_format: SampleFormat,
        mut data_callback: D,
        mut error_callback: E,
        _timeout: Option<Duration>,
    ) -> Result<Self::Stream, BuildStreamError>
    where
        D: FnMut(&mut Data, &OutputCallbackInfo) + Send + 'static,
        E: FnMut(StreamError) + Send + 'static,
    {
        if !valid_config(config, sample_format) {
            return Err(BuildStreamError::StreamConfigNotSupported);
        }

        let stream_opts = web_sys::AudioContextOptions::new();
        stream_opts.set_sample_rate(config.sample_rate as f32);

        let audio_context = web_sys::AudioContext::new_with_context_options(&stream_opts).map_err(
            |err| -> BuildStreamError {
                let description = format!("{err:?}");
                let err = BackendSpecificError { description };
                err.into()
            },
        )?;

        let destination = audio_context.destination();

        // If possible, set the destination's channel_count to the given config.channel.
        // If not, fallback on the default destination channel_count to keep previous behavior
        // and do not return an error.
        if config.channels as u32 <= destination.max_channel_count() {
            destination.set_channel_count(config.channels as u32);
        }

        let ctx = audio_context.clone();
        wasm_bindgen_futures::spawn_local(async move {
            let result: Result<(), JsValue> = async move {
                let mod_url = dependent_module!("worklet.js")?;
                wasm_bindgen_futures::JsFuture::from(ctx.audio_worklet()?.add_module(&mod_url)?)
                    .await?;

                let options = web_sys::AudioWorkletNodeOptions::new();

                let js_array = js_sys::Array::new();
                js_array.push(&JsValue::from_f64(destination.channel_count() as _));

                options.set_output_channel_count(&js_array);
                options.set_number_of_inputs(0);

                // Capture audio output latency here: the closure runs in a separate worker and cannot access AudioContext properties directly.
                // While baseLatency is fixed for the context lifetime, outputLatency can change but not be re-read from inside the worklet;
                // we snapshot it here.
                let base_latency_secs =
                    js_sys::Reflect::get(ctx.as_ref(), &JsValue::from("baseLatency"))
                        .ok()
                        .and_then(|v| v.as_f64())
                        .unwrap_or(0.0);
                let output_latency_secs =
                    js_sys::Reflect::get(ctx.as_ref(), &JsValue::from("outputLatency"))
                        .ok()
                        .and_then(|v| v.as_f64())
                        .unwrap_or(0.0);
                let total_output_latency_secs = {
                    let sum = base_latency_secs + output_latency_secs;
                    if sum.is_finite() { sum.max(0.0) } else { 0.0 }
                };

                options.set_processor_options(Some(&js_sys::Array::of3(
                    &wasm_bindgen::module(),
                    &wasm_bindgen::memory(),
                    &WasmAudioProcessor::new(Box::new(
                        move |interleaved_data, frame_size, sample_rate, now| {
                            let data = interleaved_data.as_mut_ptr() as *mut ();
                            let mut data = unsafe {
                                Data::from_parts(data, interleaved_data.len(), sample_format)
                            };

                            let callback = crate::StreamInstant::from_secs_f64(now);
                            let buffer_duration = frames_to_duration(frame_size as _, sample_rate);
                            let playback = callback
                                .add(buffer_duration + Duration::from_secs_f64(total_output_latency_secs))
                                .expect(
                                "`playback` occurs beyond representation supported by `StreamInstant`",
                            );
                            let timestamp = crate::OutputStreamTimestamp { callback, playback };
                            let info = OutputCallbackInfo { timestamp };
                            (data_callback)(&mut data, &info);
                        },
                    ))
                    .pack()
                    .into(),
                )));
                // This name 'CpalProcessor' must match the name registered in worklet.js
                let audio_worklet_node =
                    web_sys::AudioWorkletNode::new_with_options(&ctx, "CpalProcessor", &options)?;

                audio_worklet_node.connect_with_audio_node(&destination)?;
                Ok(())
            }
            .await;

            if let Err(err) = result {
                let description = if let Some(string_value) = err.as_string() {
                    string_value
                } else {
                    format!("Browser error initializing stream: {err:?}")
                };

                error_callback(StreamError::BackendSpecific {
                    err: BackendSpecificError { description },
                })
            }
        });

        Ok(Stream { audio_context })
    }
}

impl StreamTrait for Stream {
    fn play(&self) -> Result<(), PlayStreamError> {
        match self.audio_context.resume() {
            Ok(_) => Ok(()),
            Err(err) => {
                let description = format!("{err:?}");
                let err = BackendSpecificError { description };
                Err(err.into())
            }
        }
    }

    fn pause(&self) -> Result<(), PauseStreamError> {
        match self.audio_context.suspend() {
            Ok(_) => Ok(()),
            Err(err) => {
                let description = format!("{err:?}");
                let err = BackendSpecificError { description };
                Err(err.into())
            }
        }
    }
}

impl Drop for Stream {
    fn drop(&mut self) {
        let _ = self.audio_context.close();
    }
}

impl Default for Devices {
    fn default() -> Devices {
        Devices(true)
    }
}

impl Iterator for Devices {
    type Item = Device;
    #[inline]
    fn next(&mut self) -> Option<Device> {
        if self.0 {
            self.0 = false;
            Some(Device)
        } else {
            None
        }
    }
}

// Whether or not the given stream configuration is valid for building a stream.
fn valid_config(conf: StreamConfig, sample_format: SampleFormat) -> bool {
    conf.channels <= MAX_CHANNELS
        && conf.channels >= MIN_CHANNELS
        && conf.sample_rate <= MAX_SAMPLE_RATE
        && conf.sample_rate >= MIN_SAMPLE_RATE
        && sample_format == SUPPORTED_SAMPLE_FORMAT
}

// Convert the given duration in frames at the given sample rate to a `std::time::Duration`.
fn frames_to_duration(frames: usize, rate: crate::SampleRate) -> std::time::Duration {
    let secsf = frames as f64 / rate as f64;
    let secs = secsf as u64;
    let nanos = ((secsf - secs as f64) * 1_000_000_000.0) as u32;
    std::time::Duration::new(secs, nanos)
}

type AudioProcessorCallback = Box<dyn FnMut(&mut [f32], u32, u32, f64)>;

/// WasmAudioProcessor provides an interface for the Javascript code
/// running in the AudioWorklet to interact with Rust.
#[wasm_bindgen]
pub struct WasmAudioProcessor {
    #[wasm_bindgen(skip)]
    interleaved_buffer: Vec<f32>,
    #[wasm_bindgen(skip)]
    // Passes in an interleaved scratch buffer, frame size, sample rate, and current time.
    callback: AudioProcessorCallback,
}

impl WasmAudioProcessor {
    pub fn new(callback: AudioProcessorCallback) -> Self {
        Self {
            interleaved_buffer: Vec::new(),
            callback,
        }
    }
}

#[wasm_bindgen]
impl WasmAudioProcessor {
    pub fn process(
        &mut self,
        channels: u32,
        frame_size: u32,
        sample_rate: u32,
        current_time: f64,
    ) -> u32 {
        let frame_size = frame_size as usize;

        // Ensure there's enough space in the output buffer
        // This likely only occurs once, or very few times.
        let interleaved_buffer_size = channels as usize * frame_size;
        self.interleaved_buffer.resize(
            interleaved_buffer_size.max(self.interleaved_buffer.len()),
            0.0,
        );

        (self.callback)(
            &mut self.interleaved_buffer[..interleaved_buffer_size],
            frame_size as u32,
            sample_rate,
            current_time,
        );

        // Returns a pointer to the raw interleaved buffer to Javascript so
        // it can deinterleave it into the output buffers.
        //
        // Deinterleaving is done on the Javascript side because it's simpler and it may be faster.
        // Doing it this way avoids an extra copy and the JS deinterleaving code
        // is likely heavily optimized by the browser's JS engine,
        // although I have not tested that assumption.
        self.interleaved_buffer.as_mut_ptr() as _
    }

    /// Converts this `WasmAudioProcessor` into a raw pointer (as `usize`) for FFI use.
    ///
    /// # Purpose
    /// This function is intended to transfer ownership of the processor instance to the caller,
    /// typically for passing between Rust and JavaScript via WebAssembly.
    ///
    /// # Relationship with [`unpack`]
    /// The returned pointer must be passed to [`unpack`] exactly once to recover the original
    /// `WasmAudioProcessor` instance. Failing to do so will result in a memory leak. Calling
    /// [`unpack`] more than once or using the pointer after it has been unpacked will result in
    /// undefined behavior.
    ///
    /// # Safety and Lifetime
    /// After calling `pack`, the caller is responsible for ensuring that `unpack` is called
    /// exactly once, and that the pointer is not used after being unpacked. This function
    /// should be used with care, as improper use can lead to memory safety issues.
    ///
    /// [`unpack`]: Self::unpack
    pub fn pack(self) -> usize {
        Box::into_raw(Box::new(self)) as usize
    }
    /// # Safety
    ///
    /// The `val` parameter must be a value previously returned by `Self::pack`.
    /// It must not have already been unpacked or deallocated, and must not be used after this call.
    /// Using an invalid or already-consumed pointer will result in undefined behavior.
    pub unsafe fn unpack(val: usize) -> Self {
        *Box::from_raw(val as *mut _)
    }
}
```

## File: `src/host/audioworklet/worklet.js`
```javascript
registerProcessor("CpalProcessor", class WasmProcessor extends AudioWorkletProcessor {
    constructor(options) {
        super();
        let [module, memory, handle] = options.processorOptions;
        bindgen.initSync({ module, memory });
        this.processor = bindgen.WasmAudioProcessor.unpack(handle);
        this.memory = memory;
        this.wasm_memory = new Float32Array(memory.buffer);
    }

    process(inputs, outputs) {
        // Check if memory grew and update view
        if (this.wasm_memory.buffer !== this.memory.buffer) {
            this.wasm_memory = new Float32Array(this.memory.buffer);
        }

        const channels = outputs[0];
        const channels_count = channels.length;
        const frame_size = channels[0].length;
        const interleaved_ptr = this.processor.process(
            channels_count,
            frame_size,
            sampleRate,
            currentTime
        );

        const interleaved_start = interleaved_ptr / 4; // Convert byte offset to f32 index
        const interleaved = this.wasm_memory;

        const total_samples = frame_size * channels_count;
        if (interleaved_start + total_samples > this.wasm_memory.length) {
            console.error("CpalProcessor: Audio buffer out of bounds! Ptr:", interleaved_ptr, "Len:", total_samples);
            return false; // Safely stop the node
        }

        // Deinterleave: read strided from Wasm, write sequential to output
        for (let ch = 0; ch < channels_count; ch++) {
            const channel = channels[ch];
            let read_pos = interleaved_start + ch;

            for (let i = 0; i < frame_size; i++) {
                channel[i] = interleaved[read_pos];
                read_pos += channels_count;
            }
        }

        return true;
    }
});
```

## File: `src/host/coreaudio/mod.rs`
```rust
//! CoreAudio backend implementation.
//!
//! Default backend on macOS and iOS.

use objc2_core_audio_types::{
    kAudioFormatFlagIsFloat, kAudioFormatFlagIsPacked, kAudioFormatFlagIsSignedInteger,
    kAudioFormatLinearPCM, AudioStreamBasicDescription,
};

use crate::DefaultStreamConfigError;
use crate::{BuildStreamError, SupportedStreamConfigsError};

use crate::{BackendSpecificError, SampleFormat, StreamConfig};

#[cfg(target_os = "ios")]
mod ios;
#[cfg(target_os = "macos")]
mod macos;

#[cfg(target_os = "ios")]
#[allow(unused_imports)]
pub use self::ios::{
    enumerate::{Devices, SupportedInputConfigs, SupportedOutputConfigs},
    Device, Host, Stream,
};

#[cfg(target_os = "macos")]
pub use self::macos::{Host, Stream};

// Common helper methods used by both macOS and iOS

fn check_os_status(os_status: OSStatus) -> Result<(), BackendSpecificError> {
    match coreaudio::Error::from_os_status(os_status) {
        Ok(()) => Ok(()),
        Err(err) => {
            let description = err.to_string();
            Err(BackendSpecificError { description })
        }
    }
}

// Create a coreaudio AudioStreamBasicDescription from a CPAL Format.
fn asbd_from_config(
    config: StreamConfig,
    sample_format: SampleFormat,
) -> AudioStreamBasicDescription {
    let n_channels = config.channels as usize;
    let sample_rate = config.sample_rate;
    let bytes_per_channel = sample_format.sample_size();
    let bits_per_channel = bytes_per_channel * 8;
    let bytes_per_frame = n_channels * bytes_per_channel;
    let frames_per_packet = 1;
    let bytes_per_packet = frames_per_packet * bytes_per_frame;
    let format_flags = match sample_format {
        SampleFormat::F32 | SampleFormat::F64 => kAudioFormatFlagIsFloat | kAudioFormatFlagIsPacked,
        SampleFormat::I8
        | SampleFormat::I16
        | SampleFormat::I24
        | SampleFormat::I32
        | SampleFormat::I64 => kAudioFormatFlagIsSignedInteger | kAudioFormatFlagIsPacked,
        _ => kAudioFormatFlagIsPacked,
    };
    AudioStreamBasicDescription {
        mBitsPerChannel: bits_per_channel as _,
        mBytesPerFrame: bytes_per_frame as _,
        mChannelsPerFrame: n_channels as _,
        mBytesPerPacket: bytes_per_packet as _,
        mFramesPerPacket: frames_per_packet as _,
        mFormatFlags: format_flags,
        mFormatID: kAudioFormatLinearPCM,
        mSampleRate: sample_rate as _,
        mReserved: 0,
    }
}

#[inline]
fn host_time_to_stream_instant(
    m_host_time: u64,
) -> Result<crate::StreamInstant, BackendSpecificError> {
    let mut info: mach2::mach_time::mach_timebase_info = Default::default();
    let res = unsafe { mach2::mach_time::mach_timebase_info(&mut info) };
    check_os_status(res)?;
    let nanos = m_host_time as u128 * info.numer as u128 / info.denom as u128;
    crate::StreamInstant::from_nanos_i128(nanos as i128).ok_or(BackendSpecificError {
        description: "host time out of range of `StreamInstant` representation".to_string(),
    })
}

// Convert the given duration in frames at the given sample rate to a `std::time::Duration`.
#[inline]
fn frames_to_duration(frames: usize, rate: crate::SampleRate) -> std::time::Duration {
    let secsf = frames as f64 / rate as f64;
    let secs = secsf as u64;
    let nanos = ((secsf - secs as f64) * 1_000_000_000.0) as u32;
    std::time::Duration::new(secs, nanos)
}

// TODO need stronger error identification
impl From<coreaudio::Error> for BuildStreamError {
    fn from(err: coreaudio::Error) -> BuildStreamError {
        match err {
            coreaudio::Error::RenderCallbackBufferFormatDoesNotMatchAudioUnitStreamFormat
            | coreaudio::Error::NoKnownSubtype
            | coreaudio::Error::AudioUnit(coreaudio::error::AudioUnitError::FormatNotSupported)
            | coreaudio::Error::AudioCodec(_)
            | coreaudio::Error::AudioFormat(_) => BuildStreamError::StreamConfigNotSupported,
            _ => BuildStreamError::DeviceNotAvailable,
        }
    }
}

impl From<coreaudio::Error> for SupportedStreamConfigsError {
    fn from(err: coreaudio::Error) -> SupportedStreamConfigsError {
        let description = format!("{err}");
        let err = BackendSpecificError { description };
        // Check for possible DeviceNotAvailable variant
        SupportedStreamConfigsError::BackendSpecific { err }
    }
}

impl From<coreaudio::Error> for DefaultStreamConfigError {
    fn from(err: coreaudio::Error) -> DefaultStreamConfigError {
        let description = format!("{err}");
        let err = BackendSpecificError { description };
        // Check for possible DeviceNotAvailable variant
        DefaultStreamConfigError::BackendSpecific { err }
    }
}

pub(crate) type OSStatus = i32;

// Compile-time assertion that Stream is Send and Sync
crate::assert_stream_send!(Stream);
crate::assert_stream_sync!(Stream);
```

## File: `src/host/coreaudio/ios/enumerate.rs`
```rust
use std::vec::IntoIter as VecIntoIter;

use super::Device;

pub use crate::iter::{SupportedInputConfigs, SupportedOutputConfigs};

// TODO: Support enumerating earpiece vs headset vs speaker etc?
pub struct Devices(VecIntoIter<Device>);

impl Devices {
    pub fn new() -> Self {
        Self::default()
    }
}

impl Default for Devices {
    fn default() -> Devices {
        Devices(vec![Device].into_iter())
    }
}

impl Iterator for Devices {
    type Item = Device;

    fn next(&mut self) -> Option<Device> {
        self.0.next()
    }
}

pub fn default_input_device() -> Option<Device> {
    Some(Device)
}

pub fn default_output_device() -> Option<Device> {
    Some(Device)
}
```

## File: `src/host/coreaudio/ios/mod.rs`
```rust
//! CoreAudio implementation for iOS using AVAudioSession and RemoteIO Audio Units.

use std::sync::Mutex;

use coreaudio::audio_unit::render_callback::data;
use coreaudio::audio_unit::{render_callback, AudioUnit, Element, Scope};
use objc2_audio_toolbox::{kAudioOutputUnitProperty_EnableIO, kAudioUnitProperty_StreamFormat};
use objc2_core_audio_types::AudioBuffer;

use objc2_avf_audio::AVAudioSession;

use super::{asbd_from_config, frames_to_duration, host_time_to_stream_instant};
use crate::traits::{DeviceTrait, HostTrait, StreamTrait};

use crate::{
    BackendSpecificError, BufferSize, BuildStreamError, ChannelCount, Data,
    DefaultStreamConfigError, DeviceDescription, DeviceDescriptionBuilder, DeviceId, DeviceIdError,
    DeviceNameError, DevicesError, InputCallbackInfo, OutputCallbackInfo, PauseStreamError,
    PlayStreamError, SampleFormat, SampleRate, StreamConfig, StreamError, SupportedBufferSize,
    SupportedStreamConfig, SupportedStreamConfigRange, SupportedStreamConfigsError,
};

use self::enumerate::{
    default_input_device, default_output_device, Devices, SupportedInputConfigs,
    SupportedOutputConfigs,
};
use std::ptr::NonNull;
use std::time::Duration;

pub mod enumerate;

// These days the default of iOS is now F32 and no longer I16
const SUPPORTED_SAMPLE_FORMAT: SampleFormat = SampleFormat::F32;

#[derive(Clone, Debug, PartialEq, Eq, Hash)]
pub struct Device;

pub struct Host;

impl Host {
    pub fn new() -> Result<Self, crate::HostUnavailable> {
        Ok(Host)
    }
}

impl HostTrait for Host {
    type Devices = Devices;
    type Device = Device;

    fn is_available() -> bool {
        true
    }

    fn devices(&self) -> Result<Self::Devices, DevicesError> {
        Ok(Devices::new())
    }

    fn default_input_device(&self) -> Option<Self::Device> {
        default_input_device()
    }

    fn default_output_device(&self) -> Option<Self::Device> {
        default_output_device()
    }
}

impl Device {
    fn description(&self) -> Result<DeviceDescription, DeviceNameError> {
        // Query AVAudioSession to determine actual input/output availability
        // SAFETY: AVAudioSession::sharedInstance() returns the global audio session singleton
        let direction = unsafe {
            let audio_session = AVAudioSession::sharedInstance();
            let input_channels = Some(audio_session.inputNumberOfChannels() as ChannelCount);
            let output_channels = Some(audio_session.outputNumberOfChannels() as ChannelCount);

            crate::device_description::direction_from_counts(input_channels, output_channels)
        };

        Ok(DeviceDescriptionBuilder::new("Default Device".to_string())
            .direction(direction)
            .build())
    }

    fn id(&self) -> Result<DeviceId, DeviceIdError> {
        Ok(DeviceId(
            crate::platform::HostId::CoreAudio,
            "default".to_string(),
        ))
    }

    fn supported_input_configs(
        &self,
    ) -> Result<SupportedInputConfigs, SupportedStreamConfigsError> {
        Ok(get_supported_stream_configs(true))
    }

    fn supported_output_configs(
        &self,
    ) -> Result<SupportedOutputConfigs, SupportedStreamConfigsError> {
        Ok(get_supported_stream_configs(false))
    }

    fn default_input_config(&self) -> Result<SupportedStreamConfig, DefaultStreamConfigError> {
        // Get the primary (exact channel count) config from supported configs
        get_supported_stream_configs(true)
            .next()
            .map(|range| range.with_max_sample_rate())
            .ok_or(DefaultStreamConfigError::StreamTypeNotSupported)
    }

    fn default_output_config(&self) -> Result<SupportedStreamConfig, DefaultStreamConfigError> {
        // Get the maximum channel count config from supported configs
        get_supported_stream_configs(false)
            .last()
            .map(|range| range.with_max_sample_rate())
            .ok_or(DefaultStreamConfigError::StreamTypeNotSupported)
    }
}

impl DeviceTrait for Device {
    type SupportedInputConfigs = SupportedInputConfigs;
    type SupportedOutputConfigs = SupportedOutputConfigs;
    type Stream = Stream;

    fn description(&self) -> Result<DeviceDescription, DeviceNameError> {
        Device::description(self)
    }

    fn id(&self) -> Result<DeviceId, DeviceIdError> {
        Device::id(self)
    }

    fn supported_input_configs(
        &self,
    ) -> Result<Self::SupportedInputConfigs, SupportedStreamConfigsError> {
        Device::supported_input_configs(self)
    }

    fn supported_output_configs(
        &self,
    ) -> Result<Self::SupportedOutputConfigs, SupportedStreamConfigsError> {
        Device::supported_output_configs(self)
    }

    fn default_input_config(&self) -> Result<SupportedStreamConfig, DefaultStreamConfigError> {
        Device::default_input_config(self)
    }

    fn default_output_config(&self) -> Result<SupportedStreamConfig, DefaultStreamConfigError> {
        Device::default_output_config(self)
    }

    fn build_input_stream_raw<D, E>(
        &self,
        config: StreamConfig,
        sample_format: SampleFormat,
        data_callback: D,
        error_callback: E,
        _timeout: Option<Duration>,
    ) -> Result<Self::Stream, BuildStreamError>
    where
        D: FnMut(&Data, &InputCallbackInfo) + Send + 'static,
        E: FnMut(StreamError) + Send + 'static,
    {
        // Configure buffer size and create audio unit
        let mut audio_unit = setup_stream_audio_unit(config, sample_format, true)?;

        // Query device buffer size for latency calculation
        let device_buffer_frames = Some(get_device_buffer_frames());

        // Set up input callback
        setup_input_callback(
            &mut audio_unit,
            sample_format,
            config.sample_rate,
            device_buffer_frames,
            data_callback,
            error_callback,
        )?;

        audio_unit.start()?;

        Ok(Stream::new(StreamInner {
            playing: true,
            audio_unit,
        }))
    }

    /// Create an output stream.
    fn build_output_stream_raw<D, E>(
        &self,
        config: StreamConfig,
        sample_format: SampleFormat,
        data_callback: D,
        error_callback: E,
        _timeout: Option<Duration>,
    ) -> Result<Self::Stream, BuildStreamError>
    where
        D: FnMut(&mut Data, &OutputCallbackInfo) + Send + 'static,
        E: FnMut(StreamError) + Send + 'static,
    {
        // Configure buffer size and create audio unit
        let mut audio_unit = setup_stream_audio_unit(config, sample_format, false)?;

        // Query device buffer size for latency calculation
        let device_buffer_frames = Some(get_device_buffer_frames());

        // Set up output callback
        setup_output_callback(
            &mut audio_unit,
            sample_format,
            config.sample_rate,
            device_buffer_frames,
            data_callback,
            error_callback,
        )?;

        audio_unit.start()?;

        Ok(Stream::new(StreamInner {
            playing: true,
            audio_unit,
        }))
    }
}

pub struct Stream {
    inner: Mutex<StreamInner>,
}

impl Stream {
    fn new(inner: StreamInner) -> Self {
        Self {
            inner: Mutex::new(inner),
        }
    }
}

impl StreamTrait for Stream {
    fn play(&self) -> Result<(), PlayStreamError> {
        let mut stream = self
            .inner
            .lock()
            .map_err(|_| PlayStreamError::BackendSpecific {
                err: BackendSpecificError {
                    description: "A cpal stream operation panicked while holding the lock - this is a bug, please report it".to_string(),
                },
            })?;

        if !stream.playing {
            if let Err(e) = stream.audio_unit.start() {
                let description = format!("{}", e);
                let err = BackendSpecificError { description };
                return Err(err.into());
            }
            stream.playing = true;
        }
        Ok(())
    }

    fn pause(&self) -> Result<(), PauseStreamError> {
        let mut stream = self
            .inner
            .lock()
            .map_err(|_| PauseStreamError::BackendSpecific {
                err: BackendSpecificError {
                    description: "A cpal stream operation panicked while holding the lock - this is a bug, please report it".to_string(),
                },
            })?;

        if stream.playing {
            if let Err(e) = stream.audio_unit.stop() {
                let description = format!("{}", e);
                let err = BackendSpecificError { description };
                return Err(err.into());
            }
            stream.playing = false;
        }
        Ok(())
    }

    fn buffer_size(&self) -> Option<crate::FrameCount> {
        Some(get_device_buffer_frames() as crate::FrameCount)
    }
}

struct StreamInner {
    playing: bool,
    audio_unit: AudioUnit,
}

fn create_audio_unit() -> Result<AudioUnit, coreaudio::Error> {
    AudioUnit::new(coreaudio::audio_unit::IOType::RemoteIO)
}

fn configure_for_recording(audio_unit: &mut AudioUnit) -> Result<(), coreaudio::Error> {
    // Enable mic recording
    let enable_input = 1u32;
    audio_unit.set_property(
        kAudioOutputUnitProperty_EnableIO,
        Scope::Input,
        Element::Input,
        Some(&enable_input),
    )?;

    // Disable output
    let disable_output = 0u32;
    audio_unit.set_property(
        kAudioOutputUnitProperty_EnableIO,
        Scope::Output,
        Element::Output,
        Some(&disable_output),
    )?;

    Ok(())
}

/// Configure AVAudioSession with the requested buffer size.
///
/// Note: iOS may not honor the exact request due to system constraints.
fn set_audio_session_buffer_size(
    buffer_size: u32,
    sample_rate: crate::SampleRate,
) -> Result<(), BuildStreamError> {
    // SAFETY: AVAudioSession::sharedInstance() returns the global audio session singleton
    let audio_session = unsafe { AVAudioSession::sharedInstance() };

    // Calculate preferred buffer duration in seconds
    let buffer_duration = buffer_size as f64 / sample_rate as f64;

    // Set the preferred IO buffer duration
    // SAFETY: setPreferredIOBufferDuration_error is safe to call with valid duration
    unsafe {
        audio_session
            .setPreferredIOBufferDuration_error(buffer_duration)
            .map_err(|_| BuildStreamError::StreamConfigNotSupported)?;
    }

    Ok(())
}

/// Get the actual buffer size from AVAudioSession.
///
/// This queries the current IO buffer duration from AVAudioSession and converts
/// it to frames based on the current sample rate.
fn get_device_buffer_frames() -> usize {
    // SAFETY: AVAudioSession methods are safe to call on the singleton instance
    unsafe {
        let audio_session = AVAudioSession::sharedInstance();
        let buffer_duration = audio_session.IOBufferDuration();
        let sample_rate = audio_session.sampleRate();
        (buffer_duration * sample_rate) as usize
    }
}

/// Get supported stream config ranges for input (is_input=true) or output (is_input=false).
fn get_supported_stream_configs(is_input: bool) -> std::vec::IntoIter<SupportedStreamConfigRange> {
    // SAFETY: AVAudioSession methods are safe to call on the singleton instance
    let (sample_rate, max_channels) = unsafe {
        let audio_session = AVAudioSession::sharedInstance();
        let sample_rate = audio_session.sampleRate() as u32;
        let max_channels = if is_input {
            audio_session.inputNumberOfChannels() as u16
        } else {
            audio_session.outputNumberOfChannels() as u16
        };
        (sample_rate, max_channels)
    };

    // Typical iOS hardware buffer frame limits according to Apple Technical Q&A QA1631.
    let buffer_size = SupportedBufferSize::Range {
        min: 256,
        max: 4096,
    };

    // For input, only return the exact channel count (no flexibility)
    // For output, support flexible channel counts up to the hardware maximum
    let min_channels = if is_input { max_channels } else { 1 };

    let configs: Vec<_> = (min_channels..=max_channels)
        .map(|channels| SupportedStreamConfigRange {
            channels,
            min_sample_rate: sample_rate,
            max_sample_rate: sample_rate,
            buffer_size,
            sample_format: SUPPORTED_SAMPLE_FORMAT,
        })
        .collect();

    configs.into_iter()
}

/// Setup audio unit with common configuration for input or output streams.
fn setup_stream_audio_unit(
    config: StreamConfig,
    sample_format: SampleFormat,
    is_input: bool,
) -> Result<AudioUnit, BuildStreamError> {
    // Configure buffer size via AVAudioSession
    if let BufferSize::Fixed(buffer_size) = config.buffer_size {
        set_audio_session_buffer_size(buffer_size, config.sample_rate)?;
    }

    let mut audio_unit = create_audio_unit()?;

    if is_input {
        audio_unit.uninitialize()?;
        configure_for_recording(&mut audio_unit)?;
        audio_unit.initialize()?;
    }

    // Set the stream format in interleaved mode
    // For input: Output scope of Input element (data coming out of input)
    // For output: Input scope of Output element (data going into output)
    let (scope, element) = if is_input {
        (Scope::Output, Element::Input)
    } else {
        (Scope::Input, Element::Output)
    };

    let asbd = asbd_from_config(config, sample_format);
    audio_unit.set_property(kAudioUnitProperty_StreamFormat, scope, element, Some(&asbd))?;

    Ok(audio_unit)
}

/// Extract AudioBuffer and convert to Data, handling differences between input and output.
///
/// # Safety
///
/// Caller must ensure:
/// - `args.data.data` points to valid AudioBufferList
/// - For input: AudioBufferList has at least one buffer
/// - Buffer data remains valid for the callback duration
#[inline]
unsafe fn extract_audio_buffer(
    args: &render_callback::Args<data::Raw>,
    bytes_per_channel: usize,
    sample_format: SampleFormat,
    is_input: bool,
) -> (AudioBuffer, Data) {
    let buffer = if is_input {
        // Input: access through buffer array
        let first_buf_ptr = core::ptr::addr_of!((*args.data.data).mBuffers) as *const AudioBuffer;
        core::ptr::read_unaligned(first_buf_ptr)
    } else {
        // Output: direct access
        let buf_ptr = core::ptr::addr_of!((*args.data.data).mBuffers[0]);
        core::ptr::read_unaligned(buf_ptr)
    };

    let mut data_ptr = buffer.mData as *mut ();
    let mut len = buffer.mDataByteSize as usize / bytes_per_channel;

    // SAFETY: slice::from_raw_parts requires a non-null pointer.
    if data_ptr.is_null() {
        data_ptr = NonNull::dangling().as_ptr();
        len = 0;
    }

    let data = Data::from_parts(data_ptr, len, sample_format);

    (buffer, data)
}

/// Setup input callback with proper latency calculation.
fn setup_input_callback<D, E>(
    audio_unit: &mut AudioUnit,
    sample_format: SampleFormat,
    sample_rate: SampleRate,
    device_buffer_frames: Option<usize>,
    mut data_callback: D,
    mut error_callback: E,
) -> Result<(), BuildStreamError>
where
    D: FnMut(&Data, &InputCallbackInfo) + Send + 'static,
    E: FnMut(StreamError) + Send + 'static,
{
    let bytes_per_channel = sample_format.sample_size();
    type Args = render_callback::Args<data::Raw>;

    audio_unit.set_input_callback(move |args: Args| {
        // SAFETY: CoreAudio provides valid AudioBufferList for the callback duration
        let (buffer, data) =
            unsafe { extract_audio_buffer(&args, bytes_per_channel, sample_format, true) };

        let callback = match host_time_to_stream_instant(args.time_stamp.mHostTime) {
            Err(err) => {
                error_callback(err.into());
                return Err(());
            }
            Ok(cb) => cb,
        };

        let latency_frames = device_buffer_frames.unwrap_or_else(|| {
            let channels = buffer.mNumberChannels as usize;
            if channels > 0 {
                data.len() / channels
            } else {
                0
            }
        });
        let delay = frames_to_duration(latency_frames, sample_rate);
        let capture = callback
            .sub(delay)
            .expect("`capture` occurs before origin of alsa `StreamInstant`");
        let timestamp = crate::InputStreamTimestamp { callback, capture };

        let info = InputCallbackInfo { timestamp };
        data_callback(&data, &info);
        Ok(())
    })?;

    Ok(())
}

/// Setup output callback with proper latency calculation.
fn setup_output_callback<D, E>(
    audio_unit: &mut AudioUnit,
    sample_format: SampleFormat,
    sample_rate: SampleRate,
    device_buffer_frames: Option<usize>,
    mut data_callback: D,
    mut error_callback: E,
) -> Result<(), BuildStreamError>
where
    D: FnMut(&mut Data, &OutputCallbackInfo) + Send + 'static,
    E: FnMut(StreamError) + Send + 'static,
{
    let bytes_per_channel = sample_format.sample_size();
    type Args = render_callback::Args<data::Raw>;

    audio_unit.set_render_callback(move |args: Args| {
        // SAFETY: CoreAudio provides valid AudioBufferList for the callback duration
        let (buffer, mut data) =
            unsafe { extract_audio_buffer(&args, bytes_per_channel, sample_format, false) };

        let callback = match host_time_to_stream_instant(args.time_stamp.mHostTime) {
            Err(err) => {
                error_callback(err.into());
                return Err(());
            }
            Ok(cb) => cb,
        };

        let latency_frames = device_buffer_frames.unwrap_or_else(|| {
            let channels = buffer.mNumberChannels as usize;
            if channels > 0 {
                data.len() / channels
            } else {
                0
            }
        });
        let delay = frames_to_duration(latency_frames, sample_rate);
        let playback = callback
            .add(delay)
            .expect("`playback` occurs beyond representation supported by `StreamInstant`");
        let timestamp = crate::OutputStreamTimestamp { callback, playback };

        let info = OutputCallbackInfo { timestamp };
        data_callback(&mut data, &info);
        Ok(())
    })?;

    Ok(())
}

#[cfg(test)]
mod tests {
    use crate::{BufferSize, SampleRate, StreamConfig};

    #[test]
    fn test_ios_fixed_buffer_size() {
        let host = crate::default_host();
        let device = host.default_output_device().unwrap();

        let config = StreamConfig {
            channels: 2,
            sample_rate: SampleRate(48000),
            buffer_size: BufferSize::Fixed(512),
        };

        let result = device.build_output_stream(
            &config,
            |_data: &mut [f32], _info: &crate::OutputCallbackInfo| {},
            |_err| {},
            None,
        );

        assert!(
            result.is_ok(),
            "BufferSize::Fixed should be supported on iOS via AVAudioSession"
        );
    }
}
```

## File: `src/host/coreaudio/macos/device.rs`
```rust
use super::OSStatus;
use super::Stream;
use super::{asbd_from_config, check_os_status, frames_to_duration, host_time_to_stream_instant};
use crate::host::coreaudio::macos::loopback::LoopbackDevice;
use crate::host::coreaudio::macos::StreamInner;
use crate::traits::DeviceTrait;
use crate::{
    BackendSpecificError, BufferSize, BuildStreamError, ChannelCount, Data,
    DefaultStreamConfigError, DeviceId, DeviceIdError, DeviceNameError, InputCallbackInfo,
    OutputCallbackInfo, SampleFormat, SampleRate, StreamConfig, StreamError, SupportedBufferSize,
    SupportedStreamConfig, SupportedStreamConfigRange, SupportedStreamConfigsError,
};
use coreaudio::audio_unit::render_callback::{self, data};
use coreaudio::audio_unit::{AudioUnit, Element, Scope};
use objc2_audio_toolbox::{
    kAudioOutputUnitProperty_CurrentDevice, kAudioOutputUnitProperty_EnableIO,
    kAudioUnitProperty_StreamFormat,
};
use objc2_core_audio::kAudioDevicePropertyDeviceUID;
use objc2_core_audio::kAudioObjectPropertyElementMain;
use objc2_core_audio::{
    kAudioAggregateDeviceClassID, kAudioDevicePropertyAvailableNominalSampleRates,
    kAudioDevicePropertyBufferFrameSize, kAudioDevicePropertyBufferFrameSizeRange,
    kAudioDevicePropertyLatency, kAudioDevicePropertyNominalSampleRate,
    kAudioDevicePropertySafetyOffset, kAudioDevicePropertyStreamConfiguration,
    kAudioDevicePropertyStreamFormat, kAudioObjectPropertyClass, kAudioObjectPropertyElementMaster,
    kAudioObjectPropertyScopeGlobal, kAudioObjectPropertyScopeInput,
    kAudioObjectPropertyScopeOutput, AudioClassID, AudioDeviceID, AudioObjectGetPropertyData,
    AudioObjectGetPropertyDataSize, AudioObjectID, AudioObjectPropertyAddress,
    AudioObjectPropertyScope, AudioObjectSetPropertyData,
};
use objc2_core_audio_types::{
    AudioBuffer, AudioBufferList, AudioStreamBasicDescription, AudioValueRange,
};
use objc2_core_foundation::CFString;
use objc2_core_foundation::Type;

pub use super::enumerate::{
    default_input_device, default_output_device, SupportedInputConfigs, SupportedOutputConfigs,
};
use std::fmt;
use std::mem::{self, size_of};
use std::ptr::{null, NonNull};
use std::sync::mpsc::{channel, RecvTimeoutError};
use std::sync::{Arc, Mutex};
use std::time::{Duration, Instant};

use super::invoke_error_callback;
use super::property_listener::AudioObjectPropertyListener;
use coreaudio::audio_unit::macos_helpers::get_device_name;

/// Attempt to set the device sample rate to the provided rate.
/// Return an error if the requested sample rate is not supported by the device.
fn set_sample_rate(
    audio_device_id: AudioObjectID,
    target_sample_rate: SampleRate,
) -> Result<(), BuildStreamError> {
    // Get the current sample rate.
    let mut property_address = AudioObjectPropertyAddress {
        mSelector: kAudioDevicePropertyNominalSampleRate,
        mScope: kAudioObjectPropertyScopeGlobal,
        mElement: kAudioObjectPropertyElementMaster,
    };
    let mut sample_rate: f64 = 0.0;
    let mut data_size = mem::size_of::<f64>() as u32;
    let status = unsafe {
        AudioObjectGetPropertyData(
            audio_device_id,
            NonNull::from(&property_address),
            0,
            null(),
            NonNull::from(&mut data_size),
            NonNull::from(&mut sample_rate).cast(),
        )
    };
    coreaudio::Error::from_os_status(status)?;

    // If the requested sample rate is different to the device sample rate, update the device.
    if sample_rate as u32 != target_sample_rate {
        // Get available sample rate ranges.
        property_address.mSelector = kAudioDevicePropertyAvailableNominalSampleRates;
        let mut data_size = 0u32;
        let status = unsafe {
            AudioObjectGetPropertyDataSize(
                audio_device_id,
                NonNull::from(&property_address),
                0,
                null(),
                NonNull::from(&mut data_size),
            )
        };
        coreaudio::Error::from_os_status(status)?;
        let n_ranges = data_size as usize / mem::size_of::<AudioValueRange>();
        let mut ranges: Vec<AudioValueRange> = Vec::with_capacity(n_ranges);
        let status = unsafe {
            AudioObjectGetPropertyData(
                audio_device_id,
                NonNull::from(&property_address),
                0,
                null(),
                NonNull::from(&mut data_size),
                NonNull::new(ranges.as_mut_ptr()).unwrap().cast(),
            )
        };
        coreaudio::Error::from_os_status(status)?;
        unsafe {
            ranges.set_len(n_ranges);
        }

        // Now that we have the available ranges, pick the one matching the desired rate.
        let sample_rate = target_sample_rate;
        if !ranges
            .iter()
            .any(|r| sample_rate as f64 >= r.mMinimum && sample_rate as f64 <= r.mMaximum)
        {
            return Err(BuildStreamError::StreamConfigNotSupported);
        }

        let (send, recv) = channel::<Result<f64, coreaudio::Error>>();
        let sample_rate_address = AudioObjectPropertyAddress {
            mSelector: kAudioDevicePropertyNominalSampleRate,
            mScope: kAudioObjectPropertyScopeGlobal,
            mElement: kAudioObjectPropertyElementMaster,
        };
        // Send sample rate updates back on a channel.
        let sample_rate_handler = move || {
            let mut rate: f64 = 0.0;
            let mut data_size = mem::size_of::<f64>() as u32;

            let result = unsafe {
                AudioObjectGetPropertyData(
                    audio_device_id,
                    NonNull::from(&sample_rate_address),
                    0,
                    null(),
                    NonNull::from(&mut data_size),
                    NonNull::from(&mut rate).cast(),
                )
            };
            send.send(coreaudio::Error::from_os_status(result).map(|_| rate))
                .ok();
        };

        let listener = AudioObjectPropertyListener::new(
            audio_device_id,
            sample_rate_address,
            sample_rate_handler,
        )?;

        // Finally, set the sample rate.
        property_address.mSelector = kAudioDevicePropertyNominalSampleRate;
        // Set the nominal sample rate using a single f64 as required by CoreAudio.
        let rate = sample_rate as f64;
        let data_size = mem::size_of::<f64>() as u32;
        let status = unsafe {
            AudioObjectSetPropertyData(
                audio_device_id,
                NonNull::from(&property_address),
                0,
                null(),
                data_size,
                NonNull::from(&rate).cast(),
            )
        };
        coreaudio::Error::from_os_status(status)?;

        // Wait for the reported_rate to change.
        //
        // This should not take longer than a few ms, but we timeout after 1 sec just in case.
        // We loop over potentially several events from the channel to ensure
        // that we catch the expected change in sample rate.
        let mut timeout = Duration::from_secs(1);
        let start = Instant::now();

        loop {
            match recv.recv_timeout(timeout) {
                Err(err) => {
                    let description = match err {
                        RecvTimeoutError::Disconnected => {
                            "sample rate listener channel disconnected unexpectedly"
                        }
                        RecvTimeoutError::Timeout => {
                            "timeout waiting for sample rate update for device"
                        }
                    }
                    .to_string();
                    return Err(BackendSpecificError { description }.into());
                }
                Ok(Ok(reported_sample_rate)) => {
                    if reported_sample_rate == target_sample_rate as f64 {
                        break;
                    }
                }
                Ok(Err(_)) => {
                    // TODO: should we consider collecting this error?
                }
            };
            timeout = timeout
                .checked_sub(start.elapsed())
                .unwrap_or(Duration::ZERO);
        }
        listener.remove()?;
    }
    Ok(())
}

fn audio_unit_from_device(device: &Device, input: bool) -> Result<AudioUnit, coreaudio::Error> {
    let output_type = if !input && is_default_output_device(device) {
        coreaudio::audio_unit::IOType::DefaultOutput
    } else {
        coreaudio::audio_unit::IOType::HalOutput
    };
    let mut audio_unit = AudioUnit::new(output_type)?;

    if input {
        // Enable input processing.
        let enable_input = 1u32;
        audio_unit.set_property(
            kAudioOutputUnitProperty_EnableIO,
            Scope::Input,
            Element::Input,
            Some(&enable_input),
        )?;

        // Disable output processing.
        let disable_output = 0u32;
        audio_unit.set_property(
            kAudioOutputUnitProperty_EnableIO,
            Scope::Output,
            Element::Output,
            Some(&disable_output),
        )?;
    }

    // Device selection is a device-level property: always use Scope::Global + Element::Output
    audio_unit.set_property(
        kAudioOutputUnitProperty_CurrentDevice,
        Scope::Global,
        Element::Output,
        Some(&device.audio_device_id),
    )?;

    Ok(audio_unit)
}

fn get_io_buffer_frame_size_range(
    audio_unit: &AudioUnit,
) -> Result<SupportedBufferSize, coreaudio::Error> {
    // Device-level property: always use Scope::Global + Element::Output
    // regardless of whether this audio unit is configured for input or output
    let buffer_size_range: AudioValueRange = audio_unit.get_property(
        kAudioDevicePropertyBufferFrameSizeRange,
        Scope::Global,
        Element::Output,
    )?;

    Ok(SupportedBufferSize::Range {
        min: buffer_size_range.mMinimum as u32,
        max: buffer_size_range.mMaximum as u32,
    })
}

impl DeviceTrait for Device {
    type SupportedInputConfigs = SupportedInputConfigs;
    type SupportedOutputConfigs = SupportedOutputConfigs;
    type Stream = Stream;

    fn description(&self) -> Result<crate::DeviceDescription, DeviceNameError> {
        Device::description(self)
    }

    fn id(&self) -> Result<DeviceId, DeviceIdError> {
        Device::id(self)
    }

    fn supported_input_configs(
        &self,
    ) -> Result<Self::SupportedInputConfigs, SupportedStreamConfigsError> {
        Device::supported_input_configs(self)
    }

    fn supported_output_configs(
        &self,
    ) -> Result<Self::SupportedOutputConfigs, SupportedStreamConfigsError> {
        Device::supported_output_configs(self)
    }

    fn default_input_config(&self) -> Result<SupportedStreamConfig, DefaultStreamConfigError> {
        Device::default_input_config(self)
    }

    fn default_output_config(&self) -> Result<SupportedStreamConfig, DefaultStreamConfigError> {
        Device::default_output_config(self)
    }

    fn build_input_stream_raw<D, E>(
        &self,
        config: StreamConfig,
        sample_format: SampleFormat,
        data_callback: D,
        error_callback: E,
        timeout: Option<Duration>,
    ) -> Result<Self::Stream, BuildStreamError>
    where
        D: FnMut(&Data, &InputCallbackInfo) + Send + 'static,
        E: FnMut(StreamError) + Send + 'static,
    {
        Device::build_input_stream_raw(
            self,
            config,
            sample_format,
            data_callback,
            error_callback,
            timeout,
        )
    }

    fn build_output_stream_raw<D, E>(
        &self,
        config: StreamConfig,
        sample_format: SampleFormat,
        data_callback: D,
        error_callback: E,
        timeout: Option<Duration>,
    ) -> Result<Self::Stream, BuildStreamError>
    where
        D: FnMut(&mut Data, &OutputCallbackInfo) + Send + 'static,
        E: FnMut(StreamError) + Send + 'static,
    {
        Device::build_output_stream_raw(
            self,
            config,
            sample_format,
            data_callback,
            error_callback,
            timeout,
        )
    }
}

#[derive(Clone, Eq, Hash, PartialEq)]
pub struct Device {
    pub(crate) audio_device_id: AudioDeviceID,
}

fn is_default_input_device(device: &Device) -> bool {
    default_input_device().is_some_and(|d| d.audio_device_id == device.audio_device_id)
}

fn is_default_output_device(device: &Device) -> bool {
    default_output_device().is_some_and(|d| d.audio_device_id == device.audio_device_id)
}

impl Device {
    /// Construct a new device given its ID.
    /// Useful for constructing hidden devices.
    pub fn new(audio_device_id: AudioDeviceID) -> Self {
        Self { audio_device_id }
    }

    /// Checks if this device is an aggregate device.
    ///
    /// Aggregate devices combine multiple physical devices into a single logical device.
    fn is_aggregate_device(&self) -> bool {
        let property_address = AudioObjectPropertyAddress {
            mSelector: kAudioObjectPropertyClass,
            mScope: kAudioObjectPropertyScopeGlobal,
            mElement: kAudioObjectPropertyElementMain,
        };

        let mut class_id: AudioClassID = 0;
        let data_size = size_of::<AudioClassID>() as u32;

        // SAFETY: AudioObjectGetPropertyData is documented to write an AudioClassID
        // for kAudioObjectPropertyClass. We check the status before using the value.
        let status = unsafe {
            AudioObjectGetPropertyData(
                self.audio_device_id,
                NonNull::from(&property_address),
                0,
                null(),
                NonNull::from(&data_size),
                NonNull::from(&mut class_id).cast(),
            )
        };

        // If successful, check if it's an aggregate device
        status == 0 && class_id == kAudioAggregateDeviceClassID
    }

    fn description(&self) -> Result<crate::DeviceDescription, DeviceNameError> {
        let name = get_device_name(self.audio_device_id).map_err(|err| {
            DeviceNameError::BackendSpecific {
                err: BackendSpecificError {
                    description: err.to_string(),
                },
            }
        })?;

        let input_configs = self
            .supported_input_configs()
            .map(|configs| configs.count() as ChannelCount)
            .ok();
        let output_configs = self
            .supported_output_configs()
            .map(|configs| configs.count() as ChannelCount)
            .ok();

        let direction =
            crate::device_description::direction_from_counts(input_configs, output_configs);

        let mut builder = crate::DeviceDescriptionBuilder::new(name).direction(direction);

        // Check if this is an aggregate device
        if self.is_aggregate_device() {
            builder = builder.interface_type(crate::InterfaceType::Aggregate);
        }

        Ok(builder.build())
    }

    fn id(&self) -> Result<DeviceId, DeviceIdError> {
        let property_address = AudioObjectPropertyAddress {
            mSelector: kAudioDevicePropertyDeviceUID,
            mScope: kAudioObjectPropertyScopeGlobal,
            mElement: kAudioObjectPropertyElementMain,
        };

        // CFString is copied from the audio object, use wrap_under_create_rule
        let mut uid: *mut CFString = std::ptr::null_mut();
        let mut data_size = size_of::<*mut CFString>() as u32;

        // SAFETY: AudioObjectGetPropertyData is documented to write a CFString pointer
        // for kAudioDevicePropertyDeviceUID. We check the status code before use.
        let status = unsafe {
            AudioObjectGetPropertyData(
                self.audio_device_id,
                NonNull::from(&property_address),
                0,
                null(),
                NonNull::from(&mut data_size),
                NonNull::from(&mut uid).cast(),
            )
        };
        check_os_status(status)?;

        // SAFETY: Status was successful, meaning the API call succeeded.
        // We now check if the returned uid is non-null before use.
        if !uid.is_null() {
            let uid_string = unsafe { CFString::wrap_under_create_rule(uid).to_string() };
            Ok(DeviceId(crate::platform::HostId::CoreAudio, uid_string))
        } else {
            Err(DeviceIdError::BackendSpecific {
                err: BackendSpecificError {
                    description: "Device UID is null".to_string(),
                },
            })
        }
    }

    // Logic re-used between `supported_input_configs` and `supported_output_configs`.
    #[allow(clippy::cast_ptr_alignment)]
    fn supported_configs(
        &self,
        scope: AudioObjectPropertyScope,
    ) -> Result<SupportedOutputConfigs, SupportedStreamConfigsError> {
        let mut property_address = AudioObjectPropertyAddress {
            mSelector: kAudioDevicePropertyStreamConfiguration,
            mScope: scope,
            mElement: kAudioObjectPropertyElementMaster,
        };

        unsafe {
            // Retrieve the devices audio buffer list.
            let mut data_size = 0u32;
            let status = AudioObjectGetPropertyDataSize(
                self.audio_device_id,
                NonNull::from(&property_address),
                0,
                null(),
                NonNull::from(&mut data_size),
            );
            check_os_status(status)?;

            let mut audio_buffer_list: Vec<u8> = vec![];
            audio_buffer_list.reserve_exact(data_size as usize);
            let status = AudioObjectGetPropertyData(
                self.audio_device_id,
                NonNull::from(&property_address),
                0,
                null(),
                NonNull::from(&mut data_size),
                NonNull::new(audio_buffer_list.as_mut_ptr()).unwrap().cast(),
            );
            check_os_status(status)?;

            let audio_buffer_list = audio_buffer_list.as_mut_ptr() as *mut AudioBufferList;

            // Read the number of buffers without assuming alignment (avoid UB).
            let nb_ptr = core::ptr::addr_of!((*audio_buffer_list).mNumberBuffers);
            let n_buffers = core::ptr::read_unaligned(nb_ptr) as usize;
            // If there are no buffers, skip.
            if n_buffers == 0 {
                return Ok(vec![].into_iter());
            }

            // Count the number of channels as the sum of all channels in all output buffers.
            let first_buf_ptr =
                core::ptr::addr_of!((*audio_buffer_list).mBuffers) as *const AudioBuffer;
            let mut n_channels = 0usize;
            for i in 0..n_buffers {
                let buf_ptr = first_buf_ptr.add(i);
                // Read potentially unaligned
                let buf: AudioBuffer = core::ptr::read_unaligned(buf_ptr);
                n_channels += buf.mNumberChannels as usize;
            }

            // TODO: macOS should support U8, I16, I32, F32 and F64. This should allow for using
            // I16 but just use F32 for now as it's the default anyway.
            let sample_format = SampleFormat::F32;

            // Get available sample rate ranges.
            // The property "kAudioDevicePropertyAvailableNominalSampleRates" returns a list of pairs of
            // minimum and maximum sample rates but most of the devices returns pairs of same values though the underlying mechanism is unclear.
            // This may cause issues when, for example, sorting the configs by the sample rates.
            // We follows the implementation of RtAudio, which returns single element of config
            // when all the pairs have the same values and returns multiple elements otherwise.
            // See https://github.com/thestk/rtaudio/blob/master/RtAudio.cpp#L1369C1-L1375C39

            property_address.mSelector = kAudioDevicePropertyAvailableNominalSampleRates;
            let mut data_size = 0u32;
            let status = AudioObjectGetPropertyDataSize(
                self.audio_device_id,
                NonNull::from(&property_address),
                0,
                null(),
                NonNull::from(&mut data_size),
            );
            check_os_status(status)?;

            let n_ranges = data_size as usize / mem::size_of::<AudioValueRange>();
            let mut ranges: Vec<AudioValueRange> = Vec::with_capacity(n_ranges);
            let status = AudioObjectGetPropertyData(
                self.audio_device_id,
                NonNull::from(&property_address),
                0,
                null(),
                NonNull::from(&mut data_size),
                NonNull::new(ranges.as_mut_ptr()).unwrap().cast(),
            );
            check_os_status(status)?;

            ranges.set_len(n_ranges);

            #[allow(non_upper_case_globals)]
            let input = match scope {
                kAudioObjectPropertyScopeInput => Ok(true),
                kAudioObjectPropertyScopeOutput => Ok(false),
                _ => Err(BackendSpecificError {
                    description: format!("unexpected scope (neither input nor output): {scope:?}"),
                }),
            }?;
            let audio_unit = audio_unit_from_device(self, input)?;
            let buffer_size = get_io_buffer_frame_size_range(&audio_unit)?;

            // Collect the supported formats for the device.

            let contains_different_sample_rates = ranges.iter().any(|r| r.mMinimum != r.mMaximum);
            if ranges.is_empty() {
                Ok(vec![].into_iter())
            } else if contains_different_sample_rates {
                let res = ranges.iter().map(|range| SupportedStreamConfigRange {
                    channels: n_channels as ChannelCount,
                    min_sample_rate: range.mMinimum as u32,
                    max_sample_rate: range.mMaximum as u32,
                    buffer_size,
                    sample_format,
                });
                Ok(res.collect::<Vec<_>>().into_iter())
            } else {
                let fmt = SupportedStreamConfigRange {
                    channels: n_channels as ChannelCount,
                    min_sample_rate: ranges
                        .iter()
                        .map(|v| v.mMinimum as u32)
                        .min()
                        .expect("the list must not be empty"),
                    max_sample_rate: ranges
                        .iter()
                        .map(|v| v.mMaximum as u32)
                        .max()
                        .expect("the list must not be empty"),
                    buffer_size,
                    sample_format,
                };

                Ok(vec![fmt].into_iter())
            }
        }
    }

    fn supported_input_configs(
        &self,
    ) -> Result<SupportedOutputConfigs, SupportedStreamConfigsError> {
        self.supported_configs(kAudioObjectPropertyScopeInput)
    }

    fn supported_output_configs(
        &self,
    ) -> Result<SupportedOutputConfigs, SupportedStreamConfigsError> {
        self.supported_configs(kAudioObjectPropertyScopeOutput)
    }

    fn default_config(
        &self,
        scope: AudioObjectPropertyScope,
    ) -> Result<SupportedStreamConfig, DefaultStreamConfigError> {
        fn default_config_error_from_os_status(
            status: OSStatus,
        ) -> Result<(), DefaultStreamConfigError> {
            let err = match coreaudio::Error::from_os_status(status) {
                Err(err) => err,
                Ok(_) => return Ok(()),
            };
            match err {
                coreaudio::Error::AudioUnit(
                    coreaudio::error::AudioUnitError::FormatNotSupported,
                )
                | coreaudio::Error::AudioCodec(_)
                | coreaudio::Error::AudioFormat(_) => {
                    Err(DefaultStreamConfigError::StreamTypeNotSupported)
                }
                coreaudio::Error::AudioUnit(coreaudio::error::AudioUnitError::NoConnection) => {
                    Err(DefaultStreamConfigError::DeviceNotAvailable)
                }
                err => {
                    let description = format!("{err}");
                    let err = BackendSpecificError { description };
                    Err(err.into())
                }
            }
        }

        let property_address = AudioObjectPropertyAddress {
            mSelector: kAudioDevicePropertyStreamFormat,
            mScope: scope,
            mElement: kAudioObjectPropertyElementMaster,
        };

        unsafe {
            let mut asbd: AudioStreamBasicDescription = mem::zeroed();
            let mut data_size = mem::size_of::<AudioStreamBasicDescription>() as u32;
            let status = AudioObjectGetPropertyData(
                self.audio_device_id,
                NonNull::from(&property_address),
                0,
                null(),
                NonNull::from(&mut data_size),
                NonNull::from(&mut asbd).cast(),
            );
            default_config_error_from_os_status(status)?;

            let sample_format = {
                let audio_format = coreaudio::audio_unit::AudioFormat::from_format_and_flag(
                    asbd.mFormatID,
                    Some(asbd.mFormatFlags),
                );
                let flags = match audio_format {
                    Some(coreaudio::audio_unit::AudioFormat::LinearPCM(flags)) => flags,
                    _ => return Err(DefaultStreamConfigError::StreamTypeNotSupported),
                };
                let maybe_sample_format =
                    coreaudio::audio_unit::SampleFormat::from_flags_and_bits_per_sample(
                        flags,
                        asbd.mBitsPerChannel,
                    );
                match maybe_sample_format {
                    Some(coreaudio::audio_unit::SampleFormat::F32) => SampleFormat::F32,
                    Some(coreaudio::audio_unit::SampleFormat::I16) => SampleFormat::I16,
                    _ => return Err(DefaultStreamConfigError::StreamTypeNotSupported),
                }
            };

            #[allow(non_upper_case_globals)]
            let input = match scope {
                kAudioObjectPropertyScopeInput => Ok(true),
                kAudioObjectPropertyScopeOutput => Ok(false),
                _ => Err(BackendSpecificError {
                    description: format!("unexpected scope (neither input nor output): {scope:?}"),
                }),
            }?;
            let audio_unit = audio_unit_from_device(self, input)?;
            let buffer_size = get_io_buffer_frame_size_range(&audio_unit)?;

            let config = SupportedStreamConfig {
                sample_rate: asbd.mSampleRate as _,
                channels: asbd.mChannelsPerFrame as _,
                buffer_size,
                sample_format,
            };
            Ok(config)
        }
    }

    fn default_input_config(&self) -> Result<SupportedStreamConfig, DefaultStreamConfigError> {
        self.default_config(kAudioObjectPropertyScopeInput)
    }

    fn default_output_config(&self) -> Result<SupportedStreamConfig, DefaultStreamConfigError> {
        self.default_config(kAudioObjectPropertyScopeOutput)
    }

    /// Check if this device supports input (recording).
    fn supports_input(&self) -> bool {
        // Check if the device has input channels by trying to get its input configuration
        self.supported_input_configs()
            .map(|mut configs| configs.next().is_some())
            .unwrap_or(false)
    }
}

impl fmt::Debug for Device {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        f.debug_struct("Device")
            .field("audio_device_id", &self.audio_device_id)
            .field("name", &self.name())
            .finish()
    }
}

impl Device {
    #[allow(clippy::cast_ptr_alignment)]
    #[allow(clippy::while_immutable_condition)]
    #[allow(clippy::float_cmp)]
    fn build_input_stream_raw<D, E>(
        &self,
        config: StreamConfig,
        sample_format: SampleFormat,
        mut data_callback: D,
        error_callback: E,
        _timeout: Option<Duration>,
    ) -> Result<Stream, BuildStreamError>
    where
        D: FnMut(&Data, &InputCallbackInfo) + Send + 'static,
        E: FnMut(StreamError) + Send + 'static,
    {
        // The scope and element for working with a device's input stream.
        let scope = Scope::Output;
        let element = Element::Input;

        // Potentially change the device sample rate to match the config.
        set_sample_rate(self.audio_device_id, config.sample_rate)?;

        let mut loopback_aggregate: Option<LoopbackDevice> = None;
        let mut audio_unit = if self.supports_input() {
            audio_unit_from_device(self, true)?
        } else {
            loopback_aggregate.replace(LoopbackDevice::from_device(self)?);
            audio_unit_from_device(&loopback_aggregate.as_ref().unwrap().aggregate_device, true)?
        };

        // Configure stream format and buffer size for predictable callback behavior.
        configure_stream_format_and_buffer(&mut audio_unit, config, sample_format, scope, element)?;

        let error_callback = Arc::new(Mutex::new(error_callback));
        let error_callback_disconnect = error_callback.clone();

        // Register the callback that is being called by coreaudio whenever it needs data to be
        // fed to the audio buffer.
        let (bytes_per_channel, sample_rate, device_buffer_frames, extra_latency_frames) =
            setup_callback_vars(&audio_unit, config, sample_format, Scope::Input);

        type Args = render_callback::Args<data::Raw>;
        audio_unit.set_input_callback(move |args: Args| unsafe {
            // SAFETY: We configure the stream format as interleaved (via asbd_from_config which
            // does not set kAudioFormatFlagIsNonInterleaved). Interleaved format always has
            // exactly one buffer containing all channels, so mBuffers[0] is always valid.
            let AudioBuffer {
                mNumberChannels: channels,
                mDataByteSize: data_byte_size,
                mData: data,
            } = (*args.data.data).mBuffers[0];

            let data = data as *mut ();
            let len = data_byte_size as usize / bytes_per_channel;
            let data = Data::from_parts(data, len, sample_format);

            let callback = match host_time_to_stream_instant(args.time_stamp.mHostTime) {
                Err(err) => {
                    invoke_error_callback(&error_callback, err.into());
                    return Err(());
                }
                Ok(cb) => cb,
            };
            let buffer_frames = len / channels as usize;
            let latency_frames =
                device_buffer_frames.unwrap_or(buffer_frames) + extra_latency_frames;
            let delay = frames_to_duration(latency_frames, sample_rate);
            let capture = callback
                .sub(delay)
                .expect("`capture` occurs before origin of alsa `StreamInstant`");
            let timestamp = crate::InputStreamTimestamp { callback, capture };

            let info = InputCallbackInfo { timestamp };
            data_callback(&data, &info);
            Ok(())
        })?;

        // Create error callback for stream - either dummy or real based on device type
        let error_callback_for_stream: super::ErrorCallback = if is_default_input_device(self) {
            Box::new(|_: StreamError| {})
        } else {
            let error_callback_clone = error_callback_disconnect.clone();
            Box::new(move |err: StreamError| {
                invoke_error_callback(&error_callback_clone, err);
            })
        };

        let stream = Stream::new(
            StreamInner {
                playing: true,
                audio_unit,
                device_id: self.audio_device_id,
                _loopback_device: loopback_aggregate,
            },
            error_callback_for_stream,
        )?;

        stream
            .inner
            .lock()
            .map_err(|_| BuildStreamError::BackendSpecific {
                err: BackendSpecificError {
                    description: "A cpal stream operation panicked while holding the lock - this is a bug, please report it".to_string(),
                },
            })?
            .audio_unit
            .start()?;

        Ok(stream)
    }

    fn build_output_stream_raw<D, E>(
        &self,
        config: StreamConfig,
        sample_format: SampleFormat,
        mut data_callback: D,
        error_callback: E,
        _timeout: Option<Duration>,
    ) -> Result<Stream, BuildStreamError>
    where
        D: FnMut(&mut Data, &OutputCallbackInfo) + Send + 'static,
        E: FnMut(StreamError) + Send + 'static,
    {
        let mut audio_unit = audio_unit_from_device(self, false)?;

        // The scope and element for working with a device's output stream.
        let scope = Scope::Input;
        let element = Element::Output;

        // Configure device buffer (see comprehensive documentation in input stream above)
        configure_stream_format_and_buffer(&mut audio_unit, config, sample_format, scope, element)?;

        let error_callback = Arc::new(Mutex::new(error_callback));
        let error_callback_disconnect = error_callback.clone();

        // Register the callback that is being called by coreaudio whenever it needs data to be
        // fed to the audio buffer.
        let (bytes_per_channel, sample_rate, device_buffer_frames, extra_latency_frames) =
            setup_callback_vars(&audio_unit, config, sample_format, Scope::Output);

        type Args = render_callback::Args<data::Raw>;
        audio_unit.set_render_callback(move |args: Args| unsafe {
            // SAFETY: We configure the stream format as interleaved (via asbd_from_config which
            // does not set kAudioFormatFlagIsNonInterleaved). Interleaved format always has
            // exactly one buffer containing all channels, so mBuffers[0] is always valid.
            let AudioBuffer {
                mNumberChannels: channels,
                mDataByteSize: data_byte_size,
                mData: data,
            } = (*args.data.data).mBuffers[0];

            let data = data as *mut ();
            let len = data_byte_size as usize / bytes_per_channel;
            let mut data = Data::from_parts(data, len, sample_format);

            let callback = match host_time_to_stream_instant(args.time_stamp.mHostTime) {
                Err(err) => {
                    invoke_error_callback(&error_callback, err.into());
                    return Err(());
                }
                Ok(cb) => cb,
            };
            let buffer_frames = len / channels as usize;
            // Use device buffer size for latency calculation if available
            let latency_frames =
                device_buffer_frames.unwrap_or(buffer_frames) + extra_latency_frames;
            let delay = frames_to_duration(latency_frames, sample_rate);
            let playback = callback
                .add(delay)
                .expect("`playback` occurs beyond representation supported by `StreamInstant`");
            let timestamp = crate::OutputStreamTimestamp { callback, playback };

            let info = OutputCallbackInfo { timestamp };
            data_callback(&mut data, &info);
            Ok(())
        })?;

        // Create error callback for stream - either dummy or real based on device type
        let error_callback_for_stream: super::ErrorCallback = if is_default_output_device(self) {
            Box::new(|_: StreamError| {})
        } else {
            let error_callback_clone = error_callback_disconnect.clone();
            Box::new(move |err: StreamError| {
                invoke_error_callback(&error_callback_clone, err);
            })
        };

        let stream = Stream::new(
            StreamInner {
                playing: true,
                audio_unit,
                device_id: self.audio_device_id,
                _loopback_device: None,
            },
            error_callback_for_stream,
        )?;

        stream
            .inner
            .lock()
            .map_err(|_| BuildStreamError::BackendSpecific {
                err: BackendSpecificError {
                    description: "A cpal stream operation panicked while holding the lock - this is a bug, please report it".to_string(),
                },
            })?
            .audio_unit
            .start()?;

        Ok(stream)
    }
}

/// Configure stream format and buffer size for CoreAudio stream.
///
/// This handles the common setup tasks for both input and output streams:
/// - Sets the stream format (ASBD)
/// - Configures buffer size for Fixed buffer size requests
fn configure_stream_format_and_buffer(
    audio_unit: &mut AudioUnit,
    config: StreamConfig,
    sample_format: SampleFormat,
    scope: Scope,
    element: Element,
) -> Result<(), BuildStreamError> {
    // Set the stream format using stream-specific scope/element
    // - Input streams: scope=Output, element=Input (configuring output format of input element)
    // - Output streams: scope=Input, element=Output (configuring input format of output element)
    let asbd = asbd_from_config(config, sample_format);
    audio_unit.set_property(kAudioUnitProperty_StreamFormat, scope, element, Some(&asbd))?;

    // Configure device buffer size if requested
    if let BufferSize::Fixed(buffer_size) = config.buffer_size {
        // IMPORTANT: Buffer frame size is a DEVICE-LEVEL property, not stream-specific.
        // Unlike stream format above, we ALWAYS use Scope::Global + Element::Output
        // for device properties, regardless of whether this is an input or output stream.
        // This is consistent with other device properties like:
        // - kAudioOutputUnitProperty_CurrentDevice
        // - kAudioDevicePropertyBufferFrameSizeRange
        // The Element::Output here doesn't mean "output stream only" - it's the
        // canonical element used for device-wide properties in Core Audio.
        audio_unit.set_property(
            kAudioDevicePropertyBufferFrameSize,
            Scope::Global,
            Element::Output,
            Some(&buffer_size),
        )?;
    }

    Ok(())
}

/// Returns the sum of the device latency and safety offset in frames.
fn get_device_extra_latency_frames(audio_unit: &AudioUnit, scope: Scope) -> usize {
    let device_latency: u32 = audio_unit
        .get_property(kAudioDevicePropertyLatency, scope, Element::Output)
        .unwrap_or(0);
    let safety_offset: u32 = audio_unit
        .get_property(kAudioDevicePropertySafetyOffset, scope, Element::Output)
        .unwrap_or(0);
    (device_latency + safety_offset) as usize
}

/// Setup common callback variables, querying both the I/O buffer size and extra hardware latency.
///
/// Returns `(bytes_per_channel, sample_rate, device_buffer_frames, extra_latency_frames)`
fn setup_callback_vars(
    audio_unit: &AudioUnit,
    config: StreamConfig,
    sample_format: SampleFormat,
    scope: Scope,
) -> (usize, crate::SampleRate, Option<usize>, usize) {
    let bytes_per_channel = sample_format.sample_size();
    let sample_rate = config.sample_rate;

    let device_buffer_frames = get_device_buffer_frame_size(audio_unit).ok();
    let extra_latency_frames = get_device_extra_latency_frames(audio_unit, scope);

    (
        bytes_per_channel,
        sample_rate,
        device_buffer_frames,
        extra_latency_frames,
    )
}

/// Query the current device buffer frame size from CoreAudio.
///
/// Buffer frame size is a device-level property that always uses Scope::Global + Element::Output,
/// regardless of whether the audio unit is configured for input or output streams.
pub(crate) fn get_device_buffer_frame_size(
    audio_unit: &AudioUnit,
) -> Result<usize, coreaudio::Error> {
    // Device-level property: always use Scope::Global + Element::Output
    // This is consistent with how we set the buffer size and query the buffer size range
    let frames: u32 = audio_unit.get_property(
        kAudioDevicePropertyBufferFrameSize,
        Scope::Global,
        Element::Output,
    )?;
    Ok(frames as usize)
}
```

## File: `src/host/coreaudio/macos/enumerate.rs`
```rust
use super::{Device, OSStatus};
use crate::{BackendSpecificError, DevicesError};
use objc2_core_audio::{
    kAudioHardwareNoError, kAudioHardwarePropertyDefaultInputDevice,
    kAudioHardwarePropertyDefaultOutputDevice, kAudioHardwarePropertyDevices,
    kAudioObjectPropertyElementMaster, kAudioObjectPropertyScopeGlobal, kAudioObjectSystemObject,
    AudioDeviceID, AudioObjectGetPropertyData, AudioObjectGetPropertyDataSize, AudioObjectID,
    AudioObjectPropertyAddress,
};
use std::mem;
use std::ptr::{null, NonNull};
use std::vec::IntoIter as VecIntoIter;

unsafe fn audio_devices() -> Result<Vec<AudioDeviceID>, OSStatus> {
    let property_address = AudioObjectPropertyAddress {
        mSelector: kAudioHardwarePropertyDevices,
        mScope: kAudioObjectPropertyScopeGlobal,
        mElement: kAudioObjectPropertyElementMaster,
    };

    macro_rules! try_status_or_return {
        ($status:expr) => {
            if $status != kAudioHardwareNoError as i32 {
                return Err($status);
            }
        };
    }

    let mut data_size = 0u32;
    let status = AudioObjectGetPropertyDataSize(
        kAudioObjectSystemObject as AudioObjectID,
        NonNull::from(&property_address),
        0,
        null(),
        NonNull::from(&mut data_size),
    );
    try_status_or_return!(status);

    let device_count = data_size / mem::size_of::<AudioDeviceID>() as u32;
    let mut audio_devices = vec![];
    audio_devices.reserve_exact(device_count as usize);

    let status = AudioObjectGetPropertyData(
        kAudioObjectSystemObject as AudioObjectID,
        NonNull::from(&property_address),
        0,
        null(),
        NonNull::from(&mut data_size),
        NonNull::new(audio_devices.as_mut_ptr()).unwrap().cast(),
    );
    try_status_or_return!(status);

    audio_devices.set_len(device_count as usize);

    Ok(audio_devices)
}

pub struct Devices(VecIntoIter<AudioDeviceID>);

impl Devices {
    pub fn new() -> Result<Self, DevicesError> {
        let devices = unsafe {
            match audio_devices() {
                Ok(devices) => devices,
                Err(os_status) => {
                    let description = format!("{os_status}");
                    let err = BackendSpecificError { description };
                    return Err(err.into());
                }
            }
        };
        Ok(Devices(devices.into_iter()))
    }
}

impl Iterator for Devices {
    type Item = Device;

    fn next(&mut self) -> Option<Device> {
        self.0.next().map(|id| Device {
            audio_device_id: id,
        })
    }
}

pub fn default_input_device() -> Option<Device> {
    let property_address = AudioObjectPropertyAddress {
        mSelector: kAudioHardwarePropertyDefaultInputDevice,
        mScope: kAudioObjectPropertyScopeGlobal,
        mElement: kAudioObjectPropertyElementMaster,
    };

    let mut audio_device_id: AudioDeviceID = 0;
    let data_size = mem::size_of::<AudioDeviceID>() as u32;
    let status = unsafe {
        AudioObjectGetPropertyData(
            kAudioObjectSystemObject as AudioObjectID,
            NonNull::from(&property_address),
            0,
            null(),
            NonNull::from(&data_size),
            NonNull::from(&mut audio_device_id).cast(),
        )
    };
    if status != kAudioHardwareNoError {
        return None;
    }

    let device = Device { audio_device_id };
    Some(device)
}

pub fn default_output_device() -> Option<Device> {
    let property_address = AudioObjectPropertyAddress {
        mSelector: kAudioHardwarePropertyDefaultOutputDevice,
        mScope: kAudioObjectPropertyScopeGlobal,
        mElement: kAudioObjectPropertyElementMaster,
    };

    let mut audio_device_id: AudioDeviceID = 0;
    let data_size = mem::size_of::<AudioDeviceID>() as u32;
    let status = unsafe {
        AudioObjectGetPropertyData(
            kAudioObjectSystemObject as AudioObjectID,
            NonNull::from(&property_address),
            0,
            null(),
            NonNull::from(&data_size),
            NonNull::from(&mut audio_device_id).cast(),
        )
    };
    if status != kAudioHardwareNoError {
        return None;
    }

    let device = Device { audio_device_id };
    Some(device)
}

pub use crate::iter::{SupportedInputConfigs, SupportedOutputConfigs};
```

## File: `src/host/coreaudio/macos/loopback.rs`
```rust
//! Manages loopback recording (recording system audio output)

use super::device::Device;
use crate::{host::coreaudio::check_os_status, BackendSpecificError, BuildStreamError};
use objc2::{rc::Retained, AnyThread};
use objc2_core_audio::{
    kAudioAggregateDeviceNameKey, kAudioAggregateDeviceTapAutoStartKey,
    kAudioAggregateDeviceTapListKey, kAudioAggregateDeviceUIDKey, kAudioDevicePropertyDeviceUID,
    kAudioEndPointDeviceIsPrivateKey, kAudioObjectPropertyElementMain,
    kAudioObjectPropertyScopeGlobal, kAudioSubTapDriftCompensationKey, kAudioSubTapUIDKey,
    AudioHardwareCreateAggregateDevice, AudioHardwareCreateProcessTap,
    AudioHardwareDestroyAggregateDevice, AudioHardwareDestroyProcessTap,
    AudioObjectGetPropertyData, AudioObjectID, AudioObjectPropertyAddress, CATapDescription,
    CATapMuteBehavior,
};
use objc2_core_foundation::{
    kCFAllocatorDefault, kCFTypeArrayCallBacks, kCFTypeDictionaryKeyCallBacks,
    kCFTypeDictionaryValueCallBacks, CFArray, CFDictionary, CFMutableDictionary, CFRetained,
    CFString, CFStringCreateWithCString,
};
use objc2_foundation::{ns_string, NSArray, NSNumber, NSString};
use std::{
    ffi::{c_void, CStr},
    mem::MaybeUninit,
    ptr::NonNull,
};
type CFStringRef = *mut std::os::raw::c_void;

impl Device {
    fn uid(&self) -> Result<Retained<NSString>, BackendSpecificError> {
        let mut cfstring: CFStringRef = std::ptr::null_mut();
        let mut size = std::mem::size_of::<CFStringRef>() as u32;

        let property = AudioObjectPropertyAddress {
            mSelector: kAudioDevicePropertyDeviceUID,
            mScope: kAudioObjectPropertyScopeGlobal,
            mElement: kAudioObjectPropertyElementMain,
        };

        let status = unsafe {
            AudioObjectGetPropertyData(
                self.audio_device_id,
                NonNull::from(&property),
                0,
                std::ptr::null(),
                NonNull::from(&mut size),
                NonNull::from(&mut cfstring).cast(),
            )
        };
        check_os_status(status)?;

        if cfstring.is_null() {
            return Err(BackendSpecificError {
                description: "Device uid is null".to_string(),
            });
        }

        let ns_string: Retained<NSString> = unsafe {
            // unwrap cause cfstring!=null as checked before
            Retained::retain(cfstring as *mut NSString).unwrap()
        };

        Ok(ns_string)
    }
}

/// An aggregate device with tap for recording system output.
///
/// Its main difference with [`Device`] is that it's destroyed when dropped.
///
/// It also doesn't implement the [`DeviceTrait`] as users shouldn't be using it. Its
/// main purpose is to destroy the created aggregate device when loopback recording
/// is done.
#[derive(PartialEq, Eq)]
pub struct LoopbackDevice {
    pub tap_id: AudioObjectID,
    pub aggregate_device: Device,
}

impl LoopbackDevice {
    /// Create a [`LoopbackDevice`] that records the sound
    /// output of `device`.
    pub fn from_device(device: &Device) -> Result<Self, BuildStreamError> {
        // 1 - Create tap

        // Empty list of processes as we want to record all processes
        let processes = NSArray::new();
        let device_uid = device.uid()?;
        let tap_desc = unsafe {
            CATapDescription::initWithProcesses_andDeviceUID_withStream(
                CATapDescription::alloc(),
                &processes,
                device_uid.as_ref(),
                0,
            )
        };
        unsafe {
            tap_desc.setMuteBehavior(CATapMuteBehavior::Unmuted); // captured audio still goes to speakers
            tap_desc.setName(ns_string!("cpal output recorder"));
            tap_desc.setPrivate(true); // the Aggregate Device would be private
            tap_desc.setExclusive(true); // the process list means exclude them
        };

        let mut tap_obj_id: MaybeUninit<AudioObjectID> = MaybeUninit::uninit();
        let tap_obj_id = unsafe {
            let status =
                AudioHardwareCreateProcessTap(Some(tap_desc.as_ref()), tap_obj_id.as_mut_ptr());
            check_os_status(status)?;
            tap_obj_id.assume_init()
        };
        let tap_uid = unsafe { tap_desc.UUID().UUIDString() };

        // 2 - Create aggregate device
        let aggregate_device_properties = create_audio_aggregate_device_properties(tap_uid);
        let mut aggregate_device_id: AudioObjectID = 0;
        let status = unsafe {
            AudioHardwareCreateAggregateDevice(
                aggregate_device_properties.as_ref(),
                NonNull::from(&mut aggregate_device_id),
            )
        };
        check_os_status(status)?;

        Ok(Self {
            tap_id: tap_obj_id,
            aggregate_device: Device::new(aggregate_device_id),
        })
    }
}

impl Drop for LoopbackDevice {
    fn drop(&mut self) {
        unsafe {
            // We don't check status to avoid panic during `drop`
            let _status =
                AudioHardwareDestroyAggregateDevice(self.aggregate_device.audio_device_id);
            let _status = AudioHardwareDestroyProcessTap(self.tap_id);
        }
    }
}

fn to_cfstring(cstr: &'static CStr) -> CFRetained<CFString> {
    unsafe {
        CFStringCreateWithCString(
            kCFAllocatorDefault,
            cstr.as_ptr(),
            0x08000100, /* UTF8 */
        )
    }
    .unwrap()
}

/// Rust reimplementation of the following:
/// ```c
/// tap_uid = [[tap_description UUID] UUIDString];
/// taps = @[
///     @{
///         @kAudioSubTapUIDKey : (NSString*)tap_uid,
///         @kAudioSubTapDriftCompensationKey : @YES,
///     },
/// ];
///
/// aggregate_device_properties = @{
///     @kAudioAggregateDeviceNameKey : @"MiniMetersAggregateDevice",
///     @kAudioAggregateDeviceUIDKey :
///         @"com.josephlyncheski.MiniMetersAggregateDevice",
///     @kAudioAggregateDeviceTapListKey : taps,
///     @kAudioAggregateDeviceTapAutoStartKey : @NO,
///     // If we set this to NO then I believe we need to make the Tap public as
///     // well.
///     @kAudioAggregateDeviceIsPrivateKey : @YES,
/// };
/// ```
pub fn create_audio_aggregate_device_properties(
    tap_uid: Retained<NSString>,
) -> CFRetained<CFDictionary> {
    let tap_inner = unsafe {
        let dict = CFMutableDictionary::new(
            kCFAllocatorDefault,
            2,
            &kCFTypeDictionaryKeyCallBacks,
            &kCFTypeDictionaryValueCallBacks,
        )
        .unwrap();

        CFMutableDictionary::set_value(
            Some(dict.as_ref()),
            &*to_cfstring(kAudioSubTapUIDKey) as *const _ as *const c_void,
            &*tap_uid as *const _ as *const c_void,
        );
        CFMutableDictionary::set_value(
            Some(dict.as_ref()),
            &*to_cfstring(kAudioSubTapDriftCompensationKey) as *const _ as *const c_void,
            &*NSNumber::initWithBool(NSNumber::alloc(), true) as *const _ as *const c_void,
        );

        dict
    };
    let _taps_list = [tap_inner];
    let taps = unsafe {
        CFArray::new(
            kCFAllocatorDefault,
            _taps_list.as_ptr() as *mut *const c_void,
            _taps_list.len() as _,
            &kCFTypeArrayCallBacks,
        )
        .unwrap()
    };
    let aggregate_dev_properties = unsafe {
        let dict = CFMutableDictionary::new(
            kCFAllocatorDefault,
            5,
            &kCFTypeDictionaryKeyCallBacks,
            &kCFTypeDictionaryValueCallBacks,
        )
        .unwrap();

        CFMutableDictionary::set_value(
            Some(dict.as_ref()),
            &*to_cfstring(kAudioAggregateDeviceNameKey) as *const _ as *const c_void,
            &*CFString::from_str("Cpal loopback record aggregate device") as *const _
                as *const c_void,
        );
        CFMutableDictionary::set_value(
            Some(dict.as_ref()),
            &*to_cfstring(kAudioAggregateDeviceUIDKey) as *const _ as *const c_void,
            &*CFString::from_str("com.cpal.LoopbackRecordAggregateDevice") as *const _
                as *const c_void,
        );
        CFMutableDictionary::set_value(
            Some(dict.as_ref()),
            &*to_cfstring(kAudioAggregateDeviceTapListKey) as *const _ as *const c_void,
            &*taps as *const _ as *const c_void,
        );
        CFMutableDictionary::set_value(
            Some(dict.as_ref()),
            &*to_cfstring(kAudioAggregateDeviceTapAutoStartKey) as *const _ as *const c_void,
            &*NSNumber::initWithBool(NSNumber::alloc(), false) as *const _ as *const c_void,
        );
        CFMutableDictionary::set_value(
            Some(dict.as_ref()),
            &*to_cfstring(kAudioEndPointDeviceIsPrivateKey) as *const _ as *const c_void,
            &*NSNumber::initWithBool(NSNumber::alloc(), true) as *const _ as *const c_void,
        );

        CFRetained::cast_unchecked::<CFDictionary>(dict)
    };

    aggregate_dev_properties
}
```

## File: `src/host/coreaudio/macos/mod.rs`
```rust
#![allow(deprecated)]
use super::{asbd_from_config, check_os_status, frames_to_duration, host_time_to_stream_instant};

use super::OSStatus;
use crate::host::coreaudio::macos::loopback::LoopbackDevice;
use crate::traits::{HostTrait, StreamTrait};
use crate::{BackendSpecificError, DevicesError, PauseStreamError, PlayStreamError};
use coreaudio::audio_unit::AudioUnit;
use objc2_core_audio::AudioDeviceID;
use std::sync::{mpsc, Arc, Mutex, Weak};

pub use self::enumerate::{default_input_device, default_output_device, Devices};

use objc2_core_audio::{
    kAudioDevicePropertyDeviceIsAlive, kAudioObjectPropertyElementMain,
    kAudioObjectPropertyScopeGlobal, AudioObjectPropertyAddress,
};
use property_listener::AudioObjectPropertyListener;

mod device;
pub mod enumerate;
mod loopback;
mod property_listener;
pub use device::Device;

/// Coreaudio host, the default host on macOS.
#[derive(Debug)]
pub struct Host;

impl Host {
    pub fn new() -> Result<Self, crate::HostUnavailable> {
        Ok(Host)
    }
}

impl HostTrait for Host {
    type Devices = Devices;
    type Device = Device;

    fn is_available() -> bool {
        // Assume coreaudio is always available
        true
    }

    fn devices(&self) -> Result<Self::Devices, DevicesError> {
        Devices::new()
    }

    fn default_input_device(&self) -> Option<Self::Device> {
        default_input_device()
    }

    fn default_output_device(&self) -> Option<Self::Device> {
        default_output_device()
    }
}

/// Type alias for the error callback to reduce complexity
type ErrorCallback = Box<dyn FnMut(crate::StreamError) + Send + 'static>;

/// Invoke error callback, recovering from poisoned mutex if needed.
/// Returns true if callback was invoked, false if skipped due to WouldBlock.
#[inline]
fn invoke_error_callback<E>(error_callback: &Arc<Mutex<E>>, err: crate::StreamError) -> bool
where
    E: FnMut(crate::StreamError) + Send,
{
    match error_callback.try_lock() {
        Ok(mut cb) => {
            cb(err);
            true
        }
        Err(std::sync::TryLockError::Poisoned(guard)) => {
            // Recover from poisoned lock to still report this error
            guard.into_inner()(err);
            true
        }
        Err(std::sync::TryLockError::WouldBlock) => {
            // Skip if callback is busy
            false
        }
    }
}

/// Manages device disconnection listener on a dedicated thread to ensure the
/// AudioObjectPropertyListener is always created and dropped on the same thread.
/// This avoids potential threading issues with CoreAudio APIs.
///
/// When a device disconnects, this manager:
/// 1. Attempts to pause the stream to stop audio I/O
/// 2. Calls the error callback with `StreamError::DeviceNotAvailable`
///
/// The dedicated thread architecture ensures `Stream` can implement `Send`.
struct DisconnectManager {
    _shutdown_tx: mpsc::Sender<()>,
}

impl DisconnectManager {
    /// Create a new DisconnectManager that monitors device disconnection on a dedicated thread
    fn new(
        device_id: AudioDeviceID,
        stream_weak: Weak<Mutex<StreamInner>>,
        error_callback: Arc<Mutex<ErrorCallback>>,
    ) -> Result<Self, crate::BuildStreamError> {
        let (shutdown_tx, shutdown_rx) = mpsc::channel();
        let (disconnect_tx, disconnect_rx) = mpsc::channel();
        let (ready_tx, ready_rx) = mpsc::channel();

        // Spawn dedicated thread to own the AudioObjectPropertyListener
        let disconnect_tx_clone = disconnect_tx.clone();
        std::thread::spawn(move || {
            let property_address = AudioObjectPropertyAddress {
                mSelector: kAudioDevicePropertyDeviceIsAlive,
                mScope: kAudioObjectPropertyScopeGlobal,
                mElement: kAudioObjectPropertyElementMain,
            };

            // Create the listener on this dedicated thread
            let disconnect_fn = move || {
                let _ = disconnect_tx_clone.send(());
            };
            match AudioObjectPropertyListener::new(device_id, property_address, disconnect_fn) {
                Ok(_listener) => {
                    let _ = ready_tx.send(Ok(()));
                    // Drop the listener on this thread after receiving a shutdown signal
                    let _ = shutdown_rx.recv();
                }
                Err(e) => {
                    let _ = ready_tx.send(Err(e));
                }
            }
        });

        // Wait for listener creation to complete or fail
        ready_rx
            .recv()
            .map_err(|_| crate::BuildStreamError::BackendSpecific {
                err: BackendSpecificError {
                    description: "Disconnect listener thread terminated unexpectedly".to_string(),
                },
            })??;

        // Handle disconnect events on the main thread pool
        let stream_weak_clone = stream_weak.clone();
        let error_callback_clone = error_callback.clone();
        std::thread::spawn(move || {
            while disconnect_rx.recv().is_ok() {
                // Check if stream still exists
                if let Some(stream_arc) = stream_weak_clone.upgrade() {
                    // First, try to pause the stream to stop playback
                    if let Ok(mut stream_inner) = stream_arc.try_lock() {
                        let _ = stream_inner.pause();
                    }

                    // Always try to notify about device disconnection
                    invoke_error_callback(
                        &error_callback_clone,
                        crate::StreamError::DeviceNotAvailable,
                    );
                } else {
                    // Stream is gone, exit the handler thread
                    break;
                }
            }
        });

        Ok(DisconnectManager {
            _shutdown_tx: shutdown_tx,
        })
    }
}

struct StreamInner {
    playing: bool,
    audio_unit: AudioUnit,
    // Track the device with which the audio unit was spawned.
    //
    // We must do this so that we can avoid changing the device sample rate if there is already
    // a stream associated with the device.
    #[allow(dead_code)]
    device_id: AudioDeviceID,
    /// Manage the lifetime of the aggregate device used
    /// for loopback recording
    _loopback_device: Option<LoopbackDevice>,
}

impl StreamInner {
    fn play(&mut self) -> Result<(), PlayStreamError> {
        if !self.playing {
            if let Err(e) = self.audio_unit.start() {
                let description = format!("{e}");
                let err = BackendSpecificError { description };
                return Err(err.into());
            }
            self.playing = true;
        }
        Ok(())
    }

    fn pause(&mut self) -> Result<(), PauseStreamError> {
        if self.playing {
            if let Err(e) = self.audio_unit.stop() {
                let description = format!("{e}");
                let err = BackendSpecificError { description };
                return Err(err.into());
            }
            self.playing = false;
        }
        Ok(())
    }
}

pub struct Stream {
    inner: Arc<Mutex<StreamInner>>,
    // Manages the device disconnection listener separately to allow Stream to be Send.
    // The DisconnectManager contains the non-Send AudioObjectPropertyListener.
    _disconnect_manager: DisconnectManager,
}

impl Stream {
    fn new(
        inner: StreamInner,
        error_callback: ErrorCallback,
    ) -> Result<Self, crate::BuildStreamError> {
        let device_id = inner.device_id;
        let inner_arc = Arc::new(Mutex::new(inner));
        let weak_inner = Arc::downgrade(&inner_arc);

        let error_callback = Arc::new(Mutex::new(error_callback));
        let disconnect_manager = DisconnectManager::new(device_id, weak_inner, error_callback)?;

        Ok(Self {
            inner: inner_arc,
            _disconnect_manager: disconnect_manager,
        })
    }
}

impl StreamTrait for Stream {
    fn play(&self) -> Result<(), PlayStreamError> {
        let mut stream = self
            .inner
            .lock()
            .map_err(|_| PlayStreamError::BackendSpecific {
                err: BackendSpecificError {
                    description: "A cpal stream operation panicked while holding the lock - this is a bug, please report it".to_string(),
                },
            })?;

        stream.play()
    }

    fn pause(&self) -> Result<(), PauseStreamError> {
        let mut stream = self
            .inner
            .lock()
            .map_err(|_| PauseStreamError::BackendSpecific {
                err: BackendSpecificError {
                    description: "A cpal stream operation panicked while holding the lock - this is a bug, please report it".to_string(),
                },
            })?;

        stream.pause()
    }

    fn buffer_size(&self) -> Option<crate::FrameCount> {
        let stream = self.inner.lock().ok()?;

        device::get_device_buffer_frame_size(&stream.audio_unit)
            .ok()
            .map(|size| size as crate::FrameCount)
    }
}

#[cfg(test)]
mod test {
    use crate::{
        default_host,
        traits::{DeviceTrait, HostTrait, StreamTrait},
        Sample,
    };

    #[test]
    fn test_play() {
        let host = default_host();
        let device = host.default_output_device().unwrap();

        let mut supported_configs_range = device.supported_output_configs().unwrap();
        let supported_config = supported_configs_range
            .next()
            .unwrap()
            .with_max_sample_rate();
        let config = supported_config.config();

        let stream = device
            .build_output_stream(
                config,
                write_silence::<f32>,
                move |err| println!("Error: {err}"),
                None, // None=blocking, Some(Duration)=timeout
            )
            .unwrap();
        stream.play().unwrap();
        std::thread::sleep(std::time::Duration::from_secs(1));
    }

    #[test]
    fn test_record() {
        let host = default_host();
        let device = host.default_input_device().unwrap();
        println!("Device: {:?}", device.name());

        let mut supported_configs_range = device.supported_input_configs().unwrap();
        println!("Supported configs:");
        for config in supported_configs_range.clone() {
            println!("{:?}", config)
        }
        let supported_config = supported_configs_range
            .next()
            .unwrap()
            .with_max_sample_rate();
        let config = supported_config.config();

        let stream = device
            .build_input_stream(
                config,
                move |data: &[f32], _: &crate::InputCallbackInfo| {
                    // react to stream events and read or write stream data here.
                    println!("Got data: {:?}", &data[..25]);
                },
                move |err| println!("Error: {err}"),
                None, // None=blocking, Some(Duration)=timeout
            )
            .unwrap();
        stream.play().unwrap();
        std::thread::sleep(std::time::Duration::from_secs(1));
    }

    #[test]
    fn test_record_output() {
        if std::env::var("CI").is_ok() {
            println!("Skipping test_record_output in CI environment due to permissions");
            return;
        }

        let host = default_host();
        let device = host.default_output_device().unwrap();

        let mut supported_configs_range = device.supported_output_configs().unwrap();
        let supported_config = supported_configs_range
            .next()
            .unwrap()
            .with_max_sample_rate();
        let config = supported_config.config();

        println!("Building input stream");
        let stream = device
            .build_input_stream(
                config,
                move |data: &[f32], _: &crate::InputCallbackInfo| {
                    // react to stream events and read or write stream data here.
                    println!("Got data: {:?}", &data[..25]);
                },
                move |err| println!("Error: {err}"),
                None, // None=blocking, Some(Duration)=timeout
            )
            .unwrap();
        stream.play().unwrap();
        std::thread::sleep(std::time::Duration::from_secs(1));
    }

    fn write_silence<T: Sample>(data: &mut [T], _: &crate::OutputCallbackInfo) {
        for sample in data.iter_mut() {
            *sample = Sample::EQUILIBRIUM;
        }
    }
}
```

## File: `src/host/coreaudio/macos/property_listener.rs`
```rust
//! Helper code for registering audio object property listeners.
use std::ptr::NonNull;

use objc2_core_audio::{
    AudioObjectAddPropertyListener, AudioObjectID, AudioObjectPropertyAddress,
    AudioObjectRemovePropertyListener,
};

use super::OSStatus;
use crate::BuildStreamError;

/// A double-indirection to be able to pass a closure (a fat pointer)
/// via a single c_void.
struct PropertyListenerCallbackWrapper(Box<dyn FnMut()>);

/// Maintain an audio object property listener.
/// The listener will be removed when this type is dropped.
pub struct AudioObjectPropertyListener {
    callback: Box<PropertyListenerCallbackWrapper>,
    property_address: AudioObjectPropertyAddress,
    audio_object_id: AudioObjectID,
    removed: bool,
}

impl AudioObjectPropertyListener {
    /// Attach the provided callback as a audio object property listener.
    pub fn new<F: FnMut() + 'static>(
        audio_object_id: AudioObjectID,
        property_address: AudioObjectPropertyAddress,
        callback: F,
    ) -> Result<Self, BuildStreamError> {
        let callback = Box::new(PropertyListenerCallbackWrapper(Box::new(callback)));
        unsafe {
            coreaudio::Error::from_os_status(AudioObjectAddPropertyListener(
                audio_object_id,
                NonNull::from(&property_address),
                Some(property_listener_handler_shim),
                &*callback as *const _ as *mut _,
            ))?;
        };
        Ok(Self {
            callback,
            audio_object_id,
            property_address,
            removed: false,
        })
    }

    /// Explicitly remove the property listener.
    /// Use this method if you need to explicitly handle failure to remove
    /// the property listener.
    pub fn remove(mut self) -> Result<(), BuildStreamError> {
        self.remove_inner()
    }

    fn remove_inner(&mut self) -> Result<(), BuildStreamError> {
        unsafe {
            coreaudio::Error::from_os_status(AudioObjectRemovePropertyListener(
                self.audio_object_id,
                NonNull::from(&self.property_address),
                Some(property_listener_handler_shim),
                &*self.callback as *const _ as *mut _,
            ))?;
        }
        self.removed = true;
        Ok(())
    }
}

impl Drop for AudioObjectPropertyListener {
    fn drop(&mut self) {
        if !self.removed {
            let _ = self.remove_inner();
        }
    }
}

/// Callback used to call user-provided closure as a property listener.
unsafe extern "C-unwind" fn property_listener_handler_shim(
    _: AudioObjectID,
    _: u32,
    _: NonNull<AudioObjectPropertyAddress>,
    callback: *mut ::std::os::raw::c_void,
) -> OSStatus {
    let wrapper = callback as *mut PropertyListenerCallbackWrapper;
    (*wrapper).0();
    0
}
```

## File: `src/host/custom/mod.rs`
```rust
//! Custom host backend.
//!
//! Allows user-defined host implementations with the `custom` feature.
//! See `examples/custom.rs` for usage.

use crate::traits::{DeviceTrait, HostTrait, StreamTrait};
use crate::{
    BuildStreamError, Data, DefaultStreamConfigError, DeviceDescription, DeviceId, DeviceIdError,
    DeviceNameError, DevicesError, InputCallbackInfo, OutputCallbackInfo, PauseStreamError,
    PlayStreamError, SampleFormat, StreamConfig, StreamError, SupportedStreamConfig,
    SupportedStreamConfigRange, SupportedStreamConfigsError,
};
use core::time::Duration;

/// A host that can be used to write custom [`HostTrait`] implementations.
///
/// # Usage
///
/// A [`CustomHost`](Host) can be used on its own, but most crates that depend on `cpal` use a [`cpal::Host`](crate::Host) instead.
/// You can turn a `CustomHost` into a `Host` fairly easily:
///
/// ```ignore
/// let custom = cpal::platform::CustomHost::from_host(/* ... */);
/// let host = cpal::Host::from(custom);
/// ```
///
/// Custom hosts are marked as unavailable and will not appear in [`cpal::available_hosts`](crate::available_hosts).
pub struct Host(Box<dyn HostErased>);

impl Host {
    // this only exists for impl_platform_host, which requires it
    pub(crate) fn new() -> Result<Self, crate::HostUnavailable> {
        Err(crate::HostUnavailable)
    }

    /// Construct a custom host from an arbitrary [`HostTrait`] implementation.
    pub fn from_host<T>(host: T) -> Self
    where
        T: HostTrait + Send + Sync + 'static,
        T::Device: Send + Sync + Clone,
        <T::Device as DeviceTrait>::SupportedInputConfigs: Clone,
        <T::Device as DeviceTrait>::SupportedOutputConfigs: Clone,
        <T::Device as DeviceTrait>::Stream: Send + Sync,
    {
        Self(Box::new(host))
    }
}

/// A device that can be used to write custom [`DeviceTrait`] implementations.
///
/// # Usage
///
/// A [`CustomDevice`](Device) can be used on its own, but most crates that depend on `cpal` use a [`cpal::Device`](crate::Device) instead.
/// You can turn a `Device` into a `Device` fairly easily:
///
/// ```ignore
/// let custom = cpal::platform::CustomDevice::from_device(/* ... */);
/// let device = cpal::Device::from(custom);
/// ```
///
/// `rodio`, for example, lets you build an `OutputStream` with a [`cpal::Device`](crate::Device):
/// ```ignore
/// let custom = cpal::platform::CustomDevice::from_device(/* ... */);
/// let device = cpal::Device::from(custom);
///
/// let stream_builder = rodio::OutputStreamBuilder::from_device(device).expect("failed to build stream");
/// ```
pub struct Device(Box<dyn DeviceErased>);

impl Device {
    /// Construct a custom device from an arbitrary [`DeviceTrait`] implementation.
    pub fn from_device<T>(device: T) -> Self
    where
        T: DeviceTrait + Send + Sync + Clone + 'static,
        T::SupportedInputConfigs: Clone,
        T::SupportedOutputConfigs: Clone,
        T::Stream: Send + Sync,
    {
        Self(Box::new(device))
    }
}

impl Clone for Device {
    fn clone(&self) -> Self {
        self.0.clone()
    }
}

/// A stream that can be used with custom [`StreamTrait`] implementations.
pub struct Stream(Box<dyn StreamErased>);

impl Stream {
    /// Construct a custom stream from an arbitrary [`StreamTrait`] implementation.
    pub fn from_stream<T>(stream: T) -> Self
    where
        T: StreamTrait + Send + Sync + 'static,
    {
        Self(Box::new(stream))
    }
}

// dyn-compatible versions of DeviceTrait, HostTrait, and StreamTrait
// these only accept/return things via trait objects

type Devices = Box<dyn Iterator<Item = Device>>;
trait HostErased: Send + Sync {
    fn devices(&self) -> Result<Devices, DevicesError>;
    fn default_input_device(&self) -> Option<Device>;
    fn default_output_device(&self) -> Option<Device>;
}

pub struct SupportedConfigs(Box<dyn SupportedConfigsErased>);

// A trait for supported configs. This only adds a dyn compatible clone function
// This is required because `SupportedInputConfigsInner` & `SupportedOutputConfigsInner` are `Clone`
trait SupportedConfigsErased: Iterator<Item = SupportedStreamConfigRange> {
    fn clone(&self) -> SupportedConfigs;
}

impl<T> SupportedConfigsErased for T
where
    T: Iterator<Item = SupportedStreamConfigRange> + Clone + 'static,
{
    fn clone(&self) -> SupportedConfigs {
        SupportedConfigs(Box::new(Clone::clone(self)))
    }
}

impl Iterator for SupportedConfigs {
    type Item = SupportedStreamConfigRange;

    fn next(&mut self) -> Option<Self::Item> {
        self.0.next()
    }
}

impl Clone for SupportedConfigs {
    fn clone(&self) -> Self {
        self.0.clone()
    }
}

type ErrorCallback = Box<dyn FnMut(StreamError) + Send + 'static>;
type InputCallback = Box<dyn FnMut(&Data, &InputCallbackInfo) + Send + 'static>;
type OutputCallback = Box<dyn FnMut(&mut Data, &OutputCallbackInfo) + Send + 'static>;

trait DeviceErased: Send + Sync {
    fn name(&self) -> Result<String, DeviceNameError>;
    fn description(&self) -> Result<DeviceDescription, DeviceNameError>;
    fn id(&self) -> Result<DeviceId, DeviceIdError>;
    fn supports_input(&self) -> bool;
    fn supports_output(&self) -> bool;
    fn supported_input_configs(&self) -> Result<SupportedConfigs, SupportedStreamConfigsError>;
    fn supported_output_configs(&self) -> Result<SupportedConfigs, SupportedStreamConfigsError>;
    fn default_input_config(&self) -> Result<SupportedStreamConfig, DefaultStreamConfigError>;
    fn default_output_config(&self) -> Result<SupportedStreamConfig, DefaultStreamConfigError>;
    fn build_input_stream_raw(
        &self,
        config: StreamConfig,
        sample_format: SampleFormat,
        data_callback: InputCallback,
        error_callback: ErrorCallback,
        timeout: Option<Duration>,
    ) -> Result<Stream, BuildStreamError>;
    fn build_output_stream_raw(
        &self,
        config: StreamConfig,
        sample_format: SampleFormat,
        data_callback: OutputCallback,
        error_callback: ErrorCallback,
        timeout: Option<Duration>,
    ) -> Result<Stream, BuildStreamError>;
    // Required because `DeviceInner` is clone
    fn clone(&self) -> Device;
}

trait StreamErased: Send + Sync {
    fn play(&self) -> Result<(), PlayStreamError>;
    fn pause(&self) -> Result<(), PauseStreamError>;
}

fn device_to_erased(d: impl DeviceErased + 'static) -> Device {
    Device(Box::new(d))
}

impl<T> HostErased for T
where
    T: HostTrait + Send + Sync,
    T::Devices: 'static,
    T::Device: DeviceErased + 'static,
{
    fn devices(&self) -> Result<Devices, DevicesError> {
        let iter = <T as HostTrait>::devices(self)?;
        let erased = Box::new(iter.map(device_to_erased));
        Ok(erased)
    }

    fn default_input_device(&self) -> Option<Device> {
        <T as HostTrait>::default_input_device(self).map(device_to_erased)
    }

    fn default_output_device(&self) -> Option<Device> {
        <T as HostTrait>::default_output_device(self).map(device_to_erased)
    }
}

fn supported_configs_to_erased(
    i: impl Iterator<Item = SupportedStreamConfigRange> + Clone + 'static,
) -> SupportedConfigs {
    SupportedConfigs(Box::new(i))
}

fn stream_to_erased(s: impl StreamTrait + Send + Sync + 'static) -> Stream {
    Stream(Box::new(s))
}

impl<T> DeviceErased for T
where
    T: DeviceTrait + Send + Sync + Clone + 'static,
    T::SupportedInputConfigs: Clone + 'static,
    T::SupportedOutputConfigs: Clone + 'static,
    T::Stream: Send + Sync + 'static,
{
    #[allow(deprecated)]
    fn name(&self) -> Result<String, DeviceNameError> {
        <T as DeviceTrait>::name(self)
    }

    fn description(&self) -> Result<DeviceDescription, DeviceNameError> {
        <T as DeviceTrait>::description(self)
    }

    fn id(&self) -> Result<DeviceId, DeviceIdError> {
        <T as DeviceTrait>::id(self)
    }

    fn supports_input(&self) -> bool {
        <T as DeviceTrait>::supports_input(self)
    }

    fn supports_output(&self) -> bool {
        <T as DeviceTrait>::supports_output(self)
    }

    fn supported_input_configs(&self) -> Result<SupportedConfigs, SupportedStreamConfigsError> {
        <T as DeviceTrait>::supported_input_configs(self).map(supported_configs_to_erased)
    }

    fn supported_output_configs(&self) -> Result<SupportedConfigs, SupportedStreamConfigsError> {
        <T as DeviceTrait>::supported_output_configs(self).map(supported_configs_to_erased)
    }

    fn default_input_config(&self) -> Result<SupportedStreamConfig, DefaultStreamConfigError> {
        <T as DeviceTrait>::default_input_config(self)
    }

    fn default_output_config(&self) -> Result<SupportedStreamConfig, DefaultStreamConfigError> {
        <T as DeviceTrait>::default_output_config(self)
    }

    fn build_input_stream_raw(
        &self,
        config: StreamConfig,
        sample_format: SampleFormat,
        data_callback: InputCallback,
        error_callback: ErrorCallback,
        timeout: Option<Duration>,
    ) -> Result<Stream, BuildStreamError> {
        <T as DeviceTrait>::build_input_stream_raw(
            self,
            config,
            sample_format,
            data_callback,
            error_callback,
            timeout,
        )
        .map(stream_to_erased)
    }

    fn build_output_stream_raw(
        &self,
        config: StreamConfig,
        sample_format: SampleFormat,
        data_callback: OutputCallback,
        error_callback: ErrorCallback,
        timeout: Option<Duration>,
    ) -> Result<Stream, BuildStreamError> {
        <T as DeviceTrait>::build_output_stream_raw(
            self,
            config,
            sample_format,
            data_callback,
            error_callback,
            timeout,
        )
        .map(stream_to_erased)
    }

    fn clone(&self) -> Device {
        device_to_erased(Clone::clone(self))
    }
}

impl<T> StreamErased for T
where
    T: StreamTrait + Send + Sync,
{
    fn play(&self) -> Result<(), PlayStreamError> {
        <T as StreamTrait>::play(self)
    }

    fn pause(&self) -> Result<(), PauseStreamError> {
        <T as StreamTrait>::pause(self)
    }
}

// implementations of HostTrait, DeviceTrait, and StreamTrait for custom versions

impl HostTrait for Host {
    type Devices = Devices;
    type Device = Device;

    fn is_available() -> bool {
        false
    }

    fn devices(&self) -> Result<Self::Devices, DevicesError> {
        self.0.devices()
    }

    fn default_input_device(&self) -> Option<Self::Device> {
        self.0.default_input_device()
    }

    fn default_output_device(&self) -> Option<Self::Device> {
        self.0.default_output_device()
    }
}

impl DeviceTrait for Device {
    type SupportedInputConfigs = SupportedConfigs;

    type SupportedOutputConfigs = SupportedConfigs;

    type Stream = Stream;

    fn name(&self) -> Result<String, DeviceNameError> {
        self.0.name()
    }

    fn description(&self) -> Result<DeviceDescription, DeviceNameError> {
        self.0.description()
    }

    fn id(&self) -> Result<DeviceId, DeviceIdError> {
        self.0.id()
    }

    fn supports_input(&self) -> bool {
        self.0.supports_input()
    }

    fn supports_output(&self) -> bool {
        self.0.supports_output()
    }

    fn supported_input_configs(
        &self,
    ) -> Result<Self::SupportedInputConfigs, SupportedStreamConfigsError> {
        self.0.supported_input_configs()
    }

    fn supported_output_configs(
        &self,
    ) -> Result<Self::SupportedOutputConfigs, SupportedStreamConfigsError> {
        self.0.supported_output_configs()
    }

    fn default_input_config(&self) -> Result<SupportedStreamConfig, DefaultStreamConfigError> {
        self.0.default_input_config()
    }

    fn default_output_config(&self) -> Result<SupportedStreamConfig, DefaultStreamConfigError> {
        self.0.default_output_config()
    }

    fn build_input_stream_raw<D, E>(
        &self,
        config: StreamConfig,
        sample_format: SampleFormat,
        data_callback: D,
        error_callback: E,
        timeout: Option<Duration>,
    ) -> Result<Self::Stream, BuildStreamError>
    where
        D: FnMut(&Data, &InputCallbackInfo) + Send + 'static,
        E: FnMut(StreamError) + Send + 'static,
    {
        self.0.build_input_stream_raw(
            config,
            sample_format,
            Box::new(data_callback),
            Box::new(error_callback),
            timeout,
        )
    }

    fn build_output_stream_raw<D, E>(
        &self,
        config: StreamConfig,
        sample_format: SampleFormat,
        data_callback: D,
        error_callback: E,
        timeout: Option<Duration>,
    ) -> Result<Self::Stream, BuildStreamError>
    where
        D: FnMut(&mut Data, &OutputCallbackInfo) + Send + 'static,
        E: FnMut(StreamError) + Send + 'static,
    {
        self.0.build_output_stream_raw(
            config,
            sample_format,
            Box::new(data_callback),
            Box::new(error_callback),
            timeout,
        )
    }
}

impl StreamTrait for Stream {
    fn play(&self) -> Result<(), PlayStreamError> {
        self.0.play()
    }

    fn pause(&self) -> Result<(), PauseStreamError> {
        self.0.pause()
    }
}
```

## File: `src/host/emscripten/mod.rs`
```rust
//! Emscripten backend implementation.
//!
//! Default backend on Emscripten.

use js_sys::Float32Array;
use std::panic::AssertUnwindSafe;
use std::time::Duration;
use wasm_bindgen::prelude::*;
use wasm_bindgen::JsCast;
use wasm_bindgen_futures::{spawn_local, JsFuture};
use web_sys::AudioContext;

use crate::traits::{DeviceTrait, HostTrait, StreamTrait};
use crate::{
    BufferSize, BuildStreamError, Data, DefaultStreamConfigError, DeviceDescription,
    DeviceDescriptionBuilder, DeviceId, DeviceIdError, DeviceNameError, DevicesError,
    InputCallbackInfo, OutputCallbackInfo, PauseStreamError, PlayStreamError, SampleFormat,
    SampleRate, StreamConfig, StreamError, SupportedBufferSize, SupportedStreamConfig,
    SupportedStreamConfigRange, SupportedStreamConfigsError,
};

// The emscripten backend currently works by instantiating an `AudioContext` object per `Stream`.
// Creating a stream creates a new `AudioContext`. Destroying a stream destroys it. Creation of a
// `Host` instance initializes the `stdweb` context.

/// The default emscripten host type.
#[derive(Debug)]
pub struct Host;

/// Content is false if the iterator is empty.
pub struct Devices(bool);

#[derive(Clone, Debug, PartialEq, Eq)]
pub struct Device;

#[wasm_bindgen]
#[derive(Clone)]
pub struct Stream {
    // A reference to an `AudioContext` object.
    audio_ctxt: AudioContext,
}

// WASM runs in a single-threaded environment, so Send and Sync are safe by design.
unsafe impl Send for Stream {}
unsafe impl Sync for Stream {}

// Compile-time assertion that Stream is Send and Sync
crate::assert_stream_send!(Stream);
crate::assert_stream_sync!(Stream);

pub use crate::iter::{SupportedInputConfigs, SupportedOutputConfigs};

const MIN_CHANNELS: u16 = 1;
const MAX_CHANNELS: u16 = 32;
const MIN_SAMPLE_RATE: SampleRate = 8_000;
const MAX_SAMPLE_RATE: SampleRate = 96_000;
const DEFAULT_SAMPLE_RATE: SampleRate = 44_100;
const MIN_BUFFER_SIZE: u32 = 1;
const MAX_BUFFER_SIZE: u32 = u32::MAX;
const DEFAULT_BUFFER_SIZE: usize = 2048;
const SUPPORTED_SAMPLE_FORMAT: SampleFormat = SampleFormat::F32;

impl Host {
    pub fn new() -> Result<Self, crate::HostUnavailable> {
        Ok(Host)
    }
}

impl Devices {
    fn new() -> Result<Self, DevicesError> {
        Ok(Self::default())
    }
}

impl Device {
    fn description(&self) -> Result<DeviceDescription, DeviceNameError> {
        Ok(DeviceDescriptionBuilder::new("Default Device".to_string())
            .direction(crate::DeviceDirection::Output)
            .build())
    }

    fn id(&self) -> Result<DeviceId, DeviceIdError> {
        Ok(DeviceId(
            crate::platform::HostId::Emscripten,
            "default".to_string(),
        ))
    }

    fn supported_input_configs(
        &self,
    ) -> Result<SupportedInputConfigs, SupportedStreamConfigsError> {
        unimplemented!();
    }

    fn supported_output_configs(
        &self,
    ) -> Result<SupportedOutputConfigs, SupportedStreamConfigsError> {
        let buffer_size = SupportedBufferSize::Range {
            min: MIN_BUFFER_SIZE,
            max: MAX_BUFFER_SIZE,
        };
        let configs: Vec<_> = (MIN_CHANNELS..=MAX_CHANNELS)
            .map(|channels| SupportedStreamConfigRange {
                channels,
                min_sample_rate: MIN_SAMPLE_RATE,
                max_sample_rate: MAX_SAMPLE_RATE,
                buffer_size,
                sample_format: SUPPORTED_SAMPLE_FORMAT,
            })
            .collect();
        Ok(configs.into_iter())
    }

    fn default_input_config(&self) -> Result<SupportedStreamConfig, DefaultStreamConfigError> {
        unimplemented!();
    }

    fn default_output_config(&self) -> Result<SupportedStreamConfig, DefaultStreamConfigError> {
        const EXPECT: &str = "expected at least one valid webaudio stream config";
        let config = self
            .supported_output_configs()
            .expect(EXPECT)
            .max_by(|a, b| a.cmp_default_heuristics(b))
            .unwrap()
            .with_sample_rate(DEFAULT_SAMPLE_RATE);

        Ok(config)
    }
}

impl HostTrait for Host {
    type Devices = Devices;
    type Device = Device;

    fn is_available() -> bool {
        // Assume this host is always available on emscripten.
        true
    }

    fn devices(&self) -> Result<Self::Devices, DevicesError> {
        Devices::new()
    }

    fn default_input_device(&self) -> Option<Self::Device> {
        default_input_device()
    }

    fn default_output_device(&self) -> Option<Self::Device> {
        default_output_device()
    }
}

impl DeviceTrait for Device {
    type SupportedInputConfigs = SupportedInputConfigs;
    type SupportedOutputConfigs = SupportedOutputConfigs;
    type Stream = Stream;

    fn description(&self) -> Result<DeviceDescription, DeviceNameError> {
        Device::description(self)
    }

    fn id(&self) -> Result<DeviceId, DeviceIdError> {
        Device::id(self)
    }

    fn supported_input_configs(
        &self,
    ) -> Result<Self::SupportedInputConfigs, SupportedStreamConfigsError> {
        Device::supported_input_configs(self)
    }

    fn supported_output_configs(
        &self,
    ) -> Result<Self::SupportedOutputConfigs, SupportedStreamConfigsError> {
        Device::supported_output_configs(self)
    }

    fn default_input_config(&self) -> Result<SupportedStreamConfig, DefaultStreamConfigError> {
        Device::default_input_config(self)
    }

    fn default_output_config(&self) -> Result<SupportedStreamConfig, DefaultStreamConfigError> {
        Device::default_output_config(self)
    }

    fn build_input_stream_raw<D, E>(
        &self,
        _config: StreamConfig,
        _sample_format: SampleFormat,
        _data_callback: D,
        _error_callback: E,
        _timeout: Option<Duration>,
    ) -> Result<Self::Stream, BuildStreamError>
    where
        D: FnMut(&Data, &InputCallbackInfo) + Send + 'static,
        E: FnMut(StreamError) + Send + 'static,
    {
        unimplemented!()
    }

    fn build_output_stream_raw<D, E>(
        &self,
        config: StreamConfig,
        sample_format: SampleFormat,
        data_callback: D,
        _error_callback: E,
        _timeout: Option<Duration>,
    ) -> Result<Self::Stream, BuildStreamError>
    where
        D: FnMut(&mut Data, &OutputCallbackInfo) + Send + 'static,
        E: FnMut(StreamError) + Send + 'static,
    {
        if !valid_config(config, sample_format) {
            return Err(BuildStreamError::StreamConfigNotSupported);
        }

        let buffer_size_frames = match config.buffer_size {
            BufferSize::Fixed(v) => {
                if !(MIN_BUFFER_SIZE..=MAX_BUFFER_SIZE).contains(&v) {
                    return Err(BuildStreamError::StreamConfigNotSupported);
                }
                v as usize
            }
            BufferSize::Default => DEFAULT_BUFFER_SIZE,
        };

        // Create the stream.
        let audio_ctxt = AudioContext::new().expect("webaudio is not present on this system");
        let stream = Stream { audio_ctxt };

        // Use `set_timeout` to invoke a Rust callback repeatedly.
        //
        // The job of this callback is to fill the content of the audio buffers.
        //
        // See also: The call to `set_timeout` at the end of the `audio_callback_fn` which creates
        // the loop.
        let data_callback = AssertUnwindSafe(data_callback);
        set_timeout(
            10,
            stream.clone(),
            data_callback,
            config,
            sample_format,
            buffer_size_frames as u32,
        );

        Ok(stream)
    }
}

impl StreamTrait for Stream {
    fn play(&self) -> Result<(), PlayStreamError> {
        let future = JsFuture::from(
            self.audio_ctxt
                .resume()
                .expect("Could not resume the stream"),
        );
        spawn_local(async {
            match future.await {
                Ok(value) => assert!(value.is_undefined()),
                Err(value) => panic!("AudioContext.resume() promise was rejected: {:?}", value),
            }
        });
        Ok(())
    }

    fn pause(&self) -> Result<(), PauseStreamError> {
        let future = JsFuture::from(
            self.audio_ctxt
                .suspend()
                .expect("Could not suspend the stream"),
        );
        spawn_local(async {
            match future.await {
                Ok(value) => assert!(value.is_undefined()),
                Err(value) => panic!("AudioContext.suspend() promise was rejected: {:?}", value),
            }
        });
        Ok(())
    }
}

fn audio_callback_fn<D>(
    mut data_callback: AssertUnwindSafe<D>,
) -> impl FnOnce(Stream, StreamConfig, SampleFormat, u32)
where
    D: FnMut(&mut Data, &OutputCallbackInfo) + Send + 'static,
{
    |stream, config, sample_format, buffer_size_frames| {
        let sample_rate = config.sample_rate;
        let buffer_size_samples = buffer_size_frames * config.channels as u32;
        let audio_ctxt = &stream.audio_ctxt;

        // TODO: We should be re-using a buffer.
        let mut temporary_buffer = vec![0f32; buffer_size_samples as usize];

        {
            let len = temporary_buffer.len();
            let data = temporary_buffer.as_mut_ptr() as *mut ();
            let mut data = unsafe { Data::from_parts(data, len, sample_format) };
            let now_secs: f64 = audio_ctxt.current_time();
            let callback = crate::StreamInstant::from_secs_f64(now_secs);
            // TODO: Use proper latency instead. Currently, unsupported on most browsers though, so
            // we estimate based on buffer size instead. Probably should use this, but it's only
            // supported by firefox (2020-04-28).
            // let latency_secs: f64 = audio_ctxt.outputLatency.try_into().unwrap();
            let buffer_duration = frames_to_duration(len, sample_rate as usize);
            let playback = callback
                .add(buffer_duration)
                .expect("`playback` occurs beyond representation supported by `StreamInstant`");
            let timestamp = crate::OutputStreamTimestamp { callback, playback };
            let info = OutputCallbackInfo { timestamp };
            data_callback(&mut data, &info);
        }

        let typed_array: Float32Array = temporary_buffer.as_slice().into();

        debug_assert_eq!(temporary_buffer.len() % config.channels as usize, 0);

        let src_buffer = Float32Array::new(typed_array.buffer().as_ref());
        let context = audio_ctxt;
        let buffer = context
            .create_buffer(
                config.channels as u32,
                buffer_size_frames,
                sample_rate as f32,
            )
            .expect("Buffer could not be created");
        for channel in 0..config.channels {
            let mut buffer_content = buffer
                .get_channel_data(channel as u32)
                .expect("Should be impossible");
            for (i, buffer_content_item) in buffer_content.iter_mut().enumerate() {
                *buffer_content_item =
                    src_buffer.get_index(i as u32 * config.channels as u32 + channel as u32);
            }
        }

        let node = context
            .create_buffer_source()
            .expect("The buffer source node could not be created");
        node.set_buffer(Some(&buffer));
        context
            .destination()
            .connect_with_audio_node(&node)
            .expect("Could not connect the audio node to the destination");
        node.start().expect("Could not start the audio node");

        // TODO: handle latency better ; right now we just use setInterval with the amount of sound
        // data that is in each buffer ; this is obviously bad, and also the schedule is too tight
        // and there may be underflows
        set_timeout(
            1000 * buffer_size_frames as i32 / sample_rate as i32,
            stream.clone().clone(),
            data_callback,
            config,
            sample_format,
            buffer_size_frames,
        );
    }
}

fn set_timeout<D>(
    time: i32,
    stream: Stream,
    data_callback: AssertUnwindSafe<D>,
    config: StreamConfig,
    sample_format: SampleFormat,
    buffer_size_frames: u32,
) where
    D: FnMut(&mut Data, &OutputCallbackInfo) + Send + 'static,
{
    let window = web_sys::window().expect("Not in a window somehow?");
    window
        .set_timeout_with_callback_and_timeout_and_arguments_4(
            Closure::once_into_js(audio_callback_fn(data_callback))
                .dyn_ref::<js_sys::Function>()
                .expect("The function was somehow not a function"),
            time,
            &stream.into(),
            &config.into(),
            &Closure::once_into_js(move || sample_format),
            &buffer_size_frames.into(),
        )
        .expect("The timeout could not be set");
}

impl Default for Devices {
    fn default() -> Devices {
        // We produce an empty iterator if the WebAudio API isn't available.
        Devices(is_webaudio_available())
    }
}
impl Iterator for Devices {
    type Item = Device;

    fn next(&mut self) -> Option<Device> {
        if self.0 {
            self.0 = false;
            Some(Device)
        } else {
            None
        }
    }
}

fn default_input_device() -> Option<Device> {
    unimplemented!();
}

fn default_output_device() -> Option<Device> {
    if is_webaudio_available() {
        Some(Device)
    } else {
        None
    }
}

// Detects whether the `AudioContext` global variable is available.
fn is_webaudio_available() -> bool {
    AudioContext::new().is_ok()
}

// Whether or not the given stream configuration is valid for building a stream.
fn valid_config(conf: StreamConfig, sample_format: SampleFormat) -> bool {
    conf.channels <= MAX_CHANNELS
        && conf.channels >= MIN_CHANNELS
        && conf.sample_rate <= MAX_SAMPLE_RATE
        && conf.sample_rate >= MIN_SAMPLE_RATE
        && sample_format == SUPPORTED_SAMPLE_FORMAT
}

// Convert the given duration in frames at the given sample rate to a `std::time::Duration`.
fn frames_to_duration(frames: usize, rate: usize) -> std::time::Duration {
    let secsf = frames as f64 / rate as f64;
    let secs = secsf as u64;
    let nanos = ((secsf - secs as f64) * 1_000_000_000.0) as u32;
    std::time::Duration::new(secs, nanos)
}
```

## File: `src/host/jack/device.rs`
```rust
use crate::traits::DeviceTrait;
use crate::{
    BackendSpecificError, BuildStreamError, Data, DefaultStreamConfigError, DeviceDescription,
    DeviceDescriptionBuilder, DeviceDirection, DeviceId, DeviceIdError, DeviceNameError,
    InputCallbackInfo, OutputCallbackInfo, SampleFormat, SampleRate, StreamConfig, StreamError,
    SupportedBufferSize, SupportedStreamConfig, SupportedStreamConfigRange,
    SupportedStreamConfigsError,
};
use std::hash::{Hash, Hasher};
use std::time::Duration;

use super::stream::Stream;
use super::JACK_SAMPLE_FORMAT;

pub use crate::iter::{SupportedInputConfigs, SupportedOutputConfigs};

const DEFAULT_NUM_CHANNELS: u16 = 2;
const DEFAULT_SUPPORTED_CHANNELS: [u16; 10] = [1, 2, 4, 6, 8, 16, 24, 32, 48, 64];

#[derive(Clone, Debug)]
pub struct Device {
    name: String,
    sample_rate: SampleRate,
    buffer_size: SupportedBufferSize,
    direction: DeviceDirection,
    start_server_automatically: bool,
    connect_ports_automatically: bool,
}

impl Device {
    fn new_device(
        name: String,
        connect_ports_automatically: bool,
        start_server_automatically: bool,
        direction: DeviceDirection,
    ) -> Result<Self, String> {
        // ClientOptions are bit flags that you can set with the constants provided
        let client_options = super::get_client_options(start_server_automatically);

        // Create a dummy client to find out the sample rate of the server to be able to provide it as a possible config.
        // This client will be dropped, and a new one will be created when making the stream.
        // This is a hack due to the fact that the Client must be moved to create the AsyncClient.
        match super::get_client(&name, client_options) {
            Ok(client) => Ok(Device {
                // The name given to the client by JACK, could potentially be different from the name supplied e.g.if there is a name collision
                name: client.name().to_string(),
                sample_rate: client.sample_rate(),
                buffer_size: SupportedBufferSize::Range {
                    min: client.buffer_size(),
                    max: client.buffer_size(),
                },
                direction,
                start_server_automatically,
                connect_ports_automatically,
            }),
            Err(e) => Err(e),
        }
    }

    fn id(&self) -> Result<DeviceId, DeviceIdError> {
        Ok(DeviceId(crate::platform::HostId::Jack, self.name.clone()))
    }

    pub fn default_output_device(
        name: &str,
        connect_ports_automatically: bool,
        start_server_automatically: bool,
    ) -> Result<Self, String> {
        let output_client_name = format!("{}_out", name);
        Device::new_device(
            output_client_name,
            connect_ports_automatically,
            start_server_automatically,
            DeviceDirection::Output,
        )
    }

    pub fn default_input_device(
        name: &str,
        connect_ports_automatically: bool,
        start_server_automatically: bool,
    ) -> Result<Self, String> {
        let input_client_name = format!("{}_in", name);
        Device::new_device(
            input_client_name,
            connect_ports_automatically,
            start_server_automatically,
            DeviceDirection::Input,
        )
    }

    pub fn default_config(&self) -> Result<SupportedStreamConfig, DefaultStreamConfigError> {
        let channels = DEFAULT_NUM_CHANNELS;
        let sample_rate = self.sample_rate;
        let buffer_size = self.buffer_size;
        // The sample format for JACK audio ports is always "32-bit float mono audio" in the current implementation.
        // Custom formats are allowed within JACK, but this is of niche interest.
        // The format can be found programmatically by calling jack::PortSpec::port_type() on a created port.
        let sample_format = JACK_SAMPLE_FORMAT;
        Ok(SupportedStreamConfig {
            channels,
            sample_rate,
            buffer_size,
            sample_format,
        })
    }

    pub fn supported_configs(&self) -> Vec<SupportedStreamConfigRange> {
        let f = match self.default_config() {
            Err(_) => return vec![],
            Ok(f) => f,
        };

        let mut supported_configs = vec![];

        for &channels in DEFAULT_SUPPORTED_CHANNELS.iter() {
            supported_configs.push(SupportedStreamConfigRange {
                channels,
                min_sample_rate: f.sample_rate,
                max_sample_rate: f.sample_rate,
                buffer_size: f.buffer_size,
                sample_format: f.sample_format,
            });
        }
        supported_configs
    }

    pub fn is_input(&self) -> bool {
        matches!(self.direction, DeviceDirection::Input)
    }

    pub fn is_output(&self) -> bool {
        matches!(self.direction, DeviceDirection::Output)
    }

    /// Validate buffer size if Fixed is specified. This is necessary because JACK buffer size
    /// is controlled by the JACK server and cannot be changed by clients. Without validation,
    /// cpal would silently use the server's buffer size even if a different value was requested.
    fn validate_buffer_size(&self, conf: StreamConfig) -> Result<(), BuildStreamError> {
        if let crate::BufferSize::Fixed(requested_size) = conf.buffer_size {
            if let SupportedBufferSize::Range { min, max } = self.buffer_size {
                if !(min..=max).contains(&requested_size) {
                    return Err(BuildStreamError::StreamConfigNotSupported);
                }
            }
        }
        Ok(())
    }
}

impl DeviceTrait for Device {
    type SupportedInputConfigs = SupportedInputConfigs;
    type SupportedOutputConfigs = SupportedOutputConfigs;
    type Stream = Stream;

    fn description(&self) -> Result<DeviceDescription, DeviceNameError> {
        Ok(DeviceDescriptionBuilder::new(self.name.clone())
            .direction(self.direction)
            .build())
    }

    fn id(&self) -> Result<DeviceId, DeviceIdError> {
        Device::id(self)
    }

    fn supported_input_configs(
        &self,
    ) -> Result<Self::SupportedInputConfigs, SupportedStreamConfigsError> {
        Ok(self.supported_configs().into_iter())
    }

    fn supported_output_configs(
        &self,
    ) -> Result<Self::SupportedOutputConfigs, SupportedStreamConfigsError> {
        Ok(self.supported_configs().into_iter())
    }

    /// Returns the default input config
    /// The sample format for JACK audio ports is always "32-bit float mono audio" unless using a custom type.
    /// The sample rate is set by the JACK server.
    fn default_input_config(&self) -> Result<SupportedStreamConfig, DefaultStreamConfigError> {
        self.default_config()
    }

    /// Returns the default output config
    /// The sample format for JACK audio ports is always "32-bit float mono audio" unless using a custom type.
    /// The sample rate is set by the JACK server.
    fn default_output_config(&self) -> Result<SupportedStreamConfig, DefaultStreamConfigError> {
        self.default_config()
    }

    fn build_input_stream_raw<D, E>(
        &self,
        conf: StreamConfig,
        sample_format: SampleFormat,
        data_callback: D,
        error_callback: E,
        _timeout: Option<Duration>,
    ) -> Result<Self::Stream, BuildStreamError>
    where
        D: FnMut(&Data, &InputCallbackInfo) + Send + 'static,
        E: FnMut(StreamError) + Send + 'static,
    {
        if self.is_output() {
            // Trying to create an input stream from an output device
            return Err(BuildStreamError::StreamConfigNotSupported);
        }
        if conf.sample_rate != self.sample_rate || sample_format != JACK_SAMPLE_FORMAT {
            return Err(BuildStreamError::StreamConfigNotSupported);
        }
        self.validate_buffer_size(conf)?;

        // The settings should be fine, create a Client
        let client_options = super::get_client_options(self.start_server_automatically);
        let client;
        match super::get_client(&self.name, client_options) {
            Ok(c) => client = c,
            Err(e) => {
                return Err(BuildStreamError::BackendSpecific {
                    err: BackendSpecificError { description: e },
                })
            }
        };
        let mut stream = Stream::new_input(client, conf.channels, data_callback, error_callback);

        if self.connect_ports_automatically {
            stream.connect_to_system_inputs();
        }

        Ok(stream)
    }

    fn build_output_stream_raw<D, E>(
        &self,
        conf: StreamConfig,
        sample_format: SampleFormat,
        data_callback: D,
        error_callback: E,
        _timeout: Option<Duration>,
    ) -> Result<Self::Stream, BuildStreamError>
    where
        D: FnMut(&mut Data, &OutputCallbackInfo) + Send + 'static,
        E: FnMut(StreamError) + Send + 'static,
    {
        if self.is_input() {
            // Trying to create an output stream from an input device
            return Err(BuildStreamError::StreamConfigNotSupported);
        }
        if conf.sample_rate != self.sample_rate || sample_format != JACK_SAMPLE_FORMAT {
            return Err(BuildStreamError::StreamConfigNotSupported);
        }
        self.validate_buffer_size(conf)?;

        // The settings should be fine, create a Client
        let client_options = super::get_client_options(self.start_server_automatically);
        let client;
        match super::get_client(&self.name, client_options) {
            Ok(c) => client = c,
            Err(e) => {
                return Err(BuildStreamError::BackendSpecific {
                    err: BackendSpecificError { description: e },
                })
            }
        };
        let mut stream = Stream::new_output(client, conf.channels, data_callback, error_callback);

        if self.connect_ports_automatically {
            stream.connect_to_system_outputs();
        }

        Ok(stream)
    }
}

impl PartialEq for Device {
    fn eq(&self, other: &Self) -> bool {
        // Device::id() can never fail in this implementation
        self.id().unwrap() == other.id().unwrap()
    }
}

impl Eq for Device {}

impl Hash for Device {
    fn hash<H: Hasher>(&self, state: &mut H) {
        // Device::id() can never fail in this implementation
        self.id().unwrap().hash(state);
    }
}
```

## File: `src/host/jack/mod.rs`
```rust
//! JACK backend implementation.
//!
//! Available on all platforms with the `jack` feature. Requires JACK server and client libraries.

extern crate jack;

use crate::traits::HostTrait;
use crate::{DevicesError, SampleFormat};

mod device;
mod stream;

#[allow(unused_imports)] // Re-exported for public API via platform module
pub use self::{
    device::{Device, SupportedInputConfigs, SupportedOutputConfigs},
    stream::Stream,
};

const JACK_SAMPLE_FORMAT: SampleFormat = SampleFormat::F32;

pub type Devices = std::vec::IntoIter<Device>;

/// The JACK host, providing access to JACK audio devices.
///
/// # JACK-Specific Configuration
///
/// Unlike other backends, JACK provides configuration options to control connection and server behavior:
/// - Port auto-connection via [`set_connect_automatically`](Host::set_connect_automatically)
/// - Server auto-start via [`set_start_server_automatically`](Host::set_start_server_automatically)
#[derive(Debug)]
pub struct Host {
    /// The name that the client will have in JACK.
    /// Until we have duplex streams two clients will be created adding "out" or "in" to the name
    /// since names have to be unique.
    name: String,
    /// If ports are to be connected to the system (soundcard) ports automatically (default is true).
    connect_ports_automatically: bool,
    /// If the JACK server should be started automatically if it isn't already when creating a Client (default is false).
    start_server_automatically: bool,
    /// A list of the devices that have been created from this Host.
    devices_created: Vec<Device>,
}

impl Host {
    pub fn new() -> Result<Self, crate::HostUnavailable> {
        let mut host = Host {
            name: "cpal_client".to_owned(),
            connect_ports_automatically: true,
            start_server_automatically: false,
            devices_created: vec![],
        };
        // Devices don't exist for JACK, they have to be created
        host.initialize_default_devices();
        Ok(host)
    }
    /// Configures whether created ports should automatically connect to system playback/capture ports.
    ///
    /// When enabled (default), output streams connect to system playback ports and input streams
    /// connect to system capture ports automatically. When disabled, applications must manually
    /// connect ports using JACK tools or APIs.
    ///
    /// Default: `true`
    pub fn set_connect_automatically(&mut self, do_connect: bool) {
        self.connect_ports_automatically = do_connect;
    }

    /// Configures whether the JACK server should automatically start if not already running.
    ///
    /// When enabled, attempting to create a JACK client will start the JACK server if it's not
    /// running. When disabled (default), client creation fails if the server is not running.
    ///
    /// Default: `false`
    pub fn set_start_server_automatically(&mut self, do_start_server: bool) {
        self.start_server_automatically = do_start_server;
    }

    pub fn input_device_with_name(&mut self, name: &str) -> Option<Device> {
        self.name = name.to_owned();
        self.default_input_device()
    }

    pub fn output_device_with_name(&mut self, name: &str) -> Option<Device> {
        self.name = name.to_owned();
        self.default_output_device()
    }

    fn initialize_default_devices(&mut self) {
        let in_device_res = Device::default_input_device(
            &self.name,
            self.connect_ports_automatically,
            self.start_server_automatically,
        );

        match in_device_res {
            Ok(device) => self.devices_created.push(device),
            Err(err) => {
                println!("{}", err);
            }
        }

        let out_device_res = Device::default_output_device(
            &self.name,
            self.connect_ports_automatically,
            self.start_server_automatically,
        );
        match out_device_res {
            Ok(device) => self.devices_created.push(device),
            Err(err) => {
                println!("{}", err);
            }
        }
    }
}

impl HostTrait for Host {
    type Devices = Devices;
    type Device = Device;

    /// JACK is available if
    /// - the jack feature flag is set
    /// - libjack is installed (wouldn't compile without it)
    /// - the JACK server can be started
    ///
    /// If the code compiles the necessary jack libraries are installed.
    /// There is no way to know if the user has set up a correct JACK configuration e.g. with qjackctl.
    /// Users can choose to automatically start the server if it isn't already started when creating a client
    /// so checking if the server is running could give a false negative in some use cases.
    /// For these reasons this function should always return true.
    fn is_available() -> bool {
        true
    }

    fn devices(&self) -> Result<Self::Devices, DevicesError> {
        Ok(self.devices_created.clone().into_iter())
    }

    fn default_input_device(&self) -> Option<Self::Device> {
        for device in &self.devices_created {
            if device.is_input() {
                return Some(device.clone());
            }
        }
        None
    }

    fn default_output_device(&self) -> Option<Self::Device> {
        for device in &self.devices_created {
            if device.is_output() {
                return Some(device.clone());
            }
        }
        None
    }
}

fn get_client_options(start_server_automatically: bool) -> jack::ClientOptions {
    let mut client_options = jack::ClientOptions::empty();
    client_options.set(
        jack::ClientOptions::NO_START_SERVER,
        !start_server_automatically,
    );
    client_options
}

fn get_client(name: &str, client_options: jack::ClientOptions) -> Result<jack::Client, String> {
    let c_res = jack::Client::new(name, client_options);
    match c_res {
        Ok((client, status)) => {
            // The ClientStatus can tell us many things
            if status.intersects(jack::ClientStatus::SERVER_ERROR) {
                return Err(String::from(
                    "There was an error communicating with the JACK server!",
                ));
            } else if status.intersects(jack::ClientStatus::SERVER_FAILED) {
                return Err(String::from("Could not connect to the JACK server!"));
            } else if status.intersects(jack::ClientStatus::VERSION_ERROR) {
                return Err(String::from(
                    "Error connecting to JACK server: Client's protocol version does not match!",
                ));
            } else if status.intersects(jack::ClientStatus::INIT_FAILURE) {
                return Err(String::from(
                    "Error connecting to JACK server: Unable to initialize client!",
                ));
            } else if status.intersects(jack::ClientStatus::SHM_FAILURE) {
                return Err(String::from(
                    "Error connecting to JACK server: Unable to access shared memory!",
                ));
            } else if status.intersects(jack::ClientStatus::NO_SUCH_CLIENT) {
                return Err(String::from(
                    "Error connecting to JACK server: Requested client does not exist!",
                ));
            } else if status.intersects(jack::ClientStatus::INVALID_OPTION) {
                return Err(String::from("Error connecting to JACK server: The operation contained an invalid or unsupported option!"));
            }
            Ok(client)
        }
        Err(e) => Err(format!("Failed to open client because of error: {:?}", e)),
    }
}
```

## File: `src/host/jack/stream.rs`
```rust
use crate::traits::StreamTrait;
use crate::ChannelCount;
use std::sync::atomic::{AtomicBool, Ordering};
use std::sync::{Arc, Mutex};

use crate::{
    BackendSpecificError, Data, InputCallbackInfo, OutputCallbackInfo, PauseStreamError,
    PlayStreamError, SampleRate, StreamError,
};

use super::JACK_SAMPLE_FORMAT;

type ErrorCallbackPtr = Arc<Mutex<dyn FnMut(StreamError) + Send + 'static>>;

pub struct Stream {
    // TODO: It might be faster to send a message when playing/pausing than to check this every iteration
    playing: Arc<AtomicBool>,
    async_client: jack::AsyncClient<JackNotificationHandler, LocalProcessHandler>,
    // Port names are stored in order to connect them to other ports in jack automatically
    input_port_names: Vec<String>,
    output_port_names: Vec<String>,
}

// Compile-time assertion that Stream is Send and Sync
crate::assert_stream_send!(Stream);
crate::assert_stream_sync!(Stream);

impl Stream {
    // TODO: Return error messages
    pub fn new_input<D, E>(
        client: jack::Client,
        channels: ChannelCount,
        data_callback: D,
        mut error_callback: E,
    ) -> Stream
    where
        D: FnMut(&Data, &InputCallbackInfo) + Send + 'static,
        E: FnMut(StreamError) + Send + 'static,
    {
        let mut ports = vec![];
        let mut port_names: Vec<String> = vec![];
        // Create ports
        for i in 0..channels {
            let port_try = client.register_port(&format!("in_{}", i), jack::AudioIn::default());
            match port_try {
                Ok(port) => {
                    // Get the port name in order to later connect it automatically
                    if let Ok(port_name) = port.name() {
                        port_names.push(port_name);
                    }
                    // Store the port into a Vec to move to the ProcessHandler
                    ports.push(port);
                }
                Err(e) => {
                    // If port creation failed, send the error back via the error_callback
                    error_callback(
                        BackendSpecificError {
                            description: e.to_string(),
                        }
                        .into(),
                    );
                }
            }
        }

        let playing = Arc::new(AtomicBool::new(true));

        let error_callback_ptr = Arc::new(Mutex::new(error_callback)) as ErrorCallbackPtr;

        let input_process_handler = LocalProcessHandler::new(
            vec![],
            ports,
            client.sample_rate(),
            client.buffer_size() as usize,
            Some(Box::new(data_callback)),
            None,
            playing.clone(),
            Arc::clone(&error_callback_ptr),
        );

        let notification_handler = JackNotificationHandler::new(error_callback_ptr);

        let async_client = client
            .activate_async(notification_handler, input_process_handler)
            .unwrap();

        Stream {
            playing,
            async_client,
            input_port_names: port_names,
            output_port_names: vec![],
        }
    }

    pub fn new_output<D, E>(
        client: jack::Client,
        channels: ChannelCount,
        data_callback: D,
        mut error_callback: E,
    ) -> Stream
    where
        D: FnMut(&mut Data, &OutputCallbackInfo) + Send + 'static,
        E: FnMut(StreamError) + Send + 'static,
    {
        let mut ports = vec![];
        let mut port_names: Vec<String> = vec![];
        // Create ports
        for i in 0..channels {
            let port_try = client.register_port(&format!("out_{}", i), jack::AudioOut::default());
            match port_try {
                Ok(port) => {
                    // Get the port name in order to later connect it automatically
                    if let Ok(port_name) = port.name() {
                        port_names.push(port_name);
                    }
                    // Store the port into a Vec to move to the ProcessHandler
                    ports.push(port);
                }
                Err(e) => {
                    // If port creation failed, send the error back via the error_callback
                    error_callback(
                        BackendSpecificError {
                            description: e.to_string(),
                        }
                        .into(),
                    );
                }
            }
        }

        let playing = Arc::new(AtomicBool::new(true));

        let error_callback_ptr = Arc::new(Mutex::new(error_callback)) as ErrorCallbackPtr;

        let output_process_handler = LocalProcessHandler::new(
            ports,
            vec![],
            client.sample_rate(),
            client.buffer_size() as usize,
            None,
            Some(Box::new(data_callback)),
            playing.clone(),
            Arc::clone(&error_callback_ptr),
        );

        let notification_handler = JackNotificationHandler::new(error_callback_ptr);

        let async_client = client
            .activate_async(notification_handler, output_process_handler)
            .unwrap();

        Stream {
            playing,
            async_client,
            input_port_names: vec![],
            output_port_names: port_names,
        }
    }

    /// Connect to the standard system outputs in jack, system:playback_1 and system:playback_2
    /// This has to be done after the client is activated, doing it just after creating the ports doesn't work.
    pub fn connect_to_system_outputs(&mut self) {
        // Get the system ports
        let system_ports = self.async_client.as_client().ports(
            Some("system:playback_.*"),
            None,
            jack::PortFlags::empty(),
        );

        // Connect outputs from this client to the system playback inputs
        for i in 0..self.output_port_names.len() {
            if i >= system_ports.len() {
                break;
            }
            match self
                .async_client
                .as_client()
                .connect_ports_by_name(&self.output_port_names[i], &system_ports[i])
            {
                Ok(_) => (),
                Err(e) => println!("Unable to connect to port with error {}", e),
            }
        }
    }

    /// Connect to the standard system outputs in jack, system:capture_1 and system:capture_2
    /// This has to be done after the client is activated, doing it just after creating the ports doesn't work.
    pub fn connect_to_system_inputs(&mut self) {
        // Get the system ports
        let system_ports = self.async_client.as_client().ports(
            Some("system:capture_.*"),
            None,
            jack::PortFlags::empty(),
        );

        // Connect outputs from this client to the system playback inputs
        for i in 0..self.input_port_names.len() {
            if i >= system_ports.len() {
                break;
            }
            match self
                .async_client
                .as_client()
                .connect_ports_by_name(&system_ports[i], &self.input_port_names[i])
            {
                Ok(_) => (),
                Err(e) => println!("Unable to connect to port with error {}", e),
            }
        }
    }
}

impl StreamTrait for Stream {
    fn play(&self) -> Result<(), PlayStreamError> {
        self.playing.store(true, Ordering::SeqCst);
        Ok(())
    }

    fn pause(&self) -> Result<(), PauseStreamError> {
        self.playing.store(false, Ordering::SeqCst);
        Ok(())
    }

    fn buffer_size(&self) -> Option<crate::FrameCount> {
        Some(self.async_client.as_client().buffer_size() as crate::FrameCount)
    }
}

type InputDataCallback = Box<dyn FnMut(&Data, &InputCallbackInfo) + Send + 'static>;
type OutputDataCallback = Box<dyn FnMut(&mut Data, &OutputCallbackInfo) + Send + 'static>;

struct LocalProcessHandler {
    /// No new ports are allowed to be created after the creation of the LocalProcessHandler as that would invalidate the buffer sizes
    out_ports: Vec<jack::Port<jack::AudioOut>>,
    in_ports: Vec<jack::Port<jack::AudioIn>>,

    sample_rate: SampleRate,
    buffer_size: usize,
    input_data_callback: Option<InputDataCallback>,
    output_data_callback: Option<OutputDataCallback>,

    // JACK audio samples are 32-bit float (unless you do some custom dark magic)
    temp_input_buffer: Vec<f32>,
    temp_output_buffer: Vec<f32>,
    playing: Arc<AtomicBool>,
    creation_timestamp: std::time::Instant,
    /// This should not be called on `process`, only on `buffer_size` because it can block.
    error_callback_ptr: ErrorCallbackPtr,
}

impl LocalProcessHandler {
    #[allow(clippy::too_many_arguments)]
    fn new(
        out_ports: Vec<jack::Port<jack::AudioOut>>,
        in_ports: Vec<jack::Port<jack::AudioIn>>,
        sample_rate: SampleRate,
        buffer_size: usize,
        input_data_callback: Option<InputDataCallback>,
        output_data_callback: Option<OutputDataCallback>,
        playing: Arc<AtomicBool>,
        error_callback_ptr: ErrorCallbackPtr,
    ) -> Self {
        // These may be reallocated in the `buffer_size` callback.
        let temp_input_buffer = vec![0.0; in_ports.len() * buffer_size];
        let temp_output_buffer = vec![0.0; out_ports.len() * buffer_size];

        LocalProcessHandler {
            out_ports,
            in_ports,
            sample_rate,
            buffer_size,
            input_data_callback,
            output_data_callback,
            temp_input_buffer,
            temp_output_buffer,
            playing,
            creation_timestamp: std::time::Instant::now(),
            error_callback_ptr,
        }
    }
}

fn temp_buffer_to_data(temp_input_buffer: &mut [f32], total_buffer_size: usize) -> Data {
    let slice = &mut temp_input_buffer[0..total_buffer_size];
    let data: *mut () = slice.as_mut_ptr().cast();
    let len = total_buffer_size;
    unsafe { Data::from_parts(data, len, JACK_SAMPLE_FORMAT) }
}

impl jack::ProcessHandler for LocalProcessHandler {
    fn process(&mut self, _: &jack::Client, process_scope: &jack::ProcessScope) -> jack::Control {
        if !self.playing.load(Ordering::SeqCst) {
            return jack::Control::Continue;
        }

        // This should be equal to self.buffer_size, but the implementation will
        // work even if it is less. Will panic in `temp_buffer_to_data` if greater.
        let current_frame_count = process_scope.n_frames() as usize;

        // Get timestamp data
        let (current_start_usecs, next_usecs_opt) = match process_scope.cycle_times() {
            Ok(times) => (times.current_usecs, Some(times.next_usecs)),
            Err(_) => {
                // jack was unable to get the current time information
                // Fall back to using Instants
                let now = std::time::Instant::now();
                let duration = now.duration_since(self.creation_timestamp);
                (duration.as_micros() as u64, None)
            }
        };
        let start_cycle_instant = micros_to_stream_instant(current_start_usecs);
        let start_callback_instant = start_cycle_instant
            .add(frames_to_duration(
                process_scope.frames_since_cycle_start() as usize,
                self.sample_rate,
            ))
            .expect("`playback` occurs beyond representation supported by `StreamInstant`");

        if let Some(input_callback) = &mut self.input_data_callback {
            // Let's get the data from the input ports and run the callback

            let num_in_channels = self.in_ports.len();

            // Read the data from the input ports into the temporary buffer
            // Go through every channel and store its data in the temporary input buffer
            for ch_ix in 0..num_in_channels {
                let input_channel = &self.in_ports[ch_ix].as_slice(process_scope);
                for i in 0..current_frame_count {
                    self.temp_input_buffer[ch_ix + i * num_in_channels] = input_channel[i];
                }
            }
            // Create a slice of exactly current_frame_count frames
            let data = temp_buffer_to_data(
                &mut self.temp_input_buffer,
                current_frame_count * num_in_channels,
            );
            // Create timestamp
            let callback = start_callback_instant;
            // Input data was made available at the start of the cycle (current_usecs).
            let capture = start_cycle_instant;
            let timestamp = crate::InputStreamTimestamp { callback, capture };
            let info = crate::InputCallbackInfo { timestamp };
            input_callback(&data, &info);
        }

        if let Some(output_callback) = &mut self.output_data_callback {
            let num_out_channels = self.out_ports.len();

            // Create a slice of exactly current_frame_count frames
            let mut data = temp_buffer_to_data(
                &mut self.temp_output_buffer,
                current_frame_count * num_out_channels,
            );
            // Create timestamp
            let callback = start_callback_instant;
            // Use next_usecs (the hardware deadline for this cycle) when available; it is the
            // exact instant at which the last sample written here will be consumed by the device.
            let playback = match next_usecs_opt {
                Some(next_usecs) => micros_to_stream_instant(next_usecs),
                None => start_cycle_instant
                    .add(frames_to_duration(current_frame_count, self.sample_rate))
                    .expect("`playback` occurs beyond representation supported by `StreamInstant`"),
            };
            let timestamp = crate::OutputStreamTimestamp { callback, playback };
            let info = crate::OutputCallbackInfo { timestamp };
            output_callback(&mut data, &info);

            // Deinterlace
            for ch_ix in 0..num_out_channels {
                let output_channel = &mut self.out_ports[ch_ix].as_mut_slice(process_scope);
                for i in 0..current_frame_count {
                    output_channel[i] = self.temp_output_buffer[ch_ix + i * num_out_channels];
                }
            }
        }

        // Continue as normal
        jack::Control::Continue
    }

    fn buffer_size(&mut self, _: &jack::Client, size: jack::Frames) -> jack::Control {
        // The `buffer_size` callback is actually called on the process thread, but
        // it does not need to be suitable for real-time use. Thus we can simply allocate
        // new buffers here. It is also fine to call the error callback.
        // Details: https://github.com/RustAudio/rust-jack/issues/137
        let new_size = size as usize;
        if new_size != self.buffer_size {
            self.buffer_size = new_size;
            self.temp_input_buffer = vec![0.0; self.in_ports.len() * new_size];
            self.temp_output_buffer = vec![0.0; self.out_ports.len() * new_size];
            let description = format!("buffer size changed to: {}", new_size);
            if let Ok(mut mutex_guard) = self.error_callback_ptr.lock() {
                let err = &mut *mutex_guard;
                err(BackendSpecificError { description }.into());
            }
        }

        jack::Control::Continue
    }
}

fn micros_to_stream_instant(micros: u64) -> crate::StreamInstant {
    crate::StreamInstant::from_nanos_i128(micros as i128 * 1_000)
        .expect("`micros` out of range of `StreamInstant` representation")
}

// Convert the given duration in frames at the given sample rate to a `std::time::Duration`.
fn frames_to_duration(frames: usize, rate: crate::SampleRate) -> std::time::Duration {
    let secsf = frames as f64 / rate as f64;
    let secs = secsf as u64;
    let nanos = ((secsf - secs as f64) * 1_000_000_000.0) as u32;
    std::time::Duration::new(secs, nanos)
}

/// Receives notifications from the JACK server. It is unclear if this may be run concurrent with itself under JACK2 specs
/// so it needs to be Sync.
struct JackNotificationHandler {
    error_callback_ptr: ErrorCallbackPtr,
    init_sample_rate_flag: Arc<AtomicBool>,
}

impl JackNotificationHandler {
    pub fn new(error_callback_ptr: ErrorCallbackPtr) -> Self {
        JackNotificationHandler {
            error_callback_ptr,
            init_sample_rate_flag: Arc::new(AtomicBool::new(false)),
        }
    }

    fn send_error(&mut self, description: String) {
        // This thread isn't the audio thread, it's fine to block
        if let Ok(mut mutex_guard) = self.error_callback_ptr.lock() {
            let err = &mut *mutex_guard;
            err(BackendSpecificError { description }.into());
        }
    }
}

impl jack::NotificationHandler for JackNotificationHandler {
    unsafe fn shutdown(&mut self, _status: jack::ClientStatus, reason: &str) {
        self.send_error(format!("JACK was shut down for reason: {}", reason));
    }

    fn sample_rate(&mut self, _: &jack::Client, _srate: jack::Frames) -> jack::Control {
        match self.init_sample_rate_flag.load(Ordering::SeqCst) {
            false => {
                // One of these notifications is sent every time a client is started.
                self.init_sample_rate_flag.store(true, Ordering::SeqCst);
                jack::Control::Continue
            }
            true => {
                // The JACK server has changed the sample rate, invalidating this stream.
                // The stream configuration must be rebuilt with the new sample rate.
                if let Ok(mut cb) = self.error_callback_ptr.lock() {
                    cb(StreamError::StreamInvalidated);
                }
                jack::Control::Quit
            }
        }
    }

    fn xrun(&mut self, _: &jack::Client) -> jack::Control {
        if let Ok(mut cb) = self.error_callback_ptr.lock() {
            cb(StreamError::BufferUnderrun);
        }
        jack::Control::Continue
    }
}
```

## File: `src/host/null/mod.rs`
```rust
//! Null backend implementation.
//!
//! Fallback no-op backend for unsupported platforms.

use std::time::Duration;

use crate::traits::{DeviceTrait, HostTrait, StreamTrait};
use crate::{
    BuildStreamError, Data, DefaultStreamConfigError, DeviceDescription, DeviceDescriptionBuilder,
    DeviceId, DeviceIdError, DeviceNameError, DevicesError, InputCallbackInfo, OutputCallbackInfo,
    PauseStreamError, PlayStreamError, SampleFormat, StreamConfig, StreamError,
    SupportedStreamConfig, SupportedStreamConfigRange, SupportedStreamConfigsError,
};

#[derive(Default)]
pub struct Devices;

#[derive(Clone, Debug, PartialEq, Eq, Hash)]
pub struct Device;

pub struct Host;

#[derive(Debug, Clone, PartialEq, Eq, Hash)]
pub struct Stream;

// Compile-time assertion that Stream is Send and Sync
crate::assert_stream_send!(Stream);
crate::assert_stream_sync!(Stream);

#[derive(Clone)]
pub struct SupportedInputConfigs;
#[derive(Clone)]
pub struct SupportedOutputConfigs;

impl Host {
    #[allow(dead_code)]
    pub fn new() -> Result<Self, crate::HostUnavailable> {
        Ok(Host)
    }
}

impl Devices {
    pub fn new() -> Result<Self, DevicesError> {
        Ok(Devices)
    }
}

impl DeviceTrait for Device {
    type SupportedInputConfigs = SupportedInputConfigs;
    type SupportedOutputConfigs = SupportedOutputConfigs;
    type Stream = Stream;

    fn name(&self) -> Result<String, DeviceNameError> {
        Ok("null".to_string())
    }

    fn description(&self) -> Result<DeviceDescription, DeviceNameError> {
        Ok(DeviceDescriptionBuilder::new("Null Device".to_string()).build())
    }

    fn id(&self) -> Result<DeviceId, DeviceIdError> {
        Ok(DeviceId(crate::platform::HostId::Null, String::new()))
    }

    fn supported_input_configs(
        &self,
    ) -> Result<SupportedInputConfigs, SupportedStreamConfigsError> {
        unimplemented!()
    }

    fn supported_output_configs(
        &self,
    ) -> Result<SupportedOutputConfigs, SupportedStreamConfigsError> {
        unimplemented!()
    }

    fn default_input_config(&self) -> Result<SupportedStreamConfig, DefaultStreamConfigError> {
        unimplemented!()
    }

    fn default_output_config(&self) -> Result<SupportedStreamConfig, DefaultStreamConfigError> {
        unimplemented!()
    }

    fn build_input_stream_raw<D, E>(
        &self,
        _config: StreamConfig,
        _sample_format: SampleFormat,
        _data_callback: D,
        _error_callback: E,
        _timeout: Option<Duration>,
    ) -> Result<Self::Stream, BuildStreamError>
    where
        D: FnMut(&Data, &InputCallbackInfo) + Send + 'static,
        E: FnMut(StreamError) + Send + 'static,
    {
        unimplemented!()
    }

    /// Create an output stream.
    fn build_output_stream_raw<D, E>(
        &self,
        _config: StreamConfig,
        _sample_format: SampleFormat,
        _data_callback: D,
        _error_callback: E,
        _timeout: Option<Duration>,
    ) -> Result<Self::Stream, BuildStreamError>
    where
        D: FnMut(&mut Data, &OutputCallbackInfo) + Send + 'static,
        E: FnMut(StreamError) + Send + 'static,
    {
        unimplemented!()
    }
}

impl HostTrait for Host {
    type Devices = Devices;
    type Device = Device;

    fn is_available() -> bool {
        false
    }

    fn devices(&self) -> Result<Self::Devices, DevicesError> {
        Devices::new()
    }

    fn default_input_device(&self) -> Option<Device> {
        None
    }

    fn default_output_device(&self) -> Option<Device> {
        None
    }
}

impl StreamTrait for Stream {
    fn play(&self) -> Result<(), PlayStreamError> {
        unimplemented!()
    }

    fn pause(&self) -> Result<(), PauseStreamError> {
        unimplemented!()
    }
}

impl Iterator for Devices {
    type Item = Device;

    fn next(&mut self) -> Option<Device> {
        None
    }
}

impl Iterator for SupportedInputConfigs {
    type Item = SupportedStreamConfigRange;

    fn next(&mut self) -> Option<SupportedStreamConfigRange> {
        None
    }
}

impl Iterator for SupportedOutputConfigs {
    type Item = SupportedStreamConfigRange;

    fn next(&mut self) -> Option<SupportedStreamConfigRange> {
        None
    }
}
```

## File: `src/host/pipewire/device.rs`
```rust
use std::sync::{atomic::AtomicU64, Arc};
use std::time::Duration;
use std::{cell::RefCell, rc::Rc};

use crate::host::pipewire::stream::{StreamCommand, StreamData, SUPPORTED_FORMATS};
use crate::host::pipewire::utils::{audio, clock, DEVICE_ICON_NAME, METADATA_NAME};
use crate::{traits::DeviceTrait, DeviceDirection, SupportedStreamConfigRange};
use crate::{ChannelCount, FrameCount, InterfaceType, SampleRate};

use crate::iter::{SupportedInputConfigs, SupportedOutputConfigs};
use pipewire::{
    self as pw,
    metadata::{Metadata, MetadataListener},
    node::{Node, NodeListener},
    proxy::ProxyT,
    spa::utils::result::AsyncSeq,
};

use std::thread;

use super::stream::Stream;

pub type Devices = std::vec::IntoIter<Device>;

// This enum record whether it is created by human or just default device
#[derive(Clone, Debug, Default, Copy)]
pub(crate) enum Class {
    #[default]
    Node,
    DefaultSink,
    DefaultInput,
    DefaultOutput,
}

#[derive(Clone, Debug, Default, Copy)]
pub enum Role {
    Sink,
    #[default]
    Source,
    Duplex,
    StreamOutput,
    StreamInput,
}

#[derive(Clone, Debug, Default)]
pub struct Device {
    node_name: String,
    nick_name: String,
    description: String,
    direction: DeviceDirection,
    channels: ChannelCount,
    rate: SampleRate,
    allow_rates: Vec<SampleRate>,
    quantum: FrameCount,
    min_quantum: FrameCount,
    max_quantum: FrameCount,
    class: Class,
    role: Role,
    icon_name: String,
    object_serial: u32,
    interface_type: InterfaceType,
    address: Option<String>,
    driver: Option<String>,
}

impl Device {
    pub(crate) fn class(&self) -> Class {
        self.class
    }
    fn sink_default() -> Self {
        Self {
            node_name: "sink_default".to_owned(),
            nick_name: "sink_default".to_owned(),
            description: "default_sink".to_owned(),
            direction: DeviceDirection::Duplex,
            channels: 2,
            class: Class::DefaultSink,
            role: Role::Sink,
            ..Default::default()
        }
    }
    fn input_default() -> Self {
        Self {
            node_name: "input_default".to_owned(),
            nick_name: "input_default".to_owned(),
            description: "default_input".to_owned(),
            direction: DeviceDirection::Input,
            channels: 2,
            class: Class::DefaultInput,
            role: Role::Source,
            ..Default::default()
        }
    }
    fn output_default() -> Self {
        Self {
            node_name: "output_default".to_owned(),
            nick_name: "output_default".to_owned(),
            description: "default_output".to_owned(),
            direction: DeviceDirection::Output,
            channels: 2,
            class: Class::DefaultOutput,
            role: Role::Source,
            ..Default::default()
        }
    }

    fn device_type(&self) -> crate::DeviceType {
        match self.icon_name.as_str() {
            "audio-headphones" => crate::DeviceType::Headphones,
            "audio-headset" => crate::DeviceType::Headset,
            "audio-input-microphone" => crate::DeviceType::Microphone,
            "audio-speakers" => crate::DeviceType::Speaker,
            _ => crate::DeviceType::Unknown,
        }
    }

    pub(crate) fn pw_properties(
        &self,
        direction: DeviceDirection,
        config: &crate::StreamConfig,
    ) -> pw::properties::PropertiesBox {
        let mut properties = match direction {
            DeviceDirection::Output => pw::properties::properties! {
                *pw::keys::MEDIA_TYPE => "Audio",
                *pw::keys::MEDIA_CATEGORY => "Playback",
            },
            DeviceDirection::Input => pw::properties::properties! {
                *pw::keys::MEDIA_TYPE => "Audio",
                *pw::keys::MEDIA_CATEGORY => "Capture",
            },
            _ => unreachable!(),
        };
        if matches!(self.role, Role::Sink) {
            properties.insert(*pw::keys::STREAM_CAPTURE_SINK, "true");
        }
        if matches!(self.class, Class::Node) {
            properties.insert(*pw::keys::TARGET_OBJECT, self.object_serial.to_string());
        }
        if let crate::BufferSize::Fixed(buffer_size) = config.buffer_size {
            properties.insert(*pw::keys::NODE_FORCE_QUANTUM, buffer_size.to_string());
        }
        properties
    }
}
impl DeviceTrait for Device {
    type Stream = Stream;
    type SupportedInputConfigs = SupportedInputConfigs;
    type SupportedOutputConfigs = SupportedOutputConfigs;

    fn id(&self) -> Result<crate::DeviceId, crate::DeviceIdError> {
        Ok(crate::DeviceId(
            crate::HostId::PipeWire,
            self.node_name.clone(),
        ))
    }

    fn description(&self) -> Result<crate::DeviceDescription, crate::DeviceNameError> {
        let mut builder = crate::DeviceDescriptionBuilder::new(&self.nick_name)
            .direction(self.direction)
            .device_type(self.device_type())
            .interface_type(self.interface_type);
        if let Some(address) = self.address.as_ref() {
            builder = builder.address(address);
        }
        if let Some(driver) = self.driver.as_ref() {
            builder = builder.driver(driver);
        }
        if !self.description.is_empty() && self.description != self.nick_name {
            builder = builder.add_extended_line(&self.description);
        }
        Ok(builder.build())
    }

    fn supports_input(&self) -> bool {
        matches!(
            self.direction,
            DeviceDirection::Input | DeviceDirection::Duplex
        )
    }

    fn supports_output(&self) -> bool {
        matches!(
            self.direction,
            DeviceDirection::Output | DeviceDirection::Duplex
        )
    }

    fn supported_input_configs(
        &self,
    ) -> Result<Self::SupportedInputConfigs, crate::SupportedStreamConfigsError> {
        if !self.supports_input() {
            return Ok(vec![].into_iter());
        }
        let rates = if self.allow_rates.is_empty() {
            vec![self.rate]
        } else {
            self.allow_rates.clone()
        };
        Ok(rates
            .iter()
            .flat_map(|&rate| {
                SUPPORTED_FORMATS
                    .iter()
                    .map(move |sample_format| SupportedStreamConfigRange {
                        channels: self.channels,
                        min_sample_rate: rate,
                        max_sample_rate: rate,
                        buffer_size: crate::SupportedBufferSize::Range {
                            min: self.min_quantum,
                            max: self.max_quantum,
                        },
                        sample_format: *sample_format,
                    })
            })
            .collect::<Vec<_>>()
            .into_iter())
    }
    fn supported_output_configs(
        &self,
    ) -> Result<Self::SupportedOutputConfigs, crate::SupportedStreamConfigsError> {
        if !self.supports_output() {
            return Ok(vec![].into_iter());
        }
        let rates = if self.allow_rates.is_empty() {
            vec![self.rate]
        } else {
            self.allow_rates.clone()
        };
        Ok(rates
            .iter()
            .flat_map(|&rate| {
                SUPPORTED_FORMATS
                    .iter()
                    .map(move |sample_format| SupportedStreamConfigRange {
                        channels: self.channels,
                        min_sample_rate: rate,
                        max_sample_rate: rate,
                        buffer_size: crate::SupportedBufferSize::Range {
                            min: self.min_quantum,
                            max: self.max_quantum,
                        },
                        sample_format: *sample_format,
                    })
            })
            .collect::<Vec<_>>()
            .into_iter())
    }
    fn default_input_config(
        &self,
    ) -> Result<crate::SupportedStreamConfig, crate::DefaultStreamConfigError> {
        if !self.supports_input() {
            return Err(crate::DefaultStreamConfigError::StreamTypeNotSupported);
        }
        Ok(crate::SupportedStreamConfig {
            channels: self.channels,
            sample_format: crate::SampleFormat::F32,
            sample_rate: self.rate,
            buffer_size: crate::SupportedBufferSize::Range {
                min: self.min_quantum,
                max: self.max_quantum,
            },
        })
    }

    fn default_output_config(
        &self,
    ) -> Result<crate::SupportedStreamConfig, crate::DefaultStreamConfigError> {
        if !self.supports_output() {
            return Err(crate::DefaultStreamConfigError::StreamTypeNotSupported);
        }
        Ok(crate::SupportedStreamConfig {
            channels: self.channels,
            sample_format: crate::SampleFormat::F32,
            sample_rate: self.rate,
            buffer_size: crate::SupportedBufferSize::Range {
                min: self.min_quantum,
                max: self.max_quantum,
            },
        })
    }

    fn build_input_stream_raw<D, E>(
        &self,
        config: crate::StreamConfig,
        sample_format: crate::SampleFormat,
        data_callback: D,
        error_callback: E,
        timeout: Option<std::time::Duration>,
    ) -> Result<Self::Stream, crate::BuildStreamError>
    where
        D: FnMut(&crate::Data, &crate::InputCallbackInfo) + Send + 'static,
        E: FnMut(crate::StreamError) + Send + 'static,
    {
        let (pw_play_tx, pw_play_rx) = pw::channel::channel::<StreamCommand>();

        let (pw_init_tx, pw_init_rx) = std::sync::mpsc::channel::<bool>();
        let device = self.clone();
        let wait_timeout = timeout.unwrap_or(Duration::from_secs(2));
        let last_quantum = Arc::new(AtomicU64::new(0));
        let last_quantum_clone = last_quantum.clone();
        let handle = thread::Builder::new()
            .name("pw_in".to_owned())
            .spawn(move || {
                let properties = device.pw_properties(DeviceDirection::Input, &config);
                let Ok(StreamData {
                    mainloop,
                    listener,
                    stream,
                    context,
                }) = super::stream::connect_input(
                    config,
                    properties,
                    sample_format,
                    data_callback,
                    error_callback,
                    last_quantum_clone,
                )
                else {
                    let _ = pw_init_tx.send(false);
                    return;
                };
                let _ = pw_init_tx.send(true);
                let stream = stream.clone();
                let mainloop_rc1 = mainloop.clone();
                let _receiver = pw_play_rx.attach(mainloop.loop_(), move |play| match play {
                    StreamCommand::Toggle(state) => {
                        let _ = stream.set_active(state);
                    }
                    StreamCommand::Stop => {
                        let _ = stream.disconnect();
                        mainloop_rc1.quit();
                    }
                });
                mainloop.run();
                drop(listener);
                drop(context);
            })
            .map_err(|e| crate::BuildStreamError::BackendSpecific {
                err: crate::BackendSpecificError {
                    description: format!("failed to create thread: {e}"),
                },
            })?;
        match pw_init_rx.recv_timeout(wait_timeout) {
            Ok(true) => Ok(Stream {
                handle: Some(handle),
                controller: pw_play_tx,
                last_quantum,
            }),
            Ok(false) => Err(crate::BuildStreamError::StreamConfigNotSupported),
            Err(_) => Err(crate::BuildStreamError::BackendSpecific {
                err: crate::BackendSpecificError {
                    description: "pipewire timeout".to_owned(),
                },
            }),
        }
    }

    fn build_output_stream_raw<D, E>(
        &self,
        config: crate::StreamConfig,
        sample_format: crate::SampleFormat,
        data_callback: D,
        error_callback: E,
        timeout: Option<std::time::Duration>,
    ) -> Result<Self::Stream, crate::BuildStreamError>
    where
        D: FnMut(&mut crate::Data, &crate::OutputCallbackInfo) + Send + 'static,
        E: FnMut(crate::StreamError) + Send + 'static,
    {
        let (pw_play_tx, pw_play_rx) = pw::channel::channel::<StreamCommand>();

        let (pw_init_tx, pw_init_rx) = std::sync::mpsc::channel::<bool>();
        let device = self.clone();
        let wait_timeout = timeout.unwrap_or(Duration::from_secs(2));
        let last_quantum = Arc::new(AtomicU64::new(0));
        let last_quantum_clone = last_quantum.clone();
        let handle = thread::Builder::new()
            .name("pw_out".to_owned())
            .spawn(move || {
                let properties = device.pw_properties(DeviceDirection::Output, &config);

                let Ok(StreamData {
                    mainloop,
                    listener,
                    stream,
                    context,
                }) = super::stream::connect_output(
                    config,
                    properties,
                    sample_format,
                    data_callback,
                    error_callback,
                    last_quantum_clone,
                )
                else {
                    let _ = pw_init_tx.send(false);
                    return;
                };

                let _ = pw_init_tx.send(true);
                let stream = stream.clone();
                let mainloop_rc1 = mainloop.clone();
                let _receiver = pw_play_rx.attach(mainloop.loop_(), move |play| match play {
                    StreamCommand::Toggle(state) => {
                        let _ = stream.set_active(state);
                    }
                    StreamCommand::Stop => {
                        let _ = stream.disconnect();
                        mainloop_rc1.quit();
                    }
                });
                mainloop.run();
                drop(listener);
                drop(context);
            })
            .map_err(|e| crate::BuildStreamError::BackendSpecific {
                err: crate::BackendSpecificError {
                    description: format!("failed to create thread: {e}"),
                },
            })?;
        match pw_init_rx.recv_timeout(wait_timeout) {
            Ok(true) => Ok(Stream {
                handle: Some(handle),
                controller: pw_play_tx,
                last_quantum,
            }),
            Ok(false) => Err(crate::BuildStreamError::StreamConfigNotSupported),
            Err(_) => Err(crate::BuildStreamError::BackendSpecific {
                err: crate::BackendSpecificError {
                    description: "pipewire timeout".to_owned(),
                },
            }),
        }
    }
}

#[derive(Debug, Clone, Default)]
struct Settings {
    rate: SampleRate,
    allow_rates: Vec<SampleRate>,
    quantum: FrameCount,
    min_quantum: FrameCount,
    max_quantum: FrameCount,
}

// NOTE: it is just used to keep the lifetime
#[allow(dead_code)]
enum Request {
    Node(NodeListener),
    Meta(MetadataListener),
}

impl From<NodeListener> for Request {
    fn from(value: NodeListener) -> Self {
        Self::Node(value)
    }
}

impl From<MetadataListener> for Request {
    fn from(value: MetadataListener) -> Self {
        Self::Meta(value)
    }
}

pub fn init_devices() -> Option<Vec<Device>> {
    pw::init();
    let mainloop = pw::main_loop::MainLoopRc::new(None).ok()?;
    let context = pw::context::ContextRc::new(&mainloop, None).ok()?;
    let core = context.connect_rc(None).ok()?;
    let registry = core.get_registry_rc().ok()?;

    // To comply with Rust's safety rules, we wrap this variable in an `Rc` and  a `Cell`.
    let devices: Rc<RefCell<Vec<Device>>> = Rc::new(RefCell::new(vec![
        Device::sink_default(),
        Device::input_default(),
        Device::output_default(),
    ]));
    let requests = Rc::new(RefCell::new(vec![]));
    let settings = Rc::new(RefCell::new(Settings::default()));
    let loop_clone = mainloop.clone();

    // Trigger the sync event. The server's answer won't be processed until we start the main loop,
    // so we can safely do this before setting up a callback. This lets us avoid using a Cell.
    let pending_events: Rc<RefCell<Vec<AsyncSeq>>> = Rc::new(RefCell::new(vec![]));
    let pending = core.sync(0).ok()?;

    pending_events.borrow_mut().push(pending);

    let _listener_core = core
        .add_listener_local()
        .done({
            let pending_events = pending_events.clone();
            move |id, seq| {
                if id != pw::core::PW_ID_CORE {
                    return;
                }
                let mut pendinglist = pending_events.borrow_mut();
                let Some(index) = pendinglist.iter().position(|o_seq| *o_seq == seq) else {
                    return;
                };
                pendinglist.remove(index);
                if !pendinglist.is_empty() {
                    return;
                }
                loop_clone.quit();
            }
        })
        .register();
    let _listener_reg = registry
        .add_listener_local()
        .global({
            let devices = devices.clone();
            let registry = registry.clone();
            let requests = requests.clone();
            let settings = settings.clone();
            move |global| match global.type_ {
                pipewire::types::ObjectType::Metadata => {
                    if !global.props.is_some_and(|props| {
                        props
                            .get(METADATA_NAME)
                            .is_some_and(|name| name == "settings")
                    }) {
                        return;
                    }
                    let meta_settings: Metadata = match registry.bind(global) {
                        Ok(meta_settings) => meta_settings,
                        Err(_) => {
                            // TODO: do something about this error
                            // Though it is already checked, but maybe something happened with
                            // pipewire?
                            return;
                        }
                    };
                    let settings = settings.clone();
                    let listener = meta_settings
                        .add_listener_local()
                        .property(move |_, key, _, value| {
                            match (key, value) {
                                (Some(clock::RATE), Some(rate)) => {
                                    let Ok(rate) = rate.parse() else {
                                        return 0;
                                    };
                                    settings.borrow_mut().rate = rate;
                                }
                                (Some(clock::ALLOWED_RATES), Some(list)) => {
                                    let Some(allow_rates) = parse_allow_rates(list) else {
                                        return 0;
                                    };

                                    settings.borrow_mut().allow_rates = allow_rates;
                                }
                                (Some(clock::QUANTUM), Some(quantum)) => {
                                    let Ok(quantum) = quantum.parse() else {
                                        return 0;
                                    };
                                    settings.borrow_mut().quantum = quantum;
                                }
                                (Some(clock::MIN_QUANTUM), Some(min_quantum)) => {
                                    let Ok(min_quantum) = min_quantum.parse() else {
                                        return 0;
                                    };
                                    settings.borrow_mut().min_quantum = min_quantum;
                                }
                                (Some(clock::MAX_QUANTUM), Some(max_quantum)) => {
                                    let Ok(max_quantum) = max_quantum.parse() else {
                                        return 0;
                                    };
                                    settings.borrow_mut().max_quantum = max_quantum;
                                }
                                _ => {}
                            }
                            0
                        })
                        .register();
                    let Ok(pending) = core.sync(0) else {
                        // TODO: maybe we should add a log?
                        return;
                    };
                    pending_events.borrow_mut().push(pending);
                    requests
                        .borrow_mut()
                        .push((meta_settings.upcast(), Request::Meta(listener)));
                }
                pipewire::types::ObjectType::Node => {
                    let Some(props) = global.props else {
                        return;
                    };
                    let Some(media_class) = props.get(*pw::keys::MEDIA_CLASS) else {
                        return;
                    };
                    if !matches!(
                        media_class,
                        audio::SINK
                            | audio::SOURCE
                            | audio::DUPLEX
                            | audio::STREAM_INPUT
                            | audio::STREAM_OUTPUT
                    ) {
                        return;
                    }

                    let node: Node = match registry.bind(global) {
                        Ok(node) => node,
                        Err(_) => {
                            // TODO: do something about this error
                            // Though it is already checked, but maybe something happened with
                            // pipewire?
                            return;
                        }
                    };

                    let devices = devices.clone();
                    let listener = node
                        .add_listener_local()
                        .info(move |info| {
                            let Some(props) = info.props() else {
                                return;
                            };
                            let Some(media_class) = props.get(*pw::keys::MEDIA_CLASS) else {
                                return;
                            };
                            let role = match media_class {
                                audio::SINK => Role::Sink,
                                audio::SOURCE => Role::Source,
                                audio::DUPLEX => Role::Duplex,
                                audio::STREAM_OUTPUT => Role::StreamOutput,
                                audio::STREAM_INPUT => Role::StreamInput,
                                _ => {
                                    return;
                                }
                            };
                            let direction = match role {
                                Role::Sink => DeviceDirection::Duplex,
                                Role::Source => DeviceDirection::Input,
                                Role::Duplex => DeviceDirection::Duplex,
                                Role::StreamOutput => DeviceDirection::Output,
                                Role::StreamInput => DeviceDirection::Input,
                            };
                            let Some(object_serial) = props
                                .get(*pw::keys::OBJECT_SERIAL)
                                .and_then(|serial| serial.parse().ok())
                            else {
                                return;
                            };
                            let node_name = props
                                .get(*pw::keys::NODE_NAME)
                                .unwrap_or("unknown")
                                .to_owned();
                            let description = props
                                .get(*pw::keys::NODE_DESCRIPTION)
                                .unwrap_or("unknown")
                                .to_owned();
                            let nick_name = props
                                .get(*pw::keys::NODE_NICK)
                                .unwrap_or(description.as_str())
                                .to_owned();
                            let channels = props
                                .get(*pw::keys::AUDIO_CHANNELS)
                                .and_then(|channels| channels.parse().ok())
                                .unwrap_or(2);

                            let icon_name =
                                props.get(DEVICE_ICON_NAME).unwrap_or("default").to_owned();

                            let interface_type = match props.get(*pw::keys::DEVICE_API) {
                                Some("bluez5") => InterfaceType::Bluetooth,
                                _ => match props.get("device.bus") {
                                    Some("pci") => InterfaceType::Pci,
                                    Some("usb") => InterfaceType::Usb,
                                    Some("firewire") => InterfaceType::FireWire,
                                    Some("thunderbolt") => InterfaceType::Thunderbolt,
                                    _ => InterfaceType::Unknown,
                                },
                            };

                            let address = props
                                .get("api.bluez5.address")
                                .or_else(|| props.get("api.alsa.path"))
                                .map(|s| s.to_owned());

                            let driver = props.get(*pw::keys::FACTORY_NAME).map(|s| s.to_owned());

                            let device = Device {
                                node_name,
                                nick_name,
                                description,
                                direction,
                                role,
                                channels,
                                icon_name,
                                object_serial,
                                interface_type,
                                address,
                                driver,
                                ..Default::default()
                            };
                            devices.borrow_mut().push(device);
                        })
                        .register();
                    let Ok(pending) = core.sync(0) else {
                        // TODO: maybe we should add a log?
                        return;
                    };
                    pending_events.borrow_mut().push(pending);
                    requests
                        .borrow_mut()
                        .push((node.upcast(), Request::Node(listener)));
                }
                _ => {}
            }
        })
        .register();

    mainloop.run();

    let mut devices = devices.take();
    let settings = settings.take();
    for device in devices.iter_mut() {
        device.rate = settings.rate;
        device.allow_rates = settings.allow_rates.clone();
        device.quantum = settings.quantum;
        device.min_quantum = settings.min_quantum;
        device.max_quantum = settings.max_quantum;
    }
    Some(devices)
}

fn parse_allow_rates(list: &str) -> Option<Vec<u32>> {
    let list: Vec<&str> = list
        .trim()
        .strip_prefix("[")?
        .strip_suffix("]")?
        .split(' ')
        .flat_map(|s| s.split(','))
        .filter(|s| !s.is_empty())
        .collect();
    let mut allow_rates = vec![];
    for rate in list {
        let rate = rate.parse().ok()?;
        allow_rates.push(rate);
    }
    Some(allow_rates)
}

#[cfg(test)]
mod test {
    use super::parse_allow_rates;
    #[test]
    fn rate_parse() {
        // In documents, the rates are separated by space
        let rate_str = r#"  [ 44100 48000 88200 96000 176400 192000 ] "#;
        let rates = parse_allow_rates(rate_str).unwrap();
        assert_eq!(rates, vec![44100, 48000, 88200, 96000, 176400, 192000]);
        // ',' is also allowed
        let rate_str = r#"  [ 44100, 48000, 88200, 96000 ,176400 ,192000 ] "#;
        let rates = parse_allow_rates(rate_str).unwrap();
        assert_eq!(rates, vec![44100, 48000, 88200, 96000, 176400, 192000]);
        assert_eq!(rates, vec![44100, 48000, 88200, 96000, 176400, 192000]);
        // We only use [] to define the list
        let rate_str = r#"  { 44100, 48000, 88200, 96000 ,176400 ,192000 } "#;
        let rates = parse_allow_rates(rate_str);
        assert_eq!(rates, None);
    }
}
```

## File: `src/host/pipewire/mod.rs`
```rust
use crate::traits::HostTrait;
use device::{init_devices, Class, Device, Devices};
mod device;
mod stream;
mod utils;

#[inline]
fn pipewire_available() -> bool {
    let dir = std::env::var("PIPEWIRE_RUNTIME_DIR")
        .or_else(|_| std::env::var("XDG_RUNTIME_DIR"))
        .unwrap_or_default();
    std::path::Path::new(&dir).join("pipewire-0").exists()
}

#[derive(Debug)]
pub struct Host(Vec<Device>);

impl Host {
    pub fn new() -> Result<Self, crate::HostUnavailable> {
        let devices = init_devices().ok_or(crate::HostUnavailable)?;
        Ok(Host(devices))
    }
}

impl HostTrait for Host {
    type Devices = Devices;
    type Device = Device;
    fn is_available() -> bool {
        pipewire_available()
    }
    fn devices(&self) -> Result<Self::Devices, crate::DevicesError> {
        Ok(self.0.clone().into_iter())
    }

    fn default_input_device(&self) -> Option<Self::Device> {
        self.0
            .iter()
            .find(|device| matches!(device.class(), Class::DefaultInput))
            .cloned()
    }
    fn default_output_device(&self) -> Option<Self::Device> {
        self.0
            .iter()
            .find(|device| matches!(device.class(), Class::DefaultOutput))
            .cloned()
    }
}
```

## File: `src/host/pipewire/stream.rs`
```rust
use std::{
    sync::{
        atomic::{AtomicU64, Ordering},
        Arc,
    },
    thread::JoinHandle,
    time::Instant,
};

use crate::{
    host::fill_with_equilibrium, traits::StreamTrait, BackendSpecificError, InputCallbackInfo,
    OutputCallbackInfo, SampleFormat, StreamConfig, StreamError, StreamInstant,
};
use pipewire::{
    self as pw,
    context::ContextRc,
    main_loop::MainLoopRc,
    spa::{
        param::{
            format::{MediaSubtype, MediaType},
            format_utils,
        },
        pod::Pod,
    },
    stream::{StreamListener, StreamRc, StreamState},
};

use crate::Data;

#[derive(Debug, Clone, Copy)]
pub enum StreamCommand {
    Toggle(bool),
    Stop,
}

pub struct Stream {
    pub(crate) handle: Option<JoinHandle<()>>,
    pub(crate) controller: pw::channel::Sender<StreamCommand>,
    pub(crate) last_quantum: Arc<AtomicU64>,
}

impl Drop for Stream {
    fn drop(&mut self) {
        let _ = self.controller.send(StreamCommand::Stop);
        let _ = self.handle.take().map(|handle| handle.join());
    }
}

impl StreamTrait for Stream {
    fn play(&self) -> Result<(), crate::PlayStreamError> {
        self.controller
            .send(StreamCommand::Toggle(true))
            .map_err(|_| crate::PlayStreamError::BackendSpecific {
                err: BackendSpecificError {
                    description: "Cannot send message".to_owned(),
                },
            })?;
        Ok(())
    }
    fn pause(&self) -> Result<(), crate::PauseStreamError> {
        self.controller
            .send(StreamCommand::Toggle(false))
            .map_err(|_| crate::PauseStreamError::BackendSpecific {
                err: BackendSpecificError {
                    description: "Cannot send message".to_owned(),
                },
            })?;
        Ok(())
    }

    fn buffer_size(&self) -> Option<crate::FrameCount> {
        match self.last_quantum.load(Ordering::Relaxed) {
            0 => None,
            n => Some(n as _),
        }
    }
}

pub(crate) const SUPPORTED_FORMATS: &[SampleFormat] = &[
    SampleFormat::I8,
    SampleFormat::U8,
    SampleFormat::I16,
    SampleFormat::U16,
    SampleFormat::I24,
    SampleFormat::U24,
    SampleFormat::I32,
    SampleFormat::U32,
    SampleFormat::I64,
    SampleFormat::U64,
    SampleFormat::F32,
    SampleFormat::F64,
];

impl From<SampleFormat> for pw::spa::param::audio::AudioFormat {
    fn from(value: SampleFormat) -> Self {
        match value {
            SampleFormat::I8 => Self::S8,
            SampleFormat::U8 => Self::U8,

            #[cfg(target_endian = "little")]
            SampleFormat::I16 => Self::S16LE,
            #[cfg(target_endian = "big")]
            SampleFormat::I16 => Self::S16BE,
            #[cfg(target_endian = "little")]
            SampleFormat::U16 => Self::U16LE,
            #[cfg(target_endian = "big")]
            SampleFormat::U16 => Self::U16BE,

            #[cfg(target_endian = "little")]
            SampleFormat::I24 => Self::S24LE,
            #[cfg(target_endian = "big")]
            SampleFormat::I24 => Self::S24BE,
            #[cfg(target_endian = "little")]
            SampleFormat::U24 => Self::U24LE,
            #[cfg(target_endian = "big")]
            SampleFormat::U24 => Self::U24BE,
            #[cfg(target_endian = "little")]
            SampleFormat::I32 => Self::S32LE,
            #[cfg(target_endian = "big")]
            SampleFormat::I32 => Self::S32BE,
            #[cfg(target_endian = "little")]
            SampleFormat::U32 => Self::U32LE,
            #[cfg(target_endian = "big")]
            SampleFormat::U32 => Self::U32BE,
            #[cfg(target_endian = "little")]
            SampleFormat::F32 => Self::F32LE,
            #[cfg(target_endian = "big")]
            SampleFormat::F32 => Self::F32BE,
            #[cfg(target_endian = "little")]
            SampleFormat::F64 => Self::F64LE,
            #[cfg(target_endian = "big")]
            SampleFormat::F64 => Self::F64BE,
            // NOTE: Seems PipeWire does support U64 and I64, but libspa doesn't yet.
            // TODO: Maybe add the support in the future
            _ => Self::Unknown,
        }
    }
}

pub struct UserData<D, E> {
    data_callback: D,
    error_callback: E,
    sample_format: SampleFormat,
    format: pw::spa::param::audio::AudioInfoRaw,
    created_instance: Instant,
    last_quantum: Arc<AtomicU64>,
}
impl<D, E> UserData<D, E>
where
    E: FnMut(StreamError) + Send + 'static,
{
    fn state_changed(&mut self, new: StreamState) {
        match new {
            pipewire::stream::StreamState::Error(e) => {
                (self.error_callback)(StreamError::BackendSpecific {
                    err: BackendSpecificError { description: e },
                })
            }
            // TODO: maybe we need to log information when every new state comes?
            pipewire::stream::StreamState::Paused => {}
            pipewire::stream::StreamState::Streaming => {}
            pipewire::stream::StreamState::Connecting => {}
            pipewire::stream::StreamState::Unconnected => {}
        }
    }
}

/// Hardware timestamp from a PipeWire graph cycle.
struct PwTime {
    /// CLOCK_MONOTONIC nanoseconds, stamped at the start of the graph cycle.
    now_ns: i64,
    /// Pipeline delay converted to nanoseconds.
    /// For output: how far ahead of the driver our next sample will be played.
    /// For input:  how long ago the data in the buffer was captured.
    delay_ns: i64,
}

/// Returns a hardware timestamp for the current graph cycle, or `None` if
/// the driver has not started yet or the rate is unavailable.
fn pw_stream_time(stream: &pw::stream::Stream) -> Option<PwTime> {
    let mut t: pw::sys::pw_time = unsafe { std::mem::zeroed() };
    let rc = unsafe {
        pw::sys::pw_stream_get_time_n(
            stream.as_raw_ptr(),
            &mut t,
            std::mem::size_of::<pw::sys::pw_time>(),
        )
    };
    if rc != 0 || t.now == 0 || t.rate.denom == 0 {
        return None;
    }
    debug_assert_eq!(t.rate.num, 1, "unexpected pw_time rate.num");
    let delay_ns = t.delay * 1_000_000_000i64 / t.rate.denom as i64;
    Some(PwTime {
        now_ns: t.now,
        delay_ns,
    })
}

impl<D, E> UserData<D, E>
where
    D: FnMut(&Data, &InputCallbackInfo) + Send + 'static,
    E: FnMut(StreamError) + Send + 'static,
{
    fn publish_data_in(
        &mut self,
        stream: &pw::stream::Stream,
        frames: usize,
        data: &Data,
    ) -> Result<(), BackendSpecificError> {
        self.last_quantum.store(frames as u64, Ordering::Relaxed);
        let (callback, capture) = match pw_stream_time(stream) {
            Some(PwTime { now_ns, delay_ns }) => (
                StreamInstant::from_nanos(now_ns),
                StreamInstant::from_nanos(now_ns - delay_ns),
            ),
            None => {
                let cb = stream_timestamp_fallback(self.created_instance)?;
                let pl = cb
                    .sub(frames_to_duration(frames, self.format.rate()))
                    .ok_or_else(|| BackendSpecificError {
                        description:
                            "`capture` occurs beyond representation supported by `StreamInstant`"
                                .to_string(),
                    })?;
                (cb, pl)
            }
        };
        let timestamp = crate::InputStreamTimestamp { callback, capture };
        let info = InputCallbackInfo { timestamp };
        (self.data_callback)(data, &info);
        Ok(())
    }
}
impl<D, E> UserData<D, E>
where
    D: FnMut(&mut Data, &OutputCallbackInfo) + Send + 'static,
    E: FnMut(StreamError) + Send + 'static,
{
    fn publish_data_out(
        &mut self,
        stream: &pw::stream::Stream,
        frames: usize,
        data: &mut Data,
    ) -> Result<(), BackendSpecificError> {
        self.last_quantum.store(frames as u64, Ordering::Relaxed);
        let (callback, playback) = match pw_stream_time(stream) {
            Some(PwTime { now_ns, delay_ns }) => (
                StreamInstant::from_nanos(now_ns),
                StreamInstant::from_nanos(now_ns + delay_ns),
            ),
            None => {
                let cb = stream_timestamp_fallback(self.created_instance)?;
                let pl = cb
                    .add(frames_to_duration(frames, self.format.rate()))
                    .ok_or_else(|| BackendSpecificError {
                        description:
                            "`playback` occurs beyond representation supported by `StreamInstant`"
                                .to_string(),
                    })?;
                (cb, pl)
            }
        };
        let timestamp = crate::OutputStreamTimestamp { callback, playback };
        let info = OutputCallbackInfo { timestamp };
        (self.data_callback)(data, &info);
        Ok(())
    }
}
pub struct StreamData<D, E> {
    pub mainloop: MainLoopRc,
    pub listener: StreamListener<UserData<D, E>>,
    pub stream: StreamRc,
    pub context: ContextRc,
}

// Use elapsed duration since stream creation as fallback when hardware timestamps are unavailable.
//
// This ensures positive values that are compatible with our `StreamInstant` representation.
#[inline]
fn stream_timestamp_fallback(
    creation: std::time::Instant,
) -> Result<StreamInstant, BackendSpecificError> {
    let now = std::time::Instant::now();
    let duration = now.duration_since(creation);
    StreamInstant::from_nanos_i128(duration.as_nanos() as i128).ok_or(BackendSpecificError {
        description: "stream duration has exceeded `StreamInstant` representation".to_string(),
    })
}

// Convert the given duration in frames at the given sample rate to a `std::time::Duration`.
#[inline]
fn frames_to_duration(frames: usize, rate: crate::SampleRate) -> std::time::Duration {
    let secsf = frames as f64 / rate as f64;
    let secs = secsf as u64;
    let nanos = ((secsf - secs as f64) * 1_000_000_000.0) as u32;
    std::time::Duration::new(secs, nanos)
}

pub fn connect_output<D, E>(
    config: StreamConfig,
    properties: pw::properties::PropertiesBox,
    sample_format: SampleFormat,
    data_callback: D,
    error_callback: E,
    last_quantum: Arc<AtomicU64>,
) -> Result<StreamData<D, E>, pw::Error>
where
    D: FnMut(&mut Data, &OutputCallbackInfo) + Send + 'static,
    E: FnMut(StreamError) + Send + 'static,
{
    pw::init();
    let mainloop = pw::main_loop::MainLoopRc::new(None)?;
    let context = pw::context::ContextRc::new(&mainloop, None)?;
    let core = context.connect_rc(None)?;

    let data = UserData {
        data_callback,
        error_callback,
        sample_format,
        format: Default::default(),
        created_instance: Instant::now(),
        last_quantum,
    };
    let channels = config.channels as _;
    let rate = config.sample_rate as _;
    let stream = pw::stream::StreamRc::new(core, "cpal-playback", properties)?;
    let listener = stream
        .add_local_listener_with_user_data(data)
        .param_changed(move|stream, user_data, id, param| {
            let Some(param) = param else {
                return;
            };
            if id != pw::spa::param::ParamType::Format.as_raw() {
                return;
            }

            let (media_type, media_subtype) = match format_utils::parse_format(param) {
                Ok(v) => v,
                Err(_) => return,
            };

            // only accept raw audio
            if media_type != MediaType::Audio || media_subtype != MediaSubtype::Raw {
                return;
            }
            // call a helper function to parse the format for us.
            // When the format update, we check the format first, in case it does not fit what we
            // set
            if user_data.format.parse(param).is_ok() {
                let current_channels = user_data.format.channels();
                let current_rate = user_data.format.rate();
                if current_channels != channels || rate != current_rate {
                    (user_data.error_callback)(StreamError::BackendSpecific {
                        err: BackendSpecificError {
                            description: format!("channels or rate is not fit, current channels: {current_channels}, current rate: {current_rate}"),
                        },
                    });
                    // if the channels and rate do not match, we stop the stream
                    if let Err(e) = stream.set_active(false) {
                        (user_data.error_callback)(StreamError::BackendSpecific {
                            err: BackendSpecificError {
                                description: format!("failed to stop the stream, reason: {e}"),
                            },
                        });
                    }
                }

            }
        })
        .state_changed(|_stream, user_data, _old, new| {
            user_data.state_changed(new);
        })
        .process(|stream, user_data| match stream.dequeue_buffer() {
            None => (user_data.error_callback)(StreamError::BufferUnderrun),
            Some(mut buffer) => {
                // Read the requested frame count before mutably borrowing datas_mut().
                let requested = buffer.requested() as usize;
                let datas = buffer.datas_mut();
                if datas.is_empty() {
                    return;
                }
                let buf_data = &mut datas[0];
                let n_channels = user_data.format.channels();

                let stride = user_data.sample_format.sample_size() * n_channels as usize;
                // frames = samples / channels or frames = data_len / stride
                // Honor the frame count PipeWire requests this cycle, capped by the
                // mapped buffer capacity to guard against any mismatch.
                let frames = requested.min(buf_data.as_raw().maxsize as usize / stride);
                let Some(samples) = buf_data.data() else {
                    return;
                };

                // samples = frames * channels or samples = data_len / sample_size
                let n_samples = frames * n_channels as usize;

                // Pre-fill only the active region with silence before handing it to the callback.
                let active = &mut samples[..frames * stride];
                fill_with_equilibrium(active, user_data.sample_format);

                let data = active.as_mut_ptr() as *mut ();
                let mut data =
                    unsafe { Data::from_parts(data, n_samples, user_data.sample_format) };
                if let Err(err) = user_data.publish_data_out(stream, frames, &mut data) {
                    (user_data.error_callback)(StreamError::BackendSpecific { err });
                }
                let chunk = buf_data.chunk_mut();
                *chunk.offset_mut() = 0;
                *chunk.stride_mut() = stride as i32;
                *chunk.size_mut() = (frames * stride) as u32;
            }
        })
        .register()?;
    let mut audio_info = pw::spa::param::audio::AudioInfoRaw::new();
    audio_info.set_format(sample_format.into());
    audio_info.set_rate(rate);
    audio_info.set_channels(channels);

    let obj = pw::spa::pod::Object {
        type_: pw::spa::utils::SpaTypes::ObjectParamFormat.as_raw(),
        id: pw::spa::param::ParamType::EnumFormat.as_raw(),
        properties: audio_info.into(),
    };
    let values: Vec<u8> = pw::spa::pod::serialize::PodSerializer::serialize(
        std::io::Cursor::new(Vec::new()),
        &pw::spa::pod::Value::Object(obj),
    )
    .unwrap()
    .0
    .into_inner();

    let mut params = [Pod::from_bytes(&values).unwrap()];

    // TODO: what about RT_PROCESS?
    /* Now connect this stream. We ask that our process function is
     * called in a realtime thread. */
    stream.connect(
        pw::spa::utils::Direction::Output,
        None,
        pw::stream::StreamFlags::AUTOCONNECT | pw::stream::StreamFlags::MAP_BUFFERS,
        &mut params,
    )?;

    Ok(StreamData {
        mainloop,
        listener,
        stream,
        context,
    })
}
pub fn connect_input<D, E>(
    config: StreamConfig,
    properties: pw::properties::PropertiesBox,
    sample_format: SampleFormat,
    data_callback: D,
    error_callback: E,
    last_quantum: Arc<AtomicU64>,
) -> Result<StreamData<D, E>, pw::Error>
where
    D: FnMut(&Data, &InputCallbackInfo) + Send + 'static,
    E: FnMut(StreamError) + Send + 'static,
{
    pw::init();
    let mainloop = pw::main_loop::MainLoopRc::new(None)?;
    let context = pw::context::ContextRc::new(&mainloop, None)?;
    let core = context.connect_rc(None)?;

    let data = UserData {
        data_callback,
        error_callback,
        sample_format,
        format: Default::default(),
        created_instance: Instant::now(),
        last_quantum,
    };

    let channels = config.channels as _;
    let rate = config.sample_rate as _;

    let stream = pw::stream::StreamRc::new(core, "cpal-capture", properties)?;
    let listener = stream
        .add_local_listener_with_user_data(data)
        .param_changed(move |stream, user_data, id, param| {
            let Some(param) = param else {
                return;
            };
            if id != pw::spa::param::ParamType::Format.as_raw() {
                return;
            }

            let (media_type, media_subtype) = match format_utils::parse_format(param) {
                Ok(v) => v,
                Err(_) => return,
            };

            // only accept raw audio
            if media_type != MediaType::Audio || media_subtype != MediaSubtype::Raw {
                return;
            }

            // call a helper function to parse the format for us.
            // When the format update, we check the format first, in case it does not fit what we
            // set
            if user_data.format.parse(param).is_ok() {
                let current_channels = user_data.format.channels();
                let current_rate = user_data.format.rate();
                if current_channels != channels || rate != current_rate {
                    (user_data.error_callback)(StreamError::BackendSpecific {
                        err: BackendSpecificError {
                            description: format!("channels or rate is not fit, current channels: {current_channels}, current rate: {current_rate}"),
                        },
                    });
                    // if the channels and rate do not match, we stop the stream
                    if let Err(e) = stream.set_active(false) {
                        (user_data.error_callback)(StreamError::BackendSpecific {
                            err: BackendSpecificError {
                                description: format!("failed to stop the stream, reason: {e}"),
                            },
                        });
                    }
                }
            }
        })
        .state_changed(|_stream, user_data, _old, new| {
            user_data.state_changed(new);
        })
        .process(|stream, user_data| match stream.dequeue_buffer() {
            None => (user_data.error_callback)(StreamError::BufferUnderrun),
            Some(mut buffer) => {
                let datas = buffer.datas_mut();
                if datas.is_empty() {
                    return;
                }
                let data = &mut datas[0];
                let n_channels = user_data.format.channels();
                let n_samples = data.chunk().size() / user_data.sample_format.sample_size() as u32;
                let frames = n_samples / n_channels;

                let Some(samples) = data.data() else {
                    return;
                };
                let data = samples.as_mut_ptr() as *mut ();
                let data =
                    unsafe { Data::from_parts(data, n_samples as usize, user_data.sample_format) };
                if let Err(err) = user_data.publish_data_in(stream, frames as usize, &data) {
                    (user_data.error_callback)(StreamError::BackendSpecific { err });
                }
            }
        })
        .register()?;
    let mut audio_info = pw::spa::param::audio::AudioInfoRaw::new();
    audio_info.set_format(sample_format.into());
    audio_info.set_rate(rate);
    audio_info.set_channels(channels);

    let obj = pw::spa::pod::Object {
        type_: pw::spa::utils::SpaTypes::ObjectParamFormat.as_raw(),
        id: pw::spa::param::ParamType::EnumFormat.as_raw(),
        properties: audio_info.into(),
    };
    let values: Vec<u8> = pw::spa::pod::serialize::PodSerializer::serialize(
        std::io::Cursor::new(Vec::new()),
        &pw::spa::pod::Value::Object(obj),
    )
    .unwrap()
    .0
    .into_inner();

    let mut params = [Pod::from_bytes(&values).unwrap()];

    // TODO: what about RT_PROCESS?
    /* Now connect this stream. We ask that our process function is
     * called in a realtime thread. */
    stream.connect(
        pw::spa::utils::Direction::Input,
        None,
        pw::stream::StreamFlags::AUTOCONNECT | pw::stream::StreamFlags::MAP_BUFFERS,
        &mut params,
    )?;

    Ok(StreamData {
        mainloop,
        listener,
        stream,
        context,
    })
}
```

## File: `src/host/pipewire/utils.rs`
```rust
pub const METADATA_NAME: &str = "metadata.name";

// NOTE: the icon name contains bluetooth and etc, not icon-name, but icon_name
// I have tried to get the information, and get
// "device.icon-name": "audio-card-analog",
// "device.icon_name": "video-display",
// So seems the `icon_name` is usable
pub const DEVICE_ICON_NAME: &str = "device.icon_name";

pub mod clock {
    pub const RATE: &str = "clock.rate";
    pub const ALLOWED_RATES: &str = "clock.allowed-rates";
    pub const QUANTUM: &str = "clock.quantum";
    pub const MIN_QUANTUM: &str = "clock.min-quantum";
    pub const MAX_QUANTUM: &str = "clock.max-quantum";
}

pub mod audio {
    pub const SINK: &str = "Audio/Sink";
    pub const SOURCE: &str = "Audio/Source";
    pub const DUPLEX: &str = "Audio/Duplex";
    pub const STREAM_OUTPUT: &str = "Stream/Output/Audio";
    pub const STREAM_INPUT: &str = "Stream/Input/Audio";
}
```

## File: `src/host/pulseaudio/mod.rs`
```rust
use futures::executor::block_on;
use pulseaudio::protocol;

mod stream;

pub use stream::Stream;

use crate::{
    traits::{DeviceTrait, HostTrait},
    BackendSpecificError, BuildStreamError, Data, DefaultStreamConfigError, DeviceDescription,
    DeviceDescriptionBuilder, DeviceDirection, DeviceId, DeviceIdError, DeviceNameError,
    DevicesError, FrameCount, HostId, HostUnavailable, InputCallbackInfo, OutputCallbackInfo,
    SampleFormat, StreamConfig, StreamError, SupportedBufferSize, SupportedStreamConfig,
    SupportedStreamConfigRange, SupportedStreamConfigsError,
};

const PULSE_FORMATS: &[SampleFormat] = &[
    SampleFormat::U8,
    SampleFormat::I16,
    SampleFormat::I24,
    SampleFormat::I32,
    SampleFormat::F32,
];

impl TryFrom<protocol::SampleFormat> for SampleFormat {
    type Error = ();

    fn try_from(spec: protocol::SampleFormat) -> Result<Self, Self::Error> {
        match spec {
            protocol::SampleFormat::U8 => Ok(SampleFormat::U8),
            protocol::SampleFormat::S16Le | protocol::SampleFormat::S16Be => Ok(SampleFormat::I16),
            protocol::SampleFormat::S24Le | protocol::SampleFormat::S24Be => Ok(SampleFormat::I24),
            protocol::SampleFormat::S32Le | protocol::SampleFormat::S32Be => Ok(SampleFormat::I32),
            protocol::SampleFormat::Float32Le | protocol::SampleFormat::Float32Be => {
                Ok(SampleFormat::F32)
            }
            _ => Err(()),
        }
    }
}

impl TryFrom<SampleFormat> for protocol::SampleFormat {
    type Error = ();

    fn try_from(format: SampleFormat) -> Result<Self, Self::Error> {
        match (format, cfg!(target_endian = "little")) {
            (SampleFormat::U8, _) => Ok(protocol::SampleFormat::U8),
            (SampleFormat::I16, true) => Ok(protocol::SampleFormat::S16Le),
            (SampleFormat::I16, false) => Ok(protocol::SampleFormat::S16Be),
            (SampleFormat::I24, true) => Ok(protocol::SampleFormat::S24Le),
            (SampleFormat::I24, false) => Ok(protocol::SampleFormat::S24Be),
            (SampleFormat::I32, true) => Ok(protocol::SampleFormat::S32Le),
            (SampleFormat::I32, false) => Ok(protocol::SampleFormat::S32Be),
            (SampleFormat::F32, true) => Ok(protocol::SampleFormat::Float32Le),
            (SampleFormat::F32, false) => Ok(protocol::SampleFormat::Float32Be),
            _ => Err(()),
        }
    }
}

impl From<pulseaudio::ClientError> for BackendSpecificError {
    fn from(err: pulseaudio::ClientError) -> Self {
        BackendSpecificError {
            description: err.to_string(),
        }
    }
}

/// A Host for connecting to the popular PulseAudio and PipeWire (via
/// pipewire-pulse) audio servers on linux.
pub struct Host {
    client: pulseaudio::Client,
}

impl Host {
    pub fn new() -> Result<Self, HostUnavailable> {
        let client =
            pulseaudio::Client::from_env(c"cpal-pulseaudio").map_err(|_| HostUnavailable)?;

        Ok(Self { client })
    }
}

impl HostTrait for Host {
    type Devices = std::vec::IntoIter<Device>;
    type Device = Device;

    fn is_available() -> bool {
        pulseaudio::socket_path_from_env().is_some()
    }

    fn devices(&self) -> Result<Self::Devices, DevicesError> {
        let sinks = block_on(self.client.list_sinks()).map_err(|err| BackendSpecificError {
            description: format!("Failed to list sinks: {err}"),
        })?;

        let sources = block_on(self.client.list_sources()).map_err(|err| BackendSpecificError {
            description: format!("Failed to list sources: {err}"),
        })?;

        Ok(sinks
            .into_iter()
            .map(|sink_info| Device::Sink {
                client: self.client.clone(),
                info: sink_info,
            })
            .chain(sources.into_iter().map(|source_info| Device::Source {
                client: self.client.clone(),
                info: source_info,
            }))
            .collect::<Vec<_>>()
            .into_iter())
    }

    fn default_input_device(&self) -> Option<Self::Device> {
        let source_info = block_on(
            self.client
                .source_info_by_name(protocol::DEFAULT_SOURCE.to_owned()),
        )
        .ok()?;

        Some(Device::Source {
            client: self.client.clone(),
            info: source_info,
        })
    }

    fn default_output_device(&self) -> Option<Self::Device> {
        let sink_info = block_on(
            self.client
                .sink_info_by_name(protocol::DEFAULT_SINK.to_owned()),
        )
        .ok()?;

        Some(Device::Sink {
            client: self.client.clone(),
            info: sink_info,
        })
    }
}

/// A PulseAudio sink or source.
#[derive(Debug, Clone)]
pub enum Device {
    Sink {
        client: pulseaudio::Client,
        info: protocol::SinkInfo,
    },
    Source {
        client: pulseaudio::Client,
        info: protocol::SourceInfo,
    },
}

fn supported_config_ranges() -> Vec<SupportedStreamConfigRange> {
    let mut ranges = vec![];
    for format in PULSE_FORMATS {
        for channel_count in 1..protocol::sample_spec::MAX_CHANNELS {
            let bytes_per_frame = channel_count as usize * format.sample_size();
            let max_frames = (protocol::MAX_MEMBLOCKQ_LENGTH / bytes_per_frame) as FrameCount;
            ranges.push(SupportedStreamConfigRange {
                channels: channel_count as _,
                min_sample_rate: 1,
                max_sample_rate: protocol::sample_spec::MAX_RATE,
                buffer_size: SupportedBufferSize::Range {
                    min: 0,
                    max: max_frames,
                },
                sample_format: *format,
            });
        }
    }
    ranges
}

fn default_config_from_spec(
    sample_spec: &protocol::SampleSpec,
    channel_map: &protocol::ChannelMap,
) -> Result<SupportedStreamConfig, DefaultStreamConfigError> {
    let sample_format: SampleFormat = sample_spec
        .format
        .try_into()
        .map_err(|_| DefaultStreamConfigError::StreamTypeNotSupported)?;
    let bytes_per_frame = channel_map.num_channels() as usize * sample_format.sample_size();
    let max_frames = (protocol::MAX_MEMBLOCKQ_LENGTH / bytes_per_frame) as u32;
    Ok(SupportedStreamConfig {
        channels: channel_map.num_channels() as _,
        sample_rate: sample_spec.sample_rate,
        buffer_size: SupportedBufferSize::Range {
            min: 0,
            max: max_frames,
        },
        sample_format,
    })
}

impl DeviceTrait for Device {
    type SupportedInputConfigs = std::vec::IntoIter<SupportedStreamConfigRange>;
    type SupportedOutputConfigs = std::vec::IntoIter<SupportedStreamConfigRange>;
    type Stream = Stream;

    fn name(&self) -> Result<String, DeviceNameError> {
        let name = match self {
            Device::Sink { info, .. } => &info.name,
            Device::Source { info, .. } => &info.name,
        };

        Ok(String::from_utf8_lossy(name.as_bytes()).into_owned())
    }

    fn supported_input_configs(
        &self,
    ) -> Result<Self::SupportedInputConfigs, SupportedStreamConfigsError> {
        let Device::Source { .. } = self else {
            return Ok(vec![].into_iter());
        };
        Ok(supported_config_ranges().into_iter())
    }

    fn supported_output_configs(
        &self,
    ) -> Result<Self::SupportedOutputConfigs, SupportedStreamConfigsError> {
        let Device::Sink { .. } = self else {
            return Ok(vec![].into_iter());
        };
        Ok(supported_config_ranges().into_iter())
    }

    fn default_input_config(&self) -> Result<SupportedStreamConfig, DefaultStreamConfigError> {
        let Device::Source { info, .. } = self else {
            return Err(DefaultStreamConfigError::StreamTypeNotSupported);
        };
        default_config_from_spec(&info.sample_spec, &info.channel_map)
    }

    fn default_output_config(&self) -> Result<SupportedStreamConfig, DefaultStreamConfigError> {
        let Device::Sink { info, .. } = self else {
            return Err(DefaultStreamConfigError::StreamTypeNotSupported);
        };
        default_config_from_spec(&info.sample_spec, &info.channel_map)
    }

    fn build_input_stream_raw<D, E>(
        &self,
        config: StreamConfig,
        sample_format: SampleFormat,
        data_callback: D,
        error_callback: E,
        _timeout: Option<std::time::Duration>,
    ) -> Result<Self::Stream, BuildStreamError>
    where
        D: FnMut(&Data, &InputCallbackInfo) + Send + 'static,
        E: FnMut(StreamError) + Send + 'static,
    {
        let Device::Source { client, info } = self else {
            return Err(BuildStreamError::StreamConfigNotSupported);
        };

        let format: protocol::SampleFormat = sample_format
            .try_into()
            .map_err(|_| BuildStreamError::StreamConfigNotSupported)?;

        let sample_spec = make_sample_spec(config, format);
        let channel_map = make_channel_map(config);
        let buffer_attr = make_record_buffer_attr(config, format);
        let adjust_latency = matches!(config.buffer_size, crate::BufferSize::Fixed(_));

        let params = protocol::RecordStreamParams {
            sample_spec,
            channel_map,
            source_index: Some(info.index),
            buffer_attr,
            flags: protocol::stream::StreamFlags {
                // Start the stream suspended.
                start_corked: true,
                // When a fixed buffer size is requested, ask PA to configure
                // the source hardware to hit the requested latency end-to-end.
                adjust_latency,
                ..Default::default()
            },
            ..Default::default()
        };

        stream::Stream::new_record(client.clone(), params, data_callback, error_callback)
    }

    fn build_output_stream_raw<D, E>(
        &self,
        config: StreamConfig,
        sample_format: SampleFormat,
        data_callback: D,
        error_callback: E,
        _timeout: Option<std::time::Duration>,
    ) -> Result<Self::Stream, BuildStreamError>
    where
        D: FnMut(&mut Data, &OutputCallbackInfo) + Send + 'static,
        E: FnMut(StreamError) + Send + 'static,
    {
        let Device::Sink { client, info } = self else {
            return Err(BuildStreamError::StreamConfigNotSupported);
        };

        let format: protocol::SampleFormat = sample_format
            .try_into()
            .map_err(|_| BuildStreamError::StreamConfigNotSupported)?;

        let sample_spec = make_sample_spec(config, format);
        let channel_map = make_channel_map(config);
        let buffer_attr = make_playback_buffer_attr(config, format);
        let adjust_latency = matches!(config.buffer_size, crate::BufferSize::Fixed(_));

        let params = protocol::PlaybackStreamParams {
            sink_index: Some(info.index),
            sample_spec,
            channel_map,
            buffer_attr,
            flags: protocol::stream::StreamFlags {
                // Start the stream suspended.
                start_corked: true,
                // When a fixed buffer size is requested, ask PA to configure
                // the sink hardware to hit the requested latency end-to-end.
                adjust_latency,
                ..Default::default()
            },
            ..Default::default()
        };

        stream::Stream::new_playback(client.clone(), params, data_callback, error_callback)
    }

    fn description(&self) -> Result<DeviceDescription, DeviceNameError> {
        let (name, description, direction) = match self {
            Device::Sink { info, .. } => (&info.name, &info.description, DeviceDirection::Output),
            Device::Source { info, .. } => (&info.name, &info.description, DeviceDirection::Input),
        };

        let mut builder = DeviceDescriptionBuilder::new(String::from_utf8_lossy(name.as_bytes()))
            .direction(direction);
        if let Some(desc) = description {
            builder = builder.add_extended_line(String::from_utf8_lossy(desc.as_bytes()));
        }

        Ok(builder.build())
    }

    fn id(&self) -> Result<DeviceId, DeviceIdError> {
        let id = match self {
            Device::Sink { info, .. } => info.index,
            Device::Source { info, .. } => info.index,
        };

        Ok(DeviceId(HostId::PulseAudio, id.to_string()))
    }
}

fn make_sample_spec(config: StreamConfig, format: protocol::SampleFormat) -> protocol::SampleSpec {
    protocol::SampleSpec {
        format,
        sample_rate: config.sample_rate,
        channels: config.channels as _,
    }
}

fn make_channel_map(config: StreamConfig) -> protocol::ChannelMap {
    use protocol::ChannelPosition::*;

    // Standard channel layouts following the PulseAudio default channel map
    // (PA_CHANNEL_MAP_DEFAULT) for 1-8 channels, and common Atmos height-
    // channel conventions for 10 and 12 channels. Counts without a widely
    // agreed layout (9, 11, >12) fall back to sequential Aux positions.
    let standard: &[protocol::ChannelPosition] = match config.channels {
        1 => &[Mono],
        2 => &[FrontLeft, FrontRight],
        3 => &[FrontLeft, FrontRight, FrontCenter],
        4 => &[FrontLeft, FrontRight, RearLeft, RearRight],
        5 => &[FrontLeft, FrontRight, FrontCenter, RearLeft, RearRight],
        6 => &[FrontLeft, FrontRight, FrontCenter, Lfe, RearLeft, RearRight],
        7 => &[
            FrontLeft,
            FrontRight,
            FrontCenter,
            Lfe,
            RearLeft,
            RearRight,
            RearCenter,
        ],
        8 => &[
            FrontLeft,
            FrontRight,
            FrontCenter,
            Lfe,
            RearLeft,
            RearRight,
            SideLeft,
            SideRight,
        ],
        // 7.1.2 (Dolby Atmos): 7.1 + top-front L/R
        10 => &[
            FrontLeft,
            FrontRight,
            FrontCenter,
            Lfe,
            RearLeft,
            RearRight,
            SideLeft,
            SideRight,
            TopFrontLeft,
            TopFrontRight,
        ],
        // 7.1.4 (Dolby Atmos): 7.1 + top-front L/R + top-rear L/R
        12 => &[
            FrontLeft,
            FrontRight,
            FrontCenter,
            Lfe,
            RearLeft,
            RearRight,
            SideLeft,
            SideRight,
            TopFrontLeft,
            TopFrontRight,
            TopRearLeft,
            TopRearRight,
        ],
        _ => &[],
    };

    if !standard.is_empty() {
        return protocol::ChannelMap::new(standard.iter().copied());
    }

    let aux = [
        Aux0, Aux1, Aux2, Aux3, Aux4, Aux5, Aux6, Aux7, Aux8, Aux9, Aux10, Aux11, Aux12, Aux13,
        Aux14, Aux15, Aux16, Aux17, Aux18, Aux19, Aux20, Aux21, Aux22, Aux23, Aux24, Aux25, Aux26,
        Aux27, Aux28, Aux29, Aux30, Aux31,
    ];
    protocol::ChannelMap::new(aux.iter().copied().take(config.channels as usize))
}

fn make_playback_buffer_attr(
    config: StreamConfig,
    format: protocol::SampleFormat,
) -> protocol::stream::BufferAttr {
    match config.buffer_size {
        crate::BufferSize::Default => Default::default(),
        crate::BufferSize::Fixed(frame_count) => {
            let len = frame_count * config.channels as u32 * format.bytes_per_sample() as u32;
            protocol::stream::BufferAttr {
                // Double-buffer: total buffer = 2 callback periods. With
                // adjust_latency this becomes the end-to-end latency target,
                // Minimum request = one callback period, ensuring the server
                // always asks for exactly frame_count frames per call.
                max_length: 2 * len,
                target_length: 2 * len,
                minimum_request_length: len,
                ..Default::default()
            }
        }
    }
}

fn make_record_buffer_attr(
    config: StreamConfig,
    format: protocol::SampleFormat,
) -> protocol::stream::BufferAttr {
    match config.buffer_size {
        crate::BufferSize::Default => Default::default(),
        crate::BufferSize::Fixed(frame_count) => {
            let len = frame_count * config.channels as u32 * format.bytes_per_sample() as u32;
            protocol::stream::BufferAttr {
                // fragment_size controls the delivery chunk size for record
                // streams; target_length is playback-only and is ignored here.
                max_length: len,
                fragment_size: len,
                ..Default::default()
            }
        }
    }
}
```

## File: `src/host/pulseaudio/stream.rs`
```rust
use std::{
    sync::{
        atomic::{self, AtomicU64},
        Arc, Mutex,
    },
    time::{Duration, Instant},
};

use futures::executor::block_on;
use pulseaudio::{protocol, AsPlaybackSource};

use crate::{
    traits::StreamTrait, BackendSpecificError, BuildStreamError, Data, FrameCount,
    InputCallbackInfo, InputStreamTimestamp, OutputCallbackInfo, OutputStreamTimestamp,
    PlayStreamError, SampleFormat, StreamError, StreamInstant,
};

const LATENCY_POLL_INTERVAL: Duration = Duration::from_millis(5);

pub enum Stream {
    Playback(pulseaudio::PlaybackStream),
    Record(pulseaudio::RecordStream),
}

impl StreamTrait for Stream {
    fn play(&self) -> Result<(), PlayStreamError> {
        match self {
            Stream::Playback(stream) => {
                block_on(stream.uncork()).map_err(Into::<BackendSpecificError>::into)?;
            }
            Stream::Record(stream) => {
                block_on(stream.uncork()).map_err(Into::<BackendSpecificError>::into)?;
                block_on(stream.started()).map_err(Into::<BackendSpecificError>::into)?;
            }
        };

        Ok(())
    }

    fn pause(&self) -> Result<(), crate::PauseStreamError> {
        let res = match self {
            Stream::Playback(stream) => block_on(stream.cork()),
            Stream::Record(stream) => block_on(stream.cork()),
        };

        res.map_err(Into::<BackendSpecificError>::into)?;
        Ok(())
    }

    fn buffer_size(&self) -> Option<FrameCount> {
        let (spec, bytes) = match self {
            Stream::Playback(s) => (
                s.sample_spec(),
                s.buffer_attr().minimum_request_length as usize,
            ),
            Stream::Record(s) => (s.sample_spec(), s.buffer_attr().fragment_size as usize),
        };
        let frame_size = spec.channels as usize * spec.format.bytes_per_sample();
        if bytes > 0 {
            Some((bytes / frame_size) as _)
        } else {
            None
        }
    }
}

impl Stream {
    pub fn new_playback<D, E>(
        client: pulseaudio::Client,
        params: protocol::PlaybackStreamParams,
        mut data_callback: D,
        error_callback: E,
    ) -> Result<Self, BuildStreamError>
    where
        D: FnMut(&mut Data, &OutputCallbackInfo) + Send + 'static,
        E: FnMut(StreamError) + Send + 'static,
    {
        // Use a monotonic clock relative to stream creation for StreamInstants.
        let start = std::time::Instant::now();

        let current_latency_micros = Arc::new(AtomicU64::new(0));
        // Microseconds since stream creation at the time of the last latency poll, used
        // to interpolate the latency between polls.
        let last_poll_micros = Arc::new(AtomicU64::new(0));
        let latency_clone = current_latency_micros.clone();
        let poll_clone = last_poll_micros.clone();
        let sample_spec = params.sample_spec;

        let format: SampleFormat = sample_spec
            .format
            .try_into()
            .map_err(|_| BuildStreamError::StreamConfigNotSupported)?;

        // Silence for unsigned formats is the midpoint, not zero. Among
        // PulseAudio's supported formats, only U8 is unsigned and has a
        // single-byte repeatable silence representation (0x80). Multi-byte
        // unsigned formats (U16, U32, ...) are not currently supported.
        let silence_byte = if format == SampleFormat::U8 {
            0x80u8
        } else {
            0u8
        };

        // Wrap the write callback to match the pulseaudio signature.
        let callback = move |buf: &mut [u8]| {
            let elapsed = Instant::now().saturating_duration_since(start);
            let elapsed_usec = elapsed.as_micros() as u64;

            // Interpolate the latency based on elapsed time since the last
            // poll: as audio plays, the DAC drains the buffer at a constant
            // rate, so the latency decreases linearly between polls.
            let stored_latency = latency_clone.load(atomic::Ordering::Relaxed);
            let poll_usec = poll_clone.load(atomic::Ordering::Relaxed);
            // Cap to one poll interval: the linear-drain assumption is only valid
            // for that window, and a stale poll_usec (e.g. after cork/uncork where
            // timing_info blocks) would otherwise saturate latency to zero.
            let elapsed_since_poll = elapsed_usec
                .saturating_sub(poll_usec)
                .min(LATENCY_POLL_INTERVAL.as_micros() as u64);
            let latency = stored_latency.saturating_sub(elapsed_since_poll);

            let playback_time = elapsed + Duration::from_micros(latency);

            let timestamp = OutputStreamTimestamp {
                callback: StreamInstant {
                    secs: elapsed.as_secs() as i64,
                    nanos: elapsed.subsec_nanos(),
                },
                playback: StreamInstant {
                    secs: playback_time.as_secs() as i64,
                    nanos: playback_time.subsec_nanos(),
                },
            };

            // Preemptively fill the buffer with silence in case the user
            // callback doesn't fill it completely (cpal's API doesn't allow
            // short writes).
            buf.fill(silence_byte);

            let bps = sample_spec.format.bytes_per_sample();
            let n_samples = buf.len() / bps;

            // SAFETY: we calculated the number of samples based on
            // `sample_spec.format`, and `format` is directly derived from (and
            // equivalent to) `sample_spec.format`.
            let mut data = unsafe { Data::from_parts(buf.as_mut_ptr().cast(), n_samples, format) };

            data_callback(&mut data, &OutputCallbackInfo { timestamp });

            // We always consider the full buffer filled, because cpal's
            // user-facing API doesn't allow short writes.
            buf.len()
        };

        let stream = block_on(client.create_playback_stream(params, callback.as_playback_source()))
            .map_err(Into::<BackendSpecificError>::into)?;

        // Share the error callback between the worker and latency threads so
        // both can surface errors to the user.
        let error_callback = Arc::new(Mutex::new(error_callback));

        // Spawn a thread to drive the stream future. It will exit automatically
        // when the stream is stopped by the user.
        let stream_clone = stream.clone();
        let error_callback_clone = error_callback.clone();
        std::thread::spawn(move || {
            if let Err(e) = block_on(stream_clone.play_all()) {
                error_callback_clone.lock().unwrap()(StreamError::from(BackendSpecificError {
                    description: e.to_string(),
                }));
            }
        });

        // Spawn a thread to monitor the stream's latency in a loop. It will
        // exit automatically when the stream ends.
        let stream_clone = stream.clone();
        let latency_clone = current_latency_micros.clone();
        let poll_clone = last_poll_micros.clone();
        std::thread::spawn(move || loop {
            let timing_info = match block_on(stream_clone.timing_info()) {
                Ok(timing_info) => timing_info,
                Err(e) => {
                    error_callback.lock().unwrap()(StreamError::from(BackendSpecificError {
                        description: e.to_string(),
                    }));
                    break;
                }
            };

            let poll_since_epoch =
                Instant::now().saturating_duration_since(start).as_micros() as u64;
            poll_clone.store(poll_since_epoch, atomic::Ordering::Relaxed);

            store_latency(
                &latency_clone,
                sample_spec,
                timing_info.sink_usec,
                timing_info.write_offset,
                timing_info.read_offset,
            );

            std::thread::sleep(LATENCY_POLL_INTERVAL);
        });

        Ok(Self::Playback(stream))
    }

    pub fn new_record<D, E>(
        client: pulseaudio::Client,
        params: protocol::RecordStreamParams,
        mut data_callback: D,
        mut error_callback: E,
    ) -> Result<Self, BuildStreamError>
    where
        D: FnMut(&Data, &InputCallbackInfo) + Send + 'static,
        E: FnMut(StreamError) + Send + 'static,
    {
        let start = Instant::now();

        let current_latency_micros = Arc::new(AtomicU64::new(0));
        let latency_clone = current_latency_micros.clone();
        let sample_spec = params.sample_spec;

        let format: SampleFormat = sample_spec
            .format
            .try_into()
            .map_err(|_| BuildStreamError::StreamConfigNotSupported)?;

        let callback = move |buf: &[u8]| {
            let elapsed = Instant::now().saturating_duration_since(start);
            let latency = latency_clone.load(atomic::Ordering::Relaxed);
            let capture_time = elapsed
                .checked_sub(Duration::from_micros(latency))
                .unwrap_or_default();

            let timestamp = InputStreamTimestamp {
                callback: StreamInstant {
                    secs: elapsed.as_secs() as i64,
                    nanos: elapsed.subsec_nanos(),
                },
                capture: StreamInstant {
                    secs: capture_time.as_secs() as i64,
                    nanos: capture_time.subsec_nanos(),
                },
            };

            let bps = sample_spec.format.bytes_per_sample();
            let n_samples = buf.len() / bps;

            // SAFETY: we calculated the number of samples based on
            // `sample_spec.format`, and `format` is directly derived from (and
            // equivalent to) `sample_spec.format`. The pointer is cast from
            // *const to *mut, but cpal's Data type for input streams only
            // exposes shared references (&[T]), so no mutation occurs.
            let data = unsafe { Data::from_parts(buf.as_ptr() as *mut _, n_samples, format) };

            data_callback(&data, &InputCallbackInfo { timestamp });
        };

        let stream = block_on(client.create_record_stream(params, callback))
            .map_err(Into::<BackendSpecificError>::into)?;

        // Spawn a thread to monitor the stream's latency in a loop. It will
        // exit automatically when the stream ends.
        let stream_clone = stream.clone();
        let latency_clone = current_latency_micros.clone();
        std::thread::spawn(move || loop {
            let timing_info = match block_on(stream_clone.timing_info()) {
                Ok(timing_info) => timing_info,
                Err(e) => {
                    error_callback(StreamError::from(BackendSpecificError {
                        description: e.to_string(),
                    }));
                    break;
                }
            };

            store_latency(
                &latency_clone,
                sample_spec,
                timing_info.source_usec,
                timing_info.write_offset,
                timing_info.read_offset,
            );

            std::thread::sleep(LATENCY_POLL_INTERVAL);
        });

        Ok(Self::Record(stream))
    }
}

fn store_latency(
    latency_micros: &AtomicU64,
    sample_spec: protocol::SampleSpec,
    device_latency_usec: u64,
    write_offset: i64,
    read_offset: i64,
) {
    let offset = (write_offset - read_offset).max(0) as u64;

    let latency =
        Duration::from_micros(device_latency_usec) + sample_spec.bytes_to_duration(offset as usize);

    latency_micros.store(
        latency.as_micros().try_into().unwrap_or(u64::MAX),
        atomic::Ordering::Relaxed,
    );
}
```

## File: `src/host/wasapi/device.rs`
```rust
use crate::{
    BackendSpecificError, BufferSize, Data, DefaultStreamConfigError, DeviceDescription,
    DeviceDescriptionBuilder, DeviceDirection, DeviceId, DeviceIdError, DeviceNameError,
    DeviceType, DevicesError, FrameCount, InputCallbackInfo, InterfaceType, OutputCallbackInfo,
    SampleFormat, SampleRate, StreamConfig, SupportedBufferSize, SupportedStreamConfig,
    SupportedStreamConfigRange, SupportedStreamConfigsError, COMMON_SAMPLE_RATES,
};

impl From<Audio::EDataFlow> for DeviceDirection {
    fn from(data_flow: Audio::EDataFlow) -> Self {
        if data_flow == Audio::eCapture {
            DeviceDirection::Input
        } else if data_flow == Audio::eRender {
            DeviceDirection::Output
        } else {
            DeviceDirection::Unknown
        }
    }
}
use std::ffi::OsString;
use std::fmt;
use std::mem;
use std::os::windows::ffi::OsStringExt;
use std::ptr;
use std::slice;
use std::sync::OnceLock;
use std::sync::{Arc, Mutex, MutexGuard};
use std::time::Duration;

use super::{windows_err_to_cpal_err, windows_err_to_cpal_err_message};
use crate::host::com;
use windows::core::Interface;
use windows::core::GUID;
use windows::Win32::Devices::Properties;
use windows::Win32::Foundation::PROPERTYKEY;
use windows::Win32::Media::Audio::IAudioRenderClient;
use windows::Win32::Media::{Audio, KernelStreaming, Multimedia};
use windows::Win32::System::Com;
use windows::Win32::System::Com::{StructuredStorage, STGM_READ};
use windows::Win32::System::Threading;
use windows::Win32::System::Variant::{VT_LPWSTR, VT_UI4};
use windows::Win32::UI::Shell::PropertiesSystem::IPropertyStore;

use super::stream::{AudioClientFlow, Stream, StreamInner};
use crate::{traits::DeviceTrait, BuildStreamError, StreamError};

pub use crate::iter::{SupportedInputConfigs, SupportedOutputConfigs};

// PKEY_AudioEndpoint properties not yet in windows-rs

/// PKEY_AudioEndpoint_FormFactor (PID 0) - VT_UI4 containing EndpointFormFactor enum
const PKEY_AUDIOENDPOINT_FORMFACTOR: PROPERTYKEY = PROPERTYKEY {
    fmtid: GUID::from_u128(0x1da5d803_d492_4edd_8c23_e0c0ffee7f0e),
    pid: 0,
};

/// PKEY_AudioEndpoint_JackSubType (PID 8) - VT_LPWSTR containing KS node type GUID
const PKEY_AUDIOENDPOINT_JACKSUBTYPE: PROPERTYKEY = PROPERTYKEY {
    fmtid: GUID::from_u128(0x1da5d803_d492_4edd_8c23_e0c0ffee7f0e),
    pid: 8,
};

const DEFAULT_FLAGS: u32 = Audio::AUDCLNT_STREAMFLAGS_EVENTCALLBACK
    | Audio::AUDCLNT_STREAMFLAGS_SRC_DEFAULT_QUALITY
    | Audio::AUDCLNT_STREAMFLAGS_AUTOCONVERTPCM;

/// Wrapper because of that stupid decision to remove `Send` and `Sync` from raw pointers.
#[derive(Clone)]
struct IAudioClientWrapper(Audio::IAudioClient);
unsafe impl Send for IAudioClientWrapper {}
unsafe impl Sync for IAudioClientWrapper {}

/// An opaque type that identifies an end point.
#[derive(Clone)]
pub struct Device {
    device: Audio::IMMDevice,
    /// We cache an uninitialized `IAudioClient` so that we can call functions from it without
    /// having to create/destroy audio clients all the time.
    future_audio_client: Arc<Mutex<Option<IAudioClientWrapper>>>, // TODO: add NonZero around the ptr
}

impl DeviceTrait for Device {
    type SupportedInputConfigs = SupportedInputConfigs;
    type SupportedOutputConfigs = SupportedOutputConfigs;
    type Stream = Stream;

    fn description(&self) -> Result<DeviceDescription, DeviceNameError> {
        Device::description(self)
    }

    fn id(&self) -> Result<DeviceId, DeviceIdError> {
        Device::id(self)
    }

    fn supports_input(&self) -> bool {
        self.data_flow() == Audio::eCapture
    }

    fn supports_output(&self) -> bool {
        self.data_flow() == Audio::eRender
    }

    fn supported_input_configs(
        &self,
    ) -> Result<Self::SupportedInputConfigs, SupportedStreamConfigsError> {
        Device::supported_input_configs(self)
    }

    fn supported_output_configs(
        &self,
    ) -> Result<Self::SupportedOutputConfigs, SupportedStreamConfigsError> {
        Device::supported_output_configs(self)
    }

    fn default_input_config(&self) -> Result<SupportedStreamConfig, DefaultStreamConfigError> {
        Device::default_input_config(self)
    }

    fn default_output_config(&self) -> Result<SupportedStreamConfig, DefaultStreamConfigError> {
        Device::default_output_config(self)
    }

    fn build_input_stream_raw<D, E>(
        &self,
        config: StreamConfig,
        sample_format: SampleFormat,
        data_callback: D,
        error_callback: E,
        _timeout: Option<Duration>,
    ) -> Result<Self::Stream, BuildStreamError>
    where
        D: FnMut(&Data, &InputCallbackInfo) + Send + 'static,
        E: FnMut(StreamError) + Send + 'static,
    {
        let stream_inner = self.build_input_stream_raw_inner(config, sample_format)?;
        Ok(Stream::new_input(
            stream_inner,
            data_callback,
            error_callback,
        ))
    }

    fn build_output_stream_raw<D, E>(
        &self,
        config: StreamConfig,
        sample_format: SampleFormat,
        data_callback: D,
        error_callback: E,
        _timeout: Option<Duration>,
    ) -> Result<Self::Stream, BuildStreamError>
    where
        D: FnMut(&mut Data, &OutputCallbackInfo) + Send + 'static,
        E: FnMut(StreamError) + Send + 'static,
    {
        let stream_inner = self.build_output_stream_raw_inner(config, sample_format)?;
        Ok(Stream::new_output(
            stream_inner,
            data_callback,
            error_callback,
        ))
    }
}

struct Endpoint {
    endpoint: Audio::IMMEndpoint,
}

// Use RAII to make sure CoTaskMemFree is called when we are responsible for freeing.
struct WaveFormatExPtr(*mut Audio::WAVEFORMATEX);

impl Drop for WaveFormatExPtr {
    fn drop(&mut self) {
        unsafe {
            Com::CoTaskMemFree(Some(self.0 as *mut _));
        }
    }
}

unsafe fn immendpoint_from_immdevice(device: Audio::IMMDevice) -> Audio::IMMEndpoint {
    device
        .cast::<Audio::IMMEndpoint>()
        .expect("could not query IMMDevice interface for IMMEndpoint")
}

unsafe fn data_flow_from_immendpoint(endpoint: &Audio::IMMEndpoint) -> Audio::EDataFlow {
    endpoint
        .GetDataFlow()
        .expect("could not get endpoint data_flow")
}

// Given the audio client and format, returns whether or not the format is supported.
pub unsafe fn is_format_supported(
    _client: &Audio::IAudioClient,
    _waveformatex_ptr: *const Audio::WAVEFORMATEX,
) -> Result<bool, SupportedStreamConfigsError> {
    // Checking formats is not needed for shared mode with auto-conversion, therefore this check has been removed until someone implements WASAPI exclusive mode support
    // I used an NAudio issue as reference: https://github.com/naudio/NAudio/issues/819

    Ok(true)
}

// Get a cpal Format from a WAVEFORMATEX.
unsafe fn format_from_waveformatex_ptr(
    waveformatex_ptr: *const Audio::WAVEFORMATEX,
    audio_client: &Audio::IAudioClient,
) -> Option<SupportedStreamConfig> {
    fn cmp_guid(a: &GUID, b: &GUID) -> bool {
        (a.data1, a.data2, a.data3, a.data4) == (b.data1, b.data2, b.data3, b.data4)
    }
    let sample_format = match (
        (*waveformatex_ptr).wBitsPerSample,
        (*waveformatex_ptr).wFormatTag as u32,
    ) {
        (8, Audio::WAVE_FORMAT_PCM) => SampleFormat::U8,
        (16, Audio::WAVE_FORMAT_PCM) => SampleFormat::I16,
        (32, Multimedia::WAVE_FORMAT_IEEE_FLOAT) => SampleFormat::F32,
        (n_bits, KernelStreaming::WAVE_FORMAT_EXTENSIBLE) => {
            let waveformatextensible_ptr = waveformatex_ptr as *const Audio::WAVEFORMATEXTENSIBLE;
            let sub = (*waveformatextensible_ptr).SubFormat;

            if cmp_guid(&sub, &KernelStreaming::KSDATAFORMAT_SUBTYPE_PCM) {
                match n_bits {
                    8 => SampleFormat::U8,
                    16 => SampleFormat::I16,
                    24 => SampleFormat::I24,
                    32 => SampleFormat::I32,
                    64 => SampleFormat::I64,
                    _ => return None,
                }
            } else if n_bits == 32 && cmp_guid(&sub, &Multimedia::KSDATAFORMAT_SUBTYPE_IEEE_FLOAT) {
                SampleFormat::F32
            } else {
                return None;
            }
        }
        // Unknown data format returned by GetMixFormat.
        _ => return None,
    };

    let sample_rate = (*waveformatex_ptr).nSamplesPerSec;

    // GetBufferSizeLimits is only used for Hardware-Offloaded Audio
    // Processing, which was added in Windows 8, which places hardware
    // limits on the size of the audio buffer. If the sound system
    // *isn't* using offloaded audio, we're using a software audio
    // processing stack and have pretty much free rein to set buffer
    // size.
    //
    // In software audio stacks GetBufferSizeLimits returns
    // AUDCLNT_E_OFFLOAD_MODE_ONLY.
    //
    // https://docs.microsoft.com/en-us/windows-hardware/drivers/audio/hardware-offloaded-audio-processing
    let (mut min_buffer_duration, mut max_buffer_duration) = (0, 0);
    let buffer_size_is_limited = audio_client
        .cast::<Audio::IAudioClient2>()
        .and_then(|audio_client| {
            audio_client.GetBufferSizeLimits(
                waveformatex_ptr,
                true,
                &mut min_buffer_duration,
                &mut max_buffer_duration,
            )
        })
        .is_ok();
    let buffer_size = if buffer_size_is_limited {
        SupportedBufferSize::Range {
            min: buffer_duration_to_frames(min_buffer_duration, sample_rate),
            max: buffer_duration_to_frames(max_buffer_duration, sample_rate),
        }
    } else {
        SupportedBufferSize::Range {
            min: 0,
            max: u32::MAX,
        }
    };

    let format = SupportedStreamConfig {
        channels: (*waveformatex_ptr).nChannels as _,
        sample_rate,
        buffer_size,
        sample_format,
    };
    Some(format)
}

unsafe impl Send for Device {}
unsafe impl Sync for Device {}

/// Maps PKEY_AudioEndpoint_JackSubType GUID to InterfaceType.
///
/// The JackSubType property contains a KS node type GUID string from Ksmedia.h
/// that specifies the physical connector type.
fn jacksubtype_to_interface_type(guid_str: &str) -> Option<crate::InterfaceType> {
    let guid_upper = guid_str.to_uppercase();
    let typ = match guid_upper.as_str() {
        "{D9E55EA0-0C89-4692-84FF-EB3C4B0D172F}" => InterfaceType::Hdmi,
        "{E47E4031-3EA6-418D-8F9B-B73843CCB2AD}" => InterfaceType::DisplayPort,
        "{DFF21CE1-F70F-11D0-B917-00A0C9223196}" => InterfaceType::Spdif,
        _ => return None,
    };

    Some(typ)
}

/// Maps WASAPI FormFactor values to DeviceType and optionally InterfaceType.
fn form_factor_to_types(form_factor: u32) -> (crate::DeviceType, Option<crate::InterfaceType>) {
    match form_factor {
        0 => (DeviceType::Unknown, Some(InterfaceType::Network)), // RemoteNetworkDevice
        1 => (DeviceType::Speaker, None),                         // Speakers
        2 => (DeviceType::Unknown, Some(InterfaceType::Line)),    // LineLevel
        3 => (DeviceType::Headphones, None),                      // Headphones
        4 => (DeviceType::Microphone, None),                      // Microphone
        5 => (DeviceType::Headset, None),                         // Headset
        6 => (DeviceType::Handset, None),                         // Handset
        7 => (DeviceType::Unknown, None),                         // UnknownDigitalPassthrough
        8 => (DeviceType::Unknown, Some(InterfaceType::Spdif)),   // SPDIF
        9 => (DeviceType::Unknown, Some(InterfaceType::Hdmi)),    // DigitalAudioDisplayDevice
        _ => (DeviceType::Unknown, None), // UnknownFormFactor or future values
    }
}

/// Maps WASAPI EnumeratorName to InterfaceType.
fn enumerator_to_interface_type(enumerator: &str) -> Option<crate::InterfaceType> {
    let typ = match enumerator.to_uppercase().as_str() {
        "HDAUDIO" => InterfaceType::BuiltIn,
        "USB" => InterfaceType::Usb,
        "BTHENUM" => InterfaceType::Bluetooth,
        "MMDEVAPI" | "SW" => InterfaceType::Virtual,
        _ => return None,
    };
    Some(typ)
}

impl Device {
    pub fn description(&self) -> Result<DeviceDescription, DeviceNameError> {
        unsafe {
            // Open the device's property store.
            let property_store = self
                .device
                .OpenPropertyStore(STGM_READ)
                .expect("could not open property store");

            // Query all available properties
            let friendly_name = get_property_string(
                &property_store,
                &Properties::DEVPKEY_Device_FriendlyName as *const _ as *const _,
            );

            let device_desc = get_property_string(
                &property_store,
                &Properties::DEVPKEY_Device_DeviceDesc as *const _ as *const _,
            );

            let interface_name = get_property_string(
                &property_store,
                &Properties::DEVPKEY_DeviceInterface_FriendlyName as *const _ as *const _,
            );

            let enumerator_name = get_property_string(
                &property_store,
                &Properties::DEVPKEY_Device_EnumeratorName as *const _ as *const _,
            );

            let form_factor = get_property_u32(
                &property_store,
                &PKEY_AUDIOENDPOINT_FORMFACTOR as *const _ as *const _,
            );

            let jack_subtype = get_property_string(
                &property_store,
                &PKEY_AUDIOENDPOINT_JACKSUBTYPE as *const _ as *const _,
            );

            // Prefer DeviceDesc for name, fall back to FriendlyName
            let name = device_desc
                .clone()
                .or(friendly_name.clone())
                .ok_or_else(|| DeviceNameError::BackendSpecific {
                    err: BackendSpecificError {
                        description: "failed to retrieve device name".to_string(),
                    },
                })?;

            // Get direction from data flow (eCapture = Input, eRender = Output)
            let direction = self.data_flow().into();

            // Determine device_type and initial interface_type from FormFactor
            let (device_type, mut interface_type) = form_factor
                .map(form_factor_to_types)
                .unwrap_or((crate::DeviceType::Unknown, None));

            // Override interface_type from EnumeratorName if available
            if let Some(ref enumerator) = enumerator_name {
                if let Some(itype) = enumerator_to_interface_type(enumerator) {
                    interface_type = Some(itype);
                }
            }

            // JackSubType has highest priority for interface_type
            if let Some(ref jack_guid) = jack_subtype {
                if let Some(itype) = jacksubtype_to_interface_type(jack_guid) {
                    interface_type = Some(itype);
                }
            }

            let mut builder = DeviceDescriptionBuilder::new(name)
                .direction(direction)
                .device_type(device_type);

            if let Some(itype) = interface_type {
                builder = builder.interface_type(itype);
            }

            // Add interface name to driver field if available
            if let Some(iface_name) = interface_name {
                builder = builder.driver(iface_name);
            }

            // Add FriendlyName to extended if different from the name we used
            if let Some(fname) = friendly_name {
                if device_desc.is_some() && Some(&fname) != device_desc.as_ref() {
                    builder = builder.add_extended_line(fname);
                }
            }

            Ok(builder.build())
        }
    }

    fn id(&self) -> Result<DeviceId, DeviceIdError> {
        unsafe {
            match self.device.GetId() {
                Ok(pwstr) => match pwstr.to_string() {
                    Ok(id_str) => Ok(DeviceId(crate::platform::HostId::Wasapi, id_str)),
                    Err(e) => Err(DeviceIdError::BackendSpecific {
                        err: BackendSpecificError {
                            description: format!("Failed to convert device ID to string: {}", e),
                        },
                    }),
                },
                Err(e) => Err(DeviceIdError::BackendSpecific { err: e.into() }),
            }
        }
    }

    fn from_immdevice(device: Audio::IMMDevice) -> Self {
        Device {
            device,
            future_audio_client: Arc::new(Mutex::new(None)),
        }
    }

    pub fn immdevice(&self) -> &Audio::IMMDevice {
        &self.device
    }

    /// Ensures that `future_audio_client` contains a `Some` and returns a locked mutex to it.
    fn ensure_future_audio_client(
        &self,
    ) -> Result<MutexGuard<'_, Option<IAudioClientWrapper>>, windows::core::Error> {
        let mut lock = self.future_audio_client.lock().unwrap();
        if lock.is_some() {
            return Ok(lock);
        }

        let audio_client: Audio::IAudioClient = unsafe {
            // can fail if the device has been disconnected since we enumerated it, or if
            // the device doesn't support playback for some reason
            self.device.Activate(Com::CLSCTX_ALL, None)?
        };

        *lock = Some(IAudioClientWrapper(audio_client));
        Ok(lock)
    }

    /// Returns an uninitialized `IAudioClient`.
    pub(crate) fn build_audioclient(&self) -> Result<Audio::IAudioClient, windows::core::Error> {
        let mut lock = self.ensure_future_audio_client()?;
        Ok(lock.take().unwrap().0)
    }

    // There is no way to query the list of all formats that are supported by the
    // audio processor, so instead we just trial some commonly supported formats.
    //
    // Common formats are trialed by first getting the default format (returned via
    // `GetMixFormat`) and then mutating that format with common sample rates and
    // querying them via `IsFormatSupported`.
    //
    // When calling `IsFormatSupported` with the shared-mode audio engine, only the default
    // number of channels seems to be supported. Any, more or less returns an invalid
    // parameter error. Thus, we just assume that the default number of channels is the only
    // number supported.
    fn supported_formats(&self) -> Result<SupportedInputConfigs, SupportedStreamConfigsError> {
        // initializing COM because we call `CoTaskMemFree` to release the format.
        com::com_initialized();

        // Retrieve the `IAudioClient`.
        let lock = match self.ensure_future_audio_client() {
            Ok(lock) => lock,
            Err(ref e) if e.code() == Audio::AUDCLNT_E_DEVICE_INVALIDATED => {
                return Err(SupportedStreamConfigsError::DeviceNotAvailable)
            }
            Err(e) => {
                let description = format!("{}", e);
                let err = BackendSpecificError { description };
                return Err(err.into());
            }
        };
        let client = &lock.as_ref().unwrap().0;

        unsafe {
            // Retrieve the pointer to the default WAVEFORMATEX.
            let default_waveformatex_ptr = client
                .GetMixFormat()
                .map(WaveFormatExPtr)
                .map_err(windows_err_to_cpal_err::<SupportedStreamConfigsError>)?;

            // If the default format can't succeed we have no hope of finding other formats.
            if !is_format_supported(client, default_waveformatex_ptr.0)? {
                let description =
                    "Could not determine support for default `WAVEFORMATEX`".to_string();
                let err = BackendSpecificError { description };
                return Err(err.into());
            }

            let format = match format_from_waveformatex_ptr(default_waveformatex_ptr.0, client) {
                Some(fmt) => fmt,
                None => {
                    let description =
                        "could not create a `cpal::SupportedStreamConfig` from a `WAVEFORMATEX`"
                            .to_string();
                    let err = BackendSpecificError { description };
                    return Err(err.into());
                }
            };

            let mut sample_rates: Vec<SampleRate> = COMMON_SAMPLE_RATES.to_vec();

            if !sample_rates.contains(&format.sample_rate) {
                sample_rates.push(format.sample_rate)
            }

            let mut supported_formats = Vec::new();

            for sample_rate in sample_rates {
                for sample_format in [
                    SampleFormat::U8,
                    SampleFormat::I16,
                    SampleFormat::I24,
                    SampleFormat::U24,
                    SampleFormat::I32,
                    SampleFormat::I64,
                    SampleFormat::F32,
                ] {
                    if let Some(waveformat) = config_to_waveformatextensible(
                        StreamConfig {
                            channels: format.channels,
                            sample_rate,
                            buffer_size: BufferSize::Default,
                        },
                        sample_format,
                    ) {
                        if is_format_supported(
                            client,
                            &waveformat.Format as *const Audio::WAVEFORMATEX,
                        )? {
                            supported_formats.push(SupportedStreamConfigRange {
                                channels: format.channels,
                                min_sample_rate: sample_rate,
                                max_sample_rate: sample_rate,
                                buffer_size: format.buffer_size,
                                sample_format,
                            })
                        }
                    }
                }
            }
            Ok(supported_formats.into_iter())
        }
    }

    pub fn supported_input_configs(
        &self,
    ) -> Result<SupportedInputConfigs, SupportedStreamConfigsError> {
        if self.data_flow() == Audio::eCapture {
            self.supported_formats()
        // If it's an output device, assume no input formats.
        } else {
            Ok(vec![].into_iter())
        }
    }

    pub fn supported_output_configs(
        &self,
    ) -> Result<SupportedOutputConfigs, SupportedStreamConfigsError> {
        if self.data_flow() == Audio::eRender {
            self.supported_formats()
        // If it's an input device, assume no output formats.
        } else {
            Ok(vec![].into_iter())
        }
    }

    // We always create voices in shared mode, therefore all samples go through an audio
    // processor to mix them together.
    //
    // One format is guaranteed to be supported, the one returned by `GetMixFormat`.
    fn default_format(&self) -> Result<SupportedStreamConfig, DefaultStreamConfigError> {
        // initializing COM because we call `CoTaskMemFree`
        com::com_initialized();

        let lock = match self.ensure_future_audio_client() {
            Ok(lock) => lock,
            Err(ref e) if e.code() == Audio::AUDCLNT_E_DEVICE_INVALIDATED => {
                return Err(DefaultStreamConfigError::DeviceNotAvailable)
            }
            Err(e) => {
                let description = format!("{}", e);
                let err = BackendSpecificError { description };
                return Err(err.into());
            }
        };
        let client = &lock.as_ref().unwrap().0;

        unsafe {
            let format_ptr = client
                .GetMixFormat()
                .map(WaveFormatExPtr)
                .map_err(windows_err_to_cpal_err::<DefaultStreamConfigError>)?;

            format_from_waveformatex_ptr(format_ptr.0, client)
                .ok_or(DefaultStreamConfigError::StreamTypeNotSupported)
        }
    }

    pub(crate) fn data_flow(&self) -> Audio::EDataFlow {
        let endpoint = Endpoint::from(self.device.clone());
        endpoint.data_flow()
    }

    pub fn default_input_config(&self) -> Result<SupportedStreamConfig, DefaultStreamConfigError> {
        if self.data_flow() == Audio::eCapture {
            self.default_format()
        } else {
            Err(DefaultStreamConfigError::StreamTypeNotSupported)
        }
    }

    pub fn default_output_config(&self) -> Result<SupportedStreamConfig, DefaultStreamConfigError> {
        let data_flow = self.data_flow();
        if data_flow == Audio::eRender {
            self.default_format()
        } else {
            Err(DefaultStreamConfigError::StreamTypeNotSupported)
        }
    }

    pub(crate) fn build_input_stream_raw_inner(
        &self,
        config: StreamConfig,
        sample_format: SampleFormat,
    ) -> Result<StreamInner, BuildStreamError> {
        unsafe {
            // Making sure that COM is initialized.
            // It's not actually sure that this is required, but when in doubt do it.
            com::com_initialized();

            // Obtaining a `IAudioClient`.
            let audio_client = match self.build_audioclient() {
                Ok(client) => client,
                Err(ref e) if e.code() == Audio::AUDCLNT_E_DEVICE_INVALIDATED => {
                    return Err(BuildStreamError::DeviceNotAvailable)
                }
                Err(e) => {
                    let description = format!("{}", e);
                    let err = BackendSpecificError { description };
                    return Err(err.into());
                }
            };

            // Note: Buffer size validation is not needed here - `IAudioClient::Initialize`
            // will return `AUDCLNT_E_BUFFER_SIZE_ERROR` if the buffer size is not supported.
            let buffer_duration = buffer_size_to_duration(&config.buffer_size, config.sample_rate);

            let mut stream_flags = DEFAULT_FLAGS;

            if self.data_flow() == Audio::eRender {
                stream_flags |= Audio::AUDCLNT_STREAMFLAGS_LOOPBACK;
            }

            // Computing the format and initializing the device.
            let waveformatex = {
                let format_attempt = config_to_waveformatextensible(config, sample_format)
                    .ok_or(BuildStreamError::StreamConfigNotSupported)?;
                let share_mode = Audio::AUDCLNT_SHAREMODE_SHARED;

                // Ensure the format is supported.
                match super::device::is_format_supported(&audio_client, &format_attempt.Format) {
                    Ok(false) => return Err(BuildStreamError::StreamConfigNotSupported),
                    Err(_) => return Err(BuildStreamError::DeviceNotAvailable),
                    _ => (),
                }

                // Finally, initializing the audio client
                let hresult = audio_client.Initialize(
                    share_mode,
                    stream_flags,
                    buffer_duration,
                    0,
                    &format_attempt.Format,
                    None,
                );
                match hresult {
                    Err(ref e) if e.code() == Audio::AUDCLNT_E_DEVICE_INVALIDATED => {
                        return Err(BuildStreamError::DeviceNotAvailable);
                    }
                    Err(e) => {
                        let description = format!("{}", e);
                        let err = BackendSpecificError { description };
                        return Err(err.into());
                    }
                    Ok(()) => (),
                };

                format_attempt.Format
            };

            // obtaining the size of the samples buffer in number of frames
            let max_frames_in_buffer = audio_client
                .GetBufferSize()
                .map_err(windows_err_to_cpal_err::<BuildStreamError>)?;

            let period_frames =
                shared_mode_period_frames(&audio_client, config.sample_rate, max_frames_in_buffer);

            // Creating the event that will be signalled whenever we need to submit some samples.
            let event = {
                let event =
                    Threading::CreateEventA(None, false, false, windows::core::PCSTR(ptr::null()))
                        .map_err(|e| {
                            let description = format!("failed to create event: {}", e);
                            let err = BackendSpecificError { description };
                            BuildStreamError::from(err)
                        })?;

                if let Err(e) = audio_client.SetEventHandle(event) {
                    let description = format!("failed to call SetEventHandle: {}", e);
                    let err = BackendSpecificError { description };
                    return Err(err.into());
                }

                event
            };

            // Building a `IAudioCaptureClient` that will be used to read captured samples.
            let capture_client = audio_client
                .GetService::<Audio::IAudioCaptureClient>()
                .map_err(|e| {
                    windows_err_to_cpal_err_message::<BuildStreamError>(
                        e,
                        "failed to build capture client: ",
                    )
                })?;

            // Once we built the `StreamInner`, we add a command that will be picked up by the
            // `run()` method and added to the `RunContext`.
            let client_flow = AudioClientFlow::Capture { capture_client };

            let audio_clock = get_audio_clock(&audio_client)?;

            let stream_latency = {
                let hns = audio_client.GetStreamLatency().map_err(|e| {
                    windows_err_to_cpal_err_message::<BuildStreamError>(
                        e,
                        "failed to get stream latency: ",
                    )
                })?;
                Duration::from_nanos(hns.max(0) as u64 * 100)
            };

            Ok(StreamInner {
                audio_client,
                audio_clock,
                client_flow,
                event,
                playing: false,
                max_frames_in_buffer,
                period_frames,
                bytes_per_frame: waveformatex.nBlockAlign,
                config,
                sample_format,
                stream_latency,
            })
        }
    }

    pub(crate) fn build_output_stream_raw_inner(
        &self,
        config: StreamConfig,
        sample_format: SampleFormat,
    ) -> Result<StreamInner, BuildStreamError> {
        unsafe {
            // Making sure that COM is initialized.
            // It's not actually sure that this is required, but when in doubt do it.
            com::com_initialized();

            // Obtaining a `IAudioClient`.
            let audio_client = self
                .build_audioclient()
                .map_err(windows_err_to_cpal_err::<BuildStreamError>)?;

            // Note: Buffer size validation is not needed here - `IAudioClient::Initialize`
            // will return `AUDCLNT_E_BUFFER_SIZE_ERROR` if the buffer size is not supported.
            let buffer_duration = buffer_size_to_duration(&config.buffer_size, config.sample_rate);

            // Computing the format and initializing the device.
            let waveformatex = {
                let format_attempt = config_to_waveformatextensible(config, sample_format)
                    .ok_or(BuildStreamError::StreamConfigNotSupported)?;
                let share_mode = Audio::AUDCLNT_SHAREMODE_SHARED;

                // Ensure the format is supported.
                match super::device::is_format_supported(&audio_client, &format_attempt.Format) {
                    Ok(false) => return Err(BuildStreamError::StreamConfigNotSupported),
                    Err(_) => return Err(BuildStreamError::DeviceNotAvailable),
                    _ => (),
                }

                // Finally, initializing the audio client
                audio_client
                    .Initialize(
                        share_mode,
                        DEFAULT_FLAGS,
                        buffer_duration,
                        0,
                        &format_attempt.Format,
                        None,
                    )
                    .map_err(windows_err_to_cpal_err::<BuildStreamError>)?;

                format_attempt.Format
            };

            // Creating the event that will be signalled whenever we need to submit some samples.
            let event = {
                let event =
                    Threading::CreateEventA(None, false, false, windows::core::PCSTR(ptr::null()))
                        .map_err(|e| {
                            let description = format!("failed to create event: {}", e);
                            let err = BackendSpecificError { description };
                            BuildStreamError::from(err)
                        })?;

                if let Err(e) = audio_client.SetEventHandle(event) {
                    let description = format!("failed to call SetEventHandle: {}", e);
                    let err = BackendSpecificError { description };
                    return Err(err.into());
                }

                event
            };

            // obtaining the size of the samples buffer in number of frames
            let max_frames_in_buffer = audio_client.GetBufferSize().map_err(|e| {
                windows_err_to_cpal_err_message::<BuildStreamError>(
                    e,
                    "failed to obtain buffer size: ",
                )
            })?;

            let period_frames =
                shared_mode_period_frames(&audio_client, config.sample_rate, max_frames_in_buffer);

            // Building a `IAudioRenderClient` that will be used to fill the samples buffer.
            let render_client = audio_client
                .GetService::<IAudioRenderClient>()
                .map_err(|e| {
                    windows_err_to_cpal_err_message::<BuildStreamError>(
                        e,
                        "failed to build render client: ",
                    )
                })?;

            // Once we built the `StreamInner`, we add a command that will be picked up by the
            // `run()` method and added to the `RunContext`.
            let client_flow = AudioClientFlow::Render { render_client };

            let audio_clock = get_audio_clock(&audio_client)?;

            let stream_latency = {
                let hns = audio_client.GetStreamLatency().map_err(|e| {
                    windows_err_to_cpal_err_message::<BuildStreamError>(
                        e,
                        "failed to get stream latency: ",
                    )
                })?;
                Duration::from_nanos(hns.max(0) as u64 * 100)
            };

            Ok(StreamInner {
                audio_client,
                audio_clock,
                client_flow,
                event,
                playing: false,
                max_frames_in_buffer,
                period_frames,
                bytes_per_frame: waveformatex.nBlockAlign,
                config,
                sample_format,
                stream_latency,
            })
        }
    }
}

impl PartialEq for Device {
    fn eq(&self, other: &Device) -> bool {
        // Use case: In order to check whether the default device has changed
        // the client code might need to compare the previous default device with the current one.
        // The pointer comparison (`self.device == other.device`) don't work there,
        // because the pointers are different even when the default device stays the same.
        //
        // In this code section we're trying to use the GetId method for the device comparison, cf.
        // https://docs.microsoft.com/en-us/windows/desktop/api/mmdeviceapi/nf-mmdeviceapi-immdevice-getid
        unsafe {
            struct IdRAII(windows::core::PWSTR);
            /// RAII for device IDs.
            impl Drop for IdRAII {
                fn drop(&mut self) {
                    unsafe { Com::CoTaskMemFree(Some(self.0 .0 as *mut _)) }
                }
            }
            // GetId only fails with E_OUTOFMEMORY and if it does, we're probably dead already.
            // Plus it won't do to change the device comparison logic unexpectedly.
            let id1 = self.device.GetId().expect("cpal: GetId failure");
            let id1 = IdRAII(id1);
            let id2 = other.device.GetId().expect("cpal: GetId failure");
            let id2 = IdRAII(id2);
            // 16-bit null-terminated comparison.
            let mut offset = 0;
            loop {
                let w1: u16 = *(id1.0).0.offset(offset);
                let w2: u16 = *(id2.0).0.offset(offset);
                if w1 == 0 && w2 == 0 {
                    return true;
                }
                if w1 != w2 {
                    return false;
                }
                offset += 1;
            }
        }
    }
}

impl Eq for Device {}

impl std::hash::Hash for Device {
    fn hash<H: std::hash::Hasher>(&self, state: &mut H) {
        // Hash the device ID for consistency with PartialEq
        // SAFETY: GetId only fails with E_OUTOFMEMORY, which is unrecoverable.
        // We need consistent hash/eq behavior.
        unsafe {
            use windows::Win32::System::Com;

            struct IdRAII(windows::core::PWSTR);
            impl Drop for IdRAII {
                fn drop(&mut self) {
                    unsafe { Com::CoTaskMemFree(Some(self.0 .0 as *mut _)) }
                }
            }

            let id = self.device.GetId().expect("cpal: GetId failure");
            let id = IdRAII(id);

            // Hash the 16-bit null-terminated string
            let mut offset = 0;
            loop {
                let w: u16 = *(id.0).0.offset(offset);
                if w == 0 {
                    break;
                }
                w.hash(state);
                offset += 1;
            }
        }
    }
}

impl fmt::Debug for Device {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        f.debug_struct("Device")
            .field("device", &self.device)
            .field("description", &self.description())
            .finish()
    }
}

impl From<Audio::IMMDevice> for Endpoint {
    fn from(device: Audio::IMMDevice) -> Self {
        unsafe {
            let endpoint = immendpoint_from_immdevice(device);
            Endpoint { endpoint }
        }
    }
}

impl Endpoint {
    fn data_flow(&self) -> Audio::EDataFlow {
        unsafe { data_flow_from_immendpoint(&self.endpoint) }
    }
}

static ENUMERATOR: OnceLock<Enumerator> = OnceLock::new();

fn get_enumerator() -> &'static Enumerator {
    ENUMERATOR.get_or_init(|| {
        // COM initialization is thread local, but we only need to have COM initialized in the
        // thread we create the objects in
        com::com_initialized();

        // building the devices enumerator object
        unsafe {
            let enumerator = Com::CoCreateInstance::<_, Audio::IMMDeviceEnumerator>(
                &Audio::MMDeviceEnumerator,
                None,
                Com::CLSCTX_ALL,
            )
            .unwrap();

            Enumerator(enumerator)
        }
    })
}

// Helper function to query a DWORD property from a WASAPI device property store
unsafe fn get_property_u32(
    property_store: &IPropertyStore,
    property_key: *const PROPERTYKEY,
) -> Option<u32> {
    let mut property_value = property_store.GetValue(property_key).ok()?;
    let prop_variant = &property_value.Anonymous.Anonymous;

    // Check if it's a UI4 (unsigned 32-bit integer)
    if prop_variant.vt != VT_UI4 {
        return None;
    }

    let value = *(&prop_variant.Anonymous as *const _ as *const u32);

    // Clean up the property
    StructuredStorage::PropVariantClear(&mut property_value).ok();

    Some(value)
}

// Helper function to query a string property from a WASAPI device property store
unsafe fn get_property_string(
    property_store: &IPropertyStore,
    property_key: *const PROPERTYKEY,
) -> Option<String> {
    let mut property_value = property_store.GetValue(property_key).ok()?;
    let prop_variant = &property_value.Anonymous.Anonymous;

    // Read the string from the union data field, expecting a *const u16.
    if prop_variant.vt != VT_LPWSTR {
        return None;
    }
    let ptr_utf16 = *(&prop_variant.Anonymous as *const _ as *const *const u16);

    // Find the length of the null-terminated string with a safety limit
    const MAX_STRING_LEN: usize = 32768; // 32K characters should be more than enough
    let mut len = 0;
    while len < MAX_STRING_LEN && *ptr_utf16.add(len) != 0 {
        len += 1;
    }

    // If we hit the limit, the string is likely malformed (not null-terminated)
    if len >= MAX_STRING_LEN {
        return None;
    }

    // Create the utf16 slice and convert it into a string.
    let string_slice = slice::from_raw_parts(ptr_utf16, len);
    let os_string: OsString = OsStringExt::from_wide(string_slice);
    let result = match os_string.into_string() {
        Ok(string) => Some(string),
        Err(os_string) => Some(os_string.to_string_lossy().into()),
    };

    // Clean up the property.
    StructuredStorage::PropVariantClear(&mut property_value).ok();

    result
}

/// Send/Sync wrapper around `IMMDeviceEnumerator`.
struct Enumerator(Audio::IMMDeviceEnumerator);

unsafe impl Send for Enumerator {}
unsafe impl Sync for Enumerator {}

/// WASAPI implementation for `Devices`.
pub struct Devices {
    collection: Audio::IMMDeviceCollection,
    total_count: u32,
    next_item: u32,
}

impl Devices {
    pub fn new() -> Result<Self, DevicesError> {
        unsafe {
            // can fail because of wrong parameters (should never happen) or out of memory
            let collection = get_enumerator()
                .0
                .EnumAudioEndpoints(Audio::eAll, Audio::DEVICE_STATE_ACTIVE)
                .map_err(BackendSpecificError::from)?;

            let count = collection.GetCount().map_err(BackendSpecificError::from)?;

            Ok(Devices {
                collection,
                total_count: count,
                next_item: 0,
            })
        }
    }
}

unsafe impl Send for Devices {}
unsafe impl Sync for Devices {}

impl Iterator for Devices {
    type Item = Device;

    fn next(&mut self) -> Option<Device> {
        if self.next_item >= self.total_count {
            return None;
        }

        unsafe {
            let device = self.collection.Item(self.next_item).unwrap();
            self.next_item += 1;
            Some(Device::from_immdevice(device))
        }
    }

    fn size_hint(&self) -> (usize, Option<usize>) {
        let num = self.total_count - self.next_item;
        let num = num as usize;
        (num, Some(num))
    }
}

fn default_device(data_flow: Audio::EDataFlow) -> Option<Device> {
    unsafe {
        let device = get_enumerator()
            .0
            .GetDefaultAudioEndpoint(data_flow, Audio::eConsole)
            .ok()?;
        // TODO: check specifically for `E_NOTFOUND`, and panic otherwise
        Some(Device::from_immdevice(device))
    }
}

pub fn default_input_device() -> Option<Device> {
    default_device(Audio::eCapture)
}

pub fn default_output_device() -> Option<Device> {
    default_device(Audio::eRender)
}

/// Get the audio clock used to produce `StreamInstant`s.
unsafe fn get_audio_clock(
    audio_client: &Audio::IAudioClient,
) -> Result<Audio::IAudioClock, BuildStreamError> {
    audio_client
        .GetService::<Audio::IAudioClock>()
        .map_err(|e| {
            windows_err_to_cpal_err_message::<BuildStreamError>(e, "failed to build audio clock: ")
        })
}

// Turns a `Format` into a `WAVEFORMATEXTENSIBLE`.
//
// Returns `None` if the WAVEFORMATEXTENSIBLE does not support the given format.
fn config_to_waveformatextensible(
    config: StreamConfig,
    sample_format: SampleFormat,
) -> Option<Audio::WAVEFORMATEXTENSIBLE> {
    let format_tag = match sample_format {
        SampleFormat::U8 | SampleFormat::I16 => Audio::WAVE_FORMAT_PCM,

        SampleFormat::I24
        | SampleFormat::U24
        | SampleFormat::I32
        | SampleFormat::I64
        | SampleFormat::F32 => KernelStreaming::WAVE_FORMAT_EXTENSIBLE,

        _ => return None,
    };
    let channels = config.channels;
    let sample_rate = config.sample_rate;
    let sample_bytes = sample_format.sample_size() as u16;
    let avg_bytes_per_sec = u32::from(channels) * sample_rate * u32::from(sample_bytes);
    let block_align = channels * sample_bytes;
    let bits_per_sample = match sample_format {
        // 24-bit formats use 32-bit storage but only 24 valid bits
        SampleFormat::I24 | SampleFormat::U24 => 24,
        _ => 8 * sample_bytes,
    };

    let cb_size = if format_tag == Audio::WAVE_FORMAT_PCM {
        0
    } else {
        let extensible_size = mem::size_of::<Audio::WAVEFORMATEXTENSIBLE>();
        let ex_size = mem::size_of::<Audio::WAVEFORMATEX>();
        (extensible_size - ex_size) as u16
    };

    let waveformatex = Audio::WAVEFORMATEX {
        wFormatTag: format_tag as u16,
        nChannels: channels,
        nSamplesPerSec: sample_rate,
        nAvgBytesPerSec: avg_bytes_per_sec,
        nBlockAlign: block_align,
        wBitsPerSample: bits_per_sample,
        cbSize: cb_size,
    };

    // CPAL does not care about speaker positions, so pass audio right through.
    let channel_mask = KernelStreaming::KSAUDIO_SPEAKER_DIRECTOUT;

    let sub_format = match sample_format {
        SampleFormat::U8
        | SampleFormat::I16
        | SampleFormat::I24
        | SampleFormat::U24
        | SampleFormat::I32
        | SampleFormat::I64 => KernelStreaming::KSDATAFORMAT_SUBTYPE_PCM,

        SampleFormat::F32 => Multimedia::KSDATAFORMAT_SUBTYPE_IEEE_FLOAT,
        _ => return None,
    };

    let waveformatextensible = Audio::WAVEFORMATEXTENSIBLE {
        Format: waveformatex,
        Samples: Audio::WAVEFORMATEXTENSIBLE_0 {
            wSamplesPerBlock: bits_per_sample,
        },
        dwChannelMask: channel_mask,
        SubFormat: sub_format,
    };

    Some(waveformatextensible)
}

/// Get the default device period in frames for a shared-mode stream.
fn shared_mode_period_frames(
    audio_client: &Audio::IAudioClient,
    sample_rate: crate::SampleRate,
    max_frames_in_buffer: crate::FrameCount,
) -> crate::FrameCount {
    let mut default_period = 0i64;
    if unsafe { audio_client.GetDevicePeriod(Some(&mut default_period), None) }.is_ok()
        && default_period > 0
    {
        buffer_duration_to_frames(default_period, sample_rate)
    } else {
        max_frames_in_buffer
    }
}

fn buffer_size_to_duration(buffer_size: &BufferSize, sample_rate: SampleRate) -> i64 {
    match buffer_size {
        BufferSize::Fixed(frames) => *frames as i64 * (1_000_000_000 / 100) / sample_rate as i64,
        BufferSize::Default => 0,
    }
}

fn buffer_duration_to_frames(buffer_duration: i64, sample_rate: SampleRate) -> FrameCount {
    (buffer_duration * sample_rate as i64 * 100 / 1_000_000_000) as FrameCount
}
```

## File: `src/host/wasapi/mod.rs`
```rust
//! WASAPI backend implementation.
//!
//! Default backend on Windows.

#[allow(unused_imports)]
pub use self::device::{
    default_input_device, default_output_device, Device, Devices, SupportedInputConfigs,
    SupportedOutputConfigs,
};
#[allow(unused_imports)]
pub use self::stream::Stream;
use crate::traits::HostTrait;
use crate::BackendSpecificError;
use crate::DevicesError;
use std::io::Error as IoError;
use windows::Win32::Media::Audio;

mod device;
mod stream;

/// The WASAPI host, the default windows host type.
///
/// Note: If you use a WASAPI output device as an input device it will
/// transparently enable loopback mode (see
/// https://docs.microsoft.com/en-us/windows/win32/coreaudio/loopback-recording).
#[derive(Debug)]
pub struct Host;

impl Host {
    pub fn new() -> Result<Self, crate::HostUnavailable> {
        Ok(Host)
    }
}

impl HostTrait for Host {
    type Devices = Devices;
    type Device = Device;

    fn is_available() -> bool {
        // Assume WASAPI is always available on Windows.
        true
    }

    fn devices(&self) -> Result<Self::Devices, DevicesError> {
        Devices::new()
    }

    fn default_input_device(&self) -> Option<Self::Device> {
        default_input_device()
    }

    fn default_output_device(&self) -> Option<Self::Device> {
        default_output_device()
    }
}

impl From<windows::core::Error> for BackendSpecificError {
    fn from(error: windows::core::Error) -> Self {
        BackendSpecificError {
            description: format!("{}", IoError::from(error)),
        }
    }
}

trait ErrDeviceNotAvailable: From<BackendSpecificError> {
    fn device_not_available() -> Self;
}

impl ErrDeviceNotAvailable for crate::BuildStreamError {
    fn device_not_available() -> Self {
        Self::DeviceNotAvailable
    }
}

impl ErrDeviceNotAvailable for crate::SupportedStreamConfigsError {
    fn device_not_available() -> Self {
        Self::DeviceNotAvailable
    }
}

impl ErrDeviceNotAvailable for crate::DefaultStreamConfigError {
    fn device_not_available() -> Self {
        Self::DeviceNotAvailable
    }
}

impl ErrDeviceNotAvailable for crate::StreamError {
    fn device_not_available() -> Self {
        Self::DeviceNotAvailable
    }
}

fn windows_err_to_cpal_err<E: ErrDeviceNotAvailable>(e: windows::core::Error) -> E {
    windows_err_to_cpal_err_message::<E>(e, "")
}

fn windows_err_to_cpal_err_message<E: ErrDeviceNotAvailable>(
    e: windows::core::Error,
    message: &str,
) -> E {
    match e.code() {
        Audio::AUDCLNT_E_DEVICE_INVALIDATED | Audio::AUDCLNT_E_DEVICE_IN_USE => {
            E::device_not_available()
        }
        _ => {
            let description = format!("{}{}", message, e);
            let err = BackendSpecificError { description };
            err.into()
        }
    }
}
```

## File: `src/host/wasapi/stream.rs`
```rust
use super::windows_err_to_cpal_err;
use crate::traits::StreamTrait;
use crate::{
    BackendSpecificError, BufferSize, Data, FrameCount, InputCallbackInfo, OutputCallbackInfo,
    PauseStreamError, PlayStreamError, SampleFormat, SampleRate, StreamError,
};
use std::mem;
use std::ptr;
use std::sync::mpsc::{channel, Receiver, SendError, Sender};
use std::thread::{self, JoinHandle};
use std::time::Duration;
use windows::Win32::Foundation;
use windows::Win32::Foundation::WAIT_OBJECT_0;
use windows::Win32::Media::Audio;
use windows::Win32::System::SystemServices;
use windows::Win32::System::Threading;

pub struct Stream {
    /// The high-priority audio processing thread calling callbacks.
    /// Option used for moving out in destructor.
    ///
    /// TODO: Actually set the thread priority.
    thread: Option<JoinHandle<()>>,

    // Commands processed by the `run()` method that is currently running.
    // `pending_scheduled_event` must be signalled whenever a command is added here, so that it
    // will get picked up.
    commands: Sender<Command>,

    // This event is signalled after a new entry is added to `commands`, so that the `run()`
    // method can be notified.
    pending_scheduled_event: Foundation::HANDLE,

    // Callback size in frames.
    period_frames: FrameCount,
}

// SAFETY: Windows Event HANDLEs are safe to send between threads - they are designed for
// synchronization. All fields of Stream are Send:
// - JoinHandle<()> is Send
// - Sender<Command> is Send
// - Foundation::HANDLE is Send (Windows synchronization primitive)
// See: https://learn.microsoft.com/en-us/windows/win32/api/synchapi/nf-synchapi-createeventa
unsafe impl Send for Stream {}

// SAFETY: Windows Event HANDLEs are safe to access from multiple threads simultaneously.
// All synchronization operations (SetEvent, WaitForSingleObject) are thread-safe.
// All fields of Stream are Sync:
// - JoinHandle<()> is Sync
// - Sender<Command> is Sync (uses internal synchronization)
// - Foundation::HANDLE for event objects supports concurrent access
// The audio thread owns all COM objects, so no cross-thread COM access occurs.
unsafe impl Sync for Stream {}

// Compile-time assertion that Stream is Send and Sync
crate::assert_stream_send!(Stream);
crate::assert_stream_sync!(Stream);

struct RunContext {
    // Streams that have been created in this event loop.
    stream: StreamInner,

    // Handles corresponding to the `event` field of each element of `voices`. Must always be in
    // sync with `voices`, except that the first element is always `pending_scheduled_event`.
    handles: Vec<Foundation::HANDLE>,

    commands: Receiver<Command>,
}

// Once we start running the eventloop, the RunContext will not be moved.
unsafe impl Send for RunContext {}

pub enum Command {
    PlayStream,
    PauseStream,
    Terminate,
}

pub enum AudioClientFlow {
    Render {
        render_client: Audio::IAudioRenderClient,
    },
    Capture {
        capture_client: Audio::IAudioCaptureClient,
    },
}

pub struct StreamInner {
    pub audio_client: Audio::IAudioClient,
    pub audio_clock: Audio::IAudioClock,
    pub client_flow: AudioClientFlow,
    // Event that is signalled by WASAPI whenever audio data must be written.
    pub event: Foundation::HANDLE,
    // True if the stream is currently playing. False if paused.
    pub playing: bool,
    // Number of frames of audio data in the underlying buffer allocated by WASAPI.
    pub max_frames_in_buffer: FrameCount,
    // Callback size in frames.
    pub period_frames: FrameCount,
    // Number of bytes that each frame occupies.
    pub bytes_per_frame: u16,
    // The configuration with which the stream was created.
    pub config: crate::StreamConfig,
    // The sample format with which the stream was created.
    pub sample_format: SampleFormat,
    // Hardware pipeline latency.
    pub stream_latency: Duration,
}

impl Stream {
    pub(crate) fn new_input<D, E>(
        stream_inner: StreamInner,
        mut data_callback: D,
        mut error_callback: E,
    ) -> Stream
    where
        D: FnMut(&Data, &InputCallbackInfo) + Send + 'static,
        E: FnMut(StreamError) + Send + 'static,
    {
        let pending_scheduled_event = unsafe {
            Threading::CreateEventA(None, false, false, windows::core::PCSTR(ptr::null()))
        }
        .expect("cpal: could not create input stream event");
        let (tx, rx) = channel();

        let period_frames = stream_inner.period_frames;

        let run_context = RunContext {
            handles: vec![pending_scheduled_event, stream_inner.event],
            stream: stream_inner,
            commands: rx,
        };

        let thread = thread::Builder::new()
            .name("cpal_wasapi_in".to_owned())
            .spawn(move || run_input(run_context, &mut data_callback, &mut error_callback))
            .unwrap();

        Stream {
            thread: Some(thread),
            commands: tx,
            pending_scheduled_event,
            period_frames,
        }
    }

    pub(crate) fn new_output<D, E>(
        stream_inner: StreamInner,
        mut data_callback: D,
        mut error_callback: E,
    ) -> Stream
    where
        D: FnMut(&mut Data, &OutputCallbackInfo) + Send + 'static,
        E: FnMut(StreamError) + Send + 'static,
    {
        let pending_scheduled_event = unsafe {
            Threading::CreateEventA(None, false, false, windows::core::PCSTR(ptr::null()))
        }
        .expect("cpal: could not create output stream event");
        let (tx, rx) = channel();

        let period_frames = stream_inner.period_frames;

        let run_context = RunContext {
            handles: vec![pending_scheduled_event, stream_inner.event],
            stream: stream_inner,
            commands: rx,
        };

        let thread = thread::Builder::new()
            .name("cpal_wasapi_out".to_owned())
            .spawn(move || run_output(run_context, &mut data_callback, &mut error_callback))
            .unwrap();

        Stream {
            thread: Some(thread),
            commands: tx,
            pending_scheduled_event,
            period_frames,
        }
    }

    fn push_command(&self, command: Command) -> Result<(), SendError<Command>> {
        self.commands.send(command)?;
        unsafe {
            Threading::SetEvent(self.pending_scheduled_event).unwrap();
        }
        Ok(())
    }
}

impl Drop for Stream {
    fn drop(&mut self) {
        if self.push_command(Command::Terminate).is_ok() {
            if let Some(handle) = self.thread.take() {
                let _ = handle.join();
            }
            unsafe {
                let _ = Foundation::CloseHandle(self.pending_scheduled_event);
            }
        }
    }
}

impl StreamTrait for Stream {
    fn play(&self) -> Result<(), PlayStreamError> {
        self.push_command(Command::PlayStream)
            .map_err(|_| crate::error::PlayStreamError::DeviceNotAvailable)?;
        Ok(())
    }

    fn pause(&self) -> Result<(), PauseStreamError> {
        self.push_command(Command::PauseStream)
            .map_err(|_| crate::error::PauseStreamError::DeviceNotAvailable)?;
        Ok(())
    }

    fn buffer_size(&self) -> Option<FrameCount> {
        Some(self.period_frames)
    }
}

impl Drop for StreamInner {
    fn drop(&mut self) {
        unsafe {
            let _ = Foundation::CloseHandle(self.event);
        }
    }
}

// Process any pending commands that are queued within the `RunContext`.
// Returns `true` if the loop should continue running, `false` if it should terminate.
fn process_commands(run_context: &mut RunContext) -> Result<bool, StreamError> {
    // Process the pending commands.
    for command in run_context.commands.try_iter() {
        match command {
            Command::PlayStream => unsafe {
                if !run_context.stream.playing {
                    run_context
                        .stream
                        .audio_client
                        .Start()
                        .map_err(windows_err_to_cpal_err::<StreamError>)?;
                    run_context.stream.playing = true;
                }
            },
            Command::PauseStream => unsafe {
                if run_context.stream.playing {
                    run_context
                        .stream
                        .audio_client
                        .Stop()
                        .map_err(windows_err_to_cpal_err::<StreamError>)?;
                    run_context.stream.playing = false;
                }
            },
            Command::Terminate => {
                return Ok(false);
            }
        }
    }

    Ok(true)
}
// Wait for any of the given handles to be signalled.
//
// Returns the index of the `handle` that was signalled, or an `Err` if
// `WaitForMultipleObjectsEx` fails.
//
// This is called when the `run` thread is ready to wait for the next event. The
// next event might be some command submitted by the user (the first handle) or
// might indicate that one of the streams is ready to deliver or receive audio.
fn wait_for_handle_signal(handles: &[Foundation::HANDLE]) -> Result<usize, BackendSpecificError> {
    debug_assert!(handles.len() <= SystemServices::MAXIMUM_WAIT_OBJECTS as usize);
    let result = unsafe {
        Threading::WaitForMultipleObjectsEx(
            handles,
            false,               // Don't wait for all, just wait for the first
            Threading::INFINITE, // TODO: allow setting a timeout
            false,               // irrelevant parameter here
        )
    };
    if result == Foundation::WAIT_FAILED {
        let err = unsafe { Foundation::GetLastError() };
        let description = format!("`WaitForMultipleObjectsEx failed: {:?}", err);
        let err = BackendSpecificError { description };
        return Err(err);
    }
    // Notifying the corresponding task handler.
    let handle_idx = (result.0 - WAIT_OBJECT_0.0) as usize;
    Ok(handle_idx)
}

// Get the number of available frames that are available for writing/reading.
fn get_available_frames(stream: &StreamInner) -> Result<FrameCount, StreamError> {
    unsafe {
        let padding = stream
            .audio_client
            .GetCurrentPadding()
            .map_err(windows_err_to_cpal_err::<StreamError>)?;
        Ok(stream.max_frames_in_buffer - padding)
    }
}

fn run_input(
    mut run_ctxt: RunContext,
    data_callback: &mut dyn FnMut(&Data, &InputCallbackInfo),
    error_callback: &mut dyn FnMut(StreamError),
) {
    boost_current_thread_priority(
        run_ctxt.stream.config.buffer_size,
        run_ctxt.stream.config.sample_rate,
    );

    loop {
        match process_commands_and_await_signal(&mut run_ctxt, error_callback) {
            Some(ControlFlow::Break) => break,
            Some(ControlFlow::Continue) => continue,
            None => (),
        }
        let capture_client = match run_ctxt.stream.client_flow {
            AudioClientFlow::Capture { ref capture_client } => capture_client.clone(),
            _ => unreachable!(),
        };
        match process_input(
            &run_ctxt.stream,
            capture_client,
            data_callback,
            error_callback,
        ) {
            ControlFlow::Break => break,
            ControlFlow::Continue => continue,
        }
    }
}

fn run_output(
    mut run_ctxt: RunContext,
    data_callback: &mut dyn FnMut(&mut Data, &OutputCallbackInfo),
    error_callback: &mut dyn FnMut(StreamError),
) {
    boost_current_thread_priority(
        run_ctxt.stream.config.buffer_size,
        run_ctxt.stream.config.sample_rate,
    );

    loop {
        match process_commands_and_await_signal(&mut run_ctxt, error_callback) {
            Some(ControlFlow::Break) => break,
            Some(ControlFlow::Continue) => continue,
            None => (),
        }
        let render_client = match run_ctxt.stream.client_flow {
            AudioClientFlow::Render { ref render_client } => render_client.clone(),
            _ => unreachable!(),
        };
        match process_output(
            &run_ctxt.stream,
            render_client,
            data_callback,
            error_callback,
        ) {
            ControlFlow::Break => break,
            ControlFlow::Continue => continue,
        }
    }
}

#[cfg(feature = "audio_thread_priority")]
fn boost_current_thread_priority(buffer_size: BufferSize, sample_rate: SampleRate) {
    use audio_thread_priority::promote_current_thread_to_real_time;

    let buffer_size = if let BufferSize::Fixed(buffer_size) = buffer_size {
        buffer_size
    } else {
        // if the buffer size isn't fixed, let audio_thread_priority choose a sensible default value
        0
    };

    if let Err(err) = promote_current_thread_to_real_time(buffer_size, sample_rate) {
        eprintln!("Failed to promote audio thread to real-time priority: {err}");
    }
}

#[cfg(not(feature = "audio_thread_priority"))]
fn boost_current_thread_priority(_: BufferSize, _: SampleRate) {
    unsafe {
        let thread_handle = Threading::GetCurrentThread();

        let _ =
            Threading::SetThreadPriority(thread_handle, Threading::THREAD_PRIORITY_TIME_CRITICAL);
    }
}

enum ControlFlow {
    Break,
    Continue,
}

fn process_commands_and_await_signal(
    run_context: &mut RunContext,
    error_callback: &mut dyn FnMut(StreamError),
) -> Option<ControlFlow> {
    // Process queued commands.
    match process_commands(run_context) {
        Ok(true) => (),
        Ok(false) => return Some(ControlFlow::Break),
        Err(err) => {
            error_callback(err);
            return Some(ControlFlow::Break);
        }
    };

    // Wait for any of the handles to be signalled.
    let handle_idx = match wait_for_handle_signal(&run_context.handles) {
        Ok(idx) => idx,
        Err(err) => {
            error_callback(err.into());
            return Some(ControlFlow::Break);
        }
    };

    // If `handle_idx` is 0, then it's `pending_scheduled_event` that was signalled in
    // order for us to pick up the pending commands. Otherwise, a stream needs data.
    if handle_idx == 0 {
        return Some(ControlFlow::Continue);
    }

    None
}

// The loop for processing pending input data.
fn process_input(
    stream: &StreamInner,
    capture_client: Audio::IAudioCaptureClient,
    data_callback: &mut dyn FnMut(&Data, &InputCallbackInfo),
    error_callback: &mut dyn FnMut(StreamError),
) -> ControlFlow {
    unsafe {
        // Get the available data in the shared buffer.
        let mut buffer: *mut u8 = ptr::null_mut();
        let mut flags = mem::MaybeUninit::uninit();
        loop {
            let mut frames_available = match capture_client.GetNextPacketSize() {
                Ok(0) => return ControlFlow::Continue,
                Ok(f) => f,
                Err(err) => {
                    error_callback(windows_err_to_cpal_err(err));
                    return ControlFlow::Break;
                }
            };
            let mut qpc_position: u64 = 0;
            let result = capture_client.GetBuffer(
                &mut buffer,
                &mut frames_available,
                flags.as_mut_ptr(),
                None,
                Some(&mut qpc_position),
            );

            match result {
                // TODO: Can this happen?
                Err(e) if e.code() == Audio::AUDCLNT_S_BUFFER_EMPTY => continue,
                Err(e) => {
                    error_callback(windows_err_to_cpal_err(e));
                    return ControlFlow::Break;
                }
                Ok(_) => (),
            }

            debug_assert!(!buffer.is_null());

            let data = buffer as *mut ();
            let len = frames_available as usize * stream.bytes_per_frame as usize
                / stream.sample_format.sample_size();
            let data = Data::from_parts(data, len, stream.sample_format);

            // The `qpc_position` is in 100 nanosecond units. Convert it to nanoseconds.
            let timestamp = match input_timestamp(stream, qpc_position) {
                Ok(ts) => ts,
                Err(err) => {
                    error_callback(err);
                    return ControlFlow::Break;
                }
            };
            let info = InputCallbackInfo { timestamp };
            data_callback(&data, &info);

            // Release the buffer.
            let result = capture_client
                .ReleaseBuffer(frames_available)
                .map_err(windows_err_to_cpal_err);
            if let Err(err) = result {
                error_callback(err);
                return ControlFlow::Break;
            }
        }
    }
}

// The loop for writing output data.
fn process_output(
    stream: &StreamInner,
    render_client: Audio::IAudioRenderClient,
    data_callback: &mut dyn FnMut(&mut Data, &OutputCallbackInfo),
    error_callback: &mut dyn FnMut(StreamError),
) -> ControlFlow {
    // The number of frames available for writing.
    let frames_available = match get_available_frames(stream) {
        Ok(0) => return ControlFlow::Continue, // TODO: Can this happen?
        Ok(n) => n,
        Err(err) => {
            error_callback(err);
            return ControlFlow::Break;
        }
    };

    unsafe {
        let buffer = match render_client.GetBuffer(frames_available) {
            Ok(b) => b,
            Err(e) => {
                error_callback(windows_err_to_cpal_err(e));
                return ControlFlow::Break;
            }
        };

        debug_assert!(!buffer.is_null());

        let data = buffer as *mut ();
        let len = frames_available as usize * stream.bytes_per_frame as usize
            / stream.sample_format.sample_size();
        let mut data = Data::from_parts(data, len, stream.sample_format);
        let sample_rate = stream.config.sample_rate;
        let timestamp = match output_timestamp(stream, frames_available, sample_rate) {
            Ok(ts) => ts,
            Err(err) => {
                error_callback(err);
                return ControlFlow::Break;
            }
        };
        let info = OutputCallbackInfo { timestamp };
        data_callback(&mut data, &info);

        if let Err(err) = render_client.ReleaseBuffer(frames_available, 0) {
            error_callback(windows_err_to_cpal_err(err));
            return ControlFlow::Break;
        }
    }

    ControlFlow::Continue
}

/// Convert the given duration in frames at the given sample rate to a `Duration`.
fn frames_to_duration(frames: FrameCount, rate: SampleRate) -> Duration {
    let secsf = frames as f64 / rate as f64;
    let secs = secsf as u64;
    let nanos = ((secsf - secs as f64) * 1_000_000_000.0) as u32;
    Duration::new(secs, nanos)
}

/// Use the stream's `IAudioClock` to produce the current stream instant.
///
/// Uses the QPC position produced via the `GetPosition` method.
fn stream_instant(stream: &StreamInner) -> Result<crate::StreamInstant, StreamError> {
    let mut position: u64 = 0;
    let mut qpc_position: u64 = 0;
    unsafe {
        stream
            .audio_clock
            .GetPosition(&mut position, Some(&mut qpc_position))
            .map_err(windows_err_to_cpal_err::<StreamError>)?;
    };
    // The `qpc_position` is in 100 nanosecond units. Convert it to nanoseconds.
    let qpc_nanos = qpc_position as i128 * 100;
    let instant = crate::StreamInstant::from_nanos_i128(qpc_nanos)
        .expect("performance counter out of range of `StreamInstant` representation");
    Ok(instant)
}

/// Produce the input stream timestamp.
///
/// `buffer_qpc_position` is the `qpc_position` returned via the `GetBuffer` call on the capture
/// client. It represents the instant at which the first sample of the retrieved buffer was
/// captured.
fn input_timestamp(
    stream: &StreamInner,
    buffer_qpc_position: u64,
) -> Result<crate::InputStreamTimestamp, StreamError> {
    // The `qpc_position` is in 100 nanosecond units. Convert it to nanoseconds.
    let qpc_nanos = buffer_qpc_position as i128 * 100;
    let capture = crate::StreamInstant::from_nanos_i128(qpc_nanos)
        .expect("performance counter out of range of `StreamInstant` representation");
    let callback = stream_instant(stream)?;
    Ok(crate::InputStreamTimestamp { capture, callback })
}

/// Produce the output stream timestamp.
///
/// `frames_available` is the number of frames available for writing as reported by subtracting the
/// result of `GetCurrentPadding` from the maximum buffer size.
///
/// `sample_rate` is the rate at which audio frames are processed by the device.
fn output_timestamp(
    stream: &StreamInner,
    frames_available: FrameCount,
    sample_rate: SampleRate,
) -> Result<crate::OutputStreamTimestamp, StreamError> {
    let callback = stream_instant(stream)?;
    // `padding` is the number of frames already queued in the endpoint buffer ahead of the
    // frames we are about to write. Those frames must drain before ours are heard.
    let padding = stream.max_frames_in_buffer - frames_available;
    let playback = callback
        .add(frames_to_duration(padding, sample_rate) + stream.stream_latency)
        .expect("`playback` occurs beyond representation supported by `StreamInstant`");
    Ok(crate::OutputStreamTimestamp { callback, playback })
}
```

## File: `src/host/webaudio/mod.rs`
```rust
//! Web Audio backend implementation.
//!
//! Default backend on WebAssembly.

extern crate js_sys;
extern crate wasm_bindgen;
extern crate web_sys;

use self::wasm_bindgen::prelude::*;
use self::wasm_bindgen::JsCast;
use self::web_sys::{AudioContext, AudioContextOptions};
use crate::traits::{DeviceTrait, HostTrait, StreamTrait};
use crate::{
    BackendSpecificError, BufferSize, BuildStreamError, Data, DefaultStreamConfigError,
    DeviceDescription, DeviceDescriptionBuilder, DeviceId, DeviceIdError, DeviceNameError,
    DevicesError, InputCallbackInfo, OutputCallbackInfo, PauseStreamError, PlayStreamError,
    SampleFormat, SampleRate, StreamConfig, StreamError, SupportedBufferSize,
    SupportedStreamConfig, SupportedStreamConfigRange, SupportedStreamConfigsError,
};
use std::ops::DerefMut;
use std::sync::{Arc, Mutex, RwLock};
use std::time::Duration;

/// Type alias for shared closure handles used in audio callbacks
type ClosureHandle = Arc<RwLock<Option<Closure<dyn FnMut()>>>>;

/// Content is false if the iterator is empty.
pub struct Devices(bool);

#[derive(Clone, Debug, PartialEq, Eq, Hash)]
pub struct Device;

pub struct Host;

pub struct Stream {
    ctx: Arc<AudioContext>,
    on_ended_closures: Vec<ClosureHandle>,
    config: StreamConfig,
    buffer_size_frames: usize,
}

// WASM runs in a single-threaded environment, so Send and Sync are safe by design.
unsafe impl Send for Stream {}
unsafe impl Sync for Stream {}

// Compile-time assertion that Stream is Send and Sync
crate::assert_stream_send!(Stream);
crate::assert_stream_sync!(Stream);

pub use crate::iter::{SupportedInputConfigs, SupportedOutputConfigs};

const MIN_CHANNELS: u16 = 1;
const MAX_CHANNELS: u16 = 32;
const MIN_SAMPLE_RATE: SampleRate = 8_000;
const MAX_SAMPLE_RATE: SampleRate = 96_000;
const DEFAULT_SAMPLE_RATE: SampleRate = 44_100;
const MIN_BUFFER_SIZE: u32 = 1;
const MAX_BUFFER_SIZE: u32 = u32::MAX;
const DEFAULT_BUFFER_SIZE: usize = 2048;
const SUPPORTED_SAMPLE_FORMAT: SampleFormat = SampleFormat::F32;

impl Host {
    pub fn new() -> Result<Self, crate::HostUnavailable> {
        Ok(Host)
    }
}

impl HostTrait for Host {
    type Devices = Devices;
    type Device = Device;

    fn is_available() -> bool {
        // Assume this host is always available on webaudio.
        true
    }

    fn devices(&self) -> Result<Self::Devices, DevicesError> {
        Devices::new()
    }

    fn default_input_device(&self) -> Option<Self::Device> {
        default_input_device()
    }

    fn default_output_device(&self) -> Option<Self::Device> {
        default_output_device()
    }
}

impl Devices {
    fn new() -> Result<Self, DevicesError> {
        Ok(Self::default())
    }
}

impl Device {
    fn description(&self) -> Result<DeviceDescription, DeviceNameError> {
        Ok(DeviceDescriptionBuilder::new("Default Device".to_string())
            .direction(crate::DeviceDirection::Output)
            .build())
    }

    fn id(&self) -> Result<DeviceId, DeviceIdError> {
        Ok(DeviceId(
            crate::platform::HostId::WebAudio,
            "default".to_string(),
        ))
    }

    fn supported_input_configs(
        &self,
    ) -> Result<SupportedInputConfigs, SupportedStreamConfigsError> {
        // TODO
        Ok(Vec::new().into_iter())
    }

    fn supported_output_configs(
        &self,
    ) -> Result<SupportedOutputConfigs, SupportedStreamConfigsError> {
        let buffer_size = SupportedBufferSize::Range {
            min: MIN_BUFFER_SIZE,
            max: MAX_BUFFER_SIZE,
        };
        let configs: Vec<_> = (MIN_CHANNELS..=MAX_CHANNELS)
            .map(|channels| SupportedStreamConfigRange {
                channels,
                min_sample_rate: MIN_SAMPLE_RATE,
                max_sample_rate: MAX_SAMPLE_RATE,
                buffer_size,
                sample_format: SUPPORTED_SAMPLE_FORMAT,
            })
            .collect();
        Ok(configs.into_iter())
    }

    fn default_input_config(&self) -> Result<SupportedStreamConfig, DefaultStreamConfigError> {
        // TODO
        Err(DefaultStreamConfigError::StreamTypeNotSupported)
    }

    fn default_output_config(&self) -> Result<SupportedStreamConfig, DefaultStreamConfigError> {
        const EXPECT: &str = "expected at least one valid webaudio stream config";
        let config = self
            .supported_output_configs()
            .expect(EXPECT)
            .max_by(|a, b| a.cmp_default_heuristics(b))
            .unwrap()
            .with_sample_rate(DEFAULT_SAMPLE_RATE);

        Ok(config)
    }
}

impl DeviceTrait for Device {
    type SupportedInputConfigs = SupportedInputConfigs;
    type SupportedOutputConfigs = SupportedOutputConfigs;
    type Stream = Stream;

    fn description(&self) -> Result<DeviceDescription, DeviceNameError> {
        Device::description(self)
    }

    fn id(&self) -> Result<DeviceId, DeviceIdError> {
        Device::id(self)
    }

    fn supported_input_configs(
        &self,
    ) -> Result<Self::SupportedInputConfigs, SupportedStreamConfigsError> {
        Device::supported_input_configs(self)
    }

    fn supported_output_configs(
        &self,
    ) -> Result<Self::SupportedOutputConfigs, SupportedStreamConfigsError> {
        Device::supported_output_configs(self)
    }

    fn default_input_config(&self) -> Result<SupportedStreamConfig, DefaultStreamConfigError> {
        Device::default_input_config(self)
    }

    fn default_output_config(&self) -> Result<SupportedStreamConfig, DefaultStreamConfigError> {
        Device::default_output_config(self)
    }

    fn build_input_stream_raw<D, E>(
        &self,
        _config: StreamConfig,
        _sample_format: SampleFormat,
        _data_callback: D,
        _error_callback: E,
        _timeout: Option<Duration>,
    ) -> Result<Self::Stream, BuildStreamError>
    where
        D: FnMut(&Data, &InputCallbackInfo) + Send + 'static,
        E: FnMut(StreamError) + Send + 'static,
    {
        // TODO
        Err(BuildStreamError::StreamConfigNotSupported)
    }

    /// Create an output stream.
    fn build_output_stream_raw<D, E>(
        &self,
        config: StreamConfig,
        sample_format: SampleFormat,
        data_callback: D,
        _error_callback: E,
        _timeout: Option<Duration>,
    ) -> Result<Self::Stream, BuildStreamError>
    where
        D: FnMut(&mut Data, &OutputCallbackInfo) + Send + 'static,
        E: FnMut(StreamError) + Send + 'static,
    {
        if !valid_config(config, sample_format) {
            return Err(BuildStreamError::StreamConfigNotSupported);
        }

        let n_channels = config.channels as usize;

        let buffer_size_frames = match config.buffer_size {
            BufferSize::Fixed(v) => {
                if !(MIN_BUFFER_SIZE..=MAX_BUFFER_SIZE).contains(&v) {
                    return Err(BuildStreamError::StreamConfigNotSupported);
                }
                v as usize
            }
            BufferSize::Default => DEFAULT_BUFFER_SIZE,
        };
        let buffer_size_samples = buffer_size_frames * n_channels;
        let buffer_time_step_secs = buffer_time_step_secs(buffer_size_frames, config.sample_rate);

        let data_callback = Arc::new(Mutex::new(Box::new(data_callback)));

        // Create the WebAudio stream.
        let stream_opts = AudioContextOptions::new();
        stream_opts.set_sample_rate(config.sample_rate as f32);
        let ctx = AudioContext::new_with_context_options(&stream_opts).map_err(
            |err| -> BuildStreamError {
                let description = format!("{:?}", err);
                let err = BackendSpecificError { description };
                err.into()
            },
        )?;

        let destination = ctx.destination();

        // If possible, set the destination's channel_count to the given config.channel.
        // If not, fallback on the default destination channel_count to keep previous behavior
        // and do not return an error.
        if config.channels as u32 <= destination.max_channel_count() {
            destination.set_channel_count(config.channels as u32);
        }

        // SAFETY: WASM is single-threaded, so Arc is safe even though AudioContext is not Send/Sync
        #[allow(clippy::arc_with_non_send_sync)]
        let ctx = Arc::new(ctx);

        // A container for managing the lifecycle of the audio callbacks.
        let mut on_ended_closures: Vec<ClosureHandle> = Vec::new();

        // A cursor keeping track of the current time at which new frames should be scheduled.
        let time = Arc::new(RwLock::new(0f64));

        // baseLatency is fixed for the lifetime of the AudioContext.
        let base_latency_secs = js_sys::Reflect::get(ctx.as_ref(), &JsValue::from("baseLatency"))
            .ok()
            .and_then(|v| v.as_f64())
            .unwrap_or(0.0);

        // Create a set of closures / callbacks which will continuously fetch and schedule sample
        // playback. Starting with two workers, e.g. a front and back buffer so that audio frames
        // can be fetched in the background.
        for _i in 0..2 {
            let data_callback_handle = data_callback.clone();
            let ctx_handle = ctx.clone();
            let time_handle = time.clone();

            // A set of temporary buffers to be used for intermediate sample transformation steps.
            let mut temporary_buffer = vec![0f32; buffer_size_samples];
            let mut temporary_channel_buffer = vec![0f32; buffer_size_frames];

            #[cfg(target_feature = "atomics")]
            let temporary_channel_array_view: js_sys::Float32Array;
            #[cfg(target_feature = "atomics")]
            {
                let temporary_channel_array = js_sys::ArrayBuffer::new(
                    (std::mem::size_of::<f32>() * buffer_size_frames) as u32,
                );
                temporary_channel_array_view = js_sys::Float32Array::new(&temporary_channel_array);
            }

            // Create a webaudio buffer which will be reused to avoid allocations.
            let ctx_buffer = ctx
                .create_buffer(
                    config.channels as u32,
                    buffer_size_frames as u32,
                    config.sample_rate as f32,
                )
                .map_err(|err| -> BuildStreamError {
                    let description = format!("{:?}", err);
                    let err = BackendSpecificError { description };
                    err.into()
                })?;

            // A self reference to this closure for passing to future audio event calls.
            // SAFETY: WASM is single-threaded, so Arc is safe even though Closure is not Send/Sync
            #[allow(clippy::arc_with_non_send_sync)]
            let on_ended_closure: ClosureHandle = Arc::new(RwLock::new(None));
            let on_ended_closure_handle = on_ended_closure.clone();

            on_ended_closure
                .write()
                .unwrap()
                .replace(Closure::wrap(Box::new(move || {
                    let now = ctx_handle.current_time();
                    let time_at_start_of_buffer = {
                        let time_at_start_of_buffer = time_handle
                            .read()
                            .expect("Unable to get a read lock on the time cursor");
                        // Synchronise first buffer as necessary (eg. keep the time value
                        // referenced to the context clock).
                        if *time_at_start_of_buffer > 0.0 {
                            *time_at_start_of_buffer
                        } else {
                            // Schedule the first buffer far enough ahead for the browser's
                            // internal audio pipeline (baseLatency) plus one full buffer of
                            // data, so playback starts underrun-free at any buffer size.
                            now + base_latency_secs + buffer_time_step_secs
                        }
                    };

                    // Populate the sample data into an interleaved temporary buffer.
                    {
                        let len = temporary_buffer.len();
                        let data = temporary_buffer.as_mut_ptr() as *mut ();
                        let mut data = unsafe { Data::from_parts(data, len, sample_format) };
                        let mut data_callback = data_callback_handle.lock().unwrap();
                        // outputLatency can change at runtime, so read it each callback.
                        let output_latency_secs = js_sys::Reflect::get(
                            ctx_handle.as_ref(),
                            &JsValue::from("outputLatency"),
                        )
                        .ok()
                        .and_then(|v| v.as_f64())
                        .unwrap_or(0.0);
                        let total_hw_latency_secs = {
                            let sum = base_latency_secs + output_latency_secs;
                            if sum.is_finite() {
                                sum.max(0.0)
                            } else {
                                0.0
                            }
                        };
                        let callback = crate::StreamInstant::from_secs_f64(now);
                        let playback = crate::StreamInstant::from_secs_f64(
                            time_at_start_of_buffer + total_hw_latency_secs,
                        );
                        let timestamp = crate::OutputStreamTimestamp { callback, playback };
                        let info = OutputCallbackInfo { timestamp };
                        (data_callback.deref_mut())(&mut data, &info);
                    }

                    // Deinterleave the sample data and copy into the audio context buffer.
                    // We do not reference the audio context buffer directly e.g. getChannelData.
                    // As wasm-bindgen only gives us a copy, not a direct reference.
                    for channel in 0..n_channels {
                        for i in 0..buffer_size_frames {
                            temporary_channel_buffer[i] =
                                temporary_buffer[n_channels * i + channel];
                        }

                        #[cfg(not(target_feature = "atomics"))]
                        {
                            ctx_buffer
                                .copy_to_channel(&temporary_channel_buffer, channel as i32)
                                .expect(
                                    "Unable to write sample data into the audio context buffer",
                                );
                        }

                        // copyToChannel cannot be directly copied into from a SharedArrayBuffer,
                        // which WASM memory is backed by if the 'atomics' flag is enabled.
                        // This workaround copies the data into an intermediary buffer first.
                        // There's a chance browsers may eventually relax that requirement.
                        // See this issue: https://github.com/WebAudio/web-audio-api/issues/2565
                        #[cfg(target_feature = "atomics")]
                        {
                            temporary_channel_array_view.copy_from(&temporary_channel_buffer);
                            ctx_buffer
                                .unchecked_ref::<ExternalArrayAudioBuffer>()
                                .copy_to_channel(&temporary_channel_array_view, channel as i32)
                                .expect(
                                    "Unable to write sample data into the audio context buffer",
                                );
                        }
                    }

                    // Create an AudioBufferSourceNode, schedule it to playback the reused buffer
                    // in the future.
                    let source = ctx_handle
                        .create_buffer_source()
                        .expect("Unable to create a webaudio buffer source");
                    source.set_buffer(Some(&ctx_buffer));
                    source
                        .connect_with_audio_node(&ctx_handle.destination())
                        .expect(
                        "Unable to connect the web audio buffer source to the context destination",
                    );
                    source
                        .add_event_listener_with_callback(
                            "ended",
                            on_ended_closure_handle
                                .read()
                                .unwrap()
                                .as_ref()
                                .unwrap()
                                .as_ref()
                                .unchecked_ref(),
                        )
                        .expect("Failed to add ended event listener");

                    source
                        .start_with_when(time_at_start_of_buffer)
                        .expect("Unable to start the webaudio buffer source");

                    // Keep track of when the next buffer worth of samples should be played.
                    *time_handle.write().unwrap() = time_at_start_of_buffer + buffer_time_step_secs;
                }) as Box<dyn FnMut()>));

            on_ended_closures.push(on_ended_closure);
        }

        Ok(Stream {
            ctx,
            on_ended_closures,
            config,
            buffer_size_frames,
        })
    }
}

impl Stream {
    /// Return the [`AudioContext`](https://developer.mozilla.org/docs/Web/API/AudioContext) used
    /// by this stream.
    pub fn audio_context(&self) -> &AudioContext {
        &self.ctx
    }
}

impl StreamTrait for Stream {
    fn play(&self) -> Result<(), PlayStreamError> {
        let window = web_sys::window().unwrap();
        match self.ctx.resume() {
            Ok(_) => {
                // Begin webaudio playback, initially scheduling the closures to fire on a timeout
                // event.
                let mut offset_ms = 10;
                let time_step_secs =
                    buffer_time_step_secs(self.buffer_size_frames, self.config.sample_rate);
                let time_step_ms = (time_step_secs * 1_000.0) as i32;
                for on_ended_closure in self.on_ended_closures.iter() {
                    window
                        .set_timeout_with_callback_and_timeout_and_arguments_0(
                            on_ended_closure
                                .read()
                                .unwrap()
                                .as_ref()
                                .unwrap()
                                .as_ref()
                                .unchecked_ref(),
                            offset_ms,
                        )
                        .unwrap();
                    offset_ms += time_step_ms;
                }
                Ok(())
            }
            Err(err) => {
                let description = format!("{:?}", err);
                let err = BackendSpecificError { description };
                Err(err.into())
            }
        }
    }

    fn pause(&self) -> Result<(), PauseStreamError> {
        match self.ctx.suspend() {
            Ok(_) => Ok(()),
            Err(err) => {
                let description = format!("{:?}", err);
                let err = BackendSpecificError { description };
                Err(err.into())
            }
        }
    }

    fn buffer_size(&self) -> Option<crate::FrameCount> {
        Some(self.buffer_size_frames as crate::FrameCount)
    }
}

impl Drop for Stream {
    fn drop(&mut self) {
        let _ = self.ctx.close();
    }
}

impl Default for Devices {
    fn default() -> Devices {
        // We produce an empty iterator if the WebAudio API isn't available.
        Devices(is_webaudio_available())
    }
}

impl Iterator for Devices {
    type Item = Device;

    #[inline]
    fn next(&mut self) -> Option<Device> {
        if self.0 {
            self.0 = false;
            Some(Device)
        } else {
            None
        }
    }
}

fn default_input_device() -> Option<Device> {
    // TODO
    None
}

fn default_output_device() -> Option<Device> {
    if is_webaudio_available() {
        Some(Device)
    } else {
        None
    }
}

// Detects whether the `AudioContext` global variable is available.
fn is_webaudio_available() -> bool {
    js_sys::Reflect::get(&js_sys::global(), &JsValue::from("AudioContext"))
        .unwrap()
        .is_truthy()
}

// Whether or not the given stream configuration is valid for building a stream.
fn valid_config(conf: StreamConfig, sample_format: SampleFormat) -> bool {
    conf.channels <= MAX_CHANNELS
        && conf.channels >= MIN_CHANNELS
        && conf.sample_rate <= MAX_SAMPLE_RATE
        && conf.sample_rate >= MIN_SAMPLE_RATE
        && sample_format == SUPPORTED_SAMPLE_FORMAT
}

fn buffer_time_step_secs(buffer_size_frames: usize, sample_rate: SampleRate) -> f64 {
    buffer_size_frames as f64 / sample_rate as f64
}

#[cfg(target_feature = "atomics")]
#[wasm_bindgen]
extern "C" {
    #[wasm_bindgen(js_name = AudioBuffer)]
    type ExternalArrayAudioBuffer;

    # [wasm_bindgen(catch, method, structural, js_class = "AudioBuffer", js_name = copyToChannel)]
    pub fn copy_to_channel(
        this: &ExternalArrayAudioBuffer,
        source: &js_sys::Float32Array,
        channel_number: i32,
    ) -> Result<(), JsValue>;
}
```

## File: `src/platform/mod.rs`
```rust
//! Platform-specific items.
//!
//! This module also contains the implementation of the platform's dynamically dispatched [`Host`]
//! type and its associated [`Device`], [`Stream`] and other associated types. These
//! types are useful in the case that users require switching between audio host APIs at runtime.

#[doc(inline)]
pub use self::platform_impl::*;

#[cfg(feature = "custom")]
pub use crate::host::custom::{Device as CustomDevice, Host as CustomHost, Stream as CustomStream};

/// A macro to assist with implementing a platform's dynamically dispatched [`Host`] type.
///
/// These dynamically dispatched types are necessary to allow for users to switch between hosts at
/// runtime.
///
/// For example the invocation `impl_platform_host(Wasapi wasapi "WASAPI", Asio asio "ASIO")`,
/// this macro should expand to:
///
// This sample code block is marked as text because it's not a valid test,
// it's just illustrative. (see rust issue #96573)
/// ```text
/// pub enum HostId {
///     Wasapi,
///     Asio,
/// }
///
/// pub enum Host {
///     Wasapi(crate::host::wasapi::Host),
///     Asio(crate::host::asio::Host),
/// }
/// ```
///
/// And so on for Device, Devices, Host, Stream, SupportedInputConfigs,
/// SupportedOutputConfigs and all their necessary trait implementations.
///
macro_rules! impl_platform_host {
    ($($(#[cfg($feat: meta)])? $HostVariant:ident => $Host:ty),* $(,)?) => {
        /// All hosts supported by CPAL on this platform.
        pub const ALL_HOSTS: &'static [HostId] = &[
            $(
                $(#[cfg($feat)])?
                HostId::$HostVariant,
            )*
        ];

        /// The platform's dynamically dispatched `Host` type.
        ///
        /// An instance of this `Host` type may represent one of the `Host`s available
        /// on the platform.
        ///
        /// Use this type if you require switching between available hosts at runtime.
        ///
        /// This type may be constructed via the [`host_from_id`] function. [`HostId`]s may
        /// be acquired via the [`ALL_HOSTS`] const, and the [`available_hosts`] function.
        pub struct Host(HostInner);

        /// The `Device` implementation associated with the platform's dynamically dispatched
        /// [`Host`] type.
        #[derive(Clone)]
        pub struct Device(DeviceInner);

        /// The `Devices` iterator associated with the platform's dynamically dispatched [`Host`]
        /// type.
        pub struct Devices(DevicesInner);

        /// The `Stream` implementation associated with the platform's dynamically dispatched
        /// [`Host`] type.
        #[must_use = "If the stream is not stored it will not play."]
        pub struct Stream(StreamInner);

        /// The `SupportedInputConfigs` iterator associated with the platform's dynamically
        /// dispatched [`Host`] type.
        #[derive(Clone)]
        pub struct SupportedInputConfigs(SupportedInputConfigsInner);

        /// The `SupportedOutputConfigs` iterator associated with the platform's dynamically
        /// dispatched [`Host`] type.
        #[derive(Clone)]
        pub struct SupportedOutputConfigs(SupportedOutputConfigsInner);

        /// Unique identifier for available hosts on the platform.
        ///
        /// Only the hosts supported by the current platform are available as enum variants.
        /// For cross-platform code that needs to handle hosts from other platforms,
        /// use the string representation via [`std::fmt::Display`]/[`std::str::FromStr`].
        ///
        /// # Available Host Strings
        ///
        /// For cross-platform matching, these host strings are available:
        ///
        /// - `"aaudio"` - Android Audio
        /// - `"alsa"` - Advanced Linux Sound Architecture
        /// - `"asio"` - ASIO
        /// - `"coreaudio"` - CoreAudio
        /// - `"custom"` - Custom host (requires `custom` feature)
        /// - `"emscripten"` - Emscripten
        /// - `"jack"` - JACK Audio Connection Kit
        /// - `"null"` - Null host
        /// - `"wasapi"` - Windows Audio Session API
        /// - `"webaudio"` - Web Audio API
        /// - `"audioworklet"` - Audio Worklet
        ///
        /// # Cross-Platform Example
        ///
        /// ```
        /// use cpal::HostId;
        /// use std::str::FromStr;
        ///
        /// fn handle_host_string(host_string: &str) {
        ///     // String matching works on all platforms
        ///     match host_string {
        ///         "alsa" => println!("ALSA host"),
        ///         "coreaudio" => println!("CoreAudio host"),
        ///         "jack" => println!("JACK host"),
        ///         "wasapi" => println!("WASAPI host"),
        ///         "asio" => println!("ASIO host"),
        ///         "aaudio" => println!("AAudio host"),
        ///         _ => println!("Other host"),
        ///     }
        ///
        ///     // Parse host string (may fail if host is not available on this platform)
        ///     if let Ok(host_id) = HostId::from_str(host_string) {
        ///         println!("Successfully parsed: {}", host_id);
        ///     }
        /// }
        /// ```
        #[derive(Copy, Clone, Debug, Eq, Hash, PartialEq)]
        pub enum HostId {
            $(
                $(#[cfg($feat)])?
                $(#[cfg_attr(docsrs, doc(cfg($feat)))])?
                $HostVariant,
            )*
        }

        /// Contains a platform specific [`Device`] implementation.
        #[derive(Clone)]
        #[allow(clippy::large_enum_variant)]
        pub enum DeviceInner {
            $(
                $(#[cfg($feat)])?
                $HostVariant(<$Host as crate::traits::HostTrait>::Device),
            )*
        }

        /// Contains a platform specific [`Devices`] implementation.
        pub enum DevicesInner {
            $(
                $(#[cfg($feat)])?
                $HostVariant(<$Host as crate::traits::HostTrait>::Devices),
            )*
        }

        /// Contains a platform specific [`Host`] implementation.
        pub enum HostInner {
            $(
                $(#[cfg($feat)])?
                $HostVariant($Host),
            )*
        }

        /// Contains a platform specific [`Stream`] implementation.
        pub enum StreamInner {
            $(
                $(#[cfg($feat)])?
                $HostVariant(<<$Host as crate::traits::HostTrait>::Device as crate::traits::DeviceTrait>::Stream),
            )*
        }

        #[derive(Clone)]
        enum SupportedInputConfigsInner {
            $(
                $(#[cfg($feat)])?
                $HostVariant(<<$Host as crate::traits::HostTrait>::Device as crate::traits::DeviceTrait>::SupportedInputConfigs),
            )*
        }

        #[derive(Clone)]
        enum SupportedOutputConfigsInner {
            $(
                $(#[cfg($feat)])?
                $HostVariant(<<$Host as crate::traits::HostTrait>::Device as crate::traits::DeviceTrait>::SupportedOutputConfigs),
            )*
        }

        impl HostId {
            pub fn name(&self) -> &'static str {
                match self {
                    $(
                        $(#[cfg($feat)])?
                        HostId::$HostVariant => stringify!($HostVariant),
                    )*
                }
            }
        }

        impl std::fmt::Display for HostId {
            fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
                write!(f, "{}", self.name().to_lowercase())
            }
        }

        impl std::str::FromStr for HostId {
            type Err = crate::HostUnavailable;

            fn from_str(s: &str) -> Result<Self, Self::Err> {
                $(
                    $(#[cfg($feat)])?
                    if stringify!($HostVariant).eq_ignore_ascii_case(s) {
                        return Ok(HostId::$HostVariant);
                    }
                )*
                Err(crate::HostUnavailable)
            }
        }

        impl Devices {
            /// Returns a reference to the underlying platform specific implementation of this
            /// `Devices`.
            pub fn as_inner(&self) -> &DevicesInner {
                &self.0
            }

            /// Returns a mutable reference to the underlying platform specific implementation of
            /// this `Devices`.
            pub fn as_inner_mut(&mut self) -> &mut DevicesInner {
                &mut self.0
            }

            /// Returns the underlying platform specific implementation of this `Devices`.
            pub fn into_inner(self) -> DevicesInner {
                self.0
            }
        }

        impl Device {
            /// Returns a reference to the underlying platform specific implementation of this
            /// `Device`.
            pub fn as_inner(&self) -> &DeviceInner {
                &self.0
            }

            /// Returns a mutable reference to the underlying platform specific implementation of
            /// this `Device`.
            pub fn as_inner_mut(&mut self) -> &mut DeviceInner {
                &mut self.0
            }

            /// Returns the underlying platform specific implementation of this `Device`.
            pub fn into_inner(self) -> DeviceInner {
                self.0
            }
        }

        impl Host {
            /// The unique identifier associated with this `Host`.
            pub fn id(&self) -> HostId {
                match self.0 {
                    $(
                        $(#[cfg($feat)])?
                        HostInner::$HostVariant(_) => HostId::$HostVariant,
                    )*
                }
            }

            /// Returns a reference to the underlying platform specific implementation of this
            /// `Host`.
            pub fn as_inner(&self) -> &HostInner {
                &self.0
            }

            /// Returns a mutable reference to the underlying platform specific implementation of
            /// this `Host`.
            pub fn as_inner_mut(&mut self) -> &mut HostInner {
                &mut self.0
            }

            /// Returns the underlying platform specific implementation of this `Host`.
            pub fn into_inner(self) -> HostInner {
                self.0
            }
        }

        impl Stream {
            /// Returns a reference to the underlying platform specific implementation of this
            /// `Stream`.
            pub fn as_inner(&self) -> &StreamInner {
                &self.0
            }

            /// Returns a mutable reference to the underlying platform specific implementation of
            /// this `Stream`.
            pub fn as_inner_mut(&mut self) -> &mut StreamInner {
                &mut self.0
            }

            /// Returns the underlying platform specific implementation of this `Stream`.
            pub fn into_inner(self) -> StreamInner {
                self.0
            }
        }

        impl Iterator for Devices {
            type Item = Device;

            fn next(&mut self) -> Option<Self::Item> {
                match self.0 {
                    $(
                        $(#[cfg($feat)])?
                        DevicesInner::$HostVariant(ref mut d) => {
                            d.next().map(DeviceInner::$HostVariant).map(Device::from)
                        }
                    )*
                }
            }

            fn size_hint(&self) -> (usize, Option<usize>) {
                match self.0 {
                    $(
                        $(#[cfg($feat)])?
                        DevicesInner::$HostVariant(ref d) => d.size_hint(),
                    )*
                }
            }
        }

        impl Iterator for SupportedInputConfigs {
            type Item = crate::SupportedStreamConfigRange;

            fn next(&mut self) -> Option<Self::Item> {
                match self.0 {
                    $(
                        $(#[cfg($feat)])?
                        SupportedInputConfigsInner::$HostVariant(ref mut s) => s.next(),
                    )*
                }
            }

            fn size_hint(&self) -> (usize, Option<usize>) {
                match self.0 {
                    $(
                        $(#[cfg($feat)])?
                        SupportedInputConfigsInner::$HostVariant(ref d) => d.size_hint(),
                    )*
                }
            }
        }

        impl Iterator for SupportedOutputConfigs {
            type Item = crate::SupportedStreamConfigRange;

            fn next(&mut self) -> Option<Self::Item> {
                match self.0 {
                    $(
                        $(#[cfg($feat)])?
                        SupportedOutputConfigsInner::$HostVariant(ref mut s) => s.next(),
                    )*
                }
            }

            fn size_hint(&self) -> (usize, Option<usize>) {
                match self.0 {
                    $(
                        $(#[cfg($feat)])?
                        SupportedOutputConfigsInner::$HostVariant(ref d) => d.size_hint(),
                    )*
                }
            }
        }

        impl crate::traits::DeviceTrait for Device {
            type SupportedInputConfigs = SupportedInputConfigs;
            type SupportedOutputConfigs = SupportedOutputConfigs;
            type Stream = Stream;

            #[allow(deprecated)]
            fn name(&self) -> Result<String, crate::DeviceNameError> {
                match self.0 {
                    $(
                        $(#[cfg($feat)])?
                        DeviceInner::$HostVariant(ref d) => d.name(),
                    )*
                }
            }

            fn description(&self) -> Result<crate::DeviceDescription, crate::DeviceNameError> {
                match self.0 {
                    $(
                        $(#[cfg($feat)])?
                        DeviceInner::$HostVariant(ref d) => d.description(),
                    )*
                }
            }

            fn id(&self) -> Result<crate::DeviceId, crate::DeviceIdError> {
                match self.0 {
                    $(
                        $(#[cfg($feat)])?
                        DeviceInner::$HostVariant(ref d) => d.id(),
                    )*
                }
            }

            fn supports_input(&self) -> bool {
                match self.0 {
                    $(
                        $(#[cfg($feat)])?
                        DeviceInner::$HostVariant(ref d) => d.supports_input(),
                    )*
                }
            }

            fn supports_output(&self) -> bool {
                match self.0 {
                    $(
                        $(#[cfg($feat)])?
                        DeviceInner::$HostVariant(ref d) => d.supports_output(),
                    )*
                }
            }

            fn supported_input_configs(&self) -> Result<Self::SupportedInputConfigs, crate::SupportedStreamConfigsError> {
                match self.0 {
                    $(
                        $(#[cfg($feat)])?
                        DeviceInner::$HostVariant(ref d) => {
                            d.supported_input_configs()
                                .map(SupportedInputConfigsInner::$HostVariant)
                                .map(SupportedInputConfigs)
                        }
                    )*
                }
            }

            fn supported_output_configs(&self) -> Result<Self::SupportedOutputConfigs, crate::SupportedStreamConfigsError> {
                match self.0 {
                    $(
                        $(#[cfg($feat)])?
                        DeviceInner::$HostVariant(ref d) => {
                            d.supported_output_configs()
                                .map(SupportedOutputConfigsInner::$HostVariant)
                                .map(SupportedOutputConfigs)
                        }
                    )*
                }
            }

            fn default_input_config(&self) -> Result<crate::SupportedStreamConfig, crate::DefaultStreamConfigError> {
                match self.0 {
                    $(
                        $(#[cfg($feat)])?
                        DeviceInner::$HostVariant(ref d) => d.default_input_config(),
                    )*
                }
            }

            fn default_output_config(&self) -> Result<crate::SupportedStreamConfig, crate::DefaultStreamConfigError> {
                match self.0 {
                    $(
                        $(#[cfg($feat)])?
                        DeviceInner::$HostVariant(ref d) => d.default_output_config(),
                    )*
                }
            }

            fn build_input_stream_raw<D, E>(
                &self,
                config: crate::StreamConfig,
                sample_format: crate::SampleFormat,
                data_callback: D,
                error_callback: E,
                timeout: Option<std::time::Duration>,
            ) -> Result<Self::Stream, crate::BuildStreamError>
            where
                D: FnMut(&crate::Data, &crate::InputCallbackInfo) + Send + 'static,
                E: FnMut(crate::StreamError) + Send + 'static,
            {
                match self.0 {
                    $(
                        $(#[cfg($feat)])?
                        DeviceInner::$HostVariant(ref d) => d
                            .build_input_stream_raw(
                                config,
                                sample_format,
                                data_callback,
                                error_callback,
                                timeout,
                            )
                            .map(StreamInner::$HostVariant)
                            .map(Stream::from),
                    )*
                }
            }

            fn build_output_stream_raw<D, E>(
                &self,
                config: crate::StreamConfig,
                sample_format: crate::SampleFormat,
                data_callback: D,
                error_callback: E,
                timeout: Option<std::time::Duration>,
            ) -> Result<Self::Stream, crate::BuildStreamError>
            where
                D: FnMut(&mut crate::Data, &crate::OutputCallbackInfo) + Send + 'static,
                E: FnMut(crate::StreamError) + Send + 'static,
            {
                match self.0 {
                    $(
                        $(#[cfg($feat)])?
                        DeviceInner::$HostVariant(ref d) => d
                            .build_output_stream_raw(
                                config,
                                sample_format,
                                data_callback,
                                error_callback,
                                timeout,
                            )
                            .map(StreamInner::$HostVariant)
                            .map(Stream::from),
                    )*
                }
            }
        }

        impl crate::traits::HostTrait for Host {
            type Devices = Devices;
            type Device = Device;

            fn is_available() -> bool {
                $(
                    $(#[cfg($feat)])?
                    if <$Host>::is_available() { return true; }
                )*
                false
            }

            fn devices(&self) -> Result<Self::Devices, crate::DevicesError> {
                match self.0 {
                    $(
                        $(#[cfg($feat)])?
                        HostInner::$HostVariant(ref h) => {
                            h.devices().map(DevicesInner::$HostVariant).map(Devices::from)
                        }
                    )*
                }
            }

            fn device_by_id(&self, id: &crate::DeviceId) -> Option<Self::Device> {
                match self.0 {
                    $(
                        $(#[cfg($feat)])?
                        HostInner::$HostVariant(ref h) => {
                            h.device_by_id(id).map(DeviceInner::$HostVariant).map(Device::from)
                        }
                    )*
                }
            }

            fn default_input_device(&self) -> Option<Self::Device> {
                match self.0 {
                    $(
                        $(#[cfg($feat)])?
                        HostInner::$HostVariant(ref h) => {
                            h.default_input_device().map(DeviceInner::$HostVariant).map(Device::from)
                        }
                    )*
                }
            }

            fn default_output_device(&self) -> Option<Self::Device> {
                match self.0 {
                    $(
                        $(#[cfg($feat)])?
                        HostInner::$HostVariant(ref h) => {
                            h.default_output_device().map(DeviceInner::$HostVariant).map(Device::from)
                        }
                    )*
                }
            }
        }

        impl crate::traits::StreamTrait for Stream {
            fn play(&self) -> Result<(), crate::PlayStreamError> {
                match self.0 {
                    $(
                        $(#[cfg($feat)])?
                        StreamInner::$HostVariant(ref s) => {
                            s.play()
                        }
                    )*
                }
            }

            fn pause(&self) -> Result<(), crate::PauseStreamError> {
                match self.0 {
                    $(
                        $(#[cfg($feat)])?
                        StreamInner::$HostVariant(ref s) => {
                            s.pause()
                        }
                    )*
                }
            }

            fn buffer_size(&self) -> Option<crate::FrameCount> {
                match self.0 {
                    $(
                        $(#[cfg($feat)])?
                        StreamInner::$HostVariant(ref s) => {
                            s.buffer_size()
                        }
                    )*
                }
            }
        }

        impl From<DeviceInner> for Device {
            fn from(d: DeviceInner) -> Self {
                Device(d)
            }
        }

        impl From<DevicesInner> for Devices {
            fn from(d: DevicesInner) -> Self {
                Devices(d)
            }
        }

        impl From<HostInner> for Host {
            fn from(h: HostInner) -> Self {
                Host(h)
            }
        }

        impl From<StreamInner> for Stream {
            fn from(s: StreamInner) -> Self {
                Stream(s)
            }
        }

        $(
            $(#[cfg($feat)])?
            impl From<<$Host as crate::traits::HostTrait>::Device> for Device {
                fn from(h: <$Host as crate::traits::HostTrait>::Device) -> Self {
                    DeviceInner::$HostVariant(h).into()
                }
            }

            $(#[cfg($feat)])?
            impl From<<$Host as crate::traits::HostTrait>::Devices> for Devices {
                fn from(h: <$Host as crate::traits::HostTrait>::Devices) -> Self {
                    DevicesInner::$HostVariant(h).into()
                }
            }

            $(#[cfg($feat)])?
            impl From<$Host> for Host {
                fn from(h: $Host) -> Self {
                    HostInner::$HostVariant(h).into()
                }
            }

            $(#[cfg($feat)])?
            impl From<<<$Host as crate::traits::HostTrait>::Device as crate::traits::DeviceTrait>::Stream> for Stream {
                fn from(h: <<$Host as crate::traits::HostTrait>::Device as crate::traits::DeviceTrait>::Stream) -> Self {
                    StreamInner::$HostVariant(h).into()
                }
            }
        )*

        /// Produces a list of hosts that are currently available on the system.
        pub fn available_hosts() -> Vec<HostId> {
            let mut host_ids = vec![];
            $(
                $(#[cfg($feat)])?
                if <$Host as crate::traits::HostTrait>::is_available() {
                    host_ids.push(HostId::$HostVariant);
                }
            )*
            host_ids
        }

        /// Given a unique host identifier, initialise and produce the host if it is available.
        pub fn host_from_id(id: HostId) -> Result<Host, crate::HostUnavailable> {
            match id {
                $(
                    $(#[cfg($feat)])?
                    HostId::$HostVariant => {
                        <$Host>::new()
                            .map(HostInner::$HostVariant)
                            .map(Host::from)
                    }
                )*
            }
        }

        impl Default for Host {
            fn default() -> Host {
                default_host()
            }
        }
    };
}

#[cfg(any(
    target_os = "linux",
    target_os = "dragonfly",
    target_os = "freebsd",
    target_os = "netbsd"
))]
mod platform_impl {
    #[cfg_attr(
        docsrs,
        doc(cfg(any(
            target_os = "linux",
            target_os = "dragonfly",
            target_os = "freebsd",
            target_os = "netbsd"
        )))
    )]
    pub use crate::host::alsa::Host as AlsaHost;
    #[cfg(feature = "jack")]
    #[cfg_attr(
        docsrs,
        doc(cfg(all(
            any(
                target_os = "linux",
                target_os = "dragonfly",
                target_os = "freebsd",
                target_os = "netbsd"
            ),
            feature = "jack"
        )))
    )]
    pub use crate::host::jack::Host as JackHost;
    #[cfg(feature = "pipewire")]
    #[cfg_attr(
        docsrs,
        doc(cfg(all(
            any(
                target_os = "linux",
                target_os = "dragonfly",
                target_os = "freebsd",
                target_os = "netbsd"
            ),
            feature = "pipewire"
        )))
    )]
    pub use crate::host::pipewire::Host as PipeWireHost;
    #[cfg(feature = "pulseaudio")]
    #[cfg_attr(
        docsrs,
        doc(cfg(all(
            any(
                target_os = "linux",
                target_os = "dragonfly",
                target_os = "freebsd",
                target_os = "netbsd"
            ),
            feature = "pulseaudio"
        )))
    )]
    pub use crate::host::pulseaudio::Host as PulseAudioHost;
    impl_platform_host!(
        #[cfg(feature = "pipewire")] PipeWire => PipeWireHost,
        #[cfg(feature = "pulseaudio")] PulseAudio => PulseAudioHost,
        #[cfg(feature = "jack")] Jack => JackHost,
        Alsa => AlsaHost,
        #[cfg(feature = "custom")] Custom => super::CustomHost,
    );

    /// The default host for the current compilation target platform.
    pub fn default_host() -> Host {
        #[cfg(feature = "pipewire")]
        if <PipeWireHost as crate::traits::HostTrait>::is_available() {
            if let Ok(host) = PipeWireHost::new() {
                return host.into();
            }
        }
        #[cfg(feature = "pulseaudio")]
        if <PulseAudioHost as crate::traits::HostTrait>::is_available() {
            if let Ok(host) = PulseAudioHost::new() {
                return host.into();
            }
        }
        AlsaHost::new()
            .expect("the default host should always be available")
            .into()
    }
}

#[cfg(any(target_os = "macos", target_os = "ios"))]
mod platform_impl {
    #[cfg_attr(docsrs, doc(cfg(any(target_os = "macos", target_os = "ios"))))]
    pub use crate::host::coreaudio::Host as CoreAudioHost;
    #[cfg(all(feature = "jack", target_os = "macos"))]
    #[cfg_attr(docsrs, doc(cfg(all(feature = "jack", target_os = "macos"))))]
    pub use crate::host::jack::Host as JackHost;

    impl_platform_host!(
        CoreAudio => CoreAudioHost,
        #[cfg(all(feature = "jack", target_os = "macos"))] Jack => JackHost,
        #[cfg(feature = "custom")] Custom => super::CustomHost
    );

    /// The default host for the current compilation target platform.
    pub fn default_host() -> Host {
        CoreAudioHost::new()
            .expect("the default host should always be available")
            .into()
    }
}

#[cfg(target_os = "emscripten")]
mod platform_impl {
    #[cfg_attr(docsrs, doc(cfg(target_os = "emscripten")))]
    pub use crate::host::emscripten::Host as EmscriptenHost;
    impl_platform_host!(
        Emscripten => EmscriptenHost,
        #[cfg(feature = "custom")] Custom => super::CustomHost
    );

    /// The default host for the current compilation target platform.
    pub fn default_host() -> Host {
        EmscriptenHost::new()
            .expect("the default host should always be available")
            .into()
    }
}

#[cfg(all(target_arch = "wasm32", feature = "wasm-bindgen"))]
mod platform_impl {
    #[cfg_attr(
        docsrs,
        doc(cfg(all(target_arch = "wasm32", feature = "wasm-bindgen")))
    )]
    pub use crate::host::webaudio::Host as WebAudioHost;

    #[cfg(feature = "audioworklet")]
    #[cfg_attr(
        docsrs,
        doc(cfg(all(
            target_arch = "wasm32",
            feature = "wasm-bindgen",
            feature = "audioworklet"
        )))
    )]
    pub use crate::host::audioworklet::Host as AudioWorkletHost;

    impl_platform_host!(
        WebAudio => WebAudioHost,
        #[cfg(feature = "audioworklet")] AudioWorklet => AudioWorkletHost,
        #[cfg(feature = "custom")] Custom => super::CustomHost
    );

    /// The default host for the current compilation target platform.
    pub fn default_host() -> Host {
        WebAudioHost::new()
            .expect("the default host should always be available")
            .into()
    }
}

#[cfg(windows)]
mod platform_impl {
    #[cfg(feature = "asio")]
    #[cfg_attr(docsrs, doc(cfg(all(windows, feature = "asio"))))]
    pub use crate::host::asio::Host as AsioHost;
    #[cfg(feature = "jack")]
    #[cfg_attr(docsrs, doc(cfg(all(windows, feature = "jack"))))]
    pub use crate::host::jack::Host as JackHost;
    #[cfg_attr(docsrs, doc(cfg(windows)))]
    pub use crate::host::wasapi::Host as WasapiHost;

    impl_platform_host!(
        #[cfg(feature = "asio")] Asio => AsioHost,
        Wasapi => WasapiHost,
        #[cfg(feature = "jack")] Jack => JackHost,
        #[cfg(feature = "custom")] Custom => super::CustomHost,
    );

    /// The default host for the current compilation target platform.
    pub fn default_host() -> Host {
        WasapiHost::new()
            .expect("the default host should always be available")
            .into()
    }
}

#[cfg(target_os = "android")]
mod platform_impl {
    #[cfg_attr(docsrs, doc(cfg(target_os = "android")))]
    pub use crate::host::aaudio::Host as AAudioHost;
    impl_platform_host!(
        AAudio => AAudioHost,
        #[cfg(feature = "custom")] Custom => super::CustomHost
    );

    /// The default host for the current compilation target platform.
    pub fn default_host() -> Host {
        AAudioHost::new()
            .expect("the default host should always be available")
            .into()
    }
}

#[cfg(not(any(
    windows,
    target_os = "linux",
    target_os = "dragonfly",
    target_os = "freebsd",
    target_os = "netbsd",
    target_os = "macos",
    target_os = "ios",
    target_os = "emscripten",
    target_os = "android",
    all(target_arch = "wasm32", feature = "wasm-bindgen"),
)))]
mod platform_impl {
    #[cfg_attr(
        docsrs,
        doc(cfg(not(any(
            windows,
            target_os = "linux",
            target_os = "dragonfly",
            target_os = "freebsd",
            target_os = "netbsd",
            target_os = "macos",
            target_os = "ios",
            target_os = "emscripten",
            target_os = "android",
            all(target_arch = "wasm32", feature = "wasm-bindgen")
        ))))
    )]
    pub use crate::host::null::Host as NullHost;

    impl_platform_host!(
        Null => NullHost,
        #[cfg(feature = "custom")] Custom => super::CustomHost,
    );

    /// The default host for the current compilation target platform.
    pub fn default_host() -> Host {
        NullHost::new()
            .expect("the default host should always be available")
            .into()
    }
}
```

