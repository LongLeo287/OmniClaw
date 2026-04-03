---
id: github.com-sourcegraph-go-diff-98fe7565-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:24.095487
---

# KNOWLEDGE EXTRACT: github.com_sourcegraph_go-diff_98fe7565
> **Extracted on:** 2026-04-01 16:08:24
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007524925/github.com_sourcegraph_go-diff_98fe7565

---

## File: `.travis.yml`
```yaml
sudo: false
language: go
go:
  - "1.14.x"
script:
  - GO111MODULE=on go get -t -v ./...
  - diff -u <(echo -n) <(gofmt -d -s .)
  - GO111MODULE=on go test -v -race -coverprofile=coverage.txt -covermode=atomic ./...
after_success:
  - bash <(curl -s https://codecov.io/bash)
```

## File: `LICENSE`
```
Copyright (c) 2014 Sourcegraph, Inc.

Permission is hereby granted, free of charge, to any person
obtaining a copy of this software and associated documentation
files (the "Software"), to deal in the Software without
restriction, including without limitation the rights to use,
copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following
conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

-----------------------------------------------------------------

Portions adapted from python-unidiff:

Copyright (c) 2012 Matias Bordese

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE
OR OTHER DEALINGS IN THE SOFTWARE.
```

## File: `README.md`
```markdown
# go-diff [![GoDoc](https://godoc.org/github.com/sourcegraph/go-diff/diff?status.svg)](https://godoc.org/github.com/sourcegraph/go-diff/diff)

Diff parser and printer for Go.

Installing
----------

```bash
go get -u github.com/sourcegraph/go-diff/diff
```

Usage
-----

It doesn't actually compute a diff. It only reads in (and prints out, given a Go struct representation) unified diff output, such as the following. The corresponding data structure in Go is the `diff.FileDiff` struct.

```diff
--- oldname	2009-10-11 15:12:20.000000000 -0700
+++ newname	2009-10-11 15:12:30.000000000 -0700
@@ -1,3 +1,9 @@ Section Header
+This is an important
+notice! It should
+therefore be located at
+the beginning of this
+document!
+
 This part of the
 document has stayed the
 same from version to
@@ -5,16 +11,10 @@
 be shown if it doesn't
 change.  Otherwise, that
 would not be helping to
-compress the size of the
-changes.
-
-This paragraph contains
-text that is outdated.
-It will be deleted in the
-near future.
+compress anything.
```
```

## File: `go.mod`
```
module github.com/sourcegraph/go-diff

go 1.14

require github.com/google/go-cmp v0.5.2
```

## File: `go.sum`
```
github.com/google/go-cmp v0.5.2 h1:X2ev0eStA3AbceY54o37/0PQ/UWqKEiiO2dKL5OPaFM=
github.com/google/go-cmp v0.5.2/go.mod h1:v8dTdLbMG2kIc/vJvl+f65V22dbkXbowE6jgT/gNBxE=
golang.org/x/xerrors v0.0.0-20191204190536-9bdfabe68543 h1:E7g+9GITq07hpfrRu66IVDexMakfv52eLZ2CXBWiKr4=
golang.org/x/xerrors v0.0.0-20191204190536-9bdfabe68543/go.mod h1:I/5z698sn9Ka8TeJc9MKroUUfqBBauWjQqLJ2OPfmY0=
```

## File: `cmd/go-diff/go-diff.go`
```go
package main

import (
	"flag"
	"fmt"
	"io"
	"log"
	"os"

	"github.com/sourcegraph/go-diff/diff"
)

// A diagnostic program to aid in debugging diff parsing or printing
// errors.

const stdin = "<stdin>"

var (
	diffPath = flag.String("f", stdin, "filename of diff (default: stdin)")
	fileIdx  = flag.Int("i", -1, "if >= 0, only print and report errors from the i'th file (0-indexed)")
)

func main() {
	log.SetFlags(0)
	flag.Parse()

	var diffFile *os.File
	if *diffPath == stdin {
		diffFile = os.Stdin
	} else {
		var err error
		diffFile, err = os.Open(*diffPath)
		if err != nil {
			log.Fatal(err)
		}
	}
	defer diffFile.Close()

	r := diff.NewMultiFileDiffReader(diffFile)
	for i := 0; ; i++ {
		report := (*fileIdx == -1) || i == *fileIdx // true if -i==-1 or if this is the i'th file

		label := fmt.Sprintf("file(%d)", i)
		fdiff, err := r.ReadFile()
		if fdiff != nil {
			label = fmt.Sprintf("orig(%s) new(%s)", fdiff.OrigName, fdiff.NewName)
		}
		if err == io.EOF {
			break
		}
		if err != nil {
			if report {
				log.Fatalf("err read %s: %s", label, err)
			} else {
				continue
			}
		}

		if report {
			log.Printf("ok read: %s", label)
		}

		out, err := diff.PrintFileDiff(fdiff)
		if err != nil {
			if report {
				log.Fatalf("err print %s: %s", label, err)
			} else {
				continue
			}
		}
		if report {
			if _, err := os.Stdout.Write(out); err != nil {
				log.Fatal(err)
			}
		}
	}
}
```

## File: `diff/diff.go`
```go
package diff

import (
	"bytes"
	"time"
)

// A FileDiff represents a unified diff for a single file.
//
// A file unified diff has a header that resembles the following:
//
//   --- oldname	2009-10-11 15:12:20.000000000 -0700
//   +++ newname	2009-10-11 15:12:30.000000000 -0700
type FileDiff struct {
	// the original name of the file
	OrigName string
	// the original timestamp (nil if not present)
	OrigTime *time.Time
	// the new name of the file (often same as OrigName)
	NewName string
	// the new timestamp (nil if not present)
	NewTime *time.Time
	// extended header lines (e.g., git's "new mode <mode>", "rename from <path>", etc.)
	Extended []string
	// hunks that were changed from orig to new
	Hunks []*Hunk
}

// A Hunk represents a series of changes (additions or deletions) in a file's
// unified diff.
type Hunk struct {
	// starting line number in original file
	OrigStartLine int32
	// number of lines the hunk applies to in the original file
	OrigLines int32
	// if > 0, then the original file had a 'No newline at end of file' mark at this offset
	OrigNoNewlineAt int32
	// starting line number in new file
	NewStartLine int32
	// number of lines the hunk applies to in the new file
	NewLines int32
	// optional section heading
	Section string
	// 0-indexed line offset in unified file diff (including section headers); this is
	// only set when Hunks are read from entire file diff (i.e., when ReadAllHunks is
	// called) This accounts for hunk headers, too, so the StartPosition of the first
	// hunk will be 1.
	StartPosition int32
	// hunk body (lines prefixed with '-', '+', or ' ')
	Body []byte
}

// A Stat is a diff stat that represents the number of lines added/changed/deleted.
type Stat struct {
	// number of lines added
	Added int32
	// number of lines changed
	Changed int32
	// number of lines deleted
	Deleted int32
}

// Stat computes the number of lines added/changed/deleted in all
// hunks in this file's diff.
func (d *FileDiff) Stat() Stat {
	total := Stat{}
	for _, h := range d.Hunks {
		total.add(h.Stat())
	}
	return total
}

// Stat computes the number of lines added/changed/deleted in this
// hunk.
func (h *Hunk) Stat() Stat {
	lines := bytes.Split(h.Body, []byte{'\n'})
	var last byte
	st := Stat{}
	for _, line := range lines {
		if len(line) == 0 {
			last = 0
			continue
		}
		switch line[0] {
		case '-':
			if last == '+' {
				st.Added--
				st.Changed++
				last = 0 // next line can't change this one since this is already a change
			} else {
				st.Deleted++
				last = line[0]
			}
		case '+':
			if last == '-' {
				st.Deleted--
				st.Changed++
				last = 0 // next line can't change this one since this is already a change
			} else {
				st.Added++
				last = line[0]
			}
		default:
			last = 0
		}
	}
	return st
}

var (
	hunkPrefix          = []byte("@@ ")
	onlyInMessagePrefix = []byte("Only in ")
)

const hunkHeader = "@@ -%d,%d +%d,%d @@"
const onlyInMessage = "Only in %s: %s\n"

// diffTimeParseLayout is the layout used to parse the time in unified diff file
// header timestamps.
// See https://www.gnu.org/software/diffutils/manual/html_node/Detailed-Unified.html.
const diffTimeParseLayout = "2006-01-02 15:04:05 -0700"

// Apple's diff is based on freebsd diff, which uses a timestamp format that does
// not include the timezone offset.
const diffTimeParseWithoutTZLayout = "2006-01-02 15:04:05"

// diffTimeFormatLayout is the layout used to format (i.e., print) the time in unified diff file
// header timestamps.
// See https://www.gnu.org/software/diffutils/manual/html_node/Detailed-Unified.html.
const diffTimeFormatLayout = "2006-01-02 15:04:05.000000000 -0700"

func (s *Stat) add(o Stat) {
	s.Added += o.Added
	s.Changed += o.Changed
	s.Deleted += o.Deleted
}
```

## File: `diff/diff_test.go`
```go
package diff

import (
	"bytes"
	"io"
	"io/ioutil"
	"path/filepath"
	"reflect"
	"strings"
	"testing"
	"time"

	"github.com/google/go-cmp/cmp"
)

func unix(sec int64) *time.Time {
	t := time.Unix(sec, 0)
	return &t
}

func init() {
	// Diffs include times that by default are generated in the local
	// timezone. To ensure that tests behave the same in all timezones
	// (compared to the hard-coded expected output), force the test
	// timezone to UTC.
	//
	// This is safe to do in tests but should not (and need not) be
	// done for the main code.
	time.Local = time.UTC
}

func TestParseHunkNoChunksize(t *testing.T) {
	filename := "sample_no_chunksize.diff"
	diffData, err := ioutil.ReadFile(filepath.Join("testdata", filename))
	if err != nil {
		t.Fatal(err)
	}
	diff, err := ParseHunks(diffData)
	if err != nil {
		t.Errorf("%s: got ParseHunks err %v,  want %v", filename, err, nil)
	}
	if len(diff) != 1 {
		t.Fatalf("%s: Got %d hunks, want only one", filename, len(diff))
	}

	correct := &Hunk{
		NewLines:      1,
		NewStartLine:  1,
		OrigLines:     0,
		OrigStartLine: 0,
		StartPosition: 1,
	}
	h := diff[0]
	h.Body = nil // We're not testing the body.
	if !cmp.Equal(h, correct) {
		t.Errorf("%s: got - want:\n%s", filename, cmp.Diff(correct, h))
	}
}

func TestParseHunksAndPrintHunks(t *testing.T) {
	tests := []struct {
		filename     string
		wantParseErr error
	}{
		{filename: "sample_hunk.diff"},
		{filename: "sample_hunks.diff"},
		{filename: "sample_bad_hunks.diff"},
		{filename: "sample_hunks_no_newline.diff"},
		{filename: "no_newline_both.diff"},
		{filename: "no_newline_both2.diff"},
		{filename: "no_newline_orig.diff"},
		{filename: "no_newline_new.diff"},
		{filename: "empty_orig.diff"},
		{filename: "empty_new.diff"},
		{filename: "oneline_hunk.diff"},
		{filename: "empty.diff"},
		{filename: "sample_hunk_lines_start_with_minuses.diff"},
		{filename: "sample_hunk_lines_start_with_minuses_pluses.diff"},
	}
	for _, test := range tests {
		diffData, err := ioutil.ReadFile(filepath.Join("testdata", test.filename))
		if err != nil {
			t.Fatal(err)
		}
		diff, err := ParseHunks(diffData)
		if err != test.wantParseErr {
			t.Errorf("%s: got ParseHunks err %v, want %v", test.filename, err, test.wantParseErr)
			continue
		}
		if test.wantParseErr != nil {
			continue
		}

		printed, err := PrintHunks(diff)
		if err != nil {
			t.Errorf("%s: PrintHunks: %s", test.filename, err)
		}
		if !bytes.Equal(printed, diffData) {
			t.Errorf("%s: printed diff hunks != original diff hunks\n\n# PrintHunks output - Original:\n%s", test.filename, cmp.Diff(diffData, printed))
		}
	}
}

func TestParseFileDiffHeaders(t *testing.T) {
	tests := []struct {
		filename string
		wantDiff *FileDiff
	}{
		{
			filename: "sample_file.diff",
			wantDiff: &FileDiff{
				OrigName: "oldname",
				OrigTime: unix(1255273940), // 2009-10-11 15:12:20
				NewName:  "newname",
				NewTime:  unix(1255273950), // 2009-10-11 15:12:30
			},
		},
		{
			filename: "sample_file_no_fractional_seconds.diff",
			wantDiff: &FileDiff{
				OrigName: "goyaml.go",
				OrigTime: unix(1322164040), // 2011-11-24 19:47:20
				NewName:  "goyaml.go",
				NewTime:  unix(1322486679), // 2011-11-28 13:24:39
			},
		},
		{
			filename: "sample_file_extended.diff",
			wantDiff: &FileDiff{
				OrigName: "oldname",
				OrigTime: unix(1255273940), // 2009-10-11 15:12:20
				NewName:  "newname",
				NewTime:  unix(1255273950), // 2009-10-11 15:12:30
				Extended: []string{
					"diff --git a/vcs/git_cmd.go b/vcs/git_cmd.go",
					"index aa4de15..7c048ab 100644",
				},
			},
		},
		{
			filename: "sample_file_extended_empty_new.diff",
			wantDiff: &FileDiff{
				OrigName: "/dev/null",
				OrigTime: nil,
				NewName:  "b/vendor/go/build/testdata/empty/dummy",
				NewTime:  nil,
				Extended: []string{
					"diff --git a/vendor/go/build/testdata/empty/dummy b/vendor/go/build/testdata/empty/dummy",
					"new file mode 100644",
					"index 0000000..e69de29",
				},
			},
		},
		{
			filename: "sample_file_extended_empty_mode_change.diff",
			wantDiff: &FileDiff{
				OrigName: "a/docs/index.md",
				OrigTime: nil,
				NewName:  "b/docs/index.md",
				NewTime:  nil,
				Extended: []string{
					"diff --git a/docs/index.md b/docs/index.md",
					"old mode 100644",
					"new mode 100755",
				},
			},
		},
		{
			filename: "sample_file_extended_empty_new_binary.diff",
			wantDiff: &FileDiff{
				OrigName: "/dev/null",
				OrigTime: nil,
				NewName:  "b/diff/binary-image.png",
				NewTime:  nil,
				Extended: []string{
					"diff --git a/diff/binary-image.png b/diff/binary-image.png",
					"new file mode 100644",
					"index 0000000..b51756e",
					"Binary files /dev/null and b/diff/binary-image.png differ",
				},
			},
		},
		{
			filename: "sample_file_extended_empty_deleted.diff",
			wantDiff: &FileDiff{
				OrigName: "a/vendor/go/build/testdata/empty/dummy",
				OrigTime: nil,
				NewName:  "/dev/null",
				NewTime:  nil,
				Extended: []string{
					"diff --git a/vendor/go/build/testdata/empty/dummy b/vendor/go/build/testdata/empty/dummy",
					"deleted file mode 100644",
					"index e69de29..0000000",
				},
			},
		},
		{
			filename: "sample_file_extended_empty_deleted_binary.diff",
			wantDiff: &FileDiff{
				OrigName: "a/187/player/random/gopher-0.png",
				OrigTime: nil,
				NewName:  "/dev/null",
				NewTime:  nil,
				Extended: []string{
					"diff --git a/187/player/random/gopher-0.png b/187/player/random/gopher-0.png",
					"deleted file mode 100644",
					"index aebdfc7..0000000",
					"Binary files a/187/player/random/gopher-0.png and /dev/null differ",
				},
			},
		},
		{
			filename: "sample_file_extended_empty_rename.diff",
			wantDiff: &FileDiff{
				OrigName: "a/docs/integrations/Email_Notifications.md",
				OrigTime: nil,
				NewName:  "b/docs/integrations/email-notifications.md",
				NewTime:  nil,
				Extended: []string{
					"diff --git a/docs/integrations/Email_Notifications.md b/docs/integrations/email-notifications.md",
					"similarity index 100%",
					"rename from docs/integrations/Email_Notifications.md",
					"rename to docs/integrations/email-notifications.md",
				},
			},
		},
		{
			filename: "sample_file_extended_empty_rename_and_mode_change.diff",
			wantDiff: &FileDiff{
				OrigName: "a/textfile.txt",
				OrigTime: nil,
				NewName:  "b/textfile2.txt",
				NewTime:  nil,
				Extended: []string{
					"diff --git a/textfile.txt b/textfile2.txt",
					"old mode 100644",
					"new mode 100755",
					"similarity index 100%",
					"rename from textfile.txt",
					"rename to textfile2.txt",
				},
			},
		},
		{
			filename: "quoted_filename.diff",
			wantDiff: &FileDiff{
				OrigName: "a/商品详情.txt",
				OrigTime: nil,
				NewName:  "b/商品详情.txt",
				NewTime:  nil,
				Extended: []string{
					"diff --git \"a/\\345\\225\\206\\345\\223\\201\\350\\257\\246\\346\\203\\205.txt\" \"b/\\345\\225\\206\\345\\223\\201\\350\\257\\246\\346\\203\\205.txt\"",
					"index e69de29..c67479b 100644",
				},
			},
		},
		{
			filename: "sample_file_extended_binary_rename.diff",
			wantDiff: &FileDiff{
				OrigName: "a/data/Font.png",
				OrigTime: nil,
				NewName:  "b/data/Other.png",
				NewTime:  nil,
				Extended: []string{
					"diff --git a/data/Font.png b/data/Other.png",
					"similarity index 51%",
					"rename from data/Font.png",
					"rename to data/Other.png",
					"index 17a971d..599f8dd 100644",
					"Binary files a/data/Font.png and b/data/Other.png differ",
				},
			},
		},
		{
			filename: "sample_file_extended_binary_rename_no_index.diff",
			wantDiff: &FileDiff{
				OrigName: "a/data/foo.txt",
				OrigTime: nil,
				NewName:  "b/data/bar.txt",
				NewTime:  nil,
				Extended: []string{
					"diff --git a/data/foo.txt b/data/bar.txt",
					"similarity index 100%",
					"rename from data/foo.txt",
					"rename to data/bar.txt",
					"Binary files a/data/foo.txt and b/data/bar.txt differ",
				},
			},
		},
	}
	for _, test := range tests {
		t.Run(test.filename, func(t *testing.T) {
			diffData, err := ioutil.ReadFile(filepath.Join("testdata", test.filename))
			if err != nil {
				t.Fatal(err)
			}
			diff, err := ParseFileDiff(diffData)
			if err != nil {
				t.Fatalf("%s: got ParseFileDiff error %v", test.filename, err)
			}

			diff.Hunks = nil
			if got, want := diff, test.wantDiff; !cmp.Equal(got, want) {
				t.Errorf("%s:\n\ngot - want:\n%s", test.filename, cmp.Diff(want, got))
			}
		})
	}
}

func TestParseMultiFileDiffHeaders(t *testing.T) {
	tests := []struct {
		filename  string
		wantDiffs []*FileDiff
	}{
		{
			filename: "sample_multi_file_new.diff",
			wantDiffs: []*FileDiff{
				{
					OrigName: "/dev/null",
					OrigTime: nil,
					NewName:  "b/_vendor/go/build/syslist_test.go",
					NewTime:  nil,
					Extended: []string{
						"diff --git a/_vendor/go/build/syslist_test.go b/_vendor/go/build/syslist_test.go",
						"new file mode 100644",
						"index 0000000..3be2928",
					},
				},
				{
					OrigName: "/dev/null",
					OrigTime: nil,
					NewName:  "b/_vendor/go/build/testdata/empty/dummy",
					NewTime:  nil,
					Extended: []string{
						"diff --git a/_vendor/go/build/testdata/empty/dummy b/_vendor/go/build/testdata/empty/dummy",
						"new file mode 100644",
						"index 0000000..e69de29",
					},
				},
				{
					OrigName: "/dev/null",
					OrigTime: nil,
					NewName:  "b/_vendor/go/build/testdata/multi/file.go",
					NewTime:  nil,
					Extended: []string{
						"diff --git a/_vendor/go/build/testdata/multi/file.go b/_vendor/go/build/testdata/multi/file.go",
						"new file mode 100644",
						"index 0000000..ee946eb",
					},
				},
			},
		},
		{
			filename: "sample_multi_file_deleted.diff",
			wantDiffs: []*FileDiff{
				{
					OrigName: "a/vendor/go/build/syslist_test.go",
					OrigTime: nil,
					NewName:  "/dev/null",
					NewTime:  nil,
					Extended: []string{
						"diff --git a/vendor/go/build/syslist_test.go b/vendor/go/build/syslist_test.go",
						"deleted file mode 100644",
						"index 3be2928..0000000",
					},
				},
				{
					OrigName: "a/vendor/go/build/testdata/empty/dummy",
					OrigTime: nil,
					NewName:  "/dev/null",
					NewTime:  nil,
					Extended: []string{
						"diff --git a/vendor/go/build/testdata/empty/dummy b/vendor/go/build/testdata/empty/dummy",
						"deleted file mode 100644",
						"index e69de29..0000000",
					},
				},
				{
					OrigName: "a/vendor/go/build/testdata/multi/file.go",
					OrigTime: nil,
					NewName:  "/dev/null",
					NewTime:  nil,
					Extended: []string{
						"diff --git a/vendor/go/build/testdata/multi/file.go b/vendor/go/build/testdata/multi/file.go",
						"deleted file mode 100644",
						"index ee946eb..0000000",
					},
				},
			},
		},
		{
			filename: "sample_multi_file_filemode_change.diff",
			wantDiffs: []*FileDiff{
				{
					OrigName: "a/sample.sh",
					NewName:  "b/sample.sh",
					Extended: []string{"diff --git a/sample.sh b/sample.sh", "old mode 100755", "new mode 100644"},
				},
				{
					OrigName: "a/sample2.sh",
					NewName:  "b/sample2.sh",
					Extended: []string{"diff --git a/sample2.sh b/sample2.sh", "old mode 100755", "new mode 100644"},
				},
			},
		},
		{
			filename: "sample_multi_file_rename.diff",
			wantDiffs: []*FileDiff{
				{
					OrigName: "a/README.md",
					OrigTime: nil,
					NewName:  "b/README.md",
					NewTime:  nil,
					Extended: []string{
						"diff --git a/README.md b/README.md",
						"index 5f3d591..96a24fa 100644",
					},
				},
				{
					OrigName: "a/docs/integrations/Email_Notifications.md",
					OrigTime: nil,
					NewName:  "b/docs/integrations/email-notifications.md",
					NewTime:  nil,
					Extended: []string{
						"diff --git a/docs/integrations/Email_Notifications.md b/docs/integrations/email-notifications.md",
						"similarity index 100%",
						"rename from docs/integrations/Email_Notifications.md",
						"rename to docs/integrations/email-notifications.md",
					},
				},
				{
					OrigName: "a/release_notes.md",
					OrigTime: nil,
					NewName:  "b/release_notes.md",
					NewTime:  nil,
					Extended: []string{
						"diff --git a/release_notes.md b/release_notes.md",
						"index f2ff13f..f060cb5 100644",
					},
				},
			},
		},
		{
			filename: "sample_multi_file_binary.diff",
			wantDiffs: []*FileDiff{
				{
					OrigName: "a/README.md",
					OrigTime: nil,
					NewName:  "b/README.md",
					NewTime:  nil,
					Extended: []string{
						"diff --git a/README.md b/README.md",
						"index 7b73e04..36cde13 100644",
					},
				},
				{
					OrigName: "a/data/Font.png",
					OrigTime: nil,
					NewName:  "b/data/Font.png",
					NewTime:  nil,
					Extended: []string{
						"diff --git a/data/Font.png b/data/Font.png",
						"index 17a971d..599f8dd 100644",
						"Binary files a/data/Font.png and b/data/Font.png differ",
					},
				},
				{
					OrigName: "a/main.go",
					OrigTime: nil,
					NewName:  "b/main.go",
					NewTime:  nil,
					Extended: []string{
						"diff --git a/main.go b/main.go",
						"index 1aced1e..98a982e 100644",
					},
				},
			},
		},
		{
			filename: "sample_binary_inline.diff",
			wantDiffs: []*FileDiff{
				{
					OrigName: "a/logo-old.png",
					OrigTime: nil,
					NewName:  "/dev/null",
					NewTime:  nil,
					Extended: []string{
						"diff --git a/logo-old.png b/logo-old.png",
						"deleted file mode 100644",
						"index d29d0e9757e0d9b854a8ed58f170bcb454cc1ae3..0000000000000000000000000000000000000000",
						"GIT binary patch",
						"literal 0",
						"HcmV?d00001",
						"",
						"literal 0",
						"HcmV?d00001",
						"",
					},
				},
				{
					OrigName: "a/logo-old.png",
					OrigTime: nil,
					NewName:  "b/logo-old.png",
					NewTime:  nil,
					Extended: []string{
						"diff --git a/logo-old.png b/logo-old.png",
						"index ff82e793467f2050d731d75b4968d2e6b9c5d33b..d29d0e9757e0d9b854a8ed58f170bcb454cc1ae3 100644",
						"GIT binary patch",
						"literal 0",
						"HcmV?d00001",
						"",
						"literal 0",
						"HcmV?d00001",
						"",
					},
				},
				{
					OrigName: "a/logo.png",
					OrigTime: nil,
					NewName:  "b/logo-old.png",
					NewTime:  nil,
					Extended: []string{
						"diff --git a/logo.png b/logo-old.png",
						"similarity index 100%",
						"rename from logo.png",
						"rename to logo-old.png",
					},
				},
				{
					OrigName: "/dev/null",
					OrigTime: nil,
					NewName:  "b/logo.png",
					NewTime:  nil,
					Extended: []string{
						"diff --git a/logo.png b/logo.png",
						"new file mode 100644",
						"index 0000000000000000000000000000000000000000..ff82e793467f2050d731d75b4968d2e6b9c5d33b",
						"GIT binary patch",
						"literal 0",
						"HcmV?d00001",
						"",
						"literal 0",
						"HcmV?d00001",
						"",
					},
				},
			},
		},
		{
			filename: "sample_multi_file_new_win.diff",
			wantDiffs: []*FileDiff{
				{
					OrigName: "/dev/null",
					OrigTime: nil,
					NewName:  "b/_vendor/go/build/syslist_test.go",
					NewTime:  nil,
					Extended: []string{
						"diff --git a/_vendor/go/build/syslist_test.go b/_vendor/go/build/syslist_test.go",
						"new file mode 100644",
						"index 0000000..3be2928",
					},
				},
				{
					OrigName: "/dev/null",
					OrigTime: nil,
					NewName:  "b/_vendor/go/build/testdata/empty/dummy",
					NewTime:  nil,
					Extended: []string{
						"diff --git a/_vendor/go/build/testdata/empty/dummy b/_vendor/go/build/testdata/empty/dummy",
						"new file mode 100644",
						"index 0000000..e69de29",
					},
				},
				{
					OrigName: "/dev/null",
					OrigTime: nil,
					NewName:  "b/_vendor/go/build/testdata/multi/file.go",
					NewTime:  nil,
					Extended: []string{
						"diff --git a/_vendor/go/build/testdata/multi/file.go b/_vendor/go/build/testdata/multi/file.go",
						"new file mode 100644",
						"index 0000000..ee946eb",
					},
				},
			},
		},
		{
			filename: "sample_contains_added_deleted_files.diff",
			wantDiffs: []*FileDiff{
				{
					OrigName: "source_a/file_1.txt",
					OrigTime: nil,
					NewName:  "source_b/file_1.txt",
					NewTime:  nil,
					Extended: []string{
						"diff -u source_a/file_1.txt  source_b/file_1.txt",
					},
				},
				{
					OrigName: "source_a/file_2.txt",
					OrigTime: nil,
					NewName:  "",
					NewTime:  nil,
					Extended: nil,
				},
				{
					OrigName: "source_b/file_3.txt",
					OrigTime: nil,
					NewName:  "",
					NewTime:  nil,
					Extended: nil,
				},
			},
		},
		{
			filename: "sample_contains_only_added_deleted_files.diff",
			wantDiffs: []*FileDiff{
				{
					OrigName: "source_a/file_1.txt",
					OrigTime: nil,
					NewName:  "",
					NewTime:  nil,
					Extended: nil,
				},
				{
					OrigName: "source_a/file_2.txt",
					OrigTime: nil,
					NewName:  "",
					NewTime:  nil,
					Extended: nil,
				},
				{
					OrigName: "source_b/file_3.txt",
					OrigTime: nil,
					NewName:  "",
					NewTime:  nil,
					Extended: nil,
				},
			},
		},
		{
			filename: "sample_onlyin_line_isnt_a_file_header.diff",
			wantDiffs: []*FileDiff{
				{
					OrigName: "source_a/file_1.txt",
					OrigTime: nil,
					NewName:  "source_b/file_1.txt",
					NewTime:  nil,
					Extended: []string{
						"diff -u source_a/file_1.txt  source_b/file_1.txt",
					},
				},
				{
					OrigName: "source_a/file_2.txt",
					OrigTime: nil,
					NewName:  "",
					NewTime:  nil,
					Extended: []string{
						"Only in universe!",
					},
				},
				{
					OrigName: "source_b/file_3.txt some unrelated stuff here.",
					OrigTime: nil,
					NewName:  "",
					NewTime:  nil,
					Extended: nil,
				},
				{
					OrigName: "source_b/file_3.txt",
					OrigTime: nil,
					NewName:  "",
					NewTime:  nil,
					Extended: nil,
				},
			},
		},
		{
			filename: "sample_onlyin_complex_filenames.diff",
			wantDiffs: []*FileDiff{
				{
					OrigName: "internal/trace/foo bar/bam",
					OrigTime: nil,
					NewName:  "",
					NewTime:  nil,
					Extended: nil,
				},
				{
					OrigName: "internal/trace/foo bar/bam: bar",
					OrigTime: nil,
					NewName:  "",
					NewTime:  nil,
					Extended: nil,
				},
				{
					OrigName: "internal/trace/hello/world: bazz",
					OrigTime: nil,
					NewName:  "",
					NewTime:  nil,
					Extended: nil,
				},
			},
		},
		{
			filename: "sample_multi_file_without_extended.diff",
			wantDiffs: []*FileDiff{
				{
					OrigName: "source_1_a/file_1.txt",
					OrigTime: nil,
					NewName:  "source_1_c/file_1.txt",
					NewTime:  nil,
					Extended: nil,
				},
				{
					OrigName: "source_1_a/file_2.txt",
					OrigTime: nil,
					NewName:  "source_1_c/file_2.txt",
					NewTime:  nil,
					Extended: nil,
				},
			},
		},
		{
			filename: "complicated_filenames.diff",
			wantDiffs: []*FileDiff{
				{
					OrigName: "/dev/null",
					NewName:  "b/new empty file with spaces",
					Extended: []string{
						"diff --git a/new empty file with spaces b/new empty file with spaces",
						"new file mode 100644",
						"index 0000000..e69de29",
					},
				},
				{
					OrigName: "/dev/null",
					NewName:  "b/new file with text",
					Extended: []string{
						"diff --git a/new file with text b/new file with text",
						"new file mode 100644",
						"index 0000000..c3ed4be",
					},
				},
				{
					OrigName: "a/existing file with spaces",
					NewName:  "b/new file with spaces",
					Extended: []string{
						"diff --git a/existing file with spaces b/new file with spaces",
						"similarity index 100%",
						"copy from existing file with spaces",
						"copy to new file with spaces",
					},
				},
				{
					OrigName: "a/existing file with spaces",
					NewName:  "b/new, complicated\nfilenøme",
					Extended: []string{
						`diff --git a/existing file with spaces "b/new, complicated\nfilen\303\270me"`,
						"similarity index 100%",
						"copy from existing file with spaces",
						`copy to "new, complicated\nfilen\303\270me"`,
					},
				},
				{
					OrigName: "a/existing file with spaces",
					NewName:  `b/new "complicated" filename`,
					Extended: []string{
						`diff --git a/existing file with spaces "b/new \"complicated\" filename"`,
						"similarity index 100%",
						"copy from existing file with spaces",
						`copy to "new \"complicated\" filename"`,
					},
				},
				{
					OrigName: `a/existing "complicated" filename`,
					NewName:  "b/new, simpler filename",
					Extended: []string{
						`diff --git "a/existing \"complicated\" filename" b/new, simpler filename`,
						"similarity index 100%",
						`copy from "existing \"complicated\" filename"`,
						"copy to new, simpler filename",
					},
				},
			},
		},
		{
			filename: "delete_empty_file.diff",
			wantDiffs: []*FileDiff{
				{
					OrigName: "Euler 0011/README.txt~",
					NewName:  "/dev/null",
					Extended: []string{
						"diff --git Euler 0011/README.txt~ Euler 0011/README.txt~",
						"deleted file mode 100644",
						"index e69de29bb2d1d6434b8b29ae775ad8c2e48c5391..0000000000000000000000000000000000000000",
					},
				},
				{
					OrigName: "Euler 0011/Euler0011.cpp",
					NewName:  "/dev/null",
					Extended: []string{
						"diff --git Euler 0011/Euler0011.cpp Euler 0011/Euler0011.cpp",
						"deleted file mode 100644",
						"index 6490416c8cb4bbf2afbafa66251a9eab983086d1..0000000000000000000000000000000000000000",
					},
				},
				{
					OrigName: "Euler 0011/README.txt~",
					NewName:  "/dev/null",
					Extended: []string{
						"diff --git Euler 0011/README.txt~ Euler 0011/README.txt~",
						"deleted file mode 100644",
						"index e69de29bb2d1d6434b8b29ae775ad8c2e48c5391..0000000000000000000000000000000000000000",
					},
				},
				{
					OrigName: "Euler 0011/README.txt",
					NewName:  "/dev/null",
					Extended: []string{
						"diff --git Euler 0011/README.txt Euler 0011/README.txt",
						"deleted file mode 100644",
						"index f8ea904baa27c54eb73cc02d5a555878b28672ff..0000000000000000000000000000000000000000",
					},
				},
				{
					OrigName: "Euler 0011/README.txt~",
					NewName:  "/dev/null",
					Extended: []string{
						"diff --git Euler 0011/README.txt~ Euler 0011/README.txt~",
						"deleted file mode 100644",
						"index e69de29bb2d1d6434b8b29ae775ad8c2e48c5391..0000000000000000000000000000000000000000",
					},
				},
			},
		},
	}
	for _, test := range tests {
		t.Run(test.filename, func(t *testing.T) {
			diffData, err := ioutil.ReadFile(filepath.Join("testdata", test.filename))
			if err != nil {
				t.Fatal(err)
			}
			diffs, err := ParseMultiFileDiff(diffData)
			if err != nil {
				t.Fatalf("%s: got ParseMultiFileDiff error %v", test.filename, err)
			}

			for i := range diffs {
				diffs[i].Hunks = nil // This test focuses on things other than hunks, so don't compare them.
			}
			if got, want := diffs, test.wantDiffs; !cmp.Equal(got, want) {
				t.Errorf("%s:\n\ngot - want:\n%s", test.filename, cmp.Diff(want, got))
			}
		})
	}
}

func TestParseFileDiffAndPrintFileDiff(t *testing.T) {
	tests := []struct {
		filename     string
		wantParseErr error
	}{
		{filename: "sample_file.diff"},
		{filename: "sample_file_no_timestamp.diff"},
		{filename: "sample_file_extended.diff"},
		{filename: "sample_file_extended_empty_new.diff"},
		{filename: "sample_file_extended_empty_new_binary.diff"},
		{filename: "sample_file_extended_empty_deleted.diff"},
		{filename: "sample_file_extended_empty_deleted_binary.diff"},
		{filename: "sample_file_extended_empty_rename.diff"},
		{filename: "sample_file_extended_empty_binary.diff"},
		{
			filename:     "empty.diff",
			wantParseErr: &ParseError{0, 0, ErrExtendedHeadersEOF},
		},
	}
	for _, test := range tests {
		diffData, err := ioutil.ReadFile(filepath.Join("testdata", test.filename))
		if err != nil {
			t.Fatal(err)
		}
		diff, err := ParseFileDiff(diffData)
		if !reflect.DeepEqual(err, test.wantParseErr) {
			t.Errorf("%s: got ParseFileDiff err %v, want %v", test.filename, err, test.wantParseErr)
			continue
		}
		if test.wantParseErr != nil {
			continue
		}

		printed, err := PrintFileDiff(diff)
		if err != nil {
			t.Errorf("%s: PrintFileDiff: %s", test.filename, err)
		}
		if !bytes.Equal(printed, diffData) {
			t.Errorf("%s: printed file diff != original file diff\n\n# PrintFileDiff output - Original:\n%s", test.filename, cmp.Diff(diffData, printed))
		}
	}
}

func TestParseMultiFileDiffAndPrintMultiFileDiff(t *testing.T) {
	tests := []struct {
		filename        string
		wantParseErr    error
		wantFileDiffs   int    // How many instances of diff.FileDiff are expected.
		wantOutFileName string // If non-empty, the name of the file containing the expected output.
	}{
		{filename: "sample_multi_file.diff", wantFileDiffs: 2},
		{filename: "sample_multi_file_single.diff", wantFileDiffs: 1},
		{filename: "sample_multi_file_single_apple_in.diff", wantFileDiffs: 1, wantOutFileName: "sample_multi_file_single_apple_out.diff"},
		{filename: "sample_multi_file_new.diff", wantFileDiffs: 3},
		{filename: "sample_multi_file_deleted.diff", wantFileDiffs: 3},
		{filename: "sample_multi_file_rename.diff", wantFileDiffs: 3},
		{filename: "sample_multi_file_binary.diff", wantFileDiffs: 3},
		{filename: "long_line_multi.diff", wantFileDiffs: 3},
		{filename: "empty.diff", wantFileDiffs: 0},
		{filename: "empty_multi.diff", wantFileDiffs: 2},
		{filename: "sample_contains_added_deleted_files.diff", wantFileDiffs: 3},
		{filename: "sample_contains_only_added_deleted_files.diff", wantFileDiffs: 3},
		{filename: "sample_onlyin_line_isnt_a_file_header.diff", wantFileDiffs: 4},
		{filename: "sample_onlyin_complex_filenames.diff", wantFileDiffs: 3},
		{filename: "sample_multi_file_minuses_pluses.diff", wantFileDiffs: 2},
		{filename: "sample_multi_file_without_extended.diff", wantFileDiffs: 2},
	}
	for _, test := range tests {
		diffData, err := ioutil.ReadFile(filepath.Join("testdata", test.filename))
		if err != nil {
			t.Fatal(err)
		}
		diffs, err := ParseMultiFileDiff(diffData)
		if err != test.wantParseErr {
			t.Errorf("%s: got ParseMultiFileDiff err %v, want %v", test.filename, err, test.wantParseErr)
			continue
		}
		if test.wantParseErr != nil {
			continue
		}

		if got, want := len(diffs), test.wantFileDiffs; got != want {
			t.Errorf("%s: got %v instances of diff.FileDiff, expected %v", test.filename, got, want)
		}

		printed, err := PrintMultiFileDiff(diffs)
		if err != nil {
			t.Errorf("%s: PrintMultiFileDiff: %s", test.filename, err)
		}
		if test.wantOutFileName != "" {
			diffData, err = ioutil.ReadFile(filepath.Join("testdata", test.wantOutFileName))
			if err != nil {
				t.Fatal(err)
			}
		}
		if !bytes.Equal(printed, diffData) {
			t.Errorf("%s: printed multi-file diff != original multi-file diff\n\n# PrintMultiFileDiff output - Original:\n%s", test.filename, cmp.Diff(diffData, printed))
		}
	}
}

func TestParseMultiFileDiffAndPrintMultiFileDiffIncludingTrailingContent(t *testing.T) {
	testInput, err := ioutil.ReadFile(filepath.Join("testdata", "sample_multi_file_trailing_content.diff"))
	if err != nil {
		t.Fatal(err)
	}
	expectedDiffs, err := ioutil.ReadFile(filepath.Join("testdata", "sample_multi_file_trailing_content_diffsonly.diff"))
	if err != nil {
		t.Fatal(err)
	}

	diffReader := NewMultiFileDiffReader(bytes.NewReader(testInput))
	var diffs []*FileDiff
	trailingContent := ""
	for {
		var fd *FileDiff
		var err error
		fd, trailingContent, err = diffReader.ReadFileWithTrailingContent()
		if fd != nil {
			diffs = append(diffs, fd)
		}
		if err == io.EOF {
			break
		}
		if err != nil {
			t.Error(err)
		}
	}

	if len(diffs) != 2 {
		t.Errorf("expected 2 diffs, got %d", len(diffs))
	}

	printed, err := PrintMultiFileDiff(diffs)
	if err != nil {
		t.Errorf("PrintMultiFileDiff: %s", err)
	}
	if !bytes.Equal(printed, expectedDiffs) {
		t.Errorf("printed multi-file diff != original multi-file diff\n\n# PrintMultiFileDiff output - Original:\n%s", cmp.Diff(expectedDiffs, printed))
	}

	expectedTrailingContent := "some trailing content"
	if trailingContent != expectedTrailingContent {
		t.Errorf("expected trailing content %s, got %s", expectedTrailingContent, trailingContent)
	}
}

func TestNoNewlineAtEnd(t *testing.T) {
	diffs := map[string]struct {
		diff              string
		trailingNewlineOK bool
	}{
		"orig": {
			diff: `@@ -1,1 +1,1 @@
-a
\ No newline at end of file
+b
`,
			trailingNewlineOK: true,
		},
		"new": {
			diff: `@@ -1,1 +1,1 @@
-a
+b
\ No newline at end of file
`,
		},
		"both": {
			diff: `@@ -1,1 +1,1 @@
-a
\ No newline at end of file
+b
\ No newline at end of file
`,
		},
	}

	for label, test := range diffs {
		hunks, err := ParseHunks([]byte(test.diff))
		if err != nil {
			t.Errorf("%s: ParseHunks: %s", label, err)
			continue
		}

		for _, hunk := range hunks {
			if body := string(hunk.Body); strings.Contains(body, "No newline") {
				t.Errorf("%s: after parse, hunk body contains 'No newline...' string\n\nbody is:\n%s", label, body)
			}
			if !test.trailingNewlineOK {
				if bytes.HasSuffix(hunk.Body, []byte{'\n'}) {
					t.Errorf("%s: after parse, hunk body ends with newline\n\nbody is:\n%s", label, hunk.Body)
				}
			}
			if dontWant := []byte("-a+b"); bytes.Contains(hunk.Body, dontWant) {
				t.Errorf("%s: hunk body contains %q\n\nbody is:\n%s", label, dontWant, hunk.Body)
			}

			printed, err := PrintHunks(hunks)
			if err != nil {
				t.Errorf("%s: PrintHunks: %s", label, err)
				continue
			}
			if printed := string(printed); printed != test.diff {
				t.Errorf("%s: printed diff hunks != original diff hunks\n\n# PrintHunks output - Original:\n%s", label, cmp.Diff(test.diff, printed))
			}
		}
	}
}

func TestFileDiff_Stat(t *testing.T) {
	tests := map[string]struct {
		hunks []*Hunk
		want  Stat
	}{
		"no change": {
			hunks: []*Hunk{
				{Body: []byte(`@@ -0,0 +0,0
 a
 b
`)},
			},
			want: Stat{},
		},
		"added/deleted": {
			hunks: []*Hunk{
				{Body: []byte(`@@ -0,0 +0,0
+a
 b
-c
 d
`)},
			},
			want: Stat{Added: 1, Deleted: 1},
		},
		"changed": {
			hunks: []*Hunk{
				{Body: []byte(`@@ -0,0 +0,0
+a
+b
-c
-d
 e
`)},
			},
			want: Stat{Added: 1, Changed: 1, Deleted: 1},
		},
		"many changes": {
			hunks: []*Hunk{
				{Body: []byte(`@@ -0,0 +0,0
+a
-b
+c
-d
 e
`)},
			},
			want: Stat{Added: 0, Changed: 2, Deleted: 0},
		},
	}
	for label, test := range tests {
		fdiff := &FileDiff{Hunks: test.hunks}
		stat := fdiff.Stat()
		if !cmp.Equal(stat, test.want) {
			t.Errorf("%s: got - want diff stat\n%s", label, cmp.Diff(test.want, stat))
			continue
		}
	}
}
```

## File: `diff/doc.go`
```go
// Package diff provides a parser for unified diffs.
package diff
```

## File: `diff/parse.go`
```go
package diff

import (
	"bufio"
	"bytes"
	"errors"
	"fmt"
	"io"
	"path/filepath"
	"strconv"
	"strings"
	"time"
)

// ParseMultiFileDiff parses a multi-file unified diff. It returns an error if
// parsing failed as a whole, but does its best to parse as many files in the
// case of per-file errors. If it cannot detect when the diff of the next file
// begins, the hunks are added to the FileDiff of the previous file.
func ParseMultiFileDiff(diff []byte) ([]*FileDiff, error) {
	return NewMultiFileDiffReader(bytes.NewReader(diff)).ReadAllFiles()
}

// NewMultiFileDiffReader returns a new MultiFileDiffReader that reads
// a multi-file unified diff from r.
func NewMultiFileDiffReader(r io.Reader) *MultiFileDiffReader {
	return &MultiFileDiffReader{reader: newLineReader(r)}
}

// MultiFileDiffReader reads a multi-file unified diff.
type MultiFileDiffReader struct {
	line   int
	offset int64
	reader *lineReader

	// TODO(sqs): line and offset tracking in multi-file diffs is broken; add tests and fix

	// nextFileFirstLine is a line that was read by a HunksReader that
	// was how it determined the hunk was complete. But to determine
	// that, it needed to read the first line of the next file. We
	// store nextFileFirstLine so we can "give the first line back" to
	// the next file.
	nextFileFirstLine []byte
}

// ReadFile reads the next file unified diff (including headers and
// all hunks) from r. If there are no more files in the diff, it
// returns error io.EOF.
func (r *MultiFileDiffReader) ReadFile() (*FileDiff, error) {
	fd, _, err := r.ReadFileWithTrailingContent()
	return fd, err
}

// ReadFileWithTrailingContent reads the next file unified diff (including
// headers and all hunks) from r, also returning any trailing content. If there
// are no more files in the diff, it returns error io.EOF.
func (r *MultiFileDiffReader) ReadFileWithTrailingContent() (*FileDiff, string, error) {
	fr := &FileDiffReader{
		line:           r.line,
		offset:         r.offset,
		reader:         r.reader,
		fileHeaderLine: r.nextFileFirstLine,
	}
	r.nextFileFirstLine = nil

	fd, err := fr.ReadAllHeaders()
	if err != nil {
		switch e := err.(type) {
		case *ParseError:
			if e.Err == ErrNoFileHeader || e.Err == ErrExtendedHeadersEOF {
				// Any non-diff content preceding a valid diff is included in the
				// extended headers of the following diff. In this way, mixed diff /
				// non-diff content can be parsed. Trailing non-diff content is
				// different: it doesn't make sense to return a FileDiff with only
				// extended headers populated. Instead, we return any trailing content
				// in case the caller needs it.
				trailing := ""
				if fd != nil {
					trailing = strings.Join(fd.Extended, "\n")
				}
				return nil, trailing, io.EOF
			}
			return nil, "", err

		case OverflowError:
			r.nextFileFirstLine = []byte(e)
			return fd, "", nil

		default:
			return nil, "", err
		}
	}

	// FileDiff is added/deleted file
	// No further collection of hunks needed
	if fd.NewName == "" {
		return fd, "", nil
	}

	// Before reading hunks, check to see if there are any. If there
	// aren't any, and there's another file after this file in the
	// diff, then the hunks reader will complain ErrNoHunkHeader. It's
	// not easy for us to tell from that error alone if that was
	// caused by the lack of any hunks, or a malformatted hunk, so we
	// need to perform the check here.
	hr := fr.HunksReader()
	line, err := r.reader.readLine()
	if err != nil && err != io.EOF {
		return fd, "", err
	}
	line = bytes.TrimSuffix(line, []byte{'\n'})
	if bytes.HasPrefix(line, hunkPrefix) {
		hr.nextHunkHeaderLine = line
		fd.Hunks, err = hr.ReadAllHunks()
		r.line = fr.line
		r.offset = fr.offset
		if err != nil {
			if e0, ok := err.(*ParseError); ok {
				if e, ok := e0.Err.(*ErrBadHunkLine); ok {
					// This just means we finished reading the hunks for the
					// current file. See the ErrBadHunkLine doc for more info.
					r.nextFileFirstLine = e.Line
					return fd, "", nil
				}
			}
			return nil, "", err
		}
	} else {
		// There weren't any hunks, so that line we peeked ahead at
		// actually belongs to the next file. Put it back.
		r.nextFileFirstLine = line
	}

	return fd, "", nil
}

// ReadAllFiles reads all file unified diffs (including headers and all
// hunks) remaining in r.
func (r *MultiFileDiffReader) ReadAllFiles() ([]*FileDiff, error) {
	var ds []*FileDiff
	for {
		d, err := r.ReadFile()
		if d != nil {
			ds = append(ds, d)
		}
		if err == io.EOF {
			return ds, nil
		}
		if err != nil {
			return nil, err
		}
	}
}

// ParseFileDiff parses a file unified diff.
func ParseFileDiff(diff []byte) (*FileDiff, error) {
	return NewFileDiffReader(bytes.NewReader(diff)).Read()
}

// NewFileDiffReader returns a new FileDiffReader that reads a file
// unified diff.
func NewFileDiffReader(r io.Reader) *FileDiffReader {
	return &FileDiffReader{reader: &lineReader{reader: bufio.NewReader(r)}}
}

// FileDiffReader reads a unified file diff.
type FileDiffReader struct {
	line   int
	offset int64
	reader *lineReader

	// fileHeaderLine is the first file header line, set by:
	//
	// (1) ReadExtendedHeaders if it encroaches on a file header line
	//     (which it must to detect when extended headers are done); or
	// (2) (*MultiFileDiffReader).ReadFile() if it encroaches on a
	//     file header line while reading the previous file's hunks (in a
	//     multi-file diff).
	fileHeaderLine []byte
}

// Read reads a file unified diff, including headers and hunks, from r.
func (r *FileDiffReader) Read() (*FileDiff, error) {
	fd, err := r.ReadAllHeaders()
	if err != nil {
		return nil, err
	}

	fd.Hunks, err = r.HunksReader().ReadAllHunks()
	if err != nil {
		return nil, err
	}

	return fd, nil
}

// ReadAllHeaders reads the file headers and extended headers (if any)
// from a file unified diff. It does not read hunks, and the returned
// FileDiff's Hunks field is nil. To read the hunks, call the
// (*FileDiffReader).HunksReader() method to get a HunksReader and
// read hunks from that.
func (r *FileDiffReader) ReadAllHeaders() (*FileDiff, error) {
	var err error
	fd := &FileDiff{}

	fd.Extended, err = r.ReadExtendedHeaders()
	if pe, ok := err.(*ParseError); ok && pe.Err == ErrExtendedHeadersEOF {
		wasEmpty := handleEmpty(fd)
		if wasEmpty {
			return fd, nil
		}
		return fd, err
	} else if _, ok := err.(OverflowError); ok {
		handleEmpty(fd)
		return fd, err
	} else if err != nil {
		return fd, err
	}

	var origTime, newTime *time.Time
	fd.OrigName, fd.NewName, origTime, newTime, err = r.ReadFileHeaders()
	if err != nil {
		return nil, err
	}
	if origTime != nil {
		fd.OrigTime = origTime
	}
	if newTime != nil {
		fd.NewTime = newTime
	}

	return fd, nil
}

// HunksReader returns a new HunksReader that reads hunks from r. The
// HunksReader's line and offset (used in error messages) is set to
// start where the file diff header ended (which means errors have the
// correct position information).
func (r *FileDiffReader) HunksReader() *HunksReader {
	return &HunksReader{
		line:   r.line,
		offset: r.offset,
		reader: r.reader,
	}
}

// ReadFileHeaders reads the unified file diff header (the lines that
// start with "---" and "+++" with the orig/new file names and
// timestamps). Or which starts with "Only in " with dir path and filename.
// "Only in" message is supported in POSIX locale: https://pubs.opengroup.org/onlinepubs/9699919799/utilities/diff.html#tag_20_34_10
func (r *FileDiffReader) ReadFileHeaders() (origName, newName string, origTimestamp, newTimestamp *time.Time, err error) {
	if r.fileHeaderLine != nil {
		if isOnlyMessage, source, filename := parseOnlyInMessage(r.fileHeaderLine); isOnlyMessage {
			return filepath.Join(string(source), string(filename)),
				"", nil, nil, nil
		}
	}
	origName, origTimestamp, err = r.readOneFileHeader([]byte("--- "))
	if err != nil {
		return "", "", nil, nil, err
	}

	newName, newTimestamp, err = r.readOneFileHeader([]byte("+++ "))
	if err != nil {
		return "", "", nil, nil, err
	}

	unquotedOrigName, err := strconv.Unquote(origName)
	if err == nil {
		origName = unquotedOrigName
	}
	unquotedNewName, err := strconv.Unquote(newName)
	if err == nil {
		newName = unquotedNewName
	}

	return origName, newName, origTimestamp, newTimestamp, nil
}

// readOneFileHeader reads one of the file headers (prefix should be
// either "+++ " or "--- ").
func (r *FileDiffReader) readOneFileHeader(prefix []byte) (filename string, timestamp *time.Time, err error) {
	var line []byte

	if r.fileHeaderLine == nil {
		var err error
		line, err = r.reader.readLine()
		if err == io.EOF {
			return "", nil, &ParseError{r.line, r.offset, ErrNoFileHeader}
		} else if err != nil {
			return "", nil, err
		}
	} else {
		line = r.fileHeaderLine
		r.fileHeaderLine = nil
	}

	if !bytes.HasPrefix(line, prefix) {
		return "", nil, &ParseError{r.line, r.offset, ErrBadFileHeader}
	}

	r.offset += int64(len(line))
	r.line++
	line = line[len(prefix):]

	trimmedLine := strings.TrimSpace(string(line)) // filenames that contain spaces may be terminated by a tab
	parts := strings.SplitN(trimmedLine, "\t", 2)
	filename = parts[0]
	if len(parts) == 2 {
		var ts time.Time
		// Timestamp is optional, but this header has it.
		ts, err = time.Parse(diffTimeParseLayout, parts[1])
		if err != nil {
			var err1 error
			ts, err1 = time.Parse(diffTimeParseWithoutTZLayout, parts[1])
			if err1 != nil {
				return "", nil, err
			}
			err = nil
		}
		timestamp = &ts
	}

	return filename, timestamp, err
}

// OverflowError is returned when we have overflowed into the start
// of the next file while reading extended headers.
type OverflowError string

func (e OverflowError) Error() string {
	return fmt.Sprintf("overflowed into next file: %s", string(e))
}

// ReadExtendedHeaders reads the extended header lines, if any, from a
// unified diff file (e.g., git's "diff --git a/foo.go b/foo.go", "new
// mode <mode>", "rename from <path>", etc.).
func (r *FileDiffReader) ReadExtendedHeaders() ([]string, error) {
	var xheaders []string
	firstLine := true
	for {
		var line []byte
		if r.fileHeaderLine == nil {
			var err error
			line, err = r.reader.readLine()
			if err == io.EOF {
				return xheaders, &ParseError{r.line, r.offset, ErrExtendedHeadersEOF}
			} else if err != nil {
				return xheaders, err
			}
		} else {
			line = r.fileHeaderLine
			r.fileHeaderLine = nil
		}

		if bytes.HasPrefix(line, []byte("diff --git ")) {
			if firstLine {
				firstLine = false
			} else {
				return xheaders, OverflowError(line)
			}
		}
		if bytes.HasPrefix(line, []byte("--- ")) {
			// We've reached the file header.
			r.fileHeaderLine = line // pass to readOneFileHeader (see fileHeaderLine field doc)
			return xheaders, nil
		}

		// Reached message that file is added/deleted
		if isOnlyInMessage, _, _ := parseOnlyInMessage(line); isOnlyInMessage {
			r.fileHeaderLine = line // pass to readOneFileHeader (see fileHeaderLine field doc)
			return xheaders, nil
		}

		r.line++
		r.offset += int64(len(line))
		xheaders = append(xheaders, string(line))
	}
}

// readQuotedFilename extracts a quoted filename from the beginning of a string,
// returning the unquoted filename and any remaining text after the filename.
func readQuotedFilename(text string) (value string, remainder string, err error) {
	if text == "" || text[0] != '"' {
		return "", "", fmt.Errorf(`string must start with a '"': %s`, text)
	}

	// The end quote is the first quote NOT preceeded by an uneven number of backslashes.
	numberOfBackslashes := 0
	for i, c := range text {
		if c == '"' && i > 0 && numberOfBackslashes%2 == 0 {
			value, err = strconv.Unquote(text[:i+1])
			remainder = text[i+1:]
			return
		} else if c == '\\' {
			numberOfBackslashes++
		} else {
			numberOfBackslashes = 0
		}
	}
	return "", "", fmt.Errorf(`end of string found while searching for '"': %s`, text)
}

// parseDiffGitArgs extracts the two filenames from a 'diff --git' line.
// Returns false on syntax error, true if syntax is valid. Even with a
// valid syntax, it may be impossible to extract filenames; if so, the
// function returns ("", "", true).
func parseDiffGitArgs(diffArgs string) (string, string, bool) {
	length := len(diffArgs)
	if length < 3 {
		return "", "", false
	}

	if diffArgs[0] != '"' && diffArgs[length-1] != '"' {
		// Both filenames are unquoted.
		firstSpace := strings.IndexByte(diffArgs, ' ')
		if firstSpace <= 0 || firstSpace == length-1 {
			return "", "", false
		}

		secondSpace := strings.IndexByte(diffArgs[firstSpace+1:], ' ')
		if secondSpace == -1 {
			if diffArgs[firstSpace+1] == '"' {
				// The second filename begins with '"', but doesn't end with one.
				return "", "", false
			}
			return diffArgs[:firstSpace], diffArgs[firstSpace+1:], true
		}

		// One or both filenames contain a space, but the names are
		// unquoted. Here, the 'diff --git' syntax is ambiguous, and
		// we have to obtain the filenames elsewhere (e.g. from the
		// hunk headers or extended headers). HOWEVER, if the file
		// is newly created and empty, there IS no other place to
		// find the filename. In this case, the two filenames are
		// identical (except for the leading 'a/' prefix), and we have
		// to handle that case here.
		first := diffArgs[:length/2]
		second := diffArgs[length/2+1:]

		// If the two strings could be equal, based on length, proceed.
		if length%2 == 1 {
			// If the name minus the a/ b/ prefixes is equal, proceed.
			if len(first) >= 3 && first[1] == '/' && first[1:] == second[1:] {
				return first, second, true
			}
			// If the names don't have the a/ and b/ prefixes and they're equal, proceed.
			if !(first[:2] == "a/" && second[:2] == "b/") && first == second {
				return first, second, true
			}
		}

		// The syntax is (unfortunately) valid, but we could not extract
		// the filenames.
		return "", "", true
	}

	if diffArgs[0] == '"' {
		first, remainder, err := readQuotedFilename(diffArgs)
		if err != nil || len(remainder) < 2 || remainder[0] != ' ' {
			return "", "", false
		}
		if remainder[1] == '"' {
			second, remainder, err := readQuotedFilename(remainder[1:])
			if remainder != "" || err != nil {
				return "", "", false
			}
			return first, second, true
		}
		return first, remainder[1:], true
	}

	// In this case, second argument MUST be quoted (or it's a syntax error)
	i := strings.IndexByte(diffArgs, '"')
	if i == -1 || i+2 >= length || diffArgs[i-1] != ' ' {
		return "", "", false
	}

	second, remainder, err := readQuotedFilename(diffArgs[i:])
	if remainder != "" || err != nil {
		return "", "", false
	}
	return diffArgs[:i-1], second, true
}

// handleEmpty detects when FileDiff was an empty diff and will not have any hunks
// that follow. It updates fd fields from the parsed extended headers.
func handleEmpty(fd *FileDiff) (wasEmpty bool) {
	lineCount := len(fd.Extended)
	if lineCount > 0 && !strings.HasPrefix(fd.Extended[0], "diff --git ") {
		return false
	}

	lineHasPrefix := func(idx int, prefix string) bool {
		return strings.HasPrefix(fd.Extended[idx], prefix)
	}

	linesHavePrefixes := func(idx1 int, prefix1 string, idx2 int, prefix2 string) bool {
		return lineHasPrefix(idx1, prefix1) && lineHasPrefix(idx2, prefix2)
	}

	isCopy := (lineCount == 4 && linesHavePrefixes(2, "copy from ", 3, "copy to ")) ||
		(lineCount == 6 && linesHavePrefixes(2, "copy from ", 3, "copy to ") && lineHasPrefix(5, "Binary files ")) ||
		(lineCount == 6 && linesHavePrefixes(1, "old mode ", 2, "new mode ") && linesHavePrefixes(4, "copy from ", 5, "copy to "))

	isRename := (lineCount == 4 && linesHavePrefixes(2, "rename from ", 3, "rename to ")) ||
		(lineCount == 5 && linesHavePrefixes(2, "rename from ", 3, "rename to ") && lineHasPrefix(4, "Binary files ")) ||
		(lineCount == 6 && linesHavePrefixes(2, "rename from ", 3, "rename to ") && lineHasPrefix(5, "Binary files ")) ||
		(lineCount == 6 && linesHavePrefixes(1, "old mode ", 2, "new mode ") && linesHavePrefixes(4, "rename from ", 5, "rename to "))

	isDeletedFile := (lineCount == 3 || lineCount == 4 && lineHasPrefix(3, "Binary files ") || lineCount > 4 && lineHasPrefix(3, "GIT binary patch")) &&
		lineHasPrefix(1, "deleted file mode ")

	isNewFile := (lineCount == 3 || lineCount == 4 && lineHasPrefix(3, "Binary files ") || lineCount > 4 && lineHasPrefix(3, "GIT binary patch")) &&
		lineHasPrefix(1, "new file mode ")

	isModeChange := lineCount == 3 && linesHavePrefixes(1, "old mode ", 2, "new mode ")

	isBinaryPatch := lineCount == 3 && lineHasPrefix(2, "Binary files ") || lineCount > 3 && lineHasPrefix(2, "GIT binary patch")

	if !isModeChange && !isCopy && !isRename && !isBinaryPatch && !isNewFile && !isDeletedFile {
		return false
	}

	var success bool
	fd.OrigName, fd.NewName, success = parseDiffGitArgs(fd.Extended[0][len("diff --git "):])
	if isNewFile {
		fd.OrigName = "/dev/null"
	}

	if isDeletedFile {
		fd.NewName = "/dev/null"
	}

	// For ambiguous 'diff --git' lines, try to reconstruct filenames using extended headers.
	if success && (isCopy || isRename) && fd.OrigName == "" && fd.NewName == "" {
		diffArgs := fd.Extended[0][len("diff --git "):]

		tryReconstruct := func(header string, prefix string, whichFile int, result *string) {
			if !strings.HasPrefix(header, prefix) {
				return
			}
			rawFilename := header[len(prefix):]

			// extract the filename prefix (e.g. "a/") from the 'diff --git' line.
			var prefixLetterIndex int
			if whichFile == 1 {
				prefixLetterIndex = 0
			} else if whichFile == 2 {
				prefixLetterIndex = len(diffArgs) - len(rawFilename) - 2
			}
			if prefixLetterIndex < 0 || diffArgs[prefixLetterIndex+1] != '/' {
				return
			}

			*result = diffArgs[prefixLetterIndex:prefixLetterIndex+2] + rawFilename
		}

		for _, header := range fd.Extended {
			tryReconstruct(header, "copy from ", 1, &fd.OrigName)
			tryReconstruct(header, "copy to ", 2, &fd.NewName)
			tryReconstruct(header, "rename from ", 1, &fd.OrigName)
			tryReconstruct(header, "rename to ", 2, &fd.NewName)
		}
	}
	return success
}

var (
	// ErrNoFileHeader is when a file unified diff has no file header
	// (i.e., the lines that begin with "---" and "+++").
	ErrNoFileHeader = errors.New("expected file header, got EOF")

	// ErrBadFileHeader is when a file unified diff has a malformed
	// file header (i.e., the lines that begin with "---" and "+++").
	ErrBadFileHeader = errors.New("bad file header")

	// ErrExtendedHeadersEOF is when an EOF was encountered while reading extended file headers, which means that there were no ---/+++ headers encountered before hunks (if any) began.
	ErrExtendedHeadersEOF = errors.New("expected file header while reading extended headers, got EOF")

	// ErrBadOnlyInMessage is when a file have a malformed `only in` message
	// Should be in format `Only in {source}: {filename}`
	ErrBadOnlyInMessage = errors.New("bad 'only in' message")
)

// ParseHunks parses hunks from a unified diff. The diff must consist
// only of hunks and not include a file header; if it has a file
// header, use ParseFileDiff.
func ParseHunks(diff []byte) ([]*Hunk, error) {
	r := NewHunksReader(bytes.NewReader(diff))
	hunks, err := r.ReadAllHunks()
	if err != nil {
		return nil, err
	}
	return hunks, nil
}

// NewHunksReader returns a new HunksReader that reads unified diff hunks
// from r.
func NewHunksReader(r io.Reader) *HunksReader {
	return &HunksReader{reader: &lineReader{reader: bufio.NewReader(r)}}
}

// A HunksReader reads hunks from a unified diff.
type HunksReader struct {
	line   int
	offset int64
	hunk   *Hunk
	reader *lineReader

	nextHunkHeaderLine []byte
}

// ReadHunk reads one hunk from r. If there are no more hunks, it
// returns error io.EOF.
func (r *HunksReader) ReadHunk() (*Hunk, error) {
	r.hunk = nil
	lastLineFromOrig := true
	var line []byte
	var err error
	for {
		if r.nextHunkHeaderLine != nil {
			// Use stored hunk header line that was scanned in at the
			// completion of the previous hunk's ReadHunk.
			line = r.nextHunkHeaderLine
			r.nextHunkHeaderLine = nil
		} else {
			line, err = r.reader.readLine()
			if err != nil {
				if err == io.EOF && r.hunk != nil {
					return r.hunk, nil
				}
				return nil, err
			}
		}

		// Record position.
		r.line++
		r.offset += int64(len(line))

		if r.hunk == nil {
			// Check for presence of hunk header.
			if !bytes.HasPrefix(line, hunkPrefix) {
				return nil, &ParseError{r.line, r.offset, ErrNoHunkHeader}
			}

			// Parse hunk header.
			r.hunk = &Hunk{}
			items := []interface{}{
				&r.hunk.OrigStartLine, &r.hunk.OrigLines,
				&r.hunk.NewStartLine, &r.hunk.NewLines,
			}
			header, section, err := normalizeHeader(string(line))
			if err != nil {
				return nil, &ParseError{r.line, r.offset, err}
			}
			n, err := fmt.Sscanf(header, hunkHeader, items...)
			if err != nil {
				return nil, err
			}
			if n < len(items) {
				return nil, &ParseError{r.line, r.offset, &ErrBadHunkHeader{header: string(line)}}
			}

			r.hunk.Section = section
		} else {
			// Read hunk body line.

			// If the line starts with `---` and the next one with `+++` we're
			// looking at a non-extended file header and need to abort.
			if bytes.HasPrefix(line, []byte("---")) {
				ok, err := r.reader.nextLineStartsWith("+++")
				if err != nil {
					return r.hunk, err
				}
				if ok {
					ok2, _ := r.reader.nextNextLineStartsWith(string(hunkPrefix))
					if ok2 {
						return r.hunk, &ParseError{r.line, r.offset, &ErrBadHunkLine{Line: line}}
					}
				}
			}

			// If the line starts with the hunk prefix, this hunk is complete.
			if bytes.HasPrefix(line, hunkPrefix) {
				// But we've already read in the next hunk's
				// header, so we need to be sure that the next call to
				// ReadHunk starts with that header.
				r.nextHunkHeaderLine = line

				// Rewind position.
				r.line--
				r.offset -= int64(len(line))

				return r.hunk, nil
			}

			if len(line) >= 1 && !linePrefix(line[0]) {
				// Bad hunk header line. If we're reading a multi-file
				// diff, this may be the end of the current
				// file. Return a "rich" error that lets our caller
				// handle that case.
				return r.hunk, &ParseError{r.line, r.offset, &ErrBadHunkLine{Line: line}}
			}
			if bytes.Equal(line, []byte(noNewlineMessage)) {
				if lastLineFromOrig {
					// Retain the newline in the body (otherwise the
					// diff line would be like "-a+b", where "+b" is
					// the the next line of the new file, which is not
					// validly formatted) but record that the orig had
					// no newline.
					r.hunk.OrigNoNewlineAt = int32(len(r.hunk.Body))
				} else {
					// Remove previous line's newline.
					if len(r.hunk.Body) != 0 {
						r.hunk.Body = r.hunk.Body[:len(r.hunk.Body)-1]
					}
				}
				continue
			}

			if len(line) > 0 {
				lastLineFromOrig = line[0] == '-'
			}

			r.hunk.Body = append(r.hunk.Body, line...)
			r.hunk.Body = append(r.hunk.Body, '\n')
		}
	}
}

const noNewlineMessage = `\ No newline at end of file`

// linePrefixes is the set of all characters a valid line in a diff
// hunk can start with. '\' can appear in diffs when no newline is
// present at the end of a file.
// See: 'http://www.gnu.org/software/diffutils/manual/diffutils.html#Incomplete-Lines'
var linePrefixes = []byte{' ', '-', '+', '\\'}

// linePrefix returns true if 'c' is in 'linePrefixes'.
func linePrefix(c byte) bool {
	for _, p := range linePrefixes {
		if p == c {
			return true
		}
	}
	return false
}

// normalizeHeader takes a header of the form:
// "@@ -linestart[,chunksize] +linestart[,chunksize] @@ section"
// and returns two strings, with the first in the form:
// "@@ -linestart,chunksize +linestart,chunksize @@".
// where linestart and chunksize are both integers. The second is the
// optional section header. chunksize may be omitted from the header
// if its value is 1. normalizeHeader returns an error if the header
// is not in the correct format.
func normalizeHeader(header string) (string, string, error) {
	// Split the header into five parts: the first '@@', the two
	// ranges, the last '@@', and the optional section.
	pieces := strings.SplitN(header, " ", 5)
	if len(pieces) < 4 {
		return "", "", &ErrBadHunkHeader{header: header}
	}

	if pieces[0] != "@@" {
		return "", "", &ErrBadHunkHeader{header: header}
	}
	for i := 1; i < 3; i++ {
		if !strings.ContainsRune(pieces[i], ',') {
			pieces[i] = pieces[i] + ",1"
		}
	}
	if pieces[3] != "@@" {
		return "", "", &ErrBadHunkHeader{header: header}
	}

	var section string
	if len(pieces) == 5 {
		section = pieces[4]
	}
	return strings.Join(pieces, " "), strings.TrimSpace(section), nil
}

// ReadAllHunks reads all remaining hunks from r. A successful call
// returns err == nil, not err == EOF. Because ReadAllHunks is defined
// to read until EOF, it does not treat end of file as an error to be
// reported.
func (r *HunksReader) ReadAllHunks() ([]*Hunk, error) {
	var hunks []*Hunk
	linesRead := int32(0)
	for {
		hunk, err := r.ReadHunk()
		if err == io.EOF {
			return hunks, nil
		}
		if hunk != nil {
			linesRead++ // account for the hunk header line
			hunk.StartPosition = linesRead
			hunks = append(hunks, hunk)
			linesRead += int32(bytes.Count(hunk.Body, []byte{'\n'}))
		}
		if err != nil {
			return hunks, err
		}
	}
}

// parseOnlyInMessage checks if line is a "Only in {source}: {filename}" and returns source and filename
func parseOnlyInMessage(line []byte) (bool, []byte, []byte) {
	if !bytes.HasPrefix(line, onlyInMessagePrefix) {
		return false, nil, nil
	}
	line = line[len(onlyInMessagePrefix):]
	idx := bytes.Index(line, []byte(": "))
	if idx < 0 {
		return false, nil, nil
	}
	return true, line[:idx], line[idx+2:]
}

// A ParseError is a description of a unified diff syntax error.
type ParseError struct {
	Line   int   // Line where the error occurred
	Offset int64 // Offset where the error occurred
	Err    error // The actual error
}

func (e *ParseError) Error() string {
	return fmt.Sprintf("line %d, char %d: %s", e.Line, e.Offset, e.Err)
}

// ErrNoHunkHeader indicates that a unified diff hunk header was
// expected but not found during parsing.
var ErrNoHunkHeader = errors.New("no hunk header")

// ErrBadHunkHeader indicates that a malformed unified diff hunk
// header was encountered during parsing.
type ErrBadHunkHeader struct {
	header string
}

func (e *ErrBadHunkHeader) Error() string {
	if e.header == "" {
		return "bad hunk header"
	}
	return "bad hunk header: " + e.header
}

// ErrBadHunkLine is when a line not beginning with ' ', '-', '+', or
// '\' is encountered while reading a hunk. In the context of reading
// a single hunk or file, it is an unexpected error. In a multi-file
// diff, however, it indicates that the current file's diff is
// complete (and remaining diff data will describe another file
// unified diff).
type ErrBadHunkLine struct {
	Line []byte
}

func (e *ErrBadHunkLine) Error() string {
	m := "bad hunk line (does not start with ' ', '-', '+', or '\\')"
	if len(e.Line) == 0 {
		return m
	}
	return m + ": " + string(e.Line)
}
```

## File: `diff/parse_test.go`
```go
package diff

import (
	"testing"
)

func TestReadQuotedFilename_Success(t *testing.T) {
	tests := []struct {
		input, value, remainder string
	}{
		{input: `""`, value: "", remainder: ""},
		{input: `"aaa"`, value: "aaa", remainder: ""},
		{input: `"aaa" bbb`, value: "aaa", remainder: " bbb"},
		{input: `"aaa" "bbb" ccc`, value: "aaa", remainder: ` "bbb" ccc`},
		{input: `"\""`, value: "\"", remainder: ""},
		{input: `"uh \"oh\""`, value: "uh \"oh\"", remainder: ""},
		{input: `"uh \\"oh\\""`, value: "uh \\", remainder: `oh\\""`},
		{input: `"uh \\\"oh\\\""`, value: "uh \\\"oh\\\"", remainder: ""},
	}
	for _, tc := range tests {
		value, remainder, err := readQuotedFilename(tc.input)
		if err != nil {
			t.Errorf("readQuotedFilename(`%s`): expected success, got '%s'", tc.input, err)
		} else if value != tc.value || remainder != tc.remainder {
			t.Errorf("readQuotedFilename(`%s`): expected `%s` and `%s`, got `%s` and `%s`", tc.input, tc.value, tc.remainder, value, remainder)
		}
	}
}

func TestReadQuotedFilename_Error(t *testing.T) {
	tests := []string{
		// Doesn't start with a quote
		``,
		`foo`,
		` "foo"`,
		// Missing end quote
		`"`,
		`"\"`,
		// "\x" is not a valid Go string literal escape
		`"\xxx"`,
	}
	for _, input := range tests {
		_, _, err := readQuotedFilename(input)
		if err == nil {
			t.Errorf("readQuotedFilename(`%s`): expected error", input)
		}
	}
}

func TestParseDiffGitArgs_Success(t *testing.T) {
	tests := []struct {
		input, first, second string
	}{
		{input: `aaa bbb`, first: "aaa", second: "bbb"},
		{input: `"aaa" bbb`, first: "aaa", second: "bbb"},
		{input: `aaa "bbb"`, first: "aaa", second: "bbb"},
		{input: `"aaa" "bbb"`, first: "aaa", second: "bbb"},
		{input: `1/a 2/z`, first: "1/a", second: "2/z"},
		{input: `1/hello world 2/hello world`, first: "1/hello world", second: "2/hello world"},
		{input: `"new\nline" and spaces`, first: "new\nline", second: "and spaces"},
		{input: `a/existing file with spaces "b/new, complicated\nfilen\303\270me"`, first: "a/existing file with spaces", second: "b/new, complicated\nfilen\303\270me"},
	}
	for _, tc := range tests {
		first, second, success := parseDiffGitArgs(tc.input)
		if !success {
			t.Errorf("`diff --git %s`: expected success", tc.input)
		} else if first != tc.first || second != tc.second {
			t.Errorf("`diff --git %s`: expected `%s` and `%s`, got `%s` and `%s`", tc.input, tc.first, tc.second, first, second)
		}
	}
}

func TestParseDiffGitArgs_Unsuccessful(t *testing.T) {
	tests := []string{
		``,
		`hello_world.txt`,
		`word `,
		` word`,
		`"a/bad_quoting b/bad_quoting`,
		`a/bad_quoting "b/bad_quoting`,
		`a/bad_quoting b/bad_quoting"`,
		`"a/bad_quoting b/bad_quoting"`,
		`"a/bad""b/bad"`,
		`"a/bad" "b/bad" "c/bad"`,
		`a/bad "b/bad" "c/bad"`,
	}
	for _, input := range tests {
		first, second, success := parseDiffGitArgs(input)
		if success {
			t.Errorf("`diff --git %s`: expected unsuccessful; got `%s` and `%s`", input, first, second)
		}
	}
}
```

## File: `diff/print.go`
```go
package diff

import (
	"bytes"
	"fmt"
	"io"
	"path/filepath"
	"time"
)

// PrintMultiFileDiff prints a multi-file diff in unified diff format.
func PrintMultiFileDiff(ds []*FileDiff) ([]byte, error) {
	var buf bytes.Buffer
	for _, d := range ds {
		diff, err := PrintFileDiff(d)
		if err != nil {
			return nil, err
		}
		if _, err := buf.Write(diff); err != nil {
			return nil, err
		}
	}
	return buf.Bytes(), nil
}

// PrintFileDiff prints a FileDiff in unified diff format.
//
// TODO(sqs): handle escaping whitespace/etc. chars in filenames
func PrintFileDiff(d *FileDiff) ([]byte, error) {
	var buf bytes.Buffer

	for _, xheader := range d.Extended {
		if _, err := fmt.Fprintln(&buf, xheader); err != nil {
			return nil, err
		}
	}

	// FileDiff is added/deleted file
	// No further hunks printing needed
	if d.NewName == "" {
		_, err := fmt.Fprintf(&buf, onlyInMessage, filepath.Dir(d.OrigName), filepath.Base(d.OrigName))
		if err != nil {
			return nil, err
		}
		return buf.Bytes(), nil
	}

	if d.Hunks == nil {
		return buf.Bytes(), nil
	}

	if err := printFileHeader(&buf, "--- ", d.OrigName, d.OrigTime); err != nil {
		return nil, err
	}
	if err := printFileHeader(&buf, "+++ ", d.NewName, d.NewTime); err != nil {
		return nil, err
	}

	ph, err := PrintHunks(d.Hunks)
	if err != nil {
		return nil, err
	}

	if _, err := buf.Write(ph); err != nil {
		return nil, err
	}
	return buf.Bytes(), nil
}

func printFileHeader(w io.Writer, prefix string, filename string, timestamp *time.Time) error {
	if _, err := fmt.Fprint(w, prefix, filename); err != nil {
		return err
	}
	if timestamp != nil {
		if _, err := fmt.Fprint(w, "\t", timestamp.Format(diffTimeFormatLayout)); err != nil {
			return err
		}
	}
	if _, err := fmt.Fprintln(w); err != nil {
		return err
	}
	return nil
}

// PrintHunks prints diff hunks in unified diff format.
func PrintHunks(hunks []*Hunk) ([]byte, error) {
	var buf bytes.Buffer
	for _, hunk := range hunks {
		_, err := fmt.Fprintf(&buf,
			"@@ -%d,%d +%d,%d @@", hunk.OrigStartLine, hunk.OrigLines, hunk.NewStartLine, hunk.NewLines,
		)
		if err != nil {
			return nil, err
		}
		if hunk.Section != "" {
			_, err := fmt.Fprint(&buf, " ", hunk.Section)
			if err != nil {
				return nil, err
			}
		}
		if _, err := fmt.Fprintln(&buf); err != nil {
			return nil, err
		}

		if hunk.OrigNoNewlineAt == 0 {
			if _, err := buf.Write(hunk.Body); err != nil {
				return nil, err
			}
		} else {
			if _, err := buf.Write(hunk.Body[:hunk.OrigNoNewlineAt]); err != nil {
				return nil, err
			}
			if err := printNoNewlineMessage(&buf); err != nil {
				return nil, err
			}
			if _, err := buf.Write(hunk.Body[hunk.OrigNoNewlineAt:]); err != nil {
				return nil, err
			}
		}

		if !bytes.HasSuffix(hunk.Body, []byte{'\n'}) {
			if _, err := fmt.Fprintln(&buf); err != nil {
				return nil, err
			}
			if err := printNoNewlineMessage(&buf); err != nil {
				return nil, err
			}
		}
	}
	return buf.Bytes(), nil
}

func printNoNewlineMessage(w io.Writer) error {
	if _, err := w.Write([]byte(noNewlineMessage)); err != nil {
		return err
	}
	if _, err := fmt.Fprintln(w); err != nil {
		return err
	}
	return nil
}
```

## File: `diff/reader_util.go`
```go
package diff

import (
	"bufio"
	"bytes"
	"errors"
	"io"
)

var ErrLineReaderUninitialized = errors.New("line reader not initialized")

func newLineReader(r io.Reader) *lineReader {
	return &lineReader{reader: bufio.NewReader(r)}
}

// lineReader is a wrapper around a bufio.Reader that caches the next line to
// provide lookahead functionality for the next two lines.
type lineReader struct {
	reader *bufio.Reader

	cachedNextLine    []byte
	cachedNextLineErr error
}

// readLine returns the next unconsumed line and advances the internal cache of
// the lineReader.
func (l *lineReader) readLine() ([]byte, error) {
	if l.cachedNextLine == nil && l.cachedNextLineErr == nil {
		l.cachedNextLine, l.cachedNextLineErr = readLine(l.reader)
	}

	if l.cachedNextLineErr != nil {
		return nil, l.cachedNextLineErr
	}

	next := l.cachedNextLine

	l.cachedNextLine, l.cachedNextLineErr = readLine(l.reader)

	return next, nil
}

// nextLineStartsWith looks at the line that would be returned by the next call
// to readLine to check whether it has the given prefix.
//
// io.EOF and bufio.ErrBufferFull errors are ignored so that the function can
// be used when at the end of the file.
func (l *lineReader) nextLineStartsWith(prefix string) (bool, error) {
	if l.cachedNextLine == nil && l.cachedNextLineErr == nil {
		l.cachedNextLine, l.cachedNextLineErr = readLine(l.reader)
	}

	return l.lineHasPrefix(l.cachedNextLine, prefix, l.cachedNextLineErr)
}

// nextNextLineStartsWith checks the prefix of the line *after* the line that
// would be returned by the next readLine.
//
// io.EOF and bufio.ErrBufferFull errors are ignored so that the function can
// be used when at the end of the file.
//
// The lineReader MUST be initialized by calling readLine at least once before
// calling nextLineStartsWith. Otherwise ErrLineReaderUninitialized will be
// returned.
func (l *lineReader) nextNextLineStartsWith(prefix string) (bool, error) {
	if l.cachedNextLine == nil && l.cachedNextLineErr == nil {
		l.cachedNextLine, l.cachedNextLineErr = readLine(l.reader)
	}

	next, err := l.reader.Peek(len(prefix))
	return l.lineHasPrefix(next, prefix, err)
}

// lineHasPrefix checks whether the given line has the given prefix with
// bytes.HasPrefix.
//
// The readErr should be the error that was returned when the line was read.
// lineHasPrefix checks the error to adjust its return value to, e.g., return
// false and ignore the error when readErr is io.EOF.
func (l *lineReader) lineHasPrefix(line []byte, prefix string, readErr error) (bool, error) {
	if readErr != nil {
		if readErr == io.EOF || readErr == bufio.ErrBufferFull {
			return false, nil
		}
		return false, readErr
	}

	return bytes.HasPrefix(line, []byte(prefix)), nil
}

// readLine is a helper that mimics the functionality of calling bufio.Scanner.Scan() and
// bufio.Scanner.Bytes(), but without the token size limitation. It will read and return
// the next line in the Reader with the trailing newline stripped. It will return an
// io.EOF error when there is nothing left to read (at the start of the function call). It
// will return any other errors it receives from the underlying call to ReadBytes.
func readLine(r *bufio.Reader) ([]byte, error) {
	line_, err := r.ReadBytes('\n')
	if err == io.EOF {
		if len(line_) == 0 {
			return nil, io.EOF
		}

		// ReadBytes returned io.EOF, because it didn't find another newline, but there is
		// still the remainder of the file to return as a line.
		line := line_
		return line, nil
	} else if err != nil {
		return nil, err
	}
	line := line_[0 : len(line_)-1]
	return dropCR(line), nil
}

// dropCR drops a terminal \r from the data.
func dropCR(data []byte) []byte {
	if len(data) > 0 && data[len(data)-1] == '\r' {
		return data[0 : len(data)-1]
	}
	return data
}
```

## File: `diff/reader_util_test.go`
```go
package diff

import (
	"bufio"
	"io"
	"reflect"
	"strings"
	"testing"
)

func TestReadLine(t *testing.T) {
	tests := []struct {
		name  string
		input string
		want  []string
	}{
		{
			name:  "empty",
			input: "",
			want:  []string{},
		},
		{
			name:  "single_line",
			input: "@@ -0,0 +1,62 @@",
			want:  []string{"@@ -0,0 +1,62 @@"},
		},
		{
			name:  "single_lf_terminated_line",
			input: "@@ -0,0 +1,62 @@\n",
			want:  []string{"@@ -0,0 +1,62 @@"},
		},
		{
			name:  "single_crlf_terminated_line",
			input: "@@ -0,0 +1,62 @@\r\n",
			want:  []string{"@@ -0,0 +1,62 @@"},
		},
		{
			name: "multi_line",
			input: `diff --git a/test.go b/test.go
new file mode 100644
index 0000000..3be2928`,
			want: []string{
				"diff --git a/test.go b/test.go",
				"new file mode 100644",
				"index 0000000..3be2928",
			},
		},
	}
	for _, test := range tests {
		t.Run(test.name, func(t *testing.T) {
			in := bufio.NewReader(strings.NewReader(test.input))
			out := []string{}
			for {
				l, err := readLine(in)
				if err == io.EOF {
					break
				}
				if err != nil {
					t.Fatal(err)
				}
				out = append(out, string(l))
			}
			if !reflect.DeepEqual(test.want, out) {
				t.Errorf("read lines not equal: want %v, got %v", test.want, out)
			}
		})
	}
}

func TestLineReader_ReadLine(t *testing.T) {
	input := `diff --git a/test.go b/test.go
new file mode 100644
index 0000000..3be2928


`

	in := newLineReader(strings.NewReader(input))
	out := []string{}
	for i := 0; i < 4; i++ {
		l, err := in.readLine()
		if err != nil {
			t.Fatal(err)
		}
		out = append(out, string(l))
	}

	wantOut := strings.Split(input, "\n")[0:4]
	if !reflect.DeepEqual(wantOut, out) {
		t.Errorf("read lines not equal: want %v, got %v", wantOut, out)
	}

	_, err := in.readLine()
	if err != nil {
		t.Fatal(err)
	}
	if in.cachedNextLineErr != io.EOF {
		t.Fatalf("lineReader has wrong cachedNextLineErr: %s", in.cachedNextLineErr)
	}
	_, err = in.readLine()
	if err != io.EOF {
		t.Fatalf("readLine did not return io.EOF: %s", err)
	}
}

func TestLineReader_NextLine(t *testing.T) {
	input := `aaa rest of line
bbbrest of line
ccc rest of line`

	in := newLineReader(strings.NewReader(input))

	type assertion struct {
		prefix string
		want   bool
	}

	testsPerReadLine := []struct {
		nextLine        []assertion
		nextNextLine    []assertion
		wantReadLineErr error
	}{
		{
			nextLine: []assertion{
				{prefix: "a", want: true},
				{prefix: "aa", want: true},
				{prefix: "aaa", want: true},
				{prefix: "bbb", want: false},
				{prefix: "ccc", want: false},
			},
			nextNextLine: []assertion{
				{prefix: "aaa", want: false},
				{prefix: "bbb", want: true},
				{prefix: "ccc", want: false},
			},
		},
		{
			nextLine: []assertion{
				{prefix: "aaa", want: false},
				{prefix: "bbb", want: true},
				{prefix: "ccc", want: false},
			},
			nextNextLine: []assertion{
				{prefix: "aaa", want: false},
				{prefix: "bbb", want: false},
				{prefix: "ccc", want: true},
			},
		},
		{
			nextLine: []assertion{
				{prefix: "aaa", want: false},
				{prefix: "bbb", want: false},
				{prefix: "ccc", want: true},
				{prefix: "ddd", want: false},
			},
			nextNextLine: []assertion{
				{prefix: "aaa", want: false},
				{prefix: "bbb", want: false},
				{prefix: "ccc", want: false},
				{prefix: "ddd", want: false},
			},
		},
		{
			nextLine: []assertion{
				{prefix: "aaa", want: false},
				{prefix: "bbb", want: false},
				{prefix: "ccc", want: false},
				{prefix: "ddd", want: false},
			},
			nextNextLine: []assertion{
				{prefix: "aaa", want: false},
				{prefix: "bbb", want: false},
				{prefix: "ccc", want: false},
				{prefix: "ddd", want: false},
			},
			wantReadLineErr: io.EOF,
		},
	}

	for _, tc := range testsPerReadLine {
		for _, assert := range tc.nextLine {
			got, err := in.nextLineStartsWith(assert.prefix)
			if err != nil {
				t.Fatalf("nextLineStartsWith returned unexpected error: %s", err)
			}

			if got != assert.want {
				t.Fatalf("unexpected result for prefix %q. got=%t, want=%t", assert.prefix, got, assert.want)
			}
		}

		for _, assert := range tc.nextNextLine {
			got, err := in.nextNextLineStartsWith(assert.prefix)
			if err != nil {
				t.Fatalf("nextLineStartsWith returned unexpected error: %s", err)
			}

			if got != assert.want {
				t.Fatalf("unexpected result for prefix %q. got=%t, want=%t", assert.prefix, got, assert.want)
			}
		}

		_, err := in.readLine()
		if err != tc.wantReadLineErr {
			t.Fatalf("readLine returned unexpected error. got=%s, want=%s", err, tc.wantReadLineErr)
		}

	}
}
```

## File: `diff/testdata/complicated_filenames.diff`
```
diff --git a/new empty file with spaces b/new empty file with spaces
new file mode 100644
index 0000000..e69de29
diff --git a/new file with text b/new file with text
new file mode 100644
index 0000000..c3ed4be
--- /dev/null
+++ b/new file with text
@@ -0,0 +1 @@
+new file with text
diff --git a/existing file with spaces b/new file with spaces
similarity index 100%
copy from existing file with spaces
copy to new file with spaces
diff --git a/existing file with spaces "b/new, complicated\nfilen\303\270me"
similarity index 100%
copy from existing file with spaces
copy to "new, complicated\nfilen\303\270me"
diff --git a/existing file with spaces "b/new \"complicated\" filename"
similarity index 100%
copy from existing file with spaces
copy to "new \"complicated\" filename"
diff --git "a/existing \"complicated\" filename" b/new, simpler filename
similarity index 100%
copy from "existing \"complicated\" filename"
copy to new, simpler filename
```

## File: `diff/testdata/delete_empty_file.diff`
```
diff --git Euler 0011/README.txt~ Euler 0011/README.txt~
deleted file mode 100644
index e69de29bb2d1d6434b8b29ae775ad8c2e48c5391..0000000000000000000000000000000000000000
diff --git Euler 0011/Euler0011.cpp Euler 0011/Euler0011.cpp
deleted file mode 100644
index 6490416c8cb4bbf2afbafa66251a9eab983086d1..0000000000000000000000000000000000000000
--- Euler 0011/Euler0011.cpp	
+++ /dev/null
@@ -1,1 +0,0 @@
-#include <iostream>
\ No newline at end of file
diff --git Euler 0011/README.txt~ Euler 0011/README.txt~
deleted file mode 100644
index e69de29bb2d1d6434b8b29ae775ad8c2e48c5391..0000000000000000000000000000000000000000
diff --git Euler 0011/README.txt Euler 0011/README.txt
deleted file mode 100644
index f8ea904baa27c54eb73cc02d5a555878b28672ff..0000000000000000000000000000000000000000
--- Euler 0011/README.txt	
+++ /dev/null
@@ -1,1 +0,0 @@
-In the 20�20 grid below, four numbers along a diagonal line have been marked in red.
\ No newline at end of file
diff --git Euler 0011/README.txt~ Euler 0011/README.txt~
deleted file mode 100644
index e69de29bb2d1d6434b8b29ae775ad8c2e48c5391..0000000000000000000000000000000000000000
```

## File: `diff/testdata/empty_multi.diff`
```
diff --git Godeps/_workspace/src/github.com/sourcegraph/go-diff/diff/testdata/empty.diff Godeps/_workspace/src/github.com/sourcegraph/go-diff/diff/testdata/empty.diff
new file mode 100644
index 0000000000000000000000000000000000000000..e69de29bb2d1d6434b8b29ae775ad8c2e48c5391
diff --git Godeps/_workspace/src/github.com/sourcegraph/go-diff/diff/testdata/empty_new.diff Godeps/_workspace/src/github.com/sourcegraph/go-diff/diff/testdata/empty_new.diff
new file mode 100644
index 0000000000000000000000000000000000000000..527e2e70f57b02e709f53e3ac2b7f59e2b5a46bc
--- /dev/null
+++ Godeps/_workspace/src/github.com/sourcegraph/go-diff/diff/testdata/empty_new.diff
@@ -0,0 +1,2 @@
+@@ -1,1 +0,0 @@
+-b
```

## File: `diff/testdata/empty_new.diff`
```
@@ -1,1 +0,0 @@
-b
```

## File: `diff/testdata/empty_orig.diff`
```
@@ -0,0 +1,1 @@
+b
```

## File: `diff/testdata/long_line_multi.diff`
```
diff --git a/blah.txt b/blah.txt
new file mode 100644
index 0000000..6b8710a
--- /dev/null
+++ b/blah.txt
@@ -0,0 +1,1 @@
+blah
diff --git a/foo/bar.svg b/foo/bar.svg
new file mode 100644
index 0000000..d9e6c40
--- /dev/null
+++ b/foo/bar.svg
@@ -0,0 +1,4 @@
+<?xml version="1.0" standalone="yes"?>
+
+<svg version="1.1" viewBox="0.0 0.0 431.0 1003.0" fill="none" stroke="none" stroke-linecap="square" stroke-miterlimit="10" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"><clipPath id="p.0"><path d="m0 0l431.0 0l0 1003.0l-431.0 0l0 -1003.0z" clip-rule="nonzero"></path></clipPath><g clip-path="url(#p.0)"><path fill="#000000" fill-opacity="0.0" d="m0 0l431.32022 0l0 1003.2756l-431.32022 0z" fill-rule="nonzero"></path><path fill="#9fc5e8" d="m20.506561 73.764366l398.99213 0l0 310.11023l-398.99213 0z" fill-rule="nonzero"></path><path stroke="#6fa8dc" stroke-width="1.0" stroke-linejoin="round" stroke-linecap="butt" d="m20.506561 73.764366l398.99213 0l0 310.11023l-398.99213 0z" fill-rule="nonzero"></path><path fill="#0b5394" d="m141.96915 95.684364l2.671875 0.84375q-0.609375 2.21875 -2.046875 3.3125q-1.421875 1.078125 -3.609375 1.078125q-2.703125 0 -4.453125 -1.84375q-1.734375 -1.859375 -1.734375 -5.078125q0 -3.390625 1.75 -5.265625q1.75 -1.875 4.609375 -1.875q2.5 0 4.046875 1.46875q0.9375 0.875 1.390625 2.5l-2.71875 0.65625q-0.234375 -1.0625 -1.0 -1.671875q-0.765625 -0.609375 -1.859375 -0.609375q-1.515625 0 -2.453125 1.09375q-0.9375 1.078125 -0.9375 3.5q0 2.578125 0.921875 3.6875q0.921875 1.09375 2.40625 1.09375q1.109375 0 1.890625 -0.6875q0.78125 -0.703125 1.125 -2.203125zm4.160446 -0.0625q0 -1.296875 0.640625 -2.515625q0.640625 -1.21875 1.8124847 -1.859375q1.171875 -0.640625 2.609375 -0.640625q2.25 0 3.671875 1.453125q1.421875 1.453125 1.421875 3.671875q0 2.234375 -1.4375 3.703125q-1.4375 1.46875 -3.625 1.46875q-1.359375 0 -2.59375 -0.609375q-1.2187347 -0.609375 -1.8593597 -1.796875q-0.640625 -1.1875 -0.640625 -2.875zm2.6718597 0.140625q0 1.46875 0.6875 2.25q0.703125 0.765625 1.71875 0.765625q1.015625 0 1.703125 -0.765625q0.703125 -0.78125 0.703125 -2.265625q0 -1.453125 -0.703125 -2.234375q-0.6875 -0.78125 -1.703125 -0.78125q-1.015625 0 -1.71875 0.78125q-0.6875 0.78125 -0.6875 2.25zm18.286621 4.921875l-2.609375 0l0 -5.03125q0 -1.59375 -0.171875 -2.0625q-0.15625 -0.46875 -0.53125 -0.71875q-0.375 -0.265625 -0.90625 -0.265625q-0.6875 0 -1.234375 0.375q-0.53125 0.359375 -0.734375 0.984375q-0.1875 0.609375 -0.1875 2.25l0 4.46875l-2.609375 0l0 -9.859375l2.421875 0l0 1.453125q1.296875 -1.671875 3.25 -1.671875q0.859375 0 1.578125 0.3125q0.71875 0.3125 1.078125 0.796875q0.359375 0.484375 0.5 1.09375q0.15625 0.609375 0.15625 1.75l0 6.125zm1.2865906 -9.859375l1.453125 0l0 -0.734375q0 -1.25 0.265625 -1.859375q0.265625 -0.609375 0.96875 -0.984375q0.71875 -0.390625 1.796875 -0.390625q1.109375 0 2.1875 0.328125l-0.359375 1.8125q-0.625 -0.140625 -1.203125 -0.140625q-0.5625 0 -0.8125 0.265625q-0.234375 0.265625 -0.234375 1.015625l0 0.6875l1.9375 0l0 2.0625l-1.9375 0l0 7.796875l-2.609375 0l0 -7.796875l-1.453125 0l0 -2.0625zm7.353302 -1.328125l0 -2.40625l2.609375 0l0 2.40625l-2.609375 0zm0 11.1875l0 -9.859375l2.609375 0l0 9.859375l-2.609375 0zm4.948944 0.65625l2.96875 0.359375q0.078125 0.515625 0.34375 0.703125q0.375 0.28125 1.171875 0.28125q1.03125 0 1.53125 -0.296875q0.34375 -0.203125 0.515625 -0.65625q0.125 -0.328125 0.125 -1.203125l0 -1.4375q-1.171875 1.59375 -2.953125 1.59375q-1.984375 0 -3.140625 -1.671875q-0.90625 -1.328125 -0.90625 -3.3125q0 -2.46875 1.1875 -3.78125q1.1875 -1.3125 2.96875 -1.3125q1.828125 0 3.015625 1.609375l0 -1.390625l2.4375 0l0 8.84375q0 1.75 -0.296875 2.609375q-0.28125 0.859375 -0.796875 1.34375q-0.515625 0.5 -1.390625 0.78125q-0.859375 0.28125 -2.1875 0.28125q-2.515625 0 -3.5625 -0.859375q-1.046875 -0.859375 -1.046875 -2.171875q0 -0.140625 0.015625 -0.3125zm2.328125 -5.78125q0 1.5625 0.609375 2.296875q0.609375 0.71875 1.5 0.71875q0.953125 0 1.609375 -0.734375q0.65625 -0.75 0.65625 -2.21875q0 -1.53125 -0.640625 -2.265625q-0.625 -0.75 -1.578125 -0.75q-0.9375 0 -1.546875 0.734375q-0.609375 0.71875 -0.609375 2.21875zm15.786591 5.125l0 -1.46875q-0.53125 0.78125 -1.40625 1.234375q-0.875 0.453125 -1.859375 0.453125q-0.984375 0 -1.78125 -0.4375q-0.78125 -0.4375 -1.140625 -1.21875q-0.34375 -0.796875 -0.34375 -2.1875l0 -6.234375l2.609375 0l0 4.53125q0 2.078125 0.140625 2.546875q0.140625 0.46875 0.515625 0.75q0.390625 0.265625 0.96875 0.265625q0.671875 0 1.203125 -0.359375q0.53125 -0.375 0.71875 -0.90625q0.1875 -0.546875 0.1875 -2.671875l0 -4.15625l2.609375 0l0 9.859375l-2.421875 0zm7.411621 0l-2.609375 0l0 -9.859375l2.421875 0l0 1.40625q0.625 -0.984375 1.109375 -1.296875q0.5 -0.328125 1.140625 -0.328125q0.890625 0 1.71875 0.5l-0.8125 2.265625q-0.65625 -0.421875 -1.21875 -0.421875q-0.546875 0 -0.9375 0.296875q-0.375 0.296875 -0.59375 1.09375q-0.21875 0.78125 -0.21875 3.296875l0 3.046875zm10.463379 -3.140625l2.609375 0.4375q-0.5 1.4375 -1.59375 2.1875q-1.078125 0.734375 -2.703125 0.734375q-2.5625 0 -3.796875 -1.671875q-0.96875 -1.34375 -0.96875 -3.40625q0 -2.4375 1.265625 -3.828125q1.28125 -1.390625 3.25 -1.390625q2.1875 0 3.453125 1.453125q1.28125 1.453125 1.234375 4.453125l-6.53125 0q0.015625 1.15625 0.625 1.8125q0.609375 0.640625 1.5 0.640625q0.609375 0 1.03125 -0.328125q0.421875 -0.34375 0.625 -1.09375zm0.15625 -2.625q-0.03125 -1.140625 -0.59375 -1.71875q-0.546875 -0.59375 -1.34375 -0.59375q-0.859375 0 -1.40625 0.625q-0.5625 0.609375 -0.546875 1.6875l3.890625 0zm14.027771 9.765625l-1.796875 0q-1.40625 -2.140625 -2.15625 -4.453125q-0.734375 -2.3125 -0.734375 -4.46875q0 -2.6875 0.90625 -5.078125q0.796875 -2.078125 2.03125 -3.828125l1.78125 0q-1.28125 2.8125 -1.765625 4.78125q-0.46875 1.96875 -0.46875 4.171875q0 1.53125 0.28125 3.125q0.28125 1.59375 0.78125 3.03125q0.328125 0.953125 1.140625 2.71875zm1.900177 -4.0l0 -13.59375l4.421875 0q2.5 0 3.265625 0.203125q1.15625 0.296875 1.9375 1.328125q0.796875 1.015625 0.796875 2.640625q0 1.25 -0.453125 2.109375q-0.453125 0.859375 -1.15625 1.34375q-0.703125 0.484375 -1.421875 0.640625q-0.984375 0.203125 -2.84375 0.203125l-1.796875 0l0 5.125l-2.75 0zm2.75 -11.296875l0 3.859375l1.5 0q1.625 0 2.171875 -0.21875q0.546875 -0.21875 0.859375 -0.671875q0.3125 -0.453125 0.3125 -1.046875q0 -0.75 -0.4375 -1.234375q-0.4375 -0.484375 -1.09375 -0.59375q-0.5 -0.09375 -1.984375 -0.09375l-1.328125 0zm12.287323 -2.296875l0 5.0q1.25 -1.484375 3.015625 -1.484375q0.890625 0 1.609375 0.34375q0.734375 0.328125 1.09375 0.84375q0.375 0.515625 0.5 1.15625q0.140625 0.625 0.140625 1.953125l0 5.78125l-2.609375 0l0 -5.203125q0 -1.546875 -0.15625 -1.96875q-0.140625 -0.421875 -0.515625 -0.65625q-0.375 -0.25 -0.9375 -0.25q-0.65625 0 -1.171875 0.3125q-0.5 0.3125 -0.734375 0.953125q-0.234375 0.640625 -0.234375 1.875l0 4.9375l-2.609375 0l0 -13.59375l2.609375 0zm10.739746 6.75l-2.359375 -0.4375q0.390625 -1.421875 1.359375 -2.109375q0.984375 -0.6875 2.90625 -0.6875q1.734375 0 2.59375 0.421875q0.859375 0.40625 1.203125 1.046875q0.34375 0.625 0.34375 2.328125l-0.03125 3.046875q0 1.296875 0.125 1.921875q0.125 0.609375 0.46875 1.3125l-2.578125 0q-0.09375 -0.265625 -0.25 -0.765625q-0.0625 -0.234375 -0.09375 -0.3125q-0.65625 0.65625 -1.421875 0.984375q-0.765625 0.3125 -1.625 0.3125q-1.515625 0 -2.40625 -0.8125q-0.875 -0.828125 -0.875 -2.09375q0 -0.84375 0.390625 -1.484375q0.40625 -0.65625 1.125 -1.0q0.71875 -0.359375 2.078125 -0.625q1.828125 -0.328125 2.53125 -0.625l0 -0.265625q0 -0.75 -0.375 -1.0625q-0.359375 -0.328125 -1.390625 -0.328125q-0.703125 0 -1.09375 0.28125q-0.390625 0.265625 -0.625 0.953125zm3.484375 2.109375q-0.5 0.171875 -1.59375 0.40625q-1.078125 0.234375 -1.40625 0.453125q-0.515625 0.359375 -0.515625 0.921875q0 0.546875 0.40625 0.953125q0.40625 0.390625 1.046875 0.390625q0.703125 0 1.34375 -0.46875q0.46875 -0.359375 0.625 -0.859375q0.09375 -0.34375 0.09375 -1.28125l0 -0.515625zm4.031952 1.921875l2.609375 -0.390625q0.171875 0.75 0.671875 1.15625q0.515625 0.390625 1.4375 0.390625q1.0 0 1.515625 -0.375q0.34375 -0.265625 0.34375 -0.703125q0 -0.296875 -0.1875 -0.484375q-0.1875 -0.1875 -0.875 -0.34375q-3.140625 -0.703125 -4.0 -1.265625q-1.15625 -0.796875 -1.15625 -2.21875q0 -1.28125 1.0 -2.15625q1.015625 -0.875 3.140625 -0.875q2.03125 0 3.0 0.65625q0.984375 0.65625 1.359375 1.953125l-2.453125 0.453125q-0.15625 -0.578125 -0.609375 -0.875q-0.4375 -0.3125 -1.25 -0.3125q-1.03125 0 -1.46875 0.296875q-0.296875 0.203125 -0.296875 0.515625q0 0.28125 0.25 0.484375q0.359375 0.25 2.4375 0.734375q2.078125 0.46875 2.90625 1.15625q0.828125 0.6875 0.828125 1.9375q0 1.359375 -1.140625 2.328125q-1.125 0.96875 -3.34375 0.96875q-2.015625 0 -3.1875 -0.8125q-1.171875 -0.8125 -1.53125 -2.21875zm16.985107 -0.328125l2.609375 0.4375q-0.5 1.4375 -1.59375 2.1875q-1.078125 0.734375 -2.703125 0.734375q-2.5625 0 -3.796875 -1.671875q-0.96875 -1.34375 -0.96875 -3.40625q0 -2.4375 1.265625 -3.828125q1.28125 -1.390625 3.25 -1.390625q2.1875 0 3.453125 1.453125q1.28125 1.453125 1.234375 4.453125l-6.53125 0q0.015625 1.15625 0.625 1.8125q0.609375 0.640625 1.5 0.640625q0.609375 0 1.03125 -0.328125q0.421875 -0.34375 0.625 -1.09375zm0.15625 -2.625q-0.03125 -1.140625 -0.59375 -1.71875q-0.546875 -0.59375 -1.34375 -0.59375q-0.859375 0 -1.40625 0.625q-0.5625 0.609375 -0.546875 1.6875l3.890625 0zm15.824646 5.765625l-2.609375 0l0 -9.828125q-1.4375 1.34375 -3.375 1.984375l0 -2.375q1.03125 -0.328125 2.21875 -1.25q1.203125 -0.9375 1.640625 -2.1875l2.125 0l0 13.65625zm3.531952 4.0q0.765625 -1.65625 1.078125 -2.546875q0.328125 -0.875 0.59375 -2.015625q0.265625 -1.15625 0.390625 -2.1875q0.140625 -1.03125 0.140625 -2.125q0 -2.203125 -0.484375 -4.171875q-0.46875 -1.96875 -1.734375 -4.78125l1.765625 0q1.40625 1.984375 2.171875 4.234375q0.78125 2.234375 0.78125 4.53125q0 1.9375 -0.609375 4.15625q-0.703125 2.484375 -2.296875 4.90625l-1.796875 0z" fill-rule="nonzero"></path><path fill="#cfe2f3" d="m57.730812 119.18956l325.92126 0l0 52.220474l-325.92126 0z" fill-rule="nonzero"></path><path fill="#0b5394" d="m120.037544 144.21979l0 -13.59375l6.03125 0q1.8125 0 2.7500076 0.359375q0.953125 0.359375 1.515625 1.296875q0.5625 0.921875 0.5625 2.046875q0 1.453125 -0.9375 2.453125q-0.921875 0.984375 -2.8906326 1.25q0.71875 0.34375 1.0937576 0.671875q0.78125 0.734375 1.484375 1.8125l2.375 3.703125l-2.265625 0l-1.7968826 -2.828125q-0.796875 -1.21875 -1.3125 -1.875q-0.5 -0.65625 -0.90625 -0.90625q-0.40625 -0.265625 -0.8125 -0.359375q-0.3125 -0.078125 -1.015625 -0.078125l-2.078125 0l0 6.046875l-1.796875 0zm1.796875 -7.59375l3.859375 0q1.234375 0 1.921875 -0.25q0.7031326 -0.265625 1.0625076 -0.828125q0.375 -0.5625 0.375 -1.21875q0 -0.96875 -0.703125 -1.578125q-0.7031326 -0.625 -2.2187576 -0.625l-4.296875 0l0 4.5zm18.176079 4.421875l1.71875 0.21875q-0.40625 1.5 -1.515625 2.34375q-1.09375 0.828125 -2.8125 0.828125q-2.15625 0 -3.421875 -1.328125q-1.265625 -1.328125 -1.265625 -3.734375q0 -2.484375 1.265625 -3.859375q1.28125 -1.375 3.328125 -1.375q1.984375 0 3.234375 1.34375q1.25 1.34375 1.25 3.796875q0 0.140625 -0.015625 0.4375l-7.34375 0q0.09375 1.625 0.921875 2.484375q0.828125 0.859375 2.0625 0.859375q0.90625 0 1.546875 -0.46875q0.65625 -0.484375 1.046875 -1.546875zm-5.484375 -2.703125l5.5 0q-0.109375 -1.234375 -0.625 -1.859375q-0.796875 -0.96875 -2.078125 -0.96875q-1.140625 0 -1.9375 0.78125q-0.78125 0.765625 -0.859375 2.046875zm15.547592 4.65625q-0.9375 0.796875 -1.796875 1.125q-0.859375 0.3125 -1.84375 0.3125q-1.609375 0 -2.484375 -0.78125q-0.875 -0.796875 -0.875 -2.03125q0 -0.734375 0.328125 -1.328125q0.328125 -0.59375 0.859375 -0.953125q0.53125 -0.359375 1.203125 -0.546875q0.5 -0.140625 1.484375 -0.25q2.03125 -0.25 2.984375 -0.578125q0 -0.34375 0 -0.4375q0 -1.015625 -0.46875 -1.4375q-0.640625 -0.5625 -1.90625 -0.5625q-1.171875 0 -1.734375 0.40625q-0.5625 0.40625 -0.828125 1.46875l-1.640625 -0.234375q0.234375 -1.046875 0.734375 -1.6875q0.515625 -0.640625 1.46875 -0.984375q0.96875 -0.359375 2.25 -0.359375q1.265625 0 2.046875 0.296875q0.78125 0.296875 1.15625 0.75q0.375 0.453125 0.515625 1.140625q0.09375 0.421875 0.09375 1.53125l0 2.234375q0 2.328125 0.09375 2.953125q0.109375 0.609375 0.4375 1.171875l-1.75 0q-0.265625 -0.515625 -0.328125 -1.21875zm-0.140625 -3.71875q-0.90625 0.359375 -2.734375 0.625q-1.03125 0.140625 -1.453125 0.328125q-0.421875 0.1875 -0.65625 0.546875q-0.234375 0.359375 -0.234375 0.796875q0 0.671875 0.5 1.125q0.515625 0.4375 1.484375 0.4375q0.96875 0 1.71875 -0.421875q0.75 -0.4375 1.109375 -1.15625q0.265625 -0.578125 0.265625 -1.671875l0 -0.609375zm10.469467 4.9375l0 -1.25q-0.9375 1.46875 -2.75 1.46875q-1.171875 0 -2.171875 -0.640625q-0.984375 -0.65625 -1.53125 -1.8125q-0.53125 -1.171875 -0.53125 -2.6875q0 -1.46875 0.484375 -2.671875q0.5 -1.203125 1.46875 -1.84375q0.984375 -0.640625 2.203125 -0.640625q0.890625 0 1.578125 0.375q0.703125 0.375 1.140625 0.984375l0 -4.875l1.65625 0l0 13.59375l-1.546875 0zm-5.28125 -4.921875q0 1.890625 0.796875 2.828125q0.8125 0.9375 1.890625 0.9375q1.09375 0 1.859375 -0.890625q0.765625 -0.890625 0.765625 -2.734375q0 -2.015625 -0.78125 -2.953125q-0.78125 -0.953125 -1.921875 -0.953125q-1.109375 0 -1.859375 0.90625q-0.75 0.90625 -0.75 2.859375zm14.465271 -6.765625l0 -1.90625l1.671875 0l0 1.90625l-1.671875 0zm0 11.6875l0 -9.859375l1.671875 0l0 9.859375l-1.671875 0zm4.129196 0l0 -9.859375l1.5 0l0 1.40625q1.09375 -1.625 3.140625 -1.625q0.890625 0 1.640625 0.328125q0.75 0.3125 1.109375 0.84375q0.375 0.515625 0.53125 1.21875q0.09375 0.46875 0.09375 1.625l0 6.0625l-1.671875 0l0 -6.0q0 -1.015625 -0.203125 -1.515625q-0.1875 -0.515625 -0.6875 -0.8125q-0.5 -0.296875 -1.171875 -0.296875q-1.0625 0 -1.84375 0.671875q-0.765625 0.671875 -0.765625 2.578125l0 5.375l-1.671875 0zm10.391342 -11.6875l0 -1.90625l1.671875 0l0 1.90625l-1.671875 0zm0 11.6875l0 -9.859375l1.671875 0l0 9.859375l-1.671875 0zm7.785446 -1.5l0.234375 1.484375q-0.703125 0.140625 -1.265625 0.140625q-0.90625 0 -1.40625 -0.28125q-0.5 -0.296875 -0.703125 -0.75q-0.203125 -0.46875 -0.203125 -1.984375l0 -5.65625l-1.234375 0l0 -1.3125l1.234375 0l0 -2.4375l1.65625 -1.0l0 3.4375l1.6875 0l0 1.3125l-1.6875 0l0 5.75q0 0.71875 0.078125 0.921875q0.09375 0.203125 0.296875 0.328125q0.203125 0.125 0.578125 0.125q0.265625 0 0.734375 -0.078125zm1.5426788 -10.1875l0 -1.90625l1.671875 0l0 1.90625l-1.671875 0zm0 11.6875l0 -9.859375l1.671875 0l0 9.859375l-1.671875 0zm10.566696 -1.21875q-0.9375 0.796875 -1.796875 1.125q-0.859375 0.3125 -1.84375 0.3125q-1.609375 0 -2.484375 -0.78125q-0.875 -0.796875 -0.875 -2.03125q0 -0.734375 0.328125 -1.328125q0.328125 -0.59375 0.859375 -0.953125q0.53125 -0.359375 1.203125 -0.546875q0.5 -0.140625 1.484375 -0.25q2.03125 -0.25 2.984375 -0.578125q0 -0.34375 0 -0.4375q0 -1.015625 -0.46875 -1.4375q-0.640625 -0.5625 -1.90625 -0.5625q-1.171875 0 -1.734375 0.40625q-0.5625 0.40625 -0.828125 1.46875l-1.640625 -0.234375q0.234375 -1.046875 0.734375 -1.6875q0.515625 -0.640625 1.46875 -0.984375q0.96875 -0.359375 2.25 -0.359375q1.265625 0 2.046875 0.296875q0.78125 0.296875 1.15625 0.75q0.375 0.453125 0.515625 1.140625q0.09375 0.421875 0.09375 1.53125l0 2.234375q0 2.328125 0.09375 2.953125q0.109375 0.609375 0.4375 1.171875l-1.75 0q-0.265625 -0.515625 -0.328125 -1.21875zm-0.140625 -3.71875q-0.90625 0.359375 -2.734375 0.625q-1.03125 0.140625 -1.453125 0.328125q-0.421875 0.1875 -0.65625 0.546875q-0.234375 0.359375 -0.234375 0.796875q0 0.671875 0.5 1.125q0.515625 0.4375 1.484375 0.4375q0.96875 0 1.71875 -0.421875q0.75 -0.4375 1.109375 -1.15625q0.265625 -0.578125 0.265625 -1.671875l0 -0.609375zm4.047592 4.9375l0 -13.59375l1.671875 0l0 13.59375l-1.671875 0zm15.796875 -3.609375l1.640625 0.21875q-0.265625 1.6875 -1.375 2.65625q-1.109375 0.953125 -2.734375 0.953125q-2.015625 0 -3.25 -1.3125q-1.21875 -1.328125 -1.21875 -3.796875q0 -1.59375 0.515625 -2.78125q0.53125 -1.203125 1.609375 -1.796875q1.09375 -0.609375 2.359375 -0.609375q1.609375 0 2.625 0.8125q1.015625 0.8125 1.3125 2.3125l-1.625 0.25q-0.234375 -1.0 -0.828125 -1.5q-0.59375 -0.5 -1.421875 -0.5q-1.265625 0 -2.0625 0.90625q-0.78125 0.90625 -0.78125 2.859375q0 1.984375 0.765625 2.890625q0.765625 0.890625 1.984375 0.890625q0.984375 0 1.640625 -0.59375q0.65625 -0.609375 0.84375 -1.859375zm2.265625 -1.3125q0 -2.734375 1.53125 -4.0625q1.265625 -1.09375 3.09375 -1.09375q2.03125 0 3.3125 1.34375q1.296875 1.328125 1.296875 3.671875q0 1.90625 -0.578125 3.0q-0.5625 1.078125 -1.65625 1.6875q-1.078125 0.59375 -2.375 0.59375q-2.0625 0 -3.34375 -1.328125q-1.28125 -1.328125 -1.28125 -3.8125zm1.71875 0q0 1.890625 0.828125 2.828125q0.828125 0.9375 2.078125 0.9375q1.25 0 2.0625 -0.9375q0.828125 -0.953125 0.828125 -2.890625q0 -1.828125 -0.828125 -2.765625q-0.828125 -0.9375 -2.0625 -0.9375q-1.25 0 -2.078125 0.9375q-0.828125 0.9375 -0.828125 2.828125zm9.281967 4.921875l0 -9.859375l1.5 0l0 1.40625q1.09375 -1.625 3.140625 -1.625q0.890625 0 1.640625 0.328125q0.75 0.3125 1.109375 0.84375q0.375 0.515625 0.53125 1.21875q0.09375 0.46875 0.09375 1.625l0 6.0625l-1.671875 0l0 -6.0q0 -1.015625 -0.203125 -1.515625q-0.1875 -0.515625 -0.6875 -0.8125q-0.5 -0.296875 -1.171875 -0.296875q-1.0625 0 -1.84375 0.671875q-0.765625 0.671875 -0.765625 2.578125l0 5.375l-1.671875 0zm10.781967 0l0 -8.546875l-1.484375 0l0 -1.3125l1.484375 0l0 -1.046875q0 -0.984375 0.171875 -1.46875q0.234375 -0.65625 0.84375 -1.046875q0.609375 -0.40625 1.703125 -0.40625q0.703125 0 1.5625 0.15625l-0.25 1.46875q-0.515625 -0.09375 -0.984375 -0.09375q-0.765625 0 -1.078125 0.328125q-0.3125 0.3125 -0.3125 1.203125l0 0.90625l1.921875 0l0 1.3125l-1.921875 0l0 8.546875l-1.65625 0zm4.792679 -11.6875l0 -1.90625l1.671875 0l0 1.90625l-1.671875 0zm0 11.6875l0 -9.859375l1.671875 0l0 9.859375l-1.671875 0zm3.8323212 0.8125l1.609375 0.25q0.109375 0.75 0.578125 1.09375q0.609375 0.453125 1.6875 0.453125q1.171875 0 1.796875 -0.46875q0.625 -0.453125 0.859375 -1.28125q0.125 -0.515625 0.109375 -2.15625q-1.09375 1.296875 -2.71875 1.296875q-2.03125 0 -3.15625 -1.46875q-1.109375 -1.46875 -1.109375 -3.515625q0 -1.40625 0.515625 -2.59375q0.515625 -1.203125 1.484375 -1.84375q0.96875 -0.65625 2.265625 -0.65625q1.75 0 2.875 1.40625l0 -1.1875l1.546875 0l0 8.515625q0 2.3125 -0.46875 3.265625q-0.46875 0.96875 -1.484375 1.515625q-1.015625 0.5625 -2.5 0.5625q-1.765625 0 -2.859375 -0.796875q-1.078125 -0.796875 -1.03125 -2.390625zm1.375 -5.921875q0 1.953125 0.765625 2.84375q0.78125 0.890625 1.9375 0.890625q1.140625 0 1.921875 -0.890625q0.78125 -0.890625 0.78125 -2.78125q0 -1.8125 -0.8125 -2.71875q-0.796875 -0.921875 -1.921875 -0.921875q-1.109375 0 -1.890625 0.90625q-0.78125 0.890625 -0.78125 2.671875zm15.750702 5.109375l0 -1.453125q-1.140625 1.671875 -3.125 1.671875q-0.859375 0 -1.625 -0.328125q-0.75 -0.34375 -1.125 -0.84375q-0.359375 -0.5 -0.515625 -1.234375q-0.09375 -0.5 -0.09375 -1.5625l0 -6.109375l1.671875 0l0 5.46875q0 1.3125 0.09375 1.765625q0.15625 0.65625 0.671875 1.03125q0.515625 0.375 1.265625 0.375q0.75 0 1.40625 -0.375q0.65625 -0.390625 0.921875 -1.046875q0.28125 -0.671875 0.28125 -1.9375l0 -5.28125l1.671875 0l0 9.859375l-1.5 0zm3.9069824 0l0 -9.859375l1.5 0l0 1.5q0.578125 -1.046875 1.0625 -1.375q0.484375 -0.34375 1.078125 -0.34375q0.84375 0 1.71875 0.546875l-0.578125 1.546875q-0.609375 -0.359375 -1.234375 -0.359375q-0.546875 0 -0.984375 0.328125q-0.421875 0.328125 -0.609375 0.90625q-0.28125 0.890625 -0.28125 1.953125l0 5.15625l-1.671875 0zm12.665802 -1.21875q-0.9375 0.796875 -1.796875 1.125q-0.859375 0.3125 -1.84375 0.3125q-1.609375 0 -2.484375 -0.78125q-0.875 -0.796875 -0.875 -2.03125q0 -0.734375 0.328125 -1.328125q0.328125 -0.59375 0.859375 -0.953125q0.53125 -0.359375 1.203125 -0.546875q0.5 -0.140625 1.484375 -0.25q2.03125 -0.25 2.984375 -0.578125q0 -0.34375 0 -0.4375q0 -1.015625 -0.46875 -1.4375q-0.640625 -0.5625 -1.90625 -0.5625q-1.171875 0 -1.734375 0.40625q-0.5625 0.40625 -0.828125 1.46875l-1.640625 -0.234375q0.234375 -1.046875 0.734375 -1.6875q0.515625 -0.640625 1.46875 -0.984375q0.96875 -0.359375 2.25 -0.359375q1.265625 0 2.046875 0.296875q0.78125 0.296875 1.15625 0.75q0.375 0.453125 0.515625 1.140625q0.09375 0.421875 0.09375 1.53125l0 2.234375q0 2.328125 0.09375 2.953125q0.109375 0.609375 0.4375 1.171875l-1.75 0q-0.265625 -0.515625 -0.328125 -1.21875zm-0.140625 -3.71875q-0.90625 0.359375 -2.734375 0.625q-1.03125 0.140625 -1.453125 0.328125q-0.421875 0.1875 -0.65625 0.546875q-0.234375 0.359375 -0.234375 0.796875q0 0.671875 0.5 1.125q0.515625 0.4375 1.484375 0.4375q0.96875 0 1.71875 -0.421875q0.75 -0.4375 1.109375 -1.15625q0.265625 -0.578125 0.265625 -1.671875l0 -0.609375zm7.735077 3.4375l0.234375 1.484375q-0.703125 0.140625 -1.265625 0.140625q-0.90625 0 -1.40625 -0.28125q-0.5 -0.296875 -0.703125 -0.75q-0.203125 -0.46875 -0.203125 -1.984375l0 -5.65625l-1.234375 0l0 -1.3125l1.234375 0l0 -2.4375l1.65625 -1.0l0 3.4375l1.6875 0l0 1.3125l-1.6875 0l0 5.75q0 0.71875 0.078125 0.921875q0.09375 0.203125 0.296875 0.328125q0.203125 0.125 0.578125 0.125q0.265625 0 0.734375 -0.078125zm1.5426941 -10.1875l0 -1.90625l1.671875 0l0 1.90625l-1.671875 0zm0 11.6875l0 -9.859375l1.671875 0l0 9.859375l-1.671875 0zm3.504181 -4.921875q0 -2.734375 1.53125 -4.0625q1.265625 -1.09375 3.09375 -1.09375q2.03125 0 3.3125 1.34375q1.296875 1.328125 1.296875 3.671875q0 1.90625 -0.578125 3.0q-0.5625 1.078125 -1.65625 1.6875q-1.078125 0.59375 -2.375 0.59375q-2.0625 0 -3.34375 -1.328125q-1.28125 -1.328125 -1.28125 -3.8125zm1.71875 0q0 1.890625 0.828125 2.828125q0.828125 0.9375 2.078125 0.9375q1.25 0 2.0625 -0.9375q0.828125 -0.953125 0.828125 -2.890625q0 -1.828125 -0.828125 -2.765625q-0.828125 -0.9375 -2.0625 -0.9375q-1.25 0 -2.078125 0.9375q-0.828125 0.9375 -0.828125 2.828125zm9.281982 4.921875l0 -9.859375l1.5 0l0 1.40625q1.09375 -1.625 3.140625 -1.625q0.890625 0 1.640625 0.328125q0.75 0.3125 1.109375 0.84375q0.375 0.515625 0.53125 1.21875q0.09375 0.46875 0.09375 1.625l0 6.0625l-1.671875 0l0 -6.0q0 -1.015625 -0.203125 -1.515625q-0.1875 -0.515625 -0.6875 -0.8125q-0.5 -0.296875 -1.171875 -0.296875q-1.0625 0 -1.84375 0.671875q-0.765625 0.671875 -0.765625 2.578125l0 5.375l-1.671875 0z" fill-rule="nonzero"></path><path fill="#0b5394" d="m89.43633 161.0998l0 -9.3125l1.84375 0l2.203125 6.59375q0.3125 0.921875 0.453125 1.375q0.15625 -0.5 0.484375 -1.484375l2.234375 -6.484375l1.65625 0l0 9.3125l-1.1875 0l0 -7.78125l-2.703125 7.78125l-1.109375 0l-2.6875 -7.921875l0 7.921875l-1.1875 0zm15.602432 -2.171875l1.1875 0.140625q-0.28125 1.046875 -1.046875 1.625q-0.75 0.5625 -1.921875 0.5625q-1.484375 0 -2.359375 -0.90625q-0.859375 -0.921875 -0.859375 -2.5625q0 -1.703125 0.875 -2.640625q0.890625 -0.9375 2.28125 -0.9375q1.359375 0 2.203125 0.921875q0.859375 0.921875 0.859375 2.578125q0 0.109375 0 0.3125l-5.03125 0q0.0625 1.109375 0.625 1.703125q0.5625 0.59375 1.40625 0.59375q0.640625 0 1.078125 -0.328125q0.453125 -0.34375 0.703125 -1.0625zm-3.75 -1.84375l3.765625 0q-0.078125 -0.859375 -0.4375 -1.28125q-0.546875 -0.65625 -1.40625 -0.65625q-0.796875 0 -1.328125 0.53125q-0.53125 0.515625 -0.59375 1.40625zm6.5374756 4.015625l0 -6.734375l1.03125 0l0 1.015625q0.390625 -0.71875 0.71875 -0.9375q0.34375 -0.234375 0.734375 -0.234375q0.578125 0 1.171875 0.359375l-0.390625 1.0625q-0.421875 -0.25 -0.828125 -0.25q-0.375 0 -0.6875 0.234375q-0.296875 0.21875 -0.421875 0.625q-0.1875 0.609375 -0.1875 1.328125l0 3.53125l-1.140625 0zm4.2352448 0.5625l1.125 0.15625q0.0625 0.515625 0.375 0.75q0.4375 0.328125 1.171875 0.328125q0.78125 0 1.21875 -0.328125q0.4375 -0.3125 0.578125 -0.890625q0.09375 -0.34375 0.09375 -1.453125q-0.75 0.875 -1.875 0.875q-1.390625 0 -2.15625 -1.0q-0.75 -1.0 -0.75 -2.40625q0 -0.96875 0.34375 -1.78125q0.359375 -0.8125 1.015625 -1.25q0.65625 -0.453125 1.5625 -0.453125q1.1875 0 1.96875 0.96875l0 -0.8125l1.046875 0l0 5.8125q0 1.578125 -0.328125 2.234375q-0.3125 0.65625 -1.015625 1.03125q-0.6875 0.390625 -1.703125 0.390625q-1.203125 0 -1.953125 -0.546875q-0.734375 -0.53125 -0.71875 -1.625zm0.953125 -4.046875q0 1.3125 0.515625 1.921875q0.53125 0.609375 1.328125 0.609375q0.796875 0 1.328125 -0.59375q0.53125 -0.609375 0.53125 -1.90625q0 -1.234375 -0.546875 -1.859375q-0.546875 -0.640625 -1.328125 -0.640625q-0.765625 0 -1.296875 0.625q-0.53125 0.625 -0.53125 1.84375zm11.287476 1.3125l1.1875 0.140625q-0.28125 1.046875 -1.046875 1.625q-0.75 0.5625 -1.921875 0.5625q-1.484375 0 -2.359375 -0.90625q-0.859375 -0.921875 -0.859375 -2.5625q0 -1.703125 0.875 -2.640625q0.890625 -0.9375 2.28125 -0.9375q1.359375 0 2.203125 0.921875q0.859375 0.921875 0.859375 2.578125q0 0.109375 0 0.3125l-5.03125 0q0.0625 1.109375 0.625 1.703125q0.5625 0.59375 1.40625 0.59375q0.640625 0 1.078125 -0.328125q0.453125 -0.34375 0.703125 -1.0625zm-3.75 -1.84375l3.765625 0q-0.078125 -0.859375 -0.4375 -1.28125q-0.546875 -0.65625 -1.40625 -0.65625q-0.796875 0 -1.328125 0.53125q-0.53125 0.515625 -0.59375 1.40625zm9.974846 1.03125l1.171875 -0.109375q0.078125 0.703125 0.375 1.15625q0.3125 0.4375 0.9375 0.71875q0.640625 0.265625 1.4375 0.265625q0.703125 0 1.234375 -0.203125q0.546875 -0.203125 0.8125 -0.5625q0.265625 -0.375 0.265625 -0.8125q0 -0.4375 -0.265625 -0.765625q-0.25 -0.328125 -0.828125 -0.546875q-0.375 -0.140625 -1.65625 -0.453125q-1.28125 -0.3125 -1.796875 -0.578125q-0.671875 -0.34375 -1.0 -0.859375q-0.328125 -0.53125 -0.328125 -1.171875q0 -0.703125 0.390625 -1.3125q0.40625 -0.609375 1.171875 -0.921875q0.78125 -0.328125 1.71875 -0.328125q1.03125 0 1.8125 0.34375q0.796875 0.328125 1.21875 0.984375q0.4375 0.640625 0.46875 1.453125l-1.1875 0.09375q-0.09375 -0.890625 -0.640625 -1.328125q-0.546875 -0.453125 -1.625 -0.453125q-1.109375 0 -1.625 0.40625q-0.515625 0.40625 -0.515625 0.984375q0 0.5 0.359375 0.828125q0.359375 0.328125 1.859375 0.671875q1.5 0.328125 2.0625 0.578125q0.8125 0.375 1.1875 0.953125q0.390625 0.578125 0.390625 1.328125q0 0.734375 -0.421875 1.390625q-0.421875 0.65625 -1.21875 1.03125q-0.796875 0.359375 -1.796875 0.359375q-1.265625 0 -2.125 -0.359375q-0.84375 -0.375 -1.328125 -1.109375q-0.484375 -0.75 -0.515625 -1.671875zm9.15538 2.984375l0 -6.734375l1.03125 0l0 1.015625q0.390625 -0.71875 0.71875 -0.9375q0.34375 -0.234375 0.734375 -0.234375q0.578125 0 1.171875 0.359375l-0.390625 1.0625q-0.421875 -0.25 -0.828125 -0.25q-0.375 0 -0.6875 0.234375q-0.296875 0.21875 -0.421875 0.625q-0.1875 0.609375 -0.1875 1.328125l0 3.53125l-1.140625 0zm8.84462 -2.46875l1.125 0.140625q-0.171875 1.171875 -0.9375 1.828125q-0.765625 0.65625 -1.859375 0.65625q-1.390625 0 -2.234375 -0.90625q-0.828125 -0.90625 -0.828125 -2.59375q0 -1.09375 0.359375 -1.90625q0.359375 -0.828125 1.09375 -1.234375q0.734375 -0.40625 1.609375 -0.40625q1.09375 0 1.796875 0.5625q0.703125 0.546875 0.890625 1.5625l-1.109375 0.171875q-0.15625 -0.671875 -0.5625 -1.015625q-0.390625 -0.34375 -0.96875 -0.34375q-0.859375 0 -1.40625 0.625q-0.53125 0.609375 -0.53125 1.953125q0 1.359375 0.515625 1.984375q0.515625 0.609375 1.359375 0.609375q0.671875 0 1.125 -0.40625q0.453125 -0.421875 0.5625 -1.28125zm2.5390625 2.46875l0 -5.859375l-1.0 0l0 -0.875l1.0 0l0 -0.71875q0 -0.6875 0.125 -1.015625q0.171875 -0.4375 0.578125 -0.71875q0.421875 -0.28125 1.171875 -0.28125q0.484375 0 1.0625 0.125l-0.171875 0.984375q-0.359375 -0.0625 -0.671875 -0.0625q-0.515625 0 -0.734375 0.234375q-0.21875 0.21875 -0.21875 0.828125l0 0.625l1.3125 0l0 0.875l-1.3125 0l0 5.859375l-1.140625 0zm3.4373627 -7.984375l0 -1.328125l1.140625 0l0 1.328125l-1.140625 0zm0 7.984375l0 -6.734375l1.140625 0l0 6.734375l-1.140625 0zm2.92984 0l0 -9.3125l1.140625 0l0 9.3125l-1.140625 0zm7.601715 -2.171875l1.1875 0.140625q-0.28125 1.046875 -1.046875 1.625q-0.75 0.5625 -1.921875 0.5625q-1.484375 0 -2.359375 -0.90625q-0.859375 -0.921875 -0.859375 -2.5625q0 -1.703125 0.875 -2.640625q0.890625 -0.9375 2.28125 -0.9375q1.359375 0 2.203125 0.921875q0.859375 0.921875 0.859375 2.578125q0 0.109375 0 0.3125l-5.03125 0q0.0625 1.109375 0.625 1.703125q0.5625 0.59375 1.40625 0.59375q0.640625 0 1.078125 -0.328125q0.453125 -0.34375 0.703125 -1.0625zm-3.75 -1.84375l3.765625 0q-0.078125 -0.859375 -0.4375 -1.28125q-0.546875 -0.65625 -1.40625 -0.65625q-0.796875 0 -1.328125 0.53125q-0.53125 0.515625 -0.59375 1.40625zm10.256088 -3.96875l0 -1.328125l1.140625 0l0 1.328125l-1.140625 0zm0 7.984375l0 -6.734375l1.140625 0l0 6.734375l-1.140625 0zm2.96109 0l0 -6.734375l1.03125 0l0 0.953125q0.734375 -1.109375 2.140625 -1.109375q0.609375 0 1.109375 0.21875q0.515625 0.21875 0.765625 0.578125q0.265625 0.34375 0.359375 0.84375q0.0625 0.3125 0.0625 1.109375l0 4.140625l-1.140625 0l0 -4.09375q0 -0.703125 -0.140625 -1.046875q-0.125 -0.34375 -0.46875 -0.546875q-0.328125 -0.21875 -0.78125 -0.21875q-0.734375 0 -1.265625 0.46875q-0.53125 0.453125 -0.53125 1.75l0 3.6875l-1.140625 0zm13.615463 -1.015625l0.15625 1.0q-0.484375 0.109375 -0.859375 0.109375q-0.625 0 -0.96875 -0.203125q-0.34375 -0.203125 -0.484375 -0.515625q-0.140625 -0.328125 -0.140625 -1.34375l0 -3.890625l-0.828125 0l0 -0.875l0.828125 0l0 -1.671875l1.140625 -0.6875l0 2.359375l1.15625 0l0 0.875l-1.15625 0l0 3.953125q0 0.484375 0.0625 0.625q0.0625 0.140625 0.1875 0.21875q0.140625 0.078125 0.390625 0.078125q0.203125 0 0.515625 -0.03125zm1.1873627 1.015625l0 -6.734375l1.03125 0l0 1.015625q0.390625 -0.71875 0.71875 -0.9375q0.34375 -0.234375 0.734375 -0.234375q0.578125 0 1.171875 0.359375l-0.390625 1.0625q-0.421875 -0.25 -0.828125 -0.25q-0.375 0 -0.6875 0.234375q-0.296875 0.21875 -0.421875 0.625q-0.1875 0.609375 -0.1875 1.328125l0 3.53125l-1.140625 0zm9.06337 -2.171875l1.1875 0.140625q-0.28125 1.046875 -1.046875 1.625q-0.75 0.5625 -1.921875 0.5625q-1.484375 0 -2.359375 -0.90625q-0.859375 -0.921875 -0.859375 -2.5625q0 -1.703125 0.875 -2.640625q0.890625 -0.9375 2.28125 -0.9375q1.359375 0 2.203125 0.921875q0.859375 0.921875 0.859375 2.578125q0 0.109375 0 0.3125l-5.03125 0q0.0625 1.109375 0.625 1.703125q0.5625 0.59375 1.40625 0.59375q0.640625 0 1.078125 -0.328125q0.453125 -0.34375 0.703125 -1.0625zm-3.75 -1.84375l3.765625 0q-0.078125 -0.859375 -0.4375 -1.28125q-0.546875 -0.65625 -1.40625 -0.65625q-0.796875 0 -1.328125 0.53125q-0.53125 0.515625 -0.59375 1.40625zm11.162476 1.84375l1.1875 0.140625q-0.28125 1.046875 -1.046875 1.625q-0.75 0.5625 -1.921875 0.5625q-1.484375 0 -2.359375 -0.90625q-0.859375 -0.921875 -0.859375 -2.5625q0 -1.703125 0.875 -2.640625q0.890625 -0.9375 2.28125 -0.9375q1.359375 0 2.203125 0.921875q0.859375 0.921875 0.859375 2.578125q0 0.109375 0 0.3125l-5.03125 0q0.0625 1.109375 0.625 1.703125q0.5625 0.59375 1.40625 0.59375q0.640625 0 1.078125 -0.328125q0.453125 -0.34375 0.703125 -1.0625zm-3.75 -1.84375l3.765625 0q-0.078125 -0.859375 -0.4375 -1.28125q-0.546875 -0.65625 -1.40625 -0.65625q-0.796875 0 -1.328125 0.53125q-0.53125 0.515625 -0.59375 1.40625zm12.443588 6.75q-0.953125 -1.1875 -1.609375 -2.78125q-0.65625 -1.609375 -0.65625 -3.328125q0 -1.5 0.5 -2.890625q0.5625 -1.609375 1.765625 -3.203125l0.8125 0q-0.765625 1.328125 -1.015625 1.890625q-0.390625 0.875 -0.609375 1.828125q-0.265625 1.1875 -0.265625 2.390625q0 3.046875 1.890625 6.09375l-0.8125 0zm2.2508698 -10.71875l0 -1.328125l1.140625 0l0 1.328125l-1.140625 0zm0 7.984375l0 -6.734375l1.140625 0l0 6.734375l-1.140625 0zm3.226715 0l0 -5.859375l-1.0 0l0 -0.875l1.0 0l0 -0.71875q0 -0.6875 0.125 -1.015625q0.171875 -0.4375 0.578125 -0.71875q0.421875 -0.28125 1.171875 -0.28125q0.484375 0 1.0625 0.125l-0.171875 0.984375q-0.359375 -0.0625 -0.671875 -0.0625q-0.515625 0 -0.734375 0.234375q-0.21875 0.21875 -0.21875 0.828125l0 0.625l1.3125 0l0 0.875l-1.3125 0l0 5.859375l-1.140625 0zm7.1403503 2.578125l0 -9.3125l1.03125 0l0 0.875q0.375 -0.515625 0.828125 -0.765625q0.46875 -0.265625 1.140625 -0.265625q0.859375 0 1.515625 0.453125q0.65625 0.4375 0.984375 1.25q0.34375 0.796875 0.34375 1.765625q0 1.03125 -0.375 1.859375q-0.359375 0.828125 -1.078125 1.28125q-0.703125 0.4375 -1.484375 0.4375q-0.5625 0 -1.015625 -0.234375q-0.453125 -0.25 -0.75 -0.625l0 3.28125l-1.140625 0zm1.03125 -5.90625q0 1.296875 0.53125 1.921875q0.53125 0.625 1.265625 0.625q0.765625 0 1.3125 -0.640625q0.546875 -0.65625 0.546875 -2.0q0 -1.296875 -0.53125 -1.9375q-0.53125 -0.640625 -1.265625 -0.640625q-0.734375 0 -1.296875 0.6875q-0.5625 0.671875 -0.5625 1.984375zm6.3656006 3.328125l0 -6.734375l1.03125 0l0 1.015625q0.390625 -0.71875 0.71875 -0.9375q0.34375 -0.234375 0.734375 -0.234375q0.578125 0 1.171875 0.359375l-0.390625 1.0625q-0.421875 -0.25 -0.828125 -0.25q-0.375 0 -0.6875 0.234375q-0.296875 0.21875 -0.421875 0.625q-0.1875 0.609375 -0.1875 1.328125l0 3.53125l-1.140625 0zm9.06337 -2.171875l1.1875 0.140625q-0.28125 1.046875 -1.046875 1.625q-0.75 0.5625 -1.921875 0.5625q-1.484375 0 -2.359375 -0.90625q-0.859375 -0.921875 -0.859375 -2.5625q0 -1.703125 0.875 -2.640625q0.890625 -0.9375 2.28125 -0.9375q1.359375 0 2.203125 0.921875q0.859375 0.921875 0.859375 2.578125q0 0.109375 0 0.3125l-5.03125 0q0.0625 1.109375 0.625 1.703125q0.5625 0.59375 1.40625 0.59375q0.640625 0 1.078125 -0.328125q0.453125 -0.34375 0.703125 -1.0625zm-3.75 -1.84375l3.765625 0q-0.078125 -0.859375 -0.4375 -1.28125q-0.546875 -0.65625 -1.40625 -0.65625q-0.796875 0 -1.328125 0.53125q-0.53125 0.515625 -0.59375 1.40625zm6.0999756 2.0l1.125 -0.171875q0.09375 0.671875 0.53125 1.046875q0.4375 0.359375 1.21875 0.359375q0.78125 0 1.15625 -0.3125q0.390625 -0.328125 0.390625 -0.765625q0 -0.390625 -0.34375 -0.609375q-0.234375 -0.15625 -1.171875 -0.390625q-1.25 -0.3125 -1.734375 -0.546875q-0.484375 -0.234375 -0.734375 -0.640625q-0.25 -0.40625 -0.25 -0.90625q0 -0.453125 0.203125 -0.828125q0.203125 -0.390625 0.5625 -0.640625q0.265625 -0.203125 0.71875 -0.328125q0.46875 -0.140625 1.0 -0.140625q0.78125 0 1.375 0.234375q0.609375 0.21875 0.890625 0.609375q0.296875 0.390625 0.40625 1.046875l-1.125 0.15625q-0.078125 -0.53125 -0.4375 -0.8125q-0.359375 -0.296875 -1.03125 -0.296875q-0.78125 0 -1.125 0.265625q-0.34375 0.25 -0.34375 0.609375q0 0.21875 0.140625 0.390625q0.140625 0.1875 0.4375 0.3125q0.171875 0.0625 1.015625 0.28125q1.21875 0.328125 1.6875 0.53125q0.484375 0.203125 0.75 0.609375q0.28125 0.390625 0.28125 0.96875q0 0.578125 -0.34375 1.078125q-0.328125 0.5 -0.953125 0.78125q-0.625 0.28125 -1.421875 0.28125q-1.3125 0 -2.0 -0.546875q-0.6875 -0.546875 -0.875 -1.625zm11.726547 -0.15625l1.1875 0.140625q-0.28125 1.046875 -1.046875 1.625q-0.75 0.5625 -1.9218597 0.5625q-1.484375 0 -2.359375 -0.90625q-0.859375 -0.921875 -0.859375 -2.5625q0 -1.703125 0.875 -2.640625q0.890625 -0.9375 2.28125 -0.9375q1.3593597 0 2.2031097 0.921875q0.859375 0.921875 0.859375 2.578125q0 0.109375 0 0.3125l-5.0312347 0q0.0625 1.109375 0.625 1.703125q0.5625 0.59375 1.40625 0.59375q0.64060974 0 1.0781097 -0.328125q0.453125 -0.34375 0.703125 -1.0625zm-3.7499847 -1.84375l3.7656097 0q-0.078125 -0.859375 -0.4375 -1.28125q-0.546875 -0.65625 -1.4062347 -0.65625q-0.796875 0 -1.328125 0.53125q-0.53125 0.515625 -0.59375 1.40625zm6.5530853 4.015625l0 -6.734375l1.03125 0l0 0.953125q0.734375 -1.109375 2.140625 -1.109375q0.609375 0 1.109375 0.21875q0.515625 0.21875 0.765625 0.578125q0.265625 0.34375 0.359375 0.84375q0.0625 0.3125 0.0625 1.109375l0 4.140625l-1.140625 0l0 -4.09375q0 -0.703125 -0.140625 -1.046875q-0.125 -0.34375 -0.46875 -0.546875q-0.328125 -0.21875 -0.78125 -0.21875q-0.734375 0 -1.265625 0.46875q-0.53125 0.453125 -0.53125 1.75l0 3.6875l-1.140625 0zm9.912476 -1.015625l0.15625 1.0q-0.484375 0.109375 -0.859375 0.109375q-0.625 0 -0.96875 -0.203125q-0.34375 -0.203125 -0.484375 -0.515625q-0.140625 -0.328125 -0.140625 -1.34375l0 -3.890625l-0.828125 0l0 -0.875l0.828125 0l0 -1.671875l1.140625 -0.6875l0 2.359375l1.15625 0l0 0.875l-1.15625 0l0 3.953125q0 0.484375 0.0625 0.625q0.0625 0.140625 0.1875 0.21875q0.140625 0.078125 0.390625 0.078125q0.203125 0 0.515625 -0.03125zm1.9530029 3.75l-0.828125 0q1.90625 -3.046875 1.90625 -6.09375q0 -1.203125 -0.28125 -2.375q-0.203125 -0.953125 -0.59375 -1.828125q-0.25 -0.5625 -1.03125 -1.90625l0.828125 0q1.1875 1.59375 1.765625 3.203125q0.484375 1.390625 0.484375 2.890625q0 1.71875 -0.65625 3.328125q-0.65625 1.59375 -1.59375 2.78125zm8.625732 -2.734375l-2.0625 -6.734375l1.1875 0l1.078125 3.890625l0.390625 1.4375q0.03125 -0.109375 0.359375 -1.390625l1.0625 -3.9375l1.171875 0l1.015625 3.90625l0.34375 1.28125l0.375 -1.296875l1.15625 -3.890625l1.109375 0l-2.109375 6.734375l-1.171875 0l-1.078125 -4.03125l-0.265625 -1.15625l-1.359375 5.1875l-1.203125 0zm8.390778 -7.984375l0 -1.328125l1.140625 0l0 1.328125l-1.140625 0zm0 7.984375l0 -6.734375l1.140625 0l0 6.734375l-1.140625 0zm5.46109 -1.015625l0.15625 1.0q-0.484375 0.109375 -0.859375 0.109375q-0.625 0 -0.96875 -0.203125q-0.34375 -0.203125 -0.484375 -0.515625q-0.140625 -0.328125 -0.140625 -1.34375l0 -3.890625l-0.828125 0l0 -0.875l0.828125 0l0 -1.671875l1.140625 -0.6875l0 2.359375l1.15625 0l0 0.875l-1.15625 0l0 3.953125q0 0.484375 0.0625 0.625q0.0625 0.140625 0.1875 0.21875q0.140625 0.078125 0.390625 0.078125q0.203125 0 0.515625 -0.03125zm1.2029724 1.015625l0 -9.3125l1.140625 0l0 3.34375q0.796875 -0.921875 2.015625 -0.921875q0.75 0 1.296875 0.296875q0.5625 0.296875 0.796875 0.8125q0.234375 0.515625 0.234375 1.515625l0 4.265625l-1.140625 0l0 -4.265625q0 -0.859375 -0.375 -1.25q-0.359375 -0.390625 -1.046875 -0.390625q-0.5 0 -0.953125 0.265625q-0.453125 0.25 -0.640625 0.703125q-0.1875 0.453125 -0.1875 1.25l0 3.6875l-1.140625 0zm15.4904785 0l0 -0.84375q-0.640625 1.0 -1.890625 1.0q-0.796875 0 -1.484375 -0.4375q-0.671875 -0.453125 -1.046875 -1.25q-0.375 -0.796875 -0.375 -1.828125q0 -1.015625 0.34375 -1.828125q0.34375 -0.828125 1.015625 -1.265625q0.671875 -0.4375 1.5 -0.4375q0.609375 0 1.078125 0.265625q0.484375 0.25 0.78125 0.65625l0 -3.34375l1.140625 0l0 9.3125l-1.0625 0zm-3.609375 -3.359375q0 1.296875 0.53125 1.9375q0.546875 0.640625 1.296875 0.640625q0.75 0 1.265625 -0.609375q0.53125 -0.625 0.53125 -1.875q0 -1.390625 -0.53125 -2.03125q-0.53125 -0.65625 -1.3125 -0.65625q-0.765625 0 -1.28125 0.625q-0.5 0.625 -0.5 1.96875zm11.256226 1.1875l1.1875 0.140625q-0.28125 1.046875 -1.046875 1.625q-0.75 0.5625 -1.921875 0.5625q-1.484375 0 -2.359375 -0.90625q-0.859375 -0.921875 -0.859375 -2.5625q0 -1.703125 0.875 -2.640625q0.890625 -0.9375 2.28125 -0.9375q1.359375 0 2.203125 0.921875q0.859375 0.921875 0.859375 2.578125q0 0.109375 0 0.3125l-5.03125 0q0.0625 1.109375 0.625 1.703125q0.5625 0.59375 1.40625 0.59375q0.640625 0 1.078125 -0.328125q0.453125 -0.34375 0.703125 -1.0625zm-3.75 -1.84375l3.765625 0q-0.078125 -0.859375 -0.4375 -1.28125q-0.546875 -0.65625 -1.40625 -0.65625q-0.796875 0 -1.328125 0.53125q-0.53125 0.515625 -0.59375 1.40625zm6.8187256 4.015625l0 -5.859375l-1.0 0l0 -0.875l1.0 0l0 -0.71875q0 -0.6875 0.125 -1.015625q0.171875 -0.4375 0.578125 -0.71875q0.421875 -0.28125 1.171875 -0.28125q0.484375 0 1.0625 0.125l-0.171875 0.984375q-0.359375 -0.0625 -0.671875 -0.0625q-0.515625 0 -0.734375 0.234375q-0.21875 0.21875 -0.21875 0.828125l0 0.625l1.3125 0l0 0.875l-1.3125 0l0 5.859375l-1.140625 0zm7.8279724 -0.828125q-0.625 0.53125 -1.21875 0.765625q-0.578125 0.21875 -1.25 0.21875q-1.125 0 -1.71875 -0.546875q-0.59375 -0.546875 -0.59375 -1.390625q0 -0.484375 0.21875 -0.890625q0.234375 -0.421875 0.59375 -0.671875q0.375 -0.25 0.828125 -0.375q0.328125 -0.078125 1.015625 -0.171875q1.375 -0.15625 2.03125 -0.390625q0.015625 -0.234375 0.015625 -0.296875q0 -0.703125 -0.328125 -0.984375q-0.4375 -0.390625 -1.296875 -0.390625q-0.8125 0 -1.203125 0.28125q-0.375 0.28125 -0.5625 1.0l-1.109375 -0.140625q0.140625 -0.71875 0.484375 -1.15625q0.359375 -0.453125 1.015625 -0.6875q0.671875 -0.234375 1.53125 -0.234375q0.875 0 1.40625 0.203125q0.546875 0.203125 0.796875 0.515625q0.25 0.296875 0.359375 0.765625q0.046875 0.296875 0.046875 1.0625l0 1.515625q0 1.59375 0.078125 2.015625q0.078125 0.421875 0.28125 0.8125l-1.1875 0q-0.171875 -0.359375 -0.234375 -0.828125zm-0.09375 -2.5625q-0.625 0.265625 -1.859375 0.4375q-0.703125 0.109375 -1.0 0.234375q-0.296875 0.125 -0.453125 0.375q-0.15625 0.234375 -0.15625 0.53125q0 0.453125 0.34375 0.765625q0.34375 0.296875 1.015625 0.296875q0.65625 0 1.171875 -0.28125q0.515625 -0.296875 0.765625 -0.796875q0.171875 -0.375 0.171875 -1.140625l0 -0.421875zm7.5374756 3.390625l0 -0.984375q-0.796875 1.140625 -2.140625 1.140625q-0.59375 0 -1.125 -0.234375q-0.515625 -0.234375 -0.765625 -0.578125q-0.25 -0.34375 -0.34375 -0.84375q-0.078125 -0.328125 -0.078125 -1.0625l0 -4.171875l1.140625 0l0 3.734375q0 0.890625 0.078125 1.203125q0.109375 0.453125 0.453125 0.71875q0.34375 0.25 0.859375 0.25q0.515625 0 0.96875 -0.265625q0.453125 -0.265625 0.640625 -0.71875q0.1875 -0.453125 0.1875 -1.3125l0 -3.609375l1.140625 0l0 6.734375l-1.015625 0zm2.9593506 0l0 -9.3125l1.140625 0l0 9.3125l-1.140625 0zm5.49234 -1.015625l0.15625 1.0q-0.484375 0.109375 -0.859375 0.109375q-0.625 0 -0.96875 -0.203125q-0.34375 -0.203125 -0.484375 -0.515625q-0.140625 -0.328125 -0.140625 -1.34375l0 -3.890625l-0.828125 0l0 -0.875l0.828125 0l0 -1.671875l1.140625 -0.6875l0 2.359375l1.15625 0l0 0.875l-1.15625 0l0 3.953125q0 0.484375 0.0625 0.625q0.0625 0.140625 0.1875 0.21875q0.140625 0.078125 0.390625 0.078125q0.203125 0 0.515625 -0.03125zm0.7498779 -1.0l1.125 -0.171875q0.09375 0.671875 0.53125 1.046875q0.4375 0.359375 1.21875 0.359375q0.78125 0 1.15625 -0.3125q0.390625 -0.328125 0.390625 -0.765625q0 -0.390625 -0.34375 -0.609375q-0.234375 -0.15625 -1.171875 -0.390625q-1.25 -0.3125 -1.734375 -0.546875q-0.484375 -0.234375 -0.734375 -0.640625q-0.25 -0.40625 -0.25 -0.90625q0 -0.453125 0.203125 -0.828125q0.203125 -0.390625 0.5625 -0.640625q0.265625 -0.203125 0.71875 -0.328125q0.46875 -0.140625 1.0 -0.140625q0.78125 0 1.375 0.234375q0.609375 0.21875 0.890625 0.609375q0.296875 0.390625 0.40625 1.046875l-1.125 0.15625q-0.078125 -0.53125 -0.4375 -0.8125q-0.359375 -0.296875 -1.03125 -0.296875q-0.78125 0 -1.125 0.265625q-0.34375 0.25 -0.34375 0.609375q0 0.21875 0.140625 0.390625q0.140625 0.1875 0.4375 0.3125q0.171875 0.0625 1.015625 0.28125q1.21875 0.328125 1.6875 0.53125q0.484375 0.203125 0.75 0.609375q0.28125 0.390625 0.28125 0.96875q0 0.578125 -0.34375 1.078125q-0.328125 0.5 -0.953125 0.78125q-0.625 0.28125 -1.421875 0.28125q-1.3125 0 -2.0 -0.546875q-0.6875 -0.546875 -0.875 -1.625z" fill-rule="nonzero"></path><path fill="#cfe2f3" d="m57.730812 190.01724l325.92126 0l0 52.220474l-325.92126 0z" fill-rule="nonzero"></path><path fill="#0b5394" d="m133.92657 210.67247l1.6875 -0.140625q0.125 1.015625 0.5625 1.671875q0.4375 0.65625 1.359375 1.0625q0.9375 0.40625 2.09375 0.40625q1.03125 0 1.8125 -0.3125q0.796875 -0.3125 1.1875 -0.84375q0.390625 -0.53125 0.390625 -1.15625q0 -0.640625 -0.375 -1.109375q-0.375 -0.484375 -1.234375 -0.8125q-0.546875 -0.21875 -2.421875 -0.65625q-1.875 -0.453125 -2.625 -0.859375q-0.96875 -0.515625 -1.453125 -1.265625q-0.46875 -0.75 -0.46875 -1.6875q0 -1.03125 0.578125 -1.921875q0.59375 -0.90625 1.703125 -1.359375q1.125 -0.46875 2.5 -0.46875q1.515625 0 2.671875 0.484375q1.15625 0.484375 1.765625 1.4375q0.625 0.9375 0.671875 2.140625l-1.71875 0.125q-0.140625 -1.28125 -0.953125 -1.9375q-0.796875 -0.671875 -2.359375 -0.671875q-1.625 0 -2.375 0.609375q-0.75 0.59375 -0.75 1.4375q0 0.734375 0.53125 1.203125q0.515625 0.46875 2.703125 0.96875q2.203125 0.5 3.015625 0.875q1.1875 0.546875 1.75 1.390625q0.578125 0.828125 0.578125 1.921875q0 1.09375 -0.625 2.0625q-0.625 0.953125 -1.796875 1.484375q-1.15625 0.53125 -2.609375 0.53125q-1.84375 0 -3.09375 -0.53125q-1.25 -0.546875 -1.96875 -1.625q-0.703125 -1.078125 -0.734375 -2.453125zm19.271698 0.765625l1.640625 0.21875q-0.265625 1.6875 -1.375 2.65625q-1.109375 0.953125 -2.734375 0.953125q-2.015625 0 -3.25 -1.3125q-1.21875 -1.328125 -1.21875 -3.796875q0 -1.59375 0.515625 -2.78125q0.53125 -1.203125 1.609375 -1.796875q1.09375 -0.609375 2.359375 -0.609375q1.609375 0 2.625 0.8125q1.015625 0.8125 1.3125 2.3125l-1.625 0.25q-0.234375 -1.0 -0.828125 -1.5q-0.59375 -0.5 -1.421875 -0.5q-1.265625 0 -2.0625 0.90625q-0.78125 0.90625 -0.78125 2.859375q0 1.984375 0.765625 2.890625q0.765625 0.890625 1.984375 0.890625q0.984375 0 1.640625 -0.59375q0.65625 -0.609375 0.84375 -1.859375zm9.328125 2.390625q-0.9375 0.796875 -1.796875 1.125q-0.859375 0.3125 -1.84375 0.3125q-1.609375 0 -2.484375 -0.78125q-0.875 -0.796875 -0.875 -2.03125q0 -0.734375 0.328125 -1.328125q0.328125 -0.59375 0.859375 -0.953125q0.53125 -0.359375 1.203125 -0.546875q0.5 -0.140625 1.484375 -0.25q2.03125 -0.25 2.984375 -0.578125q0 -0.34375 0 -0.4375q0 -1.015625 -0.46875 -1.4375q-0.640625 -0.5625 -1.90625 -0.5625q-1.171875 0 -1.734375 0.40625q-0.5625 0.40625 -0.828125 1.46875l-1.640625 -0.234375q0.234375 -1.046875 0.734375 -1.6875q0.515625 -0.640625 1.46875 -0.984375q0.96875 -0.359375 2.25 -0.359375q1.265625 0 2.046875 0.296875q0.78125 0.296875 1.15625 0.75q0.375 0.453125 0.515625 1.140625q0.09375 0.421875 0.09375 1.53125l0 2.234375q0 2.328125 0.09375 2.953125q0.109375 0.609375 0.4375 1.171875l-1.75 0q-0.265625 -0.515625 -0.328125 -1.21875zm-0.140625 -3.71875q-0.90625 0.359375 -2.734375 0.625q-1.03125 0.140625 -1.453125 0.328125q-0.421875 0.1875 -0.65625 0.546875q-0.234375 0.359375 -0.234375 0.796875q0 0.671875 0.5 1.125q0.515625 0.4375 1.484375 0.4375q0.96875 0 1.71875 -0.421875q0.75 -0.4375 1.109375 -1.15625q0.265625 -0.578125 0.265625 -1.671875l0 -0.609375zm4.078842 4.9375l0 -9.859375l1.5 0l0 1.40625q1.09375 -1.625 3.140625 -1.625q0.890625 0 1.640625 0.328125q0.75 0.3125 1.109375 0.84375q0.375 0.515625 0.53125 1.21875q0.09375 0.46875 0.09375 1.625l0 6.0625l-1.671875 0l0 -6.0q0 -1.015625 -0.203125 -1.515625q-0.1875 -0.515625 -0.6875 -0.8125q-0.5 -0.296875 -1.171875 -0.296875q-1.0625 0 -1.84375 0.671875q-0.765625 0.671875 -0.765625 2.578125l0 5.375l-1.671875 0zm15.965271 0l0 -8.546875l-1.484375 0l0 -1.3125l1.484375 0l0 -1.046875q0 -0.984375 0.171875 -1.46875q0.234375 -0.65625 0.84375 -1.046875q0.609375 -0.40625 1.703125 -0.40625q0.703125 0 1.5625 0.15625l-0.25 1.46875q-0.515625 -0.09375 -0.984375 -0.09375q-0.765625 0 -1.078125 0.328125q-0.3125 0.3125 -0.3125 1.203125l0 0.90625l1.921875 0l0 1.3125l-1.921875 0l0 8.546875l-1.65625 0zm4.152054 -4.921875q0 -2.734375 1.53125 -4.0625q1.265625 -1.09375 3.09375 -1.09375q2.03125 0 3.3125 1.34375q1.296875 1.328125 1.296875 3.671875q0 1.90625 -0.578125 3.0q-0.5625 1.078125 -1.65625 1.6875q-1.078125 0.59375 -2.375 0.59375q-2.0625 0 -3.34375 -1.328125q-1.28125 -1.328125 -1.28125 -3.8125zm1.71875 0q0 1.890625 0.828125 2.828125q0.828125 0.9375 2.078125 0.9375q1.25 0 2.0625 -0.9375q0.828125 -0.953125 0.828125 -2.890625q0 -1.828125 -0.828125 -2.765625q-0.828125 -0.9375 -2.0625 -0.9375q-1.25 0 -2.078125 0.9375q-0.828125 0.9375 -0.828125 2.828125zm9.266342 4.921875l0 -9.859375l1.5 0l0 1.5q0.578125 -1.046875 1.0625 -1.375q0.484375 -0.34375 1.078125 -0.34375q0.84375 0 1.71875 0.546875l-0.578125 1.546875q-0.609375 -0.359375 -1.234375 -0.359375q-0.546875 0 -0.984375 0.328125q-0.421875 0.328125 -0.609375 0.90625q-0.28125 0.890625 -0.28125 1.953125l0 5.15625l-1.671875 0zm10.739731 -2.9375l1.65625 -0.265625q0.140625 1.0 0.765625 1.53125q0.640625 0.515625 1.78125 0.515625q1.15625 0 1.703125 -0.46875q0.5625 -0.46875 0.5625 -1.09375q0 -0.5625 -0.484375 -0.890625q-0.34375 -0.21875 -1.703125 -0.5625q-1.84375 -0.46875 -2.5625 -0.796875q-0.703125 -0.34375 -1.078125 -0.9375q-0.359375 -0.609375 -0.359375 -1.328125q0 -0.65625 0.296875 -1.21875q0.3125 -0.5625 0.828125 -0.9375q0.390625 -0.28125 1.0625 -0.484375q0.671875 -0.203125 1.4375 -0.203125q1.171875 0 2.046875 0.34375q0.875 0.328125 1.28125 0.90625q0.421875 0.5625 0.578125 1.515625l-1.625 0.21875q-0.109375 -0.75 -0.65625 -1.171875q-0.53125 -0.4375 -1.5 -0.4375q-1.15625 0 -1.640625 0.390625q-0.484375 0.375 -0.484375 0.875q0 0.328125 0.203125 0.59375q0.203125 0.265625 0.640625 0.4375q0.25 0.09375 1.46875 0.4375q1.765625 0.46875 2.46875 0.765625q0.703125 0.296875 1.09375 0.875q0.40625 0.578125 0.40625 1.4375q0 0.828125 -0.484375 1.578125q-0.484375 0.734375 -1.40625 1.140625q-0.921875 0.390625 -2.078125 0.390625q-1.921875 0 -2.9375 -0.796875q-1.0 -0.796875 -1.28125 -2.359375zm9.375 -1.984375q0 -2.734375 1.53125 -4.0625q1.265625 -1.09375 3.09375 -1.09375q2.03125 0 3.3125 1.34375q1.296875 1.328125 1.296875 3.671875q0 1.90625 -0.578125 3.0q-0.5625 1.078125 -1.65625 1.6875q-1.078125 0.59375 -2.375 0.59375q-2.0625 0 -3.34375 -1.328125q-1.28125 -1.328125 -1.28125 -3.8125zm1.71875 0q0 1.890625 0.828125 2.828125q0.828125 0.9375 2.078125 0.9375q1.25 0 2.0625 -0.9375q0.828125 -0.953125 0.828125 -2.890625q0 -1.828125 -0.828125 -2.765625q-0.828125 -0.9375 -2.0625 -0.9375q-1.25 0 -2.078125 0.9375q-0.828125 0.9375 -0.828125 2.828125zm15.735092 4.921875l0 -1.453125q-1.140625 1.671875 -3.125 1.671875q-0.859375 0 -1.625 -0.328125q-0.75 -0.34375 -1.125 -0.84375q-0.359375 -0.5 -0.515625 -1.234375q-0.09375 -0.5 -0.09375 -1.5625l0 -6.109375l1.671875 0l0 5.46875q0 1.3125 0.09375 1.765625q0.15625 0.65625 0.671875 1.03125q0.515625 0.375 1.265625 0.375q0.75 0 1.40625 -0.375q0.65625 -0.390625 0.921875 -1.046875q0.28125 -0.671875 0.28125 -1.9375l0 -5.28125l1.671875 0l0 9.859375l-1.5 0zm3.9069672 0l0 -9.859375l1.5 0l0 1.5q0.578125 -1.046875 1.0625 -1.375q0.484375 -0.34375 1.078125 -0.34375q0.84375 0 1.71875 0.546875l-0.578125 1.546875q-0.609375 -0.359375 -1.234375 -0.359375q-0.546875 0 -0.984375 0.328125q-0.421875 0.328125 -0.609375 0.90625q-0.28125 0.890625 -0.28125 1.953125l0 5.15625l-1.671875 0zm12.665802 -3.609375l1.640625 0.21875q-0.265625 1.6875 -1.375 2.65625q-1.109375 0.953125 -2.734375 0.953125q-2.015625 0 -3.25 -1.3125q-1.21875 -1.328125 -1.21875 -3.796875q0 -1.59375 0.515625 -2.78125q0.53125 -1.203125 1.609375 -1.796875q1.09375 -0.609375 2.359375 -0.609375q1.609375 0 2.625 0.8125q1.015625 0.8125 1.3125 2.3125l-1.625 0.25q-0.234375 -1.0 -0.828125 -1.5q-0.59375 -0.5 -1.421875 -0.5q-1.265625 0 -2.0625 0.90625q-0.78125 0.90625 -0.78125 2.859375q0 1.984375 0.765625 2.890625q0.765625 0.890625 1.984375 0.890625q0.984375 0 1.640625 -0.59375q0.65625 -0.609375 0.84375 -1.859375zm9.640625 0.4375l1.71875 0.21875q-0.40625 1.5 -1.515625 2.34375q-1.09375 0.828125 -2.8125 0.828125q-2.15625 0 -3.421875 -1.328125q-1.265625 -1.328125 -1.265625 -3.734375q0 -2.484375 1.265625 -3.859375q1.28125 -1.375 3.328125 -1.375q1.984375 0 3.234375 1.34375q1.25 1.34375 1.25 3.796875q0 0.140625 -0.015625 0.4375l-7.34375 0q0.09375 1.625 0.921875 2.484375q0.828125 0.859375 2.0625 0.859375q0.90625 0 1.546875 -0.46875q0.65625 -0.484375 1.046875 -1.546875zm-5.484375 -2.703125l5.5 0q-0.109375 -1.234375 -0.625 -1.859375q-0.796875 -0.96875 -2.078125 -0.96875q-1.140625 0 -1.9375 0.78125q-0.78125 0.765625 -0.859375 2.046875zm20.746521 5.875l0 -1.453125q-1.140625 1.671875 -3.125 1.671875q-0.859375 0 -1.625 -0.328125q-0.75 -0.34375 -1.125 -0.84375q-0.359375 -0.5 -0.515625 -1.234375q-0.09375 -0.5 -0.09375 -1.5625l0 -6.109375l1.671875 0l0 5.46875q0 1.3125 0.09375 1.765625q0.15625 0.65625 0.671875 1.03125q0.515625 0.375 1.265625 0.375q0.75 0 1.40625 -0.375q0.65625 -0.390625 0.921875 -1.046875q0.28125 -0.671875 0.28125 -1.9375l0 -5.28125l1.671875 0l0 9.859375l-1.5 0zm3.922577 0l0 -9.859375l1.5 0l0 1.40625q1.09375 -1.625 3.140625 -1.625q0.890625 0 1.640625 0.328125q0.75 0.3125 1.109375 0.84375q0.375 0.515625 0.53125 1.21875q0.09375 0.46875 0.09375 1.625l0 6.0625l-1.671875 0l0 -6.0q0 -1.015625 -0.203125 -1.515625q-0.1875 -0.515625 -0.6875 -0.8125q-0.5 -0.296875 -1.171875 -0.296875q-1.0625 0 -1.84375 0.671875q-0.765625 0.671875 -0.765625 2.578125l0 5.375l-1.671875 0zm10.391357 -11.6875l0 -1.90625l1.671875 0l0 1.90625l-1.671875 0zm0 11.6875l0 -9.859375l1.671875 0l0 9.859375l-1.671875 0zm7.785431 -1.5l0.234375 1.484375q-0.703125 0.140625 -1.265625 0.140625q-0.90625 0 -1.40625 -0.28125q-0.5 -0.296875 -0.703125 -0.75q-0.203125 -0.46875 -0.203125 -1.984375l0 -5.65625l-1.234375 0l0 -1.3125l1.234375 0l0 -2.4375l1.65625 -1.0l0 3.4375l1.6875 0l0 1.3125l-1.6875 0l0 5.75q0 0.71875 0.078125 0.921875q0.09375 0.203125 0.296875 0.328125q0.203125 0.125 0.578125 0.125q0.265625 0 0.734375 -0.078125zm0.8551941 -1.4375l1.65625 -0.265625q0.140625 1.0 0.765625 1.53125q0.640625 0.515625 1.78125 0.515625q1.15625 0 1.703125 -0.46875q0.5625 -0.46875 0.5625 -1.09375q0 -0.5625 -0.484375 -0.890625q-0.34375 -0.21875 -1.703125 -0.5625q-1.84375 -0.46875 -2.5625 -0.796875q-0.703125 -0.34375 -1.078125 -0.9375q-0.359375 -0.609375 -0.359375 -1.328125q0 -0.65625 0.296875 -1.21875q0.3125 -0.5625 0.828125 -0.9375q0.390625 -0.28125 1.0625 -0.484375q0.671875 -0.203125 1.4375 -0.203125q1.171875 0 2.046875 0.34375q0.875 0.328125 1.28125 0.90625q0.421875 0.5625 0.578125 1.515625l-1.625 0.21875q-0.109375 -0.75 -0.65625 -1.171875q-0.53125 -0.4375 -1.5 -0.4375q-1.15625 0 -1.640625 0.390625q-0.484375 0.375 -0.484375 0.875q0 0.328125 0.203125 0.59375q0.203125 0.265625 0.640625 0.4375q0.25 0.09375 1.46875 0.4375q1.765625 0.46875 2.46875 0.765625q0.703125 0.296875 1.09375 0.875q0.40625 0.578125 0.40625 1.4375q0 0.828125 -0.484375 1.578125q-0.484375 0.734375 -1.40625 1.140625q-0.921875 0.390625 -2.078125 0.390625q-1.921875 0 -2.9375 -0.796875q-1.0 -0.796875 -1.28125 -2.359375z" fill-rule="nonzero"></path><path fill="#0b5394" d="m70.19776 231.92747l0 -9.3125l3.203125 0q1.09375 0 1.65625 0.140625q0.8125 0.1875 1.375 0.671875q0.734375 0.609375 1.09375 1.578125q0.375 0.96875 0.375 2.21875q0 1.0625 -0.25 1.890625q-0.25 0.8125 -0.640625 1.34375q-0.390625 0.53125 -0.859375 0.84375q-0.453125 0.3125 -1.109375 0.46875q-0.640625 0.15625 -1.484375 0.15625l-3.359375 0zm1.234375 -1.09375l1.984375 0q0.921875 0 1.4375 -0.171875q0.53125 -0.171875 0.84375 -0.484375q0.4375 -0.4375 0.671875 -1.171875q0.25 -0.75 0.25 -1.796875q0 -1.46875 -0.484375 -2.25q-0.46875 -0.78125 -1.15625 -1.046875q-0.5 -0.1875 -1.59375 -0.1875l-1.953125 0l0 7.109375zm8.250153 -6.890625l0 -1.328125l1.140625 0l0 1.328125l-1.140625 0zm0 7.984375l0 -6.734375l1.140625 0l0 6.734375l-1.140625 0zm2.507965 -2.015625l1.125 -0.171875q0.09375 0.671875 0.53125 1.046875q0.4375 0.359375 1.21875 0.359375q0.78125 0 1.15625 -0.3125q0.390625 -0.328125 0.390625 -0.765625q0 -0.390625 -0.34375 -0.609375q-0.234375 -0.15625 -1.171875 -0.390625q-1.25 -0.3125 -1.734375 -0.546875q-0.484375 -0.234375 -0.734375 -0.640625q-0.25 -0.40625 -0.25 -0.90625q0 -0.453125 0.203125 -0.828125q0.203125 -0.390625 0.5625 -0.640625q0.265625 -0.203125 0.71875 -0.328125q0.46875 -0.140625 1.0 -0.140625q0.78125 0 1.375 0.234375q0.609375 0.21875 0.890625 0.609375q0.296875 0.390625 0.40625 1.046875l-1.125 0.15625q-0.078125 -0.53125 -0.4375 -0.8125q-0.359375 -0.296875 -1.03125 -0.296875q-0.78125 0 -1.125 0.265625q-0.34375 0.25 -0.34375 0.609375q0 0.21875 0.140625 0.390625q0.140625 0.1875 0.4375 0.3125q0.171875 0.0625 1.015625 0.28125q1.21875 0.328125 1.6875 0.53125q0.484375 0.203125 0.75 0.609375q0.28125 0.390625 0.28125 0.96875q0 0.578125 -0.34375 1.078125q-0.328125 0.5 -0.953125 0.78125q-0.625 0.28125 -1.421875 0.28125q-1.3125 0 -2.0 -0.546875q-0.6875 -0.546875 -0.875 -1.625zm11.5078125 -0.453125l1.125 0.140625q-0.171875 1.171875 -0.9375 1.828125q-0.765625 0.65625 -1.859375 0.65625q-1.390625 0 -2.234375 -0.90625q-0.828125 -0.90625 -0.828125 -2.59375q0 -1.09375 0.359375 -1.90625q0.359375 -0.828125 1.09375 -1.234375q0.734375 -0.40625 1.609375 -0.40625q1.09375 0 1.796875 0.5625q0.703125 0.546875 0.890625 1.5625l-1.109375 0.171875q-0.15625 -0.671875 -0.5625 -1.015625q-0.390625 -0.34375 -0.96875 -0.34375q-0.859375 0 -1.40625 0.625q-0.53125 0.609375 -0.53125 1.953125q0 1.359375 0.515625 1.984375q0.515625 0.609375 1.359375 0.609375q0.671875 0 1.125 -0.40625q0.453125 -0.421875 0.5625 -1.28125zm1.8515625 -0.90625q0 -1.875 1.03125 -2.765625q0.875 -0.75 2.125 -0.75q1.390625 0 2.265625 0.90625q0.890625 0.90625 0.890625 2.515625q0 1.296875 -0.390625 2.046875q-0.390625 0.75 -1.140625 1.171875q-0.75 0.40625 -1.625 0.40625q-1.421875 0 -2.296875 -0.90625q-0.859375 -0.90625 -0.859375 -2.625zm1.171875 0q0 1.296875 0.5625 1.953125q0.5625 0.640625 1.421875 0.640625q0.84375 0 1.40625 -0.640625q0.578125 -0.65625 0.578125 -1.984375q0 -1.25 -0.578125 -1.890625q-0.5625 -0.65625 -1.40625 -0.65625q-0.859375 0 -1.421875 0.640625q-0.5625 0.640625 -0.5625 1.9375zm8.537476 3.375l-2.5625 -6.734375l1.203125 0l1.4375 4.03125q0.234375 0.65625 0.4375 1.359375q0.15625 -0.53125 0.421875 -1.28125l1.5 -4.109375l1.171875 0l-2.546875 6.734375l-1.0625 0zm9.3984375 -2.171875l1.1875 0.140625q-0.28125 1.046875 -1.046875 1.625q-0.75 0.5625 -1.921875 0.5625q-1.484375 0 -2.359375 -0.90625q-0.859375 -0.921875 -0.859375 -2.5625q0 -1.703125 0.875 -2.640625q0.890625 -0.9375 2.28125 -0.9375q1.359375 0 2.203125 0.921875q0.859375 0.921875 0.859375 2.578125q0 0.109375 0 0.3125l-5.03125 0q0.0625 1.109375 0.625 1.703125q0.5625 0.59375 1.40625 0.59375q0.640625 0 1.078125 -0.328125q0.453125 -0.34375 0.703125 -1.0625zm-3.75 -1.84375l3.765625 0q-0.078125 -0.859375 -0.4375 -1.28125q-0.546875 -0.65625 -1.40625 -0.65625q-0.796875 0 -1.328125 0.53125q-0.53125 0.515625 -0.59375 1.40625zm6.5374756 4.015625l0 -6.734375l1.03125 0l0 1.015625q0.390625 -0.71875 0.71875 -0.9375q0.34375 -0.234375 0.734375 -0.234375q0.578125 0 1.171875 0.359375l-0.390625 1.0625q-0.421875 -0.25 -0.828125 -0.25q-0.375 0 -0.6875 0.234375q-0.296875 0.21875 -0.421875 0.625q-0.1875 0.609375 -0.1875 1.328125l0 3.53125l-1.140625 0zm8.156982 2.578125l0 -9.3125l1.03125 0l0 0.875q0.375 -0.515625 0.828125 -0.765625q0.46875 -0.265625 1.1406326 -0.265625q0.859375 0 1.515625 0.453125q0.65625 0.4375 0.984375 1.25q0.34375 0.796875 0.34375 1.765625q0 1.03125 -0.375 1.859375q-0.359375 0.828125 -1.078125 1.28125q-0.703125 0.4375 -1.484375 0.4375q-0.5625076 0 -1.0156326 -0.234375q-0.453125 -0.25 -0.75 -0.625l0 3.28125l-1.140625 0zm1.03125 -5.90625q0 1.296875 0.53125 1.921875q0.53125 0.625 1.2656326 0.625q0.765625 0 1.3125 -0.640625q0.546875 -0.65625 0.546875 -2.0q0 -1.296875 -0.53125 -1.9375q-0.53125 -0.640625 -1.265625 -0.640625q-0.7343826 0 -1.2968826 0.6875q-0.5625 0.671875 -0.5625 1.984375zm10.771858 2.5q-0.625 0.53125 -1.21875 0.765625q-0.578125 0.21875 -1.25 0.21875q-1.125 0 -1.71875 -0.546875q-0.59375 -0.546875 -0.59375 -1.390625q0 -0.484375 0.21875 -0.890625q0.234375 -0.421875 0.59375 -0.671875q0.375 -0.25 0.828125 -0.375q0.328125 -0.078125 1.015625 -0.171875q1.375 -0.15625 2.03125 -0.390625q0.015625 -0.234375 0.015625 -0.296875q0 -0.703125 -0.328125 -0.984375q-0.4375 -0.390625 -1.296875 -0.390625q-0.8125 0 -1.203125 0.28125q-0.375 0.28125 -0.5625 1.0l-1.109375 -0.140625q0.140625 -0.71875 0.484375 -1.15625q0.359375 -0.453125 1.015625 -0.6875q0.671875 -0.234375 1.53125 -0.234375q0.875 0 1.40625 0.203125q0.546875 0.203125 0.796875 0.515625q0.25 0.296875 0.359375 0.765625q0.046875 0.296875 0.046875 1.0625l0 1.515625q0 1.59375 0.078125 2.015625q0.078125 0.421875 0.28125 0.8125l-1.1875 0q-0.171875 -0.359375 -0.234375 -0.828125zm-0.09375 -2.5625q-0.625 0.265625 -1.859375 0.4375q-0.703125 0.109375 -1.0 0.234375q-0.296875 0.125 -0.453125 0.375q-0.15625 0.234375 -0.15625 0.53125q0 0.453125 0.34375 0.765625q0.34375 0.296875 1.015625 0.296875q0.65625 0 1.171875 -0.28125q0.515625 -0.296875 0.765625 -0.796875q0.171875 -0.375 0.171875 -1.140625l0 -0.421875zm7.5062256 0.921875l1.125 0.140625q-0.171875 1.171875 -0.9375 1.828125q-0.765625 0.65625 -1.859375 0.65625q-1.390625 0 -2.234375 -0.90625q-0.828125 -0.90625 -0.828125 -2.59375q0 -1.09375 0.359375 -1.90625q0.359375 -0.828125 1.09375 -1.234375q0.734375 -0.40625 1.609375 -0.40625q1.09375 0 1.796875 0.5625q0.703125 0.546875 0.890625 1.5625l-1.109375 0.171875q-0.15625 -0.671875 -0.5625 -1.015625q-0.390625 -0.34375 -0.96875 -0.34375q-0.859375 0 -1.40625 0.625q-0.53125 0.609375 -0.53125 1.953125q0 1.359375 0.515625 1.984375q0.515625 0.609375 1.359375 0.609375q0.671875 0 1.125 -0.40625q0.453125 -0.421875 0.5625 -1.28125zm2.2734375 2.46875l0 -9.3125l1.140625 0l0 5.3125l2.703125 -2.734375l1.484375 0l-2.578125 2.5l2.84375 4.234375l-1.40625 0l-2.234375 -3.453125l-0.8125 0.78125l0 2.671875l-1.140625 0zm11.0546875 -0.828125q-0.625 0.53125 -1.21875 0.765625q-0.578125 0.21875 -1.25 0.21875q-1.125 0 -1.71875 -0.546875q-0.59375 -0.546875 -0.59375 -1.390625q0 -0.484375 0.21875 -0.890625q0.234375 -0.421875 0.59375 -0.671875q0.375 -0.25 0.828125 -0.375q0.328125 -0.078125 1.015625 -0.171875q1.375 -0.15625 2.03125 -0.390625q0.015625 -0.234375 0.015625 -0.296875q0 -0.703125 -0.328125 -0.984375q-0.4375 -0.390625 -1.296875 -0.390625q-0.8125 0 -1.203125 0.28125q-0.375 0.28125 -0.5625 1.0l-1.109375 -0.140625q0.140625 -0.71875 0.484375 -1.15625q0.359375 -0.453125 1.015625 -0.6875q0.671875 -0.234375 1.53125 -0.234375q0.875 0 1.40625 0.203125q0.546875 0.203125 0.796875 0.515625q0.25 0.296875 0.359375 0.765625q0.046875 0.296875 0.046875 1.0625l0 1.515625q0 1.59375 0.078125 2.015625q0.078125 0.421875 0.28125 0.8125l-1.1875 0q-0.171875 -0.359375 -0.234375 -0.828125zm-0.09375 -2.5625q-0.625 0.265625 -1.859375 0.4375q-0.703125 0.109375 -1.0 0.234375q-0.296875 0.125 -0.453125 0.375q-0.15625 0.234375 -0.15625 0.53125q0 0.453125 0.34375 0.765625q0.34375 0.296875 1.015625 0.296875q0.65625 0 1.171875 -0.28125q0.515625 -0.296875 0.765625 -0.796875q0.171875 -0.375 0.171875 -1.140625l0 -0.421875zm2.8968506 3.953125l1.125 0.15625q0.0625 0.515625 0.375 0.75q0.4375 0.328125 1.171875 0.328125q0.78125 0 1.21875 -0.328125q0.4375 -0.3125 0.578125 -0.890625q0.09375 -0.34375 0.09375 -1.453125q-0.75 0.875 -1.875 0.875q-1.390625 0 -2.15625 -1.0q-0.75 -1.0 -0.75 -2.40625q0 -0.96875 0.34375 -1.78125q0.359375 -0.8125 1.015625 -1.25q0.65625 -0.453125 1.5625 -0.453125q1.1875 0 1.96875 0.96875l0 -0.8125l1.046875 0l0 5.8125q0 1.578125 -0.328125 2.234375q-0.3125 0.65625 -1.015625 1.03125q-0.6875 0.390625 -1.703125 0.390625q-1.203125 0 -1.953125 -0.546875q-0.734375 -0.53125 -0.71875 -1.625zm0.953125 -4.046875q0 1.3125 0.515625 1.921875q0.53125 0.609375 1.328125 0.609375q0.796875 0 1.328125 -0.59375q0.53125 -0.609375 0.53125 -1.90625q0 -1.234375 -0.546875 -1.859375q-0.546875 -0.640625 -1.328125 -0.640625q-0.765625 0 -1.296875 0.625q-0.53125 0.625 -0.53125 1.84375zm11.287476 1.3125l1.1875 0.140625q-0.28125 1.046875 -1.046875 1.625q-0.75 0.5625 -1.921875 0.5625q-1.484375 0 -2.359375 -0.90625q-0.859375 -0.921875 -0.859375 -2.5625q0 -1.703125 0.875 -2.640625q0.890625 -0.9375 2.28125 -0.9375q1.359375 0 2.203125 0.921875q0.859375 0.921875 0.859375 2.578125q0 0.109375 0 0.3125l-5.03125 0q0.0625 1.109375 0.625 1.703125q0.5625 0.59375 1.40625 0.59375q0.640625 0 1.078125 -0.328125q0.453125 -0.34375 0.703125 -1.0625zm-3.75 -1.84375l3.765625 0q-0.078125 -0.859375 -0.4375 -1.28125q-0.546875 -0.65625 -1.40625 -0.65625q-0.796875 0 -1.328125 0.53125q-0.53125 0.515625 -0.59375 1.40625zm6.0999756 2.0l1.125 -0.171875q0.09375 0.671875 0.53125 1.046875q0.4375 0.359375 1.21875 0.359375q0.78125 0 1.15625 -0.3125q0.390625 -0.328125 0.390625 -0.765625q0 -0.390625 -0.34375 -0.609375q-0.234375 -0.15625 -1.171875 -0.390625q-1.25 -0.3125 -1.734375 -0.546875q-0.484375 -0.234375 -0.734375 -0.640625q-0.25 -0.40625 -0.25 -0.90625q0 -0.453125 0.203125 -0.828125q0.203125 -0.390625 0.5625 -0.640625q0.265625 -0.203125 0.71875 -0.328125q0.46875 -0.140625 1.0 -0.140625q0.78125 0 1.375 0.234375q0.609375 0.21875 0.890625 0.609375q0.296875 0.390625 0.40625 1.046875l-1.125 0.15625q-0.078125 -0.53125 -0.4375 -0.8125q-0.359375 -0.296875 -1.03125 -0.296875q-0.78125 0 -1.125 0.265625q-0.34375 0.25 -0.34375 0.609375q0 0.21875 0.140625 0.390625q0.140625 0.1875 0.4375 0.3125q0.171875 0.0625 1.015625 0.28125q1.21875 0.328125 1.6875 0.53125q0.484375 0.203125 0.75 0.609375q0.28125 0.390625 0.28125 0.96875q0 0.578125 -0.34375 1.078125q-0.328125 0.5 -0.953125 0.78125q-0.625 0.28125 -1.421875 0.28125q-1.3125 0 -2.0 -0.546875q-0.6875 -0.546875 -0.875 -1.625zm13.007675 4.75q-0.953125 -1.1875 -1.609375 -2.78125q-0.65625 -1.609375 -0.65625 -3.328125q0 -1.5 0.5 -2.890625q0.5625 -1.609375 1.765625 -3.203125l0.8125 0q-0.765625 1.328125 -1.015625 1.890625q-0.390625 0.875 -0.609375 1.828125q-0.265625 1.1875 -0.265625 2.390625q0 3.046875 1.890625 6.09375l-0.8125 0zm2.2508698 -0.15625l0 -9.3125l1.03125 0l0 0.875q0.375 -0.515625 0.828125 -0.765625q0.46875 -0.265625 1.140625 -0.265625q0.859375 0 1.515625 0.453125q0.65625 0.4375 0.984375 1.25q0.34375 0.796875 0.34375 1.765625q0 1.03125 -0.375 1.859375q-0.359375 0.828125 -1.078125 1.28125q-0.703125 0.4375 -1.484375 0.4375q-0.5625 0 -1.015625 -0.234375q-0.453125 -0.25 -0.75 -0.625l0 3.28125l-1.140625 0zm1.03125 -5.90625q0 1.296875 0.53125 1.921875q0.53125 0.625 1.265625 0.625q0.765625 0 1.3125 -0.640625q0.546875 -0.65625 0.546875 -2.0q0 -1.296875 -0.53125 -1.9375q-0.53125 -0.640625 -1.265625 -0.640625q-0.734375 0 -1.296875 0.6875q-0.5625 0.671875 -0.5625 1.984375zm10.771851 2.5q-0.625 0.53125 -1.21875 0.765625q-0.578125 0.21875 -1.25 0.21875q-1.125 0 -1.71875 -0.546875q-0.59375 -0.546875 -0.59375 -1.390625q0 -0.484375 0.21875 -0.890625q0.234375 -0.421875 0.59375 -0.671875q0.375 -0.25 0.828125 -0.375q0.328125 -0.078125 1.015625 -0.171875q1.375 -0.15625 2.03125 -0.390625q0.015625 -0.234375 0.015625 -0.296875q0 -0.703125 -0.328125 -0.984375q-0.4375 -0.390625 -1.296875 -0.390625q-0.8125 0 -1.203125 0.28125q-0.375 0.28125 -0.5625 1.0l-1.109375 -0.140625q0.140625 -0.71875 0.484375 -1.15625q0.359375 -0.453125 1.015625 -0.6875q0.671875 -0.234375 1.53125 -0.234375q0.875 0 1.40625 0.203125q0.546875 0.203125 0.796875 0.515625q0.25 0.296875 0.359375 0.765625q0.046875 0.296875 0.046875 1.0625l0 1.515625q0 1.59375 0.078125 2.015625q0.078125 0.421875 0.28125 0.8125l-1.1875 0q-0.171875 -0.359375 -0.234375 -0.828125zm-0.09375 -2.5625q-0.625 0.265625 -1.859375 0.4375q-0.703125 0.109375 -1.0 0.234375q-0.296875 0.125 -0.453125 0.375q-0.15625 0.234375 -0.15625 0.53125q0 0.453125 0.34375 0.765625q0.34375 0.296875 1.015625 0.296875q0.65625 0 1.171875 -0.28125q0.515625 -0.296875 0.765625 -0.796875q0.171875 -0.375 0.171875 -1.140625l0 -0.421875zm7.5062256 0.921875l1.125 0.140625q-0.171875 1.171875 -0.9375 1.828125q-0.765625 0.65625 -1.859375 0.65625q-1.390625 0 -2.234375 -0.90625q-0.828125 -0.90625 -0.828125 -2.59375q0 -1.09375 0.359375 -1.90625q0.359375 -0.828125 1.09375 -1.234375q0.734375 -0.40625 1.609375 -0.40625q1.09375 0 1.796875 0.5625q0.703125 0.546875 0.890625 1.5625l-1.109375 0.171875q-0.15625 -0.671875 -0.5625 -1.015625q-0.390625 -0.34375 -0.96875 -0.34375q-0.859375 0 -1.40625 0.625q-0.53125 0.609375 -0.53125 1.953125q0 1.359375 0.515625 1.984375q0.515625 0.609375 1.359375 0.609375q0.671875 0 1.125 -0.40625q0.453125 -0.421875 0.5625 -1.28125zm2.2734375 2.46875l0 -9.3125l1.140625 0l0 5.3125l2.703125 -2.734375l1.484375 0l-2.578125 2.5l2.84375 4.234375l-1.40625 0l-2.234375 -3.453125l-0.8125 0.78125l0 2.671875l-1.140625 0zm11.0546875 -0.828125q-0.625 0.53125 -1.21875 0.765625q-0.578125 0.21875 -1.25 0.21875q-1.125 0 -1.71875 -0.546875q-0.59375 -0.546875 -0.59375 -1.390625q0 -0.484375 0.21875 -0.890625q0.234375 -0.421875 0.59375 -0.671875q0.375 -0.25 0.828125 -0.375q0.328125 -0.078125 1.015625 -0.171875q1.375 -0.15625 2.03125 -0.390625q0.015625 -0.234375 0.015625 -0.296875q0 -0.703125 -0.328125 -0.984375q-0.4375 -0.390625 -1.296875 -0.390625q-0.8125 0 -1.203125 0.28125q-0.375 0.28125 -0.5625 1.0l-1.109375 -0.140625q0.140625 -0.71875 0.484375 -1.15625q0.359375 -0.453125 1.015625 -0.6875q0.671875 -0.234375 1.53125 -0.234375q0.875 0 1.40625 0.203125q0.546875 0.203125 0.796875 0.515625q0.25 0.296875 0.359375 0.765625q0.046875 0.296875 0.046875 1.0625l0 1.515625q0 1.59375 0.078125 2.015625q0.078125 0.421875 0.28125 0.8125l-1.1875 0q-0.171875 -0.359375 -0.234375 -0.828125zm-0.09375 -2.5625q-0.625 0.265625 -1.859375 0.4375q-0.703125 0.109375 -1.0 0.234375q-0.296875 0.125 -0.453125 0.375q-0.15625 0.234375 -0.15625 0.53125q0 0.453125 0.34375 0.765625q0.34375 0.296875 1.015625 0.296875q0.65625 0 1.171875 -0.28125q0.515625 -0.296875 0.765625 -0.796875q0.171875 -0.375 0.171875 -1.140625l0 -0.421875zm2.8968506 3.953125l1.125 0.15625q0.0625 0.515625 0.375 0.75q0.4375 0.328125 1.171875 0.328125q0.78125 0 1.21875 -0.328125q0.4375 -0.3125 0.578125 -0.890625q0.09375 -0.34375 0.09375 -1.453125q-0.75 0.875 -1.875 0.875q-1.390625 0 -2.15625 -1.0q-0.75 -1.0 -0.75 -2.40625q0 -0.96875 0.34375 -1.78125q0.359375 -0.8125 1.015625 -1.25q0.65625 -0.453125 1.5625 -0.453125q1.1875 0 1.96875 0.96875l0 -0.8125l1.046875 0l0 5.8125q0 1.578125 -0.328125 2.234375q-0.3125 0.65625 -1.015625 1.03125q-0.6875 0.390625 -1.703125 0.390625q-1.203125 0 -1.953125 -0.546875q-0.734375 -0.53125 -0.71875 -1.625zm0.953125 -4.046875q0 1.3125 0.515625 1.921875q0.53125 0.609375 1.328125 0.609375q0.796875 0 1.328125 -0.59375q0.53125 -0.609375 0.53125 -1.90625q0 -1.234375 -0.546875 -1.859375q-0.546875 -0.640625 -1.328125 -0.640625q-0.765625 0 -1.296875 0.625q-0.53125 0.625 -0.53125 1.84375zm11.287476 1.3125l1.1875 0.140625q-0.28125 1.046875 -1.046875 1.625q-0.75 0.5625 -1.921875 0.5625q-1.484375 0 -2.359375 -0.90625q-0.859375 -0.921875 -0.859375 -2.5625q0 -1.703125 0.875 -2.640625q0.890625 -0.9375 2.28125 -0.9375q1.359375 0 2.203125 0.921875q0.859375 0.921875 0.859375 2.578125q0 0.109375 0 0.3125l-5.03125 0q0.0625 1.109375 0.625 1.703125q0.5625 0.59375 1.40625 0.59375q0.640625 0 1.078125 -0.328125q0.453125 -0.34375 0.703125 -1.0625zm-3.75 -1.84375l3.765625 0q-0.078125 -0.859375 -0.4375 -1.28125q-0.546875 -0.65625 -1.40625 -0.65625q-0.796875 0 -1.328125 0.53125q-0.53125 0.515625 -0.59375 1.40625zm6.8812256 4.015625l0 -1.296875l1.296875 0l0 1.296875l-1.296875 0zm3.3592377 -7.984375l0 -1.328125l1.15625 0l0 1.328125l-1.15625 0zm-1.4375 10.59375l0.21875 -0.96875q0.34375 0.09375 0.53125 0.09375q0.359375 0 0.515625 -0.234375q0.171875 -0.234375 0.171875 -1.15625l0 -7.078125l1.15625 0l0 7.109375q0 1.234375 -0.328125 1.71875q-0.421875 0.640625 -1.375 0.640625q-0.46875 0 -0.890625 -0.125zm3.96109 -4.625l1.125 -0.171875q0.09375 0.671875 0.53125 1.046875q0.4375 0.359375 1.21875 0.359375q0.78125 0 1.15625 -0.3125q0.390625 -0.328125 0.390625 -0.765625q0 -0.390625 -0.34375 -0.609375q-0.234375 -0.15625 -1.171875 -0.390625q-1.25 -0.3125 -1.734375 -0.546875q-0.484375 -0.234375 -0.734375 -0.640625q-0.25 -0.40625 -0.25 -0.90625q0 -0.453125 0.203125 -0.828125q0.203125 -0.390625 0.5625 -0.640625q0.265625 -0.203125 0.71875 -0.328125q0.46875 -0.140625 1.0 -0.140625q0.78125 0 1.375 0.234375q0.609375 0.21875 0.890625 0.609375q0.296875 0.390625 0.40625 1.046875l-1.125 0.15625q-0.078125 -0.53125 -0.4375 -0.8125q-0.359375 -0.296875 -1.03125 -0.296875q-0.78125 0 -1.125 0.265625q-0.34375 0.25 -0.34375 0.609375q0 0.21875 0.140625 0.390625q0.140625 0.1875 0.4375 0.3125q0.171875 0.0625 1.015625 0.28125q1.21875 0.328125 1.6875 0.53125q0.484375 0.203125 0.75 0.609375q0.28125 0.390625 0.28125 0.96875q0 0.578125 -0.34375 1.078125q-0.328125 0.5 -0.953125 0.78125q-0.625 0.28125 -1.421875 0.28125q-1.3125 0 -2.0 -0.546875q-0.6875 -0.546875 -0.875 -1.625zm6.6953125 -1.359375q0 -1.875 1.03125 -2.765625q0.875 -0.75 2.125 -0.75q1.390625 0 2.265625 0.90625q0.890625 0.90625 0.890625 2.515625q0 1.296875 -0.390625 2.046875q-0.390625 0.75 -1.140625 1.171875q-0.75 0.40625 -1.625 0.40625q-1.421875 0 -2.296875 -0.90625q-0.859375 -0.90625 -0.859375 -2.625zm1.171875 0q0 1.296875 0.5625 1.953125q0.5625 0.640625 1.421875 0.640625q0.84375 0 1.40625 -0.640625q0.578125 -0.65625 0.578125 -1.984375q0 -1.25 -0.578125 -1.890625q-0.5625 -0.65625 -1.40625 -0.65625q-0.859375 0 -1.421875 0.640625q-0.5625 0.640625 -0.5625 1.9375zm6.6624756 3.375l0 -6.734375l1.03125 0l0 0.953125q0.734375 -1.109375 2.140625 -1.109375q0.609375 0 1.109375 0.21875q0.515625 0.21875 0.765625 0.578125q0.265625 0.34375 0.359375 0.84375q0.0625 0.3125 0.0625 1.109375l0 4.140625l-1.140625 0l0 -4.09375q0 -0.703125 -0.140625 -1.046875q-0.125 -0.34375 -0.46875 -0.546875q-0.328125 -0.21875 -0.78125 -0.21875q-0.734375 0 -1.265625 0.46875q-0.53125 0.453125 -0.53125 1.75l0 3.6875l-1.140625 0zm7.7093506 0l0 -1.296875l1.296875 0l0 1.296875q0 0.71875 -0.25 1.15625q-0.25 0.4375 -0.8125 0.6875l-0.3125 -0.484375q0.359375 -0.171875 0.53125 -0.484375q0.171875 -0.296875 0.1875 -0.875l-0.640625 0zm6.6559753 -7.59375l0.296875 -0.90625q1.0 0.359375 1.46875 0.609375q-0.125 -1.140625 -0.140625 -1.578125l0.921875 0q-0.015625 0.625 -0.140625 1.578125q0.65625 -0.328125 1.5 -0.609375l0.296875 0.90625q-0.8125 0.265625 -1.59375 0.34375q0.390625 0.34375 1.09375 1.203125l-0.75 0.546875q-0.375 -0.5 -0.875 -1.375q-0.46875 0.90625 -0.828125 1.375l-0.75 -0.546875q0.734375 -0.90625 1.0625 -1.203125q-0.828125 -0.15625 -1.5625 -0.34375zm5.9680176 7.59375l0 -1.296875l1.296875 0l0 1.296875l-1.296875 0zm3.156128 0.5625l1.125 0.15625q0.0625 0.515625 0.375 0.75q0.4375 0.328125 1.171875 0.328125q0.78125 0 1.21875 -0.328125q0.4375 -0.3125 0.578125 -0.890625q0.09375 -0.34375 0.09375 -1.453125q-0.75 0.875 -1.875 0.875q-1.390625 0 -2.15625 -1.0q-0.75 -1.0 -0.75 -2.40625q0 -0.96875 0.34375 -1.78125q0.359375 -0.8125 1.015625 -1.25q0.65625 -0.453125 1.5625 -0.453125q1.1875 0 1.96875 0.96875l0 -0.8125l1.046875 0l0 5.8125q0 1.578125 -0.328125 2.234375q-0.3125 0.65625 -1.015625 1.03125q-0.6875 0.390625 -1.703125 0.390625q-1.203125 0 -1.953125 -0.546875q-0.734375 -0.53125 -0.71875 -1.625zm0.953125 -4.046875q0 1.3125 0.515625 1.921875q0.53125 0.609375 1.328125 0.609375q0.796875 0 1.328125 -0.59375q0.53125 -0.609375 0.53125 -1.90625q0 -1.234375 -0.546875 -1.859375q-0.546875 -0.640625 -1.328125 -0.640625q-0.765625 0 -1.296875 0.625q-0.53125 0.625 -0.53125 1.84375zm11.287476 1.3125l1.1875 0.140625q-0.28125 1.046875 -1.046875 1.625q-0.75 0.5625 -1.921875 0.5625q-1.484375 0 -2.359375 -0.90625q-0.859375 -0.921875 -0.859375 -2.5625q0 -1.703125 0.875 -2.640625q0.890625 -0.9375 2.28125 -0.9375q1.359375 0 2.203125 0.921875q0.859375 0.921875 0.859375 2.578125q0 0.109375 0 0.3125l-5.03125 0q0.0625 1.109375 0.625 1.703125q0.5625 0.59375 1.40625 0.59375q0.640625 0 1.078125 -0.328125q0.453125 -0.34375 0.703125 -1.0625zm-3.75 -1.84375l3.765625 0q-0.078125 -0.859375 -0.4375 -1.28125q-0.546875 -0.65625 -1.40625 -0.65625q-0.796875 0 -1.328125 0.53125q-0.53125 0.515625 -0.59375 1.40625zm6.5531006 4.015625l0 -6.734375l1.015625 0l0 0.9375q0.328125 -0.5 0.84375 -0.796875q0.53125 -0.296875 1.203125 -0.296875q0.75 0 1.21875 0.3125q0.484375 0.3125 0.6875 0.859375q0.796875 -1.171875 2.078125 -1.171875q1.0 0 1.53125 0.5625q0.546875 0.546875 0.546875 1.703125l0 4.625l-1.125 0l0 -4.25q0 -0.6875 -0.109375 -0.984375q-0.109375 -0.296875 -0.40625 -0.484375q-0.296875 -0.1875 -0.6875 -0.1875q-0.71875 0 -1.1875 0.484375q-0.46875 0.46875 -0.46875 1.5l0 3.921875l-1.140625 0l0 -4.375q0 -0.765625 -0.28125 -1.140625q-0.28125 -0.390625 -0.90625 -0.390625q-0.484375 0 -0.890625 0.265625q-0.40625 0.25 -0.59375 0.734375q-0.1875 0.484375 -0.1875 1.40625l0 3.5l-1.140625 0zm10.649292 -2.015625l1.125 -0.171875q0.09375 0.671875 0.53125 1.046875q0.4375 0.359375 1.21875 0.359375q0.78125 0 1.15625 -0.3125q0.390625 -0.328125 0.390625 -0.765625q0 -0.390625 -0.34375 -0.609375q-0.234375 -0.15625 -1.171875 -0.390625q-1.25 -0.3125 -1.734375 -0.546875q-0.484375 -0.234375 -0.734375 -0.640625q-0.25 -0.40625 -0.25 -0.90625q0 -0.453125 0.203125 -0.828125q0.203125 -0.390625 0.5625 -0.640625q0.265625 -0.203125 0.71875 -0.328125q0.46875 -0.140625 1.0 -0.140625q0.78125 0 1.375 0.234375q0.609375 0.21875 0.890625 0.609375q0.296875 0.390625 0.40625 1.046875l-1.125 0.15625q-0.078125 -0.53125 -0.4375 -0.8125q-0.359375 -0.296875 -1.03125 -0.296875q-0.78125 0 -1.125 0.265625q-0.34375 0.25 -0.34375 0.609375q0 0.21875 0.140625 0.390625q0.140625 0.1875 0.4375 0.3125q0.171875 0.0625 1.015625 0.28125q1.21875 0.328125 1.6875 0.53125q0.484375 0.203125 0.75 0.609375q0.28125 0.390625 0.28125 0.96875q0 0.578125 -0.34375 1.078125q-0.328125 0.5 -0.953125 0.78125q-0.625 0.28125 -1.421875 0.28125q-1.3125 0 -2.0 -0.546875q-0.6875 -0.546875 -0.875 -1.625zm7.1171875 4.59375l0 -9.3125l1.03125 0l0 0.875q0.375 -0.515625 0.828125 -0.765625q0.46875 -0.265625 1.140625 -0.265625q0.859375 0 1.515625 0.453125q0.65625 0.4375 0.984375 1.25q0.34375 0.796875 0.34375 1.765625q0 1.03125 -0.375 1.859375q-0.359375 0.828125 -1.078125 1.28125q-0.703125 0.4375 -1.484375 0.4375q-0.5625 0 -1.015625 -0.234375q-0.453125 -0.25 -0.75 -0.625l0 3.28125l-1.140625 0zm1.03125 -5.90625q0 1.296875 0.53125 1.921875q0.53125 0.625 1.265625 0.625q0.765625 0 1.3125 -0.640625q0.546875 -0.65625 0.546875 -2.0q0 -1.296875 -0.53125 -1.9375q-0.53125 -0.640625 -1.265625 -0.640625q-0.734375 0 -1.296875 0.6875q-0.5625 0.671875 -0.5625 1.984375zm10.990601 1.15625l1.1875 0.140625q-0.28125 1.046875 -1.046875 1.625q-0.75 0.5625 -1.921875 0.5625q-1.484375 0 -2.359375 -0.90625q-0.859375 -0.921875 -0.859375 -2.5625q0 -1.703125 0.875 -2.640625q0.890625 -0.9375 2.28125 -0.9375q1.359375 0 2.203125 0.921875q0.859375 0.921875 0.859375 2.578125q0 0.109375 0 0.3125l-5.03125 0q0.0625 1.109375 0.625 1.703125q0.5625 0.59375 1.40625 0.59375q0.640625 0 1.078125 -0.328125q0.453125 -0.34375 0.703125 -1.0625zm-3.75 -1.84375l3.765625 0q-0.078125 -0.859375 -0.4375 -1.28125q-0.546875 -0.65625 -1.40625 -0.65625q-0.796875 0 -1.328125 0.53125q-0.53125 0.515625 -0.59375 1.40625zm10.943726 1.546875l1.125 0.140625q-0.171875 1.171875 -0.9375 1.828125q-0.765625 0.65625 -1.859375 0.65625q-1.390625 0 -2.234375 -0.90625q-0.828125 -0.90625 -0.828125 -2.59375q0 -1.09375 0.359375 -1.90625q0.359375 -0.828125 1.09375 -1.234375q0.734375 -0.40625 1.609375 -0.40625q1.09375 0 1.796875 0.5625q0.703125 0.546875 0.890625 1.5625l-1.109375 0.171875q-0.15625 -0.671875 -0.5625 -1.015625q-0.390625 -0.34375 -0.96875 -0.34375q-0.859375 0 -1.40625 0.625q-0.53125 0.609375 -0.53125 1.953125q0 1.359375 0.515625 1.984375q0.515625 0.609375 1.359375 0.609375q0.671875 0 1.125 -0.40625q0.453125 -0.421875 0.5625 -1.28125zm2.5703125 2.46875l0 -1.296875l1.296875 0l0 1.296875q0 0.71875 -0.25 1.15625q-0.25 0.4375 -0.8125 0.6875l-0.3125 -0.484375q0.359375 -0.171875 0.53125 -0.484375q0.171875 -0.296875 0.1875 -0.875l-0.640625 0zm11.718506 -2.171875l1.1875 0.140625q-0.28125 1.046875 -1.046875 1.625q-0.75 0.5625 -1.921875 0.5625q-1.484375 0 -2.359375 -0.90625q-0.859375 -0.921875 -0.859375 -2.5625q0 -1.703125 0.875 -2.640625q0.890625 -0.9375 2.28125 -0.9375q1.359375 0 2.203125 0.921875q0.859375 0.921875 0.859375 2.578125q0 0.109375 0 0.3125l-5.03125 0q0.0625 1.109375 0.625 1.703125q0.5625 0.59375 1.40625 0.59375q0.640625 0 1.078125 -0.328125q0.453125 -0.34375 0.703125 -1.0625zm-3.75 -1.84375l3.765625 0q-0.078125 -0.859375 -0.4375 -1.28125q-0.546875 -0.65625 -1.40625 -0.65625q-0.796875 0 -1.328125 0.53125q-0.53125 0.515625 -0.59375 1.40625zm9.053101 3.0l0.15625 1.0q-0.484375 0.109375 -0.859375 0.109375q-0.625 0 -0.96875 -0.203125q-0.34375 -0.203125 -0.484375 -0.515625q-0.140625 -0.328125 -0.140625 -1.34375l0 -3.890625l-0.828125 0l0 -0.875l0.828125 0l0 -1.671875l1.140625 -0.6875l0 2.359375l1.15625 0l0 0.875l-1.15625 0l0 3.953125q0 0.484375 0.0625 0.625q0.0625 0.140625 0.1875 0.21875q0.140625 0.078125 0.390625 0.078125q0.203125 0 0.515625 -0.03125zm5.593628 -1.453125l1.125 0.140625q-0.171875 1.171875 -0.9375 1.828125q-0.765625 0.65625 -1.859375 0.65625q-1.390625 0 -2.234375 -0.90625q-0.828125 -0.90625 -0.828125 -2.59375q0 -1.09375 0.359375 -1.90625q0.359375 -0.828125 1.09375 -1.234375q0.734375 -0.40625 1.609375 -0.40625q1.09375 0 1.796875 0.5625q0.703125 0.546875 0.890625 1.5625l-1.109375 0.171875q-0.15625 -0.671875 -0.5625 -1.015625q-0.390625 -0.34375 -0.96875 -0.34375q-0.859375 0 -1.40625 0.625q-0.53125 0.609375 -0.53125 1.953125q0 1.359375 0.515625 1.984375q0.515625 0.609375 1.359375 0.609375q0.671875 0 1.125 -0.40625q0.453125 -0.421875 0.5625 -1.28125zm2.6015625 2.46875l0 -1.296875l1.296875 0l0 1.296875l-1.296875 0zm4.124878 2.734375l-0.828125 0q1.90625 -3.046875 1.90625 -6.09375q0 -1.203125 -0.28125 -2.375q-0.203125 -0.953125 -0.59375 -1.828125q-0.25 -0.5625 -1.03125 -1.90625l0.828125 0q1.1875 1.59375 1.765625 3.203125q0.484375 1.390625 0.484375 2.890625q0 1.71875 -0.65625 3.328125q-0.65625 1.59375 -1.59375 2.78125z" fill-rule="nonzero"></path><path fill="#cfe2f3" d="m57.730812 260.8423l325.92126 0l0 52.22049l-325.92126 0z" fill-rule="nonzero"></path><path fill="#0b5394" d="m141.32103 285.87253l5.234375 -13.59375l1.9375 0l5.5625 13.59375l-2.046875 0l-1.59375 -4.125l-5.6875 0l-1.484375 4.125l-1.921875 0zm3.921875 -5.578125l4.609375 0l-1.40625 -3.78125q-0.65625 -1.703125 -0.96875 -2.8125q-0.265625 1.3125 -0.734375 2.59375l-1.5 4.0zm9.802948 9.359375l0 -13.640625l1.53125 0l0 1.28125q0.53125 -0.75 1.203125 -1.125q0.6875 -0.375 1.640625 -0.375q1.265625 0 2.234375 0.65625q0.96875 0.640625 1.453125 1.828125q0.5 1.1875 0.5 2.59375q0 1.515625 -0.546875 2.734375q-0.546875 1.203125 -1.578125 1.84375q-1.03125 0.640625 -2.171875 0.640625q-0.84375 0 -1.515625 -0.34375q-0.65625 -0.359375 -1.078125 -0.890625l0 4.796875l-1.671875 0zm1.515625 -8.65625q0 1.90625 0.765625 2.8125q0.78125 0.90625 1.875 0.90625q1.109375 0 1.890625 -0.9375q0.796875 -0.9375 0.796875 -2.921875q0 -1.875 -0.78125 -2.8125q-0.765625 -0.9375 -1.84375 -0.9375q-1.0625 0 -1.890625 1.0q-0.8125 1.0 -0.8125 2.890625zm8.860092 8.65625l0 -13.640625l1.53125 0l0 1.28125q0.53125 -0.75 1.203125 -1.125q0.6875 -0.375 1.640625 -0.375q1.265625 0 2.234375 0.65625q0.96875 0.640625 1.453125 1.828125q0.5 1.1875 0.5 2.59375q0 1.515625 -0.546875 2.734375q-0.546875 1.203125 -1.578125 1.84375q-1.03125 0.640625 -2.171875 0.640625q-0.84375 0 -1.515625 -0.34375q-0.65625 -0.359375 -1.078125 -0.890625l0 4.796875l-1.671875 0zm1.515625 -8.65625q0 1.90625 0.765625 2.8125q0.78125 0.90625 1.875 0.90625q1.109375 0 1.890625 -0.9375q0.796875 -0.9375 0.796875 -2.921875q0 -1.875 -0.78125 -2.8125q-0.765625 -0.9375 -1.84375 -0.9375q-1.0625 0 -1.890625 1.0q-0.8125 1.0 -0.8125 2.890625zm8.828842 4.875l0 -13.59375l1.671875 0l0 13.59375l-1.671875 0zm4.097946 3.796875l-0.171875 -1.5625q0.546875 0.140625 0.953125 0.140625q0.546875 0 0.875 -0.1875q0.34375 -0.1875 0.5625 -0.515625q0.15625 -0.25 0.5 -1.25q0.046875 -0.140625 0.15625 -0.40625l-3.734375 -9.875l1.796875 0l2.046875 5.71875q0.40625 1.078125 0.71875 2.28125q0.28125 -1.15625 0.6875 -2.25l2.0937653 -5.75l1.671875 0l-3.7500153 10.03125q-0.59375 1.625 -0.9375 2.234375q-0.4375 0.828125 -1.015625 1.203125q-0.578125 0.390625 -1.375 0.390625q-0.484375 0 -1.078125 -0.203125zm21.027054 -7.40625l1.640625 0.21875q-0.265625 1.6875 -1.375 2.65625q-1.109375 0.953125 -2.734375 0.953125q-2.015625 0 -3.25 -1.3125q-1.21875 -1.328125 -1.21875 -3.796875q0 -1.59375 0.515625 -2.78125q0.53125 -1.203125 1.609375 -1.796875q1.09375 -0.609375 2.359375 -0.609375q1.609375 0 2.625 0.8125q1.015625 0.8125 1.3125 2.3125l-1.625 0.25q-0.234375 -1.0 -0.828125 -1.5q-0.59375 -0.5 -1.421875 -0.5q-1.265625 0 -2.0625 0.90625q-0.78125 0.90625 -0.78125 2.859375q0 1.984375 0.765625 2.890625q0.765625 0.890625 1.984375 0.890625q0.984375 0 1.640625 -0.59375q0.65625 -0.609375 0.84375 -1.859375zm2.265625 -1.3125q0 -2.734375 1.53125 -4.0625q1.265625 -1.09375 3.09375 -1.09375q2.03125 0 3.3125 1.34375q1.296875 1.328125 1.296875 3.671875q0 1.90625 -0.578125 3.0q-0.5625 1.078125 -1.65625 1.6875q-1.078125 0.59375 -2.375 0.59375q-2.0625 0 -3.34375 -1.328125q-1.28125 -1.328125 -1.28125 -3.8125zm1.71875 0q0 1.890625 0.828125 2.828125q0.828125 0.9375 2.078125 0.9375q1.25 0 2.0625 -0.9375q0.828125 -0.953125 0.828125 -2.890625q0 -1.828125 -0.828125 -2.765625q-0.828125 -0.9375 -2.0625 -0.9375q-1.25 0 -2.078125 0.9375q-0.828125 0.9375 -0.828125 2.828125zm9.281982 4.921875l0 -9.859375l1.5 0l0 1.40625q1.09375 -1.625 3.140625 -1.625q0.890625 0 1.640625 0.328125q0.75 0.3125 1.109375 0.84375q0.375 0.515625 0.53125 1.21875q0.09375 0.46875 0.09375 1.625l0 6.0625l-1.671875 0l0 -6.0q0 -1.015625 -0.203125 -1.515625q-0.1875 -0.515625 -0.6875 -0.8125q-0.5 -0.296875 -1.171875 -0.296875q-1.0625 0 -1.84375 0.671875q-0.765625 0.671875 -0.765625 2.578125l0 5.375l-1.671875 0zm10.781952 0l0 -8.546875l-1.484375 0l0 -1.3125l1.484375 0l0 -1.046875q0 -0.984375 0.171875 -1.46875q0.234375 -0.65625 0.84375 -1.046875q0.609375 -0.40625 1.703125 -0.40625q0.703125 0 1.5625 0.15625l-0.25 1.46875q-0.515625 -0.09375 -0.984375 -0.09375q-0.765625 0 -1.078125 0.328125q-0.3125 0.3125 -0.3125 1.203125l0 0.90625l1.921875 0l0 1.3125l-1.921875 0l0 8.546875l-1.65625 0zm4.792694 -11.6875l0 -1.90625l1.671875 0l0 1.90625l-1.671875 0zm0 11.6875l0 -9.859375l1.671875 0l0 9.859375l-1.671875 0zm3.832306 0.8125l1.609375 0.25q0.109375 0.75 0.578125 1.09375q0.609375 0.453125 1.6875 0.453125q1.171875 0 1.796875 -0.46875q0.625 -0.453125 0.859375 -1.28125q0.125 -0.515625 0.109375 -2.15625q-1.09375 1.296875 -2.71875 1.296875q-2.03125 0 -3.15625 -1.46875q-1.109375 -1.46875 -1.109375 -3.515625q0 -1.40625 0.515625 -2.59375q0.515625 -1.203125 1.484375 -1.84375q0.96875 -0.65625 2.265625 -0.65625q1.75 0 2.875 1.40625l0 -1.1875l1.546875 0l0 8.515625q0 2.3125 -0.46875 3.265625q-0.46875 0.96875 -1.484375 1.515625q-1.015625 0.5625 -2.5 0.5625q-1.765625 0 -2.859375 -0.796875q-1.078125 -0.796875 -1.03125 -2.390625zm1.375 -5.921875q0 1.953125 0.765625 2.84375q0.78125 0.890625 1.9375 0.890625q1.140625 0 1.921875 -0.890625q0.78125 -0.890625 0.78125 -2.78125q0 -1.8125 -0.8125 -2.71875q-0.796875 -0.921875 -1.921875 -0.921875q-1.109375 0 -1.890625 0.90625q-0.78125 0.890625 -0.78125 2.671875zm15.750732 5.109375l0 -1.453125q-1.140625 1.671875 -3.125 1.671875q-0.859375 0 -1.625 -0.328125q-0.75 -0.34375 -1.125 -0.84375q-0.359375 -0.5 -0.515625 -1.234375q-0.09375 -0.5 -0.09375 -1.5625l0 -6.109375l1.671875 0l0 5.46875q0 1.3125 0.09375 1.765625q0.15625 0.65625 0.671875 1.03125q0.515625 0.375 1.265625 0.375q0.75 0 1.40625 -0.375q0.65625 -0.390625 0.921875 -1.046875q0.28125 -0.671875 0.28125 -1.9375l0 -5.28125l1.671875 0l0 9.859375l-1.5 0zm3.906952 0l0 -9.859375l1.4999847 0l0 1.5q0.578125 -1.046875 1.0625 -1.375q0.484375 -0.34375 1.078125 -0.34375q0.84375 0 1.71875 0.546875l-0.578125 1.546875q-0.609375 -0.359375 -1.234375 -0.359375q-0.546875 0 -0.984375 0.328125q-0.421875 0.328125 -0.609375 0.90625q-0.28125 0.890625 -0.28125 1.953125l0 5.15625l-1.6718597 0zm12.665787 -1.21875q-0.9375 0.796875 -1.796875 1.125q-0.859375 0.3125 -1.84375 0.3125q-1.609375 0 -2.484375 -0.78125q-0.875 -0.796875 -0.875 -2.03125q0 -0.734375 0.328125 -1.328125q0.328125 -0.59375 0.859375 -0.953125q0.53125 -0.359375 1.203125 -0.546875q0.5 -0.140625 1.484375 -0.25q2.03125 -0.25 2.984375 -0.578125q0 -0.34375 0 -0.4375q0 -1.015625 -0.46875 -1.4375q-0.640625 -0.5625 -1.90625 -0.5625q-1.171875 0 -1.734375 0.40625q-0.5625 0.40625 -0.828125 1.46875l-1.640625 -0.234375q0.234375 -1.046875 0.734375 -1.6875q0.515625 -0.640625 1.46875 -0.984375q0.96875 -0.359375 2.25 -0.359375q1.265625 0 2.046875 0.296875q0.78125 0.296875 1.15625 0.75q0.375 0.453125 0.515625 1.140625q0.09375 0.421875 0.09375 1.53125l0 2.234375q0 2.328125 0.09375 2.953125q0.109375 0.609375 0.4375 1.171875l-1.75 0q-0.265625 -0.515625 -0.328125 -1.21875zm-0.140625 -3.71875q-0.90625 0.359375 -2.734375 0.625q-1.03125 0.140625 -1.453125 0.328125q-0.421875 0.1875 -0.65625 0.546875q-0.234375 0.359375 -0.234375 0.796875q0 0.671875 0.5 1.125q0.515625 0.4375 1.484375 0.4375q0.96875 0 1.71875 -0.421875q0.75 -0.4375 1.109375 -1.15625q0.265625 -0.578125 0.265625 -1.671875l0 -0.609375zm7.7351074 3.4375l0.234375 1.484375q-0.703125 0.140625 -1.265625 0.140625q-0.90625 0 -1.40625 -0.28125q-0.5 -0.296875 -0.703125 -0.75q-0.203125 -0.46875 -0.203125 -1.984375l0 -5.65625l-1.234375 0l0 -1.3125l1.234375 0l0 -2.4375l1.65625 -1.0l0 3.4375l1.6875 0l0 1.3125l-1.6875 0l0 5.75q0 0.71875 0.078125 0.921875q0.09375 0.203125 0.296875 0.328125q0.203125 0.125 0.578125 0.125q0.265625 0 0.734375 -0.078125zm1.5426636 -10.1875l0 -1.90625l1.671875 0l0 1.90625l-1.671875 0zm0 11.6875l0 -9.859375l1.671875 0l0 9.859375l-1.671875 0zm3.5042114 -4.921875q0 -2.734375 1.53125 -4.0625q1.265625 -1.09375 3.09375 -1.09375q2.03125 0 3.3125 1.34375q1.296875 1.328125 1.296875 3.671875q0 1.90625 -0.578125 3.0q-0.5625 1.078125 -1.65625 1.6875q-1.078125 0.59375 -2.375 0.59375q-2.0625 0 -3.34375 -1.328125q-1.28125 -1.328125 -1.28125 -3.8125zm1.71875 0q0 1.890625 0.828125 2.828125q0.828125 0.9375 2.078125 0.9375q1.25 0 2.0625 -0.9375q0.828125 -0.953125 0.828125 -2.890625q0 -1.828125 -0.828125 -2.765625q-0.828125 -0.9375 -2.0625 -0.9375q-1.25 0 -2.078125 0.9375q-0.828125 0.9375 -0.828125 2.828125zm9.281952 4.921875l0 -9.859375l1.5 0l0 1.40625q1.09375 -1.625 3.140625 -1.625q0.890625 0 1.640625 0.328125q0.75 0.3125 1.109375 0.84375q0.375 0.515625 0.53125 1.21875q0.09375 0.46875 0.09375 1.625l0 6.0625l-1.671875 0l0 -6.0q0 -1.015625 -0.203125 -1.515625q-0.1875 -0.515625 -0.6875 -0.8125q-0.5 -0.296875 -1.171875 -0.296875q-1.0625 0 -1.84375 0.671875q-0.765625 0.671875 -0.765625 2.578125l0 5.375l-1.671875 0z" fill-rule="nonzero"></path><path fill="#0b5394" d="m80.21276 302.75253l0 -9.3125l4.125 0q1.25 0 1.890625 0.265625q0.65625 0.25 1.046875 0.890625q0.390625 0.625 0.390625 1.390625q0 0.984375 -0.65625 1.671875q-0.640625 0.671875 -1.96875 0.859375q0.484375 0.234375 0.734375 0.46875q0.546875 0.484375 1.03125 1.234375l1.609375 2.53125l-1.546875 0l-1.234375 -1.9375q-0.53125 -0.84375 -0.890625 -1.28125q-0.34375 -0.4375 -0.625 -0.609375q-0.265625 -0.1875 -0.546875 -0.265625q-0.21875 -0.03125 -0.6875 -0.03125l-1.4375 0l0 4.125l-1.234375 0zm1.234375 -5.203125l2.65625 0q0.84375 0 1.3125 -0.171875q0.484375 -0.171875 0.71875 -0.546875q0.25 -0.390625 0.25 -0.84375q0 -0.65625 -0.484375 -1.078125q-0.46875 -0.4375 -1.5 -0.4375l-2.953125 0l0 3.078125zm12.843903 3.03125l1.1875 0.140625q-0.28125 1.046875 -1.046875 1.625q-0.75 0.5625 -1.921875 0.5625q-1.484375 0 -2.359375 -0.90625q-0.859375 -0.921875 -0.859375 -2.5625q0 -1.703125 0.875 -2.640625q0.890625 -0.9375 2.28125 -0.9375q1.359375 0 2.203125 0.921875q0.859375 0.921875 0.859375 2.578125q0 0.109375 0 0.3125l-5.03125 0q0.0625 1.109375 0.625 1.703125q0.5625 0.59375 1.40625 0.59375q0.640625 0 1.078125 -0.328125q0.453125 -0.34375 0.703125 -1.0625zm-3.75 -1.84375l3.765625 0q-0.078125 -0.859375 -0.4375 -1.28125q-0.546875 -0.65625 -1.40625 -0.65625q-0.796875 0 -1.328125 0.53125q-0.53125 0.515625 -0.59375 1.40625zm6.5531006 4.015625l0 -6.734375l1.015625 0l0 0.9375q0.328125 -0.5 0.84375 -0.796875q0.53125 -0.296875 1.203125 -0.296875q0.75 0 1.21875 0.3125q0.484375 0.3125 0.6875 0.859375q0.796875 -1.171875 2.078125 -1.171875q1.0 0 1.53125 0.5625q0.546875 0.546875 0.546875 1.703125l0 4.625l-1.125 0l0 -4.25q0 -0.6875 -0.109375 -0.984375q-0.109375 -0.296875 -0.40625 -0.484375q-0.296875 -0.1875 -0.6875 -0.1875q-0.71875 0 -1.1875 0.484375q-0.46875 0.46875 -0.46875 1.5l0 3.921875l-1.140625 0l0 -4.375q0 -0.765625 -0.28125 -1.140625q-0.28125 -0.390625 -0.90625 -0.390625q-0.484375 0 -0.890625 0.265625q-0.40625 0.25 -0.59375 0.734375q-0.1875 0.484375 -0.1875 1.40625l0 3.5l-1.140625 0zm10.680557 -3.375q0 -1.875 1.03125 -2.765625q0.875 -0.75 2.125 -0.75q1.390625 0 2.265625 0.90625q0.890625 0.90625 0.890625 2.515625q0 1.296875 -0.390625 2.046875q-0.390625 0.75 -1.140625 1.171875q-0.75 0.40625 -1.625 0.40625q-1.421875 0 -2.296875 -0.90625q-0.859375 -0.90625 -0.859375 -2.625zm1.171875 0q0 1.296875 0.5625 1.953125q0.5625 0.640625 1.421875 0.640625q0.84375 0 1.40625 -0.640625q0.578125 -0.65625 0.578125 -1.984375q0 -1.25 -0.578125 -1.890625q-0.5625 -0.65625 -1.40625 -0.65625q-0.859375 0 -1.421875 0.640625q-0.5625 0.640625 -0.5625 1.9375zm8.537476 3.375l-2.5625 -6.734375l1.203125 0l1.4375 4.03125q0.234375 0.65625 0.4375 1.359375q0.15625 -0.53125 0.421875 -1.28125l1.5 -4.109375l1.171875 0l-2.546875 6.734375l-1.0625 0zm9.3984375 -2.171875l1.1875076 0.140625q-0.28125763 1.046875 -1.0468826 1.625q-0.75 0.5625 -1.921875 0.5625q-1.484375 0 -2.359375 -0.90625q-0.859375 -0.921875 -0.859375 -2.5625q0 -1.703125 0.875 -2.640625q0.890625 -0.9375 2.28125 -0.9375q1.359375 0 2.203125 0.921875q0.8593826 0.921875 0.8593826 2.578125q0 0.109375 0 0.3125l-5.0312576 0q0.0625 1.109375 0.625 1.703125q0.5625 0.59375 1.40625 0.59375q0.640625 0 1.078125 -0.328125q0.453125 -0.34375 0.703125 -1.0625zm-3.75 -1.84375l3.765625 0q-0.078125 -0.859375 -0.4375 -1.28125q-0.546875 -0.65625 -1.40625 -0.65625q-0.796875 0 -1.328125 0.53125q-0.53125 0.515625 -0.59375 1.40625zm9.802971 2.0l1.125 -0.171875q0.09375 0.671875 0.53125 1.046875q0.4375 0.359375 1.21875 0.359375q0.78125 0 1.15625 -0.3125q0.390625 -0.328125 0.390625 -0.765625q0 -0.390625 -0.34375 -0.609375q-0.234375 -0.15625 -1.171875 -0.390625q-1.25 -0.3125 -1.734375 -0.546875q-0.484375 -0.234375 -0.734375 -0.640625q-0.25 -0.40625 -0.25 -0.90625q0 -0.453125 0.203125 -0.828125q0.203125 -0.390625 0.5625 -0.640625q0.265625 -0.203125 0.71875 -0.328125q0.46875 -0.140625 1.0 -0.140625q0.78125 0 1.375 0.234375q0.609375 0.21875 0.890625 0.609375q0.296875 0.390625 0.40625 1.046875l-1.125 0.15625q-0.078125 -0.53125 -0.4375 -0.8125q-0.359375 -0.296875 -1.03125 -0.296875q-0.78125 0 -1.125 0.265625q-0.34375 0.25 -0.34375 0.609375q0 0.21875 0.140625 0.390625q0.140625 0.1875 0.4375 0.3125q0.171875 0.0625 1.015625 0.28125q1.21875 0.328125 1.6875 0.53125q0.484375 0.203125 0.75 0.609375q0.28125 0.390625 0.28125 0.96875q0 0.578125 -0.34375 1.078125q-0.328125 0.5 -0.953125 0.78125q-0.625 0.28125 -1.421875 0.28125q-1.3125 0 -2.0 -0.546875q-0.6875 -0.546875 -0.875 -1.625zm7.1171875 2.015625l0 -9.3125l1.140625 0l0 5.3125l2.703125 -2.734375l1.484375 0l-2.578125 2.5l2.84375 4.234375l-1.40625 0l-2.234375 -3.453125l-0.8125 0.78125l0 2.671875l-1.140625 0zm6.6640625 -7.984375l0 -1.328125l1.140625 0l0 1.328125l-1.140625 0zm0 7.984375l0 -6.734375l1.140625 0l0 6.734375l-1.140625 0zm2.96109 2.578125l0 -9.3125l1.03125 0l0 0.875q0.375 -0.515625 0.828125 -0.765625q0.46875 -0.265625 1.140625 -0.265625q0.859375 0 1.515625 0.453125q0.65625 0.4375 0.984375 1.25q0.34375 0.796875 0.34375 1.765625q0 1.03125 -0.375 1.859375q-0.359375 0.828125 -1.078125 1.28125q-0.703125 0.4375 -1.484375 0.4375q-0.5625 0 -1.015625 -0.234375q-0.453125 -0.25 -0.75 -0.625l0 3.28125l-1.140625 0zm1.03125 -5.90625q0 1.296875 0.53125 1.921875q0.53125 0.625 1.265625 0.625q0.765625 0 1.3125 -0.640625q0.546875 -0.65625 0.546875 -2.0q0 -1.296875 -0.53125 -1.9375q-0.53125 -0.640625 -1.265625 -0.640625q-0.734375 0 -1.296875 0.6875q-0.5625 0.671875 -0.5625 1.984375zm6.3812256 5.90625l0 -9.3125l1.03125 0l0 0.875q0.375 -0.515625 0.828125 -0.765625q0.46875 -0.265625 1.140625 -0.265625q0.859375 0 1.515625 0.453125q0.65625 0.4375 0.984375 1.25q0.34375 0.796875 0.34375 1.765625q0 1.03125 -0.375 1.859375q-0.359375 0.828125 -1.078125 1.28125q-0.703125 0.4375 -1.484375 0.4375q-0.5625 0 -1.015625 -0.234375q-0.453125 -0.25 -0.75 -0.625l0 3.28125l-1.140625 0zm1.03125 -5.90625q0 1.296875 0.53125 1.921875q0.53125 0.625 1.265625 0.625q0.765625 0 1.3125 -0.640625q0.546875 -0.65625 0.546875 -2.0q0 -1.296875 -0.53125 -1.9375q-0.53125 -0.640625 -1.265625 -0.640625q-0.734375 0 -1.296875 0.6875q-0.5625 0.671875 -0.5625 1.984375zm10.990601 1.15625l1.1875 0.140625q-0.28125 1.046875 -1.046875 1.625q-0.75 0.5625 -1.921875 0.5625q-1.484375 0 -2.359375 -0.90625q-0.859375 -0.921875 -0.859375 -2.5625q0 -1.703125 0.875 -2.640625q0.890625 -0.9375 2.28125 -0.9375q1.359375 0 2.203125 0.921875q0.859375 0.921875 0.859375 2.578125q0 0.109375 0 0.3125l-5.03125 0q0.0625 1.109375 0.625 1.703125q0.5625 0.59375 1.40625 0.59375q0.640625 0 1.078125 -0.328125q0.453125 -0.34375 0.703125 -1.0625zm-3.75 -1.84375l3.765625 0q-0.078125 -0.859375 -0.4375 -1.28125q-0.546875 -0.65625 -1.40625 -0.65625q-0.796875 0 -1.328125 0.53125q-0.53125 0.515625 -0.59375 1.40625zm10.928101 4.015625l0 -0.84375q-0.640625 1.0 -1.890625 1.0q-0.796875 0 -1.484375 -0.4375q-0.671875 -0.453125 -1.046875 -1.25q-0.375 -0.796875 -0.375 -1.828125q0 -1.015625 0.34375 -1.828125q0.34375 -0.828125 1.015625 -1.265625q0.671875 -0.4375 1.5 -0.4375q0.609375 0 1.078125 0.265625q0.484375 0.25 0.78125 0.65625l0 -3.34375l1.140625 0l0 9.3125l-1.0625 0zm-3.609375 -3.359375q0 1.296875 0.53125 1.9375q0.546875 0.640625 1.296875 0.640625q0.75 0 1.265625 -0.609375q0.53125 -0.625 0.53125 -1.875q0 -1.390625 -0.53125 -2.03125q-0.53125 -0.65625 -1.3125 -0.65625q-0.765625 0 -1.28125 0.625q-0.5 0.625 -0.5 1.96875zm9.896713 1.34375l1.125 -0.171875q0.09375 0.671875 0.53125 1.046875q0.4375 0.359375 1.21875 0.359375q0.78125 0 1.15625 -0.3125q0.390625 -0.328125 0.390625 -0.765625q0 -0.390625 -0.34375 -0.609375q-0.234375 -0.15625 -1.171875 -0.390625q-1.25 -0.3125 -1.734375 -0.546875q-0.484375 -0.234375 -0.734375 -0.640625q-0.25 -0.40625 -0.25 -0.90625q0 -0.453125 0.203125 -0.828125q0.203125 -0.390625 0.5625 -0.640625q0.265625 -0.203125 0.71875 -0.328125q0.46875 -0.140625 1.0 -0.140625q0.78125 0 1.375 0.234375q0.609375 0.21875 0.890625 0.609375q0.296875 0.390625 0.40625 1.046875l-1.125 0.15625q-0.078125 -0.53125 -0.4375 -0.8125q-0.359375 -0.296875 -1.03125 -0.296875q-0.78125 0 -1.125 0.265625q-0.34375 0.25 -0.34375 0.609375q0 0.21875 0.140625 0.390625q0.140625 0.1875 0.4375 0.3125q0.171875 0.0625 1.015625 0.28125q1.21875 0.328125 1.6875 0.53125q0.484375 0.203125 0.75 0.609375q0.28125 0.390625 0.28125 0.96875q0 0.578125 -0.34375 1.078125q-0.328125 0.5 -0.953125 0.78125q-0.625 0.28125 -1.421875 0.28125q-1.3125 0 -2.0 -0.546875q-0.6875 -0.546875 -0.875 -1.625zm6.6953125 -1.359375q0 -1.875 1.03125 -2.765625q0.875 -0.75 2.125 -0.75q1.390625 0 2.265625 0.90625q0.890625 0.90625 0.890625 2.515625q0 1.296875 -0.390625 2.046875q-0.390625 0.75 -1.140625 1.171875q-0.75 0.40625 -1.625 0.40625q-1.421875 0 -2.296875 -0.90625q-0.859375 -0.90625 -0.859375 -2.625zm1.171875 0q0 1.296875 0.5625 1.953125q0.5625 0.640625 1.421875 0.640625q0.84375 0 1.40625 -0.640625q0.578125 -0.65625 0.578125 -1.984375q0 -1.25 -0.578125 -1.890625q-0.5625 -0.65625 -1.40625 -0.65625q-0.859375 0 -1.421875 0.640625q-0.5625 0.640625 -0.5625 1.9375zm11.084351 3.375l0 -0.984375q-0.796875 1.140625 -2.140625 1.140625q-0.59375 0 -1.125 -0.234375q-0.515625 -0.234375 -0.765625 -0.578125q-0.25 -0.34375 -0.34375 -0.84375q-0.078125 -0.328125 -0.078125 -1.0625l0 -4.171875l1.140625 0l0 3.734375q0 0.890625 0.078125 1.203125q0.109375 0.453125 0.453125 0.71875q0.34375 0.25 0.859375 0.25q0.515625 0 0.96875 -0.265625q0.453125 -0.265625 0.640625 -0.71875q0.1875 -0.453125 0.1875 -1.3125l0 -3.609375l1.140625 0l0 6.734375l-1.015625 0zm2.9749756 0l0 -6.734375l1.03125 0l0 1.015625q0.390625 -0.71875 0.71875 -0.9375q0.34375 -0.234375 0.734375 -0.234375q0.578125 0 1.171875 0.359375l-0.390625 1.0625q-0.421875 -0.25 -0.828125 -0.25q-0.375 0 -0.6875 0.234375q-0.296875 0.21875 -0.421875 0.625q-0.1875 0.609375 -0.1875 1.328125l0 3.53125l-1.140625 0zm8.84462 -2.46875l1.125 0.140625q-0.171875 1.171875 -0.9375 1.828125q-0.765625 0.65625 -1.859375 0.65625q-1.390625 0 -2.234375 -0.90625q-0.828125 -0.90625 -0.828125 -2.59375q0 -1.09375 0.359375 -1.90625q0.359375 -0.828125 1.09375 -1.234375q0.734375 -0.40625 1.609375 -0.40625q1.09375 0 1.796875 0.5625q0.703125 0.546875 0.890625 1.5625l-1.109375 0.171875q-0.15625 -0.671875 -0.5625 -1.015625q-0.390625 -0.34375 -0.96875 -0.34375q-0.859375 0 -1.40625 0.625q-0.53125 0.609375 -0.53125 1.953125q0 1.359375 0.515625 1.984375q0.515625 0.609375 1.359375 0.609375q0.671875 0 1.125 -0.40625q0.453125 -0.421875 0.5625 -1.28125zm6.8828125 0.296875l1.1875 0.140625q-0.28125 1.046875 -1.046875 1.625q-0.75 0.5625 -1.921875 0.5625q-1.484375 0 -2.359375 -0.90625q-0.859375 -0.921875 -0.859375 -2.5625q0 -1.703125 0.875 -2.640625q0.890625 -0.9375 2.28125 -0.9375q1.359375 0 2.203125 0.921875q0.859375 0.921875 0.859375 2.578125q0 0.109375 0 0.3125l-5.03125 0q0.0625 1.109375 0.625 1.703125q0.5625 0.59375 1.40625 0.59375q0.640625 0 1.078125 -0.328125q0.453125 -0.34375 0.703125 -1.0625zm-3.75 -1.84375l3.765625 0q-0.078125 -0.859375 -0.4375 -1.28125q-0.546875 -0.65625 -1.40625 -0.65625q-0.796875 0 -1.328125 0.53125q-0.53125 0.515625 -0.59375 1.40625zm14.677963 4.015625l0 -0.984375q-0.796875 1.140625 -2.140625 1.140625q-0.59375 0 -1.125 -0.234375q-0.515625 -0.234375 -0.765625 -0.578125q-0.25 -0.34375 -0.34375 -0.84375q-0.078125 -0.328125 -0.078125 -1.0625l0 -4.171875l1.140625 0l0 3.734375q0 0.890625 0.078125 1.203125q0.109375 0.453125 0.453125 0.71875q0.34375 0.25 0.859375 0.25q0.515625 0 0.96875 -0.265625q0.453125 -0.265625 0.640625 -0.71875q0.1875 -0.453125 0.1875 -1.3125l0 -3.609375l1.140625 0l0 6.734375l-1.015625 0zm2.9906006 0l0 -6.734375l1.03125 0l0 0.953125q0.734375 -1.109375 2.140625 -1.109375q0.609375 0 1.109375 0.21875q0.515625 0.21875 0.765625 0.578125q0.265625 0.34375 0.359375 0.84375q0.0625 0.3125 0.0625 1.109375l0 4.140625l-1.140625 0l0 -4.09375q0 -0.703125 -0.140625 -1.046875q-0.125 -0.34375 -0.46875 -0.546875q-0.328125 -0.21875 -0.78125 -0.21875q-0.734375 0 -1.265625 0.46875q-0.53125 0.453125 -0.53125 1.75l0 3.6875l-1.140625 0zm7.4124756 -7.984375l0 -1.328125l1.140625 0l0 1.328125l-1.140625 0zm0 7.984375l0 -6.734375l1.140625 0l0 6.734375l-1.140625 0zm5.46109 -1.015625l0.15625 1.0q-0.484375 0.109375 -0.859375 0.109375q-0.625 0 -0.96875 -0.203125q-0.34375 -0.203125 -0.484375 -0.515625q-0.140625 -0.328125 -0.140625 -1.34375l0 -3.890625l-0.828125 0l0 -0.875l0.828125 0l0 -1.671875l1.140625 -0.6875l0 2.359375l1.15625 0l0 0.875l-1.15625 0l0 3.953125q0 0.484375 0.0625 0.625q0.0625 0.140625 0.1875 0.21875q0.140625 0.078125 0.390625 0.078125q0.203125 0 0.515625 -0.03125zm0.7498627 -1.0l1.125 -0.171875q0.09375 0.671875 0.53125 1.046875q0.4375 0.359375 1.21875 0.359375q0.78125 0 1.15625 -0.3125q0.390625 -0.328125 0.390625 -0.765625q0 -0.390625 -0.34375 -0.609375q-0.234375 -0.15625 -1.171875 -0.390625q-1.25 -0.3125 -1.734375 -0.546875q-0.484375 -0.234375 -0.734375 -0.640625q-0.25 -0.40625 -0.25 -0.90625q0 -0.453125 0.203125 -0.828125q0.203125 -0.390625 0.5625 -0.640625q0.265625 -0.203125 0.71875 -0.328125q0.46875 -0.140625 1.0 -0.140625q0.78125 0 1.375 0.234375q0.609375 0.21875 0.890625 0.609375q0.296875 0.390625 0.40625 1.046875l-1.125 0.15625q-0.078125 -0.53125 -0.4375 -0.8125q-0.359375 -0.296875 -1.03125 -0.296875q-0.78125 0 -1.125 0.265625q-0.34375 0.25 -0.34375 0.609375q0 0.21875 0.140625 0.390625q0.140625 0.1875 0.4375 0.3125q0.171875 0.0625 1.015625 0.28125q1.21875 0.328125 1.6875 0.53125q0.484375 0.203125 0.75 0.609375q0.28125 0.390625 0.28125 0.96875q0 0.578125 -0.34375 1.078125q-0.328125 0.5 -0.953125 0.78125q-0.625 0.28125 -1.421875 0.28125q-1.3125 0 -2.0 -0.546875q-0.6875 -0.546875 -0.875 -1.625zm7.4140625 2.015625l0 -1.296875l1.296875 0l0 1.296875q0 0.71875 -0.25 1.15625q-0.25 0.4375 -0.8125 0.6875l-0.3125 -0.484375q0.359375 -0.171875 0.53125 -0.484375q0.171875 -0.296875 0.1875 -0.875l-0.640625 0zm7.1091003 0l0 -6.734375l1.015625 0l0 0.9375q0.328125 -0.5 0.84375 -0.796875q0.53125 -0.296875 1.203125 -0.296875q0.75 0 1.21875 0.3125q0.484375 0.3125 0.6875 0.859375q0.796875 -1.171875 2.078125 -1.171875q1.0 0 1.53125 0.5625q0.546875 0.546875 0.546875 1.703125l0 4.625l-1.125 0l0 -4.25q0 -0.6875 -0.109375 -0.984375q-0.109375 -0.296875 -0.40625 -0.484375q-0.296875 -0.1875 -0.6875 -0.1875q-0.71875 0 -1.1875 0.484375q-0.46875 0.46875 -0.46875 1.5l0 3.921875l-1.140625 0l0 -4.375q0 -0.765625 -0.28125 -1.140625q-0.28125 -0.390625 -0.90625 -0.390625q-0.484375 0 -0.890625 0.265625q-0.40625 0.25 -0.59375 0.734375q-0.1875 0.484375 -0.1875 1.40625l0 3.5l-1.140625 0zm15.711792 -2.171875l1.1875 0.140625q-0.28125 1.046875 -1.046875 1.625q-0.75 0.5625 -1.921875 0.5625q-1.484375 0 -2.359375 -0.90625q-0.859375 -0.921875 -0.859375 -2.5625q0 -1.703125 0.875 -2.640625q0.890625 -0.9375 2.28125 -0.9375q1.359375 0 2.203125 0.921875q0.859375 0.921875 0.859375 2.578125q0 0.109375 0 0.3125l-5.03125 0q0.0625 1.109375 0.625 1.703125q0.5625 0.59375 1.40625 0.59375q0.640625 0 1.078125 -0.328125q0.453125 -0.34375 0.703125 -1.0625zm-3.75 -1.84375l3.765625 0q-0.078125 -0.859375 -0.4375 -1.28125q-0.546875 -0.65625 -1.40625 -0.65625q-0.796875 0 -1.328125 0.53125q-0.53125 0.515625 -0.59375 1.40625zm6.5374756 4.015625l0 -6.734375l1.03125 0l0 1.015625q0.390625 -0.71875 0.71875 -0.9375q0.34375 -0.234375 0.734375 -0.234375q0.578125 0 1.171875 0.359375l-0.390625 1.0625q-0.421875 -0.25 -0.828125 -0.25q-0.375 0 -0.6875 0.234375q-0.296875 0.21875 -0.421875 0.625q-0.1875 0.609375 -0.1875 1.328125l0 3.53125l-1.140625 0zm4.23526 0.5625l1.125 0.15625q0.0625 0.515625 0.375 0.75q0.4375 0.328125 1.171875 0.328125q0.78125 0 1.21875 -0.328125q0.4375 -0.3125 0.578125 -0.890625q0.09375 -0.34375 0.09375 -1.453125q-0.75 0.875 -1.875 0.875q-1.390625 0 -2.15625 -1.0q-0.75 -1.0 -0.75 -2.40625q0 -0.96875 0.34375 -1.78125q0.359375 -0.8125 1.015625 -1.25q0.65625 -0.453125 1.5625 -0.453125q1.1875 0 1.96875 0.96875l0 -0.8125l1.046875 0l0 5.8125q0 1.578125 -0.328125 2.234375q-0.3125 0.65625 -1.015625 1.03125q-0.6875 0.390625 -1.703125 0.390625q-1.203125 0 -1.953125 -0.546875q-0.734375 -0.53125 -0.71875 -1.625zm0.953125 -4.046875q0 1.3125 0.515625 1.921875q0.53125 0.609375 1.328125 0.609375q0.796875 0 1.328125 -0.59375q0.53125 -0.609375 0.53125 -1.90625q0 -1.234375 -0.546875 -1.859375q-0.546875 -0.640625 -1.328125 -0.640625q-0.765625 0 -1.296875 0.625q-0.53125 0.625 -0.53125 1.84375zm11.287476 1.3125l1.1875 0.140625q-0.28125 1.046875 -1.046875 1.625q-0.75 0.5625 -1.921875 0.5625q-1.484375 0 -2.359375 -0.90625q-0.859375 -0.921875 -0.859375 -2.5625q0 -1.703125 0.875 -2.640625q0.890625 -0.9375 2.28125 -0.9375q1.359375 0 2.203125 0.921875q0.859375 0.921875 0.859375 2.578125q0 0.109375 0 0.3125l-5.03125 0q0.0625 1.109375 0.625 1.703125q0.5625 0.59375 1.40625 0.59375q0.640625 0 1.078125 -0.328125q0.453125 -0.34375 0.703125 -1.0625zm-3.75 -1.84375l3.765625 0q-0.078125 -0.859375 -0.4375 -1.28125q-0.546875 -0.65625 -1.40625 -0.65625q-0.796875 0 -1.328125 0.53125q-0.53125 0.515625 -0.59375 1.40625zm10.256073 6.59375l0 -9.3125l1.03125 0l0 0.875q0.375 -0.515625 0.828125 -0.765625q0.46875 -0.265625 1.140625 -0.265625q0.859375 0 1.515625 0.453125q0.65625 0.4375 0.984375 1.25q0.34375 0.796875 0.34375 1.765625q0 1.03125 -0.375 1.859375q-0.359375 0.828125 -1.078125 1.28125q-0.703125 0.4375 -1.484375 0.4375q-0.5625 0 -1.015625 -0.234375q-0.453125 -0.25 -0.75 -0.625l0 3.28125l-1.140625 0zm1.03125 -5.90625q0 1.296875 0.53125 1.921875q0.53125 0.625 1.265625 0.625q0.765625 0 1.3125 -0.640625q0.546875 -0.65625 0.546875 -2.0q0 -1.296875 -0.53125 -1.9375q-0.53125 -0.640625 -1.265625 -0.640625q-0.734375 0 -1.296875 0.6875q-0.5625 0.671875 -0.5625 1.984375zm6.3656006 3.328125l0 -6.734375l1.03125 0l0 1.015625q0.390625 -0.71875 0.71875 -0.9375q0.34375 -0.234375 0.734375 -0.234375q0.578125 0 1.171875 0.359375l-0.390625 1.0625q-0.421875 -0.25 -0.828125 -0.25q-0.375 0 -0.6875 0.234375q-0.296875 0.21875 -0.421875 0.625q-0.1875 0.609375 -0.1875 1.328125l0 3.53125l-1.140625 0zm4.0321045 -3.375q0 -1.875 1.03125 -2.765625q0.875 -0.75 2.125 -0.75q1.390625 0 2.265625 0.90625q0.890625 0.90625 0.890625 2.515625q0 1.296875 -0.390625 2.046875q-0.390625 0.75 -1.140625 1.171875q-0.75 0.40625 -1.625 0.40625q-1.421875 0 -2.296875 -0.90625q-0.859375 -0.90625 -0.859375 -2.625zm1.171875 0q0 1.296875 0.5625 1.953125q0.5625 0.640625 1.421875 0.640625q0.84375 0 1.40625 -0.640625q0.578125 -0.65625 0.578125 -1.984375q0 -1.25 -0.578125 -1.890625q-0.5625 -0.65625 -1.40625 -0.65625q-0.859375 0 -1.421875 0.640625q-0.5625 0.640625 -0.5625 1.9375zm6.6624756 5.953125l0 -9.3125l1.03125 0l0 0.875q0.375 -0.515625 0.828125 -0.765625q0.46875 -0.265625 1.140625 -0.265625q0.859375 0 1.515625 0.453125q0.65625 0.4375 0.984375 1.25q0.34375 0.796875 0.34375 1.765625q0 1.03125 -0.375 1.859375q-0.359375 0.828125 -1.078125 1.28125q-0.703125 0.4375 -1.484375 0.4375q-0.5625 0 -1.015625 -0.234375q-0.453125 -0.25 -0.75 -0.625l0 3.28125l-1.140625 0zm1.03125 -5.90625q0 1.296875 0.53125 1.921875q0.53125 0.625 1.265625 0.625q0.765625 0 1.3125 -0.640625q0.546875 -0.65625 0.546875 -2.0q0 -1.296875 -0.53125 -1.9375q-0.53125 -0.640625 -1.265625 -0.640625q-0.734375 0 -1.296875 0.6875q-0.5625 0.671875 -0.5625 1.984375zm10.990601 1.15625l1.1875 0.140625q-0.28125 1.046875 -1.046875 1.625q-0.75 0.5625 -1.921875 0.5625q-1.484375 0 -2.359375 -0.90625q-0.859375 -0.921875 -0.859375 -2.5625q0 -1.703125 0.875 -2.640625q0.890625 -0.9375 2.28125 -0.9375q1.359375 0 2.203125 0.921875q0.859375 0.921875 0.859375 2.578125q0 0.109375 0 0.3125l-5.03125 0q0.0625 1.109375 0.625 1.703125q0.5625 0.59375 1.40625 0.59375q0.640625 0 1.078125 -0.328125q0.453125 -0.34375 0.703125 -1.0625zm-3.75 -1.84375l3.765625 0q-0.078125 -0.859375 -0.4375 -1.28125q-0.546875 -0.65625 -1.40625 -0.65625q-0.796875 0 -1.328125 0.53125q-0.53125 0.515625 -0.59375 1.40625zm6.5374756 4.015625l0 -6.734375l1.03125 0l0 1.015625q0.390625 -0.71875 0.71875 -0.9375q0.34375 -0.234375 0.734375 -0.234375q0.578125 0 1.171875 0.359375l-0.390625 1.0625q-0.421875 -0.25 -0.828125 -0.25q-0.375 0 -0.6875 0.234375q-0.296875 0.21875 -0.421875 0.625q-0.1875 0.609375 -0.1875 1.328125l0 3.53125l-1.140625 0zm6.9539795 -1.015625l0.15625 1.0q-0.484375 0.109375 -0.859375 0.109375q-0.625 0 -0.96875 -0.203125q-0.34375 -0.203125 -0.484375 -0.515625q-0.140625 -0.328125 -0.140625 -1.34375l0 -3.890625l-0.828125 0l0 -0.875l0.828125 0l0 -1.671875l1.140625 -0.6875l0 2.359375l1.15625 0l0 0.875l-1.15625 0l0 3.953125q0 0.484375 0.0625 0.625q0.0625 0.140625 0.1875 0.21875q0.140625 0.078125 0.390625 0.078125q0.203125 0 0.515625 -0.03125zm1.2030029 -6.96875l0 -1.328125l1.140625 0l0 1.328125l-1.140625 0zm0 7.984375l0 -6.734375l1.140625 0l0 6.734375l-1.140625 0zm7.5704956 -2.171875l1.1875 0.140625q-0.28125 1.046875 -1.046875 1.625q-0.75 0.5625 -1.921875 0.5625q-1.484375 0 -2.359375 -0.90625q-0.859375 -0.921875 -0.859375 -2.5625q0 -1.703125 0.875 -2.640625q0.890625 -0.9375 2.28125 -0.9375q1.359375 0 2.203125 0.921875q0.859375 0.921875 0.859375 2.578125q0 0.109375 0 0.3125l-5.03125 0q0.0625 1.109375 0.625 1.703125q0.5625 0.59375 1.40625 0.59375q0.640625 0 1.078125 -0.328125q0.453125 -0.34375 0.703125 -1.0625zm-3.75 -1.84375l3.765625 0q-0.078125 -0.859375 -0.4375 -1.28125q-0.546875 -0.65625 -1.40625 -0.65625q-0.796875 0 -1.328125 0.53125q-0.53125 0.515625 -0.59375 1.40625zm6.0999756 2.0l1.125 -0.171875q0.09375 0.671875 0.53125 1.046875q0.4375 0.359375 1.21875 0.359375q0.78125 0 1.15625 -0.3125q0.390625 -0.328125 0.390625 -0.765625q0 -0.390625 -0.34375 -0.609375q-0.234375 -0.15625 -1.171875 -0.390625q-1.25 -0.3125 -1.734375 -0.546875q-0.484375 -0.234375 -0.734375 -0.640625q-0.25 -0.40625 -0.25 -0.90625q0 -0.453125 0.203125 -0.828125q0.203125 -0.390625 0.5625 -0.640625q0.265625 -0.203125 0.71875 -0.328125q0.46875 -0.140625 1.0 -0.140625q0.78125 0 1.375 0.234375q0.609375 0.21875 0.890625 0.609375q0.296875 0.390625 0.40625 1.046875l-1.125 0.15625q-0.078125 -0.53125 -0.4375 -0.8125q-0.359375 -0.296875 -1.03125 -0.296875q-0.78125 0 -1.125 0.265625q-0.34375 0.25 -0.34375 0.609375q0 0.21875 0.140625 0.390625q0.140625 0.1875 0.4375 0.3125q0.171875 0.0625 1.015625 0.28125q1.21875 0.328125 1.6875 0.53125q0.484375 0.203125 0.75 0.609375q0.28125 0.390625 0.28125 0.96875q0 0.578125 -0.34375 1.078125q-0.328125 0.5 -0.953125 0.78125q-0.625 0.28125 -1.421875 0.28125q-1.3125 0 -2.0 -0.546875q-0.6875 -0.546875 -0.875 -1.625z" fill-rule="nonzero"></path><path fill="#cfe2f3" d="m20.506561 331.66986l398.99213 0l0 52.22049l-398.99213 0z" fill-rule="nonzero"></path><path fill="#0b5394" d="m109.26712 356.7001l-3.609375 -13.59375l1.84375 0l2.0625 8.90625q0.34375 1.40625 0.578125 2.78125q0.515625 -2.171875 0.609375 -2.515625l2.59375 -9.171875l2.171875 0l1.953125 6.875q0.734375 2.5625 1.046875 4.8125q0.265625 -1.28125 0.6875 -2.953125l2.125 -8.734375l1.8125 0l-3.734375 13.59375l-1.734375 0l-2.859375 -10.359375q-0.359375 -1.296875 -0.421875 -1.59375q-0.21875 0.9375 -0.40625 1.59375l-2.890625 10.359375l-1.828125 0zm14.999283 0l0 -9.859375l1.5 0l0 1.5q0.578125 -1.046875 1.0625 -1.375q0.484375 -0.34375 1.078125 -0.34375q0.84375 0 1.71875 0.546875l-0.578125 1.546875q-0.609375 -0.359375 -1.234375 -0.359375q-0.546875 0 -0.984375 0.328125q-0.421875 0.328125 -0.609375 0.90625q-0.28125 0.890625 -0.28125 1.953125l0 5.15625l-1.671875 0zm6.243927 -11.6875l0 -1.90625l1.671875 0l0 1.90625l-1.671875 0zm0 11.6875l0 -9.859375l1.671875 0l0 9.859375l-1.671875 0zm7.785446 -1.5l0.234375 1.484375q-0.703125 0.140625 -1.265625 0.140625q-0.90625 0 -1.40625 -0.28125q-0.5 -0.296875 -0.703125 -0.75q-0.203125 -0.46875 -0.203125 -1.984375l0 -5.65625l-1.234375 0l0 -1.3125l1.234375 0l0 -2.4375l1.65625 -1.0l0 3.4375l1.6875 0l0 1.3125l-1.6875 0l0 5.75q0 0.71875 0.078125 0.921875q0.09375 0.203125 0.296875 0.328125q0.203125 0.125 0.578125 0.125q0.265625 0 0.734375 -0.078125zm8.277054 -1.671875l1.71875 0.21875q-0.40625 1.5 -1.515625 2.34375q-1.09375 0.828125 -2.8125 0.828125q-2.15625 0 -3.421875 -1.328125q-1.265625 -1.328125 -1.265625 -3.734375q0 -2.484375 1.265625 -3.859375q1.28125 -1.375 3.328125 -1.375q1.984375 0 3.234375 1.34375q1.25 1.34375 1.25 3.796875q0 0.140625 -0.015625 0.4375l-7.34375 0q0.09375 1.625 0.921875 2.484375q0.828125 0.859375 2.0625 0.859375q0.90625 0 1.546875 -0.46875q0.65625 -0.484375 1.046875 -1.546875zm-5.484375 -2.703125l5.5 0q-0.109375 -1.234375 -0.625 -1.859375q-0.796875 -0.96875 -2.078125 -0.96875q-1.140625 0 -1.9375 0.78125q-0.78125 0.765625 -0.859375 2.046875zm13.621521 2.9375l1.65625 -0.265625q0.140625 1.0 0.765625 1.53125q0.640625 0.515625 1.78125 0.515625q1.15625 0 1.703125 -0.46875q0.5625 -0.46875 0.5625 -1.09375q0 -0.5625 -0.484375 -0.890625q-0.34375 -0.21875 -1.703125 -0.5625q-1.84375 -0.46875 -2.5625 -0.796875q-0.703125 -0.34375 -1.078125 -0.9375q-0.359375 -0.609375 -0.359375 -1.328125q0 -0.65625 0.296875 -1.21875q0.3125 -0.5625 0.828125 -0.9375q0.390625 -0.28125 1.0625 -0.484375q0.671875 -0.203125 1.4375 -0.203125q1.171875 0 2.046875 0.34375q0.875 0.328125 1.28125 0.90625q0.421875 0.5625 0.578125 1.515625l-1.625 0.21875q-0.109375 -0.75 -0.65625 -1.171875q-0.53125 -0.4375 -1.5 -0.4375q-1.15625 0 -1.640625 0.390625q-0.484375 0.375 -0.484375 0.875q0 0.328125 0.203125 0.59375q0.203125 0.265625 0.640625 0.4375q0.25 0.09375 1.46875 0.4375q1.765625 0.46875 2.46875 0.765625q0.703125 0.296875 1.09375 0.875q0.40625 0.578125 0.40625 1.4375q0 0.828125 -0.484375 1.578125q-0.484375 0.734375 -1.40625 1.140625q-0.921875 0.390625 -2.078125 0.390625q-1.921875 0 -2.9375 -0.796875q-1.0 -0.796875 -1.28125 -2.359375zm9.375 -1.984375q0 -2.734375 1.53125 -4.0625q1.265625 -1.09375 3.09375 -1.09375q2.03125 0 3.3125 1.34375q1.296875 1.328125 1.296875 3.671875q0 1.90625 -0.578125 3.0q-0.5625 1.078125 -1.65625 1.6875q-1.078125 0.59375 -2.375 0.59375q-2.0625 0 -3.34375 -1.328125q-1.28125 -1.328125 -1.28125 -3.8125zm1.71875 0q0 1.890625 0.828125 2.828125q0.828125 0.9375 2.078125 0.9375q1.25 0 2.0625 -0.9375q0.828125 -0.953125 0.828125 -2.890625q0 -1.828125 -0.828125 -2.765625q-0.828125 -0.9375 -2.0625 -0.9375q-1.25 0 -2.078125 0.9375q-0.828125 0.9375 -0.828125 2.828125zm15.735092 4.921875l0 -1.453125q-1.140625 1.671875 -3.125 1.671875q-0.859375 0 -1.625 -0.328125q-0.75 -0.34375 -1.125 -0.84375q-0.359375 -0.5 -0.515625 -1.234375q-0.09375 -0.5 -0.09375 -1.5625l0 -6.109375l1.671875 0l0 5.46875q0 1.3125 0.09375 1.765625q0.15625 0.65625 0.671875 1.03125q0.515625 0.375 1.265625 0.375q0.75 0 1.40625 -0.375q0.65625 -0.390625 0.921875 -1.046875q0.28125 -0.671875 0.28125 -1.9375l0 -5.28125l1.671875 0l0 9.859375l-1.5 0zm3.9069672 0l0 -9.859375l1.5 0l0 1.5q0.578125 -1.046875 1.0625 -1.375q0.484375 -0.34375 1.078125 -0.34375q0.84375 0 1.71875 0.546875l-0.578125 1.546875q-0.609375 -0.359375 -1.234375 -0.359375q-0.546875 0 -0.984375 0.328125q-0.421875 0.328125 -0.609375 0.90625q-0.28125 0.890625 -0.28125 1.953125l0 5.15625l-1.671875 0zm12.665802 -3.609375l1.640625 0.21875q-0.265625 1.6875 -1.375 2.65625q-1.109375 0.953125 -2.734375 0.953125q-2.015625 0 -3.25 -1.3125q-1.21875 -1.328125 -1.21875 -3.796875q0 -1.59375 0.515625 -2.78125q0.53125 -1.203125 1.609375 -1.796875q1.09375 -0.609375 2.359375 -0.609375q1.609375 0 2.625 0.8125q1.015625 0.8125 1.3125 2.3125l-1.625 0.25q-0.234375 -1.0 -0.828125 -1.5q-0.59375 -0.5 -1.421875 -0.5q-1.265625 0 -2.0625 0.90625q-0.78125 0.90625 -0.78125 2.859375q0 1.984375 0.765625 2.890625q0.765625 0.890625 1.984375 0.890625q0.984375 0 1.640625 -0.59375q0.65625 -0.609375 0.84375 -1.859375zm9.640625 0.4375l1.71875 0.21875q-0.40625 1.5 -1.515625 2.34375q-1.09375 0.828125 -2.8125 0.828125q-2.15625 0 -3.421875 -1.328125q-1.265625 -1.328125 -1.265625 -3.734375q0 -2.484375 1.265625 -3.859375q1.28125 -1.375 3.328125 -1.375q1.984375 0 3.234375 1.34375q1.25 1.34375 1.25 3.796875q0 0.140625 -0.015625 0.4375l-7.34375 0q0.09375 1.625 0.921875 2.484375q0.828125 0.859375 2.0625 0.859375q0.90625 0 1.546875 -0.46875q0.65625 -0.484375 1.046875 -1.546875zm-5.484375 -2.703125l5.5 0q-0.109375 -1.234375 -0.625 -1.859375q-0.796875 -0.96875 -2.078125 -0.96875q-1.140625 0 -1.9375 0.78125q-0.78125 0.765625 -0.859375 2.046875zm20.746521 5.875l0 -1.453125q-1.140625 1.671875 -3.125 1.671875q-0.859375 0 -1.625 -0.328125q-0.75 -0.34375 -1.125 -0.84375q-0.359375 -0.5 -0.515625 -1.234375q-0.09375 -0.5 -0.09375 -1.5625l0 -6.109375l1.671875 0l0 5.46875q0 1.3125 0.09375 1.765625q0.15625 0.65625 0.671875 1.03125q0.515625 0.375 1.265625 0.375q0.75 0 1.40625 -0.375q0.65625 -0.390625 0.921875 -1.046875q0.28125 -0.671875 0.28125 -1.9375l0 -5.28125l1.671875 0l0 9.859375l-1.5 0zm3.9225922 0l0 -9.859375l1.5 0l0 1.40625q1.09375 -1.625 3.140625 -1.625q0.890625 0 1.640625 0.328125q0.75 0.3125 1.109375 0.84375q0.375 0.515625 0.53125 1.21875q0.09375 0.46875 0.09375 1.625l0 6.0625l-1.671875 0l0 -6.0q0 -1.015625 -0.203125 -1.515625q-0.1875 -0.515625 -0.6875 -0.8125q-0.5 -0.296875 -1.171875 -0.296875q-1.0625 0 -1.84375 0.671875q-0.765625 0.671875 -0.765625 2.578125l0 5.375l-1.671875 0zm10.391342 -11.6875l0 -1.90625l1.671875 0l0 1.90625l-1.671875 0zm0 11.6875l0 -9.859375l1.671875 0l0 9.859375l-1.671875 0zm7.785446 -1.5l0.234375 1.484375q-0.703125 0.140625 -1.265625 0.140625q-0.90625 0 -1.40625 -0.28125q-0.5 -0.296875 -0.703125 -0.75q-0.203125 -0.46875 -0.203125 -1.984375l0 -5.65625l-1.234375 0l0 -1.3125l1.234375 0l0 -2.4375l1.65625 -1.0l0 3.4375l1.6875 0l0 1.3125l-1.6875 0l0 5.75q0 0.71875 0.078125 0.921875q0.09375 0.203125 0.296875 0.328125q0.203125 0.125 0.578125 0.125q0.265625 0 0.734375 -0.078125zm13.100983 1.5l0 -1.25q-0.9375 1.46875 -2.75 1.46875q-1.171875 0 -2.171875 -0.640625q-0.984375 -0.65625 -1.53125 -1.8125q-0.53125 -1.171875 -0.53125 -2.6875q0 -1.46875 0.484375 -2.671875q0.5 -1.203125 1.46875 -1.84375q0.984375 -0.640625 2.203125 -0.640625q0.890625 0 1.578125 0.375q0.703125 0.375 1.140625 0.984375l0 -4.875l1.65625 0l0 13.59375l-1.546875 0zm-5.28125 -4.921875q0 1.890625 0.796875 2.828125q0.8125 0.9375 1.890625 0.9375q1.09375 0 1.859375 -0.890625q0.765625 -0.890625 0.765625 -2.734375q0 -2.015625 -0.78125 -2.953125q-0.78125 -0.953125 -1.921875 -0.953125q-1.109375 0 -1.859375 0.90625q-0.75 0.90625 -0.75 2.859375zm16.016357 1.75l1.71875 0.21875q-0.40625 1.5 -1.515625 2.34375q-1.09375 0.828125 -2.8125 0.828125q-2.15625 0 -3.421875 -1.328125q-1.265625 -1.328125 -1.265625 -3.734375q0 -2.484375 1.265625 -3.859375q1.28125 -1.375 3.328125 -1.375q1.984375 0 3.234375 1.34375q1.25 1.34375 1.25 3.796875q0 0.140625 -0.015625 0.4375l-7.34375 0q0.09375 1.625 0.921875 2.484375q0.828125 0.859375 2.0625 0.859375q0.90625 0 1.546875 -0.46875q0.65625 -0.484375 1.046875 -1.546875zm-5.484375 -2.703125l5.5 0q-0.109375 -1.234375 -0.625 -1.859375q-0.796875 -0.96875 -2.078125 -0.96875q-1.140625 0 -1.9375 0.78125q-0.78125 0.765625 -0.859375 2.046875zm9.516327 5.875l0 -8.546875l-1.484375 0l0 -1.3125l1.484375 0l0 -1.046875q0 -0.984375 0.171875 -1.46875q0.234375 -0.65625 0.84375 -1.046875q0.609375 -0.40625 1.703125 -0.40625q0.703125 0 1.5625 0.15625l-0.25 1.46875q-0.515625 -0.09375 -0.984375 -0.09375q-0.765625 0 -1.078125 0.328125q-0.3125 0.3125 -0.3125 1.203125l0 0.90625l1.921875 0l0 1.3125l-1.921875 0l0 8.546875l-1.65625 0zm4.7926636 -11.6875l0 -1.90625l1.671875 0l0 1.90625l-1.671875 0zm0 11.6875l0 -9.859375l1.671875 0l0 9.859375l-1.671875 0zm4.1292114 0l0 -9.859375l1.5 0l0 1.40625q1.09375 -1.625 3.140625 -1.625q0.890625 0 1.640625 0.328125q0.75 0.3125 1.109375 0.84375q0.375 0.515625 0.53125 1.21875q0.09375 0.46875 0.09375 1.625l0 6.0625l-1.671875 0l0 -6.0q0 -1.015625 -0.203125 -1.515625q-0.1875 -0.515625 -0.6875 -0.8125q-0.5 -0.296875 -1.171875 -0.296875q-1.0625 0 -1.84375 0.671875q-0.765625 0.671875 -0.765625 2.578125l0 5.375l-1.671875 0zm10.391357 -11.6875l0 -1.90625l1.671875 0l0 1.90625l-1.671875 0zm0 11.6875l0 -9.859375l1.671875 0l0 9.859375l-1.671875 0zm7.785431 -1.5l0.234375 1.484375q-0.703125 0.140625 -1.265625 0.140625q-0.90625 0 -1.40625 -0.28125q-0.5 -0.296875 -0.703125 -0.75q-0.203125 -0.46875 -0.203125 -1.984375l0 -5.65625l-1.234375 0l0 -1.3125l1.234375 0l0 -2.4375l1.65625 -1.0l0 3.4375l1.6875 0l0 1.3125l-1.6875 0l0 5.75q0 0.71875 0.078125 0.921875q0.09375 0.203125 0.296875 0.328125q0.203125 0.125 0.578125 0.125q0.265625 0 0.734375 -0.078125zm1.5426941 -10.1875l0 -1.90625l1.671875 0l0 1.90625l-1.671875 0zm0 11.6875l0 -9.859375l1.671875 0l0 9.859375l-1.671875 0zm3.504181 -4.921875q0 -2.734375 1.53125 -4.0625q1.265625 -1.09375 3.09375 -1.09375q2.03125 0 3.3125 1.34375q1.296875 1.328125 1.296875 3.671875q0 1.90625 -0.578125 3.0q-0.5625 1.078125 -1.65625 1.6875q-1.078125 0.59375 -2.375 0.59375q-2.0625 0 -3.34375 -1.328125q-1.28125 -1.328125 -1.28125 -3.8125zm1.71875 0q0 1.890625 0.828125 2.828125q0.828125 0.9375 2.078125 0.9375q1.25 0 2.0625 -0.9375q0.828125 -0.953125 0.828125 -2.890625q0 -1.828125 -0.828125 -2.765625q-0.828125 -0.9375 -2.0625 -0.9375q-1.25 0 -2.078125 0.9375q-0.828125 0.9375 -0.828125 2.828125zm9.281952 4.921875l0 -9.859375l1.5 0l0 1.40625q1.09375 -1.625 3.140625 -1.625q0.890625 0 1.640625 0.328125q0.75 0.3125 1.109375 0.84375q0.375 0.515625 0.53125 1.21875q0.09375 0.46875 0.09375 1.625l0 6.0625l-1.671875 0l0 -6.0q0 -1.015625 -0.203125 -1.515625q-0.1875 -0.515625 -0.6875 -0.8125q-0.5 -0.296875 -1.171875 -0.296875q-1.0625 0 -1.84375 0.671875q-0.765625 0.671875 -0.765625 2.578125l0 5.375l-1.671875 0zm9.703857 -2.9375l1.65625 -0.265625q0.140625 1.0 0.765625 1.53125q0.640625 0.515625 1.78125 0.515625q1.15625 0 1.703125 -0.46875q0.5625 -0.46875 0.5625 -1.09375q0 -0.5625 -0.484375 -0.890625q-0.34375 -0.21875 -1.703125 -0.5625q-1.84375 -0.46875 -2.5625 -0.796875q-0.703125 -0.34375 -1.078125 -0.9375q-0.359375 -0.609375 -0.359375 -1.328125q0 -0.65625 0.296875 -1.21875q0.3125 -0.5625 0.828125 -0.9375q0.390625 -0.28125 1.0625 -0.484375q0.671875 -0.203125 1.4375 -0.203125q1.171875 0 2.046875 0.34375q0.875 0.328125 1.28125 0.90625q0.421875 0.5625 0.578125 1.515625l-1.625 0.21875q-0.109375 -0.75 -0.65625 -1.171875q-0.53125 -0.4375 -1.5 -0.4375q-1.15625 0 -1.640625 0.390625q-0.484375 0.375 -0.484375 0.875q0 0.328125 0.203125 0.59375q0.203125 0.265625 0.640625 0.4375q0.25 0.09375 1.46875 0.4375q1.765625 0.46875 2.46875 0.765625q0.703125 0.296875 1.09375 0.875q0.40625 0.578125 0.40625 1.4375q0 0.828125 -0.484375 1.578125q-0.484375 0.734375 -1.40625 1.140625q-0.921875 0.390625 -2.078125 0.390625q-1.921875 0 -2.9375 -0.796875q-1.0 -0.796875 -1.28125 -2.359375z" fill-rule="nonzero"></path><path fill="#0b5394" d="m65.80858 370.31448l1.234375 0.3125q-0.390625 1.515625 -1.40625 2.3125q-1.0 0.796875 -2.453125 0.796875q-1.5 0 -2.453125 -0.609375q-0.9375 -0.609375 -1.4375 -1.765625q-0.484375 -1.171875 -0.484375 -2.5q0 -1.453125 0.5625 -2.53125q0.5625 -1.09375 1.578125 -1.65625q1.03125 -0.5625 2.265625 -0.5625q1.390625 0 2.34375 0.71875q0.953125 0.703125 1.328125 2.0l-1.21875 0.28125q-0.328125 -1.015625 -0.9375 -1.46875q-0.609375 -0.46875 -1.546875 -0.46875q-1.078125 0 -1.796875 0.515625q-0.71875 0.515625 -1.015625 1.375q-0.28125 0.859375 -0.28125 1.78125q0 1.1875 0.34375 2.078125q0.34375 0.890625 1.0625 1.328125q0.734375 0.4375 1.59375 0.4375q1.03125 0 1.75 -0.59375q0.71875 -0.609375 0.96875 -1.78125zm7.2345276 2.4375q-0.625 0.53125 -1.21875 0.765625q-0.578125 0.21875 -1.25 0.21875q-1.125 0 -1.71875 -0.546875q-0.59375 -0.546875 -0.59375 -1.390625q0 -0.484375 0.21875 -0.890625q0.234375 -0.421875 0.59375 -0.671875q0.375 -0.25 0.828125 -0.375q0.328125 -0.078125 1.015625 -0.171875q1.375 -0.15625 2.03125 -0.390625q0.015625 -0.234375 0.015625 -0.296875q0 -0.703125 -0.328125 -0.984375q-0.4375 -0.390625 -1.296875 -0.390625q-0.8125 0 -1.203125 0.28125q-0.375 0.28125 -0.5625 1.0l-1.109375 -0.140625q0.140625 -0.71875 0.484375 -1.15625q0.359375 -0.453125 1.015625 -0.6875q0.671875 -0.234375 1.53125 -0.234375q0.875 0 1.40625 0.203125q0.546875 0.203125 0.796875 0.515625q0.25 0.296875 0.359375 0.765625q0.046875 0.296875 0.046875 1.0625l0 1.515625q0 1.59375 0.078125 2.015625q0.078125 0.421875 0.28125 0.8125l-1.1875 0q-0.171875 -0.359375 -0.234375 -0.828125zm-0.09375 -2.5625q-0.625 0.265625 -1.859375 0.4375q-0.703125 0.109375 -1.0 0.234375q-0.296875 0.125 -0.453125 0.375q-0.15625 0.234375 -0.15625 0.53125q0 0.453125 0.34375 0.765625q0.34375 0.296875 1.015625 0.296875q0.65625 0 1.171875 -0.28125q0.515625 -0.296875 0.765625 -0.796875q0.171875 -0.375 0.171875 -1.140625l0 -0.421875zm7.5062256 0.921875l1.125 0.140625q-0.171875 1.171875 -0.9375 1.828125q-0.765625 0.65625 -1.859375 0.65625q-1.390625 0 -2.234375 -0.90625q-0.828125 -0.90625 -0.828125 -2.59375q0 -1.09375 0.359375 -1.90625q0.359375 -0.828125 1.09375 -1.234375q0.734375 -0.40625 1.609375 -0.40625q1.09375 0 1.796875 0.5625q0.703125 0.546875 0.890625 1.5625l-1.109375 0.171875q-0.15625 -0.671875 -0.5625 -1.015625q-0.390625 -0.34375 -0.96875 -0.34375q-0.859375 0 -1.40625 0.625q-0.53125 0.609375 -0.53125 1.953125q0 1.359375 0.515625 1.984375q0.515625 0.609375 1.359375 0.609375q0.671875 0 1.125 -0.40625q0.453125 -0.421875 0.5625 -1.28125zm2.2734375 2.46875l0 -9.3125l1.140625 0l0 3.34375q0.796875 -0.921875 2.015625 -0.921875q0.75 0 1.296875 0.296875q0.5625 0.296875 0.796875 0.8125q0.234375 0.515625 0.234375 1.515625l0 4.265625l-1.140625 0l0 -4.265625q0 -0.859375 -0.375 -1.25q-0.359375 -0.390625 -1.046875 -0.390625q-0.5 0 -0.953125 0.265625q-0.453125 0.25 -0.640625 0.703125q-0.1875 0.453125 -0.1875 1.25l0 3.6875l-1.140625 0zm12.021851 -2.171875l1.1875 0.140625q-0.28125 1.046875 -1.046875 1.625q-0.75 0.5625 -1.921875 0.5625q-1.484375 0 -2.359375 -0.90625q-0.859375 -0.921875 -0.859375 -2.5625q0 -1.703125 0.875 -2.640625q0.890625 -0.9375 2.28125 -0.9375q1.359375 0 2.203125 0.921875q0.859375 0.921875 0.859375 2.578125q0 0.109375 0 0.3125l-5.03125 0q0.0625 1.109375 0.625 1.703125q0.5625 0.59375 1.40625 0.59375q0.640625 0 1.078125 -0.328125q0.453125 -0.34375 0.703125 -1.0625zm-3.75 -1.84375l3.765625 0q-0.078125 -0.859375 -0.4375 -1.28125q-0.546875 -0.65625 -1.40625 -0.65625q-0.796875 0 -1.328125 0.53125q-0.53125 0.515625 -0.59375 1.40625zm12.756088 3.0l0.15625 1.0q-0.484375 0.109375 -0.859375 0.109375q-0.625 0 -0.96875 -0.203125q-0.34375 -0.203125 -0.484375 -0.515625q-0.140625 -0.328125 -0.140625 -1.34375l0 -3.890625l-0.828125 0l0 -0.875l0.828125 0l0 -1.671875l1.140625 -0.6875l0 2.359375l1.15625 0l0 0.875l-1.15625 0l0 3.953125q0 0.484375 0.0625 0.625q0.0625 0.140625 0.1875 0.21875q0.140625 0.078125 0.390625 0.078125q0.203125 0 0.515625 -0.03125zm0.7811127 -2.359375q0 -1.875 1.03125 -2.765625q0.875 -0.75 2.125 -0.75q1.390625 0 2.265625 0.90625q0.890625 0.90625 0.890625 2.515625q0 1.296875 -0.390625 2.046875q-0.390625 0.75 -1.140625 1.171875q-0.75 0.40625 -1.625 0.40625q-1.421875 0 -2.296875 -0.90625q-0.859375 -0.90625 -0.859375 -2.625zm1.171875 0q0 1.296875 0.5625 1.953125q0.5625 0.640625 1.421875 0.640625q0.84375 0 1.40625 -0.640625q0.578125 -0.65625 0.578125 -1.984375q0 -1.25 -0.578125 -1.890625q-0.5625 -0.65625 -1.40625 -0.65625q-0.859375 0 -1.421875 0.640625q-0.5625 0.640625 -0.5625 1.9375zm10.693588 3.375l0 -1.296875l1.296875 0l0 1.296875l-1.296875 0zm2.9217377 -2.015625l1.125 -0.171875q0.09375 0.671875 0.53125 1.046875q0.4375 0.359375 1.21875 0.359375q0.78125 0 1.15625 -0.3125q0.390625 -0.328125 0.390625 -0.765625q0 -0.390625 -0.34375 -0.609375q-0.234375 -0.15625 -1.171875 -0.390625q-1.25 -0.3125 -1.734375 -0.546875q-0.484375 -0.234375 -0.734375 -0.640625q-0.25 -0.40625 -0.25 -0.90625q0 -0.453125 0.203125 -0.828125q0.203125 -0.390625 0.5625 -0.640625q0.265625 -0.203125 0.71875 -0.328125q0.46875 -0.140625 1.0 -0.140625q0.78125 0 1.375 0.234375q0.609375 0.21875 0.890625 0.609375q0.296875 0.390625 0.40625 1.046875l-1.125 0.15625q-0.078125 -0.53125 -0.4375 -0.8125q-0.359375 -0.296875 -1.03125 -0.296875q-0.78125 0 -1.125 0.265625q-0.34375 0.25 -0.34375 0.609375q0 0.21875 0.140625 0.390625q0.140625 0.1875 0.4375 0.3125q0.171875 0.0625 1.015625 0.28125q1.21875 0.328125 1.6875 0.53125q0.484375 0.203125 0.75 0.609375q0.28125 0.390625 0.28125 0.96875q0 0.578125 -0.34375 1.078125q-0.328125 0.5 -0.953125 0.78125q-0.625 0.28125 -1.421875 0.28125q-1.3125 0 -2.0 -0.546875q-0.6875 -0.546875 -0.875 -1.625zm7.1015625 2.015625l0 -6.734375l1.03125 0l0 1.015625q0.390625 -0.71875 0.71875 -0.9375q0.34375 -0.234375 0.734375 -0.234375q0.578125 0 1.171875 0.359375l-0.390625 1.0625q-0.421875 -0.25 -0.828125 -0.25q-0.375 0 -0.6875 0.234375q-0.296875 0.21875 -0.421875 0.625q-0.1875 0.609375 -0.1875 1.328125l0 3.53125l-1.140625 0zm8.84462 -2.46875l1.125 0.140625q-0.171875 1.171875 -0.9375 1.828125q-0.765625 0.65625 -1.859375 0.65625q-1.390625 0 -2.234375 -0.90625q-0.828125 -0.90625 -0.828125 -2.59375q0 -1.09375 0.359375 -1.90625q0.359375 -0.828125 1.09375 -1.234375q0.734375 -0.40625 1.609375 -0.40625q1.09375 0 1.796875 0.5625q0.703125 0.546875 0.890625 1.5625l-1.109375 0.171875q-0.15625 -0.671875 -0.5625 -1.015625q-0.390625 -0.34375 -0.96875 -0.34375q-0.859375 0 -1.40625 0.625q-0.53125 0.609375 -0.53125 1.953125q0 1.359375 0.515625 1.984375q0.515625 0.609375 1.359375 0.609375q0.671875 0 1.125 -0.40625q0.453125 -0.421875 0.5625 -1.28125zm2.2421875 2.46875l0 -9.3125l1.140625 0l0 9.3125l-1.140625 0zm2.99234 -7.984375l0 -1.328125l1.140625 0l0 1.328125l-1.140625 0zm0 7.984375l0 -6.734375l1.140625 0l0 6.734375l-1.140625 0zm4.007965 0l-1.0625 0l0 -9.3125l1.15625 0l0 3.328125q0.71875 -0.90625 1.84375 -0.90625q0.625 0 1.171875 0.25q0.5625 0.25 0.921875 0.703125q0.359375 0.453125 0.5625 1.09375q0.203125 0.640625 0.203125 1.375q0 1.734375 -0.859375 2.6875q-0.859375 0.9375 -2.0625 0.9375q-1.1875 0 -1.875 -1.0l0 0.84375zm-0.015625 -3.421875q0 1.21875 0.34375 1.75q0.53125 0.890625 1.453125 0.890625q0.75 0 1.296875 -0.65625q0.546875 -0.65625 0.546875 -1.9375q0 -1.328125 -0.53125 -1.953125q-0.515625 -0.625 -1.265625 -0.625q-0.75 0 -1.296875 0.65625q-0.546875 0.640625 -0.546875 1.875zm5.9281006 0.625l0 -1.140625l3.515625 0l0 1.140625l-3.515625 0zm9.28212 0.328125l1.125 0.140625q-0.171875 1.171875 -0.9375 1.828125q-0.765625 0.65625 -1.859375 0.65625q-1.390625 0 -2.234375 -0.90625q-0.828125 -0.90625 -0.828125 -2.59375q0 -1.09375 0.359375 -1.90625q0.359375 -0.828125 1.09375 -1.234375q0.734375 -0.40625 1.609375 -0.40625q1.09375 0 1.796875 0.5625q0.703125 0.546875 0.890625 1.5625l-1.109375 0.171875q-0.15625 -0.671875 -0.5625 -1.015625q-0.390625 -0.34375 -0.96875 -0.34375q-0.859375 0 -1.40625 0.625q-0.53125 0.609375 -0.53125 1.953125q0 1.359375 0.515625 1.984375q0.515625 0.609375 1.359375 0.609375q0.671875 0 1.125 -0.40625q0.453125 -0.421875 0.5625 -1.28125zm6.6640625 1.640625q-0.625 0.53125 -1.21875 0.765625q-0.578125 0.21875 -1.25 0.21875q-1.125 0 -1.71875 -0.546875q-0.59375 -0.546875 -0.59375 -1.390625q0 -0.484375 0.21875 -0.890625q0.234375 -0.421875 0.59375 -0.671875q0.375 -0.25 0.828125 -0.375q0.328125 -0.078125 1.015625 -0.171875q1.375 -0.15625 2.03125 -0.390625q0.015625 -0.234375 0.015625 -0.296875q0 -0.703125 -0.328125 -0.984375q-0.4375 -0.390625 -1.296875 -0.390625q-0.8125 0 -1.203125 0.28125q-0.375 0.28125 -0.5625 1.0l-1.109375 -0.140625q0.140625 -0.71875 0.484375 -1.15625q0.359375 -0.453125 1.015625 -0.6875q0.671875 -0.234375 1.53125 -0.234375q0.875 0 1.40625 0.203125q0.546875 0.203125 0.796875 0.515625q0.25 0.296875 0.359375 0.765625q0.046875 0.296875 0.046875 1.0625l0 1.515625q0 1.59375 0.078125 2.015625q0.078125 0.421875 0.28125 0.8125l-1.1875 0q-0.171875 -0.359375 -0.234375 -0.828125zm-0.09375 -2.5625q-0.625 0.265625 -1.859375 0.4375q-0.703125 0.109375 -1.0 0.234375q-0.296875 0.125 -0.453125 0.375q-0.15625 0.234375 -0.15625 0.53125q0 0.453125 0.34375 0.765625q0.34375 0.296875 1.015625 0.296875q0.65625 0 1.171875 -0.28125q0.515625 -0.296875 0.765625 -0.796875q0.171875 -0.375 0.171875 -1.140625l0 -0.421875zm7.5062256 0.921875l1.125 0.140625q-0.171875 1.171875 -0.9375 1.828125q-0.765625 0.65625 -1.859375 0.65625q-1.390625 0 -2.234375 -0.90625q-0.828125 -0.90625 -0.828125 -2.59375q0 -1.09375 0.359375 -1.90625q0.359375 -0.828125 1.09375 -1.234375q0.734375 -0.40625 1.609375 -0.40625q1.09375 0 1.796875 0.5625q0.703125 0.546875 0.890625 1.5625l-1.109375 0.171875q-0.15625 -0.671875 -0.5625 -1.015625q-0.390625 -0.34375 -0.96875 -0.34375q-0.859375 0 -1.40625 0.625q-0.53125 0.609375 -0.53125 1.953125q0 1.359375 0.515625 1.984375q0.515625 0.609375 1.359375 0.609375q0.671875 0 1.125 -0.40625q0.453125 -0.421875 0.5625 -1.28125zm2.2734375 2.46875l0 -9.3125l1.140625 0l0 3.34375q0.796875 -0.921875 2.015625 -0.921875q0.75 0 1.296875 0.296875q0.5625 0.296875 0.796875 0.8125q0.234375 0.515625 0.234375 1.515625l0 4.265625l-1.140625 0l0 -4.265625q0 -0.859375 -0.375 -1.25q-0.359375 -0.390625 -1.046875 -0.390625q-0.5 0 -0.953125 0.265625q-0.453125 0.25 -0.640625 0.703125q-0.1875 0.453125 -0.1875 1.25l0 3.6875l-1.140625 0zm12.021851 -2.171875l1.1875 0.140625q-0.28125 1.046875 -1.046875 1.625q-0.75 0.5625 -1.921875 0.5625q-1.484375 0 -2.359375 -0.90625q-0.859375 -0.921875 -0.859375 -2.5625q0 -1.703125 0.875 -2.640625q0.890625 -0.9375 2.28125 -0.9375q1.359375 0 2.203125 0.921875q0.859375 0.921875 0.859375 2.578125q0 0.109375 0 0.3125l-5.03125 0q0.0625 1.109375 0.625 1.703125q0.5625 0.59375 1.40625 0.59375q0.640625 0 1.078125 -0.328125q0.453125 -0.34375 0.703125 -1.0625zm-3.75 -1.84375l3.765625 0q-0.078125 -0.859375 -0.4375 -1.28125q-0.546875 -0.65625 -1.40625 -0.65625q-0.796875 0 -1.328125 0.53125q-0.53125 0.515625 -0.59375 1.40625zm5.6937256 4.171875l2.703125 -9.625l0.90625 0l-2.6875 9.625l-0.921875 0zm11.343613 -3.421875l1.234375 0.3125q-0.390625 1.515625 -1.40625 2.3125q-1.0 0.796875 -2.453125 0.796875q-1.5 0 -2.453125 -0.609375q-0.9375 -0.609375 -1.4375 -1.765625q-0.484375 -1.171875 -0.484375 -2.5q0 -1.453125 0.5625 -2.53125q0.5625 -1.09375 1.578125 -1.65625q1.03125 -0.5625 2.265625 -0.5625q1.390625 0 2.34375 0.71875q0.953125 0.703125 1.328125 2.0l-1.21875 0.28125q-0.328125 -1.015625 -0.9375 -1.46875q-0.609375 -0.46875 -1.546875 -0.46875q-1.078125 0 -1.796875 0.515625q-0.71875 0.515625 -1.015625 1.375q-0.28125 0.859375 -0.28125 1.78125q0 1.1875 0.34375 2.078125q0.34375 0.890625 1.0625 1.328125q0.734375 0.4375 1.59375 0.4375q1.03125 0 1.75 -0.59375q0.71875 -0.609375 0.96875 -1.78125zm2.6095276 -1.265625q0 -2.3125 1.234375 -3.625q1.25 -1.3125 3.21875 -1.3125q1.296875 0 2.328125 0.625q1.03125 0.609375 1.578125 1.71875q0.546875 1.09375 0.546875 2.484375q0 1.421875 -0.578125 2.546875q-0.5625 1.109375 -1.609375 1.6875q-1.046875 0.5625 -2.265625 0.5625q-1.3125 0 -2.359375 -0.625q-1.03125 -0.640625 -1.5625 -1.734375q-0.53125 -1.109375 -0.53125 -2.328125zm1.265625 0.015625q0 1.6875 0.90625 2.65625q0.90625 0.96875 2.28125 0.96875q1.390625 0 2.28125 -0.96875q0.90625 -0.984375 0.90625 -2.78125q0 -1.140625 -0.390625 -1.984375q-0.390625 -0.859375 -1.125 -1.3125q-0.734375 -0.46875 -1.65625 -0.46875q-1.3125 0 -2.265625 0.90625q-0.9375 0.890625 -0.9375 2.984375zm9.445175 4.515625l0 -9.3125l1.84375 0l2.203125 6.59375q0.3125 0.921875 0.453125 1.375q0.15625 -0.5 0.484375 -1.484375l2.234375 -6.484375l1.65625 0l0 9.3125l-1.1875 0l0 -7.78125l-2.703125 7.78125l-1.109375 0l-2.6875 -7.921875l0 7.921875l-1.1875 0zm11.102432 0l0 -9.3125l1.84375 0l2.203125 6.59375q0.3125 0.921875 0.453125 1.375q0.15625 -0.5 0.484375 -1.484375l2.234375 -6.484375l1.65625 0l0 9.3125l-1.1875 0l0 -7.78125l-2.703125 7.78125l-1.109375 0l-2.6875 -7.921875l0 7.921875l-1.1875 0zm11.352432 0l0 -9.3125l1.21875 0l0 9.3125l-1.21875 0zm5.8592377 0l0 -8.203125l-3.0625 0l0 -1.109375l7.375 0l0 1.109375l-3.078125 0l0 8.203125l-1.234375 0zm4.7663574 0.15625l2.703125 -9.625l0.90625 0l-2.6875 9.625l-0.921875 0zm4.6873627 -0.15625l0 -9.3125l1.265625 0l4.8906403 7.3125l0 -7.3125l1.1875 0l0 9.3125l-1.265625 0l-4.8906403 -7.3125l0 7.3125l-1.1875 0zm8.625168 0l3.578125 -9.3125l1.3125 0l3.8125 9.3125l-1.40625 0l-1.078125 -2.8125l-3.890625 0l-1.03125 2.8125l-1.296875 0zm2.6875 -3.828125l3.15625 0l-0.984375 -2.578125q-0.4375 -1.171875 -0.65625 -1.921875q-0.171875 0.890625 -0.5 1.78125l-1.015625 2.71875zm7.186615 3.828125l0 -9.3125l1.84375 0l2.203125 6.59375q0.3125 0.921875 0.453125 1.375q0.15625 -0.5 0.484375 -1.484375l2.234375 -6.484375l1.65625 0l0 9.3125l-1.1875 0l0 -7.78125l-2.703125 7.78125l-1.109375 0l-2.6875 -7.921875l0 7.921875l-1.1875 0zm11.1649475 0l0 -9.3125l6.71875 0l0 1.109375l-5.484375 0l0 2.84375l5.140625 0l0 1.09375l-5.140625 0l0 3.171875l5.703125 0l0 1.09375l-6.9375 0zm7.85849 0.15625l2.703125 -9.625l0.90625 0l-2.6875 9.625l-0.921875 0zm7.0779724 -0.15625l0 -8.203125l-3.0625 0l0 -1.109375l7.375 0l0 1.109375l-3.078125 0l0 8.203125l-1.234375 0zm8.391357 0l0 -3.9375l-3.59375 -5.375l1.5 0l1.84375 2.8125q0.5 0.78125 0.9375 1.578125q0.421875 -0.734375 1.015625 -1.640625l1.8125 -2.75l1.421875 0l-3.703125 5.375l0 3.9375l-1.234375 0zm6.2647705 0l0 -9.3125l3.515625 0q0.921875 0 1.40625 0.09375q0.6875 0.109375 1.15625 0.4375q0.46875 0.3125 0.75 0.890625q0.28125 0.578125 0.28125 1.28125q0 1.1875 -0.765625 2.015625q-0.75 0.8125 -2.71875 0.8125l-2.390625 0l0 3.78125l-1.234375 0zm1.234375 -4.875l2.40625 0q1.1875 0 1.6875 -0.4375q0.515625 -0.453125 0.515625 -1.265625q0 -0.578125 -0.296875 -0.984375q-0.296875 -0.421875 -0.78125 -0.5625q-0.3125 -0.078125 -1.15625 -0.078125l-2.375 0l0 3.328125zm7.6866455 4.875l0 -9.3125l6.71875 0l0 1.109375l-5.484375 0l0 2.84375l5.140625 0l0 1.09375l-5.140625 0l0 3.171875l5.703125 0l0 1.09375l-6.9375 0zm9.045959 0l0 -1.296875l1.296875 0l0 1.296875l-1.296875 0zm7.796753 0l0 -0.984375q-0.796875 1.140625 -2.140625 1.140625q-0.59375 0 -1.125 -0.234375q-0.515625 -0.234375 -0.765625 -0.578125q-0.25 -0.34375 -0.34375 -0.84375q-0.078125 -0.328125 -0.078125 -1.0625l0 -4.171875l1.140625 0l0 3.734375q0 0.890625 0.078125 1.203125q0.109375 0.453125 0.453125 0.71875q0.34375 0.25 0.859375 0.25q0.515625 0 0.96875 -0.265625q0.453125 -0.265625 0.640625 -0.71875q0.1875 -0.453125 0.1875 -1.3125l0 -3.609375l1.140625 0l0 6.734375l-1.015625 0zm2.9906006 0l0 -6.734375l1.03125 0l0 0.953125q0.734375 -1.109375 2.140625 -1.109375q0.609375 0 1.109375 0.21875q0.515625 0.21875 0.765625 0.578125q0.265625 0.34375 0.359375 0.84375q0.0625 0.3125 0.0625 1.109375l0 4.140625l-1.140625 0l0 -4.09375q0 -0.703125 -0.140625 -1.046875q-0.125 -0.34375 -0.46875 -0.546875q-0.328125 -0.21875 -0.78125 -0.21875q-0.734375 0 -1.265625 0.46875q-0.53125 0.453125 -0.53125 1.75l0 3.6875l-1.140625 0zm7.4124756 -7.984375l0 -1.328125l1.140625 0l0 1.328125l-1.140625 0zm0 7.984375l0 -6.734375l1.140625 0l0 6.734375l-1.140625 0zm5.4611206 -1.015625l0.15625 1.0q-0.484375 0.109375 -0.859375 0.109375q-0.625 0 -0.96875 -0.203125q-0.34375 -0.203125 -0.484375 -0.515625q-0.140625 -0.328125 -0.140625 -1.34375l0 -3.890625l-0.828125 0l0 -0.875l0.828125 0l0 -1.671875l1.140625 -0.6875l0 2.359375l1.15625 0l0 0.875l-1.15625 0l0 3.953125q0 0.484375 0.0625 0.625q0.0625 0.140625 0.1875 0.21875q0.140625 0.078125 0.390625 0.078125q0.203125 0 0.515625 -0.03125zm1.5310669 1.015625l0 -1.296875l1.296875 0l0 1.296875l-1.296875 0zm3.359253 -7.984375l0 -1.328125l1.15625 0l0 1.328125l-1.15625 0zm-1.4375 10.59375l0.21875 -0.96875q0.34375 0.09375 0.53125 0.09375q0.359375 0 0.515625 -0.234375q0.171875 -0.234375 0.171875 -1.15625l0 -7.078125l1.15625 0l0 7.109375q0 1.234375 -0.328125 1.71875q-0.421875 0.640625 -1.375 0.640625q-0.46875 0 -0.890625 -0.125zm3.9611206 -4.625l1.125 -0.171875q0.09375 0.671875 0.53125 1.046875q0.4375 0.359375 1.21875 0.359375q0.78125 0 1.15625 -0.3125q0.390625 -0.328125 0.390625 -0.765625q0 -0.390625 -0.34375 -0.609375q-0.234375 -0.15625 -1.171875 -0.390625q-1.25 -0.3125 -1.734375 -0.546875q-0.484375 -0.234375 -0.734375 -0.640625q-0.25 -0.40625 -0.25 -0.90625q0 -0.453125 0.203125 -0.828125q0.203125 -0.390625 0.5625 -0.640625q0.265625 -0.203125 0.71875 -0.328125q0.46875 -0.140625 1.0 -0.140625q0.78125 0 1.375 0.234375q0.609375 0.21875 0.890625 0.609375q0.296875 0.390625 0.40625 1.046875l-1.125 0.15625q-0.078125 -0.53125 -0.4375 -0.8125q-0.359375 -0.296875 -1.03125 -0.296875q-0.78125 0 -1.125 0.265625q-0.34375 0.25 -0.34375 0.609375q0 0.21875 0.140625 0.390625q0.140625 0.1875 0.4375 0.3125q0.171875 0.0625 1.015625 0.28125q1.21875 0.328125 1.6875 0.53125q0.484375 0.203125 0.75 0.609375q0.28125 0.390625 0.28125 0.96875q0 0.578125 -0.34375 1.078125q-0.328125 0.5 -0.953125 0.78125q-0.625 0.28125 -1.421875 0.28125q-1.3125 0 -2.0 -0.546875q-0.6875 -0.546875 -0.875 -1.625zm6.6953125 -1.359375q0 -1.875 1.03125 -2.765625q0.875 -0.75 2.125 -0.75q1.390625 0 2.265625 0.90625q0.890625 0.90625 0.890625 2.515625q0 1.296875 -0.390625 2.046875q-0.390625 0.75 -1.140625 1.171875q-0.75 0.40625 -1.625 0.40625q-1.421875 0 -2.296875 -0.90625q-0.859375 -0.90625 -0.859375 -2.625zm1.171875 0q0 1.296875 0.5625 1.953125q0.5625 0.640625 1.421875 0.640625q0.84375 0 1.40625 -0.640625q0.578125 -0.65625 0.578125 -1.984375q0 -1.25 -0.578125 -1.890625q-0.5625 -0.65625 -1.40625 -0.65625q-0.859375 0 -1.421875 0.640625q-0.5625 0.640625 -0.5625 1.9375zm6.6624756 3.375l0 -6.734375l1.03125 0l0 0.953125q0.734375 -1.109375 2.140625 -1.109375q0.609375 0 1.109375 0.21875q0.515625 0.21875 0.765625 0.578125q0.265625 0.34375 0.359375 0.84375q0.0625 0.3125 0.0625 1.109375l0 4.140625l-1.140625 0l0 -4.09375q0 -0.703125 -0.140625 -1.046875q-0.125 -0.34375 -0.46875 -0.546875q-0.328125 -0.21875 -0.78125 -0.21875q-0.734375 0 -1.265625 0.46875q-0.53125 0.453125 -0.53125 1.75l0 3.6875l-1.140625 0z" fill-rule="nonzero"></path><path fill="#000000" fill-opacity="0.0" d="m220.69144 171.41003l0 18.607208" fill-rule="nonzero"></path><path stroke="#cfe2f3" stroke-width="1.0" stroke-linejoin="round" stroke-linecap="butt" d="m220.69144 171.41003l0 12.607208" fill-rule="evenodd"></path><path fill="#cfe2f3" stroke="#cfe2f3" stroke-width="1.0" stroke-linecap="butt" d="m219.0397 184.01724l1.6517334 4.538101l1.6517334 -4.538101z" fill-rule="evenodd"></path><path fill="#000000" fill-opacity="0.0" d="m220.69144 242.23772l0 18.604568" fill-rule="nonzero"></path><path stroke="#cfe2f3" stroke-width="1.0" stroke-linejoin="round" stroke-linecap="butt" d="m220.69144 242.23772l0 12.604584" fill-rule="evenodd"></path><path fill="#cfe2f3" stroke="#cfe2f3" stroke-width="1.0" stroke-linecap="butt" d="m219.0397 254.8423l1.6517334 4.538101l1.6517334 -4.538101z" fill-rule="evenodd"></path><path fill="#000000" fill-opacity="0.0" d="m220.00262 316.01633l0 15.653534" fill-rule="nonzero"></path><path stroke="#cfe2f3" stroke-width="1.0" stroke-linejoin="round" stroke-linecap="butt" d="m220.00262 316.01633l0 9.653534" fill-rule="evenodd"></path><path fill="#cfe2f3" stroke="#cfe2f3" stroke-width="1.0" stroke-linecap="butt" d="m218.35089 325.66986l1.6517334 4.5381165l1.6517334 -4.5381165z" fill-rule="evenodd"></path><path fill="#b6d7a8" d="m20.506561 428.63312l398.99213 0l0 396.8819l-398.99213 0z" fill-rule="nonzero"></path><path stroke="#93c47d" stroke-width="1.0" stroke-linejoin="round" stroke-linecap="butt" d="m20.506561 428.63312l398.99213 0l0 396.8819l-398.99213 0z" fill-rule="nonzero"></path><path fill="#38761d" d="m157.61115 455.55313l0 -13.59375l4.421875 0q2.5 0 3.265625 0.203125q1.15625 0.296875 1.9375 1.328125q0.796875 1.015625 0.796875 2.640625q0 1.25 -0.453125 2.109375q-0.453125 0.859375 -1.15625 1.34375q-0.703125 0.484375 -1.421875 0.640625q-0.984375 0.203125 -2.84375 0.203125l-1.796875 0l0 5.125l-2.75 0zm2.75 -11.296875l0 3.859375l1.5 0q1.625 0 2.171875 -0.21875q0.546875 -0.21875 0.859375 -0.671875q0.3125 -0.453125 0.3125 -1.046875q0 -0.75 -0.4375 -1.234375q-0.4375 -0.484375 -1.09375 -0.59375q-0.5 -0.09375 -1.984375 -0.09375l-1.328125 0zm9.677948 11.296875l0 -13.59375l2.609375 0l0 13.59375l-2.609375 0zm7.136429 -6.84375l-2.359375 -0.4375q0.390625 -1.421875 1.359375 -2.109375q0.984375 -0.6875 2.90625 -0.6875q1.734375 0 2.59375 0.421875q0.859375 0.40625 1.203125 1.046875q0.34375 0.625 0.34375 2.328125l-0.03125 3.046875q0 1.296875 0.125 1.921875q0.125 0.609375 0.46875 1.3125l-2.578125 0q-0.09375 -0.265625 -0.25 -0.765625q-0.0625 -0.234375 -0.09375 -0.3125q-0.65625 0.65625 -1.421875 0.984375q-0.765625 0.3125 -1.625 0.3125q-1.515625 0 -2.40625 -0.8125q-0.875 -0.828125 -0.875 -2.09375q0 -0.84375 0.390625 -1.484375q0.40625 -0.65625 1.125 -1.0q0.71875 -0.359375 2.078125 -0.625q1.828125 -0.328125 2.53125 -0.625l0 -0.265625q0 -0.75 -0.375 -1.0625q-0.359375 -0.328125 -1.390625 -0.328125q-0.703125 0 -1.09375 0.28125q-0.390625 0.265625 -0.625 0.953125zm3.484375 2.109375q-0.5 0.171875 -1.59375 0.40625q-1.078125 0.234375 -1.40625 0.453125q-0.515625 0.359375 -0.515625 0.921875q0 0.546875 0.40625 0.953125q0.40625 0.390625 1.046875 0.390625q0.703125 0 1.34375 -0.46875q0.46875 -0.359375 0.625 -0.859375q0.09375 -0.34375 0.09375 -1.28125l0 -0.515625zm13.906967 4.734375l-2.609375 0l0 -5.03125q0 -1.59375 -0.171875 -2.0625q-0.15625 -0.46875 -0.53125 -0.71875q-0.375 -0.265625 -0.90625 -0.265625q-0.6875 0 -1.234375 0.375q-0.53125 0.359375 -0.734375 0.984375q-0.1875 0.609375 -0.1875 2.25l0 4.46875l-2.609375 0l0 -9.859375l2.421875 0l0 1.453125q1.296875 -1.671875 3.25 -1.671875q0.859375 0 1.578125 0.3125q0.71875 0.3125 1.078125 0.796875q0.359375 0.484375 0.5 1.09375q0.15625 0.609375 0.15625 1.75l0 6.125zm11.93866 4.0l-1.796875 0q-1.40625 -2.140625 -2.15625 -4.453125q-0.734375 -2.3125 -0.734375 -4.46875q0 -2.6875 0.90625 -5.078125q0.796875 -2.078125 2.03125 -3.828125l1.78125 0q-1.28125 2.8125 -1.765625 4.78125q-0.46875 1.96875 -0.46875 4.171875q0 1.53125 0.28125 3.125q0.28125 1.59375 0.78125 3.03125q0.328125 0.953125 1.140625 2.71875zm1.900177 -4.0l0 -13.59375l4.421875 0q2.5 0 3.265625 0.203125q1.15625 0.296875 1.9375 1.328125q0.796875 1.015625 0.796875 2.640625q0 1.25 -0.453125 2.109375q-0.453125 0.859375 -1.15625 1.34375q-0.703125 0.484375 -1.421875 0.640625q-0.984375 0.203125 -2.84375 0.203125l-1.796875 0l0 5.125l-2.75 0zm2.75 -11.296875l0 3.859375l1.5 0q1.625 0 2.171875 -0.21875q0.546875 -0.21875 0.859375 -0.671875q0.3125 -0.453125 0.3125 -1.046875q0 -0.75 -0.4375 -1.234375q-0.4375 -0.484375 -1.09375 -0.59375q-0.5 -0.09375 -1.984375 -0.09375l-1.328125 0zm12.287323 -2.296875l0 5.0q1.25 -1.484375 3.015625 -1.484375q0.890625 0 1.609375 0.34375q0.734375 0.328125 1.09375 0.84375q0.375 0.515625 0.5 1.15625q0.140625 0.625 0.140625 1.953125l0 5.78125l-2.609375 0l0 -5.203125q0 -1.546875 -0.15625 -1.96875q-0.140625 -0.421875 -0.515625 -0.65625q-0.375 -0.25 -0.9375 -0.25q-0.65625 0 -1.171875 0.3125q-0.5 0.3125 -0.734375 0.953125q-0.234375 0.640625 -0.234375 1.875l0 4.9375l-2.609375 0l0 -13.59375l2.609375 0zm10.739731 6.75l-2.359375 -0.4375q0.390625 -1.421875 1.359375 -2.109375q0.984375 -0.6875 2.90625 -0.6875q1.734375 0 2.59375 0.421875q0.859375 0.40625 1.203125 1.046875q0.34375 0.625 0.34375 2.328125l-0.03125 3.046875q0 1.296875 0.125 1.921875q0.125 0.609375 0.46875 1.3125l-2.578125 0q-0.09375 -0.265625 -0.25 -0.765625q-0.0625 -0.234375 -0.09375 -0.3125q-0.65625 0.65625 -1.421875 0.984375q-0.765625 0.3125 -1.625 0.3125q-1.515625 0 -2.40625 -0.8125q-0.875 -0.828125 -0.875 -2.09375q0 -0.84375 0.390625 -1.484375q0.40625 -0.65625 1.125 -1.0q0.71875 -0.359375 2.078125 -0.625q1.828125 -0.328125 2.53125 -0.625l0 -0.265625q0 -0.75 -0.375 -1.0625q-0.359375 -0.328125 -1.390625 -0.328125q-0.703125 0 -1.09375 0.28125q-0.390625 0.265625 -0.625 0.953125zm3.484375 2.109375q-0.5 0.171875 -1.59375 0.40625q-1.078125 0.234375 -1.40625 0.453125q-0.515625 0.359375 -0.515625 0.921875q0 0.546875 0.40625 0.953125q0.40625 0.390625 1.046875 0.390625q0.703125 0 1.34375 -0.46875q0.46875 -0.359375 0.625 -0.859375q0.09375 -0.34375 0.09375 -1.28125l0 -0.515625zm4.031967 1.921875l2.609375 -0.390625q0.171875 0.75 0.671875 1.15625q0.515625 0.390625 1.4375 0.390625q1.0 0 1.515625 -0.375q0.34375 -0.265625 0.34375 -0.703125q0 -0.296875 -0.1875 -0.484375q-0.1875 -0.1875 -0.875 -0.34375q-3.140625 -0.703125 -4.0 -1.265625q-1.15625 -0.796875 -1.15625 -2.21875q0 -1.28125 1.0 -2.15625q1.015625 -0.875 3.140625 -0.875q2.03125 0 3.0 0.65625q0.984375 0.65625 1.359375 1.953125l-2.453125 0.453125q-0.15625 -0.578125 -0.609375 -0.875q-0.4375 -0.3125 -1.25 -0.3125q-1.03125 0 -1.46875 0.296875q-0.296875 0.203125 -0.296875 0.515625q0 0.28125 0.25 0.484375q0.359375 0.25 2.4375 0.734375q2.078125 0.46875 2.90625 1.15625q0.828125 0.6875 0.828125 1.9375q0 1.359375 -1.140625 2.328125q-1.125 0.96875 -3.34375 0.96875q-2.015625 0 -3.1875 -0.8125q-1.171875 -0.8125 -1.53125 -2.21875zm16.985107 -0.328125l2.609375 0.4375q-0.5 1.4375 -1.59375 2.1875q-1.078125 0.734375 -2.703125 0.734375q-2.5625153 0 -3.7968903 -1.671875q-0.96875 -1.34375 -0.96875 -3.40625q0 -2.4375 1.265625 -3.828125q1.28125 -1.390625 3.2500153 -1.390625q2.1875 0 3.453125 1.453125q1.28125 1.453125 1.234375 4.453125l-6.5312653 0q0.015625 1.15625 0.625 1.8125q0.60939026 0.640625 1.5000153 0.640625q0.609375 0 1.03125 -0.328125q0.421875 -0.34375 0.625 -1.09375zm0.15625 -2.625q-0.03125 -1.140625 -0.59375 -1.71875q-0.546875 -0.59375 -1.34375 -0.59375q-0.859375 0 -1.4062653 0.625q-0.5625 0.609375 -0.546875 1.6875l3.8906403 0zm17.949615 3.34375l0 2.421875l-9.1405945 0q0.15625 -1.375 0.890625 -2.59375q0.75 -1.234375 2.9375 -3.265625q1.765625 -1.640625 2.15625 -2.234375q0.546875 -0.796875 0.546875 -1.59375q0 -0.875 -0.46875 -1.34375q-0.46875 -0.46875 -1.296875 -0.46875q-0.8125 0 -1.296875 0.5q-0.484375 0.484375 -0.5625 1.625l-2.59375 -0.25q0.234375 -2.15625 1.453125 -3.09375q1.21875 -0.9375 3.0625 -0.9375q2.015625 0 3.15625 1.09375q1.1562195 1.078125 1.1562195 2.6875q0 0.921875 -0.32809448 1.75q-0.328125 0.828125 -1.046875 1.734375q-0.46875 0.609375 -1.703125 1.75q-1.234375 1.125 -1.5625 1.5q-0.328125 0.359375 -0.53125 0.71875l5.1718445 0zm1.4069824 6.421875q0.765625 -1.65625 1.078125 -2.546875q0.328125 -0.875 0.59375 -2.015625q0.265625 -1.15625 0.390625 -2.1875q0.140625 -1.03125 0.140625 -2.125q0 -2.203125 -0.484375 -4.171875q-0.46875 -1.96875 -1.734375 -4.78125l1.765625 0q1.40625 1.984375 2.171875 4.234375q0.78125 2.234375 0.78125 4.53125q0 1.9375 -0.609375 4.15625q-0.703125 2.484375 -2.296875 4.90625l-1.796875 0z" fill-rule="nonzero"></path><path fill="#d9ead3" d="m56.816273 474.05832l325.92123 0l0 34.393707l-325.92123 0z" fill-rule="nonzero"></path><path fill="#38761d" d="m106.160194 498.17517l0 -13.59375l6.03125 0q1.8125 0 2.75 0.359375q0.953125 0.359375 1.515625 1.296875q0.5625 0.921875 0.5625 2.046875q0 1.453125 -0.9375 2.453125q-0.921875 0.984375 -2.890625 1.25q0.71875 0.34375 1.09375 0.671875q0.78125 0.734375 1.484375 1.8125l2.375 3.703125l-2.265625 0l-1.796875 -2.828125q-0.796875 -1.21875 -1.3125 -1.875q-0.5 -0.65625 -0.90625 -0.90625q-0.40625 -0.265625 -0.8125 -0.359375q-0.3125 -0.078125 -1.015625 -0.078125l-2.078125 0l0 6.046875l-1.796875 0zm1.796875 -7.59375l3.859375 0q1.234375 0 1.921875 -0.25q0.703125 -0.265625 1.0625 -0.828125q0.375 -0.5625 0.375 -1.21875q0 -0.96875 -0.703125 -1.578125q-0.703125 -0.625 -2.21875 -0.625l-4.296875 0l0 4.5zm18.176071 4.421875l1.71875 0.21875q-0.40625 1.5 -1.515625 2.34375q-1.09375 0.828125 -2.8125 0.828125q-2.15625 0 -3.421875 -1.328125q-1.265625 -1.328125 -1.265625 -3.734375q0 -2.484375 1.265625 -3.859375q1.28125 -1.375 3.328125 -1.375q1.984375 0 3.234375 1.34375q1.25 1.34375 1.25 3.796875q0 0.140625 -0.015625 0.4375l-7.34375 0q0.09375 1.625 0.921875 2.484375q0.828125 0.859375 2.0625 0.859375q0.90625 0 1.546875 -0.46875q0.65625 -0.484375 1.046875 -1.546875zm-5.484375 -2.703125l5.5 0q-0.109375 -1.234375 -0.625 -1.859375q-0.796875 -0.96875 -2.078125 -0.96875q-1.140625 0 -1.9375 0.78125q-0.78125 0.765625 -0.859375 2.046875zm15.547585 4.65625q-0.9375 0.796875 -1.796875 1.125q-0.859375 0.3125 -1.84375 0.3125q-1.609375 0 -2.484375 -0.78125q-0.875 -0.796875 -0.875 -2.03125q0 -0.734375 0.328125 -1.328125q0.328125 -0.59375 0.859375 -0.953125q0.53125 -0.359375 1.203125 -0.546875q0.5 -0.140625 1.484375 -0.25q2.03125 -0.25 2.984375 -0.578125q0 -0.34375 0 -0.4375q0 -1.015625 -0.46875 -1.4375q-0.640625 -0.5625 -1.90625 -0.5625q-1.171875 0 -1.734375 0.40625q-0.5625 0.40625 -0.828125 1.46875l-1.640625 -0.234375q0.234375 -1.046875 0.734375 -1.6875q0.515625 -0.640625 1.46875 -0.984375q0.96875 -0.359375 2.25 -0.359375q1.265625 0 2.046875 0.296875q0.78125 0.296875 1.15625 0.75q0.375 0.453125 0.515625 1.140625q0.09375 0.421875 0.09375 1.53125l0 2.234375q0 2.328125 0.09375 2.953125q0.109375 0.609375 0.4375 1.171875l-1.75 0q-0.265625 -0.515625 -0.328125 -1.21875zm-0.140625 -3.71875q-0.90625 0.359375 -2.734375 0.625q-1.03125 0.140625 -1.453125 0.328125q-0.421875 0.1875 -0.65625 0.546875q-0.234375 0.359375 -0.234375 0.796875q0 0.671875 0.5 1.125q0.515625 0.4375 1.484375 0.4375q0.96875 0 1.71875 -0.421875q0.75 -0.4375 1.109375 -1.15625q0.265625 -0.578125 0.265625 -1.671875l0 -0.609375zm10.469467 4.9375l0 -1.25q-0.9375 1.46875 -2.75 1.46875q-1.171875 0 -2.171875 -0.640625q-0.984375 -0.65625 -1.53125 -1.8125q-0.53125 -1.171875 -0.53125 -2.6875q0 -1.46875 0.484375 -2.671875q0.5 -1.203125 1.46875 -1.84375q0.984375 -0.640625 2.203125 -0.640625q0.890625 0 1.578125 0.375q0.703125 0.375 1.140625 0.984375l0 -4.875l1.65625 0l0 13.59375l-1.546875 0zm-5.28125 -4.921875q0 1.890625 0.796875 2.828125q0.8125 0.9375 1.890625 0.9375q1.09375 0 1.859375 -0.890625q0.765625 -0.890625 0.765625 -2.734375q0 -2.015625 -0.78125 -2.953125q-0.78125 -0.953125 -1.921875 -0.953125q-1.109375 0 -1.859375 0.90625q-0.75 0.90625 -0.75 2.859375zm13.777771 1.984375l1.65625 -0.265625q0.140625 1.0 0.765625 1.53125q0.640625 0.515625 1.78125 0.515625q1.15625 0 1.703125 -0.46875q0.5625 -0.46875 0.5625 -1.09375q0 -0.5625 -0.484375 -0.890625q-0.34375 -0.21875 -1.703125 -0.5625q-1.84375 -0.46875 -2.5625 -0.796875q-0.703125 -0.34375 -1.078125 -0.9375q-0.359375 -0.609375 -0.359375 -1.328125q0 -0.65625 0.296875 -1.21875q0.3125 -0.5625 0.828125 -0.9375q0.390625 -0.28125 1.0625 -0.484375q0.671875 -0.203125 1.4375 -0.203125q1.171875 0 2.046875 0.34375q0.875 0.328125 1.28125 0.90625q0.421875 0.5625 0.578125 1.515625l-1.625 0.21875q-0.109375 -0.75 -0.65625 -1.171875q-0.53125 -0.4375 -1.5 -0.4375q-1.15625 0 -1.640625 0.390625q-0.484375 0.375 -0.484375 0.875q0 0.328125 0.203125 0.59375q0.203125 0.265625 0.640625 0.4375q0.25 0.09375 1.46875 0.4375q1.765625 0.46875 2.46875 0.765625q0.703125 0.296875 1.09375 0.875q0.40625 0.578125 0.40625 1.4375q0 0.828125 -0.484375 1.578125q-0.484375 0.734375 -1.40625 1.140625q-0.921875 0.390625 -2.078125 0.390625q-1.921875 0 -2.9375 -0.796875q-1.0 -0.796875 -1.28125 -2.359375zm9.375 -1.984375q0 -2.734375 1.53125 -4.0625q1.265625 -1.09375 3.09375 -1.09375q2.03125 0 3.3125 1.34375q1.296875 1.328125 1.296875 3.671875q0 1.90625 -0.578125 3.0q-0.5625 1.078125 -1.65625 1.6875q-1.078125 0.59375 -2.375 0.59375q-2.0625 0 -3.34375 -1.328125q-1.28125 -1.328125 -1.28125 -3.8125zm1.71875 0q0 1.890625 0.828125 2.828125q0.828125 0.9375 2.078125 0.9375q1.25 0 2.0625 -0.9375q0.828125 -0.953125 0.828125 -2.890625q0 -1.828125 -0.828125 -2.765625q-0.828125 -0.9375 -2.0625 -0.9375q-1.25 0 -2.078125 0.9375q-0.828125 0.9375 -0.828125 2.828125zm15.735092 4.921875l0 -1.453125q-1.140625 1.671875 -3.125 1.671875q-0.859375 0 -1.625 -0.328125q-0.75 -0.34375 -1.125 -0.84375q-0.359375 -0.5 -0.515625 -1.234375q-0.09375 -0.5 -0.09375 -1.5625l0 -6.109375l1.671875 0l0 5.46875q0 1.3125 0.09375 1.765625q0.15625 0.65625 0.671875 1.03125q0.515625 0.375 1.265625 0.375q0.75 0 1.40625 -0.375q0.65625 -0.390625 0.921875 -1.046875q0.28125 -0.671875 0.28125 -1.9375l0 -5.28125l1.671875 0l0 9.859375l-1.5 0zm3.9069672 0l0 -9.859375l1.5 0l0 1.5q0.578125 -1.046875 1.0625 -1.375q0.484375 -0.34375 1.078125 -0.34375q0.84375 0 1.71875 0.546875l-0.578125 1.546875q-0.609375 -0.359375 -1.234375 -0.359375q-0.546875 0 -0.984375 0.328125q-0.421875 0.328125 -0.609375 0.90625q-0.28125 0.890625 -0.28125 1.953125l0 5.15625l-1.671875 0zm12.665802 -3.609375l1.640625 0.21875q-0.265625 1.6875 -1.375 2.65625q-1.109375 0.953125 -2.734375 0.953125q-2.015625 0 -3.25 -1.3125q-1.21875 -1.328125 -1.21875 -3.796875q0 -1.59375 0.515625 -2.78125q0.53125 -1.203125 1.609375 -1.796875q1.09375 -0.609375 2.359375 -0.609375q1.609375 0 2.625 0.8125q1.015625 0.8125 1.3125 2.3125l-1.625 0.25q-0.234375 -1.0 -0.828125 -1.5q-0.59375 -0.5 -1.421875 -0.5q-1.265625 0 -2.0625 0.90625q-0.78125 0.90625 -0.78125 2.859375q0 1.984375 0.765625 2.890625q0.765625 0.890625 1.984375 0.890625q0.984375 0 1.640625 -0.59375q0.65625 -0.609375 0.84375 -1.859375zm9.640625 0.4375l1.71875 0.21875q-0.40625 1.5 -1.515625 2.34375q-1.09375 0.828125 -2.8125 0.828125q-2.15625 0 -3.421875 -1.328125q-1.265625 -1.328125 -1.265625 -3.734375q0 -2.484375 1.265625 -3.859375q1.28125 -1.375 3.328125 -1.375q1.984375 0 3.234375 1.34375q1.25 1.34375 1.25 3.796875q0 0.140625 -0.015625 0.4375l-7.34375 0q0.09375 1.625 0.921875 2.484375q0.828125 0.859375 2.0625 0.859375q0.90625 0 1.546875 -0.46875q0.65625 -0.484375 1.046875 -1.546875zm-5.484375 -2.703125l5.5 0q-0.109375 -1.234375 -0.625 -1.859375q-0.796875 -0.96875 -2.078125 -0.96875q-1.140625 0 -1.9375 0.78125q-0.78125 0.765625 -0.859375 2.046875zm20.746521 5.875l0 -1.453125q-1.140625 1.671875 -3.125 1.671875q-0.859375 0 -1.625 -0.328125q-0.75 -0.34375 -1.125 -0.84375q-0.359375 -0.5 -0.515625 -1.234375q-0.09375 -0.5 -0.09375 -1.5625l0 -6.109375l1.671875 0l0 5.46875q0 1.3125 0.09375 1.765625q0.15625 0.65625 0.671875 1.03125q0.515625 0.375 1.265625 0.375q0.75 0 1.40625 -0.375q0.65625 -0.390625 0.921875 -1.046875q0.28125 -0.671875 0.28125 -1.9375l0 -5.28125l1.671875 0l0 9.859375l-1.5 0zm3.9225922 0l0 -9.859375l1.5 0l0 1.40625q1.09375 -1.625 3.140625 -1.625q0.890625 0 1.640625 0.328125q0.75 0.3125 1.109375 0.84375q0.375 0.515625 0.53125 1.21875q0.09375 0.46875 0.09375 1.625l0 6.0625l-1.671875 0l0 -6.0q0 -1.015625 -0.203125 -1.515625q-0.1875 -0.515625 -0.6875 -0.8125q-0.5 -0.296875 -1.171875 -0.296875q-1.0625 0 -1.84375 0.671875q-0.765625 0.671875 -0.765625 2.578125l0 5.375l-1.671875 0zm10.391342 -11.6875l0 -1.90625l1.671875 0l0 1.90625l-1.671875 0zm0 11.6875l0 -9.859375l1.671875 0l0 9.859375l-1.671875 0zm7.785446 -1.5l0.234375 1.484375q-0.703125 0.140625 -1.265625 0.140625q-0.90625 0 -1.40625 -0.28125q-0.5 -0.296875 -0.703125 -0.75q-0.203125 -0.46875 -0.203125 -1.984375l0 -5.65625l-1.234375 0l0 -1.3125l1.234375 0l0 -2.4375l1.65625 -1.0l0 3.4375l1.6875 0l0 1.3125l-1.6875 0l0 5.75q0 0.71875 0.078125 0.921875q0.09375 0.203125 0.296875 0.328125q0.203125 0.125 0.578125 0.125q0.265625 0 0.734375 -0.078125zm13.100983 1.5l0 -1.25q-0.9375 1.46875 -2.75 1.46875q-1.171875 0 -2.171875 -0.640625q-0.984375 -0.65625 -1.53125 -1.8125q-0.53125 -1.171875 -0.53125 -2.6875q0 -1.46875 0.484375 -2.671875q0.5 -1.203125 1.46875 -1.84375q0.984375 -0.640625 2.203125 -0.640625q0.890625 0 1.578125 0.375q0.703125 0.375 1.140625 0.984375l0 -4.875l1.65625 0l0 13.59375l-1.546875 0zm-5.28125 -4.921875q0 1.890625 0.796875 2.828125q0.8125 0.9375 1.890625 0.9375q1.09375 0 1.859375 -0.890625q0.765625 -0.890625 0.765625 -2.734375q0 -2.015625 -0.78125 -2.953125q-0.78125 -0.953125 -1.921875 -0.953125q-1.109375 0 -1.859375 0.90625q-0.75 0.90625 -0.75 2.859375zm16.016357 1.75l1.71875 0.21875q-0.40625 1.5 -1.515625 2.34375q-1.09375 0.828125 -2.8125 0.828125q-2.15625 0 -3.421875 -1.328125q-1.265625 -1.328125 -1.265625 -3.734375q0 -2.484375 1.265625 -3.859375q1.28125 -1.375 3.328125 -1.375q1.984375 0 3.234375 1.34375q1.25 1.34375 1.25 3.796875q0 0.140625 -0.015625 0.4375l-7.34375 0q0.09375 1.625 0.921875 2.484375q0.828125 0.859375 2.0625 0.859375q0.90625 0 1.546875 -0.46875q0.65625 -0.484375 1.046875 -1.546875zm-5.484375 -2.703125l5.5 0q-0.109375 -1.234375 -0.625 -1.859375q-0.796875 -0.96875 -2.078125 -0.96875q-1.140625 0 -1.9375 0.78125q-0.78125 0.765625 -0.859375 2.046875zm9.516327 5.875l0 -8.546875l-1.484375 0l0 -1.3125l1.484375 0l0 -1.046875q0 -0.984375 0.171875 -1.46875q0.234375 -0.65625 0.84375 -1.046875q0.609375 -0.40625 1.703125 -0.40625q0.703125 0 1.5625 0.15625l-0.25 1.46875q-0.515625 -0.09375 -0.984375 -0.09375q-0.765625 0 -1.078125 0.328125q-0.3125 0.3125 -0.3125 1.203125l0 0.90625l1.921875 0l0 1.3125l-1.921875 0l0 8.546875l-1.65625 0zm4.792694 -11.6875l0 -1.90625l1.671875 0l0 1.90625l-1.671875 0zm0 11.6875l0 -9.859375l1.671875 0l0 9.859375l-1.671875 0zm4.129181 0l0 -9.859375l1.5 0l0 1.40625q1.09375 -1.625 3.140625 -1.625q0.890625 0 1.640625 0.328125q0.75 0.3125 1.109375 0.84375q0.375 0.515625 0.53125 1.21875q0.09375 0.46875 0.09375 1.625l0 6.0625l-1.671875 0l0 -6.0q0 -1.015625 -0.203125 -1.515625q-0.1875 -0.515625 -0.6875 -0.8125q-0.5 -0.296875 -1.171875 -0.296875q-1.0625 0 -1.84375 0.671875q-0.765625 0.671875 -0.765625 2.578125l0 5.375l-1.671875 0zm10.391357 -11.6875l0 -1.90625l1.671875 0l0 1.90625l-1.671875 0zm0 11.6875l0 -9.859375l1.671875 0l0 9.859375l-1.671875 0zm7.785431 -1.5l0.234375 1.484375q-0.703125 0.140625 -1.265625 0.140625q-0.90625 0 -1.40625 -0.28125q-0.5 -0.296875 -0.703125 -0.75q-0.203125 -0.46875 -0.203125 -1.984375l0 -5.65625l-1.234375 0l0 -1.3125l1.234375 0l0 -2.4375l1.65625 -1.0l0 3.4375l1.6875 0l0 1.3125l-1.6875 0l0 5.75q0 0.71875 0.078125 0.921875q0.09375 0.203125 0.296875 0.328125q0.203125 0.125 0.578125 0.125q0.265625 0 0.734375 -0.078125zm1.5426941 -10.1875l0 -1.90625l1.671875 0l0 1.90625l-1.671875 0zm0 11.6875l0 -9.859375l1.671875 0l0 9.859375l-1.671875 0zm3.504181 -4.921875q0 -2.734375 1.53125 -4.0625q1.265625 -1.09375 3.09375 -1.09375q2.03125 0 3.3125305 1.34375q1.296875 1.328125 1.296875 3.671875q0 1.90625 -0.578125 3.0q-0.5625 1.078125 -1.6562805 1.6875q-1.078125 0.59375 -2.375 0.59375q-2.0625 0 -3.34375 -1.328125q-1.28125 -1.328125 -1.28125 -3.8125zm1.71875 0q0 1.890625 0.828125 2.828125q0.828125 0.9375 2.078125 0.9375q1.25 0 2.0625 -0.9375q0.8281555 -0.953125 0.8281555 -2.890625q0 -1.828125 -0.8281555 -2.765625q-0.828125 -0.9375 -2.0625 -0.9375q-1.25 0 -2.078125 0.9375q-0.828125 0.9375 -0.828125 2.828125zm9.281982 4.921875l0 -9.859375l1.5 0l0 1.40625q1.09375 -1.625 3.140625 -1.625q0.890625 0 1.640625 0.328125q0.75 0.3125 1.109375 0.84375q0.375 0.515625 0.53125 1.21875q0.09375 0.46875 0.09375 1.625l0 6.0625l-1.671875 0l0 -6.0q0 -1.015625 -0.203125 -1.515625q-0.1875 -0.515625 -0.6875 -0.8125q-0.5 -0.296875 -1.171875 -0.296875q-1.0625 0 -1.84375 0.671875q-0.765625 0.671875 -0.765625 2.578125l0 5.375l-1.671875 0zm9.703827 -2.9375l1.65625 -0.265625q0.140625 1.0 0.765625 1.53125q0.640625 0.515625 1.78125 0.515625q1.15625 0 1.703125 -0.46875q0.5625 -0.46875 0.5625 -1.09375q0 -0.5625 -0.484375 -0.890625q-0.34375 -0.21875 -1.703125 -0.5625q-1.84375 -0.46875 -2.5625 -0.796875q-0.703125 -0.34375 -1.078125 -0.9375q-0.359375 -0.609375 -0.359375 -1.328125q0 -0.65625 0.296875 -1.21875q0.3125 -0.5625 0.828125 -0.9375q0.390625 -0.28125 1.0625 -0.484375q0.671875 -0.203125 1.4375 -0.203125q1.171875 0 2.046875 0.34375q0.875 0.328125 1.28125 0.90625q0.421875 0.5625 0.578125 1.515625l-1.625 0.21875q-0.109375 -0.75 -0.65625 -1.171875q-0.53125 -0.4375 -1.5 -0.4375q-1.15625 0 -1.640625 0.390625q-0.484375 0.375 -0.484375 0.875q0 0.328125 0.203125 0.59375q0.203125 0.265625 0.640625 0.4375q0.25 0.09375 1.46875 0.4375q1.765625 0.46875 2.46875 0.765625q0.703125 0.296875 1.09375 0.875q0.40625 0.578125 0.40625 1.4375q0 0.828125 -0.484375 1.578125q-0.484375 0.734375 -1.40625 1.140625q-0.921875 0.390625 -2.078125 0.390625q-1.921875 0 -2.9375 -0.796875q-1.0 -0.796875 -1.28125 -2.359375z" fill-rule="nonzero"></path><path fill="#d9ead3" d="m57.725563 542.8674l325.92126 0l0 52.22046l-325.92126 0z" fill-rule="nonzero"></path><path fill="#38761d" d="m134.9627 567.8976l0 -13.59375l1.796875 0l0 11.984375l6.703125 0l0 1.609375l-8.5 0zm10.250717 -11.6875l0 -1.90625l1.671875 0l0 1.90625l-1.671875 0zm0 11.6875l0 -9.859375l1.671875 0l0 9.859375l-1.671875 0zm3.4573212 -2.9375l1.65625 -0.265625q0.140625 1.0 0.765625 1.53125q0.640625 0.515625 1.78125 0.515625q1.15625 0 1.703125 -0.46875q0.5625 -0.46875 0.5625 -1.09375q0 -0.5625 -0.484375 -0.890625q-0.34375 -0.21875 -1.703125 -0.5625q-1.84375 -0.46875 -2.5625 -0.796875q-0.703125 -0.34375 -1.078125 -0.9375q-0.359375 -0.609375 -0.359375 -1.328125q0 -0.65625 0.296875 -1.21875q0.3125 -0.5625 0.828125 -0.9375q0.390625 -0.28125 1.0625 -0.484375q0.671875 -0.203125 1.4375 -0.203125q1.171875 0 2.046875 0.34375q0.875 0.328125 1.28125 0.90625q0.421875 0.5625 0.578125 1.515625l-1.625 0.21875q-0.109375 -0.75 -0.65625 -1.171875q-0.53125 -0.4375 -1.5 -0.4375q-1.15625 0 -1.640625 0.390625q-0.484375 0.375 -0.484375 0.875q0 0.328125 0.203125 0.59375q0.203125 0.265625 0.640625 0.4375q0.25 0.09375 1.46875 0.4375q1.765625 0.46875 2.46875 0.765625q0.703125 0.296875 1.09375 0.875q0.40625 0.578125 0.40625 1.4375q0 0.828125 -0.484375 1.578125q-0.484375 0.734375 -1.40625 1.140625q-0.921875 0.390625 -2.078125 0.390625q-1.921875 0 -2.9375 -0.796875q-1.0 -0.796875 -1.28125 -2.359375zm13.65625 1.4375l0.234375 1.484375q-0.703125 0.140625 -1.265625 0.140625q-0.90625 0 -1.40625 -0.28125q-0.5 -0.296875 -0.703125 -0.75q-0.203125 -0.46875 -0.203125 -1.984375l0 -5.65625l-1.234375 0l0 -1.3125l1.234375 0l0 -2.4375l1.65625 -1.0l0 3.4375l1.6875 0l0 1.3125l-1.6875 0l0 5.75q0 0.71875 0.078125 0.921875q0.09375 0.203125 0.296875 0.328125q0.203125 0.125 0.578125 0.125q0.265625 0 0.734375 -0.078125zm6.0853577 -3.421875q0 -2.734375 1.53125 -4.0625q1.265625 -1.09375 3.09375 -1.09375q2.03125 0 3.3125 1.34375q1.296875 1.328125 1.296875 3.671875q0 1.90625 -0.578125 3.0q-0.5625 1.078125 -1.65625 1.6875q-1.078125 0.59375 -2.375 0.59375q-2.0625 0 -3.34375 -1.328125q-1.28125 -1.328125 -1.28125 -3.8125zm1.71875 0q0 1.890625 0.828125 2.828125q0.828125 0.9375 2.078125 0.9375q1.25 0 2.0625 -0.9375q0.828125 -0.953125 0.828125 -2.890625q0 -1.828125 -0.828125 -2.765625q-0.828125 -0.9375 -2.0625 -0.9375q-1.25 0 -2.078125 0.9375q-0.828125 0.9375 -0.828125 2.828125zm9.281967 8.703125l0 -13.640625l1.53125 0l0 1.28125q0.53125 -0.75 1.203125 -1.125q0.6875 -0.375 1.640625 -0.375q1.265625 0 2.234375 0.65625q0.96875 0.640625 1.453125 1.828125q0.5 1.1875 0.5 2.59375q0 1.515625 -0.546875 2.734375q-0.546875 1.203125 -1.578125 1.84375q-1.03125 0.640625 -2.171875 0.640625q-0.84375 0 -1.515625 -0.34375q-0.65625 -0.359375 -1.078125 -0.890625l0 4.796875l-1.671875 0zm1.515625 -8.65625q0 1.90625 0.765625 2.8125q0.78125 0.90625 1.875 0.90625q1.109375 0 1.890625 -0.9375q0.796875 -0.9375 0.796875 -2.921875q0 -1.875 -0.78125 -2.8125q-0.765625 -0.9375 -1.84375 -0.9375q-1.0625 0 -1.890625 1.0q-0.8125 1.0 -0.8125 2.890625zm15.610092 1.703125l1.71875 0.21875q-0.40625 1.5 -1.515625 2.34375q-1.09375 0.828125 -2.8125 0.828125q-2.15625 0 -3.421875 -1.328125q-1.265625 -1.328125 -1.265625 -3.734375q0 -2.484375 1.265625 -3.859375q1.28125 -1.375 3.328125 -1.375q1.984375 0 3.234375 1.34375q1.25 1.34375 1.25 3.796875q0 0.140625 -0.015625 0.4375l-7.34375 0q0.09375 1.625 0.921875 2.484375q0.828125 0.859375 2.0625 0.859375q0.90625 0 1.546875 -0.46875q0.65625 -0.484375 1.046875 -1.546875zm-5.484375 -2.703125l5.5 0q-0.109375 -1.234375 -0.625 -1.859375q-0.796875 -0.96875 -2.078125 -0.96875q-1.140625 0 -1.9375 0.78125q-0.78125 0.765625 -0.859375 2.046875zm9.094467 5.875l0 -9.859375l1.5 0l0 1.5q0.578125 -1.046875 1.0625 -1.375q0.484375 -0.34375 1.078125 -0.34375q0.84375 0 1.71875 0.546875l-0.578125 1.546875q-0.609375 -0.359375 -1.234375 -0.359375q-0.546875 0 -0.984375 0.328125q-0.421875 0.328125 -0.609375 0.90625q-0.28125 0.890625 -0.28125 1.953125l0 5.15625l-1.671875 0zm12.665802 -1.21875q-0.9375 0.796875 -1.796875 1.125q-0.859375 0.3125 -1.84375 0.3125q-1.609375 0 -2.484375 -0.78125q-0.875 -0.796875 -0.875 -2.03125q0 -0.734375 0.328125 -1.328125q0.328125 -0.59375 0.859375 -0.953125q0.53125 -0.359375 1.203125 -0.546875q0.5 -0.140625 1.484375 -0.25q2.03125 -0.25 2.984375 -0.578125q0 -0.34375 0 -0.4375q0 -1.015625 -0.46875 -1.4375q-0.640625 -0.5625 -1.90625 -0.5625q-1.171875 0 -1.734375 0.40625q-0.5625 0.40625 -0.828125 1.46875l-1.640625 -0.234375q0.234375 -1.046875 0.734375 -1.6875q0.515625 -0.640625 1.46875 -0.984375q0.96875 -0.359375 2.25 -0.359375q1.265625 0 2.046875 0.296875q0.78125 0.296875 1.15625 0.75q0.375 0.453125 0.515625 1.140625q0.09375 0.421875 0.09375 1.53125l0 2.234375q0 2.328125 0.09375 2.953125q0.109375 0.609375 0.4375 1.171875l-1.75 0q-0.265625 -0.515625 -0.328125 -1.21875zm-0.140625 -3.71875q-0.90625 0.359375 -2.734375 0.625q-1.03125 0.140625 -1.453125 0.328125q-0.421875 0.1875 -0.65625 0.546875q-0.234375 0.359375 -0.234375 0.796875q0 0.671875 0.5 1.125q0.515625 0.4375 1.484375 0.4375q0.96875 0 1.71875 -0.421875q0.75 -0.4375 1.109375 -1.15625q0.265625 -0.578125 0.265625 -1.671875l0 -0.609375zm7.735092 3.4375l0.234375 1.484375q-0.703125 0.140625 -1.265625 0.140625q-0.90625 0 -1.40625 -0.28125q-0.5 -0.296875 -0.703125 -0.75q-0.203125 -0.46875 -0.203125 -1.984375l0 -5.65625l-1.234375 0l0 -1.3125l1.234375 0l0 -2.4375l1.65625 -1.0l0 3.4375l1.6875 0l0 1.3125l-1.6875 0l0 5.75q0 0.71875 0.078125 0.921875q0.09375 0.203125 0.296875 0.328125q0.203125 0.125 0.578125 0.125q0.265625 0 0.734375 -0.078125zm1.5426788 -10.1875l0 -1.90625l1.671875 0l0 1.90625l-1.671875 0zm0 11.6875l0 -9.859375l1.671875 0l0 9.859375l-1.671875 0zm3.5041962 -4.921875q0 -2.734375 1.53125 -4.0625q1.265625 -1.09375 3.09375 -1.09375q2.03125 0 3.3125 1.34375q1.296875 1.328125 1.296875 3.671875q0 1.90625 -0.578125 3.0q-0.5625 1.078125 -1.65625 1.6875q-1.078125 0.59375 -2.375 0.59375q-2.0625 0 -3.34375 -1.328125q-1.28125 -1.328125 -1.28125 -3.8125zm1.71875 0q0 1.890625 0.828125 2.828125q0.828125 0.9375 2.078125 0.9375q1.25 0 2.0625 -0.9375q0.828125 -0.953125 0.828125 -2.890625q0 -1.828125 -0.828125 -2.765625q-0.828125 -0.9375 -2.0625 -0.9375q-1.25 0 -2.078125 0.9375q-0.828125 0.9375 -0.828125 2.828125zm9.281967 4.921875l0 -9.859375l1.5 0l0 1.40625q1.09375 -1.625 3.140625 -1.625q0.890625 0 1.640625 0.328125q0.75 0.3125 1.109375 0.84375q0.375 0.515625 0.53125 1.21875q0.09375 0.46875 0.09375 1.625l0 6.0625l-1.671875 0l0 -6.0q0 -1.015625 -0.203125 -1.515625q-0.1875 -0.515625 -0.6875 -0.8125q-0.5 -0.296875 -1.171875 -0.296875q-1.0625 0 -1.84375 0.671875q-0.765625 0.671875 -0.765625 2.578125l0 5.375l-1.671875 0zm9.703842 -2.9375l1.65625 -0.265625q0.140625 1.0 0.765625 1.53125q0.640625 0.515625 1.78125 0.515625q1.15625 0 1.703125 -0.46875q0.5625 -0.46875 0.5625 -1.09375q0 -0.5625 -0.484375 -0.890625q-0.34375 -0.21875 -1.703125 -0.5625q-1.84375 -0.46875 -2.5625 -0.796875q-0.703125 -0.34375 -1.078125 -0.9375q-0.359375 -0.609375 -0.359375 -1.328125q0 -0.65625 0.296875 -1.21875q0.3125 -0.5625 0.828125 -0.9375q0.390625 -0.28125 1.0625 -0.484375q0.671875 -0.203125 1.4375 -0.203125q1.171875 0 2.046875 0.34375q0.875 0.328125 1.28125 0.90625q0.421875 0.5625 0.578125 1.515625l-1.625 0.21875q-0.109375 -0.75 -0.65625 -1.171875q-0.53125 -0.4375 -1.5 -0.4375q-1.15625 0 -1.640625 0.390625q-0.484375 0.375 -0.484375 0.875q0 0.328125 0.203125 0.59375q0.203125 0.265625 0.640625 0.4375q0.25 0.09375 1.46875 0.4375q1.765625 0.46875 2.46875 0.765625q0.703125 0.296875 1.09375 0.875q0.40625 0.578125 0.40625 1.4375q0 0.828125 -0.484375 1.578125q-0.484375 0.734375 -1.40625 1.140625q-0.921875 0.390625 -2.078125 0.390625q-1.921875 0 -2.9375 -0.796875q-1.0 -0.796875 -1.28125 -2.359375zm18.839539 1.4375l0.234375 1.484375q-0.703125 0.140625 -1.265625 0.140625q-0.90625 0 -1.40625 -0.28125q-0.5 -0.296875 -0.703125 -0.75q-0.203125 -0.46875 -0.203125 -1.984375l0 -5.65625l-1.234375 0l0 -1.3125l1.234375 0l0 -2.4375l1.65625 -1.0l0 3.4375l1.6875 0l0 1.3125l-1.6875 0l0 5.75q0 0.71875 0.078125 0.921875q0.09375 0.203125 0.296875 0.328125q0.203125 0.125 0.578125 0.125q0.265625 0 0.734375 -0.078125zm0.9020691 -3.421875q0 -2.734375 1.53125 -4.0625q1.265625 -1.09375 3.09375 -1.09375q2.03125 0 3.3125 1.34375q1.296875 1.328125 1.296875 3.671875q0 1.90625 -0.578125 3.0q-0.5625 1.078125 -1.65625 1.6875q-1.078125 0.59375 -2.375 0.59375q-2.0625 0 -3.34375 -1.328125q-1.28125 -1.328125 -1.28125 -3.8125zm1.71875 0q0 1.890625 0.828125 2.828125q0.828125 0.9375 2.078125 0.9375q1.25 0 2.0625 -0.9375q0.828125 -0.953125 0.828125 -2.890625q0 -1.828125 -0.828125 -2.765625q-0.828125 -0.9375 -2.0625 -0.9375q-1.25 0 -2.078125 0.9375q-0.828125 0.9375 -0.828125 2.828125zm14.449646 4.921875l0 -9.859375l1.5 0l0 1.5q0.578125 -1.046875 1.0625 -1.375q0.484375 -0.34375 1.078125 -0.34375q0.84375 0 1.71875 0.546875l-0.578125 1.546875q-0.609375 -0.359375 -1.234375 -0.359375q-0.546875 0 -0.984375 0.328125q-0.421875 0.328125 -0.609375 0.90625q-0.28125 0.890625 -0.28125 1.953125l0 5.15625l-1.671875 0zm12.681427 0l0 -1.453125q-1.140625 1.671875 -3.125 1.671875q-0.859375 0 -1.625 -0.328125q-0.75 -0.34375 -1.125 -0.84375q-0.359375 -0.5 -0.515625 -1.234375q-0.09375 -0.5 -0.09375 -1.5625l0 -6.109375l1.671875 0l0 5.46875q0 1.3125 0.09375 1.765625q0.15625 0.65625 0.671875 1.03125q0.515625 0.375 1.265625 0.375q0.75 0 1.40625 -0.375q0.65625 -0.390625 0.921875 -1.046875q0.28125 -0.671875 0.28125 -1.9375l0 -5.28125l1.671875 0l0 9.859375l-1.5 0zm3.922577 0l0 -9.859375l1.5 0l0 1.40625q1.09375 -1.625 3.140625 -1.625q0.890625 0 1.640625 0.328125q0.75 0.3125 1.109375 0.84375q0.375 0.515625 0.53125 1.21875q0.09375 0.46875 0.09375 1.625l0 6.0625l-1.671875 0l0 -6.0q0 -1.015625 -0.203125 -1.515625q-0.1875 -0.515625 -0.6875 -0.8125q-0.5 -0.296875 -1.171875 -0.296875q-1.0625 0 -1.84375 0.671875q-0.765625 0.671875 -0.765625 2.578125l0 5.375l-1.671875 0z" fill-rule="nonzero"></path><path fill="#38761d" d="m148.01247 584.7776l0 -9.3125l6.71875 0l0 1.109375l-5.484375 0l0 2.84375l5.140625 0l0 1.09375l-5.140625 0l0 3.171875l5.703125 0l0 1.09375l-6.9375 0zm7.9522552 0l2.46875 -3.5l-2.28125 -3.234375l1.421875 0l1.046875 1.578125q0.28125 0.453125 0.46875 0.75q0.265625 -0.421875 0.5 -0.734375l1.140625 -1.59375l1.375 0l-2.34375 3.171875l2.515625 3.5625l-1.40625 0l-1.375 -2.09375l-0.375 -0.5625l-1.765625 2.65625l-1.390625 0zm7.7421875 -5.4375l0 -1.296875l1.296875 0l0 1.296875l-1.296875 0zm0 5.4375l0 -1.296875l1.296875 0l0 1.296875l-1.296875 0zm7.9841003 -7.75l0 1.328125l-1.21875 0l0 -1.046875q0 -0.84375 0.203125 -1.234375q0.265625 -0.5 0.84375 -0.765625l0.28125 0.453125q-0.359375 0.140625 -0.53125 0.4375q-0.15625 0.28125 -0.171875 0.828125l0.59375 0zm1.96875 0l0 1.328125l-1.21875 0l0 -1.046875q0 -0.84375 0.203125 -1.234375q0.265625 -0.5 0.84375 -0.765625l0.28125 0.453125q-0.359375 0.140625 -0.53125 0.4375q-0.15625 0.28125 -0.171875 0.828125l0.59375 0zm1.3602448 8.3125l1.125 0.15625q0.0625 0.515625 0.375 0.75q0.4375 0.328125 1.171875 0.328125q0.78125 0 1.21875 -0.328125q0.4375 -0.3125 0.578125 -0.890625q0.09375 -0.34375 0.09375 -1.453125q-0.75 0.875 -1.875 0.875q-1.390625 0 -2.15625 -1.0q-0.75 -1.0 -0.75 -2.40625q0 -0.96875 0.34375 -1.78125q0.359375 -0.8125 1.015625 -1.25q0.65625 -0.453125 1.5625 -0.453125q1.1875 0 1.96875 0.96875l0 -0.8125l1.046875 0l0 5.8125q0 1.578125 -0.328125 2.234375q-0.3125 0.65625 -1.015625 1.03125q-0.6875 0.390625 -1.703125 0.390625q-1.203125 0 -1.953125 -0.546875q-0.734375 -0.53125 -0.71875 -1.625zm0.953125 -4.046875q0 1.3125 0.515625 1.921875q0.53125 0.609375 1.328125 0.609375q0.796875 0 1.328125 -0.59375q0.53125 -0.609375 0.53125 -1.90625q0 -1.234375 -0.546875 -1.859375q-0.546875 -0.640625 -1.328125 -0.640625q-0.765625 0 -1.296875 0.625q-0.53125 0.625 -0.53125 1.84375zm6.6624756 3.484375l0 -6.734375l1.03125 0l0 1.015625q0.390625 -0.71875 0.71875 -0.9375q0.34375 -0.234375 0.734375 -0.234375q0.578125 0 1.171875 0.359375l-0.390625 1.0625q-0.421875 -0.25 -0.828125 -0.25q-0.375 0 -0.6875 0.234375q-0.296875 0.21875 -0.421875 0.625q-0.1875 0.609375 -0.1875 1.328125l0 3.53125l-1.140625 0zm8.844635 -0.828125q-0.625 0.53125 -1.21875 0.765625q-0.578125 0.21875 -1.25 0.21875q-1.125 0 -1.71875 -0.546875q-0.59375 -0.546875 -0.59375 -1.390625q0 -0.484375 0.21875 -0.890625q0.234375 -0.421875 0.59375 -0.671875q0.375 -0.25 0.828125 -0.375q0.328125 -0.078125 1.015625 -0.171875q1.375 -0.15625 2.03125 -0.390625q0.015625 -0.234375 0.015625 -0.296875q0 -0.703125 -0.328125 -0.984375q-0.4375 -0.390625 -1.296875 -0.390625q-0.8125 0 -1.203125 0.28125q-0.375 0.28125 -0.5625 1.0l-1.109375 -0.140625q0.140625 -0.71875 0.484375 -1.15625q0.359375 -0.453125 1.015625 -0.6875q0.671875 -0.234375 1.53125 -0.234375q0.875 0 1.40625 0.203125q0.546875 0.203125 0.796875 0.515625q0.25 0.296875 0.359375 0.765625q0.046875 0.296875 0.046875 1.0625l0 1.515625q0 1.59375 0.078125 2.015625q0.078125 0.421875 0.28125 0.8125l-1.1875 0q-0.171875 -0.359375 -0.234375 -0.828125zm-0.09375 -2.5625q-0.625 0.265625 -1.859375 0.4375q-0.703125 0.109375 -1.0 0.234375q-0.296875 0.125 -0.453125 0.375q-0.15625 0.234375 -0.15625 0.53125q0 0.453125 0.34375 0.765625q0.34375 0.296875 1.015625 0.296875q0.65625 0 1.171875 -0.28125q0.515625 -0.296875 0.765625 -0.796875q0.171875 -0.375 0.171875 -1.140625l0 -0.421875zm3.1156006 5.96875l0 -9.3125l1.03125 0l0 0.875q0.375 -0.515625 0.828125 -0.765625q0.46875 -0.265625 1.140625 -0.265625q0.859375 0 1.515625 0.453125q0.65625 0.4375 0.984375 1.25q0.34375 0.796875 0.34375 1.765625q0 1.03125 -0.375 1.859375q-0.359375 0.828125 -1.078125 1.28125q-0.703125 0.4375 -1.484375 0.4375q-0.5625 0 -1.015625 -0.234375q-0.453125 -0.25 -0.75 -0.625l0 3.28125l-1.140625 0zm1.03125 -5.90625q0 1.296875 0.53125 1.921875q0.53125 0.625 1.265625 0.625q0.765625 0 1.3125 -0.640625q0.546875 -0.65625 0.546875 -2.0q0 -1.296875 -0.53125 -1.9375q-0.53125 -0.640625 -1.265625 -0.640625q-0.734375 0 -1.296875 0.6875q-0.5625 0.671875 -0.5625 1.984375zm6.3812256 3.328125l0 -9.3125l1.140625 0l0 3.34375q0.796875 -0.921875 2.015625 -0.921875q0.75 0 1.296875 0.296875q0.5625 0.296875 0.796875 0.8125q0.234375 0.515625 0.234375 1.515625l0 4.265625l-1.140625 0l0 -4.265625q0 -0.859375 -0.375 -1.25q-0.359375 -0.390625 -1.046875 -0.390625q-0.5 0 -0.953125 0.265625q-0.453125 0.25 -0.640625 0.703125q-0.1875 0.453125 -0.1875 1.25l0 3.6875l-1.140625 0zm7.0999756 -8.078125l0 -1.328125l1.234375 0l0 1.046875q0 0.859375 -0.203125 1.234375q-0.265625 0.515625 -0.84375 0.765625l-0.28125 -0.453125q0.34375 -0.125 0.5 -0.421875q0.171875 -0.3125 0.203125 -0.84375l-0.609375 0zm1.96875 0l0 -1.328125l1.234375 0l0 1.046875q0 0.859375 -0.203125 1.234375q-0.265625 0.515625 -0.84375 0.765625l-0.28125 -0.453125q0.34375 -0.125 0.5 -0.421875q0.171875 -0.3125 0.1875 -0.84375l-0.59375 0zm3.0789795 8.078125l0 -1.296875l1.296875 0l0 1.296875q0 0.71875 -0.25 1.15625q-0.25 0.4375 -0.8125 0.6875l-0.3125 -0.484375q0.359375 -0.171875 0.53125 -0.484375q0.171875 -0.296875 0.1875 -0.875l-0.640625 0zm7.9997253 -7.75l0 1.328125l-1.21875 0l0 -1.046875q0 -0.84375 0.203125 -1.234375q0.265625 -0.5 0.84375 -0.765625l0.28125 0.453125q-0.359375 0.140625 -0.53125 0.4375q-0.15625 0.28125 -0.171875 0.828125l0.59375 0zm1.96875 0l0 1.328125l-1.21875 0l0 -1.046875q0 -0.84375 0.203125 -1.234375q0.265625 -0.5 0.84375 -0.765625l0.28125 0.453125q-0.359375 0.140625 -0.53125 0.4375q-0.15625 0.28125 -0.171875 0.828125l0.59375 0zm5.95401 7.75l0 -0.84375q-0.640625 1.0 -1.890625 1.0q-0.796875 0 -1.484375 -0.4375q-0.671875 -0.453125 -1.046875 -1.25q-0.375 -0.796875 -0.375 -1.828125q0 -1.015625 0.34375 -1.828125q0.34375 -0.828125 1.015625 -1.265625q0.671875 -0.4375 1.5 -0.4375q0.609375 0 1.078125 0.265625q0.484375 0.25 0.78125 0.65625l0 -3.34375l1.140625 0l0 9.3125l-1.0625 0zm-3.609375 -3.359375q0 1.296875 0.53125 1.9375q0.546875 0.640625 1.296875 0.640625q0.75 0 1.265625 -0.609375q0.53125 -0.625 0.53125 -1.875q0 -1.390625 -0.53125 -2.03125q-0.53125 -0.65625 -1.3125 -0.65625q-0.765625 0 -1.28125 0.625q-0.5 0.625 -0.5 1.96875zm11.256226 1.1875l1.1875 0.140625q-0.28125 1.046875 -1.046875 1.625q-0.75 0.5625 -1.921875 0.5625q-1.484375 0 -2.359375 -0.90625q-0.859375 -0.921875 -0.859375 -2.5625q0 -1.703125 0.875 -2.640625q0.890625 -0.9375 2.28125 -0.9375q1.359375 0 2.203125 0.921875q0.859375 0.921875 0.859375 2.578125q0 0.109375 0 0.3125l-5.03125 0q0.0625 1.109375 0.625 1.703125q0.5625 0.59375 1.40625 0.59375q0.640625 0 1.078125 -0.328125q0.453125 -0.34375 0.703125 -1.0625zm-3.75 -1.84375l3.765625 0q-0.078125 -0.859375 -0.4375 -1.28125q-0.546875 -0.65625 -1.40625 -0.65625q-0.796875 0 -1.328125 0.53125q-0.53125 0.515625 -0.59375 1.40625zm6.5531006 6.59375l0 -9.3125l1.03125 0l0 0.875q0.375 -0.515625 0.828125 -0.765625q0.46875 -0.265625 1.140625 -0.265625q0.859375 0 1.515625 0.453125q0.65625 0.4375 0.984375 1.25q0.34375 0.796875 0.34375 1.765625q0 1.03125 -0.375 1.859375q-0.359375 0.828125 -1.078125 1.28125q-0.703125 0.4375 -1.484375 0.4375q-0.5625 0 -1.015625 -0.234375q-0.453125 -0.25 -0.75 -0.625l0 3.28125l-1.140625 0zm1.03125 -5.90625q0 1.296875 0.53125 1.921875q0.53125 0.625 1.265625 0.625q0.765625 0 1.3125 -0.640625q0.546875 -0.65625 0.546875 -2.0q0 -1.296875 -0.53125 -1.9375q-0.53125 -0.640625 -1.265625 -0.640625q-0.734375 0 -1.296875 0.6875q-0.5625 0.671875 -0.5625 1.984375zm6.3656006 3.328125l0 -6.734375l1.03125 0l0 1.015625q0.390625 -0.71875 0.71875 -0.9375q0.34375 -0.234375 0.734375 -0.234375q0.578125 0 1.171875 0.359375l-0.390625 1.0625q-0.421875 -0.25 -0.828125 -0.25q-0.375 0 -0.6875 0.234375q-0.296875 0.21875 -0.421875 0.625q-0.1875 0.609375 -0.1875 1.328125l0 3.53125l-1.140625 0zm9.063339 -2.171875l1.1875 0.140625q-0.28125 1.046875 -1.046875 1.625q-0.75 0.5625 -1.9218597 0.5625q-1.484375 0 -2.359375 -0.90625q-0.859375 -0.921875 -0.859375 -2.5625q0 -1.703125 0.875 -2.640625q0.890625 -0.9375 2.28125 -0.9375q1.3593597 0 2.2031097 0.921875q0.859375 0.921875 0.859375 2.578125q0 0.109375 0 0.3125l-5.0312347 0q0.0625 1.109375 0.625 1.703125q0.5625 0.59375 1.40625 0.59375q0.640625 0 1.0781097 -0.328125q0.453125 -0.34375 0.703125 -1.0625zm-3.7499847 -1.84375l3.7656097 0q-0.078125 -0.859375 -0.4375 -1.28125q-0.54685974 -0.65625 -1.4062347 -0.65625q-0.796875 0 -1.328125 0.53125q-0.53125 0.515625 -0.59375 1.40625zm6.0999603 2.0l1.125 -0.171875q0.09375 0.671875 0.53125 1.046875q0.4375 0.359375 1.21875 0.359375q0.78125 0 1.15625 -0.3125q0.390625 -0.328125 0.390625 -0.765625q0 -0.390625 -0.34375 -0.609375q-0.234375 -0.15625 -1.171875 -0.390625q-1.25 -0.3125 -1.734375 -0.546875q-0.484375 -0.234375 -0.734375 -0.640625q-0.25 -0.40625 -0.25 -0.90625q0 -0.453125 0.203125 -0.828125q0.203125 -0.390625 0.5625 -0.640625q0.265625 -0.203125 0.71875 -0.328125q0.46875 -0.140625 1.0 -0.140625q0.78125 0 1.375 0.234375q0.609375 0.21875 0.890625 0.609375q0.296875 0.390625 0.40625 1.046875l-1.125 0.15625q-0.078125 -0.53125 -0.4375 -0.8125q-0.359375 -0.296875 -1.03125 -0.296875q-0.78125 0 -1.125 0.265625q-0.34375 0.25 -0.34375 0.609375q0 0.21875 0.140625 0.390625q0.140625 0.1875 0.4375 0.3125q0.171875 0.0625 1.015625 0.28125q1.21875 0.328125 1.6875 0.53125q0.484375 0.203125 0.75 0.609375q0.28125 0.390625 0.28125 0.96875q0 0.578125 -0.34375 1.078125q-0.328125 0.5 -0.953125 0.78125q-0.625 0.28125 -1.421875 0.28125q-1.3125 0 -2.0 -0.546875q-0.6875 -0.546875 -0.875 -1.625zm6.6953125 -1.359375q0 -1.875 1.03125 -2.765625q0.875 -0.75 2.125 -0.75q1.390625 0 2.265625 0.90625q0.890625 0.90625 0.890625 2.515625q0 1.296875 -0.390625 2.046875q-0.390625 0.75 -1.140625 1.171875q-0.75 0.40625 -1.625 0.40625q-1.421875 0 -2.296875 -0.90625q-0.859375 -0.90625 -0.859375 -2.625zm1.171875 0q0 1.296875 0.5625 1.953125q0.5625 0.640625 1.421875 0.640625q0.84375 0 1.40625 -0.640625q0.578125 -0.65625 0.578125 -1.984375q0 -1.25 -0.578125 -1.890625q-0.5625 -0.65625 -1.40625 -0.65625q-0.859375 0 -1.421875 0.640625q-0.5625 0.640625 -0.5625 1.9375zm6.6312256 3.375l0 -9.3125l1.140625 0l0 9.3125l-1.140625 0zm4.86734 0l-2.5625 -6.734375l1.203125 0l1.4375 4.03125q0.234375 0.65625 0.4375 1.359375q0.15625 -0.53125 0.421875 -1.28125l1.5 -4.109375l1.171875 0l-2.546875 6.734375l-1.0625 0zm9.3984375 -2.171875l1.1875 0.140625q-0.28125 1.046875 -1.046875 1.625q-0.75 0.5625 -1.921875 0.5625q-1.484375 0 -2.359375 -0.90625q-0.859375 -0.921875 -0.859375 -2.5625q0 -1.703125 0.875 -2.640625q0.890625 -0.9375 2.28125 -0.9375q1.359375 0 2.203125 0.921875q0.859375 0.921875 0.859375 2.578125q0 0.109375 0 0.3125l-5.03125 0q0.0625 1.109375 0.625 1.703125q0.5625 0.59375 1.40625 0.59375q0.640625 0 1.078125 -0.328125q0.453125 -0.34375 0.703125 -1.0625zm-3.75 -1.84375l3.765625 0q-0.078125 -0.859375 -0.4375 -1.28125q-0.546875 -0.65625 -1.40625 -0.65625q-0.796875 0 -1.328125 0.53125q-0.53125 0.515625 -0.59375 1.40625zm6.2406006 -4.0625l0 -1.328125l1.234375 0l0 1.046875q0 0.859375 -0.203125 1.234375q-0.265625 0.515625 -0.84375 0.765625l-0.28125 -0.453125q0.34375 -0.125 0.5 -0.421875q0.171875 -0.3125 0.203125 -0.84375l-0.609375 0zm1.96875 0l0 -1.328125l1.234375 0l0 1.046875q0 0.859375 -0.203125 1.234375q-0.265625 0.515625 -0.84375 0.765625l-0.28125 -0.453125q0.34375 -0.125 0.5 -0.421875q0.171875 -0.3125 0.1875 -0.84375l-0.59375 0z" fill-rule="nonzero"></path><path fill="#d9ead3" d="m57.725563 613.6924l325.92126 0l0 52.22046l-325.92126 0z" fill-rule="nonzero"></path><path fill="#38761d" d="m122.082565 638.72266l0 -13.59375l4.6875 0q1.578125 0 2.421875 0.1875q1.15625 0.265625 1.984375 0.96875q1.078125 0.921875 1.609375 2.34375q0.53125 1.40625 0.53125 3.21875q0 1.546875 -0.359375 2.75q-0.359375 1.1875 -0.921875 1.984375q-0.5625 0.78125 -1.234375 1.234375q-0.671875 0.4375 -1.625 0.671875q-0.953125 0.234375 -2.1875 0.234375l-4.90625 0zm1.796875 -1.609375l2.90625 0q1.34375 0 2.109375 -0.25q0.765625 -0.25 1.21875 -0.703125q0.640625 -0.640625 1.0 -1.71875q0.359375 -1.078125 0.359375 -2.625q0 -2.125 -0.703125 -3.265625q-0.703125 -1.15625 -1.703125 -1.546875q-0.71875 -0.28125 -2.328125 -0.28125l-2.859375 0l0 10.390625zm18.207321 -1.5625l1.71875 0.21875q-0.40625 1.5 -1.515625 2.34375q-1.09375 0.828125 -2.8125 0.828125q-2.15625 0 -3.421875 -1.328125q-1.265625 -1.328125 -1.265625 -3.734375q0 -2.484375 1.265625 -3.859375q1.28125 -1.375 3.328125 -1.375q1.984375 0 3.234375 1.34375q1.25 1.34375 1.25 3.796875q0 0.140625 -0.015625 0.4375l-7.34375 0q0.09375 1.625 0.921875 2.484375q0.828125 0.859375 2.0625 0.859375q0.90625 0 1.546875 -0.46875q0.65625 -0.484375 1.046875 -1.546875zm-5.484375 -2.703125l5.5 0q-0.109375 -1.234375 -0.625 -1.859375q-0.796875 -0.96875 -2.078125 -0.96875q-1.140625 0 -1.9375 0.78125q-0.78125 0.765625 -0.859375 2.046875zm12.766342 4.375l0.234375 1.484375q-0.703125 0.140625 -1.265625 0.140625q-0.90625 0 -1.40625 -0.28125q-0.5 -0.296875 -0.703125 -0.75q-0.203125 -0.46875 -0.203125 -1.984375l0 -5.65625l-1.234375 0l0 -1.3125l1.234375 0l0 -2.4375l1.65625 -1.0l0 3.4375l1.6875 0l0 1.3125l-1.6875 0l0 5.75q0 0.71875 0.078125 0.921875q0.09375 0.203125 0.296875 0.328125q0.203125 0.125 0.578125 0.125q0.265625 0 0.734375 -0.078125zm8.277054 -1.671875l1.71875 0.21875q-0.40625 1.5 -1.515625 2.34375q-1.09375 0.828125 -2.8125 0.828125q-2.15625 0 -3.421875 -1.328125q-1.265625 -1.328125 -1.265625 -3.734375q0 -2.484375 1.265625 -3.859375q1.28125 -1.375 3.328125 -1.375q1.984375 0 3.234375 1.34375q1.25 1.34375 1.25 3.796875q0 0.140625 -0.015625 0.4375l-7.34375 0q0.09375 1.625 0.921875 2.484375q0.828125 0.859375 2.0625 0.859375q0.90625 0 1.546875 -0.46875q0.65625 -0.484375 1.046875 -1.546875zm-5.484375 -2.703125l5.5 0q-0.109375 -1.234375 -0.625 -1.859375q-0.796875 -0.96875 -2.078125 -0.96875q-1.140625 0 -1.9375 0.78125q-0.78125 0.765625 -0.859375 2.046875zm9.094467 5.875l0 -9.859375l1.5 0l0 1.5q0.578125 -1.046875 1.0625 -1.375q0.484375 -0.34375 1.078125 -0.34375q0.84375 0 1.71875 0.546875l-0.578125 1.546875q-0.609375 -0.359375 -1.234375 -0.359375q-0.546875 0 -0.984375 0.328125q-0.421875 0.328125 -0.609375 0.90625q-0.28125 0.890625 -0.28125 1.953125l0 5.15625l-1.671875 0zm6.228302 0l0 -9.859375l1.5 0l0 1.390625q0.453125 -0.71875 1.21875 -1.15625q0.78125 -0.453125 1.765625 -0.453125q1.09375 0 1.796875 0.453125q0.703125 0.453125 0.984375 1.28125q1.171875 -1.734375 3.046875 -1.734375q1.46875 0 2.25 0.8125q0.796875 0.8125 0.796875 2.5l0 6.765625l-1.671875 0l0 -6.203125q0 -1.0 -0.15625 -1.4375q-0.15625 -0.453125 -0.59375 -0.71875q-0.421875 -0.265625 -1.0 -0.265625q-1.03125 0 -1.71875 0.6875q-0.6875 0.6875 -0.6875 2.21875l0 5.71875l-1.671875 0l0 -6.40625q0 -1.109375 -0.40625 -1.65625q-0.40625 -0.5625 -1.34375 -0.5625q-0.703125 0 -1.3125 0.375q-0.59375 0.359375 -0.859375 1.078125q-0.265625 0.71875 -0.265625 2.0625l0 5.109375l-1.671875 0zm15.556427 -11.6875l0 -1.90625l1.671875 0l0 1.90625l-1.671875 0zm0 11.6875l0 -9.859375l1.671875 0l0 9.859375l-1.671875 0zm4.1292114 0l0 -9.859375l1.5 0l0 1.40625q1.09375 -1.625 3.140625 -1.625q0.890625 0 1.640625 0.328125q0.75 0.3125 1.109375 0.84375q0.375 0.515625 0.53125 1.21875q0.09375 0.46875 0.09375 1.625l0 6.0625l-1.671875 0l0 -6.0q0 -1.015625 -0.203125 -1.515625q-0.1875 -0.515625 -0.6875 -0.8125q-0.5 -0.296875 -1.171875 -0.296875q-1.0625 0 -1.84375 0.671875q-0.765625 0.671875 -0.765625 2.578125l0 5.375l-1.671875 0zm17.125702 -3.171875l1.71875 0.21875q-0.40625 1.5 -1.515625 2.34375q-1.09375 0.828125 -2.8125 0.828125q-2.15625 0 -3.421875 -1.328125q-1.265625 -1.328125 -1.265625 -3.734375q0 -2.484375 1.265625 -3.859375q1.28125 -1.375 3.328125 -1.375q1.984375 0 3.234375 1.34375q1.25 1.34375 1.25 3.796875q0 0.140625 -0.015625 0.4375l-7.34375 0q0.09375 1.625 0.921875 2.484375q0.828125 0.859375 2.0625 0.859375q0.90625 0 1.546875 -0.46875q0.65625 -0.484375 1.046875 -1.546875zm-5.484375 -2.703125l5.5 0q-0.109375 -1.234375 -0.625 -1.859375q-0.796875 -0.96875 -2.078125 -0.96875q-1.140625 0 -1.9375 0.78125q-0.78125 0.765625 -0.859375 2.046875zm17.949646 4.375l0.234375 1.484375q-0.703125 0.140625 -1.265625 0.140625q-0.90625 0 -1.40625 -0.28125q-0.5 -0.296875 -0.703125 -0.75q-0.203125 -0.46875 -0.203125 -1.984375l0 -5.65625l-1.234375 0l0 -1.3125l1.234375 0l0 -2.4375l1.65625 -1.0l0 3.4375l1.6875 0l0 1.3125l-1.6875 0l0 5.75q0 0.71875 0.078125 0.921875q0.09375 0.203125 0.296875 0.328125q0.203125 0.125 0.578125 0.125q0.265625 0 0.734375 -0.078125zm0.9020691 -3.421875q0 -2.734375 1.53125 -4.0625q1.265625 -1.09375 3.09375 -1.09375q2.03125 0 3.3125 1.34375q1.296875 1.328125 1.296875 3.671875q0 1.90625 -0.578125 3.0q-0.5625 1.078125 -1.65625 1.6875q-1.078125 0.59375 -2.375 0.59375q-2.0625 0 -3.34375 -1.328125q-1.28125 -1.328125 -1.28125 -3.8125zm1.71875 0q0 1.890625 0.828125 2.828125q0.828125 0.9375 2.078125 0.9375q1.25 0 2.0625 -0.9375q0.828125 -0.953125 0.828125 -2.890625q0 -1.828125 -0.828125 -2.765625q-0.828125 -0.9375 -2.0625 -0.9375q-1.25 0 -2.078125 0.9375q-0.828125 0.9375 -0.828125 2.828125zm8.656952 0q0 -2.734375 1.53125 -4.0625q1.265625 -1.09375 3.09375 -1.09375q2.03125 0 3.3125 1.34375q1.296875 1.328125 1.296875 3.671875q0 1.90625 -0.578125 3.0q-0.5625 1.078125 -1.65625 1.6875q-1.078125 0.59375 -2.375 0.59375q-2.0625 0 -3.34375 -1.328125q-1.28125 -1.328125 -1.28125 -3.8125zm1.71875 0q0 1.890625 0.828125 2.828125q0.828125 0.9375 2.078125 0.9375q1.25 0 2.0625 -0.9375q0.828125 -0.953125 0.828125 -2.890625q0 -1.828125 -0.828125 -2.765625q-0.828125 -0.9375 -2.0625 -0.9375q-1.25 0 -2.078125 0.9375q-0.828125 0.9375 -0.828125 2.828125zm9.250732 4.921875l0 -13.59375l1.671875 0l0 13.59375l-1.671875 0zm13.015625 -1.5l0.234375 1.484375q-0.703125 0.140625 -1.265625 0.140625q-0.90625 0 -1.40625 -0.28125q-0.5 -0.296875 -0.703125 -0.75q-0.203125 -0.46875 -0.203125 -1.984375l0 -5.65625l-1.234375 0l0 -1.3125l1.234375 0l0 -2.4375l1.65625 -1.0l0 3.4375l1.6875 0l0 1.3125l-1.6875 0l0 5.75q0 0.71875 0.078125 0.921875q0.09375 0.203125 0.296875 0.328125q0.203125 0.125 0.578125 0.125q0.265625 0 0.734375 -0.078125zm0.9020386 -3.421875q0 -2.734375 1.53125 -4.0625q1.265625 -1.09375 3.0937347 -1.09375q2.03125 0 3.3125 1.34375q1.296875 1.328125 1.296875 3.671875q0 1.90625 -0.578125 3.0q-0.5625 1.078125 -1.65625 1.6875q-1.078125 0.59375 -2.375 0.59375q-2.0624847 0 -3.3437347 -1.328125q-1.28125 -1.328125 -1.28125 -3.8125zm1.71875 0q0 1.890625 0.828125 2.828125q0.82810974 0.9375 2.0781097 0.9375q1.25 0 2.0625 -0.9375q0.828125 -0.953125 0.828125 -2.890625q0 -1.828125 -0.828125 -2.765625q-0.828125 -0.9375 -2.0625 -0.9375q-1.25 0 -2.0781097 0.9375q-0.828125 0.9375 -0.828125 2.828125zm14.449631 4.921875l0 -9.859375l1.5 0l0 1.5q0.578125 -1.046875 1.0625 -1.375q0.484375 -0.34375 1.078125 -0.34375q0.84375 0 1.71875 0.546875l-0.578125 1.546875q-0.609375 -0.359375 -1.234375 -0.359375q-0.546875 0 -0.984375 0.328125q-0.421875 0.328125 -0.609375 0.90625q-0.28125 0.890625 -0.28125 1.953125l0 5.15625l-1.671875 0zm12.681427 0l0 -1.453125q-1.140625 1.671875 -3.125 1.671875q-0.859375 0 -1.625 -0.328125q-0.75 -0.34375 -1.125 -0.84375q-0.359375 -0.5 -0.515625 -1.234375q-0.09375 -0.5 -0.09375 -1.5625l0 -6.109375l1.671875 0l0 5.46875q0 1.3125 0.09375 1.765625q0.15625 0.65625 0.671875 1.03125q0.515625 0.375 1.265625 0.375q0.75 0 1.40625 -0.375q0.65625 -0.390625 0.921875 -1.046875q0.28125 -0.671875 0.28125 -1.9375l0 -5.28125l1.671875 0l0 9.859375l-1.5 0zm3.9226074 0l0 -9.859375l1.5 0l0 1.40625q1.09375 -1.625 3.140625 -1.625q0.890625 0 1.640625 0.328125q0.75 0.3125 1.109375 0.84375q0.375 0.515625 0.53125 1.21875q0.09375 0.46875 0.09375 1.625l0 6.0625l-1.671875 0l0 -6.0q0 -1.015625 -0.203125 -1.515625q-0.1875 -0.515625 -0.6875 -0.8125q-0.5 -0.296875 -1.171875 -0.296875q-1.0625 0 -1.84375 0.671875q-0.765625 0.671875 -0.765625 2.578125l0 5.375l-1.671875 0zm14.934021 -4.921875q0 -2.734375 1.53125 -4.0625q1.265625 -1.09375 3.09375 -1.09375q2.03125 0 3.3125 1.34375q1.296875 1.328125 1.296875 3.671875q0 1.90625 -0.578125 3.0q-0.5625 1.078125 -1.65625 1.6875q-1.078125 0.59375 -2.375 0.59375q-2.0625 0 -3.34375 -1.328125q-1.28125 -1.328125 -1.28125 -3.8125zm1.71875 0q0 1.890625 0.828125 2.828125q0.828125 0.9375 2.078125 0.9375q1.25 0 2.0625 -0.9375q0.828125 -0.953125 0.828125 -2.890625q0 -1.828125 -0.828125 -2.765625q-0.828125 -0.9375 -2.0625 -0.9375q-1.25 0 -2.078125 0.9375q-0.828125 0.9375 -0.828125 2.828125zm9.281952 8.703125l0 -13.640625l1.53125 0l0 1.28125q0.53125 -0.75 1.203125 -1.125q0.6875 -0.375 1.640625 -0.375q1.265625 0 2.234375 0.65625q0.96875 0.640625 1.453125 1.828125q0.5 1.1875 0.5 2.59375q0 1.515625 -0.546875 2.734375q-0.546875 1.203125 -1.578125 1.84375q-1.03125 0.640625 -2.171875 0.640625q-0.84375 0 -1.515625 -0.34375q-0.65625 -0.359375 -1.078125 -0.890625l0 4.796875l-1.671875 0zm1.515625 -8.65625q0 1.90625 0.765625 2.8125q0.78125 0.90625 1.875 0.90625q1.109375 0 1.890625 -0.9375q0.796875 -0.9375 0.796875 -2.921875q0 -1.875 -0.78125 -2.8125q-0.765625 -0.9375 -1.84375 -0.9375q-1.0625 0 -1.890625 1.0q-0.8125 1.0 -0.8125 2.890625z" fill-rule="nonzero"></path><path fill="#38761d" d="m110.592155 655.60266l0 -9.3125l6.71875 0l0 1.109375l-5.484375 0l0 2.84375l5.140625 0l0 1.09375l-5.140625 0l0 3.171875l5.703125 0l0 1.09375l-6.9375 0zm7.9522552 0l2.46875 -3.5l-2.28125 -3.234375l1.421875 0l1.046875 1.578125q0.28125 0.453125 0.46875 0.75q0.265625 -0.421875 0.5 -0.734375l1.140625 -1.59375l1.375 0l-2.34375 3.171875l2.515625 3.5625l-1.40625 0l-1.375 -2.09375l-0.375 -0.5625l-1.765625 2.65625l-1.390625 0zm7.7421875 -5.4375l0 -1.296875l1.296875 0l0 1.296875l-1.296875 0zm0 5.4375l0 -1.296875l1.296875 0l0 1.296875l-1.296875 0zm6.640358 -2.015625l1.125 -0.171875q0.09375 0.671875 0.53125 1.046875q0.4375 0.359375 1.21875 0.359375q0.78125 0 1.15625 -0.3125q0.390625 -0.328125 0.390625 -0.765625q0 -0.390625 -0.34375 -0.609375q-0.234375 -0.15625 -1.171875 -0.390625q-1.25 -0.3125 -1.734375 -0.546875q-0.484375 -0.234375 -0.734375 -0.640625q-0.25 -0.40625 -0.25 -0.90625q0 -0.453125 0.203125 -0.828125q0.203125 -0.390625 0.5625 -0.640625q0.265625 -0.203125 0.71875 -0.328125q0.46875 -0.140625 1.0 -0.140625q0.78125 0 1.375 0.234375q0.609375 0.21875 0.890625 0.609375q0.296875 0.390625 0.40625 1.046875l-1.125 0.15625q-0.078125 -0.53125 -0.4375 -0.8125q-0.359375 -0.296875 -1.03125 -0.296875q-0.78125 0 -1.125 0.265625q-0.34375 0.25 -0.34375 0.609375q0 0.21875 0.140625 0.390625q0.140625 0.1875 0.4375 0.3125q0.171875 0.0625 1.015625 0.28125q1.21875 0.328125 1.6875 0.53125q0.484375 0.203125 0.75 0.609375q0.28125 0.390625 0.28125 0.96875q0 0.578125 -0.34375 1.078125q-0.328125 0.5 -0.953125 0.78125q-0.625 0.28125 -1.421875 0.28125q-1.3125 0 -2.0 -0.546875q-0.6875 -0.546875 -0.875 -1.625zm7.1015625 2.015625l0 -6.734375l1.03125 0l0 1.015625q0.390625 -0.71875 0.71875 -0.9375q0.34375 -0.234375 0.734375 -0.234375q0.578125 0 1.171875 0.359375l-0.390625 1.0625q-0.421875 -0.25 -0.828125 -0.25q-0.375 0 -0.6875 0.234375q-0.296875 0.21875 -0.421875 0.625q-0.1875 0.609375 -0.1875 1.328125l0 3.53125l-1.140625 0zm8.84462 -2.46875l1.125 0.140625q-0.171875 1.171875 -0.9375 1.828125q-0.765625 0.65625 -1.859375 0.65625q-1.390625 0 -2.234375 -0.90625q-0.828125 -0.90625 -0.828125 -2.59375q0 -1.09375 0.359375 -1.90625q0.359375 -0.828125 1.09375 -1.234375q0.734375 -0.40625 1.609375 -0.40625q1.09375 0 1.796875 0.5625q0.703125 0.546875 0.890625 1.5625l-1.109375 0.171875q-0.15625 -0.671875 -0.5625 -1.015625q-0.390625 -0.34375 -0.96875 -0.34375q-0.859375 0 -1.40625 0.625q-0.53125 0.609375 -0.53125 1.953125q0 1.359375 0.515625 1.984375q0.515625 0.609375 1.359375 0.609375q0.671875 0 1.125 -0.40625q0.453125 -0.421875 0.5625 -1.28125zm2.2421875 2.46875l0 -9.3125l1.140625 0l0 9.3125l-1.140625 0zm2.99234 -7.984375l0 -1.328125l1.140625 0l0 1.328125l-1.140625 0zm0 7.984375l0 -6.734375l1.140625 0l0 6.734375l-1.140625 0zm4.007965 0l-1.0625 0l0 -9.3125l1.15625 0l0 3.328125q0.71875 -0.90625 1.84375 -0.90625q0.625 0 1.171875 0.25q0.5625 0.25 0.921875 0.703125q0.359375 0.453125 0.5625 1.09375q0.203125 0.640625 0.203125 1.375q0 1.734375 -0.859375 2.6875q-0.859375 0.9375 -2.0625 0.9375q-1.1875 0 -1.875 -1.0l0 0.84375zm-0.015625 -3.421875q0 1.21875 0.34375 1.75q0.53125 0.890625 1.453125 0.890625q0.75 0 1.296875 -0.65625q0.546875 -0.65625 0.546875 -1.9375q0 -1.328125 -0.53125 -1.953125q-0.515625 -0.625 -1.265625 -0.625q-0.75 0 -1.296875 0.65625q-0.546875 0.640625 -0.546875 1.875zm5.9281006 0.625l0 -1.140625l3.515625 0l0 1.140625l-3.515625 0zm4.6727448 3.359375l1.125 0.15625q0.0625 0.515625 0.375 0.75q0.4375 0.328125 1.171875 0.328125q0.78125 0 1.21875 -0.328125q0.4375 -0.3125 0.578125 -0.890625q0.09375 -0.34375 0.09375 -1.453125q-0.75 0.875 -1.875 0.875q-1.390625 0 -2.15625 -1.0q-0.75 -1.0 -0.75 -2.40625q0 -0.96875 0.34375 -1.78125q0.359375 -0.8125 1.015625 -1.25q0.65625 -0.453125 1.5625 -0.453125q1.1875 0 1.96875 0.96875l0 -0.8125l1.046875 0l0 5.8125q0 1.578125 -0.328125 2.234375q-0.3125 0.65625 -1.015625 1.03125q-0.6875 0.390625 -1.703125 0.390625q-1.203125 0 -1.953125 -0.546875q-0.734375 -0.53125 -0.71875 -1.625zm0.953125 -4.046875q0 1.3125 0.515625 1.921875q0.53125 0.609375 1.328125 0.609375q0.796875 0 1.328125 -0.59375q0.53125 -0.609375 0.53125 -1.90625q0 -1.234375 -0.546875 -1.859375q-0.546875 -0.640625 -1.328125 -0.640625q-0.765625 0 -1.296875 0.625q-0.53125 0.625 -0.53125 1.84375zm6.2562256 0.109375q0 -1.875 1.03125 -2.765625q0.875 -0.75 2.125 -0.75q1.390625 0 2.265625 0.90625q0.890625 0.90625 0.890625 2.515625q0 1.296875 -0.390625 2.046875q-0.390625 0.75 -1.140625 1.171875q-0.75 0.40625 -1.625 0.40625q-1.421875 0 -2.296875 -0.90625q-0.859375 -0.90625 -0.859375 -2.625zm1.171875 0q0 1.296875 0.5625 1.953125q0.5625 0.640625 1.421875 0.640625q0.84375 0 1.40625 -0.640625q0.578125 -0.65625 0.578125 -1.984375q0 -1.25 -0.578125 -1.890625q-0.5625 -0.65625 -1.40625 -0.65625q-0.859375 0 -1.421875 0.640625q-0.5625 0.640625 -0.5625 1.9375zm10.631088 3.375l0 -5.859375l-1.0 0l0 -0.875l1.0 0l0 -0.71875q0 -0.6875 0.125 -1.015625q0.171875 -0.4375 0.578125 -0.71875q0.421875 -0.28125 1.171875 -0.28125q0.484375 0 1.0625 0.125l-0.171875 0.984375q-0.359375 -0.0625 -0.671875 -0.0625q-0.515625 0 -0.734375 0.234375q-0.21875 0.21875 -0.21875 0.828125l0 0.625l1.3125 0l0 0.875l-1.3125 0l0 5.859375l-1.140625 0zm3.0154877 -3.375q0 -1.875 1.03125 -2.765625q0.875 -0.75 2.125 -0.75q1.390625 0 2.265625 0.90625q0.890625 0.90625 0.890625 2.515625q0 1.296875 -0.390625 2.046875q-0.390625 0.75 -1.140625 1.171875q-0.75 0.40625 -1.625 0.40625q-1.421875 0 -2.296875 -0.90625q-0.859375 -0.90625 -0.859375 -2.625zm1.171875 0q0 1.296875 0.5625 1.953125q0.5625 0.640625 1.421875 0.640625q0.84375 0 1.40625 -0.640625q0.578125 -0.65625 0.578125 -1.984375q0 -1.25 -0.578125 -1.890625q-0.5625 -0.65625 -1.40625 -0.65625q-0.859375 0 -1.421875 0.640625q-0.5625 0.640625 -0.5625 1.9375zm6.6468506 3.375l0 -6.734375l1.03125 0l0 1.015625q0.390625 -0.71875 0.71875 -0.9375q0.34375 -0.234375 0.734375 -0.234375q0.578125 0 1.171875 0.359375l-0.390625 1.0625q-0.421875 -0.25 -0.828125 -0.25q-0.375 0 -0.6875 0.234375q-0.296875 0.21875 -0.421875 0.625q-0.1875 0.609375 -0.1875 1.328125l0 3.53125l-1.140625 0zm12.656982 -3.65625l0 -1.078125l3.9375 -0.015625l0 3.453125q-0.90625 0.71875 -1.875 1.09375q-0.953125 0.359375 -1.96875 0.359375q-1.375 0 -2.5 -0.578125q-1.125 -0.59375 -1.703125 -1.703125q-0.5625 -1.109375 -0.5625 -2.484375q0 -1.359375 0.5625 -2.53125q0.578125 -1.1875 1.640625 -1.75q1.078125 -0.578125 2.453125 -0.578125q1.015625 0 1.828125 0.328125q0.8125 0.328125 1.28125 0.921875q0.46875 0.578125 0.703125 1.515625l-1.109375 0.296875q-0.203125 -0.703125 -0.515625 -1.109375q-0.3125 -0.40625 -0.890625 -0.640625q-0.578125 -0.25 -1.28125 -0.25q-0.84375 0 -1.46875 0.265625q-0.609375 0.25 -0.984375 0.671875q-0.375 0.40625 -0.59375 0.90625q-0.34375 0.875 -0.34375 1.875q0 1.25 0.421875 2.09375q0.421875 0.828125 1.234375 1.234375q0.828125 0.40625 1.75 0.40625q0.796875 0 1.5625 -0.296875q0.765625 -0.3125 1.15625 -0.671875l0 -1.734375l-2.734375 0zm5.445175 0.28125q0 -1.875 1.03125 -2.765625q0.875 -0.75 2.125 -0.75q1.390625 0 2.265625 0.90625q0.890625 0.90625 0.890625 2.515625q0 1.296875 -0.390625 2.046875q-0.390625 0.75 -1.140625 1.171875q-0.75 0.40625 -1.625 0.40625q-1.421875 0 -2.296875 -0.90625q-0.859375 -0.90625 -0.859375 -2.625zm1.171875 0q0 1.296875 0.5625 1.953125q0.5625 0.640625 1.421875 0.640625q0.84375 0 1.40625 -0.640625q0.578125 -0.65625 0.578125 -1.984375q0 -1.25 -0.578125 -1.890625q-0.5625 -0.65625 -1.40625 -0.65625q-0.859375 0 -1.421875 0.640625q-0.5625 0.640625 -0.5625 1.9375zm6.8031006 3.375l0 -9.3125l3.515625 0q0.921875 0 1.40625 0.09375q0.6875 0.109375 1.15625 0.4375q0.46875 0.3125 0.75 0.890625q0.28125 0.578125 0.28125 1.28125q0 1.1875 -0.765625 2.015625q-0.75 0.8125 -2.71875 0.8125l-2.390625 0l0 3.78125l-1.234375 0zm1.234375 -4.875l2.40625 0q1.1875 0 1.6875 -0.4375q0.515625 -0.453125 0.515625 -1.265625q0 -0.578125 -0.296875 -0.984375q-0.296875 -0.421875 -0.78125 -0.5625q-0.3125 -0.078125 -1.15625 -0.078125l-2.375 0l0 3.328125zm11.90538 4.046875q-0.625 0.53125 -1.21875 0.765625q-0.578125 0.21875 -1.25 0.21875q-1.125 0 -1.71875 -0.546875q-0.59375 -0.546875 -0.59375 -1.390625q0 -0.484375 0.21875 -0.890625q0.234375 -0.421875 0.59375 -0.671875q0.375 -0.25 0.828125 -0.375q0.328125 -0.078125 1.015625 -0.171875q1.375 -0.15625 2.03125 -0.390625q0.015625 -0.234375 0.015625 -0.296875q0 -0.703125 -0.328125 -0.984375q-0.4375 -0.390625 -1.296875 -0.390625q-0.8125 0 -1.203125 0.28125q-0.375 0.28125 -0.5625 1.0l-1.109375 -0.140625q0.140625 -0.71875 0.484375 -1.15625q0.359375 -0.453125 1.015625 -0.6875q0.671875 -0.234375 1.53125 -0.234375q0.875 0 1.40625 0.203125q0.546875 0.203125 0.796875 0.515625q0.25 0.296875 0.359375 0.765625q0.046875 0.296875 0.046875 1.0625l0 1.515625q0 1.59375 0.078125 2.015625q0.078125 0.421875 0.28125 0.8125l-1.1875 0q-0.171875 -0.359375 -0.234375 -0.828125zm-0.09375 -2.5625q-0.625 0.265625 -1.859375 0.4375q-0.703125 0.109375 -1.0 0.234375q-0.296875 0.125 -0.453125 0.375q-0.15625 0.234375 -0.15625 0.53125q0 0.453125 0.34375 0.765625q0.34375 0.296875 1.015625 0.296875q0.65625 0 1.171875 -0.28125q0.515625 -0.296875 0.765625 -0.796875q0.171875 -0.375 0.171875 -1.140625l0 -0.421875zm7.5062256 0.921875l1.125 0.140625q-0.171875 1.171875 -0.9375 1.828125q-0.765625 0.65625 -1.859375 0.65625q-1.390625 0 -2.234375 -0.90625q-0.828125 -0.90625 -0.828125 -2.59375q0 -1.09375 0.359375 -1.90625q0.359375 -0.828125 1.09375 -1.234375q0.734375 -0.40625 1.609375 -0.40625q1.09375 0 1.796875 0.5625q0.703125 0.546875 0.890625 1.5625l-1.109375 0.171875q-0.15625 -0.671875 -0.5625 -1.015625q-0.390625 -0.34375 -0.96875 -0.34375q-0.859375 0 -1.40625 0.625q-0.53125 0.609375 -0.53125 1.953125q0 1.359375 0.515625 1.984375q0.515625 0.609375 1.359375 0.609375q0.671875 0 1.125 -0.40625q0.453125 -0.421875 0.5625 -1.28125zm2.2734375 2.46875l0 -9.3125l1.140625 0l0 5.3125l2.703125 -2.734375l1.484375 0l-2.578125 2.5l2.84375 4.234375l-1.40625 0l-2.234375 -3.453125l-0.8125 0.78125l0 2.671875l-1.140625 0zm11.054672 -0.828125q-0.625 0.53125 -1.21875 0.765625q-0.578125 0.21875 -1.25 0.21875q-1.1249847 0 -1.7187347 -0.546875q-0.59375 -0.546875 -0.59375 -1.390625q0 -0.484375 0.21875 -0.890625q0.234375 -0.421875 0.59375 -0.671875q0.375 -0.25 0.828125 -0.375q0.328125 -0.078125 1.0156097 -0.171875q1.375 -0.15625 2.03125 -0.390625q0.015625 -0.234375 0.015625 -0.296875q0 -0.703125 -0.328125 -0.984375q-0.4375 -0.390625 -1.296875 -0.390625q-0.81248474 0 -1.2031097 0.28125q-0.375 0.28125 -0.5625 1.0l-1.109375 -0.140625q0.140625 -0.71875 0.484375 -1.15625q0.359375 -0.453125 1.015625 -0.6875q0.67185974 -0.234375 1.5312347 -0.234375q0.875 0 1.40625 0.203125q0.546875 0.203125 0.796875 0.515625q0.25 0.296875 0.359375 0.765625q0.046875 0.296875 0.046875 1.0625l0 1.515625q0 1.59375 0.078125 2.015625q0.078125 0.421875 0.28125 0.8125l-1.1875 0q-0.171875 -0.359375 -0.234375 -0.828125zm-0.09375 -2.5625q-0.625 0.265625 -1.859375 0.4375q-0.70310974 0.109375 -0.99998474 0.234375q-0.296875 0.125 -0.453125 0.375q-0.15625 0.234375 -0.15625 0.53125q0 0.453125 0.34375 0.765625q0.34375 0.296875 1.0156097 0.296875q0.65625 0 1.171875 -0.28125q0.515625 -0.296875 0.765625 -0.796875q0.171875 -0.375 0.171875 -1.140625l0 -0.421875zm2.8968506 3.953125l1.125 0.15625q0.0625 0.515625 0.375 0.75q0.4375 0.328125 1.171875 0.328125q0.78125 0 1.21875 -0.328125q0.4375 -0.3125 0.578125 -0.890625q0.09375 -0.34375 0.09375 -1.453125q-0.75 0.875 -1.875 0.875q-1.390625 0 -2.15625 -1.0q-0.75 -1.0 -0.75 -2.40625q0 -0.96875 0.34375 -1.78125q0.359375 -0.8125 1.015625 -1.25q0.65625 -0.453125 1.5625 -0.453125q1.1875 0 1.96875 0.96875l0 -0.8125l1.046875 0l0 5.8125q0 1.578125 -0.328125 2.234375q-0.3125 0.65625 -1.015625 1.03125q-0.6875 0.390625 -1.703125 0.390625q-1.203125 0 -1.953125 -0.546875q-0.734375 -0.53125 -0.71875 -1.625zm0.953125 -4.046875q0 1.3125 0.515625 1.921875q0.53125 0.609375 1.328125 0.609375q0.796875 0 1.328125 -0.59375q0.53125 -0.609375 0.53125 -1.90625q0 -1.234375 -0.546875 -1.859375q-0.546875 -0.640625 -1.328125 -0.640625q-0.765625 0 -1.296875 0.625q-0.53125 0.625 -0.53125 1.84375zm11.287476 1.3125l1.1875 0.140625q-0.28125 1.046875 -1.046875 1.625q-0.75 0.5625 -1.921875 0.5625q-1.484375 0 -2.359375 -0.90625q-0.859375 -0.921875 -0.859375 -2.5625q0 -1.703125 0.875 -2.640625q0.890625 -0.9375 2.28125 -0.9375q1.359375 0 2.203125 0.921875q0.859375 0.921875 0.859375 2.578125q0 0.109375 0 0.3125l-5.03125 0q0.0625 1.109375 0.625 1.703125q0.5625 0.59375 1.40625 0.59375q0.640625 0 1.078125 -0.328125q0.453125 -0.34375 0.703125 -1.0625zm-3.75 -1.84375l3.765625 0q-0.078125 -0.859375 -0.4375 -1.28125q-0.546875 -0.65625 -1.40625 -0.65625q-0.796875 0 -1.328125 0.53125q-0.53125 0.515625 -0.59375 1.40625zm10.0373535 4.578125l1.125 0.15625q0.0625 0.515625 0.375 0.75q0.4375 0.328125 1.171875 0.328125q0.78125 0 1.21875 -0.328125q0.4375 -0.3125 0.578125 -0.890625q0.09375 -0.34375 0.09375 -1.453125q-0.75 0.875 -1.875 0.875q-1.390625 0 -2.15625 -1.0q-0.75 -1.0 -0.75 -2.40625q0 -0.96875 0.34375 -1.78125q0.359375 -0.8125 1.015625 -1.25q0.65625 -0.453125 1.5625 -0.453125q1.1875 0 1.96875 0.96875l0 -0.8125l1.046875 0l0 5.8125q0 1.578125 -0.328125 2.234375q-0.3125 0.65625 -1.015625 1.03125q-0.6875 0.390625 -1.703125 0.390625q-1.203125 0 -1.953125 -0.546875q-0.734375 -0.53125 -0.71875 -1.625zm0.953125 -4.046875q0 1.3125 0.515625 1.921875q0.53125 0.609375 1.328125 0.609375q0.796875 0 1.328125 -0.59375q0.53125 -0.609375 0.53125 -1.90625q0 -1.234375 -0.546875 -1.859375q-0.546875 -0.640625 -1.328125 -0.640625q-0.765625 0 -1.296875 0.625q-0.53125 0.625 -0.53125 1.84375zm6.6624756 3.484375l0 -6.734375l1.03125 0l0 1.015625q0.390625 -0.71875 0.71875 -0.9375q0.34375 -0.234375 0.734375 -0.234375q0.578125 0 1.171875 0.359375l-0.390625 1.0625q-0.421875 -0.25 -0.828125 -0.25q-0.375 0 -0.6875 0.234375q-0.296875 0.21875 -0.421875 0.625q-0.1875 0.609375 -0.1875 1.328125l0 3.53125l-1.140625 0zm8.8446045 -0.828125q-0.625 0.53125 -1.21875 0.765625q-0.578125 0.21875 -1.25 0.21875q-1.125 0 -1.71875 -0.546875q-0.59375 -0.546875 -0.59375 -1.390625q0 -0.484375 0.21875 -0.890625q0.234375 -0.421875 0.59375 -0.671875q0.375 -0.25 0.828125 -0.375q0.328125 -0.078125 1.015625 -0.171875q1.375 -0.15625 2.03125 -0.390625q0.015625 -0.234375 0.015625 -0.296875q0 -0.703125 -0.328125 -0.984375q-0.4375 -0.390625 -1.296875 -0.390625q-0.8125 0 -1.203125 0.28125q-0.375 0.28125 -0.5625 1.0l-1.109375 -0.140625q0.140625 -0.71875 0.484375 -1.15625q0.359375 -0.453125 1.015625 -0.6875q0.671875 -0.234375 1.53125 -0.234375q0.875 0 1.40625 0.203125q0.546875 0.203125 0.796875 0.515625q0.25 0.296875 0.359375 0.765625q0.046875 0.296875 0.046875 1.0625l0 1.515625q0 1.59375 0.078125 2.015625q0.078125 0.421875 0.28125 0.8125l-1.1875 0q-0.171875 -0.359375 -0.234375 -0.828125zm-0.09375 -2.5625q-0.625 0.265625 -1.859375 0.4375q-0.703125 0.109375 -1.0 0.234375q-0.296875 0.125 -0.453125 0.375q-0.15625 0.234375 -0.15625 0.53125q0 0.453125 0.34375 0.765625q0.34375 0.296875 1.015625 0.296875q0.65625 0 1.171875 -0.28125q0.515625 -0.296875 0.765625 -0.796875q0.171875 -0.375 0.171875 -1.140625l0 -0.421875zm3.1156006 5.96875l0 -9.3125l1.03125 0l0 0.875q0.375 -0.515625 0.828125 -0.765625q0.46875 -0.265625 1.140625 -0.265625q0.859375 0 1.515625 0.453125q0.65625 0.4375 0.984375 1.25q0.34375 0.796875 0.34375 1.765625q0 1.03125 -0.375 1.859375q-0.359375 0.828125 -1.078125 1.28125q-0.703125 0.4375 -1.484375 0.4375q-0.5625 0 -1.015625 -0.234375q-0.453125 -0.25 -0.75 -0.625l0 3.28125l-1.140625 0zm1.03125 -5.90625q0 1.296875 0.53125 1.921875q0.53125 0.625 1.265625 0.625q0.765625 0 1.3125 -0.640625q0.546875 -0.65625 0.546875 -2.0q0 -1.296875 -0.53125 -1.9375q-0.53125 -0.640625 -1.265625 -0.640625q-0.734375 0 -1.296875 0.6875q-0.5625 0.671875 -0.5625 1.984375zm6.3812256 3.328125l0 -9.3125l1.140625 0l0 3.34375q0.796875 -0.921875 2.015625 -0.921875q0.75 0 1.296875 0.296875q0.5625 0.296875 0.796875 0.8125q0.234375 0.515625 0.234375 1.515625l0 4.265625l-1.140625 0l0 -4.265625q0 -0.859375 -0.375 -1.25q-0.359375 -0.390625 -1.046875 -0.390625q-0.5 0 -0.953125 0.265625q-0.453125 0.25 -0.640625 0.703125q-0.1875 0.453125 -0.1875 1.25l0 3.6875l-1.140625 0zm10.6936035 -3.375q0 -1.875 1.03125 -2.765625q0.875 -0.75 2.125 -0.75q1.390625 0 2.265625 0.90625q0.890625 0.90625 0.890625 2.515625q0 1.296875 -0.390625 2.046875q-0.390625 0.75 -1.140625 1.171875q-0.75 0.40625 -1.625 0.40625q-1.421875 0 -2.296875 -0.90625q-0.859375 -0.90625 -0.859375 -2.625zm1.171875 0q0 1.296875 0.5625 1.953125q0.5625 0.640625 1.421875 0.640625q0.84375 0 1.40625 -0.640625q0.578125 -0.65625 0.578125 -1.984375q0 -1.25 -0.578125 -1.890625q-0.5625 -0.65625 -1.40625 -0.65625q-0.859375 0 -1.421875 0.640625q-0.5625 0.640625 -0.5625 1.9375zm6.6624756 5.953125l0 -9.3125l1.03125 0l0 0.875q0.375 -0.515625 0.828125 -0.765625q0.46875 -0.265625 1.140625 -0.265625q0.859375 0 1.515625 0.453125q0.65625 0.4375 0.984375 1.25q0.34375 0.796875 0.34375 1.765625q0 1.03125 -0.375 1.859375q-0.359375 0.828125 -1.078125 1.28125q-0.703125 0.4375 -1.484375 0.4375q-0.5625 0 -1.015625 -0.234375q-0.453125 -0.25 -0.75 -0.625l0 3.28125l-1.140625 0zm1.03125 -5.90625q0 1.296875 0.53125 1.921875q0.53125 0.625 1.265625 0.625q0.765625 0 1.3125 -0.640625q0.546875 -0.65625 0.546875 -2.0q0 -1.296875 -0.53125 -1.9375q-0.53125 -0.640625 -1.265625 -0.640625q-0.734375 0 -1.296875 0.6875q-0.5625 0.671875 -0.5625 1.984375z" fill-rule="nonzero"></path><path fill="#d9ead3" d="m19.745407 773.39557l399.90552 0l0 52.22052l-399.90552 0z" fill-rule="nonzero"></path><path fill="#38761d" d="m164.45317 798.42584l-3.609375 -13.59375l1.84375 0l2.0625 8.90625q0.34375 1.40625 0.578125 2.78125q0.515625 -2.171875 0.609375 -2.515625l2.59375 -9.171875l2.171875 0l1.953125 6.875q0.734375 2.5625 1.046875 4.8125q0.265625 -1.28125 0.6875 -2.953125l2.125 -8.734375l1.8125 0l-3.734375 13.59375l-1.734375 0l-2.859375 -10.359375q-0.359375 -1.296875 -0.421875 -1.59375q-0.21875 0.9375 -0.40625 1.59375l-2.890625 10.359375l-1.828125 0zm14.999283 0l0 -9.859375l1.5 0l0 1.5q0.578125 -1.046875 1.0625 -1.375q0.484375 -0.34375 1.078125 -0.34375q0.84375 0 1.71875 0.546875l-0.578125 1.546875q-0.609375 -0.359375 -1.234375 -0.359375q-0.546875 0 -0.984375 0.328125q-0.421875 0.328125 -0.609375 0.90625q-0.28125 0.890625 -0.28125 1.953125l0 5.15625l-1.671875 0zm6.243927 -11.6875l0 -1.90625l1.671875 0l0 1.90625l-1.671875 0zm0 11.6875l0 -9.859375l1.671875 0l0 9.859375l-1.671875 0zm7.785446 -1.5l0.234375 1.484375q-0.703125 0.140625 -1.265625 0.140625q-0.90625 0 -1.40625 -0.28125q-0.5 -0.296875 -0.703125 -0.75q-0.203125 -0.46875 -0.203125 -1.984375l0 -5.65625l-1.234375 0l0 -1.3125l1.234375 0l0 -2.4375l1.65625 -1.0l0 3.4375l1.6875 0l0 1.3125l-1.6875 0l0 5.75q0 0.71875 0.078125 0.921875q0.09375 0.203125 0.296875 0.328125q0.203125 0.125 0.578125 0.125q0.265625 0 0.734375 -0.078125zm8.277054 -1.671875l1.71875 0.21875q-0.40625 1.5 -1.515625 2.34375q-1.09375 0.828125 -2.8125 0.828125q-2.15625 0 -3.421875 -1.328125q-1.265625 -1.328125 -1.265625 -3.734375q0 -2.484375 1.265625 -3.859375q1.28125 -1.375 3.328125 -1.375q1.984375 0 3.234375 1.34375q1.25 1.34375 1.25 3.796875q0 0.140625 -0.015625 0.4375l-7.34375 0q0.09375 1.625 0.921875 2.484375q0.828125 0.859375 2.0625 0.859375q0.90625 0 1.546875 -0.46875q0.65625 -0.484375 1.046875 -1.546875zm-5.484375 -2.703125l5.5 0q-0.109375 -1.234375 -0.625 -1.859375q-0.796875 -0.96875 -2.078125 -0.96875q-1.140625 0 -1.9375 0.78125q-0.78125 0.765625 -0.859375 2.046875zm14.449646 5.875l0 -13.59375l2.71875 0l3.21875 9.625q0.4375 1.34375 0.640625 2.015625q0.234375 -0.75 0.734375 -2.1875l3.25 -9.453125l2.421875 0l0 13.59375l-1.734375 0l0 -11.390625l-3.953125 11.390625l-1.625 0l-3.9375 -11.578125l0 11.578125l-1.734375 0zm21.822052 -1.21875q-0.9375 0.796875 -1.796875 1.125q-0.859375 0.3125 -1.84375 0.3125q-1.609375 0 -2.484375 -0.78125q-0.875 -0.796875 -0.875 -2.03125q0 -0.734375 0.328125 -1.328125q0.328125 -0.59375 0.859375 -0.953125q0.53125 -0.359375 1.203125 -0.546875q0.5 -0.140625 1.484375 -0.25q2.03125 -0.25 2.984375 -0.578125q0 -0.34375 0 -0.4375q0 -1.015625 -0.46875 -1.4375q-0.640625 -0.5625 -1.90625 -0.5625q-1.171875 0 -1.734375 0.40625q-0.5625 0.40625 -0.828125 1.46875l-1.640625 -0.234375q0.234375 -1.046875 0.734375 -1.6875q0.515625 -0.640625 1.46875 -0.984375q0.96875 -0.359375 2.25 -0.359375q1.265625 0 2.046875 0.296875q0.78125 0.296875 1.15625 0.75q0.375 0.453125 0.515625 1.140625q0.09375 0.421875 0.09375 1.53125l0 2.234375q0 2.328125 0.09375 2.953125q0.109375 0.609375 0.4375 1.171875l-1.75 0q-0.265625 -0.515625 -0.328125 -1.21875zm-0.140625 -3.71875q-0.90625 0.359375 -2.734375 0.625q-1.03125 0.140625 -1.453125 0.328125q-0.421875 0.1875 -0.65625 0.546875q-0.234375 0.359375 -0.234375 0.796875q0 0.671875 0.5 1.125q0.515625 0.4375 1.484375 0.4375q0.96875 0 1.71875 -0.421875q0.75 -0.4375 1.109375 -1.15625q0.265625 -0.578125 0.265625 -1.671875l0 -0.609375zm4.094467 4.9375l0 -13.59375l1.671875 0l0 7.75l3.953125 -4.015625l2.15625 0l-3.765625 3.65625l4.140625 6.203125l-2.0625 0l-3.25 -5.03125l-1.171875 1.125l0 3.90625l-1.671875 0zm16.0625 -3.171875l1.71875 0.21875q-0.40625 1.5 -1.515625 2.34375q-1.09375 0.828125 -2.8125 0.828125q-2.15625 0 -3.421875 -1.328125q-1.265625 -1.328125 -1.265625 -3.734375q0 -2.484375 1.265625 -3.859375q1.28125 -1.375 3.328125 -1.375q1.984375 0 3.234375 1.34375q1.25 1.34375 1.25 3.796875q0 0.140625 -0.015625 0.4375l-7.34375 0q0.09375 1.625 0.921875 2.484375q0.828125 0.859375 2.0625 0.859375q0.90625 0 1.546875 -0.46875q0.65625 -0.484375 1.046875 -1.546875zm-5.484375 -2.703125l5.5 0q-0.109375 -1.234375 -0.625 -1.859375q-0.796875 -0.96875 -2.078125 -0.96875q-1.140625 0 -1.9375 0.78125q-0.78125 0.765625 -0.859375 2.046875zm9.516342 5.875l0 -8.546875l-1.484375 0l0 -1.3125l1.484375 0l0 -1.046875q0 -0.984375 0.171875 -1.46875q0.234375 -0.65625 0.84375 -1.046875q0.609375 -0.40625 1.703125 -0.40625q0.703125 0 1.5625 0.15625l-0.25 1.46875q-0.515625 -0.09375 -0.984375 -0.09375q-0.765625 0 -1.078125 0.328125q-0.3125 0.3125 -0.3125 1.203125l0 0.90625l1.921875 0l0 1.3125l-1.921875 0l0 8.546875l-1.65625 0zm4.7926636 -11.6875l0 -1.90625l1.671875 0l0 1.90625l-1.671875 0zm0 11.6875l0 -9.859375l1.671875 0l0 9.859375l-1.671875 0zm4.0979614 0l0 -13.59375l1.671875 0l0 13.59375l-1.671875 0zm10.926056 -3.171875l1.71875 0.21875q-0.40625 1.5 -1.515625 2.34375q-1.09375 0.828125 -2.8125 0.828125q-2.15625 0 -3.421875 -1.328125q-1.265625 -1.328125 -1.265625 -3.734375q0 -2.484375 1.265625 -3.859375q1.28125 -1.375 3.328125 -1.375q1.984375 0 3.234375 1.34375q1.25 1.34375 1.25 3.796875q0 0.140625 -0.015625 0.4375l-7.34375 0q0.09375 1.625 0.921875 2.484375q0.828125 0.859375 2.0625 0.859375q0.90625 0 1.546875 -0.46875q0.65625 -0.484375 1.046875 -1.546875zm-5.484375 -2.703125l5.5 0q-0.109375 -1.234375 -0.625 -1.859375q-0.796875 -0.96875 -2.078125 -0.96875q-1.140625 0 -1.9375 0.78125q-0.78125 0.765625 -0.859375 2.046875z" fill-rule="nonzero"></path><path fill="#38761d" d="m102.88392 812.3215l1.171875 -0.109375q0.078125 0.703125 0.375 1.15625q0.3125 0.4375 0.9375 0.71875q0.640625 0.265625 1.4375 0.265625q0.703125 0 1.234375 -0.203125q0.546875 -0.203125 0.8125 -0.5625q0.265625 -0.375 0.265625 -0.8125q0 -0.4375 -0.265625 -0.765625q-0.25 -0.328125 -0.828125 -0.546875q-0.375 -0.140625 -1.65625 -0.453125q-1.28125 -0.3125 -1.796875 -0.578125q-0.671875 -0.34375 -1.0 -0.859375q-0.328125 -0.53125 -0.328125 -1.171875q0 -0.703125 0.390625 -1.3125q0.40625 -0.609375 1.171875 -0.921875q0.78125 -0.328125 1.71875 -0.328125q1.03125 0 1.8125 0.34375q0.796875 0.328125 1.21875 0.984375q0.4375 0.640625 0.46875 1.453125l-1.1875 0.09375q-0.09375 -0.890625 -0.640625 -1.328125q-0.546875 -0.453125 -1.625 -0.453125q-1.109375 0 -1.625 0.40625q-0.515625 0.40625 -0.515625 0.984375q0 0.5 0.359375 0.828125q0.359375 0.328125 1.859375 0.671875q1.5 0.328125 2.0625 0.578125q0.8125 0.375 1.1875 0.953125q0.390625 0.578125 0.390625 1.328125q0 0.734375 -0.421875 1.390625q-0.421875 0.65625 -1.21875 1.03125q-0.796875 0.359375 -1.796875 0.359375q-1.265625 0 -2.125 -0.359375q-0.84375 -0.375 -1.328125 -1.109375q-0.484375 -0.75 -0.515625 -1.671875zm13.56163 2.15625q-0.625 0.53125 -1.21875 0.765625q-0.578125 0.21875 -1.25 0.21875q-1.125 0 -1.71875 -0.546875q-0.59375 -0.546875 -0.59375 -1.390625q0 -0.484375 0.21875 -0.890625q0.234375 -0.421875 0.59375 -0.671875q0.375 -0.25 0.828125 -0.375q0.328125 -0.078125 1.015625 -0.171875q1.375 -0.15625 2.03125 -0.390625q0.015625 -0.234375 0.015625 -0.296875q0 -0.703125 -0.328125 -0.984375q-0.4375 -0.390625 -1.296875 -0.390625q-0.8125 0 -1.203125 0.28125q-0.375 0.28125 -0.5625 1.0l-1.109375 -0.140625q0.140625 -0.71875 0.484375 -1.15625q0.359375 -0.453125 1.015625 -0.6875q0.671875 -0.234375 1.53125 -0.234375q0.875 0 1.40625 0.203125q0.546875 0.203125 0.796875 0.515625q0.25 0.296875 0.359375 0.765625q0.046875 0.296875 0.046875 1.0625l0 1.515625q0 1.59375 0.078125 2.015625q0.078125 0.421875 0.28125 0.8125l-1.1875 0q-0.171875 -0.359375 -0.234375 -0.828125zm-0.09375 -2.5625q-0.625 0.265625 -1.859375 0.4375q-0.703125 0.109375 -1.0 0.234375q-0.296875 0.125 -0.453125 0.375q-0.15625 0.234375 -0.15625 0.53125q0 0.453125 0.34375 0.765625q0.34375 0.296875 1.015625 0.296875q0.65625 0 1.171875 -0.28125q0.515625 -0.296875 0.765625 -0.796875q0.171875 -0.375 0.171875 -1.140625l0 -0.421875zm4.9906006 3.390625l-2.5625 -6.734375l1.203125 0l1.4375 4.03125q0.234375 0.65625 0.4375 1.359375q0.15625 -0.53125 0.421875 -1.28125l1.5 -4.109375l1.171875 0l-2.546875 6.734375l-1.0625 0zm9.39843 -2.171875l1.1875 0.140625q-0.28125 1.046875 -1.046875 1.625q-0.75 0.5625 -1.921875 0.5625q-1.4843674 0 -2.3593674 -0.90625q-0.859375 -0.921875 -0.859375 -2.5625q0 -1.703125 0.875 -2.640625q0.890625 -0.9375 2.2812424 -0.9375q1.359375 0 2.203125 0.921875q0.859375 0.921875 0.859375 2.578125q0 0.109375 0 0.3125l-5.0312424 0q0.0625 1.109375 0.625 1.703125q0.5624924 0.59375 1.4062424 0.59375q0.640625 0 1.078125 -0.328125q0.453125 -0.34375 0.703125 -1.0625zm-3.7499924 -1.84375l3.7656174 0q-0.078125 -0.859375 -0.4375 -1.28125q-0.546875 -0.65625 -1.40625 -0.65625q-0.796875 0 -1.3281174 0.53125q-0.53125 0.515625 -0.59375 1.40625zm12.756081 3.0l0.15625 1.0q-0.484375 0.109375 -0.859375 0.109375q-0.625 0 -0.96875 -0.203125q-0.34375 -0.203125 -0.484375 -0.515625q-0.140625 -0.328125 -0.140625 -1.34375l0 -3.890625l-0.828125 0l0 -0.875l0.828125 0l0 -1.671875l1.140625 -0.6875l0 2.359375l1.15625 0l0 0.875l-1.15625 0l0 3.953125q0 0.484375 0.0625 0.625q0.0625 0.140625 0.1875 0.21875q0.140625 0.078125 0.390625 0.078125q0.203125 0 0.515625 -0.03125zm0.7811127 -2.359375q0 -1.875 1.03125 -2.765625q0.875 -0.75 2.125 -0.75q1.390625 0 2.265625 0.90625q0.890625 0.90625 0.890625 2.515625q0 1.296875 -0.390625 2.046875q-0.390625 0.75 -1.140625 1.171875q-0.75 0.40625 -1.625 0.40625q-1.421875 0 -2.296875 -0.90625q-0.859375 -0.90625 -0.859375 -2.625zm1.171875 0q0 1.296875 0.5625 1.953125q0.5625 0.640625 1.421875 0.640625q0.84375 0 1.40625 -0.640625q0.578125 -0.65625 0.578125 -1.984375q0 -1.25 -0.578125 -1.890625q-0.5625 -0.65625 -1.40625 -0.65625q-0.859375 0 -1.421875 0.640625q-0.5625 0.640625 -0.5625 1.9375zm10.6936035 3.375l0 -1.296875l1.296875 0l0 1.296875l-1.296875 0zm2.9217224 -2.015625l1.125 -0.171875q0.09375 0.671875 0.53125 1.046875q0.4375 0.359375 1.21875 0.359375q0.78125 0 1.15625 -0.3125q0.390625 -0.328125 0.390625 -0.765625q0 -0.390625 -0.34375 -0.609375q-0.234375 -0.15625 -1.171875 -0.390625q-1.25 -0.3125 -1.734375 -0.546875q-0.484375 -0.234375 -0.734375 -0.640625q-0.25 -0.40625 -0.25 -0.90625q0 -0.453125 0.203125 -0.828125q0.203125 -0.390625 0.5625 -0.640625q0.265625 -0.203125 0.71875 -0.328125q0.46875 -0.140625 1.0 -0.140625q0.78125 0 1.375 0.234375q0.609375 0.21875 0.890625 0.609375q0.296875 0.390625 0.40625 1.046875l-1.125 0.15625q-0.078125 -0.53125 -0.4375 -0.8125q-0.359375 -0.296875 -1.03125 -0.296875q-0.78125 0 -1.125 0.265625q-0.34375 0.25 -0.34375 0.609375q0 0.21875 0.140625 0.390625q0.140625 0.1875 0.4375 0.3125q0.171875 0.0625 1.015625 0.28125q1.21875 0.328125 1.6875 0.53125q0.484375 0.203125 0.75 0.609375q0.28125 0.390625 0.28125 0.96875q0 0.578125 -0.34375 1.078125q-0.328125 0.5 -0.953125 0.78125q-0.625 0.28125 -1.421875 0.28125q-1.3125 0 -2.0 -0.546875q-0.6875 -0.546875 -0.875 -1.625zm7.1015625 2.015625l0 -6.734375l1.03125 0l0 1.015625q0.390625 -0.71875 0.71875 -0.9375q0.34375 -0.234375 0.734375 -0.234375q0.578125 0 1.171875 0.359375l-0.390625 1.0625q-0.421875 -0.25 -0.828125 -0.25q-0.375 0 -0.6875 0.234375q-0.296875 0.21875 -0.421875 0.625q-0.1875 0.609375 -0.1875 1.328125l0 3.53125l-1.140625 0zm8.844635 -2.46875l1.125 0.140625q-0.171875 1.171875 -0.9375 1.828125q-0.765625 0.65625 -1.859375 0.65625q-1.390625 0 -2.234375 -0.90625q-0.828125 -0.90625 -0.828125 -2.59375q0 -1.09375 0.359375 -1.90625q0.359375 -0.828125 1.09375 -1.234375q0.734375 -0.40625 1.609375 -0.40625q1.09375 0 1.796875 0.5625q0.703125 0.546875 0.890625 1.5625l-1.109375 0.171875q-0.15625 -0.671875 -0.5625 -1.015625q-0.390625 -0.34375 -0.96875 -0.34375q-0.859375 0 -1.40625 0.625q-0.53125 0.609375 -0.53125 1.953125q0 1.359375 0.515625 1.984375q0.515625 0.609375 1.359375 0.609375q0.671875 0 1.125 -0.40625q0.453125 -0.421875 0.5625 -1.28125zm2.2421875 2.46875l0 -9.3125l1.140625 0l0 9.3125l-1.140625 0zm2.99234 -7.984375l0 -1.328125l1.140625 0l0 1.328125l-1.140625 0zm0 7.984375l0 -6.734375l1.140625 0l0 6.734375l-1.140625 0zm4.007965 0l-1.0625 0l0 -9.3125l1.15625 0l0 3.328125q0.71875 -0.90625 1.84375 -0.90625q0.625 0 1.171875 0.25q0.5625 0.25 0.921875 0.703125q0.359375 0.453125 0.5625 1.09375q0.203125 0.640625 0.203125 1.375q0 1.734375 -0.859375 2.6875q-0.859375 0.9375 -2.0625 0.9375q-1.1875 0 -1.875 -1.0l0 0.84375zm-0.015625 -3.421875q0 1.21875 0.34375 1.75q0.53125 0.890625 1.453125 0.890625q0.75 0 1.296875 -0.65625q0.546875 -0.65625 0.546875 -1.9375q0 -1.328125 -0.53125 -1.953125q-0.515625 -0.625 -1.265625 -0.625q-0.75 0 -1.296875 0.65625q-0.546875 0.640625 -0.546875 1.875zm5.9281006 0.625l0 -1.140625l3.515625 0l0 1.140625l-3.515625 0zm9.2821045 0.328125l1.125 0.140625q-0.171875 1.171875 -0.9375 1.828125q-0.765625 0.65625 -1.859375 0.65625q-1.390625 0 -2.234375 -0.90625q-0.828125 -0.90625 -0.828125 -2.59375q0 -1.09375 0.359375 -1.90625q0.359375 -0.828125 1.09375 -1.234375q0.734375 -0.40625 1.609375 -0.40625q1.09375 0 1.796875 0.5625q0.703125 0.546875 0.890625 1.5625l-1.109375 0.171875q-0.15625 -0.671875 -0.5625 -1.015625q-0.390625 -0.34375 -0.96875 -0.34375q-0.859375 0 -1.40625 0.625q-0.53125 0.609375 -0.53125 1.953125q0 1.359375 0.515625 1.984375q0.515625 0.609375 1.359375 0.609375q0.671875 0 1.125 -0.40625q0.453125 -0.421875 0.5625 -1.28125zm6.6640625 1.640625q-0.625 0.53125 -1.21875 0.765625q-0.578125 0.21875 -1.25 0.21875q-1.125 0 -1.71875 -0.546875q-0.59375 -0.546875 -0.59375 -1.390625q0 -0.484375 0.21875 -0.890625q0.234375 -0.421875 0.59375 -0.671875q0.375 -0.25 0.828125 -0.375q0.328125 -0.078125 1.015625 -0.171875q1.375 -0.15625 2.03125 -0.390625q0.015625 -0.234375 0.015625 -0.296875q0 -0.703125 -0.328125 -0.984375q-0.4375 -0.390625 -1.296875 -0.390625q-0.8125 0 -1.203125 0.28125q-0.375 0.28125 -0.5625 1.0l-1.109375 -0.140625q0.140625 -0.71875 0.484375 -1.15625q0.359375 -0.453125 1.015625 -0.6875q0.671875 -0.234375 1.53125 -0.234375q0.875 0 1.40625 0.203125q0.546875 0.203125 0.796875 0.515625q0.25 0.296875 0.359375 0.765625q0.046875 0.296875 0.046875 1.0625l0 1.515625q0 1.59375 0.078125 2.015625q0.078125 0.421875 0.28125 0.8125l-1.1875 0q-0.171875 -0.359375 -0.234375 -0.828125zm-0.09375 -2.5625q-0.625 0.265625 -1.859375 0.4375q-0.703125 0.109375 -1.0 0.234375q-0.296875 0.125 -0.453125 0.375q-0.15625 0.234375 -0.15625 0.53125q0 0.453125 0.34375 0.765625q0.34375 0.296875 1.015625 0.296875q0.65625 0 1.171875 -0.28125q0.515625 -0.296875 0.765625 -0.796875q0.171875 -0.375 0.171875 -1.140625l0 -0.421875zm7.5062256 0.921875l1.125 0.140625q-0.171875 1.171875 -0.9375 1.828125q-0.765625 0.65625 -1.859375 0.65625q-1.390625 0 -2.234375 -0.90625q-0.828125 -0.90625 -0.828125 -2.59375q0 -1.09375 0.359375 -1.90625q0.359375 -0.828125 1.09375 -1.234375q0.734375 -0.40625 1.609375 -0.40625q1.09375 0 1.796875 0.5625q0.703125 0.546875 0.890625 1.5625l-1.109375 0.171875q-0.15625 -0.671875 -0.5625 -1.015625q-0.390625 -0.34375 -0.96875 -0.34375q-0.859375 0 -1.40625 0.625q-0.53125 0.609375 -0.53125 1.953125q0 1.359375 0.515625 1.984375q0.515625 0.609375 1.359375 0.609375q0.671875 0 1.125 -0.40625q0.453125 -0.421875 0.5625 -1.28125zm2.2734375 2.46875l0 -9.3125l1.140625 0l0 3.34375q0.796875 -0.921875 2.015625 -0.921875q0.75 0 1.296875 0.296875q0.5625 0.296875 0.796875 0.8125q0.234375 0.515625 0.234375 1.515625l0 4.265625l-1.140625 0l0 -4.265625q0 -0.859375 -0.375 -1.25q-0.359375 -0.390625 -1.046875 -0.390625q-0.5 0 -0.953125 0.265625q-0.453125 0.25 -0.640625 0.703125q-0.1875 0.453125 -0.1875 1.25l0 3.6875l-1.140625 0zm12.021851 -2.171875l1.1875 0.140625q-0.28125 1.046875 -1.046875 1.625q-0.75 0.5625 -1.921875 0.5625q-1.484375 0 -2.359375 -0.90625q-0.859375 -0.921875 -0.859375 -2.5625q0 -1.703125 0.875 -2.640625q0.890625 -0.9375 2.28125 -0.9375q1.359375 0 2.203125 0.921875q0.859375 0.921875 0.859375 2.578125q0 0.109375 0 0.3125l-5.03125 0q0.0625 1.109375 0.625 1.703125q0.5625 0.59375 1.40625 0.59375q0.640625 0 1.078125 -0.328125q0.453125 -0.34375 0.703125 -1.0625zm-3.75 -1.84375l3.765625 0q-0.078125 -0.859375 -0.4375 -1.28125q-0.546875 -0.65625 -1.40625 -0.65625q-0.796875 0 -1.328125 0.53125q-0.53125 0.515625 -0.59375 1.40625zm5.6937256 4.171875l2.703125 -9.625l0.90625 0l-2.6875 9.625l-0.921875 0zm11.343628 -3.421875l1.234375 0.3125q-0.390625 1.515625 -1.40625 2.3125q-1.0 0.796875 -2.453125 0.796875q-1.5 0 -2.453125 -0.609375q-0.9375 -0.609375 -1.4375 -1.765625q-0.484375 -1.171875 -0.484375 -2.5q0 -1.453125 0.5625 -2.53125q0.5625 -1.09375 1.578125 -1.65625q1.03125 -0.5625 2.265625 -0.5625q1.390625 0 2.34375 0.71875q0.953125 0.703125 1.328125 2.0l-1.21875 0.28125q-0.328125 -1.015625 -0.9375 -1.46875q-0.609375 -0.46875 -1.546875 -0.46875q-1.078125 0 -1.796875 0.515625q-0.71875 0.515625 -1.015625 1.375q-0.28125 0.859375 -0.28125 1.78125q0 1.1875 0.34375 2.078125q0.34375 0.890625 1.0625 1.328125q0.734375 0.4375 1.59375 0.4375q1.03125 0 1.75 -0.59375q0.71875 -0.609375 0.96875 -1.78125zm2.6095276 -1.265625q0 -2.3125 1.234375 -3.625q1.25 -1.3125 3.21875 -1.3125q1.296875 0 2.328125 0.625q1.03125 0.609375 1.578125 1.71875q0.546875 1.09375 0.546875 2.484375q0 1.421875 -0.578125 2.546875q-0.5625 1.109375 -1.609375 1.6875q-1.046875 0.5625 -2.265625 0.5625q-1.3125 0 -2.359375 -0.625q-1.03125 -0.640625 -1.5625 -1.734375q-0.53125 -1.109375 -0.53125 -2.328125zm1.265625 0.015625q0 1.6875 0.90625 2.65625q0.90625 0.96875 2.28125 0.96875q1.390625 0 2.28125 -0.96875q0.90625 -0.984375 0.90625 -2.78125q0 -1.140625 -0.390625 -1.984375q-0.390625 -0.859375 -1.125 -1.3125q-0.734375 -0.46875 -1.65625 -0.46875q-1.3125 0 -2.265625 0.90625q-0.9375 0.890625 -0.9375 2.984375zm9.44516 4.515625l0 -9.3125l1.84375 0l2.203125 6.59375q0.3125 0.921875 0.453125 1.375q0.15625 -0.5 0.484375 -1.484375l2.2343597 -6.484375l1.65625 0l0 9.3125l-1.1875 0l0 -7.78125l-2.7031097 7.78125l-1.109375 0l-2.6875 -7.921875l0 7.921875l-1.1875 0zm11.102432 0l0 -9.3125l1.84375 0l2.203125 6.59375q0.3125 0.921875 0.453125 1.375q0.15625 -0.5 0.484375 -1.484375l2.234375 -6.484375l1.65625 0l0 9.3125l-1.1875 0l0 -7.78125l-2.703125 7.78125l-1.109375 0l-2.6875 -7.921875l0 7.921875l-1.1875 0zm11.352417 0l0 -9.3125l1.21875 0l0 9.3125l-1.21875 0zm5.859253 0l0 -8.203125l-3.0625 0l0 -1.109375l7.375 0l0 1.109375l-3.078125 0l0 8.203125l-1.234375 0zm4.7663574 0.15625l2.703125 -9.625l0.90625 0l-2.6875 9.625l-0.921875 0zm4.6717224 -0.15625l0 -9.3125l1.84375 0l2.203125 6.59375q0.3125 0.921875 0.453125 1.375q0.15625 -0.5 0.484375 -1.484375l2.234375 -6.484375l1.65625 0l0 9.3125l-1.1875 0l0 -7.78125l-2.703125 7.78125l-1.109375 0l-2.6875 -7.921875l0 7.921875l-1.1875 0zm15.3836975 -0.828125q-0.625 0.53125 -1.21875 0.765625q-0.578125 0.21875 -1.25 0.21875q-1.125 0 -1.71875 -0.546875q-0.59375 -0.546875 -0.59375 -1.390625q0 -0.484375 0.21875 -0.890625q0.234375 -0.421875 0.59375 -0.671875q0.375 -0.25 0.828125 -0.375q0.328125 -0.078125 1.015625 -0.171875q1.375 -0.15625 2.03125 -0.390625q0.015625 -0.234375 0.015625 -0.296875q0 -0.703125 -0.328125 -0.984375q-0.4375 -0.390625 -1.296875 -0.390625q-0.8125 0 -1.203125 0.28125q-0.375 0.28125 -0.5625 1.0l-1.109375 -0.140625q0.140625 -0.71875 0.484375 -1.15625q0.359375 -0.453125 1.015625 -0.6875q0.671875 -0.234375 1.53125 -0.234375q0.875 0 1.40625 0.203125q0.546875 0.203125 0.796875 0.515625q0.25 0.296875 0.359375 0.765625q0.046875 0.296875 0.046875 1.0625l0 1.515625q0 1.59375 0.078125 2.015625q0.078125 0.421875 0.28125 0.8125l-1.1875 0q-0.171875 -0.359375 -0.234375 -0.828125zm-0.09375 -2.5625q-0.625 0.265625 -1.859375 0.4375q-0.703125 0.109375 -1.0 0.234375q-0.296875 0.125 -0.453125 0.375q-0.15625 0.234375 -0.15625 0.53125q0 0.453125 0.34375 0.765625q0.34375 0.296875 1.015625 0.296875q0.65625 0 1.171875 -0.28125q0.515625 -0.296875 0.765625 -0.796875q0.171875 -0.375 0.171875 -1.140625l0 -0.421875zm3.1156006 3.390625l0 -9.3125l1.140625 0l0 5.3125l2.703125 -2.734375l1.484375 0l-2.578125 2.5l2.84375 4.234375l-1.40625 0l-2.234375 -3.453125l-0.8125 0.78125l0 2.671875l-1.140625 0zm11.2734375 -2.171875l1.1875 0.140625q-0.28125 1.046875 -1.046875 1.625q-0.75 0.5625 -1.921875 0.5625q-1.484375 0 -2.359375 -0.90625q-0.859375 -0.921875 -0.859375 -2.5625q0 -1.703125 0.875 -2.640625q0.890625 -0.9375 2.28125 -0.9375q1.359375 0 2.203125 0.921875q0.859375 0.921875 0.859375 2.578125q0 0.109375 0 0.3125l-5.03125 0q0.0625 1.109375 0.625 1.703125q0.5625 0.59375 1.40625 0.59375q0.640625 0 1.078125 -0.328125q0.453125 -0.34375 0.703125 -1.0625zm-3.75 -1.84375l3.765625 0q-0.078125 -0.859375 -0.4375 -1.28125q-0.546875 -0.65625 -1.40625 -0.65625q-0.796875 0 -1.328125 0.53125q-0.53125 0.515625 -0.59375 1.40625zm6.8187256 4.015625l0 -5.859375l-1.0 0l0 -0.875l1.0 0l0 -0.71875q0 -0.6875 0.125 -1.015625q0.171875 -0.4375 0.578125 -0.71875q0.421875 -0.28125 1.171875 -0.28125q0.484375 0 1.0625 0.125l-0.171875 0.984375q-0.359375 -0.0625 -0.671875 -0.0625q-0.515625 0 -0.734375 0.234375q-0.21875 0.21875 -0.21875 0.828125l0 0.625l1.3125 0l0 0.875l-1.3125 0l0 5.859375l-1.140625 0zm3.4373474 -7.984375l0 -1.328125l1.140625 0l0 1.328125l-1.140625 0zm0 7.984375l0 -6.734375l1.140625 0l0 6.734375l-1.140625 0zm2.92984 0l0 -9.3125l1.140625 0l0 9.3125l-1.140625 0zm7.601715 -2.171875l1.1875 0.140625q-0.28125 1.046875 -1.046875 1.625q-0.75 0.5625 -1.921875 0.5625q-1.484375 0 -2.359375 -0.90625q-0.859375 -0.921875 -0.859375 -2.5625q0 -1.703125 0.875 -2.640625q0.890625 -0.9375 2.28125 -0.9375q1.359375 0 2.203125 0.921875q0.859375 0.921875 0.859375 2.578125q0 0.109375 0 0.3125l-5.03125 0q0.0625 1.109375 0.625 1.703125q0.5625 0.59375 1.40625 0.59375q0.640625 0 1.078125 -0.328125q0.453125 -0.34375 0.703125 -1.0625zm-3.75 -1.84375l3.765625 0q-0.078125 -0.859375 -0.4375 -1.28125q-0.546875 -0.65625 -1.40625 -0.65625q-0.796875 0 -1.328125 0.53125q-0.53125 0.515625 -0.59375 1.40625z" fill-rule="nonzero"></path><path fill="#000000" fill-opacity="0.0" d="m220.68619 595.0878l0 18.604553" fill-rule="nonzero"></path><path stroke="#d9ead3" stroke-width="1.0" stroke-linejoin="round" stroke-linecap="butt" d="m220.68619 595.0878l0 12.604553" fill-rule="evenodd"></path><path fill="#d9ead3" stroke="#d9ead3" stroke-width="1.0" stroke-linecap="butt" d="m219.03445 607.6924l1.6517334 4.538086l1.6517334 -4.538086z" fill-rule="evenodd"></path><path fill="#d9ead3" d="m56.81743 684.51917l325.92126 0l0 52.22046l-325.92126 0z" fill-rule="nonzero"></path><path fill="#38761d" d="m143.99828 701.5494l0 -13.59375l4.6875 0q1.578125 0 2.421875 0.1875q1.15625 0.265625 1.984375 0.96875q1.078125 0.921875 1.609375 2.34375q0.53125 1.40625 0.53125 3.21875q0 1.546875 -0.359375 2.75q-0.359375 1.1875 -0.921875 1.984375q-0.5625 0.78125 -1.234375 1.234375q-0.671875 0.4375 -1.625 0.671875q-0.953125 0.234375 -2.1875 0.234375l-4.90625 0zm1.796875 -1.609375l2.90625 0q1.34375 0 2.109375 -0.25q0.765625 -0.25 1.21875 -0.703125q0.640625 -0.640625 1.0 -1.71875q0.359375 -1.078125 0.359375 -2.625q0 -2.125 -0.703125 -3.265625q-0.703125 -1.15625 -1.703125 -1.546875q-0.71875 -0.28125 -2.328125 -0.28125l-2.859375 0l0 10.390625zm18.207321 -1.5625l1.71875 0.21875q-0.40625 1.5 -1.515625 2.34375q-1.09375 0.828125 -2.8125 0.828125q-2.15625 0 -3.421875 -1.328125q-1.265625 -1.328125 -1.265625 -3.734375q0 -2.484375 1.265625 -3.859375q1.28125 -1.375 3.328125 -1.375q1.984375 0 3.234375 1.34375q1.25 1.34375 1.25 3.796875q0 0.140625 -0.015625 0.4375l-7.34375 0q0.09375 1.625 0.921875 2.484375q0.828125 0.859375 2.0625 0.859375q0.90625 0 1.546875 -0.46875q0.65625 -0.484375 1.046875 -1.546875zm-5.484375 -2.703125l5.5 0q-0.109375 -1.234375 -0.625 -1.859375q-0.796875 -0.96875 -2.078125 -0.96875q-1.140625 0 -1.9375 0.78125q-0.78125 0.765625 -0.859375 2.046875zm12.766342 4.375l0.234375 1.484375q-0.703125 0.140625 -1.265625 0.140625q-0.90625 0 -1.40625 -0.28125q-0.5 -0.296875 -0.703125 -0.75q-0.203125 -0.46875 -0.203125 -1.984375l0 -5.65625l-1.234375 0l0 -1.3125l1.234375 0l0 -2.4375l1.65625 -1.0l0 3.4375l1.6875 0l0 1.3125l-1.6875 0l0 5.75q0 0.71875 0.078125 0.921875q0.09375 0.203125 0.296875 0.328125q0.203125 0.125 0.578125 0.125q0.265625 0 0.734375 -0.078125zm8.277054 -1.671875l1.71875 0.21875q-0.40625 1.5 -1.515625 2.34375q-1.09375 0.828125 -2.8125 0.828125q-2.15625 0 -3.421875 -1.328125q-1.265625 -1.328125 -1.265625 -3.734375q0 -2.484375 1.265625 -3.859375q1.28125 -1.375 3.328125 -1.375q1.984375 0 3.234375 1.34375q1.25 1.34375 1.25 3.796875q0 0.140625 -0.015625 0.4375l-7.34375 0q0.09375 1.625 0.921875 2.484375q0.828125 0.859375 2.0625 0.859375q0.90625 0 1.546875 -0.46875q0.65625 -0.484375 1.046875 -1.546875zm-5.484375 -2.703125l5.5 0q-0.109375 -1.234375 -0.625 -1.859375q-0.796875 -0.96875 -2.078125 -0.96875q-1.140625 0 -1.9375 0.78125q-0.78125 0.765625 -0.859375 2.046875zm9.094467 5.875l0 -9.859375l1.5 0l0 1.5q0.578125 -1.046875 1.0625 -1.375q0.484375 -0.34375 1.078125 -0.34375q0.84375 0 1.71875 0.546875l-0.578125 1.546875q-0.609375 -0.359375 -1.234375 -0.359375q-0.546875 0 -0.984375 0.328125q-0.421875 0.328125 -0.609375 0.90625q-0.28125 0.890625 -0.28125 1.953125l0 5.15625l-1.671875 0zm6.228302 0l0 -9.859375l1.5 0l0 1.390625q0.453125 -0.71875 1.21875 -1.15625q0.78125 -0.453125 1.765625 -0.453125q1.09375 0 1.796875 0.453125q0.703125 0.453125 0.984375 1.28125q1.171875 -1.734375 3.046875 -1.734375q1.46875 0 2.25 0.8125q0.796875 0.8125 0.796875 2.5l0 6.765625l-1.671875 0l0 -6.203125q0 -1.0 -0.15625 -1.4375q-0.15625 -0.453125 -0.59375 -0.71875q-0.421875 -0.265625 -1.0 -0.265625q-1.03125 0 -1.71875 0.6875q-0.6875 0.6875 -0.6875 2.21875l0 5.71875l-1.671875 0l0 -6.40625q0 -1.109375 -0.40625 -1.65625q-0.40625 -0.5625 -1.34375 -0.5625q-0.703125 0 -1.3125 0.375q-0.59375 0.359375 -0.859375 1.078125q-0.265625 0.71875 -0.265625 2.0625l0 5.109375l-1.671875 0zm15.556427 -11.6875l0 -1.90625l1.671875 0l0 1.90625l-1.671875 0zm0 11.6875l0 -9.859375l1.671875 0l0 9.859375l-1.671875 0zm4.129196 0l0 -9.859375l1.5 0l0 1.40625q1.09375 -1.625 3.140625 -1.625q0.890625 0 1.640625 0.328125q0.75 0.3125 1.109375 0.84375q0.375 0.515625 0.53125 1.21875q0.09375 0.46875 0.09375 1.625l0 6.0625l-1.671875 0l0 -6.0q0 -1.015625 -0.203125 -1.515625q-0.1875 -0.515625 -0.6875 -0.8125q-0.5 -0.296875 -1.171875 -0.296875q-1.0625 0 -1.84375 0.671875q-0.765625 0.671875 -0.765625 2.578125l0 5.375l-1.671875 0zm17.125717 -3.171875l1.71875 0.21875q-0.40625 1.5 -1.515625 2.34375q-1.09375 0.828125 -2.8125 0.828125q-2.15625 0 -3.421875 -1.328125q-1.265625 -1.328125 -1.265625 -3.734375q0 -2.484375 1.265625 -3.859375q1.28125 -1.375 3.328125 -1.375q1.984375 0 3.234375 1.34375q1.25 1.34375 1.25 3.796875q0 0.140625 -0.015625 0.4375l-7.34375 0q0.09375 1.625 0.921875 2.484375q0.828125 0.859375 2.0625 0.859375q0.90625 0 1.546875 -0.46875q0.65625 -0.484375 1.046875 -1.546875zm-5.484375 -2.703125l5.5 0q-0.109375 -1.234375 -0.625 -1.859375q-0.796875 -0.96875 -2.078125 -0.96875q-1.140625 0 -1.9375 0.78125q-0.78125 0.765625 -0.859375 2.046875zm14.293396 9.65625l0 -13.640625l1.53125 0l0 1.28125q0.53125 -0.75 1.203125 -1.125q0.6875 -0.375 1.640625 -0.375q1.265625 0 2.234375 0.65625q0.96875 0.640625 1.453125 1.828125q0.5 1.1875 0.5 2.59375q0 1.515625 -0.546875 2.734375q-0.546875 1.203125 -1.578125 1.84375q-1.03125 0.640625 -2.171875 0.640625q-0.84375 0 -1.515625 -0.34375q-0.65625 -0.359375 -1.078125 -0.890625l0 4.796875l-1.671875 0zm1.515625 -8.65625q0 1.90625 0.765625 2.8125q0.78125 0.90625 1.875 0.90625q1.109375 0 1.890625 -0.9375q0.796875 -0.9375 0.796875 -2.921875q0 -1.875 -0.78125 -2.8125q-0.765625 -0.9375 -1.84375 -0.9375q-1.0625 0 -1.890625 1.0q-0.8125 1.0 -0.8125 2.890625zm8.844467 4.875l0 -9.859375l1.5 0l0 1.5q0.578125 -1.046875 1.0625 -1.375q0.484375 -0.34375 1.078125 -0.34375q0.84375 0 1.71875 0.546875l-0.578125 1.546875q-0.609375 -0.359375 -1.234375 -0.359375q-0.546875 0 -0.984375 0.328125q-0.421875 0.328125 -0.609375 0.90625q-0.28125 0.890625 -0.28125 1.953125l0 5.15625l-1.671875 0zm12.978302 -3.171875l1.71875 0.21875q-0.40625 1.5 -1.515625 2.34375q-1.09375 0.828125 -2.8125 0.828125q-2.15625 0 -3.421875 -1.328125q-1.265625 -1.328125 -1.265625 -3.734375q0 -2.484375 1.265625 -3.859375q1.28125 -1.375 3.328125 -1.375q1.984375 0 3.234375 1.34375q1.25 1.34375 1.25 3.796875q0 0.140625 -0.015625 0.4375l-7.34375 0q0.09375 1.625 0.921875 2.484375q0.828125 0.859375 2.0625 0.859375q0.90625 0 1.546875 -0.46875q0.65625 -0.484375 1.046875 -1.546875zm-5.484375 -2.703125l5.5 0q-0.109375 -1.234375 -0.625 -1.859375q-0.796875 -0.96875 -2.078125 -0.96875q-1.140625 0 -1.9375 0.78125q-0.78125 0.765625 -0.859375 2.046875zm9.094452 5.875l0 -9.859375l1.5 0l0 1.5q0.578125 -1.046875 1.0625 -1.375q0.484375 -0.34375 1.078125 -0.34375q0.84375 0 1.71875 0.546875l-0.578125 1.546875q-0.609375 -0.359375 -1.234375 -0.359375q-0.546875 0 -0.984375 0.328125q-0.421875 0.328125 -0.609375 0.90625q-0.28125 0.890625 -0.28125 1.953125l0 5.15625l-1.671875 0zm12.978302 -3.171875l1.71875 0.21875q-0.40625 1.5 -1.515625 2.34375q-1.09375 0.828125 -2.8125 0.828125q-2.15625 0 -3.421875 -1.328125q-1.265625 -1.328125 -1.265625 -3.734375q0 -2.484375 1.265625 -3.859375q1.28125 -1.375 3.328125 -1.375q1.984375 0 3.234375 1.34375q1.25 1.34375 1.25 3.796875q0 0.140625 -0.015625 0.4375l-7.34375 0q0.09375 1.625 0.921875 2.484375q0.828125 0.859375 2.0625 0.859375q0.90625 0 1.546875 -0.46875q0.65625 -0.484375 1.046875 -1.546875zm-5.484375 -2.703125l5.5 0q-0.109375 -1.234375 -0.625 -1.859375q-0.796875 -0.96875 -2.078125 -0.96875q-1.140625 0 -1.9375 0.78125q-0.78125 0.765625 -0.859375 2.046875zm15.391357 9.65625l0 -4.828125q-0.390625 0.546875 -1.09375 0.90625q-0.6875 0.359375 -1.484375 0.359375q-1.75 0 -3.015625 -1.390625q-1.265625 -1.40625 -1.265625 -3.84375q0 -1.484375 0.515625 -2.65625q0.515625 -1.1875 1.484375 -1.796875q0.984375 -0.609375 2.15625 -0.609375q1.828125 0 2.875 1.546875l0 -1.328125l1.5 0l0 13.640625l-1.671875 0zm-5.140625 -8.734375q0 1.90625 0.796875 2.859375q0.796875 0.9375 1.90625 0.9375q1.0625 0 1.828125 -0.890625q0.78125 -0.90625 0.78125 -2.765625q0 -1.953125 -0.8125 -2.953125q-0.8125 -1.0 -1.90625 -1.0q-1.09375 0 -1.84375 0.9375q-0.75 0.921875 -0.75 2.875zm8.563202 2.015625l1.65625 -0.265625q0.140625 1.0 0.765625 1.53125q0.640625 0.515625 1.78125 0.515625q1.15625 0 1.703125 -0.46875q0.5625 -0.46875 0.5625 -1.09375q0 -0.5625 -0.484375 -0.890625q-0.34375 -0.21875 -1.703125 -0.5625q-1.84375 -0.46875 -2.5625 -0.796875q-0.703125 -0.34375 -1.078125 -0.9375q-0.359375 -0.609375 -0.359375 -1.328125q0 -0.65625 0.296875 -1.21875q0.3125 -0.5625 0.828125 -0.9375q0.390625 -0.28125 1.0625 -0.484375q0.671875 -0.203125 1.4375 -0.203125q1.171875 0 2.046875 0.34375q0.875 0.328125 1.28125 0.90625q0.421875 0.5625 0.578125 1.515625l-1.625 0.21875q-0.109375 -0.75 -0.65625 -1.171875q-0.53125 -0.4375 -1.5 -0.4375q-1.15625 0 -1.640625 0.390625q-0.484375 0.375 -0.484375 0.875q0 0.328125 0.203125 0.59375q0.203125 0.265625 0.640625 0.4375q0.25 0.09375 1.46875 0.4375q1.765625 0.46875 2.46875 0.765625q0.703125 0.296875 1.09375 0.875q0.40625 0.578125 0.40625 1.4375q0 0.828125 -0.484375 1.578125q-0.484375 0.734375 -1.40625 1.140625q-0.921875 0.390625 -2.078125 0.390625q-1.921875 0 -2.9375 -0.796875q-1.0 -0.796875 -1.28125 -2.359375z" fill-rule="nonzero"></path><path fill="#38761d" d="m84.47249 718.4294l0 -9.3125l6.71875 0l0 1.109375l-5.484375 0l0 2.84375l5.140625 0l0 1.09375l-5.140625 0l0 3.171875l5.703125 0l0 1.09375l-6.9375 0zm7.9522552 0l2.46875 -3.5l-2.28125 -3.234375l1.421875 0l1.046875 1.578125q0.28125 0.453125 0.46875 0.75q0.265625 -0.421875 0.5 -0.734375l1.140625 -1.59375l1.375 0l-2.34375 3.171875l2.515625 3.5625l-1.40625 0l-1.375 -2.09375l-0.375 -0.5625l-1.765625 2.65625l-1.390625 0zm7.7421875 -5.4375l0 -1.296875l1.296875 0l0 1.296875l-1.296875 0zm0 5.4375l0 -1.296875l1.296875 0l0 1.296875l-1.296875 0zm11.593475 -3.65625l0 -1.078125l3.9375 -0.015625l0 3.453125q-0.90625 0.71875 -1.875 1.09375q-0.953125 0.359375 -1.96875 0.359375q-1.375 0 -2.5 -0.578125q-1.125 -0.59375 -1.703125 -1.703125q-0.5625 -1.109375 -0.5625 -2.484375q0 -1.359375 0.5625 -2.53125q0.578125 -1.1875 1.640625 -1.75q1.078125 -0.578125 2.453125 -0.578125q1.015625 0 1.828125 0.328125q0.8125 0.328125 1.28125 0.921875q0.46875 0.578125 0.703125 1.515625l-1.109375 0.296875q-0.203125 -0.703125 -0.515625 -1.109375q-0.3125 -0.40625 -0.890625 -0.640625q-0.578125 -0.25 -1.28125 -0.25q-0.84375 0 -1.46875 0.265625q-0.609375 0.25 -0.984375 0.671875q-0.375 0.40625 -0.59375 0.90625q-0.34375 0.875 -0.34375 1.875q0 1.25 0.421875 2.09375q0.421875 0.828125 1.234375 1.234375q0.828125 0.40625 1.75 0.40625q0.796875 0 1.5625 -0.296875q0.765625 -0.3125 1.15625 -0.671875l0 -1.734375l-2.734375 0zm5.445175 0.28125q0 -1.875 1.03125 -2.765625q0.875 -0.75 2.125 -0.75q1.390625 0 2.265625 0.90625q0.890625 0.90625 0.890625 2.515625q0 1.296875 -0.390625 2.046875q-0.390625 0.75 -1.140625 1.171875q-0.75 0.40625 -1.625 0.40625q-1.421875 0 -2.296875 -0.90625q-0.859375 -0.90625 -0.859375 -2.625zm1.171875 0q0 1.296875 0.5625 1.953125q0.5625 0.640625 1.421875 0.640625q0.84375 0 1.40625 -0.640625q0.578125 -0.65625 0.578125 -1.984375q0 -1.25 -0.578125 -1.890625q-0.5625 -0.65625 -1.40625 -0.65625q-0.859375 0 -1.421875 0.640625q-0.5625 0.640625 -0.5625 1.9375zm6.8031006 3.375l0 -9.3125l3.515625 0q0.921875 0 1.40625 0.09375q0.6875 0.109375 1.15625 0.4375q0.46875 0.3125 0.75 0.890625q0.28125 0.578125 0.28125 1.28125q0 1.1875 -0.765625 2.015625q-0.75 0.8125 -2.71875 0.8125l-2.390625 0l0 3.78125l-1.234375 0zm1.234375 -4.875l2.40625 0q1.1875 0 1.6875 -0.4375q0.515625 -0.453125 0.515625 -1.265625q0 -0.578125 -0.296875 -0.984375q-0.296875 -0.421875 -0.78125 -0.5625q-0.3125 -0.078125 -1.15625 -0.078125l-2.375 0l0 3.328125zm11.90538 4.046875q-0.625 0.53125 -1.21875 0.765625q-0.578125 0.21875 -1.25 0.21875q-1.125 0 -1.71875 -0.546875q-0.59375 -0.546875 -0.59375 -1.390625q0 -0.484375 0.21875 -0.890625q0.234375 -0.421875 0.59375 -0.671875q0.375 -0.25 0.828125 -0.375q0.328125 -0.078125 1.015625 -0.171875q1.375 -0.15625 2.03125 -0.390625q0.015625 -0.234375 0.015625 -0.296875q0 -0.703125 -0.328125 -0.984375q-0.4375 -0.390625 -1.296875 -0.390625q-0.8125 0 -1.203125 0.28125q-0.375 0.28125 -0.5625 1.0l-1.109375 -0.140625q0.140625 -0.71875 0.484375 -1.15625q0.359375 -0.453125 1.015625 -0.6875q0.671875 -0.234375 1.53125 -0.234375q0.875 0 1.40625 0.203125q0.546875 0.203125 0.796875 0.515625q0.25 0.296875 0.359375 0.765625q0.046875 0.296875 0.046875 1.0625l0 1.515625q0 1.59375 0.078125 2.015625q0.078125 0.421875 0.28125 0.8125l-1.1875 0q-0.171875 -0.359375 -0.234375 -0.828125zm-0.09375 -2.5625q-0.625 0.265625 -1.859375 0.4375q-0.703125 0.109375 -1.0 0.234375q-0.296875 0.125 -0.453125 0.375q-0.15625 0.234375 -0.15625 0.53125q0 0.453125 0.34375 0.765625q0.34375 0.296875 1.015625 0.296875q0.65625 0 1.171875 -0.28125q0.515625 -0.296875 0.765625 -0.796875q0.171875 -0.375 0.171875 -1.140625l0 -0.421875zm7.5062256 0.921875l1.125 0.140625q-0.171875 1.171875 -0.9375 1.828125q-0.765625 0.65625 -1.859375 0.65625q-1.390625 0 -2.234375 -0.90625q-0.828125 -0.90625 -0.828125 -2.59375q0 -1.09375 0.359375 -1.90625q0.359375 -0.828125 1.09375 -1.234375q0.734375 -0.40625 1.609375 -0.40625q1.09375 0 1.796875 0.5625q0.703125 0.546875 0.890625 1.5625l-1.109375 0.171875q-0.15625 -0.671875 -0.5625 -1.015625q-0.390625 -0.34375 -0.96875 -0.34375q-0.859375 0 -1.40625 0.625q-0.53125 0.609375 -0.53125 1.953125q0 1.359375 0.515625 1.984375q0.515625 0.609375 1.359375 0.609375q0.671875 0 1.125 -0.40625q0.453125 -0.421875 0.5625 -1.28125zm2.2734375 2.46875l0 -9.3125l1.140625 0l0 5.3125l2.703125 -2.734375l1.484375 0l-2.578125 2.5l2.84375 4.234375l-1.40625 0l-2.234375 -3.453125l-0.8125 0.78125l0 2.671875l-1.140625 0zm11.0546875 -0.828125q-0.625 0.53125 -1.21875 0.765625q-0.578125 0.21875 -1.25 0.21875q-1.125 0 -1.71875 -0.546875q-0.59375 -0.546875 -0.59375 -1.390625q0 -0.484375 0.21875 -0.890625q0.234375 -0.421875 0.59375 -0.671875q0.375 -0.25 0.828125 -0.375q0.328125 -0.078125 1.015625 -0.171875q1.375 -0.15625 2.03125 -0.390625q0.015625 -0.234375 0.015625 -0.296875q0 -0.703125 -0.328125 -0.984375q-0.4375 -0.390625 -1.296875 -0.390625q-0.8125 0 -1.203125 0.28125q-0.375 0.28125 -0.5625 1.0l-1.109375 -0.140625q0.140625 -0.71875 0.484375 -1.15625q0.359375 -0.453125 1.015625 -0.6875q0.671875 -0.234375 1.53125 -0.234375q0.875 0 1.40625 0.203125q0.546875 0.203125 0.796875 0.515625q0.25 0.296875 0.359375 0.765625q0.046875 0.296875 0.046875 1.0625l0 1.515625q0 1.59375 0.078125 2.015625q0.078125 0.421875 0.28125 0.8125l-1.1875 0q-0.171875 -0.359375 -0.234375 -0.828125zm-0.09375 -2.5625q-0.625 0.265625 -1.859375 0.4375q-0.703125 0.109375 -1.0 0.234375q-0.296875 0.125 -0.453125 0.375q-0.15625 0.234375 -0.15625 0.53125q0 0.453125 0.34375 0.765625q0.34375 0.296875 1.015625 0.296875q0.65625 0 1.171875 -0.28125q0.515625 -0.296875 0.765625 -0.796875q0.171875 -0.375 0.171875 -1.140625l0 -0.421875zm2.8968506 3.953125l1.125 0.15625q0.0625 0.515625 0.375 0.75q0.4375 0.328125 1.171875 0.328125q0.78125 0 1.21875 -0.328125q0.4375 -0.3125 0.578125 -0.890625q0.09375 -0.34375 0.09375 -1.453125q-0.75 0.875 -1.875 0.875q-1.390625 0 -2.15625 -1.0q-0.75 -1.0 -0.75 -2.40625q0 -0.96875 0.34375 -1.78125q0.359375 -0.8125 1.015625 -1.25q0.65625 -0.453125 1.5625 -0.453125q1.1875 0 1.96875 0.96875l0 -0.8125l1.046875 0l0 5.8125q0 1.578125 -0.328125 2.234375q-0.3125 0.65625 -1.015625 1.03125q-0.6875 0.390625 -1.703125 0.390625q-1.203125 0 -1.953125 -0.546875q-0.734375 -0.53125 -0.71875 -1.625zm0.953125 -4.046875q0 1.3125 0.515625 1.921875q0.53125 0.609375 1.328125 0.609375q0.796875 0 1.328125 -0.59375q0.53125 -0.609375 0.53125 -1.90625q0 -1.234375 -0.546875 -1.859375q-0.546875 -0.640625 -1.328125 -0.640625q-0.765625 0 -1.296875 0.625q-0.53125 0.625 -0.53125 1.84375zm11.287476 1.3125l1.1875 0.140625q-0.28125 1.046875 -1.046875 1.625q-0.75 0.5625 -1.921875 0.5625q-1.484375 0 -2.359375 -0.90625q-0.859375 -0.921875 -0.859375 -2.5625q0 -1.703125 0.875 -2.640625q0.890625 -0.9375 2.28125 -0.9375q1.359375 0 2.203125 0.921875q0.859375 0.921875 0.859375 2.578125q0 0.109375 0 0.3125l-5.03125 0q0.0625 1.109375 0.625 1.703125q0.5625 0.59375 1.40625 0.59375q0.640625 0 1.078125 -0.328125q0.453125 -0.34375 0.703125 -1.0625zm-3.75 -1.84375l3.765625 0q-0.078125 -0.859375 -0.4375 -1.28125q-0.546875 -0.65625 -1.40625 -0.65625q-0.796875 0 -1.328125 0.53125q-0.53125 0.515625 -0.59375 1.40625zm10.037338 4.578125l1.125 0.15625q0.0625 0.515625 0.375 0.75q0.4375 0.328125 1.171875 0.328125q0.78125 0 1.21875 -0.328125q0.4375 -0.3125 0.578125 -0.890625q0.09375 -0.34375 0.09375 -1.453125q-0.75 0.875 -1.875 0.875q-1.390625 0 -2.15625 -1.0q-0.75 -1.0 -0.75 -2.40625q0 -0.96875 0.34375 -1.78125q0.359375 -0.8125 1.015625 -1.25q0.65625 -0.453125 1.5625 -0.453125q1.1875 0 1.96875 0.96875l0 -0.8125l1.046875 0l0 5.8125q0 1.578125 -0.328125 2.234375q-0.3125 0.65625 -1.015625 1.03125q-0.6875 0.390625 -1.703125 0.390625q-1.203125 0 -1.953125 -0.546875q-0.734375 -0.53125 -0.71875 -1.625zm0.953125 -4.046875q0 1.3125 0.515625 1.921875q0.53125 0.609375 1.328125 0.609375q0.796875 0 1.328125 -0.59375q0.53125 -0.609375 0.53125 -1.90625q0 -1.234375 -0.546875 -1.859375q-0.546875 -0.640625 -1.328125 -0.640625q-0.765625 0 -1.296875 0.625q-0.53125 0.625 -0.53125 1.84375zm6.6624756 3.484375l0 -6.734375l1.03125 0l0 1.015625q0.390625 -0.71875 0.71875 -0.9375q0.34375 -0.234375 0.734375 -0.234375q0.578125 0 1.171875 0.359375l-0.390625 1.0625q-0.421875 -0.25 -0.828125 -0.25q-0.375 0 -0.6875 0.234375q-0.296875 0.21875 -0.421875 0.625q-0.1875 0.609375 -0.1875 1.328125l0 3.53125l-1.140625 0zm8.84462 -0.828125q-0.625 0.53125 -1.21875 0.765625q-0.578125 0.21875 -1.25 0.21875q-1.125 0 -1.71875 -0.546875q-0.59375 -0.546875 -0.59375 -1.390625q0 -0.484375 0.21875 -0.890625q0.234375 -0.421875 0.59375 -0.671875q0.375 -0.25 0.828125 -0.375q0.328125 -0.078125 1.015625 -0.171875q1.375 -0.15625 2.03125 -0.390625q0.015625 -0.234375 0.015625 -0.296875q0 -0.703125 -0.328125 -0.984375q-0.4375 -0.390625 -1.296875 -0.390625q-0.8125 0 -1.203125 0.28125q-0.375 0.28125 -0.5625 1.0l-1.109375 -0.140625q0.140625 -0.71875 0.484375 -1.15625q0.359375 -0.453125 1.015625 -0.6875q0.671875 -0.234375 1.53125 -0.234375q0.875 0 1.40625 0.203125q0.546875 0.203125 0.796875 0.515625q0.25 0.296875 0.359375 0.765625q0.046875 0.296875 0.046875 1.0625l0 1.515625q0 1.59375 0.078125 2.015625q0.078125 0.421875 0.28125 0.8125l-1.1875 0q-0.171875 -0.359375 -0.234375 -0.828125zm-0.09375 -2.5625q-0.625 0.265625 -1.859375 0.4375q-0.703125 0.109375 -1.0 0.234375q-0.296875 0.125 -0.453125 0.375q-0.15625 0.234375 -0.15625 0.53125q0 0.453125 0.34375 0.765625q0.34375 0.296875 1.015625 0.296875q0.65625 0 1.171875 -0.28125q0.515625 -0.296875 0.765625 -0.796875q0.171875 -0.375 0.171875 -1.140625l0 -0.421875zm3.1156006 5.96875l0 -9.3125l1.03125 0l0 0.875q0.375 -0.515625 0.828125 -0.765625q0.46875 -0.265625 1.140625 -0.265625q0.859375 0 1.515625 0.453125q0.65625 0.4375 0.984375 1.25q0.34375 0.796875 0.34375 1.765625q0 1.03125 -0.375 1.859375q-0.359375 0.828125 -1.078125 1.28125q-0.703125 0.4375 -1.484375 0.4375q-0.5625 0 -1.015625 -0.234375q-0.453125 -0.25 -0.75 -0.625l0 3.28125l-1.140625 0zm1.03125 -5.90625q0 1.296875 0.53125 1.921875q0.53125 0.625 1.265625 0.625q0.765625 0 1.3125 -0.640625q0.546875 -0.65625 0.546875 -2.0q0 -1.296875 -0.53125 -1.9375q-0.53125 -0.640625 -1.265625 -0.640625q-0.734375 0 -1.296875 0.6875q-0.5625 0.671875 -0.5625 1.984375zm6.3812256 3.328125l0 -9.3125l1.140625 0l0 3.34375q0.796875 -0.921875 2.015625 -0.921875q0.75 0 1.296875 0.296875q0.5625 0.296875 0.796875 0.8125q0.234375 0.515625 0.234375 1.515625l0 4.265625l-1.140625 0l0 -4.265625q0 -0.859375 -0.375 -1.25q-0.359375 -0.390625 -1.046875 -0.390625q-0.5 0 -0.953125 0.265625q-0.453125 0.25 -0.640625 0.703125q-0.1875 0.453125 -0.1875 1.25l0 3.6875l-1.140625 0zm15.490463 0l0 -0.84375q-0.640625 1.0 -1.890625 1.0q-0.796875 0 -1.484375 -0.4375q-0.671875 -0.453125 -1.046875 -1.25q-0.375 -0.796875 -0.375 -1.828125q0 -1.015625 0.34375 -1.828125q0.34375 -0.828125 1.015625 -1.265625q0.671875 -0.4375 1.5 -0.4375q0.609375 0 1.078125 0.265625q0.484375 0.25 0.78125 0.65625l0 -3.34375l1.140625 0l0 9.3125l-1.0625 0zm-3.609375 -3.359375q0 1.296875 0.53125 1.9375q0.546875 0.640625 1.296875 0.640625q0.75 0 1.265625 -0.609375q0.53125 -0.625 0.53125 -1.875q0 -1.390625 -0.53125 -2.03125q-0.53125 -0.65625 -1.3125 -0.65625q-0.765625 0 -1.28125 0.625q-0.5 0.625 -0.5 1.96875zm11.256226 1.1875l1.1875 0.140625q-0.28125 1.046875 -1.046875 1.625q-0.75 0.5625 -1.921875 0.5625q-1.484375 0 -2.359375 -0.90625q-0.859375 -0.921875 -0.859375 -2.5625q0 -1.703125 0.875 -2.640625q0.890625 -0.9375 2.28125 -0.9375q1.359375 0 2.203125 0.921875q0.859375 0.921875 0.859375 2.578125q0 0.109375 0 0.3125l-5.03125 0q0.0625 1.109375 0.625 1.703125q0.5625 0.59375 1.40625 0.59375q0.640625 0 1.078125 -0.328125q0.453125 -0.34375 0.703125 -1.0625zm-3.75 -1.84375l3.765625 0q-0.078125 -0.859375 -0.4375 -1.28125q-0.546875 -0.65625 -1.40625 -0.65625q-0.796875 0 -1.328125 0.53125q-0.53125 0.515625 -0.59375 1.40625zm6.5531006 6.59375l0 -9.3125l1.03125 0l0 0.875q0.375 -0.515625 0.828125 -0.765625q0.46875 -0.265625 1.140625 -0.265625q0.859375 0 1.515625 0.453125q0.65625 0.4375 0.984375 1.25q0.34375 0.796875 0.34375 1.765625q0 1.03125 -0.375 1.859375q-0.359375 0.828125 -1.078125 1.28125q-0.703125 0.4375 -1.484375 0.4375q-0.5625 0 -1.015625 -0.234375q-0.453125 -0.25 -0.75 -0.625l0 3.28125l-1.140625 0zm1.03125 -5.90625q0 1.296875 0.53125 1.921875q0.53125 0.625 1.265625 0.625q0.765625 0 1.3125 -0.640625q0.546875 -0.65625 0.546875 -2.0q0 -1.296875 -0.53125 -1.9375q-0.53125 -0.640625 -1.265625 -0.640625q-0.734375 0 -1.296875 0.6875q-0.5625 0.671875 -0.5625 1.984375zm10.990601 1.15625l1.1875 0.140625q-0.28125 1.046875 -1.046875 1.625q-0.75 0.5625 -1.921875 0.5625q-1.484375 0 -2.359375 -0.90625q-0.859375 -0.921875 -0.859375 -2.5625q0 -1.703125 0.875 -2.640625q0.890625 -0.9375 2.28125 -0.9375q1.359375 0 2.203125 0.921875q0.859375 0.921875 0.859375 2.578125q0 0.109375 0 0.3125l-5.03125 0q0.0625 1.109375 0.625 1.703125q0.5625 0.59375 1.40625 0.59375q0.640625 0 1.078125 -0.328125q0.453125 -0.34375 0.703125 -1.0625zm-3.75 -1.84375l3.765625 0q-0.078125 -0.859375 -0.4375 -1.28125q-0.546875 -0.65625 -1.40625 -0.65625q-0.796875 0 -1.328125 0.53125q-0.53125 0.515625 -0.59375 1.40625zm6.5531006 4.015625l0 -6.734375l1.03125 0l0 0.953125q0.734375 -1.109375 2.140625 -1.109375q0.609375 0 1.109375 0.21875q0.515625 0.21875 0.765625 0.578125q0.265625 0.34375 0.359375 0.84375q0.0625 0.3125 0.0625 1.109375l0 4.140625l-1.140625 0l0 -4.09375q0 -0.703125 -0.140625 -1.046875q-0.125 -0.34375 -0.46875 -0.546875q-0.328125 -0.21875 -0.78125 -0.21875q-0.734375 0 -1.265625 0.46875q-0.53125 0.453125 -0.53125 1.75l0 3.6875l-1.140625 0zm11.78746 0l0 -0.84375q-0.640625 1.0 -1.890625 1.0q-0.796875 0 -1.484375 -0.4375q-0.67185974 -0.453125 -1.0468597 -1.25q-0.375 -0.796875 -0.375 -1.828125q0 -1.015625 0.34375 -1.828125q0.34375 -0.828125 1.0156097 -1.265625q0.671875 -0.4375 1.5 -0.4375q0.609375 0 1.078125 0.265625q0.484375 0.25 0.78125 0.65625l0 -3.34375l1.140625 0l0 9.3125l-1.0625 0zm-3.609375 -3.359375q0 1.296875 0.53125 1.9375q0.546875 0.640625 1.296875 0.640625q0.75 0 1.265625 -0.609375q0.53125 -0.625 0.53125 -1.875q0 -1.390625 -0.53125 -2.03125q-0.53125 -0.65625 -1.3125 -0.65625q-0.765625 0 -1.28125 0.625q-0.5 0.625 -0.5 1.96875zm6.1937256 1.34375l1.125 -0.171875q0.09375 0.671875 0.53125 1.046875q0.4375 0.359375 1.21875 0.359375q0.78125 0 1.15625 -0.3125q0.390625 -0.328125 0.390625 -0.765625q0 -0.390625 -0.34375 -0.609375q-0.234375 -0.15625 -1.171875 -0.390625q-1.25 -0.3125 -1.734375 -0.546875q-0.484375 -0.234375 -0.734375 -0.640625q-0.25 -0.40625 -0.25 -0.90625q0 -0.453125 0.203125 -0.828125q0.203125 -0.390625 0.5625 -0.640625q0.265625 -0.203125 0.71875 -0.328125q0.46875 -0.140625 1.0 -0.140625q0.78125 0 1.375 0.234375q0.609375 0.21875 0.890625 0.609375q0.296875 0.390625 0.40625 1.046875l-1.125 0.15625q-0.078125 -0.53125 -0.4375 -0.8125q-0.359375 -0.296875 -1.03125 -0.296875q-0.78125 0 -1.125 0.265625q-0.34375 0.25 -0.34375 0.609375q0 0.21875 0.140625 0.390625q0.140625 0.1875 0.4375 0.3125q0.171875 0.0625 1.015625 0.28125q1.21875 0.328125 1.6875 0.53125q0.484375 0.203125 0.75 0.609375q0.28125 0.390625 0.28125 0.96875q0 0.578125 -0.34375 1.078125q-0.328125 0.5 -0.953125 0.78125q-0.625 0.28125 -1.421875 0.28125q-1.3125 0 -2.0 -0.546875q-0.6875 -0.546875 -0.875 -1.625zm10.398315 -1.359375q0 -1.875 1.03125 -2.765625q0.875 -0.75 2.125 -0.75q1.390625 0 2.265625 0.90625q0.890625 0.90625 0.890625 2.515625q0 1.296875 -0.390625 2.046875q-0.390625 0.75 -1.140625 1.171875q-0.75 0.40625 -1.625 0.40625q-1.421875 0 -2.296875 -0.90625q-0.859375 -0.90625 -0.859375 -2.625zm1.171875 0q0 1.296875 0.5625 1.953125q0.5625 0.640625 1.421875 0.640625q0.84375 0 1.40625 -0.640625q0.578125 -0.65625 0.578125 -1.984375q0 -1.25 -0.578125 -1.890625q-0.5625 -0.65625 -1.40625 -0.65625q-0.859375 0 -1.421875 0.640625q-0.5625 0.640625 -0.5625 1.9375zm6.6624756 3.375l0 -6.734375l1.03125 0l0 0.953125q0.734375 -1.109375 2.140625 -1.109375q0.609375 0 1.109375 0.21875q0.515625 0.21875 0.765625 0.578125q0.265625 0.34375 0.359375 0.84375q0.0625 0.3125 0.0625 1.109375l0 4.140625l-1.140625 0l0 -4.09375q0 -0.703125 -0.140625 -1.046875q-0.125 -0.34375 -0.46875 -0.546875q-0.328125 -0.21875 -0.78125 -0.21875q-0.734375 0 -1.265625 0.46875q-0.53125 0.453125 -0.53125 1.75l0 3.6875l-1.140625 0zm15.490448 0l0 -0.84375q-0.640625 1.0 -1.890625 1.0q-0.796875 0 -1.484375 -0.4375q-0.671875 -0.453125 -1.046875 -1.25q-0.375 -0.796875 -0.375 -1.828125q0 -1.015625 0.34375 -1.828125q0.34375 -0.828125 1.015625 -1.265625q0.671875 -0.4375 1.5 -0.4375q0.609375 0 1.078125 0.265625q0.484375 0.25 0.78125 0.65625l0 -3.34375l1.140625 0l0 9.3125l-1.0625 0zm-3.609375 -3.359375q0 1.296875 0.53125 1.9375q0.546875 0.640625 1.296875 0.640625q0.75 0 1.265625 -0.609375q0.53125 -0.625 0.53125 -1.875q0 -1.390625 -0.53125 -2.03125q-0.53125 -0.65625 -1.3125 -0.65625q-0.765625 0 -1.28125 0.625q-0.5 0.625 -0.5 1.96875zm11.256226 1.1875l1.1875 0.140625q-0.28125 1.046875 -1.046875 1.625q-0.75 0.5625 -1.921875 0.5625q-1.484375 0 -2.359375 -0.90625q-0.859375 -0.921875 -0.859375 -2.5625q0 -1.703125 0.875 -2.640625q0.890625 -0.9375 2.28125 -0.9375q1.359375 0 2.203125 0.921875q0.859375 0.921875 0.859375 2.578125q0 0.109375 0 0.3125l-5.03125 0q0.0625 1.109375 0.625 1.703125q0.5625 0.59375 1.40625 0.59375q0.640625 0 1.078125 -0.328125q0.453125 -0.34375 0.703125 -1.0625zm-3.75 -1.84375l3.765625 0q-0.078125 -0.859375 -0.4375 -1.28125q-0.546875 -0.65625 -1.40625 -0.65625q-0.796875 0 -1.328125 0.53125q-0.53125 0.515625 -0.59375 1.40625zm6.5531006 6.59375l0 -9.3125l1.03125 0l0 0.875q0.375 -0.515625 0.828125 -0.765625q0.46875 -0.265625 1.140625 -0.265625q0.859375 0 1.515625 0.453125q0.65625 0.4375 0.984375 1.25q0.34375 0.796875 0.34375 1.765625q0 1.03125 -0.375 1.859375q-0.359375 0.828125 -1.078125 1.28125q-0.703125 0.4375 -1.484375 0.4375q-0.5625 0 -1.015625 -0.234375q-0.453125 -0.25 -0.75 -0.625l0 3.28125l-1.140625 0zm1.03125 -5.90625q0 1.296875 0.53125 1.921875q0.53125 0.625 1.265625 0.625q0.765625 0 1.3125 -0.640625q0.546875 -0.65625 0.546875 -2.0q0 -1.296875 -0.53125 -1.9375q-0.53125 -0.640625 -1.265625 -0.640625q-0.734375 0 -1.296875 0.6875q-0.5625 0.671875 -0.5625 1.984375zm6.3656006 3.328125l0 -6.734375l1.03125 0l0 1.015625q0.390625 -0.71875 0.71875 -0.9375q0.34375 -0.234375 0.734375 -0.234375q0.578125 0 1.171875 0.359375l-0.390625 1.0625q-0.421875 -0.25 -0.828125 -0.25q-0.375 0 -0.6875 0.234375q-0.296875 0.21875 -0.421875 0.625q-0.1875 0.609375 -0.1875 1.328125l0 3.53125l-1.140625 0zm9.063385 -2.171875l1.1875 0.140625q-0.28125 1.046875 -1.046875 1.625q-0.75 0.5625 -1.921875 0.5625q-1.484375 0 -2.359375 -0.90625q-0.859375 -0.921875 -0.859375 -2.5625q0 -1.703125 0.875 -2.640625q0.890625 -0.9375 2.28125 -0.9375q1.359375 0 2.203125 0.921875q0.859375 0.921875 0.859375 2.578125q0 0.109375 0 0.3125l-5.03125 0q0.0625 1.109375 0.625 1.703125q0.5625 0.59375 1.40625 0.59375q0.640625 0 1.078125 -0.328125q0.453125 -0.34375 0.703125 -1.0625zm-3.75 -1.84375l3.765625 0q-0.078125 -0.859375 -0.4375 -1.28125q-0.546875 -0.65625 -1.40625 -0.65625q-0.796875 0 -1.328125 0.53125q-0.53125 0.515625 -0.59375 1.40625zm6.0999756 2.0l1.125 -0.171875q0.09375 0.671875 0.53125 1.046875q0.4375 0.359375 1.21875 0.359375q0.78125 0 1.15625 -0.3125q0.390625 -0.328125 0.390625 -0.765625q0 -0.390625 -0.34375 -0.609375q-0.234375 -0.15625 -1.171875 -0.390625q-1.25 -0.3125 -1.734375 -0.546875q-0.484375 -0.234375 -0.734375 -0.640625q-0.25 -0.40625 -0.25 -0.90625q0 -0.453125 0.203125 -0.828125q0.203125 -0.390625 0.5625 -0.640625q0.265625 -0.203125 0.71875 -0.328125q0.46875 -0.140625 1.0 -0.140625q0.78125 0 1.375 0.234375q0.609375 0.21875 0.890625 0.609375q0.296875 0.390625 0.40625 1.046875l-1.125 0.15625q-0.078125 -0.53125 -0.4375 -0.8125q-0.359375 -0.296875 -1.03125 -0.296875q-0.78125 0 -1.125 0.265625q-0.34375 0.25 -0.34375 0.609375q0 0.21875 0.140625 0.390625q0.140625 0.1875 0.4375 0.3125q0.171875 0.0625 1.015625 0.28125q1.21875 0.328125 1.6875 0.53125q0.484375 0.203125 0.75 0.609375q0.28125 0.390625 0.28125 0.96875q0 0.578125 -0.34375 1.078125q-0.328125 0.5 -0.953125 0.78125q-0.625 0.28125 -1.421875 0.28125q-1.3125 0 -2.0 -0.546875q-0.6875 -0.546875 -0.875 -1.625zm6.6953125 -1.359375q0 -1.875 1.03125 -2.765625q0.875 -0.75 2.125 -0.75q1.390625 0 2.265625 0.90625q0.890625 0.90625 0.890625 2.515625q0 1.296875 -0.390625 2.046875q-0.390625 0.75 -1.140625 1.171875q-0.75 0.40625 -1.625 0.40625q-1.421875 0 -2.296875 -0.90625q-0.859375 -0.90625 -0.859375 -2.625zm1.171875 0q0 1.296875 0.5625 1.953125q0.5625 0.640625 1.421875 0.640625q0.84375 0 1.40625 -0.640625q0.578125 -0.65625 0.578125 -1.984375q0 -1.25 -0.578125 -1.890625q-0.5625 -0.65625 -1.40625 -0.65625q-0.859375 0 -1.421875 0.640625q-0.5625 0.640625 -0.5625 1.9375zm6.6312256 3.375l0 -9.3125l1.140625 0l0 9.3125l-1.140625 0zm4.86734 0l-2.5625 -6.734375l1.203125 0l1.4375 4.03125q0.234375 0.65625 0.4375 1.359375q0.15625 -0.53125 0.421875 -1.28125l1.5 -4.109375l1.171875 0l-2.546875 6.734375l-1.0625 0zm9.3984375 -2.171875l1.1875 0.140625q-0.28125 1.046875 -1.046875 1.625q-0.75 0.5625 -1.921875 0.5625q-1.484375 0 -2.359375 -0.90625q-0.859375 -0.921875 -0.859375 -2.5625q0 -1.703125 0.875 -2.640625q0.890625 -0.9375 2.28125 -0.9375q1.359375 0 2.203125 0.921875q0.859375 0.921875 0.859375 2.578125q0 0.109375 0 0.3125l-5.03125 0q0.0625 1.109375 0.625 1.703125q0.5625 0.59375 1.40625 0.59375q0.640625 0 1.078125 -0.328125q0.453125 -0.34375 0.703125 -1.0625zm-3.75 -1.84375l3.765625 0q-0.078125 -0.859375 -0.4375 -1.28125q-0.546875 -0.65625 -1.40625 -0.65625q-0.796875 0 -1.328125 0.53125q-0.53125 0.515625 -0.59375 1.40625z" fill-rule="nonzero"></path><path fill="#38761d" d="m201.68762 731.0544q0 -1.875 1.03125 -2.765625q0.875 -0.75 2.125 -0.75q1.390625 0 2.265625 0.90625q0.890625 0.90625 0.890625 2.515625q0 1.296875 -0.390625 2.046875q-0.390625 0.75 -1.140625 1.171875q-0.75 0.40625 -1.625 0.40625q-1.421875 0 -2.296875 -0.90625q-0.859375 -0.90625 -0.859375 -2.625zm1.171875 0q0 1.296875 0.5625 1.953125q0.5625 0.640625 1.421875 0.640625q0.84375 0 1.40625 -0.640625q0.578125 -0.65625 0.578125 -1.984375q0 -1.25 -0.578125 -1.890625q-0.5625 -0.65625 -1.40625 -0.65625q-0.859375 0 -1.421875 0.640625q-0.5625 0.640625 -0.5625 1.9375zm11.084351 3.375l0 -0.984375q-0.796875 1.140625 -2.140625 1.140625q-0.59375 0 -1.125 -0.234375q-0.515625 -0.234375 -0.765625 -0.578125q-0.25 -0.34375 -0.34375 -0.84375q-0.078125 -0.328125 -0.078125 -1.0625l0 -4.171875l1.140625 0l0 3.734375q0 0.890625 0.078125 1.203125q0.109375 0.453125 0.453125 0.71875q0.34375 0.25 0.859375 0.25q0.515625 0 0.96875 -0.265625q0.453125 -0.265625 0.640625 -0.71875q0.1875 -0.453125 0.1875 -1.3125l0 -3.609375l1.140625 0l0 6.734375l-1.015625 0zm5.4906006 -1.015625l0.15625 1.0q-0.484375 0.109375 -0.859375 0.109375q-0.625 0 -0.96875 -0.203125q-0.34375 -0.203125 -0.484375 -0.515625q-0.140625 -0.328125 -0.140625 -1.34375l0 -3.890625l-0.828125 0l0 -0.875l0.828125 0l0 -1.671875l1.140625 -0.6875l0 2.359375l1.15625 0l0 0.875l-1.15625 0l0 3.953125q0 0.484375 0.0625 0.625q0.0625 0.140625 0.1875 0.21875q0.140625 0.078125 0.390625 0.078125q0.203125 0 0.515625 -0.03125zm1.2029877 3.59375l0 -9.3125l1.03125 0l0 0.875q0.375 -0.515625 0.828125 -0.765625q0.46875 -0.265625 1.140625 -0.265625q0.859375 0 1.515625 0.453125q0.65625 0.4375 0.984375 1.25q0.34375 0.796875 0.34375 1.765625q0 1.03125 -0.375 1.859375q-0.359375 0.828125 -1.078125 1.28125q-0.703125 0.4375 -1.484375 0.4375q-0.5625 0 -1.015625 -0.234375q-0.453125 -0.25 -0.75 -0.625l0 3.28125l-1.140625 0zm1.03125 -5.90625q0 1.296875 0.53125 1.921875q0.53125 0.625 1.265625 0.625q0.765625 0 1.3125 -0.640625q0.546875 -0.65625 0.546875 -2.0q0 -1.296875 -0.53125 -1.9375q-0.53125 -0.640625 -1.265625 -0.640625q-0.734375 0 -1.296875 0.6875q-0.5625 0.671875 -0.5625 1.984375zm10.803101 3.328125l0 -0.984375q-0.796875 1.140625 -2.140625 1.140625q-0.59375 0 -1.125 -0.234375q-0.515625 -0.234375 -0.765625 -0.578125q-0.25 -0.34375 -0.34375 -0.84375q-0.078125 -0.328125 -0.078125 -1.0625l0 -4.171875l1.140625 0l0 3.734375q0 0.890625 0.078125 1.203125q0.109375 0.453125 0.453125 0.71875q0.34375 0.25 0.859375 0.25q0.515625 0 0.96875 -0.265625q0.453125 -0.265625 0.640625 -0.71875q0.1875 -0.453125 0.1875 -1.3125l0 -3.609375l1.140625 0l0 6.734375l-1.015625 0zm5.4906006 -1.015625l0.15625 1.0q-0.484375 0.109375 -0.859375 0.109375q-0.625 0 -0.96875 -0.203125q-0.34375 -0.203125 -0.484375 -0.515625q-0.140625 -0.328125 -0.140625 -1.34375l0 -3.890625l-0.828125 0l0 -0.875l0.828125 0l0 -1.671875l1.140625 -0.6875l0 2.359375l1.15625 0l0 0.875l-1.15625 0l0 3.953125q0 0.484375 0.0625 0.625q0.0625 0.140625 0.1875 0.21875q0.140625 0.078125 0.390625 0.078125q0.203125 0 0.515625 -0.03125z" fill-rule="nonzero"></path><path fill="#000000" fill-opacity="0.0" d="m220.68619 665.91284l-0.90812683 18.606323" fill-rule="nonzero"></path><path stroke="#d9ead3" stroke-width="1.0" stroke-linejoin="round" stroke-linecap="butt" d="m220.68619 665.91284l-0.6156311 12.613464" fill-rule="evenodd"></path><path fill="#d9ead3" stroke="#d9ead3" stroke-width="1.0" stroke-linecap="butt" d="m218.42078 678.44574l1.4285431 4.61322l1.8710022 -4.4521484z" fill-rule="evenodd"></path><path fill="#b4a7d6" d="m19.824146 886.3208l399.9055 0l0 97.63782l-399.9055 0z" fill-rule="nonzero"></path><path stroke="#8e7cc3" stroke-width="1.0" stroke-linejoin="round" stroke-linecap="butt" d="m19.824146 886.3208l399.9055 0l0 97.63782l-399.9055 0z" fill-rule="nonzero"></path><path fill="#351c75" d="m141.30716 913.2408l0 -13.59375l10.09375 0l0 2.296875l-7.34375 0l0 3.015625l6.828125 0l0 2.28125l-6.828125 0l0 3.703125l7.609375 0l0 2.296875l-10.359375 0zm11.177948 0l3.5625 -5.078125l-3.40625 -4.78125l3.171875 0l1.75 2.71875l1.828125 -2.71875l3.0625 0l-3.328125 4.671875l3.640625 5.1875l-3.203125 0l-2.0 -3.046875l-2.03125 3.046875l-3.046875 0zm17.328842 -3.140625l2.609375 0.4375q-0.5 1.4375 -1.59375 2.1875q-1.078125 0.734375 -2.703125 0.734375q-2.5625 0 -3.796875 -1.671875q-0.96875 -1.34375 -0.96875 -3.40625q0 -2.4375 1.265625 -3.828125q1.28125 -1.390625 3.25 -1.390625q2.1875 0 3.453125 1.453125q1.28125 1.453125 1.234375 4.453125l-6.53125 0q0.015625 1.15625 0.625 1.8125q0.609375 0.640625 1.5 0.640625q0.609375 0 1.03125 -0.328125q0.421875 -0.34375 0.625 -1.09375zm0.15625 -2.625q-0.03125 -1.140625 -0.59375 -1.71875q-0.546875 -0.59375 -1.34375 -0.59375q-0.859375 0 -1.40625 0.625q-0.5625 0.609375 -0.546875 1.6875l3.890625 0zm13.110092 -1.171875l-2.5625 0.46875q-0.140625 -0.78125 -0.59375 -1.171875q-0.453125 -0.390625 -1.1875 -0.390625q-0.984375 0 -1.5625 0.671875q-0.578125 0.671875 -0.578125 2.25q0 1.765625 0.578125 2.484375q0.59375 0.71875 1.59375 0.71875q0.75 0 1.21875 -0.421875q0.46875 -0.421875 0.671875 -1.453125l2.546875 0.4375q-0.390625 1.765625 -1.53125 2.671875q-1.125 0.890625 -3.03125 0.890625q-2.15625 0 -3.453125 -1.359375q-1.28125 -1.359375 -1.28125 -3.78125q0 -2.4375 1.296875 -3.796875q1.296875 -1.359375 3.484375 -1.359375q1.796875 0 2.859375 0.78125q1.0625 0.765625 1.53125 2.359375zm8.266342 6.9375l0 -1.46875q-0.53125 0.78125 -1.40625 1.234375q-0.875 0.453125 -1.859375 0.453125q-0.984375 0 -1.78125 -0.4375q-0.78125 -0.4375 -1.140625 -1.21875q-0.34375 -0.796875 -0.34375 -2.1875l0 -6.234375l2.609375 0l0 4.53125q0 2.078125 0.140625 2.546875q0.140625 0.46875 0.515625 0.75q0.390625 0.265625 0.96875 0.265625q0.671875 0 1.203125 -0.359375q0.53125 -0.375 0.71875 -0.90625q0.1875 -0.546875 0.1875 -2.671875l0 -4.15625l2.609375 0l0 9.859375l-2.421875 0zm9.427231 -9.859375l0 2.078125l-1.78125 0l0 3.984375q0 1.203125 0.046875 1.40625q0.0625 0.1875 0.234375 0.328125q0.1875 0.125 0.453125 0.125q0.359375 0 1.046875 -0.25l0.21875 2.015625q-0.90625 0.390625 -2.0625 0.390625q-0.703125 0 -1.265625 -0.234375q-0.5625 -0.234375 -0.828125 -0.609375q-0.265625 -0.375 -0.375 -1.015625q-0.078125 -0.453125 -0.078125 -1.84375l0 -4.296875l-1.203125 0l0 -2.078125l1.203125 0l0 -1.953125l2.609375 -1.515625l0 3.46875l1.78125 0zm7.400177 6.71875l2.609375 0.4375q-0.5 1.4375 -1.59375 2.1875q-1.078125 0.734375 -2.703125 0.734375q-2.5625 0 -3.796875 -1.671875q-0.96875 -1.34375 -0.96875 -3.40625q0 -2.4375 1.265625 -3.828125q1.28125 -1.390625 3.25 -1.390625q2.1875 0 3.453125 1.453125q1.28125 1.453125 1.234375 4.453125l-6.53125 0q0.015625 1.15625 0.625 1.8125q0.609375 0.640625 1.5 0.640625q0.609375 0 1.03125 -0.328125q0.421875 -0.34375 0.625 -1.09375zm0.15625 -2.625q-0.03125 -1.140625 -0.59375 -1.71875q-0.546875 -0.59375 -1.34375 -0.59375q-0.859375 0 -1.40625 0.625q-0.5625 0.609375 -0.546875 1.6875l3.890625 0zm14.027771 9.765625l-1.796875 0q-1.40625 -2.140625 -2.15625 -4.453125q-0.734375 -2.3125 -0.734375 -4.46875q0 -2.6875 0.90625 -5.078125q0.796875 -2.078125 2.03125 -3.828125l1.78125 0q-1.28125 2.8125 -1.765625 4.78125q-0.46875 1.96875 -0.46875 4.171875q0 1.53125 0.28125 3.125q0.28125 1.59375 0.78125 3.03125q0.328125 0.953125 1.140625 2.71875zm1.900177 -4.0l0 -13.59375l4.421875 0q2.5 0 3.265625 0.203125q1.15625 0.296875 1.9375 1.328125q0.796875 1.015625 0.796875 2.640625q0 1.25 -0.453125 2.109375q-0.453125 0.859375 -1.15625 1.34375q-0.703125 0.484375 -1.421875 0.640625q-0.984375 0.203125 -2.84375 0.203125l-1.796875 0l0 5.125l-2.75 0zm2.75 -11.296875l0 3.859375l1.5 0q1.625 0 2.171875 -0.21875q0.546875 -0.21875 0.859375 -0.671875q0.3125 -0.453125 0.3125 -1.046875q0 -0.75 -0.4375 -1.234375q-0.4375 -0.484375 -1.09375 -0.59375q-0.5 -0.09375 -1.984375 -0.09375l-1.328125 0zm12.287323 -2.296875l0 5.0q1.25 -1.484375 3.015625 -1.484375q0.890625 0 1.609375 0.34375q0.734375 0.328125 1.09375 0.84375q0.375 0.515625 0.5 1.15625q0.140625 0.625 0.140625 1.953125l0 5.78125l-2.609375 0l0 -5.203125q0 -1.546875 -0.15625 -1.96875q-0.140625 -0.421875 -0.515625 -0.65625q-0.375 -0.25 -0.9375 -0.25q-0.65625 0 -1.171875 0.3125q-0.5 0.3125 -0.734375 0.953125q-0.234375 0.640625 -0.234375 1.875l0 4.9375l-2.609375 0l0 -13.59375l2.609375 0zm10.739731 6.75l-2.359375 -0.4375q0.390625 -1.421875 1.359375 -2.109375q0.984375 -0.6875 2.90625 -0.6875q1.734375 0 2.59375 0.421875q0.859375 0.40625 1.203125 1.046875q0.34376526 0.625 0.34376526 2.328125l-0.03125 3.046875q0 1.296875 0.125 1.921875q0.125 0.609375 0.46875 1.3125l-2.5781403 0q-0.09375 -0.265625 -0.25 -0.765625q-0.0625 -0.234375 -0.09375 -0.3125q-0.65625 0.65625 -1.421875 0.984375q-0.765625 0.3125 -1.625 0.3125q-1.515625 0 -2.40625 -0.8125q-0.875 -0.828125 -0.875 -2.09375q0 -0.84375 0.390625 -1.484375q0.40625 -0.65625 1.125 -1.0q0.71875 -0.359375 2.078125 -0.625q1.828125 -0.328125 2.53125 -0.625l0 -0.265625q0 -0.75 -0.375 -1.0625q-0.359375 -0.328125 -1.390625 -0.328125q-0.703125 0 -1.09375 0.28125q-0.390625 0.265625 -0.625 0.953125zm3.484375 2.109375q-0.5 0.171875 -1.59375 0.40625q-1.078125 0.234375 -1.40625 0.453125q-0.515625 0.359375 -0.515625 0.921875q0 0.546875 0.40625 0.953125q0.40625 0.390625 1.046875 0.390625q0.703125 0 1.34375 -0.46875q0.46875 -0.359375 0.625 -0.859375q0.09375 -0.34375 0.09375 -1.28125l0 -0.515625zm4.031967 1.921875l2.609375 -0.390625q0.171875 0.75 0.671875 1.15625q0.515625 0.390625 1.4375 0.390625q1.0 0 1.515625 -0.375q0.34375 -0.265625 0.34375 -0.703125q0 -0.296875 -0.1875 -0.484375q-0.1875 -0.1875 -0.875 -0.34375q-3.140625 -0.703125 -4.0 -1.265625q-1.15625 -0.796875 -1.15625 -2.21875q0 -1.28125 1.0 -2.15625q1.015625 -0.875 3.140625 -0.875q2.03125 0 3.0 0.65625q0.984375 0.65625 1.359375 1.953125l-2.453125 0.453125q-0.15625 -0.578125 -0.609375 -0.875q-0.4375 -0.3125 -1.25 -0.3125q-1.03125 0 -1.46875 0.296875q-0.296875 0.203125 -0.296875 0.515625q0 0.28125 0.25 0.484375q0.359375 0.25 2.4375 0.734375q2.078125 0.46875 2.90625 1.15625q0.828125 0.6875 0.828125 1.9375q0 1.359375 -1.140625 2.328125q-1.125 0.96875 -3.34375 0.96875q-2.015625 0 -3.1875 -0.8125q-1.171875 -0.8125 -1.53125 -2.21875zm16.985107 -0.328125l2.609375 0.4375q-0.5 1.4375 -1.59375 2.1875q-1.078125 0.734375 -2.703125 0.734375q-2.5625 0 -3.796875 -1.671875q-0.96875 -1.34375 -0.96875 -3.40625q0 -2.4375 1.265625 -3.828125q1.28125 -1.390625 3.25 -1.390625q2.1875 0 3.453125 1.453125q1.28125 1.453125 1.234375 4.453125l-6.53125 0q0.015625 1.15625 0.625 1.8125q0.609375 0.640625 1.5 0.640625q0.609375 0 1.03125 -0.328125q0.421875 -0.34375 0.625 -1.09375zm0.15625 -2.625q-0.03125 -1.140625 -0.59375 -1.71875q-0.546875 -0.59375 -1.34375 -0.59375q-0.859375 0 -1.40625 0.625q-0.5625 0.609375 -0.546875 1.6875l3.890625 0zm9.059021 2.15625l2.515625 -0.3125q0.125 0.96875 0.65625 1.484375q0.53125 0.5 1.28125 0.5q0.796875 0 1.34375 -0.609375q0.5625 -0.609375 0.5625 -1.640625q0 -0.984375 -0.53125 -1.5625q-0.53125 -0.578125 -1.28125 -0.578125q-0.5 0 -1.203125 0.203125l0.28125 -2.125q1.0625 0.015625 1.609375 -0.46875q0.5625 -0.484375 0.5625 -1.296875q0 -0.6875 -0.40625 -1.09375q-0.40625 -0.40625 -1.078125 -0.40625q-0.671875 0 -1.140625 0.46875q-0.46875 0.46875 -0.578125 1.359375l-2.40625 -0.421875q0.25 -1.234375 0.75 -1.96875q0.515625 -0.734375 1.421875 -1.15625q0.90625 -0.421875 2.03125 -0.421875q1.90625 0 3.078125 1.21875q0.953125 1.0 0.953125 2.265625q0 1.796875 -1.953125 2.859375q1.15625 0.25 1.859375 1.125q0.703125 0.875 0.703125 2.109375q0 1.78125 -1.3125 3.046875q-1.296875 1.265625 -3.25 1.265625q-1.84375 0 -3.0625 -1.0625q-1.21875 -1.0625 -1.40625 -2.78125zm10.297607 7.609375q0.765625 -1.65625 1.078125 -2.546875q0.328125 -0.875 0.59375 -2.015625q0.265625 -1.15625 0.390625 -2.1875q0.140625 -1.03125 0.140625 -2.125q0 -2.203125 -0.484375 -4.171875q-0.46875 -1.96875 -1.734375 -4.78125l1.765625 0q1.40625 1.984375 2.171875 4.234375q0.78125 2.234375 0.78125 4.53125q0 1.9375 -0.609375 4.15625q-0.703125 2.484375 -2.296875 4.90625l-1.796875 0z" fill-rule="nonzero"></path><path fill="#d9d2e9" d="m19.824146 931.082l399.9055 0l0 52.881897l-399.9055 0z" fill-rule="nonzero"></path><path fill="#351c75" d="m96.33105 956.4429l0 -13.59375l6.03125 0q1.8125 0 2.75 0.359375q0.953125 0.359375 1.515625 1.296875q0.5625 0.921875 0.5625 2.046875q0 1.453125 -0.9375 2.453125q-0.921875 0.984375 -2.890625 1.25q0.71875 0.34375 1.09375 0.671875q0.78125 0.734375 1.484375 1.8125l2.375 3.703125l-2.265625 0l-1.796875 -2.828125q-0.796875 -1.21875 -1.3125 -1.875q-0.5 -0.65625 -0.90625 -0.90625q-0.40625 -0.265625 -0.8125 -0.359375q-0.3125 -0.078125 -1.015625 -0.078125l-2.078125 0l0 6.046875l-1.796875 0zm1.796875 -7.59375l3.859375 0q1.234375 0 1.921875 -0.25q0.703125 -0.265625 1.0625 -0.828125q0.375 -0.5625 0.375 -1.21875q0 -0.96875 -0.703125 -1.578125q-0.703125 -0.625 -2.21875 -0.625l-4.296875 0l0 4.5zm17.879196 7.59375l0 -1.453125q-1.140625 1.671875 -3.125 1.671875q-0.859375 0 -1.625 -0.328125q-0.75 -0.34375 -1.125 -0.84375q-0.359375 -0.5 -0.515625 -1.234375q-0.09375 -0.5 -0.09375 -1.5625l0 -6.109375l1.671875 0l0 5.46875q0 1.3125 0.09375 1.765625q0.15625 0.65625 0.671875 1.03125q0.515625 0.375 1.265625 0.375q0.75 0 1.40625 -0.375q0.65625 -0.390625 0.921875 -1.046875q0.28125 -0.671875 0.28125 -1.9375l0 -5.28125l1.671875 0l0 9.859375l-1.5 0zm3.9225922 0l0 -9.859375l1.5 0l0 1.40625q1.09375 -1.625 3.140625 -1.625q0.890625 0 1.640625 0.328125q0.75 0.3125 1.109375 0.84375q0.375 0.515625 0.53125 1.21875q0.09375 0.46875 0.09375 1.625l0 6.0625l-1.671875 0l0 -6.0q0 -1.015625 -0.203125 -1.515625q-0.1875 -0.515625 -0.6875 -0.8125q-0.5 -0.296875 -1.171875 -0.296875q-1.0625 0 -1.84375 0.671875q-0.765625 0.671875 -0.765625 2.578125l0 5.375l-1.671875 0zm15.715263 0l0 -13.59375l2.71875 0l3.21875 9.625q0.4375 1.34375 0.640625 2.015625q0.234375 -0.75 0.734375 -2.1875l3.25 -9.453125l2.421875 0l0 13.59375l-1.734375 0l0 -11.390625l-3.953125 11.390625l-1.625 0l-3.9375 -11.578125l0 11.578125l-1.734375 0zm21.822052 -1.21875q-0.9375 0.796875 -1.796875 1.125q-0.859375 0.3125 -1.84375 0.3125q-1.609375 0 -2.484375 -0.78125q-0.875 -0.796875 -0.875 -2.03125q0 -0.734375 0.328125 -1.328125q0.328125 -0.59375 0.859375 -0.953125q0.53125 -0.359375 1.203125 -0.546875q0.5 -0.140625 1.484375 -0.25q2.03125 -0.25 2.984375 -0.578125q0 -0.34375 0 -0.4375q0 -1.015625 -0.46875 -1.4375q-0.640625 -0.5625 -1.90625 -0.5625q-1.171875 0 -1.734375 0.40625q-0.5625 0.40625 -0.828125 1.46875l-1.640625 -0.234375q0.234375 -1.046875 0.734375 -1.6875q0.515625 -0.640625 1.46875 -0.984375q0.96875 -0.359375 2.25 -0.359375q1.265625 0 2.046875 0.296875q0.78125 0.296875 1.15625 0.75q0.375 0.453125 0.515625 1.140625q0.09375 0.421875 0.09375 1.53125l0 2.234375q0 2.328125 0.09375 2.953125q0.109375 0.609375 0.4375 1.171875l-1.75 0q-0.265625 -0.515625 -0.328125 -1.21875zm-0.140625 -3.71875q-0.90625 0.359375 -2.734375 0.625q-1.03125 0.140625 -1.453125 0.328125q-0.421875 0.1875 -0.65625 0.546875q-0.234375 0.359375 -0.234375 0.796875q0 0.671875 0.5 1.125q0.515625 0.4375 1.484375 0.4375q0.96875 0 1.71875 -0.421875q0.75 -0.4375 1.109375 -1.15625q0.265625 -0.578125 0.265625 -1.671875l0 -0.609375zm4.094467 4.9375l0 -13.59375l1.671875 0l0 7.75l3.953125 -4.015625l2.15625 0l-3.765625 3.65625l4.140625 6.203125l-2.0625 0l-3.25 -5.03125l-1.171875 1.125l0 3.90625l-1.671875 0zm16.0625 -3.171875l1.71875 0.21875q-0.40625 1.5 -1.515625 2.34375q-1.09375 0.828125 -2.8125 0.828125q-2.15625 0 -3.421875 -1.328125q-1.265625 -1.328125 -1.265625 -3.734375q0 -2.484375 1.265625 -3.859375q1.28125 -1.375 3.328125 -1.375q1.984375 0 3.234375 1.34375q1.25 1.34375 1.25 3.796875q0 0.140625 -0.015625 0.4375l-7.34375 0q0.09375 1.625 0.921875 2.484375q0.828125 0.859375 2.0625 0.859375q0.90625 0 1.546875 -0.46875q0.65625 -0.484375 1.046875 -1.546875zm-5.484375 -2.703125l5.5 0q-0.109375 -1.234375 -0.625 -1.859375q-0.796875 -0.96875 -2.078125 -0.96875q-1.140625 0 -1.9375 0.78125q-0.78125 0.765625 -0.859375 2.046875zm9.516342 5.875l0 -8.546875l-1.484375 0l0 -1.3125l1.484375 0l0 -1.046875q0 -0.984375 0.171875 -1.46875q0.234375 -0.65625 0.84375 -1.046875q0.609375 -0.40625 1.703125 -0.40625q0.703125 0 1.5625 0.15625l-0.25 1.46875q-0.515625 -0.09375 -0.984375 -0.09375q-0.765625 0 -1.078125 0.328125q-0.3125 0.3125 -0.3125 1.203125l0 0.90625l1.921875 0l0 1.3125l-1.921875 0l0 8.546875l-1.65625 0zm4.792679 -11.6875l0 -1.90625l1.671875 0l0 1.90625l-1.671875 0zm0 11.6875l0 -9.859375l1.671875 0l0 9.859375l-1.671875 0zm4.097946 0l0 -13.59375l1.671875 0l0 13.59375l-1.671875 0zm10.926071 -3.171875l1.71875 0.21875q-0.40625 1.5 -1.515625 2.34375q-1.09375 0.828125 -2.8125 0.828125q-2.15625 0 -3.421875 -1.328125q-1.265625 -1.328125 -1.265625 -3.734375q0 -2.484375 1.265625 -3.859375q1.28125 -1.375 3.328125 -1.375q1.984375 0 3.234375 1.34375q1.25 1.34375 1.25 3.796875q0 0.140625 -0.015625 0.4375l-7.34375 0q0.09375 1.625 0.921875 2.484375q0.828125 0.859375 2.0625 0.859375q0.90625 0 1.546875 -0.46875q0.65625 -0.484375 1.046875 -1.546875zm-5.484375 -2.703125l5.5 0q-0.109375 -1.234375 -0.625 -1.859375q-0.796875 -0.96875 -2.078125 -0.96875q-1.140625 0 -1.9375 0.78125q-0.78125 0.765625 -0.859375 2.046875zm17.949646 4.375l0.234375 1.484375q-0.703125 0.140625 -1.265625 0.140625q-0.90625 0 -1.40625 -0.28125q-0.5 -0.296875 -0.703125 -0.75q-0.203125 -0.46875 -0.203125 -1.984375l0 -5.65625l-1.234375 0l0 -1.3125l1.234375 0l0 -2.4375l1.65625 -1.0l0 3.4375l1.6875 0l0 1.3125l-1.6875 0l0 5.75q0 0.71875 0.078125 0.921875q0.09375 0.203125 0.296875 0.328125q0.203125 0.125 0.578125 0.125q0.265625 0 0.734375 -0.078125zm0.90205383 -3.421875q0 -2.734375 1.53125 -4.0625q1.265625 -1.09375 3.09375 -1.09375q2.03125 0 3.3125 1.34375q1.296875 1.328125 1.296875 3.671875q0 1.90625 -0.578125 3.0q-0.5625 1.078125 -1.65625 1.6875q-1.078125 0.59375 -2.375 0.59375q-2.0625 0 -3.34375 -1.328125q-1.28125 -1.328125 -1.28125 -3.8125zm1.71875 0q0 1.890625 0.828125 2.828125q0.828125 0.9375 2.078125 0.9375q1.25 0 2.0625 -0.9375q0.828125 -0.953125 0.828125 -2.890625q0 -1.828125 -0.828125 -2.765625q-0.828125 -0.9375 -2.0625 -0.9375q-1.25 0 -2.078125 0.9375q-0.828125 0.9375 -0.828125 2.828125zm13.793396 1.984375l1.65625 -0.265625q0.140625 1.0 0.765625 1.53125q0.640625 0.515625 1.78125 0.515625q1.15625 0 1.703125 -0.46875q0.5625 -0.46875 0.5625 -1.09375q0 -0.5625 -0.484375 -0.890625q-0.34375 -0.21875 -1.703125 -0.5625q-1.84375 -0.46875 -2.5625 -0.796875q-0.703125 -0.34375 -1.078125 -0.9375q-0.359375 -0.609375 -0.359375 -1.328125q0 -0.65625 0.296875 -1.21875q0.3125 -0.5625 0.828125 -0.9375q0.390625 -0.28125 1.0625 -0.484375q0.671875 -0.203125 1.4375 -0.203125q1.171875 0 2.046875 0.34375q0.875 0.328125 1.28125 0.90625q0.421875 0.5625 0.578125 1.515625l-1.625 0.21875q-0.109375 -0.75 -0.65625 -1.171875q-0.53125 -0.4375 -1.5 -0.4375q-1.15625 0 -1.640625 0.390625q-0.484375 0.375 -0.484375 0.875q0 0.328125 0.203125 0.59375q0.203125 0.265625 0.640625 0.4375q0.25 0.09375 1.46875 0.4375q1.765625 0.46875 2.46875 0.765625q0.703125 0.296875 1.09375 0.875q0.40625 0.578125 0.40625 1.4375q0 0.828125 -0.484375 1.578125q-0.484375 0.734375 -1.40625 1.140625q-0.921875 0.390625 -2.078125 0.390625q-1.921875 0 -2.9375 -0.796875q-1.0 -0.796875 -1.28125 -2.359375zm16.4375 1.71875q-0.9375 0.796875 -1.796875 1.125q-0.859375 0.3125 -1.84375 0.3125q-1.609375 0 -2.484375 -0.78125q-0.875 -0.796875 -0.875 -2.03125q0 -0.734375 0.328125 -1.328125q0.328125 -0.59375 0.859375 -0.953125q0.53125 -0.359375 1.203125 -0.546875q0.5 -0.140625 1.484375 -0.25q2.03125 -0.25 2.984375 -0.578125q0 -0.34375 0 -0.4375q0 -1.015625 -0.46875 -1.4375q-0.640625 -0.5625 -1.90625 -0.5625q-1.171875 0 -1.734375 0.40625q-0.5625 0.40625 -0.828125 1.46875l-1.640625 -0.234375q0.234375 -1.046875 0.734375 -1.6875q0.515625 -0.640625 1.46875 -0.984375q0.96875 -0.359375 2.25 -0.359375q1.265625 0 2.046875 0.296875q0.78125 0.296875 1.15625 0.75q0.375 0.453125 0.515625 1.140625q0.09375 0.421875 0.09375 1.53125l0 2.234375q0 2.328125 0.09375 2.953125q0.109375 0.609375 0.4375 1.171875l-1.75 0q-0.265625 -0.515625 -0.328125 -1.21875zm-0.140625 -3.71875q-0.90625 0.359375 -2.734375 0.625q-1.03125 0.140625 -1.453125 0.328125q-0.421875 0.1875 -0.65625 0.546875q-0.234375 0.359375 -0.234375 0.796875q0 0.671875 0.5 1.125q0.515625 0.4375 1.484375 0.4375q0.96875 0 1.71875 -0.421875q0.75 -0.4375 1.109375 -1.15625q0.265625 -0.578125 0.265625 -1.671875l0 -0.609375zm7.735092 3.4375l0.234375 1.484375q-0.703125 0.140625 -1.265625 0.140625q-0.90625 0 -1.40625 -0.28125q-0.5 -0.296875 -0.703125 -0.75q-0.203125 -0.46875 -0.203125 -1.984375l0 -5.65625l-1.234375 0l0 -1.3125l1.234375 0l0 -2.4375l1.65625 -1.0l0 3.4375l1.6875 0l0 1.3125l-1.6875 0l0 5.75q0 0.71875 0.078125 0.921875q0.09375 0.203125 0.296875 0.328125q0.203125 0.125 0.578125 0.125q0.265625 0 0.734375 -0.078125zm1.5426788 -10.1875l0 -1.90625l1.6718903 0l0 1.90625l-1.6718903 0zm0 11.6875l0 -9.859375l1.6718903 0l0 9.859375l-1.6718903 0zm3.4573212 -2.9375l1.65625 -0.265625q0.140625 1.0 0.765625 1.53125q0.640625 0.515625 1.78125 0.515625q1.15625 0 1.703125 -0.46875q0.5625 -0.46875 0.5625 -1.09375q0 -0.5625 -0.484375 -0.890625q-0.34375 -0.21875 -1.703125 -0.5625q-1.84375 -0.46875 -2.5625 -0.796875q-0.703125 -0.34375 -1.078125 -0.9375q-0.359375 -0.609375 -0.359375 -1.328125q0 -0.65625 0.296875 -1.21875q0.3125 -0.5625 0.828125 -0.9375q0.390625 -0.28125 1.0625 -0.484375q0.671875 -0.203125 1.4375 -0.203125q1.171875 0 2.046875 0.34375q0.875 0.328125 1.28125 0.90625q0.421875 0.5625 0.578125 1.515625l-1.625 0.21875q-0.109375 -0.75 -0.65625 -1.171875q-0.53125 -0.4375 -1.5 -0.4375q-1.15625 0 -1.640625 0.390625q-0.484375 0.375 -0.484375 0.875q0 0.328125 0.203125 0.59375q0.203125 0.265625 0.640625 0.4375q0.25 0.09375 1.46875 0.4375q1.765625 0.46875 2.46875 0.765625q0.703125 0.296875 1.09375 0.875q0.40625 0.578125 0.40625 1.4375q0 0.828125 -0.484375 1.578125q-0.484375 0.734375 -1.40625 1.140625q-0.921875 0.390625 -2.078125 0.390625q-1.921875 0 -2.9375 -0.796875q-1.0 -0.796875 -1.28125 -2.359375zm10.40625 2.9375l0 -8.546875l-1.484375 0l0 -1.3125l1.484375 0l0 -1.046875q0 -0.984375 0.171875 -1.46875q0.234375 -0.65625 0.84375 -1.046875q0.609375 -0.40625 1.703125 -0.40625q0.703125 0 1.5625 0.15625l-0.25 1.46875q-0.515625 -0.09375 -0.984375 -0.09375q-0.765625 0 -1.078125 0.328125q-0.3125 0.3125 -0.3125 1.203125l0 0.90625l1.921875 0l0 1.3125l-1.921875 0l0 8.546875l-1.65625 0zm4.698944 3.796875l-0.171875 -1.5625q0.546875 0.140625 0.953125 0.140625q0.546875 0 0.875 -0.1875q0.34375 -0.1875 0.5625 -0.515625q0.15625 -0.25 0.5 -1.25q0.046875 -0.140625 0.15625 -0.40625l-3.734375 -9.875l1.796875 0l2.046875 5.71875q0.40625 1.078125 0.71875 2.28125q0.28125 -1.15625 0.6875 -2.25l2.09375 -5.75l1.671875 0l-3.75 10.03125q-0.59375 1.625 -0.9375 2.234375q-0.4375 0.828125 -1.015625 1.203125q-0.578125 0.390625 -1.375 0.390625q-0.484375 0 -1.078125 -0.203125zm18.24582 -5.296875l0.234375 1.484375q-0.703125 0.140625 -1.265625 0.140625q-0.90625 0 -1.40625 -0.28125q-0.5 -0.296875 -0.703125 -0.75q-0.203125 -0.46875 -0.203125 -1.984375l0 -5.65625l-1.234375 0l0 -1.3125l1.234375 0l0 -2.4375l1.65625 -1.0l0 3.4375l1.6875 0l0 1.3125l-1.6875 0l0 5.75q0 0.71875 0.078125 0.921875q0.09375 0.203125 0.296875 0.328125q0.203125 0.125 0.578125 0.125q0.265625 0 0.734375 -0.078125zm7.9645386 0.28125q-0.9375 0.796875 -1.796875 1.125q-0.859375 0.3125 -1.84375 0.3125q-1.609375 0 -2.484375 -0.78125q-0.875 -0.796875 -0.875 -2.03125q0 -0.734375 0.328125 -1.328125q0.328125 -0.59375 0.859375 -0.953125q0.53125 -0.359375 1.203125 -0.546875q0.5 -0.140625 1.484375 -0.25q2.03125 -0.25 2.984375 -0.578125q0 -0.34375 0 -0.4375q0 -1.015625 -0.46875 -1.4375q-0.640625 -0.5625 -1.90625 -0.5625q-1.171875 0 -1.734375 0.40625q-0.5625 0.40625 -0.828125 1.46875l-1.640625 -0.234375q0.234375 -1.046875 0.734375 -1.6875q0.515625 -0.640625 1.46875 -0.984375q0.96875 -0.359375 2.25 -0.359375q1.265625 0 2.046875 0.296875q0.78125 0.296875 1.15625 0.75q0.375 0.453125 0.515625 1.140625q0.09375 0.421875 0.09375 1.53125l0 2.234375q0 2.328125 0.09375 2.953125q0.109375 0.609375 0.4375 1.171875l-1.75 0q-0.265625 -0.515625 -0.328125 -1.21875zm-0.140625 -3.71875q-0.90625 0.359375 -2.734375 0.625q-1.03125 0.140625 -1.453125 0.328125q-0.421875 0.1875 -0.65625 0.546875q-0.234375 0.359375 -0.234375 0.796875q0 0.671875 0.5 1.125q0.515625 0.4375 1.484375 0.4375q0.96875 0 1.71875 -0.421875q0.75 -0.4375 1.109375 -1.15625q0.265625 -0.578125 0.265625 -1.671875l0 -0.609375zm4.0632324 4.9375l0 -9.859375l1.5 0l0 1.5q0.578125 -1.046875 1.0625 -1.375q0.484375 -0.34375 1.078125 -0.34375q0.84375 0 1.71875 0.546875l-0.578125 1.546875q-0.609375 -0.359375 -1.234375 -0.359375q-0.546875 0 -0.984375 0.328125q-0.421875 0.328125 -0.609375 0.90625q-0.28125 0.890625 -0.28125 1.953125l0 5.15625l-1.671875 0zm5.9313965 0.8125l1.609375 0.25q0.109375 0.75 0.578125 1.09375q0.609375 0.453125 1.6875 0.453125q1.171875 0 1.796875 -0.46875q0.625 -0.453125 0.859375 -1.28125q0.125 -0.515625 0.109375 -2.15625q-1.09375 1.296875 -2.71875 1.296875q-2.03125 0 -3.15625 -1.46875q-1.109375 -1.46875 -1.109375 -3.515625q0 -1.40625 0.515625 -2.59375q0.515625 -1.203125 1.484375 -1.84375q0.96875 -0.65625 2.265625 -0.65625q1.75 0 2.875 1.40625l0 -1.1875l1.546875 0l0 8.515625q0 2.3125 -0.46875 3.265625q-0.46875 0.96875 -1.484375 1.515625q-1.015625 0.5625 -2.5 0.5625q-1.765625 0 -2.859375 -0.796875q-1.078125 -0.796875 -1.03125 -2.390625zm1.375 -5.921875q0 1.953125 0.765625 2.84375q0.78125 0.890625 1.9375 0.890625q1.140625 0 1.921875 -0.890625q0.78125 -0.890625 0.78125 -2.78125q0 -1.8125 -0.8125 -2.71875q-0.796875 -0.921875 -1.921875 -0.921875q-1.109375 0 -1.890625 0.90625q-0.78125 0.890625 -0.78125 2.671875zm16.047607 1.9375l1.71875 0.21875q-0.40625 1.5 -1.515625 2.34375q-1.09375 0.828125 -2.8125 0.828125q-2.15625 0 -3.421875 -1.328125q-1.265625 -1.328125 -1.265625 -3.734375q0 -2.484375 1.265625 -3.859375q1.28125 -1.375 3.328125 -1.375q1.984375 0 3.234375 1.34375q1.25 1.34375 1.25 3.796875q0 0.140625 -0.015625 0.4375l-7.34375 0q0.09375 1.625 0.921875 2.484375q0.828125 0.859375 2.0625 0.859375q0.90625 0 1.546875 -0.46875q0.65625 -0.484375 1.046875 -1.546875zm-5.484375 -2.703125l5.5 0q-0.109375 -1.234375 -0.625 -1.859375q-0.796875 -0.96875 -2.078125 -0.96875q-1.140625 0 -1.9375 0.78125q-0.78125 0.765625 -0.859375 2.046875zm12.766357 4.375l0.234375 1.484375q-0.703125 0.140625 -1.265625 0.140625q-0.90625 0 -1.40625 -0.28125q-0.5 -0.296875 -0.703125 -0.75q-0.203125 -0.46875 -0.203125 -1.984375l0 -5.65625l-1.234375 0l0 -1.3125l1.234375 0l0 -2.4375l1.65625 -1.0l0 3.4375l1.6875 0l0 1.3125l-1.6875 0l0 5.75q0 0.71875 0.078125 0.921875q0.09375 0.203125 0.296875 0.328125q0.203125 0.125 0.578125 0.125q0.265625 0 0.734375 -0.078125zm0.8551636 -1.4375l1.65625 -0.265625q0.140625 1.0 0.765625 1.53125q0.640625 0.515625 1.78125 0.515625q1.15625 0 1.703125 -0.46875q0.5625 -0.46875 0.5625 -1.09375q0 -0.5625 -0.484375 -0.890625q-0.34375 -0.21875 -1.703125 -0.5625q-1.84375 -0.46875 -2.5625 -0.796875q-0.703125 -0.34375 -1.078125 -0.9375q-0.359375 -0.609375 -0.359375 -1.328125q0 -0.65625 0.296875 -1.21875q0.3125 -0.5625 0.828125 -0.9375q0.390625 -0.28125 1.0625 -0.484375q0.671875 -0.203125 1.4375 -0.203125q1.171875 0 2.046875 0.34375q0.875 0.328125 1.28125 0.90625q0.421875 0.5625 0.578125 1.515625l-1.625 0.21875q-0.109375 -0.75 -0.65625 -1.171875q-0.53125 -0.4375 -1.5 -0.4375q-1.15625 0 -1.640625 0.390625q-0.484375 0.375 -0.484375 0.875q0 0.328125 0.203125 0.59375q0.203125 0.265625 0.640625 0.4375q0.25 0.09375 1.46875 0.4375q1.765625 0.46875 2.46875 0.765625q0.703125 0.296875 1.09375 0.875q0.40625 0.578125 0.40625 1.4375q0 0.828125 -0.484375 1.578125q-0.484375 0.734375 -1.40625 1.140625q-0.921875 0.390625 -2.078125 0.390625q-1.921875 0 -2.9375 -0.796875q-1.0 -0.796875 -1.28125 -2.359375z" fill-rule="nonzero"></path><path fill="#351c75" d="m67.4166 970.3385l1.171875 -0.109375q0.078125 0.703125 0.375 1.15625q0.3125 0.4375 0.9375 0.71875q0.640625 0.265625 1.4375 0.265625q0.703125 0 1.234375 -0.203125q0.546875 -0.203125 0.8125 -0.5625q0.265625 -0.375 0.265625 -0.8125q0 -0.4375 -0.265625 -0.765625q-0.25 -0.328125 -0.828125 -0.546875q-0.375 -0.140625 -1.65625 -0.453125q-1.28125 -0.3125 -1.796875 -0.578125q-0.671875 -0.34375 -1.0 -0.859375q-0.328125 -0.53125 -0.328125 -1.171875q0 -0.703125 0.390625 -1.3125q0.40625 -0.609375 1.171875 -0.921875q0.78125 -0.328125 1.71875 -0.328125q1.03125 0 1.8125 0.34375q0.796875 0.328125 1.21875 0.984375q0.4375 0.640625 0.46875 1.453125l-1.1875 0.09375q-0.09375 -0.890625 -0.640625 -1.328125q-0.546875 -0.453125 -1.625 -0.453125q-1.109375 0 -1.625 0.40625q-0.515625 0.40625 -0.515625 0.984375q0 0.5 0.359375 0.828125q0.359375 0.328125 1.859375 0.671875q1.5 0.328125 2.0625 0.578125q0.8125 0.375 1.1875 0.953125q0.390625 0.578125 0.390625 1.328125q0 0.734375 -0.421875 1.390625q-0.421875 0.65625 -1.21875 1.03125q-0.796875 0.359375 -1.796875 0.359375q-1.265625 0 -2.125 -0.359375q-0.84375 -0.375 -1.328125 -1.109375q-0.484375 -0.75 -0.515625 -1.671875zm13.56163 2.15625q-0.625 0.53125 -1.21875 0.765625q-0.578125 0.21875 -1.25 0.21875q-1.125 0 -1.71875 -0.546875q-0.59375 -0.546875 -0.59375 -1.390625q0 -0.484375 0.21875 -0.890625q0.234375 -0.421875 0.59375 -0.671875q0.375 -0.25 0.828125 -0.375q0.328125 -0.078125 1.015625 -0.171875q1.375 -0.15625 2.03125 -0.390625q0.015625 -0.234375 0.015625 -0.296875q0 -0.703125 -0.328125 -0.984375q-0.4375 -0.390625 -1.296875 -0.390625q-0.8125 0 -1.203125 0.28125q-0.375 0.28125 -0.5625 1.0l-1.109375 -0.140625q0.140625 -0.71875 0.484375 -1.15625q0.359375 -0.453125 1.015625 -0.6875q0.671875 -0.234375 1.53125 -0.234375q0.875 0 1.40625 0.203125q0.546875 0.203125 0.796875 0.515625q0.25 0.296875 0.359375 0.765625q0.046875 0.296875 0.046875 1.0625l0 1.515625q0 1.59375 0.078125 2.015625q0.078125 0.421875 0.28125 0.8125l-1.1875 0q-0.171875 -0.359375 -0.234375 -0.828125zm-0.09375 -2.5625q-0.625 0.265625 -1.859375 0.4375q-0.703125 0.109375 -1.0 0.234375q-0.296875 0.125 -0.453125 0.375q-0.15625 0.234375 -0.15625 0.53125q0 0.453125 0.34375 0.765625q0.34375 0.296875 1.015625 0.296875q0.65625 0 1.171875 -0.28125q0.515625 -0.296875 0.765625 -0.796875q0.171875 -0.375 0.171875 -1.140625l0 -0.421875zm4.9906006 3.390625l-2.5625 -6.734375l1.203125 0l1.4375 4.03125q0.234375 0.65625 0.4375 1.359375q0.15625 -0.53125 0.421875 -1.28125l1.5 -4.109375l1.171875 0l-2.546875 6.734375l-1.0625 0zm9.3984375 -2.171875l1.1875 0.140625q-0.28125 1.046875 -1.046875 1.625q-0.75 0.5625 -1.921875 0.5625q-1.484375 0 -2.359375 -0.90625q-0.859375 -0.921875 -0.859375 -2.5625q0 -1.703125 0.875 -2.640625q0.890625 -0.9375 2.28125 -0.9375q1.359375 0 2.203125 0.921875q0.859375 0.921875 0.859375 2.578125q0 0.109375 0 0.3125l-5.03125 0q0.0625 1.109375 0.625 1.703125q0.5625 0.59375 1.40625 0.59375q0.640625 0 1.078125 -0.328125q0.453125 -0.34375 0.703125 -1.0625zm-3.75 -1.84375l3.765625 0q-0.078125 -0.859375 -0.4375 -1.28125q-0.546875 -0.65625 -1.40625 -0.65625q-0.796875 0 -1.328125 0.53125q-0.53125 0.515625 -0.59375 1.40625zm12.756088 3.0l0.15625 1.0q-0.484375 0.109375 -0.859375 0.109375q-0.625 0 -0.96875 -0.203125q-0.34375 -0.203125 -0.484375 -0.515625q-0.140625 -0.328125 -0.140625 -1.34375l0 -3.890625l-0.828125 0l0 -0.875l0.828125 0l0 -1.671875l1.140625 -0.6875l0 2.359375l1.15625 0l0 0.875l-1.15625 0l0 3.953125q0 0.484375 0.0625 0.625q0.0625 0.140625 0.1875 0.21875q0.140625 0.078125 0.390625 0.078125q0.203125 0 0.515625 -0.03125zm0.7811127 -2.359375q0 -1.875 1.03125 -2.765625q0.875 -0.75 2.125 -0.75q1.390625 0 2.265625 0.90625q0.890625 0.90625 0.890625 2.515625q0 1.296875 -0.390625 2.046875q-0.390625 0.75 -1.140625 1.171875q-0.75 0.40625 -1.625 0.40625q-1.421875 0 -2.296875 -0.90625q-0.859375 -0.90625 -0.859375 -2.625zm1.171875 0q0 1.296875 0.5625 1.953125q0.5625 0.640625 1.421875 0.640625q0.84375 0 1.40625 -0.640625q0.578125 -0.65625 0.578125 -1.984375q0 -1.25 -0.578125 -1.890625q-0.5625 -0.65625 -1.40625 -0.65625q-0.859375 0 -1.421875 0.640625q-0.5625 0.640625 -0.5625 1.9375zm10.693588 3.375l0 -1.296875l1.296875 0l0 1.296875l-1.296875 0zm2.9217377 -2.015625l1.125 -0.171875q0.09375 0.671875 0.53125 1.046875q0.4375 0.359375 1.21875 0.359375q0.78125 0 1.15625 -0.3125q0.390625 -0.328125 0.390625 -0.765625q0 -0.390625 -0.34375 -0.609375q-0.234375 -0.15625 -1.171875 -0.390625q-1.25 -0.3125 -1.734375 -0.546875q-0.484375 -0.234375 -0.734375 -0.640625q-0.25 -0.40625 -0.25 -0.90625q0 -0.453125 0.203125 -0.828125q0.203125 -0.390625 0.5625 -0.640625q0.265625 -0.203125 0.71875 -0.328125q0.46875 -0.140625 1.0 -0.140625q0.78125 0 1.375 0.234375q0.609375 0.21875 0.890625 0.609375q0.296875 0.390625 0.40625 1.046875l-1.125 0.15625q-0.078125 -0.53125 -0.4375 -0.8125q-0.359375 -0.296875 -1.03125 -0.296875q-0.78125 0 -1.125 0.265625q-0.34375 0.25 -0.34375 0.609375q0 0.21875 0.140625 0.390625q0.140625 0.1875 0.4375 0.3125q0.171875 0.0625 1.015625 0.28125q1.21875 0.328125 1.6875 0.53125q0.484375 0.203125 0.75 0.609375q0.28125 0.390625 0.28125 0.96875q0 0.578125 -0.34375 1.078125q-0.328125 0.5 -0.953125 0.78125q-0.625 0.28125 -1.421875 0.28125q-1.3125 0 -2.0 -0.546875q-0.6875 -0.546875 -0.875 -1.625zm7.1015625 2.015625l0 -6.734375l1.03125 0l0 1.015625q0.39061737 -0.71875 0.7187424 -0.9375q0.34375 -0.234375 0.734375 -0.234375q0.578125 0 1.171875 0.359375l-0.390625 1.0625q-0.421875 -0.25 -0.828125 -0.25q-0.375 0 -0.6875 0.234375q-0.296875 0.21875 -0.421875 0.625q-0.1875 0.609375 -0.1875 1.328125l0 3.53125l-1.1406174 0zm8.844612 -2.46875l1.125 0.140625q-0.171875 1.171875 -0.9375 1.828125q-0.765625 0.65625 -1.859375 0.65625q-1.390625 0 -2.234375 -0.90625q-0.828125 -0.90625 -0.828125 -2.59375q0 -1.09375 0.359375 -1.90625q0.359375 -0.828125 1.09375 -1.234375q0.734375 -0.40625 1.609375 -0.40625q1.09375 0 1.796875 0.5625q0.703125 0.546875 0.890625 1.5625l-1.109375 0.171875q-0.15625 -0.671875 -0.5625 -1.015625q-0.390625 -0.34375 -0.96875 -0.34375q-0.859375 0 -1.40625 0.625q-0.53125 0.609375 -0.53125 1.953125q0 1.359375 0.515625 1.984375q0.515625 0.609375 1.359375 0.609375q0.671875 0 1.125 -0.40625q0.453125 -0.421875 0.5625 -1.28125zm2.2421875 2.46875l0 -9.3125l1.140625 0l0 9.3125l-1.140625 0zm2.99234 -7.984375l0 -1.328125l1.140625 0l0 1.328125l-1.140625 0zm0 7.984375l0 -6.734375l1.140625 0l0 6.734375l-1.140625 0zm4.007965 0l-1.0625 0l0 -9.3125l1.15625 0l0 3.328125q0.71875 -0.90625 1.84375 -0.90625q0.625 0 1.171875 0.25q0.5625 0.25 0.921875 0.703125q0.359375 0.453125 0.5625 1.09375q0.203125 0.640625 0.203125 1.375q0 1.734375 -0.859375 2.6875q-0.859375 0.9375 -2.0625 0.9375q-1.1875 0 -1.875 -1.0l0 0.84375zm-0.015625 -3.421875q0 1.21875 0.34375 1.75q0.53125 0.890625 1.453125 0.890625q0.75 0 1.296875 -0.65625q0.546875 -0.65625 0.546875 -1.9375q0 -1.328125 -0.53125 -1.953125q-0.515625 -0.625 -1.265625 -0.625q-0.75 0 -1.296875 0.65625q-0.546875 0.640625 -0.546875 1.875zm5.9281006 0.625l0 -1.140625l3.515625 0l0 1.140625l-3.515625 0zm9.28212 0.328125l1.125 0.140625q-0.171875 1.171875 -0.9375 1.828125q-0.765625 0.65625 -1.859375 0.65625q-1.390625 0 -2.234375 -0.90625q-0.828125 -0.90625 -0.828125 -2.59375q0 -1.09375 0.359375 -1.90625q0.359375 -0.828125 1.09375 -1.234375q0.734375 -0.40625 1.609375 -0.40625q1.09375 0 1.796875 0.5625q0.703125 0.546875 0.890625 1.5625l-1.109375 0.171875q-0.15625 -0.671875 -0.5625 -1.015625q-0.390625 -0.34375 -0.96875 -0.34375q-0.859375 0 -1.40625 0.625q-0.53125 0.609375 -0.53125 1.953125q0 1.359375 0.515625 1.984375q0.515625 0.609375 1.359375 0.609375q0.671875 0 1.125 -0.40625q0.453125 -0.421875 0.5625 -1.28125zm6.6640625 1.640625q-0.625 0.53125 -1.21875 0.765625q-0.578125 0.21875 -1.25 0.21875q-1.125 0 -1.71875 -0.546875q-0.59375 -0.546875 -0.59375 -1.390625q0 -0.484375 0.21875 -0.890625q0.234375 -0.421875 0.59375 -0.671875q0.375 -0.25 0.828125 -0.375q0.328125 -0.078125 1.015625 -0.171875q1.375 -0.15625 2.03125 -0.390625q0.015625 -0.234375 0.015625 -0.296875q0 -0.703125 -0.328125 -0.984375q-0.4375 -0.390625 -1.296875 -0.390625q-0.8125 0 -1.203125 0.28125q-0.375 0.28125 -0.5625 1.0l-1.109375 -0.140625q0.140625 -0.71875 0.484375 -1.15625q0.359375 -0.453125 1.015625 -0.6875q0.671875 -0.234375 1.53125 -0.234375q0.875 0 1.40625 0.203125q0.546875 0.203125 0.796875 0.515625q0.25 0.296875 0.359375 0.765625q0.046875 0.296875 0.046875 1.0625l0 1.515625q0 1.59375 0.078125 2.015625q0.078125 0.421875 0.28125 0.8125l-1.1875 0q-0.171875 -0.359375 -0.234375 -0.828125zm-0.09375 -2.5625q-0.625 0.265625 -1.859375 0.4375q-0.703125 0.109375 -1.0 0.234375q-0.296875 0.125 -0.453125 0.375q-0.15625 0.234375 -0.15625 0.53125q0 0.453125 0.34375 0.765625q0.34375 0.296875 1.015625 0.296875q0.65625 0 1.171875 -0.28125q0.515625 -0.296875 0.765625 -0.796875q0.171875 -0.375 0.171875 -1.140625l0 -0.421875zm7.5062256 0.921875l1.125 0.140625q-0.171875 1.171875 -0.9375 1.828125q-0.765625 0.65625 -1.859375 0.65625q-1.390625 0 -2.234375 -0.90625q-0.828125 -0.90625 -0.828125 -2.59375q0 -1.09375 0.359375 -1.90625q0.359375 -0.828125 1.09375 -1.234375q0.734375 -0.40625 1.609375 -0.40625q1.09375 0 1.796875 0.5625q0.703125 0.546875 0.890625 1.5625l-1.109375 0.171875q-0.15625 -0.671875 -0.5625 -1.015625q-0.390625 -0.34375 -0.96875 -0.34375q-0.859375 0 -1.40625 0.625q-0.53125 0.609375 -0.53125 1.953125q0 1.359375 0.515625 1.984375q0.515625 0.609375 1.359375 0.609375q0.671875 0 1.125 -0.40625q0.453125 -0.421875 0.5625 -1.28125zm2.2734375 2.46875l0 -9.3125l1.140625 0l0 3.34375q0.796875 -0.921875 2.015625 -0.921875q0.75 0 1.296875 0.296875q0.5625 0.296875 0.796875 0.8125q0.234375 0.515625 0.234375 1.515625l0 4.265625l-1.140625 0l0 -4.265625q0 -0.859375 -0.375 -1.25q-0.359375 -0.390625 -1.046875 -0.390625q-0.5 0 -0.953125 0.265625q-0.453125 0.25 -0.640625 0.703125q-0.1875 0.453125 -0.1875 1.25l0 3.6875l-1.140625 0zm12.021851 -2.171875l1.1875 0.140625q-0.28125 1.046875 -1.046875 1.625q-0.75 0.5625 -1.921875 0.5625q-1.484375 0 -2.359375 -0.90625q-0.859375 -0.921875 -0.859375 -2.5625q0 -1.703125 0.875 -2.640625q0.890625 -0.9375 2.28125 -0.9375q1.359375 0 2.203125 0.921875q0.859375 0.921875 0.859375 2.578125q0 0.109375 0 0.3125l-5.03125 0q0.0625 1.109375 0.625 1.703125q0.5625 0.59375 1.40625 0.59375q0.640625 0 1.078125 -0.328125q0.453125 -0.34375 0.703125 -1.0625zm-3.75 -1.84375l3.765625 0q-0.078125 -0.859375 -0.4375 -1.28125q-0.546875 -0.65625 -1.40625 -0.65625q-0.796875 0 -1.328125 0.53125q-0.53125 0.515625 -0.59375 1.40625zm5.6937256 4.171875l2.703125 -9.625l0.90625 0l-2.6875 9.625l-0.921875 0zm11.343613 -3.421875l1.234375 0.3125q-0.390625 1.515625 -1.40625 2.3125q-1.0 0.796875 -2.453125 0.796875q-1.5 0 -2.453125 -0.609375q-0.9375 -0.609375 -1.4375 -1.765625q-0.484375 -1.171875 -0.484375 -2.5q0 -1.453125 0.5625 -2.53125q0.5625 -1.09375 1.578125 -1.65625q1.03125 -0.5625 2.265625 -0.5625q1.390625 0 2.34375 0.71875q0.953125 0.703125 1.328125 2.0l-1.21875 0.28125q-0.328125 -1.015625 -0.9375 -1.46875q-0.609375 -0.46875 -1.546875 -0.46875q-1.078125 0 -1.796875 0.515625q-0.71875 0.515625 -1.015625 1.375q-0.28125 0.859375 -0.28125 1.78125q0 1.1875 0.34375 2.078125q0.34375 0.890625 1.0625 1.328125q0.734375 0.4375 1.59375 0.4375q1.03125 0 1.75 -0.59375q0.71875 -0.609375 0.96875 -1.78125zm2.6095276 -1.265625q0 -2.3125 1.234375 -3.625q1.25 -1.3125 3.21875 -1.3125q1.296875 0 2.328125 0.625q1.03125 0.609375 1.578125 1.71875q0.546875 1.09375 0.546875 2.484375q0 1.421875 -0.578125 2.546875q-0.5625 1.109375 -1.609375 1.6875q-1.046875 0.5625 -2.265625 0.5625q-1.3125 0 -2.359375 -0.625q-1.03125 -0.640625 -1.5625 -1.734375q-0.53125 -1.109375 -0.53125 -2.328125zm1.265625 0.015625q0 1.6875 0.90625 2.65625q0.90625 0.96875 2.28125 0.96875q1.390625 0 2.28125 -0.96875q0.90625 -0.984375 0.90625 -2.78125q0 -1.140625 -0.390625 -1.984375q-0.390625 -0.859375 -1.125 -1.3125q-0.734375 -0.46875 -1.65625 -0.46875q-1.3125 0 -2.265625 0.90625q-0.9375 0.890625 -0.9375 2.984375zm9.445175 4.515625l0 -9.3125l1.84375 0l2.203125 6.59375q0.3125 0.921875 0.453125 1.375q0.15625 -0.5 0.484375 -1.484375l2.234375 -6.484375l1.65625 0l0 9.3125l-1.1875 0l0 -7.78125l-2.703125 7.78125l-1.109375 0l-2.6875 -7.921875l0 7.921875l-1.1875 0zm11.102432 0l0 -9.3125l1.84375 0l2.203125 6.59375q0.3125 0.921875 0.453125 1.375q0.15625 -0.5 0.484375 -1.484375l2.234375 -6.484375l1.65625 0l0 9.3125l-1.1875 0l0 -7.78125l-2.703125 7.78125l-1.109375 0l-2.6875 -7.921875l0 7.921875l-1.1875 0zm11.352432 0l0 -9.3125l1.21875 0l0 9.3125l-1.21875 0zm5.8592377 0l0 -8.203125l-3.0625 0l0 -1.109375l7.375 0l0 1.109375l-3.078125 0l0 8.203125l-1.234375 0zm4.7663574 0.15625l2.703125 -9.625l0.90625 0l-2.6875 9.625l-0.921875 0zm7.0779877 -0.15625l0 -8.203125l-3.0625 0l0 -1.109375l7.3750153 0l0 1.109375l-3.078125 0l0 8.203125l-1.2343903 0zm8.391373 0l0 -3.9375l-3.59375 -5.375l1.5 0l1.84375 2.8125q0.5 0.78125 0.9375 1.578125q0.421875 -0.734375 1.015625 -1.640625l1.8125 -2.75l1.421875 0l-3.703125 5.375l0 3.9375l-1.234375 0zm6.26474 0l0 -9.3125l3.515625 0q0.921875 0 1.40625 0.09375q0.6875 0.109375 1.1562805 0.4375q0.46875 0.3125 0.75 0.890625q0.28125 0.578125 0.28125 1.28125q0 1.1875 -0.765625 2.015625q-0.7500305 0.8125 -2.7187805 0.8125l-2.390625 0l0 3.78125l-1.234375 0zm1.234375 -4.875l2.40625 0q1.1875 0 1.6875 -0.4375q0.5156555 -0.453125 0.5156555 -1.265625q0 -0.578125 -0.29690552 -0.984375q-0.296875 -0.421875 -0.78125 -0.5625q-0.3125 -0.078125 -1.15625 -0.078125l-2.375 0l0 3.328125zm7.6866455 4.875l0 -9.3125l6.71875 0l0 1.109375l-5.484375 0l0 2.84375l5.140625 0l0 1.09375l-5.140625 0l0 3.171875l5.703125 0l0 1.09375l-6.9375 0zm7.85849 0.15625l2.703125 -9.625l0.90625 0l-2.6875 9.625l-0.921875 0zm10.812378 -9.46875l1.234375 0l0 5.390625q0 1.390625 -0.328125 2.21875q-0.3125 0.828125 -1.140625 1.34375q-0.828125 0.515625 -2.171875 0.515625q-1.3125 0 -2.140625 -0.453125q-0.828125 -0.453125 -1.1875 -1.296875q-0.359375 -0.859375 -0.359375 -2.328125l0 -5.390625l1.234375 0l0 5.375q0 1.21875 0.21875 1.796875q0.234375 0.5625 0.78125 0.875q0.546875 0.3125 1.34375 0.3125q1.359375 0 1.9375 -0.609375q0.578125 -0.625 0.578125 -2.375l0 -5.375zm3.5001526 9.3125l0 -9.3125l1.265625 0l4.890625 7.3125l0 -7.3125l1.1875 0l0 9.3125l-1.265625 0l-4.890625 -7.3125l0 7.3125l-1.1875 0zm9.859528 0l0 -9.3125l1.21875 0l0 9.3125l-1.21875 0zm5.859253 0l0 -8.203125l-3.0625 0l0 -1.109375l7.375 0l0 1.109375l-3.078125 0l0 8.203125l-1.234375 0zm5.9538574 0l0 -1.296875l1.296875 0l0 1.296875l-1.296875 0zm3.140503 -4.53125q0 -2.3125 1.234375 -3.625q1.25 -1.3125 3.21875 -1.3125q1.296875 0 2.328125 0.625q1.03125 0.609375 1.578125 1.71875q0.546875 1.09375 0.546875 2.484375q0 1.421875 -0.578125 2.546875q-0.5625 1.109375 -1.609375 1.6875q-1.046875 0.5625 -2.265625 0.5625q-1.3125 0 -2.359375 -0.625q-1.03125 -0.640625 -1.5625 -1.734375q-0.53125 -1.109375 -0.53125 -2.328125zm1.265625 0.015625q0 1.6875 0.90625 2.65625q0.90625 0.96875 2.28125 0.96875q1.390625 0 2.28125 -0.96875q0.90625 -0.984375 0.90625 -2.78125q0 -1.140625 -0.390625 -1.984375q-0.390625 -0.859375 -1.125 -1.3125q-0.734375 -0.46875 -1.65625 -0.46875q-1.3125 0 -2.265625 0.90625q-0.9375 0.890625 -0.9375 2.984375zm9.47644 4.515625l0 -9.3125l3.515625 0q0.921875 0 1.40625 0.09375q0.6875 0.109375 1.15625 0.4375q0.46875 0.3125 0.75 0.890625q0.28125 0.578125 0.28125 1.28125q0 1.1875 -0.765625 2.015625q-0.75 0.8125 -2.71875 0.8125l-2.390625 0l0 3.78125l-1.234375 0zm1.234375 -4.875l2.40625 0q1.1875 0 1.6875 -0.4375q0.515625 -0.453125 0.515625 -1.265625q0 -0.578125 -0.296875 -0.984375q-0.296875 -0.421875 -0.78125 -0.5625q-0.3125 -0.078125 -1.15625 -0.078125l-2.375 0l0 3.328125zm7.8428955 4.875l0 -1.296875l1.296875 0l0 1.296875l-1.296875 0zm3.359253 -7.984375l0 -1.328125l1.15625 0l0 1.328125l-1.15625 0zm-1.4375 10.59375l0.21875 -0.96875q0.34375 0.09375 0.53125 0.09375q0.359375 0 0.515625 -0.234375q0.171875 -0.234375 0.171875 -1.15625l0 -7.078125l1.15625 0l0 7.109375q0 1.234375 -0.328125 1.71875q-0.421875 0.640625 -1.375 0.640625q-0.46875 0 -0.890625 -0.125zm3.9610596 -4.625l1.125 -0.171875q0.09375 0.671875 0.53125 1.046875q0.4375 0.359375 1.21875 0.359375q0.78125 0 1.15625 -0.3125q0.390625 -0.328125 0.390625 -0.765625q0 -0.390625 -0.34375 -0.609375q-0.234375 -0.15625 -1.171875 -0.390625q-1.25 -0.3125 -1.734375 -0.546875q-0.484375 -0.234375 -0.734375 -0.640625q-0.25 -0.40625 -0.25 -0.90625q0 -0.453125 0.203125 -0.828125q0.203125 -0.390625 0.5625 -0.640625q0.265625 -0.203125 0.71875 -0.328125q0.46875 -0.140625 1.0 -0.140625q0.78125 0 1.375 0.234375q0.609375 0.21875 0.890625 0.609375q0.296875 0.390625 0.40625 1.046875l-1.125 0.15625q-0.078125 -0.53125 -0.4375 -0.8125q-0.359375 -0.296875 -1.03125 -0.296875q-0.78125 0 -1.125 0.265625q-0.34375 0.25 -0.34375 0.609375q0 0.21875 0.140625 0.390625q0.140625 0.1875 0.4375 0.3125q0.171875 0.0625 1.015625 0.28125q1.21875 0.328125 1.6875 0.53125q0.484375 0.203125 0.75 0.609375q0.28125 0.390625 0.28125 0.96875q0 0.578125 -0.34375 1.078125q-0.328125 0.5 -0.953125 0.78125q-0.625 0.28125 -1.421875 0.28125q-1.3125 0 -2.0 -0.546875q-0.6875 -0.546875 -0.875 -1.625zm6.6953125 -1.359375q0 -1.875 1.03125 -2.765625q0.875 -0.75 2.125 -0.75q1.390625 0 2.265625 0.90625q0.890625 0.90625 0.890625 2.515625q0 1.296875 -0.390625 2.046875q-0.390625 0.75 -1.140625 1.171875q-0.75 0.40625 -1.625 0.40625q-1.421875 0 -2.296875 -0.90625q-0.859375 -0.90625 -0.859375 -2.625zm1.171875 0q0 1.296875 0.5625 1.953125q0.5625 0.640625 1.421875 0.640625q0.84375 0 1.40625 -0.640625q0.578125 -0.65625 0.578125 -1.984375q0 -1.25 -0.578125 -1.890625q-0.5625 -0.65625 -1.40625 -0.65625q-0.859375 0 -1.421875 0.640625q-0.5625 0.640625 -0.5625 1.9375zm6.6624756 3.375l0 -6.734375l1.03125 0l0 0.953125q0.734375 -1.109375 2.140625 -1.109375q0.609375 0 1.109375 0.21875q0.515625 0.21875 0.765625 0.578125q0.265625 0.34375 0.359375 0.84375q0.0625 0.3125 0.0625 1.109375l0 4.140625l-1.140625 0l0 -4.09375q0 -0.703125 -0.140625 -1.046875q-0.125 -0.34375 -0.46875 -0.546875q-0.328125 -0.21875 -0.78125 -0.21875q-0.734375 0 -1.265625 0.46875q-0.53125 0.453125 -0.53125 1.75l0 3.6875l-1.140625 0z" fill-rule="nonzero"></path><path fill="#000000" fill-opacity="0.0" d="m220.00262 841.5859l0 44.75592" fill-rule="nonzero"></path><path stroke="#000000" stroke-width="2.0" stroke-linejoin="round" stroke-linecap="butt" d="m220.00262 841.5859l0 32.75592" fill-rule="evenodd"></path><path fill="#000000" stroke="#000000" stroke-width="2.0" stroke-linecap="butt" d="m216.69916 874.3418l3.3034668 9.076172l3.3034668 -9.076172z" fill-rule="evenodd"></path><path fill="#000000" fill-opacity="0.0" d="m220.00262 383.89035l0 44.742767" fill-rule="nonzero"></path><path stroke="#000000" stroke-width="2.0" stroke-linejoin="round" stroke-linecap="butt" d="m220.00262 383.89035l0 32.742767" fill-rule="evenodd"></path><path fill="#000000" stroke="#000000" stroke-width="2.0" stroke-linecap="butt" d="m216.69916 416.63312l3.3034668 9.076202l3.3034668 -9.076202z" fill-rule="evenodd"></path><path fill="#000000" fill-opacity="0.0" d="m56.813644 513.6722l325.92126 0l0 36.44098l-325.92126 0z" fill-rule="nonzero"></path><path fill="#38761d" d="m110.397385 535.4722l0 -9.3125l3.203125 0q1.09375 0 1.65625 0.140625q0.8125 0.1875 1.375 0.671875q0.734375 0.609375 1.09375 1.578125q0.375 0.96875 0.375 2.21875q0 1.0625 -0.25 1.890625q-0.25 0.8125 -0.640625 1.34375q-0.390625 0.53125 -0.859375 0.84375q-0.453125 0.3125 -1.109375 0.46875q-0.640625 0.15625 -1.484375 0.15625l-3.359375 0zm1.234375 -1.09375l1.984375 0q0.921875 0 1.4375 -0.171875q0.53125 -0.171875 0.84375 -0.484375q0.4375 -0.4375 0.671875 -1.171875q0.25 -0.75 0.25 -1.796875q0 -1.46875 -0.484375 -2.25q-0.46875 -0.78125 -1.15625 -1.046875q-0.5 -0.1875 -1.59375 -0.1875l-1.953125 0l0 7.109375zm12.859528 -1.078125l1.1875 0.140625q-0.28125 1.046875 -1.046875 1.625q-0.75 0.5625 -1.921875 0.5625q-1.484375 0 -2.359375 -0.90625q-0.859375 -0.921875 -0.859375 -2.5625q0 -1.703125 0.875 -2.640625q0.890625 -0.9375 2.28125 -0.9375q1.359375 0 2.203125 0.921875q0.859375 0.921875 0.859375 2.578125q0 0.109375 0 0.3125l-5.03125 0q0.0625 1.109375 0.625 1.703125q0.5625 0.59375 1.40625 0.59375q0.640625 0 1.078125 -0.328125q0.453125 -0.34375 0.703125 -1.0625zm-3.75 -1.84375l3.765625 0q-0.078125 -0.859375 -0.4375 -1.28125q-0.546875 -0.65625 -1.40625 -0.65625q-0.796875 0 -1.328125 0.53125q-0.53125 0.515625 -0.59375 1.40625zm9.053101 3.0l0.15625 1.0q-0.484375 0.109375 -0.859375 0.109375q-0.625 0 -0.96875 -0.203125q-0.34375 -0.203125 -0.484375 -0.515625q-0.140625 -0.328125 -0.140625 -1.34375l0 -3.890625l-0.828125 0l0 -0.875l0.828125 0l0 -1.671875l1.140625 -0.6875l0 2.359375l1.15625 0l0 0.875l-1.15625 0l0 3.953125q0 0.484375 0.0625 0.625q0.0625 0.140625 0.1875 0.21875q0.140625 0.078125 0.390625 0.078125q0.203125 0 0.515625 -0.03125zm5.8123627 -1.15625l1.1875 0.140625q-0.28125 1.046875 -1.046875 1.625q-0.75 0.5625 -1.921875 0.5625q-1.484375 0 -2.359375 -0.90625q-0.859375 -0.921875 -0.859375 -2.5625q0 -1.703125 0.875 -2.640625q0.890625 -0.9375 2.28125 -0.9375q1.359375 0 2.203125 0.921875q0.859375 0.921875 0.859375 2.578125q0 0.109375 0 0.3125l-5.03125 0q0.0625 1.109375 0.625 1.703125q0.5625 0.59375 1.40625 0.59375q0.640625 0 1.078125 -0.328125q0.453125 -0.34375 0.703125 -1.0625zm-3.75 -1.84375l3.765625 0q-0.078125 -0.859375 -0.4375 -1.28125q-0.546875 -0.65625 -1.40625 -0.65625q-0.796875 0 -1.328125 0.53125q-0.53125 0.515625 -0.59375 1.40625zm6.5374756 4.015625l0 -6.734375l1.03125 0l0 1.015625q0.390625 -0.71875 0.71875 -0.9375q0.34375 -0.234375 0.734375 -0.234375q0.578125 0 1.171875 0.359375l-0.390625 1.0625q-0.421875 -0.25 -0.828125 -0.25q-0.375 0 -0.6875 0.234375q-0.296875 0.21875 -0.421875 0.625q-0.1875 0.609375 -0.1875 1.328125l0 3.53125l-1.140625 0zm4.4539948 0l0 -6.734375l1.015625 0l0 0.9375q0.328125 -0.5 0.84375 -0.796875q0.53125 -0.296875 1.203125 -0.296875q0.75 0 1.21875 0.3125q0.484375 0.3125 0.6875 0.859375q0.796875 -1.171875 2.078125 -1.171875q1.0 0 1.53125 0.5625q0.546875 0.546875 0.546875 1.703125l0 4.625l-1.125 0l0 -4.25q0 -0.6875 -0.109375 -0.984375q-0.109375 -0.296875 -0.40625 -0.484375q-0.296875 -0.1875 -0.6875 -0.1875q-0.71875 0 -1.1875 0.484375q-0.46875 0.46875 -0.46875 1.5l0 3.921875l-1.140625 0l0 -4.375q0 -0.765625 -0.28125 -1.140625q-0.28125 -0.390625 -0.90625 -0.390625q-0.484375 0 -0.890625 0.265625q-0.40625 0.25 -0.59375 0.734375q-0.1875 0.484375 -0.1875 1.40625l0 3.5l-1.140625 0zm11.102432 -7.984375l0 -1.328125l1.140625 0l0 1.328125l-1.140625 0zm0 7.984375l0 -6.734375l1.140625 0l0 6.734375l-1.140625 0zm2.96109 0l0 -6.734375l1.03125 0l0 0.953125q0.734375 -1.109375 2.140625 -1.109375q0.609375 0 1.109375 0.21875q0.515625 0.21875 0.765625 0.578125q0.265625 0.34375 0.359375 0.84375q0.0625 0.3125 0.0625 1.109375l0 4.140625l-1.140625 0l0 -4.09375q0 -0.703125 -0.140625 -1.046875q-0.125 -0.34375 -0.46875 -0.546875q-0.328125 -0.21875 -0.78125 -0.21875q-0.734375 0 -1.265625 0.46875q-0.53125 0.453125 -0.53125 1.75l0 3.6875l-1.140625 0zm12.021851 -2.171875l1.1875 0.140625q-0.28125 1.046875 -1.046875 1.625q-0.75 0.5625 -1.921875 0.5625q-1.484375 0 -2.359375 -0.90625q-0.859375 -0.921875 -0.859375 -2.5625q0 -1.703125 0.875 -2.640625q0.890625 -0.9375 2.28125 -0.9375q1.359375 0 2.203125 0.921875q0.859375 0.921875 0.859375 2.578125q0 0.109375 0 0.3125l-5.03125 0q0.0625 1.109375 0.625 1.703125q0.5625 0.59375 1.40625 0.59375q0.640625 0 1.078125 -0.328125q0.453125 -0.34375 0.703125 -1.0625zm-3.75 -1.84375l3.765625 0q-0.078125 -0.859375 -0.4375 -1.28125q-0.546875 -0.65625 -1.40625 -0.65625q-0.796875 0 -1.328125 0.53125q-0.53125 0.515625 -0.59375 1.40625zm12.756088 3.0l0.15625 1.0q-0.484375 0.109375 -0.859375 0.109375q-0.625 0 -0.96875 -0.203125q-0.34375 -0.203125 -0.484375 -0.515625q-0.140625 -0.328125 -0.140625 -1.34375l0 -3.890625l-0.828125 0l0 -0.875l0.828125 0l0 -1.671875l1.140625 -0.6875l0 2.359375l1.15625 0l0 0.875l-1.15625 0l0 3.953125q0 0.484375 0.0625 0.625q0.0625 0.140625 0.1875 0.21875q0.140625 0.078125 0.390625 0.078125q0.203125 0 0.515625 -0.03125zm5.5936127 0.1875q-0.625 0.53125 -1.21875 0.765625q-0.578125 0.21875 -1.25 0.21875q-1.125 0 -1.71875 -0.546875q-0.59375 -0.546875 -0.59375 -1.390625q0 -0.484375 0.21875 -0.890625q0.234375 -0.421875 0.59375 -0.671875q0.375 -0.25 0.828125 -0.375q0.328125 -0.078125 1.015625 -0.171875q1.375 -0.15625 2.03125 -0.390625q0.015625 -0.234375 0.015625 -0.296875q0 -0.703125 -0.328125 -0.984375q-0.4375 -0.390625 -1.296875 -0.390625q-0.8125 0 -1.203125 0.28125q-0.375 0.28125 -0.5625 1.0l-1.109375 -0.140625q0.140625 -0.71875 0.484375 -1.15625q0.359375 -0.453125 1.015625 -0.6875q0.671875 -0.234375 1.53125 -0.234375q0.875 0 1.40625 0.203125q0.546875 0.203125 0.796875 0.515625q0.25 0.296875 0.359375 0.765625q0.046875 0.296875 0.046875 1.0625l0 1.515625q0 1.59375 0.078125 2.015625q0.078125 0.421875 0.28125 0.8125l-1.1875 0q-0.171875 -0.359375 -0.234375 -0.828125zm-0.09375 -2.5625q-0.625 0.265625 -1.859375 0.4375q-0.703125 0.109375 -1.0 0.234375q-0.296875 0.125 -0.453125 0.375q-0.15625 0.234375 -0.15625 0.53125q0 0.453125 0.34375 0.765625q0.34375 0.296875 1.015625 0.296875q0.65625 0 1.171875 -0.28125q0.515625 -0.296875 0.765625 -0.796875q0.171875 -0.375 0.171875 -1.140625l0 -0.421875zm2.6624756 1.375l1.125 -0.171875q0.09375 0.671875 0.53125 1.046875q0.4375 0.359375 1.21875 0.359375q0.78125 0 1.15625 -0.3125q0.390625 -0.328125 0.390625 -0.765625q0 -0.390625 -0.34375 -0.609375q-0.234375 -0.15625 -1.171875 -0.390625q-1.25 -0.3125 -1.734375 -0.546875q-0.484375 -0.234375 -0.734375 -0.640625q-0.25 -0.40625 -0.25 -0.90625q0 -0.453125 0.203125 -0.828125q0.203125 -0.390625 0.5625 -0.640625q0.265625 -0.203125 0.71875 -0.328125q0.46875 -0.140625 1.0 -0.140625q0.78125 0 1.375 0.234375q0.609375 0.21875 0.890625 0.609375q0.296875 0.390625 0.40625 1.046875l-1.125 0.15625q-0.078125 -0.53125 -0.4375 -0.8125q-0.359375 -0.296875 -1.03125 -0.296875q-0.78125 0 -1.125 0.265625q-0.34375 0.25 -0.34375 0.609375q0 0.21875 0.140625 0.390625q0.140625 0.1875 0.4375 0.3125q0.171875 0.0625 1.015625 0.28125q1.21875 0.328125 1.6875 0.53125q0.484375 0.203125 0.75 0.609375q0.28125 0.390625 0.28125 0.96875q0 0.578125 -0.34375 1.078125q-0.328125 0.5 -0.953125 0.78125q-0.625 0.28125 -1.421875 0.28125q-1.3125 0 -2.0 -0.546875q-0.6875 -0.546875 -0.875 -1.625zm7.1171875 2.015625l0 -9.3125l1.140625 0l0 5.3125l2.703125 -2.734375l1.484375 0l-2.578125 2.5l2.84375 4.234375l-1.40625 0l-2.234375 -3.453125l-0.8125 0.78125l0 2.671875l-1.140625 0zm6.2109375 -2.015625l1.125 -0.171875q0.09375 0.671875 0.53125 1.046875q0.4375 0.359375 1.21875 0.359375q0.78125 0 1.15625 -0.3125q0.390625 -0.328125 0.390625 -0.765625q0 -0.390625 -0.34375 -0.609375q-0.234375 -0.15625 -1.171875 -0.390625q-1.25 -0.3125 -1.734375 -0.546875q-0.484375 -0.234375 -0.734375 -0.640625q-0.25 -0.40625 -0.25 -0.90625q0 -0.453125 0.203125 -0.828125q0.203125 -0.390625 0.5625 -0.640625q0.265625 -0.203125 0.71875 -0.328125q0.46875 -0.140625 1.0 -0.140625q0.78125 0 1.375 0.234375q0.609375 0.21875 0.890625 0.609375q0.296875 0.390625 0.40625 1.046875l-1.125 0.15625q-0.078125 -0.53125 -0.4375 -0.8125q-0.359375 -0.296875 -1.03125 -0.296875q-0.78125 0 -1.125 0.265625q-0.34375 0.25 -0.34375 0.609375q0 0.21875 0.140625 0.390625q0.140625 0.1875 0.4375 0.3125q0.171875 0.0625 1.015625 0.28125q1.21875 0.328125 1.6875 0.53125q0.484375 0.203125 0.75 0.609375q0.28125 0.390625 0.28125 0.96875q0 0.578125 -0.34375 1.078125q-0.328125 0.5 -0.953125 0.78125q-0.625 0.28125 -1.421875 0.28125q-1.3125 0 -2.0 -0.546875q-0.6875 -0.546875 -0.875 -1.625zm11.0858 2.015625l0 -5.859375l-1.0 0l0 -0.875l1.0 0l0 -0.71875q0 -0.6875 0.125 -1.015625q0.171875 -0.4375 0.578125 -0.71875q0.421875 -0.28125 1.171875 -0.28125q0.484375 0 1.0625 0.125l-0.171875 0.984375q-0.359375 -0.0625 -0.671875 -0.0625q-0.515625 0 -0.734375 0.234375q-0.21875 0.21875 -0.21875 0.828125l0 0.625l1.3125 0l0 0.875l-1.3125 0l0 5.859375l-1.140625 0zm3.0154877 -3.375q0 -1.875 1.03125 -2.765625q0.875 -0.75 2.125 -0.75q1.390625 0 2.265625 0.90625q0.890625 0.90625 0.890625 2.515625q0 1.296875 -0.390625 2.046875q-0.390625 0.75 -1.140625 1.171875q-0.75 0.40625 -1.625 0.40625q-1.421875 0 -2.296875 -0.90625q-0.859375 -0.90625 -0.859375 -2.625zm1.171875 0q0 1.296875 0.5625 1.953125q0.5625 0.640625 1.421875 0.640625q0.84375 0 1.40625 -0.640625q0.578125 -0.65625 0.578125 -1.984375q0 -1.25 -0.578125 -1.890625q-0.5625 -0.65625 -1.40625 -0.65625q-0.859375 0 -1.421875 0.640625q-0.5625 0.640625 -0.5625 1.9375zm6.6468506 3.375l0 -6.734375l1.03125 0l0 1.015625q0.390625 -0.71875 0.71875 -0.9375q0.34375 -0.234375 0.734375 -0.234375q0.578125 0 1.171875 0.359375l-0.390625 1.0625q-0.421875 -0.25 -0.828125 -0.25q-0.375 0 -0.6875 0.234375q-0.296875 0.21875 -0.421875 0.625q-0.1875 0.609375 -0.1875 1.328125l0 3.53125l-1.140625 0zm12.766357 -2.171875l1.1875 0.140625q-0.28125 1.046875 -1.046875 1.625q-0.75 0.5625 -1.921875 0.5625q-1.484375 0 -2.359375 -0.90625q-0.859375 -0.921875 -0.859375 -2.5625q0 -1.703125 0.875 -2.640625q0.890625 -0.9375 2.28125 -0.9375q1.359375 0 2.203125 0.921875q0.859375 0.921875 0.859375 2.578125q0 0.109375 0 0.3125l-5.03125 0q0.0625 1.109375 0.625 1.703125q0.5625 0.59375 1.40625 0.59375q0.640625 0 1.078125 -0.328125q0.453125 -0.34375 0.703125 -1.0625zm-3.75 -1.84375l3.765625 0q-0.078125 -0.859375 -0.4375 -1.28125q-0.546875 -0.65625 -1.40625 -0.65625q-0.796875 0 -1.328125 0.53125q-0.53125 0.515625 -0.59375 1.40625zm10.943726 3.1875q-0.625 0.53125 -1.21875 0.765625q-0.578125 0.21875 -1.25 0.21875q-1.125 0 -1.71875 -0.546875q-0.59375 -0.546875 -0.59375 -1.390625q0 -0.484375 0.21875 -0.890625q0.234375 -0.421875 0.59375 -0.671875q0.375 -0.25 0.828125 -0.375q0.328125 -0.078125 1.015625 -0.171875q1.375 -0.15625 2.03125 -0.390625q0.015625 -0.234375 0.015625 -0.296875q0 -0.703125 -0.328125 -0.984375q-0.4375 -0.390625 -1.296875 -0.390625q-0.8125 0 -1.203125 0.28125q-0.375 0.28125 -0.5625 1.0l-1.109375 -0.140625q0.140625 -0.71875 0.484375 -1.15625q0.359375 -0.453125 1.015625 -0.6875q0.671875 -0.234375 1.53125 -0.234375q0.875 0 1.40625 0.203125q0.546875 0.203125 0.796875 0.515625q0.25 0.296875 0.359375 0.765625q0.046875 0.296875 0.046875 1.0625l0 1.515625q0 1.59375 0.078125 2.015625q0.078125 0.421875 0.28125 0.8125l-1.1875 0q-0.171875 -0.359375 -0.234375 -0.828125zm-0.09375 -2.5625q-0.625 0.265625 -1.859375 0.4375q-0.703125 0.109375 -1.0 0.234375q-0.296875 0.125 -0.453125 0.375q-0.15625 0.234375 -0.15625 0.53125q0 0.453125 0.34375 0.765625q0.34375 0.296875 1.015625 0.296875q0.65625 0 1.171875 -0.28125q0.515625 -0.296875 0.765625 -0.796875q0.171875 -0.375 0.171875 -1.140625l0 -0.421875zm7.5062256 0.921875l1.125 0.140625q-0.171875 1.171875 -0.9375 1.828125q-0.765625 0.65625 -1.859375 0.65625q-1.390625 0 -2.234375 -0.90625q-0.828125 -0.90625 -0.828125 -2.59375q0 -1.09375 0.359375 -1.90625q0.359375 -0.828125 1.09375 -1.234375q0.734375 -0.40625 1.609375 -0.40625q1.09375 0 1.796875 0.5625q0.703125 0.546875 0.890625 1.5625l-1.109375 0.171875q-0.15625 -0.671875 -0.5625 -1.015625q-0.390625 -0.34375 -0.96875 -0.34375q-0.859375 0 -1.40625 0.625q-0.53125 0.609375 -0.53125 1.953125q0 1.359375 0.515625 1.984375q0.515625 0.609375 1.359375 0.609375q0.671875 0 1.125 -0.40625q0.453125 -0.421875 0.5625 -1.28125zm2.2734375 2.46875l0 -9.3125l1.140625 0l0 3.34375q0.796875 -0.921875 2.015625 -0.921875q0.75 0 1.296875 0.296875q0.5625 0.296875 0.796875 0.8125q0.234375 0.515625 0.234375 1.515625l0 4.265625l-1.140625 0l0 -4.265625q0 -0.859375 -0.375 -1.25q-0.359375 -0.390625 -1.046875 -0.390625q-0.5 0 -0.953125 0.265625q-0.453125 0.25 -0.640625 0.703125q-0.1875 0.453125 -0.1875 1.25l0 3.6875l-1.140625 0zm10.662323 -2.015625l1.125 -0.171875q0.09375 0.671875 0.53125 1.046875q0.4375 0.359375 1.21875 0.359375q0.78125 0 1.15625 -0.3125q0.390625 -0.328125 0.390625 -0.765625q0 -0.390625 -0.34375 -0.609375q-0.234375 -0.15625 -1.171875 -0.390625q-1.25 -0.3125 -1.734375 -0.546875q-0.484375 -0.234375 -0.734375 -0.640625q-0.25 -0.40625 -0.25 -0.90625q0 -0.453125 0.203125 -0.828125q0.203125 -0.390625 0.5625 -0.640625q0.265625 -0.203125 0.71875 -0.328125q0.46875 -0.140625 1.0 -0.140625q0.78125 0 1.375 0.234375q0.609375 0.21875 0.890625 0.609375q0.296875 0.390625 0.40625 1.046875l-1.125 0.15625q-0.078125 -0.53125 -0.4375 -0.8125q-0.359375 -0.296875 -1.03125 -0.296875q-0.78125 0 -1.125 0.265625q-0.34375 0.25 -0.34375 0.609375q0 0.21875 0.140625 0.390625q0.140625 0.1875 0.4375 0.3125q0.171875 0.0625 1.015625 0.28125q1.21875 0.328125 1.6875 0.53125q0.484375 0.203125 0.75 0.609375q0.28125 0.390625 0.28125 0.96875q0 0.578125 -0.34375 1.078125q-0.328125 0.5 -0.953125 0.78125q-0.625 0.28125 -1.421875 0.28125q-1.3125 0 -2.0 -0.546875q-0.6875 -0.546875 -0.875 -1.625zm6.6953125 -1.359375q0 -1.875 1.03125 -2.765625q0.875 -0.75 2.125 -0.75q1.390625 0 2.265625 0.90625q0.890625 0.90625 0.890625 2.515625q0 1.296875 -0.390625 2.046875q-0.390625 0.75 -1.140625 1.171875q-0.75 0.40625 -1.625 0.40625q-1.421875 0 -2.296875 -0.90625q-0.859375 -0.90625 -0.859375 -2.625zm1.171875 0q0 1.296875 0.5625 1.953125q0.5625 0.640625 1.421875 0.640625q0.84375 0 1.40625 -0.640625q0.578125 -0.65625 0.578125 -1.984375q0 -1.25 -0.578125 -1.890625q-0.5625 -0.65625 -1.40625 -0.65625q-0.859375 0 -1.421875 0.640625q-0.5625 0.640625 -0.5625 1.9375zm11.084351 3.375l0 -0.984375q-0.796875 1.140625 -2.140625 1.140625q-0.59375 0 -1.125 -0.234375q-0.515625 -0.234375 -0.765625 -0.578125q-0.25 -0.34375 -0.34375 -0.84375q-0.078125 -0.328125 -0.078125 -1.0625l0 -4.171875l1.140625 0l0 3.734375q0 0.890625 0.078125 1.203125q0.109375 0.453125 0.453125 0.71875q0.34375 0.25 0.859375 0.25q0.515625 0 0.96875 -0.265625q0.453125 -0.265625 0.640625 -0.71875q0.1875 -0.453125 0.1875 -1.3125l0 -3.609375l1.140625 0l0 6.734375l-1.015625 0zm2.9749756 0l0 -6.734375l1.03125 0l0 1.015625q0.390625 -0.71875 0.71875 -0.9375q0.34375 -0.234375 0.734375 -0.234375q0.578125 0 1.171875 0.359375l-0.390625 1.0625q-0.421875 -0.25 -0.828125 -0.25q-0.375 0 -0.6875 0.234375q-0.296875 0.21875 -0.421875 0.625q-0.1875 0.609375 -0.1875 1.328125l0 3.53125l-1.140625 0zm8.844635 -2.46875l1.125 0.140625q-0.171875 1.171875 -0.9375 1.828125q-0.765625 0.65625 -1.859375 0.65625q-1.390625 0 -2.234375 -0.90625q-0.828125 -0.90625 -0.828125 -2.59375q0 -1.09375 0.359375 -1.90625q0.359375 -0.828125 1.09375 -1.234375q0.734375 -0.40625 1.609375 -0.40625q1.09375 0 1.796875 0.5625q0.703125 0.546875 0.890625 1.5625l-1.109375 0.171875q-0.15625 -0.671875 -0.5625 -1.015625q-0.390625 -0.34375 -0.96875 -0.34375q-0.859375 0 -1.40625 0.625q-0.53125 0.609375 -0.53125 1.953125q0 1.359375 0.515625 1.984375q0.515625 0.609375 1.359375 0.609375q0.671875 0 1.125 -0.40625q0.453125 -0.421875 0.5625 -1.28125zm6.8828125 0.296875l1.1875 0.140625q-0.28125 1.046875 -1.046875 1.625q-0.75 0.5625 -1.921875 0.5625q-1.484375 0 -2.359375 -0.90625q-0.859375 -0.921875 -0.859375 -2.5625q0 -1.703125 0.875 -2.640625q0.890625 -0.9375 2.28125 -0.9375q1.359375 0 2.203125 0.921875q0.859375 0.921875 0.859375 2.578125q0 0.109375 0 0.3125l-5.03125 0q0.0625 1.109375 0.625 1.703125q0.5625 0.59375 1.40625 0.59375q0.640625 0 1.078125 -0.328125q0.453125 -0.34375 0.703125 -1.0625zm-3.75 -1.84375l3.765625 0q-0.078125 -0.859375 -0.4375 -1.28125q-0.546875 -0.65625 -1.40625 -0.65625q-0.796875 0 -1.328125 0.53125q-0.53125 0.515625 -0.59375 1.40625zm14.677948 4.015625l0 -0.984375q-0.796875 1.140625 -2.140625 1.140625q-0.59375 0 -1.125 -0.234375q-0.515625 -0.234375 -0.765625 -0.578125q-0.25 -0.34375 -0.34375 -0.84375q-0.078125 -0.328125 -0.078125 -1.0625l0 -4.171875l1.140625 0l0 3.734375q0 0.890625 0.078125 1.203125q0.109375 0.453125 0.453125 0.71875q0.34375 0.25 0.859375 0.25q0.515625 0 0.96875 -0.265625q0.453125 -0.265625 0.640625 -0.71875q0.1875 -0.453125 0.1875 -1.3125l0 -3.609375l1.140625 0l0 6.734375l-1.015625 0zm2.9906006 0l0 -6.734375l1.03125 0l0 0.953125q0.734375 -1.109375 2.140625 -1.109375q0.609375 0 1.109375 0.21875q0.515625 0.21875 0.765625 0.578125q0.265625 0.34375 0.359375 0.84375q0.0625 0.3125 0.0625 1.109375l0 4.140625l-1.140625 0l0 -4.09375q0 -0.703125 -0.140625 -1.046875q-0.125 -0.34375 -0.46875 -0.546875q-0.328125 -0.21875 -0.78125 -0.21875q-0.734375 0 -1.265625 0.46875q-0.53125 0.453125 -0.53125 1.75l0 3.6875l-1.140625 0zm7.4124756 -7.984375l0 -1.328125l1.140625 0l0 1.328125l-1.140625 0zm0 7.984375l0 -6.734375l1.140625 0l0 6.734375l-1.140625 0zm5.46109 -1.015625l0.15625 1.0q-0.484375 0.109375 -0.859375 0.109375q-0.625 0 -0.96875 -0.203125q-0.34375 -0.203125 -0.484375 -0.515625q-0.140625 -0.328125 -0.140625 -1.34375l0 -3.890625l-0.828125 0l0 -0.875l0.828125 0l0 -1.671875l1.140625 -0.6875l0 2.359375l1.15625 0l0 0.875l-1.15625 0l0 3.953125q0 0.484375 0.0625 0.625q0.0625 0.140625 0.1875 0.21875q0.140625 0.078125 0.390625 0.078125q0.203125 0 0.515625 -0.03125zm1.5154724 -4.421875l0 -1.296875l1.296875 0l0 1.296875l-1.296875 0zm0 5.4375l0 -1.296875l1.296875 0l0 1.296875l-1.296875 0z" fill-rule="nonzero"></path><path fill="#000000" fill-opacity="0.0" d="m56.737526 743.2906l325.92126 0l0 36.44098l-325.92126 0z" fill-rule="nonzero"></path><path fill="#38761d" d="m119.93274 761.825l1.234375 0.3125q-0.390625 1.515625 -1.40625 2.3125q-1.0 0.796875 -2.453125 0.796875q-1.5 0 -2.453125 -0.609375q-0.9375 -0.609375 -1.4375 -1.765625q-0.484375 -1.171875 -0.484375 -2.5q0 -1.453125 0.5625 -2.53125q0.5625 -1.09375 1.578125 -1.65625q1.03125 -0.5625 2.265625 -0.5625q1.390625 0 2.34375 0.71875q0.953125 0.703125 1.328125 2.0l-1.21875 0.28125q-0.328125 -1.015625 -0.9375 -1.46875q-0.609375 -0.46875 -1.546875 -0.46875q-1.078125 0 -1.796875 0.515625q-0.71875 0.515625 -1.015625 1.375q-0.28125 0.859375 -0.28125 1.78125q0 1.1875 0.34375 2.078125q0.34375 0.890625 1.0625 1.328125q0.734375 0.4375 1.59375 0.4375q1.03125 0 1.75 -0.59375q0.71875 -0.609375 0.96875 -1.78125zm2.4220276 -0.109375q0 -1.875 1.03125 -2.765625q0.875 -0.75 2.125 -0.75q1.390625 0 2.265625 0.90625q0.890625 0.90625 0.890625 2.515625q0 1.296875 -0.390625 2.046875q-0.390625 0.75 -1.140625 1.171875q-0.75 0.40625 -1.625 0.40625q-1.421875 0 -2.296875 -0.90625q-0.859375 -0.90625 -0.859375 -2.625zm1.171875 0q0 1.296875 0.5625 1.953125q0.5625 0.640625 1.421875 0.640625q0.84375 0 1.40625 -0.640625q0.578125 -0.65625 0.578125 -1.984375q0 -1.25 -0.578125 -1.890625q-0.5625 -0.65625 -1.40625 -0.65625q-0.859375 0 -1.421875 0.640625q-0.5625 0.640625 -0.5625 1.9375zm6.6624756 3.375l0 -6.734375l1.015625 0l0 0.9375q0.328125 -0.5 0.84375 -0.796875q0.53125 -0.296875 1.203125 -0.296875q0.75 0 1.21875 0.3125q0.484375 0.3125 0.6875 0.859375q0.796875 -1.171875 2.078125 -1.171875q1.0 0 1.53125 0.5625q0.546875 0.546875 0.546875 1.703125l0 4.625l-1.125 0l0 -4.25q0 -0.6875 -0.109375 -0.984375q-0.109375 -0.296875 -0.40625 -0.484375q-0.296875 -0.1875 -0.6875 -0.1875q-0.71875 0 -1.1875 0.484375q-0.46875 0.46875 -0.46875 1.5l0 3.921875l-1.140625 0l0 -4.375q0 -0.765625 -0.28125 -1.140625q-0.28125 -0.390625 -0.90625 -0.390625q-0.484375 0 -0.890625 0.265625q-0.40625 0.25 -0.59375 0.734375q-0.1875 0.484375 -0.1875 1.40625l0 3.5l-1.140625 0zm12.149307 0l-1.0625 0l0 -9.3125l1.15625 0l0 3.328125q0.71875 -0.90625 1.84375 -0.90625q0.625 0 1.171875 0.25q0.5625 0.25 0.921875 0.703125q0.359375 0.453125 0.5625 1.09375q0.203125 0.640625 0.203125 1.375q0 1.734375 -0.859375 2.6875q-0.859375 0.9375 -2.0625 0.9375q-1.1875 0 -1.875 -1.0l0 0.84375zm-0.015625 -3.421875q0 1.21875 0.34375 1.75q0.53125 0.890625 1.453125 0.890625q0.75 0 1.296875 -0.65625q0.546875 -0.65625 0.546875 -1.9375q0 -1.328125 -0.53125 -1.953125q-0.515625 -0.625 -1.265625 -0.625q-0.75 0 -1.296875 0.65625q-0.546875 0.640625 -0.546875 1.875zm6.3812256 -4.5625l0 -1.328125l1.140625 0l0 1.328125l-1.140625 0zm0 7.984375l0 -6.734375l1.140625 0l0 6.734375l-1.140625 0zm2.96109 0l0 -6.734375l1.03125 0l0 0.953125q0.734375 -1.109375 2.140625 -1.109375q0.609375 0 1.109375 0.21875q0.515625 0.21875 0.765625 0.578125q0.265625 0.34375 0.359375 0.84375q0.0625 0.3125 0.0625 1.109375l0 4.140625l-1.140625 0l0 -4.09375q0 -0.703125 -0.140625 -1.046875q-0.125 -0.34375 -0.46875 -0.546875q-0.328125 -0.21875 -0.78125 -0.21875q-0.734375 0 -1.265625 0.46875q-0.53125 0.453125 -0.53125 1.75l0 3.6875l-1.140625 0zm12.021851 -2.171875l1.1875 0.140625q-0.28125 1.046875 -1.046875 1.625q-0.75 0.5625 -1.921875 0.5625q-1.484375 0 -2.359375 -0.90625q-0.859375 -0.921875 -0.859375 -2.5625q0 -1.703125 0.875 -2.640625q0.890625 -0.9375 2.28125 -0.9375q1.359375 0 2.203125 0.921875q0.859375 0.921875 0.859375 2.578125q0 0.109375 0 0.3125l-5.03125 0q0.0625 1.109375 0.625 1.703125q0.5625 0.59375 1.40625 0.59375q0.640625 0 1.078125 -0.328125q0.453125 -0.34375 0.703125 -1.0625zm-3.75 -1.84375l3.765625 0q-0.078125 -0.859375 -0.4375 -1.28125q-0.546875 -0.65625 -1.40625 -0.65625q-0.796875 0 -1.328125 0.53125q-0.53125 0.515625 -0.59375 1.40625zm12.756088 3.0l0.15625 1.0q-0.484375 0.109375 -0.859375 0.109375q-0.625 0 -0.96875 -0.203125q-0.34375 -0.203125 -0.484375 -0.515625q-0.140625 -0.328125 -0.140625 -1.34375l0 -3.890625l-0.828125 0l0 -0.875l0.828125 0l0 -1.671875l1.140625 -0.6875l0 2.359375l1.15625 0l0 0.875l-1.15625 0l0 3.953125q0 0.484375 0.0625 0.625q0.0625 0.140625 0.1875 0.21875q0.140625 0.078125 0.390625 0.078125q0.203125 0 0.515625 -0.03125zm5.5936127 0.1875q-0.625 0.53125 -1.21875 0.765625q-0.578125 0.21875 -1.25 0.21875q-1.125 0 -1.71875 -0.546875q-0.59375 -0.546875 -0.59375 -1.390625q0 -0.484375 0.21875 -0.890625q0.234375 -0.421875 0.59375 -0.671875q0.375 -0.25 0.828125 -0.375q0.328125 -0.078125 1.015625 -0.171875q1.375 -0.15625 2.03125 -0.390625q0.015625 -0.234375 0.015625 -0.296875q0 -0.703125 -0.328125 -0.984375q-0.4375 -0.390625 -1.296875 -0.390625q-0.8125 0 -1.203125 0.28125q-0.375 0.28125 -0.5625 1.0l-1.109375 -0.140625q0.140625 -0.71875 0.484375 -1.15625q0.359375 -0.453125 1.015625 -0.6875q0.671875 -0.234375 1.53125 -0.234375q0.875 0 1.40625 0.203125q0.546875 0.203125 0.796875 0.515625q0.25 0.296875 0.359375 0.765625q0.046875 0.296875 0.046875 1.0625l0 1.515625q0 1.59375 0.078125 2.015625q0.078125 0.421875 0.28125 0.8125l-1.1875 0q-0.171875 -0.359375 -0.234375 -0.828125zm-0.09375 -2.5625q-0.625 0.265625 -1.859375 0.4375q-0.703125 0.109375 -1.0 0.234375q-0.296875 0.125 -0.453125 0.375q-0.15625 0.234375 -0.15625 0.53125q0 0.453125 0.34375 0.765625q0.34375 0.296875 1.015625 0.296875q0.65625 0 1.171875 -0.28125q0.515625 -0.296875 0.765625 -0.796875q0.171875 -0.375 0.171875 -1.140625l0 -0.421875zm2.6624756 1.375l1.125 -0.171875q0.09375 0.671875 0.53125 1.046875q0.4375 0.359375 1.21875 0.359375q0.78125 0 1.15625 -0.3125q0.390625 -0.328125 0.390625 -0.765625q0 -0.390625 -0.34375 -0.609375q-0.234375 -0.15625 -1.171875 -0.390625q-1.25 -0.3125 -1.734375 -0.546875q-0.484375 -0.234375 -0.734375 -0.640625q-0.25 -0.40625 -0.25 -0.90625q0 -0.453125 0.203125 -0.828125q0.203125 -0.390625 0.5625 -0.640625q0.265625 -0.203125 0.71875 -0.328125q0.46875 -0.140625 1.0 -0.140625q0.78125 0 1.375 0.234375q0.609375 0.21875 0.890625 0.609375q0.296875 0.390625 0.40625 1.046875l-1.125 0.15625q-0.078125 -0.53125 -0.4375 -0.8125q-0.359375 -0.296875 -1.03125 -0.296875q-0.78125 0 -1.125 0.265625q-0.34375 0.25 -0.34375 0.609375q0 0.21875 0.140625 0.390625q0.140625 0.1875 0.4375 0.3125q0.171875 0.0625 1.015625 0.28125q1.21875 0.328125 1.6875 0.53125q0.484375 0.203125 0.75 0.609375q0.28125 0.390625 0.28125 0.96875q0 0.578125 -0.34375 1.078125q-0.328125 0.5 -0.953125 0.78125q-0.625 0.28125 -1.421875 0.28125q-1.3125 0 -2.0 -0.546875q-0.6875 -0.546875 -0.875 -1.625zm7.1171875 2.015625l0 -9.3125l1.140625 0l0 5.3125l2.703125 -2.734375l1.484375 0l-2.578125 2.5l2.84375 4.234375l-1.40625 0l-2.234375 -3.453125l-0.8125 0.78125l0 2.671875l-1.140625 0zm6.2109375 -2.015625l1.125 -0.171875q0.09375 0.671875 0.53125 1.046875q0.4375 0.359375 1.21875 0.359375q0.78125 0 1.15625 -0.3125q0.390625 -0.328125 0.390625 -0.765625q0 -0.390625 -0.34375 -0.609375q-0.234375 -0.15625 -1.171875 -0.390625q-1.25 -0.3125 -1.734375 -0.546875q-0.484375 -0.234375 -0.734375 -0.640625q-0.25 -0.40625 -0.25 -0.90625q0 -0.453125 0.203125 -0.828125q0.203125 -0.390625 0.5625 -0.640625q0.265625 -0.203125 0.71875 -0.328125q0.46875 -0.140625 1.0 -0.140625q0.78125 0 1.375 0.234375q0.609375 0.21875 0.890625 0.609375q0.296875 0.390625 0.40625 1.046875l-1.125 0.15625q-0.078125 -0.53125 -0.4375 -0.8125q-0.359375 -0.296875 -1.03125 -0.296875q-0.78125 0 -1.125 0.265625q-0.34375 0.25 -0.34375 0.609375q0 0.21875 0.140625 0.390625q0.140625 0.1875 0.4375 0.3125q0.171875 0.0625 1.015625 0.28125q1.21875 0.328125 1.6875 0.53125q0.484375 0.203125 0.75 0.609375q0.28125 0.390625 0.28125 0.96875q0 0.578125 -0.34375 1.078125q-0.328125 0.5 -0.953125 0.78125q-0.625 0.28125 -1.421875 0.28125q-1.3125 0 -2.0 -0.546875q-0.6875 -0.546875 -0.875 -1.625zm11.085815 2.015625l0 -5.859375l-1.0 0l0 -0.875l1.0 0l0 -0.71875q0 -0.6875 0.125 -1.015625q0.171875 -0.4375 0.578125 -0.71875q0.421875 -0.28125 1.171875 -0.28125q0.484375 0 1.0625 0.125l-0.171875 0.984375q-0.359375 -0.0625 -0.671875 -0.0625q-0.515625 0 -0.734375 0.234375q-0.21875 0.21875 -0.21875 0.828125l0 0.625l1.3125 0l0 0.875l-1.3125 0l0 5.859375l-1.140625 0zm3.4217224 0l0 -6.734375l1.03125 0l0 1.015625q0.390625 -0.71875 0.71875 -0.9375q0.34375 -0.234375 0.734375 -0.234375q0.578125 0 1.171875 0.359375l-0.390625 1.0625q-0.421875 -0.25 -0.828125 -0.25q-0.375 0 -0.6875 0.234375q-0.296875 0.21875 -0.421875 0.625q-0.1875 0.609375 -0.1875 1.328125l0 3.53125l-1.140625 0zm4.032135 -3.375q0 -1.875 1.03125 -2.765625q0.875 -0.75 2.125 -0.75q1.390625 0 2.265625 0.90625q0.890625 0.90625 0.890625 2.515625q0 1.296875 -0.390625 2.046875q-0.390625 0.75 -1.140625 1.171875q-0.75 0.40625 -1.625 0.40625q-1.421875 0 -2.296875 -0.90625q-0.859375 -0.90625 -0.859375 -2.625zm1.171875 0q0 1.296875 0.5625 1.953125q0.5625 0.640625 1.421875 0.640625q0.84375 0 1.40625 -0.640625q0.578125 -0.65625 0.578125 -1.984375q0 -1.25 -0.578125 -1.890625q-0.5625 -0.65625 -1.40625 -0.65625q-0.859375 0 -1.421875 0.640625q-0.5625 0.640625 -0.5625 1.9375zm6.6624756 3.375l0 -6.734375l1.015625 0l0 0.9375q0.328125 -0.5 0.84375 -0.796875q0.53125 -0.296875 1.203125 -0.296875q0.75 0 1.21875 0.3125q0.484375 0.3125 0.6875 0.859375q0.796875 -1.171875 2.078125 -1.171875q1.0 0 1.53125 0.5625q0.546875 0.546875 0.546875 1.703125l0 4.625l-1.125 0l0 -4.25q0 -0.6875 -0.109375 -0.984375q-0.109375 -0.296875 -0.40625 -0.484375q-0.296875 -0.1875 -0.6875 -0.1875q-0.71875 0 -1.1875 0.484375q-0.46875 0.46875 -0.46875 1.5l0 3.921875l-1.140625 0l0 -4.375q0 -0.765625 -0.28125 -1.140625q-0.28125 -0.390625 -0.90625 -0.390625q-0.484375 0 -0.890625 0.265625q-0.40625 0.25 -0.59375 0.734375q-0.1875 0.484375 -0.1875 1.40625l0 3.5l-1.140625 0zm19.196045 -0.828125q-0.625 0.53125 -1.21875 0.765625q-0.578125 0.21875 -1.25 0.21875q-1.125 0 -1.71875 -0.546875q-0.59375 -0.546875 -0.59375 -1.390625q0 -0.484375 0.21875 -0.890625q0.234375 -0.421875 0.59375 -0.671875q0.375 -0.25 0.828125 -0.375q0.328125 -0.078125 1.015625 -0.171875q1.375 -0.15625 2.03125 -0.390625q0.015625 -0.234375 0.015625 -0.296875q0 -0.703125 -0.328125 -0.984375q-0.4375 -0.390625 -1.296875 -0.390625q-0.8125 0 -1.203125 0.28125q-0.375 0.28125 -0.5625 1.0l-1.109375 -0.140625q0.140625 -0.71875 0.484375 -1.15625q0.359375 -0.453125 1.015625 -0.6875q0.671875 -0.234375 1.53125 -0.234375q0.875 0 1.40625 0.203125q0.546875 0.203125 0.796875 0.515625q0.25 0.296875 0.359375 0.765625q0.046875 0.296875 0.046875 1.0625l0 1.515625q0 1.59375 0.078125 2.015625q0.078125 0.421875 0.28125 0.8125l-1.1875 0q-0.171875 -0.359375 -0.234375 -0.828125zm-0.09375 -2.5625q-0.625 0.265625 -1.859375 0.4375q-0.703125 0.109375 -1.0 0.234375q-0.296875 0.125 -0.453125 0.375q-0.15625 0.234375 -0.15625 0.53125q0 0.453125 0.34375 0.765625q0.34375 0.296875 1.015625 0.296875q0.65625 0 1.171875 -0.28125q0.515625 -0.296875 0.765625 -0.796875q0.171875 -0.375 0.171875 -1.140625l0 -0.421875zm3.0843506 3.390625l0 -9.3125l1.140625 0l0 9.3125l-1.140625 0zm2.96109 0l0 -9.3125l1.140625 0l0 9.3125l-1.140625 0zm6.2421875 -2.015625l1.125 -0.171875q0.09375 0.671875 0.53125 1.046875q0.4375 0.359375 1.21875 0.359375q0.78125 0 1.15625 -0.3125q0.39060974 -0.328125 0.39060974 -0.765625q0 -0.390625 -0.34375 -0.609375q-0.23435974 -0.15625 -1.1718597 -0.390625q-1.25 -0.3125 -1.734375 -0.546875q-0.484375 -0.234375 -0.734375 -0.640625q-0.25 -0.40625 -0.25 -0.90625q0 -0.453125 0.203125 -0.828125q0.203125 -0.390625 0.5625 -0.640625q0.265625 -0.203125 0.71875 -0.328125q0.46875 -0.140625 1.0 -0.140625q0.78125 0 1.375 0.234375q0.60935974 0.21875 0.89060974 0.609375q0.296875 0.390625 0.40625 1.046875l-1.125 0.15625q-0.078125 -0.53125 -0.43748474 -0.8125q-0.359375 -0.296875 -1.03125 -0.296875q-0.78125 0 -1.125 0.265625q-0.34375 0.25 -0.34375 0.609375q0 0.21875 0.140625 0.390625q0.140625 0.1875 0.4375 0.3125q0.171875 0.0625 1.015625 0.28125q1.2187347 0.328125 1.6874847 0.53125q0.484375 0.203125 0.75 0.609375q0.28125 0.390625 0.28125 0.96875q0 0.578125 -0.34375 1.078125q-0.328125 0.5 -0.953125 0.78125q-0.62498474 0.28125 -1.4218597 0.28125q-1.3125 0 -2.0 -0.546875q-0.6875 -0.546875 -0.875 -1.625zm6.6952972 -1.359375q0 -1.875 1.03125 -2.765625q0.875 -0.75 2.125 -0.75q1.390625 0 2.265625 0.90625q0.890625 0.90625 0.890625 2.515625q0 1.296875 -0.390625 2.046875q-0.390625 0.75 -1.140625 1.171875q-0.75 0.40625 -1.625 0.40625q-1.421875 0 -2.296875 -0.90625q-0.859375 -0.90625 -0.859375 -2.625zm1.171875 0q0 1.296875 0.5625 1.953125q0.5625 0.640625 1.421875 0.640625q0.84375 0 1.40625 -0.640625q0.578125 -0.65625 0.578125 -1.984375q0 -1.25 -0.578125 -1.890625q-0.5625 -0.65625 -1.40625 -0.65625q-0.859375 0 -1.421875 0.640625q-0.5625 0.640625 -0.5625 1.9375zm11.084351 3.375l0 -0.984375q-0.796875 1.140625 -2.140625 1.140625q-0.59375 0 -1.125 -0.234375q-0.515625 -0.234375 -0.765625 -0.578125q-0.25 -0.34375 -0.34375 -0.84375q-0.078125 -0.328125 -0.078125 -1.0625l0 -4.171875l1.140625 0l0 3.734375q0 0.890625 0.078125 1.203125q0.109375 0.453125 0.453125 0.71875q0.34375 0.25 0.859375 0.25q0.515625 0 0.96875 -0.265625q0.453125 -0.265625 0.640625 -0.71875q0.1875 -0.453125 0.1875 -1.3125l0 -3.609375l1.140625 0l0 6.734375l-1.015625 0zm2.9749756 0l0 -6.734375l1.03125 0l0 1.015625q0.390625 -0.71875 0.71875 -0.9375q0.34375 -0.234375 0.734375 -0.234375q0.578125 0 1.171875 0.359375l-0.390625 1.0625q-0.421875 -0.25 -0.828125 -0.25q-0.375 0 -0.6875 0.234375q-0.296875 0.21875 -0.421875 0.625q-0.1875 0.609375 -0.1875 1.328125l0 3.53125l-1.140625 0zm8.844635 -2.46875l1.125 0.140625q-0.171875 1.171875 -0.9375 1.828125q-0.765625 0.65625 -1.859375 0.65625q-1.390625 0 -2.234375 -0.90625q-0.828125 -0.90625 -0.828125 -2.59375q0 -1.09375 0.359375 -1.90625q0.359375 -0.828125 1.09375 -1.234375q0.734375 -0.40625 1.609375 -0.40625q1.09375 0 1.796875 0.5625q0.703125 0.546875 0.890625 1.5625l-1.109375 0.171875q-0.15625 -0.671875 -0.5625 -1.015625q-0.390625 -0.34375 -0.96875 -0.34375q-0.859375 0 -1.40625 0.625q-0.53125 0.609375 -0.53125 1.953125q0 1.359375 0.515625 1.984375q0.515625 0.609375 1.359375 0.609375q0.671875 0 1.125 -0.40625q0.453125 -0.421875 0.5625 -1.28125zm6.8828125 0.296875l1.1875 0.140625q-0.28125 1.046875 -1.046875 1.625q-0.75 0.5625 -1.921875 0.5625q-1.484375 0 -2.359375 -0.90625q-0.859375 -0.921875 -0.859375 -2.5625q0 -1.703125 0.875 -2.640625q0.890625 -0.9375 2.28125 -0.9375q1.359375 0 2.203125 0.921875q0.859375 0.921875 0.859375 2.578125q0 0.109375 0 0.3125l-5.03125 0q0.0625 1.109375 0.625 1.703125q0.5625 0.59375 1.40625 0.59375q0.640625 0 1.078125 -0.328125q0.453125 -0.34375 0.703125 -1.0625zm-3.75 -1.84375l3.765625 0q-0.078125 -0.859375 -0.4375 -1.28125q-0.546875 -0.65625 -1.40625 -0.65625q-0.796875 0 -1.328125 0.53125q-0.53125 0.515625 -0.59375 1.40625zm14.677948 4.015625l0 -0.984375q-0.796875 1.140625 -2.140625 1.140625q-0.59375 0 -1.125 -0.234375q-0.515625 -0.234375 -0.765625 -0.578125q-0.25 -0.34375 -0.34375 -0.84375q-0.078125 -0.328125 -0.078125 -1.0625l0 -4.171875l1.140625 0l0 3.734375q0 0.890625 0.078125 1.203125q0.109375 0.453125 0.453125 0.71875q0.34375 0.25 0.859375 0.25q0.515625 0 0.96875 -0.265625q0.453125 -0.265625 0.640625 -0.71875q0.1875 -0.453125 0.1875 -1.3125l0 -3.609375l1.140625 0l0 6.734375l-1.015625 0zm2.9906006 0l0 -6.734375l1.03125 0l0 0.953125q0.734375 -1.109375 2.140625 -1.109375q0.609375 0 1.109375 0.21875q0.515625 0.21875 0.765625 0.578125q0.265625 0.34375 0.359375 0.84375q0.0625 0.3125 0.0625 1.109375l0 4.140625l-1.140625 0l0 -4.09375q0 -0.703125 -0.140625 -1.046875q-0.125 -0.34375 -0.46875 -0.546875q-0.328125 -0.21875 -0.78125 -0.21875q-0.734375 0 -1.265625 0.46875q-0.53125 0.453125 -0.53125 1.75l0 3.6875l-1.140625 0zm7.4124756 -7.984375l0 -1.328125l1.140625 0l0 1.328125l-1.140625 0zm0 7.984375l0 -6.734375l1.140625 0l0 6.734375l-1.140625 0zm5.46109 -1.015625l0.15625 1.0q-0.484375 0.109375 -0.859375 0.109375q-0.625 0 -0.96875 -0.203125q-0.34375 -0.203125 -0.484375 -0.515625q-0.140625 -0.328125 -0.140625 -1.34375l0 -3.890625l-0.828125 0l0 -0.875l0.828125 0l0 -1.671875l1.140625 -0.6875l0 2.359375l1.15625 0l0 0.875l-1.15625 0l0 3.953125q0 0.484375 0.0625 0.625q0.0625 0.140625 0.1875 0.21875q0.140625 0.078125 0.390625 0.078125q0.203125 0 0.515625 -0.03125zm0.7498779 -1.0l1.125 -0.171875q0.09375 0.671875 0.53125 1.046875q0.4375 0.359375 1.21875 0.359375q0.78125 0 1.15625 -0.3125q0.390625 -0.328125 0.390625 -0.765625q0 -0.390625 -0.34375 -0.609375q-0.234375 -0.15625 -1.171875 -0.390625q-1.25 -0.3125 -1.734375 -0.546875q-0.484375 -0.234375 -0.734375 -0.640625q-0.25 -0.40625 -0.25 -0.90625q0 -0.453125 0.203125 -0.828125q0.203125 -0.390625 0.5625 -0.640625q0.265625 -0.203125 0.71875 -0.328125q0.46875 -0.140625 1.0 -0.140625q0.78125 0 1.375 0.234375q0.609375 0.21875 0.890625 0.609375q0.296875 0.390625 0.40625 1.046875l-1.125 0.15625q-0.078125 -0.53125 -0.4375 -0.8125q-0.359375 -0.296875 -1.03125 -0.296875q-0.78125 0 -1.125 0.265625q-0.34375 0.25 -0.34375 0.609375q0 0.21875 0.140625 0.390625q0.140625 0.1875 0.4375 0.3125q0.171875 0.0625 1.015625 0.28125q1.21875 0.328125 1.6875 0.53125q0.484375 0.203125 0.75 0.609375q0.28125 0.390625 0.28125 0.96875q0 0.578125 -0.34375 1.078125q-0.328125 0.5 -0.953125 0.78125q-0.625 0.28125 -1.421875 0.28125q-1.3125 0 -2.0 -0.546875q-0.6875 -0.546875 -0.875 -1.625zm7.4296875 -3.421875l0 -1.296875l1.296875 0l0 1.296875l-1.296875 0zm0 5.4375l0 -1.296875l1.296875 0l0 1.296875l-1.296875 0z" fill-rule="nonzero"></path><path fill="#000000" fill-opacity="0.0" d="m-0.33858266 0.36220473l440.063 0l0 52.88189l-440.063 0z" fill-rule="nonzero"></path><path fill="#000000" d="m142.10503 15.214705l6.859375 0q2.046875 0 3.046875 0.171875q1.0 0.171875 1.78125 0.71875095q0.796875 0.53125 1.328125 1.4375q0.53125 0.890625 0.53125 2.0q0 1.203125 -0.65625 2.21875q-0.65625 1.0 -1.765625 1.515625q1.578125 0.453125 2.421875 1.5625q0.84375 1.09375 0.84375 2.578125q0 1.171875 -0.546875 2.28125q-0.546875 1.109375 -1.5 1.78125q-0.9375 0.65625 -2.3125 0.796875q-0.875 0.09375 -4.1875 0.125l-5.84375 0l0 -17.1875zm3.46875 2.859376l0 3.984375l2.265625 0q2.03125 0 2.515625 -0.0625q0.890625 -0.109375 1.40625 -0.609375q0.515625 -0.515625 0.515625 -1.34375q0 -0.796875 -0.453125 -1.296875q-0.4375 -0.5 -1.296875 -0.609375q-0.515625 -0.0625 -2.96875 -0.0625l-1.984375 0zm0 6.84375l0 4.59375l3.203125 0q1.875 0 2.375 -0.109375q0.78125 -0.140625 1.265625 -0.6875q0.484375 -0.546875 0.484375 -1.453125q0 -0.78125 -0.375 -1.3125q-0.375 -0.546875 -1.09375 -0.78125q-0.703125 -0.25 -3.0625 -0.25l-2.796875 0zm22.019531 7.484375l0 -1.859375q-0.6875 0.984375 -1.796875 1.5625q-1.109375 0.578125 -2.328125 0.578125q-1.265625 0 -2.265625 -0.546875q-0.984375 -0.5625 -1.4375 -1.546875q-0.4375 -1.0 -0.4375 -2.765625l0 -7.875l3.296875 0l0 5.71875q0 2.625 0.171875 3.21875q0.1875 0.59375 0.65625 0.9375q0.484375 0.34375 1.234375 0.34375q0.84375 0 1.5 -0.453125q0.671875 -0.46875 0.921875 -1.15625q0.25 -0.6875 0.25 -3.359375l0 -5.25l3.28125 0l0 12.453125l-3.046875 0zm6.4570312 -14.140625l0 -3.046876l3.296875 0l0 3.046876l-3.296875 0zm0 14.140625l0 -12.453125l3.296875 0l0 12.453125l-3.296875 0zm6.6679688 0l0 -17.1875l3.296875 0l0 17.1875l-3.296875 0zm18.089844 0l-3.0625 0l0 -1.828125q-0.765625 1.0625 -1.796875 1.59375q-1.03125 0.515625 -2.09375 0.515625q-2.140625 0 -3.671875 -1.71875q-1.53125 -1.734375 -1.53125 -4.828125q0 -3.171875 1.484375 -4.8125q1.5 -1.65625 3.765625 -1.65625q2.09375 0 3.609375 1.734375l0 -6.187501l3.296875 0l0 17.1875zm-8.796875 -6.5q0 2.0 0.5625 2.890625q0.796875 1.28125 2.21875 1.28125q1.140625 0 1.9375 -0.953125q0.796875 -0.96875 0.796875 -2.890625q0 -2.15625 -0.78125 -3.09375q-0.765625 -0.9375 -1.96875 -0.9375q-1.171875 0 -1.96875 0.9375q-0.796875 0.921875 -0.796875 2.765625zm18.609375 -5.953125l3.078125 0l0 1.828125q0.59375 -0.9375 1.609375 -1.515625q1.03125 -0.59375 2.265625 -0.59375q2.171875 0 3.671875 1.703125q1.515625 1.703125 1.515625 4.734375q0 3.125 -1.53125 4.859375q-1.515625 1.71875 -3.671875 1.71875q-1.03125 0 -1.875 -0.40625q-0.84375 -0.421875 -1.765625 -1.40625l0 6.265625l-3.296875 0l0 -17.1875zm3.265625 6.015625q0 2.09375 0.828125 3.109375q0.828125 1.0 2.03125 1.0q1.140625 0 1.90625 -0.921875q0.765625 -0.921875 0.765625 -3.015625q0 -1.96875 -0.796875 -2.90625q-0.78125 -0.953125 -1.9375 -0.953125q-1.203125 0 -2.0 0.9375q-0.796875 0.921875 -0.796875 2.75zm14.644531 6.4375l-3.296875 0l0 -12.453125l3.0625 0l0 1.78125q0.78125 -1.265625 1.40625 -1.65625q0.640625 -0.40625 1.4375 -0.40625q1.125 0 2.15625 0.625l-1.015625 2.875q-0.828125 -0.546875 -1.546875 -0.546875q-0.6875 0 -1.171875 0.390625q-0.484375 0.375 -0.765625 1.375q-0.265625 1.0 -0.265625 4.171875l0 3.84375zm5.4335938 -6.40625q0 -1.640625 0.796875 -3.171875q0.8125 -1.53125 2.296875 -2.34375q1.484375 -0.8125 3.3125 -0.8125q2.828125 0 4.625 1.84375q1.8125 1.828125 1.8125 4.625q0 2.828125 -1.828125 4.6875q-1.828125 1.859375 -4.59375 1.859375q-1.703125 0 -3.265625 -0.765625q-1.546875 -0.78125 -2.359375 -2.265625q-0.796875 -1.5 -0.796875 -3.65625zm3.375 0.1875q0 1.84375 0.875 2.828125q0.875 0.984375 2.171875 0.984375q1.28125 0 2.15625 -0.984375q0.875 -0.984375 0.875 -2.859375q0 -1.828125 -0.875 -2.8125q-0.875 -0.984375 -2.15625 -0.984375q-1.296875 0 -2.171875 0.984375q-0.875 0.984375 -0.875 2.84375zm22.894516 -2.546875l-3.2499847 0.578125q-0.15625 -0.96875 -0.75 -1.453125q-0.578125 -0.5 -1.5 -0.5q-1.234375 0 -1.96875 0.859375q-0.71875 0.84375 -0.71875 2.828125q0 2.21875 0.734375 3.140625q0.75 0.90625 2.0 0.90625q0.9375 0 1.53125 -0.53125q0.609375 -0.53125 0.84375 -1.828125l3.2343597 0.546875q-0.5 2.21875 -1.9375 3.359375q-1.4218597 1.140625 -3.8281097 1.140625q-2.71875 0 -4.34375 -1.71875q-1.625 -1.734375 -1.625 -4.78125q0 -3.078125 1.625 -4.796875q1.625 -1.71875 4.40625 -1.71875q2.28125 0 3.6093597 0.984375q1.34375 0.984375 1.9375 2.984375zm9.707031 4.796875l3.28125 0.5625q-0.640625 1.796875 -2.015625 2.75q-1.359375 0.9375 -3.40625 0.9375q-3.25 0 -4.796875 -2.125q-1.234375 -1.703125 -1.234375 -4.28125q0 -3.09375 1.609375 -4.84375q1.625 -1.765625 4.09375 -1.765625q2.78125 0 4.375 1.84375q1.609375 1.828125 1.546875 5.609375l-8.25 0q0.03125 1.46875 0.796875 2.28125q0.765625 0.8125 1.890625 0.8125q0.78125 0 1.296875 -0.421875q0.53125 -0.421875 0.8125 -1.359375zm0.1875 -3.328125q-0.046875 -1.421875 -0.75 -2.15625q-0.703125 -0.75 -1.703125 -0.75q-1.078125 0 -1.78125 0.78125q-0.703125 0.78125 -0.6875 2.125l4.921875 0zm4.7851562 3.75l3.3125 -0.515625q0.203125 0.96875 0.84375 1.46875q0.65625 0.5 1.8125 0.5q1.28125 0 1.921875 -0.46875q0.4375 -0.328125 0.4375 -0.890625q0 -0.375 -0.234375 -0.609375q-0.25 -0.234375 -1.109375 -0.4375q-3.984375 -0.875 -5.046875 -1.609375q-1.484375 -1.0 -1.484375 -2.796875q0 -1.625 1.28125 -2.71875q1.28125 -1.109375 3.96875 -1.109375q2.546875 0 3.78125 0.84375q1.25 0.828125 1.71875 2.453125l-3.109375 0.578125q-0.1875 -0.734375 -0.75 -1.109375q-0.5625 -0.390625 -1.59375 -0.390625q-1.296875 0 -1.859375 0.359375q-0.375 0.265625 -0.375 0.671875q0 0.34375 0.328125 0.59375q0.453125 0.328125 3.078125 0.9375q2.625 0.59375 3.671875 1.453125q1.03125 0.875 1.03125 2.453125q0 1.703125 -1.4375 2.9375q-1.421875 1.234375 -4.21875 1.234375q-2.546875 0 -4.03125 -1.03125q-1.484375 -1.03125 -1.9375 -2.796875zm13.347656 0l3.3125 -0.515625q0.203125 0.96875 0.84375 1.46875q0.65625 0.5 1.8125 0.5q1.28125 0 1.921875 -0.46875q0.4375 -0.328125 0.4375 -0.890625q0 -0.375 -0.234375 -0.609375q-0.25 -0.234375 -1.109375 -0.4375q-3.984375 -0.875 -5.046875 -1.609375q-1.484375 -1.0 -1.484375 -2.796875q0 -1.625 1.28125 -2.71875q1.28125 -1.109375 3.96875 -1.109375q2.546875 0 3.78125 0.84375q1.25 0.828125 1.71875 2.453125l-3.109375 0.578125q-0.1875 -0.734375 -0.75 -1.109375q-0.5625 -0.390625 -1.59375 -0.390625q-1.296875 0 -1.859375 0.359375q-0.375 0.265625 -0.375 0.671875q0 0.34375 0.328125 0.59375q0.453125 0.328125 3.078125 0.9375q2.625 0.59375 3.671875 1.453125q1.03125 0.875 1.03125 2.453125q0 1.703125 -1.4375 2.9375q-1.421875 1.234375 -4.21875 1.234375q-2.546875 0 -4.03125 -1.03125q-1.484375 -1.03125 -1.9375 -2.796875z" fill-rule="nonzero"></path><path fill="#000000" d="m187.52312 53.73533q0 0.5 -0.171875 0.890625q-0.15625 0.390625 -0.453125 0.6875q-0.28125 0.296875 -0.671875 0.515625q-0.375 0.21875 -0.8125 0.359375q-0.421875 0.125 -0.875 0.1875q-0.453125 0.078125 -0.890625 0.078125q-0.953125 0 -1.75 -0.09375q-0.78125 -0.078125 -1.546875 -0.265625l0 -1.484375q0.8125 0.234375 1.625 0.359375q0.8125 0.109375 1.609375 0.109375q1.15625 0 1.703125 -0.3125q0.5625 -0.3125 0.5625 -0.890625q0 -0.25 -0.09375 -0.453125q-0.078125 -0.203125 -0.3125 -0.375q-0.234375 -0.1875 -0.71875 -0.375q-0.484375 -0.203125 -1.328125 -0.453125q-0.640625 -0.1875 -1.171875 -0.421875q-0.53125 -0.234375 -0.921875 -0.5625q-0.390625 -0.328125 -0.609375 -0.765625q-0.21875 -0.4375 -0.21875 -1.03125q0 -0.390625 0.171875 -0.84375q0.1875 -0.46875 0.625 -0.859375q0.4375 -0.40625 1.171875 -0.671875q0.75 -0.265625 1.859375 -0.265625q0.546875 0 1.21875 0.0625q0.671875 0.0625 1.390625 0.203125l0 1.4375q-0.765625 -0.171875 -1.453125 -0.265625q-0.671875 -0.09375 -1.171875 -0.09375q-0.609375 0 -1.03125 0.09375q-0.40625 0.09375 -0.65625 0.265625q-0.25 0.15625 -0.375 0.375q-0.109375 0.21875 -0.109375 0.46875q0 0.25 0.09375 0.453125q0.109375 0.203125 0.375 0.390625q0.265625 0.1875 0.734375 0.390625q0.46875 0.1875 1.234375 0.40625q0.828125 0.234375 1.390625 0.5q0.5625 0.265625 0.90625 0.59375q0.359375 0.328125 0.515625 0.734375q0.15625 0.40625 0.15625 0.921875zm3.2572937 -6.765625l1.484375 0l0.046875 1.71875q0.828125 -1.0 1.625 -1.4375q0.796875 -0.453125 1.625 -0.453125q1.4375 0 2.1875 0.9375q0.75 0.9375 0.6875 2.78125l-1.625 0q0.015625 -1.21875 -0.375 -1.765625q-0.375 -0.5625 -1.109375 -0.5625q-0.328125 0 -0.65625 0.125q-0.328125 0.109375 -0.6875 0.375q-0.34375 0.25 -0.734375 0.65625q-0.390625 0.390625 -0.828125 0.953125l0 5.984375l-1.640625 0l0 -9.3125zm17.116669 8.96875q-0.625 0.234375 -1.296875 0.34375q-0.65625 0.125 -1.359375 0.125q-2.21875 0 -3.40625 -1.1875q-1.1875 -1.203125 -1.1875 -3.5q0 -1.109375 0.34375 -2.0q0.34375 -0.90625 0.953125 -1.546875q0.625 -0.640625 1.484375 -0.984375q0.875 -0.34375 1.90625 -0.34375q0.734375 0 1.359375 0.109375q0.625 0.09375 1.203125 0.3125l0 1.546875q-0.59375 -0.3125 -1.234375 -0.453125q-0.625 -0.15625 -1.28125 -0.15625q-0.625 0 -1.1875 0.25q-0.546875 0.234375 -0.96875 0.6875q-0.40625 0.4375 -0.65625 1.078125q-0.234375 0.640625 -0.234375 1.4375q0 1.6875 0.8125 2.53125q0.828125 0.84375 2.28125 0.84375q0.65625 0 1.265625 -0.140625q0.625 -0.15625 1.203125 -0.453125l0 1.5zm19.920837 0.34375l0 -6.6875q0 -0.4375 -0.03125 -0.71875q-0.03125 -0.28125 -0.109375 -0.4375q-0.0625 -0.15625 -0.171875 -0.21875q-0.109375 -0.078125 -0.265625 -0.078125q-0.1875 0 -0.34375 0.125q-0.15625 0.109375 -0.34375 0.359375q-0.171875 0.25 -0.390625 0.65625q-0.21875 0.40625 -0.515625 1.015625l0 5.984375l-1.46875 0l0 -6.515625q0 -0.5 -0.03125 -0.8125q-0.03125 -0.328125 -0.109375 -0.5q-0.0625 -0.171875 -0.1875 -0.234375q-0.109375 -0.078125 -0.265625 -0.078125q-0.15625 0 -0.3125 0.09375q-0.140625 0.09375 -0.328125 0.34375q-0.171875 0.234375 -0.40625 0.65625q-0.21875 0.40625 -0.53125 1.0625l0 5.984375l-1.484375 0l0 -9.3125l1.234375 0l0.078125 1.765625q0.25 -0.53125 0.46875 -0.890625q0.234375 -0.375 0.46875 -0.59375q0.25 -0.234375 0.515625 -0.34375q0.28125 -0.109375 0.609375 -0.109375q0.75 0 1.140625 0.5q0.390625 0.484375 0.390625 1.515625q0.21875 -0.484375 0.4375 -0.859375q0.21875 -0.375 0.453125 -0.625q0.25 -0.265625 0.546875 -0.390625q0.296875 -0.140625 0.6875 -0.140625q1.75 0 1.75 2.703125l0 6.78125l-1.484375 0zm9.601044 0l-0.03125 -1.25q-0.765625 0.75 -1.546875 1.09375q-0.78125 0.328125 -1.65625 0.328125q-0.796875 0 -1.359375 -0.203125q-0.5625 -0.203125 -0.9375 -0.5625q-0.359375 -0.359375 -0.53125 -0.84375q-0.171875 -0.484375 -0.171875 -1.046875q0 -1.40625 1.046875 -2.1875q1.046875 -0.796875 3.078125 -0.796875l1.9375 0l0 -0.828125q0 -0.8125 -0.53125 -1.3125q-0.53125 -0.5 -1.609375 -0.5q-0.796875 0 -1.5625 0.1875q-0.765625 0.171875 -1.578125 0.484375l0 -1.453125q0.296875 -0.109375 0.671875 -0.21875q0.390625 -0.109375 0.796875 -0.1875q0.421875 -0.078125 0.875 -0.125q0.453125 -0.0625 0.921875 -0.0625q0.84375 0 1.515625 0.1875q0.6875 0.1875 1.15625 0.578125q0.46875 0.375 0.71875 0.953125q0.25 0.5625 0.25 1.34375l0 6.421875l-1.453125 0zm-0.171875 -4.234375l-2.0625 0q-0.59375 0 -1.03125 0.125q-0.4375 0.109375 -0.71875 0.34375q-0.28125 0.21875 -0.421875 0.53125q-0.125 0.296875 -0.125 0.6875q0 0.28125 0.078125 0.53125q0.09375 0.234375 0.28125 0.421875q0.1875 0.1875 0.484375 0.3125q0.296875 0.109375 0.71875 0.109375q0.5625 0 1.28125 -0.34375q0.71875 -0.34375 1.515625 -1.078125l0 -1.640625zm12.819794 4.234375l-2.21875 0l-4.34375 -4.984375l0 4.984375l-1.609375 0l0 -13.109375l1.609375 0l0 8.046875l4.1875 -4.25l2.140625 0l-4.375 4.296875l4.609375 5.015625zm9.757278 -5.15625q0 0.34375 -0.015625 0.578125q-0.015625 0.234375 -0.03125 0.4375l-6.5312347 0q0 1.4375 0.796875 2.203125q0.796875 0.765625 2.2968597 0.765625q0.40625 0 0.8125 -0.03125q0.40625 -0.046875 0.78125 -0.09375q0.390625 -0.0625 0.734375 -0.125q0.34375 -0.078125 0.640625 -0.15625l0 1.328125q-0.65625 0.1875 -1.484375 0.296875q-0.828125 0.125 -1.71875 0.125q-1.2031097 0 -2.0624847 -0.328125q-0.859375 -0.328125 -1.421875 -0.9375q-0.546875 -0.625 -0.8125 -1.515625q-0.265625 -0.890625 -0.265625 -2.03125q0 -0.984375 0.28125 -1.859375q0.296875 -0.875 0.828125 -1.53125q0.546875 -0.671875 1.328125 -1.0625q0.796875 -0.390625 1.796875 -0.390625q0.98435974 0 1.7343597 0.3125q0.75 0.296875 1.265625 0.859375q0.515625 0.5625 0.78125 1.375q0.265625 0.796875 0.265625 1.78125zm-1.6875 -0.21875q0.03125 -0.625 -0.125 -1.140625q-0.140625 -0.515625 -0.453125 -0.890625q-0.3125 -0.375 -0.78125 -0.578125q-0.453125 -0.203125 -1.0781097 -0.203125q-0.515625 0 -0.953125 0.203125q-0.4375 0.203125 -0.765625 0.578125q-0.3125 0.359375 -0.5 0.890625q-0.1875 0.515625 -0.234375 1.140625l4.8906097 0z" fill-rule="nonzero"></path></g></svg>
+
diff --git a/more.txt b/more.txt
new file mode 100644
index 0000000..6b8710a
--- /dev/null
+++ b/more.txt
@@ -0,0 +1,1 @@
+more
```

## File: `diff/testdata/no_newline_both.diff`
```
@@ -1,1 +1,1 @@
-a
\ No newline at end of file
+b
\ No newline at end of file
```

## File: `diff/testdata/no_newline_both2.diff`
```
@@ -1,3 +1,3 @@
 0
-a
-a
\ No newline at end of file
+b
+b
\ No newline at end of file
```

## File: `diff/testdata/no_newline_new.diff`
```
@@ -1,3 +1,2 @@
 a
-a
-a
+a
\ No newline at end of file
```

## File: `diff/testdata/no_newline_orig.diff`
```
@@ -1,1 +1,1 @@
-a
\ No newline at end of file
+b
```

## File: `diff/testdata/oneline_hunk.diff`
```
@@ -1,1 +1,1 @@
-a
+b
```

## File: `diff/testdata/quoted_filename.diff`
```
diff --git "a/\345\225\206\345\223\201\350\257\246\346\203\205.txt" "b/\345\225\206\345\223\201\350\257\246\346\203\205.txt"
index e69de29..c67479b 100644
--- "a/\345\225\206\345\223\201\350\257\246\346\203\205.txt"
+++ "b/\345\225\206\345\223\201\350\257\246\346\203\205.txt"
@@ -0,0 +1,3 @@
+some
+test
+file
```

## File: `diff/testdata/sample_bad_hunks.diff`
```
@@ -1,3 +1,9 @@
+This is an important
+notice! It should
+therefore be located at
+the beginning of this
+document!
+
 This part of the
 document has stayed the
 same from version to
@@ -5,16 +11,13 @@
 be shown if it doesn't
 change.  Otherwise, that
 would not be helping to
-compress the size of the
-changes.
-
-This paragraph contains
-text that is outdated.
-It will be deleted in the
-near future.
+compress anything.
 
 It is important to spell
-check this dokument. On
+check this document. On
 the other hand, a
 misspelled word isn't
 the end of the world.
@@ -22,3 +22,7 @@
 this paragraph needs to
 be changed. Things can
 be added after it.
+
+This paragraph contains
+important new additions
+to this document.
```

## File: `diff/testdata/sample_binary_inline.diff`
```
diff --git a/logo-old.png b/logo-old.png
deleted file mode 100644
index d29d0e9757e0d9b854a8ed58f170bcb454cc1ae3..0000000000000000000000000000000000000000
GIT binary patch
literal 0
HcmV?d00001

literal 0
HcmV?d00001

diff --git a/logo-old.png b/logo-old.png
index ff82e793467f2050d731d75b4968d2e6b9c5d33b..d29d0e9757e0d9b854a8ed58f170bcb454cc1ae3 100644
GIT binary patch
literal 0
HcmV?d00001

literal 0
HcmV?d00001

diff --git a/logo.png b/logo-old.png
similarity index 100%
rename from logo.png
rename to logo-old.png
diff --git a/logo.png b/logo.png
new file mode 100644
index 0000000000000000000000000000000000000000..ff82e793467f2050d731d75b4968d2e6b9c5d33b
GIT binary patch
literal 0
HcmV?d00001

literal 0
HcmV?d00001

```

## File: `diff/testdata/sample_contains_added_deleted_files.diff`
```
diff -u source_a/file_1.txt  source_b/file_1.txt
--- source_a/file_1.txt
+++ source_b/file_1.txt
@@ -2,3 +3,4 @@
 To be, or not to be, that is the question:
-Whether 'tis nobler in the mind to suffer
+The slings and arrows of outrageous fortune,
+Or to take arms against a sea of troubles
 And by opposing end them. To die—to sleep,
Only in source_a: file_2.txt
Only in source_b: file_3.txt
```

## File: `diff/testdata/sample_contains_only_added_deleted_files.diff`
```
Only in source_a: file_1.txt
Only in source_a: file_2.txt
Only in source_b: file_3.txt
```

## File: `diff/testdata/sample_file.diff`
```
--- oldname	2009-10-11 15:12:20.000000000 +0000
+++ newname	2009-10-11 15:12:30.000000000 +0000
@@ -1,3 +1,9 @@
+This is an important
+notice! It should
+therefore be located at
+the beginning of this
+document!
+
 This part of the
 document has stayed the
 same from version to
@@ -5,16 +11,10 @@
 be shown if it doesn't
 change.  Otherwise, that
 would not be helping to
-compress the size of the
-changes.
-
-This paragraph contains
-text that is outdated.
-It will be deleted in the
-near future.
+compress anything.
 
 It is important to spell
-check this dokument. On
+check this document. On
 the other hand, a
 misspelled word isn't
 the end of the world.
```

## File: `diff/testdata/sample_file_extended.diff`
```
diff --git a/vcs/git_cmd.go b/vcs/git_cmd.go
index aa4de15..7c048ab 100644
--- oldname	2009-10-11 15:12:20.000000000 +0000
+++ newname	2009-10-11 15:12:30.000000000 +0000
@@ -1,3 +1,9 @@
+This is an important
+notice! It should
+therefore be located at
+the beginning of this
+document!
+
 This part of the
 document has stayed the
 same from version to
@@ -5,16 +11,10 @@
 be shown if it doesn't
 change.  Otherwise, that
 would not be helping to
-compress the size of the
-changes.
-
-This paragraph contains
-text that is outdated.
-It will be deleted in the
-near future.
+compress anything.
 
 It is important to spell
-check this dokument. On
+check this document. On
 the other hand, a
 misspelled word isn't
 the end of the world.
```

## File: `diff/testdata/sample_file_extended_binary_rename.diff`
```
diff --git a/data/Font.png b/data/Other.png
similarity index 51%
rename from data/Font.png
rename to data/Other.png
index 17a971d..599f8dd 100644
Binary files a/data/Font.png and b/data/Other.png differ
```

## File: `diff/testdata/sample_file_extended_binary_rename_no_index.diff`
```
diff --git a/data/foo.txt b/data/bar.txt
similarity index 100%
rename from data/foo.txt
rename to data/bar.txt
Binary files a/data/foo.txt and b/data/bar.txt differ
```

## File: `diff/testdata/sample_file_extended_empty_binary.diff`
```
diff --git a/data/Font.png b/data/Font.png
index 17a971d..599f8dd 100644
Binary files a/data/Font.png and b/data/Font.png differ
```

## File: `diff/testdata/sample_file_extended_empty_deleted.diff`
```
diff --git a/vendor/go/build/testdata/empty/dummy b/vendor/go/build/testdata/empty/dummy
deleted file mode 100644
index e69de29..0000000
```

## File: `diff/testdata/sample_file_extended_empty_deleted_binary.diff`
```
diff --git a/187/player/random/gopher-0.png b/187/player/random/gopher-0.png
deleted file mode 100644
index aebdfc7..0000000
Binary files a/187/player/random/gopher-0.png and /dev/null differ
```

## File: `diff/testdata/sample_file_extended_empty_mode_change.diff`
```
diff --git a/docs/index.md b/docs/index.md
old mode 100644
new mode 100755
```

## File: `diff/testdata/sample_file_extended_empty_new.diff`
```
diff --git a/vendor/go/build/testdata/empty/dummy b/vendor/go/build/testdata/empty/dummy
new file mode 100644
index 0000000..e69de29
```

## File: `diff/testdata/sample_file_extended_empty_new_binary.diff`
```
diff --git a/diff/binary-image.png b/diff/binary-image.png
new file mode 100644
index 0000000..b51756e
Binary files /dev/null and b/diff/binary-image.png differ
```

## File: `diff/testdata/sample_file_extended_empty_rename.diff`
```
diff --git a/docs/integrations/Email_Notifications.md b/docs/integrations/email-notifications.md
similarity index 100%
rename from docs/integrations/Email_Notifications.md
rename to docs/integrations/email-notifications.md
```

## File: `diff/testdata/sample_file_extended_empty_rename_and_mode_change.diff`
```
diff --git a/textfile.txt b/textfile2.txt
old mode 100644
new mode 100755
similarity index 100%
rename from textfile.txt
rename to textfile2.txt
```

## File: `diff/testdata/sample_file_no_fractional_seconds.diff`
```
--- goyaml.go	2011-11-24 19:47:20 +0000
+++ goyaml.go	2011-11-28 13:24:39 +0000
@@ -256,7 +256,7 @@
 	switch v.Kind() {
 	case reflect.String:
 		return len(v.String()) == 0
-	case reflect.Interface:
+	case reflect.Interface, reflect.Ptr:
 		return v.IsNil()
 	case reflect.Slice:
 		return v.Len() == 0
```

## File: `diff/testdata/sample_file_no_timestamp.diff`
```
--- oldname
+++ newname
@@ -1,3 +1,9 @@
+This is an important
+notice! It should
+therefore be located at
+the beginning of this
+document!
+
 This part of the
 document has stayed the
 same from version to
@@ -5,16 +11,10 @@
 be shown if it doesn't
 change.  Otherwise, that
 would not be helping to
-compress the size of the
-changes.
-
-This paragraph contains
-text that is outdated.
-It will be deleted in the
-near future.
+compress anything.
 
 It is important to spell
-check this dokument. On
+check this document. On
 the other hand, a
 misspelled word isn't
 the end of the world.
```

## File: `diff/testdata/sample_hunk.diff`
```
@@ -1,3 +1,9 @@ Section Header
+This is an important
+notice! It should
+therefore be located at
+the beginning of this
+document!
+
 This part of the
 document has stayed the
 same from version to
```

## File: `diff/testdata/sample_hunk_lines_start_with_minuses.diff`
```
@@ -1,5 +1,3 @@
 select 1;
--- this is my query
 select 2;
 select 3;
--- this is the last line
```

## File: `diff/testdata/sample_hunk_lines_start_with_minuses_pluses.diff`
```
@@ -1,5 +1,5 @@
 select 1;
--- this is my query
+++ this is my query
 select 2;
 select 3;
--- this is the last line
+++ this is the last line
```

## File: `diff/testdata/sample_hunks.diff`
```
@@ -1,3 +1,9 @@ Section Header
+This is an important
+notice! It should
+therefore be located at
+the beginning of this
+document!
+
 This part of the
 document has stayed the
 same from version to
@@ -5,16 +11,10 @@
 be shown if it doesn't
 change.  Otherwise, that
 would not be helping to
-compress the size of the
-changes.
-
-This paragraph contains
-text that is outdated.
-It will be deleted in the
-near future.
+compress anything.
 
 It is important to spell
-check this dokument. On
+check this document. On
 the other hand, a
 misspelled word isn't
 the end of the world.
@@ -22,3 +22,7 @@
 this paragraph needs to
 be changed. Things can
 be added after it.
+
+This paragraph contains
+important new additions
+to this document.
```

## File: `diff/testdata/sample_hunks_no_newline.diff`
```
@@ -1,1 +1,1 @@
-b
+b
\ No newline at end of file
```

## File: `diff/testdata/sample_multi_file.diff`
```
diff --ruN a/oldname1 b/newname1
old mode 0777
new mode 0755
--- oldname1	2009-10-11 15:12:20.000000000 +0000
+++ newname1	2009-10-11 15:12:30.000000000 +0000
@@ -1,3 +1,9 @@
+This is an important
+notice! It should
+therefore be located at
+the beginning of this
+document!
+
 This part of the
 document has stayed the
 same from version to
@@ -5,16 +11,10 @@
 be shown if it doesn't
 change.  Otherwise, that
 would not be helping to
-compress the size of the
-changes.
-
-This paragraph contains
-text that is outdated.
-It will be deleted in the
-near future.
+compress anything.
 
 It is important to spell
-check this dokument. On
+check this document. On
diff --ruN a/oldname2 b/newname2
--- oldname2	2009-10-11 15:12:20.000000000 +0000
+++ newname2	2009-10-11 15:12:30.000000000 +0000
@@ -1,3 +1,9 @@
+This is an important
+notice! It should
+therefore be located at
+the beginning of this
+document!
+
 This part of the
 document has stayed the
 same from version to
@@ -5,16 +11,10 @@
 be shown if it doesn't
 change.  Otherwise, that
 would not be helping to
-compress the size of the
-changes.
-
-This paragraph contains
-text that is outdated.
-It will be deleted in the
-near future.
+compress anything.
 
 It is important to spell
-check this dokument. On
+check this document. On
 the other hand, a
 misspelled word isn't
 the end of the world.
```

## File: `diff/testdata/sample_multi_file_binary.diff`
```
diff --git a/README.md b/README.md
index 7b73e04..36cde13 100644
--- a/README.md
+++ b/README.md
@@ -1,6 +1,8 @@
 Conception-go [![Build Status](https://travis-ci.org/shurcooL/Conception-go.svg?branch=master)](https://travis-ci.org/shurcooL/Conception-go)
 =============

+This is a change.
+
 This is a work in progress Go implementation of [Conception](https://github.com/shurcooL/Conception#demonstration).

 Conception is an experimental project. It's a platform for researching software development tools and techniques. It is driven by a set of guiding principles. Conception-go targets Go development.
diff --git a/data/Font.png b/data/Font.png
index 17a971d..599f8dd 100644
Binary files a/data/Font.png and b/data/Font.png differ
diff --git a/main.go b/main.go
index 1aced1e..98a982e 100644
--- a/main.go
+++ b/main.go
@@ -6710,6 +6710,8 @@ func init() {
 }

 func main() {
+	// Another plain text change.
+
 	//defer profile.Start(profile.CPUProfile).Stop()
 	//defer profile.Start(profile.MemProfile).Stop()

```

## File: `diff/testdata/sample_multi_file_deleted.diff`
```
diff --git a/vendor/go/build/syslist_test.go b/vendor/go/build/syslist_test.go
deleted file mode 100644
index 3be2928..0000000
--- a/vendor/go/build/syslist_test.go
+++ /dev/null
@@ -1,62 +0,0 @@
-func TestGoodOSArch(t *testing.T) {
-       for _, test := range tests {
-               if Default.goodOSArchFile(test.name, make(map[string]bool)) != test.result {
-                       t.Fatalf("goodOSArchFile(%q) != %v", test.name, test.result)
-               }
-       }
-}
diff --git a/vendor/go/build/testdata/empty/dummy b/vendor/go/build/testdata/empty/dummy
deleted file mode 100644
index e69de29..0000000
diff --git a/vendor/go/build/testdata/multi/file.go b/vendor/go/build/testdata/multi/file.go
deleted file mode 100644
index ee946eb..0000000
--- a/vendor/go/build/testdata/multi/file.go
+++ /dev/null
@@ -1,5 +0,0 @@
-// Test data - not compiled.
-
-package main
-
-func main() {}
```

## File: `diff/testdata/sample_multi_file_filemode_change.diff`
```
diff --git a/sample.sh b/sample.sh
old mode 100755
new mode 100644
diff --git a/sample2.sh b/sample2.sh
old mode 100755
new mode 100644
```

## File: `diff/testdata/sample_multi_file_minuses_pluses.diff`
```
diff --git a/comment-last-line.sql b/comment-last-line.sql
index 04a1655..97bd115 100644
--- a/comment-last-line.sql
+++ b/comment-last-line.sql
@@ -1,4 +1,4 @@
 select 1;
+++ invalid SQL comment
 select 2;
 select 3;
--- end of three queries
diff --git a/query.sql b/query.sql
index 9537d7b..234ef35 100644
--- a/query.sql
+++ b/query.sql
@@ -1,5 +1,4 @@
 select 1;
--- this is my query
 select 2;
 select 3;
--- this is the last line
+++ invalid sql comment
```

## File: `diff/testdata/sample_multi_file_new.diff`
```
diff --git a/_vendor/go/build/syslist_test.go b/_vendor/go/build/syslist_test.go
new file mode 100644
index 0000000..3be2928
--- /dev/null
+++ b/_vendor/go/build/syslist_test.go
@@ -0,0 +1,62 @@
+func TestGoodOSArch(t *testing.T) {
+	for _, test := range tests {
+		if Default.goodOSArchFile(test.name, make(map[string]bool)) != test.result {
+			t.Fatalf("goodOSArchFile(%q) != %v", test.name, test.result)
+		}
+	}
+}
diff --git a/_vendor/go/build/testdata/empty/dummy b/_vendor/go/build/testdata/empty/dummy
new file mode 100644
index 0000000..e69de29
diff --git a/_vendor/go/build/testdata/multi/file.go b/_vendor/go/build/testdata/multi/file.go
new file mode 100644
index 0000000..ee946eb
--- /dev/null
+++ b/_vendor/go/build/testdata/multi/file.go
@@ -0,0 +1,5 @@
+// Test data - not compiled.
+
+package main
+
+func main() {}
```

## File: `diff/testdata/sample_multi_file_new_win.diff`
```
diff --git a/_vendor/go/build/syslist_test.go b/_vendor/go/build/syslist_test.go
new file mode 100644
index 0000000..3be2928
--- /dev/null
+++ b/_vendor/go/build/syslist_test.go
@@ -0,0 +1,62 @@
+func TestGoodOSArch(t *testing.T) {
+	for _, test := range tests {
+		if Default.goodOSArchFile(test.name, make(map[string]bool)) != test.result {
+			t.Fatalf("goodOSArchFile(%q) != %v", test.name, test.result)
+		}
+	}
+}
diff --git a/_vendor/go/build/testdata/empty/dummy b/_vendor/go/build/testdata/empty/dummy
new file mode 100644
index 0000000..e69de29
diff --git a/_vendor/go/build/testdata/multi/file.go b/_vendor/go/build/testdata/multi/file.go
new file mode 100644
index 0000000..ee946eb
--- /dev/null
+++ b/_vendor/go/build/testdata/multi/file.go
@@ -0,0 +1,5 @@
+// Test data - not compiled.
+
+package main
+
+func main() {}
```

## File: `diff/testdata/sample_multi_file_rename.diff`
```
diff --git a/README.md b/README.md
index 5f3d591..96a24fa 100644
--- a/README.md
+++ b/README.md
@@ -24,6 +24,8 @@ and [view enterprise capabilities](https://www.example.com).*
 
 ## Installation
 
+Minor change here.
+
 Follow the 5-minute
 [installation instructions](https://www.example.com/.docs/getting-started/). For
 more installation methods, check out the
diff --git a/docs/integrations/Email_Notifications.md b/docs/integrations/email-notifications.md
similarity index 100%
rename from docs/integrations/Email_Notifications.md
rename to docs/integrations/email-notifications.md
diff --git a/release_notes.md b/release_notes.md
index f2ff13f..f060cb5 100644
--- a/release_notes.md
+++ b/release_notes.md
@@ -1,3 +1,5 @@
+# new section
+
 # dev
 
 - Removed example pages and the `--auth.example-flag`
```

## File: `diff/testdata/sample_multi_file_single.diff`
```
diff --ruN a/oldname1 b/newname1
--- oldname1	2009-10-11 15:12:20.000000000 +0000
+++ newname1	2009-10-11 15:12:30.000000000 +0000
@@ -1,3 +1,9 @@
+This is an important
+notice! It should
+therefore be located at
+the beginning of this
+document!
+
 This part of the
 document has stayed the
 same from version to
@@ -5,16 +11,10 @@
 be shown if it doesn't
 change.  Otherwise, that
 would not be helping to
-compress the size of the
-changes.
-
-This paragraph contains
-text that is outdated.
-It will be deleted in the
-near future.
+compress anything.
 
 It is important to spell
-check this dokument. On
+check this document. On
```

## File: `diff/testdata/sample_multi_file_single_apple_in.diff`
```
diff -u a/oldname1 b/newname1
--- oldname1	2009-10-11 15:12:20
+++ newname1	2009-10-11 15:12:30
@@ -1,3 +1,9 @@
+This is an important
+notice! It should
+therefore be located at
+the beginning of this
+document!
+
 This part of the
 document has stayed the
 same from version to
@@ -5,16 +11,10 @@
 be shown if it doesn't
 change.  Otherwise, that
 would not be helping to
-compress the size of the
-changes.
-
-This paragraph contains
-text that is outdated.
-It will be deleted in the
-near future.
+compress anything.
 
 It is important to spell
-check this dokument. On
+check this document. On
```

## File: `diff/testdata/sample_multi_file_single_apple_out.diff`
```
diff -u a/oldname1 b/newname1
--- oldname1	2009-10-11 15:12:20.000000000 +0000
+++ newname1	2009-10-11 15:12:30.000000000 +0000
@@ -1,3 +1,9 @@
+This is an important
+notice! It should
+therefore be located at
+the beginning of this
+document!
+
 This part of the
 document has stayed the
 same from version to
@@ -5,16 +11,10 @@
 be shown if it doesn't
 change.  Otherwise, that
 would not be helping to
-compress the size of the
-changes.
-
-This paragraph contains
-text that is outdated.
-It will be deleted in the
-near future.
+compress anything.
 
 It is important to spell
-check this dokument. On
+check this document. On
```

## File: `diff/testdata/sample_multi_file_trailing_content.diff`
```
some leading content
diff --git a/comment-last-line.sql b/comment-last-line.sql
index 04a1655..97bd115 100644
--- a/comment-last-line.sql
+++ b/comment-last-line.sql
@@ -1,4 +1,4 @@
 select 1;
+++ invalid SQL comment
 select 2;
 select 3;
--- end of three queries
some content between diffs
diff --git a/query.sql b/query.sql
index 9537d7b..234ef35 100644
--- a/query.sql
+++ b/query.sql
@@ -1,5 +1,4 @@
 select 1;
--- this is my query
 select 2;
 select 3;
--- this is the last line
+++ invalid sql comment
some trailing content
```

## File: `diff/testdata/sample_multi_file_trailing_content_diffsonly.diff`
```
some leading content
diff --git a/comment-last-line.sql b/comment-last-line.sql
index 04a1655..97bd115 100644
--- a/comment-last-line.sql
+++ b/comment-last-line.sql
@@ -1,4 +1,4 @@
 select 1;
+++ invalid SQL comment
 select 2;
 select 3;
--- end of three queries
some content between diffs
diff --git a/query.sql b/query.sql
index 9537d7b..234ef35 100644
--- a/query.sql
+++ b/query.sql
@@ -1,5 +1,4 @@
 select 1;
--- this is my query
 select 2;
 select 3;
--- this is the last line
+++ invalid sql comment
```

## File: `diff/testdata/sample_multi_file_without_extended.diff`
```
--- source_1_a/file_1.txt
+++ source_1_c/file_1.txt
@@ -1,11 +1,13 @@
 Text generated by www.randomtextgenerator.com

+
 In to am attended desirous raptures declared diverted confined at.
+In to are desirous declared diverted confined at.
+In to am attended raptures declared diverted confined at.
+In to am attended desirous confined at.
 Collected instantly remaining up certainly to necessary as.
 Over walk dull into son boy door went new.
 At or happiness commanded daughters as.
 Is handsome an declared at received in extended vicinity subjects.
-Is handsome received in extended vicinity subjects.
-Is handsome an declared at vicinity subjects.
 Into miss on he over been late pain an.
 Only week bore boy what fat case left use.
--- source_1_a/file_2.txt
+++ source_1_c/file_2.txt
@@ -4,8 +4,8 @@
 Still round match we to.
 Frankness pronounce daughters remainder extensive has but.
+Happiness cordially one determine concluded fat.
 Plenty season beyond by hardly giving of.
-Consulted or acuteness dejection an smallness if.
-Outward general passage another as it.
 Very his are come man walk one next.
 Delighted prevailed supported too not remainder perpetual who furnished.
 Nay affronting bed projection compliment instrument.
+Still round match we to here.
```

## File: `diff/testdata/sample_no_chunksize.diff`
```
@@ -0,0 +1 @@
+Added one line
```

## File: `diff/testdata/sample_onlyin_complex_filenames.diff`
```
Only in internal/trace/foo bar: bam
Only in internal/trace/foo bar: bam: bar
Only in internal/trace/hello: world: bazz
```

## File: `diff/testdata/sample_onlyin_line_isnt_a_file_header.diff`
```
diff -u source_a/file_1.txt  source_b/file_1.txt
--- source_a/file_1.txt
+++ source_b/file_1.txt
@@ -2,3 +3,4 @@
 To be, or not to be, that is the question:
-Whether 'tis nobler in the mind to suffer
+The slings and arrows of outrageous fortune,
+Or to take arms against a sea of troubles
 And by opposing end them. To die—to sleep,
Only in universe!
Only in source_a: file_2.txt
Only in source_b: file_3.txt some unrelated stuff here.
Only in source_b: file_3.txt
```

