---
id: uv
type: knowledge
owner: OA_Triage
---
# uv
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
# uv

[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![image](https://img.shields.io/pypi/v/uv.svg)](https://pypi.python.org/pypi/uv)
[![image](https://img.shields.io/pypi/l/uv.svg)](https://pypi.python.org/pypi/uv)
[![image](https://img.shields.io/pypi/pyversions/uv.svg)](https://pypi.python.org/pypi/uv)
[![Actions status](https://github.com/astral-sh/uv/actions/workflows/ci.yml/badge.svg)](https://github.com/astral-sh/uv/actions)
[![Discord](https://img.shields.io/badge/Discord-%235865F2.svg?logo=discord&logoColor=white)](https://discord.gg/astral-sh)

An extremely fast Python package and project manager, written in Rust.

<p align="center">
  <picture align="center">
    <source media="(prefers-color-scheme: dark)" srcset="https://github.com/astral-sh/uv/assets/1309177/03aa9163-1c79-4a87-a31d-7a9311ed9310">
    <source media="(prefers-color-scheme: light)" srcset="https://github.com/astral-sh/uv/assets/1309177/629e59c0-9c6e-4013-9ad4-adb2bcf5080d">
    <img alt="Shows a bar chart with benchmark results." src="https://github.com/astral-sh/uv/assets/1309177/629e59c0-9c6e-4013-9ad4-adb2bcf5080d">
  </picture>
</p>

<p align="center">
  <i>Installing <a href="https://trio.readthedocs.io/">Trio</a>'s dependencies with a warm cache.</i>
</p>

## Highlights

- A single tool to replace `pip`, `pip-tools`, `pipx`, `poetry`, `pyenv`, `twine`, `virtualenv`, and
  more.
- [10-100x faster](https://github.com/astral-sh/uv/blob/main/BENCHMARKS.md) than `pip`.
- Provides [comprehensive project management](#projects), with a
  [universal lockfile](https://docs.astral.sh/uv/concepts/projects/layout#the-lockfile).
- [Runs scripts](#scripts), with support for
  [inline dependency metadata](https://docs.astral.sh/uv/guides/scripts#declaring-script-dependencies).
- [Installs and manages](#python-versions) Python versions.
- [Runs and installs](#tools) tools published as Python packages.
- Includes a [pip-compatible interface](#the-pip-interface) for a performance boost with a familiar
  CLI.
- Supports Cargo-style [workspaces](https://docs.astral.sh/uv/concepts/projects/workspaces) for
  scalable projects.
- Disk-space efficient, with a [global cache](https://docs.astral.sh/uv/concepts/cache) for
  dependency deduplication.
- Installable without Rust or Python via `curl` or `pip`.
- Supports macOS, Linux, and Windows.

uv is backed by [Astral](https://astral.sh), the creators of
[Ruff](https://github.com/astral-sh/ruff) and [ty](https://github.com/astral-sh/ty).

## Installation

Install uv with our standalone installers:

```bash
# On macOS and Linux.
curl -LsSf https://astral.sh/uv/install.sh | sh
```

```bash
# On Windows.
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Or, from [PyPI](https://pypi.org/project/uv/):

```bash
# With pip.
pip install uv
```

```bash
# Or pipx.
pipx install uv
```

If installed via the standalone installer, uv can update itself to the latest version:

```bash
uv self update
```

See the [installation documentation](https://docs.astral.sh/uv/getting-started/installation/) for
details and alternative installation methods.

## Documentation

uv's documentation is available at [docs.astral.sh/uv](https://docs.astral.sh/uv).

Additionally, the command line reference documentation can be viewed with `uv help`.

## Features

### Projects

uv manages project dependencies and environments, with support for lockfiles, workspaces, and more,
similar to `rye` or `poetry`:

```console
$ uv init example
Initialized project `example` at `/home/user/example`

$ cd example

$ uv add ruff
Creating virtual environment at: .venv
Resolved 2 packages in 170ms
   Built example @ file:///home/user/example
Prepared 2 packages in 627ms
Installed 2 packages in 1ms
 + example==0.1.0 (from file:///home/user/example)
 + ruff==0.5.0

$ uv run ruff check
All checks passed!

$ uv lock
Resolved 2 packages in 0.33ms

$ uv sync
Resolved 2 packages in 0.70ms
Checked 1 package in 0.02ms
```

See the [project documentation](https://docs.astral.sh/uv/guides/projects/) to get started.

uv also supports building and publishing projects, even if they're not managed with uv. See the
[publish guide](https://docs.astral.sh/uv/guides/publish/) to learn more.

### Scripts

uv manages dependencies and environments for single-file scripts.

Create a new script and add inline metadata declaring its dependencies:

```console
$ echo 'import requests; print(requests.get("https://astral.sh"))' > example.py

$ uv add --script example.py requests
Updated `example.py`
```

Then, run the script in an isolated virtual environment:

```console
$ uv run example.py
Reading inline script metadata from: example.py
Installed 5 packages in 12ms
<Response [200]>
```

See the [scripts documentation](https://docs.astral.sh/uv/guides/scripts/) to get started.

### Tools

uv executes and installs command-line tools provided by Python packages, similar to `pipx`.

Run a tool in an ephemeral environment using `uvx` (an alias for `uv tool run`):

```console
$ uvx pycowsay 'hello world!'
Resolved 1 package in 167ms
Installed 1 package in 9ms
 + pycowsay==0.0.0.2
  """

  ------------
< hello world! >
  ------------
   \   ^__^
    \  (oo)\_______
       (__)\       )\/\
           ||----w |
           ||     ||
```

Install a tool with `uv tool install`:

```console
$ uv tool install ruff
Resolved 1 package in 6ms
Installed 1 package in 2ms
 + ruff==0.5.0
Installed 1 executable: ruff

$ ruff --version
ruff 0.5.0
```

See the [tools documentation](https://docs.astral.sh/uv/guides/tools/) to get started.

### Python versions

uv installs Python and allows quickly switching between versions.

Install multiple Python versions:

```console
$ uv python install 3.12 3.13 3.14
Installed 3 versions in 972ms
 + cpython-3.12.12-macos-aarch64-none (python3.12)
 + cpython-3.13.9-macos-aarch64-none (python3.13)
 + cpython-3.14.0-macos-aarch64-none (python3.14)

```

Download Python versions as needed:

```console
$ uv venv --python 3.12.0
Using Python 3.12.0
Creating virtual environment at: .venv
Activate with: source .venv/bin/activate

$ uv run --python pypy@3.8 -- python --version
Python 3.8.16 (a9dbdca6fc3286b0addd2240f11d97d8e8de187a, Dec 29 2022, 11:45:30)
[PyPy 7.3.11 with GCC Apple LLVM 13.1.6 (clang-1316.0.21.2.5)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>>
```

Use a specific Python version in the current directory:

```console
$ uv python pin 3.11
Pinned `.python-version` to `3.11`
```

See the [Python installation documentation](https://docs.astral.sh/uv/guides/install-python/) to get
started.

### The pip interface

uv provides a drop-in replacement for common `pip`, `pip-tools`, and `virtualenv` commands.

uv extends their interfaces with advanced features, such as dependency version overrides,
platform-independent resolutions, reproducible resolutions, alternative resolution strategies, and
more.

Migrate to uv without changing your existing workflows — and experience a 10-100x speedup — with the
`uv pip` interface.

Compile requirements into a platform-independent requirements file:

```console
$ uv pip compile requirements.in \
   --universal \
   --output-file requirements.txt
Resolved 43 packages in 12ms
```

Create a virtual environment:

```console
$ uv venv
Using Python 3.12.3
Creating virtual environment at: .venv
Activate with: source .venv/bin/activate
```

Install the locked requirements:

```console
$ uv pip sync requirements.txt
Resolved 43 packages in 11ms
Installed 43 packages in 208ms
 + babel==2.15.0
 + black==24.4.2
 + certifi==2024.7.4
 ...
```

See the [pip interface documentation](https://docs.astral.sh/uv/pip/index/) to get started.

## Contributing

We are passionate about supporting contributors of all levels of experience and would love to see
you get involved in the project. See the
[contributing guide](https://github.com/astral-sh/uv?tab=contributing-ov-file#contributing) to get
started.

## FAQ

#### How do you pronounce uv?

It's pronounced as "you - vee" ([`/juː viː/`](https://en.wikipedia.org/wiki/Help:IPA/English#Key))

#### How should I stylize uv?

Just "uv", please. See the [style guide](./STYLE.md#styling-uv) for details.

#### What platforms does uv support?

See uv's [platform support](https://docs.astral.sh/uv/reference/platforms/) document.

#### Is uv ready for production?

Yes, uv is stable and widely used in production. See uv's
[versioning policy](https://docs.astral.sh/uv/reference/versioning/) document for details.

## Acknowledgements

uv's dependency resolver uses [PubGrub](https://github.com/pubgrub-rs/pubgrub) under the hood. We're
grateful to the PubGrub maintainers, especially [Jacob Finkelman](https://github.com/Eh2406), for
their support.

uv's Git implementation is based on [Cargo](https://github.com/rust-lang/cargo).

Some of uv's optimizations are inspired by the great work we've seen in [pnpm](https://pnpm.io/),
[Orogene](https://github.com/orogene/orogene), and [Bun](https://github.com/oven-sh/bun). We've also
learned a lot from Nathaniel J. Smith's [Posy](https://github.com/njsmith/posy) and adapted its
[trampoline](https://github.com/njsmith/posy/tree/main/src/trampolines/windows-trampolines/posy-trampoline)
for Windows support.

## License

uv is licensed under either of

- Apache License, Version 2.0, ([LICENSE-APACHE](LICENSE-APACHE) or
  <https://www.apache.org/licenses/LICENSE-2.0>)
- MIT license ([LICENSE-MIT](LICENSE-MIT) or <https://opensource.org/licenses/MIT>)

at your option.

Unless you explicitly state otherwise, any contribution intentionally submitted for inclusion in uv
by you, as defined in the Apache-2.0 license, shall be dually licensed as above, without any
additional terms or conditions.

<div align="center">
  <a target="_blank" href="https://astral.sh" style="background:none">
    <img src="https://raw.githubusercontent.com/astral-sh/uv/main/assets/svg/Astral.svg" alt="Made by Astral">
  </a>
</div>

```

### File: crates\README.md
```md
# Crates

## [uv-bench](./uv-bench)

Functionality for benchmarking uv.

## [uv-cache-key](./uv-cache-key)

Generic functionality for caching paths, URLs, and other resources across platforms.

## [uv-distribution-filename](./uv-distribution-filename)

Parse built distribution (wheel) and source distribution (sdist) filenames to extract structured
metadata.

## [uv-distribution-types](./uv-distribution-types)

Abstractions for representing built distributions (wheels) and source distributions (sdists), and
the sources from which they can be downloaded.

## [uv-install-wheel-rs](./uv-install-wheel)

Install built distributions (wheels) into a virtual environment.

## [uv-once-map](./uv-once-map)

A [`waitmap`](https://github.com/withoutboats/waitmap)-like concurrent hash map for executing tasks
exactly once.

## [uv-pep440-rs](./uv-pep440)

Utilities for interacting with Python version numbers and specifiers.

## [uv-pep508-rs](./uv-pep508)

Utilities for parsing and evaluating
[dependency specifiers](https://packaging.python.org/en/latest/specifications/dependency-specifiers/),
previously known as [PEP 508](https://peps.python.org/pep-0508/).

## [uv-platform-tags](./uv-platform-tags)

Functionality for parsing and inferring Python platform tags as per
[PEP 425](https://peps.python.org/pep-0425/).

## [uv-cli](./uv-cli)

Command-line interface for the uv package manager.

## [uv-build-frontend](./uv-build-frontend)

A [PEP 517](https://www.python.org/dev/peps/pep-0517/)-compatible build frontend for uv.

## [uv-cache](./uv-cache)

Functionality for caching Python packages and associated metadata.

## [uv-client](./uv-client)

Client for interacting with PyPI-compatible HTTP APIs.

## [uv-dev](./uv-dev)

Development utilities for uv.

## [uv-dispatch](./uv-dispatch)

A centralized `struct` for resolving and building source distributions in isolated environments.
Implements the traits defined in `uv-types`.

## [uv-distribution](./uv-distribution)

Client for interacting with built distributions (wheels) and source distributions (sdists). Capable
of fetching metadata, distribution contents, etc.

## [uv-extract](./uv-extract)

Utilities for extracting files from archives.

## [uv-fs](./uv-fs)

Utilities for interacting with the filesystem.

## [uv-git](./uv-git)

Functionality for interacting with Git repositories.

## [uv-installer](./uv-installer)

Functionality for installing Python packages into a virtual environment.

## [uv-python](./uv-python)

Functionality for detecting and leveraging the current Python interpreter.

## [uv-normalize](./uv-normalize)

Normalize package and extra names as per Python specifications.

## [uv-requirements](./uv-requirements)

Utilities for reading package requirements from `pyproject.toml` and `requirements.txt` files.

## [uv-resolver](./uv-resolver)

Functionality for resolving Python packages and their dependencies.

## [uv-shell](./uv-shell)

Utilities for detecting and manipulating shell environments.

## [uv-types](./uv-types)

Shared traits for uv, to avoid circular dependencies.

## [uv-pypi-types](./uv-pypi-types)

General-purpose type definitions for types used in PyPI-compatible APIs.

## [uv-virtualenv](./uv-virtualenv)

A `venv` replacement to create virtual environments in Rust.

## [uv-warnings](./uv-warnings)

User-facing warnings for uv.

## [uv-workspace](./uv-workspace)

Workspace abstractions for uv.

## [uv-requirements-txt](./uv-requirements-txt)

Functionality for parsing `requirements.txt` files.

```

### File: crates\uv\README.md
```md
<!-- This file is generated. DO NOT EDIT -->

# uv

uv is a Python package and project manager.

See the [documentation](https://docs.astral.sh/uv/) or [repository](https://github.com/astral-sh/uv)
for more information.

This crate is the entry point to the uv command-line interface. The Rust API exposed here is not
considered public interface.

This is version 0.11.3. The source can be found
[here](https://github.com/astral-sh/uv/blob/0.11.3/crates/uv).

The following uv workspace members are also available:

- [uv-audit](https://crates.io/crates/uv-audit)
- [uv-auth](https://crates.io/crates/uv-auth)
- [uv-bin-install](https://crates.io/crates/uv-bin-install)
- [uv-build](https://crates.io/crates/uv-build)
- [uv-build-backend](https://crates.io/crates/uv-build-backend)
- [uv-build-frontend](https://crates.io/crates/uv-build-frontend)
- [uv-cache](https://crates.io/crates/uv-cache)
- [uv-cache-info](https://crates.io/crates/uv-cache-info)
- [uv-cache-key](https://crates.io/crates/uv-cache-key)
- [uv-cli](https://crates.io/crates/uv-cli)
- [uv-client](https://crates.io/crates/uv-client)
- [uv-configuration](https://crates.io/crates/uv-configuration)
- [uv-console](https://crates.io/crates/uv-console)
- [uv-dirs](https://crates.io/crates/uv-dirs)
- [uv-dispatch](https://crates.io/crates/uv-dispatch)
- [uv-distribution](https://crates.io/crates/uv-distribution)
- [uv-distribution-filename](https://crates.io/crates/uv-distribution-filename)
- [uv-distribution-types](https://crates.io/crates/uv-distribution-types)
- [uv-extract](https://crates.io/crates/uv-extract)
- [uv-flags](https://crates.io/crates/uv-flags)
- [uv-fs](https://crates.io/crates/uv-fs)
- [uv-git](https://crates.io/crates/uv-git)
- [uv-git-types](https://crates.io/crates/uv-git-types)
- [uv-globfilter](https://crates.io/crates/uv-globfilter)
- [uv-install-wheel](https://crates.io/crates/uv-install-wheel)
- [uv-installer](https://crates.io/crates/uv-installer)
- [uv-keyring](https://crates.io/crates/uv-keyring)
- [uv-logging](https://crates.io/crates/uv-logging)
- [uv-macros](https://crates.io/crates/uv-macros)
- [uv-metadata](https://crates.io/crates/uv-metadata)
- [uv-normalize](https://crates.io/crates/uv-normalize)
- [uv-once-map](https://crates.io/crates/uv-once-map)
- [uv-options-metadata](https://crates.io/crates/uv-options-metadata)
- [uv-pep440](https://crates.io/crates/uv-pep440)
- [uv-pep508](https://crates.io/crates/uv-pep508)
- [uv-performance-memory-allocator](https://crates.io/crates/uv-performance-memory-allocator)
- [uv-platform](https://crates.io/crates/uv-platform)
- [uv-platform-tags](https://crates.io/crates/uv-platform-tags)
- [uv-preview](https://crates.io/crates/uv-preview)
- [uv-publish](https://crates.io/crates/uv-publish)
- [uv-pypi-types](https://crates.io/crates/uv-pypi-types)
- [uv-python](https://crates.io/crates/uv-python)
- [uv-redacted](https://crates.io/crates/uv-redacted)
- [uv-requirements](https://crates.io/crates/uv-requirements)
- [uv-requirements-txt](https://crates.io/crates/uv-requirements-txt)
- [uv-resolver](https://crates.io/crates/uv-resolver)
- [uv-scripts](https://crates.io/crates/uv-scripts)
- [uv-settings](https://crates.io/crates/uv-settings)
- [uv-shell](https://crates.io/crates/uv-shell)
- [uv-small-str](https://crates.io/crates/uv-small-str)
- [uv-state](https://crates.io/crates/uv-state)
- [uv-static](https://crates.io/crates/uv-static)
- [uv-test](https://crates.io/crates/uv-test)
- [uv-tool](https://crates.io/crates/uv-tool)
- [uv-torch](https://crates.io/crates/uv-torch)
- [uv-trampoline-builder](https://crates.io/crates/uv-trampoline-builder)
- [uv-types](https://crates.io/crates/uv-types)
- [uv-unix](https://crates.io/crates/uv-unix)
- [uv-version](https://crates.io/crates/uv-version)
- [uv-virtualenv](https://crates.io/crates/uv-virtualenv)
- [uv-warnings](https://crates.io/crates/uv-warnings)
- [uv-windows](https://crates.io/crates/uv-windows)
- [uv-workspace](https://crates.io/crates/uv-workspace)

uv's workspace members are considered internal and will have frequent breaking changes.

See uv's
[crate versioning policy](https://docs.astral.sh/uv/reference/policies/versioning/#crate-versioning)
for details on versioning.

```

### File: scripts\benchmark\README.md
```md
# benchmark

Benchmarking scripts for uv and other package management tools.

## Getting Started

From the `scripts/benchmark` directory:

```shell
uv run resolver \
    --uv-pip \
    --poetry \
    --benchmark \
    resolve-cold \
    ../requirements/trio.in
```

```

### File: test\packages\README.md
```md
# packages

A collection of packages used to test editable installs and bespoke behaviors in packaging setups
and definitions.

```

### File: .pre-commit-config.yaml
```yaml
fail_fast: true

exclude: |
  (?x)^(
    .*/(snapshots)/.*|
  )$

repos:
  - repo: https://github.com/abravalheri/validate-pyproject
    rev: v0.24.1
    hooks:
      - id: validate-pyproject

  - repo: https://github.com/crate-ci/typos
    rev: v1.42.3
    hooks:
      - id: typos

  - repo: local
    hooks:
      - id: rustfmt
        name: rustfmt
        entry: rustfmt
        language: system
        types: [rust]

  - repo: local
    hooks:
      - id: cargo-dev-generate-all
        name: cargo dev generate-all
        entry: cargo dev generate-all
        language: system
        types: [rust]
        pass_filenames: false
        files: ^crates/(uv-cli|uv-settings)/

  - repo: local
    hooks:
      - id: prettier
        name: prettier
        entry: prettier --write --ignore-unknown
        language: node
        additional_dependencies: ["prettier@3"]
        types_or: [yaml, json5]

  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.14.14
    hooks:
      - id: ruff-format
      - id: ruff
        args: [--fix, --exit-non-zero-on-fix]

```

### File: BENCHMARKS.md
```md
# Benchmarks

All benchmarks were computed on macOS using Python 3.12.4 (for non-uv tools), and come with a few
important caveats:

- Benchmark performance may vary dramatically across different operating systems and filesystems. In
  particular, uv uses different installation strategies based on the underlying filesystem's
  capabilities. (For example, uv uses reflinking on macOS, and hardlinking on Linux.)
- Benchmark performance may vary dramatically depending on the set of packages being installed. For
  example, a resolution that requires building a single intensive source distribution may appear
  very similar across tools, since the bottleneck is tool-agnostic.

This document benchmarks against Trio's `docs-requirements.in`, as a representative example of a
real-world project.

In each case, a smaller bar (i.e., lower) is better.

## Warm Installation

Benchmarking package installation (e.g., `uv sync`) with a warm cache. This is equivalent to
removing and recreating a virtual environment, and then populating it with dependencies that you've
installed previously on the same machine.

![install-warm](https://github.com/user-attachments/assets/84118aaa-d030-4e29-8f1e-9483091ceca3)

## Cold Installation

Benchmarking package installation (e.g., `uv sync`) with a cold cache. This is equivalent to running
`uv sync` on a new machine or in CI (assuming that the package manager cache is not shared across
runs).

![install-cold](https://github.com/user-attachments/assets/e7f5b203-7e84-452b-8c56-1ff6531c9898)

## Warm Resolution

Benchmarking dependency resolution (e.g., `uv lock`) with a warm cache, but no existing lockfile.
This is equivalent to blowing away an existing `requirements.txt` file to regenerate it from a
`requirements.in` file.

![resolve-warm](https://github.com/user-attachments/assets/e1637a08-8b27-4077-8138-b3849e53eb04)

## Cold Resolution

Benchmarking dependency resolution (e.g., `uv lock`) with a cold cache. This is equivalent to
running `uv lock` on a new machine or in CI (assuming that the package manager cache is not shared
across runs).

![resolve-cold](https://github.com/user-attachments/assets/b578c264-c209-45ab-b4c3-54073d871e86)

## Reproduction

All benchmarks were generated using the `scripts/benchmark` package, which wraps
[`hyperfine`](https://github.com/sharkdp/hyperfine) to facilitate benchmarking uv against a variety
of other tools.

The benchmark script itself has a several requirements:

- A local uv release build (`cargo build --release`).
- An installation of the production `uv` binary in your path.
- The [`hyperfine`](https://github.com/sharkdp/hyperfine) command-line tool installed on your
  system.

To benchmark resolution against pip-compile, Poetry, and PDM:

```shell
uv run resolver \
    --uv-project \
    --poetry \
    --pdm \
    --pip-compile \
    --benchmark resolve-warm --benchmark resolve-cold \
    --json \
    ../requirements/trio.in
```

To benchmark installation against pip-sync, Poetry, and PDM:

```shell
uv run resolver \
    --uv-project \
    --poetry \
    --pdm \
    --pip-sync \
    --benchmark install-warm --benchmark install-cold \
    --json \
    ../requirements/compiled/trio.txt
```

Both commands should be run from the `scripts/benchmark` directory.

After running the benchmark script, you can generate the corresponding graph via:

```shell
cargo run -p uv-dev --all-features render-benchmarks resolve-warm.json --title "Warm Resolution"
cargo run -p uv-dev --all-features render-benchmarks resolve-cold.json --title "Cold Resolution"
cargo run -p uv-dev --all-features render-benchmarks install-warm.json --title "Warm Installation"
cargo run -p uv-dev --all-features render-benchmarks install-cold.json --title "Cold Installation"
```

You need to install the [Roboto Font](https://fonts.google.com/specimen/Roboto) if the labels are
missing in the generated graph.

## Acknowledgements

The inclusion of this `BENCHMARKS.md` file was inspired by the excellent benchmarking documentation
in
[Orogene](https://github.com/orogene/orogene/blob/472e481b4fc6e97c2b57e69240bf8fe995dfab83/BENCHMARKS.md).

## Troubleshooting

### Flaky benchmarks

If you're seeing high variance when running the cold benchmarks, then it's likely that you're
running into throttling or DDoS prevention from your ISP. In that case, ISPs forcefully terminate
TCP connections with a TCP reset. We believe this is due to the benchmarks making the exact same
requests in a very short time (especially true for `uv`). A possible workaround is to connect to VPN
to bypass your ISPs filtering mechanism.

```

### File: CHANGELOG.md
```md
# Changelog

<!-- prettier-ignore-start -->


## 0.11.3

Released on 2026-04-01.

### Enhancements

- Add progress bar for hashing phase in uv publish ([#18752](https://github.com/astral-sh/uv/pull/18752))
- Add support for ROCm 7.2 ([#18730](https://github.com/astral-sh/uv/pull/18730))
- Emit abi3t tags for every abi3 version ([#18777](https://github.com/astral-sh/uv/pull/18777))
- Expand `uv workspace metadata` with dependency information from the lock ([#18356](https://github.com/astral-sh/uv/pull/18356))
- Implement support for PEP 803 ([#18767](https://github.com/astral-sh/uv/pull/18767))
- Pretty-print platform in built wheel errors ([#18738](https://github.com/astral-sh/uv/pull/18738))
- Publish installers to `/installers/uv/latest` on the mirror ([#18725](https://github.com/astral-sh/uv/pull/18725))
- Show free-threaded Python in built-wheel errors ([#18740](https://github.com/astral-sh/uv/pull/18740))

### Preview features

- Add `--ignore` and `--ignore-until-fixed` to `uv audit` ([#18737](https://github.com/astral-sh/uv/pull/18737))

### Bug fixes

- Bump simple API cache ([#18797](https://github.com/astral-sh/uv/pull/18797))
- Don't drop `blake2b` hashes ([#18794](https://github.com/astral-sh/uv/pull/18794))
- Handle broken range request implementations ([#18780](https://github.com/astral-sh/uv/pull/18780))
- Remove `powerpc64-unknown-linux-gnu` from release build targets ([#18800](https://github.com/astral-sh/uv/pull/18800))
- Respect dependency metadata overrides in `uv pip check` ([#18742](https://github.com/astral-sh/uv/pull/18742))
- Support debug CPython ABI tags in environment compatibility ([#18739](https://github.com/astral-sh/uv/pull/18739))

### Documentation

- Document `false` opt-out for `exclude-newer-package` ([#18768](https://github.com/astral-sh/uv/pull/18768), [#18803](https://github.com/astral-sh/uv/pull/18803))

## 0.11.2

Released on 2026-03-26.

### Enhancements

- Add a dedicated Windows PE editing error ([#18710](https://github.com/astral-sh/uv/pull/18710))
- Make `uv self update` fetch the manifest from the mirror first ([#18679](https://github.com/astral-sh/uv/pull/18679))
- Use uv reqwest client for self update ([#17982](https://github.com/astral-sh/uv/pull/17982))
- Show `uv self update` success and failure messages with `--quiet` ([#18645](https://github.com/astral-sh/uv/pull/18645))

### Preview features

- Evaluate extras and groups when determining auditable packages ([#18511](https://github.com/astral-sh/uv/pull/18511))

### Bug fixes

- Skip redundant project configuration parsing for `uv run` ([#17890](https://github.com/astral-sh/uv/pull/17890))

## 0.11.1

Released on 2026-03-24.

### Bug fixes

- Add missing hash verification for `riscv64gc-unknown-linux-musl` ([#18686](https://github.com/astral-sh/uv/pull/18686))
- Fallback to direct download when direct URL streaming is unsupported ([#18688](https://github.com/astral-sh/uv/pull/18688))
- Revert treating 'Dynamic' values as case-insensitive ([#18692](https://github.com/astral-sh/uv/pull/18692))
- Remove torchdata from list of packages to source from the PyTorch index ([#18703](https://github.com/astral-sh/uv/pull/18703))
- Special-case `==` Python version request ranges ([#9697](https://github.com/astral-sh/uv/pull/9697))

### Documentation

- Cover `--python <dir>` in "Using arbitrary Python environments" ([#6457](https://github.com/astral-sh/uv/pull/6457))
- Fix version annotations for `PS_MODULE_PATH` and `UV_WORKING_DIR` ([#18691](https://github.com/astral-sh/uv/pull/18691))

## 0.11.0

Released on 2026-03-23.

### Breaking changes

This release includes changes to the networking stack used by uv. While we think that breakage will be rare, it is possible that these changes will result in the rejection of certificates previously trusted by uv so we have marked the change as breaking out of an abundance of caution.

The changes are largely driven by the upgrade of reqwest, which powers uv's HTTP clients, to [v0.13](https://seanmonstar.com/blog/reqwest-v013-rustls-default/) which included some breaking changes to TLS certificate verification.

The following changes are included:

- [`rustls-platform-verifier`](https://github.com/rustls/rustls-platform-verifier) is used instead of [`rustls-native-certs`](https://github.com/rustls/rustls-native-certs) and [`webpki`](https://github.com/rustls/webpki) for certificate verification
  
  **This change should have no effect unless you are using the `native-tls` option to enable reading system certificates.**
  
  `rustls-platform-verifier` delegates to the system for certificate validation (e.g., `Security.framework` on macOS) instead of eagerly loading certificates from the system and verifying them via `webpki`. The effects of this change will vary based on the operating system. In general, uv's certificate validation should now be more consistent with browsers and other native applications. However, this is the most likely cause of breaking changes in this release. Some previously failing certificate chains may succeed, and some previously accepted certificate chains may fail. In either case, we expect the validation to be more correct and welcome reports of regressions.
  
  In particular, because more responsibility for validating the certificate is transferred to your system's security library, some features like [CA constraints](https://support.apple.com/en-us/103255) or [revocation of certificates](https://en.wikipedia.org/wiki/Certificate_revocation) via OCSP and CRLs may now be used.
  
  This change should improve performance when using system certificate on macOS, as uv no longer needs to load all certificates from the keychain at startup.
- [`aws-lc`](https://github.com/aws/aws-lc) is used instead of `ring` for a cryptography backend
  
  There should not be breaking changes from this change. We expect this to expand support for certificate signature algorithms.
- `--native-tls` is deprecated in favor of a new `--system-certs` flag
  
  The `--native-tls` flag is still usable and has identical behavior to `--system-certs.`
  
  This change was made to reduce confusion about the TLS implementation uv uses. uv always uses `rustls` not `native-tls`.
- Building uv on x86-64 and i686 Windows requires NASM
  
  NASM is required by `aws-lc`. If not found on the system, a prebuilt blob provided by `aws-lc-sys` will be used.
  
  If you are not building uv from source, this change has no effect.
  
  See the [CONTRIBUTING](https://github.com/astral-sh/uv/blob/b6854d77bfd0cb78157fecaf8b30126c6f16bc11/CONTRIBUTING.md#setup) guide for details.
- Empty `SSL_CERT_FILE` values are ignored (for consistency with `SSL_CERT_DIR`)

See [#18550](https://github.com/astral-sh/uv/pull/18550) for details.

### Python

- Enable frame pointers for improved profiling on Linux x86-64 and aarch64

See the [python-build-standalone release notes](https://github.com/astral-sh/python-build-standalone/releases/20260320) for details.

### Enhancements

- Treat 'Dynamic' values as case-insensitive ([#18669](https://github.com/astral-sh/uv/pull/18669))
- Use a dedicated error for invalid cache control headers ([#18657](https://github.com/astral-sh/uv/pull/18657))
- Enable checksum verification in the generated installer script ([#18625](https://github.com/astral-sh/uv/pull/18625))

### Preview features

- Add `--service-format` and `--service-url` to `uv audit` ([#18571](https://github.com/astral-sh/uv/pull/18571))

### Performance

- Avoid holding flat index lock across indexes ([#18659](https://github.com/astral-sh/uv/pull/18659))

### Bug fixes

- Find the dynamic linker on the file system when sniffing binaries fails ([#18457](https://github.com/astral-sh/uv/pull/18457))
- Fix export of conflicting workspace members with dependencies ([#18666](https://github.com/astral-sh/uv/pull/18666))
- Respect installed settings in `uv tool list --outdated` ([#18586](https://github.com/astral-sh/uv/pull/18586))
- Treat paths originating as PEP 508 URLs which contain expanded variables as relative ([#18680](https://github.com/astral-sh/uv/pull/18680))
- Fix `uv export` for workspace member packages with conflicts ([#18635](https://github.com/astral-sh/uv/pull/18635))
- Continue to alternative authentication providers when the pyx store has no token ([#18425](https://github.com/astral-sh/uv/pull/18425))
- Use redacted URLs for log messages in cached client ([#18599](https://github.com/astral-sh/uv/pull/18599))

### Documentation

- Add details on Linux versions to the platform policy ([#18574](https://github.com/astral-sh/uv/pull/18574))
- Clarify `FLASH_ATTENTION_SKIP_CUDA_BUILD` guidance for `flash-attn` installs ([#18473](https://github.com/astral-sh/uv/pull/18473))
- Split the dependency bots page into two separate pages ([#18597](https://github.com/astral-sh/uv/pull/18597))
- Split the alternative indexes page into separate pages ([#18607](https://github.com/astral-sh/uv/pull/18607))

## 0.10.12

Released on 2026-03-19.

### Python

- Add pypy 3.11.15 ([#18468](https://github.com/astral-sh/uv/pull/18468))
- Add support for using Python 3.6 interpreters ([#18454](https://github.com/astral-sh/uv/pull/18454))

### Enhancements

- Include uv's target triple in version report ([#18520](https://github.com/astral-sh/uv/pull/18520))
- Allow comma separated values in `--no-emit-package` ([#18565](https://github.com/astral-sh/uv/pull/18565))

### Preview features

- Show `uv audit` in the CLI help ([#18540](https://github.com/astral-sh/uv/pull/18540))

### Bug fixes

- Improve reporting of managed interpreter symlinks in `uv python list` ([#18459](https://github.com/astral-sh/uv/pull/18459))
- Preserve end-of-line comments on previous entries when removing dependencies ([#18557](https://github.com/astral-sh/uv/pull/18557))
- Treat abi3 wheel Python version as a lower bound ([#18536](https://github.com/astral-sh/uv/pull/18536))
- Detect hard-float support on aarch64 kernels running armv7 userspace ([#18530](https://github.com/astral-sh/uv/pull/18530))

### Documentation

- Add Python 3.15 to supported versions ([#18552](https://github.com/astral-sh/uv/pull/18552))
- Adjust the PyPy note ([#18548](https://github.com/astral-sh/uv/pull/18548))
- Move Pyodide to Tier 2 in the Python support policy ([#18561](https://github.com/astral-sh/uv/pull/18561))
- Move Rust and Python version support out of the Platform support policy ([#18535](https://github.com/astral-sh/uv/pull/18535))
- Update Docker guide with changes from `uv-docker-example` ([#18558](https://github.com/astral-sh/uv/pull/18558))
- Update the Python version policy ([#18559](https://github.com/astral-sh/uv/pull/18559))

## 0.10.11

Released on 2026-03-16.

### Enhancements

- Fetch Ruff release metadata from an Astral mirror ([#18358](https://github.com/astral-sh/uv/pull/18358))
- Use PEP 639 license metadata for uv itself ([#16477](https://github.com/astral-sh/uv/pull/16477))

### Performance

- Improve distribution id performance ([#18486](https://github.com/astral-sh/uv/pull/18486))

### Bug fixes

- Allow `--project` to refer to a `pyproject.toml` directly and reduce to a warning on other files ([#18513](https://github.com/astral-sh/uv/pull/18513))
- Disable `SYSTEM_VERSION_COMPAT` when querying interpreters on macOS ([#18452](https://github.com/astral-sh/uv/pull/18452))
- Enforce available distributions for supported environments ([#18451](https://github.com/astral-sh/uv/pull/18451))
- Fix `uv sync --active` recreating active environments when `UV_PYTHON_INSTALL_DIR` is relative ([#18398](https://github.com/astral-sh/uv/pull/18398))

### Documentation

- Add missing `-o requirements.txt` in `uv pip compile` example ([#12308](https://github.com/astral-sh/uv/pull/12308))
- Link to organization security policy ([#18449](https://github.com/astral-sh/uv/pull/18449))
- Link to the AI policy in the contributing guide ([#18448](https://github.com/astral-sh/uv/pull/18448))
## 0.10.10

Released on 2026-03-13.

### Python

- Add CPython 3.15.0a7 ([#18403](https://github.com/astral-sh/uv/pull/18403))

### Enhancements

- Add `--outdated` flag to `uv tool list` ([#18318](https://github.com/astral-sh/uv/pull/18318))
- Add riscv64 musl target to build-release-binaries workflow ([#18228](https://github.com/astral-sh/uv/pull/18228))
- Fetch Ruff from an Astral mirror ([#18286](https://github.com/astral-sh/uv/pull/18286))
- Improve error handling for platform detection in Python downloads ([#18453](https://github.com/astral-sh/uv/pull/18453))
- Warn if `--project` directory does not exist ([#17714](https://github.com/astral-sh/uv/pull/17714))
- Warn when workspace member scripts are skipped due to missing build system ([#18389](https://github.com/astral-sh/uv/pull/18389))
- Update build backend versions used in `uv init` ([#18417](https://github.com/astral-sh/uv/pull/18417))
- Log explicit config file path in verbose output ([#18353](https://github.com/astral-sh/uv/pull/18353))
- Make `uv cache clear` an alias of `uv cache clean` ([#18420](https://github.com/astral-sh/uv/pull/18420))
- Reject invalid classifiers, warn on license classifiers in `uv_build` ([#18419](https://github.com/astral-sh/uv/pull/18419))

### Preview features

- Add links to `uv audit` output ([#18392](https://github.com/astral-sh/uv/pull/18392))
- Output/report formatting for `uv audit` ([#18193](https://github.com/astral-sh/uv/pull/18193))
- Switch to batched OSV queries for `uv audit` ([#18394](https://github.com/astral-sh/uv/pull/18394))

### Bug fixes

- Avoid sharing version metadata across indexes ([#18373](https://github.com/astral-sh/uv/pull/18373))
- Bump zlib-rs to 0.6.2 to fix panic on decompression of large wheels on Windows ([#18362](https://github.com/astral-sh/uv/pull/18362))
- Filter out unsupported environment wheels ([#18445](https://github.com/astral-sh/uv/pull/18445))
- Preserve absolute/relative paths in lockfiles ([#18176](https://github.com/astral-sh/uv/pull/18176))
- Recreate Python environments under `uv tool install --force` ([#18399](https://github.com/astral-sh/uv/pull/18399))
- Respect timestamp and other cache keys in cached environments ([#18396](https://github.com/astral-sh/uv/pull/18396))
- Simplify selected extra markers in `uv export` ([#18433](https://github.com/astral-sh/uv/pull/18433))
- Send pyx mint-token requests with a proper `Content-Type` ([#18334](https://github.com/astral-sh/uv/pull/18334))
- Fix Windows operating system and version reporting ([#18383](https://github.com/astral-sh/uv/pull/18383))

### Documentation

- Update the platform support policy with a tier 3 section including freebsd and 32-bit windows ([#18345](https://github.com/astral-sh/uv/pull/18345))

## 0.10.9

Released on 2026-03-06.

### Enhancements

- Add `fbgemm-gpu`, `fbgemm-gpu-genai`, `torchrec`, and `torchtune` to the PyTorch list ([#18338](https://github.com/astral-sh/uv/pull/18338))
- Add torchcodec to PyTorch List ([#18336](https://github.com/astral-sh/uv/pull/18336))
- L
... [TRUNCATED]
```

### File: CLAUDE.md
```md
- Read CONTRIBUTING.md for guidelines on how to run tools
- ALWAYS attempt to add a test case for changed behavior
- PREFER integration tests, e.g., at `it/...` over unit tests
- When making changes for Windows from Unix, use `cargo xwin clippy` to check compilation
- NEVER perform builds with the release profile, unless asked or reproducing performance issues
- PREFER running specific tests over running the entire test suite
- AVOID using `panic!`, `unreachable!`, `.unwrap()`, unsafe code, and clippy rule ignores
- PREFER patterns like `if let` to handle fallibility
- ALWAYS write `SAFETY` comments following our usual style when writing `unsafe` code
- PREFER `#[expect()]` over `[allow()]` if clippy must be disabled
- PREFER let chains (`if let` combined with `&&`) over nested `if let` statements
- NEVER update all dependencies in the lockfile and ALWAYS use `cargo update --precise` to make
  lockfile changes
- NEVER assume clippy warnings are pre-existing, it is very rare that `main` has warnings
- ALWAYS read and copy the style of similar tests when adding new cases
- PREFER top-level imports over local imports or fully qualified names
- AVOID shortening variable names, e.g., use `version` instead of `ver`, and `requires_python`
  instead of `rp`
- PREFER [`TypeName`] references when writing Rust doc comments

```

### File: CONTRIBUTING.md
```md
# Contributing

## Finding ways to help

We label issues that would be good for a first time contributor as
[`good first issue`](https://github.com/astral-sh/uv/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+issue%22).
These usually do not require significant experience with Rust or the uv code base.

We label issues that we think are a good opportunity for subsequent contributions as
[`help wanted`](https://github.com/astral-sh/uv/issues?q=is%3Aopen+is%3Aissue+label%3A%22help+wanted%22).
These require varying levels of experience with Rust and uv. Often, we want to accomplish these
tasks but do not have the resources to do so ourselves.

You don't need our permission to start on an issue we have labeled as appropriate for community
contribution as described above. However, it's a good idea to indicate that you are going to work on
an issue to avoid concurrent attempts to solve the same problem.

Please check in with us before starting work on an issue that has not been labeled as appropriate
for community contribution. We're happy to receive contributions for other issues, but it's
important to make sure we have consensus on the solution to the problem first.

Outside of issues with the labels above, issues labeled as
[`bug`](https://github.com/astral-sh/uv/issues?q=is%3Aopen+is%3Aissue+label%3A%22bug%22) are the
best candidates for contribution. In contrast, issues labeled with `needs-decision` or
`needs-design` are _not_ good candidates for contribution. Please do not open pull requests for
issues with these labels.

Please do not open pull requests for new features without prior discussion. While we appreciate
exploration of new features, we will almost always close these pull requests immediately. Adding a
new feature to uv creates a long-term maintenance burden and requires strong consensus from the uv
team before it is appropriate to begin work on an implementation.

## Use of AI

We **require all use of AI in contributions to follow our
[AI Policy](https://github.com/astral-sh/.github/blob/main/AI_POLICY.md)**.

If your contribution does not follow the policy, it will be closed.

## Setup

[Rust](https://rustup.rs/) (and a C compiler) are required to build uv.

On Ubuntu and other Debian-based distributions, you can install a C compiler with:

```shell
sudo apt install build-essential
```

On Fedora-based distributions, you can install a C compiler with:

```shell
sudo dnf install gcc
```

On Windows, [NASM](https://www.nasm.us/) is required for building the TLS backend (`aws-lc-sys`). If
it is not present, a prebuilt blob provided by `aws-lc-sys` will be used instead. WinGet can be used
to install NASM:

```shell
winget install NASM.NASM
```

After installation, add `C:\Program Files\NASM` to your `PATH`. While the prebuilt blob will not be
used when NASM is found, you can guarantee this behavior by setting `AWS_LC_SYS_PREBUILT_NASM=0`.

## Testing

For running tests, we recommend [nextest](https://nexte.st/).

To run a specific test by name:

```shell
cargo nextest run -E 'test(test_name)'
```

To run all tests and accept snapshot changes:

```shell
cargo insta test --accept --test-runner nextest
```

To update snapshots for a specific test:

```shell
cargo insta test --accept --test-runner nextest -- <test_name>
```

### Python

Testing uv requires multiple specific Python versions; they can be installed with:

```shell
cargo run python install
```

The storage directory can be configured with `UV_PYTHON_INSTALL_DIR`. (It must be an absolute path.)

### Snapshot testing

uv uses [insta](https://insta.rs/) for snapshot testing. It's recommended (but not necessary) to use
`cargo-insta` for a better snapshot review experience. See the
[installation guide](https://insta.rs/docs/cli/) for more information.

In tests, you can use `uv_snapshot!` macro to simplify creating snapshots for uv commands. For
example:

```rust
#[test]
fn test_add() {
    let context = TestContext::new("3.12");
    uv_snapshot!(context.filters(), context.add().arg("requests"), @"");
}
```

To run and review a specific snapshot test:

```shell
cargo test --package <package> --test <test> -- <test_name> -- --exact
cargo insta review
```

A script is available to update the snapshots based on results in CI. This is useful for updating
snapshots without re-running the test suite and for updating platform-specific snapshots.

```shell
./scripts/apply-ci-snapshots.sh
```

### Git and Git LFS

A subset of uv tests require both [Git](https://git-scm.com) and [Git LFS](https://git-lfs.com/) to
execute properly.

These tests can be disabled by turning off either `git` or `git-lfs` uv features.

### Local testing

You can invoke your development version of uv with `cargo run -- <args>`. For example:

```shell
cargo run -- venv
cargo run -- pip install requests
```

## Formatting

```shell
# Rust
cargo fmt --all

# Python
uvx ruff format .

# Markdown, YAML, and other files (requires Node.js)
npx prettier --write .
# or in Docker
docker run --rm -v .:/src/ -w /src/ node:alpine npx prettier --write .
```

## Linting

Linting requires [shellcheck](https://github.com/koalaman/shellcheck) and
[cargo-shear](https://github.com/Boshen/cargo-shear) to be installed separately.

```shell
# Rust
cargo clippy --workspace --all-targets --all-features --locked -- -D warnings

# Python
uvx ruff check .

# Python type checking
uvx ty check python/uv

# Shell scripts
shellcheck <script>

# Spell checking
uvx typos

# Unused Rust dependencies
cargo shear
```

### Compiling for Windows from Unix

To run clippy for a Windows target from Linux or macOS, you can use
[cargo-xwin](https://github.com/rust-cross/cargo-xwin):

```shell
# Install cargo-xwin
cargo install cargo-xwin --locked

# Add the Windows target
rustup target add x86_64-pc-windows-msvc

# Run clippy for Windows
cargo xwin clippy --workspace --all-targets --all-features --locked -- -D warnings
```

## Crate structure

Rust does not allow circular dependencies between crates. To visualize the crate hierarchy, install
[cargo-depgraph](https://github.com/jplatte/cargo-depgraph) and graphviz, then run:

```shell
cargo depgraph --dedup-transitive-deps --workspace-only | dot -Tpng > graph.png
```

## Running inside a Docker container

Source distributions can run arbitrary code on build and can make unwanted modifications to your
system
(["Someone's Been Messing With My Subnormals!" on Blogspot](https://moyix.blogspot.com/2022/09/someones-been-messing-with-my-subnormals.html),
["nvidia-pyindex" on PyPI](https://pypi.org/project/nvidia-pyindex/)), which can even occur when
just resolving requirements. To prevent this, there's a Docker container you can run commands in:

```console
$ docker build -t uv-builder -f crates/uv-dev/builder.dockerfile --load .
# Build for musl to avoid glibc errors, might not be required with your OS version
cargo build --target x86_64-unknown-linux-musl --profile profiling
docker run --rm -it -v $(pwd):/app uv-builder /app/target/x86_64-unknown-linux-musl/profiling/uv-dev resolve-many --cache-dir /app/cache-docker /app/scripts/popular_packages/pypi_10k_most_dependents.txt
```

We recommend using this container if you don't trust the dependency tree of the package(s) you are
trying to resolve or install.

## Profiling and Benchmarking

Please refer to Ruff's
[Profiling Guide](https://github.com/astral-sh/ruff/blob/main/CONTRIBUTING.md#profiling-projects),
it applies to uv, too.

We provide diverse sets of requirements for testing and benchmarking the resolver in
`test/requirements` and for the installer in `test/requirements/compiled`.

You can use `scripts/benchmark` to benchmark predefined workloads between uv versions and with other
tools, e.g., from the `scripts/benchmark` directory:

```shell
uv run resolver \
    --uv-pip \
    --poetry \
    --benchmark \
    resolve-cold \
    ../test/requirements/trio.in
```

### Analyzing concurrency

You can use [tracing-durations-export](https://github.com/konstin/tracing-durations-export) to
visualize parallel requests and find any spots where uv is CPU-bound. Example usage, with `uv` and
`uv-dev` respectively:

```shell
RUST_LOG=uv=info TRACING_DURATIONS_FILE=target/traces/jupyter.ndjson cargo run --features tracing-durations-export --profile profiling -- pip compile test/requirements/jupyter.in
```

```shell
RUST_LOG=uv=info TRACING_DURATIONS_FILE=target/traces/jupyter.ndjson cargo run --features tracing-durations-export --bin uv-dev --profile profiling -- resolve jupyter
```

### Trace-level logging

You can enable `trace` level logging using the `RUST_LOG` environment variable, i.e.

```shell
RUST_LOG=trace uv
```

## Documentation

To preview any changes to the documentation locally:

1. Install the [Rust toolchain](https://www.rust-lang.org/tools/install).

2. Run `cargo dev generate-all`, to update any auto-generated documentation.

3. Run the development server with:

   ```shell
   uv run --only-group docs mkdocs serve -f mkdocs.yml
   ```

The documentation should then be available locally at
[http://127.0.0.1:8000/uv/](http://127.0.0.1:8000/uv/).

Documentation is deployed automatically on release by publishing to the
[Astral documentation](https://github.com/astral-sh/docs) repository, which itself deploys via
Cloudflare Pages.

After making changes to the documentation, [format the markdown files](#formatting) using Prettier.

## Development code signing on macOS

Code signing can only be performed by Astral team members.

Code signing on macOS can improve developer experience when running tests, e.g., when running tests
that access the macOS keychain, a signed binary can be approved once but an unsigned binary will
need to be approved on each re-compile.

### Acquiring a development certificate

1. Generate a
   [request for the certificate](https://developer.apple.com/help/account/certificates/create-a-certificate-signing-request)
2. Create a certificate in the
   [Apple Developer portal](https://developer.apple.com/account/resources/certificates/list)
3. Download and install the certificate to your login keychain

   ```shell
   security import ~/Downloads/mac_development.cer -k ~/Library/Keychains/login.keychain-db
   ```

4. Identify your code signing identity

   ```shell
   security find-identity -v -p codesigning
   ```

5. If the above fails to find your identity, install the intermediate certificates

   ```shell
   curl -sLO "https://www.apple.com/certificateauthority/AppleWWDRCAG3.cer"
   security import AppleWWDRCAG3.cer -k ~/Library/Keychains/login.keychain-db
   rm AppleWWDRCAG3.cer
   ```

6. Set `UV_TEST_CODESIGN_IDENTITY`

   ```shell
   export UV_TEST_CODESIGN_IDENTITY="Mac Developer: Your Name (TEAM_ID)"
   ```

Note `UV_TEST_CODESIGN_IDENTITY` is only supported via `nextest`.

## Releases

Releases can only be performed by Astral team members.

Changelog entries and version bumps are automated. First, run:

```shell
./scripts/release.sh
```

Then, editorialize the `CHANGELOG.md` file to ensure entries are consistently styled.

Then, open a pull request, e.g., `Bump version to ...`.

Binary builds will automatically be tested for the release.

After merging the pull request, run the
[release workflow](https://github.com/astral-sh/uv/actions/workflows/release.yml) with the version
tag. **Do not include a leading `v`**. The release will automatically be created on GitHub after
everything else publishes.

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
