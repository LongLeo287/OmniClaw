---
id: qsv
type: knowledge
owner: OA_Triage
---
# qsv
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
## qsv: Blazing-fast Data-Wrangling toolkit

[![Linux build status](https://github.com/dathere/qsv/actions/workflows/rust.yml/badge.svg)](https://github.com/dathere/qsv/actions/workflows/rust.yml)
[![Windows build status](https://github.com/dathere/qsv/actions/workflows/rust-windows.yml/badge.svg)](https://github.com/dathere/qsv/actions/workflows/rust-windows.yml)
[![macOS build status](https://github.com/dathere/qsv/actions/workflows/rust-macos.yml/badge.svg)](https://github.com/dathere/qsv/actions/workflows/rust-macos.yml)
[![Security audit](https://github.com/dathere/qsv/actions/workflows/security-audit.yml/badge.svg)](https://github.com/dathere/qsv/actions/workflows/security-audit.yml)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/29e587760af64abcb115ba23efe1b365)](https://app.codacy.com/gh/dathere/qsv/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade)
[![Crates.io](https://img.shields.io/crates/v/qsv.svg?logo=crates.io)](https://crates.io/crates/qsv)
[![Discussions](https://img.shields.io/github/discussions/dathere/qsv)](https://github.com/dathere/qsv/discussions)
[![Minimum supported Rust version](https://img.shields.io/badge/Rust-1.94-red?logo=rust)](#minimum-supported-rust-version)
[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2Fjqnatividad%2Fqsv.svg?type=shield)](https://app.fossa.com/projects/git%2Bgithub.com%2Fjqnatividad%2Fqsv?ref=badge_shield) [![DOI](https://zenodo.org/badge/320463703.svg)](https://doi.org/10.5281/zenodo.17851335)
[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/dathere/qsv)

<div align="center">

 &nbsp;          |  Table of Contents
:--------------------------|:-------------------------
![qsv logo](docs/images/qsv_logo-gemini-indy-robothorse-small.png "Nano Banana Prompt: Can you make the horse robotic? Also, add an \"MCP\" label on the robotic horse. Keep the same pose and dimensions.")<br/>[_Hi-ho "Quicksilver" away!_](https://www.youtube.com/watch?v=p9lf76xOA5k)<br/><sub><sup>[original logo details](https://github.com/dathere/qsv/discussions/295) * [Base AI-reimagined logo](docs/images/qsv_logo-gemini-indy-robothorse-small.png) * [Event logo archive](docs/images/event-logos/)</sup></sub><br/>|qsv is a data-wrangling toolkit for querying, slicing,<br>sorting, analyzing, filtering, enriching, transforming,<br>validating, joining, formatting, converting, chatting,<br>[FAIR](https://www.go-fair.org/fair-principles/)ifying & documenting tabular data (CSV, Excel, [etc](#file-formats)).<br>Commands are simple, composable & ___["blazing fast"](https://github.com/dathere/qsv/discussions/1348)___.<br><br>* [Commands](#available-commands)<br>* Installation: [CLI](#installation-options) • [MCP Server](.claude/skills/docs/guides/START_HERE.md) • [Cowork Plugin](.claude/skills/docs/guides/START_HERE.md#step-2-optional-install-the-cowork-plugin)<br> * [Whirlwind Tour](docs/whirlwind_tour.md#a-whirlwind-tour) / [Notebooks](contrib/notebooks/) / [Lessons & Exercises](https://100.dathere.com)<br>* [FAQ](https://github.com/dathere/qsv/discussions/categories/faq)<br>* [Performance Tuning](docs/PERFORMANCE.md#performance-tuning)<br>* 👉 [Benchmarks](https://qsv.dathere.com/benchmarks) 🚀<br>* [Environment Variables](docs/ENVIRONMENT_VARIABLES.md)<br>* [Feature Flags](#feature-flags)<br>* [Goals/Non-goals](#goals--non-goals)<br>* [Testing](#testing)<br>* [NYC&nbsp;SOD&nbsp;2022](https://docs.google.com/presentation/d/e/2PACX-1vQ12ndZL--gkz0HLQRaxqsNOwzddkv1iUKB3sq661yA77OPlAsmHJHpjaqt9s9QEf73VqMfb0cv4jHU/pub?start=false&loop=false&delayms=3000)/[csv,conf,v8](https://docs.google.com/presentation/d/10T_3MyIqS5UsKxJaOY7Ktrd-GfhJelQImlE_qYmtuis/edit#slide=id.g2e0f1e7aa0e_0_62)/[PyConUS&nbsp;2025](https://docs.google.com/presentation/d/e/2PACX-1vRKFnU0Hm8oDrtCYbxcf96kHVsPcoLU05jPVNYaAs09D05gPMWDJ96q_4_zgUvadGro4deohisy-XtY/pub?start=false&loop=false&delayms=3000)/<br>&nbsp;&nbsp;&nbsp;[csv,conf,v9](https://docs.google.com/presentation/d/1j-S0q5gqR8agsqIPBVXabGEntMlc4FDTwb4r-v8-9tA/edit?usp=sharing)/[NYC&nbsp;SOD&nbsp;2026](https://docs.google.com/presentation/d/e/2PACX-1vTobPFucA1QO6u8dF3CyHjOctoom1DBmgQF558I_gx5e8cWPr0HLvJISvoaZyCMwLZZdDHlhK2cil0o/pub?start=false&loop=false&delayms=5000)<br>* **_"Have we achieved ACI?"_** series - [1](https://dathere.com/2026/01/the-peoples-api-is-finally-here/) • [2](https://dathere.github.io/NYC-Snow-Analysis-2010-2026-Claude-Cowork/)  • [3](https://dathere.github.io/peoples-api-demos/NYC-Housing-Policy-SOD2026/) <br>* [Sponsor](#sponsor)
</div>
<div align="center">

## Try it out at [qsv.dathere.com](https://qsv.dathere.com)! <!-- markdownlint-disable-line -->

</div>

| <a name="available-commands">Command | Description |
| --- | --- |
| [apply](docs/help/apply.md)✨<br>📇🚀🧠🤖🔣👆| Apply series of string, date, math & currency transformations to given CSV column/s. It also has some basic [NLP](https://en.wikipedia.org/wiki/Natural_language_processing) functions ([similarity](https://crates.io/crates/strsim), [sentiment analysis](https://crates.io/crates/vader_sentiment), [profanity](https://docs.rs/censor/latest/censor/), [eudex](https://github.com/ticki/eudex#eudex-a-blazingly-fast-phonetic-reductionhashing-algorithm), [language](https://crates.io/crates/whatlang) & [name gender](https://github.com/Raduc4/gender_guesser?tab=readme-ov-file#gender-guesser)) detection.  |
| [applydp](docs/help/applydp.md)✨<br>📇🚀🔣👆 ![CKAN](docs/images/ckan.png)| <a name="applydp_deeplink"></a>applydp is a slimmed-down version of `apply` with only [Datapusher+](https://github.com/dathere/datapusher-plus) relevant subcommands/operations (`qsvdp` binary variant only). |
| [behead](docs/help/behead.md) | Drop headers from a CSV. |
| [blake3](docs/help/blake3.md)<br>🚀 | Compute or check [BLAKE3](https://github.com/BLAKE3-team/BLAKE3/?tab=readme-ov-file#blake3) hashes of files. |
| [cat](docs/help/cat.md)<br>🗄️ | Concatenate CSV files by row or by column. |
| [clipboard](docs/help/clipboard.md)✨<br>🖥️ | Provide input from the clipboard or save output to the clipboard. |
| [color](docs/help/color.md)✨<br>🐻‍❄️🖥️ | Outputs tabular data as a pretty, colorized table that always fits into the terminal. Apart from CSV and its dialects, Arrow, Avro/IPC, Parquet, JSON array & JSONL formats are supported with the "polars" feature. |
| [count](docs/help/count.md)<br>📇🏎️🐻‍❄️ | Count the rows and optionally compile record width statistics of a CSV file. (11.87 seconds for a 15gb, 28m row NYC 311 dataset without an index. Instantaneous with an index.) If the `polars` feature is enabled, uses Polars' multithreaded, mem-mapped CSV reader for fast counts even without an index |
| [datefmt](docs/help/datefmt.md)<br>📇🚀👆 | Formats recognized date fields ([19 formats recognized](https://docs.rs/qsv-dateparser/latest/qsv_dateparser/#accepted-date-formats)) to a specified date format using [strftime date format specifiers](https://docs.rs/chrono/latest/chrono/format/strftime/). |
| [dedup](docs/help/dedup.md)<br>🤯🚀👆 | Remove duplicate rows (See also `extdedup`, `extsort`, `sort` & `sortcheck` commands). |
| [describegpt](docs/help/describegpt.md)<br>🌐🤖🪄🗃️📚⛩️ ![CKAN](docs/images/ckan.png) | <a name="describegpt_deeplink"></a>Infer a ["neuro-symbolic"](https://en.wikipedia.org/wiki/Neuro-symbolic_AI) Data Dictionary, Description & Tags or ask questions about a CSV with a [configurable, Mini Jinja prompt file](resources/describegpt_defaults.toml), using any [OpenAI API](https://platform.openai.com/docs/introduction)-compatible LLM, including local LLMs via [Ollama](https://ollama.com), [Jan](https://jan.ai) & [LM Studio](https://lmstudio.ai/).<br>(e.g. [Markdown](docs/describegpt/nyc311-describegpt.md), [JSON](docs/describegpt/nyc311-describegpt.json), [TOON](docs/describegpt/nyc311-describegpt.toon), [Everything](docs/describegpt/nyc311-describegpt-everything.md), [Spanish](docs/describegpt/nyc311-describegpt-spanish.md), [Mandarin](docs/describegpt/nyc311-describegpt-mandarin.md), [Controlled Tags](docs/describegpt/nyc311-describegpt-tagvocab.md);<br>[--prompt "What are the top 10 complaint types by community board & borough by year?"](docs/describegpt/nyc311-describegpt-prompt.md) - [deterministic, hallucination-free SQL RAG result](docs/describegpt/nyc311-describegpt-prompt.csv); [iterative, session-based SQL RAG refinement](docs/describegpt/allegheny_discussion3.md) - [refined SQL RAG result](docs/describegpt/mostexpensive6.csv)) |
| [diff](docs/help/diff.md)<br>🚀 | Find the difference between two CSVs with ludicrous speed!<br/>e.g. _compare two CSVs with 1M rows x 9 columns in under 600ms!_ |
| [edit](docs/help/edit.md) | Replace the value of a cell specified by its row and column. |
| [enum](docs/help/enum.md)<br>👆 | Add a new column enumerating rows by adding a column of incremental or uuid identifiers. Can also be used to copy a column or fill a new column with a constant value.  |
| [excel](docs/help/excel.md)<br>🚀 | Exports a specified Excel/ODS sheet to a CSV file. |
| [exclude](docs/help/exclude.md)<br>📇👆 | Removes a set of CSV data from another set based on the specified columns.  |
| [explode](docs/help/explode.md)<br>🔣👆 | Explode rows into multiple ones by splitting a column value based on the given separator.  |
| [extdedup](docs/help/extdedup.md)<br>👆 | Remove duplicate rows from an arbitrarily large CSV/text file using a memory-mapped, [on-disk hash table](https://crates.io/crates/odht). Unlike the `dedup` command, this command does not load the entire file into memory nor does it sort the deduped file. |
| [extsort](docs/help/extsort.md)<br>🚀📇👆 | Sort an arbitrarily large CSV/text file using a multithreaded [external merge sort](https://en.wikipedia.org/wiki/External_sorting) algorithm. |
| [fetch](docs/help/fetch.md)✨<br>📇🧠🌐 | Send/Fetch data to/from web services for every row using **HTTP Get**. Comes with [HTTP/2](https://http2-explained.haxx.se/en/part1) [adaptive flow control](https://medium.com/coderscorner/http-2-flow-control-77e54f7fd518), [jaq](https://github.com/01mf02/jaq?tab=readme-ov-file#jaq) JSON query language support, dynamic throttling ([RateLimit](https://www.ietf.org/archive/id/draft-ietf-httpapi-ratelimit-headers-06.html)) & caching with available persistent caching using [Redis](https://redis.io/) or a disk-cache. |
| [fetchpost](docs/help/fetchpost.md)✨<br>📇🧠🌐⛩️ | Similar to `fetch`, but uses **HTTP Post** ([HTTP GET vs POST methods](https://www.geeksforgeeks.org/difference-between-http-get-and-post-methods/)). Supports HTML form (application/x-www-form-urlencoded), JSON (application/json) and custom content types - with the ability to render payloads using CSV data using the [Mini Jinja](https://docs.rs/minijinja/latest/minijinja/) template engine. |
| [fill](docs/help/fill.md)<br>👆 | Fill empty values.  |
| [fixlengths](docs/help/fixlengths.md) | Force a CSV to have same-length records by either padding or truncating them. |
| [flatten](docs/help/flatten.md) | A flattened view of CSV records. Useful for viewing one record at a time.<br />e.g. `qsv slice -i 5 data.csv \| qsv flatten`. |
| [fmt](docs/help/fmt.md) | Reformat a CSV with different delimiters, record terminators or quoting rules. (Supports ASCII delimited data.)  |
| [foreach](docs/help/foreach.md)✨<br>📇 | Execute a shell command once per record in a given CSV file. |
| [frequency](docs/help/frequency.md)<br>📇😣🏎️👆🪄![Luau](docs/images/luau.png) | Build [frequency distribution tables](https://en.wikipedia.org/wiki/Frequency_(statistics)) of each column. Uses multithreading to go faster if an index is present (Examples: [CSV](scripts/nyc311-1m.freqs.csv) [JSON](scripts/nyc311-1m.freqs.json) [TOON](scripts/nyc311-1m.freqs.toon)). |
| [geocode](docs/help/geocode.md)✨<br>📇🧠🌐🚀🔣👆🌎 | Geocodes a location against an updatable local copy of the [Geonames](https://www.geonames.org/) cities & the [Maxmind GeoLite2](https://www.maxmind.com/en/geolite-free-ip-geolocation-data) databases. With caching and multi-threading, it geocodes up to 360,000 records/sec! |
| [geoconvert](docs/help/geoconvert.md)✨<br>🌎 | Convert between various spatial formats and CSV/SVG including GeoJSON, SHP, and more. |
| [headers](docs/help/headers.md)<br>🗄️ | Show the headers of a CSV. Or show the intersection of all headers between many CSV files. |
| [index](docs/help/index.md) | Create an index (📇) for a CSV. This is very quick (even the 15gb, 28m row NYC 311 dataset takes all of 14 seconds to index) & provides constant time indexing/random access into the CSV. With an index, `count`, `sample` & `slice` work instantaneously; random access mode is enabled in `luau`; and multithreading (🏎️) is enabled for the `frequency`, `split`, `stats` & `schema` commands. |
| [input](docs/help/input.md) | Read CSV data with special commenting, quoting, trimming, line-skipping & non-UTF8 encoding handling rules. Typically used to "normalize" a CSV for further processing with other qsv commands. |
| [join](docs/help/join.md)<br>😣👆 | Inner, outer, right, cross, anti & semi joins. Automatically creates a simple, in-memory hash index to make it fast.  |
| [joinp](docs/help/joinp.md)✨<br>🚀🐻‍❄️🪄 | Inner, outer, right, cross, anti, semi, non-equi & asof joins using the [Pola.rs](https://www.pola.rs) engine. Unlike the `join` command, `joinp` can process files larger than RAM, is multithreaded, has join key validation, a maintain row order option, pre and post-join filtering, join keys unicode normalization, supports "special" [non-equi joins](https://docs.pola.rs/user-guide/transformations/joins/#non-equi-joins) and [asof joins](https://docs.pola.rs/user-guide/transformations/joins/#asof-join) (which is [particularly useful for time series data](https://github.com/dathere/qsv/blob/30cc920d0812a854fcbfedc5db81788a0600c92b/tests/test_joinp.rs#L509-L983)) & its output columns can be coalesced. |
| [json](docs/help/json.md)<br>👆 | Convert JSON array to CSV.
| [jsonl](docs/help/jsonl.md)<br>🚀🔣 | Convert newline-delimited JSON ([JSONL](https://jsonlines.org/)/[NDJSON](http://ndjson.org/)) to CSV. See `tojsonl` command to convert CSV to JSONL.
| [lens](docs/help/lens.md)✨🗃️<br>🐻‍❄️🖥️ | Interactively view, search & filter tabular data files using the [csvlens](https://github.com/YS-L/csvlens#csvlens) engine. Apart from CSV and its dialects, Arrow, Avro/IPC, Parquet, JSON array & JSONL formats are supported with the "polars" feature. |
| [luau](docs/help/luau.md) ![Luau](docs/images/luau.png)✨<br>📇🌐🔣📚 ![CKAN](docs/images/ckan.png) | <a name="luau_deeplink"></a>Create multiple new computed columns, filter rows, compute aggregations and build complex data pipelines by executing a [Luau](https://luau-lang.org) [0.709](https://github.com/Roblox/luau/releases/tag/0.709) expression/script for every row of a CSV file ([sequential mode](https://github.com/dathere/qsv/blob/bb72c4ef369d192d85d8b7cc6e972c1b7df77635/tests/test_luau.rs#L254-L298)), or using [random access](https://www.webopedia.com/definitio
... [TRUNCATED]
```

### File: scripts\README.md
```md
# SCRIPTS

This directory contains various scripts for the project.

## benchmarks.sh - configurable benchmarking script
This script runs the benchmarks for the project. It takes one argument:

Usage: ./benchmarks.sh <argument>
  where <argument> is a substring pattern of the benchmark name.
  e.g. ./benchmarks.sh sort - will run benchmarks with "sort" in the benchmark name
  if <argument> is omitted, all benchmarks are executed.

  if <argument> is "reset", the benchmark data will be downloaded and prepared again.
   though the results/benchmark_results.csv and results/run_info_history.tsv historical
   archives will be preserved.
  if <argument> is "clean", temporary files will be deleted.
  if <argument> is "setup", setup and install all the required tools.
  if <argument> is "help", help text is displayed.

This script benchmarks Quicksilver (qsv) using a 520mb, 41 column, 1M row sample of
NYC's 311 data. If it doesn't exist on your system, it will be downloaded for you.

Though this script was primarily created to maintain the Benchmark page on the qsv site,
it was also designed to be a useful tool for users to benchmark qsv on their own systems,
so it be can run on hardware and workloads that reflect your requirements/environment.

See [benchmarks.sh](benchmarks.sh) for more details.

## misc/docopt-wordlist.bash - optional qsv tab completion support
qsv's command-line options are quite extensive. Thankfully, since it uses [docopt](http://docopt.org/) for CLI processing,
we can take advantage of [docopt.rs' tab completion support](https://github.com/docopt/docopt.rs#tab-completion-support) to make it
easier to use qsv at the command-line (currently, only bash shell is supported):

```bash
# install docopt-wordlist
cargo install docopt

# IMPORTANT: run these commands from the root directory of your qsv git repository
# to setup bash qsv tab completion
echo "DOCOPT_WORDLIST_BIN=\"$(which docopt-wordlist)"\" >> $HOME/.bash_completion
echo "source \"$(pwd)/scripts/misc/docopt-wordlist.bash\"" >> $HOME/.bash_completion
echo "complete -F _docopt_wordlist_commands qsv" >> $HOME/.bash_completion
```

```

### File: .claude\skills\package.json
```json
{
  "name": "@qsv/agent-skills",
  "version": "18.0.5",
  "description": "Agent Skills for qsv tabular data-wrangling toolkit",
  "type": "module",
  "main": "dist/index.js",
  "types": "dist/index.d.ts",
  "bin": {
    "qsv-mcp-server": "./dist/mcp-server.js"
  },
  "scripts": {
    "build": "tsc",
    "build:test": "tsc -p tsconfig.test.json",
    "test": "npm run build:test && node scripts/run-tests.js",
    "test:coverage": "npm run build:test && c8 --reporter=text node scripts/run-tests.js",
    "test:watch": "node --test --watch dist/tests/*.test.js",
    "test:examples": "node examples/basic.js",
    "test-update-checker": "node examples/update-checker-demo.js",
    "mcp:start": "node dist/mcp-server.js",
    "mcp:install": "node scripts/install-mcp.js",
    "mcpb:package": "node scripts/package-mcpb.js",
    "plugin:package": "node scripts/package-plugin.js",
    "plugin:install": "bash scripts/install-cowork-plugin.sh"
  },
  "keywords": [
    "qsv",
    "csv",
    "agent",
    "skills",
    "data-wrangling",
    "claude"
  ],
  "author": "Joel Natividad",
  "license": "MIT",
  "devDependencies": {
    "@types/node": "^20.0.0",
    "archiver": "^7.0.0",
    "c8": "^10.0.0",
    "typescript": "^5.0.0"
  },
  "dependencies": {
    "@modelcontextprotocol/ext-apps": "^1.2.0",
    "@modelcontextprotocol/sdk": "^1.26.0",
    "wink-bm25-text-search": "^3.0.0",
    "wink-nlp-utils": "^2.1.0"
  },
  "engines": {
    "node": ">=18.0.0"
  }
}

```

### File: .claude\skills\README.md
```md
# QSV Agent Skills

Complete TypeScript implementation for loading, executing, and composing qsv command pipelines with the Claude Agent SDK and Claude Desktop (MCP).

## 🎯 NEW: Work with Local Tabular Data Files Without Uploading!

The QSV MCP Server now supports **direct access to local tabular data files** (CSV, Excel, JSONL, etc.). No more uploading files to Claude Desktop!

**Getting Started**: See [docs/guides/START_HERE.md](./docs/guides/START_HERE.md)
**Full Guide**: See [docs/guides/FILESYSTEM_USAGE.md](./docs/guides/FILESYSTEM_USAGE.md)

### Key Features:
- ✅ Browse tabular data files in your directories (CSV, Excel, JSONL, etc.)
- ✅ Process files without uploading
- ✅ No input file size limits (streams large files efficiently)
- ✅ Smart output handling (auto-saves large results > 850KB to disk)
- ✅ Instant access
- ✅ Secure path validation

## Overview

This directory contains:

1. **51 Auto-generated Skill Definitions** - JSON files describing all qsv commands (parsed with qsv-docopt)
2. **TypeScript Executor** - Complete implementation for running qsv skills
3. **MCP Server with Filesystem Access** - Model Context Protocol server for Claude Desktop integration
5. **Working Demos** - Practical demonstrations of the system

Each skill file provides:
- **Command specification**: Binary, subcommand, arguments, and options (parsed with qsv-docopt)
- **Rich descriptions**: Extracted from usage text
- **Usage examples**: Real usage examples from documentation (180 total)
- **Type information**: Inferred parameter types and validation
- **Performance hints**: Memory usage, streaming capability, indexing benefits
- **Links to tests**: For additional context and validation

## Quick Start

### Installation

**Choose your installation method:**

<details>
<summary><b>🎁 Desktop Extension (Recommended for GUI users)</b> - Easiest installation, automatic updates, zero configuration</summary>

**Perfect for**: Most users, especially non-technical users

**Requirements**: Claude Desktop + qsv binary

**Installation**:
1. Install qsv: `brew install qsv` (macOS) or see [qsv installation](https://github.com/dathere/qsv#installation)
2. Download `qsv-mcp-server.mcpb` from releases
3. Double-click the `.mcpb` file (opens with Claude Desktop)
4. **That's it!** qsv binary path is auto-detected, no manual configuration needed
5. Restart Claude Desktop

Auto-detection finds qsv in standard locations (PATH, /usr/local/bin, ~/.cargo/bin, etc.)

**Documentation**: [docs/guides/START_HERE.md](./docs/guides/START_HERE.md)

</details>

<details>
<summary><b>💻 Claude Code (Recommended for CLI users)</b> - Terminal-based, perfect for developers</summary>

**Perfect for**: Developers, terminal users, automation, remote servers, SSH workflows

**Requirements**: Claude Code CLI + Node.js ≥ 18.0.0 + qsv binary

**Installation**:
```bash
cd .claude/skills
npm install
npm run build
npm run mcp:install  # Detects and configures Claude Code automatically
```

**Benefits**:
- ✅ Terminal integration - work with files in current directory
- ✅ Scriptable - automate data workflows
- ✅ Works over SSH - process data on remote servers
- ✅ Git integration - see operations in repository context
- ✅ Lightweight - no GUI overhead

**Documentation**: [docs/guides/CLAUDE_CODE.md](./docs/guides/CLAUDE_CODE.md)

</details>

<details>
<summary><b>⚙️ Legacy MCP Server</b> - Maximum flexibility, for advanced users</summary>

**Perfect for**: Advanced users who want full config file control, using non-Claude MCP clients

**Requirements**: Node.js ≥ 18.0.0 + npm + qsv binary

**Installation**:
```bash
cd .claude/skills
npm install
npm run build
npm run mcp:install  # Interactive configuration
```

This will:
1. Build TypeScript code
2. Prompt for configuration (qsv path, allowed directories, etc.)
3. Update Claude Desktop config file automatically
4. Restart Claude Desktop to activate

**Manual configuration**: Edit `~/Library/Application Support/Claude/claude_desktop_config.json`

</details>

**All methods provide identical qsv functionality** - choose based on your interface preference (GUI vs CLI) and use case.

### Run Examples (Legacy MCP Server only)

```bash
# Basic skill loading and execution
npm test

# Package as Desktop Extension
npm run mcpb:package
```

## Generated Skills (51)

| Category | Count | Skills |
|----------|-------|--------|
| **utility** | 23 | cat, clipboard, count, headers, index, input, partition, pseudo, reverse, sniff, split, template, etc. |
| **transformation** | 5 | rename, replace, transpose, etc. |
| **aggregation** | 5 | frequency, moarstats, stats, count, pragmastat |
| **conversion** | 5 | excel, json, jsonl, tojsonl, etc. |
| **selection** | 3 | select, slice, sample |
| **filtering** | 2 | search, searchset |
| **formatting** | 3 | fmt, fixlengths, table |
| **joining** | 2 | join, joinp |
| **validation** | 3 | schema, safenames, validate |
| **documentation** | 1 | describegpt |

**Total Statistics:**
- **Skills**: 51 commands
- **Usage Examples**: 180 from documentation
- **Options**: 607 command-line options
- **Arguments**: 89 positional arguments

## Project Structure

```
.claude/skills/
├── qsv/                    # 51 skill JSON definitions
│   ├── qsv-select.json
│   ├── qsv-stats.json
│   ├── qsv-moarstats.json
│   └── ... (48 more)
├── src/                    # TypeScript source
│   ├── types.ts           # Type definitions
│   ├── loader.ts          # Skill loading
│   ├── executor.ts        # qsv execution wrapper
│   ├── mcp-server.ts      # MCP server implementation
│   ├── mcp-tools.ts       # MCP tool definitions
│   ├── mcp-filesystem.ts  # Filesystem resource provider
│   ├── mcp-sampling.ts    # MCP sampling support
│   ├── bm25-search.ts     # BM25 search index for tool discovery
│   ├── browse-directory.ts # Directory browser (MCP Apps)
│   ├── config.ts          # Configuration and validation
│   ├── converted-file-manager.ts  # LIFO cache for converted files
│   ├── duckdb.ts          # DuckDB integration for SQL queries
│   ├── installer.ts       # Binary installer
│   ├── update-checker.ts  # Version detection and skill regeneration
│   ├── utils.ts           # Utility functions
│   ├── version.ts         # Version management
│   ├── wink-bm25-text-search.d.ts  # BM25 type declarations
│   ├── wink-nlp-utils.d.ts         # NLP utils type declarations
│   ├── ui/                # UI components
│   │   └── directory-picker-html.ts
│   └── index.ts           # Public exports
├── scripts/
│   ├── install-mcp.js     # MCP installation helper
│   ├── package-mcpb.js    # MCPB packaging script
│   ├── package-plugin.js  # Plugin packaging script
│   ├── cowork-setup.cjs   # Claude Cowork integration setup
│   └── run-tests.js       # Cross-platform test runner
├── dist/                   # Compiled JavaScript (gitignored)
├── package.json
├── tsconfig.json
├── mcp-config.json         # Claude Desktop config template
├── README.md               # This file
├── README-MCP.md           # MCP server documentation
├── CHANGELOG.md            # Release notes
└── docs/                   # Documentation
    ├── guides/             # User guides
    ├── reference/          # Technical reference
    └── desktop/            # Desktop extension documentation
```

## Usage

### Basic Skill Execution

```typescript
import { SkillLoader, SkillExecutor } from './dist/index.js';

// Load all 51 skills
const loader = new SkillLoader();
await loader.loadAll();

// Search for skills
const dedupSkills = loader.search('duplicate');
// Returns: qsv-dedup, qsv-extdedup, qsv-diff, etc.

// Execute a skill
const executor = new SkillExecutor();
const skill = await loader.load('qsv-select');

const result = await executor.execute(skill, {
  args: { selection: '1-5' },
  stdin: csvData
});

console.log(result.output);
```

## Skill Schema

Each skill JSON file follows this structure:

```json
{
  "name": "qsv-<command>",
  "version": "12.0.0",
  "description": "Command description from usage text",
  "category": "selection|filtering|transformation|aggregation|...",
  "command": {
    "binary": "qsv",
    "subcommand": "<command>",
    "args": [
      {
        "name": "argument_name",
        "type": "string|number|file|regex",
        "required": true|false,
        "description": "Argument description",
        "examples": []
      }
    ],
    "options": [
      {
        "flag": "--option",
        "short": "-o",
        "type": "flag|string|number",
        "description": "Option description",
        "default": "value"
      }
    ]
  },
  "examples": [
    {
      "description": "What this example does",
      "command": "qsv command example"
    }
  ],
  "hints": {
    "streamable": true,
    "indexed": false,
    "memory": "constant"
  },
  "test_file": "https://github.com/dathere/qsv/blob/master/tests/test_<command>.rs"
}
```

## Generation

### Skill Definitions

Skills are auto-generated from qsv command USAGE text using the `--update-mcp-skills` flag:

```bash
# Must be run from within the qsv repository directory
cd /path/to/qsv
qsv --update-mcp-skills

# Output: .claude/skills/qsv/*.json
```

The generator uses **qsv-docopt Parser** (the same parser qsv uses at runtime) for robust parsing:
1. Extracts `USAGE` static string from command source files
2. **Parses with qsv-docopt** for accurate argument/option detection
3. Extracts descriptions from USAGE text
4. Infers types from names and descriptions
5. Detects performance hints from emoji markers (🤯 📇 🏎️ 😣)
6. Generates structured JSON skill definitions

## Type Inference

The generator infers parameter types:

| Pattern | Inferred Type |
|---------|---------------|
| `<input>`, `<file>` | `file` |
| `<number>`, `<count>` | `number` |
| `<regex>`, `<pattern>` | `regex` |
| `<selection>`, `<column>` | `string` |
| Default | `string` |

## Performance Hints

Hints are extracted from usage text markers:

- 🤯 → `memory: "full"` (loads entire file)
- 📇 → `indexed: true` (benefits from index)
- 🏎️ → `parallel: true` (supports parallel execution)
- 😣 → `memory: "proportional"` (memory scales with cardinality)

## API Documentation

See [docs/reference/SKILLS_API.md](./docs/reference/SKILLS_API.md) for complete API documentation including:

- SkillLoader API (loading, searching, statistics)
- SkillExecutor API (execution, validation)
- QsvPipeline API (15 convenience methods)
- Type definitions
- Advanced examples

## Integration with Claude Agent SDK

```typescript
import { Agent } from '@anthropic-ai/agent-sdk';
import { SkillLoader } from './dist/index.js';

const loader = new SkillLoader();
await loader.loadAll();

const agent = new Agent({
  skills: Array.from((await loader.loadAll()).values())
});

// Agent can now discover and invoke qsv skills
await agent.chat("Remove duplicates from sales.csv");
// Agent automatically finds and invokes qsv-dedup
```

## Integration with Claude Desktop (MCP Server)

The QSV MCP Server exposes all 51 qsv skill-based commands to Claude Desktop through the Model Context Protocol.

### Quick Start

```bash
# Install and configure
cd .claude/skills
npm install
npm run mcp:install
```

This will:
1. Build the MCP server
2. Update Claude Desktop configuration
3. Enable qsv tools in Claude Desktop

### Manual Configuration

Edit `~/Library/Application Support/Claude/claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "qsv": {
      "command": "node",
      "args": ["/path/to/qsv/.claude/skills/dist/mcp-server.js"],
      "env": {
        "QSV_MCP_BIN_PATH": "/usr/local/bin/qsv",
        "QSV_MCP_WORKING_DIR": "/Users/your-username/Downloads",
        "QSV_MCP_ALLOWED_DIRS": "/Users/your-username/Downloads:/Users/your-username/Documents"
      }
    }
  }
}
```

Restart Claude Desktop to load the server.

### Usage

Once configured, use natural language in Claude Desktop:

```
"Select columns 1-5 from data.csv"
"Calculate statistics for the price column in sales.csv"
"Remove duplicates from data.csv and sort by revenue"
"Show me an example of joining two CSV files"
```

Claude will automatically:
- Select the appropriate qsv tool
- Execute the command
- Return results or explanations

### What's Available

- **24+ MCP Tools**: 10 core tools (search, config, set_working_dir, get_working_dir, filesystem, log, command, to_parquet, index, stats) + 13 common command tools (including sniff). `qsv_browse_directory` is also available when MCP Apps are supported.
- **Local File Access**: Browse and process tabular data files (CSV, Excel, JSONL, etc.) directly from your filesystem
- **File-Based Processing**: Works with your local files without uploading
- **Natural Language Interface**: No command syntax needed

For complete MCP documentation, see [README-MCP.md](./README-MCP.md).

## Development

```bash
# Install dependencies
npm install

# Build TypeScript
npm run build

# Run demos
npm test                              # Basic skill usage
npm run mcp:install                   # Install MCP server for Claude Desktop

# Regenerate skills (from qsv repository root)
cd /path/to/qsv
qsv --update-mcp-skills
```

## Documentation

### Installation & Setup
- [Getting Started Guide](./docs/guides/START_HERE.md) - Install qsv MCP Server + Cowork Plugin (recommended)
- [MCP Server Guide](./README-MCP.md) - Claude Desktop integration (legacy method)
- [Auto-Update Guide](./docs/reference/AUTO_UPDATE.md) - Keep skills in sync with qsv releases

### Usage & Features
- [Additional Servers Guide](./docs/guides/ADDITIONAL_SERVERS.md) - Census + Wikidata MCP servers
- [Filesystem Usage Guide](./docs/guides/FILESYSTEM_USAGE.md) - Local file access
- [Complete API Documentation](./docs/reference/SKILLS_API.md)
- [qsv Commands](https://github.com/dathere/qsv#commands)

## Requirements

- Node.js >= 18.0.0
- qsv installed and in PATH (for execution)
- TypeScript 5.0+ (for development)

## License

MIT

---

**Updated**: 2026-03-22
**Version**: 18.0.5
**Generator**: `qsv --update-mcp-skills`
**Skills**: 51 commands
**Usage Examples**: 180 from documentation
**Parsing**: qsv-docopt (robust, accurate)
**Features**: MCP server, filesystem access, type-safe execution
**Status**: ✅ Production Ready

```

### File: contrib\completions\README.md
```md
# qsv completions - bash, zsh, fish, powershell, nushell, fig, elvish

Generate shell completions for qsv including the following shells:

-   bash
-   zsh
-   powershell
-   fish
-   nushell
-   fig
-   elvish

Completions are **auto-generated** from qsv's `static USAGE` text in `src/cmd/*.rs`, so they stay in sync with the CLI automatically. No manual command definition files to maintain.

> Status as of qsv release 16.0.0: Completions for 66 commands (all qsv commands except `applydp` and `generate` -- `applydp` is specific to DataPusher+ and `generate` is not usually distributed with qsv anymore) are auto-generated with short and long flags, subcommands, and value-taking hints. Completions may not account for file paths (you may need to explicitly use a relative path for example starting with `./` to begin file completions). Not all shells have been verified to work with the generated completions.

## Usage

You may use one of the completions in the `examples` folder or follow the following instructions to generate them.

To generate completions for all shells into an examples folder run the `generate_examples.bash` script from `contrib/completions/` within the qsv repository:

```bash
bash generate_examples.bash
```

To generate a completion manually run:

```bash
cargo run -- <shell>
```

Replace `<shell>` with any of the shells mentioned above.

The completions output should be printed to your terminal. You may redirect this to a file. For example for Bash completions:

```bash
cargo run -- bash > completions.bash
```

Then run them as your shell intends it to be ran.

## How It Works

At runtime, the tool:

1. Locates the qsv repository root (walks up from CWD looking for `Cargo.toml` + `src/cmd/`)
2. Reads the `static USAGE` text from each `src/cmd/*.rs` file
3. Parses USAGE text with `qsv_docopt` to discover flags, option types, and subcommands
4. Builds a `clap::Command` tree and feeds it to `clap_complete` for the requested shell

## Updating Completions

When qsv adds, removes, or modifies commands or flags, just regenerate:

```bash
bash generate_examples.bash
```

No other changes are needed in this project.

```

### File: scripts\misc\README.md
```md
For convenience, the [docopt-wordlist.bash from the docopt.rs project](https://github.com/docopt/docopt.rs/blob/master/completions/docopt-wordlist.bash) is bundled here to quickly install qsv tab completion support.

```

### File: scripts\results\README.md
```md
These benchmarks are compiled on an Apple Mac Mini 2023 model with an M2 Pro chip with 12 CPU cores & 32GB of RAM; a 1TB SSD primary drive & a 1TB Samsung SSD 970 Evo plus external drive running the latest macOS at the time (see [run_info_history.tsv](run_info_history.tsv)).

It uses the prebuilt, CPU optimized qsv binary variant in aarch64-apple-darwin.zip found at `https://github.com/dathere/qsv/releases/latest`.

The benchmarks were performed on a million row, 41 column, 520 MB sample of NYC's 311 data.
`https://raw.githubusercontent.com/wiki/dathere/qsv/files/NYC_311_SR_2010-2020-sample-1M.7z`

Each benchmark is executed five times using hyperfine v1.18.0. Two warmup runs followed by three benchmark runs.

Records per second is calculated by dividing the number of records (1M) by the mean of the three benchmark runs. All other measurements are in seconds.

```

### File: resources\luau\vendor\README.md
```md
As date manipulation is an oft-used feature in many applications, qsv vendors the `LuaDate` library at https://github.com/Tieske/date. This library provides a comprehensive set of date manipulation functions in the `luau` command.

See https://tieske.github.io/date/ for more information.

```

### File: .markdownlint.json
```json
{
    "MD009": false,
    "MD013": false,
    "MD022": false,
    "MD032": false,
    "MD033": false,
    "MD037": false,
    "MD040": false,
    "MD041": false
}

```

### File: build.rs
```rs
fn main() {
    // we use TARGET in --version and user-agent strings
    println!(
        "cargo:rustc-env=TARGET={}",
        std::env::var("TARGET").unwrap()
    );
    // QSV_KIND is used to determine how qsv was built and is displayed in --version
    // check PERFORMANCE.md for more info
    println!(
        "cargo:rustc-env=QSV_KIND={}",
        std::env::var("QSV_KIND").unwrap_or_else(|_| "compiled".to_string())
    );

    #[cfg(feature = "polars")]
    {
        use std::{fs, path::Path};

        // This is the string that is searched for in Cargo.toml to find the Polars revision
        const QSV_POLARS_REV: &str = "# QSV_POLARS_REV=";

        // QSV_POLARS_REV contains either the commit id short hash or the git tag
        // of the Polars version qsv was built against
        let cargo_toml_path = Path::new("Cargo.toml");
        let cargo_toml_content =
            fs::read_to_string(cargo_toml_path).expect("Failed to read Cargo.toml");
        let polars_rev = cargo_toml_content.find(QSV_POLARS_REV).map_or_else(
            || "unknown".to_string(),
            |index| {
                let start_index = index + QSV_POLARS_REV.len();
                let end_index = cargo_toml_content[start_index..]
                    .find('\n')
                    .map_or(cargo_toml_content.len(), |i| start_index + i);
                let final_rev = cargo_toml_content[start_index..end_index]
                    .trim()
                    .to_string();
                if final_rev.is_empty() {
                    "release".to_string()
                } else {
                    final_rev
                }
            },
        );
        println!("cargo:rustc-env=QSV_POLARS_REV={polars_rev}");
    }
}

```

### File: CLAUDE.md
```md
# CLAUDE.md

## General Rules

When unsure how to use a project tool or publish workflow, check existing docs first (e.g., marketplace docs, plugin docs) before guessing. Never fabricate CLI flags.

## Documentation

When counting items in documentation (tools, commands, features), always verify counts by explicitly listing and numbering each item. Never estimate counts.

## Tools & commands

- Build qsv: `cargo build --locked --bin qsv -F all_features`
- Build qsvlite: `cargo build --locked --bin qsvlite -F lite`
- Build qsvmcp: `cargo build --locked --bin qsvmcp -F qsvmcp`
- Build qsvdp: `cargo build --locked --bin qsvdp -F datapusher_plus`
- Do not use `--release` during development.
- Test qsv: `cargo test -F all_features`
- Test qsvlite: `cargo test -F lite`
- Test qsvmcp: `cargo test -F qsvmcp`
- Test qsvdp: `cargo test -F datapusher_plus`
- Test single command: `cargo t stats -F all_features`
- Test specific function: `cargo t test_stats::stats_cache -F all_features`
- Regenerate MCP skill JSONs: `qsv --update-mcp-skills`

## Workflow requirements

Adding a new command requires changes in multiple places:
1. Create `src/cmd/yourcommand.rs` following the pattern in any existing command
2. Add module declaration in `src/cmd/mod.rs`
3. Add command registration in `src/main.rs` (conditional on features)
4. Add feature flag in `Cargo.toml` if needed
5. Create `tests/test_yourcommand.rs`
6. Add usage text with examples and link to test file
7. Update README.md with command description

## Rust / qsv Development

For qsv Rust work: after editing code, always run `cargo test` and `cargo clippy` before committing. For feature-gated code, test with the relevant feature flag enabled.

## Code Review Response

For Copilot/code review responses: apply the fix, run tests, commit, and reply to the review comment. Do not dismiss review findings without verifying them in code first.

## Debugging

When debugging, state your hypothesis explicitly before investigating. If the first hypothesis fails, don't try variations of the same idea — step back and consider fundamentally different root causes.

```

### File: CODE_OF_CONDUCT.md
```md
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
codeofconduct@datHere.com.
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

### File: CONTRIBUTING.md
```md
# Contributing

We welcome and encourage all contributions to the project. Please read the following guidelines before submitting a pull request.

## Code Contributions

For code contributions, we follow several conventions:

* Please run `cargo +nightly fmt` before submitting a pull request. We use [rustfmt settings](https://github.com/dathere/qsv/blob/master/rustfmt.toml) that require nightly.
* Please run `cargo +nightly clippy -F all_features -- -W clippy::perf` before submitting a pull request. The project has its clippy preferences set [here](https://github.com/dathere/qsv/blob/bb4f4c7d683719a30f5e9552d16fba96a6872ce9/src/main.rs#L1-L36), and we generally apply clippy's suggestions with those preferences unless there is a good reason not to.   
In that case, our practice is to suppress lints for each specific instance with an optional comment so it does not show up again in future clippy runs, e.g:  

```rust
#[allow(clippy::unused_assignments)]
let mut var_a = String::with_capacity(10); // amortize allocation
```

* Ensure you have the latest version of Rust nightly installed (`rustup toolchain update nightly`), as we use it for clippy and rustfmt. Running `cargo +nightly fmt` and `cargo +nightly clippy` may return different results if you are not using the latest nightly version of Rust.
* We use docopt for command line argument parsing as we fully take advantage of its ability to parse command line arguments from the contiguous, verbose usage text that is at the beginning of each command's source code that more popular libraries like clap or structopt do not offer.   
However, since [docopt.rs is unmaintained](https://github.com/docopt/docopt.rs#this-crate-is-unmaintained), we have a [fork](https://github.com/dathere/qsv-docopt) that will be maintained along with this project. See this [discussion thread](https://github.com/dathere/qsv/discussions/463) for more details.
* `unwrap()` and `expect()` are allowed, but there should be an accompanying comment detailing safety
* TODO: explain testing conventions, and test helpers
* TODO: explain error handling conventions
* TODO: explain logging conventions
* TODO: release practices
* TODO: explain the various GitHub Action workflows

## Recipe Contributions

We also welcome and highly encourage recipe contributions!

The recipes need not be all that complicated or use `qsv` exclusively (feel free to mix and match qsv with other CLI tools) but they should be useful and not trivial. We also ask that you include a short description of the recipe, and a link to the source of the recipe if it is not your own.

Just go to the [Cookbook](https://github.com/dathere/qsv/wiki/Cookbook#cookbook) and add your recipe.

Once you add a recipe, show it in action! Add a [_"Show and tell"_](https://github.com/dathere/qsv/discussions/categories/show-and-tell) entry in [Discussions](https://github.com/dathere/qsv/discussions), and link to your recipe.

## Documentation Contributions

We are always looking for ways to improve the documentation. If you find a typo, or have a suggestion for improvement, please submit a pull request.

And if you want to add a new page to the Wiki, please do! Just make sure to add section headers to your Wiki contributions, so it automatically shows up in the sidebar.

If you are not familiar with GitHub Wikis, you can find a guide [here](https://docs.github.com/en/github/building-a-strong-community/adding-or-editing-wiki-pages#adding-wiki-pages).

```

### File: GEMINI.md
```md
# qsv: Blazing-fast Data-Wrangling Toolkit

## Project Overview

`qsv` is a high-performance command-line program for querying, slicing, sorting, analyzing, filtering, enriching, transforming, validating, joining, formatting, and documenting tabular data (CSV, Excel, etc.). It is a fork of the popular `xsv` utility, significantly expanded with numerous features and commands.

### Key Technologies
- **Language:** Rust (requires latest stable or nightly)
- **CLI Parser:** `docopt` (via a maintained fork `qsv_docopt`)
- **Core Engine:** `csv` crate for fast parsing, `polars` for vectorized queries in certain commands.
- **Embedded Scripting:** `Luau` (a fast Lua dialect) and `Python` (optional).
- **Template Engine:** `MiniJinja`.

### Architecture
- **Modular Commands:** Each command is implemented as a self-contained module in `src/cmd/`.
- **Streaming by Default:** Most commands process data in a streaming fashion with constant memory usage, enabling processing of arbitrarily large files.
- **Feature Gated:** Functionality is modularized using Rust feature flags (e.g., `polars`, `luau`, `python`, `geocode`).
- **Performance Focused:** Employs multithreading (via `rayon`), custom memory allocators (`mimalloc`), and extensive caching strategies.

## Building and Running

### Build Variants
`qsv` supports several binary variants tailored for different needs:
- `qsv`: Feature-capable variant (all features enabled).
- `qsvlite`: Slimmed-down version (similar to original `xsv`).
- `qsvmcp`: Optimized for MCP server use (geocode, luau, mcp, polars, self_update).
- `qsvdp`: Optimized for `DataPusher+`.
- `qsvpy`: Variant with Python support enabled.

### Key Commands
- **Build (Release):** `cargo build --release --locked --bin qsv --features all_features`
- **Test:** `cargo test --features all_features`
- **Lint:** `cargo +nightly clippy -F all_features -- -W clippy::perf`
- **Format:** `cargo +nightly fmt`

## Development Conventions

- **Rust Version:** Requires latest stable Rust supported by Homebrew. Nightly is required for formatting and clippy.
- **Coding Style:**
  - Strict adherence to `rustfmt` (nightly).
  - Use `clippy` for performance and correctness checks.
  - `unwrap()` and `expect()` are allowed but should have a safety comment.
- **CLI Design:** Uses `docopt` for usage-driven argument parsing. Usage text is embedded at the top of each command's source file.
- **Error Handling:** Standardized via `CliError` and `CliResult` in `src/clitypes.rs`. Uses macros like `fail!`, `fail_clierror!`, etc.
- **Testing:** Extensive test suite (~2,448 tests) in the `tests/` directory. Each command should have its own `test_<command>.rs` file.
- **Logging:** Uses `flexi_logger`. Level can be controlled via `QSV_LOG_LEVEL`.

## Configuration

`qsv` is highly configurable via environment variables (prefix `QSV_`) and `.env` files.
Key variables include:
- `QSV_DEFAULT_DELIMITER`: Set default delimiter.
- `QSV_MAX_JOBS`: Control multithreading.
- `QSV_AUTOINDEX_SIZE`: Automatically create indices for large files.
- `QSV_MEMORY_CHECK`: Enable Out-of-Memory prevention.

For a full list of environment variables, refer to `docs/ENVIRONMENT_VARIABLES.md`.

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
