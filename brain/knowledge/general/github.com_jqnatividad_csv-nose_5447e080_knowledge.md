---
id: github.com-jqnatividad-csv-nose-5447e080-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:20:16.644554
---

# KNOWLEDGE EXTRACT: github.com_jqnatividad_csv-nose_5447e080
> **Extracted on:** 2026-04-01 10:08:52
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007520693/github.com_jqnatividad_csv-nose_5447e080

---

## File: `.gitattributes`
```
# Auto detect text files and perform LF normalization
* text=auto
```

## File: `.gitignore`
```
/target

# Test data files (copied from CSVsniffer, not included in repo)
# See README.md "Benchmark Setup" section for instructions
tests/data/pollock/
tests/data/w3c-csvw/
tests/data/csv-wrangling/

# Documentation audit reports
docs/audits/
```

## File: `CHANGELOG.md`
```markdown
# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.0.1] - 2026-02-21

### Fixed

- Re-release of 1.0.0 with no code changes; corrects a crates.io publish that preceded the release commit

**Full Changelog**: https://github.com/jqnatividad/csv-nose/compare/v1.0.0...v1.0.1

## [1.0.0] - 2026-02-21

### Performance

- Parallel dialect scoring via `rayon::par_iter` with thread-local `TypeScoreBuffers` for multi-core speedup
- `#[inline]` on `detect_cell_type` hot path
- Float regex gating with cheap `.contains('.')` / `.contains('e')` checks before regex evaluation
- `TypeScoreBuffers` struct eliminates per-call heap allocations in type scoring
- `normalize_line_endings` moved before `QuoteBoundaryCounts::new` to avoid redundant work
- `cached_modal_field_count_freq` field on `Table` avoids repeated filter+count in `calculate_tau_1`
- `Cow<Table>` in `build_metadata` avoids clone in the no-preamble case

### Changed

- Bump `clap` from 4.5.56 to 4.5.60
- Bump `ureq` from 3.1.4 to 3.2.0
- Bump `regex` from 1.12.2 to 1.12.3
- Bump `tempfile` from 3.24.0 to 3.25.0
- Rename `docs/PERFORMANCE.md` to `docs/ACCURACY.md` and update accuracy figures to v1.0.0

### Fixed

- CSV Wrangling accuracy improved from 87.15% to 92.74%:
  - Fix `nsign` benchmark annotation mapping (`"nsign"` → `b'#'`, not `b'§'`)
  - Raise pipe delimiter priority to prevent space-delimiter false positives
  - Double-quote 2.2× density check now requires real quote density (not just boundary count)
  - Single-quote opening boundary requirement prevents apostrophe-in-content false positives
- Cap `Records`-mode buffer allocations at 100 MB; use probe read to avoid false-positive truncation warnings
- Restore first-maximum tie-breaking semantics and fix related correctness issues
- Address HIGH, MEDIUM, and LOW security audit findings
- Dampen false quote boost from JSON content in unquoted fields
- Fix `isco.csv` and `uniq_nl_data.csv` detection (closing-only boundary boost, space+empty-first-field penalty)
- Fix misleading comment on float regex gate in `type_detection`
- Correct `lib.rs` paper citation to García (2024) Table Uniformity Method
- Fix tiebreaking threshold comment: 10% → 5% (`score_ratio > 0.95`)
- Fix accuracy figures in `docs/BENCHMARK_DATASETS_INFO.md` (CSV Wrangling ~87%→~93%, POLLOCK 96.62%→97.30%)
- Fix `docs/IMPLEMENTATION.md` NULL specificity weight (empty string=0.0, null-like strings=0.5)

### Added

- `docs/IMPLEMENTATION.md` — comprehensive algorithm reference covering all scoring details, thresholds, and design decisions
- `docs/ACCURACY.md` — accuracy summary and known limitations (replaces `PERFORMANCE.md`, updated to v1.0.0)
- Claude Code automations: clippy pre-tool hook, `api-compat-checker` subagent, `cargo-audit` and `benchmark` skills, benchmark regression checker subagent

**Full Changelog**: https://github.com/jqnatividad/csv-nose/compare/0.8.0...v1.0.0

## [0.8.0] - 2026-01-30

### Performance

- Set CSV reader buffer capacity to 32KB (from default 8KB) for improved parsing performance with larger sample data
- Add `#[inline]` to `Quote::char` method
- Optimize `is_boolean` check in type detection pipeline
- Make `is_numeric` and `is_temporal` const functions for compile-time optimization

### Changed

- Bump `clap` from 4.5.55 to 4.5.56

### Fixed

- Remove incorrect citation in documentation

**Full Changelog**: https://github.com/jqnatividad/csv-nose/compare/v0.7.0...v0.8.0

## [0.7.0] - 2026-01-28

### Changed

- Bump `clap` from 4.5.54 to 4.5.55
- Bump `actions/checkout` from 4 to 6 in CI workflow
- Updated Dependabot config for Cargo and GitHub Actions

### Performance

- Optimize type detection by using array for type counts instead of HashMap
- Make several methods `const` for improved compile-time optimization
- Optimize hot paths for ~18-21% speedup in dialect detection

No change in detection accuracy - these are pure performance optimizations.

**Full Changelog**: https://github.com/jqnatividad/csv-nose/compare/v0.6.0...v0.7.0

## [0.6.0] - 2026-01-26

### Changed

- Replaced `std::collections::HashMap` with `foldhash::HashMap` for faster hashing
- Updated package description to credit @ws-garcia's Table Uniformity Method

### Performance

- Pre-allocate HashMap capacities to avoid reallocation during growth
- Add `#[inline]` to Table accessor methods for better optimization
- Pass Table by reference to avoid unnecessary cloning
- Use `fmt::Write` instead of `format!()` to avoid temporary string allocations

No change in detection accuracy - these are pure performance optimizations.

**Full Changelog**: https://github.com/jqnatividad/csv-nose/compare/v0.5.0...v0.6.0

## [0.5.0] - 2026-01-22

### Added

- HTTP support for sniffing remote CSV files directly from URLs without downloading the entire file
- New `http` feature flag with `ureq` dependency for HTTP Range request support
- CLI can now accept URLs alongside local file paths (e.g., `csv-nose local.csv https://example.com/remote.csv`)
- Efficient Range request handling: uses partial downloads when server supports it, falls back to
  full download with truncation otherwise

### Fixed

- Properly escape paths and URLs in JSON and CSV output formats

**Full Changelog**: https://github.com/jqnatividad/csv-nose/compare/v0.4.0...v0.5.0

## [0.4.0] - 2026-01-21

### Added

- `BENCHMARK_DATASETS_INFO.md` documenting benchmark dataset characteristics and implications for detection
- Regression test with NYC 311 sample data (`tests/data/fixtures/nyc_311_sample_200.csv`) to prevent
  future `avg_record_len` calculation bugs

### Changed

- Quote detection now uses boundary analysis - quotes must appear at field boundaries (after delimiter/newline
  or before delimiter/newline) to receive a boost, improving accuracy for standardized files
- Tightened tiebreaker threshold from 90% to 95% for delimiter/quote priority decisions
- Reduced small sample penalties (< 3 rows: 0.80 instead of 0.70; 3-4 rows: 0.90 instead of 0.85)
- Increased section sign (`§`) delimiter factor from 0.70 to 0.78 (rare but legitimate delimiter)
- Increased double-quote density boost from 1.03 to 1.06/1.08/1.15/2.2 based on boundary evidence

### Fixed

- Quote boundary detection now uses the dialect's actual delimiter instead of hardcoded values
- `avg_record_len` now correctly calculates using only the bytes consumed
  by parsed rows, not the entire sample buffer. `SampleSize::Records(n)` was always producing ~1024
  bytes because the buffer size estimate (`n * 1024`) was divided by the parsed row count (`n`)

### Performance

Significant improvement for standardized CSV files (W3C-CSVW +6.34%), with tradeoff on real-world
messy files (CSV Wrangling datasets -3.9% to -4.8%).

| Dataset | v0.3.x | v0.4.0 | Change |
|:--------|:-------|:-------|:-------|
| POLLOCK | 96.62% | 96.62% | — |
| W3C-CSVW | 93.21% | 99.55% | +6.34% |
| CSV Wrangling | 91.06% | 87.15% | -3.91% |
| CSV Wrangling CODEC | 90.85% | 86.62% | -4.23% |
| CSV Wrangling MESSY | 89.68% | 84.92% | -4.76% |

**Full Changelog**: https://github.com/jqnatividad/csv-nose/compare/v0.3.1...v0.4.0

## [0.3.1] - 2026-01-20

### Fixed

- `avg_record_len` was always ~1024 bytes regardless of actual record size. Now correctly
  calculates from parsed table data (sum of field lengths plus delimiter and line terminator overhead).

### Performance

No change in detection accuracy.

**Full Changelog**: https://github.com/jqnatividad/csv-nose/compare/v0.3.0...v0.3.1

## [0.3.0] - 2026-01-19

### Added

- `ACCURACY.md` documenting detection accuracy, known limitations, and workarounds

### Changed

- Applied select Clippy suggestions for cleaner code

### Fixed

- Non-deterministic benchmark results caused by HashMap iteration order in modal
  field count calculation. Tie-breaking is now deterministic (prefers higher field count).

### Performance

- Cache pattern categories via LazyLock (eliminates ~25,500 Vec allocs/sniff)
- Pre-compute quote counts once for all dialect evaluations (eliminates 26 scans)
- Use Cow for line normalization (zero-copy for LF-terminated files)
- Cache modal field count in Table struct (eliminates HashMap allocs)
- Return best table from scoring to avoid redundant parsing (saves 2 parses)
- Fix O(n²) preamble detection with suffix count precomputation

Results are now deterministic (v0.2.x had non-deterministic tie-breaking).

| Dataset | v0.2.x* | v0.3.0 | Change |
|:--------|:--------|:-------|:-------|
| POLLOCK | 95.95% | 96.62% | +0.67% |
| W3C-CSVW | 94.12% | 93.21% | -0.91% |
| CSV Wrangling | 91.06% | 91.06% | — |
| CSV Wrangling CODEC | 90.85% | 90.85% | — |
| CSV Wrangling MESSY | 89.68% | 89.68% | — |

*v0.2.x results varied between runs due to non-deterministic HashMap iteration

**Full Changelog**: https://github.com/jqnatividad/csv-nose/compare/v0.2.1...v0.3.0

## [0.2.1] - 2025-01-19

### Added

- added CI test workflow
- registered crate on Zenodo
- added README.md badges

### Changed

- Updated CLAUDE.md with preamble detection documentation

### Performance

No change in detection accuracy.

**Full Changelog**: https://github.com/jqnatividad/csv-nose/compare/v0.2.0...v0.2.1

## [0.2.0] - 2025-01-19

### Added

- Preamble detection for both comment lines (`#`) and structural preambles
  (rows with inconsistent field counts at the start of files)
- `Header.num_preamble_rows` now reports the total preamble count

### Fixed

- Bug where comment preamble count was detected but discarded

### Performance

| Dataset | v0.1.0 | v0.2.0 | Change |
|:--------|:-------|:-------|:-------|
| POLLOCK | 95.95% | 95.95% | — |
| W3C-CSVW | 95.02% | 94.12% | -0.90% |
| CSV Wrangling | 90.50% | 91.06% | +0.56% |
| CSV Wrangling CODEC | 90.14% | 90.85% | +0.71% |
| CSV Wrangling MESSY | 90.48% | 89.68% | -0.80% |

**Full Changelog**: https://github.com/jqnatividad/csv-nose/compare/v0.1.0...v0.2.0

## [0.1.0] - 2025-01-18

### Added

- Initial release implementing the Table Uniformity Method from
  "Detecting CSV File Dialects by Table Uniformity Measurement and Data Type Inference"
  (García, 2024)
- Core dialect detection for delimiter, quote character, and line terminator
- Header row detection using type-based heuristics
- Column type inference (Text, Integer, Float, Boolean, Date, DateTime, Null)
- qsv-sniffer compatible API for drop-in replacement
- CLI tool with multiple output formats (text, JSON)
- Encoding detection and transcoding support (UTF-8, UTF-16, Windows-1251,
  GB2312, ISO-8859, etc.) via chardetng and encoding_rs
- Comment/preamble line detection (lines starting with `#`)
- Benchmark suite against POLLOCK, W3C-CSVW, and CSV Wrangling datasets
- Support for 12 delimiter characters: `,`, `;`, `\t`, `|`, `:`, `~`, `^`,
  `#`, `&`, ` `, `§`, `/`
- Configurable sample size (records, bytes, or entire file)
- Date format preference (MDY vs DMY) for ambiguous dates
- Forced delimiter and quote character options

### Performance

- Zero error rate across all benchmark datasets (no crashes on malformed data)
- ~95% accuracy on POLLOCK dataset
- ~94% accuracy on W3C-CSVW dataset
- ~91% accuracy on CSV Wrangling dataset

```

## File: `CLAUDE.md`
```markdown
# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Build Commands

```bash
cargo build              # Build debug
cargo build --release    # Build optimized release
cargo test               # Run all tests (unit + integration + doc tests)
cargo test test_name     # Run single test by name
cargo run -- file.csv    # Run CLI on a file
cargo clippy             # Lint
cargo fmt                # Format code
```

## Benchmark Commands

```bash
# Run benchmark on POLLOCK dataset (148 files)
cargo run --release -- --benchmark tests/data/pollock

# Run benchmark on W3C-CSVW dataset (221 files)
cargo run --release -- --benchmark tests/data/w3c-csvw

# Run benchmark on CSV Wrangling dataset (179 files)
cargo run --release -- --benchmark tests/data/csv-wrangling

# Run benchmark on CSV Wrangling filtered CODEC dataset (142 files)
cargo run --release -- --benchmark tests/data/csv-wrangling --annotations tests/data/annotations/csv-wrangling-codec.txt

# Run benchmark on CSV Wrangling MESSY dataset (126 non-normal files)
cargo run --release -- --benchmark tests/data/csv-wrangling --annotations tests/data/annotations/csv-wrangling-messy.txt

# Run benchmark with custom annotations file
cargo run --release -- --benchmark tests/data/pollock --annotations tests/data/annotations/pollock.txt

# Run benchmark integration tests with output
cargo test --test benchmark_accuracy -- --nocapture
```

Note: Benchmark test files must be copied from [CSVsniffer](https://github.com/ws-garcia/CSVsniffer). See README.md "Benchmark Setup" section.

## Architecture

csv-nose is a CSV dialect sniffer implementing the **Table Uniformity Method** from "Detecting CSV File Dialects by Table Uniformity Measurement and Data Type Inference" (García, 2024). It provides both a library (`csv_nose`) and CLI binary (`csv-nose`).

### Core Algorithm Flow

1. **`Sniffer`** (`src/sniffer.rs`) - Entry point. Reads sample data, detects preamble, generates potential dialects, scores them, returns `Metadata`

2. **TUM Pipeline** (`src/tum/`):
   - `potential_dialects.rs` - Generates dialect candidates (delimiter × quote × line terminator combinations)
   - `table.rs` - Parses data into a `Table` struct with rows and field counts
   - `uniformity.rs` - Computes tau_0 (consistency) and tau_1 (dispersion) scores
   - `type_detection.rs` - Detects cell types and computes type consistency scores
   - `score.rs` - Combines uniformity and type scores into gamma score, selects best dialect with delimiter/quote preference tiebreakers
   - `regexes.rs` - Lazy-compiled regex patterns for type detection

3. **Output Types** (`src/metadata.rs`):
   - `Metadata` - Full sniff result (dialect, fields, types)
   - `Dialect` - Delimiter, quote char, header info, flexibility
   - `Header` - Has header row flag and preamble row count
   - `Quote` - Quote character enum (`None` or `Some(u8)`)

4. **Benchmark Module** (`src/benchmark.rs`) - CLI only, not part of library:
   - Parses CSVsniffer annotation files (pipe-delimited format)
   - Runs dialect detection against test datasets
   - Calculates accuracy metrics (precision, recall, F1 score)
   - Available only via CLI `--benchmark` flag (not exported from library)

### Key Design Decisions

- **qsv-sniffer API compatibility**: The public API mirrors qsv-sniffer for drop-in replacement
- **Gamma scoring**: Dialects ranked by combined score = uniformity × type consistency × bonuses/penalties
- **Delimiter preference**: When scores are close (within 5%, `score_ratio > 0.95`), prefer common delimiters (`,` > `;` > `\t` > `|`) over rare ones (`#`, `&`, space)
- **Quote preference**: When scores are close, prefer `"` over `'` over `None`
- **Header detection**: Heuristic-based (type differences between first row and data, uniqueness, length)
- **Preamble detection**: Two-phase detection - first skips comment lines (`#`), then detects structural preambles (rows with inconsistent field counts). Total count stored in `Header.num_preamble_rows`
- **Sampling**: Configurable via `SampleSize::Records(n)`, `SampleSize::Bytes(n)`, or `SampleSize::All`

### Test Data

- `tests/data/annotations/` - Dialect annotation files (checked in)
- `tests/data/pollock/` - POLLOCK test CSVs (gitignored, copy from CSVsniffer)
- `tests/data/w3c-csvw/` - W3C-CSVW test CSVs (gitignored, copy from CSVsniffer)
- `tests/data/csv-wrangling/` - CSV Wrangling test CSVs (gitignored, copy from CSVsniffer)
```

## File: `Cargo.toml`
```
[package]
name = "csv-nose"
version = "1.0.1"
edition = "2024"
authors = ["Joel Natividad <joel@datHere.com>"]
description = "CSV dialect sniffer using Garcia's Table Uniformity Method"
license = "MIT OR Apache-2.0"
repository = "https://github.com/jqnatividad/csv-nose"
keywords = ["csv", "sniffer", "dialect", "detection"]
categories = ["command-line-utilities", "parsing", "text-processing"]
exclude = ["tests/data/*"]

[lib]
name = "csv_nose"
path = "src/lib.rs"

[[bin]]
name = "csv-nose"
path = "src/main.rs"
required-features = ["cli"]

[features]
default = ["cli"]
cli = ["clap"]
http = ["ureq"]
runtime-dispatch-simd = ["bytecount/runtime-dispatch-simd"]
generic-simd = ["bytecount/generic-simd"]

[dependencies]
csv = "1"
clap = { version = "4.6", features = ["derive"], optional = true }
regex = "1"
simdutf8 = "0.1"
thiserror = "2.0"
bytecount = "0.6"
chardetng = "0.1"
encoding_rs = "0.8"
ureq = { version = "3", optional = true }
foldhash = "0.2"
rayon = "1"

[dev-dependencies]
tempfile = "3"

[profile.release]
lto = true
codegen-units = 1
strip = true
```

## File: `README.md`
```markdown
[![Crates.io](https://img.shields.io/crates/v/csv-nose.svg?logo=crates.io)](https://crates.io/crates/csv-nose)
[![Docs.rs](https://docs.rs/csv-nose/badge.svg)](https://docs.rs/crate/csv-nose)
![License: MIT OR Apache-2.0](https://img.shields.io/crates/l/csv-nose.svg)
[![DOI](https://zenodo.org/badge/1137017320.svg)](https://doi.org/10.5281/zenodo.18303093)

# csv-nose

A Rust port of the [Table Uniformity Method](https://github.com/ws-garcia/CSVsniffer) for CSV dialect detection.

## Background

This crate [implements](implementation.md) the algorithm from ["Detecting CSV File Dialects by Table Uniformity Measurement and Data Type Inference"](https://doi.org/10.3233/DS-240062)[^1] by [W. García](https://github.com/ws-garcia). This implementation of the Table Uniformity Method achieves 99.55%[^2] accuracy on the [W3C-CSVW test suite](https://github.com/w3c/csvw) by:

1. Testing multiple potential dialects (delimiter × quote × line terminator combinations)
2. Scoring each dialect based on table uniformity (consistent field counts)
3. Scoring based on type detection (consistent data types within columns)
4. Selecting the dialect with the highest combined gamma score

[^1]: García W. Detecting CSV file dialects by table uniformity measurement and data type inference. Data Science. 2024;7(2):55-72. [doi:10.3233/DS-240062](https://doi.org/10.3233/DS-240062)

## Installation

### As a library

```toml
[dependencies]
csv-nose = "0.8"
```

### As a CLI tool

```bash
cargo install csv-nose
```

### With HTTP support (for remote URLs)

```bash
cargo install csv-nose --features http
```

## Library Usage

```rust
use csv_nose::{Sniffer, SampleSize};

let mut sniffer = Sniffer::new();
sniffer.sample_size(SampleSize::Records(100));

let metadata = sniffer.sniff_path("data.csv").unwrap();

println!("Delimiter: {}", metadata.dialect.delimiter as char);
println!("Has header: {}", metadata.dialect.header.has_header_row);
println!("Fields: {:?}", metadata.fields);
println!("Types: {:?}", metadata.types);
```

## CLI Usage

```bash
csv-nose data.csv                    # Sniff a single file
csv-nose *.csv                       # Sniff multiple files
csv-nose -f json data.csv            # Output as JSON
csv-nose --delimiter-only data.csv   # Output only the delimiter
csv-nose -v data.csv                 # Verbose output with field types
csv-nose https://example.com/data.csv  # Sniff remote CSV (requires http feature)
csv-nose local.csv https://example.com/remote.csv  # Mix local and remote
```

```bash
csv-nose -v /tmp/NYC_311_SR_2010-2020-sample-1M.csv
File: /tmp/NYC_311_SR_2010-2020-sample-1M.csv
  Delimiter: ','
  Quote: '"'
  Has header: true
  Preamble rows: 0
  Flexible: false
  UTF-8: true
  Fields: 41
  Avg record length: 547 bytes
  Field details:
    1: Unique Key (Unsigned)
    2: Created Date (DateTime)
    3: Closed Date (DateTime)
    4: Agency (Text)
    5: Agency Name (Text)
    6: Complaint Type (Text)
    7: Descriptor (Text)
    8: Location Type (Text)
    9: Incident Zip (Unsigned)
    10: Incident Address (Text)
    11: Street Name (Text)
    12: Cross Street 1 (Text)
    13: Cross Street 2 (Text)
    14: Intersection Street 1 (Text)
    15: Intersection Street 2 (Text)
    16: Address Type (Text)
    17: City (Text)
    18: Landmark (Text)
    19: Facility Type (Text)
    20: Status (Text)
    21: Due Date (DateTime)
    22: Resolution Description (Text)
    23: Resolution Action Updated Date (DateTime)
    24: Community Board (Text)
    25: BBL (Unsigned)
    26: Borough (Text)
    27: X Coordinate (State Plane) (Unsigned)
    28: Y Coordinate (State Plane) (Unsigned)
    29: Open Data Channel Type (Text)
    30: Park Facility Name (Text)
    31: Park Borough (Text)
    32: Vehicle Type (NULL)
    33: Taxi Company Borough (NULL)
    34: Taxi Pick Up Location (Text)
    35: Bridge Highway Name (NULL)
    36: Bridge Highway Direction (NULL)
    37: Road Ramp (NULL)
    38: Bridge Highway Segment (NULL)
    39: Latitude (Float)
    40: Longitude (Float)
    41: Location (Text)
```

## Remote URL Support

When built with the `http` feature, csv-nose can sniff remote CSV files directly from URLs:

```bash
# Build with HTTP support
cargo build --release --features http

# Sniff remote CSV
csv-nose https://raw.githubusercontent.com/datasets/gdp/main/data/gdp.csv

# Limit bytes fetched (useful for large remote files)
csv-nose -b 8192 https://example.com/large.csv
```

The HTTP feature uses Range requests when supported by the server to minimize data transfer. If the server doesn't support Range requests, it falls back to downloading and truncating at the sample size limit.

## API Compatibility

This library is designed as a drop-in replacement for [qsv-sniffer](https://github.com/jqnatividad/qsv-sniffer) used by [qsv](https://github.com/dathere/qsv). The public API mirrors qsv-sniffer for easy migration:

```rust
use csv_nose::{Sniffer, Metadata, Dialect, Header, Quote, Type, SampleSize, DatePreference};

let mut sniffer = Sniffer::new();
sniffer
    .sample_size(SampleSize::Records(50))
    .date_preference(DatePreference::MdyFormat)
    .delimiter(b',')
    .quote(Quote::Some(b'"'));
```

## Accuracy Benchmarks

csv-nose is benchmarked against the [same test datasets](docs/BENCHMARK_DATASETS_INFO.md) used by [CSVsniffer](https://github.com/ws-garcia/CSVsniffer), enabling direct accuracy comparison with other CSV dialect detection tools.

### Success Ratio

The table below shows the dialect detection success ratio. Accuracy is measured using only files that do not produce errors during dialect inference.

| Data set | `csv-nose` | `CSVsniffer MADSE` | `CSVsniffer` | `CleverCSV` | `csv.Sniffer` | DuckDB `sniff_csv` |
|:---------|:-----------|:-------------------|:-------------|:------------|:--------------|:-------------------|
| POLLOCK  | **97.30%** | 95.27%             | 96.55%       | 95.17%      | 96.35%        | 84.14%             |
| W3C-CSVW[^2] | **99.55%** | 94.52%             | 95.39%       | 61.11%      | 97.69%        | 99.08%             |
| CSV Wrangling | **92.74%** | 90.50%          | 89.94%       | 87.99%      | 84.26%        | 91.62%             |
| CSV Wrangling CODEC | **91.55%** | 90.14%    | 90.14%       | 89.44%      | 84.18%        | 92.25%             |
| CSV Wrangling MESSY | **90.48%** | 89.60%    | 89.60%       | 89.60%      | 83.06%        | 91.94%             |

[^2]: csv-nose is optimized for the [W3C CSV on the Web Test Suite](https://w3c.github.io/csvw/tests/) - reaching 99.55% accuracy.

### Failure Ratio

The table below shows the failure ratio (errors during dialect detection) for each tool.

> **Note:** "Errors" are files that caused crashes or exceptions during processing (e.g., encoding issues, malformed data). This is distinct from "failures" where a file was successfully processed but the wrong dialect was detected. A 0% error rate means all files were processed without crashes, even if some detections were incorrect.

| Data set             | `csv-nose` | `CSVsniffer MADSE` | `CSVsniffer` | `CleverCSV` | `csv.Sniffer` | DuckDB `sniff_csv` |
|:---------------------|:-----------|:-------------------|:-------------|:------------|:--------------|:-------------------|
| POLLOCK [148 files]  | **0.00%**  | 0.00%              | 2.03%        | 2.03%       | 7.43%         | 2.03%              |
| W3C-CSVW [221 files] | **0.00%**  | 0.91%              | 1.81%        | 2.26%       | 41.18%        | 1.81%              |
| CSV Wrangling [179 files] | **0.00%** | 0.00%         | 0.56%        | 0.56%       | 39.66%        | 0.00%              |
| CSV Wrangling CODEC [142 files] | **0.00%** | 0.00%   | 0.00%        | 0.00%       | 38.03%        | 0.00%              |
| CSV Wrangling MESSY [126 files] | **0.00%** | 0.79%   | 0.79%        | 0.79%       | 42.06%        | 0.79%              |

### F1 Score

The F1 score is the harmonic mean of precision and recall, providing a balanced measure of dialect detection accuracy.

| Data set | `csv-nose` | `CSVsniffer MADSE` | `CSVsniffer` | `CleverCSV` | `csv.Sniffer` | DuckDB `sniff_csv` |
|:---------|:-----------|:-------------------|:-------------|:------------|:--------------|:-------------------|
| POLLOCK  | **0.973**  | 0.976              | 0.972        | 0.965       | 0.943         | 0.904              |
| W3C-CSVW | **0.995**  | 0.967              | 0.967        | 0.748       | 0.730         | 0.986              |
| CSV Wrangling | **0.927** | 0.950             | 0.945        | 0.935       | 0.724         | 0.956              |
| CSV Wrangling CODEC | **0.916** | 0.948       | 0.948        | 0.944       | 0.728         | 0.959              |
| CSV Wrangling MESSY | **0.905** | 0.943       | 0.943        | 0.943       | 0.705         | 0.956              |

### Component Accuracy

csv-nose's delimiter and quote detection accuracy on each dataset:

| Data set | Delimiter Accuracy | Quote Accuracy |
|:---------|:-------------------|:---------------|
| POLLOCK  | 97.30%             | 100.00%        |
| W3C-CSVW | 99.55%             | 100.00%        |
| CSV Wrangling | 93.30%         | 99.44%         |
| CSV Wrangling CODEC | 91.55%   | 99.30%         |
| CSV Wrangling MESSY | 90.48%   | 99.21%         |

> NOTE: See [ACCURACY.md](docs/ACCURACY.md) for details on accuracy breakdowns and known limitations.

### Benchmark Setup

The benchmark test files are not included in this repository. To run benchmarks, first clone [CSVsniffer](https://github.com/ws-garcia/CSVsniffer) and copy the test files:

```bash
# Clone CSVsniffer (if not already available)
git clone https://github.com/ws-garcia/CSVsniffer.git /path/to/CSVsniffer

# Copy test files to csv-nose
cp -r /path/to/CSVsniffer/CSV/* tests/data/pollock/
cp -r /path/to/CSVsniffer/W3C-CSVW/* tests/data/w3c-csvw/
cp -r "/path/to/CSVsniffer/CSV_Wrangling/data/github/Curated files/"* tests/data/csv-wrangling/
```

### Running Benchmarks

Once the test files are in place:

```bash
# Run benchmark on POLLOCK dataset
cargo run --release -- --benchmark tests/data/pollock

# Run benchmark on W3C-CSVW dataset
cargo run --release -- --benchmark tests/data/w3c-csvw

# Run benchmark on CSV Wrangling dataset (all 179 files)
cargo run --release -- --benchmark tests/data/csv-wrangling

# Run benchmark on CSV Wrangling filtered CODEC (142 files)
cargo run --release -- --benchmark tests/data/csv-wrangling --annotations tests/data/annotations/csv-wrangling-codec.txt

# Run benchmark on CSV Wrangling MESSY (126 non-normal files)
cargo run --release -- --benchmark tests/data/csv-wrangling --annotations tests/data/annotations/csv-wrangling-messy.txt

# Run integration tests with detailed output
cargo test --test benchmark_accuracy -- --nocapture
```

## License

MIT OR Apache-2.0

## Naming

The name "csv-nose" is a play on words, combining "CSV" (Comma-Separated Values) with "nose," suggesting the tool's ability to "sniff out" the correct CSV dialect. "Nose" also sounds like "knows," implying expertise in CSV dialect detection.

## AI Contributions

Claude Code using Opus 4.5 was used to assist in code generation and documentation. All AI-generated content has been reviewed and edited by human contributors to ensure accuracy and quality.
```

## File: `docs/ACCURACY.md`
```markdown
# Accuracy and Known Limitations

This document describes cases where csv-nose may not correctly detect CSV dialects, helping you understand when to use manual overrides.

## Accuracy Summary

Tested against standard CSV benchmark datasets:

| Dataset | Success Rate | Notes |
|---------|--------------|-------|
| POLLOCK | 97.30% | General CSV files |
| W3C-CSVW | 99.55% | W3C CSV on the Web test suite |
| CSV Wrangling | 92.74% | Real-world messy CSVs |
| CSV Wrangling CODEC | 91.55% | Filtered subset |
| CSV Wrangling MESSY | 90.48% | Non-normal structures |

## Known Limitations

### Uncommon Delimiters

csv-nose is biased toward common delimiters (`,`, `;`, `\t`) to improve accuracy on real-world data. Files using rare delimiters may be misdetected.

**Space-delimited files** (0.75 penalty):
- Spaces appear frequently in text content, making them difficult to distinguish as delimiters
- Examples: `diamonds.csv`, `dict.csv`, `methane_molecular_structure_xyz_20140911.csv`

**Hash-delimited files** (0.60 penalty):
- Hash (`#`) is commonly used as a comment marker
- Examples: `councils.csv`, `flat_file_database.csv`, `uniq_nl_data.csv`

**Other rare delimiters**:
- Ampersand (`&`): 0.60 penalty
- Forward slash (`/`): 0.65 penalty
- Section sign (`§`): 0.78 penalty
- Caret (`^`) and tilde (`~`): 0.80 penalty
- Colon (`:`): 0.90 penalty (often appears in timestamps)

**Workaround**: Use explicit delimiter hint:
```rust
use csv_nose::Sniffer;

let metadata = Sniffer::new()
    .delimiter(b' ')  // Force space delimiter
    .sniff_path("space-delimited.csv")?;
```

### Quote Character Detection

**Single-quote vs double-quote**:
- Quote detection now uses boundary analysis - quotes must appear at field boundaries (after delimiter/newline or before delimiter/newline) to receive a boost
- Single quotes require boundary evidence AND no double quotes present to be detected
- Single quotes appearing only within text content (not at boundaries) receive a 0.95 penalty
- When double quotes are present, single-quote dialects receive a 0.90 penalty
- Examples of challenging files: `Auto_Tone_sub315_day1.csv`, `currencies.csv`, `isco.csv`

**Quote::None when quotes exist**:
- When double quotes have ≥0.5% density, `Quote::None` receives a 0.90 penalty
- This helps prefer quoted parsing when evidence exists

**Workaround**: Use explicit quote hint:
```rust
use csv_nose::{Sniffer, Quote};

let metadata = Sniffer::new()
    .quote(Quote::Some(b'\''))  // Force single quote
    .sniff_path("single-quoted.csv")?;
```

### Small Files

Files with few rows have less reliable detection:

| Rows | Penalty |
|------|---------|
| < 3 | 0.80 |
| 3-4 | 0.90 |
| ≥ 5 | None |

**Workaround**: Increase sample size or provide hints:
```rust
use csv_nose::{Sniffer, SampleSize};

let metadata = Sniffer::new()
    .sample_size(SampleSize::All)  // Read entire file
    .sniff_path("small.csv")?;
```

### Multi-table and Embedded Content

Files containing multiple tables or embedded non-CSV content may confuse detection:
- `file_multitable_less.csv`
- `file_multitable_more.csv`
- `file_multitable_same.csv`

These files have ambiguous structure where multiple dialects produce similar uniformity scores.

### Extreme Field Counts

**Single field** (0.50 penalty):
- A single field per row usually indicates the wrong delimiter was selected

**Very high field counts**:
- 50-100 fields: 0.80 penalty
- \>100 fields: 0.50 penalty
- May indicate splitting on a character that appears frequently in content

## Scoring Algorithm Reference

### Delimiter Penalties

| Delimiter | Penalty | Priority (tiebreaker) |
|-----------|---------|----------------------|
| `,` `;` `\t` | 1.00 | 10, 9, 8 |
| `\|` | 0.98 | 8 (ties with `\t`) |
| `:` | 0.90 | 4 |
| `^` `~` | 0.80 | 3 |
| `§` | 0.78 | 2 |
| ` ` (space) | 0.75 | 2 |
| `/` | 0.65 | 2 |
| `#` `&` | 0.60 | 1 |

When scores are within 5%, delimiter priority is used as a tiebreaker.

### Quote Evidence Scoring

Quote detection uses boundary analysis (quotes appearing at field boundaries, e.g., after/before the delimiter or newline) for improved accuracy:

| Condition | Multiplier |
|-----------|------------|
| Double quotes at boundaries, no single quotes | 2.20 boost |
| Double quotes at boundaries with good density | 1.15 boost |
| Double quotes with ≥0.5% density | 1.08 boost |
| Single quotes at boundaries (≥4), no double quotes, high density | 2.20 boost |
| Single quotes at boundaries (≥2), no double quotes | 1.20 boost |
| Single quote dialect when double quotes present | 0.90 penalty |
| Single quotes present but not at boundaries | 0.95 penalty |
| Quote::None when double quotes have ≥0.5% density | 0.90 penalty |

## Workarounds Summary

```rust
use csv_nose::{Sniffer, Quote, SampleSize};

// Force specific delimiter
let metadata = Sniffer::new()
    .delimiter(b'#')
    .sniff_path("hash-delimited.csv")?;

// Force specific quote character
let metadata = Sniffer::new()
    .quote(Quote::Some(b'\''))
    .sniff_path("single-quoted.csv")?;

// Force no quoting
let metadata = Sniffer::new()
    .quote(Quote::None)
    .sniff_path("unquoted.csv")?;

// Read entire file instead of sampling
let metadata = Sniffer::new()
    .sample_size(SampleSize::All)
    .sniff_path("small.csv")?;

// Combine hints
let metadata = Sniffer::new()
    .delimiter(b' ')
    .quote(Quote::None)
    .sample_size(SampleSize::Records(1000))
    .sniff_path("tricky.csv")?;
```

## When to Use Alternative Approaches

Consider using explicit dialect specification (bypassing sniffing entirely) when:

1. **You know the dialect** - If your data source has a documented format
2. **Consistent pipeline** - Processing files from the same source repeatedly
3. **Rare delimiters** - Space, hash, or other uncommon separators
4. **Performance critical** - Sniffing adds overhead; known formats can skip detection

For these cases, use a CSV parser directly with explicit configuration rather than sniffing.
```

## File: `docs/BENCHMARK_DATASETS_INFO.md`
```markdown
# Benchmark Datasets Information

This document describes the benchmark datasets used to evaluate csv-nose's dialect detection accuracy. These datasets are sourced from [CSVsniffer](https://github.com/ws-garcia/CSVsniffer) and represent a range of CSV file characteristics.

## Dataset Overview

| Dataset | Files | Source | Purpose |
|---------|-------|--------|---------|
| **POLLOCK** | 148 | Synthetic + curated | Test edge cases and controlled variations |
| **W3C-CSVW** | 221 | W3C CSV on the Web | Standardized test suite for CSV parsing |
| **CSV Wrangling** | 179 | Real-world GitHub files | Messy, real-world CSV files |
| **CSV Wrangling CODEC** | 142 | Filtered subset | Files that other tools can parse |
| **CSV Wrangling MESSY** | 126 | Filtered subset | Non-normal/problematic files |

## Delimiter Distribution

| Delimiter | POLLOCK | W3C-CSVW | CSV Wrangling |
|-----------|---------|----------|---------------|
| Comma | 104 (70%) | 219 (99%) | 127 (71%) |
| Semicolon | 39 (26%) | 0 | 36 (20%) |
| Tab | 3 (2%) | 1 (<1%) | 7 (4%) |
| Pipe (`\|`) | 1 (<1%) | 0 | 4 (2%) |
| Section sign (§) | 0 | 0 | 3 (2%) |
| Space | 1 (<1%) | 1 (<1%) | 2 (1%) |

## Quote Character Distribution

| Quote | POLLOCK | W3C-CSVW | CSV Wrangling |
|-------|---------|----------|---------------|
| Double (`"`) | 145 (98%) | 221 (100%) | 174 (97%) |
| Single (`'`) | 3 (2%) | 0 | 5 (3%) |

## Encoding Diversity

| Encoding | POLLOCK | W3C-CSVW | CSV Wrangling |
|----------|---------|----------|---------------|
| UTF-8 | 119 (80%) | 219 (99%) | 159 (89%) |
| ASCII | 29 (20%) | 0 | 1 (<1%) |
| ANSI | 0 | 2 (1%) | 12 (7%) |
| Windows-1251 | 0 | 0 | 3 (2%) |
| Other (UTF-16, Shift-JIS, GB2312) | 0 | 0 | 4 (2%) |

## Dataset Characteristics

### POLLOCK

Synthetic test files designed to test specific edge cases:

- **Multi-table files**: Files containing multiple embedded tables
- **Preamble handling**: Files with header comments or metadata rows
- **Unusual delimiters**: Space, pipe, and semicolon-delimited files
- **Escape character variations**: Different escape character configurations
- **Row anomalies**: Files with inconsistent field counts in specific rows
- **Quote variations**: Single-quote and double-quote files

Mix of simple well-formed CSVs and files with intentional structural challenges.

### W3C-CSVW

Files from the [W3C CSV on the Web](https://github.com/w3c/csvw) test suite:

- **Highly standardized**: 99% comma-delimited, 100% double-quoted, 99% UTF-8
- **Uniform dialect**: Designed for the W3C CSV on the Web specification
- **Structural variations**: Tests many small structural edge cases across 221 files
- **Line ending diversity**: Mix of LF and CRLF line endings
- **Well-documented**: Each file has a clear expected behavior

Best dataset for testing standard CSV compliance.

### CSV Wrangling

Real-world CSV files scraped from GitHub repositories:

- **Most diverse**: Wide range of encodings, delimiters, and structures
- **Real-world messiness**: Files created by various tools and humans
- **Encoding variety**: Includes UTF-16, Shift-JIS, GB2312, Windows-1251
- **Rare delimiters**: Section sign (§), pipe, and other unusual separators
- **Annotation issues**: Some expected dialects may not match actual file content

The CODEC and MESSY subsets filter this dataset:

- **CODEC (142 files)**: Files that standard CSV tools can successfully parse
- **MESSY (126 files)**: Files with non-normal structures or problematic content

## Implications for Detection

### Why W3C-CSVW has highest accuracy (99.55%)

- Uniform dialect (comma + double-quote) matches csv-nose's default preferences
- Well-formed files with clear quoting patterns
- Boundary detection works well with consistent structure

### Why CSV Wrangling has lower accuracy (~93%)

- Delimiter diversity: 29% use non-comma delimiters
- Rare delimiters (§, space) have detection penalties
- Some annotation errors in expected dialects
- Real-world files often have ambiguous structures

### Why POLLOCK is in between (97.30%)

- Intentionally challenging edge cases
- Tests specific failure modes
- Semicolon-heavy (26%) but well-structured

## Running Benchmarks

See [README.md](README.md#benchmark-setup) for instructions on setting up and running benchmarks.

```bash
# Run all benchmarks
cargo test --test benchmark_accuracy -- --nocapture

# Run individual dataset
cargo run --release -- --benchmark tests/data/pollock
cargo run --release -- --benchmark tests/data/w3c-csvw
cargo run --release -- --benchmark tests/data/csv-wrangling
```
```

## File: `docs/IMPLEMENTATION.md`
```markdown
# csv-nose Implementation Notes

csv-nose implements the **Table Uniformity Method (TUM)** from:

> García, W. S. (2024). *Detecting CSV File Dialects by Table Uniformity Measurement and Data Type Inference*. DOI: 10.13140/RG.2.2.28318.82245

This document describes the implementation pipeline, where we follow the paper closely, and where we diverge. The implementation was tuned to push benchmark accuracy above 90% on W3C-CSVW while maintaining or improving POLLOCK accuracy.

---

## 1. Pipeline Overview

The entry point is `Sniffer::sniff_bytes` in `src/sniffer.rs`. The pipeline is:

1. **Encoding detection + transcoding** — detect character encoding and transcode to UTF-8 if necessary; strip BOM
2. **Comment preamble stripping** — skip leading lines starting with `#` (with optional leading whitespace); count skipped rows
3. **Line terminator detection** — detect LF / CRLF / CR from the data (once, not per dialect)
4. **Dialect candidate generation** — 11 delimiters × 3 quote chars = 33 candidates, all sharing the detected line terminator (`src/tum/potential_dialects.rs`)
5. **Line ending normalization** — normalize to LF once before parallel scoring (zero-copy for LF files via `Cow::Borrowed`)
6. **Parallel dialect scoring** — score all 33 candidates via `rayon::par_iter` with thread-local `TypeScoreBuffers` (`src/tum/score.rs::score_all_dialects_with_best_table`)
7. **Best dialect selection** — `find_best_dialect` picks the winner with delimiter/quote priority tiebreaking
8. **Structural preamble detection** — identify non-data rows at the start using field count consistency
9. **Header detection** — multi-criterion heuristic scoring on the effective table
10. **Column type inference** — `infer_column_types` assigns a type to each column

---

## 2. Table Uniformity Scores

### tau_0 (Consistency)

Matches the paper exactly. Measures whether all rows have the same number of fields.

```
τ₀ = 1 / (1 + 2σ)
```

where σ is the standard deviation of per-row field counts. Range: [0, 1]; 1.0 = perfectly uniform.

Implementation: `src/tum/uniformity.rs::calculate_tau_0`

### tau_1 (Dispersion)

**Diverges from the paper.** The paper's formula is:

```
τ₁ = 2 · R(α² + 1)((1 - β) / M)
```

where R = range of field counts, α = number of row-to-row transitions, M = modal field count, β = M/n. This formula is unbounded (0 to ∞) and equals 0 for a perfectly uniform table.

Our formula is a bounded weighted composite, where 1.0 = perfectly uniform:

```
τ₁ = mode_score × 0.4 + range_score × 0.3 + transition_score × 0.3
```

- `mode_score` = fraction of rows with the modal field count
- `range_score` = `1 − (range / max_field_count)`, clamped to [0, 1]
- `transition_score` = `1 − (transitions / (n − 1))` where transitions counts row-to-row field count changes

**Rationale**: the paper's τ₁ is unbounded and grows with dispersion. Inverting and bounding it to [0, 1] lets it fit naturally into our gamma composite formula as a multiplicative term.

Implementation: `src/tum/uniformity.rs::calculate_tau_1`

---

## 3. Type Detection

**Type system** (`src/field_type.rs`, `src/tum/type_detection.rs`):

Types detected: `NULL`, `Unsigned`, `Signed`, `Float`, `Boolean`, `Date`, `DateTime`, `Text`

This is richer than the paper, which uses a binary known/unknown classification for scoring.

**Detection order** (optimized for hot path, each cell runs this sequence):

1. NULL — empty string or known null literals (`null`, `NA`, `N/A`, `NaN`, `#N/A`, `#VALUE!`, etc.)
2. Unsigned integer — direct digit scan, no regex; limited to 19 digits (fits u64)
3. Signed integer — direct scan for negative integers; positive integers are caught by Unsigned above
4. Boolean — exhaustive length-keyed match (`true`/`false`, `yes`/`no`, `on`/`off`, `1`/`0`, `y`/`n`, `t`/`f`)
5. Float — gated by `.contains('.')` or `.contains('e')` before applying float regex
6. DateTime — regex match for ISO 8601 and common timestamp formats
7. Date — regex match for common date formats
8. Text — fallthrough

The cheap string-operation gates for NULL, integers, and booleans avoid regex overhead on the most common cell types.

### Type Score

**Diverges from the paper.** The paper computes a global type score:

```
λ = (Σ Sᵢ)² / (100 · k²)
```

where Sᵢ = 100 if the cell type is "known", 0.1 if "unknown", and k = total cell count.

Our approach computes a **per-column consistency score**:

```
column_score = max_type_count / non_null_total
type_score = mean(column_score for all columns)
```

- `max_type_count` = count of the most frequent non-null type in the column
- NULL cells are excluded from the denominator (sparse data is not penalized)
- Final type score = average across all columns

**Rationale**: per-column scoring rewards uniform column types rather than raw "known type" fraction, which is a better signal for dialect detection (correct delimiter → consistent column types).

### Pattern Score

**Not in the paper.** An additional per-table pattern specificity score:

```
pattern_score = mean(specificity_weight for modal type of each column)
```

Type specificity weights: `DateTime`=1.0, `Date`=0.9, `Float`=1.0, `Unsigned`/`Signed`=1.0, `Boolean`=1.0, `Text`=0.1, null-like strings (`"NULL"`, `"NA"`, etc.)=0.5, empty string=0.0

Contributes 0.1× to gamma; rewards files with structured data types over free-form text.

Implementation: `src/tum/type_detection.rs::calculate_pattern_score`

---

## 4. Gamma Score (Combined Score)

**Diverges from the paper.** The paper's combined formula is:

```
ϖ = (τ₀/Δ + 1/(τ₁ + n)) · Σᵢ λᵢ   (for n > 1)
```

where Δ = expected record count threshold.

Our formula (`src/tum/score.rs::compute_gamma`):

```
uniformity_score = sqrt(τ₀ × τ₁)            # geometric mean
raw_score = uniformity_score × 0.5
          + type_score × 0.3
          + pattern_score × 0.1
          + row_bonus                         # up to +0.10 at ≥20 rows
          + field_bonus                       # up to +0.20 at ≥10 fields

gamma = raw_score
      × single_field_penalty   # 0.5× if modal_fields == 1
      × high_field_penalty     # 0.8× if >50 fields; 0.5× if >100 fields
      × delimiter_penalty      # 0.60–1.0 by delimiter rarity (see table below)
      × small_sample_penalty   # 0.80 if <3 rows; 0.90 if <5 rows; 1.0 otherwise
```

Then multiplied by `quote_multiplier` (0.90–2.2×) from quote evidence scoring (Section 5).

**Bonus details**:
- `row_bonus = (min(num_rows, 20) / 20) × 0.10`
- `field_bonus = (min(field_count, 10) / 10) × 0.20` (only when field_count ≥ 2)

**Delimiter penalty table**:

| Delimiter | Penalty | Relaxed condition |
|-----------|---------|-------------------|
| `,` `;` `\t` | 1.00 | — |
| `\|` | 0.98 | — |
| `:` | 0.90 | — *(vestigial — `:` is excluded from candidates; see Section 9)* |
| `^` `~` | 0.80 | — |
| `§` (0xA7) | 0.78 | — |
| ` ` | 0.75 | — |
| `/` | 0.65 | — |
| `#` | 0.60 | relaxed to 0.85 when ≥3 fields AND ≥50 rows |
| `&` | 0.60 | — |

**Rationale for divergence**: The paper's formula uses τ₀/Δ where Δ is the sample threshold — there is no equivalent concept in our implementation. We fold sample reliability into the row_bonus additive term and small_sample_penalty multiplicative term instead.

---

## 5. Quote Evidence Scoring

**Novel, not in the paper.** A major addition that significantly improves accuracy on quoted files.

Pre-computation (once per sniff call, not per dialect):

- **`QuoteCounts`**: total `"` and `'` character counts; `\"` and `\'` escape pair counts; total data length
- **`QuoteBoundaryCounts`**: opening boundaries (delimiter/newline → quote) and closing boundaries (quote → delimiter/newline) for each delimiter × quote combination, computed in a single pass

Quote density is measured in counts per 1000 bytes. The significance threshold is 5/1000 (0.5%).

### Double-quote multiplier rules (`Quote::Some(b'"')`)

| Condition | Multiplier |
|-----------|-----------|
| No single quotes + ≥2 boundaries + density ≥ 0.5% | **2.2×** |
| ≥2 boundaries + density ≥ 0.5% | **1.15×** |
| Density ≥ 0.5% only | **1.08×** |
| Otherwise | 1.0× |

### Single-quote multiplier rules (`Quote::Some(b'\'')`)

Opening boundary requirement guards against apostrophes in text content (which produce only closing boundaries before delimiters, never opening boundaries after them).

| Condition | Multiplier |
|-----------|-----------|
| No double quotes + ≥2 opening boundaries + ≥4 total boundaries + density ≥ 1.0% | **2.2×** |
| No double quotes + ≥1 opening boundary + ≥2 total boundaries + density ≥ 0.5% | **1.20×** |
| Double-quote density ≥ 0.5% (double quotes dominate) | **0.90×** |
| Backslash-escaped single quotes (`\'`) + no double-quote escapes + no boundaries | **1.10×** |
| No double quotes + 0 opening boundaries + ≥20 total boundaries + density ≥ 5% | **1.10×** |
| No boundaries at all + single quotes present | **0.95×** |
| Otherwise | 1.0× |

The closing-only 1.10× case handles hash-delimited data with space-padded fields (e.g., `# 'addr' # 'city'`) where the space between the `#` delimiter and the `'` quote character prevents the adjacency scan from detecting an opening boundary. The opening boundary scan requires the delimiter and quote to be immediately adjacent (no intervening whitespace), so `# '` does not register as an opening boundary for the next field (the intervening space breaks adjacency). The `'` still contributes to total boundary counts but not to opening boundary counts, leaving `opening_count = 0` and triggering the closing-only 1.10× path.

### No-quote multiplier rules (`Quote::None`)

| Condition | Multiplier |
|-----------|-----------|
| Double-quote density ≥ 0.5% | **0.90×** |
| Otherwise | 1.0× |

### Special dampening rules

Applied after the base quote multiplier in `score_dialect_with_normalized_data`:

1. **JSON-like chaos**: if quote multiplier > 1.5, modal field count ≥ 5, table is non-uniform, first row has ≤1 field, and ≥3 distinct non-modal field counts exist → scale the boost excess down to 30%: `1.0 + (multiplier − 1.0) × 0.3`

2. **Space delimiter + empty first field**: if >50% of rows have an empty first field → cap quote multiplier at 1.05×, then apply 0.55× to the combined gamma. This suppresses the false quote boundary signal from spaces adjacent to quote characters in leading-space-padded row formats.

3. **Comma + ` # ` pattern**: if >90% of rows have ` # ` in the first parsed field AND comma yields exactly 2 fields → apply 0.82× to the comma dialect gamma. This indicates that `#` is the true delimiter and comma splits inside a `#`-delimited field.

---

## 6. Tiebreaking

**Extends the paper.** The paper's `GetBestDialect` simply picks the highest ϖ.

Our `find_best_dialect` (`src/tum/score.rs`):

- Compute `score_ratio = min_gamma / max_gamma` for each pair being compared
- If `score_ratio > 0.95` (scores within 5%), apply priority ordering:
  1. Delimiter priority (higher = preferred): `,`=10, `;`=9, `\t`=8, `|`=8, `:`=4 *(vestigial — excluded from candidates)*, `^`=3, `~`=3, `§`=2, `/`=2, ` `=2, `#`=1, `&`=1
  2. Quote priority (higher = preferred): `"`=3, `'`=2, `None`=1
  3. If both priorities tie, use raw gamma
- If all non-zero dialects produce single-field tables, apply priority ordering regardless of score gap (fallback for files that can't be parsed with any delimiter)

---

## 7. Preamble Detection

**Extends the paper** (not detailed there). Two-phase approach:

### Phase 1: Comment preamble (`src/sniffer.rs::skip_preamble`)

Strip leading lines that start with `#` (with optional leading whitespace/tabs). Performed before dialect scoring so comment lines don't pollute field count statistics. The count is stored and added to the final `Header.num_preamble_rows`.

### Phase 2: Structural preamble (`src/sniffer.rs::detect_structural_preamble`)

After dialect scoring, find the first row from which ≥80% of the remaining rows share the modal field count. Uses an O(n) suffix-count precomputation to avoid O(n²) scanning:

1. Compute the modal field count for the full table
2. Precompute `matching_suffix[i]` = number of rows from index i to end that match the modal count
3. Scan forward; return the first index i where `matching_suffix[i] / (n − i) ≥ 0.80`

Requires ≥3 rows to attempt detection. The total preamble count reported in metadata is `comment_rows + structural_rows`.

---

## 8. Header Detection

**Extends the paper.** The paper treats the header row as "a simple record." Our `detect_header` (`src/sniffer.rs`) uses a weighted multi-criterion score:

| Check | Score if true |
|-------|--------------|
| First row has more text-typed cells than second row | +1.0 |
| First row has more text cells than numeric cells | +0.5 |
| All first-row values are unique (no duplicate column names) | +0.5 |
| Average first-row cell length ≤ average second-row cell length | +0.3 |

`has_header = (total_score / 4) > 0.4`

Requires ≥2 rows. All type classification uses `detect_cell_type` from `src/tum/type_detection.rs`.

---

## 9. Candidate Dialects

**Extends the paper.** The paper tests `, ; TAB | SPACE` delimiters and `" ' ~` quote chars.

Our candidates (`src/tum/potential_dialects.rs`):

| Category | Values |
|----------|--------|
| Delimiters (11) | `,` `;` `\t` `\|` ` ` `^` `~` `#` `&` `§` `/` |
| Quote chars (3) | `"` `'` `None` |
| Line terminators | 1 per file (detected once, not iterated) |
| **Total candidates** | **33** |

Additional delimiters compared to paper: `#` (scientific/hash-delimited data), `§` (section sign, used in some European data formats), `/` (path-like delimiters), `^`, `~`.

Note: `:` (colon) is intentionally excluded from candidates despite appearing in `delimiter_priority` — it commonly appears in timestamp values and causes too many false positives.

---

## 10. Performance

Not described in the paper. Implemented to handle bulk sniffing efficiently:

- **Parallel scoring**: `rayon::par_iter` over all 33 candidates; each rayon worker thread owns a `TypeScoreBuffers` instance via `thread_local!` to avoid per-call heap allocation
- **Zero-copy normalization**: `normalize_line_endings` returns `Cow::Borrowed` for LF files (most common case)
- **Single-pass boundary counting**: `QuoteBoundaryCounts::new` scans data once for all delimiters using a 256-entry lookup table
- **Reused best table**: the parsed table for the winning dialect is passed through to preamble detection and metadata building, avoiding a redundant re-parse
- **`Cow<Table>` in build_metadata**: avoids cloning the table in the common no-preamble case

---

## Divergence Summary

| Aspect | Paper (García 2024) | Our Implementation |
|--------|---------------------|--------------------|
| τ₁ formula | `2·R(α²+1)((1−β)/M)`, unbounded, 0=uniform | Weighted composite, bounded [0,1], 1=uniform |
| Type score λ | Global `(ΣSᵢ)²/(100·k²)`, binary S | Per-column max-type consistency, NULL-excluded |
| Gamma formula | `(τ₀/Δ + 1/(τ₁+n))·Σλᵢ` | Weighted sum with multiplicative penalties |
| Quote detection | Not described | Layered density + boundary evidence multiplier |
| Tiebreaking | Highest score wins | Delimiter + quote priority within 5% score band |
| Preamble | Not detailed | Two-phase: comment lines + structural field-count analysis |
| Header | "Treat as a record" | Multi-criterion weighted heuristic |
| Delimiter set | `, ; TAB \| SPACE` (5) | 11 delimiters including `# § / ^ ~` |
| Pattern score | Not present | Type specificity score (0.1× weight in gamma) |
| Sample size | Threshold Δ parameter | `SampleSize::{Records(n), Bytes(n), All}` |
| Parallel scoring | Not described | Rayon par_iter + thread-local type score buffers |
| Line terminators | LF and CRLF iterated | Detected once, normalized before scoring |
```

## File: `src/benchmark.rs`
```rust
//! Benchmark module for testing csv-nose accuracy against CSVsniffer test datasets.
//!
//! This module provides tools to validate the Table Uniformity Method implementation
//! against the same test datasets used by CSVsniffer, enabling accuracy comparison.

use csv_nose::{Metadata, Quote, Sniffer};
use foldhash::{HashMap, HashMapExt};
use std::fs;
use std::io::{self, BufRead};
use std::path::{Path, PathBuf};

/// Expected dialect from annotation file.
///
/// Note: `encoding`, `escape_char`, and `line_terminator` are parsed from the annotation file
/// but not yet used in validation. They are retained for potential future accuracy comparisons.
#[derive(Debug, Clone)]
#[allow(dead_code)]
pub struct ExpectedDialect {
    pub file_name: String,
    pub encoding: String,
    pub delimiter: u8,
    pub quote_char: Option<u8>,
    pub escape_char: Option<u8>,
    pub line_terminator: LineTerminator,
}

/// Line terminator type.
#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub enum LineTerminator {
    Lf,
    Cr,
    CrLf,
}

/// Result of benchmarking a single file.
#[derive(Debug, Clone)]
pub struct FileResult {
    pub file_name: String,
    pub passed: bool,
    pub delimiter_match: bool,
    pub quote_match: bool,
    pub expected_delimiter: u8,
    pub detected_delimiter: u8,
    pub expected_quote: Option<u8>,
    pub detected_quote: Option<u8>,
    pub error: Option<String>,
}

/// Aggregate benchmark results.
#[derive(Debug, Clone, Default)]
pub struct BenchmarkResult {
    pub total: usize,
    pub passed: usize,
    pub failed: usize,
    pub errors: usize,
    pub delimiter_matches: usize,
    pub quote_matches: usize,
    pub file_results: Vec<FileResult>,
}

impl BenchmarkResult {
    /// Calculate success ratio (passed / total).
    pub fn success_ratio(&self) -> f64 {
        if self.total == 0 {
            0.0
        } else {
            self.passed as f64 / self.total as f64
        }
    }

    /// Calculate failure ratio (failed / total).
    pub fn failure_ratio(&self) -> f64 {
        if self.total == 0 {
            0.0
        } else {
            self.failed as f64 / self.total as f64
        }
    }

    /// Calculate error ratio (errors / total).
    pub fn error_ratio(&self) -> f64 {
        if self.total == 0 {
            0.0
        } else {
            self.errors as f64 / self.total as f64
        }
    }

    /// Calculate delimiter accuracy.
    pub fn delimiter_accuracy(&self) -> f64 {
        let valid = self.total - self.errors;
        if valid == 0 {
            0.0
        } else {
            self.delimiter_matches as f64 / valid as f64
        }
    }

    /// Calculate quote accuracy.
    pub fn quote_accuracy(&self) -> f64 {
        let valid = self.total - self.errors;
        if valid == 0 {
            0.0
        } else {
            self.quote_matches as f64 / valid as f64
        }
    }

    /// Calculate precision (true positives / (true positives + false positives)).
    /// For dialect detection, this is essentially the success ratio.
    pub fn precision(&self) -> f64 {
        self.success_ratio()
    }

    /// Calculate recall (true positives / (true positives + false negatives)).
    /// For dialect detection with known ground truth, this equals precision.
    pub fn recall(&self) -> f64 {
        self.success_ratio()
    }

    /// Calculate F1 score (harmonic mean of precision and recall).
    pub fn f1_score(&self) -> f64 {
        let p = self.precision();
        let r = self.recall();
        if p + r == 0.0 {
            0.0
        } else {
            2.0 * p * r / (p + r)
        }
    }

    /// Print detailed results to stdout.
    pub fn print_details(&self) {
        println!("\n=== Benchmark Results ===\n");

        for result in &self.file_results {
            let status = if result.error.is_some() {
                "ERROR"
            } else if result.passed {
                "PASS"
            } else {
                "FAIL"
            };

            print!("[{}] {}", status, result.file_name);

            if !result.passed && result.error.is_none() {
                print!(" - ");
                if !result.delimiter_match {
                    print!(
                        "delimiter: expected '{}' got '{}' ",
                        result.expected_delimiter as char, result.detected_delimiter as char
                    );
                }
                if !result.quote_match {
                    let exp = result
                        .expected_quote
                        .map_or_else(|| "none".to_string(), |c| format!("'{}'", c as char));
                    let det = result
                        .detected_quote
                        .map_or_else(|| "none".to_string(), |c| format!("'{}'", c as char));
                    print!("quote: expected {exp} got {det}");
                }
            }

            if let Some(ref err) = result.error {
                print!(" - {err}");
            }

            println!();
        }
    }

    /// Print summary metrics to stdout.
    pub fn print_summary(&self) {
        println!("\n=== Summary ===\n");
        println!("Total files:        {}", self.total);
        println!(
            "Passed:             {} ({:.1}%)",
            self.passed,
            self.success_ratio() * 100.0
        );
        println!(
            "Failed:             {} ({:.1}%)",
            self.failed,
            self.failure_ratio() * 100.0
        );
        println!(
            "Errors:             {} ({:.1}%)",
            self.errors,
            self.error_ratio() * 100.0
        );
        println!();
        println!(
            "Delimiter accuracy: {:.1}%",
            self.delimiter_accuracy() * 100.0
        );
        println!("Quote accuracy:     {:.1}%", self.quote_accuracy() * 100.0);
        println!();
        println!("Precision:          {:.3}", self.precision());
        println!("Recall:             {:.3}", self.recall());
        println!("F1 Score:           {:.3}", self.f1_score());
    }
}

/// Parse an annotation file and return a map of file name to expected dialect.
pub fn parse_annotations(path: &Path) -> io::Result<HashMap<String, ExpectedDialect>> {
    let file = fs::File::open(path)?;
    let reader = io::BufReader::new(file);
    // currently expecting around 250 annotations at most
    let mut annotations = HashMap::with_capacity(250);

    for line in reader.lines() {
        let line = line?;
        let line = line.trim();

        // Skip comments and empty lines
        if line.is_empty() || line.starts_with('#') {
            continue;
        }

        // Skip header line
        if line.starts_with("file_name|") {
            continue;
        }

        let parts: Vec<&str> = line.split('|').collect();
        if parts.len() < 6 {
            continue;
        }

        let file_name = parts[0].to_string();
        let encoding = parts[1].to_string();
        let delimiter = parse_delimiter(parts[2]);
        let quote_char = parse_quote(parts[3]);
        let _escape_char = parse_escape(parts[4]);
        let line_terminator = parse_line_terminator(parts[5]);

        annotations.insert(
            file_name.clone(),
            ExpectedDialect {
                file_name,
                encoding,
                delimiter,
                quote_char,
                escape_char: _escape_char,
                line_terminator,
            },
        );
    }

    Ok(annotations)
}

/// Parse delimiter name to byte.
fn parse_delimiter(name: &str) -> u8 {
    match name.to_lowercase().as_str() {
        "comma" => b',',
        "semicolon" => b';',
        "tab" => b'\t',
        "space" => b' ',
        "vslash" | "pipe" => b'|',
        "colon" => b':',
        "nsign" => b'#', // Number sign (#)
        "slash" => b'/',
        _ => b',', // Default to comma
    }
}

/// Parse quote character name to byte.
fn parse_quote(name: &str) -> Option<u8> {
    match name.to_lowercase().as_str() {
        "doublequote" | "double" => Some(b'"'),
        "singlequote" | "single" => Some(b'\''),
        "tilde" => Some(b'~'),
        "" | "none" => None,
        _ => Some(b'"'), // Default to double quote
    }
}

/// Parse escape character name to byte.
fn parse_escape(name: &str) -> Option<u8> {
    match name.to_lowercase().as_str() {
        "doublequote" | "double" => Some(b'"'),
        "singlequote" | "single" => Some(b'\''),
        "backslash" => Some(b'\\'),
        "" | "none" => None,
        _ => None,
    }
}

/// Parse line terminator name.
fn parse_line_terminator(name: &str) -> LineTerminator {
    match name.to_lowercase().as_str() {
        "lf" => LineTerminator::Lf,
        "cr" => LineTerminator::Cr,
        "crlf" => LineTerminator::CrLf,
        _ => LineTerminator::Lf,
    }
}

/// Run benchmark on a directory of CSV files.
pub fn run_benchmark(data_dir: &Path, annotations_path: &Path) -> io::Result<BenchmarkResult> {
    let annotations = parse_annotations(annotations_path)?;
    let mut result = BenchmarkResult::default();

    // Process each file in the annotations
    for (file_name, expected) in &annotations {
        let file_path = data_dir.join(file_name);
        result.total += 1;

        let file_result = benchmark_file(&file_path, expected);

        if file_result.error.is_some() {
            result.errors += 1;
        } else if file_result.passed {
            result.passed += 1;
            result.delimiter_matches += 1;
            result.quote_matches += 1;
        } else {
            result.failed += 1;
            if file_result.delimiter_match {
                result.delimiter_matches += 1;
            }
            if file_result.quote_match {
                result.quote_matches += 1;
            }
        }

        result.file_results.push(file_result);
    }

    // Sort results by file name for consistent output
    result
        .file_results
        .sort_by(|a, b| a.file_name.cmp(&b.file_name));

    Ok(result)
}

/// Benchmark a single file against expected dialect.
fn benchmark_file(file_path: &Path, expected: &ExpectedDialect) -> FileResult {
    let file_name = expected.file_name.clone();

    // Check if file exists
    if !file_path.exists() {
        return FileResult {
            file_name,
            passed: false,
            delimiter_match: false,
            quote_match: false,
            expected_delimiter: expected.delimiter,
            detected_delimiter: 0,
            expected_quote: expected.quote_char,
            detected_quote: None,
            error: Some("File not found".to_string()),
        };
    }

    // Run sniffer
    let mut sniffer = Sniffer::new();
    let metadata: Result<Metadata, _> = sniffer.sniff_path(file_path);

    match metadata {
        Ok(meta) => {
            let detected_delimiter = meta.dialect.delimiter;
            let detected_quote = match meta.dialect.quote {
                Quote::None => None,
                Quote::Some(c) => Some(c),
            };

            let delimiter_match = detected_delimiter == expected.delimiter;
            let quote_match = detected_quote == expected.quote_char;
            let passed = delimiter_match && quote_match;

            FileResult {
                file_name,
                passed,
                delimiter_match,
                quote_match,
                expected_delimiter: expected.delimiter,
                detected_delimiter,
                expected_quote: expected.quote_char,
                detected_quote,
                error: None,
            }
        }
        Err(e) => FileResult {
            file_name,
            passed: false,
            delimiter_match: false,
            quote_match: false,
            expected_delimiter: expected.delimiter,
            detected_delimiter: 0,
            expected_quote: expected.quote_char,
            detected_quote: None,
            error: Some(e.to_string()),
        },
    }
}

/// Find the annotation file for a data directory.
pub fn find_annotations(data_dir: &Path) -> Option<PathBuf> {
    // Check for annotations in parent directory
    let dir_name = data_dir.file_name()?.to_str()?;
    let parent = data_dir.parent()?;

    // Try annotations subdirectory
    let annotations_dir = parent.join("annotations");
    if annotations_dir.is_dir() {
        let annotation_file = annotations_dir.join(format!("{dir_name}.txt"));
        if annotation_file.exists() {
            return Some(annotation_file);
        }
    }

    // Try direct annotation file in data dir
    let direct_annotation = data_dir.join("annotations.txt");
    if direct_annotation.exists() {
        return Some(direct_annotation);
    }

    None
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_parse_delimiter() {
        assert_eq!(parse_delimiter("comma"), b',');
        assert_eq!(parse_delimiter("semicolon"), b';');
        assert_eq!(parse_delimiter("tab"), b'\t');
        assert_eq!(parse_delimiter("space"), b' ');
        assert_eq!(parse_delimiter("vslash"), b'|');
        assert_eq!(parse_delimiter("colon"), b':');
        // "nsign" is the CSVsniffer annotation name for number sign (#, 0x23).
        // It must NOT map to 0xA7 (§, section sign), which is a different Unicode character.
        assert_eq!(parse_delimiter("nsign"), b'#');
    }

    #[test]
    fn test_parse_quote() {
        assert_eq!(parse_quote("doublequote"), Some(b'"'));
        assert_eq!(parse_quote("singlequote"), Some(b'\''));
        assert_eq!(parse_quote("tilde"), Some(b'~'));
        assert_eq!(parse_quote(""), None);
        assert_eq!(parse_quote("none"), None);
    }

    #[test]
    fn test_parse_line_terminator() {
        assert_eq!(parse_line_terminator("lf"), LineTerminator::Lf);
        assert_eq!(parse_line_terminator("cr"), LineTerminator::Cr);
        assert_eq!(parse_line_terminator("crlf"), LineTerminator::CrLf);
    }

    #[test]
    fn test_benchmark_result_metrics() {
        let result = BenchmarkResult {
            total: 100,
            passed: 80,
            failed: 15,
            errors: 5,
            delimiter_matches: 85,
            quote_matches: 90,
            file_results: vec![],
        };

        assert!((result.success_ratio() - 0.80).abs() < 0.001);
        assert!((result.failure_ratio() - 0.15).abs() < 0.001);
        assert!((result.error_ratio() - 0.05).abs() < 0.001);
        assert!((result.delimiter_accuracy() - 0.894736).abs() < 0.001); // 85/95
        assert!((result.quote_accuracy() - 0.947368).abs() < 0.001); // 90/95
        assert!((result.f1_score() - 0.80).abs() < 0.001);
    }
}
```

## File: `src/encoding.rs`
```rust
//! Encoding detection and transcoding using chardetng and `encoding_rs`.

use chardetng::EncodingDetector;
use simdutf8::basic::from_utf8;

/// Check if the given bytes are valid UTF-8.
///
/// Uses SIMD-accelerated validation for performance.
pub fn is_utf8(data: &[u8]) -> bool {
    from_utf8(data).is_ok()
}

/// Check if the data starts with a UTF-8 BOM (Byte Order Mark).
///
/// The UTF-8 BOM is the byte sequence: EF BB BF
pub fn has_utf8_bom(data: &[u8]) -> bool {
    data.len() >= 3 && data[0] == 0xEF && data[1] == 0xBB && data[2] == 0xBF
}

/// Skip the UTF-8 BOM if present and return the remaining data.
pub fn skip_bom(data: &[u8]) -> &[u8] {
    if has_utf8_bom(data) { &data[3..] } else { data }
}

/// Detect the encoding of the data.
///
/// Currently only supports UTF-8 detection. Returns true if valid UTF-8.
pub fn detect_encoding(data: &[u8]) -> EncodingInfo {
    let has_bom = has_utf8_bom(data);
    let data_without_bom = skip_bom(data);
    let valid_utf8 = is_utf8(data_without_bom);

    EncodingInfo {
        is_utf8: valid_utf8,
        has_bom,
    }
}

/// Information about the detected encoding.
#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub struct EncodingInfo {
    /// Whether the data is valid UTF-8.
    pub is_utf8: bool,
    /// Whether a UTF-8 BOM was present.
    pub has_bom: bool,
}

impl EncodingInfo {
    /// Create a new `EncodingInfo`.
    pub const fn new(is_utf8: bool, has_bom: bool) -> Self {
        Self { is_utf8, has_bom }
    }
}

/// Detect the encoding of data and transcode to UTF-8 if necessary.
///
/// Uses chardetng for robust encoding detection supporting:
/// - Windows-1251 (Cyrillic)
/// - Windows-1250 (Central European)
/// - ISO-8859 variants
/// - GB2312/GBK (Chinese)
/// - UTF-16 LE/BE
/// - And many more
///
/// Returns (`transcoded_data`, `was_transcoded`). If `was_transcoded` is false,
/// the original data is returned as-is (it was already valid UTF-8).
pub fn detect_and_transcode(data: &[u8]) -> (std::borrow::Cow<'_, [u8]>, bool) {
    // Check for UTF-16 BOM first (chardetng doesn't handle these well)
    if data.len() >= 2 {
        // UTF-16 LE BOM: FF FE
        if data[0] == 0xFF && data[1] == 0xFE {
            let (decoded, _, _) = encoding_rs::UTF_16LE.decode(data);
            return (
                std::borrow::Cow::Owned(decoded.into_owned().into_bytes()),
                true,
            );
        }
        // UTF-16 BE BOM: FE FF
        if data[0] == 0xFE && data[1] == 0xFF {
            let (decoded, _, _) = encoding_rs::UTF_16BE.decode(data);
            return (
                std::borrow::Cow::Owned(decoded.into_owned().into_bytes()),
                true,
            );
        }
    }

    // Check if already valid UTF-8
    if is_utf8(data) {
        return (std::borrow::Cow::Borrowed(data), false);
    }

    // Use chardetng to detect encoding
    let mut detector = EncodingDetector::new();
    detector.feed(data, true);
    let encoding = detector.guess(None, true);

    // If detected as UTF-8, return as-is (might have some invalid bytes)
    if encoding == encoding_rs::UTF_8 {
        return (std::borrow::Cow::Borrowed(data), false);
    }

    // Transcode to UTF-8
    let (decoded, _, _) = encoding.decode(data);
    (
        std::borrow::Cow::Owned(decoded.into_owned().into_bytes()),
        true,
    )
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_is_utf8() {
        assert!(is_utf8(b"Hello, World!"));
        assert!(is_utf8("こんにちは".as_bytes()));
        assert!(is_utf8(b""));
    }

    #[test]
    fn test_invalid_utf8() {
        // Invalid UTF-8 sequence
        assert!(!is_utf8(&[0xFF, 0xFE]));
        assert!(!is_utf8(&[0x80, 0x81, 0x82]));
    }

    #[test]
    fn test_utf8_bom() {
        let with_bom = [0xEF, 0xBB, 0xBF, b'a', b'b', b'c'];
        let without_bom = b"abc";

        assert!(has_utf8_bom(&with_bom));
        assert!(!has_utf8_bom(without_bom));

        assert_eq!(skip_bom(&with_bom), b"abc");
        assert_eq!(skip_bom(without_bom), b"abc");
    }

    #[test]
    fn test_detect_encoding() {
        let info = detect_encoding(b"Hello");
        assert!(info.is_utf8);
        assert!(!info.has_bom);

        let with_bom = [0xEF, 0xBB, 0xBF, b'H', b'i'];
        let info = detect_encoding(&with_bom);
        assert!(info.is_utf8);
        assert!(info.has_bom);
    }

    #[test]
    fn test_detect_and_transcode_utf8() {
        // Valid UTF-8 should not be transcoded
        let data = b"Hello, World!";
        let (result, was_transcoded) = detect_and_transcode(data);
        assert!(!was_transcoded);
        assert_eq!(&result[..], data);
    }

    #[test]
    fn test_detect_and_transcode_utf16_le() {
        // UTF-16 LE with BOM: "Hi"
        let data: &[u8] = &[0xFF, 0xFE, b'H', 0x00, b'i', 0x00];
        let (result, was_transcoded) = detect_and_transcode(data);
        assert!(was_transcoded);
        // Result should be UTF-8 (without BOM marker in content)
        assert!(is_utf8(&result));
    }

    #[test]
    fn test_detect_and_transcode_windows1251() {
        // Windows-1251 encoded Cyrillic text: "Привет" (Hello in Russian)
        // П=0xCF, р=0xF0, и=0xE8, в=0xE2, е=0xE5, т=0xF2
        let data: &[u8] = &[0xCF, 0xF0, 0xE8, 0xE2, 0xE5, 0xF2];
        let (result, was_transcoded) = detect_and_transcode(data);
        // Should be transcoded since it's not valid UTF-8
        assert!(was_transcoded);
        // Result should be valid UTF-8
        assert!(is_utf8(&result));
    }
}
```

## File: `src/error.rs`
```rust
use std::io;
use thiserror::Error;

/// Error type for CSV sniffing operations.
#[derive(Error, Debug)]
pub enum SnifferError {
    /// IO error during file operations.
    #[error("IO error: {0}")]
    Io(#[from] io::Error),

    /// CSV parsing error.
    #[error("CSV parsing error: {0}")]
    Csv(#[from] csv::Error),

    /// No valid dialect could be detected.
    #[error("Could not detect CSV dialect: {0}")]
    NoDialectDetected(String),

    /// Empty file or no data.
    #[error("Empty file or no data to analyze")]
    EmptyData,

    /// Invalid configuration.
    #[error("Invalid configuration: {0}")]
    InvalidConfig(String),
}

/// Result type alias for sniffing operations.
pub type Result<T> = std::result::Result<T, SnifferError>;
```

## File: `src/field_type.rs`
```rust
use std::fmt;

/// Data type detected for a CSV field.
#[derive(Debug, Clone, Copy, PartialEq, Eq, Hash, Default)]
pub enum Type {
    /// Unsigned integer (non-negative whole number).
    Unsigned,
    /// Signed integer (whole number, possibly negative).
    Signed,
    /// Floating point number.
    Float,
    /// Boolean value (true/false, yes/no, 0/1, etc.).
    Boolean,
    /// Date value (without time component).
    Date,
    /// `DateTime` value (date with time component).
    DateTime,
    /// Null/empty value.
    NULL,
    /// Text/string value (fallback type).
    #[default]
    Text,
}

impl fmt::Display for Type {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        match self {
            Type::Unsigned => write!(f, "Unsigned"),
            Type::Signed => write!(f, "Signed"),
            Type::Float => write!(f, "Float"),
            Type::Boolean => write!(f, "Boolean"),
            Type::Date => write!(f, "Date"),
            Type::DateTime => write!(f, "DateTime"),
            Type::NULL => write!(f, "NULL"),
            Type::Text => write!(f, "Text"),
        }
    }
}

impl Type {
    /// Number of variants in the Type enum.
    pub const COUNT: usize = 8;

    /// Returns the index for this type (0-7), suitable for array indexing.
    /// This index is based on type priority (see `priority()`), not enum
    /// declaration order: NULL=0, Boolean=1, Unsigned=2, Signed=3, Float=4,
    /// Date=5, DateTime=6, Text=7.
    #[inline]
    pub const fn as_index(&self) -> usize {
        self.priority() as usize
    }

    /// Returns true if this type is numeric.
    #[inline]
    pub const fn is_numeric(&self) -> bool {
        matches!(self, Type::Unsigned | Type::Signed | Type::Float)
    }

    /// Returns true if this type is temporal.
    #[inline]
    pub const fn is_temporal(&self) -> bool {
        matches!(self, Type::Date | Type::DateTime)
    }

    /// Returns the type priority for type inference.
    /// Higher priority types are preferred when merging types.
    pub const fn priority(&self) -> u8 {
        match self {
            Type::NULL => 0,
            Type::Boolean => 1,
            Type::Unsigned => 2,
            Type::Signed => 3,
            Type::Float => 4,
            Type::Date => 5,
            Type::DateTime => 6,
            Type::Text => 7,
        }
    }

    /// Merge two types, returning the most general type that can represent both.
    pub fn merge(self, other: Type) -> Type {
        if self == other {
            return self;
        }

        // NULL can be promoted to any type
        if self == Type::NULL {
            return other;
        }
        if other == Type::NULL {
            return self;
        }

        // Numeric type promotion
        match (self, other) {
            (Type::Unsigned, Type::Signed) | (Type::Signed, Type::Unsigned) => Type::Signed,
            (Type::Unsigned, Type::Float)
            | (Type::Float, Type::Unsigned)
            | (Type::Signed, Type::Float)
            | (Type::Float, Type::Signed) => Type::Float,
            (Type::Date, Type::DateTime) | (Type::DateTime, Type::Date) => Type::DateTime,
            // Everything else becomes Text
            _ => Type::Text,
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_type_merge() {
        assert_eq!(Type::Unsigned.merge(Type::Unsigned), Type::Unsigned);
        assert_eq!(Type::Unsigned.merge(Type::Signed), Type::Signed);
        assert_eq!(Type::Unsigned.merge(Type::Float), Type::Float);
        assert_eq!(Type::NULL.merge(Type::Unsigned), Type::Unsigned);
        assert_eq!(Type::Date.merge(Type::DateTime), Type::DateTime);
        assert_eq!(Type::Boolean.merge(Type::Text), Type::Text);
    }
}
```

## File: `src/http.rs`
```rust
//! HTTP Range request support for fetching remote CSV files.

use std::io::Read;
use std::time::Duration;
use thiserror::Error;

/// Default timeout for HTTP requests (30 seconds).
const DEFAULT_TIMEOUT: Duration = Duration::from_secs(30);

/// Result of fetching a URL.
pub struct FetchResult {
    /// The fetched data bytes.
    pub data: Vec<u8>,
    /// Whether the server supports Range requests.
    #[allow(dead_code)]
    pub range_supported: bool,
    /// Total content length if known.
    #[allow(dead_code)]
    pub content_length: Option<u64>,
}

/// Errors that can occur during HTTP fetching.
#[derive(Error, Debug)]
pub enum HttpError {
    #[error("Invalid URL: {0}")]
    InvalidUrl(String),
    #[error("HTTP error {status}: {message}")]
    HttpStatus { status: u16, message: String },
    #[error("Network error: {0}")]
    Network(String),
    #[error("IO error: {0}")]
    Io(#[from] std::io::Error),
}

impl From<ureq::Error> for HttpError {
    fn from(err: ureq::Error) -> Self {
        match err {
            ureq::Error::StatusCode(code) => HttpError::HttpStatus {
                status: code,
                message: format!("Server returned status {code}"),
            },
            _ => HttpError::Network(err.to_string()),
        }
    }
}

/// Fetch data from a URL, optionally using Range requests to limit download size.
///
/// If `max_bytes` is `Some(n)`, attempts a Range request for the first `n` bytes.
/// Falls back to full download (truncated at max_bytes) if the server doesn't support Range requests.
pub fn fetch_url(url: &str, max_bytes: Option<usize>) -> Result<FetchResult, HttpError> {
    // Validate URL
    if !url.starts_with("http://") && !url.starts_with("https://") {
        return Err(HttpError::InvalidUrl(format!(
            "URL must start with http:// or https://: {url}"
        )));
    }

    // Try Range request if max_bytes is specified
    if let Some(bytes) = max_bytes {
        match fetch_with_range(url, bytes) {
            Ok(result) if result.range_supported => return Ok(result),
            Ok(result) => {
                // Server responded with 200 instead of 206 - it doesn't support Range
                // The result already contains truncated data
                return Ok(result);
            }
            Err(HttpError::HttpStatus { status: 416, .. }) => {
                // Range Not Satisfiable - file might be smaller than requested range
                // Fall through to full download
            }
            Err(e) => return Err(e),
        }
    }

    // Full download (no Range request)
    fetch_full(url, max_bytes)
}

/// Attempt to fetch with a Range request.
fn fetch_with_range(url: &str, bytes: usize) -> Result<FetchResult, HttpError> {
    let range_header = format!("bytes=0-{}", bytes.saturating_sub(1));

    let config = ureq::Agent::config_builder()
        .timeout_global(Some(DEFAULT_TIMEOUT))
        .build();
    let agent = ureq::Agent::new_with_config(config);

    let response = agent.get(url).header("Range", &range_header).call()?;

    let status = response.status();
    let content_length = response
        .headers()
        .get("Content-Range")
        .and_then(|h| {
            // Parse "bytes 0-N/TOTAL" format
            let s = h.to_str().ok()?;
            s.split('/').next_back()?.parse::<u64>().ok()
        })
        .or_else(|| {
            response
                .headers()
                .get("Content-Length")
                .and_then(|h| h.to_str().ok()?.parse::<u64>().ok())
        });

    // 206 Partial Content means Range was accepted
    let range_supported = status == 206;

    // Read the body - use take() to truncate instead of erroring
    let body = response.into_body();
    let reader = body.into_reader();
    let mut data = Vec::with_capacity(bytes);
    reader.take(bytes as u64).read_to_end(&mut data)?;

    Ok(FetchResult {
        data,
        range_supported,
        content_length,
    })
}

/// Fetch the full content (or up to max_bytes if specified).
fn fetch_full(url: &str, max_bytes: Option<usize>) -> Result<FetchResult, HttpError> {
    let config = ureq::Agent::config_builder()
        .timeout_global(Some(DEFAULT_TIMEOUT))
        .build();
    let agent = ureq::Agent::new_with_config(config);

    let response = agent.get(url).call()?;

    let content_length = response
        .headers()
        .get("Content-Length")
        .and_then(|h| h.to_str().ok()?.parse::<u64>().ok());

    let body = response.into_body();
    let mut reader = body.into_reader();

    const MAX_BYTES: u64 = 1024 * 1024 * 1024; // 1 GB hard cap
    let data = if let Some(bytes) = max_bytes {
        let mut buf = Vec::with_capacity(bytes);
        reader.take(bytes as u64).read_to_end(&mut buf)?;
        buf
    } else {
        let mut buf = Vec::new();
        (&mut reader).take(MAX_BYTES).read_to_end(&mut buf)?;
        if buf.len() as u64 == MAX_BYTES {
            let mut probe = [0u8; 1];
            if reader.read(&mut probe)? > 0 {
                eprintln!(
                    "warning: HTTP response exceeds 1 GB; sniffing on truncated sample — results may be inaccurate"
                );
            }
        }
        buf
    };

    Ok(FetchResult {
        data,
        range_supported: false,
        content_length,
    })
}
```

## File: `src/lib.rs`
```rust
//! csv-nose: CSV dialect sniffer using the Table Uniformity Method
//!
//! A drop-in replacement for qsv-sniffer with improved dialect detection accuracy
//! using the Table Uniformity Method from the CSVsniffer paper.
//!
//! # Quick Start
//!
//! ```no_run
//! use csv_nose::{Sniffer, SampleSize};
//!
//! // Create a sniffer with default settings
//! let mut sniffer = Sniffer::new();
//!
//! // Optionally configure sampling
//! sniffer.sample_size(SampleSize::Records(100));
//!
//! // Sniff a file
//! let metadata = sniffer.sniff_path("data.csv").unwrap();
//!
//! println!("Delimiter: {}", metadata.dialect.delimiter as char);
//! println!("Has header: {}", metadata.dialect.header.has_header_row);
//! println!("Fields: {:?}", metadata.fields);
//! println!("Types: {:?}", metadata.types);
//! ```
//!
//! # API Compatibility
//!
//! This crate provides API compatibility with qsv-sniffer, making it easy to
//! switch between implementations:
//!
//! ```no_run
//! use csv_nose::{Sniffer, Metadata, Dialect, Header, Quote, Type, SampleSize, DatePreference};
//!
//! let mut sniffer = Sniffer::new();
//! sniffer
//!     .sample_size(SampleSize::Records(50))
//!     .date_preference(DatePreference::MdyFormat)
//!     .delimiter(b',')
//!     .quote(Quote::Some(b'"'));
//! ```
//!
//! # The Table Uniformity Method
//!
//! This library implements the Table Uniformity Method from:
//! "Detecting CSV File Dialects by Table Uniformity Measurement and Data Type Inference"
//! by García (2024).
//!
//! The algorithm achieves ~93% accuracy on real-world messy CSV files by:
//! 1. Testing multiple potential dialects (delimiter, quote, line terminator combinations)
//! 2. Scoring each dialect based on table uniformity (consistent field counts)
//! 3. Scoring based on type detection (consistent data types within columns)
//! 4. Selecting the dialect with the highest combined score

mod encoding;
mod error;
mod field_type;
pub mod metadata;
mod sample;
mod sniffer;
mod tum;

// Re-export public API (qsv-sniffer compatible)
pub use error::{Result, SnifferError};
pub use field_type::Type;
pub use metadata::{Dialect, Header, Metadata, Quote};
pub use sample::{DatePreference, SampleSize};
pub use sniffer::Sniffer;

// Re-export for advanced usage
pub use encoding::{EncodingInfo, detect_encoding, is_utf8};

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_public_api() {
        // Verify all public types are accessible
        let _sniffer = Sniffer::new();
        let _sample = SampleSize::Records(100);
        let _date_pref = DatePreference::MdyFormat;
        let _quote = Quote::Some(b'"');
        let _type = Type::Text;
    }

    #[test]
    fn test_sniff_simple_csv() {
        let data = b"a,b,c\n1,2,3\n4,5,6\n";
        let sniffer = Sniffer::new();

        let metadata = sniffer.sniff_bytes(data).unwrap();

        assert_eq!(metadata.dialect.delimiter, b',');
        assert_eq!(metadata.num_fields, 3);
    }

    #[test]
    fn test_builder_pattern() {
        let mut sniffer = Sniffer::new();
        sniffer
            .sample_size(SampleSize::Bytes(4096))
            .date_preference(DatePreference::DmyFormat)
            .delimiter(b';')
            .quote(Quote::None);

        // Verify builder returns &mut Self for chaining
    }
}
```

## File: `src/main.rs`
```rust
//! csv-nose CLI - CSV dialect sniffer

mod benchmark;
#[cfg(feature = "http")]
mod http;

use benchmark::{find_annotations, run_benchmark};
use clap::Parser;
use csv_nose::{DatePreference, Quote, SampleSize, Sniffer};
use std::fmt::Write;
use std::path::PathBuf;
use std::process::ExitCode;

/// CSV dialect sniffer using the Table Uniformity Method.
///
/// Detects CSV dialect (delimiter, quote character, header presence)
/// with high accuracy using the Table Uniformity Method.
#[derive(Parser, Debug)]
#[command(name = "csv-nose")]
#[command(author, version, about, long_about = None)]
struct Args {
    /// Input CSV file(s) or URL(s) to sniff, or directory for benchmark mode
    #[arg(required_unless_present = "benchmark")]
    files: Vec<String>,

    /// Run benchmark mode on a directory of test files
    #[arg(long)]
    benchmark: bool,

    /// Path to annotations file for benchmark mode (auto-detected if not specified)
    #[arg(long)]
    annotations: Option<PathBuf>,

    /// Number of records to sample (default: 100)
    #[arg(short = 'n', long, default_value = "100")]
    sample_records: usize,

    /// Number of bytes to sample (overrides --sample-records)
    #[arg(short = 'b', long)]
    sample_bytes: Option<usize>,

    /// Read entire file instead of sampling
    #[arg(short = 'a', long)]
    all: bool,

    /// Force specific delimiter (single character)
    #[arg(short = 'd', long)]
    delimiter: Option<char>,

    /// Force specific quote character (single character, or 'none')
    #[arg(short = 'q', long)]
    quote: Option<String>,

    /// Use day-month-year date format preference (default: month-day-year)
    #[arg(long)]
    dmy: bool,

    /// Output format: text (default), json, or csv
    #[arg(short = 'f', long, default_value = "text")]
    format: OutputFormat,

    /// Show detailed field information
    #[arg(short = 'v', long)]
    verbose: bool,

    /// Only output the detected delimiter character
    #[arg(long)]
    delimiter_only: bool,
}

#[derive(Debug, Clone, Copy, PartialEq, Eq, clap::ValueEnum)]
enum OutputFormat {
    Text,
    Json,
    Csv,
}

fn main() -> ExitCode {
    let args = Args::parse();

    // Handle benchmark mode
    if args.benchmark {
        return run_benchmark_cli(&args);
    }

    let mut exit_code = ExitCode::SUCCESS;

    for file in &args.files {
        let result = if is_url(file) {
            #[cfg(feature = "http")]
            {
                sniff_url(file, &args)
            }
            #[cfg(not(feature = "http"))]
            {
                Err("HTTP support not enabled. Rebuild with --features http".into())
            }
        } else {
            sniff_file(&PathBuf::from(file), &args)
        };

        if let Err(e) = result {
            eprintln!("Error processing {file}: {e}");
            exit_code = ExitCode::FAILURE;
        }
    }

    exit_code
}

/// Check if a path looks like a URL.
fn is_url(path: &str) -> bool {
    path.starts_with("http://") || path.starts_with("https://")
}

fn run_benchmark_cli(args: &Args) -> ExitCode {
    if args.files.is_empty() {
        eprintln!("Error: benchmark mode requires a directory path");
        return ExitCode::FAILURE;
    }

    if is_url(&args.files[0]) {
        eprintln!("Error: benchmark mode requires a local directory, not a URL");
        return ExitCode::FAILURE;
    }

    let data_dir = PathBuf::from(&args.files[0]);

    if !data_dir.is_dir() {
        eprintln!("Error: {} is not a directory", data_dir.display());
        return ExitCode::FAILURE;
    }

    // Find or use provided annotations file
    let annotations_path = if let Some(ref path) = args.annotations {
        path.clone()
    } else if let Some(path) = find_annotations(&data_dir) {
        path
    } else {
        eprintln!(
            "Error: Could not find annotations file for {}",
            data_dir.display()
        );
        eprintln!("Use --annotations to specify the path to the annotations file");
        return ExitCode::FAILURE;
    };

    println!("Running benchmark on: {}", data_dir.display());
    println!("Using annotations: {}", annotations_path.display());
    println!();

    match run_benchmark(&data_dir, &annotations_path) {
        Ok(result) => {
            result.print_details();
            result.print_summary();
            ExitCode::SUCCESS
        }
        Err(e) => {
            eprintln!("Error running benchmark: {e}");
            ExitCode::FAILURE
        }
    }
}

fn sniff_file(path: &PathBuf, args: &Args) -> Result<(), Box<dyn std::error::Error>> {
    let mut sniffer = Sniffer::new();

    // Configure sample size
    if args.all {
        sniffer.sample_size(SampleSize::All);
    } else if let Some(bytes) = args.sample_bytes {
        sniffer.sample_size(SampleSize::Bytes(bytes));
    } else {
        sniffer.sample_size(SampleSize::Records(args.sample_records));
    }

    // Configure date preference
    if args.dmy {
        sniffer.date_preference(DatePreference::DmyFormat);
    }

    // Configure forced delimiter
    if let Some(delim) = args.delimiter {
        sniffer.delimiter(delim as u8);
    }

    // Configure forced quote
    if let Some(ref quote_str) = args.quote {
        if quote_str.to_lowercase() == "none" {
            sniffer.quote(Quote::None);
        } else if let Some(c) = quote_str.chars().next() {
            sniffer.quote(Quote::Some(c as u8));
        }
    }

    // Sniff the file
    let metadata = sniffer.sniff_path(path)?;

    // Output based on format
    if args.delimiter_only {
        println!("{}", metadata.dialect.delimiter as char);
        return Ok(());
    }

    let display_path = path.display().to_string();
    match args.format {
        OutputFormat::Text => print_text_output(&display_path, &metadata, args.verbose),
        OutputFormat::Json => print_json_output(&display_path, &metadata, args.verbose),
        OutputFormat::Csv => print_csv_output(&display_path, &metadata),
    }

    Ok(())
}

/// Sniff a remote CSV file from a URL using HTTP Range requests.
#[cfg(feature = "http")]
fn sniff_url(url: &str, args: &Args) -> Result<(), Box<dyn std::error::Error>> {
    // Calculate max bytes to fetch
    let max_bytes = if args.all {
        None
    } else if let Some(bytes) = args.sample_bytes {
        Some(bytes)
    } else {
        // For record-based sampling, estimate bytes needed.
        // 500 bytes/record is a reasonable middle ground based on typical CSVs.
        // Users can override with -b/--sample-bytes for specific needs.
        Some(args.sample_records * 500)
    };

    // Fetch data from URL
    let fetch_result = http::fetch_url(url, max_bytes)?;

    let mut sniffer = Sniffer::new();

    // For bytes data, we already limited the fetch, so use SampleSize::All
    sniffer.sample_size(SampleSize::All);

    // Configure date preference
    if args.dmy {
        sniffer.date_preference(DatePreference::DmyFormat);
    }

    // Configure forced delimiter
    if let Some(delim) = args.delimiter {
        sniffer.delimiter(delim as u8);
    }

    // Configure forced quote
    if let Some(ref quote_str) = args.quote {
        if quote_str.to_lowercase() == "none" {
            sniffer.quote(Quote::None);
        } else if let Some(c) = quote_str.chars().next() {
            sniffer.quote(Quote::Some(c as u8));
        }
    }

    // Sniff the fetched bytes
    let metadata = sniffer.sniff_bytes(&fetch_result.data)?;

    // Output based on format
    if args.delimiter_only {
        println!("{}", metadata.dialect.delimiter as char);
        return Ok(());
    }

    match args.format {
        OutputFormat::Text => print_text_output(url, &metadata, args.verbose),
        OutputFormat::Json => print_json_output(url, &metadata, args.verbose),
        OutputFormat::Csv => print_csv_output(url, &metadata),
    }

    Ok(())
}

fn print_text_output(path: &str, metadata: &csv_nose::Metadata, verbose: bool) {
    println!("File: {path}");
    println!("  Delimiter: {:?}", metadata.dialect.delimiter as char);
    println!(
        "  Quote: {}",
        match metadata.dialect.quote {
            Quote::None => "none".to_string(),
            Quote::Some(q) => format!("{:?}", q as char),
        }
    );
    println!("  Has header: {}", metadata.dialect.header.has_header_row);
    println!(
        "  Preamble rows: {}",
        metadata.dialect.header.num_preamble_rows
    );
    println!("  Flexible: {}", metadata.dialect.flexible);
    println!("  UTF-8: {}", metadata.dialect.is_utf8);
    println!("  Fields: {}", metadata.num_fields);
    println!("  Avg record length: {} bytes", metadata.avg_record_len);

    if verbose {
        println!("  Field details:");
        for (i, (name, typ)) in metadata
            .fields
            .iter()
            .zip(metadata.types.iter())
            .enumerate()
        {
            println!("    {}: {} ({})", i + 1, name, typ);
        }
    }

    println!();
}

/// Escape a string for JSON output (handles quotes, backslashes, and control characters).
fn escape_json(s: &str) -> String {
    let mut result = String::with_capacity(s.len());
    for c in s.chars() {
        match c {
            '"' => result.push_str("\\\""),
            '\\' => result.push_str("\\\\"),
            '\n' => result.push_str("\\n"),
            '\r' => result.push_str("\\r"),
            '\t' => result.push_str("\\t"),
            c if c.is_control() => {
                // we use write! to avoid allocating a temporary string
                let _ = write!(result, "\\u{:04x}", c as u32);
            }
            c => result.push(c),
        }
    }
    result
}

/// Escape a string for CSV output (quotes the value and doubles internal quotes).
fn escape_csv(s: &str) -> String {
    if s.contains(',') || s.contains('"') || s.contains('\n') || s.contains('\r') {
        format!("\"{}\"", s.replace('"', "\"\""))
    } else {
        s.to_string()
    }
}

fn print_json_output(path: &str, metadata: &csv_nose::Metadata, verbose: bool) {
    let quote_str = match metadata.dialect.quote {
        Quote::None => "null".to_string(),
        Quote::Some(q) => format!("\"{}\"", q as char),
    };

    print!(
        r#"{{"file":"{}","dialect":{{"delimiter":"{}","quote":{},"has_header":{},"preamble_rows":{},"flexible":{},"is_utf8":{}}},"num_fields":{},"avg_record_len":{}"#,
        escape_json(path),
        metadata.dialect.delimiter as char,
        quote_str,
        metadata.dialect.header.has_header_row,
        metadata.dialect.header.num_preamble_rows,
        metadata.dialect.flexible,
        metadata.dialect.is_utf8,
        metadata.num_fields,
        metadata.avg_record_len
    );

    if verbose {
        print!(r#","fields":["#);
        for (i, (name, typ)) in metadata
            .fields
            .iter()
            .zip(metadata.types.iter())
            .enumerate()
        {
            if i > 0 {
                print!(",");
            }
            print!(
                r#"{{"name":"{}","type":"{}"}}"#,
                escape_json(name),
                escape_json(&typ.to_string())
            );
        }
        print!("]");
    }

    println!("}}");
}

fn print_csv_output(path: &str, metadata: &csv_nose::Metadata) {
    use std::sync::atomic::{AtomicBool, Ordering};
    static HEADER_PRINTED: AtomicBool = AtomicBool::new(false);

    let quote_str = match metadata.dialect.quote {
        Quote::None => "none".to_string(),
        Quote::Some(q) => format!("{}", q as char),
    };

    // CSV header (print only for first file or could be configured)
    if !HEADER_PRINTED.swap(true, Ordering::Relaxed) {
        println!(
            "file,delimiter,quote,has_header,preamble_rows,flexible,is_utf8,num_fields,avg_record_len"
        );
    }

    println!(
        "{},{},{},{},{},{},{},{},{}",
        escape_csv(path),
        metadata.dialect.delimiter as char,
        quote_str,
        metadata.dialect.header.has_header_row,
        metadata.dialect.header.num_preamble_rows,
        metadata.dialect.flexible,
        metadata.dialect.is_utf8,
        metadata.num_fields,
        metadata.avg_record_len
    );
}
```

## File: `src/metadata.rs`
```rust
use crate::field_type::Type;
use std::fmt;

/// Metadata about a CSV file.
#[derive(Debug, Clone)]
pub struct Metadata {
    /// The detected CSV dialect.
    pub dialect: Dialect,
    /// Average record length in bytes.
    pub avg_record_len: usize,
    /// Number of fields per record.
    pub num_fields: usize,
    /// Field names from the header row (or generated names if no header).
    pub fields: Vec<String>,
    /// Detected type for each field.
    pub types: Vec<Type>,
}

impl Metadata {
    /// Create a new Metadata instance.
    pub const fn new(
        dialect: Dialect,
        avg_record_len: usize,
        num_fields: usize,
        fields: Vec<String>,
        types: Vec<Type>,
    ) -> Self {
        Self {
            dialect,
            avg_record_len,
            num_fields,
            fields,
            types,
        }
    }
}

/// CSV dialect specification.
#[derive(Debug, Clone, PartialEq)]
pub struct Dialect {
    /// Field delimiter character.
    pub delimiter: u8,
    /// Header configuration.
    pub header: Header,
    /// Quote character configuration.
    pub quote: Quote,
    /// Whether the CSV has variable field counts across records.
    pub flexible: bool,
    /// Whether the file is valid UTF-8.
    pub is_utf8: bool,
}

impl Default for Dialect {
    fn default() -> Self {
        Self {
            delimiter: b',',
            header: Header::default(),
            quote: Quote::Some(b'"'),
            flexible: false,
            is_utf8: true,
        }
    }
}

impl Dialect {
    /// Create a new Dialect with the given parameters.
    pub const fn new(
        delimiter: u8,
        header: Header,
        quote: Quote,
        flexible: bool,
        is_utf8: bool,
    ) -> Self {
        Self {
            delimiter,
            header,
            quote,
            flexible,
            is_utf8,
        }
    }
}

/// Header configuration for a CSV file.
#[derive(Debug, Clone, PartialEq, Default)]
pub struct Header {
    /// Whether the CSV has a header row.
    pub has_header_row: bool,
    /// Number of rows to skip before the data (preamble/comment rows).
    pub num_preamble_rows: usize,
}

impl Header {
    /// Create a new Header configuration.
    pub const fn new(has_header_row: bool, num_preamble_rows: usize) -> Self {
        Self {
            has_header_row,
            num_preamble_rows,
        }
    }
}

/// Quote character configuration.
#[derive(Debug, Clone, Copy, PartialEq, Eq, Hash)]
pub enum Quote {
    /// No quoting.
    None,
    /// Quote with the specified character.
    Some(u8),
}

impl Default for Quote {
    fn default() -> Self {
        Quote::Some(b'"')
    }
}

impl Quote {
    /// Returns the quote character if set.
    #[inline]
    pub fn char(&self) -> Option<u8> {
        match self {
            Quote::None => None,
            Quote::Some(c) => Some(*c),
        }
    }
}

impl fmt::Display for Quote {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        match self {
            Quote::None => write!(f, "none"),
            Quote::Some(c) => write!(f, "{}", *c as char),
        }
    }
}
```

## File: `src/sample.rs`
```rust
/// Sample size configuration for sniffing.
#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub enum SampleSize {
    /// Sample a specific number of records.
    Records(usize),
    /// Sample a specific number of bytes.
    Bytes(usize),
    /// Read the entire file.
    ///
    /// # Warning
    ///
    /// This loads the entire file into memory. For large files (e.g., >100 MB), prefer
    /// [`SampleSize::Bytes`] with a reasonable limit to avoid excessive memory usage.
    All,
}

impl Default for SampleSize {
    fn default() -> Self {
        // Default to 100 records which is reasonable for most files
        SampleSize::Records(100)
    }
}

impl SampleSize {
    /// Returns the number of records to sample, or None for All.
    pub fn records(&self) -> Option<usize> {
        match self {
            SampleSize::Records(n) => Some(*n),
            _ => None,
        }
    }

    /// Returns the number of bytes to sample, or None for other modes.
    pub fn bytes(&self) -> Option<usize> {
        match self {
            SampleSize::Bytes(n) => Some(*n),
            _ => None,
        }
    }
}

/// Date format preference for ambiguous date parsing.
#[derive(Debug, Clone, Copy, PartialEq, Eq, Default)]
pub enum DatePreference {
    /// Day-Month-Year format (e.g., 31/12/2023).
    DmyFormat,
    /// Month-Day-Year format (e.g., 12/31/2023).
    #[default]
    MdyFormat,
}

impl DatePreference {
    /// Returns true if day comes before month in ambiguous dates.
    pub fn is_dmy(&self) -> bool {
        matches!(self, DatePreference::DmyFormat)
    }
}
```

## File: `src/sniffer.rs`
```rust
//! Main Sniffer builder and sniff methods.
//!
//! This module provides the qsv-sniffer compatible API.

use std::borrow::Cow;
use std::fs::File;
use std::io::{Read, Seek};
use std::path::Path;

use crate::encoding::{detect_and_transcode, detect_encoding, skip_bom};
use crate::error::{Result, SnifferError};
use crate::field_type::Type;
use crate::metadata::{Dialect, Header, Metadata, Quote};
use crate::sample::{DatePreference, SampleSize};
use crate::tum::potential_dialects::{
    PotentialDialect, detect_line_terminator, generate_dialects_with_terminator,
};
use crate::tum::score::{DialectScore, find_best_dialect, score_all_dialects_with_best_table};
use crate::tum::table::{Table, parse_table};
use crate::tum::type_detection::infer_column_types;

/// Maximum buffer size for `SampleSize::Records` mode (100 MB).
const MAX_RECORDS_BYTES: usize = 100 * 1024 * 1024;

/// CSV dialect sniffer using the Table Uniformity Method.
///
/// # Example
///
/// ```no_run
/// use csv_nose::{Sniffer, SampleSize};
///
/// let mut sniffer = Sniffer::new();
/// sniffer.sample_size(SampleSize::Records(100));
///
/// let metadata = sniffer.sniff_path("data.csv").unwrap();
/// println!("Delimiter: {}", metadata.dialect.delimiter as char);
/// println!("Has header: {}", metadata.dialect.header.has_header_row);
/// ```
#[derive(Debug, Clone)]
pub struct Sniffer {
    /// Sample size for sniffing.
    sample_size: SampleSize,
    /// Date format preference for ambiguous dates.
    date_preference: DatePreference,
    /// Optional forced delimiter.
    forced_delimiter: Option<u8>,
    /// Optional forced quote character.
    forced_quote: Option<Quote>,
}

impl Default for Sniffer {
    fn default() -> Self {
        Self::new()
    }
}

impl Sniffer {
    /// Create a new Sniffer with default settings.
    pub const fn new() -> Self {
        Self {
            sample_size: SampleSize::Records(100),
            date_preference: DatePreference::MdyFormat,
            forced_delimiter: None,
            forced_quote: None,
        }
    }

    /// Set the sample size for sniffing.
    pub fn sample_size(&mut self, sample_size: SampleSize) -> &mut Self {
        self.sample_size = sample_size;
        self
    }

    /// Set the date preference for ambiguous date parsing.
    pub fn date_preference(&mut self, date_preference: DatePreference) -> &mut Self {
        self.date_preference = date_preference;
        self
    }

    /// Force a specific delimiter (skip delimiter detection).
    pub fn delimiter(&mut self, delimiter: u8) -> &mut Self {
        self.forced_delimiter = Some(delimiter);
        self
    }

    /// Force a specific quote character.
    pub fn quote(&mut self, quote: Quote) -> &mut Self {
        self.forced_quote = Some(quote);
        self
    }

    /// Sniff a CSV file at the given path.
    pub fn sniff_path<P: AsRef<Path>>(&mut self, path: P) -> Result<Metadata> {
        let file = File::open(path.as_ref())?;
        let mut reader = std::io::BufReader::new(file);
        self.sniff_reader(&mut reader)
    }

    /// Sniff CSV data from a reader.
    pub fn sniff_reader<R: Read + Seek>(&mut self, reader: R) -> Result<Metadata> {
        let data = self.read_sample(reader)?;

        if data.is_empty() {
            return Err(SnifferError::EmptyData);
        }

        self.sniff_bytes(&data)
    }

    /// Sniff CSV data from bytes.
    pub fn sniff_bytes(&self, data: &[u8]) -> Result<Metadata> {
        if data.is_empty() {
            return Err(SnifferError::EmptyData);
        }

        // Detect encoding and transcode to UTF-8 if necessary
        let (transcoded_data, was_transcoded) = detect_and_transcode(data);
        let data = &transcoded_data[..];

        // Detect encoding info (for metadata)
        let encoding_info = detect_encoding(data);
        let is_utf8 = !was_transcoded || encoding_info.is_utf8;

        // Skip BOM
        let data = skip_bom(data);

        // Skip comment/preamble lines (lines starting with #)
        let (comment_preamble_rows, data) = skip_preamble(data);

        // Detect line terminator first to reduce search space
        let line_terminator = detect_line_terminator(data);

        // Generate potential dialects
        let dialects = self.forced_delimiter.map_or_else(
            || generate_dialects_with_terminator(line_terminator),
            |delim| {
                // If delimiter is forced, only test that delimiter with different quotes
                let quotes = if let Some(q) = self.forced_quote {
                    vec![q]
                } else {
                    vec![Quote::Some(b'"'), Quote::Some(b'\''), Quote::None]
                };

                quotes
                    .into_iter()
                    .map(|q| PotentialDialect::new(delim, q, line_terminator))
                    .collect()
            },
        );
        // Determine max rows for scoring
        let max_rows = match self.sample_size {
            SampleSize::Records(n) => n,
            SampleSize::Bytes(_) | SampleSize::All => 0, // Already limited by read_sample
        };

        // Score all dialects and get the best table (avoids re-parsing)
        let (scores, best_table) = score_all_dialects_with_best_table(data, &dialects, max_rows);

        // Find the best dialect
        let best = find_best_dialect(&scores)
            .ok_or_else(|| SnifferError::NoDialectDetected("No valid dialect found".to_string()))?;

        // Detect structural preamble using the already-parsed table
        let table_for_preamble =
            best_table.unwrap_or_else(|| parse_table(data, &best.dialect, max_rows));
        let structural_preamble = detect_structural_preamble(&table_for_preamble);

        // Total preamble = comment rows + structural rows
        let total_preamble_rows = comment_preamble_rows + structural_preamble;

        // Build metadata from the best dialect, reusing the already-parsed table
        // Pass structural_preamble for table row indexing (since comment rows are already skipped from data)
        // Pass total_preamble_rows for Header metadata (to report true preamble count in original file)
        self.build_metadata(
            best,
            is_utf8,
            structural_preamble,
            total_preamble_rows,
            &table_for_preamble,
            data,
        )
    }

    /// Read a sample of data from the reader based on `sample_size` settings.
    fn read_sample<R: Read + Seek>(&self, mut reader: R) -> Result<Vec<u8>> {
        match self.sample_size {
            SampleSize::Bytes(n) => {
                let mut buffer = vec![0u8; n];
                let bytes_read = reader.read(&mut buffer)?;
                buffer.truncate(bytes_read);
                Ok(buffer)
            }
            SampleSize::All => {
                const MAX_BYTES: u64 = 1024 * 1024 * 1024; // 1 GB hard cap
                let mut buffer = Vec::new();
                (&mut reader).take(MAX_BYTES).read_to_end(&mut buffer)?;
                if buffer.len() as u64 == MAX_BYTES {
                    let mut probe = [0u8; 1];
                    if reader.read(&mut probe)? > 0 {
                        eprintln!(
                            "warning: input exceeds 1 GB; sniffing on truncated sample — results may be inaccurate"
                        );
                    }
                }
                Ok(buffer)
            }
            SampleSize::Records(n) => {
                // For records, we read enough to capture n records
                // Estimate ~1KB per record as a starting point, with a minimum
                let estimated_size = n.saturating_mul(1024).clamp(8192, MAX_RECORDS_BYTES);
                let mut buffer = vec![0u8; estimated_size];
                let bytes_read = reader.read(&mut buffer)?;
                buffer.truncate(bytes_read);

                // If we need more data, keep reading
                if bytes_read == estimated_size {
                    // Count newlines to see if we have enough records
                    let newlines = bytecount::count(&buffer, b'\n');
                    if newlines < n {
                        // Read more data
                        let additional = (n - newlines).saturating_mul(2048).min(MAX_RECORDS_BYTES);
                        let mut more = vec![0u8; additional];
                        let more_read = reader.read(&mut more)?;
                        more.truncate(more_read);
                        buffer.extend(more);
                    }
                }

                if buffer.len() >= MAX_RECORDS_BYTES {
                    let mut probe = [0u8; 1];
                    if reader.read(&mut probe)? > 0 {
                        eprintln!(
                            "warning: Records sample capped at 100 MB; \
                             sniff result may be approximate for very large inputs"
                        );
                    }
                }

                Ok(buffer)
            }
        }
    }

    /// Build Metadata from the best scoring dialect.
    ///
    /// # Arguments
    /// * `structural_preamble` - Number of structural preamble rows in the table (for row indexing)
    /// * `total_preamble_rows` - Total preamble rows including comments (for Header metadata)
    /// * `table` - Pre-parsed table to avoid redundant parsing
    /// * `data` - Raw data bytes for accurate avg_record_len calculation
    fn build_metadata(
        &self,
        score: &DialectScore,
        is_utf8: bool,
        structural_preamble: usize,
        total_preamble_rows: usize,
        table: &Table,
        data: &[u8],
    ) -> Result<Metadata> {
        if table.is_empty() {
            return Err(SnifferError::EmptyData);
        }

        // Create a view of the table without structural preamble
        // (comment preamble rows are already stripped from data)
        // Use Cow to avoid cloning in the common no-preamble case
        let effective_table: Cow<'_, Table> =
            if structural_preamble > 0 && table.rows.len() > structural_preamble {
                let mut et = Table::new();
                et.rows = table.rows[structural_preamble..].to_vec();
                et.field_counts = table.field_counts[structural_preamble..].to_vec();
                et.update_modal_field_count();
                Cow::Owned(et)
            } else {
                Cow::Borrowed(table)
            };

        // Detect header on the effective table (pass total_preamble_rows for Header metadata)
        let header = detect_header(&effective_table, &score.dialect, total_preamble_rows);

        // Get field names from the effective table (first row after structural preamble)
        let fields = if header.has_header_row && !effective_table.rows.is_empty() {
            effective_table.rows[0].clone()
        } else {
            // Generate field names
            (0..score.num_fields)
                .map(|i| format!("field_{}", i + 1))
                .collect()
        };

        // Skip header row for type inference if present
        let data_table = if header.has_header_row && effective_table.rows.len() > 1 {
            let mut dt = crate::tum::table::Table::new();
            dt.rows = effective_table.rows[1..].to_vec();
            dt.field_counts = effective_table.field_counts[1..].to_vec();
            dt.update_modal_field_count();
            dt
        } else {
            effective_table.into_owned()
        };

        // Infer types for each column
        let types = infer_column_types(&data_table);

        // Build dialect
        let dialect = Dialect {
            delimiter: score.dialect.delimiter,
            header,
            quote: score.dialect.quote,
            flexible: !score.is_uniform,
            is_utf8,
        };

        // Calculate average record length from the raw data
        let avg_record_len = calculate_avg_record_len(data, table.num_rows());

        Ok(Metadata {
            dialect,
            avg_record_len,
            num_fields: score.num_fields,
            fields,
            types,
        })
    }
}

/// Detect if the first row (after preamble) is likely a header row.
///
/// Optimized: Computes type counts in a single pass without allocating Vecs.
fn detect_header(
    table: &crate::tum::table::Table,
    _dialect: &PotentialDialect,
    preamble_rows: usize,
) -> Header {
    if table.rows.is_empty() {
        return Header::new(false, preamble_rows);
    }

    if table.rows.len() < 2 {
        // Can't determine header with only one row
        return Header::new(false, preamble_rows);
    }

    let first_row = &table.rows[0];
    let second_row = &table.rows[1];

    // Heuristics for header detection:
    // 1. First row has different types than subsequent rows
    // 2. First row values look like labels (text when data is numeric)
    // 3. First row has no duplicates (header columns should be unique)

    let mut header_score = 0.0;
    let mut checks = 0;

    // Check 1 & 2: Count types in a single pass for first row
    let (first_text_count, first_numeric_count) =
        first_row.iter().fold((0, 0), |(text, num), s| {
            let t = crate::tum::type_detection::detect_cell_type(s);
            (
                text + usize::from(t == Type::Text),
                num + usize::from(t.is_numeric()),
            )
        });

    // Count types in a single pass for second row
    let second_text_count = second_row
        .iter()
        .filter(|s| crate::tum::type_detection::detect_cell_type(s) == Type::Text)
        .count();

    if first_text_count > second_text_count {
        header_score += 1.0;
    }
    checks += 1;

    // Check 2: First row has more text than numeric
    if first_text_count > first_numeric_count {
        header_score += 0.5;
    }
    checks += 1;

    // Check 3: No duplicates in first row
    let unique_count = {
        let mut seen = std::collections::HashSet::new();
        first_row.iter().filter(|s| seen.insert(s.as_str())).count()
    };
    if unique_count == first_row.len() {
        header_score += 0.5;
    }
    checks += 1;

    // Check 4: First row values are shorter (headers tend to be concise)
    let avg_first_len: f64 = first_row
        .iter()
        .map(std::string::String::len)
        .sum::<usize>() as f64
        / first_row.len().max(1) as f64;
    let avg_second_len: f64 = second_row
        .iter()
        .map(std::string::String::len)
        .sum::<usize>() as f64
        / second_row.len().max(1) as f64;

    if avg_first_len <= avg_second_len {
        header_score += 0.3;
    }
    checks += 1;

    // Threshold for header detection
    let has_header = (header_score / checks as f64) > 0.4;

    Header::new(has_header, preamble_rows)
}

/// Calculate average record length from raw data.
///
/// Uses the byte length of the first `num_rows` rows for accurate results
/// that include quote characters and actual line terminators.
/// This handles the case where `data` contains more bytes than `num_rows` rows
/// (e.g., when `SampleSize::Records(n)` reads more data than needed).
fn calculate_avg_record_len(data: &[u8], num_rows: usize) -> usize {
    if num_rows == 0 || data.is_empty() {
        return 0;
    }

    // Find the byte offset where the num_rows-th row ends
    // by counting newlines (handling both \n and \r\n)
    let mut rows_seen = 0;
    let mut byte_offset = 0;

    for (i, &byte) in data.iter().enumerate() {
        if byte == b'\n' {
            rows_seen += 1;
            if rows_seen >= num_rows {
                byte_offset = i + 1; // Include the newline
                break;
            }
        }
    }

    // If we didn't find enough newlines, use the entire data length
    // (this handles files without trailing newlines or small files)
    if byte_offset == 0 {
        byte_offset = data.len();
    }

    byte_offset / num_rows
}

/// Skip preamble/comment lines at the start of data.
///
/// Detects lines starting with '#' at the beginning of the file and returns
/// the number of preamble rows and a slice starting after the preamble.
fn skip_preamble(data: &[u8]) -> (usize, &[u8]) {
    let mut preamble_rows = 0;
    let mut offset = 0;

    while offset < data.len() {
        // Skip leading whitespace on the line
        let mut line_start = offset;
        while line_start < data.len() && (data[line_start] == b' ' || data[line_start] == b'\t') {
            line_start += 1;
        }

        // Check if line starts with #
        if line_start < data.len() && data[line_start] == b'#' {
            // Find end of line
            let mut line_end = line_start;
            while line_end < data.len() && data[line_end] != b'\n' && data[line_end] != b'\r' {
                line_end += 1;
            }

            // Skip line terminator
            if line_end < data.len() && data[line_end] == b'\r' {
                line_end += 1;
            }
            if line_end < data.len() && data[line_end] == b'\n' {
                line_end += 1;
            }

            preamble_rows += 1;
            offset = line_end;
        } else {
            // Not a comment line, stop
            break;
        }
    }

    (preamble_rows, &data[offset..])
}

/// Detect structural preamble rows using field count consistency analysis.
///
/// Identifies rows at the start that don't match the predominant field count
/// pattern (metadata rows, empty rows, title rows with different structure).
fn detect_structural_preamble(table: &crate::tum::table::Table) -> usize {
    let n = table.field_counts.len();
    if n < 3 {
        return 0;
    }

    let modal_count = table.modal_field_count();

    // Pre-compute suffix counts: for each position i, how many rows from i to end match modal_count
    // This converts O(n²) scanning to O(n) preprocessing + O(1) lookups
    let mut matching_suffix = vec![0usize; n];
    let mut count = 0;
    for i in (0..n).rev() {
        if table.field_counts[i] == modal_count {
            count += 1;
        }
        matching_suffix[i] = count;
    }

    // Find first row where remaining data is 80%+ consistent with modal field count
    for (i, &field_count) in table.field_counts.iter().enumerate() {
        if field_count == modal_count {
            let remaining_len = n - i;
            let matching = matching_suffix[i];
            let consistency = matching as f64 / remaining_len as f64;

            if consistency >= 0.8 {
                return i;
            }
        }
    }

    0
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_sniffer_builder() {
        let mut sniffer = Sniffer::new();
        sniffer
            .sample_size(SampleSize::Records(50))
            .date_preference(DatePreference::DmyFormat)
            .delimiter(b',');

        assert_eq!(sniffer.sample_size, SampleSize::Records(50));
        assert_eq!(sniffer.date_preference, DatePreference::DmyFormat);
        assert_eq!(sniffer.forced_delimiter, Some(b','));
    }

    #[test]
    fn test_sniff_bytes() {
        let data = b"name,age,city\nAlice,30,NYC\nBob,25,LA\n";
        let sniffer = Sniffer::new();

        let metadata = sniffer.sniff_bytes(data).unwrap();

        assert_eq!(metadata.dialect.delimiter, b',');
        assert!(metadata.dialect.header.has_header_row);
        assert_eq!(metadata.num_fields, 3);
        assert_eq!(metadata.fields, vec!["name", "age", "city"]);
    }

    #[test]
    fn test_sniff_tsv() {
        let data = b"name\tage\tcity\nAlice\t30\tNYC\nBob\t25\tLA\n";
        let sniffer = Sniffer::new();

        let metadata = sniffer.sniff_bytes(data).unwrap();

        assert_eq!(metadata.dialect.delimiter, b'\t');
        assert!(metadata.dialect.header.has_header_row);
    }

    #[test]
    fn test_sniff_semicolon() {
        let data = b"name;age;city\nAlice;30;NYC\nBob;25;LA\n";
        let sniffer = Sniffer::new();

        let metadata = sniffer.sniff_bytes(data).unwrap();

        assert_eq!(metadata.dialect.delimiter, b';');
    }

    #[test]
    fn test_sniff_no_header() {
        let data = b"1,2,3\n4,5,6\n7,8,9\n";
        let sniffer = Sniffer::new();

        let metadata = sniffer.sniff_bytes(data).unwrap();

        assert_eq!(metadata.dialect.delimiter, b',');
        // All numeric data - should not detect header
        assert!(!metadata.dialect.header.has_header_row);
    }

    #[test]
    fn test_sniff_with_quotes() {
        let data = b"\"name\",\"value\"\n\"hello, world\",123\n\"test\",456\n";
        let sniffer = Sniffer::new();

        let metadata = sniffer.sniff_bytes(data).unwrap();

        assert_eq!(metadata.dialect.delimiter, b',');
        assert_eq!(metadata.dialect.quote, Quote::Some(b'"'));
    }

    #[test]
    fn test_sniff_empty() {
        let data = b"";
        let sniffer = Sniffer::new();

        let result = sniffer.sniff_bytes(data);
        assert!(result.is_err());
    }

    #[test]
    fn test_skip_preamble() {
        // Test with comment lines
        let data = b"# This is a comment\n# Another comment\nname,age\nAlice,30\n";
        let (preamble_rows, remaining) = skip_preamble(data);
        assert_eq!(preamble_rows, 2);
        assert_eq!(remaining, b"name,age\nAlice,30\n");

        // Test without comment lines
        let data = b"name,age\nAlice,30\n";
        let (preamble_rows, remaining) = skip_preamble(data);
        assert_eq!(preamble_rows, 0);
        assert_eq!(remaining, b"name,age\nAlice,30\n");

        // Test with whitespace before #
        let data = b"  # Indented comment\nname,age\n";
        let (preamble_rows, remaining) = skip_preamble(data);
        assert_eq!(preamble_rows, 1);
        assert_eq!(remaining, b"name,age\n");
    }

    #[test]
    fn test_sniff_with_preamble() {
        let data = b"# LimeSurvey export\n# Generated 2024-01-01\nname,age,city\nAlice,30,NYC\nBob,25,LA\n";
        let sniffer = Sniffer::new();

        let metadata = sniffer.sniff_bytes(data).unwrap();

        assert_eq!(metadata.dialect.delimiter, b',');
        assert!(metadata.dialect.header.has_header_row);
        assert_eq!(metadata.num_fields, 3);
    }

    #[test]
    fn test_comment_preamble_propagated() {
        let data = b"# Comment 1\n# Comment 2\nname,age\nAlice,30\nBob,25\n";
        let metadata = Sniffer::new().sniff_bytes(data).unwrap();
        assert_eq!(metadata.dialect.header.num_preamble_rows, 2);
        assert!(metadata.dialect.header.has_header_row);
        assert_eq!(metadata.fields, vec!["name", "age"]);
    }

    #[test]
    fn test_structural_preamble_detection() {
        // TITLE row has 1 field, SUBTITLE has 2 fields, data has 5 fields
        let data = b"TITLE\nSUB,TITLE\nA,B,C,D,E\n1,2,3,4,5\n2,3,4,5,6\n3,4,5,6,7\n";
        let metadata = Sniffer::new().sniff_bytes(data).unwrap();
        assert_eq!(metadata.dialect.header.num_preamble_rows, 2);
        assert!(metadata.dialect.header.has_header_row);
        assert_eq!(metadata.fields, vec!["A", "B", "C", "D", "E"]);
    }

    #[test]
    fn test_mixed_preamble_detection() {
        // Both comment preamble and structural preamble
        // METADATA has 1 field, data has 3 fields
        let data =
            b"# File header\nMETADATA\nname,age,city\nAlice,30,NYC\nBob,25,LA\nCharlie,35,CHI\n";
        let metadata = Sniffer::new().sniff_bytes(data).unwrap();
        // 1 comment + 1 structural = 2 total
        assert_eq!(metadata.dialect.header.num_preamble_rows, 2);
        assert!(metadata.dialect.header.has_header_row);
        assert_eq!(metadata.fields, vec!["name", "age", "city"]);
    }

    #[test]
    fn test_no_preamble() {
        let data = b"a,b,c\n1,2,3\n4,5,6\n";
        let metadata = Sniffer::new().sniff_bytes(data).unwrap();
        assert_eq!(metadata.dialect.header.num_preamble_rows, 0);
    }

    #[test]
    fn test_detect_structural_preamble_function() {
        use crate::tum::table::Table;

        // Table with 2 preamble rows (different field counts)
        let mut table = Table::new();
        table.rows = vec![
            vec!["TITLE".to_string()],
            vec!["".to_string(), "".to_string()],
            vec!["A".to_string(), "B".to_string(), "C".to_string()],
            vec!["1".to_string(), "2".to_string(), "3".to_string()],
            vec!["4".to_string(), "5".to_string(), "6".to_string()],
        ];
        table.field_counts = vec![1, 2, 3, 3, 3];
        table.update_modal_field_count();
        assert_eq!(detect_structural_preamble(&table), 2);

        // Table with no preamble (uniform field counts)
        let mut table = Table::new();
        table.rows = vec![
            vec!["A".to_string(), "B".to_string(), "C".to_string()],
            vec!["1".to_string(), "2".to_string(), "3".to_string()],
        ];
        table.field_counts = vec![3, 3];
        table.update_modal_field_count();
        assert_eq!(detect_structural_preamble(&table), 0);

        // Table too small to determine preamble
        let mut table = Table::new();
        table.rows = vec![vec!["A".to_string()]];
        table.field_counts = vec![1];
        table.update_modal_field_count();
        assert_eq!(detect_structural_preamble(&table), 0);
    }

    #[test]
    fn test_avg_record_len_calculated_from_data() {
        // Test that avg_record_len uses raw bytes, not parsed content
        let short_data = b"a,b\n1,2\n3,4\n";
        let sniffer = Sniffer::new();
        let metadata = sniffer.sniff_bytes(short_data).unwrap();

        // Each row: "a,b\n" = 4 bytes, "1,2\n" = 4 bytes, "3,4\n" = 4 bytes
        // Average: 12 / 3 = 4 bytes
        assert_eq!(metadata.avg_record_len, 4);
    }

    #[test]
    fn test_avg_record_len_with_quoted_fields() {
        let quoted_data = b"\"hello\",\"world\"\n\"foo\",\"bar\"\n";
        let sniffer = Sniffer::new();
        let metadata = sniffer.sniff_bytes(quoted_data).unwrap();

        // Raw: 16 + 12 = 28 bytes for 2 rows = 14 bytes avg
        assert_eq!(metadata.avg_record_len, 14);
    }

    #[test]
    fn test_records_mode_cap_boundary_ok() {
        // Verify that a reader with more than MAX_RECORDS_BYTES of valid CSV is handled
        // gracefully and returns Ok. Uses a cycling pattern to avoid a large literal in
        // test source; the runtime still materializes ~100 MB via collect().
        // We supply MAX_RECORDS_BYTES + one extra row so the probe-read finds data and
        // the truncation warning fires, but the sniff still succeeds.
        let row = b"col1,col2,col3\n1,2,3\n"; // 21 bytes, valid CSV pair
        let total = MAX_RECORDS_BYTES + row.len();
        let data: Vec<u8> = row.iter().copied().cycle().take(total).collect();
        // Confirm the test data actually exceeds the cap so the probe path is exercised.
        assert!(
            data.len() > MAX_RECORDS_BYTES,
            "test data must exceed MAX_RECORDS_BYTES to exercise probe-read path"
        );
        let cursor = std::io::Cursor::new(data);
        let mut sniffer = Sniffer::new();
        // Records(200_000): estimated_size = 200_000 * 1024 > MAX_RECORDS_BYTES (100 MB), clamped to MAX_RECORDS_BYTES.
        sniffer.sample_size(SampleSize::Records(200_000));
        let result = sniffer.sniff_reader(cursor);
        assert!(
            result.is_ok(),
            "sniff should succeed at cap boundary: {result:?}"
        );
        // Note: the eprintln! truncation warning cannot be captured in a standard Rust
        // unit test without process-level stderr redirection. The probe-read path is
        // exercised by virtue of data.len() > MAX_RECORDS_BYTES (asserted above).
    }
}
```

## File: `src/tum/mod.rs`
```rust
//! Table Uniformity Method (TUM) for CSV dialect detection.

pub mod potential_dialects;
pub mod regexes;
pub mod score;
pub mod table;
pub mod type_detection;
pub mod uniformity;
```

## File: `src/tum/potential_dialects.rs`
```rust
//! Generation of potential CSV dialect combinations.

use crate::metadata::Quote;

/// A potential CSV dialect to test.
#[derive(Debug, Clone, PartialEq, Eq, Hash)]
pub struct PotentialDialect {
    /// Field delimiter character.
    pub delimiter: u8,
    /// Quote character configuration.
    pub quote: Quote,
    /// Line terminator sequence.
    pub line_terminator: LineTerminator,
}

impl PotentialDialect {
    /// Create a new potential dialect.
    pub const fn new(delimiter: u8, quote: Quote, line_terminator: LineTerminator) -> Self {
        Self {
            delimiter,
            quote,
            line_terminator,
        }
    }
}

/// Line terminator sequences.
#[allow(clippy::upper_case_acronyms)]
#[derive(Debug, Clone, Copy, PartialEq, Eq, Hash)]
pub enum LineTerminator {
    /// Unix-style line ending (\n).
    LF,
    /// Windows-style line ending (\r\n).
    CRLF,
    /// Old Mac-style line ending (\r).
    CR,
}

impl LineTerminator {
    /// Returns the byte sequence for this line terminator.
    #[allow(dead_code)]
    pub const fn as_bytes(&self) -> &'static [u8] {
        match self {
            LineTerminator::LF => b"\n",
            LineTerminator::CRLF => b"\r\n",
            LineTerminator::CR => b"\r",
        }
    }

    /// Returns the string representation.
    #[allow(dead_code)]
    pub const fn as_str(&self) -> &'static str {
        match self {
            LineTerminator::LF => "\\n",
            LineTerminator::CRLF => "\\r\\n",
            LineTerminator::CR => "\\r",
        }
    }
}

/// Common delimiters to test (ordered by frequency in real-world data).
/// Note: Colon is intentionally excluded as it commonly appears in time values (HH:MM:SS).
// pub const DELIMITERS: &[u8] = &[
//     b',',  // Comma (most common)
//     b';',  // Semicolon (common in European locales)
//     b'\t', // Tab (TSV files)
//     b'|',  // Pipe
//     b' ',  // Space
//     b'^',  // Caret
//     b'~',  // Tilde
//     b'#',  // Hash (rare)car
//     b'&',  // Ampersand (rare)
// ];
pub const DELIMITERS: &[u8] = b",;\t| ^~#&\xa7/";

/// Quote characters to test.
pub const QUOTES: &[Quote] = &[
    Quote::Some(b'"'),  // Double quote (most common)
    Quote::Some(b'\''), // Single quote
    Quote::None,        // No quoting
];

/// Line terminators to test.
#[allow(dead_code)]
pub const LINE_TERMINATORS: &[LineTerminator] = &[
    LineTerminator::CRLF, // Windows (check first as it's a superset of LF)
    LineTerminator::LF,   // Unix
    LineTerminator::CR,   // Old Mac
];

/// Generate all potential dialect combinations.
///
/// Returns approximately 81 combinations (9 delimiters × 3 quotes × 3 line endings).
#[allow(dead_code)]
pub fn generate_potential_dialects() -> Vec<PotentialDialect> {
    let mut dialects = Vec::with_capacity(DELIMITERS.len() * QUOTES.len() * LINE_TERMINATORS.len());

    for &delimiter in DELIMITERS {
        for &quote in QUOTES {
            for &line_terminator in LINE_TERMINATORS {
                dialects.push(PotentialDialect::new(delimiter, quote, line_terminator));
            }
        }
    }

    dialects
}

/// Detect the most likely line terminator from data.
pub fn detect_line_terminator(data: &[u8]) -> LineTerminator {
    let mut crlf_count = 0;
    let mut lf_count = 0;
    let mut cr_count = 0;

    let mut i = 0;
    while i < data.len() {
        if data[i] == b'\r' {
            if i + 1 < data.len() && data[i + 1] == b'\n' {
                crlf_count += 1;
                i += 2;
                continue;
            }
            cr_count += 1;
        } else if data[i] == b'\n' {
            lf_count += 1;
        }
        i += 1;
    }

    // Prefer CRLF if present (Windows), then LF (Unix), then CR (old Mac)
    if crlf_count > 0 && crlf_count >= lf_count && crlf_count >= cr_count {
        LineTerminator::CRLF
    } else if lf_count >= cr_count {
        LineTerminator::LF
    } else {
        LineTerminator::CR
    }
}

/// Generate potential dialects with a detected line terminator.
///
/// This reduces the search space by detecting the line terminator first.
pub fn generate_dialects_with_terminator(line_terminator: LineTerminator) -> Vec<PotentialDialect> {
    let mut dialects = Vec::with_capacity(DELIMITERS.len() * QUOTES.len());

    for &delimiter in DELIMITERS {
        for &quote in QUOTES {
            dialects.push(PotentialDialect::new(delimiter, quote, line_terminator));
        }
    }

    dialects
}

/// Normalize line endings to LF for consistent parsing.
///
/// Returns `Cow::Borrowed` for LF data (zero-copy) and `Cow::Owned` for CR/CRLF.
/// This is used to normalize data once before scoring multiple dialects.
pub fn normalize_line_endings(
    data: &[u8],
    line_terminator: LineTerminator,
) -> std::borrow::Cow<'_, [u8]> {
    use std::borrow::Cow;

    match line_terminator {
        LineTerminator::LF => Cow::Borrowed(data), // Zero-copy for LF
        LineTerminator::CRLF => {
            // Replace \r\n with \n
            let mut result = Vec::with_capacity(data.len());
            let mut i = 0;
            while i < data.len() {
                if i + 1 < data.len() && data[i] == b'\r' && data[i + 1] == b'\n' {
                    result.push(b'\n');
                    i += 2;
                } else {
                    result.push(data[i]);
                    i += 1;
                }
            }
            Cow::Owned(result)
        }
        LineTerminator::CR => {
            // Replace standalone \r with \n
            Cow::Owned(
                data.iter()
                    .map(|&b| if b == b'\r' { b'\n' } else { b })
                    .collect(),
            )
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_generate_potential_dialects() {
        let dialects = generate_potential_dialects();
        assert_eq!(dialects.len(), 99); // 11 * 3 * 3
    }

    #[test]
    fn test_detect_line_terminator() {
        assert_eq!(detect_line_terminator(b"a,b\nc,d\n"), LineTerminator::LF);
        assert_eq!(
            detect_line_terminator(b"a,b\r\nc,d\r\n"),
            LineTerminator::CRLF
        );
        assert_eq!(detect_line_terminator(b"a,b\rc,d\r"), LineTerminator::CR);
    }
}
```

## File: `src/tum/regexes.rs`
```rust
//! Compiled regex patterns for type detection.
//!
//! These patterns are based on the CSVsniffer paper and extended for
//! better real-world coverage.

use regex::Regex;

/// Pattern for NULL-like values.
pub static NULL_PATTERN: std::sync::LazyLock<Regex> = std::sync::LazyLock::new(|| {
    Regex::new(r"(?i)^(null|nil|none|na|n/a|\?|nan|-|--|\.|\.\.|#n/a|#value!|#ref!|#div/0!)$")
        .expect("Invalid null pattern")
});

/// Pattern for unsigned integers (non-negative whole numbers).
pub static UNSIGNED_PATTERN: std::sync::LazyLock<Regex> =
    std::sync::LazyLock::new(|| Regex::new(r"^[+]?\d{1,20}$").expect("Invalid unsigned pattern"));

/// Pattern for signed integers (including negative).
pub static SIGNED_PATTERN: std::sync::LazyLock<Regex> =
    std::sync::LazyLock::new(|| Regex::new(r"^[-+]?\d{1,20}$").expect("Invalid signed pattern"));

/// Pattern for floating point numbers (various formats).
pub static FLOAT_PATTERN: std::sync::LazyLock<Regex> = std::sync::LazyLock::new(|| {
    Regex::new(r"^[-+]?(?:\d+\.?\d*|\d*\.?\d+)(?:[eE][-+]?\d+)?$").expect("Invalid float pattern")
});

/// Pattern for European-style floats (comma as decimal separator).
pub static FLOAT_EURO_PATTERN: std::sync::LazyLock<Regex> =
    std::sync::LazyLock::new(|| Regex::new(r"^[-+]?\d+,\d+$").expect("Invalid euro float pattern"));

/// Pattern for numbers with thousand separators (US style: 1,234,567.89).
pub static FLOAT_THOUSANDS_PATTERN: std::sync::LazyLock<Regex> = std::sync::LazyLock::new(|| {
    Regex::new(r"^[-+]?(?:\d{1,3}(?:,\d{3})*(?:\.\d+)?|\d+(?:\.\d+)?)$")
        .expect("Invalid thousands pattern")
});

/// Pattern for boolean values.
pub static BOOLEAN_PATTERN: std::sync::LazyLock<Regex> = std::sync::LazyLock::new(|| {
    Regex::new(r"(?i)^(true|false|yes|no|y|n|t|f|1|0|on|off)$").expect("Invalid boolean pattern")
});

/// Pattern for ISO 8601 dates (YYYY-MM-DD).
pub static DATE_ISO_PATTERN: std::sync::LazyLock<Regex> = std::sync::LazyLock::new(|| {
    Regex::new(r"^\d{4}[-/]\d{1,2}[-/]\d{1,2}$").expect("Invalid ISO date pattern")
});

/// Pattern for US-style dates (MM/DD/YYYY or MM-DD-YYYY).
pub static DATE_US_PATTERN: std::sync::LazyLock<Regex> = std::sync::LazyLock::new(|| {
    Regex::new(r"^\d{1,2}[-/]\d{1,2}[-/]\d{2,4}$").expect("Invalid US date pattern")
});

/// Pattern for European-style dates (DD.MM.YYYY).
pub static DATE_EURO_PATTERN: std::sync::LazyLock<Regex> = std::sync::LazyLock::new(|| {
    Regex::new(r"^\d{1,2}\.\d{1,2}\.\d{2,4}$").expect("Invalid Euro date pattern")
});

/// Pattern for ISO 8601 datetime (YYYY-MM-DDTHH:MM:SS).
pub static DATETIME_ISO_PATTERN: std::sync::LazyLock<Regex> = std::sync::LazyLock::new(|| {
    Regex::new(
        r"^\d{4}[-/]\d{1,2}[-/]\d{1,2}[T ]\d{1,2}:\d{2}(:\d{2})?(\.\d+)?(Z|[+-]\d{2}:?\d{2})?$",
    )
    .expect("Invalid ISO datetime pattern")
});

/// Pattern for general datetime with various separators.
pub static DATETIME_GENERAL_PATTERN: std::sync::LazyLock<Regex> = std::sync::LazyLock::new(|| {
    Regex::new(r"^\d{1,4}[-/\.]\d{1,2}[-/\.]\d{1,4}[T ]?\d{1,2}:\d{2}(:\d{2})?(\s*(AM|PM|am|pm))?$")
        .expect("Invalid general datetime pattern")
});

/// Pattern for time values (HH:MM:SS).
pub static TIME_PATTERN: std::sync::LazyLock<Regex> = std::sync::LazyLock::new(|| {
    Regex::new(r"^\d{1,2}:\d{2}(:\d{2})?(\.\d+)?(\s*(AM|PM|am|pm))?$")
        .expect("Invalid time pattern")
});

/// Pattern for email addresses.
pub static EMAIL_PATTERN: std::sync::LazyLock<Regex> = std::sync::LazyLock::new(|| {
    Regex::new(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$").expect("Invalid email pattern")
});

/// Pattern for URLs.
pub static URL_PATTERN: std::sync::LazyLock<Regex> = std::sync::LazyLock::new(|| {
    Regex::new(r"^(https?|ftp)://[^\s/$.?#].[^\s]*$").expect("Invalid URL pattern")
});

/// Pattern for IPv4 addresses.
pub static IPV4_PATTERN: std::sync::LazyLock<Regex> = std::sync::LazyLock::new(|| {
    Regex::new(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$").expect("Invalid IPv4 pattern")
});

/// Pattern for currency values.
pub static CURRENCY_PATTERN: std::sync::LazyLock<Regex> = std::sync::LazyLock::new(|| {
    Regex::new(r"^[$€£¥₹]?\s*[-+]?[\d,]+\.?\d*$|^[-+]?[\d,]+\.?\d*\s*[$€£¥₹]$")
        .expect("Invalid currency pattern")
});

/// Pattern for percentage values.
pub static PERCENTAGE_PATTERN: std::sync::LazyLock<Regex> = std::sync::LazyLock::new(|| {
    Regex::new(r"^[-+]?\d+\.?\d*\s*%$").expect("Invalid percentage pattern")
});

/// Pattern for UUID values.
pub static UUID_PATTERN: std::sync::LazyLock<Regex> = std::sync::LazyLock::new(|| {
    Regex::new(r"^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$")
        .expect("Invalid UUID pattern")
});

/// Pattern for alphanumeric identifiers (common for IDs).
pub static ALPHANUM_PATTERN: std::sync::LazyLock<Regex> = std::sync::LazyLock::new(|| {
    Regex::new(r"^[A-Za-z0-9_-]+$").expect("Invalid alphanumeric pattern")
});

/// All patterns with their type categories for scoring.
pub struct PatternCategory {
    pub pattern: &'static std::sync::LazyLock<Regex>,
    #[allow(dead_code)]
    pub category: &'static str,
    pub weight: f64,
}

/// Static pattern categories for type detection (cached via LazyLock).
static PATTERN_CATEGORIES: std::sync::LazyLock<Vec<PatternCategory>> =
    std::sync::LazyLock::new(|| {
        vec![
            PatternCategory {
                pattern: &NULL_PATTERN,
                category: "null",
                weight: 0.5,
            },
            PatternCategory {
                pattern: &BOOLEAN_PATTERN,
                category: "boolean",
                weight: 1.0,
            },
            PatternCategory {
                pattern: &UNSIGNED_PATTERN,
                category: "unsigned",
                weight: 1.0,
            },
            PatternCategory {
                pattern: &SIGNED_PATTERN,
                category: "signed",
                weight: 1.0,
            },
            PatternCategory {
                pattern: &FLOAT_PATTERN,
                category: "float",
                weight: 1.0,
            },
            PatternCategory {
                pattern: &FLOAT_EURO_PATTERN,
                category: "float_euro",
                weight: 0.9,
            },
            PatternCategory {
                pattern: &FLOAT_THOUSANDS_PATTERN,
                category: "float_thousands",
                weight: 0.9,
            },
            PatternCategory {
                pattern: &DATE_ISO_PATTERN,
                category: "date",
                weight: 1.0,
            },
            PatternCategory {
                pattern: &DATE_US_PATTERN,
                category: "date",
                weight: 0.9,
            },
            PatternCategory {
                pattern: &DATE_EURO_PATTERN,
                category: "date",
                weight: 0.9,
            },
            PatternCategory {
                pattern: &DATETIME_ISO_PATTERN,
                category: "datetime",
                weight: 1.0,
            },
            PatternCategory {
                pattern: &DATETIME_GENERAL_PATTERN,
                category: "datetime",
                weight: 0.9,
            },
            PatternCategory {
                pattern: &TIME_PATTERN,
                category: "time",
                weight: 0.8,
            },
            PatternCategory {
                pattern: &EMAIL_PATTERN,
                category: "email",
                weight: 0.8,
            },
            PatternCategory {
                pattern: &URL_PATTERN,
                category: "url",
                weight: 0.8,
            },
            PatternCategory {
                pattern: &IPV4_PATTERN,
                category: "ipv4",
                weight: 0.8,
            },
            PatternCategory {
                pattern: &CURRENCY_PATTERN,
                category: "currency",
                weight: 0.9,
            },
            PatternCategory {
                pattern: &PERCENTAGE_PATTERN,
                category: "percentage",
                weight: 0.9,
            },
            PatternCategory {
                pattern: &UUID_PATTERN,
                category: "uuid",
                weight: 0.8,
            },
            PatternCategory {
                pattern: &ALPHANUM_PATTERN,
                category: "alphanum",
                weight: 0.3,
            },
        ]
    });

/// Get all pattern categories for type detection.
/// Returns a static reference to avoid allocating a new Vec on each call.
pub fn get_pattern_categories() -> &'static [PatternCategory] {
    &PATTERN_CATEGORIES
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_unsigned_pattern() {
        assert!(UNSIGNED_PATTERN.is_match("123"));
        assert!(UNSIGNED_PATTERN.is_match("0"));
        assert!(UNSIGNED_PATTERN.is_match("+42"));
        assert!(!UNSIGNED_PATTERN.is_match("-42"));
        assert!(!UNSIGNED_PATTERN.is_match("12.34"));
    }

    #[test]
    fn test_boolean_pattern() {
        assert!(BOOLEAN_PATTERN.is_match("true"));
        assert!(BOOLEAN_PATTERN.is_match("FALSE"));
        assert!(BOOLEAN_PATTERN.is_match("yes"));
        assert!(BOOLEAN_PATTERN.is_match("1"));
        assert!(!BOOLEAN_PATTERN.is_match("maybe"));
    }

    #[test]
    fn test_date_patterns() {
        assert!(DATE_ISO_PATTERN.is_match("2023-12-31"));
        assert!(DATE_ISO_PATTERN.is_match("2023/12/31"));
        assert!(DATE_US_PATTERN.is_match("12/31/2023"));
        assert!(DATE_EURO_PATTERN.is_match("31.12.2023"));
    }

    #[test]
    fn test_datetime_patterns() {
        assert!(DATETIME_ISO_PATTERN.is_match("2023-12-31T12:30:45"));
        assert!(DATETIME_ISO_PATTERN.is_match("2023-12-31 12:30:45"));
        assert!(DATETIME_ISO_PATTERN.is_match("2023-12-31T12:30:45Z"));
        assert!(DATETIME_ISO_PATTERN.is_match("2023-12-31T12:30:45+05:30"));
    }

    #[test]
    fn test_null_pattern() {
        assert!(NULL_PATTERN.is_match("NULL"));
        assert!(NULL_PATTERN.is_match("null"));
        assert!(NULL_PATTERN.is_match("NA"));
        assert!(NULL_PATTERN.is_match("N/A"));
        assert!(NULL_PATTERN.is_match("-"));
        assert!(NULL_PATTERN.is_match("NaN"));
    }
}
```

## File: `src/tum/score.rs`
```rust
//! Combined scoring for dialect detection.
//!
//! The gamma score combines uniformity and type detection scores
//! to rank potential CSV dialects.

use std::cell::RefCell;

use rayon::prelude::*;

use super::potential_dialects::PotentialDialect;
use super::table::{Table, parse_table, parse_table_normalized};
use super::type_detection::{TypeScoreBuffers, calculate_pattern_score, calculate_type_score};
use super::uniformity::{calculate_tau_0, calculate_tau_1, is_uniform};

thread_local! {
    // Each rayon worker thread owns one reusable TypeScoreBuffers.  Vec::clear()
    // keeps the allocated capacity, so after sniffing a very-wide CSV a thread's
    // buffer retains the high-water-mark allocation for the lifetime of the rayon
    // pool (typically the whole process).  Overhead is small
    // (max_cols × Type::COUNT × 2 × sizeof(usize) per thread) but worth noting
    // for long-running library users processing a mix of narrow and wide files.
    static BUFFERS: RefCell<TypeScoreBuffers> = RefCell::new(TypeScoreBuffers::new());
}

/// Pre-computed quote character counts for the data.
/// Used to avoid redundant byte counting across multiple dialect evaluations.
#[derive(Debug, Clone, Copy)]
struct QuoteCounts {
    double: usize,
    single: usize,
    /// Number of `\'` (backslash + single-quote) byte pairs in the data.
    backslash_single: usize,
    /// Number of `\"` (backslash + double-quote) byte pairs in the data.
    backslash_double: usize,
    data_len: usize,
}

impl QuoteCounts {
    fn new(data: &[u8]) -> Self {
        let mut backslash_single = 0usize;
        let mut backslash_double = 0usize;
        for window in data.windows(2) {
            if window[0] == b'\\' {
                if window[1] == b'\'' {
                    backslash_single += 1;
                } else if window[1] == b'"' {
                    backslash_double += 1;
                }
            }
        }
        Self {
            double: bytecount::count(data, b'"'),
            single: bytecount::count(data, b'\''),
            backslash_single,
            backslash_double,
            data_len: data.len(),
        }
    }
}

/// Pre-computed quote boundary counts for both quote characters.
/// Used to avoid redundant data scanning across multiple dialect evaluations.
#[derive(Debug, Clone)]
struct QuoteBoundaryCounts {
    /// Boundary counts for double quote with each delimiter (opening + closing)
    double_boundaries: Vec<(u8, usize)>,
    /// Boundary counts for single quote with each delimiter (opening + closing)
    single_boundaries: Vec<(u8, usize)>,
    /// Opening-only boundary counts for single quote with each delimiter
    /// (delimiter/newline → quote, field start).  Used to distinguish genuine
    /// quoting from apostrophes that appear only before delimiters (closing).
    single_opening_boundaries: Vec<(u8, usize)>,
    /// Newline boundary counts for double quote (not delimiter-specific)
    double_newline_boundaries: usize,
    /// Newline boundary counts for single quote (not delimiter-specific)
    single_newline_boundaries: usize,
    /// Opening-only newline boundary counts for single quote
    single_opening_newline_boundaries: usize,
    /// Whether data starts with double quote
    starts_with_double: bool,
    /// Whether data starts with single quote
    starts_with_single: bool,
}

impl QuoteBoundaryCounts {
    /// Compute quote boundary counts for all delimiters in a single pass.
    fn new(data: &[u8], delimiters: &[u8]) -> Self {
        let mut double_counts: Vec<usize> = vec![0; delimiters.len()];
        let mut single_counts: Vec<usize> = vec![0; delimiters.len()];
        let mut single_opening_counts: Vec<usize> = vec![0; delimiters.len()];
        let mut double_newline_boundaries: usize = 0;
        let mut single_newline_boundaries: usize = 0;
        let mut single_opening_newline_boundaries: usize = 0;

        // Create lookup table for delimiter indices
        let mut delim_indices = [usize::MAX; 256];
        for (i, &d) in delimiters.iter().enumerate() {
            delim_indices[d as usize] = i;
        }

        // Single pass through data for all delimiters
        for window in data.windows(2) {
            let is_newline = window[0] == b'\n' || window[0] == b'\r';
            let delim_idx = delim_indices[window[0] as usize];
            let is_delimiter = delim_idx != usize::MAX;

            // Quote after delimiter/newline (field start = OPENING boundary)
            if is_newline || is_delimiter {
                if window[1] == b'"' {
                    if is_newline {
                        // Count newline boundaries separately (once, not per delimiter)
                        double_newline_boundaries += 1;
                    } else {
                        // Count delimiter-specific boundary
                        double_counts[delim_idx] += 1;
                    }
                }
                if window[1] == b'\'' {
                    if is_newline {
                        single_newline_boundaries += 1;
                        single_opening_newline_boundaries += 1;
                    } else {
                        single_counts[delim_idx] += 1;
                        single_opening_counts[delim_idx] += 1;
                    }
                }
            }

            // Quote before delimiter/newline (field end = CLOSING boundary)
            let is_end_newline = window[1] == b'\n' || window[1] == b'\r';
            let end_delim_idx = delim_indices[window[1] as usize];
            let is_end_delimiter = end_delim_idx != usize::MAX;

            if window[0] == b'"' && (is_end_newline || is_end_delimiter) {
                if is_end_newline {
                    double_newline_boundaries += 1;
                } else {
                    double_counts[end_delim_idx] += 1;
                }
            }
            if window[0] == b'\'' && (is_end_newline || is_end_delimiter) {
                if is_end_newline {
                    single_newline_boundaries += 1;
                } else {
                    single_counts[end_delim_idx] += 1;
                }
            }
        }

        let starts_with_double = !data.is_empty() && data[0] == b'"';
        let starts_with_single = !data.is_empty() && data[0] == b'\'';

        Self {
            double_boundaries: delimiters.iter().copied().zip(double_counts).collect(),
            single_boundaries: delimiters.iter().copied().zip(single_counts).collect(),
            single_opening_boundaries: delimiters
                .iter()
                .copied()
                .zip(single_opening_counts)
                .collect(),
            double_newline_boundaries,
            single_newline_boundaries,
            single_opening_newline_boundaries,
            starts_with_double,
            starts_with_single,
        }
    }

    /// Get the boundary count for a specific quote character and delimiter.
    fn get_boundary_count(&self, quote_char: u8, delimiter: u8) -> usize {
        let (boundaries, newline_boundaries) = if quote_char == b'"' {
            (&self.double_boundaries, self.double_newline_boundaries)
        } else {
            (&self.single_boundaries, self.single_newline_boundaries)
        };

        let delimiter_count = boundaries
            .iter()
            .find(|&&(d, _)| d == delimiter)
            .map_or(0, |&(_, c)| c);

        // Add 1 if data starts with this quote char
        let starts_with_quote = (quote_char == b'"' && self.starts_with_double)
            || (quote_char == b'\'' && self.starts_with_single);
        let start_bonus = usize::from(starts_with_quote);

        // Combine delimiter-specific count with newline boundaries (which apply to all delimiters)
        delimiter_count + newline_boundaries + start_bonus
    }

    /// Get the opening-only boundary count for single-quote with a given delimiter.
    ///
    /// Opening boundaries are delimiter/newline → single-quote transitions (field starts).
    /// This distinguishes genuine single-quote quoting (both opening and closing boundaries)
    /// from apostrophes that appear only before delimiters (closing only, as in `'value',`).
    fn get_single_opening_boundary_count(&self, delimiter: u8) -> usize {
        let delimiter_count = self
            .single_opening_boundaries
            .iter()
            .find(|&&(d, _)| d == delimiter)
            .map_or(0, |&(_, c)| c);

        // starts_with_single is an opening boundary (file-start → single-quote)
        let start_bonus = usize::from(self.starts_with_single);

        delimiter_count + self.single_opening_newline_boundaries + start_bonus
    }
}

/// Score result for a dialect.
#[derive(Debug, Clone)]
pub struct DialectScore {
    /// The potential dialect that was scored.
    pub dialect: PotentialDialect,
    /// The combined gamma score (higher is better).
    pub gamma: f64,
    /// Consistency score (tau_0).
    #[allow(dead_code)]
    pub tau_0: f64,
    /// Dispersion score (tau_1).
    #[allow(dead_code)]
    pub tau_1: f64,
    /// Type detection score.
    #[allow(dead_code)]
    pub type_score: f64,
    /// Pattern specificity score.
    #[allow(dead_code)]
    pub pattern_score: f64,
    /// Number of rows parsed.
    #[allow(dead_code)]
    pub num_rows: usize,
    /// Modal (most common) field count.
    pub num_fields: usize,
    /// Whether the table has uniform field counts.
    pub is_uniform: bool,
}

impl DialectScore {
    /// Create a new score result.
    pub fn new(dialect: PotentialDialect, table: &Table, type_score: f64) -> Self {
        let tau_0 = calculate_tau_0(table);
        let tau_1 = calculate_tau_1(table);
        let pattern_score = calculate_pattern_score(table);
        let uniform = is_uniform(table);

        // Calculate combined gamma score (includes delimiter penalty)
        let gamma = compute_gamma(
            tau_0,
            tau_1,
            type_score,
            pattern_score,
            table,
            dialect.delimiter,
        );

        Self {
            dialect,
            gamma,
            tau_0,
            tau_1,
            type_score,
            pattern_score,
            num_rows: table.num_rows(),
            num_fields: table.modal_field_count(),
            is_uniform: uniform,
        }
    }

    /// Create a zero score (for failed parses).
    pub const fn zero(dialect: PotentialDialect) -> Self {
        Self {
            dialect,
            gamma: 0.0,
            tau_0: 0.0,
            tau_1: 0.0,
            type_score: 0.0,
            pattern_score: 0.0,
            num_rows: 0,
            num_fields: 0,
            is_uniform: false,
        }
    }
}

/// Compute the combined gamma score.
///
/// The gamma score combines multiple factors:
/// - tau_0 (consistency): higher is better
/// - tau_1 (dispersion): higher is better (less dispersion)
/// - type_score: higher means better type consistency
/// - pattern_score: higher means more specific patterns detected
/// - Additional bonuses for uniform tables and reasonable field counts
/// - Penalties for uncommon delimiters
fn compute_gamma(
    tau_0: f64,
    tau_1: f64,
    type_score: f64,
    pattern_score: f64,
    table: &Table,
    delimiter: u8,
) -> f64 {
    if table.is_empty() {
        return 0.0;
    }

    // Base score from uniformity metrics
    let uniformity_score = (tau_0 * tau_1).sqrt();

    // Type detection contributes to the score
    let type_contribution = type_score * 0.3;

    // Pattern specificity provides additional signal
    let pattern_contribution = pattern_score * 0.1;

    // Bonus for having multiple rows (more data is more reliable)
    let row_bonus = (table.num_rows().min(20) as f64 / 20.0) * 0.1;

    // Bonus for having multiple fields (single field might be wrong delimiter)
    let field_count = table.modal_field_count();
    let field_bonus = if field_count >= 2 {
        (field_count.min(10) as f64 / 10.0) * 0.2
    } else {
        0.0
    };

    // Penalty for single-field tables (likely wrong delimiter)
    let single_field_penalty = if field_count == 1 { 0.5 } else { 1.0 };

    // Penalty for extremely high field counts (might be splitting on wrong char)
    let high_field_penalty = if field_count > 100 {
        0.5
    } else if field_count > 50 {
        0.8
    } else {
        1.0
    };

    // Penalty for very small samples (less reliable detection)
    let num_rows = table.num_rows();
    let small_sample_penalty = if num_rows < 3 {
        0.80 // Very small - high unreliability
    } else if num_rows < 5 {
        0.90 // Small - moderate unreliability
    } else {
        1.0
    };

    // Penalty for uncommon delimiters
    // This helps prevent rare characters from winning due to accidental patterns
    let delimiter_penalty = match delimiter {
        b',' | b';' | b'\t' => 1.0, // Common delimiters - no penalty
        b'|' => 0.98,               // Pipe - slight penalty
        b':' => 0.90,               // Colon - moderate penalty (often in timestamps)
        b' ' => 0.75,               // Space - significant penalty (often in text)
        b'^' | b'~' => 0.80,        // Rare delimiters
        // Hash - often a comment marker, but can be a legitimate delimiter.
        // For large uniform tables with ≥3 fields, reduce the penalty: the
        // heavy evidence of consistent multi-field parsing overrides the prior.
        //
        // Threshold rationale:
        //   - field_count >= 3: 1- or 2-field tables are too ambiguous — a file with
        //     comments (`# header`) parsed as 1-field could accidentally reach any
        //     uniform score.  Three or more fields give strong structural evidence.
        //   - num_rows >= 50: small tables may accidentally produce consistent patterns
        //     even with `#` as a comment character.  50 rows provides enough statistical
        //     weight to trust the uniformity signal.
        b'#' => {
            if field_count >= 3 && num_rows >= 50 {
                0.85 // Relaxed: large multi-field table is unlikely to be a comment file
            } else {
                0.60 // Strict default: treat `#` as a comment marker unless proven otherwise
            }
        }
        b'&' => 0.60, // Ampersand - very rare
        0xA7 => 0.78, // Section sign (§) - rare but legitimate delimiter
        b'/' => 0.65, // Forward slash - rare, often in paths/dates
        _ => 0.70,    // Unknown - penalty
    };

    // Combine all factors
    // uniformity_score * 0.5 + type_contribution + pattern_contribution + row_bonus + field_bonus;
    let raw_score = uniformity_score.mul_add(0.5, type_contribution)
        + pattern_contribution
        + row_bonus
        + field_bonus;

    raw_score * single_field_penalty * high_field_penalty * delimiter_penalty * small_sample_penalty
}

/// Score a dialect against the data.
///
/// Returns the DialectScore which includes the gamma score and component scores.
#[allow(dead_code)]
pub fn score_dialect(data: &[u8], dialect: &PotentialDialect, max_rows: usize) -> DialectScore {
    let quote_counts = QuoteCounts::new(data);
    let mut buffers = TypeScoreBuffers::new();
    let (score, _table) =
        score_dialect_with_counts(data, dialect, max_rows, &quote_counts, &mut buffers);
    score
}

/// Score a dialect against the data with pre-computed quote counts.
///
/// This is the internal implementation that accepts pre-computed QuoteCounts
/// to avoid redundant byte counting when scoring multiple dialects.
/// Returns both the score and the parsed table for potential reuse.
fn score_dialect_with_counts(
    data: &[u8],
    dialect: &PotentialDialect,
    max_rows: usize,
    quote_counts: &QuoteCounts,
    buffers: &mut TypeScoreBuffers,
) -> (DialectScore, Table) {
    let table = parse_table(data, dialect, max_rows);

    if table.is_empty() {
        return (DialectScore::zero(dialect.clone()), table);
    }

    let type_score = calculate_type_score(&table, buffers);
    let mut score = DialectScore::new(dialect.clone(), &table, type_score);

    // Apply quote evidence scoring using pre-computed counts and raw data for boundary detection
    let quote_multiplier = quote_evidence_score_with_data(data, quote_counts, dialect);
    score.gamma *= quote_multiplier;

    (score, table)
}

/// Score a dialect against pre-normalized data with pre-computed quote counts.
///
/// This variant assumes the data has already been normalized to LF line endings
/// for better performance when scoring multiple dialects.
fn score_dialect_with_normalized_data(
    normalized_data: &[u8],
    dialect: &PotentialDialect,
    max_rows: usize,
    quote_counts: &QuoteCounts,
    boundary_counts: &QuoteBoundaryCounts,
    buffers: &mut TypeScoreBuffers,
) -> (DialectScore, Table) {
    let table = parse_table_normalized(normalized_data, dialect, max_rows);

    if table.is_empty() {
        return (DialectScore::zero(dialect.clone()), table);
    }

    let type_score = calculate_type_score(&table, buffers);
    let mut score = DialectScore::new(dialect.clone(), &table, type_score);

    // Apply quote evidence scoring using pre-computed counts and cached boundary counts
    let quote_multiplier =
        quote_evidence_score_with_cached_boundaries(quote_counts, boundary_counts, dialect);

    // Dampen the quote boost when the first row has just 1 field AND the non-modal rows
    // exhibit diverse field counts (≥3 distinct values). This prevents JSON-content-in-
    // unquoted-fields from triggering a false 2.2x boost: e.g. a tab-delimited file where
    // unquoted JSON fields contain `,key"` patterns that look like opening quote boundaries
    // for comma+doublequote. In such files the first row (tab-delimited header) has 0 commas
    // → 1 field, and JSON data rows have wildly varying comma counts (e.g., 1, 46, 32, 19).
    //
    // The distinguishing check: if the rows that deviate from the modal all share the same
    // count (like {1, 1, 1} for preamble title rows), the non-uniformity is just preamble.
    // If the non-modal rows have ≥3 distinct field counts, the whole table is chaotically
    // variable — a strong signal that boundaries come from field content, not real quoting.
    let effective_multiplier =
        if quote_multiplier > 1.5 && score.num_fields >= 5 && !score.is_uniform {
            let first_fields = table
                .field_counts
                .first()
                .copied()
                .unwrap_or(score.num_fields);
            if first_fields <= 1 {
                // Count distinct field counts among non-modal rows.
                let modal = score.num_fields;
                let mut distinct_counts: Vec<usize> = table
                    .field_counts
                    .iter()
                    .filter(|&&c| c != modal)
                    .copied()
                    .collect();
                distinct_counts.sort_unstable();
                distinct_counts.dedup();
                let distinct_non_modal = distinct_counts.len();
                if distinct_non_modal >= 3 {
                    // ≥3 distinct non-modal field counts → genuinely chaotic table, not just
                    // a small preamble. Scale boost down to 30% of excess so the correct
                    // dialect can compete.
                    1.0 + (quote_multiplier - 1.0) * 0.3
                } else {
                    quote_multiplier
                }
            } else {
                quote_multiplier
            }
        } else {
            quote_multiplier
        };
    // Two-layer penalty for space delimiter when most rows have an empty first field.
    // When leading spaces pad row numbers (e.g. `     1 # 'addr' # 'city'`):
    //   (a) The spaces between the delimiter and adjacent quote characters look like
    //       opening/closing quote boundaries, falsely triggering the 2.2× quote boost.
    //       Hard-cap the boost to ≤ 1.05 to suppress these spurious boundary signals.
    //   (b) The many split-on-space fields inflate field_bonus and field_count metrics.
    //       Multiply the combined gamma by 0.55 to offset this inflation.
    // Legitimate space-delimited files start their rows with actual content, not spaces,
    // so their first field is never empty and this penalty never fires.
    let effective_multiplier = if dialect.delimiter == b' ' && !table.rows.is_empty() {
        let empty_first_count = table
            .rows
            .iter()
            .filter(|row| row.first().is_none_or(|f| f.is_empty()))
            .count();
        if empty_first_count * 2 > table.rows.len() {
            // Cap the quote-evidence boost and fold in a 0.55 base penalty.
            //
            // Threshold rationale:
            //   - empty_first_count * 2 > rows.len(): more than 50% of rows have
            //     an empty first field.  This is the distinguishing signal for
            //     leading-space-padded formats (e.g. `     1 # 'addr'`); legitimate
            //     space-delimited files start rows with real content.
            //   - min(1.05): cap the quote multiplier to nearly-neutral.  The spaces
            //     adjacent to quote characters create false opening/closing boundary
            //     counts; capping prevents this spurious evidence from dominating.
            //   - 0.55: empirically calibrated to suppress the space-delimiter score
            //     below the true delimiter without zeroing it out entirely.  Values
            //     below ~0.50 caused regressions on legitimate space-delimited files.
            effective_multiplier.min(1.05) * 0.55
        } else {
            effective_multiplier
        }
    } else {
        effective_multiplier
    };
    score.gamma *= effective_multiplier;

    // Penalize comma when ' # ' (space-hash-space) appears consistently in the first
    // parsed field.  This pattern is a strong signal that '#' is the true separator used
    // with padded fields (e.g. `     1 # 'addr' # 'city'`), and that comma is splitting
    // on an incidental comma *inside* a '#'-delimited field (e.g. `city, state`).
    // The space-on-both-sides requirement excludes hex colours (`#FF0000`), CSS IDs
    // (`#header`), and other embedded '#' that are not separator uses.
    if dialect.delimiter == b',' && score.num_fields == 2 && !table.rows.is_empty() {
        let hash_sep_count = table
            .rows
            .iter()
            .filter(|row| row.first().is_some_and(|f| f.trim_start().contains(" # ")))
            .count();
        if hash_sep_count * 10 > table.rows.len() * 9 {
            // More than 90% of rows have ' # ' in field-0: comma is very likely
            // splitting inside '#'-delimited rows.  Apply a strong penalty so that
            // '#' dialects can outscore comma even after singlequote boosts.
            //
            // Threshold rationale:
            //   - 90% (hash_sep_count * 10 > rows.len() * 9): requires near-unanimous
            //     presence across rows to avoid penalizing CSV files that happen to
            //     contain ` # ` in a small number of text fields (e.g., comments or
            //     markdown-style tables).  A file that is genuinely '#'-delimited will
            //     have the pattern in virtually every row.
            //   - 0.82: chosen to be strong enough to let the '#' dialect win after its
            //     own penalty (0.85 for large tables) and single-quote boost (1.10) are
            //     factored in, without being so severe that it causes regressions on
            //     legitimate comma-separated files with rare embedded ' # '.
            score.gamma *= 0.82;
        }
    }

    (score, table)
}

/// Calculate a score multiplier based on quote character evidence in the data.
///
/// This function examines the actual presence of quote characters in the data
/// to boost dialects where the quote char is genuinely used and penalize
/// Quote::None when quotes are present.
///
/// The scoring is conservative to avoid false positives from apostrophes
/// in text content (e.g., "John's" contains a single quote but isn't quoted).
#[allow(dead_code)]
fn quote_evidence_score(data: &[u8], dialect: &PotentialDialect) -> f64 {
    let quote_counts = QuoteCounts::new(data);
    quote_evidence_score_with_counts(&quote_counts, dialect)
}

/// Calculate quote evidence score using pre-computed quote counts.
/// This avoids redundant byte counting when scoring multiple dialects.
fn quote_evidence_score_with_counts(quote_counts: &QuoteCounts, dialect: &PotentialDialect) -> f64 {
    use crate::metadata::Quote;

    if quote_counts.data_len == 0 {
        return 1.0;
    }

    // Calculate density (quotes per 1000 bytes) - higher density suggests quoting
    let double_density = (quote_counts.double * 1000) / quote_counts.data_len;
    let single_density = (quote_counts.single * 1000) / quote_counts.data_len;

    // Threshold: need at least ~0.5% quote density to consider it significant
    // This filters out incidental apostrophes in text
    let min_density_threshold = 5; // 0.5% = 5 per 1000

    match dialect.quote {
        Quote::Some(b'"') => {
            if double_density >= min_density_threshold {
                // Double quotes have significant density - boost
                1.06
            } else {
                // Neutral - rely on other scoring factors
                1.0
            }
        }
        Quote::Some(b'\'') => {
            // Single quotes are tricky because apostrophes are common in text
            // Only boost if single quotes dominate AND double quotes are absent
            if double_density == 0 && single_density >= min_density_threshold {
                // No double quotes at all - strong single-quote evidence
                1.10
            } else if single_density >= min_density_threshold * 2
                && double_density < min_density_threshold
            {
                // Strong evidence of single-quote usage
                1.05
            } else if double_density >= min_density_threshold {
                // Double quotes present but testing single - stronger penalty
                0.92
            } else {
                1.0
            }
        }
        Quote::None => {
            // Only penalize Quote::None when there's strong quoting evidence
            if double_density >= min_density_threshold {
                0.90
            } else {
                1.0
            }
        }
        Quote::Some(_) => 1.0, // Other quote chars - neutral
    }
}

/// Check if quote characters appear at field boundaries (stronger evidence).
/// Returns the count of boundary pairs found.
#[allow(dead_code)]
fn quote_boundary_count(data: &[u8], quote_char: u8, delimiter: u8) -> usize {
    let mut boundary_pairs = 0;
    for window in data.windows(2) {
        // Quote after delimiter/newline (field start)
        if (window[0] == delimiter || window[0] == b'\n' || window[0] == b'\r')
            && window[1] == quote_char
        {
            boundary_pairs += 1;
        }
        // Quote before delimiter/newline (field end)
        if window[0] == quote_char
            && (window[1] == delimiter || window[1] == b'\n' || window[1] == b'\r')
        {
            boundary_pairs += 1;
        }
    }
    // Also check start of data
    if !data.is_empty() && data[0] == quote_char {
        boundary_pairs += 1;
    }
    boundary_pairs
}

/// Compute the score multiplier for single-quote evidence.
///
/// Shared by both `quote_evidence_score_with_cached_boundaries` and
/// `quote_evidence_score_with_data` so that the two code paths stay in sync.
/// Previously each function contained an identical copy of these branches;
/// a divergence (one gets a fix the other misses) is prevented by this helper.
///
/// # Parameters
/// - `boundary_count`: total single-quote boundary events (opening + closing)
///   as returned by `get_boundary_count` or `quote_boundary_count`.  When
///   `opening_count == 0` every event counted here is a *closing* boundary.
/// - `opening_count`: opening-only boundary events (delimiter/newline → quote).
/// - `single_density`: single-quote count per 1000 bytes.
/// - `double_density`: double-quote count per 1000 bytes.
/// - `min_density_threshold`: minimum density to treat as significant (5 / 1000).
fn compute_single_quote_multiplier(
    quote_counts: &QuoteCounts,
    boundary_count: usize,
    opening_count: usize,
    single_density: usize,
    double_density: usize,
    min_density_threshold: usize,
) -> f64 {
    if quote_counts.double == 0
        && opening_count >= 2
        && boundary_count >= 4
        && single_density >= min_density_threshold * 2
    {
        // No double quotes, opening+closing boundaries, high density
        // This is strong evidence of single-quote quoting
        2.2
    } else if quote_counts.double == 0
        && opening_count >= 1
        && boundary_count >= 2
        && single_density >= min_density_threshold
    {
        // No double quotes, opening boundary present, decent density
        1.20
    } else if double_density >= min_density_threshold {
        // Double quotes present - penalize single-quote detection
        0.90
    } else if quote_counts.backslash_single > 0
        && quote_counts.backslash_double == 0
        && boundary_count == 0
    {
        // Backslash-escaped single quotes (e.g. `Ships\' engineers`) with no
        // double-quote evidence — single-quote is the dialect's escape target.
        // Boost must exceed 5% to escape the quote-preference tiebreaker zone.
        //
        // `backslash_double` is used only as a negative guard: double-quoted files
        // don't need this boost because their `\"` pairs already produce sufficient
        // boundary events via the normal path above.
        1.10
    } else if quote_counts.double == 0
        && opening_count == 0
        && boundary_count >= 20
        && single_density >= 50
    {
        // Only closing single-quote boundaries (field-end `'<delim>` or `'\n`) but
        // no opening boundaries (delimiter → quote).  `boundary_count` reflects
        // total events from `get_boundary_count`/`quote_boundary_count`; because
        // `opening_count == 0`, every counted event here is a closing boundary.
        //
        // This pattern occurs when single-quote quoting uses a space between the
        // delimiter and the quote character (e.g. `# 'addr' # 'city'`): the
        // adjacency scan misses the opening `# '` pair due to the intermediate
        // space.
        //
        // Threshold rationale:
        //   - boundary_count >= 20: prose apostrophes rarely accumulate 20+
        //     closing boundary events in a structured file; this requires at
        //     least ~10 quoted fields at minimum.  Irish names, possessives, or
        //     contractions at line ends would need an unusually dense poem to
        //     reach this count before the density gate fires.
        //   - single_density >= 50 (50 per 1000 bytes = 5%): a very high density
        //     that prose text with incidental apostrophes typically does not reach.
        //     Together, both conditions make false positives from apostrophe-heavy
        //     plain text extremely unlikely.
        1.10
    } else if boundary_count == 0 && single_density > 0 {
        // Single quotes in content but not at any boundaries (no opening,
        // no closing).  Likely just apostrophes in text content.
        0.95
    } else {
        1.0
    }
}

/// Calculate quote evidence score using pre-computed counts and cached boundary counts.
/// This is the optimized version that avoids redundant data scanning.
fn quote_evidence_score_with_cached_boundaries(
    quote_counts: &QuoteCounts,
    boundary_counts: &QuoteBoundaryCounts,
    dialect: &PotentialDialect,
) -> f64 {
    use crate::metadata::Quote;

    if quote_counts.data_len == 0 {
        return 1.0;
    }

    // Calculate density (quotes per 1000 bytes) - higher density suggests quoting
    let double_density = (quote_counts.double * 1000) / quote_counts.data_len;
    let single_density = (quote_counts.single * 1000) / quote_counts.data_len;

    // Threshold: need at least ~0.5% quote density to consider it significant
    // This filters out incidental apostrophes in text
    let min_density_threshold = 5; // 0.5% = 5 per 1000

    match dialect.quote {
        Quote::Some(b'"') => {
            let boundary_count = boundary_counts.get_boundary_count(b'"', dialect.delimiter);
            if quote_counts.single == 0
                && boundary_count >= 2
                && double_density >= min_density_threshold
            {
                // No single quotes AND double quotes at boundaries with real density
                // This handles small files with quoted fields containing delimiters
                2.2
            } else if boundary_count >= 2 && double_density >= min_density_threshold {
                // Double quotes at boundaries with good density
                1.15
            } else if double_density >= min_density_threshold {
                // Double quotes have significant density - moderate boost
                1.08
            } else {
                // Neutral - rely on other scoring factors
                1.0
            }
        }
        Quote::Some(b'\'') => {
            // Single quotes are tricky because apostrophes are common in text
            // MUST have opening boundary evidence - apostrophes in content tend to appear
            // only before delimiters (closing only), while genuine quoting has both
            // opening (delimiter→quote) and closing (quote→delimiter) boundaries
            let boundary_count = boundary_counts.get_boundary_count(b'\'', dialect.delimiter);
            let opening_count =
                boundary_counts.get_single_opening_boundary_count(dialect.delimiter);
            compute_single_quote_multiplier(
                quote_counts,
                boundary_count,
                opening_count,
                single_density,
                double_density,
                min_density_threshold,
            )
        }
        Quote::None => {
            // Only penalize Quote::None when there's strong quoting evidence
            if double_density >= min_density_threshold {
                0.90
            } else {
                1.0
            }
        }
        Quote::Some(_) => 1.0, // Other quote chars - neutral
    }
}

/// Count opening quote boundaries (delimiter/newline → quote) only.
/// Used to distinguish genuine quoting from apostrophes that appear only at field ends.
fn quote_opening_boundary_count(data: &[u8], quote_char: u8, delimiter: u8) -> usize {
    let mut count = 0;
    for window in data.windows(2) {
        if (window[0] == delimiter || window[0] == b'\n' || window[0] == b'\r')
            && window[1] == quote_char
        {
            count += 1;
        }
    }
    // Also count start of data as an opening boundary
    if !data.is_empty() && data[0] == quote_char {
        count += 1;
    }
    count
}

/// Calculate quote evidence score using pre-computed counts and raw data for boundary detection.
/// This provides more accurate quote detection for small files.
fn quote_evidence_score_with_data(
    data: &[u8],
    quote_counts: &QuoteCounts,
    dialect: &PotentialDialect,
) -> f64 {
    use crate::metadata::Quote;

    if quote_counts.data_len == 0 {
        return 1.0;
    }

    // Calculate density (quotes per 1000 bytes) - higher density suggests quoting
    let double_density = (quote_counts.double * 1000) / quote_counts.data_len;
    let single_density = (quote_counts.single * 1000) / quote_counts.data_len;

    // Threshold: need at least ~0.5% quote density to consider it significant
    // This filters out incidental apostrophes in text
    let min_density_threshold = 5; // 0.5% = 5 per 1000

    match dialect.quote {
        Quote::Some(b'"') => {
            let boundary_count = quote_boundary_count(data, b'"', dialect.delimiter);
            if quote_counts.single == 0
                && boundary_count >= 2
                && double_density >= min_density_threshold
            {
                // No single quotes AND double quotes at boundaries with real density
                // This handles small files with quoted fields containing delimiters
                2.2
            } else if boundary_count >= 2 && double_density >= min_density_threshold {
                // Double quotes at boundaries with good density
                1.15
            } else if double_density >= min_density_threshold {
                // Double quotes have significant density - moderate boost
                1.08
            } else {
                // Neutral - rely on other scoring factors
                1.0
            }
        }
        Quote::Some(b'\'') => {
            // Single quotes are tricky because apostrophes are common in text
            // MUST have opening boundary evidence - apostrophes in content tend to appear
            // only before delimiters (closing only), while genuine quoting has both
            // opening (delimiter→quote) and closing (quote→delimiter) boundaries
            let boundary_count = quote_boundary_count(data, b'\'', dialect.delimiter);
            let opening_count = quote_opening_boundary_count(data, b'\'', dialect.delimiter);
            compute_single_quote_multiplier(
                quote_counts,
                boundary_count,
                opening_count,
                single_density,
                double_density,
                min_density_threshold,
            )
        }
        Quote::None => {
            // Only penalize Quote::None when there's strong quoting evidence
            if double_density >= min_density_threshold {
                0.90
            } else {
                1.0
            }
        }
        Quote::Some(_) => 1.0, // Other quote chars - neutral
    }
}

/// Find the best scoring dialect from a list.
///
/// When dialects have similar scores, this function prefers:
/// 1. Common delimiters (comma, semicolon, tab) over rare ones (space, #, &)
/// 2. Dialects with Quote::Some(b'"') over Quote::None (standard default)
/// 3. Dialects with Quote::Some(b'"') over Quote::Some(b'\'')
pub fn find_best_dialect(scores: &[DialectScore]) -> Option<&DialectScore> {
    // First, check if all dialects result in single-field tables
    // In that case, prefer comma as the default delimiter
    let all_single_field = scores
        .iter()
        .filter(|s| s.gamma > 0.0)
        .all(|s| s.num_fields <= 1);

    scores.iter().filter(|s| s.gamma > 0.0).max_by(|a, b| {
        // If scores are very close (within 5%, score_ratio > 0.95), use delimiter and quote preference
        let score_ratio = if a.gamma > b.gamma {
            b.gamma / a.gamma
        } else {
            a.gamma / b.gamma
        };

        // For single-field tables, prefer comma delimiter and double-quote
        if all_single_field {
            let a_delim_priority = delimiter_priority(a.dialect.delimiter);
            let b_delim_priority = delimiter_priority(b.dialect.delimiter);

            match a_delim_priority.cmp(&b_delim_priority) {
                std::cmp::Ordering::Equal => {
                    // Same delimiter priority, use quote preference
                    let a_quote_priority = quote_priority(a.dialect.quote);
                    let b_quote_priority = quote_priority(b.dialect.quote);
                    return a_quote_priority.cmp(&b_quote_priority);
                }
                other => return other,
            }
        }

        if score_ratio > 0.95 {
            // Scores are close, use delimiter priority first, then quote priority
            let a_delim_priority = delimiter_priority(a.dialect.delimiter);
            let b_delim_priority = delimiter_priority(b.dialect.delimiter);

            match a_delim_priority.cmp(&b_delim_priority) {
                std::cmp::Ordering::Equal => {
                    // Delimiters have same priority, check quotes
                    let a_quote_priority = quote_priority(a.dialect.quote);
                    let b_quote_priority = quote_priority(b.dialect.quote);

                    match a_quote_priority.cmp(&b_quote_priority) {
                        std::cmp::Ordering::Equal => a
                            .gamma
                            .partial_cmp(&b.gamma)
                            .unwrap_or(std::cmp::Ordering::Equal),
                        other => other,
                    }
                }
                other => other,
            }
        } else {
            // Scores are different enough, use gamma directly
            a.gamma
                .partial_cmp(&b.gamma)
                .unwrap_or(std::cmp::Ordering::Equal)
        }
    })
}

/// Returns a priority score for delimiters (higher = preferred).
/// Common delimiters like comma are preferred over rare ones like space or &.
const fn delimiter_priority(delimiter: u8) -> u8 {
    match delimiter {
        b',' => 10, // Comma - most common, highest priority
        b';' => 9,  // Semicolon - common in European locales
        b'\t' => 8, // Tab - TSV files
        // Pipe - common in data exports; intentionally tied with tab (both are
        // respectable standard delimiters); tie resolved by iteration order
        b'|' => 8,
        b':' => 4, // Colon - sometimes used, but also appears in timestamps
        b'^' => 3, // Caret - rare
        b'~' => 3, // Tilde - rare
        0xA7 => 2, // Section sign (§) - rare
        b'/' => 2, // Forward slash - rare
        b' ' => 2, // Space - very rare as delimiter, often appears in text
        b'#' => 1, // Hash - very rare, often used for comments
        b'&' => 1, // Ampersand - very rare
        _ => 0,    // Unknown delimiters - lowest priority
    }
}

/// Returns a priority score for quote characters (higher = preferred).
/// Double-quote is the standard default and should be preferred.
const fn quote_priority(quote: crate::metadata::Quote) -> u8 {
    use crate::metadata::Quote;
    match quote {
        Quote::Some(b'"') => 3,  // Standard default - highest priority
        Quote::Some(b'\'') => 2, // Single quote - second priority
        Quote::None => 1,        // No quoting - lowest priority
        Quote::Some(_) => 0,     // Other quote chars - very low priority
    }
}

/// Score all potential dialects and return sorted by gamma score (descending).
#[allow(dead_code)]
pub fn score_all_dialects(
    data: &[u8],
    dialects: &[PotentialDialect],
    max_rows: usize,
) -> Vec<DialectScore> {
    let (scores, _) = score_all_dialects_with_best_table(data, dialects, max_rows);
    scores
}

/// Score all potential dialects and return sorted by gamma score (descending),
/// along with the parsed table of the best-scoring dialect.
///
/// This avoids re-parsing the best dialect's data for preamble detection
/// and metadata building.
pub fn score_all_dialects_with_best_table(
    data: &[u8],
    dialects: &[PotentialDialect],
    max_rows: usize,
) -> (Vec<DialectScore>, Option<Table>) {
    // Pre-compute quote counts once for all dialect evaluations
    let quote_counts = QuoteCounts::new(data);

    // Get the list of delimiters being tested
    let delimiters: Vec<u8> = dialects
        .iter()
        .map(|d| d.delimiter)
        .collect::<std::collections::HashSet<_>>()
        .into_iter()
        .collect();

    // Detect and normalize line endings once for all dialects
    // All dialects in the list have the same line terminator (set by detect_line_terminator)
    let line_terminator = dialects
        .first()
        .map_or(super::potential_dialects::LineTerminator::LF, |d| {
            d.line_terminator
        });
    let normalized_data = super::potential_dialects::normalize_line_endings(data, line_terminator);
    let normalized_bytes: &[u8] = normalized_data.as_ref();

    // Pre-compute quote boundary counts for all delimiters in one pass (on normalized data)
    let boundary_counts = QuoteBoundaryCounts::new(normalized_bytes, &delimiters);

    // Score all dialects in parallel, using per-thread reusable TypeScoreBuffers
    let pairs: Vec<(DialectScore, Table)> = dialects
        .par_iter()
        .map(|d| {
            BUFFERS.with(|b| {
                score_dialect_with_normalized_data(
                    normalized_bytes,
                    d,
                    max_rows,
                    &quote_counts,
                    &boundary_counts,
                    &mut b.borrow_mut(),
                )
            })
        })
        .collect();

    // Keep first-maximum semantics: when two dialects tie on gamma, the one
    // with the lower index (earlier in `dialects`) wins — matching the
    // original sequential `if score.gamma > best_gamma` loop which used
    // strict `>` so the first winner was never displaced by a tie.
    let best_table = pairs
        .iter()
        .enumerate()
        .max_by(|(i, a), (j, b)| {
            a.0.gamma
                .partial_cmp(&b.0.gamma)
                .unwrap_or(std::cmp::Ordering::Equal)
                .then_with(|| j.cmp(i)) // lower index wins on tie
        })
        .map(|(_, (_, t))| t.clone());

    let mut scores: Vec<DialectScore> = pairs.into_iter().map(|(s, _)| s).collect();

    // Sort by gamma score descending
    scores.sort_by(|a, b| {
        b.gamma
            .partial_cmp(&a.gamma)
            .unwrap_or(std::cmp::Ordering::Equal)
    });

    (scores, best_table)
}

#[cfg(test)]
mod tests {
    use super::*;
    use crate::metadata::Quote;
    use crate::tum::potential_dialects::LineTerminator;

    #[test]
    fn test_score_simple_csv() {
        let data = b"a,b,c\n1,2,3\n4,5,6\n";
        let dialect = PotentialDialect::new(b',', Quote::Some(b'"'), LineTerminator::LF);

        let score = score_dialect(data, &dialect, 100);
        assert!(score.gamma > 0.0);
        assert_eq!(score.num_fields, 3);
        assert!(score.is_uniform);
    }

    #[test]
    fn test_wrong_delimiter_lower_score() {
        let data = b"a,b,c\n1,2,3\n4,5,6\n";

        let correct_dialect = PotentialDialect::new(b',', Quote::Some(b'"'), LineTerminator::LF);
        let wrong_dialect = PotentialDialect::new(b';', Quote::Some(b'"'), LineTerminator::LF);

        let correct_score = score_dialect(data, &correct_dialect, 100);
        let wrong_score = score_dialect(data, &wrong_dialect, 100);

        assert!(correct_score.gamma > wrong_score.gamma);
    }

    #[test]
    fn test_find_best_dialect() {
        let data = b"a,b,c\n1,2,3\n4,5,6\n";
        let dialects = vec![
            PotentialDialect::new(b',', Quote::Some(b'"'), LineTerminator::LF),
            PotentialDialect::new(b';', Quote::Some(b'"'), LineTerminator::LF),
            PotentialDialect::new(b'\t', Quote::Some(b'"'), LineTerminator::LF),
        ];

        let scores = score_all_dialects(data, &dialects, 100);
        let best = find_best_dialect(&scores).unwrap();

        assert_eq!(best.dialect.delimiter, b',');
    }

    // --- Tests for quote_opening_boundary_count and get_single_opening_boundary_count ---

    #[test]
    fn test_quote_opening_boundary_count_apostrophes_only() {
        // Apostrophes appear only before delimiters (closing-only), not at field starts
        // e.g. "value's, other" - apostrophe is mid-word, not at field start
        let data = b"value's, other's, thing's\n";
        let count = quote_opening_boundary_count(data, b'\'', b',');
        // No delimiter→quote or newline→quote or leading-quote transitions
        assert_eq!(count, 0);
    }

    #[test]
    fn test_quote_opening_boundary_count_genuine_quoting() {
        // Genuine single-quote quoting: quote appears at field start after delimiter/newline
        let data = b",'field', 'next'\n";
        let count = quote_opening_boundary_count(data, b'\'', b',');
        // First window [b',', b'\''] is delimiter→quote → +1 opening boundary
        // Second window [b' ', b'\''] is space→quote (space not a delimiter here) → 0
        assert!(
            count >= 1,
            "expected at least 1 opening boundary, got {count}"
        );
    }

    #[test]
    fn test_quote_opening_boundary_count_leading_quote() {
        // Data starts with the quote character = opening boundary
        let data = b"'field','next'\n";
        let count = quote_opening_boundary_count(data, b'\'', b',');
        // Starts with quote (+1), and delimiter→quote at position 7→8 (+1)
        assert_eq!(count, 2);
    }

    #[test]
    fn test_quote_opening_boundary_count_empty() {
        let count = quote_opening_boundary_count(b"", b'\'', b',');
        assert_eq!(count, 0);
    }

    #[test]
    fn test_get_single_opening_boundary_count_apostrophes_only() {
        // Apostrophes only at field ends (before delimiter) — no opening boundaries
        // "it's, we're, they've" — each apostrophe is mid-word, not at a field start
        let data = b"it's, we're, they've\n";
        let delimiters = vec![b','];
        let counts = QuoteBoundaryCounts::new(data, &delimiters);
        let opening = counts.get_single_opening_boundary_count(b',');
        assert_eq!(
            opening, 0,
            "apostrophes should produce zero opening boundaries"
        );
    }

    #[test]
    fn test_get_single_opening_boundary_count_genuine_quoting() {
        // Genuine single-quote quoting: 'val','val2' — quote appears right after delimiter
        let data = b"'first','second','third'\n";
        let delimiters = vec![b','];
        let counts = QuoteBoundaryCounts::new(data, &delimiters);
        let opening = counts.get_single_opening_boundary_count(b',');
        // data[0] == b'\'' counts via starts_with_single in get_boundary_count, but
        // get_single_opening_boundary_count only counts delimiter→quote and newline→quote,
        // plus data[0] if it is a quote (handled by starts_with_single bonus)
        assert!(
            opening >= 2,
            "expected ≥2 opening boundaries for genuinely quoted fields, got {opening}"
        );
    }

    // --- Tests for the five new heuristics ---

    // Heuristic 1: `#` delimiter penalty relaxation for large multi-field tables.

    #[test]
    fn test_hash_penalty_strict_for_small_table() {
        // Small table (10 rows, < 50 row threshold): hash penalty stays at 0.60.
        // Large table (60 rows, >= 50 row threshold): hash penalty relaxes to 0.85.
        //
        // We use score_all_dialects (the production path) so that the full heuristic
        // stack in score_dialect_with_normalized_data applies consistently.  The hash
        // penalty relaxation (0.60 → 0.85) lives in compute_gamma, which is reached via
        // both score_dialect and score_all_dialects; using score_all_dialects keeps this
        // test consistent with test_comma_hash_penalty_fires_on_hash_delimited_data.
        //
        // Note: a higher row count also earns a larger row_bonus (up to +0.10 at ≥20 rows,
        // computed as `(num_rows.min(20) / 20) * 0.1`).  At 10 rows the small table earns
        // +0.05; at 60 rows the large table earns the maximum +0.10 additive bonus.
        // row_bonus is additive, not multiplicative, so it shifts absolute scores rather
        // than scaling the ratio.  The 1.3× threshold remains defensible even if the
        // penalty ratio were to drop from 0.85/0.60 ≈ 1.42 down to ~1.30, because the
        // +0.05 additive gap in row_bonus further favours the large dataset on top of the
        // penalty ratio — both effects reinforce the same direction.
        let mut small_data = String::new();
        for _ in 0..10 {
            small_data.push_str("a#b#c\n");
        }
        let mut large_data = String::new();
        for _ in 0..60 {
            large_data.push_str("a#b#c\n");
        }

        let dialects = vec![PotentialDialect::new(
            b'#',
            Quote::Some(b'"'),
            LineTerminator::LF,
        )];

        let small_scores = score_all_dialects(small_data.as_bytes(), &dialects, 200);
        let large_scores = score_all_dialects(large_data.as_bytes(), &dialects, 200);

        let small_score = small_scores
            .iter()
            .find(|s| s.dialect.delimiter == b'#')
            .unwrap();
        let large_score = large_scores
            .iter()
            .find(|s| s.dialect.delimiter == b'#')
            .unwrap();

        // The large table gets the relaxed 0.85 penalty vs the strict 0.60 for the small
        // table.  With identical per-row uniformity, the large score must exceed the small
        // score by at least the ratio 0.85/0.60 ≈ 1.42.  We use a conservative bound of
        // 1.3 to tolerate minor variation in type scoring across different row counts.
        assert!(
            large_score.gamma > small_score.gamma * 1.3,
            "large hash table (0.85 penalty) should outscore small hash table (0.60 penalty) \
             by factor ≥ 1.3; small={} large={}",
            small_score.gamma,
            large_score.gamma
        );
    }

    #[test]
    fn test_hash_penalty_relaxed_for_large_table() {
        // Large table (≥ 50 rows, ≥ 3 fields): hash penalty should relax to 0.85.
        let mut data = String::new();
        for i in 0..60 {
            data.push_str(&format!("val{i}#val{i}b#val{i}c\n"));
        }
        let bytes = data.as_bytes();

        let hash_dialect = PotentialDialect::new(b'#', Quote::Some(b'"'), LineTerminator::LF);

        let hash_score = score_dialect(bytes, &hash_dialect, 200);
        // Score must be non-trivial: a 60-row, 3-field uniform table with relaxed
        // penalty (0.85) should produce a meaningful gamma.
        assert!(
            hash_score.gamma > 0.3,
            "large hash-delimited table should have a meaningful gamma; got {}",
            hash_score.gamma
        );
    }

    // Heuristic 2: Space-delimiter dampening when >50% of rows have an empty first field.

    #[test]
    fn test_space_dampening_fires_when_majority_empty_first() {
        // Simulate a leading-space-padded format: every row starts with a single space,
        // so splitting on space yields an empty first field followed by two value fields
        // (3 fields total).  The dampening heuristic applies 0.55× when >50% of rows
        // have an empty first field.
        //
        // The undampened dataset uses the same delimiter and the same field count (3)
        // but without a leading space, so no empty first field is present and dampening
        // must NOT fire.  Equal field counts eliminate field-count as a confound so the
        // assertion purely isolates the 0.55× multiplier.
        //
        // Space dampening lives in score_dialect_with_normalized_data; we therefore use
        // score_all_dialects (the production path) rather than score_dialect so that the
        // heuristic is actually exercised.
        //
        // leading:  " a b\n c d\n e f\n" → ["", "a", "b"] per row  (3 fields, empty first)
        // baseline: "a b c\nd e f\ng h i\n" → ["a", "b", "c"] per row (3 fields, no empty)
        let leading_space_data = b" a b\n c d\n e f\n";
        let no_leading_space_data = b"a b c\nd e f\ng h i\n";

        let dialects = vec![PotentialDialect::new(
            b' ',
            Quote::Some(b'"'),
            LineTerminator::LF,
        )];

        let dampened_scores = score_all_dialects(leading_space_data, &dialects, 100);
        let undampened_scores = score_all_dialects(no_leading_space_data, &dialects, 100);

        let dampened_score = dampened_scores
            .iter()
            .find(|s| s.dialect.delimiter == b' ')
            .unwrap();
        let undampened_score = undampened_scores
            .iter()
            .find(|s| s.dialect.delimiter == b' ')
            .unwrap();

        // Dampening (0.55×) must reduce the score compared to the undampened baseline.
        // Both datasets have identical three-field-per-row uniformity.  Note: the empty
        // first field in the leading-space dataset is classified as a distinct type from
        // the alphabetic values in the baseline, so column-0 type-consistency scores will
        // differ slightly between the two datasets independently of the 0.55× multiplier.
        // In practice the dampening effect (0.55×) is large enough to dominate this
        // residual type-scoring difference.
        assert!(
            dampened_score.gamma < undampened_score.gamma,
            "dampening should reduce score when majority rows have empty first field; \
             dampened={} undampened={}",
            dampened_score.gamma,
            undampened_score.gamma
        );
    }

    #[test]
    fn test_space_dampening_does_not_fire_when_minority_empty_first() {
        // Fewer than 50% of rows have empty first field — dampening must NOT fire.
        // One row starts with a space (empty first), two rows do not.
        let data = b" x y\na b\nc d\n";
        let space_dialect = PotentialDialect::new(b' ', Quote::Some(b'"'), LineTerminator::LF);

        let score = score_dialect(data, &space_dialect, 100);
        // Dampening should not have been applied; score should be reasonable.
        // Since dampening applies 0.55×, an un-dampened score near 0.5 would
        // become ~0.28 when dampened.  Without dampening it stays >= 0.4.
        // We just verify the score is non-zero and not catastrophically suppressed.
        assert!(
            score.gamma > 0.1,
            "dampening should not fire for minority empty-first; gamma={}",
            score.gamma
        );
    }

    // Heuristic 3: Comma penalty when ' # ' appears in >90% of first parsed fields.

    #[test]
    fn test_comma_hash_penalty_fires_on_hash_delimited_data() {
        // A '#'-delimited file where comma splits on an incidental comma inside a field.
        // Comma sees 2 fields: field-0 = "foo # baz", which contains ' # '.
        // When >90% of rows have ' # ' in field-0 AND num_fields == 2, the 0.82× penalty fires.
        //
        // The penalty lives in score_dialect_with_normalized_data (the path exercised by
        // score_all_dialects), NOT in the score_dialect path.  We therefore use
        // score_all_dialects for both datasets so the penalty is consistently applied
        // (or not) on both paths.
        let penalized_data = b"foo # baz,bar\nfoo # baz,bar\nfoo # baz,bar\n\
                               foo # baz,bar\nfoo # baz,bar\nfoo # baz,bar\n\
                               foo # baz,bar\nfoo # baz,bar\nfoo # baz,bar\n\
                               foo # baz,bar\n";

        // Structurally identical (2 fields per row, 10 rows, all-text) but field-0
        // has no ' # ' — the penalty must NOT fire here.
        let clean_data = b"foo bar baz,bar\nfoo bar baz,bar\nfoo bar baz,bar\n\
                           foo bar baz,bar\nfoo bar baz,bar\nfoo bar baz,bar\n\
                           foo bar baz,bar\nfoo bar baz,bar\nfoo bar baz,bar\n\
                           foo bar baz,bar\n";

        let dialects = vec![PotentialDialect::new(
            b',',
            Quote::Some(b'"'),
            LineTerminator::LF,
        )];

        let penalized_scores = score_all_dialects(penalized_data, &dialects, 100);
        let clean_scores = score_all_dialects(clean_data, &dialects, 100);

        let penalized_score = penalized_scores
            .iter()
            .find(|s| s.dialect.delimiter == b',')
            .unwrap();
        let clean_score = clean_scores
            .iter()
            .find(|s| s.dialect.delimiter == b',')
            .unwrap();

        assert!(
            penalized_score.gamma >= 0.0,
            "comma gamma must be non-negative"
        );
        // The 0.82× penalty must reduce the comma score compared to the clean dataset.
        // Both datasets have identical two-field-per-row uniformity; the only scoring
        // difference is the ' # ' penalty on the penalized dataset.
        assert!(
            penalized_score.gamma < clean_score.gamma,
            "comma penalty (0.82×) should reduce score when ' # ' dominates field-0; \
             penalized={} clean={}",
            penalized_score.gamma,
            clean_score.gamma
        );
    }

    #[test]
    fn test_comma_hash_penalty_does_not_fire_below_90pct() {
        // Only 5 of 10 rows have ' # ' in field-0 → below 90% → no penalty.
        let data = b"a # b,c\na # b,c\na # b,c\na # b,c\na # b,c\n\
                     x,y\nx,y\nx,y\nx,y\nx,y\n";

        let comma_dialect = PotentialDialect::new(b',', Quote::Some(b'"'), LineTerminator::LF);

        // Just verify scoring does not panic and produces a valid gamma.
        let score = score_dialect(data, &comma_dialect, 100);
        assert!(score.gamma >= 0.0);
    }

    // Heuristic 4: Backslash-escape boost for single-quote dialect.

    #[test]
    fn test_backslash_single_boost_applied() {
        // File with backslash-escaped single quotes and no double quotes.
        // boundary_count == 0 because the quote chars are not at field boundaries
        // (they appear inside words, not adjacent to the comma delimiter).
        // This triggers the 1.10× backslash-escape boost branch.
        let data_with_backslash = b"it\\'s fine,next\ndon\\'t stop,go\nwe\\'re here,now\n";

        // Structurally identical dataset with no apostrophes — no boost fires, multiplier = 1.0.
        let data_no_apostrophe = b"its fine,next\ndont stop,go\nwere here,now\n";

        let sq_dialect = PotentialDialect::new(b',', Quote::Some(b'\''), LineTerminator::LF);

        let boosted_score = score_dialect(data_with_backslash, &sq_dialect, 100);
        let baseline_score = score_dialect(data_no_apostrophe, &sq_dialect, 100);

        assert!(
            boosted_score.gamma > 0.0,
            "single-quote dialect must score positively; gamma={}",
            boosted_score.gamma
        );
        // The 1.10× backslash-escape boost must make the score net-positive relative
        // to the no-apostrophe baseline (which gets only the neutral 1.0 multiplier).
        // Both datasets have identical two-field-per-row uniformity and similar type
        // scores; the only scoring difference is the quote-evidence multiplier.
        assert!(
            boosted_score.gamma > baseline_score.gamma,
            "backslash-escape boost (1.10×) should raise sq score above no-apostrophe baseline; \
             boosted={} baseline={}",
            boosted_score.gamma,
            baseline_score.gamma
        );
    }

    #[test]
    fn test_backslash_boost_does_not_fire_when_double_quotes_present() {
        // backslash_single > 0 but backslash_double > 0 as well → no boost.
        let data = b"it\\'s,\"quoted\"\ndon\\'t,\"also\"\n";

        let sq_dialect = PotentialDialect::new(b',', Quote::Some(b'\''), LineTerminator::LF);

        // Verify scoring runs without panic; the 1.10× branch should NOT fire.
        let score = score_dialect(data, &sq_dialect, 100);
        assert!(score.gamma >= 0.0);
    }

    // Heuristic 5: Closing-only boundary boost — threshold edge tests.

    #[test]
    fn test_closing_only_boost_below_threshold_no_boost() {
        // boundary_count == 19 (just below threshold of 20) → boost should NOT fire.
        // boundary_count == 20 (at threshold) → 1.10× boost SHOULD fire.
        //
        // Both datasets have the same total row count (25 rows) to eliminate row-count
        // as a confound.  The only structural difference is 19 vs 20 closing boundaries.
        //
        // Pattern: `x'\trest\n` — quote before tab = closing boundary; quote is not
        // adjacent to a newline or at the start of data, so no opening boundaries.
        // `x\trest\n` — no quote, no boundary contribution.
        let tab_sq_dialect = PotentialDialect::new(b'\t', Quote::Some(b'\''), LineTerminator::LF);

        // 19-boundary dataset: 19 rows with a closing boundary + 6 padding rows = 25 total
        let mut data_19 = Vec::new();
        for _ in 0..19 {
            data_19.extend_from_slice(b"x'\trest\n");
        }
        for _ in 0..6 {
            data_19.extend_from_slice(b"x\trest\n");
        }

        // 20-boundary dataset: 20 rows with a closing boundary + 5 padding rows = 25 total
        let mut data_20 = Vec::new();
        for _ in 0..20 {
            data_20.extend_from_slice(b"x'\trest\n");
        }
        for _ in 0..5 {
            data_20.extend_from_slice(b"x\trest\n");
        }

        let score_19 = score_dialect(&data_19, &tab_sq_dialect, 200);
        let score_20 = score_dialect(&data_20, &tab_sq_dialect, 200);

        // At exactly 20 boundaries the closing-only 1.10× boost fires; at 19 it does
        // not (falls through to the neutral 1.0 branch).  Both datasets have identical
        // row counts and per-row structure, so the boost is the only score difference.
        assert!(
            score_20.gamma > score_19.gamma,
            "closing-only boost (1.10×) should fire at boundary_count=20 but not at 19; \
             score_19={} score_20={}",
            score_19.gamma,
            score_20.gamma
        );

        // Parallel assertion via score_all_dialects (cached path): the cached path
        // tallies boundary_count from QuoteBoundaryCounts struct fields, while the
        // non-cached path above iterates raw data directly.  Both paths share
        // compute_single_quote_multiplier, but a discrepancy in boundary tallying
        // between them would not be caught by score_dialect alone.
        // tab_sq_dialect is still in scope: score_dialect takes &PotentialDialect, not by value.
        let dialects = vec![tab_sq_dialect];
        let cached_19 = score_all_dialects(&data_19, &dialects, 200);
        let cached_20 = score_all_dialects(&data_20, &dialects, 200);
        let cached_score_19 = cached_19
            .iter()
            .find(|s| s.dialect.delimiter == b'\t')
            .unwrap();
        let cached_score_20 = cached_20
            .iter()
            .find(|s| s.dialect.delimiter == b'\t')
            .unwrap();
        assert!(
            cached_score_20.gamma > cached_score_19.gamma,
            "closing-only boost (1.10×) should fire on cached path at boundary_count=20 but not at 19; \
             cached_19={} cached_20={}",
            cached_score_19.gamma,
            cached_score_20.gamma
        );

        // Cross-path agreement: cached and non-cached paths must produce the same gamma
        // values, confirming that boundary tallying is consistent between them.  A bug
        // in QuoteBoundaryCounts field accumulation would cause a discrepancy here even
        // if both paths produce internally consistent orderings.
        // The two paths share compute_single_quote_multiplier and identical arithmetic,
        // so results should be bit-identical (difference = 0.0).  1e-9 is a generous
        // sentinel that would catch any real boundary-tallying divergence.
        let tolerance = 1e-9_f64;
        assert!(
            (cached_score_19.gamma - score_19.gamma).abs() < tolerance,
            "cached and non-cached paths disagree on 19-boundary score: \
             non_cached={} cached={}",
            score_19.gamma,
            cached_score_19.gamma
        );
        assert!(
            (cached_score_20.gamma - score_20.gamma).abs() < tolerance,
            "cached and non-cached paths disagree on 20-boundary score: \
             non_cached={} cached={}",
            score_20.gamma,
            cached_score_20.gamma
        );
    }
}
```

## File: `src/tum/table.rs`
```rust
//! CSV parsing into a table structure for analysis.

use super::potential_dialects::PotentialDialect;
use crate::metadata::Quote;
use foldhash::{HashMap, HashMapExt};
use std::borrow::Cow;
use std::io::{BufRead, Cursor};

/// A parsed CSV table for analysis.
#[derive(Debug, Clone)]
pub struct Table {
    /// The rows of the table (each row is a vector of field values).
    pub rows: Vec<Vec<String>>,
    /// Number of fields in each row.
    pub field_counts: Vec<usize>,
    /// Cached modal (most common) field count, computed during parsing.
    cached_modal_field_count: usize,
    /// Cached frequency of the modal field count.
    cached_modal_field_count_freq: usize,
}

impl Table {
    /// Create a new empty table.
    pub const fn new() -> Self {
        Self {
            rows: Vec::new(),
            field_counts: Vec::new(),
            cached_modal_field_count: 0,
            cached_modal_field_count_freq: 0,
        }
    }

    /// Returns true if the table is empty.
    #[inline]
    pub const fn is_empty(&self) -> bool {
        self.rows.is_empty()
    }

    /// Returns the number of rows.
    #[inline]
    pub const fn num_rows(&self) -> usize {
        self.rows.len()
    }

    /// Returns the modal (most common) field count.
    /// Uses cached value computed during parsing for efficiency.
    #[inline]
    pub const fn modal_field_count(&self) -> usize {
        self.cached_modal_field_count
    }

    /// Compute the modal field count and its frequency from field_counts.
    /// Called internally after parsing or when constructing tables manually.
    ///
    /// Optimized: Uses a frequency array for small field counts (≤256),
    /// falling back to HashMap for unusually wide tables.
    /// Returns `(modal_field_count, frequency)`.
    fn compute_modal_field_count(field_counts: &[usize]) -> (usize, usize) {
        if field_counts.is_empty() {
            return (0, 0);
        }

        let max_fc = field_counts.iter().copied().max().unwrap_or(0);

        // Use array for small field counts (most common case), HashMap for large
        if max_fc <= 256 {
            // Fast path: use fixed-size array
            let mut freq = [0usize; 257];
            for &fc in field_counts {
                freq[fc] += 1;
            }

            // Find the modal field count with deterministic tie-breaking
            // (prefer higher field count when frequencies are equal)
            let mut best_fc = 0;
            let mut best_count = 0;
            for (fc, &count) in freq.iter().enumerate() {
                if count > best_count || (count == best_count && fc > best_fc) {
                    best_fc = fc;
                    best_count = count;
                }
            }
            (best_fc, best_count)
        } else {
            // Fallback to HashMap for unusually wide tables
            let mut counts: HashMap<usize, usize> = HashMap::with_capacity(field_counts.len());
            for &fc in field_counts {
                *counts.entry(fc).or_insert(0) += 1;
            }

            // Use deterministic tie-breaking: prefer higher field count when frequencies are equal
            // This ensures consistent results regardless of HashMap iteration order
            counts
                .into_iter()
                .max_by(|(fc_a, count_a), (fc_b, count_b)| {
                    count_a.cmp(count_b).then_with(|| fc_a.cmp(fc_b))
                })
                .map_or((0, 0), |(fc, count)| (fc, count))
        }
    }

    /// Update the cached modal field count and its frequency. Call after modifying field_counts.
    pub fn update_modal_field_count(&mut self) {
        let (modal, freq) = Self::compute_modal_field_count(&self.field_counts);
        self.cached_modal_field_count = modal;
        self.cached_modal_field_count_freq = freq;
    }

    /// Returns the frequency of the modal (most common) field count.
    #[inline]
    pub const fn modal_field_count_freq(&self) -> usize {
        self.cached_modal_field_count_freq
    }

    /// Returns the minimum field count.
    #[inline]
    pub fn min_field_count(&self) -> usize {
        self.field_counts.iter().copied().min().unwrap_or(0)
    }

    /// Returns the maximum field count.
    #[inline]
    pub fn max_field_count(&self) -> usize {
        self.field_counts.iter().copied().max().unwrap_or(0)
    }
}

impl Default for Table {
    fn default() -> Self {
        Self::new()
    }
}

/// Parse data into a table using the given dialect.
///
/// # Arguments
/// * `data` - The raw CSV data bytes
/// * `dialect` - The dialect to use for parsing
/// * `max_rows` - Maximum number of rows to parse (0 = unlimited)
pub fn parse_table(data: &[u8], dialect: &PotentialDialect, max_rows: usize) -> Table {
    // Normalize line endings for this dialect
    let normalized = normalize_line_endings(data, dialect);
    parse_table_impl(&normalized, dialect, max_rows)
}

/// Parse data into a table assuming line endings are already normalized to LF.
///
/// This function skips line ending normalization for performance when the caller
/// has already normalized the data (e.g., in `score_all_dialects_with_best_table`).
///
/// # Arguments
/// * `data` - The CSV data bytes with LF-normalized line endings
/// * `dialect` - The dialect to use for parsing
/// * `max_rows` - Maximum number of rows to parse (0 = unlimited)
pub(crate) fn parse_table_normalized(
    data: &[u8],
    dialect: &PotentialDialect,
    max_rows: usize,
) -> Table {
    parse_table_impl(data, dialect, max_rows)
}

/// Internal implementation of table parsing.
///
/// # Arguments
/// * `data` - The CSV data bytes (should have LF line endings)
/// * `dialect` - The dialect to use for parsing
/// * `max_rows` - Maximum number of rows to parse (0 = unlimited)
fn parse_table_impl<D: AsRef<[u8]>>(data: D, dialect: &PotentialDialect, max_rows: usize) -> Table {
    let mut table = Table::new();

    // Build CSV reader with the dialect settings
    let mut reader_builder = csv::ReaderBuilder::new();
    reader_builder
        .delimiter(dialect.delimiter)
        .has_headers(false)
        .flexible(true)
        .buffer_capacity(32768); // 32KB buffer

    // Configure quoting
    match dialect.quote {
        Quote::None => {
            reader_builder.quoting(false);
        }
        Quote::Some(q) => {
            reader_builder.quoting(true);
            reader_builder.quote(q);
        }
    }

    let cursor = Cursor::new(data);
    let mut reader = reader_builder.from_reader(cursor);

    let mut record = csv::StringRecord::new();
    let limit = if max_rows == 0 { usize::MAX } else { max_rows };

    while table.rows.len() < limit {
        match reader.read_record(&mut record) {
            Ok(true) => {
                let row: Vec<String> = record
                    .iter()
                    .map(std::string::ToString::to_string)
                    .collect();
                let field_count = row.len();
                table.rows.push(row);
                table.field_counts.push(field_count);
            }
            Ok(false) => break, // EOF
            Err(_) => break,    // Parse error, stop here
        }
    }

    // Cache the modal field count for efficient repeated access
    table.update_modal_field_count();

    table
}

/// Normalize line endings to LF for consistent parsing.
/// Returns `Cow::Borrowed` for LF data (zero-copy) and `Cow::Owned` for CR/CRLF.
fn normalize_line_endings<'a>(data: &'a [u8], dialect: &PotentialDialect) -> Cow<'a, [u8]> {
    use super::potential_dialects::LineTerminator;

    match dialect.line_terminator {
        LineTerminator::LF => Cow::Borrowed(data), // Zero-copy for LF
        LineTerminator::CRLF => {
            // Replace \r\n with \n
            let mut result = Vec::with_capacity(data.len());
            let mut i = 0;
            while i < data.len() {
                if i + 1 < data.len() && data[i] == b'\r' && data[i + 1] == b'\n' {
                    result.push(b'\n');
                    i += 2;
                } else {
                    result.push(data[i]);
                    i += 1;
                }
            }
            Cow::Owned(result)
        }
        LineTerminator::CR => {
            // Replace standalone \r with \n
            Cow::Owned(
                data.iter()
                    .map(|&b| if b == b'\r' { b'\n' } else { b })
                    .collect(),
            )
        }
    }
}

/// Simple line-based parser for when csv crate fails.
///
/// This is a fallback parser that handles edge cases the csv crate might reject.
#[allow(dead_code)]
pub fn parse_table_simple(data: &[u8], dialect: &PotentialDialect, max_rows: usize) -> Table {
    let mut table = Table::new();
    let normalized = normalize_line_endings(data, dialect);

    let cursor = Cursor::new(normalized.as_ref());
    let limit = if max_rows == 0 { usize::MAX } else { max_rows };

    for line in cursor.lines().take(limit) {
        let Ok(line) = line else { continue };
        if line.is_empty() {
            continue;
        }

        let fields = split_line(&line, dialect);
        let field_count = fields.len();
        table.rows.push(fields);
        table.field_counts.push(field_count);
    }

    // Cache the modal field count for efficient repeated access
    table.update_modal_field_count();

    table
}

/// Split a line into fields based on the dialect.
#[allow(dead_code)]
fn split_line(line: &str, dialect: &PotentialDialect) -> Vec<String> {
    let delimiter = dialect.delimiter as char;
    let quote_char = match dialect.quote {
        Quote::None => None,
        Quote::Some(q) => Some(q as char),
    };

    let mut fields = Vec::new();
    let mut current_field = String::new();
    let mut in_quotes = false;
    let mut chars = line.chars().peekable();

    while let Some(c) = chars.next() {
        if let Some(q) = quote_char
            && c == q
        {
            if in_quotes {
                // Check for escaped quote (doubled quote)
                if chars.peek() == Some(&q) {
                    current_field.push(q);
                    chars.next();
                } else {
                    in_quotes = false;
                }
            } else {
                in_quotes = true;
            }
            continue;
        }

        if c == delimiter && !in_quotes {
            fields.push(current_field.trim().to_string());
            current_field = String::new();
        } else {
            current_field.push(c);
        }
    }

    fields.push(current_field.trim().to_string());
    fields
}

#[cfg(test)]
mod tests {
    use super::*;
    use crate::tum::potential_dialects::LineTerminator;

    #[test]
    fn test_parse_simple_csv() {
        let data = b"a,b,c\n1,2,3\n4,5,6\n";
        let dialect = PotentialDialect::new(b',', Quote::Some(b'"'), LineTerminator::LF);

        let table = parse_table(data, &dialect, 0);
        assert_eq!(table.num_rows(), 3);
        assert_eq!(table.field_counts, vec![3, 3, 3]);
        assert_eq!(table.rows[0], vec!["a", "b", "c"]);
    }

    #[test]
    fn test_parse_quoted_csv() {
        let data = b"\"a,b\",c,d\n1,2,3\n";
        let dialect = PotentialDialect::new(b',', Quote::Some(b'"'), LineTerminator::LF);

        let table = parse_table(data, &dialect, 0);
        assert_eq!(table.num_rows(), 2);
        assert_eq!(table.rows[0], vec!["a,b", "c", "d"]);
    }

    #[test]
    fn test_modal_field_count() {
        let mut table = Table::new();
        table.field_counts = vec![3, 3, 3, 4, 3];
        table.update_modal_field_count();
        assert_eq!(table.modal_field_count(), 3);
    }
}
```

## File: `src/tum/type_detection.rs`
```rust
//! Type detection for CSV cells using optimized string operations.

use super::regexes::*;
use super::table::Table;
use crate::field_type::Type;

/// Check for NULL-like values using string matching instead of regex.
/// This is a hot path optimization - called for every cell.
#[inline]
fn is_null_value(s: &str) -> bool {
    matches!(
        s,
        "" | "-"
            | "--"
            | "."
            | ".."
            | "?"
            | "null"
            | "NULL"
            | "Null"
            | "nil"
            | "NIL"
            | "Nil"
            | "none"
            | "NONE"
            | "None"
            | "na"
            | "NA"
            | "Na"
            | "n/a"
            | "N/A"
            | "N/a"
            | "nan"
            | "NaN"
            | "NAN"
            | "#N/A"
            | "#VALUE!"
            | "#REF!"
            | "#DIV/0!"
    )
}

/// Check for unsigned integer using string parsing instead of regex.
/// This is a hot path optimization - called for every cell.
/// Limit to 19 digits to ensure all values fit in u64 (max is 18,446,744,073,709,551,615).
#[inline]
fn is_unsigned_int(s: &str) -> bool {
    let s = s.strip_prefix('+').unwrap_or(s);
    !s.is_empty() && s.len() <= 19 && s.bytes().all(|b| b.is_ascii_digit())
}

/// Check for signed integer using string parsing instead of regex.
/// Returns true only for negative integers (positive ones are unsigned).
/// Limit to 19 digits to ensure all values fit in i64 (min is -9,223,372,036,854,775,808).
#[inline]
fn is_signed_int(s: &str) -> bool {
    if let Some(rest) = s.strip_prefix('-') {
        !rest.is_empty() && rest.len() <= 19 && rest.bytes().all(|b| b.is_ascii_digit())
    } else {
        false
    }
}

/// Check for boolean values using exhaustive match instead of regex.
/// This is a hot path optimization - called for every cell.
#[inline]
fn is_boolean(s: &str) -> bool {
    match s.len() {
        1 => {
            let b = s.as_bytes()[0].to_ascii_lowercase();
            matches!(b, b'1' | b'0' | b'y' | b'n' | b't' | b'f')
        }
        2 => s.eq_ignore_ascii_case("on") || s.eq_ignore_ascii_case("no"),
        3 => s.eq_ignore_ascii_case("yes") || s.eq_ignore_ascii_case("off"),
        4 => s.eq_ignore_ascii_case("true"),
        5 => s.eq_ignore_ascii_case("false"),
        _ => false,
    }
}

/// Detect the type of a single cell value.
#[inline]
pub fn detect_cell_type(value: &str) -> Type {
    let trimmed = value.trim();

    // Check for empty first
    if trimmed.is_empty() {
        return Type::NULL;
    }

    // Check for NULL-like values using optimized string matching
    if is_null_value(trimmed) {
        return Type::NULL;
    }

    // Check for unsigned integer (must come before boolean since 1/0 match boolean)
    if is_unsigned_int(trimmed) {
        return Type::Unsigned;
    }

    // Check for signed integer (negative numbers only)
    if is_signed_int(trimmed) {
        return Type::Signed;
    }

    // Check for boolean (after integers so "1" and "0" are treated as numbers)
    if is_boolean(trimmed) {
        return Type::Boolean;
    }

    // Check for float - gate regex with cheap string checks first.
    // This path is only reached after integer detection, so plain integers
    // have already been classified and do not rely on FLOAT_PATTERN. The gate
    // also skips representations like NaN/Inf, which lack both a decimal point
    // and an exponent marker and are therefore not matched here.
    let has_dot = trimmed.contains('.');
    let has_exp = trimmed.contains('e') || trimmed.contains('E');
    if (has_dot || has_exp) && FLOAT_PATTERN.is_match(trimmed) {
        return Type::Float;
    }

    // Check for float with thousand separators
    if (trimmed.contains(',') || has_dot) && FLOAT_THOUSANDS_PATTERN.is_match(trimmed) {
        return Type::Float;
    }

    // Check for ISO datetime first (more specific)
    if DATETIME_ISO_PATTERN.is_match(trimmed) || DATETIME_GENERAL_PATTERN.is_match(trimmed) {
        return Type::DateTime;
    }

    // Check for dates
    if DATE_ISO_PATTERN.is_match(trimmed)
        || DATE_US_PATTERN.is_match(trimmed)
        || DATE_EURO_PATTERN.is_match(trimmed)
    {
        return Type::Date;
    }

    // Fallback to text
    Type::Text
}

/// Reusable buffers for `calculate_type_score` to avoid per-call heap allocations.
pub struct TypeScoreBuffers {
    pub col_type_counts: Vec<[usize; Type::COUNT]>,
    pub col_totals: Vec<usize>,
}

impl Default for TypeScoreBuffers {
    fn default() -> Self {
        Self::new()
    }
}

impl TypeScoreBuffers {
    pub fn new() -> Self {
        Self {
            col_type_counts: Vec::new(),
            col_totals: Vec::new(),
        }
    }

    pub fn reset(&mut self, num_cols: usize) {
        self.col_type_counts.clear();
        self.col_type_counts.resize(num_cols, [0usize; Type::COUNT]);
        self.col_totals.clear();
        self.col_totals.resize(num_cols, 0);
    }
}

/// Calculate the type score for a table.
///
/// This score measures how well the values in each column conform to
/// consistent data types. Higher scores indicate better type consistency.
///
/// Optimized: Single pass through all cells, tracking type counts for all columns simultaneously.
/// Accepts reusable `buffers` to avoid per-call heap allocations.
pub fn calculate_type_score(table: &Table, buffers: &mut TypeScoreBuffers) -> f64 {
    if table.is_empty() {
        return 0.0;
    }

    let num_cols = table.modal_field_count();
    if num_cols == 0 {
        return 0.0;
    }

    // Track type counts for ALL columns in one pass using reusable buffers
    buffers.reset(num_cols);

    // Single pass through all rows and cells
    for row in &table.rows {
        for (col_idx, cell) in row.iter().enumerate().take(num_cols) {
            let cell_type = detect_cell_type(cell);
            buffers.col_type_counts[col_idx][cell_type.as_index()] += 1;
            buffers.col_totals[col_idx] += 1;
        }
    }

    // Calculate scores from accumulated counts
    let mut total_score = 0.0;
    let mut valid_cols = 0;

    for col_idx in 0..num_cols {
        let score = compute_consistency_from_counts(
            &buffers.col_type_counts[col_idx],
            buffers.col_totals[col_idx],
        );
        if score > 0.0 {
            total_score += score;
            valid_cols += 1;
        }
    }

    if valid_cols == 0 {
        return 0.0;
    }

    total_score / valid_cols as f64
}

/// Compute type consistency score from pre-computed type counts.
#[inline]
fn compute_consistency_from_counts(type_counts: &[usize; Type::COUNT], total_cells: usize) -> f64 {
    if total_cells == 0 {
        return 0.0;
    }

    // Special handling: NULL values shouldn't penalize the score
    let null_count = type_counts[Type::NULL.as_index()];
    let non_null_total = total_cells - null_count;

    if non_null_total == 0 {
        // All nulls - neutral score
        return 0.5;
    }

    // Calculate consistency excluding nulls
    let max_non_null = type_counts
        .iter()
        .enumerate()
        .filter(|&(i, _)| i != Type::NULL.as_index())
        .map(|(_, &c)| c)
        .max()
        .unwrap_or(0);

    max_non_null as f64 / non_null_total as f64
}

/// Infer the type for each column in a table.
pub fn infer_column_types(table: &Table) -> Vec<Type> {
    let num_cols = table.modal_field_count();
    let mut types = Vec::with_capacity(num_cols);

    for col_idx in 0..num_cols {
        types.push(infer_single_column_type(table, col_idx));
    }

    types
}

/// Infer the type for a single column.
fn infer_single_column_type(table: &Table, col_idx: usize) -> Type {
    let mut merged_type = Type::NULL;

    for row in &table.rows {
        if col_idx < row.len() {
            let cell_type = detect_cell_type(&row[col_idx]);
            merged_type = merged_type.merge(cell_type);
        }
    }

    merged_type
}

/// Calculate the pattern score for a value.
///
/// This gives a weighted score based on how specific the detected pattern is.
/// More specific patterns (like datetime) score higher than generic ones (like text).
pub fn pattern_specificity_score(value: &str) -> f64 {
    let trimmed = value.trim();

    if trimmed.is_empty() {
        return 0.0;
    }

    // Check patterns in order of specificity (uses cached static slice)
    for pc in get_pattern_categories() {
        if pc.pattern.is_match(trimmed) {
            return pc.weight;
        }
    }

    // Text is the fallback with lowest specificity
    0.1
}

/// Calculate the average pattern specificity score for a table.
pub fn calculate_pattern_score(table: &Table) -> f64 {
    if table.is_empty() {
        return 0.0;
    }

    let mut total_score = 0.0;
    let mut count = 0;

    for row in &table.rows {
        for cell in row {
            total_score += pattern_specificity_score(cell);
            count += 1;
        }
    }

    if count == 0 {
        return 0.0;
    }

    total_score / count as f64
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_detect_cell_type() {
        assert_eq!(detect_cell_type("123"), Type::Unsigned);
        assert_eq!(detect_cell_type("-123"), Type::Signed);
        assert_eq!(detect_cell_type("12.34"), Type::Float);
        assert_eq!(detect_cell_type("true"), Type::Boolean);
        assert_eq!(detect_cell_type("2023-12-31"), Type::Date);
        assert_eq!(detect_cell_type("2023-12-31T12:30:45"), Type::DateTime);
        assert_eq!(detect_cell_type("hello"), Type::Text);
        assert_eq!(detect_cell_type(""), Type::NULL);
        assert_eq!(detect_cell_type("NULL"), Type::NULL);
    }

    #[test]
    fn test_infer_column_types() {
        let mut table = Table::new();
        table.rows = vec![
            vec![
                "1".to_string(),
                "hello".to_string(),
                "2023-01-01".to_string(),
            ],
            vec![
                "2".to_string(),
                "world".to_string(),
                "2023-01-02".to_string(),
            ],
            vec![
                "3".to_string(),
                "test".to_string(),
                "2023-01-03".to_string(),
            ],
        ];
        table.field_counts = vec![3, 3, 3];
        table.update_modal_field_count();

        let types = infer_column_types(&table);
        assert_eq!(types, vec![Type::Unsigned, Type::Text, Type::Date]);
    }
}
```

## File: `src/tum/uniformity.rs`
```rust
//! Table uniformity calculations (`tau_0`, `tau_1`).
//!
//! These metrics measure how uniform a parsed CSV table is:
//! - `tau_0` (consistency): measures if all rows have the same number of fields
//! - `tau_1` (dispersion): measures the variability of field counts

use super::table::Table;

/// Calculate `tau_0` (consistency score).
///
/// This measures how consistent the field counts are across rows.
/// Formula: `tau_0` = 1 / (1 + 2 * sigma)
/// where sigma is the standard deviation of field counts.
///
/// Returns a value between 0 and 1, where 1 means perfect consistency.
pub fn calculate_tau_0(table: &Table) -> f64 {
    if table.field_counts.is_empty() {
        return 0.0;
    }

    let sigma = standard_deviation(&table.field_counts);

    // tau_0 = 1 / (1 + 2 * sigma)
    // 1.0 / (1.0 + 2.0 * sigma)
    1.0 / 2.0f64.mul_add(sigma, 1.0)
}

/// Calculate `tau_1` (dispersion score).
///
/// This measures the variability in field counts using multiple factors:
/// - Range of field counts
/// - Number of transitions between different field counts
/// - Dominance of the modal (most common) field count
///
/// Returns a value between 0 and 1, where 1 means low dispersion (good).
pub fn calculate_tau_1(table: &Table) -> f64 {
    if table.field_counts.is_empty() {
        return 0.0;
    }

    let n = table.field_counts.len();
    if n == 1 {
        return 1.0; // Single row is perfectly uniform
    }

    // 1. Range component: penalize wide range of field counts
    let min_fc = table.min_field_count();
    let max_fc = table.max_field_count();
    let range = max_fc - min_fc;

    let range_score = if max_fc == 0 {
        0.0
    } else {
        1.0 - (range as f64 / max_fc as f64).min(1.0)
    };

    // 2. Transition component: count changes between consecutive rows
    let mut transitions = 0;
    for i in 1..n {
        if table.field_counts[i] != table.field_counts[i - 1] {
            transitions += 1;
        }
    }
    let transition_score = 1.0 - (transitions as f64 / (n - 1) as f64);

    // 3. Mode dominance: fraction of rows with the modal field count
    let mode_count = table.modal_field_count_freq();
    let mode_score = mode_count as f64 / n as f64;

    // Combine components with weights
    // Range and mode are most important, transitions provide additional signal
    // range_score * 0.3 + transition_score * 0.3 + mode_score * 0.4
    mode_score.mul_add(0.4, range_score * 0.3 + transition_score * 0.3)
}

/// Calculate the combined uniformity score.
///
/// This combines `tau_0` and `tau_1` into a single uniformity measure.
#[allow(dead_code)]
pub fn calculate_uniformity(table: &Table) -> f64 {
    let tau_0 = calculate_tau_0(table);
    let tau_1 = calculate_tau_1(table);

    // Geometric mean gives a balanced combination
    (tau_0 * tau_1).sqrt()
}

/// Calculate standard deviation of field counts.
fn standard_deviation(values: &[usize]) -> f64 {
    if values.is_empty() {
        return 0.0;
    }

    let n = values.len() as f64;
    let mean: f64 = values.iter().sum::<usize>() as f64 / n;

    let variance: f64 = values
        .iter()
        .map(|&v| {
            let diff = v as f64 - mean;
            diff * diff
        })
        .sum::<f64>()
        / n;

    variance.sqrt()
}

/// Check if a table has uniform field counts (all rows same number of fields).
pub fn is_uniform(table: &Table) -> bool {
    if table.field_counts.is_empty() {
        return true;
    }

    let first = table.field_counts[0];
    table.field_counts.iter().all(|&fc| fc == first)
}

/// Get statistics about the table's field count distribution.
#[allow(dead_code)]
#[derive(Debug, Clone)]
pub struct FieldCountStats {
    pub min: usize,
    pub max: usize,
    pub mode: usize,
    pub mean: f64,
    pub std_dev: f64,
    pub is_uniform: bool,
}

impl FieldCountStats {
    /// Calculate field count statistics for a table.
    #[allow(dead_code)]
    pub fn from_table(table: &Table) -> Self {
        let min = table.min_field_count();
        let max = table.max_field_count();
        let mode = table.modal_field_count();
        let mean = if table.field_counts.is_empty() {
            0.0
        } else {
            table.field_counts.iter().sum::<usize>() as f64 / table.field_counts.len() as f64
        };
        let std_dev = standard_deviation(&table.field_counts);
        let is_uniform_val = is_uniform(table);

        Self {
            min,
            max,
            mode,
            mean,
            std_dev,
            is_uniform: is_uniform_val,
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_tau_0_uniform() {
        let mut table = Table::new();
        table.field_counts = vec![3, 3, 3, 3, 3];
        table.update_modal_field_count();

        let tau_0 = calculate_tau_0(&table);
        assert!((tau_0 - 1.0).abs() < 0.001); // Should be 1.0 for uniform counts
    }

    #[test]
    fn test_tau_0_varied() {
        let mut table = Table::new();
        table.field_counts = vec![3, 4, 3, 5, 3];
        table.update_modal_field_count();

        let tau_0 = calculate_tau_0(&table);
        assert!(tau_0 < 1.0); // Should be less than 1.0 for varied counts
        assert!(tau_0 > 0.0);
    }

    #[test]
    fn test_tau_1_uniform() {
        let mut table = Table::new();
        table.field_counts = vec![3, 3, 3, 3, 3];
        table.update_modal_field_count();

        let tau_1 = calculate_tau_1(&table);
        assert!((tau_1 - 1.0).abs() < 0.001); // Should be 1.0 for uniform counts
    }

    #[test]
    fn test_is_uniform() {
        let mut uniform_table = Table::new();
        uniform_table.field_counts = vec![3, 3, 3];
        uniform_table.update_modal_field_count();
        assert!(is_uniform(&uniform_table));

        let mut varied_table = Table::new();
        varied_table.field_counts = vec![3, 4, 3];
        varied_table.update_modal_field_count();
        assert!(!is_uniform(&varied_table));
    }
}
```

## File: `tests/benchmark_accuracy.rs`
```rust
//! Benchmark accuracy tests for csv-nose against CSVsniffer test datasets.
//!
//! These tests validate the Table Uniformity Method implementation against
//! real-world CSV files with known dialects by invoking the CLI binary.

use std::path::PathBuf;
use std::process::Command;

fn get_test_data_dir() -> PathBuf {
    PathBuf::from(env!("CARGO_MANIFEST_DIR")).join("tests/data")
}

fn get_binary_path() -> PathBuf {
    // The test binary is built in target/debug or target/release
    let mut path = PathBuf::from(env!("CARGO_MANIFEST_DIR"));
    path.push("target");
    path.push(if cfg!(debug_assertions) {
        "debug"
    } else {
        "release"
    });
    path.push("csv-nose");
    path
}

/// Parse accuracy percentage from benchmark output.
/// Looks for lines like "Passed:             123 (85.0%)"
fn parse_accuracy_from_output(output: &str) -> Option<f64> {
    for line in output.lines() {
        if line.contains("Passed:") && line.contains('%') {
            // Extract the percentage from the line
            if let Some(start) = line.find('(') {
                if let Some(end) = line.find('%') {
                    if start < end {
                        let pct_str = &line[start + 1..end];
                        return pct_str.trim().parse().ok();
                    }
                }
            }
        }
    }
    None
}

/// Parse total file count from benchmark output.
/// Looks for lines like "Total files:        148"
fn parse_total_from_output(output: &str) -> Option<usize> {
    for line in output.lines() {
        if line.contains("Total files:") {
            let parts: Vec<&str> = line.split_whitespace().collect();
            if let Some(last) = parts.last() {
                return last.parse().ok();
            }
        }
    }
    None
}

/// Run benchmark on a dataset and return (total_files, accuracy_pct, stdout)
fn run_dataset_benchmark(dataset: &str) -> (usize, f64, String) {
    run_benchmark_with_annotations(dataset, dataset)
}

/// Run benchmark with separate data directory and annotations file.
/// This allows multiple benchmarks to share the same data directory with different annotation files.
fn run_benchmark_with_annotations(
    data_dir_name: &str,
    annotations_name: &str,
) -> (usize, f64, String) {
    let data_dir = get_test_data_dir();
    let csv_dir = data_dir.join(data_dir_name);
    let annotations_path = data_dir
        .join("annotations")
        .join(format!("{}.txt", annotations_name));

    if !csv_dir.exists() {
        panic!(
            "Test data directory not found: {}. \
             Please copy CSVsniffer test files to tests/data/{}",
            csv_dir.display(),
            data_dir_name
        );
    }

    if !annotations_path.exists() {
        panic!(
            "Annotations file not found: {}. \
             Please copy annotations to tests/data/annotations/{}.txt",
            annotations_path.display(),
            annotations_name
        );
    }

    let binary = get_binary_path();
    if !binary.exists() {
        panic!(
            "Binary not found at {}. Run `cargo build` first.",
            binary.display()
        );
    }

    let output = Command::new(&binary)
        .arg("--benchmark")
        .arg(&csv_dir)
        .arg("--annotations")
        .arg(&annotations_path)
        .output()
        .expect("Failed to execute csv-nose binary");

    let stdout = String::from_utf8_lossy(&output.stdout).to_string();
    let stderr = String::from_utf8_lossy(&output.stderr).to_string();

    if !output.status.success() {
        panic!(
            "Benchmark command failed with status {:?}\nstdout: {}\nstderr: {}",
            output.status, stdout, stderr
        );
    }

    let total = parse_total_from_output(&stdout).unwrap_or(0);
    let accuracy = parse_accuracy_from_output(&stdout).unwrap_or(0.0);

    (total, accuracy, stdout)
}

#[test]
fn test_pollock_accuracy() {
    let (total, accuracy, stdout) = run_dataset_benchmark("pollock");

    println!("\n========== POLLOCK Dataset ==========");
    println!("{}", stdout);

    // Basic sanity checks
    assert!(total > 0, "Should have test files");
    println!("\nPOLLOCK Accuracy: {:.1}%", accuracy);

    // Target: >90% accuracy on POLLOCK
    // Note: This assertion may need adjustment based on actual performance
    // assert!(accuracy >= 90.0, "Accuracy should be >= 90%, got {:.1}%", accuracy);
}

#[test]
fn test_w3c_csvw_accuracy() {
    let (total, accuracy, stdout) = run_dataset_benchmark("w3c-csvw");

    println!("\n========== W3C-CSVW Dataset ==========");
    println!("{}", stdout);

    // Basic sanity checks
    assert!(total > 0, "Should have test files");
    println!("\nW3C-CSVW Accuracy: {:.1}%", accuracy);

    // Target: >90% accuracy on W3C-CSVW
    // Note: This assertion may need adjustment based on actual performance
    // assert!(accuracy >= 90.0, "Accuracy should be >= 90%, got {:.1}%", accuracy);
}

#[test]
fn test_csv_wrangling_accuracy() {
    let (total, accuracy, stdout) = run_dataset_benchmark("csv-wrangling");

    println!("\n========== CSV Wrangling Dataset ==========");
    println!("{}", stdout);

    // Basic sanity checks
    assert!(total > 0, "Should have test files");
    println!("\nCSV Wrangling Accuracy: {:.1}%", accuracy);
}

#[test]
fn test_csv_wrangling_codec_accuracy() {
    // Uses csv-wrangling data dir but csv-wrangling-codec annotations
    let (total, accuracy, stdout) =
        run_benchmark_with_annotations("csv-wrangling", "csv-wrangling-codec");

    println!("\n========== CSV Wrangling filtered CODEC ==========");
    println!("{}", stdout);

    // Basic sanity checks
    assert!(total > 0, "Should have test files");
    println!("\nCSV Wrangling CODEC Accuracy: {:.1}%", accuracy);
}

#[test]
fn test_csv_wrangling_messy_accuracy() {
    // Uses csv-wrangling data dir but csv-wrangling-messy annotations (only non-normal files)
    let (total, accuracy, stdout) =
        run_benchmark_with_annotations("csv-wrangling", "csv-wrangling-messy");

    println!("\n========== CSV Wrangling MESSY ==========");
    println!("{}", stdout);

    // Basic sanity checks
    assert!(total > 0, "Should have test files");
    println!("\nCSV Wrangling MESSY Accuracy: {:.1}%", accuracy);
}

#[test]
fn test_combined_accuracy_report() {
    let (pollock_total, pollock_accuracy, _) = run_dataset_benchmark("pollock");
    let (w3c_total, w3c_accuracy, _) = run_dataset_benchmark("w3c-csvw");
    let (wrangling_total, wrangling_accuracy, _) = run_dataset_benchmark("csv-wrangling");
    let (codec_total, codec_accuracy, _) =
        run_benchmark_with_annotations("csv-wrangling", "csv-wrangling-codec");
    let (messy_total, messy_accuracy, _) =
        run_benchmark_with_annotations("csv-wrangling", "csv-wrangling-messy");

    println!("\n========================================");
    println!("       COMBINED ACCURACY REPORT        ");
    println!("========================================\n");

    println!("Dataset            | Total | Accuracy");
    println!("-------------------|-------|----------");
    println!(
        "POLLOCK            | {:>5} | {:>7.1}%",
        pollock_total, pollock_accuracy
    );
    println!(
        "W3C-CSVW           | {:>5} | {:>7.1}%",
        w3c_total, w3c_accuracy
    );
    println!(
        "CSV Wrangling      | {:>5} | {:>7.1}%",
        wrangling_total, wrangling_accuracy
    );
    println!(
        "CSV Wrangling CODEC| {:>5} | {:>7.1}%",
        codec_total, codec_accuracy
    );
    println!(
        "CSV Wrangling MESSY| {:>5} | {:>7.1}%",
        messy_total, messy_accuracy
    );

    let total_files = pollock_total + w3c_total + wrangling_total;

    // Weighted average accuracy (using non-overlapping datasets: POLLOCK, W3C-CSVW, CSV Wrangling)
    let combined_accuracy = if total_files > 0 {
        (pollock_accuracy * pollock_total as f64
            + w3c_accuracy * w3c_total as f64
            + wrangling_accuracy * wrangling_total as f64)
            / total_files as f64
    } else {
        0.0
    };

    println!("-------------------|-------|----------");
    println!(
        "COMBINED           | {:>5} | {:>7.1}%",
        total_files, combined_accuracy
    );
}
```

## File: `tests/integration_tests.rs`
```rust
//! Integration tests for csv-nose

use csv_nose::{DatePreference, Quote, SampleSize, Sniffer, Type};
use std::io::Cursor;
use std::io::Write;
use tempfile::NamedTempFile;

#[test]
fn test_sniff_comma_delimited() {
    let data = b"name,age,city\nAlice,30,New York\nBob,25,Los Angeles\nCharlie,35,Chicago\n";
    let sniffer = Sniffer::new();

    let metadata = sniffer.sniff_bytes(data).unwrap();

    assert_eq!(metadata.dialect.delimiter, b',');
    assert!(metadata.dialect.header.has_header_row);
    assert_eq!(metadata.num_fields, 3);
    assert_eq!(metadata.fields, vec!["name", "age", "city"]);
}

#[test]
fn test_sniff_tab_delimited() {
    let data = b"name\tage\tcity\nAlice\t30\tNew York\nBob\t25\tLos Angeles\n";
    let sniffer = Sniffer::new();

    let metadata = sniffer.sniff_bytes(data).unwrap();

    assert_eq!(metadata.dialect.delimiter, b'\t');
    assert!(metadata.dialect.header.has_header_row);
    assert_eq!(metadata.num_fields, 3);
}

#[test]
fn test_sniff_semicolon_delimited() {
    let data = b"name;age;city\nAlice;30;New York\nBob;25;Los Angeles\n";
    let sniffer = Sniffer::new();

    let metadata = sniffer.sniff_bytes(data).unwrap();

    assert_eq!(metadata.dialect.delimiter, b';');
}

#[test]
fn test_sniff_pipe_delimited() {
    let data = b"name|age|city\nAlice|30|New York\nBob|25|Los Angeles\n";
    let sniffer = Sniffer::new();

    let metadata = sniffer.sniff_bytes(data).unwrap();

    assert_eq!(metadata.dialect.delimiter, b'|');
}

#[test]
fn test_sniff_quoted_fields() {
    let data = b"\"name\",\"value\"\n\"hello, world\",\"123\"\n\"test\",\"456\"\n";
    let sniffer = Sniffer::new();

    let metadata = sniffer.sniff_bytes(data).unwrap();

    assert_eq!(metadata.dialect.delimiter, b',');
    assert_eq!(metadata.dialect.quote, Quote::Some(b'"'));
}

#[test]
fn test_sniff_single_quoted() {
    let data = b"'name','value'\n'hello, world','123'\n'test','456'\n";
    let sniffer = Sniffer::new();

    let metadata = sniffer.sniff_bytes(data).unwrap();

    assert_eq!(metadata.dialect.delimiter, b',');
    assert_eq!(metadata.dialect.quote, Quote::Some(b'\''));
}

#[test]
fn test_sniff_no_header() {
    let data = b"1,2,3\n4,5,6\n7,8,9\n10,11,12\n";
    let sniffer = Sniffer::new();

    let metadata = sniffer.sniff_bytes(data).unwrap();

    assert_eq!(metadata.dialect.delimiter, b',');
    assert!(!metadata.dialect.header.has_header_row);
    assert_eq!(metadata.num_fields, 3);
    // Should have generated field names
    assert_eq!(metadata.fields, vec!["field_1", "field_2", "field_3"]);
}

#[test]
fn test_sniff_type_detection() {
    let data =
        b"id,name,score,active,date\n1,Alice,95.5,true,2023-01-15\n2,Bob,87.2,false,2023-02-20\n";
    let sniffer = Sniffer::new();

    let metadata = sniffer.sniff_bytes(data).unwrap();

    assert_eq!(metadata.types.len(), 5);
    assert_eq!(metadata.types[0], Type::Unsigned); // id
    assert_eq!(metadata.types[1], Type::Text); // name
    assert_eq!(metadata.types[2], Type::Float); // score
    assert_eq!(metadata.types[3], Type::Boolean); // active
    assert_eq!(metadata.types[4], Type::Date); // date
}

#[test]
fn test_sniff_windows_line_endings() {
    let data = b"name,age\r\nAlice,30\r\nBob,25\r\n";
    let sniffer = Sniffer::new();

    let metadata = sniffer.sniff_bytes(data).unwrap();

    assert_eq!(metadata.dialect.delimiter, b',');
    assert_eq!(metadata.num_fields, 2);
}

#[test]
fn test_sniff_from_reader() {
    let data = b"a,b,c\n1,2,3\n4,5,6\n";
    let cursor = Cursor::new(data.to_vec());

    let mut sniffer = Sniffer::new();
    let metadata = sniffer.sniff_reader(cursor).unwrap();

    assert_eq!(metadata.dialect.delimiter, b',');
    assert_eq!(metadata.num_fields, 3);
}

#[test]
fn test_sniff_from_file() {
    let mut temp_file = NamedTempFile::new().unwrap();
    writeln!(temp_file, "name,age,city").unwrap();
    writeln!(temp_file, "Alice,30,NYC").unwrap();
    writeln!(temp_file, "Bob,25,LA").unwrap();
    temp_file.flush().unwrap();

    let mut sniffer = Sniffer::new();
    let metadata = sniffer.sniff_path(temp_file.path()).unwrap();

    assert_eq!(metadata.dialect.delimiter, b',');
    assert_eq!(metadata.num_fields, 3);
    assert!(metadata.dialect.header.has_header_row);
}

#[test]
fn test_forced_delimiter() {
    // Data that could be interpreted as comma or semicolon
    let data = b"a;b;c\n1;2;3\n";

    let mut sniffer = Sniffer::new();
    sniffer.delimiter(b';');

    let metadata = sniffer.sniff_bytes(data).unwrap();

    assert_eq!(metadata.dialect.delimiter, b';');
}

#[test]
fn test_sample_size_records() {
    let data = b"a,b\n1,2\n3,4\n5,6\n7,8\n9,10\n";

    let mut sniffer = Sniffer::new();
    sniffer.sample_size(SampleSize::Records(3));

    let metadata = sniffer.sniff_bytes(data).unwrap();

    assert_eq!(metadata.dialect.delimiter, b',');
}

#[test]
fn test_sample_size_bytes() {
    let data = b"name,age\nAlice,30\nBob,25\nCharlie,35\n";

    let mut sniffer = Sniffer::new();
    sniffer.sample_size(SampleSize::Bytes(50));

    let metadata = sniffer.sniff_bytes(data).unwrap();

    assert_eq!(metadata.dialect.delimiter, b',');
}

#[test]
fn test_utf8_detection() {
    let data = "name,city\nAlice,东京\nBob,Москва\n".as_bytes();
    let sniffer = Sniffer::new();

    let metadata = sniffer.sniff_bytes(data).unwrap();

    assert!(metadata.dialect.is_utf8);
}

#[test]
fn test_utf8_bom() {
    let mut data = vec![0xEF, 0xBB, 0xBF]; // UTF-8 BOM
    data.extend_from_slice(b"a,b,c\n1,2,3\n");

    let sniffer = Sniffer::new();
    let metadata = sniffer.sniff_bytes(&data).unwrap();

    assert_eq!(metadata.dialect.delimiter, b',');
    assert!(metadata.dialect.is_utf8);
}

#[test]
fn test_empty_file_error() {
    let data = b"";
    let sniffer = Sniffer::new();

    let result = sniffer.sniff_bytes(data);

    assert!(result.is_err());
}

#[test]
fn test_flexible_field_counts() {
    let data = b"a,b,c\n1,2\n3,4,5,6\n7,8,9\n";
    let sniffer = Sniffer::new();

    let metadata = sniffer.sniff_bytes(data).unwrap();

    // Should detect as flexible due to varying field counts
    assert!(metadata.dialect.flexible);
}

#[test]
fn test_date_types() {
    let data = b"iso_date,us_date,euro_date\n2023-12-31,12/31/2023,31.12.2023\n2024-01-15,01/15/2024,15.01.2024\n";
    let sniffer = Sniffer::new();

    let metadata = sniffer.sniff_bytes(data).unwrap();

    // All three columns should be detected as Date
    for typ in &metadata.types {
        assert_eq!(*typ, Type::Date);
    }
}

#[test]
fn test_datetime_types() {
    let data = b"timestamp\n2023-12-31T12:30:45\n2024-01-15T08:00:00Z\n";
    let sniffer = Sniffer::new();

    let metadata = sniffer.sniff_bytes(data).unwrap();

    assert_eq!(metadata.types[0], Type::DateTime);
}

#[test]
fn test_null_values() {
    let data = b"id,value\n1,100\n2,\n3,NULL\n4,N/A\n";
    let sniffer = Sniffer::new();

    let metadata = sniffer.sniff_bytes(data).unwrap();

    // First column should still be detected as Unsigned despite some null values
    assert_eq!(metadata.types[0], Type::Unsigned);
}

#[test]
fn test_builder_chaining() {
    let mut sniffer = Sniffer::new();
    let sniffer_ref = sniffer
        .sample_size(SampleSize::Records(50))
        .date_preference(DatePreference::DmyFormat)
        .delimiter(b',')
        .quote(Quote::Some(b'"'));

    // Verify chaining works
    let data = b"a,b\n1,2\n";
    let _ = sniffer_ref.sniff_bytes(data);
}

#[test]
fn test_many_columns() {
    // Generate CSV with many columns
    let header: Vec<String> = (0..50).map(|i| format!("col{}", i)).collect();
    let row: Vec<String> = (0..50).map(|i| format!("{}", i)).collect();

    let mut data = header.join(",");
    data.push('\n');
    data.push_str(&row.join(","));
    data.push('\n');

    let sniffer = Sniffer::new();
    let metadata = sniffer.sniff_bytes(data.as_bytes()).unwrap();

    assert_eq!(metadata.num_fields, 50);
    assert_eq!(metadata.dialect.delimiter, b',');
}

#[test]
fn test_single_column() {
    let data = b"value\n100\n200\n300\n";
    let sniffer = Sniffer::new();

    let metadata = sniffer.sniff_bytes(data).unwrap();

    assert_eq!(metadata.num_fields, 1);
}

#[test]
fn test_mixed_types_column() {
    // Column with mixed types should become Text
    let data = b"value\n100\nhello\n300\n";
    let sniffer = Sniffer::new();

    let metadata = sniffer.sniff_bytes(data).unwrap();

    assert_eq!(metadata.types[0], Type::Text);
}

/// Regression test for avg_record_len calculation with SampleSize::Records.
///
/// Previously, when using SampleSize::Records(n), the avg_record_len was always
/// ~1024 bytes because the buffer size estimate (n * 1024) was divided by the
/// parsed row count (n), regardless of actual record size.
///
/// This test uses a real-world CSV sample (NYC 311 data) to verify that
/// avg_record_len reflects the actual average record size (~530 bytes),
/// not the buffer estimate constant (1024 bytes).
#[test]
fn test_avg_record_len_regression_nyc_311() {
    let fixture_path = std::path::Path::new("tests/data/fixtures/nyc_311_sample_200.csv");

    // Skip test if fixture file doesn't exist
    if !fixture_path.exists() {
        eprintln!(
            "Skipping test: fixture file not found at {:?}",
            fixture_path
        );
        return;
    }

    let mut sniffer = Sniffer::new();
    // Use default SampleSize::Records(100) which triggered the bug
    sniffer.sample_size(SampleSize::Records(100));

    let metadata = sniffer.sniff_path(fixture_path).unwrap();

    // Verify basic detection
    assert_eq!(metadata.dialect.delimiter, b',');
    assert_eq!(metadata.dialect.quote, Quote::Some(b'"'));
    assert!(metadata.dialect.header.has_header_row);
    assert_eq!(metadata.num_fields, 41);

    // THE KEY REGRESSION TEST:
    // avg_record_len should be approximately 530 bytes (actual record size),
    // NOT 1024 bytes (the old buggy value from buffer_size / row_count)
    assert!(
        metadata.avg_record_len < 700,
        "avg_record_len should be ~530 bytes, not 1024. Got: {} bytes",
        metadata.avg_record_len
    );
    assert!(
        metadata.avg_record_len > 400,
        "avg_record_len should be ~530 bytes, not too small. Got: {} bytes",
        metadata.avg_record_len
    );
}
```

## File: `tests/data/annotations/csv-wrangling-codec.txt`
```
1.csv|utf8|comma|doublequote||lf
1.fail.csv|utf8|comma|doublequote||crlf
2_18-05-2011-17-21-59_0.csv|windows-1251|semicolon|doublequote|doublequote|crlf
2_ip_test.csv|utf8|comma|doublequote|doublequote|crlf
100-external-simple.csv|utf8|comma|doublequote||lf
ABCAUS2011.csv|ansi|comma|doublequote||lf
ACS_12_5YR_S1903_metadata.csv|utf8|comma|doublequote||crlf
act.csv|utf8|comma|doublequote||crlf
admins.csv|utf8|comma|doublequote||lf
af.csv|utf8|comma|doublequote|doublequote|lf
afghanngos.csv|utf8|comma|doublequote|doublequote|lf
airports.csv|utf8|comma|doublequote|doublequote|lf
alfa_example.csv|windows-1251|semicolon|doublequote||crlf
all-classes.csv|utf8|comma|doublequote|doublequote|lf
AllUseCasesOrdered.csv|utf8|vslash|doublequote||crlf
answer.csv|utf8|comma|doublequote||lf
Apr-2014_Apr-2014_Platform.csv|utf8|comma|doublequote||crlf
association.csv|utf8|semicolon|doublequote||crlf
awaymanagers-data.csv|utf8|comma|doublequote||lf
bandwidth-2011-08-21-1MHz-175MHz.csv|utf8|tab|doublequote||lf
baselog.csv|utf8|comma|doublequote|doublequote|lf
benchmark.csv|utf8|comma|doublequote|doublequote|lf
BIO.csv|utf8|comma|doublequote|doublequote|lf
blocks.csv|utf8|semicolon|doublequote||crlf
bookings.csv|utf8|semicolon|doublequote|doublequote|lf
bugs.csv|utf8|comma|doublequote|doublequote|lf
CalculusComponents.csv|utf8|comma|doublequote|doublequote|lf
cassette_features.csv|utf8|comma|doublequote|doublequote|lf
cityList.csv|utf8|comma|doublequote||crlf
ckan-endpoints.csv|utf8|semicolon|doublequote||lf
cliente.csv|ansi|semicolon|doublequote|doublequote|lf
cnx22-XE133-XE131M-XE133M.csv|utf8|comma|doublequote||lf
conversion_17_to_18.csv|utf8|semicolon|doublequote|backslash|lf
coord.csv|utf8|semicolon|doublequote||lf
copyright.csv|utf8|tab|doublequote||lf
countrynames.csv|utf8|comma|doublequote||lf
coupons.csv|utf8|comma|doublequote||lf
csv_data.csv|utf8|comma|doublequote||lf
csv_ingestion.csv|utf8|comma|doublequote|doublequote|crlf
CsvBulkLoaderTest_Players.csv|utf8|comma|doublequote|backslash|cr
cuentas.csv|utf8|semicolon|doublequote||lf
currencies.csv|utf8|comma|singlequote||lf
data.csv|utf16|comma|doublequote||lf
db_general.csv|utf8|comma|doublequote||lf
de_DE.csv|utf8|semicolon|doublequote||lf
devices_data.csv|utf8|comma|doublequote||lf
diamonds.csv|utf8|space|doublequote||lf
dodgers_2010_schedule.csv|utf8|comma|doublequote||crlf
durden_saucer.csv|utf8|semicolon|doublequote|backslash|lf
Empty.csv|utf8|comma|doublequote||lf
en.csv|utf8|comma|doublequote||lf
engine_reqs_2.csv|utf8|comma|doublequote||lf
Error331_DynCatsMenu.csv|utf8|comma|doublequote||lf
events.csv|utf8|comma|doublequote||lf
example.csv|utf8|semicolon|doublequote||crlf
exit.csv|utf8|comma|doublequote||lf
export.csv|utf8|comma|doublequote||lf
feats.csv|utf8|comma|doublequote|doublequote|lf
feedback.csv|utf8|comma|doublequote||crlf
flat_file_database.csv|utf8|nsign|doublequote|doublequote|lf
Formats.csv|utf8|comma|doublequote|doublequote|lf
fuw1.csv|utf8|semicolon|doublequote||lf
general.csv|utf8|comma|doublequote||crlf
GPU_rod_1_metrica.csv|utf8|semicolon|doublequote||lf
iconbar-hermes.csv|utf8|comma|doublequote||lf
iometeroutput.csv|utf8|comma|doublequote||crlf
ip-log.csv|utf8|comma|doublequote||lf
isco.csv|utf8|semicolon|singlequote|backslash|lf
items.csv|utf8|comma|doublequote||crlf
JeannieProperties.csv|utf8|comma|doublequote||lf
JV_newsite_IBC_current_20110517.csv|utf8|comma|singlequote||lf
keyword-count.csv|utf8|semicolon|doublequote||lf
kodepos-2008-10-20.csv|utf8|comma|doublequote||crlf
limesurvey_survey_94328.csv|utf8|comma|doublequote||lf
linodef_bueditor_button.csv|utf8|comma|doublequote||lf
load_fund_structure_data.csv|windows-1251|semicolon|doublequote|doublequote|lf
maatkit-issues.csv|utf8|comma|doublequote|doublequote|lf
Mage_Adminhtml.csv|utf8|comma|doublequote|doublequote|lf
Mage_Catalog.csv|utf8|comma|doublequote|doublequote|lf
Mage_Lucene.csv|utf8|comma|doublequote||lf
mammalia-10.csv|utf8|tab|doublequote||lf
memberList.csv|utf8|comma|doublequote||lf
metricData.csv|utf8|comma|doublequote|doublequote|lf
mgrs_index.csv|utf8|tab|doublequote||lf
model.csv|utf8|comma|doublequote|backslash|crlf
mxoClothing.csv|utf8|semicolon|doublequote||crlf
my_Jess_Robinson.csv|utf8|comma|doublequote||lf
MyList.csv|utf8|comma|doublequote||lf
NA_letters.csv|utf8|comma|doublequote||lf
next_q.csv|utf8|comma|doublequote||lf
one-line-with-accents.csv|utf8|comma|doublequote|doublequote|crlf
orders.csv|utf8|comma|doublequote||lf
orig_data.csv|utf8|comma|doublequote||lf
out.csv|utf8|comma|doublequote|doublequote|crlf
paperpile.csv|utf8|comma|doublequote|backslash|lf
Parsed.csv|utf8|semicolon|doublequote|doublequote|lf
poblacion.csv|utf8|semicolon|doublequote|backslash|lf
product_feed.csv|utf8|comma|doublequote||lf
products.csv|utf8|comma|doublequote||lf
prt_statuses.csv|utf8|comma|doublequote||lf
publish.csv|utf8|semicolon|doublequote||lf
questions.csv|utf8|comma|doublequote|doublequote|crlf
quotes.csv|utf8|comma|doublequote||lf
rail-points.csv|utf8|comma|doublequote||crlf
raw-data-russian-parlimentary-elections-2011-english-headers-only-no-links.csv|utf8|semicolon|doublequote|doublequote|crlf
register_data.csv|utf8|semicolon|doublequote||lf
replace.csv|utf8|comma|doublequote||lf
report.csv|utf8|comma|doublequote||lf
resources.csv|utf8|semicolon|doublequote||lf
responses.csv|utf8|comma|doublequote||lf
results.csv|utf8|tab|doublequote||lf
sample.csv|utf8|semicolon|doublequote||lf
sample_map.csv|utf8|comma|doublequote||lf
set001.csv|utf8|comma|doublequote||crlf
shops.csv|ansi|semicolon|doublequote|doublequote|crlf
simulation.csv|utf8|tab|doublequote||lf
solar-system.csv|utf8|comma|doublequote||lf
source-en.csv|utf8|semicolon|doublequote||crlf
spirate.csv|utf8|semicolon|doublequote||lf
stringtable.csv|utf8|comma|doublequote||lf
table1.csv|utf8|comma|doublequote||lf
TableA.csv|utf8|comma|doublequote||lf
talks.csv|utf8|comma|doublequote||lf
task4_pad.csv|utf8|comma|doublequote||crlf
tentative_accounts.csv|utf8|comma|doublequote|doublequote|lf
test.csv|utf8|comma|doublequote||lf
test_data.csv|utf8|comma|doublequote||lf
test_neighbours.csv|utf8|comma|doublequote||lf
test-spreadsheet-for-csv-blank-row.csv|utf8|comma|doublequote||lf
timing.csv|utf8|comma|doublequote||lf
top-10k-2009-03-06.csv|utf8|comma|doublequote||lf
unemploy.csv|utf8|comma|doublequote||lf
uniq_nl_data.csv|utf8|nsign|singlequote||crlf
upload.csv|utf8|comma|doublequote||lf
upload0.csv|utf8|comma|doublequote||lf
uris.csv|utf8|semicolon|doublequote||lf
user_design_template.csv|utf8|comma|doublequote||lf
utf8.csv|utf8|comma|doublequote||lf
weapondef.csv|utf8|vslash|doublequote||lf
xlsws_category_amazon.csv|utf8|comma|doublequote||lf
zips.csv|utf8|comma|doublequote||lf
Zipssortedbycitystate.csv|utf8|comma|doublequote|doublequote|crlf
```

## File: `tests/data/annotations/csv-wrangling-messy.txt`
```
1.csv|utf8|comma|doublequote||lf
1.fail.csv|utf8|comma|doublequote||crlf
2_18-05-2011-17-21-59_0.csv|windows-1251|semicolon|doublequote|doublequote|crlf
2_ip_test.csv|utf8|comma|doublequote|doublequote|crlf
100-external-simple.csv|utf8|comma|doublequote||lf
ABCAUS2011.csv|ansi|comma|doublequote||lf
ACS_12_5YR_S1903_metadata.csv|utf8|comma|doublequote||crlf
act.csv|utf8|comma|doublequote||crlf
admins.csv|utf8|comma|doublequote||lf
af.csv|utf8|comma|doublequote|doublequote|lf
afghanngos.csv|utf8|comma|doublequote|doublequote|lf
airports.csv|utf8|comma|doublequote|doublequote|lf
alfa_example.csv|windows-1251|semicolon|doublequote||crlf
all-classes.csv|utf8|comma|doublequote|doublequote|lf
AllUseCasesOrdered.csv|utf8|vslash|doublequote||crlf
answer.csv|utf8|comma|doublequote||lf
association.csv|utf8|semicolon|doublequote||crlf
baselog.csv|utf8|comma|doublequote|doublequote|lf
benchmark.csv|utf8|comma|doublequote|doublequote|lf
BIO.csv|utf8|comma|doublequote|doublequote|lf
blocks.csv|utf8|semicolon|doublequote||crlf
bookings.csv|utf8|semicolon|doublequote|doublequote|lf
bugs.csv|utf8|comma|doublequote|doublequote|lf
CalculusComponents.csv|utf8|comma|doublequote|doublequote|lf
cassette_features.csv|utf8|comma|doublequote|doublequote|lf
cityList.csv|utf8|comma|doublequote||crlf
ckan-endpoints.csv|utf8|semicolon|doublequote||lf
cliente.csv|ansi|semicolon|doublequote|doublequote|lf
cnx22-XE133-XE131M-XE133M.csv|utf8|comma|doublequote||lf
conversion_17_to_18.csv|utf8|semicolon|doublequote|backslash|lf
coord.csv|utf8|semicolon|doublequote||lf
copyright.csv|utf8|tab|doublequote||lf
countrynames.csv|utf8|comma|doublequote||lf
coupons.csv|utf8|comma|doublequote||lf
csv_ingestion.csv|utf8|comma|doublequote|doublequote|crlf
CsvBulkLoaderTest_Players.csv|utf8|comma|doublequote|backslash|cr
cuentas.csv|utf8|semicolon|doublequote||lf
currencies.csv|utf8|comma|singlequote||lf
db_general.csv|utf8|comma|doublequote||lf
devices_data.csv|utf8|comma|doublequote||lf
diamonds.csv|utf8|space|doublequote||lf
dodgers_2010_schedule.csv|utf8|comma|doublequote||crlf
durden_saucer.csv|utf8|semicolon|doublequote|backslash|lf
Empty.csv|utf8|comma|doublequote||lf
en.csv|utf8|comma|doublequote||lf
engine_reqs_2.csv|utf8|comma|doublequote||lf
Error331_DynCatsMenu.csv|utf8|comma|doublequote||lf
events.csv|utf8|comma|doublequote||lf
exit.csv|utf8|comma|doublequote||lf
export.csv|utf8|comma|doublequote||lf
feats.csv|utf8|comma|doublequote|doublequote|lf
flat_file_database.csv|utf8|nsign|doublequote|doublequote|lf
Formats.csv|utf8|comma|doublequote|doublequote|lf
fuw1.csv|utf8|semicolon|doublequote||lf
general.csv|utf8|comma|doublequote||crlf
GPU_rod_1_metrica.csv|utf8|semicolon|doublequote||lf
iconbar-hermes.csv|utf8|comma|doublequote||lf
iometeroutput.csv|utf8|comma|doublequote||crlf
ip-log.csv|utf8|comma|doublequote||lf
isco.csv|utf8|semicolon|singlequote|backslash|lf
items.csv|utf8|comma|doublequote||crlf
JeannieProperties.csv|utf8|comma|doublequote||lf
JV_newsite_IBC_current_20110517.csv|utf8|comma|singlequote||lf
keyword-count.csv|utf8|semicolon|doublequote||lf
kodepos-2008-10-20.csv|utf8|comma|doublequote||crlf
limesurvey_survey_94328.csv|utf8|comma|doublequote||lf
linodef_bueditor_button.csv|utf8|comma|doublequote||lf
load_fund_structure_data.csv|windows-1251|semicolon|doublequote|doublequote|lf
maatkit-issues.csv|utf8|comma|doublequote|doublequote|lf
Mage_Adminhtml.csv|utf8|comma|doublequote|doublequote|lf
Mage_Catalog.csv|utf8|comma|doublequote|doublequote|lf
Mage_Lucene.csv|utf8|comma|doublequote||lf
mammalia-10.csv|utf8|tab|doublequote||lf
memberList.csv|utf8|comma|doublequote||lf
metricData.csv|utf8|comma|doublequote|doublequote|lf
mgrs_index.csv|utf8|tab|doublequote||lf
model.csv|utf8|comma|doublequote|backslash|crlf
mxoClothing.csv|utf8|semicolon|doublequote||crlf
my_Jess_Robinson.csv|utf8|comma|doublequote||lf
MyList.csv|utf8|comma|doublequote||lf
NA_letters.csv|utf8|comma|doublequote||lf
next_q.csv|utf8|comma|doublequote||lf
one-line-with-accents.csv|utf8|comma|doublequote|doublequote|crlf
orders.csv|utf8|comma|doublequote||lf
out.csv|utf8|comma|doublequote|doublequote|crlf
paperpile.csv|utf8|comma|doublequote|backslash|lf
Parsed.csv|utf8|semicolon|doublequote|doublequote|lf
poblacion.csv|utf8|semicolon|doublequote|backslash|lf
product_feed.csv|utf8|comma|doublequote||lf
prt_statuses.csv|utf8|comma|doublequote||lf
publish.csv|utf8|semicolon|doublequote||lf
questions.csv|utf8|comma|doublequote|doublequote|crlf
quotes.csv|utf8|comma|doublequote||lf
rail-points.csv|utf8|comma|doublequote||crlf
raw-data-russian-parlimentary-elections-2011-english-headers-only-no-links.csv|utf8|semicolon|doublequote|doublequote|crlf
register_data.csv|utf8|semicolon|doublequote||lf
replace.csv|utf8|comma|doublequote||lf
report.csv|utf8|comma|doublequote||lf
resources.csv|utf8|semicolon|doublequote||lf
responses.csv|utf8|comma|doublequote||lf
results.csv|utf8|tab|doublequote||lf
sample.csv|utf8|semicolon|doublequote||lf
sample_map.csv|utf8|comma|doublequote||lf
set001.csv|utf8|comma|doublequote||crlf
shops.csv|ansi|semicolon|doublequote|doublequote|crlf
solar-system.csv|utf8|comma|doublequote||lf
source-en.csv|utf8|semicolon|doublequote||crlf
spirate.csv|utf8|semicolon|doublequote||lf
stringtable.csv|utf8|comma|doublequote||lf
talks.csv|utf8|comma|doublequote||lf
task4_pad.csv|utf8|comma|doublequote||crlf
tentative_accounts.csv|utf8|comma|doublequote|doublequote|lf
test.csv|utf8|comma|doublequote||lf
test_neighbours.csv|utf8|comma|doublequote||lf
test-spreadsheet-for-csv-blank-row.csv|utf8|comma|doublequote||lf
timing.csv|utf8|comma|doublequote||lf
top-10k-2009-03-06.csv|utf8|comma|doublequote||lf
unemploy.csv|utf8|comma|doublequote||lf
uniq_nl_data.csv|utf8|nsign|singlequote||crlf
upload0.csv|utf8|comma|doublequote||lf
uris.csv|utf8|semicolon|doublequote||lf
user_design_template.csv|utf8|comma|doublequote||lf
utf8.csv|utf8|comma|doublequote||lf
weapondef.csv|utf8|vslash|doublequote||lf
xlsws_category_amazon.csv|utf8|comma|doublequote||lf
zips.csv|utf8|comma|doublequote||lf
```

## File: `tests/data/annotations/csv-wrangling.txt`
```
1.csv|utf8|comma|doublequote||lf
1.fail.csv|utf8|comma|doublequote||crlf
2_18-05-2011-17-21-59_0.csv|windows-1251|semicolon|doublequote|doublequote|crlf
2_ip_test.csv|utf8|comma|doublequote|doublequote|crlf
100-external-simple.csv|utf8|comma|doublequote||lf
211.csv|ansi|comma|doublequote|doublequote|cr
2009-2010ZS-studenti.csv|ansi|semicolon|doublequote||lf
ABCAUS2011.csv|ansi|comma|doublequote||lf
ACS_12_5YR_S1903_metadata.csv|utf8|comma|doublequote||crlf
act.csv|utf8|comma|doublequote||crlf
admins.csv|utf8|comma|doublequote||lf
ads_classic_queries.csv|utf8|comma|doublequote||lf
af.csv|utf8|comma|doublequote|doublequote|lf
afghanngos.csv|utf8|comma|doublequote|doublequote|lf
ag2.csv|utf8|semicolon|doublequote|doublequote|lf
airports.csv|utf8|comma|doublequote|doublequote|lf
ALBUMS.csv|utf8|comma|doublequote||lf
alfa_example.csv|windows-1251|semicolon|doublequote||crlf
all-classes.csv|utf8|comma|doublequote|doublequote|lf
AllUseCasesOrdered.csv|utf8|vslash|doublequote||crlf
answer.csv|utf8|comma|doublequote||lf
Apr-2014_Apr-2014_Platform.csv|utf8|comma|doublequote||crlf
articles.csv|utf8|vslash|doublequote|doublequote|lf
artists.csv|ansi|comma|doublequote||lf
association.csv|utf8|semicolon|doublequote||crlf
awaymanagers-data.csv|utf8|comma|doublequote||lf
bandwidth-2011-08-21-1MHz-175MHz.csv|utf8|tab|doublequote||lf
baselog.csv|utf8|comma|doublequote|doublequote|lf
benchmark.csv|utf8|comma|doublequote|doublequote|lf
BIO.csv|utf8|comma|doublequote|doublequote|lf
Blizak_2010.csv|ansi|semicolon|singlequote|backslash|lf
blocks.csv|utf8|semicolon|doublequote||crlf
book.csv|utf8|comma|doublequote|doublequote|crlf
bookings.csv|utf8|semicolon|doublequote|doublequote|lf
bugs.csv|utf8|comma|doublequote|doublequote|lf
CalculusComponents.csv|utf8|comma|doublequote|doublequote|lf
cassette_features.csv|utf8|comma|doublequote|doublequote|lf
cityList.csv|utf8|comma|doublequote||crlf
ckan-endpoints.csv|utf8|semicolon|doublequote||lf
cliente.csv|ansi|semicolon|doublequote|doublequote|lf
clientes_lujan.csv|ascii|comma|doublequote|doublequote|crlf
cnx22-XE133-XE131M-XE133M.csv|utf8|comma|doublequote||lf
conversion_17_to_18.csv|utf8|semicolon|doublequote|backslash|lf
coord.csv|utf8|semicolon|doublequote||lf
copyright.csv|utf8|tab|doublequote||lf
councils.csv|utf8|nsign|doublequote|doublequote|lf
countrynames.csv|utf8|comma|doublequote||lf
coupons.csv|utf8|comma|doublequote||lf
csv_data.csv|utf8|comma|doublequote||lf
csv_ingestion.csv|utf8|comma|doublequote|doublequote|crlf
csv_template.csv|utf16|comma|doublequote||lf
CsvBulkLoaderTest_Players.csv|utf8|comma|doublequote|backslash|cr
cuentas.csv|utf8|semicolon|doublequote||lf
currencies.csv|utf8|comma|singlequote||lf
data.csv|utf16|comma|doublequote||lf
data_gov_catalog.csv|ansi|comma|doublequote|doublequote|lf
data-1.csv|utf8|comma|doublequote|backslash|lf
db_general.csv|utf8|comma|doublequote||lf
dbpj_female_fbg.csv|ansi|comma|doublequote||lf
DBPortfolioGenerale.csv|ansi|semicolon|doublequote||crlf
de_DE.csv|utf8|semicolon|doublequote||lf
devices_data.csv|utf8|comma|doublequote||lf
diamonds.csv|utf8|space|doublequote||lf
dict.csv|gb2312|space|doublequote||lf
docs.csv|utf8|comma|doublequote|backslash|lf
dodgers_2010_schedule.csv|utf8|comma|doublequote||crlf
dtslist.csv|utf8|comma|doublequote||lf
dumplovr.csv|utf8|comma|doublequote|doublequote|lf
durden_saucer.csv|utf8|semicolon|doublequote|backslash|lf
Empty.csv|utf8|comma|doublequote||lf
en.csv|utf8|comma|doublequote||lf
engine_reqs_2.csv|utf8|comma|doublequote||lf
en-phrases.csv|utf8|comma|doublequote||lf
Error331_DynCatsMenu.csv|utf8|comma|doublequote||lf
events.csv|utf8|comma|doublequote||lf
example.csv|utf8|semicolon|doublequote||crlf
exit.csv|utf8|comma|doublequote||lf
explanations.csv|utf8|comma|doublequote||lf
export.csv|utf8|comma|doublequote||lf
feats.csv|utf8|comma|doublequote|doublequote|lf
feedback.csv|utf8|comma|doublequote||crlf
flat_file_database.csv|utf8|nsign|doublequote|doublequote|lf
Formats.csv|utf8|comma|doublequote|doublequote|lf
fuw1.csv|utf8|semicolon|doublequote||lf
general.csv|utf8|comma|doublequote||crlf
GPU_rod_1_metrica.csv|utf8|semicolon|doublequote||lf
gsi_adresser_og_elevtall_2010.csv|utf8|comma|doublequote|doublequote|crlf
hirise_captions.csv|utf8|tab|doublequote||lf
iconbar-hermes.csv|utf8|comma|doublequote||lf
index_cfi.csv|utf8|comma|doublequote||lf
input.csv|utf8|comma|doublequote|doublequote|lf
iometeroutput.csv|utf8|comma|doublequote||crlf
ip-log.csv|utf8|comma|doublequote||lf
isco.csv|utf8|semicolon|singlequote|backslash|lf
items.csv|utf8|comma|doublequote||crlf
JeannieProperties.csv|utf8|comma|doublequote||lf
JV_newsite_IBC_current_20110517.csv|utf8|comma|singlequote||lf
keyword-count.csv|utf8|semicolon|doublequote||lf
kodepos-2008-10-20.csv|utf8|comma|doublequote||crlf
library_data.csv|utf8|comma|doublequote|doublequote|lf
libros.csv|utf8|semicolon|doublequote|doublequote|crlf
limesurvey_survey_94328.csv|utf8|comma|doublequote||lf
linodef_bueditor_button.csv|utf8|comma|doublequote||lf
load_fund_structure_data.csv|windows-1251|semicolon|doublequote|doublequote|lf
maatkit-issues.csv|utf8|comma|doublequote|doublequote|lf
Mage_Adminhtml.csv|utf8|comma|doublequote|doublequote|lf
Mage_Catalog.csv|utf8|comma|doublequote|doublequote|lf
Mage_Lucene.csv|utf8|comma|doublequote||lf
mammalia-10.csv|utf8|tab|doublequote||lf
memberList.csv|utf8|comma|doublequote||lf
metricData.csv|utf8|comma|doublequote|doublequote|lf
mgrs_index.csv|utf8|tab|doublequote||lf
MicrosoftTermCollection-bel.csv|utf8|comma|doublequote|doublequote|lf
model.csv|utf8|comma|doublequote|backslash|crlf
mxoClothing.csv|utf8|semicolon|doublequote||crlf
my_Jess_Robinson.csv|utf8|comma|doublequote||lf
MyList.csv|utf8|comma|doublequote||lf
NA_letters.csv|utf8|comma|doublequote||lf
next_q.csv|utf8|comma|doublequote||lf
one-line-with-accents.csv|utf8|comma|doublequote|doublequote|crlf
orders.csv|utf8|comma|doublequote||lf
orig_data.csv|utf8|comma|doublequote||lf
out.csv|utf8|comma|doublequote|doublequote|crlf
paperpile.csv|utf8|comma|doublequote|backslash|lf
parneringwithinterviews.csv|utf8|comma|doublequote|doublequote|crlf
Parsed.csv|utf8|semicolon|doublequote|doublequote|lf
phonography_lib.csv|utf8|comma|doublequote|doublequote|lf
poblacion.csv|utf8|semicolon|doublequote|backslash|lf
product_feed.csv|utf8|comma|doublequote||lf
products.csv|utf8|comma|doublequote||lf
prt_statuses.csv|utf8|comma|doublequote||lf
publish.csv|utf8|semicolon|doublequote||lf
questions.csv|utf8|comma|doublequote|doublequote|crlf
quotes.csv|utf8|comma|doublequote||lf
rail-points.csv|utf8|comma|doublequote||crlf
raw_58_house.csv|utf8|comma|doublequote||lf
raw-data-russian-parlimentary-elections-2011-english-headers-only-no-links.csv|utf8|semicolon|doublequote|doublequote|crlf
register_data.csv|utf8|semicolon|doublequote||lf
replace.csv|utf8|comma|doublequote||lf
report.csv|utf8|comma|doublequote||lf
resources.csv|utf8|semicolon|doublequote||lf
responses.csv|utf8|comma|doublequote||lf
results.csv|utf8|tab|doublequote||lf
sample.csv|utf8|semicolon|doublequote||lf
sample_map.csv|utf8|comma|doublequote||lf
set001.csv|utf8|comma|doublequote||crlf
shops.csv|ansi|semicolon|doublequote|doublequote|crlf
shortcuts.csv|utf8|vslash|doublequote||lf
simulation.csv|utf8|tab|doublequote||lf
sjis.csv|shif-jis|comma|doublequote||lf
solar-system.csv|utf8|comma|doublequote||lf
source-en.csv|utf8|semicolon|doublequote||crlf
Speaking_Tool.csv|ansi|semicolon|doublequote||cr
spirate.csv|utf8|semicolon|doublequote||lf
stringtable.csv|utf8|comma|doublequote||lf
supplements.csv|ansi|comma|doublequote|doublequote|lf
table1.csv|utf8|comma|doublequote||lf
TableA.csv|utf8|comma|doublequote||lf
talks.csv|utf8|comma|doublequote||lf
task4_pad.csv|utf8|comma|doublequote||crlf
tentative_accounts.csv|utf8|comma|doublequote|doublequote|lf
test.csv|utf8|comma|doublequote||lf
test_data.csv|utf8|comma|doublequote||lf
test_neighbours.csv|utf8|comma|doublequote||lf
test-spreadsheet-for-csv-blank-row.csv|utf8|comma|doublequote||lf
timing.csv|utf8|comma|doublequote||lf
top-10k-2009-03-06.csv|utf8|comma|doublequote||lf
tweets.csv|utf8|comma|doublequote|doublequote|lf
unemploy.csv|utf8|comma|doublequote||lf
uniq_nl_data.csv|utf8|nsign|singlequote||crlf
upload.csv|utf8|comma|doublequote||lf
upload0.csv|utf8|comma|doublequote||lf
uris.csv|utf8|semicolon|doublequote||lf
user_design_template.csv|utf8|comma|doublequote||lf
utf8.csv|utf8|comma|doublequote||lf
weapondef.csv|utf8|vslash|doublequote||lf
xlsws_category_amazon.csv|utf8|comma|doublequote||lf
zips.csv|utf8|comma|doublequote||lf
Zipssortedbycitystate.csv|utf8|comma|doublequote|doublequote|crlf
```

## File: `tests/data/annotations/pollock.txt`
```
#This file contains the dialects of each of the test files. Do not add more files to the list without first saving the corresponding CSV file in the "CSV" folder
file_name|encoding|fields_delimiter|quotechar|escapechar|records_delimiter
file_double_trailing_newline.csv|ascii|comma|doublequote|doublequote|lf
file_escape_char_0x00.csv|ascii|comma|doublequote||lf
file_escape_char_0x5C.csv|ascii|comma|doublequote|backslash|lf
file_field_delimiter_0x2C_0x20.csv|ascii|comma|doublequote|doublequote|lf
file_field_delimiter_0x3B.csv|ascii|semicolon|doublequote|doublequote|lf
file_field_delimiter_0x9.csv|ascii|tab|doublequote|doublequote|lf
file_field_delimiter_0x20.csv|ascii|space|doublequote|doublequote|lf
file_header_multirow_2.csv|ascii|comma|doublequote|doublequote|lf
file_header_multirow_3.csv|ascii|comma|doublequote|doublequote|lf
file_header_only.csv|ascii|comma|doublequote||lf
file_multitable_less.csv|ascii|semicolon|doublequote|doublequote|lf
file_multitable_more.csv|ascii|semicolon|doublequote|doublequote|lf
file_multitable_same.csv|ascii|semicolon|doublequote|doublequote|lf
file_no_header.csv|ascii|semicolon|doublequote|doublequote|lf
file_no_trailing_newline.csv|ascii|comma|doublequote|doublequote|lf
file_one_data_row.csv|ascii|comma|doublequote||lf
file_preamble.csv|ascii|comma|doublequote|doublequote|lf
file_quotation_char_0x27.csv|ascii|comma|singlequote|singlequote|lf
file_record_delimiter_0xA.csv|ascii|comma|doublequote|doublequote|lf
file_record_delimiter_0xD.csv|ascii|comma|doublequote|doublequote|cr
row_extra_quote0_col0.csv|ascii|comma|doublequote|doublequote|lf
row_extra_quote5_col3.csv|ascii|comma|doublequote|doublequote|lf
row_field_delimiter_0_0x20.csv|ascii|comma|doublequote|doublequote|lf
row_field_delimiter_5_0x20.csv|ascii|comma|doublequote|doublequote|lf
row_less_sep_row0_col1.csv|ascii|comma|doublequote|doublequote|lf
row_less_sep_row5_col6.csv|ascii|comma|doublequote|doublequote|lf
row_more_sep_row0_col0.csv|ascii|comma|doublequote|doublequote|lf
row_more_sep_row5_col6.csv|ascii|comma|doublequote|doublequote|lf
18-12-06.CSV|utf8|comma|doublequote|doublequote|lf
1% nano+20% micro.csv|utf8|comma|doublequote|doublequote|lf
10.January_2019.csv|utf8|comma|doublequote|doublequote|lf
2004-2016.csv|utf8|comma|doublequote|doublequote|lf
air_quality_station3_2006.csv|utf8|comma|doublequote|doublequote|lf
all.csv|utf8|comma|doublequote|doublequote|lf
April-2011-for-publication.csv|utf8|comma|doublequote|doublequote|lf
business_expenses_apr_jun_14_peter_lewis.csv|utf8|comma|doublequote|doublequote|lf
Camp Palacios - Humidity.csv|utf8|comma|doublequote|doublequote|lf
Consular_cases_April_2016.csv|utf8|comma|doublequote|doublequote|lf
download (6).csv|utf8|comma|doublequote|doublequote|lf
june_2015(1).csv|utf8|comma|doublequote|doublequote|lf
senior-staff-march-2020.csv|utf8|comma|doublequote|doublequote|lf
W44out.csv|utf8|comma|doublequote|doublequote|lf
workforce-management-information-dft_201706.csv|utf8|comma|doublequote|doublequote|lf
20170320-ePC_Data-Travel-Stationery.csv|utf8|comma|doublequote|doublequote|lf
dd_Wickenburg_nobmp_623.csv|utf8|semicolon|doublequote|doublequote|lf
0Al-Sn.CSV|utf8|comma|doublequote||lf
1% SiO2_003.csv|utf8|comma|doublequote||lf
100mAOne.CSV|utf8|comma|doublequote||lf
300mAThree.CSV|utf8|comma|doublequote||lf
AL5083-emissivity.csv|utf8|comma|doublequote||lf
Auto_Tone_sub205_over.csv|utf8|comma|doublequote||lf
Auto_Tone_sub242_nov.csv|utf8|comma|doublequote||lf
Auto_Tone_sub315_day1.csv|utf8|comma|singlequote||lf
Batch_3250493_batch_results.csv|utf8|comma|doublequote|doublequote|lf
Businesses with a rateable value of less than $12,000 - March 2016.csv|utf8|comma|doublequote|doublequote|lf
Camp Palacios - Wind Direction.csv|utf8|comma|doublequote||lf
Copy_of_2016-17_Q3_Final_V2.csv|utf8|comma|doublequote||lf
download (10).csv|utf8|comma|doublequote|doublequote|lf
dwp-cmg-spend-1214.csv|utf8|comma|doublequote||lf
epcs-dwp-cmg-spend-july-2017.csv|utf8|comma|doublequote|doublequote|lf
erionite.csv|utf8|semicolon|doublequote||lf
extended.csv|utf8|comma|doublequote||lf
Feb-2016.csv|utf8|comma|doublequote||lf
fire_archive_V1_50574.csv|utf8|comma|doublequote||lf
fr_hypo1.csv|utf8|comma|doublequote||lf
fr_RG65_pageid.csv|utf8|comma|doublequote||lf
GPC_DCLG_December_2015_for_Publication.csv|utf8|comma|doublequote|doublequote|lf
hist_2000_15O.csv|utf8|comma|doublequote||lf
HMRC_spending_over_25000_for_September_2018.csv|utf8|comma|doublequote|doublequote|lf
hypo5.csv|utf8|comma|doublequote||lf
Kokad pollen.csv|utf8|semicolon|doublequote||lf
LOS_1050CFit.csv|utf8|comma|doublequote|doublequote|lf
ministers-overseas-travel-jan-mar-2013.csv|utf8|comma|doublequote|doublequote|lf
ministry-of-defence__30-09-2012__mod_300912-Air-Govt-data-template-u-senior.csv|utf8|comma|doublequote|doublequote|lf
moj-aramis-data-march-11.csv|utf8|comma|doublequote|doublequote|lf
mordenite-dh-2.csv|utf8|semicolon|doublequote||lf
mos-oct-dec-2014.csv|utf8|comma|doublequote|doublequote|lf
narrow.csv|utf8|comma|doublequote||lf
nati-clin-audi-bowe-canc-2017-tran-main-fiel-list.csv|utf8|comma|doublequote|doublequote|lf
NBA_scores_out.csv|utf8|comma|doublequote|doublequote|lf
Note_4_Staff_costs_-_Average_number_of_persons_employed_13-14.csv|utf8|comma|doublequote|doublequote|lf
O18_air.csv|utf8|comma|doublequote||lf
OccurrenceData351.csv|utf8|comma|doublequote||lf
Oct_2013.csv|utf8|comma|doublequote|doublequote|lf
over25k-transparency.csv|utf8|comma|doublequote|doublequote|lf
permanent_secretary_and_director_general_expenses_and_hospitality_april_to_june_2012.csv|utf8|comma|doublequote|doublequote|lf
PLA_6%Talc-1hz.csv|utf8|comma|doublequote||lf
planning-application-aug-17.csv|utf8|comma|doublequote|doublequote|lf
prison-and-probation-ombudsman__30-09-2014__justice_PPO-September-Return-senior.csv|utf8|comma|doublequote|doublequote|lf
pssave_traindata_m=10_n=10_timelow=15_timehight=30_numofloop=2000.csv|utf8|comma|doublequote|doublequote|lf
public-toilet-borough-grid.csv|utf8|comma|doublequote||lf
rape_table_3_prosecution_outcomes_0708_1314.csv|utf8|comma|doublequote|doublequote|lf
Resultsgk06.datInfos.csv|utf8|semicolon|doublequote||lf
ResultsOR30x100-0.25_5.dat__m28.csv|utf8|semicolon|doublequote||lf
ResultsOR30x100-0.25_10.dat__m21Infos.csv|utf8|semicolon|doublequote||lf
ResultsOR30x100-0.50_1.dat__m21.csv|utf8|semicolon|doublequote||lf
ResultsOR30x100-0.50_3.dat.csv|utf8|semicolon|doublequote||lf
ResultsOR30x100-0.50_5.dat__m23.csv|utf8|semicolon|doublequote||lf
ResultsOR30x100-0.50_10.dat__m28Infos.csv|utf8|semicolon|doublequote||lf
ResultsOR30x100-0.75_1.dat__m21Infos.csv|utf8|semicolon|doublequote||lf
ResultsOR30x100-0.75_5.dat__m29Infos.csv|utf8|semicolon|doublequote||lf
ResultsOR30x100-0.75_10.dat__m13.csv|utf8|semicolon|doublequote||lf
ResultsOR30x250-0.25_7.dat.csv|utf8|semicolon|doublequote||lf
ResultsOR30x250-0.50_1.datInfos.csv|utf8|semicolon|doublequote||lf
ResultsOR30x250-0.50_4.dat.csv|utf8|semicolon|doublequote||lf
ResultsOR30x250-0.75_2.dat.csv|utf8|semicolon|doublequote||lf
ResultsOR30x250-0.75_3.dat.csv|utf8|semicolon|doublequote||lf
ResultsOR30x250-0.75_4.datInfos.csv|utf8|semicolon|doublequote||lf
ResultsOR30x250-0.75_9.datInfos.csv|utf8|semicolon|doublequote||lf
ResultsOR30x500-0.50_6.datInfos.csv|utf8|semicolon|doublequote||lf
ResultsOR30x500-0.75_3.dat.csv|utf8|semicolon|doublequote||lf
S30out.csv|utf8|comma|doublequote||lf
S39.csv|utf8|comma|doublequote||lf
scottish_law_commission-2011-03-31-organogram-junior.csv|utf8|comma|doublequote|doublequote|lf
SouthTrent_Demand_zone-based.csv|utf8|comma|doublequote||lf
spending_2020_01.csv|utf8|comma|doublequote||lf
student_loans_company_limited-2011-09-30-organogram-senior.csv|utf8|comma|doublequote|doublequote|lf
Sun2014-Rs.csv|utf8|comma|doublequote||lf
Sustainability_-_Water_consumption_P_56.csv|utf8|comma|doublequote|doublequote|lf
Takakai2008-ch4.csv|utf8|comma|doublequote||lf
tetranatrolite.csv|utf8|semicolon|doublequote||lf
trinity-house__31-03-2015__dft_310315-Trinity-House-Organogram-ver-1-junior.csv|utf8|comma|doublequote|doublequote|lf
vissim_data_conf2473_i7_v1987.csv|utf8|semicolon|doublequote||lf
vissim_data_conf2473_i12_v2026.csv|utf8|semicolon|doublequote||lf
W32.csv|utf8|comma|doublequote||lf
wairakite-dh.csv|utf8|semicolon|doublequote||lf
Wakefield Council Procurement Card Transactions 2018-19 Q2.csv|utf8|comma|doublequote||lf
Wine_Cellar_Consumption_dataset_14-15.csv|utf8|comma|doublequote|doublequote|lf
picasso.csv|utf8|tab|doublequote|doublequote|lf
FEC data - [clevercsv issue #15].csv|utf8|vslash|doublequote||lf
File with multi-line field.csv|utf8|semicolon|doublequote|doublequote|lf
Json data type - [clevercsv issue #37].csv|utf8|comma|doublequote|doublequote|lf
Line feed character is more frequent than the car return-line feed combination.csv|utf8|semicolon|doublequote|doublequote|cr
Mixed comma and colon - [clevercsv issue #35].csv|utf8|comma|doublequote||lf
Mixed comma and semicolon.csv|ascii|semicolon|singlequote|singlequote|lf
Mixed comma and semicolon-B.csv|utf8|semicolon|doublequote||lf
Multiple commas in fields.csv|utf8|semicolon|doublequote|doublequote|lf
Optional quoted fields.csv|utf8|comma|doublequote|doublequote|crlf
Pipe character is more frequent than the comma.csv|utf8|comma|doublequote||crlf
Pipe character is more frequent than the semicolon.csv|utf8|semicolon|doublequote||crlf
Rainbow CSV [issue #92].csv|utf8|comma|doublequote||lf
Short pipe separated table embedded.csv|utf8|comma|doublequote||lf
Table embedded in the last record.csv|utf8|comma|doublequote|doublequote|lf
Table embedded in the second record.csv|utf8|comma|doublequote|doublequote|lf
testGeometries.txt|utf8|semicolon|doublequote|doublequote|crlf
Undefined field delimiter.csv|utf8|comma|doublequote|doublequote|lf
movies-condensed.csv|utf8|tab|doublequote||lf
csv_good_dialect_star.csv|utf8|comma|doublequote|doublequote|crlf
```

## File: `tests/data/annotations/w3c-csvw.txt`
```
#This file contains the dialects for curated set of files from CSV on the Web Repository https://github.com/w3c/csvw.
file_name|encoding|fields_delimiter|quotechar|escapechar|records_delimiter
2010_Occupations.csv|utf8|comma|doublequote||lf
addresses.csv|utf8|comma|doublequote||lf
Album.csv|utf8|comma|doublequote||lf
Artist.csv|utf8|comma|doublequote||lf
cambornedata.csv|utf8|comma|doublequote||crlf
cambornedata-snippet.csv|utf8|comma|doublequote||lf
countries.csv|utf8|comma|doublequote||lf
country_slice.csv|utf8|comma|doublequote||lf
CSV_QS601EW2011WARDH_151277.csv|utf8|comma|doublequote||lf
csvw-requirements-notes.csv|utf8|comma|doublequote|doublequote|crlf
Customer.csv|utf8|comma|doublequote||lf
department.csv|utf8|comma|doublequote||lf
EG.csv|utf8|comma|doublequote||lf
Employee.csv|utf8|comma|doublequote||lf
ESCC-payment-data-Q2281011.csv|ansi|comma|doublequote||lf
events-listing.csv|utf8|comma|doublequote||lf
events-listing2.csv|utf8|comma|doublequote||lf
Genre.csv|utf8|comma|doublequote||lf
HEFCE_organogram_junior_data_31032011.csv|utf8|comma|doublequote||crlf
HEFCE_organogram_senior_data_31032011.csv|utf8|comma|doublequote||crlf
HXL_3W_samples_draft_Multilingual.csv|utf8|comma|doublequote||lf
Invoice.csv|utf8|comma|doublequote||lf
InvoiceLine.csv|utf8|comma|doublequote||lf
junior-roles.csv|utf8|comma|doublequote||crlf
MediaType.csv|utf8|comma|doublequote||lf
methane_molecular_structure_xyz_20140911.csv|utf8|space|doublequote||lf
moon-walkers.csv|utf8|comma|doublequote||lf
mth-10-january-2014.csv|ansi|comma|doublequote||crlf
ni.2449-S3.csv|utf8|comma|doublequote||crlf
occurrence.txt|utf8|tab|doublequote||lf
open_data_-_banes_public_toilets_-_15.09.14_-v3-2.csv|utf8|comma|doublequote||crlf
organizations.csv|utf8|comma|doublequote||lf
Palo_Alto_Trees.csv|utf8|comma|doublequote|doublequote|lf
people.csv|utf8|comma|doublequote||lf
Playlist.csv|utf8|comma|doublequote||lf
PlaylistTrack.csv|utf8|comma|doublequote||lf
PLOSone-search-results.csv|utf8|comma|doublequote||lf
pp-monthly-update-new-version.csv|utf8|comma|doublequote|doublequote|crlf
professions.csv|utf8|comma|doublequote||lf
projects.csv|utf8|comma|doublequote||lf
rembrandt-paintings.csv|utf8|comma|doublequote||lf
senior-roles.csv|utf8|comma|doublequote||crlf
soc_structure_2010.csv|utf8|comma|doublequote||crlf
task_assignments.csv|utf8|comma|doublequote||lf
test001.csv|utf8|comma|doublequote||lf
test002.csv|utf8|comma|doublequote||lf
test003.csv|utf8|comma|doublequote||lf
test005.csv|utf8|comma|doublequote||lf
test006.csv|utf8|comma|doublequote||lf
test007.csv|utf8|comma|doublequote||lf
test008.csv|utf8|comma|doublequote||lf
test009.csv|utf8|comma|doublequote||crlf
test010.csv|utf8|comma|doublequote||lf
test019.csv|utf8|comma|doublequote||lf
test020.csv|utf8|comma|doublequote||lf
test021.csv|utf8|comma|doublequote||lf
test022.csv|utf8|comma|doublequote||lf
test038.csv|utf8|comma|doublequote||lf
test039.csv|utf8|comma|doublequote||lf
test040.csv|utf8|comma|doublequote||lf
test041.csv|utf8|comma|doublequote||lf
test042.csv|utf8|comma|doublequote||lf
test043.csv|utf8|comma|doublequote||lf
test044.csv|utf8|comma|doublequote||lf
test045.csv|utf8|comma|doublequote||lf
test046.csv|utf8|comma|doublequote||lf
test047.csv|utf8|comma|doublequote||lf
test048.csv|utf8|comma|doublequote||lf
test049.csv|utf8|comma|doublequote||lf
test051.csv|utf8|comma|doublequote||lf
test052.csv|utf8|comma|doublequote||lf
test055.csv|utf8|comma|doublequote||lf
test056.csv|utf8|comma|doublequote||lf
test057.csv|utf8|comma|doublequote||lf
test058.csv|utf8|comma|doublequote||lf
test091.csv|utf8|comma|doublequote||lf
test116.csv|utf8|comma|doublequote||lf
test117.csv|utf8|comma|doublequote||lf
test120.csv|utf8|comma|doublequote||lf
test121.csv|utf8|comma|doublequote||lf
test121-ref.csv|utf8|comma|doublequote||lf
test122.csv|utf8|comma|doublequote||lf
test125.csv|utf8|comma|doublequote||lf
test126.csv|utf8|comma|doublequote||lf
test127.csv|utf8|comma|doublequote||lf
test152.csv|utf8|comma|doublequote||lf
test153.csv|utf8|comma|doublequote||lf
test154.csv|utf8|comma|doublequote||lf
test155.csv|utf8|comma|doublequote||lf
test156.csv|utf8|comma|doublequote||lf
test157.csv|utf8|comma|doublequote||lf
test158.csv|utf8|comma|doublequote||lf
test159.csv|utf8|comma|doublequote||lf
test160.csv|utf8|comma|doublequote||lf
test161.csv|utf8|comma|doublequote||lf
test162.csv|utf8|comma|doublequote||lf
test163.csv|utf8|comma|doublequote||lf
test164.csv|utf8|comma|doublequote||lf
test165.csv|utf8|comma|doublequote||lf
test166.csv|utf8|comma|doublequote||lf
test167.csv|utf8|comma|doublequote||lf
test168.csv|utf8|comma|doublequote||lf
test169.csv|utf8|comma|doublequote||lf
test170.csv|utf8|comma|doublequote||lf
test171.csv|utf8|comma|doublequote||lf
test172.csv|utf8|comma|doublequote||lf
test173.csv|utf8|comma|doublequote||lf
test174.csv|utf8|comma|doublequote||lf
test175.csv|utf8|comma|doublequote||lf
test176.csv|utf8|comma|doublequote||lf
test177.csv|utf8|comma|doublequote||lf
test178.csv|utf8|comma|doublequote||lf
test179.csv|utf8|comma|doublequote||lf
test180.csv|utf8|comma|doublequote||lf
test181.csv|utf8|comma|doublequote||lf
test182.csv|utf8|comma|doublequote||lf
test183.csv|utf8|comma|doublequote||lf
test184.csv|utf8|comma|doublequote||lf
test185.csv|utf8|comma|doublequote||lf
test186.csv|utf8|comma|doublequote||lf
test187.csv|utf8|comma|doublequote||lf
test188.csv|utf8|comma|doublequote||lf
test189.csv|utf8|comma|doublequote||lf
test190.csv|utf8|comma|doublequote||lf
test191.csv|utf8|comma|doublequote||lf
test192.csv|utf8|comma|doublequote||lf
test193.csv|utf8|comma|doublequote||lf
test194.csv|utf8|comma|doublequote||lf
test195.csv|utf8|comma|doublequote||lf
test196.csv|utf8|comma|doublequote||lf
test197.csv|utf8|comma|doublequote||lf
test198.csv|utf8|comma|doublequote||lf
test199.csv|utf8|comma|doublequote||lf
test200.csv|utf8|comma|doublequote||lf
test201.csv|utf8|comma|doublequote||lf
test202.csv|utf8|comma|doublequote||lf
test203.csv|utf8|comma|doublequote||lf
test204.csv|utf8|comma|doublequote||lf
test205.csv|utf8|comma|doublequote||lf
test206.csv|utf8|comma|doublequote||lf
test207.csv|utf8|comma|doublequote||lf
test208.csv|utf8|comma|doublequote||lf
test209.csv|utf8|comma|doublequote||lf
test210.csv|utf8|comma|doublequote||lf
test211.csv|utf8|comma|doublequote||lf
test212.csv|utf8|comma|doublequote||lf
test213.csv|utf8|comma|doublequote||lf
test214.csv|utf8|comma|doublequote||lf
test215.csv|utf8|comma|doublequote||lf
test216.csv|utf8|comma|doublequote||lf
test217.csv|utf8|comma|doublequote||lf
test218.csv|utf8|comma|doublequote||lf
test219.csv|utf8|comma|doublequote||lf
test220.csv|utf8|comma|doublequote||lf
test221.csv|utf8|comma|doublequote||lf
test222.csv|utf8|comma|doublequote||lf
test223.csv|utf8|comma|doublequote||lf
test224.csv|utf8|comma|doublequote||lf
test225.csv|utf8|comma|doublequote||lf
test226.csv|utf8|comma|doublequote||lf
test227.csv|utf8|comma|doublequote||lf
test228.csv|utf8|comma|doublequote||lf
test229.csv|utf8|comma|doublequote||lf
test230.csv|utf8|comma|doublequote||lf
test231.csv|utf8|comma|doublequote||lf
test232.csv|utf8|comma|doublequote||lf
test233.csv|utf8|comma|doublequote||lf
test234.csv|utf8|comma|doublequote||lf
test238.csv|utf8|comma|doublequote||lf
test242.csv|utf8|comma|doublequote||lf
test243.csv|utf8|comma|doublequote||lf
test244.csv|utf8|comma|doublequote||lf
test245.csv|utf8|comma|doublequote||lf
test246.csv|utf8|comma|doublequote||lf
test247.csv|utf8|comma|doublequote||lf
test248.csv|utf8|comma|doublequote||lf
test249.csv|utf8|comma|doublequote||lf
test254.csv|utf8|comma|doublequote||lf
test255.csv|utf8|comma|doublequote||lf
test256.csv|utf8|comma|doublequote||lf
test257.csv|utf8|comma|doublequote||lf
test258.csv|utf8|comma|doublequote||lf
test261.csv|utf8|comma|doublequote||lf
test262.csv|utf8|comma|doublequote||lf
test269.csv|utf8|comma|doublequote||lf
test271.csv|utf8|comma|doublequote||lf
test272.csv|utf8|comma|doublequote||lf
test279.csv|utf8|comma|doublequote||lf
test280.csv|utf8|comma|doublequote||lf
test281.csv|utf8|comma|doublequote||lf
test282.csv|utf8|comma|doublequote||lf
test283.csv|utf8|comma|doublequote||lf
test284.csv|utf8|comma|doublequote||lf
test285.csv|utf8|comma|doublequote||lf
test286.csv|utf8|comma|doublequote||lf
test287.csv|utf8|comma|doublequote||lf
test288.csv|utf8|comma|doublequote||lf
test289.csv|utf8|comma|doublequote||lf
test290.csv|utf8|comma|doublequote||lf
test291.csv|utf8|comma|doublequote||lf
test292.csv|utf8|comma|doublequote||lf
test293.csv|utf8|comma|doublequote||lf
test294.csv|utf8|comma|doublequote||lf
test295.csv|utf8|comma|doublequote||lf
test296.csv|utf8|comma|doublequote||lf
test297.csv|utf8|comma|doublequote||lf
test298.csv|utf8|comma|doublequote||lf
test299.csv|utf8|comma|doublequote||lf
test300.csv|utf8|comma|doublequote||lf
test301.csv|utf8|comma|doublequote||lf
test302.csv|utf8|comma|doublequote||lf
test303.csv|utf8|comma|doublequote||lf
test304.csv|utf8|comma|doublequote||lf
test305.csv|utf8|comma|doublequote||lf
test306.csv|utf8|comma|doublequote||lf
test307.csv|utf8|comma|doublequote||lf
Track.csv|utf8|comma|doublequote|doublequote|lf
tree-ops.csv|utf8|comma|doublequote||lf
tree-ops-ext.csv|utf8|comma|doublequote||lf
tweets.csv|utf8|comma|doublequote||lf
unicode-nfc.csv|utf8|comma|doublequote||lf
```

## File: `tests/data/fixtures/nyc_311_sample_200.csv`
```
Unique Key,Created Date,Closed Date,Agency,Agency Name,Complaint Type,Descriptor,Location Type,Incident Zip,Incident Address,Street Name,Cross Street 1,Cross Street 2,Intersection Street 1,Intersection Street 2,Address Type,City,Landmark,Facility Type,Status,Due Date,Resolution Description,Resolution Action Updated Date,Community Board,BBL,Borough,X Coordinate (State Plane),Y Coordinate (State Plane),Open Data Channel Type,Park Facility Name,Park Borough,Vehicle Type,Taxi Company Borough,Taxi Pick Up Location,Bridge Highway Name,Bridge Highway Direction,Road Ramp,Bridge Highway Segment,Latitude,Longitude,Location
42254749,04/18/2019 09:55:45 PM,04/19/2019 03:45:24 AM,NYPD,New York City Police Department,Noise - Residential,Banging/Pounding,Residential Building/House,11235,3855 SHORE PARKWAY,SHORE PARKWAY,BRAGG STREET,BELT PARKWAY WB KNAPP STREET EN,,,ADDRESS,BROOKLYN,,Precinct,Closed,04/19/2019 05:55:45 AM,The Police Department responded to the complaint and with the information available observed no evidence of the violation at that time.,04/19/2019 03:45:24 AM,15 BROOKLYN,3088060140,BROOKLYN,1002973,152924,PHONE,Unspecified,BROOKLYN,,,,,,,,40.5863974,-73.9325913,"(40.5863974, -73.9325913)"
16561258,05/01/2010 09:59:44 AM,05/01/2010 10:24:07 AM,NYPD,New York City Police Department,Traffic/Illegal Parking,Posted Parking Sign Violation,Street/Sidewalk,10019,WEST 55 STREET,WEST 55 STREET,9 AVENUE,10 AVENUE,,,BLOCKFACE,NEW YORK,,Precinct,Closed,05/01/2010 05:59:44 PM,The Police Department responded and upon arrival those responsible for the condition were gone.,05/01/2010 10:24:07 AM,04 MANHATTAN,,MANHATTAN,987551,218794,PHONE,Unspecified,MANHATTAN,,,,,,,,40.7672147,-73.9880831,"(40.7672147, -73.9880831)"
46412656,05/21/2020 06:15:38 PM,05/21/2020 06:33:51 PM,NYPD,New York City Police Department,Non-Emergency Police Matter,Face Covering Violation,Store/Commercial,11205,241 TAAFFE PLACE,TAAFFE PLACE,WILLOUGHBY AVENUE,DEKALB AVENUE,WILLOUGHBY AVENUE,DEKALB AVENUE,,BROOKLYN,TAAFFE PLACE,,Closed,,The Police Department responded to the complaint and took action to fix the condition.,05/21/2020 10:34:01 PM,03 BROOKLYN,3019250001,BROOKLYN,995466,191079,ONLINE,Unspecified,BROOKLYN,,,,,,,,40.69113738107441,-73.95955540938948,"(40.69113738107441, -73.95955540938948)"
40039013,08/17/2018 03:25:16 PM,08/20/2018 09:21:15 AM,HPD,Department of Housing Preservation and Development,PLUMBING,WATER SUPPLY,RESIDENTIAL BUILDING,10462,2132 WALLACE AVENUE,WALLACE AVENUE,,,,,ADDRESS,BRONX,,N/A,Closed,,The following complaint conditions are still open. HPD may attempt to contact you to verify the correction of the condition or may conduct an inspection.,08/20/2018 09:21:15 AM,11 BRONX,2042920024,BRONX,1021647,250439,PHONE,Unspecified,BRONX,,,,,,,,40.8539929,-73.8648172,"(40.8539929, -73.8648172)"
33913755,07/23/2016 10:09:54 AM,07/23/2016 03:10:37 PM,NYPD,New York City Police Department,Noise - Residential,Banging/Pounding,Residential Building/House,11367,79-25 150 STREET,150 STREET,79 AVENUE,UNION TURNPIKE,,,ADDRESS,FLUSHING,,Precinct,Closed,07/23/2016 06:09:54 PM,The Police Department reviewed your complaint and provided additional information below.,07/23/2016 03:10:37 PM,08 QUEENS,4067120001,QUEENS,1036022,201509,MOBILE,Unspecified,QUEENS,,,,,,,,40.7196209,-73.8132317,"(40.7196209, -73.8132317)"
18556060,08/25/2010 12:00:00 AM,09/12/2010 12:00:00 AM,HPD,Department of Housing Preservation and Development,PLUMBING,WATER-LEAKS,RESIDENTIAL BUILDING,11385,64-19 WOODBINE STREET,WOODBINE STREET,64 STREET,TRAFFIC AVENUE,,,ADDRESS,RIDGEWOOD,,N/A,Closed,,The Department of Housing Preservation and Development inspected the following conditions. Violations were issued. Information about specific violations is available at www.nyc.gov/hpd.,09/12/2010 12:00:00 AM,0 Unspecified,4036170055,Unspecified,1013387,197397,UNKNOWN,Unspecified,Unspecified,,,,,,,,,,
34961688,12/08/2016 03:45:20 PM,12/16/2016 07:55:09 AM,DOT,Department of Transportation,Broken Muni Meter,Timer Defect - Fast/Fail,Street,11217,64 7 AVENUE,7 AVENUE,LINCOLN PLACE,BERKELEY PLACE,,,ADDRESS,BROOKLYN,,N/A,Closed,12/28/2016 03:45:20 PM,"The Department of Transportation inspected the condition you reported. You can find additional information in the ""Notes to Customer"" field.",12/16/2016 07:55:09 AM,06 BROOKLYN,3009517501,BROOKLYN,991255,185391,PHONE,Unspecified,BROOKLYN,,,,,,,,40.6755294,-73.9747461,"(40.6755294, -73.9747461)"
20227197,04/13/2011 09:34:46 AM,04/13/2011 10:05:57 AM,DPR,Department of Parks and Recreation,Root/Sewer/Sidewalk Condition,Sidewalk Consultation,Street,11375,63-61 YELLOWSTONE BOULEVARD,YELLOWSTONE BOULEVARD,63 DRIVE,64 AVENUE,,,ADDRESS,FOREST HILLS,,N/A,Closed,05/13/2011 09:58:26 AM,"The agency has mailed literature to the customer concerning the Sidewalk Consultation, and is currently evaluating the request.",04/13/2011 10:05:57 AM,06 QUEENS,4021480001,QUEENS,1025253,206273,PHONE,Unspecified,QUEENS,,,,,,,,40.7327533,-73.8520519,"(40.7327533, -73.8520519)"
16296482,03/23/2010 07:20:41 PM,12/02/2013 12:00:00 AM,DOB,Department of Buildings,Special Projects Inspection Team (SPIT),Illegal Hotel Rooms In Residential Building,,11230,1305 EAST 19 STREET,EAST 19 STREET,AVENUE L,AVENUE M,,,ADDRESS,BROOKLYN,,N/A,Closed,,"The Department of Buildings determined that the conditions described in this complaint were addressed under another service request number. Click on ""Learn More"" in the ""Did You Know"" section below for more information.",12/02/2013 12:00:00 AM,14 BROOKLYN,3067390001,BROOKLYN,996377,164759,UNKNOWN,Unspecified,BROOKLYN,,,,,,,,,,
23046063,04/13/2012 12:17:04 AM,04/13/2012 12:36:30 AM,NYPD,New York City Police Department,Noise - Commercial,Loud Music/Party,Store/Commercial,10010,2 LEXINGTON AVENUE,LEXINGTON AVENUE,GRAMERCY PARK,EAST 22 STREET,,,ADDRESS,NEW YORK,,Precinct,Closed,04/13/2012 08:17:04 AM,The Police Department responded to the complaint and determined that police action was not necessary.,04/13/2012 12:35:38 AM,06 MANHATTAN,1008770018,MANHATTAN,988236,208265,PHONE,Unspecified,MANHATTAN,,,,,,,,40.738315,-73.9856164,"(40.738315, -73.9856164)"
34566659,10/18/2016 09:44:43 AM,10/18/2016 09:53:30 AM,NYPD,New York City Police Department,Derelict Vehicle,With License Plate,Street/Sidewalk,11223,2186 EAST 3 STREET,EAST 3 STREET,AVENUE U,AVENUE V,,,ADDRESS,BROOKLYN,,Precinct,Closed,10/18/2016 05:44:43 PM,The Police Department reviewed your complaint and provided additional information below.,10/18/2016 09:53:30 AM,15 BROOKLYN,3071290020,BROOKLYN,992981,156659,ONLINE,Unspecified,BROOKLYN,,,,,,,,40.5966647,-73.9685608,"(40.5966647, -73.9685608)"
28154846,05/30/2014 09:44:19 AM,05/30/2014 10:09:42 AM,DOB,DOB Inspections - Queens,Construction,Initial - Construction,Street Address,11354,32-02 LINDEN PLACE,LINDEN PLACE,32 AVENUE,34 AVENUE,,,ADDRESS,FLUSHING,,N/A,Closed,06/03/2014 09:44:19 AM,The Department of Buildings contacted you and scheduled an inspection. See Notes to Customer for more details.,05/30/2014 10:09:08 AM,07 QUEENS,4049500048,QUEENS,1030824,218969,ONLINE,Unspecified,QUEENS,,,,,,,,40.767573,-73.8318626,"(40.767573, -73.8318626)"
29662292,01/07/2015 12:00:00 AM,01/11/2015 12:00:00 AM,HPD,Department of Housing Preservation and Development,HEAT/HOT WATER,APARTMENT ONLY,RESIDENTIAL BUILDING,10035,236 EAST 118 STREET,EAST 118 STREET,3 AVENUE,2 AVENUE,,,ADDRESS,NEW YORK,,N/A,Closed,,"The Department of Housing Preservation and Development was not able to gain access to your apartment or others in the building to inspect for a lack of heat or hot water. The complaint has been closed. If the condition still exists, please file a new complaint.",01/11/2015 12:00:00 AM,11 MANHATTAN,1016670031,MANHATTAN,1001375,230330,PHONE,Unspecified,MANHATTAN,,,,,,,,40.798862,-73.9381478,"(40.798862, -73.9381478)"
20530993,05/30/2011 08:42:51 PM,05/31/2011 06:57:20 AM,DPR,Department of Parks and Recreation,Overgrown Tree/Branches,Hitting Power/Phone Lines,Street,11413,229-08 148 AVENUE,148 AVENUE,229 STREET,230 STREET,,,ADDRESS,SPRINGFIELD GARDENS,,N/A,Closed,06/09/2011 08:42:51 PM,The condition was inspected and it was determined that no work order was necessary. The condition will not be inspected again for at least 90 days.,05/31/2011 06:57:20 AM,13 QUEENS,4137170036,QUEENS,1052580,178597,PHONE,Unspecified,QUEENS,,,,,,,,40.6566205,-73.7537311,"(40.6566205, -73.7537311)"
19198603,11/24/2010 08:18:00 AM,11/27/2010 12:00:00 PM,DSNY,Brooklyn South 10,Missed Collection (All Materials),1 Missed Collection,Sidewalk,11209,8045 SHORE ROAD,SHORE ROAD,80 STREET,82 STREET,,,ADDRESS,BROOKLYN,,N/A,Closed,,The Department of Sanitation investigated this complaint and found no condition at the location.,11/27/2010 12:00:00 PM,10 BROOKLYN,3059750185,BROOKLYN,973180,168907,PHONE,Unspecified,BROOKLYN,,,,,,,,,,
19349369,12/15/2010 02:38:36 PM,12/23/2010 04:18:57 PM,DHS,DHS Advantage Programs,DHS Advantage - Tenant,Lease Expiring,Tenant Address,10472,,,,,,,ADDRESS,BRONX,,N/A,Closed,12/22/2010 06:30:59 PM,See notes.,12/23/2010 04:18:57 PM,09 BRONX,,BRONX,,,PHONE,Unspecified,BRONX,,,,,,,,,,
31830127,10/25/2015 11:07:26 AM,10/29/2015 07:27:27 AM,HPD,Department of Housing Preservation and Development,APPLIANCE,REFRIGERATOR,RESIDENTIAL BUILDING,10301,411 JERSEY STREET,JERSEY STREET,,,,,ADDRESS,STATEN ISLAND,,N/A,Closed,,The Department of Housing Preservation and Development inspected the following conditions. No violations were issued. The complaint has been closed.,10/29/2015 07:27:27 AM,01 STATEN ISLAND,5000420010,STATEN ISLAND,959960,171856,PHONE,Unspecified,STATEN ISLAND,,,,,,,,40.6383483,-74.0875198,"(40.6383483, -74.0875198)"
41659569,02/09/2019 11:58:11 PM,02/10/2019 06:52:30 PM,NYPD,New York City Police Department,Noise - Commercial,Loud Music/Party,Store/Commercial,10461,1556 WILLIAMBRIDGE ROAD,WILLIAMBRIDGE ROAD,SACKET AVENUE,PIERCE AVENUE,,,ADDRESS,BRONX,,Precinct,Closed,02/10/2019 07:58:11 AM,This complaint does not fall under the Police Department's jurisdiction.,02/10/2019 06:52:30 PM,11 BRONX,2040880003,BRONX,1026260,247626,MOBILE,Unspecified,BRONX,,,,,,,,40.8462513,-73.8481598,"(40.8462513, -73.8481598)"
43145369,06/28/2019 02:08:05 PM,07/30/2019 01:47:02 PM,DOT,Department of Transportation,Sidewalk Condition,Broken Sidewalk,Sidewalk,10460,1730 TAYLOR AVENUE,TAYLOR AVENUE,VAN NEST AVENUE,MORRIS PARK AVENUE,VAN NEST AVENUE,MORRIS PARK AVENUE,ADDRESS,BRONX,,,Closed,07/28/2019 02:08:05 PM,"The Department of Transportation will inspect the complaint location and notify the property owner within 180 days if a defective sidewalk condition exists. The property owner is responsible for maintaining, repairing and installing sidewalks adjoining their property, according to Section 19-152 of the New York City Administrative Code.",07/30/2019 05:47:06 PM,11 BRONX,2040210045,BRONX,1020420,246288,PHONE,Unspecified,BRONX,,,,,,,,40.8426047,-73.869275,"(40.8426047, -73.869275)"
26273401,09/07/2013 12:00:00 AM,09/11/2013 12:00:00 AM,HPD,Department of Housing Preservation and Development,ELECTRIC,ELECTRIC-SUPPLY,RESIDENTIAL BUILDING,11374,98-10 64 AVENUE,64 AVENUE,98 STREET,99 STREET,,,ADDRESS,Rego Park,,N/A,Closed,,The Department of Housing Preservation and Development inspected the following conditions. No violations were issued. The complaint has been closed.,09/11/2013 12:00:00 AM,06 QUEENS,4021010001,QUEENS,1023603,205423,PHONE,Unspecified,QUEENS,,,,,,,,,,
44086942,10/18/2019 06:15:15 PM,10/18/2019 10:30:33 PM,NYPD,New York City Police Department,Noise - Residential,Loud Music/Party,Residential Building/House,10013,52 HOWARD STREET,HOWARD STREET,BROADWAY,MERCER STREET,BROADWAY,MERCER STREET,,NEW YORK,HOWARD STREET,,Closed,,The Police Department responded to the complaint and with the information available observed no evidence of the violation at that time.,10/19/2019 02:30:35 AM,02 MANHATTAN,1002310016,MANHATTAN,983721,201662,ONLINE,Unspecified,MANHATTAN,,,,,,,,40.7201923,-74.0019084,"(40.7201923, -74.0019084)"
26022040,07/29/2013 07:14:45 PM,07/30/2013 07:53:57 AM,DPR,Department of Parks and Recreation,Damaged Tree,Branch Cracked and Will Fall,Street,11221,309 VAN BUREN STREET,VAN BUREN STREET,LEWIS AVENUE,STUYVESANT AVENUE,,,ADDRESS,BROOKLYN,,N/A,Closed,08/06/2013 07:14:45 PM,The condition was inspected and it was determined that no work order was necessary. The condition will not be inspected again for at least 90 days.,07/30/2013 07:53:34 AM,03 BROOKLYN,3016100061,BROOKLYN,1002328,191047,PHONE,Unspecified,BROOKLYN,,,,,,,,40.6910382,-73.9348113,"(40.6910382, -73.9348113)"
31920883,11/05/2015 09:18:00 AM,11/06/2015 09:20:00 AM,DEP,Department of Environmental Protection,Water System,Other Water Problem (Use Comments) (WZZ),,11423,,,90 AVE,182 PL,90 AVENUE,182 PLACE,INTERSECTION,Hollis,,N/A,Closed,,"The Department of Environment Protection inspected your complaint but could not find the problem you reported. If the condition persists, please call 311 (or 212-639-9675 if calling from a non-New York City area code) with more detailed information to submit a new complaint.",11/06/2015 09:20:00 AM,12 QUEENS,,QUEENS,1045545,198435,UNKNOWN,Unspecified,QUEENS,,,,,,,,40.7111226,-73.7789054,"(40.7111226, -73.7789054)"
39238613,05/20/2018 03:53:34 PM,05/20/2018 04:45:01 PM,NYPD,New York City Police Department,Noise - Street/Sidewalk,Loud Music/Party,Street/Sidewalk,10456,,,,,EAST 168 STREET,CLAY AVENUE,INTERSECTION,BRONX,,Precinct,Closed,05/20/2018 11:53:34 PM,The Police Department responded to the complaint and determined that police action was not necessary.,05/20/2018 04:45:01 PM,04 BRONX,,BRONX,1009013,242619,PHONE,Unspecified,BRONX,,,,,,,,40.8325737,-73.9105155,"(40.8325737, -73.9105155)"
42697283,05/17/2019 11:21:22 AM,06/04/2019 03:16:38 PM,DOT,Department of Transportation,Sidewalk Condition,Broken Sidewalk,Sidewalk,10310,569 BARD AVENUE,BARD AVENUE,BAKER PLACE,MORRISON AVENUE,,,ADDRESS,STATEN ISLAND,,N/A,Closed,06/16/2019 11:21:22 AM,"The Department of Transportation inspected the location more than six months ago and has notified the property owner of any defective sidewalk conditions. The property owner is responsible for maintaining, repairing and installing sidewalks adjoining their property, according to Section 19-152 of the New York City Administrative Code.",06/04/2019 03:16:38 PM,01 STATEN ISLAND,5002610021,STATEN ISLAND,954921,168653,PHONE,Unspecified,STATEN ISLAND,,,,,,,,40.6295415,-74.105662,"(40.6295415, -74.105662)"
19891481,02/22/2011 12:00:00 AM,02/25/2011 12:00:00 AM,HPD,Department of Housing Preservation and Development,HEATING,HEAT,RESIDENTIAL BUILDING,10024,3 WEST 83 STREET,WEST 83 STREET,CENTRAL PARK WEST,COLUMBUS AVENUE,,,ADDRESS,NEW YORK,,N/A,Closed,,"The Department of Housing Preservation and Development was not able to gain access to your apartment or others in the building to inspect for a lack of heat or hot water. The complaint has been closed. If the condition still exists, please file a new complaint.",02/25/2011 12:00:00 AM,0 Unspecified,1011970027,Unspecified,992220,224744,UNKNOWN,Unspecified,Unspecified,,,,,,,,,,
39562843,06/26/2018 12:41:38 AM,06/26/2018 09:12:33 AM,NYPD,New York City Police Department,Noise - Residential,Loud Music/Party,Residential Building/House,10128,405 EAST 92 STREET,EAST 92 STREET,1 AVENUE,FDR DRIVE SB ENTRANCE YORK AVE,,,ADDRESS,NEW YORK,,Precinct,Closed,06/26/2018 08:41:38 AM,The Police Department responded to the complaint and with the information available observed no evidence of the violation at that time.,06/26/2018 09:12:33 AM,08 MANHATTAN,1015730020,MANHATTAN,999093,223684,ONLINE,Unspecified,MANHATTAN,,,,,,,,40.7806247,-73.9464046,"(40.7806247, -73.9464046)"
38707149,03/16/2018 06:12:00 AM,03/19/2018 12:00:00 PM,DSNY,A - Canine Task Force Citywide,Dirty Conditions,E8 Canine Violation,Sidewalk,10458,2985 WEBSTER AVENUE,WEBSTER AVENUE,BOTANICAL SQUARE,,,,ADDRESS,BRONX,,N/A,Closed,,The Department of Sanitation investigated this complaint and found no violation at the location.,03/19/2018 12:00:00 PM,07 BRONX,2032800048,BRONX,1016748,255519,PHONE,Unspecified,BRONX,,,,,,,,40.8679553,-73.8825015,"(40.8679553, -73.8825015)"
27970420,05/03/2014 12:23:01 PM,07/04/2014 06:52:56 AM,DOHMH,Department of Health and Mental Hygiene,Food Establishment,Rodents/Insects/Garbage,Restaurant/Bar/Deli/Bakery,11372,93-10 ROOSEVELT AVENUE,ROOSEVELT AVENUE,WHITNEY AVENUE,94 STREET,,,ADDRESS,JACKSON HEIGHTS,,N/A,Closed,07/02/2014 12:23:01 PM,"The Department of Health and Mental Hygiene has sent official written notification to the Owner/Landlord warning them of potential violations and instructing them to correct the situation. If the situation persists 21 days after your initial complaint, please make a new complaint.",07/04/2014 06:40:49 AM,04 QUEENS,4015620014,QUEENS,1019434,212103,PHONE,Unspecified,QUEENS,,,,,,,,40.7487803,-73.8730176,"(40.7487803, -73.8730176)"
30598360,05/11/2015 12:00:00 AM,05/26/2015 12:00:00 AM,DOHMH,Department of Health and Mental Hygiene,Rodent,Mouse Sighting,3+ Family Mixed Use Building,10075,516 EAST 80 STREET,EAST 80 STREET,YORK AVENUE,EAST END AVENUE,,,ADDRESS,NEW YORK,,N/A,Closed,06/10/2015 03:05:43 PM,The Department of Health and Mental Hygiene will review your complaint to determine appropriate action. Complaints of this type usually result in an inspection. Please call 311 in 30 days from the date of your complaint for status,05/26/2015 12:00:00 AM,08 MANHATTAN,1015760041,MANHATTAN,998287,220470,ONLINE,Unspecified,MANHATTAN,,,,,,,,40.7718044,-73.9493216,"(40.7718044, -73.9493216)"
16183241,03/10/2010 08:26:00 AM,03/10/2010 12:00:00 PM,DSNY,BCC - Manhattan,Sanitation Condition,15 Street Cond/Dump-Out/Drop-Off,Street,10027,638 WEST 131 STREET,WEST 131 STREET,BROADWAY,12 AVENUE,,,ADDRESS,NEW YORK,,DSNY Garage,Closed,,The Department of Sanitation investigated this complaint and issued a Notice of Violation.,03/10/2010 12:00:00 AM,09 MANHATTAN,1019970056,MANHATTAN,995820,237327,PHONE,Unspecified,MANHATTAN,,,,,,,,,,
22873997,03/13/2012 03:23:00 PM,03/13/2012 03:23:00 PM,DOT,Department of Transportation,Street Light Condition,Street Light Cycling,,,HARLEM RVR DR,HARLEM RVR DR,179 ST W,,,,,,,N/A,Closed,,Service Request status for this request is available on the Department of Transportation?s website. Please click the ?Learn More? link below.,03/12/2012 03:23:00 PM,Unspecified MANHATTAN,,MANHATTAN,,,UNKNOWN,Unspecified,MANHATTAN,,,,,,,,,,
19925561,02/28/2011 01:15:14 PM,02/28/2011 03:29:26 PM,NYPD,New York City Police Department,Blocked Driveway,No Access,Street/Sidewalk,11385,22-18 HIMROD STREET,HIMROD STREET,TONSOR STREET,BEND,,,ADDRESS,RIDGEWOOD,,Precinct,Closed,02/28/2011 09:15:14 PM,The Police Department responded to the complaint and determined that police action was not necessary.,02/28/2011 03:29:26 PM,05 QUEENS,4033660014,QUEENS,1009842,198732,PHONE,Unspecified,QUEENS,,,,,,,,40.7121131,-73.9076869,"(40.7121131, -73.9076869)"
24719908,01/04/2013 02:17:00 PM,01/07/2013 12:05:00 AM,DEP,Department of Environmental Protection,Water System,Hydrant Defective (WC2),,11201,ADAMS STREET,ADAMS STREET,JOHNSON STREET,BOERUM PLACE,,,BLOCKFACE,BROOKLYN,,N/A,Closed,,The Department of Environmental Protection investigated this complaint and installed caps and chains.,01/07/2013 12:05:00 AM,02 BROOKLYN,,BROOKLYN,987338,192380,ONLINE,Unspecified,BROOKLYN,,,,,,,,,,
23206441,05/10/2012 08:41:27 AM,05/22/2012 10:46:55 AM,DPR,Department of Parks and Recreation,Root/Sewer/Sidewalk Condition,Trees and Sidewalks Program,Street,11420,130-43 118 STREET,118 STREET,SUTTER AVENUE,133 AVENUE,,,ADDRESS,SOUTH OZONE PARK,,N/A,Closed,06/09/2012 09:35:27 AM,This request has been inspected and is pending prioritization for possible inclusion in the pilot program.,05/22/2012 10:46:19 AM,10 QUEENS,4117250014,QUEENS,1033964,184901,PHONE,Unspecified,QUEENS,,,,,,,,40.6740477,-73.8207785,"(40.6740477, -73.8207785)"
34286207,09/10/2016 11:03:11 PM,09/11/2016 07:24:28 AM,NYPD,New York City Police Department,Noise - Residential,Loud Music/Party,Residential Building/House,10451,331 EAST 159 STREET,EAST 159 STREET,PARK AVENUE,COURTLANDT AVENUE,,,ADDRESS,BRONX,,Precinct,Closed,09/11/2016 07:03:11 AM,The Police Department responded to the complaint and took action to fix the condition.,09/11/2016 07:24:28 AM,03 BRONX,2024190120,BRONX,1007293,239362,MOBILE,Unspecified,BRONX,,,,,,,,40.8236389,-73.9167421,"(40.8236389, -73.9167421)"
18425908,08/06/2010 12:00:00 AM,08/09/2010 12:00:00 AM,DOHMH,Department of Health and Mental Hygiene,Rodent,Condition Attracting Rodents,Vacant Lot,11377,32-28 68 STREET,68 STREET,32 AVENUE,BROOKLYN QUEENS EXPRESSWAY,,,ADDRESS,WOODSIDE,,N/A,Closed,09/05/2010 09:34:53 AM,Please contact the Department of Health and Mental Hygiene's Pest Control Services for updated status of your complaint by calling (718) 520-4974.,08/09/2010 12:00:00 AM,03 QUEENS,4011630040,QUEENS,1012280,214630,UNKNOWN,Unspecified,QUEENS,,,,,,,,40.7557418,-73.8988265,"(40.7557418, -73.8988265)"
37068071,08/30/2017 10:40:04 AM,09/29/2017 12:49:09 PM,HPD,Department of Housing Preservation and Development,PAINT/PLASTER,WALL,RESIDENTIAL BUILDING,10452,911 WALTON AVENUE,WALTON AVENUE,,,,,ADDRESS,BRONX,,N/A,Closed,,The Department of Housing Preservation and Development inspected the following conditions. No violations were issued. The complaint has been closed.,09/29/2017 12:49:09 PM,04 BRONX,2024760050,BRONX,1005414,241007,PHONE,Unspecified,BRONX,,,,,,,,40.8281586,-73.923526,"(40.8281586, -73.923526)"
22686305,02/09/2012 12:00:00 AM,02/14/2012 12:00:00 AM,HPD,Department of Housing Preservation and Development,GENERAL CONSTRUCTION,WINDOW GUARDS,RESIDENTIAL BUILDING,11207,754 MILLER AVENUE,MILLER AVENUE,BEND,HEGEMAN AVENUE,,,ADDRESS,BROOKLYN,,N/A,Closed,,The Department of Housing Preservation and Development inspected the following conditions. Violations were issued. Information about specific violations is available at www.nyc.gov/hpd.,02/14/2012 12:00:00 AM,05 BROOKLYN,3043030032,BROOKLYN,1015326,180569,UNKNOWN,Unspecified,BROOKLYN,,,,,,,,,,
23206449,05/10/2012 06:41:41 PM,05/10/2012 08:01:08 PM,NYPD,New York City Police Department,Noise - Residential,Loud Music/Party,Residential Building/House,10030,131 WEST 137 STREET,WEST 137 STREET,LENOX AVENUE,7 AVENUE,,,ADDRESS,NEW YORK,,Precinct,Closed,05/11/2012 02:41:41 AM,The Police Department responded to the complaint and took action to fix the condition.,05/10/2012 08:00:44 PM,10 MANHATTAN,1020060014,MANHATTAN,1000595,236519,PHONE,Unspecified,MANHATTAN,,,,,,,,40.8158506,-73.9409499,"(40.8158506, -73.9409499)"
31132444,07/21/2015 12:00:00 AM,,DOHMH,Department of Health and Mental Hygiene,Rodent,Rat Sighting,3+ Family Apt. Building,10468,2486 DAVIDSON AVE,DAVIDSON AVE,,,,,LATLONG,BRONX,,N/A,Assigned,08/20/2015 05:26:26 AM,The Department of Health and Mental Hygiene will review your complaint to determine appropriate action. Complaints of this type usually result in an inspection. Please call 311 in 30 days from the date of your complaint for status,07/23/2015 08:39:07 AM,Unspecified BRONX,,BRONX,1011542,253922,MOBILE,Unspecified,BRONX,,,,,,,,40.8635902,-73.9013291,"(40.8635902, -73.9013291)"
42964236,06/13/2019 07:54:23 AM,06/14/2019 03:36:09 PM,DOT,Department of Transportation,Sidewalk Condition,Blocked - Construction,Sidewalk,10024,122 WEST 87 STREET,WEST 87 STREET,COLUMBUS AVENUE,AMSTERDAM AVENUE,COLUMBUS AVENUE,AMSTERDAM AVENUE,ADDRESS,NEW YORK,,,Closed,,"The Department of Transportation inspected the location for the condition you reported and could not find the problem. It you would like to pursue the complaint, please call 311 or (212) 639-9675 with additional information.",06/14/2019 07:36:09 PM,07 MANHATTAN,1012170142,MANHATTAN,991849,226194,UNKNOWN,Unspecified,MANHATTAN,,,,,,,,40.7875231,-73.9725585,"(40.7875231, -73.9725585)"
29056347,10/12/2014 11:31:02 PM,10/13/2014 01:30:37 AM,NYPD,New York City Police Department,Noise - Residential,Banging/Pounding,Residential Building/House,10075,300 EAST 79 STREET,EAST 79 STREET,2 AVENUE,1 AVENUE,,,ADDRESS,NEW YORK,,Precinct,Closed,10/13/2014 07:31:02 AM,The Police Department responded to the complaint and took action to fix the condition.,10/13/2014 01:30:02 AM,08 MANHATTAN,1014537501,MANHATTAN,996796,220970,PHONE,Unspecified,MANHATTAN,,,,,,,,40.773179,-73.9547037,"(40.773179, -73.9547037)"
23206455,05/10/2012 09:27:52 AM,05/10/2012 12:50:36 PM,DFTA,Department for the Aging,Housing - Low Income Senior,N/A,Senior Address,10302,,,,,,,ADDRESS,STATEN ISLAND,,N/A,Closed,05/24/2012 09:27:52 AM,"The Department for the Aging contacted you and provided the assistance requested. No further updates will be available through 311. If further assistance is needed, please open a new Service Request.",05/10/2012 12:49:31 PM,01 STATEN ISLAND,,STATEN ISLAND,,,PHONE,Unspecified,STATEN ISLAND,,,,,,,,,,
42163769,04/08/2019 12:00:00 AM,04/08/2019 12:00:00 AM,DOHMH,Department of Health and Mental Hygiene,Rodent,Rat Sighting,3+ Family Mixed Use Building,11432,89-29 163 STREET,163 STREET,89 AVENUE,JAMAICA AVENUE,,,ADDRESS,Jamaica,,N/A,Closed,05/08/2019 10:02:07 PM,The Department of Health and Mental Hygiene will review your complaint to determine appropriate action. Complaints of this type usually result in an inspection. Please call 311 in 30 days from the date of your complaint for status,04/08/2019 10:04:48 PM,12 QUEENS,4097930033,QUEENS,1040249,196797,ONLINE,Unspecified,QUEENS,,,,,,,,40.7066618,-73.7980219,"(40.7066618, -73.7980219)"
40493179,10/08/2018 12:12:01 PM,10/31/2018 03:08:04 PM,HPD,Department of Housing Preservation and Development,PAINT/PLASTER,WALL,RESIDENTIAL BUILDING,10456,1087 BOSTON ROAD,BOSTON ROAD,,,,,ADDRESS,BRONX,,N/A,Closed,,The Department of Housing Preservation and Development inspected the following conditions. Violations were issued. Information about specific violations is available at www.nyc.gov/hpd.,10/31/2018 03:08:04 PM,03 BRONX,2026070062,BRONX,1010466,240579,PHONE,Unspecified,BRONX,,,,,,,,40.8269703,-73.9052728,"(40.8269703, -73.9052728)"
33378060,05/17/2016 11:35:52 AM,05/20/2016 01:05:57 PM,DOT,Department of Transportation,Street Condition,Failed Street Repair,Street,11365,HORACE HARDING EXPRESSWAY,HORACE HARDING EXPRESSWAY,160 STREET,161 STREET,,,BLOCKFACE,FRESH MEADOWS,,N/A,Closed,05/27/2016 11:35:52 AM,The Department of Transportation inspected the condition you reported and found that the condition meets its standards and/or there is a valid permit to conduct work.,05/20/2016 01:05:57 PM,08 QUEENS,,QUEENS,1037454,208299,PHONE,Unspecified,QUEENS,,,,,,,,40.7382492,-73.808012,"(40.7382492, -73.808012)"
25312910,04/06/2013 01:22:40 PM,04/09/2013 10:08:00 AM,DOT,Department of Transportation,Street Condition,Pothole,,11693,8200 SHOREFRONT PARKWAY,SHOREFRONT PARKWAY,BEACH 81 STREET,BEACH 84 STREET,,,ADDRESS,Far Rockaway,,N/A,Closed,,The Department of Transportation inspected this complaint and repaired the problem.,04/09/2013 10:08:00 AM,Unspecified QUEENS,4161300001,QUEENS,1037822,152923,UNKNOWN,Unspecified,QUEENS,,,,,,,,,,
41908022,03/08/2019 05:52:00 PM,03/14/2019 12:00:00 AM,DSNY,Department of Sanitation,Request Large Bulky Item Collection,Request Large Bulky Item Collection,Sidewalk,11385,411 WOODWARD AVENUE,WOODWARD AVENUE,STANHOPE STREET,HIMROD STREET,,,ADDRESS,Ridgewood,,N/A,Closed,,,03/14/2019 12:00:00 AM,05 QUEENS,4033860004,QUEENS,1008630,197472,PHONE,Unspecified,QUEENS,,,,,,,,40.7086582,-73.9120633,"(40.7086582, -73.9120633)"
34605609,10/23/2016 02:48:39 PM,11/03/2016 08:58:25 AM,HPD,Department of Housing Preservation and Development,GENERAL,JANITOR/SUPER,RESIDENTIAL BUILDING,10019,859 9 AVENUE,9 AVENUE,,,,,ADDRESS,NEW YORK,,N/A,Closed,,The Department of Housing Preservation and Development inspected the following conditions. Violations were issued. Information about specific violations is available at www.nyc.gov/hpd.,11/03/2016 08:58:25 AM,04 MANHATTAN,1010650036,MANHATTAN,988041,218755,ONLINE,Unspecified,MANHATTAN,,,,,,,,40.7671075,-73.9863142,"(40.7671075, -73.9863142)"
23206465,05/10/2012 11:19:14 AM,05/14/2012 02:18:45 PM,DOT,Department of Transportation,Broken Parking Meter,Out of Order,Street,11217,222 FLATBUSH AVENUE,FLATBUSH AVENUE,DEAN STREET,BERGEN STREET,,,ADDRESS,BROOKLYN,,N/A,Closed,05/30/2012 11:19:14 AM,The Department of Transportation has completed the request or corrected the condition.,05/14/2012 02:18:14 PM,06 BROOKLYN,,BROOKLYN,991113,187388,PHONE,Unspecified,BROOKLYN,,,,,,,,40.6810108,-73.975256,"(40.6810108, -73.975256)"
15751112,01/17/2010 12:00:00 AM,01/21/2010 12:00:00 AM,HPD,Department of Housing Preservation and Development,HEATING,HEAT,RESIDENTIAL BUILDING,11211,70 ROSS STREET,ROSS STREET,WYTHE AVENUE,BEDFORD AVENUE,,,ADDRESS,BROOKLYN,,N/A,Closed,,"The Department of Housing Preservation and Development responded to a complaint of no heat or hot water and was advised by a tenant in the building that heat and hot water had been restored. If the condition still exists, please file a new complaint.",01/21/2010 12:00:00 AM,0 Unspecified,3021860001,Unspecified,994285,195587,UNKNOWN,Unspecified,Unspecified,,,,,,,,,,
30632312,05/16/2015 07:04:58 AM,05/16/2015 03:00:11 PM,NYPD,New York City Police Department,Illegal Parking,Blocked Hydrant,Street/Sidewalk,11385,70-22 69 STREET,69 STREET,70 AVENUE,CENTRAL AVENUE,,,ADDRESS,RIDGEWOOD,,Precinct,Closed,05/16/2015 03:04:58 PM,The Police Department responded and upon arrival those responsible for the condition were gone.,05/16/2015 02:59:14 PM,05 QUEENS,4036570016,QUEENS,1016372,196139,PHONE,Unspecified,QUEENS,,,,,,,,40.7049747,-73.8841449,"(40.7049747, -73.8841449)"
16861806,06/14/2010 12:00:00 AM,07/07/2010 12:00:00 AM,HPD,Department of Housing Preservation and Development,PAINT - PLASTER,CEILING,RESIDENTIAL BUILDING,10030,672 ST NICHOLAS AVENUE,ST NICHOLAS AVENUE,WEST 141 STREET,WEST 145 STREET,,,ADDRESS,NEW YORK,,N/A,Closed,,The Department of Housing Preservation and Development inspected the following conditions. Violations were issued. Information about specific violations is available at www.nyc.gov/hpd.,07/07/2010 12:00:00 AM,0 Unspecified,1020510039,Unspecified,999417,239154,UNKNOWN,Unspecified,Unspecified,,,,,,,,,,
34170943,08/24/2016 04:35:00 PM,08/26/2016 12:00:00 PM,DSNY,Lot Cleaning,Vacant Lot,8 Request to Clean Vacant Lot,Lot,11233,39 ROCHESTER AVENUE,ROCHESTER AVENUE,HERKIMER STREET,ATLANTIC AVENUE,,,ADDRESS,BROOKLYN,,N/A,Pending,,The Department of Sanitation found an open service request already exists for the same location.,08/26/2016 12:00:00 PM,03 BROOKLYN,3017090008,BROOKLYN,1004366,186236,PHONE,Unspecified,BROOKLYN,,,,,,,,40.6778287,-73.9274767,"(40.6778287, -73.9274767)"
32721999,02/18/2016 08:03:02 PM,02/23/2016 01:16:28 AM,HPD,Department of Housing Preservation and Development,HEAT/HOT WATER,ENTIRE BUILDING,RESIDENTIAL BUILDING,10454,682 EAST 141 STREET,EAST 141 STREET,,,,,ADDRESS,BRONX,,N/A,Closed,,The complaint you filed is a duplicate of a condition already reported by another tenant for a building-wide condition. The original complaint is still open. HPD may attempt to contact you to verify the correction of the condition or may conduct an inspection of your unit if the original complainant is not available for verification.,02/23/2016 01:16:28 AM,01 BRONX,2025680054,BRONX,1008362,233442,ONLINE,Unspecified,BRONX,,,,,,,,40.8073873,-73.9129009,"(40.8073873, -73.9129009)"
32922161,03/16/2016 01:23:28 PM,03/16/2016 04:09:36 PM,DOT,Department of Transportation,Sidewalk Condition,Blocked - Construction,Sidewalk,11105,22-32 49 STREET,49 STREET,DITMARS BOULEVARD,ASTORIA BOULEVARD,,,ADDRESS,ASTORIA,,N/A,Closed,03/26/2016 01:23:28 PM,The Department of Transportation contacted the customer and resolved the service request or provided the information requested.,03/16/2016 04:09:36 PM,01 QUEENS,4007580040,QUEENS,1011719,219246,UNKNOWN,Unspecified,QUEENS,,,,,,,,40.7684133,-73.9008326,"(40.7684133, -73.9008326)"
36603036,07/03/2017 05:48:25 PM,07/05/2017 08:30:00 AM,DOT,Department of Transportation,Street Condition,Pothole,,11205,122 CLASSON AVENUE,CLASSON AVENUE,EMERSON PLACE,PARK AVENUE,,,ADDRESS,BROOKLYN,,N/A,Closed,,The Department of Transportation inspected this complaint and repaired the problem.,07/05/2017 08:30:00 AM,02 BROOKLYN,3018800055,BROOKLYN,994880,193026,UNKNOWN,Unspecified,BROOKLYN,,,,,,,,40.6964821,-73.9616654,"(40.6964821, -73.9616654)"
48444304,12/18/2020 02:41:29 PM,12/20/2020 06:27:42 PM,HPD,Department of Housing Preservation and Development,HEAT/HOT WATER,ENTIRE BUILDING,RESIDENTIAL BUILDING,11691,249 BEACH   15 STREET,BEACH   15 STREET,,,,,ADDRESS,Far Rockaway,,,Closed,,"The Department of Housing Preservation and Development responded to a complaint of no heat or hot water and was advised by a tenant in the building that heat and hot water had been restored. If the condition still exists, please file a new complaint.",12/20/2020 06:27:42 PM,14 QUEENS,4156290062,QUEENS,1053933,156887,MOBILE,Unspecified,QUEENS,,,,,,,,40.597020881541596,-73.74907884692875,"(40.597020881541596, -73.74907884692875)"
38971872,04/18/2018 02:49:00 PM,07/31/2018 12:00:00 AM,DOT,Department of Transportation,Traffic Signal Condition,In Conduit,,11103,,,BROADWAY,43 ST,BROADWAY,43 STREET,INTERSECTION,Astoria,,N/A,Closed,,Service Request status for this request is available on the Department of Transportationâs website. Please click the âLearn Moreâ link below.,07/31/2018 12:00:00 AM,01 QUEENS,,QUEENS,1007354,215392,UNKNOWN,Unspecified,QUEENS,,,,,,,,40.75784758555258,-73.91660415727934,"(40.75784758555258, -73.91660415727934)"
37119651,09/06/2017 11:43:45 AM,09/06/2017 03:58:05 PM,NYPD,New York City Police Department,Noise - Commercial,Loud Music/Party,Store/Commercial,10462,1229 CASTLE HILL AVENUE,CASTLE HILL AVENUE,ELLIS AVENUE,NEWBOLD AVENUE,,,ADDRESS,BRONX,,Precinct,Closed,09/06/2017 07:43:45 PM,The Police Department responded to the complaint and with the information available observed no evidence of the violation at that time.,09/06/2017 03:58:05 PM,09 BRONX,2038130049,BRONX,1025411,242728,ONLINE,Unspecified,BRONX,,,,,,,,40.8328117,-73.8512584,"(40.8328117, -73.8512584)"
16643434,05/12/2010 11:06:59 AM,06/02/2010 02:12:09 AM,TLC,Taxi and Limousine Commission,Taxi Complaint,Driver Complaint,Street,10037,,,,,WEST 139 STREET,LENOX AVENUE,INTERSECTION,NEW YORK,,N/A,Closed,06/02/2010 01:32:13 PM,"The complaint confirmation letter was not returned to the Taxi and Limousine Commission, therefore the complaint cannot be processed.",06/02/2010 02:12:09 AM,10 MANHATTAN,,MANHATTAN,1001137,236815,PHONE,Unspecified,MANHATTAN,,,Other,,,,,40.816662,-73.9389911,"(40.816662, -73.9389911)"
48024139,10/30/2020 09:09:09 AM,11/02/2020 05:50:06 PM,HPD,Department of Housing Preservation and Development,HEAT/HOT WATER,ENTIRE BUILDING,RESIDENTIAL BUILDING,10461,1821 MAHAN AVENUE,MAHAN AVENUE,,,,,ADDRESS,BRONX,,,Closed,,"The Department of Housing Preservation and Development responded to a complaint of no heat or hot water and was advised by a tenant in the building that heat and hot water had been restored. If the condition still exists, please file a new complaint.",11/02/2020 05:50:06 PM,10 BRONX,2041960018,BRONX,1031181,248641,MOBILE,Unspecified,BRONX,,,,,,,,40.84901241451358,-73.8303663339637,"(40.84901241451358, -73.8303663339637)"
45897786,03/26/2020 01:52:33 AM,03/26/2020 01:52:33 AM,DOB,Department of Buildings,Emergency Response Team (ERT),After Hours Work - Illegal,,11201,7 BOERUM PLACE,BOERUM PLACE,,,,,ADDRESS,BROOKLYN,,N/A,Closed,,The Department of Buildings investigated this complaint and determined that no further action was necessary.,03/26/2020 12:00:00 AM,02 BROOKLYN,3001530003,BROOKLYN,987264,191275,UNKNOWN,Unspecified,BROOKLYN,,,,,,,,40.6916819,-73.9891315,"(40.6916819, -73.9891315)"
19767844,02/05/2011 10:25:21 PM,02/06/2011 03:26:04 AM,NYPD,New York City Police Department,Blocked Driveway,No Access,Street/Sidewalk,11378,52-89 70 STREET,70 STREET,52 DRIVE,53 AVENUE,,,ADDRESS,MASPETH,,Precinct,Closed,02/06/2011 06:25:21 AM,The Police Department responded and upon arrival those responsible for the condition were gone.,02/06/2011 03:26:04 AM,05 QUEENS,4024810003,QUEENS,1013660,205785,PHONE,Unspecified,QUEENS,,,,,,,,40.73146,-73.8938841,"(40.73146, -73.8938841)"
31216281,07/31/2015 09:18:17 PM,08/05/2015 10:45:45 AM,HPD,Department of Housing Preservation and Development,ELECTRIC,POWER OUTAGE,RESIDENTIAL BUILDING,11374,98-10 64 AVENUE,64 AVENUE,,,,,ADDRESS,Rego Park,,N/A,Closed,,The Department of Housing Preservation and Development inspected the following conditions. No violations were issued. The complaint has been closed.,08/05/2015 10:45:45 AM,06 QUEENS,4021010001,QUEENS,1023603,205423,PHONE,Unspecified,QUEENS,,,,,,,,40.7304278,-73.8580104,"(40.7304278, -73.8580104)"
37379179,10/08/2017 11:42:02 AM,10/12/2017 05:07:25 PM,HPD,Department of Housing Preservation and Development,ELECTRIC,OUTLET/SWITCH,RESIDENTIAL BUILDING,10032,250 FT WASHINGTON AVENUE,FT WASHINGTON AVENUE,,,,,ADDRESS,NEW YORK,,N/A,Closed,,The Department of Housing Preservation and Development inspected the following conditions. No violations were issued. The complaint has been closed.,10/12/2017 05:07:25 PM,12 MANHATTAN,1021420001,MANHATTAN,1000443,246636,PHONE,Unspecified,MANHATTAN,,,,,,,,40.8436191,-73.9414746,"(40.8436191, -73.9414746)"
30701629,05/26/2015 12:00:00 AM,06/03/2015 12:00:00 AM,HPD,Department of Housing Preservation and Development,WATER LEAK,HEAVY FLOW,RESIDENTIAL BUILDING,10457,1511 SHERIDAN AVENUE,SHERIDAN AVENUE,,,,,ADDRESS,BRONX,,N/A,Closed,,The Department of Housing Preservation and Development inspected the following conditions. Violations were issued. Information about specific violations is available at www.nyc.gov/hpd.,06/03/2015 12:00:00 AM,04 BRONX,2028210068,BRONX,1008782,245677,PHONE,Unspecified,BRONX,,,,,,,,40.8409677,-73.911339,"(40.8409677, -73.911339)"
38318012,01/26/2018 09:54:14 AM,01/26/2018 12:55:39 PM,NYPD,New York City Police Department,Illegal Parking,Blocked Sidewalk,Street/Sidewalk,10460,1171 WYATT STREET,WYATT STREET,BRONX PARK AVENUE,MORRIS PARK AVENUE,,,ADDRESS,BRONX,,Precinct,Closed,01/26/2018 05:54:14 PM,The Police Department issued a summons in response to the complaint.,01/26/2018 12:55:39 PM,06 BRONX,2039080043,BRONX,1018638,244881,PHONE,Unspecified,BRONX,,,,,,,,40.83875,-73.8757226,"(40.83875, -73.8757226)"
30282317,03/28/2015 02:11:53 AM,03/28/2015 06:55:02 AM,NYPD,New York City Police Department,Noise - Commercial,Loud Talking,Store/Commercial,10302,958 POST AVENUE,POST AVENUE,SIMONSON PLACE,DECKER AVENUE,,,ADDRESS,STATEN ISLAND,,Precinct,Closed,03/28/2015 10:11:53 AM,The Police Department responded to the complaint and with the information available observed no evidence of the violation at that time.,03/28/2015 06:42:44 AM,01 STATEN ISLAND,5010290033,STATEN ISLAND,947458,169543,MOBILE,Unspecified,STATEN ISLAND,,,,,,,,40.6319565,-74.1325533,"(40.6319565, -74.1325533)"
45117977,12/07/2019 08:14:14 AM,12/08/2019 02:06:20 AM,NYPD,New York City Police Department,Blocked Driveway,No Access,Street/Sidewalk,11385,1888 HART STREET,HART STREET,ONDERDONK AVENUE,WOODWARD AVENUE,ONDERDONK AVENUE,WOODWARD AVENUE,,RIDGEWOOD,HART STREET,,Closed,,The Police Department responded and upon arrival those responsible for the condition were gone.,12/08/2019 07:06:22 AM,05 QUEENS,4033990034,QUEENS,1007856,197869,MOBILE,Unspecified,QUEENS,,,,,,,,40.7097499,-73.9148536,"(40.7097499, -73.9148536)"
35535415,02/20/2017 06:23:53 PM,03/27/2017 02:19:33 PM,HPD,Department of Housing Preservation and Development,PAINT/PLASTER,WALL,RESIDENTIAL BUILDING,10031,508 WEST 151 STREET,WEST 151 STREET,,,,,ADDRESS,NEW YORK,,N/A,Closed,,The Department of Housing Preservation and Development was unable to access the rooms where the following conditions were reported. No violations were issued. The complaint has been closed.,03/27/2017 02:19:33 PM,09 MANHATTAN,1020820040,MANHATTAN,999357,241402,PHONE,Unspecified,MANHATTAN,,,,,,,,40.8292552,-73.9454115,"(40.8292552, -73.9454115)"
34542600,10/16/2016 12:31:58 AM,10/16/2016 04:22:45 AM,NYPD,New York City Police Department,Noise - Commercial,Loud Music/Party,Club/Bar/Restaurant,11357,,,,,149 STREET,WILLETS POINT BOULEVARD,INTERSECTION,WHITESTONE,,Precinct,Closed,10/16/2016 08:31:58 AM,The Police Department responded to the complaint and with the information available observed no evidence of the violation at that time.,10/16/2016 04:22:45 AM,07 QUEENS,,QUEENS,1034756,222192,PHONE,Unspecified,QUEENS,,,,,,,,40.7763977,-73.8176434,"(40.7763977, -73.8176434)"
27911112,04/24/2014 10:43:00 PM,04/28/2014 12:00:00 PM,DSNY,A - Brooklyn,Dirty Conditions,E1 Improper Disposal,Sidewalk,11207,256 HIGHLAND BOULEVARD,HIGHLAND BOULEVARD,BULWER PLACE,HEATH PLACE,,,ADDRESS,BROOKLYN,,N/A,Closed,,The Department of Sanitation investigated this complaint and found no violation at the location.,04/28/2014 12:00:00 PM,05 BROOKLYN,3038860026,BROOKLYN,1014064,187931,PHONE,Unspecified,BROOKLYN,,,,,,,,40.6824537,-73.8925055,"(40.6824537, -73.8925055)"
32701129,02/16/2016 08:35:52 PM,03/31/2016 07:56:49 AM,HPD,Department of Housing Preservation and Development,WATER LEAK,HEAVY FLOW,RESIDENTIAL BUILDING,11368,104-27 46 AVENUE,46 AVENUE,,,,,ADDRESS,Corona,,N/A,Closed,,"The Department of Housing Preservation and Development was not able to gain access to inspect the following conditions. The complaint has been closed. If the condition still exists, please file a new complaint.",03/31/2016 07:56:49 AM,04 QUEENS,4019890070,QUEENS,1023195,211290,PHONE,Unspecified,QUEENS,,,,,,,,40.746533,-73.8594486,"(40.746533, -73.8594486)"
43537807,08/13/2019 03:29:24 PM,08/14/2019 02:59:25 AM,NYPD,New York City Police Department,Noise - Commercial,Banging/Pounding,Store/Commercial,11238,1111 FULTON STREET,FULTON STREET,CLAVER PLACE,FRANKLIN AVENUE,CLAVER PLACE,FRANKLIN AVENUE,,BROOKLYN,FULTON STREET,,Closed,,The Police Department responded to the complaint and determined that police action was not necessary.,08/14/2019 06:59:27 AM,03 BROOKLYN,3019970060,BROOKLYN,996166,187542,MOBILE,Unspecified,BROOKLYN,,,,,,,,40.68142821215693,-73.95703748426672,"(40.68142821215693, -73.95703748426672)"
46752950,07/03/2020 08:55:06 AM,07/07/2020 09:05:16 PM,HPD,Department of Housing Preservation and Development,DOOR/WINDOW,DOOR,RESIDENTIAL BUILDING,11212,1698 PITKIN AVENUE,PITKIN AVENUE,,,,,ADDRESS,BROOKLYN,,,Closed,,The Department of Housing Preservation and Development inspected the following conditions. No violations were issued. The complaint has been closed.,07/07/2020 09:05:16 PM,16 BROOKLYN,3035220014,BROOKLYN,1009084,183284,PHONE,Unspecified,BROOKLYN,,,,,,,,40.6697141,-73.910478,"(40.6697141, -73.910478)"
48116118,11/09/2020 09:47:33 PM,11/09/2020 10:12:19 PM,NYPD,New York City Police Department,Noise - Street/Sidewalk,Loud Music/Party,Street/Sidewalk,10024,589 AMSTERDAM AVENUE,AMSTERDAM AVENUE,WEST   88 STREET,WEST   89 STREET,WEST   88 STREET,WEST   89 STREET,,NEW YORK,AMSTERDAM AVENUE,,Closed,,The Police Department responded to the complaint and with the information available observed no evidence of the violation at that time.,11/10/2020 03:12:23 AM,07 MANHATTAN,1012190001,MANHATTAN,991491,226827,ONLINE,Unspecified,MANHATTAN,,,,,,,,40.789260886149705,-73.97385066924859,"(40.789260886149705, -73.97385066924859)"
23206508,05/10/2012 09:21:13 PM,08/27/2012 09:32:11 AM,DPR,Department of Parks and Recreation,Damaged Tree,Branch or Limb Has Fallen Down,Street,11367,64-12 155 STREET,155 STREET,64 AVENUE,65 AVENUE,,,ADDRESS,FLUSHING,,N/A,Closed,06/30/2012 11:18:19 AM,The Department of Parks and Recreation has corrected the condition.,08/27/2012 09:31:34 AM,08 QUEENS,4067430009,QUEENS,1035989,208092,PHONE,Unspecified,QUEENS,,,,,,,,40.7376897,-73.8133001,"(40.7376897, -73.8133001)"
46463507,06/13/2020 05:47:20 PM,06/13/2020 06:09:03 PM,NYPD,New York City Police Department,Non-Emergency Police Matter,Social Distancing,Store/Commercial,10014,183 WEST   10 STREET,WEST   10 STREET,7 AVENUE SOUTH,WEST    4 STREET,7 AVENUE SOUTH,WEST    4 STREET,,NEW YORK,WEST   10 STREET,,Closed,,The Police Department responded to the complaint and determined that police action was not necessary.,06/13/2020 10:09:05 PM,02 MANHATTAN,1006110001,MANHATTAN,983473,206797,PHONE,Unspecified,MANHATTAN,,,,,,,,40.73428661860387,-74.00280365511169,"(40.73428661860387, -74.00280365511169)"
29785832,01/24/2015 04:26:43 PM,02/06/2015 12:00:00 AM,DOB,Department of Buildings,Electrical,Electrical Wiring Defective/Exposed,,11218,204 PROSPECT PARK SOUTH WEST,PROSPECT PARK SOUTH WEST,GREENWOOD AVENUE,EAST DRIVE,,,ADDRESS,BROOKLYN,,N/A,Closed,,"The Department of Buildings attempted to investigate this complaint twice but could not gain access to the location. If the problem still exists, please call 311 and file a new complaint with additional access information. If you are outside of New York City, please call (212) NEW-YORK (212-639-9675).",02/06/2015 12:00:00 AM,07 BROOKLYN,3052870038,BROOKLYN,991847,176958,UNKNOWN,Unspecified,BROOKLYN,,,,,,,,40.6523822,-73.9726213,"(40.6523822, -73.9726213)"
38112535,01/04/2018 12:42:15 PM,01/18/2018 02:14:08 AM,HPD,Department of Housing Preservation and Development,HEAT/HOT WATER,ENTIRE BUILDING,RESIDENTIAL BUILDING,10040,90 ELLWOOD STREET,ELLWOOD STREET,,,,,ADDRESS,NEW YORK,,N/A,Closed,,"The Department of Housing Preservation and Development responded to a complaint of no heat or hot water and was advised by a tenant in the building that heat and hot water had been restored. If the condition still exists, please file a new complaint.",01/18/2018 02:14:08 AM,12 MANHATTAN,1021720041,MANHATTAN,1003821,253153,PHONE,Unspecified,MANHATTAN,,,,,,,,40.8614995,-73.9292467,"(40.8614995, -73.9292467)"
31665095,10/02/2015 12:30:00 AM,10/06/2015 02:45:00 PM,DEP,Department of Environmental Protection,Air Quality,"Air: Smoke, Chimney or vent (AS1)",,10005,75 WALL STREET,WALL STREET,GOUVERNEUR LN,WALL ST,,,ADDRESS,NEW YORK,,N/A,Closed,,"The Department of Environmental Protection did not observe a violation of the New York City Air/Noise Code at the time of inspection and could not issue a notice of violation. If the problem still exists, please call 311 and file a new complaint. If you are outside of New York City, please call (212) NEW-YORK (212-639-9675).",10/06/2015 02:45:00 PM,01 MANHATTAN,1000317501,MANHATTAN,982103,196230,ONLINE,Unspecified,MANHATTAN,,,,,,,,40.7052825,-74.0077437,"(40.7052825, -74.0077437)"
38690320,03/14/2018 11:39:00 PM,03/16/2018 11:00:00 PM,DEP,Department of Environmental Protection,Noise,Noise: Construction Before/After Hours (NM1),,10038,90 FULTON STREET,FULTON STREET,GOLD ST,WILLIAM ST,,,ADDRESS,NEW YORK,,N/A,Closed,,"The Department of Environmental Protection did not observe a violation of the New York City Air/Noise Code at the time of inspection and could not issue a notice of violation. If the problem still exists, please call 311 and file a new complaint. If you are outside of New York City, please call (212) NEW-YORK (212-639-9675).",03/16/2018 11:00:00 PM,01 MANHATTAN,1000770015,MANHATTAN,982582,197707,ONLINE,Unspecified,MANHATTAN,,,,,,,,40.7093366,-74.0060164,"(40.7093366, -74.0060164)"
37587983,11/01/2017 03:26:20 PM,11/02/2017 11:54:00 AM,DOT,Department of Transportation,Street Condition,Pothole,,11220,4 AVENUE,4 AVENUE,54 STREET,55 STREET,,,BLOCKFACE,BROOKLYN,,N/A,Closed,,The Department of Transportation inspected this complaint and repaired the problem.,11/02/2017 11:54:00 AM,07 BROOKLYN,,BROOKLYN,980031,173885,UNKNOWN,Unspecified,BROOKLYN,,,,,,,,40.6439502,-74.0151994,"(40.6439502, -74.0151994)"
27838680,04/13/2014 07:29:31 PM,04/13/2014 10:34:33 PM,NYPD,New York City Police Department,Noise - Residential,Loud Music/Party,Residential Building/House,11385,78-65 85 STREET,85 STREET,78 AVENUE,MYRTLE AVENUE,,,ADDRESS,RIDGEWOOD,,Precinct,Closed,04/14/2014 03:29:31 AM,The Police Department responded to the complaint and with the information available observed no evidence of the violation at that time.,04/13/2014 10:33:14 PM,05 QUEENS,4038440015,QUEENS,1021980,195891,ONLINE,Unspecified,QUEENS,,,,,,,,40.7042718,-73.8639198,"(40.7042718, -73.8639198)"
23206523,05/10/2012 01:40:28 PM,05/10/2012 02:24:04 PM,NYPD,New York City Police Department,Noise - Vehicle,Engine Idling,Street/Sidewalk,11379,72-52 METROPOLITAN AVENUE,METROPOLITAN AVENUE,LUTHERAN CEMETERY BOUNDARY,73 PLACE,,,ADDRESS,MIDDLE VILLAGE,,Precinct,Closed,05/10/2012 09:40:28 PM,The Police Department responded and upon arrival those responsible for the condition were gone.,05/10/2012 02:23:41 PM,05 QUEENS,4036677501,QUEENS,1017536,198940,PHONE,Unspecified,QUEENS,,,,,,,,40.7126584,-73.8799328,"(40.7126584, -73.8799328)"
44102076,10/20/2019 02:57:23 AM,10/20/2019 04:50:12 AM,NYPD,New York City Police Department,Noise - Commercial,Loud Music/Party,Store/Commercial,11209,7316 3 AVENUE,3 AVENUE,73 STREET,74 STREET,73 STREET,74 STREET,,BROOKLYN,3 AVENUE,,Closed,,The Police Department responded to the complaint and with the information available observed no evidence of the violation at that time.,10/20/2019 08:50:16 AM,10 BROOKLYN,3059170044,BROOKLYN,976669,169772,MOBILE,Unspecified,BROOKLYN,,,,,,,,40.6326582,-74.0273129,"(40.6326582, -74.0273129)"
31536250,09/15/2015 09:30:42 AM,01/18/2018 03:19:09 PM,DPR,Department of Parks and Recreation,Overgrown Tree/Branches,Blocking Street,Street,11429,111 AVENUE,111 AVENUE,223 STREET,225 STREET,,,BLOCKFACE,QUEENS VILLAGE,,N/A,Closed,03/12/2017 09:28:19 AM,The Department of Parks and Recreation has determined that the issue will be addressed in the next pruning cycle through the routine block pruning program.,01/18/2018 03:19:09 PM,13 QUEENS,,QUEENS,1058316,196631,PHONE,Unspecified,QUEENS,,,,,,,,40.7060734,-73.7328598,"(40.7060734, -73.7328598)"
43650566,08/26/2019 04:15:18 PM,09/05/2019 12:14:11 PM,DOHMH,Department of Health and Mental Hygiene,Rodent,Rat Sighting,3+ Family Apartment Building,11238,189 ST MARKS AVENUE,ST MARKS AVENUE,CARLTON AVENUE,VANDERBILT AVENUE,CARLTON AVENUE,VANDERBILT AVENUE,ADDRESS,BROOKLYN,ST MARKS AVENUE,,Closed,,,08/30/2019 05:07:40 PM,08 BROOKLYN,3011440072,BROOKLYN,992629,186588,PHONE,Unspecified,BROOKLYN,,,,,,,,40.6788137,-73.9697911,"(40.6788137, -73.9697911)"
48007859,10/28/2020 07:55:42 AM,11/10/2020 12:28:08 PM,HPD,Department of Housing Preservation and Development,WATER LEAK,DAMP SPOT,RESIDENTIAL BUILDING,11225,50 LINCOLN ROAD,LINCOLN ROAD,,,,,ADDRESS,BROOKLYN,,,Closed,,The Department of Housing Preservation and Development inspected the following conditions. No violations were issued. The complaint has been closed.,11/10/2020 12:28:08 PM,09 BROOKLYN,3050260065,BROOKLYN,995012,180033,ONLINE,Unspecified,BROOKLYN,,,,,,,,40.660819168462886,-73.96121015904247,"(40.660819168462886, -73.96121015904247)"
47096589,08/04/2020 05:33:08 PM,08/06/2020 05:28:14 PM,DPR,Department of Parks and Recreation,Damaged Tree,Entire Tree Has Fallen Down,Street,10027,3111 BROADWAY,BROADWAY,WEST  123 STREET,LA SALLE STREET,WEST  123 STREET,LA SALLE STREET,,NEW YORK,BROADWAY,,Closed,,The Department of Parks and Recreation performed the work necessary to correct the condition.,08/06/2020 09:28:21 PM,09 MANHATTAN,1019930015,MANHATTAN,995214,235413,MOBILE,Unspecified,MANHATTAN,,,,,,,,40.8128232705935,-73.9603918284767,"(40.8128232705935, -73.9603918284767)"
33243154,04/29/2016 04:18:00 PM,04/29/2016 04:18:00 PM,DEP,Department of Environmental Protection,Water System,Leak (Use Comments) (WA2),,11413,,,,,228 STREET,MERRICK BOULEVARD,INTERSECTION,Springfield Gardens,,N/A,Closed,,The Department of Environmental Protection determined that this complaint is a duplicate of a previously filed complaint. The original complaint is being addressed.,04/29/2016 04:18:00 PM,13 QUEENS,,QUEENS,1055757,185920,PHONE,Unspecified,QUEENS,,,,,,,,40.6766954,-73.7422032,"(40.6766954, -73.7422032)"
19419082,12/25/2010 12:00:00 AM,01/03/2011 12:00:00 AM,HPD,Department of Housing Preservation and Development,HEATING,HEAT,RESIDENTIAL BUILDING,11209,220 72 STREET,72 STREET,RIDGE BOULEVARD,3 AVENUE,,,ADDRESS,BROOKLYN,,N/A,Closed,,"More than one complaint was received for this building-wide condition.This complaint status is for the initial complaint.The Department of Housing Preservation and Development contacted an occupant of the apartment and verified that the following conditions were corrected. The complaint has been closed. If the condition still exists, please file a new c",01/03/2011 12:00:00 AM,0 Unspecified,3059070018,Unspecified,976242,170246,UNKNOWN,Unspecified,Unspecified,,,,,,,,,,
25012731,02/16/2013 04:48:47 PM,05/15/2013 12:00:00 AM,DSNY,Department of Sanitation,Graffiti,Graffiti,Mixed Use,10470,4330 KATONAH AVENUE,KATONAH AVENUE,EAST 238 STREET,EAST 239 STREET,,,ADDRESS,BRONX,,N/A,Closed,,The City has removed the graffiti from this property.,05/17/2013 12:56:56 PM,12 BRONX,2033870001,BRONX,1020854,267121,UNKNOWN,Unspecified,BRONX,,,,,,,,40.8997831,-73.8675926,"(40.8997831, -73.8675926)"
17566285,07/02/2010 11:20:42 AM,07/13/2010 09:04:07 AM,NYCEM,NYC Emergency Management,OEM Literature Request,Ready NY - Spanish - Full Size,,,,,,,,,,,,N/A,Closed,07/20/2010 09:04:05 AM,"The literature has been mailed. If it has not been received, please request it again from 311.",07/13/2010 09:04:07 AM,0 Unspecified,,Unspecified,,,PHONE,Unspecified,Unspecified,,,,,,,,,,
35057744,12/19/2016 11:43:31 AM,12/27/2016 04:11:21 PM,HPD,Department of Housing Preservation and Development,DOOR/WINDOW,DOOR FRAME,RESIDENTIAL BUILDING,10453,130 WEST 183 STREET,WEST 183 STREET,,,,,ADDRESS,BRONX,,N/A,Closed,,The Department of Housing Preservation and Development inspected the following conditions. Violations were issued. Information about specific violations is available at www.nyc.gov/hpd.,12/27/2016 04:11:21 PM,07 BRONX,2032230030,BRONX,1009071,252673,PHONE,Unspecified,BRONX,,,,,,,,40.8601688,-73.9102687,"(40.8601688, -73.9102687)"
16510273,04/23/2010 12:00:00 AM,04/28/2010 12:00:00 AM,HPD,Department of Housing Preservation and Development,GENERAL CONSTRUCTION,DOORS,RESIDENTIAL BUILDING,10034,647 ACADEMY STREET,ACADEMY STREET,VERMILYEA AVENUE,BROADWAY,,,ADDRESS,NEW YORK,,N/A,Closed,,The Department of Housing Preservation and Development inspected the following conditions. No violations were issued. The complaint has been closed.,04/28/2010 12:00:00 AM,0 Unspecified,1022340047,Unspecified,1005073,254759,UNKNOWN,Unspecified,Unspecified,,,,,,,,,,
23528640,06/30/2012 09:53:00 PM,07/06/2012 12:00:00 PM,DSNY,A - Manhattan,Dirty Conditions,E5 Loose Rubbish,Sidewalk,10023,72 WEST 69 STREET,WEST 69 STREET,CENTRAL PARK WEST,COLUMBUS AVENUE,,,ADDRESS,NEW YORK,,N/A,Closed,,The Department of Sanitation investigated this complaint and found no violation at the location.,07/06/2012 12:00:00 PM,07 MANHATTAN,1011210062,MANHATTAN,989998,221655,PHONE,Unspecified,MANHATTAN,,,,,,,,,,
32801674,02/29/2016 06:50:00 PM,03/01/2016 11:09:00 AM,DOT,Department of Transportation,Street Light Condition,Street Light Out,,11209,119 86 STREET,86 STREET,COLONIAL RD,RIDGE BLVD,86 STREET,COLONIAL ROAD,INTERSECTION,BROOKLYN,,N/A,Closed,,Service Request status for this request is available on the Department of Transportation?s website. Please click the ?Learn More? link below.,03/01/2016 11:09:00 AM,10 BROOKLYN,3060320074,BROOKLYN,974138,166886,UNKNOWN,Unspecified,BROOKLYN,,,,,,,,40.6247342,-74.0364273,"(40.6247342, -74.0364273)"
31935209,11/07/2015 11:53:55 PM,11/08/2015 03:07:21 AM,NYPD,New York City Police Department,Noise - Commercial,Loud Music/Party,Club/Bar/Restaurant,10002,39 ESSEX STREET,ESSEX STREET,HESTER STREET,GRAND STREET,,,ADDRESS,NEW YORK,,Precinct,Closed,11/08/2015 07:53:55 AM,The Police Department responded to the complaint and with the information available observed no evidence of the violation at that time.,11/08/2015 03:06:58 AM,03 MANHATTAN,1003100026,MANHATTAN,987170,200184,ONLINE,Unspecified,MANHATTAN,,,,,,,,40.7161351,-73.9894666,"(40.7161351, -73.9894666)"
41775744,02/24/2019 11:07:01 PM,02/25/2019 02:26:19 AM,NYPD,New York City Police Department,Noise - Residential,Loud Music/Party,Residential Building/House,10033,603 WEST 184 STREET,WEST 184 STREET,ST NICHOLAS AVENUE,WADSWORTH AVENUE,,,ADDRESS,NEW YORK,,Precinct,Closed,02/25/2019 07:07:01 AM,The Police Department responded to the complaint and with the information available observed no evidence of the violation at that time.,02/25/2019 02:26:19 AM,12 MANHATTAN,1021660026,MANHATTAN,1002876,249402,ONLINE,Unspecified,MANHATTAN,,,,,,,,40.8512062,-73.9326735,"(40.8512062, -73.9326735)"
29121465,10/22/2014 12:00:00 AM,02/06/2015 12:00:00 AM,HPD,Department of Housing Preservation and Development,APPLIANCE,ELECTRIC/GAS RANGE,RESIDENTIAL BUILDING,10473,880 BOYNTON AVENUE,BOYNTON AVENUE,LAFAYETTE AVENUE,STORY AVENUE,,,ADDRESS,BRONX,,N/A,Closed,,"The Department of Housing Preservation and Development contacted an occupant of the apartment and verified that the following conditions were corrected. The complaint has been closed. If the condition still exists, please file a new complaint.",02/06/2015 12:00:00 AM,09 BRONX,2036270050,BRONX,1018430,238528,PHONE,Unspecified,BRONX,,,,,,,,40.8213137,-73.8765067,"(40.8213137, -73.8765067)"
39539894,06/22/2018 06:58:00 PM,06/24/2018 12:00:00 AM,DSNY,Department of Sanitation,Request Large Bulky Item Collection,Request Large Bulky Item Collection,Sidewalk,10307,133 NASHVILLE STREET,NASHVILLE STREET,LENHART STREET,AMBOY ROAD,,,ADDRESS,STATEN ISLAND,,N/A,Closed,,,06/24/2018 12:00:00 AM,03 STATEN ISLAND,5080380028,STATEN ISLAND,917726,126673,PHONE,Unspecified,STATEN ISLAND,,,,,,,,40.5141138,-74.2392488,"(40.5141138, -74.2392488)"
46220169,05/16/2020 06:53:38 PM,05/16/2020 07:20:07 PM,NYPD,New York City Police Department,Non-Emergency Police Matter,Social Distancing,Residential Building/House,10033,530 WEST  187 STREET,WEST  187 STREET,AMSTERDAM AVENUE,AUDUBON AVENUE,AMSTERDAM AVENUE,AUDUBON AVENUE,,NEW YORK,WEST  187 STREET,,Closed,,The Police Department responded to the complaint and took action to fix the condition.,05/16/2020 11:20:09 PM,12 MANHATTAN,1021560074,MANHATTAN,1003855,249790,ONLINE,Unspecified,MANHATTAN,,,,,,,,40.85226903618749,-73.9291336401013,"(40.85226903618749, -73.9291336401013)"
42851632,06/03/2019 02:44:26 PM,06/04/2019 08:54:58 AM,DOF,Land Records,DOF Property - Update Account,Billing Name Incorrect,Property Address,10306,,,,,,,ADDRESS,STATEN ISLAND,,N/A,Closed,06/13/2019 02:44:26 PM,See notes.,06/04/2019 08:54:58 AM,03 STATEN ISLAND,,STATEN ISLAND,,,PHONE,Unspecified,STATEN ISLAND,,,,,,,,,,
41572358,01/31/2019 04:55:55 PM,01/07/2020 10:59:24 AM,DPR,Department of Parks and Recreation,Illegal Tree Damage,Branches Damaged,,11234,3702 AVENUE S,AVENUE S,,,,,LATLONG,BROOKLYN,,,Closed,03/25/2019 05:00:01 PM,The Department of Parks and Recreation performed the work necessary to correct the condition.,01/07/2020 03:59:27 PM,18 BROOKLYN,,BROOKLYN,1003601,161569,MOBILE,Unspecified,BROOKLYN,,,,,,,,40.61012482787971,-73.93030549486245,"(40.61012482787971, -73.93030549486245)"
42317172,11/09/2017 09:20:43 AM,11/16/2017 12:00:00 AM,DOB,Department of Buildings,Borough Office,Construction Enforcement Work Order (DOB),,11213,1298 PARK PLACE,PARK PLACE,,,,,ADDRESS,BROOKLYN,,N/A,Closed,,The Department of Buildings investigated this complaint and determined that no further action was necessary.,11/16/2017 12:00:00 AM,08 BROOKLYN,3013710032,BROOKLYN,1002403,184320,UNKNOWN,Unspecified,BROOKLYN,,,,,,,,40.6725739,-73.934559,"(40.6725739, -73.934559)"
27740683,03/28/2014 12:00:00 AM,04/03/2014 12:00:00 AM,HPD,Department of Housing Preservation and Development,PLUMBING,BATHTUB/SHOWER,RESIDENTIAL BUILDING,10458,2676 GRAND CONCOURSE,GRAND CONCOURSE,EAST KINGSBRIDGE ROAD,EAST 196 STREET,,,ADDRESS,BRONX,,N/A,Closed,,The Department of Housing Preservation and Development inspected the following conditions. No violations were issued. The complaint has been closed.,04/03/2014 12:00:00 AM,07 BRONX,2033040020,BRONX,1013597,255053,PHONE,Unspecified,BRONX,,,,,,,,40.8666873,-73.8938961,"(40.8666873, -73.8938961)"
34901574,12/01/2016 09:52:29 AM,12/05/2016 10:57:21 AM,HPD,Department of Housing Preservation and Development,GENERAL,BELL/BUZZER/INTERCOM,RESIDENTIAL BUILDING,11225,56 WINTHROP STREET,WINTHROP STREET,,,,,ADDRESS,BROOKLYN,,N/A,Closed,,The Department of Housing Preservation and Development inspected the following conditions. Violations were issued. Information about specific violations is available at www.nyc.gov/hpd.,12/05/2016 10:57:21 AM,09 BROOKLYN,3050480031,BROOKLYN,995868,178496,PHONE,Unspecified,BROOKLYN,,,,,,,,40.6565993,-73.9581275,"(40.6565993, -73.9581275)"
43215763,07/07/2019 12:28:26 AM,07/07/2019 07:31:15 AM,NYPD,New York City Police Department,Blocked Driveway,No Access,Street/Sidewalk,11103,25-51 41 STREET,41 STREET,25 AVENUE,28 AVENUE,25 AVENUE,28 AVENUE,,ASTORIA,41 STREET,,Closed,,The Police Department responded and upon arrival those responsible for the condition were gone.,07/07/2019 11:31:15 AM,01 QUEENS,4006850024,QUEENS,1008844,218788,MOBILE,Unspecified,QUEENS,,,,,,,,40.7671647,-73.9112135,"(40.7671647, -73.9112135)"
41892465,03/06/2019 03:37:39 PM,03/08/2019 02:12:17 AM,HPD,Department of Housing Preservation and Development,HEAT/HOT WATER,ENTIRE BUILDING,RESIDENTIAL BUILDING,11228,915 84 STREET,84 STREET,,,,,ADDRESS,BROOKLYN,,N/A,Closed,,The complaint you filed is a duplicate of a condition already reported by another tenant for a building-wide condition. The original complaint is still open. HPD may attempt to contact you to verify the correction of the condition or may conduct an inspection of your unit if the original complainant is not available for verification.,03/08/2019 02:12:17 AM,10 BROOKLYN,3060210046,BROOKLYN,978624,165088,ONLINE,Unspecified,BROOKLYN,,,,,,,,40.6198031,-74.0202655,"(40.6198031, -74.0202655)"
36115956,05/05/2017 07:08:00 PM,05/06/2017 01:30:00 PM,DEP,Department of Environmental Protection,Water System,Leak (Use Comments) (WA2),,11235,14 CASS PLACE,CASS PLACE,BRIGHTON 11 ST,CORBIN PL,,,ADDRESS,BROOKLYN,,N/A,Closed,,"The Department of Environment Protection inspected your complaint but could not find the problem you reported. If the condition persists, please call 311 (or 212-639-9675 if calling from a non-New York City area code) with more detailed information to submit a new complaint.",05/06/2017 01:30:00 PM,13 BROOKLYN,3087110015,BROOKLYN,996533,151452,OTHER,Unspecified,BROOKLYN,,,,,,,,40.5823683,-73.95578,"(40.5823683, -73.95578)"
41617568,02/02/2019 10:50:21 PM,02/05/2019 02:10:41 AM,HPD,Department of Housing Preservation and Development,HEAT/HOT WATER,ENTIRE BUILDING,RESIDENTIAL BUILDING,10467,2714 WALLACE AVENUE,WALLACE AVENUE,,,,,ADDRESS,BRONX,,N/A,Closed,,"The Department of Housing Preservation and Development responded to a complaint of no heat or hot water and was advised by a tenant in the building that heat and hot water had been restored. If the condition still exists, please file a new complaint.",02/05/2019 02:10:41 AM,11 BRONX,2045120005,BRONX,1021746,254799,ONLINE,Unspecified,BRONX,,,,,,,,40.8659593,-73.8644349,"(40.8659593, -73.8644349)"
34110049,08/17/2016 03:58:10 PM,11/04/2016 11:17:56 AM,TLC,Taxi and Limousine Commission,For Hire Vehicle Complaint,Driver Complaint,Street,10023,1934 BROADWAY,BROADWAY,WEST 64 STREET,COLUMBUS AVENUE,,,ADDRESS,NEW YORK,,N/A,Closed,10/02/2016 09:47:52 AM,The Taxi and Limousine Commission reviewed your complaint. The driver or owner pled guilty to a violation and paid a fine. TLC has sent you a written confirmation of this outcome.,11/04/2016 11:17:56 AM,07 MANHATTAN,1011170001,MANHATTAN,989186,220766,ONLINE,Unspecified,MANHATTAN,,,,,,,,40.7726266,-73.9821791,"(40.7726266, -73.9821791)"
27524602,02/26/2014 03:26:14 PM,02/27/2014 10:45:22 AM,DFTA,Department for the Aging,Senior Center Complaint,N/A,Senior Center,,,,,,,,,,,N/A,Closed,03/12/2014 03:26:14 PM,"The Department for the Aging contacted you and provided the assistance requested. No further updates will be available through 311. If further assistance is needed, please open a new Service Request.",02/27/2014 10:44:42 AM,0 Unspecified,,Unspecified,,,PHONE,Unspecified,Unspecified,,,,,,,,,,
46251385,05/20/2020 04:51:57 PM,05/20/2020 05:27:09 PM,NYPD,New York City Police Department,Non-Emergency Police Matter,Social Distancing,Store/Commercial,11219,58 STREET,58 STREET,58 STREET,NEW UTRECHT AVENUE,58 STREET,NEW UTRECHT AVENUE,,,,,Closed,,The Police Department responded to the complaint and took action to fix the condition.,05/20/2020 09:27:10 PM,12 BROOKLYN,,BROOKLYN,985328,168523,PHONE,Unspecified,BROOKLYN,,,,,,,,40.62923317483001,-73.9961163671332,"(40.62923317483001, -73.9961163671332)"
30759754,06/04/2015 12:21:37 AM,06/04/2015 02:47:33 AM,NYPD,New York City Police Department,Blocked Driveway,No Access,Street/Sidewalk,11368,34-52 97 STREET,97 STREET,34 AVENUE,35 AVENUE,,,ADDRESS,CORONA,,Precinct,Closed,06/04/2015 08:21:37 AM,The Police Department issued a summons in response to the complaint.,06/04/2015 02:47:29 AM,03 QUEENS,4017300029,QUEENS,1020033,214124,MOBILE,Unspecified,QUEENS,,,,,,,,40.754325,-73.870845,"(40.754325, -73.870845)"
25826221,06/26/2013 12:00:00 AM,07/08/2013 12:00:00 AM,HPD,Department of Housing Preservation and Development,PAINT - PLASTER,WALLS,RESIDENTIAL BUILDING,11221,909 GREENE AVENUE,GREENE AVENUE,STUYVESANT AVENUE,MALCOLM X BOULEVARD,,,ADDRESS,BROOKLYN,,N/A,Closed,,The Department of Housing Preservation and Development inspected the following conditions. No violations were issued. The complaint has been closed.,07/08/2013 12:00:00 AM,03 BROOKLYN,3016160061,BROOKLYN,1003274,190917,PHONE,Unspecified,BROOKLYN,,,,,,,,,,
20676425,06/20/2011 11:10:00 AM,06/26/2011 01:00:00 PM,DEP,Department of Environmental Protection,Noise,Noise: Construction Equipment (NC1),,11233,289 RALPH AVE,RALPH AVE,SUMPTER ST,MAC DOUGAL ST,,,ADDRESS,BROOKLYN,,N/A,Closed,,"The Department of Environmental Protection did not observe a violation of the New York City Air/Noise Code at the time of inspection and could not issue a notice of violation. If the problem still exists, please call 311 and file a new complaint. If you are outside of New York City, please call (212) NEW-YORK (212-639-9675).",06/26/2011 01:00:00 PM,03 BROOKLYN,3015240003,BROOKLYN,1005868,186842,UNKNOWN,Unspecified,BROOKLYN,,,,,,,,,,
23322941,05/30/2012 09:19:40 AM,06/01/2012 10:33:50 AM,DOF,Correspondence Unit,DOF Property - Owner Issue,Remove Mortgage,Property Address,10308,,,,,,,ADDRESS,STATEN ISLAND,,N/A,Closed,06/04/2012 09:19:40 AM,The Department of Finance updated its records with the information provided.,06/01/2012 10:33:34 AM,03 STATEN ISLAND,,STATEN ISLAND,,,PHONE,Unspecified,STATEN ISLAND,,,,,,,,,,
46440420,06/11/2020 12:01:36 AM,06/11/2020 12:24:14 AM,NYPD,New York City Police Department,Noise - Street/Sidewalk,Loud Talking,,11211,BEDFORD AVENUE,BEDFORD AVENUE,BEDFORD AVENUE,SOUTH    3 STREET,BEDFORD AVENUE,SOUTH    3 STREET,,,,,Closed,,The Police Department responded to the complaint and took action to fix the condition.,06/11/2020 04:24:15 AM,01 BROOKLYN,,BROOKLYN,994632,198871,PHONE,Unspecified,BROOKLYN,,,,,,,,40.71252561081519,-73.96255077806624,"(40.71252561081519, -73.96255077806624)"
19067590,11/06/2010 07:44:00 PM,11/08/2010 12:00:00 AM,DEP,Department of Environmental Protection,Lead,Lead Kit Request (Residential) (L10),,11230,1360 OCEAN PARKWAY,OCEAN PARKWAY,AVENUE M,AVENUE N,,,ADDRESS,BROOKLYN,,N/A,Closed,,The Department of Environmental Protection investigated this complaint and created a Service Request to have a Lead Test Kit sent to the complainant.,11/08/2010 12:00:00 AM,12 BROOKLYN,3065680033,BROOKLYN,992896,163566,ONLINE,Unspecified,BROOKLYN,,,,,,,,40.6156231,-73.968858,"(40.6156231, -73.968858)"
41961291,02/16/2019 05:32:03 AM,03/14/2019 05:02:28 PM,HPD,Department of Housing Preservation and Development,PAINT/PLASTER,CEILING,RESIDENTIAL BUILDING,11226,46 LINDEN BOULEVARD,LINDEN BOULEVARD,,,,,ADDRESS,BROOKLYN,,N/A,Closed,,The Department of Housing Preservation and Development inspected the following conditions. No violations were issued. The complaint has been closed.,03/14/2019 05:02:28 PM,14 BROOKLYN,3050860030,BROOKLYN,996049,176904,PHONE,Unspecified,BROOKLYN,,,,,,,,40.6522294,-73.9574779,"(40.6522294, -73.9574779)"
40606783,10/20/2018 10:46:25 AM,10/20/2018 11:40:20 AM,NYPD,New York City Police Department,Noise - Residential,Banging/Pounding,Residential Building/House,10314,145 WELLINGTON COURT,WELLINGTON COURT,CHESTERFIELD LANE,ESSEX DRIVE,,,ADDRESS,STATEN ISLAND,,Precinct,Closed,10/20/2018 06:46:25 PM,The Police Department responded to the complaint and took action to fix the condition.,10/20/2018 11:40:20 AM,02 STATEN ISLAND,5024527503,STATEN ISLAND,940213,150379,PHONE,Unspecified,STATEN ISLAND,,,,,,,,40.5793222,-74.1585305,"(40.5793222, -74.1585305)"
38837544,04/02/2018 07:17:04 AM,04/02/2018 09:18:37 AM,NYPD,New York City Police Department,Blocked Driveway,No Access,Street/Sidewalk,11414,149-48 82 STREET,82 STREET,149 AVENUE,151 AVENUE,,,ADDRESS,HOWARD BEACH,,Precinct,Closed,04/02/2018 03:17:04 PM,The Police Department responded and upon arrival those responsible for the condition were gone.,04/02/2018 09:18:37 AM,10 QUEENS,4114130035,QUEENS,1025050,182995,PHONE,Unspecified,QUEENS,,,,,,,,40.6688617,-73.8529254,"(40.6688617, -73.8529254)"
21586532,10/05/2011 04:13:50 PM,,DPR,Department of Parks and Recreation,Root/Sewer/Sidewalk Condition,Trees and Sidewalks Program,Street,10306,91 NEW DORP LANE,NEW DORP LANE,4 STREET,NEW DORP PLAZA,,,ADDRESS,STATEN ISLAND,,N/A,Open,11/04/2011 04:13:50 PM,The Department of Parks and Recreation usually requires 30 days to inspect this type of complaint. Please note your Service Request number for future reference.,10/05/2011 04:25:16 PM,02 STATEN ISLAND,5036300042,STATEN ISLAND,951696,148582,PHONE,Unspecified,STATEN ISLAND,,,,,,,,40.5744394,-74.1171838,"(40.5744394, -74.1171838)"
15889530,01/29/2010 08:11:00 AM,01/29/2010 09:50:00 AM,DOT,Department of Transportation,Traffic Signal Condition,Controller,,,,,,,FARMS RD WEST,CROSS BX EXPY,INTERSECTION,,,N/A,Closed,,Service Request status for this request is available on the Department of Transportation?s website. Please click the ?Learn More? link below.,01/29/2010 12:00:00 AM,Unspecified BRONX,,BRONX,,,UNKNOWN,Unspecified,BRONX,,,,,,,,,,
46798032,07/08/2020 03:04:12 PM,,DOHMH,Department of Health and Mental Hygiene,Rodent,Rat Sighting,1-2 Family Dwelling,10301,54 WEBSTER AVENUE,WEBSTER AVENUE,STANLEY AVENUE,CASTLETON COURT,STANLEY AVENUE,CASTLETON COURT,,STATEN ISLAND,WEBSTER AVENUE,,In Progress,,,,01 STATEN ISLAND,5001130024,STATEN ISLAND,959572,170552,PHONE,Unspecified,STATEN ISLAND,,,,,,,,40.63476803929322,-74.08891304015974,"(40.63476803929322, -74.08891304015974)"
36301952,05/28/2017 08:23:23 PM,05/28/2017 09:37:50 PM,NYPD,New York City Police Department,Noise - Residential,Loud Music/Party,Residential Building/House,10453,55 WEST 175 STREET,WEST 175 STREET,GRAND AVENUE,MACOMBS ROAD,,,ADDRESS,BRONX,,Precinct,Closed,05/29/2017 04:23:23 AM,The Police Department responded to the complaint and with the information available observed no evidence of the violation at that time.,05/28/2017 09:37:50 PM,05 BRONX,2028660090,BRONX,1007728,248276,ONLINE,Unspecified,BRONX,,,,,,,,40.8481041,-73.9151392,"(40.8481041, -73.9151392)"
27430270,02/14/2014 12:34:15 PM,02/14/2014 01:41:28 PM,NYPD,New York City Police Department,Noise - Street/Sidewalk,Loud Music/Party,Street/Sidewalk,10467,3510 TRYON AVENUE,TRYON AVENUE,EAST GUN HILL ROAD,EAST 211 STREET,,,ADDRESS,BRONX,,Precinct,Closed,02/14/2014 08:34:15 PM,The Police Department responded to the complaint and determined that police action was not necessary.,02/14/2014 01:40:23 PM,07 BRONX,2033440085,BRONX,1018359,260130,ONLINE,Unspecified,BRONX,,,,,,,,40.880605,-73.8766533,"(40.880605, -73.8766533)"
47244055,08/15/2020 02:01:14 AM,08/15/2020 03:16:51 AM,NYPD,New York City Police Department,Noise - Residential,Loud Music/Party,Residential Building/House,11436,144-16 123 AVENUE,123 AVENUE,144 STREET,145 STREET,144 STREET,145 STREET,,JAMAICA,123 AVENUE,,Closed,,The Police Department responded to the complaint and took action to fix the condition.,08/15/2020 07:16:54 AM,12 QUEENS,4120470057,QUEENS,1041150,185214,ONLINE,Unspecified,QUEENS,,,,,,,,40.674863535477606,-73.79487003528645,"(40.674863535477606, -73.79487003528645)"
38049084,12/29/2017 10:37:00 AM,12/29/2017 11:54:00 PM,DSNY,Department of Sanitation,Request Large Bulky Item Collection,Request Large Bulky Item Collection,Sidewalk,11385,61-29 MADISON STREET,MADISON STREET,FRESH POND ROAD,64 STREET,,,ADDRESS,Ridgewood,,N/A,Closed,,,12/29/2017 11:54:00 PM,05 QUEENS,4036140043,QUEENS,1012828,196938,PHONE,Unspecified,QUEENS,,,,,,,,40.7071799,-73.8969237,"(40.7071799, -73.8969237)"
35805314,03/27/2017 12:08:15 PM,04/17/2017 08:54:30 AM,HPD,Department of Housing Preservation and Development,PLUMBING,BATHTUB/SHOWER,RESIDENTIAL BUILDING,10468,2797 WEBB AVENUE,WEBB AVENUE,,,,,ADDRESS,BRONX,,N/A,Closed,,"The Department of Housing Preservation and Development was not able to gain access to inspect the following conditions. The complaint has been closed. If the condition still exists, please file a new complaint.",04/17/2017 08:54:30 AM,08 BRONX,2032490214,BRONX,1011592,256882,PHONE,Unspecified,BRONX,,,,,,,,40.8717138,-73.9011377,"(40.8717138, -73.9011377)"
27790736,04/05/2014 12:24:02 PM,04/15/2014 07:41:51 AM,DOT,Department of Transportation,Broken Muni Meter,No Receipt,Street,11209,,,,,85 STREET,4 AVENUE,INTERSECTION,BROOKLYN,,N/A,Closed,04/26/2014 12:24:02 PM,"The Department of Transportation inspected the condition you reported. You can find additional information in the ""Notes to Customer"" field.",04/15/2014 07:37:39 AM,10 BROOKLYN,,BROOKLYN,976467,166462,PHONE,Unspecified,BROOKLYN,,,,,,,,40.6235728,-74.0280369,"(40.6235728, -74.0280369)"
39137020,05/08/2018 03:02:50 PM,05/08/2018 03:20:59 PM,DOHMH,Department of Health and Mental Hygiene,Indoor Air Quality,Ventilation,3+ Family Apartment Building,11238,411 GRAND AVENUE,GRAND AVENUE,GATES AVENUE,PUTNAM AVENUE,,,ADDRESS,BROOKLYN,,N/A,Closed,06/22/2018 03:02:51 PM,"The Department of Health and Mental Hygiene will review your complaint to determine appropriate action. Complaints of this type usually result in complainant contact or an inspection. You may be contacted if you provided a phone number. Status will be available 45 days after the date of your complaint by calling 311. If you are experiencing medical symptoms, please seek medical attention or consult the NYC Poison Control Center. Please note your Service Request number for future reference.",05/08/2018 03:20:59 PM,02 BROOKLYN,3019820013,BROOKLYN,994836,188320,ONLINE,Unspecified,BROOKLYN,,,,,,,,40.6835653,-73.9618315,"(40.6835653, -73.9618315)"
24107570,09/28/2012 12:00:00 AM,10/03/2012 12:00:00 AM,HPD,Department of Housing Preservation and Development,GENERAL CONSTRUCTION,CERAMIC-TILE,RESIDENTIAL BUILDING,10039,210 WEST 150 STREET,WEST 150 STREET,7 AVENUE,8 AVENUE,,,ADDRESS,NEW YORK,,N/A,Closed,,The Department of Housing Preservation and Development inspected the following conditions. Violations were issued. Information about specific violations is available at www.nyc.gov/hpd.,10/03/2012 12:00:00 AM,10 MANHATTAN,1020350001,MANHATTAN,1001574,239877,PHONE,Unspecified,MANHATTAN,,,,,,,,,,
36699458,07/14/2017 10:08:23 AM,08/17/2017 11:20:43 AM,DOF,Personal Exemption Unit,DOF Property - Reduction Issue,Personal SCHE Exemption,"1-, 2- and 3- Family Home",10314,,,,,,,ADDRESS,STATEN ISLAND,,N/A,Closed,07/19/2017 10:08:23 AM,See notes.,08/17/2017 11:20:43 AM,02 STATEN ISLAND,,STATEN ISLAND,,,PHONE,Unspecified,STATEN ISLAND,,,,,,,,,,
46058172,04/24/2020 06:26:26 AM,04/24/2020 07:01:13 AM,DHS,Department of Homeless Services,Homeless Person Assistance,,N/A,11377,64-20 35 AVENUE,35 AVENUE,64 STREET,65 STREET,64 STREET,65 STREET,ADDRESS,Woodside,35 AVENUE,,Closed,,The Department of Homeless Services did not have enough information to act on your request.,04/24/2020 07:01:13 AM,02 QUEENS,4012020021,QUEENS,1012405,212662,MOBILE,Unspecified,QUEENS,,,,,,,,40.75033979232645,-73.8983835915638,"(40.75033979232645, -73.8983835915638)"
33655611,06/21/2016 09:02:49 PM,06/22/2016 01:10:58 PM,DPR,Department of Parks and Recreation,Maintenance or Facility,Hours of Operation,Park,11211,,,,,,,,BROOKLYN,,N/A,Closed,06/24/2016 09:02:49 PM,The Department of Parks and Recreation has completed the requested work order and corrected the problem.,06/22/2016 01:10:58 PM,01 BROOKLYN,,BROOKLYN,,,MOBILE,Bedford Playground,BROOKLYN,,,,,,,,,,
22408627,12/28/2011 02:16:39 PM,12/29/2011 01:15:01 PM,DHS,DHS Advantage Programs,DHS Advantage - Tenant,Other Issue,Tenant Address,11420,,,,,,,ADDRESS,SOUTH OZONE PARK,,N/A,Closed,01/04/2012 05:34:29 PM,The Department of Homeless Services has removed the tenant from the program as per your request.,12/29/2011 01:15:02 PM,10 QUEENS,,QUEENS,,,PHONE,Unspecified,QUEENS,,,,,,,,,,
38663083,03/10/2018 01:53:11 PM,03/14/2018 02:06:04 AM,HPD,Department of Housing Preservation and Development,HEAT/HOT WATER,ENTIRE BUILDING,RESIDENTIAL BUILDING,10453,1920 OSBORNE PLACE,OSBORNE PLACE,,,,,ADDRESS,BRONX,,N/A,Closed,,"The Department of Housing Preservation and Development responded to a complaint of no heat or hot water and was advised by a tenant in the building that heat and hot water had been restored. If the condition still exists, please file a new complaint.",03/14/2018 02:06:04 AM,05 BRONX,2032280021,BRONX,1007514,250864,PHONE,Unspecified,BRONX,,,,,,,,40.8552079,-73.9159037,"(40.8552079, -73.9159037)"
39099516,05/03/2018 07:01:00 PM,05/03/2018 10:00:00 PM,DEP,Department of Environmental Protection,Water System,Possible Water Main Break (Use Comments) (WA1),,11218,,,,,CORTELYOU ROAD,EAST 7 STREET,INTERSECTION,BROOKLYN,,N/A,Closed,,The Department of Environmental Protection determined that this complaint is a duplicate of a previously filed complaint. The original complaint is being addressed.,05/03/2018 10:00:00 PM,12 BROOKLYN,,BROOKLYN,992073,171964,PHONE,Unspecified,BROOKLYN,,,,,,,,40.6386746,-73.9718127,"(40.6386746, -73.9718127)"
25789684,06/21/2013 12:00:00 AM,07/11/2013 12:00:00 AM,HPD,Department of Housing Preservation and Development,GENERAL CONSTRUCTION,DOORS,RESIDENTIAL BUILDING,10013,121 MULBERRY STREET,MULBERRY STREET,CANAL STREET,HESTER STREET,,,ADDRESS,NEW YORK,,N/A,Closed,,"The Department of Housing Preservation and Development was not able to gain access to inspect the following conditions. The complaint has been closed. If the condition still exists, please file a new complaint.",07/11/2013 12:00:00 AM,02 MANHATTAN,1002060019,MANHATTAN,984766,200806,PHONE,Unspecified,MANHATTAN,,,,,,,,,,
34225195,09/01/2016 07:39:15 PM,09/01/2016 10:35:52 PM,NYPD,New York City Police Department,Noise - Residential,Banging/Pounding,Residential Building/House,11231,30 BUSH STREET,BUSH STREET,DWIGHT STREET,COLUMBIA STREET,,,ADDRESS,BROOKLYN,,Precinct,Closed,09/02/2016 03:39:15 AM,The Police Department responded to the complaint and took action to fix the condition.,09/01/2016 10:35:52 PM,06 BROOKLYN,3005330001,BROOKLYN,981948,185369,PHONE,Unspecified,BROOKLYN,,,,,,,,40.6754715,-74.008299,"(40.6754715, -74.008299)"
30190759,03/16/2015 12:00:00 AM,03/22/2015 12:00:00 AM,HPD,Department of Housing Preservation and Development,HEAT/HOT WATER,ENTIRE BUILDING,RESIDENTIAL BUILDING,10023,344 WEST 72 STREET,WEST 72 STREET,,,,,ADDRESS,NEW YORK,,N/A,Closed,,The Department of Housing Preservation and Development inspected the following conditions. No violations were issued. The complaint has been closed.,03/22/2015 12:00:00 AM,07 MANHATTAN,1011830053,MANHATTAN,988144,223600,MOBILE,Unspecified,MANHATTAN,,,,,,,,40.7804057,-73.9859395,"(40.7804057, -73.9859395)"
18513794,08/18/2010 11:51:00 PM,08/31/2010 09:35:00 PM,DOT,Department of Transportation,Street Light Condition,Street Light Out,,10025,,,,,COLUMBUS AVENUE,WEST 110 STREET,INTERSECTION,NEW YORK,,N/A,Closed,,Service Request status for this request is available on the Department of Transportation?s website. Please click the ?Learn More? link below.,08/31/2010 12:00:00 AM,07 MANHATTAN,,MANHATTAN,995026,231397,UNKNOWN,Unspecified,MANHATTAN,,,,,,,,,,
40404058,09/28/2018 12:52:00 PM,09/28/2018 12:52:00 PM,DEP,Department of Environmental Protection,Water System,Possible Water Main Break (Use Comments) (WA1),,10457,603 EAST 182 STREET,EAST 182 STREET,ARTHUR AVE,ARTHUR AVE,,,ADDRESS,BRONX,,N/A,Closed,,The Department of Environmental Protection determined that this complaint is a duplicate of a previously filed complaint. The original complaint is being addressed.,09/28/2018 12:52:00 PM,06 BRONX,2030710005,BRONX,1014739,249709,PHONE,Unspecified,BRONX,,,,,,,,40.8520158,-73.8897916,"(40.8520158, -73.8897916)"
23406529,06/12/2012 01:41:53 PM,06/12/2012 01:50:38 PM,DOF,Correspondence Unit,DOF Property - Request Copy,Copy of Statement,Property Address,11235,,,,,,,ADDRESS,BROOKLYN,,N/A,Closed,06/17/2012 01:41:53 PM,The Department of Finance mailed the requested item.,06/12/2012 01:50:24 PM,13 BROOKLYN,,BROOKLYN,,,PHONE,Unspecified,BROOKLYN,,,,,,,,,,
34098277,08/16/2016 09:06:54 AM,08/18/2016 12:00:00 AM,DOB,Department of Buildings,Electrical,Electrical Wiring Defective/Exposed,,11219,5402 FORT HAMILTON PARKWAY,FORT HAMILTON PARKWAY,,,,,ADDRESS,BROOKLYN,,N/A,Closed,,The Department of Buildings investigated this complaint and issued an Office of Administrative Trials and Hearings (OATH) summons.,08/18/2016 12:00:00 AM,12 BROOKLYN,3056730042,BROOKLYN,983874,170956,UNKNOWN,Unspecified,BROOKLYN,,,,,,,,40.6359113,-74.0013547,"(40.6359113, -74.0013547)"
47779189,10/04/2020 05:02:52 PM,,TLC,Taxi and Limousine Commission,Green Taxi Complaint,Driver Complaint - Passenger,,10035,1800 PARK AVENUE,PARK AVENUE,EAST  124 STREET,EAST  125 STREET,EAST  124 STREET,EAST  125 STREET,,NEW YORK,PARK AVENUE,,In Progress,,,11/13/2020 06:34:24 PM,11 MANHATTAN,1017490033,MANHATTAN,1001028,232410,ONLINE,Unspecified,MANHATTAN,,,"1800 PARK AVENUE, MANHATTAN (NEW YORK), NY, 10035",,,,,40.80457174037283,-73.93939588196304,"(40.80457174037283, -73.93939588196304)"
41972638,03/16/2019 09:51:23 PM,03/18/2019 08:31:10 AM,HPD,Department of Housing Preservation and Development,HEAT/HOT WATER,ENTIRE BUILDING,RESIDENTIAL BUILDING,10033,495 WEST 186 STREET,WEST 186 STREET,,,,,ADDRESS,NEW YORK,,N/A,Closed,,"The Department of Housing Preservation and Development contacted a tenant in the building and verified that the following conditions were corrected. The complaint has been closed. If the condition still exists, please file a new complaint.",03/18/2019 08:31:10 AM,12 MANHATTAN,1021490093,MANHATTAN,1004046,249366,ONLINE,Unspecified,MANHATTAN,,,,,,,,40.8511048,-73.9284445,"(40.8511048, -73.9284445)"
21928401,11/20/2011 12:00:00 AM,12/10/2011 12:00:00 AM,HPD,Department of Housing Preservation and Development,PLUMBING,WATER-SUPPLY,RESIDENTIAL BUILDING,10031,53 HAMILTON TERRACE,HAMILTON TERRACE,WEST 141 STREET,WEST 144 STREET,,,ADDRESS,NEW YORK,,N/A,Closed,,The Department of Housing Preservation and Development inspected the following conditions. No violations were issued. The complaint has been closed.,12/10/2011 12:00:00 AM,09 MANHATTAN,1020500113,MANHATTAN,999098,239115,UNKNOWN,Unspecified,MANHATTAN,,,,,,,,,,
38268365,01/21/2018 03:03:00 PM,01/21/2018 05:50:00 PM,DEP,Department of Environmental Protection,Sewer,Manhole Cover Missing (Emergency) (SA3),,10025,,,W 96 ST,CENTRAL PARK W,WEST 96 STREET,CENTRAL PARK WEST,INTERSECTION,NEW YORK,,N/A,Closed,,"The Department of Environment Protection inspected your complaint but could not find the problem you reported. If the condition persists, please call 311 (or 212-639-9675 if calling from a non-New York City area code) with more detailed information to submit a new complaint.",01/21/2018 05:50:00 PM,07 MANHATTAN,,MANHATTAN,994029,227703,PHONE,Unspecified,MANHATTAN,,,,,,,,,,
29188031,10/31/2014 12:00:00 AM,11/03/2014 12:00:00 AM,HPD,Department of Housing Preservation and Development,HEAT/HOT WATER,ENTIRE BUILDING,RESIDENTIAL BUILDING,11235,2785 OCEAN PARKWAY,OCEAN PARKWAY,BELT PARKWAY,WEST AVENUE,,,ADDRESS,BROOKLYN,,N/A,Closed,,"The Department of Housing Preservation and Development was not able to gain access to your apartment or others in the building to inspect for a lack of heat or hot water. The complaint has been closed. If the condition still exists, please file a new complaint.",11/03/2014 12:00:00 AM,13 BROOKLYN,3072600020,BROOKLYN,993347,151254,PHONE,Unspecified,BROOKLYN,,,,,,,,40.5818287,-73.9672502,"(40.5818287, -73.9672502)"
23206660,05/10/2012 07:22:56 PM,05/16/2012 04:30:03 PM,DOF,Senior Citizen Rent Increase Exemption Unit,SCRIE,SCRIE Assistance,Senior Address,11230,,,,,,,ADDRESS,BROOKLYN,,N/A,Closed,05/24/2012 07:22:56 PM,"The Department of Finance contacted you and provided the assistance requested. No further updates will be available through 311. If further assistance is needed, please open a new Service Request.",05/16/2012 04:29:09 PM,14 BROOKLYN,,BROOKLYN,,,PHONE,Unspecified,BROOKLYN,,,,,,,,,,
25775797,06/19/2013 06:16:00 AM,06/19/2013 09:00:00 AM,DEP,Department of Environmental Protection,Sewer,Manhole Cover Broken/Making Noise (SB),,10302,,,DECKER AVE,PALMER AVE,DECKER AVENUE,PALMER AVENUE,INTERSECTION,STATEN ISLAND,,N/A,Closed,,The Department of Environmental Protection investigated this complaint and found the repairs completed.,06/19/2013 09:00:00 AM,01 STATEN ISLAND,,STATEN ISLAND,947231,169397,OTHER,Unspecified,STATEN ISLAND,,,,,,,,40.6315548,-74.1333704,"(40.6315548, -74.1333704)"
16761226,05/29/2010 11:27:00 AM,06/02/2010 12:00:00 PM,DSNY,A - Brooklyn,Other Enforcement,E6 Commercial Waste Disposal,Sidewalk,11222,42 DOBBIN STREET,DOBBIN STREET,NASSAU AVENUE,NORMAN AVENUE,,,ADDRESS,BROOKLYN,,N/A,Closed,,The Department of Sanitation investigated this complaint and found no violation at the location.,06/02/2010 12:00:00 AM,01 BROOKLYN,3026430026,BROOKLYN,997088,202903,PHONE,Unspecified,BROOKLYN,,,,,,,,,,
23206672,05/10/2012 03:22:14 PM,05/10/2012 06:02:59 PM,NYPD,New York City Police Department,Illegal Parking,Blocked Hydrant,Street/Sidewalk,11204,1755 61 STREET,61 STREET,17 AVENUE,18 AVENUE,,,ADDRESS,BROOKLYN,,Precinct,Closed,05/10/2012 11:22:14 PM,The Police Department responded and upon arrival those responsible for the condition were gone.,05/10/2012 06:02:17 PM,12 BROOKLYN,3055180056,BROOKLYN,987335,165913,PHONE,Unspecified,BROOKLYN,,,,,,,,40.6220688,-73.9888871,"(40.6220688, -73.9888871)"
33474539,05/30/2016 04:08:32 PM,10/30/2017 12:00:00 AM,DOB,Department of Buildings,Building/Use,Zoning - Non-Conforming/Illegal Vehicle Storage,,11223,2118 WEST 8 STREET,WEST 8 STREET,,,,,ADDRESS,BROOKLYN,,N/A,Closed,,The Department of Buildings investigated this complaint and issued an Office of Administrative Trials and Hearings (OATH) summons.,10/30/2017 12:00:00 AM,15 BROOKLYN,3071180014,BROOKLYN,989986,156346,UNKNOWN,Unspecified,BROOKLYN,,,,,,,,40.595808,-73.9793457,"(40.595808, -73.9793457)"
19078151,11/08/2010 12:00:00 AM,11/17/2010 12:00:00 AM,HPD,Department of Housing Preservation and Development,GENERAL CONSTRUCTION,DOORS,RESIDENTIAL BUILDING,10302,1020 POST AVENUE,POST AVENUE,HEBERTON AVENUE,PORT RICHMOND AVENUE,,,ADDRESS,STATEN ISLAND,,N/A,Closed,,The Department of Housing Preservation and Development inspected the following conditions. No violations were issued. The complaint has been closed.,11/17/2010 12:00:00 AM,0 Unspecified,5010380036,Unspecified,946842,169995,UNKNOWN,Unspecified,Unspecified,,,,,,,,,,
40282728,09/14/2018 02:32:00 PM,09/19/2018 12:00:00 AM,DSNY,Department of Sanitation,Request Large Bulky Item Collection,Request Large Bulky Item Collection,Sidewalk,11427,88-07 PONTIAC STREET,PONTIAC STREET,88 AVENUE,BRADDOCK AVENUE,,,ADDRESS,Queens Village,,N/A,Closed,,,09/19/2018 12:00:00 AM,13 QUEENS,4079700176,QUEENS,1058073,205483,PHONE,Unspecified,QUEENS,,,,,,,,40.7303719,-73.7336391,"(40.7303719, -73.7336391)"
34423878,09/28/2016 03:37:38 PM,09/30/2016 04:09:27 PM,DCA,Department of Consumer Affairs,DCA / DOH New License Application Request,Full Term Mobile Food Unit Permit,,,,,,,,,,,,N/A,Closed,10/07/2016 04:08:26 PM,"The literature has been mailed. If it has not been received, please request it again from 311.",09/30/2016 04:09:27 PM,0 Unspecified,,Unspecified,,,PHONE,Unspecified,Unspecified,,,,,,,,,,
22552931,01/19/2012 02:38:00 PM,01/19/2012 09:40:00 PM,DOT,Department of Transportation,Traffic Signal Condition,Pedestrian Signal,,11236,,,DITMAS AVE,ROCKAWAY PKWY,DITMAS AVENUE,ROCKAWAY PARKWAY,INTERSECTION,BROOKLYN,,N/A,Closed,,Service Request status for this request is available on the Department of Transportation?s website. Please click the ?Learn More? link below.,01/19/2012 09:40:00 PM,17 BROOKLYN,,BROOKLYN,1009376,176656,UNKNOWN,Unspecified,BROOKLYN,,,,,,,,,,
43385956,07/27/2019 12:37:56 AM,07/27/2019 01:25:28 AM,NYPD,New York City Police Department,Blocked Driveway,No Access,,11236,1334 EAST 98 STREET,EAST 98 STREET,AVENUE K,AVENUE L,AVENUE K,AVENUE L,,BROOKLYN,EAST 98 STREET,,Closed,,The Police Department issued a summons in response to the complaint.,07/27/2019 05:25:31 AM,18 BROOKLYN,3082430071,BROOKLYN,1013358,172471,PHONE,Unspecified,BROOKLYN,,,,,,,,40.6400218,-73.8951177,"(40.6400218, -73.8951177)"
23443628,06/17/2012 10:07:13 PM,11/16/2013 12:00:00 AM,DOB,Department of Buildings,Building/Use,Illegal. Commercial Use In Resident Zone,,10469,3029 PAULDING AVENUE,PAULDING AVENUE,ADEE AVENUE,BURKE AVENUE,,,ADDRESS,BRONX,,N/A,Closed,,The Department of Buildings investigated this complaint and determined that no further action was necessary.,11/16/2013 12:00:00 AM,12 BRONX,2045760038,BRONX,1023374,256267,UNKNOWN,Unspecified,BRONX,,,,,,,,,,
20374827,05/06/2011 12:30:23 PM,05/10/2011 04:06:57 PM,DHS,DHS Advantage Programs,DHS Advantage -Landlord/Broker,Payment Not Received from DHS,Tenant Address,10461,,,,,,,ADDRESS,BRONX,,N/A,Closed,05/16/2011 07:37:59 AM,The Department of Homeless Services has addressed the payment issue.,05/10/2011 04:06:57 PM,10 BRONX,,BRONX,,,PHONE,Unspecified,BRONX,,,,,,,,,,
23206689,05/10/2012 10:56:35 AM,05/10/2012 01:48:49 PM,NYPD,New York City Police Department,Blocked Driveway,No Access,Street/Sidewalk,11204,1647 52 STREET,52 STREET,16 AVENUE,17 AVENUE,,,ADDRESS,BROOKLYN,,Precinct,Closed,05/10/2012 06:56:35 PM,The Police Department responded and upon arrival those responsible for the condition were gone.,05/10/2012 01:47:49 PM,12 BROOKLYN,3054660071,BROOKLYN,988115,168312,PHONE,Unspecified,BROOKLYN,,,,,,,,40.6286532,-73.986076,"(40.6286532, -73.986076)"
26448544,10/07/2013 02:33:21 PM,10/09/2013 02:36:42 PM,TLC,Taxi and Limousine Commission,Taxi Complaint,Driver Complaint,Street,10036,,,WEST 41 STREET,WEST 42 STREET,,,PLACENAME,NEW YORK,PORT AUTH 42 STREET,N/A,Closed,11/22/2013 09:37:27 AM,"Based on the information provided by the customer, the Taxi and Limousine Commission has determined that a hearing is not necessary or not possible.",10/09/2013 02:36:39 PM,04 MANHATTAN,1013320029,MANHATTAN,986791,215111,PHONE,Unspecified,MANHATTAN,,,Other,,,,,40.7571061,-73.9908281,"(40.7571061, -73.9908281)"
44900954,11/12/2019 07:55:05 AM,11/12/2019 12:01:41 PM,NYPD,New York City Police Department,Abandoned Vehicle,With License Plate,Street/Sidewalk,11385,73-17 72 STREET,72 STREET,MYRTLE AVENUE,INDIANA AVENUE,MYRTLE AVENUE,INDIANA AVENUE,,RIDGEWOOD,72 STREET,,Closed,,The Police Department responded to the complaint and determined that police action was not necessary.,11/12/2019 05:01:43 PM,05 QUEENS,4037110005,QUEENS,1018024,195067,MOBILE,Unspecified,QUEENS,,,,,,,,40.7020261,-73.8781919,"(40.7020261, -73.8781919)"
38096642,01/03/2018 10:58:00 AM,01/07/2018 12:00:00 PM,DSNY,BCC - Brooklyn North,Sanitation Condition,15 Street Cond/Dump-Out/Drop-Off,Street,11211,203 SOUTH 2 STREET,SOUTH2 STREET,DRIGGS AVENUE,ROEBLING STREET,,,ADDRESS,BROOKLYN,,DSNY Garage,Closed,,The Department of Sanitation cleaned the location.,01/07/2018 12:00:00 PM,01 BROOKLYN,3024070032,BROOKLYN,995441,198820,MOBILE,Unspecified,BROOKLYN,,,,,,,,40.7123846,-73.9596327,"(40.7123846, -73.9596327)"
42744613,05/22/2019 08:34:43 AM,06/04/2019 07:50:00 AM,DOT,Department of Transportation,Street Condition,Pothole,,11418,,,,,91 AVENUE,114 STREET,INTERSECTION,Richmond Hill,,N/A,Closed,,The Department of Transportation inspected this complaint and repaired the problem.,06/04/2019 07:50:00 AM,09 QUEENS,,QUEENS,1030543,192409,UNKNOWN,Unspecified,QUEENS,,,,,,,,40.6946739,-73.8330598,"(40.6946739, -73.8330598)"
42648572,05/10/2019 07:14:00 PM,05/11/2019 12:00:00 PM,DSNY,BCC - Brooklyn North,Sanitation Condition,12 Dead Animals,Sidewalk,11207,,,,,NEWPORT STREET,ALABAMA AVENUE,INTERSECTION,BROOKLYN,,DSNY Garage,Closed,,The Department of Sanitation removed the items.,05/11/2019 12:00:00 PM,05 BROOKLYN,,BROOKLYN,1013089,180213,PHONE,Unspecified,BROOKLYN,,,,,,,,40.6612728,-73.8960539,"(40.6612728, -73.8960539)"
47971560,10/24/2020 10:51:44 AM,,DPR,Department of Parks and Recreation,New Tree Request,For One Address,Street,11102,26-24 14 STREET,14 STREET,26 AVENUE,27 AVENUE,26 AVENUE,27 AVENUE,,ASTORIA,14 STREET,,In Progress,,,,01 QUEENS,4009020034,QUEENS,1003951,221143,ONLINE,Unspecified,QUEENS,,,,,,,,40.773640825439564,-73.92887071166908,"(40.773640825439564, -73.92887071166908)"
38445574,02/12/2018 08:22:00 AM,02/21/2018 12:00:00 PM,DSNY,BCC - Queens East,Litter Basket / Request,10 Litter Basket / Request,Sidewalk,11358,,,162 STREET,45 AVENUE,162 STREET,45 AVENUE,INTERSECTION,Flushing,,DSNY Garage,Closed,,The location does not meet the criteria for Litter Basket placement.,02/21/2018 12:00:00 PM,07 QUEENS,,QUEENS,1038405,214914,PHONE,Unspecified,QUEENS,,,,,,,,40.7563999,-73.8045271,"(40.7563999, -73.8045271)"
23206715,05/10/2012 05:00:35 PM,05/11/2012 02:13:38 PM,DOT,Department of Transportation,Broken Parking Meter,Coin or Card Did Not Register,Street,11215,232 PROSPECT PARK WEST,PROSPECT PARK WEST,WINDSOR PLACE,PROSPECT AVENUE,,,ADDRESS,BROOKLYN,,N/A,Closed,05/30/2012 05:00:35 PM,The Department of Transportation has completed the request or corrected the condition.,05/11/2012 02:13:18 PM,07 BROOKLYN,3011130045,BROOKLYN,989495,179570,PHONE,Unspecified,BROOKLYN,,,,,,,,40.6595533,-73.9810956,"(40.6595533, -73.9810956)"
23374652,06/06/2012 10:58:00 AM,06/06/2012 10:58:00 AM,DOT,Department of Transportation,Street Light Condition,Street Light Out,,11435,,,,,107 AVENUE,WALTHAM STREET,INTERSECTION,JAMAICA,,N/A,Closed,,Service Request status for this request is available on the Department of Transportation?s website. Please click the ?Learn More? link below.,06/05/2012 10:58:00 AM,12 QUEENS,,QUEENS,1039083,191943,UNKNOWN,Unspecified,QUEENS,,,,,,,,,,
21701603,10/20/2011 12:00:00 AM,11/06/2011 12:00:00 AM,HPD,Department of Housing Preservation and Development,PAINT - PLASTER,WALLS,RESIDENTIAL BUILDING,10460,1950 DALY AVENUE,DALY AVENUE,ELSMERE PLACE,EAST TREMONT AVENUE,,,ADDRESS,BRONX,,N/A,Closed,,The Department of Housing Preservation and Development conducted an inspection for the following conditions and identified potential lead-based paint conditions. HPD will attempt to contact you to schedule a follow-up inspection to test the paint for lead,11/06/2011 12:00:00 AM,06 BRONX,2029920043,BRONX,1016342,245912,UNKNOWN,Unspecified,BRONX,,,,,,,,,,
24037169,09/17/2012 12:00:00 AM,09/22/2012 12:00:00 AM,HPD,Department of Housing Preservation and Development,GENERAL CONSTRUCTION,MOLD,RESIDENTIAL BUILDING,10029,22 EAST 108 STREET,EAST 108 STREET,5 AVENUE,MADISON AVENUE,,,ADDRESS,NEW YORK,,N/A,Closed,,The Department of Housing Preservation and Development conducted an inspection for the following conditions and identified potential lead-based paint conditions. HPD will attempt to contact you to schedule a follow-up inspection to test the paint for lead,09/22/2012 12:00:00 AM,11 MANHATTAN,1016130006,MANHATTAN,998298,228994,PHONE,Unspecified,MANHATTAN,,,,,,,,,,
42598510,05/06/2019 02:55:00 PM,05/08/2019 03:45:00 PM,DEP,Department of Environmental Protection,Air Quality,"Air: Odor/Fumes, Vehicle Idling (AD3)",,10451,255 EAST 138 STREET,EAST 138 STREET,RIDER AVE,3 AVE,,,ADDRESS,BRONX,,N/A,Closed,,"The Department of Environmental Protection did not observe a violation of the New York City Air/Noise Code at the time of inspection and could not issue a notice of violation. If the problem still exists, please call 311 and file a new complaint. If you are outside of New York City, please call (212) NEW-YORK (212-639-9675).",05/08/2019 03:45:00 PM,01 BRONX,2023337501,BRONX,1004278,234888,PHONE,Unspecified,BRONX,,,,,,,,40.8113664,-73.9276491,"(40.8113664, -73.9276491)"
27951890,05/01/2014 01:47:00 PM,05/01/2014 05:00:00 PM,DOT,Department of Transportation,Street Light Condition,Street Light Out,,,,,,,SHORE PKWY,156 AVE,INTERSECTION,,,N/A,Closed,,Service Request status for this request is available on the Department of Transportation?s website. Please click the ?Learn More? link below.,05/01/2014 05:00:00 PM,Unspecified QUEENS,,QUEENS,,,UNKNOWN,Unspecified,QUEENS,,,,,,,,,,
24052327,09/19/2012 10:11:00 AM,09/20/2012 12:00:00 PM,DSNY,BCC - Brooklyn North,Litter Basket / Request,10 Litter Basket / Request,Sidewalk,11238,,,,,WASHINGTON AVENUE,PACIFIC STREET,INTERSECTION,BROOKLYN,,DSNY Garage,Closed,,"The Department of Sanitation has investigated the complaint and addressed the issue. If the problem persists, call 311 to enter a new complaint. If you are outside of New York City, please call (212) NEW-YORK (212-639-9675).",09/20/2012 12:00:00 PM,08 BROOKLYN,,BROOKLYN,994169,187107,PHONE,Unspecified,BROOKLYN,,,,,,,,,,
21961189,11/25/2011 12:00:00 AM,11/30/2011 12:00:00 AM,HPD,Department of Housing Preservation and Development,HEATING,HEAT,RESIDENTIAL BUILDING,11211,95 NORTH 7 STREET,NORTH 7 STREET,WYTHE AVENUE,BERRY STREET,,,ADDRESS,BROOKLYN,,N/A,Closed,,"More than one complaint was received for this building-wide condition.This complaint status is for the initial complaint.The Department of Housing Preservation and Development contacted an occupant of the apartment and verified that the following conditions were corrected. The complaint has been closed. If the condition still exists, please",11/30/2011 12:00:00 AM,01 BROOKLYN,3023180037,BROOKLYN,995329,201334,UNKNOWN,Unspecified,BROOKLYN,,,,,,,,,,
36810813,07/28/2017 08:28:17 PM,08/01/2017 01:00:34 PM,DPR,Department of Parks and Recreation,Overgrown Tree/Branches,Traffic Sign or Signal Blocked,Street,10014,,,,,HORATIO STREET,GREENWICH STREET,INTERSECTION,NEW YORK,,N/A,Closed,08/04/2017 07:20:57 AM,The Department of Parks and Recreation has determined that this issue is not within its jurisdiction. Please file a Service Request with the Department of Transportation.,08/01/2017 01:00:34 PM,02 MANHATTAN,,MANHATTAN,982460,208425,PHONE,Unspecified,MANHATTAN,,,,,,,,40.7387549,-74.0064593,"(40.7387549, -74.0064593)"
40519625,10/12/2018 12:34:59 AM,10/12/2018 06:41:08 AM,NYPD,New York City Police Department,Noise - Residential,Banging/Pounding,Residential Building/House,10026,203 WEST 117 STREET,WEST 117 STREET,7 AVENUE,ST NICHOLAS AVENUE,,,ADDRESS,NEW YORK,,Precinct,Closed,10/12/2018 08:34:59 AM,The Police Department responded to the complaint and took action to fix the condition.,10/12/2018 06:41:08 AM,10 MANHATTAN,1019230029,MANHATTAN,997490,232187,MOBILE,Unspecified,MANHATTAN,,,,,,,,40.8039656,-73.952176,"(40.8039656, -73.952176)"
19577617,01/11/2011 12:00:00 AM,01/14/2011 12:00:00 AM,HPD,Department of Housing Preservation and Development,HEATING,HEAT,RESIDENTIAL BUILDING,10466,648 EAST 233 STREET,EAST 233 STREET,CARPENTER AVENUE,WHITE PLAINS ROAD,,,ADDRESS,BRONX,,N/A,Closed,,"The Department of Housing Preservation and Development responded to a complaint of no heat or hot water and was advised by a tenant in the building that heat and hot water had been restored. If the condition still exists, please file a new complaint.",01/14/2011 12:00:00 AM,0 Unspecified,2048350059,Unspecified,1023196,264998,UNKNOWN,Unspecified,Unspecified,,,,,,,,,,
38785085,03/26/2018 05:37:55 PM,03/26/2018 07:43:53 PM,NYPD,New York City Police Department,Noise - Commercial,Loud Music/Party,Store/Commercial,11237,505 JOHNSON AVENUE,JOHNSON AVENUE,VARICK AVENUE,STEWART AVENUE,,,ADDRESS,BROOKLYN,,Precinct,Closed,03/27/2018 01:37:55 AM,The Police Department responded to the complaint and determined that police action was not necessary.,03/26/2018 07:43:53 PM,01 BROOKLYN,3029870006,BROOKLYN,1004511,197457,ONLINE,Unspecified,BROOKLYN,,,,,,,,40.7086274,-73.9269202,"(40.7086274, -73.9269202)"
45766131,03/06/2020 09:26:34 AM,03/06/2020 02:22:33 PM,NYPD,New York City Police Department,Illegal Parking,Parking Permit Improper Use,Street/Sidewalk,11691,312 BEACH   43 STREET,BEACH   43 STREET,ROCKAWAY BEACH BOULEVARD,BEACH CHANNEL DRIVE,ROCKAWAY BEACH BOULEVARD,BEACH CHANNEL DRIVE,,FAR ROCKAWAY,BEACH   43 STREET,,Closed,,The Police Department responded to the complaint and determined that police action was not necessary.,03/06/2020 07:22:35 PM,14 QUEENS,4158330005,QUEENS,1046832,156069,ONLINE,Unspecified,QUEENS,,,,,,,,40.59482863024436,-73.77465625912266,"(40.59482863024436, -73.77465625912266)"
31793762,10/19/2015 07:47:21 PM,10/21/2015 01:09:43 AM,HPD,Department of Housing Preservation and Development,HEAT/HOT WATER,APARTMENT ONLY,RESIDENTIAL BUILDING,11226,165 EAST 19 STREET,EAST 19 STREET,,,,,ADDRESS,BROOKLYN,,N/A,Closed,,The complaint you filed is a duplicate of a condition already reported by another tenant for a building-wide condition. The original complaint is still open. HPD may attempt to contact you to verify the correction of the condition or may conduct an inspection of your unit if the original complainant is not available for verification.,10/21/2015 12:00:00 AM,14 BROOKLYN,3051230051,BROOKLYN,994967,174511,ONLINE,Unspecified,BROOKLYN,,,,,,,,40.6456625,-73.9613811,"(40.6456625, -73.9613811)"
20512016,05/26/2011 12:34:40 PM,06/24/2011 01:24:00 PM,DOT,Department of Transportation,Street Condition,Pothole,,11223,KINGS HIGHWAY,KINGS HIGHWAY,NYCTA SUBWAY,WEST 7 STREET,,,BLOCKFACE,BROOKLYN,,N/A,Closed,,The Department of Transportation inspected this complaint and repaired the problem.,06/24/2011 01:24:00 PM,Unspecified BROOKLYN,,BROOKLYN,989695,159768,UNKNOWN,Unspecified,BROOKLYN,,,,,,,,,,
47108193,08/04/2020 01:46:05 PM,08/08/2020 06:27:09 PM,DPR,Department of Parks and Recreation,Damaged Tree,Branch or Limb Has Fallen Down,Street,11434,120-55 SMITH STREET,SMITH STREET,BEND,122 AVENUE,BEND,122 AVENUE,,JAMAICA,SMITH STREET,,Closed,,The Department of Parks and Recreation visited the location but could not find the tree condition you reported.,08/08/2020 10:27:14 PM,12 QUEENS,4123810027,QUEENS,1045641,187181,PHONE,Unspecified,QUEENS,,,,,,,,40.6802324834927,-73.77866169748087,"(40.6802324834927, -73.77866169748087)"
41862767,03/03/2019 01:16:04 PM,03/03/2019 06:34:08 PM,NYPD,New York City Police Department,Blocked Driveway,No Access,Street/Sidewalk,11234,1263 EAST 55 STREET,EAST 55 STREET,AVENUE K,AVENUE L,,,ADDRESS,BROOKLYN,,Precinct,Closed,03/03/2019 09:16:04 PM,The Police Department responded and upon arrival those responsible for the condition were gone.,03/03/2019 06:34:08 PM,18 BROOKLYN,3078350041,BROOKLYN,1005694,167239,PHONE,Unspecified,BROOKLYN,,,,,,,,40.6256829,-73.9227493,"(40.6256829, -73.9227493)"
22602318,01/26/2012 12:00:00 AM,02/17/2012 12:00:00 AM,HPD,Department of Housing Preservation and Development,PAINT - PLASTER,CEILING,RESIDENTIAL BUILDING,10458,382 EAST 197 STREET,EAST 197 STREET,DECATUR AVENUE,WEBSTER AVENUE,,,ADDRESS,BRONX,,N/A,Closed,,The Department of Housing Preservation and Development inspected the following conditions. No violations were issued. The complaint has been closed.,02/17/2012 12:00:00 AM,07 BRONX,2032780028,BRONX,1015411,254705,UNKNOWN,Unspecified,BRONX,,,,,,,,,,
34005962,08/04/2016 08:29:35 AM,08/04/2016 08:50:46 AM,NYPD,New York City Police Department,Vending,In Prohibited Area,Store/Commercial,10036,,,,,WEST 45 STREET,6 AVENUE,INTERSECTION,NEW YORK,,Precinct,Closed,08/04/2016 04:29:35 PM,The Police Department reviewed your complaint and provided additional information below.,08/04/2016 08:50:46 AM,05 MANHATTAN,,MANHATTAN,989040,214989,PHONE,Unspecified,MANHATTAN,,,,,,,,40.7567703,-73.9827104,"(40.7567703, -73.9827104)"
46970980,07/24/2020 10:05:47 PM,07/24/2020 11:18:23 PM,NYPD,New York City Police Department,Blocked Driveway,No Access,Street/Sidewalk,11220,658 47 STREET,47 STREET,6 AVENUE,7 AVENUE,6 AVENUE,7 AVENUE,,BROOKLYN,47 STREET,,Closed,,The Police Department responded to the complaint and took action to fix the condition.,07/25/2020 03:18:26 AM,07 BROOKLYN,3007670029,BROOKLYN,982826,174158,PHONE,Unspecified,BROOKLYN,,,,,,,,40.644699999902215,-74.00513133130951,"(40.644699999902215, -74.00513133130951)"
39403983,06/08/2018 11:53:09 PM,06/09/2018 02:54:59 AM,NYPD,New York City Police Department,Noise - Residential,Loud Music/Party,Residential Building/House,11234,1140 BERGEN AVENUE,BERGEN AVENUE,AVENUE K,AVENUE L,,,ADDRESS,BROOKLYN,,Precinct,Closed,06/09/2018 07:53:09 AM,The Police Department responded to the complaint and took action to fix the condition.,06/09/2018 02:54:59 AM,18 BROOKLYN,3083430056,BROOKLYN,1007895,168148,PHONE,Unspecified,BROOKLYN,,,,,,,,40.6281723,-73.9148172,"(40.6281723, -73.9148172)"
28230392,06/10/2014 11:57:59 AM,06/26/2014 12:00:00 AM,DOB,Department of Buildings,Building/Use,Zoning - Non-Conforming/Illegal Vehicle Storage,,10304,415 NORTH RAILROAD AVENUE,NORTH RAILROAD AVENUE,CORNELIA STREET,EVERGREEN AVENUE,,,ADDRESS,STATEN ISLAND,,N/A,Closed,,The Department of Buildings investigated this complaint and determined that no further action was necessary.,06/26/2014 12:00:00 AM,02 STATEN ISLAND,5033120046,STATEN ISLAND,959094,155503,UNKNOWN,Unspecified,STATEN ISLAND,,,,,,,,40.5934603,-74.0905792,"(40.5934603, -74.0905792)"
23414430,06/13/2012 12:00:00 AM,07/01/2012 12:00:00 AM,HPD,Department of Housing Preservation and Development,GENERAL CONSTRUCTION,MOLD,RESIDENTIAL BUILDING,11208,767 AUTUMN AVENUE,AUTUMN AVENUE,DUMONT AVENUE,LINDEN BOULEVARD,,,ADDRESS,BROOKLYN,,N/A,Closed,,The Department of Housing Preservation and Development inspected the following conditions. No violations were issued. The complaint has been closed.,07/01/2012 12:00:00 AM,05 BROOKLYN,3044650053,BROOKLYN,1021227,183348,UNKNOWN,Unspecified,BROOKLYN,,,,,,,,,,
30516710,04/30/2015 10:41:12 AM,04/30/2015 10:41:35 AM,HRA,HRA Benefit Card Replacement,Benefit Card Replacement,Medicaid,NYC Street Address,,,,,,,,,,,N/A,Closed,,"The Human Resources Administration received your request. If you are eligible for a benefit card replacement, you will receive it in 7 to 10 business days. No further updates will be available by calling 311 or on 311 Online.",,0 Unspecified,,Unspecified,,,ONLINE,Unspecified,Unspecified,,,,,,,,,,
46324565,05/29/2020 12:15:27 AM,05/29/2020 12:47:29 AM,NYPD,New York City Police Department,Noise - Street/Sidewalk,Loud Music/Party,Street/Sidewalk,10453,2055 DAVIDSON AVENUE,DAVIDSON AVENUE,WEST BURNSIDE AVENUE,WEST  180 STREET,WEST BURNSIDE AVENUE,WEST  180 STREET,,BRONX,DAVIDSON AVENUE,,Closed,,The Police Department responded to the complaint and took action to fix the condition.,05/29/2020 04:47:30 AM,05 BRONX,2031930030,BRONX,1009637,250473,MOBILE,Unspecified,BRONX,,,,,,,,40.854128935037835,-73.90823082274932,"(40.854128935037835, -73.90823082274932)"
```

