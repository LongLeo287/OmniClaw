---
id: medialab-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:29:07.344168
---

# KNOWLEDGE EXTRACT: medialab
> **Extracted on:** 2026-03-30 17:42:29
> **Source:** medialab

---

## File: `xan.md`
```markdown
# 📦 medialab/xan [🔖 PENDING/APPROVE]
🔗 https://github.com/medialab/xan


## Meta
- **Stars:** ⭐ 3864 | **Forks:** 🍴 77
- **Language:** Rust | **License:** Unlicense
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
The CSV magician

## README (trích đầu)
```
[![Build Status](https://github.com/medialab/xan/workflows/Tests/badge.svg)](https://github.com/medialab/xan/actions) [![DOI](https://zenodo.org/badge/140488417.svg)](https://doi.org/10.5281/zenodo.15310200)

# `xan`, the CSV magician

`xan` is a command line tool that can be used to process CSV files directly from the shell.

It has been written in Rust to be as fast as possible, use as little memory as possible, and can very easily handle large CSV files (Gigabytes). It leverages a novel [SIMD](https://en.wikipedia.org/wiki/Single_instruction,_multiple_data) CSV [parser](https://docs.rs/simd-csv) and is also able to parallelize some computations (through multithreading) to make some tasks complete as fast as your computer can allow.

It can easily preview, filter, slice, aggregate, sort, join CSV files, and exposes a large collection of composable commands that can be chained together to perform a wide variety of typical tasks.

`xan` also offers its own expression language so you can perform complex tasks that cannot be done by relying on the simplest commands. This minimalistic language has been tailored for CSV data and is *way* faster than evaluating typical dynamically-typed languages such as Python, Lua, JavaScript etc.

Note that this tool is originally a fork of [BurntSushi](https://github.com/BurntSushi)'s [`xsv`](https://github.com/BurntSushi/xsv), but has been nearly entirely rewritten at that point, to fit [SciencesPo's médialab](https://github.com/medialab) use-cases, rooted in web data collection and analysis geared towards social sciences (you might think CSV is outdated by now, but read our [love letter](./docs/LOVE_LETTER.md) to the format before judging too quickly).

`xan` therefore goes beyond typical data manipulation and expose utilities related to lexicometry, graph theory and even scraping.

Beyond CSV data, `xan` is able to process a large variety of CSV-adjacent data formats from many different disciplines such as web archival (`.cdx`) or bioinformatics (`.vcf`, `.gtf`, `.sam`, `.bed` etc.). `xan` is also able to convert to & from many data formats such as json, excel files, numpy arrays etc. using [`xan to`](./docs/cmd/to.md) and [`xan from`](./docs/cmd/from.md). See [this](#supported-file-formats) section for more detail.

Finally, `xan` can be used to display CSV files in the terminal, for easy exploration, and can even be used to draw basic data visualisations:

|*view command*|*flatten command*|
|:---:|:---:|
|![view](./docs/img/grid/view.png)|![flatten](./docs/img/grid/flatten.png)|
|__*categorical histogram*__|__*scatterplot*__|
|![categ-hist](./docs/img/grid/categ-hist.png)|![correlation](./docs/img/grid/correlation.png)|
|__*categorical scatterplot*__|__*histograms*__|
|![scatter](./docs/img/grid/scatter.png)|![hist](./docs/img/grid/hist.png)|
|__*parallel processing*__|__*time series*__|
|![parallel](./docs/img/grid/parallel.png)|![series](./docs/img/grid/series.png)|
|__*small multiples (facet grid)*__|__*gr
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

