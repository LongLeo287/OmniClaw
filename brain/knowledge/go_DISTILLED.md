---
id: go
type: knowledge
owner: OA_Triage
---
# go
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
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
delete "Hello, world!\n"
insert "Hello, Go!\n"
insert "Say hi to µDiff"
```

## Alternatives

- [sergi/go-diff](https://github.com/sergi/go-diff) No longer reliable. See [#123](https://github.com/sergi/go-diff/issues/123) and [#141](https://github.com/sergi/go-diff/pull/141).
- [hexops/gotextdiff](https://github.com/hexops/gotextdiff) Takes the same approach but looks like the project is abandoned.
- [sourcegraph/go-diff](https://github.com/sourcegraph/go-diff) It doesn't compute diffs. Great package for parsing and printing unified diffs.

## Contributing

Please send any contributions [upstream](https://github.com/golang/tools). Pull
requests made against [the upstream diff package](https://github.com/golang/tools/tree/master/internal/diff)
are welcome.

## License

[BSD 3-Clause](./LICENSE-BSD) and [MIT](./LICENSE-MIT).

```

### File: diff.go
```go
// Copyright 2019 The Go Authors. All rights reserved.
// Use of this source code is governed by a BSD-style
// license that can be found in the LICENSE file.

// Package diff computes differences between text files or strings.
package udiff

import (
	"fmt"
	"slices"
	"sort"
	"strings"
)

// An Edit describes the replacement of a portion of a text file.
type Edit struct {
	Start, End int    // byte offsets of the region to replace
	New        string // the replacement
}

func (e Edit) String() string {
	return fmt.Sprintf("{Start:%d,End:%d,New:%q}", e.Start, e.End, e.New)
}

// Apply applies a sequence of edits to the src buffer and returns the
// result. Edits are applied in order of start offset; edits with the
// same start offset are applied in they order they were provided.
//
// Apply returns an error if any edit is out of bounds,
// or if any pair of edits is overlapping.
func Apply(src string, edits []Edit) (string, error) {
	edits, size, err := validate(src, edits)
	if err != nil {
		return "", err
	}

	// Apply edits.
	out := make([]byte, 0, size)
	lastEnd := 0
	for _, edit := range edits {
		if lastEnd < edit.Start {
			out = append(out, src[lastEnd:edit.Start]...)
		}
		out = append(out, edit.New...)
		lastEnd = edit.End
	}
	out = append(out, src[lastEnd:]...)

	if len(out) != size {
		panic("wrong size")
	}

	return string(out), nil
}

// ApplyBytes is like Apply, but it accepts a byte slice.
// The result is always a new array.
func ApplyBytes(src []byte, edits []Edit) ([]byte, error) {
	res, err := Apply(string(src), edits)
	return []byte(res), err
}

// validate checks that edits are consistent with src,
// and returns the size of the patched output.
// It may return a different slice.
func validate(src string, edits []Edit) ([]Edit, int, error) {
	if !sort.IsSorted(editsSort(edits)) {
		edits = slices.Clone(edits)
		SortEdits(edits)
	}

	// Check validity of edits and compute final size.
	size := len(src)
	lastEnd := 0
	for _, edit := range edits {
		if !(0 <= edit.Start && edit.Start <= edit.End && edit.End <= len(src)) {
			return nil, 0, fmt.Errorf("diff has out-of-bounds edits")
		}
		if edit.Start < lastEnd {
			return nil, 0, fmt.Errorf("diff has overlapping edits")
		}
		size += len(edit.New) + edit.Start - edit.End
		lastEnd = edit.End
	}

	return edits, size, nil
}

// SortEdits orders a slice of Edits by (start, end) offset.
// This ordering puts insertions (end = start) before deletions
// (end > start) at the same point, but uses a stable sort to preserve
// the order of multiple insertions at the same point.
// (Apply detects multiple deletions at the same point as an error.)
func SortEdits(edits []Edit) {
	sort.Stable(editsSort(edits))
}

type editsSort []Edit

func (a editsSort) Len() int { return len(a) }
func (a editsSort) Less(i, j int) bool {
	if cmp := a[i].Start - a[j].Start; cmp != 0 {
		return cmp < 0
	}
	return a[i].End < a[j].End
}
func (a editsSort) Swap(i, j int) { a[i], a[j] = a[j], a[i] }

// lineEdits expands and merges a sequence of edits so that each
// resulting edit replaces one or more complete lines.
// See ApplyEdits for preconditions.
func lineEdits(src string, edits []Edit) ([]Edit, error) {
	edits, _, err := validate(src, edits)
	if err != nil {
		return nil, err
	}

	// Do all deletions begin and end at the start of a line,
	// and all insertions end with a newline?
	// (This is merely a fast path.)
	for _, edit := range edits {
		if edit.Start >= len(src) || // insertion at EOF
			edit.Start > 0 && src[edit.Start-1] != '\n' || // not at line start
			edit.End > 0 && src[edit.End-1] != '\n' || // not at line start
			edit.New != "" && edit.New[len(edit.New)-1] != '\n' { // partial insert
			goto expand // slow path
		}
	}
	return edits, nil // aligned

expand:
	if len(edits) == 0 {
		return edits, nil // no edits (unreachable due to fast path)
	}
	expanded := make([]Edit, 0, len(edits)) // a guess
	prev := edits[0]
	// TODO(adonovan): opt: start from the first misaligned edit.
	// TODO(adonovan): opt: avoid quadratic cost of string += string.
	for _, edit := range edits[1:] {
		between := src[prev.End:edit.Start]
		if !strings.Contains(between, "\n") {
			// overlapping lines: combine with previous edit.
			prev.New += between + edit.New
			prev.End = edit.End
		} else {
			// non-overlapping lines: flush previous edit.
			expanded = append(expanded, expandEdit(prev, src))
			prev = edit
		}
	}
	return append(expanded, expandEdit(prev, src)), nil // flush final edit
}

// expandEdit returns edit expanded to complete whole lines.
func expandEdit(edit Edit, src string) Edit {
	// Expand start left to start of line.
	// (delta is the zero-based column number of start.)
	start := edit.Start
	if delta := start - 1 - strings.LastIndex(src[:start], "\n"); delta > 0 {
		edit.Start -= delta
		edit.New = src[start-delta:start] + edit.New
	}

	// Expand end right to end of line.
	end := edit.End
	if end > 0 && src[end-1] != '\n' ||
		edit.New != "" && edit.New[len(edit.New)-1] != '\n' {
		if nl := strings.IndexByte(src[end:], '\n'); nl < 0 {
			edit.End = len(src) // extend to EOF
		} else {
			edit.End = end + nl + 1 // extend beyond \n
		}
	}
	edit.New += src[end:edit.End]

	return edit
}

```

