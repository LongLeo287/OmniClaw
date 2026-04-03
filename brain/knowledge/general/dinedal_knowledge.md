---
id: dinedal-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:20.299179
---

# KNOWLEDGE EXTRACT: dinedal
> **Extracted on:** 2026-03-30 17:35:58
> **Source:** dinedal

---

## File: `textql.md`
```markdown
# 📦 dinedal/textql [🔖 PENDING/APPROVE]
🔗 https://github.com/dinedal/textql


## Meta
- **Stars:** ⭐ 9118 | **Forks:** 🍴 298
- **Language:** Go | **License:** MIT
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Execute SQL against structured text like CSV or TSV

## README (trích đầu)
```
# TextQL

[![Build Status](https://travis-ci.org/dinedal/textql.svg)](https://travis-ci.org/dinedal/textql) [![Go Report Card](http://goreportcard.com/badge/dinedal/textql)](http://goreportcard.com/report/dinedal/textql)

Allows you to easily execute SQL against structured text like CSV or TSV.

Example session:

![textql_usage_session](https://raw.github.com/dinedal/textql/master/textql_usage.gif)

## Major changes!

In the time since the initial release of textql, I've made some improvements as well as made the project much more modular. There've also been additional performance tweaks and added functionality, but this comes at the cost of breaking the original command-line flags and changing the install command.

### Changes since v1

Additions:

- Numeric values are automatically recognized in more cases.
- Date / Time / DateTime values are automatically recognized in reasonable formats. See [Time Strings](https://www.sqlite.org/lang_datefunc.html) for a list for accepted formats, and how to convert from other formats.
- Added join support! Multiple files / directories can be loaded by listing them at the end of the command.
- Directories are read by reading each file inside, and this is non-recursive.
- You can list as many files / directories as you like.
- Added flag '-output-file' to save output directly to a file.
- Added flag '-output-dlm' to modify the output delimiter.
- Added "short SQL" syntax.
  - For the case of a single table, the `FROM [table]` can be dropped from the query.
  - For simple selects, the `SELECT` keyword can be dropped from the query.
  - This means the v1 command `textql -sql "select * from tbl" -source some_file.csv` can be shortened to `textql -sql "*" some_file.csv`

Changes:

- The flag '-outputHeader' was renamed to '-output-header'.

Removals:

- Dropped the ability to override table names. This makes less sense after the automatic tablename generation based on filename, joins, and shorter SQL syntax changes.
- Removed '-source', any files / paths at the end of the command are used, as well as piped-in data.

Bug fixes:

- Writing to a directory no longer fails silently.

## Key differences between textql and sqlite importing

- sqlite import will not accept stdin, breaking unix pipes. textql will happily do so.
- textql supports quote-escaped delimiters, sqlite does not.
- textql leverages the sqlite in-memory database feature as much as possible and only touches disk if asked.

## Is it any good?

[Yes](https://news.ycombinator.com/item?id=3067434)

## Requirements

- Go 1.4 or later

## Install

**Latest release on Homebrew (OS X)**

```bash
brew install textql
```

**Build from source**

```bash
go get -u github.com/dinedal/textql/...
```

## Docker

First build the image.

```bash
docker build -t textql .
```

Now use that image mounting your current directory into the container.

```bash
docker run --rm -it -v $(pwd):/tmp textql [rest_of_command]
```

### Alias

You can add the following alias to your
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

