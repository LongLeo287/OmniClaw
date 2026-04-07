---
id: rq
type: knowledge
owner: OA_Triage
---
# rq
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
# `rq` [![Build Status](https://travis-ci.org/dflemstr/rq.svg?branch=master)](https://travis-ci.org/dflemstr/rq) [![Build status](https://ci.appveyor.com/api/projects/status/aq916pu1odthadeh?svg=true)](https://ci.appveyor.com/project/dflemstr/rq) [![Crates.io](https://img.shields.io/crates/v/record-query.svg)](https://crates.io/crates/record-query) [![Language (Rust)](https://img.shields.io/badge/powered_by-Rust-blue.svg)](http://www.rust-lang.org/)
**NOTE**: `rq` is in very low maintenance mode as my day job is taking up
a lot of my time.  I will try my best to merge pull requests but will
not drive active development of this crate.

**NOTE**: `rq` no longer ships with query support and a Javascript
engine is not included; instead, it focuses exclusively on format
transformation.  You can still pipe into a runtime like node.js if
you need Javascript evaluation.  Please see [this issue](https://github.com/dflemstr/rq/issues/208)
to discuss introducing a new query language.

This is the home of the tool called `rq` (record query).  It's a tool
that's used for performing queries on streams of records in various
formats.

The goal is to make ad-hoc exploration of data sets easy without
having to use more heavy-weight tools like SQL/MapReduce/custom
programs.  `rq` fills a similar niche as tools like `awk` or `sed`,
but works with structured (record) data instead of text.

It was created with love out of the best parts of Rust, and is
distributed as a dependency-free binary on many operating systems and
architectures.

## Quick links

  - [Installation](doc/installation.md) — How to install `rq`.
  - [Tutorial](doc/tutorial.md) — Learn `rq` from scratch.
  - [Protobuf](doc/protobuf.md) — Configure Protobuf specifics.
  - [Development](CONTRIBUTING.md) — Contribute to `rq`.

## Format support status

| Format                  | Read | Write |
|-------------------------|------|-------|
| Apache Avro             | ✔️    | ✔️     |
| CBOR                    | ✔️    | ✔️     |
| JSON                    | ✔️    | ✔️     |
| MessagePack             | ✔️    | ✔️     |
| Google Protocol Buffers | ✔️    | ✖️     |
| YAML                    | ✔️    | ✔️     |
| TOML                    | ✔️    | ✔️     |
| Raw (plain text)        | ✔️    | ✔️     |
| CSV                     | ✔️    | ✔️     |

```

### File: build.rs
```rs
use vergen::{vergen, Config};

fn main() {
    // Setup the flags, toggling off the 'SEMVER_FROM_CARGO_PKG' flag
    let mut flags = Config::default();
    *flags.build_mut().semver_mut() = false;

    // Generate the 'cargo:' key output
    vergen(flags).expect("Unable to generate the cargo keys!")
}

```

### File: CONTRIBUTING.md
```md
# Contributing

Contributions to `rq` are very welcome; please track contributions via
the [issue tracker](https://github.com/dflemstr/rq/issues).

All issues are marked as either `Bug`s or `Issue`s.  They can also be
tagged with an experience level `E-` which is one of `E-easy`,
`E-medium`, `E-hard`, `E-mentor` and the most likely languages
involved in the change `L-` which can be `L-rust`, `L-js` or `L-c`.

`rq` is not directly affiliated with Spotify but the project still
adheres to its
[code of conduct](https://github.com/spotify/code-of-conduct/blob/master/code-of-conduct.md).

# Development

`rq` is mostly written in the [Rust programming language][rust].
Assuming that you have nothing installed, the easiest way to set
things up is to use `rustup` (see [rustup.rs](https://www.rustup.rs/)
for more info):

    curl -sSLf https://sh.rustup.rs | sh

The Rust installer will give you further platform-specific
instructions (e.g. if you're missing other development tools).

You will need the clang development libraries. On a Debian based Linux system, 
you can get those like this:

    sudo apt install libclang-dev clang

To build `rq`, navigate to the source directory.

You will need a build of the V8 JavaScript engine as well.  If
your operating system package manager doesn't provide a package,
you can download a build like this:

    wget "https://s3-eu-west-1.amazonaws.com/record-query/v8/$TARGET/5.7.441.1/v8-build.tar.gz"
    tar -xvf v8-build.tar.gz
    export V8_LIBS=$PWD/v8-build/lib/libv8uber.a
    export V8_SOURCE=$PWD/v8-build

Now you can run the tests for the project (including JSDoc tests):

    cargo test

A debug build of the executable can be created like so:

    cargo build

It will be available in `target/debug/rq`.

A release build can be created like so (might take a lot longer):

    cargo build --release

It will be available in `target/release/rq`.

# Cross-compiled builds

The easiest way to create cross-compiled builds is to use the `./ci` script.

Look in the Travis build config for available parameters.  For example:

    TARGET=x86_64-unknown-linux-gnu USE_DOCKER=true ./ci test
    TARGET=x86_64-unknown-linux-gnu USE_DOCKER=true ./ci deploy

[rust]: https://www.rust-lang.org/

```

### File: install.sh
```sh
#!/bin/bash -eu
# Copyright 2016 David Flemström.
#
# Based on https://sh.rustup.rs, which is:
# Copyright 2016 The Rust Project Developers
# Licensed under the Apache License, Version 2.0
# (http://www.apache.org/licenses/LICENSE-2.0)

base='https://s3-eu-west-1.amazonaws.com/record-query/record-query'

msg() {
    printf "\33[1mrq:\33[0m %s\n" "$*" >&2
}

err() {
    msg "$@"
    exit 1
}

interactive=true
path=$( (command -v rq | grep -Fv '/usr/bin/') || echo /usr/local/bin/rq)

while [[ $# -gt 1 ]]
do
    case "$1" in
        -y|--yes)
            interactive=false
            ;;
        -o|--output|-p|--path)
            path=$2
            shift
            ;;
        *)
            ;;
    esac
    shift
done

msg "Welcome to the rq installer!"
msg

cpu="$(uname -m)"
os="$(uname -s)"

# Darwin `uname -s` lies
if [ "$os" = Darwin ] && [ "$cpu" = i386 ]
then
    if sysctl hw.optional.x86_64 | grep -q ': 1'
    then
        cpu=x86_64
    fi
fi

case "$os" in
    Linux)
        os=unknown-linux-gnu ;;
    FreeBSD)
        os=unknown-freebsd ;;
    DragonFly)
        os=unknown-dragonfly ;;
    Darwin)
        os=apple-darwin ;;
    MINGW* | MSYS* | CYGWIN*)
        os=pc-windows-gnu ;;
    *)
        err "unrecognized OS type: $os" ;;
