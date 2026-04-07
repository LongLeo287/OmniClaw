---
id: docopt.rs
type: knowledge
owner: OA_Triage
---
# docopt.rs
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
# THIS CRATE IS UNMAINTAINED

This crate is unlikely to see significant future evolution. The primary reason
to choose this crate for a new project is if you're specifically interested in
using [docopt](http://docopt.org/) syntax for your project. However, the wider
docopt project is mostly unmaintained at this point.

Consider using [clap](http://docs.rs/clap/) or possibly
[structopt](http://docs.rs/structopt/) instead.

Note that this crate has some significant bugs. The two biggest ones are the
lack of `OsStr` support and some severe performance problems in not-uncommon
edge cases.

docopt
======

Docopt for Rust with automatic type based decoding (i.e., data validation).
This implementation conforms to the
[official description of Docopt](http://docopt.org/) and
[passes its test suite](https://github.com/docopt/docopt/pull/201).

[![Build status](https://api.travis-ci.org/docopt/docopt.rs.svg)](https://travis-ci.org/docopt/docopt.rs)
[![](http://meritbadge.herokuapp.com/docopt)](https://crates.io/crates/docopt)

Dual-licensed under MIT or the [UNLICENSE](http://unlicense.org).


### Documentation

https://docs.rs/docopt


### Installation

This crate is fully compatible with Cargo. Just add it to your `Cargo.toml`:

```toml
[dependencies]
docopt = "1"
serde = { version = "1", features = ["derive"] }
```


### Quick example

Here is a full working example. Notice that you can specify the types of each
of the named values in the Docopt usage string. Values will be automatically
converted to those types (or an error will be reported).

```rust
use docopt::Docopt;
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


### Struct field name mapping

The field names of the struct map like this:

```
-g            => flag_g
--group       => flag_group
--group <arg> => flag_group
FILE          => arg_FILE
<file>        => arg_file
build         => cmd_build
```


### Traditional Docopt API

The reference implementation of Docopt returns a Python dictionary with names
like `<arg>` or `--flag`. If you prefer this access pattern, then you can use
`docopt::ArgvMap`. The disadvantage is that you have to do all of your type
conversion manually. Here's the canonical Docopt example with a hash table:

```rust
use docopt::Docopt;

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

### Tab completion support

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

### File: examples\cargo.rs
```rs
use docopt::Docopt;
use serde::Deserialize;

// Write the Docopt usage string.
const USAGE: &'static str = "
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
    arg_command: Option<Command>,
    arg_args: Vec<String>,
    flag_list: bool,
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

### File: examples\cp.rs
```rs
use docopt::Docopt;
use serde::Deserialize;

// Write the Docopt usage string.
const USAGE: &'static str = "
Usage: cp [-a] <source> <dest>
       cp [-a] <source>... <dir>

Options:
    -a, --archive  Copy everything.
";

#[derive(Debug, Deserialize)]
struct Args {
    arg_source: Vec<String>,
    arg_dest: String,
    arg_dir: String,
    flag_archive: bool,
}

fn main() {
    let args: Args = Docopt::new(USAGE)
        .and_then(|d| d.deserialize())
        .unwrap_or_else(|e| e.exit());
    println!("{:?}", args);
}

```

### File: examples\decode.rs
```rs
use docopt::Docopt;
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
    arg_x: Option<isize>,
    arg_y: Option<isize>,
    cmd_ship: bool,
    cmd_mine: bool,
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

### File: examples\hashmap.rs
```rs
use docopt::Docopt;

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

### File: examples\optional_command.rs
```rs
// This example shows how to implement a command with a "catch all."
//
// This requires writing your own impl for `Decodable` because docopt's
// decoder uses `Option<T>` to mean "T may not be present" rather than
// "T may be present but incorrect."

use std::fmt;

use docopt::Docopt;
use serde::{Deserialize, de::{Deserializer, Error, Visitor}};

// Write the Docopt usage string.
const USAGE: &'static str = "
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
        where E: Error
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
        where D: Deserializer<'de>
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

### File: examples\verbose_multiple.rs
```rs
use docopt::Docopt;
use serde::Deserialize;

// This shows how to implement multiple levels of verbosity.
//
// When you have multiple patterns, I think the only way to carry the
// repeated flag through all of them is to specify it for each pattern
// explicitly.
//
// This is unfortunate.
const USAGE: &'static str = "
Usage: cp [options] [-v | -vv | -vvv] <source> <dest>
       cp [options] [-v | -vv | -vvv] <source>... <dir>

Options:
    -a, --archive  Copy everything.
    -v, --verbose  Show extra log output.
";

#[derive(Debug, Deserialize)]
struct Args {
    arg_source: Vec<String>,
    arg_dest: String,
    arg_dir: String,
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

### File: src\dopt.rs
```rs
use std::collections::HashMap;
use std::error::Error as StdError;
use std::fmt::{self, Debug};
use std::io::{self, Write};
use std::str::FromStr;
use std::result;

use lazy_static::lazy_static;
use regex::{Captures, Regex};
use serde::de;
use serde::de::IntoDeserializer;

use crate::parse::Parser;
use crate::synonym::SynonymMap;

use self::Value::{Switch, Counted, Plain, List};
use self::Error::{Usage, Argv, NoMatch, Deserialize, WithProgramUsage, Help, Version};

use crate::cap_or_empty;

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
/// use docopt::Docopt;
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
            let _ = writeln!(&mut io::stdout(), "{}", self);
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
                    write!(f, "{}", usage)
                } else {
                    write!(f, "{}\n\n{}", other, usage)
                }
            }
            Help => write!(f, ""),
            NoMatch => write!(f, "Invalid arguments."),
            Usage(ref s) |
            Argv(ref s) |
            Deserialize(ref s) |
            Version(ref s) => write!(f, "{}", s),
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
    p: Parser,
    argv: Option<Vec<String>>,
    options_first: bool,
    help: bool,
    version: Option<String>,
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
            where S: ::std::ops::Deref<Target=str> {
        Parser::new(usage.deref())
               .map_err(Usage)
               .map(|p| Docopt {
                   p: p,
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
        where D: de::Deserialize<'de>
    {
        self.parse().and_then(|vals| vals.deserialize())
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
        let vals =
            self.p.parse_argv(argv, self.options_first)
                .map_err(|s| self.err_with_usage(Argv(s)))
                .and_then(|argv|
                    match self.p.matches(&argv) {
                        Some(m) => Ok(ArgvMap { map: m }),
                        None => Err(self.err_with_usage(NoMatch)),
                    })?;
        if self.help && vals.get_bool("--help") {
            return Err(self.err_with_full_doc(Help));
        }
        match self.version {
            Some(ref v) if vals.get_bool("--version") => {
                return Err(Version(v.clone()))
            }
            _ => {},
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
               where I: IntoIterator<Item=S>, S: AsRef<str> {
        self.argv = Some(
            argv.into_iter().skip(1).map(|s| s.as_ref().to_owned()).collect()
        );
        self
    }

    /// Enables the "options first" Docopt behavior.
    ///
    /// The options first behavior means that all flags *must* appear before
    /// position arguments. That is, after the first position argument is
    /// seen, all proceeding arguments are interpreted as positional
    /// arguments unconditionally.
    pub fn options_first(mut self, yes: bool) -> Docopt {
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
    pub fn help(mut self, yes: bool) -> Docopt {
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
    pub fn version(mut self, version: Option<String>) -> Docopt {
        self.version = version;
        self
    }

    #[doc(hidden)]
    pub fn parser(&self) -> &Parser {
        &self.p
    }

    fn err_with_usage(&self, e: Error) -> Error {
        WithProgramUsage(
            Box::new(e), self.p.usage.trim().into())
    }

    fn err_with_full_doc(&self, e: Error) -> Error {
        WithProgramUsage(
            Box::new(e), self.p.full_doc.trim().into())
    }

    fn get_argv() -> Vec<String> {
        // Hmm, we should probably handle a Unicode decode error here... ---AG
        ::std::env::args().skip(1).collect()
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
    /// use docopt::Docopt;
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
                                              vals: self,
                                              stack: vec![],
                                          })
    }

    /// Finds the value corresponding to `key` and calls `as_bool()` on it.
    /// If the key does not exist, `false` is returned.
    pub fn get_bool(&self, key: &str) -> bool {
        self.find(key).map_or(false, |v| v.as_bool())
    }

    /// Finds the value corresponding to `key` and calls `as_count()` on it.
    /// If the key does not exist, `0` is returned.
    pub fn get_count(&self, key: &str) -> u64 {
        self.find(key).map_or(0, |v| v.as_count())
    }

    /// Finds the value corresponding to `key` and calls `as_str()` on it.
    /// If the key does not exist, `""` is returned.
    pub fn get_str(&self, key: &str) -> &str {
        self.find(key).map_or("", |v| v.as_str())
    }

    /// Finds the value corresponding to `key` and calls `as_vec()` on it.
    /// If the key does not exist, `vec!()` is returned.
    pub fn get_vec(&self, key: &str) -> Vec<&str> {
        self.find(key).map(|v| v.as_vec()).unwrap_or(vec!())
    }

    /// Return the raw value corresponding to some `key`.
    ///
    /// `key` should be a string in the traditional Docopt format. e.g.,
    /// `<arg>` or `--flag`.
    pub fn find(&self, key: &str) -> Option<&Value> {
        self.map.find(&key.into())
    }

    /// Return the number of values, not including synonyms.
    pub fn len(&self) -> usize {
        self.map.len()
    }

    /// Converts a Docopt key to a struct field name.
    /// This makes a half-hearted attempt at making the key a valid struct
    /// field name (like replacing `-` with `_`), but it does not otherwise
    /// guarantee that the result is a valid struct field name.
    #[doc(hidden)]
    pub fn key_to_struct_field(name: &str) -> String {
        lazy_static! {
            static ref RE: Regex = rege
... [TRUNCATED]
```

### File: src\lib.rs
```rs
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
//! use docopt::Docopt;
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
//! ```rust
//! # fn main() {
//! use docopt::Docopt;
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
//! use docopt::Docopt;
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

#![crate_name = "docopt"]
#![doc(html_root_url = "http://burntsushi.net/rustdoc/docopt")]
#![deny(missing_docs)]

pub use crate::dopt::{ArgvMap, Deserializer, Docopt, Error, Value};

macro_rules! werr(
    ($($arg:tt)*) => ({
        use std::io::{Write, stderr};
        write!(&mut stderr(), $($arg)*).unwrap();
    })
);

macro_rules! regex(
    ($s:expr) => (regex::Regex::new($s).unwrap());
);

fn cap_or_empty<'t>(caps: &regex::Captures<'t>, name: &str) -> &'t str {
    caps.name(name).map_or("", |m| m.as_str())
}

mod dopt;
#[doc(hidden)]
pub mod parse;
mod synonym;
#[cfg(test)]
mod test;

```

### File: src\parse.rs
```rs
// I am overall pretty displeased with the quality of code in this module.
// I wrote it while simultaneously trying to build a mental model of Docopt's
// specification (hint: one does not exist in written form). As a result, there
// is a lot of coupling and some duplication.
//
// Some things that I think are good about the following code:
//
//   - The representation of a "usage pattern." I think it is a minimal
//     representation of a pattern's syntax. (One possible tweak:
//     `Optional<Vec<Pattern>>` -> `Optional<Box<Pattern>>`.)
//   - Some disciplined use of regexes. I use a pretty basic state machine
//     for parsing patterns, but for teasing out the patterns and options
//     from the Docopt string and for picking out flags with arguments, I
//     think regexes aren't too bad. There may be one or two scary ones though.
//   - The core matching algorithm is reasonably simple and concise, but I
//     think writing down some contracts will help me figure out how to make
//     the code clearer.
//
// Some bad things:
//
//   - I tried several times to split some of the pieces in this module into
//     separate modules. I could find no clear separation. This suggests that
//     there is too much coupling between parsing components. I'm not convinced
//     that the coupling is necessary.
//   - The parsers for patterns and argv share some structure. There may be
//     an easy abstraction waiting there.
//   - It is not efficient in the slightest. I tried to be conservative with
//     copying strings, but I think I failed. (It may not be worthwhile to fix
//     this if it makes the code more awkward. Docopt does not need to be
//     efficient.)
//
// Some things to do immediately:
//
//   - Document representation and invariants.
//   - Less important: write contracts for functions.
//
// Long term:
//
//   - Write a specification for Docopt.

use std::borrow::ToOwned;
use std::collections::{HashMap, HashSet};
use std::collections::hash_map::Entry::{Vacant, Occupied};
use std::cmp::Ordering;
use std::fmt;

use lazy_static::lazy_static;
use regex;
use regex::Regex;
use strsim::levenshtein;

use crate::dopt::Value::{self, Switch, Counted, Plain, List};
use crate::synonym::SynonymMap;
use crate::cap_or_empty;

use self::Argument::{Zero, One};
use self::Atom::{Short, Long, Command, Positional};
use self::Pattern::{Alternates, Sequence, Optional, Repeat, PatAtom};

macro_rules! err(
    ($($arg:tt)*) => (return Err(format!($($arg)*)))
);

#[derive(Clone)]
pub struct Parser {
    pub program: String,
    pub full_doc: String,
    pub usage: String,
    pub descs: SynonymMap<Atom, Options>,
    usages: Vec<Pattern>,
    last_atom_added: Option<Atom>, // context for [default: ...]
}

impl Parser {
    pub fn new(doc: &str) -> Result<Parser, String> {
        let mut d = Parser {
            program: String::new(),
            full_doc: doc.into(),
            usage: String::new(),
            usages: vec!(),
            descs: SynonymMap::new(),
            last_atom_added: None,
        };
        d.parse(doc)?;
        Ok(d)
    }

    pub fn matches(&self, argv: &Argv<'_>) -> Option<SynonymMap<String, Value>> {
        for usage in &self.usages {
            match Matcher::matches(argv, usage) {
                None => continue,
                Some(vals) => return Some(vals),
            }
        }
        None
    }

    pub fn parse_argv(&self, argv: Vec<String>, options_first: bool)
                         -> Result<Argv<'_>, String> {
        Argv::new(self, argv, options_first)
    }
}

impl Parser {
    fn options_atoms(&self) -> Vec<Atom> {
        let mut atoms = vec!();
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
        lazy_static! {
            static ref MUSAGE: Regex = Regex::new(
                r"(?s)(?i:usage):\s*(?P<prog>\S+)(?P<pats>.*?)(?:$|\n\s*\n)"
            ).unwrap();
        }
        let caps = match MUSAGE.captures(doc) {
            None => err!("Could not find usage patterns in doc string."),
            Some(caps) => caps,
        };
        if cap_or_empty(&caps, "prog").is_empty() {
            err!("Could not find program name in doc string.")
        }
        self.program = cap_or_empty(&caps, "prog").to_string();
        self.usage = caps[0].to_string();

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
        let (pstart, pend) = caps.get(0).map(|m|(m.start(), m.end())).unwrap();
        let (before, after) = (&doc[..pstart], &doc[pend..]);
        // We process every line here (instead of restricting to lines starting
        // with "-") because we need to check every line for a default value.
        // The default value always belongs to the most recently defined desc.
        for line in before.lines().chain(after.lines()) {
            self.parse_desc(line)?;
        }

        let mprog = format!(
            "^(?:{})?\\s*(.*?)\\s*$",
            regex::escape(cap_or_empty(&caps, "prog")));
        let pats = Regex::new(&*mprog).unwrap();

        if cap_or_empty(&caps, "pats").is_empty() {
            let pattern = PatParser::new(self, "").parse()?;
            self.usages.push(pattern);
        } else {
            for line in cap_or_empty(&caps, "pats").lines() {
                for pat in pats.captures_iter(line.trim()) {
                    let pattern = PatParser::new(self, &pat[1]).parse()?;
                    self.usages.push(pattern);
                }
            }
        }
        Ok(())
    }

    fn parse_desc(&mut self, full_desc: &str) -> Result<(), String> {
        lazy_static! {
            static ref OPTIONS: Regex = regex!(r"^\s*(?i:options:)\s*");
            static ref ISFLAG: Regex = regex!(r"^(-\S|--\S)");
            static ref REMOVE_DESC: Regex = regex!(r"  .*$");
            static ref NORMALIZE_FLAGS: Regex = regex!(r"([^-\s]), -");
            static ref FIND_FLAGS: Regex = regex!(r"(?x)
                (?:(?P<long>--[^\x20\t=]+)|(?P<short>-[^\x20\t=]+))
                (?:(?:\x20|=)(?P<arg>[^.-]\S*))?
                (?P<repeated>\x20\.\.\.)?
            ");
        }
        let desc = OPTIONS.replace(full_desc.trim(), "");
        let desc = &*desc;
        if !ISFLAG.is_match(desc) {
            self.parse_default(full_desc)?;
            return Ok(())
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
            let (s, l) = (
                cap_or_empty(&flags, "short"),
                cap_or_empty(&flags, "long"),
            );
            if !s.is_empty() {
                if !short.is_empty() {
                    err!("Only one short flag is allowed in an option \
                          description, but found '{}' and '{}'.", short, s)
                }
                short = s.into()
            }
            if !l.is_empty() {
                if !long.is_empty() {
                    err!("Only one long flag is allowed in an option \
                          description, but found '{}' and '{}'.", long, l)
                }
                long = l.into()
            }
            if let Some(arg) = flags.name("arg").map(|m| m.as_str()) {
                if !arg.is_empty() {
                    if !Atom::is_arg(arg) {
                        err!("Argument '{}' is not of the form ARG or <arg>.",
                             arg)
                    }
                    has_arg = true; // may be changed to default later
                }
            }
        }
        // Make sure that we consumed everything. If there are leftovers,
        // then there is some malformed description. Alert the user.
        assert!(last_end <= desc.len());
        if last_end < desc.len() {
            err!("Extraneous text '{}' in option description '{}'.",
                 &desc[last_end..], desc)
        }
        self.add_desc(&short, &long, has_arg, repeated)?;
        // Looking for default in this line must come after adding the
        // description, otherwise `parse_default` won't know which option
        // to assign it to.
        self.parse_default(full_desc)
    }

    fn parse_default(&mut self, desc: &str) -> Result<(), String> {
        lazy_static! {
            static ref FIND_DEFAULT: Regex = regex!(
                r"\[(?i:default):(?P<val>.*)\]"
            );
        }
        let defval =
            match FIND_DEFAULT.captures(desc) {
                None => return Ok(()),
                Some(c) => cap_or_empty(&c, "val").trim(),
            };
        let last_atom =
            match self.last_atom_added {
                None => err!("Found default value '{}' in '{}' before first \
                              option description.", defval, desc),
                Some(ref atom) => atom,
            };
        let opts =
            self.descs
            .find_mut(last_atom)
            .expect(&*format!("BUG: last opt desc key ('{:?}') is invalid.",
                              last_atom));
        match opts.arg {
            One(None) => {}, // OK
            Zero =>
                err!("Cannot assign default value '{}' to flag '{}' \
                      that has no arguments.", defval, last_atom),
            One(Some(ref curval)) =>
                err!("Flag '{}' already has a default value \
                      of '{}' (second default value: '{}').",
                     last_atom, curval, defval),
        }
        opts.arg = One(Some(defval.into()));
        Ok(())
    }

    fn add_desc(
        &mut self,
        short: &str,
        long: &str,
        has_arg: bool,
        repeated: bool,
    ) -> Result<(), String> {
        assert!(!short.is_empty() || !long.is_empty());
        if !short.is_empty() && short.chars().count() != 2 {
            // It looks like the reference implementation just ignores
            // these lines.
            return Ok(());
        }
        let mut opts = Options::new(
            repeated, if has_arg { One(None) } else { Zero });
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
        Ok(())
    }
}

impl fmt::Debug for Parser {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> Result<(), fmt::Error> {
        fn sorted<T: Ord>(mut xs: Vec<T>) -> Vec<T> {
            xs.sort(); xs
        }

        writeln!(f, "=====")?;
        writeln!(f, "Program: {}", self.program)?;

        writeln!(f, "Option descriptions:")?;
        let keys = sorted(self.descs.keys().collect());
        for &k in &keys {
            writeln!(f, "  '{}' => {:?}", k, self.descs.get(k))?;
        }

        writeln!(f, "Synonyms:")?;
        let keys: Vec<(&Atom, &Atom)> =
            sorted(self.descs.synonyms().collect());
        for &(from, to) in &keys {
            writeln!(f, "  {:?} => {:?}", from, to)?;
        }

        writeln!(f, "Usages:")?;
        for pat in &self.usages {
            writeln!(f, "  {:?}", pat)?;
        }
        writeln!(f, "=====")
    }
}

struct PatParser<'a> {
    dopt: &'a mut Parser,
    tokens: Vec<String>, // used while parsing a single usage pattern
    curi: usize, // ^^ index into pattern chars
    expecting: Vec<char>, // stack of expected ']' or ')'
}

impl<'a> PatParser<'a> {
    fn new(dopt: &'a mut Parser, pat: &str) -> PatParser<'a> {
        PatParser {
            dopt: dopt,
            tokens: pattern_tokens(pat),
            curi: 0,
            expecting: vec!(),
        }
    }

    fn parse(&mut self) -> Result<Pattern, String> {
        // let mut seen = HashSet::new();
        let mut p = self.pattern()?;
        match self.expecting.pop() {
            None => {},
            Some(c) => err!("Unclosed group. Expected '{}'.", c),
        }
        p.add_options_shortcut(self.dopt);
        p.tag_repeats(&mut self.dopt.descs);
        Ok(p)
    }

    fn pattern(&mut self) -> Result<Pattern, String> {
        let mut alts = vec!();
        let mut seq = vec!();
        while !self.is_eof() {
            match self.cur() {
                "..." => {
                    err!("'...' must appear directly after a group, argument, \
                          flag or command.")
                }
                "-" | "--" => {
                    // As per specification, `-` and `--` by themselves are
                    // just commands that should be interpreted conventionally.
                    seq.push(self.command()?);
                }
                "|" => {
                    if seq.is_empty() {
                        err!("Unexpected '|'. Not in form 'a | b | c'.")
    
... [TRUNCATED]
```

### File: src\synonym.rs
```rs
use std::collections::HashMap;
use std::collections::hash_map::{Iter, Keys};
use std::fmt::Debug;
use std::hash::Hash;
use std::iter::{FromIterator, IntoIterator};
use std::mem;

#[derive(Clone)]
pub struct SynonymMap<K, V> {
    vals: HashMap<K, V>,
    syns: HashMap<K, K>,
}

impl<K: Eq + Hash, V> SynonymMap<K, V> {
    pub fn new() -> SynonymMap<K, V> {
        SynonymMap {
            vals: HashMap::new(),
            syns: HashMap::new(),
        }
    }

    pub fn insert_synonym(&mut self, from: K, to: K) -> bool {
        assert!(self.vals.contains_key(&to));
        self.syns.insert(from, to).is_none()
    }

    pub fn keys(&self) -> Keys<'_, K, V> {
        self.vals.keys()
    }

    pub fn iter(&self) -> Iter<'_, K, V> {
        self.vals.iter()
    }

    pub fn synonyms(&self) -> Iter<'_, K, K> {
        self.syns.iter()
    }

    pub fn find(&self, k: &K) -> Option<&V> {
        self.with_key(k, |k| self.vals.get(k))
    }

    pub fn contains_key(&self, k: &K) -> bool {
        self.with_key(k, |k| self.vals.contains_key(k))
    }

    pub fn len(&self) -> usize {
        self.vals.len()
    }

    fn with_key<T, F>(&self, k: &K, with: F) -> T where F: FnOnce(&K) -> T {
        if self.syns.contains_key(k) {
            with(&self.syns[k])
        } else {
            with(k)
        }
    }
}

impl<K: Eq + Hash + Clone, V> SynonymMap<K, V> {
    pub fn resolve(&self, k: &K) -> K {
        self.with_key(k, |k| k.clone())
    }

    pub fn get<'a>(&'a self, k: &K) -> &'a V {
        self.find(k).unwrap()
    }

    pub fn find_mut<'a>(&'a mut self, k: &K) -> Option<&'a mut V> {
        if self.syns.contains_key(k) {
            self.vals.get_mut(&self.syns[k])
        } else {
            self.vals.get_mut(k)
        }
    }

    pub fn swap(&mut self, k: K, mut new: V) -> Option<V> {
        if self.syns.contains_key(&k) {
            let old = self.vals.get_mut(&k).unwrap();
            mem::swap(old, &mut new);
            Some(new)
        } else {
            self.vals.insert(k, new)
        }
    }

    pub fn insert(&mut self, k: K, v: V) -> bool {
        self.swap(k, v).is_none()
    }
}

impl<K: Eq + Hash + Clone, V> FromIterator<(K, V)> for SynonymMap<K, V> {
    fn from_iter<T: IntoIterator<Item=(K, V)>>(iter: T) -> SynonymMap<K, V> {
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



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
