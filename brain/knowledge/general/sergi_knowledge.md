---
id: sergi-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:31:12.239823
---

# KNOWLEDGE EXTRACT: sergi
> **Extracted on:** 2026-03-30 17:53:11
> **Source:** sergi

---

## File: `go-diff.md`
```markdown
# 📦 sergi/go-diff [🔖 PENDING/APPROVE]
🔗 https://github.com/sergi/go-diff


## Meta
- **Stars:** ⭐ 2062 | **Forks:** 🍴 222
- **Language:** Go | **License:** MIT
- **Last updated:** 2026-03-24
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Diff, match and patch text in Go

## README (trích đầu)
```
# go-diff [![GoDoc](https://godoc.org/github.com/sergi/go-diff?status.png)](https://godoc.org/github.com/sergi/go-diff/diffmatchpatch) [![Build Status](https://travis-ci.org/sergi/go-diff.svg?branch=master)](https://travis-ci.org/sergi/go-diff) [![Coverage Status](https://coveralls.io/repos/sergi/go-diff/badge.png?branch=master)](https://coveralls.io/r/sergi/go-diff?branch=master)

go-diff offers algorithms to perform operations required for synchronizing plain text:

- Compare two texts and return their differences.
- Perform fuzzy matching of text.
- Apply patches onto text.

## Installation

```bash
go get -u github.com/sergi/go-diff/...
```

## Usage

The following example compares two texts and writes out the differences to standard output.

```go
package main

import (
	"fmt"

	"github.com/sergi/go-diff/diffmatchpatch"
)

const (
	text1 = "Lorem ipsum dolor."
	text2 = "Lorem dolor sit amet."
)

func main() {
	dmp := diffmatchpatch.New()

	diffs := dmp.DiffMain(text1, text2, false)

	fmt.Println(dmp.DiffPrettyText(diffs))
}
```

## Found a bug or are you missing a feature in go-diff?

Please make sure to have the latest version of go-diff. If the problem still persists go through the [open issues](https://github.com/sergi/go-diff/issues) in the tracker first. If you cannot find your request just open up a [new issue](https://github.com/sergi/go-diff/issues/new).

## How to contribute?

You want to contribute to go-diff? GREAT! If you are here because of a bug you want to fix or a feature you want to add, you can just read on. Otherwise we have a list of [open issues in the tracker](https://github.com/sergi/go-diff/issues). Just choose something you think you can work on and discuss your plans in the issue by commenting on it.

Please make sure that every behavioral change is accompanied by test cases. Additionally, every contribution must pass the `lint` and `test` Makefile targets which can be run using the following commands in the repository root directory.

```bash
make lint
make test
```

After your contribution passes these commands, [create a PR](https://help.github.com/articles/creating-a-pull-request/) and we will review your contribution.

## Origins

go-diff is a Go language port of Neil Fraser's google-diff-match-patch code. His original code is available at [http://code.google.com/p/google-diff-match-patch/](http://code.google.com/p/google-diff-match-patch/).

## Copyright and License

The original Google Diff, Match and Patch Library is licensed under the [Apache License 2.0](http://www.apache.org/licenses/LICENSE-2.0). The full terms of that license are included here in the [APACHE-LICENSE-2.0](/APACHE-LICENSE-2.0) file.

Diff, Match and Patch Library

> Written by Neil Fraser
> Copyright (c) 2006 Google Inc.
> <http://code.google.com/p/google-diff-match-patch/>

This Go version of Diff, Match and Patch Library is licensed under the [MIT License](http://www.opensource.org/licenses/MIT) (a.k.a. the Expat License) which is inclu
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

