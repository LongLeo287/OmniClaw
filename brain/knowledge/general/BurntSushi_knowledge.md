---
id: burntsushi-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:00.052382
---

# KNOWLEDGE EXTRACT: BurntSushi
> **Extracted on:** 2026-03-30 17:31:15
> **Source:** BurntSushi

---

## File: `quickcheck.md`
```markdown
# 📦 BurntSushi/quickcheck [🔖 PENDING/APPROVE]
🔗 https://github.com/BurntSushi/quickcheck


## Meta
- **Stars:** ⭐ 2724 | **Forks:** 🍴 160
- **Language:** Rust | **License:** Unlicense
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Automated property based testing for Rust (with shrinking).

## README (trích đầu)
```
# quickcheck

QuickCheck is a way to do property based testing using randomly generated
input. This crate comes with the ability to randomly generate and shrink
integers, floats, tuples, booleans, lists, strings, options and results.
All QuickCheck needs is a property function—it will then randomly generate
inputs to that function and call the property for each set of inputs. If the
property fails (whether by a runtime error like index out-of-bounds or by not
satisfying your property), the inputs are "shrunk" to find a smaller
counter-example.

The shrinking strategies for lists and numbers use a binary search to cover
the input space quickly. (It should be the same strategy used in
[Koen Claessen's QuickCheck for
Haskell](https://hackage.haskell.org/package/QuickCheck).)

[![Build status](https://github.com/BurntSushi/quickcheck/workflows/ci/badge.svg)](https://github.com/BurntSushi/quickcheck/actions)
[![crates.io](https://img.shields.io/crates/v/quickcheck.svg)](https://crates.io/crates/quickcheck)

Dual-licensed under MIT or the [UNLICENSE](https://unlicense.org/).

## Documentation

The API is fully documented:
[https://docs.rs/quickcheck](https://docs.rs/quickcheck).

## Simple example

Here's an example that tests a function that reverses a vector:

```rust
fn reverse<T: Clone>(xs: &[T]) -> Vec<T> {
    let mut rev = vec![];
    for x in xs.iter() {
        rev.insert(0, x.clone())
    }
    rev
}

#[cfg(test)]
mod tests {
    use quickcheck::quickcheck;
    use super::reverse;

    quickcheck! {
        fn prop(xs: Vec<u32>) -> bool {
            xs == reverse(&reverse(&xs))
        }
  }
}
```

This example uses the `quickcheck!` macro, which is backwards compatible with
old versions of Rust.

## The `#[quickcheck]` attribute

To make it easier to write QuickCheck tests, the `#[quickcheck]` attribute
will convert a property function into a `#[test]` function.

To use the `#[quickcheck]` attribute, you must import the `quickcheck` macro
from the `quickcheck_macros` crate:

```rust
fn reverse<T: Clone>(xs: &[T]) -> Vec<T> {
    let mut rev = vec![];
    for x in xs {
        rev.insert(0, x.clone())
    }
    rev
}

#[cfg(test)]
mod tests {
    use quickcheck_macros::quickcheck;
    use super::reverse;

    #[quickcheck]
    fn double_reversal_is_identity(xs: Vec<isize>) -> bool {
        xs == reverse(&reverse(&xs))
    }
}
```

## Installation

`quickcheck` is on `crates.io`, so you can include it in your project like so:

```toml
[dependencies]
quickcheck = "1"
```

If you're only using `quickcheck` in your test code, then you can add it as a
development dependency instead:

```toml
[dev-dependencies]
quickcheck = "1"
```

If you want to use the `#[quickcheck]` attribute, then add `quickcheck_macros`

```toml
[dev-dependencies]
quickcheck = "1"
quickcheck_macros = "1"
```

N.B. When using `quickcheck` (either directly or via the attributes),
`RUST_LOG=quickcheck` enables `info!` so that it shows useful output
(like the number of tests p
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `ripgrep.md`
```markdown
# 📦 BurntSushi/ripgrep [🔖 PENDING]
🔗 https://github.com/BurntSushi/ripgrep


## Meta
- **Stars:** ⭐ 61452 | **Forks:** 🍴 2440
- **Language:** Rust | **License:** Unlicense
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING

## Description:
ripgrep recursively searches directories for a regex pattern while respecting your gitignore

## README (trích đầu)
```
ripgrep (rg)
------------
ripgrep is a line-oriented search tool that recursively searches the current
directory for a regex pattern. By default, ripgrep will respect gitignore rules
and automatically skip hidden files/directories and binary files. (To disable
all automatic filtering by default, use `rg -uuu`.) ripgrep has first class
support on Windows, macOS and Linux, with binary downloads available for [every
release](https://github.com/BurntSushi/ripgrep/releases). ripgrep is similar to
other popular search tools like The Silver Searcher, ack and grep.

[![Build status](https://github.com/BurntSushi/ripgrep/workflows/ci/badge.svg)](https://github.com/BurntSushi/ripgrep/actions)
[![Crates.io](https://img.shields.io/crates/v/ripgrep.svg)](https://crates.io/crates/ripgrep)
[![Packaging status](https://repology.org/badge/tiny-repos/ripgrep.svg)](https://repology.org/project/ripgrep/badges)

Dual-licensed under MIT or the [UNLICENSE](https://unlicense.org).


### CHANGELOG

Please see the [CHANGELOG](CHANGELOG.md) for a release history.

### Documentation quick links

* [Installation](#installation)
* [User Guide](../../../core/security/QUARANTINE/vetted/repos/litellm/cookbook/ai_coding_tool_guides/claude_code_quickstart/guide.md)
* [Frequently Asked Questions](FAQ.md)
* [Regex syntax](https://docs.rs/regex/1/regex/#syntax)
* [Configuration files](../../../core/security/QUARANTINE/vetted/repos/litellm/cookbook/ai_coding_tool_guides/claude_code_quickstart/guide.md#configuration-file)
* [Shell completions](FAQ.md#complete)
* [Building](#building)
* [Translations](#translations)


### Screenshot of search results

[![A screenshot of a sample search with ripgrep](https://burntsushi.net/stuff/ripgrep1.png)](https://burntsushi.net/stuff/ripgrep1.png)


### Quick examples comparing tools

This example searches the entire
[Linux kernel source tree](https://github.com/BurntSushi/linux)
(after running `make defconfig && make -j8`) for `[A-Z]+_SUSPEND`, where
all matches must be words. Timings were collected on a system with an Intel
i9-12900K 5.2 GHz.

Please remember that a single benchmark is never enough! See my
[blog post on ripgrep](https://blog.burntsushi.net/ripgrep/)
for a very detailed comparison with more benchmarks and analysis.

| Tool | Command | Line count | Time |
| ---- | ------- | ---------- | ---- |
| ripgrep (Unicode) | `rg -n -w '[A-Z]+_SUSPEND'` | 536 | **0.082s** (1.00x) |
| [hypergrep](https://github.com/p-ranav/hypergrep) | `hgrep -n -w '[A-Z]+_SUSPEND'` | 536 | 0.167s (2.04x) |
| [git grep](https://www.kernel.org/pub/software/scm/git/brain/knowledge/docs_legacy/git-grep.html) | `git grep -P -n -w '[A-Z]+_SUSPEND'` | 536 | 0.273s (3.34x) |
| [The Silver Searcher](https://github.com/ggreer/the_silver_searcher) | `ag -w '[A-Z]+_SUSPEND'` | 534 | 0.443s (5.43x) |
| [ugrep](https://github.com/Genivia/ugrep) | `ugrep -r --ignore-files --no-hidden -I -w '[A-Z]+_SUSPEND'` | 536 | 0.639s (7.82x) |
| [git grep](https://www.kernel.org/pub/software/scm/git/brain/knowledge/docs_legacy/git-grep.html) | `LC_ALL=C git grep -E -n -w '[A-Z]+_SUSPEND'` | 536 | 0.727s (8.91x) |
| [git grep (Unicode)](https://www.kernel.org/pub/software/scm/git/brain/knowledge/docs_legacy/git-grep.html) | `LC_ALL=en_US.UTF-8 git grep -E -n -w '[A-Z]+
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `rust-csv.md`
```markdown
# 📦 BurntSushi/rust-csv [🔖 PENDING/APPROVE]
🔗 https://github.com/BurntSushi/rust-csv


## Meta
- **Stars:** ⭐ 1919 | **Forks:** 🍴 245
- **Language:** Rust | **License:** Unlicense
- **Last updated:** 2026-03-22
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

## File: `rust-stats.md`
```markdown
# 📦 BurntSushi/rust-stats [🔖 PENDING/APPROVE]
🔗 https://github.com/BurntSushi/rust-stats


## Meta
- **Stars:** ⭐ 88 | **Forks:** 🍴 17
- **Language:** Rust | **License:** Unlicense
- **Last updated:** 2025-10-10
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Basic statistical functions on streams for Rust.

## README (trích đầu)
```
An experimental library that provides some common statistical functions with
some support for computing them efficiently on *streams* of data. The intent
is to permit parallel computation of statistics on large data sets.

[![Build status](https://api.travis-ci.org/BurntSushi/rust-stats.png)](https://travis-ci.org/BurntSushi/rust-stats)
[![](http://meritbadge.herokuapp.com/streaming-stats)](https://crates.io/crates/streaming-stats)

Dual-licensed under MIT or the [UNLICENSE](http://unlicense.org).


### Documentation

Some documentation exists here:
[https://docs.rs/streaming-stats](https://docs.rs/streaming-stats).


### Installation

Simply add `streaming-stats` as a dependency to your project's `Cargo.toml`:

```toml
[dependencies]
streaming-stats = "0.2"
```

```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `tabwriter.md`
```markdown
# 📦 BurntSushi/tabwriter [🔖 PENDING/APPROVE]
🔗 https://github.com/BurntSushi/tabwriter


## Meta
- **Stars:** ⭐ 272 | **Forks:** 🍴 25
- **Language:** Rust | **License:** Unlicense
- **Last updated:** 2026-03-06
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Elastic tabstops for Rust.

## README (trích đầu)
```
tabwriter is a crate that implements
[elastic tabstops](http://nickgravgaard.com/elastictabstops/index.html). It
provides both a library for wrapping Rust `Writer`s and a small program that
exposes the same functionality at the command line.

[![Build status](https://github.com/BurntSushi/tabwriter/workflows/ci/badge.svg)](https://github.com/BurntSushi/tabwriter/actions)
[![](http://meritbadge.herokuapp.com/tabwriter)](https://crates.io/crates/tabwriter)

Dual-licensed under MIT or the [UNLICENSE](http://unlicense.org).


### Simple example of library

```rust
use std::io::Write;

use tabwriter::TabWriter;

let mut tw = TabWriter::new(vec![]);
tw.write_all(b"
Bruce Springsteen\tBorn to Run
Bob Seger\tNight Moves
Metallica\tBlack
The Boss\tDarkness on the Edge of Town
").unwrap();
tw.flush().unwrap();

let written = String::from_utf8(tw.into_inner().unwrap()).unwrap();

assert_eq!(&written, "
Bruce Springsteen  Born to Run
Bob Seger          Night Moves
Metallica          Black
The Boss           Darkness on the Edge of Town
");
```

You can see an example of *real* use in my
[CSV toolkit](https://github.com/BurntSushi/xsv/blob/master/src/cmd/table.rs#L57-L60).


### Simple example of command line utility

```bash
[andrew@Liger tabwriter] cat sample | sed 's/   /\\t/g'
a\tb\tc
abc\tmnopqrstuv\txyz
abcmnoxyz\tmore text

a\tb\tc
[andrew@Liger tabwriter] ./target/tabwriter < sample
a          b           c
abc        mnopqrstuv  xyz
abcmnoxyz  more text

a   b   c
```

Notice that once a column block is broken, alignment starts over again.


### Documentation

The API is fully documented with some examples:
[https://docs.rs/tabwriter/latest/tabwriter/](https://docs.rs/tabwriter/latest/tabwriter/).


### Installation

This crate works with Cargo. Assuming you have Rust and
[Cargo](http://crates.io/) installed, simply check out the source and run
tests:

```bash
git clone git://github.com/BurntSushi/tabwriter
cd tabwriter
cargo test
```

You can also add `tabwriter` as a dependency to your project's `Cargo.toml`:

```toml
[dependencies]
tabwriter = "1"
```


### Dealing with ANSI escape codes

If you want `tabwriter` to be aware of ANSI escape codes, then you should
enable the `TabWriter::ansi` option. Previously this was done by enabling the
crate feature `ansi_formatting`, but that feature is now deprecated. (If you
use it, then `TabWriter::ansi` will be automatically enabled for you. Otherwise
it is disabled by default.)


### Minimum Rust version policy

This crate's minimum supported `rustc` version is `1.67.0`.

The current policy is that the minimum Rust version required to use this crate
can be increased in minor version updates. For example, if `crate 1.0` requires
Rust 1.20.0, then `crate 1.0.z` for all values of `z` will also require Rust
1.20.0 or newer. However, `crate 1.y` for `y > 0` may require a newer minimum
version of Rust.

In general, this crate will be conservative with respect to the minimum
supported version of Rust.

```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