esac

case "$cpu" in
    i386 | i486 | i686 | i786 | x86)
        cpu=i686 ;;
    xscale | arm)
        cpu=arm ;;
    armv6l)
        cpu=arm
        os="${os}eabihf" ;;
    armv7l)
        cpu=armv7
        os="${os}eabihf" ;;
    aarch64)
        cpu=aarch64 ;;
    x86_64 | x86-64 | x64 | amd64)
        cpu=x86_64 ;;
    *)
        err "unrecognized CPU type: $cpu" ;;
esac

# Detect 64-bit linux with 32-bit user land
if [ "$os" = unknown-linux-gnu ] && [ "$cpu" = x86_64 ]
then
    bin_to_probe="/usr/bin/env"
    if [ -e "$bin_to_probe" ]
    then
        file -L "$bin_to_probe" | grep -q "x86[_-]64"
        if [ $? != 0 ]
        then
            cpu=i686
        fi
    fi
fi

arch="$cpu-$os"

msg "Detected your architecture to be $arch"

# musl mappings
case "$arch" in
    x86_64-unknown-linux-gnu)
        musl_arch=x86_64-unknown-linux-musl ;;
    i686-unknown-linux-gnu)
        musl_arch=i686-unknown-linux-musl ;;
    arm-unknown-linux-gnueabi)
        musl_arch=arm-unknown-linux-musleabi ;;
    arm-unknown-linux-gnueabihf)
        musl_arch=arm-unknown-linux-musleabihf ;;
    armv7-unknown-linux-gnueabihf)
        musl_arch=armv7-unknown-linux-musleabihf ;;
esac

if [ -n "$musl_arch" ]
then
    if [ "$interactive" = true ]
    then
        msg 'You can install the glibc or musl version of rq:'
        msg
        msg '  • The musl version is statically linked and with zero'
        msg '    dependencies (recommended).'
        msg '  • The glibc version is slightly smaller but depends on'
        msg '    recent versions of libstdc++ and glibc that you might'
        msg '    not have installed.'
        msg
        msg 'Which one do you prefer?'

        options=(musl glibc)
        PS3='Choice: '
        select opt in "${options[@]}"
        do
            case "$opt" in
                musl)
                    arch="$musl_arch"; break ;;
                glibc)
                    break ;;
                *)
                    msg "Invalid choice" ;;
            esac
        done < /dev/tty
    else
        msg 'Detected that your platform supports musl!'
        arch="$musl_arch"
    fi
    msg "Using architecture $arch"
fi

url="$base/$arch/rq"

if [ "$interactive" = true ]
then
    msg "Where should rq be installed? (default: $path)"
    read -rp 'Path: ' new_path < /dev/tty
    if [ -n "$new_path" ]
    then
        path=$(eval echo "$new_path")
    fi
fi

if [ -f "$path" ]
then
    if command -v md5 > /dev/null
    then md5tool=md5
    elif command -v md5sum > /dev/null
    then md5tool=md5sum
    fi

    if command -v python2 > /dev/null
    then pythontool=python2
    elif command -v python > /dev/null
    then pythontool=python
    fi

    if [ -n "$md5tool" ]
    then
        checksum=$("$pythontool" - "$path" <<EOF
import hashlib
import sys

chunk_size = 5 * 1024 * 1024
md5s = []

with open(sys.argv[1], 'rb') as f:
    while True:
        data = f.read(chunk_size)

        if not data:
            break

        md5s.append(hashlib.md5(data))

digests = b''.join(m.digest() for m in md5s)

md5 = hashlib.md5(digests)
print '%s-%s' % (md5.hexdigest(), len(md5s))
EOF
                )
    else
        checksum='0'
    fi
else
    checksum='0'
fi

msg "Downloading rq..."
tmppath=$(mktemp)
trap "rm -f $(printf '%q' "$tmppath")" EXIT
status=$(curl -Lf "$url" --write-out "%{http_code}" -H "If-None-Match: \"$checksum\"" --progress-bar -o "$tmppath")

if [ "$status" = 304 ]
then msg "You already have the latest version of rq in $path"
elif [[ "$status" == 2* ]]
then
    if [ -w "$(dirname "$path")" ]
    then
        msg "Installing rq into $path"
        mv "$tmppath" "$path"
        chmod +x "$path"
    else
        msg "Installing rq into $path (using sudo)"
        sudo /bin/sh -euc "
          mv $(printf '%q' "$tmppath") $(printf '%q' "$path")
          chmod 755 $(printf '%q' "$path")
          chown root:root $(printf '%q' "$path")
        "
    fi

    msg "rq is now installed"
else
    msg "Failed to download rq"
    msg "Status code: $status"
    msg "$(cat "$tmppath")"
fi

