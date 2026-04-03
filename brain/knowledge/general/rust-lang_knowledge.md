---
id: rust-lang-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:31:10.529469
---

# KNOWLEDGE EXTRACT: rust-lang
> **Extracted on:** 2026-03-30 17:53:02
> **Source:** rust-lang

---

## File: `regex.md`
```markdown
# 📦 rust-lang/regex [🔖 PENDING/APPROVE]
🔗 https://github.com/rust-lang/regex
🌐 https://docs.rs/regex

## Meta
- **Stars:** ⭐ 3932 | **Forks:** 🍴 495
- **Language:** Rust | **License:** Apache-2.0
- **Last updated:** 2026-03-24
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
An implementation of regular expressions for Rust. This implementation uses finite automata and guarantees linear time matching on all inputs.

## README (trích đầu)
```
regex
=====
This crate provides routines for searching strings for matches of a [regular
expression] (aka "regex"). The regex syntax supported by this crate is similar
to other regex engines, but it lacks several features that are not known how to
implement efficiently. This includes, but is not limited to, look-around and
backreferences. In exchange, all regex searches in this crate have worst case
`O(m * n)` time complexity, where `m` is proportional to the size of the regex
and `n` is proportional to the size of the string being searched.

[regular expression]: https://en.wikipedia.org/wiki/Regular_expression