### File: diff_test.go
```go
// Copyright 2019 The Go Authors. All rights reserved.
// Use of this source code is governed by a BSD-style
// license that can be found in the LICENSE file.

package udiff_test

import (
	"bytes"
	"math/rand"
	"os"
	"os/exec"
	"path/filepath"
	"reflect"
	"strings"
	"testing"
	"unicode/utf8"

	diff "github.com/aymanbagabas/go-udiff"
	"github.com/aymanbagabas/go-udiff/difftest"
)

func TestApply(t *testing.T) {
	for _, tc := range difftest.TestCases {
		t.Run(tc.Name, func(t *testing.T) {
			got, err := diff.Apply(tc.In, tc.Edits)
			if err != nil {
				t.Fatalf("Apply(Edits) failed: %v", err)
			}
			if got != tc.Out {
				t.Errorf("Apply(Edits): got %q, want %q", got, tc.Out)
			}
			if tc.LineEdits != nil {
				got, err := diff.Apply(tc.In, tc.LineEdits)
				if err != nil {
					t.Fatalf("Apply(LineEdits) failed: %v", err)
				}
				if got != tc.Out {
					t.Errorf("Apply(LineEdits): got %q, want %q", got, tc.Out)
				}
			}
		})
	}
}

func TestNEdits(t *testing.T) {
	for _, tc := range difftest.TestCases {
		edits := diff.Strings(tc.In, tc.Out)
		got, err := diff.Apply(tc.In, edits)
		if err != nil {
			t.Fatalf("Apply failed: %v", err)
		}
		if got != tc.Out {
			t.Fatalf("%s: got %q wanted %q", tc.Name, got, tc.Out)
		}
		if len(edits) < len(tc.Edits) { // should find subline edits
			t.Errorf("got %v, expected %v for %#v", edits, tc.Edits, tc)
		}
	}
}

func TestNRandom(t *testing.T) {
	rnd := rand.New(rand.NewSource(1))
	for i := range 1000 {
		a := randstr(rnd, "abω", 16)
		b := randstr(rnd, "abωc", 16)
		edits := diff.Strings(a, b)
		got, err := diff.Apply(a, edits)
		if err != nil {
			t.Fatalf("Apply failed: %v", err)
		}
		if got != b {
			t.Fatalf("%d: got %q, wanted %q, starting with %q", i, got, b, a)
		}
	}
}

// $ go test -fuzz=FuzzRoundTrip ./internal/diff
func FuzzRoundTrip(f *testing.F) {
	f.Fuzz(func(t *testing.T, a, b string) {
		if !utf8.ValidString(a) || !utf8.ValidString(b) {
			return // inputs must be text
		}
		edits := diff.Strings(a, b)
		got, err := diff.Apply(a, edits)
		if err != nil {
			t.Fatalf("Apply failed: %v", err)
		}
		if got != b {
			t.Fatalf("applying diff(%q, %q) gives %q; edits=%v", a, b, got, edits)
		}
	})
}

func TestLineEdits(t *testing.T) {
	for _, tc := range difftest.TestCases {
		t.Run(tc.Name, func(t *testing.T) {
			want := tc.LineEdits
			if want == nil {
				want = tc.Edits // already line-aligned
			}
			got, err := diff.LineEdits(tc.In, tc.Edits)
			if err != nil {
				t.Fatalf("LineEdits: %v", err)
			}
			if !reflect.DeepEqual(got, want) {
				t.Errorf("in=<<%s>>\nout=<<%s>>\nraw  edits=%s\nline edits=%s\nwant: %s",
					tc.In, tc.Out, tc.Edits, got, want)
			}
			// make sure that applying the edits gives the expected result
			fixed, err := diff.Apply(tc.In, got)
			if err != nil {
				t.Error(err)
			}
			if fixed != tc.Out {
				t.Errorf("Apply(LineEdits): got %q, want %q", fixed, tc.Out)
			}
		})
	}
}

func TestToUnified(t *testing.T) {
	for _, tc := range difftest.TestCases {
		t.Run(tc.Name, func(t *testing.T) {
			nedits := diff.Lines(tc.In, tc.Out)
			xunified, err := diff.ToUnified(difftest.FileA, difftest.FileB, tc.In, nedits, diff.DefaultContextLines)
			if err != nil {
				t.Fatal(err)
			}
			if xunified == "" {
				return
			}
			orig := filepath.Join(t.TempDir(), "original")
			err = os.WriteFile(orig, []byte(tc.In), 0644)
			if err != nil {
				t.Fatal(err)
			}
			temp := filepath.Join(t.TempDir(), "patched")
			err = os.WriteFile(temp, []byte(tc.In), 0644)
			if err != nil {
				t.Fatal(err)
			}
			cmd := exec.Command("patch", "-p0", "-u", "-s", "-o", temp, orig)
			cmd.Stdin = strings.NewReader(xunified)
			cmd.Stdout = new(bytes.Buffer)
			cmd.Stderr = new(bytes.Buffer)
			if err = cmd.Run(); err != nil {
				t.Fatalf("%v: %q (%q) (%q)", err, cmd.String(),
					cmd.Stderr, cmd.Stdout)
			}
			got, err := os.ReadFile(temp)
			if err != nil {
				t.Fatal(err)
			}
			if string(got) != tc.Out {
				t.Errorf("applying unified failed: got\n%q, wanted\n%q unified\n%q",
					got, tc.Out, xunified)
			}

		})
	}
}

func TestRegressionOld001(t *testing.T) {
	a := "// Copyright 2019 The Go Authors. All rights reserved.\n// Use of this source code is governed by a BSD-style\n// license that can be found in the LICENSE file.\n\npackage udiff_test\n\nimport (\n\t\"fmt\"\n\t\"math/rand\"\n\t\"strings\"\n\t\"testing\"\n\n\t\"golang.org/x/tools/gopls/internal/lsp/diff\"\n\t\"github.com/aymanbagabas/go-udiff/difftest\"\n\t\"golang.org/x/tools/gopls/internal/span\"\n)\n"

	b := "// Copyright 2019 The Go Authors. All rights reserved.\n// Use of this source code is governed by a BSD-style\n// license that can be found in the LICENSE file.\n\npackage udiff_test\n\nimport (\n\t\"fmt\"\n\t\"math/rand\"\n\t\"strings\"\n\t\"testing\"\n\n\t\"github.com/google/safehtml/template\"\n\t\"golang.org/x/tools/gopls/internal/lsp/diff\"\n\t\"github.com/aymanbagabas/go-udiff/difftest\"\n\t\"golang.org/x/tools/gopls/internal/span\"\n)\n"
	diffs := diff.Strings(a, b)
	got, err := diff.Apply(a, diffs)
	if err != nil {
		t.Fatalf("Apply failed: %v", err)
	}
	if got != b {
		i := 0
		for ; i < len(a) && i < len(b) && got[i] == b[i]; i++ {
		}
		t.Errorf("oops %vd\n%q\n%q", diffs, got, b)
		t.Errorf("\n%q\n%q", got[i:], b[i:])
	}
}

func TestRegressionOld002(t *testing.T) {
	a := "n\"\n)\n"
	b := "n\"\n\t\"golang.org/x//nnal/stack\"\n)\n"
	diffs := diff.Strings(a, b)
	got, err := diff.Apply(a, diffs)
	if err != nil {
		t.Fatalf("Apply failed: %v", err)
	}
	if got != b {
		i := 0
		for ; i < len(a) && i < len(b) && got[i] == b[i]; i++ {
		}
		t.Errorf("oops %vd\n%q\n%q", diffs, got, b)
		t.Errorf("\n%q\n%q", got[i:], b[i:])
	}
}

// return a random string of length n made of characters from s
func randstr(rnd *rand.Rand, s string, n int) string {
	src := []rune(s)
	x := make([]rune, n)
	for i := range n {
		x[i] = src[rnd.Intn(len(src))]
	}
	return string(x)
}

```

