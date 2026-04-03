---
id: github.com-dathere-qsv-docopt-58458c6d-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:43.448257
---

# KNOWLEDGE EXTRACT: github.com_dathere_qsv-docopt_58458c6d
> **Extracted on:** 2026-04-01 12:03:21
> **Source:** D:/LongLeo/AI OS CORP/AI OS/core/security/QUARANTINE/KI-BATCH-20260331205007521690/github.com_dathere_qsv-docopt_58458c6d

---

## File: `.gitignore`
```
.*.swp
doc
tags
target
scratch*
Cargo.lock
```

## File: `COPYING`
```
This project is dual-licensed under the Unlicense and MIT licenses.

You may use this code under the terms of either license.
```

## File: `Cargo.toml`
```
[package]
name = "qsv_docopt"
version = "1.9.0" #:version
authors = [
    "Andrew Gallant <jamslam@gmail.com>",
    "Joel Natividad <joel@datHere.com>",
]
description = "Command line argument parsing."
documentation = "https://docs.rs/qsv_docopt"
homepage = "https://github.com/dathere/qsv-docopt"
repository = "https://github.com/dathere/qsv-docopt"
readme = "README.md"
keywords = ["docopt", "argument", "command", "argv"]
categories = ["command-line-interface"]
license = "Unlicense/MIT"
exclude = ["/Makefile", "/scripts/*"]
edition = "2024"
rust-version = "1.90.0"

[lib]
name = "qsv_docopt"

[[bin]]
name = "docopt-wordlist"
path = "src/wordlist.rs"
doc  = false
test = false

[dependencies]
regex  = "1"
serde  = { version = "1", features = ["derive"] }
strsim = "0.11"
ahash  = "0.8"
```

## File: `LICENSE-MIT`
```
The MIT License (MIT)

Copyright (c) 2015 Andrew Gallant

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
```

## File: `Makefile`
```
all:
	@echo Nothing to do

docs: $(LIB_FILES)
	cargo doc
	# WTF is rustdoc doing?
	in-dir ./target/doc fix-perms
	rscp ./target/doc/* gopher:~/www/burntsushi.net/rustdoc/

src/test/testcases.rs: src/test/testcases.docopt scripts/mk-testcases
	./scripts/mk-testcases ./src/test/testcases.docopt > ./src/test/testcases.rs

ctags:
	ctags --recurse --options=ctags.rust --languages=Rust

push:
	git push github master
	git push origin master
```

## File: `README.md`
```markdown
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

fn main() {
    let args = Docopt::new(USAGE)
                      .and_then(|dopt| dopt.parse())
                      .unwrap_or_else(|e| e.exit());
    println!("{:?}", args);

    // You can conveniently access values with `get_{bool,count,str,vec}`
    // functions. If the key doesn't exist (or if, e.g., you use `get_str` on
    // a switch), then a sensible default value is returned.
    println!("\nSome values:");
    println!("  Speed: {}", args.get_str("--speed"));
    println!("  Drifting? {}", args.get_bool("--drifting"));
    println!("  Names: {:?}", args.get_vec("<name>"));
}
```

## Tab completion support

This particular implementation bundles a command called `docopt-wordlist` that
can be used to automate tab completion. This repository also collects some
basic completion support for various shells (currently only bash) in the
`completions` directory.

You can use them to setup tab completion on your system. It should work with
any program that uses Docopt (or rather, any program that outputs usage
messages that look like Docopt). For example, to get tab completion support for
Cargo, you'll have to install `docopt-wordlist` and add some voodoo to your
`$HOME/.bash_completion` file (this may vary for other shells).

Here it is step by step:

```bash
# Download and build `docopt-wordlist` (as part of the Docopt package)
$ git clone git://github.com/docopt/docopt.rs
$ cd docopt.rs
$ cargo build --release

# Now setup tab completion (for bash)
$ echo "DOCOPT_WORDLIST_BIN=\"$(pwd)/target/release/docopt-wordlist\"" >> $HOME/.bash_completion
$ echo "source \"$(pwd)/completions/docopt-wordlist.bash\"" >> $HOME/.bash_completion
$ echo "complete -F _docopt_wordlist_commands cargo" >> $HOME/.bash_completion
```

