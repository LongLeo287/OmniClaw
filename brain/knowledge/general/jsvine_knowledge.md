---
id: jsvine-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:56.673145
---

# KNOWLEDGE EXTRACT: jsvine
> **Extracted on:** 2026-03-30 17:38:13
> **Source:** jsvine

---

## File: `pdfplumber.md`
```markdown
# 📦 jsvine/pdfplumber [🔖 PENDING/APPROVE]
🔗 https://github.com/jsvine/pdfplumber


## Meta
- **Stars:** ⭐ 9991 | **Forks:** 🍴 875
- **Language:** Python | **License:** MIT
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Plumb a PDF for detailed information about each char, rectangle, line, et cetera — and easily extract text and tables.

## README (trích đầu)
```
# pdfplumber

[![Version](https://img.shields.io/pypi/v/pdfplumber.svg)](https://pypi.python.org/pypi/pdfplumber) ![Tests](https://github.com/jsvine/pdfplumber/workflows/Tests/badge.svg) [![Code coverage](https://codecov.io/gh/jsvine/pdfplumber/branch/stable/graph/badge.svg)](https://codecov.io/gh/jsvine/pdfplumber/branch/stable) [![Support Python versions](https://img.shields.io/pypi/pyversions/pdfplumber.svg)](https://pypi.python.org/pypi/pdfplumber)

Plumb a PDF for detailed information about each text character, rectangle, and line. Plus: Table extraction and visual debugging.

Works best on machine-generated, rather than scanned, PDFs. Built on [`pdfminer.six`](https://github.com/goulu/pdfminer). 

Currently [tested](tests/) on [Python 3.10, 3.11, 3.12, 3.13, 3.14](.github/workflows/tests.yml).

Translations of this document are available in: [Chinese (by @hbh112233abc)](https://github.com/hbh112233abc/pdfplumber/blob/stable/README-CN.md).

__To report a bug__ or request a feature, please [file an issue](https://github.com/jsvine/pdfplumber/issues/new/choose). __To ask a question__ or request assistance with a specific PDF, please [use the discussions forum](https://github.com/jsvine/pdfplumber/discussions).

## Table of Contents

- [Installation](#installation)
- [Command line interface](#command-line-interface)
- [Python library](#python-library)
- [Visual debugging](#visual-debugging)
- [Extracting text](#extracting-text)
- [Extracting tables](#extracting-tables)
- [Extracting form values](#extracting-form-values)
- [Demonstrations](#demonstrations)
- [Comparison to other libraries](#comparison-to-other-libraries)
- [Acknowledgments / Contributors](#acknowledgments--contributors)
- [Contributing](#contributing)

## Installation

```sh
pip install pdfplumber
```

## Command line interface

### Basic example

```sh
curl "https://raw.githubusercontent.com/jsvine/pdfplumber/stable/examples/pdfs/background-checks.pdf" > background-checks.pdf
pdfplumber background-checks.pdf > background-checks.csv
```

The output will be a CSV containing info about every character, line, and rectangle in the PDF.

### Options

| Argument | Description |
|----------|-------------|
|`--format [format]`| `csv`, `json`, or `text`. The `csv` and `json` formats return information about each object. Of those two, the `json` format returns more information; it includes PDF-level and page-level metadata, plus dictionary-nested attributes. The `text` option returns a plain-text representation of the PDF, using `Page.extract_text(layout=True)`.|
|`--pages [list of pages]`| A space-delimited, `1`-indexed list of pages or hyphenated page ranges. E.g., `1, 11-15`, which would return data for pages 1, 11, 12, 13, 14, and 15.|
|`--types [list of object types to extract]`| Choices are `char`, `rect`, `line`, `curve`, `image`, `annot`, et cetera. Defaults to all available.|
|`--laparams`| A JSON-formatted string (e.g., `'{"detect_vertical": true}'`) to pass to `pdfplumber.open(
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

