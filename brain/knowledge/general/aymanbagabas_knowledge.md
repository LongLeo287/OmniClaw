---
id: aymanbagabas-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:18:56.070989
---

# KNOWLEDGE EXTRACT: aymanbagabas
> **Extracted on:** 2026-03-30 17:30:48
> **Source:** aymanbagabas

---

## File: `go-udiff.md`
```markdown
# 📦 aymanbagabas/go-udiff [🔖 PENDING/APPROVE]
🔗 https://github.com/aymanbagabas/go-udiff


## Meta
- **Stars:** ⭐ 222 | **Forks:** 🍴 7
- **Language:** Go | **License:** BSD-3-Clause
- **Last updated:** 2026-03-08
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
µDiff - a micro Go diffing library

## README (trích đầu)
```
# µDiff

<p>
<a href="https://github.com/aymanbagabas/go-udiff/releases"><img src="https://img.shields.io/github/release/aymanbagabas/go-udiff.svg" alt="Latest Release"></a>
<a href="https://pkg.go.dev/github.com/aymanbagabas/go-udiff?tab=doc"><img src="https://godoc.org/github.com/golang/gddo?status.svg" alt="Go Docs"></a>
<a href="https://github.com/aymanbagabas/go-udiff/actions"><img src="https://github.com/aymanbagabas/go-udiff/workflows/build/badge.svg" alt="Build Status"></a>
<a href="https://goreportcard.com/report/github.com/aymanbagabas/go-udiff"><img alt="Go Report Card" src="https://goreportcard.com/badge/github.com/aymanbagabas/go-udiff"></a>
</p>

Micro diff (µDiff) is a Go library that implements the
[Myers'](http://www.xmailserver.org/diff2.pdf) diffing algorithm. It aims to
provide a minimal API to compute and apply diffs with zero dependencies. It
also supports generating diffs in the [Unified Format](https://www.gnu.org/software/diffutils/manual/html_node/Unified-Format.html).
If you are looking for a way to parse unified diffs, check out
[sourcegraph/go-diff](https://github.com/sourcegraph/go-diff).

This is merely a copy of the [Golang tools internal diff package](https://github.com/golang/tools/tree/master/internal/diff)
with a few modifications to export package symbols. All credit goes to the [Go authors](https://go.dev/AUTHORS).

## Usage

You can import the package using the following command:

```bash
go get github.com/aymanbagabas/go-udiff
```

## Examples

Generate a unified diff for strings `a` and `b` with the default number of
context lines (3). Use `udiff.ToUnified` to specify the number of context
lines.

```go
package main

import (
    "fmt"

    "github.com/aymanbagabas/go-udiff"
)

func main() {
    a := "Hello, world!\n"
    b := "Hello, Go!\nSay hi to µDiff"
    unified := udiff.Unified("a.txt", "b.txt", a, b)
    fmt.Println(unified)
}
```

```
--- a.txt
+++ b.txt
@@ -1 +1,2 @@
-Hello, world!
+Hello, Go!
+Say hi to µDiff
\ No newline at end of file
```

Apply changes to a string.

```go
package main

import (
    "fmt"

    "github.com/aymanbagabas/go-udiff"
)

func main() {
    a := "Hello, world!\n"
    b := "Hello, Go!\nSay hi to µDiff"

    edits := udiff.Strings(a, b)
    final, err := udiff.Apply(a, edits)
    if err != nil {
        panic(err)
    }

    fmt.Println(final)
}
```

```
Hello, Go!
Say hi to µDiff
```

To get a line-by-line diff and edits:

```go
package main

import (
    "fmt"

    "github.com/aymanbagabas/go-udiff"
)

func main() {
    a := "Hello, world!\n"
    b := "Hello, Go!\nSay hi to µDiff"

    edits := udiff.Strings(a, b)
    d, err := udiff.ToUnifiedDiff("a.txt", "b.txt", a, edits, udiff.DefaultContextLines)
    if err != nil {
        panic(err)
    }

    for _, h := range d.Hunks {
        fmt.Printf("hunk: -%d, +%d\n", h.FromLine, h.ToLine)
        for _, l := range h.Lines {
            fmt.Printf("%s %q\n", l.Kind, l.Content)
        }
    }
}
```

```
hunk: -1, +1
dele
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