```

### File: ci\before_deploy.ps1
```ps1
# This script takes care of packaging the build artifacts that will go in the
# release zipfile

$SRC_DIR = $PWD.Path
$STAGE = [System.Guid]::NewGuid().ToString()

Set-Location $ENV:Temp
New-Item -Type Directory -Name $STAGE
Set-Location $STAGE

$ZIP = "$SRC_DIR\$($Env:CRATE_NAME)-$($Env:APPVEYOR_REPO_TAG_NAME)-$($Env:TARGET).zip"

Copy-Item "$SRC_DIR\target\$($Env:TARGET)\release\rq.exe" '.\'

7z a "$ZIP" *

Push-AppveyorArtifact "$ZIP"

Remove-Item *.* -Force
Set-Location ..
Remove-Item $STAGE
Set-Location $SRC_DIR

```

### File: ci\before_deploy.sh
```sh
# This script takes care of building your crate and packaging it for release

set -ex

main() {
    local src=$(pwd) \
          stage=

    case $TRAVIS_OS_NAME in
        linux)
            stage=$(mktemp -d)
            ;;
        osx)
            stage=$(mktemp -d -t tmp)
            ;;
    esac

    test -f Cargo.lock || cargo generate-lockfile

    cross rustc --bin rq --target $TARGET --release -- -C lto

    cp target/$TARGET/release/rq $stage/

    cd $stage
    tar czf $src/$CRATE_NAME-$TRAVIS_TAG-$TARGET.tar.gz *
    cd $src

    rm -rf $stage
}

main

```

### File: ci\install.sh
```sh
set -ex

main() {
    local target=
    if [ $TRAVIS_OS_NAME = linux ]; then
        target=x86_64-unknown-linux-musl
        sort=sort
    else
        target=x86_64-apple-darwin
        sort=gsort  # for `sort --sort-version`, from brew's coreutils.
    fi

    # Builds for iOS are done on OSX, but require the specific target to be
    # installed.
    case $TARGET in
        aarch64-apple-ios)
            rustup target install aarch64-apple-ios
            ;;
        armv7-apple-ios)
            rustup target install armv7-apple-ios
            ;;
        armv7s-apple-ios)
            rustup target install armv7s-apple-ios
            ;;
        i386-apple-ios)
            rustup target install i386-apple-ios
            ;;
        x86_64-apple-ios)
            rustup target install x86_64-apple-ios
            ;;
    esac

    # This fetches latest stable release
    local tag=$(git ls-remote --tags --refs --exit-code https://github.com/japaric/cross \
                       | cut -d/ -f3 \
                       | grep -E '^v[0.1.0-9.]+$' \
                       | $sort --version-sort \
                       | tail -n1)
    curl -LSfs https://japaric.github.io/trust/install.sh | \
        sh -s -- \
           --force \
           --git japaric/cross \
           --tag $tag \
           --target $target
}

main

```

### File: ci\script.sh
```sh
# This script takes care of testing your crate

set -ex

main() {
    cross build --target $TARGET
    cross build --target $TARGET --release

    if [ ! -z $DISABLE_TESTS ]; then
        return
    fi

    cross test --target $TARGET
    cross test --target $TARGET --release
}

# we don't run the "test phase" when doing deploys
if [ -z $TRAVIS_TAG ]; then
    main
fi

```

### File: doc\installation.md
```md
# Installation

There are many different ways to install `rq`, listed from most preferred
to least preferred.