My [CSV toolkit](https://github.com/BurntSushi/xsv) is supported too:

```bash
# shameless plug...
$ echo "complete -F _docopt_wordlist_commands xsv" >> $HOME/.bash_completion
```

Note that this is emphatically a first pass. There are several improvements
that I'd like to make:

1. Take context into account when completing. For example, it should be
   possible to only show completions that can lead to a valid Docopt match.
   This may be hard. (i.e., It may require restructuring Docopt's internals.)
2. Support more shells. (I'll happily accept pull requests on this one. I doubt
   I'll venture outside of bash any time soon.)
3. Make tab completion support more seamless. The way it works right now is
   pretty hacky by intermingling file/directory completion.
```

## File: `UNLICENSE`
```
This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.

In jurisdictions that recognize copyright laws, the author or authors
of this software dedicate any and all copyright interest in the
software to the public domain. We make this dedication for the benefit
of the public at large and to the detriment of our heirs and
successors. We intend this dedication to be an overt act of
relinquishment in perpetuity of all present and future rights to this
software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <http://unlicense.org/>
```

## File: `rustfmt.toml`
```
# NOTE: these options require nightly
# cargo +nightly fmt
comment_width                = 100
wrap_comments                = true
format_strings               = true
group_imports                = "StdExternalCrate"
imports_granularity          = "Crate"
enum_discrim_align_threshold = 20
struct_field_align_threshold = 20

```

## File: `completions/docopt-wordlist.bash`
```bash
# This is your basic tab completion that will work well with commands that
# have only one usage (i.e., no distinct sub-commands).
#
# Completion works by simply taking the command name and running `$cmd --help`
# to get the usage (which is then parsed for possible completions).
function _docopt_wordlist {
  if [ -z "$DOCOPT_WORDLIST_BIN" ]; then
    DOCOPT_WORDLIST_BIN=/usr/local/bin/docopt-wordlist
  fi

  cword=$(_get_cword)
  cmd="${COMP_WORDS[0]}"
  wordlist=$("$cmd" --help 2>&1 | "$DOCOPT_WORDLIST_BIN")
  gen "$cword" "$wordlist"
}

# This is a fancier version of the above that supports commands that have
# multiple sub-commands (i.e., distinct usages like Cargo).
#
# This supports sub-command completion only if `$cmd --list` shows a list of
# available sub-commands.
#
# Otherwise, the usage for the command `a b c d` is taken from the first
# command that exits successfully:
#
#   a b c d --help
#   a b c --help
#   a b --help
#   a --help
#
# So for example, if you've typed `cargo test --jo`, then the following
# happens:
#
#   cargo test --jo --help  # error
#   cargo test --help       # gives 'test' sub-command usage!
#
# As a special case, if only the initial command has been typed, then the
# sub-commands (taken from `$cmd --list`) are added to the wordlist.
function _docopt_wordlist_commands {
  if [ -z "$DOCOPT_WORDLIST_BIN" ]; then
    DOCOPT_WORDLIST_BIN=/usr/local/bin/docopt-wordlist
  fi

  cword=$(_get_cword)
  if [ "$COMP_CWORD" = 1 ]; then
    cmd="${COMP_WORDS[0]}"
    wordlist=$("$cmd" --help 2>&1 | "$DOCOPT_WORDLIST_BIN")
    wordlist+=" $("$cmd" --list | egrep '^ +\w' | awk '{print $1}')"
    gen "$cword" "$wordlist"
  else
    for ((i="$COMP_CWORD"; i >= 1; i++)); do
      cmd="${COMP_WORDS[@]::$i}"
      wordlist=$($cmd --help 2>&1 | "$DOCOPT_WORDLIST_BIN")
      if [ $? = 0 ]; then
        gen "$cword" "$wordlist"
        break
      fi
    done
  fi
}

# A helper function for running `compgen`, which is responsible for taking
# a prefix and presenting possible completions.
#
# If the current prefix starts with a `.` or a `/`, then file/directory
# completion is done. Otherwise, Docopt completion is done. If Docopt
# completion is empty, then it falls back to file/directory completion.
function gen {
  cword="$1"
  wordlist="$2"
  if [[ "$cword" = .* || "$cword" = /* ]]; then
    COMPREPLY=($(compgen -A file -- "$cword"))
  else
    COMPREPLY=($(compgen -W "$wordlist" -- "$cword"))
    if [ -z "$COMPREPLY" ]; then
      COMPREPLY=($(compgen -A file -- "$cword"))
    fi
  fi
}
```

## File: `examples/cargo.rs`
```rust
use qsv_docopt::Docopt;
use serde::Deserialize;

// Write the Docopt usage string.
const USAGE: &str = "
Rust's package manager

Usage:
    cargo <command> [<args>...]
    cargo [options]

Options:
    -h, --help       Display this message
    -V, --version    Print version info and exit
    --list           List installed commands
    -v, --verbose    Use verbose output

Some common cargo commands are:
    build       Compile the current project
    clean       Remove the target directory
    doc         Build this project's and its dependencies' documentation
    new         Create a new cargo project
    run         Build and execute src/main.rs
    test        Run the tests
    bench       Run the benchmarks
    update      Update dependencies listed in Cargo.lock

See 'cargo help <command>' for more information on a specific command.
";

#[derive(Debug, Deserialize)]
struct Args {
    arg_command:  Option<Command>,
    arg_args:     Vec<String>,
    flag_list:    bool,
    flag_verbose: bool,
}

#[derive(Debug, Deserialize)]
enum Command {
    Build,
    Clean,
    Doc,
    New,
    Run,
    Test,
    Bench,
    Update,
}

fn main() {
    let args: Args = Docopt::new(USAGE)
        .and_then(|d| d.options_first(true).deserialize())
        .unwrap_or_else(|e| e.exit());
    println!("{:?}", args);
}
```

## File: `examples/cp.rs`
```rust
use qsv_docopt::Docopt;
use serde::Deserialize;

// Write the Docopt usage string.
const USAGE: &str = "
Usage: cp [-a] <source> <dest>
       cp [-a] <source>... <dir>

Options:
    -a, --archive  Copy everything.
";

#[derive(Debug, Deserialize)]
struct Args {
    arg_source:   Vec<String>,
    arg_dest:     String,
    arg_dir:      String,
    flag_archive: bool,
}

fn main() {
    let args: Args = Docopt::new(USAGE)
        .and_then(|d| d.deserialize())
        .unwrap_or_else(|e| e.exit());
    println!("{:?}", args);
}
```

## File: `examples/decode.rs`
```rust
use qsv_docopt::Docopt;
use serde::Deserialize;

const USAGE: &str = "
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
    flag_speed:    isize,
    flag_drifting: bool,
    arg_name:      Vec<String>,
    arg_x:         Option<isize>,
    arg_y:         Option<isize>,
    cmd_ship:      bool,
    cmd_mine:      bool,
}

fn main() {
    let args: Args = Docopt::new(USAGE)
        .and_then(|d| d.deserialize())
        .unwrap_or_else(|e| e.exit());
    println!("{:?}", args);

    println!("\nSome values:");
    println!("  Speed: {}", args.flag_speed);
    println!("  Drifting? {}", args.flag_drifting);
    println!("  Names: {:?}", args.arg_name);
    println!("  Command 'ship' invoked? {:?}", args.cmd_ship);
}
```

## File: `examples/hashmap.rs`
```rust
use qsv_docopt::Docopt;

const USAGE: &str = "
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

fn main() {
    let version = "1.2.3".to_owned();
    let args = Docopt::new(USAGE)
        .and_then(|dopt| dopt.version(Some(version)).parse())
        .unwrap_or_else(|e| e.exit());
    println!("{:?}", args);

    // You can conveniently access values with `get_{bool,count,str,vec}`
    // functions. If the key doesn't exist (or if, e.g., you use `get_str` on
    // a switch), then a sensible default value is returned.
    println!("\nSome values:");
    println!("  Speed: {}", args.get_str("--speed"));
    println!("  Drifting? {}", args.get_bool("--drifting"));
    println!("  Names: {:?}", args.get_vec("<name>"));
    println!("  Command 'ship' invoked? {:?}", args.get_bool("ship"));
}
```

## File: `examples/optional_command.rs`
```rust
// This example shows how to implement a command with a "catch all."
//
// This requires writing your own impl for `Decodable` because docopt's
// decoder uses `Option<T>` to mean "T may not be present" rather than
// "T may be present but incorrect."

use std::fmt;

use qsv_docopt::Docopt;
use serde::{
    Deserialize,
    de::{Deserializer, Error, Visitor},
};

// Write the Docopt usage string.
const USAGE: &str = "
Rust's package manager

Usage:
    mycli [<command>]

Options:
    -h, --help       Display this message
";

#[derive(Debug, Deserialize)]
struct Args {
    arg_command: Command,
}

struct CommandVisitor;

impl<'de> Visitor<'de> for CommandVisitor {
    type Value = Command;

    fn expecting(&self, formatter: &mut fmt::Formatter<'_>) -> fmt::Result {
        formatter.write_str("a string A, B or C")
    }

    fn visit_str<E>(self, s: &str) -> Result<Self::Value, E>
    where
        E: Error,
    {
        Ok(match s {
            "" => Command::None,
            "A" => Command::A,
            "B" => Command::B,
            "C" => Command::C,
            s => Command::Unknown(s.to_string()),
        })
    }
}

impl<'de> Deserialize<'de> for Command {
    fn deserialize<D>(d: D) -> Result<Command, D::Error>
    where
        D: Deserializer<'de>,
    {
        d.deserialize_str(CommandVisitor)
    }
}

#[derive(Debug)]
enum Command {
    A,
    B,
    C,
    Unknown(String),
    None,
}

fn main() {
    let args: Args = Docopt::new(USAGE)
        .and_then(|d| d.deserialize())
        .unwrap_or_else(|e| e.exit());
    println!("{:?}", args);
}
```

## File: `examples/options_from_usage.rs`
```rust
use qsv_docopt::{Docopt, parse::Atom};
use std::io::Read;

// Write the Docopt usage string.
const USAGE: &str = r#"
Rust's package manager

Usage:
    cargo <command> [<args>...]
    cargo [options]

Options:
    -h, --help       Display this message
    -V, --version    Print version info and exit
    --list           List installed commands
    -v, --verbose    Use verbose output

Some common cargo commands are:
    build       Compile the current project
    clean       Remove the target directory
    doc         Build this project's and its dependencies' documentation
    new         Create a new cargo project
    run         Build and execute src/main.rs
    test        Run the tests
    bench       Run the benchmarks
    update      Update dependencies listed in Cargo.lock

See 'cargo help <command>' for more information on a specific command.
"#;

fn main() {
    let args = std::env::args().collect::<Vec<String>>();
    let mut passed_usage = USAGE.to_string();
    if let Some(arg) = args.get(1) {
        if arg == "-" {
            std::io::stdin().read_to_string(&mut passed_usage).unwrap();
            println!("{}", get_options(passed_usage.clone()).join(", "));
            return;
        } else if arg == "qsv" {
            let qsv_list = String::from_utf8(
                std::process::Command::new("qsv")
                    .arg("--list")
                    .output()
                    .unwrap()
                    .stdout,
            )
            .unwrap();
            let mut commands = vec![];
            for line in qsv_list.lines() {
                if line.starts_with("    ") {
                    let command = line.trim_start().split_whitespace().next().unwrap();
                    commands.push(command);
                }
            }
            for command in commands.iter() {
                let command_usage_text = String::from_utf8(
                    std::process::Command::new("qsv")
                        .arg(command)
                        .arg("--help")
                        .output()
                        .unwrap()
                        .stdout,
                )
                .unwrap();
                println!("{command} options:");
                let options = get_options(command_usage_text);
                println!("{}", options.join(", "));
                println!("=====================");
            }
        }
    }
    println!("{}", get_options(passed_usage).join(", "));
}

fn get_options(usage: String) -> Vec<String> {
    let docopt = Docopt::new(usage).unwrap();
    let parser = docopt.parser();
    let descs = parser.descs.clone();
    let descs: Vec<String> = descs
        .keys()
        .filter(|l| match l {
            Atom::Short(_) => true,
            Atom::Long(l) => {
                if l.starts_with("---") {
                    false
                } else {
                    true
                }
            }
            _ => false,
        })
        .map(|k| k.to_string())
        .collect();
    descs
}
```

## File: `examples/verbose_multiple.rs`
```rust
use qsv_docopt::Docopt;
use serde::Deserialize;

// This shows how to implement multiple levels of verbosity.
//
// When you have multiple patterns, I think the only way to carry the
// repeated flag through all of them is to specify it for each pattern
// explicitly.
//
// This is unfortunate.
const USAGE: &str = "
Usage: cp [options] [-v | -vv | -vvv] <source> <dest>
       cp [options] [-v | -vv | -vvv] <source>... <dir>

Options:
    -a, --archive  Copy everything.
    -v, --verbose  Show extra log output.
";

#[derive(Debug, Deserialize)]
struct Args {
    arg_source:   Vec<String>,
    arg_dest:     String,
    arg_dir:      String,
    flag_archive: bool,
    flag_verbose: usize,
}

fn main() {
    let args: Args = Docopt::new(USAGE)
        .and_then(|d| d.deserialize())
        .unwrap_or_else(|e| e.exit());
    println!("{:?}", args);
}
```

## File: `scripts/mk-testcases`
```
#!/usr/bin/env python2

from __future__ import absolute_import, division, print_function
import argparse
import json
import re

retests = re.compile('(.*?)"""(.*?)(r"""|\s*$)', re.DOTALL)
reinvokes = re.compile('(.+?$)(.+?)\s*(\$|\Z)', re.DOTALL | re.MULTILINE)

p = argparse.ArgumentParser(
    description="Outputs src/test/testcases.rs to stdout")
p.add_argument("testcases", metavar="FILE",
               help="The testcases.docopt language agnostic test suite.")
args = p.parse_args()

with open(args.testcases) as f:
    alltests = f.read()

alltests = re.sub('^r"""', '', alltests)
alltests = re.sub('^\s*#.*$', '', alltests, flags=re.MULTILINE)

tests = []  # [{usage, args, expect}]   (expect is None ==> user-error)
for m in retests.finditer(alltests):
    usage, invokes = m.group(1).strip(), m.group(2).strip()
    assert invokes.startswith('$'), 'Bad test: "%s"' % invokes
    invokes = re.sub('^\$', '', invokes)

    for mi in reinvokes.finditer(invokes):
        invoke, expect = mi.group(1).strip(), mi.group(2).strip()
        err = expect.startswith('"user-error"')
        tests.append({
            'usage': usage,
            'args': invoke.split()[1:],
            'expect': None if err else json.loads(expect),
        })


def show_test(i, t):
    def show_expect(e):
        kvs = []
        for k, v in e.iteritems():
            kvs.append('("%s", %s)' % (k, show_value(v)))
        return ', '.join(kvs)
    def show_value(v):
        if v is None:
            return 'Plain(None)'
        elif isinstance(v, basestring):
            return 'Plain(Some("%s".to_string()))' % v
        elif isinstance(v, bool):
            return 'Switch(%s)' % ('true' if v else 'false')
        elif isinstance(v, int):
            return 'Counted(%d)' % v
        elif isinstance(v, list):
            elms = ', '.join(['"%s".to_string()' % el for el in v])
            return 'List(vec!(%s))' % elms
        else:
            raise ValueError('Unrecognized value: "%s" (type: %s)'
                             % (v, type(v)))

    args = ', '.join(['"%s"' % arg for arg in t['args']])
    if t['expect'] is None:
        return 'test_user_error!(test_%d_testcases, "%s", &[%s]);' \
                % (i, t['usage'], args)
    else:
        expect = show_expect(t['expect'])
        return 'test_expect!(test_%d_testcases, "%s", &[%s], vec!(%s));' \
                % (i, t['usage'], args, expect)

print(
"""// !!! ATTENTION !!!
// This file is automatically generated by `scripts/mk-testcases`.
// Please do not edit this file directly!

use Value::{{Switch, Counted, Plain, List}};
use test::{{get_args, map_from_alist, same_args}};

{tests}
""".format(tests='\n\n'.join([show_test(i, t) for i, t in enumerate(tests)])))

```

## File: `src/dopt.rs`
```rust
use std::{
    error::Error as StdError,
    fmt::{self, Debug},
    io::{self, Write},
    result,
    str::FromStr,
};

use ahash::AHashMap;
use regex::Captures;
use serde::{de, de::IntoDeserializer};

use self::{
    Error::{Argv, Deserialize, Help, NoMatch, Usage, Version, WithProgramUsage},
    Value::{Counted, List, Plain, Switch},
};
use crate::{cap_or_empty, parse::Parser, synonym::SynonymMap};

/// Represents the different types of Docopt errors.
///
/// This error type has a lot of variants. In the common case, you probably
/// don't care why Docopt has failed, and would rather just quit the program
/// and show an error message instead. The `exit` method defined on the `Error`
/// type will do just that. It will also set the exit code appropriately
/// (no error for `--help` or `--version`, but an error code for bad usage,
/// bad argv, no match or bad decode).
///
/// ### Example
///
/// Generally, you want to parse the usage string, try to match the argv
/// and then quit the program if there was an error reported at any point
/// in that process. This can be achieved like so:
///
/// ```no_run
/// use qsv_docopt::Docopt;
///
/// const USAGE: &'static str = "
/// Usage: ...
/// ";
///
/// let args = Docopt::new(USAGE)
///                   .and_then(|d| d.parse())
///                   .unwrap_or_else(|e| e.exit());
/// ```
#[derive(Debug)]
pub enum Error {
    /// Parsing the usage string failed.
    ///
    /// This error can only be triggered by the programmer, i.e., the writer
    /// of the Docopt usage string. This error is usually indicative of a bug
    /// in your program.
    Usage(String),

    /// Parsing the argv specified failed.
    ///
    /// The payload is a string describing why the arguments provided could not
    /// be parsed.
    ///
    /// This is distinct from `NoMatch` because it will catch errors like
    /// using flags that aren't defined in the usage string.
    Argv(String),

    /// The given argv parsed successfully, but it did not match any example
    /// usage of the program.
    ///
    /// Regrettably, there is no descriptive message describing *why* the
    /// given argv didn't match any of the usage strings.
    NoMatch,

    /// This indicates a problem deserializing a successful argv match into a
    /// deserializable value.
    Deserialize(String),

    /// Parsing failed, and the program usage should be printed next to the
    /// failure message. Typically this wraps `Argv` and `NoMatch` errors.
    WithProgramUsage(Box<Error>, String),

    /// Decoding or parsing failed because the command line specified that the
    /// help message should be printed.
    Help,

    /// Decoding or parsing failed because the command line specified that the
    /// version should be printed
    ///
    /// The version is included as a payload to this variant.
    Version(String),
}

impl Error {
    /// Return whether this was a fatal error or not.
    ///
    /// Non-fatal errors include requests to print the help or version
    /// information of a program, while fatal errors include those such as
    /// failing to decode or parse.
    #[must_use]
    pub fn fatal(&self) -> bool {
        match *self {
            Help | Version(..) => false,
            Usage(..) | Argv(..) | NoMatch | Deserialize(..) => true,
            WithProgramUsage(ref b, _) => b.fatal(),
        }
    }

    /// Print this error and immediately exit the program.
    ///
    /// If the error is non-fatal (e.g., `Help` or `Version`), then the
    /// error is printed to stdout and the exit status will be `0`. Otherwise,
    /// when the error is fatal, the error is printed to stderr and the
    /// exit status will be `1`.
    pub fn exit(&self) -> ! {
        if self.fatal() {
            werr!("{}\n", self);
            ::std::process::exit(1)
        } else {
            let _ = writeln!(&mut io::stdout(), "{self}");
            ::std::process::exit(0)
        }
    }
}

type Result<T> = result::Result<T, Error>;

impl fmt::Display for Error {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        match *self {
            WithProgramUsage(ref other, ref usage) => {
                let other = other.to_string();
                if other.is_empty() {
                    write!(f, "{usage}")
                } else {
                    write!(f, "{other}\n\n{usage}")
                }
            }
            Help => write!(f, ""),
            NoMatch => write!(f, "Invalid arguments."),
            Usage(ref s) | Argv(ref s) | Deserialize(ref s) | Version(ref s) => write!(f, "{s}"),
        }
    }
}

impl StdError for Error {
    fn source(&self) -> Option<&(dyn StdError + 'static)> {
        match *self {
            WithProgramUsage(ref cause, _) => Some(&**cause),
            _ => None,
        }
    }
}

impl de::Error for Error {
    fn custom<T: fmt::Display>(msg: T) -> Self {
        Error::Deserialize(msg.to_string())
    }
}

/// The main Docopt type, which is constructed with a Docopt usage string.
///
/// This can be used to match command line arguments to produce a `ArgvMap`.
#[derive(Clone, Debug)]
pub struct Docopt {
    p:             Parser,
    argv:          Option<Vec<String>>,
    options_first: bool,
    help:          bool,
    version:       Option<String>,
}

impl Docopt {
    /// Parse the Docopt usage string given.
    ///
    /// The `Docopt` value returned may be used immediately to parse command
    /// line arguments with a default configuration.
    ///
    /// If there was a problem parsing the usage string, a `Usage` error
    /// is returned.
    pub fn new<S>(usage: S) -> Result<Docopt>
    where
        S: ::std::ops::Deref<Target = str>,
    {
        Parser::new(&usage).map_err(Usage).map(|p| Docopt {
            p,
            argv: None,
            options_first: false,
            help: true,
            version: None,
        })
    }

    /// Parse and deserialize the given argv.
    ///
    /// This is a convenience method for
    /// `parse().and_then(|vals| vals.deserialize())`.
    ///
    /// For details on how decoding works, please see the documentation for
    /// `ArgvMap`.
    pub fn deserialize<'a, 'de: 'a, D>(&'a self) -> Result<D>
    where
        D: de::Deserialize<'de>,
    {
        self.parse().and_then(ArgvMap::deserialize)
    }

    /// Parse command line arguments and try to match them against a usage
    /// pattern specified in the Docopt string.
    ///
    /// If there is a match, then an `ArgvMap` is returned, which maps
    /// flags, commands and arguments to values.
    ///
    /// If parsing the command line arguments fails, then an `Argv` error is
    /// returned. If parsing succeeds but there is no match, then a `NoMatch`
    /// error is returned. Both of these errors are always returned inside a
    /// `WithProgramUsage` error.
    ///
    /// If special handling of `help` or `version` is enabled (the former is
    /// enabled by default), then `Help` or `Version` errors are returned
    /// if `--help` or `--version` is present.
    pub fn parse(&self) -> Result<ArgvMap> {
        let argv = self.argv.clone().unwrap_or_else(Docopt::get_argv);
        let vals = self
            .p
            .parse_argv(&argv, self.options_first)
            .map_err(|s| self.err_with_usage(Argv(s)))
            .and_then(|argv| match self.p.matches(&argv) {
                Some(m) => Ok(ArgvMap { map: m }),
                None => Err(self.err_with_usage(NoMatch)),
            })?;
        if self.help && vals.get_bool("--help") {
            return Err(self.err_with_full_doc(Help));
        }
        match self.version {
            Some(ref v) if vals.get_bool("--version") => return Err(Version(v.clone())),
            _ => {}
        }
        Ok(vals)
    }

    /// Set the argv to be used for Docopt parsing.
    ///
    /// By default, when no argv is set, and it is automatically taken from
    /// `std::env::args()`.
    ///
    /// The `argv` given *must* be the full set of `argv` passed to the
    /// program. e.g., `["cp", "src", "dest"]` is right while `["src", "dest"]`
    /// is wrong.
    pub fn argv<I, S>(mut self, argv: I) -> Docopt
    where
        I: IntoIterator<Item = S>,
        S: AsRef<str>,
    {
        self.argv = Some(
            argv.into_iter()
                .skip(1)
                .map(|s| s.as_ref().to_owned())
                .collect(),
        );
        self
    }

    /// Enables the "options first" Docopt behavior.
    ///
    /// The options first behavior means that all flags *must* appear before
    /// position arguments. That is, after the first position argument is
    /// seen, all proceeding arguments are interpreted as positional
    /// arguments unconditionally.
    #[must_use]
    pub const fn options_first(mut self, yes: bool) -> Docopt {
        self.options_first = yes;
        self
    }

    /// Enables automatic handling of `--help`.
    ///
    /// When this is enabled and `--help` appears anywhere in the arguments,
    /// then a `Help` error will be returned. You may then use the `exit`
    /// method on the error value to conveniently quit the program (which will
    /// print the full usage string to stdout).
    ///
    /// Note that for this to work, `--help` must be a valid pattern.
    ///
    /// When disabled, there is no special handling of `--help`.
    #[must_use]
    pub const fn help(mut self, yes: bool) -> Docopt {
        self.help = yes;
        self
    }

    /// Enables automatic handling of `--version`.
    ///
    /// When this is enabled and `--version` appears anywhere in the arguments,
    /// then a `Version(s)` error will be returned, where `s` is the string
    /// given here. You may then use the `exit` method on the error value to
    /// convenient quit the program (which will print the version to stdout).
    ///
    /// When disabled (a `None` value), there is no special handling of
    /// `--version`.
    #[must_use]
    pub fn version(mut self, version: Option<String>) -> Docopt {
        self.version = version;
        self
    }

    #[doc(hidden)]
    #[must_use]
    pub const fn parser(&self) -> &Parser {
        &self.p
    }

    fn err_with_usage(&self, e: Error) -> Error {
        WithProgramUsage(Box::new(e), self.p.usage.trim().into())
    }

    fn err_with_full_doc(&self, e: Error) -> Error {
        WithProgramUsage(Box::new(e), self.p.full_doc.trim().into())
    }

    fn get_argv() -> Vec<String> {
        // Use args_os() to avoid panicking on non-UTF-8 arguments.
        // Non-UTF-8 sequences are converted to the Unicode replacement character.
        ::std::env::args_os()
            .skip(1)
            .map(|s| s.to_string_lossy().into_owned())
            .collect()
    }
}

/// A map containing matched values from command line arguments.
///
/// The keys are just as specified in Docopt: `--flag` for a long flag or
/// `-f` for a short flag. (If `-f` is a synonym for `--flag`, then either
/// key will work.) `ARG` or `<arg>` specify a positional argument and `cmd`
/// specifies a command.
#[derive(Clone)]
pub struct ArgvMap {
    #[doc(hidden)]
    pub map: SynonymMap<String, Value>,
}

impl ArgvMap {
    /// Tries to deserialize the map of values into a struct.
    ///
    /// This method should always be called to deserialize a `ArgvMap` into
    /// a struct. All fields of the struct must map to a corresponding key
    /// in the `ArgvMap`. To this end, each member must have a special prefix
    /// corresponding to the different kinds of patterns in Docopt. There are
    /// three prefixes: `flag_`, `arg_` and `cmd_` which respectively
    /// correspond to short/long flags, positional arguments and commands.
    ///
    /// If a Docopt item has a `-` in its name, then it is converted to an `_`.
    ///
    /// # Example
    ///
    /// ```rust
    /// # fn main() {
    /// use serde::Deserialize;
    ///
    /// use qsv_docopt::Docopt;
    ///
    /// const USAGE: &'static str = "
    /// Usage: cargo [options] (build | test)
    ///        cargo --help
    ///
    /// Options: -v, --verbose
    ///          -h, --help
    /// ";
    ///
    /// #[derive(Deserialize)]
    /// struct Args {
    ///   cmd_build: bool,
    ///   cmd_test: bool,
    ///   flag_verbose: bool,
    ///   flag_h: bool,
    /// }
    ///
    /// let argv = || vec!["cargo", "build", "-v"].into_iter();
    /// let args: Args = Docopt::new(USAGE)
    ///     .and_then(|d| d.argv(argv()).deserialize())
    ///     .unwrap_or_else(|e| e.exit());
    /// assert!(args.cmd_build && !args.cmd_test
    ///         && args.flag_verbose && !args.flag_h);
    /// # }
    /// ```
    ///
    /// Note that in the above example, `flag_h` is used but `flag_help`
    /// could also be used. (In fact, both could be used at the same time.)
    ///
    /// In this example, only the `bool` type was used, but any type satisfying
    /// the `Deserialize` trait is valid.
    pub fn deserialize<'de, T: de::Deserialize<'de>>(self) -> Result<T> {
        de::Deserialize::deserialize(&mut Deserializer {
            vals:  self,
            stack: vec![],
        })
    }

    /// Finds the value corresponding to `key` and calls `as_bool()` on it.
    /// If the key does not exist, `false` is returned.
    pub fn get_bool(&self, key: &str) -> bool {
        self.find(key).is_some_and(Value::as_bool)
    }

    /// Finds the value corresponding to `key` and calls `as_count()` on it.
    /// If the key does not exist, `0` is returned.
    pub fn get_count(&self, key: &str) -> u64 {
        self.find(key).map_or(0, Value::as_count)
    }

    /// Finds the value corresponding to `key` and calls `as_str()` on it.
    /// If the key does not exist, `""` is returned.
    pub fn get_str(&self, key: &str) -> &str {
        self.find(key).map_or("", Value::as_str)
    }

    /// Finds the value corresponding to `key` and calls `as_vec()` on it.
    /// If the key does not exist, `vec!()` is returned.
    pub fn get_vec(&self, key: &str) -> Vec<&str> {
        self.find(key).map(Value::as_vec).unwrap_or_default()
    }

    /// Return the raw value corresponding to some `key`.
    ///
    /// `key` should be a string in the traditional Docopt format. e.g.,
    /// `<arg>` or `--flag`.
    #[must_use]
    pub fn find(&self, key: &str) -> Option<&Value> {
        self.map.find(&key.into())
    }

    /// Return the number of values, not including synonyms.
    #[must_use]
    pub fn len(&self) -> usize {
        self.map.len()
    }

    /// Converts a Docopt key to a struct field name.
    /// This makes a half-hearted attempt at making the key a valid struct
    /// field name (like replacing `-` with `_`), but it does not otherwise
    /// guarantee that the result is a valid struct field name.
    #[doc(hidden)]
    pub fn key_to_struct_field(name: &str) -> String {
        decl_regex! {
            RE :
                r"^(?:--?(?P<flag>\S+)|(?:(?P<argu>\p{Lu}+)|<(?P<argb>[^>]+)>)|(?P<cmd>\S+))$"
            ;
        }
        fn sanitize(name: &str) -> String {
            name.replace('-', "_")
        }

        RE.replace(name, |cap: &Captures<'_>| {
            let (flag, cmd) = (cap_or_empty(cap, "flag"), cap_or_empty(cap, "cmd"));
            let (argu, argb) = (cap_or_empty(cap, "argu"), cap_or_empty(cap, "argb"));
            let (prefix, name) = if !flag.is_empty() {
                ("flag_", flag)
            } else if !argu.is_empty() {
                ("arg_", argu)
            } else if !argb.is_empty() {
                ("arg_", argb)
            } else if !cmd.is_empty() {
                ("cmd_", cmd)
            } else {
                panic!("Unknown ArgvMap key: '{name}'")
            };
            let mut prefix = prefix.to_owned();
            prefix.push_str(&sanitize(name));
            prefix
        })
        .into_owned()
    }

    /// Converts a struct field name to a Docopt key.
    #[doc(hidden)]
    pub fn struct_field_to_key(field: &str) -> String {
        decl_regex! {
            FLAG: r"^flag_";
            ARG: r"^arg_";
            LETTERS: r"^\p{Lu}+$";
            CMD: r"^cmd_";
        }
        fn desanitize(name: &str) -> String {
            name.replace('_', "-")
        }
        let name = if field.starts_with("flag_") {
            let name = FLAG.replace(field, "");
            let mut pre_name = (if name.len() == 1 { "-" } else { "--" }).to_owned();
            pre_name.push_str(&name);
            pre_name
        } else if field.starts_with("arg_") {
            let name = ARG.replace(field, "").into_owned();
            if LETTERS.is_match(&name) {
                name
            } else {
                let mut pre_name = "<".to_owned();
                pre_name.push_str(&name);
                pre_name.push('>');
                pre_name
            }
        } else if field.starts_with("cmd_") {
            CMD.replace(field, "").into_owned()
        } else {
            panic!("Unrecognized struct field: '{field}'")
        };
        desanitize(&name)
    }
}

impl fmt::Debug for ArgvMap {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        if self.len() == 0 {
            return write!(f, "{{EMPTY}}");
        }

        // This is a little crazy, but we want to group synonyms with
        // their keys and sort them for predictable output.
        let reverse: AHashMap<&String, &String> =
            self.map.synonyms().map(|(from, to)| (to, from)).collect();
        let mut keys: Vec<&String> = self.map.keys().collect();
        keys.sort();
        let mut first = true;
        for &k in &keys {
            if first {
                first = false;
            } else {
                writeln!(f)?;
            }
            match reverse.get(&k) {
                None => write!(f, "{k} => {:?}", self.map.get(k))?,
                Some(s) => write!(f, "{s}, {k} => {:?}", self.map.get(k))?,
            }
        }
        Ok(())
    }
}

/// A matched command line value.
///
/// The value can be a boolean, counted repetition, a plain string or a list
/// of strings.
///
/// The various `as_{bool,count,str,vec}` methods provide convenient access
/// to values without destructuring manually.
#[derive(Clone, Debug, PartialEq)]
pub enum Value {
    /// A boolean value from a flag that has no argument.
    ///
    /// The presence of a flag means `true` and the absence of a flag
    /// means `false`.
    Switch(bool),

    /// The number of occurrences of a repeated flag.
    Counted(u64),

    /// A positional or flag argument.
    ///
    /// This is `None` when the positional argument or flag is not present.
    /// Note that it is possible to have `Some("")` for a present but empty
    /// argument.
    Plain(Option<String>),

    /// A List of positional or flag arguments.
    ///
    /// This list may be empty when no arguments or flags are present.
    List(Vec<String>),
}

impl Value {
    /// Returns the value as a bool.
    ///
    /// Counted repetitions are `false` if `0` and `true` otherwise.
    /// Plain strings are `true` if present and `false` otherwise.
    /// Lists are `true` if non-empty and `false` otherwise.
    #[must_use]
    pub fn as_bool(&self) -> bool {
        match *self {
            Switch(b) => b,
            Counted(n) => n > 0,
            Plain(None) => false,
            Plain(Some(_)) => true,
            List(ref vs) => !vs.is_empty(),
        }
    }

    /// Returns the value as a count of the number of times it occurred.
    ///
    /// Booleans are `1` if `true` and `0` otherwise.
    /// Plain strings are `1` if present and `0` otherwise.
    /// Lists correspond to its length.
    #[must_use]
    pub fn as_count(&self) -> u64 {
        match *self {
            Switch(b) => u64::from(b), // if b { 1 } else { 0 },
            Counted(n) => n,
            Plain(None) => 0,
            Plain(Some(_)) => 1,
            List(ref vs) => vs.len() as u64,
        }
    }

    /// Returns the value as a string.
    ///
    /// All values return an empty string except for a non-empty plain string.
    #[must_use]
    pub fn as_str(&self) -> &str {
        match *self {
            Switch(_) | Counted(_) | Plain(None) | List(_) => "",
            Plain(Some(ref s)) => s,
        }
    }

    /// Returns the value as a list of strings.
    ///
    /// Booleans, repetitions and empty strings correspond to an empty list.
    /// Plain strings correspond to a list of length `1`.
    #[must_use]
    pub fn as_vec(&self) -> Vec<&str> {
        match *self {
            Switch(_) | Counted(_) | Plain(None) => vec![],
            Plain(Some(ref s)) => vec![&**s],
            List(ref vs) => vs.iter().map(|s| &**s).collect(),
        }
    }
}

/// Deserializer for `ArgvMap` into your own `Deserialize`able types.
///
/// In general, you shouldn't have to use this type directly. It is exposed
/// in case you want to write a generic function that produces a deserializable
/// value. For example, here's a function that takes a usage string, an argv
/// and produces a deserializable value:
///
/// ```rust
/// # extern crate qsv_docopt;
/// extern crate serde;
/// # fn main() {
/// use qsv_docopt::Docopt;
/// use serde::de::Deserialize;
///
/// fn deserialize<'de, D: Deserialize<'de>>(usage: &str, argv: &[&str])
///                         -> Result<D, qsv_docopt::Error> {
///     Docopt::new(usage)
///            .and_then(|d| d.argv(argv.iter()).deserialize())
/// }
/// # }
pub struct Deserializer<'de> {
    vals:  ArgvMap,
    stack: Vec<DeserializerItem<'de>>,
}

#[derive(Debug)]
struct DeserializerItem<'de> {
    key:          String,
    struct_field: &'de str,
    val:          Option<Value>,
}

macro_rules! derr(
    ($($arg:tt)*) => (return Err(Deserialize(format!($($arg)*))))
);

impl<'de> Deserializer<'de> {
    #[inline]
    fn push(&mut self, struct_field: &'de str) {
        let key = ArgvMap::struct_field_to_key(struct_field);
        self.stack.push(DeserializerItem {
            key: key.clone(),
            struct_field,
            val: self.vals.find(&key).cloned(),
        });
    }

    #[inline]
    fn pop(&mut self) -> Result<DeserializerItem<'_>> {
        match self.stack.pop() {
            None => derr!("Could not deserialize value into unknown key."),
            Some(it) => Ok(it),
        }
    }

    #[inline]
    fn pop_key_val(&mut self) -> Result<(String, Value)> {
        let it = self.pop()?;
        match it.val {
            None => {
                derr!(
                    "Could not find argument '{}' (from struct field '{}').
Note that each struct field must have the right key prefix, which must
be one of `cmd_`, `flag_` or `arg_`.",
                    it.key,
                    it.struct_field
                )
            }
            Some(v) => Ok((it.key, v)),
        }
    }

    #[inline]
    fn pop_val(&mut self) -> Result<Value> {
        let (_, v) = self.pop_key_val()?;
        Ok(v)
    }

    fn to_number<T>(&mut self, expect: &str) -> Result<T>
    where
        T: FromStr + ToString,
        <T as FromStr>::Err: Debug,
    {
        let (k, v) = self.pop_key_val()?;
        if let Counted(n) = v {
            Ok(n.to_string().parse().unwrap())
        } else {
            let vstr = v.as_str();
            if vstr.trim().is_empty() {
                Ok("0".parse().unwrap()) // lol
            } else {
                match vstr.parse() {
                    Err(_) => {
                        derr!("Could not deserialize '{vstr}' to {expect} for '{k}'.")
                    }
                    Ok(v) => Ok(v),
                }
            }
        }
    }

    fn to_float(&mut self, expect: &str) -> Result<f64> {
        let (k, v) = self.pop_key_val()?;
        if let Counted(n) = v {
            Ok(n as f64)
        } else {
            let vstr = v.as_str();
            match vstr.parse() {
                Err(_) => {
                    derr!("Could not deserialize '{vstr}' to {expect} for '{k}'.")
                }
                Ok(v) => Ok(v),
            }
        }
    }
}

macro_rules! deserialize_num {
    ($name:ident, $method:ident, $ty:ty) => {
        fn $name<V>(self, visitor: V) -> Result<V::Value>
        where
            V: de::Visitor<'de>,
        {
            visitor.$method(self.to_number::<$ty>(stringify!($ty)).map(|n| n as $ty)?)
        }
    };
}

impl<'de> ::serde::Deserializer<'de> for &mut Deserializer<'de> {
    type Error = Error;

    fn deserialize_any<V>(self, _visitor: V) -> Result<V::Value>
    where
        V: de::Visitor<'de>,
    {
        unimplemented!()
    }

    fn deserialize_bool<V>(self, visitor: V) -> Result<V::Value>
    where
        V: de::Visitor<'de>,
    {
        visitor.visit_bool(self.pop_val().map(|v| v.as_bool())?)
    }

    // wish for stable macro concat_idents!
    deserialize_num!(deserialize_i8, visit_i8, i8);
    deserialize_num!(deserialize_i16, visit_i16, i16);
    deserialize_num!(deserialize_i32, visit_i32, i32);
    deserialize_num!(deserialize_i64, visit_i64, i64);
    deserialize_num!(deserialize_u8, visit_u8, u8);
    deserialize_num!(deserialize_u16, visit_u16, u16);
    deserialize_num!(deserialize_u32, visit_u32, u32);
    deserialize_num!(deserialize_u64, visit_u64, u64);

    fn deserialize_f32<V>(self, visitor: V) -> Result<V::Value>
    where
        V: de::Visitor<'de>,
    {
        visitor.visit_f32(self.to_float("f32").map(|n| n as f32)?)
    }

    fn deserialize_f64<V>(self, visitor: V) -> Result<V::Value>
    where
        V: de::Visitor<'de>,
    {
        visitor.visit_f64(self.to_float("f64")?)
    }

    fn deserialize_char<V>(self, visitor: V) -> Result<V::Value>
    where
        V: de::Visitor<'de>,
    {
        let (k, v) = self.pop_key_val()?;
        let vstr = v.as_str();
        match vstr.chars().count() {
            1 => visitor.visit_char(vstr.chars().next().unwrap()),
            _ => derr!("Could not deserialize '{vstr}' into char for '{k}'."),
        }
    }

    fn deserialize_str<V>(self, visitor: V) -> Result<V::Value>
    where
        V: de::Visitor<'de>,
    {
        let s = self.pop_val()?;
        visitor.visit_str(s.as_str())
    }

    fn deserialize_string<V>(self, visitor: V) -> Result<V::Value>
    where
        V: de::Visitor<'de>,
    {
        self.deserialize_str(visitor)
    }

    fn deserialize_bytes<V>(self, _visitor: V) -> Result<V::Value>
    where
        V: de::Visitor<'de>,
    {
        unimplemented!()
    }

    fn deserialize_byte_buf<V>(self, _visitor: V) -> Result<V::Value>
    where
        V: de::Visitor<'de>,
    {
        unimplemented!()
    }

    fn deserialize_option<V>(self, visitor: V) -> Result<V::Value>
    where
        V: de::Visitor<'de>,
    {
        let is_some = match self.stack.last() {
            None => derr!("Could not deserialize value into unknown key."),
            Some(it) => it.val.as_ref().is_some_and(Value::as_bool),
        };
        if is_some {
            visitor.visit_some(self)
        } else {
            visitor.visit_none()
        }
    }

    fn deserialize_unit<V>(self, _visitor: V) -> Result<V::Value>
    where
        V: de::Visitor<'de>,
    {
        // I don't know what the right thing is here, so just fail for now.
        panic!("I don't know how to read into a nil value.")
    }

    fn deserialize_unit_struct<V>(self, _name: &'static str, visitor: V) -> Result<V::Value>
    where
        V: de::Visitor<'de>,
    {
        visitor.visit_unit()
    }

    fn deserialize_newtype_struct<V>(self, _name: &'static str, visitor: V) -> Result<V::Value>
    where
        V: de::Visitor<'de>,
    {
        visitor.visit_newtype_struct(self)
    }

    fn deserialize_tuple<V>(self, _len: usize, _visitor: V) -> Result<V::Value>
    where
        V: de::Visitor<'de>,
    {
        unimplemented!()
    }

    fn deserialize_tuple_struct<V>(
        self,
        _name: &'static str,
        _len: usize,
        _visitor: V,
    ) -> Result<V::Value>
    where
        V: de::Visitor<'de>,
    {
        unimplemented!()
    }

    fn deserialize_map<V>(self, _visitor: V) -> Result<V::Value>
    where
        V: de::Visitor<'de>,
    {
        unimplemented!()
    }

    fn deserialize_seq<V>(self, visitor: V) -> Result<V::Value>
    where
        V: de::Visitor<'de>,
    {
        let (key, struct_field, val) = match self.stack.pop() {
            None => derr!("Could not deserialize value into unknown key."),
            Some(DeserializerItem {
                key,
                struct_field,
                val,
            }) => (key, struct_field, val),
        };
        let list = val.unwrap_or(List(vec![]));
        let vals = list.as_vec();
        for val in vals.iter().rev() {
            self.stack.push(DeserializerItem {
                key: key.clone(),
                struct_field,
                val: Some(Plain(Some((*val).into()))),
            });
        }
        visitor.visit_seq(SeqDeserializer::new(self, vals.len()))
    }

    fn deserialize_struct<V>(
        self,
        _: &str,
        fields: &'static [&'static str],
        visitor: V,
    ) -> Result<V::Value>
    where
        V: de::Visitor<'de>,
    {
        visitor.visit_seq(StructDeserializer::new(self, fields))
    }

    fn deserialize_enum<V>(self, _name: &str, variants: &[&str], visitor: V) -> Result<V::Value>
    where
        V: de::Visitor<'de>,
    {
        let v = self.pop_val()?.as_str().to_lowercase();
        let Some(s) = variants.iter().find(|&n| n.to_lowercase() == v) else {
            derr!("Could not match '{v}' with any of the allowed variants: {variants:?}")
        };
        visitor.visit_enum(s.into_deserializer())
    }

    fn deserialize_identifier<V>(self, visitor: V) -> Result<V::Value>
    where
        V: de::Visitor<'de>,
    {
        self.deserialize_str(visitor)
    }

    fn deserialize_ignored_any<V>(self, visitor: V) -> Result<V::Value>
    where
        V: de::Visitor<'de>,
    {
        self.deserialize_any(visitor)
    }
}

struct SeqDeserializer<'a, 'de: 'a> {
    de:  &'a mut Deserializer<'de>,
    len: usize,
}

impl<'a, 'de> SeqDeserializer<'a, 'de> {
    fn new(de: &'a mut Deserializer<'de>, len: usize) -> Self {
        SeqDeserializer { de, len }
    }
}

impl<'de> de::SeqAccess<'de> for SeqDeserializer<'_, 'de> {
    type Error = Error;

    fn next_element_seed<T>(&mut self, seed: T) -> Result<Option<T::Value>>
    where
        T: de::DeserializeSeed<'de>,
    {
        if self.len == 0 {
            return Ok(None);
        }
        self.len -= 1;
        seed.deserialize(&mut *self.de).map(Some)
    }

    fn size_hint(&self) -> Option<usize> {
        Some(self.len)
    }
}

struct StructDeserializer<'a, 'de: 'a> {
    de:     &'a mut Deserializer<'de>,
    fields: &'static [&'static str],
}

impl<'a, 'de> StructDeserializer<'a, 'de> {
    fn new(de: &'a mut Deserializer<'de>, fields: &'static [&'static str]) -> Self {
        StructDeserializer { de, fields }
    }
}

impl<'de> de::SeqAccess<'de> for StructDeserializer<'_, 'de> {
    type Error = Error;

    fn next_element_seed<T>(&mut self, seed: T) -> Result<Option<T::Value>>
    where
        T: de::DeserializeSeed<'de>,
    {
        if self.fields.is_empty() {
            return Ok(None);
        }
        self.de.push(self.fields[0]);
        self.fields = &self.fields[1..];
        seed.deserialize(&mut *self.de).map(Some)
    }

    fn size_hint(&self) -> Option<usize> {
        Some(self.fields.len())
    }
}
```

## File: `src/lib.rs`
```rust
//! Docopt for Rust. This implementation conforms to the
//! [official description of Docopt](http://docopt.org/) and
//! [passes its test suite](https://github.com/docopt/docopt/pull/201).
//!
//! This library is [on GitHub](https://github.com/docopt/docopt.rs).
//!
//! Fundamentally, Docopt is a command line argument parser. The detail that
//! distinguishes it from most parsers is that the parser is derived from the
//! usage string. Here's a simple example:
//!
//! ```rust
//! use qsv_docopt::Docopt;
//!
//! // Write the Docopt usage string.
//! const USAGE: &'static str = "
//! Usage: cp [-a] <source> <dest>
//!        cp [-a] <source>... <dir>
//!
//! Options:
//!     -a, --archive  Copy everything.
//! ";
//!
//! // The argv. Normally you'd just use `parse` which will automatically
//! // use `std::env::args()`.
//! let argv = || vec!["cp", "-a", "file1", "file2", "dest/"];
//!
//! // Parse argv and exit the program with an error message if it fails.
//! let args = Docopt::new(USAGE)
//!                   .and_then(|d| d.argv(argv().into_iter()).parse())
//!                   .unwrap_or_else(|e| e.exit());
//!
//! // Now access your argv values. Synonyms work just fine!
//! assert!(args.get_bool("-a") && args.get_bool("--archive"));
//! assert_eq!(args.get_vec("<source>"), vec!["file1", "file2"]);
//! assert_eq!(args.get_str("<dir>"), "dest/");
//! assert_eq!(args.get_str("<dest>"), "");
//! ```
//!
//! # Type based decoding
//!
//! Often, command line values aren't just strings or booleans---sometimes
//! they are integers, or enums, or something more elaborate. Using the
//! standard Docopt interface can be inconvenient for this purpose, because
//! you'll need to convert all of the values explicitly. Instead, this crate
//! provides a `Decoder` that converts an `ArgvMap` to your custom struct.
//! Here is the same example as above using type based decoding:
//!
//! ## Non-UTF-8 Arguments
//!
//! **Note:** This library uses `std::env::args_os()` internally with lossy
//! UTF-8 conversion. This means that non-UTF-8 command-line arguments (rare
//! on most systems) will be converted to the Unicode replacement character (�).
//! If you need to preserve exact non-UTF-8 byte sequences, you'll need to
//! handle `std::env::args_os()` directly in your application before calling
//! docopt.
//!
//! ```rust
//! # fn main() {
//! use qsv_docopt::Docopt;
//! use serde::Deserialize;
//!
//! // Write the Docopt usage string.
//! const USAGE: &'static str = "
//! Usage: cp [-a] <source> <dest>
//!        cp [-a] <source>... <dir>
//!
//! Options:
//!     -a, --archive  Copy everything.
//! ";
//!
//! #[derive(Deserialize)]
//! struct Args {
//!     arg_source: Vec<String>,
//!     arg_dest: String,
//!     arg_dir: String,
//!     flag_archive: bool,
//! }
//!
//! let argv = || vec!["cp", "-a", "file1", "file2", "dest/"];
//! let args: Args = Docopt::new(USAGE)
//!     .and_then(|d| d.argv(argv().into_iter()).deserialize())
//!     .unwrap_or_else(|e| e.exit());
//!
//! // Now access your argv values.
//! fn s(x: &str) -> String { x.to_string() }
//! assert!(args.flag_archive);
//! assert_eq!(args.arg_source, vec![s("file1"), s("file2")]);
//! assert_eq!(args.arg_dir, s("dest/"));
//! assert_eq!(args.arg_dest, s(""));
//! # }
//! ```
//!
//! # Command line arguments for `rustc`
//!
//! Here's an example with a subset of `rustc`'s command line arguments that
//! shows more of Docopt and some of the benefits of type based decoding.
//!
//! ```rust
//! # fn main() {
//! # #![allow(non_snake_case)]
//! use std::fmt;
//!
//! use serde::Deserialize;
//!
//! use qsv_docopt::Docopt;
//!
//! // Write the Docopt usage string.
//! const USAGE: &'static str = "
//! Usage: rustc [options] [--cfg SPEC... -L PATH...] INPUT
//!        rustc (--help | --version)
//!
//! Options:
//!     -h, --help         Show this message.
//!     --version          Show the version of rustc.
//!     --cfg SPEC         Configure the compilation environment.
//!     -L PATH            Add a directory to the library search path.
//!     --emit TYPE        Configure the output that rustc will produce.
//!                        Valid values: asm, ir, bc, obj, link.
//!     --opt-level LEVEL  Optimize with possible levels 0-3.
//! ";
//!
//! #[derive(Deserialize)]
//! struct Args {
//!     arg_INPUT: String,
//!     flag_emit: Option<Emit>,
//!     flag_opt_level: Option<OptLevel>,
//!     flag_cfg: Vec<String>,
//!     flag_L: Vec<String>,
//!     flag_help: bool,
//!     flag_version: bool,
//! }
//!
//! // This is easy. The decoder will automatically restrict values to
//! // strings that match one of the enum variants.
//! #[derive(Deserialize)]
//! # #[derive(Debug, PartialEq)]
//! enum Emit { Asm, Ir, Bc, Obj, Link }
//!
//! // This one is harder because we want the user to specify an integer,
//! // but restrict it to a specific range. So we implement `Deserialize`
//! // ourselves.
//! # #[derive(Debug, PartialEq)]
//! enum OptLevel { Zero, One, Two, Three }
//! struct OptLevelVisitor;
//!
//! impl<'de> serde::de::Visitor<'de> for OptLevelVisitor {
//!     type Value = OptLevel;
//!
//!     fn expecting(&self, formatter: &mut fmt::Formatter) -> fmt::Result {
//!         formatter.write_str("a number from range 0..3")
//!     }
//!
//!     fn visit_u8<E>(self, n: u8) -> Result<Self::Value, E>
//!         where E: serde::de::Error
//!     {
//!         Ok(match n {
//!             0 => OptLevel::Zero, 1 => OptLevel::One,
//!             2 => OptLevel::Two, 3 => OptLevel::Three,
//!             n => {
//!                 let err = format!(
//!                     "Could not deserialize '{}' as opt-level.", n);
//!                 return Err(E::custom(err));
//!             }
//!         })
//!     }
//! }
//!
//! impl<'de> serde::de::Deserialize<'de> for OptLevel {
//!     fn deserialize<D>(d: D) -> Result<OptLevel, D::Error>
//!         where D: serde::de::Deserializer<'de>
//!     {
//!         d.deserialize_u8(OptLevelVisitor)
//!     }
//! }
//!
//! let argv = || vec!["rustc", "-L", ".", "-L", "..", "--cfg", "a",
//!                             "--opt-level", "2", "--emit=ir", "docopt.rs"];
//! let args: Args = Docopt::new(USAGE)
//!                         .and_then(|d| d.argv(argv().into_iter()).deserialize())
//!                         .unwrap_or_else(|e| e.exit());
//!
//! // Now access your argv values.
//! fn s(x: &str) -> String { x.to_string() }
//! assert_eq!(args.arg_INPUT, "docopt.rs".to_string());
//! assert_eq!(args.flag_L, vec![s("."), s("..")]);
//! assert_eq!(args.flag_cfg, vec![s("a")]);
//! assert_eq!(args.flag_opt_level, Some(OptLevel::Two));
//! assert_eq!(args.flag_emit, Some(Emit::Ir));
//! # }
//! ```

#![crate_name = "qsv_docopt"]
#![deny(missing_docs)]

#[macro_use]
pub mod utils;
pub use self::utils::*;

mod dopt;
pub use self::dopt::{ArgvMap, Deserializer, Docopt, Error, Value};
#[doc(hidden)]
pub mod parse;
mod synonym;
#[cfg(test)]
mod test;
```

## File: `src/parse.rs`
```rust
// I am overall pretty displeased with the quality of code in this module.
// I wrote it while simultaneously trying to build a mental model of Docopt's
// specification (hint: one does not exist in written form). As a result, there
// is a lot of coupling and some duplication.
//
// Some things that I think are good about the following code:
//
//   - The representation of a "usage pattern." I think it is a minimal representation of a
//     pattern's syntax. (One possible tweak: `Optional<Vec<Pattern>>` -> `Optional<Box<Pattern>>`.)
//   - Some disciplined use of regexes. I use a pretty basic state machine for parsing patterns, but
//     for teasing out the patterns and options from the Docopt string and for picking out flags
//     with arguments, I think regexes aren't too bad. There may be one or two scary ones though.
//   - The core matching algorithm is reasonably simple and concise, but I think writing down some
//     contracts will help me figure out how to make the code clearer.
//
// Some bad things:
//
//   - I tried several times to split some of the pieces in this module into separate modules. I
//     could find no clear separation. This suggests that there is too much coupling between parsing
//     components. I'm not convinced that the coupling is necessary.
//   - The parsers for patterns and argv share some structure. There may be an easy abstraction
//     waiting there.
//   - It is not efficient in the slightest. I tried to be conservative with copying strings, but I
//     think I failed. (It may not be worthwhile to fix this if it makes the code more awkward.
//     Docopt does not need to be efficient.)
//
// Some things to do immediately:
//
//   - Document representation and invariants.
//   - Less important: write contracts for functions.
//
// Long term:
//
//   - Write a specification for Docopt.

use std::{
    cmp::Ordering,
    collections::hash_map::Entry::{Occupied, Vacant},
    fmt,
};

use ahash::{AHashMap, AHashSet};
use regex::Regex;
use strsim::levenshtein;

use self::{
    Argument::{One, Zero},
    Atom::{Command, Long, Positional, Short},
    Pattern::{Alternates, Optional, PatAtom, Repeat, Sequence},
};
use crate::{
    cap_or_empty,
    dopt::Value::{self, Counted, List, Plain, Switch},
    synonym::SynonymMap,
};

macro_rules! err(
    ($($arg:tt)*) => (return Err(format!($($arg)*)))
);

#[derive(Clone)]
pub struct Parser {
    pub program:     String,
    pub full_doc:    String,
    pub usage:       String,
    pub descs:       SynonymMap<Atom, Options>,
    usages:          Vec<Pattern>,
    last_atom_added: Option<Atom>, // context for [default: ...]
}

impl Parser {
    pub fn new(doc: &str) -> Result<Parser, String> {
        let mut d = Parser {
            program:         String::new(),
            full_doc:        doc.into(),
            usage:           String::new(),
            usages:          vec![],
            descs:           SynonymMap::new(),
            last_atom_added: None,
        };
        d.parse(doc)?;
        Ok(d)
    }

    #[must_use]
    pub fn matches(&self, argv: &Argv<'_>) -> Option<SynonymMap<String, Value>> {
        for usage in &self.usages {
            if let Some(vals) = Matcher::matches(argv, usage) {
                return Some(vals);
            }
        }
        None
    }

    pub fn parse_argv(&self, argv: &[String], options_first: bool) -> Result<Argv<'_>, String> {
        Argv::new(self, argv, options_first)
    }
}

impl Parser {
    fn options_atoms(&self) -> Vec<Atom> {
        let mut atoms = vec![];
        for (atom, _) in self.descs.iter().filter(|&(_, opts)| opts.is_desc) {
            atoms.push(atom.clone());
        }
        atoms
    }

    fn has_arg(&self, atom: &Atom) -> bool {
        match self.descs.find(atom) {
            None => false,
            Some(opts) => opts.arg.has_arg(),
        }
    }

    fn has_repeat(&self, atom: &Atom) -> bool {
        match self.descs.find(atom) {
            None => false,
            Some(opts) => opts.repeats,
        }
    }

    fn parse(&mut self, doc: &str) -> Result<(), String> {
        decl_regex! {
            MUSAGE: r"(?s)(?i:usage):\s*(?P<prog>\S+)(?P<pats>.*?)(?:$|\n\s*\n)";
        }
        let Some(caps) = MUSAGE.captures(doc) else {
            err!("Could not find usage patterns in doc string.")
        };

        let prog = cap_or_empty(&caps, "prog");
        if prog.is_empty() {
            err!("Could not find program name in doc string.")
        }

        prog.clone_into(&mut self.program);
        caps.get(0).unwrap().as_str().clone_into(&mut self.usage);

        // Before we parse the usage patterns, we look for option descriptions.
        // We do this because the information in option descriptions can be
        // used to resolve ambiguities in usage patterns (i.e., whether
        // `--flag ARG` is a flag with an argument or not).
        //
        // From the docopt page, "every" line starting with a `-` or a `--`
        // is considered an option description. Instead, we restrict the lines
        // to any line *not* in the usage pattern section.
        //
        // *sigh* Apparently the above is not true. The official test suite
        // includes `Options: -a ...`, which means some lines not beginning
        // with `-` can actually have options.
        let (pstart, pend) = caps.get(0).map(|m| (m.start(), m.end())).unwrap();
        let (before, after) = (&doc[..pstart], &doc[pend..]);
        // We process every line here (instead of restricting to lines starting
        // with "-") because we need to check every line for a default value.
        // The default value always belongs to the most recently defined desc.
        for line in before.lines().chain(after.lines()) {
            self.parse_desc(line)?;
        }

        let mprog = format!("^(?:{})?\\s*(.*?)\\s*$", regex::escape(prog));
        let pats = Regex::new(&mprog).unwrap();

        let pats_str = cap_or_empty(&caps, "pats");
        if pats_str.is_empty() {
            let pattern = PatParser::new(self, "").parse()?;
            self.usages.push(pattern);
        } else {
            for line in pats_str.lines() {
                for pat in pats.captures_iter(line.trim()) {
                    let pattern = PatParser::new(self, &pat[1]).parse()?;
                    self.usages.push(pattern);
                }
            }
        }
        Ok(())
    }

    fn parse_desc(&mut self, full_desc: &str) -> Result<(), String> {
        decl_regex! {
            OPTIONS:r"^\s*(?i:options:)\s*";
            ISFLAG: r"^(-\S|--\S)";
            REMOVE_DESC: r"  .*$";
            NORMALIZE_FLAGS: r"([^-\s]), -";
            FIND_FLAGS:
                r"(?x)
                (?:(?P<long>--[^\x20\t=]+)|(?P<short>-[^\x20\t=]+))
                (?:(?:\x20|=)(?P<arg>[^.-]\S*))?
                (?P<repeated>\x20\.\.\.)?";
        }
        let desc = OPTIONS.replace(full_desc.trim(), "");
        let desc = &*desc;
        if !ISFLAG.is_match(desc) {
            self.parse_default(full_desc)?;
            return Ok(());
        }

        // Get rid of the description, which must be at least two spaces
        // after the flag or argument.
        let desc = REMOVE_DESC.replace(desc, "");
        // Normalize `-x, --xyz` to `-x --xyz`.
        let desc = NORMALIZE_FLAGS.replace(&desc, "$1 -");
        let desc = desc.trim();

        let (mut short, mut long) = <(String, String)>::default();
        let mut has_arg = false;
        let mut last_end = 0;
        let mut repeated = false;
        for flags in FIND_FLAGS.captures_iter(desc) {
            last_end = flags.get(0).unwrap().end();
            if !cap_or_empty(&flags, "repeated").is_empty() {
                // If the "repeated" subcapture is not empty, then we have
                // a valid repeated option.
                repeated = true;
            }
            let (s, l) = (cap_or_empty(&flags, "short"), cap_or_empty(&flags, "long"));
            if !s.is_empty() {
                if !short.is_empty() {
                    err!(
                        "Only one short flag is allowed in an option description, but found \
                         '{short}' and '{s}'."
                    )
                }
                short = s.into();
            }
            if !l.is_empty() {
                if !long.is_empty() {
                    err!(
                        "Only one long flag is allowed in an option description, but found \
                         '{long}' and '{l}'."
                    )
                }
                long = l.into();
            }
            if let Some(arg) = flags.name("arg").map(|m| m.as_str())
                && !arg.is_empty()
            {
                if !Atom::is_arg(arg) {
                    err!("Argument '{arg}' is not of the form ARG or <arg>.")
                }
                has_arg = true; // may be changed to default later
            }
        }
        // Make sure that we consumed everything. If there are leftovers,
        // then there is some malformed description. Alert the user.
        assert!(last_end <= desc.len());
        if last_end < desc.len() {
            err!(
                "Extraneous text '{}' in option description '{desc}'.",
                &desc[last_end..]
            )
        }
        self.add_desc(&short, &long, has_arg, repeated);
        // Looking for default in this line must come after adding the
        // description, otherwise `parse_default` won't know which option
        // to assign it to.
        self.parse_default(full_desc)
    }

    fn parse_default(&mut self, desc: &str) -> Result<(), String> {
        decl_regex! {
            FIND_DEFAULT: r"\[(?i:default):(?P<val>.*)\]";
        }
        let defval = match FIND_DEFAULT.captures(desc) {
            None => return Ok(()),
            Some(c) => cap_or_empty(&c, "val").trim(),
        };
        let Some(ref last_atom) = self.last_atom_added else {
            err!("Found default value '{defval}' in '{desc}' before first option description.")
        };
        let opts = self
            .descs
            .find_mut(last_atom)
            .unwrap_or_else(|| panic!("BUG: last opt desc key ('{last_atom:?}') is invalid."));
        match opts.arg {
            One(None) => {} // OK
            Zero => err!(
                "Cannot assign default value '{defval}' to flag '{last_atom}' that has no \
                 arguments."
            ),
            One(Some(ref curval)) => err!(
                "Flag '{last_atom}' already has a default value of '{curval}' (second default \
                 value: '{defval}')."
            ),
        }
        opts.arg = One(Some(defval.into()));
        Ok(())
    }

    fn add_desc(&mut self, short: &str, long: &str, has_arg: bool, repeated: bool) {
        assert!(!short.is_empty() || !long.is_empty());
        if !short.is_empty() && short.chars().count() != 2 {
            // It looks like the reference implementation just ignores
            // these lines.
            return;
        }
        let mut opts = Options::new(repeated, if has_arg { One(None) } else { Zero });
        opts.is_desc = true;

        if !short.is_empty() && !long.is_empty() {
            let (short, long) = (Atom::new(short), Atom::new(long));
            self.descs.insert(long.clone(), opts);
            self.descs.insert_synonym(short, long.clone());
            self.last_atom_added = Some(long);
        } else if !short.is_empty() {
            let short = Atom::new(short);
            self.descs.insert(short.clone(), opts);
            self.last_atom_added = Some(short);
        } else if !long.is_empty() {
            let long = Atom::new(long);
            self.descs.insert(long.clone(), opts);
            self.last_atom_added = Some(long);
        }
    }
}

impl fmt::Debug for Parser {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> Result<(), fmt::Error> {
        fn sorted<T: Ord>(mut xs: Vec<T>) -> Vec<T> {
            xs.sort();
            xs
        }

        writeln!(f, "=====")?;
        writeln!(f, "Program: {}", self.program)?;

        writeln!(f, "Option descriptions:")?;
        let keys = sorted(self.descs.keys().collect());
        for &k in &keys {
            writeln!(f, "  '{k}' => {:?}", self.descs.get(k))?;
        }

        writeln!(f, "Synonyms:")?;
        let keys: Vec<(&Atom, &Atom)> = sorted(self.descs.synonyms().collect());
        for &(from, to) in &keys {
            writeln!(f, "  {from:?} => {to:?}")?;
        }

        writeln!(f, "Usages:")?;
        for pat in &self.usages {
            writeln!(f, "  {pat:?}")?;
        }
        writeln!(f, "=====")
    }
}

struct PatParser<'a> {
    dopt:      &'a mut Parser,
    tokens:    Vec<String>, // used while parsing a single usage pattern
    curi:      usize,       // ^^ index into pattern chars
    expecting: Vec<char>,   // stack of expected ']' or ')'
}

impl<'a> PatParser<'a> {
    fn new(dopt: &'a mut Parser, pat: &str) -> PatParser<'a> {
        PatParser {
            dopt,
            tokens: pattern_tokens(pat),
            curi: 0,
            expecting: vec![],
        }
    }

    fn parse(&mut self) -> Result<Pattern, String> {
        // let mut seen = HashSet::new();
        let mut p = self.pattern()?;
        match self.expecting.pop() {
            None => {}
            Some(c) => err!("Unclosed group. Expected '{c}'."),
        }
        p.add_options_shortcut(self.dopt);
        p.tag_repeats(&mut self.dopt.descs);
        Ok(p)
    }

    fn pattern(&mut self) -> Result<Pattern, String> {
        let mut alts = vec![];
        let mut seq = vec![];
        while !self.is_eof() {
            match self.cur() {
                "..." => {
                    err!("'...' must appear directly after a group, argument, flag or command.")
                }
                "-" | "--" => {
                    // As per specification, `-` and `--` by themselves are
                    // just commands that should be interpreted conventionally.
                    seq.push(self.command());
                }
                "|" => {
                    if seq.is_empty() {
                        err!("Unexpected '|'. Not in form 'a | b | c'.")
                    }
                    self.next_noeof("pattern")?;
                    alts.push(Sequence(seq));
                    seq = vec![];
                }
                "]" | ")" => {
                    if seq.is_empty() {
                        err!("Unexpected '{}'. Empty groups are not allowed.", self.cur())
                    }
                    match self.expecting.pop() {
                        None => err!("Unexpected '{}'. No open bracket found.", self.cur()),
                        Some(c) => {
                            if c != self.cur().chars().next().unwrap() {
                                err!("Expected '{c}' but got '{}'.", self.cur())
                            }
                        }
                    }
                    let mk: fn(Vec<Pattern>) -> Pattern = if self.cur() == "]" {
                        Optional
                    } else {
                        Sequence
                    };
                    self.next();
                    return if alts.is_empty() {
                        Ok(mk(seq))
                    } else {
                        alts.push(Sequence(seq));
                        Ok(mk(vec![Alternates(alts)]))
                    };
                }
                "[" => {
                    // Check for special '[options]' shortcut.
                    if self.atis(1, "options") && self.atis(2, "]") {
                        self.next(); // cur == options
                        self.next(); // cur == ]
                        self.next();
                        seq.push(self.maybe_repeat(Optional(vec![])));
                        continue;
                    }
                    self.expecting.push(']');
                    seq.push(self.group()?);
                }
                "(" => {
                    self.expecting.push(')');
                    seq.push(self.group()?);
                }
                _ => {
                    if Atom::is_short(self.cur()) {
                        seq.extend(self.flag_short()?);
                    } else if Atom::is_long(self.cur()) {
                        seq.push(self.flag_long()?);
                    } else if Atom::is_arg(self.cur()) {
                        // These are always positional.
                        // Arguments for -s and --short are picked up
                        // when parsing flags.
                        seq.push(self.positional());
                    } else if Atom::is_cmd(self.cur()) {
                        seq.push(self.command());
                    } else {
                        err!("Unknown token type '{}'.", self.cur())
                    }
                }
            }
        }
        if alts.is_empty() {
            Ok(Sequence(seq))
        } else {
            alts.push(Sequence(seq));
            Ok(Alternates(alts))
        }
    }

    fn flag_short(&mut self) -> Result<Vec<Pattern>, String> {
        let mut seq = vec![];
        let stacked: String = self.cur()[1..].into();
        for (i, c) in stacked.chars().enumerate() {
            let atom = self.dopt.descs.resolve(&Short(c));
            let mut pat = PatAtom(atom.clone());
            if self.dopt.has_repeat(&atom) {
                pat = Pattern::repeat(pat);
            }
            seq.push(pat);

            // The only way for a short option to have an argument is if
            // it's specified in an option description.
            if self.dopt.has_arg(&atom) {
                // At this point, the flag MUST have an argument. Therefore,
                // we interpret the "rest" of the characters as the argument.
                // If the "rest" is empty, then we peek to find and make sure
                // there is an argument.
                let rest = &stacked[i + 1..];
                if rest.is_empty() {
                    self.next_flag_arg(&atom)?;
                } else {
                    self.errif_invalid_flag_arg(&atom, rest)?;
                }
                // We either error'd or consumed the rest of the short stack as
                // an argument.
                break;
            }
            self.add_atom_ifnotexists(Zero, &atom);
        }
        self.next();
        // This is a little weird. We've got to manually look for a repeat
        // operator right after the stack, and then apply it to each short
        // flag we generated.
        // If "sequences" never altered semantics, then we could just use that
        // here to group a short stack.
        if self.atis(0, "...") {
            self.next();
            seq = seq.into_iter().map(Pattern::repeat).collect();
        }
        Ok(seq)
    }

    fn flag_long(&mut self) -> Result<Pattern, String> {
        let (atom, arg) = parse_long_equal(self.cur())?;
        let atom = self.dopt.descs.resolve(&atom);
        if self.dopt.descs.contains_key(&atom) {
            // Options already exist for this atom, so we must check to make
            // sure things are consistent.
            let has_arg = self.dopt.has_arg(&atom);
            if arg.has_arg() && !has_arg {
                // Found `=` in usage, but previous usage of this flag
                // didn't specify an argument.
                err!("Flag '{atom}' does not take any arguments.")
            } else if !arg.has_arg() && has_arg {
                // Didn't find any `=` in usage for this flag, but previous
                // usage of this flag specifies an argument.
                // So look for `--flag ARG`
                self.next_flag_arg(&atom)?;
                // We don't care about the value of `arg` since options
                // already exist. (In which case, the argument value can never
                // change.)
            }
        }
        self.add_atom_ifnotexists(arg, &atom);
        self.next();
        let pat = if self.dopt.has_repeat(&atom) {
            Pattern::repeat(PatAtom(atom))
        } else {
            PatAtom(atom)
        };
        Ok(self.maybe_repeat(pat))
    }

    fn next_flag_arg(&mut self, atom: &Atom) -> Result<(), String> {
        self.next_noeof(&format!("argument for flag '{atom}'"))?;
        self.errif_invalid_flag_arg(atom, self.cur())
    }

    fn errif_invalid_flag_arg(&self, atom: &Atom, arg: &str) -> Result<(), String> {
        if !Atom::is_arg(arg) {
            err!("Expected argument for flag '{atom}', but found malformed argument '{arg}'.")
        }
        Ok(())
    }

    fn command(&mut self) -> Pattern {
        let atom = Atom::new(self.cur());
        self.add_atom_ifnotexists(Zero, &atom);
        self.next();
        self.maybe_repeat(PatAtom(atom))
    }

    fn positional(&mut self) -> Pattern {
        let atom = Atom::new(self.cur());
        self.add_atom_ifnotexists(Zero, &atom);
        self.next();
        self.maybe_repeat(PatAtom(atom))
    }

    fn add_atom_ifnotexists(&mut self, arg: Argument, atom: &Atom) {
        if !self.dopt.descs.contains_key(atom) {
            let opts = Options::new(false, arg);
            self.dopt.descs.insert(atom.clone(), opts);
        }
    }

    fn group(&mut self) -> Result<Pattern, String> {
        self.next_noeof("pattern")?;
        let pat = self.pattern()?;
        Ok(self.maybe_repeat(pat))
    }

    fn maybe_repeat(&mut self, pat: Pattern) -> Pattern {
        if self.atis(0, "...") {
            self.next();
            Pattern::repeat(pat)
        } else {
            pat
        }
    }

    fn is_eof(&self) -> bool {
        self.curi == self.tokens.len()
    }
    fn next(&mut self) {
        if self.curi == self.tokens.len() {
            return;
        }
        self.curi += 1;
    }
    fn next_noeof(&mut self, expected: &str) -> Result<(), String> {
        self.next();
        if self.curi == self.tokens.len() {
            err!("Expected {expected} but reached end of usage pattern.")
        }
        Ok(())
    }
    fn cur(&self) -> &str {
        &self.tokens[self.curi]
    }
    fn atis(&self, offset: usize, is: &str) -> bool {
        let i = self.curi + offset;
        i < self.tokens.len() && self.tokens[i] == is
    }
}

#[derive(Clone, Debug)]
enum Pattern {
    Alternates(Vec<Pattern>),
    Sequence(Vec<Pattern>),
    Optional(Vec<Pattern>),
    Repeat(Box<Pattern>),
    PatAtom(Atom),
}

#[allow(clippy::derive_ord_xor_partial_ord)]
#[derive(PartialEq, Eq, Ord, Hash, Clone, Debug)]
pub enum Atom {
    Short(char),
    Long(String),
    Command(String),
    Positional(String),
}

#[derive(Clone, Debug)]
pub struct Options {
    /// Set to true if this atom is ever repeated in any context.
    /// For positional arguments, non-argument flags and commands, repetition
    /// means that they become countable.
    /// For flags with arguments, repetition means multiple distinct values
    /// can be specified (and are represented as a Vec).
    pub repeats: bool,

    /// This specifies whether this atom has any arguments.
    /// For commands and positional arguments, this is always Zero.
    /// Flags can have zero or one argument, with an optionally default value.
    pub arg: Argument,

    /// Whether it shows up in the "options description" second.
    pub is_desc: bool,
}

#[derive(Clone, Debug, PartialEq)]
pub enum Argument {
    Zero,
    One(Option<String>), // optional default value
}

impl Pattern {
    fn add_options_shortcut(&mut self, par: &Parser) {
        fn add(pat: &mut Pattern, all_atoms: &AHashSet<Atom>, par: &Parser) {
            match *pat {
                Alternates(ref mut ps) | Sequence(ref mut ps) => {
                    for p in ps.iter_mut() {
                        add(p, all_atoms, par);
                    }
                }
                Repeat(ref mut p) => add(p, all_atoms, par),
                PatAtom(_) => {}
                Optional(ref mut ps) => {
                    if ps.is_empty() {
                        for atom in par.options_atoms() {
                            if !all_atoms.contains(&atom) {
                                if par.has_repeat(&atom) {
                                    ps.push(Pattern::repeat(PatAtom(atom)));
                                } else {
                                    ps.push(PatAtom(atom));
                                }
                            }
                        }
                    } else {
                        for p in &mut *ps {
                            add(p, all_atoms, par);
                        }
                    }
                }
            }
        }
        let all_atoms = self.all_atoms();
        add(self, &all_atoms, par);
    }

    fn all_atoms(&self) -> AHashSet<Atom> {
        fn all_atoms(pat: &Pattern, set: &mut AHashSet<Atom>) {
            match *pat {
                Alternates(ref ps) | Sequence(ref ps) | Optional(ref ps) => {
                    for p in ps {
                        all_atoms(p, set);
                    }
                }
                Repeat(ref p) => all_atoms(p, set),
                PatAtom(ref a) => {
                    set.insert(a.clone());
                }
            }
        }
        let mut set = AHashSet::new();
        all_atoms(self, &mut set);
        set
    }

    fn tag_repeats(&self, map: &mut SynonymMap<Atom, Options>) {
        fn dotag(
            p: &Pattern,
            rep: bool,
            map: &mut SynonymMap<Atom, Options>,
            seen: &mut AHashSet<Atom>,
        ) {
            match *p {
                Alternates(ref ps) => {
                    // This is a bit tricky. Basically, we don't want the
                    // existence of an item in mutually exclusive alternations
                    // to affect whether it repeats or not.
                    // However, we still need to record seeing each item in
                    // each alternation.
                    let fresh = seen.clone();
                    for p in ps {
                        let mut isolated = fresh.clone();
                        dotag(p, rep, map, &mut isolated);
                        for a in isolated {
                            seen.insert(a);
                        }
                    }
                }
                Sequence(ref ps) | Optional(ref ps) => {
                    for p in ps {
                        dotag(p, rep, map, seen);
                    }
                }
                Repeat(ref p) => dotag(p, true, map, seen),
                PatAtom(ref atom) => {
                    let opt = map.find_mut(atom).expect("bug: no atom found");
                    opt.repeats = opt.repeats || rep || seen.contains(atom);
                    seen.insert(atom.clone());
                }
            }
        }
        let mut seen = AHashSet::new();
        dotag(self, false, map, &mut seen);
    }

    fn repeat(p: Pattern) -> Pattern {
        match p {
            p @ Repeat(_) => p,
            p => Repeat(Box::new(p)),
        }
    }
}

impl Atom {
    #[must_use]
    pub fn new(s: &str) -> Atom {
        if Atom::is_short(s) {
            Short(s[1..].chars().next().unwrap())
        } else if Atom::is_long(s) {
            Long(s[2..].into())
        } else if Atom::is_arg(s) {
            if s.starts_with('<') && s.ends_with('>') {
                Positional(s[1..s.len() - 1].into())
            } else {
                Positional(s.into())
            }
        } else if Atom::is_cmd(s) {
            Command(s.into())
        } else {
            panic!("Unknown atom string: '{s}'")
        }
    }

    fn is_short(s: &str) -> bool {
        decl_regex! {
            IS_SHORT_RE: r"^-[^-]\S*$";
        }
        IS_SHORT_RE.is_match(s)
    }

    fn is_long(s: &str) -> bool {
        decl_regex! {
            IS_LONG_RE: r"^--\S+(?:<[^>]+>)?$";
        }
        IS_LONG_RE.is_match(s)
    }

    fn is_long_argv(s: &str) -> bool {
        decl_regex! {
            IS_LONG_ARGV_RE: r"^--\S+(=.+)?$";
        }
        IS_LONG_ARGV_RE.is_match(s)
    }

    fn is_arg(s: &str) -> bool {
        decl_regex! {
            IS_ARG_RE: r"^(\p{Lu}+|<[^>]+>)$";
        }
        IS_ARG_RE.is_match(s)
    }

    fn is_cmd(s: &str) -> bool {
        decl_regex! {
            IS_CMD_RE: r"^(-|--|[^-]\S*)$";
        }
        IS_CMD_RE.is_match(s)
    }

    // NOTE: NO LONGER NEEDED WHEN WE SIMPLIFIED partial_cmp
    // Assigns an integer to each variant of Atom. (For easier sorting.)
    // const fn type_as_usize(&self) -> usize {
    //     match *self {
    //         Short(_) => 0,
    //         Long(_) => 1,
    //         Command(_) => 2,
    //         Positional(_) => 3,
    //     }
    // }
}

impl PartialOrd for Atom {
    fn partial_cmp(&self, other: &Atom) -> Option<Ordering> {
        Some(self.cmp(other))
    }
}

impl fmt::Display for Atom {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        match *self {
            Short(c) => write!(f, "-{c}"),
            Long(ref s) => write!(f, "--{s}"),
            Command(ref s) => write!(f, "{s}"),
            Positional(ref s) => {
                if s.chars().all(char::is_uppercase) {
                    write!(f, "{s}")
                } else {
                    write!(f, "<{s}>")
                }
            }
        }
    }
}

impl Options {
    const fn new(rep: bool, arg: Argument) -> Options {
        Options {
            repeats: rep,
            arg,
            is_desc: false,
        }
    }
}

impl Argument {
    const fn has_arg(&self) -> bool {
        match *self {
            Zero => false,
            One(_) => true,
        }
    }
}

#[doc(hidden)]
pub struct Argv<'a> {
    /// A representation of an argv string as an ordered list of tokens.
    /// This contains only positional arguments and commands.
    positional: Vec<ArgvToken>,
    /// Same as positional, but contains short and long flags.
    /// Each flag may have an argument string.
    flags:      Vec<ArgvToken>,
    /// Counts the number of times each flag appears.
    counts:     AHashMap<Atom, usize>,

    // State for parser.
    dopt:          &'a Parser,
    argv:          Vec<String>,
    curi:          usize,
    options_first: bool,
}

#[derive(Clone, Debug)]
struct ArgvToken {
    atom: Atom,
    arg:  Option<String>,
}

impl<'a> Argv<'a> {
    fn new(dopt: &'a Parser, argv: &[String], options_first: bool) -> Result<Argv<'a>, String> {
        let mut a = Argv {
            positional: vec![],
            flags: vec![],
            counts: AHashMap::new(),
            dopt,
            argv: argv.to_vec(),
            curi: 0,
            options_first,
        };
        a.parse()?;
        for flag in &a.flags {
            match a.counts.entry(flag.atom.clone()) {
                Vacant(v) => {
                    v.insert(1);
                }
                Occupied(mut v) => {
                    *v.get_mut() += 1;
                }
            }
        }
        Ok(a)
    }

    fn parse(&mut self) -> Result<(), String> {
        let mut seen_double_dash = false;
        while self.curi < self.argv.len() {
            let current_arg = self.cur();
            let do_flags = !seen_double_dash && (!self.options_first || self.positional.is_empty());

            if do_flags && Atom::is_short(current_arg) {
                let stacked: String = current_arg[1..].into();
                for (i, c) in stacked.chars().enumerate() {
                    let mut tok = ArgvToken {
                        atom: self.dopt.descs.resolve(&Short(c)),
                        arg:  None,
                    };
                    if !self.dopt.descs.contains_key(&tok.atom) {
                        err!("Unknown flag: '{}'", &tok.atom);
                    }
                    if self.dopt.has_arg(&tok.atom) {
                        let rest = &stacked[i + 1..];
                        tok.arg = Some(if rest.is_empty() {
                            let arg = self.next_arg(&tok.atom)?;
                            arg.into()
                        } else {
                            rest.into()
                        });
                        self.flags.push(tok);
                        // We've either produced an error or gobbled up the
                        // rest of these stacked short flags, so stop.
                        break;
                    }
                    self.flags.push(tok);
                }
            } else if do_flags && Atom::is_long_argv(current_arg) {
                let (atom, mut arg) = parse_long_equal_argv(current_arg);
                let atom = self.dopt.descs.resolve(&atom);
                if !self.dopt.descs.contains_key(&atom) {
                    return self.err_unknown_flag(&atom);
                }
                if let Some(arg_value) = &arg {
                    if !self.dopt.has_arg(&atom) {
                        err!(
                            "Flag '{}' cannot have an argument, but found '{}'.",
                            &atom,
                            arg_value
                        )
                    }
                } else if self.dopt.has_arg(&atom) {
                    self.next_noeof(&format!("argument for flag '{}'", &atom))?;
                    arg = Some(self.cur().into());
                }
                self.flags.push(ArgvToken { atom, arg });
            } else if !seen_double_dash && current_arg == "--" {
                seen_double_dash = true;
            } else {
                // Yup, we *always* insert a positional argument, which
                // means we completely neglect `Command` here.
                // This is because we can't tell whether something is a
                // `command` or not until we start pattern matching.
                let tok = ArgvToken {
                    atom: Positional(current_arg.into()),
                    arg:  None,
                };
                self.positional.push(tok);
            }
            self.next();
        }
        Ok(())
    }

    fn err_unknown_flag(&self, atom: &Atom) -> Result<(), String> {
        let mut best = String::new();
        let flag = atom.to_string();
        let mut min = usize::MAX;

        let mut possibles = Vec::new();

        for (key, _) in self.dopt.descs.synonyms() {
            possibles.push(key);
        }

        for key in self.dopt.descs.keys() {
            possibles.push(key);
        }

        for key in &possibles {
            match **key {
                Long(_) | Command(_) => {
                    let name = key.to_string();
                    let dist = levenshtein(&flag, &name);
                    if dist < 3 && dist < min {
                        min = dist;
                        best = name;
                    }
                }
                _ => {}
            }
        }
        if best.is_empty() {
            err!("Unknown flag: '{}'", &atom);
        }
        err!("Unknown flag: '{}'. Did you mean '{}'?", &atom, &best)
    }

    fn cur(&self) -> &str {
        self.at(0)
    }
    fn at(&self, i: usize) -> &str {
        &self.argv[self.curi + i]
    }
    fn next(&mut self) {
        if self.curi < self.argv.len() {
            self.curi += 1;
        }
    }
    #[inline]
    fn next_arg(&mut self, atom: &Atom) -> Result<&str, String> {
        let expected = format!("argument for flag '{atom}'");
        self.next_noeof(&expected)?;
        Ok(self.cur())
    }
    fn next_noeof(&mut self, expected: &str) -> Result<(), String> {
        self.next();
        if self.curi == self.argv.len() {
            err!("Expected {expected} but reached end of arguments.")
        }
        Ok(())
    }
}

impl fmt::Debug for Argv<'_> {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> Result<(), fmt::Error> {
        writeln!(f, "Positional: {:?}", self.positional)?;
        writeln!(f, "Flags: {:?}", self.flags)?;
        writeln!(f, "Counts: {:?}", self.counts)?;
        Ok(())
    }
}

struct Matcher<'a, 'b: 'a> {
    argv: &'a Argv<'b>,
}

#[derive(Clone, Debug, PartialEq)]
struct MState {
    argvi:      usize,                 // index into Argv.positional
    counts:     AHashMap<Atom, usize>, // flags remaining for pattern consumption
    max_counts: AHashMap<Atom, usize>, // optional flag appearances
    vals:       AHashMap<Atom, Value>,
}

impl MState {
    fn fill_value(&mut self, key: Atom, rep: bool, arg: Option<String>) -> bool {
        match (arg, rep) {
            (None, false) => {
                self.vals.insert(key, Switch(true));
            }
            (Some(arg), false) => {
                self.vals.insert(key, Plain(Some(arg)));
            }
            (None, true) => match self.vals.entry(key) {
                Vacant(v) => {
                    v.insert(Counted(1));
                }
                Occupied(mut v) => match *v.get_mut() {
                    Counted(ref mut c) => {
                        *c += 1;
                    }
                    _ => return false,
                },
            },
            (Some(arg), true) => match self.vals.entry(key) {
                Vacant(v) => {
                    v.insert(List(vec![arg]));
                }
                Occupied(mut v) => match *v.get_mut() {
                    List(ref mut vs) => vs.push(arg),
                    _ => return false,
                },
            },
        }
        true
    }

    #[inline]
    fn add_value(
        &mut self,
        opts: &Options,
        spec: &Atom,
        atom: &Atom,
        arg: &Option<String>,
    ) -> bool {
        assert!(
            opts.arg.has_arg() == arg.is_some(),
            "'{atom:?}' should have an argument but doesn't"
        );
        match *atom {
            Short(_) | Long(_) => self.fill_value(spec.clone(), opts.repeats, arg.clone()),
            Positional(ref v) => {
                assert!(!opts.arg.has_arg());
                self.fill_value(spec.clone(), opts.repeats, Some(v.clone()))
            }
            Command(_) => {
                assert!(!opts.arg.has_arg());
                self.fill_value(spec.clone(), opts.repeats, None)
            }
        }
    }

    #[inline]
    fn use_flag(&mut self, flag: &Atom) -> bool {
        match self.max_counts.entry(flag.clone()) {
            Vacant(v) => {
                v.insert(0);
            }
            Occupied(_) => {}
        }
        match self.counts.entry(flag.clone()) {
            Vacant(_) => false,
            Occupied(mut v) => {
                let c = v.get_mut();
                if *c == 0 {
                    false
                } else {
                    *c -= 1;
                    true
                }
            }
        }
    }

    #[inline]
    fn use_optional_flag(&mut self, flag: &Atom) {
        match self.max_counts.entry(flag.clone()) {
            Vacant(v) => {
                v.insert(1);
            }
            Occupied(mut v) => {
                *v.get_mut() += 1;
            }
        }
    }

    #[inline]
    fn match_cmd_or_posarg(&mut self, spec: &Atom, argv: &ArgvToken) -> Option<ArgvToken> {
        match (spec, &argv.atom) {
            (_, &Command(_)) => {
                // This is impossible because the argv parser doesn't know
                // how to produce `Command` values.
                unreachable!()
            }
            (Command(n1), Positional(n2)) if n1 == n2 => {
                // Coerce a positional to a command because the pattern
                // demands it and the positional argument matches it.
                self.argvi += 1;
                Some(ArgvToken {
                    atom: spec.clone(),
                    arg:  None,
                })
            }
            (&Positional(_), _) => {
                self.argvi += 1;
                Some(argv.clone())
            }
            _ => None,
        }
    }
}

impl<'a> Matcher<'a, '_> {
    fn matches(argv: &'a Argv<'_>, pat: &Pattern) -> Option<SynonymMap<String, Value>> {
        let m = Matcher { argv };
        let init = MState {
            argvi:      0,
            counts:     argv.counts.clone(),
            max_counts: AHashMap::new(),
            vals:       AHashMap::new(),
        };
        m.states(pat, &init)
            .into_iter()
            .filter(|s| m.state_consumed_all_argv(s))
            .filter(|s| m.state_has_valid_flags(s))
            .find(|s| m.state_valid_num_flags(s))
            .map(|mut s| {
                m.add_flag_values(&mut s);
                m.add_default_values(&mut s);

                // Build a synonym map so that it's easier to look up values.
                let mut synmap: SynonymMap<String, Value> = SynonymMap::new();
                for (k, v) in s.vals {
                    synmap.insert(k.to_string(), v);
                }
                for (from, to) in argv.dopt.descs.synonyms() {
                    let (from, to) = (from.to_string(), to.to_string());
                    if synmap.contains_key(&to) {
                        synmap.insert_synonym(from, to);
                    }
                }
                synmap
            })
    }

    fn token_from(&self, state: &MState) -> Option<&ArgvToken> {
        self.argv.positional.get(state.argvi)
    }

    #[inline]
    fn add_value(
        &self,
        state: &mut MState,
        atom_spec: &Atom,
        atom: &Atom,
        arg: &Option<String>,
    ) -> bool {
        let opts = self.argv.dopt.descs.get(atom_spec);
        state.add_value(opts, atom_spec, atom, arg)
    }

    #[inline]
    fn add_flag_values(&self, state: &mut MState) {
        for tok in &self.argv.flags {
            self.add_value(state, &tok.atom, &tok.atom, &tok.arg);
        }
    }

    #[inline]
    fn add_default_values(&self, state: &mut MState) {
        decl_regex! {
            SPLIT_SPACE: r"\s+";
        }
        let vs = &mut state.vals;
        for (a, opts) in self.argv.dopt.descs.iter() {
            if vs.contains_key(a) {
                continue;
            }
            let atom = a.clone();
            match (opts.repeats, &opts.arg) {
                (false, &Zero) => {
                    match *a {
                        Positional(_) => vs.insert(atom, Plain(None)),
                        _ => vs.insert(atom, Switch(false)),
                    };
                }
                (true, &Zero) => {
                    match *a {
                        Positional(_) => vs.insert(atom, List(vec![])),
                        _ => vs.insert(atom, Counted(0)),
                    };
                }
                (false, &One(None)) => {
                    vs.insert(atom, Plain(None));
                }
                (true, &One(None)) => {
                    vs.insert(atom, List(vec![]));
                }
                (false, &One(Some(ref v))) => {
                    vs.insert(atom, Plain(Some(v.clone())));
                }
                (true, &One(Some(ref v))) => {
                    let words = SPLIT_SPACE
                        .split(v)
                        .map(std::borrow::ToOwned::to_owned)
                        .collect();
                    vs.insert(atom, List(words));
                }
            }
        }
    }

    #[inline]
    fn state_consumed_all_argv(&self, state: &MState) -> bool {
        self.argv.positional.len() == state.argvi
    }

    #[inline]
    fn state_has_valid_flags(&self, state: &MState) -> bool {
        self.argv
            .counts
            .keys()
            .all(|flag| state.max_counts.contains_key(flag))
    }

    #[inline]
    fn state_valid_num_flags(&self, state: &MState) -> bool {
        state
            .counts
            .iter()
            .all(|(flag, count)| count <= &state.max_counts[flag])
    }

    #[inline]
    fn states(&self, pat: &Pattern, init: &MState) -> Vec<MState> {
        match *pat {
            Alternates(ref ps) => {
                let mut alt_states = vec![];
                for p in ps {
                    alt_states.extend(self.states(p, init));
                }
                alt_states
            }
            Sequence(ref ps) => {
                let (mut states, mut next) = (vec![], vec![]);
                let mut iter = ps.iter();
                match iter.next() {
                    None => return vec![init.clone()],
                    Some(p) => states.extend(self.states(p, init)),
                }
                for p in iter {
                    for s in states {
                        next.extend(self.states(p, &s));
                    }
                    states = vec![];
                    states.extend(next);
                    next = vec![];
                }
                states
            }
            Optional(ref ps) => {
                let mut base = init.clone();
                let mut noflags = vec![];
                for p in ps {
                    match p {
                        // Prevent exponential growth in cases like [--flag...]
                        // See https://github.com/docopt/docopt.rs/issues/195
                        Repeat(b) => match &**b {
                            &PatAtom(ref a @ Short(_)) | &PatAtom(ref a @ Long(_)) => {
                                let argv_count = self.argv.counts.get(a).map_or(0, |&x| x);
                                let max_count = base.max_counts.get(a).map_or(0, |&x| x);
                                if argv_count > max_count {
                                    for _ in max_count..argv_count {
                                        base.use_optional_flag(a);
                                    }
                                }
                            }
                            _ => {
                                noflags.push(p);
                            }
                        },
                        &PatAtom(ref a @ Short(_)) | &PatAtom(ref a @ Long(_)) => {
                            let argv_count = self.argv.counts.get(a).map_or(0, |&x| x);
                            let max_count = base.max_counts.get(a).map_or(0, |&x| x);
                            if argv_count > max_count {
                                base.use_optional_flag(a);
                            }
                        }
                        other => {
                            noflags.push(other);
                        }
                    }
                }
                let mut states = vec![];
                self.all_option_states(&base, &mut states, &noflags);
                states
            }
            Repeat(ref p) => match &**p {
                &PatAtom(ref a @ Short(_)) | &PatAtom(ref a @ Long(_)) => {
                    let mut bases = self.states(p, init);
                    for base in &mut bases {
                        let argv_count = self.argv.counts.get(a).map_or(0, |&x| x);
                        let max_count = base.max_counts.get(a).map_or(0, |&x| x);
                        if argv_count > max_count {
                            for _ in max_count..argv_count {
                                base.use_optional_flag(a);
                            }
                        }
                    }
                    bases
                }
                _ => {
                    let mut grouped_states = vec![self.states(p, init)];
                    loop {
                        let mut nextss = vec![];
                        for s in grouped_states.last().unwrap() {
                            nextss.extend(self.states(p, s).into_iter().filter(|snext| snext != s));
                        }
                        if nextss.is_empty() {
                            break;
                        }
                        grouped_states.push(nextss);
                    }
                    grouped_states
                        .into_iter()
                        .flat_map(std::iter::IntoIterator::into_iter)
                        .collect::<Vec<MState>>()
                }
            },
            PatAtom(ref atom) => {
                let mut state = init.clone();
                match *atom {
                    Short(_) | Long(_) => {
                        if !state.use_flag(atom) {
                            return vec![];
                        }
                    }
                    Command(_) | Positional(_) => {
                        let Some(tok) = self.token_from(init) else {
                            return vec![];
                        };
                        let Some(tok) = state.match_cmd_or_posarg(atom, tok) else {
                            return vec![];
                        };
                        if !self.add_value(&mut state, atom, &tok.atom, &tok.arg) {
                            return vec![];
                        }
                    }
                }
                vec![state]
            }
        }
    }

    #[inline]
    fn all_option_states(&self, base: &MState, states: &mut Vec<MState>, pats: &[&Pattern]) {
        if pats.is_empty() {
            states.push(base.clone());
        } else {
            let (pat, rest) = (*pats.first().unwrap(), &pats[1..]);
            for s in self.states(pat, base) {
                self.all_option_states(&s, states, rest);
            }
            // Order is important here! This must come after the loop above
            // because we prefer presence over absence. The first state wins.
            self.all_option_states(base, states, &pats[1..]);
        }
    }
}

// Tries to parse a long flag of the form '--flag[=arg]' and returns a tuple
// with the flag atom and whether there is an argument or not.
// If '=arg' exists and 'arg' isn't a valid argument, an error is returned.
fn parse_long_equal(flag: &str) -> Result<(Atom, Argument), String> {
    decl_regex! {
        LONG_EQUAL: "^(?P<name>[^=]+)=(?P<arg>.+)$";
    }
    if let Some(cap) = LONG_EQUAL.captures(flag) {
        let arg = cap_or_empty(&cap, "arg");
        if !Atom::is_arg(arg) {
            err!("Argument '{flag}' for flag '{arg}' is not in the form ARG or <arg>.")
        }
        Ok((Atom::new(cap_or_empty(&cap, "name")), One(None)))
    } else {
        Ok((Atom::new(flag), Zero))
    }
}

fn parse_long_equal_argv(flag: &str) -> (Atom, Option<String>) {
    decl_regex! {
        LONG_EQUAL: "^(?P<name>[^=]+)=(?P<arg>.*)$";
    }
    if let Some(cap) = LONG_EQUAL.captures(flag) {
        (
            Atom::new(cap_or_empty(&cap, "name")),
            Some(cap_or_empty(&cap, "arg").to_string()),
        )
    } else {
        (Atom::new(flag), None)
    }
}

// Tokenizes a usage pattern.
// Beware: regex hack ahead. Tokenizes based on whitespace separated words.
// It first normalizes `[xyz]` -> `[ xyz ]` so that delimiters are tokens.
// Similarly for `...`, `(`, `)` and `|`.
// One hitch: `--flag=<arg spaces>` is allowed, so we use a regex to pick out
// words.
fn pattern_tokens(pat: &str) -> Vec<String> {
    decl_regex! {
        NORMALIZE: r"\.\.\.|\[|\]|\(|\)|\|";
        WORDS: r"--\S+?=<[^>]+>|<[^>]+>|\S+";
    }

    let pat = NORMALIZE.replace_all(pat.trim(), " $0 ");
    WORDS
        .captures_iter(&pat)
        .map(|cap| cap[0].to_string())
        .collect()
}
```

## File: `src/synonym.rs`
```rust
use std::{
    collections::hash_map::{Iter, Keys},
    fmt::Debug,
    hash::Hash,
    mem,
};

use ahash::AHashMap;

#[derive(Clone)]
pub struct SynonymMap<K, V> {
    vals: AHashMap<K, V>,
    syns: AHashMap<K, K>,
}

impl<K: Eq + Hash, V> Default for SynonymMap<K, V> {
    fn default() -> Self {
        Self::new()
    }
}

impl<K: Eq + Hash, V> SynonymMap<K, V> {
    pub fn new() -> SynonymMap<K, V> {
        SynonymMap {
            vals: AHashMap::new(),
            syns: AHashMap::new(),
        }
    }

    #[inline]
    pub fn insert_synonym(&mut self, from: K, to: K) -> bool {
        assert!(self.vals.contains_key(&to));
        self.syns.insert(from, to).is_none()
    }

    #[inline]
    pub fn keys(&self) -> Keys<'_, K, V> {
        self.vals.keys()
    }

    #[inline]
    pub fn iter(&self) -> Iter<'_, K, V> {
        self.vals.iter()
    }

    #[inline]
    pub fn synonyms(&self) -> Iter<'_, K, K> {
        self.syns.iter()
    }

    #[inline]
    pub fn find(&self, k: &K) -> Option<&V> {
        self.with_key(k, |k| self.vals.get(k))
    }

    #[inline]
    pub fn contains_key(&self, k: &K) -> bool {
        self.with_key(k, |k| self.vals.contains_key(k))
    }

    #[inline]
    pub fn len(&self) -> usize {
        self.vals.len()
    }

    #[inline]
    fn with_key<T, F>(&self, k: &K, with: F) -> T
    where
        F: FnOnce(&K) -> T,
    {
        if self.syns.contains_key(k) {
            with(&self.syns[k])
        } else {
            with(k)
        }
    }
}

impl<K: Eq + Hash + Clone, V> SynonymMap<K, V> {
    #[inline]
    pub fn resolve(&self, k: &K) -> K {
        self.with_key(k, std::clone::Clone::clone)
    }

    #[inline]
    pub fn get<'a>(&'a self, k: &K) -> &'a V {
        self.find(k).unwrap()
    }

    #[inline]
    pub fn find_mut<'a>(&'a mut self, k: &K) -> Option<&'a mut V> {
        if self.syns.contains_key(k) {
            self.vals.get_mut(&self.syns[k])
        } else {
            self.vals.get_mut(k)
        }
    }

    #[inline]
    pub fn swap(&mut self, k: K, mut new: V) -> Option<V> {
        if self.syns.contains_key(&k) {
            let old = self.vals.get_mut(&k).unwrap();
            mem::swap(old, &mut new);
            Some(new)
        } else {
            self.vals.insert(k, new)
        }
    }

    #[inline]
    pub fn insert(&mut self, k: K, v: V) -> bool {
        self.swap(k, v).is_none()
    }
}

impl<K: Eq + Hash + Clone, V> FromIterator<(K, V)> for SynonymMap<K, V> {
    fn from_iter<T: IntoIterator<Item = (K, V)>>(iter: T) -> SynonymMap<K, V> {
        let mut map = SynonymMap::new();
        for (k, v) in iter {
            map.insert(k, v);
        }
        map
    }
}

impl<K: Eq + Hash + Debug, V: Debug> Debug for SynonymMap<K, V> {
    fn fmt(&self, f: &mut ::std::fmt::Formatter<'_>) -> ::std::fmt::Result {
        self.vals.fmt(f)?;
        write!(f, " (synomyns: {:?})", self.syns)
    }
}
```

## File: `src/utils.rs`
```rust
//! Utilities that needed a home.

/// Wrapper for lazily compiled regexes
pub struct RegexWrap(&'static str, ::std::sync::OnceLock<::regex::Regex>);

impl RegexWrap {
    /// Create a new const instances with the given regexp
    #[must_use]
    pub const fn new(re: &'static str) -> Self {
        Self(re, ::std::sync::OnceLock::<::regex::Regex>::new())
    }
}

impl ::std::ops::Deref for RegexWrap {
    type Target = ::regex::Regex;
    fn deref(&self) -> &Self::Target {
        self.1.get_or_init(|| ::regex::Regex::new(self.0).unwrap())
    }
}

/// Declares a `OnceLock` regex
macro_rules! decl_regex {
    ($($name:ident : $re:literal; )*) => {
        $(
            static $name: $crate::utils::RegexWrap = $crate::utils::RegexWrap::new($re);
        )*
    };
}

/// Print an error.
macro_rules! werr(
    ($($arg:tt)*) => ({
        use std::io::{Write, stderr};
        write!(&mut stderr(), $($arg)*).unwrap();
    })
);

/// return the value of a capture group or an empty string
#[inline]
#[must_use]
pub fn cap_or_empty<'t>(caps: &regex::Captures<'t>, name: &str) -> &'t str {
    caps.name(name).map_or("", |m| m.as_str())
}
```

## File: `src/wordlist.rs`
```rust
#[macro_use]
mod utils;
use self::utils::cap_or_empty;

#[allow(dead_code)]
mod dopt;
#[allow(dead_code)]
mod parse;
#[allow(dead_code)]
mod synonym;

use std::io::{self, Read, Write};

use ahash::AHashMap;
use regex::Regex;
use serde::Deserialize;

use crate::{
    dopt::Docopt,
    parse::{Atom, Parser},
};

const USAGE: &str = "
Usage: docopt-wordlist [(<name> <possibles>)] ...

docopt-wordlist prints a list of available flags and commands arguments for the
given usage (provided on stdin).

Example use:

  your-command --help | docopt-wordlist

This command also supports completing positional arguments when given a list of
choices. The choices are included in the word list if and only if the argument
name appears in the usage string. For example:

  your-command --help | docopt-wordlist 'arg' 'a b c'

Which will only include 'a', 'b' and 'c' in the wordlist if
'your-command --help' contains a positional argument named 'arg'.
";

#[derive(Debug, Deserialize)]
struct Args {
    arg_name:      Vec<String>,
    arg_possibles: Vec<String>,
}

fn main() {
    let args: Args = Docopt::new(USAGE)
        .and_then(|d| d.deserialize())
        .unwrap_or_else(|e| e.exit());
    match run(&args) {
        Ok(()) => {}
        Err(err) => {
            write!(&mut io::stderr(), "{err}").unwrap();
            ::std::process::exit(1)
        }
    }
}

fn run(args: &Args) -> Result<(), String> {
    let mut usage = String::new();
    io::stdin()
        .read_to_string(&mut usage)
        .map_err(|e| e.to_string())?;
    let parsed = Parser::new(&usage)?;
    let arg_possibles: AHashMap<String, Vec<String>> = args
        .arg_name
        .iter()
        .zip(args.arg_possibles.iter())
        .map(|(name, possibles)| {
            let choices = Regex::new(r"[ \t]+")
                .unwrap()
                .split(possibles)
                .map(std::string::ToString::to_string)
                .collect::<Vec<String>>();
            (name.clone(), choices)
        })
        .collect();

    let mut words = vec![];
    for k in parsed.descs.keys() {
        if let Atom::Positional(ref arg_name) = *k {
            if let Some(choices) = arg_possibles.get(arg_name) {
                words.extend(choices.iter().cloned());
            }
            // If the user hasn't given choices for this positional argument,
            // then there's really nothing to complete here.
        } else {
            words.push(k.to_string());
        }
    }
    for (k, _) in parsed.descs.synonyms() {
        // We don't need to do anything special here since synonyms can
        // only be flags, which we always include in the wordlist.
        words.push(k.to_string());
    }
    println!("{}", words.join(" "));
    Ok(())
}
```

## File: `src/test/mod.rs`
```rust
use ahash::AHashMap;
use serde::Deserialize;

use crate::{
    ArgvMap, Docopt, Error,
    Value::{self, Plain, Switch},
};

fn get_args(doc: &str, argv: &[&'static str]) -> ArgvMap {
    let dopt = match Docopt::new(doc) {
        Err(err) => panic!("Invalid usage: {}", err),
        Ok(dopt) => dopt,
    };
    match dopt.argv(vec!["cmd"].iter().chain(argv.iter())).parse() {
        Err(err) => panic!("{}", err),
        Ok(vals) => vals,
    }
}

fn map_from_alist(alist: Vec<(&'static str, Value)>) -> AHashMap<String, Value> {
    alist.into_iter().map(|(k, v)| (k.to_string(), v)).collect()
}

fn same_args(expected: &AHashMap<String, Value>, got: &ArgvMap) {
    for (k, ve) in expected.iter() {
        match got.map.find(k) {
            None => panic!("EXPECTED has '{}' but GOT does not.", k),
            Some(vg) => {
                assert!(ve == vg, "{}: EXPECTED = '{:?}' != '{:?}' = GOT", k, ve, vg)
            }
        }
    }
    for (k, vg) in got.map.iter() {
        match got.map.find(k) {
            None => panic!("GOT has '{}' but EXPECTED does not.", k),
            Some(ve) => {
                assert!(vg == ve, "{}: GOT = '{:?}' != '{:?}' = EXPECTED", k, vg, ve)
            }
        }
    }
}

macro_rules! test_expect(
    ($name:ident, $doc:expr, $args:expr, $expected:expr) => (
        #[test]
        fn $name() {
            let vals = get_args($doc, $args);
            let expected = map_from_alist($expected);
            same_args(&expected, &vals);
        }
    );
);

macro_rules! test_user_error(
    ($name:ident, $doc:expr, $args:expr) => (
        #[test]
        #[should_panic]
        fn $name() { get_args($doc, $args); }
    );
);

test_expect!(
    test_issue_13,
    "Usage: prog file <file>",
    &["file", "file"],
    vec![
        ("file", Switch(true)),
        ("<file>", Plain(Some("file".to_string())))
    ]
);

test_expect!(
    test_issue_129,
    "Usage: prog [options]

Options:
    --foo ARG   Foo foo.",
    &["--foo=a b"],
    vec![("--foo", Plain(Some("a b".into())))]
);

#[test]
fn regression_issue_12() {
    const USAGE: &str = "
    Usage:
        whisper info <file>
        whisper update <file> <timestamp> <value>
        whisper mark <file> <value>
    ";

    #[derive(Deserialize, Debug)]
    struct Args {
        arg_file:      String,
        cmd_info:      bool,
        cmd_update:    bool,
        arg_timestamp: u64,
        arg_value:     f64,
    }

    let dopt: Args = Docopt::new(USAGE)
        .unwrap()
        .argv(&["whisper", "mark", "./p/blah", "100"])
        .deserialize()
        .unwrap();
    assert_eq!(dopt.arg_timestamp, 0);
}

#[test]
fn regression_issue_195() {
    const USAGE: &str = "
    Usage:
        slow [-abcdefghijklmnopqrs...]
    ";

    let argv = &["slow", "-abcdefghijklmnopqrs"];
    let dopt: Docopt = Docopt::new(USAGE).unwrap().argv(argv);

    dopt.parse().unwrap();
}

#[test]
fn regression_issue_219() {
    #[derive(Deserialize)]
    struct Args {
        arg_type:  Vec<String>,
        arg_param: Vec<String>,
    }

    const USAGE: &str = "
    Usage:
        encode [-v <type> <param>]...
    ";

    let argv = &["encode", "-v", "bool", "true", "string", "foo"];
    let args: Args = Docopt::new(USAGE)
        .unwrap()
        .argv(argv)
        .deserialize()
        .unwrap();
    assert_eq!(args.arg_type, vec!["bool".to_owned(), "string".to_owned()]);
    assert_eq!(args.arg_param, vec!["true".to_owned(), "foo".to_owned()]);
}

#[test]
fn test_unit_struct() {
    const USAGE: &str = "
    Usage:
        cargo version [options]

    Options:
        -h, --help               Print this message
    ";

    #[derive(Deserialize)]
    struct Options;

    let argv = &["cargo", "version"];
    let dopt: Result<Options, Error> = Docopt::new(USAGE).unwrap().argv(argv).deserialize();
    assert!(dopt.is_ok());
}

#[test]
#[cfg(unix)]
fn test_non_utf8_args_lossy_conversion() {
    use std::os::unix::ffi::OsStringExt;

    const USAGE: &str = "
    Usage:
        prog <input> <output>
    ";

    #[derive(Deserialize, Debug)]
    struct Args {
        arg_input:  String,
        arg_output: String,
    }

    // Create an OsString with invalid UTF-8 bytes
    let invalid_utf8_input = std::ffi::OsString::from_vec(vec![0xFF, 0xFE, 0xFD]);
    let valid_output = std::ffi::OsString::from("output.txt");

    // Convert to strings as the library would do internally
    let input_str = invalid_utf8_input.to_string_lossy().into_owned();
    let output_str = valid_output.to_string_lossy().into_owned();

    // Verify that lossy conversion produces the replacement character
    assert!(
        input_str.contains('�'),
        "Non-UTF-8 should convert to replacement character"
    );

    // Test that the library handles these arguments without panicking
    let argv = vec!["prog", &input_str, &output_str];
    let args: Args = Docopt::new(USAGE)
        .unwrap()
        .argv(&argv)
        .deserialize()
        .unwrap();

    // The converted string will contain the Unicode replacement character
    assert_eq!(args.arg_input, input_str);
    assert_eq!(args.arg_output, "output.txt");

    // Verify the replacement character is present in the converted input
    assert!(args.arg_input.contains('�'));
}

mod suggestions;
mod testcases;
```

## File: `src/test/suggestions.rs`
```rust
use crate::{Docopt, Error};

fn get_suggestion(doc: &str, argv: &[&'static str]) -> Error {
    let dopt = match Docopt::new(doc) {
        Err(err) => panic!("Invalid usage: {}", err),
        Ok(dopt) => dopt,
    };
    let mut argv: Vec<_> = argv.iter().map(|x| x.to_string()).collect();
    argv.insert(0, "prog".to_string());
    match dopt.argv(argv.into_iter()).parse() {
        Err(err) => err,
        Ok(_) => panic!("Should have been a user error"),
    }
}

macro_rules! test_suggest(
    ($name:ident, $doc:expr, $args:expr, $expected:expr) => (
        #[test]
        fn $name() {
            let sg = get_suggestion($doc, $args);
            println!("{}", sg);
            match sg {
                Error::WithProgramUsage(e, _) => {
                    match *e {
                        Error::Argv(msg) => {
                            println!("{:?}",msg);
                            assert_eq!(msg, $expected);
                        }
                        err => panic!("Error other than argv: {:?}", err)
                    }
                },
                _ => panic!("Error without program usage")
            }
        }
    );
);

test_suggest!(
    test_suggest_1,
    "Usage: prog [--release]",
    &["--releas"],
    "Unknown flag: '--releas'. Did you mean '--release'?"
);

test_suggest!(
    test_suggest_2,
    "Usage: prog [-a] <source> <dest>
        prog [-a] <source>... <dir>
        prog [-e]
 Options:
    -a, --archive  Copy everything.
",
    &["-d"],
    "Unknown flag: '-d'"
);

test_suggest!(
    test_suggest_3,
    "Usage: prog [-a] <source> <dest>
        prog [-a] <source>... <dir>
        prog [-e]
 Options:
    -a, --archive  Copy everything.
    -e, --export Export all the things.
",
    &["--expotr"],
    "Unknown flag: '--expotr'. Did you mean '--export'?"
);

test_suggest!(
    test_suggest_4,
    "Usage: prog [--import] [--complete]
",
    &["--mport", "--complte"],
    "Unknown flag: '--mport'. Did you mean '--import'?"
);

test_suggest!(
    test_suggest_5,
    "Usage: prog [--import] [--complete]
",
    &["--import", "--complte"],
    "Unknown flag: '--complte'. Did you mean '--complete'?"
);
```

## File: `src/test/testcases.docopt`
```
r"""Usage: prog

"""
$ prog
{}

$ prog --xxx
"user-error"


r"""Usage: prog [options]

Options: -a  All.

"""
$ prog
{"-a": false}

$ prog -a
{"-a": true}

$ prog -x
"user-error"


r"""Usage: prog [options]

Options: --all  All.

"""
$ prog
{"--all": false}

$ prog --all
{"--all": true}

$ prog --xxx
"user-error"


r"""Usage: prog [options]

Options: -v, --verbose  Verbose.

"""
$ prog --verbose
{"--verbose": true}

$ prog --ver
"user-error"

$ prog -v
{"--verbose": true}


r"""Usage: prog [options]

Options: -p PATH

"""
$ prog -p home/
{"-p": "home/"}

$ prog -phome/
{"-p": "home/"}

$ prog -p
"user-error"


r"""Usage: prog [options]

Options: --path <path>

"""
$ prog --path home/
{"--path": "home/"}

$ prog --path=home/
{"--path": "home/"}

$ prog --pa home/
"user-error"

$ prog --pa=home/
"user-error"

$ prog --path
"user-error"


r"""Usage: prog [options]

Options: -p PATH, --path=<path>  Path to files.

"""
$ prog -proot
{"--path": "root"}


r"""Usage: prog [options]

Options:    -p --path PATH  Path to files.

"""
$ prog -p root
{"--path": "root"}

$ prog --path root
{"--path": "root"}


r"""Usage: prog [options]

Options:
 -p PATH  Path to files [default: ./]

"""
$ prog
{"-p": "./"}

$ prog -phome
{"-p": "home"}


r"""UsAgE: prog [options]

OpTiOnS: --path=<files>  Path to files
                [dEfAuLt: /root]

"""
$ prog
{"--path": "/root"}

$ prog --path=home
{"--path": "home"}


r"""usage: prog [options]

options:
    -a        Add
    -r        Remote
    -m <msg>  Message

"""
$ prog -a -r -m Hello
{"-a": true,
 "-r": true,
 "-m": "Hello"}

$ prog -armyourass
{"-a": true,
 "-r": true,
 "-m": "yourass"}

$ prog -a -r
{"-a": true,
 "-r": true,
 "-m": null}


r"""Usage: prog [options]

Options: --version
         --verbose

"""
$ prog --version
{"--version": true,
 "--verbose": false}

$ prog --verbose
{"--version": false,
 "--verbose": true}

$ prog --ver
"user-error"

$ prog --verb
"user-error"


r"""usage: prog [-a -r -m <msg>]

options:
 -a        Add
 -r        Remote
 -m <msg>  Message

"""
$ prog -armyourass
{"-a": true,
 "-r": true,
 "-m": "yourass"}


r"""usage: prog [-armMSG]

options: -a        Add
         -r        Remote
         -m <msg>  Message

"""
$ prog -a -r -m Hello
{"-a": true,
 "-r": true,
 "-m": "Hello"}


r"""usage: prog -a -b

options:
 -a
 -b

"""
$ prog -a -b
{"-a": true, "-b": true}

$ prog -b -a
{"-a": true, "-b": true}

$ prog -a
"user-error"

$ prog
"user-error"


r"""usage: prog (-a -b)

options: -a
         -b

"""
$ prog -a -b
{"-a": true, "-b": true}

$ prog -b -a
{"-a": true, "-b": true}

$ prog -a
"user-error"

$ prog
"user-error"


r"""usage: prog [-a] -b

options: -a
 -b

"""
$ prog -a -b
{"-a": true, "-b": true}

$ prog -b -a
{"-a": true, "-b": true}

$ prog -a
"user-error"

$ prog -b
{"-a": false, "-b": true}

$ prog
"user-error"


r"""usage: prog [(-a -b)]

options: -a
         -b

"""
$ prog -a -b
{"-a": true, "-b": true}

$ prog -b -a
{"-a": true, "-b": true}

$ prog -a
"user-error"

$ prog -b
"user-error"

$ prog
{"-a": false, "-b": false}


r"""usage: prog (-a|-b)

options: -a
         -b

"""
$ prog -a -b
"user-error"

$ prog
"user-error"

$ prog -a
{"-a": true, "-b": false}

$ prog -b
{"-a": false, "-b": true}


r"""usage: prog [ -a | -b ]

options: -a
         -b

"""
$ prog -a -b
"user-error"

$ prog
{"-a": false, "-b": false}

$ prog -a
{"-a": true, "-b": false}

$ prog -b
{"-a": false, "-b": true}


r"""usage: prog <arg>"""
$ prog 10
{"<arg>": "10"}

$ prog 10 20
"user-error"

$ prog
"user-error"


r"""usage: prog [<arg>]"""
$ prog 10
{"<arg>": "10"}

$ prog 10 20
"user-error"

$ prog
{"<arg>": null}


r"""usage: prog <kind> <name> <type>"""
$ prog 10 20 40
{"<kind>": "10", "<name>": "20", "<type>": "40"}

$ prog 10 20
"user-error"

$ prog
"user-error"


r"""usage: prog <kind> [<name> <type>]"""
$ prog 10 20 40
{"<kind>": "10", "<name>": "20", "<type>": "40"}

$ prog 10 20
{"<kind>": "10", "<name>": "20", "<type>": null}

$ prog
"user-error"


r"""usage: prog [<kind> | <name> <type>]"""
$ prog 10 20 40
"user-error"

$ prog 20 40
{"<kind>": null, "<name>": "20", "<type>": "40"}

$ prog
{"<kind>": null, "<name>": null, "<type>": null}


r"""usage: prog (<kind> --all | <name>)

options:
 --all

"""
$ prog 10 --all
{"<kind>": "10", "--all": true, "<name>": null}

$ prog 10
{"<kind>": null, "--all": false, "<name>": "10"}

$ prog
"user-error"


r"""usage: prog [<name> <name>]"""
$ prog 10 20
{"<name>": ["10", "20"]}

$ prog 10
{"<name>": ["10"]}

$ prog
{"<name>": []}


r"""usage: prog [(<name> <name>)]"""
$ prog 10 20
{"<name>": ["10", "20"]}

$ prog 10
"user-error"

$ prog
{"<name>": []}


r"""usage: prog NAME..."""
$ prog 10 20
{"NAME": ["10", "20"]}

$ prog 10
{"NAME": ["10"]}

$ prog
"user-error"


r"""usage: prog [NAME]..."""
$ prog 10 20
{"NAME": ["10", "20"]}

$ prog 10
{"NAME": ["10"]}

$ prog
{"NAME": []}


r"""usage: prog [NAME...]"""
$ prog 10 20
{"NAME": ["10", "20"]}

$ prog 10
{"NAME": ["10"]}

$ prog
{"NAME": []}


r"""usage: prog [NAME [NAME ...]]"""
$ prog 10 20
{"NAME": ["10", "20"]}

$ prog 10
{"NAME": ["10"]}

$ prog
{"NAME": []}


r"""usage: prog (NAME | --foo NAME)

options: --foo

"""
$ prog 10
{"NAME": "10", "--foo": false}

$ prog --foo 10
{"NAME": "10", "--foo": true}

$ prog --foo=10
"user-error"


r"""usage: prog (NAME | --foo) [--bar | NAME]

options: --foo
options: --bar

"""
$ prog 10
{"NAME": ["10"], "--foo": false, "--bar": false}

$ prog 10 20
{"NAME": ["10", "20"], "--foo": false, "--bar": false}

$ prog --foo --bar
{"NAME": [], "--foo": true, "--bar": true}


r"""Naval Fate.

Usage:
  prog ship new <name>...
  prog ship [<name>] move <x> <y> [--speed=<kn>]
  prog ship shoot <x> <y>
  prog mine (set|remove) <x> <y> [--moored|--drifting]
  prog -h | --help
  prog --version

Options:
  -h --help     Show this screen.
  --version     Show version.
  --speed=<kn>  Speed in knots [default: 10].
  --moored      Mored (anchored) mine.
  --drifting    Drifting mine.

"""
$ prog ship Guardian move 150 300 --speed=20
{"--drifting": false,
 "--help": false,
 "--moored": false,
 "--speed": "20",
 "--version": false,
 "<name>": ["Guardian"],
 "<x>": "150",
 "<y>": "300",
 "mine": false,
 "move": true,
 "new": false,
 "remove": false,
 "set": false,
 "ship": true,
 "shoot": false}


r"""usage: prog --hello"""
$ prog --hello
{"--hello": true}


r"""usage: prog [--hello=<world>]"""
$ prog
{"--hello": null}

$ prog --hello wrld
{"--hello": "wrld"}


r"""usage: prog [-o]"""
$ prog
{"-o": false}

$ prog -o
{"-o": true}


r"""usage: prog [-opr]"""
$ prog -op
{"-o": true, "-p": true, "-r": false}


r"""usage: prog --aabb | --aa"""
$ prog --aa
{"--aabb": false, "--aa": true}

$ prog --a
"user-error"  # not a unique prefix

#
# Counting number of flags
#

r"""Usage: prog -v"""
$ prog -v
{"-v": true}


r"""Usage: prog [-v -v]"""
$ prog
{"-v": 0}

$ prog -v
{"-v": 1}

$ prog -vv
{"-v": 2}


r"""Usage: prog -v ..."""
$ prog
"user-error"

$ prog -v
{"-v": 1}

$ prog -vv
{"-v": 2}

$ prog -vvvvvv
{"-v": 6}


r"""Usage: prog [-v | -vv | -vvv]

This one is probably most readable user-friednly variant.

"""
$ prog
{"-v": 0}

$ prog -v
{"-v": 1}

$ prog -vv
{"-v": 2}

$ prog -vvvv
"user-error"


r"""usage: prog [--ver --ver]"""
$ prog --ver --ver
{"--ver": 2}


#
# Counting commands
#

r"""usage: prog [go]"""
$ prog go
{"go": true}


r"""usage: prog [go go]"""
$ prog
{"go": 0}

$ prog go
{"go": 1}

$ prog go go
{"go": 2}

$ prog go go go
"user-error"

r"""usage: prog go..."""
$ prog go go go go go
{"go": 5}

#
# [options] does not include options from usage-pattern
#
r"""usage: prog [options] [-a]

options: -a
         -b
"""
$ prog -a
{"-a": true, "-b": false}

$ prog -aa
"user-error"

#
# Test [options] shourtcut
#

r"""Usage: prog [options] A

Options:
    -q  Be quiet
    -v  Be verbose.

"""
$ prog arg
{"A": "arg", "-v": false, "-q": false}

$ prog -v arg
{"A": "arg", "-v": true, "-q": false}

$ prog -q arg
{"A": "arg", "-v": false, "-q": true}

#
# Test single dash
#

r"""usage: prog [-]"""

$ prog -
{"-": true}

$ prog
{"-": false}

#
# If argument is repeated, its value should always be a list
#

r"""usage: prog [NAME [NAME ...]]"""

$ prog a b
{"NAME": ["a", "b"]}

$ prog
{"NAME": []}

#
# Option's argument defaults to null/None
#

r"""usage: prog [options]

options:
 -a        Add
 -m <msg>  Message

"""
$ prog -a
{"-m": null, "-a": true}

#
# Test options without description
#

r"""usage: prog --hello"""
$ prog --hello
{"--hello": true}

r"""usage: prog [--hello=<world>]"""
$ prog
{"--hello": null}

$ prog --hello wrld
{"--hello": "wrld"}

r"""usage: prog [-o]"""
$ prog
{"-o": false}

$ prog -o
{"-o": true}

r"""usage: prog [-opr]"""
$ prog -op
{"-o": true, "-p": true, "-r": false}

r"""usage: git [-v | --verbose]"""
$ prog -v
{"-v": true, "--verbose": false}

r"""usage: git remote [-v | --verbose]"""
$ prog remote -v
{"remote": true, "-v": true, "--verbose": false}

#
# Test empty usage pattern
#

r"""usage: prog"""
$ prog
{}

r"""usage: prog
           prog <a> <b>
"""
$ prog 1 2
{"<a>": "1", "<b>": "2"}

$ prog
{"<a>": null, "<b>": null}

r"""usage: prog <a> <b>
           prog
"""
$ prog
{"<a>": null, "<b>": null}

#
# Option's argument should not capture default value from usage pattern
#

r"""usage: prog [--file=<f>]"""
$ prog
{"--file": null}

r"""usage: prog [--file=<f>]

options: --file <a>

"""
$ prog
{"--file": null}

r"""Usage: prog [-a <host:port>]

Options: -a, --address <host:port>  TCP address [default: localhost:6283].

"""
$ prog
{"--address": "localhost:6283"}

#
# If option with argument could be repeated,
# its arguments should be accumulated into a list
#

r"""usage: prog --long=<arg> ..."""

$ prog --long one
{"--long": ["one"]}

$ prog --long one --long two
{"--long": ["one", "two"]}

#
# Test multiple elements repeated at once
#

r"""usage: prog (go <direction> --speed=<km/h>)..."""
$ prog  go left --speed=5  go right --speed=9
{"go": 2, "<direction>": ["left", "right"], "--speed": ["5", "9"]}

#
# Required options should work with option shortcut
#

r"""usage: prog [options] -a

options: -a

"""
$ prog -a
{"-a": true}

#
# If option could be repeated its defaults should be split into a list
#

r"""usage: prog [-o <o>]...

options: -o <o>  [default: x]

"""
$ prog -o this -o that
{"-o": ["this", "that"]}

$ prog
{"-o": ["x"]}

r"""usage: prog [-o <o>]...

options: -o <o>  [default: x y]

"""
$ prog -o this
{"-o": ["this"]}

$ prog
{"-o": ["x", "y"]}

#
# Test stacked option's argument
#

r"""usage: prog -pPATH

options: -p PATH

"""
$ prog -pHOME
{"-p": "HOME"}

#
# Issue 56: Repeated mutually exclusive args give nested lists sometimes
#

r"""Usage: foo (--xx=X|--yy=Y)..."""
$ prog --xx=1 --yy=2
{"--xx": ["1"], "--yy": ["2"]}

#
# POSIXly correct tokenization
#

r"""usage: prog [<input file>]"""
$ prog f.txt
{"<input file>": "f.txt"}

r"""usage: prog [--input=<file name>]..."""
$ prog --input a.txt --input=b.txt
{"--input": ["a.txt", "b.txt"]}

#
# Issue 85: `[options]` shourtcut with multiple subcommands
#

r"""usage: prog good [options]
           prog fail [options]

options: --loglevel=N

"""
$ prog fail --loglevel 5
{"--loglevel": "5", "fail": true, "good": false}

#
# Usage-section syntax
#

r"""usage:prog --foo"""
$ prog --foo
{"--foo": true}

r"""PROGRAM USAGE: prog --foo"""
$ prog --foo
{"--foo": true}

r"""Usage: prog --foo
           prog --bar
NOT PART OF SECTION"""
$ prog --foo
{"--foo": true, "--bar": false}

r"""Usage:
 prog --foo
 prog --bar

NOT PART OF SECTION"""
$ prog --foo
{"--foo": true, "--bar": false}

r"""Usage:
 prog --foo
 prog --bar
NOT PART OF SECTION"""
$ prog --foo
{"--foo": true, "--bar": false}

#
# Options-section syntax
#

r"""Usage: prog [options]

global options: --foo
local options: --baz
               --bar
other options:
 --egg
 --spam
-not-an-option-

"""
$ prog --bar --egg
{"--bar": true, "--egg": true, "--spam": false}

r"""Usage: prog [-a] [--] [<arg>...]"""
$ program -a
{"-a": true, "<arg>": []}

r"""Usage: prog [-a] [--] [<arg>...]"""
$ program --
{"-a": false, "<arg>": []}

r"""Usage: prog [-a] [--] [<arg>...]"""
$ program -a -- -b
{"-a": true, "<arg>": ["-b"]}

r"""Usage: prog [-a] [--] [<arg>...]"""
$ program -a -- -a
{"-a": true, "<arg>": ["-a"]}

r"""Usage: prog [-a] [--] [<arg>...]"""
$ program -- -a
{"-a": false, "<arg>": ["-a"]}

r"""Usage: prog test [options] [--] [<args>...]"""
$ program test a -- -b
{"<args>": ["a", "-b"]}

r"""Usage: prog test [options] [--] [<args>...]"""
$ program test -- -b
{"<args>": ["-b"]}

r"""Usage: prog test [options] [--] [<args>...]"""
$ program test a -b
"user-error"

r"""Usage: prog test [options] [--] [<args>...]"""
$ program test -- -b --
{"<args>": ["-b", "--"]}

r"""Usage: prog [options]

Options:
  -a ...  Foo
"""
$ program
{"-a": 0}
$ program -a
{"-a": 1}
$ program -a -a
{"-a": 2}
$ program -aa
{"-a": 2}
$ program -a -a -a
{"-a": 3}
$ program -aaa
{"-a": 3}

r"""Usage: prog [options]

Options:
  -a, --all ...  Foo
"""
$ program
{"-a": 0}
$ program -a
{"-a": 1}
$ program -a --all
{"-a": 2}
$ program -aa --all
{"-a": 3}
$ program --all
{"-a": 1}
$ program --all --all
{"-a": 2}

r"""Usage: prog [options]

Options:
  -a, --all ARG ...  Foo
"""
$ program
{"-a": []}
$ program -a 1
{"-a": ["1"]}
$ program -a 2 --all 3
{"-a": ["2", "3"]}
$ program -a4 -a5 --all 6
{"-a": ["4", "5", "6"]}
$ program --all 7
{"-a": ["7"]}
$ program --all 8 --all 9
{"-a": ["8", "9"]}

r"""Usage: prog [options]

Options:
  --all ...  Foo
"""
$ program
{"--all": 0}
$ program --all
{"--all": 1}
$ program --all --all
{"--all": 2}

r"""Usage: prog [options]

Options:
  --all=ARG ...  Foo
"""
$ program
{"--all": []}
$ program --all 1
{"--all": ["1"]}
$ program --all 2 --all 3
{"--all": ["2", "3"]}

r"""Usage: prog [options]

Options:
  --all  ...  Foo
"""
$ program --all --all
"user-error"

r"""Usage: prog [options]

Options:
  --all ARG  ...  Foo
"""
$ program --all foo --all bar
"user-error"

r"""Usage: prog --speed=ARG"""
$ program --speed 20
{"--speed": "20"}
$ program --speed=20
{"--speed": "20"}
$ program --speed=-20
{"--speed": "-20"}
$ program --speed -20
{"--speed": "-20"}

#
# Issue 187: Fails to parse a default value containing ']'
#

r"""usage: prog [--datetime=<regex>]

options: --datetime=<regex>    Regex for datetimes [default: ^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}]

"""
$ prog
{"--datetime": "^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}"}

#
# Issue 137: -x-y being seen as a positional argument
#

r"""Usage: prog [options]

Options:
  -x ARG
  -y"""
$ prog -x-y
{"-x": "-y"}
```

## File: `src/test/testcases.rs`
```rust
// !!! ATTENTION !!!
// This file is automatically generated by `scripts/mk-testcases`.
// Please do not edit this file directly!

use crate::{
    Value::{Counted, List, Plain, Switch},
    test::{get_args, map_from_alist, same_args},
};

test_expect!(test_0_testcases, "Usage: prog", &[], vec!());

test_user_error!(test_1_testcases, "Usage: prog", &["--xxx"]);

test_expect!(
    test_2_testcases,
    "Usage: prog [options]

Options: -a  All.",
    &[],
    vec!(("-a", Switch(false)))
);

test_expect!(
    test_3_testcases,
    "Usage: prog [options]

Options: -a  All.",
    &["-a"],
    vec!(("-a", Switch(true)))
);

test_user_error!(
    test_4_testcases,
    "Usage: prog [options]

Options: -a  All.",
    &["-x"]
);

test_expect!(
    test_5_testcases,
    "Usage: prog [options]

Options: --all  All.",
    &[],
    vec!(("--all", Switch(false)))
);

test_expect!(
    test_6_testcases,
    "Usage: prog [options]

Options: --all  All.",
    &["--all"],
    vec!(("--all", Switch(true)))
);

test_user_error!(
    test_7_testcases,
    "Usage: prog [options]

Options: --all  All.",
    &["--xxx"]
);

test_expect!(
    test_8_testcases,
    "Usage: prog [options]

Options: -v, --verbose  Verbose.",
    &["--verbose"],
    vec!(("--verbose", Switch(true)))
);

test_user_error!(
    test_9_testcases,
    "Usage: prog [options]

Options: -v, --verbose  Verbose.",
    &["--ver"]
);

test_expect!(
    test_10_testcases,
    "Usage: prog [options]

Options: -v, --verbose  Verbose.",
    &["-v"],
    vec!(("--verbose", Switch(true)))
);

test_expect!(
    test_11_testcases,
    "Usage: prog [options]

Options: -p PATH",
    &["-p", "home/"],
    vec!(("-p", Plain(Some("home/".to_string()))))
);

test_expect!(
    test_12_testcases,
    "Usage: prog [options]

Options: -p PATH",
    &["-phome/"],
    vec!(("-p", Plain(Some("home/".to_string()))))
);

test_user_error!(
    test_13_testcases,
    "Usage: prog [options]

Options: -p PATH",
    &["-p"]
);

test_expect!(
    test_14_testcases,
    "Usage: prog [options]

Options: --path <path>",
    &["--path", "home/"],
    vec!(("--path", Plain(Some("home/".to_string()))))
);

test_expect!(
    test_15_testcases,
    "Usage: prog [options]

Options: --path <path>",
    &["--path=home/"],
    vec!(("--path", Plain(Some("home/".to_string()))))
);

test_user_error!(
    test_16_testcases,
    "Usage: prog [options]

Options: --path <path>",
    &["--pa", "home/"]
);

test_user_error!(
    test_17_testcases,
    "Usage: prog [options]

Options: --path <path>",
    &["--pa=home/"]
);

test_user_error!(
    test_18_testcases,
    "Usage: prog [options]

Options: --path <path>",
    &["--path"]
);

test_expect!(
    test_19_testcases,
    "Usage: prog [options]

Options: -p PATH, --path=<path>  Path to files.",
    &["-proot"],
    vec!(("--path", Plain(Some("root".to_string()))))
);

test_expect!(
    test_20_testcases,
    "Usage: prog [options]

Options:    -p --path PATH  Path to files.",
    &["-p", "root"],
    vec!(("--path", Plain(Some("root".to_string()))))
);

test_expect!(
    test_21_testcases,
    "Usage: prog [options]

Options:    -p --path PATH  Path to files.",
    &["--path", "root"],
    vec!(("--path", Plain(Some("root".to_string()))))
);

test_expect!(
    test_22_testcases,
    "Usage: prog [options]

Options:
 -p PATH  Path to files [default: ./]",
    &[],
    vec!(("-p", Plain(Some("./".to_string()))))
);

test_expect!(
    test_23_testcases,
    "Usage: prog [options]

Options:
 -p PATH  Path to files [default: ./]",
    &["-phome"],
    vec!(("-p", Plain(Some("home".to_string()))))
);

test_expect!(
    test_24_testcases,
    "UsAgE: prog [options]

OpTiOnS: --path=<files>  Path to files
                [dEfAuLt: /root]",
    &[],
    vec!(("--path", Plain(Some("/root".to_string()))))
);

test_expect!(
    test_25_testcases,
    "UsAgE: prog [options]

OpTiOnS: --path=<files>  Path to files
                [dEfAuLt: /root]",
    &["--path=home"],
    vec!(("--path", Plain(Some("home".to_string()))))
);

test_expect!(
    test_26_testcases,
    "usage: prog [options]

options:
    -a        Add
    -r        Remote
    -m <msg>  Message",
    &["-a", "-r", "-m", "Hello"],
    vec!(
        ("-m", Plain(Some("Hello".to_string()))),
        ("-a", Switch(true)),
        ("-r", Switch(true))
    )
);

test_expect!(
    test_27_testcases,
    "usage: prog [options]

options:
    -a        Add
    -r        Remote
    -m <msg>  Message",
    &["-armyourass"],
    vec!(
        ("-m", Plain(Some("yourass".to_string()))),
        ("-a", Switch(true)),
        ("-r", Switch(true))
    )
);

test_expect!(
    test_28_testcases,
    "usage: prog [options]

options:
    -a        Add
    -r        Remote
    -m <msg>  Message",
    &["-a", "-r"],
    vec!(
        ("-m", Plain(None)),
        ("-a", Switch(true)),
        ("-r", Switch(true))
    )
);

test_expect!(
    test_29_testcases,
    "Usage: prog [options]

Options: --version
         --verbose",
    &["--version"],
    vec!(("--verbose", Switch(false)), ("--version", Switch(true)))
);

test_expect!(
    test_30_testcases,
    "Usage: prog [options]

Options: --version
         --verbose",
    &["--verbose"],
    vec!(("--verbose", Switch(true)), ("--version", Switch(false)))
);

test_user_error!(
    test_31_testcases,
    "Usage: prog [options]

Options: --version
         --verbose",
    &["--ver"]
);

test_user_error!(
    test_32_testcases,
    "Usage: prog [options]

Options: --version
         --verbose",
    &["--verb"]
);

test_expect!(
    test_33_testcases,
    "usage: prog [-a -r -m <msg>]

options:
 -a        Add
 -r        Remote
 -m <msg>  Message",
    &["-armyourass"],
    vec!(
        ("-m", Plain(Some("yourass".to_string()))),
        ("-a", Switch(true)),
        ("-r", Switch(true))
    )
);

test_expect!(
    test_34_testcases,
    "usage: prog [-armMSG]

options: -a        Add
         -r        Remote
         -m <msg>  Message",
    &["-a", "-r", "-m", "Hello"],
    vec!(
        ("-m", Plain(Some("Hello".to_string()))),
        ("-a", Switch(true)),
        ("-r", Switch(true))
    )
);

test_expect!(
    test_35_testcases,
    "usage: prog -a -b

options:
 -a
 -b",
    &["-a", "-b"],
    vec!(("-a", Switch(true)), ("-b", Switch(true)))
);

test_expect!(
    test_36_testcases,
    "usage: prog -a -b

options:
 -a
 -b",
    &["-b", "-a"],
    vec!(("-a", Switch(true)), ("-b", Switch(true)))
);

test_user_error!(
    test_37_testcases,
    "usage: prog -a -b

options:
 -a
 -b",
    &["-a"]
);

test_user_error!(
    test_38_testcases,
    "usage: prog -a -b

options:
 -a
 -b",
    &[]
);

test_expect!(
    test_39_testcases,
    "usage: prog (-a -b)

options: -a
         -b",
    &["-a", "-b"],
    vec!(("-a", Switch(true)), ("-b", Switch(true)))
);

test_expect!(
    test_40_testcases,
    "usage: prog (-a -b)

options: -a
         -b",
    &["-b", "-a"],
    vec!(("-a", Switch(true)), ("-b", Switch(true)))
);

test_user_error!(
    test_41_testcases,
    "usage: prog (-a -b)

options: -a
         -b",
    &["-a"]
);

test_user_error!(
    test_42_testcases,
    "usage: prog (-a -b)

options: -a
         -b",
    &[]
);

test_expect!(
    test_43_testcases,
    "usage: prog [-a] -b

options: -a
 -b",
    &["-a", "-b"],
    vec!(("-a", Switch(true)), ("-b", Switch(true)))
);

test_expect!(
    test_44_testcases,
    "usage: prog [-a] -b

options: -a
 -b",
    &["-b", "-a"],
    vec!(("-a", Switch(true)), ("-b", Switch(true)))
);

test_user_error!(
    test_45_testcases,
    "usage: prog [-a] -b

options: -a
 -b",
    &["-a"]
);

test_expect!(
    test_46_testcases,
    "usage: prog [-a] -b

options: -a
 -b",
    &["-b"],
    vec!(("-a", Switch(false)), ("-b", Switch(true)))
);

test_user_error!(
    test_47_testcases,
    "usage: prog [-a] -b

options: -a
 -b",
    &[]
);

test_expect!(
    test_48_testcases,
    "usage: prog [(-a -b)]

options: -a
         -b",
    &["-a", "-b"],
    vec!(("-a", Switch(true)), ("-b", Switch(true)))
);

test_expect!(
    test_49_testcases,
    "usage: prog [(-a -b)]

options: -a
         -b",
    &["-b", "-a"],
    vec!(("-a", Switch(true)), ("-b", Switch(true)))
);

test_user_error!(
    test_50_testcases,
    "usage: prog [(-a -b)]

options: -a
         -b",
    &["-a"]
);

test_user_error!(
    test_51_testcases,
    "usage: prog [(-a -b)]

options: -a
         -b",
    &["-b"]
);

test_expect!(
    test_52_testcases,
    "usage: prog [(-a -b)]

options: -a
         -b",
    &[],
    vec!(("-a", Switch(false)), ("-b", Switch(false)))
);

test_user_error!(
    test_53_testcases,
    "usage: prog (-a|-b)

options: -a
         -b",
    &["-a", "-b"]
);

test_user_error!(
    test_54_testcases,
    "usage: prog (-a|-b)

options: -a
         -b",
    &[]
);

test_expect!(
    test_55_testcases,
    "usage: prog (-a|-b)

options: -a
         -b",
    &["-a"],
    vec!(("-a", Switch(true)), ("-b", Switch(false)))
);

test_expect!(
    test_56_testcases,
    "usage: prog (-a|-b)

options: -a
         -b",
    &["-b"],
    vec!(("-a", Switch(false)), ("-b", Switch(true)))
);

test_user_error!(
    test_57_testcases,
    "usage: prog [ -a | -b ]

options: -a
         -b",
    &["-a", "-b"]
);

test_expect!(
    test_58_testcases,
    "usage: prog [ -a | -b ]

options: -a
         -b",
    &[],
    vec!(("-a", Switch(false)), ("-b", Switch(false)))
);

test_expect!(
    test_59_testcases,
    "usage: prog [ -a | -b ]

options: -a
         -b",
    &["-a"],
    vec!(("-a", Switch(true)), ("-b", Switch(false)))
);

test_expect!(
    test_60_testcases,
    "usage: prog [ -a | -b ]

options: -a
         -b",
    &["-b"],
    vec!(("-a", Switch(false)), ("-b", Switch(true)))
);

test_expect!(
    test_61_testcases,
    "usage: prog <arg>",
    &["10"],
    vec!(("<arg>", Plain(Some("10".to_string()))))
);

test_user_error!(test_62_testcases, "usage: prog <arg>", &["10", "20"]);

test_user_error!(test_63_testcases, "usage: prog <arg>", &[]);

test_expect!(
    test_64_testcases,
    "usage: prog [<arg>]",
    &["10"],
    vec!(("<arg>", Plain(Some("10".to_string()))))
);

test_user_error!(test_65_testcases, "usage: prog [<arg>]", &["10", "20"]);

test_expect!(
    test_66_testcases,
    "usage: prog [<arg>]",
    &[],
    vec!(("<arg>", Plain(None)))
);

test_expect!(
    test_67_testcases,
    "usage: prog <kind> <name> <type>",
    &["10", "20", "40"],
    vec!(
        ("<type>", Plain(Some("40".to_string()))),
        ("<kind>", Plain(Some("10".to_string()))),
        ("<name>", Plain(Some("20".to_string())))
    )
);

test_user_error!(
    test_68_testcases,
    "usage: prog <kind> <name> <type>",
    &["10", "20"]
);

test_user_error!(test_69_testcases, "usage: prog <kind> <name> <type>", &[]);

test_expect!(
    test_70_testcases,
    "usage: prog <kind> [<name> <type>]",
    &["10", "20", "40"],
    vec!(
        ("<type>", Plain(Some("40".to_string()))),
        ("<kind>", Plain(Some("10".to_string()))),
        ("<name>", Plain(Some("20".to_string())))
    )
);

test_expect!(
    test_71_testcases,
    "usage: prog <kind> [<name> <type>]",
    &["10", "20"],
    vec!(
        ("<type>", Plain(None)),
        ("<kind>", Plain(Some("10".to_string()))),
        ("<name>", Plain(Some("20".to_string())))
    )
);

test_user_error!(test_72_testcases, "usage: prog <kind> [<name> <type>]", &[]);

test_user_error!(
    test_73_testcases,
    "usage: prog [<kind> | <name> <type>]",
    &["10", "20", "40"]
);

test_expect!(
    test_74_testcases,
    "usage: prog [<kind> | <name> <type>]",
    &["20", "40"],
    vec!(
        ("<type>", Plain(Some("40".to_string()))),
        ("<kind>", Plain(None)),
        ("<name>", Plain(Some("20".to_string())))
    )
);

test_expect!(
    test_75_testcases,
    "usage: prog [<kind> | <name> <type>]",
    &[],
    vec!(
        ("<type>", Plain(None)),
        ("<kind>", Plain(None)),
        ("<name>", Plain(None))
    )
);

test_expect!(
    test_76_testcases,
    "usage: prog (<kind> --all | <name>)

options:
 --all",
    &["10", "--all"],
    vec!(
        ("--all", Switch(true)),
        ("<kind>", Plain(Some("10".to_string()))),
        ("<name>", Plain(None))
    )
);

test_expect!(
    test_77_testcases,
    "usage: prog (<kind> --all | <name>)

options:
 --all",
    &["10"],
    vec!(
        ("--all", Switch(false)),
        ("<kind>", Plain(None)),
        ("<name>", Plain(Some("10".to_string())))
    )
);

test_user_error!(
    test_78_testcases,
    "usage: prog (<kind> --all | <name>)

options:
 --all",
    &[]
);

test_expect!(
    test_79_testcases,
    "usage: prog [<name> <name>]",
    &["10", "20"],
    vec!(("<name>", List(vec!("10".to_string(), "20".to_string()))))
);

test_expect!(
    test_80_testcases,
    "usage: prog [<name> <name>]",
    &["10"],
    vec!(("<name>", List(vec!("10".to_string()))))
);

test_expect!(
    test_81_testcases,
    "usage: prog [<name> <name>]",
    &[],
    vec!(("<name>", List(vec!())))
);

test_expect!(
    test_82_testcases,
    "usage: prog [(<name> <name>)]",
    &["10", "20"],
    vec!(("<name>", List(vec!("10".to_string(), "20".to_string()))))
);

test_user_error!(test_83_testcases, "usage: prog [(<name> <name>)]", &["10"]);

test_expect!(
    test_84_testcases,
    "usage: prog [(<name> <name>)]",
    &[],
    vec!(("<name>", List(vec!())))
);

test_expect!(
    test_85_testcases,
    "usage: prog NAME...",
    &["10", "20"],
    vec!(("NAME", List(vec!("10".to_string(), "20".to_string()))))
);

test_expect!(
    test_86_testcases,
    "usage: prog NAME...",
    &["10"],
    vec!(("NAME", List(vec!("10".to_string()))))
);

test_user_error!(test_87_testcases, "usage: prog NAME...", &[]);

test_expect!(
    test_88_testcases,
    "usage: prog [NAME]...",
    &["10", "20"],
    vec!(("NAME", List(vec!("10".to_string(), "20".to_string()))))
);

test_expect!(
    test_89_testcases,
    "usage: prog [NAME]...",
    &["10"],
    vec!(("NAME", List(vec!("10".to_string()))))
);

test_expect!(
    test_90_testcases,
    "usage: prog [NAME]...",
    &[],
    vec!(("NAME", List(vec!())))
);

test_expect!(
    test_91_testcases,
    "usage: prog [NAME...]",
    &["10", "20"],
    vec!(("NAME", List(vec!("10".to_string(), "20".to_string()))))
);

test_expect!(
    test_92_testcases,
    "usage: prog [NAME...]",
    &["10"],
    vec!(("NAME", List(vec!("10".to_string()))))
);

test_expect!(
    test_93_testcases,
    "usage: prog [NAME...]",
    &[],
    vec!(("NAME", List(vec!())))
);

test_expect!(
    test_94_testcases,
    "usage: prog [NAME [NAME ...]]",
    &["10", "20"],
    vec!(("NAME", List(vec!("10".to_string(), "20".to_string()))))
);

test_expect!(
    test_95_testcases,
    "usage: prog [NAME [NAME ...]]",
    &["10"],
    vec!(("NAME", List(vec!("10".to_string()))))
);

test_expect!(
    test_96_testcases,
    "usage: prog [NAME [NAME ...]]",
    &[],
    vec!(("NAME", List(vec!())))
);

test_expect!(
    test_97_testcases,
    "usage: prog (NAME | --foo NAME)

options: --foo",
    &["10"],
    vec!(
        ("NAME", Plain(Some("10".to_string()))),
        ("--foo", Switch(false))
    )
);

test_expect!(
    test_98_testcases,
    "usage: prog (NAME | --foo NAME)

options: --foo",
    &["--foo", "10"],
    vec!(
        ("NAME", Plain(Some("10".to_string()))),
        ("--foo", Switch(true))
    )
);

test_user_error!(
    test_99_testcases,
    "usage: prog (NAME | --foo NAME)

options: --foo",
    &["--foo=10"]
);

test_expect!(
    test_100_testcases,
    "usage: prog (NAME | --foo) [--bar | NAME]

options: --foo
options: --bar",
    &["10"],
    vec!(
        ("--bar", Switch(false)),
        ("NAME", List(vec!("10".to_string()))),
        ("--foo", Switch(false))
    )
);

test_expect!(
    test_101_testcases,
    "usage: prog (NAME | --foo) [--bar | NAME]

options: --foo
options: --bar",
    &["10", "20"],
    vec!(
        ("--bar", Switch(false)),
        ("NAME", List(vec!("10".to_string(), "20".to_string()))),
        ("--foo", Switch(false))
    )
);

test_expect!(
    test_102_testcases,
    "usage: prog (NAME | --foo) [--bar | NAME]

options: --foo
options: --bar",
    &["--foo", "--bar"],
    vec!(
        ("--bar", Switch(true)),
        ("NAME", List(vec!())),
        ("--foo", Switch(true))
    )
);

test_expect!(
    test_103_testcases,
    "Naval Fate.

Usage:
  prog ship new <name>...
  prog ship [<name>] move <x> <y> [--speed=<kn>]
  prog ship shoot <x> <y>
  prog mine (set|remove) <x> <y> [--moored|--drifting]
  prog -h | --help
  prog --version

Options:
  -h --help     Show this screen.
  --version     Show version.
  --speed=<kn>  Speed in knots [default: 10].
  --moored      Mored (anchored) mine.
  --drifting    Drifting mine.",
    &["ship", "Guardian", "move", "150", "300", "--speed=20"],
    vec!(
        ("shoot", Switch(false)),
        ("--moored", Switch(false)),
        ("--drifting", Switch(false)),
        ("move", Switch(true)),
        ("--speed", Plain(Some("20".to_string()))),
        ("mine", Switch(false)),
        ("new", Switch(false)),
        ("--version", Switch(false)),
        ("set", Switch(false)),
        ("remove", Switch(false)),
        ("<name>", List(vec!("Guardian".to_string()))),
        ("ship", Switch(true)),
        ("<x>", Plain(Some("150".to_string()))),
        ("<y>", Plain(Some("300".to_string()))),
        ("--help", Switch(false))
    )
);

test_expect!(
    test_104_testcases,
    "usage: prog --hello",
    &["--hello"],
    vec!(("--hello", Switch(true)))
);

test_expect!(
    test_105_testcases,
    "usage: prog [--hello=<world>]",
    &[],
    vec!(("--hello", Plain(None)))
);

test_expect!(
    test_106_testcases,
    "usage: prog [--hello=<world>]",
    &["--hello", "wrld"],
    vec!(("--hello", Plain(Some("wrld".to_string()))))
);

test_expect!(
    test_107_testcases,
    "usage: prog [-o]",
    &[],
    vec!(("-o", Switch(false)))
);

test_expect!(
    test_108_testcases,
    "usage: prog [-o]",
    &["-o"],
    vec!(("-o", Switch(true)))
);

test_expect!(
    test_109_testcases,
    "usage: prog [-opr]",
    &["-op"],
    vec!(
        ("-o", Switch(true)),
        ("-p", Switch(true)),
        ("-r", Switch(false))
    )
);

test_expect!(
    test_110_testcases,
    "usage: prog --aabb | --aa",
    &["--aa"],
    vec!(("--aa", Switch(true)), ("--aabb", Switch(false)))
);

test_user_error!(test_111_testcases, "usage: prog --aabb | --aa", &["--a"]);

test_expect!(
    test_112_testcases,
    "Usage: prog -v",
    &["-v"],
    vec!(("-v", Switch(true)))
);

test_expect!(
    test_113_testcases,
    "Usage: prog [-v -v]",
    &[],
    vec!(("-v", Counted(0)))
);

test_expect!(
    test_114_testcases,
    "Usage: prog [-v -v]",
    &["-v"],
    vec!(("-v", Counted(1)))
);

test_expect!(
    test_115_testcases,
    "Usage: prog [-v -v]",
    &["-vv"],
    vec!(("-v", Counted(2)))
);

test_user_error!(test_116_testcases, "Usage: prog -v ...", &[]);

test_expect!(
    test_117_testcases,
    "Usage: prog -v ...",
    &["-v"],
    vec!(("-v", Counted(1)))
);

test_expect!(
    test_118_testcases,
    "Usage: prog -v ...",
    &["-vv"],
    vec!(("-v", Counted(2)))
);

test_expect!(
    test_119_testcases,
    "Usage: prog -v ...",
    &["-vvvvvv"],
    vec!(("-v", Counted(6)))
);

test_expect!(
    test_120_testcases,
    "Usage: prog [-v | -vv | -vvv]

This one is probably most readable user-friednly variant.",
    &[],
    vec!(("-v", Counted(0)))
);

test_expect!(
    test_121_testcases,
    "Usage: prog [-v | -vv | -vvv]

This one is probably most readable user-friednly variant.",
    &["-v"],
    vec!(("-v", Counted(1)))
);

test_expect!(
    test_122_testcases,
    "Usage: prog [-v | -vv | -vvv]

This one is probably most readable user-friednly variant.",
    &["-vv"],
    vec!(("-v", Counted(2)))
);

test_user_error!(
    test_123_testcases,
    "Usage: prog [-v | -vv | -vvv]

This one is probably most readable user-friednly variant.",
    &["-vvvv"]
);

test_expect!(
    test_124_testcases,
    "usage: prog [--ver --ver]",
    &["--ver", "--ver"],
    vec!(("--ver", Counted(2)))
);

test_expect!(
    test_125_testcases,
    "usage: prog [go]",
    &["go"],
    vec!(("go", Switch(true)))
);

test_expect!(
    test_126_testcases,
    "usage: prog [go go]",
    &[],
    vec!(("go", Counted(0)))
);

test_expect!(
    test_127_testcases,
    "usage: prog [go go]",
    &["go"],
    vec!(("go", Counted(1)))
);

test_expect!(
    test_128_testcases,
    "usage: prog [go go]",
    &["go", "go"],
    vec!(("go", Counted(2)))
);

test_user_error!(
    test_129_testcases,
    "usage: prog [go go]",
    &["go", "go", "go"]
);

test_expect!(
    test_130_testcases,
    "usage: prog go...",
    &["go", "go", "go", "go", "go"],
    vec!(("go", Counted(5)))
);

test_expect!(
    test_131_testcases,
    "usage: prog [options] [-a]

options: -a
         -b",
    &["-a"],
    vec!(("-a", Switch(true)), ("-b", Switch(false)))
);

test_user_error!(
    test_132_testcases,
    "usage: prog [options] [-a]

options: -a
         -b",
    &["-aa"]
);

test_expect!(
    test_133_testcases,
    "Usage: prog [options] A

Options:
    -q  Be quiet
    -v  Be verbose.",
    &["arg"],
    vec!(
        ("A", Plain(Some("arg".to_string()))),
        ("-v", Switch(false)),
        ("-q", Switch(false))
    )
);

test_expect!(
    test_134_testcases,
    "Usage: prog [options] A

Options:
    -q  Be quiet
    -v  Be verbose.",
    &["-v", "arg"],
    vec!(
        ("A", Plain(Some("arg".to_string()))),
        ("-v", Switch(true)),
        ("-q", Switch(false))
    )
);

test_expect!(
    test_135_testcases,
    "Usage: prog [options] A

Options:
    -q  Be quiet
    -v  Be verbose.",
    &["-q", "arg"],
    vec!(
        ("A", Plain(Some("arg".to_string()))),
        ("-v", Switch(false)),
        ("-q", Switch(true))
    )
);

test_expect!(
    test_136_testcases,
    "usage: prog [-]",
    &["-"],
    vec!(("-", Switch(true)))
);

test_expect!(
    test_137_testcases,
    "usage: prog [-]",
    &[],
    vec!(("-", Switch(false)))
);

test_expect!(
    test_138_testcases,
    "usage: prog [NAME [NAME ...]]",
    &["a", "b"],
    vec!(("NAME", List(vec!("a".to_string(), "b".to_string()))))
);

test_expect!(
    test_139_testcases,
    "usage: prog [NAME [NAME ...]]",
    &[],
    vec!(("NAME", List(vec!())))
);

test_expect!(
    test_140_testcases,
    "usage: prog [options]

options:
 -a        Add
 -m <msg>  Message",
    &["-a"],
    vec!(("-m", Plain(None)), ("-a", Switch(true)))
);

test_expect!(
    test_141_testcases,
    "usage: prog --hello",
    &["--hello"],
    vec!(("--hello", Switch(true)))
);

test_expect!(
    test_142_testcases,
    "usage: prog [--hello=<world>]",
    &[],
    vec!(("--hello", Plain(None)))
);

test_expect!(
    test_143_testcases,
    "usage: prog [--hello=<world>]",
    &["--hello", "wrld"],
    vec!(("--hello", Plain(Some("wrld".to_string()))))
);

test_expect!(
    test_144_testcases,
    "usage: prog [-o]",
    &[],
    vec!(("-o", Switch(false)))
);

test_expect!(
    test_145_testcases,
    "usage: prog [-o]",
    &["-o"],
    vec!(("-o", Switch(true)))
);

test_expect!(
    test_146_testcases,
    "usage: prog [-opr]",
    &["-op"],
    vec!(
        ("-o", Switch(true)),
        ("-p", Switch(true)),
        ("-r", Switch(false))
    )
);

test_expect!(
    test_147_testcases,
    "usage: git [-v | --verbose]",
    &["-v"],
    vec!(("-v", Switch(true)), ("--verbose", Switch(false)))
);

test_expect!(
    test_148_testcases,
    "usage: git remote [-v | --verbose]",
    &["remote", "-v"],
    vec!(
        ("-v", Switch(true)),
        ("remote", Switch(true)),
        ("--verbose", Switch(false))
    )
);

test_expect!(test_149_testcases, "usage: prog", &[], vec!());

test_expect!(
    test_150_testcases,
    "usage: prog
           prog <a> <b>",
    &["1", "2"],
    vec!(
        ("<a>", Plain(Some("1".to_string()))),
        ("<b>", Plain(Some("2".to_string())))
    )
);

test_expect!(
    test_151_testcases,
    "usage: prog
           prog <a> <b>",
    &[],
    vec!(("<a>", Plain(None)), ("<b>", Plain(None)))
);

test_expect!(
    test_152_testcases,
    "usage: prog <a> <b>
           prog",
    &[],
    vec!(("<a>", Plain(None)), ("<b>", Plain(None)))
);

test_expect!(
    test_153_testcases,
    "usage: prog [--file=<f>]",
    &[],
    vec!(("--file", Plain(None)))
);

test_expect!(
    test_154_testcases,
    "usage: prog [--file=<f>]

options: --file <a>",
    &[],
    vec!(("--file", Plain(None)))
);

test_expect!(
    test_155_testcases,
    "Usage: prog [-a <host:port>]

Options: -a, --address <host:port>  TCP address [default: localhost:6283].",
    &[],
    vec!(("--address", Plain(Some("localhost:6283".to_string()))))
);

test_expect!(
    test_156_testcases,
    "usage: prog --long=<arg> ...",
    &["--long", "one"],
    vec!(("--long", List(vec!("one".to_string()))))
);

test_expect!(
    test_157_testcases,
    "usage: prog --long=<arg> ...",
    &["--long", "one", "--long", "two"],
    vec!(("--long", List(vec!("one".to_string(), "two".to_string()))))
);

test_expect!(
    test_158_testcases,
    "usage: prog (go <direction> --speed=<km/h>)...",
    &["go", "left", "--speed=5", "go", "right", "--speed=9"],
    vec!(
        ("go", Counted(2)),
        (
            "<direction>",
            List(vec!("left".to_string(), "right".to_string()))
        ),
        ("--speed", List(vec!("5".to_string(), "9".to_string())))
    )
);

test_expect!(
    test_159_testcases,
    "usage: prog [options] -a

options: -a",
    &["-a"],
    vec!(("-a", Switch(true)))
);

test_expect!(
    test_160_testcases,
    "usage: prog [-o <o>]...

options: -o <o>  [default: x]",
    &["-o", "this", "-o", "that"],
    vec!(("-o", List(vec!("this".to_string(), "that".to_string()))))
);

test_expect!(
    test_161_testcases,
    "usage: prog [-o <o>]...

options: -o <o>  [default: x]",
    &[],
    vec!(("-o", List(vec!("x".to_string()))))
);

test_expect!(
    test_162_testcases,
    "usage: prog [-o <o>]...

options: -o <o>  [default: x y]",
    &["-o", "this"],
    vec!(("-o", List(vec!("this".to_string()))))
);

test_expect!(
    test_163_testcases,
    "usage: prog [-o <o>]...

options: -o <o>  [default: x y]",
    &[],
    vec!(("-o", List(vec!("x".to_string(), "y".to_string()))))
);

test_expect!(
    test_164_testcases,
    "usage: prog -pPATH

options: -p PATH",
    &["-pHOME"],
    vec!(("-p", Plain(Some("HOME".to_string()))))
);

test_expect!(
    test_165_testcases,
    "Usage: foo (--xx=X|--yy=Y)...",
    &["--xx=1", "--yy=2"],
    vec!(
        ("--yy", List(vec!("2".to_string()))),
        ("--xx", List(vec!("1".to_string())))
    )
);

test_expect!(
    test_166_testcases,
    "usage: prog [<input file>]",
    &["f.txt"],
    vec!(("<input file>", Plain(Some("f.txt".to_string()))))
);

test_expect!(
    test_167_testcases,
    "usage: prog [--input=<file name>]...",
    &["--input", "a.txt", "--input=b.txt"],
    vec!((
        "--input",
        List(vec!("a.txt".to_string(), "b.txt".to_string()))
    ))
);

test_expect!(
    test_168_testcases,
    "usage: prog good [options]
           prog fail [options]

options: --loglevel=N",
    &["fail", "--loglevel", "5"],
    vec!(
        ("fail", Switch(true)),
        ("good", Switch(false)),
        ("--loglevel", Plain(Some("5".to_string())))
    )
);

test_expect!(
    test_169_testcases,
    "usage:prog --foo",
    &["--foo"],
    vec!(("--foo", Switch(true)))
);

test_expect!(
    test_170_testcases,
    "PROGRAM USAGE: prog --foo",
    &["--foo"],
    vec!(("--foo", Switch(true)))
);

test_expect!(
    test_171_testcases,
    "Usage: prog --foo
           prog --bar
NOT PART OF SECTION",
    &["--foo"],
    vec!(("--bar", Switch(false)), ("--foo", Switch(true)))
);

test_expect!(
    test_172_testcases,
    "Usage:
 prog --foo
 prog --bar

NOT PART OF SECTION",
    &["--foo"],
    vec!(("--bar", Switch(false)), ("--foo", Switch(true)))
);

test_expect!(
    test_173_testcases,
    "Usage:
 prog --foo
 prog --bar
NOT PART OF SECTION",
    &["--foo"],
    vec!(("--bar", Switch(false)), ("--foo", Switch(true)))
);

test_expect!(
    test_174_testcases,
    "Usage: prog [options]

global options: --foo
local options: --baz
               --bar
other options:
 --egg
 --spam
-not-an-option-",
    &["--bar", "--egg"],
    vec!(
        ("--bar", Switch(true)),
        ("--egg", Switch(true)),
        ("--spam", Switch(false))
    )
);

test_expect!(
    test_175_testcases,
    "Usage: prog [-a] [--] [<arg>...]",
    &["-a"],
    vec!(("<arg>", List(vec!())), ("-a", Switch(true)))
);

test_expect!(
    test_176_testcases,
    "Usage: prog [-a] [--] [<arg>...]",
    &["--"],
    vec!(("<arg>", List(vec!())), ("-a", Switch(false)))
);

test_expect!(
    test_177_testcases,
    "Usage: prog [-a] [--] [<arg>...]",
    &["-a", "--", "-b"],
    vec!(
        ("<arg>", List(vec!("-b".to_string()))),
        ("-a", Switch(true))
    )
);

test_expect!(
    test_178_testcases,
    "Usage: prog [-a] [--] [<arg>...]",
    &["-a", "--", "-a"],
    vec!(
        ("<arg>", List(vec!("-a".to_string()))),
        ("-a", Switch(true))
    )
);

test_expect!(
    test_179_testcases,
    "Usage: prog [-a] [--] [<arg>...]",
    &["--", "-a"],
    vec!(
        ("<arg>", List(vec!("-a".to_string()))),
        ("-a", Switch(false))
    )
);

test_expect!(
    test_180_testcases,
    "Usage: prog test [options] [--] [<args>...]",
    &["test", "a", "--", "-b"],
    vec!(("<args>", List(vec!("a".to_string(), "-b".to_string()))))
);

test_expect!(
    test_181_testcases,
    "Usage: prog test [options] [--] [<args>...]",
    &["test", "--", "-b"],
    vec!(("<args>", List(vec!("-b".to_string()))))
);

test_user_error!(
    test_182_testcases,
    "Usage: prog test [options] [--] [<args>...]",
    &["test", "a", "-b"]
);

test_expect!(
    test_183_testcases,
    "Usage: prog test [options] [--] [<args>...]",
    &["test", "--", "-b", "--"],
    vec!(("<args>", List(vec!("-b".to_string(), "--".to_string()))))
);

test_expect!(
    test_184_testcases,
    "Usage: prog [options]

Options:
  -a ...  Foo",
    &[],
    vec!(("-a", Counted(0)))
);

test_expect!(
    test_185_testcases,
    "Usage: prog [options]

Options:
  -a ...  Foo",
    &["-a"],
    vec!(("-a", Counted(1)))
);

test_expect!(
    test_186_testcases,
    "Usage: prog [options]

Options:
  -a ...  Foo",
    &["-a", "-a"],
    vec!(("-a", Counted(2)))
);

test_expect!(
    test_187_testcases,
    "Usage: prog [options]

Options:
  -a ...  Foo",
    &["-aa"],
    vec!(("-a", Counted(2)))
);

test_expect!(
    test_188_testcases,
    "Usage: prog [options]

Options:
  -a ...  Foo",
    &["-a", "-a", "-a"],
    vec!(("-a", Counted(3)))
);

test_expect!(
    test_189_testcases,
    "Usage: prog [options]

Options:
  -a ...  Foo",
    &["-aaa"],
    vec!(("-a", Counted(3)))
);

test_expect!(
    test_190_testcases,
    "Usage: prog [options]

Options:
  -a, --all ...  Foo",
    &[],
    vec!(("-a", Counted(0)))
);

test_expect!(
    test_191_testcases,
    "Usage: prog [options]

Options:
  -a, --all ...  Foo",
    &["-a"],
    vec!(("-a", Counted(1)))
);

test_expect!(
    test_192_testcases,
    "Usage: prog [options]

Options:
  -a, --all ...  Foo",
    &["-a", "--all"],
    vec!(("-a", Counted(2)))
);

test_expect!(
    test_193_testcases,
    "Usage: prog [options]

Options:
  -a, --all ...  Foo",
    &["-aa", "--all"],
    vec!(("-a", Counted(3)))
);

test_expect!(
    test_194_testcases,
    "Usage: prog [options]

Options:
  -a, --all ...  Foo",
    &["--all"],
    vec!(("-a", Counted(1)))
);

test_expect!(
    test_195_testcases,
    "Usage: prog [options]

Options:
  -a, --all ...  Foo",
    &["--all", "--all"],
    vec!(("-a", Counted(2)))
);

test_expect!(
    test_196_testcases,
    "Usage: prog [options]

Options:
  -a, --all ARG ...  Foo",
    &[],
    vec!(("-a", List(vec!())))
);

test_expect!(
    test_197_testcases,
    "Usage: prog [options]

Options:
  -a, --all ARG ...  Foo",
    &["-a", "1"],
    vec!(("-a", List(vec!("1".to_string()))))
);

test_expect!(
    test_198_testcases,
    "Usage: prog [options]

Options:
  -a, --all ARG ...  Foo",
    &["-a", "2", "--all", "3"],
    vec!(("-a", List(vec!("2".to_string(), "3".to_string()))))
);

test_expect!(
    test_199_testcases,
    "Usage: prog [options]

Options:
  -a, --all ARG ...  Foo",
    &["-a4", "-a5", "--all", "6"],
    vec!((
        "-a",
        List(vec!("4".to_string(), "5".to_string(), "6".to_string()))
    ))
);

test_expect!(
    test_200_testcases,
    "Usage: prog [options]

Options:
  -a, --all ARG ...  Foo",
    &["--all", "7"],
    vec!(("-a", List(vec!("7".to_string()))))
);

test_expect!(
    test_201_testcases,
    "Usage: prog [options]

Options:
  -a, --all ARG ...  Foo",
    &["--all", "8", "--all", "9"],
    vec!(("-a", List(vec!("8".to_string(), "9".to_string()))))
);

test_expect!(
    test_202_testcases,
    "Usage: prog [options]

Options:
  --all ...  Foo",
    &[],
    vec!(("--all", Counted(0)))
);

test_expect!(
    test_203_testcases,
    "Usage: prog [options]

Options:
  --all ...  Foo",
    &["--all"],
    vec!(("--all", Counted(1)))
);

test_expect!(
    test_204_testcases,
    "Usage: prog [options]

Options:
  --all ...  Foo",
    &["--all", "--all"],
    vec!(("--all", Counted(2)))
);

test_expect!(
    test_205_testcases,
    "Usage: prog [options]

Options:
  --all=ARG ...  Foo",
    &[],
    vec!(("--all", List(vec!())))
);

test_expect!(
    test_206_testcases,
    "Usage: prog [options]

Options:
  --all=ARG ...  Foo",
    &["--all", "1"],
    vec!(("--all", List(vec!("1".to_string()))))
);

test_expect!(
    test_207_testcases,
    "Usage: prog [options]

Options:
  --all=ARG ...  Foo",
    &["--all", "2", "--all", "3"],
    vec!(("--all", List(vec!("2".to_string(), "3".to_string()))))
);

test_user_error!(
    test_208_testcases,
    "Usage: prog [options]

Options:
  --all  ...  Foo",
    &["--all", "--all"]
);

test_user_error!(
    test_209_testcases,
    "Usage: prog [options]

Options:
  --all ARG  ...  Foo",
    &["--all", "foo", "--all", "bar"]
);

test_expect!(
    test_210_testcases,
    "Usage: prog --speed=ARG",
    &["--speed", "20"],
    vec!(("--speed", Plain(Some("20".to_string()))))
);

test_expect!(
    test_211_testcases,
    "Usage: prog --speed=ARG",
    &["--speed=20"],
    vec!(("--speed", Plain(Some("20".to_string()))))
);

test_expect!(
    test_212_testcases,
    "Usage: prog --speed=ARG",
    &["--speed=-20"],
    vec!(("--speed", Plain(Some("-20".to_string()))))
);

test_expect!(
    test_213_testcases,
    "Usage: prog --speed=ARG",
    &["--speed", "-20"],
    vec!(("--speed", Plain(Some("-20".to_string()))))
);

test_expect!(
    test_214_testcases,
    "usage: prog [--datetime=<regex>]

options: --datetime=<regex>    Regex for datetimes [default: \
     ^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}]",
    &[],
    vec!((
        "--datetime",
        Plain(Some(
            "^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}".to_string()
        ))
    ))
);

test_expect!(
    test_215_testcases,
    "Usage: prog [options]

Options:
  -x ARG
  -y",
    &["-x-y"],
    vec!(("-x", Plain(Some("-y".to_string()))))
);
```

