---
id: ruff
type: knowledge
owner: OA_Triage
---
# ruff
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
<!-- Begin section: Overview -->

# Ruff

[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![image](https://img.shields.io/pypi/v/ruff.svg)](https://pypi.python.org/pypi/ruff)
[![image](https://img.shields.io/pypi/l/ruff.svg)](https://github.com/astral-sh/ruff/blob/main/LICENSE)
[![image](https://img.shields.io/pypi/pyversions/ruff.svg)](https://pypi.python.org/pypi/ruff)
[![Actions status](https://github.com/astral-sh/ruff/workflows/CI/badge.svg)](https://github.com/astral-sh/ruff/actions)
[![Discord](https://img.shields.io/badge/Discord-%235865F2.svg?logo=discord&logoColor=white)](https://discord.com/invite/astral-sh)

[**Docs**](https://docs.astral.sh/ruff/) | [**Playground**](https://play.ruff.rs/)

An extremely fast Python linter and code formatter, written in Rust.

<p align="center">
  <picture align="center">
    <source media="(prefers-color-scheme: dark)" srcset="https://user-images.githubusercontent.com/1309177/232603514-c95e9b0f-6b31-43de-9a80-9e844173fd6a.svg">
    <source media="(prefers-color-scheme: light)" srcset="https://user-images.githubusercontent.com/1309177/232603516-4fb4892d-585c-4b20-b810-3db9161831e4.svg">
    <img alt="Shows a bar chart with benchmark results." src="https://user-images.githubusercontent.com/1309177/232603516-4fb4892d-585c-4b20-b810-3db9161831e4.svg">
  </picture>
</p>

<p align="center">
  <i>Linting the CPython codebase from scratch.</i>
</p>

- ⚡️ 10-100x faster than existing linters (like Flake8) and formatters (like Black)
- 🐍 Installable via `pip`
- 🛠️ `pyproject.toml` support
- 🤝 Python 3.14 compatibility
- ⚖️ Drop-in parity with [Flake8](https://docs.astral.sh/ruff/faq/#how-does-ruffs-linter-compare-to-flake8), isort, and [Black](https://docs.astral.sh/ruff/faq/#how-does-ruffs-formatter-compare-to-black)
- 📦 Built-in caching, to avoid re-analyzing unchanged files
- 🔧 Fix support, for automatic error correction (e.g., automatically remove unused imports)
- 📏 Over [800 built-in rules](https://docs.astral.sh/ruff/rules/), with native re-implementations
    of popular Flake8 plugins, like flake8-bugbear
- ⌨️ First-party [editor integrations](https://docs.astral.sh/ruff/editors) for [VS Code](https://github.com/astral-sh/ruff-vscode) and [more](https://docs.astral.sh/ruff/editors/setup)
- 🌎 Monorepo-friendly, with [hierarchical and cascading configuration](https://docs.astral.sh/ruff/configuration/#config-file-discovery)

Ruff aims to be orders of magnitude faster than alternative tools while integrating more
functionality behind a single, common interface.

Ruff can be used to replace [Flake8](https://pypi.org/project/flake8/) (plus dozens of plugins),
[Black](https://github.com/psf/black), [isort](https://pypi.org/project/isort/),
[pydocstyle](https://pypi.org/project/pydocstyle/), [pyupgrade](https://pypi.org/project/pyupgrade/),
[autoflake](https://pypi.org/project/autoflake/), and more, all while executing tens or hundreds of
times faster than any individual tool.

Ruff is extremely actively developed and used in major open-source projects like:

- [Apache Airflow](https://github.com/apache/airflow)
- [Apache Superset](https://github.com/apache/superset)
- [FastAPI](https://github.com/tiangolo/fastapi)
- [Hugging Face](https://github.com/huggingface/transformers)
- [Pandas](https://github.com/pandas-dev/pandas)
- [SciPy](https://github.com/scipy/scipy)

...and [many more](#whos-using-ruff).

Ruff is backed by [Astral](https://astral.sh), the creators of
[uv](https://github.com/astral-sh/uv) and [ty](https://github.com/astral-sh/ty).

Read the [launch
post](https://astral.sh/blog/announcing-astral-the-company-behind-ruff), or the
original [project
announcement](https://notes.crmarsh.com/python-tooling-could-be-much-much-faster).

## Testimonials

[**Sebastián Ramírez**](https://twitter.com/tiangolo/status/1591912354882764802), creator
of [FastAPI](https://github.com/tiangolo/fastapi):

> Ruff is so fast that sometimes I add an intentional bug in the code just to confirm it's actually
> running and checking the code.

[**Nick Schrock**](https://twitter.com/schrockn/status/1612615862904827904), founder of [Elementl](https://www.elementl.com/),
co-creator of [GraphQL](https://graphql.org/):

> Why is Ruff a gamechanger? Primarily because it is nearly 1000x faster. Literally. Not a typo. On
> our largest module (dagster itself, 250k LOC) pylint takes about 2.5 minutes, parallelized across 4
> cores on my M1. Running ruff against our _entire_ codebase takes .4 seconds.

[**Bryan Van de Ven**](https://github.com/bokeh/bokeh/pull/12605), co-creator
of [Bokeh](https://github.com/bokeh/bokeh/), original author
of [Conda](https://docs.conda.io/en/latest/):

> Ruff is ~150-200x faster than flake8 on my machine, scanning the whole repo takes ~0.2s instead of
> ~20s. This is an enormous quality of life improvement for local dev. It's fast enough that I added
> it as an actual commit hook, which is terrific.

[**Timothy Crosley**](https://twitter.com/timothycrosley/status/1606420868514877440),
creator of [isort](https://github.com/PyCQA/isort):

> Just switched my first project to Ruff. Only one downside so far: it's so fast I couldn't believe
> it was working till I intentionally introduced some errors.

[**Tim Abbott**](https://github.com/zulip/zulip/pull/23431#issuecomment-1302557034), lead developer of [Zulip](https://github.com/zulip/zulip) (also [here](https://github.com/astral-sh/ruff/issues/465#issuecomment-1317400028)):

> This is just ridiculously fast... `ruff` is amazing.

<!-- End section: Overview -->

## Table of Contents

For more, see the [documentation](https://docs.astral.sh/ruff/).

1. [Getting Started](#getting-started)
1. [Configuration](#configuration)
1. [Rules](#rules)
1. [Contributing](#contributing)
1. [Support](#support)
1. [Acknowledgements](#acknowledgements)
1. [Who's Using Ruff?](#whos-using-ruff)
1. [License](#license)

## Getting Started<a id="getting-started"></a>

For more, see the [documentation](https://docs.astral.sh/ruff/).

### Installation

Ruff is available as [`ruff`](https://pypi.org/project/ruff/) on PyPI.

Invoke Ruff directly with [`uvx`](https://docs.astral.sh/uv/):

```shell
uvx ruff check   # Lint all files in the current directory.
uvx ruff format  # Format all files in the current directory.
```

Or install Ruff with `uv` (recommended), `pip`, or `pipx`:

```shell
# With uv.
uv tool install ruff@latest  # Install Ruff globally.
uv add --dev ruff            # Or add Ruff to your project.

# With pip.
pip install ruff

# With pipx.
pipx install ruff
```

Starting with version `0.5.0`, Ruff can be installed with our standalone installers:

```shell
# On macOS and Linux.
curl -LsSf https://astral.sh/ruff/install.sh | sh

# On Windows.
powershell -c "irm https://astral.sh/ruff/install.ps1 | iex"

# For a specific version.
curl -LsSf https://astral.sh/ruff/0.15.9/install.sh | sh
powershell -c "irm https://astral.sh/ruff/0.15.9/install.ps1 | iex"
```

You can also install Ruff via [Homebrew](https://formulae.brew.sh/formula/ruff), [Conda](https://anaconda.org/conda-forge/ruff),
and with [a variety of other package managers](https://docs.astral.sh/ruff/installation/).

### Usage

To run Ruff as a linter, try any of the following:

```shell
ruff check                          # Lint all files in the current directory (and any subdirectories).
ruff check path/to/code/            # Lint all files in `/path/to/code` (and any subdirectories).
ruff check path/to/code/*.py        # Lint all `.py` files in `/path/to/code`.
ruff check path/to/code/to/file.py  # Lint `file.py`.
ruff check @arguments.txt           # Lint using an input file, treating its contents as newline-delimited command-line arguments.
```

Or, to run Ruff as a formatter:

```shell
ruff format                          # Format all files in the current directory (and any subdirectories).
ruff format path/to/code/            # Format all files in `/path/to/code` (and any subdirectories).
ruff format path/to/code/*.py        # Format all `.py` files in `/path/to/code`.
ruff format path/to/code/to/file.py  # Format `file.py`.
ruff format @arguments.txt           # Format using an input file, treating its contents as newline-delimited command-line arguments.
```

Ruff can also be used as a [pre-commit](https://pre-commit.com/) hook via [`ruff-pre-commit`](https://github.com/astral-sh/ruff-pre-commit):

```yaml
- repo: https://github.com/astral-sh/ruff-pre-commit
  # Ruff version.
  rev: v0.15.9
  hooks:
    # Run the linter.
    - id: ruff-check
      args: [ --fix ]
    # Run the formatter.
    - id: ruff-format
```

Ruff can also be used as a [VS Code extension](https://github.com/astral-sh/ruff-vscode) or with [various other editors](https://docs.astral.sh/ruff/editors/setup).

Ruff can also be used as a [GitHub Action](https://github.com/features/actions) via
[`ruff-action`](https://github.com/astral-sh/ruff-action):

```yaml
name: Ruff
on: [ push, pull_request ]
jobs:
  ruff:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: astral-sh/ruff-action@v3
```

### Configuration<a id="configuration"></a>

Ruff can be configured through a `pyproject.toml`, `ruff.toml`, or `.ruff.toml` file (see:
[_Configuration_](https://docs.astral.sh/ruff/configuration/), or [_Settings_](https://docs.astral.sh/ruff/settings/)
for a complete list of all configuration options).

If left unspecified, Ruff's default configuration is equivalent to the following `ruff.toml` file:

```toml
# Exclude a variety of commonly ignored directories.
exclude = [
    ".bzr",
    ".direnv",
    ".eggs",
    ".git",
    ".git-rewrite",
    ".hg",
    ".ipynb_checkpoints",
    ".mypy_cache",
    ".nox",
    ".pants.d",
    ".pyenv",
    ".pytest_cache",
    ".pytype",
    ".ruff_cache",
    ".svn",
    ".tox",
    ".venv",
    ".vscode",
    "__pypackages__",
    "_build",
    "buck-out",
    "build",
    "dist",
    "node_modules",
    "site-packages",
    "venv",
]

# Same as Black.
line-length = 88
indent-width = 4

# Assume Python 3.10
target-version = "py310"

[lint]
# Enable Pyflakes (`F`) and a subset of the pycodestyle (`E`) codes by default.
select = ["E4", "E7", "E9", "F"]
ignore = []

# Allow fix for all enabled rules (when `--fix`) is provided.
fixable = ["ALL"]
unfixable = []

# Allow unused variables when underscore-prefixed.
dummy-variable-rgx = "^(_+|(_+[a-zA-Z0-9_]*[a-zA-Z0-9]+?))$"

[format]
# Like Black, use double quotes for strings.
quote-style = "double"

# Like Black, indent with spaces, rather than tabs.
indent-style = "space"

# Like Black, respect magic trailing commas.
skip-magic-trailing-comma = false

# Like Black, automatically detect the appropriate line ending.
line-ending = "auto"
```

Note that, in a `pyproject.toml`, each section header should be prefixed with `tool.ruff`. For
example, `[lint]` should be replaced with `[tool.ruff.lint]`.

Some configuration options can be provided via dedicated command-line arguments, such as those
related to rule enablement and disablement, file discovery, and logging level:

```shell
ruff check --select F401 --select F403 --quiet
```

The remaining configuration options can be provided through a catch-all `--config` argument:

```shell
ruff check --config "lint.per-file-ignores = {'some_file.py' = ['F841']}"
```

To opt in to the latest lint rules, formatter style changes, interface updates, and more, enable
[preview mode](https://docs.astral.sh/ruff/preview/) by setting `preview = true` in your configuration
file or passing `--preview` on the command line. Preview mode enables a collection of unstable
features that may change prior to stabilization.

See `ruff help` for more on Ruff's top-level commands, or `ruff help check` and `ruff help format`
for more on the linting and formatting commands, respectively.

## Rules<a id="rules"></a>

<!-- Begin section: Rules -->

**Ruff supports over 900 lint rules**, many of which are inspired by popular tools like Flake8,
isort, pyupgrade, and others. Regardless of the rule's origin, Ruff re-implements every rule in
Rust as a first-party feature.

By default, Ruff enables Flake8's `F` rules, along with a subset of the `E` rules, omitting any
stylistic rules that overlap with the use of a formatter, like `ruff format` or
[Black](https://github.com/psf/black).

If you're just getting started with Ruff, **the default rule set is a great place to start**: it
catches a wide variety of common errors (like unused imports) with zero configuration.

In [preview](https://docs.astral.sh/ruff/preview/), Ruff enables an expanded set of default rules
that includes rules from the `B`, `UP`, and `RUF` categories, as well as many more. If you give the
new defaults a try, feel free to leave feedback in the [GitHub
discussion](https://github.com/astral-sh/ruff/discussions/23203), where you can also find the new
rule set listed in full.

<!-- End section: Rules -->

Beyond the defaults, Ruff re-implements some of the most popular Flake8 plugins and related code
quality tools, including:

- [autoflake](https://pypi.org/project/autoflake/)
- [eradicate](https://pypi.org/project/eradicate/)
- [flake8-2020](https://pypi.org/project/flake8-2020/)
- [flake8-annotations](https://pypi.org/project/flake8-annotations/)
- [flake8-async](https://pypi.org/project/flake8-async)
- [flake8-bandit](https://pypi.org/project/flake8-bandit/) ([#1646](https://github.com/astral-sh/ruff/issues/1646))
- [flake8-blind-except](https://pypi.org/project/flake8-blind-except/)
- [flake8-boolean-trap](https://pypi.org/project/flake8-boolean-trap/)
- [flake8-bugbear](https://pypi.org/project/flake8-bugbear/)
- [flake8-builtins](https://pypi.org/project/flake8-builtins/)
- [flake8-commas](https://pypi.org/project/flake8-commas/)
- [flake8-comprehensions](https://pypi.org/project/flake8-comprehensions/)
- [flake8-copyright](https://pypi.org/project/flake8-copyright/)
- [flake8-datetimez](https://pypi.org/project/flake8-datetimez/)
- [flake8-debugger](https://pypi.org/project/flake8-debugger/)
- [flake8-django](https://pypi.org/project/flake8-django/)
- [flake8-docstrings](https://pypi.org/project/flake8-docstrings/)
- [flake8-eradicate](https://pypi.org/project/flake8-eradicate/)
- [flake8-errmsg](https://pypi.org/project/flake8-errmsg/)
- [flake8-executable](https://pypi.org/project/flake8-executable/)
- [flake8-future-annotations](https://pypi.org/project/flake8-future-annotations/)
- [flake8-gettext](https://pypi.org/project/flake8-gettext/)
- [flake8-implicit-str-concat](https://pypi.org/project/flake8-implicit-str-concat/)
- [flake8-import-conventions](https://github.com/joaopalmeiro/flake8-import-conventions)
- [flake8-logging](https://pypi.org/project/flake8-logging/)
- [flake8-logging-format](https://pypi.org/project/flake8-logging-format/)
- [flake8-no-pep420](https://pypi.org/project/flake8-no-pep420)
-
... [TRUNCATED]
```

### File: docs\requirements.txt
```txt
PyYAML==6.0.3
ruff==0.15.8
mkdocs==1.6.1
mkdocs-material==9.7.6
mkdocs-redirects==1.2.2
mdformat==1.0.0
mdformat-mkdocs==5.1.4
mkdocs-github-admonitions-plugin @ git+https://github.com/PGijsbers/admonitions.git#7343d2f4a92e4d1491094530ef3d0d02d93afbb7
mkdocs-llmstxt==0.2.0

```

### File: fuzz\README.md
```md
# ruff-fuzz

Fuzzers and associated utilities for automatic testing of Ruff.

## Usage

To use the fuzzers provided in this directory, start by invoking:

```bash
./fuzz/init-fuzzer.sh
```

This will install [`cargo-fuzz`](https://github.com/rust-fuzz/cargo-fuzz) and optionally download a
[dataset](https://zenodo.org/record/3628784) which improves the efficacy of the testing.

> [!NOTE]
>
> This step is necessary for initialising the corpus directory, as all fuzzers share a common corpus.

The dataset may take several hours to download and clean, so if you're just looking to try out the
fuzzers, skip the dataset download, though be warned that some features simply cannot be tested
without it (very unlikely for the fuzzer to generate valid python code from "thin air").

Once you have initialised the fuzzers, you can then execute any fuzzer with:

```bash
cargo fuzz run -s none name_of_fuzzer -- -timeout=1
```

> [!NOTE]
>
> Users using Apple M1 devices must use a nightly compiler and omit the `-s none` portion of this
> command, as this architecture does not support fuzzing without a sanitizer.
>
> ```shell
> cargo +nightly fuzz run name_of_fuzzer -- -timeout=1
> ```

You can view the names of the available fuzzers with `cargo fuzz list`.
For specific details about how each fuzzer works, please read this document in its entirety.

> [!NOTE]
>
> Re-run `./init-fuzzer.sh` (say no to the dataset download) after adding more file-based test cases
> to the repository. This will make sure that the corpus is up to date with any new Python code
> added to the repository.

### Debugging a crash

Once you've found a crash, you'll need to debug it.
The easiest first step in this process is to minimise the input such that the crash is still
triggered with a smaller input.
`cargo-fuzz` supports this out of the box with:

```bash
cargo fuzz tmin -s none name_of_fuzzer artifacts/name_of_fuzzer/crash-...
```

From here, you will need to analyse the input and potentially the behaviour of the program.
The debugging process from here is unfortunately less well-defined, so you will need to apply some
expertise here.
Happy hunting!

## A brief introduction to fuzzers

Fuzzing, or fuzz testing, is the process of providing generated data to a program under test.
The most common variety of fuzzers are mutational fuzzers; given a set of existing inputs (a
"corpus"), it will attempt to slightly change (or "mutate") these inputs into new inputs that cover
parts of the code that haven't yet been observed.
Using this strategy, we can quite efficiently generate testcases which cover significant portions of
the program, both with expected and unexpected data.
[This is really quite effective for finding bugs.](https://github.com/rust-fuzz/trophy-case)

The fuzzers here use [`cargo-fuzz`](https://github.com/rust-fuzz/cargo-fuzz), a utility which allows
Rust to integrate with [libFuzzer](https://llvm.org/docs/LibFuzzer.html), the fuzzer library built
into LLVM.
Each source file present in [`fuzz_targets`](fuzz_targets) is a harness, which is, in effect, a unit
test which can handle different inputs.
When an input is provided to a harness, the harness processes this data and libFuzzer observes the
code coverage and any special values used in comparisons over the course of the run.
Special values are preserved for future mutations and inputs which cover new regions of code are
added to the corpus.

## Each fuzzer harness in detail

Each fuzzer harness in [`fuzz_targets`](fuzz_targets) targets a different aspect of Ruff and tests
them in different ways. While there is implementation-specific documentation in the source code
itself, each harness is briefly described below.

### `ty_check_invalid_syntax`

This fuzz harness checks that the type checker (ty) does not panic when checking a source
file with invalid syntax. This rejects any corpus entries that is already valid Python code.
Currently, this is limited to syntax errors that's produced by Ruff's Python parser which means
that it does not cover all possible syntax errors (<https://github.com/astral-sh/ruff/issues/11934>).
A possible workaround for now would be to bypass the parser and run the type checker on all inputs
regardless of syntax errors.

### `ruff_parse_simple`

This fuzz harness does not perform any "smart" testing of Ruff; it merely checks that the parsing
and unparsing of a particular input (what would normally be a source code file) does not crash.
It also attempts to verify that the locations of tokens and errors identified do not fall in the
middle of a UTF-8 code point, which may cause downstream panics.
While this is unlikely to find any issues on its own, it executes very quickly and covers a large
and diverse code region that may speed up the generation of inputs and therefore make a more
valuable corpus quickly.
It is particularly useful if you skip the dataset generation.

### `ruff_parse_idempotency`

This fuzz harness checks that Ruff's parser is idempotent in order to check that it is not
incorrectly parsing or unparsing an input.
It can be built in two modes: default (where it is only checked that the parser does not enter an
unstable state) or full idempotency (the parser is checked to ensure that it will _always_ produce
the same output after the first unparsing).
Full idempotency mode can be used by enabling the `full-idempotency` feature when running the
fuzzer, but this may be too strict of a restriction for initial testing.

### `ruff_fix_validity`

This fuzz harness checks that fixes applied by Ruff do not introduce new errors using the existing
[`ruff_linter::test::test_snippet`](../crates/ruff_linter/src/test.rs) testing utility.
It currently is only configured to use default settings, but may be extended in future versions to
test non-default linter settings.

### `ruff_formatter_idempotency`

This fuzz harness ensures that the formatter is [idempotent](https://en.wikipedia.org/wiki/Idempotence)
which detects possible unsteady states of Ruff's formatter.

### `ruff_formatter_validity`

This fuzz harness checks that Ruff's formatter does not introduce new linter errors/warnings by
linting once, counting the number of each error type, then formatting, then linting again and
ensuring that the number of each error type does not increase across formats. This has the
beneficial side effect of discovering cases where the linter does not discover a lint error when
it should have due to a formatting inconsistency.

```

### File: playground\package.json
```json
{
  "name": "playground",
  "private": true,
  "version": "0.0.0",
  "type": "module",
  "scripts": {
    "check": "npm run dev:wasm && npm run lint && npm run tsc",
    "dev:wasm": "npm run dev:wasm --workspace ty-playground && npm run dev:wasm --workspace ruff-playground",
    "dev:build": "npm run dev:build --workspace ty-playground && npm run dev:build --workspace ruff-playground",
    "fmt": "prettier --cache -w .",
    "fmt:check": "prettier --cache --check .",
    "lint": "eslint --cache --ext .ts,.tsx ruff/src ty/src",
    "tsc": "tsc"
  },
  "workspaces": [
    "ty",
    "ruff",
    "shared"
  ],
  "prettier": {
    "trailingComma": "all"
  },
  "devDependencies": {
    "@eslint/js": "^9.21.0",
    "@tailwindcss/vite": "^4.0.14",
    "@types/react": "^19.0.11",
    "@types/react-dom": "^19.0.0",
    "@vitejs/plugin-react-swc": "^4.0.0",
    "eslint": "^9.22.0",
    "eslint-plugin-import": "^2.31.0",
    "eslint-plugin-react": "^7.31.11",
    "eslint-plugin-react-hooks": "^7.0.0",
    "prettier": "^3.5.3",
    "tailwindcss": "^4.0.14",
    "typescript": "^5.8.2",
    "typescript-eslint": "^8.26.1",
    "vite": "^7.0.0",
    "wasm-pack": "^0.14.0"
  }
}

```

### File: playground\README.md
```md
# playground

In-browser playground for Ruff. Available [https://play.ruff.rs/](https://play.ruff.rs/).

## Getting started

Install the NPM dependencies with `npm ci --ignore-scripts`, and run the development server with
`npm start --workspace ruff-playground` or `npm start --workspace ty-playground`.
You may need to restart the server after making changes to Ruff or ty to re-build the WASM
module.

To run the datastore, which is based
on [Workers KV](https://developers.cloudflare.com/workers/runtime-apis/kv/),
install the [Wrangler CLI](https://developers.cloudflare.com/workers/wrangler/install-and-update/),
then run `npx wrangler dev --local` from the `./playground/api` directory. Note that the datastore
is
only required to generate shareable URLs for code snippets. The development datastore does not
require Cloudflare authentication or login, but in turn only persists data locally.

## Architecture

The playground is implemented as a single-page React application powered by
[Vite](https://vitejs.dev/), with the editor experience itself powered by
[Monaco](https://github.com/microsoft/monaco-editor).

The playground stores state in `localStorage`, but supports persisting code snippets to
a persistent datastore based
on [Workers KV](https://developers.cloudflare.com/workers/runtime-apis/kv/)
and exposed via
a [Cloudflare Worker](https://developers.cloudflare.com/workers/learning/how-workers-works/).

The playground design is originally based on [Tailwind Play](https://play.tailwindcss.com/), with
additional inspiration from the [Biome Playground](https://biomejs.dev/playground/).

## Known issues

### Stack overflows

If you see stack overflows in the playground, build the WASM module in release mode:
`npm run --workspace ty-playground build:wasm`.

```

### File: crates\ty\README.md
```md
# ty

ty is an extremely fast type checker.

The Rust code for ty lives in this repository; see [CONTRIBUTING.md](CONTRIBUTING.md) for more
information on contributing to ty.

See [the ty repo](https://github.com/astral-sh/ty) for ty documentation and releases.

```

### File: playground\api\package.json
```json
{
  "name": "api",
  "version": "0.0.0",
  "devDependencies": {
    "@cloudflare/workers-types": "^4.20230801.0",
    "miniflare": "^4.0.0",
    "typescript": "^5.1.6",
    "wrangler": "^4.1.0"
  },
  "private": true,
  "scripts": {
    "start": "wrangler dev",
    "deploy": "wrangler publish"
  },
  "dependencies": {
    "@miniflare/kv": "^2.14.0",
    "@miniflare/storage-memory": "^2.14.0",
    "uuid": "^13.0.0"
  }
}

```

### File: playground\api\README.md
```md
# api

Key-value store based on [Workers KV](https://developers.cloudflare.com/workers/runtime-apis/kv/).

Used to persist code snippets in the playground and generate shareable URLs.

```

### File: playground\ruff\package.json
```json
{
  "name": "ruff-playground",
  "private": true,
  "version": "0.0.0",
  "type": "module",
  "scripts": {
    "prebuild": "npm run build:wasm",
    "build": "vite build",
    "build:wasm": "wasm-pack build ../../crates/ruff_wasm --target web --out-dir ../../playground/ruff/ruff_wasm",
    "dev:wasm": "wasm-pack build ../../crates/ruff_wasm --dev --target web --out-dir ../../playground/ruff/ruff_wasm",
    "predev:build": "npm run dev:wasm",
    "dev:build": "vite build",
    "prestart": "npm run dev:wasm",
    "start": "vite",
    "preview": "vite preview"
  },
  "dependencies": {
    "@monaco-editor/react": "^4.4.6",
    "classnames": "^2.3.2",
    "lz-string": "^1.5.0",
    "monaco-editor": "^0.55.0",
    "react": "^19.0.0",
    "react-dom": "^19.0.0",
    "react-resizable-panels": "^4.0.0",
    "ruff_wasm": "file:ruff_wasm",
    "shared": "0.0.0",
    "smol-toml": "^1.3.0"
  },
  "overrides": {
    "@monaco-editor/react": {
      "react": "$react",
      "react-dom": "$react-dom"
    }
  }
}

```

### File: playground\shared\package.json
```json
{
  "name": "shared",
  "private": true,
  "version": "0.0.0",
  "type": "module",
  "dependencies": {
    "@monaco-editor/react": "^4.7.0",
    "classnames": "^2.3.2",
    "fflate": "^0.8.2",
    "react-aria-components": "^1.16.0",
    "react": "^19.0.0",
    "react-resizable-panels": "^4.0.0"
  },
  "exports": "./src/index.ts"
}

```

### File: scripts\benchmarks\README.md
```md
# benchmarks

Utilities for benchmarking Ruff.

## Getting Started

Run `./scripts/benchmarks/setup.sh` to clone the benchmarking target (CPython).

If you're looking to benchmark Ruff against other tools, you'll also need to run `uv venv --project ./scripts/benchmarks`,
activate the venv and finally `uv sync --project ./scripts/benchmarks` to create a virtual environment with the required dependencies.

## Running Benchmarks

Run `./scripts/benchmarks/run.sh` to run Ruff over the target repo (CPython). The
`./scripts/benchmarks` folder contains a few other benchmarks (e.g., `scripts/benchmarks/run_comparisons.sh`
compares Ruff to a variety of other tools).

## Generating Plots

The Vega specification for the benchmark plot depicted in the root README can be found at
`scripts/benchmarks/graph-spec.json`. You can render this JSON spec in the [Vega Editor](https://vega.github.io/editor/#/edited).

The images seen in the README are generated by exporting the rendered Vega spec as SVG (at around
688px wide) and manually bolding the Ruff title and benchmark time. The dark mode variant is
generated by changing the fill from `fill="#333333"` to `fill="#C9D1D9"`.

```

### File: crates\ty_python_semantic\resources\README.md
```md
Markdown files within the `mdtest/` subdirectory are tests of type inference and type checking;
executed by the `tests/mdtest.rs` integration test.

See `crates/ty_test/README.md` for documentation of this test format.

```

### File: crates\ty_python_semantic\resources\mdtest\type_compendium\README.md
```md
# Type compendium

The type compendium contains "fact sheets" about important, interesting, and peculiar types in (ty's
interpretation of) Python's type system. It is meant to be an educational reference for developers
and users of ty. It is also a living document that ensures that our implementation of these types
and their properties is consistent with the specification.

## Table of contents

- [`Never`](never.md)
- [`Object`](object.md)
- [`None`](none.md)
- [Integer `Literal`s](integer_literals.md)
- String `Literal`s, `LiteralString`
- [`tuple` types](tuple.md)
- Class instance types
- [`Any`](any.md)
- Class literal types, `type[C]`, `type[object]`, `type[Any]`
- [`AlwaysTruthy`, `AlwaysFalsy`](always_truthy_falsy.md)
- [`Not[T]`](not_t.md)

```

### File: .markdownlint.yaml
```yaml
# default to true for all rules
default: true

# MD007/unordered-list-indent
MD007:
  indent: 4

# MD033/no-inline-html
MD033: false

# MD041/first-line-h1
MD041: false

# MD013/line-length
MD013: false

# MD014/commands-show-output
MD014: false

# MD024/no-duplicate-heading
MD024:
  # Allow when nested under different parents e.g. CHANGELOG.md
  siblings_only: true

# MD046/code-block-style
#
# Ignore this because it conflicts with the code block style used in content
# tabs of mkdocs-material which is to add a blank line after the content title.
#
# Ref: https://github.com/astral-sh/ruff/pull/15011#issuecomment-2544790854
MD046: false

# Link text should be descriptive
# Disallows link text like *here* which is annoying.
MD059: false

```

### File: .pre-commit-config.yaml
```yaml
fail_fast: false

exclude: |
  (?x)^(
    .github/workflows/release.yml|
    crates/ty_vendored/vendor/.*|
    crates/ty_project/resources/.*|
    crates/ty/docs/(configuration|rules|cli|environment).md|
    crates/ruff_benchmark/resources/.*|
    crates/ruff_linter/resources/.*|
    crates/ruff_linter/src/rules/.*/snapshots/.*|
    crates/ruff_notebook/resources/.*|
    crates/ruff_server/resources/.*|
    crates/ruff/resources/.*|
    crates/ruff_python_formatter/resources/.*|
    crates/ruff_python_formatter/tests/snapshots/.*|
    crates/ruff_python_resolver/resources/.*|
    crates/ruff_python_resolver/tests/snapshots/.*|
    crates/ty_completion_eval/truth/.*
  )$

repos:
  # Priority 0: Read-only hooks; hooks that modify disjoint file types.
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v6.0.0
    hooks:
      - id: check-merge-conflict
        priority: 0
      - id: end-of-file-fixer
        # Don't run this on all files: the absence of trailing newlines is often
        # intentional in parser/linter/formatter tests
        files: '^((crates/ty_python_semantic/resources/corpus/.*)|(.*\.toml))$'
        priority: 0

  - repo: https://github.com/abravalheri/validate-pyproject
    rev: v0.25
    hooks:
      - id: validate-pyproject
        priority: 0

  - repo: https://github.com/crate-ci/typos
    rev: v1.44.0
    hooks:
      - id: typos
        priority: 0

  - repo: local
    hooks:
      - id: rustfmt
        name: rustfmt
        entry: rustfmt
        language: system
        types: [rust]
        priority: 0
  # Prettier
  - repo: https://github.com/rbubley/mirrors-prettier
    rev: v3.8.1
    hooks:
      - id: prettier
        types: [yaml]
        priority: 0

  # zizmor detects security vulnerabilities in GitHub Actions workflows.
  # Additional configuration for the tool is found in `.github/zizmor.yml`
  - repo: https://github.com/zizmorcore/zizmor-pre-commit
    rev: v1.23.1
    hooks:
      - id: zizmor
        priority: 0

  - repo: https://github.com/python-jsonschema/check-jsonschema
    rev: 0.37.0
    hooks:
      - id: check-github-workflows
        priority: 0

  - repo: https://github.com/shellcheck-py/shellcheck-py
    rev: v0.11.0.1
    hooks:
      - id: shellcheck
        priority: 0

  - repo: https://github.com/executablebooks/mdformat
    rev: 1.0.0
    hooks:
      - id: mdformat
        language: python # means renovate will also update `additional_dependencies`
        additional_dependencies:
          - mdformat-mkdocs==5.1.4
          - mdformat-footnote==0.1.3
        exclude: |
          (?x)^(
            docs/formatter/black\.md
            | docs/\w+\.md
          )$
        priority: 0

  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.15.7
    hooks:
      - id: ruff-format
        exclude: crates/ty_python_semantic/resources/corpus/
        priority: 0
      - id: ruff-check
        args: [--fix, --exit-non-zero-on-fix]
        types_or: [python, pyi]
        exclude: crates/ty_python_semantic/resources/corpus/
        require_serial: true
        priority: 1

  # Priority 1: Second-pass fixers (e.g., markdownlint-fix runs after mdformat).
  - repo: https://github.com/igorshubovych/markdownlint-cli
    rev: v0.48.0
    hooks:
      - id: markdownlint-fix
        exclude: |
          (?x)^(
            docs/formatter/black\.md
            | docs/\w+\.md
          )$
        priority: 1

  # Priority 2: ruffen-docs runs after markdownlint-fix (both modify markdown).
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.15.7
    hooks:
      - id: ruff-format
        name: mdtest format
        types_or: [markdown]
        files: '^crates/.*/resources/mdtest/.*\.md$'
        pass_filenames: true
        priority: 2

  # `actionlint` hook, for verifying correct syntax in GitHub Actions workflows.
  # Some additional configuration for `actionlint` can be found in `.github/actionlint.yaml`.
  - repo: https://github.com/rhysd/actionlint
    rev: v1.7.11
    hooks:
      - id: actionlint
        stages:
          # This hook is disabled by default, since it's quite slow.
          # To run all hooks *including* this hook, use `uvx prek run -a --hook-stage=manual`.
          # To run *just* this hook, use `uvx prek run -a actionlint --hook-stage=manual`.
          - manual
        args:
          - "-ignore=SC2129" # ignorable stylistic lint from shellcheck
          - "-ignore=SC2016" # another shellcheck lint: seems to have false positives?
        language: golang # means renovate will also update `additional_dependencies`
        additional_dependencies:
          # actionlint has a shellcheck integration which extracts shell scripts in `run:` steps from GitHub Actions
          # and checks these with shellcheck. This is arguably its most useful feature,
          # but the integration only works if shellcheck is installed
          - "github.com/wasilibs/go-shellcheck/cmd/shellcheck@v0.11.1"
        priority: 0

```

### File: AGENTS.md
```md
# Ruff Repository

This repository contains both Ruff (a Python linter and formatter) and ty (a Python type checker). The crates follow a naming convention: `ruff_*` for Ruff-specific code and `ty_*` for ty-specific code. ty reuses several Ruff crates, including the Python parser (`ruff_python_parser`) and AST definitions (`ruff_python_ast`).

## Running Tests

Run all tests (using `nextest` for faster execution, setting `CARGO_PROFILE_DEV_OPT_LEVEL=1` to enable optimizations while retaining debug info, and setting `INSTA_FORCE_PASS=1 INSTA_UPDATE=always` to ensure all snapshots are updated):

```sh
CARGO_PROFILE_DEV_OPT_LEVEL=1 INSTA_FORCE_PASS=1 INSTA_UPDATE=always cargo nextest run
```

Run tests for a specific crate:

```sh
CARGO_PROFILE_DEV_OPT_LEVEL=1 INSTA_FORCE_PASS=1 INSTA_UPDATE=always cargo nextest run -p ty_python_semantic
```

Run a single mdtest file. The path to the mdtest file should be relative to the `crates/ty_python_semantic/resources/mdtest` folder:

```sh
CARGO_PROFILE_DEV_OPT_LEVEL=1 INSTA_FORCE_PASS=1 INSTA_UPDATE=always cargo nextest run -p ty_python_semantic -- mdtest::<path/to/mdtest_file.md>
```

To run a specific mdtest within a file, use a substring of the Markdown header text as `MDTEST_TEST_FILTER`. Only use this if it's necessary to isolate a single test case:

```sh
MDTEST_TEST_FILTER="<filter>" CARGO_PROFILE_DEV_OPT_LEVEL=1 INSTA_FORCE_PASS=1 INSTA_UPDATE=always cargo nextest run -p ty_python_semantic -- mdtest::<path/to/mdtest_file.md>
```

After running the tests, always review the contents of any snapshots that have been added or updated.

## Running Clippy

```sh
cargo clippy --workspace --all-targets --all-features -- -D warnings
```

## Running Debug Builds

Use debug builds (not `--release`) when developing, as release builds lack debug assertions and have slower compile times.

Run Ruff:

```sh
cargo run --bin ruff -- check path/to/file.py
```

Run ty:

```sh
cargo run --bin ty -- check path/to/file.py
```

## Reproducing and minimizing ty ecosystem changes

If asked to reproduce changes in the ty ecosystem, use this script to clone the project to some
directory and install its dependencies into `.venv`:

```sh
uv run scripts/setup_primer_project.py <project-name> <some-temp-dir>
```

If asked to *minimize* a change in the ty ecosystem, you should start off with the above command to ensure that the change reproduces. You should then attempt to minimize the Python code required to demonstrate a behaviour difference between ty on your feature branch and ty on the main branch. Your minimization process should consist of systematically removing files from the cloned ecosystem project, and stripping content from existing files, until the behaviour difference between your branch and `main` no longer reproduces.

## Pull Requests

When working on ty, PR titles should start with `[ty]` and be tagged with the `ty` GitHub label.

## Development Guidelines

- All changes must be tested. If you're not testing your changes, you're not done.
- Look to see if your tests could go in an existing file before adding a new file for your tests.
- Get your tests to pass. If you didn't run the tests, your code does not work.
- Follow existing code style. Check neighboring files for patterns.
- Rust imports should always go at the top of the file, never locally in functions.
- Always run `uvx prek run -a` at the end of a task, after every rebase, after addressing any review comment, and before pushing any code.
- Avoid writing significant amounts of new code. This is often a sign that we're missing an existing method or mechanism that could help solve the problem. Look for existing utilities first.
- Try hard to avoid patterns that require `panic!`, `unreachable!`, or `.unwrap()`. Instead, try to encode those constraints in the type system. Don't be afraid to write code that's more verbose or requires largeish refactors if it enables you to avoid these unsafe calls.
- Prefer let chains (`if let` combined with `&&`) over nested `if let` statements to reduce indentation and improve readability. At the end of a task, always check your work to see if you missed opportunities to use `let` chains.
- If you *have* to suppress a Clippy lint, prefer to use `#[expect()]` over `[allow()]`, where possible. But if a lint is complaining about unused/dead code, it's usually best to just delete the unused code.
- Use comments purposefully. Don't use comments to narrate code, but do use them to explain invariants and why something unusual was done a particular way.
- When adding new ty checks, it's important to make error messages concise. Think about how an error message would look on a narrow terminal screen. Sometimes more detail can be provided in subdiagnostics or secondary annotations, but it's also important to make sure that the diagnostic is understandable if the user has passed `--output-format=concise`.
- **Salsa incrementality (ty):** Any method that accesses `.node()` must be `#[salsa::tracked]`, or it will break incrementality. Prefer higher-level semantic APIs over raw AST access.
- Run `cargo dev generate-all` after changing configuration options, CLI arguments, lint rules, or environment variable definitions, as these changes require regeneration of schemas, docs, and CLI references.

```

### File: BREAKING_CHANGES.md
```md
# Breaking Changes

## 0.15.0

- **2026 formatter style guide**

    Ruff now formats your code according to the 2026 style guide. See the
    formatter section in the changelog or blog post for a detailed list of
    changes.

- **Block suppression comments in the linter**

    The linter now supports block suppression comments. For example, to suppress
    `N803` for all parameters in this function:

    ```python
    # ruff: disable[N803]
    def foo(
        legacyArg1,
        legacyArg2,
        legacyArg3,
        legacyArg4,
    ): ...
    # ruff: enable[N803]
    ```

- **Alpine Docker image**

    The `ruff:alpine` Docker image is now based on Alpine 3.23 (up from 3.21).

- **Debian Docker image**

    The `ruff:debian` and `ruff:debian-slim` Docker images are now based on Debian 13 "Trixie" instead of Debian 12 "Bookworm."

- **`ppc64` binaries**

    Binaries for the `ppc64` (64-bit big-endian PowerPC) architecture are no longer included in our releases. It should still be possible to build Ruff manually for this platform, if needed.

- **Default Python version and `extend`**

    Ruff now resolves all `extend`ed configuration files before falling back on a default Python version.

## 0.14.0

- **Default to Python 3.10**

    Ruff now defaults to Python 3.10 instead of 3.9 if no explicit Python
    version is configured using [`ruff.target-version`](https://docs.astral.sh/ruff/settings/#target-version)
    or [`project.requires-python`](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/#python-requires)
    ([#20725](https://github.com/astral-sh/ruff/pull/20725))

- **Default to Python 3.14 for syntax errors**

    Ruff will default to the _latest_ supported Python version (3.14) when
    checking for syntax errors without a Python version configured. The default
    in all other cases, like applying lint rules, remains at the minimum
    supported Python version (3.10).

## 0.13.0

- **Several rules can now add `from __future__ import annotations` automatically**

    `TC001`, `TC002`, `TC003`, `RUF013`, and `UP037` now add `from __future__ import annotations` as part of their fixes when the
    `lint.future-annotations` setting is enabled. This allows the rules to move
    more imports into `TYPE_CHECKING` blocks (`TC001`, `TC002`, and `TC003`),
    use PEP 604 union syntax on Python versions before 3.10 (`RUF013`), and
    unquote more annotations (`UP037`).

- **Full module paths are now used to verify first-party modules**

    Ruff now checks that the full path to a module exists on disk before
    categorizing it as a first-party import. This change makes first-party
    import detection more accurate, helping to avoid false positives on local
    directories with the same name as a third-party dependency, for example. See
    the [FAQ
    section](https://docs.astral.sh/ruff/faq/#how-does-ruff-determine-which-of-my-imports-are-first-party-third-party-etc) on import categorization for more details.

- **Deprecated rules must now be selected by exact rule code**

    Ruff will no longer activate deprecated rules selected by their group name
    or prefix. As noted below, the two remaining deprecated rules were also
    removed in this release, so this won't affect any current rules, but it will
    still affect any deprecations in the future.

- **The deprecated macOS configuration directory fallback has been removed**

    Ruff will no longer look for a user-level configuration file at
    `~/Library/Application Support/ruff/ruff.toml` on macOS. This feature was
    deprecated in v0.5 in favor of using the [XDG
    specification](https://specifications.freedesktop.org/basedir-spec/latest/)
    (usually resolving to `~/.config/ruff/ruff.toml`), like on Linux. The
    fallback and accompanying deprecation warning have now been removed.

- **[`pandas-df-variable-name`](https://docs.astral.sh/ruff/rules/pandas-df-variable-name) (`PD901`) has been removed**

- **[`non-pep604-isinstance`](https://docs.astral.sh/ruff/rules/non-pep604-isinstance) (`UP038`) has been removed**

## 0.12.0

- **Detection of more syntax errors**

    Ruff now detects version-related syntax errors, such as the use of the `match`
    statement on Python versions before 3.10, and syntax errors emitted by
    CPython's compiler, such as irrefutable `match` patterns before the final
    `case` arm.

- **New default Python version handling for syntax errors**

    Ruff will default to the _latest_ supported Python version (3.13) when
    checking for the version-related syntax errors mentioned above to prevent
    false positives in projects without a Python version configured. The default
    in all other cases, like applying lint rules, is unchanged and remains at the
    minimum supported Python version (3.9).

- **Updated f-string formatting**

    Ruff now formats multi-line f-strings with format specifiers to avoid adding a
    line break after the format specifier. This addresses a change to the Python
    grammar in version 3.13.4 that made such a line break a syntax error.

- **`rust-toolchain.toml` is no longer included in source distributions**

    The `rust-toolchain.toml` is used to specify a higher Rust version than Ruff's
    minimum supported Rust version (MSRV) for development and building release
    artifacts. However, when present in source distributions, it would also cause
    downstream package maintainers to pull in the same Rust toolchain, even if
    their available toolchain was MSRV-compatible.

- **[`suspicious-xmle-tree-usage`](https://docs.astral.sh/ruff/rules/suspicious-xmle-tree-usage/)
    (`S320`) has been removed**

## 0.11.0

This is a follow-up to release 0.10.0. Because of a mistake in the release process, the `requires-python` inference changes were not included in that release. Ruff 0.11.0 now includes this change as well as the stabilization of the preview behavior for `PGH004`.

- **Changes to how the Python version is inferred when a `target-version` is not specified** ([#16319](https://github.com/astral-sh/ruff/pull/16319))

    In previous versions of Ruff, you could specify your Python version with:

    - The `target-version` option in a `ruff.toml` file or the `[tool.ruff]` section of a pyproject.toml file.
    - The `project.requires-python` field in a `pyproject.toml` file with a `[tool.ruff]` section.

    These options worked well in most cases, and are still recommended for fine control of the Python version. However, because of the way Ruff discovers config files, `pyproject.toml` files without a `[tool.ruff]` section would be ignored, including the `requires-python` setting. Ruff would then use the default Python version (3.9 as of this writing) instead, which is surprising when you've attempted to request another version.

    In v0.10, config discovery has been updated to address this issue:

    - If Ruff finds a `ruff.toml` file without a `target-version`, it will check
        for a `pyproject.toml` file in the same directory and respect its
        `requires-python` version, even if it does not contain a `[tool.ruff]`
        section.
    - If Ruff finds a user-level configuration, the `requires-python` field of the closest `pyproject.toml` in a parent directory will take precedence.
    - If there is no config file (`ruff.toml`or `pyproject.toml` with a
        `[tool.ruff]` section) in the directory of the file being checked, Ruff will
        search for the closest `pyproject.toml` in the parent directories and use its
        `requires-python` setting.

## 0.10.0

- **Changes to how the Python version is inferred when a `target-version` is not specified** ([#16319](https://github.com/astral-sh/ruff/pull/16319))

    Because of a mistake in the release process, the `requires-python` inference changes are not included in this release and instead shipped as part of 0.11.0.
    You can find a description of this change in the 0.11.0 section.

- **Updated `TYPE_CHECKING` behavior** ([#16669](https://github.com/astral-sh/ruff/pull/16669))

    Previously, Ruff only recognized typechecking blocks that tested the `typing.TYPE_CHECKING` symbol. Now, Ruff recognizes any local variable named `TYPE_CHECKING`. This release also removes support for the legacy `if 0:` and `if False:` typechecking checks. Use a local `TYPE_CHECKING` variable instead.

- **More robust noqa parsing** ([#16483](https://github.com/astral-sh/ruff/pull/16483))

    The syntax for both file-level and in-line suppression comments has been unified and made more robust to certain errors. In most cases, this will result in more suppression comments being read by Ruff, but there are a few instances where previously read comments will now log an error to the user instead. Please refer to the documentation on [_Error suppression_](https://docs.astral.sh/ruff/linter/#error-suppression) for the full specification.

- **Avoid unnecessary parentheses around with statements with a single context manager and a trailing comment** ([#14005](https://github.com/astral-sh/ruff/pull/14005))

    This change fixes a bug in the formatter where it introduced unnecessary parentheses around with statements with a single context manager and a trailing comment. This change may result in a change in formatting for some users.

- **Bump alpine default tag to 3.21 for derived Docker images** ([#16456](https://github.com/astral-sh/ruff/pull/16456))

    Alpine 3.21 was released in Dec 2024 and is used in the official Alpine-based Python images. Now the ruff:alpine image will use 3.21 instead of 3.20 and ruff:alpine3.20 will no longer be updated.

- **\[`unsafe-markup-use`\]: `RUF035` has been recoded to `S704`** ([#15957](https://github.com/astral-sh/ruff/pull/15957))

## 0.9.0

Ruff now formats your code according to the 2025 style guide. As a result, your code might now get formatted differently. See the [changelog](./CHANGELOG.md#090) for a detailed list of changes.

## 0.8.0

- **Default to Python 3.9**

    Ruff now defaults to Python 3.9 instead of 3.8 if no explicit Python version is configured using [`ruff.target-version`](https://docs.astral.sh/ruff/settings/#target-version) or [`project.requires-python`](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/#python-requires) ([#13896](https://github.com/astral-sh/ruff/pull/13896))

- **Changed location of `pydoclint` diagnostics**

    [`pydoclint`](https://docs.astral.sh/ruff/rules/#pydoclint-doc) diagnostics now point to the first-line of the problematic docstring. Previously, this was not the case.

    If you've opted into these preview rules but have them suppressed using
    [`noqa`](https://docs.astral.sh/ruff/linter/#error-suppression) comments in
    some places, this change may mean that you need to move the `noqa` suppression
    comments. Most users should be unaffected by this change.

- **Use XDG (i.e. `~/.local/bin`) instead of the Cargo home directory in the standalone installer**

    Previously, Ruff's installer used `$CARGO_HOME` or `~/.cargo/bin` for its target install directory. Now, Ruff will be installed into `$XDG_BIN_HOME`, `$XDG_DATA_HOME/../bin`, or `~/.local/bin` (in that order).

    This change is only relevant to users of the standalone Ruff installer (using the shell or PowerShell script). If you installed Ruff using uv or pip, you should be unaffected.

- **Changes to the line width calculation**

    Ruff now uses a new version of the [unicode-width](https://github.com/unicode-rs/unicode-width) Rust crate to calculate the line width. In very rare cases, this may lead to lines containing Unicode characters being reformatted, or being considered too long when they were not before ([`E501`](https://docs.astral.sh/ruff/rules/line-too-long/)).

## 0.7.0

- The pytest rules `PT001` and `PT023` now default to omitting the decorator parentheses when there are no arguments
    ([#12838](https://github.com/astral-sh/ruff/pull/12838), [#13292](https://github.com/astral-sh/ruff/pull/13292)).
    This was a change that we attempted to make in Ruff v0.6.0, but only partially made due to an error on our part.
    See the [blog post](https://astral.sh/blog/ruff-v0.7.0) for more details.
- The `useless-try-except` rule (in our `tryceratops` category) has been recoded from `TRY302` to
    `TRY203` ([#13502](https://github.com/astral-sh/ruff/pull/13502)). This ensures Ruff's code is consistent with
    the same rule in the [`tryceratops`](https://github.com/guilatrova/tryceratops) linter.
- The `lint.allow-unused-imports` setting has been removed ([#13677](https://github.com/astral-sh/ruff/pull/13677)). Use
    [`lint.pyflakes.allow-unused-imports`](https://docs.astral.sh/ruff/settings/#lint_pyflakes_allowed-unused-imports)
    instead.

## 0.6.0

- Detect imports in `src` layouts by default for `isort` rules ([#12848](https://github.com/astral-sh/ruff/pull/12848))

- The pytest rules `PT001` and `PT023` now default to omitting the decorator parentheses when there are no arguments ([#12838](https://github.com/astral-sh/ruff/pull/12838)).

- Lint and format Jupyter Notebook by default ([#12878](https://github.com/astral-sh/ruff/pull/12878)).

    You can disable specific rules for notebooks using [`per-file-ignores`](https://docs.astral.sh/ruff/settings/#lint_per-file-ignores):

    ```toml
    [tool.ruff.lint.per-file-ignores]
    "*.ipynb" = ["E501"] # disable line-too-long in notebooks
    ```

    If you'd prefer to either only lint or only format Jupyter Notebook files, you can use the
    section-specific `exclude` option to do so. For example, the following would only lint Jupyter
    Notebook files and not format them:

    ```toml
    [tool.ruff.format]
    exclude = ["*.ipynb"]
    ```

    And, conversely, the following would only format Jupyter Notebook files and not lint them:

    ```toml
    [tool.ruff.lint]
    exclude = ["*.ipynb"]
    ```

    You can completely disable Jupyter Notebook support by updating the [`extend-exclude`](https://docs.astral.sh/ruff/settings/#extend-exclude) setting:

    ```toml
    [tool.ruff]
    extend-exclude = ["*.ipynb"]
    ```

## 0.5.0

- Follow the XDG specification to discover user-level configurations on macOS (same as on other Unix platforms)
- Selecting `ALL` now excludes deprecated rules
- The released archives now include an extra level of nesting, which can be removed with `--strip-components=1` when untarring.
- The release artifact's file name no longer includes the version tag. This enables users to install via `/latest` URLs on GitHub.

## 0.3.0

### Ruff 2024.2 style

The formatter now formats code according to the Ruff 2024.2 style guide. Read the [changelog](./CHANGELOG.md#030) for a detailed list of stabilized style changes.

### `isort`: Use one blank line after imports in typing stub files ([#9971](https://github.com/astral-sh/ruff/pull/9971))

Previously, Ruff used one or two blank lines (or the number configured by `isort.lines-after-imports`) after imp
... [TRUNCATED]
```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