### File: export.go
```go
package udiff

// UnifiedDiff is a unified diff.
type UnifiedDiff = unified

// Hunk represents a single hunk in a unified diff.
type Hunk = hunk

// Line represents a single line in a hunk.
type Line = line

// ToUnifiedDiff takes a file contents and a sequence of edits, and calculates
// a unified diff that represents those edits.
func ToUnifiedDiff(fromName, toName string, content string, edits []Edit, contextLines int) (UnifiedDiff, error) {
	return toUnified(fromName, toName, content, edits, contextLines)
}

```

### File: export_test.go
```go
// Copyright 2022 The Go Authors. All rights reserved.
// Use of this source code is governed by a BSD-style
// license that can be found in the LICENSE file.

package udiff

// This file exports some private declarations to tests.

var LineEdits = lineEdits

```

### File: merge.go
```go
// Copyright 2025 The Go Authors. All rights reserved.
// Use of this source code is governed by a BSD-style
// license that can be found in the LICENSE file.

package udiff

import (
	"slices"
)

// Merge merges two valid, ordered lists of edits.
// It returns zero if there was a conflict.
//
// If corresponding edits in x and y are identical,
// they are coalesced in the result.
//
// If x and y both provide different insertions at the same point,
// the insertions from x will be first in the result.
//
// TODO(adonovan): this algorithm could be improved, for example by
// working harder to coalesce non-identical edits that share a common
// deletion or common prefix of insertion (see the tests).
// Survey the academic literature for insights.
func Merge(x, y []Edit) ([]Edit, bool) {
	// Make a defensive (premature) copy of the arrays.
	x = slices.Clone(x)
	y = slices.Clone(y)

	var merged []Edit
	add := func(edit Edit) {
		merged = append(merged, edit)
	}
	var xi, yi int
	for xi < len(x) && yi < len(y) {
		px := &x[xi]
		py := &y[yi]

		if *px == *py {
			// x and y are identical: coalesce.
			add(*px)
			xi++
			yi++

		} else if px.End <= py.Start {
			// x is entirely before y,
			// or an insertion at start of y.
			add(*px)
			xi++

		} else if py.End <= px.Start {
			// y is entirely before x,
			// or an insertion at start of x.
			add(*py)
			yi++

		} else if px.Start < py.Start {
			// x is partly before y:
			// split it into a deletion and an edit.
			add(Edit{px.Start, py.Start, ""})
			px.Start = py.Start

		} else if py.Start < px.Start {
			// y is partly before x:
			// split it into a deletion and an edit.
			add(Edit{py.Start, px.Start, ""})
			py.Start = px.Start

		} else {
			// x and y are unequal non-insertions
			// at the same point: conflict.
			return nil, false
		}
	}
	for ; xi < len(x); xi++ {
		add(x[xi])
	}
	for ; yi < len(y); yi++ {
		add(y[yi])
	}
	return merged, true
}

```

