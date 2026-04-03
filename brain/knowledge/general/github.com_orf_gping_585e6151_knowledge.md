---
id: github.com-orf-gping-585e6151-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:09.890384
---

# KNOWLEDGE EXTRACT: github.com_orf_gping_585e6151
> **Extracted on:** 2026-04-01 07:43:05
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007519190/github.com_orf_gping_585e6151

---

## File: `.dockerignore`
```
target/
.git/
```

## File: `.gitignore`
```
/target
.idea/
```

## File: `.pre-commit-config.yaml`
```yaml
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v5.0.0
    hooks:
      - id: check-yaml
      - id: end-of-file-fixer
      - id: trailing-whitespace
        exclude: 'ping.1'
  - repo: local
    hooks:
      - id: rustfmt
        name: rustfmt
        entry: cargo fmt -- --check
        pass_filenames: false
        language: system
      - id: clippy
        name: clippy
        entry: cargo clippy --all-targets --all-features -- -D warnings
        pass_filenames: false
        language: system
      - id: mangen
        name: mangen
        entry: env GENERATE_MANPAGE="gping.1" cargo run
        pass_filenames: false
        language: system
```

## File: `CODE_OF_CONDUCT.md`
```markdown
# Contributor Covenant Code of Conduct

## Our Pledge

We as members, contributors, and leaders pledge to make participation in our
community a harassment-free experience for everyone, regardless of age, body
size, visible or invisible disability, ethnicity, sex characteristics, gender
identity and expression, level of experience, education, socio-economic status,
nationality, personal appearance, race, religion, or sexual identity
and orientation.

We pledge to act and interact in ways that contribute to an open, welcoming,
diverse, inclusive, and healthy community.

## Our Standards

Examples of behavior that contributes to a positive environment for our
community include:

* Demonstrating empathy and kindness toward other people
* Being respectful of differing opinions, viewpoints, and experiences
* Giving and gracefully accepting constructive feedback
* Accepting responsibility and apologizing to those affected by our mistakes,
  and learning from the experience
* Focusing on what is best not just for us as individuals, but for the
  overall community

Examples of unacceptable behavior include:

* The use of sexualized language or imagery, and sexual attention or
  advances of any kind
* Trolling, insulting or derogatory comments, and personal or political attacks
* Public or private harassment
* Publishing others' private information, such as a physical or email
  address, without their explicit permission
* Other conduct which could reasonably be considered inappropriate in a
  professional setting

## Enforcement Responsibilities

Community leaders are responsible for clarifying and enforcing our standards of
acceptable behavior and will take appropriate and fair corrective action in
response to any behavior that they deem inappropriate, threatening, offensive,
or harmful.

Community leaders have the right and responsibility to remove, edit, or reject
comments, commits, code, wiki edits, issues, and other contributions that are
not aligned to this Code of Conduct, and will communicate reasons for moderation
decisions when appropriate.

## Scope

This Code of Conduct applies within all community spaces, and also applies when
an individual is officially representing the community in public spaces.
Examples of representing our community include using an official e-mail address,
posting via an official social media account, or acting as an appointed
representative at an online or offline event.

## Enforcement

Instances of abusive, harassing, or otherwise unacceptable behavior may be
reported to the community leaders responsible for enforcement at
.
All complaints will be reviewed and investigated promptly and fairly.

All community leaders are obligated to respect the privacy and security of the
reporter of any incident.

## Enforcement Guidelines

Community leaders will follow these Community Impact Guidelines in determining
the consequences for any action they deem in violation of this Code of Conduct:

### 1. Correction

**Community Impact**: Use of inappropriate language or other behavior deemed
unprofessional or unwelcome in the community.

**Consequence**: A private, written warning from community leaders, providing
clarity around the nature of the violation and an explanation of why the
behavior was inappropriate. A public apology may be requested.

### 2. Warning

**Community Impact**: A violation through a single incident or series
of actions.

**Consequence**: A warning with consequences for continued behavior. No
interaction with the people involved, including unsolicited interaction with
those enforcing the Code of Conduct, for a specified period of time. This
includes avoiding interactions in community spaces as well as external channels
like social media. Violating these terms may lead to a temporary or
permanent ban.

### 3. Temporary Ban

**Community Impact**: A serious violation of community standards, including
sustained inappropriate behavior.

**Consequence**: A temporary ban from any sort of interaction or public
communication with the community for a specified period of time. No public or
private interaction with the people involved, including unsolicited interaction
with those enforcing the Code of Conduct, is allowed during this period.
Violating these terms may lead to a permanent ban.

### 4. Permanent Ban

**Community Impact**: Demonstrating a pattern of violation of community
standards, including sustained inappropriate behavior,  harassment of an
individual, or aggression toward or disparagement of classes of individuals.

**Consequence**: A permanent ban from any sort of public interaction within
the community.

## Attribution

This Code of Conduct is adapted from the [Contributor Covenant][homepage],
version 2.0, available at
https://www.contributor-covenant.org/version/2/0/code_of_conduct.html.

Community Impact Guidelines were inspired by [Mozilla's code of conduct
enforcement ladder](https://github.com/mozilla/diversity).

[homepage]: https://www.contributor-covenant.org

For answers to common questions about this code of conduct, see the FAQ at
https://www.contributor-covenant.org/faq. Translations are available at
https://www.contributor-covenant.org/translations.
```

## File: `Cargo.toml`
```
[workspace]

members = [
    "gping",
    "pinger"
]

[profile.release]
lto = true
codegen-units = 1
```

## File: `Cross.toml`
```
#[target."armv7-linux-androideabi"]
#pre-build = ["apt-get update && apt-get install --assume-yes iputils-ping"]
#
#[target."armv7-unknown-linux-gnueabihf"]
#pre-build = ["apt-get update && apt-get install --assume-yes iputils-ping"]
#
#[target."armv7-unknown-linux-musleabihf"]
#pre-build = ["apt-get update && apt-get install --assume-yes iputils-ping"]
#
#[target."aarch64-linux-android"]
#pre-build = ["apt-get update && apt-get install --assume-yes iputils-ping"]
#
#[target."aarch64-unknown-linux-gnu"]
#pre-build = ["apt-get update && apt-get install --assume-yes iputils-ping"]
#
#[target."aarch64-unknown-linux-musl"]
#pre-build = ["apt-get update && apt-get install --assume-yes iputils-ping"]
#
#[target."x86_64-unknown-linux-musl"]
#pre-build = ["apt-get update && apt-get install --assume-yes iputils-ping"]
#

[build]
pre-build = ["apt-get update && apt-get install --assume-yes iputils-ping"]

[build.env]
passthrough = ["CI", "GITHUB_ACTIONS"]
```

## File: `Dockerfile`
```
# syntax=docker/dockerfile:1

FROM rust:slim-bookworm AS builder

WORKDIR /usr/src/gping

COPY gping/ gping/
COPY pinger/ pinger/
COPY Cargo.* ./

RUN cargo install --locked --path ./gping


FROM debian:bookworm-slim

RUN apt-get update \
    && apt-get install -y iputils-ping \
    && rm -rf /var/lib/apt/lists/*

COPY --link --from=builder /usr/local/cargo/bin/gping /usr/local/bin/gping

ENTRYPOINT ["gping"]
```

