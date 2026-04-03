---
id: olekukonko-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:29:14.637622
---

# KNOWLEDGE EXTRACT: olekukonko
> **Extracted on:** 2026-03-30 17:49:54
> **Source:** olekukonko

---

## File: `tablewriter.md`
```markdown
# 📦 olekukonko/tablewriter [🔖 PENDING/APPROVE]
🔗 https://github.com/olekukonko/tablewriter


## Meta
- **Stars:** ⭐ 4776 | **Forks:** 🍴 391
- **Language:** Go | **License:** MIT
- **Last updated:** 2026-03-23
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
ASCII table in golang

## README (trích đầu)
```
# TableWriter for Go

[![Go](https://github.com/olekukonko/tablewriter/actions/workflows/go.yml/badge.svg)](https://github.com/olekukonko/tablewriter/actions/workflows/go.yml)
[![Go Reference](https://pkg.go.dev/badge/github.com/olekukonko/tablewriter.svg)](https://pkg.go.dev/github.com/olekukonko/tablewriter)
[![Go Report Card](https://goreportcard.com/badge/github.com/olekukonko/tablewriter)](https://goreportcard.com/report/github.com/olekukonko/tablewriter)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Benchmarks](https://img.shields.io/badge/benchmarks-included-success)](README.md#benchmarks)

`tablewriter` is a Go library for generating **rich text-based tables** with support for multiple output formats, including ASCII, Unicode, Markdown, HTML, and colorized terminals. Perfect for CLI tools, logs, and web applications.

### Key Features
- **Multi-format rendering**: ASCII, Unicode, Markdown, HTML, ANSI-colored
- **Advanced styling**: Cell merging, alignment, padding, borders
- **Flexible input**: CSV, structs, slices, or streaming data
- **High performance**: Minimal allocations, buffer reuse
- **Modern features**: Generics support, hierarchical merging, real-time streaming

---

### Installation

#### Legacy Version (v0.0.5)
For use with legacy applications:
```bash
go get github.com/olekukonko/tablewriter@v0.0.5
```

#### Latest  Version
The latest stable version
```bash
go get github.com/olekukonko/tablewriter@v1.1.4
```

**Warning:** Version `v1.0.0` contains missing functionality and should not be used.


> **Version Guidance**
> - Legacy: Use `v0.0.5` (stable)
> - New Features: Use `@latest` (includes generics, super fast streaming APIs)
> - Legacy Docs: See [README_LEGACY.md](README_LEGACY.md)

---

### Why TableWriter?
- **CLI Ready**: Instant compatibility with terminal outputs
- **Database Friendly**: Native support for `sql.Null*` types
- **Secure**: Auto-escaping for HTML/Markdown
- **Extensible**: Custom renderers and formatters

---

### Quick Example
```go
package main

import (
	"github.com/olekukonko/tablewriter"
	"os"
)

func main() {
	data := [][]string{
		{"Package", "Version", "Status"},
		{"tablewriter", "v0.0.5", "legacy"},
		{"tablewriter", "v1.1.4", "latest"},
	}

	table := tablewriter.NewWriter(os.Stdout)
	table.Header(data[0])
	table.Bulk(data[1:])
	table.Render()
}
```
**Output**:
```
┌─────────────┬─────────┬────────┐
│   PACKAGE   │ VERSION │ STATUS │
├─────────────┼─────────┼────────┤
│ tablewriter │ v0.0.5  │ legacy │
│ tablewriter │ v1.1.4  │ latest │
└─────────────┴─────────┴────────┘
```


## Detailed Usage

Create a table with `NewTable` or `NewWriter`, configure it using options or a `Config` struct, add data with `Append` or `Bulk`, and render to an `io.Writer`. Use renderers like `Blueprint` (ASCII), `HTML`, `Markdown`, `Colorized`, or `Ocean` (streaming).

Here's how the API primitives map to the generated ASCII table:

```
API Call                                  ASCII 
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