### File: merge_test.go
```go
// Copyright 2025 The Go Authors. All rights reserved.
// Use of this source code is governed by a BSD-style
// license that can be found in the LICENSE file.

package udiff_test

import (
	"testing"

	diff "github.com/aymanbagabas/go-udiff"
)

func TestMerge(t *testing.T) {
	// For convenience, we test Merge using strings, not sequences
	// of edits, though this does put us at the mercy of the diff
	// algorithm.
	for _, test := range []struct {
		base, x, y string
		want       string // "!" => conflict
	}{
		// independent insertions
		{"abcdef", "abXcdef", "abcdeYf", "abXcdeYf"},
		// independent deletions
		{"abcdef", "acdef", "abcdf", "acdf"},
		// colocated insertions (X first)
		{"abcdef", "abcXdef", "abcYdef", "abcXYdef"},
		// colocated identical insertions (coalesced)
		{"abcdef", "abcXdef", "abcXdef", "abcXdef"},
		// colocated insertions with common prefix (X first)
		// TODO(adonovan): would "abcXYdef" be better?
		// i.e. should we dissect the insertions?
		{"abcdef", "abcXdef", "abcXYdef", "abcXXYdef"},
		// mix of identical and independent insertions (X first)
		{"abcdef", "aIbcdXef", "aIbcdYef", "aIbcdXYef"},
		// independent deletions
		{"abcdef", "def", "abc", ""},
		// overlapping deletions: conflict
		{"abcdef", "adef", "abef", "!"},
		// overlapping deletions with distinct insertions, X first
		{"abcdef", "abXef", "abcYf", "!"},
		// overlapping deletions with distinct insertions, Y first
		{"abcdef", "abcXf", "abYef", "!"},
		// overlapping deletions with common insertions
		{"abcdef", "abXef", "abcXf", "!"},
		// trailing insertions in X (observe X bias)
		{"abcdef", "aXbXcXdXeXfX", "aYbcdef", "aXYbXcXdXeXfX"},
		// trailing insertions in Y (observe X bias)
		{"abcdef", "aXbcdef", "aYbYcYdYeYfY", "aXYbYcYdYeYfY"},
	} {
		dx := diff.Strings(test.base, test.x)
		dy := diff.Strings(test.base, test.y)
		got := "!" // conflict
		if dz, ok := diff.Merge(dx, dy); ok {
			var err error
			got, err = diff.Apply(test.base, dz)
			if err != nil {
				t.Errorf("Merge(%q, %q, %q) produced invalid edits %v: %v", test.base, test.x, test.y, dz, err)
				continue
			}
		}
		if test.want != got {
			t.Errorf("base=%q x=%q y=%q: got %q, want %q", test.base, test.x, test.y, got, test.want)
		}
	}
}

```

