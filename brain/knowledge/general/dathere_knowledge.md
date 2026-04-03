---
id: dathere-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:16.686223
---

# KNOWLEDGE EXTRACT: dathere
> **Extracted on:** 2026-03-30 17:35:45
> **Source:** dathere

---

## File: `datapusher-plus.md`
```markdown
# 📦 dathere/datapusher-plus [🔖 PENDING/APPROVE]
🔗 https://github.com/dathere/datapusher-plus


## Meta
- **Stars:** ⭐ 43 | **Forks:** 🍴 33
- **Language:** Python | **License:** AGPL-3.0
- **Last updated:** 2026-02-20
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Push data into the CKAN Datastore fast & reliably while inferring, calculating & suggesting metadata using Jinja2 Formulas defined in your scheming metadata schema. It pushes real good!

## README (trích đầu)
```
[CKAN Service Provider]: https://github.com/ckan/ckan-service-provider
[Messytables]: https://github.com/okfn/messytables
[qsv]: https://github.com/dathere/qsv#qsv-ultra-fast-csv-data-wrangling-toolkit

# DataPusher+

> NOTE: v2 is a major revamp. Documentation is currently WIP.

DataPusher+ is a fork of [Datapusher](https://github.com/ckan/datapusher) that combines the speed and robustness of [ckanext-xloader](https://github.com/ckan/ckanext-xloader) with the data type guessing of Datapusher - [super-powered with the ability to infer, calculate & suggest metadata using Jinja2 formulas defined in the scheming configuration file](brain/knowledge/docs_legacy/dataset_schema.yaml).


https://github.com/user-attachments/assets/b2fc2c3a-d244-4d11-9cf3-8270f0e99162


The Formulas have access to not just the `package` and `resource` fields (in the same namespaces), it also has access to the following information in these additional namespaces that can be used in Jinja2 expressions:
* `dpps` - with the "s" for stats.<br/>Each field will have an extensive list of summary statistics (by default: 
type, is_ascii, sum, min/max, range, sort_order, sortiness, min_length, max_length, sum_length, avg_length, stddev_length, variance_length, cv_length, mean, sem, geometric_mean, harmonic_mean, stddev, variance, cv, nullcount, max_precision, sparsity, cardinality, uniqueness_ratio.) Check [here](https://github.com/dathere/qsv/wiki/Supplemental#stats-command-output-explanation) for all other available statistics.
* `dppf` - with the "f" for frequency table.<br/>Each field will have its frequency table available sorted in descending order the top N (configurable, default 10) values, with a corresponding count & percentage. "Other (COUNT)" will be used as a "basket" for other values with COUNT set to the count of other values beyond the top N. ID fields will be indicated by "<ALL_UNIQUE>" in the table.
* `dpp` - additional inferred/calculated metadata.<br/>
  * `ORIGINAL_FILE_SIZE` (bytes)
  * `PREVIEW_FILE_SIZE` (bytes)
  * `RECORD_COUNT` (int)
  * `PREVIEW_RECORD_COUNT` (int)
  * `IS_SORTED` (bool)
  * `DEDUPED` (bool)
  * `DUPE_COUNT` (int: -1 if there are no dupes)
  * Date/DateTime metadata<br/>
    DP+ can infer date/datetime columns - supporting 19 different formats. As it is a relatively expensive operation, it will only do so for candidate columns with names that fit a configurable pattern.
      * `DATE_FIELDS` - a list of inferred date columns
      * `NO_DATE_FIELDS` (bool)
      * `DATETIME_FIELDS` - a list of inferred datetime columns
      * `NO_DATETIME_FIELDS` (bool)
  * Latitude/Longitude metadata<br/>
    DP+ can infer the latitude and longitude columns based on the column's characteristics. A column is inferred to be a latitude/longitude column if:
      * its in a comma-separated priority-order list of lat/long name patterns
      * for latitude, if its of type "Float" with a range of -90.0 to 90.0, and
      * for longitude, if its a "Float" with a range of -180.0 to 18
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `docopt.rs.md`
```markdown
# 📦 dathere/docopt.rs [🔖 PENDING/APPROVE]
🔗 https://github.com/dathere/docopt.rs


## Meta
- **Stars:** ⭐ 3 | **Forks:** 🍴 1
- **Language:** Rust | **License:** Unlicense
- **Last updated:** 2026-01-06
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Docopt for Rust (command line argument parser).

## README (trích đầu)
```
# qsv_docopt

This crate is primarily maintained for the [qsv](https://github.com/jqnatividad/qsv) project as its been optimized to
take advantage of the self-documenting nature of [docopt](http://docopt.org/),
which neither [clap](http://docs.rs/clap/) nor [structopt](http://docs.rs/structopt/)
can provide.

As the [docopt.rs](https://github.com/docopt/docopt.rs) project is no longer maintained,
this crate will be updated to ensure qsv uses the latest features and innovations of Rust
with this qsv-optimized version of docopt.

------------

Docopt for Rust with automatic type based decoding (i.e., data validation).
This implementation conforms to the
[official description of Docopt](http://docopt.org/) and
[passes its test suite](https://github.com/docopt/docopt/pull/201).

Dual-licensed under MIT or the [UNLICENSE](http://unlicense.org).

## Documentation

https://docs.rs/qsv_docopt

## Installation

This crate is fully compatible with Cargo. Just add it to your `Cargo.toml`:

```toml
[dependencies]
qsv_docopt = "1"
serde = { version = "1", features = ["derive"] }
```

## Quick example

Here is a full working example. Notice that you can specify the types of each
of the named values in the Docopt usage string. Values will be automatically
converted to those types (or an error will be reported).

```rust
use qsv_docopt::Docopt;
use serde::Deserialize;

const USAGE: &'static str = "
Naval Fate.

Usage:
  naval_fate.py ship new <name>...
  naval_fate.py ship <name> move <x> <y> [--speed=<kn>]
  naval_fate.py ship shoot <x> <y>
  naval_fate.py mine (set|remove) <x> <y> [--moored | --drifting]
  naval_fate.py (-h | --help)
  naval_fate.py --version

Options:
  -h --help     Show this screen.
  --version     Show version.
  --speed=<kn>  Speed in knots [default: 10].
  --moored      Moored (anchored) mine.
  --drifting    Drifting mine.
";

#[derive(Debug, Deserialize)]
struct Args {
    flag_speed: isize,
    flag_drifting: bool,
    arg_name: Vec<String>,
    arg_x: Option<i32>,
    arg_y: Option<i32>,
    cmd_ship: bool,
    cmd_mine: bool,
}

fn main() {
    let args: Args = Docopt::new(USAGE)
        .and_then(|d| d.deserialize())
        .unwrap_or_else(|e| e.exit());
    println!("{:?}", args);
}
```

## Struct field name mapping

The field names of the struct map like this:

```
-g            => flag_g
--group       => flag_group
--group <arg> => flag_group
FILE          => arg_FILE
<file>        => arg_file
build         => cmd_build
```

## Traditional Docopt API

The reference implementation of Docopt returns a Python dictionary with names
like `<arg>` or `--flag`. If you prefer this access pattern, then you can use
`docopt::ArgvMap`. The disadvantage is that you have to do all of your type
conversion manually. Here's the canonical Docopt example with a hash table:

```rust
use qsv_docopt::Docopt;

const USAGE: &'static str = "
Naval Fate.

Usage:
  naval_fate.py ship new <name>...
  naval_fate.py ship <name> move <x> <y> [--speed=<kn>]
  
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `qsv-docopt.md`
```markdown
# 📦 dathere/qsv-docopt [🔖 PENDING/APPROVE]
🔗 https://github.com/dathere/qsv-docopt


## Meta
- **Stars:** ⭐ 1 | **Forks:** 🍴 1
- **Language:** Rust | **License:** Unlicense
- **Last updated:** 2026-02-15
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Docopt for qsv

## README (trích đầu)
```
# qsv_docopt

This crate is primarily maintained for the [qsv](https://github.com/jqnatividad/qsv) project as its been optimized to
take advantage of the self-documenting nature of [docopt](http://docopt.org/),
which neither [clap](http://docs.rs/clap/) nor [structopt](http://docs.rs/structopt/)
can provide.

As the [docopt.rs](https://github.com/docopt/docopt.rs) project is no longer maintained,
this crate will be updated to ensure qsv uses the latest features and innovations of Rust
with this qsv-optimized version of docopt.

------------

Docopt for Rust with automatic type based decoding (i.e., data validation).
This implementation conforms to the
[official description of Docopt](http://docopt.org/) and
[passes its test suite](https://github.com/docopt/docopt/pull/201).

Dual-licensed under MIT or the [UNLICENSE](http://unlicense.org).

## Documentation

https://docs.rs/qsv_docopt

## Installation

This crate is fully compatible with Cargo. Just add it to your `Cargo.toml`:

```toml
[dependencies]
qsv_docopt = "1"
serde = { version = "1", features = ["derive"] }
```

## Quick example

Here is a full working example. Notice that you can specify the types of each
of the named values in the Docopt usage string. Values will be automatically
converted to those types (or an error will be reported).

```rust
use qsv_docopt::Docopt;
use serde::Deserialize;

const USAGE: &'static str = "
Naval Fate.

Usage:
  naval_fate.py ship new <name>...
  naval_fate.py ship <name> move <x> <y> [--speed=<kn>]
  naval_fate.py ship shoot <x> <y>
  naval_fate.py mine (set|remove) <x> <y> [--moored | --drifting]
  naval_fate.py (-h | --help)
  naval_fate.py --version

Options:
  -h --help     Show this screen.
  --version     Show version.
  --speed=<kn>  Speed in knots [default: 10].
  --moored      Moored (anchored) mine.
  --drifting    Drifting mine.
";

#[derive(Debug, Deserialize)]
struct Args {
    flag_speed: isize,
    flag_drifting: bool,
    arg_name: Vec<String>,
    arg_x: Option<i32>,
    arg_y: Option<i32>,
    cmd_ship: bool,
    cmd_mine: bool,
}

fn main() {
    let args: Args = Docopt::new(USAGE)
        .and_then(|d| d.deserialize())
        .unwrap_or_else(|e| e.exit());
    println!("{:?}", args);
}
```

## Struct field name mapping

The field names of the struct map like this:

```
-g            => flag_g
--group       => flag_group
--group <arg> => flag_group
FILE          => arg_FILE
<file>        => arg_file
build         => cmd_build
```

## Non-UTF-8 Arguments

**Note:** This library uses `std::env::args_os()` internally with lossy UTF-8
conversion to avoid panicking on non-UTF-8 arguments. This means that non-UTF-8
command-line arguments (rare on most systems) will be converted to the Unicode
replacement character (�). 

If you need to preserve exact non-UTF-8 byte sequences in your arguments, you
should handle `std::env::args_os()` directly in your application before passing
arguments to docopt via the `.argv()` method.

## Traditional Do
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `qsv-easy-windows-installer.md`
```markdown
# 📦 dathere/qsv-easy-windows-installer [🔖 PENDING/APPROVE]
🔗 https://github.com/dathere/qsv-easy-windows-installer


## Meta
- **Stars:** ⭐ 2 | **Forks:** 🍴 0
- **Language:** Rust | **License:** Unknown
- **Last updated:** 2025-05-22
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
⚡ Easy installer for qsv on Windows devices. Simply click the app's Install button and wait a few seconds to get the latest version of qsv installed to your PATH.

## README (trích đầu)
```
# qsv Easy installer for Windows

![image](https://github.com/user-attachments/assets/3ccc6cad-04ab-4288-9a41-9afadaa1fcfc)

This is a desktop app to help install the latest release of the [qsv](https://qsv.dathere.com) command-line tool for Windows devices to a a folder included in the user's `PATH`.

Built with Tauri.

```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `qsv-lookup-tables.md`
```markdown
# 📦 dathere/qsv-lookup-tables [🔖 PENDING/APPROVE]
🔗 https://github.com/dathere/qsv-lookup-tables


## Meta
- **Stars:** ⭐ 5 | **Forks:** 🍴 1
- **Language:** N/A | **License:** MIT
- **Last updated:** 2024-11-30
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
A repository of common lookup tables that can be used with qsv

## README (trích đầu)
```
# qsv-lookup-tables

A repository of common lookup tables that can be used with [qsv](https://github.com/jqnatividad/qsv#qsv-ultra-fast-csv-data-wrangling-toolkit)'s [`luau`](https://github.com/jqnatividad/qsv#luau_deeplink) command's `qsv_register_lookup` helper function.

Please feel free to submit a pull request to add more lookup tables.

## Usage

To use a lookup table, simply use the name of the csv you want to use with the [`qsv_register_lookup`](https://github.com/jqnatividad/qsv/blob/b8fded6b41c4b31f0f257a0fa1513a921e035e7a/src/cmd/luau.rs#L1349-L1368) helper using the "dathere://" scheme.

```lua
us_states_lookup_headers = qsv_register_lookup("us_states", "dathere://us-states-example.csv")
```

The first argument is the name of the lookup table to download the data to. The second argument is the dathere URL of the CSV file in the [`lookup-tables`](https://github.com/dathere/qsv-lookup-tables/tree/main/lookup-tables) directory.

When the lookup table is downloaded sucessfully, a Luau table is created with the same name as the first argument ("us_states" in this case). The table is a two-dimensional Luau table, where the first dimension is the value of the first column of the CSV file (the lookup key), and the second dimension are the rest of the columns with their data.

Further, qsv_register_lookup returns the header names of the CSV file as another Luau table ("us_states_lookup_headers" in this example), which can be used to access the data in the lookup table.

### Example

We have a small table with some transactions for which we want to get the total amount with the corresponding state sales tax.   
(source code: [testlookup.luau](examples/readme-example/testlookup.luau), data: [data.csv](examples/readme-example/data.csv))

#### data.csv

```csv
Order ID,Amount,State
20230301001,13.50,NJ
20230301002,15.00,NY
20230301003,72.00,TX
20230301004,12.00,CA
20230301005,33.70,DE
```

#### [us-states-example.csv](https://github.com/dathere/qsv-lookup-tables/blob/main/lookup-tables/us-states-example.csv) lookup table

```csv
 Abbreviation,Name,Capital,Population (2019),area (square miles),Sales Tax (2023)
 AL,Alabama,Montgomery ,"4,903,185","52,420",4
 AK,Alaska,Juneau,"731,545","665,384",0
 AZ,Arizona,Phoenix,"7,278,717","113,990",5.6
 AR,Arkansas,Little Rock,"3,017,804","53,179",6.5
 CA,California,Sacramento,"39,512,223","163,695",7.5
 ...
 WV,West Virginia,Charleston,"1,792,147,24,230",6
 WI,Wisconsin,Madison,"5,822,434,65,496",5
 WY,Wyoming,Cheyenne,"578,759,97,813",4
```

#### testlookup.luau

```lua
BEGIN {
    -- this is the BEGIN block, which is executed ONCE at the beginning
    -- we typically use it to initialize variables, load lookup tables and setup functions
    running_total = 0;
    running_total_after_tax = 0;
    amount_table = {};
    amount_table_with_salestax = {};

    -- we use the "dathere://" scheme to load "us-states-example.csv" from the
    -- https://github.com/dathere/qsv-lookup-tables repository
    -- 6000 is t
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `qsv-stats.md`
```markdown
# 📦 dathere/qsv-stats [🔖 PENDING/APPROVE]
🔗 https://github.com/dathere/qsv-stats


## Meta
- **Stars:** ⭐ 10 | **Forks:** 🍴 0
- **Language:** Rust | **License:** Unlicense
- **Last updated:** 2026-03-08
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Blazing-fast, parallelized statistical functions on streams for Rust.

## README (trích đầu)
```
# qsv-stats

This library provides common statistical functions with support for computing them
efficiently on *streams* of data. The intent is to permit parallel computation of
statistics on large data sets.

> NOTE: This fork of [streaming-stats](https://github.com/BurntSushi/rust-stats) merges 
pending upstream PRs for quartile computation and a different variance algorithm 
that is used in [qsv](https://github.com/dathere/qsv)'s [`stats` command](https://github.com/dathere/qsv/blob/master/README.md#stats_deeplink).  
It has numerous other stats, heavily updated for performance, uses parallel processing,
uses the [fused multiply add](https://en.wikipedia.org/wiki/Multiply%E2%80%93accumulate_operation#Fused_multiply%E2%80%93add) CPU instruction along with several other performance tweaks.

Dual-licensed under MIT or the [UNLICENSE](http://unlicense.org).


### Documentation

Documentation for qsv-stats exists here:
[https://docs.rs/qsv-stats](https://docs.rs/qsv-stats).


### Installation

Simply add `qsv-stats` as a dependency to your project's `Cargo.toml`:

```toml
[dependencies]
qsv-stats = "0.47.0"
```

```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `qsv.md`
```markdown
# 📦 dathere/qsv [🔖 PENDING/APPROVE]
🔗 https://github.com/dathere/qsv
🌐 https://qsv.dathere.com

## Meta
- **Stars:** ⭐ 3557 | **Forks:** 🍴 105
- **Language:** Rust | **License:** Unlicense
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Blazing-fast Data-Wrangling toolkit

## README (trích đầu)
```
## qsv: Blazing-fast Data-Wrangling toolkit

[![Linux build status](https://github.com/dathere/qsv/actions/workflows/rust.yml/badge.svg)](https://github.com/dathere/qsv/actions/workflows/rust.yml)
[![Windows build status](https://github.com/dathere/qsv/actions/workflows/rust-windows.yml/badge.svg)](https://github.com/dathere/qsv/actions/workflows/rust-windows.yml)
[![macOS build status](https://github.com/dathere/qsv/actions/workflows/rust-macos.yml/badge.svg)](https://github.com/dathere/qsv/actions/workflows/rust-macos.yml)
[![Security audit](https://github.com/dathere/qsv/actions/workflows/security-audit.yml/badge.svg)](https://github.com/dathere/qsv/actions/workflows/security-audit.yml)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/29e587760af64abcb115ba23efe1b365)](https://app.codacy.com/gh/dathere/qsv/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade)
[![Crates.io](https://img.shields.io/crates/v/qsv.svg?logo=crates.io)](https://crates.io/crates/qsv)
[![Discussions](https://img.shields.io/github/discussions/dathere/qsv)](https://github.com/dathere/qsv/discussions)
[![Minimum supported Rust version](https://img.shields.io/badge/Rust-1.94-red?logo=rust)](#minimum-supported-rust-version)
[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2Fjqnatividad%2Fqsv.svg?type=shield)](https://app.fossa.com/projects/git%2Bgithub.com%2Fjqnatividad%2Fqsv?ref=badge_shield) [![DOI](https://zenodo.org/badge/320463703.svg)](https://doi.org/10.5281/zenodo.17851335)
[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/dathere/qsv)

<div align="center">

 &nbsp;          |  Table of Contents
:--------------------------|:-------------------------
![qsv logo](brain/knowledge/docs_legacy/images/qsv_logo-gemini-indy-robothorse-small.png "Nano Banana Prompt: Can you make the horse robotic? Also, add an \"MCP\" label on the robotic horse. Keep the same pose and dimensions.")<br/>[_Hi-ho "Quicksilver" away!_](https://www.youtube.com/watch?v=p9lf76xOA5k)<br/><sub><sup>[original logo details](https://github.com/dathere/qsv/discussions/295) * [Base AI-reimagined logo](brain/knowledge/docs_legacy/images/qsv_logo-gemini-indy-robothorse-small.png) * [Event logo archive](brain/knowledge/docs_legacy/images/event-logos/)</sup></sub><br/>|qsv is a command line program for querying, slicing,<br>sorting, analyzing, filtering, enriching, transforming,<br>validating, joining, formatting, converting, chatting,<br>[FAIR](https://www.go-fair.org/fair-principles/)ifying & documenting tabular data (CSV, Excel, [etc](#file-formats)).<br>Commands are simple, composable & ___["blazing fast"](https://github.com/dathere/qsv/discussions/1348)___.<br><br>* [Commands](#available-commands)<br>* [Installation Options](#installation-options)<br> * [Whirlwind Tour](../../../vault/archives/archive_legacy/qsv/docs/whirlwind_tour.md#a-whirlwind-tour) / [Notebooks](contrib/notebooks/) / [Lessons & Exercises](https://100.dathere.com)<br>* [FAQ](https://github.com/dathere/qsv/discussions/categories/faq)<br>* [Performance Tuning](brain/knowledge/docs_legacy/PE
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `rust-csv.md`
```markdown
# 📦 dathere/rust-csv [🔖 PENDING/APPROVE]
🔗 https://github.com/dathere/rust-csv


## Meta
- **Stars:** ⭐ 2 | **Forks:** 🍴 0
- **Language:** Rust | **License:** Unlicense
- **Last updated:** 2026-03-09
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
A CSV parser for Rust, with Serde support.

## README (trích đầu)
```
csv
===
A fast and flexible CSV reader and writer for Rust, with support for Serde.

[![Build status](https://github.com/BurntSushi/rust-csv/workflows/ci/badge.svg)](https://github.com/BurntSushi/rust-csv/actions)
[![crates.io](https://img.shields.io/crates/v/csv.svg)](https://crates.io/crates/csv)

Dual-licensed under MIT or the [UNLICENSE](http://unlicense.org).


### Documentation

https://docs.rs/csv

If you're new to Rust, the
[tutorial](https://docs.rs/csv/1.*/csv/tutorial/index.html)
is a good place to start.


### Usage

To bring this crate into your repository, either add `csv` to your
`Cargo.toml`, or run `cargo add csv`.


### Example

This example shows how to read CSV data from stdin and print each record to
stdout.

There are more examples in the
[cookbook](https://docs.rs/csv/1.*/csv/cookbook/index.html).

```rust
use std::{error::Error, io, process};

fn example() -> Result<(), Box<dyn Error>> {
    // Build the CSV reader and iterate over each record.
    let mut rdr = csv::Reader::from_reader(io::stdin());
    for result in rdr.records() {
        // The iterator yields Result<StringRecord, Error>, so we check the
        // error here.
        let record = result?;
        println!("{:?}", record);
    }
    Ok(())
}

fn main() {
    if let Err(err) = example() {
        println!("error running example: {}", err);
        process::exit(1);
    }
}
```

The above example can be run like so:

```text
$ git clone git://github.com/BurntSushi/rust-csv
$ cd rust-csv
$ cargo run --example cookbook-read-basic < examples/data/smallpop.csv
```

### Example with Serde

This example shows how to read CSV data from stdin into your own custom struct.
By default, the member names of the struct are matched with the values in the
header record of your CSV data.

```rust
use std::{error::Error, io, process};

#[derive(Debug, serde::Deserialize)]
struct Record {
    city: String,
    region: String,
    country: String,
    population: Option<u64>,
}

fn example() -> Result<(), Box<dyn Error>> {
    let mut rdr = csv::Reader::from_reader(io::stdin());
    for result in rdr.deserialize() {
        // Notice that we need to provide a type hint for automatic
        // deserialization.
        let record: Record = result?;
        println!("{:?}", record);
    }
    Ok(())
}

fn main() {
    if let Err(err) = example() {
        println!("error running example: {}", err);
        process::exit(1);
    }
}
```

The above example can be run like so:

```
$ git clone git://github.com/BurntSushi/rust-csv
$ cd rust-csv
$ cargo run --example cookbook-read-serde < examples/data/smallpop.csv
```

```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `us-census-bureau-data-api-mcp.md`
```markdown
# 📦 dathere/us-census-bureau-data-api-mcp [🔖 PENDING/APPROVE]
🔗 https://github.com/dathere/us-census-bureau-data-api-mcp
🌐 https://www.census.gov

## Meta
- **Stars:** ⭐ 0 | **Forks:** 🍴 0
- **Language:** TypeScript | **License:** CC0-1.0
- **Last updated:** 2026-02-10
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
The U.S. Census Bureau Data API MCP connects AI Assistants with official Census Bureau statistics.

## README (trích đầu)
```
# U.S. Census Bureau Data API MCP
[![License: CC0-1.0](https://img.shields.io/badge/License-CC0%201.0-lightgrey.svg)](https://github.com/uscensusbureau/us-census-bureau-data-api-mcp/blob/main/LICENSE)
[![MCP Project Build](https://github.com/uscensusbureau/us-census-bureau-data-api-mcp/actions/workflows/build.yml/badge.svg)](https://github.com/uscensusbureau/us-census-bureau-data-api-mcp/actions/workflows/build.yml)
[![MCP Project - Lint](https://github.com/uscensusbureau/us-census-bureau-data-api-mcp/actions/workflows/lint.yml/badge.svg)](https://github.com/uscensusbureau/us-census-bureau-data-api-mcp/actions/workflows/lint.yml)
[![MCP Server - Tests](https://github.com/uscensusbureau/us-census-bureau-data-api-mcp/actions/workflows/test.yml/badge.svg)](https://github.com/uscensusbureau/us-census-bureau-data-api-mcp/actions/workflows/test.yml)
[![MCP Database - Tests](https://github.com/uscensusbureau/us-census-bureau-data-api-mcp/actions/workflows/test-db.yml/badge.svg)](https://github.com/uscensusbureau/us-census-bureau-data-api-mcp/actions/workflows/test-db.yml)
![MCP Server - Test Coverage](https://raw.githubusercontent.com/gist/luke-keller-census/0589e2c69696f077eef7d6af818a108b/raw/badge.svg)
![MCP Database - Test Coverage](https://raw.githubusercontent.com/gist/luke-keller-census/ae50d82d94893c2e674f7f742aea958e/raw/badge.svg)

Bringing _official_ Census Bureau statistics to AI assistants everywhere.

The *U.S. Census Bureau Data API MCP* is a [Model Context Protocol (MCP)](https://modelcontextprotocol.io/introduction) server that connects AI assistants with data from the Census Data API and other official Census Bureau sources. This project is built using the [MCP Typescript SDK](https://github.com/modelcontextprotocol/typescript-sdk).

## Contents
* [Getting Started](#getting-started)
* [Using the MCP Server](#using-the-mcp-server)
* [How the MCP Server Works](#how-the-mcp-server-works)
* [Development](#development)
* [MCP Server Architecture](#mcp-server-architecture)
* [Available Methods](#available-methods)
* [Available Tools](#available-tools)
* [Available Prompts](#available-prompts)
* [Helper Scripts](#helper-scripts)
* [Additional Information](#additional-information)

## Getting Started
To get started, you will need:

* A valid Census Bureau [Data API key](https://api.census.gov/data/key_signup.html)
* Docker (i.e. Docker Desktop)
* Node 18+

## Using the MCP Server
To use the U.S. Census Bureau Data API MCP server:
1. Clone or download the project locally.
2. In a terminal window, navigate to the project’s root directory and run `docker compose --profile prod run --rm census-mcp-db-init sh -c "npm run migrate:up && npm run seed"` to pull data from the Census Data API into the local database. *This is only required on first-time setup.*
3. Configure your AI Assistant to use the MCP Server (see below).
4. Start your AI Assistant.

Here is an example configuration file that includes the appropriate scripts for launching the MCP Ser
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