## File: `LICENSE`
```
MIT License

Copyright (c) 2020 Tom Forbes

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## File: `gping.1`
```
.ie \n(.g .ds Aq \(aq
.el .ds Aq '
.TH gping 1  "gping " 
.SH NAME
gping \- Ping, but with a graph.
.SH SYNOPSIS
\fBgping\fR [\fB\-\-cmd\fR] [\fB\-n\fR|\fB\-\-watch\-interval\fR] [\fB\-b\fR|\fB\-\-buffer\fR] [\fB\-4 \fR] [\fB\-6 \fR] [\fB\-i\fR|\fB\-\-interface\fR] [\fB\-s\fR|\fB\-\-simple\-graphics\fR] [\fB\-\-vertical\-margin\fR] [\fB\-\-horizontal\-margin\fR] [\fB\-c\fR|\fB\-\-color\fR] [\fB\-\-clear\fR] [\fB\-\-ping\-args\fR] [\fB\-h\fR|\fB\-\-help\fR] [\fIHOSTS_OR_COMMANDS\fR] 
.SH DESCRIPTION
Ping, but with a graph.
.SH OPTIONS
.TP
\fB\-\-cmd\fR
Graph the execution time for a list of commands rather than pinging hosts
.TP
\fB\-n\fR, \fB\-\-watch\-interval\fR \fI<WATCH_INTERVAL>\fR
Watch interval seconds (provide partial seconds like \*(Aq0.5\*(Aq). Default for ping is 0.2, default for cmd is 0.5
.TP
\fB\-b\fR, \fB\-\-buffer\fR \fI<BUFFER>\fR [default: 30]
Determines the number of seconds to display in the graph
.TP
\fB\-4\fR
Resolve ping targets to IPv4 address
.TP
\fB\-6\fR
Resolve ping targets to IPv6 address
.TP
\fB\-i\fR, \fB\-\-interface\fR \fI<INTERFACE>\fR
Interface to use when pinging
.TP
\fB\-s\fR, \fB\-\-simple\-graphics\fR

.TP
\fB\-\-vertical\-margin\fR \fI<VERTICAL_MARGIN>\fR [default: 1]
Vertical margin around the graph (top and bottom)
.TP
\fB\-\-horizontal\-margin\fR \fI<HORIZONTAL_MARGIN>\fR [default: 0]
Horizontal margin around the graph (left and right)
.TP
\fB\-c\fR, \fB\-\-color\fR \fI<color>\fR
Assign color to a graph entry.

This option can be defined more than once as a comma separated string, and the
order which the colors are provided will be matched against the hosts or
commands passed to gping.

Hexadecimal RGB color codes are accepted in the form of \*(Aq#RRGGBB\*(Aq or the
following color names: \*(Aqblack\*(Aq, \*(Aqred\*(Aq, \*(Aqgreen\*(Aq, \*(Aqyellow\*(Aq, \*(Aqblue\*(Aq, \*(Aqmagenta\*(Aq,
\*(Aqcyan\*(Aq, \*(Aqgray\*(Aq, \*(Aqdark\-gray\*(Aq, \*(Aqlight\-red\*(Aq, \*(Aqlight\-green\*(Aq, \*(Aqlight\-yellow\*(Aq,
\*(Aqlight\-blue\*(Aq, \*(Aqlight\-magenta\*(Aq, \*(Aqlight\-cyan\*(Aq, and \*(Aqwhite\*(Aq
.TP
\fB\-\-clear\fR
Clear the graph from the terminal after closing the program
.TP
\fB\-\-ping\-args\fR [\fI<PING_ARGS>...\fR]
Extra arguments to pass to `ping`. These are platform dependent
.TP
\fB\-h\fR, \fB\-\-help\fR
Print help
.TP
[\fIHOSTS_OR_COMMANDS\fR]
Hosts or IPs to ping, or commands to run if \-\-cmd is provided. Can use cloud shorthands like aws:eu\-west\-1
.SH AUTHORS
Tom Forbes <tom@tomforb.es>
```

## File: `readme.md`
```markdown
# gping 🚀

[![Crates.io](https://img.shields.io/crates/v/gping.svg)](https://crates.io/crates/gping)
[![Actions Status](https://github.com/orf/gping/workflows/CI/badge.svg)](https://github.com/orf/gping/actions)

Ping, but with a graph.

![](./images/readme-example.gif)

Comes with the following super-powers:
* Graph the ping time for multiple hosts
* Graph the _execution time_ for commands via the `--cmd` flag
* Custom colours
* Windows, Mac and Linux support

Table of Contents
=================

   * [Install :cd:](#install-cd)
   * [Usage :saxophone:](#usage-saxophone)

<a href="https://repology.org/project/gping/versions">
    <img src="https://repology.org/badge/vertical-allrepos/gping.svg" alt="Packaging status" align="right">
</a>

# Install :cd:

* macOS
  * [Homebrew](https://formulae.brew.sh/formula/gping#default): `brew install gping`
  * [MacPorts](https://ports.macports.org/port/gping/): `sudo port install gping`
* Linux (Homebrew): `brew install gping`
* CentOS (and other distributions with an old glibc): Download the MUSL build from the latest release
* Windows/ARM:
  * Scoop: `scoop install gping`
  * Chocolatey: `choco install gping`
  * Download the latest release from [the github releases page](https://github.com/orf/gping/releases)
* Fedora ([COPR](https://copr.fedorainfracloud.org/coprs/atim/gping/)): `sudo dnf copr enable atim/gping -y && sudo dnf install gping`
* Cargo (**This requires `rustc` version 1.67.0 or greater**): `cargo install gping`
* Arch Linux: `pacman -S gping`
* Alpine linux: `apk add gping`
* Ubuntu >23.10/Debian >13: `apt install gping`
* Ubuntu/Debian ([Azlux's repo](https://packages.azlux.fr/)):
  ```bash
  echo 'deb [signed-by=/usr/share/keyrings/azlux.gpg] https://packages.azlux.fr/debian/ bookworm main' | sudo tee /etc/apt/sources.list.d/azlux.list
  sudo apt install gpg curl
  curl -s https://azlux.fr/repo.gpg.key | gpg --dearmor | sudo tee /usr/share/keyrings/azlux.gpg > /dev/null
  sudo apt update
  sudo apt install gping
  ```
* Gentoo ([dm9pZCAq overlay](https://github.com/gentoo-mirror/dm9pZCAq)):
  ```sh
  sudo eselect repository enable dm9pZCAq
  sudo emerge --sync dm9pZCAq
  sudo emerge net-misc/gping::dm9pZCAq
  ```
* FreeBSD:
  * [pkg](https://www.freshports.org/net-mgmt/gping/): `pkg install gping`
  * [ports](https://cgit.freebsd.org/ports/tree/net-mgmt/gping) `cd /usr/ports/net-mgmt/gping; make install clean`
* Docker:
  ```sh
  # Check all options
  docker run --rm -ti --network host ghcr.io/orf/gping:gping-v1.15.1 --help
  # Ping google.com
  docker run --rm -ti --network host ghcr.io/orf/gping:gping-v1.15.1 google.com
  ```
* Flox:
  ```sh
  # Inside of a Flox environment
  flox install gping
  ```
* [gah](https://github.com/marverix/gah):
  ```sh
  gah install gping
  ```

# Usage :saxophone:

Just run `gping [host]`. `host` can be a command like `curl google.com` if the `--cmd` flag is used. You can also use
shorthands like `aws:eu-west-1` or `aws:ca-central-1` to ping specific cloud regions. Only `aws` is currently supported.

```bash
$ gping --help
Ping, but with a graph.

Usage: gping [OPTIONS] [HOSTS_OR_COMMANDS]...

Arguments:
  [HOSTS_OR_COMMANDS]...  Hosts or IPs to ping, or commands to run if --cmd is provided. Can use cloud shorthands like aws:eu-west-1.

Options:
      --cmd
          Graph the execution time for a list of commands rather than pinging hosts
  -n, --watch-interval <WATCH_INTERVAL>
          Watch interval seconds (provide partial seconds like '0.5'). Default for ping is 0.2, default for cmd is 0.5.
  -b, --buffer <BUFFER>
          Determines the number of seconds to display in the graph. [default: 30]
  -4
          Resolve ping targets to IPv4 address
  -6
          Resolve ping targets to IPv6 address
  -i, --interface <INTERFACE>
          Interface to use when pinging
  -s, --simple-graphics
          Uses dot characters instead of braille
      --vertical-margin <VERTICAL_MARGIN>
          Vertical margin around the graph (top and bottom) [default: 1]
      --horizontal-margin <HORIZONTAL_MARGIN>
          Horizontal margin around the graph (left and right) [default: 0]
  -c, --color <color>
          Assign color to a graph entry. This option can be defined more than once as a comma separated string, and the order which the colors are provided will be matched against the hosts or commands passed to gping. Hexadecimal RGB color codes are accepted in the form of '#RRGGBB' or the following color names: 'black', 'red', 'green', 'yellow', 'blue', 'magenta','cyan', 'gray', 'dark-gray', 'light-red', 'light-green', 'light-yellow', 'light-blue', 'light-magenta', 'light-cyan', and 'white'
  -h, --help
          Print help information
  -V, --version
          Print version information
      --clear
          Clear the graph from the terminal after closing the program
```
```

## File: `gping/Cargo.toml`
```
[package]
name = "gping"
version = "1.20.1"
authors = ["Tom Forbes <tom@tomforb.es>"]
edition = "2018"
repository = "https://github.com/orf/gping"
license = "MIT"
description = "Ping, but with a graph."
build = "build.rs"
readme = "../readme.md"

[dependencies]
pinger = { version = "^2.1.1", path = "../pinger" }
tui = { package = "ratatui", version = "0.29.0", features = ["crossterm"], default-features = false }
crossterm = "0.29.0"
anyhow = "1.0.101"
chrono = "0.4.43"
itertools = "0.14.0"
shadow-rs = { version = "1.7.0", default-features = false }
const_format = "0.2.35"
clap = { version = "4.5.57", features = ["derive"] }
clap_mangen = "0.2.31"
idna = "1.1.0"
clap-cargo = "0.18.3"

[build-dependencies]
shadow-rs = { version = "1.7.0"}
```

## File: `gping/build.rs`
```rust
fn main() {
    shadow_rs::ShadowBuilder::builder().build().unwrap();
}
```

## File: `gping/src/colors.rs`
```rust
use std::{iter::Iterator, ops::RangeFrom, str::FromStr};

use anyhow::{anyhow, Result};
use tui::style::Color;

pub struct Colors<T> {
    already_used: Vec<Color>,
    color_names: T,
    indices: RangeFrom<u8>,
}

impl<T> From<T> for Colors<T> {
    fn from(color_names: T) -> Self {
        Self {
            already_used: Vec::new(),
            color_names,
            indices: 2..,
        }
    }
}

impl<'a, T> Iterator for Colors<T>
where
    T: Iterator<Item = &'a String>,
{
    type Item = Result<Color>;

    fn next(&mut self) -> Option<Self::Item> {
        match self.color_names.next() {
            Some(name) => match Color::from_str(name) {
                Ok(color) => {
                    if !self.already_used.contains(&color) {
                        self.already_used.push(color);
                    }
                    Some(Ok(color))
                }
                error => Some(error.map_err(|err| {
                    anyhow!(err).context(format!("Invalid color code: `{}`", name))
                })),
            },
            None => loop {
                let index = unsafe { self.indices.next().unwrap_unchecked() };
                let color = Color::Indexed(index);
                if !self.already_used.contains(&color) {
                    self.already_used.push(color);
                    break Some(Ok(color));
                }
            },
        }
    }
}
```

## File: `gping/src/main.rs`
```rust
use crate::plot_data::PlotData;
use anyhow::{anyhow, bail, Context, Result};
use chrono::prelude::*;
use clap::{CommandFactory, Parser};
use crossterm::event::KeyModifiers;
use crossterm::terminal::{EnterAlternateScreen, LeaveAlternateScreen};
use crossterm::{
    event::{self, Event as CEvent, KeyCode},
    execute,
    terminal::{disable_raw_mode, enable_raw_mode, SetSize},
};
use itertools::{Itertools, MinMaxResult};
use pinger::{ping, PingOptions, PingResult};
use std::io;
use std::io::BufWriter;
use std::iter;
use std::net::{IpAddr, ToSocketAddrs};
use std::ops::Add;
use std::path::Path;
use std::process::{Command, ExitStatus, Stdio};
use std::sync::atomic::{AtomicBool, Ordering};
use std::sync::mpsc::Sender;
use std::sync::{mpsc, Arc};
use std::thread;
use std::thread::{sleep, JoinHandle};
use std::time::{Duration, Instant};
use tui::backend::{Backend, CrosstermBackend};
use tui::layout::{Constraint, Direction, Flex, Layout};
use tui::style::{Color, Style};
use tui::text::Span;
use tui::widgets::{Axis, Block, Borders, Chart, Dataset};
use tui::Terminal;

mod colors;
mod plot_data;
mod region_map;

use colors::Colors;
use shadow_rs::{formatcp, shadow};
use tui::prelude::Position;

shadow!(build);

const VERSION_INFO: &str = formatcp!(
    r#"{}
commit_hash: {}
build_time: {}
build_env: {},{}"#,
    build::PKG_VERSION,
    build::SHORT_COMMIT,
    build::BUILD_TIME,
    build::RUST_VERSION,
    build::RUST_CHANNEL
);

#[derive(Parser, Debug)]
#[command(author, version=build::PKG_VERSION, name = "gping", about = "Ping, but with a graph.", long_version = VERSION_INFO, styles = clap_cargo::style::CLAP_STYLING
)]
struct Args {
    /// Graph the execution time for a list of commands rather than pinging hosts
    #[arg(long)]
    cmd: bool,

    /// Watch interval seconds (provide partial seconds like '0.5'). Default for ping is 0.2, default for cmd is 0.5.
    #[arg(short = 'n', long)]
    watch_interval: Option<f32>,

    /// Hosts or IPs to ping, or commands to run if --cmd is provided. Can use cloud shorthands like aws:eu-west-1.
    #[arg(allow_hyphen_values = false)]
    hosts_or_commands: Vec<String>,

    /// Determines the number of seconds to display in the graph.
    #[arg(short, long, default_value = "30")]
    buffer: u64,
    /// Resolve ping targets to IPv4 address
    #[arg(short = '4', conflicts_with = "ipv6")]
    ipv4: bool,
    /// Resolve ping targets to IPv6 address
    #[arg(short = '6', conflicts_with = "ipv4")]
    ipv6: bool,

    #[cfg(not(target_os = "windows"))]
    /// Interface to use when pinging.
    #[arg(short = 'i', long)]
    interface: Option<String>,

    /// Uses dot characters instead of braille
    #[arg(short = 's', long, help = "")]
    simple_graphics: bool,

    /// Vertical margin around the graph (top and bottom)
    #[arg(long, default_value = "1")]
    vertical_margin: u16,

    /// Horizontal margin around the graph (left and right)
    #[arg(long, default_value = "0")]
    horizontal_margin: u16,

    #[arg(
        name = "color",
        short = 'c',
        long = "color",
        use_value_delimiter = true,
        value_delimiter = ',',
        help = r#"Assign color to a graph entry.

This option can be defined more than once as a comma separated string, and the
order which the colors are provided will be matched against the hosts or
commands passed to gping.

Hexadecimal RGB color codes are accepted in the form of '#RRGGBB' or the
following color names: 'black', 'red', 'green', 'yellow', 'blue', 'magenta',
'cyan', 'gray', 'dark-gray', 'light-red', 'light-green', 'light-yellow',
'light-blue', 'light-magenta', 'light-cyan', and 'white'"#
    )]
    color_codes_or_names: Vec<String>,

    /// Clear the graph from the terminal after closing the program
    #[arg(name = "clear", long = "clear", action)]
    clear: bool,

    #[cfg(not(target_os = "windows"))]
    /// Extra arguments to pass to `ping`. These are platform dependent.
    #[arg(long, allow_hyphen_values = true, num_args = 0.., conflicts_with="cmd")]
    ping_args: Option<Vec<String>>,
}

struct App {
    data: Vec<PlotData>,
    display_interval: chrono::Duration,
    started: chrono::DateTime<Local>,
}

impl App {
    fn new(data: Vec<PlotData>, buffer: u64) -> Self {
        App {
            data,
            display_interval: chrono::Duration::from_std(Duration::from_secs(buffer)).unwrap(),
            started: Local::now(),
        }
    }

    fn update(&mut self, host_idx: usize, item: Option<Duration>) {
        let host = &mut self.data[host_idx];
        host.update(item);
    }

    fn y_axis_bounds(&self) -> [f64; 2] {
        // Find the Y axis bounds for our chart.
        // This is trickier than the x-axis. We iterate through all our PlotData structs
        // and find the min/max of all the values. Then we add a 10% buffer to them.
        let (min, max) = match self
            .data
            .iter()
            .flat_map(|b| b.data.as_slice())
            .map(|v| v.1)
            .filter(|v| !v.is_nan())
            .minmax()
        {
            MinMaxResult::NoElements => (f64::INFINITY, 0_f64),
            MinMaxResult::OneElement(elm) => (elm, elm),
            MinMaxResult::MinMax(min, max) => (min, max),
        };

        // Add a 10% buffer to the top and bottom
        let max_10_percent = (max * 10_f64) / 100_f64;
        let min_10_percent = (min * 10_f64) / 100_f64;
        [min - min_10_percent, max + max_10_percent]
    }

    fn x_axis_bounds(&self) -> [f64; 2] {
        let now = Local::now();
        let now_idx;
        let before_idx;
        if (now - self.started) < self.display_interval {
            now_idx = (self.started + self.display_interval).timestamp_millis() as f64 / 1_000f64;
            before_idx = self.started.timestamp_millis() as f64 / 1_000f64;
        } else {
            now_idx = now.timestamp_millis() as f64 / 1_000f64;
            let before = now - self.display_interval;
            before_idx = before.timestamp_millis() as f64 / 1_000f64;
        }

        [before_idx, now_idx]
    }

    fn x_axis_labels(&self, bounds: [f64; 2]) -> Vec<Span<'_>> {
        let lower_utc = DateTime::<Utc>::from_timestamp(bounds[0] as i64, 0)
            .expect("Error parsing x-axis bounds 0");
        let upper_utc = DateTime::<Utc>::from_timestamp(bounds[1] as i64, 0)
            .expect("Error parsing x-asis bounds 1");
        let lower: DateTime<Local> = DateTime::from(lower_utc);
        let upper: DateTime<Local> = DateTime::from(upper_utc);
        let diff = (upper - lower) / 2;
        let midpoint = lower + diff;
        vec![
            Span::raw(format!("{:?}", lower.time())),
            Span::raw(format!("{:?}", midpoint.time())),
            Span::raw(format!("{:?}", upper.time())),
        ]
    }

    fn y_axis_labels(&self, bounds: [f64; 2]) -> Vec<Span<'_>> {
        // Create 7 labels for our y axis, based on the y-axis bounds we computed above.
        let min = bounds[0];
        let max = bounds[1];

        let difference = max - min;
        let num_labels = 7;
        // Split difference into one chunk for each of the 7 labels
        let increment = Duration::from_micros((difference / num_labels as f64) as u64);
        let duration = Duration::from_micros(min as u64);

        (0..num_labels)
            .map(|i| Span::raw(format!("{:?}", duration.add(increment * i))))
            .collect()
    }
}

#[derive(Debug)]
enum Update {
    Result(Duration),
    Timeout,
    Unknown,
    Terminated(ExitStatus, String),
}

impl From<PingResult> for Update {
    fn from(result: PingResult) -> Self {
        match result {
            PingResult::Pong(duration, _) => Update::Result(duration),
            PingResult::Timeout(_) => Update::Timeout,
            PingResult::Unknown(_) => Update::Unknown,
            PingResult::PingExited(e, stderr) => Update::Terminated(e, stderr),
        }
    }
}

#[derive(Debug)]
enum Event {
    Update(usize, Update),
    Terminate,
    Render,
}

fn start_render_thread(
    kill_event: Arc<AtomicBool>,
    cmd_tx: Sender<Event>,
) -> JoinHandle<Result<()>> {
    thread::spawn(move || {
        while !kill_event.load(Ordering::Acquire) {
            sleep(Duration::from_millis(250));
            cmd_tx.send(Event::Render)?;
        }
        Ok(())
    })
}

fn start_cmd_thread(
    watch_cmd: &str,
    host_id: usize,
    watch_interval: Option<f32>,
    cmd_tx: Sender<Event>,
    kill_event: Arc<AtomicBool>,
) -> JoinHandle<Result<()>> {
    let mut words = watch_cmd.split_ascii_whitespace();
    let cmd = words
        .next()
        .expect("Must specify a command to watch")
        .to_string();
    let cmd_args = words.map(|w| w.to_string()).collect::<Vec<String>>();

    let interval = Duration::from_millis((watch_interval.unwrap_or(0.5) * 1000.0) as u64);

    // Pump cmd watches into the queue
    thread::spawn(move || -> Result<()> {
        while !kill_event.load(Ordering::Acquire) {
            let start = Instant::now();
            let mut child = Command::new(&cmd)
                .args(&cmd_args)
                .stderr(Stdio::null())
                .stdout(Stdio::null())
                .spawn()?;
            let status = child.wait()?;
            let duration = start.elapsed();
            let update = if status.success() {
                Update::Result(duration)
            } else {
                Update::Timeout
            };
            cmd_tx.send(Event::Update(host_id, update))?;
            sleep(interval);
        }
        Ok(())
    })
}

fn start_ping_thread(
    options: PingOptions,
    host_id: usize,
    ping_tx: Sender<Event>,
    kill_event: Arc<AtomicBool>,
) -> Result<JoinHandle<Result<()>>> {
    let stream = ping(options)?;
    // Pump ping messages into the queue
    Ok(thread::spawn(move || -> Result<()> {
        while !kill_event.load(Ordering::Acquire) {
            match stream.recv() {
                Ok(v) => {
                    ping_tx.send(Event::Update(host_id, v.into()))?;
                }
                Err(_) => {
                    // Stream closed, just break
                    return Ok(());
                }
            }
        }
        Ok(())
    }))
}

fn get_host_ipaddr(host: &str, force_ipv4: bool, force_ipv6: bool) -> Result<String> {
    let mut host = host.to_string();
    if !host.is_ascii() {
        let Ok(encoded_host) = idna::domain_to_ascii(&host) else {
            bail!("Could not encode host {host} to punycode")
        };
        host = encoded_host;
    }
    let ipaddr: Vec<_> = (host.as_str(), 80)
        .to_socket_addrs()
        .with_context(|| format!("Resolving {host}"))?
        .map(|s| s.ip())
        .collect();
    if ipaddr.is_empty() {
        bail!("Could not resolve hostname {}", host)
    }
    let ipaddr = if force_ipv4 {
        ipaddr
            .iter()
            .find(|ip| matches!(ip, IpAddr::V4(_)))
            .ok_or_else(|| anyhow!("Could not resolve '{}' to IPv4", host))
    } else if force_ipv6 {
        ipaddr
            .iter()
            .find(|ip| matches!(ip, IpAddr::V6(_)))
            .ok_or_else(|| anyhow!("Could not resolve '{}' to IPv6", host))
    } else {
        ipaddr
            .first()
            .ok_or_else(|| anyhow!("Could not resolve '{}' to IP", host))
    };
    Ok(ipaddr?.to_string())
}

fn generate_man_page(path: &Path) -> anyhow::Result<()> {
    let man = clap_mangen::Man::new(Args::command().version(None).long_version(None));
    let mut buffer: Vec<u8> = Default::default();
    man.render(&mut buffer)?;

    std::fs::write(path, buffer)?;
    Ok(())
}

fn main() -> Result<()> {
    if let Some(path) = std::env::var_os("GENERATE_MANPAGE") {
        return generate_man_page(Path::new(&path));
    };
    let args: Args = Args::parse();

    if args.hosts_or_commands.is_empty() {
        return Err(anyhow!("At least one host or command must be given (i.e gping google.com). Use --help for a full list of arguments."));
    }

    let mut data = vec![];

    let colors = Colors::from(args.color_codes_or_names.iter());
    let hosts_or_commands: Vec<String> = args
        .hosts_or_commands
        .clone()
        .into_iter()
        .map(|s| match region_map::try_host_from_cloud_region(&s) {
            None => s,
            Some(new_domain) => new_domain,
        })
        .collect();

    for (host_or_cmd, color) in hosts_or_commands.iter().zip(colors) {
        let color = color?;
        let display = match args.cmd {
            true => host_or_cmd.to_string(),
            false => format!(
                "{} ({})",
                host_or_cmd,
                get_host_ipaddr(host_or_cmd, args.ipv4, args.ipv6)?
            ),
        };
        data.push(PlotData::new(
            display,
            args.buffer,
            Style::default().fg(color),
            args.simple_graphics,
        ));
    }

    #[cfg(not(target_os = "windows"))]
    let interface: Option<String> = args.interface.clone();
    #[cfg(target_os = "windows")]
    let interface: Option<String> = None;

    #[cfg(not(target_os = "windows"))]
    let ping_args: Option<Vec<String>> = args.ping_args.clone();
    #[cfg(target_os = "windows")]
    let ping_args: Option<Vec<String>> = None;

    let (key_tx, rx) = mpsc::channel();

    let mut threads = vec![];

    let killed = Arc::new(AtomicBool::new(false));

    for (host_id, host_or_cmd) in hosts_or_commands.iter().cloned().enumerate() {
        if args.cmd {
            let cmd_thread = start_cmd_thread(
                &host_or_cmd,
                host_id,
                args.watch_interval,
                key_tx.clone(),
                std::sync::Arc::clone(&killed),
            );
            threads.push(cmd_thread);
        } else {
            let interval =
                Duration::from_millis((args.watch_interval.unwrap_or(0.2) * 1000.0) as u64);

            let mut ping_opts = if args.ipv4 {
                PingOptions::new_ipv4(host_or_cmd, interval, interface.clone())
            } else if args.ipv6 {
                PingOptions::new_ipv6(host_or_cmd, interval, interface.clone())
            } else {
                PingOptions::new(host_or_cmd, interval, interface.clone())
            };
            if let Some(ping_args) = &ping_args {
                ping_opts = ping_opts.with_raw_arguments(ping_args.clone());
            }

            threads.push(start_ping_thread(
                ping_opts,
                host_id,
                key_tx.clone(),
                std::sync::Arc::clone(&killed),
            )?);
        }
    }
    threads.push(start_render_thread(
        std::sync::Arc::clone(&killed),
        key_tx.clone(),
    ));

    let mut app = App::new(data, args.buffer);
    enable_raw_mode()?;
    let stdout = io::stdout();
    let mut backend = CrosstermBackend::new(BufWriter::with_capacity(1024 * 1024 * 4, stdout));
    let rect = backend.size()?;

    if args.clear {
        execute!(
            backend,
            SetSize(rect.width, rect.height),
            EnterAlternateScreen,
        )?;
    } else {
        execute!(backend, SetSize(rect.width, rect.height),)?;
    }

    let mut terminal = Terminal::new(backend)?;
    terminal.clear()?;

    // Pump keyboard messages into the queue
    let killed_thread = std::sync::Arc::clone(&killed);
    thread::spawn(move || -> Result<()> {
        while !killed_thread.load(Ordering::Acquire) {
            if event::poll(Duration::from_secs(5))? {
                if let CEvent::Key(key) = event::read()? {
                    match key.code {
                        KeyCode::Char('q') | KeyCode::Esc => {
                            key_tx.send(Event::Terminate)?;
                            break;
                        }
                        KeyCode::Char('c') if key.modifiers == KeyModifiers::CONTROL => {
                            key_tx.send(Event::Terminate)?;
                            break;
                        }
                        _ => {}
                    }
                }
            }
        }
        Ok(())
    });

    loop {
        match rx.recv()? {
            Event::Update(host_id, update) => {
                match update {
                    Update::Result(duration) => app.update(host_id, Some(duration)),
                    Update::Timeout => app.update(host_id, None),
                    Update::Unknown => (),
                    Update::Terminated(e, _) if e.success() => {
                        break;
                    }
                    Update::Terminated(e, stderr) => {
                        eprintln!("There was an error running ping: {e}\nStderr: {stderr}\n");
                        break;
                    }
                };
            }
            Event::Render => {
                terminal.draw(|f| {
                    let chunks = Layout::default()
                        .flex(Flex::Legacy)
                        .direction(Direction::Vertical)
                        .vertical_margin(args.vertical_margin)
                        .horizontal_margin(args.horizontal_margin)
                        .constraints(
                            std::iter::repeat_n(Constraint::Length(1), app.data.len())
                                .chain(iter::once(Constraint::Percentage(10)))
                                .collect::<Vec<_>>(),
                        )
                        .split(f.area());

                    let total_chunks = chunks.len();

                    let header_chunks = &chunks[0..total_chunks - 1];
                    let chart_chunk = &chunks[total_chunks - 1];

                    for (plot_data, chunk) in app.data.iter().zip(header_chunks) {
                        let header_layout = Layout::default()
                            .direction(Direction::Horizontal)
                            .constraints(
                                [
                                    Constraint::Percentage(30),
                                    Constraint::Percentage(10),
                                    Constraint::Percentage(10),
                                    Constraint::Percentage(10),
                                    Constraint::Percentage(10),
                                    Constraint::Percentage(10),
                                    Constraint::Percentage(10),
                                    Constraint::Percentage(10),
                                ]
                                .as_ref(),
                            )
                            .split(*chunk);

                        for (area, paragraph) in header_layout.iter().zip(plot_data.header_stats())
                        {
                            f.render_widget(paragraph, *area);
                        }
                    }

                    let datasets: Vec<Dataset> = app.data.iter().map(|d| d.into()).collect();

                    let y_axis_bounds = app.y_axis_bounds();
                    let x_axis_bounds = app.x_axis_bounds();

                    let chart = Chart::new(datasets)
                        .block(Block::default().borders(Borders::NONE))
                        .x_axis(
                            Axis::default()
                                .style(Style::default().fg(Color::Gray))
                                .bounds(x_axis_bounds)
                                .labels(app.x_axis_labels(x_axis_bounds)),
                        )
                        .y_axis(
                            Axis::default()
                                .style(Style::default().fg(Color::Gray))
                                .bounds(y_axis_bounds)
                                .labels(app.y_axis_labels(y_axis_bounds)),
                        );

                    f.render_widget(chart, *chart_chunk)
                })?;
            }
            Event::Terminate => {
                killed.store(true, Ordering::Release);
                break;
            }
        }
    }
    killed.store(true, Ordering::Relaxed);

    disable_raw_mode()?;
    execute!(terminal.backend_mut())?;
    terminal.show_cursor()?;

    let new_size = terminal.size()?;
    terminal.set_cursor_position(Position {
        x: new_size.width,
        y: new_size.height,
    })?;
    for thread in threads {
        thread.join().unwrap()?;
    }

    if args.clear {
        execute!(terminal.backend_mut(), LeaveAlternateScreen)?;
    };

    Ok(())
}
```

## File: `gping/src/plot_data.rs`
```rust
use anyhow::Context;
use chrono::prelude::*;
use core::option::Option;
use core::option::Option::{None, Some};
use core::time::Duration;
use itertools::Itertools;
use tui::style::Style;
use tui::symbols;
use tui::widgets::{Dataset, GraphType, Paragraph};

pub struct PlotData {
    pub display: String,
    pub data: Vec<(f64, f64)>,
    pub style: Style,
    buffer: chrono::Duration,
    simple_graphics: bool,
}

impl PlotData {
    pub fn new(display: String, buffer: u64, style: Style, simple_graphics: bool) -> PlotData {
        PlotData {
            display,
            data: Vec::with_capacity(150),
            style,
            buffer: chrono::Duration::try_seconds(buffer as i64)
                .with_context(|| format!("Error converting {buffer} to seconds"))
                .unwrap(),
            simple_graphics,
        }
    }
    pub fn update(&mut self, item: Option<Duration>) {
        let now = Local::now();
        let idx = now.timestamp_millis() as f64 / 1_000f64;
        match item {
            Some(dur) => self.data.push((idx, dur.as_micros() as f64)),
            None => self.data.push((idx, f64::NAN)),
        }
        // Find the last index that we should remove.
        let earliest_timestamp = (now - self.buffer).timestamp_millis() as f64 / 1_000f64;
        let last_idx = self
            .data
            .iter()
            .enumerate()
            .filter(|(_, (timestamp, _))| *timestamp < earliest_timestamp)
            .map(|(idx, _)| idx)
            .next_back();
        if let Some(idx) = last_idx {
            self.data.drain(0..idx).for_each(drop)
        }
    }

    pub fn header_stats(&self) -> Vec<Paragraph<'_>> {
        let ping_header = Paragraph::new(self.display.clone()).style(self.style);
        let items: Vec<&f64> = self
            .data
            .iter()
            .filter(|(_, x)| !x.is_nan())
            .map(|(_, v)| v)
            .sorted_by(|a, b| a.partial_cmp(b).unwrap_or(std::cmp::Ordering::Equal))
            .collect();
        if items.is_empty() {
            return vec![ping_header];
        }

        let min = **items.first().unwrap();
        let max = **items.last().unwrap();
        let avg = items.iter().copied().sum::<f64>() / items.len() as f64;
        let jtr = items
            .iter()
            .zip(items.iter().skip(1))
            .map(|(&prev, &curr)| (curr - prev).abs())
            .sum::<f64>()
            / (items.len() - 1) as f64;

        let percentile_position = 0.95 * items.len() as f32;
        let rounded_position = percentile_position.round() as usize;
        let p95 = items.get(rounded_position).map(|i| **i).unwrap_or(0f64);

        // count timeouts
        let to = self.data.iter().filter(|(_, x)| x.is_nan()).count();

        let last = self.data.last().unwrap_or(&(0f64, 0f64)).1;

        vec![
            ping_header,
            Paragraph::new(format!("last {:?}", Duration::from_micros(last as u64)))
                .style(self.style),
            Paragraph::new(format!("min {:?}", Duration::from_micros(min as u64)))
                .style(self.style),
            Paragraph::new(format!("max {:?}", Duration::from_micros(max as u64)))
                .style(self.style),
            Paragraph::new(format!("avg {:?}", Duration::from_micros(avg as u64)))
                .style(self.style),
            Paragraph::new(format!("jtr {:?}", Duration::from_micros(jtr as u64)))
                .style(self.style),
            Paragraph::new(format!("p95 {:?}", Duration::from_micros(p95 as u64)))
                .style(self.style),
            Paragraph::new(format!("t/o {to:?}")).style(self.style),
        ]
    }
}

impl<'a> From<&'a PlotData> for Dataset<'a> {
    fn from(plot: &'a PlotData) -> Self {
        let slice = plot.data.as_slice();
        Dataset::default()
            .marker(if plot.simple_graphics {
                symbols::Marker::Dot
            } else {
                symbols::Marker::Braille
            })
            .style(plot.style)
            .graph_type(GraphType::Line)
            .data(slice)
    }
}
```

## File: `gping/src/region_map.rs`
```rust
type Host = String;

pub fn try_host_from_cloud_region(query: &str) -> Option<Host> {
    match query.split_once(':') {
        Some(("aws", region)) => Some(format!("ec2.{region}.amazonaws.com")),
        Some(("gcp", "")) => Some("cloud.google.com".to_string()),
        Some(("gcp", region)) => Some(format!("storage.{region}.rep.googleapis.com")),
        _ => None,
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_host_from_aws() {
        assert_eq!(
            try_host_from_cloud_region("aws:eu-west-1"),
            Some("ec2.eu-west-1.amazonaws.com".to_string())
        );
    }

    #[test]
    fn test_host_from_gcp() {
        assert_eq!(
            try_host_from_cloud_region("gcp:me-central2"),
            Some("storage.me-central2.rep.googleapis.com".to_string())
        );
        assert_eq!(
            try_host_from_cloud_region("gcp:"),
            Some("cloud.google.com".to_string())
        );
    }

    #[test]
    fn test_host_from_foo() {
        assert_eq!(try_host_from_cloud_region("foo:bar"), None);
    }

    #[test]
    fn test_invalid_input() {
        assert_eq!(try_host_from_cloud_region("foo"), None);
    }
}
```

## File: `pinger/Cargo.toml`
```
[package]
name = "pinger"
version = "2.1.1"
authors = ["Tom Forbes <tom@tomforb.es>"]
edition = "2018"
license = "MIT"
description = "A small cross-platform library to execute the ping command and parse the output"
repository = "https://github.com/orf/gping/tree/master/pinger"

[dependencies]
thiserror = "2.0.18"
lazy-regex = "3.5.1"
rand = { version = "0.10.0", optional = true }

[target.'cfg(windows)'.dependencies]
winping = "0.10.1"

[dev-dependencies]
os_info = "3.14.0"
ntest = "0.9.5"
anyhow = "1.0.101"

[features]
default = []
fake-ping = ["rand"]
```

## File: `pinger/README.md`
```markdown
# pinger

> A small cross-platform library to execute the ping command and parse the output.

This crate is primarily built for use with `gping`, but it can also be used as a
standalone library.

This allows you to reliably ping hosts without having to worry about process permissions,
in a cross-platform manner on Windows, Linux and macOS.

## Usage

A full example of using the library can be found in the `examples/` directory, but the
interface is quite simple:

```rust
use std::time::Duration;
use pinger::{ping, PingOptions};

fn ping_google() {
    let options = PingOptions::new("google.com", Duration::from_secs(1), None);
    let stream = ping(options).expect("Error pinging");
    for message in stream {
        match message {
            pinger::PingResult::Pong(duration, _) => {
                println!("Duration: {:?}", duration)
            }
            _ => {} // Handle errors, log ping timeouts, etc.
        }
    }
}
```

## Adding pinger to your project.

`cargo add pinger`
```

## File: `pinger/examples/simple-ping.rs`
```rust
use pinger::{ping, PingOptions};

const LIMIT: usize = 3;

pub fn main() {
    let target = "tomforb.es".to_string();
    let interval = std::time::Duration::from_millis(500);
    let options = PingOptions::new(target, interval, None);
    let stream = ping(options).expect("Error pinging");
    for message in stream.into_iter().take(LIMIT) {
        match message {
            pinger::PingResult::Pong(duration, line) => {
                println!("Duration: {:?}\t\t(raw: {:?})", duration, line)
            }
            pinger::PingResult::Timeout(line) => println!("Timeout! (raw: {line:?})"),
            pinger::PingResult::Unknown(line) => println!("Unknown line: {:?}", line),
            pinger::PingResult::PingExited(code, stderr) => {
                panic!("Ping exited! Code: {:?}. Stderr: {:?}", code, stderr)
            }
        }
    }
}
```

## File: `pinger/src/bsd.rs`
```rust
use crate::{extract_regex, PingCreationError, PingOptions, PingResult, Pinger};
use lazy_regex::*;

pub static RE: Lazy<Regex> = lazy_regex!(r"time=(?:(?P<ms>[0-9]+).(?P<ns>[0-9]+)\s+ms)");

pub struct BSDPinger {
    options: PingOptions,
}

pub(crate) fn parse_bsd(line: String) -> Option<PingResult> {
    if line.starts_with("PING ") {
        return None;
    }
    if line.starts_with("Request timeout") {
        return Some(PingResult::Timeout(line));
    }
    extract_regex(&RE, line)
}

impl Pinger for BSDPinger {
    fn from_options(options: PingOptions) -> Result<Self, PingCreationError>
    where
        Self: Sized,
    {
        Ok(Self { options })
    }

    fn parse_fn(&self) -> fn(String) -> Option<PingResult> {
        parse_bsd
    }

    fn ping_args(&self) -> (&str, Vec<String>) {
        let mut args = vec![format!(
            "-i{:.1}",
            self.options.interval.as_millis() as f32 / 1_000_f32
        )];
        if let Some(interface) = &self.options.interface {
            args.push("-I".into());
            args.push(interface.clone());
        }
        if let Some(raw_args) = &self.options.raw_arguments {
            args.extend(raw_args.iter().cloned());
        }
        args.push(self.options.target.to_string());
        ("ping", args)
    }
}
```

## File: `pinger/src/fake.rs`
```rust
use crate::{PingCreationError, PingOptions, PingResult, Pinger};
use rand::prelude::*;
use rand::rng;
use std::sync::mpsc;
use std::sync::mpsc::Receiver;
use std::thread;
use std::time::Duration;

pub struct FakePinger {
    options: PingOptions,
}

impl Pinger for FakePinger {
    fn from_options(options: PingOptions) -> Result<Self, PingCreationError>
    where
        Self: Sized,
    {
        Ok(Self { options })
    }

    fn parse_fn(&self) -> fn(String) -> Option<PingResult> {
        unimplemented!("parse for FakeParser not implemented")
    }

    fn ping_args(&self) -> (&str, Vec<String>) {
        unimplemented!("ping_args not implemented for FakePinger")
    }

    fn start(&self) -> Result<Receiver<PingResult>, PingCreationError> {
        let (tx, rx) = mpsc::channel();
        let sleep_time = self.options.interval;

        thread::spawn(move || {
            let mut random = rng();
            loop {
                let fake_seconds = random.random_range(50..150);
                let ping_result = PingResult::Pong(
                    Duration::from_millis(fake_seconds),
                    format!("Fake ping line: {fake_seconds} ms"),
                );
                if tx.send(ping_result).is_err() {
                    break;
                }

                std::thread::sleep(sleep_time);
            }
        });

        Ok(rx)
    }
}
```

## File: `pinger/src/lib.rs`
```rust
/// Pinger
/// This crate exposes a simple function to ping remote hosts across different operating systems.
/// Example:
/// ```no_run
/// use std::time::Duration;
/// use pinger::{ping, PingResult, PingOptions};
/// let options = PingOptions::new("tomforb.es".to_string(), Duration::from_secs(1), None);
/// let stream = ping(options).expect("Error pinging");
/// for message in stream {
///     match message {
///         PingResult::Pong(duration, line) => println!("{:?} (line: {})", duration, line),
///         PingResult::Timeout(_) => println!("Timeout!"),
///         PingResult::Unknown(line) => println!("Unknown line: {}", line),
///         PingResult::PingExited(_code, _stderr) => {}
///     }
/// }
/// ```
use lazy_regex::Regex;
use std::ffi::OsStr;
use std::fmt::{Debug, Formatter};
use std::io::{BufRead, BufReader};
use std::process::{Child, Command, ExitStatus, Stdio};
use std::sync::{mpsc, Arc};
use std::time::Duration;
use std::{fmt, io, thread};
use target::Target;
use thiserror::Error;

#[cfg(unix)]
pub mod linux;
#[cfg(unix)]
pub mod macos;
#[cfg(windows)]
pub mod windows;

#[cfg(unix)]
mod bsd;
#[cfg(feature = "fake-ping")]
mod fake;
mod target;
#[cfg(test)]
mod test;

#[derive(Debug, Clone)]
pub struct PingOptions {
    pub target: Target,
    pub interval: Duration,
    pub interface: Option<String>,
    pub raw_arguments: Option<Vec<String>>,
}

impl PingOptions {
    pub fn with_raw_arguments(mut self, raw_arguments: Vec<impl ToString>) -> Self {
        self.raw_arguments = Some(
            raw_arguments
                .into_iter()
                .map(|item| item.to_string())
                .collect(),
        );
        self
    }
}

impl PingOptions {
    pub fn from_target(target: Target, interval: Duration, interface: Option<String>) -> Self {
        Self {
            target,
            interval,
            interface,
            raw_arguments: None,
        }
    }
    pub fn new(target: impl ToString, interval: Duration, interface: Option<String>) -> Self {
        Self::from_target(Target::new_any(target), interval, interface)
    }

    pub fn new_ipv4(target: impl ToString, interval: Duration, interface: Option<String>) -> Self {
        Self::from_target(Target::new_ipv4(target), interval, interface)
    }

    pub fn new_ipv6(target: impl ToString, interval: Duration, interface: Option<String>) -> Self {
        Self::from_target(Target::new_ipv6(target), interval, interface)
    }
}

pub fn run_ping(
    cmd: impl AsRef<OsStr> + Debug,
    args: Vec<impl AsRef<OsStr> + Debug>,
) -> Result<Child, PingCreationError> {
    Ok(Command::new(cmd.as_ref())
        .args(&args)
        .stdout(Stdio::piped())
        .stderr(Stdio::piped())
        // Required to ensure that the output is formatted in the way we expect, not
        // using locale specific delimiters.
        .env("LANG", "C")
        .env("LC_ALL", "C")
        .spawn()?)
}

pub(crate) fn extract_regex(regex: &Regex, line: String) -> Option<PingResult> {
    let cap = regex.captures(&line)?;
    let ms = cap
        .name("ms")
        .expect("No capture group named 'ms'")
        .as_str()
        .parse::<u64>()
        .ok()?;
    let ns = match cap.name("ns") {
        None => 0,
        Some(cap) => {
            let matched_str = cap.as_str();
            let number_of_digits = matched_str.len() as u32;
            let fractional_ms = matched_str.parse::<u64>().ok()?;
            fractional_ms * (10u64.pow(6 - number_of_digits))
        }
    };
    let duration = Duration::from_millis(ms) + Duration::from_nanos(ns);
    Some(PingResult::Pong(duration, line))
}

pub trait Pinger: Send + Sync {
    fn from_options(options: PingOptions) -> std::result::Result<Self, PingCreationError>
    where
        Self: Sized;

    fn parse_fn(&self) -> fn(String) -> Option<PingResult>;

    fn ping_args(&self) -> (&str, Vec<String>);

    fn start(&self) -> Result<mpsc::Receiver<PingResult>, PingCreationError> {
        let (tx, rx) = mpsc::channel();
        let (cmd, args) = self.ping_args();

        let mut child = run_ping(cmd, args)?;
        let stdout = child.stdout.take().expect("child did not have a stdout");

        let parse_fn = self.parse_fn();

        thread::spawn(move || {
            let reader = BufReader::new(stdout).lines();
            for line in reader {
                match line {
                    Ok(msg) => {
                        if let Some(result) = parse_fn(msg) {
                            if tx.send(result).is_err() {
                                break;
                            }
                        }
                    }
                    Err(_) => break,
                }
            }
            let result = child.wait_with_output().expect("Child wasn't started?");
            let decoded_stderr = String::from_utf8(result.stderr).expect("Error decoding stderr");
            let _ = tx.send(PingResult::PingExited(result.status, decoded_stderr));
        });

        Ok(rx)
    }
}

#[derive(Debug)]
pub enum PingResult {
    Pong(Duration, String),
    Timeout(String),
    Unknown(String),
    PingExited(ExitStatus, String),
}

impl fmt::Display for PingResult {
    fn fmt(&self, f: &mut Formatter<'_>) -> fmt::Result {
        match &self {
            PingResult::Pong(duration, _) => write!(f, "{duration:?}"),
            PingResult::Timeout(_) => write!(f, "Timeout"),
            PingResult::Unknown(_) => write!(f, "Unknown"),
            PingResult::PingExited(status, stderr) => write!(f, "Exited({status}, {stderr})"),
        }
    }
}

#[derive(Error, Debug)]
pub enum PingCreationError {
    #[error("Could not detect ping. Stderr: {stderr:?}\nStdout: {stdout:?}")]
    UnknownPing {
        stderr: Vec<String>,
        stdout: Vec<String>,
    },
    #[error("Error spawning ping: {0}")]
    SpawnError(#[from] io::Error),

    #[error("Installed ping is not supported: {alternative}")]
    NotSupported { alternative: String },

    #[error("Invalid or unresolvable hostname {0}")]
    HostnameError(String),
}

pub fn get_pinger(options: PingOptions) -> std::result::Result<Arc<dyn Pinger>, PingCreationError> {
    #[cfg(feature = "fake-ping")]
    if std::env::var("PINGER_FAKE_PING")
        .map(|e| e == "1")
        .unwrap_or_default()
    {
        return Ok(Arc::new(fake::FakePinger::from_options(options)?));
    }

    #[cfg(windows)]
    {
        return Ok(Arc::new(windows::WindowsPinger::from_options(options)?));
    }
    #[cfg(unix)]
    {
        if cfg!(target_os = "freebsd")
            || cfg!(target_os = "dragonfly")
            || cfg!(target_os = "openbsd")
            || cfg!(target_os = "netbsd")
        {
            Ok(Arc::new(bsd::BSDPinger::from_options(options)?))
        } else if cfg!(target_os = "macos") {
            Ok(Arc::new(macos::MacOSPinger::from_options(options)?))
        } else {
            Ok(Arc::new(linux::LinuxPinger::from_options(options)?))
        }
    }
}

/// Start pinging a an address. The address can be either a hostname or an IP address.
pub fn ping(
    options: PingOptions,
) -> std::result::Result<mpsc::Receiver<PingResult>, PingCreationError> {
    let pinger = get_pinger(options)?;
    pinger.start()
}
```

## File: `pinger/src/linux.rs`
```rust
use crate::{extract_regex, run_ping, PingCreationError, PingOptions, PingResult, Pinger};
use lazy_regex::*;

pub static UBUNTU_RE: Lazy<Regex> = lazy_regex!(r"(?i-u)time=(?P<ms>\d+)(?:\.(?P<ns>\d+))? *ms");

#[derive(Debug)]
pub enum LinuxPinger {
    // Alpine
    BusyBox(PingOptions),
    // Debian, Ubuntu, etc
    IPTools(PingOptions),
}

impl LinuxPinger {
    pub fn detect_platform_ping(options: PingOptions) -> Result<Self, PingCreationError> {
        let child = run_ping("ping", vec!["-V".to_string()])?;
        let output = child.wait_with_output()?;
        let stdout = String::from_utf8(output.stdout).expect("Error decoding ping stdout");
        let stderr = String::from_utf8(output.stderr).expect("Error decoding ping stderr");

        if stderr.contains("BusyBox") {
            Ok(LinuxPinger::BusyBox(options))
        } else if stdout.contains("iputils") {
            Ok(LinuxPinger::IPTools(options))
        } else if stdout.contains("inetutils") {
            Err(PingCreationError::NotSupported {
                alternative: "Please use iputils ping, not inetutils.".to_string(),
            })
        } else {
            let first_two_lines_stderr: Vec<String> =
                stderr.lines().take(2).map(str::to_string).collect();
            let first_two_lines_stout: Vec<String> =
                stdout.lines().take(2).map(str::to_string).collect();
            Err(PingCreationError::UnknownPing {
                stdout: first_two_lines_stout,
                stderr: first_two_lines_stderr,
            })
        }
    }
}

impl Pinger for LinuxPinger {
    fn from_options(options: PingOptions) -> Result<Self, PingCreationError>
    where
        Self: Sized,
    {
        Self::detect_platform_ping(options)
    }

    fn parse_fn(&self) -> fn(String) -> Option<PingResult> {
        |line| {
            #[cfg(test)]
            eprintln!("Got line {line}");
            if line.starts_with("64 bytes from") {
                return extract_regex(&UBUNTU_RE, line);
            } else if line.starts_with("no answer yet") {
                return Some(PingResult::Timeout(line));
            }
            None
        }
    }

    fn ping_args(&self) -> (&str, Vec<String>) {
        match self {
            // Alpine doesn't support timeout notifications, so we don't add the -O flag here.
            LinuxPinger::BusyBox(options) => {
                let cmd = if options.target.is_ipv6() {
                    "ping6"
                } else {
                    "ping"
                };

                let mut args = vec![
                    options.target.to_string(),
                    format!("-i{:.1}", options.interval.as_millis() as f32 / 1_000_f32),
                ];

                if let Some(raw_args) = &options.raw_arguments {
                    args.extend(raw_args.iter().cloned());
                }

                (cmd, args)
            }
            LinuxPinger::IPTools(options) => {
                let cmd = if options.target.is_ipv6() {
                    "ping6"
                } else {
                    "ping"
                };

                // The -O flag ensures we "no answer yet" messages from ping
                // See https://superuser.com/questions/270083/linux-ping-show-time-out
                let mut args = vec![
                    "-O".to_string(),
                    format!("-i{:.1}", options.interval.as_millis() as f32 / 1_000_f32),
                ];
                if let Some(interface) = &options.interface {
                    args.push("-I".into());
                    args.push(interface.clone());
                }
                if let Some(raw_args) = &options.raw_arguments {
                    args.extend(raw_args.iter().cloned());
                }

                args.push(options.target.to_string());
                (cmd, args)
            }
        }
    }
}

#[cfg(test)]
mod tests {
    #[test]
    #[cfg(target_os = "linux")]
    fn test_linux_detection() {
        use super::*;
        use os_info::Type;
        use std::time::Duration;

        let platform = LinuxPinger::detect_platform_ping(PingOptions::new(
            "foo.com".to_string(),
            Duration::from_secs(1),
            None,
        ))
        .unwrap();
        match os_info::get().os_type() {
            Type::Alpine => {
                assert!(matches!(platform, LinuxPinger::BusyBox(_)))
            }
            Type::Ubuntu => {
                assert!(matches!(platform, LinuxPinger::IPTools(_)))
            }
            _ => {}
        }
    }
}
```

## File: `pinger/src/macos.rs`
```rust
use crate::bsd::parse_bsd;
use crate::{PingCreationError, PingOptions, PingResult, Pinger};
use lazy_regex::*;

pub static RE: Lazy<Regex> = lazy_regex!(r"time=(?:(?P<ms>[0-9]+).(?P<ns>[0-9]+)\s+ms)");

pub struct MacOSPinger {
    options: PingOptions,
}

impl Pinger for MacOSPinger {
    fn from_options(options: PingOptions) -> Result<Self, PingCreationError>
    where
        Self: Sized,
    {
        Ok(Self { options })
    }

    fn parse_fn(&self) -> fn(String) -> Option<PingResult> {
        parse_bsd
    }

    fn ping_args(&self) -> (&str, Vec<String>) {
        let cmd = if self.options.target.is_ipv6() {
            "ping6"
        } else {
            "ping"
        };
        let mut args = vec![
            format!(
                "-i{:.1}",
                self.options.interval.as_millis() as f32 / 1_000_f32
            ),
            self.options.target.to_string(),
        ];
        if let Some(interface) = &self.options.interface {
            args.push("-b".into());
            args.push(interface.clone());
        }

        if let Some(raw_args) = &self.options.raw_arguments {
            args.extend(raw_args.iter().cloned());
        }

        (cmd, args)
    }
}
```

## File: `pinger/src/target.rs`
```rust
use std::fmt;
use std::fmt::{Display, Formatter};
use std::net::{IpAddr, Ipv4Addr, Ipv6Addr};

#[derive(Debug, Copy, Clone, Eq, PartialEq)]
pub enum IPVersion {
    V4,
    V6,
    Any,
}

#[derive(Debug, Clone)]
pub enum Target {
    IP(IpAddr),
    Hostname { domain: String, version: IPVersion },
}

impl Target {
    pub fn is_ipv6(&self) -> bool {
        match self {
            Target::IP(ip) => ip.is_ipv6(),
            Target::Hostname { version, .. } => *version == IPVersion::V6,
        }
    }

    pub fn new_any(value: impl ToString) -> Self {
        let value = value.to_string();
        if let Ok(ip) = value.parse::<IpAddr>() {
            return Self::IP(ip);
        }
        Self::Hostname {
            domain: value,
            version: IPVersion::Any,
        }
    }

    pub fn new_ipv4(value: impl ToString) -> Self {
        let value = value.to_string();
        if let Ok(ip) = value.parse::<Ipv4Addr>() {
            return Self::IP(IpAddr::V4(ip));
        }
        Self::Hostname {
            domain: value.to_string(),
            version: IPVersion::V4,
        }
    }

    pub fn new_ipv6(value: impl ToString) -> Self {
        let value = value.to_string();
        if let Ok(ip) = value.parse::<Ipv6Addr>() {
            return Self::IP(IpAddr::V6(ip));
        }
        Self::Hostname {
            domain: value.to_string(),
            version: IPVersion::V6,
        }
    }
}

impl Display for Target {
    fn fmt(&self, f: &mut Formatter<'_>) -> fmt::Result {
        match self {
            Target::IP(v) => Display::fmt(&v, f),
            Target::Hostname { domain, .. } => Display::fmt(&domain, f),
        }
    }
}
```

## File: `pinger/src/test.rs`
```rust
#[cfg(test)]
mod tests {
    #[cfg(unix)]
    use crate::bsd::BSDPinger;
    #[cfg(unix)]
    use crate::linux::LinuxPinger;
    #[cfg(unix)]
    use crate::macos::MacOSPinger;
    #[cfg(windows)]
    use crate::windows::WindowsPinger;
    use crate::{PingOptions, PingResult, Pinger};
    use anyhow::bail;
    use ntest::timeout;
    use std::time::Duration;

    const IS_GHA: bool = option_env!("GITHUB_ACTIONS").is_some();

    #[test]
    #[timeout(20_000)]
    fn test_integration_any() {
        run_integration_test(PingOptions::new(
            "tomforb.es",
            Duration::from_millis(500),
            None,
        ))
        .unwrap();
    }
    #[test]
    #[timeout(20_000)]
    fn test_integration_ipv4() {
        run_integration_test(PingOptions::new_ipv4(
            "tomforb.es",
            Duration::from_millis(500),
            None,
        ))
        .unwrap();
    }
    #[test]
    #[timeout(20_000)]
    fn test_integration_ip6() {
        let res = run_integration_test(PingOptions::new_ipv6(
            "tomforb.es",
            Duration::from_millis(500),
            None,
        ));
        // ipv6 tests are allowed to fail on Gitlab CI, as it doesn't support ipv6, apparently.
        if !IS_GHA {
            res.unwrap();
        }
    }

    fn run_integration_test(options: PingOptions) -> anyhow::Result<()> {
        let stream = crate::ping(options.clone())?;

        let mut success = 0;
        let mut errors = 0;

        for message in stream.into_iter().take(3) {
            match message {
                PingResult::Pong(_, m) | PingResult::Timeout(m) => {
                    eprintln!("Message: {}", m);
                    success += 1;
                }
                PingResult::Unknown(line) => {
                    eprintln!("Unknown line: {}", line);
                    errors += 1;
                }
                PingResult::PingExited(code, stderr) => {
                    bail!("Ping exited with code: {}, stderr: {}", code, stderr);
                }
            }
        }
        assert_eq!(success, 3, "Success != 3 with opts {options:?}");
        assert_eq!(errors, 0, "Errors != 0 with opts {options:?}");
        Ok(())
    }

    fn opts() -> PingOptions {
        PingOptions::new("foo".to_string(), Duration::from_secs(1), None)
    }

    fn test_parser<T: Pinger>(contents: &str) {
        let pinger = T::from_options(opts()).unwrap();
        run_parser_test(contents, &pinger);
    }

    fn run_parser_test(contents: &str, pinger: &impl Pinger) {
        let parser = pinger.parse_fn();
        let test_file: Vec<&str> = contents.split("-----").collect();
        let input = test_file[0].trim().split('\n');
        let expected: Vec<&str> = test_file[1].trim().split('\n').collect();
        let parsed: Vec<Option<PingResult>> = input.map(|l| parser(l.to_string())).collect();

        assert_eq!(
            parsed.len(),
            expected.len(),
            "Parsed: {:?}, Expected: {:?}",
            &parsed,
            &expected
        );

        for (idx, (output, expected)) in parsed.into_iter().zip(expected).enumerate() {
            if let Some(value) = output {
                assert_eq!(
                    format!("{value}").trim(),
                    expected.trim(),
                    "Failed at idx {idx}"
                )
            } else {
                assert_eq!("None", expected.trim(), "Failed at idx {idx}")
            }
        }
    }

    #[cfg(unix)]
    #[test]
    fn macos() {
        test_parser::<MacOSPinger>(include_str!("tests/macos.txt"));
    }

    #[cfg(unix)]
    #[test]
    fn freebsd() {
        test_parser::<BSDPinger>(include_str!("tests/bsd.txt"));
    }

    #[cfg(unix)]
    #[test]
    fn dragonfly() {
        test_parser::<BSDPinger>(include_str!("tests/bsd.txt"));
    }

    #[cfg(unix)]
    #[test]
    fn openbsd() {
        test_parser::<BSDPinger>(include_str!("tests/bsd.txt"));
    }

    #[cfg(unix)]
    #[test]
    fn netbsd() {
        test_parser::<BSDPinger>(include_str!("tests/bsd.txt"));
    }

    #[cfg(unix)]
    #[test]
    fn ubuntu() {
        run_parser_test(
            include_str!("tests/ubuntu.txt"),
            &LinuxPinger::IPTools(opts()),
        );
    }

    #[cfg(unix)]
    #[test]
    fn debian() {
        run_parser_test(
            include_str!("tests/debian.txt"),
            &LinuxPinger::IPTools(opts()),
        );
    }

    #[cfg(windows)]
    #[test]
    fn windows() {
        test_parser::<WindowsPinger>(include_str!("tests/windows.txt"));
    }

    #[cfg(unix)]
    #[test]
    fn android() {
        run_parser_test(
            include_str!("tests/android.txt"),
            &LinuxPinger::BusyBox(opts()),
        );
    }

    #[cfg(unix)]
    #[test]
    fn alpine() {
        run_parser_test(
            include_str!("tests/alpine.txt"),
            &LinuxPinger::BusyBox(opts()),
        );
    }
}
```

## File: `pinger/src/windows.rs`
```rust
use crate::target::{IPVersion, Target};
use crate::PingCreationError;
use crate::{extract_regex, PingOptions, PingResult, Pinger};
use lazy_regex::*;
use std::net::{IpAddr, ToSocketAddrs};
use std::sync::mpsc;
use std::thread;
use std::time::Duration;
use winping::{Buffer, Pinger as WinPinger};

pub static RE: Lazy<Regex> = lazy_regex!(r"(?ix-u)time=(?P<ms>\d+)(?:\.(?P<ns>\d+))?");

pub struct WindowsPinger {
    options: PingOptions,
}

impl Pinger for WindowsPinger {
    fn from_options(options: PingOptions) -> Result<Self, PingCreationError> {
        Ok(Self { options })
    }

    fn parse_fn(&self) -> fn(String) -> Option<PingResult> {
        |line| {
            if line.contains("timed out") || line.contains("failure") {
                return Some(PingResult::Timeout(line));
            }
            extract_regex(&RE, line)
        }
    }

    fn ping_args(&self) -> (&str, Vec<String>) {
        unimplemented!("ping_args for WindowsPinger is not implemented")
    }

    fn start(&self) -> Result<mpsc::Receiver<PingResult>, PingCreationError> {
        let interval = self.options.interval;
        let parsed_ip = match &self.options.target {
            Target::IP(ip) => ip.clone(),
            Target::Hostname { domain, version } => {
                let ips = (domain.as_str(), 0).to_socket_addrs()?;
                let selected_ips: Vec<_> = if *version == IPVersion::Any {
                    ips.collect()
                } else {
                    ips.into_iter()
                        .filter(|addr| {
                            if *version == IPVersion::V6 {
                                matches!(addr.ip(), IpAddr::V6(_))
                            } else {
                                matches!(addr.ip(), IpAddr::V4(_))
                            }
                        })
                        .collect()
                };
                if selected_ips.is_empty() {
                    return Err(PingCreationError::HostnameError(domain.clone()).into());
                }
                selected_ips[0].ip()
            }
        };

        let (tx, rx) = mpsc::channel();

        thread::spawn(move || {
            let pinger = WinPinger::new().expect("Failed to create a WinPinger instance");
            let mut buffer = Buffer::new();
            loop {
                match pinger.send(parsed_ip.clone(), &mut buffer) {
                    Ok(rtt) => {
                        if tx
                            .send(PingResult::Pong(
                                Duration::from_millis(rtt as u64),
                                "".to_string(),
                            ))
                            .is_err()
                        {
                            break;
                        }
                    }
                    Err(_) => {
                        // Fuck it. All errors are timeouts. Why not.
                        if tx.send(PingResult::Timeout("".to_string())).is_err() {
                            break;
                        }
                    }
                }
                thread::sleep(interval);
            }
        });

        Ok(rx)
    }
}
```

## File: `pinger/src/tests/alpine.txt`
```
PING google.com (142.250.178.14): 56 data bytes
64 bytes from 142.250.178.14: seq=0 ttl=37 time=19.236 ms
64 bytes from 142.250.178.14: seq=1 ttl=37 time=19.319 ms
64 bytes from 142.250.178.14: seq=2 ttl=37 time=17.944 ms
ping: sendto: Network unreachable
-----

None
19.236ms
19.319ms
17.944ms
None
```

## File: `pinger/src/tests/android.txt`
```
PING google.com (172.217.173.46) 56(84) bytes of data.
64 bytes from bog02s12-in-f14.1e100.net (172.217.173.46): icmp_seq=1 ttl=110 time=106 ms
64 bytes from bog02s12-in-f14.1e100.net (172.217.173.46): icmp_seq=2 ttl=110 time=142 ms
64 bytes from bog02s12-in-f14.1e100.net (172.217.173.46): icmp_seq=3 ttl=110 time=244 ms
64 bytes from bog02s12-in-f14.1e100.net (172.217.173.46): icmp_seq=4 ttl=110 time=120 ms
64 bytes from bog02s12-in-f14.1e100.net (172.217.173.46): icmp_seq=5 ttl=110 time=122 ms
64 bytes from 172.217.173.46: icmp_seq=6 ttl=110 time=246 ms

--- google.com ping statistics ---
6 packets transmitted, 6 received, 0% packet loss, time 5018ms
rtt min/avg/max/mdev = 106.252/163.821/246.851/58.823 ms

-----

None
106ms
142ms
244ms
120ms
122ms
246ms
None
None
None
None
```

## File: `pinger/src/tests/bsd.txt`
```
PING google.com (216.58.198.174): 56 data bytes
64 bytes from 96.47.72.84: icmp_seq=0 ttl=50 time=111.525 ms
ping: sendto: Host is down
64 bytes from 96.47.72.84: icmp_seq=1 ttl=50 time=110.395 ms
ping: sendto: No route to host

-----

None
111.525ms
None
110.395ms
None
```

## File: `pinger/src/tests/debian.txt`
```
PING google.com (216.58.209.78): 56 data bytes
64 bytes from 216.58.209.78: icmp_seq=0 ttl=37 time=21.308 ms
64 bytes from 216.58.209.78: icmp_seq=1 ttl=37 time=15.769 ms
^C--- google.com ping statistics ---
8 packets transmitted, 8 packets received, 0% packet loss
round-trip min/avg/max/stddev = 15.282/20.347/41.775/8.344 ms

-----

None
21.308ms
15.769ms
None
None
None
```

## File: `pinger/src/tests/macos.txt`
```
PING google.com (216.58.209.78): 56 data bytes
64 bytes from 216.58.209.78: icmp_seq=0 ttl=119 time=14.621 ms
64 bytes from 216.58.209.78: icmp_seq=1 ttl=119 time=33.898 ms
64 bytes from 216.58.209.78: icmp_seq=2 ttl=119 time=17.305 ms
64 bytes from 216.58.209.78: icmp_seq=3 ttl=119 time=24.235 ms
64 bytes from 216.58.209.78: icmp_seq=4 ttl=119 time=15.242 ms
64 bytes from 216.58.209.78: icmp_seq=5 ttl=119 time=16.639 ms
Request timeout for icmp_seq 19
Request timeout for icmp_seq 20
Request timeout for icmp_seq 21
64 bytes from 216.58.209.78: icmp_seq=30 ttl=119 time=16.943 ms

-----

None
14.621ms
33.898ms
17.305ms
24.235ms
15.242ms
16.639ms
Timeout
Timeout
Timeout
16.943ms
```

## File: `pinger/src/tests/ubuntu.txt`
```
PING google.com (216.58.209.78) 56(84) bytes of data.
64 bytes from mad07s22-in-f14.1e100.net (216.58.209.78): icmp_seq=1 ttl=37 time=25.1 ms
64 bytes from mad07s22-in-f14.1e100.net (216.58.209.78): icmp_seq=2 ttl=37 time=19.4 ms
64 bytes from mad07s22-in-f14.1e100.net (216.58.209.78): icmp_seq=3 ttl=37 time=14.9 ms
64 bytes from mad07s22-in-f14.1e100.net (216.58.209.78): icmp_seq=4 ttl=37 time=22.8 ms
64 bytes from mad07s22-in-f14.1e100.net (216.58.209.78): icmp_seq=5 ttl=37 time=13.9 ms
64 bytes from mad07s22-in-f14.1e100.net (216.58.209.78): icmp_seq=6 ttl=37 time=77.6 ms
64 bytes from mad07s22-in-f14.1e100.net (216.58.209.78): icmp_seq=7 ttl=37 time=158 ms
no answer yet for icmp_seq=8
no answer yet for icmp_seq=9
64 bytes from mad07s22-in-f14.1e100.net (216.58.209.78): icmp_seq=18 ttl=37 time=357 ms
64 bytes from mad07s22-in-f14.1e100.net (216.58.209.78): icmp_seq=19 ttl=37 time=85.2 ms
64 bytes from mad07s22-in-f14.1e100.net (216.58.209.78): icmp_seq=20 ttl=37 time=17.8 ms

-----

None
25.1ms
19.4ms
14.9ms
22.8ms
13.9ms
77.6ms
158ms
Timeout
Timeout
357ms
85.2ms
17.8ms
```

## File: `pinger/src/tests/windows.txt`
```
pinging example.microsoft.com [192.168.239.132] with 32 bytes of data:
Reply from 192.168.239.132: bytes=32 time=101ms TTL=124
Reply from 192.168.239.132: bytes=32 time=100ms TTL=124
Reply from 192.168.239.132: bytes=32 time=120ms TTL=124
Reply from 192.168.239.132: bytes=32 time=120ms TTL=124
Request timed out.
Request timed out.
Reply from 192.168.239.132: bytes=32 time=120ms TTL=124

-----

None
101ms
100ms
120ms
120ms
Timeout
Timeout
120ms
```