[![Build status](https://github.com/rust-lang/regex/workflows/ci/badge.svg)](https://github.com/rust-lang/regex/actions)
[![Crates.io](https://img.shields.io/crates/v/regex.svg)](https://crates.io/crates/regex)

### Documentation

[Module documentation with examples](https://docs.rs/regex).
The module documentation also includes a comprehensive description of the
syntax supported.

Documentation with examples for the various matching functions and iterators
can be found on the
[`Regex` type](https://docs.rs/regex/*/regex/struct.Regex.html).

### Usage

To bring this crate into your repository, either add `regex` to your
`Cargo.toml`, or run `cargo add regex`.

Here's a simple example that matches a date in YYYY-MM-DD format and prints the
year, month and day:

```rust
use regex::Regex;

fn main() {
    let re = Regex::new(r"(?x)
(?P<year>\d{4})  # the year
-
(?P<month>\d{2}) # the month
-
(?P<day>\d{2})   # the day
").unwrap();

    let caps = re.captures("2010-03-14").unwrap();
    assert_eq!("2010", &caps["year"]);
    assert_eq!("03", &caps["month"]);
    assert_eq!("14", &caps["day"]);
}
```

If you have lots of dates in text that you'd like to iterate over, then it's
easy to adapt the above example with an iterator:

```rust
use regex::Regex;

fn main() {
    let re = Regex::new(r"(\d{4})-(\d{2})-(\d{2})").unwrap();
    let hay = "On 2010-03-14, foo happened. On 2014-10-14, bar happened.";

    let mut dates = vec![];
    for (_, [year, month, day]) in re.captures_iter(hay).map(|c| c.extract()) {
        dates.push((year, month, day));
    }
    assert_eq!(dates, vec![
      ("2010", "03", "14"),
      ("2014", "10", "14"),
    ]);
}
```

### Usage: Avoid compiling the same regex in a loop

It is an anti-pattern to compile the same regular expression in a loop since
compilation is typically expensive. (It takes anywhere from a few microseconds
to a few **milliseconds** depending on the size of the regex.) Not only is
compilation itself expensive, but this also prevents optimizations that reuse
allocations internally to the matching engines.

In Rust, it can sometimes be a pain to pass regular expressions around if
they're used from inside a helper function. Instead, we recommend using
[`std::sync::LazyLock`], or the [`once_cell`] crate,
if you can't use the standard library.

This example shows how to use `std::sync::LazyLock`:

```
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `rust-clippy.md`
```markdown
# 📦 rust-lang/rust-clippy [🔖 PENDING/APPROVE]
🔗 https://github.com/rust-lang/rust-clippy
🌐 https://rust-lang.github.io/rust-clippy/

## Meta
- **Stars:** ⭐ 13001 | **Forks:** 🍴 1943
- **Language:** Rust | **License:** Apache-2.0
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
A bunch of lints to catch common mistakes and improve your Rust code. Book: https://doc.rust-lang.org/clippy/

## README (trích đầu)
```
# Clippy

[![License: MIT OR Apache-2.0](https://img.shields.io/crates/l/clippy.svg)](#license)

A collection of lints to catch common mistakes and improve your [Rust](https://github.com/rust-lang/rust) code.

[There are over 800 lints included in this crate!](https://rust-lang.github.io/rust-clippy/master/index.html)

Lints are divided into categories, each with a default [lint level](https://doc.rust-lang.org/rustc/lints/levels.html).
You can choose how much Clippy is supposed to ~~annoy~~ help you by changing the lint level by category.

| Category              | Description                                                                         | Default level |
|-----------------------|-------------------------------------------------------------------------------------|---------------|
| `clippy::all`         | all lints that are on by default (correctness, suspicious, style, complexity, perf) | **warn/deny** |
| `clippy::correctness` | code that is outright wrong or useless                                              | **deny**      |
| `clippy::suspicious`  | code that is most likely wrong or useless                                           | **warn**      |
| `clippy::style`       | code that should be written in a more idiomatic way                                 | **warn**      |
| `clippy::complexity`  | code that does something simple but in a complex way                                | **warn**      |
| `clippy::perf`        | code that can be written to run faster                                              | **warn**      |
| `clippy::pedantic`    | lints which are rather strict or have occasional false positives                    | allow         |
| `clippy::restriction` | lints which prevent the use of language and library features[^restrict]             | allow         |
| `clippy::nursery`     | new lints that are still under development                                          | allow         |
| `clippy::cargo`       | lints for the cargo manifest                                                        | allow         |

More to come, please [file an issue](https://github.com/rust-lang/rust-clippy/issues) if you have ideas!

The `restriction` category should, *emphatically*, not be enabled as a whole. The contained
lints may lint against perfectly reasonable code, may not have an alternative suggestion,
and may contradict any other lints (including other categories). Lints should be considered
on a case-by-case basis before enabling.

[^restrict]: Some use cases for `restriction` lints include:
    - Strict coding styles (e.g. [`clippy::else_if_without_else`]).
    - Additional restrictions on CI (e.g. [`clippy::todo`]).
    - Preventing panicking in certain functions (e.g. [`clippy::unwrap_used`]).
    - Running a lint only on a subset of code (e.g. `#[forbid(clippy::float_arithmetic)]` on a module).

[`clippy::else_if_without_else`]: https://rust-lang.github.io/rust-clippy/master/index.html#else_if_without_else
[`clip
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `rust.md`
```markdown
# 📦 rust-lang/rust [🔖 PENDING]
🔗 https://github.com/rust-lang/rust
🌐 https://www.rust-lang.org

## Meta
- **Stars:** ⭐ 111525 | **Forks:** 🍴 14674
- **Language:** Rust | **License:** Apache-2.0
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING

## Description:
Empowering everyone to build reliable and efficient software.

## README (trích đầu)
```
<div align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/rust-lang/www.rust-lang.org/master/static/images/rust-social-wide-dark.svg">
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/rust-lang/www.rust-lang.org/master/static/images/rust-social-wide-light.svg">
    <img alt="The Rust Programming Language: A language empowering everyone to build reliable and efficient software"
         src="https://raw.githubusercontent.com/rust-lang/www.rust-lang.org/master/static/images/rust-social-wide-light.svg"
         width="50%">
  </picture>

[Website][Rust] | [Getting started] | [Learn] | [Documentation] | [Contributing]
</div>

This is the main source code repository for [Rust]. It contains the compiler,
standard library, and documentation.

[Rust]: https://www.rust-lang.org/
[Getting Started]: https://www.rust-lang.org/learn/get-started
[Learn]: https://www.rust-lang.org/learn
[Documentation]: https://www.rust-lang.org/learn#learn-use
[Contributing]: CONTRIBUTING.md

## Why Rust?

- **Performance:** Fast and memory-efficient, suitable for critical services, embedded devices, and easily integrated with other languages.

- **Reliability:** Our rich type system and ownership model ensure memory and thread safety, reducing bugs at compile-time.

- **Productivity:** Comprehensive documentation, a compiler committed to providing great diagnostics, and advanced tooling including package manager and build tool ([Cargo]), auto-formatter ([rustfmt]), linter ([Clippy]) and editor support ([rust-analyzer]).

[Cargo]: https://github.com/rust-lang/cargo
[rustfmt]: https://github.com/rust-lang/rustfmt
[Clippy]: https://github.com/rust-lang/rust-clippy
[rust-analyzer]: https://github.com/rust-lang/rust-analyzer

## Quick Start

Read ["Installation"] from [The Book].

["Installation"]: https://doc.rust-lang.org/book/ch01-01-installation.html
[The Book]: https://doc.rust-lang.org/book/index.html

## Installing from Source

If you really want to install from source (though this is not recommended), see
[INSTALL.md](INSTALL.md).

## Getting Help

See https://www.rust-lang.org/community for a list of chat platforms and forums.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

For a detailed explanation of the compiler's architecture and how to begin contributing, see the [rustc-dev-guide](https://rustc-dev-guide.rust-lang.org/).

## License

Rust is primarily distributed under the terms of both the MIT license and the
Apache License (Version 2.0), with portions covered by various BSD-like
licenses.

See [LICENSE-APACHE](LICENSE-APACHE), [LICENSE-MIT](LICENSE-MIT), and
[COPYRIGHT](COPYRIGHT) for details.

## Trademark

[The Rust Foundation][rust-foundation] owns and protects the Rust and Cargo
trademarks and logos (the "Rust Trademarks").

If you want to use these names or brands, please read the
[Rust language trademark policy][trademark-policy].

Third-pa
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