### File: ndiff.go
```go
// Copyright 2022 The Go Authors. All rights reserved.
// Use of this source code is governed by a BSD-style
// license that can be found in the LICENSE file.

package udiff

import (
	"bytes"
	"strings"
	"unicode/utf8"

	"github.com/aymanbagabas/go-udiff/lcs"
)

// Lines computes differences between two strings. All edits are at line boundaries.
func Lines(before, after string) []Edit {
	beforeLines, bOffsets := splitLines(before)
	afterLines, _ := splitLines(after)
	diffs := lcs.DiffLines(beforeLines, afterLines)

	// Convert from LCS diffs to Edits
	res := make([]Edit, len(diffs))
	for i, d := range diffs {
		res[i] = Edit{
			Start: bOffsets[d.Start],
			End:   bOffsets[d.End],
			New:   strings.Join(afterLines[d.ReplStart:d.ReplEnd], ""),
		}
	}
	return res
}

// Strings computes the differences between two strings.
// The resulting edits respect rune boundaries.
func Strings(before, after string) []Edit {
	if before == after {
		return nil // common case
	}

	if isASCII(before) && isASCII(after) {
		// TODO(adonovan): opt: specialize diffASCII for strings.
		return diffASCII([]byte(before), []byte(after))
	}
	return diffRunes([]rune(before), []rune(after))
}

// Bytes computes the differences between two byte slices.
// The resulting edits respect rune boundaries.
func Bytes(before, after []byte) []Edit {
	if bytes.Equal(before, after) {
		return nil // common case
	}

	if isASCII(before) && isASCII(after) {
		return diffASCII(before, after)
	}
	return diffRunes(runes(before), runes(after))
}

func diffASCII(before, after []byte) []Edit {
	diffs := lcs.DiffBytes(before, after)

	// Convert from LCS diffs.
	res := make([]Edit, len(diffs))
	for i, d := range diffs {
		res[i] = Edit{d.Start, d.End, string(after[d.ReplStart:d.ReplEnd])}
	}
	return res
}

func diffRunes(before, after []rune) []Edit {
	diffs := lcs.DiffRunes(before, after)

	// The diffs returned by the lcs package use indexes
	// into whatever slice was passed in.
	// Convert rune offsets to byte offsets.
	res := make([]Edit, len(diffs))
	lastEnd := 0
	utf8Len := 0
	for i, d := range diffs {
		utf8Len += runesLen(before[lastEnd:d.Start]) // text between edits
		start := utf8Len
		utf8Len += runesLen(before[d.Start:d.End]) // text deleted by this edit
		res[i] = Edit{start, utf8Len, string(after[d.ReplStart:d.ReplEnd])}
		lastEnd = d.End
	}
	return res
}

// runes is like []rune(string(bytes)) without the duplicate allocation.
func runes(bytes []byte) []rune {
	n := utf8.RuneCount(bytes)
	runes := make([]rune, n)
	for i := range n {
		r, sz := utf8.DecodeRune(bytes)
		bytes = bytes[sz:]
		runes[i] = r
	}
	return runes
}

// runesLen returns the length in bytes of the UTF-8 encoding of runes.
func runesLen(runes []rune) (len int) {
	for _, r := range runes {
		len += utf8.RuneLen(r)
	}
	return len
}

// isASCII reports whether s contains only ASCII.
func isASCII[S string | []byte](s S) bool {
	for i := 0; i < len(s); i++ {
		if s[i] >= utf8.RuneSelf {
			return false
		}
	}
	return true
}

```

