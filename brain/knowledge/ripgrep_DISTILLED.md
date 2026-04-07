---
id: ripgrep
type: knowledge
owner: OA_Triage
---
# ripgrep
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
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
* [User Guide](GUIDE.md)
* [Frequently Asked Questions](FAQ.md)
* [Regex syntax](https://docs.rs/regex/1/regex/#syntax)
* [Configuration files](GUIDE.md#configuration-file)
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
| [git grep](https://www.kernel.org/pub/software/scm/git/docs/git-grep.html) | `git grep -P -n -w '[A-Z]+_SUSPEND'` | 536 | 0.273s (3.34x) |
| [The Silver Searcher](https://github.com/ggreer/the_silver_searcher) | `ag -w '[A-Z]+_SUSPEND'` | 534 | 0.443s (5.43x) |
| [ugrep](https://github.com/Genivia/ugrep) | `ugrep -r --ignore-files --no-hidden -I -w '[A-Z]+_SUSPEND'` | 536 | 0.639s (7.82x) |
| [git grep](https://www.kernel.org/pub/software/scm/git/docs/git-grep.html) | `LC_ALL=C git grep -E -n -w '[A-Z]+_SUSPEND'` | 536 | 0.727s (8.91x) |
| [git grep (Unicode)](https://www.kernel.org/pub/software/scm/git/docs/git-grep.html) | `LC_ALL=en_US.UTF-8 git grep -E -n -w '[A-Z]+_SUSPEND'` | 536 | 2.670s (32.70x) |
| [ack](https://github.com/beyondgrep/ack3) | `ack -w '[A-Z]+_SUSPEND'` | 2677 | 2.935s (35.94x) |

Here's another benchmark on the same corpus as above that disregards gitignore
files and searches with a whitelist instead. The corpus is the same as in the
previous benchmark, and the flags passed to each command ensure that they are
doing equivalent work:

| Tool | Command | Line count | Time |
| ---- | ------- | ---------- | ---- |
| ripgrep | `rg -uuu -tc -n -w '[A-Z]+_SUSPEND'` | 447 | **0.063s** (1.00x) |
| [ugrep](https://github.com/Genivia/ugrep) | `ugrep -r -n --include='*.c' --include='*.h' -w '[A-Z]+_SUSPEND'` | 447 | 0.607s (9.62x) |
| [GNU grep](https://www.gnu.org/software/grep/) | `grep -E -r -n --include='*.c' --include='*.h' -w '[A-Z]+_SUSPEND'` | 447 | 0.674s (10.69x) |

Now we'll move to searching on single large file. Here is a straight-up
comparison between ripgrep, ugrep and GNU grep on a file cached in memory
(~13GB, [`OpenSubtitles.raw.en.gz`](http://opus.nlpl.eu/download.php?f=OpenSubtitles/v2018/mono/OpenSubtitles.raw.en.gz), decompressed):

| Tool | Command | Line count | Time |
| ---- | ------- | ---------- | ---- |
| ripgrep (Unicode) | `rg -w 'Sherlock [A-Z]\w+'` | 7882 | **1.042s** (1.00x) |
| [ugrep](https://github.com/Genivia/ugrep) | `ugrep -w 'Sherlock [A-Z]\w+'` | 7882 | 1.339s (1.28x) |
| [GNU grep (Unicode)](https://www.gnu.org/software/grep/) | `LC_ALL=en_US.UTF-8 egrep -w 'Sherlock [A-Z]\w+'` | 7882 | 6.577s (6.31x) |

In the above benchmark, passing the `-n` flag (for showing line numbers)
increases the times to `1.664s` for ripgrep and `9.484s` for GNU grep. ugrep
times are unaffected by the presence or absence of `-n`.

Beware of performance cliffs though:

| Tool | Command | Line count | Time |
| ---- | ------- | ---------- | ---- |
| ripgrep (Unicode) | `rg -w '[A-Z]\w+ Sherlock [A-Z]\w+'` | 485 | **1.053s** (1.00x) |
| [GNU grep (Unicode)](https://www.gnu.org/software/grep/) | `LC_ALL=en_US.UTF-8 grep -E -w '[A-Z]\w+ Sherlock [A-Z]\w+'` | 485 | 6.234s (5.92x) |
| [ugrep](https://github.com/Genivia/ugrep) | `ugrep -w '[A-Z]\w+ Sherlock [A-Z]\w+'` | 485 | 28.973s (27.51x) |

And performance can drop precipitously across the board when searching big
files for patterns without any opportunities for literal optimizations:

| Tool | Command | Line count | Time |
| ---- | ------- | ---------- | ---- |
| ripgrep | `rg '[A-Za-z]{30}'` | 6749 | **15.569s** (1.00x) |
| [ugrep](https://github.com/Genivia/ugrep) | `ugrep -E '[A-Za-z]{30}'` | 6749 | 21.857s (1.40x) |
| [GNU grep](https://www.gnu.org/software/grep/) | `LC_ALL=C grep -E '[A-Za-z]{30}'` | 6749 | 32.409s (2.08x) |
| [GNU grep (Unicode)](https://www.gnu.org/software/grep/) | `LC_ALL=en_US.UTF-8 grep -E '[A-Za-z]{30}'` | 6795 | 8m30s (32.74x) |

Finally, high match counts also tend to both tank performance and smooth
out the differences between tools (because performance is dominated by how
quickly one can handle a match and not the algorithm used to detect the match,
generally speaking):

| Tool | Command | Line count | Time |
| ---- | ------- | ---------- | ---- |
| ripgrep | `rg the` | 83499915 | **6.948s** (1.00x) |
| [ugrep](https://github.com/Genivia/ugrep) | `ugrep the` | 83499915 | 11.721s (1.69x) |
| [GNU grep](https://www.gnu.org/software/grep/) | `LC_ALL=C grep the` | 83499915 | 15.217s (2.19x) |

### Why should I use ripgrep?

* It can replace many use cases served by other search tools
  because it contains most of their features and is generally faster. (See
  [the FAQ](FAQ.md#posix4ever) for more details on whether ripgrep can truly
  replace grep.)
* Like other tools specialized to code search, ripgrep defaults to
  [recursive search](GUIDE.md#recursive-search) and does [automatic
  filtering](GUIDE.md#automatic-filtering). Namely, ripgrep won't search files
  ignored by your `.gitignore`/`.ignore`/`.rgignore` files, it won't search
  hidden files and it won't search binary files. Automatic filtering can be
  disabled with `rg -uuu`.
* ripgrep can [search specific types of files](GUIDE.md#manual-filtering-file-types).
  For example, `rg -tpy foo` limits your search to Python files and `rg -Tjs
  foo` excludes JavaScript files from your search. ripgrep can be taught about
  new file types with custom matching rules.
* ripgrep supports many features found in `grep`, such as showing the context
  of search results, searching multiple patterns, highlighting matches with
  color and full Unicode support. Unlike GNU grep, ripgrep stays fast while
  supporting Unicode (which is always on).
* ripgrep has optional support for switching its regex engine to use PCRE2.
  Among other things, this makes it possible to use look-around and
  backreferences in your patterns, which are not supported in ripgrep's default
  regex engine. PCRE2 support can be enabled with `-P/--pcre2` (use PCRE2
  always) or `--auto-hybrid-regex` (use PCRE2 only if needed). An alternative
  syntax is provided via the `--engine (default|pcre2|auto)` option.
* ripgrep has [rudimentary support for replacements](GUIDE.md#replacements),
  which permit rewriting output based on what was matched.
* ripgrep supports [searching files in text encodings](GUIDE.md#file-encoding)
  other than UTF-8, such as UTF-16, latin-1, GBK, EUC-JP, Shift_JIS and more.
  (Some support for automatically detecting UTF-16 is provided. Other text
  encodings must be specifically specified with the `-E/--encoding` flag.)
* ripgrep supports searching files compressed in a common format (brotli,
  bzip2, gzip, lz4, lzma, xz, or zstandard) with the `-z/--search-zip` flag.
* ripgrep supports
  [arbitrary input preprocessing filters](GUIDE.md#preprocessor)
  which could be PDF text extraction, less supported decompression, decrypting,
  automatic encoding detection and so on.
* ripgrep can be configured via a
  [configuration file](GUIDE.md#configuration-file).

In other words, use ripgrep if you like speed, filtering by default, fewer
bugs and Unicode support.


### Why shouldn't I use ripgrep?

Despite initially not wanting to add every feature under the sun to ripgrep,
over time, ripgrep has grown support for most features found in other file
searching tools. This includes searching for results spanning across multiple
lines, and opt-in support for PCRE2, which provides look-around and
backreference support.

At this point, the primary reasons not to use ripgrep probably consist of one
or more of the following:

* You need a portable and ubiquitous tool. While ripgrep works on Windows,
  macOS and Linux, it is not ubiquitous and it does not conform to any
  standard such as POSIX. The best tool for this job is good old grep.
* There still exists some other feature (or bug) not listed in this README that
  you rely on that's in another tool that isn't in ripgrep.
* There is a performance edge case where ripgrep doesn't do well where another
  tool does do well. (Please file a bug report!)
* ripgrep isn't possible to install on your machine or isn't available for your
  platform. (Please file a bug report!)


### Is it really faster than everything else?

Generally, yes. A large number of benchmarks with detailed analysis for each is
[available on my blog](https://blog.burntsushi.net/ripgrep/).

Summarizing, ripgrep is fast because:

* It is built on top of
  [Rust's regex engine](https://github.com/rust-lang/regex).
  Rust's regex engine uses finite automata, SIMD and aggressive literal
  optimizations to make searching very fast. (PCRE2 support can be opted into
  with the `-P/--pcre2` flag.)
* Rust's regex library maintains performance with full Unicode support by
  building UTF-8 decoding directly into its deterministic finite automaton
  engine.
* It supports searching with either memory maps or by searching incrementally
  with an intermediate buffer. The former is better for single files and the
  latter is better for large directories. ripgrep chooses the best searching
  strategy for you automatically.
* Applies your ignore patterns in `.gitignore` files using a
  [`RegexSet`](https://docs.rs/regex/1/regex/struct.RegexSet.html).
  That means a single file path can be matched against multiple glob patterns
  simultaneously.
* It uses a lock-free parallel recursive directory iterator, courtesy of
  [`crossbeam`](https://docs.rs/crossbeam) and
  [`ignore`](https://docs.rs/ignore).


### Feature comparison

Andy Lester, author of [ack](https://beyondgrep.com/), has published an
excellent table comparing the features of ack, ag, git-grep, GNU grep and
ripgrep: https://beyondgrep.com/feature-comparison/

Note that ripgrep has grown a few significant new features recently that
are not yet present in Andy's table. This includes, but is not limited to,
configuration files, passthru, support for searching compressed files,
multiline search and opt-in fancy regex support via PCRE2.


### Playground

If you'd like to try ripgrep before installing, there's an unofficial
[playground](https://codapi.org/ripgrep/) and an [interactive
tutorial](https://codapi.org/try/ripgrep/).

If you have any questions about these, please open an issue in the [tutorial
repo](https://github.com/nalgeon/tryxinyminutes).


### Installation

The binary name for ripgrep is `rg`.

**[Archives of precompiled binaries for ripgrep are available for Windows,
macOS and Linux.](https://github.com/BurntSushi/ripgrep/releases)** Linux and
Windows binaries are static executables. Users of platforms not explicitly
mentioned below are advised to download one of these archives.

If you're a **macOS Homebrew** or a **Linuxbrew** user, then you can install
ripgrep from homebrew-core:

```
$ brew install ripgrep
```

If you're a **MacPorts** user, then you can install ripgrep from the
[official ports](https://www.macports.org/ports.php?by=name&substr=ripgrep):

```
$ sudo port install ripgrep
```

If you're a **Windows Chocolatey** user, then you can install ripgrep from the
[official repo](https://chocolatey.org/packages/ripgrep):

```
$ choco install ripgrep
```

If you're a **Windows Scoop** user, then you can install ripgrep from the
[official bucket](https://github.com/ScoopInstaller/Main/blob/master/bucket/ripgrep.json):

```
$ scoop install ripgrep
```

If you're a **Windows Winget** user, then you can install ripgrep from the
[winget-pkgs](https://github.com/microsoft/winget-pkgs/tree/master/manifests/b/BurntSushi/ripgrep)
repository:

```
$ winget install BurntSushi.ripgrep.MSVC
```

If you're an **Arch Linux** user, then you can install ripgrep from the official repos:

```
$ sudo pacman -S ripgrep
```

If you're a **Gentoo** user, you can install ripgrep from the
[official repo](https://packages.gentoo.org/packages/sys-apps/ripgrep):

```
$ sudo emerge sys-apps/ripgrep
```

If you're a **Fedora** user, you can install ripgrep from official
repositories.

```
$ sudo dnf install ripgrep
```

If you're an **openSUSE** user, ripgrep is included in **openSUSE Tumbleweed**
and **openSUSE Leap** since 15.1.

```
$ sudo zypper install ripgrep
```

If you're a **CentOS Stream 10** user, you can install ripgrep from the
[EPEL](https://docs.fedoraproject.org/en-US/epel/getting-started/) repository:

```
$ sudo dnf config-manager --set-enabled crb
$ sudo dnf install https://dl.fedoraproject.org/pub/epel/epel-release-latest-10.noarch.rpm
$ sudo dnf install ripgrep
```

If you're a **Red Hat 10** user, you can install ripgrep from the
[EPEL](https://docs.fedoraproject.org/en-US/epel/getting-started/) repository:

```
$ sudo subscription-manager repos --enable codeready-builder-for-rhel-10-$(arch)-rpms
$ sudo dnf install https://dl.fedoraproject.org/pub/epel/epel-release-latest-10.noarch.rpm
$ sudo dnf install ripgrep
```

If you're a **Rocky Linux 10** user, you can install ripgrep from the
[EPEL](https://docs.fedoraproject.org/en-US/epel/getting-started/) repository:

```
$ sudo dnf install https://dl.fedoraproject.org/pub/epel/epel-release-lat
... [TRUNCATED]
```

### File: fuzz\README.md
```md
# Fuzz Testing

## Introduction

Fuzz testing produces pseudo-random / arbitrary data that is used to find
stability issues within a code base. While Rust provides a strong type system,
this does not guarantee that an object will convert properly from one struct
to another. It is the responsibility of the developer to ensure that a struct
is converted properly. Fuzz testing will generate input within the domain of
each property. This arbitrary data can then be used to convert from ObjectA
to ObjectB and then back. This type of testing will help catch bugs that the
type system is not able to see.

## Installation

This crate relies on the `cargo-fuzz` component. To install this component,
run the following from the `fuzz` directory:

```bash
cargo install cargo-fuzz
```

## Listing Targets

Once installed, fuzz targets can be listed by running the following command:

```bash
cargo fuzz list
```

This command will print out a list of all targets that can be tested.

## Running Fuzz Tests

To run a fuzz test, the target must be specified:

```bash
cargo fuzz run <target>
```

Note that the above will run the fuzz test indefinitely. Use the
`-max_total_time=<num seconds>` flag to specify how many seconds the test
should run for:

```bash
cargo fuzz run <target> -- -max_total_time=5
```

The above command will run the fuzz test for five seconds. If the test
completes without error it will show how many tests were run successfully.
The test will abort and return a non-zero error code if it is able to produce
an error. The arbitrary input will be displayed in the event of a failure.

```

### File: crates\cli\README.md
```md
grep-cli
--------
A utility library that provides common routines desired in search oriented
command line applications. This includes, but is not limited to, parsing hex
escapes, detecting whether stdin is readable and more. To the extent possible,
this crate strives for compatibility across Windows, macOS and Linux.

[![Build status](https://github.com/BurntSushi/ripgrep/workflows/ci/badge.svg)](https://github.com/BurntSushi/ripgrep/actions)
[![](https://img.shields.io/crates/v/grep-cli.svg)](https://crates.io/crates/grep-cli)

Dual-licensed under MIT or the [UNLICENSE](https://unlicense.org/).


### Documentation

[https://docs.rs/grep-cli](https://docs.rs/grep-cli)

**NOTE:** You probably don't want to use this crate directly. Instead, you
should prefer the facade defined in the
[`grep`](https://docs.rs/grep)
crate.


### Usage

Add this to your `Cargo.toml`:

```toml
[dependencies]
grep-cli = "0.1"
```

```

### File: crates\core\README.md
```md
ripgrep core
------------
This is the core ripgrep crate. In particular, `main.rs` is where the `main`
function lives.

Most of ripgrep core consists of two things:

* The definition of the CLI interface, including docs for every flag.
* Glue code that brings the `grep-matcher`, `grep-regex`, `grep-searcher` and
  `grep-printer` crates together to actually execute the search.

Currently, there are no plans to make ripgrep core available as an independent
library. However, much of the heavy lifting of ripgrep is done via its
constituent crates, which can be reused independent of ripgrep. Unfortunately,
there is no guide or tutorial to teach folks how to do this yet.

```

### File: crates\grep\README.md
```md
grep
----
ripgrep, as a library.

[![Build status](https://github.com/BurntSushi/ripgrep/workflows/ci/badge.svg)](https://github.com/BurntSushi/ripgrep/actions)
[![](https://img.shields.io/crates/v/grep.svg)](https://crates.io/crates/grep)

Dual-licensed under MIT or the [UNLICENSE](https://unlicense.org/).


### Documentation

[https://docs.rs/grep](https://docs.rs/grep)

NOTE: This crate isn't ready for wide use yet. Ambitious individuals can
probably piece together the parts, but there is no high level documentation
describing how all of the pieces fit together.


### Usage

Add this to your `Cargo.toml`:

```toml
[dependencies]
grep = "0.2"
```


### Features

This crate provides a `pcre2` feature (disabled by default) which, when
enabled, re-exports the `grep-pcre2` crate as an alternative `Matcher`
implementation to the standard `grep-regex` implementation.

```

### File: pkg\windows\README.md
```md
This directory contains a Windows manifest for various Windows-specific
settings.

The main thing we enable here is [`longPathAware`], which permits paths of the
form `C:\` to be longer than 260 characters.

The approach taken here was modeled off of a [similar change for `rustc`][rustc pr].
In particular, this manifest gets linked into the final binary. Those linker
arguments are applied in `build.rs`.

This currently only applies to MSVC builds. If there's an easy way to make this
apply to GNU builds as well, then patches are welcome.

[`longPathAware`]: https://learn.microsoft.com/en-us/windows/win32/sbscs/application-manifests#longpathaware
[rustc pr]: https://github.com/rust-lang/rust/pull/96737

```

### File: build.rs
```rs
fn main() {
    set_git_revision_hash();
    set_windows_exe_options();
}

/// Embed a Windows manifest and set some linker options.
///
/// The main reason for this is to enable long path support on Windows. This
/// still, I believe, requires enabling long path support in the registry. But
/// if that's enabled, then this will let ripgrep use C:\... style paths that
/// are longer than 260 characters.
fn set_windows_exe_options() {
    static MANIFEST: &str = "pkg/windows/Manifest.xml";

    let Ok(target_os) = std::env::var("CARGO_CFG_TARGET_OS") else { return };
    let Ok(target_env) = std::env::var("CARGO_CFG_TARGET_ENV") else { return };
    if !(target_os == "windows" && target_env == "msvc") {
        return;
    }

    let Ok(mut manifest) = std::env::current_dir() else { return };
    manifest.push(MANIFEST);
    let Some(manifest) = manifest.to_str() else { return };

    println!("cargo:rerun-if-changed={MANIFEST}");
    // Embed the Windows application manifest file.
    println!("cargo:rustc-link-arg-bin=rg=/MANIFEST:EMBED");
    println!("cargo:rustc-link-arg-bin=rg=/MANIFESTINPUT:{manifest}");
    // Turn linker warnings into errors. Helps debugging, otherwise the
    // warnings get squashed (I believe).
    println!("cargo:rustc-link-arg-bin=rg=/WX");
}

/// Make the current git hash available to the build as the environment
/// variable `RIPGREP_BUILD_GIT_HASH`.
fn set_git_revision_hash() {
    use std::process::Command;

    let args = &["rev-parse", "--short=10", "HEAD"];
    let output = Command::new("git").args(args).output();
    match output {
        Ok(output) => {
            let rev =
                String::from_utf8_lossy(&output.stdout).trim().to_string();
            if rev.is_empty() {
                println!(
                    "cargo:warning=output from `git rev-parse` is empty, \
                     so skipping embedding of commit hash"
                );
                return;
            }
            println!("cargo:rustc-env=RIPGREP_BUILD_GIT_HASH={rev}");
        }
        Err(e) => {
            println!(
                "cargo:warning=failed to run `git rev-parse`, \
                 so skipping embedding of commit hash: {e}"
            );
        }
    }
}

```

### File: CHANGELOG.md
```md
TBD
===
Unreleased changes. Release notes have not yet been written.

Bug fixes:

* [BUG #3212](https://github.com/BurntSushi/ripgrep/pull/3212):
  Don't check for the existence of `.jj` when `--no-ignore` is used.


15.1.0
======
This is a small release that fixes a bug with how ripgrep handles line
buffering. This might manifest as ripgrep printing output later than you
expect or not working correctly with `tail -f` (even if you're using the
`--line-buffered` flag).

Bug fixes:

* [BUG #3194](https://github.com/BurntSushi/ripgrep/issues/3194):
  Fix a regression with `--line-buffered` introduced in ripgrep 15.0.0.

Feature enhancements:

* [FEATURE #3192](https://github.com/BurntSushi/ripgrep/pull/3192):
  Add hyperlink alias for Cursor.


15.0.0 (2025-10-15)
===================
ripgrep 15 is a new major version release of ripgrep that mostly has bug fixes,
some minor performance improvements and minor new features. Here are some
highlights:

* Several bugs around gitignore matching have been fixed. This includes
  a commonly reported bug related to applying gitignore rules from parent
  directories.
* A memory usage regression when handling very large gitignore files has been
  fixed.
* `rg -vf file`, where `file` is empty, now matches everything.
* The `-r/--replace` flag now works with `--json`.
* A subset of Jujutsu (`jj`) repositories are now treated as if they were git
  repositories. That is, ripgrep will respect `jj`'s gitignores.
* Globs can now use nested curly braces.

Platform support:

* `aarch64` for Windows now has release artifacts.
* `powerpc64` no longer has release artifacts generated for it. The CI
  release workflow stopped working, and I didn't deem it worth my time to
  debug it. If someone wants this and can test it, I'd be happy to add it
  back.
* ripgrep binaries are now compiled with full LTO enabled. You may notice
  small performance improvements from this and a modest decrease in binary
  size.

Performance improvements:

* [PERF #2111](https://github.com/BurntSushi/ripgrep/issues/2111):
  Don't resolve helper binaries on Windows when `-z/--search-zip` isn't used.
* [PERF #2865](https://github.com/BurntSushi/ripgrep/pull/2865):
  Avoid using path canonicalization on Windows when emitting hyperlinks.

Bug fixes:

* [BUG #829](https://github.com/BurntSushi/ripgrep/issues/829),
  [BUG #2731](https://github.com/BurntSushi/ripgrep/issues/2731),
  [BUG #2747](https://github.com/BurntSushi/ripgrep/issues/2747),
  [BUG #2770](https://github.com/BurntSushi/ripgrep/issues/2770),
  [BUG #2778](https://github.com/BurntSushi/ripgrep/issues/2778),
  [BUG #2836](https://github.com/BurntSushi/ripgrep/issues/2836),
  [BUG #2933](https://github.com/BurntSushi/ripgrep/pull/2933),
  [BUG #3067](https://github.com/BurntSushi/ripgrep/pull/3067):
  Fix bug related to gitignores from parent directories.
* [BUG #1332](https://github.com/BurntSushi/ripgrep/issues/1332),
  [BUG #3001](https://github.com/BurntSushi/ripgrep/issues/3001):
  Make `rg -vf file` where `file` is empty match everything.
* [BUG #2177](https://github.com/BurntSushi/ripgrep/issues/2177):
  Ignore a UTF-8 BOM marker at the start of `.gitignore` (and similar files).
* [BUG #2750](https://github.com/BurntSushi/ripgrep/issues/2750):
  Fix memory usage regression for some truly large gitignore files.
* [BUG #2944](https://github.com/BurntSushi/ripgrep/pull/2944):
  Fix a bug where the "bytes searched" in `--stats` output could be incorrect.
* [BUG #2990](https://github.com/BurntSushi/ripgrep/issues/2990):
  Fix a bug where ripgrep would mishandle globs that ended with a `.`.
* [BUG #2094](https://github.com/BurntSushi/ripgrep/issues/2094),
  [BUG #3076](https://github.com/BurntSushi/ripgrep/issues/3076):
  Fix bug with `-m/--max-count` and `-U/--multiline` showing too many matches.
* [BUG #3100](https://github.com/BurntSushi/ripgrep/pull/3100):
  Preserve line terminators when using `-r/--replace` flag.
* [BUG #3108](https://github.com/BurntSushi/ripgrep/issues/3108):
  Fix a bug where `-q --files-without-match` inverted the exit code.
* [BUG #3131](https://github.com/BurntSushi/ripgrep/issues/3131):
  Document inconsistency between `-c/--count` and `--files-with-matches`.
* [BUG #3135](https://github.com/BurntSushi/ripgrep/issues/3135):
  Fix rare panic for some classes of large regexes on large haystacks.
* [BUG #3140](https://github.com/BurntSushi/ripgrep/issues/3140):
  Ensure hyphens in flag names are escaped in the roff text for the man page.
* [BUG #3155](https://github.com/BurntSushi/ripgrep/issues/3155):
  Statically compile PCRE2 into macOS release artifacts on `aarch64`.
* [BUG #3173](https://github.com/BurntSushi/ripgrep/issues/3173):
  Fix ancestor ignore filter bug when searching whitelisted hidden files.
* [BUG #3178](https://github.com/BurntSushi/ripgrep/discussions/3178):
  Fix bug causing incorrect summary statistics with `--json` flag.
* [BUG #3179](https://github.com/BurntSushi/ripgrep/issues/3179):
  Fix gitignore bug when searching absolute paths with global gitignores.
* [BUG #3180](https://github.com/BurntSushi/ripgrep/issues/3180):
  Fix a panicking bug when using `-U/--multiline` and `-r/--replace`.

Feature enhancements:

* Many enhancements to the default set of file types available for filtering.
* [FEATURE #1872](https://github.com/BurntSushi/ripgrep/issues/1872):
  Make `-r/--replace` work with `--json`.
* [FEATURE #2708](https://github.com/BurntSushi/ripgrep/pull/2708):
  Completions for the fish shell take ripgrep's config file into account.
* [FEATURE #2841](https://github.com/BurntSushi/ripgrep/pull/2841):
  Add `italic` to the list of available style attributes in `--color`.
* [FEATURE #2842](https://github.com/BurntSushi/ripgrep/pull/2842):
  Directories containing `.jj` are now treated as git repositories.
* [FEATURE #2849](https://github.com/BurntSushi/ripgrep/pull/2849):
  When using multithreading, schedule files to search in order given on CLI.
* [FEATURE #2943](https://github.com/BurntSushi/ripgrep/issues/2943):
  Add `aarch64` release artifacts for Windows.
* [FEATURE #3024](https://github.com/BurntSushi/ripgrep/issues/3024):
  Add `highlight` color type, for styling non-matching text in a matching line.
* [FEATURE #3048](https://github.com/BurntSushi/ripgrep/pull/3048):
  Globs in ripgrep (and the `globset` crate) now support nested alternates.
* [FEATURE #3096](https://github.com/BurntSushi/ripgrep/pull/3096):
  Improve completions for `--hyperlink-format` in bash and fish.
* [FEATURE #3102](https://github.com/BurntSushi/ripgrep/pull/3102):
  Improve completions for `--hyperlink-format` in zsh.


14.1.1 (2024-09-08)
===================
This is a minor release with a bug fix for a matching bug. In particular, a bug
was found that could cause ripgrep to ignore lines that should match. That is,
false negatives. It is difficult to characterize the specific set of regexes
in which this occurs as it requires multiple different optimization strategies
to collide and produce an incorrect result. But as one reported example, in
ripgrep, the regex `(?i:e.x|ex)` does not match `e-x` when it should. (This
bug is a result of an inner literal optimization performed in the `grep-regex`
crate and not in the `regex` crate.)

Bug fixes:

* [BUG #2884](https://github.com/BurntSushi/ripgrep/issues/2884):
  Fix bug where ripgrep could miss some matches that it should report.

Miscellaneous:

* [MISC #2748](https://github.com/BurntSushi/ripgrep/issues/2748):
  Remove ripgrep's `simd-accel` feature because it was frequently broken.


14.1.0 (2024-01-06)
===================
This is a minor release with a few small new features and bug fixes. This
release contains a bug fix for unbounded memory growth while walking a
directory tree. This release also includes improvements to the completions for
the `fish` shell, and release binaries for several additional ARM targets.

Bug fixes:

* [BUG #2664](https://github.com/BurntSushi/ripgrep/issues/2690):
  Fix unbounded memory growth in the `ignore` crate.

Feature enhancements:

* Added or improved file type filtering for Lean and Meson.
* [FEATURE #2684](https://github.com/BurntSushi/ripgrep/issues/2684):
  Improve completions for the `fish` shell.
* [FEATURE #2702](https://github.com/BurntSushi/ripgrep/pull/2702):
  Add release binaries for `armv7-unknown-linux-gnueabihf`,
  `armv7-unknown-linux-musleabihf` and `armv7-unknown-linux-musleabi`.


14.0.3 (2023-11-28)
===================
This is a patch release with a bug fix for the `--sortr` flag.

Bug fixes:

* [BUG #2664](https://github.com/BurntSushi/ripgrep/issues/2664):
  Fix `--sortr=path`. I left a `todo!()` in the source. Oof.


14.0.2 (2023-11-27)
===================
This is a patch release with a few small bug fixes.

Bug fixes:

* [BUG #2654](https://github.com/BurntSushi/ripgrep/issues/2654):
  Fix `deb` release sha256 sum file.
* [BUG #2658](https://github.com/BurntSushi/ripgrep/issues/2658):
  Fix partial regression in the behavior of `--null-data --line-regexp`.
* [BUG #2659](https://github.com/BurntSushi/ripgrep/issues/2659):
  Fix Fish shell completions.
* [BUG #2662](https://github.com/BurntSushi/ripgrep/issues/2662):
  Fix typo in documentation for `-i/--ignore-case`.


14.0.1 (2023-11-26)
===================
This a patch release meant to fix `cargo install ripgrep` on Windows.

Bug fixes:

* [BUG #2653](https://github.com/BurntSushi/ripgrep/issues/2653):
  Include `pkg/windows/Manifest.xml` in crate package.


14.0.0 (2023-11-26)
===================
ripgrep 14 is a new major version release of ripgrep that has some new
features, performance improvements and a lot of bug fixes.

The headlining feature in this release is hyperlink support. In this release,
they are an opt-in feature but may change to an opt-out feature in the future.
To enable them, try passing `--hyperlink-format default`. If you use [VS Code],
then try passing `--hyperlink-format vscode`. Please [report your experience
with hyperlinks][report-hyperlinks], positive or negative.

[VS Code]: https://code.visualstudio.com/
[report-hyperlinks]: https://github.com/BurntSushi/ripgrep/discussions/2611

Another headlining development in this release is that it contains a rewrite
of its regex engine. You generally shouldn't notice any changes, except for
some searches may get faster. You can read more about the [regex engine rewrite
on my blog][regex-internals]. Please [report your performance improvements or
regressions that you notice][report-perf].

[report-perf]: https://github.com/BurntSushi/ripgrep/discussions/2652

Finally, ripgrep switched the library it uses for argument parsing. Users
should not notice a difference in most cases (error messages have changed
somewhat), but flag overrides should generally be more consistent. For example,
things like `--no-ignore --ignore-vcs` work as one would expect (disables all
filtering related to ignore rules except for rules found in version control
systems such as `git`).

[regex-internals]: https://blog.burntsushi.net/regex-internals/

**BREAKING CHANGES**:

* `rg -C1 -A2` used to be equivalent to `rg -A2`, but now it is equivalent to
  `rg -B1 -A2`. That is, `-A` and `-B` no longer completely override `-C`.
  Instead, they only partially override `-C`.

Build process changes:

* ripgrep's shell completions and man page are now created by running ripgrep
with a new `--generate` flag. For example, `rg --generate man` will write a
man page in `roff` format on stdout. The release archives have not changed.
* The optional build dependency on `asciidoc` or `asciidoctor` has been
dropped. Previously, it was used to produce ripgrep's man page. ripgrep now
owns this process itself by writing `roff` directly.

Performance improvements:

* [PERF #1746](https://github.com/BurntSushi/ripgrep/issues/1746):
  Make some cases with inner literals faster.
* [PERF #1760](https://github.com/BurntSushi/ripgrep/issues/1760):
  Make most searches with `\b` look-arounds (among others) much faster.
* [PERF #2591](https://github.com/BurntSushi/ripgrep/pull/2591):
  Parallel directory traversal now uses work stealing for faster searches.
* [PERF #2642](https://github.com/BurntSushi/ripgrep/pull/2642):
  Parallel directory traversal has some contention reduced.

Feature enhancements:

* Added or improved file type filtering for Ada, DITA, Elixir, Fuchsia, Gentoo,
  Gradle, GraphQL, Markdown, Prolog, Raku, TypeScript, USD, V
* [FEATURE #665](https://github.com/BurntSushi/ripgrep/issues/665):
  Add a new `--hyperlink-format` flag that turns file paths into hyperlinks.
* [FEATURE #1709](https://github.com/BurntSushi/ripgrep/issues/1709):
  Improve documentation of ripgrep's behavior when stdout is a tty.
* [FEATURE #1737](https://github.com/BurntSushi/ripgrep/issues/1737):
  Provide binaries for Apple silicon.
* [FEATURE #1790](https://github.com/BurntSushi/ripgrep/issues/1790):
  Add new `--stop-on-nonmatch` flag.
* [FEATURE #1814](https://github.com/BurntSushi/ripgrep/issues/1814):
  Flags are now categorized in `-h/--help` output and ripgrep's man page.
* [FEATURE #1838](https://github.com/BurntSushi/ripgrep/issues/1838):
  An error is shown when searching for NUL bytes with binary detection enabled.
* [FEATURE #2195](https://github.com/BurntSushi/ripgrep/issues/2195):
  When `extra-verbose` mode is enabled in zsh, show extra file type info.
* [FEATURE #2298](https://github.com/BurntSushi/ripgrep/issues/2298):
  Add instructions for installing ripgrep using `cargo binstall`.
* [FEATURE #2409](https://github.com/BurntSushi/ripgrep/pull/2409):
  Added installation instructions for `winget`.
* [FEATURE #2425](https://github.com/BurntSushi/ripgrep/pull/2425):
  Shell completions (and man page) can be created via `rg --generate`.
* [FEATURE #2524](https://github.com/BurntSushi/ripgrep/issues/2524):
  The `--debug` flag now indicates whether stdin or `./` is being searched.
* [FEATURE #2643](https://github.com/BurntSushi/ripgrep/issues/2643):
  Make `-d` a short flag for `--max-depth`.
* [FEATURE #2645](https://github.com/BurntSushi/ripgrep/issues/2645):
  The `--version` output will now also contain PCRE2 availability information.

Bug fixes:

* [BUG #884](https://github.com/BurntSushi/ripgrep/issues/884):
  Don't error when `-v/--invert-match` is used multiple times.
* [BUG #1275](https://github.com/BurntSushi/ripgrep/issues/1275):
  Fix bug with `\b` assertion in the regex engine.
* [BUG #1376](https://github.com/BurntSushi/ripgrep/issues/1376):
  Using `--no-ignore --ignore-vcs` now works as one would expect.
* [BUG #1622](https://github.com/BurntSushi/ripgrep/issues/1622):
  Add note about error messages to `-z/--search-zip` documentation.
* [BUG #1648](https://github.com/BurntSushi/ripgrep/issues/1648):
  Fix bug where sometimes short flags with values, e.g., `-M 900`, would fail.
* [BUG #1701](https://github.com/BurntSushi/ripgrep/issues/1701):
  Fix bug where some flags could not be repeated.
* [BUG #1757](https://github.co
... [TRUNCATED]
```

### File: FAQ.md
```md
## FAQ

* [Does ripgrep support configuration files?](#config)
* [What's changed in ripgrep recently?](#changelog)
* [When is the next release?](#release)
* [Does ripgrep have a man page?](#manpage)
* [Does ripgrep have support for shell auto-completion?](#complete)
* [How can I get results in a consistent order?](#order)
* [How do I search files that aren't UTF-8?](#encoding)
* [How do I search compressed files?](#compressed)
* [How do I search over multiple lines?](#multiline)
* [How do I use lookaround and/or backreferences?](#fancy)
* [How do I configure ripgrep's colors?](#colors)
* [How do I enable true colors on Windows?](#truecolors-windows)
* [How do I stop ripgrep from messing up colors when I kill it?](#stop-ripgrep)
* [Why does using a leading `/` on Windows fail?](#because-cygwin)
* [How do I get around the regex size limit?](#size-limit)
* [How do I make the `-f/--file` flag faster?](#dfa-size)
* [How do I make the output look like The Silver Searcher's output?](#silver-searcher-output)
* [Why does ripgrep get slower when I enabled PCRE2 regexes?](#pcre2-slow)
* [When I run `rg`, why does it execute some other command?](#rg-other-cmd)
* [How do I create an alias for ripgrep on Windows?](#rg-alias-windows)
* [How do I create a PowerShell profile?](#powershell-profile)
* [How do I pipe non-ASCII content to ripgrep on Windows?](#pipe-non-ascii-windows)
* [How can I search and replace with ripgrep?](#search-and-replace)
* [How is ripgrep licensed?](#license)
* [Can ripgrep replace grep?](#posix4ever)
* [What does the "rip" in ripgrep mean?](#intentcountsforsomething)
* [How can I donate to ripgrep or its maintainers?](#donations)


<h3 name="config">
Does ripgrep support configuration files?
</h3>

Yes. See the
[guide's section on configuration files](GUIDE.md#configuration-file).


<h3 name="changelog">
What's changed in ripgrep recently?
</h3>

Please consult ripgrep's [CHANGELOG](CHANGELOG.md).


<h3 name="release">
When is the next release?
</h3>

ripgrep is a project whose contributors are volunteers. A release schedule
adds undue stress to said volunteers. Therefore, releases are made on a best
effort basis and no dates **will ever be given**.

An exception to this _can be_ high impact bugs. If a ripgrep release contains
a significant regression, then there will generally be a strong push to get a
patch release out with a fix. However, no promises are made.


<h3 name="manpage">
Does ripgrep have a man page?
</h3>

Yes. If you installed ripgrep through a package manager on a Unix system, then
it would have ideally been installed for you in the proper location. In which
case, `man rg` should just work.

Otherwise, you can ask ripgrep to generate the man page:

```
$ mkdir -p man/man1
$ rg --generate man > man/man1/rg.1
$ MANPATH="$PWD/man" man rg
```

Or, if your version of `man` supports the `-l/--local-file` flag, then this
will suffice:

```
$ rg --generate man | man -l -
```

Note that the man page's documentation for options is equivalent to the output
shown in `rg --help`. To see more condensed documentation (one line per flag),
run `rg -h`.

The man page is also included in all
[ripgrep binary releases](https://github.com/BurntSushi/ripgrep/releases).


<h3 name="complete">
Does ripgrep have support for shell auto-completion?
</h3>

Yes! If you installed ripgrep through a package manager on a Unix system, then
the shell completion files included in the release archive should have been
installed for you automatically. If not, you can generate completions using
ripgrep's command line interface.

For **bash**:

```
$ dir="$XDG_CONFIG_HOME/bash_completion"
$ mkdir -p "$dir"
$ rg --generate complete-bash > "$dir/rg.bash"
```

For **fish**:

```
$ dir="$XDG_CONFIG_HOME/fish/completions"
$ mkdir -p "$dir"
$ rg --generate complete-fish > "$dir/rg.fish"
```

For **zsh**, the recommended approach is:

```zsh
$ dir="$HOME/.zsh-complete"
$ mkdir -p "$dir"
$ rg --generate complete-zsh > "$dir/_rg"
```

And then add `$HOME/.zsh-complete` to your `fpath` in, e.g., your
`$HOME/.zshrc` file:

```zsh
fpath=($HOME/.zsh-complete $fpath)
```

Or if you'd prefer to load and generate completions at the same time, you can
add the following to your `$HOME/.zshrc` file:

```zsh
$ source <(rg --generate complete-zsh)
```

Note though that while this approach is easier to setup, is generally slower
than the previous method, and will add more time to loading your shell prompt.

For **PowerShell**, create the completions:

```
$ rg --generate complete-powershell > _rg.ps1
```

And then add `. _rg.ps1` to your PowerShell
[profile](https://technet.microsoft.com/en-us/library/bb613488(v=vs.85).aspx)
(note the leading period). If the `_rg.ps1` file is not on your `PATH`, do
`. /path/to/_rg.ps1` instead.


<h3 name="order">
How can I get results in a consistent order?
</h3>

By default, ripgrep uses parallelism to execute its search because this makes
the search much faster on most modern systems. This in turn means that ripgrep
has a non-deterministic aspect to it, since the interleaving of threads during
the execution of the program is itself non-deterministic. This has the effect
of printing results in a somewhat arbitrary order, and this order can change
from run to run of ripgrep.

The only way to make the order of results consistent is to ask ripgrep to
sort the output. Currently, this will disable all parallelism. (On smaller
repositories, you might not notice much of a performance difference!) You
can achieve this with the `--sort path` flag.

There is more discussion on this topic here:
https://github.com/BurntSushi/ripgrep/issues/152


<h3 name="encoding">
How do I search files that aren't UTF-8?
</h3>

See the [guide's section on file encoding](GUIDE.md#file-encoding).


<h3 name="compressed">
How do I search compressed files?
</h3>

ripgrep's `-z/--search-zip` flag will cause it to search compressed files
automatically. Currently, this supports gzip, bzip2, xz, lzma, lz4, Brotli and
Zstd. Each of these requires the corresponding `gzip`, `bzip2`, `xz`,
`lz4`, `brotli` and `zstd` binaries to be installed on your system. (That is,
ripgrep does decompression by shelling out to another process.)

ripgrep currently does not search archive formats, so `*.tar.gz` files, for
example, are skipped.


<h3 name="multiline">
How do I search over multiple lines?
</h3>

The `-U/--multiline` flag enables ripgrep to report results that span over
multiple lines.


<h3 name="fancy">
How do I use lookaround and/or backreferences?
</h3>

ripgrep's default regex engine does not support lookaround or backreferences.
This is primarily because the default regex engine is implemented using finite
state machines in order to guarantee a linear worst case time complexity on all
inputs. Backreferences are not possible to implement in this paradigm, and
lookaround appears difficult to do efficiently.

However, ripgrep optionally supports using PCRE2 as the regex engine instead of
the default one based on finite state machines. You can enable PCRE2 with the
`-P/--pcre2` flag. For example, in the root of the ripgrep repo, you can easily
find all palindromes:

```
$ rg -P '(\w{10})\1'
tests/misc.rs
483:    cmd.arg("--max-filesize").arg("44444444444444444444");
globset/src/glob.rs
1206:    matches!(match7, "a*a*a*a*a*a*a*a*a", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa");
```

If your version of ripgrep doesn't support PCRE2, then you'll get an error
message when you try to use the `-P/--pcre2` flag:

```
$ rg -P '(\w{10})\1'
PCRE2 is not available in this build of ripgrep
```

Most of the releases distributed by the ripgrep project here on GitHub will
come bundled with PCRE2 enabled. If you installed ripgrep through a different
means (like your system's package manager), then please reach out to the
maintainer of that package to see whether it's possible to enable the PCRE2
feature.


<h3 name="colors">
How do I configure ripgrep's colors?
</h3>

ripgrep has two flags related to colors:

* `--color` controls *when* to use colors.
* `--colors` controls *which* colors to use.

The `--color` flag accepts one of the following possible values: `never`,
`auto`, `always` or `ansi`. The `auto` value is the default and will cause
ripgrep to only enable colors when it is printing to a terminal. But if you
pipe ripgrep to a file or some other process, then it will suppress colors.

The `--colors` flag is a bit more complicated. The general format is:

```
--colors '{type}:{attribute}:{value}'
```

* `{type}` should be one of `path`, `line`, `column` or `match`. Each of these
  correspond to the four different types of things that ripgrep will add color
  to in its output. Select the type whose color you want to change.
* `{attribute}` should be one of `fg`, `bg` or `style`, corresponding to
  foreground color, background color, or miscellaneous styling (such as whether
  to bold the output or not).
* `{value}` is determined by the value of `{attribute}`. If
  `{attribute}` is `style`, then `{value}` should be one of `nobold`,
  `bold`, `nointense`, `intense`, `nounderline`, `underline`, `noitalic` or
  `italic`. If `{attribute}` is `fg` or `bg`, then `{value}` should be a color.

A color is specified by either one of eight of English names, a single 256-bit
number or an RGB triple (with over 16 million possible values, or "true
color").

The color names are `red`, `blue`, `green`, `cyan`, `magenta`, `yellow`,
`white` or `black`.

A single 256-bit number is a value in the range 0-255 (inclusive). It can
either be in decimal format (e.g., `62`) or hexadecimal format (e.g., `0x3E`).

An RGB triple corresponds to three numbers (decimal or hexadecimal) separated
by commas.

As a special case, `--colors '{type}:none'` will clear all colors and styles
associated with `{type}`, which lets you start with a clean slate (instead of
building on top of ripgrep's default color settings).

Here's an example that highlights the matches with a nice blue background with
bolded white text:

```
$ rg somepattern \
    --colors 'match:none' \
    --colors 'match:bg:0x33,0x66,0xFF' \
    --colors 'match:fg:white' \
    --colors 'match:style:bold'
```

Colors are an ideal candidate to set in your
[configuration file](GUIDE.md#configuration-file). See the
[question on emulating The Silver Searcher's output style](#silver-searcher-output)
for an example specific to colors.


<h3 name="truecolors-windows">
How do I enable true colors on Windows?
</h3>

First, see the previous question's
[answer on configuring colors](#colors).

Secondly, coloring on Windows is a bit complicated. If you're using a terminal
like Cygwin, then it's likely true color support already works out of the box.
However, if you are using a normal Windows console (`cmd` or `PowerShell`) and
a version of Windows prior to 10, then there is no known way to get true
color support. If you are on Windows 10 and using a Windows console, then
true colors should work out of the box with one caveat: you might need to
clear ripgrep's default color settings first. That is, instead of this:

```
$ rg somepattern --colors 'match:fg:0x33,0x66,0xFF'
```

you should do this

```
$ rg somepattern --colors 'match:none' --colors 'match:fg:0x33,0x66,0xFF'
```

This is because ripgrep might set the default style for `match` to `bold`, and
it seems like Windows 10's VT100 support doesn't permit bold and true color
ANSI escapes to be used simultaneously. The work-around above will clear
ripgrep's default styling, allowing you to craft it exactly as desired.


<h3 name="stop-ripgrep">
How do I stop ripgrep from messing up colors when I kill it?
</h3>

Type in `color` in cmd.exe (Command Prompt) and `echo -ne "\033[0m"` on
Unix-like systems to restore your original foreground color.

In PowerShell, you can add the following code to your profile which will
restore the original foreground color when `Reset-ForegroundColor` is called.
Including the `Set-Alias` line will allow you to call it with simply `color`.

```powershell
$OrigFgColor = $Host.UI.RawUI.ForegroundColor
function Reset-ForegroundColor {
	$Host.UI.RawUI.ForegroundColor = $OrigFgColor
}
Set-Alias -Name color -Value Reset-ForegroundColor
```

PR [#187](https://github.com/BurntSushi/ripgrep/pull/187) fixed this, and it
was later deprecated in
[#281](https://github.com/BurntSushi/ripgrep/issues/281). A full explanation is
available
[here](https://github.com/BurntSushi/ripgrep/issues/281#issuecomment-269093893).


<h3 name="because-cygwin">
Why does using a leading `/` on Windows fail?
</h3>

If you're using cygwin on Windows and try to search for a pattern beginning
with a `/`, then it's possible that cygwin is mangling that pattern without
your knowledge. For example, if you tried running `rg /foo` in a cygwin shell
on Windows, then cygwin might mistakenly perform path translation on `/foo`,
which would result in `rg C:/msys64/foo` being searched instead.

You can fix this in one of three ways:

1. Stop using cygwin.
2. Escape the leading slash with an additional slash. e.g., `rg //foo`.
3. Temporarily disable path translation by setting `MSYS_NO_PATHCONV=1`. e.g.,
   `MSYS_NO_PATHCONV=1 rg /foo`.

For more details, see https://github.com/BurntSushi/ripgrep/issues/1277


<h3 name="size-limit">
How do I get around the regex size limit?
</h3>

If you've given ripgrep a particularly large pattern (or a large number of
smaller patterns), then it is possible that it will fail to compile because it
hit a pre-set limit. For example:

```
$ rg '\pL{1000}'
Compiled regex exceeds size limit of 10485760 bytes.
```

(Note: `\pL{1000}` may look small, but `\pL` is the character class containing
all Unicode letters, which is quite large. *And* it's repeated 1000 times.)

In this case, you can work around by simply increasing the limit:

```
$ rg '\pL{1000}' --regex-size-limit 1G
```

Increasing the limit to 1GB does not necessarily mean that ripgrep will use
that much memory. The limit just says that it's allowed to (approximately) use
that much memory for constructing the regular expression.


<h3 name="dfa-size">
How do I make the <code>-f/--file</code> flag faster?
</h3>

The `-f/--file` permits one to give a file to ripgrep which contains a pattern
on each line. ripgrep will then report any line that matches any of the
patterns.

If this pattern file gets too big, then it is possible ripgrep will slow down
dramatically. *Typically* this is because an internal cache is too small, and
will cause ripgrep to spill over to a slower but more robust regular expression
engine. If this is indeed the problem, then it is possible to increase this
cache and regain speed. The cache can be controlled via the `--dfa-size-limit`
flag. For example, using `--dfa-size-limit 1G` will set the cache size to 1GB.
(Note that this doesn't mean ripgrep will use 1GB of memory automatically, but
it will allow the regex engine to if it needs to.)


<h3 name="silver-searcher-output">
How do I make the output look like The Silve
... [TRUNCATED]
```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
