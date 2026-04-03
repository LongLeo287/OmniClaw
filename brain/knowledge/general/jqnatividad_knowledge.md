---
id: jqnatividad-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:56.288398
---

# KNOWLEDGE EXTRACT: jqnatividad
> **Extracted on:** 2026-03-30 17:38:13
> **Source:** jqnatividad

---

## File: `csv-nose.md`
```markdown
# 📦 jqnatividad/csv-nose [🔖 PENDING/APPROVE]
🔗 https://github.com/jqnatividad/csv-nose


## Meta
- **Stars:** ⭐ 5 | **Forks:** 🍴 0
- **Language:** Rust | **License:** Unknown
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Detecting CSV file dialects by Table Uniformity Measurement and Data Type Inference

## README (trích đầu)
```
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
    8: Location Typ
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