### File: unified.go
```go
// Copyright 2019 The Go Authors. All rights reserved.
// Use of this source code is governed by a BSD-style
// license that can be found in the LICENSE file.

package udiff

import (
	"fmt"
	"log"
	"regexp"
	"strconv"
	"strings"
)

// DefaultContextLines is the number of unchanged lines of surrounding
// context displayed by Unified. Use ToUnified to specify a different value.
const DefaultContextLines = 3

// Unified returns a unified diff of the old and new strings.
// The old and new labels are the names of the old and new files.
// If the strings are equal, it returns the empty string.
func Unified(oldLabel, newLabel, old, new string) string {
	edits := Lines(old, new)
	unified, err := ToUnified(oldLabel, newLabel, old, edits, DefaultContextLines)
	if err != nil {
		// Can't happen: edits are consistent.
		log.Fatalf("internal error in diff.Unified: %v", err)
	}
	return unified
}

// ToUnified applies the edits to content and returns a unified diff,
// with contextLines lines of (unchanged) context around each diff hunk.
// The old and new labels are the names of the content and result files.
// It returns an error if the edits are inconsistent; see ApplyEdits.
func ToUnified(oldLabel, newLabel, content string, edits []Edit, contextLines int) (string, error) {
	u, err := toUnified(oldLabel, newLabel, content, edits, contextLines)
	if err != nil {
		return "", err
	}
	return u.String(), nil
}

// unified represents a set of edits as a unified diff.
type unified struct {
	// From is the name of the original file.
	From string
	// To is the name of the modified file.
	To string
	// Hunks is the set of edit Hunks needed to transform the file content.
	Hunks []*hunk
}

// Hunk represents a contiguous set of line edits to apply.
type hunk struct {
	// The line in the original source where the hunk starts.
	FromLine int
	// The line in the original source where the hunk finishes.
	ToLine int
	// The set of line based edits to apply.
	Lines []line
}

// Line represents a single line operation to apply as part of a Hunk.
type line struct {
	// Kind is the type of line this represents, deletion, insertion or copy.
	Kind OpKind
	// Content is the Content of this line.
	// For deletion it is the line being removed, for all others it is the line
	// to put in the output.
	Content string
}

// OpKind is used to denote the type of operation a line represents.
type OpKind int

const (
	// Delete is the operation kind for a line that is present in the input
	// but not in the output.
	Delete OpKind = iota
	// Insert is the operation kind for a line that is new in the output.
	Insert
	// Equal is the operation kind for a line that is the same in the input and
	// output, often used to provide context around edited lines.
	Equal
)

// String returns a human readable representation of an OpKind. It is not
// intended for machine processing.
func (k OpKind) String() string {
	switch k {
	case Delete:
		return "delete"
	case Insert:
		return "insert"
	case Equal:
		return "equal"
	default:
		panic("unknown operation kind")
	}
}

// toUnified takes a file contents and a sequence of edits, and calculates
// a unified diff that represents those edits.
func toUnified(fromName, toName string, content string, edits []Edit, contextLines int) (unified, error) {
	gap := contextLines * 2
	u := unified{
		From: fromName,
		To:   toName,
	}
	if len(edits) == 0 {
		return u, nil
	}
	var err error
	edits, err = lineEdits(content, edits) // expand to whole lines
	if err != nil {
		return u, err
	}
	lines, _ := splitLines(content)
	var h *hunk
	last := 0
	toLine := 0
	for _, edit := range edits {
		// Compute the zero-based line numbers of the edit start and end.
		// TODO(adonovan): opt: compute incrementally, avoid O(n^2).
		start := strings.Count(content[:edit.Start], "\n")
		end := strings.Count(content[:edit.End], "\n")
		if edit.End == len(content) && len(content) > 0 && content[len(content)-1] != '\n' {
			end++ // EOF counts as an implicit newline
		}

		switch {
		case h != nil && start == last:
			//direct extension
		case h != nil && start <= last+gap:
			//within range of previous lines, add the joiners
			addEqualLines(h, lines, last, start)
		default:
			//need to start a new hunk
			if h != nil {
				// add the edge to the previous hunk
				addEqualLines(h, lines, last, last+contextLines)
				u.Hunks = append(u.Hunks, h)
			}
			toLine += start - last
			h = &hunk{
				FromLine: start + 1,
				ToLine:   toLine + 1,
			}
			// add the edge to the new hunk
			delta := addEqualLines(h, lines, start-contextLines, start)
			h.FromLine -= delta
			h.ToLine -= delta
		}
		last = start
		for i := start; i < end; i++ {
			h.Lines = append(h.Lines, line{Kind: Delete, Content: lines[i]})
			last++
		}
		if edit.New != "" {
			v, _ := splitLines(edit.New)
			for _, content := range v {
				h.Lines = append(h.Lines, line{Kind: Insert, Content: content})
				toLine++
			}
		}
	}
	if h != nil {
		// add the edge to the final hunk
		addEqualLines(h, lines, last, last+contextLines)
		u.Hunks = append(u.Hunks, h)
	}
	return u, nil
}

// split into lines removing a final empty line,
// and also return the offsets of the line beginnings.
func splitLines(text string) ([]string, []int) {
	var lines []string
	offsets := []int{0}
	start := 0
	for i, r := range text {
		if r == '\n' {
			lines = append(lines, text[start:i+1])
			start = i + 1
			offsets = append(offsets, start)
		}
	}
	if start < len(text) {
		lines = append(lines, text[start:])
		offsets = append(offsets, len(text))
	}
	return lines, offsets
}

func addEqualLines(h *hunk, lines []string, start, end int) int {
	delta := 0
	for i := start; i < end; i++ {
		if i < 0 {
			continue
		}
		if i >= len(lines) {
			return delta
		}
		h.Lines = append(h.Lines, line{Kind: Equal, Content: lines[i]})
		delta++
	}
	return delta
}

// String converts a unified diff to the standard textual form for that diff.
// The output of this function can be passed to tools like patch.
func (u unified) String() string {
	if len(u.Hunks) == 0 {
		return ""
	}
	b := new(strings.Builder)
	fmt.Fprintf(b, "--- %s\n", u.From)
	fmt.Fprintf(b, "+++ %s\n", u.To)
	for _, hunk := range u.Hunks {
		fromCount, toCount := 0, 0
		for _, l := range hunk.Lines {
			switch l.Kind {
			case Delete:
				fromCount++
			case Insert:
				toCount++
			default:
				fromCount++
				toCount++
			}
		}
		fmt.Fprint(b, "@@")
		if fromCount > 1 {
			fmt.Fprintf(b, " -%d,%d", hunk.FromLine, fromCount)
		} else if hunk.FromLine == 1 && fromCount == 0 {
			// Match odd GNU diff -u behavior adding to empty file.
			fmt.Fprintf(b, " -0,0")
		} else {
			fmt.Fprintf(b, " -%d", hunk.FromLine)
		}
		if toCount > 1 {
			fmt.Fprintf(b, " +%d,%d", hunk.ToLine, toCount)
		} else if hunk.ToLine == 1 && toCount == 0 {
			// Match odd GNU diff -u behavior adding to empty file.
			fmt.Fprintf(b, " +0,0")
		} else {
			fmt.Fprintf(b, " +%d", hunk.ToLine)
		}
		fmt.Fprint(b, " @@\n")
		for _, l := range hunk.Lines {
			switch l.Kind {
			case Delete:
				fmt.Fprintf(b, "-%s", l.Content)
			case Insert:
				fmt.Fprintf(b, "+%s", l.Content)
			default:
				fmt.Fprintf(b, " %s", l.Content)
			}
			if !strings.HasSuffix(l.Content, "\n") {
				fmt.Fprintf(b, "\n\\ No newline at end of file\n")
			}
		}
	}
	return b.String()
}

// ApplyUnified applies the unified diffs.
func ApplyUnified(udiffs, bef string) (string, error) {
	before := strings.Split(bef, "\n")
	unif := strings.Split(udiffs, "\n")
	var got []string
	left := 0
	// parse and apply the unified diffs
	for _, l := range unif {
		if len(l) == 0 {
			continue // probably the last line (from Split)
		}
		switch l[0] {
		case '@': // The @@ line
			m := atregexp.FindStringSubmatch(l)
			fromLine, err := strconv.Atoi(m[1])
			if err != nil {
				return "", fmt.Errorf("missing line number in %q", l)
			}
			// before is a slice, so0-based; fromLine is 1-based
			for ; left < fromLine-1; left++ {
				got = append(got, before[left])
			}
		case '+': // add this line
			if strings.HasPrefix(l, "+++ ") {
				continue
			}
			got = append(got, l[1:])
		case '-': // delete this line
			if strings.HasPrefix(l, "--- ") {
				continue
			}
			left++
		case ' ':
			return "", fmt.Errorf("unexpected line %q", l)
		default:
			return "", fmt.Errorf("impossible unified %q", udiffs)
		}
	}
	// copy any remaining lines
	for ; left < len(before); left++ {
		got = append(got, before[left])
	}
	return strings.Join(got, "\n"), nil
}

// The first number in the @@ lines is the line number in the 'before' data
var atregexp = regexp.MustCompile(`@@ -(\d+).* @@`)

```

