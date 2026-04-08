---
id: repo-fetched-chartli-112745
type: knowledge
owner: OA
registered_at: 2026-04-05T04:08:15.408622
tags: ["auto-cloned", "oa-assimilated"]
---

# FETCHED_chartli_112745

## Assimilation Report
Auto-cloned repository: FETCHED_chartli_112745

## Application for OmniClaw
No structural integration blueprint provided.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
![npx chartli](https://raw.githubusercontent.com/ahmadawais/chartli/main/.github/chartli.jpg)

# chartli

CLI for rendering charts in terminals from numeric text data. `chartli` turns plain numbers into terminal charts. ascii, spark, bars, columns, heatmap, unicode, braille, svg.


## Install

Run instantly:

```sh
npx chartli --help
```

Or install globally:

```sh
npm i -g chartli
```

## Agent skill install

Install the repository skill for agents:

```sh
npx skills add ahmadawais/chartli
```

Quick start:

```sh
npx chartli
npx chartli --help
```

## Usage

```sh
npx chartli [file] [options]
```

```text
Usage: chartli [options] [file]

Render terminal charts from numeric data

Arguments:
  file                   Input file (reads from stdin if not provided)

Options:
  -v, --version          Output the version number
  -t, --type <type>      Chart type: svg, ascii, unicode, braille, spark, bars,
                         columns, heatmap (default: "ascii")
  -w, --width <number>   Chart width
  -h, --height <number>  Chart height
  -m, --mode <mode>      SVG mode: circles or lines (default: "circles")
  --x-axis-label <label> Title to render for the x-axis
  --y-axis-label <label> Title to render for the y-axis
  --x-labels <labels>    Comma-separated labels for x-axis ticks or row labels
  --series-labels <labels>
                         Comma-separated labels for plotted series or categories
  --data-labels          Show raw values near plotted data when supported
  --first-column-x       Treat the first numeric column as x labels instead of a
                         plotted series
  --help                 Display help for command
```

## Labels and metadata

- Use `--x-axis-label` and `--y-axis-label` to add axis titles.
- Use `--x-labels` for explicit tick labels.
- Use `--series-labels` to replace generic labels like `S1` and `C1`.
- Use `--data-labels` to print raw values on or near the plotted data where the renderer supports it.
- Use `--first-column-x` when the first numeric column is a domain like `day`, `month`, or `year`.

With `--first-column-x`, chartli will:

- use the first numeric column as x-axis labels
- use the first header cell as the x-axis title when a header row exists
- use the remaining header cells as series labels
- use the second header cell as the y-axis title for common two-column data

Example:

```sh
pnpm chartli examples/assets/core-single-series.txt -t ascii -w 24 -h 8 --first-column-x --data-labels
```

```sh
pnpm chartli examples/assets/core-multi-series.txt -t columns -h 8 --first-column-x --series-labels sales,costs,profit --x-axis-label Metrics --y-axis-label Value --data-labels
```

## Labeled chart examples

### ASCII line with inferred axis labels and data labels

```sh
pnpm chartli examples/assets/weekly-signups.txt -t ascii -w 28 -h 8 --first-column-x --data-labels
```

```text
        signups
    91 │                      ●   87
       │                     91    ●
       │            73
       │             ●   68
  66.5 │   58             ●
       │    ●   49
       │42       ●
    42 │●
       └────────────────────────────
        1   2    3   4    5   6    7
                    day
```

### Columns with explicit axis titles and inferred series names

```sh
pnpm chartli examples/assets/weekly-metrics.txt -t columns -h 8 --first-column-x --x-axis-label Metrics --y-axis-label Count --data-labels
```

```text
Count
 176     29     10


  █
  █
  █
  █
  █      ▓      ▒
  █      ▓      ▒
────────────────────
visits trials  paid
      Metrics
```

### SVG with axes, x labels, and point labels

```sh
pnpm chartli examples/assets/weekly-signups.txt -t svg -m lines -w 320 -h 120 --first-column-x --data-labels | sed -n '/^<?xml/,$p' > examples/assets/output/weekly-signups-chart.svg
```

This writes `examples/assets/output/weekly-signups-chart.svg`.

## Types

- `ascii`
- `spark`
- `bars`
- `columns`
- `heatmap`
- `unicode`
- `braille`
- `svg`

## Example data files

- `examples/assets/core-single-series.txt`
- `examples/assets/core-multi-series.txt`
- `examples/assets/image-data.txt`
- `examples/assets/image-single-series.txt`
- `examples/assets/image-columns-variant.txt`
- `examples/assets/weekly-signups.txt`
- `examples/assets/weekly-metrics.txt`

## Image chart set (text diagrams)

### ASCII Line

```sh
pnpm chartli examples/assets/image-data.txt -t ascii -w 24 -h 8
```

```text
      day=●  sales=○  costs=◆  profit=◇
1.00 │                       ○
     │
     │             ◇         ◇
     │                  ◆    ●
0.50 │                  ●    ◆
     │    ◇    ◆   ●
     │         ○   ◆
0.00 │◇   ◆    ◇        ◇
     └────────────────────────
```

### Sparklines

```sh
pnpm chartli examples/assets/image-data.txt -t spark
```

```text
day    ▁▂▃▄▅▆
sales  ▁▄▂▇▅█
costs  ▁▂▄▃▆▅
profit ▁▄▂▇▂▇
```

### Horizontal Bars

```sh
pnpm chartli examples/assets/image-data.txt -t bars -w 28
```

```text
day    |███████████████████         | 0.67
sales  |▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓| 1.00
costs  |▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒             | 0.53
profit |░░░░░░░░░░░░░░░░░░░░░░░     | 0.83
```

### Columns

```sh
pnpm chartli examples/assets/image-data.txt -t columns -h 8
```

```text
         ▓
         ▓             ░
         ▓             ░
  █      ▓             ░
  █      ▓      ▒      ░
  █      ▓      ▒      ░
  █      ▓      ▒      ░
  █      ▓      ▒      ░
───────────────────────────
 day   sales  costs  profit
```

### Columns (Variant)

```sh
pnpm chartli examples/assets/image-columns-variant.txt -t columns -h 8
```

```text

         ▓             ░
  █      ▓             ░
  █      ▓             ░
  █      ▓      ▒      ░
  █      ▓      ▒      ░
  █      ▓      ▒      ░
───────────────────────────
 day   sales  costs  profit
```

### Heatmap

```sh
pnpm chartli examples/assets/image-data.txt -t heatmap
```

```text
    day sales costs profit
R01
R02 ░ ▒ ░ ▒
R03 ░ ░ ▒ ░
R04 ▒ ▓ ░ ▓
R05 ▒ ▒ ▓ ░
R06 ▓ █ ▒ ▓
```

### Unicode Bars

```sh
pnpm chartli examples/assets/image-data.txt -t unicode
```

```text
 day    sales   costs   profit
             █
           ▃ █             ▅ ▅
     ▃     █ █      ▃      █ █
    ▂█     █▆█      █▂     █ █
   ▂██   ▂ ███    ▂ ██   ▃ █ █
  ▁███   █ ███    █▁██   █ █ █
 ▁████   █▅███   ▁████   █▁█▁█
 █████   █████   █████   █████
```

### Braille

```sh
pnpm chartli examples/assets/image-data.txt -t braille -w 16 -h 6
```

```text
profit

⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠈
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⡀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠁⠀⠀⠀
```

### SVG Chart

```sh
pnpm chartli examples/assets/image-data.txt -t svg -m lines -w 320 -h 120 | sed -n '/^<?xml/,$p' > examples/assets/output/image-chart.svg
```

```text
<?xml version='1.0'?>
<svg xmlns='http://www.w3.org/2000/svg' width='650' height='120' version='1.1'>
  <polyline ... />
  <polyline ... />
  <polyline ... />
  <polyline ... />
</svg>
```

![svg](examples/assets/output/image-chart.svg)

# Examples

All examples are data-file driven from `examples/assets/`.

## Data files

- `examples/assets/core-single-series.txt`
- `examples/assets/core-multi-series.txt`
- `examples/assets/image-data.txt`
- `examples/assets/image-single-series.txt`
- `examples/assets/image-columns-variant.txt`
- `examples/assets/weekly-signups.txt`
- `examples/assets/weekly-metrics.txt`
- `examples/assets/output/`

## Core commands

- `pnpm chartli examples/assets/core-single-series.txt -t ascii -w 24 -h 8`
- `pnpm chartli examples/assets/core-multi-series.txt -t spark`
- `pnpm chartli examples/assets/core-multi-series.txt -t bars -w 28`
- `pnpm chartli examples/assets/core-multi-series.txt -t columns -h 8`
- `pnpm chartli examples/assets/core-multi-series.txt -t heatmap`
- `pnpm chartli examples/assets/core-multi-series.txt -t unicode`
- `pnpm chartli examples/assets/core-single-series.txt -t braille -w 16 -h 6`
- `pnpm chartli examples/assets/core-multi-series.txt -t svg -m lines -w 320 -h 120 | sed -n '/^<?xml/,$p' > examples/assets/output/core-chart.svg`

## Image commands

- `pnpm chartli examples/assets/image-data.txt -t ascii -w 24 -h 8`
- `pnpm chartli examples/assets/image-data.txt -t spark`
- `pnpm chartli examples/assets/image-data.txt -t bars -w 28`
- `pnpm chartli examples/assets/image-data.txt -t columns -h 8`
- `pnpm chartli examples/assets/image-columns-variant.txt -t columns -h 8`
- `pnpm chartli examples/assets/image-data.txt -t heatmap`
- `pnpm chartli examples/assets/image-data.txt -t unicode`
- `pnpm chartli examples/assets/image-data.txt -t braille -w 16 -h 6`
- `pnpm chartli examples/assets/image-data.txt -t svg -m lines -w 320 -h 120 | sed -n '/^<?xml/,$p' > examples/assets/output/image-chart.svg`

## Labeled commands

- `pnpm chartli examples/assets/weekly-signups.txt -t ascii -w 28 -h 8 --first-column-x --data-labels`
- `pnpm chartli examples/assets/weekly-metrics.txt -t columns -h 8 --first-column-x --x-axis-label Metrics --y-axis-label Count --data-labels`
- `pnpm chartli examples/assets/weekly-signups.txt -t svg -m lines -w 320 -h 120 --first-column-x --data-labels | sed -n '/^<?xml/,$p' > examples/assets/output/weekly-signups-chart.svg`

## Run grouped examples

- `pnpm run example:kitchen-sink`
- `pnpm run example:image-set:kitchen-sink`
- `pnpm run example:labeled:kitchen-sink`
- `pnpm run example:all-kitchen-sink`

## Run all examples

Image-set chart run:

```sh
pnpm run example:image-set:kitchen-sink
```

Core + image run:

```sh
pnpm run example:all-kitchen-sink
```

## License

Apache-2.0 by [Ahmad Awais](https://x.com/MrAhmadAwais) built with [Command Code](https://commandcode.ai).

```

### File: examples\README.md
```md
# Examples

All examples are data-file driven from `examples/assets/`.

## Data files

- `examples/assets/core-single-series.txt`
- `examples/assets/core-multi-series.txt`
- `examples/assets/image-data.txt`
- `examples/assets/image-single-series.txt`
- `examples/assets/image-columns-variant.txt`
- `examples/assets/weekly-signups.txt`
- `examples/assets/weekly-metrics.txt`
- `examples/assets/output/`

## Core commands

- `pnpm chartli examples/assets/core-single-series.txt -t ascii -w 24 -h 8`
- `pnpm chartli examples/assets/core-multi-series.txt -t spark`
- `pnpm chartli examples/assets/core-multi-series.txt -t bars -w 28`
- `pnpm chartli examples/assets/core-multi-series.txt -t columns -h 8`
- `pnpm chartli examples/assets/core-multi-series.txt -t heatmap`
- `pnpm chartli examples/assets/core-multi-series.txt -t unicode`
- `pnpm chartli examples/assets/core-single-series.txt -t braille -w 16 -h 6`
- `pnpm chartli examples/assets/core-multi-series.txt -t svg -m lines -w 320 -h 120 | sed -n '/^<?xml/,$p' > examples/assets/output/core-chart.svg`

## Image commands

- `pnpm chartli examples/assets/image-data.txt -t ascii -w 24 -h 8`
- `pnpm chartli examples/assets/image-data.txt -t spark`
- `pnpm chartli examples/assets/image-data.txt -t bars -w 28`
- `pnpm chartli examples/assets/image-data.txt -t columns -h 8`
- `pnpm chartli examples/assets/image-columns-variant.txt -t columns -h 8`
- `pnpm chartli examples/assets/image-data.txt -t heatmap`
- `pnpm chartli examples/assets/image-data.txt -t unicode`
- `pnpm chartli examples/assets/image-data.txt -t braille -w 16 -h 6`
- `pnpm chartli examples/assets/image-data.txt -t svg -m lines -w 320 -h 120 | sed -n '/^<?xml/,$p' > examples/assets/output/image-chart.svg`

## Labeled commands

- `pnpm chartli examples/assets/weekly-signups.txt -t ascii -w 28 -h 8 --first-column-x --data-labels`
- `pnpm chartli examples/assets/weekly-metrics.txt -t columns -h 8 --first-column-x --x-axis-label Metrics --y-axis-label Count --data-labels`
- `pnpm chartli examples/assets/weekly-signups.txt -t svg -m lines -w 320 -h 120 --first-column-x --data-labels | sed -n '/^<?xml/,$p' > examples/assets/output/weekly-signups-chart.svg`

## Run grouped examples

- `pnpm run example:kitchen-sink`
- `pnpm run example:image-set:kitchen-sink`
- `pnpm run example:labeled:kitchen-sink`
- `pnpm run example:all-kitchen-sink`

```

### File: CHANGELOG.md
```md
# Changelog

## [1.0.0](https://github.com/ahmadawais/chartli/compare/0.0.5...1.0.0) (2026-03-10)

### Features

* add chart labels and labeled examples ([de2f44e](https://github.com/ahmadawais/chartli/commit/de2f44e14b94fe1051c2b51b2e1e40ea024e4660))

## 0.0.5 (2026-03-06)

### Features

* build chartli TypeScript CLI for terminal charts ([14db8b1](https://github.com/ahmadawais/chartli/commit/14db8b12fa568832d2b250ffbedd6f3f3cbac7db))
* **chartli:** root-first CLI DX, richer chart suite, and docs refresh ([73b0009](https://github.com/ahmadawais/chartli/commit/73b000994d7ed254caad51b0357b551fbde5eb83))
* image ([f344658](https://github.com/ahmadawais/chartli/commit/f344658bbd5fb6d965469b48cc18620d271afc97))
* implement chartli CLI for data visualization in SVG, ASCII, Unicode, and Braille ([9268e1f](https://github.com/ahmadawais/chartli/commit/9268e1f191daca073e999071df3031dd4b2e423e))
* Init ([741b103](https://github.com/ahmadawais/chartli/commit/741b1037bfdafb6fa35400d5e9b3c3474be6a766))
* rust pkg ([bd81b95](https://github.com/ahmadawais/chartli/commit/bd81b953c23f58b737584a56d6f98c2af1895e80))
* taste ([935d343](https://github.com/ahmadawais/chartli/commit/935d3435228a33ea917e68ee1c14314ef47982a3))
* taste ([cbb3449](https://github.com/ahmadawais/chartli/commit/cbb3449c28450f5d07c2e3d53f693bfe055c5782))

### Bug Fixes

* builds ([bc09158](https://github.com/ahmadawais/chartli/commit/bc0915863738a0ce96408b95d3cc80ae2dc40fe5))
* Sync .gitignore ([12cc10b](https://github.com/ahmadawais/chartli/commit/12cc10b24cad3a960aab50ad1f2acb1d31a13d8e))
* version ([e2af579](https://github.com/ahmadawais/chartli/commit/e2af5796deaa5edf795f034d8764e7b91a8a2b88))

### Documentation

* Enhance README with detailed chartli features ([60f3ab1](https://github.com/ahmadawais/chartli/commit/60f3ab1c8bf8fc0d1ef56b2cbe61e8c58635043e))

### Improvements

* cover ([9b8d33a](https://github.com/ahmadawais/chartli/commit/9b8d33a9c25f9918eca1187d9479303c545f89d4))

### Chores

* **examples:** flatten example layout, fix npx UX, and refresh docs ([d4eb868](https://github.com/ahmadawais/chartli/commit/d4eb8681380f16abe469b504815d9a15558aa557))
* **examples:** remove bash scripts, add data-driven chart docs, and ship agent skill ([596afb5](https://github.com/ahmadawais/chartli/commit/596afb5e950b9f0db6a0ae48adc1e2dbd7994d56))

## [0.0.4](https://github.com/ahmadawais/chartli/compare/v0.0.3...v0.0.4) (2026-03-05)

### Chores

* **examples:** flatten example layout, fix npx UX, and refresh docs ([cdc8c1c](https://github.com/ahmadawais/chartli/commit/cdc8c1cdcfa8f86aa4f95d4cf29431d976a165fd))
* **examples:** remove bash scripts, add data-driven chart docs, and ship agent skill ([2c2ded9](https://github.com/ahmadawais/chartli/commit/2c2ded9509606effe10df0215b29fe693379ddeb))

## [0.0.3](https://github.com/ahmadawais/chartli/compare/v0.0.2...v0.0.3) (2026-03-05)

### Features

* Init ([8cb0499](https://github.com/ahmadawais/chartli/commit/8cb04996e3a6c2bfca155e19844652192ce24b2d))

### Bug Fixes

* version ([c1f2383](https://github.com/ahmadawais/chartli/commit/c1f238387b283037fb042b1ca050235105572797))

### Improvements

* cover ([fb75190](https://github.com/ahmadawais/chartli/commit/fb751905fd74ad3f289bdc85ed8f6c0474501c89))

```

### File: VETTING_REPORT.md
```md
---
title: Auto Vetting Report for chartli
date: 2026-04-05
analyst: civ_vetting_pipeline
status: AUTO_VETTED
---

# Auto-Vetted Repository
This repository was automatically swept and vetted by the batch processor. Only documentation remains.

```

### File: .commandcode\taste\taste.md
```md
# Taste (Continuously Learned by [CommandCode][cmd])

[cmd]: https://commandcode.ai/

# Communication
- Use text diagrams to explain architecture and how things work. Confidence: 0.80
- Explain concepts before or alongside implementation, especially for unfamiliar patterns. Confidence: 0.55

# CLI Design
- Use pnpm or npx for running CLI tools, not bash scripts. Confidence: 0.80
- README examples should use npx or pnpm commands, not bash. Confidence: 0.80
- Keep CLI subcommand structure minimal; don't add redundant subcommands when the CLI's purpose is already specific. Confidence: 0.65

# Project Structure
- Keep examples flat in a single examples/ directory, not nested in subdirectories. Confidence: 0.80
- Use an assets/ subdirectory for data files, but example scripts stay flat. Confidence: 0.70
- Include text diagrams of output directly in README alongside runnable examples. Confidence: 0.80

# Git
- Write commit messages with detailed, specific technical descriptions. Confidence: 0.70

```