TODO: this section will soon be updated!

  * [Generic](#generic) (Up to date, fast)
  * [Cargo](#cargo) (Stable releases, slow)
  * [GitHub releases](#github-releases) (Stable releases, fast)
  * [Arch Linux](#arch-linux) (Up to date, fast)
  * [Mac OS X](#mac-os-x) (Out of date, slow)
  * [Nix](#nix) (Up to date, slow)

## Generic

There is a generic best-effort installer available via the dreaded
`curl | bash` method.  This is the preferred method, because you don't
need to compile `rq` from scratch, and you always get the latest
version.

    curl -LSfs https://japaric.github.io/trust/install.sh | sh -s -- --git dflemstr/rq

## Cargo

There is a crate available on [crates.io](https://crates.io/), so just run:

    cargo install record-query

## GitHub releases

There are tagged releases of `rq` fairly infrequently.  You can
download pre-built binaries from the
[GitHub releases](https://github.com/dflemstr/rq/releases) page.  Note
that these might be very out of date compared to `master`.

## Arch Linux

There is an official package in the [community] repository:

    pacman -S rq

## Mac OS X

There is a Homebrew tap available.  Add it like this:

    brew tap dflemstr/tools

This will let you install the latest version of `rq` (recommended):

    brew install --HEAD rq

Note that the compilation might take some time, use `-v` for details.

If you for some reason want the last tagged release of `rq` (might be
severely out of date):

    brew install rq

## Nix

`rq` is available in nixpkgs. You can install it via `nix-env`:

    nix-env -i rq

 Or add to packages list if you use [Home Manager](https://github.com/rycee/home-manager):

     home.packages = [ pkgs.rq ]

```

### File: doc\protobuf.md
```md
# Protobuf

The Google Protocol Buffer support in `rq` is special because Protobuf
requires an external schema to parse messages.

`rq` maintains its own database of Protobuf schemata that is used to
parse messages.  You can add a schema to the database and all
definitions in that schema will be made available.  The schemata all
share the same namespace so you can't provide conflicting definitions
for messages.

## Adding new schemata

Adding new schemata to the database is simple:

    rq protobuf add myschema.proto

This stashes away the schema to be used the next time you run `rq`
with the `-p` flag.

Some schemata need to be in specific directories because of references
by other schema files.  `rq` will by default use the relative file
name specified in the invocation to save the file internally.  That
means that if you call `rq` like so:

    rq protobuf add foo/bar/schema.proto

...then the schema will be stored internally with the given relative
path of `foo/bar/schema.proto`.  You can control this behavior with
the `--base` flag, so this:

    rq protobuf add foo/bar/schema.proto --base foo

...will store the schema as `bar/schema.proto`.

## Deserializing messages

You specify the fully qualified message name when deserializing
Protobuf:

    rq -p .foo.bar.Person

The leading `.` is needed to disambiguate namespace/package aliases,
which are yet to be implemented.

```

### File: doc\tutorial.md
```md
# Tutorial

This assumes that `rq` is installed.  See
[installation](installation.md) for more details on how to do that if
you want to follow along.

## Input/Output

`rq` reads record data from stdin, and writes transformed data to
stdout.  By default, it uses JSON for the input and output format, and
returns each input record unmodified:

    $ rq <<< 'null true {"a": 2.5}'
    null
    true
    {"a":2.5}

## Highlighting

This Markdown document doesn't do the `rq` output justice.  The output
of `rq` is actually very colorful!

![highlighting](image/highlighting.png)

## Record formats

You can configure the input and output formats to use with flags (see
`rq --help` for details).  A lower-case single-letter flag sets the
input format, and an upper-case single-letter flag sets the output
format.  For example, to read JSON and output CBOR, pass `-jC` and to
read CBOR and output JSON, pass `-cJ`.  This can be used to build a
not-very-useful conversion pipeline that round-trips to CBOR (maybe
you could pipe it through `gzip` and `ssh` in-between and it might be
worth it):

    $ (rq -jC | rq -cJ) <<< 'null true {"a": 2.5}'
    null
    true
    {"a":2.5}

Some format flags take an argument to configure them, for example
Google Protocol Buffers:

    $ rq protobuf add example.proto
    $ rq -p .example.Person < person.pb
    {"name":"John","age":34}

```

### File: src\config.rs
```rs
use crate::error;

use glob;
use std::env;
use std::path;

#[derive(Debug)]
pub struct Paths {
    config: path::PathBuf,
    cache: path::PathBuf,
    data: path::PathBuf,
}

impl Paths {
    pub fn new() -> error::Result<Self> {
        match env::var_os("RQ_SYSTEM_DIR") {
            Some(basepath) => {
                let basepath = path::Path::new(&basepath);
                Ok(Self {
                    config: basepath.join("config"),
                    cache: basepath.join("cache"),
                    data: basepath.join("data"),
                })
            },
            None => match directories::ProjectDirs::from("io", "dflemstr", "rq") {
                Some(dirs) => Ok(Self {
                    config: dirs.config_dir().into(),
                    cache: dirs.cache_dir().into(),
                    data: dirs.data_dir().into(),
                }),
                None => Err(error::Error::Message(
                    "The environment variable RQ_SYSTEM_DIR is unspecified and no home directory is known".to_string()
                )),
            },
        }
    }

    pub fn preferred_config<P>(&self, path: P) -> path::PathBuf
    where
        P: AsRef<path::Path>,
    {
        let mut result = self.config.clone();
        result.push(path);
        result
    }

    pub fn preferred_cache<P>(&self, path: P) -> path::PathBuf
    where
        P: AsRef<path::Path>,
    {
        let mut result = self.cache.clone();
        result.push(path);
        result
    }

    pub fn preferred_data<P>(&self, path: P) -> path::PathBuf
    where
        P: AsRef<path::Path>,
    {
        let mut result = self.data.clone();
        result.push(path);
        result
    }

    pub fn find_config(&self, pattern: &str) -> error::Result<Vec<path::PathBuf>> {
        find(&self.config, pattern)
    }

    pub fn find_data(&self, pattern: &str) -> error::Result<Vec<path::PathBuf>> {
        find(&self.data, pattern)
    }
}

fn find(home: &path::Path, pattern: &str) -> error::Result<Vec<path::PathBuf>> {
    let mut result = Vec::new();
    run_pattern(home, pattern, &mut result)?;
    Ok(result)
}

fn run_pattern(
    dir: &path::Path,
    pattern: &str,
    result: &mut Vec<path::PathBuf>,
) -> error::Result<()> {
    let full_pattern = format!("{}/{}", dir.to_string_lossy(), pattern);

    for entry in glob::glob(&full_pattern)? {
        result.push(entry?);
    }

    Ok(())
}

```

### File: src\error.rs
```rs
use csv;
use glob;
use protobuf;
use rmpv;
use serde_cbor;
use serde_hjson;
use serde_json;
use serde_protobuf;
use serde_yaml;
use std::io;
use std::string;
use toml;
#[cfg(feature = "v8")]
use v8;
use yaml_rust;

use std::result;

pub type Result<A> = result::Result<A, Error>;

#[derive(Debug, Fail)]
pub enum Error {
    #[fail(display = "protobuf error")]
    Protobuf(#[cause] serde_protobuf::error::Error),
    #[fail(display = "IO error")]
    Io(#[cause] io::Error),
    #[fail(display = "UTF-8 error")]
    Utf8(#[cause] string::FromUtf8Error),
    #[fail(display = "native protobuf error")]
    NativeProtobuf(#[cause] protobuf::ProtobufError),
    #[fail(display = "MessagePack encode error")]
    MessagePackEncode(#[cause] rmpv::encode::Error),
    #[fail(display = "Avro error")]
    Avro(#[cause] Avro),
    #[fail(display = "CBOR error")]
    Cbor(#[cause] serde_cbor::error::Error),
    #[fail(display = "HJSON error")]
    Hjson(#[cause] serde_hjson::Error),
    #[fail(display = "JSON error")]
    Json(#[cause] serde_json::Error),
    #[fail(display = "YAML error")]
    Yaml(#[cause] serde_yaml::Error),
    #[fail(display = "YAML scan error")]
    YamlScan(#[cause] yaml_rust::ScanError),
    #[fail(display = "TOML deserialize error")]
    TomlDeserialize(#[cause] toml::de::Error),
    #[fail(display = "TOML serialize error")]
    TomlSerialize(#[cause] toml::ser::Error),
    #[fail(display = "glob error")]
    Glob(#[cause] glob::GlobError),
    #[fail(display = "glob pattern error")]
    GlobPattern(#[cause] glob::PatternError),
    #[fail(display = "CSV error")]
    Csv(#[cause] csv::Error),
    #[fail(display = "MessagePack decode error")]
    MessagePackDecode(#[cause] rmpv::decode::Error),
    #[fail(display = "unimplemented: {}", msg)]
    Unimplemented { msg: String },
    #[fail(display = "illegal state: {}", msg)]
    IllegalState { msg: String },
    #[fail(display = "format error: {}", msg)]
    Format { msg: String },
    #[fail(display = "internal error: {}", _0)]
    Internal(&'static str),
    #[fail(display = "{}", _0)]
    Message(String),
}

#[derive(Debug, Fail)]
pub enum Avro {
    #[fail(display = "decode error")]
    Decode(#[cause] avro_rs::DecodeError),
    #[fail(display = "error when parsing schema")]
    ParseSchema(#[cause] avro_rs::ParseSchemaError),
    #[fail(display = "schema resolution error")]
    SchemaResolution(#[cause] avro_rs::SchemaResolutionError),
    #[fail(display = "validation error")]
    Validation(#[cause] avro_rs::ValidationError),
    #[fail(display = "{}", message)]
    Custom { message: String },
}

impl Error {
    pub fn unimplemented(msg: String) -> Self {
        Self::Unimplemented { msg }
    }

    pub fn illegal_state(msg: String) -> Self {
        Self::IllegalState { msg }
    }
}

impl Avro {
    pub fn downcast(error: failure::Error) -> Self {
        let error = match error.downcast::<avro_rs::DecodeError>() {
            Ok(error) => return Self::Decode(error),
            Err(error) => error,
        };

        let error = match error.downcast::<avro_rs::ParseSchemaError>() {
            Ok(error) => return Self::ParseSchema(error),
            Err(error) => error,
        };

        let error = match error.downcast::<avro_rs::SchemaResolutionError>() {
            Ok(error) => return Self::SchemaResolution(error),
            Err(error) => error,
        };

        let error = match error.downcast::<avro_rs::ValidationError>() {
            Ok(error) => return Self::Validation(error),
            Err(error) => error,
        };

        Self::Custom {
            message: error.to_string(),
        }
    }
}

macro_rules! gen_from {
    ($t:ty, $i:ident) => {
        impl From<$t> for Error {
            fn from(e: $t) -> Self {
                Self::$i(e)
            }
        }
    };
}

gen_from!(serde_protobuf::error::Error, Protobuf);
gen_from!(io::Error, Io);
#[cfg(feature = "js")]
gen_from!(v8::error::Error, Js);
gen_from!(string::FromUtf8Error, Utf8);
gen_from!(protobuf::ProtobufError, NativeProtobuf);
gen_from!(rmpv::encode::Error, MessagePackEncode);
gen_from!(serde_cbor::error::Error, Cbor);
gen_from!(serde_hjson::Error, Hjson);
gen_from!(serde_json::Error, Json);
gen_from!(serde_yaml::Error, Yaml);
gen_from!(yaml_rust::ScanError, YamlScan);
gen_from!(toml::de::Error, TomlDeserialize);
gen_from!(toml::ser::Error, TomlSerialize);
gen_from!(glob::GlobError, Glob);
gen_from!(glob::PatternError, GlobPattern);
gen_from!(csv::Error, Csv);
gen_from!(rmpv::decode::Error, MessagePackDecode);

```

### File: src\lib.rs
```rs
//! `rq` (Record Query) is a library and command-line tool for manipulating structured (record)
//! data.

// For pest parser generation
#![recursion_limit = "1024"]
#![deny(warnings)]
#![deny(clippy::all)]
#![deny(
    missing_debug_implementations,
    trivial_casts,
    trivial_numeric_casts,
    unused_extern_crates,
    unused_import_braces,
    unused_qualifications
)]

#[macro_use]
extern crate failure;
#[macro_use]
extern crate log;
#[macro_use]
extern crate pest;

pub mod config;
pub mod error;
pub mod proto_index;
pub mod value;

pub const VERSION: &str = env!("VERGEN_GIT_SEMVER");

#[doc(hidden)]
#[deprecated(since = "1.0.1", note = "use VERSION instead")]
pub const GIT_VERSION: &str = VERSION;

```

### File: src\proto_index.rs
```rs
use crate::config;
use crate::error;

use protobuf;
use std::cmp;
use std::fs;
use std::path;
use std::process;

pub fn add_file(
    paths: &config::Paths,
    relative_to: &path::Path,
    file: &path::Path,
) -> error::Result<()> {
    let rel_file = file
        .strip_prefix(relative_to)
        .unwrap_or_else(|_| file.file_name().map_or(file, path::Path::new));
    let target = paths.preferred_data("proto").join(rel_file);

    if let Some(parent) = target.parent() {
        trace!("Creating directory {:?}", parent);
        fs::create_dir_all(parent)?;
    }

    fs::copy(file, &target)?;
    info!("Added proto file as {:?}", target);
    Ok(())
}

pub fn compile_descriptor_set(
    paths: &config::Paths,
) -> error::Result<protobuf::descriptor::FileDescriptorSet> {
    let proto_includes = paths.find_data("proto")?;
    let proto_files = paths.find_data("proto/**/*.proto")?;
    let cache = paths.preferred_cache("descriptor-cache.pb");

    debug!("Proto includes: {:?}", proto_includes);
    debug!("Proto files: {:?}", proto_files);
    debug!("Proto cache location: {:?}", cache);

    if is_cache_stale(&cache, &proto_files)? {
        info!("Proto descriptor cache is stale; recomputing");

        if let Some(parent) = cache.parent() {
            trace!("Creating directory {:?}", parent);
            fs::create_dir_all(parent)?;
        }

        let include_args = proto_includes
            .into_iter()
            .map(|p| format!("-I{}", p.to_string_lossy()))
            .collect::<Vec<_>>();

        let status = process::Command::new("protoc")
            .arg("-o")
            .arg(&cache)
            .args(&include_args)
            .args(&proto_files)
            .status()?;
        if !status.success() {
            panic!("protoc descriptor compilation failed");
        }

        trace!("Proto descriptor cache regenerated");
    }

    let mut cache_file = fs::File::open(&cache)?;
    let descriptor_set = protobuf::Message::parse_from_reader(&mut cache_file)?;

    trace!("Successfully parsed descriptor set from cache");

    Ok(descriptor_set)
}

fn is_cache_stale<P>(cache: &path::Path, proto_files: &[P]) -> error::Result<bool>
where
    P: AsRef<path::Path>,
{
    if cache.exists() {
        let cache_metadata = fs::metadata(&cache)?;
        let cache_mtime = cache_metadata.modified()?;
        let mut max_proto_mtime = std::time::SystemTime::UNIX_EPOCH;

        for proto_file in proto_files.iter() {
            let proto_metadata = fs::metadata(&proto_file)?;
            let proto_mtime = proto_metadata.modified()?;
            max_proto_mtime = cmp::max(max_proto_mtime, proto_mtime);
        }

        Ok(cache_mtime < max_proto_mtime)
    } else {
        Ok(true)
    }
}

```

### File: src\bin\rq.rs
```rs
#[macro_use]
extern crate log;
#[macro_use]
extern crate structopt;

use record_query as rq;
use std::env;
use std::fs;
use std::io;
use std::io::prelude::*;
use std::path;
use std::str;

#[derive(Debug, StructOpt)]
#[structopt(
    name = "rq",
    version = record_query::VERSION,
    about = r#"
A tool for manipulating data records.

Records are read from stdin, processed, and written to stdout.  The tool accepts
a query in the custom rq query language as its main command-line arguments.

See https://github.com/dflemstr/rq for in-depth documentation.
"#
)]
pub struct Options {
    #[structopt(subcommand)]
    pub subcmd: Option<Subcmd>,

    /// A query indicating how to transform each record.
    pub arg_query: Option<String>,

    /// Force stylistic output formatting.  Can be one of 'compact',
    /// 'readable' (with color) or 'indented' (without color) and the default is
    /// inferred from the terminal environment.
    #[structopt(long = "format")]
    pub flag_format: Option<Format>,
    #[structopt(long = "codec")]
    pub flag_codec: Option<String>,

    /// Input is an Apache Avro container file.
    #[structopt(short = "a", long = "input-avro")]
    pub flag_input_avro: bool,
    /// Input is a series of CBOR values.
    #[structopt(short = "c", long = "input-cbor")]
    pub flag_input_cbor: bool,
    /// Input is white-space separated JSON values (default).
    #[structopt(short = "j", long = "input-json")]
    pub flag_input_json: bool,
    /// Input is CSV.
    #[structopt(short = "v", long = "input-csv")]
    pub flag_input_csv: bool,
    /// Input is formatted as MessagePack.
    #[structopt(short = "m", long = "input-message-pack")]
    pub flag_input_message_pack: bool,
    #[structopt(short = "p", long = "input-protobuf")]
    pub flag_input_protobuf: Option<String>,
    /// Input is plain text.
    #[structopt(short = "r", long = "input-raw")]
    pub flag_input_raw: bool,
    /// Input is formatted as TOML document.
    #[structopt(short = "t", long = "input-toml")]
    pub flag_input_toml: bool,
    /// Input is a series of YAML documents.
    #[structopt(short = "y", long = "input-yaml")]
    pub flag_input_yaml: bool,

    #[structopt(short = "A", long = "output-avro")]
    pub flag_output_avro: Option<String>,
    #[structopt(short = "C", long = "output-cbor")]
    pub flag_output_cbor: bool,
    #[structopt(short = "J", long = "output-json")]
    pub flag_output_json: bool,
    #[structopt(short = "R", long = "output-raw")]
    pub flag_output_raw: bool,
    #[structopt(short = "V", long = "output-csv")]
    pub flag_output_csv: bool,
    #[structopt(short = "M", long = "output-message-pack")]
    pub flag_output_message_pack: bool,
    #[structopt(short = "P", long = "output-protobuf")]
    pub flag_output_protobuf: Option<String>,
    #[structopt(short = "T", long = "output-toml")]
    pub flag_output_toml: bool,
    #[structopt(short = "Y", long = "output-yaml")]
    pub flag_output_yaml: bool,

    #[structopt(short = "l", long = "log")]
    pub flag_log: Option<String>,
    #[structopt(short = "q", long = "quiet")]
    pub flag_quiet: bool,
    #[structopt(long = "trace")]
    pub flag_trace: bool,
}

#[derive(Debug, StructOpt)]
pub enum Subcmd {
    #[structopt(name = "protobuf")]
    Protobuf {
        #[structopt(subcommand)]
        subcmd: ProtobufSubcmd,
    },
}

#[derive(Debug, StructOpt)]
pub enum ProtobufSubcmd {
    #[structopt(name = "add")]
    Add {
        schema: path::PathBuf,
        #[structopt(short = "b", long = "base")]
        base: Option<path::PathBuf>,
    },
}

#[derive(Clone, Copy, Debug, Eq, Ord, PartialEq, PartialOrd)]
pub enum Format {
    Compact,
    Readable,
    Indented,
}

fn main() {
    use structopt::StructOpt;

    let args: Options = match Options::clap().get_matches_safe() {
        Err(e) => {
            match e.kind {
                structopt::clap::ErrorKind::HelpDisplayed => set_ran_cmd("help").unwrap(),
                structopt::clap::ErrorKind::VersionDisplayed => set_ran_cmd("version").unwrap(),
                _ => (),
            }
            e.exit()
        }
        Ok(a) => Options::from_clap(&a),
    };

    setup_log(args.flag_log.as_ref().map(String::as_ref), args.flag_quiet);

    main_with_args(&args).unwrap_or_else(|e| log_error(&args, &e));
}

fn main_with_args(args: &Options) -> rq::error::Result<()> {
    match args.subcmd {
        Some(Subcmd::Protobuf { ref subcmd }) => match subcmd {
            ProtobufSubcmd::Add { schema, base } => {
                let base = base
                    .as_ref()
                    .map_or_else(|| path::Path::new("."), |p| p.as_path());
                let paths = rq::config::Paths::new()?;
                rq::proto_index::add_file(&paths, base, schema)
            }
        },
        None => run(args),
    }
}

fn run(args: &Options) -> rq::error::Result<()> {
    let stdin = io::stdin();
    let mut input = stdin.lock();

    if let Some(ref name) = args.flag_input_protobuf {
        let paths = rq::config::Paths::new()?;
        let proto_descriptors = load_descriptors(&paths)?;
        let stream = protobuf::CodedInputStream::new(&mut input);
        let source = rq::value::protobuf::source(&proto_descriptors, name, stream)?;
        run_source(args, source)
    } else if args.flag_input_avro {
        let source = rq::value::avro::source(&mut input)?;
        run_source(args, source)
    } else if args.flag_input_cbor {
        let source = rq::value::cbor::source(&mut input);
        run_source(args, source)
    } else if args.flag_input_message_pack {
        let source = rq::value::messagepack::source(&mut input);
        run_source(args, source)
    } else if args.flag_input_toml {
        let source = rq::value::toml::source(&mut input)?;
        run_source(args, source)
    } else if args.flag_input_yaml {
        let source = rq::value::yaml::source(&mut input);
        run_source(args, source)
    } else if args.flag_input_raw {
        let source = rq::value::raw::source(&mut input);
        run_source(args, source)
    } else if args.flag_input_csv {
        if env::args().skip(1).any(|v| v == "-v") && !has_ran_cmd("help")? {
            warn!("You started rq -v, which puts it in CSV input mode.");
            warn!("It's now waiting for CSV input, which might not be what you wanted.");
            warn!(
                "Specify --input-csv explicitly or run rq --help once to suppress this \
                 warning."
            );
        }
        let source = rq::value::csv::source(&mut input);
        run_source(args, source)
    } else {
        if !args.flag_input_json && !has_ran_cmd("help")? {
            warn!("You started rq without any input flags, which puts it in JSON input mode.");
            warn!("It's now waiting for JSON input, which might not be what you wanted.");
            warn!(
                "Specify (-j|--input-json) explicitly or run rq --help once to suppress this \
                 warning."
            );
        }
        let source = rq::value::json::source(&mut input);
        run_source(args, source)
    }
}

fn run_source<I>(args: &Options, source: I) -> rq::error::Result<()>
where
    I: rq::value::Source,
{
    let mut output = io::stdout();

    let format = args.flag_format.unwrap_or_else(infer_format);

    macro_rules! dispatch_format {
        ($compact:expr, $readable:expr, $indented:expr) => {
            match format {
                Format::Compact => {
                    let sink = $compact(&mut output);
                    run_source_sink(source, sink)
                }
                Format::Readable => {
                    let sink = $readable(&mut output);
                    run_source_sink(source, sink)
                }
                Format::Indented => {
                    let sink = $indented(&mut output);
                    run_source_sink(source, sink)
                }
            }
        };
    }

    if args.flag_output_protobuf.is_some() {
        Err(rq::error::Error::unimplemented(
            "protobuf serialization".to_owned(),
        ))
    } else if let Some(ref schema_filename) = args.flag_output_avro {
        use std::str::FromStr;

        let schema = read_avro_schema_from_file(path::Path::new(schema_filename))?;
        let codec_string = if let Some(ref c) = args.flag_codec {
            c.as_str()
        } else {
            "null"
        };
        let codec = if let Ok(v) = avro_rs::Codec::from_str(codec_string) {
            v
        } else {
            return Err(rq::error::Error::Message(format!(
                "illegal Avro codec: {}",
                codec_string
            )));
        };
        let sink = rq::value::avro::sink(&schema, &mut output, codec)?;
        run_source_sink(source, sink)
    } else if args.flag_output_cbor {
        let sink = rq::value::cbor::sink(&mut output);
        run_source_sink(source, sink)
    } else if args.flag_output_message_pack {
        let sink = rq::value::messagepack::sink(&mut output);
        run_source_sink(source, sink)
    } else if args.flag_output_toml {
        // TODO: add TOML ugly printing eventually; now it's always "readable"
        dispatch_format!(
            rq::value::toml::sink,
            rq::value::toml::sink,
            rq::value::toml::sink
        )
    } else if args.flag_output_yaml {
        // TODO: add YAML ugly printing eventually; now it's always "readable"
        dispatch_format!(
            rq::value::yaml::sink,
            rq::value::yaml::sink,
            rq::value::yaml::sink
        )
    } else if args.flag_output_raw {
        let sink = rq::value::raw::sink(&mut output);
        run_source_sink(source, sink)
    } else if args.flag_output_csv {
        let sink = rq::value::csv::sink(&mut output);
        run_source_sink(source, sink)
    } else {
        dispatch_format!(
            rq::value::json::sink_compact,
            rq::value::json::sink_readable,
            rq::value::json::sink_indented
        )
    }
}

fn read_avro_schema_from_file(path: &path::Path) -> rq::error::Result<avro_rs::Schema> {
    let mut file = fs::File::open(path)?;
    let mut buffer = String::new();
    file.read_to_string(&mut buffer)?;
    avro_rs::Schema::parse_str(&buffer)
        .map_err(|e| rq::error::Error::Avro(rq::error::Avro::downcast(e)))
}

fn run_source_sink<I, O>(mut source: I, mut sink: O) -> rq::error::Result<()>
where
    I: rq::value::Source,
    O: rq::value::Sink,
{
    while let Some(result) = rq::value::Source::read(&mut source)? {
        sink.write(result)?;
    }
    Ok(())
}

fn load_descriptors(
    paths: &rq::config::Paths,
) -> rq::error::Result<serde_protobuf::descriptor::Descriptors> {
    let descriptors_proto = rq::proto_index::compile_descriptor_set(paths)?;
    Ok(serde_protobuf::descriptor::Descriptors::from_proto(
        &descriptors_proto,
    ))
}

fn infer_format() -> Format {
    if atty::is(atty::Stream::Stdout) {
        Format::Readable
    } else {
        Format::Compact
    }
}

fn has_ran_cmd(cmd: &str) -> rq::error::Result<bool> {
    let paths = match rq::config::Paths::new() {
        Ok(paths) => paths,
        Err(_) => return Ok(false),
    };
    paths
        .find_config(&format!("{}{}", "has-ran-", cmd))
        .map(|v| !v.is_empty())
        .map_err(From::from)
}

fn set_ran_cmd(cmd: &str) -> rq::error::Result<()> {
    let paths = match rq::config::Paths::new() {
        Ok(paths) => paths,
        Err(_) => return Ok(()),
    };

    let file = paths.preferred_config(format!("{}{}", "has-ran-", cmd));

    if let Some(parent) = file.parent() {
        fs::create_dir_all(parent)?;
    }

    fs::File::create(&file)?;

    Ok(())
}

fn log_error(args: &Options, error: &rq::error::Error) {
    use failure::Fail;

    let main_str = format!("{}", error);
    let mut main_lines = main_str.lines();
    error!("Encountered: {}", main_lines.next().unwrap());
    for line in main_lines {
        error!("  {}", line);
    }
    for e in <dyn failure::Fail>::iter_causes(error) {
        let sub_str = format!("{}", e);
        let mut sub_lines = sub_str.lines();
        error!("Caused by: {}", sub_lines.next().unwrap());
        for line in sub_lines {
            error!("  {}", line);
        }
    }

    if args.flag_trace || env::var("RUST_BACKTRACE").as_ref().map(String::as_str) == Ok("1") {
        error!("");
        if let Some(backtrace) = error.backtrace() {
            error!("Backtrace:");
            for line in format!("{:?}", backtrace).lines() {
                error!("  {}", line);
            }
        } else {
            error!("(No backtrace available)");
        }
    } else {
        error!("(Re-run with --trace or RUST_BACKTRACE=1 for a backtrace)");
    }
}

fn setup_log(spec: Option<&str>, quiet: bool) {
    let mut builder = env_logger::Builder::new();

    if quiet {
        builder.filter(None, log::LevelFilter::Off);
    } else if let Some(s) = spec {
        builder.parse_filters(s);
    } else if let Ok(s) = env::var("RUST_LOG") {
        builder.parse_filters(&s);
    } else {
        builder.filter(None, log::LevelFilter::Info);
    };

    builder.format(format_log_record);

    builder.init();
}

impl str::FromStr for Format {
    type Err = failure::Error;

    fn from_str(s: &str) -> Result<Self, Self::Err> {
        match s {
            "compact" => Ok(Self::Compact),
            "readable" => Ok(Self::Readable),
            "indented" => Ok(Self::Indented),
            _ => Err(failure::err_msg(format!("unrecognized format: {}", s))),
        }
    }
}

fn format_log_record(
    formatter: &mut env_logger::fmt::Formatter,
    record: &log::Record,
) -> io::Result<()> {
    use ansi_term::ANSIStrings;
    use ansi_term::Colour;
    use ansi_term::Style;

    if atty::is(atty::Stream::Stderr) {
        let normal = Style::new();
        let (front, back) = match record.level() {
            log::Level::Error => (Colour::Red.normal(), Colour::Red.dimmed()),
            log::Level::Warn => (Colour::Yellow.normal(), Colour::Yellow.dimmed()),
            log::Level::Info => (Colour::Blue.normal(), Colour::Blue.dimmed()),
            log::Level::Debug => (Colour::Purple.normal(), Colour::Purple.dimmed()),
            log::Level::Trace => (Colour::White.dimmed(), Colour::Black.normal()),
        };

        let strings = &[
            back.paint("["),
            front.paint(format!("{}", record.level())),
            back.paint("]"),
            normal.paint(" "),
            back.paint("["),
            front.paint(record.module_path().unwrap_or("<unknown>")),
            back.paint("]"),
            normal.paint(" "),
            front.paint(format!("{}", record.args())),
        ];

        writeln!(formatter, "{}", ANSIStrings(strings))
    } else {
        writeln!(
            formatter,
            "[{}] [{}] {}",
            record.level(),
            record.module_path().unwrap_o
... [TRUNCATED]
```