### File: scripts\import.sh
```sh
#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$REPO_ROOT"

UPSTREAM_REPO="https://github.com/golang/tools"
UPSTREAM_PKG="internal/diff"
MODULE_PATH="github.com/aymanbagabas/go-udiff"

# Clone upstream to a temporary directory.
tools=$(mktemp -d)/tools
trap 'rm -rf "$(dirname "$tools")"' EXIT
git clone --depth 1 "$UPSTREAM_REPO" "$tools"

# Copy the diff package to the current directory.
cp -r "$tools/$UPSTREAM_PKG/"* .

# Replace import paths.
find . -type f -name '*.go' -exec sed -i'' "s|golang.org/x/tools/${UPSTREAM_PKG}/|${MODULE_PATH}/|g" {} +
find . -type f -name '*.go' -exec sed -i'' "s|\"golang.org/x/tools/${UPSTREAM_PKG}|diff \"${MODULE_PATH}|g" {} +

# Change package name to udiff.
sed -i'' 's|package diff|package udiff|g' *.go

# Apply patches.
for p in _patches/*; do
	git apply "$p"
done

# Resolve upstream commit.
commit=$(cd "$tools" && git rev-parse HEAD)

# Update the upstream commit marker if there are changes.
if ! git update-index --refresh >/dev/null 2>&1 || ! git diff-index --quiet HEAD --; then
	echo "$commit" >.github/UPSTREAM
	echo "Upstream updated to $commit"
else
	echo "No changes from upstream"
fi

```

