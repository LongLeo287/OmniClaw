---
id: github.com-ys-l-csvlens-09d3514c-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:45.907730
---

# KNOWLEDGE EXTRACT: github.com_YS-L_csvlens_09d3514c
> **Extracted on:** 2026-04-01 10:26:35
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007520869/github.com_YS-L_csvlens_09d3514c

---

## File: `.gitignore`
```
/target

.vscode
```

## File: `CHANGELOG.md`
```markdown
# v0.15.1

* Fix potential blank table when streaming input from stdin (#183)
* Fix incorrectly truncated fields when search regex is empty (#184)

# v0.15.0

* Add `--auto-reload` option to automatically reload content on file change (#79)
* Stream data from stdin by default (disable with `--no-streaming-stdin`) (#81)
* Support visually marking rows (toggle: `m`; clear all marks: `M`) (#166 by @giantatwork)
* Preserve selected row after filter is cleared (#170)
* Fix search from current cursor for larger files (#165)
* Fix row selection when scrolling to rows near bottom (#168)
* Fix potential freeze when the underlying file changes unexpectedly

# v0.14.0

* Support natural sorting via `Ctrl + j` (#143 by @jqnatividad):

  ![natural_sort](.github/demos/0.14.0-natural-sort.png)

* Add `--wrap chars` (or `-S`) and `--wrap words` (or `-W`) options to set the default wrapping mode

* Make auto-delimiter the default. Use `-c` or `--comma-separated` to force a comma delimiter (#51)

* Find command now searches from the current cursor (#14)

* Reduce flicker at the start of filtering. Before:

  ![reduce_flickering_before](.github/demos/0.14.0-filter-flicker-before.gif)

  After:

  ![reduce_flickering_after](.github/demos/0.14.0-filter-flicker-after.gif)

* Fix copying cells containing CRLF (#151)

# v0.13.0

* Add `--color-columns` to display each column in a different color (#39)
* Add `--prompt` to show a custom prompt message in the status bar (#135)
* Expose freeze columns option in library usage (#124 by @jqnatividad)
* Improve visibility of line numbers and borders
* Add `aarch64` release targets (#55)

# v0.12.0

* Freeze first `n` columns when scrolling via `f<n>` (#62, #117)
* Support searching in header row (#102)
* Support moving find mode cursor horizontally via `n` / `N`
* Support library usage without clap dependency (#118 by @jqnatividad)
* Fix search highlighting when columns are filtered
* Fix column scrolling for CSV with irregular last row (#99)

# v0.11.0

* Support copying a row to the clipboard (#97 by @mendelmaleh)
* Improve rendering performance by using line-buffered `stderr` (#107)
* Fix panic when filtering columns with irregular CSV (#112 by @antmelon)
* Disable `arboard` default features to reduce image related dependencies (#114 by @jqnatividad)
* Improve test stability across different environments (#101)

# v0.10.1

* Fix `--echo-column` option error

# v0.10.0

* Improve horizontal space utilization when rendering wide columns
* Support toggling sort direction
* Accept tab delimiter specified as `-d \t` without quotes
* Add library target

# v0.9.1

## Bug fixes

* Fixed issue with finding and filtering using an empty cell leading to incorrect matches
* Fixed certain Shift key-related key bindings not functioning correctly on Windows (Issue #82)

# v0.9.0

* Improve scrolling responsiveness for large csv
* Find and filter using selected cell (`#` and `@`) to search for exact matches
* Fix rendering of cursor in input prompt
* Fix app freeze on line wrap in some cases
* Fix potential overflow when subtracting durations in Windows (#77)
* Fix rendering of right border with irregular columns (#73)
* Fix misspelling ([#72](https://github.com/YS-L/csvlens/pull/72) by @theKnightsOfRohan)

# v0.8.1

* Fix rendering of consecutive newlines
* Fix clipboard support on Wayland (@ram02z)
* Allow opting out of clipboard feature

# v0.8.0

This release adds support for the following:

* Find and filter within the selected column
* Find and filter using the selected cell (`#` and `@`)
* Wrap lines by words (toggled via `-W`)
* Copy selected cell to clipboard (`y`)

# v0.7.0

* Support sorting rows by a column (`Shift + ↓` or `Shift + j`)
* Support CSV without headers via `--no-headers`
* Add `--columns`, `--filter`, and `--find` options for filtering rows and columns

# v0.6.0

* Accept `"\t"` for tab as delimiter argument ([#49](https://github.com/YS-L/csvlens/pull/49) by @peterjc)
* Add `-t` flag for tsv files ([#47](https://github.com/YS-L/csvlens/pull/47) by @JojiiOfficial)
* Print lower level causes on error

# v0.5.1

* Fix panic caused by unicode and newline

# v0.5.0

* Migrate to Ratatui ([#42](https://github.com/YS-L/csvlens/pull/42) by @joshka)
* Better readline support using tui-input (move cursor forward / backward, jump to the start, etc)
* Improve buffer history to retrieve more than just the last input

# v0.4.0

This release adds support for the following:

* Show help page with key bindings (`H`)
* Scroll to left most and right most columns (`Ctrl + ←`  or `Ctrl + →`)
* Scroll forward and backward half a window (`Ctrl + d` or `Ctrl + u`)
* Resize columns (`<` or `>`)
* Reset to default view (`r`)

# v0.3.2

* Fix incorrectly truncated content due to highlighting
* Fix potential overflow panic

# v0.3.1

* Fix panic due to unicode handling
* Fix row height calculation to account for column widths properly
* Reduce maximum column width fraction to make more columns visible

# v0.3.0

* Support line wrapping for displaying long or multiline content

# v0.2.0

* Add `-d auto` option to auto-detect delimiter
* Add `Home` and `End` key bindings
* Support row, column and cell selection modes (toggle via `TAB`)

# v0.1.14

* Implement --ignore-case option
* Fix crossterm double input issue on Windows

# v0.1.13

* Switch to Rust 2021 edition and update dependencies (#25)
* Fix crossterm panic by upgrading to version 0.26.1
* New styling for selected row

# v0.1.12

* Add --version option
* Add --echo-column option to print column's value at selected row to stdout
* Use stderr as tui buffer to support piping from csvlens

# v0.1.11

* Attempt to restore terminal state on panic
* Fix piped input not working on macOS

# v0.1.10

* Handle irregular CSV when calculating column widths
* Improved event loop handling
* Improved memory usage when creating temporary file from stdin

# v0.1.9

* Support filtering on columns
* Support basic command history

# v0.1.8

* Support horizontal scrolling

# v0.1.7

* Ensure terminal state is restored on error

# v0.1.6

* Fix bug where program sometimes crashes due to unicode characters
* Switch to `crossterm`

# v0.1.5

* Support irregular CSV to some extent (parse CSV in non-strict mode)
* Support regex patterns in search and filter
* Support scrolling to top with `g`
```

## File: `Cargo.toml`
```
[package]
name = "csvlens"
version = "0.15.1"
authors = ["Yung Siang Liau <liauys@gmail.com>"]
license = "MIT"
description = "Command line csv viewer"
readme = "README.md"
homepage = "https://github.com/YS-L/csvlens"
repository = "https://github.com/YS-L/csvlens"
keywords = ["cli", "csv", "viewer", "pager", "tui"]
edition = "2024"
rust-version = "1.88"
default-run = "csvlens"
include = [
    "src/**",
    "Cargo.toml",
    "README.md",
    "CHANGELOG.md",
    "LICENSE*"
]

# See more keys and their definitions at https://doc.rust-lang.org/cargo/reference/manifest.html

[dependencies]
csv = "1.4"
ratatui = "0.30"
crossterm = { version = "0.28", features = ["use-dev-tty"] }
anyhow = "1.0"
clap = { version = "4.5", features = ["derive", "wrap_help"], optional = true }
tempfile = "3"
regex = "1"
csv-nose = { version = "1", default-features = false }
tui-input = { version = "0.13", features = ["crossterm"] }
arrow = {version = "57", default-features = false, features = ["csv"]}
sorted-vec = "0.8"
arboard = { version = "3.6", default-features = false, features = ["wayland-data-control"], optional = true }
thiserror = "2"
terminal-colorsaurus = "1.0"
ansi-to-tui = "8.0.1"
clap-cargo = {version = "0.18.3", optional = true}
csv-core = "0.1.13"
rand = { version = "0.10", optional = true }

[target.'cfg(windows)'.dependencies]
crossterm = "0.28"

[features]
default = ["clipboard", "cli"]
clipboard = ["dep:arboard"]
cli = ["dep:clap", "dep:clap-cargo"]
bench = ["dep:rand"]

# The profile that 'cargo dist' will build with
[profile.dist]
inherits = "release"
lto = "thin"

[profile.release]
strip = "debuginfo"

[profile.bench]
debug = true

[dev-dependencies]
rstest = "0.26.1"
criterion = "0.8"
rand = "0.10"

[[bench]]
name = "record_iterator"
harness = false

[[example]]
name = "build_bench_data"
required-features = ["bench"]
```

## File: `Justfile`
```
# Test cargo-dist release build by creating a PR
dist-test-pr:
    #!/usr/bin/env bash
    set -euo pipefail

    # Checkout new branch
    BRANCH_NAME="dist-test-$(date +%Y%m%d-%H%M%S)"
    echo "Creating new branch: $BRANCH_NAME"
    git checkout -b "$BRANCH_NAME"

    # Patch dist-workspace.toml to set pr-run-mode = "upload"
    echo "Patching dist-workspace.toml..."
    sed -i.bak 's/pr-run-mode = "plan"/pr-run-mode = "upload"/' dist-workspace.toml
    rm -f dist-workspace.toml.bak

    # Run dist generate to generate updated workflow
    echo "Running cargo dist generate..."
    dist generate

    # Check if there are changes to commit
    if ! git diff --quiet; then
        echo "Committing changes..."
        git add .
        git commit -m "test: cargo-dist release artifact build"

        echo "Pushing branch and creating PR..."
        git push -u origin "$BRANCH_NAME"

        gh pr create \
            --title "test: cargo-dist release artifact build" \
            --body "Test cargo-dist release build process."

        echo "PR created successfully!"
    else
        echo "No changes to commit. Cleaning up branch..."
        git checkout -
        git branch -D "$BRANCH_NAME"
    fi
```

## File: `LICENSE`
```
MIT License

Copyright (c) 2022 Yung Siang Liau

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

## File: `README.md`
```markdown
# csvlens

`csvlens` is a command line CSV file viewer. It is like `less` but made
for CSV.

![Demo](.github/demo.gif)

## Usage

Run `csvlens` by providing the CSV filename:

```
csvlens <filename>
```

Pipe CSV data directly to `csvlens`:

```
<your commands producing some csv data> | csvlens
```
### Key bindings

Key | Action
--- | ---
`hjkl` (or `← ↓ ↑ →`) | Scroll one row or column in the given direction
`Ctrl + f` (or `Page Down`) | Scroll one window down
`Ctrl + b` (or `Page Up`) | Scroll one window up
`Ctrl + d` (or `d`) | Scroll half a window down
`Ctrl + u` (or `u`) | Scroll half a window up
`Ctrl + h` | Scroll one window left
`Ctrl + l` | Scroll one window right
`Ctrl + ←` | Scroll left to first column
`Ctrl + →` | Scroll right to last column
`Ctrl + e` | Print the marked lines to stdout and exit
`G` (or `End`) | Go to bottom
`g` (or `Home`) | Go to top
`<n>G` | Go to line `n`
`/<regex>` | Find content matching regex and highlight matches
`n` (in Find mode) | Jump to next result
`N` (in Find mode) | Jump to previous result
`&<regex>` | Filter rows using regex (show only matches)
`*<regex>` | Filter columns using regex (show only matches)
`TAB` | Toggle between row, column or cell selection modes
`>` | Increase selected column's width
`<` | Decrease selected column's width
`Shift + ↓` (or `J`) | Sort rows or toggle sort direction by the selected column
`Ctrl + j` | Same as above, but sort by natural ordering (e.g. "file2" < "file10")
`#` (in Cell mode) | Find and highlight rows like the selected cell
`@` (in Cell mode) | Filter rows like the selected cell
`y` | Copy the selected row or cell to clipboard
`Enter` (in Cell mode) | Print the selected cell to stdout and exit
`-S` | Toggle line wrapping
`-W` | Toggle line wrapping by words
`f<n>` | Freeze this number of columns from the left
`m` | Mark / unmark the selected row visually
`M` | Clear all row marks
`Ctrl + e` | Print the marked rows (with header) to stdout and exit
`r` | Reset to default view (clear all filters and custom column widths)
`H` (or `?`) | Display help
`q` | Exit

### Optional parameters

* `-d <char>`: Use this delimiter when parsing the CSV
  (e.g. `csvlens file.csv -d '\t'`).

  Specify `-d auto` to auto-detect the delimiter.

* `-t`, `--tab-separated`: Use tab as the delimiter (when specified, `-d` is ignored).

* `-i`, `--ignore-case`: Ignore case when searching. This flag is ignored if any
  uppercase letters are present in the search string.

* `--no-headers`: Do not interpret the first row as headers.

* `--columns <regex>`: Use this regex to select columns to display by default.

  Example: `"column1|column2"` matches `"column1"`, `"column2"`, and also column names like
  `"column11"`, `"column22"`.

* `--filter <regex>`: Use this regex to filter rows to display by default.

  The regex is matched against each cell in every column.

  Example: `"value1|value2"` filters rows with any cells containing `"value1"`, `"value2"`, or text
  like `"my_value1"` or `"value234"`.

* `--find <regex>`: Use this regex to find and highlight matches by default.

  The regex is matched against each cell in every column.

  Example: `"value1|value2"` highlights text in any cells containing `"value1"`, `"value2"`, or
  longer text like `"value1_ok"`.

* `--echo-column <column_name>`: Print the value of this column at the selected
  row to stdout on `Enter` key and then exit.

* `--prompt <prompt>`: Show a custom prompt message in the status bar. Supports ANSI escape codes
  for colored or styled text.

  Example:
  ```bash
  csvlens Pokemon.csv --prompt $'\e[1m\e[32mSelect a Pokémon!\e[0m'
  ```

* `--color-columns` (or `--colorful`): Display each column in a different color.

## Installation

### Direct download

You can download the `tar.xz` or `zip` file matching your operating system from the
[releases page](https://github.com/YS-L/csvlens/releases), extract it and execute the `csvlens`
binary.

### Homebrew

For macOS, `csvlens` is available on [Homebrew](https://formulae.brew.sh/formula/csvlens). You can
install it using:
```
brew install csvlens
```

### Arch Linux
`csvlens` is available in the [official repositories](https://archlinux.org/packages/extra/x86_64/csvlens). You can install it using:
```
pacman -S csvlens
```

### Windows

For Windows, `csvlens` is available on [winget](https://learn.microsoft.com/en-gb/windows/package-manager/). You can install it using:
```powershell
winget install --id YS-L.csvlens
```

### FreeBSD
`csvlens` is available as a [FreeBSD pkg](https://www.freshports.org/textproc/csvlens/). You can install it using:
```
pkg install csvlens
```

### NetBSD
`csvlens` is available on [pkgsrc](https://ftp.netbsd.org/pub/pkgsrc/current/pkgsrc/textproc/csvlens/index.html). If you're using NetBSD you can install it using:
```
pkgin install csvlens
```

### OpenBSD
`csvlens` is available as an [OpenBSD port](https://cvsweb.openbsd.org/ports/textproc/csvlens/). If you're using OpenBSD 7.6-current or later, you can install it using:
```
doas pkg_add csvlens
```

### Cargo

If you have [Rust](https://www.rust-lang.org/tools/install) installed, `csvlens` is available on
[crates.io](https://crates.io/crates/csvlens) and you can install it using:
```
cargo install csvlens
```

Or, build and install from source after cloning this repo:
```
cargo install --path $(pwd)
```

Requires Rust 1.88.0 or newer.

## Library Usage

This crate allows you to use csvlens as a library.

In your `Cargo.toml`, add the following:

```toml
[dependencies]
csvlens = { version = "0.12.0", default-features = false, features = ["clipboard"] }
```

### Example

Here's a simple example of how to use `csvlens` as a library ([Documentation](https://docs.rs/csvlens/0.12.0/csvlens/index.html)):

```rust
use csvlens::run_csvlens;

let out = run_csvlens(&["/path/to/your.csv"]).unwrap();
if let Some(selected_cell) = out {
    println!("Selected: {}", selected_cell);
}
```

For more advanced usage, you can use `CsvlensOptions` to customize the behavior:

```rust
use csvlens::{run_csvlens_with_options, CsvlensOptions};

let options = CsvlensOptions {
    filename: "/path/to/your.csv".to_string(),
    delimiter: Some("|".to_string()),
    ignore_case: true,
    debug: true,
    ..Default::default()
};
let out = run_csvlens_with_options(options).unwrap();
if let Some(selected_cell) = out {
    println!("Selected: {}", selected_cell);
}
```

See how [qsv](https://github.com/dathere/qsv/tree/master?tab=readme-ov-file#qsv-blazing-fast-data-wrangling-toolkit) uses `csvlens` as a library [here](https://github.com/dathere/qsv/blob/master/src/cmd/lens.rs#L2).
```

## File: `dist-workspace.toml`
```
[workspace]
members = ["cargo:."]

# Config for 'dist'
[dist]
# The preferred dist version to use in CI (Cargo.toml SemVer syntax)
cargo-dist-version = "0.30.2"
# CI backends to support
ci = "github"
# The installers to generate for each app
installers = []
# Target platforms to build apps for (Rust target-triple syntax)
targets = ["aarch64-apple-darwin", "aarch64-unknown-linux-gnu", "aarch64-pc-windows-msvc", "x86_64-apple-darwin", "x86_64-unknown-linux-gnu", "x86_64-unknown-linux-musl", "x86_64-pc-windows-msvc"]
# Which actions to run on pull requests
pr-run-mode = "plan"

[dist.github-custom-runners]
global = "ubuntu-22.04"
aarch64-unknown-linux-gnu = "ubuntu-22.04"
aarch64-pc-windows-msvc = "ubuntu-22.04"
x86_64-unknown-linux-gnu = "ubuntu-22.04"
x86_64-unknown-linux-musl = "ubuntu-22.04"
```

## File: `benches/record_iterator.rs`
```rust
use std::{
    hint::black_box,
    sync::{Arc, atomic::AtomicBool},
};

use criterion::{Criterion, criterion_group, criterion_main};
use csvlens::bench_api::{CsvBaseConfig, CsvConfig, CsvlensRecordIterator};

const PERF_DATA: &str = "benches/data/random_100k.csv";

fn run_iterator(streaming: bool) {
    let stream_active = if streaming {
        Some(Arc::new(AtomicBool::new(true)))
    } else {
        None
    };

    let base_config = CsvBaseConfig::new(b',', false);
    let config = CsvConfig::new(PERF_DATA, stream_active.clone(), base_config);
    let record_iterator = CsvlensRecordIterator::new(Arc::new(config)).unwrap();

    stream_active
        .as_ref()
        .map(|x| x.store(false, std::sync::atomic::Ordering::Relaxed));

    for record in record_iterator {
        let record = record.unwrap();
        black_box(record);
    }
}

fn criterion_benchmark(c: &mut Criterion) {
    c.bench_function("built_in_record_iterator", |b| {
        b.iter(|| run_iterator(false))
    });
    c.bench_function("streaming_record_iterator", |b| {
        b.iter(|| run_iterator(true))
    });
}

criterion_group!(benches, criterion_benchmark);
criterion_main!(benches);
```

## File: `examples/build_bench_data.rs`
```rust
use std::{
    fs::File,
    io::{BufWriter, Write},
};

fn generate_random_csv(path: &str, rows: usize, cols: usize) {
    use rand::RngExt;
    std::fs::create_dir_all("benches/data").unwrap();

    let mut rng = rand::rng();
    let file = File::create(path).unwrap();
    let mut w = BufWriter::new(file);

    // header
    for c in 0..cols {
        if c > 0 {
            write!(w, ",").unwrap();
        }
        write!(w, "col{}", c).unwrap();
    }
    writeln!(w).unwrap();

    for _ in 0..rows {
        for c in 0..cols {
            if c > 0 {
                write!(w, ",").unwrap();
            }
            let val: i64 = rng.random_range(0..1_000_000);
            write!(w, "{val}").unwrap();
        }
        writeln!(w).unwrap();
    }
}

/// Generate a random CSV file for benchmarking
///
/// Run with:
///
/// cargo run --example build_bench_data --features=bench
fn main() {
    generate_random_csv("benches/data/random_100k.csv", 100_000, 30);
}
```

## File: `src/app.rs`
```rust
extern crate csv_nose;

use crate::columns_filter::ColumnsFilter;
use crate::csv;
use crate::delimiter::{Delimiter, sniff_delimiter};
use crate::errors::{CsvlensError, CsvlensResult};
use crate::find;
use crate::help;
use crate::input::{Control, InputHandler};
use crate::io::SeekableFile;
use crate::sort::{self, SortOrder, SorterStatus};
use crate::ui::{CsvTable, CsvTableState, FilterColumnsState, FinderState};
use crate::view::{self, ColumnsOffset, SelectionType};
use crate::watch::{FileWatcher, Watcher};

#[cfg(feature = "clipboard")]
use arboard::Clipboard;
use ratatui::backend::Backend;
use ratatui::prelude::Position;
use ratatui::{Frame, Terminal};

use anyhow::Result;
use regex::Regex;
use std::cmp::min;
use std::sync::Arc;
use std::time::{Duration, Instant};

fn get_offsets_to_make_visible(
    found_record: &find::FoundEntry,
    rows_view: &view::RowsView,
    csv_table_state: &CsvTableState,
) -> (Option<u64>, Option<u64>) {
    // TODO: row_index() should probably be u64
    let new_rows_offset = if let find::FoundEntry::Row(entry) = found_record {
        if rows_view.in_view(entry.row_order() as u64) {
            None
        } else {
            Some(entry.row_order() as u64)
        }
    } else {
        None
    };

    let column_index = match found_record {
        find::FoundEntry::Header(entry) => entry.column_index(),
        find::FoundEntry::Row(entry) => entry.column_index(),
    } as u64;
    let cols_offset = rows_view.cols_offset();
    let new_cols_offset_num_skip = if cols_offset
        .is_filtered_column_index_visible(column_index, csv_table_state.num_cols_rendered)
    {
        None
    } else {
        Some(cols_offset.get_num_skip_to_make_visible(column_index))
    };

    (new_rows_offset, new_cols_offset_num_skip)
}

fn scroll_to_found_entry(
    found_entry: find::FoundEntry,
    rows_view: &mut view::RowsView,
    csv_table_state: &mut CsvTableState,
) {
    let (new_rows_offset, new_cols_offset_num_skip) =
        get_offsets_to_make_visible(&found_entry, rows_view, csv_table_state);

    // csv_table_state.debug = format!("{:?} {:?}", new_rows_offset, new_cols_offset);
    // csv_table_state.debug = format!("{:?}", found_record);
    if let Some(rows_offset) = new_rows_offset {
        rows_view.set_rows_from(rows_offset).unwrap();
        csv_table_state.set_rows_offset(rows_offset);
    }

    if let Some(cols_offset_num_skip) = new_cols_offset_num_skip {
        rows_view.set_cols_offset_num_skip(cols_offset_num_skip);
        csv_table_state.set_cols_offset(rows_view.cols_offset());
    }
}

/// Returns the offset of the first column that can be shown in the current frame, while keeping the
/// column corresponding to right_most_cols_offset in view.
fn get_cols_offset_to_fill_frame_width(
    frame_width: u16,
    right_most_cols_offset: u64,
    csv_table_state: &CsvTableState,
) -> Option<u64> {
    let view_layout = csv_table_state.view_layout.as_ref();
    let mut total: u16 = 0;
    let mut new_cols_offset = None;
    let unusable_width = csv_table_state.line_number_and_spaces_width();
    if let Some(layout) = view_layout {
        for c in (0..right_most_cols_offset.saturating_add(1) as usize).rev() {
            let maybe_width = layout.column_widths.get(c);
            if let Some(w) = maybe_width {
                if total + w > frame_width.saturating_sub(unusable_width) {
                    break;
                }
                new_cols_offset = Some(c as u64);
                total += w;
            } else {
                break;
            }
        }
        new_cols_offset
    } else {
        None
    }
}

#[derive(Debug, Clone, Copy, PartialEq, Eq, Default)]
pub enum WrapMode {
    Chars,
    Words,
    #[default]
    Disabled,
}

impl WrapMode {
    pub fn toggle(&mut self, mode: WrapMode) {
        if self.is_enabled() {
            if *self == mode {
                // Toggling the same mode disables line wrap
                *self = WrapMode::Disabled;
            } else {
                // Just switch between line wrap and word wrap if already enabled
                *self = mode;
            }
        } else {
            // If currently disabled, just enable it with the specified mode
            *self = mode;
        }
    }

    pub fn transient_message(&self) -> String {
        match self {
            WrapMode::Chars => "Line wrap enabled".to_string(),
            WrapMode::Words => "Word wrap enabled".to_string(),
            WrapMode::Disabled => "Line wrap disabled".to_string(),
        }
    }

    pub fn is_enabled(&self) -> bool {
        !matches!(self, WrapMode::Disabled)
    }

    pub fn is_word_wrap(&self) -> bool {
        matches!(self, WrapMode::Words)
    }
}

enum ScrollToFoundState {
    Pending,
    Done,
}

fn poll_finder_first_match(finder: &find::Finder, timeout: Duration) -> bool {
    let start = Instant::now();
    while start.elapsed() < timeout {
        if finder.found_any() {
            return true;
        }
        std::thread::sleep(Duration::from_millis(1));
    }
    false
}

pub struct App {
    input_handler: InputHandler,
    num_rows_not_visible: u16,
    shared_config: Arc<csv::CsvConfig>,
    rows_view: view::RowsView,
    columns_filter: Option<Arc<ColumnsFilter>>,
    csv_table_state: CsvTableState,
    finder: Option<find::Finder>,
    scroll_to_found_state: ScrollToFoundState,
    frame_width: Option<u16>,
    transient_message: Option<String>,
    show_stats: bool,
    echo_column: Option<String>,
    ignore_case: bool,
    help_page_state: help::HelpPageState,
    sorter: Option<Arc<sort::Sorter>>,
    sort_order: SortOrder,
    wrap_mode: WrapMode,
    #[cfg(feature = "clipboard")]
    clipboard: Result<Clipboard>,
    _seekable_file: SeekableFile,
}

impl App {
    #[allow(clippy::too_many_arguments)]
    pub fn new(
        original_filename: Option<String>,
        delimiter: Delimiter,
        show_stats: bool,
        echo_column: Option<String>,
        ignore_case: bool,
        no_headers: bool,
        columns_regex: Option<String>,
        filter_regex: Option<String>,
        find_regex: Option<String>,
        freeze_cols_offset: Option<u64>,
        color_columns: bool,
        prompt: Option<String>,
        wrap_mode: Option<WrapMode>,
        auto_reload: bool,
        no_streaming_stdin: bool,
    ) -> CsvlensResult<Self> {
        // TODO: pass a base_config to wait for header properly?
        let seekable_file = SeekableFile::new(&original_filename, no_streaming_stdin)?;
        let filename = seekable_file.filename();

        let watcher = if auto_reload || seekable_file.stream_active().is_some() {
            Some(Arc::new(Watcher::new(filename)?))
        } else {
            None
        };
        let input_handler = InputHandler::new(watcher.map(FileWatcher::from));

        // Some lines are reserved for plotting headers (3 lines for headers + 2 lines for status bar)
        let num_rows_not_visible: u16 = 5;

        // Number of rows that are visible in the current frame
        let num_rows = 50 - num_rows_not_visible;

        let delimiter = match delimiter {
            Delimiter::Comma => b',',
            Delimiter::Tab => b'\t',
            Delimiter::Character(d) => d,
            Delimiter::Default | Delimiter::Auto => sniff_delimiter(filename).unwrap_or(b','),
        };
        let base_config = csv::CsvBaseConfig::new(delimiter, no_headers);
        let config =
            csv::CsvConfig::new(filename, seekable_file.stream_active().clone(), base_config);
        let shared_config = Arc::new(config);

        let csvlens_reader = csv::CsvLensReader::new(shared_config.clone())?;
        let mut rows_view = view::RowsView::new(csvlens_reader, num_rows as u64)?;

        // Set the number of columns to freeze
        if let Some(freeze_cols_offset) = freeze_cols_offset {
            rows_view.set_cols_offset_num_freeze(freeze_cols_offset);
        }

        if let Some(column_name) = &echo_column
            && !rows_view.headers().iter().any(|h| h.name == *column_name)
        {
            return Err(CsvlensError::ColumnNameNotFound(column_name.clone()));
        }

        let csv_table_state = CsvTableState::new(
            original_filename,
            rows_view.headers().len(),
            &echo_column,
            ignore_case,
            color_columns,
            prompt,
        );

        let finder: Option<find::Finder> = None;
        let frame_width = None;

        let transient_message: Option<String> = None;
        let help_page_state = help::HelpPageState::new();

        #[cfg(feature = "clipboard")]
        let clipboard = match Clipboard::new() {
            Ok(clipboard) => Ok(clipboard),
            Err(e) => Err(anyhow::anyhow!(e)),
        };

        let mut app = App {
            input_handler,
            num_rows_not_visible,
            shared_config,
            rows_view,
            columns_filter: None,
            csv_table_state,
            finder,
            scroll_to_found_state: ScrollToFoundState::Done,
            frame_width,
            transient_message,
            show_stats,
            echo_column,
            ignore_case,
            help_page_state,
            sorter: None,
            sort_order: SortOrder::Ascending,
            wrap_mode: WrapMode::default(),
            #[cfg(feature = "clipboard")]
            clipboard,
            _seekable_file: seekable_file,
        };

        if let Some(pat) = &columns_regex {
            app.set_columns_filter(pat);
        }

        if let Some(pat) = &filter_regex {
            app.handle_find_or_filter(pat, true, false);
        } else if let Some(pat) = &find_regex {
            app.handle_find_or_filter(pat, false, false);
        }

        app.rows_view.set_sort_order(app.sort_order)?;
        app.csv_table_state.debug_stats.show_stats(app.show_stats);

        if let Some(mode) = wrap_mode {
            app.handle_line_wrap_toggle(mode, false);
        }

        Ok(app)
    }

    pub fn main_loop<B: Backend>(
        &mut self,
        terminal: &mut Terminal<B>,
    ) -> CsvlensResult<Option<String>> {
        loop {
            let control = self.input_handler.next();
            if matches!(control, Control::Quit) {
                if self.help_page_state.is_active() {
                    self.help_page_state.deactivate();
                    self.input_handler.exit_help_mode();
                } else {
                    return Ok(None);
                }
            }
            if matches!(control, Control::Select)
                && let Some(result) = self.get_selection()
            {
                return Ok(Some(result));
            }
            if matches!(control, Control::SelectMarks)
                && let Some(result) = self.get_marked_rows()
            {
                return Ok(Some(result));
            }
            if matches!(control, Control::Help) {
                self.help_page_state.activate();
                self.input_handler.enter_help_mode();
            }
            self.step(&control)?;
            self.draw(terminal)?;
        }
    }

    fn step_help(&mut self, control: &Control) -> CsvlensResult<()> {
        match &control {
            Control::ScrollDown => {
                self.help_page_state.scroll_down();
            }
            Control::ScrollUp => {
                self.help_page_state.scroll_up();
            }
            _ => {}
        }
        Ok(())
    }

    fn step(&mut self, control: &Control) -> CsvlensResult<()> {
        if self.help_page_state.is_active() {
            return self.step_help(control);
        }

        // Clear message without changing other states on any action. FileChanged is excluded since
        // it is not initiated by user and can mask other messages on streaming input.
        if !matches!(control, Control::Nothing | Control::FileChanged) {
            self.transient_message = None;
        }

        self.rows_view.handle_control(control)?;
        self.rows_view
            .selection
            .column
            .set_bound(self.csv_table_state.num_cols_rendered);

        match &control {
            Control::ScrollTo(_) => {
                self.csv_table_state.reset_buffer();
            }
            Control::ScrollLeft => {
                if let Some(i) = self.rows_view.selection.column.index() {
                    if i == 0 {
                        self.decrease_cols_offset();
                    } else {
                        self.rows_view.selection.column.select_previous();
                    }
                } else {
                    self.decrease_cols_offset();
                }
            }
            Control::ScrollRight => {
                if let Some(i) = self.rows_view.selection.column.index() {
                    if i == self.csv_table_state.num_cols_rendered - 1 {
                        self.increase_cols_offset();
                    } else {
                        self.rows_view.selection.column.select_next();
                    }
                } else {
                    self.increase_cols_offset();
                }
            }
            Control::ScrollPageLeft => {
                let new_cols_offset = match self.frame_width {
                    Some(frame_width) => get_cols_offset_to_fill_frame_width(
                        frame_width,
                        self.csv_table_state.cols_offset.num_skip.saturating_sub(1),
                        &self.csv_table_state,
                    ),
                    _ => Some(0),
                };
                if let Some(new_cols_offset) = new_cols_offset {
                    self.rows_view.set_cols_offset_num_skip(new_cols_offset);
                }
            }
            Control::ScrollPageRight => {
                if self.csv_table_state.has_more_cols_to_show() {
                    // num_cols_rendered includes the last truncated column
                    let mut new_cols_offset_num_skip =
                        self.csv_table_state.cols_offset.num_skip.saturating_add(
                            self.csv_table_state.num_cols_rendered.saturating_sub(1),
                        );
                    new_cols_offset_num_skip = min(
                        new_cols_offset_num_skip,
                        self.rows_view.max_cols_offset_num_skip(),
                    );
                    if new_cols_offset_num_skip != self.csv_table_state.cols_offset.num_skip {
                        self.rows_view
                            .set_cols_offset_num_skip(new_cols_offset_num_skip);
                    }
                }
            }
            Control::ScrollLeftMost => {
                self.rows_view.set_cols_offset_num_skip(0);
            }
            Control::ScrollRightMost => {
                if self.csv_table_state.has_more_cols_to_show() {
                    let new_cols_offset = match self.frame_width {
                        Some(frame_width) => get_cols_offset_to_fill_frame_width(
                            frame_width,
                            self.rows_view.max_cols_offset_num_skip(),
                            &self.csv_table_state,
                        ),
                        _ => Some(0),
                    };
                    if let Some(new_cols_offset) = new_cols_offset {
                        self.rows_view.set_cols_offset_num_skip(new_cols_offset);
                    }
                }
            }
            Control::ScrollToNextFound if !self.rows_view.is_filter() => {
                if let Some(fdr) = self.finder.as_mut()
                    && let Some(found_entry) = fdr.next()
                {
                    scroll_to_found_entry(
                        found_entry,
                        &mut self.rows_view,
                        &mut self.csv_table_state,
                    );
                }
            }
            Control::ScrollToPrevFound if !self.rows_view.is_filter() => {
                if let Some(fdr) = self.finder.as_mut()
                    && let Some(found_entry) = fdr.prev()
                {
                    scroll_to_found_entry(
                        found_entry,
                        &mut self.rows_view,
                        &mut self.csv_table_state,
                    );
                }
            }
            Control::Find(s) | Control::Filter(s) => {
                self.handle_find_or_filter(s, matches!(control, Control::Filter(_)), false);
            }
            Control::FindLikeCell | Control::FilterLikeCell => {
                if let Some(value) = self.rows_view.get_cell_value_from_selection() {
                    self.handle_find_or_filter(
                        value.as_str(),
                        matches!(control, Control::FilterLikeCell),
                        true,
                    );
                } else {
                    self.transient_message.replace(
                        "Select a cell first before finding (#) or filtering (@) rows like it"
                            .to_string(),
                    );
                }
            }
            Control::FilterColumns(pat) => {
                self.set_columns_filter(pat);
            }
            Control::FreezeColumns(num_cols) => {
                self.rows_view.set_cols_offset_num_freeze(*num_cols as u64);
                self.csv_table_state.reset_buffer();
            }
            Control::BufferContent(input) => {
                self.csv_table_state
                    .set_buffer(self.input_handler.mode(), input.clone());
            }
            Control::BufferReset => {
                self.csv_table_state.reset_buffer();
                self.reset_filter(true);
                self.reset_columns_filter();
            }
            Control::ToggleSelectionType => {
                self.rows_view.selection.toggle_selection_type();
            }
            Control::ToggleMark => {
                if let SelectionType::Row = self.rows_view.selection.selection_type() {
                    if let Some(row_index) = self.rows_view.selection.row.index() {
                        if let Some(toggle_result) = self.rows_view.toggle_mark(row_index as usize)
                        {
                            if toggle_result.marked {
                                self.transient_message
                                    .replace(format!("Marked line {}", toggle_result.record_num));
                            } else {
                                self.transient_message
                                    .replace(format!("Unmarked line {}", toggle_result.record_num));
                            }
                        } else {
                            self.transient_message
                                .replace("Unable to mark this line".to_string());
                        }
                    }
                } else {
                    self.transient_message
                        .replace("Marking of rows only works in row mode".to_string());
                }
            }
            Control::ResetMarks => {
                self.rows_view.clear_marks();
                self.transient_message
                    .replace("All marks cleared".to_string());
            }
            Control::ToggleLineWrap(word_wrap) => {
                self.handle_line_wrap_toggle(*word_wrap, true);
            }
            Control::ToggleSort | Control::ToggleNaturalSort => {
                if self.shared_config.is_streaming() {
                    self.transient_message.replace(
                        "Sorting is not supported when data is still streaming".to_string(),
                    );
                } else {
                    self.handle_sort(control)?;
                }
            }
            Control::IncreaseWidth => {
                self.adjust_column_width(4);
            }
            Control::DecreaseWidth => {
                self.adjust_column_width(-4);
            }
            #[cfg(feature = "clipboard")]
            Control::CopySelection => {
                if let Some(selected) = self.rows_view.get_cell_value_from_selection() {
                    let selected_cleaned = selected.replace(['\n', '\r'], "");
                    match self.clipboard.as_mut().map(|c| c.set_text(&selected)) {
                        Ok(_) => self
                            .transient_message
                            .replace(format!("Copied {} to clipboard", selected_cleaned.as_str())),
                        Err(e) => self
                            .transient_message
                            .replace(format!("Failed to copy to clipboard: {e}")),
                    };
                } else if let Some((index, row)) = self.rows_view.get_row_value() {
                    match self.clipboard.as_mut().map(|c| c.set_text(&row)) {
                        Ok(_) => self
                            .transient_message
                            .replace(format!("Copied row {} to clipboard", index)),
                        Err(e) => self
                            .transient_message
                            .replace(format!("Failed to copy to clipboard: {e}")),
                    };
                }
            }
            Control::FileChanged => {
                self.handle_file_changed()?;
            }
            Control::Reset => {
                self.csv_table_state.column_width_overrides.reset();
                self.reset_filter(false);
                self.reset_columns_filter();
                self.reset_sorter();
            }
            Control::UnknownOption(s) => {
                self.csv_table_state.reset_buffer();
                self.transient_message
                    .replace(format!("Unknown option: {s}"));
            }
            Control::UserError(s) => {
                self.csv_table_state.reset_buffer();
                self.transient_message.replace(s.clone());
            }
            _ => {}
        }

        if let Some(sorter) = &self.sorter {
            // Update rows_view sorter if outdated
            let mut should_set_rows_view_sorter = false;
            if sorter.status() == SorterStatus::Finished {
                if let Some(rows_view_sorter) = self.rows_view.sorter() {
                    // Sorter can be reused by rows view even if sort order is different.
                    if rows_view_sorter.column_index != sorter.column_index
                        || rows_view_sorter.sort_type() != sorter.sort_type()
                    {
                        should_set_rows_view_sorter = true;
                    }
                } else {
                    should_set_rows_view_sorter = true;
                }
            }
            if should_set_rows_view_sorter {
                self.rows_view.set_sorter(sorter).unwrap();
            }

            // Update finder if sorter outdated
            let mut should_create_new_finder = false;
            if sorter.status() == SorterStatus::Finished
                && let Some(finder) = &self.finder
            {
                if let Some(finder_sorter) = finder.sorter() {
                    // Internal state of finder needs to be rebuilt if sorter is different,
                    // including sort order.
                    if finder_sorter.column_index != sorter.column_index
                        || finder_sorter.sort_type() != sorter.sort_type()
                        || finder.sort_order != self.sort_order
                    {
                        should_create_new_finder = true;
                    }
                } else {
                    should_create_new_finder = true;
                }
            }
            if should_create_new_finder {
                let target = self.finder.as_ref().unwrap().target();
                let sorter = self.sorter.clone();
                if let Some(finder) = &self.finder {
                    // Inherit previous finder's column index if any, instead of using the current
                    // selected column intended for sorter
                    self.create_finder_with_params(
                        target,
                        self.rows_view.is_filter(),
                        finder.column_index(),
                        finder.starting_row_index(),
                        sorter,
                    );
                } else {
                    self.create_finder(target, self.rows_view.is_filter(), sorter);
                }
            }
        }

        if let Some(fdr) = self.finder.as_mut() {
            if !self.rows_view.is_filter() {
                // scroll to first result once ready
                match self.scroll_to_found_state {
                    ScrollToFoundState::Pending => {
                        if let Some(found_entry) = fdr.set_initial_cursor_if_ready() {
                            scroll_to_found_entry(
                                found_entry,
                                &mut self.rows_view,
                                &mut self.csv_table_state,
                            );
                            self.scroll_to_found_state = ScrollToFoundState::Done;
                        }
                    }
                    ScrollToFoundState::Done => {
                        // reset cursor if out of view
                        if let Some(cursor_row_order) = fdr.cursor_row_order()
                            && !self.rows_view.in_view(cursor_row_order as u64)
                        {
                            fdr.reset_cursor();
                        }

                        fdr.set_row_hint(self.rows_view.rows_from() as usize);
                    }
                }
            } else {
                self.rows_view.set_filter(fdr).unwrap();
            }
        }

        // update rows and elapsed time if there are new results
        self.update_debug_stats();

        // TODO: is this update too late?
        self.csv_table_state
            .set_rows_offset(self.rows_view.rows_from());
        self.csv_table_state
            .set_cols_offset(self.rows_view.cols_offset());
        self.csv_table_state.selection = Some(self.rows_view.selection.clone());
        self.csv_table_state.marked_rows = Some(self.rows_view.marked_rows().clone());

        if let Some(n) = self.rows_view.get_total_line_numbers() {
            self.csv_table_state.set_total_line_number(n, false);
        } else if let Some(n) = self.rows_view.get_total_line_numbers_approx() {
            self.csv_table_state.set_total_line_number(n, true);
        }

        self.csv_table_state
            .set_total_cols(self.rows_view.headers().len());

        if let Some(f) = &self.finder {
            // TODO: need to create a new finder every time?
            self.csv_table_state.finder_state = FinderState::from_finder(f, &self.rows_view);
        }
        self.csv_table_state.filter_columns_state =
            FilterColumnsState::from_rows_view(&self.rows_view);

        self.csv_table_state
            .update_sorter(&self.sorter, self.sort_order);

        self.csv_table_state
            .transient_message
            .clone_from(&self.transient_message);

        // if let Some(finder) = &self.finder {
        //     self.csv_table_state.debug = format!("cursor: {:?}", finder.cursor);
        // }
        // self.csv_table_state.debug =
        //     format!("last reload: {:?}", self.csv_table_state.last_autoreload_at);

        Ok(())
    }

    fn update_debug_stats(&mut self) {
        let debug_stats = &mut self.csv_table_state.debug_stats;
        debug_stats.rows_view_perf(self.rows_view.perf_stats());
        if let Some(fdr) = &self.finder {
            debug_stats.finder_elapsed(fdr.elapsed());
        } else {
            debug_stats.finder_elapsed(None);
        }
        if let Some(sorter) = &self.sorter {
            debug_stats.sorter_elapsed(sorter.elapsed());
        } else {
            debug_stats.sorter_elapsed(None);
        }
    }

    fn get_selection(&self) -> Option<String> {
        if let Some(result) = self.rows_view.get_cell_value_from_selection() {
            return Some(result);
        } else if let Some(column_name) = &self.echo_column
            && let Some(result) = self.rows_view.get_cell_value(column_name)
        {
            return Some(result);
        };
        None
    }

    fn get_marked_rows(&mut self) -> Option<String> {
        let marked = self.rows_view.marked_rows();
        if marked.is_empty() {
            return None;
        }

        let mut record_numbers: Vec<usize> = marked.iter().copied().collect();
        record_numbers.sort_unstable();

        let headers_line = self.rows_view.get_headers_line();
        match self.rows_view.get_rows_values(&record_numbers) {
            Ok(lines) => {
                let mut content_lines = Vec::with_capacity(lines.len().saturating_add(1));
                content_lines.push(headers_line);
                content_lines.extend(lines);
                Some(content_lines.join("\n"))
            }
            Err(_) => None,
        }
    }

    fn get_finder_starting_row_index(&self) -> usize {
        self.rows_view.selected_offset().unwrap_or(0) as usize
    }

    fn create_finder(&mut self, target: Regex, is_filter: bool, sorter: Option<Arc<sort::Sorter>>) {
        self.create_finder_with_params(
            target,
            is_filter,
            self.get_selected_column_index().map(|x| x as usize),
            self.get_finder_starting_row_index(),
            sorter,
        );
    }

    fn create_finder_with_params(
        &mut self,
        target: Regex,
        is_filter: bool,
        column_index: Option<usize>,
        starting_row_index: usize,
        sorter: Option<Arc<sort::Sorter>>,
    ) {
        let finder = find::Finder::new(
            self.shared_config.clone(),
            target,
            column_index,
            starting_row_index,
            sorter,
            self.sort_order,
            self.columns_filter.clone(),
        )
        .unwrap();

        // Instead of calling rows_view.set_filter() right away, wait for a bit until the first
        // match. Otherwise, it's almost guaranteed that no match will be found yet and the view
        // port becomes empty and comes back again in the next tick at rate of 250ms. This appears
        // as flickering. Also do this even when not filtering so jumping to first match is faster.
        // For most small files, 5ms should be sufficient to prevent flickering while not
        // introducing visible delays.
        poll_finder_first_match(&finder, Duration::from_millis(5));

        if is_filter {
            self.rows_view.set_rows_from(0).unwrap();
            self.rows_view.set_filter(&finder).unwrap();
        } else {
            self.rows_view.reset_filter(false).unwrap();
            self.scroll_to_found_state = ScrollToFoundState::Pending;
        }
        self.finder = Some(finder);
    }

    fn create_regex(&mut self, s: &str, escape: bool) -> std::result::Result<Regex, regex::Error> {
        let s = if escape {
            format!("^{}$", regex::escape(s))
        } else {
            s.to_string()
        };
        let lower_s = s.to_lowercase();
        if self.ignore_case && lower_s.starts_with(s.as_str()) {
            Regex::new(&format!("(?i){}", s))
        } else {
            Regex::new(s.as_str())
        }
    }

    fn set_columns_filter(&mut self, pat: &str) {
        let re = self.create_regex(pat, false);
        if let Ok(target) = re {
            let columns_filter = Arc::new(ColumnsFilter::new(target, self.rows_view.raw_headers()));
            self.columns_filter = Some(columns_filter.clone());
            self.rows_view.set_columns_filter(&columns_filter).unwrap();
        } else {
            self.reset_columns_filter();
            self.transient_message = Some(format!("Invalid regex: {pat}"));
        }
        self.csv_table_state.reset_buffer();
        self.csv_table_state
            .set_cols_offset(ColumnsOffset::default());
    }

    fn reset_columns_filter(&mut self) {
        self.columns_filter = None;
        self.rows_view.reset_columns_filter().unwrap();
    }

    fn handle_find_or_filter(&mut self, pat: &str, is_filter: bool, escape: bool) {
        if pat.is_empty() {
            // This can occur only when the regex is directly provided via CLI argument. Empty regex
            // would match everything and is almost certainly not what user intends, so just ignore
            // it for now.
            return;
        }
        let re = self.create_regex(pat, escape);
        if let Ok(target) = re {
            let _sorter = if let Some(s) = &self.sorter {
                if s.status() == SorterStatus::Finished {
                    Some(s.clone())
                } else {
                    None
                }
            } else {
                None
            };
            self.create_finder(target, is_filter, _sorter);
        } else {
            self.finder = None;
            // TODO: how to show multi-line error
            self.transient_message = Some(format!("Invalid regex: {pat}"));
        }
        self.csv_table_state.reset_buffer();
    }

    fn handle_sort(&mut self, control: &Control) -> CsvlensResult<()> {
        let desired_sort_type = if matches!(control, Control::ToggleNaturalSort) {
            sort::SortType::Natural
        } else {
            sort::SortType::Auto
        };
        if let Some(selected_column_index) = self.get_global_selected_column_index() {
            let mut should_create_new_sorter = false;
            if let Some(sorter) = &self.sorter {
                if selected_column_index as usize != sorter.column_index
                    || desired_sort_type != sorter.sort_type()
                {
                    should_create_new_sorter = true;
                } else {
                    match self.sort_order {
                        SortOrder::Ascending => {
                            self.sort_order = SortOrder::Descending;
                        }
                        SortOrder::Descending => {
                            self.sort_order = SortOrder::Ascending;
                        }
                    }
                    self.rows_view.set_sort_order(self.sort_order)?;
                }
            } else {
                should_create_new_sorter = true;
            }
            if should_create_new_sorter {
                let column_name = self
                    .rows_view
                    .get_column_name_from_global_index(selected_column_index as usize);
                let _sorter = sort::Sorter::new(
                    self.shared_config.clone(),
                    selected_column_index as usize,
                    column_name,
                    desired_sort_type,
                );
                self.sorter = Some(Arc::new(_sorter));
            }
        } else {
            self.transient_message
                .replace("Press TAB and select a column before sorting".to_string());
        }
        Ok(())
    }

    fn handle_file_changed(&mut self) -> CsvlensResult<()> {
        if self._seekable_file.stream_active().is_some() {
            // No need to rebuild states for streaming input, just reload rows. Check this instead
            // of shared_config.is_streaming() since the latter can be set to false when streaming
            // is complete. We still don't want to rebuild states in that case.
            return self.rows_view.do_get_rows();
        }

        // Recreate finder if any
        if let Some(finder) = &self.finder {
            let target = finder.target().clone();
            self.create_finder_with_params(
                target,
                self.rows_view.is_filter(),
                // TODO: this assumes the previous column index is still valid after reload which
                // might not be true
                finder.column_index(),
                finder.starting_row_index(),
                None,
            );
        }

        // Recreate sorter if any
        if let Some(sorter) = &self.sorter {
            let selected_column_index = sorter.column_index as u64;
            let column_name = self
                .rows_view
                .get_column_name_from_global_index(selected_column_index as usize);
            let desired_sort_type = sorter.sort_type();
            let _sorter = sort::Sorter::new(
                self.shared_config.clone(),
                selected_column_index as usize,
                column_name,
                desired_sort_type,
            );
            self.sorter = Some(Arc::new(_sorter));
        }

        // Update reader but preserve other states such as cursor position
        let csvlens_reader = csv::CsvLensReader::new(self.shared_config.clone())?;
        let filter_finder = if let Some(finder) = &self.finder
            && self.rows_view.is_filter()
        {
            Some(finder)
        } else {
            None
        };
        self.rows_view.set_reader(csvlens_reader, filter_finder)?;
        self.rows_view.reset_sorter()?;

        // Re-apply columns filter if any
        if let Some(columns_filter) = &self.columns_filter {
            let columns_filter = Arc::new(ColumnsFilter::new(
                columns_filter.pattern(),
                self.rows_view.raw_headers(),
            ));
            self.columns_filter = Some(columns_filter.clone());
            self.rows_view.set_columns_filter(&columns_filter).unwrap();
        }

        self.csv_table_state.last_autoreload_at = Some(Instant::now());

        Ok(())
    }

    fn increase_cols_offset(&mut self) {
        if self.csv_table_state.has_more_cols_to_show() {
            // TODO: should this be a &mut method in RowsView that modifies cols_offset directly?
            let new_cols_offset = self.rows_view.cols_offset().num_skip.saturating_add(1);
            self.rows_view.set_cols_offset_num_skip(new_cols_offset);
        }
    }

    fn decrease_cols_offset(&mut self) {
        let new_cols_offset = self.rows_view.cols_offset().num_skip.saturating_sub(1);
        self.rows_view.set_cols_offset_num_skip(new_cols_offset);
    }

    fn adjust_column_width(&mut self, delta: i16) {
        if let Some(column_index) = self.get_selected_column_index()
            && let Some(view_layout) = &mut self.csv_table_state.view_layout
        {
            let current_width = view_layout.column_widths[column_index as usize];
            let new_width = (current_width as i16).saturating_add(delta);

            if new_width > 0 {
                let origin_index = self
                    .rows_view
                    .get_column_origin_index(column_index as usize);
                self.csv_table_state
                    .column_width_overrides
                    .set(origin_index, new_width as u16);
            }
        }
    }

    fn get_selected_column_index(&self) -> Option<u64> {
        // local index as in local to the view port
        if let Some(local_column_index) = self.rows_view.selection.column.index() {
            // return Some(local_column_index.saturating_add(self.csv_table_state.cols_offset));
            return Some(
                self.csv_table_state
                    .cols_offset
                    .get_filtered_column_index(local_column_index),
            );
        }
        None
    }

    fn get_global_selected_column_index(&self) -> Option<u64> {
        // TODO: maybe this and above should be methods provided by RowsView directly?
        self.get_selected_column_index()
            .map(|local_index| self.rows_view.get_column_origin_index(local_index as usize) as u64)
    }

    fn reset_filter(&mut self, preserve_row_selection: bool) {
        if self.finder.is_some() {
            self.finder = None;
            self.csv_table_state.finder_state = FinderState::FinderInactive;
            self.rows_view.reset_filter(preserve_row_selection).unwrap();
        }
    }

    fn reset_sorter(&mut self) {
        // TODO: consolidate rows_view reset
        self.sorter = None;
        self.rows_view.reset_sorter().unwrap();
    }

    fn handle_line_wrap_toggle(&mut self, mode: WrapMode, with_message: bool) {
        self.wrap_mode.toggle(mode);
        self.csv_table_state.enable_line_wrap = self.wrap_mode.is_enabled();
        self.csv_table_state.is_word_wrap = self.wrap_mode.is_word_wrap();
        if with_message {
            self.csv_table_state.reset_buffer();
            self.transient_message
                .replace(self.wrap_mode.transient_message());
        }
    }

    fn render_frame(&mut self, f: &mut Frame) {
        let size = f.area();

        // Render help; if so exit early.
        if self.help_page_state.is_active() {
            f.render_stateful_widget(help::HelpPage::new(), size, &mut self.help_page_state);
            return;
        }

        // Render table
        // TODO: check type of num_rows too big?
        let num_rows_adjusted = size.height.saturating_sub(self.num_rows_not_visible) as u64;
        if let Some(view_layout) = &self.csv_table_state.view_layout {
            self.rows_view.set_num_rows_rendered(
                view_layout.num_rows_renderable(num_rows_adjusted as u16) as u64,
            );
        }
        self.rows_view.set_num_rows(num_rows_adjusted).unwrap();
        self.frame_width = Some(size.width);

        let rows = self.rows_view.rows();
        let csv_table = CsvTable::new(self.rows_view.headers(), rows);
        f.render_stateful_widget(csv_table, size, &mut self.csv_table_state);
        if let Some((x, y)) = self.csv_table_state.cursor_xy {
            f.set_cursor_position(Position::new(x, y));
        }
    }

    fn draw<B: Backend>(&mut self, terminal: &mut Terminal<B>) -> CsvlensResult<()> {
        let start = Instant::now();
        let draw_result = terminal.draw(|f| {
            self.render_frame(f);
        });
        if let Err(e) = draw_result {
            return Err(CsvlensError::DrawError(format!("{e}")));
        }
        self.csv_table_state
            .debug_stats
            .render_elapsed(Some(start.elapsed()));
        Ok(())
    }
}
#[cfg(test)]
mod tests {
    use super::*;
    use ratatui::backend::TestBackend;
    use ratatui::buffer::Buffer;

    struct AppBuilder {
        original_filename: Option<String>,
        delimiter: Delimiter,
        show_stats: bool,
        echo_column: Option<String>,
        ignore_case: bool,
        no_headers: bool,
        columns_regex: Option<String>,
        filter_regex: Option<String>,
        find_regex: Option<String>,
        prompt: Option<String>,
        wrap_mode: Option<WrapMode>,
    }

    impl AppBuilder {
        fn new(filename: &str) -> Self {
            AppBuilder {
                original_filename: Some(filename.to_owned()),
                delimiter: Delimiter::Default,
                show_stats: false,
                echo_column: None,
                ignore_case: false,
                no_headers: false,
                columns_regex: None,
                filter_regex: None,
                find_regex: None,
                prompt: Some("stdin".to_owned()),
                wrap_mode: None,
            }
        }

        fn build(self) -> CsvlensResult<App> {
            App::new(
                self.original_filename,
                self.delimiter,
                self.show_stats,
                self.echo_column,
                self.ignore_case,
                self.no_headers,
                self.columns_regex,
                self.filter_regex,
                self.find_regex,
                None,
                false,
                self.prompt,
                self.wrap_mode,
                false,
                false,
            )
        }

        fn delimiter(mut self, delimiter: Delimiter) -> Self {
            self.delimiter = delimiter;
            self
        }

        fn ignore_case(mut self, ignore_case: bool) -> Self {
            self.ignore_case = ignore_case;
            self
        }

        fn no_headers(mut self, no_headers: bool) -> Self {
            self.no_headers = no_headers;
            self
        }

        fn columns_regex(mut self, columns: Option<String>) -> Self {
            self.columns_regex = columns;
            self
        }

        fn find_regex(mut self, find: Option<String>) -> Self {
            self.find_regex = find;
            self
        }

        fn filter_regex(mut self, filter: Option<String>) -> Self {
            self.filter_regex = filter;
            self
        }

        fn echo_column(mut self, column: &str) -> Self {
            self.echo_column = Some(column.to_owned());
            self
        }

        fn prompt(mut self, prompt: &str) -> Self {
            self.prompt = Some(prompt.to_owned());
            self
        }

        fn wrap_mode(mut self, wrap_mode: Option<WrapMode>) -> Self {
            self.wrap_mode = wrap_mode;
            self
        }
    }

    fn to_lines(buf: &Buffer) -> Vec<String> {
        let mut symbols: String = "".to_owned();
        let area = buf.area();
        for y in 0..area.bottom() {
            for x in 0..area.right() {
                let symbol = buf[Position::new(x, y)].symbol();
                symbols.push_str(symbol);
            }
            if y != area.bottom() - 1 {
                symbols.push('\n');
            }
        }

        symbols.split('\n').map(|s| s.to_string()).collect()
    }

    fn step_and_draw<B: Backend>(app: &mut App, terminal: &mut Terminal<B>, control: Control) {
        app.step(&control).unwrap();

        // While it's possible to step multiple times before any draw when
        // testing, App::render_frame() can update App's state (e.g. based on
        // the current terminal frame size) with information that might be
        // required for stepping to work correctly. Also, immediately drawing
        // after each step is what App::main_loop() will be doing.
        terminal.draw(|f| app.render_frame(f)).unwrap();
    }

    fn till_app_ready(app: &App) {
        app.rows_view.wait_internal();
        if let Some(sorter) = &app.sorter {
            sorter.wait_internal();
        }
        if let Some(finder) = &app.finder {
            finder.wait_internal();
        }
    }

    #[test]
    fn test_simple() {
        let mut app = AppBuilder::new("tests/data/simple.csv").build().unwrap();
        till_app_ready(&app);

        let backend = TestBackend::new(30, 10);
        let mut terminal = Terminal::new(backend).unwrap();

        step_and_draw(&mut app, &mut terminal, Control::Nothing);
        for _ in 0..7 {
            step_and_draw(&mut app, &mut terminal, Control::ScrollDown);
        }

        // TODO: need a less clunky way of checking expected output, and include
        // checking of styles. Probably using automatically generated fixtures
        // that are readable and can be easily updated
        let expected = vec![
            "──────────────────────────────",
            "      a     b                 ",
            "───┬──────────────┬───────────",
            "4  │  A4    B4    │           ",
            "5  │  A5    B5    │           ",
            "6  │  A6    B6    │           ",
            "7  │  A7    B7    │           ",
            "8  │  A8    B8    │           ",
            "───┴──────────────┴───────────",
            "stdin [Row 8/5000, Col 1/2]   ",
        ];
        let actual_buffer = terminal.backend().buffer().clone();
        let lines = to_lines(&actual_buffer);
        assert_eq!(lines, expected);
    }

    #[test]
    fn test_scroll_horizontal() {
        let mut app = AppBuilder::new("tests/data/cities.csv").build().unwrap();
        till_app_ready(&app);

        let backend = TestBackend::new(30, 10);
        let mut terminal = Terminal::new(backend).unwrap();

        step_and_draw(&mut app, &mut terminal, Control::Nothing);
        let expected = vec![
            "──────────────────────────────",
            "      La…    La…    La…    …  ",
            "───┬──────────────────────────",
            "1  │  41     5      59     …  ",
            "2  │  42     52     48     …  ",
            "3  │  46     35     59     …  ",
            "4  │  42     16     12     …  ",
            "5  │  43     37     48     …  ",
            "───┴──────────────────────────",
            "stdin [Row 1/128, Col 1/10]   ",
        ];
        let actual_buffer = terminal.backend().buffer().clone();
        let lines = to_lines(&actual_buffer);
        assert_eq!(lines, expected);

        step_and_draw(&mut app, &mut terminal, Control::ScrollPageRight);
        let expected = vec![
            "──────────────────────────────",
            "      NS    Lo…    Lo…    …   ",
            "───┬──────────────────────────",
            "1  │  N     80     39     …   ",
            "2  │  N     97     23     …   ",
            "3  │  N     120    30     …   ",
            "4  │  N     71     48     …   ",
            "5  │  N     89     46     …   ",
            "───┴──────────────────────────",
            "stdin [Row 1/128, Col 4/10]   ",
        ];
        let actual_buffer = terminal.backend().buffer().clone();
        let lines = to_lines(&actual_buffer);
        assert_eq!(lines, expected);

        step_and_draw(&mut app, &mut terminal, Control::ScrollPageLeft);
        let expected = vec![
            "──────────────────────────────",
            "      La…    La…    La…    …  ",
            "───┬──────────────────────────",
            "1  │  41     5      59     …  ",
            "2  │  42     52     48     …  ",
            "3  │  46     35     59     …  ",
            "4  │  42     16     12     …  ",
            "5  │  43     37     48     …  ",
            "───┴──────────────────────────",
            "stdin [Row 1/128, Col 1/10]   ",
        ];
        let actual_buffer = terminal.backend().buffer().clone();
        let lines = to_lines(&actual_buffer);
        assert_eq!(lines, expected);
    }

    #[test]
    fn test_filter_columns() {
        let mut app = AppBuilder::new("tests/data/cities.csv").build().unwrap();
        till_app_ready(&app);

        let backend = TestBackend::new(80, 10);
        let mut terminal = Terminal::new(backend).unwrap();

        step_and_draw(
            &mut app,
            &mut terminal,
            Control::FilterColumns("Lon|City".into()),
        );
        let expected = vec![
            "────────────────────────────────────────────────────────────────────────────────",
            "      LonD    LonM    LonS    City                                              ",
            "───┬─────────────────────────────────────────────┬──────────────────────────────",
            "1  │  80      39      0       Youngstown         │                              ",
            "2  │  97      23      23      Yankton            │                              ",
            "3  │  120     30      36      Yakima             │                              ",
            "4  │  71      48      0       Worcester          │                              ",
            "5  │  89      46      11      Wisconsin Dells    │                              ",
            "───┴─────────────────────────────────────────────┴──────────────────────────────",
            "stdin [Row 1/128, Col 1/4] [Filter \"Lon|City\": 4/10 cols]                       ",
        ];
        let actual_buffer = terminal.backend().buffer().clone();
        let lines = to_lines(&actual_buffer);
        assert_eq!(lines, expected);
    }

    #[test]
    fn test_filter_columns_irregular() {
        let mut app = AppBuilder::new("tests/data/irregular.csv").build().unwrap();
        till_app_ready(&app);

        let backend = TestBackend::new(80, 10);
        let mut terminal = Terminal::new(backend).unwrap();

        step_and_draw(
            &mut app,
            &mut terminal,
            Control::FilterColumns("COL2".into()),
        );
        let expected = vec![
            "────────────────────────────────────────────────────────────────────────────────",
            "       COL2                                                                     ",
            "───┬───────────┬────────────────────────────────────────────────────────────────",
            "1  │           │                                                                ",
            "2  │   v2      │                                                                ",
            "   │           │                                                                ",
            "   │           │                                                                ",
            "   │           │                                                                ",
            "───┴───────────┴────────────────────────────────────────────────────────────────",
            "stdin [Row 1/2, Col 1/1] [Filter \"COL2\": 1/2 cols]                              ",
        ];
        let actual_buffer = terminal.backend().buffer().clone();
        let lines = to_lines(&actual_buffer);
        assert_eq!(lines, expected);
    }

    #[test]
    fn test_filter_columns_case_sensitive() {
        let mut app = AppBuilder::new("tests/data/cities.csv").build().unwrap();
        till_app_ready(&app);

        let backend = TestBackend::new(80, 10);
        let mut terminal = Terminal::new(backend).unwrap();

        step_and_draw(
            &mut app,
            &mut terminal,
            Control::FilterColumns("city|state|wa".into()),
        );
        let expected = vec![
            "────────────────────────────────────────────────────────────────────────────────",
            "      LatD    LatM    LatS    NS    LonD    LonM    LonS    EW    City          ",
            "───┬────────────────────────────────────────────────────────────────────────────",
            "1  │  41      5       59      N     80      39      0       W     Youngstown    ",
            "2  │  42      52      48      N     97      23      23            Yankton       ",
            "3  │  46      35      59      N     120     30      36      W     Yakima        ",
            "4  │  42      16      12      N     71      48      0       W     Worcester     ",
            "5  │  43      37      48      N     89      46      11      W     Wisconsin…    ",
            "───┴────────────────────────────────────────────────────────────────────────────",
            "stdin [Row 1/128, Col 1/10] [Filter \"city|state|wa\": no match, showing all colum",
        ];
        let actual_buffer = terminal.backend().buffer().clone();
        let lines = to_lines(&actual_buffer);
        assert_eq!(lines, expected);
    }

    #[test]
    fn test_filter_columns_ignore_case() {
        let mut app = AppBuilder::new("tests/data/cities.csv")
            .ignore_case(true)
            .build()
            .unwrap();
        till_app_ready(&app);

        let backend = TestBackend::new(80, 10);
        let mut terminal = Terminal::new(backend).unwrap();

        step_and_draw(
            &mut app,
            &mut terminal,
            Control::FilterColumns("city|state|wa".into()),
        );
        let expected = vec![
            "────────────────────────────────────────────────────────────────────────────────",
            "      City               State                                                  ",
            "───┬──────────────────────────────┬─────────────────────────────────────────────",
            "1  │  Youngstown         OH       │                                             ",
            "2  │  Yankton            SD       │                                             ",
            "3  │  Yakima             WA       │                                             ",
            "4  │  Worcester          MA       │                                             ",
            "5  │  Wisconsin Dells    WI       │                                             ",
            "───┴──────────────────────────────┴─────────────────────────────────────────────",
            "stdin [Row 1/128, Col 1/2] [Filter \"(?i)city|state|wa\": 2/10 cols] [ignore-case]",
        ];
        let actual_buffer = terminal.backend().buffer().clone();
        let lines = to_lines(&actual_buffer);
        assert_eq!(lines, expected);
    }

    #[test]
    fn test_find_from_row_cursor() {
        let mut app = AppBuilder::new("tests/data/simple.csv").build().unwrap();
        till_app_ready(&app);

        let backend = TestBackend::new(30, 10);
        let mut terminal = Terminal::new(backend).unwrap();

        // scroll down for a bit before finding
        step_and_draw(&mut app, &mut terminal, Control::Nothing);
        for _ in 0..2 {
            step_and_draw(&mut app, &mut terminal, Control::ScrollDown);
        }

        // now find "1", it should not scroll back to A1, but to the next match after the current
        // row (A10)
        step_and_draw(&mut app, &mut terminal, Control::Find("1".into()));
        till_app_ready(&app);
        step_and_draw(&mut app, &mut terminal, Control::ScrollToNextFound);

        let expected = vec![
            "──────────────────────────────",
            "       a      b               ",
            "────┬────────────────┬────────",
            "10  │  A10    B10    │        ",
            "11  │  A11    B11    │        ",
            "12  │  A12    B12    │        ",
            "13  │  A13    B13    │        ",
            "14  │  A14    B14    │        ",
            "────┴────────────────┴────────",
            "stdin [Row 12/5000, Col 1/2] [",
        ];
        let actual_buffer = terminal.backend().buffer().clone();
        let lines = to_lines(&actual_buffer);
        assert_eq!(lines, expected);
    }

    #[test]
    fn test_extra_fields_in_some_rows() {
        // Test getting column widths should not fail on data with bad formatting (some rows having
        // more fields than the header)
        let mut app = AppBuilder::new("tests/data/bad_double_quote.csv")
            .delimiter(Delimiter::Comma)
            .build()
            .unwrap();
        till_app_ready(&app);

        let backend = TestBackend::new(35, 10);
        let mut terminal = Terminal::new(backend).unwrap();

        step_and_draw(&mut app, &mut terminal, Control::Nothing);
        let expected = vec![
            "───────────────────────────────────",
            "      Column1     \"column2\"        ",
            "───┬───────────────────────────┬───",
            "1  │  1           \"quote\"      │   ",
            "2  │  5           \"Comma       │   ",
            "   │                           │   ",
            "   │                           │   ",
            "   │                           │   ",
            "───┴───────────────────────────┴───",
            "stdin [Row 1/2, Col 1/2]           ",
        ];
        let actual_buffer = terminal.backend().buffer().clone();
        let lines = to_lines(&actual_buffer);
        assert_eq!(lines, expected);
    }

    #[test]
    fn test_extra_fields_right_most_border() {
        let mut app = AppBuilder::new("tests/data/bad_73.csv")
            .delimiter(Delimiter::Comma)
            .build()
            .unwrap();
        till_app_ready(&app);

        let backend = TestBackend::new(35, 10);
        let mut terminal = Terminal::new(backend).unwrap();

        step_and_draw(&mut app, &mut terminal, Control::Nothing);
        let expected = vec![
            "───────────────────────────────────",
            "      COL1     COL2                ",
            "───┬───────────────────┬───────────",
            "1  │  c1               │           ",
            "2  │  c2       v2      │           ",
            "3  │  c2       4       │           ",
            "4  │  c3               │           ",
            "5  │  c4               │           ",
            "───┴───────────────────┴───────────",
            "stdin [Row 1/13, Col 1/2]          ",
        ];
        let actual_buffer = terminal.backend().buffer().clone();
        let lines = to_lines(&actual_buffer);
        assert_eq!(lines, expected);
    }

    #[test]
    fn test_sniff_delimiter() {
        let mut app = AppBuilder::new("tests/data/small.bsv")
            .delimiter(Delimiter::Default)
            .build()
            .unwrap();
        till_app_ready(&app);

        let backend = TestBackend::new(30, 10);
        let mut terminal = Terminal::new(backend).unwrap();

        step_and_draw(&mut app, &mut terminal, Control::Nothing);
        let expected = vec![
            "──────────────────────────────",
            "      COL1    COL2            ",
            "───┬──────────────────┬───────",
            "1  │  c1      v1      │       ",
            "2  │  c2      v2      │       ",
            "   │                  │       ",
            "   │                  │       ",
            "   │                  │       ",
            "───┴──────────────────┴───────",
            "stdin [Row 1/2, Col 1/2]      ",
        ];
        let actual_buffer = terminal.backend().buffer().clone();
        let lines = to_lines(&actual_buffer);
        assert_eq!(lines, expected);
    }

    #[test]
    fn test_multi_lines() {
        let mut app = AppBuilder::new("tests/data/multi_lines.csv")
            .build()
            .unwrap();
        till_app_ready(&app);

        let backend = TestBackend::new(50, 30);
        let mut terminal = Terminal::new(backend).unwrap();

        step_and_draw(&mut app, &mut terminal, Control::Nothing);
        let expected = vec![
            "──────────────────────────────────────────────────",
            "      a    b                      c               ",
            "───┬─────────────────────────────────────────────┬",
            "1  │  1    this is a very lon…    12345          │",
            "2  │  2    thi…                   678910         │",
            "3  │  3    normal text now        123,456,789    │",
            "   │                                             │",
            "   │                                             │",
            "   │                                             │",
            "   │                                             │",
            "   │                                             │",
            "   │                                             │",
            "   │                                             │",
            "   │                                             │",
            "   │                                             │",
            "   │                                             │",
            "   │                                             │",
            "   │                                             │",
            "   │                                             │",
            "   │                                             │",
            "   │                                             │",
            "   │                                             │",
            "   │                                             │",
            "   │                                             │",
            "   │                                             │",
            "   │                                             │",
            "   │                                             │",
            "   │                                             │",
            "───┴─────────────────────────────────────────────┴",
            "stdin [Row 1/3, Col 1/3]                          ",
        ];
        let actual_buffer = terminal.backend().buffer().clone();
        let lines = to_lines(&actual_buffer);
        assert_eq!(lines, expected);

        step_and_draw(
            &mut app,
            &mut terminal,
            Control::ToggleLineWrap(WrapMode::Chars),
        );
        let expected = vec![
            "──────────────────────────────────────────────────",
            "      a    b                      c               ",
            "───┬─────────────────────────────────────────────┬",
            "1  │  1    this is a very long    12345          │",
            "   │        text that surely w                   │",
            "   │       ill not fit in your                   │",
            "   │        small screen                         │",
            "2  │  2    this                   678910         │",
            "   │       is                                    │",
            "   │       an                                    │",
            "   │       even                                  │",
            "   │       longer                                │",
            "   │       text                                  │",
            "   │       that                                  │",
            "   │       surely                                │",
            "   │       will                                  │",
            "   │       not                                   │",
            "   │       fit                                   │",
            "   │       in                                    │",
            "   │       your                                  │",
            "   │       small                                 │",
            "   │       screen                                │",
            "3  │  3    normal text now        123,456,789    │",
            "   │                                             │",
            "   │                                             │",
            "   │                                             │",
            "   │                                             │",
            "   │                                             │",
            "───┴─────────────────────────────────────────────┴",
            "Line wrap enabled                                 ",
        ];
        let actual_buffer = terminal.backend().buffer().clone();
        let lines = to_lines(&actual_buffer);
        assert_eq!(lines, expected);

        step_and_draw(
            &mut app,
            &mut terminal,
            Control::ToggleLineWrap(WrapMode::Words),
        );
        let expected = vec![
            "──────────────────────────────────────────────────",
            "      a    b                      c               ",
            "───┬─────────────────────────────────────────────┬",
            "1  │  1    this is a very         12345          │",
            "   │       long text that                        │",
            "   │       surely will not                       │",
            "   │       fit in your small                     │",
            "   │       screen                                │",
            "2  │  2    this                   678910         │",
            "   │       is                                    │",
            "   │       an                                    │",
            "   │       even                                  │",
            "   │       longer                                │",
            "   │       text                                  │",
            "   │       that                                  │",
            "   │       surely                                │",
            "   │       will                                  │",
            "   │       not                                   │",
            "   │       fit                                   │",
            "   │       in                                    │",
            "   │       your                                  │",
            "   │       small                                 │",
            "   │       screen                                │",
            "3  │  3    normal text now        123,456,789    │",
            "   │                                             │",
            "   │                                             │",
            "   │                                             │",
            "   │                                             │",
            "───┴─────────────────────────────────────────────┴",
            "Word wrap enabled                                 ",
        ];
        let actual_buffer = terminal.backend().buffer().clone();
        let lines = to_lines(&actual_buffer);
        assert_eq!(lines, expected);
    }

    #[test]
    fn test_multi_lines_degenerate_width() {
        let mut app = AppBuilder::new("tests/data/multi_lines.csv")
            .build()
            .unwrap();
        till_app_ready(&app);

        let backend = TestBackend::new(50, 30);
        let mut terminal = Terminal::new(backend).unwrap();

        step_and_draw(&mut app, &mut terminal, Control::Nothing);
        step_and_draw(&mut app, &mut terminal, Control::ToggleSelectionType);
        step_and_draw(&mut app, &mut terminal, Control::ScrollRight);
        step_and_draw(
            &mut app,
            &mut terminal,
            Control::ToggleLineWrap(WrapMode::Chars),
        );
        step_and_draw(&mut app, &mut terminal, Control::DecreaseWidth);
        step_and_draw(&mut app, &mut terminal, Control::DecreaseWidth);
        step_and_draw(&mut app, &mut terminal, Control::DecreaseWidth);
        step_and_draw(&mut app, &mut terminal, Control::DecreaseWidth);
        step_and_draw(&mut app, &mut terminal, Control::DecreaseWidth);

        let expected = vec![
            "──────────────────────────────────────────────────",
            "      a    …   c                                  ",
            "───┬──────────────────────────┬───────────────────",
            "1  │  1    …   12345          │                   ",
            "2  │  2    …   678910         │                   ",
            "3  │  3    …   123,456,789    │                   ",
            "   │                          │                   ",
            "   │                          │                   ",
            "   │                          │                   ",
            "   │                          │                   ",
            "   │                          │                   ",
            "   │                          │                   ",
            "   │                          │                   ",
            "   │                          │                   ",
            "   │                          │                   ",
            "   │                          │                   ",
            "   │                          │                   ",
            "   │                          │                   ",
            "   │                          │                   ",
            "   │                          │                   ",
            "   │                          │                   ",
            "   │                          │                   ",
            "   │                          │                   ",
            "   │                          │                   ",
            "   │                          │                   ",
            "   │                          │                   ",
            "   │                          │                   ",
            "   │                          │                   ",
            "───┴──────────────────────────┴───────────────────",
            "stdin [Row 1/3, Col 1/3]                          ",
        ];
        let actual_buffer = terminal.backend().buffer().clone();
        let lines = to_lines(&actual_buffer);
        assert_eq!(lines, expected);
    }

    #[test]
    fn test_multiple_newlines() {
        let mut app = AppBuilder::new("tests/data/multiple_newlines.csv")
            .build()
            .unwrap();
        till_app_ready(&app);

        let backend = TestBackend::new(50, 45);
        let mut terminal = Terminal::new(backend).unwrap();

        step_and_draw(&mut app, &mut terminal, Control::Nothing);
        step_and_draw(
            &mut app,
            &mut terminal,
            Control::ToggleLineWrap(WrapMode::Words),
        );
        let expected = vec![
            "──────────────────────────────────────────────────",
            "      a    b                      c               ",
            "───┬─────────────────────────────────────────────┬",
            "1  │  1    this is a very         12345          │",
            "   │       long text that                        │",
            "   │       surely will not                       │",
            "   │       fit in your small                     │",
            "   │       screen                                │",
            "2  │  2    this                   678910         │",
            "   │                                             │",
            "   │       is                                    │",
            "   │                                             │",
            "   │       an                                    │",
            "   │                                             │",
            "   │       even                                  │",
            "   │                                             │",
            "   │       longer                                │",
            "   │                                             │",
            "   │       text                                  │",
            "   │                                             │",
            "   │       that                                  │",
            "   │                                             │",
            "   │       surely                                │",
            "   │                                             │",
            "   │       will                                  │",
            "   │                                             │",
            "   │       not                                   │",
            "   │                                             │",
            "   │       fit                                   │",
            "   │                                             │",
            "   │       in                                    │",
            "   │                                             │",
            "   │       your                                  │",
            "   │                                             │",
            "   │       small                                 │",
            "   │                                             │",
            "   │       screen                                │",
            "3  │  3    normal text now        123,456,789    │",
            "   │                                             │",
            "   │                                             │",
            "   │                                             │",
            "   │                                             │",
            "   │                                             │",
            "───┴─────────────────────────────────────────────┴",
            "Word wrap enabled                                 ",
        ];
        let actual_buffer = terminal.backend().buffer().clone();
        let lines = to_lines(&actual_buffer);
        assert_eq!(lines, expected);
    }

    #[test]
    fn test_carriage_returns() {
        let mut app = AppBuilder::new("tests/data/multi_lines_carriage_return.csv")
            .build()
            .unwrap();
        till_app_ready(&app);

        let backend = TestBackend::new(50, 45);
        let mut terminal = Terminal::new(backend).unwrap();

        step_and_draw(&mut app, &mut terminal, Control::Nothing);
        step_and_draw(
            &mut app,
            &mut terminal,
            Control::ToggleLineWrap(WrapMode::Words),
        );
        let expected = vec![
            "──────────────────────────────────────────────────",
            "      a    b                      c               ",
            "───┬─────────────────────────────────────────────┬",
            "1  │  1    this is a very         12345          │",
            "   │       long text that                        │",
            "   │       surely will not                       │",
            "   │       fit in your small                     │",
            "   │       screen                                │",
            "2  │  2    this                   678910         │",
            "   │                                             │",
            "   │       is                                    │",
            "   │                                             │",
            "   │       an                                    │",
            "   │                                             │",
            "   │       even                                  │",
            "   │                                             │",
            "   │       longer                                │",
            "   │                                             │",
            "   │       text                                  │",
            "   │                                             │",
            "   │       that                                  │",
            "   │                                             │",
            "   │       surely                                │",
            "   │                                             │",
            "   │       will                                  │",
            "   │                                             │",
            "   │       not                                   │",
            "   │                                             │",
            "   │       fit                                   │",
            "   │                                             │",
            "   │       in                                    │",
            "   │                                             │",
            "   │       your                                  │",
            "   │                                             │",
            "   │       small                                 │",
            "   │                                             │",
            "   │       screen                                │",
            "3  │  3    normal text now        123,456,789    │",
            "   │                                             │",
            "   │                                             │",
            "   │                                             │",
            "   │                                             │",
            "   │                                             │",
            "───┴─────────────────────────────────────────────┴",
            "Word wrap enabled                                 ",
        ];
        let actual_buffer = terminal.backend().buffer().clone();
        let lines = to_lines(&actual_buffer);
        assert_eq!(lines, expected);
    }

    #[test]
    fn test_starts_with_newline() {
        let mut app = AppBuilder::new("tests/data/starts_with_newline.csv")
            .build()
            .unwrap();
        till_app_ready(&app);

        let backend = TestBackend::new(50, 20);
        let mut terminal = Terminal::new(backend).unwrap();

        step_and_draw(&mut app, &mut terminal, Control::Nothing);
        let expected = vec![
            "──────────────────────────────────────────────────",
            "      a    b                      c               ",
            "───┬─────────────────────────────────────────────┬",
            "1  │  1    this is a very lon…    12345          │",
            "2  │  2    …                      678910         │",
            "3  │  3    normal text now        123,456,789    │",
            "   │                                             │",
            "   │                                             │",
            "   │                                             │",
            "   │                                             │",
            "   │                                             │",
            "   │                                             │",
            "   │                                             │",
            "   │                                             │",
            "   │                                             │",
            "   │                                             │",
            "   │                                             │",
            "   │                                             │",
            "───┴─────────────────────────────────────────────┴",
            "stdin [Row 1/3, Col 1/3]                          ",
        ];
        let actual_buffer = terminal.backend().buffer().clone();
        let lines = to_lines(&actual_buffer);
        assert_eq!(lines, expected);

        step_and_draw(
            &mut app,
            &mut terminal,
            Control::ToggleLineWrap(WrapMode::Words),
        );
        let expected = vec![
            "──────────────────────────────────────────────────",
            "      a    b                      c               ",
            "───┬─────────────────────────────────────────────┬",
            "1  │  1    this is a very         12345          │",
            "   │       long text that                        │",
            "   │       surely will not                       │",
            "   │       fit in your small                     │",
            "   │       screen                                │",
            "2  │  2                           678910         │",
            "   │       starts with new                       │",
            "   │       line                                  │",
            "3  │  3    normal text now        123,456,789    │",
            "   │                                             │",
            "   │                                             │",
            "   │                                             │",
            "   │                                             │",
            "   │                                             │",
            "   │                                             │",
            "───┴─────────────────────────────────────────────┴",
            "Word wrap enabled                                 ",
        ];
        let actual_buffer = terminal.backend().buffer().clone();
        let lines = to_lines(&actual_buffer);
        assert_eq!(lines, expected);
    }

    #[test]
    fn test_specify_wrap_mode() {
        let mut app = AppBuilder::new("tests/data/multi_lines.csv")
            .wrap_mode(Some(WrapMode::Words))
            .build()
            .unwrap();
        till_app_ready(&app);

        let backend = TestBackend::new(50, 10);
        let mut terminal = Terminal::new(backend).unwrap();

        step_and_draw(&mut app, &mut terminal, Control::Nothing);
        let expected = vec![
            "──────────────────────────────────────────────────",
            "      a    b                      c               ",
            "───┬─────────────────────────────────────────────┬",
            "1  │  1    this is a very         12345          │",
            "   │       long text that                        │",
            "   │       surely will not                       │",
            "   │       fit in your small                     │",
            "   │       screen                                │",
            "───┴─────────────────────────────────────────────┴",
            "stdin [Row 1/3, Col 1/3]                          ",
        ];
        let actual_buffer = terminal.backend().buffer().clone();
        let lines = to_lines(&actual_buffer);
        assert_eq!(lines, expected);
    }

    #[test]
    fn test_column_widths_boundary_condition() {
        let mut app = AppBuilder::new("tests/data/cities.csv").build().unwrap();
        till_app_ready(&app);

        let backend = TestBackend::new(120, 10);
        let mut terminal = Terminal::new(backend).unwrap();

        step_and_draw(
            &mut app,
            &mut terminal,
            Control::Filter("Salt Lake City".into()),
        );
        till_app_ready(&app);
        step_and_draw(
            &mut app,
            &mut terminal,
            Control::FilterColumns("City".into()),
        );
        till_app_ready(&app);
        step_and_draw(&mut app, &mut terminal, Control::Nothing);
        let expected = vec![
            "────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────",
            "       City                                                                                                             ",
            "────┬────────────────────┬──────────────────────────────────────────────────────────────────────────────────────────────",
            "97  │  Salt Lake City    │                                                                                              ",
            "    │                    │                                                                                              ",
            "    │                    │                                                                                              ",
            "    │                    │                                                                                              ",
            "    │                    │                                                                                              ",
            "────┴────────────────────┴──────────────────────────────────────────────────────────────────────────────────────────────",
            "stdin [Row 97/128, Col 1/1] [Filter \"Salt Lake City\": 1/1] [Filter \"City\": 1/10 cols]                                   ",
        ];
        let actual_buffer = terminal.backend().buffer().clone();
        let lines = to_lines(&actual_buffer);
        assert_eq!(lines, expected);
    }

    #[test]
    fn test_scroll_right_most() {
        let mut app = AppBuilder::new("tests/data/cities.csv").build().unwrap();
        till_app_ready(&app);

        let backend = TestBackend::new(40, 10);
        let mut terminal = Terminal::new(backend).unwrap();

        // TODO: why is this first nothing step needed?
        step_and_draw(&mut app, &mut terminal, Control::Nothing);
        step_and_draw(&mut app, &mut terminal, Control::ScrollRightMost);
        let expected = vec![
            "────────────────────────────────────────",
            "      LonS    EW    City      State     ",
            "───┬───────────────────────────────────┬",
            "1  │  0       W     Young…    OH       │",
            "2  │  23            Yankt…    SD       │",
            "3  │  36      W     Yakima    WA       │",
            "4  │  0       W     Worce…    MA       │",
            "5  │  11      W     Wisco…    WI       │",
            "───┴───────────────────────────────────┴",
            "stdin [Row 1/128, Col 7/10]             ",
        ];
        let actual_buffer = terminal.backend().buffer().clone();
        let lines = to_lines(&actual_buffer);
        assert_eq!(lines, expected);
    }

    #[test]
    fn test_scroll_left_most() {
        let mut app = AppBuilder::new("tests/data/cities.csv").build().unwrap();
        till_app_ready(&app);

        let backend = TestBackend::new(40, 10);
        let mut terminal = Terminal::new(backend).unwrap();

        // TODO: why is this first nothing step needed?
        step_and_draw(&mut app, &mut terminal, Control::Nothing);
        step_and_draw(&mut app, &mut terminal, Control::ScrollRightMost);
        step_and_draw(&mut app, &mut terminal, Control::ScrollLeftMost);
        let expected = vec![
            "────────────────────────────────────────",
            "      LatD    LatM    LatS    NS    …   ",
            "───┬────────────────────────────────────",
            "1  │  41      5       59      N     …   ",
            "2  │  42      52      48      N     …   ",
            "3  │  46      35      59      N     …   ",
            "4  │  42      16      12      N     …   ",
            "5  │  43      37      48      N     …   ",
            "───┴────────────────────────────────────",
            "stdin [Row 1/128, Col 1/10]             ",
        ];
        let actual_buffer = terminal.backend().buffer().clone();
        let lines = to_lines(&actual_buffer);
        assert_eq!(lines, expected);
    }

    #[test]
    fn test_scroll_half_page() {
        let mut app = AppBuilder::new("tests/data/cities.csv").build().unwrap();
        till_app_ready(&app);

        let backend = TestBackend::new(40, 10);
        let mut terminal = Terminal::new(backend).unwrap();

        // TODO: since some states are updated late only during rendering, sometimes some extra
        // no-ops are required to warm up the states. I don't like it, but this is how it has to be
        // in tests for now.
        step_and_draw(&mut app, &mut terminal, Control::Nothing);
        step_and_draw(&mut app, &mut terminal, Control::Nothing);
        step_and_draw(&mut app, &mut terminal, Control::ScrollHalfPageDown);
        step_and_draw(&mut app, &mut terminal, Control::ScrollHalfPageDown);
        let expected = vec![
            "────────────────────────────────────────",
            "      LatD    LatM    LatS    NS    …   ",
            "───┬────────────────────────────────────",
            "5  │  43      37      48      N     …   ",
            "6  │  36      5       59      N     …   ",
            "7  │  49      52      48      N     …   ",
            "8  │  39      11      23      N     …   ",
            "9  │  34      14      24      N     …   ",
            "───┴────────────────────────────────────",
            "stdin [Row 5/128, Col 1/10]             ",
        ];
        let actual_buffer = terminal.backend().buffer().clone();
        let lines = to_lines(&actual_buffer);
        assert_eq!(lines, expected);

        step_and_draw(&mut app, &mut terminal, Control::Nothing);
        step_and_draw(&mut app, &mut terminal, Control::ScrollHalfPageUp);
        let expected = vec![
            "────────────────────────────────────────",
            "      LatD    LatM    LatS    NS    …   ",
            "───┬────────────────────────────────────",
            "3  │  46      35      59      N     …   ",
            "4  │  42      16      12      N     …   ",
            "5  │  43      37      48      N     …   ",
            "6  │  36      5       59      N     …   ",
            "7  │  49      52      48      N     …   ",
            "───┴────────────────────────────────────",
            "stdin [Row 3/128, Col 1/10]             ",
        ];
        let actual_buffer = terminal.backend().buffer().clone();
        let lines = to_lines(&actual_buffer);
        assert_eq!(lines, expected);
    }

    #[test]
    fn test_resize_column() {
        let mut app = AppBuilder::new("tests/data/cities.csv").build().unwrap();
        till_app_ready(&app);

        let backend = TestBackend::new(80, 10);
        let mut terminal = Terminal::new(backend).unwrap();

        // Check column widths are adjusted correctly
        step_and_draw(&mut app, &mut terminal, Control::ToggleSelectionType);
        step_and_draw(&mut app, &mut terminal, Control::ScrollRight);
        step_and_draw(&mut app, &mut terminal, Control::ScrollRight);
        step_and_draw(&mut app, &mut terminal, Control::IncreaseWidth);
        step_and_draw(&mut app, &mut terminal, Control::IncreaseWidth);
        step_and_draw(&mut app, &mut terminal, Control::ScrollLeft);
        step_and_draw(&mut app, &mut terminal, Control::DecreaseWidth);
        let actual_buffer = terminal.backend().buffer().clone();
        let lines = to_lines(&actual_buffer);
        let expected = vec![
            "────────────────────────────────────────────────────────────────────────────────",
            "      LatD    …   LatS            NS    LonD    LonM    LonS    EW    City      ",
            "───┬────────────────────────────────────────────────────────────────────────────",
            "1  │  41      …   59              N     80      39      0       W     Young…    ",
            "2  │  42      …   48              N     97      23      23            Yankt…    ",
            "3  │  46      …   59              N     120     30      36      W     Yakima    ",
            "4  │  42      …   12              N     71      48      0       W     Worce…    ",
            "5  │  43      …   48              N     89      46      11      W     Wisco…    ",
            "───┴────────────────────────────────────────────────────────────────────────────",
            "stdin [Row 1/128, Col 1/10]                                                     ",
        ];
        assert_eq!(lines, expected);

        // Check overridden column widths still have  when columns are filtered
        step_and_draw(
            &mut app,
            &mut terminal,
            Control::FilterColumns("Lat".into()),
        );
        till_app_ready(&app);
        let actual_buffer = terminal.backend().buffer().clone();
        let lines = to_lines(&actual_buffer);
        let expected = vec![
            "────────────────────────────────────────────────────────────────────────────────",
            "      LatD    …   LatS                                                          ",
            "───┬──────────────────────────────┬─────────────────────────────────────────────",
            "1  │  41      …   59              │                                             ",
            "2  │  42      …   48              │                                             ",
            "3  │  46      …   59              │                                             ",
            "4  │  42      …   12              │                                             ",
            "5  │  43      …   48              │                                             ",
            "───┴──────────────────────────────┴─────────────────────────────────────────────",
            "stdin [Row 1/128, Col 1/3] [Filter \"Lat\": 3/10 cols]                            ",
        ];
        assert_eq!(lines, expected);

        // Check reset
        step_and_draw(&mut app, &mut terminal, Control::Reset);
        let actual_buffer = terminal.backend().buffer().clone();
        let lines = to_lines(&actual_buffer);
        let expected = vec![
            "────────────────────────────────────────────────────────────────────────────────",
            "      LatD    LatM    LatS    NS    LonD    LonM    LonS    EW    City          ",
            "───┬────────────────────────────────────────────────────────────────────────────",
            "1  │  41      5       59      N     80      39      0       W     Youngstown    ",
            "2  │  42      52      48      N     97      23      23            Yankton       ",
            "3  │  46      35      59      N     120     30      36      W     Yakima        ",
            "4  │  42      16      12      N     71      48      0       W     Worcester     ",
            "5  │  43      37      48      N     89      46      11      W     Wisconsin…    ",
            "───┴────────────────────────────────────────────────────────────────────────────",
            "stdin [Row 1/128, Col 1/10]                                                     ",
        ];
        assert_eq!(lines, expected);
    }

    #[test]
    fn test_sorting() {
        let mut app = AppBuilder::new("tests/data/cities.csv").build().unwrap();
        till_app_ready(&app);

        let backend = TestBackend::new(100, 10);
        let mut terminal = Terminal::new(backend).unwrap();

        step_and_draw(&mut app, &mut terminal, Control::ToggleSelectionType);
        // Sort by City (no tie)
        for _ in 0..8 {
            step_and_draw(&mut app, &mut terminal, Control::ScrollRight);
        }
        step_and_draw(&mut app, &mut terminal, Control::ToggleSort);
        till_app_ready(&app);
        step_and_draw(&mut app, &mut terminal, Control::Nothing);

        let actual_buffer = terminal.backend().buffer().clone();
        let lines = to_lines(&actual_buffer);
        let expected = vec![
            "────────────────────────────────────────────────────────────────────────────────────────────────────",
            "        LatD    LatM    LatS    NS    LonD    LonM    LonS    EW    City [▴]      State             ",
            "─────┬─────────────────────────────────────────────────────────────────────────────────────┬────────",
            "128  │  41      9       35      N     81      14      23      W     Ravenna       OH       │        ",
            "127  │  40      19      48      N     75      55      48      W     Reading       PA       │        ",
            "126  │  40      10      48      N     122     14      23      W     Red Bluff     CA       │        ",
            "125  │  50      25      11      N     104     39      0       W     Regina        SA       │        ",
            "124  │  39      31      12      N     119     48      35      W     Reno          NV       │        ",
            "─────┴─────────────────────────────────────────────────────────────────────────────────────┴────────",
            "stdin [Row 128/128, Col 1/10]                                                                       ",
        ];
        assert_eq!(lines, expected);

        // Check descending
        step_and_draw(&mut app, &mut terminal, Control::ToggleSort);
        till_app_ready(&app);
        let actual_buffer = terminal.backend().buffer().clone();
        let lines = to_lines(&actual_buffer);
        let expected = vec![
            "────────────────────────────────────────────────────────────────────────────────────────────────────",
            "      LatD    LatM    LatS    NS    LonD    LonM    LonS    EW    City [▾]           State          ",
            "───┬──────────────────────────────────────────────────────────────────────────────────────────┬─────",
            "1  │  41      5       59      N     80      39      0       W     Youngstown         OH       │     ",
            "2  │  42      52      48      N     97      23      23            Yankton            SD       │     ",
            "3  │  46      35      59      N     120     30      36      W     Yakima             WA       │     ",
            "4  │  42      16      12      N     71      48      0       W     Worcester          MA       │     ",
            "5  │  43      37      48      N     89      46      11      W     Wisconsin Dells    WI       │     ",
            "───┴──────────────────────────────────────────────────────────────────────────────────────────┴─────",
            "stdin [Row 1/128, Col 1/10]                                                                         ",
        ];
        assert_eq!(lines, expected);
    }

    #[test]
    fn test_natural_sorting() {
        let mut app = AppBuilder::new("tests/data/natural_sort.csv")
            .build()
            .unwrap();
        till_app_ready(&app);

        let backend = TestBackend::new(80, 10);
        let mut terminal = Terminal::new(backend).unwrap();

        step_and_draw(&mut app, &mut terminal, Control::ToggleSelectionType);
        // Select the name column (first column, no need to scroll)
        step_and_draw(&mut app, &mut terminal, Control::ToggleNaturalSort);
        till_app_ready(&app);
        step_and_draw(&mut app, &mut terminal, Control::Nothing);

        let actual_buffer = terminal.backend().buffer().clone();
        let lines = to_lines(&actual_buffer);
        let expected = vec![
            "────────────────────────────────────────────────────────────────────────────────",
            "       name [▴N]      value                                                     ",
            "────┬──────────────────────────┬────────────────────────────────────────────────",
            "13  │  appendix       0        │                                                ",
            "9   │  chapter1       1        │                                                ",
            "11  │  chapter2       2        │                                                ",
            "10  │  chapter10      10       │                                                ",
            "12  │  chapter20      20       │                                                ",
            "────┴──────────────────────────┴────────────────────────────────────────────────",
            "stdin [Row 13/13, Col 1/2]                                                      ",
        ];
        assert_eq!(lines, expected);

        // Check descending
        step_and_draw(&mut app, &mut terminal, Control::ToggleNaturalSort);
        till_app_ready(&app);
        step_and_draw(&mut app, &mut terminal, Control::Nothing);
        let actual_buffer = terminal.backend().buffer().clone();
        let lines = to_lines(&actual_buffer);
        let expected = vec![
            "────────────────────────────────────────────────────────────────────────────────",
            "      name [▾N]      value                                                      ",
            "───┬──────────────────────────┬─────────────────────────────────────────────────",
            "8  │  file20.txt     20       │                                                 ",
            "6  │  file10.txt     10       │                                                 ",
            "7  │  file2.txt      2        │                                                 ",
            "5  │  file1.txt      1        │                                                 ",
            "4  │  disk11         110      │                                                 ",
            "───┴──────────────────────────┴─────────────────────────────────────────────────",
            "stdin [Row 8/13, Col 1/2]                                                       ",
        ];
        assert_eq!(lines, expected);
    }

    #[test]
    fn test_toggle_auto_vs_natural_sorting() {
        let mut app = AppBuilder::new("tests/data/natural_sort.csv")
            .build()
            .unwrap();
        till_app_ready(&app);

        let backend = TestBackend::new(80, 10);
        let mut terminal = Terminal::new(backend).unwrap();

        step_and_draw(&mut app, &mut terminal, Control::ToggleSelectionType);
        // Select the name column (first column, no need to scroll)
        step_and_draw(&mut app, &mut terminal, Control::ToggleNaturalSort);
        till_app_ready(&app);
        step_and_draw(&mut app, &mut terminal, Control::Nothing);

        let actual_buffer = terminal.backend().buffer().clone();
        let lines = to_lines(&actual_buffer);
        let expected = vec![
            "────────────────────────────────────────────────────────────────────────────────",
            "       name [▴N]      value                                                     ",
            "────┬──────────────────────────┬────────────────────────────────────────────────",
            "13  │  appendix       0        │                                                ",
            "9   │  chapter1       1        │                                                ",
            "11  │  chapter2       2        │                                                ",
            "10  │  chapter10      10       │                                                ",
            "12  │  chapter20      20       │                                                ",
            "────┴──────────────────────────┴────────────────────────────────────────────────",
            "stdin [Row 13/13, Col 1/2]                                                      ",
        ];
        assert_eq!(lines, expected);

        // Check toggling back to auto sorting
        step_and_draw(&mut app, &mut terminal, Control::ToggleSort);
        till_app_ready(&app);
        step_and_draw(&mut app, &mut terminal, Control::Nothing);
        let actual_buffer = terminal.backend().buffer().clone();
        let lines = to_lines(&actual_buffer);
        let expected = vec![
            "────────────────────────────────────────────────────────────────────────────────",
            "       name [▴]      value                                                      ",
            "────┬─────────────────────────┬─────────────────────────────────────────────────",
            "13  │  appendix      0        │                                                 ",
            "9   │  chapter1      1        │                                                 ",
            "10  │  chapter10     10       │                                                 ",
            "11  │  chapter2      2        │                                                 ",
            "12  │  chapter20     20       │                                                 ",
            "────┴─────────────────────────┴─────────────────────────────────────────────────",
            "stdin [Row 13/13, Col 1/2]                                                      ",
        ];
        assert_eq!(lines, expected);
    }

    #[test]
    fn test_sorting_with_filter() {
        let mut app = AppBuilder::new("tests/data/cities.csv").build().unwrap();
        till_app_ready(&app);

        let backend = TestBackend::new(80, 10);
        let mut terminal = Terminal::new(backend).unwrap();

        step_and_draw(&mut app, &mut terminal, Control::ToggleSelectionType);
        // Sort by City (no tie)
        for _ in 0..8 {
            step_and_draw(&mut app, &mut terminal, Control::ScrollRight);
        }
        step_and_draw(&mut app, &mut terminal, Control::ToggleSort);
        till_app_ready(&app);

        // Toggle back to row selection mode before filtering
        step_and_draw(&mut app, &mut terminal, Control::ToggleSelectionType);
        step_and_draw(&mut app, &mut terminal, Control::ToggleSelectionType);

        step_and_draw(&mut app, &mut terminal, Control::Nothing);

        step_and_draw(&mut app, &mut terminal, Control::Filter("San".into()));
        step_and_draw(
            &mut app,
            &mut terminal,
            Control::FilterColumns("Lat|City".into()),
        );

        till_app_ready(&app);
        step_and_draw(&mut app, &mut terminal, Control::Nothing);

        let actual_buffer = terminal.backend().buffer().clone();
        let lines = to_lines(&actual_buffer);
        let expected = vec![
            "────────────────────────────────────────────────────────────────────────────────",
            "       LatD    LatM    LatS    City [▴]                                         ",
            "────┬────────────────────────────────────────────┬──────────────────────────────",
            "96  │  31      27      35      San Angelo        │                              ",
            "95  │  29      25      12      San Antonio       │                              ",
            "94  │  34      6       36      San Bernardino    │                              ",
            "93  │  32      42      35      San Diego         │                              ",
            "91  │  37      46      47      San Francisco     │                              ",
            "────┴────────────────────────────────────────────┴──────────────────────────────",
            "stdin [Row 96/128, Col 1/4] [Filter \"San\": 1/11] [Filter \"Lat|City\": 4/10 cols] ",
        ];
        assert_eq!(lines, expected);

        // Check descending
        step_and_draw(&mut app, &mut terminal, Control::ToggleSelectionType);
        step_and_draw(&mut app, &mut terminal, Control::ToggleSort);
        till_app_ready(&app);
        step_and_draw(&mut app, &mut terminal, Control::Nothing);
        let actual_buffer = terminal.backend().buffer().clone();
        let lines = to_lines(&actual_buffer);
        let expected = vec![
            "────────────────────────────────────────────────────────────────────────────────",
            "       LatD    LatM    LatS    City [▾]                                         ",
            "────┬───────────────────────────────────────────┬───────────────────────────────",
            "86  │  38      26      23      Santa Rosa       │                               ",
            "87  │  35      40      48      Santa Fe         │                               ",
            "88  │  34      25      11      Santa Barbara    │                               ",
            "89  │  33      45      35      Santa Ana        │                               ",
            "92  │  41      27      0       Sandusky         │                               ",
            "────┴───────────────────────────────────────────┴───────────────────────────────",
            "stdin [Row 86/128, Col 1/4] [Filter \"San\": -/11] [Filter \"Lat|City\": 4/10 cols] ",
        ];
        assert_eq!(lines, expected);
    }

    #[test]
    fn test_no_headers() {
        let mut app = AppBuilder::new("tests/data/no_headers.csv")
            .no_headers(true)
            .build()
            .unwrap();
        till_app_ready(&app);

        let backend = TestBackend::new(30, 10);
        let mut terminal = Terminal::new(backend).unwrap();

        step_and_draw(&mut app, &mut terminal, Control::Nothing);
        for _ in 0..7 {
            step_and_draw(&mut app, &mut terminal, Control::ScrollDown);
        }

        let expected = vec![
            "──────────────────────────────",
            "      1     2                 ",
            "───┬──────────────┬───────────",
            "4  │  A4    B4    │           ",
            "5  │  A5    B5    │           ",
            "6  │  A6    B6    │           ",
            "7  │  A7    B7    │           ",
            "8  │  A8    B8    │           ",
            "───┴──────────────┴───────────",
            "stdin [Row 8/20, Col 1/2]     ",
        ];
        let actual_buffer = terminal.backend().buffer().clone();
        let lines = to_lines(&actual_buffer);
        assert_eq!(lines, expected);
    }

    #[test]
    fn test_cli_columns_option() {
        let mut app = AppBuilder::new("tests/data/cities.csv")
            .columns_regex(Some("Lat".to_string()))
            .build()
            .unwrap();
        till_app_ready(&app);

        let backend = TestBackend::new(80, 10);
        let mut terminal = Terminal::new(backend).unwrap();
        step_and_draw(&mut app, &mut terminal, Control::Nothing);

        let expected = vec![
            "────────────────────────────────────────────────────────────────────────────────",
            "      LatD    LatM    LatS                                                      ",
            "───┬──────────────────────────┬─────────────────────────────────────────────────",
            "1  │  41      5       59      │                                                 ",
            "2  │  42      52      48      │                                                 ",
            "3  │  46      35      59      │                                                 ",
            "4  │  42      16      12      │                                                 ",
            "5  │  43      37      48      │                                                 ",
            "───┴──────────────────────────┴─────────────────────────────────────────────────",
            "stdin [Row 1/128, Col 1/3] [Filter \"Lat\": 3/10 cols]                            ",
        ];
        let actual_buffer = terminal.backend().buffer().clone();
        let lines = to_lines(&actual_buffer);
        assert_eq!(lines, expected);
    }

    #[test]
    fn test_cli_filter_option() {
        let mut app = AppBuilder::new("tests/data/cities.csv")
            .filter_regex(Some("San".to_string()))
            .build()
            .unwrap();
        till_app_ready(&app);

        let backend = TestBackend::new(80, 10);
        let mut terminal = Terminal::new(backend).unwrap();
        step_and_draw(&mut app, &mut terminal, Control::Nothing);

        let expected = vec![
            "────────────────────────────────────────────────────────────────────────────────",
            "       LatD    LatM    LatS    NS    LonD    LonM    LonS    EW    City         ",
            "────┬───────────────────────────────────────────────────────────────────────────",
            "86  │  38      26      23      N     122     43      12      W     Santa Ro…    ",
            "87  │  35      40      48      N     105     56      59      W     Santa Fe     ",
            "88  │  34      25      11      N     119     41      59      W     Santa Ba…    ",
            "89  │  33      45      35      N     117     52      12      W     Santa Ana    ",
            "90  │  37      20      24      N     121     52      47      W     San Jose     ",
            "────┴───────────────────────────────────────────────────────────────────────────",
            "stdin [Row 86/128, Col 1/10] [Filter \"San\": 1/11]                               ",
        ];
        let actual_buffer = terminal.backend().buffer().clone();
        let lines = to_lines(&actual_buffer);
        assert_eq!(lines, expected);
    }

    #[test]
    fn test_filter_rows_for_specific_column() {
        let mut app = AppBuilder::new("tests/data/cities.csv").build().unwrap();
        till_app_ready(&app);

        let backend = TestBackend::new(80, 10);
        let mut terminal = Terminal::new(backend).unwrap();

        step_and_draw(&mut app, &mut terminal, Control::ToggleSelectionType);
        step_and_draw(&mut app, &mut terminal, Control::ScrollRight);
        step_and_draw(&mut app, &mut terminal, Control::Filter("^1".into()));

        till_app_ready(&app);
        step_and_draw(&mut app, &mut terminal, Control::Nothing);

        let actual_buffer = terminal.backend().buffer().clone();
        let lines = to_lines(&actual_buffer);
        let expected = vec![
            "────────────────────────────────────────────────────────────────────────────────",
            "       LatD    LatM    LatS    NS    LonD    LonM    LonS    EW    City         ",
            "────┬───────────────────────────────────────────────────────────────────────────",
            "4   │  42      16      12      N     71      48      0       W     Worcester    ",
            "8   │  39      11      23      N     78      9       36      W     Winchest…    ",
            "9   │  34      14      24      N     77      55      11      W     Wilmingt…    ",
            "12  │  41      15      0       N     77      0       0       W     Williams…    ",
            "20  │  31      13      11      N     82      20      59      W     Waycross     ",
            "────┴───────────────────────────────────────────────────────────────────────────",
            "stdin [Row 4/128, Col 1/10] [Filter \"^1\" in LatM: -/19]                         ",
        ];
        assert_eq!(lines, expected);
    }

    #[test]
    fn test_filter_like_cell() {
        let mut app = AppBuilder::new("tests/data/cities.csv").build().unwrap();
        till_app_ready(&app);

        let backend = TestBackend::new(80, 10);
        let mut terminal = Terminal::new(backend).unwrap();

        // Enter cell selection mode
        step_and_draw(&mut app, &mut terminal, Control::ToggleSelectionType);
        step_and_draw(&mut app, &mut terminal, Control::ToggleSelectionType);

        // Select the State column
        for _ in 0..10 {
            step_and_draw(&mut app, &mut terminal, Control::ScrollRight);
        }
        step_and_draw(&mut app, &mut terminal, Control::FilterLikeCell);

        till_app_ready(&app);
        step_and_draw(&mut app, &mut terminal, Control::Nothing);

        let actual_buffer = terminal.backend().buffer().clone();
        let lines = to_lines(&actual_buffer);
        let expected = vec![
            "────────────────────────────────────────────────────────────────────────────────",
            "       LatS    NS    LonD    LonM    LonS    EW    City            State        ",
            "────┬───────────────────────────────────────────────────────────────────────┬───",
            "1   │  59      N     80      39      0       W     Youngstown      OH       │   ",
            "50  │  0       N     83      32      24      W     Toledo          OH       │   ",
            "62  │  36      N     80      37      12      W     Steubenville    OH       │   ",
            "65  │  11      N     83      48      35      W     Springfield     OH       │   ",
            "92  │  0       N     82      42      35      W     Sandusky        OH       │   ",
            "────┴───────────────────────────────────────────────────────────────────────┴───",
            "stdin [Row 1/128, Col 3/10] [Filter \"^OH$\" in State: 1/6]                       ",
        ];
        assert_eq!(lines, expected);
    }

    #[test]
    fn test_filter_like_cell_escape() {
        let mut app = AppBuilder::new("tests/data/filter.csv").build().unwrap();
        till_app_ready(&app);

        let backend = TestBackend::new(80, 10);
        let mut terminal = Terminal::new(backend).unwrap();

        // Enter cell selection mode
        step_and_draw(&mut app, &mut terminal, Control::ToggleSelectionType);
        step_and_draw(&mut app, &mut terminal, Control::ToggleSelectionType);

        // Filter like the selected cell
        step_and_draw(&mut app, &mut terminal, Control::FilterLikeCell);
        till_app_ready(&app);

        step_and_draw(&mut app, &mut terminal, Control::Nothing);

        let actual_buffer = terminal.backend().buffer().clone();
        let lines = to_lines(&actual_buffer);
        let expected = vec![
            "────────────────────────────────────────────────────────────────────────────────",
            "      a             b                                                           ",
            "───┬─────────────────────┬──────────────────────────────────────────────────────",
            "1  │  $(#1#2#.3)    1    │                                                      ",
            "   │                     │                                                      ",
            "   │                     │                                                      ",
            "   │                     │                                                      ",
            "   │                     │                                                      ",
            "───┴─────────────────────┴──────────────────────────────────────────────────────",
            "stdin [Row 1/3, Col 1/2] [Filter \"^\\$\\(\\#1\\#2\\#\\.3\\)$\" in a: 1/1]               ",
        ];
        assert_eq!(lines, expected);
    }

    #[test]
    fn test_input_cursor() {
        let mut app = AppBuilder::new("tests/data/cities.csv").build().unwrap();
        till_app_ready(&app);

        let backend = TestBackend::new(30, 10);
        let mut terminal = Terminal::new(backend).unwrap();

        step_and_draw(&mut app, &mut terminal, Control::Nothing);
        step_and_draw(
            &mut app,
            &mut terminal,
            Control::BufferContent("abc".into()),
        );
        assert_eq!(app.csv_table_state.cursor_xy, Some((3, 9)));
        let expected = vec![
            "──────────────────────────────",
            "      La…    La…    La…    …  ",
            "───┬──────────────────────────",
            "1  │  41     5      59     …  ",
            "2  │  42     52     48     …  ",
            "3  │  46     35     59     …  ",
            "4  │  42     16     12     …  ",
            "5  │  43     37     48     …  ",
            "───┴──────────────────────────",
            "abc                           ",
        ];
        let actual_buffer = terminal.backend().buffer().clone();
        let lines = to_lines(&actual_buffer);
        assert_eq!(lines, expected);
    }

    #[test]
    fn test_one_wide_column_but_terminal_is_wider() {
        let mut app = AppBuilder::new("tests/data/one_wide_column.txt")
            .build()
            .unwrap();
        till_app_ready(&app);

        let backend = TestBackend::new(180, 8);
        let mut terminal = Terminal::new(backend).unwrap();

        step_and_draw(&mut app, &mut terminal, Control::Nothing);
        let expected = vec![
            "────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────",
            "      id    text                                                                                                                                        label                       ",
            "───┬──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┬─────────────",
            "1  │  1     this is a very very very very very very very very very very very very very very very very very very very very very very very long thing     hotdog        │             ",
            "2  │  2     this is a very very very very very very very very very very very very very very very very very very very very very very very short thing    not_hotdog    │             ",
            "   │                                                                                                                                                                  │             ",
            "───┴──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┴─────────────",
            "stdin [Row 1/2, Col 1/3]                                                                                                                                                            ",
        ];
        let actual_buffer = terminal.backend().buffer().clone();
        let lines = to_lines(&actual_buffer);
        assert_eq!(lines, expected);
    }

    #[test]
    fn test_echo_column() {
        let mut app = AppBuilder::new("tests/data/cities.csv")
            .echo_column("City")
            .build()
            .unwrap();
        till_app_ready(&app);

        let backend = TestBackend::new(180, 8);
        let mut terminal = Terminal::new(backend).unwrap();

        step_and_draw(&mut app, &mut terminal, Control::ScrollDown);
        step_and_draw(&mut app, &mut terminal, Control::ScrollDown);
        step_and_draw(&mut app, &mut terminal, Control::ScrollDown);

        let selection = app.get_selection();
        assert_eq!(selection, Some("Worcester".to_string()));
    }

    #[test]
    fn test_echo_column_not_found() {
        let app = AppBuilder::new("tests/data/cities.csv")
            .echo_column("Cityz")
            .build();
        if let Err(e) = app {
            assert_eq!(e.to_string(), "Column name not found: Cityz");
        } else {
            panic!("Expected error");
        }
    }

    #[test]
    fn test_irregular_columns_scrolling() {
        let mut app = AppBuilder::new("tests/data/irregular_last_row.csv")
            .no_headers(true)
            .build()
            .unwrap();
        till_app_ready(&app);

        let backend = TestBackend::new(50, 10);
        let mut terminal = Terminal::new(backend).unwrap();

        step_and_draw(&mut app, &mut terminal, Control::Nothing);
        let expected = vec![
            "──────────────────────────────────────────────────",
            "      1            2            3            4    ",
            "───┬──────────────────────────────────────────────",
            "1  │  AAAAAAAA…    BBBBBBBB…    AAAAAAAA…    …    ",
            "2  │  AAAAAAAA…    BBBBBBBB…    AAAAAAAA…    …    ",
            "3  │  A                                           ",
            "   │                                              ",
            "   │                                              ",
            "───┴──────────────────────────────────────────────",
            "stdin [Row 1/3, Col 1/10]                         ",
        ];
        let actual_buffer = terminal.backend().buffer().clone();
        let lines = to_lines(&actual_buffer);
        assert_eq!(lines, expected);

        step_and_draw(&mut app, &mut terminal, Control::ScrollRight);
        let expected = vec![
            "──────────────────────────────────────────────────",
            "      2            3            4            5    ",
            "───┬──────────────────────────────────────────────",
            "1  │  BBBBBBBB…    AAAAAAAA…    BBBBBBBB…    …    ",
            "2  │  BBBBBBBB…    AAAAAAAA…    BBBBBBBB…    …    ",
            "3  │                                              ",
            "   │                                              ",
            "   │                                              ",
            "───┴──────────────────────────────────────────────",
            "stdin [Row 1/3, Col 2/10]                         ",
        ];
        let actual_buffer = terminal.backend().buffer().clone();
        let lines = to_lines(&actual_buffer);
        assert_eq!(lines, expected);
    }

    #[test]
    fn test_irregular_filter_columns_then_rows() {
        let mut app = AppBuilder::new("tests/data/irregular_more_fields.csv")
            .delimiter(Delimiter::Comma)
            .build()
            .unwrap();
        till_app_ready(&app);

        let backend = TestBackend::new(50, 10);
        let mut terminal = Terminal::new(backend).unwrap();

        step_and_draw(&mut app, &mut terminal, Control::Nothing);
        step_and_draw(
            &mut app,
            &mut terminal,
            Control::FilterColumns("COL1".into()),
        );
        till_app_ready(&app);
        step_and_draw(&mut app, &mut terminal, Control::Filter("x1".into()));
        till_app_ready(&app);
        // Toggle to cell selection
        step_and_draw(&mut app, &mut terminal, Control::ToggleSelectionType);
        step_and_draw(&mut app, &mut terminal, Control::ToggleSelectionType);

        let expected = vec![
            "──────────────────────────────────────────────────",
            "      COL1                                        ",
            "───┬──────────┬───────────────────────────────────",
            "1  │  x1      │                                   ",
            "   │          │                                   ",
            "   │          │                                   ",
            "   │          │                                   ",
            "   │          │                                   ",
            "───┴──────────┴───────────────────────────────────",
            "stdin [Row 1/2, Col 1/1] [Filter \"x1\": 1/1] [Filte",
        ];
        let actual_buffer = terminal.backend().buffer().clone();
        let lines = to_lines(&actual_buffer);
        assert_eq!(lines, expected);

        let selection = app.get_selection();
        assert_eq!(selection, Some("x1".to_string()));
    }

    #[test]
    fn test_freeze_columns() {
        let mut app = AppBuilder::new("tests/data/cities.csv").build().unwrap();
        till_app_ready(&app);

        let backend = TestBackend::new(50, 10);
        let mut terminal = Terminal::new(backend).unwrap();

        step_and_draw(&mut app, &mut terminal, Control::Nothing);
        step_and_draw(&mut app, &mut terminal, Control::FreezeColumns(2));
        step_and_draw(&mut app, &mut terminal, Control::ScrollRight);
        step_and_draw(&mut app, &mut terminal, Control::ScrollRight);
        step_and_draw(&mut app, &mut terminal, Control::ScrollRight);
        step_and_draw(&mut app, &mut terminal, Control::ScrollRight);
        step_and_draw(&mut app, &mut terminal, Control::ScrollRight);
        let actual_buffer = terminal.backend().buffer().clone();
        let lines = to_lines(&actual_buffer);
        let expected = vec![
            "──────────────────────────────────────────────────",
            "      LatD    LatM    EW    City         State    ",
            "───┬────────────────╥─────────────────────────────",
            "1  │  41      5     ║ W     Youngsto…    OH       ",
            "2  │  42      52    ║       Yankton      SD       ",
            "3  │  46      35    ║ W     Yakima       WA       ",
            "4  │  42      16    ║ W     Worcester    MA       ",
            "5  │  43      37    ║ W     Wisconsi…    WI       ",
            "───┴────────────────╨─────────────────────────────",
            "stdin [Row 1/128, Col 6/10]                       ",
        ];
        assert_eq!(lines, expected);
    }

    #[test]
    fn test_prompt() {
        let mut app = AppBuilder::new("tests/data/cities.csv")
            .echo_column("City")
            .columns_regex(Some("NS|City|State".to_string()))
            .prompt("\x1b[32m\x1b[1mSelect your city!\x1b[0m")
            .build()
            .unwrap();
        till_app_ready(&app);

        let backend = TestBackend::new(50, 10);
        let mut terminal = Terminal::new(backend).unwrap();

        step_and_draw(&mut app, &mut terminal, Control::Nothing);
        let actual_buffer = terminal.backend().buffer().clone();
        let lines = to_lines(&actual_buffer);
        let expected = vec![
            "──────────────────────────────────────────────────",
            "      NS    City               State              ",
            "───┬────────────────────────────────────┬─────────",
            "1  │  N     Youngstown         OH       │         ",
            "2  │  N     Yankton            SD       │         ",
            "3  │  N     Yakima             WA       │         ",
            "4  │  N     Worcester          MA       │         ",
            "5  │  N     Wisconsin Dells    WI       │         ",
            "───┴────────────────────────────────────┴─────────",
            "Select your city! [Row 1/128, Col 1/3] [Filter \"NS",
        ];
        assert_eq!(lines, expected);
    }

    #[test]
    fn test_degenerate_height_0() {
        let mut app = AppBuilder::new("tests/data/cities.csv")
            .prompt("City, city everywhere!")
            .build()
            .unwrap();
        till_app_ready(&app);

        let backend = TestBackend::new(50, 0);
        let mut terminal = Terminal::new(backend).unwrap();

        step_and_draw(&mut app, &mut terminal, Control::Nothing);
        let actual_buffer = terminal.backend().buffer().clone();
        let lines = to_lines(&actual_buffer);
        let expected = vec![""];
        assert_eq!(lines, expected);
    }

    #[test]
    fn test_degenerate_height_1() {
        let mut app = AppBuilder::new("tests/data/cities.csv")
            .prompt("City, city everywhere!")
            .build()
            .unwrap();
        till_app_ready(&app);

        let backend = TestBackend::new(50, 1);
        let mut terminal = Terminal::new(backend).unwrap();

        step_and_draw(&mut app, &mut terminal, Control::Nothing);
        let actual_buffer = terminal.backend().buffer().clone();
        let lines = to_lines(&actual_buffer);
        let expected = vec!["──────────────────────────────────────────────────"];
        assert_eq!(lines, expected);
    }

    #[test]
    fn test_degenerate_height_2() {
        let mut app = AppBuilder::new("tests/data/cities.csv")
            .prompt("City, city everywhere!")
            .build()
            .unwrap();
        till_app_ready(&app);

        let backend = TestBackend::new(50, 2);
        let mut terminal = Terminal::new(backend).unwrap();

        step_and_draw(&mut app, &mut terminal, Control::Nothing);
        let actual_buffer = terminal.backend().buffer().clone();
        let lines = to_lines(&actual_buffer);
        let expected = vec![
            "──────────────────────────────────────────────────",
            "City, city everywhere! [Row -/128, Col 1/10]L…    ",
        ];
        assert_eq!(lines, expected);
    }

    #[test]
    fn test_degenerate_width_0() {
        let mut app = AppBuilder::new("tests/data/cities.csv")
            .prompt("City, city everywhere!")
            .build()
            .unwrap();
        till_app_ready(&app);

        let backend = TestBackend::new(0, 10);
        let mut terminal = Terminal::new(backend).unwrap();

        step_and_draw(&mut app, &mut terminal, Control::Nothing);
        let actual_buffer = terminal.backend().buffer().clone();
        let lines = to_lines(&actual_buffer);
        let expected = vec!["", "", "", "", "", "", "", "", "", ""];
        assert_eq!(lines, expected);
    }

    #[test]
    fn test_degenerate_width_1() {
        let mut app = AppBuilder::new("tests/data/cities.csv")
            .prompt("City, city everywhere!")
            .build()
            .unwrap();
        till_app_ready(&app);

        let backend = TestBackend::new(1, 10);
        let mut terminal = Terminal::new(backend).unwrap();

        step_and_draw(&mut app, &mut terminal, Control::Nothing);
        let actual_buffer = terminal.backend().buffer().clone();
        let lines = to_lines(&actual_buffer);
        let expected = vec!["─", " ", "─", "1", "2", "3", "4", "5", " ", "C"];
        assert_eq!(lines, expected);
    }

    #[test]
    fn test_copy_selection_crlf() {
        // Skip test in CI environments where clipboard is not available
        if std::env::var("CI").is_ok() {
            return;
        }

        let mut app = AppBuilder::new("tests/data/cell_with_crlf.csv")
            .build()
            .unwrap();
        till_app_ready(&app);

        let backend = TestBackend::new(50, 10);
        let mut terminal = Terminal::new(backend).unwrap();

        step_and_draw(&mut app, &mut terminal, Control::Nothing);
        step_and_draw(&mut app, &mut terminal, Control::ToggleSelectionType);
        step_and_draw(&mut app, &mut terminal, Control::ToggleSelectionType);
        step_and_draw(&mut app, &mut terminal, Control::CopySelection);
        let actual_buffer = terminal.backend().buffer().clone();
        let lines = to_lines(&actual_buffer);
        let expected = vec![
            "──────────────────────────────────────────────────",
            "      column_name                                 ",
            "───┬─────────────────┬────────────────────────────",
            "1  │  value 1…       │                            ",
            "2  │  value 2…       │                            ",
            "3  │  value 3…       │                            ",
            "   │                 │                            ",
            "   │                 │                            ",
            "───┴─────────────────┴────────────────────────────",
            "Copied value 1 to clipboard                       ",
        ];
        assert_eq!(lines, expected);
    }

    #[test]
    fn test_scroll_to_last_rows() {
        let mut app = AppBuilder::new("tests/data/cities.csv").build().unwrap();
        till_app_ready(&app);

        let backend = TestBackend::new(50, 20);
        let mut terminal = Terminal::new(backend).unwrap();

        // Need a second Nothing to get states like num_rendered rows right, probably something to
        // fix later.
        step_and_draw(&mut app, &mut terminal, Control::Nothing);
        step_and_draw(&mut app, &mut terminal, Control::Nothing);

        // cities.csv has 128 rows, scroll to row 125 to test scrolling near the end
        step_and_draw(&mut app, &mut terminal, Control::ScrollTo(125));

        let actual_buffer = terminal.backend().buffer().clone();
        let lines = to_lines(&actual_buffer);
        let expected = vec![
            "──────────────────────────────────────────────────",
            "        LatD    LatM    LatS    NS    LonD    …   ",
            "─────┬────────────────────────────────────────────",
            "114  │  35      56      23      N     77      …   ",
            "115  │  41      35      24      N     109     …   ",
            "116  │  42      16      12      N     89      …   ",
            "117  │  43      9       35      N     77      …   ",
            "118  │  44      1       12      N     92      …   ",
            "119  │  37      16      12      N     79      …   ",
            "120  │  37      32      24      N     77      …   ",
            "121  │  39      49      48      N     84      …   ",
            "122  │  38      46      12      N     112     …   ",
            "123  │  45      38      23      N     89      …   ",
            "124  │  39      31      12      N     119     …   ",
            "125  │  50      25      11      N     104     …   ",
            "126  │  40      10      48      N     122     …   ",
            "127  │  40      19      48      N     75      …   ",
            "128  │  41      9       35      N     81      …   ",
            "─────┴────────────────────────────────────────────",
            "stdin [Row 125/128, Col 1/10]                     ",
        ];

        assert_eq!(lines, expected);
    }

    #[test]
    fn test_scroll_to_column_selection_mode() {
        let mut app = AppBuilder::new("tests/data/cities.csv").build().unwrap();
        till_app_ready(&app);

        let backend = TestBackend::new(50, 10);
        let mut terminal = Terminal::new(backend).unwrap();

        step_and_draw(&mut app, &mut terminal, Control::Nothing);
        step_and_draw(&mut app, &mut terminal, Control::ToggleSelectionType);
        step_and_draw(&mut app, &mut terminal, Control::ScrollTo(10));

        let actual_buffer = terminal.backend().buffer().clone();
        let lines = to_lines(&actual_buffer);
        let expected = vec![
            "──────────────────────────────────────────────────",
            "       LatD    LatM    LatS    NS    LonD    …    ",
            "────┬─────────────────────────────────────────────",
            "10  │  39      45      0       N     75      …    ",
            "11  │  48      9       0       N     103     …    ",
            "12  │  41      15      0       N     77      0    ",
            "13  │  37      40      48      N     82      …    ",
            "14  │  33      54      0       N     98      …    ",
            "────┴─────────────────────────────────────────────",
            "stdin [Row 10/128, Col 1/10]                      ",
        ];

        assert_eq!(lines, expected);

        // Check remains in column selection mode
        assert_eq!(app.rows_view.selection.row.index().is_some(), false);
        assert_eq!(app.rows_view.selection.column.index().is_some(), true);
    }

    #[test]
    fn test_filter_reset_preserve_selected_row() {
        let mut app = AppBuilder::new("tests/data/cities.csv")
            .filter_regex(Some("OH".to_string()))
            .build()
            .unwrap();
        till_app_ready(&app);

        let backend = TestBackend::new(80, 10);
        let mut terminal = Terminal::new(backend).unwrap();

        // Filter and select row 62 (3rd row in filtered view)
        step_and_draw(&mut app, &mut terminal, Control::Nothing);
        step_and_draw(&mut app, &mut terminal, Control::ScrollDown);
        step_and_draw(&mut app, &mut terminal, Control::ScrollDown);

        let expected = vec![
            "────────────────────────────────────────────────────────────────────────────────",
            "       LatD    LatM    LatS    NS    LonD    LonM    LonS    EW    City         ",
            "────┬───────────────────────────────────────────────────────────────────────────",
            "1   │  41      5       59      N     80      39      0       W     Youngsto…    ",
            "50  │  41      39      0       N     83      32      24      W     Toledo       ",
            "62  │  40      21      36      N     80      37      12      W     Steubenv…    ",
            "65  │  39      55      11      N     83      48      35      W     Springfi…    ",
            "92  │  41      27      0       N     82      42      35      W     Sandusky     ",
            "────┴───────────────────────────────────────────────────────────────────────────",
            "stdin [Row 62/128, Col 1/10] [Filter \"OH\": 3/6]                                 ",
        ];
        let actual_buffer = terminal.backend().buffer().clone();
        let lines = to_lines(&actual_buffer);
        assert_eq!(lines, expected);

        // Reset filter, row 62 should still be selected
        step_and_draw(&mut app, &mut terminal, Control::BufferReset);
        let expected = vec![
            "────────────────────────────────────────────────────────────────────────────────",
            "       LatD    LatM    LatS    NS    LonD    LonM    LonS    EW    City         ",
            "────┬───────────────────────────────────────────────────────────────────────────",
            "62  │  40      21      36      N     80      37      12      W     Steubenv…    ",
            "63  │  40      37      11      N     103     13      12      W     Sterling     ",
            "64  │  38      9       0       N     79      4       11      W     Staunton     ",
            "65  │  39      55      11      N     83      48      35      W     Springfi…    ",
            "66  │  37      13      12      N     93      17      24      W     Springfi…    ",
            "────┴───────────────────────────────────────────────────────────────────────────",
            "stdin [Row 62/128, Col 1/10]                                                    ",
        ];
        let actual_buffer = terminal.backend().buffer().clone();
        let lines = to_lines(&actual_buffer);
        assert_eq!(lines, expected);
    }

    #[test]
    fn test_filter_reset_preserve_rows_from() {
        let mut app = AppBuilder::new("tests/data/cities.csv")
            .filter_regex(Some("CA".to_string()))
            .build()
            .unwrap();
        till_app_ready(&app);

        let backend = TestBackend::new(80, 10);
        let mut terminal = Terminal::new(backend).unwrap();

        // Filter and toggle to column selection
        step_and_draw(&mut app, &mut terminal, Control::Nothing);
        step_and_draw(&mut app, &mut terminal, Control::ToggleSelectionType);

        let expected = vec![
            "────────────────────────────────────────────────────────────────────────────────",
            "       LatD    LatM    LatS    NS    LonD    LonM    LonS    EW    City         ",
            "────┬───────────────────────────────────────────────────────────────────────────",
            "19  │  41      25      11      N     122     23      23      W     Weed         ",
            "60  │  37      57      35      N     121     17      24      W     Stockton     ",
            "86  │  38      26      23      N     122     43      12      W     Santa Ro…    ",
            "88  │  34      25      11      N     119     41      59      W     Santa Ba…    ",
            "89  │  33      45      35      N     117     52      12      W     Santa Ana    ",
            "────┴───────────────────────────────────────────────────────────────────────────",
            "stdin [Row 19/128, Col 1/10] [Filter \"CA\": -/12]                                ",
        ];
        let actual_buffer = terminal.backend().buffer().clone();
        let lines = to_lines(&actual_buffer);
        assert_eq!(lines, expected);

        // Reset filter, rows should start with 19
        step_and_draw(&mut app, &mut terminal, Control::BufferReset);
        let expected = vec![
            "────────────────────────────────────────────────────────────────────────────────",
            "       LatD    LatM    LatS    NS    LonD    LonM    LonS    EW    City         ",
            "────┬───────────────────────────────────────────────────────────────────────────",
            "19  │  41      25      11      N     122     23      23      W     Weed         ",
            "20  │  31      13      11      N     82      20      59      W     Waycross     ",
            "21  │  44      57      35      N     89      38      23      W     Wausau       ",
            "22  │  42      21      36      N     87      49      48      W     Waukegan     ",
            "23  │  44      54      0       N     97      6       36      W     Watertown    ",
            "────┴───────────────────────────────────────────────────────────────────────────",
            "stdin [Row 19/128, Col 1/10]                                                    ",
        ];
        let actual_buffer = terminal.backend().buffer().clone();
        let lines = to_lines(&actual_buffer);
        assert_eq!(lines, expected);
    }

    #[test]
    fn test_filter_reset_preserve_rows_from_with_sorter() {
        let mut app = AppBuilder::new("tests/data/cities.csv")
            .filter_regex(Some("CA".to_string()))
            .build()
            .unwrap();
        till_app_ready(&app);

        let backend = TestBackend::new(80, 10);
        let mut terminal = Terminal::new(backend).unwrap();

        // Filter and toggle to column selection and sort
        step_and_draw(&mut app, &mut terminal, Control::Nothing);
        step_and_draw(&mut app, &mut terminal, Control::ToggleSelectionType);
        step_and_draw(&mut app, &mut terminal, Control::ToggleSort);
        till_app_ready(&app); // Wait for sorter
        step_and_draw(&mut app, &mut terminal, Control::Nothing);
        till_app_ready(&app); // Wait for the re-created finder with sorter
        step_and_draw(&mut app, &mut terminal, Control::Nothing);

        let expected = vec![
            "────────────────────────────────────────────────────────────────────────────────",
            "       LatD [▴]      LatM    LatS    NS    LonD    LonM    LonS    EW    Ci…    ",
            "────┬───────────────────────────────────────────────────────────────────────────",
            "93  │  32            42      35      N     117     9       0       W     Sa…    ",
            "89  │  33            45      35      N     117     52      12      W     Sa…    ",
            "88  │  34            25      11      N     119     41      59      W     Sa…    ",
            "94  │  34            6       36      N     117     18      35      W     Sa…    ",
            "99  │  36            40      11      N     121     39      0       W     Sa…    ",
            "────┴───────────────────────────────────────────────────────────────────────────",
            "stdin [Row 93/128, Col 1/10] [Filter \"CA\": -/12]                                ",
        ];
        let actual_buffer = terminal.backend().buffer().clone();
        let lines = to_lines(&actual_buffer);
        assert_eq!(lines, expected);

        // Reset filter, rows should start with 93
        step_and_draw(&mut app, &mut terminal, Control::BufferReset);
        let expected = vec![
            "────────────────────────────────────────────────────────────────────────────────",
            "       LatD [▴]      LatM    LatS    NS    LonD    LonM    LonS    EW    Ci…    ",
            "────┬───────────────────────────────────────────────────────────────────────────",
            "93  │  32            42      35      N     117     9       0       W     Sa…    ",
            "41  │  33            12      35      N     87      34      11      W     Tu…    ",
            "58  │  33            55      11      N     80      20      59      W     Su…    ",
            "74  │  33            38      23      N     96      36      36      W     Sh…    ",
            "51  │  33            25      48      N     94      3       0       W     Te…    ",
            "────┴───────────────────────────────────────────────────────────────────────────",
            "stdin [Row 93/128, Col 1/10]                                                    ",
        ];
        let actual_buffer = terminal.backend().buffer().clone();
        let lines = to_lines(&actual_buffer);
        assert_eq!(lines, expected);
    }

    #[test]
    fn test_cli_find_option_empty_regex() {
        let mut app = AppBuilder::new("tests/data/cities.csv")
            .find_regex(Some("".to_string()))
            .build()
            .unwrap();
        till_app_ready(&app);

        let backend = TestBackend::new(80, 10);
        let mut terminal = Terminal::new(backend).unwrap();
        step_and_draw(&mut app, &mut terminal, Control::Nothing);

        let expected = vec![
            "────────────────────────────────────────────────────────────────────────────────",
            "      LatD    LatM    LatS    NS    LonD    LonM    LonS    EW    City          ",
            "───┬────────────────────────────────────────────────────────────────────────────",
            "1  │  41      5       59      N     80      39      0       W     Youngstown    ",
            "2  │  42      52      48      N     97      23      23            Yankton       ",
            "3  │  46      35      59      N     120     30      36      W     Yakima        ",
            "4  │  42      16      12      N     71      48      0       W     Worcester     ",
            "5  │  43      37      48      N     89      46      11      W     Wisconsin…    ",
            "───┴────────────────────────────────────────────────────────────────────────────",
            "stdin [Row 1/128, Col 1/10]                                                     ",
        ];
        let actual_buffer = terminal.backend().buffer().clone();
        let lines = to_lines(&actual_buffer);
        assert_eq!(lines, expected);
    }
}
```

## File: `src/columns_filter.rs`
```rust
use regex::Regex;

#[derive(Debug)]
pub struct ColumnsFilter {
    pattern: Regex,
    indices: Vec<usize>,
    filtered_headers: Vec<String>,
    filtered_flags: Vec<bool>,
    num_columns_before_filter: usize,
    disabled_because_no_match: bool,
}

impl ColumnsFilter {
    pub fn new(pattern: Regex, headers: &[String]) -> Self {
        let mut indices = vec![];
        let mut filtered_headers: Vec<String> = vec![];
        let mut filtered_flags: Vec<bool> = vec![];
        for (i, header) in headers.iter().enumerate() {
            if pattern.is_match(header) {
                indices.push(i);
                filtered_headers.push(header.clone());
                filtered_flags.push(true);
            } else {
                filtered_flags.push(false);
            }
        }
        let disabled_because_no_match;
        if indices.is_empty() {
            indices = (0..headers.len()).collect();
            filtered_headers = headers.into();
            disabled_because_no_match = true;
        } else {
            disabled_because_no_match = false;
        }
        Self {
            pattern,
            indices,
            filtered_headers,
            filtered_flags,
            num_columns_before_filter: headers.len(),
            disabled_because_no_match,
        }
    }

    pub fn filtered_headers(&self) -> &Vec<String> {
        &self.filtered_headers
    }

    pub fn indices(&self) -> &Vec<usize> {
        &self.indices
    }

    pub fn pattern(&self) -> Regex {
        self.pattern.to_owned()
    }

    pub fn num_filtered(&self) -> usize {
        self.indices.len()
    }

    pub fn num_original(&self) -> usize {
        self.num_columns_before_filter
    }

    pub fn disabled_because_no_match(&self) -> bool {
        self.disabled_because_no_match
    }

    pub fn is_column_filtered(&self, index: usize) -> bool {
        self.filtered_flags.get(index).cloned().unwrap_or(false)
    }
}
```

## File: `src/common.rs`
```rust
use std::fmt;

#[derive(Clone, PartialEq, Eq, Hash, Copy, Debug)]
pub enum InputMode {
    Default,
    GotoLine,
    Find,
    Filter,
    FilterColumns,
    FreezeColumns,
    Option,
    Help,
}

impl fmt::Display for InputMode {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "{:?}", self)
    }
}
```

## File: `src/csv.rs`
```rust
extern crate csv;

use csv::{Position, Reader, ReaderBuilder};
use std::cmp::max;
use std::fs::File;
use std::sync::atomic::AtomicUsize;
use std::sync::{Arc, Mutex};
use std::thread::{self, JoinHandle};
use std::time;
use std::{
    io::{self, Read},
    sync::atomic::{AtomicBool, Ordering},
    time::Duration,
};

use csv::{ByteRecord, StringRecord};
use csv_core::Reader as CoreReader;
use csv_core::ReaderBuilder as CoreReaderBuilder;

use crate::errors::CsvlensResult;

fn string_record_to_vec(record: &csv::StringRecord) -> Vec<String> {
    let mut string_vec = Vec::with_capacity(record.len());
    for field in record.iter() {
        string_vec.push(String::from(field));
    }
    string_vec
}

pub struct CsvBaseConfig {
    delimiter: u8,
    no_headers: bool,
}

impl CsvBaseConfig {
    pub fn new(delimiter: u8, no_headers: bool) -> CsvBaseConfig {
        CsvBaseConfig {
            delimiter,
            no_headers,
        }
    }
}

pub struct CsvConfig {
    path: String,
    stream_active: Option<Arc<AtomicBool>>,
    base: CsvBaseConfig,
}

impl CsvConfig {
    pub fn new(
        path: &str,
        stream_active: Option<Arc<AtomicBool>>,
        base: CsvBaseConfig,
    ) -> CsvConfig {
        CsvConfig {
            path: path.to_string(),
            stream_active,
            base,
        }
    }

    pub fn new_reader(&self) -> CsvlensResult<Reader<File>> {
        let reader = ReaderBuilder::new()
            .flexible(true)
            .delimiter(self.base.delimiter)
            .has_headers(!self.base.no_headers)
            .from_path(self.path.as_str())?;
        Ok(reader)
    }

    pub fn new_core_reader(&self) -> CoreReader {
        CoreReaderBuilder::new()
            .delimiter(self.base.delimiter)
            .build()
    }

    pub fn filename(&self) -> &str {
        self.path.as_str()
    }

    pub fn delimiter(&self) -> u8 {
        self.base.delimiter
    }

    pub fn no_headers(&self) -> bool {
        self.base.no_headers
    }

    pub fn has_headers(&self) -> bool {
        !self.base.no_headers
    }

    /// Convert position to a 0-based record index
    pub fn position_to_record_index(&self, position: u64) -> u64 {
        if self.base.no_headers {
            position
        } else {
            position - 1
        }
    }

    /// Convert position to a 1-based record number
    pub fn position_to_record_num(&self, position: u64) -> u64 {
        if self.base.no_headers {
            position + 1
        } else {
            position
        }
    }

    /// Whether the file should be read in streaming mode, and whether the stream is still active
    pub fn is_streaming(&self) -> bool {
        self.stream_active
            .as_ref()
            .map(|x| x.load(Ordering::Relaxed))
            .unwrap_or(false)
    }
}

pub struct CsvLensReader {
    config: Arc<CsvConfig>,
    reader: Reader<File>,
    pub headers: Vec<String>,
    internal: Arc<Mutex<ReaderInternalState>>,
}

#[derive(Debug, PartialEq, Eq, Clone)]
pub struct Row {
    pub record_num: usize,
    pub fields: Vec<String>,
}

impl Row {
    pub fn subset(&self, indices: &[usize]) -> Row {
        let mut subfields = vec![];
        for i in indices {
            if let Some(field) = self.fields.get(*i) {
                subfields.push(field.clone());
            }
        }
        Row {
            record_num: self.record_num,
            fields: subfields,
        }
    }

    fn empty() -> Row {
        Row {
            record_num: 0,
            fields: vec![],
        }
    }
}

#[derive(Debug)]
struct GetRowIndex {
    // 0-based index of the record in the csv file
    record_index: u64,

    // Position where the record should be in the resulting list of rows
    order_index: usize,
}

impl Drop for CsvLensReader {
    fn drop(&mut self) {
        self.terminate();
    }
}

impl CsvLensReader {
    pub fn new(config: Arc<CsvConfig>) -> CsvlensResult<Self> {
        let mut reader = config.new_reader()?;

        let headers_record = if config.no_headers() {
            let mut dummy_headers = csv::StringRecord::new();
            for (i, _) in reader.headers()?.into_iter().enumerate() {
                dummy_headers.push_field((i + 1).to_string().as_str());
            }
            dummy_headers
        } else {
            reader.headers()?.clone()
        };
        let headers = string_record_to_vec(&headers_record);

        let (m_internal, _handle) = ReaderInternalState::init_internal(config.clone());

        // _handle.join().unwrap();

        let reader = Self {
            config: config.clone(),
            reader,
            headers,
            internal: m_internal,
        };
        Ok(reader)
    }

    pub fn get_rows(
        &mut self,
        rows_from: u64,
        num_rows: u64,
    ) -> CsvlensResult<(Vec<Row>, GetRowsStats)> {
        let indices: Vec<u64> = (rows_from..rows_from + num_rows).collect();
        self.get_rows_impl(&indices)
    }

    pub fn get_rows_for_indices(
        &mut self,
        indices: &[u64],
    ) -> CsvlensResult<(Vec<Row>, GetRowsStats)> {
        self.get_rows_impl(indices)
    }

    fn get_rows_impl(&mut self, indices: &[u64]) -> CsvlensResult<(Vec<Row>, GetRowsStats)> {
        let mut get_row_indices = indices
            .iter()
            .enumerate()
            .map(|x| GetRowIndex {
                record_index: *x.1,
                order_index: x.0,
            })
            .collect::<Vec<_>>();
        get_row_indices.sort_by(|a, b| a.record_index.cmp(&b.record_index));
        self._get_rows_impl_sorted(&get_row_indices)
    }

    fn _get_rows_impl_sorted(
        &mut self,
        indices: &[GetRowIndex],
    ) -> CsvlensResult<(Vec<Row>, GetRowsStats)> {
        // stats for debugging and testing
        let mut stats = GetRowsStats::new();

        let pos = Position::new();
        self.reader.seek(pos)?;

        let tic = time::Instant::now();
        let pos_table = self.get_pos_table();
        stats.pos_table_elapsed = Some(tic.elapsed());
        stats.pos_table_entry = pos_table.len();

        let mut pos_iter = pos_table.iter();
        let mut indices_iter = indices.iter();

        let mut res = vec![Row::empty(); indices.len()];
        let mut res_max_index: Option<usize> = None;

        let mut next_pos = pos_iter.next();
        let mut next_wanted = indices_iter.next();

        let num_fields = self.headers.len();

        let mut should_stop = false;
        loop {
            if next_wanted.is_none() {
                break;
            }
            // seek as close to the next wanted record index as possible
            let index = next_wanted.unwrap();
            let mut seek_pos: Option<Position> = None;
            while let Some(pos) = next_pos {
                if self.config.position_to_record_index(pos.record()) <= index.record_index {
                    seek_pos.replace(pos.clone());
                } else {
                    break;
                }
                next_pos = pos_iter.next();
            }
            if let Some(pos) = seek_pos {
                self.reader.seek(pos.clone())?;
                stats.log_seek();
            }

            // note that records() excludes header by default, but here the first entry is header
            // because of the seek() above.
            let mut records = self.reader.records();

            // parse records and collect those that are wanted
            loop {
                // exit early if all found. This should be common in case of consecutive indices
                if next_wanted.is_none() {
                    break;
                }
                let wanted = next_wanted.unwrap();
                let record_position = records.reader().position().record();
                if let Some(r) = records.next() {
                    stats.log_parsed_record();
                    // no effective pre-seeking happened, this is still the header
                    if self.config.has_headers() && record_position == 0 {
                        continue;
                    }
                    if self.config.position_to_record_index(record_position) == wanted.record_index
                    {
                        let string_record = r?;
                        let mut fields = Vec::with_capacity(num_fields);
                        for field in string_record.iter() {
                            fields.push(String::from(field));
                        }
                        let row = Row {
                            record_num: self.config.position_to_record_num(record_position)
                                as usize,
                            fields,
                        };
                        res[wanted.order_index] = row;
                        res_max_index.replace(
                            res_max_index
                                .map_or(wanted.order_index, |x| max(x, wanted.order_index)),
                        );
                        next_wanted = indices_iter.next();
                    }
                    // stop parsing if done scanning whole block between marked positions
                    if let Some(pos) = next_pos
                        && record_position >= pos.record()
                    {
                        break;
                    }
                } else {
                    // no more records
                    should_stop = true;
                    break;
                }
            }

            if next_pos.is_none() {
                // If here, the last block had been scanned, and we should be
                // done. If next_wanted is not None, that means an out of bound
                // index was provided - that could happen for small input - and
                // we should ignore it and stop here regardless
                break;
            }

            if should_stop {
                // no more records, no point continuing even if there are more marked positions.
                // This could be caused by out of bound indices or changed file content.
                break;
            }
        }

        // In case requested indices are beyond the last record, truncate those indices.
        res.truncate(res_max_index.map_or(0, |x| x + 1));

        Ok((res, stats))
    }

    pub fn get_approx_line_numbers(&self) -> usize {
        self.internal
            .lock()
            .unwrap()
            .current_line_number
            .load(Ordering::Relaxed)
    }

    pub fn get_total_line_numbers(&self) -> Option<usize> {
        self.internal.lock().unwrap().total_line_number
    }

    pub fn get_pos_table(&self) -> Vec<Position> {
        self.internal.lock().unwrap().pos_table.clone()
    }

    fn terminate(&self) {
        let mut m_guard = self.internal.lock().unwrap();
        m_guard.terminate();
    }

    #[cfg(test)]
    fn wait_till_start_scanning(&self) {
        loop {
            if self.internal.lock().unwrap().started_scanning {
                break;
            }
            thread::sleep(time::Duration::from_millis(100));
        }
    }

    #[cfg(test)]
    pub fn wait_internal(&self) {
        loop {
            if self.internal.lock().unwrap().done {
                break;
            }
            thread::sleep(time::Duration::from_millis(100));
        }
    }
}

#[derive(Debug, Clone, PartialEq)]
pub struct GetRowsStats {
    pub num_seek: u64,
    pub num_parsed_record: u64,
    pub pos_table_elapsed: Option<time::Duration>,
    pub pos_table_entry: usize,
}

impl GetRowsStats {
    fn new() -> GetRowsStats {
        GetRowsStats {
            num_seek: 0,
            num_parsed_record: 0,
            pos_table_elapsed: None,
            pos_table_entry: 0,
        }
    }

    fn log_seek(&mut self) {
        self.num_seek += 1;
    }

    fn log_parsed_record(&mut self) {
        self.num_parsed_record += 1
    }
}

pub struct StreamingCsvReader {
    file: File,
    core: CoreReader,
    in_buf: Vec<u8>,
    buf_start: usize,
    buf_end: usize,
    fields: Vec<u8>,
    ends: Vec<usize>,
    cur_pos: Position,
    first_record_returned: bool,
    config: Arc<CsvConfig>,
    sleep: Duration,
}

impl StreamingCsvReader {
    pub fn new(csv_config: Arc<CsvConfig>) -> io::Result<Self> {
        let file = File::open(csv_config.path.as_str())?;
        let core = csv_config.new_core_reader();
        // TODO: these initial capacities ok?
        Ok(Self {
            file,
            core,
            in_buf: vec![0u8; 64 * 1024],
            buf_start: 0,
            buf_end: 0,
            fields: vec![0u8; 8 * 1024],
            ends: vec![0; 256],
            cur_pos: Position::new(),
            first_record_returned: false,
            config: csv_config,
            sleep: Duration::from_millis(200),
        })
    }

    fn read_buffer(&mut self) -> io::Result<()> {
        self.buf_start = 0;
        let n = self.file.read(&mut self.in_buf)?;
        self.buf_end = n;
        Ok(())
    }

    fn build_byte_record(&self, fields: &[u8], ends: &[usize], pos: Position) -> ByteRecord {
        let mut rec = ByteRecord::new();
        let mut start = 0usize;
        for &end in ends {
            let field_bytes = &fields[start..end];
            rec.push_field(field_bytes);
            start = end;
        }
        rec.set_position(Some(pos.clone()));
        rec
    }

    #[inline(always)]
    fn read_string_record(&mut self) -> Option<CsvlensResult<StringRecord>> {
        use csv_core::ReadRecordResult::*;

        let (mut outlen, mut endlen) = (0, 0);
        let record_pos = self.cur_pos.clone();
        loop {
            // If no input left in buffer, try to read more
            if self.buf_start == self.buf_end {
                if let Err(e) = self.read_buffer() {
                    return Some(Err(e.into()));
                }

                if self.buf_end == 0 {
                    if !self.config.is_streaming() {
                        break;
                    }
                    // Temporary EOF: no new bytes right now. In streaming mode we just wait and
                    // try again.
                    thread::sleep(self.sleep);
                    continue;
                }
            }

            // Similar implementation as csv crate's read_byte_record_impl but blocks on EOF to
            // allow tailing
            let (res, nin, nout, nend) = {
                let input = &self.in_buf[self.buf_start..self.buf_end];
                self.core
                    .read_record(input, &mut self.fields[outlen..], &mut self.ends[endlen..])
            };
            let byte = self.cur_pos.byte();
            self.cur_pos
                .set_byte(byte + nin as u64)
                .set_line(self.core.line());
            self.buf_start += nin;
            outlen += nout;
            endlen += nend;
            match res {
                InputEmpty => continue,
                OutputFull => {
                    let new_len = self.fields.len() * 2;
                    self.fields.resize(new_len, 0);
                    continue;
                }
                OutputEndsFull => {
                    let new_len = self.ends.len() * 2;
                    self.ends.resize(new_len, 0);
                    continue;
                }
                Record => {
                    let byte_rec = self.build_byte_record(
                        &self.fields[..outlen],
                        &self.ends[..endlen],
                        record_pos,
                    );
                    self.cur_pos
                        .set_record(self.cur_pos.record().checked_add(1).unwrap());
                    match StringRecord::from_byte_record(byte_rec) {
                        Ok(srec) => return Some(Ok(srec)),
                        Err(e) => return Some(Err(e.into())),
                    }
                }
                End => {}
            }
        }

        // Handle any remaining partial record at true EOF
        if endlen > 0 {
            let byte_rec =
                self.build_byte_record(&self.fields[..outlen], &self.ends[..endlen], record_pos);
            match StringRecord::from_byte_record(byte_rec) {
                Ok(srec) => return Some(Ok(srec)),
                Err(e) => return Some(Err(e.into())),
            }
        }

        None
    }

    fn reader_position(&self) -> &Position {
        &self.cur_pos
    }
}

impl Iterator for StreamingCsvReader {
    type Item = CsvlensResult<StringRecord>;

    #[inline(always)]
    fn next(&mut self) -> Option<Self::Item> {
        // For the first record, if there are headers, skip it
        let mut record = self.read_string_record();
        if self.config.has_headers() && !self.first_record_returned {
            record = self.read_string_record();
        }
        self.first_record_returned = true;
        record
    }
}

pub enum CsvlensRecordIterator {
    Streaming(Box<StreamingCsvReader>),
    Standard(csv::StringRecordsIntoIter<File>),
}

impl CsvlensRecordIterator {
    pub fn new(config: Arc<CsvConfig>) -> CsvlensResult<CsvlensRecordIterator> {
        Ok(if config.is_streaming() {
            CsvlensRecordIterator::Streaming(Box::new(StreamingCsvReader::new(config)?))
        } else {
            let reader = config.new_reader()?;
            CsvlensRecordIterator::Standard(reader.into_records())
        })
    }

    pub fn position(&self) -> &Position {
        match self {
            CsvlensRecordIterator::Streaming(iter) => iter.reader_position(),
            CsvlensRecordIterator::Standard(iter) => iter.reader().position(),
        }
    }
}

impl Iterator for CsvlensRecordIterator {
    type Item = CsvlensResult<csv::StringRecord>;

    fn next(&mut self) -> Option<Self::Item> {
        match self {
            CsvlensRecordIterator::Streaming(iter) => iter.next(),
            CsvlensRecordIterator::Standard(iter) => iter.next().map(|item| match item {
                Ok(record) => Ok(record),
                Err(e) => Err(e.into()),
            }),
        }
    }
}

struct ReaderInternalState {
    total_line_number: Option<usize>,
    current_line_number: Arc<AtomicUsize>,
    pos_table: Vec<Position>,
    done: bool,
    should_terminate: bool,
    #[cfg(test)]
    started_scanning: bool,
}

impl ReaderInternalState {
    fn init_internal(config: Arc<CsvConfig>) -> (Arc<Mutex<ReaderInternalState>>, JoinHandle<()>) {
        // current_line_number will be updated every record, so need a lock free way to update it
        let current_line_number = Arc::new(AtomicUsize::new(0));

        let internal = ReaderInternalState {
            total_line_number: None,
            current_line_number: current_line_number.clone(),
            pos_table: vec![],
            done: false,
            should_terminate: false,
            #[cfg(test)]
            started_scanning: false,
        };

        let m_state = Arc::new(Mutex::new(internal));

        let _m = m_state.clone();
        let handle = thread::spawn(move || {
            let pos_table_update_every = if config.is_streaming() {
                // When streaming, filesize cannot be determined. Use a larger default of 64KB (16K
                // entries for 1GB file, pos table size: 384 KB)
                #[cfg(test)]
                {
                    500
                }
                #[cfg(not(test))]
                {
                    64 * 1024
                }
            } else {
                let filesize = File::open(config.filename())
                    .unwrap()
                    .metadata()
                    .unwrap()
                    .len();
                let pos_table_num_entries = 10000;
                let minimum_interval = 500; // handle small csv (don't keep pos every byte)
                max(minimum_interval, filesize / pos_table_num_entries)
            };

            // full csv parsing
            let mut n_lines = 0;
            let mut n_bytes: u64 = 0;
            let mut last_updated_at = 0;
            let mut iter = CsvlensRecordIterator::new(config).unwrap();

            #[cfg(test)]
            {
                _m.lock().unwrap().started_scanning = true;
            }

            loop {
                let next_pos = iter.position().clone();
                if iter.next().is_none() {
                    break;
                }
                // must not include headers position here (n > 0)
                let cur = n_bytes / pos_table_update_every;
                if n_bytes > 0 && cur > last_updated_at {
                    let mut m = _m.lock().unwrap();
                    if m.should_terminate {
                        break;
                    }
                    m.pos_table.push(next_pos.clone());
                    last_updated_at = cur;
                }
                n_lines += 1;
                n_bytes = next_pos.byte();
                current_line_number.store(n_lines, Ordering::Relaxed);
            }
            let mut m = _m.lock().unwrap();
            m.total_line_number = Some(n_lines);
            m.done = true;
        });

        (m_state, handle)
    }

    fn terminate(&mut self) {
        self.should_terminate = true;
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    use rstest::rstest;

    impl Row {
        pub fn new(record_num: usize, fields: Vec<&str>) -> Row {
            Row {
                record_num,
                fields: fields.iter().map(|x| x.to_string()).collect(),
            }
        }
    }

    #[rstest]
    #[case(false)]
    #[case(true)]
    fn test_cities_get_rows(#[case] is_streaming: bool) {
        let stream_active = if is_streaming {
            Some(Arc::new(AtomicBool::new(true)))
        } else {
            None
        };
        let config = Arc::new(CsvConfig::new(
            "tests/data/cities.csv",
            stream_active.clone(),
            CsvBaseConfig::new(b',', false),
        ));
        let mut r = CsvLensReader::new(config).unwrap();
        wait_till_ready(&r, &stream_active);
        let rows = r.get_rows(2, 3).unwrap().0;
        let expected = vec![
            Row::new(
                3,
                vec![
                    "46", "35", "59", "N", "120", "30", "36", "W", "Yakima", "WA",
                ],
            ),
            Row::new(
                4,
                vec![
                    "42",
                    "16",
                    "12",
                    "N",
                    "71",
                    "48",
                    "0",
                    "W",
                    "Worcester",
                    "MA",
                ],
            ),
            Row::new(
                5,
                vec![
                    "43",
                    "37",
                    "48",
                    "N",
                    "89",
                    "46",
                    "11",
                    "W",
                    "Wisconsin Dells",
                    "WI",
                ],
            ),
        ];
        assert_eq!(rows, expected);
    }

    #[rstest]
    #[case(false)]
    #[case(true)]
    fn test_simple_get_rows(#[case] is_streaming: bool) {
        let stream_active = if is_streaming {
            Some(Arc::new(AtomicBool::new(true)))
        } else {
            None
        };
        let config = Arc::new(CsvConfig::new(
            "tests/data/simple.csv",
            stream_active.clone(),
            CsvBaseConfig::new(b',', false),
        ));
        let mut r = CsvLensReader::new(config).unwrap();
        wait_till_ready(&r, &stream_active);
        let rows = r.get_rows(1234, 2).unwrap().0;
        let expected = vec![
            Row::new(1235, vec!["A1235", "B1235"]),
            Row::new(1236, vec!["A1236", "B1236"]),
        ];
        assert_eq!(rows, expected);
    }

    #[rstest]
    #[case(false)]
    #[case(true)]
    fn test_simple_get_rows_out_of_bound(#[case] is_streaming: bool) {
        let stream_active = if is_streaming {
            Some(Arc::new(AtomicBool::new(true)))
        } else {
            None
        };
        let config = Arc::new(CsvConfig::new(
            "tests/data/simple.csv",
            stream_active.clone(),
            CsvBaseConfig::new(b',', false),
        ));
        let mut r = CsvLensReader::new(config).unwrap();
        wait_till_ready(&r, &stream_active);
        let indices = vec![5000];
        let (rows, _stats) = r.get_rows_impl(&indices).unwrap();
        assert_eq!(rows, vec![]);
    }

    #[rstest]
    #[case(false)]
    #[case(true)]
    fn test_simple_get_rows_impl_1(#[case] is_streaming: bool) {
        let stream_active = if is_streaming {
            Some(Arc::new(AtomicBool::new(true)))
        } else {
            None
        };
        let config = Arc::new(CsvConfig::new(
            "tests/data/simple.csv",
            stream_active.clone(),
            CsvBaseConfig::new(b',', false),
        ));
        let mut r = CsvLensReader::new(config).unwrap();
        wait_till_ready(&r, &stream_active);
        let indices = vec![1, 3, 5, 1234, 2345, 3456, 4999];
        let (rows, mut stats) = r.get_rows_impl(&indices).unwrap();
        let expected = vec![
            Row::new(2, vec!["A2", "B2"]),
            Row::new(4, vec!["A4", "B4"]),
            Row::new(6, vec!["A6", "B6"]),
            Row::new(1235, vec!["A1235", "B1235"]),
            Row::new(2346, vec!["A2346", "B2346"]),
            Row::new(3457, vec!["A3457", "B3457"]),
            Row::new(5000, vec!["A5000", "B5000"]),
        ];
        assert_eq!(rows, expected);
        stats.pos_table_elapsed.take();
        let expected = GetRowsStats {
            num_seek: 4,
            num_parsed_record: 218,
            pos_table_elapsed: None,
            pos_table_entry: 115,
        };
        assert_eq!(stats, expected);
    }

    #[rstest]
    #[case(false)]
    #[case(true)]
    fn test_simple_get_rows_impl_2(#[case] is_streaming: bool) {
        let stream_active = if is_streaming {
            Some(Arc::new(AtomicBool::new(true)))
        } else {
            None
        };
        let config = Arc::new(CsvConfig::new(
            "tests/data/simple.csv",
            stream_active.clone(),
            CsvBaseConfig::new(b',', false),
        ));
        let mut r = CsvLensReader::new(config).unwrap();
        wait_till_ready(&r, &stream_active);
        let indices = vec![1234];
        let (rows, mut stats) = r.get_rows_impl(&indices).unwrap();
        let expected = vec![Row::new(1235, vec!["A1235", "B1235"])];
        assert_eq!(rows, expected);
        stats.pos_table_elapsed.take();
        let expected = GetRowsStats {
            num_seek: 1,
            num_parsed_record: 8,
            pos_table_elapsed: None,
            pos_table_entry: 115,
        };
        assert_eq!(stats, expected);
    }

    #[rstest]
    #[case(false)]
    #[case(true)]
    fn test_simple_get_rows_impl_3(#[case] is_streaming: bool) {
        let stream_active = if is_streaming {
            Some(Arc::new(AtomicBool::new(true)))
        } else {
            None
        };
        let config = Arc::new(CsvConfig::new(
            "tests/data/simple.csv",
            stream_active.clone(),
            CsvBaseConfig::new(b',', false),
        ));
        let mut r = CsvLensReader::new(config).unwrap();
        wait_till_ready(&r, &stream_active);
        let indices = vec![2];
        let (rows, mut stats) = r.get_rows_impl(&indices).unwrap();
        let expected = vec![Row::new(3, vec!["A3", "B3"])];
        assert_eq!(rows, expected);
        stats.pos_table_elapsed.take();
        let expected = GetRowsStats {
            num_seek: 0,
            num_parsed_record: 4, // 3 + 1 (including header)
            pos_table_elapsed: None,
            pos_table_entry: 115,
        };
        assert_eq!(stats, expected);
    }

    #[rstest]
    #[case(false)]
    #[case(true)]
    fn test_small(#[case] is_streaming: bool) {
        let stream_active = if is_streaming {
            Some(Arc::new(AtomicBool::new(true)))
        } else {
            None
        };
        let config = Arc::new(CsvConfig::new(
            "tests/data/small.csv",
            stream_active.clone(),
            CsvBaseConfig::new(b',', false),
        ));
        let mut r = CsvLensReader::new(config).unwrap();
        wait_till_ready(&r, &stream_active);
        let rows = r.get_rows(0, 50).unwrap().0;
        let expected = vec![
            Row::new(1, vec!["c1", " v1"]),
            Row::new(2, vec!["c2", " v2"]),
        ];
        assert_eq!(rows, expected);
    }

    #[rstest]
    #[case(false)]
    #[case(true)]
    fn test_small_delimiter(#[case] is_streaming: bool) {
        let stream_active = if is_streaming {
            Some(Arc::new(AtomicBool::new(true)))
        } else {
            None
        };
        let config = Arc::new(CsvConfig::new(
            "tests/data/small.bsv",
            stream_active.clone(),
            CsvBaseConfig::new(b'|', false),
        ));
        let mut r = CsvLensReader::new(config).unwrap();
        wait_till_ready(&r, &stream_active);
        let rows = r.get_rows(0, 50).unwrap().0;
        let expected = vec![Row::new(1, vec!["c1", "v1"]), Row::new(2, vec!["c2", "v2"])];
        assert_eq!(rows, expected);
    }

    #[rstest]
    #[case(false)]
    #[case(true)]
    fn test_irregular(#[case] is_streaming: bool) {
        let stream_active = if is_streaming {
            Some(Arc::new(AtomicBool::new(true)))
        } else {
            None
        };
        let config = Arc::new(CsvConfig::new(
            "tests/data/irregular.csv",
            stream_active.clone(),
            CsvBaseConfig::new(b',', false),
        ));
        let mut r = CsvLensReader::new(config).unwrap();
        wait_till_ready(&r, &stream_active);
        let rows = r.get_rows(0, 50).unwrap().0;
        let expected = vec![Row::new(1, vec!["c1"]), Row::new(2, vec!["c2", " v2"])];
        assert_eq!(rows, expected);
    }

    #[rstest]
    #[case(false)]
    #[case(true)]
    fn test_double_quoting_as_escape_chars(#[case] is_streaming: bool) {
        let stream_active = if is_streaming {
            Some(Arc::new(AtomicBool::new(true)))
        } else {
            None
        };
        let config = Arc::new(CsvConfig::new(
            "tests/data/good_double_quote.csv",
            stream_active.clone(),
            CsvBaseConfig::new(b',', false),
        ));
        let mut r = CsvLensReader::new(config).unwrap();
        wait_till_ready(&r, &stream_active);
        let rows = r.get_rows(0, 50).unwrap().0;
        let expected = vec![
            Row::new(1, vec!["1", "quote"]),
            Row::new(2, vec!["5", "Comma, comma"]),
        ];
        assert_eq!(rows, expected);
    }

    #[rstest]
    #[case(false)]
    #[case(true)]
    fn get_rows_unsorted_indices(#[case] is_streaming: bool) {
        let stream_active = if is_streaming {
            Some(Arc::new(AtomicBool::new(true)))
        } else {
            None
        };
        let config = Arc::new(CsvConfig::new(
            "tests/data/simple.csv",
            stream_active.clone(),
            CsvBaseConfig::new(b',', false),
        ));
        let mut r = CsvLensReader::new(config).unwrap();
        wait_till_ready(&r, &stream_active);
        let rows = r.get_rows_for_indices(&vec![1235, 1234]).unwrap().0;
        let expected = vec![
            Row::new(1236, vec!["A1236", "B1236"]),
            Row::new(1235, vec!["A1235", "B1235"]),
        ];
        assert_eq!(rows, expected);
    }

    #[rstest]
    #[case(false)]
    #[case(true)]
    fn test_streaming_100(#[case] is_streaming: bool) {
        let stream_active = if is_streaming {
            Some(Arc::new(AtomicBool::new(true)))
        } else {
            None
        };
        let config = Arc::new(CsvConfig::new(
            "tests/data/test_streaming_100.csv",
            stream_active.clone(),
            CsvBaseConfig::new(b',', false),
        ));
        let mut r = CsvLensReader::new(config).unwrap();
        wait_till_ready(&r, &stream_active);
        let rows = r.get_rows_for_indices(&vec![95]).unwrap().0;
        let expected = vec![Row::new(
            96,
            vec!["2020-05-05", "1000717", "717490024", "0", "train"],
        )];
        assert_eq!(rows, expected);
    }

    #[rstest]
    #[case(false)]
    #[case(true)]
    fn test_streaming_100_tsv(#[case] is_streaming: bool) {
        let stream_active = if is_streaming {
            Some(Arc::new(AtomicBool::new(true)))
        } else {
            None
        };
        let config = Arc::new(CsvConfig::new(
            "tests/data/test_streaming_100.tsv",
            stream_active.clone(),
            CsvBaseConfig::new(b'\t', false),
        ));
        let mut r = CsvLensReader::new(config).unwrap();
        wait_till_ready(&r, &stream_active);
        let rows = r.get_rows_for_indices(&vec![95]).unwrap().0;
        let expected = vec![Row::new(
            96,
            vec!["2020-05-05", "1000717", "717490024", "0", "train"],
        )];
        assert_eq!(rows, expected);
    }

    #[rstest]
    #[case(false)]
    #[case(true)]
    fn test_streaming_100_iterator(#[case] is_streaming: bool) {
        let stream_active = if is_streaming {
            Some(Arc::new(AtomicBool::new(true)))
        } else {
            None
        };
        let config = Arc::new(CsvConfig::new(
            "tests/data/test_streaming_100.csv",
            stream_active.clone(),
            CsvBaseConfig::new(b',', false),
        ));
        let mut iter = CsvlensRecordIterator::new(config).unwrap();
        iter.next();
        let position = iter.position();
        let mut expected = Position::new();
        // This is one case where record is not necessarily (line - 1)
        expected.set_byte(79);
        expected.set_line(2);
        expected.set_record(2);
        assert_eq!(*position, expected);
    }

    fn wait_till_ready(reader: &CsvLensReader, stream_active: &Option<Arc<AtomicBool>>) {
        // Wait till scanning starts. This will make the scanning use streaming / non-streaming
        // iterator based on the initial value of stream_active
        reader.wait_till_start_scanning();

        // Now turn off streaming mode if applicable so that the internal thread can finish
        stream_active
            .as_ref()
            .map(|x| x.store(false, Ordering::Relaxed));

        // Finally wait till internal thread is done
        reader.wait_internal();
    }
}
```

## File: `src/delimiter.rs`
```rust
use crate::errors::{CsvlensError, CsvlensResult};

/// Delimiter behaviour as specified in the command line
#[derive(Debug)]
pub enum Delimiter {
    /// Use the default delimiter (auto detect)
    Default,

    /// Comma delimiter
    Comma,

    /// Use tab as the delimiter
    Tab,

    /// Use the specified delimiter
    Character(u8),

    /// Auto-detect the delimiter
    Auto,
}

impl Delimiter {
    /// Create a Delimiter by parsing the command line argument for the delimiter
    pub fn from_arg(
        delimiter_arg: &Option<String>,
        tab_separation: bool,
        comma_separation: bool,
    ) -> CsvlensResult<Self> {
        if comma_separation {
            return Ok(Delimiter::Comma);
        }
        if tab_separation {
            return Ok(Delimiter::Tab);
        }

        if let Some(s) = delimiter_arg {
            if s == "auto" {
                return Ok(Delimiter::Auto);
            }
            if s == r"\t" {
                return Ok(Delimiter::Tab);
            }
            let mut chars = s.chars();
            let c = chars.next().ok_or_else(|| CsvlensError::DelimiterEmpty)?;
            if !c.is_ascii() {
                return Err(CsvlensError::DelimiterNotAscii(c));
            }
            if chars.next().is_some() {
                return Err(CsvlensError::DelimiterMultipleCharacters(s.clone()));
            }
            if c == 't' {
                // commonly occurrs when argument is specified like "-d \t" without quotes
                return Ok(Delimiter::Tab);
            }
            Ok(Delimiter::Character(c.try_into()?))
        } else {
            Ok(Delimiter::Default)
        }
    }
}

/// Sniff the delimiter from the file
pub fn sniff_delimiter(filename: &str) -> Option<u8> {
    let mut sniffer = csv_nose::Sniffer::new();
    sniffer.sample_size(csv_nose::SampleSize::Records(200));
    if let Ok(metadata) = sniffer.sniff_path(filename) {
        return Some(metadata.dialect.delimiter);
    }
    None
}
```

## File: `src/errors.rs`
```rust
use thiserror::Error;

pub type CsvlensResult<T> = std::result::Result<T, CsvlensError>;

/// Errors csvlens can have
#[derive(Debug, Error)]
pub enum CsvlensError {
    #[error("File not found: {0}")]
    FileNotFound(String),

    #[error("Column name not found: {0}")]
    ColumnNameNotFound(String),

    #[error("Delimiter should not be empty")]
    DelimiterEmpty,

    #[error("Delimiter should be within the ASCII range: {0} is too fancy")]
    DelimiterNotAscii(char),

    #[error("Delimiter should be exactly one character (or \\t), got '{0}'")]
    DelimiterMultipleCharacters(String),

    #[error(transparent)]
    DelimiterParsing(#[from] std::char::TryFromCharError),

    #[error(transparent)]
    Csv(#[from] csv::Error),

    #[error(transparent)]
    CsvFromUtf8Error(#[from] csv::FromUtf8Error),

    #[error(transparent)]
    Arrow(#[from] arrow::error::ArrowError),

    #[error(transparent)]
    Io(#[from] std::io::Error),

    #[error("Draw error: {0}")]
    DrawError(String),
}
```

## File: `src/find.rs`
```rust
use crate::columns_filter;
use crate::csv;
use crate::csv::CsvlensRecordIterator;
use crate::errors::CsvlensResult;
use crate::sort;
use crate::sort::SortOrder;
use regex::Regex;
use sorted_vec::SortedVec;
use std::cmp::min;
use std::sync::{Arc, Mutex, MutexGuard};
use std::thread::{self};
use std::time::{Duration, Instant};

#[derive(Debug, Clone)]
pub enum RowPos {
    Header,
    Row(usize),
}

#[derive(Debug, Clone)]
pub struct FinderCursor {
    pub row: RowPos,
    pub column: usize,
}

impl FinderCursor {
    fn next_row(&self, total_count: usize) -> FinderCursor {
        match self.row {
            RowPos::Header => FinderCursor {
                row: if total_count > 0 {
                    RowPos::Row(0)
                } else {
                    RowPos::Header
                },
                column: 0,
            },
            RowPos::Row(n) => FinderCursor {
                row: if n + 1 < total_count {
                    RowPos::Row(n + 1)
                } else {
                    RowPos::Row(n)
                },
                column: 0,
            },
        }
    }

    fn prev_row(&self, has_header_found: bool) -> FinderCursor {
        match self.row {
            RowPos::Header => FinderCursor {
                row: RowPos::Header,
                column: 0,
            },
            RowPos::Row(0) => FinderCursor {
                row: if has_header_found {
                    RowPos::Header
                } else {
                    RowPos::Row(0)
                },
                column: 0,
            },
            RowPos::Row(n) => FinderCursor {
                row: RowPos::Row(n.saturating_sub(1)),
                column: 0,
            },
        }
    }

    fn next_column(&self) -> FinderCursor {
        match self.row {
            RowPos::Header => FinderCursor {
                row: RowPos::Header,
                column: self.column.saturating_add(1),
            },
            RowPos::Row(n) => FinderCursor {
                row: RowPos::Row(n),
                column: self.column.saturating_add(1),
            },
        }
    }

    fn prev_column(&self) -> FinderCursor {
        match self.row {
            RowPos::Header => FinderCursor {
                row: RowPos::Header,
                column: self.column.saturating_sub(1),
            },
            RowPos::Row(n) => FinderCursor {
                row: RowPos::Row(n),
                column: self.column.saturating_sub(1),
            },
        }
    }
}

pub struct Finder {
    internal: Arc<Mutex<FinderInternalState>>,
    pub cursor: Option<FinderCursor>,
    row_hint: usize,
    target: Regex,
    column_index: Option<usize>,
    starting_row_index: usize,
    sorter: Option<Arc<sort::Sorter>>,
    pub sort_order: SortOrder,
}

#[derive(Clone, Debug)]
pub enum FoundEntry {
    Header(HeaderEntry),
    Row(RowEntry),
}

#[derive(Clone, Debug)]
pub struct RowEntry {
    row_index: usize,
    row_order: usize,
    column_index: usize,
}

impl RowEntry {
    pub fn row_index(&self) -> usize {
        self.row_index
    }

    pub fn row_order(&self) -> usize {
        self.row_order
    }

    pub fn column_index(&self) -> usize {
        self.column_index
    }
}

#[derive(Clone, Debug)]
pub struct HeaderEntry {
    column_index: usize,
}

impl HeaderEntry {
    pub fn column_index(&self) -> usize {
        self.column_index
    }
}

#[derive(Clone, Debug)]
pub struct FoundHeader {
    column_indices: Vec<usize>,
}

impl FoundHeader {
    pub fn column_indices(&self) -> &Vec<usize> {
        &self.column_indices
    }

    pub fn get_entry(&self, entry_index: usize) -> Option<HeaderEntry> {
        self.column_indices
            .get(entry_index)
            .map(|column_index| HeaderEntry {
                column_index: *column_index,
            })
    }
}

#[derive(Clone, Debug)]
pub struct FoundRow {
    row_index: usize,
    row_order: usize,
    column_indices: Vec<usize>,
}

impl FoundRow {
    pub fn row_index(&self) -> usize {
        self.row_index
    }

    pub fn row_order(&self) -> usize {
        self.row_order
    }

    pub fn column_indices(&self) -> &Vec<usize> {
        &self.column_indices
    }

    pub fn get_entry(&self, entry_index: usize) -> Option<RowEntry> {
        self.column_indices
            .get(entry_index)
            .map(|column_index| RowEntry {
                row_index: self.row_index,
                row_order: self.row_order,
                column_index: *column_index,
            })
    }
}

impl Ord for FoundRow {
    fn cmp(&self, other: &Self) -> std::cmp::Ordering {
        self.row_order.cmp(&other.row_order)
    }
}

impl PartialOrd for FoundRow {
    fn partial_cmp(&self, other: &Self) -> Option<std::cmp::Ordering> {
        Some(self.cmp(other))
    }
}

impl PartialEq for FoundRow {
    fn eq(&self, other: &Self) -> bool {
        self.row_order == other.row_order
    }
}

impl Eq for FoundRow {}

impl Finder {
    pub fn new(
        config: Arc<csv::CsvConfig>,
        target: Regex,
        column_index: Option<usize>,
        starting_row_index: usize,
        sorter: Option<Arc<sort::Sorter>>,
        sort_order: SortOrder,
        columns_filter: Option<Arc<columns_filter::ColumnsFilter>>,
    ) -> CsvlensResult<Self> {
        let internal = FinderInternalState::init(
            config,
            target.clone(),
            column_index,
            starting_row_index,
            sorter.clone(),
            sort_order,
            columns_filter,
        );
        let finder = Finder {
            internal,
            cursor: None,
            row_hint: starting_row_index,
            target,
            column_index,
            starting_row_index,
            sorter: sorter.clone(),
            sort_order,
        };
        Ok(finder)
    }

    pub fn count(&self) -> usize {
        (self.internal.lock().unwrap()).count
    }

    pub fn count_and_max_row_index(&self) -> (usize, Option<u64>) {
        let g = self.internal.lock().unwrap();
        (g.count, g.founds.last().map(|x| x.row_index() as u64))
    }

    pub fn found_any(&self) -> bool {
        let g = self.internal.lock().unwrap();
        g.count > 0 || g.found_header.is_some()
    }

    pub fn header_has_match(&self) -> bool {
        (self.internal.lock().unwrap()).found_header.is_some()
    }

    pub fn done(&self) -> bool {
        (self.internal.lock().unwrap()).done
    }

    pub fn cursor(&self) -> Option<FinderCursor> {
        self.cursor.as_ref().cloned()
    }

    pub fn cursor_row_order(&self) -> Option<usize> {
        let m_guard = self.internal.lock().unwrap();
        if let Some(FoundEntry::Row(entry)) =
            self.get_found_record_at_cursor(&m_guard, &self.cursor)
        {
            Some(entry.row_order())
        } else {
            None
        }
    }

    pub fn target(&self) -> Regex {
        self.target.clone()
    }

    pub fn column_index(&self) -> Option<usize> {
        self.column_index
    }

    pub fn starting_row_index(&self) -> usize {
        self.starting_row_index
    }

    pub fn sorter(&self) -> &Option<Arc<sort::Sorter>> {
        &self.sorter
    }

    pub fn reset_cursor(&mut self) {
        self.cursor = None;
    }

    pub fn set_row_hint(&mut self, row_hint: usize) {
        self.row_hint = row_hint;
    }

    pub fn set_initial_cursor_if_ready(&mut self) -> Option<FoundEntry> {
        let m_guard = self.internal.lock().unwrap();
        if let Some(cursor_row) = m_guard.founds_index_after_starting_row {
            self.cursor = Some(FinderCursor {
                row: RowPos::Row(cursor_row),
                column: 0,
            });
        }
        self.get_found_record_at_cursor(&m_guard, &self.cursor)
    }

    pub fn next(&mut self) -> Option<FoundEntry> {
        let m_guard = self.internal.lock().unwrap();
        let count = m_guard.count;
        let founds = &m_guard.founds;
        let found_header = &m_guard.found_header;
        if let Some(cursor) = &self.cursor {
            let column_indices = match cursor.row {
                RowPos::Header => m_guard.found_header.as_ref().map(|x| x.column_indices()),
                RowPos::Row(n) => founds.get(n).map(|x| x.column_indices()),
            };
            if let Some(column_indices) = column_indices {
                if cursor.column + 1 < column_indices.len() {
                    // Try next column first if available
                    self.cursor = Some(cursor.next_column());
                } else {
                    // Next row if available
                    self.cursor = Some(cursor.next_row(count));
                }
            }
        } else if count > 0 {
            self.cursor = Some(FinderCursor {
                row: RowPos::Row(m_guard.next_from(self.row_hint)),
                column: 0,
            });
        } else if found_header.is_some() {
            // No rows found, but header has match
            self.cursor = Some(FinderCursor {
                row: RowPos::Header,
                column: 0,
            });
        }
        self.get_found_record_at_cursor(&m_guard, &self.cursor)
    }

    pub fn prev(&mut self) -> Option<FoundEntry> {
        let m_guard = self.internal.lock().unwrap();
        if let Some(cursor) = &self.cursor {
            if cursor.column > 0 {
                // Try previous column first if available
                self.cursor = Some(cursor.prev_column());
            } else {
                // Previous row if available
                self.cursor = Some(cursor.prev_row(m_guard.found_header.is_some()));
            }
        } else if m_guard.count > 0 {
            self.cursor = Some(FinderCursor {
                row: RowPos::Row(m_guard.prev_from(self.row_hint)),
                column: 0,
            });
        } else if m_guard.found_header.is_some() {
            // No rows found, but header has match
            self.cursor = Some(FinderCursor {
                row: RowPos::Header,
                column: 0,
            });
        }
        self.get_found_record_at_cursor(&m_guard, &self.cursor)
    }

    pub fn current(&self) -> Option<FoundEntry> {
        let m_guard = self.internal.lock().unwrap();
        self.get_found_record_at_cursor(&m_guard, &self.cursor)
    }

    fn get_found_record_at_cursor(
        &self,
        m_guard: &MutexGuard<FinderInternalState>,
        cursor: &Option<FinderCursor>,
    ) -> Option<FoundEntry> {
        if let Some(cursor) = cursor {
            match cursor.row {
                RowPos::Header => m_guard
                    .found_header
                    .as_ref()
                    .and_then(|x| x.get_entry(cursor.column))
                    .map(FoundEntry::Header),
                RowPos::Row(n) => m_guard
                    .founds
                    .get(n)
                    .and_then(|x| x.get_entry(cursor.column))
                    .map(FoundEntry::Row),
            }
        } else {
            None
        }
    }

    fn terminate(&self) {
        let mut m_guard = self.internal.lock().unwrap();
        m_guard.terminate();
    }

    pub fn elapsed(&self) -> Option<Duration> {
        let m_guard = self.internal.lock().unwrap();
        m_guard.elapsed()
    }

    pub fn get_subset_found(&self, offset: usize, num_rows: usize) -> Vec<u64> {
        let m_guard = self.internal.lock().unwrap();
        let founds = &m_guard.founds;
        let start = min(offset, founds.len().saturating_sub(1));
        let end = start.saturating_add(num_rows);
        let end = min(end, founds.len());
        let indices: Vec<u64> = founds[start..end]
            .iter()
            .map(|x| x.row_index() as u64)
            .collect();
        indices
    }

    #[cfg(test)]
    pub fn wait_internal(&self) {
        loop {
            if self.internal.lock().unwrap().done {
                break;
            }
            thread::sleep(core::time::Duration::from_millis(100));
        }
    }
}

impl Drop for Finder {
    fn drop(&mut self) {
        self.terminate();
    }
}

struct FinderInternalState {
    count: usize,
    found_header: Option<FoundHeader>,
    founds: SortedVec<FoundRow>,
    founds_index_after_starting_row: Option<usize>,
    done: bool,
    should_terminate: bool,
    start: Instant,
    first_match_elapsed: Option<Duration>,
    elapsed: Option<Duration>,
}

impl FinderInternalState {
    pub fn init(
        config: Arc<csv::CsvConfig>,
        target: Regex,
        target_local_column_index: Option<usize>,
        starting_row_index: usize,
        sorter: Option<Arc<sort::Sorter>>,
        sort_order: SortOrder,
        columns_filter: Option<Arc<columns_filter::ColumnsFilter>>,
    ) -> Arc<Mutex<FinderInternalState>> {
        let internal = FinderInternalState {
            count: 0,
            found_header: None,
            founds: SortedVec::new(),
            founds_index_after_starting_row: None,
            done: false,
            should_terminate: false,
            start: Instant::now(),
            first_match_elapsed: None,
            elapsed: None,
        };

        let m_state = Arc::new(Mutex::new(internal));

        let _m = m_state.clone();
        let _filename = config.filename().to_owned();

        let _handle = thread::spawn(move || {
            let mut bg_reader = config.new_reader().unwrap();

            // search header
            let mut column_indices = vec![];
            if let Ok(header) = bg_reader.headers() {
                let mut local_column_index = 0;
                for (column_index, field) in header.iter().enumerate() {
                    if let Some(columns_filter) = &columns_filter
                        && !columns_filter.is_column_filtered(column_index)
                    {
                        continue;
                    }
                    if target.is_match(field) {
                        column_indices.push(local_column_index);
                    }
                    local_column_index += 1;
                }
            }
            if !column_indices.is_empty() {
                let found = FoundHeader { column_indices };
                let mut m = _m.lock().unwrap();
                m.found_header = Some(found);
            }

            // note that records() excludes header
            let records = CsvlensRecordIterator::new(config).unwrap();

            for (row_index, r) in records.enumerate() {
                let mut column_indices = vec![];
                if let Ok(valid_record) = r {
                    let mut local_column_index = 0;
                    for (column_index, field) in valid_record.iter().enumerate() {
                        if let Some(columns_filter) = &columns_filter
                            && !columns_filter.is_column_filtered(column_index)
                        {
                            continue;
                        }
                        let should_check_regex =
                            if let Some(target_local_column_index) = target_local_column_index {
                                local_column_index == target_local_column_index
                            } else {
                                true
                            };
                        if should_check_regex && target.is_match(field) {
                            column_indices.push(local_column_index);
                        }
                        local_column_index += 1;
                    }
                }
                if !column_indices.is_empty() {
                    let row_order = match &sorter {
                        Some(s) => s
                            .get_record_order(row_index as u64, sort_order)
                            .unwrap_or(u64::MAX) as usize,
                        _ => row_index,
                    };
                    let found = FoundRow {
                        row_index,
                        row_order,
                        column_indices,
                    };
                    let mut m = _m.lock().unwrap();
                    // Update founds_index_after_starting_row if not set yet for non-sorting case.
                    // Sorting case needs to be handled differently since the record order is not
                    // sequential
                    if row_order >= starting_row_index
                        && m.founds_index_after_starting_row.is_none()
                        && sorter.is_none()
                    {
                        m.founds_index_after_starting_row = Some(m.count);
                    }
                    (*m).found_one(found);
                }
                let m = _m.lock().unwrap();
                if m.should_terminate {
                    break;
                }
            }

            let mut m = _m.lock().unwrap();

            // Update founds_index_after_starting_row for sorting case after all records are scanned
            if sorter.is_some() {
                let found_index = m.next_from(starting_row_index);
                if let Some(found) = m.founds.get(found_index)
                    && found.row_order() >= starting_row_index
                {
                    m.founds_index_after_starting_row = Some(found_index);
                }
            };

            m.done = true;
            m.elapsed = Some(m.start.elapsed());
        });

        m_state
    }

    fn found_one(&mut self, found: FoundRow) {
        if self.first_match_elapsed.is_none() {
            self.first_match_elapsed = Some(self.start.elapsed());
        }
        self.founds.push(found);
        self.count += 1;
    }

    fn next_from(&self, row_hint: usize) -> usize {
        let mut index = self.founds.partition_point(|r| r.row_order() < row_hint);
        if index >= self.founds.len() {
            index -= 1;
        }
        index
    }

    fn prev_from(&self, row_hint: usize) -> usize {
        let next = self.next_from(row_hint);
        if next > 0 { next - 1 } else { next }
    }

    fn terminate(&mut self) {
        self.should_terminate = true;
    }

    fn elapsed(&self) -> Option<Duration> {
        self.elapsed
    }
}
```

## File: `src/help.rs`
```rust
use ratatui::{
    buffer::Buffer,
    layout::Rect,
    style::{Color, Modifier, Style},
    text::{Line, Span},
    widgets::{Block, Borders, Paragraph, StatefulWidget, Widget, Wrap},
};

const HELP_CONTENT: &str = "
csvlens is an interactive CSV file viewer in the command line.

These are the key bindings. Press q to exit.

# Moving

hjkl (or ← ↓ ↑ →)       : Scroll one row or column in the given direction
Ctrl + f (or Page Down) : Scroll one window down
Ctrl + b (or Page Up)   : Scroll one window up
Ctrl + d (or d)         : Scroll half a window down
Ctrl + u (or u)         : Scroll half a window up
Ctrl + h                : Scroll one window left
Ctrl + l                : Scroll one window right
Ctrl + ←                : Scroll left to first column
Ctrl + →                : Scroll right to last column
G (or End)              : Go to bottom
g (or Home)             : Go to top
<n>G                    : Go to line n

# Search

/<regex>                : Find content matching regex and highlight matches
n (in Find mode)        : Jump to next result
N (in Find mode)        : Jump to previous result
&<regex>                : Filter rows using regex (show only matches)
*<regex>                : Filter columns using regex (show only matches)

# Selection modes

TAB                     : Toggle between row, column or cell selection modes
>                       : Increase selected column's width
<                       : Decrease selected column's width
Shift + ↓ (or J)        : Sort rows by the selected column (auto by type: numeric for numbers and lexicographic for text)
Ctrl + J                : Sort rows by the selected column (natural; e.g. \"file2\" < \"file10\")
# (in Cell mode)        : Find and highlight rows like the selected cell
@ (in Cell mode)        : Filter rows like the selected cell
y                       : Copy the selected row or cell to clipboard
Enter (in Cell mode)    : Print the selected cell to stdout and exit

# Other options

-S                      : Toggle line wrapping
-W                      : Toggle line wrapping by words
f<n>                    : Freeze this number of columns from the left
r                       : Reset to default view (clear all filters and custom column widths)
H (or ?)                : Display this help
m                       : Mark / unmark the selected row visually
M                       : Clear all row marks
Ctrl + e                : Print the marked rows (with header) to stdout and exit
q                       : Exit";

pub struct HelpPage {}

pub struct HelpPageState {
    active: bool,
    offset: u16,
    render_complete: bool,
}

impl HelpPage {
    pub fn new() -> Self {
        HelpPage {}
    }
}

impl HelpPageState {
    pub fn new() -> Self {
        HelpPageState {
            active: false,
            offset: 0,
            render_complete: true,
        }
    }

    pub fn activate(&mut self) -> &Self {
        self.active = true;
        self.offset = 0;
        self
    }

    pub fn deactivate(&mut self) -> &Self {
        self.active = false;
        self.offset = 0;
        self
    }

    pub fn is_active(&self) -> bool {
        self.active
    }

    pub fn scroll_up(&mut self) -> &Self {
        if self.offset > 0 {
            self.offset -= 1;
        }
        self
    }

    pub fn scroll_down(&mut self) -> &Self {
        if !self.render_complete {
            self.offset += 1;
        }
        self
    }
}

impl StatefulWidget for HelpPage {
    type State = HelpPageState;

    fn render(self, area: Rect, buf: &mut Buffer, state: &mut Self::State) {
        fn line_to_span(line: &str) -> Span<'_> {
            if line.starts_with("# ") && !line.contains(':') {
                let header_style = Style::default()
                    .add_modifier(Modifier::BOLD)
                    .fg(Color::Rgb(200, 200, 200));
                let header_formatted = format!("[{}]", line.strip_prefix("# ").unwrap());
                Span::styled(header_formatted, header_style)
            } else {
                Span::raw(line)
            }
        }

        let text: Vec<Line> = HELP_CONTENT
            .split('\n')
            .map(|s| Line::from(line_to_span(s)))
            .collect();

        // Minus 2 to account for borders.
        let num_lines_to_be_rendered = (text.len() as u16).saturating_sub(state.offset);
        state.render_complete = area.height.saturating_sub(2) >= num_lines_to_be_rendered;

        let paragraph = Paragraph::new(text)
            .block(Block::default().title("Help").borders(Borders::ALL))
            .wrap(Wrap { trim: true })
            .scroll((state.offset, 0));

        paragraph.render(area, buf);
    }
}
```

## File: `src/history.rs`
```rust
use crate::common::InputMode;
use std::collections::HashMap;
use std::collections::hash_map::Entry::{Occupied, Vacant};

pub struct BufferHistory {
    buffers: Vec<String>,
    cursor: usize,
}

impl BufferHistory {
    fn new_with(buf: &str) -> Self {
        BufferHistory {
            buffers: vec![buf.to_string()],
            cursor: 1,
        }
    }

    fn push(&mut self, buf: &str) {
        if buf.is_empty() {
            // Don't keep empty entries
            return;
        }
        if let Some(index) = self.buffers.iter().position(|x| x == buf) {
            // Don't keep duplicate entries
            self.buffers.remove(index);
        }
        self.buffers.push(buf.to_string());
        self.reset_cursor();
    }

    fn prev(&mut self) -> Option<String> {
        if self.cursor == 0 {
            return None;
        }
        self.cursor = self.cursor.saturating_sub(1);
        Some(self.buffers[self.cursor].clone())
    }

    fn next(&mut self) -> Option<String> {
        if self.cursor >= self.buffers.len() - 1 {
            return None;
        }
        self.cursor = self.cursor.saturating_add(1);
        Some(self.buffers[self.cursor].clone())
    }

    fn reset_cursor(&mut self) {
        self.cursor = self.buffers.len();
    }
}

pub struct BufferHistoryContainer {
    inner: HashMap<InputMode, BufferHistory>,
}

impl BufferHistoryContainer {
    pub fn new() -> Self {
        BufferHistoryContainer {
            inner: HashMap::new(),
        }
    }

    pub fn set(&mut self, input_mode: InputMode, content: &str) {
        match self.inner.entry(input_mode) {
            Occupied(mut e) => {
                e.get_mut().push(content);
            }
            Vacant(e) => {
                e.insert(BufferHistory::new_with(content));
            }
        }
    }

    pub fn prev(&mut self, input_mode: InputMode) -> Option<String> {
        self.inner
            .get_mut(&input_mode)
            .and_then(|history| history.prev())
    }

    pub fn next(&mut self, input_mode: InputMode) -> Option<String> {
        self.inner
            .get_mut(&input_mode)
            .and_then(|history| history.next())
    }

    pub fn reset_cursors(&mut self) {
        for (_, history) in self.inner.iter_mut() {
            history.reset_cursor();
        }
    }
}

#[cfg(test)]
mod tests {

    use super::*;

    #[test]
    fn test_prev_next() {
        let mut history = BufferHistory::new_with("foo");
        history.push("bar");
        history.push("baz");
        history.push("foo");
        assert_eq!(history.prev(), Some("foo".to_string()));
        assert_eq!(history.prev(), Some("baz".to_string()));
        assert_eq!(history.prev(), Some("bar".to_string()));
        assert_eq!(history.prev(), None);
        assert_eq!(history.prev(), None);
        assert_eq!(history.next(), Some("baz".to_string()));
        assert_eq!(history.next(), Some("foo".to_string()));
        assert_eq!(history.next(), None);
        assert_eq!(history.next(), None);
    }

    #[test]
    fn test_push_duplicate() {
        let mut history = BufferHistory::new_with("foo");
        history.push("bar");
        history.push("baz");
        history.push("foo");
        history.push("bar");
        assert_eq!(history.prev(), Some("bar".to_string()));
        assert_eq!(history.prev(), Some("foo".to_string()));
        assert_eq!(history.prev(), Some("baz".to_string()));
        assert_eq!(history.prev(), None);
    }

    #[test]
    fn test_container() {
        let mut history_container = BufferHistoryContainer::new();
        history_container.set(InputMode::Find, "foo");
        history_container.set(InputMode::Find, "bar");
        history_container.set(InputMode::GotoLine, "123");
        history_container.set(InputMode::GotoLine, "456");
        assert_eq!(history_container.prev(InputMode::Default), None);
        assert_eq!(
            history_container.prev(InputMode::Find),
            Some("bar".to_string())
        );
        assert_eq!(
            history_container.prev(InputMode::GotoLine),
            Some("456".to_string())
        );
    }
}
```

## File: `src/input.rs`
```rust
use crate::app::WrapMode;
use crate::common::InputMode;
use crate::history::BufferHistoryContainer;
use crate::util::events::{CsvlensEvent, CsvlensEvents};
use crate::watch::FileWatcher;
use crossterm::event::{Event, KeyCode, KeyEvent, KeyModifiers};
use tui_input::Input;
use tui_input::backend::crossterm::EventHandler;

pub enum Control {
    ScrollUp,
    ScrollDown,
    ScrollLeft,
    ScrollRight,
    ScrollTop,
    ScrollBottom,
    ScrollPageUp,
    ScrollPageDown,
    ScrollHalfPageUp,
    ScrollHalfPageDown,
    ScrollPageLeft,
    ScrollPageRight,
    ScrollLeftMost,
    ScrollRightMost,
    ScrollTo(usize),
    ScrollToNextFound,
    ScrollToPrevFound,
    IncreaseWidth,
    DecreaseWidth,
    Find(String),
    FindLikeCell,
    Filter(String),
    FilterColumns(String),
    FilterLikeCell,
    FreezeColumns(usize),
    Quit,
    BufferContent(Input),
    BufferReset,
    Select,
    CopySelection,
    SelectMarks,
    ToggleSelectionType,
    ToggleLineWrap(WrapMode),
    ToggleMark,
    ResetMarks,
    ToggleSort,
    ToggleNaturalSort,
    Reset,
    Help,
    UnknownOption(String),
    UserError(String),
    FileChanged,
    Nothing,
}

impl Control {
    fn empty_buffer() -> Control {
        Control::BufferContent("".into())
    }
}

enum BufferState {
    Active(Input),
    Inactive,
}

pub struct InputHandler {
    events: CsvlensEvents,
    mode: InputMode,
    buffer_state: BufferState,
    buffer_history_container: BufferHistoryContainer,
}

impl InputHandler {
    pub fn new(file_watcher: Option<FileWatcher>) -> InputHandler {
        InputHandler {
            events: CsvlensEvents::new(file_watcher),
            mode: InputMode::Default,
            buffer_state: BufferState::Inactive,
            buffer_history_container: BufferHistoryContainer::new(),
        }
    }

    pub fn next(&mut self) -> Control {
        match self.events.next().unwrap() {
            CsvlensEvent::Input(key) => self.handle_key(key),
            CsvlensEvent::FileChanged => Control::FileChanged,
            CsvlensEvent::Tick => Control::Nothing,
        }
    }

    fn handle_key(&mut self, mut key: KeyEvent) -> Control {
        /*
        The shift key modifier is not consistent across platforms.

        For upper case alphabets, e.g. 'A'

        Unix: Char("A") + SHIFT
        Windows: Char("A") + SHIFT

        For non-alphabets, e.g. '>'

        Unix: Char(">") + NULL
        Windows: Char(">") + SHIFT

        But the key event handling below assumes that the shift key modifier is only added for
        alphabets. To satisfy the assumption, the following ensures that the presence or absence
        of shift modifier is consistent across platforms.

        Idea borrowed from: https://github.com/sxyazi/yazi/pull/174
        */
        let platform_consistent_shift = match (key.code, key.modifiers) {
            (KeyCode::Char(c), _) => c.is_ascii_uppercase(),
            (_, m) => m.contains(KeyModifiers::SHIFT),
        };
        if platform_consistent_shift {
            key.modifiers.insert(KeyModifiers::SHIFT);
        } else {
            key.modifiers.remove(KeyModifiers::SHIFT);
        }
        if self.is_help_mode() {
            self.handler_help(key)
        } else if self.is_input_buffering() {
            self.handler_buffering(key)
        } else {
            self.handler_default(key)
        }
    }

    fn handler_default(&mut self, key_event: KeyEvent) -> Control {
        match key_event.modifiers {
            KeyModifiers::NONE => match key_event.code {
                KeyCode::Char('q') => Control::Quit,
                KeyCode::Char('j') | KeyCode::Down => Control::ScrollDown,
                KeyCode::Char('k') | KeyCode::Up => Control::ScrollUp,
                KeyCode::Char('l') | KeyCode::Right => Control::ScrollRight,
                KeyCode::Char('h') | KeyCode::Left => Control::ScrollLeft,
                KeyCode::Char('g') | KeyCode::Home => Control::ScrollTop,
                KeyCode::End => Control::ScrollBottom,
                KeyCode::Char('n') => Control::ScrollToNextFound,
                KeyCode::PageDown => Control::ScrollPageDown,
                KeyCode::PageUp => Control::ScrollPageUp,
                KeyCode::Char('d') => Control::ScrollHalfPageDown,
                KeyCode::Char('u') => Control::ScrollHalfPageUp,
                KeyCode::Char(x) if "0123456789".contains(x.to_string().as_str()) => {
                    self.buffer_state = BufferState::Active(Input::new(x.to_string()));
                    self.mode = InputMode::GotoLine;
                    Control::BufferContent(Input::new(x.to_string()))
                }
                KeyCode::Char('/') => {
                    self.init_buffer(InputMode::Find);
                    Control::empty_buffer()
                }
                KeyCode::Char('&') => {
                    self.init_buffer(InputMode::Filter);
                    Control::empty_buffer()
                }
                KeyCode::Char('*') => {
                    self.init_buffer(InputMode::FilterColumns);
                    Control::empty_buffer()
                }
                KeyCode::Char('-') => {
                    self.init_buffer(InputMode::Option);
                    Control::empty_buffer()
                }
                KeyCode::Char('f') => {
                    self.init_buffer(InputMode::FreezeColumns);
                    Control::empty_buffer()
                }
                KeyCode::Enter => Control::Select,
                KeyCode::Tab => Control::ToggleSelectionType,
                KeyCode::Char('>') => Control::IncreaseWidth,
                KeyCode::Char('<') => Control::DecreaseWidth,
                KeyCode::Char('r') => Control::Reset,
                KeyCode::Char('?') => Control::Help,
                KeyCode::Char('#') => Control::FindLikeCell,
                KeyCode::Char('@') => Control::FilterLikeCell,
                KeyCode::Char('y') => Control::CopySelection,
                KeyCode::Char('m') => Control::ToggleMark,
                _ => Control::Nothing,
            },
            KeyModifiers::SHIFT => match key_event.code {
                KeyCode::Char('G') | KeyCode::End => Control::ScrollBottom,
                KeyCode::Char('N') => Control::ScrollToPrevFound,
                KeyCode::Char('H') => Control::Help,
                KeyCode::Char('J') | KeyCode::Down => Control::ToggleSort,
                KeyCode::Char('M') => Control::ResetMarks,
                _ => Control::Nothing,
            },
            KeyModifiers::CONTROL => match key_event.code {
                KeyCode::Char('f') => Control::ScrollPageDown,
                KeyCode::Char('b') => Control::ScrollPageUp,
                KeyCode::Char('d') => Control::ScrollHalfPageDown,
                KeyCode::Char('u') => Control::ScrollHalfPageUp,
                KeyCode::Char('h') => Control::ScrollPageLeft,
                KeyCode::Char('l') => Control::ScrollPageRight,
                KeyCode::Left => Control::ScrollLeftMost,
                KeyCode::Right => Control::ScrollRightMost,
                KeyCode::Char('j') => Control::ToggleNaturalSort,
                KeyCode::Char('e') => Control::SelectMarks,
                _ => Control::Nothing,
            },
            _ => Control::Nothing,
        }
    }

    fn handler_buffering(&mut self, key_event: KeyEvent) -> Control {
        let input = match &mut self.buffer_state {
            BufferState::Active(input) => input,
            BufferState::Inactive => return Control::Nothing,
        };
        if self.mode == InputMode::Option {
            return self.handler_buffering_option_mode(key_event);
        }
        match key_event.code {
            KeyCode::Esc => {
                self.reset_buffer();
                Control::BufferReset
            }
            KeyCode::Char('g' | 'G') | KeyCode::Enter if self.mode == InputMode::GotoLine => {
                self.buffer_history_container.set(self.mode, input.value());
                let goto_line = match &self.buffer_state {
                    BufferState::Active(input) => input.value().parse::<usize>().ok(),
                    BufferState::Inactive => None,
                };
                let res = if let Some(n) = goto_line {
                    Control::ScrollTo(n)
                } else {
                    Control::BufferReset
                };
                self.reset_buffer();
                res
            }
            KeyCode::Up => {
                let mode = match self.mode {
                    InputMode::Filter => InputMode::Find,
                    _ => self.mode,
                };
                if let Some(buf) = self.buffer_history_container.prev(mode) {
                    self.buffer_state = BufferState::Active(Input::new(buf.clone()));
                    Control::BufferContent(Input::new(buf))
                } else {
                    Control::Nothing
                }
            }
            KeyCode::Down => {
                let mode = match self.mode {
                    InputMode::Filter => InputMode::Find,
                    _ => self.mode,
                };
                if let Some(buf) = self.buffer_history_container.next(mode) {
                    self.buffer_state = BufferState::Active(Input::new(buf.clone()));
                    Control::BufferContent(Input::new(buf))
                } else {
                    self.buffer_state = BufferState::Active(Input::default());
                    Control::BufferContent(Input::default())
                }
            }
            KeyCode::Enter => {
                let control;
                if input.value().is_empty() {
                    control = Control::BufferReset;
                } else if self.mode == InputMode::Find {
                    control = Control::Find(input.value().to_string());
                } else if self.mode == InputMode::Filter {
                    control = Control::Filter(input.value().to_string());
                } else if self.mode == InputMode::FilterColumns {
                    control = Control::FilterColumns(input.value().to_string());
                } else {
                    control = Control::BufferReset;
                }
                if self.mode == InputMode::Filter {
                    // Share buffer history between Find and Filter, see also KeyCode::Up
                    self.buffer_history_container
                        .set(InputMode::Find, input.value());
                } else {
                    self.buffer_history_container.set(self.mode, input.value());
                }
                self.reset_buffer();
                control
            }
            _ => {
                if input.handle_event(&Event::Key(key_event)).is_some() {
                    // Parse immediately for FreezeColumns since it should just be a number
                    let control = if self.mode == InputMode::FreezeColumns {
                        let control = if let Ok(n) = input.value().parse::<usize>() {
                            Control::FreezeColumns(n)
                        } else {
                            Control::UserError(format!("Invalid number: {}", input.value()))
                        };
                        self.reset_buffer();
                        control
                    } else {
                        Control::BufferContent(input.clone())
                    };
                    return control;
                }
                Control::Nothing
            }
        }
    }

    fn handler_buffering_option_mode(&mut self, key_event: KeyEvent) -> Control {
        match key_event.code {
            KeyCode::Esc | KeyCode::Backspace | KeyCode::Enter => {
                self.reset_buffer();
                Control::BufferReset
            }
            KeyCode::Char('S') => {
                self.reset_buffer();
                Control::ToggleLineWrap(WrapMode::Chars)
            }
            KeyCode::Char('W') | KeyCode::Char('w') => {
                self.reset_buffer();
                Control::ToggleLineWrap(WrapMode::Words)
            }
            KeyCode::Char(x) => {
                self.reset_buffer();
                Control::UnknownOption(x.to_string())
            }
            _ => Control::Nothing,
        }
    }

    fn handler_help(&mut self, key_event: KeyEvent) -> Control {
        match key_event.code {
            KeyCode::Char('q') | KeyCode::Esc => Control::Quit,
            KeyCode::Char('j') | KeyCode::Down => Control::ScrollDown,
            KeyCode::Char('k') | KeyCode::Up => Control::ScrollUp,
            _ => Control::Nothing,
        }
    }

    fn is_input_buffering(&self) -> bool {
        matches!(self.buffer_state, BufferState::Active(_))
    }

    fn init_buffer(&mut self, mode: InputMode) {
        self.buffer_state = BufferState::Active(Input::default());
        self.mode = mode;
    }

    fn reset_buffer(&mut self) {
        self.buffer_state = BufferState::Inactive;
        self.buffer_history_container.reset_cursors();
        self.mode = InputMode::Default;
    }

    pub fn mode(&self) -> InputMode {
        self.mode
    }

    pub fn enter_help_mode(&mut self) {
        self.mode = InputMode::Help;
    }

    pub fn exit_help_mode(&mut self) {
        self.mode = InputMode::Default;
    }

    fn is_help_mode(&mut self) -> bool {
        self.mode == InputMode::Help
    }
}
```

## File: `src/io.rs`
```rust
use std::fs::{File, OpenOptions};
use std::io::{Read, Seek, SeekFrom, Write};
use std::sync::Arc;
use std::sync::atomic::{AtomicBool, Ordering};
use tempfile::NamedTempFile;

use crate::csv::{CsvBaseConfig, CsvConfig, CsvlensRecordIterator};
use crate::errors::{CsvlensError, CsvlensResult};

pub struct SeekableFile {
    filename: Option<String>,
    inner_file: Option<NamedTempFile>,
    stream_active: Option<Arc<AtomicBool>>,
}

impl SeekableFile {
    pub fn new(
        maybe_filename: &Option<String>,
        no_streaming_stdin: bool,
    ) -> CsvlensResult<SeekableFile> {
        let inner_file = NamedTempFile::new()?;
        let inner_file_res;
        let mut stream_active = None;

        let mut stream_to_inner_file = || {
            let inner_path = inner_file.path().to_owned();

            // Thread to stream stdin to inner file
            let stream_active_flag = Arc::new(AtomicBool::new(true));
            let _stream_active_flag = stream_active_flag.clone();
            let _inner_path = inner_path.clone();
            std::thread::spawn(move || {
                let mut stdin = std::io::stdin();
                Self::chunked_copy_to_path(&mut stdin, _inner_path).unwrap();
                _stream_active_flag.store(false, Ordering::Relaxed);
            });
            stream_active = Some(stream_active_flag);

            // Thread to wait for the headers to be available. This is needed because once App is
            // started, it will immediately read the headers from the file. For slowly streaming
            // inputs, the headers might not be available yet.
            let _stream_active = stream_active.clone();
            let handle = std::thread::spawn(move || {
                // The delimiter here can be just an approximation since we just need to make sure
                // the header row as a whole is ready. Set no_headers: true to yield the header row
                // as a record.
                let base_config = CsvBaseConfig::new(b',', true);
                let path = inner_path.to_str().unwrap();
                let config = CsvConfig::new(path, _stream_active, base_config);
                let mut record_iterator = CsvlensRecordIterator::new(Arc::new(config)).unwrap();
                record_iterator.next();
            });
            handle.join().unwrap();
        };

        let copy_to_inner_file = || {
            let inner_path = inner_file.path().to_owned();
            let mut stdin = std::io::stdin();
            Self::chunked_copy_to_path(&mut stdin, inner_path).unwrap();
        };

        let mut prepare_inner_file = || {
            if no_streaming_stdin {
                copy_to_inner_file()
            } else {
                stream_to_inner_file()
            }
        };

        if let Some(filename) = maybe_filename {
            let mut f = File::open(filename).map_err(|e| match e.kind() {
                std::io::ErrorKind::NotFound => CsvlensError::FileNotFound(filename.clone()),
                _ => e.into(),
            })?;
            // If not seekable, it most likely is due to process substitution using
            // pipe - write out to a temp file to make it seekable
            if f.seek(SeekFrom::Start(0)).is_err() {
                prepare_inner_file();
                inner_file_res = Some(inner_file);
            } else {
                inner_file_res = None;
            }
        } else {
            // Handle input from stdin
            prepare_inner_file();
            inner_file_res = Some(inner_file);
        }

        Ok(SeekableFile {
            filename: maybe_filename.clone(),
            inner_file: inner_file_res,
            stream_active,
        })
    }

    pub fn filename(&self) -> &str {
        if let Some(f) = &self.inner_file {
            f.path().to_str().unwrap()
        } else {
            // If data is from stdin, then inner_file must be there
            self.filename.as_ref().unwrap()
        }
    }

    pub fn stream_active(&self) -> &Option<Arc<AtomicBool>> {
        &self.stream_active
    }

    fn chunked_copy<R: Read, W: Write>(source: &mut R, dest: &mut W) -> CsvlensResult<usize> {
        let mut total_copied = 0;
        let mut buffer = vec![0; 1_000_000];
        loop {
            let n = source.read(&mut buffer)?;
            if n == 0 {
                break;
            }
            let n_written = dest.write(&buffer[..n])?;
            total_copied += n_written;
        }
        Ok(total_copied)
    }

    fn chunked_copy_to_path<R: Read>(
        source: &mut R,
        path: impl AsRef<std::path::Path>,
    ) -> CsvlensResult<usize> {
        let mut file = OpenOptions::new()
            .write(true)
            .create(true)
            .truncate(true)
            .open(path)?;

        SeekableFile::chunked_copy(source, &mut file)
    }
}
```

## File: `src/lib.rs`
```rust
//! # csvlens
//!
//! This crate allows you to use csvlens as a library.
//!
//! In your `Cargo.toml`, add the following:
//!
//! ```toml
//! [dependencies]
//! csvlens = { version = "0.11.0", default-features = false, features = ["clipboard"] }    
//! ```
//!
//! ## Example
//!
//! ```rust,no_run
//! use csvlens::run_csvlens;
//!
//! let out = run_csvlens(&["/path/to/your.csv"]).unwrap();
//! if let Some(selected_cell) = out {
//!     println!("Selected: {}", selected_cell);
//! }
//! ```
//!
//! ## Library Usage with options
//!
//! ```ignore
//! use csvlens::{run_csvlens_with_options, CsvlensOptions};
//!
//! let options = CsvlensOptions {
//!     filename: "/path/to/your.csv".to_string(),
//!     delimiter: Some("|".to_string()),
//!     ignore_case: true,
//!     debug: true,
//!     ..Default::default()
//! };
//! let out = run_csvlens_with_options(options).unwrap();
//! if let Some(selected_cell) = out {
//!     println!("Selected: {}", selected_cell);
//! }
//! ```
mod app;
mod columns_filter;
mod common;
mod csv;
mod delimiter;
pub mod errors;
mod find;
mod help;
mod history;
mod input;
mod io;
mod runner;
mod sort;
mod theme;
mod ui;
mod util;
mod view;
mod watch;
mod wrap;

pub use app::WrapMode;
pub use runner::CsvlensOptions;
pub use runner::run_csvlens;
pub use runner::run_csvlens_with_options;

#[cfg(any(test, feature = "bench"))]
pub mod bench_api {
    pub use crate::csv::{CsvBaseConfig, CsvConfig, CsvlensRecordIterator};
}
```

## File: `src/main.rs`
```rust
use csvlens::run_csvlens;

fn main() {
    let args_itr = std::env::args_os().skip(1);
    match run_csvlens(args_itr) {
        Err(e) => {
            println!("{e:#}");
            std::process::exit(1);
        }
        Ok(Some(selection)) => {
            println!("{selection}");
        }
        _ => {}
    }
}
```

## File: `src/runner.rs`
```rust
use crate::app::{App, WrapMode};
use crate::delimiter::Delimiter;
use crate::errors::CsvlensResult;

#[cfg(feature = "cli")]
use clap::ArgGroup;
#[cfg(feature = "cli")]
use clap::Parser;
#[cfg(feature = "cli")]
use clap::ValueEnum;
use crossterm::execute;
use crossterm::terminal::{
    EnterAlternateScreen, LeaveAlternateScreen, disable_raw_mode, enable_raw_mode,
};
use ratatui::Terminal;
use ratatui::backend::CrosstermBackend;
use std::ffi::OsString;
use std::io::LineWriter;
use std::panic;
use std::thread::panicking;

#[cfg(feature = "cli")]
#[derive(Debug, Clone, ValueEnum)]
#[clap(rename_all = "lower")]
pub enum ClapWrapMode {
    Chars,
    Words,
}

#[cfg(feature = "cli")]
#[derive(Parser, Debug)]
#[command(version)]
#[command(group(ArgGroup::new("wrap_flags").conflicts_with("wrap")))]
#[command(styles = clap_cargo::style::CLAP_STYLING)]
struct Args {
    /// CSV filename
    filename: Option<String>,

    /// Delimiter character (comma by default) or "auto" to auto-detect the delimiter
    #[clap(short, long, value_name = "char")]
    delimiter: Option<String>,

    /// Use tab separation. Shortcut for -d '\t'.
    #[clap(short = 't', long)]
    tab_separated: bool,

    /// Use comma separation. Shortcut for -d ','.
    #[clap(short = 'c', long)]
    comma_separated: bool,

    /// Do not interpret the first row as headers.
    #[clap(long)]
    no_headers: bool,

    /// Use this regex to select columns to display by default
    ///
    /// Example: "column1|column2" matches "column1", "column2", and also column names like
    /// "column11", "column22".
    #[arg(long, value_name = "regex")]
    columns: Option<String>,

    /// Use this regex to filter rows to display by default
    ///
    /// The regex is matched against each cell in every column.
    ///
    /// Example: "value1|value2" filters rows with any cells containing "value1", "value2", or text
    /// like "my_value1" or "value234".
    #[arg(long, value_name = "regex")]
    filter: Option<String>,

    /// Use this regex to find and highlight matches by default
    ///
    /// The regex is matched against each cell in every column.
    ///
    /// Example: "value1|value2" highlights text in any cells containing "value1", "value2", or
    /// longer text like "value1_ok".
    #[arg(long, value_name = "regex")]
    find: Option<String>,

    /// Searches ignore case. Ignored if any uppercase letters are present in the search string
    #[clap(short, long)]
    ignore_case: bool,

    /// Print the value of this column to stdout for the selected row
    #[arg(long, value_name = "column_name")]
    echo_column: Option<String>,

    /// Whether to display each column in a different color
    #[arg(long, alias = "colorful", visible_alias = "colorful")]
    color_columns: bool,

    /// Show a custom prompt message in the status bar. Supports ANSI escape codes for colored or
    /// styled text.
    #[arg(long, value_name = "prompt")]
    prompt: Option<String>,

    /// Set wrapping mode
    #[arg(long, value_enum, value_name = "mode")]
    pub wrap: Option<ClapWrapMode>,

    /// Shortcut for --wrap=chars (wrap by character count)
    #[arg(short = 'S', group = "wrap_flags")]
    pub wrap_chars: bool,

    /// Shortcut for --wrap=words (wrap by word boundaries)
    #[arg(short = 'W', group = "wrap_flags")]
    pub wrap_words: bool,

    /// Auto-reload the file when it changes on disk
    #[clap(long)]
    pub auto_reload: bool,

    /// Show stats for debugging
    #[clap(long)]
    debug: bool,

    /// Disable streaming stdin (load entire input before displaying)
    #[clap(long)]
    pub no_streaming_stdin: bool,
}

#[cfg(feature = "cli")]
impl Args {
    fn get_wrap_mode(
        wrap: Option<ClapWrapMode>,
        wrap_chars: bool,
        wrap_words: bool,
    ) -> Option<WrapMode> {
        if let Some(mode) = wrap {
            return match mode {
                ClapWrapMode::Chars => Some(WrapMode::Chars),
                ClapWrapMode::Words => Some(WrapMode::Words),
            };
        } else {
            if wrap_chars {
                return Some(WrapMode::Chars);
            }
            if wrap_words {
                return Some(WrapMode::Words);
            }
        }
        None
    }
}

#[cfg(feature = "cli")]
impl From<Args> for CsvlensOptions {
    fn from(args: Args) -> Self {
        Self {
            filename: args.filename,
            delimiter: args.delimiter,
            tab_separated: args.tab_separated,
            comma_separated: args.comma_separated,
            no_headers: args.no_headers,
            columns: args.columns,
            filter: args.filter,
            find: args.find,
            ignore_case: args.ignore_case,
            echo_column: args.echo_column,
            debug: args.debug,
            freeze_cols_offset: None,
            color_columns: args.color_columns,
            prompt: args.prompt,
            wrap_mode: Args::get_wrap_mode(args.wrap, args.wrap_chars, args.wrap_words),
            auto_reload: args.auto_reload,
            no_streaming_stdin: args.no_streaming_stdin,
        }
    }
}

// Struct for library usage without clap directives
#[derive(Debug, Default)]
pub struct CsvlensOptions {
    pub filename: Option<String>,
    pub delimiter: Option<String>,
    pub tab_separated: bool,
    pub comma_separated: bool,
    pub no_headers: bool,
    pub columns: Option<String>,
    pub filter: Option<String>,
    pub find: Option<String>,
    pub ignore_case: bool,
    pub echo_column: Option<String>,
    pub debug: bool,
    pub freeze_cols_offset: Option<u64>,
    pub color_columns: bool,
    pub prompt: Option<String>,
    pub wrap_mode: Option<WrapMode>,
    pub auto_reload: bool,
    pub no_streaming_stdin: bool,
}

struct AppRunner {
    app: App,
}

impl AppRunner {
    fn new(app: App) -> AppRunner {
        let original_panic_hook = panic::take_hook();

        panic::set_hook(Box::new(move |info| {
            // Restore terminal states first so that the backtrace on panic can
            // be printed with proper line breaks
            disable_raw_mode().unwrap();
            execute!(std::io::stderr(), LeaveAlternateScreen).unwrap();
            original_panic_hook(info);
        }));

        AppRunner { app }
    }

    fn run(&mut self) -> CsvlensResult<Option<String>> {
        enable_raw_mode()?;
        let mut output = std::io::stderr();
        execute!(output, EnterAlternateScreen)?;

        let backend = CrosstermBackend::new(LineWriter::new(output));
        let mut terminal = Terminal::new(backend)?;

        self.app.main_loop(&mut terminal)
    }
}

impl Drop for AppRunner {
    fn drop(&mut self) {
        // If panicked, restoring of terminal states would have been done in the
        // panic hook. Avoid doing that twice since that would clear the printed
        // backtrace.
        if !panicking() {
            disable_raw_mode().unwrap();
            execute!(std::io::stderr(), LeaveAlternateScreen).unwrap();
        }
    }
}

/// Run csvlens with options provided in a `CsvlensOptions` struct.
///
/// On success, the result contains an optional string that is the value of the selected cell if
/// any. If csvlens exits without selecting a cell, the result is None.
///
/// Example:
///
/// ```
/// use csvlens::{run_csvlens_with_options, CsvlensOptions};
///
/// let options = CsvlensOptions {
///     filename: Some("/path/to/your.csv".to_string()),
///     ..Default::default()
/// };
/// match run_csvlens_with_options(options) {
///     Ok(Some(selected_cell)) => println!("Selected: {}", selected_cell),
///     Ok(None) => {},
///     Err(e) => eprintln!("Error: {:?}", e),
/// }
/// ```
pub fn run_csvlens_with_options(options: CsvlensOptions) -> CsvlensResult<Option<String>> {
    let show_stats = options.debug;
    let delimiter = Delimiter::from_arg(
        &options.delimiter,
        options.tab_separated,
        options.comma_separated,
    )?;

    let app = App::new(
        options.filename,
        delimiter,
        show_stats,
        options.echo_column,
        options.ignore_case,
        options.no_headers,
        options.columns,
        options.filter,
        options.find,
        options.freeze_cols_offset,
        options.color_columns,
        options.prompt,
        options.wrap_mode,
        options.auto_reload,
        options.no_streaming_stdin,
    )?;

    let mut app_runner = AppRunner::new(app);
    app_runner.run()
}

/// Run csvlens with a list of arguments. The accepted arguments are the same as the command line
/// arguments for the csvlens binary.
///
/// On success, the result contains an optional string that is the value of the selected cell if
/// any. If csvlens exits without selecting a cell, the result is None.
///
/// Example:
///
/// ```
/// use csvlens::run_csvlens;
///
/// match run_csvlens(&["/path/to/your.csv", "--delimiter", "\t"]) {
///     Ok(Some(selected_cell)) => println!("Selected: {}", selected_cell),
///     Ok(None) => {},
///     Err(e) => eprintln!("Error: {:?}", e),
/// }
/// ```
#[cfg(feature = "cli")]
pub fn run_csvlens<I, T>(args: I) -> CsvlensResult<Option<String>>
where
    I: IntoIterator<Item = T>,
    T: Into<OsString> + Clone,
{
    let mut args_items = vec![OsString::from("csvlens")];
    for item in args {
        args_items.push(item.into());
    }
    let args = Args::parse_from(args_items);
    run_csvlens_with_options(args.into())
}

#[cfg(not(feature = "cli"))]
pub fn run_csvlens<I, T>(_args: I) -> CsvlensResult<Option<String>>
where
    I: IntoIterator<Item = T>,
    T: Into<OsString> + Clone,
{
    eprintln!("Error: CLI is not enabled. Compile with the 'cli' feature to use this binary.");
    std::process::exit(1);
}
```

## File: `src/sort.rs`
```rust
use crate::csv;
use crate::errors::CsvlensResult;

use std::cmp::Ordering;
use std::fs::File;
use std::sync::Arc;
use std::sync::Mutex;
use std::thread::{self};
use std::time::Duration;
use std::time::Instant;

use arrow::array::{Array, ArrayIter};
use arrow::compute::concat;
use arrow::compute::kernels;
use arrow::datatypes::Fields;
use arrow::datatypes::Schema;
use arrow::datatypes::SchemaBuilder;

#[derive(Clone, Debug, PartialEq)]
pub enum SorterStatus {
    Running,
    Finished,
    Error(String),
}

#[derive(Clone, Copy, Debug, PartialEq)]
pub enum SortOrder {
    Ascending,
    Descending,
}

#[derive(Clone, Copy, Debug, PartialEq)]
pub enum SortType {
    Auto,
    Natural,
}

// Natural sorting comparison function
fn natural_cmp(a: &str, b: &str) -> Ordering {
    let mut a_chars = a.chars().peekable();
    let mut b_chars = b.chars().peekable();

    loop {
        // Skip leading whitespace
        while a_chars.peek().is_some_and(|c| c.is_whitespace()) {
            a_chars.next();
        }
        while b_chars.peek().is_some_and(|c| c.is_whitespace()) {
            b_chars.next();
        }

        // Check if we've reached the end of both strings
        let a_done = a_chars.peek().is_none();
        let b_done = b_chars.peek().is_none();

        if a_done && b_done {
            return Ordering::Equal;
        } else if a_done {
            return Ordering::Less;
        } else if b_done {
            return Ordering::Greater;
        }

        // Check if both characters are digits
        let a_is_digit = a_chars.peek().is_some_and(|c| c.is_ascii_digit());
        let b_is_digit = b_chars.peek().is_some_and(|c| c.is_ascii_digit());

        if a_is_digit && b_is_digit {
            // Both are digits, compare numerically
            let a_num = parse_number(&mut a_chars);
            let b_num = parse_number(&mut b_chars);

            match a_num.cmp(&b_num) {
                Ordering::Equal => continue,
                other => return other,
            }
        } else if a_is_digit {
            // Only a is digit, digits come before non-digits
            return Ordering::Less;
        } else if b_is_digit {
            // Only b is digit, digits come before non-digits
            return Ordering::Greater;
        } else {
            // Both are non-digits, compare lexicographically
            let a_char = a_chars.next().unwrap();
            let b_char = b_chars.next().unwrap();

            match a_char.cmp(&b_char) {
                Ordering::Equal => continue,
                other => return other,
            }
        }
    }
}

fn parse_number(chars: &mut std::iter::Peekable<std::str::Chars>) -> u64 {
    let mut num = 0u64;
    while let Some(&c) = chars.peek() {
        if c.is_ascii_digit() {
            num = num * 10 + c.to_digit(10).unwrap() as u64;
            chars.next();
        } else {
            break;
        }
    }
    num
}

#[derive(Debug)]
pub struct Sorter {
    pub column_index: usize,
    column_name: String,
    #[allow(dead_code)]
    sort_type: SortType,
    internal: Arc<Mutex<SorterInternalState>>,
}

impl Sorter {
    pub fn new(
        csv_config: Arc<csv::CsvConfig>,
        column_index: usize,
        column_name: String,
        sort_type: SortType,
    ) -> Self {
        let internal = SorterInternalState::init(csv_config, column_index, sort_type);
        Sorter {
            column_index,
            column_name,
            sort_type,
            internal,
        }
    }

    pub fn get_sorted_indices(
        &self,
        rows_from: u64,
        num_rows: u64,
        order: SortOrder,
    ) -> Option<Vec<u64>> {
        let m_guard = self.internal.lock().unwrap();
        if let Some(sort_result) = &m_guard.sort_result {
            let mut out = vec![];
            let index_range: Box<dyn Iterator<Item = u64>> = if order == SortOrder::Ascending {
                let start = rows_from;
                let end = start.saturating_add(num_rows);
                Box::new(start..end)
            } else {
                let end = sort_result.num_rows() as u64 - rows_from;
                let start = end.saturating_sub(num_rows);
                Box::new((start..end).rev())
            };
            for i in index_range {
                if let Some(record_index) = sort_result.record_indices.get(i as usize) {
                    out.push(*record_index as u64)
                }
            }
            return Some(out);
        }
        None
    }

    pub fn get_record_order(&self, row_index: u64, order: SortOrder) -> Option<u64> {
        let m_guard = self.internal.lock().unwrap();
        if let Some(sort_result) = &m_guard.sort_result
            && let Some(mut record_order) =
                sort_result.record_orders.get(row_index as usize).cloned()
        {
            if order == SortOrder::Descending {
                record_order = sort_result.num_rows() - record_order - 1;
            }
            return Some(record_order as u64);
        }
        None
    }

    pub fn status(&self) -> SorterStatus {
        (self.internal.lock().unwrap()).status.clone()
    }

    pub fn column_name(&self) -> &str {
        self.column_name.as_str()
    }

    pub fn sort_type(&self) -> SortType {
        self.sort_type
    }

    pub fn elapsed(&self) -> Option<Duration> {
        (self.internal.lock().unwrap()).elapsed
    }

    pub fn terminate(&self) {
        let mut m = self.internal.lock().unwrap();
        m.terminate();
    }

    #[cfg(test)]
    pub fn wait_internal(&self) {
        loop {
            if self.internal.lock().unwrap().done {
                break;
            }
            thread::sleep(core::time::Duration::from_millis(100));
        }
    }
}

impl Drop for Sorter {
    fn drop(&mut self) {
        self.terminate();
    }
}

#[derive(Debug)]
struct SortResult {
    record_indices: Vec<usize>,
    record_orders: Vec<usize>,
}

impl SortResult {
    fn num_rows(&self) -> usize {
        self.record_indices.len()
    }
}

#[derive(Debug)]
struct SorterInternalState {
    sort_result: Option<SortResult>,
    status: SorterStatus,
    should_terminate: bool,
    done: bool,
    start: Instant,
    elapsed: Option<Duration>,
}

impl SorterInternalState {
    pub fn init(
        config: Arc<csv::CsvConfig>,
        column_index: usize,
        sort_type: SortType,
    ) -> Arc<Mutex<SorterInternalState>> {
        let m_state = Arc::new(Mutex::new(SorterInternalState {
            sort_result: None,
            status: SorterStatus::Running,
            should_terminate: false,
            done: false,
            start: Instant::now(),
            elapsed: None,
        }));

        let _m = m_state.clone();
        thread::spawn(move || {
            let sort_result = if sort_type == SortType::Natural {
                // Use natural sorting
                run_natural_sort(_m.clone(), config, column_index)
            } else {
                // Use auto sorting based on type (numeric for numbers and lexicographic for strings)
                run_auto_sort(_m.clone(), config, column_index)
            };

            let mut m = _m.lock().unwrap();
            if let Ok(sort_result) = sort_result {
                m.sort_result = Some(sort_result);
                m.status = SorterStatus::Finished;
            } else {
                m.status = SorterStatus::Error(sort_result.err().unwrap().to_string());
            }
            m.done = true;
            m.elapsed = Some(m.start.elapsed());
        });

        m_state
    }

    fn infer_schema(filename: &str, delimiter: u8) -> CsvlensResult<Schema> {
        let schema = arrow::csv::infer_schema_from_files(
            &[filename.to_string()],
            delimiter,
            Some(1000),
            true,
        )?;

        // Convert integer fields to float64 to be more permissive
        let mut updated_fields = vec![];
        for field in schema.fields() {
            if field.data_type().is_integer() {
                let new_field = field
                    .as_ref()
                    .clone()
                    .with_data_type(arrow::datatypes::DataType::Float64);
                updated_fields.push(new_field);
            } else {
                updated_fields.push(field.as_ref().clone());
            }
        }
        let updated_fields = Fields::from(updated_fields);

        Ok(SchemaBuilder::from(updated_fields).finish())
    }

    fn terminate(&mut self) {
        self.should_terminate = true;
    }
}

fn run_natural_sort(
    m: Arc<Mutex<SorterInternalState>>,
    config: Arc<csv::CsvConfig>,
    column_index: usize,
) -> CsvlensResult<SortResult> {
    // Read all values and their indices
    let mut values_with_indices: Vec<(String, usize)> = Vec::new();
    let mut reader = config.new_reader()?;

    // Skip header if present
    if config.has_headers() {
        reader.headers()?;
    }

    for (index, result) in reader.records().enumerate() {
        if m.lock().unwrap().should_terminate {
            return Ok(SortResult {
                record_indices: vec![],
                record_orders: vec![],
            });
        }

        let record = result?;
        if let Some(field) = record.get(column_index) {
            values_with_indices.push((field.to_string(), index));
        } else {
            // Handle missing field
            values_with_indices.push(("".to_string(), index));
        }
    }

    // Sort using natural comparison
    values_with_indices.sort_by(|(a, _), (b, _)| natural_cmp(a, b));

    // Construct result
    let mut sorted_record_indices: Vec<usize> = Vec::with_capacity(values_with_indices.len());
    let mut record_orders: Vec<usize> = vec![0; values_with_indices.len()];

    for (order, (_, original_index)) in values_with_indices.into_iter().enumerate() {
        sorted_record_indices.push(original_index);
        record_orders[original_index] = order;
    }

    Ok(SortResult {
        record_indices: sorted_record_indices,
        record_orders,
    })
}

fn run_auto_sort(
    m: Arc<Mutex<SorterInternalState>>,
    config: Arc<csv::CsvConfig>,
    column_index: usize,
) -> CsvlensResult<SortResult> {
    let schema = SorterInternalState::infer_schema(config.filename(), config.delimiter())?;
    let file = File::open(config.filename())?;
    let arrow_csv_reader = arrow::csv::ReaderBuilder::new(Arc::new(schema))
        .with_delimiter(config.delimiter())
        .with_header(!config.no_headers())
        .with_projection(vec![column_index])
        .build(file)?;

    let mut arrs: Vec<Arc<dyn Array>> = Vec::new();
    for record_batch_result in arrow_csv_reader {
        let record_batch = record_batch_result?;
        let arr = record_batch.column(0);
        arrs.push(arr.clone());
        if m.lock().unwrap().should_terminate {
            return Ok(SortResult {
                record_indices: vec![],
                record_orders: vec![],
            });
        }
    }
    let ref_arrs = arrs
        .iter()
        .map(|arr| arr.as_ref())
        .collect::<Vec<&dyn Array>>();
    let combined_arr = concat(&ref_arrs)?;

    let sorted_indices = kernels::sort::sort_to_indices(combined_arr.as_ref(), None, None)?;

    let mut sorted_record_indices: Vec<usize> = vec![];
    let mut record_orders: Vec<usize> = vec![0; sorted_indices.len()];
    for (record_order, sorted_record_index) in ArrayIter::new(&sorted_indices).flatten().enumerate()
    {
        sorted_record_indices.push(sorted_record_index as usize);
        record_orders[sorted_record_index as usize] = record_order;
    }
    let sort_result = SortResult {
        record_indices: sorted_record_indices,
        record_orders,
    };
    Ok(sort_result)
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_natural_sort() {
        let mut items = vec!["disk1", "disk10", "disk2", "disk11"];
        items.sort_by(|a, b| natural_cmp(a, b));
        assert_eq!(items, vec!["disk1", "disk2", "disk10", "disk11"]);
    }

    #[test]
    fn test_natural_sort_mixed() {
        let mut items = vec!["file1.txt", "file10.txt", "file2.txt", "file20.txt"];
        items.sort_by(|a, b| natural_cmp(a, b));
        assert_eq!(
            items,
            vec!["file1.txt", "file2.txt", "file10.txt", "file20.txt"]
        );
    }

    #[test]
    fn test_natural_sort_with_text() {
        let mut items = vec!["chapter1", "chapter10", "chapter2", "chapter20", "appendix"];
        items.sort_by(|a, b| natural_cmp(a, b));
        assert_eq!(
            items,
            vec!["appendix", "chapter1", "chapter2", "chapter10", "chapter20"]
        );
    }

    #[test]
    fn test_simple() {
        let config = Arc::new(csv::CsvConfig::new(
            "tests/data/simple.csv",
            None,
            csv::CsvBaseConfig::new(b',', false),
        ));
        let s = Sorter::new(config, 0, "A1".to_string(), SortType::Auto);
        s.wait_internal();
        let rows = s.get_sorted_indices(0, 5, SortOrder::Ascending).unwrap();
        let expected = vec![0, 9, 99, 999, 1000];
        assert_eq!(rows, expected);
    }

    #[test]
    fn test_descending() {
        let config = Arc::new(csv::CsvConfig::new(
            "tests/data/simple.csv",
            None,
            csv::CsvBaseConfig::new(b',', false),
        ));
        let s = Sorter::new(config, 0, "A1".to_string(), SortType::Auto);
        s.wait_internal();
        let rows = s.get_sorted_indices(0, 5, SortOrder::Descending).unwrap();
        let expected = vec![998, 997, 996, 995, 994];
        assert_eq!(rows, expected);
    }

    #[test]
    fn test_empty() {
        let config = Arc::new(csv::CsvConfig::new(
            "tests/data/empty.csv",
            None,
            csv::CsvBaseConfig::new(b',', false),
        ));
        let s = Sorter::new(config, 1, "b".to_string(), SortType::Auto);
        s.wait_internal();
        assert_eq!(
            s.status(),
            SorterStatus::Error("Compute error: Sort not supported for data type Null".to_string())
        );
    }
}
```

## File: `src/theme.rs`
```rust
use ratatui::style::Color;
use terminal_colorsaurus::{QueryOptions, ThemeMode, theme_mode};

pub struct Theme {
    pub row_number: Color,
    pub border: Color,
    pub selected_foreground: Color,
    pub selected_background: Color,
    pub marked_foreground: Color,
    pub marked_background: Color,
    pub found: Color,
    pub found_selected_background: Color,
    pub status: Color,
    pub column_colors: [Color; 5],
}

impl Theme {
    pub fn default() -> Self {
        match theme_mode(QueryOptions::default()) {
            Ok(ThemeMode::Dark) => Theme::dark(),
            Ok(ThemeMode::Light) => Theme::light(),
            _ => Theme::dark(),
        }
    }

    pub fn dark() -> Self {
        let gutter = Color::Rgb(131, 148, 150);
        Theme {
            row_number: gutter,
            border: gutter,
            selected_foreground: Color::Rgb(192, 192, 192),
            selected_background: Color::Rgb(62, 61, 50),
            marked_foreground: Color::Rgb(220, 230, 255),
            marked_background: Color::Rgb(40, 50, 80),
            found: Color::Rgb(200, 0, 0),
            found_selected_background: Color::LightYellow,
            status: gutter,
            column_colors: [
                Color::Rgb(253, 151, 31),
                Color::Rgb(102, 217, 239),
                Color::Rgb(190, 132, 255),
                Color::Rgb(249, 38, 114),
                Color::Rgb(230, 219, 116),
            ],
        }
    }

    pub fn light() -> Self {
        let gutter = Color::Rgb(131, 148, 150);
        Theme {
            row_number: gutter,
            border: gutter,
            selected_foreground: Color::Rgb(73, 72, 62),
            selected_background: Color::Rgb(230, 227, 196),
            marked_foreground: Color::Rgb(0, 40, 80),
            marked_background: Color::Rgb(220, 235, 255),
            found: Color::Rgb(200, 0, 0),
            found_selected_background: Color::LightYellow,
            status: gutter,
            column_colors: [
                Color::Rgb(207, 112, 0),
                Color::Rgb(0, 137, 179),
                Color::Rgb(104, 77, 153),
                Color::Rgb(249, 0, 90),
                Color::Rgb(153, 143, 47),
            ],
        }
    }
}
```

## File: `src/ui.rs`
```rust
use crate::common::InputMode;
use crate::csv::Row;
use crate::find;
use crate::sort;
use crate::sort::SortOrder;
use crate::sort::SortType;
use crate::theme::Theme;
use crate::view;
use crate::view::Header;
use crate::wrap;
use ansi_to_tui::IntoText as _;
use ratatui::buffer::Buffer;
use ratatui::layout::Rect;
use ratatui::prelude::Position;
use ratatui::style::Styled;
use ratatui::style::{Modifier, Style};
use ratatui::symbols::line;
use ratatui::text::Text;
use ratatui::text::{Line, Span};
use ratatui::widgets::Clear;
use ratatui::widgets::Widget;
use ratatui::widgets::{Block, Borders, StatefulWidget};
use regex::Regex;
use tui_input::Input;

use std::cmp::{max, min};
use std::collections::HashMap;
use std::collections::HashSet;
use std::sync::Arc;
use std::time::Duration;
use std::time::Instant;

const NUM_SPACES_AFTER_LINE_NUMBER: u16 = 2;
const NUM_SPACES_BETWEEN_COLUMNS: u16 = 4;
const MAX_COLUMN_WIDTH_FRACTION: f32 = 0.3;

pub fn set_line_safe(
    buf: &mut Buffer,
    x: u16,
    y: u16,
    line: &Line<'_>,
    max_width: u16,
) -> Option<(u16, u16)> {
    if y < buf.area.bottom() {
        Some(buf.set_line(x, y, line, max_width))
    } else {
        None
    }
}

#[derive(Debug)]
pub struct ColumnWidthOverrides {
    overrides: HashMap<usize, u16>,
}

impl ColumnWidthOverrides {
    pub fn new() -> Self {
        Self {
            overrides: HashMap::new(),
        }
    }

    /// Sets the width override for the given origin column index
    pub fn set(&mut self, col_index: usize, width: u16) {
        self.overrides.insert(col_index, width);
    }

    /// Returns the width override for the given origin column index, if any
    pub fn get(&self, col_index: usize) -> Option<&u16> {
        self.overrides.get(&col_index)
    }

    /// Returns the list of origin column indices that have width overrides
    pub fn overriden_indices(&self) -> Vec<usize> {
        self.overrides.keys().copied().collect()
    }

    pub fn reset(&mut self) {
        self.overrides.clear();
    }
}

#[derive(Debug)]
pub struct CsvTable<'a> {
    header: &'a [Header],
    rows: &'a [Row],
}

impl<'a> CsvTable<'a> {
    pub fn new(header: &'a [Header], rows: &'a [Row]) -> Self {
        Self { header, rows }
    }
}

impl<'a> CsvTable<'a> {
    fn get_column_widths(
        &self,
        area_width: u16,
        overrides: &ColumnWidthOverrides,
        sorter_state: &SorterState,
    ) -> Vec<u16> {
        let mut column_widths = Vec::new();

        for h in self.header {
            let column_name = self.get_effective_column_name(h.name.as_str(), sorter_state);
            if let Some(w) = overrides.get(h.origin_index) {
                column_widths.push(*w);
                continue;
            } else {
                column_widths.push(column_name.len() as u16);
            }
        }

        let overriden_indices = overrides.overriden_indices();

        for row in self.rows {
            for (i, value) in row.fields.iter().enumerate() {
                if i >= column_widths.len() {
                    continue;
                }
                if overriden_indices.contains(&self.header.get(i).unwrap().origin_index) {
                    continue;
                }
                let v = column_widths.get_mut(i).unwrap();
                value.split('\n').for_each(|x| {
                    let value_len = x.len() as u16;
                    if *v < value_len {
                        *v = value_len;
                    }
                });
            }
        }

        // Limit maximum width for a column to make way for other columns
        let max_single_column_width = (area_width as f32 * MAX_COLUMN_WIDTH_FRACTION) as u16;
        let mut clipped_columns: Vec<(usize, u16)> = vec![];
        for (i, w) in column_widths.iter_mut().enumerate() {
            if overriden_indices.contains(&self.header.get(i).unwrap().origin_index) {
                *w = max(*w, NUM_SPACES_BETWEEN_COLUMNS);
            } else {
                *w += NUM_SPACES_BETWEEN_COLUMNS;
                if *w > max_single_column_width {
                    clipped_columns.push((i, *w));
                    *w = max_single_column_width;
                }
            }
        }

        // If clipping was too aggressive, redistribute the remaining width
        CsvTable::redistribute_widths_after_clipping(
            &mut column_widths,
            area_width,
            clipped_columns,
        );

        column_widths
    }

    fn redistribute_widths_after_clipping(
        column_widths: &mut [u16],
        area_width: u16,
        mut clipped_columns: Vec<(usize, u16)>,
    ) {
        if clipped_columns.is_empty() {
            // Nothing to adjust
            return;
        }

        let total_width: u16 = column_widths.iter().sum();
        if total_width >= area_width {
            // No need to adjust if we're already using the full width
            return;
        }

        // Greedily adjust from the narrowest column by equally distributing the remaining width. If
        // a column doesn't use the allocated adjustment, subsequent columns will get to use it.
        clipped_columns.sort_by_key(|x| x.1);

        // Subtract 1 to leave space for the right border. If not, this will be too greedy and
        // consume all the space making that border disappear.
        let mut remaining_width = area_width.saturating_sub(total_width).saturating_sub(1);

        let mut num_columns_to_adjust = clipped_columns.len();
        for (i, width_before_clipping) in clipped_columns {
            let adjustment = remaining_width / num_columns_to_adjust as u16;
            let width_after_adjustment = min(width_before_clipping, column_widths[i] + adjustment);
            let added_width = width_after_adjustment - column_widths[i];
            column_widths[i] = width_after_adjustment;
            remaining_width -= added_width;
            num_columns_to_adjust -= 1;
        }
    }

    fn get_row_heights(
        &self,
        area_height: u16,
        rows: &[Row],
        column_widths: &[u16],
        enable_line_wrap: bool,
        is_word_wrap: bool,
    ) -> Vec<u16> {
        if !enable_line_wrap {
            return rows.iter().map(|_| 1).collect();
        }
        let mut total_height = 0;
        let mut row_heights = Vec::new();
        for (i, row) in rows.iter().enumerate() {
            if total_height >= area_height {
                // Exit early if we've already filled the available height. Important since
                // LineWrapper at its current state is not particularly efficient...
                row_heights.push(1);
                continue;
            }
            for (j, content) in row.fields.iter().enumerate() {
                let num_lines = match column_widths.get(j) {
                    Some(w) => {
                        let usable_width = (*w).saturating_sub(NUM_SPACES_BETWEEN_COLUMNS);
                        if usable_width > 0 {
                            let spans = [Span::styled(content.as_str(), Style::default())];
                            let mut line_wrapper =
                                wrap::LineWrapper::new(&spans, usable_width as usize, is_word_wrap);
                            let mut num_lines = 0;
                            loop {
                                line_wrapper.next();
                                num_lines += 1;
                                if line_wrapper.finished() {
                                    break;
                                }
                            }
                            num_lines
                        } else {
                            1
                        }
                    }
                    None => 1,
                };
                if let Some(height) = row_heights.get_mut(i) {
                    if *height < num_lines {
                        *height = num_lines;
                    }
                } else {
                    row_heights.push(num_lines);
                }
            }
            total_height += row_heights[i];
        }
        row_heights
    }

    fn render_row_numbers(
        &self,
        buf: &mut Buffer,
        state: &mut CsvTableState,
        area: Rect,
        rows: &[Row],
        view_layout: &ViewLayout,
    ) {
        // Render line numbers
        let y_first_record = area.y;
        let mut y = area.y;
        for (i, row) in rows.iter().enumerate() {
            let row_num_formatted = row.record_num.to_string();
            let mut style = Style::default().fg(state.theme.row_number);
            if let Some(selection) = &state.selection
                && selection.row.is_selected(i)
            {
                style = style
                    .add_modifier(Modifier::BOLD)
                    .add_modifier(Modifier::UNDERLINED);
            }
            let span = Span::styled(row_num_formatted, style);
            buf.set_span(0, y, &span, view_layout.row_number_layout.max_length);
            y += view_layout.row_heights[i];
            if y >= area.bottom() {
                break;
            }
        }

        state.borders_state = Some(BordersState {
            x_row_separator: view_layout.row_number_layout.x_row_separator,
            y_first_record,
            x_freeze_separator: view_layout.x_freeze_separator,
        });
    }

    fn render_header_borders(&self, buf: &mut Buffer, area: Rect, theme: &Theme) -> (u16, u16) {
        let block = Block::default()
            .borders(Borders::TOP | Borders::BOTTOM)
            .border_style(Style::default().fg(theme.border));
        let height = 3;
        let area = Rect::new(0, 0, area.width, height);
        block.render(area, buf);
        // y pos of header text and next line
        (height.saturating_sub(2), height)
    }

    fn render_other_borders(&self, buf: &mut Buffer, area: Rect, state: &CsvTableState) {
        // TODO: maybe should be combined with render_header_borders() above
        // Render vertical separator
        if state.borders_state.is_none() {
            return;
        }

        let borders_state = state.borders_state.as_ref().unwrap();
        let y_first_record = borders_state.y_first_record;
        let section_width = borders_state.x_row_separator;

        if area.width < section_width {
            return;
        }

        let border_style = Style::default().fg(state.theme.border);

        // Line number separator
        let line_number_block = Block::default()
            .borders(Borders::RIGHT)
            .border_style(border_style);
        let line_number_area = Rect::new(0, y_first_record, section_width, area.height);
        line_number_block.render(line_number_area, buf);

        // Intersection with header separator
        if let Some(cell) = buf.cell_mut(Position::new(section_width - 1, y_first_record - 1)) {
            cell.set_symbol(line::HORIZONTAL_DOWN);
        }

        // Status separator at the bottom (rendered here first for the interesection)
        let block = Block::default()
            .borders(Borders::TOP)
            .border_style(border_style);
        let status_separator_area = Rect::new(0, y_first_record + area.height, area.width, 1);
        block.render(status_separator_area, buf);

        // Intersection with bottom separator
        if let Some(cell) = buf.cell_mut(Position::new(
            section_width - 1,
            y_first_record + area.height,
        )) {
            cell.set_symbol(line::HORIZONTAL_UP);
        }

        // Vertical line after last rendered column
        // TODO: refactor
        let col_ending_pos_x = state.col_ending_pos_x;
        if !state.has_more_cols_to_show() && col_ending_pos_x < area.right() {
            if let Some(cell) = buf.cell_mut(Position::new(
                col_ending_pos_x,
                y_first_record.saturating_sub(1),
            )) {
                cell.set_style(border_style)
                    .set_symbol(line::HORIZONTAL_DOWN);
            }

            for y in y_first_record..y_first_record + area.height {
                if let Some(cell) = buf.cell_mut(Position::new(col_ending_pos_x, y)) {
                    cell.set_style(border_style).set_symbol(line::VERTICAL);
                }
            }

            if let Some(cell) = buf.cell_mut(Position::new(
                col_ending_pos_x,
                y_first_record + area.height,
            )) {
                cell.set_style(border_style).set_symbol(line::HORIZONTAL_UP);
            }
        }

        // Freeze separator
        if let Some(x_freeze_separator) = borders_state.x_freeze_separator {
            // Clear highlight style made by render_row before rendering the separator
            if x_freeze_separator < area.right() {
                let x_freeze_separator_area =
                    Rect::new(x_freeze_separator, y_first_record, 1, area.height);
                Clear.render(x_freeze_separator_area, buf);

                if let Some(cell) = buf.cell_mut(Position::new(
                    x_freeze_separator,
                    y_first_record.saturating_sub(1),
                )) {
                    cell.set_style(border_style).set_symbol("╥");
                }

                for y in y_first_record..y_first_record + area.height {
                    if let Some(cell) = buf.cell_mut(Position::new(x_freeze_separator, y)) {
                        cell.set_style(border_style)
                            .set_symbol(line::DOUBLE_VERTICAL);
                    }
                }

                if let Some(cell) = buf.cell_mut(Position::new(
                    x_freeze_separator,
                    y_first_record + area.height,
                )) {
                    cell.set_style(border_style).set_symbol("╨");
                }
            }
        }
    }

    fn get_effective_column_name(&self, column_name: &str, sorter_state: &SorterState) -> String {
        if let SorterState::Enabled(info) = sorter_state
            && info.status == sort::SorterStatus::Finished
            && info.column_name == column_name
        {
            let indicator = match info.order {
                SortOrder::Ascending => "▴",
                SortOrder::Descending => "▾",
            };

            let sort_type_indicator = match info.sort_type {
                SortType::Natural => "N",
                _ => "",
            };
            return format!("{} [{}{}]", column_name, indicator, sort_type_indicator);
        }
        column_name.to_string()
    }

    #[allow(clippy::too_many_arguments)]
    fn render_row(
        &self,
        buf: &mut Buffer,
        state: &mut CsvTableState,
        column_widths: &[u16],
        area: Rect,
        x: u16,
        y: u16,
        row_type: RowType,
        row: &'a [String],
        row_index: Option<usize>,
        view_layout: &ViewLayout,
        remaining_height: Option<u16>,
    ) -> u16 {
        let mut x_offset_header = x;
        let mut remaining_width = area.width.saturating_sub(x);
        // TODO: seems strange that these have to be set every row
        let mut has_more_cols_to_show = false;
        let mut col_ending_pos_x = 0;
        let mut num_cols_rendered: u64 = 0;
        let row_height = match row_type {
            RowType::Header => 1,
            RowType::Record(i) => match remaining_height {
                Some(h) => min(h, view_layout.row_heights[i]),
                None => view_layout.row_heights[i],
            },
        };
        for (col_index, (hname, &hlen)) in row.iter().zip(column_widths).enumerate() {
            if !state
                .cols_offset
                .should_filtered_column_index_be_rendered(col_index as u64)
            {
                continue;
            }
            let effective_width = min(remaining_width, hlen);
            let mut content_style = Style::default();
            if state.color_columns {
                content_style = content_style
                    .fg(state.theme.column_colors[col_index % state.theme.column_colors.len()]);
            }
            if let RowType::Header = row_type {
                content_style = content_style.add_modifier(Modifier::BOLD);
                if let Some(selection) = &state.selection
                    && selection.column.is_selected(num_cols_rendered as usize)
                {
                    content_style = content_style.add_modifier(Modifier::UNDERLINED);
                }
            }
            let is_selected = if let Some(selection) = &state.selection {
                Self::is_position_selected(selection, &row_type, num_cols_rendered)
            } else {
                false
            };
            let mut filler_style = Style::default();
            if is_selected {
                let selected_style = Style::default()
                    .fg(state.theme.selected_foreground)
                    .bg(state.theme.selected_background)
                    .add_modifier(Modifier::BOLD);
                filler_style = filler_style.patch(selected_style);
                content_style = content_style.patch(selected_style);
            }

            let is_marked = if matches!(row_type, RowType::Record(_)) {
                match (row_index, &state.marked_rows) {
                    (Some(idx), Some(marked_rows)) => marked_rows.contains(&(idx + 1)),
                    _ => false,
                }
            } else {
                false
            };

            if is_marked && !is_selected {
                let marked_style = Style::default()
                    .fg(state.theme.marked_foreground)
                    .bg(state.theme.marked_background);
                filler_style = filler_style.patch(marked_style);
                content_style = content_style.patch(marked_style);
            }

            let short_padding = match &state.selection {
                Some(selection) => !matches!(selection.selection_type(), view::SelectionType::Row),
                None => false,
            };
            let filler_style = FillerStyle {
                style: filler_style,
                short_padding,
            };

            let should_highlight_cell = |active: &FinderActiveState, content: &str| {
                // Only highlight the selected column in column selection mode. But header search is
                // always across all columns regardless of the selection mode.
                if let Some((target_column_index, _)) = active.column_index
                    && target_column_index != col_index
                    && matches!(row_type, RowType::Record(_))
                {
                    return false;
                }
                if active.is_filter && matches!(row_type, RowType::Header) {
                    return false;
                }
                active.target.is_match(content)
            };
            match &state.finder_state {
                // TODO: seems like doing a bit too much of heavy lifting of
                // checking for matches (finder's work)
                FinderState::FinderActive(active) if should_highlight_cell(active, hname) => {
                    let mut highlight_style = filler_style.style.fg(state.theme.found);
                    if let Some(found_record) = &active.found_record {
                        match found_record {
                            find::FoundEntry::Row(entry) => {
                                if let Some(row_index) = row_index
                                    && row_index == entry.row_index()
                                    && entry.column_index() == col_index
                                {
                                    highlight_style =
                                        highlight_style.bg(state.theme.found_selected_background);
                                }
                            }
                            find::FoundEntry::Header(entry) => {
                                if matches!(row_type, RowType::Header)
                                    && entry.column_index() == col_index
                                {
                                    highlight_style =
                                        highlight_style.bg(state.theme.found_selected_background);
                                }
                            }
                        }
                    }
                    let spans = CsvTable::get_highlighted_spans(
                        active,
                        hname,
                        content_style,
                        highlight_style,
                    );
                    self.set_spans(
                        buf,
                        &spans,
                        x_offset_header,
                        y,
                        effective_width,
                        row_height,
                        filler_style,
                        state.is_word_wrap,
                    );
                }
                _ => {
                    let span = Span::styled((*hname).as_str(), content_style);
                    self.set_spans(
                        buf,
                        &[span],
                        x_offset_header,
                        y,
                        effective_width,
                        row_height,
                        filler_style,
                        state.is_word_wrap,
                    );
                }
            };
            x_offset_header += hlen;
            col_ending_pos_x = x_offset_header;
            num_cols_rendered += 1;
            if remaining_width < hlen {
                has_more_cols_to_show = true;
                break;
            }
            remaining_width = remaining_width.saturating_sub(hlen);
        }
        state.num_cols_rendered = max(state.num_cols_rendered, num_cols_rendered);
        state.update_more_cols_to_show(has_more_cols_to_show);
        state.col_ending_pos_x = max(state.col_ending_pos_x, col_ending_pos_x);
        row_height
    }

    fn is_position_selected(
        selection: &view::Selection,
        row_type: &RowType,
        num_cols_rendered: u64,
    ) -> bool {
        match selection.selection_type() {
            view::SelectionType::Row => {
                if let RowType::Record(i) = *row_type {
                    selection.row.is_selected(i)
                } else {
                    false
                }
            }
            view::SelectionType::Column => {
                if let RowType::Record(_) = *row_type {
                    selection.column.is_selected(num_cols_rendered as usize)
                } else {
                    false
                }
            }
            view::SelectionType::Cell => {
                if let RowType::Record(i) = *row_type {
                    selection.row.is_selected(i)
                        && selection.column.is_selected(num_cols_rendered as usize)
                } else {
                    false
                }
            }
            _ => false,
        }
    }

    fn get_highlighted_spans(
        active: &FinderActiveState,
        hname: &'a str,
        style: Style,
        highlight_style: Style,
    ) -> Vec<Span<'a>> {
        let mut spans = Vec::new();
        let mut last = 0;

        for m in active.target.find_iter(hname) {
            let (s, e) = (m.start(), m.end());
            if s == e {
                continue;
            }
            if last < s {
                spans.push(Span::styled(&hname[last..s], style));
            }
            spans.push(Span::styled(&hname[s..e], highlight_style));
            last = e;
        }

        if last < hname.len() {
            spans.push(Span::styled(&hname[last..], style));
        }

        if spans.is_empty() {
            spans.push(Span::styled(hname, style));
        }

        spans
    }

    #[allow(clippy::too_many_arguments)]
    fn set_spans(
        &self,
        buf: &mut Buffer,
        spans: &[Span],
        x: u16,
        y: u16,
        width: u16,
        height: u16,
        filler_style: FillerStyle,
        is_word_wrap: bool,
    ) {
        const SUFFIX: &str = "…";
        const SUFFIX_LEN: u16 = 1;

        // Reserve some space before the next column (same number used in get_column_widths)
        let effective_width = width.saturating_sub(NUM_SPACES_BETWEEN_COLUMNS);

        let buffer_space = if filler_style.short_padding {
            NUM_SPACES_BETWEEN_COLUMNS / 2
        } else {
            NUM_SPACES_BETWEEN_COLUMNS
        } as usize;

        let mut line_wrapper =
            wrap::LineWrapper::new(spans, effective_width as usize, is_word_wrap);

        for offset in 0..height {
            if let Some(mut line) = line_wrapper.next() {
                // There is some content to render. Truncate with ... if there is no more vertical
                // space available.
                if offset == height - 1
                    && !line_wrapper.finished()
                    && let Some(last_span) = line.spans.pop()
                {
                    let truncate_length = last_span.width().saturating_sub(SUFFIX_LEN as usize);
                    let truncated_content: String =
                        last_span.content.chars().take(truncate_length).collect();
                    let truncated_span = Span::styled(truncated_content, last_span.style);
                    line.spans.push(truncated_span);
                    line.spans.push(Span::styled(SUFFIX, last_span.style));
                }
                let padding_width = min(
                    (effective_width as usize + buffer_space).saturating_sub(line.width()),
                    width as usize,
                );
                if padding_width > 0 {
                    line.spans
                        .push(Span::styled(" ".repeat(padding_width), filler_style.style));
                }
                set_line_safe(buf, x, y + offset, &line, width);
            } else {
                // There are extra vertical spaces that are just empty lines. Fill them with the
                // correct style.
                let mut content =
                    " ".repeat(min(effective_width as usize + buffer_space, width as usize));

                // It's possible that no spans are yielded due to insufficient remaining width.
                // Render ... in this case.
                if !line_wrapper.finished() {
                    let truncated_content: String = content
                        .chars()
                        .take(content.len().saturating_sub(1))
                        .collect();
                    content = format!("{SUFFIX}{}", truncated_content.as_str());
                }
                let span = Span::styled(content, filler_style.style);
                set_line_safe(buf, x, y + offset, &Line::from(vec![span]), width);
            }
        }
    }

    fn render_status(&self, area: Rect, buf: &mut Buffer, state: &mut CsvTableState) {
        // Content of status line (separator already plotted elsewhere)
        let style = Style::default().fg(state.theme.status);
        let mut prompt_text: Text;
        let mut content: String;
        state.cursor_xy = None;
        if let Some(msg) = &state.transient_message {
            prompt_text = Text::default();
            content = msg.to_owned();
        } else if let BufferState::Enabled(buffer_mode, input) = &state.buffer_content {
            prompt_text = Text::default();
            let get_prefix = |&input_mode| {
                let prefix = match input_mode {
                    InputMode::GotoLine => "Go to line",
                    InputMode::Find => "Find",
                    InputMode::Filter => "Filter",
                    InputMode::FilterColumns => "Columns regex",
                    InputMode::Option => "Option",
                    InputMode::FreezeColumns => "Number of columns to freeze",
                    _ => "",
                };
                if prefix.is_empty() {
                    "".to_string()
                } else {
                    format!("{prefix}: ")
                }
            };
            let prefix = get_prefix(buffer_mode);
            content = format!("{prefix}{}", input.value());
            state.cursor_xy = Some((
                area.x
                    .saturating_add(prefix.len() as u16)
                    .saturating_add(input.cursor() as u16),
                area.bottom().saturating_sub(1),
            ));
        } else {
            // User provided prompt
            prompt_text = if let Some(prompt) = &state.prompt {
                prompt.into_text().unwrap_or(Text::default())
            } else {
                Text::default()
            };
            // Filename
            if state.prompt.is_some() {
                content = "".to_string();
            } else if let Some(f) = &state.filename {
                content = f.to_string();
            } else {
                content = "stdin".to_string();
            }

            // Row / Col
            let total_str = match state.total_line_number {
                Some((total, false)) => format!("{}", total),
                Some((total, true)) => format!("{}+", total),
                _ => "?".to_owned(),
            };
            let current_row;
            if let Some(selection) = &state.selection {
                current_row = if let Some(i) = selection.row.index() {
                    self.rows.get(i as usize)
                } else {
                    self.rows.first()
                }
            } else {
                current_row = self.rows.first()
            }

            let row_num = match current_row {
                Some(row) => row.record_num.to_string(),
                _ => "-".to_owned(),
            };
            content += format!(
                " [Row {}/{}, Col {}/{}]",
                row_num,
                total_str,
                state.cols_offset.num_skip + 1,
                state.total_cols,
            )
            .as_str();

            // Finder
            if let FinderState::FinderActive(s) = &state.finder_state {
                content += format!(" {}", s.status_line()).as_str();
            }

            if let Some(stats_line) = &state.debug_stats.status_line() {
                content += format!(" {stats_line}").as_str();
            }

            // Filter columns
            if let FilterColumnsState::Enabled(info) = &state.filter_columns_state {
                content += format!(" {}", info.status_line()).as_str();
            }

            // Sorter
            if let SorterState::Enabled(info) = &state.sorter_state {
                let sorter_status_line = info.status_line();
                if !sorter_status_line.is_empty() {
                    content += format!(" {}", sorter_status_line).as_str();
                }
            }

            // Echo option
            if let Some(column_name) = &state.echo_column {
                content += format!(" [Echo {column_name} ↵]").as_str();
            }

            // Ignore case option
            if state.ignore_case {
                content += " [ignore-case]";
            }

            // Last autoreload time
            if let Some(last_autoreload_at) = &state.last_autoreload_at {
                content += format!(
                    " [Last reload: {}s ago]",
                    last_autoreload_at.elapsed().as_secs()
                )
                .as_str();
            }

            // Debug
            if !state.debug.is_empty() {
                content += format!(" (debug: {})", state.debug).as_str();
            }
        }
        prompt_text = prompt_text.set_style(style);
        prompt_text.push_span(Span::from(content));
        let prompt_area = Rect::new(area.x, area.y + 1, area.width, area.height);
        prompt_text.render(prompt_area, buf);
    }

    fn get_view_layout(&self, area: Rect, state: &mut CsvTableState, rows: &[Row]) -> ViewLayout {
        let max_row_num = rows.iter().map(|x| x.record_num).max().unwrap_or(0);
        let max_row_num_length = format!("{max_row_num}").len() as u16;
        let row_num_section_width_with_spaces =
            max_row_num_length + 2 * NUM_SPACES_AFTER_LINE_NUMBER + 1;
        let x_row_separator = max_row_num_length + NUM_SPACES_AFTER_LINE_NUMBER + 1;

        let column_widths = self.get_column_widths(
            area.width.saturating_sub(row_num_section_width_with_spaces),
            &state.column_width_overrides,
            &state.sorter_state,
        );
        let _tic = std::time::Instant::now();
        let row_heights = self.get_row_heights(
            area.height,
            self.rows,
            &column_widths,
            state.enable_line_wrap,
            state.is_word_wrap,
        );
        state.num_cols_rendered = 0;
        state.col_ending_pos_x = 0;

        let row_number_layout = RowNumberLayout {
            max_length: max_row_num_length,
            width_with_spaces: row_num_section_width_with_spaces,
            x_row_separator,
        };

        // x-position of the vertical separator if any columns are frozen
        let x_freeze_separator = if state.cols_offset.num_freeze > 0 {
            let mut x_sum = row_number_layout.x_row_separator;
            for (column_index, width) in column_widths.iter().enumerate() {
                if state.cols_offset.is_frozen(column_index as u64) {
                    x_sum += width;
                }
            }
            Some(x_sum)
        } else {
            None
        };

        ViewLayout {
            column_widths,
            row_heights,
            row_number_layout,
            x_freeze_separator,
        }
    }
}

impl StatefulWidget for CsvTable<'_> {
    type State = CsvTableState;

    fn render(self, area: Rect, buf: &mut Buffer, state: &mut Self::State) {
        // TODO: draw relative to the provided area

        if area.area() == 0 {
            return;
        }

        let status_height = 2;

        let layout = self.get_view_layout(area, state, self.rows);
        state.view_layout = Some(layout.clone());

        let (y_header, y_first_record) = self.render_header_borders(buf, area, &state.theme);

        // row area: including row numbers and row content
        let rows_area = Rect::new(
            area.x,
            y_first_record,
            area.width,
            area.height
                .saturating_sub(y_first_record)
                .saturating_sub(status_height),
        );

        self.render_row_numbers(buf, state, rows_area, self.rows, &layout);
        let row_num_section_width = layout.row_number_layout.width_with_spaces;

        state.reset_more_cols_to_show();
        self.render_row(
            buf,
            state,
            &layout.column_widths,
            rows_area,
            row_num_section_width,
            y_header,
            RowType::Header,
            &self
                .header
                .iter()
                .map(|h| self.get_effective_column_name(h.name.as_str(), &state.sorter_state))
                .collect::<Vec<String>>(),
            None,
            &layout,
            None,
        );

        let mut remaining_height = rows_area.height;
        let mut y_offset = y_first_record;
        for (i, row) in self.rows.iter().enumerate() {
            let rendered_height = self.render_row(
                buf,
                state,
                &layout.column_widths,
                rows_area,
                row_num_section_width,
                y_offset,
                RowType::Record(i),
                &row.fields,
                Some(row.record_num - 1),
                &layout,
                Some(remaining_height),
            );
            remaining_height = remaining_height.saturating_sub(rendered_height);
            y_offset += rendered_height;
            if y_offset >= rows_area.bottom() {
                break;
            }
        }

        let status_area = Rect::new(
            area.x,
            area.bottom().saturating_sub(status_height),
            area.width,
            status_height,
        );
        self.render_status(status_area, buf, state);

        self.render_other_borders(buf, rows_area, state);
    }
}

pub enum RowType {
    /// Header row
    Header,
    /// Regular row. Contains the row index (not the record number) and the row itself.
    Record(usize),
}

/// Style to use for the fillers (spaces and elipses) between columns
#[derive(Clone, Copy)]
struct FillerStyle {
    style: Style,
    short_padding: bool,
}

#[derive(Debug, Clone)]
pub struct RowNumberLayout {
    pub max_length: u16,
    pub width_with_spaces: u16,
    pub x_row_separator: u16,
}

#[derive(Debug, Clone)]
pub struct ViewLayout {
    pub column_widths: Vec<u16>,
    pub row_heights: Vec<u16>,
    pub row_number_layout: RowNumberLayout,
    pub x_freeze_separator: Option<u16>,
}

impl ViewLayout {
    pub fn num_rows_renderable(&self, frame_height: u16) -> usize {
        let mut out = 0;
        let mut remaining = frame_height;
        for h in &self.row_heights {
            if *h > remaining {
                if remaining > 0 {
                    // Include partially rendered row
                    out += 1;
                }
                break;
            }
            out += 1;
            remaining -= h;
        }
        out
    }
}

pub enum BufferState {
    Disabled,
    Enabled(InputMode, Input),
}

pub enum FinderState {
    FinderInactive,
    FinderActive(FinderActiveState),
}

impl FinderState {
    pub fn from_finder(finder: &find::Finder, rows_view: &view::RowsView) -> FinderState {
        let active_state = FinderActiveState::new(finder, rows_view);
        FinderState::FinderActive(active_state)
    }
}

pub struct FinderActiveState {
    find_complete: bool,
    total_found: u64,
    cursor: Option<find::FinderCursor>,
    target: Regex,
    column_index: Option<(usize, String)>,
    found_record: Option<find::FoundEntry>,
    selected_offset: Option<u64>,
    is_filter: bool,
    header_has_match: bool,
}

impl FinderActiveState {
    pub fn new(finder: &find::Finder, rows_view: &view::RowsView) -> Self {
        let header_has_match = finder.header_has_match();
        let total_count = finder.count() + if header_has_match { 1 } else { 0 };
        FinderActiveState {
            find_complete: finder.done(),
            total_found: total_count as u64,
            cursor: finder.cursor(),
            target: finder.target(),
            column_index: finder
                .column_index()
                .map(|i| (i, rows_view.get_column_name_from_local_index(i))),
            found_record: finder.current(),
            selected_offset: rows_view.selected_offset(),
            is_filter: rows_view.is_filter(),
            header_has_match,
        }
    }

    fn status_line(&self) -> String {
        let plus_marker;
        let line;
        if self.total_found == 0 {
            if self.find_complete {
                line = "Not found".to_owned();
            } else {
                line = "Finding...".to_owned();
            }
        } else {
            if self.find_complete {
                plus_marker = "";
            } else {
                plus_marker = "+";
            }
            let cursor_str;
            if self.is_filter {
                if let Some(i) = self.selected_offset {
                    cursor_str = i.saturating_add(1).to_string();
                } else {
                    cursor_str = "-".to_owned();
                }
            } else if let Some(cursor) = &self.cursor {
                cursor_str = match cursor.row {
                    find::RowPos::Row(i) => (i
                        .saturating_add(1)
                        .saturating_add(if self.header_has_match { 1 } else { 0 }))
                    .to_string(),
                    find::RowPos::Header => "1".to_string(),
                };
            } else {
                cursor_str = "-".to_owned();
            }
            line = format!("{cursor_str}/{}{plus_marker}", self.total_found);
        }
        let action = if self.is_filter { "Filter" } else { "Find" };
        let target_column = self
            .column_index
            .as_ref()
            .map(|(_, name)| format!(" in {}", name))
            .unwrap_or_default();
        format!("[{action} \"{}\"{target_column}: {line}]", self.target)
    }
}

pub enum FilterColumnsState {
    Disabled,
    Enabled(FilterColumnsInfo),
}

impl FilterColumnsState {
    pub fn from_rows_view(rows_view: &view::RowsView) -> Self {
        if let Some(columns_filter) = rows_view.columns_filter() {
            Self::Enabled(FilterColumnsInfo {
                pattern: columns_filter.pattern(),
                shown: columns_filter.num_filtered(),
                total: columns_filter.num_original(),
                disabled_because_no_match: columns_filter.disabled_because_no_match(),
            })
        } else {
            Self::Disabled
        }
    }
}

pub struct FilterColumnsInfo {
    pattern: Regex,
    shown: usize,
    total: usize,
    disabled_because_no_match: bool,
}

impl FilterColumnsInfo {
    fn status_line(&self) -> String {
        let mut line;
        line = format!("[Filter \"{}\": ", self.pattern);
        if self.disabled_because_no_match {
            line += "no match, showing all columns]";
        } else {
            line += format!("{}/{} cols]", self.shown, self.total).as_str();
        }
        line
    }
}

enum SorterState {
    Disabled,
    Enabled(SorterInfo),
}

impl SorterState {
    fn from_sorter(sorter: &sort::Sorter, sort_order: SortOrder) -> Self {
        Self::Enabled(SorterInfo {
            status: sorter.status(),
            column_name: sorter.column_name().to_string(),
            order: sort_order,
            sort_type: sorter.sort_type(),
        })
    }
}

struct SorterInfo {
    status: sort::SorterStatus,
    column_name: String,
    order: SortOrder,
    sort_type: sort::SortType,
}

impl SorterInfo {
    fn status_line(&self) -> String {
        let sort_type_str = match self.sort_type {
            sort::SortType::Natural => "natural",
            sort::SortType::Auto => "auto based on type",
        };
        let prefix = format!("[Sorting by {} ({})", self.column_name, sort_type_str);
        match &self.status {
            sort::SorterStatus::Running => format!("{prefix}...]").to_string(),
            sort::SorterStatus::Error(error_msg) => {
                format!("{} failed: {}]", prefix, error_msg).to_string()
            }
            _ => "".to_string(),
        }
    }
}

struct BordersState {
    x_row_separator: u16,
    y_first_record: u16,
    x_freeze_separator: Option<u16>,
}

pub struct DebugStats {
    show_stats: bool,
    rows_view_stats: Option<crate::view::PerfStats>,
    finder_elapsed: Option<Duration>,
    sorter_elapsed: Option<Duration>,
    render_elapsed: Option<Duration>,
}

impl DebugStats {
    pub fn new() -> Self {
        DebugStats {
            show_stats: false,
            rows_view_stats: None,
            finder_elapsed: None,
            sorter_elapsed: None,
            render_elapsed: None,
        }
    }

    pub fn show_stats(&mut self, show: bool) {
        self.show_stats = show;
    }

    pub fn rows_view_perf(&mut self, stats: Option<crate::view::PerfStats>) {
        self.rows_view_stats = stats;
    }

    pub fn finder_elapsed(&mut self, elapsed: Option<Duration>) {
        self.finder_elapsed = elapsed;
    }

    pub fn sorter_elapsed(&mut self, elapsed: Option<Duration>) {
        self.sorter_elapsed = elapsed;
    }

    pub fn render_elapsed(&mut self, elapsed: Option<Duration>) {
        self.render_elapsed = elapsed;
    }

    pub fn status_line(&self) -> Option<String> {
        if !self.show_stats {
            return None;
        }
        let mut line = "[".to_string();
        if let Some(stats) = &self.rows_view_stats {
            line += format!(
                "rows:{:.3}ms pos:{}us npos:{} seek:{} parse:{}",
                stats.elapsed.as_micros() as f64 / 1000.0,
                stats
                    .reader_stats
                    .pos_table_elapsed
                    .as_ref()
                    .map_or(0, |e| e.as_micros()),
                stats.reader_stats.pos_table_entry,
                stats.reader_stats.num_seek,
                stats.reader_stats.num_parsed_record
            )
            .as_str();
        }
        if let Some(elapsed) = self.finder_elapsed {
            line += format!(" finder:{:.3}ms", elapsed.as_micros() as f64 / 1000.0).as_str();
        }
        if let Some(elapsed) = self.sorter_elapsed {
            line += format!(" sorter:{:.3}ms", elapsed.as_micros() as f64 / 1000.0).as_str();
        }
        if let Some(elapsed) = self.render_elapsed {
            line += format!(" render:{:.3}ms", elapsed.as_micros() as f64 / 1000.0).as_str();
        }
        line += "]";
        Some(line)
    }
}

pub struct CsvTableState {
    // TODO: types appropriate?
    pub rows_offset: u64,
    pub cols_offset: view::ColumnsOffset,
    pub num_cols_rendered: u64,
    pub more_cols_to_show: Option<bool>,
    filename: Option<String>,
    total_line_number: Option<(usize, bool)>,
    total_cols: usize,
    pub debug_stats: DebugStats,
    buffer_content: BufferState,
    pub finder_state: FinderState,
    pub filter_columns_state: FilterColumnsState,
    sorter_state: SorterState,
    borders_state: Option<BordersState>,
    // TODO: should probably be with BordersState
    col_ending_pos_x: u16,
    pub selection: Option<view::Selection>,
    pub marked_rows: Option<HashSet<usize>>,
    pub transient_message: Option<String>,
    pub echo_column: Option<String>,
    pub ignore_case: bool,
    pub view_layout: Option<ViewLayout>,
    pub enable_line_wrap: bool,
    pub is_word_wrap: bool,
    pub column_width_overrides: ColumnWidthOverrides,
    pub cursor_xy: Option<(u16, u16)>,
    pub theme: Theme,
    pub color_columns: bool,
    pub prompt: Option<String>,
    pub last_autoreload_at: Option<Instant>,
    pub debug: String,
}

impl CsvTableState {
    pub fn new(
        filename: Option<String>,
        total_cols: usize,
        echo_column: &Option<String>,
        ignore_case: bool,
        color_columns: bool,
        prompt: Option<String>,
    ) -> Self {
        Self {
            rows_offset: 0,
            cols_offset: view::ColumnsOffset::default(),
            num_cols_rendered: 0,
            more_cols_to_show: None,
            filename,
            total_line_number: None,
            total_cols,
            debug_stats: DebugStats::new(),
            buffer_content: BufferState::Disabled,
            finder_state: FinderState::FinderInactive,
            filter_columns_state: FilterColumnsState::Disabled,
            sorter_state: SorterState::Disabled,
            borders_state: None,
            col_ending_pos_x: 0,
            selection: None,
            marked_rows: None,
            transient_message: None,
            echo_column: echo_column.clone(),
            ignore_case,
            view_layout: None,
            enable_line_wrap: false,
            is_word_wrap: false,
            column_width_overrides: ColumnWidthOverrides::new(),
            cursor_xy: None,
            theme: Theme::default(),
            color_columns,
            prompt,
            last_autoreload_at: None,
            debug: "".into(),
        }
    }

    pub fn set_rows_offset(&mut self, offset: u64) {
        self.rows_offset = offset;
    }

    pub fn set_cols_offset(&mut self, offset: view::ColumnsOffset) {
        self.cols_offset = offset;
    }

    fn reset_more_cols_to_show(&mut self) {
        self.more_cols_to_show = None;
    }

    fn update_more_cols_to_show(&mut self, value: bool) {
        // If any rows have more columns to show, keep it that way
        if let Some(current) = self.more_cols_to_show {
            self.more_cols_to_show = Some(current || value);
        } else {
            self.more_cols_to_show = Some(value);
        }
    }

    pub fn has_more_cols_to_show(&self) -> bool {
        self.more_cols_to_show.is_none_or(|v| v)
    }

    pub fn set_total_line_number(&mut self, n: usize, is_approx: bool) {
        self.total_line_number = Some((n, is_approx));
    }

    pub fn set_total_cols(&mut self, n: usize) {
        self.total_cols = n;
    }

    pub fn set_buffer(&mut self, mode: InputMode, input: Input) {
        self.buffer_content = BufferState::Enabled(mode, input);
    }

    pub fn reset_buffer(&mut self) {
        self.buffer_content = BufferState::Disabled;
    }

    pub fn line_number_and_spaces_width(&self) -> u16 {
        self.borders_state
            .as_ref()
            .map_or(0, |bs| bs.x_row_separator)
            + NUM_SPACES_AFTER_LINE_NUMBER
    }

    pub fn update_sorter(&mut self, sorter: &Option<Arc<sort::Sorter>>, sort_order: SortOrder) {
        if let Some(s) = sorter {
            self.sorter_state = SorterState::from_sorter(s.as_ref(), sort_order);
        } else {
            self.sorter_state = SorterState::Disabled;
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    use crate::sort::{SortType, SorterStatus};

    #[test]
    fn test_sorter_info_status_line() {
        let info = SorterInfo {
            status: SorterStatus::Running,
            column_name: "test_column".to_string(),
            order: SortOrder::Ascending,
            sort_type: SortType::Natural,
        };

        let status_line = info.status_line();
        assert!(status_line.contains("Sorting by test_column (natural)"));

        let info_lex = SorterInfo {
            status: SorterStatus::Running,
            column_name: "test_column".to_string(),
            order: SortOrder::Ascending,
            sort_type: SortType::Auto,
        };

        let status_line_lex = info_lex.status_line();
        assert!(status_line_lex.contains("Sorting by test_column (auto based on type)"));
    }
}
```

## File: `src/view.rs`
```rust
use crate::columns_filter::ColumnsFilter;
use crate::csv::{CsvLensReader, Row};
use crate::errors::CsvlensResult;
use crate::find;
use crate::input::Control;
use crate::sort::{SortOrder, Sorter};

use std::cmp::min;
use std::collections::HashSet;
use std::sync::Arc;
use std::time::{Duration, Instant};

struct RowsFilter {
    indices: Vec<u64>,
    total: usize,
    max_index: Option<u64>,
}

impl RowsFilter {
    fn new(finder: &find::Finder, rows_from: u64, num_rows: u64) -> RowsFilter {
        let (total, max_index) = finder.count_and_max_row_index();
        let indices = finder.get_subset_found(rows_from as usize, num_rows as usize);
        RowsFilter {
            indices,
            total,
            max_index,
        }
    }
}

pub struct MarkToggleResult {
    pub record_num: usize,
    pub marked: bool,
}

#[derive(Clone)]
pub struct SelectionDimension {
    index: Option<u64>,
    pub bound: u64,
    last_selected: Option<u64>,
}

impl SelectionDimension {
    /// Create a new SelectionDimension
    pub fn new(index: Option<u64>, bound: u64) -> Self {
        Self {
            index,
            bound,
            last_selected: None,
        }
    }

    /// The currently selected index
    ///
    /// This index is dumb as in it is always between 0 and bound - 1 and
    /// has nothing to do with the actual record number in the data.
    pub fn index(&self) -> Option<u64> {
        self.index
    }

    /// Set selected to the given index and adjust it to be within bounds
    pub fn set_index(&mut self, index: u64) {
        self.index = Some(min(index, self.bound.saturating_sub(1)));
        self.last_selected = Some(index);
    }

    /// Unset the selected index
    pub fn unset_index(&mut self) {
        self.index = None;
    }

    /// Set the maximum allowed value for for index
    pub fn set_bound(&mut self, bound: u64) {
        self.bound = bound;
        if let Some(i) = self.index {
            self.set_index(i);
        }
    }

    /// Increase selected index by 1. Does nothing if nothing is currently selected.
    pub fn select_next(&mut self) {
        if let Some(i) = self.index() {
            self.set_index(i.saturating_add(1));
        };
    }

    /// Decrease selected index by 1. Does nothing if nothing is currently selected.
    pub fn select_previous(&mut self) {
        if let Some(i) = self.index() {
            self.set_index(i.saturating_sub(1));
        };
    }

    /// Select the first index. Does nothing if nothing is currently selected.
    pub fn select_first(&mut self) {
        if self.index.is_some() {
            self.set_index(0);
        }
    }

    /// Select the last index. Does nothing if nothing is currently selected.
    pub fn select_last(&mut self) {
        if self.index.is_some() {
            self.set_index(self.bound.saturating_sub(1))
        }
    }

    /// Whether the given index is currently selected
    pub fn is_selected(&self, i: usize) -> bool {
        if let Some(selected) = self.index {
            return selected == i as u64;
        }
        false
    }

    /// The last selected index even if the current selection is None
    pub fn last_selected(&self) -> Option<u64> {
        self.last_selected
    }
}

pub enum SelectionType {
    Row,
    Column,
    Cell,
    None,
}

#[derive(Clone)]
pub struct Selection {
    pub row: SelectionDimension,
    pub column: SelectionDimension,
}

impl Selection {
    pub fn default(row_bound: u64) -> Self {
        Selection {
            row: SelectionDimension::new(Some(0), row_bound),
            column: SelectionDimension::new(None, 0),
        }
    }

    pub fn selection_type(&self) -> SelectionType {
        if self.row.index.is_some() && self.column.index.is_some() {
            SelectionType::Cell
        } else if self.row.index.is_some() {
            SelectionType::Row
        } else if self.column.index.is_some() {
            SelectionType::Column
        } else {
            SelectionType::None
        }
    }

    fn set_selection_type(&mut self, selection_type: SelectionType) {
        let target_row_index = self.row.last_selected().unwrap_or(0);
        let target_column_index = self.column.last_selected().unwrap_or(0);

        match selection_type {
            SelectionType::Row => {
                self.row.set_index(target_row_index);
                self.column.unset_index();
            }
            SelectionType::Column => {
                self.row.unset_index();
                self.column.set_index(target_column_index);
            }
            SelectionType::Cell => {
                self.row.set_index(target_row_index);
                self.column.set_index(target_column_index);
            }
            SelectionType::None => {
                self.row.unset_index();
                self.column.unset_index();
            }
        }
    }

    pub fn toggle_selection_type(&mut self) {
        let selection_type = self.selection_type();
        match selection_type {
            SelectionType::Row => self.set_selection_type(SelectionType::Column),
            SelectionType::Column => self.set_selection_type(SelectionType::Cell),
            SelectionType::Cell => self.set_selection_type(SelectionType::Row), // for now don't allow toggling to None
            SelectionType::None => self.set_selection_type(SelectionType::Row),
        }
    }
}

#[derive(Debug)]
pub struct Header {
    pub name: String,
    pub origin_index: usize,
}

#[derive(Debug, Clone)]
pub struct PerfStats {
    pub elapsed: Duration,
    pub reader_stats: crate::csv::GetRowsStats,
}

#[derive(Debug, Clone, Copy, Default)]
pub struct ColumnsOffset {
    /// Number of columns that are frozen on the left side (always visible)
    pub num_freeze: u64,

    /// Number of columns that are skipped after the frozen columns (not visible)
    pub num_skip: u64,
}

impl ColumnsOffset {
    /// Check if the column is frozen
    pub fn is_frozen(&self, filtered_columns_index: u64) -> bool {
        filtered_columns_index < self.num_freeze
    }

    /// Get the index of the column in the columns-filtered data given the view port column index
    pub fn get_filtered_column_index(&self, view_port_column_index: u64) -> u64 {
        if view_port_column_index < self.num_freeze {
            return view_port_column_index;
        }
        view_port_column_index.saturating_add(self.num_skip)
    }

    pub fn should_filtered_column_index_be_rendered(&self, filtered_column_index: u64) -> bool {
        if filtered_column_index < self.num_freeze {
            return true;
        }
        filtered_column_index >= self.num_freeze.saturating_add(self.num_skip)
    }

    pub fn is_filtered_column_index_visible(
        &self,
        filtered_column_index: u64,
        num_cols_rendered: u64,
    ) -> bool {
        if filtered_column_index < self.num_freeze {
            return true;
        }
        let rendered_start_index = self.num_freeze.saturating_add(self.num_skip);
        let num_non_frozen_cols_rendered = num_cols_rendered.saturating_sub(self.num_freeze);
        let rendered_end_index = rendered_start_index.saturating_add(num_non_frozen_cols_rendered);
        filtered_column_index >= rendered_start_index && filtered_column_index < rendered_end_index
    }

    pub fn get_num_skip_to_make_visible(&self, filtered_column_index: u64) -> u64 {
        if filtered_column_index < self.num_freeze {
            0
        } else {
            filtered_column_index.saturating_sub(self.num_freeze)
        }
    }
}

pub struct RowsView {
    reader: CsvLensReader,
    rows: Vec<Row>,
    headers: Vec<Header>,
    num_rows: u64,
    num_rows_rendered: u64,
    rows_from: u64,
    cols_offset: ColumnsOffset,
    filter: Option<RowsFilter>,
    columns_filter: Option<Arc<ColumnsFilter>>,
    sorter: Option<Arc<Sorter>>,
    sort_order: SortOrder,
    pub selection: Selection,
    perf_stats: Option<PerfStats>,
    marked_rows: HashSet<usize>,
}

impl RowsView {
    pub fn new(mut reader: CsvLensReader, num_rows: u64) -> CsvlensResult<RowsView> {
        let rows_from = 0;
        let rows = reader.get_rows(rows_from, num_rows)?.0;
        let headers = Self::get_default_headers_from_reader(&reader);
        let view = Self {
            reader,
            rows,
            headers,
            num_rows,
            num_rows_rendered: num_rows,
            rows_from,
            cols_offset: ColumnsOffset::default(),
            filter: None,
            columns_filter: None,
            sorter: None,
            sort_order: SortOrder::Ascending,
            selection: Selection::default(num_rows),
            perf_stats: None,
            marked_rows: HashSet::new(),
        };
        Ok(view)
    }

    pub fn headers(&self) -> &Vec<Header> {
        &self.headers
    }

    pub fn raw_headers(&self) -> &Vec<String> {
        &self.reader.headers
    }

    pub fn rows(&self) -> &Vec<Row> {
        &self.rows
    }

    pub fn marked_rows(&self) -> &HashSet<usize> {
        &self.marked_rows
    }

    pub fn get_column_name_from_global_index(&self, column_index: usize) -> String {
        self.raw_headers()
            .get(column_index)
            .cloned()
            .unwrap_or_default()
    }

    pub fn get_column_name_from_local_index(&self, column_index: usize) -> String {
        self.headers()
            .get(column_index)
            .map(|header| header.name.clone())
            .unwrap_or_default()
    }

    pub fn get_cell_value(&self, column_name: &str) -> Option<String> {
        if let (Some(column_index), Some(row_index)) = (
            self.headers()
                .iter()
                .position(|header| header.name == column_name),
            self.selection.row.index(),
        ) {
            return self
                .rows()
                .get(row_index as usize)
                .and_then(|row| row.fields.get(column_index))
                .cloned();
        }
        None
    }

    /// Get the value of the cell at the current selection. Only returns a value
    /// if the selection type is Cell.
    pub fn get_cell_value_from_selection(&self) -> Option<String> {
        if let (Some(column_index), Some(row_index)) =
            (self.selection.column.index(), self.selection.row.index())
        {
            // Note: row_index and column_index are "local" index.
            return self
                .rows()
                .get(row_index as usize)
                .and_then(|row| {
                    row.fields
                        .get(self.cols_offset.get_filtered_column_index(column_index) as usize)
                })
                .cloned();
        }
        None
    }

    pub fn get_row_value(&self) -> Option<(usize, String)> {
        if let Some(row_index) = self.selection.row.index()
            && let Some(row) = self.rows().get(row_index as usize)
        {
            return Some((row.record_num, row.fields.join("\t")));
        }
        None
    }

    pub fn get_headers_line(&self) -> String {
        self.headers()
            .iter()
            .map(|h| h.name.clone())
            .collect::<Vec<_>>()
            .join("\t")
    }

    pub fn get_rows_values(&mut self, record_numbers: &[usize]) -> CsvlensResult<Vec<String>> {
        if record_numbers.is_empty() {
            return Ok(vec![]);
        }

        // marked rows store 1-based record numbers; convert to 0-based indices for fetching
        let indices: Vec<u64> = record_numbers
            .iter()
            .map(|&n| n.saturating_sub(1) as u64)
            .collect();

        let (mut rows, _) = self.reader.get_rows_for_indices(&indices)?;

        if let Some(columns_filter) = &self.columns_filter {
            rows = Self::subset_columns(&rows, columns_filter.indices());
        }

        Ok(rows.into_iter().map(|row| row.fields.join("\t")).collect())
    }

    pub fn num_rows(&self) -> u64 {
        self.num_rows
    }

    pub fn set_num_rows(&mut self, num_rows: u64) -> CsvlensResult<()> {
        if num_rows == self.num_rows {
            return Ok(());
        }
        self.num_rows = num_rows;
        self.do_get_rows()?;
        Ok(())
    }

    pub fn set_num_rows_rendered(&mut self, num_rows_rendered: u64) {
        self.num_rows_rendered = num_rows_rendered;
        // current selected might be out of range, reset it
        self.selection.row.set_bound(num_rows_rendered);
    }

    pub fn set_reader(
        &mut self,
        reader: CsvLensReader,
        filter_finder: Option<&find::Finder>,
    ) -> CsvlensResult<()> {
        self.reader = reader;
        self.headers = Self::get_default_headers_from_reader(&self.reader);
        if let Some(finder) = filter_finder {
            self.set_filter(finder)?;
        } else {
            self.do_get_rows()?;
        }
        Ok(())
    }

    pub fn set_filter(&mut self, finder: &find::Finder) -> CsvlensResult<()> {
        let filter = RowsFilter::new(finder, self.rows_from, self.num_rows);
        // only need to reload rows if the currently shown indices changed
        let mut needs_reload = true;
        if let Some(cur_filter) = &self.filter
            && cur_filter.indices == filter.indices
        {
            needs_reload = false;
        }
        // but always need to update filter because it holds other states such
        // as total count
        self.filter = Some(filter);
        if needs_reload {
            self.do_get_rows()
        } else {
            Ok(())
        }
    }

    pub fn is_filter(&self) -> bool {
        self.filter.is_some()
    }

    pub fn reset_filter(&mut self, preserve_row_selection: bool) -> CsvlensResult<()> {
        if let Some(filter) = &self.filter {
            let mut record_index_to_preserve = None;
            if preserve_row_selection {
                if let Some(row_selection_index) = self.selection.row.index {
                    record_index_to_preserve =
                        filter.indices.get(row_selection_index as usize).cloned();
                } else {
                    record_index_to_preserve = filter.indices.first().cloned();
                }
            }
            if let (Some(sorter), Some(index)) = (&self.sorter, record_index_to_preserve) {
                // The row index is in terms of original data, but the view is now sorted. Need to
                // get the actual row number to scroll to that points to that record.
                record_index_to_preserve = sorter.get_record_order(index, self.sort_order);
            }
            self.filter = None;
            if let Some(n) = record_index_to_preserve {
                self.handle_scroll_to((n as usize).saturating_add(1))
            } else {
                self.do_get_rows()
            }
        } else {
            Ok(())
        }
    }

    pub fn columns_filter(&self) -> Option<&Arc<ColumnsFilter>> {
        self.columns_filter.as_ref()
    }

    pub fn set_columns_filter(&mut self, columns_filter: &Arc<ColumnsFilter>) -> CsvlensResult<()> {
        let columns_filter = columns_filter.clone();
        self.headers = columns_filter
            .indices()
            .iter()
            .zip(columns_filter.filtered_headers())
            .map(|(i, h)| Header {
                name: h.clone(),
                origin_index: *i,
            })
            .collect();
        self.columns_filter = Some(columns_filter);
        self.do_get_rows()
    }

    pub fn reset_columns_filter(&mut self) -> CsvlensResult<()> {
        self.columns_filter = None;
        self.headers = Self::get_default_headers_from_reader(&self.reader);
        self.do_get_rows()
    }

    pub fn get_column_origin_index(&self, column_index: usize) -> usize {
        self.headers[column_index].origin_index
    }

    fn get_default_headers_from_reader(reader: &CsvLensReader) -> Vec<Header> {
        reader
            .headers
            .iter()
            .enumerate()
            .map(|(i, h)| Header {
                name: h.clone(),
                origin_index: i,
            })
            .collect::<Vec<_>>()
    }

    pub fn sorter(&self) -> &Option<Arc<Sorter>> {
        &self.sorter
    }

    pub fn set_sorter(&mut self, sorter: &Arc<Sorter>) -> CsvlensResult<()> {
        self.sorter = Some(sorter.clone());
        self.do_get_rows()
    }

    pub fn reset_sorter(&mut self) -> CsvlensResult<()> {
        self.sorter = None;
        self.do_get_rows()
    }

    pub fn set_sort_order(&mut self, sort_order: SortOrder) -> CsvlensResult<()> {
        if self.sort_order != sort_order {
            self.sort_order = sort_order;
            return self.do_get_rows();
        }
        Ok(())
    }

    pub fn rows_from(&self) -> u64 {
        self.rows_from
    }

    pub fn set_rows_from(&mut self, rows_from_: u64) -> CsvlensResult<()> {
        let rows_from = if let Some(n) = self.bottom_rows_from() {
            min(rows_from_, n)
        } else {
            rows_from_
        };
        if rows_from == self.rows_from {
            return Ok(());
        }
        self.rows_from = rows_from;
        self.do_get_rows()?;
        Ok(())
    }

    /// Offset of the first column to show. All columns are still read into Row
    /// (per ColumnsFilter if any).
    pub fn cols_offset(&self) -> ColumnsOffset {
        self.cols_offset
    }

    pub fn set_cols_offset_num_skip(&mut self, cols_offset: u64) {
        self.cols_offset.num_skip = min(cols_offset, self.max_cols_offset_num_skip());
    }

    pub fn set_cols_offset_num_freeze(&mut self, num_freeze: u64) {
        self.cols_offset.num_freeze =
            min(num_freeze, self.headers().len().saturating_sub(1) as u64);
    }

    pub fn max_cols_offset_num_skip(&self) -> u64 {
        (self.headers().len() as u64)
            .saturating_sub(self.cols_offset.num_freeze)
            .saturating_sub(1)
    }

    pub fn selected_offset(&self) -> Option<u64> {
        self.selection
            .row
            .index()
            .map(|x| x.saturating_add(self.rows_from))
    }

    pub fn perf_stats(&self) -> Option<PerfStats> {
        self.perf_stats.as_ref().cloned()
    }

    pub fn get_total_line_numbers(&self) -> Option<usize> {
        self.reader.get_total_line_numbers()
    }

    pub fn get_total_line_numbers_approx(&self) -> Option<usize> {
        Some(self.reader.get_approx_line_numbers())
    }

    pub fn in_view(&self, row_index: u64) -> bool {
        let last_row = self.rows_from().saturating_add(self.num_rows());
        if row_index >= self.rows_from() && row_index < last_row {
            return true;
        }
        false
    }

    pub fn handle_control(&mut self, control: &Control) -> CsvlensResult<()> {
        match control {
            Control::ScrollDown => {
                if let Some(i) = self.selection.row.index() {
                    if i >= self.num_rows_rendered.saturating_sub(1) {
                        self.increase_rows_from(1)?;
                    } else {
                        self.selection.row.select_next();
                    }
                } else {
                    self.increase_rows_from(1)?;
                }
            }
            Control::ScrollHalfPageDown => {
                self.increase_rows_from(self.num_rows_rendered / 2)?;
                self.selection.row.select_first()
            }
            Control::ScrollPageDown => {
                self.increase_rows_from(self.num_rows_rendered)?;
                self.selection.row.select_first()
            }
            Control::ScrollUp => {
                if let Some(i) = self.selection.row.index() {
                    if i == 0 {
                        self.decrease_rows_from(1)?;
                    } else {
                        self.selection.row.select_previous();
                    }
                } else {
                    self.decrease_rows_from(1)?;
                }
            }
            Control::ScrollHalfPageUp => {
                self.decrease_rows_from(self.num_rows_rendered / 2)?;
                self.selection.row.select_first()
            }
            Control::ScrollPageUp => {
                self.decrease_rows_from(self.num_rows_rendered)?;
                self.selection.row.select_first()
            }
            Control::ScrollTop => {
                self.set_rows_from(0)?;
                self.selection.row.select_first()
            }
            Control::ScrollBottom => {
                if let Some(total) = self.get_total_line_numbers_indexed() {
                    // Note: Using num_rows_rendered is not exactly correct, but it's simple and
                    // a bit better than num_rows. To be exact, this should use row heights to
                    // determine exactly how many rows to show from the bottom.
                    let rows_from = total.saturating_sub(self.num_rows_rendered as usize) as u64;
                    self.set_rows_from(rows_from)?;
                }
                self.selection.row.select_last()
            }
            Control::ScrollTo(n) => {
                self.handle_scroll_to(*n)?;
            }
            _ => {}
        }
        Ok(())
    }

    /// Scroll to a 1-based record number
    fn handle_scroll_to(&mut self, n: usize) -> CsvlensResult<()> {
        // Don't scroll beyond the bottom row
        let mut rows_from = n.saturating_sub(1) as u64;
        if let Some(n) = self.bottom_rows_from() {
            rows_from = min(rows_from, n);
        }
        self.set_rows_from(rows_from)?;
        // Set row selection to the correct row
        if self.selection.row.index().is_some() {
            self.selection
                .row
                .set_index(n.saturating_sub(1).saturating_sub(rows_from as usize) as u64);
        }
        Ok(())
    }

    fn get_total_line_numbers_indexed(&self) -> Option<usize> {
        if let Some(max_line_number) = self
            .reader
            .get_total_line_numbers()
            .or_else(|| Some(self.reader.get_approx_line_numbers()))
        {
            if let Some(filter) = &self.filter {
                if let Some(max_index) = filter.max_index {
                    if max_index < max_line_number as u64 {
                        // Only allow jumping to the bottom of found records if it can be
                        // efficiently retrieved
                        return Some(filter.total);
                    }
                    return None;
                }
            } else {
                return Some(max_line_number);
            }
        }
        None
    }

    fn increase_rows_from(&mut self, delta: u64) -> CsvlensResult<()> {
        let new_rows_from = self.rows_from.saturating_add(delta);
        self.set_rows_from(new_rows_from)?;
        Ok(())
    }

    fn decrease_rows_from(&mut self, delta: u64) -> CsvlensResult<()> {
        let new_rows_from = self.rows_from.saturating_sub(delta);
        self.set_rows_from(new_rows_from)?;
        Ok(())
    }

    fn bottom_rows_from(&self) -> Option<u64> {
        // fix type conversion craziness
        if let Some(n) = self.get_total_line_numbers_indexed() {
            return Some(n.saturating_sub(self.num_rows_rendered as usize) as u64);
        }
        None
    }

    fn subset_columns(rows: &Vec<Row>, indices: &[usize]) -> Vec<Row> {
        let mut out = vec![];
        for row in rows {
            out.push(row.subset(indices));
        }
        out
    }

    pub fn do_get_rows(&mut self) -> CsvlensResult<()> {
        let start = Instant::now();
        let (mut rows, reader_stats) = if let Some(filter) = &self.filter {
            let indices = &filter.indices;
            self.reader.get_rows_for_indices(indices)?
        } else if let Some(sorter) = &self.sorter {
            if let Some(sorted_indices) =
                sorter.get_sorted_indices(self.rows_from, self.num_rows, self.sort_order)
            {
                self.reader.get_rows_for_indices(&sorted_indices)?
            } else {
                self.reader.get_rows(self.rows_from, self.num_rows)?
            }
        } else {
            self.reader.get_rows(self.rows_from, self.num_rows)?
        };
        let elapsed = start.elapsed();
        if let Some(columns_filter) = &self.columns_filter {
            rows = Self::subset_columns(&rows, columns_filter.indices());
        }
        self.rows = rows;
        self.perf_stats = Some(PerfStats {
            elapsed,
            reader_stats,
        });
        // current selected might be out of range, reset it
        // self.selection.row.set_bound(self.rows.len() as u64);
        Ok(())
    }

    pub fn toggle_mark(&mut self, row_index: usize) -> Option<MarkToggleResult> {
        let record_num = self.rows.get(row_index)?.record_num;

        if self.marked_rows.remove(&record_num) {
            return Some(MarkToggleResult {
                record_num,
                marked: false,
            });
        };

        self.marked_rows.insert(record_num);

        Some(MarkToggleResult {
            record_num,
            marked: true,
        })
    }

    pub fn clear_marks(&mut self) {
        self.marked_rows.clear();
    }

    #[cfg(test)]
    pub fn wait_internal(&self) {
        self.reader.wait_internal()
    }
}
```

## File: `src/watch.rs`
```rust
use std::sync::{Arc, Mutex};

use crate::errors::CsvlensResult;

/// A file watcher that keeps track of the file state and can check for changes. A thin wrapper
/// around a shared `Watcher` for easier usage.
pub struct FileWatcher {
    pub file_state: FileState,
    pub watcher: Arc<Watcher>,
}

impl From<Arc<Watcher>> for FileWatcher {
    fn from(watcher: Arc<Watcher>) -> Self {
        let file_state = watcher.get_file_state();
        FileWatcher {
            file_state,
            watcher,
        }
    }
}

impl FileWatcher {
    /// Check if the file has changed since the last check.
    pub fn check(&mut self) -> bool {
        let current_file_state = self.watcher.get_file_state();
        if self.file_state != current_file_state {
            self.file_state = current_file_state;
            true
        } else {
            false
        }
    }
}

/// A file watcher that monitors a file for changes in a separate thread.
pub struct Watcher {
    internal: Arc<Mutex<WatcherInternal>>,
}

impl Watcher {
    pub fn new(filename: &str) -> CsvlensResult<Watcher> {
        let internal = WatcherInternal::init(filename)?;

        Ok(Watcher { internal })
    }

    pub fn get_file_state(&self) -> FileState {
        let internal = self.internal.lock().unwrap();
        internal.file_state
    }

    pub fn terminate(&self) {
        let mut internal = self.internal.lock().unwrap();
        internal.terminate();
    }
}

impl Drop for Watcher {
    fn drop(&mut self) {
        self.terminate();
    }
}

#[derive(Debug, Copy, Clone, Eq, PartialEq)]
pub struct FileState {
    pub modified_time: std::time::SystemTime,
    pub size: u64,
}

impl From<std::fs::Metadata> for FileState {
    fn from(metadata: std::fs::Metadata) -> Self {
        FileState {
            modified_time: metadata
                .modified()
                .unwrap_or(std::time::SystemTime::UNIX_EPOCH),
            size: metadata.len(),
        }
    }
}

struct WatcherInternal {
    should_terminate: bool,
    file_state: FileState,
}

impl WatcherInternal {
    pub fn init(filename: &str) -> CsvlensResult<Arc<Mutex<WatcherInternal>>> {
        let file_state = std::fs::metadata(filename)?;

        let internal = WatcherInternal {
            should_terminate: false,
            file_state: file_state.into(),
        };

        let m_internal = Arc::new(Mutex::new(internal));

        let _handle = {
            let filename = filename.to_string();
            let m_internal = Arc::clone(&m_internal);
            std::thread::spawn(move || {
                loop {
                    if m_internal.lock().unwrap().should_terminate {
                        break;
                    }
                    match std::fs::metadata(&filename) {
                        Ok(metadata) => {
                            let mut internal = m_internal.lock().unwrap();
                            let new_file_state = FileState::from(metadata);
                            internal.file_state = new_file_state;
                        }
                        Err(_) => {
                            // File might be temporarily unavailable, skip for now
                        }
                    }
                    std::thread::sleep(std::time::Duration::from_millis(250));
                }
            })
        };

        Ok(m_internal)
    }

    pub fn terminate(&mut self) {
        self.should_terminate = true;
    }
}
```

## File: `src/wrap.rs`
```rust
use ratatui::text::{Line, Span};

pub struct LineWrapper<'a> {
    spans: &'a [Span<'a>],
    max_width: usize,
    word_wrap: bool,
    index: usize,
    pending: Option<Span<'a>>,
}

impl<'a> LineWrapper<'a> {
    pub fn new(spans: &'a [Span<'a>], max_width: usize, word_wrap: bool) -> Self {
        LineWrapper {
            spans,
            max_width,
            word_wrap,
            index: 0,
            pending: None,
        }
    }

    pub fn next(&mut self) -> Option<Line<'a>> {
        if self.finished() {
            return None;
        }
        let mut out_spans = vec![];
        let mut remaining_width = self.max_width;
        loop {
            let mut span = None;
            if let Some(s) = self.pending.take() {
                span = Some(s);
            } else if self.index < self.spans.len() {
                span = Some(self.spans.get(self.index).cloned().unwrap());
                self.index += 1;
            }
            if let Some(span) = span {
                let chars_count = span.content.chars().count();
                let newline_pos = span.content.chars().position(|c| c == '\n');
                if let Some((pos, true)) = newline_pos.map(|x| (x, x <= remaining_width)) {
                    out_spans.push(Span::styled(
                        span.content.chars().take(pos).collect::<String>(),
                        span.style,
                    ));
                    self.pending = Some(Span::styled(
                        span.content.chars().skip(pos + 1).collect::<String>(),
                        span.style,
                    ));
                    // Technically this might not be zero, but this is to force the loop to break -
                    // we must wrap now.
                    remaining_width = 0;
                } else if chars_count <= remaining_width {
                    remaining_width = remaining_width.saturating_sub(chars_count);
                    out_spans.push(span);
                } else {
                    let mut current: String = span.content.chars().take(remaining_width).collect();
                    let pending: String;

                    if self.word_wrap {
                        if let Some(wrapped) = LineWrapper::wrap_by_whitespace(current.as_str()) {
                            current = wrapped;
                            pending = span.content.chars().skip(current.chars().count()).collect();
                        } else {
                            pending = span.content.chars().skip(remaining_width).collect();
                        }
                    } else {
                        pending = span.content.chars().skip(remaining_width).collect();
                    }
                    out_spans.push(Span::styled(current, span.style));
                    self.pending = Some(Span::styled(pending, span.style));
                    remaining_width = 0;
                }
            } else {
                break;
            }
            if remaining_width == 0 {
                break;
            }
        }
        Some(Line::from(out_spans))
    }

    pub fn finished(&self) -> bool {
        self.pending.is_none() && self.index >= self.spans.len()
    }

    fn wrap_by_whitespace(s: &str) -> Option<String> {
        let mut s_split = s.split(' ');
        let last = s_split.next_back();
        if last.is_some() {
            let front = s_split.collect::<Vec<&str>>().join(" ");
            if front.chars().filter(|c| !c.is_whitespace()).count() > 0 {
                Some(front + " ")
            } else {
                None
            }
        } else {
            None
        }
    }
}

#[cfg(test)]
mod tests {

    use super::*;
    use ratatui::style::{Color, Style};

    #[test]
    fn test_no_wrapping() {
        let s = Span::raw("hello");
        let spans = vec![s.clone()];
        let mut wrapper = LineWrapper::new(&spans, 10, false);
        assert_eq!(wrapper.next(), Some(Line::from(vec![s.clone()])));
        assert_eq!(wrapper.next(), None);
    }

    #[test]
    fn test_with_wrapping() {
        let s = Span::raw("hello");
        let spans = vec![s.clone()];
        let mut wrapper = LineWrapper::new(&spans, 2, false);
        assert_eq!(wrapper.next(), Some(Line::from(vec![Span::raw("he")])));
        assert_eq!(wrapper.next(), Some(Line::from(vec![Span::raw("ll")])));
        assert_eq!(wrapper.next(), Some(Line::from(vec![Span::raw("o")])));
        assert_eq!(wrapper.next(), None);
    }

    #[test]
    fn test_new_lines_before_max_width() {
        let s = Span::raw("hello\nworld");
        let spans = vec![s.clone()];
        let mut wrapper = LineWrapper::new(&spans, 10, false);
        assert_eq!(wrapper.next(), Some(Line::from(vec![Span::raw("hello")])));
        assert_eq!(wrapper.next(), Some(Line::from(vec![Span::raw("world")])));
        assert_eq!(wrapper.next(), None);
    }

    #[test]
    fn test_new_lines_after_max_width() {
        let s = Span::raw("hello\nworld");
        let spans = vec![s.clone()];
        let mut wrapper = LineWrapper::new(&spans, 3, false);
        assert_eq!(wrapper.next(), Some(Line::from(vec![Span::raw("hel")])));
        assert_eq!(wrapper.next(), Some(Line::from(vec![Span::raw("lo")])));
        assert_eq!(wrapper.next(), Some(Line::from(vec![Span::raw("wor")])));
        assert_eq!(wrapper.next(), Some(Line::from(vec![Span::raw("ld")])));
        assert_eq!(wrapper.next(), None);
    }

    #[test]
    fn test_multiple_spans() {
        let style = Style::default().fg(Color::Red);
        let spans = vec![
            Span::raw("hello\n"),
            Span::styled("my", style),
            Span::raw("world"),
        ];
        let mut wrapper = LineWrapper::new(&spans, 5, false);
        assert_eq!(wrapper.next(), Some(Line::from(vec![Span::raw("hello")])));
        assert_eq!(
            wrapper.next(),
            Some(Line::from(vec![
                Span::raw(""),
                Span::styled("my", style),
                Span::raw("wor")
            ]))
        );
        assert_eq!(wrapper.next(), Some(Line::from(vec![Span::raw("ld")])));
        assert_eq!(wrapper.next(), None);
    }

    #[test]
    fn test_wrap_at_styled_span() {
        let style = Style::default().fg(Color::Red);
        let spans = vec![
            Span::raw("hello"),
            Span::styled("m\ny", style),
            Span::raw("world"),
        ];
        let mut wrapper = LineWrapper::new(&spans, 5, false);
        assert_eq!(wrapper.next(), Some(Line::from(vec![Span::raw("hello")])));
        assert_eq!(
            wrapper.next(),
            Some(Line::from(vec![Span::styled("m", style)]))
        );
        assert_eq!(
            wrapper.next(),
            Some(Line::from(vec![
                Span::styled("y", style),
                Span::raw("worl")
            ]))
        );
        assert_eq!(wrapper.next(), Some(Line::from(vec![Span::raw("d")])));
        assert_eq!(wrapper.next(), None);
    }

    #[test]
    fn test_unicode() {
        let s = Span::raw("héllo");
        let spans = vec![s.clone()];
        let mut wrapper = LineWrapper::new(&spans, 2, false);
        assert_eq!(wrapper.next(), Some(Line::from(vec![Span::raw("hé")])));
        assert_eq!(wrapper.next(), Some(Line::from(vec![Span::raw("ll")])));
        assert_eq!(wrapper.next(), Some(Line::from(vec![Span::raw("o")])));
        assert_eq!(wrapper.next(), None);
    }

    #[test]
    fn test_unicode_with_newline_w1() {
        let s = Span::raw("éé\néééééé");
        let spans = vec![s.clone()];
        let mut wrapper = LineWrapper::new(&spans, 1, false);
        assert_eq!(wrapper.next(), Some(Line::from(vec![Span::raw("é")])));
        assert_eq!(wrapper.next(), Some(Line::from(vec![Span::raw("é")])));
        assert_eq!(wrapper.next(), Some(Line::from(vec![Span::raw("é")])));
        assert_eq!(wrapper.next(), Some(Line::from(vec![Span::raw("é")])));
        assert_eq!(wrapper.next(), Some(Line::from(vec![Span::raw("é")])));
        assert_eq!(wrapper.next(), Some(Line::from(vec![Span::raw("é")])));
        assert_eq!(wrapper.next(), Some(Line::from(vec![Span::raw("é")])));
        assert_eq!(wrapper.next(), Some(Line::from(vec![Span::raw("é")])));
        assert_eq!(wrapper.next(), None);
    }

    #[test]
    fn test_unicode_with_newline_w2() {
        let s = Span::raw("éé\néééééé");
        let spans = vec![s.clone()];
        let mut wrapper = LineWrapper::new(&spans, 2, false);
        assert_eq!(wrapper.next(), Some(Line::from(vec![Span::raw("éé")])));
        assert_eq!(wrapper.next(), Some(Line::from(vec![Span::raw("éé")])));
        assert_eq!(wrapper.next(), Some(Line::from(vec![Span::raw("éé")])));
        assert_eq!(wrapper.next(), Some(Line::from(vec![Span::raw("éé")])));
        assert_eq!(wrapper.next(), None);
    }

    #[test]
    fn test_unicode_with_newline_w3() {
        let s = Span::raw("éé\néééééé");
        let spans = vec![s.clone()];
        let mut wrapper = LineWrapper::new(&spans, 3, false);
        assert_eq!(wrapper.next(), Some(Line::from(vec![Span::raw("éé")])));
        assert_eq!(wrapper.next(), Some(Line::from(vec![Span::raw("ééé")])));
        assert_eq!(wrapper.next(), Some(Line::from(vec![Span::raw("ééé")])));
        assert_eq!(wrapper.next(), None);
    }

    #[test]
    fn test_unicode_with_newline_w4() {
        let s = Span::raw("éé\néééééé");
        let spans = vec![s.clone()];
        let mut wrapper = LineWrapper::new(&spans, 4, false);
        assert_eq!(wrapper.next(), Some(Line::from(vec![Span::raw("éé")])));
        assert_eq!(wrapper.next(), Some(Line::from(vec![Span::raw("éééé")])));
        assert_eq!(wrapper.next(), Some(Line::from(vec![Span::raw("éé")])));
        assert_eq!(wrapper.next(), None);
    }

    #[test]
    fn test_wrap_by_whitespace_1() {
        let s = Span::raw("é é");
        let out = LineWrapper::wrap_by_whitespace(&s.content);
        assert_eq!(out, Some("é ".to_string()));
    }

    #[test]
    fn test_wrap_by_whitespace_2() {
        let s = Span::raw(" éé");
        let out = LineWrapper::wrap_by_whitespace(&s.content);
        assert_eq!(out, None);
    }

    #[test]
    fn test_word_wrap_1() {
        let s = Span::raw("éé\né éé ééé");
        let spans = vec![s.clone()];
        let mut wrapper = LineWrapper::new(&spans, 3, true);
        assert_eq!(wrapper.next(), Some(Line::from(vec![Span::raw("éé")])));
        assert_eq!(wrapper.next(), Some(Line::from(vec![Span::raw("é ")])));
        assert_eq!(wrapper.next(), Some(Line::from(vec![Span::raw("éé ")])));
        assert_eq!(wrapper.next(), Some(Line::from(vec![Span::raw("ééé")])));
        assert_eq!(wrapper.next(), None);
    }

    #[test]
    fn test_word_wrap_2() {
        let s = Span::raw("ééé é ééé ééé");
        let spans = vec![s.clone()];
        let mut wrapper = LineWrapper::new(&spans, 3, true);
        assert_eq!(wrapper.next(), Some(Line::from(vec![Span::raw("ééé")])));
        assert_eq!(wrapper.next(), Some(Line::from(vec![Span::raw(" é ")])));
        assert_eq!(wrapper.next(), Some(Line::from(vec![Span::raw("ééé")])));
        assert_eq!(wrapper.next(), Some(Line::from(vec![Span::raw(" éé")])));
        assert_eq!(wrapper.next(), Some(Line::from(vec![Span::raw("é")])));
        assert_eq!(wrapper.next(), None);
    }

    #[test]
    fn test_multiple_newlines() {
        let s = Span::raw("ééé\n\nééé");
        let spans = vec![s.clone()];
        let mut wrapper = LineWrapper::new(&spans, 4, false);
        assert_eq!(wrapper.next(), Some(Line::from(vec![Span::raw("ééé")])));
        assert_eq!(wrapper.next(), Some(Line::from(vec![Span::raw("")])));
        assert_eq!(wrapper.next(), Some(Line::from(vec![Span::raw("ééé")])));
        assert_eq!(wrapper.next(), None);
    }

    #[test]
    fn test_zero_max_width() {
        let s = Span::raw("ééé\n\nééé");
        let spans = vec![s.clone()];
        let mut wrapper = LineWrapper::new(&spans, 0, false);
        assert_eq!(wrapper.next(), Some(Line::from(vec![Span::raw("")])));
        assert_eq!(wrapper.next(), Some(Line::from(vec![Span::raw("")])));
        assert_eq!(wrapper.next(), Some(Line::from(vec![Span::raw("")])));
        assert_eq!(wrapper.next(), Some(Line::from(vec![Span::raw("")])));
        assert_eq!(wrapper.finished(), false);
    }
}
```

## File: `src/util/events.rs`
```rust
use std::time::Duration;

use crossterm::event::{Event, KeyEvent, KeyEventKind, poll, read};

use crate::watch::FileWatcher;

pub enum CsvlensEvent<I> {
    Input(I),
    FileChanged,
    Tick,
}

/// A small event handler that wrap termion input and tick events. Each event
/// type is handled in its own thread and returned to a common `Receiver`
pub struct CsvlensEvents {
    tick_rate: Duration,
    file_watcher: Option<FileWatcher>,
}

impl CsvlensEvents {
    pub fn new(file_watcher: Option<FileWatcher>) -> CsvlensEvents {
        CsvlensEvents {
            tick_rate: Duration::from_millis(250),
            file_watcher,
        }
    }

    pub fn next(&mut self) -> std::io::Result<CsvlensEvent<KeyEvent>> {
        // let now = Instant::now();
        match poll(self.tick_rate) {
            Ok(true) => match read()? {
                Event::Key(event) if event.kind == KeyEventKind::Press => {
                    Ok(CsvlensEvent::Input(event))
                }
                _ => Ok(CsvlensEvent::Tick),
            },
            Ok(false) => {
                if let Some(file_watcher) = &mut self.file_watcher {
                    if file_watcher.check() {
                        return Ok(CsvlensEvent::FileChanged);
                    }
                    return Ok(CsvlensEvent::Tick);
                }
                Ok(CsvlensEvent::Tick)
            }
            Err(_) => todo!(),
        }
    }
}
```

## File: `src/util/mod.rs`
```rust
pub mod events;
```

## File: `tests/data/bad_73.csv`
```
COL1, COL2
c1
c2, v2
c2, 4,
c3
c4
c5
c7
c9
c10
c11
c12
c13
c14,2
```

## File: `tests/data/bad_double_quote.csv`
```
Column1, "column2"
1, "quote"
5, "Comma, comma"
```

## File: `tests/data/cell_with_crlf.csv`
```
column_name
"value 1
"
"value 2
"
"value 3
"
```

## File: `tests/data/cities.csv`
```
LatD,LatM,LatS,NS,LonD,LonM,LonS,EW,City,State
41,5,59,N,80,39,0,W,Youngstown,OH
42,52,48,N,97,23,23,,Yankton,SD
46,35,59,N,120,30,36,W,Yakima,WA
42,16,12,N,71,48,0,W,Worcester,MA
43,37,48,N,89,46,11,W,Wisconsin Dells,WI
36,5,59,N,80,15,0,W,Winston-Salem,NC
49,52,48,N,97,9,0,W,Winnipeg,MB
39,11,23,N,78,9,36,W,Winchester,VA
34,14,24,N,77,55,11,W,Wilmington,NC
39,45,0,N,75,33,0,W,Wilmington,DE
48,9,0,N,103,37,12,W,Williston,ND
41,15,0,N,77,0,0,W,Williamsport,PA
37,40,48,N,82,16,47,W,Williamson,WV
33,54,0,N,98,29,23,W,Wichita Falls,TX
37,41,23,N,97,20,23,W,Wichita,KS
40,4,11,N,80,43,12,W,Wheeling,WV
26,43,11,N,80,3,0,W,West Palm Beach,FL
47,25,11,N,120,19,11,W,Wenatchee,WA
41,25,11,N,122,23,23,W,Weed,CA
31,13,11,N,82,20,59,W,Waycross,GA
44,57,35,N,89,38,23,W,Wausau,WI
42,21,36,N,87,49,48,W,Waukegan,IL
44,54,0,N,97,6,36,W,Watertown,SD
43,58,47,N,75,55,11,W,Watertown,NY
42,30,0,N,92,20,23,W,Waterloo,IA
41,32,59,N,73,3,0,W,Waterbury,CT
38,53,23,N,77,1,47,W,Washington,DC
41,50,59,N,79,8,23,W,Warren,PA
46,4,11,N,118,19,48,W,Walla Walla,WA
31,32,59,N,97,8,23,W,Waco,TX
38,40,48,N,87,31,47,W,Vincennes,IN
28,48,35,N,97,0,36,W,Victoria,TX
32,20,59,N,90,52,47,W,Vicksburg,MS
49,16,12,N,123,7,12,W,Vancouver,BC
46,55,11,N,98,0,36,W,Valley City,ND
30,49,47,N,83,16,47,W,Valdosta,GA
43,6,36,N,75,13,48,W,Utica,NY
39,54,0,N,79,43,48,W,Uniontown,PA
32,20,59,N,95,18,0,W,Tyler,TX
42,33,36,N,114,28,12,W,Twin Falls,ID
33,12,35,N,87,34,11,W,Tuscaloosa,AL
34,15,35,N,88,42,35,W,Tupelo,MS
36,9,35,N,95,54,36,W,Tulsa,OK
32,13,12,N,110,58,12,W,Tucson,AZ
37,10,11,N,104,30,36,W,Trinidad,CO
40,13,47,N,74,46,11,W,Trenton,NJ
44,45,35,N,85,37,47,W,Traverse City,MI
43,39,0,N,79,22,47,W,Toronto,ON
39,2,59,N,95,40,11,W,Topeka,KS
41,39,0,N,83,32,24,W,Toledo,OH
33,25,48,N,94,3,0,W,Texarkana,TX
39,28,12,N,87,24,36,W,Terre Haute,IN
27,57,0,N,82,26,59,W,Tampa,FL
30,27,0,N,84,16,47,W,Tallahassee,FL
47,14,24,N,122,25,48,W,Tacoma,WA
43,2,59,N,76,9,0,W,Syracuse,NY
32,35,59,N,82,20,23,W,Swainsboro,GA
33,55,11,N,80,20,59,W,Sumter,SC
40,59,24,N,75,11,24,W,Stroudsburg,PA
37,57,35,N,121,17,24,W,Stockton,CA
44,31,12,N,89,34,11,W,Stevens Point,WI
40,21,36,N,80,37,12,W,Steubenville,OH
40,37,11,N,103,13,12,W,Sterling,CO
38,9,0,N,79,4,11,W,Staunton,VA
39,55,11,N,83,48,35,W,Springfield,OH
37,13,12,N,93,17,24,W,Springfield,MO
42,5,59,N,72,35,23,W,Springfield,MA
39,47,59,N,89,39,0,W,Springfield,IL
47,40,11,N,117,24,36,W,Spokane,WA
41,40,48,N,86,15,0,W,South Bend,IN
43,32,24,N,96,43,48,W,Sioux Falls,SD
42,29,24,N,96,23,23,W,Sioux City,IA
32,30,35,N,93,45,0,W,Shreveport,LA
33,38,23,N,96,36,36,W,Sherman,TX
44,47,59,N,106,57,35,W,Sheridan,WY
35,13,47,N,96,40,48,W,Seminole,OK
32,25,11,N,87,1,11,W,Selma,AL
38,42,35,N,93,13,48,W,Sedalia,MO
47,35,59,N,122,19,48,W,Seattle,WA
41,24,35,N,75,40,11,W,Scranton,PA
41,52,11,N,103,39,36,W,Scottsbluff,NB
42,49,11,N,73,56,59,W,Schenectady,NY
32,4,48,N,81,5,23,W,Savannah,GA
46,29,24,N,84,20,59,W,Sault Sainte Marie,MI
27,20,24,N,82,31,47,W,Sarasota,FL
38,26,23,N,122,43,12,W,Santa Rosa,CA
35,40,48,N,105,56,59,W,Santa Fe,NM
34,25,11,N,119,41,59,W,Santa Barbara,CA
33,45,35,N,117,52,12,W,Santa Ana,CA
37,20,24,N,121,52,47,W,San Jose,CA
37,46,47,N,122,25,11,W,San Francisco,CA
41,27,0,N,82,42,35,W,Sandusky,OH
32,42,35,N,117,9,0,W,San Diego,CA
34,6,36,N,117,18,35,W,San Bernardino,CA
29,25,12,N,98,30,0,W,San Antonio,TX
31,27,35,N,100,26,24,W,San Angelo,TX
40,45,35,N,111,52,47,W,Salt Lake City,UT
38,22,11,N,75,35,59,W,Salisbury,MD
36,40,11,N,121,39,0,W,Salinas,CA
38,50,24,N,97,36,36,W,Salina,KS
38,31,47,N,106,0,0,W,Salida,CO
44,56,23,N,123,1,47,W,Salem,OR
44,57,0,N,93,5,59,W,Saint Paul,MN
38,37,11,N,90,11,24,W,Saint Louis,MO
39,46,12,N,94,50,23,W,Saint Joseph,MO
42,5,59,N,86,28,48,W,Saint Joseph,MI
44,25,11,N,72,1,11,W,Saint Johnsbury,VT
45,34,11,N,94,10,11,W,Saint Cloud,MN
29,53,23,N,81,19,11,W,Saint Augustine,FL
43,25,48,N,83,56,24,W,Saginaw,MI
38,35,24,N,121,29,23,W,Sacramento,CA
43,36,36,N,72,58,12,W,Rutland,VT
33,24,0,N,104,31,47,W,Roswell,NM
35,56,23,N,77,48,0,W,Rocky Mount,NC
41,35,24,N,109,13,48,W,Rock Springs,WY
42,16,12,N,89,5,59,W,Rockford,IL
43,9,35,N,77,36,36,W,Rochester,NY
44,1,12,N,92,27,35,W,Rochester,MN
37,16,12,N,79,56,24,W,Roanoke,VA
37,32,24,N,77,26,59,W,Richmond,VA
39,49,48,N,84,53,23,W,Richmond,IN
38,46,12,N,112,5,23,W,Richfield,UT
45,38,23,N,89,25,11,W,Rhinelander,WI
39,31,12,N,119,48,35,W,Reno,NV
50,25,11,N,104,39,0,W,Regina,SA
40,10,48,N,122,14,23,W,Red Bluff,CA
40,19,48,N,75,55,48,W,Reading,PA
41,9,35,N,81,14,23,W,Ravenna,OH
```

## File: `tests/data/empty.csv`
```
a,b
1,
2,
```

## File: `tests/data/filter.csv`
```
a,b
$(#1#2#.3),1
123,2
456,3
```

## File: `tests/data/gnu_lgpl.txt`
```
		   GNU LESSER GENERAL PUBLIC LICENSE
                       Version 3, 29 June 2007

 Copyright (C) 2007 Free Software Foundation, Inc. <http://fsf.org/>
 Everyone is permitted to copy and distribute verbatim copies
 of this license document, but changing it is not allowed.


  This version of the GNU Lesser General Public License incorporates
the terms and conditions of version 3 of the GNU General Public
License, supplemented by the additional permissions listed below.

  0. Additional Definitions.

  As used herein, "this License" refers to version 3 of the GNU Lesser
General Public License, and the "GNU GPL" refers to version 3 of the GNU
General Public License.

  "The Library" refers to a covered work governed by this License,
other than an Application or a Combined Work as defined below.

  An "Application" is any work that makes use of an interface provided
by the Library, but which is not otherwise based on the Library.
Defining a subclass of a class defined by the Library is deemed a mode
of using an interface provided by the Library.

  A "Combined Work" is a work produced by combining or linking an
Application with the Library.  The particular version of the Library
with which the Combined Work was made is also called the "Linked
Version".

  The "Minimal Corresponding Source" for a Combined Work means the
Corresponding Source for the Combined Work, excluding any source code
for portions of the Combined Work that, considered in isolation, are
based on the Application, and not on the Linked Version.

  The "Corresponding Application Code" for a Combined Work means the
object code and/or source code for the Application, including any data
and utility programs needed for reproducing the Combined Work from the
Application, but excluding the System Libraries of the Combined Work.

  1. Exception to Section 3 of the GNU GPL.

  You may convey a covered work under sections 3 and 4 of this License
without being bound by section 3 of the GNU GPL.

  2. Conveying Modified Versions.

  If you modify a copy of the Library, and, in your modifications, a
facility refers to a function or data to be supplied by an Application
that uses the facility (other than as an argument passed when the
facility is invoked), then you may convey a copy of the modified
version:

   a) under this License, provided that you make a good faith effort to
   ensure that, in the event an Application does not supply the
   function or data, the facility still operates, and performs
   whatever part of its purpose remains meaningful, or

   b) under the GNU GPL, with none of the additional permissions of
   this License applicable to that copy.

  3. Object Code Incorporating Material from Library Header Files.

  The object code form of an Application may incorporate material from
a header file that is part of the Library.  You may convey such object
code under terms of your choice, provided that, if the incorporated
material is not limited to numerical parameters, data structure
layouts and accessors, or small macros, inline functions and templates
(ten or fewer lines in length), you do both of the following:

   a) Give prominent notice with each copy of the object code that the
   Library is used in it and that the Library and its use are
   covered by this License.

   b) Accompany the object code with a copy of the GNU GPL and this license
   document.

  4. Combined Works.

  You may convey a Combined Work under terms of your choice that,
taken together, effectively do not restrict modification of the
portions of the Library contained in the Combined Work and reverse
engineering for debugging such modifications, if you also do each of
the following:

   a) Give prominent notice with each copy of the Combined Work that
   the Library is used in it and that the Library and its use are
   covered by this License.

   b) Accompany the Combined Work with a copy of the GNU GPL and this license
   document.

   c) For a Combined Work that displays copyright notices during
   execution, include the copyright notice for the Library among
   these notices, as well as a reference directing the user to the
   copies of the GNU GPL and this license document.

   d) Do one of the following:

       0) Convey the Minimal Corresponding Source under the terms of this
       License, and the Corresponding Application Code in a form
       suitable for, and under terms that permit, the user to
       recombine or relink the Application with a modified version of
       the Linked Version to produce a modified Combined Work, in the
       manner specified by section 6 of the GNU GPL for conveying
       Corresponding Source.

       1) Use a suitable shared library mechanism for linking with the
       Library.  A suitable mechanism is one that (a) uses at run time
       a copy of the Library already present on the user's computer
       system, and (b) will operate properly with a modified version
       of the Library that is interface-compatible with the Linked
       Version.

   e) Provide Installation Information, but only if you would otherwise
   be required to provide such information under section 6 of the
   GNU GPL, and only to the extent that such information is
   necessary to install and execute a modified version of the
   Combined Work produced by recombining or relinking the
   Application with a modified version of the Linked Version. (If
   you use option 4d0, the Installation Information must accompany
   the Minimal Corresponding Source and Corresponding Application
   Code. If you use option 4d1, you must provide the Installation
   Information in the manner specified by section 6 of the GNU GPL
   for conveying Corresponding Source.)

  5. Combined Libraries.

  You may place library facilities that are a work based on the
Library side by side in a single library together with other library
facilities that are not Applications and are not covered by this
License, and convey such a combined library under terms of your
choice, if you do both of the following:

   a) Accompany the combined library with a copy of the same work based
   on the Library, uncombined with any other library facilities,
   conveyed under the terms of this License.

   b) Give prominent notice with the combined library that part of it
   is a work based on the Library, and explaining where to find the
   accompanying uncombined form of the same work.

  6. Revised Versions of the GNU Lesser General Public License.

  The Free Software Foundation may publish revised and/or new versions
of the GNU Lesser General Public License from time to time. Such new
versions will be similar in spirit to the present version, but may
differ in detail to address new problems or concerns.

  Each version is given a distinguishing version number. If the
Library as you received it specifies that a certain numbered version
of the GNU Lesser General Public License "or any later version"
applies to it, you have the option of following the terms and
conditions either of that published version or of any later version
published by the Free Software Foundation. If the Library as you
received it does not specify a version number of the GNU Lesser
General Public License, you may choose any version of the GNU Lesser
General Public License ever published by the Free Software Foundation.

  If the Library as you received it specifies that a proxy can decide
whether future versions of the GNU Lesser General Public License shall
apply, that proxy's public statement of acceptance of any version is
permanent authorization for you to choose that version for the
Library.
```

## File: `tests/data/good_double_quote.csv`
```
Column1,"column2"
1,"quote"
5,"Comma, comma"
```

## File: `tests/data/irregular.csv`
```
COL1, COL2
c1
c2, v2
```

## File: `tests/data/irregular_last_row.csv`
```
AAAAAAAAAAAAAAAAAAAA,BBBBBBBBBBBBBBBBBBBB,AAAAAAAAAAAAAAAAAAAA,BBBBBBBBBBBBBBBBBBBB,AAAAAAAAAAAAAAAAAAAA,BBBBBBBBBBBBBBBBBBBB,AAAAAAAAAAAAAAAAAAAA,BBBBBBBBBBBBBBBBBBBB,AAAAAAAAAAAAAAAAAAAA,BBBBBBBBBBBBBBBBBBBB
AAAAAAAAAAAAAAAAAAAA,BBBBBBBBBBBBBBBBBBBB,AAAAAAAAAAAAAAAAAAAA,BBBBBBBBBBBBBBBBBBBB,AAAAAAAAAAAAAAAAAAAA,BBBBBBBBBBBBBBBBBBBB,AAAAAAAAAAAAAAAAAAAA,BBBBBBBBBBBBBBBBBBBB,AAAAAAAAAAAAAAAAAAAA,BBBBBBBBBBBBBBBBBBBB
A,
```

## File: `tests/data/irregular_more_fields.csv`
```
COL1,COL2
x1,x2,x3
y1,y2,y3,y4
```

## File: `tests/data/multi_lines.csv`
```
a,"b","c"
1,"this is a very long text that surely will not fit in your small screen",12345
2,"this
is
an
even
longer
text
that
surely
will
not
fit
in
your
small
screen",678910
3,normal text now,"123,456,789"
```

## File: `tests/data/multi_lines_carriage_return.csv`
```
a,b,c
1,this is a very long text that surely will not fit in your small screen,12345
2,"this

is

an

even

longer

text

that

surely

will

not

fit

in

your

small

screen",678910
3,normal text now,"123,456,789"
```

## File: `tests/data/multiple_newlines.csv`
```
a,b,c
1,this is a very long text that surely will not fit in your small screen,12345
2,"this

is

an

even

longer

text

that

surely

will

not

fit

in

your

small

screen",678910
3,normal text now,"123,456,789"
```

## File: `tests/data/natural_sort.csv`
```
name,value
disk1,10
disk10,100
disk2,20
disk11,110
file1.txt,1
file10.txt,10
file2.txt,2
file20.txt,20
chapter1,1
chapter10,10
chapter2,2
chapter20,20
appendix,0
```

## File: `tests/data/no_headers.csv`
```
A1,B1
A2,B2
A3,B3
A4,B4
A5,B5
A6,B6
A7,B7
A8,B8
A9,B9
A10,B10
A11,B11
A12,B12
A13,B13
A14,B14
A15,B15
A16,B16
A17,B17
A18,B18
A19,B19
A20,B20
```

## File: `tests/data/one_wide_column.txt`
```
id,text,label
1,this is a very very very very very very very very very very very very very very very very very very very very very very very long thing,hotdog
2,this is a very very very very very very very very very very very very very very very very very very very very very very very short thing,not_hotdog
```

## File: `tests/data/simple.csv`
```
a,b
A1,B1
A2,B2
A3,B3
A4,B4
A5,B5
A6,B6
A7,B7
A8,B8
A9,B9
A10,B10
A11,B11
A12,B12
A13,B13
A14,B14
A15,B15
A16,B16
A17,B17
A18,B18
A19,B19
A20,B20
A21,B21
A22,B22
A23,B23
A24,B24
A25,B25
A26,B26
A27,B27
A28,B28
A29,B29
A30,B30
A31,B31
A32,B32
A33,B33
A34,B34
A35,B35
A36,B36
A37,B37
A38,B38
A39,B39
A40,B40
A41,B41
A42,B42
A43,B43
A44,B44
A45,B45
A46,B46
A47,B47
A48,B48
A49,B49
A50,B50
A51,B51
A52,B52
A53,B53
A54,B54
A55,B55
A56,B56
A57,B57
A58,B58
A59,B59
A60,B60
A61,B61
A62,B62
A63,B63
A64,B64
A65,B65
A66,B66
A67,B67
A68,B68
A69,B69
A70,B70
A71,B71
A72,B72
A73,B73
A74,B74
A75,B75
A76,B76
A77,B77
A78,B78
A79,B79
A80,B80
A81,B81
A82,B82
A83,B83
A84,B84
A85,B85
A86,B86
A87,B87
A88,B88
A89,B89
A90,B90
A91,B91
A92,B92
A93,B93
A94,B94
A95,B95
A96,B96
A97,B97
A98,B98
A99,B99
A100,B100
A101,B101
A102,B102
A103,B103
A104,B104
A105,B105
A106,B106
A107,B107
A108,B108
A109,B109
A110,B110
A111,B111
A112,B112
A113,B113
A114,B114
A115,B115
A116,B116
A117,B117
A118,B118
A119,B119
A120,B120
A121,B121
A122,B122
A123,B123
A124,B124
A125,B125
A126,B126
A127,B127
A128,B128
A129,B129
A130,B130
A131,B131
A132,B132
A133,B133
A134,B134
A135,B135
A136,B136
A137,B137
A138,B138
A139,B139
A140,B140
A141,B141
A142,B142
A143,B143
A144,B144
A145,B145
A146,B146
A147,B147
A148,B148
A149,B149
A150,B150
A151,B151
A152,B152
A153,B153
A154,B154
A155,B155
A156,B156
A157,B157
A158,B158
A159,B159
A160,B160
A161,B161
A162,B162
A163,B163
A164,B164
A165,B165
A166,B166
A167,B167
A168,B168
A169,B169
A170,B170
A171,B171
A172,B172
A173,B173
A174,B174
A175,B175
A176,B176
A177,B177
A178,B178
A179,B179
A180,B180
A181,B181
A182,B182
A183,B183
A184,B184
A185,B185
A186,B186
A187,B187
A188,B188
A189,B189
A190,B190
A191,B191
A192,B192
A193,B193
A194,B194
A195,B195
A196,B196
A197,B197
A198,B198
A199,B199
A200,B200
A201,B201
A202,B202
A203,B203
A204,B204
A205,B205
A206,B206
A207,B207
A208,B208
A209,B209
A210,B210
A211,B211
A212,B212
A213,B213
A214,B214
A215,B215
A216,B216
A217,B217
A218,B218
A219,B219
A220,B220
A221,B221
A222,B222
A223,B223
A224,B224
A225,B225
A226,B226
A227,B227
A228,B228
A229,B229
A230,B230
A231,B231
A232,B232
A233,B233
A234,B234
A235,B235
A236,B236
A237,B237
A238,B238
A239,B239
A240,B240
A241,B241
A242,B242
A243,B243
A244,B244
A245,B245
A246,B246
A247,B247
A248,B248
A249,B249
A250,B250
A251,B251
A252,B252
A253,B253
A254,B254
A255,B255
A256,B256
A257,B257
A258,B258
A259,B259
A260,B260
A261,B261
A262,B262
A263,B263
A264,B264
A265,B265
A266,B266
A267,B267
A268,B268
A269,B269
A270,B270
A271,B271
A272,B272
A273,B273
A274,B274
A275,B275
A276,B276
A277,B277
A278,B278
A279,B279
A280,B280
A281,B281
A282,B282
A283,B283
A284,B284
A285,B285
A286,B286
A287,B287
A288,B288
A289,B289
A290,B290
A291,B291
A292,B292
A293,B293
A294,B294
A295,B295
A296,B296
A297,B297
A298,B298
A299,B299
A300,B300
A301,B301
A302,B302
A303,B303
A304,B304
A305,B305
A306,B306
A307,B307
A308,B308
A309,B309
A310,B310
A311,B311
A312,B312
A313,B313
A314,B314
A315,B315
A316,B316
A317,B317
A318,B318
A319,B319
A320,B320
A321,B321
A322,B322
A323,B323
A324,B324
A325,B325
A326,B326
A327,B327
A328,B328
A329,B329
A330,B330
A331,B331
A332,B332
A333,B333
A334,B334
A335,B335
A336,B336
A337,B337
A338,B338
A339,B339
A340,B340
A341,B341
A342,B342
A343,B343
A344,B344
A345,B345
A346,B346
A347,B347
A348,B348
A349,B349
A350,B350
A351,B351
A352,B352
A353,B353
A354,B354
A355,B355
A356,B356
A357,B357
A358,B358
A359,B359
A360,B360
A361,B361
A362,B362
A363,B363
A364,B364
A365,B365
A366,B366
A367,B367
A368,B368
A369,B369
A370,B370
A371,B371
A372,B372
A373,B373
A374,B374
A375,B375
A376,B376
A377,B377
A378,B378
A379,B379
A380,B380
A381,B381
A382,B382
A383,B383
A384,B384
A385,B385
A386,B386
A387,B387
A388,B388
A389,B389
A390,B390
A391,B391
A392,B392
A393,B393
A394,B394
A395,B395
A396,B396
A397,B397
A398,B398
A399,B399
A400,B400
A401,B401
A402,B402
A403,B403
A404,B404
A405,B405
A406,B406
A407,B407
A408,B408
A409,B409
A410,B410
A411,B411
A412,B412
A413,B413
A414,B414
A415,B415
A416,B416
A417,B417
A418,B418
A419,B419
A420,B420
A421,B421
A422,B422
A423,B423
A424,B424
A425,B425
A426,B426
A427,B427
A428,B428
A429,B429
A430,B430
A431,B431
A432,B432
A433,B433
A434,B434
A435,B435
A436,B436
A437,B437
A438,B438
A439,B439
A440,B440
A441,B441
A442,B442
A443,B443
A444,B444
A445,B445
A446,B446
A447,B447
A448,B448
A449,B449
A450,B450
A451,B451
A452,B452
A453,B453
A454,B454
A455,B455
A456,B456
A457,B457
A458,B458
A459,B459
A460,B460
A461,B461
A462,B462
A463,B463
A464,B464
A465,B465
A466,B466
A467,B467
A468,B468
A469,B469
A470,B470
A471,B471
A472,B472
A473,B473
A474,B474
A475,B475
A476,B476
A477,B477
A478,B478
A479,B479
A480,B480
A481,B481
A482,B482
A483,B483
A484,B484
A485,B485
A486,B486
A487,B487
A488,B488
A489,B489
A490,B490
A491,B491
A492,B492
A493,B493
A494,B494
A495,B495
A496,B496
A497,B497
A498,B498
A499,B499
A500,B500
A501,B501
A502,B502
A503,B503
A504,B504
A505,B505
A506,B506
A507,B507
A508,B508
A509,B509
A510,B510
A511,B511
A512,B512
A513,B513
A514,B514
A515,B515
A516,B516
A517,B517
A518,B518
A519,B519
A520,B520
A521,B521
A522,B522
A523,B523
A524,B524
A525,B525
A526,B526
A527,B527
A528,B528
A529,B529
A530,B530
A531,B531
A532,B532
A533,B533
A534,B534
A535,B535
A536,B536
A537,B537
A538,B538
A539,B539
A540,B540
A541,B541
A542,B542
A543,B543
A544,B544
A545,B545
A546,B546
A547,B547
A548,B548
A549,B549
A550,B550
A551,B551
A552,B552
A553,B553
A554,B554
A555,B555
A556,B556
A557,B557
A558,B558
A559,B559
A560,B560
A561,B561
A562,B562
A563,B563
A564,B564
A565,B565
A566,B566
A567,B567
A568,B568
A569,B569
A570,B570
A571,B571
A572,B572
A573,B573
A574,B574
A575,B575
A576,B576
A577,B577
A578,B578
A579,B579
A580,B580
A581,B581
A582,B582
A583,B583
A584,B584
A585,B585
A586,B586
A587,B587
A588,B588
A589,B589
A590,B590
A591,B591
A592,B592
A593,B593
A594,B594
A595,B595
A596,B596
A597,B597
A598,B598
A599,B599
A600,B600
A601,B601
A602,B602
A603,B603
A604,B604
A605,B605
A606,B606
A607,B607
A608,B608
A609,B609
A610,B610
A611,B611
A612,B612
A613,B613
A614,B614
A615,B615
A616,B616
A617,B617
A618,B618
A619,B619
A620,B620
A621,B621
A622,B622
A623,B623
A624,B624
A625,B625
A626,B626
A627,B627
A628,B628
A629,B629
A630,B630
A631,B631
A632,B632
A633,B633
A634,B634
A635,B635
A636,B636
A637,B637
A638,B638
A639,B639
A640,B640
A641,B641
A642,B642
A643,B643
A644,B644
A645,B645
A646,B646
A647,B647
A648,B648
A649,B649
A650,B650
A651,B651
A652,B652
A653,B653
A654,B654
A655,B655
A656,B656
A657,B657
A658,B658
A659,B659
A660,B660
A661,B661
A662,B662
A663,B663
A664,B664
A665,B665
A666,B666
A667,B667
A668,B668
A669,B669
A670,B670
A671,B671
A672,B672
A673,B673
A674,B674
A675,B675
A676,B676
A677,B677
A678,B678
A679,B679
A680,B680
A681,B681
A682,B682
A683,B683
A684,B684
A685,B685
A686,B686
A687,B687
A688,B688
A689,B689
A690,B690
A691,B691
A692,B692
A693,B693
A694,B694
A695,B695
A696,B696
A697,B697
A698,B698
A699,B699
A700,B700
A701,B701
A702,B702
A703,B703
A704,B704
A705,B705
A706,B706
A707,B707
A708,B708
A709,B709
A710,B710
A711,B711
A712,B712
A713,B713
A714,B714
A715,B715
A716,B716
A717,B717
A718,B718
A719,B719
A720,B720
A721,B721
A722,B722
A723,B723
A724,B724
A725,B725
A726,B726
A727,B727
A728,B728
A729,B729
A730,B730
A731,B731
A732,B732
A733,B733
A734,B734
A735,B735
A736,B736
A737,B737
A738,B738
A739,B739
A740,B740
A741,B741
A742,B742
A743,B743
A744,B744
A745,B745
A746,B746
A747,B747
A748,B748
A749,B749
A750,B750
A751,B751
A752,B752
A753,B753
A754,B754
A755,B755
A756,B756
A757,B757
A758,B758
A759,B759
A760,B760
A761,B761
A762,B762
A763,B763
A764,B764
A765,B765
A766,B766
A767,B767
A768,B768
A769,B769
A770,B770
A771,B771
A772,B772
A773,B773
A774,B774
A775,B775
A776,B776
A777,B777
A778,B778
A779,B779
A780,B780
A781,B781
A782,B782
A783,B783
A784,B784
A785,B785
A786,B786
A787,B787
A788,B788
A789,B789
A790,B790
A791,B791
A792,B792
A793,B793
A794,B794
A795,B795
A796,B796
A797,B797
A798,B798
A799,B799
A800,B800
A801,B801
A802,B802
A803,B803
A804,B804
A805,B805
A806,B806
A807,B807
A808,B808
A809,B809
A810,B810
A811,B811
A812,B812
A813,B813
A814,B814
A815,B815
A816,B816
A817,B817
A818,B818
A819,B819
A820,B820
A821,B821
A822,B822
A823,B823
A824,B824
A825,B825
A826,B826
A827,B827
A828,B828
A829,B829
A830,B830
A831,B831
A832,B832
A833,B833
A834,B834
A835,B835
A836,B836
A837,B837
A838,B838
A839,B839
A840,B840
A841,B841
A842,B842
A843,B843
A844,B844
A845,B845
A846,B846
A847,B847
A848,B848
A849,B849
A850,B850
A851,B851
A852,B852
A853,B853
A854,B854
A855,B855
A856,B856
A857,B857
A858,B858
A859,B859
A860,B860
A861,B861
A862,B862
A863,B863
A864,B864
A865,B865
A866,B866
A867,B867
A868,B868
A869,B869
A870,B870
A871,B871
A872,B872
A873,B873
A874,B874
A875,B875
A876,B876
A877,B877
A878,B878
A879,B879
A880,B880
A881,B881
A882,B882
A883,B883
A884,B884
A885,B885
A886,B886
A887,B887
A888,B888
A889,B889
A890,B890
A891,B891
A892,B892
A893,B893
A894,B894
A895,B895
A896,B896
A897,B897
A898,B898
A899,B899
A900,B900
A901,B901
A902,B902
A903,B903
A904,B904
A905,B905
A906,B906
A907,B907
A908,B908
A909,B909
A910,B910
A911,B911
A912,B912
A913,B913
A914,B914
A915,B915
A916,B916
A917,B917
A918,B918
A919,B919
A920,B920
A921,B921
A922,B922
A923,B923
A924,B924
A925,B925
A926,B926
A927,B927
A928,B928
A929,B929
A930,B930
A931,B931
A932,B932
A933,B933
A934,B934
A935,B935
A936,B936
A937,B937
A938,B938
A939,B939
A940,B940
A941,B941
A942,B942
A943,B943
A944,B944
A945,B945
A946,B946
A947,B947
A948,B948
A949,B949
A950,B950
A951,B951
A952,B952
A953,B953
A954,B954
A955,B955
A956,B956
A957,B957
A958,B958
A959,B959
A960,B960
A961,B961
A962,B962
A963,B963
A964,B964
A965,B965
A966,B966
A967,B967
A968,B968
A969,B969
A970,B970
A971,B971
A972,B972
A973,B973
A974,B974
A975,B975
A976,B976
A977,B977
A978,B978
A979,B979
A980,B980
A981,B981
A982,B982
A983,B983
A984,B984
A985,B985
A986,B986
A987,B987
A988,B988
A989,B989
A990,B990
A991,B991
A992,B992
A993,B993
A994,B994
A995,B995
A996,B996
A997,B997
A998,B998
A999,B999
A1000,B1000
A1001,B1001
A1002,B1002
A1003,B1003
A1004,B1004
A1005,B1005
A1006,B1006
A1007,B1007
A1008,B1008
A1009,B1009
A1010,B1010
A1011,B1011
A1012,B1012
A1013,B1013
A1014,B1014
A1015,B1015
A1016,B1016
A1017,B1017
A1018,B1018
A1019,B1019
A1020,B1020
A1021,B1021
A1022,B1022
A1023,B1023
A1024,B1024
A1025,B1025
A1026,B1026
A1027,B1027
A1028,B1028
A1029,B1029
A1030,B1030
A1031,B1031
A1032,B1032
A1033,B1033
A1034,B1034
A1035,B1035
A1036,B1036
A1037,B1037
A1038,B1038
A1039,B1039
A1040,B1040
A1041,B1041
A1042,B1042
A1043,B1043
A1044,B1044
A1045,B1045
A1046,B1046
A1047,B1047
A1048,B1048
A1049,B1049
A1050,B1050
A1051,B1051
A1052,B1052
A1053,B1053
A1054,B1054
A1055,B1055
A1056,B1056
A1057,B1057
A1058,B1058
A1059,B1059
A1060,B1060
A1061,B1061
A1062,B1062
A1063,B1063
A1064,B1064
A1065,B1065
A1066,B1066
A1067,B1067
A1068,B1068
A1069,B1069
A1070,B1070
A1071,B1071
A1072,B1072
A1073,B1073
A1074,B1074
A1075,B1075
A1076,B1076
A1077,B1077
A1078,B1078
A1079,B1079
A1080,B1080
A1081,B1081
A1082,B1082
A1083,B1083
A1084,B1084
A1085,B1085
A1086,B1086
A1087,B1087
A1088,B1088
A1089,B1089
A1090,B1090
A1091,B1091
A1092,B1092
A1093,B1093
A1094,B1094
A1095,B1095
A1096,B1096
A1097,B1097
A1098,B1098
A1099,B1099
A1100,B1100
A1101,B1101
A1102,B1102
A1103,B1103
A1104,B1104
A1105,B1105
A1106,B1106
A1107,B1107
A1108,B1108
A1109,B1109
A1110,B1110
A1111,B1111
A1112,B1112
A1113,B1113
A1114,B1114
A1115,B1115
A1116,B1116
A1117,B1117
A1118,B1118
A1119,B1119
A1120,B1120
A1121,B1121
A1122,B1122
A1123,B1123
A1124,B1124
A1125,B1125
A1126,B1126
A1127,B1127
A1128,B1128
A1129,B1129
A1130,B1130
A1131,B1131
A1132,B1132
A1133,B1133
A1134,B1134
A1135,B1135
A1136,B1136
A1137,B1137
A1138,B1138
A1139,B1139
A1140,B1140
A1141,B1141
A1142,B1142
A1143,B1143
A1144,B1144
A1145,B1145
A1146,B1146
A1147,B1147
A1148,B1148
A1149,B1149
A1150,B1150
A1151,B1151
A1152,B1152
A1153,B1153
A1154,B1154
A1155,B1155
A1156,B1156
A1157,B1157
A1158,B1158
A1159,B1159
A1160,B1160
A1161,B1161
A1162,B1162
A1163,B1163
A1164,B1164
A1165,B1165
A1166,B1166
A1167,B1167
A1168,B1168
A1169,B1169
A1170,B1170
A1171,B1171
A1172,B1172
A1173,B1173
A1174,B1174
A1175,B1175
A1176,B1176
A1177,B1177
A1178,B1178
A1179,B1179
A1180,B1180
A1181,B1181
A1182,B1182
A1183,B1183
A1184,B1184
A1185,B1185
A1186,B1186
A1187,B1187
A1188,B1188
A1189,B1189
A1190,B1190
A1191,B1191
A1192,B1192
A1193,B1193
A1194,B1194
A1195,B1195
A1196,B1196
A1197,B1197
A1198,B1198
A1199,B1199
A1200,B1200
A1201,B1201
A1202,B1202
A1203,B1203
A1204,B1204
A1205,B1205
A1206,B1206
A1207,B1207
A1208,B1208
A1209,B1209
A1210,B1210
A1211,B1211
A1212,B1212
A1213,B1213
A1214,B1214
A1215,B1215
A1216,B1216
A1217,B1217
A1218,B1218
A1219,B1219
A1220,B1220
A1221,B1221
A1222,B1222
A1223,B1223
A1224,B1224
A1225,B1225
A1226,B1226
A1227,B1227
A1228,B1228
A1229,B1229
A1230,B1230
A1231,B1231
A1232,B1232
A1233,B1233
A1234,B1234
A1235,B1235
A1236,B1236
A1237,B1237
A1238,B1238
A1239,B1239
A1240,B1240
A1241,B1241
A1242,B1242
A1243,B1243
A1244,B1244
A1245,B1245
A1246,B1246
A1247,B1247
A1248,B1248
A1249,B1249
A1250,B1250
A1251,B1251
A1252,B1252
A1253,B1253
A1254,B1254
A1255,B1255
A1256,B1256
A1257,B1257
A1258,B1258
A1259,B1259
A1260,B1260
A1261,B1261
A1262,B1262
A1263,B1263
A1264,B1264
A1265,B1265
A1266,B1266
A1267,B1267
A1268,B1268
A1269,B1269
A1270,B1270
A1271,B1271
A1272,B1272
A1273,B1273
A1274,B1274
A1275,B1275
A1276,B1276
A1277,B1277
A1278,B1278
A1279,B1279
A1280,B1280
A1281,B1281
A1282,B1282
A1283,B1283
A1284,B1284
A1285,B1285
A1286,B1286
A1287,B1287
A1288,B1288
A1289,B1289
A1290,B1290
A1291,B1291
A1292,B1292
A1293,B1293
A1294,B1294
A1295,B1295
A1296,B1296
A1297,B1297
A1298,B1298
A1299,B1299
A1300,B1300
A1301,B1301
A1302,B1302
A1303,B1303
A1304,B1304
A1305,B1305
A1306,B1306
A1307,B1307
A1308,B1308
A1309,B1309
A1310,B1310
A1311,B1311
A1312,B1312
A1313,B1313
A1314,B1314
A1315,B1315
A1316,B1316
A1317,B1317
A1318,B1318
A1319,B1319
A1320,B1320
A1321,B1321
A1322,B1322
A1323,B1323
A1324,B1324
A1325,B1325
A1326,B1326
A1327,B1327
A1328,B1328
A1329,B1329
A1330,B1330
A1331,B1331
A1332,B1332
A1333,B1333
A1334,B1334
A1335,B1335
A1336,B1336
A1337,B1337
A1338,B1338
A1339,B1339
A1340,B1340
A1341,B1341
A1342,B1342
A1343,B1343
A1344,B1344
A1345,B1345
A1346,B1346
A1347,B1347
A1348,B1348
A1349,B1349
A1350,B1350
A1351,B1351
A1352,B1352
A1353,B1353
A1354,B1354
A1355,B1355
A1356,B1356
A1357,B1357
A1358,B1358
A1359,B1359
A1360,B1360
A1361,B1361
A1362,B1362
A1363,B1363
A1364,B1364
A1365,B1365
A1366,B1366
A1367,B1367
A1368,B1368
A1369,B1369
A1370,B1370
A1371,B1371
A1372,B1372
A1373,B1373
A1374,B1374
A1375,B1375
A1376,B1376
A1377,B1377
A1378,B1378
A1379,B1379
A1380,B1380
A1381,B1381
A1382,B1382
A1383,B1383
A1384,B1384
A1385,B1385
A1386,B1386
A1387,B1387
A1388,B1388
A1389,B1389
A1390,B1390
A1391,B1391
A1392,B1392
A1393,B1393
A1394,B1394
A1395,B1395
A1396,B1396
A1397,B1397
A1398,B1398
A1399,B1399
A1400,B1400
A1401,B1401
A1402,B1402
A1403,B1403
A1404,B1404
A1405,B1405
A1406,B1406
A1407,B1407
A1408,B1408
A1409,B1409
A1410,B1410
A1411,B1411
A1412,B1412
A1413,B1413
A1414,B1414
A1415,B1415
A1416,B1416
A1417,B1417
A1418,B1418
A1419,B1419
A1420,B1420
A1421,B1421
A1422,B1422
A1423,B1423
A1424,B1424
A1425,B1425
A1426,B1426
A1427,B1427
A1428,B1428
A1429,B1429
A1430,B1430
A1431,B1431
A1432,B1432
A1433,B1433
A1434,B1434
A1435,B1435
A1436,B1436
A1437,B1437
A1438,B1438
A1439,B1439
A1440,B1440
A1441,B1441
A1442,B1442
A1443,B1443
A1444,B1444
A1445,B1445
A1446,B1446
A1447,B1447
A1448,B1448
A1449,B1449
A1450,B1450
A1451,B1451
A1452,B1452
A1453,B1453
A1454,B1454
A1455,B1455
A1456,B1456
A1457,B1457
A1458,B1458
A1459,B1459
A1460,B1460
A1461,B1461
A1462,B1462
A1463,B1463
A1464,B1464
A1465,B1465
A1466,B1466
A1467,B1467
A1468,B1468
A1469,B1469
A1470,B1470
A1471,B1471
A1472,B1472
A1473,B1473
A1474,B1474
A1475,B1475
A1476,B1476
A1477,B1477
A1478,B1478
A1479,B1479
A1480,B1480
A1481,B1481
A1482,B1482
A1483,B1483
A1484,B1484
A1485,B1485
A1486,B1486
A1487,B1487
A1488,B1488
A1489,B1489
A1490,B1490
A1491,B1491
A1492,B1492
A1493,B1493
A1494,B1494
A1495,B1495
A1496,B1496
A1497,B1497
A1498,B1498
A1499,B1499
A1500,B1500
A1501,B1501
A1502,B1502
A1503,B1503
A1504,B1504
A1505,B1505
A1506,B1506
A1507,B1507
A1508,B1508
A1509,B1509
A1510,B1510
A1511,B1511
A1512,B1512
A1513,B1513
A1514,B1514
A1515,B1515
A1516,B1516
A1517,B1517
A1518,B1518
A1519,B1519
A1520,B1520
A1521,B1521
A1522,B1522
A1523,B1523
A1524,B1524
A1525,B1525
A1526,B1526
A1527,B1527
A1528,B1528
A1529,B1529
A1530,B1530
A1531,B1531
A1532,B1532
A1533,B1533
A1534,B1534
A1535,B1535
A1536,B1536
A1537,B1537
A1538,B1538
A1539,B1539
A1540,B1540
A1541,B1541
A1542,B1542
A1543,B1543
A1544,B1544
A1545,B1545
A1546,B1546
A1547,B1547
A1548,B1548
A1549,B1549
A1550,B1550
A1551,B1551
A1552,B1552
A1553,B1553
A1554,B1554
A1555,B1555
A1556,B1556
A1557,B1557
A1558,B1558
A1559,B1559
A1560,B1560
A1561,B1561
A1562,B1562
A1563,B1563
A1564,B1564
A1565,B1565
A1566,B1566
A1567,B1567
A1568,B1568
A1569,B1569
A1570,B1570
A1571,B1571
A1572,B1572
A1573,B1573
A1574,B1574
A1575,B1575
A1576,B1576
A1577,B1577
A1578,B1578
A1579,B1579
A1580,B1580
A1581,B1581
A1582,B1582
A1583,B1583
A1584,B1584
A1585,B1585
A1586,B1586
A1587,B1587
A1588,B1588
A1589,B1589
A1590,B1590
A1591,B1591
A1592,B1592
A1593,B1593
A1594,B1594
A1595,B1595
A1596,B1596
A1597,B1597
A1598,B1598
A1599,B1599
A1600,B1600
A1601,B1601
A1602,B1602
A1603,B1603
A1604,B1604
A1605,B1605
A1606,B1606
A1607,B1607
A1608,B1608
A1609,B1609
A1610,B1610
A1611,B1611
A1612,B1612
A1613,B1613
A1614,B1614
A1615,B1615
A1616,B1616
A1617,B1617
A1618,B1618
A1619,B1619
A1620,B1620
A1621,B1621
A1622,B1622
A1623,B1623
A1624,B1624
A1625,B1625
A1626,B1626
A1627,B1627
A1628,B1628
A1629,B1629
A1630,B1630
A1631,B1631
A1632,B1632
A1633,B1633
A1634,B1634
A1635,B1635
A1636,B1636
A1637,B1637
A1638,B1638
A1639,B1639
A1640,B1640
A1641,B1641
A1642,B1642
A1643,B1643
A1644,B1644
A1645,B1645
A1646,B1646
A1647,B1647
A1648,B1648
A1649,B1649
A1650,B1650
A1651,B1651
A1652,B1652
A1653,B1653
A1654,B1654
A1655,B1655
A1656,B1656
A1657,B1657
A1658,B1658
A1659,B1659
A1660,B1660
A1661,B1661
A1662,B1662
A1663,B1663
A1664,B1664
A1665,B1665
A1666,B1666
A1667,B1667
A1668,B1668
A1669,B1669
A1670,B1670
A1671,B1671
A1672,B1672
A1673,B1673
A1674,B1674
A1675,B1675
A1676,B1676
A1677,B1677
A1678,B1678
A1679,B1679
A1680,B1680
A1681,B1681
A1682,B1682
A1683,B1683
A1684,B1684
A1685,B1685
A1686,B1686
A1687,B1687
A1688,B1688
A1689,B1689
A1690,B1690
A1691,B1691
A1692,B1692
A1693,B1693
A1694,B1694
A1695,B1695
A1696,B1696
A1697,B1697
A1698,B1698
A1699,B1699
A1700,B1700
A1701,B1701
A1702,B1702
A1703,B1703
A1704,B1704
A1705,B1705
A1706,B1706
A1707,B1707
A1708,B1708
A1709,B1709
A1710,B1710
A1711,B1711
A1712,B1712
A1713,B1713
A1714,B1714
A1715,B1715
A1716,B1716
A1717,B1717
A1718,B1718
A1719,B1719
A1720,B1720
A1721,B1721
A1722,B1722
A1723,B1723
A1724,B1724
A1725,B1725
A1726,B1726
A1727,B1727
A1728,B1728
A1729,B1729
A1730,B1730
A1731,B1731
A1732,B1732
A1733,B1733
A1734,B1734
A1735,B1735
A1736,B1736
A1737,B1737
A1738,B1738
A1739,B1739
A1740,B1740
A1741,B1741
A1742,B1742
A1743,B1743
A1744,B1744
A1745,B1745
A1746,B1746
A1747,B1747
A1748,B1748
A1749,B1749
A1750,B1750
A1751,B1751
A1752,B1752
A1753,B1753
A1754,B1754
A1755,B1755
A1756,B1756
A1757,B1757
A1758,B1758
A1759,B1759
A1760,B1760
A1761,B1761
A1762,B1762
A1763,B1763
A1764,B1764
A1765,B1765
A1766,B1766
A1767,B1767
A1768,B1768
A1769,B1769
A1770,B1770
A1771,B1771
A1772,B1772
A1773,B1773
A1774,B1774
A1775,B1775
A1776,B1776
A1777,B1777
A1778,B1778
A1779,B1779
A1780,B1780
A1781,B1781
A1782,B1782
A1783,B1783
A1784,B1784
A1785,B1785
A1786,B1786
A1787,B1787
A1788,B1788
A1789,B1789
A1790,B1790
A1791,B1791
A1792,B1792
A1793,B1793
A1794,B1794
A1795,B1795
A1796,B1796
A1797,B1797
A1798,B1798
A1799,B1799
A1800,B1800
A1801,B1801
A1802,B1802
A1803,B1803
A1804,B1804
A1805,B1805
A1806,B1806
A1807,B1807
A1808,B1808
A1809,B1809
A1810,B1810
A1811,B1811
A1812,B1812
A1813,B1813
A1814,B1814
A1815,B1815
A1816,B1816
A1817,B1817
A1818,B1818
A1819,B1819
A1820,B1820
A1821,B1821
A1822,B1822
A1823,B1823
A1824,B1824
A1825,B1825
A1826,B1826
A1827,B1827
A1828,B1828
A1829,B1829
A1830,B1830
A1831,B1831
A1832,B1832
A1833,B1833
A1834,B1834
A1835,B1835
A1836,B1836
A1837,B1837
A1838,B1838
A1839,B1839
A1840,B1840
A1841,B1841
A1842,B1842
A1843,B1843
A1844,B1844
A1845,B1845
A1846,B1846
A1847,B1847
A1848,B1848
A1849,B1849
A1850,B1850
A1851,B1851
A1852,B1852
A1853,B1853
A1854,B1854
A1855,B1855
A1856,B1856
A1857,B1857
A1858,B1858
A1859,B1859
A1860,B1860
A1861,B1861
A1862,B1862
A1863,B1863
A1864,B1864
A1865,B1865
A1866,B1866
A1867,B1867
A1868,B1868
A1869,B1869
A1870,B1870
A1871,B1871
A1872,B1872
A1873,B1873
A1874,B1874
A1875,B1875
A1876,B1876
A1877,B1877
A1878,B1878
A1879,B1879
A1880,B1880
A1881,B1881
A1882,B1882
A1883,B1883
A1884,B1884
A1885,B1885
A1886,B1886
A1887,B1887
A1888,B1888
A1889,B1889
A1890,B1890
A1891,B1891
A1892,B1892
A1893,B1893
A1894,B1894
A1895,B1895
A1896,B1896
A1897,B1897
A1898,B1898
A1899,B1899
A1900,B1900
A1901,B1901
A1902,B1902
A1903,B1903
A1904,B1904
A1905,B1905
A1906,B1906
A1907,B1907
A1908,B1908
A1909,B1909
A1910,B1910
A1911,B1911
A1912,B1912
A1913,B1913
A1914,B1914
A1915,B1915
A1916,B1916
A1917,B1917
A1918,B1918
A1919,B1919
A1920,B1920
A1921,B1921
A1922,B1922
A1923,B1923
A1924,B1924
A1925,B1925
A1926,B1926
A1927,B1927
A1928,B1928
A1929,B1929
A1930,B1930
A1931,B1931
A1932,B1932
A1933,B1933
A1934,B1934
A1935,B1935
A1936,B1936
A1937,B1937
A1938,B1938
A1939,B1939
A1940,B1940
A1941,B1941
A1942,B1942
A1943,B1943
A1944,B1944
A1945,B1945
A1946,B1946
A1947,B1947
A1948,B1948
A1949,B1949
A1950,B1950
A1951,B1951
A1952,B1952
A1953,B1953
A1954,B1954
A1955,B1955
A1956,B1956
A1957,B1957
A1958,B1958
A1959,B1959
A1960,B1960
A1961,B1961
A1962,B1962
A1963,B1963
A1964,B1964
A1965,B1965
A1966,B1966
A1967,B1967
A1968,B1968
A1969,B1969
A1970,B1970
A1971,B1971
A1972,B1972
A1973,B1973
A1974,B1974
A1975,B1975
A1976,B1976
A1977,B1977
A1978,B1978
A1979,B1979
A1980,B1980
A1981,B1981
A1982,B1982
A1983,B1983
A1984,B1984
A1985,B1985
A1986,B1986
A1987,B1987
A1988,B1988
A1989,B1989
A1990,B1990
A1991,B1991
A1992,B1992
A1993,B1993
A1994,B1994
A1995,B1995
A1996,B1996
A1997,B1997
A1998,B1998
A1999,B1999
A2000,B2000
A2001,B2001
A2002,B2002
A2003,B2003
A2004,B2004
A2005,B2005
A2006,B2006
A2007,B2007
A2008,B2008
A2009,B2009
A2010,B2010
A2011,B2011
A2012,B2012
A2013,B2013
A2014,B2014
A2015,B2015
A2016,B2016
A2017,B2017
A2018,B2018
A2019,B2019
A2020,B2020
A2021,B2021
A2022,B2022
A2023,B2023
A2024,B2024
A2025,B2025
A2026,B2026
A2027,B2027
A2028,B2028
A2029,B2029
A2030,B2030
A2031,B2031
A2032,B2032
A2033,B2033
A2034,B2034
A2035,B2035
A2036,B2036
A2037,B2037
A2038,B2038
A2039,B2039
A2040,B2040
A2041,B2041
A2042,B2042
A2043,B2043
A2044,B2044
A2045,B2045
A2046,B2046
A2047,B2047
A2048,B2048
A2049,B2049
A2050,B2050
A2051,B2051
A2052,B2052
A2053,B2053
A2054,B2054
A2055,B2055
A2056,B2056
A2057,B2057
A2058,B2058
A2059,B2059
A2060,B2060
A2061,B2061
A2062,B2062
A2063,B2063
A2064,B2064
A2065,B2065
A2066,B2066
A2067,B2067
A2068,B2068
A2069,B2069
A2070,B2070
A2071,B2071
A2072,B2072
A2073,B2073
A2074,B2074
A2075,B2075
A2076,B2076
A2077,B2077
A2078,B2078
A2079,B2079
A2080,B2080
A2081,B2081
A2082,B2082
A2083,B2083
A2084,B2084
A2085,B2085
A2086,B2086
A2087,B2087
A2088,B2088
A2089,B2089
A2090,B2090
A2091,B2091
A2092,B2092
A2093,B2093
A2094,B2094
A2095,B2095
A2096,B2096
A2097,B2097
A2098,B2098
A2099,B2099
A2100,B2100
A2101,B2101
A2102,B2102
A2103,B2103
A2104,B2104
A2105,B2105
A2106,B2106
A2107,B2107
A2108,B2108
A2109,B2109
A2110,B2110
A2111,B2111
A2112,B2112
A2113,B2113
A2114,B2114
A2115,B2115
A2116,B2116
A2117,B2117
A2118,B2118
A2119,B2119
A2120,B2120
A2121,B2121
A2122,B2122
A2123,B2123
A2124,B2124
A2125,B2125
A2126,B2126
A2127,B2127
A2128,B2128
A2129,B2129
A2130,B2130
A2131,B2131
A2132,B2132
A2133,B2133
A2134,B2134
A2135,B2135
A2136,B2136
A2137,B2137
A2138,B2138
A2139,B2139
A2140,B2140
A2141,B2141
A2142,B2142
A2143,B2143
A2144,B2144
A2145,B2145
A2146,B2146
A2147,B2147
A2148,B2148
A2149,B2149
A2150,B2150
A2151,B2151
A2152,B2152
A2153,B2153
A2154,B2154
A2155,B2155
A2156,B2156
A2157,B2157
A2158,B2158
A2159,B2159
A2160,B2160
A2161,B2161
A2162,B2162
A2163,B2163
A2164,B2164
A2165,B2165
A2166,B2166
A2167,B2167
A2168,B2168
A2169,B2169
A2170,B2170
A2171,B2171
A2172,B2172
A2173,B2173
A2174,B2174
A2175,B2175
A2176,B2176
A2177,B2177
A2178,B2178
A2179,B2179
A2180,B2180
A2181,B2181
A2182,B2182
A2183,B2183
A2184,B2184
A2185,B2185
A2186,B2186
A2187,B2187
A2188,B2188
A2189,B2189
A2190,B2190
A2191,B2191
A2192,B2192
A2193,B2193
A2194,B2194
A2195,B2195
A2196,B2196
A2197,B2197
A2198,B2198
A2199,B2199
A2200,B2200
A2201,B2201
A2202,B2202
A2203,B2203
A2204,B2204
A2205,B2205
A2206,B2206
A2207,B2207
A2208,B2208
A2209,B2209
A2210,B2210
A2211,B2211
A2212,B2212
A2213,B2213
A2214,B2214
A2215,B2215
A2216,B2216
A2217,B2217
A2218,B2218
A2219,B2219
A2220,B2220
A2221,B2221
A2222,B2222
A2223,B2223
A2224,B2224
A2225,B2225
A2226,B2226
A2227,B2227
A2228,B2228
A2229,B2229
A2230,B2230
A2231,B2231
A2232,B2232
A2233,B2233
A2234,B2234
A2235,B2235
A2236,B2236
A2237,B2237
A2238,B2238
A2239,B2239
A2240,B2240
A2241,B2241
A2242,B2242
A2243,B2243
A2244,B2244
A2245,B2245
A2246,B2246
A2247,B2247
A2248,B2248
A2249,B2249
A2250,B2250
A2251,B2251
A2252,B2252
A2253,B2253
A2254,B2254
A2255,B2255
A2256,B2256
A2257,B2257
A2258,B2258
A2259,B2259
A2260,B2260
A2261,B2261
A2262,B2262
A2263,B2263
A2264,B2264
A2265,B2265
A2266,B2266
A2267,B2267
A2268,B2268
A2269,B2269
A2270,B2270
A2271,B2271
A2272,B2272
A2273,B2273
A2274,B2274
A2275,B2275
A2276,B2276
A2277,B2277
A2278,B2278
A2279,B2279
A2280,B2280
A2281,B2281
A2282,B2282
A2283,B2283
A2284,B2284
A2285,B2285
A2286,B2286
A2287,B2287
A2288,B2288
A2289,B2289
A2290,B2290
A2291,B2291
A2292,B2292
A2293,B2293
A2294,B2294
A2295,B2295
A2296,B2296
A2297,B2297
A2298,B2298
A2299,B2299
A2300,B2300
A2301,B2301
A2302,B2302
A2303,B2303
A2304,B2304
A2305,B2305
A2306,B2306
A2307,B2307
A2308,B2308
A2309,B2309
A2310,B2310
A2311,B2311
A2312,B2312
A2313,B2313
A2314,B2314
A2315,B2315
A2316,B2316
A2317,B2317
A2318,B2318
A2319,B2319
A2320,B2320
A2321,B2321
A2322,B2322
A2323,B2323
A2324,B2324
A2325,B2325
A2326,B2326
A2327,B2327
A2328,B2328
A2329,B2329
A2330,B2330
A2331,B2331
A2332,B2332
A2333,B2333
A2334,B2334
A2335,B2335
A2336,B2336
A2337,B2337
A2338,B2338
A2339,B2339
A2340,B2340
A2341,B2341
A2342,B2342
A2343,B2343
A2344,B2344
A2345,B2345
A2346,B2346
A2347,B2347
A2348,B2348
A2349,B2349
A2350,B2350
A2351,B2351
A2352,B2352
A2353,B2353
A2354,B2354
A2355,B2355
A2356,B2356
A2357,B2357
A2358,B2358
A2359,B2359
A2360,B2360
A2361,B2361
A2362,B2362
A2363,B2363
A2364,B2364
A2365,B2365
A2366,B2366
A2367,B2367
A2368,B2368
A2369,B2369
A2370,B2370
A2371,B2371
A2372,B2372
A2373,B2373
A2374,B2374
A2375,B2375
A2376,B2376
A2377,B2377
A2378,B2378
A2379,B2379
A2380,B2380
A2381,B2381
A2382,B2382
A2383,B2383
A2384,B2384
A2385,B2385
A2386,B2386
A2387,B2387
A2388,B2388
A2389,B2389
A2390,B2390
A2391,B2391
A2392,B2392
A2393,B2393
A2394,B2394
A2395,B2395
A2396,B2396
A2397,B2397
A2398,B2398
A2399,B2399
A2400,B2400
A2401,B2401
A2402,B2402
A2403,B2403
A2404,B2404
A2405,B2405
A2406,B2406
A2407,B2407
A2408,B2408
A2409,B2409
A2410,B2410
A2411,B2411
A2412,B2412
A2413,B2413
A2414,B2414
A2415,B2415
A2416,B2416
A2417,B2417
A2418,B2418
A2419,B2419
A2420,B2420
A2421,B2421
A2422,B2422
A2423,B2423
A2424,B2424
A2425,B2425
A2426,B2426
A2427,B2427
A2428,B2428
A2429,B2429
A2430,B2430
A2431,B2431
A2432,B2432
A2433,B2433
A2434,B2434
A2435,B2435
A2436,B2436
A2437,B2437
A2438,B2438
A2439,B2439
A2440,B2440
A2441,B2441
A2442,B2442
A2443,B2443
A2444,B2444
A2445,B2445
A2446,B2446
A2447,B2447
A2448,B2448
A2449,B2449
A2450,B2450
A2451,B2451
A2452,B2452
A2453,B2453
A2454,B2454
A2455,B2455
A2456,B2456
A2457,B2457
A2458,B2458
A2459,B2459
A2460,B2460
A2461,B2461
A2462,B2462
A2463,B2463
A2464,B2464
A2465,B2465
A2466,B2466
A2467,B2467
A2468,B2468
A2469,B2469
A2470,B2470
A2471,B2471
A2472,B2472
A2473,B2473
A2474,B2474
A2475,B2475
A2476,B2476
A2477,B2477
A2478,B2478
A2479,B2479
A2480,B2480
A2481,B2481
A2482,B2482
A2483,B2483
A2484,B2484
A2485,B2485
A2486,B2486
A2487,B2487
A2488,B2488
A2489,B2489
A2490,B2490
A2491,B2491
A2492,B2492
A2493,B2493
A2494,B2494
A2495,B2495
A2496,B2496
A2497,B2497
A2498,B2498
A2499,B2499
A2500,B2500
A2501,B2501
A2502,B2502
A2503,B2503
A2504,B2504
A2505,B2505
A2506,B2506
A2507,B2507
A2508,B2508
A2509,B2509
A2510,B2510
A2511,B2511
A2512,B2512
A2513,B2513
A2514,B2514
A2515,B2515
A2516,B2516
A2517,B2517
A2518,B2518
A2519,B2519
A2520,B2520
A2521,B2521
A2522,B2522
A2523,B2523
A2524,B2524
A2525,B2525
A2526,B2526
A2527,B2527
A2528,B2528
A2529,B2529
A2530,B2530
A2531,B2531
A2532,B2532
A2533,B2533
A2534,B2534
A2535,B2535
A2536,B2536
A2537,B2537
A2538,B2538
A2539,B2539
A2540,B2540
A2541,B2541
A2542,B2542
A2543,B2543
A2544,B2544
A2545,B2545
A2546,B2546
A2547,B2547
A2548,B2548
A2549,B2549
A2550,B2550
A2551,B2551
A2552,B2552
A2553,B2553
A2554,B2554
A2555,B2555
A2556,B2556
A2557,B2557
A2558,B2558
A2559,B2559
A2560,B2560
A2561,B2561
A2562,B2562
A2563,B2563
A2564,B2564
A2565,B2565
A2566,B2566
A2567,B2567
A2568,B2568
A2569,B2569
A2570,B2570
A2571,B2571
A2572,B2572
A2573,B2573
A2574,B2574
A2575,B2575
A2576,B2576
A2577,B2577
A2578,B2578
A2579,B2579
A2580,B2580
A2581,B2581
A2582,B2582
A2583,B2583
A2584,B2584
A2585,B2585
A2586,B2586
A2587,B2587
A2588,B2588
A2589,B2589
A2590,B2590
A2591,B2591
A2592,B2592
A2593,B2593
A2594,B2594
A2595,B2595
A2596,B2596
A2597,B2597
A2598,B2598
A2599,B2599
A2600,B2600
A2601,B2601
A2602,B2602
A2603,B2603
A2604,B2604
A2605,B2605
A2606,B2606
A2607,B2607
A2608,B2608
A2609,B2609
A2610,B2610
A2611,B2611
A2612,B2612
A2613,B2613
A2614,B2614
A2615,B2615
A2616,B2616
A2617,B2617
A2618,B2618
A2619,B2619
A2620,B2620
A2621,B2621
A2622,B2622
A2623,B2623
A2624,B2624
A2625,B2625
A2626,B2626
A2627,B2627
A2628,B2628
A2629,B2629
A2630,B2630
A2631,B2631
A2632,B2632
A2633,B2633
A2634,B2634
A2635,B2635
A2636,B2636
A2637,B2637
A2638,B2638
A2639,B2639
A2640,B2640
A2641,B2641
A2642,B2642
A2643,B2643
A2644,B2644
A2645,B2645
A2646,B2646
A2647,B2647
A2648,B2648
A2649,B2649
A2650,B2650
A2651,B2651
A2652,B2652
A2653,B2653
A2654,B2654
A2655,B2655
A2656,B2656
A2657,B2657
A2658,B2658
A2659,B2659
A2660,B2660
A2661,B2661
A2662,B2662
A2663,B2663
A2664,B2664
A2665,B2665
A2666,B2666
A2667,B2667
A2668,B2668
A2669,B2669
A2670,B2670
A2671,B2671
A2672,B2672
A2673,B2673
A2674,B2674
A2675,B2675
A2676,B2676
A2677,B2677
A2678,B2678
A2679,B2679
A2680,B2680
A2681,B2681
A2682,B2682
A2683,B2683
A2684,B2684
A2685,B2685
A2686,B2686
A2687,B2687
A2688,B2688
A2689,B2689
A2690,B2690
A2691,B2691
A2692,B2692
A2693,B2693
A2694,B2694
A2695,B2695
A2696,B2696
A2697,B2697
A2698,B2698
A2699,B2699
A2700,B2700
A2701,B2701
A2702,B2702
A2703,B2703
A2704,B2704
A2705,B2705
A2706,B2706
A2707,B2707
A2708,B2708
A2709,B2709
A2710,B2710
A2711,B2711
A2712,B2712
A2713,B2713
A2714,B2714
A2715,B2715
A2716,B2716
A2717,B2717
A2718,B2718
A2719,B2719
A2720,B2720
A2721,B2721
A2722,B2722
A2723,B2723
A2724,B2724
A2725,B2725
A2726,B2726
A2727,B2727
A2728,B2728
A2729,B2729
A2730,B2730
A2731,B2731
A2732,B2732
A2733,B2733
A2734,B2734
A2735,B2735
A2736,B2736
A2737,B2737
A2738,B2738
A2739,B2739
A2740,B2740
A2741,B2741
A2742,B2742
A2743,B2743
A2744,B2744
A2745,B2745
A2746,B2746
A2747,B2747
A2748,B2748
A2749,B2749
A2750,B2750
A2751,B2751
A2752,B2752
A2753,B2753
A2754,B2754
A2755,B2755
A2756,B2756
A2757,B2757
A2758,B2758
A2759,B2759
A2760,B2760
A2761,B2761
A2762,B2762
A2763,B2763
A2764,B2764
A2765,B2765
A2766,B2766
A2767,B2767
A2768,B2768
A2769,B2769
A2770,B2770
A2771,B2771
A2772,B2772
A2773,B2773
A2774,B2774
A2775,B2775
A2776,B2776
A2777,B2777
A2778,B2778
A2779,B2779
A2780,B2780
A2781,B2781
A2782,B2782
A2783,B2783
A2784,B2784
A2785,B2785
A2786,B2786
A2787,B2787
A2788,B2788
A2789,B2789
A2790,B2790
A2791,B2791
A2792,B2792
A2793,B2793
A2794,B2794
A2795,B2795
A2796,B2796
A2797,B2797
A2798,B2798
A2799,B2799
A2800,B2800
A2801,B2801
A2802,B2802
A2803,B2803
A2804,B2804
A2805,B2805
A2806,B2806
A2807,B2807
A2808,B2808
A2809,B2809
A2810,B2810
A2811,B2811
A2812,B2812
A2813,B2813
A2814,B2814
A2815,B2815
A2816,B2816
A2817,B2817
A2818,B2818
A2819,B2819
A2820,B2820
A2821,B2821
A2822,B2822
A2823,B2823
A2824,B2824
A2825,B2825
A2826,B2826
A2827,B2827
A2828,B2828
A2829,B2829
A2830,B2830
A2831,B2831
A2832,B2832
A2833,B2833
A2834,B2834
A2835,B2835
A2836,B2836
A2837,B2837
A2838,B2838
A2839,B2839
A2840,B2840
A2841,B2841
A2842,B2842
A2843,B2843
A2844,B2844
A2845,B2845
A2846,B2846
A2847,B2847
A2848,B2848
A2849,B2849
A2850,B2850
A2851,B2851
A2852,B2852
A2853,B2853
A2854,B2854
A2855,B2855
A2856,B2856
A2857,B2857
A2858,B2858
A2859,B2859
A2860,B2860
A2861,B2861
A2862,B2862
A2863,B2863
A2864,B2864
A2865,B2865
A2866,B2866
A2867,B2867
A2868,B2868
A2869,B2869
A2870,B2870
A2871,B2871
A2872,B2872
A2873,B2873
A2874,B2874
A2875,B2875
A2876,B2876
A2877,B2877
A2878,B2878
A2879,B2879
A2880,B2880
A2881,B2881
A2882,B2882
A2883,B2883
A2884,B2884
A2885,B2885
A2886,B2886
A2887,B2887
A2888,B2888
A2889,B2889
A2890,B2890
A2891,B2891
A2892,B2892
A2893,B2893
A2894,B2894
A2895,B2895
A2896,B2896
A2897,B2897
A2898,B2898
A2899,B2899
A2900,B2900
A2901,B2901
A2902,B2902
A2903,B2903
A2904,B2904
A2905,B2905
A2906,B2906
A2907,B2907
A2908,B2908
A2909,B2909
A2910,B2910
A2911,B2911
A2912,B2912
A2913,B2913
A2914,B2914
A2915,B2915
A2916,B2916
A2917,B2917
A2918,B2918
A2919,B2919
A2920,B2920
A2921,B2921
A2922,B2922
A2923,B2923
A2924,B2924
A2925,B2925
A2926,B2926
A2927,B2927
A2928,B2928
A2929,B2929
A2930,B2930
A2931,B2931
A2932,B2932
A2933,B2933
A2934,B2934
A2935,B2935
A2936,B2936
A2937,B2937
A2938,B2938
A2939,B2939
A2940,B2940
A2941,B2941
A2942,B2942
A2943,B2943
A2944,B2944
A2945,B2945
A2946,B2946
A2947,B2947
A2948,B2948
A2949,B2949
A2950,B2950
A2951,B2951
A2952,B2952
A2953,B2953
A2954,B2954
A2955,B2955
A2956,B2956
A2957,B2957
A2958,B2958
A2959,B2959
A2960,B2960
A2961,B2961
A2962,B2962
A2963,B2963
A2964,B2964
A2965,B2965
A2966,B2966
A2967,B2967
A2968,B2968
A2969,B2969
A2970,B2970
A2971,B2971
A2972,B2972
A2973,B2973
A2974,B2974
A2975,B2975
A2976,B2976
A2977,B2977
A2978,B2978
A2979,B2979
A2980,B2980
A2981,B2981
A2982,B2982
A2983,B2983
A2984,B2984
A2985,B2985
A2986,B2986
A2987,B2987
A2988,B2988
A2989,B2989
A2990,B2990
A2991,B2991
A2992,B2992
A2993,B2993
A2994,B2994
A2995,B2995
A2996,B2996
A2997,B2997
A2998,B2998
A2999,B2999
A3000,B3000
A3001,B3001
A3002,B3002
A3003,B3003
A3004,B3004
A3005,B3005
A3006,B3006
A3007,B3007
A3008,B3008
A3009,B3009
A3010,B3010
A3011,B3011
A3012,B3012
A3013,B3013
A3014,B3014
A3015,B3015
A3016,B3016
A3017,B3017
A3018,B3018
A3019,B3019
A3020,B3020
A3021,B3021
A3022,B3022
A3023,B3023
A3024,B3024
A3025,B3025
A3026,B3026
A3027,B3027
A3028,B3028
A3029,B3029
A3030,B3030
A3031,B3031
A3032,B3032
A3033,B3033
A3034,B3034
A3035,B3035
A3036,B3036
A3037,B3037
A3038,B3038
A3039,B3039
A3040,B3040
A3041,B3041
A3042,B3042
A3043,B3043
A3044,B3044
A3045,B3045
A3046,B3046
A3047,B3047
A3048,B3048
A3049,B3049
A3050,B3050
A3051,B3051
A3052,B3052
A3053,B3053
A3054,B3054
A3055,B3055
A3056,B3056
A3057,B3057
A3058,B3058
A3059,B3059
A3060,B3060
A3061,B3061
A3062,B3062
A3063,B3063
A3064,B3064
A3065,B3065
A3066,B3066
A3067,B3067
A3068,B3068
A3069,B3069
A3070,B3070
A3071,B3071
A3072,B3072
A3073,B3073
A3074,B3074
A3075,B3075
A3076,B3076
A3077,B3077
A3078,B3078
A3079,B3079
A3080,B3080
A3081,B3081
A3082,B3082
A3083,B3083
A3084,B3084
A3085,B3085
A3086,B3086
A3087,B3087
A3088,B3088
A3089,B3089
A3090,B3090
A3091,B3091
A3092,B3092
A3093,B3093
A3094,B3094
A3095,B3095
A3096,B3096
A3097,B3097
A3098,B3098
A3099,B3099
A3100,B3100
A3101,B3101
A3102,B3102
A3103,B3103
A3104,B3104
A3105,B3105
A3106,B3106
A3107,B3107
A3108,B3108
A3109,B3109
A3110,B3110
A3111,B3111
A3112,B3112
A3113,B3113
A3114,B3114
A3115,B3115
A3116,B3116
A3117,B3117
A3118,B3118
A3119,B3119
A3120,B3120
A3121,B3121
A3122,B3122
A3123,B3123
A3124,B3124
A3125,B3125
A3126,B3126
A3127,B3127
A3128,B3128
A3129,B3129
A3130,B3130
A3131,B3131
A3132,B3132
A3133,B3133
A3134,B3134
A3135,B3135
A3136,B3136
A3137,B3137
A3138,B3138
A3139,B3139
A3140,B3140
A3141,B3141
A3142,B3142
A3143,B3143
A3144,B3144
A3145,B3145
A3146,B3146
A3147,B3147
A3148,B3148
A3149,B3149
A3150,B3150
A3151,B3151
A3152,B3152
A3153,B3153
A3154,B3154
A3155,B3155
A3156,B3156
A3157,B3157
A3158,B3158
A3159,B3159
A3160,B3160
A3161,B3161
A3162,B3162
A3163,B3163
A3164,B3164
A3165,B3165
A3166,B3166
A3167,B3167
A3168,B3168
A3169,B3169
A3170,B3170
A3171,B3171
A3172,B3172
A3173,B3173
A3174,B3174
A3175,B3175
A3176,B3176
A3177,B3177
A3178,B3178
A3179,B3179
A3180,B3180
A3181,B3181
A3182,B3182
A3183,B3183
A3184,B3184
A3185,B3185
A3186,B3186
A3187,B3187
A3188,B3188
A3189,B3189
A3190,B3190
A3191,B3191
A3192,B3192
A3193,B3193
A3194,B3194
A3195,B3195
A3196,B3196
A3197,B3197
A3198,B3198
A3199,B3199
A3200,B3200
A3201,B3201
A3202,B3202
A3203,B3203
A3204,B3204
A3205,B3205
A3206,B3206
A3207,B3207
A3208,B3208
A3209,B3209
A3210,B3210
A3211,B3211
A3212,B3212
A3213,B3213
A3214,B3214
A3215,B3215
A3216,B3216
A3217,B3217
A3218,B3218
A3219,B3219
A3220,B3220
A3221,B3221
A3222,B3222
A3223,B3223
A3224,B3224
A3225,B3225
A3226,B3226
A3227,B3227
A3228,B3228
A3229,B3229
A3230,B3230
A3231,B3231
A3232,B3232
A3233,B3233
A3234,B3234
A3235,B3235
A3236,B3236
A3237,B3237
A3238,B3238
A3239,B3239
A3240,B3240
A3241,B3241
A3242,B3242
A3243,B3243
A3244,B3244
A3245,B3245
A3246,B3246
A3247,B3247
A3248,B3248
A3249,B3249
A3250,B3250
A3251,B3251
A3252,B3252
A3253,B3253
A3254,B3254
A3255,B3255
A3256,B3256
A3257,B3257
A3258,B3258
A3259,B3259
A3260,B3260
A3261,B3261
A3262,B3262
A3263,B3263
A3264,B3264
A3265,B3265
A3266,B3266
A3267,B3267
A3268,B3268
A3269,B3269
A3270,B3270
A3271,B3271
A3272,B3272
A3273,B3273
A3274,B3274
A3275,B3275
A3276,B3276
A3277,B3277
A3278,B3278
A3279,B3279
A3280,B3280
A3281,B3281
A3282,B3282
A3283,B3283
A3284,B3284
A3285,B3285
A3286,B3286
A3287,B3287
A3288,B3288
A3289,B3289
A3290,B3290
A3291,B3291
A3292,B3292
A3293,B3293
A3294,B3294
A3295,B3295
A3296,B3296
A3297,B3297
A3298,B3298
A3299,B3299
A3300,B3300
A3301,B3301
A3302,B3302
A3303,B3303
A3304,B3304
A3305,B3305
A3306,B3306
A3307,B3307
A3308,B3308
A3309,B3309
A3310,B3310
A3311,B3311
A3312,B3312
A3313,B3313
A3314,B3314
A3315,B3315
A3316,B3316
A3317,B3317
A3318,B3318
A3319,B3319
A3320,B3320
A3321,B3321
A3322,B3322
A3323,B3323
A3324,B3324
A3325,B3325
A3326,B3326
A3327,B3327
A3328,B3328
A3329,B3329
A3330,B3330
A3331,B3331
A3332,B3332
A3333,B3333
A3334,B3334
A3335,B3335
A3336,B3336
A3337,B3337
A3338,B3338
A3339,B3339
A3340,B3340
A3341,B3341
A3342,B3342
A3343,B3343
A3344,B3344
A3345,B3345
A3346,B3346
A3347,B3347
A3348,B3348
A3349,B3349
A3350,B3350
A3351,B3351
A3352,B3352
A3353,B3353
A3354,B3354
A3355,B3355
A3356,B3356
A3357,B3357
A3358,B3358
A3359,B3359
A3360,B3360
A3361,B3361
A3362,B3362
A3363,B3363
A3364,B3364
A3365,B3365
A3366,B3366
A3367,B3367
A3368,B3368
A3369,B3369
A3370,B3370
A3371,B3371
A3372,B3372
A3373,B3373
A3374,B3374
A3375,B3375
A3376,B3376
A3377,B3377
A3378,B3378
A3379,B3379
A3380,B3380
A3381,B3381
A3382,B3382
A3383,B3383
A3384,B3384
A3385,B3385
A3386,B3386
A3387,B3387
A3388,B3388
A3389,B3389
A3390,B3390
A3391,B3391
A3392,B3392
A3393,B3393
A3394,B3394
A3395,B3395
A3396,B3396
A3397,B3397
A3398,B3398
A3399,B3399
A3400,B3400
A3401,B3401
A3402,B3402
A3403,B3403
A3404,B3404
A3405,B3405
A3406,B3406
A3407,B3407
A3408,B3408
A3409,B3409
A3410,B3410
A3411,B3411
A3412,B3412
A3413,B3413
A3414,B3414
A3415,B3415
A3416,B3416
A3417,B3417
A3418,B3418
A3419,B3419
A3420,B3420
A3421,B3421
A3422,B3422
A3423,B3423
A3424,B3424
A3425,B3425
A3426,B3426
A3427,B3427
A3428,B3428
A3429,B3429
A3430,B3430
A3431,B3431
A3432,B3432
A3433,B3433
A3434,B3434
A3435,B3435
A3436,B3436
A3437,B3437
A3438,B3438
A3439,B3439
A3440,B3440
A3441,B3441
A3442,B3442
A3443,B3443
A3444,B3444
A3445,B3445
A3446,B3446
A3447,B3447
A3448,B3448
A3449,B3449
A3450,B3450
A3451,B3451
A3452,B3452
A3453,B3453
A3454,B3454
A3455,B3455
A3456,B3456
A3457,B3457
A3458,B3458
A3459,B3459
A3460,B3460
A3461,B3461
A3462,B3462
A3463,B3463
A3464,B3464
A3465,B3465
A3466,B3466
A3467,B3467
A3468,B3468
A3469,B3469
A3470,B3470
A3471,B3471
A3472,B3472
A3473,B3473
A3474,B3474
A3475,B3475
A3476,B3476
A3477,B3477
A3478,B3478
A3479,B3479
A3480,B3480
A3481,B3481
A3482,B3482
A3483,B3483
A3484,B3484
A3485,B3485
A3486,B3486
A3487,B3487
A3488,B3488
A3489,B3489
A3490,B3490
A3491,B3491
A3492,B3492
A3493,B3493
A3494,B3494
A3495,B3495
A3496,B3496
A3497,B3497
A3498,B3498
A3499,B3499
A3500,B3500
A3501,B3501
A3502,B3502
A3503,B3503
A3504,B3504
A3505,B3505
A3506,B3506
A3507,B3507
A3508,B3508
A3509,B3509
A3510,B3510
A3511,B3511
A3512,B3512
A3513,B3513
A3514,B3514
A3515,B3515
A3516,B3516
A3517,B3517
A3518,B3518
A3519,B3519
A3520,B3520
A3521,B3521
A3522,B3522
A3523,B3523
A3524,B3524
A3525,B3525
A3526,B3526
A3527,B3527
A3528,B3528
A3529,B3529
A3530,B3530
A3531,B3531
A3532,B3532
A3533,B3533
A3534,B3534
A3535,B3535
A3536,B3536
A3537,B3537
A3538,B3538
A3539,B3539
A3540,B3540
A3541,B3541
A3542,B3542
A3543,B3543
A3544,B3544
A3545,B3545
A3546,B3546
A3547,B3547
A3548,B3548
A3549,B3549
A3550,B3550
A3551,B3551
A3552,B3552
A3553,B3553
A3554,B3554
A3555,B3555
A3556,B3556
A3557,B3557
A3558,B3558
A3559,B3559
A3560,B3560
A3561,B3561
A3562,B3562
A3563,B3563
A3564,B3564
A3565,B3565
A3566,B3566
A3567,B3567
A3568,B3568
A3569,B3569
A3570,B3570
A3571,B3571
A3572,B3572
A3573,B3573
A3574,B3574
A3575,B3575
A3576,B3576
A3577,B3577
A3578,B3578
A3579,B3579
A3580,B3580
A3581,B3581
A3582,B3582
A3583,B3583
A3584,B3584
A3585,B3585
A3586,B3586
A3587,B3587
A3588,B3588
A3589,B3589
A3590,B3590
A3591,B3591
A3592,B3592
A3593,B3593
A3594,B3594
A3595,B3595
A3596,B3596
A3597,B3597
A3598,B3598
A3599,B3599
A3600,B3600
A3601,B3601
A3602,B3602
A3603,B3603
A3604,B3604
A3605,B3605
A3606,B3606
A3607,B3607
A3608,B3608
A3609,B3609
A3610,B3610
A3611,B3611
A3612,B3612
A3613,B3613
A3614,B3614
A3615,B3615
A3616,B3616
A3617,B3617
A3618,B3618
A3619,B3619
A3620,B3620
A3621,B3621
A3622,B3622
A3623,B3623
A3624,B3624
A3625,B3625
A3626,B3626
A3627,B3627
A3628,B3628
A3629,B3629
A3630,B3630
A3631,B3631
A3632,B3632
A3633,B3633
A3634,B3634
A3635,B3635
A3636,B3636
A3637,B3637
A3638,B3638
A3639,B3639
A3640,B3640
A3641,B3641
A3642,B3642
A3643,B3643
A3644,B3644
A3645,B3645
A3646,B3646
A3647,B3647
A3648,B3648
A3649,B3649
A3650,B3650
A3651,B3651
A3652,B3652
A3653,B3653
A3654,B3654
A3655,B3655
A3656,B3656
A3657,B3657
A3658,B3658
A3659,B3659
A3660,B3660
A3661,B3661
A3662,B3662
A3663,B3663
A3664,B3664
A3665,B3665
A3666,B3666
A3667,B3667
A3668,B3668
A3669,B3669
A3670,B3670
A3671,B3671
A3672,B3672
A3673,B3673
A3674,B3674
A3675,B3675
A3676,B3676
A3677,B3677
A3678,B3678
A3679,B3679
A3680,B3680
A3681,B3681
A3682,B3682
A3683,B3683
A3684,B3684
A3685,B3685
A3686,B3686
A3687,B3687
A3688,B3688
A3689,B3689
A3690,B3690
A3691,B3691
A3692,B3692
A3693,B3693
A3694,B3694
A3695,B3695
A3696,B3696
A3697,B3697
A3698,B3698
A3699,B3699
A3700,B3700
A3701,B3701
A3702,B3702
A3703,B3703
A3704,B3704
A3705,B3705
A3706,B3706
A3707,B3707
A3708,B3708
A3709,B3709
A3710,B3710
A3711,B3711
A3712,B3712
A3713,B3713
A3714,B3714
A3715,B3715
A3716,B3716
A3717,B3717
A3718,B3718
A3719,B3719
A3720,B3720
A3721,B3721
A3722,B3722
A3723,B3723
A3724,B3724
A3725,B3725
A3726,B3726
A3727,B3727
A3728,B3728
A3729,B3729
A3730,B3730
A3731,B3731
A3732,B3732
A3733,B3733
A3734,B3734
A3735,B3735
A3736,B3736
A3737,B3737
A3738,B3738
A3739,B3739
A3740,B3740
A3741,B3741
A3742,B3742
A3743,B3743
A3744,B3744
A3745,B3745
A3746,B3746
A3747,B3747
A3748,B3748
A3749,B3749
A3750,B3750
A3751,B3751
A3752,B3752
A3753,B3753
A3754,B3754
A3755,B3755
A3756,B3756
A3757,B3757
A3758,B3758
A3759,B3759
A3760,B3760
A3761,B3761
A3762,B3762
A3763,B3763
A3764,B3764
A3765,B3765
A3766,B3766
A3767,B3767
A3768,B3768
A3769,B3769
A3770,B3770
A3771,B3771
A3772,B3772
A3773,B3773
A3774,B3774
A3775,B3775
A3776,B3776
A3777,B3777
A3778,B3778
A3779,B3779
A3780,B3780
A3781,B3781
A3782,B3782
A3783,B3783
A3784,B3784
A3785,B3785
A3786,B3786
A3787,B3787
A3788,B3788
A3789,B3789
A3790,B3790
A3791,B3791
A3792,B3792
A3793,B3793
A3794,B3794
A3795,B3795
A3796,B3796
A3797,B3797
A3798,B3798
A3799,B3799
A3800,B3800
A3801,B3801
A3802,B3802
A3803,B3803
A3804,B3804
A3805,B3805
A3806,B3806
A3807,B3807
A3808,B3808
A3809,B3809
A3810,B3810
A3811,B3811
A3812,B3812
A3813,B3813
A3814,B3814
A3815,B3815
A3816,B3816
A3817,B3817
A3818,B3818
A3819,B3819
A3820,B3820
A3821,B3821
A3822,B3822
A3823,B3823
A3824,B3824
A3825,B3825
A3826,B3826
A3827,B3827
A3828,B3828
A3829,B3829
A3830,B3830
A3831,B3831
A3832,B3832
A3833,B3833
A3834,B3834
A3835,B3835
A3836,B3836
A3837,B3837
A3838,B3838
A3839,B3839
A3840,B3840
A3841,B3841
A3842,B3842
A3843,B3843
A3844,B3844
A3845,B3845
A3846,B3846
A3847,B3847
A3848,B3848
A3849,B3849
A3850,B3850
A3851,B3851
A3852,B3852
A3853,B3853
A3854,B3854
A3855,B3855
A3856,B3856
A3857,B3857
A3858,B3858
A3859,B3859
A3860,B3860
A3861,B3861
A3862,B3862
A3863,B3863
A3864,B3864
A3865,B3865
A3866,B3866
A3867,B3867
A3868,B3868
A3869,B3869
A3870,B3870
A3871,B3871
A3872,B3872
A3873,B3873
A3874,B3874
A3875,B3875
A3876,B3876
A3877,B3877
A3878,B3878
A3879,B3879
A3880,B3880
A3881,B3881
A3882,B3882
A3883,B3883
A3884,B3884
A3885,B3885
A3886,B3886
A3887,B3887
A3888,B3888
A3889,B3889
A3890,B3890
A3891,B3891
A3892,B3892
A3893,B3893
A3894,B3894
A3895,B3895
A3896,B3896
A3897,B3897
A3898,B3898
A3899,B3899
A3900,B3900
A3901,B3901
A3902,B3902
A3903,B3903
A3904,B3904
A3905,B3905
A3906,B3906
A3907,B3907
A3908,B3908
A3909,B3909
A3910,B3910
A3911,B3911
A3912,B3912
A3913,B3913
A3914,B3914
A3915,B3915
A3916,B3916
A3917,B3917
A3918,B3918
A3919,B3919
A3920,B3920
A3921,B3921
A3922,B3922
A3923,B3923
A3924,B3924
A3925,B3925
A3926,B3926
A3927,B3927
A3928,B3928
A3929,B3929
A3930,B3930
A3931,B3931
A3932,B3932
A3933,B3933
A3934,B3934
A3935,B3935
A3936,B3936
A3937,B3937
A3938,B3938
A3939,B3939
A3940,B3940
A3941,B3941
A3942,B3942
A3943,B3943
A3944,B3944
A3945,B3945
A3946,B3946
A3947,B3947
A3948,B3948
A3949,B3949
A3950,B3950
A3951,B3951
A3952,B3952
A3953,B3953
A3954,B3954
A3955,B3955
A3956,B3956
A3957,B3957
A3958,B3958
A3959,B3959
A3960,B3960
A3961,B3961
A3962,B3962
A3963,B3963
A3964,B3964
A3965,B3965
A3966,B3966
A3967,B3967
A3968,B3968
A3969,B3969
A3970,B3970
A3971,B3971
A3972,B3972
A3973,B3973
A3974,B3974
A3975,B3975
A3976,B3976
A3977,B3977
A3978,B3978
A3979,B3979
A3980,B3980
A3981,B3981
A3982,B3982
A3983,B3983
A3984,B3984
A3985,B3985
A3986,B3986
A3987,B3987
A3988,B3988
A3989,B3989
A3990,B3990
A3991,B3991
A3992,B3992
A3993,B3993
A3994,B3994
A3995,B3995
A3996,B3996
A3997,B3997
A3998,B3998
A3999,B3999
A4000,B4000
A4001,B4001
A4002,B4002
A4003,B4003
A4004,B4004
A4005,B4005
A4006,B4006
A4007,B4007
A4008,B4008
A4009,B4009
A4010,B4010
A4011,B4011
A4012,B4012
A4013,B4013
A4014,B4014
A4015,B4015
A4016,B4016
A4017,B4017
A4018,B4018
A4019,B4019
A4020,B4020
A4021,B4021
A4022,B4022
A4023,B4023
A4024,B4024
A4025,B4025
A4026,B4026
A4027,B4027
A4028,B4028
A4029,B4029
A4030,B4030
A4031,B4031
A4032,B4032
A4033,B4033
A4034,B4034
A4035,B4035
A4036,B4036
A4037,B4037
A4038,B4038
A4039,B4039
A4040,B4040
A4041,B4041
A4042,B4042
A4043,B4043
A4044,B4044
A4045,B4045
A4046,B4046
A4047,B4047
A4048,B4048
A4049,B4049
A4050,B4050
A4051,B4051
A4052,B4052
A4053,B4053
A4054,B4054
A4055,B4055
A4056,B4056
A4057,B4057
A4058,B4058
A4059,B4059
A4060,B4060
A4061,B4061
A4062,B4062
A4063,B4063
A4064,B4064
A4065,B4065
A4066,B4066
A4067,B4067
A4068,B4068
A4069,B4069
A4070,B4070
A4071,B4071
A4072,B4072
A4073,B4073
A4074,B4074
A4075,B4075
A4076,B4076
A4077,B4077
A4078,B4078
A4079,B4079
A4080,B4080
A4081,B4081
A4082,B4082
A4083,B4083
A4084,B4084
A4085,B4085
A4086,B4086
A4087,B4087
A4088,B4088
A4089,B4089
A4090,B4090
A4091,B4091
A4092,B4092
A4093,B4093
A4094,B4094
A4095,B4095
A4096,B4096
A4097,B4097
A4098,B4098
A4099,B4099
A4100,B4100
A4101,B4101
A4102,B4102
A4103,B4103
A4104,B4104
A4105,B4105
A4106,B4106
A4107,B4107
A4108,B4108
A4109,B4109
A4110,B4110
A4111,B4111
A4112,B4112
A4113,B4113
A4114,B4114
A4115,B4115
A4116,B4116
A4117,B4117
A4118,B4118
A4119,B4119
A4120,B4120
A4121,B4121
A4122,B4122
A4123,B4123
A4124,B4124
A4125,B4125
A4126,B4126
A4127,B4127
A4128,B4128
A4129,B4129
A4130,B4130
A4131,B4131
A4132,B4132
A4133,B4133
A4134,B4134
A4135,B4135
A4136,B4136
A4137,B4137
A4138,B4138
A4139,B4139
A4140,B4140
A4141,B4141
A4142,B4142
A4143,B4143
A4144,B4144
A4145,B4145
A4146,B4146
A4147,B4147
A4148,B4148
A4149,B4149
A4150,B4150
A4151,B4151
A4152,B4152
A4153,B4153
A4154,B4154
A4155,B4155
A4156,B4156
A4157,B4157
A4158,B4158
A4159,B4159
A4160,B4160
A4161,B4161
A4162,B4162
A4163,B4163
A4164,B4164
A4165,B4165
A4166,B4166
A4167,B4167
A4168,B4168
A4169,B4169
A4170,B4170
A4171,B4171
A4172,B4172
A4173,B4173
A4174,B4174
A4175,B4175
A4176,B4176
A4177,B4177
A4178,B4178
A4179,B4179
A4180,B4180
A4181,B4181
A4182,B4182
A4183,B4183
A4184,B4184
A4185,B4185
A4186,B4186
A4187,B4187
A4188,B4188
A4189,B4189
A4190,B4190
A4191,B4191
A4192,B4192
A4193,B4193
A4194,B4194
A4195,B4195
A4196,B4196
A4197,B4197
A4198,B4198
A4199,B4199
A4200,B4200
A4201,B4201
A4202,B4202
A4203,B4203
A4204,B4204
A4205,B4205
A4206,B4206
A4207,B4207
A4208,B4208
A4209,B4209
A4210,B4210
A4211,B4211
A4212,B4212
A4213,B4213
A4214,B4214
A4215,B4215
A4216,B4216
A4217,B4217
A4218,B4218
A4219,B4219
A4220,B4220
A4221,B4221
A4222,B4222
A4223,B4223
A4224,B4224
A4225,B4225
A4226,B4226
A4227,B4227
A4228,B4228
A4229,B4229
A4230,B4230
A4231,B4231
A4232,B4232
A4233,B4233
A4234,B4234
A4235,B4235
A4236,B4236
A4237,B4237
A4238,B4238
A4239,B4239
A4240,B4240
A4241,B4241
A4242,B4242
A4243,B4243
A4244,B4244
A4245,B4245
A4246,B4246
A4247,B4247
A4248,B4248
A4249,B4249
A4250,B4250
A4251,B4251
A4252,B4252
A4253,B4253
A4254,B4254
A4255,B4255
A4256,B4256
A4257,B4257
A4258,B4258
A4259,B4259
A4260,B4260
A4261,B4261
A4262,B4262
A4263,B4263
A4264,B4264
A4265,B4265
A4266,B4266
A4267,B4267
A4268,B4268
A4269,B4269
A4270,B4270
A4271,B4271
A4272,B4272
A4273,B4273
A4274,B4274
A4275,B4275
A4276,B4276
A4277,B4277
A4278,B4278
A4279,B4279
A4280,B4280
A4281,B4281
A4282,B4282
A4283,B4283
A4284,B4284
A4285,B4285
A4286,B4286
A4287,B4287
A4288,B4288
A4289,B4289
A4290,B4290
A4291,B4291
A4292,B4292
A4293,B4293
A4294,B4294
A4295,B4295
A4296,B4296
A4297,B4297
A4298,B4298
A4299,B4299
A4300,B4300
A4301,B4301
A4302,B4302
A4303,B4303
A4304,B4304
A4305,B4305
A4306,B4306
A4307,B4307
A4308,B4308
A4309,B4309
A4310,B4310
A4311,B4311
A4312,B4312
A4313,B4313
A4314,B4314
A4315,B4315
A4316,B4316
A4317,B4317
A4318,B4318
A4319,B4319
A4320,B4320
A4321,B4321
A4322,B4322
A4323,B4323
A4324,B4324
A4325,B4325
A4326,B4326
A4327,B4327
A4328,B4328
A4329,B4329
A4330,B4330
A4331,B4331
A4332,B4332
A4333,B4333
A4334,B4334
A4335,B4335
A4336,B4336
A4337,B4337
A4338,B4338
A4339,B4339
A4340,B4340
A4341,B4341
A4342,B4342
A4343,B4343
A4344,B4344
A4345,B4345
A4346,B4346
A4347,B4347
A4348,B4348
A4349,B4349
A4350,B4350
A4351,B4351
A4352,B4352
A4353,B4353
A4354,B4354
A4355,B4355
A4356,B4356
A4357,B4357
A4358,B4358
A4359,B4359
A4360,B4360
A4361,B4361
A4362,B4362
A4363,B4363
A4364,B4364
A4365,B4365
A4366,B4366
A4367,B4367
A4368,B4368
A4369,B4369
A4370,B4370
A4371,B4371
A4372,B4372
A4373,B4373
A4374,B4374
A4375,B4375
A4376,B4376
A4377,B4377
A4378,B4378
A4379,B4379
A4380,B4380
A4381,B4381
A4382,B4382
A4383,B4383
A4384,B4384
A4385,B4385
A4386,B4386
A4387,B4387
A4388,B4388
A4389,B4389
A4390,B4390
A4391,B4391
A4392,B4392
A4393,B4393
A4394,B4394
A4395,B4395
A4396,B4396
A4397,B4397
A4398,B4398
A4399,B4399
A4400,B4400
A4401,B4401
A4402,B4402
A4403,B4403
A4404,B4404
A4405,B4405
A4406,B4406
A4407,B4407
A4408,B4408
A4409,B4409
A4410,B4410
A4411,B4411
A4412,B4412
A4413,B4413
A4414,B4414
A4415,B4415
A4416,B4416
A4417,B4417
A4418,B4418
A4419,B4419
A4420,B4420
A4421,B4421
A4422,B4422
A4423,B4423
A4424,B4424
A4425,B4425
A4426,B4426
A4427,B4427
A4428,B4428
A4429,B4429
A4430,B4430
A4431,B4431
A4432,B4432
A4433,B4433
A4434,B4434
A4435,B4435
A4436,B4436
A4437,B4437
A4438,B4438
A4439,B4439
A4440,B4440
A4441,B4441
A4442,B4442
A4443,B4443
A4444,B4444
A4445,B4445
A4446,B4446
A4447,B4447
A4448,B4448
A4449,B4449
A4450,B4450
A4451,B4451
A4452,B4452
A4453,B4453
A4454,B4454
A4455,B4455
A4456,B4456
A4457,B4457
A4458,B4458
A4459,B4459
A4460,B4460
A4461,B4461
A4462,B4462
A4463,B4463
A4464,B4464
A4465,B4465
A4466,B4466
A4467,B4467
A4468,B4468
A4469,B4469
A4470,B4470
A4471,B4471
A4472,B4472
A4473,B4473
A4474,B4474
A4475,B4475
A4476,B4476
A4477,B4477
A4478,B4478
A4479,B4479
A4480,B4480
A4481,B4481
A4482,B4482
A4483,B4483
A4484,B4484
A4485,B4485
A4486,B4486
A4487,B4487
A4488,B4488
A4489,B4489
A4490,B4490
A4491,B4491
A4492,B4492
A4493,B4493
A4494,B4494
A4495,B4495
A4496,B4496
A4497,B4497
A4498,B4498
A4499,B4499
A4500,B4500
A4501,B4501
A4502,B4502
A4503,B4503
A4504,B4504
A4505,B4505
A4506,B4506
A4507,B4507
A4508,B4508
A4509,B4509
A4510,B4510
A4511,B4511
A4512,B4512
A4513,B4513
A4514,B4514
A4515,B4515
A4516,B4516
A4517,B4517
A4518,B4518
A4519,B4519
A4520,B4520
A4521,B4521
A4522,B4522
A4523,B4523
A4524,B4524
A4525,B4525
A4526,B4526
A4527,B4527
A4528,B4528
A4529,B4529
A4530,B4530
A4531,B4531
A4532,B4532
A4533,B4533
A4534,B4534
A4535,B4535
A4536,B4536
A4537,B4537
A4538,B4538
A4539,B4539
A4540,B4540
A4541,B4541
A4542,B4542
A4543,B4543
A4544,B4544
A4545,B4545
A4546,B4546
A4547,B4547
A4548,B4548
A4549,B4549
A4550,B4550
A4551,B4551
A4552,B4552
A4553,B4553
A4554,B4554
A4555,B4555
A4556,B4556
A4557,B4557
A4558,B4558
A4559,B4559
A4560,B4560
A4561,B4561
A4562,B4562
A4563,B4563
A4564,B4564
A4565,B4565
A4566,B4566
A4567,B4567
A4568,B4568
A4569,B4569
A4570,B4570
A4571,B4571
A4572,B4572
A4573,B4573
A4574,B4574
A4575,B4575
A4576,B4576
A4577,B4577
A4578,B4578
A4579,B4579
A4580,B4580
A4581,B4581
A4582,B4582
A4583,B4583
A4584,B4584
A4585,B4585
A4586,B4586
A4587,B4587
A4588,B4588
A4589,B4589
A4590,B4590
A4591,B4591
A4592,B4592
A4593,B4593
A4594,B4594
A4595,B4595
A4596,B4596
A4597,B4597
A4598,B4598
A4599,B4599
A4600,B4600
A4601,B4601
A4602,B4602
A4603,B4603
A4604,B4604
A4605,B4605
A4606,B4606
A4607,B4607
A4608,B4608
A4609,B4609
A4610,B4610
A4611,B4611
A4612,B4612
A4613,B4613
A4614,B4614
A4615,B4615
A4616,B4616
A4617,B4617
A4618,B4618
A4619,B4619
A4620,B4620
A4621,B4621
A4622,B4622
A4623,B4623
A4624,B4624
A4625,B4625
A4626,B4626
A4627,B4627
A4628,B4628
A4629,B4629
A4630,B4630
A4631,B4631
A4632,B4632
A4633,B4633
A4634,B4634
A4635,B4635
A4636,B4636
A4637,B4637
A4638,B4638
A4639,B4639
A4640,B4640
A4641,B4641
A4642,B4642
A4643,B4643
A4644,B4644
A4645,B4645
A4646,B4646
A4647,B4647
A4648,B4648
A4649,B4649
A4650,B4650
A4651,B4651
A4652,B4652
A4653,B4653
A4654,B4654
A4655,B4655
A4656,B4656
A4657,B4657
A4658,B4658
A4659,B4659
A4660,B4660
A4661,B4661
A4662,B4662
A4663,B4663
A4664,B4664
A4665,B4665
A4666,B4666
A4667,B4667
A4668,B4668
A4669,B4669
A4670,B4670
A4671,B4671
A4672,B4672
A4673,B4673
A4674,B4674
A4675,B4675
A4676,B4676
A4677,B4677
A4678,B4678
A4679,B4679
A4680,B4680
A4681,B4681
A4682,B4682
A4683,B4683
A4684,B4684
A4685,B4685
A4686,B4686
A4687,B4687
A4688,B4688
A4689,B4689
A4690,B4690
A4691,B4691
A4692,B4692
A4693,B4693
A4694,B4694
A4695,B4695
A4696,B4696
A4697,B4697
A4698,B4698
A4699,B4699
A4700,B4700
A4701,B4701
A4702,B4702
A4703,B4703
A4704,B4704
A4705,B4705
A4706,B4706
A4707,B4707
A4708,B4708
A4709,B4709
A4710,B4710
A4711,B4711
A4712,B4712
A4713,B4713
A4714,B4714
A4715,B4715
A4716,B4716
A4717,B4717
A4718,B4718
A4719,B4719
A4720,B4720
A4721,B4721
A4722,B4722
A4723,B4723
A4724,B4724
A4725,B4725
A4726,B4726
A4727,B4727
A4728,B4728
A4729,B4729
A4730,B4730
A4731,B4731
A4732,B4732
A4733,B4733
A4734,B4734
A4735,B4735
A4736,B4736
A4737,B4737
A4738,B4738
A4739,B4739
A4740,B4740
A4741,B4741
A4742,B4742
A4743,B4743
A4744,B4744
A4745,B4745
A4746,B4746
A4747,B4747
A4748,B4748
A4749,B4749
A4750,B4750
A4751,B4751
A4752,B4752
A4753,B4753
A4754,B4754
A4755,B4755
A4756,B4756
A4757,B4757
A4758,B4758
A4759,B4759
A4760,B4760
A4761,B4761
A4762,B4762
A4763,B4763
A4764,B4764
A4765,B4765
A4766,B4766
A4767,B4767
A4768,B4768
A4769,B4769
A4770,B4770
A4771,B4771
A4772,B4772
A4773,B4773
A4774,B4774
A4775,B4775
A4776,B4776
A4777,B4777
A4778,B4778
A4779,B4779
A4780,B4780
A4781,B4781
A4782,B4782
A4783,B4783
A4784,B4784
A4785,B4785
A4786,B4786
A4787,B4787
A4788,B4788
A4789,B4789
A4790,B4790
A4791,B4791
A4792,B4792
A4793,B4793
A4794,B4794
A4795,B4795
A4796,B4796
A4797,B4797
A4798,B4798
A4799,B4799
A4800,B4800
A4801,B4801
A4802,B4802
A4803,B4803
A4804,B4804
A4805,B4805
A4806,B4806
A4807,B4807
A4808,B4808
A4809,B4809
A4810,B4810
A4811,B4811
A4812,B4812
A4813,B4813
A4814,B4814
A4815,B4815
A4816,B4816
A4817,B4817
A4818,B4818
A4819,B4819
A4820,B4820
A4821,B4821
A4822,B4822
A4823,B4823
A4824,B4824
A4825,B4825
A4826,B4826
A4827,B4827
A4828,B4828
A4829,B4829
A4830,B4830
A4831,B4831
A4832,B4832
A4833,B4833
A4834,B4834
A4835,B4835
A4836,B4836
A4837,B4837
A4838,B4838
A4839,B4839
A4840,B4840
A4841,B4841
A4842,B4842
A4843,B4843
A4844,B4844
A4845,B4845
A4846,B4846
A4847,B4847
A4848,B4848
A4849,B4849
A4850,B4850
A4851,B4851
A4852,B4852
A4853,B4853
A4854,B4854
A4855,B4855
A4856,B4856
A4857,B4857
A4858,B4858
A4859,B4859
A4860,B4860
A4861,B4861
A4862,B4862
A4863,B4863
A4864,B4864
A4865,B4865
A4866,B4866
A4867,B4867
A4868,B4868
A4869,B4869
A4870,B4870
A4871,B4871
A4872,B4872
A4873,B4873
A4874,B4874
A4875,B4875
A4876,B4876
A4877,B4877
A4878,B4878
A4879,B4879
A4880,B4880
A4881,B4881
A4882,B4882
A4883,B4883
A4884,B4884
A4885,B4885
A4886,B4886
A4887,B4887
A4888,B4888
A4889,B4889
A4890,B4890
A4891,B4891
A4892,B4892
A4893,B4893
A4894,B4894
A4895,B4895
A4896,B4896
A4897,B4897
A4898,B4898
A4899,B4899
A4900,B4900
A4901,B4901
A4902,B4902
A4903,B4903
A4904,B4904
A4905,B4905
A4906,B4906
A4907,B4907
A4908,B4908
A4909,B4909
A4910,B4910
A4911,B4911
A4912,B4912
A4913,B4913
A4914,B4914
A4915,B4915
A4916,B4916
A4917,B4917
A4918,B4918
A4919,B4919
A4920,B4920
A4921,B4921
A4922,B4922
A4923,B4923
A4924,B4924
A4925,B4925
A4926,B4926
A4927,B4927
A4928,B4928
A4929,B4929
A4930,B4930
A4931,B4931
A4932,B4932
A4933,B4933
A4934,B4934
A4935,B4935
A4936,B4936
A4937,B4937
A4938,B4938
A4939,B4939
A4940,B4940
A4941,B4941
A4942,B4942
A4943,B4943
A4944,B4944
A4945,B4945
A4946,B4946
A4947,B4947
A4948,B4948
A4949,B4949
A4950,B4950
A4951,B4951
A4952,B4952
A4953,B4953
A4954,B4954
A4955,B4955
A4956,B4956
A4957,B4957
A4958,B4958
A4959,B4959
A4960,B4960
A4961,B4961
A4962,B4962
A4963,B4963
A4964,B4964
A4965,B4965
A4966,B4966
A4967,B4967
A4968,B4968
A4969,B4969
A4970,B4970
A4971,B4971
A4972,B4972
A4973,B4973
A4974,B4974
A4975,B4975
A4976,B4976
A4977,B4977
A4978,B4978
A4979,B4979
A4980,B4980
A4981,B4981
A4982,B4982
A4983,B4983
A4984,B4984
A4985,B4985
A4986,B4986
A4987,B4987
A4988,B4988
A4989,B4989
A4990,B4990
A4991,B4991
A4992,B4992
A4993,B4993
A4994,B4994
A4995,B4995
A4996,B4996
A4997,B4997
A4998,B4998
A4999,B4999
A5000,B5000
```

## File: `tests/data/small.bsv`
```
COL1|COL2
c1|v1
c2|v2
```

## File: `tests/data/small.csv`
```
COL1, COL2
c1, v1
c2, v2
```

## File: `tests/data/starts_with_newline.csv`
```
a,b,c
1,this is a very long text that surely will not fit in your small screen,12345
2,"
starts with new line",678910
3,normal text now,"123,456,789"
```

## File: `tests/data/test_streaming_100.csv`
```
cutoff,customer_id,article_id,label,name
2020-05-05,1000717,160442007,0,train
2020-05-05,1000717,179123001,0,train
2020-05-05,1000717,189634001,0,train
2020-05-05,1000717,212629004,0,train
2020-05-05,1000717,278811006,0,train
2020-05-05,1000717,349301001,0,train
2020-05-05,1000717,351484039,0,train
2020-05-05,1000717,372860002,0,train
2020-05-05,1000717,372860024,0,train
2020-05-05,1000717,373506008,0,train
2020-05-05,1000717,408875001,0,train
2020-05-05,1000717,408875020,0,train
2020-05-05,1000717,484398001,0,train
2020-05-05,1000717,506098007,0,train
2020-05-05,1000717,524529004,0,train
2020-05-05,1000717,524529010,0,train
2020-05-05,1000717,547780001,0,train
2020-05-05,1000717,547780003,0,train
2020-05-05,1000717,549253002,0,train
2020-05-05,1000717,549253007,0,train
2020-05-05,1000717,554450036,0,train
2020-05-05,1000717,554598001,0,train
2020-05-05,1000717,554598047,0,train
2020-05-05,1000717,562245018,0,train
2020-05-05,1000717,562245046,0,train
2020-05-05,1000717,562245050,0,train
2020-05-05,1000717,562245100,0,train
2020-05-05,1000717,565379002,0,train
2020-05-05,1000717,572797002,0,train
2020-05-05,1000717,573085043,0,train
2020-05-05,1000717,573085047,0,train
2020-05-05,1000717,579302001,0,train
2020-05-05,1000717,579541076,0,train
2020-05-05,1000717,588245004,0,train
2020-05-05,1000717,590928001,0,train
2020-05-05,1000717,590928023,0,train
2020-05-05,1000717,599580038,0,train
2020-05-05,1000717,599580046,0,train
2020-05-05,1000717,599580052,0,train
2020-05-05,1000717,599580055,0,train
2020-05-05,1000717,610776001,0,train
2020-05-05,1000717,610776002,0,train
2020-05-05,1000717,612891008,0,train
2020-05-05,1000717,621381001,0,train
2020-05-05,1000717,621381012,0,train
2020-05-05,1000717,624486003,0,train
2020-05-05,1000717,639838012,0,train
2020-05-05,1000717,639838017,0,train
2020-05-05,1000717,640021011,0,train
2020-05-05,1000717,640021018,0,train
2020-05-05,1000717,652924010,0,train
2020-05-05,1000717,659854020,0,train
2020-05-05,1000717,664074001,0,train
2020-05-05,1000717,668956001,0,train
2020-05-05,1000717,673396002,0,train
2020-05-05,1000717,678342028,0,train
2020-05-05,1000717,679284001,0,train
2020-05-05,1000717,684037005,0,train
2020-05-05,1000717,684209004,0,train
2020-05-05,1000717,684209013,0,train
2020-05-05,1000717,684209019,0,train
2020-05-05,1000717,684209027,0,train
2020-05-05,1000717,685816001,0,train
2020-05-05,1000717,685816041,0,train
2020-05-05,1000717,687034023,0,train
2020-05-05,1000717,688537004,0,train
2020-05-05,1000717,688537021,0,train
2020-05-05,1000717,688728009,0,train
2020-05-05,1000717,690936006,0,train
2020-05-05,1000717,690936021,0,train
2020-05-05,1000717,691855012,0,train
2020-05-05,1000717,694848001,0,train
2020-05-05,1000717,695632002,0,train
2020-05-05,1000717,699080001,0,train
2020-05-05,1000717,700701001,0,train
2020-05-05,1000717,700758001,0,train
2020-05-05,1000717,704754001,0,train
2020-05-05,1000717,706016001,0,train
2020-05-05,1000717,706016002,0,train
2020-05-05,1000717,706016007,0,train
2020-05-05,1000717,706016015,0,train
2020-05-05,1000717,706016036,0,train
2020-05-05,1000717,707356001,0,train
2020-05-05,1000717,708459006,0,train
2020-05-05,1000717,708459007,0,train
2020-05-05,1000717,711431002,0,train
2020-05-05,1000717,711431007,0,train
2020-05-05,1000717,712924012,0,train
2020-05-05,1000717,714790008,0,train
2020-05-05,1000717,714790017,0,train
2020-05-05,1000717,714790020,0,train
2020-05-05,1000717,714790024,0,train
2020-05-05,1000717,714828002,0,train
2020-05-05,1000717,716672001,0,train
2020-05-05,1000717,717464001,0,train
2020-05-05,1000717,717490024,0,train
2020-05-05,1000717,719530003,0,train
2020-05-05,1000717,720125001,0,train
2020-05-05,1000717,720125041,0,train
2020-05-05,1000717,723469001,0,train
```

## File: `tests/data/test_streaming_100.tsv`
```
cutoff	customer_id	article_id	label	name
2020-05-05	1000717	160442007	0	train
2020-05-05	1000717	179123001	0	train
2020-05-05	1000717	189634001	0	train
2020-05-05	1000717	212629004	0	train
2020-05-05	1000717	278811006	0	train
2020-05-05	1000717	349301001	0	train
2020-05-05	1000717	351484039	0	train
2020-05-05	1000717	372860002	0	train
2020-05-05	1000717	372860024	0	train
2020-05-05	1000717	373506008	0	train
2020-05-05	1000717	408875001	0	train
2020-05-05	1000717	408875020	0	train
2020-05-05	1000717	484398001	0	train
2020-05-05	1000717	506098007	0	train
2020-05-05	1000717	524529004	0	train
2020-05-05	1000717	524529010	0	train
2020-05-05	1000717	547780001	0	train
2020-05-05	1000717	547780003	0	train
2020-05-05	1000717	549253002	0	train
2020-05-05	1000717	549253007	0	train
2020-05-05	1000717	554450036	0	train
2020-05-05	1000717	554598001	0	train
2020-05-05	1000717	554598047	0	train
2020-05-05	1000717	562245018	0	train
2020-05-05	1000717	562245046	0	train
2020-05-05	1000717	562245050	0	train
2020-05-05	1000717	562245100	0	train
2020-05-05	1000717	565379002	0	train
2020-05-05	1000717	572797002	0	train
2020-05-05	1000717	573085043	0	train
2020-05-05	1000717	573085047	0	train
2020-05-05	1000717	579302001	0	train
2020-05-05	1000717	579541076	0	train
2020-05-05	1000717	588245004	0	train
2020-05-05	1000717	590928001	0	train
2020-05-05	1000717	590928023	0	train
2020-05-05	1000717	599580038	0	train
2020-05-05	1000717	599580046	0	train
2020-05-05	1000717	599580052	0	train
2020-05-05	1000717	599580055	0	train
2020-05-05	1000717	610776001	0	train
2020-05-05	1000717	610776002	0	train
2020-05-05	1000717	612891008	0	train
2020-05-05	1000717	621381001	0	train
2020-05-05	1000717	621381012	0	train
2020-05-05	1000717	624486003	0	train
2020-05-05	1000717	639838012	0	train
2020-05-05	1000717	639838017	0	train
2020-05-05	1000717	640021011	0	train
2020-05-05	1000717	640021018	0	train
2020-05-05	1000717	652924010	0	train
2020-05-05	1000717	659854020	0	train
2020-05-05	1000717	664074001	0	train
2020-05-05	1000717	668956001	0	train
2020-05-05	1000717	673396002	0	train
2020-05-05	1000717	678342028	0	train
2020-05-05	1000717	679284001	0	train
2020-05-05	1000717	684037005	0	train
2020-05-05	1000717	684209004	0	train
2020-05-05	1000717	684209013	0	train
2020-05-05	1000717	684209019	0	train
2020-05-05	1000717	684209027	0	train
2020-05-05	1000717	685816001	0	train
2020-05-05	1000717	685816041	0	train
2020-05-05	1000717	687034023	0	train
2020-05-05	1000717	688537004	0	train
2020-05-05	1000717	688537021	0	train
2020-05-05	1000717	688728009	0	train
2020-05-05	1000717	690936006	0	train
2020-05-05	1000717	690936021	0	train
2020-05-05	1000717	691855012	0	train
2020-05-05	1000717	694848001	0	train
2020-05-05	1000717	695632002	0	train
2020-05-05	1000717	699080001	0	train
2020-05-05	1000717	700701001	0	train
2020-05-05	1000717	700758001	0	train
2020-05-05	1000717	704754001	0	train
2020-05-05	1000717	706016001	0	train
2020-05-05	1000717	706016002	0	train
2020-05-05	1000717	706016007	0	train
2020-05-05	1000717	706016015	0	train
2020-05-05	1000717	706016036	0	train
2020-05-05	1000717	707356001	0	train
2020-05-05	1000717	708459006	0	train
2020-05-05	1000717	708459007	0	train
2020-05-05	1000717	711431002	0	train
2020-05-05	1000717	711431007	0	train
2020-05-05	1000717	712924012	0	train
2020-05-05	1000717	714790008	0	train
2020-05-05	1000717	714790017	0	train
2020-05-05	1000717	714790020	0	train
2020-05-05	1000717	714790024	0	train
2020-05-05	1000717	714828002	0	train
2020-05-05	1000717	716672001	0	train
2020-05-05	1000717	717464001	0	train
2020-05-05	1000717	717490024	0	train
2020-05-05	1000717	719530003	0	train
2020-05-05	1000717	720125001	0	train
2020-05-05	1000717	720125041	0	train
2020-05-05	1000717	723469001	0	train
```

## File: `tests/scripts/dynamic_random_csv.sh`
```bash
#!/usr/bin/env bash
set -euo pipefail

# Dynamically rewrites OUTPUT_CSV every few seconds
# Each rewrite keeps the header and replaces the rows with a random sample

if [ "$#" -lt 2 ]; then
  echo "Usage: $0 INPUT_CSV OUTPUT_CSV [interval_seconds] [sample_size]" >&2
  exit 1
fi

INPUT="$1"
OUTPUT="$2"
INTERVAL="${3:-1}"
SAMPLE_SIZE="${4:-5}"

if ! command -v qsv >/dev/null 2>&1; then
  echo "qsv is required but not found in PATH" >&2
  exit 1
fi

if [ ! -f "$INPUT" ]; then
  echo "Input file not found: $INPUT" >&2
  exit 1
fi

while :; do
  qsv sample "$SAMPLE_SIZE" "$INPUT" > "$OUTPUT"

  echo "[dynamic_csv] $(date '+%H:%M:%S'): wrote $SAMPLE_SIZE random rows to $OUTPUT"

  sleep "$INTERVAL"
done
```

## File: `tests/scripts/stream_csv.sh`
```bash
#!/usr/bin/env bash
set -euo pipefail

# Stream CSV data in a "tricky" way for testing viewers
# - Not line buffered (outputs partial lines)
# - Variable chunk sizes
# - Configurable speed

show_usage() {
  cat >&2 <<EOF
Usage: $0 INPUT_CSV [OPTIONS]

Stream CSV data with configurable speed and tricky buffering.

Options:
  -s, --speed SPEED        Delay between chunks in seconds (default: 0.1)
  -c, --chunk-size SIZE    Base chunk size in bytes (default: random 1-50)
                          Use 'random' for variable chunks, or a number
  -l, --line-buffered      Stream complete lines instead of arbitrary chunks
  -d, --delay SECONDS      Initial delay before streaming starts (default: 0)
  -o, --output FILE        Output to file instead of stdout
  -h, --help              Show this help message

Examples:
  $0 data.csv
  $0 data.csv -s 0.05
  $0 data.csv -s 0.2 -c 10
  $0 data.csv -c random
  $0 data.csv -l           # Line buffered mode
  $0 data.csv -d 2         # Wait 2 seconds before streaming
  $0 data.csv -o out.csv   # Output to file
EOF
  exit 1
}

SPEED=0.1
CHUNK_MODE="random"
CHUNK_SIZE=0
LINE_BUFFERED=false
INITIAL_DELAY=0
OUTPUT=""

INPUT=""
while [[ $# -gt 0 ]]; do
  case $1 in
    -s|--speed)
      SPEED="$2"
      shift 2
      ;;
    -c|--chunk-size)
      if [[ "$2" == "random" ]]; then
        CHUNK_MODE="random"
      else
        CHUNK_MODE="fixed"
        CHUNK_SIZE="$2"
      fi
      shift 2
      ;;
    -l|--line-buffered)
      LINE_BUFFERED=true
      shift
      ;;
    -d|--delay)
      INITIAL_DELAY="$2"
      shift 2
      ;;
    -o|--output)
      OUTPUT="$2"
      shift 2
      ;;
    -h|--help)
      show_usage
      ;;
    *)
      if [[ -z "$INPUT" ]]; then
        INPUT="$1"
      else
        echo "Error: Unexpected argument '$1'" >&2
        show_usage
      fi
      shift
      ;;
  esac
done

if [[ -z "$INPUT" ]]; then
  echo "Error: INPUT_CSV is required" >&2
  show_usage
fi

if [[ ! -f "$INPUT" ]]; then
  echo "Error: Input file not found: $INPUT" >&2
  exit 1
fi

if ! [[ "$SPEED" =~ ^[0-9]+\.?[0-9]*$ ]]; then
  echo "Error: Speed must be a number" >&2
  exit 1
fi

if ! [[ "$INITIAL_DELAY" =~ ^[0-9]+\.?[0-9]*$ ]]; then
  echo "Error: Initial delay must be a number" >&2
  exit 1
fi

get_chunk_size() {
  if [[ "$CHUNK_MODE" == "random" ]]; then
    echo $((RANDOM % 50 + 1))
  else
    echo "$CHUNK_SIZE"
  fi
}

# Use perl for sub-second sleep (works on both Linux and macOS)
do_sleep() {
  perl -e "select(undef, undef, undef, $1)"
}

# Setup output redirection
if [[ -n "$OUTPUT" ]]; then
  # Clear output file
  > "$OUTPUT"
  OUTPUT_TARGET="file: $OUTPUT"
else
  OUTPUT_TARGET="stdout"
fi

if [[ "$LINE_BUFFERED" == "true" ]]; then
  echo "[stream_csv] Starting: $INPUT (speed=${SPEED}s, line-buffered mode, output=$OUTPUT_TARGET)" >&2

  # Initial delay before streaming
  if (( $(echo "$INITIAL_DELAY > 0" | bc -l) )); then
    do_sleep "$INITIAL_DELAY"
  fi

  # Stream line by line
  while IFS= read -r line; do
    if [[ -n "$OUTPUT" ]]; then
      printf '%s\n' "$line" >> "$OUTPUT"
    else
      printf '%s\n' "$line"
    fi
    if (( $(echo "$SPEED > 0" | bc -l) )); then
      do_sleep "$SPEED"
    fi
  done < "$INPUT"
else
  echo "[stream_csv] Starting: $INPUT (speed=${SPEED}s, chunks=$CHUNK_MODE, output=$OUTPUT_TARGET)" >&2

  # Initial delay before streaming
  if (( $(echo "$INITIAL_DELAY > 0" | bc -l) )); then
    do_sleep "$INITIAL_DELAY"
  fi

  FILE_CONTENT=$(cat "$INPUT")
  FILE_SIZE=${#FILE_CONTENT}
  POSITION=0

  # Stream content in chunks, potentially breaking lines mid-way
  while [[ $POSITION -lt $FILE_SIZE ]]; do
    CHUNK_SIZE=$(get_chunk_size)
    CHUNK="${FILE_CONTENT:$POSITION:$CHUNK_SIZE}"
    if [[ -n "$OUTPUT" ]]; then
      printf '%s' "$CHUNK" >> "$OUTPUT"
    else
      printf '%s' "$CHUNK"
    fi
    POSITION=$((POSITION + CHUNK_SIZE))

    if (( $(echo "$SPEED > 0" | bc -l) )); then
      do_sleep "$SPEED"
    fi
  done
fi
```

