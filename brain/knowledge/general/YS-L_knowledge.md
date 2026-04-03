---
id: ys-l-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:32:47.641600
---

# KNOWLEDGE EXTRACT: YS-L
> **Extracted on:** 2026-03-30 18:01:25
> **Source:** YS-L

---

## File: `csvlens.md`
```markdown
# 📦 YS-L/csvlens [🔖 PENDING/APPROVE]
🔗 https://github.com/YS-L/csvlens


## Meta
- **Stars:** ⭐ 3666 | **Forks:** 🍴 67
- **Language:** Rust | **License:** MIT
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Command line csv viewer

## README (trích đầu)
```
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
  like `"my_value1"` or `"v
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

