---
id: github.com-segmentio-encoding-ef7ddd04-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:20.277009
---

# KNOWLEDGE EXTRACT: github.com_segmentio_encoding_ef7ddd04
> **Extracted on:** 2026-04-01 09:18:57
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007520114/github.com_segmentio_encoding_ef7ddd04

---

## File: `.gitignore`
```
# Binaries for programs and plugins
*.exe
*.exe~
*.dll
*.so
*.dylib

benchmark
anonymize

# Test binary, build with `go test -c`
*.test

# Output of the go coverage tool, specifically when used with LiteIDE
*.out

# Emacs
*~

vendor

benchmarks/msgs.json
benchmarks/results/*json
benchmarks/result/benchmark
*.txt

json/fuzz/corpus/*
json/fuzz/crashers/*
json/fuzz/suppressions/*
*-fuzz.zip
```

## File: `.golangci.yml`
```yaml
version: "2"
linters:
  exclusions:
    rules:
      # Tests copied from the stdlib are not meant to be linted.
      - path: 'golang_(.+_)?test\.go'
        source: "^" # regex
```

## File: `LICENSE`
```
MIT License

Copyright (c) 2019 Segment.io, Inc.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## File: `Makefile`
```
.PHONY: test bench-simple clean update-golang-test fuzz fuzz-json

golang.version ?= 1.21
golang.tmp.root := /tmp/golang$(golang.version)
golang.tmp.json.root := $(golang.tmp.root)/go-go$(golang.version)/src/encoding/json
golang.test.files := $(wildcard json/golang_*_test.go)
benchstat := ${GOPATH}/bin/benchstat
go-fuzz := ${GOPATH}/bin/go-fuzz
go-fuzz-build := ${GOPATH}/bin/go-fuzz-build
go-fuzz-corpus := ${GOPATH}/src/github.com/dvyukov/go-fuzz-corpus
go-fuzz-dep := ${GOPATH}/src/github.com/dvyukov/go-fuzz/go-fuzz-dep

test: test-ascii test-json test-json-bugs test-proto test-iso8601 test-thrift test-purego

test-ascii:
	go test -cover -race ./ascii

test-json:
	go test -cover -race ./json

test-json-bugs:
	go test -race ./json/bugs/...

test-proto:
	go test -cover -race ./proto

test-iso8601:
	go test -cover -race ./iso8601

test-thrift:
	go test -cover -race ./thrift

test-purego:
	go test -race -tags purego ./...

$(benchstat):
	GO111MODULE=off go get -u golang.org/x/perf/cmd/benchstat

# This compares segmentio/encoding/json to the standard golang encoding/json;
# for more in-depth benchmarks, see the `benchmarks` directory.
count ?= 5
bench-simple: $(benchstat)
	@go test -v -run '^$$' -bench '(Marshal|Unmarshal)$$/codeResponse' -benchmem -cpu 1 -count $(count) ./json -package encoding/json | tee /tmp/encoding-json.txt
	@go test -v -run '^$$' -bench '(Marshal|Unmarshal)$$/codeResponse' -benchmem -cpu 1 -count $(count) ./json | tee /tmp/segmentio-encoding-json.txt
	benchstat /tmp/encoding-json.txt /tmp/segmentio-encoding-json.txt

bench-master: $(benchstat)
	git stash
	git checkout master
	@go test -v -run '^$$' -bench /codeResponse -benchmem -benchtime 3s -cpu 1 ./json -count 8 | tee /tmp/segmentio-encoding-json-master.txt
	git checkout -
	git stash pop
	@go test -v -run '^$$' -bench /codeResponse -benchmem -benchtime 3s -cpu 1 ./json -count 8 | tee /tmp/segmentio-encoding-json.txt
	benchstat /tmp/segmentio-encoding-json-master.txt /tmp/segmentio-encoding-json.txt

update-golang-test: $(golang.test.files)
	@echo "updated golang tests to $(golang.version)"

json/golang_%_test.go: $(golang.tmp.json.root)/%_test.go $(golang.tmp.json.root)
	@echo "updating $@ with $<"
	cp $< $@
	sed -i '' -E '/(import)?[ \t]*"internal\/.*".*/d' $@

$(golang.tmp.json.root): $(golang.tmp.root)
	curl -L "https://github.com/golang/go/archive/go${golang.version}.tar.gz" | tar xz -C "$</"

$(golang.tmp.root):
	mkdir -p "$@"

$(go-fuzz):
	GO111MODULE=off go install github.com/dvyukov/go-fuzz/go-fuzz

$(go-fuzz-build):
	GO111MODULE=off go install github.com/dvyukov/go-fuzz/go-fuzz-build

$(go-fuzz-corpus):
	GO111MODULE=off go get github.com/dvyukov/go-fuzz-corpus

$(go-fuzz-dep):
	GO111MODULE=off go get github.com/dvyukov/go-fuzz/go-fuzz-dep

json/fuzz/corpus: $(go-fuzz-corpus)
	cp -r $(go-fuzz-corpus)/json/corpus json/fuzz/corpus

json/fuzz/json-fuzz.zip: $(go-fuzz-build) $(go-fuzz-corpus) $(go-fuzz-dep) $(wildcard ./json/fuzz/corpus/*)
	cd json/fuzz && GO111MODULE=off go-fuzz-build -o json-fuzz.zip

fuzz: fuzz-json

fuzz-json: $(go-fuzz) $(wildcard json/fuzz/*.go) json/fuzz/json-fuzz.zip
	cd json/fuzz && GO111MODULE=off go-fuzz -bin json-fuzz.zip

clean:
	rm -rf $(golang.tmp.root) json/fuzz/{crashers,corpus,suppressions,json-fuzz.zip} *json.txt
```

## File: `README.md`
```markdown
# encoding ![build status](https://github.com/segmentio/encoding/actions/workflows/test.yml/badge.svg) [![Go Report Card](https://goreportcard.com/badge/github.com/segmentio/encoding)](https://goreportcard.com/report/github.com/segmentio/encoding) [![GoDoc](https://godoc.org/github.com/segmentio/encoding?status.svg)](https://godoc.org/github.com/segmentio/encoding)

Go package containing implementations of encoders and decoders for various data
formats.

## Motivation

At Segment, we do a lot of marshaling and unmarshaling of data when sending,
queuing, or storing messages. The resources we need to provision on the
infrastructure are directly related to the type and amount of data that we are
processing. At the scale we operate at, the tools we choose to build programs
can have a large impact on the efficiency of our systems. It is important to
explore alternative approaches when we reach the limits of the code we use.

This repository includes experiments for Go packages for marshaling and
unmarshaling data in various formats. While the focus is on providing a high
performance library, we also aim for very low development and maintenance overhead
by implementing APIs that can be used as drop-in replacements for the default
solutions.

## Requirements and Maintenance Schedule

This package has no dependencies outside of the core runtime of Go.  It
requires a recent version of Go.

This package follows the same maintenance schedule as the [Go
project](https://github.com/golang/go/wiki/Go-Release-Cycle#release-maintenance),
meaning that issues relating to versions of Go which aren't supported by the Go
team, or versions of this package which are older than 1 year, are unlikely to
be considered.

Additionally, we have fuzz tests which aren't a runtime required dependency but
will be pulled in when running `go mod tidy`.  Please don't include these go.mod
updates in change requests.

## encoding/json [![GoDoc](https://godoc.org/github.com/segmentio/encoding/json?status.svg)](https://godoc.org/github.com/segmentio/encoding/json)

More details about _how_ this package achieves a lower CPU and memory footprint
can be found [in the package README](../../../README.md).

The `json` sub-package provides a re-implementation of the functionalities
offered by the standard library's [`encoding/json`](https://golang.org/pkg/encoding/json/)
package, with a focus on lowering the CPU and memory footprint of the code.

The exported API of this package mirrors the standard library's
[`encoding/json`](https://golang.org/pkg/encoding/json/) package, the only
change needed to take advantage of the performance improvements is the import
path of the `json` package, from:
```go
import (
    "encoding/json"
)
```
to
```go
import (
    "github.com/segmentio/encoding/json"
)
```

The improvement can be significant for code that heavily relies on serializing
and deserializing JSON payloads. The CI pipeline runs benchmarks to compare the
performance of the package with the standard library and other popular
alternatives; here's an overview of the results:

**Comparing to encoding/json (`v1.16.2`)**
```
name                           old time/op    new time/op     delta
Marshal/*json.codeResponse2      6.40ms ± 2%     3.82ms ± 1%   -40.29%  (p=0.008 n=5+5)
Unmarshal/*json.codeResponse2    28.1ms ± 3%      5.6ms ± 3%   -80.21%  (p=0.008 n=5+5)

name                           old speed      new speed       delta
Marshal/*json.codeResponse2     303MB/s ± 2%    507MB/s ± 1%   +67.47%  (p=0.008 n=5+5)
Unmarshal/*json.codeResponse2  69.2MB/s ± 3%  349.6MB/s ± 3%  +405.42%  (p=0.008 n=5+5)

name                           old alloc/op   new alloc/op    delta
Marshal/*json.codeResponse2       0.00B           0.00B           ~     (all equal)
Unmarshal/*json.codeResponse2    1.80MB ± 1%     0.02MB ± 0%   -99.14%  (p=0.016 n=5+4)

name                           old allocs/op  new allocs/op   delta
Marshal/*json.codeResponse2        0.00            0.00           ~     (all equal)
Unmarshal/*json.codeResponse2     76.6k ± 0%       0.1k ± 3%   -99.92%  (p=0.008 n=5+5)
```

*Benchmarks were run on a Core i9-8950HK CPU @ 2.90GHz.*

**Comparing to github.com/json-iterator/go (`v1.1.10`)**
```
name                           old time/op    new time/op    delta
Marshal/*json.codeResponse2      6.19ms ± 3%    3.82ms ± 1%   -38.26%  (p=0.008 n=5+5)
Unmarshal/*json.codeResponse2    8.52ms ± 3%    5.55ms ± 3%   -34.84%  (p=0.008 n=5+5)

name                           old speed      new speed      delta
Marshal/*json.codeResponse2     313MB/s ± 3%   507MB/s ± 1%   +61.91%  (p=0.008 n=5+5)
Unmarshal/*json.codeResponse2   228MB/s ± 3%   350MB/s ± 3%   +53.50%  (p=0.008 n=5+5)

name                           old alloc/op   new alloc/op   delta
Marshal/*json.codeResponse2       8.00B ± 0%     0.00B       -100.00%  (p=0.008 n=5+5)
Unmarshal/*json.codeResponse2    1.05MB ± 0%    0.02MB ± 0%   -98.53%  (p=0.000 n=5+4)

name                           old allocs/op  new allocs/op  delta
Marshal/*json.codeResponse2        1.00 ± 0%      0.00       -100.00%  (p=0.008 n=5+5)
Unmarshal/*json.codeResponse2     37.2k ± 0%      0.1k ± 3%   -99.83%  (p=0.008 n=5+5)
```

Although this package aims to be a drop-in replacement of [`encoding/json`](https://golang.org/pkg/encoding/json/),
it does not guarantee the same error messages. It will error in the same cases
as the standard library, but the exact error message may be different.

## encoding/iso8601 [![GoDoc](https://godoc.org/github.com/segmentio/encoding/iso8601?status.svg)](https://godoc.org/github.com/segmentio/encoding/iso8601)

The `iso8601` sub-package exposes APIs to efficiently deal with with string
representations of iso8601 dates.

Data formats like JSON have no syntaxes to represent dates, they are usually
serialized and represented as a string value. In our experience, we often have
to _check_ whether a string value looks like a date, and either construct a
`time.Time` by parsing it or simply treat it as a `string`. This check can be
done by attempting to parse the value, and if it fails fallback to using the
raw string. Unfortunately, while the _happy path_ for `time.Parse` is fairly
efficient, constructing errors is much slower and has a much bigger memory
footprint.

We've developed fast iso8601 validation functions that cause no heap allocations
to remediate this problem. We added a validation step to determine whether
the value is a date representation or a simple string. This reduced CPU and
memory usage by 5% in some programs that were doing `time.Parse` calls on very
hot code paths.
```

## File: `go.mod`
```
module github.com/segmentio/encoding

go 1.23

require github.com/segmentio/asm v1.1.3

require golang.org/x/sys v0.0.0-20211110154304-99a53858aa08 // indirect
```

## File: `go.sum`
```
github.com/segmentio/asm v1.1.3 h1:WM03sfUOENvvKexOLp+pCqgb/WDjsi7EK8gIsICtzhc=
github.com/segmentio/asm v1.1.3/go.mod h1:Ld3L4ZXGNcSLRg4JBsZ3//1+f/TjYl0Mzen/DQy1EJg=
golang.org/x/sys v0.0.0-20211110154304-99a53858aa08 h1:WecRHqgE09JBkh/584XIE6PMz5KKE/vER4izNUi30AQ=
golang.org/x/sys v0.0.0-20211110154304-99a53858aa08/go.mod h1:oPkhp1MJrh7nUepCBck5+mAzfO9JrbApNNgaTdGDITg=
```

## File: `ascii/ascii_test.go`
```go
package ascii

import (
	"bytes"
	"fmt"
	"strings"
	"testing"
	"unicode/utf8"
)

var testStrings = [...]string{
	"",
	"a",
	"ab",
	"abc",
	"abcd",
	"hello",
	"Hello World!",
	"Hello\"World!",
	"Hello\\World!",
	"Hello\nWorld!",
	"Hello\rWorld!",
	"Hello\tWorld!",
	"Hello\bWorld!",
	"Hello\fWorld!",
	"H~llo World!",
	"H~llo",
	"你好",
	"~",
	"\x80",
	"\x7F",
	"\xFF",
	"\x1fxxx",
	"\x1fxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
	"a string of 16B.",
	"an invalid string of 32B. \x00......",
	"some kind of long string with only ascii characters.",
	"some kind of long string with a non-ascii character at the end.\xff",
	strings.Repeat("1234567890", 1000),
}

var testStringsUTF8 []string

func init() {
	for _, test := range testStrings {
		if utf8.ValidString(test) {
			testStringsUTF8 = append(testStringsUTF8, test)
		}
	}
}

func testString(s string, f func(byte) bool) bool {
	for i := range s {
		if !f(s[i]) {
			return false
		}
	}
	return true
}

func testValid(s string) bool {
	return testString(s, ValidByte)
}

func testValidPrint(s string) bool {
	return testString(s, ValidPrintByte)
}

func TestValid(t *testing.T) {
	testValidationFunction(t, testValid, ValidString)
}

func TestValidPrint(t *testing.T) {
	testValidationFunction(t, testValidPrint, ValidPrintString)
}

func testValidationFunction(t *testing.T, reference, function func(string) bool) {
	for _, test := range testStrings {
		t.Run(limit(test), func(t *testing.T) {
			expect := reference(test)

			if valid := function(test); expect != valid {
				t.Errorf("expected %t but got %t", expect, valid)
			}
		})
	}
}

func BenchmarkValid(b *testing.B) {
	benchmarkValidationFunction(b, ValidString)
}

func BenchmarkValidPrint(b *testing.B) {
	benchmarkValidationFunction(b, ValidPrintString)
}

func benchmarkValidationFunction(b *testing.B, function func(string) bool) {
	for _, test := range testStrings {
		b.Run(limit(test), func(b *testing.B) {
			for range b.N {
				_ = function(test)
			}
			b.SetBytes(int64(len(test)))
		})
	}
}

func limit(s string) string {
	if len(s) > 17 {
		return s[:17] + "..."
	}
	return s
}

func TestHasPrefixFold(t *testing.T) {
	for _, test := range testStringsUTF8 {
		t.Run(limit(test), func(t *testing.T) {
			prefix := test
			if len(prefix) > 0 {
				prefix = prefix[:len(prefix)/2]
			}
			upper := strings.ToUpper(prefix)
			lower := strings.ToLower(prefix)

			if !HasPrefixFoldString(test, prefix) {
				t.Errorf("%q does not match %q", test, prefix)
			}

			if !HasPrefixFoldString(test, upper) {
				t.Errorf("%q does not match %q", test, upper)
			}

			if !HasPrefixFoldString(test, lower) {
				t.Errorf("%q does not match %q", test, lower)
			}
		})
	}
}

func TestHasSuffixFold(t *testing.T) {
	for _, test := range testStringsUTF8 {
		t.Run(limit(test), func(t *testing.T) {
			suffix := test
			if len(suffix) > 0 {
				suffix = suffix[len(suffix)/2:]
			}
			upper := strings.ToUpper(suffix)
			lower := strings.ToLower(suffix)

			if !HasSuffixFoldString(test, suffix) {
				t.Errorf("%q does not match %q", test, suffix)
			}

			if !HasSuffixFoldString(test, upper) {
				t.Errorf("%q does not match %q", test, upper)
			}

			if !HasSuffixFoldString(test, lower) {
				t.Errorf("%q does not match %q", test, lower)
			}
		})
	}
}

func TestEqualFoldASCII(t *testing.T) {
	pairs := [...][2]byte{
		{0, ' '},
		{'@', '`'},
		{'[', '{'},
		{'_', 127},
	}

	for _, pair := range pairs {
		t.Run(fmt.Sprintf("0x%02x=0x%02x", pair[0], pair[1]), func(t *testing.T) {
			for i := 1; i <= 256; i++ {
				a := bytes.Repeat([]byte{'x'}, i)
				b := bytes.Repeat([]byte{'X'}, i)

				if !EqualFold(a, b) {
					t.Errorf("%q does not match %q", a, b)
					break
				}

				a[0] = pair[0]
				b[0] = pair[1]

				if EqualFold(a, b) {
					t.Errorf("%q matches %q", a, b)
					break
				}
			}
		})
	}
}

func TestEqualFold(t *testing.T) {
	// Only test valid UTF-8 otherwise ToUpper/ToLower will convert invalid
	// characters to UTF-8 placeholders, which breaks the case-insensitive
	// equality.
	for _, test := range testStringsUTF8 {
		t.Run(limit(test), func(t *testing.T) {
			upper := strings.ToUpper(test)
			lower := strings.ToLower(test)

			if !EqualFoldString(test, test) {
				t.Errorf("%q does not match %q", test, test)
			}

			if !EqualFoldString(test, upper) {
				t.Errorf("%q does not match %q", test, upper)
			}

			if !EqualFoldString(test, lower) {
				t.Errorf("%q does not match %q", test, lower)
			}

			if len(test) > 1 {
				reverse := make([]byte, len(test))
				for i := range reverse {
					reverse[i] = test[len(test)-(i+1)]
				}

				if EqualFoldString(test, string(reverse)) {
					t.Errorf("%q matches %q", test, reverse)
				}
			}
		})
	}
}

func BenchmarkEqualFold(b *testing.B) {
	for _, test := range testStringsUTF8 {
		b.Run(limit(test), func(b *testing.B) {
			other := test + "_" // not the same pointer

			for range b.N {
				_ = EqualFoldString(test, other[:len(test)]) // same length
			}

			b.SetBytes(int64(len(test)))
		})
	}
}
```

## File: `ascii/equal_fold.go`
```go
//go:generate go run equal_fold_asm.go -out equal_fold_amd64.s -stubs equal_fold_amd64.go
package ascii

import (
	"github.com/segmentio/asm/ascii"
)

// EqualFold is a version of bytes.EqualFold designed to work on ASCII input
// instead of UTF-8.
//
// When the program has guarantees that the input is composed of ASCII
// characters only, it allows for greater optimizations.
func EqualFold(a, b []byte) bool {
	return ascii.EqualFold(a, b)
}

func HasPrefixFold(s, prefix []byte) bool {
	return ascii.HasPrefixFold(s, prefix)
}

func HasSuffixFold(s, suffix []byte) bool {
	return ascii.HasSuffixFold(s, suffix)
}

// EqualFoldString is a version of strings.EqualFold designed to work on ASCII
// input instead of UTF-8.
//
// When the program has guarantees that the input is composed of ASCII
// characters only, it allows for greater optimizations.
func EqualFoldString(a, b string) bool {
	return ascii.EqualFoldString(a, b)
}

func HasPrefixFoldString(s, prefix string) bool {
	return ascii.HasPrefixFoldString(s, prefix)
}

func HasSuffixFoldString(s, suffix string) bool {
	return ascii.HasSuffixFoldString(s, suffix)
}
```

## File: `ascii/valid.go`
```go
//go:generate go run valid_asm.go -out valid_amd64.s -stubs valid_amd64.go
package ascii

import (
	"github.com/segmentio/asm/ascii"
)

// Valid returns true if b contains only ASCII characters.
func Valid(b []byte) bool {
	return ascii.Valid(b)
}

// ValidBytes returns true if b is an ASCII character.
func ValidByte(b byte) bool {
	return ascii.ValidByte(b)
}

// ValidBytes returns true if b is an ASCII character.
func ValidRune(r rune) bool {
	return ascii.ValidRune(r)
}

// ValidString returns true if s contains only ASCII characters.
func ValidString(s string) bool {
	return ascii.ValidString(s)
}
```

## File: `ascii/valid_print.go`
```go
//go:generate go run valid_print_asm.go -out valid_print_amd64.s -stubs valid_print_amd64.go
package ascii

import (
	"github.com/segmentio/asm/ascii"
)

// Valid returns true if b contains only printable ASCII characters.
func ValidPrint(b []byte) bool {
	return ascii.ValidPrint(b)
}

// ValidBytes returns true if b is an ASCII character.
func ValidPrintByte(b byte) bool {
	return ascii.ValidPrintByte(b)
}

// ValidBytes returns true if b is an ASCII character.
func ValidPrintRune(r rune) bool {
	return ascii.ValidPrintRune(r)
}

// ValidString returns true if s contains only printable ASCII characters.
func ValidPrintString(s string) bool {
	return ascii.ValidPrintString(s)
}
```

## File: `benchmarks/Makefile`
```
benchmark.dir ?= results
benchmark.batch ?= 1000
benchmark.count ?= 8

benchmark.encoding.json := $(benchmark.dir)/encoding-json
benchmark.github.com.json-iterator.go := $(benchmark.dir)/json-iterator
benchmark.github.com.segmentio.encoding.json := $(benchmark.dir)/segment-encoding-json
benchmark.github.com.mailru.easyjson := $(benchmark.dir)/easyjson
benchmark.github.com.protobuf.v1 := $(benchmark.dir)/segment-protobuf-v1
benchmark.vmihailenco.msgpack := $(benchmark.dir)/vmihailenco-msgpack
benchmark.tinylib.msgp := $(benchmark.dir)/tinylib-msgp

benchmark.encoding.json.gzip := $(benchmark.dir)/encoding-json+gzip
benchmark.github.com.json-iterator.go.gzip := $(benchmark.dir)/json-iterator+gzip
benchmark.github.com.segmentio.encoding.json.gzip := $(benchmark.dir)/segment-encoding-json+gzip
benchmark.github.com.mailru.easyjson.gzip := $(benchmark.dir)/easyjson+gzip
benchmark.github.com.protobuf.v1.gzip := $(benchmark.dir)/segment-protobuf-v1+gzip
benchmark.vmihailenco.msgpack.gzip := $(benchmark.dir)/vmihailenco-msgpack+gzip
benchmark.tinylib.msgp.gzip := $(benchmark.dir)/tinylib-msgp+gzip

benchmark.encoding.json.snappy := $(benchmark.dir)/encoding-json+snappy
benchmark.github.com.json-iterator.go.snappy := $(benchmark.dir)/json-iterator+snappy
benchmark.github.com.segmentio.encoding.json.snappy := $(benchmark.dir)/segment-encoding-json+snappy
benchmark.github.com.mailru.easyjson.snappy := $(benchmark.dir)/easyjson+snappy
benchmark.github.com.protobuf.v1.snappy := $(benchmark.dir)/segment-protobuf-v1+snappy
benchmark.vmihailenco.msgpack.snappy := $(benchmark.dir)/vmihailenco-msgpack+snappy
benchmark.tinylib.msgp.snappy := $(benchmark.dir)/tinylib-msgp+snappy

benchmark.encoding.json.zstd := $(benchmark.dir)/encoding-json+zstd
benchmark.github.com.json-iterator.go.zstd := $(benchmark.dir)/json-iterator+zstd
benchmark.github.com.segmentio.encoding.json.zstd := $(benchmark.dir)/segment-encoding-json+zstd
benchmark.github.com.mailru.easyjson.zstd := $(benchmark.dir)/easyjson+zstd
benchmark.github.com.protobuf.v1.zstd := $(benchmark.dir)/segment-protobuf-v1+zstd
benchmark.vmihailenco.msgpack.zstd := $(benchmark.dir)/vmihailenco-msgpack+zstd
benchmark.tinylib.msgp.zstd := $(benchmark.dir)/tinylib-msgp+zstd

benchmark.data := ../json/testdata/msgs.json.gz
benchmark.msgs := $(benchmark.dir)/msgs.json
benchmark.bin := $(benchmark.dir)/benchmark
benchmark.cmd.dir := cmd/benchmark
benchmark.src := $(wildcard ./$(benchmark.cmd.dir)/*.go)
benchmark.out := \
	$(benchmark.encoding.json).txt \
	$(benchmark.github.com.json-iterator.go).txt \
	$(benchmark.github.com.segmentio.encoding.json).txt \
	$(benchmark.github.com.mailru.easyjson).txt \
	$(benchmark.github.com.protobuf.v1).txt \
	$(benchmark.vmihailenco.msgpack).txt \
	$(benchmark.tinylib.msgp).txt \
	$(benchmark.encoding.json.gzip).txt \
	$(benchmark.github.com.json-iterator.go.gzip).txt \
	$(benchmark.github.com.segmentio.encoding.json.gzip).txt \
	$(benchmark.github.com.mailru.easyjson.gzip).txt \
	$(benchmark.github.com.protobuf.v1.gzip).txt \
	$(benchmark.vmihailenco.msgpack.gzip).txt \
	$(benchmark.tinylib.msgp.gzip).txt \
	$(benchmark.encoding.json.snappy).txt \
	$(benchmark.github.com.json-iterator.go.snappy).txt \
	$(benchmark.github.com.segmentio.encoding.json.snappy).txt \
	$(benchmark.github.com.mailru.easyjson.snappy).txt \
	$(benchmark.github.com.protobuf.v1.snappy).txt \
	$(benchmark.vmihailenco.msgpack.snappy).txt \
	$(benchmark.tinylib.msgp.snappy).txt \
	$(benchmark.encoding.json.zstd).txt \
	$(benchmark.github.com.json-iterator.go.zstd).txt \
	$(benchmark.github.com.segmentio.encoding.json.zstd).txt \
	$(benchmark.github.com.mailru.easyjson.zstd).txt \
	$(benchmark.github.com.protobuf.v1.zstd).txt \
	$(benchmark.vmihailenco.msgpack.zstd).txt \
	$(benchmark.tinylib.msgp.zstd).txt

benchstat := ${GOPATH}/bin/benchstat

all:

$(benchstat):
	go install golang.org/x/perf/cmd/benchstat@latest

$(benchmark.cmd.dir)/message.pb.go: $(benchmark.cmd.dir)/message.proto
	@protoc -I. \
		-I$(GOPATH)/src \
		-I$(GOPATH)/src/github.com/gogo/protobuf/protobuf \
		--gogofaster_out=\
Mgoogle/protobuf/struct.proto=github.com/gogo/protobuf/types,\
Mgoogle/protobuf/timestamp.proto=github.com/gogo/protobuf/types:.\
		$(benchmark.cmd.dir)/message.proto

bench: $(benchstat) $(benchmark.out)
	@for file in $(benchmark.out); do \
		echo '======' $$(basename $$file | sed 's/.txt//') '======'; \
		cat $$(echo $$file | sed 's/.txt/.log/'); \
		echo; \
		$(benchstat) $(benchmark.encoding.json).txt $$file; \
		echo; \
	done

$(benchmark.dir):
	mkdir -p $(benchmark.dir)

$(benchmark.bin): $(benchmark.src)
	go build -o $(benchmark.bin) ./$(benchmark.cmd.dir)

$(benchmark.msgs): $(benchmark.dir) $(benchmark.data)
	cat $(benchmark.data) | gzip -d > $(benchmark.msgs)

$(benchmark.encoding.json).txt: $(benchmark.msgs) $(benchmark.bin)
	cat $(benchmark.msgs) | $(benchmark.bin) -count $(benchmark.count) -batch $(benchmark.batch) -package encoding/json \
		1> $(benchmark.encoding.json).txt \
		2> $(benchmark.encoding.json).log

$(benchmark.github.com.json-iterator.go).txt: $(benchmark.msgs) $(benchmark.bin)
	cat $(benchmark.msgs) | $(benchmark.bin) -count $(benchmark.count) -batch $(benchmark.batch) -package github.com/json-iterator/go \
		1> $(benchmark.github.com.json-iterator.go).txt \
		2> $(benchmark.github.com.json-iterator.go).log

$(benchmark.github.com.segmentio.encoding.json).txt: $(benchmark.msgs) $(benchmark.bin)
	cat $(benchmark.msgs) | $(benchmark.bin) -count $(benchmark.count) -batch $(benchmark.batch) -package github.com/segmentio/encoding/json \
		1> $(benchmark.github.com.segmentio.encoding.json).txt \
		2> $(benchmark.github.com.segmentio.encoding.json).log

$(benchmark.github.com.mailru.easyjson).txt: $(benchmark.msgs) $(benchmark.bin)
	cat $(benchmark.msgs) | $(benchmark.bin) -count $(benchmark.count) -batch $(benchmark.batch) -package github.com/mailru/easyjson \
		1> $(benchmark.github.com.mailru.easyjson).txt \
		2> $(benchmark.github.com.mailru.easyjson).log

$(benchmark.github.com.protobuf.v1).txt: $(benchmark.msgs) $(benchmark.bin)
	cat $(benchmark.msgs) | $(benchmark.bin) -count $(benchmark.count) -batch $(benchmark.batch) -package github.com/segmentio/protobuf/v1 \
		1> $(benchmark.github.com.protobuf.v1).txt \
		2> $(benchmark.github.com.protobuf.v1).log

$(benchmark.vmihailenco.msgpack).txt: $(benchmark.msgs) $(benchmark.bin)
	cat $(benchmark.msgs) | $(benchmark.bin) -count $(benchmark.count) -batch $(benchmark.batch) -package github.com/vmihailenco/msgpack \
		1> $(benchmark.vmihailenco.msgpack).txt \
		2> $(benchmark.vmihailenco.msgpack).log

$(benchmark.tinylib.msgp).txt: $(benchmark.msgs) $(benchmark.bin)
	cat $(benchmark.msgs) | $(benchmark.bin) -count $(benchmark.count) -batch $(benchmark.batch) -package github.com/tinylib/msgp \
		1> $(benchmark.tinylib.msgp).txt \
		2> $(benchmark.tinylib.msgp).log

$(benchmark.encoding.json.gzip).txt: $(benchmark.msgs) $(benchmark.bin)
	cat $(benchmark.msgs) | $(benchmark.bin) -count $(benchmark.count) -batch $(benchmark.batch) -package encoding/json -compression gzip \
		1> $(benchmark.encoding.json.gzip).txt \
		2> $(benchmark.encoding.json.gzip).log

$(benchmark.github.com.json-iterator.go.gzip).txt: $(benchmark.msgs) $(benchmark.bin)
	cat $(benchmark.msgs) | $(benchmark.bin) -count $(benchmark.count) -batch $(benchmark.batch) -package github.com/json-iterator/go -compression gzip \
		1> $(benchmark.github.com.json-iterator.go.gzip).txt \
		2> $(benchmark.github.com.json-iterator.go.gzip).log

$(benchmark.github.com.segmentio.encoding.json.gzip).txt: $(benchmark.msgs) $(benchmark.bin)
	cat $(benchmark.msgs) | $(benchmark.bin) -count $(benchmark.count) -batch $(benchmark.batch) -package github.com/segmentio/encoding/json -compression gzip \
		1> $(benchmark.github.com.segmentio.encoding.json.gzip).txt \
		2> $(benchmark.github.com.segmentio.encoding.json.gzip).log

$(benchmark.github.com.mailru.easyjson.gzip).txt: $(benchmark.msgs) $(benchmark.bin)
	cat $(benchmark.msgs) | $(benchmark.bin) -count $(benchmark.count) -batch $(benchmark.batch) -package github.com/mailru/easyjson -compression gzip \
		1> $(benchmark.github.com.mailru.easyjson.gzip).txt \
		2> $(benchmark.github.com.mailru.easyjson.gzip).log

$(benchmark.github.com.protobuf.v1.gzip).txt: $(benchmark.msgs) $(benchmark.bin)
	cat $(benchmark.msgs) | $(benchmark.bin) -count $(benchmark.count) -batch $(benchmark.batch) -package github.com/segmentio/protobuf/v1 -compression gzip \
		1> $(benchmark.github.com.protobuf.v1.gzip).txt \
		2> $(benchmark.github.com.protobuf.v1.gzip).log

$(benchmark.vmihailenco.msgpack.gzip).txt: $(benchmark.msgs) $(benchmark.bin)
	cat $(benchmark.msgs) | $(benchmark.bin) -count $(benchmark.count) -batch $(benchmark.batch) -package github.com/vmihailenco/msgpack -compression gzip \
		1> $(benchmark.vmihailenco.msgpack.gzip).txt \
		2> $(benchmark.vmihailenco.msgpack.gzip).log

$(benchmark.tinylib.msgp.gzip).txt: $(benchmark.msgs) $(benchmark.bin)
	cat $(benchmark.msgs) | $(benchmark.bin) -count $(benchmark.count) -batch $(benchmark.batch) -package github.com/tinylib/msgp -compression gzip \
		1> $(benchmark.tinylib.msgp.gzip).txt \
		2> $(benchmark.tinylib.msgp.gzip).log

$(benchmark.encoding.json.snappy).txt: $(benchmark.msgs) $(benchmark.bin)
	cat $(benchmark.msgs) | $(benchmark.bin) -count $(benchmark.count) -batch $(benchmark.batch) -package encoding/json -compression snappy \
		1> $(benchmark.encoding.json.snappy).txt \
		2> $(benchmark.encoding.json.snappy).log

$(benchmark.github.com.json-iterator.go.snappy).txt: $(benchmark.msgs) $(benchmark.bin)
	cat $(benchmark.msgs) | $(benchmark.bin) -count $(benchmark.count) -batch $(benchmark.batch) -package github.com/json-iterator/go -compression snappy \
		1> $(benchmark.github.com.json-iterator.go.snappy).txt \
		2> $(benchmark.github.com.json-iterator.go.snappy).log

$(benchmark.github.com.segmentio.encoding.json.snappy).txt: $(benchmark.msgs) $(benchmark.bin)
	cat $(benchmark.msgs) | $(benchmark.bin) -count $(benchmark.count) -batch $(benchmark.batch) -package github.com/segmentio/encoding/json -compression snappy \
		1> $(benchmark.github.com.segmentio.encoding.json.snappy).txt \
		2> $(benchmark.github.com.segmentio.encoding.json.snappy).log

$(benchmark.github.com.mailru.easyjson.snappy).txt: $(benchmark.msgs) $(benchmark.bin)
	cat $(benchmark.msgs) | $(benchmark.bin) -count $(benchmark.count) -batch $(benchmark.batch) -package github.com/mailru/easyjson -compression snappy \
		1> $(benchmark.github.com.mailru.easyjson.snappy).txt \
		2> $(benchmark.github.com.mailru.easyjson.snappy).log

$(benchmark.github.com.protobuf.v1.snappy).txt: $(benchmark.msgs) $(benchmark.bin)
	cat $(benchmark.msgs) | $(benchmark.bin) -count $(benchmark.count) -batch $(benchmark.batch) -package github.com/segmentio/protobuf/v1 -compression snappy \
		1> $(benchmark.github.com.protobuf.v1.snappy).txt \
		2> $(benchmark.github.com.protobuf.v1.snappy).log

$(benchmark.vmihailenco.msgpack.snappy).txt: $(benchmark.msgs) $(benchmark.bin)
	cat $(benchmark.msgs) | $(benchmark.bin) -count $(benchmark.count) -batch $(benchmark.batch) -package github.com/vmihailenco/msgpack -compression snappy \
		1> $(benchmark.vmihailenco.msgpack.snappy).txt \
		2> $(benchmark.vmihailenco.msgpack.snappy).log

$(benchmark.tinylib.msgp.snappy).txt: $(benchmark.msgs) $(benchmark.bin)
	cat $(benchmark.msgs) | $(benchmark.bin) -count $(benchmark.count) -batch $(benchmark.batch) -package github.com/tinylib/msgp -compression snappy \
		1> $(benchmark.tinylib.msgp.snappy).txt \
		2> $(benchmark.tinylib.msgp.snappy).log

$(benchmark.encoding.json.zstd).txt: $(benchmark.msgs) $(benchmark.bin)
	cat $(benchmark.msgs) | $(benchmark.bin) -count $(benchmark.count) -batch $(benchmark.batch) -package encoding/json -compression zstd \
		1> $(benchmark.encoding.json.zstd).txt \
		2> $(benchmark.encoding.json.zstd).log

$(benchmark.github.com.json-iterator.go.zstd).txt: $(benchmark.msgs) $(benchmark.bin)
	cat $(benchmark.msgs) | $(benchmark.bin) -count $(benchmark.count) -batch $(benchmark.batch) -package github.com/json-iterator/go -compression zstd \
		1> $(benchmark.github.com.json-iterator.go.zstd).txt \
		2> $(benchmark.github.com.json-iterator.go.zstd).log

$(benchmark.github.com.segmentio.encoding.json.zstd).txt: $(benchmark.msgs) $(benchmark.bin)
	cat $(benchmark.msgs) | $(benchmark.bin) -count $(benchmark.count) -batch $(benchmark.batch) -package github.com/segmentio/encoding/json -compression zstd \
		1> $(benchmark.github.com.segmentio.encoding.json.zstd).txt \
		2> $(benchmark.github.com.segmentio.encoding.json.zstd).log

$(benchmark.github.com.mailru.easyjson.zstd).txt: $(benchmark.msgs) $(benchmark.bin)
	cat $(benchmark.msgs) | $(benchmark.bin) -count $(benchmark.count) -batch $(benchmark.batch) -package github.com/mailru/easyjson -compression zstd \
		1> $(benchmark.github.com.mailru.easyjson.zstd).txt \
		2> $(benchmark.github.com.mailru.easyjson.zstd).log

$(benchmark.github.com.protobuf.v1.zstd).txt: $(benchmark.msgs) $(benchmark.bin)
	cat $(benchmark.msgs) | $(benchmark.bin) -count $(benchmark.count) -batch $(benchmark.batch) -package github.com/segmentio/protobuf/v1 -compression zstd \
		1> $(benchmark.github.com.protobuf.v1.zstd).txt \
		2> $(benchmark.github.com.protobuf.v1.zstd).log

$(benchmark.vmihailenco.msgpack.zstd).txt: $(benchmark.msgs) $(benchmark.bin)
	cat $(benchmark.msgs) | $(benchmark.bin) -count $(benchmark.count) -batch $(benchmark.batch) -package github.com/vmihailenco/msgpack -compression zstd \
		1> $(benchmark.vmihailenco.msgpack.zstd).txt \
		2> $(benchmark.vmihailenco.msgpack.zstd).log

$(benchmark.tinylib.msgp.zstd).txt: $(benchmark.msgs) $(benchmark.bin)
	cat $(benchmark.msgs) | $(benchmark.bin) -count $(benchmark.count) -batch $(benchmark.batch) -package github.com/tinylib/msgp -compression zstd \
		1> $(benchmark.tinylib.msgp.zstd).txt \
		2> $(benchmark.tinylib.msgp.zstd).log
```

## File: `benchmarks/go.mod`
```
module github.com/segmentio/encoding/benchmarks

go 1.13

require (
	github.com/DataDog/zstd v1.4.1
	github.com/gogo/protobuf v1.3.1
	github.com/golang/snappy v0.0.1
	github.com/google/uuid v1.0.0
	github.com/json-iterator/go v1.1.7
	github.com/kr/pretty v0.1.0 // indirect
	github.com/mailru/easyjson v0.7.0
	github.com/modern-go/concurrent v0.0.0-20180306012644-bacd9c7ef1dd // indirect
	github.com/modern-go/reflect2 v1.0.1 // indirect
	github.com/philhofer/fwd v1.0.0 // indirect
	github.com/segmentio/encoding v0.1.1
	github.com/tinylib/msgp v1.1.0
	github.com/vmihailenco/msgpack v4.0.4+incompatible
	golang.org/x/net v0.0.0-20190620200207-3b0461eec859 // indirect
	golang.org/x/sync v0.0.0-20190423024810-112230192c58 // indirect
	google.golang.org/appengine v1.2.0 // indirect
	gopkg.in/check.v1 v1.0.0-20180628173108-788fd7840127 // indirect
)
```

## File: `benchmarks/go.sum`
```
github.com/DataDog/zstd v1.4.1 h1:3oxKN3wbHibqx897utPC2LTQU4J+IHWWJO+glkAkpFM=
github.com/DataDog/zstd v1.4.1/go.mod h1:1jcaCB/ufaK+sKp1NBhlGmpz41jOoPQ35bpF36t7BBo=
github.com/davecgh/go-spew v1.1.0/go.mod h1:J7Y8YcW2NihsgmVo/mv3lAwl/skON4iLHjSsI+c5H38=
github.com/davecgh/go-spew v1.1.1 h1:vj9j/u1bqnvCEfJOwUhtlOARqs3+rkHYY13jYWTU97c=
github.com/davecgh/go-spew v1.1.1/go.mod h1:J7Y8YcW2NihsgmVo/mv3lAwl/skON4iLHjSsI+c5H38=
github.com/gogo/protobuf v1.3.1 h1:DqDEcV5aeaTmdFBePNpYsp3FlcVH/2ISVVM9Qf8PSls=
github.com/gogo/protobuf v1.3.1/go.mod h1:SlYgWuQ5SjCEi6WLHjHCa1yvBfUnHcTbrrZtXPKa29o=
github.com/golang/protobuf v1.2.0 h1:P3YflyNX/ehuJFLhxviNdFxQPkGK5cDcApsge1SqnvM=
github.com/golang/protobuf v1.2.0/go.mod h1:6lQm79b+lXiMfvg/cZm0SGofjICqVBUtrP5yJMmIC1U=
github.com/golang/snappy v0.0.1 h1:Qgr9rKW7uDUkrbSmQeiDsGa8SjGyCOGtuasMWwvp2P4=
github.com/golang/snappy v0.0.1/go.mod h1:/XxbfmMg8lxefKM7IXC3fBNl/7bRcc72aCRzEWrmP2Q=
github.com/google/gofuzz v1.0.0/go.mod h1:dBl0BpW6vV/+mYPU4Po3pmUjxk6FQPldtuIdl/M65Eg=
github.com/google/uuid v1.0.0 h1:b4Gk+7WdP/d3HZH8EJsZpvV7EtDOgaZLtnaNGIu1adA=
github.com/google/uuid v1.0.0/go.mod h1:TIyPZe4MgqvfeYDBFedMoGGpEw/LqOeaOT+nhxU+yHo=
github.com/json-iterator/go v1.1.7 h1:KfgG9LzI+pYjr4xvmz/5H4FXjokeP+rlHLhv3iH62Fo=
github.com/json-iterator/go v1.1.7/go.mod h1:KdQUCv79m/52Kvf8AW2vK1V8akMuk1QjK/uOdHXbAo4=
github.com/kisielk/errcheck v1.2.0/go.mod h1:/BMXB+zMLi60iA8Vv6Ksmxu/1UDYcXs4uQLJ+jE2L00=
github.com/kisielk/gotool v1.0.0/go.mod h1:XhKaO+MFFWcvkIS/tQcRk01m1F5IRFswLeQ+oQHNcck=
github.com/kr/pretty v0.1.0 h1:L/CwN0zerZDmRFUapSPitk6f+Q3+0za1rQkzVuMiMFI=
github.com/kr/pretty v0.1.0/go.mod h1:dAy3ld7l9f0ibDNOQOHHMYYIIbhfbHSm3C4ZsoJORNo=
github.com/kr/pty v1.1.1/go.mod h1:pFQYn66WHrOpPYNljwOMqo10TkYh1fy3cYio2l3bCsQ=
github.com/kr/text v0.1.0 h1:45sCR5RtlFHMR4UwH9sdQ5TC8v0qDQCHnXt+kaKSTVE=
github.com/kr/text v0.1.0/go.mod h1:4Jbv+DJW3UT/LiOwJeYQe1efqtUx/iVham/4vfdArNI=
github.com/mailru/easyjson v0.7.0 h1:aizVhC/NAAcKWb+5QsU1iNOZb4Yws5UO2I+aIprQITM=
github.com/mailru/easyjson v0.7.0/go.mod h1:KAzv3t3aY1NaHWoQz1+4F1ccyAH66Jk7yos7ldAVICs=
github.com/modern-go/concurrent v0.0.0-20180228061459-e0a39a4cb421/go.mod h1:6dJC0mAP4ikYIbvyc7fijjWJddQyLn8Ig3JB5CqoB9Q=
github.com/modern-go/concurrent v0.0.0-20180306012644-bacd9c7ef1dd h1:TRLaZ9cD/w8PVh93nsPXa1VrQ6jlwL5oN8l14QlcNfg=
github.com/modern-go/concurrent v0.0.0-20180306012644-bacd9c7ef1dd/go.mod h1:6dJC0mAP4ikYIbvyc7fijjWJddQyLn8Ig3JB5CqoB9Q=
github.com/modern-go/reflect2 v0.0.0-20180701023420-4b7aa43c6742/go.mod h1:bx2lNnkwVCuqBIxFjflWJWanXIb3RllmbCylyMrvgv0=
github.com/modern-go/reflect2 v1.0.1 h1:9f412s+6RmYXLWZSEzVVgPGK7C2PphHj5RJrvfx9AWI=
github.com/modern-go/reflect2 v1.0.1/go.mod h1:bx2lNnkwVCuqBIxFjflWJWanXIb3RllmbCylyMrvgv0=
github.com/philhofer/fwd v1.0.0 h1:UbZqGr5Y38ApvM/V/jEljVxwocdweyH+vmYvRPBnbqQ=
github.com/philhofer/fwd v1.0.0/go.mod h1:gk3iGcWd9+svBvR0sR+KPcfE+RNWozjowpeBVG3ZVNU=
github.com/pmezard/go-difflib v1.0.0 h1:4DBwDE0NGyQoBHbLQYPwSUPoCMWR5BEzIk/f1lZbAQM=
github.com/pmezard/go-difflib v1.0.0/go.mod h1:iKH77koFhYxTK1pcRnkKkqfTogsbg7gZNVY4sRDYZ/4=
github.com/segmentio/encoding v0.1.0 h1:V/FrZFA2Fm4Hpk3JdA+3JWN6fJnp15dZOnB+CI3Wcbw=
github.com/segmentio/encoding v0.1.0/go.mod h1:RWhr02uzMB9gQC1x+MfYxedtmBibb9cZ6Vv9VxRSSbw=
github.com/segmentio/encoding v0.1.1 h1:L2CR2XRdOOBhwvyAilVG+jDGQFdfcqCKPTGdE46bC74=
github.com/segmentio/encoding v0.1.1/go.mod h1:RWhr02uzMB9gQC1x+MfYxedtmBibb9cZ6Vv9VxRSSbw=
github.com/stretchr/objx v0.1.0/go.mod h1:HFkY916IF+rwdDfMAkV7OtwuqBVzrE8GR6GFx+wExME=
github.com/stretchr/testify v1.3.0 h1:TivCn/peBQ7UY8ooIcPgZFpTNSz0Q2U6UrFlUfqbe0Q=
github.com/stretchr/testify v1.3.0/go.mod h1:M5WIy9Dh21IEIfnGCwXGc5bZfKNJtfHm1UVUgZn+9EI=
github.com/tinylib/msgp v1.1.0 h1:9fQd+ICuRIu/ue4vxJZu6/LzxN0HwMds2nq/0cFvxHU=
github.com/tinylib/msgp v1.1.0/go.mod h1:+d+yLhGm8mzTaHzB+wgMYrodPfmZrzkirds8fDWklFE=
github.com/vmihailenco/msgpack v4.0.4+incompatible h1:dSLoQfGFAo3F6OoNhwUmLwVgaUXK79GlxNBwueZn0xI=
github.com/vmihailenco/msgpack v4.0.4+incompatible/go.mod h1:fy3FlTQTDXWkZ7Bh6AcGMlsjHatGryHQYUTf1ShIgkk=
golang.org/x/crypto v0.0.0-20190308221718-c2843e01d9a2/go.mod h1:djNgcEr1/C05ACkg1iLfiJU5Ep61QUkGW8qpdssI0+w=
golang.org/x/net v0.0.0-20180724234803-3673e40ba225/go.mod h1:mL1N/T3taQHkDXs73rZJwtUhF3w3ftmwwsq0BUmARs4=
golang.org/x/net v0.0.0-20190620200207-3b0461eec859 h1:R/3boaszxrf1GEUWTVDzSKVwLmSJpwZ1yqXm8j0v2QI=
golang.org/x/net v0.0.0-20190620200207-3b0461eec859/go.mod h1:z5CRVTTTmAJ677TzLLGU+0bjPO0LkuOLi4/5GtJWs/s=
golang.org/x/sync v0.0.0-20190423024810-112230192c58 h1:8gQV6CLnAEikrhgkHFbMAEhagSSnXWGV915qUMm9mrU=
golang.org/x/sync v0.0.0-20190423024810-112230192c58/go.mod h1:RxMgew5VJxzue5/jJTE5uejpjVlOe/izrB70Jof72aM=
golang.org/x/sys v0.0.0-20190215142949-d0b11bdaac8a/go.mod h1:STP8DvDyc/dI5b8T5hshtkjS+E42TnysNCUPdjciGhY=
golang.org/x/text v0.3.0/go.mod h1:NqM8EUOU14njkJ3fqMW+pc6Ldnwhi/IjpwHt7yyuwOQ=
golang.org/x/tools v0.0.0-20181030221726-6c7e314b6563/go.mod h1:n7NCudcB/nEzxVGmLbDWY5pfWTLqBcC2KZ6jyYvM4mQ=
google.golang.org/appengine v1.2.0 h1:S0iUepdCWODXRvtE+gcRDd15L+k+k1AiHlMiMjefH24=
google.golang.org/appengine v1.2.0/go.mod h1:xpcJRLb0r/rnEns0DIKYYv+WjYCduHsrkT7/EB5XEv4=
gopkg.in/check.v1 v1.0.0-20180628173108-788fd7840127 h1:qIbj1fsPNlZgppZ+VLlY7N33q108Sa+fhmuc+sWQYwY=
gopkg.in/check.v1 v1.0.0-20180628173108-788fd7840127/go.mod h1:Co6ibVJAznAaIkqp8huTwlJQCZ016jof/cbN4VW5Yz0=
```

## File: `benchmarks/results/easyjson+gzip.log`
```
goos: darwin
goarch: amd64
pkg: github.com/mailru/easyjson
compression: gzip
avg size: 1083.83 KB
min size: 1050.79 KB
max size: 1109.25 KB
```

## File: `benchmarks/results/easyjson+gzip.txt`
```
BenchmarkEncoding/count=20		200000		78793 ns/op		14.09 MB/s		17599 B/op		297 allocs/op		1.08 KB/msg
```

## File: `benchmarks/results/easyjson+snappy.log`
```
goos: darwin
goarch: amd64
pkg: github.com/mailru/easyjson
compression: snappy
avg size: 1415.50 KB
min size: 1369.04 KB
max size: 1468.66 KB
```

## File: `benchmarks/results/easyjson+snappy.txt`
```
BenchmarkEncoding/count=20		200000		46097 ns/op		31.44 MB/s		17568 B/op		297 allocs/op		1.42 KB/msg
```

## File: `benchmarks/results/easyjson+zstd.log`
```
goos: darwin
goarch: amd64
pkg: github.com/mailru/easyjson
compression: zstd
avg size: 974.70 KB
min size: 943.27 KB
max size: 1000.17 KB
```

## File: `benchmarks/results/easyjson+zstd.txt`
```
BenchmarkEncoding/count=20		200000		49942 ns/op		19.98 MB/s		17591 B/op		297 allocs/op		0.97 KB/msg
```

## File: `benchmarks/results/easyjson.log`
```
goos: darwin
goarch: amd64
pkg: github.com/mailru/easyjson
avg size: 2026.88 KB
min size: 1959.94 KB
max size: 2076.68 KB
```

## File: `benchmarks/results/encoding-json+gzip.log`
```
goos: darwin
goarch: amd64
pkg: encoding/json
compression: gzip
#187: json: cannot unmarshal number into Go struct field Message.userId of type string
errors: 2/10000
avg size: 1075.97 KB
min size: 1044.33 KB
max size: 1100.51 KB
```

## File: `benchmarks/results/encoding-json+gzip.txt`
```
BenchmarkEncoding/count=20		200000		101048 ns/op		10.90 MB/s		15780 B/op		423 allocs/op		1.08 KB/msg
```

## File: `benchmarks/results/encoding-json+snappy.log`
```
goos: darwin
goarch: amd64
pkg: encoding/json
compression: snappy
#187: json: cannot unmarshal number into Go struct field Message.userId of type string
errors: 2/10000
avg size: 1408.08 KB
min size: 1363.64 KB
max size: 1451.60 KB
```

## File: `benchmarks/results/encoding-json+snappy.txt`
```
BenchmarkEncoding/count=20		200000		69750 ns/op		20.67 MB/s		15743 B/op		423 allocs/op		1.41 KB/msg
```

## File: `benchmarks/results/encoding-json+zstd.log`
```
goos: darwin
goarch: amd64
pkg: encoding/json
compression: zstd
#187: json: cannot unmarshal number into Go struct field Message.userId of type string
errors: 2/10000
avg size: 952.03 KB
min size: 922.46 KB
max size: 978.53 KB
```

## File: `benchmarks/results/encoding-json+zstd.txt`
```
BenchmarkEncoding/count=20		200000		72932 ns/op		13.37 MB/s		15767 B/op		423 allocs/op		0.95 KB/msg
```

## File: `benchmarks/results/encoding-json.log`
```
goos: darwin
goarch: amd64
pkg: encoding/json
#187: json: cannot unmarshal number into Go struct field Message.userId of type string
errors: 2/10000
avg size: 2027.14 KB
min size: 1960.16 KB
max size: 2076.95 KB
```

## File: `benchmarks/results/json-iterator+gzip.log`
```
goos: darwin
goarch: amd64
pkg: github.com/json-iterator/go
compression: gzip
#187: json: cannot unmarshal number into Go struct field Message.userId of type string
errors: 2/10000
avg size: 1089.84 KB
min size: 1056.57 KB
max size: 1114.99 KB
```

## File: `benchmarks/results/json-iterator+gzip.txt`
```
BenchmarkEncoding/count=20		200000		76778 ns/op		14.54 MB/s		13357 B/op		388 allocs/op		1.09 KB/msg
```

## File: `benchmarks/results/json-iterator+snappy.log`
```
goos: darwin
goarch: amd64
pkg: github.com/json-iterator/go
compression: snappy
#187: json: cannot unmarshal number into Go struct field Message.userId of type string
errors: 2/10000
avg size: 1423.65 KB
min size: 1375.36 KB
max size: 1479.84 KB
```

## File: `benchmarks/results/json-iterator+snappy.txt`
```
BenchmarkEncoding/count=20		200000		44201 ns/op		32.98 MB/s		13321 B/op		388 allocs/op		1.42 KB/msg
```

## File: `benchmarks/results/json-iterator+zstd.log`
```
goos: darwin
goarch: amd64
pkg: github.com/json-iterator/go
compression: zstd
#187: json: cannot unmarshal number into Go struct field Message.userId of type string
errors: 2/10000
avg size: 988.18 KB
min size: 956.31 KB
max size: 1014.69 KB
```

## File: `benchmarks/results/json-iterator+zstd.txt`
```
BenchmarkEncoding/count=20		200000		47690 ns/op		21.22 MB/s		13344 B/op		388 allocs/op		0.99 KB/msg
```

## File: `benchmarks/results/json-iterator.log`
```
goos: darwin
goarch: amd64
pkg: github.com/json-iterator/go
#187: json: cannot unmarshal number into Go struct field Message.userId of type string
errors: 2/10000
avg size: 2027.15 KB
min size: 1960.16 KB
max size: 2076.95 KB
```

## File: `benchmarks/results/json-iterator.txt`
```
BenchmarkEncoding/count=20		200000		37497 ns/op		55.36 MB/s		13277 B/op		388 allocs/op		2.03 KB/msg
```

## File: `benchmarks/results/segment-encoding-json+gzip.log`
```
goos: darwin
goarch: amd64
pkg: github.com/segmentio/encoding/json
compression: gzip
#187: json: cannot unmarshal number into Go struct field Message.userId of type string
errors: 2/10000
avg size: 1089.58 KB
min size: 1056.63 KB
max size: 1114.71 KB
```

## File: `benchmarks/results/segment-encoding-json+gzip.txt`
```
BenchmarkEncoding/count=20		200000		66910 ns/op		16.67 MB/s		6105 B/op		165 allocs/op		1.09 KB/msg
```

## File: `benchmarks/results/segment-encoding-json+snappy.log`
```
goos: darwin
goarch: amd64
pkg: github.com/segmentio/encoding/json
compression: snappy
#187: json: cannot unmarshal number into Go struct field Message.userId of type string
errors: 2/10000
avg size: 1423.02 KB
min size: 1375.34 KB
max size: 1481.57 KB
```

## File: `benchmarks/results/segment-encoding-json+snappy.txt`
```
BenchmarkEncoding/count=20		200000		33337 ns/op		43.71 MB/s		6070 B/op		165 allocs/op		1.42 KB/msg
```

## File: `benchmarks/results/segment-encoding-json+zstd.log`
```
goos: darwin
goarch: amd64
pkg: github.com/segmentio/encoding/json
compression: zstd
#187: json: cannot unmarshal number into Go struct field Message.userId of type string
errors: 2/10000
avg size: 988.11 KB
min size: 956.38 KB
max size: 1014.44 KB
```

## File: `benchmarks/results/segment-encoding-json+zstd.txt`
```
BenchmarkEncoding/count=20		200000		37417 ns/op		27.04 MB/s		6094 B/op		165 allocs/op		0.99 KB/msg
```

## File: `benchmarks/results/segment-encoding-json.log`
```
goos: darwin
goarch: amd64
pkg: github.com/segmentio/encoding/json
#187: json: cannot unmarshal number into Go struct field Message.userId of type string
errors: 2/10000
avg size: 2026.17 KB
min size: 1959.18 KB
max size: 2075.97 KB
```

## File: `benchmarks/results/segment-protobuf-v1+gzip.log`
```
goos: darwin
goarch: amd64
pkg: github.com/segmentio/protobuf/v1
compression: gzip
#187: json: cannot unmarshal number into Go struct field Message.userId of type string
errors: 2/10000
avg size: 1130.42 KB
min size: 1093.34 KB
max size: 1170.82 KB
```

## File: `benchmarks/results/segment-protobuf-v1+gzip.txt`
```
BenchmarkEncoding/count=20		200000		69366 ns/op		16.69 MB/s		16287 B/op		256 allocs/op		1.13 KB/msg
```

## File: `benchmarks/results/segment-protobuf-v1+snappy.log`
```
goos: darwin
goarch: amd64
pkg: github.com/segmentio/protobuf/v1
compression: snappy
#187: json: cannot unmarshal number into Go struct field Message.userId of type string
errors: 2/10000
avg size: 1412.94 KB
min size: 1356.50 KB
max size: 1480.25 KB
```

## File: `benchmarks/results/segment-protobuf-v1+snappy.txt`
```
BenchmarkEncoding/count=20		200000		34140 ns/op		42.38 MB/s		16067 B/op		255 allocs/op		1.41 KB/msg
```

## File: `benchmarks/results/segment-protobuf-v1+zstd.log`
```
goos: darwin
goarch: amd64
pkg: github.com/segmentio/protobuf/v1
compression: zstd
#187: json: cannot unmarshal number into Go struct field Message.userId of type string
errors: 2/10000
avg size: 1055.01 KB
min size: 1019.95 KB
max size: 1086.27 KB
```

## File: `benchmarks/results/segment-protobuf-v1+zstd.txt`
```
BenchmarkEncoding/count=20		200000		39298 ns/op		27.49 MB/s		16061 B/op		255 allocs/op		1.06 KB/msg
```

## File: `benchmarks/results/segment-protobuf-v1.log`
```
goos: darwin
goarch: amd64
pkg: github.com/segmentio/protobuf/v1
#187: json: cannot unmarshal number into Go struct field Message.userId of type string
errors: 2/10000
avg size: 1866.52 KB
min size: 1798.21 KB
max size: 1917.75 KB
```

## File: `benchmarks/results/segment-protobuf-v1.txt`
```
BenchmarkEncoding/count=20		200000		30998 ns/op		61.66 MB/s		16003 B/op		255 allocs/op		1.87 KB/msg
```

## File: `benchmarks/results/tinylib-msgp+gzip.log`
```
goos: darwin
goarch: amd64
pkg: github.com/tinylib/msgp
compression: gzip
#187: json: cannot unmarshal number into Go struct field Message.userId of type string
errors: 2/10000
avg size: 1052.68 KB
min size: 1018.90 KB
max size: 1078.90 KB
```

## File: `benchmarks/results/tinylib-msgp+gzip.txt`
```
BenchmarkEncoding/count=20		200000		53809 ns/op		20.03 MB/s		5592 B/op		164 allocs/op		1.05 KB/msg
```

## File: `benchmarks/results/tinylib-msgp+snappy.log`
```
goos: darwin
goarch: amd64
pkg: github.com/tinylib/msgp
compression: snappy
#187: json: cannot unmarshal number into Go struct field Message.userId of type string
errors: 2/10000
avg size: 1337.42 KB
min size: 1283.11 KB
max size: 1391.90 KB
```

## File: `benchmarks/results/tinylib-msgp+snappy.txt`
```
BenchmarkEncoding/count=20		200000		20895 ns/op		65.54 MB/s		5398 B/op		163 allocs/op		1.34 KB/msg
```

## File: `benchmarks/results/tinylib-msgp+zstd.log`
```
goos: darwin
goarch: amd64
pkg: github.com/tinylib/msgp
compression: zstd
#187: json: cannot unmarshal number into Go struct field Message.userId of type string
errors: 2/10000
avg size: 1001.53 KB
min size: 968.40 KB
max size: 1029.62 KB
```

## File: `benchmarks/results/tinylib-msgp+zstd.txt`
```
BenchmarkEncoding/count=20		200000		27037 ns/op		37.93 MB/s		5403 B/op		163 allocs/op		1.00 KB/msg
```

## File: `benchmarks/results/tinylib-msgp.log`
```
goos: darwin
goarch: amd64
pkg: github.com/tinylib/msgp
#187: json: cannot unmarshal number into Go struct field Message.userId of type string
errors: 2/10000
avg size: 1807.43 KB
min size: 1747.94 KB
max size: 1852.62 KB
```

## File: `benchmarks/results/tinylib-msgp.txt`
```
BenchmarkEncoding/count=20		200000		16889 ns/op		109.59 MB/s		5356 B/op		163 allocs/op		1.81 KB/msg
```

## File: `benchmarks/results/vmihailenco-msgpack+gzip.log`
```
goos: darwin
goarch: amd64
pkg: github.com/vmihailenco/msgpack
compression: gzip
#187: json: cannot unmarshal number into Go struct field Message.userId of type string
errors: 2/10000
avg size: 1042.87 KB
min size: 1008.43 KB
max size: 1077.14 KB
```

## File: `benchmarks/results/vmihailenco-msgpack+gzip.txt`
```
BenchmarkEncoding/count=20		200000		61153 ns/op		17.46 MB/s		6720 B/op		197 allocs/op		1.04 KB/msg
```

## File: `benchmarks/results/vmihailenco-msgpack+snappy.log`
```
goos: darwin
goarch: amd64
pkg: github.com/vmihailenco/msgpack
compression: snappy
#187: json: cannot unmarshal number into Go struct field Message.userId of type string
errors: 2/10000
avg size: 1324.88 KB
min size: 1266.77 KB
max size: 1384.42 KB
```

## File: `benchmarks/results/vmihailenco-msgpack+snappy.txt`
```
BenchmarkEncoding/count=20		200000		28369 ns/op		47.82 MB/s		6541 B/op		196 allocs/op		1.32 KB/msg
```

## File: `benchmarks/results/vmihailenco-msgpack+zstd.log`
```
goos: darwin
goarch: amd64
pkg: github.com/vmihailenco/msgpack
compression: zstd
#187: json: cannot unmarshal number into Go struct field Message.userId of type string
errors: 2/10000
avg size: 995.18 KB
min size: 961.61 KB
max size: 1023.46 KB
```

## File: `benchmarks/results/vmihailenco-msgpack+zstd.txt`
```
BenchmarkEncoding/count=20		200000		33937 ns/op		30.03 MB/s		6547 B/op		196 allocs/op		1.00 KB/msg
```

## File: `benchmarks/results/vmihailenco-msgpack.log`
```
goos: darwin
goarch: amd64
pkg: github.com/vmihailenco/msgpack
#187: json: cannot unmarshal number into Go struct field Message.userId of type string
errors: 2/10000
avg size: 1717.19 KB
min size: 1657.45 KB
max size: 1762.65 KB
```

## File: `benchmarks/results/vmihailenco-msgpack.txt`
```
BenchmarkEncoding/count=20		200000		24901 ns/op		70.61 MB/s		6503 B/op		196 allocs/op		1.72 KB/msg
```

## File: `internal/runtime_reflect/map.go`
```go
// Package runtime_reflect exposes internal APIs of the Go runtime.
//
// This package is internal so it doesn't become part of the exported APIs that
// users of this package can take dependencies on. There is a risk that these
// APIs will be implicitly changed by Go, in which case packages that depend on
// it will break. We use these APIs to have access to optimziations that aren't
// possible today via the reflect package. Ideally, the reflect package evolves
// to expose APIs that are efficient enough that we can drop the need for this
// package, but until then we will be maintaining bridges to these Go runtime
// functions and types.
package runtime_reflect

import "unsafe"

func Assign(typ, dst, src unsafe.Pointer) {
	typedmemmove(typ, dst, src)
}

func MapAssign(t, m, k unsafe.Pointer) unsafe.Pointer {
	return mapassign(t, m, k)
}

func MakeMap(t unsafe.Pointer, cap int) unsafe.Pointer {
	return makemap(t, cap)
}

type MapIter struct{ hiter }

func (it *MapIter) Init(t unsafe.Pointer, m unsafe.Pointer) {
	mapiterinit(t, m, &it.hiter)
}

func (it *MapIter) Done() {
	if it.h != nil {
		it.key = nil
		mapiternext(&it.hiter)
	}
}

func (it *MapIter) Next() {
	mapiternext(&it.hiter)
}

func (it *MapIter) HasNext() bool {
	return it.key != nil
}

func (it *MapIter) Key() unsafe.Pointer { return it.key }

func (it *MapIter) Value() unsafe.Pointer { return it.value }

// copied from src/runtime/map.go, all pointer types replaced with
// unsafe.Pointer.
//
// Alternatively we could get away with a heap allocation and only
// defining key and val if we were using reflect.mapiterinit instead,
// which returns a heap-allocated *hiter.
type hiter struct {
	key         unsafe.Pointer // nil when iteration is done
	value       unsafe.Pointer
	t           unsafe.Pointer
	h           unsafe.Pointer
	buckets     unsafe.Pointer // bucket ptr at hash_iter initialization time
	bptr        unsafe.Pointer // current bucket
	overflow    unsafe.Pointer // keeps overflow buckets of hmap.buckets alive
	oldoverflow unsafe.Pointer // keeps overflow buckets of hmap.oldbuckets alive
	startBucket uintptr        // bucket iteration started at
	offset      uint8          // intra-bucket offset to start from during iteration (should be big enough to hold bucketCnt-1)
	wrapped     bool           // already wrapped around from end of bucket array to beginning
	B           uint8
	i           uint8
	bucket      uintptr
	checkBucket uintptr
}

//go:noescape
//go:linkname makemap reflect.makemap
func makemap(t unsafe.Pointer, cap int) unsafe.Pointer

// m escapes into the return value, but the caller of mapiterinit
// doesn't let the return value escape.
//
//go:noescape
//go:linkname mapiterinit runtime.mapiterinit
func mapiterinit(t unsafe.Pointer, m unsafe.Pointer, it *hiter)

//go:noescape
//go:linkname mapiternext runtime.mapiternext
func mapiternext(it *hiter)

//go:noescape
//go:linkname mapassign runtime.mapassign
func mapassign(t, m, k unsafe.Pointer) unsafe.Pointer

//go:nosplit
//go:noescape
//go:linkname typedmemmove runtime.typedmemmove
func typedmemmove(typ, dst, src unsafe.Pointer)
```

## File: `internal/runtime_reflect/slice.go`
```go
package runtime_reflect

import "unsafe"

type Slice struct {
	data unsafe.Pointer
	len  int
	cap  int
}

func (s *Slice) Cap() int {
	return s.cap
}

func (s *Slice) Len() int {
	return s.len
}

func (s *Slice) SetLen(n int) {
	s.len = n
}

func (s *Slice) Index(i int, elemSize uintptr) unsafe.Pointer {
	return unsafe.Pointer(uintptr(s.data) + (uintptr(i) * elemSize))
}

func MakeSlice(elemType unsafe.Pointer, len, cap int) Slice {
	return Slice{
		data: newarray(elemType, cap),
		len:  len,
		cap:  cap,
	}
}

func CopySlice(elemType unsafe.Pointer, dst, src Slice) int {
	return typedslicecopy(elemType, dst, src)
}

//go:linkname newarray runtime.newarray
func newarray(t unsafe.Pointer, n int) unsafe.Pointer

//go:linkname typedslicecopy runtime.typedslicecopy
//go:noescape
func typedslicecopy(t unsafe.Pointer, dst, src Slice) int
```

## File: `iso8601/parse.go`
```go
package iso8601

import (
	"encoding/binary"
	"errors"
	"time"
	"unsafe"
)

var (
	errInvalidTimestamp = errors.New("invalid ISO8601 timestamp")
	errMonthOutOfRange  = errors.New("month out of range")
	errDayOutOfRange    = errors.New("day out of range")
	errHourOutOfRange   = errors.New("hour out of range")
	errMinuteOutOfRange = errors.New("minute out of range")
	errSecondOutOfRange = errors.New("second out of range")
)

// Parse parses an ISO8601 timestamp, e.g. "2021-03-25T21:36:12Z".
func Parse(input string) (time.Time, error) {
	b := unsafeStringToBytes(input)
	if len(b) >= 20 && len(b) <= 30 && b[len(b)-1] == 'Z' {
		if len(b) == 21 || (len(b) > 21 && b[19] != '.') {
			return time.Time{}, errInvalidTimestamp
		}

		t1 := binary.LittleEndian.Uint64(b)
		t2 := binary.LittleEndian.Uint64(b[8:16])
		t3 := uint64(b[16]) | uint64(b[17])<<8 | uint64(b[18])<<16 | uint64('Z')<<24

		// Check for valid separators by masking input with "    -  -  T  :  :  Z".
		// If separators are all valid, replace them with a '0' (0x30) byte and
		// check all bytes are now numeric.
		if !match(t1, mask1) || !match(t2, mask2) || !match(t3, mask3) {
			return time.Time{}, errInvalidTimestamp
		}
		t1 ^= replace1
		t2 ^= replace2
		t3 ^= replace3
		if (nonNumeric(t1) | nonNumeric(t2) | nonNumeric(t3)) != 0 {
			return time.Time{}, errInvalidTimestamp
		}

		t1 -= zero
		t2 -= zero
		t3 -= zero
		year := (t1&0xF)*1000 + (t1>>8&0xF)*100 + (t1>>16&0xF)*10 + (t1 >> 24 & 0xF)
		month := (t1>>40&0xF)*10 + (t1 >> 48 & 0xF)
		day := (t2&0xF)*10 + (t2 >> 8 & 0xF)
		hour := (t2>>24&0xF)*10 + (t2 >> 32 & 0xF)
		minute := (t2>>48&0xF)*10 + (t2 >> 56)
		second := (t3>>8&0xF)*10 + (t3 >> 16)

		nanos := int64(0)
		if len(b) > 20 {
			for _, c := range b[20 : len(b)-1] {
				if c < '0' || c > '9' {
					return time.Time{}, errInvalidTimestamp
				}
				nanos = (nanos * 10) + int64(c-'0')
			}
			nanos *= pow10[30-len(b)]
		}

		if err := validate(year, month, day, hour, minute, second); err != nil {
			return time.Time{}, err
		}

		unixSeconds := int64(daysSinceEpoch(year, month, day))*86400 + int64(hour*3600+minute*60+second)
		return time.Unix(unixSeconds, nanos).UTC(), nil
	}

	// Fallback to using time.Parse().
	t, err := time.Parse(time.RFC3339Nano, input)
	if err != nil {
		// Override (and don't wrap) the error here. The error returned by
		// time.Parse() is dynamic, and includes a reference to the input
		// string. By overriding the error, we guarantee that the input string
		// doesn't escape.
		return time.Time{}, errInvalidTimestamp
	}
	return t, nil
}

var pow10 = []int64{1, 10, 100, 1000, 1e4, 1e5, 1e6, 1e7, 1e8}

const (
	mask1 = 0x2d00002d00000000 // YYYY-MM-
	mask2 = 0x00003a0000540000 // DDTHH:MM
	mask3 = 0x000000005a00003a // :SSZ____

	// Generate masks that replace the separators with a numeric byte.
	// The input must have valid separators. XOR with the separator bytes
	// to zero them out and then XOR with 0x30 to replace them with '0'.
	replace1 = mask1 ^ 0x3000003000000000
	replace2 = mask2 ^ 0x0000300000300000
	replace3 = mask3 ^ 0x3030303030000030

	lsb = ^uint64(0) / 255
	msb = lsb * 0x80

	zero = lsb * '0'
	nine = lsb * '9'
)

func validate(year, month, day, hour, minute, second uint64) error {
	if day == 0 || day > 31 {
		return errDayOutOfRange
	}
	if month == 0 || month > 12 {
		return errMonthOutOfRange
	}
	if hour >= 24 {
		return errHourOutOfRange
	}
	if minute >= 60 {
		return errMinuteOutOfRange
	}
	if second >= 60 {
		return errSecondOutOfRange
	}
	if month == 2 && (day > 29 || (day == 29 && !isLeapYear(year))) {
		return errDayOutOfRange
	}
	if day == 31 {
		switch month {
		case 4, 6, 9, 11:
			return errDayOutOfRange
		}
	}
	return nil
}

func match(u, mask uint64) bool {
	return (u & mask) == mask
}

func nonNumeric(u uint64) uint64 {
	// Derived from https://graphics.stanford.edu/~seander/bithacks.html#HasLessInWord.
	// Subtract '0' (0x30) from each byte so that the MSB is set in each byte
	// if there's a byte less than '0' (0x30). Add 0x46 (0x7F-'9') so that the
	// MSB is set if there's a byte greater than '9' (0x39). To handle overflow
	// when adding 0x46, include the MSB from the input bytes in the final mask.
	// Remove all but the MSBs and then you're left with a mask where each
	// non-numeric byte from the input has its MSB set in the output.
	return ((u - zero) | (u + (^msb - nine)) | u) & msb
}

func daysSinceEpoch(year, month, day uint64) uint64 {
	// Derived from https://blog.reverberate.org/2020/05/12/optimizing-date-algorithms.html.
	monthAdjusted := month - 3
	var carry uint64
	if monthAdjusted > month {
		carry = 1
	}
	var adjust uint64
	if carry == 1 {
		adjust = 12
	}
	yearAdjusted := year + 4800 - carry
	monthDays := ((monthAdjusted+adjust)*62719 + 769) / 2048
	leapDays := yearAdjusted/4 - yearAdjusted/100 + yearAdjusted/400
	return yearAdjusted*365 + leapDays + monthDays + (day - 1) - 2472632
}

func isLeapYear(y uint64) bool {
	return (y%4) == 0 && ((y%100) != 0 || (y%400) == 0)
}

func unsafeStringToBytes(s string) []byte {
	return *(*[]byte)(unsafe.Pointer(&sliceHeader{
		Data: *(*unsafe.Pointer)(unsafe.Pointer(&s)),
		Len:  len(s),
		Cap:  len(s),
	}))
}

// sliceHeader is like reflect.SliceHeader but the Data field is a
// unsafe.Pointer instead of being a uintptr to avoid invalid
// conversions from uintptr to unsafe.Pointer.
type sliceHeader struct {
	Data unsafe.Pointer
	Len  int
	Cap  int
}
```

## File: `iso8601/parse_test.go`
```go
package iso8601

import (
	"fmt"
	"testing"
	"time"
)

func TestParse(t *testing.T) {
	for _, input := range []string{
		// Fast path (20 bytes)
		"1987-12-16T23:45:12Z",
		"2006-01-02T15:04:05Z",
		"2000-02-29T23:59:59Z", // leap year
		"2020-02-29T23:59:59Z", // leap year
		"0000-01-01T00:00:00Z",
		"9999-12-31T23:59:59Z",

		// Fast path (24 bytes)
		"1987-12-16T23:45:12.123Z",
		"2006-01-02T15:04:05.123Z",
		"2000-02-29T23:59:59.123Z",
		"2020-02-29T23:59:59.123Z",
		"0000-01-01T00:00:00.000Z",
		"9999-12-31T23:59:59.999Z",

		// Fast path (30 bytes)
		"1987-12-16T23:45:12.123456789Z",
		"2006-01-02T15:04:05.123456789Z",
		"2000-02-29T23:59:59.123456789Z",
		"2020-02-29T23:59:59.123456789Z",
		"0000-01-01T00:00:00.000000000Z",
		"9999-12-31T23:59:59.999999999Z",

		// Slow path
		"2006-01-02T15:04:05.1Z",
		"2006-01-02T15:04:05.12Z",
		"2006-01-02T15:04:05.1234Z",
		"2006-01-02T15:04:05.12345Z",
		"2006-01-02T15:04:05.123456Z",
		"2006-01-02T15:04:05.1234567Z",
		"2006-01-02T15:04:05.12345678Z",
		"2021-10-16T07:55:07+10:00",
		"2021-10-16T07:55:07.1+10:00",
		"2021-10-16T07:55:07.12+10:00",
		"2021-10-16T07:55:07.123+10:00",
		"2021-10-16T07:55:07.1234+10:00",
		"2021-10-16T07:55:07.12345+10:00",
		"2021-10-16T07:55:07.123456+10:00",
		"2021-10-16T07:55:07.1234567+10:00",
		"2021-10-16T07:55:07.12345678+10:00",
		"2021-10-16T07:55:07.123456789+10:00",
		"2021-10-16T07:55:07-10:00",
		"2021-10-16T07:55:07.1-10:00",
		"2021-10-16T07:55:07.12-10:00",
		"2021-10-16T07:55:07.123-10:00",
		"2021-10-16T07:55:07.1234-10:00",
		"2021-10-16T07:55:07.12345-10:00",
		"2021-10-16T07:55:07.123456-10:00",
		"2021-10-16T07:55:07.1234567-10:00",
		"2021-10-16T07:55:07.12345678-10:00",
		"2021-10-16T07:55:07.123456789-10:00",
	} {
		t.Run(input, func(t *testing.T) {
			expect, err := time.Parse(time.RFC3339Nano, input)
			if err != nil {
				t.Fatal(err)
			}
			actual, err := Parse(input)
			if err != nil {
				t.Error(err)
			} else if !actual.Equal(expect) {
				t.Errorf("unexpected time: %v vs expected %v", actual, expect)
			} else if actual.Location().String() != expect.Location().String() {
				t.Errorf("unexpected timezone: %v vs expected %v", actual.Location().String(), expect.Location().String())
			}
		})
	}

	// Check ~4M YYYY-MM-DD dates in 20 byte form.
	for year := range 10000 {
		for month := range 14 {
			for day := range 33 {
				input := fmt.Sprintf("%04d-%02d-%02dT12:34:56Z", year, month, day)
				expect, expectErr := time.Parse(time.RFC3339Nano, input)
				actual, actualErr := Parse(input)
				if (expectErr != nil) != (actualErr != nil) {
					t.Errorf("unexpected error for %v: %v vs. %v expected", input, actualErr, expectErr)
				} else if !actual.Equal(expect) {
					t.Errorf("unexpected time for %v: %v vs. %v expected", input, actual, expect)
				}
			}
		}
	}

	// Check ~4M YYYY-MM-DD dates in 24 byte form.
	for year := range 10000 {
		for month := range 14 {
			for day := range 33 {
				input := fmt.Sprintf("%04d-%02d-%02dT12:34:56.789Z", year, month, day)
				expect, expectErr := time.Parse(time.RFC3339Nano, input)
				actual, actualErr := Parse(input)
				if (expectErr != nil) != (actualErr != nil) {
					t.Errorf("unexpected error for %v: %v vs. %v expected", input, actualErr, expectErr)
				} else if !actual.Equal(expect) {
					t.Errorf("unexpected time for %v: %v vs. %v expected", input, actual, expect)
				}
			}
		}
	}

	// Check ~4M YYYY-MM-DD dates in 30 byte form.
	for year := range 10000 {
		for month := range 14 {
			for day := range 33 {
				input := fmt.Sprintf("%04d-%02d-%02dT12:34:56.123456789Z", year, month, day)
				expect, expectErr := time.Parse(time.RFC3339Nano, input)
				actual, actualErr := Parse(input)
				if (expectErr != nil) != (actualErr != nil) {
					t.Errorf("unexpected error for %v: %v vs. %v expected", input, actualErr, expectErr)
				} else if !actual.Equal(expect) {
					t.Errorf("unexpected time for %v: %v vs. %v expected", input, actual, expect)
				}
			}
		}
	}

	// Check all ~1M HH:MM:SS times in 20 byte form.
	for hour := range 100 {
		for minute := range 100 {
			for second := range 100 {
				input := fmt.Sprintf("2000-01-01T%02d:%02d:%02dZ", hour, minute, second)
				expect, expectErr := time.Parse(time.RFC3339Nano, input)
				actual, actualErr := Parse(input)
				if (expectErr != nil) != (actualErr != nil) {
					t.Errorf("unexpected error for %v: %v vs. %v expected", input, actualErr, expectErr)
				} else if !actual.Equal(expect) {
					t.Errorf("unexpected time for %v: %v vs. %v expected", input, actual, expect)
				}
			}
		}
	}

	// Check ~1M HH:MM:SS.MMM times in 24 byte form.
	for hour := range 100 {
		for minute := range 100 {
			for second := range 100 {
				input := fmt.Sprintf("2000-01-01T%02d:%02d:%02d.123Z", hour, minute, second)
				expect, expectErr := time.Parse(time.RFC3339Nano, input)
				actual, actualErr := Parse(input)
				if (expectErr != nil) != (actualErr != nil) {
					t.Errorf("unexpected error for %v: %v vs. %v expected", input, actualErr, expectErr)
				} else if !actual.Equal(expect) {
					t.Errorf("unexpected time for %v: %v vs. %v expected", input, actual, expect)
				}
			}
		}
	}

	// Check ~1M HH:MM:SS.MMM times in 30 byte form.
	for hour := range 100 {
		for minute := range 100 {
			for second := range 100 {
				input := fmt.Sprintf("2000-01-01T%02d:%02d:%02d.123456789Z", hour, minute, second)
				expect, expectErr := time.Parse(time.RFC3339Nano, input)
				actual, actualErr := Parse(input)
				if (expectErr != nil) != (actualErr != nil) {
					t.Errorf("unexpected error for %v: %v vs. %v expected", input, actualErr, expectErr)
				} else if !actual.Equal(expect) {
					t.Errorf("unexpected time for %v: %v vs. %v expected", input, actual, expect)
				}
			}
		}
	}

	// Check milliseconds.
	for millis := 1; millis < 1000; millis <<= 1 {
		input := fmt.Sprintf("2000-01-01T00:00:00.%03dZ", millis)
		expect, expectErr := time.Parse(time.RFC3339Nano, input)
		actual, actualErr := Parse(input)
		if (expectErr != nil) != (actualErr != nil) {
			t.Errorf("unexpected error for %v: %v vs. %v expected", input, actualErr, expectErr)
		} else if !actual.Equal(expect) {
			t.Errorf("unexpected time for %v: %v vs. %v expected", input, actual, expect)
		}
	}

	// Check nanoseconds.
	for nanos := 1; nanos < 1e9; nanos <<= 1 {
		input := fmt.Sprintf("2000-01-01T00:00:00.%09dZ", nanos)
		expect, expectErr := time.Parse(time.RFC3339Nano, input)
		actual, actualErr := Parse(input)
		if (expectErr != nil) != (actualErr != nil) {
			t.Errorf("unexpected error for %v: %v vs. %v expected", input, actualErr, expectErr)
		} else if !actual.Equal(expect) {
			t.Errorf("unexpected time for %v: %v vs. %v expected", input, actual, expect)
		}
	}

	// Check with trailing zeroes omitted.
	for n := 1; n < 1e9; n <<= 1 {
		input := fmt.Sprintf("2000-01-01T00:00:00.%dZ", n)
		expect, expectErr := time.Parse(time.RFC3339Nano, input)
		actual, actualErr := Parse(input)
		if (expectErr != nil) != (actualErr != nil) {
			t.Errorf("unexpected error for %v: %v vs. %v expected", input, actualErr, expectErr)
		} else if !actual.Equal(expect) {
			t.Errorf("unexpected time for %v: %v vs. %v expected", input, actual, expect)
		}
	}
}

func TestParseInvalid(t *testing.T) {
	for _, input := range []string{
		// 20 bytes
		"XXXXXXXXXXXXXXXXXXXX",
		"00000000000000000000",
		"1900-02-29T00:00:00Z", // 28 days in month (not a leap year)
		"2021-02-29T00:00:00Z", // 28 days in month (not a leap year)
		"2021-02-30T00:00:00Z", // 28 days in month
		"2021-02-31T00:00:00Z", // 28 days in month
		"2021-04-31T00:00:00Z", // 30 days in month
		"2021-06-31T00:00:00Z", // 30 days in month
		"2021-09-31T00:00:00Z", // 30 days in month
		"2021-11-31T00:00:00Z", // 30 days in month
		"XXXX-13-01T00:00:00Z", // invalid year
		"2000-13-01T00:00:00Z", // invalid month (1)
		"2000-00-01T00:00:00Z", // invalid month (2)
		"2000-XX-01T00:00:00Z", // invalid month (3)
		"2000-12-32T00:00:00Z", // invalid day (1)
		"2000-12-00T00:00:00Z", // invalid day (2)
		"2000-12-XXT00:00:00Z", // invalid day (3)
		"2000-12-31T24:00:00Z", // invalid hour (1)
		"2000-12-31TXX:00:00Z", // invalid hour (2)
		"2000-12-31T23:60:00Z", // invalid minute (1)
		"2000-12-31T23:XX:00Z", // invalid minute (2)
		"2000-12-31T23:59:60Z", // invalid second (1)
		"2000-12-31T23:59:XXZ", // invalid second (2)
		"1999-01-01 23:45:00Z", // missing T separator
		"1999 01-01T23:45:00Z", // missing date separator (1)
		"1999-01 01T23:45:00Z", // missing date separator (2)
		"1999-01-01T23 45:00Z", // missing time separator (1)
		"1999-01-01T23:45 00Z", // missing time separator (2)
		"1999-01-01T23:45:00 ", // missing timezone
		"1999-01-01t23:45:00Z", // lowercase T
		"1999-01-01T23:45:00z", // lowercase Z
		"X999-01-01T23:45:00Z", // X in various positions
		"1X99-01-01T23:45:00Z",
		"19X9-01-01T23:45:00Z",
		"199X-01-01T23:45:00Z",
		"1999X01-01T23:45:00Z",
		"1999-X1-01T23:45:00Z",
		"1999-0X-01T23:45:00Z",
		"1999-01X01T23:45:00Z",
		"1999-01-X1T23:45:00Z",
		"1999-01-0XT23:45:00Z",
		"1999-01-01X23:45:00Z",
		"1999-01-01TX3:45:00Z",
		"1999-01-01T2X:45:00Z",
		"1999-01-01T23X45:00Z",
		"1999-01-01T23:X5:00Z",
		"1999-01-01T23:4X:00Z",
		"1999-01-01T23:45X00Z",
		"1999-01-01T23:45:X0Z",
		"1999-01-01T23:45:0XZ",
		"1999-01-01T23:45:00X",

		// 24 bytes
		"XXXXXXXXXXXXXXXXXXXXXXXX",
		"000000000000000000000000",
		"1900-02-29T00:00:00.123Z", // 28 days in month (not a leap year)
		"2021-02-29T00:00:00.123Z", // 28 days in month (not a leap year)
		"2021-02-30T00:00:00.123Z", // 28 days in month
		"2021-02-31T00:00:00.123Z", // 28 days in month
		"2021-04-31T00:00:00.123Z", // 30 days in month
		"2021-06-31T00:00:00.123Z", // 30 days in month
		"2021-09-31T00:00:00.123Z", // 30 days in month
		"2021-11-31T00:00:00.123Z", // 30 days in month
		"XXXX-13-01T00:00:00.123Z", // invalid year
		"2000-13-01T00:00:00.123Z", // invalid month (1)
		"2000-00-01T00:00:00.123Z", // invalid month (2)
		"2000-XX-01T00:00:00.123Z", // invalid month (3)
		"2000-12-32T00:00:00.123Z", // invalid day (1)
		"2000-12-00T00:00:00.123Z", // invalid day (2)
		"2000-12-XXT00:00:00.123Z", // invalid day (3)
		"2000-12-31T24:00:00.123Z", // invalid hour (1)
		"2000-12-31TXX:00:00.123Z", // invalid hour (2)
		"2000-12-31T23:60:00.123Z", // invalid minute (1)
		"2000-12-31T23:XX:00.123Z", // invalid minute (2)
		"2000-12-31T23:59:60.123Z", // invalid second (1)
		"2000-12-31T23:59:XX.123Z", // invalid second (2)
		"2000-12-31T23:59:59.XXXZ", // invalid millis
		"1999-01-01 23:45:00.123Z", // missing T separator
		"1999 01-01T23:45:00.123Z", // missing date separator (1)
		"1999-01 01T23:45:00.123Z", // missing date separator (2)
		"1999-01-01T23 45:00.123Z", // missing time separator (1)
		"1999-01-01T23:45 00.123Z", // missing time separator (2)
		"1999-01-01T23:45:00 123Z", // missing time separator (3)
		"1999-01-01T23:45:00.123 ", // missing timezone
		"1999-01-01t23:45:00.123Z", // lowercase T
		"1999-01-01T23:45:00.123z", // lowercase Z
		"X999-01-01T23:45:00.123Z", // X in various positions
		"1X99-01-01T23:45:00.123Z",
		"19X9-01-01T23:45:00.123Z",
		"199X-01-01T23:45:00.123Z",
		"1999X01-01T23:45:00.123Z",
		"1999-X1-01T23:45:00.123Z",
		"1999-0X-01T23:45:00.123Z",
		"1999-01X01T23:45:00.123Z",
		"1999-01-X1T23:45:00.123Z",
		"1999-01-0XT23:45:00.123Z",
		"1999-01-01X23:45:00.123Z",
		"1999-01-01TX3:45:00.123Z",
		"1999-01-01T2X:45:00.123Z",
		"1999-01-01T23X45:00.123Z",
		"1999-01-01T23:X5:00.123Z",
		"1999-01-01T23:4X:00.123Z",
		"1999-01-01T23:45X00.123Z",
		"1999-01-01T23:45:X0.123Z",
		"1999-01-01T23:45:0X.123Z",
		"1999-01-01T23:45:00X123Z",
		"1999-01-01T23:45:00.X23Z",
		"1999-01-01T23:45:00.1X3Z",
		"1999-01-01T23:45:00.12XZ",
		"1999-01-01T23:45:00.123X",

		// 30 bytes
		"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
		"000000000000000000000000000000",
		"1900-02-29T00:00:00.123456789Z", // 28 days in month (not a leap year)
		"2021-02-29T00:00:00.123456789Z", // 28 days in month (not a leap year)
		"2021-02-30T00:00:00.123456789Z", // 28 days in month
		"2021-02-31T00:00:00.123456789Z", // 28 days in month
		"2021-04-31T00:00:00.123456789Z", // 30 days in month
		"2021-06-31T00:00:00.123456789Z", // 30 days in month
		"2021-09-31T00:00:00.123456789Z", // 30 days in month
		"2021-11-31T00:00:00.123456789Z", // 30 days in month
		"XXXX-13-01T00:00:00.123456789Z", // invalid year
		"2000-13-01T00:00:00.123456789Z", // invalid month (1)
		"2000-00-01T00:00:00.123456789Z", // invalid month (2)
		"2000-XX-01T00:00:00.123456789Z", // invalid month (3)
		"2000-12-32T00:00:00.123456789Z", // invalid day (1)
		"2000-12-00T00:00:00.123456789Z", // invalid day (2)
		"2000-12-XXT00:00:00.123456789Z", // invalid day (3)
		"2000-12-31T24:00:00.123456789Z", // invalid hour (1)
		"2000-12-31TXX:00:00.123456789Z", // invalid hour (2)
		"2000-12-31T23:60:00.123456789Z", // invalid minute (1)
		"2000-12-31T23:XX:00.123456789Z", // invalid minute (2)
		"2000-12-31T23:59:60.123456789Z", // invalid second (1)
		"2000-12-31T23:59:XX.123456789Z", // invalid second (2)
		"2000-12-31T23:59:59.XXXXXXXXXZ", // invalid nanos
		"1999-01-01 23:45:00.123456789Z", // missing T separator
		"1999 01-01T23:45:00.123456789Z", // missing date separator (1)
		"1999-01 01T23:45:00.123456789Z", // missing date separator (2)
		"1999-01-01T23 45:00.123456789Z", // missing time separator (1)
		"1999-01-01T23:45 00.123456789Z", // missing time separator (2)
		"1999-01-01T23:45:00 123456789Z", // missing time separator (3)
		"1999-01-01T23:45:00.123456789 ", // missing timezone
		"1999-01-01t23:45:00.123456789Z", // lowercase T
		"1999-01-01T23:45:00.123456789z", // lowercase Z
		"X999-01-01T23:45:00.123456789Z", // X in various positions
		"1X99-01-01T23:45:00.123456789Z",
		"19X9-01-01T23:45:00.123456789Z",
		"199X-01-01T23:45:00.123456789Z",
		"1999X01-01T23:45:00.123456789Z",
		"1999-X1-01T23:45:00.123456789Z",
		"1999-0X-01T23:45:00.123456789Z",
		"1999-01X01T23:45:00.123456789Z",
		"1999-01-X1T23:45:00.123456789Z",
		"1999-01-0XT23:45:00.123456789Z",
		"1999-01-01X23:45:00.123456789Z",
		"1999-01-01TX3:45:00.123456789Z",
		"1999-01-01T2X:45:00.123456789Z",
		"1999-01-01T23X45:00.123456789Z",
		"1999-01-01T23:X5:00.123456789Z",
		"1999-01-01T23:4X:00.123456789Z",
		"1999-01-01T23:45X00.123456789Z",
		"1999-01-01T23:45:X0.123456789Z",
		"1999-01-01T23:45:0X.123456789Z",
		"1999-01-01T23:45:00X123456789Z",
		"1999-01-01T23:45:00.X23456789Z",
		"1999-01-01T23:45:00.1X3456789Z",
		"1999-01-01T23:45:00.12X456789Z",
		"1999-01-01T23:45:00.123X56789Z",
		"1999-01-01T23:45:00.1234X6789Z",
		"1999-01-01T23:45:00.12345X789Z",
		"1999-01-01T23:45:00.123456X89Z",
		"1999-01-01T23:45:00.1234567X9Z",
		"1999-01-01T23:45:00.12345678XZ",
		"1999-01-01T23:45:00.123456789X",

		"2000-01-01T00:00:00.Z", // missing number after decimal point
	} {
		t.Run(input, func(t *testing.T) {
			ts, err := time.Parse(time.RFC3339Nano, input)
			if err == nil {
				t.Fatalf("expected time.Parse('%s') error, got %v", input, ts)
			}
			ts, actualErr := Parse(input)
			if (err != nil) != (actualErr != nil) {
				t.Fatalf("expected Parse('%s') error %v, got %v", input, err, actualErr)
			}
		})
	}
}

func BenchmarkParse(b *testing.B) {
	for range b.N {
		Parse("2006-01-02T15:04:05Z")
	}
}

func BenchmarkParseMilliseconds(b *testing.B) {
	for range b.N {
		Parse("2006-01-02T15:04:05.123Z")
	}
}

func BenchmarkParseMicroseconds(b *testing.B) {
	for range b.N {
		Parse("2006-01-02T15:04:05.123456Z")
	}
}

func BenchmarkParseNanoseconds(b *testing.B) {
	for range b.N {
		Parse("2006-01-02T15:04:05.123456789Z")
	}
}

func BenchmarkParseInvalid(b *testing.B) {
	for range b.N {
		Parse("2006-01-02T15:04:05.XZ")
	}
}
```

## File: `iso8601/valid.go`
```go
package iso8601

// ValidFlags is a bitset type used to configure the behavior of the Valid
// function.
type ValidFlags int

const (
	// Strict is a validation flag used to represent a string iso8601 validation
	// (this is the default).
	Strict ValidFlags = 0

	// AllowSpaceSeparator allows the presence of a space instead of a 'T' as
	// separator between the date and time.
	AllowSpaceSeparator ValidFlags = 1 << iota

	// AllowMissingTime allows the value to contain only a date.
	AllowMissingTime

	// AllowMissingSubsecond allows the value to contain only a date and time.
	AllowMissingSubsecond

	// AllowMissingTimezone allows the value to be missing the timezone
	// information.
	AllowMissingTimezone

	// AllowNumericTimezone allows the value to represent timezones in their
	// numeric form.
	AllowNumericTimezone

	// Flexible is a combination of all validation flag that allow for
	// non-strict checking of the input value.
	Flexible = AllowSpaceSeparator | AllowMissingTime | AllowMissingSubsecond | AllowMissingTimezone | AllowNumericTimezone
)

// Valid check value to verify whether or not it is a valid iso8601 time
// representation.
func Valid(value string, flags ValidFlags) bool {
	var ok bool

	// year
	if value, ok = readDigits(value, 4, 4); !ok {
		return false
	}

	if value, ok = readByte(value, '-'); !ok {
		return false
	}

	// month
	if value, ok = readDigits(value, 2, 2); !ok {
		return false
	}

	if value, ok = readByte(value, '-'); !ok {
		return false
	}

	// day
	if value, ok = readDigits(value, 2, 2); !ok {
		return false
	}

	if len(value) == 0 && (flags&AllowMissingTime) != 0 {
		return true // date only
	}

	// separator
	if value, ok = readByte(value, 'T'); !ok {
		if (flags & AllowSpaceSeparator) == 0 {
			return false
		}
		if value, ok = readByte(value, ' '); !ok {
			return false
		}
	}

	// hour
	if value, ok = readDigits(value, 2, 2); !ok {
		return false
	}

	if value, ok = readByte(value, ':'); !ok {
		return false
	}

	// minute
	if value, ok = readDigits(value, 2, 2); !ok {
		return false
	}

	if value, ok = readByte(value, ':'); !ok {
		return false
	}

	// second
	if value, ok = readDigits(value, 2, 2); !ok {
		return false
	}

	// microsecond
	if value, ok = readByte(value, '.'); !ok {
		if (flags & AllowMissingSubsecond) == 0 {
			return false
		}
	} else {
		if value, ok = readDigits(value, 1, 9); !ok {
			return false
		}
	}

	if len(value) == 0 && (flags&AllowMissingTimezone) != 0 {
		return true // date and time
	}

	// timezone
	if value, ok = readByte(value, 'Z'); ok {
		return len(value) == 0
	}

	if (flags & AllowSpaceSeparator) != 0 {
		value, _ = readByte(value, ' ')
	}

	if value, ok = readByte(value, '+'); !ok {
		if value, ok = readByte(value, '-'); !ok {
			return false
		}
	}

	// timezone hour
	if value, ok = readDigits(value, 2, 2); !ok {
		return false
	}

	if value, ok = readByte(value, ':'); !ok {
		if (flags & AllowNumericTimezone) == 0 {
			return false
		}
	}

	// timezone minute
	if value, ok = readDigits(value, 2, 2); !ok {
		return false
	}

	return len(value) == 0
}

func readDigits(value string, min, max int) (string, bool) {
	if len(value) < min {
		return value, false
	}

	i := 0

	for i < max && i < len(value) && isDigit(value[i]) {
		i++
	}

	if i < max && i < min {
		return value, false
	}

	return value[i:], true
}

func readByte(value string, c byte) (string, bool) {
	if len(value) == 0 {
		return value, false
	}
	if value[0] != c {
		return value, false
	}
	return value[1:], true
}

func isDigit(c byte) bool {
	return '0' <= c && c <= '9'
}
```

## File: `iso8601/valid_test.go`
```go
package iso8601

import (
	"testing"
	"time"
)

func TestValidate(t *testing.T) {
	tests := []struct {
		value string
		flags ValidFlags
		valid bool
	}{
		// valid
		{"2018-01-01T23:42:59.123456789Z", Strict, true},
		{"2018-01-01T23:42:59.123456789+07:00", Strict, true},
		{"2018-01-01T23:42:59.123456789-07:00", Strict, true},
		{"2018-01-01T23:42:59.000+07:00", Strict, true},

		{"2018-01-01", Flexible, true},
		{"2018-01-01 23:42:59", Flexible, true},
		{"2018-01-01T23:42:59.123-0700", Flexible, true},

		// invalid
		{"", Flexible, false},                                 // empty string
		{"whatever", Flexible, false},                         // not a time
		{"2018-01-01", Strict, false},                         // missing time
		{"2018-01-01 23:42:59-0700", Strict, false},           // missing subsecond
		{"2018-01-01T23:42:59.123456789+0700", Strict, false}, // don't allow numeric time zone
		{"2018_01-01T23:42:59.123456789Z", Strict, false},     // invalid date separator (first)
		{"2018-01_01T23:42:59.123456789Z", Strict, false},     // invalid date separator (second)
		{"2018-01-01 23:42:59.123456789Z", Strict, false},     // invalid date-time separator
		{"2018-01-01T23-42:59.123456789Z", Strict, false},     // invalid time separator (first)
		{"2018-01-01T23:42-59.123456789Z", Strict, false},     // invalid time separator (second)
		{"2018-01-01T23:42:59,123456789Z", Strict, false},     // invalid decimal separator
		{"2018-01-01T23:42:59.123456789", Strict, false},      // missing timezone
		{"18-01-01T23:42:59.123456789Z", Strict, false},       // 2-digit year
		{"2018-1-01T23:42:59.123456789Z", Strict, false},      // 1-digit month
		{"2018-01-1T23:42:59.123456789Z", Strict, false},      // 1-digit day
		{"2018-01-01T3:42:59.123456789Z", Strict, false},      // 1-digit hour
		{"2018-01-01T23:2:59.123456789Z", Strict, false},      // 1-digit minute
		{"2018-01-01T23:42:9.123456789Z", Strict, false},      // 1-digit second
		{"2018-01-01T23:42:59.Z", Strict, false},              // not enough subsecond digits
		{"2018-01-01T23:42:59.1234567890Z", Strict, false},    // too many subsecond digits
		{"2018-01-01T23:42:59.123456789+7:00", Strict, false}, // 1-digit timezone hour
		{"2018-01-01T23:42:59.123456789+07:0", Strict, false}, // 1-digit timezone minute
		{"2018-01-01_23:42:59", Flexible, false},              // invalid date-time separator (not a space)
	}

	for _, test := range tests {
		if test.valid != Valid(test.value, test.flags) {
			t.Errorf("%q expected Valid to return %t", test.value, test.valid)
		} else if test.valid {
			if !isIsoString(test.value) {
				t.Errorf("behavior mismatch, isIsoString says %q must not be a valid date", test.value)
			}
		} else if test.flags != Strict {
			if isIsoString(test.value) {
				t.Errorf("behavior mismatch, isIsoString says %q must be a valid date", test.value)
			}
		}
	}
}

func BenchmarkValidate(b *testing.B) {
	b.Run("success", benchmarkValidateSuccess)
	b.Run("failure", benchmarkValidateFailure)
}

func benchmarkValidateSuccess(b *testing.B) {
	for range b.N {
		if !Valid("2018-01-01T23:42:59.123456789Z", Flexible) {
			b.Fatal("not valid")
		}
	}
}

func benchmarkValidateFailure(b *testing.B) {
	for range b.N {
		if Valid("2018-01-01T23:42:59 oops!", Flexible) {
			b.Fatal("valid but should not")
		}
	}
}

func BenchmarkTimeParse(b *testing.B) {
	b.Run("success", benchmarkTimeParseSuccess)
	b.Run("failure", benchmarkTimeParseFailure)
}

func benchmarkTimeParseSuccess(b *testing.B) {
	for range b.N {
		if _, err := time.Parse(time.RFC3339Nano, "2018-01-01T23:42:59.123456789Z"); err != nil {
			b.Fatal("not valid")
		}
	}
}

func benchmarkTimeParseFailure(b *testing.B) {
	for range b.N {
		if _, err := time.Parse(time.RFC3339Nano, "2018-01-01T23:42:59 oops!"); err == nil {
			b.Fatal("valid but should not")
		}
	}
}

// =============================================================================
// This code is extracted from a library we had that we are replacing with this
// package, we use it to verify that the behavior matches.
// =============================================================================
var validDates = [...]string{
	time.RFC3339Nano,
	time.RFC3339,
	"2006-01-02T15:04:05.999-0700",
	"2006-01-02 15:04:05",
	"2006-01-02",
}

func isIsoString(str string) bool {
	// Per RFC3339Nano Spec a date should never be more than 35 chars.
	if len(str) > 36 {
		return false
	}

	for _, format := range validDates {
		if _, err := time.Parse(format, str); err == nil {
			return true
		}
	}

	return false
}
```

## File: `json/README.md`
```markdown
# encoding/json [![GoDoc](https://godoc.org/github.com/segmentio/encoding/json?status.svg)](https://godoc.org/github.com/segmentio/encoding/json)

Go package offering a replacement implementation of the standard library's
[`encoding/json`](https://golang.org/pkg/encoding/json/) package, with much
better performance.

## Usage

The exported API of this package mirrors the standard library's
[`encoding/json`](https://golang.org/pkg/encoding/json/) package, the only
change needed to take advantage of the performance improvements is the import
path of the `json` package, from:
```go
import (
    "encoding/json"
)
```
to
```go
import (
    "github.com/segmentio/encoding/json"
)
```

One way to gain higher encoding throughput is to disable HTML escaping.
It allows the string encoding to use a much more efficient code path which
does not require parsing UTF-8 runes most of the time.

## Performance Improvements

The internal implementation uses a fair amount of unsafe operations (untyped
code, pointer arithmetic, etc...) to avoid using reflection as much as possible,
which is often the reason why serialization code has a large CPU and memory
footprint.

The package aims for zero unnecessary dynamic memory allocations and hot code
paths that are mostly free from calls into the reflect package.

## Compatibility with encoding/json

This package aims to be a drop-in replacement, therefore it is tested to behave
exactly like the standard library's package. However, there are still a few
missing features that have not been ported yet:

- Streaming decoder, currently the `Decoder` implementation offered by the
package does not support progressively reading values from a JSON array (unlike
the standard library). In our experience this is a very rare use-case, if you
need it you're better off sticking to the standard library, or spend a bit of
time implementing it in here ;)

Note that none of those features should result in performance degradations if
they were implemented in the package, and we welcome contributions!

## Trade-offs

As one would expect, we had to make a couple of trade-offs to achieve greater
performance than the standard library, but there were also features that we
did not want to give away.

Other open-source packages offering a reduced CPU and memory footprint usually
do so by designing a different API, or require code generation (therefore adding
complexity to the build process). These were not acceptable conditions for us,
as we were not willing to trade off developer productivity for better runtime
performance. To achieve this, we chose to exactly replicate the standard
library interfaces and behavior, which meant the package implementation was the
only area that we were able to work with. The internals of this package make
heavy use of unsafe pointer arithmetics and other performance optimizations,
and therefore are not as approachable as typical Go programs. Basically, we put
a bigger burden on maintainers to achieve better runtime cost without
sacrificing developer productivity.

For these reasons, we also don't believe that this code should be ported upstream
to the standard `encoding/json` package. The standard library has to remain
readable and approachable to maximize stability and maintainability, and make
projects like this one possible because a high quality reference implementation
already exists.
```

## File: `json/codec.go`
```go
package json

import (
	"encoding"
	"encoding/json"
	"fmt"
	"maps"
	"math/big"
	"reflect"
	"sort"
	"strconv"
	"strings"
	"sync/atomic"
	"time"
	"unicode"
	"unsafe"

	"github.com/segmentio/asm/keyset"
)

const (
	// 1000 is the value used by the standard encoding/json package.
	//
	// https://cs.opensource.google/go/go/+/refs/tags/go1.17.3:src/encoding/json/encode.go;drc=refs%2Ftags%2Fgo1.17.3;l=300
	startDetectingCyclesAfter = 1000
)

type codec struct {
	encode encodeFunc
	decode decodeFunc
}

type encoder struct {
	flags AppendFlags
	// ptrDepth tracks the depth of pointer cycles, when it reaches the value
	// of startDetectingCyclesAfter, the ptrSeen map is allocated and the
	// encoder starts tracking pointers it has seen as an attempt to detect
	// whether it has entered a pointer cycle and needs to error before the
	// goroutine runs out of stack space.
	ptrDepth uint32
	ptrSeen  map[unsafe.Pointer]struct{}
}

type decoder struct {
	flags ParseFlags
}

type (
	encodeFunc func(encoder, []byte, unsafe.Pointer) ([]byte, error)
	decodeFunc func(decoder, []byte, unsafe.Pointer) ([]byte, error)
)

type (
	emptyFunc func(unsafe.Pointer) bool
	sortFunc  func([]reflect.Value)
)

// Eventually consistent cache mapping go types to dynamically generated
// codecs.
//
// Note: using a uintptr as key instead of reflect.Type shaved ~15ns off of
// the ~30ns Marhsal/Unmarshal functions which were dominated by the map
// lookup time for simple types like bool, int, etc..
var cache atomic.Pointer[map[unsafe.Pointer]codec]

func cacheLoad() map[unsafe.Pointer]codec {
	p := cache.Load()
	if p == nil {
		return nil
	}

	return *p
}

func cacheStore(typ reflect.Type, cod codec, oldCodecs map[unsafe.Pointer]codec) {
	newCodecs := make(map[unsafe.Pointer]codec, len(oldCodecs)+1)
	maps.Copy(newCodecs, oldCodecs)
	newCodecs[typeid(typ)] = cod

	cache.Store(&newCodecs)
}

func typeid(t reflect.Type) unsafe.Pointer {
	return (*iface)(unsafe.Pointer(&t)).ptr
}

func constructCachedCodec(t reflect.Type, cache map[unsafe.Pointer]codec) codec {
	c := constructCodec(t, map[reflect.Type]*structType{}, t.Kind() == reflect.Ptr)

	if inlined(t) {
		c.encode = constructInlineValueEncodeFunc(c.encode)
	}

	cacheStore(t, c, cache)
	return c
}

func constructCodec(t reflect.Type, seen map[reflect.Type]*structType, canAddr bool) (c codec) {
	switch t {
	case nullType, nil:
		c = codec{encode: encoder.encodeNull, decode: decoder.decodeNull}

	case numberType:
		c = codec{encode: encoder.encodeNumber, decode: decoder.decodeNumber}

	case bytesType:
		c = codec{encode: encoder.encodeBytes, decode: decoder.decodeBytes}

	case durationType:
		c = codec{encode: encoder.encodeDuration, decode: decoder.decodeDuration}

	case timeType:
		c = codec{encode: encoder.encodeTime, decode: decoder.decodeTime}

	case interfaceType:
		c = codec{encode: encoder.encodeInterface, decode: decoder.decodeInterface}

	case rawMessageType:
		c = codec{encode: encoder.encodeRawMessage, decode: decoder.decodeRawMessage}

	case numberPtrType:
		c = constructPointerCodec(numberPtrType, nil)

	case durationPtrType:
		c = constructPointerCodec(durationPtrType, nil)

	case timePtrType:
		c = constructPointerCodec(timePtrType, nil)

	case rawMessagePtrType:
		c = constructPointerCodec(rawMessagePtrType, nil)
	}

	if c.encode != nil {
		return
	}

	switch t.Kind() {
	case reflect.Bool:
		c = codec{encode: encoder.encodeBool, decode: decoder.decodeBool}

	case reflect.Int:
		c = codec{encode: encoder.encodeInt, decode: decoder.decodeInt}

	case reflect.Int8:
		c = codec{encode: encoder.encodeInt8, decode: decoder.decodeInt8}

	case reflect.Int16:
		c = codec{encode: encoder.encodeInt16, decode: decoder.decodeInt16}

	case reflect.Int32:
		c = codec{encode: encoder.encodeInt32, decode: decoder.decodeInt32}

	case reflect.Int64:
		c = codec{encode: encoder.encodeInt64, decode: decoder.decodeInt64}

	case reflect.Uint:
		c = codec{encode: encoder.encodeUint, decode: decoder.decodeUint}

	case reflect.Uintptr:
		c = codec{encode: encoder.encodeUintptr, decode: decoder.decodeUintptr}

	case reflect.Uint8:
		c = codec{encode: encoder.encodeUint8, decode: decoder.decodeUint8}

	case reflect.Uint16:
		c = codec{encode: encoder.encodeUint16, decode: decoder.decodeUint16}

	case reflect.Uint32:
		c = codec{encode: encoder.encodeUint32, decode: decoder.decodeUint32}

	case reflect.Uint64:
		c = codec{encode: encoder.encodeUint64, decode: decoder.decodeUint64}

	case reflect.Float32:
		c = codec{encode: encoder.encodeFloat32, decode: decoder.decodeFloat32}

	case reflect.Float64:
		c = codec{encode: encoder.encodeFloat64, decode: decoder.decodeFloat64}

	case reflect.String:
		c = codec{encode: encoder.encodeString, decode: decoder.decodeString}

	case reflect.Interface:
		c = constructInterfaceCodec(t)

	case reflect.Array:
		c = constructArrayCodec(t, seen, canAddr)

	case reflect.Slice:
		c = constructSliceCodec(t, seen)

	case reflect.Map:
		c = constructMapCodec(t, seen)

	case reflect.Struct:
		c = constructStructCodec(t, seen, canAddr)

	case reflect.Ptr:
		c = constructPointerCodec(t, seen)

	default:
		c = constructUnsupportedTypeCodec(t)
	}

	p := reflect.PointerTo(t)

	if canAddr {
		switch {
		case p.Implements(jsonMarshalerType):
			c.encode = constructJSONMarshalerEncodeFunc(t, true)
		case p.Implements(textMarshalerType):
			c.encode = constructTextMarshalerEncodeFunc(t, true)
		}
	}

	switch {
	case t.Implements(jsonMarshalerType):
		c.encode = constructJSONMarshalerEncodeFunc(t, false)
	case t.Implements(textMarshalerType):
		c.encode = constructTextMarshalerEncodeFunc(t, false)
	}

	switch {
	case p.Implements(jsonUnmarshalerType):
		c.decode = constructJSONUnmarshalerDecodeFunc(t, true)
	case p.Implements(textUnmarshalerType):
		c.decode = constructTextUnmarshalerDecodeFunc(t, true)
	}

	return
}

func constructStringCodec(t reflect.Type, seen map[reflect.Type]*structType, canAddr bool) codec {
	c := constructCodec(t, seen, canAddr)
	return codec{
		encode: constructStringEncodeFunc(c.encode),
		decode: constructStringDecodeFunc(c.decode),
	}
}

func constructStringEncodeFunc(encode encodeFunc) encodeFunc {
	return func(e encoder, b []byte, p unsafe.Pointer) ([]byte, error) {
		return e.encodeToString(b, p, encode)
	}
}

func constructStringDecodeFunc(decode decodeFunc) decodeFunc {
	return func(d decoder, b []byte, p unsafe.Pointer) ([]byte, error) {
		return d.decodeFromString(b, p, decode)
	}
}

func constructStringToIntDecodeFunc(t reflect.Type, decode decodeFunc) decodeFunc {
	return func(d decoder, b []byte, p unsafe.Pointer) ([]byte, error) {
		return d.decodeFromStringToInt(b, p, t, decode)
	}
}

func constructArrayCodec(t reflect.Type, seen map[reflect.Type]*structType, canAddr bool) codec {
	e := t.Elem()
	c := constructCodec(e, seen, canAddr)
	s := alignedSize(e)
	return codec{
		encode: constructArrayEncodeFunc(s, t, c.encode),
		decode: constructArrayDecodeFunc(s, t, c.decode),
	}
}

func constructArrayEncodeFunc(size uintptr, t reflect.Type, encode encodeFunc) encodeFunc {
	n := t.Len()
	return func(e encoder, b []byte, p unsafe.Pointer) ([]byte, error) {
		return e.encodeArray(b, p, n, size, t, encode)
	}
}

func constructArrayDecodeFunc(size uintptr, t reflect.Type, decode decodeFunc) decodeFunc {
	n := t.Len()
	return func(d decoder, b []byte, p unsafe.Pointer) ([]byte, error) {
		return d.decodeArray(b, p, n, size, t, decode)
	}
}

func constructSliceCodec(t reflect.Type, seen map[reflect.Type]*structType) codec {
	e := t.Elem()
	s := alignedSize(e)

	if e.Kind() == reflect.Uint8 {
		// Go 1.7+ behavior: slices of byte types (and aliases) may override the
		// default encoding and decoding behaviors by implementing marshaler and
		// unmarshaler interfaces.
		p := reflect.PointerTo(e)
		c := codec{}

		switch {
		case e.Implements(jsonMarshalerType):
			c.encode = constructJSONMarshalerEncodeFunc(e, false)
		case e.Implements(textMarshalerType):
			c.encode = constructTextMarshalerEncodeFunc(e, false)
		case p.Implements(jsonMarshalerType):
			c.encode = constructJSONMarshalerEncodeFunc(e, true)
		case p.Implements(textMarshalerType):
			c.encode = constructTextMarshalerEncodeFunc(e, true)
		}

		switch {
		case e.Implements(jsonUnmarshalerType):
			c.decode = constructJSONUnmarshalerDecodeFunc(e, false)
		case e.Implements(textUnmarshalerType):
			c.decode = constructTextUnmarshalerDecodeFunc(e, false)
		case p.Implements(jsonUnmarshalerType):
			c.decode = constructJSONUnmarshalerDecodeFunc(e, true)
		case p.Implements(textUnmarshalerType):
			c.decode = constructTextUnmarshalerDecodeFunc(e, true)
		}

		if c.encode != nil {
			c.encode = constructSliceEncodeFunc(s, t, c.encode)
		} else {
			c.encode = encoder.encodeBytes
		}

		if c.decode != nil {
			c.decode = constructSliceDecodeFunc(s, t, c.decode)
		} else {
			c.decode = decoder.decodeBytes
		}

		return c
	}

	c := constructCodec(e, seen, true)
	return codec{
		encode: constructSliceEncodeFunc(s, t, c.encode),
		decode: constructSliceDecodeFunc(s, t, c.decode),
	}
}

func constructSliceEncodeFunc(size uintptr, t reflect.Type, encode encodeFunc) encodeFunc {
	return func(e encoder, b []byte, p unsafe.Pointer) ([]byte, error) {
		return e.encodeSlice(b, p, size, t, encode)
	}
}

func constructSliceDecodeFunc(size uintptr, t reflect.Type, decode decodeFunc) decodeFunc {
	return func(d decoder, b []byte, p unsafe.Pointer) ([]byte, error) {
		return d.decodeSlice(b, p, size, t, decode)
	}
}

func constructMapCodec(t reflect.Type, seen map[reflect.Type]*structType) codec {
	var sortKeys sortFunc
	k := t.Key()
	v := t.Elem()

	// Faster implementations for some common cases.
	switch {
	case k == stringType && v == interfaceType:
		return codec{
			encode: encoder.encodeMapStringInterface,
			decode: decoder.decodeMapStringInterface,
		}

	case k == stringType && v == rawMessageType:
		return codec{
			encode: encoder.encodeMapStringRawMessage,
			decode: decoder.decodeMapStringRawMessage,
		}

	case k == stringType && v == stringType:
		return codec{
			encode: encoder.encodeMapStringString,
			decode: decoder.decodeMapStringString,
		}

	case k == stringType && v == stringsType:
		return codec{
			encode: encoder.encodeMapStringStringSlice,
			decode: decoder.decodeMapStringStringSlice,
		}

	case k == stringType && v == boolType:
		return codec{
			encode: encoder.encodeMapStringBool,
			decode: decoder.decodeMapStringBool,
		}
	}

	kc := codec{}
	vc := constructCodec(v, seen, false)

	if k.Implements(textMarshalerType) || reflect.PointerTo(k).Implements(textUnmarshalerType) {
		kc.encode = constructTextMarshalerEncodeFunc(k, false)
		kc.decode = constructTextUnmarshalerDecodeFunc(k, true)

		sortKeys = func(keys []reflect.Value) {
			sort.Slice(keys, func(i, j int) bool {
				// This is a performance abomination but the use case is rare
				// enough that it shouldn't be a problem in practice.
				k1, _ := keys[i].Interface().(encoding.TextMarshaler).MarshalText()
				k2, _ := keys[j].Interface().(encoding.TextMarshaler).MarshalText()
				return string(k1) < string(k2)
			})
		}
	} else {
		switch k.Kind() {
		case reflect.String:
			kc.encode = encoder.encodeString
			kc.decode = decoder.decodeString

			sortKeys = func(keys []reflect.Value) {
				sort.Slice(keys, func(i, j int) bool { return keys[i].String() < keys[j].String() })
			}

		case reflect.Int,
			reflect.Int8,
			reflect.Int16,
			reflect.Int32,
			reflect.Int64:
			kc = constructStringCodec(k, seen, false)

			sortKeys = func(keys []reflect.Value) {
				sort.Slice(keys, func(i, j int) bool { return intStringsAreSorted(keys[i].Int(), keys[j].Int()) })
			}

		case reflect.Uint,
			reflect.Uintptr,
			reflect.Uint8,
			reflect.Uint16,
			reflect.Uint32,
			reflect.Uint64:
			kc = constructStringCodec(k, seen, false)

			sortKeys = func(keys []reflect.Value) {
				sort.Slice(keys, func(i, j int) bool { return uintStringsAreSorted(keys[i].Uint(), keys[j].Uint()) })
			}

		default:
			return constructUnsupportedTypeCodec(t)
		}
	}

	if inlined(v) {
		vc.encode = constructInlineValueEncodeFunc(vc.encode)
	}

	return codec{
		encode: constructMapEncodeFunc(t, kc.encode, vc.encode, sortKeys),
		decode: constructMapDecodeFunc(t, kc.decode, vc.decode),
	}
}

func constructMapEncodeFunc(t reflect.Type, encodeKey, encodeValue encodeFunc, sortKeys sortFunc) encodeFunc {
	return func(e encoder, b []byte, p unsafe.Pointer) ([]byte, error) {
		return e.encodeMap(b, p, t, encodeKey, encodeValue, sortKeys)
	}
}

func constructMapDecodeFunc(t reflect.Type, decodeKey, decodeValue decodeFunc) decodeFunc {
	kt := t.Key()
	vt := t.Elem()
	kz := reflect.Zero(kt)
	vz := reflect.Zero(vt)
	return func(d decoder, b []byte, p unsafe.Pointer) ([]byte, error) {
		return d.decodeMap(b, p, t, kt, vt, kz, vz, decodeKey, decodeValue)
	}
}

func constructStructCodec(t reflect.Type, seen map[reflect.Type]*structType, canAddr bool) codec {
	st := constructStructType(t, seen, canAddr)
	return codec{
		encode: constructStructEncodeFunc(st),
		decode: constructStructDecodeFunc(st),
	}
}

func constructStructType(t reflect.Type, seen map[reflect.Type]*structType, canAddr bool) *structType {
	// Used for preventing infinite recursion on types that have pointers to
	// themselves.
	st := seen[t]

	if st == nil {
		st = &structType{
			fields:      make([]structField, 0, t.NumField()),
			fieldsIndex: make(map[string]*structField),
			ficaseIndex: make(map[string]*structField),
			typ:         t,
		}

		seen[t] = st
		st.fields = appendStructFields(st.fields, t, 0, seen, canAddr)

		for i := range st.fields {
			f := &st.fields[i]
			s := strings.ToLower(f.name)
			st.fieldsIndex[f.name] = f
			// When there is ambiguity because multiple fields have the same
			// case-insensitive representation, the first field must win.
			if _, exists := st.ficaseIndex[s]; !exists {
				st.ficaseIndex[s] = f
			}
		}

		// At a certain point the linear scan provided by keyset is less
		// efficient than a map. The 32 was chosen based on benchmarks in the
		// segmentio/asm repo run with an Intel Kaby Lake processor and go1.17.
		if len(st.fields) <= 32 {
			keys := make([][]byte, len(st.fields))
			for i, f := range st.fields {
				keys[i] = []byte(f.name)
			}
			st.keyset = keyset.New(keys)
		}
	}

	return st
}

func constructStructEncodeFunc(st *structType) encodeFunc {
	return func(e encoder, b []byte, p unsafe.Pointer) ([]byte, error) {
		return e.encodeStruct(b, p, st)
	}
}

func constructStructDecodeFunc(st *structType) decodeFunc {
	return func(d decoder, b []byte, p unsafe.Pointer) ([]byte, error) {
		return d.decodeStruct(b, p, st)
	}
}

func constructEmbeddedStructPointerCodec(t reflect.Type, unexported bool, offset uintptr, field codec) codec {
	return codec{
		encode: constructEmbeddedStructPointerEncodeFunc(t, unexported, offset, field.encode),
		decode: constructEmbeddedStructPointerDecodeFunc(t, unexported, offset, field.decode),
	}
}

func constructEmbeddedStructPointerEncodeFunc(t reflect.Type, unexported bool, offset uintptr, encode encodeFunc) encodeFunc {
	return func(e encoder, b []byte, p unsafe.Pointer) ([]byte, error) {
		return e.encodeEmbeddedStructPointer(b, p, t, unexported, offset, encode)
	}
}

func constructEmbeddedStructPointerDecodeFunc(t reflect.Type, unexported bool, offset uintptr, decode decodeFunc) decodeFunc {
	return func(d decoder, b []byte, p unsafe.Pointer) ([]byte, error) {
		return d.decodeEmbeddedStructPointer(b, p, t, unexported, offset, decode)
	}
}

func appendStructFields(fields []structField, t reflect.Type, offset uintptr, seen map[reflect.Type]*structType, canAddr bool) []structField {
	type embeddedField struct {
		index      int
		offset     uintptr
		pointer    bool
		unexported bool
		subtype    *structType
		subfield   *structField
	}

	names := make(map[string]struct{})
	embedded := make([]embeddedField, 0, 10)

	for i := range t.NumField() {
		f := t.Field(i)

		var (
			name       = f.Name
			anonymous  = f.Anonymous
			tag        = false
			omitempty  = false
			stringify  = false
			unexported = len(f.PkgPath) != 0
		)

		if unexported && !anonymous { // unexported
			continue
		}

		if parts := strings.Split(f.Tag.Get("json"), ","); len(parts) != 0 {
			if len(parts[0]) != 0 {
				name, tag = parts[0], true
			}

			if name == "-" && len(parts) == 1 { // ignored
				continue
			}

			if !isValidTag(name) {
				name = f.Name
			}

			for _, tag := range parts[1:] {
				switch tag {
				case "omitempty":
					omitempty = true
				case "string":
					stringify = true
				}
			}
		}

		if anonymous && !tag { // embedded
			typ := f.Type
			ptr := f.Type.Kind() == reflect.Ptr

			if ptr {
				typ = f.Type.Elem()
			}

			if typ.Kind() == reflect.Struct {
				// When the embedded fields is inlined the fields can be looked
				// up by offset from the address of the wrapping object, so we
				// simply add the embedded struct fields to the list of fields
				// of the current struct type.
				subtype := constructStructType(typ, seen, canAddr)

				for j := range subtype.fields {
					embedded = append(embedded, embeddedField{
						index:      i<<32 | j,
						offset:     offset + f.Offset,
						pointer:    ptr,
						unexported: unexported,
						subtype:    subtype,
						subfield:   &subtype.fields[j],
					})
				}

				continue
			}

			if unexported { // ignore unexported non-struct types
				continue
			}
		}

		codec := constructCodec(f.Type, seen, canAddr)

		if stringify {
			// https://golang.org/pkg/encoding/json/#Marshal
			//
			// The "string" option signals that a field is stored as JSON inside
			// a JSON-encoded string. It applies only to fields of string,
			// floating point, integer, or boolean types. This extra level of
			// encoding is sometimes used when communicating with JavaScript
			// programs:
			typ := f.Type

			if typ.Kind() == reflect.Ptr {
				typ = typ.Elem()
			}

			switch typ.Kind() {
			case reflect.Int,
				reflect.Int8,
				reflect.Int16,
				reflect.Int32,
				reflect.Int64,
				reflect.Uint,
				reflect.Uintptr,
				reflect.Uint8,
				reflect.Uint16,
				reflect.Uint32,
				reflect.Uint64:
				codec.encode = constructStringEncodeFunc(codec.encode)
				codec.decode = constructStringToIntDecodeFunc(typ, codec.decode)
			case reflect.Bool,
				reflect.Float32,
				reflect.Float64,
				reflect.String:
				codec.encode = constructStringEncodeFunc(codec.encode)
				codec.decode = constructStringDecodeFunc(codec.decode)
			}
		}

		fields = append(fields, structField{
			codec:     codec,
			offset:    offset + f.Offset,
			empty:     emptyFuncOf(f.Type),
			tag:       tag,
			omitempty: omitempty,
			name:      name,
			index:     i << 32,
			typ:       f.Type,
			zero:      reflect.Zero(f.Type),
		})

		names[name] = struct{}{}
	}

	// Only unambiguous embedded fields must be serialized.
	ambiguousNames := make(map[string]int)
	ambiguousTags := make(map[string]int)

	// Embedded types can never override a field that was already present at
	// the top-level.
	for name := range names {
		ambiguousNames[name]++
		ambiguousTags[name]++
	}

	for _, embfield := range embedded {
		ambiguousNames[embfield.subfield.name]++
		if embfield.subfield.tag {
			ambiguousTags[embfield.subfield.name]++
		}
	}

	for _, embfield := range embedded {
		subfield := *embfield.subfield

		if ambiguousNames[subfield.name] > 1 && (!subfield.tag || ambiguousTags[subfield.name] != 1) {
			continue // ambiguous embedded field
		}

		if embfield.pointer {
			subfield.codec = constructEmbeddedStructPointerCodec(embfield.subtype.typ, embfield.unexported, subfield.offset, subfield.codec)
			subfield.offset = embfield.offset
		} else {
			subfield.offset += embfield.offset
		}

		// To prevent dominant flags more than one level below the embedded one.
		subfield.tag = false

		// To ensure the order of the fields in the output is the same is in the
		// struct type.
		subfield.index = embfield.index

		fields = append(fields, subfield)
	}

	for i := range fields {
		name := fields[i].name
		fields[i].json = encodeKeyFragment(name, 0)
		fields[i].html = encodeKeyFragment(name, EscapeHTML)
	}

	sort.Slice(fields, func(i, j int) bool { return fields[i].index < fields[j].index })
	return fields
}

func encodeKeyFragment(s string, flags AppendFlags) string {
	b := make([]byte, 1, len(s)+4)
	b[0] = ','
	e := encoder{flags: flags}
	b, _ = e.encodeString(b, unsafe.Pointer(&s))
	b = append(b, ':')
	return *(*string)(unsafe.Pointer(&b))
}

func constructPointerCodec(t reflect.Type, seen map[reflect.Type]*structType) codec {
	e := t.Elem()
	c := constructCodec(e, seen, true)
	return codec{
		encode: constructPointerEncodeFunc(e, c.encode),
		decode: constructPointerDecodeFunc(e, c.decode),
	}
}

func constructPointerEncodeFunc(t reflect.Type, encode encodeFunc) encodeFunc {
	return func(e encoder, b []byte, p unsafe.Pointer) ([]byte, error) {
		return e.encodePointer(b, p, t, encode)
	}
}

func constructPointerDecodeFunc(t reflect.Type, decode decodeFunc) decodeFunc {
	return func(d decoder, b []byte, p unsafe.Pointer) ([]byte, error) {
		return d.decodePointer(b, p, t, decode)
	}
}

func constructInterfaceCodec(t reflect.Type) codec {
	return codec{
		encode: constructMaybeEmptyInterfaceEncoderFunc(t),
		decode: constructMaybeEmptyInterfaceDecoderFunc(t),
	}
}

func constructMaybeEmptyInterfaceEncoderFunc(t reflect.Type) encodeFunc {
	return func(e encoder, b []byte, p unsafe.Pointer) ([]byte, error) {
		return e.encodeMaybeEmptyInterface(b, p, t)
	}
}

func constructMaybeEmptyInterfaceDecoderFunc(t reflect.Type) decodeFunc {
	return func(d decoder, b []byte, p unsafe.Pointer) ([]byte, error) {
		return d.decodeMaybeEmptyInterface(b, p, t)
	}
}

func constructUnsupportedTypeCodec(t reflect.Type) codec {
	return codec{
		encode: constructUnsupportedTypeEncodeFunc(t),
		decode: constructUnsupportedTypeDecodeFunc(t),
	}
}

func constructUnsupportedTypeEncodeFunc(t reflect.Type) encodeFunc {
	return func(e encoder, b []byte, p unsafe.Pointer) ([]byte, error) {
		return e.encodeUnsupportedTypeError(b, p, t)
	}
}

func constructUnsupportedTypeDecodeFunc(t reflect.Type) decodeFunc {
	return func(d decoder, b []byte, p unsafe.Pointer) ([]byte, error) {
		return d.decodeUnmarshalTypeError(b, p, t)
	}
}

func constructJSONMarshalerEncodeFunc(t reflect.Type, pointer bool) encodeFunc {
	return func(e encoder, b []byte, p unsafe.Pointer) ([]byte, error) {
		return e.encodeJSONMarshaler(b, p, t, pointer)
	}
}

func constructJSONUnmarshalerDecodeFunc(t reflect.Type, pointer bool) decodeFunc {
	return func(d decoder, b []byte, p unsafe.Pointer) ([]byte, error) {
		return d.decodeJSONUnmarshaler(b, p, t, pointer)
	}
}

func constructTextMarshalerEncodeFunc(t reflect.Type, pointer bool) encodeFunc {
	return func(e encoder, b []byte, p unsafe.Pointer) ([]byte, error) {
		return e.encodeTextMarshaler(b, p, t, pointer)
	}
}

func constructTextUnmarshalerDecodeFunc(t reflect.Type, pointer bool) decodeFunc {
	return func(d decoder, b []byte, p unsafe.Pointer) ([]byte, error) {
		return d.decodeTextUnmarshaler(b, p, t, pointer)
	}
}

func constructInlineValueEncodeFunc(encode encodeFunc) encodeFunc {
	return func(e encoder, b []byte, p unsafe.Pointer) ([]byte, error) {
		return encode(e, b, noescape(unsafe.Pointer(&p)))
	}
}

// noescape hides a pointer from escape analysis.  noescape is
// the identity function but escape analysis doesn't think the
// output depends on the input. noescape is inlined and currently
// compiles down to zero instructions.
// USE CAREFULLY!
// This was copied from the runtime; see issues 23382 and 7921.
//
//go:nosplit
func noescape(p unsafe.Pointer) unsafe.Pointer {
	x := uintptr(p)
	return unsafe.Pointer(x ^ 0)
}

func alignedSize(t reflect.Type) uintptr {
	a := t.Align()
	s := t.Size()
	return align(uintptr(a), uintptr(s))
}

func align(align, size uintptr) uintptr {
	if align != 0 && (size%align) != 0 {
		size = ((size / align) + 1) * align
	}
	return size
}

func inlined(t reflect.Type) bool {
	switch t.Kind() {
	case reflect.Ptr:
		return true
	case reflect.Map:
		return true
	case reflect.Struct:
		return t.NumField() == 1 && inlined(t.Field(0).Type)
	default:
		return false
	}
}

func isValidTag(s string) bool {
	if s == "" {
		return false
	}
	for _, c := range s {
		switch {
		case strings.ContainsRune("!#$%&()*+-./:;<=>?@[]^_{|}~ ", c):
			// Backslash and quote chars are reserved, but
			// otherwise any punctuation chars are allowed
			// in a tag name.
		default:
			if !unicode.IsLetter(c) && !unicode.IsDigit(c) {
				return false
			}
		}
	}
	return true
}

func emptyFuncOf(t reflect.Type) emptyFunc {
	switch t {
	case bytesType, rawMessageType:
		return func(p unsafe.Pointer) bool { return (*slice)(p).len == 0 }
	}

	switch t.Kind() {
	case reflect.Array:
		if t.Len() == 0 {
			return func(unsafe.Pointer) bool { return true }
		}

	case reflect.Map:
		return func(p unsafe.Pointer) bool { return reflect.NewAt(t, p).Elem().Len() == 0 }

	case reflect.Slice:
		return func(p unsafe.Pointer) bool { return (*slice)(p).len == 0 }

	case reflect.String:
		return func(p unsafe.Pointer) bool { return len(*(*string)(p)) == 0 }

	case reflect.Bool:
		return func(p unsafe.Pointer) bool { return !*(*bool)(p) }

	case reflect.Int, reflect.Uint:
		return func(p unsafe.Pointer) bool { return *(*uint)(p) == 0 }

	case reflect.Uintptr:
		return func(p unsafe.Pointer) bool { return *(*uintptr)(p) == 0 }

	case reflect.Int8, reflect.Uint8:
		return func(p unsafe.Pointer) bool { return *(*uint8)(p) == 0 }

	case reflect.Int16, reflect.Uint16:
		return func(p unsafe.Pointer) bool { return *(*uint16)(p) == 0 }

	case reflect.Int32, reflect.Uint32:
		return func(p unsafe.Pointer) bool { return *(*uint32)(p) == 0 }

	case reflect.Int64, reflect.Uint64:
		return func(p unsafe.Pointer) bool { return *(*uint64)(p) == 0 }

	case reflect.Float32:
		return func(p unsafe.Pointer) bool { return *(*float32)(p) == 0 }

	case reflect.Float64:
		return func(p unsafe.Pointer) bool { return *(*float64)(p) == 0 }

	case reflect.Ptr:
		return func(p unsafe.Pointer) bool { return *(*unsafe.Pointer)(p) == nil }

	case reflect.Interface:
		return func(p unsafe.Pointer) bool { return (*iface)(p).ptr == nil }
	}

	return func(unsafe.Pointer) bool { return false }
}

type iface struct {
	typ unsafe.Pointer
	ptr unsafe.Pointer
}

type slice struct {
	data unsafe.Pointer
	len  int
	cap  int
}

type structType struct {
	fields      []structField
	fieldsIndex map[string]*structField
	ficaseIndex map[string]*structField
	keyset      []byte
	typ         reflect.Type
}

type structField struct {
	codec     codec
	offset    uintptr
	empty     emptyFunc
	tag       bool
	omitempty bool
	json      string
	html      string
	name      string
	typ       reflect.Type
	zero      reflect.Value
	index     int
}

func unmarshalTypeError(b []byte, t reflect.Type) error {
	return &UnmarshalTypeError{Value: strconv.Quote(prefix(b)), Type: t}
}

func unmarshalOverflow(b []byte, t reflect.Type) error {
	return &UnmarshalTypeError{Value: "number " + prefix(b) + " overflows", Type: t}
}

func unexpectedEOF(b []byte) error {
	return syntaxError(b, "unexpected end of JSON input")
}

var syntaxErrorMsgOffset = ^uintptr(0)

func init() {
	t := reflect.TypeOf(SyntaxError{})
	for i := range t.NumField() {
		if f := t.Field(i); f.Type.Kind() == reflect.String {
			syntaxErrorMsgOffset = f.Offset
		}
	}
}

func syntaxError(b []byte, msg string, args ...any) error {
	e := new(SyntaxError)
	i := syntaxErrorMsgOffset
	if i != ^uintptr(0) {
		s := "json: " + fmt.Sprintf(msg, args...) + ": " + prefix(b)
		p := unsafe.Pointer(e)
		// Hack to set the unexported `msg` field.
		*(*string)(unsafe.Pointer(uintptr(p) + i)) = s
	}
	return e
}

func objectKeyError(b []byte, err error) ([]byte, error) {
	if len(b) == 0 {
		return nil, unexpectedEOF(b)
	}
	switch err.(type) {
	case *UnmarshalTypeError:
		err = syntaxError(b, "invalid character '%c' looking for beginning of object key", b[0])
	}
	return b, err
}

func prefix(b []byte) string {
	if len(b) < 32 {
		return string(b)
	}
	return string(b[:32]) + "..."
}

func intStringsAreSorted(i0, i1 int64) bool {
	var b0, b1 [32]byte
	return string(strconv.AppendInt(b0[:0], i0, 10)) < string(strconv.AppendInt(b1[:0], i1, 10))
}

func uintStringsAreSorted(u0, u1 uint64) bool {
	var b0, b1 [32]byte
	return string(strconv.AppendUint(b0[:0], u0, 10)) < string(strconv.AppendUint(b1[:0], u1, 10))
}

func stringToBytes(s string) []byte {
	return *(*[]byte)(unsafe.Pointer(&sliceHeader{
		Data: *(*unsafe.Pointer)(unsafe.Pointer(&s)),
		Len:  len(s),
		Cap:  len(s),
	}))
}

type sliceHeader struct {
	Data unsafe.Pointer
	Len  int
	Cap  int
}

var (
	nullType = reflect.TypeOf(nil)
	boolType = reflect.TypeOf(false)

	intType   = reflect.TypeOf(int(0))
	int8Type  = reflect.TypeOf(int8(0))
	int16Type = reflect.TypeOf(int16(0))
	int32Type = reflect.TypeOf(int32(0))
	int64Type = reflect.TypeOf(int64(0))

	uintType    = reflect.TypeOf(uint(0))
	uint8Type   = reflect.TypeOf(uint8(0))
	uint16Type  = reflect.TypeOf(uint16(0))
	uint32Type  = reflect.TypeOf(uint32(0))
	uint64Type  = reflect.TypeOf(uint64(0))
	uintptrType = reflect.TypeOf(uintptr(0))

	float32Type = reflect.TypeOf(float32(0))
	float64Type = reflect.TypeOf(float64(0))

	bigIntType     = reflect.TypeOf(new(big.Int))
	numberType     = reflect.TypeOf(json.Number(""))
	stringType     = reflect.TypeOf("")
	stringsType    = reflect.TypeOf([]string(nil))
	bytesType      = reflect.TypeOf(([]byte)(nil))
	durationType   = reflect.TypeOf(time.Duration(0))
	timeType       = reflect.TypeOf(time.Time{})
	rawMessageType = reflect.TypeOf(RawMessage(nil))

	numberPtrType     = reflect.PointerTo(numberType)
	durationPtrType   = reflect.PointerTo(durationType)
	timePtrType       = reflect.PointerTo(timeType)
	rawMessagePtrType = reflect.PointerTo(rawMessageType)

	sliceInterfaceType       = reflect.TypeOf(([]any)(nil))
	sliceStringType          = reflect.TypeOf(([]any)(nil))
	mapStringInterfaceType   = reflect.TypeOf((map[string]any)(nil))
	mapStringRawMessageType  = reflect.TypeOf((map[string]RawMessage)(nil))
	mapStringStringType      = reflect.TypeOf((map[string]string)(nil))
	mapStringStringSliceType = reflect.TypeOf((map[string][]string)(nil))
	mapStringBoolType        = reflect.TypeOf((map[string]bool)(nil))

	interfaceType       = reflect.TypeOf((*any)(nil)).Elem()
	jsonMarshalerType   = reflect.TypeOf((*Marshaler)(nil)).Elem()
	jsonUnmarshalerType = reflect.TypeOf((*Unmarshaler)(nil)).Elem()
	textMarshalerType   = reflect.TypeOf((*encoding.TextMarshaler)(nil)).Elem()
	textUnmarshalerType = reflect.TypeOf((*encoding.TextUnmarshaler)(nil)).Elem()

	bigIntDecoder = constructJSONUnmarshalerDecodeFunc(bigIntType, false)
)

// =============================================================================
// Copyright 2009 The Go Authors. All rights reserved.
// Use of this source code is governed by a BSD-style
// license that can be found in the LICENSE file.

// appendDuration appends a human-readable representation of d to b.
//
// The function copies the implementation of time.Duration.String but prevents
// Go from making a dynamic memory allocation on the returned value.
func appendDuration(b []byte, d time.Duration) []byte {
	// Largest time is 2540400h10m10.000000000s
	var buf [32]byte
	w := len(buf)

	u := uint64(d)
	neg := d < 0
	if neg {
		u = -u
	}

	if u < uint64(time.Second) {
		// Special case: if duration is smaller than a second,
		// use smaller units, like 1.2ms
		var prec int
		w--
		buf[w] = 's'
		w--
		switch {
		case u == 0:
			return append(b, '0', 's')
		case u < uint64(time.Microsecond):
			// print nanoseconds
			prec = 0
			buf[w] = 'n'
		case u < uint64(time.Millisecond):
			// print microseconds
			prec = 3
			// U+00B5 'µ' micro sign == 0xC2 0xB5
			w-- // Need room for two bytes.
			copy(buf[w:], "µ")
		default:
			// print milliseconds
			prec = 6
			buf[w] = 'm'
		}
		w, u = fmtFrac(buf[:w], u, prec)
		w = fmtInt(buf[:w], u)
	} else {
		w--
		buf[w] = 's'

		w, u = fmtFrac(buf[:w], u, 9)

		// u is now integer seconds
		w = fmtInt(buf[:w], u%60)
		u /= 60

		// u is now integer minutes
		if u > 0 {
			w--
			buf[w] = 'm'
			w = fmtInt(buf[:w], u%60)
			u /= 60

			// u is now integer hours
			// Stop at hours because days can be different lengths.
			if u > 0 {
				w--
				buf[w] = 'h'
				w = fmtInt(buf[:w], u)
			}
		}
	}

	if neg {
		w--
		buf[w] = '-'
	}

	return append(b, buf[w:]...)
}

// fmtFrac formats the fraction of v/10**prec (e.g., ".12345") into the
// tail of buf, omitting trailing zeros.  it omits the decimal
// point too when the fraction is 0.  It returns the index where the
// output bytes begin and the value v/10**prec.
func fmtFrac(buf []byte, v uint64, prec int) (nw int, nv uint64) {
	// Omit trailing zeros up to and including decimal point.
	w := len(buf)
	print := false
	for range prec {
		digit := v % 10
		print = print || digit != 0
		if print {
			w--
			buf[w] = byte(digit) + '0'
		}
		v /= 10
	}
	if print {
		w--
		buf[w] = '.'
	}
	return w, v
}

// fmtInt formats v into the tail of buf.
// It returns the index where the output begins.
func fmtInt(buf []byte, v uint64) int {
	w := len(buf)
	if v == 0 {
		w--
		buf[w] = '0'
	} else {
		for v > 0 {
			w--
			buf[w] = byte(v%10) + '0'
			v /= 10
		}
	}
	return w
}

// =============================================================================
```

## File: `json/decode.go`
```go
package json

import (
	"bytes"
	"encoding"
	"encoding/json"
	"fmt"
	"math"
	"math/big"
	"reflect"
	"strconv"
	"time"
	"unsafe"

	"github.com/segmentio/asm/base64"
	"github.com/segmentio/asm/keyset"
	"github.com/segmentio/encoding/iso8601"
)

func (d decoder) anyFlagsSet(flags ParseFlags) bool {
	return d.flags&flags != 0
}

func (d decoder) decodeNull(b []byte, p unsafe.Pointer) ([]byte, error) {
	if hasNullPrefix(b) {
		return b[4:], nil
	}
	return d.inputError(b, nullType)
}

func (d decoder) decodeBool(b []byte, p unsafe.Pointer) ([]byte, error) {
	switch {
	case hasTruePrefix(b):
		*(*bool)(p) = true
		return b[4:], nil

	case hasFalsePrefix(b):
		*(*bool)(p) = false
		return b[5:], nil

	case hasNullPrefix(b):
		return b[4:], nil

	default:
		return d.inputError(b, boolType)
	}
}

func (d decoder) decodeInt(b []byte, p unsafe.Pointer) ([]byte, error) {
	if hasNullPrefix(b) {
		return b[4:], nil
	}

	v, r, err := d.parseInt(b, intType)
	if err != nil {
		return r, err
	}

	*(*int)(p) = int(v)
	return r, nil
}

func (d decoder) decodeInt8(b []byte, p unsafe.Pointer) ([]byte, error) {
	if hasNullPrefix(b) {
		return b[4:], nil
	}

	v, r, err := d.parseInt(b, int8Type)
	if err != nil {
		return r, err
	}

	if v < math.MinInt8 || v > math.MaxInt8 {
		return r, unmarshalOverflow(b[:len(b)-len(r)], int8Type)
	}

	*(*int8)(p) = int8(v)
	return r, nil
}

func (d decoder) decodeInt16(b []byte, p unsafe.Pointer) ([]byte, error) {
	if hasNullPrefix(b) {
		return b[4:], nil
	}

	v, r, err := d.parseInt(b, int16Type)
	if err != nil {
		return r, err
	}

	if v < math.MinInt16 || v > math.MaxInt16 {
		return r, unmarshalOverflow(b[:len(b)-len(r)], int16Type)
	}

	*(*int16)(p) = int16(v)
	return r, nil
}

func (d decoder) decodeInt32(b []byte, p unsafe.Pointer) ([]byte, error) {
	if hasNullPrefix(b) {
		return b[4:], nil
	}

	v, r, err := d.parseInt(b, int32Type)
	if err != nil {
		return r, err
	}

	if v < math.MinInt32 || v > math.MaxInt32 {
		return r, unmarshalOverflow(b[:len(b)-len(r)], int32Type)
	}

	*(*int32)(p) = int32(v)
	return r, nil
}

func (d decoder) decodeInt64(b []byte, p unsafe.Pointer) ([]byte, error) {
	if hasNullPrefix(b) {
		return b[4:], nil
	}

	v, r, err := d.parseInt(b, int64Type)
	if err != nil {
		return r, err
	}

	*(*int64)(p) = v
	return r, nil
}

func (d decoder) decodeUint(b []byte, p unsafe.Pointer) ([]byte, error) {
	if hasNullPrefix(b) {
		return b[4:], nil
	}

	v, r, err := d.parseUint(b, uintType)
	if err != nil {
		return r, err
	}

	*(*uint)(p) = uint(v)
	return r, nil
}

func (d decoder) decodeUintptr(b []byte, p unsafe.Pointer) ([]byte, error) {
	if hasNullPrefix(b) {
		return b[4:], nil
	}

	v, r, err := d.parseUint(b, uintptrType)
	if err != nil {
		return r, err
	}

	*(*uintptr)(p) = uintptr(v)
	return r, nil
}

func (d decoder) decodeUint8(b []byte, p unsafe.Pointer) ([]byte, error) {
	if hasNullPrefix(b) {
		return b[4:], nil
	}

	v, r, err := d.parseUint(b, uint8Type)
	if err != nil {
		return r, err
	}

	if v > math.MaxUint8 {
		return r, unmarshalOverflow(b[:len(b)-len(r)], uint8Type)
	}

	*(*uint8)(p) = uint8(v)
	return r, nil
}

func (d decoder) decodeUint16(b []byte, p unsafe.Pointer) ([]byte, error) {
	if hasNullPrefix(b) {
		return b[4:], nil
	}

	v, r, err := d.parseUint(b, uint16Type)
	if err != nil {
		return r, err
	}

	if v > math.MaxUint16 {
		return r, unmarshalOverflow(b[:len(b)-len(r)], uint16Type)
	}

	*(*uint16)(p) = uint16(v)
	return r, nil
}

func (d decoder) decodeUint32(b []byte, p unsafe.Pointer) ([]byte, error) {
	if hasNullPrefix(b) {
		return b[4:], nil
	}

	v, r, err := d.parseUint(b, uint32Type)
	if err != nil {
		return r, err
	}

	if v > math.MaxUint32 {
		return r, unmarshalOverflow(b[:len(b)-len(r)], uint32Type)
	}

	*(*uint32)(p) = uint32(v)
	return r, nil
}

func (d decoder) decodeUint64(b []byte, p unsafe.Pointer) ([]byte, error) {
	if hasNullPrefix(b) {
		return b[4:], nil
	}

	v, r, err := d.parseUint(b, uint64Type)
	if err != nil {
		return r, err
	}

	*(*uint64)(p) = v
	return r, nil
}

func (d decoder) decodeFloat32(b []byte, p unsafe.Pointer) ([]byte, error) {
	if hasNullPrefix(b) {
		return b[4:], nil
	}

	v, r, _, err := d.parseNumber(b)
	if err != nil {
		return d.inputError(b, float32Type)
	}

	f, err := strconv.ParseFloat(*(*string)(unsafe.Pointer(&v)), 32)
	if err != nil {
		return d.inputError(b, float32Type)
	}

	*(*float32)(p) = float32(f)
	return r, nil
}

func (d decoder) decodeFloat64(b []byte, p unsafe.Pointer) ([]byte, error) {
	if hasNullPrefix(b) {
		return b[4:], nil
	}

	v, r, _, err := d.parseNumber(b)
	if err != nil {
		return d.inputError(b, float64Type)
	}

	f, err := strconv.ParseFloat(*(*string)(unsafe.Pointer(&v)), 64)
	if err != nil {
		return d.inputError(b, float64Type)
	}

	*(*float64)(p) = f
	return r, nil
}

func (d decoder) decodeNumber(b []byte, p unsafe.Pointer) ([]byte, error) {
	if hasNullPrefix(b) {
		return b[4:], nil
	}

	v, r, _, err := d.parseNumber(b)
	if err != nil {
		return d.inputError(b, numberType)
	}

	if (d.flags & DontCopyNumber) != 0 {
		*(*Number)(p) = *(*Number)(unsafe.Pointer(&v))
	} else {
		*(*Number)(p) = Number(v)
	}

	return r, nil
}

func (d decoder) decodeString(b []byte, p unsafe.Pointer) ([]byte, error) {
	if hasNullPrefix(b) {
		return b[4:], nil
	}

	s, r, new, err := d.parseStringUnquote(b, nil)
	if err != nil {
		if len(b) == 0 || b[0] != '"' {
			return d.inputError(b, stringType)
		}
		return r, err
	}

	if new || (d.flags&DontCopyString) != 0 {
		*(*string)(p) = *(*string)(unsafe.Pointer(&s))
	} else {
		*(*string)(p) = string(s)
	}

	return r, nil
}

func (d decoder) decodeFromString(b []byte, p unsafe.Pointer, decode decodeFunc) ([]byte, error) {
	if hasNullPrefix(b) {
		return decode(d, b, p)
	}

	v, b, _, err := d.parseStringUnquote(b, nil)
	if err != nil {
		return d.inputError(v, stringType)
	}

	if v, err = decode(d, v, p); err != nil {
		return b, err
	}

	if v = skipSpaces(v); len(v) != 0 {
		return b, syntaxError(v, "unexpected trailing tokens after string value")
	}

	return b, nil
}

func (d decoder) decodeFromStringToInt(b []byte, p unsafe.Pointer, t reflect.Type, decode decodeFunc) ([]byte, error) {
	if hasNullPrefix(b) {
		return decode(d, b, p)
	}

	if len(b) > 0 && b[0] != '"' {
		v, r, k, err := d.parseNumber(b)
		if err == nil {
			// The encoding/json package will return a *json.UnmarshalTypeError if
			// the input was a floating point number representation, even tho a
			// string is expected here.
			if k == Float {
				_, err := strconv.ParseFloat(*(*string)(unsafe.Pointer(&v)), 64)
				if err != nil {
					return r, unmarshalTypeError(v, t)
				}
			}
		}
		return r, fmt.Errorf("json: invalid use of ,string struct tag, trying to unmarshal unquoted value into int")
	}

	if len(b) > 1 && b[0] == '"' && b[1] == '"' {
		return b, fmt.Errorf("json: invalid use of ,string struct tag, trying to unmarshal \"\" into int")
	}

	v, b, _, err := d.parseStringUnquote(b, nil)
	if err != nil {
		return d.inputError(v, t)
	}

	if hasLeadingZeroes(v) {
		// In this context the encoding/json package accepts leading zeroes because
		// it is not constrained by the JSON syntax, remove them so the parsing
		// functions don't return syntax errors.
		u := make([]byte, 0, len(v))
		i := 0

		if i < len(v) && v[i] == '-' || v[i] == '+' {
			u = append(u, v[i])
			i++
		}

		for (i+1) < len(v) && v[i] == '0' && '0' <= v[i+1] && v[i+1] <= '9' {
			i++
		}

		v = append(u, v[i:]...)
	}

	if r, err := decode(d, v, p); err != nil {
		if _, isSyntaxError := err.(*SyntaxError); isSyntaxError {
			if hasPrefix(v, "-") {
				// The standard library interprets sequences of '-' characters
				// as numbers but still returns type errors in this case...
				return b, unmarshalTypeError(v, t)
			}
			return b, fmt.Errorf("json: invalid use of ,string struct tag, trying to unmarshal %q into int", prefix(v))
		}
		// When the input value was a valid number representation we retain the
		// error returned by the decoder.
		if _, _, _, err := d.parseNumber(v); err != nil {
			// When the input value valid JSON we mirror the behavior of the
			// encoding/json package and return a generic error.
			if _, _, _, err := d.parseValue(v); err == nil {
				return b, fmt.Errorf("json: invalid use of ,string struct tag, trying to unmarshal %q into int", prefix(v))
			}
		}
		return b, err
	} else if len(r) != 0 {
		return r, unmarshalTypeError(v, t)
	}

	return b, nil
}

func (d decoder) decodeBytes(b []byte, p unsafe.Pointer) ([]byte, error) {
	if hasNullPrefix(b) {
		*(*[]byte)(p) = nil
		return b[4:], nil
	}

	if len(b) < 2 {
		return d.inputError(b, bytesType)
	}

	if b[0] != '"' {
		// Go 1.7- behavior: bytes slices may be decoded from array of integers.
		if len(b) > 0 && b[0] == '[' {
			return d.decodeSlice(b, p, 1, bytesType, decoder.decodeUint8)
		}
		return d.inputError(b, bytesType)
	}

	// The input string contains escaped sequences, we need to parse it before
	// decoding it to match the encoding/json package behvaior.
	src, r, _, err := d.parseStringUnquote(b, nil)
	if err != nil {
		return d.inputError(b, bytesType)
	}

	dst := make([]byte, base64.StdEncoding.DecodedLen(len(src)))

	n, err := base64.StdEncoding.Decode(dst, src)
	if err != nil {
		return r, err
	}

	*(*[]byte)(p) = dst[:n]
	return r, nil
}

func (d decoder) decodeDuration(b []byte, p unsafe.Pointer) ([]byte, error) {
	if hasNullPrefix(b) {
		return b[4:], nil
	}

	// in order to inter-operate with the stdlib, we must be able to interpret
	// durations passed as integer values.  there's some discussion about being
	// flexible on how durations are formatted, but for the time being, it's
	// been punted to go2 at the earliest: https://github.com/golang/go/issues/4712
	if len(b) > 0 && b[0] != '"' {
		v, r, err := d.parseInt(b, durationType)
		if err != nil {
			return d.inputError(b, int32Type)
		}

		if v < math.MinInt64 || v > math.MaxInt64 {
			return r, unmarshalOverflow(b[:len(b)-len(r)], int32Type)
		}

		*(*time.Duration)(p) = time.Duration(v)
		return r, nil
	}

	if len(b) < 2 || b[0] != '"' {
		return d.inputError(b, durationType)
	}

	i := bytes.IndexByte(b[1:], '"') + 1
	if i <= 0 {
		return d.inputError(b, durationType)
	}

	s := b[1:i] // trim quotes

	v, err := time.ParseDuration(*(*string)(unsafe.Pointer(&s)))
	if err != nil {
		return d.inputError(b, durationType)
	}

	*(*time.Duration)(p) = v
	return b[i+1:], nil
}

func (d decoder) decodeTime(b []byte, p unsafe.Pointer) ([]byte, error) {
	if hasNullPrefix(b) {
		return b[4:], nil
	}

	if len(b) < 2 || b[0] != '"' {
		return d.inputError(b, timeType)
	}

	i := bytes.IndexByte(b[1:], '"') + 1
	if i <= 0 {
		return d.inputError(b, timeType)
	}

	s := b[1:i] // trim quotes

	v, err := iso8601.Parse(*(*string)(unsafe.Pointer(&s)))
	if err != nil {
		return d.inputError(b, timeType)
	}

	*(*time.Time)(p) = v
	return b[i+1:], nil
}

func (d decoder) decodeArray(b []byte, p unsafe.Pointer, n int, size uintptr, t reflect.Type, decode decodeFunc) ([]byte, error) {
	if hasNullPrefix(b) {
		return b[4:], nil
	}

	if len(b) < 2 || b[0] != '[' {
		return d.inputError(b, t)
	}
	b = b[1:]

	var err error
	for i := range n {
		b = skipSpaces(b)

		if i != 0 {
			if len(b) == 0 {
				return b, syntaxError(b, "unexpected EOF after array element")
			}
			switch b[0] {
			case ',':
				b = skipSpaces(b[1:])
			case ']':
				return b[1:], nil
			default:
				return b, syntaxError(b, "expected ',' after array element but found '%c'", b[0])
			}
		}

		b, err = decode(d, b, unsafe.Pointer(uintptr(p)+(uintptr(i)*size)))
		if err != nil {
			if e, ok := err.(*UnmarshalTypeError); ok {
				e.Struct = t.String() + e.Struct
				e.Field = d.prependField(strconv.Itoa(i), e.Field)
			}
			return b, err
		}
	}

	// The encoding/json package ignores extra elements found when decoding into
	// array types (which have a fixed size).
	for {
		b = skipSpaces(b)

		if len(b) == 0 {
			return b, syntaxError(b, "missing closing ']' in array value")
		}

		switch b[0] {
		case ',':
			b = skipSpaces(b[1:])
		case ']':
			return b[1:], nil
		}

		_, b, _, err = d.parseValue(b)
		if err != nil {
			return b, err
		}
	}
}

// This is a placeholder used to consturct non-nil empty slices.
var empty struct{}

func (d decoder) decodeSlice(b []byte, p unsafe.Pointer, size uintptr, t reflect.Type, decode decodeFunc) ([]byte, error) {
	if hasNullPrefix(b) {
		*(*slice)(p) = slice{}
		return b[4:], nil
	}

	if len(b) < 2 {
		return d.inputError(b, t)
	}

	if b[0] != '[' {
		// Go 1.7- behavior: fallback to decoding as a []byte if the element
		// type is byte; allow conversions from JSON strings even tho the
		// underlying type implemented unmarshaler interfaces.
		if t.Elem().Kind() == reflect.Uint8 {
			return d.decodeBytes(b, p)
		}
		return d.inputError(b, t)
	}

	input := b
	b = b[1:]

	s := (*slice)(p)
	s.len = 0

	var err error
	for {
		b = skipSpaces(b)

		if len(b) != 0 && b[0] == ']' {
			if s.data == nil {
				s.data = unsafe.Pointer(&empty)
			}
			return b[1:], nil
		}

		if s.len != 0 {
			if len(b) == 0 {
				return b, syntaxError(b, "unexpected EOF after array element")
			}
			if b[0] != ',' {
				return b, syntaxError(b, "expected ',' after array element but found '%c'", b[0])
			}
			b = skipSpaces(b[1:])
		}

		if s.len == s.cap {
			c := s.cap

			if c == 0 {
				c = 10
			} else {
				c *= 2
			}

			*s = extendSlice(t, s, c)
		}

		b, err = decode(d, b, unsafe.Pointer(uintptr(s.data)+(uintptr(s.len)*size)))
		if err != nil {
			if _, r, _, err := d.parseValue(input); err != nil {
				return r, err
			} else {
				b = r
			}
			if e, ok := err.(*UnmarshalTypeError); ok {
				e.Struct = t.String() + e.Struct
				e.Field = d.prependField(strconv.Itoa(s.len), e.Field)
			}
			return b, err
		}

		s.len++
	}
}

func (d decoder) decodeMap(b []byte, p unsafe.Pointer, t, kt, vt reflect.Type, kz, vz reflect.Value, decodeKey, decodeValue decodeFunc) ([]byte, error) {
	if hasNullPrefix(b) {
		*(*unsafe.Pointer)(p) = nil
		return b[4:], nil
	}

	if len(b) < 2 || b[0] != '{' {
		return d.inputError(b, t)
	}
	i := 0
	m := reflect.NewAt(t, p).Elem()

	k := reflect.New(kt).Elem()
	v := reflect.New(vt).Elem()

	kptr := (*iface)(unsafe.Pointer(&k)).ptr
	vptr := (*iface)(unsafe.Pointer(&v)).ptr
	input := b

	if m.IsNil() {
		m = reflect.MakeMap(t)
	}

	var err error
	b = b[1:]
	for {
		k.Set(kz)
		v.Set(vz)
		b = skipSpaces(b)

		if len(b) != 0 && b[0] == '}' {
			*(*unsafe.Pointer)(p) = unsafe.Pointer(m.Pointer())
			return b[1:], nil
		}

		if i != 0 {
			if len(b) == 0 {
				return b, syntaxError(b, "unexpected end of JSON input after object field value")
			}
			if b[0] != ',' {
				return b, syntaxError(b, "expected ',' after object field value but found '%c'", b[0])
			}
			b = skipSpaces(b[1:])
		}

		if hasNullPrefix(b) {
			return b, syntaxError(b, "cannot decode object key string from 'null' value")
		}

		if b, err = decodeKey(d, b, kptr); err != nil {
			return objectKeyError(b, err)
		}
		b = skipSpaces(b)

		if len(b) == 0 {
			return b, syntaxError(b, "unexpected end of JSON input after object field key")
		}
		if b[0] != ':' {
			return b, syntaxError(b, "expected ':' after object field key but found '%c'", b[0])
		}
		b = skipSpaces(b[1:])

		if b, err = decodeValue(d, b, vptr); err != nil {
			if _, r, _, err := d.parseValue(input); err != nil {
				return r, err
			} else {
				b = r
			}
			if e, ok := err.(*UnmarshalTypeError); ok {
				e.Struct = "map[" + kt.String() + "]" + vt.String() + "{" + e.Struct + "}"
				e.Field = d.prependField(fmt.Sprint(k.Interface()), e.Field)
			}
			return b, err
		}

		m.SetMapIndex(k, v)
		i++
	}
}

func (d decoder) decodeMapStringInterface(b []byte, p unsafe.Pointer) ([]byte, error) {
	if hasNullPrefix(b) {
		*(*unsafe.Pointer)(p) = nil
		return b[4:], nil
	}

	if len(b) < 2 || b[0] != '{' {
		return d.inputError(b, mapStringInterfaceType)
	}

	i := 0
	m := *(*map[string]any)(p)

	if m == nil {
		m = make(map[string]any, 64)
	}

	var (
		input = b
		key   string
		val   any
		err   error
	)

	b = b[1:]
	for {
		key = ""
		val = nil

		b = skipSpaces(b)

		if len(b) != 0 && b[0] == '}' {
			*(*unsafe.Pointer)(p) = *(*unsafe.Pointer)(unsafe.Pointer(&m))
			return b[1:], nil
		}

		if i != 0 {
			if len(b) == 0 {
				return b, syntaxError(b, "unexpected end of JSON input after object field value")
			}
			if b[0] != ',' {
				return b, syntaxError(b, "expected ',' after object field value but found '%c'", b[0])
			}
			b = skipSpaces(b[1:])
		}

		if hasNullPrefix(b) {
			return b, syntaxError(b, "cannot decode object key string from 'null' value")
		}

		b, err = d.decodeString(b, unsafe.Pointer(&key))
		if err != nil {
			return objectKeyError(b, err)
		}
		b = skipSpaces(b)

		if len(b) == 0 {
			return b, syntaxError(b, "unexpected end of JSON input after object field key")
		}
		if b[0] != ':' {
			return b, syntaxError(b, "expected ':' after object field key but found '%c'", b[0])
		}
		b = skipSpaces(b[1:])

		b, err = d.decodeInterface(b, unsafe.Pointer(&val))
		if err != nil {
			if _, r, _, err := d.parseValue(input); err != nil {
				return r, err
			} else {
				b = r
			}
			if e, ok := err.(*UnmarshalTypeError); ok {
				e.Struct = mapStringInterfaceType.String() + e.Struct
				e.Field = d.prependField(key, e.Field)
			}
			return b, err
		}

		m[key] = val
		i++
	}
}

func (d decoder) decodeMapStringRawMessage(b []byte, p unsafe.Pointer) ([]byte, error) {
	if hasNullPrefix(b) {
		*(*unsafe.Pointer)(p) = nil
		return b[4:], nil
	}

	if len(b) < 2 || b[0] != '{' {
		return d.inputError(b, mapStringRawMessageType)
	}

	i := 0
	m := *(*map[string]RawMessage)(p)

	if m == nil {
		m = make(map[string]RawMessage, 64)
	}

	var err error
	var key string
	var val RawMessage
	input := b

	b = b[1:]
	for {
		key = ""
		val = nil

		b = skipSpaces(b)

		if len(b) != 0 && b[0] == '}' {
			*(*unsafe.Pointer)(p) = *(*unsafe.Pointer)(unsafe.Pointer(&m))
			return b[1:], nil
		}

		if i != 0 {
			if len(b) == 0 {
				return b, syntaxError(b, "unexpected end of JSON input after object field value")
			}
			if b[0] != ',' {
				return b, syntaxError(b, "expected ',' after object field value but found '%c'", b[0])
			}
			b = skipSpaces(b[1:])
		}

		if hasNullPrefix(b) {
			return b, syntaxError(b, "cannot decode object key string from 'null' value")
		}

		b, err = d.decodeString(b, unsafe.Pointer(&key))
		if err != nil {
			return objectKeyError(b, err)
		}
		b = skipSpaces(b)

		if len(b) == 0 {
			return b, syntaxError(b, "unexpected end of JSON input after object field key")
		}
		if b[0] != ':' {
			return b, syntaxError(b, "expected ':' after object field key but found '%c'", b[0])
		}
		b = skipSpaces(b[1:])

		b, err = d.decodeRawMessage(b, unsafe.Pointer(&val))
		if err != nil {
			if _, r, _, err := d.parseValue(input); err != nil {
				return r, err
			} else {
				b = r
			}
			if e, ok := err.(*UnmarshalTypeError); ok {
				e.Struct = mapStringRawMessageType.String() + e.Struct
				e.Field = d.prependField(key, e.Field)
			}
			return b, err
		}

		m[key] = val
		i++
	}
}

func (d decoder) decodeMapStringString(b []byte, p unsafe.Pointer) ([]byte, error) {
	if hasNullPrefix(b) {
		*(*unsafe.Pointer)(p) = nil
		return b[4:], nil
	}

	if len(b) < 2 || b[0] != '{' {
		return d.inputError(b, mapStringStringType)
	}

	i := 0
	m := *(*map[string]string)(p)

	if m == nil {
		m = make(map[string]string, 64)
	}

	var err error
	var key string
	var val string
	input := b

	b = b[1:]
	for {
		key = ""
		val = ""

		b = skipSpaces(b)

		if len(b) != 0 && b[0] == '}' {
			*(*unsafe.Pointer)(p) = *(*unsafe.Pointer)(unsafe.Pointer(&m))
			return b[1:], nil
		}

		if i != 0 {
			if len(b) == 0 {
				return b, syntaxError(b, "unexpected end of JSON input after object field value")
			}
			if b[0] != ',' {
				return b, syntaxError(b, "expected ',' after object field value but found '%c'", b[0])
			}
			b = skipSpaces(b[1:])
		}

		if hasNullPrefix(b) {
			return b, syntaxError(b, "cannot decode object key string from 'null' value")
		}

		b, err = d.decodeString(b, unsafe.Pointer(&key))
		if err != nil {
			return objectKeyError(b, err)
		}
		b = skipSpaces(b)

		if len(b) == 0 {
			return b, syntaxError(b, "unexpected end of JSON input after object field key")
		}
		if b[0] != ':' {
			return b, syntaxError(b, "expected ':' after object field key but found '%c'", b[0])
		}
		b = skipSpaces(b[1:])

		b, err = d.decodeString(b, unsafe.Pointer(&val))
		if err != nil {
			if _, r, _, err := d.parseValue(input); err != nil {
				return r, err
			} else {
				b = r
			}
			if e, ok := err.(*UnmarshalTypeError); ok {
				e.Struct = mapStringStringType.String() + e.Struct
				e.Field = d.prependField(key, e.Field)
			}
			return b, err
		}

		m[key] = val
		i++
	}
}

func (d decoder) decodeMapStringStringSlice(b []byte, p unsafe.Pointer) ([]byte, error) {
	if hasNullPrefix(b) {
		*(*unsafe.Pointer)(p) = nil
		return b[4:], nil
	}

	if len(b) < 2 || b[0] != '{' {
		return d.inputError(b, mapStringStringSliceType)
	}

	i := 0
	m := *(*map[string][]string)(p)

	if m == nil {
		m = make(map[string][]string, 64)
	}

	var err error
	var key string
	var buf []string
	input := b
	stringSize := unsafe.Sizeof("")

	b = b[1:]
	for {
		key = ""
		buf = buf[:0]

		b = skipSpaces(b)

		if len(b) != 0 && b[0] == '}' {
			*(*unsafe.Pointer)(p) = *(*unsafe.Pointer)(unsafe.Pointer(&m))
			return b[1:], nil
		}

		if i != 0 {
			if len(b) == 0 {
				return b, syntaxError(b, "unexpected end of JSON input after object field value")
			}
			if b[0] != ',' {
				return b, syntaxError(b, "expected ',' after object field value but found '%c'", b[0])
			}
			b = skipSpaces(b[1:])
		}

		if hasNullPrefix(b) {
			return b, syntaxError(b, "cannot decode object key string from 'null' value")
		}

		b, err = d.decodeString(b, unsafe.Pointer(&key))
		if err != nil {
			return objectKeyError(b, err)
		}
		b = skipSpaces(b)

		if len(b) == 0 {
			return b, syntaxError(b, "unexpected end of JSON input after object field key")
		}
		if b[0] != ':' {
			return b, syntaxError(b, "expected ':' after object field key but found '%c'", b[0])
		}
		b = skipSpaces(b[1:])

		b, err = d.decodeSlice(b, unsafe.Pointer(&buf), stringSize, sliceStringType, decoder.decodeString)
		if err != nil {
			if _, r, _, err := d.parseValue(input); err != nil {
				return r, err
			} else {
				b = r
			}
			if e, ok := err.(*UnmarshalTypeError); ok {
				e.Struct = mapStringStringType.String() + e.Struct
				e.Field = d.prependField(key, e.Field)
			}
			return b, err
		}

		val := make([]string, len(buf))
		copy(val, buf)

		m[key] = val
		i++
	}
}

func (d decoder) decodeMapStringBool(b []byte, p unsafe.Pointer) ([]byte, error) {
	if hasNullPrefix(b) {
		*(*unsafe.Pointer)(p) = nil
		return b[4:], nil
	}

	if len(b) < 2 || b[0] != '{' {
		return d.inputError(b, mapStringBoolType)
	}

	i := 0
	m := *(*map[string]bool)(p)

	if m == nil {
		m = make(map[string]bool, 64)
	}

	var err error
	var key string
	var val bool
	input := b

	b = b[1:]
	for {
		key = ""
		val = false

		b = skipSpaces(b)

		if len(b) != 0 && b[0] == '}' {
			*(*unsafe.Pointer)(p) = *(*unsafe.Pointer)(unsafe.Pointer(&m))
			return b[1:], nil
		}

		if i != 0 {
			if len(b) == 0 {
				return b, syntaxError(b, "unexpected end of JSON input after object field value")
			}
			if b[0] != ',' {
				return b, syntaxError(b, "expected ',' after object field value but found '%c'", b[0])
			}
			b = skipSpaces(b[1:])
		}

		if hasNullPrefix(b) {
			return b, syntaxError(b, "cannot decode object key string from 'null' value")
		}

		b, err = d.decodeString(b, unsafe.Pointer(&key))
		if err != nil {
			return objectKeyError(b, err)
		}
		b = skipSpaces(b)

		if len(b) == 0 {
			return b, syntaxError(b, "unexpected end of JSON input after object field key")
		}
		if b[0] != ':' {
			return b, syntaxError(b, "expected ':' after object field key but found '%c'", b[0])
		}
		b = skipSpaces(b[1:])

		b, err = d.decodeBool(b, unsafe.Pointer(&val))
		if err != nil {
			if _, r, _, err := d.parseValue(input); err != nil {
				return r, err
			} else {
				b = r
			}
			if e, ok := err.(*UnmarshalTypeError); ok {
				e.Struct = mapStringStringType.String() + e.Struct
				e.Field = d.prependField(key, e.Field)
			}
			return b, err
		}

		m[key] = val
		i++
	}
}

func (d decoder) decodeStruct(b []byte, p unsafe.Pointer, st *structType) ([]byte, error) {
	if hasNullPrefix(b) {
		return b[4:], nil
	}

	if len(b) < 2 || b[0] != '{' {
		return d.inputError(b, st.typ)
	}

	var err error
	var k []byte
	var i int

	// memory buffer used to convert short field names to lowercase
	var buf [64]byte
	var key []byte
	input := b

	b = b[1:]
	for {
		b = skipSpaces(b)

		if len(b) != 0 && b[0] == '}' {
			return b[1:], nil
		}

		if i != 0 {
			if len(b) == 0 {
				return b, syntaxError(b, "unexpected end of JSON input after object field value")
			}
			if b[0] != ',' {
				return b, syntaxError(b, "expected ',' after object field value but found '%c'", b[0])
			}
			b = skipSpaces(b[1:])
		}
		i++

		if hasNullPrefix(b) {
			return b, syntaxError(b, "cannot decode object key string from 'null' value")
		}

		k, b, _, err = d.parseStringUnquote(b, nil)
		if err != nil {
			return objectKeyError(b, err)
		}
		b = skipSpaces(b)

		if len(b) == 0 {
			return b, syntaxError(b, "unexpected end of JSON input after object field key")
		}
		if b[0] != ':' {
			return b, syntaxError(b, "expected ':' after object field key but found '%c'", b[0])
		}
		b = skipSpaces(b[1:])

		var f *structField
		if len(st.keyset) != 0 {
			if n := keyset.Lookup(st.keyset, k); n < len(st.fields) {
				if len(st.fields[n].name) == len(k) {
					f = &st.fields[n]
				}
			}
		} else {
			f = st.fieldsIndex[string(k)]
		}

		if f == nil && (d.flags&DontMatchCaseInsensitiveStructFields) == 0 {
			key = appendToLower(buf[:0], k)
			f = st.ficaseIndex[string(key)]
		}

		if f == nil {
			if (d.flags & DisallowUnknownFields) != 0 {
				return b, fmt.Errorf("json: unknown field %q", k)
			}
			if _, b, _, err = d.parseValue(b); err != nil {
				return b, err
			}
			continue
		}

		if b, err = f.codec.decode(d, b, unsafe.Pointer(uintptr(p)+f.offset)); err != nil {
			if _, r, _, err := d.parseValue(input); err != nil {
				return r, err
			} else {
				b = r
			}
			if e, ok := err.(*UnmarshalTypeError); ok {
				e.Struct = st.typ.String() + e.Struct
				e.Field = d.prependField(string(k), e.Field)
			}
			return b, err
		}
	}
}

func (d decoder) decodeEmbeddedStructPointer(b []byte, p unsafe.Pointer, t reflect.Type, unexported bool, offset uintptr, decode decodeFunc) ([]byte, error) {
	v := *(*unsafe.Pointer)(p)

	if v == nil {
		if unexported {
			return nil, fmt.Errorf("json: cannot set embedded pointer to unexported struct: %s", t)
		}
		v = unsafe.Pointer(reflect.New(t).Pointer())
		*(*unsafe.Pointer)(p) = v
	}

	return decode(d, b, unsafe.Pointer(uintptr(v)+offset))
}

func (d decoder) decodePointer(b []byte, p unsafe.Pointer, t reflect.Type, decode decodeFunc) ([]byte, error) {
	if hasNullPrefix(b) {
		pp := *(*unsafe.Pointer)(p)
		if pp != nil && t.Kind() == reflect.Ptr {
			return decode(d, b, pp)
		}
		*(*unsafe.Pointer)(p) = nil
		return b[4:], nil
	}

	v := *(*unsafe.Pointer)(p)
	if v == nil {
		v = unsafe.Pointer(reflect.New(t).Pointer())
		*(*unsafe.Pointer)(p) = v
	}

	return decode(d, b, v)
}

func (d decoder) decodeInterface(b []byte, p unsafe.Pointer) ([]byte, error) {
	val := *(*any)(p)
	*(*any)(p) = nil

	if t := reflect.TypeOf(val); t != nil && t.Kind() == reflect.Ptr {
		if v := reflect.ValueOf(val); v.IsNil() || t.Elem().Kind() != reflect.Ptr {
			// If the destination is nil the only value that is OK to decode is
			// `null`, and the encoding/json package always nils the destination
			// interface value in this case.
			if hasNullPrefix(b) {
				*(*any)(p) = nil
				return b[4:], nil
			}
		}

		b, err := Parse(b, val, d.flags)
		if err == nil {
			*(*any)(p) = val
		}

		return b, err
	}

	v, b, k, err := d.parseValue(b)
	if err != nil {
		return b, err
	}

	switch k.Class() {
	case Object:
		m := make(map[string]interface{})
		v, err = d.decodeMapStringInterface(v, unsafe.Pointer(&m))
		val = m

	case Array:
		a := make([]interface{}, 0, 10)
		v, err = d.decodeSlice(v, unsafe.Pointer(&a), unsafe.Sizeof(a[0]), sliceInterfaceType, decoder.decodeInterface)
		val = a

	case String:
		s := ""
		v, err = d.decodeString(v, unsafe.Pointer(&s))
		val = s

	case Null:
		v, val = nil, nil

	case Bool:
		v, val = nil, k == True

	case Num:
		v, err = d.decodeDynamicNumber(v, unsafe.Pointer(&val))

	default:
		return b, syntaxError(v, "expected token but found '%c'", v[0])
	}

	if err != nil {
		return b, err
	}

	if v = skipSpaces(v); len(v) != 0 {
		return b, syntaxError(v, "unexpected trailing trailing tokens after json value")
	}

	*(*any)(p) = val
	return b, nil
}

func (d decoder) decodeDynamicNumber(b []byte, p unsafe.Pointer) ([]byte, error) {
	kind := Float
	var err error

	// Only pre-parse for numeric kind if a conditional decode
	// has been requested.
	if d.anyFlagsSet(UseBigInt | UseInt64 | UseUint64) {
		_, _, kind, err = d.parseNumber(b)
		if err != nil {
			return b, err
		}
	}

	var rem []byte
	anyPtr := (*any)(p)

	// Mutually exclusive integer handling cases.
	switch {
	// If requested, attempt decode of positive integers as uint64.
	case kind == Uint && d.anyFlagsSet(UseUint64):
		rem, err = decodeInto[uint64](anyPtr, b, d, decoder.decodeUint64)
		if err == nil {
			return rem, err
		}

	// If uint64 decode was not requested but int64 decode was requested,
	// then attempt decode of positive integers as int64.
	case kind == Uint && d.anyFlagsSet(UseInt64):
		fallthrough

	// If int64 decode was requested,
	// attempt decode of negative integers as int64.
	case kind == Int && d.anyFlagsSet(UseInt64):
		rem, err = decodeInto[int64](anyPtr, b, d, decoder.decodeInt64)
		if err == nil {
			return rem, err
		}
	}

	// Fallback numeric handling cases:
	// these cannot be combined into the above switch,
	// since these cases also handle overflow
	// from the above cases, if decode was already attempted.
	switch {
	// If *big.Int decode was requested, handle that case for any integer.
	case kind == Uint && d.anyFlagsSet(UseBigInt):
		fallthrough
	case kind == Int && d.anyFlagsSet(UseBigInt):
		rem, err = decodeInto[*big.Int](anyPtr, b, d, bigIntDecoder)

	// If json.Number decode was requested, handle that for any number.
	case d.anyFlagsSet(UseNumber):
		rem, err = decodeInto[Number](anyPtr, b, d, decoder.decodeNumber)

	// Fall back to float64 decode when no special decoding has been requested.
	default:
		rem, err = decodeInto[float64](anyPtr, b, d, decoder.decodeFloat64)
	}

	return rem, err
}

func (d decoder) decodeMaybeEmptyInterface(b []byte, p unsafe.Pointer, t reflect.Type) ([]byte, error) {
	if hasNullPrefix(b) {
		*(*any)(p) = nil
		return b[4:], nil
	}

	if x := reflect.NewAt(t, p).Elem(); !x.IsNil() {
		if e := x.Elem(); e.Kind() == reflect.Ptr {
			return Parse(b, e.Interface(), d.flags)
		}
	} else if t.NumMethod() == 0 { // empty interface
		return Parse(b, (*any)(p), d.flags)
	}

	return d.decodeUnmarshalTypeError(b, p, t)
}

func (d decoder) decodeUnmarshalTypeError(b []byte, _ unsafe.Pointer, t reflect.Type) ([]byte, error) {
	v, b, _, err := d.parseValue(b)
	if err != nil {
		return b, err
	}
	return b, &UnmarshalTypeError{
		Value: string(v),
		Type:  t,
	}
}

func (d decoder) decodeRawMessage(b []byte, p unsafe.Pointer) ([]byte, error) {
	v, r, _, err := d.parseValue(b)
	if err != nil {
		return d.inputError(b, rawMessageType)
	}

	if (d.flags & DontCopyRawMessage) == 0 {
		v = append(make([]byte, 0, len(v)), v...)
	}

	*(*RawMessage)(p) = json.RawMessage(v)
	return r, err
}

func (d decoder) decodeJSONUnmarshaler(b []byte, p unsafe.Pointer, t reflect.Type, pointer bool) ([]byte, error) {
	v, b, _, err := d.parseValue(b)
	if err != nil {
		return b, err
	}

	u := reflect.NewAt(t, p)
	if !pointer {
		u = u.Elem()
		t = t.Elem()
	}
	if u.IsNil() {
		u.Set(reflect.New(t))
	}

	return b, u.Interface().(Unmarshaler).UnmarshalJSON(v)
}

func (d decoder) decodeTextUnmarshaler(b []byte, p unsafe.Pointer, t reflect.Type, pointer bool) ([]byte, error) {
	var value string

	v, b, k, err := d.parseValue(b)
	if err != nil {
		return b, err
	}
	if len(v) == 0 {
		return d.inputError(v, t)
	}

	switch k.Class() {
	case Null:
		return b, err

	case String:
		s, _, _, err := d.parseStringUnquote(v, nil)
		if err != nil {
			return b, err
		}
		u := reflect.NewAt(t, p)
		if !pointer {
			u = u.Elem()
			t = t.Elem()
		}
		if u.IsNil() {
			u.Set(reflect.New(t))
		}
		return b, u.Interface().(encoding.TextUnmarshaler).UnmarshalText(s)

	case Bool:
		if k == True {
			value = "true"
		} else {
			value = "false"
		}

	case Num:
		value = "number"

	case Object:
		value = "object"

	case Array:
		value = "array"
	}

	return b, &UnmarshalTypeError{Value: value, Type: reflect.PointerTo(t)}
}

func (d decoder) prependField(key, field string) string {
	if field != "" {
		return key + "." + field
	}
	return key
}

func (d decoder) inputError(b []byte, t reflect.Type) ([]byte, error) {
	if len(b) == 0 {
		return nil, unexpectedEOF(b)
	}
	_, r, _, err := d.parseValue(b)
	if err != nil {
		return r, err
	}
	return skipSpaces(r), unmarshalTypeError(b, t)
}

func decodeInto[T any](dest *any, b []byte, d decoder, fn decodeFunc) ([]byte, error) {
	var v T
	rem, err := fn(d, b, unsafe.Pointer(&v))
	if err == nil {
		*dest = v
	}

	return rem, err
}
```

## File: `json/encode.go`
```go
package json

import (
	"encoding"
	"fmt"
	"math"
	"reflect"
	"sort"
	"strconv"
	"sync"
	"time"
	"unicode/utf8"
	"unsafe"

	"github.com/segmentio/asm/base64"
)

const hex = "0123456789abcdef"

func (e encoder) encodeNull(b []byte, p unsafe.Pointer) ([]byte, error) {
	return append(b, "null"...), nil
}

func (e encoder) encodeBool(b []byte, p unsafe.Pointer) ([]byte, error) {
	if *(*bool)(p) {
		return append(b, "true"...), nil
	}
	return append(b, "false"...), nil
}

func (e encoder) encodeInt(b []byte, p unsafe.Pointer) ([]byte, error) {
	return appendInt(b, int64(*(*int)(p))), nil
}

func (e encoder) encodeInt8(b []byte, p unsafe.Pointer) ([]byte, error) {
	return appendInt(b, int64(*(*int8)(p))), nil
}

func (e encoder) encodeInt16(b []byte, p unsafe.Pointer) ([]byte, error) {
	return appendInt(b, int64(*(*int16)(p))), nil
}

func (e encoder) encodeInt32(b []byte, p unsafe.Pointer) ([]byte, error) {
	return appendInt(b, int64(*(*int32)(p))), nil
}

func (e encoder) encodeInt64(b []byte, p unsafe.Pointer) ([]byte, error) {
	return appendInt(b, *(*int64)(p)), nil
}

func (e encoder) encodeUint(b []byte, p unsafe.Pointer) ([]byte, error) {
	return appendUint(b, uint64(*(*uint)(p))), nil
}

func (e encoder) encodeUintptr(b []byte, p unsafe.Pointer) ([]byte, error) {
	return appendUint(b, uint64(*(*uintptr)(p))), nil
}

func (e encoder) encodeUint8(b []byte, p unsafe.Pointer) ([]byte, error) {
	return appendUint(b, uint64(*(*uint8)(p))), nil
}

func (e encoder) encodeUint16(b []byte, p unsafe.Pointer) ([]byte, error) {
	return appendUint(b, uint64(*(*uint16)(p))), nil
}

func (e encoder) encodeUint32(b []byte, p unsafe.Pointer) ([]byte, error) {
	return appendUint(b, uint64(*(*uint32)(p))), nil
}

func (e encoder) encodeUint64(b []byte, p unsafe.Pointer) ([]byte, error) {
	return appendUint(b, *(*uint64)(p)), nil
}

func (e encoder) encodeFloat32(b []byte, p unsafe.Pointer) ([]byte, error) {
	return e.encodeFloat(b, float64(*(*float32)(p)), 32)
}

func (e encoder) encodeFloat64(b []byte, p unsafe.Pointer) ([]byte, error) {
	return e.encodeFloat(b, *(*float64)(p), 64)
}

func (e encoder) encodeFloat(b []byte, f float64, bits int) ([]byte, error) {
	switch {
	case math.IsNaN(f):
		return b, &UnsupportedValueError{Value: reflect.ValueOf(f), Str: "NaN"}
	case math.IsInf(f, 0):
		return b, &UnsupportedValueError{Value: reflect.ValueOf(f), Str: "inf"}
	}

	// Convert as if by ES6 number to string conversion.
	// This matches most other JSON generators.
	// See golang.org/issue/6384 and golang.org/issue/14135.
	// Like fmt %g, but the exponent cutoffs are different
	// and exponents themselves are not padded to two digits.
	abs := math.Abs(f)
	fmt := byte('f')
	// Note: Must use float32 comparisons for underlying float32 value to get precise cutoffs right.
	if abs != 0 {
		if bits == 64 && (abs < 1e-6 || abs >= 1e21) || bits == 32 && (float32(abs) < 1e-6 || float32(abs) >= 1e21) {
			fmt = 'e'
		}
	}

	b = strconv.AppendFloat(b, f, fmt, -1, int(bits))

	if fmt == 'e' {
		// clean up e-09 to e-9
		n := len(b)
		if n >= 4 && b[n-4] == 'e' && b[n-3] == '-' && b[n-2] == '0' {
			b[n-2] = b[n-1]
			b = b[:n-1]
		}
	}

	return b, nil
}

func (e encoder) encodeNumber(b []byte, p unsafe.Pointer) ([]byte, error) {
	n := *(*Number)(p)
	if n == "" {
		n = "0"
	}

	d := decoder{}
	_, _, _, err := d.parseNumber(stringToBytes(string(n)))
	if err != nil {
		return b, err
	}

	return append(b, n...), nil
}

func (e encoder) encodeString(b []byte, p unsafe.Pointer) ([]byte, error) {
	s := *(*string)(p)
	if len(s) == 0 {
		return append(b, `""`...), nil
	}
	i := 0
	j := 0
	escapeHTML := (e.flags & EscapeHTML) != 0

	b = append(b, '"')

	if len(s) >= 8 {
		if j = escapeIndex(s, escapeHTML); j < 0 {
			return append(append(b, s...), '"'), nil
		}
	}

	for j < len(s) {
		c := s[j]

		if c >= 0x20 && c <= 0x7f && c != '\\' && c != '"' && (!escapeHTML || (c != '<' && c != '>' && c != '&')) {
			// fast path: most of the time, printable ascii characters are used
			j++
			continue
		}

		switch c {
		case '\\', '"', '\b', '\f', '\n', '\r', '\t':
			b = append(b, s[i:j]...)
			b = append(b, '\\', escapeByteRepr(c))
			i = j + 1
			j = j + 1
			continue

		case '<', '>', '&':
			b = append(b, s[i:j]...)
			b = append(b, `\u00`...)
			b = append(b, hex[c>>4], hex[c&0xF])
			i = j + 1
			j = j + 1
			continue
		}

		// This encodes bytes < 0x20 except for \t, \n and \r.
		if c < 0x20 {
			b = append(b, s[i:j]...)
			b = append(b, `\u00`...)
			b = append(b, hex[c>>4], hex[c&0xF])
			i = j + 1
			j = j + 1
			continue
		}

		r, size := utf8.DecodeRuneInString(s[j:])

		if r == utf8.RuneError && size == 1 {
			b = append(b, s[i:j]...)
			b = append(b, `\ufffd`...)
			i = j + size
			j = j + size
			continue
		}

		switch r {
		case '\u2028', '\u2029':
			// U+2028 is LINE SEPARATOR.
			// U+2029 is PARAGRAPH SEPARATOR.
			// They are both technically valid characters in JSON strings,
			// but don't work in JSONP, which has to be evaluated as JavaScript,
			// and can lead to security holes there. It is valid JSON to
			// escape them, so we do so unconditionally.
			// See http://timelessrepo.com/json-isnt-a-javascript-subset for discussion.
			b = append(b, s[i:j]...)
			b = append(b, `\u202`...)
			b = append(b, hex[r&0xF])
			i = j + size
			j = j + size
			continue
		}

		j += size
	}

	b = append(b, s[i:]...)
	b = append(b, '"')
	return b, nil
}

func (e encoder) encodeToString(b []byte, p unsafe.Pointer, encode encodeFunc) ([]byte, error) {
	i := len(b)

	b, err := encode(e, b, p)
	if err != nil {
		return b, err
	}

	j := len(b)
	s := b[i:]

	if b, err = e.encodeString(b, unsafe.Pointer(&s)); err != nil {
		return b, err
	}

	n := copy(b[i:], b[j:])
	return b[:i+n], nil
}

func (e encoder) encodeBytes(b []byte, p unsafe.Pointer) ([]byte, error) {
	v := *(*[]byte)(p)
	if v == nil {
		return append(b, "null"...), nil
	}

	n := base64.StdEncoding.EncodedLen(len(v)) + 2

	if avail := cap(b) - len(b); avail < n {
		newB := make([]byte, cap(b)+(n-avail))
		copy(newB, b)
		b = newB[:len(b)]
	}

	i := len(b)
	j := len(b) + n

	b = b[:j]
	b[i] = '"'
	base64.StdEncoding.Encode(b[i+1:j-1], v)
	b[j-1] = '"'
	return b, nil
}

func (e encoder) encodeDuration(b []byte, p unsafe.Pointer) ([]byte, error) {
	b = append(b, '"')
	b = appendDuration(b, *(*time.Duration)(p))
	b = append(b, '"')
	return b, nil
}

func (e encoder) encodeTime(b []byte, p unsafe.Pointer) ([]byte, error) {
	t := *(*time.Time)(p)
	b = append(b, '"')
	b = t.AppendFormat(b, time.RFC3339Nano)
	b = append(b, '"')
	return b, nil
}

func (e encoder) encodeArray(b []byte, p unsafe.Pointer, n int, size uintptr, t reflect.Type, encode encodeFunc) ([]byte, error) {
	start := len(b)
	var err error
	b = append(b, '[')

	for i := range n {
		if i != 0 {
			b = append(b, ',')
		}
		if b, err = encode(e, b, unsafe.Pointer(uintptr(p)+(uintptr(i)*size))); err != nil {
			return b[:start], err
		}
	}

	b = append(b, ']')
	return b, nil
}

func (e encoder) encodeSlice(b []byte, p unsafe.Pointer, size uintptr, t reflect.Type, encode encodeFunc) ([]byte, error) {
	s := (*slice)(p)

	if s.data == nil && s.len == 0 && s.cap == 0 {
		return append(b, "null"...), nil
	}

	return e.encodeArray(b, s.data, s.len, size, t, encode)
}

func (e encoder) encodeMap(b []byte, p unsafe.Pointer, t reflect.Type, encodeKey, encodeValue encodeFunc, sortKeys sortFunc) ([]byte, error) {
	m := reflect.NewAt(t, p).Elem()
	if m.IsNil() {
		return append(b, "null"...), nil
	}

	keys := m.MapKeys()
	if sortKeys != nil && (e.flags&SortMapKeys) != 0 {
		sortKeys(keys)
	}

	start := len(b)
	var err error
	b = append(b, '{')

	for i, k := range keys {
		v := m.MapIndex(k)

		if i != 0 {
			b = append(b, ',')
		}

		if b, err = encodeKey(e, b, (*iface)(unsafe.Pointer(&k)).ptr); err != nil {
			return b[:start], err
		}

		b = append(b, ':')

		if b, err = encodeValue(e, b, (*iface)(unsafe.Pointer(&v)).ptr); err != nil {
			return b[:start], err
		}
	}

	b = append(b, '}')
	return b, nil
}

type element struct {
	key string
	val any
	raw RawMessage
}

type mapslice struct {
	elements []element
}

func (m *mapslice) Len() int           { return len(m.elements) }
func (m *mapslice) Less(i, j int) bool { return m.elements[i].key < m.elements[j].key }
func (m *mapslice) Swap(i, j int)      { m.elements[i], m.elements[j] = m.elements[j], m.elements[i] }

var mapslicePool = sync.Pool{
	New: func() any { return new(mapslice) },
}

func (e encoder) encodeMapStringInterface(b []byte, p unsafe.Pointer) ([]byte, error) {
	m := *(*map[string]any)(p)
	if m == nil {
		return append(b, "null"...), nil
	}

	if (e.flags & SortMapKeys) == 0 {
		// Optimized code path when the program does not need the map keys to be
		// sorted.
		b = append(b, '{')

		if len(m) != 0 {
			var err error
			i := 0

			for k, v := range m {
				if i != 0 {
					b = append(b, ',')
				}

				b, _ = e.encodeString(b, unsafe.Pointer(&k))
				b = append(b, ':')

				b, err = Append(b, v, e.flags)
				if err != nil {
					return b, err
				}

				i++
			}
		}

		b = append(b, '}')
		return b, nil
	}

	s := mapslicePool.Get().(*mapslice)
	if cap(s.elements) < len(m) {
		s.elements = make([]element, 0, align(10, uintptr(len(m))))
	}
	for key, val := range m {
		s.elements = append(s.elements, element{key: key, val: val})
	}
	sort.Sort(s)

	start := len(b)
	var err error
	b = append(b, '{')

	for i, elem := range s.elements {
		if i != 0 {
			b = append(b, ',')
		}

		b, _ = e.encodeString(b, unsafe.Pointer(&elem.key))
		b = append(b, ':')

		b, err = Append(b, elem.val, e.flags)
		if err != nil {
			break
		}
	}

	for i := range s.elements {
		s.elements[i] = element{}
	}

	s.elements = s.elements[:0]
	mapslicePool.Put(s)

	if err != nil {
		return b[:start], err
	}

	b = append(b, '}')
	return b, nil
}

func (e encoder) encodeMapStringRawMessage(b []byte, p unsafe.Pointer) ([]byte, error) {
	m := *(*map[string]RawMessage)(p)
	if m == nil {
		return append(b, "null"...), nil
	}

	if (e.flags & SortMapKeys) == 0 {
		// Optimized code path when the program does not need the map keys to be
		// sorted.
		b = append(b, '{')

		if len(m) != 0 {
			var err error
			i := 0

			for k, v := range m {
				if i != 0 {
					b = append(b, ',')
				}

				// encodeString doesn't return errors so we ignore it here
				b, _ = e.encodeString(b, unsafe.Pointer(&k))
				b = append(b, ':')

				b, err = e.encodeRawMessage(b, unsafe.Pointer(&v))
				if err != nil {
					break
				}

				i++
			}
		}

		b = append(b, '}')
		return b, nil
	}

	s := mapslicePool.Get().(*mapslice)
	if cap(s.elements) < len(m) {
		s.elements = make([]element, 0, align(10, uintptr(len(m))))
	}
	for key, raw := range m {
		s.elements = append(s.elements, element{key: key, raw: raw})
	}
	sort.Sort(s)

	start := len(b)
	var err error
	b = append(b, '{')

	for i, elem := range s.elements {
		if i != 0 {
			b = append(b, ',')
		}

		b, _ = e.encodeString(b, unsafe.Pointer(&elem.key))
		b = append(b, ':')

		b, err = e.encodeRawMessage(b, unsafe.Pointer(&elem.raw))
		if err != nil {
			break
		}
	}

	for i := range s.elements {
		s.elements[i] = element{}
	}

	s.elements = s.elements[:0]
	mapslicePool.Put(s)

	if err != nil {
		return b[:start], err
	}

	b = append(b, '}')
	return b, nil
}

func (e encoder) encodeMapStringString(b []byte, p unsafe.Pointer) ([]byte, error) {
	m := *(*map[string]string)(p)
	if m == nil {
		return append(b, "null"...), nil
	}

	if (e.flags & SortMapKeys) == 0 {
		// Optimized code path when the program does not need the map keys to be
		// sorted.
		b = append(b, '{')

		if len(m) != 0 {
			i := 0

			for k, v := range m {
				if i != 0 {
					b = append(b, ',')
				}

				// encodeString never returns an error so we ignore it here
				b, _ = e.encodeString(b, unsafe.Pointer(&k))
				b = append(b, ':')
				b, _ = e.encodeString(b, unsafe.Pointer(&v))

				i++
			}
		}

		b = append(b, '}')
		return b, nil
	}

	s := mapslicePool.Get().(*mapslice)
	if cap(s.elements) < len(m) {
		s.elements = make([]element, 0, align(10, uintptr(len(m))))
	}
	for key, val := range m {
		v := val
		s.elements = append(s.elements, element{key: key, val: &v})
	}
	sort.Sort(s)

	b = append(b, '{')

	for i, elem := range s.elements {
		if i != 0 {
			b = append(b, ',')
		}

		// encodeString never returns an error so we ignore it here
		b, _ = e.encodeString(b, unsafe.Pointer(&elem.key))
		b = append(b, ':')
		b, _ = e.encodeString(b, unsafe.Pointer(elem.val.(*string)))
	}

	for i := range s.elements {
		s.elements[i] = element{}
	}

	s.elements = s.elements[:0]
	mapslicePool.Put(s)

	b = append(b, '}')
	return b, nil
}

func (e encoder) encodeMapStringStringSlice(b []byte, p unsafe.Pointer) ([]byte, error) {
	m := *(*map[string][]string)(p)
	if m == nil {
		return append(b, "null"...), nil
	}

	stringSize := unsafe.Sizeof("")

	if (e.flags & SortMapKeys) == 0 {
		// Optimized code path when the program does not need the map keys to be
		// sorted.
		b = append(b, '{')

		if len(m) != 0 {
			var err error
			i := 0

			for k, v := range m {
				if i != 0 {
					b = append(b, ',')
				}

				b, _ = e.encodeString(b, unsafe.Pointer(&k))
				b = append(b, ':')

				b, err = e.encodeSlice(b, unsafe.Pointer(&v), stringSize, sliceStringType, encoder.encodeString)
				if err != nil {
					return b, err
				}

				i++
			}
		}

		b = append(b, '}')
		return b, nil
	}

	s := mapslicePool.Get().(*mapslice)
	if cap(s.elements) < len(m) {
		s.elements = make([]element, 0, align(10, uintptr(len(m))))
	}
	for key, val := range m {
		v := val
		s.elements = append(s.elements, element{key: key, val: &v})
	}
	sort.Sort(s)

	start := len(b)
	var err error
	b = append(b, '{')

	for i, elem := range s.elements {
		if i != 0 {
			b = append(b, ',')
		}

		b, _ = e.encodeString(b, unsafe.Pointer(&elem.key))
		b = append(b, ':')

		b, err = e.encodeSlice(b, unsafe.Pointer(elem.val.(*[]string)), stringSize, sliceStringType, encoder.encodeString)
		if err != nil {
			break
		}
	}

	for i := range s.elements {
		s.elements[i] = element{}
	}

	s.elements = s.elements[:0]
	mapslicePool.Put(s)

	if err != nil {
		return b[:start], err
	}

	b = append(b, '}')
	return b, nil
}

func (e encoder) encodeMapStringBool(b []byte, p unsafe.Pointer) ([]byte, error) {
	m := *(*map[string]bool)(p)
	if m == nil {
		return append(b, "null"...), nil
	}

	if (e.flags & SortMapKeys) == 0 {
		// Optimized code path when the program does not need the map keys to be
		// sorted.
		b = append(b, '{')

		if len(m) != 0 {
			i := 0

			for k, v := range m {
				if i != 0 {
					b = append(b, ',')
				}

				// encodeString never returns an error so we ignore it here
				b, _ = e.encodeString(b, unsafe.Pointer(&k))
				if v {
					b = append(b, ":true"...)
				} else {
					b = append(b, ":false"...)
				}

				i++
			}
		}

		b = append(b, '}')
		return b, nil
	}

	s := mapslicePool.Get().(*mapslice)
	if cap(s.elements) < len(m) {
		s.elements = make([]element, 0, align(10, uintptr(len(m))))
	}
	for key, val := range m {
		s.elements = append(s.elements, element{key: key, val: val})
	}
	sort.Sort(s)

	b = append(b, '{')

	for i, elem := range s.elements {
		if i != 0 {
			b = append(b, ',')
		}

		// encodeString never returns an error so we ignore it here
		b, _ = e.encodeString(b, unsafe.Pointer(&elem.key))
		if elem.val.(bool) {
			b = append(b, ":true"...)
		} else {
			b = append(b, ":false"...)
		}
	}

	for i := range s.elements {
		s.elements[i] = element{}
	}

	s.elements = s.elements[:0]
	mapslicePool.Put(s)

	b = append(b, '}')
	return b, nil
}

func (e encoder) encodeStruct(b []byte, p unsafe.Pointer, st *structType) ([]byte, error) {
	start := len(b)
	var err error
	var k string
	var n int
	b = append(b, '{')

	escapeHTML := (e.flags & EscapeHTML) != 0

	for i := range st.fields {
		f := &st.fields[i]
		v := unsafe.Pointer(uintptr(p) + f.offset)

		if f.omitempty && f.empty(v) {
			continue
		}

		if escapeHTML {
			k = f.html
		} else {
			k = f.json
		}

		lengthBeforeKey := len(b)

		if n != 0 {
			b = append(b, k...)
		} else {
			b = append(b, k[1:]...)
		}

		if b, err = f.codec.encode(e, b, v); err != nil {
			if err == (rollback{}) {
				b = b[:lengthBeforeKey]
				continue
			}
			return b[:start], err
		}

		n++
	}

	b = append(b, '}')
	return b, nil
}

type rollback struct{}

func (rollback) Error() string { return "rollback" }

func (e encoder) encodeEmbeddedStructPointer(b []byte, p unsafe.Pointer, t reflect.Type, unexported bool, offset uintptr, encode encodeFunc) ([]byte, error) {
	p = *(*unsafe.Pointer)(p)
	if p == nil {
		return b, rollback{}
	}
	return encode(e, b, unsafe.Pointer(uintptr(p)+offset))
}

func (e encoder) encodePointer(b []byte, p unsafe.Pointer, t reflect.Type, encode encodeFunc) ([]byte, error) {
	if p = *(*unsafe.Pointer)(p); p != nil {
		if e.ptrDepth++; e.ptrDepth >= startDetectingCyclesAfter {
			if _, seen := e.ptrSeen[p]; seen {
				// TODO: reconstruct the reflect.Value from p + t so we can set
				// the erorr's Value field?
				return b, &UnsupportedValueError{Str: fmt.Sprintf("encountered a cycle via %s", t)}
			}
			if e.ptrSeen == nil {
				e.ptrSeen = make(map[unsafe.Pointer]struct{})
			}
			e.ptrSeen[p] = struct{}{}
			defer delete(e.ptrSeen, p)
		}
		return encode(e, b, p)
	}
	return e.encodeNull(b, nil)
}

func (e encoder) encodeInterface(b []byte, p unsafe.Pointer) ([]byte, error) {
	return Append(b, *(*any)(p), e.flags)
}

func (e encoder) encodeMaybeEmptyInterface(b []byte, p unsafe.Pointer, t reflect.Type) ([]byte, error) {
	return Append(b, reflect.NewAt(t, p).Elem().Interface(), e.flags)
}

func (e encoder) encodeUnsupportedTypeError(b []byte, p unsafe.Pointer, t reflect.Type) ([]byte, error) {
	return b, &UnsupportedTypeError{Type: t}
}

func (e encoder) encodeRawMessage(b []byte, p unsafe.Pointer) ([]byte, error) {
	v := *(*RawMessage)(p)

	if v == nil {
		return append(b, "null"...), nil
	}

	var s []byte

	if (e.flags & TrustRawMessage) != 0 {
		s = v
	} else {
		var err error
		v = skipSpaces(v) // don't assume that a RawMessage starts with a token.
		d := decoder{}
		s, _, _, err = d.parseValue(v)
		if err != nil {
			return b, &UnsupportedValueError{Value: reflect.ValueOf(v), Str: err.Error()}
		}
	}

	if (e.flags & EscapeHTML) != 0 {
		return appendCompactEscapeHTML(b, s), nil
	}

	return append(b, s...), nil
}

func (e encoder) encodeJSONMarshaler(b []byte, p unsafe.Pointer, t reflect.Type, pointer bool) ([]byte, error) {
	v := reflect.NewAt(t, p)

	if !pointer {
		v = v.Elem()
	}

	switch v.Kind() {
	case reflect.Ptr, reflect.Interface:
		if v.IsNil() {
			return append(b, "null"...), nil
		}
	}

	j, err := v.Interface().(Marshaler).MarshalJSON()
	if err != nil {
		return b, err
	}

	d := decoder{}
	s, _, _, err := d.parseValue(j)
	if err != nil {
		return b, &MarshalerError{Type: t, Err: err}
	}

	if (e.flags & EscapeHTML) != 0 {
		return appendCompactEscapeHTML(b, s), nil
	}

	return append(b, s...), nil
}

func (e encoder) encodeTextMarshaler(b []byte, p unsafe.Pointer, t reflect.Type, pointer bool) ([]byte, error) {
	v := reflect.NewAt(t, p)

	if !pointer {
		v = v.Elem()
	}

	switch v.Kind() {
	case reflect.Ptr, reflect.Interface:
		if v.IsNil() {
			return append(b, `null`...), nil
		}
	}

	s, err := v.Interface().(encoding.TextMarshaler).MarshalText()
	if err != nil {
		return b, err
	}

	return e.encodeString(b, unsafe.Pointer(&s))
}

func appendCompactEscapeHTML(dst []byte, src []byte) []byte {
	start := 0
	escape := false
	inString := false

	for i, c := range src {
		if !inString {
			switch c {
			case '"': // enter string
				inString = true
			case ' ', '\n', '\r', '\t': // skip space
				if start < i {
					dst = append(dst, src[start:i]...)
				}
				start = i + 1
			}
			continue
		}

		if escape {
			escape = false
			continue
		}

		if c == '\\' {
			escape = true
			continue
		}

		if c == '"' {
			inString = false
			continue
		}

		if c == '<' || c == '>' || c == '&' {
			if start < i {
				dst = append(dst, src[start:i]...)
			}
			dst = append(dst, `\u00`...)
			dst = append(dst, hex[c>>4], hex[c&0xF])
			start = i + 1
			continue
		}

		// Convert U+2028 and U+2029 (E2 80 A8 and E2 80 A9).
		if c == 0xE2 && i+2 < len(src) && src[i+1] == 0x80 && src[i+2]&^1 == 0xA8 {
			if start < i {
				dst = append(dst, src[start:i]...)
			}
			dst = append(dst, `\u202`...)
			dst = append(dst, hex[src[i+2]&0xF])
			start = i + 3
			continue
		}
	}

	if start < len(src) {
		dst = append(dst, src[start:]...)
	}

	return dst
}
```

## File: `json/golang_bench_test.go`
```go
// Copyright 2011 The Go Authors. All rights reserved.
// Use of this source code is governed by a BSD-style
// license that can be found in the LICENSE file.

// Large data benchmark.
// The JSON data is a summary of agl's changes in the
// go, webkit, and chromium open source projects.
// We benchmark converting between the JSON form
// and in-memory data structures.

package json

import (
	"bytes"
	"compress/gzip"
	"fmt"
	"io"
	"os"
	"reflect"
	"runtime"
	"strings"
	"sync"
	"testing"
)

type codeResponse struct {
	Tree     *codeNode `json:"tree"`
	Username string    `json:"username"`
}

type codeNode struct {
	Name     string      `json:"name"`
	Kids     []*codeNode `json:"kids"`
	CLWeight float64     `json:"cl_weight"`
	Touches  int         `json:"touches"`
	MinT     int64       `json:"min_t"`
	MaxT     int64       `json:"max_t"`
	MeanT    int64       `json:"mean_t"`
}

var (
	codeJSON   []byte
	codeStruct codeResponse
)

func codeInit() {
	f, err := os.Open("testdata/code.json.gz")
	if err != nil {
		panic(err)
	}
	defer f.Close()
	gz, err := gzip.NewReader(f)
	if err != nil {
		panic(err)
	}
	data, err := io.ReadAll(gz)
	if err != nil {
		panic(err)
	}

	codeJSON = data

	if err := Unmarshal(codeJSON, &codeStruct); err != nil {
		panic("unmarshal code.json: " + err.Error())
	}

	if data, err = Marshal(&codeStruct); err != nil {
		panic("marshal code.json: " + err.Error())
	}

	if !bytes.Equal(data, codeJSON) {
		println("different lengths", len(data), len(codeJSON))
		for i := range min(len(data), len(codeJSON)) {
			if data[i] != codeJSON[i] {
				println("re-marshal: changed at byte", i)
				println("orig: ", string(codeJSON[i-10:i+10]))
				println("new: ", string(data[i-10:i+10]))
				break
			}
		}
		panic("re-marshal code.json: different result")
	}
}

func BenchmarkCodeEncoder(b *testing.B) {
	b.ReportAllocs()
	if codeJSON == nil {
		b.StopTimer()
		codeInit()
		b.StartTimer()
	}
	b.RunParallel(func(pb *testing.PB) {
		enc := NewEncoder(io.Discard)
		for pb.Next() {
			if err := enc.Encode(&codeStruct); err != nil {
				b.Fatal("Encode:", err)
			}
		}
	})
	b.SetBytes(int64(len(codeJSON)))
}

func BenchmarkCodeMarshal(b *testing.B) {
	b.ReportAllocs()
	if codeJSON == nil {
		b.StopTimer()
		codeInit()
		b.StartTimer()
	}
	b.RunParallel(func(pb *testing.PB) {
		for pb.Next() {
			if _, err := Marshal(&codeStruct); err != nil {
				b.Fatal("Marshal:", err)
			}
		}
	})
	b.SetBytes(int64(len(codeJSON)))
}

func benchMarshalBytes(n int) func(*testing.B) {
	sample := []byte("hello world")
	// Use a struct pointer, to avoid an allocation when passing it as an
	// interface parameter to Marshal.
	v := &struct {
		Bytes []byte
	}{
		bytes.Repeat(sample, (n/len(sample))+1)[:n],
	}
	return func(b *testing.B) {
		for range b.N {
			if _, err := Marshal(v); err != nil {
				b.Fatal("Marshal:", err)
			}
		}
	}
}

func BenchmarkMarshalBytes(b *testing.B) {
	b.ReportAllocs()
	// 32 fits within encodeState.scratch.
	b.Run("32", benchMarshalBytes(32))
	// 256 doesn't fit in encodeState.scratch, but is small enough to
	// allocate and avoid the slower base64.NewEncoder.
	b.Run("256", benchMarshalBytes(256))
	// 4096 is large enough that we want to avoid allocating for it.
	b.Run("4096", benchMarshalBytes(4096))
}

func BenchmarkCodeDecoder(b *testing.B) {
	b.ReportAllocs()
	if codeJSON == nil {
		b.StopTimer()
		codeInit()
		b.StartTimer()
	}
	b.RunParallel(func(pb *testing.PB) {
		var buf bytes.Buffer
		dec := NewDecoder(&buf)
		var r codeResponse
		for pb.Next() {
			buf.Write(codeJSON)
			// hide EOF
			buf.WriteByte('\n')
			buf.WriteByte('\n')
			buf.WriteByte('\n')
			if err := dec.Decode(&r); err != nil {
				b.Fatal("Decode:", err)
			}
		}
	})
	b.SetBytes(int64(len(codeJSON)))
}

func BenchmarkUnicodeDecoder(b *testing.B) {
	b.ReportAllocs()
	j := []byte(`"\uD83D\uDE01"`)
	b.SetBytes(int64(len(j)))
	r := bytes.NewReader(j)
	dec := NewDecoder(r)
	var out string
	b.ResetTimer()
	for range b.N {
		if err := dec.Decode(&out); err != nil {
			b.Fatal("Decode:", err)
		}
		r.Seek(0, 0)
	}
}

func BenchmarkDecoderStream(b *testing.B) {
	b.ReportAllocs()
	b.StopTimer()
	var buf bytes.Buffer
	dec := NewDecoder(&buf)
	buf.WriteString(`"` + strings.Repeat("x", 1000000) + `"` + "\n\n\n")
	var x any
	if err := dec.Decode(&x); err != nil {
		b.Fatal("Decode:", err)
	}
	ones := strings.Repeat(" 1\n", 300000) + "\n\n\n"
	b.StartTimer()
	for i := range b.N {
		// XXX: making use of the index variable
		// is probably a misuse of b.N loops.
		if i%300000 == 0 {
			buf.WriteString(ones)
		}
		x = nil
		if err := dec.Decode(&x); err != nil || x != 1.0 {
			b.Fatalf("Decode: %v after %d", err, i)
		}
	}
}

func BenchmarkCodeUnmarshal(b *testing.B) {
	b.ReportAllocs()
	if codeJSON == nil {
		b.StopTimer()
		codeInit()
		b.StartTimer()
	}
	b.RunParallel(func(pb *testing.PB) {
		for pb.Next() {
			var r codeResponse
			if err := Unmarshal(codeJSON, &r); err != nil {
				b.Fatal("Unmarshal:", err)
			}
		}
	})
	b.SetBytes(int64(len(codeJSON)))
}

func BenchmarkCodeUnmarshalReuse(b *testing.B) {
	b.ReportAllocs()
	if codeJSON == nil {
		b.StopTimer()
		codeInit()
		b.StartTimer()
	}
	b.RunParallel(func(pb *testing.PB) {
		var r codeResponse
		for pb.Next() {
			if err := Unmarshal(codeJSON, &r); err != nil {
				b.Fatal("Unmarshal:", err)
			}
		}
	})
	b.SetBytes(int64(len(codeJSON)))
}

func BenchmarkUnmarshalString(b *testing.B) {
	b.ReportAllocs()
	data := []byte(`"hello, world"`)
	b.RunParallel(func(pb *testing.PB) {
		var s string
		for pb.Next() {
			if err := Unmarshal(data, &s); err != nil {
				b.Fatal("Unmarshal:", err)
			}
		}
	})
}

func BenchmarkUnmarshalObjectMixed(b *testing.B) {
	b.ReportAllocs()
	data := []byte(`{"string":"hello world","time":"2025-07-17T18:40:04.338Z","bool":true,"integer":42,"decimal":3.14,"null":null,"object":{"hello":"world"},"array":[1,2,3]}`)
	b.RunParallel(func(pb *testing.PB) {
		var m map[string]any
		for pb.Next() {
			if err := Unmarshal(data, &m); err != nil {
				b.Fatal("Unmarshal:", err)
			}
		}
	})
}

func BenchmarkUnmarshalArrayMixed(b *testing.B) {
	b.ReportAllocs()
	data := []byte(`["hello world","2025-07-17T18:40:04.338Z",true,42,3.14,null,{"hello":"world"},[1,2,3]]`)
	b.RunParallel(func(pb *testing.PB) {
		var a []any
		for pb.Next() {
			if err := Unmarshal(data, &a); err != nil {
				b.Fatal("Unmarshal:", err)
			}
		}
	})
}

func BenchmarkUnmarshalFloat64(b *testing.B) {
	b.ReportAllocs()
	data := []byte(`3.14`)
	b.RunParallel(func(pb *testing.PB) {
		var f float64
		for pb.Next() {
			if err := Unmarshal(data, &f); err != nil {
				b.Fatal("Unmarshal:", err)
			}
		}
	})
}

func BenchmarkUnmarshalInt64(b *testing.B) {
	b.ReportAllocs()
	data := []byte(`3`)
	b.RunParallel(func(pb *testing.PB) {
		var x int64
		for pb.Next() {
			if err := Unmarshal(data, &x); err != nil {
				b.Fatal("Unmarshal:", err)
			}
		}
	})
}

func BenchmarkIssue10335(b *testing.B) {
	b.ReportAllocs()
	j := []byte(`{"a":{ }}`)
	b.RunParallel(func(pb *testing.PB) {
		var s struct{}
		for pb.Next() {
			if err := Unmarshal(j, &s); err != nil {
				b.Fatal(err)
			}
		}
	})
}

func BenchmarkUnmapped(b *testing.B) {
	b.ReportAllocs()
	j := []byte(`{"s": "hello", "y": 2, "o": {"x": 0}, "a": [1, 99, {"x": 1}]}`)
	b.RunParallel(func(pb *testing.PB) {
		var s struct{}
		for pb.Next() {
			if err := Unmarshal(j, &s); err != nil {
				b.Fatal(err)
			}
		}
	})
}

func BenchmarkTypeFieldsCache(b *testing.B) {
	b.ReportAllocs()
	var maxTypes int = 1e6
	if testenv.Builder() != "" {
		maxTypes = 1e3 // restrict cache sizes on builders
	}

	// Dynamically generate many new types.
	types := make([]reflect.Type, maxTypes)
	fs := []reflect.StructField{{
		Type:  reflect.TypeOf(""),
		Index: []int{0},
	}}
	for i := range types {
		fs[0].Name = fmt.Sprintf("TypeFieldsCache%d", i)
		types[i] = reflect.StructOf(fs)
	}

	// clearClear clears the cache. Other JSON operations, must not be running.
	clearCache := func() {
		fieldCache = sync.Map{}
	}

	// MissTypes tests the performance of repeated cache misses.
	// This measures the time to rebuild a cache of size nt.
	for nt := 1; nt <= maxTypes; nt *= 10 {
		ts := types[:nt]
		b.Run(fmt.Sprintf("MissTypes%d", nt), func(b *testing.B) {
			nc := runtime.GOMAXPROCS(0)
			for range b.N {
				clearCache()
				var wg sync.WaitGroup
				for j := range nc {
					wg.Add(1)
					go func(j int) {
						for _, t := range ts[(j*len(ts))/nc : ((j+1)*len(ts))/nc] {
							cachedTypeFields(t)
						}
						wg.Done()
					}(j)
				}
				wg.Wait()
			}
		})
	}

	// HitTypes tests the performance of repeated cache hits.
	// This measures the average time of each cache lookup.
	for nt := 1; nt <= maxTypes; nt *= 10 {
		// Pre-warm a cache of size nt.
		clearCache()
		for _, t := range types[:nt] {
			cachedTypeFields(t)
		}
		b.Run(fmt.Sprintf("HitTypes%d", nt), func(b *testing.B) {
			b.RunParallel(func(pb *testing.PB) {
				for pb.Next() {
					cachedTypeFields(types[0])
				}
			})
		})
	}
}
```

## File: `json/golang_decode_test.go`
```go
// Copyright 2010 The Go Authors. All rights reserved.
// Use of this source code is governed by a BSD-style
// license that can be found in the LICENSE file.

package json

import (
	"bytes"
	"encoding"
	"errors"
	"fmt"
	"image"
	"math"
	"math/big"
	"net"
	"reflect"
	"strconv"
	"strings"
	"testing"
	"time"
)

type T struct {
	X string
	Y int
	Z int `json:"-"`
}

type U struct {
	Alphabet string `json:"alpha"`
}

type V struct {
	F1 any
	F2 int32
	F3 Number
	F4 *VOuter
}

type VOuter struct {
	V V
}

type W struct {
	S SS
}

type P struct {
	PP PP
}

type PP struct {
	T  T
	Ts []T
}

type SS string

func (*SS) UnmarshalJSON(data []byte) error {
	return &UnmarshalTypeError{Value: "number", Type: reflect.TypeOf(SS(""))}
}

// ifaceNumAsFloat64/ifaceNumAsNumber are used to test unmarshaling with and
// without UseNumber
var ifaceNumAsFloat64 = map[string]any{
	"k1": float64(1),
	"k2": "s",
	"k3": []any{float64(1), float64(2.0), float64(3e-3)},
	"k4": map[string]any{"kk1": "s", "kk2": float64(2)},
}

var ifaceNumAsNumber = map[string]any{
	"k1": Number("1"),
	"k2": "s",
	"k3": []any{Number("1"), Number("2.0"), Number("3e-3")},
	"k4": map[string]any{"kk1": "s", "kk2": Number("2")},
}

type tx struct {
	x int
}

type u8 uint8

// A type that can unmarshal itself.

type unmarshaler struct {
	T bool
}

func (u *unmarshaler) UnmarshalJSON(b []byte) error {
	*u = unmarshaler{true} // All we need to see that UnmarshalJSON is called.
	return nil
}

type ustruct struct {
	M unmarshaler
}

type unmarshalerText struct {
	A, B string
}

// needed for re-marshaling tests
func (u unmarshalerText) MarshalText() ([]byte, error) {
	return []byte(u.A + ":" + u.B), nil
}

func (u *unmarshalerText) UnmarshalText(b []byte) error {
	pos := bytes.IndexByte(b, ':')
	if pos == -1 {
		return errors.New("missing separator")
	}
	u.A, u.B = string(b[:pos]), string(b[pos+1:])
	return nil
}

var _ encoding.TextUnmarshaler = (*unmarshalerText)(nil)

type ustructText struct {
	M unmarshalerText
}

// u8marshal is an integer type that can marshal/unmarshal itself.
type u8marshal uint8

func (u8 u8marshal) MarshalText() ([]byte, error) {
	return []byte(fmt.Sprintf("u%d", u8)), nil
}

var errMissingU8Prefix = errors.New("missing 'u' prefix")

func (u8 *u8marshal) UnmarshalText(b []byte) error {
	if !bytes.HasPrefix(b, []byte{'u'}) {
		return errMissingU8Prefix
	}
	n, err := strconv.Atoi(string(b[1:]))
	if err != nil {
		return err
	}
	*u8 = u8marshal(n)
	return nil
}

var _ encoding.TextUnmarshaler = (*u8marshal)(nil)

var (
	um0, um1 unmarshaler // target2 of unmarshaling
	ump      = &um1
	umtrue   = unmarshaler{true}
	umslice  = []unmarshaler{{true}}
	umslicep = new([]unmarshaler)
	umstruct = ustruct{unmarshaler{true}}

	um0T, um1T   unmarshalerText // target2 of unmarshaling
	umpType      = &um1T
	umtrueXY     = unmarshalerText{"x", "y"}
	umsliceXY    = []unmarshalerText{{"x", "y"}}
	umslicepType = new([]unmarshalerText)
	umstructType = new(ustructText)
	umstructXY   = ustructText{unmarshalerText{"x", "y"}}

	ummapType = map[unmarshalerText]bool{}
	ummapXY   = map[unmarshalerText]bool{{"x", "y"}: true}
)

// Test data structures for anonymous fields.

type Point struct {
	Z int
}

type Top struct {
	Level0 int
	Embed0
	*Embed0a
	*Embed0b `json:"e,omitempty"` // treated as named
	Embed0c  `json:"-"`           // ignored
	Loop
	Embed0p // has Point with X, Y, used
	Embed0q // has Point with Z, used
	embed   // contains exported field
}

type Embed0 struct {
	Level1a int // overridden by Embed0a's Level1a with json tag
	Level1b int // used because Embed0a's Level1b is renamed
	Level1c int // used because Embed0a's Level1c is ignored
	Level1d int // annihilated by Embed0a's Level1d
	Level1e int `json:"x"` // annihilated by Embed0a.Level1e
}

type Embed0a struct {
	Level1a int `json:"Level1a,omitempty"`
	Level1b int `json:"LEVEL1B,omitempty"`
	Level1c int `json:"-"`
	Level1d int // annihilated by Embed0's Level1d
	Level1f int `json:"x"` // annihilated by Embed0's Level1e
}

type Embed0b Embed0

type Embed0c Embed0

type Embed0p struct {
	image.Point
}

type Embed0q struct {
	Point
}

type embed struct {
	Q int
}

type Loop struct {
	Loop1 int `json:",omitempty"`
	Loop2 int `json:",omitempty"`
	*Loop
}

// From reflect test:
// The X in S6 and S7 annihilate, but they also block the X in S8.S9.
type S5 struct {
	S6
	S7
	S8
}

type S6 struct {
	X int
}

type S7 S6

type S8 struct {
	S9
}

type S9 struct {
	X int
	Y int
}

// From reflect test:
// The X in S11.S6 and S12.S6 annihilate, but they also block the X in S13.S8.S9.
type S10 struct {
	S11
	S12
	S13
}

type S11 struct {
	S6
}

type S12 struct {
	S6
}

type S13 struct {
	S8
}

type Ambig struct {
	// Given "hello", the first match should win.
	First  int `json:"HELLO"`
	Second int `json:"Hello"`
}

type XYZ struct {
	X any
	Y any
	Z any
}

type unexportedWithMethods struct{}

func (unexportedWithMethods) F() {}

func sliceAddr(x []int) *[]int                 { return &x }
func mapAddr(x map[string]int) *map[string]int { return &x }

type byteWithMarshalJSON byte

func (b byteWithMarshalJSON) MarshalJSON() ([]byte, error) {
	return []byte(fmt.Sprintf(`"Z%.2x"`, byte(b))), nil
}

func (b *byteWithMarshalJSON) UnmarshalJSON(data []byte) error {
	if len(data) != 5 || data[0] != '"' || data[1] != 'Z' || data[4] != '"' {
		return fmt.Errorf("bad quoted string")
	}
	i, err := strconv.ParseInt(string(data[2:4]), 16, 8)
	if err != nil {
		return fmt.Errorf("bad hex")
	}
	*b = byteWithMarshalJSON(i)
	return nil
}

type byteWithPtrMarshalJSON byte

func (b *byteWithPtrMarshalJSON) MarshalJSON() ([]byte, error) {
	return byteWithMarshalJSON(*b).MarshalJSON()
}

func (b *byteWithPtrMarshalJSON) UnmarshalJSON(data []byte) error {
	return (*byteWithMarshalJSON)(b).UnmarshalJSON(data)
}

type byteWithMarshalText byte

func (b byteWithMarshalText) MarshalText() ([]byte, error) {
	return []byte(fmt.Sprintf(`Z%.2x`, byte(b))), nil
}

func (b *byteWithMarshalText) UnmarshalText(data []byte) error {
	if len(data) != 3 || data[0] != 'Z' {
		return fmt.Errorf("bad quoted string")
	}
	i, err := strconv.ParseInt(string(data[1:3]), 16, 8)
	if err != nil {
		return fmt.Errorf("bad hex")
	}
	*b = byteWithMarshalText(i)
	return nil
}

type byteWithPtrMarshalText byte

func (b *byteWithPtrMarshalText) MarshalText() ([]byte, error) {
	return byteWithMarshalText(*b).MarshalText()
}

func (b *byteWithPtrMarshalText) UnmarshalText(data []byte) error {
	return (*byteWithMarshalText)(b).UnmarshalText(data)
}

type intWithMarshalJSON int

func (b intWithMarshalJSON) MarshalJSON() ([]byte, error) {
	return []byte(fmt.Sprintf(`"Z%.2x"`, int(b))), nil
}

func (b *intWithMarshalJSON) UnmarshalJSON(data []byte) error {
	if len(data) != 5 || data[0] != '"' || data[1] != 'Z' || data[4] != '"' {
		return fmt.Errorf("bad quoted string")
	}
	i, err := strconv.ParseInt(string(data[2:4]), 16, 8)
	if err != nil {
		return fmt.Errorf("bad hex")
	}
	*b = intWithMarshalJSON(i)
	return nil
}

type intWithPtrMarshalJSON int

func (b *intWithPtrMarshalJSON) MarshalJSON() ([]byte, error) {
	return intWithMarshalJSON(*b).MarshalJSON()
}

func (b *intWithPtrMarshalJSON) UnmarshalJSON(data []byte) error {
	return (*intWithMarshalJSON)(b).UnmarshalJSON(data)
}

type intWithMarshalText int

func (b intWithMarshalText) MarshalText() ([]byte, error) {
	return []byte(fmt.Sprintf(`Z%.2x`, int(b))), nil
}

func (b *intWithMarshalText) UnmarshalText(data []byte) error {
	if len(data) != 3 || data[0] != 'Z' {
		return fmt.Errorf("bad quoted string")
	}
	i, err := strconv.ParseInt(string(data[1:3]), 16, 8)
	if err != nil {
		return fmt.Errorf("bad hex")
	}
	*b = intWithMarshalText(i)
	return nil
}

type intWithPtrMarshalText int

func (b *intWithPtrMarshalText) MarshalText() ([]byte, error) {
	return intWithMarshalText(*b).MarshalText()
}

func (b *intWithPtrMarshalText) UnmarshalText(data []byte) error {
	return (*intWithMarshalText)(b).UnmarshalText(data)
}

type mapStringToStringData struct {
	Data map[string]string `json:"data"`
}

type unmarshalTest struct {
	in                    string
	ptr                   any
	out                   any
	err                   error
	useNumber             bool
	golden                bool
	disallowUnknownFields bool
}

type B struct {
	B bool `json:",string"`
}

var unmarshalTests = []unmarshalTest{
	// basic types
	{in: `true`, ptr: new(bool), out: true},
	{in: `1`, ptr: new(int), out: 1},
	{in: `1.2`, ptr: new(float64), out: 1.2},
	{in: `-5`, ptr: new(int16), out: int16(-5)},
	{in: `2`, ptr: new(Number), out: Number("2"), useNumber: true},
	{in: `2`, ptr: new(Number), out: Number("2")},
	{in: `2`, ptr: new(any), out: float64(2.0)},
	{in: `2`, ptr: new(any), out: Number("2"), useNumber: true},
	{in: `"a\u1234"`, ptr: new(string), out: "a\u1234"},
	{in: `"http:\/\/"`, ptr: new(string), out: "http://"},
	{in: `"g-clef: \uD834\uDD1E"`, ptr: new(string), out: "g-clef: \U0001D11E"},
	//TODO
	//{in: `"invalid: \uD834x\uDD1E"`, ptr: new(string), out: "invalid: \uFFFDx\uFFFD"},
	{in: "null", ptr: new(any), out: nil},
	{in: `{"X": [1,2,3], "Y": 4}`, ptr: new(T), out: T{Y: 4}, err: &UnmarshalTypeError{Value: "array", Type: reflect.TypeOf(""), Offset: 7, Struct: "T", Field: "X"}},
	{in: `{"X": 23}`, ptr: new(T), out: T{}, err: &UnmarshalTypeError{Value: "number", Type: reflect.TypeOf(""), Offset: 8, Struct: "T", Field: "X"}},
	{in: `{"x": 1}`, ptr: new(tx), out: tx{}},
	{in: `{"x": 1}`, ptr: new(tx), out: tx{}},
	{in: `{"x": 1}`, ptr: new(tx), err: fmt.Errorf("json: unknown field \"x\""), disallowUnknownFields: true},
	{in: `{"S": 23}`, ptr: new(W), out: W{}, err: &UnmarshalTypeError{Value: "number", Type: reflect.TypeOf(SS("")), Offset: 0, Struct: "W", Field: "S"}},
	{in: `{"F1":1,"F2":2,"F3":3}`, ptr: new(V), out: V{F1: float64(1), F2: int32(2), F3: Number("3")}},
	{in: `{"F1":1,"F2":2,"F3":3}`, ptr: new(V), out: V{F1: Number("1"), F2: int32(2), F3: Number("3")}, useNumber: true},
	{in: `{"k1":1,"k2":"s","k3":[1,2.0,3e-3],"k4":{"kk1":"s","kk2":2}}`, ptr: new(any), out: ifaceNumAsFloat64},
	{in: `{"k1":1,"k2":"s","k3":[1,2.0,3e-3],"k4":{"kk1":"s","kk2":2}}`, ptr: new(any), out: ifaceNumAsNumber, useNumber: true},

	// raw values with whitespace
	{in: "\n true ", ptr: new(bool), out: true},
	{in: "\t 1 ", ptr: new(int), out: 1},
	{in: "\r 1.2 ", ptr: new(float64), out: 1.2},
	{in: "\t -5 \n", ptr: new(int16), out: int16(-5)},
	{in: "\t \"a\\u1234\" \n", ptr: new(string), out: "a\u1234"},

	// Z has a "-" tag.
	{in: `{"Y": 1, "Z": 2}`, ptr: new(T), out: T{Y: 1}},
	{in: `{"Y": 1, "Z": 2}`, ptr: new(T), err: fmt.Errorf("json: unknown field \"Z\""), disallowUnknownFields: true},

	{in: `{"alpha": "abc", "alphabet": "xyz"}`, ptr: new(U), out: U{Alphabet: "abc"}},
	{in: `{"alpha": "abc", "alphabet": "xyz"}`, ptr: new(U), err: fmt.Errorf("json: unknown field \"alphabet\""), disallowUnknownFields: true},
	{in: `{"alpha": "abc"}`, ptr: new(U), out: U{Alphabet: "abc"}},
	{in: `{"alphabet": "xyz"}`, ptr: new(U), out: U{}},
	{in: `{"alphabet": "xyz"}`, ptr: new(U), err: fmt.Errorf("json: unknown field \"alphabet\""), disallowUnknownFields: true},

	// syntax errors
	{in: `{"X": "foo", "Y"}`, err: &testSyntaxError{"invalid character '}' after object key", 17}},
	{in: `[1, 2, 3+]`, err: &testSyntaxError{"invalid character '+' after array element", 9}},
	{in: `{"X":12x}`, err: &testSyntaxError{"invalid character 'x' after object key:value pair", 8}, useNumber: true},
	{in: `[2, 3`, err: &testSyntaxError{msg: "unexpected end of JSON input", Offset: 5}},

	// raw value errors
	{in: "\x01 42", err: &testSyntaxError{"invalid character '\\x01' looking for beginning of value", 1}},
	{in: " 42 \x01", err: &testSyntaxError{"invalid character '\\x01' after top-level value", 5}},
	{in: "\x01 true", err: &testSyntaxError{"invalid character '\\x01' looking for beginning of value", 1}},
	{in: " false \x01", err: &testSyntaxError{"invalid character '\\x01' after top-level value", 8}},
	{in: "\x01 1.2", err: &testSyntaxError{"invalid character '\\x01' looking for beginning of value", 1}},
	{in: " 3.4 \x01", err: &testSyntaxError{"invalid character '\\x01' after top-level value", 6}},
	{in: "\x01 \"string\"", err: &testSyntaxError{"invalid character '\\x01' looking for beginning of value", 1}},
	{in: " \"string\" \x01", err: &testSyntaxError{"invalid character '\\x01' after top-level value", 11}},

	// array tests
	{in: `[1, 2, 3]`, ptr: new([3]int), out: [3]int{1, 2, 3}},
	{in: `[1, 2, 3]`, ptr: new([1]int), out: [1]int{1}},
	{in: `[1, 2, 3]`, ptr: new([5]int), out: [5]int{1, 2, 3, 0, 0}},
	{in: `[1, 2, 3]`, ptr: new(MustNotUnmarshalJSON), err: errors.New("MustNotUnmarshalJSON was used")},

	// empty array to interface test
	{in: `[]`, ptr: new([]any), out: []any{}},
	{in: `null`, ptr: new([]any), out: []any(nil)},
	{in: `{"T":[]}`, ptr: new(map[string]any), out: map[string]any{"T": []any{}}},
	{in: `{"T":null}`, ptr: new(map[string]any), out: map[string]any{"T": any(nil)}},

	// composite tests
	{in: allValueIndent, ptr: new(All), out: allValue},
	{in: allValueCompact, ptr: new(All), out: allValue},
	{in: allValueIndent, ptr: new(*All), out: &allValue},
	{in: allValueCompact, ptr: new(*All), out: &allValue},
	{in: pallValueIndent, ptr: new(All), out: pallValue},
	{in: pallValueCompact, ptr: new(All), out: pallValue},
	{in: pallValueIndent, ptr: new(*All), out: &pallValue},
	{in: pallValueCompact, ptr: new(*All), out: &pallValue},

	// unmarshal interface test
	{in: `{"T":false}`, ptr: &um0, out: umtrue}, // use "false" so test will fail if custom unmarshaler is not called
	{in: `{"T":false}`, ptr: &ump, out: &umtrue},
	{in: `[{"T":false}]`, ptr: &umslice, out: umslice},
	{in: `[{"T":false}]`, ptr: &umslicep, out: &umslice},
	{in: `{"M":{"T":"x:y"}}`, ptr: &umstruct, out: umstruct},

	// UnmarshalText interface test
	{in: `"x:y"`, ptr: &um0T, out: umtrueXY},
	{in: `"x:y"`, ptr: &umpType, out: &umtrueXY},
	{in: `["x:y"]`, ptr: &umsliceXY, out: umsliceXY},
	{in: `["x:y"]`, ptr: &umslicepType, out: &umsliceXY},
	{in: `{"M":"x:y"}`, ptr: umstructType, out: umstructXY},

	// integer-keyed map test
	{
		in:  `{"-1":"a","0":"b","1":"c"}`,
		ptr: new(map[int]string),
		out: map[int]string{-1: "a", 0: "b", 1: "c"},
	},
	{
		in:  `{"0":"a","10":"c","9":"b"}`,
		ptr: new(map[u8]string),
		out: map[u8]string{0: "a", 9: "b", 10: "c"},
	},
	{
		in:  `{"-9223372036854775808":"min","9223372036854775807":"max"}`,
		ptr: new(map[int64]string),
		out: map[int64]string{math.MinInt64: "min", math.MaxInt64: "max"},
	},
	{
		in:  `{"18446744073709551615":"max"}`,
		ptr: new(map[uint64]string),
		out: map[uint64]string{math.MaxUint64: "max"},
	},
	{
		in:  `{"0":false,"10":true}`,
		ptr: new(map[uintptr]bool),
		out: map[uintptr]bool{0: false, 10: true},
	},

	// Check that MarshalText and UnmarshalText take precedence
	// over default integer handling in map keys.
	{
		in:  `{"u2":4}`,
		ptr: new(map[u8marshal]int),
		out: map[u8marshal]int{2: 4},
	},
	{
		in:  `{"2":4}`,
		ptr: new(map[u8marshal]int),
		err: errMissingU8Prefix,
	},

	// integer-keyed map errors
	{
		in:  `{"abc":"abc"}`,
		ptr: new(map[int]string),
		err: &UnmarshalTypeError{Value: "number abc", Type: reflect.TypeOf(0), Offset: 2},
	},
	{
		in:  `{"256":"abc"}`,
		ptr: new(map[uint8]string),
		err: &UnmarshalTypeError{Value: "number 256", Type: reflect.TypeOf(uint8(0)), Offset: 2},
	},
	{
		in:  `{"128":"abc"}`,
		ptr: new(map[int8]string),
		err: &UnmarshalTypeError{Value: "number 128", Type: reflect.TypeOf(int8(0)), Offset: 2},
	},
	{
		in:  `{"-1":"abc"}`,
		ptr: new(map[uint8]string),
		err: &UnmarshalTypeError{Value: "number -1", Type: reflect.TypeOf(uint8(0)), Offset: 2},
	},
	{
		in:  `{"F":{"a":2,"3":4}}`,
		ptr: new(map[string]map[int]int),
		err: &UnmarshalTypeError{Value: "number a", Type: reflect.TypeOf(int(0)), Offset: 7},
	},
	{
		in:  `{"F":{"a":2,"3":4}}`,
		ptr: new(map[string]map[uint]int),
		err: &UnmarshalTypeError{Value: "number a", Type: reflect.TypeOf(uint(0)), Offset: 7},
	},

	// Map keys can be encoding.TextUnmarshalers.
	{in: `{"x:y":true}`, ptr: &ummapType, out: ummapXY},
	// If multiple values for the same key exists, only the most recent value is used.
	{in: `{"x:y":false,"x:y":true}`, ptr: &ummapType, out: ummapXY},

	// Overwriting of data.
	// This is different from package xml, but it's what we've always done.
	// Now documented and tested.
	{in: `[2]`, ptr: sliceAddr([]int{1}), out: []int{2}},
	{in: `{"key": 2}`, ptr: mapAddr(map[string]int{"old": 0, "key": 1}), out: map[string]int{"key": 2}},

	{
		in: `{
			"Level0": 1,
			"Level1b": 2,
			"Level1c": 3,
			"x": 4,
			"Level1a": 5,
			"LEVEL1B": 6,
			"e": {
				"Level1a": 8,
				"Level1b": 9,
				"Level1c": 10,
				"Level1d": 11,
				"x": 12
			},
			"Loop1": 13,
			"Loop2": 14,
			"X": 15,
			"Y": 16,
			"Z": 17,
			"Q": 18
		}`,
		ptr: new(Top),
		out: Top{
			Level0: 1,
			Embed0: Embed0{
				Level1b: 2,
				Level1c: 3,
			},
			Embed0a: &Embed0a{
				Level1a: 5,
				Level1b: 6,
			},
			Embed0b: &Embed0b{
				Level1a: 8,
				Level1b: 9,
				Level1c: 10,
				Level1d: 11,
				Level1e: 12,
			},
			Loop: Loop{
				Loop1: 13,
				Loop2: 14,
			},
			Embed0p: Embed0p{
				Point: image.Point{X: 15, Y: 16},
			},
			Embed0q: Embed0q{
				Point: Point{Z: 17},
			},
			embed: embed{
				Q: 18,
			},
		},
	},
	{
		in:  `{"hello": 1}`,
		ptr: new(Ambig),
		out: Ambig{First: 1},
	},
	{
		in:  `{"X": 1,"Y":2}`,
		ptr: new(S5),
		out: S5{S8: S8{S9: S9{Y: 2}}},
	},
	{
		in:                    `{"X": 1,"Y":2}`,
		ptr:                   new(S5),
		err:                   fmt.Errorf("json: unknown field \"X\""),
		disallowUnknownFields: true,
	},
	{
		in:  `{"X": 1,"Y":2}`,
		ptr: new(S10),
		out: S10{S13: S13{S8: S8{S9: S9{Y: 2}}}},
	},
	{
		in:                    `{"X": 1,"Y":2}`,
		ptr:                   new(S10),
		err:                   fmt.Errorf("json: unknown field \"X\""),
		disallowUnknownFields: true,
	},

	// invalid UTF-8 is coerced to valid UTF-8.
	{
		in:  "\"hello\xffworld\"",
		ptr: new(string),
		out: "hello\ufffdworld",
	},
	{
		in:  "\"hello\xc2\xc2world\"",
		ptr: new(string),
		out: "hello\ufffd\ufffdworld",
	},
	{
		in:  "\"hello\xc2\xffworld\"",
		ptr: new(string),
		out: "hello\ufffd\ufffdworld",
	},
	{
		in:  "\"hello\\ud800world\"",
		ptr: new(string),
		out: "hello\ufffdworld",
	},
	{
		in:  "\"hello\\ud800\\ud800world\"",
		ptr: new(string),
		out: "hello\ufffd\ufffdworld",
	},
	{
		in:  "\"hello\\ud800\\ud800world\"",
		ptr: new(string),
		out: "hello\ufffd\ufffdworld",
	},
	{
		in:  "\"hello\xed\xa0\x80\xed\xb0\x80world\"",
		ptr: new(string),
		out: "hello\ufffd\ufffd\ufffd\ufffd\ufffd\ufffdworld",
	},

	// Used to be issue 8305, but time.Time implements encoding.TextUnmarshaler so this works now.
	{
		in:  `{"2009-11-10T23:00:00Z": "hello world"}`,
		ptr: &map[time.Time]string{},
		out: map[time.Time]string{time.Date(2009, 11, 10, 23, 0, 0, 0, time.UTC): "hello world"},
	},

	// issue 8305
	{
		in:  `{"2009-11-10T23:00:00Z": "hello world"}`,
		ptr: &map[Point]string{},
		err: &UnmarshalTypeError{Value: "object", Type: reflect.TypeOf(map[Point]string{}), Offset: 1},
	},
	{
		in:  `{"asdf": "hello world"}`,
		ptr: &map[unmarshaler]string{},
		err: &UnmarshalTypeError{Value: "object", Type: reflect.TypeOf(map[unmarshaler]string{}), Offset: 1},
	},

	// related to issue 13783.
	// Go 1.7 changed marshaling a slice of typed byte to use the methods on the byte type,
	// similar to marshaling a slice of typed int.
	// These tests check that, assuming the byte type also has valid decoding methods,
	// either the old base64 string encoding or the new per-element encoding can be
	// successfully unmarshaled. The custom unmarshalers were accessible in earlier
	// versions of Go, even though the custom marshaler was not.
	{
		in:  `"AQID"`,
		ptr: new([]byteWithMarshalJSON),
		out: []byteWithMarshalJSON{1, 2, 3},
	},
	{
		in:     `["Z01","Z02","Z03"]`,
		ptr:    new([]byteWithMarshalJSON),
		out:    []byteWithMarshalJSON{1, 2, 3},
		golden: true,
	},
	{
		in:  `"AQID"`,
		ptr: new([]byteWithMarshalText),
		out: []byteWithMarshalText{1, 2, 3},
	},
	{
		in:     `["Z01","Z02","Z03"]`,
		ptr:    new([]byteWithMarshalText),
		out:    []byteWithMarshalText{1, 2, 3},
		golden: true,
	},
	{
		in:  `"AQID"`,
		ptr: new([]byteWithPtrMarshalJSON),
		out: []byteWithPtrMarshalJSON{1, 2, 3},
	},
	{
		in:     `["Z01","Z02","Z03"]`,
		ptr:    new([]byteWithPtrMarshalJSON),
		out:    []byteWithPtrMarshalJSON{1, 2, 3},
		golden: true,
	},
	{
		in:  `"AQID"`,
		ptr: new([]byteWithPtrMarshalText),
		out: []byteWithPtrMarshalText{1, 2, 3},
	},
	{
		in:     `["Z01","Z02","Z03"]`,
		ptr:    new([]byteWithPtrMarshalText),
		out:    []byteWithPtrMarshalText{1, 2, 3},
		golden: true,
	},

	// ints work with the marshaler but not the base64 []byte case
	{
		in:     `["Z01","Z02","Z03"]`,
		ptr:    new([]intWithMarshalJSON),
		out:    []intWithMarshalJSON{1, 2, 3},
		golden: true,
	},
	{
		in:     `["Z01","Z02","Z03"]`,
		ptr:    new([]intWithMarshalText),
		out:    []intWithMarshalText{1, 2, 3},
		golden: true,
	},
	{
		in:     `["Z01","Z02","Z03"]`,
		ptr:    new([]intWithPtrMarshalJSON),
		out:    []intWithPtrMarshalJSON{1, 2, 3},
		golden: true,
	},
	{
		in:     `["Z01","Z02","Z03"]`,
		ptr:    new([]intWithPtrMarshalText),
		out:    []intWithPtrMarshalText{1, 2, 3},
		golden: true,
	},

	{in: `0.000001`, ptr: new(float64), out: 0.000001, golden: true},
	{in: `1e-7`, ptr: new(float64), out: 1e-7, golden: true},
	{in: `100000000000000000000`, ptr: new(float64), out: 100000000000000000000.0, golden: true},
	{in: `1e+21`, ptr: new(float64), out: 1e21, golden: true},
	{in: `-0.000001`, ptr: new(float64), out: -0.000001, golden: true},
	{in: `-1e-7`, ptr: new(float64), out: -1e-7, golden: true},
	{in: `-100000000000000000000`, ptr: new(float64), out: -100000000000000000000.0, golden: true},
	{in: `-1e+21`, ptr: new(float64), out: -1e21, golden: true},
	{in: `999999999999999900000`, ptr: new(float64), out: 999999999999999900000.0, golden: true},
	{in: `9007199254740992`, ptr: new(float64), out: 9007199254740992.0, golden: true},
	{in: `9007199254740993`, ptr: new(float64), out: 9007199254740992.0, golden: false},

	{
		in:  `{"V": {"F2": "hello"}}`,
		ptr: new(VOuter),
		err: &UnmarshalTypeError{
			Value:  "string",
			Struct: "V",
			Field:  "V.F2",
			Type:   reflect.TypeOf(int32(0)),
			Offset: 20,
		},
	},
	{
		in:  `{"V": {"F4": {}, "F2": "hello"}}`,
		ptr: new(VOuter),
		err: &UnmarshalTypeError{
			Value:  "string",
			Struct: "V",
			Field:  "V.F2",
			Type:   reflect.TypeOf(int32(0)),
			Offset: 30,
		},
	},

	// issue 15146.
	// invalid inputs in wrongStringTests below.
	{in: `{"B":"true"}`, ptr: new(B), out: B{true}, golden: true},
	{in: `{"B":"false"}`, ptr: new(B), out: B{false}, golden: true},
	{in: `{"B": "maybe"}`, ptr: new(B), err: errors.New(`json: invalid use of ,string struct tag, trying to unmarshal "maybe" into bool`)},
	{in: `{"B": "tru"}`, ptr: new(B), err: errors.New(`json: invalid use of ,string struct tag, trying to unmarshal "tru" into bool`)},
	{in: `{"B": "False"}`, ptr: new(B), err: errors.New(`json: invalid use of ,string struct tag, trying to unmarshal "False" into bool`)},
	{in: `{"B": "null"}`, ptr: new(B), out: B{false}},
	{in: `{"B": "nul"}`, ptr: new(B), err: errors.New(`json: invalid use of ,string struct tag, trying to unmarshal "nul" into bool`)},
	{in: `{"B": [2, 3]}`, ptr: new(B), err: errors.New(`json: invalid use of ,string struct tag, trying to unmarshal unquoted value into bool`)},

	// additional tests for disallowUnknownFields
	{
		in: `{
			"Level0": 1,
			"Level1b": 2,
			"Level1c": 3,
			"x": 4,
			"Level1a": 5,
			"LEVEL1B": 6,
			"e": {
				"Level1a": 8,
				"Level1b": 9,
				"Level1c": 10,
				"Level1d": 11,
				"x": 12
			},
			"Loop1": 13,
			"Loop2": 14,
			"X": 15,
			"Y": 16,
			"Z": 17,
			"Q": 18,
			"extra": true
		}`,
		ptr:                   new(Top),
		err:                   fmt.Errorf("json: unknown field \"extra\""),
		disallowUnknownFields: true,
	},
	{
		in: `{
			"Level0": 1,
			"Level1b": 2,
			"Level1c": 3,
			"x": 4,
			"Level1a": 5,
			"LEVEL1B": 6,
			"e": {
				"Level1a": 8,
				"Level1b": 9,
				"Level1c": 10,
				"Level1d": 11,
				"x": 12,
				"extra": null
			},
			"Loop1": 13,
			"Loop2": 14,
			"X": 15,
			"Y": 16,
			"Z": 17,
			"Q": 18
		}`,
		ptr:                   new(Top),
		err:                   fmt.Errorf("json: unknown field \"extra\""),
		disallowUnknownFields: true,
	},
	// issue 26444
	// UnmarshalTypeError without field & struct values
	{
		in:  `{"data":{"test1": "bob", "test2": 123}}`,
		ptr: new(mapStringToStringData),
		err: &UnmarshalTypeError{Value: "number", Type: reflect.TypeOf(""), Offset: 37, Struct: "mapStringToStringData", Field: "data"},
	},
	{
		in:  `{"data":{"test1": 123, "test2": "bob"}}`,
		ptr: new(mapStringToStringData),
		err: &UnmarshalTypeError{Value: "number", Type: reflect.TypeOf(""), Offset: 21, Struct: "mapStringToStringData", Field: "data"},
	},

	// trying to decode JSON arrays or objects via TextUnmarshaler
	{
		in:  `[1, 2, 3]`,
		ptr: new(MustNotUnmarshalText),
		err: &UnmarshalTypeError{Value: "array", Type: reflect.TypeOf(&MustNotUnmarshalText{}), Offset: 1},
	},
	{
		in:  `{"foo": "bar"}`,
		ptr: new(MustNotUnmarshalText),
		err: &UnmarshalTypeError{Value: "object", Type: reflect.TypeOf(&MustNotUnmarshalText{}), Offset: 1},
	},
	// #22369
	{
		in:  `{"PP": {"T": {"Y": "bad-type"}}}`,
		ptr: new(P),
		err: &UnmarshalTypeError{
			Value:  "string",
			Struct: "T",
			Field:  "PP.T.Y",
			Type:   reflect.TypeOf(int(0)),
			Offset: 29,
		},
	},
	{
		in:  `{"Ts": [{"Y": 1}, {"Y": 2}, {"Y": "bad-type"}]}`,
		ptr: new(PP),
		err: &UnmarshalTypeError{
			Value:  "string",
			Struct: "T",
			Field:  "Ts.Y",
			Type:   reflect.TypeOf(int(0)),
			Offset: 29,
		},
	},
}

func TestMarshal(t *testing.T) {
	b, err := Marshal(allValue)
	if err != nil {
		t.Fatalf("Marshal allValue: %v", err)
	}
	if string(b) != allValueCompact {
		t.Errorf("Marshal allValueCompact")
		diff(t, b, []byte(allValueCompact))
		return
	}

	b, err = Marshal(pallValue)
	if err != nil {
		t.Fatalf("Marshal pallValue: %v", err)
	}
	if string(b) != pallValueCompact {
		t.Errorf("Marshal pallValueCompact")
		diff(t, b, []byte(pallValueCompact))
		return
	}
}

var badUTF8 = []struct {
	in, out string
}{
	{"hello\xffworld", `"hello\ufffdworld"`},
	{"", `""`},
	{"\xff", `"\ufffd"`},
	{"\xff\xff", `"\ufffd\ufffd"`},
	{"a\xffb", `"a\ufffdb"`},
	{"\xe6\x97\xa5\xe6\x9c\xac\xff\xaa\x9e", `"日本\ufffd\ufffd\ufffd"`},
}

func TestMarshalBadUTF8(t *testing.T) {
	for _, tt := range badUTF8 {
		b, err := Marshal(tt.in)
		if string(b) != tt.out || err != nil {
			t.Errorf("Marshal(%q) = %#q, %v, want %#q, nil", tt.in, b, err, tt.out)
		}
	}
}

func TestMarshalNumberZeroVal(t *testing.T) {
	var n Number
	out, err := Marshal(n)
	if err != nil {
		t.Fatal(err)
	}
	outStr := string(out)
	if outStr != "0" {
		t.Fatalf("Invalid zero val for Number: %q", outStr)
	}
}

func TestMarshalEmbeds(t *testing.T) {
	top := &Top{
		Level0: 1,
		Embed0: Embed0{
			Level1b: 2,
			Level1c: 3,
		},
		Embed0a: &Embed0a{
			Level1a: 5,
			Level1b: 6,
		},
		Embed0b: &Embed0b{
			Level1a: 8,
			Level1b: 9,
			Level1c: 10,
			Level1d: 11,
			Level1e: 12,
		},
		Loop: Loop{
			Loop1: 13,
			Loop2: 14,
		},
		Embed0p: Embed0p{
			Point: image.Point{X: 15, Y: 16},
		},
		Embed0q: Embed0q{
			Point: Point{Z: 17},
		},
		embed: embed{
			Q: 18,
		},
	}
	b, err := Marshal(top)
	if err != nil {
		t.Fatal(err)
	}
	want := "{\"Level0\":1,\"Level1b\":2,\"Level1c\":3,\"Level1a\":5,\"LEVEL1B\":6,\"e\":{\"Level1a\":8,\"Level1b\":9,\"Level1c\":10,\"Level1d\":11,\"x\":12},\"Loop1\":13,\"Loop2\":14,\"X\":15,\"Y\":16,\"Z\":17,\"Q\":18}"
	if string(b) != want {
		t.Errorf("Wrong marshal result.\n got: %q\nwant: %q", b, want)
	}
}

func equalError(a, b error) bool {
	if a == nil {
		return b == nil
	}
	if b == nil {
		return a == nil
	}
	return a.Error() == b.Error()
}

func TestUnmarshal(t *testing.T) {
	for i, tt := range unmarshalTests {
		var scan scanner
		in := []byte(tt.in)
		if err := checkValid(in, &scan); err != nil {
			if !equalError(err, tt.err) {
				t.Errorf("#%d: checkValid: %#v", i, err)
				continue
			}
		}
		if tt.ptr == nil {
			continue
		}

		// v = new(right-type)
		v := reflect.New(reflect.TypeOf(tt.ptr).Elem())
		dec := NewDecoder(bytes.NewReader(in))
		if tt.useNumber {
			dec.UseNumber()
		}
		if tt.disallowUnknownFields {
			dec.DisallowUnknownFields()
		}
		err := dec.Decode(v.Interface())
		assertErrorPresence(t, tt.err, err, "testUnmarshal", i, tt.in)
		if err != nil {
			continue
		}
		if !reflect.DeepEqual(v.Elem().Interface(), tt.out) {
			t.Errorf("#%d: mismatch\n%v\nhave: %#+v\nwant: %#+v", i, tt.in, v.Elem().Interface(), tt.out)
			data, _ := Marshal(v.Elem().Interface())
			println(string(data))
			data, _ = Marshal(tt.out)
			println(string(data))
			continue
		}

		// Check round trip also decodes correctly.
		if tt.err == nil {
			enc, err := Marshal(v.Interface())
			if err != nil {
				t.Errorf("#%d: error re-marshaling: %v", i, err)
				continue
			}
			if tt.golden && !bytes.Equal(enc, in) {
				t.Errorf("#%d: remarshal mismatch:\nhave: %s\nwant: %s", i, enc, in)
			}
			vv := reflect.New(reflect.TypeOf(tt.ptr).Elem())
			dec = NewDecoder(bytes.NewReader(enc))
			if tt.useNumber {
				dec.UseNumber()
			}
			if err := dec.Decode(vv.Interface()); err != nil {
				t.Errorf("#%d: error re-unmarshaling %#q: %v", i, enc, err)
				continue
			}
			if !reflect.DeepEqual(v.Elem().Interface(), vv.Elem().Interface()) {
				t.Errorf("#%d: mismatch\nhave: %#+v\nwant: %#+v", i, v.Elem().Interface(), vv.Elem().Interface())
				t.Errorf("     In: %q", strings.Map(noSpace, string(in)))
				t.Errorf("Marshal: %q", strings.Map(noSpace, string(enc)))
				continue
			}
		}
	}
}

func TestUnmarshalMarshal(t *testing.T) {
	initBig()
	var v any
	if err := Unmarshal(jsonBig, &v); err != nil {
		t.Fatalf("Unmarshal: %v", err)
	}
	b, err := Marshal(v)
	if err != nil {
		t.Fatalf("Marshal: %v", err)
	}
	if !bytes.Equal(jsonBig, b) {
		t.Errorf("Marshal jsonBig")
		diff(t, b, jsonBig)
		return
	}
}

var numberTests = []struct {
	in       string
	i        int64
	intErr   string
	f        float64
	floatErr string
}{
	{in: "-1.23e1", intErr: "strconv.ParseInt: parsing \"-1.23e1\": invalid syntax", f: -1.23e1},
	{in: "-12", i: -12, f: -12.0},
	{in: "1e1000", intErr: "strconv.ParseInt: parsing \"1e1000\": invalid syntax", floatErr: "strconv.ParseFloat: parsing \"1e1000\": value out of range"},
}

// Independent of Decode, basic coverage of the accessors in Number
func TestNumberAccessors(t *testing.T) {
	for _, tt := range numberTests {
		n := Number(tt.in)
		if s := n.String(); s != tt.in {
			t.Errorf("Number(%q).String() is %q", tt.in, s)
		}
		if i, err := n.Int64(); err == nil && tt.intErr == "" && i != tt.i {
			t.Errorf("Number(%q).Int64() is %d", tt.in, i)
		} else if (err == nil && tt.intErr != "") || (err != nil && err.Error() != tt.intErr) {
			t.Errorf("Number(%q).Int64() wanted error %q but got: %v", tt.in, tt.intErr, err)
		}
		if f, err := n.Float64(); err == nil && tt.floatErr == "" && f != tt.f {
			t.Errorf("Number(%q).Float64() is %g", tt.in, f)
		} else if (err == nil && tt.floatErr != "") || (err != nil && err.Error() != tt.floatErr) {
			t.Errorf("Number(%q).Float64() wanted error %q but got: %v", tt.in, tt.floatErr, err)
		}
	}
}

func TestLargeByteSlice(t *testing.T) {
	s0 := make([]byte, 2000)
	for i := range s0 {
		s0[i] = byte(i)
	}
	b, err := Marshal(s0)
	if err != nil {
		t.Fatalf("Marshal: %v", err)
	}
	var s1 []byte
	if err := Unmarshal(b, &s1); err != nil {
		t.Fatalf("Unmarshal: %v", err)
	}
	if !bytes.Equal(s0, s1) {
		t.Errorf("Marshal large byte slice")
		diff(t, s0, s1)
	}
}

type Xint struct {
	X int
}

func TestUnmarshalInterface(t *testing.T) {
	var xint Xint
	var i any = &xint
	if err := Unmarshal([]byte(`{"X":1}`), &i); err != nil {
		t.Fatalf("Unmarshal: %v", err)
	}
	if xint.X != 1 {
		t.Fatalf("Did not write to xint")
	}
}

func TestUnmarshalPtrPtr(t *testing.T) {
	var xint Xint
	pxint := &xint
	if err := Unmarshal([]byte(`{"X":1}`), &pxint); err != nil {
		t.Fatalf("Unmarshal: %v", err)
	}
	if xint.X != 1 {
		t.Fatalf("Did not write to xint")
	}
}

func TestEscape(t *testing.T) {
	const input = `"foobar"<html>` + " [\u2028 \u2029]"
	const expected = `"\"foobar\"\u003chtml\u003e [\u2028 \u2029]"`
	b, err := Marshal(input)
	if err != nil {
		t.Fatalf("Marshal error: %v", err)
	}
	if s := string(b); s != expected {
		t.Errorf("Encoding of [%s]:\n got [%s]\nwant [%s]", input, s, expected)
	}
}

// WrongString is a struct that's misusing the ,string modifier.
type WrongString struct {
	Message string `json:"result,string"`
}

type wrongStringTest struct {
	in, err string
}

var wrongStringTests = []wrongStringTest{
	{`{"result":"x"}`, `json: invalid use of ,string struct tag, trying to unmarshal "x" into string`},
	{`{"result":"foo"}`, `json: invalid use of ,string struct tag, trying to unmarshal "foo" into string`},
	{`{"result":"123"}`, `json: invalid use of ,string struct tag, trying to unmarshal "123" into string`},
	{`{"result":123}`, `json: invalid use of ,string struct tag, trying to unmarshal unquoted value into string`},
	{`{"result":"\""}`, `json: invalid use of ,string struct tag, trying to unmarshal "\"" into string`},
	{`{"result":"\"foo"}`, `json: invalid use of ,string struct tag, trying to unmarshal "\"foo" into string`},
}

// If people misuse the ,string modifier, the error message should be
// helpful, telling the user that they're doing it wrong.
func TestErrorMessageFromMisusedString(t *testing.T) {
	for n, tt := range wrongStringTests {
		r := strings.NewReader(tt.in)
		var s WrongString
		err := NewDecoder(r).Decode(&s)
		assertErrorPresence(t, errors.New(tt.err), err, n)
	}
}

func noSpace(c rune) rune {
	if isSpace(byte(c)) { // only used for ascii
		return -1
	}
	return c
}

type All struct {
	Bool    bool
	Int     int
	Int8    int8
	Int16   int16
	Int32   int32
	Int64   int64
	Uint    uint
	Uint8   uint8
	Uint16  uint16
	Uint32  uint32
	Uint64  uint64
	Uintptr uintptr
	Float32 float32
	Float64 float64

	Foo  string `json:"bar"`
	Foo2 string `json:"bar2,dummyopt"`

	IntStr     int64   `json:",string"`
	UintptrStr uintptr `json:",string"`

	PBool    *bool
	PInt     *int
	PInt8    *int8
	PInt16   *int16
	PInt32   *int32
	PInt64   *int64
	PUint    *uint
	PUint8   *uint8
	PUint16  *uint16
	PUint32  *uint32
	PUint64  *uint64
	PUintptr *uintptr
	PFloat32 *float32
	PFloat64 *float64

	String  string
	PString *string

	Map   map[string]Small
	MapP  map[string]*Small
	PMap  *map[string]Small
	PMapP *map[string]*Small

	EmptyMap map[string]Small
	NilMap   map[string]Small

	Slice   []Small
	SliceP  []*Small
	PSlice  *[]Small
	PSliceP *[]*Small

	EmptySlice []Small
	NilSlice   []Small

	StringSlice []string
	ByteSlice   []byte

	Small   Small
	PSmall  *Small
	PPSmall **Small

	Interface  any
	PInterface *any

	unexported int
}

type Small struct {
	Tag string
}

var allValue = All{
	Bool:       true,
	Int:        2,
	Int8:       3,
	Int16:      4,
	Int32:      5,
	Int64:      6,
	Uint:       7,
	Uint8:      8,
	Uint16:     9,
	Uint32:     10,
	Uint64:     11,
	Uintptr:    12,
	Float32:    14.1,
	Float64:    15.1,
	Foo:        "foo",
	Foo2:       "foo2",
	IntStr:     42,
	UintptrStr: 44,
	String:     "16",
	Map: map[string]Small{
		"17": {Tag: "tag17"},
		"18": {Tag: "tag18"},
	},
	MapP: map[string]*Small{
		"19": {Tag: "tag19"},
		"20": nil,
	},
	EmptyMap:    map[string]Small{},
	Slice:       []Small{{Tag: "tag20"}, {Tag: "tag21"}},
	SliceP:      []*Small{{Tag: "tag22"}, nil, {Tag: "tag23"}},
	EmptySlice:  []Small{},
	StringSlice: []string{"str24", "str25", "str26"},
	ByteSlice:   []byte{27, 28, 29},
	Small:       Small{Tag: "tag30"},
	PSmall:      &Small{Tag: "tag31"},
	Interface:   5.2,
}

var pallValue = All{
	PBool:      &allValue.Bool,
	PInt:       &allValue.Int,
	PInt8:      &allValue.Int8,
	PInt16:     &allValue.Int16,
	PInt32:     &allValue.Int32,
	PInt64:     &allValue.Int64,
	PUint:      &allValue.Uint,
	PUint8:     &allValue.Uint8,
	PUint16:    &allValue.Uint16,
	PUint32:    &allValue.Uint32,
	PUint64:    &allValue.Uint64,
	PUintptr:   &allValue.Uintptr,
	PFloat32:   &allValue.Float32,
	PFloat64:   &allValue.Float64,
	PString:    &allValue.String,
	PMap:       &allValue.Map,
	PMapP:      &allValue.MapP,
	PSlice:     &allValue.Slice,
	PSliceP:    &allValue.SliceP,
	PPSmall:    &allValue.PSmall,
	PInterface: &allValue.Interface,
}

var allValueIndent = `{
	"Bool": true,
	"Int": 2,
	"Int8": 3,
	"Int16": 4,
	"Int32": 5,
	"Int64": 6,
	"Uint": 7,
	"Uint8": 8,
	"Uint16": 9,
	"Uint32": 10,
	"Uint64": 11,
	"Uintptr": 12,
	"Float32": 14.1,
	"Float64": 15.1,
	"bar": "foo",
	"bar2": "foo2",
	"IntStr": "42",
	"UintptrStr": "44",
	"PBool": null,
	"PInt": null,
	"PInt8": null,
	"PInt16": null,
	"PInt32": null,
	"PInt64": null,
	"PUint": null,
	"PUint8": null,
	"PUint16": null,
	"PUint32": null,
	"PUint64": null,
	"PUintptr": null,
	"PFloat32": null,
	"PFloat64": null,
	"String": "16",
	"PString": null,
	"Map": {
		"17": {
			"Tag": "tag17"
		},
		"18": {
			"Tag": "tag18"
		}
	},
	"MapP": {
		"19": {
			"Tag": "tag19"
		},
		"20": null
	},
	"PMap": null,
	"PMapP": null,
	"EmptyMap": {},
	"NilMap": null,
	"Slice": [
		{
			"Tag": "tag20"
		},
		{
			"Tag": "tag21"
		}
	],
	"SliceP": [
		{
			"Tag": "tag22"
		},
		null,
		{
			"Tag": "tag23"
		}
	],
	"PSlice": null,
	"PSliceP": null,
	"EmptySlice": [],
	"NilSlice": null,
	"StringSlice": [
		"str24",
		"str25",
		"str26"
	],
	"ByteSlice": "Gxwd",
	"Small": {
		"Tag": "tag30"
	},
	"PSmall": {
		"Tag": "tag31"
	},
	"PPSmall": null,
	"Interface": 5.2,
	"PInterface": null
}`

var allValueCompact = strings.Map(noSpace, allValueIndent)

var pallValueIndent = `{
	"Bool": false,
	"Int": 0,
	"Int8": 0,
	"Int16": 0,
	"Int32": 0,
	"Int64": 0,
	"Uint": 0,
	"Uint8": 0,
	"Uint16": 0,
	"Uint32": 0,
	"Uint64": 0,
	"Uintptr": 0,
	"Float32": 0,
	"Float64": 0,
	"bar": "",
	"bar2": "",
        "IntStr": "0",
	"UintptrStr": "0",
	"PBool": true,
	"PInt": 2,
	"PInt8": 3,
	"PInt16": 4,
	"PInt32": 5,
	"PInt64": 6,
	"PUint": 7,
	"PUint8": 8,
	"PUint16": 9,
	"PUint32": 10,
	"PUint64": 11,
	"PUintptr": 12,
	"PFloat32": 14.1,
	"PFloat64": 15.1,
	"String": "",
	"PString": "16",
	"Map": null,
	"MapP": null,
	"PMap": {
		"17": {
			"Tag": "tag17"
		},
		"18": {
			"Tag": "tag18"
		}
	},
	"PMapP": {
		"19": {
			"Tag": "tag19"
		},
		"20": null
	},
	"EmptyMap": null,
	"NilMap": null,
	"Slice": null,
	"SliceP": null,
	"PSlice": [
		{
			"Tag": "tag20"
		},
		{
			"Tag": "tag21"
		}
	],
	"PSliceP": [
		{
			"Tag": "tag22"
		},
		null,
		{
			"Tag": "tag23"
		}
	],
	"EmptySlice": null,
	"NilSlice": null,
	"StringSlice": null,
	"ByteSlice": null,
	"Small": {
		"Tag": ""
	},
	"PSmall": null,
	"PPSmall": {
		"Tag": "tag31"
	},
	"Interface": null,
	"PInterface": 5.2
}`

var pallValueCompact = strings.Map(noSpace, pallValueIndent)

func TestRefUnmarshal(t *testing.T) {
	type S struct {
		// Ref is defined in encode_test.go.
		R0 Ref
		R1 *Ref
		R2 RefText
		R3 *RefText
	}
	want := S{
		R0: 12,
		R1: new(Ref),
		R2: 13,
		R3: new(RefText),
	}
	*want.R1 = 12
	*want.R3 = 13

	var got S
	if err := Unmarshal([]byte(`{"R0":"ref","R1":"ref","R2":"ref","R3":"ref"}`), &got); err != nil {
		t.Fatalf("Unmarshal: %v", err)
	}
	if !reflect.DeepEqual(got, want) {
		t.Errorf("got %+v, want %+v", got, want)
	}
}

// Test that the empty string doesn't panic decoding when ,string is specified
// Issue 3450
func TestEmptyString(t *testing.T) {
	type T2 struct {
		Number1 int `json:",string"`
		Number2 int `json:",string"`
	}
	data := `{"Number1":"1", "Number2":""}`
	dec := NewDecoder(strings.NewReader(data))
	var t2 T2
	err := dec.Decode(&t2)
	if err == nil {
		t.Fatal("Decode: did not return error")
	}
	if t2.Number1 != 1 {
		t.Fatal("Decode: did not set Number1")
	}
}

// Test that a null for ,string is not replaced with the previous quoted string (issue 7046).
// It should also not be an error (issue 2540, issue 8587).
func TestNullString(t *testing.T) {
	type T struct {
		A int  `json:",string"`
		B int  `json:",string"`
		C *int `json:",string"`
	}
	data := []byte(`{"A": "1", "B": null, "C": null}`)
	var s T
	s.B = 1
	s.C = new(int)
	*s.C = 2
	err := Unmarshal(data, &s)
	if err != nil {
		t.Fatalf("Unmarshal: %v", err)
	}
	if s.B != 1 || s.C != nil {
		t.Fatalf("after Unmarshal, s.B=%d, s.C=%p, want 1, nil", s.B, s.C)
	}
}

func intp(x int) *int {
	p := new(int)
	*p = x
	return p
}

func intpp(x *int) **int {
	pp := new(*int)
	*pp = x
	return pp
}

var interfaceSetTests = []struct {
	pre  any
	json string
	post any
}{
	{"foo", `"bar"`, "bar"},
	{"foo", `2`, 2.0},
	{"foo", `true`, true},
	{"foo", `null`, nil},

	{nil, `null`, nil},
	{new(int), `null`, nil},
	{(*int)(nil), `null`, nil},
	{new(*int), `null`, new(*int)},
	{(**int)(nil), `null`, nil},
	{intp(1), `null`, nil},
	{intpp(nil), `null`, intpp(nil)},
	{intpp(intp(1)), `null`, intpp(nil)},
}

func TestInterfaceSet(t *testing.T) {
	for _, tt := range interfaceSetTests {
		b := struct{ X any }{tt.pre}
		blob := `{"X":` + tt.json + `}`
		if err := Unmarshal([]byte(blob), &b); err != nil {
			t.Errorf("Unmarshal %#q: %v", blob, err)
			continue
		}
		if !reflect.DeepEqual(b.X, tt.post) {
			t.Errorf("Unmarshal %#q into %#v: X=%#v, want %#v", blob, tt.pre, b.X, tt.post)
		}
	}
}

type NullTest struct {
	Bool      bool
	Int       int
	Int8      int8
	Int16     int16
	Int32     int32
	Int64     int64
	Uint      uint
	Uint8     uint8
	Uint16    uint16
	Uint32    uint32
	Uint64    uint64
	Float32   float32
	Float64   float64
	String    string
	PBool     *bool
	Map       map[string]string
	Slice     []string
	Interface any

	PRaw    *RawMessage
	PTime   *time.Time
	PBigInt *big.Int
	PText   *MustNotUnmarshalText
	PBuffer *bytes.Buffer // has methods, just not relevant ones
	PStruct *struct{}

	Raw    RawMessage
	Time   time.Time
	BigInt big.Int
	Text   MustNotUnmarshalText
	Buffer bytes.Buffer
	Struct struct{}
}

type NullTestStrings struct {
	Bool      bool              `json:",string"`
	Int       int               `json:",string"`
	Int8      int8              `json:",string"`
	Int16     int16             `json:",string"`
	Int32     int32             `json:",string"`
	Int64     int64             `json:",string"`
	Uint      uint              `json:",string"`
	Uint8     uint8             `json:",string"`
	Uint16    uint16            `json:",string"`
	Uint32    uint32            `json:",string"`
	Uint64    uint64            `json:",string"`
	Float32   float32           `json:",string"`
	Float64   float64           `json:",string"`
	String    string            `json:",string"`
	PBool     *bool             `json:",string"`
	Map       map[string]string `json:",string"`
	Slice     []string          `json:",string"`
	Interface any               `json:",string"`

	PRaw    *RawMessage           `json:",string"`
	PTime   *time.Time            `json:",string"`
	PBigInt *big.Int              `json:",string"`
	PText   *MustNotUnmarshalText `json:",string"`
	PBuffer *bytes.Buffer         `json:",string"`
	PStruct *struct{}             `json:",string"`

	Raw    RawMessage           `json:",string"`
	Time   time.Time            `json:",string"`
	BigInt big.Int              `json:",string"`
	Text   MustNotUnmarshalText `json:",string"`
	Buffer bytes.Buffer         `json:",string"`
	Struct struct{}             `json:",string"`
}

// JSON null values should be ignored for primitives and string values instead of resulting in an error.
// Issue 2540
func TestUnmarshalNulls(t *testing.T) {
	// Unmarshal docs:
	// The JSON null value unmarshals into an interface, map, pointer, or slice
	// by setting that Go value to nil. Because null is often used in JSON to mean
	// ``not present,'' unmarshaling a JSON null into any other Go type has no effect
	// on the value and produces no error.

	jsonData := []byte(`{
				"Bool"    : null,
				"Int"     : null,
				"Int8"    : null,
				"Int16"   : null,
				"Int32"   : null,
				"Int64"   : null,
				"Uint"    : null,
				"Uint8"   : null,
				"Uint16"  : null,
				"Uint32"  : null,
				"Uint64"  : null,
				"Float32" : null,
				"Float64" : null,
				"String"  : null,
				"PBool": null,
				"Map": null,
				"Slice": null,
				"Interface": null,
				"PRaw": null,
				"PTime": null,
				"PBigInt": null,
				"PText": null,
				"PBuffer": null,
				"PStruct": null,
				"Raw": null,
				"Time": null,
				"BigInt": null,
				"Text": null,
				"Buffer": null,
				"Struct": null
			}`)
	nulls := NullTest{
		Bool:      true,
		Int:       2,
		Int8:      3,
		Int16:     4,
		Int32:     5,
		Int64:     6,
		Uint:      7,
		Uint8:     8,
		Uint16:    9,
		Uint32:    10,
		Uint64:    11,
		Float32:   12.1,
		Float64:   13.1,
		String:    "14",
		PBool:     new(bool),
		Map:       map[string]string{},
		Slice:     []string{},
		Interface: new(MustNotUnmarshalJSON),
		PRaw:      new(RawMessage),
		PTime:     new(time.Time),
		PBigInt:   new(big.Int),
		PText:     new(MustNotUnmarshalText),
		PStruct:   new(struct{}),
		PBuffer:   new(bytes.Buffer),
		Raw:       RawMessage("123"),
		Time:      time.Unix(123456789, 0),
		BigInt:    *big.NewInt(123),
	}

	before := nulls.Time.String()

	err := Unmarshal(jsonData, &nulls)
	if err != nil {
		t.Errorf("Unmarshal of null values failed: %v", err)
	}
	if !nulls.Bool || nulls.Int != 2 || nulls.Int8 != 3 || nulls.Int16 != 4 || nulls.Int32 != 5 || nulls.Int64 != 6 ||
		nulls.Uint != 7 || nulls.Uint8 != 8 || nulls.Uint16 != 9 || nulls.Uint32 != 10 || nulls.Uint64 != 11 ||
		nulls.Float32 != 12.1 || nulls.Float64 != 13.1 || nulls.String != "14" {
		t.Errorf("Unmarshal of null values affected primitives")
	}

	if nulls.PBool != nil {
		t.Errorf("Unmarshal of null did not clear nulls.PBool")
	}
	if nulls.Map != nil {
		t.Errorf("Unmarshal of null did not clear nulls.Map")
	}
	if nulls.Slice != nil {
		t.Errorf("Unmarshal of null did not clear nulls.Slice")
	}
	if nulls.Interface != nil {
		t.Errorf("Unmarshal of null did not clear nulls.Interface")
	}
	if nulls.PRaw != nil {
		t.Errorf("Unmarshal of null did not clear nulls.PRaw")
	}
	if nulls.PTime != nil {
		t.Errorf("Unmarshal of null did not clear nulls.PTime")
	}
	if nulls.PBigInt != nil {
		t.Errorf("Unmarshal of null did not clear nulls.PBigInt")
	}
	if nulls.PText != nil {
		t.Errorf("Unmarshal of null did not clear nulls.PText")
	}
	if nulls.PBuffer != nil {
		t.Errorf("Unmarshal of null did not clear nulls.PBuffer")
	}
	if nulls.PStruct != nil {
		t.Errorf("Unmarshal of null did not clear nulls.PStruct")
	}

	if string(nulls.Raw) != "null" {
		t.Errorf("Unmarshal of RawMessage null did not record null: %v", string(nulls.Raw))
	}
	if nulls.Time.String() != before {
		t.Errorf("Unmarshal of time.Time null set time to %v", nulls.Time.String())
	}
	if nulls.BigInt.String() != "123" {
		t.Errorf("Unmarshal of big.Int null set int to %v", nulls.BigInt.String())
	}
}

type MustNotUnmarshalJSON struct{}

func (x MustNotUnmarshalJSON) UnmarshalJSON(data []byte) error {
	return errors.New("MustNotUnmarshalJSON was used")
}

type MustNotUnmarshalText struct{}

func (x MustNotUnmarshalText) UnmarshalText(text []byte) error {
	return errors.New("MustNotUnmarshalText was used")
}

func TestStringKind(t *testing.T) {
	type stringKind string

	var m1, m2 map[stringKind]int
	m1 = map[stringKind]int{
		"foo": 42,
	}

	data, err := Marshal(m1)
	if err != nil {
		t.Errorf("Unexpected error marshaling: %v", err)
	}

	err = Unmarshal(data, &m2)
	if err != nil {
		t.Errorf("Unexpected error unmarshaling: %v", err)
	}

	if !reflect.DeepEqual(m1, m2) {
		t.Error("Items should be equal after encoding and then decoding")
	}
}

// Custom types with []byte as underlying type could not be marshaled
// and then unmarshaled.
// Issue 8962.
func TestByteKind(t *testing.T) {
	type byteKind []byte

	a := byteKind("hello")

	data, err := Marshal(a)
	if err != nil {
		t.Error(err)
	}
	var b byteKind
	err = Unmarshal(data, &b)
	if err != nil {
		t.Fatal(err)
	}
	if !reflect.DeepEqual(a, b) {
		t.Errorf("expected %v == %v", a, b)
	}
}

// The fix for issue 8962 introduced a regression.
// Issue 12921.
func TestSliceOfCustomByte(t *testing.T) {
	type Uint8 uint8

	a := []Uint8("hello")

	data, err := Marshal(a)
	if err != nil {
		t.Fatal(err)
	}
	var b []Uint8
	err = Unmarshal(data, &b)
	if err != nil {
		t.Fatal(err)
	}
	if !reflect.DeepEqual(a, b) {
		t.Fatalf("expected %v == %v", a, b)
	}
}

var decodeTypeErrorTests = []struct {
	dest any
	src  string
}{
	{new(string), `{"user": "name"}`}, // issue 4628.
	{new(error), `{}`},                // issue 4222
	{new(error), `[]`},
	{new(error), `""`},
	{new(error), `123`},
	{new(error), `true`},
}

func TestUnmarshalTypeError(t *testing.T) {
	for _, item := range decodeTypeErrorTests {
		err := Unmarshal([]byte(item.src), item.dest)
		if _, ok := err.(*UnmarshalTypeError); !ok {
			t.Errorf("expected type error for Unmarshal(%q, type %T): got %T",
				item.src, item.dest, err)
		}
	}
}

var unmarshalSyntaxTests = []string{
	"tru",
	"fals",
	"nul",
	"123e",
	`"hello`,
	`[1,2,3`,
	`{"key":1`,
	`{"key":1,`,
}

func TestUnmarshalSyntax(t *testing.T) {
	var x any
	for _, src := range unmarshalSyntaxTests {
		err := Unmarshal([]byte(src), &x)
		if _, ok := err.(*SyntaxError); !ok {
			t.Errorf("expected syntax error for Unmarshal(%q): got %T", src, err)
		}
	}
}

// Test handling of unexported fields that should be ignored.
// Issue 4660
type unexportedFields struct {
	Name string
	m    map[string]any `json:"-"`
	m2   map[string]any `json:"abcd"`

	s []int `json:"-"`
}

func TestUnmarshalUnexported(t *testing.T) {
	input := `{"Name": "Bob", "m": {"x": 123}, "m2": {"y": 456}, "abcd": {"z": 789}, "s": [2, 3]}`
	want := &unexportedFields{Name: "Bob"}

	out := &unexportedFields{}
	err := Unmarshal([]byte(input), out)
	if err != nil {
		t.Errorf("got error %v, expected nil", err)
	}
	if !reflect.DeepEqual(out, want) {
		t.Errorf("got %q, want %q", out, want)
	}
}

// Time3339 is a time.Time which encodes to and from JSON
// as an RFC 3339 time in UTC.
type Time3339 time.Time

func (t *Time3339) UnmarshalJSON(b []byte) error {
	if len(b) < 2 || b[0] != '"' || b[len(b)-1] != '"' {
		return fmt.Errorf("types: failed to unmarshal non-string value %q as an RFC 3339 time", b)
	}
	tm, err := time.Parse(time.RFC3339, string(b[1:len(b)-1]))
	if err != nil {
		return err
	}
	*t = Time3339(tm)
	return nil
}

func TestUnmarshalJSONLiteralError(t *testing.T) {
	var t3 Time3339
	err := Unmarshal([]byte(`"0000-00-00T00:00:00Z"`), &t3)
	if err == nil {
		t.Fatalf("expected error; got time %v", time.Time(t3))
	}
	if !strings.Contains(err.Error(), "range") {
		t.Errorf("got err = %v; want out of range error", err)
	}
}

// Test that extra object elements in an array do not result in a
// "data changing underfoot" error.
// Issue 3717
func TestSkipArrayObjects(t *testing.T) {
	json := `[{}]`
	var dest [0]any

	err := Unmarshal([]byte(json), &dest)
	if err != nil {
		t.Errorf("got error %q, want nil", err)
	}
}

// Test semantics of pre-filled struct fields and pre-filled map fields.
// Issue 4900.
func TestPrefilled(t *testing.T) {
	ptrToMap := func(m map[string]any) *map[string]any { return &m }

	// Values here change, cannot reuse table across runs.
	prefillTests := []struct {
		in  string
		ptr any
		out any
	}{
		{
			in:  `{"X": 1, "Y": 2}`,
			ptr: &XYZ{X: float32(3), Y: int16(4), Z: 1.5},
			out: &XYZ{X: float64(1), Y: float64(2), Z: 1.5},
		},
		{
			in:  `{"X": 1, "Y": 2}`,
			ptr: ptrToMap(map[string]any{"X": float32(3), "Y": int16(4), "Z": 1.5}),
			out: ptrToMap(map[string]any{"X": float64(1), "Y": float64(2), "Z": 1.5}),
		},
	}

	for _, tt := range prefillTests {
		ptrstr := fmt.Sprintf("%v", tt.ptr)
		err := Unmarshal([]byte(tt.in), tt.ptr) // tt.ptr edited here
		if err != nil {
			t.Errorf("Unmarshal: %v", err)
		}
		if !reflect.DeepEqual(tt.ptr, tt.out) {
			t.Errorf("Unmarshal(%#q, %s): have %v, want %v", tt.in, ptrstr, tt.ptr, tt.out)
		}
	}
}

var invalidUnmarshalTests = []struct {
	v    any
	want string
}{
	{nil, "json: Unmarshal(nil)"},
	{struct{}{}, "json: Unmarshal(non-pointer struct {})"},
	{(*int)(nil), "json: Unmarshal(nil *int)"},
}

func TestInvalidUnmarshal(t *testing.T) {
	buf := []byte(`{"a":"1"}`)
	for _, tt := range invalidUnmarshalTests {
		err := Unmarshal(buf, tt.v)
		if err == nil {
			t.Errorf("Unmarshal expecting error, got nil")
			continue
		}
		if got := err.Error(); got != tt.want {
			t.Errorf("Unmarshal = %q; want %q", got, tt.want)
		}
	}
}

var invalidUnmarshalTextTests = []struct {
	v    any
	want string
}{
	{nil, "json: Unmarshal(nil)"},
	{struct{}{}, "json: Unmarshal(non-pointer struct {})"},
	{(*int)(nil), "json: Unmarshal(nil *int)"},
	{new(net.IP), "json: cannot unmarshal number into Go value of type *net.IP"},
}

func TestInvalidUnmarshalText(t *testing.T) {
	buf := []byte(`123`)
	for _, tt := range invalidUnmarshalTextTests {
		err := Unmarshal(buf, tt.v)
		if err == nil {
			t.Errorf("Unmarshal expecting error, got nil")
			continue
		}
		if got := err.Error(); got != tt.want {
			t.Errorf("Unmarshal = %q; want %q", got, tt.want)
		}
	}
}

// Test that string option is ignored for invalid types.
// Issue 9812.
func TestInvalidStringOption(t *testing.T) {
	num := 0
	item := struct {
		T time.Time         `json:",string"`
		M map[string]string `json:",string"`
		S []string          `json:",string"`
		A [1]string         `json:",string"`
		I any               `json:",string"`
		P *int              `json:",string"`
	}{M: make(map[string]string), S: make([]string, 0), I: num, P: &num}

	data, err := Marshal(item)
	if err != nil {
		t.Fatalf("Marshal: %v", err)
	}

	err = Unmarshal(data, &item)
	if err != nil {
		t.Fatalf("Unmarshal: %v", err)
	}
}

// Test unmarshal behavior with regards to embedded unexported structs.
//
// (Issue 21357) If the embedded struct is a pointer and is unallocated,
// this returns an error because unmarshal cannot set the field.
//
// (Issue 24152) If the embedded struct is given an explicit name,
// ensure that the normal unmarshal logic does not panic in reflect.
//
// (Issue 28145) If the embedded struct is given an explicit name and has
// exported methods, don't cause a panic trying to get its value.
func TestUnmarshalEmbeddedUnexported(t *testing.T) {
	type (
		embed1 struct{ Q int }
		embed2 struct{ Q int }
		embed3 struct {
			Q int64 `json:",string"`
		}
		S1 struct {
			*embed1
			R int
		}
		S2 struct {
			*embed1
			Q int
		}
		S3 struct {
			embed1
			R int
		}
		S4 struct {
			*embed1
			embed2
		}
		S5 struct {
			*embed3
			R int
		}
		S6 struct {
			embed1 `json:"embed1"`
		}
		S7 struct {
			embed1 `json:"embed1"`
			embed2
		}
		S8 struct {
			embed1 `json:"embed1"`
			embed2 `json:"embed2"`
			Q      int
		}
		S9 struct {
			unexportedWithMethods `json:"embed"`
		}
	)

	tests := []struct {
		in  string
		ptr any
		out any
		err error
	}{{
		// Error since we cannot set S1.embed1, but still able to set S1.R.
		in:  `{"R":2,"Q":1}`,
		ptr: new(S1),
		out: &S1{R: 2},
		err: fmt.Errorf("json: cannot set embedded pointer to unexported struct: json.embed1"),
	}, {
		// The top level Q field takes precedence.
		in:  `{"Q":1}`,
		ptr: new(S2),
		out: &S2{Q: 1},
	}, {
		// No issue with non-pointer variant.
		in:  `{"R":2,"Q":1}`,
		ptr: new(S3),
		out: &S3{embed1: embed1{Q: 1}, R: 2},
	}, {
		// No error since both embedded structs have field R, which annihilate each other.
		// Thus, no attempt is made at setting S4.embed1.
		in:  `{"R":2}`,
		ptr: new(S4),
		out: new(S4),
	}, {
		// Error since we cannot set S5.embed1, but still able to set S5.R.
		in:  `{"R":2,"Q":1}`,
		ptr: new(S5),
		out: &S5{R: 2},
		err: fmt.Errorf("json: cannot set embedded pointer to unexported struct: json.embed3"),
	}, {
		// Issue 24152, ensure decodeState.indirect does not panic.
		in:  `{"embed1": {"Q": 1}}`,
		ptr: new(S6),
		out: &S6{embed1{1}},
	}, {
		// Issue 24153, check that we can still set forwarded fields even in
		// the presence of a name conflict.
		//
		// This relies on obscure behavior of reflect where it is possible
		// to set a forwarded exported field on an unexported embedded struct
		// even though there is a name conflict, even when it would have been
		// impossible to do so according to Go visibility rules.
		// Go forbids this because it is ambiguous whether S7.Q refers to
		// S7.embed1.Q or S7.embed2.Q. Since embed1 and embed2 are unexported,
		// it should be impossible for an external package to set either Q.
		//
		// It is probably okay for a future reflect change to break this.
		in:  `{"embed1": {"Q": 1}, "Q": 2}`,
		ptr: new(S7),
		out: &S7{embed1{1}, embed2{2}},
	}, {
		// Issue 24153, similar to the S7 case.
		in:  `{"embed1": {"Q": 1}, "embed2": {"Q": 2}, "Q": 3}`,
		ptr: new(S8),
		out: &S8{embed1{1}, embed2{2}, 3},
	}, {
		// Issue 228145, similar to the cases above.
		in:  `{"embed": {}}`,
		ptr: new(S9),
		out: &S9{},
	}}

	for i, tt := range tests {
		err := Unmarshal([]byte(tt.in), tt.ptr)
		if !equalError(err, tt.err) {
			t.Errorf("#%d: %v, want %v", i, err, tt.err)
		}
		if !reflect.DeepEqual(tt.ptr, tt.out) {
			t.Errorf("#%d: mismatch\ngot:  %#+v\nwant: %#+v", i, tt.ptr, tt.out)
		}
	}
}

type unmarshalPanic struct{}

func (unmarshalPanic) UnmarshalJSON([]byte) error { panic(0xdead) }

func TestUnmarshalPanic(t *testing.T) {
	defer func() {
		if got := recover(); !reflect.DeepEqual(got, 0xdead) {
			t.Errorf("panic() = (%T)(%v), want 0xdead", got, got)
		}
	}()
	Unmarshal([]byte("{}"), &unmarshalPanic{})
	t.Fatalf("Unmarshal should have panicked")
}

// The decoder used to hang if decoding into an interface pointing to its own address.
// See golang.org/issues/31740.
func TestUnmarshalRecursivePointer(t *testing.T) {
	var v any
	v = &v
	data := []byte(`{"a": "b"}`)

	if err := Unmarshal(data, v); err != nil {
		t.Fatal(err)
	}
}
```

## File: `json/golang_encode_test.go`
```go
// Copyright 2011 The Go Authors. All rights reserved.
// Use of this source code is governed by a BSD-style
// license that can be found in the LICENSE file.

package json

import (
	"bytes"
	"fmt"
	"log"
	"math"
	"reflect"
	"regexp"
	"strconv"
	"testing"
	"unicode"
)

type Optionals struct {
	Sr string `json:"sr"`
	So string `json:"so,omitempty"`
	Sw string `json:"-"`

	Ir int `json:"omitempty"` // actually named omitempty, not an option
	Io int `json:"io,omitempty"`

	Slr []string `json:"slr,random"`
	Slo []string `json:"slo,omitempty"`

	Mr map[string]any `json:"mr"`
	Mo map[string]any `json:",omitempty"`

	Fr float64 `json:"fr"`
	Fo float64 `json:"fo,omitempty"`

	Br bool `json:"br"`
	Bo bool `json:"bo,omitempty"`

	Ur uint `json:"ur"`
	Uo uint `json:"uo,omitempty"`

	Str struct{} `json:"str"`
	Sto struct{} `json:"sto,omitempty"`
}

var optionalsExpected = `{
 "sr": "",
 "omitempty": 0,
 "slr": null,
 "mr": {},
 "fr": 0,
 "br": false,
 "ur": 0,
 "str": {},
 "sto": {}
}`

func TestOmitEmpty(t *testing.T) {
	var o Optionals
	o.Sw = "something"
	o.Mr = map[string]any{}
	o.Mo = map[string]any{}

	got, err := MarshalIndent(&o, "", " ")
	if err != nil {
		t.Fatal(err)
	}
	if got := string(got); got != optionalsExpected {
		t.Errorf(" got: %s\nwant: %s\n", got, optionalsExpected)
	}
}

type StringTag struct {
	BoolStr    bool    `json:",string"`
	IntStr     int64   `json:",string"`
	UintptrStr uintptr `json:",string"`
	StrStr     string  `json:",string"`
}

var stringTagExpected = `{
 "BoolStr": "true",
 "IntStr": "42",
 "UintptrStr": "44",
 "StrStr": "\"xzbit\""
}`

func TestStringTag(t *testing.T) {
	var s StringTag
	s.BoolStr = true
	s.IntStr = 42
	s.UintptrStr = 44
	s.StrStr = "xzbit"
	got, err := MarshalIndent(&s, "", " ")
	if err != nil {
		t.Fatal(err)
	}
	if got := string(got); got != stringTagExpected {
		t.Fatalf(" got: %s\nwant: %s\n", got, stringTagExpected)
	}

	// Verify that it round-trips.
	var s2 StringTag
	err = NewDecoder(bytes.NewReader(got)).Decode(&s2)
	if err != nil {
		t.Fatalf("Decode: %v", err)
	}
	if !reflect.DeepEqual(s, s2) {
		t.Fatalf("decode didn't match.\nsource: %#v\nEncoded as:\n%s\ndecode: %#v", s, string(got), s2)
	}
}

// byte slices are special even if they're renamed types.
type (
	renamedByte             byte
	renamedByteSlice        []byte
	renamedRenamedByteSlice []renamedByte
)

func TestEncodeRenamedByteSlice(t *testing.T) {
	s := renamedByteSlice("abc")
	result, err := Marshal(s)
	if err != nil {
		t.Fatal(err)
	}
	expect := `"YWJj"`
	if string(result) != expect {
		t.Errorf(" got %s want %s", result, expect)
	}
	r := renamedRenamedByteSlice("abc")
	result, err = Marshal(r)
	if err != nil {
		t.Fatal(err)
	}
	if string(result) != expect {
		t.Errorf(" got %s want %s", result, expect)
	}
}

var unsupportedValues = []any{
	math.NaN(),
	math.Inf(-1),
	math.Inf(1),
}

func TestUnsupportedValues(t *testing.T) {
	for _, v := range unsupportedValues {
		if _, err := Marshal(v); err != nil {
			if _, ok := err.(*UnsupportedValueError); !ok {
				t.Errorf("for %v, got %T want UnsupportedValueError", v, err)
			}
		} else {
			t.Errorf("for %v, expected error", v)
		}
	}
}

// Ref has Marshaler and Unmarshaler methods with pointer receiver.
type Ref int

func (*Ref) MarshalJSON() ([]byte, error) {
	return []byte(`"ref"`), nil
}

func (r *Ref) UnmarshalJSON([]byte) error {
	*r = 12
	return nil
}

// Val has Marshaler methods with value receiver.
type Val int

func (Val) MarshalJSON() ([]byte, error) {
	return []byte(`"val"`), nil
}

// RefText has Marshaler and Unmarshaler methods with pointer receiver.
type RefText int

func (*RefText) MarshalText() ([]byte, error) {
	return []byte(`"ref"`), nil
}

func (r *RefText) UnmarshalText([]byte) error {
	*r = 13
	return nil
}

// ValText has Marshaler methods with value receiver.
type ValText int

func (ValText) MarshalText() ([]byte, error) {
	return []byte(`"val"`), nil
}

func TestRefValMarshal(t *testing.T) {
	s := struct {
		R0 Ref
		R1 *Ref
		R2 RefText
		R3 *RefText
		V0 Val
		V1 *Val
		V2 ValText
		V3 *ValText
	}{
		R0: 12,
		R1: new(Ref),
		R2: 14,
		R3: new(RefText),
		V0: 13,
		V1: new(Val),
		V2: 15,
		V3: new(ValText),
	}
	const want = `{"R0":"ref","R1":"ref","R2":"\"ref\"","R3":"\"ref\"","V0":"val","V1":"val","V2":"\"val\"","V3":"\"val\""}`
	b, err := Marshal(&s)
	if err != nil {
		t.Fatalf("Marshal: %v", err)
	}
	if got := string(b); got != want {
		t.Errorf("got %q, want %q", got, want)
	}
}

// C implements Marshaler and returns unescaped JSON.
type C int

func (C) MarshalJSON() ([]byte, error) {
	return []byte(`"<&>"`), nil
}

// CText implements Marshaler and returns unescaped text.
type CText int

func (CText) MarshalText() ([]byte, error) {
	return []byte(`"<&>"`), nil
}

func TestMarshalerEscaping(t *testing.T) {
	var c C
	want := `"\u003c\u0026\u003e"`
	b, err := Marshal(c)
	if err != nil {
		t.Fatalf("Marshal(c): %v", err)
	}
	if got := string(b); got != want {
		t.Errorf("Marshal(c) = %#q, want %#q", got, want)
	}

	var ct CText
	want = `"\"\u003c\u0026\u003e\""`
	b, err = Marshal(ct)
	if err != nil {
		t.Fatalf("Marshal(ct): %v", err)
	}
	if got := string(b); got != want {
		t.Errorf("Marshal(ct) = %#q, want %#q", got, want)
	}
}

func TestAnonymousFields(t *testing.T) {
	tests := []struct {
		label     string     // Test name
		makeInput func() any // Function to create input value
		want      string     // Expected JSON output
	}{
		{
			// Both S1 and S2 have a field named X. From the perspective of S,
			// it is ambiguous which one X refers to.
			// This should not serialize either field.
			label: "AmbiguousField",
			makeInput: func() any {
				type (
					S1 struct{ x, X int }
					S2 struct{ x, X int }
					S  struct {
						S1
						S2
					}
				)
				return S{S1{1, 2}, S2{3, 4}}
			},
			want: `{}`,
		},
		{
			label: "DominantField",
			// Both S1 and S2 have a field named X, but since S has an X field as
			// well, it takes precedence over S1.X and S2.X.
			makeInput: func() any {
				type (
					S1 struct{ x, X int }
					S2 struct{ x, X int }
					S  struct {
						S1
						S2
						x, X int
					}
				)
				return S{S1{1, 2}, S2{3, 4}, 5, 6}
			},
			want: `{"X":6}`,
		},
		{
			// Unexported embedded field of non-struct type should not be serialized.
			label: "UnexportedEmbeddedInt",
			makeInput: func() any {
				type (
					myInt int
					S     struct{ myInt }
				)
				return S{5}
			},
			want: `{}`,
		},
		{
			// Exported embedded field of non-struct type should be serialized.
			label: "ExportedEmbeddedInt",
			makeInput: func() any {
				type (
					MyInt int
					S     struct{ MyInt }
				)
				return S{5}
			},
			want: `{"MyInt":5}`,
		},
		{
			// Unexported embedded field of pointer to non-struct type
			// should not be serialized.
			label: "UnexportedEmbeddedIntPointer",
			makeInput: func() any {
				type (
					myInt int
					S     struct{ *myInt }
				)
				s := S{new(myInt)}
				*s.myInt = 5
				return s
			},
			want: `{}`,
		},
		{
			// Exported embedded field of pointer to non-struct type
			// should be serialized.
			label: "ExportedEmbeddedIntPointer",
			makeInput: func() any {
				type (
					MyInt int
					S     struct{ *MyInt }
				)
				s := S{new(MyInt)}
				*s.MyInt = 5
				return s
			},
			want: `{"MyInt":5}`,
		},
		{
			// Exported fields of embedded structs should have their
			// exported fields be serialized regardless of whether the struct types
			// themselves are exported.
			label: "EmbeddedStruct",
			makeInput: func() any {
				type (
					s1 struct{ x, X int }
					S2 struct{ y, Y int }
					S  struct {
						s1
						S2
					}
				)
				return S{s1{1, 2}, S2{3, 4}}
			},
			want: `{"X":2,"Y":4}`,
		},
		{
			// Exported fields of pointers to embedded structs should have their
			// exported fields be serialized regardless of whether the struct types
			// themselves are exported.
			label: "EmbeddedStructPointer",
			makeInput: func() any {
				type (
					s1 struct{ x, X int }
					S2 struct{ y, Y int }
					S  struct {
						*s1
						*S2
					}
				)
				return S{&s1{1, 2}, &S2{3, 4}}
			},
			want: `{"X":2,"Y":4}`,
		},
		{
			// Exported fields on embedded unexported structs at multiple levels
			// of nesting should still be serialized.
			label: "NestedStructAndInts",
			makeInput: func() any {
				type (
					MyInt1 int
					MyInt2 int
					myInt  int
					s2     struct {
						MyInt2
						myInt
					}
					s1 struct {
						MyInt1
						myInt
						s2
					}
					S struct {
						s1
						myInt
					}
				)
				return S{s1{1, 2, s2{3, 4}}, 6}
			},
			want: `{"MyInt1":1,"MyInt2":3}`,
		},
		{
			// If an anonymous struct pointer field is nil, we should ignore
			// the embedded fields behind it. Not properly doing so may
			// result in the wrong output or reflect panics.
			label: "EmbeddedFieldBehindNilPointer",
			makeInput: func() any {
				type (
					S2 struct{ Field string }
					S  struct{ *S2 }
				)
				return S{}
			},
			want: `{}`,
		},
	}

	for _, tt := range tests {
		t.Run(tt.label, func(t *testing.T) {
			b, err := Marshal(tt.makeInput())
			if err != nil {
				t.Fatalf("Marshal() = %v, want nil error", err)
			}
			if string(b) != tt.want {
				t.Fatalf("Marshal() = %q, want %q", b, tt.want)
			}
		})
	}
}

type BugA struct {
	S string
}

type BugB struct {
	BugA
	S string
}

type BugC struct {
	S string
}

// Legal Go: We never use the repeated embedded field (S).
type BugX struct {
	A int
	BugA
	BugB
}

// Issue 16042. Even if a nil interface value is passed in
// as long as it implements MarshalJSON, it should be marshaled.
type nilMarshaler string

func (nm *nilMarshaler) MarshalJSON() ([]byte, error) {
	if nm == nil {
		return Marshal("0zenil0")
	}
	return Marshal("zenil:" + string(*nm))
}

// Issue 16042.
func TestNilMarshal(t *testing.T) {
	testCases := []struct {
		v    any
		want string
	}{
		{v: nil, want: `null`},
		{v: new(float64), want: `0`},
		{v: []any(nil), want: `null`},
		{v: []string(nil), want: `null`},
		{v: map[string]string(nil), want: `null`},
		{v: []byte(nil), want: `null`},
		{v: struct{ M string }{"gopher"}, want: `{"M":"gopher"}`},
		{v: struct{ M Marshaler }{}, want: `{"M":null}`},
		{v: struct{ M Marshaler }{(*nilMarshaler)(nil)}, want: `{"M":"0zenil0"}`},
		{v: struct{ M any }{(*nilMarshaler)(nil)}, want: `{"M":null}`},
	}

	for _, tt := range testCases {
		out, err := Marshal(tt.v)
		if err != nil || string(out) != tt.want {
			t.Errorf("Marshal(%#v) = %#q, %#v, want %#q, nil", tt.v, out, err, tt.want)
			continue
		}
	}
}

// Issue 5245.
func TestEmbeddedBug(t *testing.T) {
	v := BugB{
		BugA{"A"},
		"B",
	}
	b, err := Marshal(v)
	if err != nil {
		t.Fatal("Marshal:", err)
	}
	want := `{"S":"B"}`
	got := string(b)
	if got != want {
		t.Fatalf("Marshal: got %s want %s", got, want)
	}
	// Now check that the duplicate field, S, does not appear.
	x := BugX{
		A: 23,
	}
	b, err = Marshal(x)
	if err != nil {
		t.Fatal("Marshal:", err)
	}
	want = `{"A":23}`
	got = string(b)
	if got != want {
		t.Fatalf("Marshal: got %s want %s", got, want)
	}
}

type BugD struct { // Same as BugA after tagging.
	XXX string `json:"S"`
}

// BugD's tagged S field should dominate BugA's.
type BugY struct {
	BugA
	BugD
}

// Test that a field with a tag dominates untagged fields.
func TestTaggedFieldDominates(t *testing.T) {
	v := BugY{
		BugA{"BugA"},
		BugD{"BugD"},
	}
	b, err := Marshal(v)
	if err != nil {
		t.Fatal("Marshal:", err)
	}
	want := `{"S":"BugD"}`
	got := string(b)
	if got != want {
		t.Fatalf("Marshal: got %s want %s", got, want)
	}
}

// There are no tags here, so S should not appear.
type BugZ struct {
	BugA
	BugC
	BugY // Contains a tagged S field through BugD; should not dominate.
}

func TestDuplicatedFieldDisappears(t *testing.T) {
	v := BugZ{
		BugA{"BugA"},
		BugC{"BugC"},
		BugY{
			BugA{"nested BugA"},
			BugD{"nested BugD"},
		},
	}
	b, err := Marshal(v)
	if err != nil {
		t.Fatal("Marshal:", err)
	}
	want := `{}`
	got := string(b)
	if got != want {
		t.Fatalf("Marshal: got %s want %s", got, want)
	}
}

func TestStringBytes(t *testing.T) {
	t.Parallel()
	// Test that encodeState.stringBytes and encodeState.string use the same encoding.
	var r []rune
	for i := '\u0000'; i <= unicode.MaxRune; i++ {
		if testing.Short() && i > 1000 {
			i = unicode.MaxRune
		}
		r = append(r, i)
	}
	s := string(r) + "\xff\xff\xffhello" // some invalid UTF-8 too

	for _, escapeHTML := range []bool{true, false} {
		es := &encodeState{}
		es.string(s, escapeHTML)

		esBytes := &encodeState{}
		esBytes.stringBytes([]byte(s), escapeHTML)

		enc := es.Buffer.String()
		encBytes := esBytes.Buffer.String()
		if enc != encBytes {
			i := 0
			for i < len(enc) && i < len(encBytes) && enc[i] == encBytes[i] {
				i++
			}
			enc = enc[i:]
			encBytes = encBytes[i:]
			i = 0
			for i < len(enc) && i < len(encBytes) && enc[len(enc)-i-1] == encBytes[len(encBytes)-i-1] {
				i++
			}
			enc = enc[:len(enc)-i]
			encBytes = encBytes[:len(encBytes)-i]

			if len(enc) > 20 {
				enc = enc[:20] + "..."
			}
			if len(encBytes) > 20 {
				encBytes = encBytes[:20] + "..."
			}

			t.Errorf("with escapeHTML=%t, encodings differ at %#q vs %#q",
				escapeHTML, enc, encBytes)
		}
	}
}

func TestIssue10281(t *testing.T) {
	type Foo struct {
		N Number
	}
	x := Foo{Number(`invalid`)}

	b, err := Marshal(&x)
	if err == nil {
		t.Errorf("Marshal(&x) = %#q; want error", b)
	}
}

func TestHTMLEscape(t *testing.T) {
	var b, want bytes.Buffer
	m := `{"M":"<html>foo &` + "\xe2\x80\xa8 \xe2\x80\xa9" + `</html>"}`
	want.Write([]byte(`{"M":"\u003chtml\u003efoo \u0026\u2028 \u2029\u003c/html\u003e"}`))
	HTMLEscape(&b, []byte(m))
	if !bytes.Equal(b.Bytes(), want.Bytes()) {
		t.Errorf("HTMLEscape(&b, []byte(m)) = %s; want %s", b.Bytes(), want.Bytes())
	}
}

// golang.org/issue/8582
func TestEncodePointerString(t *testing.T) {
	type stringPointer struct {
		N *int64 `json:"n,string"`
	}
	var n int64 = 42
	b, err := Marshal(stringPointer{N: &n})
	if err != nil {
		t.Fatalf("Marshal: %v", err)
	}
	if got, want := string(b), `{"n":"42"}`; got != want {
		t.Errorf("Marshal = %s, want %s", got, want)
	}
	var back stringPointer
	err = Unmarshal(b, &back)
	if err != nil {
		t.Fatalf("Unmarshal: %v", err)
	}
	if back.N == nil {
		t.Fatalf("Unmarshaled nil N field")
	}
	if *back.N != 42 {
		t.Fatalf("*N = %d; want 42", *back.N)
	}
}

var encodeStringTests = []struct {
	in  string
	out string
}{
	{"\x00", `"\u0000"`},
	{"\x01", `"\u0001"`},
	{"\x02", `"\u0002"`},
	{"\x03", `"\u0003"`},
	{"\x04", `"\u0004"`},
	{"\x05", `"\u0005"`},
	{"\x06", `"\u0006"`},
	{"\x07", `"\u0007"`},
	{"\x08", `"\b"`},
	{"\x09", `"\t"`},
	{"\x0a", `"\n"`},
	{"\x0b", `"\u000b"`},
	{"\x0c", `"\f"`},
	{"\x0d", `"\r"`},
	{"\x0e", `"\u000e"`},
	{"\x0f", `"\u000f"`},
	{"\x10", `"\u0010"`},
	{"\x11", `"\u0011"`},
	{"\x12", `"\u0012"`},
	{"\x13", `"\u0013"`},
	{"\x14", `"\u0014"`},
	{"\x15", `"\u0015"`},
	{"\x16", `"\u0016"`},
	{"\x17", `"\u0017"`},
	{"\x18", `"\u0018"`},
	{"\x19", `"\u0019"`},
	{"\x1a", `"\u001a"`},
	{"\x1b", `"\u001b"`},
	{"\x1c", `"\u001c"`},
	{"\x1d", `"\u001d"`},
	{"\x1e", `"\u001e"`},
	{"\x1f", `"\u001f"`},
}

func TestEncodeString(t *testing.T) {
	for _, tt := range encodeStringTests {
		b, err := Marshal(tt.in)
		if err != nil {
			t.Errorf("Marshal(%q): %v", tt.in, err)
			continue
		}
		out := string(b)
		if out != tt.out {
			t.Errorf("Marshal(%q) = %#q, want %#q", tt.in, out, tt.out)
		}
	}
}

type jsonbyte byte

func (b jsonbyte) MarshalJSON() ([]byte, error) { return tenc(`{"JB":%d}`, b) }

type textbyte byte

func (b textbyte) MarshalText() ([]byte, error) { return tenc(`TB:%d`, b) }

type jsonint int

func (i jsonint) MarshalJSON() ([]byte, error) { return tenc(`{"JI":%d}`, i) }

type textint int

func (i textint) MarshalText() ([]byte, error) { return tenc(`TI:%d`, i) }

func tenc(format string, a ...any) ([]byte, error) {
	var buf bytes.Buffer
	fmt.Fprintf(&buf, format, a...)
	return buf.Bytes(), nil
}

// Issue 13783
func TestEncodeBytekind(t *testing.T) {
	testdata := []struct {
		data any
		want string
	}{
		{byte(7), "7"},
		{jsonbyte(7), `{"JB":7}`},
		{textbyte(4), `"TB:4"`},
		{jsonint(5), `{"JI":5}`},
		{textint(1), `"TI:1"`},
		{[]byte{0, 1}, `"AAE="`},
		{[]jsonbyte{0, 1}, `[{"JB":0},{"JB":1}]`},
		{[][]jsonbyte{{0, 1}, {3}}, `[[{"JB":0},{"JB":1}],[{"JB":3}]]`},
		{[]textbyte{2, 3}, `["TB:2","TB:3"]`},
		{[]jsonint{5, 4}, `[{"JI":5},{"JI":4}]`},
		{[]textint{9, 3}, `["TI:9","TI:3"]`},
		{[]int{9, 3}, `[9,3]`},
	}
	for _, d := range testdata {
		js, err := Marshal(d.data)
		if err != nil {
			t.Error(err)
			continue
		}
		got, want := string(js), d.want
		if got != want {
			t.Errorf("got %s, want %s", got, want)
		}
	}
}

func TestTextMarshalerMapKeysAreSorted(t *testing.T) {
	b, err := Marshal(map[unmarshalerText]int{
		{"x", "y"}: 1,
		{"y", "x"}: 2,
		{"a", "z"}: 3,
		{"z", "a"}: 4,
	})
	if err != nil {
		t.Fatalf("Failed to Marshal text.Marshaler: %v", err)
	}
	const want = `{"a:z":3,"x:y":1,"y:x":2,"z:a":4}`
	if string(b) != want {
		t.Errorf("Marshal map with text.Marshaler keys: got %#q, want %#q", b, want)
	}
}

var re = regexp.MustCompile

// syntactic checks on form of marshaled floating point numbers.
var badFloatREs = []*regexp.Regexp{
	re(`p`),                     // no binary exponential notation
	re(`^\+`),                   // no leading + sign
	re(`^-?0[^.]`),              // no unnecessary leading zeros
	re(`^-?\.`),                 // leading zero required before decimal point
	re(`\.(e|$)`),               // no trailing decimal
	re(`\.[0-9]+0(e|$)`),        // no trailing zero in fraction
	re(`^-?(0|[0-9]{2,})\..*e`), // exponential notation must have normalized mantissa
	re(`e[0-9]`),                // positive exponent must be signed
	re(`e[+-]0`),                // exponent must not have leading zeros
	re(`e-[1-6]$`),              // not tiny enough for exponential notation
	re(`e+(.|1.|20)$`),          // not big enough for exponential notation
	re(`^-?0\.0000000`),         // too tiny, should use exponential notation
	re(`^-?[0-9]{22}`),          // too big, should use exponential notation
	re(`[1-9][0-9]{16}[1-9]`),   // too many significant digits in integer
	re(`[1-9][0-9.]{17}[1-9]`),  // too many significant digits in decimal
	// below here for float32 only
	re(`[1-9][0-9]{8}[1-9]`),  // too many significant digits in integer
	re(`[1-9][0-9.]{9}[1-9]`), // too many significant digits in decimal
}

func TestMarshalFloat(t *testing.T) {
	t.Parallel()
	nfail := 0
	test := func(f float64, bits int) {
		vf := any(f)
		if bits == 32 {
			f = float64(float32(f)) // round
			vf = float32(f)
		}
		bout, err := Marshal(vf)
		if err != nil {
			t.Errorf("Marshal(%T(%g)): %v", vf, vf, err)
			nfail++
			return
		}
		out := string(bout)

		// result must convert back to the same float
		g, err := strconv.ParseFloat(out, bits)
		if err != nil {
			t.Errorf("Marshal(%T(%g)) = %q, cannot parse back: %v", vf, vf, out, err)
			nfail++
			return
		}
		if f != g || fmt.Sprint(f) != fmt.Sprint(g) { // fmt.Sprint handles ±0
			t.Errorf("Marshal(%T(%g)) = %q (is %g, not %g)", vf, vf, out, float32(g), vf)
			nfail++
			return
		}

		bad := badFloatREs
		if bits == 64 {
			bad = bad[:len(bad)-2]
		}
		for _, re := range bad {
			if re.MatchString(out) {
				t.Errorf("Marshal(%T(%g)) = %q, must not match /%s/", vf, vf, out, re)
				nfail++
				return
			}
		}
	}

	var (
		bigger  = math.Inf(+1)
		smaller = math.Inf(-1)
	)

	digits := "1.2345678901234567890123"
	for i := len(digits); i >= 2; i-- {
		if testing.Short() && i < len(digits)-4 {
			break
		}
		for exp := -30; exp <= 30; exp++ {
			for _, sign := range "+-" {
				for bits := 32; bits <= 64; bits += 32 {
					s := fmt.Sprintf("%c%se%d", sign, digits[:i], exp)
					f, err := strconv.ParseFloat(s, bits)
					if err != nil {
						log.Fatal(err)
					}
					next := math.Nextafter
					if bits == 32 {
						next = func(g, h float64) float64 {
							return float64(math.Nextafter32(float32(g), float32(h)))
						}
					}
					test(f, bits)
					test(next(f, bigger), bits)
					test(next(f, smaller), bits)
					if nfail > 50 {
						t.Fatalf("stopping test early")
					}
				}
			}
		}
	}
	test(0, 64)
	test(math.Copysign(0, -1), 64)
	test(0, 32)
	test(math.Copysign(0, -1), 32)
}

func TestMarshalRawMessageValue(t *testing.T) {
	type (
		T1 struct {
			M RawMessage `json:",omitempty"`
		}
		T2 struct {
			M *RawMessage `json:",omitempty"`
		}
	)

	var (
		rawNil   = RawMessage(nil)
		rawEmpty = RawMessage([]byte{})
		rawText  = RawMessage([]byte(`"foo"`))
	)

	tests := []struct {
		in   any
		want string
		ok   bool
	}{
		// Test with nil RawMessage.
		{rawNil, "null", true},
		{&rawNil, "null", true},
		{[]any{rawNil}, "[null]", true},
		{&[]any{rawNil}, "[null]", true},
		{[]any{&rawNil}, "[null]", true},
		{&[]any{&rawNil}, "[null]", true},
		{struct{ M RawMessage }{rawNil}, `{"M":null}`, true},
		{&struct{ M RawMessage }{rawNil}, `{"M":null}`, true},
		{struct{ M *RawMessage }{&rawNil}, `{"M":null}`, true},
		{&struct{ M *RawMessage }{&rawNil}, `{"M":null}`, true},
		{map[string]any{"M": rawNil}, `{"M":null}`, true},
		{&map[string]any{"M": rawNil}, `{"M":null}`, true},
		{map[string]any{"M": &rawNil}, `{"M":null}`, true},
		{&map[string]any{"M": &rawNil}, `{"M":null}`, true},
		{T1{rawNil}, "{}", true},
		{T2{&rawNil}, `{"M":null}`, true},
		{&T1{rawNil}, "{}", true},
		{&T2{&rawNil}, `{"M":null}`, true},

		// Test with empty, but non-nil, RawMessage.
		{rawEmpty, "", false},
		{&rawEmpty, "", false},
		{[]any{rawEmpty}, "", false},
		{&[]any{rawEmpty}, "", false},
		{[]any{&rawEmpty}, "", false},
		{&[]any{&rawEmpty}, "", false},
		{struct{ X RawMessage }{rawEmpty}, "", false},
		{&struct{ X RawMessage }{rawEmpty}, "", false},
		{struct{ X *RawMessage }{&rawEmpty}, "", false},
		{&struct{ X *RawMessage }{&rawEmpty}, "", false},
		{map[string]any{"nil": rawEmpty}, "", false},
		{&map[string]any{"nil": rawEmpty}, "", false},
		{map[string]any{"nil": &rawEmpty}, "", false},
		{&map[string]any{"nil": &rawEmpty}, "", false},
		{T1{rawEmpty}, "{}", true},
		{T2{&rawEmpty}, "", false},
		{&T1{rawEmpty}, "{}", true},
		{&T2{&rawEmpty}, "", false},

		// Test with RawMessage with some text.
		//
		// The tests below marked with Issue6458 used to generate "ImZvbyI=" instead "foo".
		// This behavior was intentionally changed in Go 1.8.
		// See https://golang.org/issues/14493#issuecomment-255857318
		{rawText, `"foo"`, true}, // Issue6458
		{&rawText, `"foo"`, true},
		{[]any{rawText}, `["foo"]`, true},  // Issue6458
		{&[]any{rawText}, `["foo"]`, true}, // Issue6458
		{[]any{&rawText}, `["foo"]`, true},
		{&[]any{&rawText}, `["foo"]`, true},
		{struct{ M RawMessage }{rawText}, `{"M":"foo"}`, true}, // Issue6458
		{&struct{ M RawMessage }{rawText}, `{"M":"foo"}`, true},
		{struct{ M *RawMessage }{&rawText}, `{"M":"foo"}`, true},
		{&struct{ M *RawMessage }{&rawText}, `{"M":"foo"}`, true},
		{map[string]any{"M": rawText}, `{"M":"foo"}`, true},  // Issue6458
		{&map[string]any{"M": rawText}, `{"M":"foo"}`, true}, // Issue6458
		{map[string]any{"M": &rawText}, `{"M":"foo"}`, true},
		{&map[string]any{"M": &rawText}, `{"M":"foo"}`, true},
		{T1{rawText}, `{"M":"foo"}`, true}, // Issue6458
		{T2{&rawText}, `{"M":"foo"}`, true},
		{&T1{rawText}, `{"M":"foo"}`, true},
		{&T2{&rawText}, `{"M":"foo"}`, true},
	}

	for i, tt := range tests {
		b, err := Marshal(tt.in)
		if ok := (err == nil); ok != tt.ok {
			if err != nil {
				t.Errorf("test %d, unexpected failure: %v", i, err)
			} else {
				t.Errorf("test %d, unexpected success", i)
			}
		}
		if got := string(b); got != tt.want {
			t.Errorf("test %d, Marshal(%#v) = %q, want %q", i, tt.in, got, tt.want)
		}
	}
}

type marshalPanic struct{}

func (marshalPanic) MarshalJSON() ([]byte, error) { panic(0xdead) }

func TestMarshalPanic(t *testing.T) {
	defer func() {
		if got := recover(); !reflect.DeepEqual(got, 0xdead) {
			t.Errorf("panic() = (%T)(%v), want 0xdead", got, got)
		}
	}()
	Marshal(&marshalPanic{})
	t.Error("Marshal should have panicked")
}

func TestMarshalUncommonFieldNames(t *testing.T) {
	v := struct {
		A0, À, Aβ int
	}{}
	b, err := Marshal(v)
	if err != nil {
		t.Fatal("Marshal:", err)
	}
	want := `{"A0":0,"À":0,"Aβ":0}`
	got := string(b)
	if got != want {
		t.Fatalf("Marshal: got %s want %s", got, want)
	}
}
```

## File: `json/golang_example_marshaling_test.go`
```go
// Copyright 2016 The Go Authors. All rights reserved.
// Use of this source code is governed by a BSD-style
// license that can be found in the LICENSE file.

package json_test

import (
	"encoding/json"
	"fmt"
	"log"
	"strings"
)

type Animal int

const (
	Unknown Animal = iota
	Gopher
	Zebra
)

func (a *Animal) UnmarshalJSON(b []byte) error {
	var s string
	if err := json.Unmarshal(b, &s); err != nil {
		return err
	}
	switch strings.ToLower(s) {
	default:
		*a = Unknown
	case "gopher":
		*a = Gopher
	case "zebra":
		*a = Zebra
	}

	return nil
}

func (a Animal) MarshalJSON() ([]byte, error) {
	var s string
	switch a {
	default:
		s = "unknown"
	case Gopher:
		s = "gopher"
	case Zebra:
		s = "zebra"
	}

	return json.Marshal(s)
}

func Example_customMarshalJSON() {
	blob := `["gopher","armadillo","zebra","unknown","gopher","bee","gopher","zebra"]`
	var zoo []Animal
	if err := json.Unmarshal([]byte(blob), &zoo); err != nil {
		log.Fatal(err)
	}

	census := make(map[Animal]int)
	for _, animal := range zoo {
		census[animal] += 1
	}

	fmt.Printf("Zoo Census:\n* Gophers: %d\n* Zebras:  %d\n* Unknown: %d\n",
		census[Gopher], census[Zebra], census[Unknown])

	// Output:
	// Zoo Census:
	// * Gophers: 3
	// * Zebras:  2
	// * Unknown: 3
}
```

## File: `json/golang_example_test.go`
```go
// Copyright 2011 The Go Authors. All rights reserved.
// Use of this source code is governed by a BSD-style
// license that can be found in the LICENSE file.

package json_test

import (
	"bytes"
	"encoding/json"
	"fmt"
	"io"
	"log"
	"os"
	"strings"
)

func ExampleMarshal() {
	type ColorGroup struct {
		ID     int
		Name   string
		Colors []string
	}
	group := ColorGroup{
		ID:     1,
		Name:   "Reds",
		Colors: []string{"Crimson", "Red", "Ruby", "Maroon"},
	}
	b, err := json.Marshal(group)
	if err != nil {
		fmt.Println("error:", err)
	}
	os.Stdout.Write(b)
	// Output:
	// {"ID":1,"Name":"Reds","Colors":["Crimson","Red","Ruby","Maroon"]}
}

func ExampleUnmarshal() {
	jsonBlob := []byte(`[
	{"Name": "Platypus", "Order": "Monotremata"},
	{"Name": "Quoll",    "Order": "Dasyuromorphia"}
]`)
	type Animal struct {
		Name  string
		Order string
	}
	var animals []Animal
	err := json.Unmarshal(jsonBlob, &animals)
	if err != nil {
		fmt.Println("error:", err)
	}
	fmt.Printf("%+v", animals)
	// Output:
	// [{Name:Platypus Order:Monotremata} {Name:Quoll Order:Dasyuromorphia}]
}

// This example uses a Decoder to decode a stream of distinct JSON values.
func ExampleDecoder() {
	const jsonStream = `
	{"Name": "Ed", "Text": "Knock knock."}
	{"Name": "Sam", "Text": "Who's there?"}
	{"Name": "Ed", "Text": "Go fmt."}
	{"Name": "Sam", "Text": "Go fmt who?"}
	{"Name": "Ed", "Text": "Go fmt yourself!"}
`
	type Message struct {
		Name, Text string
	}
	dec := json.NewDecoder(strings.NewReader(jsonStream))
	for {
		var m Message
		if err := dec.Decode(&m); err == io.EOF {
			break
		} else if err != nil {
			log.Fatal(err)
		}
		fmt.Printf("%s: %s\n", m.Name, m.Text)
	}
	// Output:
	// Ed: Knock knock.
	// Sam: Who's there?
	// Ed: Go fmt.
	// Sam: Go fmt who?
	// Ed: Go fmt yourself!
}

// This example uses a Decoder to decode a stream of distinct JSON values.
func ExampleDecoder_Token() {
	const jsonStream = `
	{"Message": "Hello", "Array": [1, 2, 3], "Null": null, "Number": 1.234}
`
	dec := json.NewDecoder(strings.NewReader(jsonStream))
	for {
		t, err := dec.Token()
		if err == io.EOF {
			break
		}
		if err != nil {
			log.Fatal(err)
		}
		fmt.Printf("%T: %v", t, t)
		if dec.More() {
			fmt.Printf(" (more)")
		}
		fmt.Printf("\n")
	}
	// Output:
	// json.Delim: { (more)
	// string: Message (more)
	// string: Hello (more)
	// string: Array (more)
	// json.Delim: [ (more)
	// float64: 1 (more)
	// float64: 2 (more)
	// float64: 3
	// json.Delim: ] (more)
	// string: Null (more)
	// <nil>: <nil> (more)
	// string: Number (more)
	// float64: 1.234
	// json.Delim: }
}

// This example uses a Decoder to decode a streaming array of JSON objects.
func ExampleDecoder_Decode_stream() {
	const jsonStream = `
	[
		{"Name": "Ed", "Text": "Knock knock."},
		{"Name": "Sam", "Text": "Who's there?"},
		{"Name": "Ed", "Text": "Go fmt."},
		{"Name": "Sam", "Text": "Go fmt who?"},
		{"Name": "Ed", "Text": "Go fmt yourself!"}
	]
`
	type Message struct {
		Name, Text string
	}
	dec := json.NewDecoder(strings.NewReader(jsonStream))

	// read open bracket
	t, err := dec.Token()
	if err != nil {
		log.Fatal(err)
	}
	fmt.Printf("%T: %v\n", t, t)

	// while the array contains values
	for dec.More() {
		var m Message
		// decode an array value (Message)
		err := dec.Decode(&m)
		if err != nil {
			log.Fatal(err)
		}

		fmt.Printf("%v: %v\n", m.Name, m.Text)
	}

	// read closing bracket
	t, err = dec.Token()
	if err != nil {
		log.Fatal(err)
	}
	fmt.Printf("%T: %v\n", t, t)

	// Output:
	// json.Delim: [
	// Ed: Knock knock.
	// Sam: Who's there?
	// Ed: Go fmt.
	// Sam: Go fmt who?
	// Ed: Go fmt yourself!
	// json.Delim: ]
}

// This example uses RawMessage to delay parsing part of a JSON message.
func ExampleRawMessage_unmarshal() {
	type Color struct {
		Space string
		Point json.RawMessage // delay parsing until we know the color space
	}
	type RGB struct {
		R uint8
		G uint8
		B uint8
	}
	type YCbCr struct {
		Y  uint8
		Cb int8
		Cr int8
	}

	j := []byte(`[
	{"Space": "YCbCr", "Point": {"Y": 255, "Cb": 0, "Cr": -10}},
	{"Space": "RGB",   "Point": {"R": 98, "G": 218, "B": 255}}
]`)
	var colors []Color
	err := json.Unmarshal(j, &colors)
	if err != nil {
		log.Fatalln("error:", err)
	}

	for _, c := range colors {
		var dst any
		switch c.Space {
		case "RGB":
			dst = new(RGB)
		case "YCbCr":
			dst = new(YCbCr)
		}
		err := json.Unmarshal(c.Point, dst)
		if err != nil {
			log.Fatalln("error:", err)
		}
		fmt.Println(c.Space, dst)
	}
	// Output:
	// YCbCr &{255 0 -10}
	// RGB &{98 218 255}
}

// This example uses RawMessage to use a precomputed JSON during marshal.
func ExampleRawMessage_marshal() {
	h := json.RawMessage(`{"precomputed": true}`)

	c := struct {
		Header *json.RawMessage `json:"header"`
		Body   string           `json:"body"`
	}{Header: &h, Body: "Hello Gophers!"}

	b, err := json.MarshalIndent(&c, "", "\t")
	if err != nil {
		fmt.Println("error:", err)
	}
	os.Stdout.Write(b)

	// Output:
	// {
	// 	"header": {
	// 		"precomputed": true
	// 	},
	// 	"body": "Hello Gophers!"
	// }
}

func ExampleIndent() {
	type Road struct {
		Name   string
		Number int
	}
	roads := []Road{
		{"Diamond Fork", 29},
		{"Sheep Creek", 51},
	}

	b, err := json.Marshal(roads)
	if err != nil {
		log.Fatal(err)
	}

	var out bytes.Buffer
	json.Indent(&out, b, "=", "\t")
	out.WriteTo(os.Stdout)
	// Output:
	// [
	// =	{
	// =		"Name": "Diamond Fork",
	// =		"Number": 29
	// =	},
	// =	{
	// =		"Name": "Sheep Creek",
	// =		"Number": 51
	// =	}
	// =]
}

func ExampleMarshalIndent() {
	data := map[string]int{
		"a": 1,
		"b": 2,
	}

	json, err := json.MarshalIndent(data, "<prefix>", "<indent>")
	if err != nil {
		log.Fatal(err)
	}

	fmt.Println(string(json))
	// Output:
	// {
	// <prefix><indent>"a": 1,
	// <prefix><indent>"b": 2
	// <prefix>}
}

func ExampleValid() {
	goodJSON := `{"example": 1}`
	badJSON := `{"example":2:]}}`

	fmt.Println(json.Valid([]byte(goodJSON)), json.Valid([]byte(badJSON)))
	// Output:
	// true false
}

func ExampleHTMLEscape() {
	var out bytes.Buffer
	json.HTMLEscape(&out, []byte(`{"Name":"<b>HTML content</b>"}`))
	out.WriteTo(os.Stdout)
	// Output:
	//{"Name":"\u003cb\u003eHTML content\u003c/b\u003e"}
}
```

## File: `json/golang_number_test.go`
```go
// Copyright 2011 The Go Authors. All rights reserved.
// Use of this source code is governed by a BSD-style
// license that can be found in the LICENSE file.

package json

import (
	"regexp"
	"testing"
)

func TestNumberIsValid(t *testing.T) {
	// From: https://stackoverflow.com/a/13340826
	jsonNumberRegexp := regexp.MustCompile(`^-?(?:0|[1-9]\d*)(?:\.\d+)?(?:[eE][+-]?\d+)?$`)

	validTests := []string{
		"0",
		"-0",
		"1",
		"-1",
		"0.1",
		"-0.1",
		"1234",
		"-1234",
		"12.34",
		"-12.34",
		"12E0",
		"12E1",
		"12e34",
		"12E-0",
		"12e+1",
		"12e-34",
		"-12E0",
		"-12E1",
		"-12e34",
		"-12E-0",
		"-12e+1",
		"-12e-34",
		"1.2E0",
		"1.2E1",
		"1.2e34",
		"1.2E-0",
		"1.2e+1",
		"1.2e-34",
		"-1.2E0",
		"-1.2E1",
		"-1.2e34",
		"-1.2E-0",
		"-1.2e+1",
		"-1.2e-34",
		"0E0",
		"0E1",
		"0e34",
		"0E-0",
		"0e+1",
		"0e-34",
		"-0E0",
		"-0E1",
		"-0e34",
		"-0E-0",
		"-0e+1",
		"-0e-34",
	}

	for _, test := range validTests {
		if !isValidNumber(test) {
			t.Errorf("%s should be valid", test)
		}

		var f float64
		if err := Unmarshal([]byte(test), &f); err != nil {
			t.Errorf("%s should be valid but Unmarshal failed: %v", test, err)
		}

		if !jsonNumberRegexp.MatchString(test) {
			t.Errorf("%s should be valid but regexp does not match", test)
		}
	}

	invalidTests := []string{
		"",
		"invalid",
		"1.0.1",
		"1..1",
		"-1-2",
		"012a42",
		"01.2",
		"012",
		"12E12.12",
		"1e2e3",
		"1e+-2",
		"1e--23",
		"1e",
		"e1",
		"1e+",
		"1ea",
		"1a",
		"1.a",
		"1.",
		"01",
		"1.e1",
	}

	for _, test := range invalidTests {
		var f float64
		if err := Unmarshal([]byte(test), &f); err == nil {
			t.Errorf("%s should be invalid but unmarshal wrote %v", test, f)
		}

		if jsonNumberRegexp.MatchString(test) {
			t.Errorf("%s should be invalid but matches regexp", test)
		}
	}
}

func BenchmarkNumberIsValid(b *testing.B) {
	s := "-61657.61667E+61673"
	for range b.N {
		isValidNumber(s)
	}
}

func BenchmarkNumberIsValidRegexp(b *testing.B) {
	jsonNumberRegexp := regexp.MustCompile(`^-?(?:0|[1-9]\d*)(?:\.\d+)?(?:[eE][+-]?\d+)?$`)
	s := "-61657.61667E+61673"
	for range b.N {
		jsonNumberRegexp.MatchString(s)
	}
}
```

## File: `json/golang_scanner_test.go`
```go
// Copyright 2010 The Go Authors. All rights reserved.
// Use of this source code is governed by a BSD-style
// license that can be found in the LICENSE file.

package json

import (
	"bytes"
	"math"
	"math/rand"
	"testing"
)

var validTests = []struct {
	data string
	ok   bool
}{
	{`foo`, false},
	{`}{`, false},
	{`{]`, false},
	{`{}`, true},
	{`{"foo":"bar"}`, true},
	{`{"foo":"bar","bar":{"baz":["qux"]}}`, true},
}

func TestValid(t *testing.T) {
	for _, tt := range validTests {
		if ok := Valid([]byte(tt.data)); ok != tt.ok {
			t.Errorf("Valid(%#q) = %v, want %v", tt.data, ok, tt.ok)
		}
	}
}

// Tests of simple examples.

type example struct {
	compact string
	indent  string
}

var examples = []example{
	{`1`, `1`},
	{`{}`, `{}`},
	{`[]`, `[]`},
	{`{"":2}`, "{\n\t\"\": 2\n}"},
	{`[3]`, "[\n\t3\n]"},
	{`[1,2,3]`, "[\n\t1,\n\t2,\n\t3\n]"},
	{`{"x":1}`, "{\n\t\"x\": 1\n}"},
	{ex1, ex1i},
	{"{\"\":\"<>&\u2028\u2029\"}", "{\n\t\"\": \"<>&\u2028\u2029\"\n}"}, // See golang.org/issue/34070
}

var ex1 = `[true,false,null,"x",1,1.5,0,-5e+2]`

var ex1i = `[
	true,
	false,
	null,
	"x",
	1,
	1.5,
	0,
	-5e+2
]`

func TestCompact(t *testing.T) {
	var buf bytes.Buffer
	for _, tt := range examples {
		buf.Reset()
		if err := Compact(&buf, []byte(tt.compact)); err != nil {
			t.Errorf("Compact(%#q): %v", tt.compact, err)
		} else if s := buf.String(); s != tt.compact {
			t.Errorf("Compact(%#q) = %#q, want original", tt.compact, s)
		}

		buf.Reset()
		if err := Compact(&buf, []byte(tt.indent)); err != nil {
			t.Errorf("Compact(%#q): %v", tt.indent, err)
			continue
		} else if s := buf.String(); s != tt.compact {
			t.Errorf("Compact(%#q) = %#q, want %#q", tt.indent, s, tt.compact)
		}
	}
}

func TestCompactSeparators(t *testing.T) {
	// U+2028 and U+2029 should be escaped inside strings.
	// They should not appear outside strings.
	tests := []struct {
		in, compact string
	}{
		{"{\"\u2028\": 1}", "{\"\u2028\":1}"},
		{"{\"\u2029\" :2}", "{\"\u2029\":2}"},
	}
	for _, tt := range tests {
		var buf bytes.Buffer
		if err := Compact(&buf, []byte(tt.in)); err != nil {
			t.Errorf("Compact(%q): %v", tt.in, err)
		} else if s := buf.String(); s != tt.compact {
			t.Errorf("Compact(%q) = %q, want %q", tt.in, s, tt.compact)
		}
	}
}

func TestIndent(t *testing.T) {
	var buf bytes.Buffer
	for _, tt := range examples {
		buf.Reset()
		if err := Indent(&buf, []byte(tt.indent), "", "\t"); err != nil {
			t.Errorf("Indent(%#q): %v", tt.indent, err)
		} else if s := buf.String(); s != tt.indent {
			t.Errorf("Indent(%#q) = %#q, want original", tt.indent, s)
		}

		buf.Reset()
		if err := Indent(&buf, []byte(tt.compact), "", "\t"); err != nil {
			t.Errorf("Indent(%#q): %v", tt.compact, err)
			continue
		} else if s := buf.String(); s != tt.indent {
			t.Errorf("Indent(%#q) = %#q, want %#q", tt.compact, s, tt.indent)
		}
	}
}

// Tests of a large random structure.

func TestCompactBig(t *testing.T) {
	initBig()
	var buf bytes.Buffer
	if err := Compact(&buf, jsonBig); err != nil {
		t.Fatalf("Compact: %v", err)
	}
	b := buf.Bytes()
	if !bytes.Equal(b, jsonBig) {
		t.Error("Compact(jsonBig) != jsonBig")
		diff(t, b, jsonBig)
		return
	}
}

func TestIndentBig(t *testing.T) {
	t.Parallel()
	initBig()
	var buf bytes.Buffer
	if err := Indent(&buf, jsonBig, "", "\t"); err != nil {
		t.Fatalf("Indent1: %v", err)
	}
	b := buf.Bytes()
	if len(b) == len(jsonBig) {
		// jsonBig is compact (no unnecessary spaces);
		// indenting should make it bigger
		t.Fatalf("Indent(jsonBig) did not get bigger")
	}

	// should be idempotent
	var buf1 bytes.Buffer
	if err := Indent(&buf1, b, "", "\t"); err != nil {
		t.Fatalf("Indent2: %v", err)
	}
	b1 := buf1.Bytes()
	if !bytes.Equal(b1, b) {
		t.Error("Indent(Indent(jsonBig)) != Indent(jsonBig)")
		diff(t, b1, b)
		return
	}

	// should get back to original
	buf1.Reset()
	if err := Compact(&buf1, b); err != nil {
		t.Fatalf("Compact: %v", err)
	}
	b1 = buf1.Bytes()
	if !bytes.Equal(b1, jsonBig) {
		t.Error("Compact(Indent(jsonBig)) != jsonBig")
		diff(t, b1, jsonBig)
		return
	}
}

type indentErrorTest struct {
	in  string
	err error
}

var indentErrorTests = []indentErrorTest{
	{`{"X": "foo", "Y"}`, &testSyntaxError{"invalid character '}' after object key", 17}},
	{`{"X": "foo" "Y": "bar"}`, &testSyntaxError{"invalid character '\"' after object key:value pair", 13}},
}

func TestIndentErrors(t *testing.T) {
	for i, tt := range indentErrorTests {
		slice := make([]uint8, 0)
		buf := bytes.NewBuffer(slice)
		err := Indent(buf, []uint8(tt.in), "", "")
		assertErrorPresence(t, tt.err, err, i)
	}
}

func diff(t *testing.T, a, b []byte) {
	for i := 0; ; i++ {
		if i >= len(a) || i >= len(b) || a[i] != b[i] {
			j := max(0, i-10)
			t.Errorf("diverge at %d: «%s» vs «%s»", i, trim(a[j:]), trim(b[j:]))
			return
		}
	}
}

func trim(b []byte) []byte {
	if len(b) > 20 {
		return b[0:20]
	}
	return b
}

// Generate a random JSON object.

var jsonBig []byte

func initBig() {
	n := 10000
	if testing.Short() {
		n = 100
	}
	b, err := Marshal(genValue(n))
	if err != nil {
		panic(err)
	}
	jsonBig = b
}

func genValue(n int) any {
	if n > 1 {
		switch rand.Intn(2) {
		case 0:
			return genArray(n)
		case 1:
			return genMap(n)
		}
	}
	switch rand.Intn(3) {
	case 0:
		return rand.Intn(2) == 0
	case 1:
		return rand.NormFloat64()
	case 2:
		return genString(30)
	}
	panic("unreachable")
}

func genString(stddev float64) string {
	n := int(math.Abs(rand.NormFloat64()*stddev + stddev/2))
	c := make([]rune, n)
	for i := range c {
		f := math.Abs(rand.NormFloat64()*64 + 32)
		if f > 0x10ffff {
			f = 0x10ffff
		}
		c[i] = rune(f)
	}
	return string(c)
}

func genArray(n int) []any {
	f := int(math.Abs(rand.NormFloat64()) * math.Min(10, float64(n/2)))
	if f > n {
		f = n
	}
	if f < 1 {
		f = 1
	}
	x := make([]any, f)
	for i := range x {
		x[i] = genValue(((i+1)*n)/f - (i*n)/f)
	}
	return x
}

func genMap(n int) map[string]any {
	f := int(math.Abs(rand.NormFloat64()) * math.Min(10, float64(n/2)))
	f = min(f, n)
	if n > 0 && f == 0 {
		f = 1
	}
	x := make(map[string]any)
	for i := range f {
		x[genString(10)] = genValue(((i+1)*n)/f - (i*n)/f)
	}
	return x
}
```

## File: `json/golang_shim_test.go`
```go
// This file is a shim for dependencies of golang_*_test.go files that are normally provided by the standard library.
// It helps importing those files with minimal changes.
package json

import (
	"bytes"
	"reflect"
	"sync"
	"testing"
)

// Field cache used in golang_bench_test.go
var fieldCache = sync.Map{}

func cachedTypeFields(reflect.Type) {}

// Fake test env for golang_bench_test.go
type testenvShim struct{}

func (ts testenvShim) Builder() string {
	return ""
}

var testenv testenvShim

// Fake scanner for golang_decode_test.go
type scanner struct{}

func checkValid(in []byte, scan *scanner) error {
	return nil
}

// Actual isSpace implementation
func isSpace(c byte) bool {
	return c == ' ' || c == '\t' || c == '\r' || c == '\n'
}

// Fake encoder for golang_encode_test.go
type encodeState struct {
	Buffer bytes.Buffer
}

func (es *encodeState) string(s string, escapeHTML bool) {
}

func (es *encodeState) stringBytes(b []byte, escapeHTML bool) {
}

// Fake number test
func isValidNumber(n string) bool {
	return true
}

func assertErrorPresence(t *testing.T, expected error, actual error, prefixes ...any) {
	if expected != nil && actual == nil {
		errorWithPrefixes(t, prefixes, "expected error, but did not get an error")
	} else if expected == nil && actual != nil {
		errorWithPrefixes(t, prefixes, "did not expect error but got %v", actual)
	}
}

func errorWithPrefixes(t *testing.T, prefixes []any, format string, elements ...any) {
	fullFormat := format
	allElements := append(prefixes, elements...)

	for range prefixes {
		fullFormat = "%v: " + fullFormat
	}
	t.Errorf(fullFormat, allElements...)
}
```

## File: `json/golang_tagkey_test.go`
```go
// Copyright 2011 The Go Authors. All rights reserved.
// Use of this source code is governed by a BSD-style
// license that can be found in the LICENSE file.

package json

import (
	"testing"
)

type basicLatin2xTag struct {
	V string `json:"$%-/"`
}

type basicLatin3xTag struct {
	V string `json:"0123456789"`
}

type basicLatin4xTag struct {
	V string `json:"ABCDEFGHIJKLMO"`
}

type basicLatin5xTag struct {
	V string `json:"PQRSTUVWXYZ_"`
}

type basicLatin6xTag struct {
	V string `json:"abcdefghijklmno"`
}

type basicLatin7xTag struct {
	V string `json:"pqrstuvwxyz"`
}

type miscPlaneTag struct {
	V string `json:"色は匂へど"`
}

type percentSlashTag struct {
	V string `json:"text/html%"` // https://golang.org/issue/2718
}

type punctuationTag struct {
	V string `json:"!#$%&()*+-./:;<=>?@[]^_{|}~"` // https://golang.org/issue/3546
}

type dashTag struct {
	V string `json:"-,"`
}

type emptyTag struct {
	W string
}

type misnamedTag struct {
	X string `jsom:"Misnamed"`
}

type badFormatTag struct {
	Y string `:"BadFormat"`
}

type badCodeTag struct {
	Z string `json:" !\"#&'()*+,."`
}

type spaceTag struct {
	Q string `json:"With space"`
}

type unicodeTag struct {
	W string `json:"Ελλάδα"`
}

var structTagObjectKeyTests = []struct {
	raw   any
	value string
	key   string
}{
	{basicLatin2xTag{"2x"}, "2x", "$%-/"},
	{basicLatin3xTag{"3x"}, "3x", "0123456789"},
	{basicLatin4xTag{"4x"}, "4x", "ABCDEFGHIJKLMO"},
	{basicLatin5xTag{"5x"}, "5x", "PQRSTUVWXYZ_"},
	{basicLatin6xTag{"6x"}, "6x", "abcdefghijklmno"},
	{basicLatin7xTag{"7x"}, "7x", "pqrstuvwxyz"},
	{miscPlaneTag{"いろはにほへと"}, "いろはにほへと", "色は匂へど"},
	{dashTag{"foo"}, "foo", "-"},
	{emptyTag{"Pour Moi"}, "Pour Moi", "W"},
	{misnamedTag{"Animal Kingdom"}, "Animal Kingdom", "X"},
	{badFormatTag{"Orfevre"}, "Orfevre", "Y"},
	{badCodeTag{"Reliable Man"}, "Reliable Man", "Z"},
	{percentSlashTag{"brut"}, "brut", "text/html%"},
	{punctuationTag{"Union Rags"}, "Union Rags", "!#$%&()*+-./:;<=>?@[]^_{|}~"},
	{spaceTag{"Perreddu"}, "Perreddu", "With space"},
	{unicodeTag{"Loukanikos"}, "Loukanikos", "Ελλάδα"},
}

func TestStructTagObjectKey(t *testing.T) {
	for _, tt := range structTagObjectKeyTests {
		b, err := Marshal(tt.raw)
		if err != nil {
			t.Fatalf("Marshal(%#q) failed: %v", tt.raw, err)
		}
		var f any
		err = Unmarshal(b, &f)
		if err != nil {
			t.Fatalf("Unmarshal(%#q) failed: %v", b, err)
		}
		for i, v := range f.(map[string]any) {
			switch i {
			case tt.key:
				if s, ok := v.(string); !ok || s != tt.value {
					t.Fatalf("Unexpected value: %#q, want %v", s, tt.value)
				}
			default:
				t.Fatalf("Unexpected key: %#q, from %#q", i, b)
			}
		}
	}
}
```

## File: `json/int.go`
```go
package json

import (
	"unsafe"
)

var endianness int

func init() {
	var b [2]byte
	*(*uint16)(unsafe.Pointer(&b)) = uint16(0xABCD)

	switch b[0] {
	case 0xCD:
		endianness = 0 // LE
	case 0xAB:
		endianness = 1 // BE
	default:
		panic("could not determine endianness")
	}
}

// "00010203...96979899" cast to []uint16
var intLELookup = [100]uint16{
	0x3030, 0x3130, 0x3230, 0x3330, 0x3430, 0x3530, 0x3630, 0x3730, 0x3830, 0x3930,
	0x3031, 0x3131, 0x3231, 0x3331, 0x3431, 0x3531, 0x3631, 0x3731, 0x3831, 0x3931,
	0x3032, 0x3132, 0x3232, 0x3332, 0x3432, 0x3532, 0x3632, 0x3732, 0x3832, 0x3932,
	0x3033, 0x3133, 0x3233, 0x3333, 0x3433, 0x3533, 0x3633, 0x3733, 0x3833, 0x3933,
	0x3034, 0x3134, 0x3234, 0x3334, 0x3434, 0x3534, 0x3634, 0x3734, 0x3834, 0x3934,
	0x3035, 0x3135, 0x3235, 0x3335, 0x3435, 0x3535, 0x3635, 0x3735, 0x3835, 0x3935,
	0x3036, 0x3136, 0x3236, 0x3336, 0x3436, 0x3536, 0x3636, 0x3736, 0x3836, 0x3936,
	0x3037, 0x3137, 0x3237, 0x3337, 0x3437, 0x3537, 0x3637, 0x3737, 0x3837, 0x3937,
	0x3038, 0x3138, 0x3238, 0x3338, 0x3438, 0x3538, 0x3638, 0x3738, 0x3838, 0x3938,
	0x3039, 0x3139, 0x3239, 0x3339, 0x3439, 0x3539, 0x3639, 0x3739, 0x3839, 0x3939,
}

var intBELookup = [100]uint16{
	0x3030, 0x3031, 0x3032, 0x3033, 0x3034, 0x3035, 0x3036, 0x3037, 0x3038, 0x3039,
	0x3130, 0x3131, 0x3132, 0x3133, 0x3134, 0x3135, 0x3136, 0x3137, 0x3138, 0x3139,
	0x3230, 0x3231, 0x3232, 0x3233, 0x3234, 0x3235, 0x3236, 0x3237, 0x3238, 0x3239,
	0x3330, 0x3331, 0x3332, 0x3333, 0x3334, 0x3335, 0x3336, 0x3337, 0x3338, 0x3339,
	0x3430, 0x3431, 0x3432, 0x3433, 0x3434, 0x3435, 0x3436, 0x3437, 0x3438, 0x3439,
	0x3530, 0x3531, 0x3532, 0x3533, 0x3534, 0x3535, 0x3536, 0x3537, 0x3538, 0x3539,
	0x3630, 0x3631, 0x3632, 0x3633, 0x3634, 0x3635, 0x3636, 0x3637, 0x3638, 0x3639,
	0x3730, 0x3731, 0x3732, 0x3733, 0x3734, 0x3735, 0x3736, 0x3737, 0x3738, 0x3739,
	0x3830, 0x3831, 0x3832, 0x3833, 0x3834, 0x3835, 0x3836, 0x3837, 0x3838, 0x3839,
	0x3930, 0x3931, 0x3932, 0x3933, 0x3934, 0x3935, 0x3936, 0x3937, 0x3938, 0x3939,
}

var intLookup = [2]*[100]uint16{&intLELookup, &intBELookup}

func appendInt(b []byte, n int64) []byte {
	return formatInteger(b, uint64(n), n < 0)
}

func appendUint(b []byte, n uint64) []byte {
	return formatInteger(b, n, false)
}

func formatInteger(out []byte, n uint64, negative bool) []byte {
	if !negative {
		if n < 10 {
			return append(out, byte(n+'0'))
		} else if n < 100 {
			u := intLELookup[n]
			return append(out, byte(u), byte(u>>8))
		}
	} else {
		n = -n
	}

	lookup := intLookup[endianness]

	var b [22]byte
	u := (*[11]uint16)(unsafe.Pointer(&b))
	i := 11

	for n >= 100 {
		j := n % 100
		n /= 100
		i--
		u[i] = lookup[j]
	}

	i--
	u[i] = lookup[n]

	i *= 2 // convert to byte index
	if n < 10 {
		i++ // remove leading zero
	}
	if negative {
		i--
		b[i] = '-'
	}

	return append(out, b[i:]...)
}
```

## File: `json/int_test.go`
```go
package json

import (
	"math"
	"strconv"
	"testing"
)

func TestAppendInt(t *testing.T) {
	var ints []int64
	for i := range 64 {
		u := uint64(1) << i
		ints = append(ints, int64(u-1), int64(u), int64(u+1), -int64(u))
	}

	var std, our [20]byte

	for _, i := range ints {
		expected := strconv.AppendInt(std[:], i, 10)
		actual := appendInt(our[:], i)
		if string(expected) != string(actual) {
			t.Fatalf("appendInt(%d) = %v, expected = %v", i, string(actual), string(expected))
		}
	}
}

func benchStd(b *testing.B, n int64) {
	var buf [20]byte
	b.ResetTimer()
	for range b.N {
		strconv.AppendInt(buf[:0], n, 10)
	}
}

func benchNew(b *testing.B, n int64) {
	var buf [20]byte
	b.ResetTimer()
	for range b.N {
		appendInt(buf[:0], n)
	}
}

func BenchmarkAppendIntStd1(b *testing.B) {
	benchStd(b, 1)
}

func BenchmarkAppendInt1(b *testing.B) {
	benchNew(b, 1)
}

func BenchmarkAppendIntStdMinI64(b *testing.B) {
	benchStd(b, math.MinInt64)
}

func BenchmarkAppendIntMinI64(b *testing.B) {
	benchNew(b, math.MinInt64)
}
```

## File: `json/json.go`
```go
package json

import (
	"bytes"
	"encoding/json"
	"io"
	"math/bits"
	"reflect"
	"runtime"
	"sync"
	"unsafe"
)

// Delim is documented at https://golang.org/pkg/encoding/json/#Delim
type Delim = json.Delim

// InvalidUTF8Error is documented at https://golang.org/pkg/encoding/json/#InvalidUTF8Error
type InvalidUTF8Error = json.InvalidUTF8Error //nolint:staticcheck // compat.

// InvalidUnmarshalError is documented at https://golang.org/pkg/encoding/json/#InvalidUnmarshalError
type InvalidUnmarshalError = json.InvalidUnmarshalError

// Marshaler is documented at https://golang.org/pkg/encoding/json/#Marshaler
type Marshaler = json.Marshaler

// MarshalerError is documented at https://golang.org/pkg/encoding/json/#MarshalerError
type MarshalerError = json.MarshalerError

// Number is documented at https://golang.org/pkg/encoding/json/#Number
type Number = json.Number

// RawMessage is documented at https://golang.org/pkg/encoding/json/#RawMessage
type RawMessage = json.RawMessage

// A SyntaxError is a description of a JSON syntax error.
type SyntaxError = json.SyntaxError

// Token is documented at https://golang.org/pkg/encoding/json/#Token
type Token = json.Token

// UnmarshalFieldError is documented at https://golang.org/pkg/encoding/json/#UnmarshalFieldError
type UnmarshalFieldError = json.UnmarshalFieldError //nolint:staticcheck // compat.

// UnmarshalTypeError is documented at https://golang.org/pkg/encoding/json/#UnmarshalTypeError
type UnmarshalTypeError = json.UnmarshalTypeError

// Unmarshaler is documented at https://golang.org/pkg/encoding/json/#Unmarshaler
type Unmarshaler = json.Unmarshaler

// UnsupportedTypeError is documented at https://golang.org/pkg/encoding/json/#UnsupportedTypeError
type UnsupportedTypeError = json.UnsupportedTypeError

// UnsupportedValueError is documented at https://golang.org/pkg/encoding/json/#UnsupportedValueError
type UnsupportedValueError = json.UnsupportedValueError

// AppendFlags is a type used to represent configuration options that can be
// applied when formatting json output.
type AppendFlags uint32

const (
	// EscapeHTML is a formatting flag used to to escape HTML in json strings.
	EscapeHTML AppendFlags = 1 << iota

	// SortMapKeys is formatting flag used to enable sorting of map keys when
	// encoding JSON (this matches the behavior of the standard encoding/json
	// package).
	SortMapKeys

	// TrustRawMessage is a performance optimization flag to skip value
	// checking of raw messages. It should only be used if the values are
	// known to be valid json (e.g., they were created by json.Unmarshal).
	TrustRawMessage

	// appendNewline is a formatting flag to enable the addition of a newline
	// in Encode (this matches the behavior of the standard encoding/json
	// package).
	appendNewline
)

// ParseFlags is a type used to represent configuration options that can be
// applied when parsing json input.
type ParseFlags uint32

func (flags ParseFlags) has(f ParseFlags) bool {
	return (flags & f) != 0
}

func (f ParseFlags) kind() Kind {
	return Kind((f >> kindOffset) & 0xFF)
}

func (f ParseFlags) withKind(kind Kind) ParseFlags {
	return (f & ^(ParseFlags(0xFF) << kindOffset)) | (ParseFlags(kind) << kindOffset)
}

const (
	// DisallowUnknownFields is a parsing flag used to prevent decoding of
	// objects to Go struct values when a field of the input does not match
	// with any of the struct fields.
	DisallowUnknownFields ParseFlags = 1 << iota

	// UseNumber is a parsing flag used to load numeric values as Number
	// instead of float64.
	UseNumber

	// DontCopyString is a parsing flag used to provide zero-copy support when
	// loading string values from a json payload. It is not always possible to
	// avoid dynamic memory allocations, for example when a string is escaped in
	// the json data a new buffer has to be allocated, but when the `wire` value
	// can be used as content of a Go value the decoder will simply point into
	// the input buffer.
	DontCopyString

	// DontCopyNumber is a parsing flag used to provide zero-copy support when
	// loading Number values (see DontCopyString and DontCopyRawMessage).
	DontCopyNumber

	// DontCopyRawMessage is a parsing flag used to provide zero-copy support
	// when loading RawMessage values from a json payload. When used, the
	// RawMessage values will not be allocated into new memory buffers and
	// will instead point directly to the area of the input buffer where the
	// value was found.
	DontCopyRawMessage

	// DontMatchCaseInsensitiveStructFields is a parsing flag used to prevent
	// matching fields in a case-insensitive way. This can prevent degrading
	// performance on case conversions, and can also act as a stricter decoding
	// mode.
	DontMatchCaseInsensitiveStructFields

	// Decode integers into *big.Int.
	// Takes precedence over UseNumber for integers.
	UseBigInt

	// Decode in-range integers to int64.
	// Takes precedence over UseNumber and UseBigInt for in-range integers.
	UseInt64

	// Decode in-range positive integers to uint64.
	// Takes precedence over UseNumber, UseBigInt, and UseInt64
	// for positive, in-range integers.
	UseUint64

	// ZeroCopy is a parsing flag that combines all the copy optimizations
	// available in the package.
	//
	// The zero-copy optimizations are better used in request-handler style
	// code where none of the values are retained after the handler returns.
	ZeroCopy = DontCopyString | DontCopyNumber | DontCopyRawMessage

	// validAsciiPrint is an internal flag indicating that the input contains
	// only valid ASCII print chars (0x20 <= c <= 0x7E). If the flag is unset,
	// it's unknown whether the input is valid ASCII print.
	validAsciiPrint ParseFlags = 1 << 28

	// noBackslach is an internal flag indicating that the input does not
	// contain a backslash. If the flag is unset, it's unknown whether the
	// input contains a backslash.
	noBackslash ParseFlags = 1 << 29

	// Bit offset where the kind of the json value is stored.
	//
	// See Kind in token.go for the enum.
	kindOffset ParseFlags = 16
)

// Kind represents the different kinds of value that exist in JSON.
type Kind uint

const (
	Undefined Kind = 0

	Null Kind = 1 // Null is not zero, so we keep zero for "undefined".

	Bool  Kind = 2 // Bit two is set to 1, means it's a boolean.
	False Kind = 2 // Bool + 0
	True  Kind = 3 // Bool + 1

	Num   Kind = 4 // Bit three is set to 1, means it's a number.
	Uint  Kind = 5 // Num + 1
	Int   Kind = 6 // Num + 2
	Float Kind = 7 // Num + 3

	String    Kind = 8 // Bit four is set to 1, means it's a string.
	Unescaped Kind = 9 // String + 1

	Array  Kind = 16 // Equivalent to Delim == '['
	Object Kind = 32 // Equivalent to Delim == '{'
)

// Class returns the class of k.
func (k Kind) Class() Kind { return Kind(1 << uint(bits.Len(uint(k))-1)) }

// Append acts like Marshal but appends the json representation to b instead of
// always reallocating a new slice.
func Append(b []byte, x any, flags AppendFlags) ([]byte, error) {
	if x == nil {
		// Special case for nil values because it makes the rest of the code
		// simpler to assume that it won't be seeing nil pointers.
		return append(b, "null"...), nil
	}

	t := reflect.TypeOf(x)
	p := (*iface)(unsafe.Pointer(&x)).ptr

	cache := cacheLoad()
	c, found := cache[typeid(t)]

	if !found {
		c = constructCachedCodec(t, cache)
	}

	b, err := c.encode(encoder{flags: flags}, b, p)
	runtime.KeepAlive(x)
	return b, err
}

// Escape is a convenience helper to construct an escaped JSON string from s.
// The function escales HTML characters, for more control over the escape
// behavior and to write to a pre-allocated buffer, use AppendEscape.
func Escape(s string) []byte {
	// +10 for extra escape characters, maybe not enough and the buffer will
	// be reallocated.
	b := make([]byte, 0, len(s)+10)
	return AppendEscape(b, s, EscapeHTML)
}

// AppendEscape appends s to b with the string escaped as a JSON value.
// This will include the starting and ending quote characters, and the
// appropriate characters will be escaped correctly for JSON encoding.
func AppendEscape(b []byte, s string, flags AppendFlags) []byte {
	e := encoder{flags: flags}
	b, _ = e.encodeString(b, unsafe.Pointer(&s))
	return b
}

// Unescape is a convenience helper to unescape a JSON value.
// For more control over the unescape behavior and
// to write to a pre-allocated buffer, use AppendUnescape.
func Unescape(s []byte) []byte {
	b := make([]byte, 0, len(s))
	return AppendUnescape(b, s, ParseFlags(0))
}

// AppendUnescape appends s to b with the string unescaped as a JSON value.
// This will remove starting and ending quote characters, and the
// appropriate characters will be escaped correctly as if JSON decoded.
// New space will be reallocated if more space is needed.
func AppendUnescape(b []byte, s []byte, flags ParseFlags) []byte {
	d := decoder{flags: flags}
	buf := new(string)
	d.decodeString(s, unsafe.Pointer(buf))
	return append(b, *buf...)
}

// Compact is documented at https://golang.org/pkg/encoding/json/#Compact
func Compact(dst *bytes.Buffer, src []byte) error {
	return json.Compact(dst, src)
}

// HTMLEscape is documented at https://golang.org/pkg/encoding/json/#HTMLEscape
func HTMLEscape(dst *bytes.Buffer, src []byte) {
	json.HTMLEscape(dst, src)
}

// Indent is documented at https://golang.org/pkg/encoding/json/#Indent
func Indent(dst *bytes.Buffer, src []byte, prefix, indent string) error {
	return json.Indent(dst, src, prefix, indent)
}

// Marshal is documented at https://golang.org/pkg/encoding/json/#Marshal
func Marshal(x any) ([]byte, error) {
	var err error
	buf := encoderBufferPool.Get().(*encoderBuffer)

	if buf.data, err = Append(buf.data[:0], x, EscapeHTML|SortMapKeys); err != nil {
		return nil, err
	}

	b := make([]byte, len(buf.data))
	copy(b, buf.data)
	encoderBufferPool.Put(buf)
	return b, nil
}

// MarshalIndent is documented at https://golang.org/pkg/encoding/json/#MarshalIndent
func MarshalIndent(x any, prefix, indent string) ([]byte, error) {
	b, err := Marshal(x)

	if err == nil {
		tmp := &bytes.Buffer{}
		tmp.Grow(2 * len(b))

		Indent(tmp, b, prefix, indent)
		b = tmp.Bytes()
	}

	return b, err
}

// Unmarshal is documented at https://golang.org/pkg/encoding/json/#Unmarshal
func Unmarshal(b []byte, x any) error {
	r, err := Parse(b, x, 0)
	if len(r) != 0 {
		if _, ok := err.(*SyntaxError); !ok {
			// The encoding/json package prioritizes reporting errors caused by
			// unexpected trailing bytes over other issues; here we emulate this
			// behavior by overriding the error.
			err = syntaxError(r, "invalid character '%c' after top-level value", r[0])
		}
	}
	return err
}

// Parse behaves like Unmarshal but the caller can pass a set of flags to
// configure the parsing behavior.
func Parse(b []byte, x any, flags ParseFlags) ([]byte, error) {
	t := reflect.TypeOf(x)
	p := (*iface)(unsafe.Pointer(&x)).ptr

	d := decoder{flags: flags | internalParseFlags(b)}

	b = skipSpaces(b)

	if t == nil || p == nil || t.Kind() != reflect.Ptr {
		_, r, _, err := d.parseValue(b)
		r = skipSpaces(r)
		if err != nil {
			return r, err
		}
		return r, &InvalidUnmarshalError{Type: t}
	}
	t = t.Elem()

	cache := cacheLoad()
	c, found := cache[typeid(t)]

	if !found {
		c = constructCachedCodec(t, cache)
	}

	r, err := c.decode(d, b, p)
	return skipSpaces(r), err
}

// Valid is documented at https://golang.org/pkg/encoding/json/#Valid
func Valid(data []byte) bool {
	data = skipSpaces(data)
	d := decoder{flags: internalParseFlags(data)}
	_, data, _, err := d.parseValue(data)
	if err != nil {
		return false
	}
	return len(skipSpaces(data)) == 0
}

// Decoder is documented at https://golang.org/pkg/encoding/json/#Decoder
type Decoder struct {
	reader      io.Reader
	buffer      []byte
	remain      []byte
	inputOffset int64
	err         error
	flags       ParseFlags
}

// NewDecoder is documented at https://golang.org/pkg/encoding/json/#NewDecoder
func NewDecoder(r io.Reader) *Decoder { return &Decoder{reader: r} }

// Buffered is documented at https://golang.org/pkg/encoding/json/#Decoder.Buffered
func (dec *Decoder) Buffered() io.Reader {
	return bytes.NewReader(dec.remain)
}

// Decode is documented at https://golang.org/pkg/encoding/json/#Decoder.Decode
func (dec *Decoder) Decode(v any) error {
	raw, err := dec.readValue()
	if err != nil {
		return err
	}
	_, err = Parse(raw, v, dec.flags)
	return err
}

const (
	minBufferSize = 32768
	minReadSize   = 4096
)

// readValue reads one JSON value from the buffer and returns its raw bytes. It
// is optimized for the "one JSON value per line" case.
func (dec *Decoder) readValue() (v []byte, err error) {
	var n int
	var r []byte
	d := decoder{flags: dec.flags}

	for {
		if len(dec.remain) != 0 {
			v, r, _, err = d.parseValue(dec.remain)
			if err == nil {
				dec.remain, n = skipSpacesN(r)
				dec.inputOffset += int64(len(v) + n)
				return
			}
			if len(r) != 0 {
				// Parsing of the next JSON value stopped at a position other
				// than the end of the input buffer, which indicaates that a
				// syntax error was encountered.
				return
			}
		}

		if err = dec.err; err != nil {
			if len(dec.remain) != 0 && err == io.EOF {
				err = io.ErrUnexpectedEOF
			}
			return
		}

		if dec.buffer == nil {
			dec.buffer = make([]byte, 0, minBufferSize)
		} else {
			dec.buffer = dec.buffer[:copy(dec.buffer[:cap(dec.buffer)], dec.remain)]
			dec.remain = nil
		}

		if (cap(dec.buffer) - len(dec.buffer)) < minReadSize {
			buf := make([]byte, len(dec.buffer), 2*cap(dec.buffer))
			copy(buf, dec.buffer)
			dec.buffer = buf
		}

		n, err = io.ReadFull(dec.reader, dec.buffer[len(dec.buffer):cap(dec.buffer)])
		if n > 0 {
			dec.buffer = dec.buffer[:len(dec.buffer)+n]
			if err != nil {
				err = nil
			}
		} else if err == io.ErrUnexpectedEOF {
			err = io.EOF
		}
		dec.remain, n = skipSpacesN(dec.buffer)
		d.flags = dec.flags | internalParseFlags(dec.remain)
		dec.inputOffset += int64(n)
		dec.err = err
	}
}

// DisallowUnknownFields is documented at https://golang.org/pkg/encoding/json/#Decoder.DisallowUnknownFields
func (dec *Decoder) DisallowUnknownFields() { dec.flags |= DisallowUnknownFields }

// UseNumber is documented at https://golang.org/pkg/encoding/json/#Decoder.UseNumber
func (dec *Decoder) UseNumber() { dec.flags |= UseNumber }

// DontCopyString is an extension to the standard encoding/json package
// which instructs the decoder to not copy strings loaded from the json
// payloads when possible.
func (dec *Decoder) DontCopyString() { dec.flags |= DontCopyString }

// DontCopyNumber is an extension to the standard encoding/json package
// which instructs the decoder to not copy numbers loaded from the json
// payloads.
func (dec *Decoder) DontCopyNumber() { dec.flags |= DontCopyNumber }

// DontCopyRawMessage is an extension to the standard encoding/json package
// which instructs the decoder to not allocate RawMessage values in separate
// memory buffers (see the documentation of the DontcopyRawMessage flag for
// more detais).
func (dec *Decoder) DontCopyRawMessage() { dec.flags |= DontCopyRawMessage }

// DontMatchCaseInsensitiveStructFields is an extension to the standard
// encoding/json package which instructs the decoder to not match object fields
// against struct fields in a case-insensitive way, the field names have to
// match exactly to be decoded into the struct field values.
func (dec *Decoder) DontMatchCaseInsensitiveStructFields() {
	dec.flags |= DontMatchCaseInsensitiveStructFields
}

// ZeroCopy is an extension to the standard encoding/json package which enables
// all the copy optimizations of the decoder.
func (dec *Decoder) ZeroCopy() { dec.flags |= ZeroCopy }

// InputOffset returns the input stream byte offset of the current decoder position.
// The offset gives the location of the end of the most recently returned token
// and the beginning of the next token.
func (dec *Decoder) InputOffset() int64 {
	return dec.inputOffset
}

// Encoder is documented at https://golang.org/pkg/encoding/json/#Encoder
type Encoder struct {
	writer io.Writer
	prefix string
	indent string
	buffer *bytes.Buffer
	err    error
	flags  AppendFlags
}

// NewEncoder is documented at https://golang.org/pkg/encoding/json/#NewEncoder
func NewEncoder(w io.Writer) *Encoder {
	return &Encoder{writer: w, flags: EscapeHTML | SortMapKeys | appendNewline}
}

// Encode is documented at https://golang.org/pkg/encoding/json/#Encoder.Encode
func (enc *Encoder) Encode(v any) error {
	if enc.err != nil {
		return enc.err
	}

	var err error
	buf := encoderBufferPool.Get().(*encoderBuffer)

	buf.data, err = Append(buf.data[:0], v, enc.flags)
	if err != nil {
		encoderBufferPool.Put(buf)
		return err
	}

	if (enc.flags & appendNewline) != 0 {
		buf.data = append(buf.data, '\n')
	}
	b := buf.data

	if enc.prefix != "" || enc.indent != "" {
		if enc.buffer == nil {
			enc.buffer = new(bytes.Buffer)
			enc.buffer.Grow(2 * len(buf.data))
		} else {
			enc.buffer.Reset()
		}
		Indent(enc.buffer, buf.data, enc.prefix, enc.indent)
		b = enc.buffer.Bytes()
	}

	if _, err := enc.writer.Write(b); err != nil {
		enc.err = err
	}

	encoderBufferPool.Put(buf)
	return err
}

// SetEscapeHTML is documented at https://golang.org/pkg/encoding/json/#Encoder.SetEscapeHTML
func (enc *Encoder) SetEscapeHTML(on bool) {
	if on {
		enc.flags |= EscapeHTML
	} else {
		enc.flags &= ^EscapeHTML
	}
}

// SetIndent is documented at https://golang.org/pkg/encoding/json/#Encoder.SetIndent
func (enc *Encoder) SetIndent(prefix, indent string) {
	enc.prefix = prefix
	enc.indent = indent
}

// SetSortMapKeys is an extension to the standard encoding/json package which
// allows the program to toggle sorting of map keys on and off.
func (enc *Encoder) SetSortMapKeys(on bool) {
	if on {
		enc.flags |= SortMapKeys
	} else {
		enc.flags &= ^SortMapKeys
	}
}

// SetTrustRawMessage skips value checking when encoding a raw json message. It should only
// be used if the values are known to be valid json, e.g. because they were originally created
// by json.Unmarshal.
func (enc *Encoder) SetTrustRawMessage(on bool) {
	if on {
		enc.flags |= TrustRawMessage
	} else {
		enc.flags &= ^TrustRawMessage
	}
}

// SetAppendNewline is an extension to the standard encoding/json package which
// allows the program to toggle the addition of a newline in Encode on or off.
func (enc *Encoder) SetAppendNewline(on bool) {
	if on {
		enc.flags |= appendNewline
	} else {
		enc.flags &= ^appendNewline
	}
}

var encoderBufferPool = sync.Pool{
	New: func() any { return &encoderBuffer{data: make([]byte, 0, 4096)} },
}

type encoderBuffer struct{ data []byte }
```

## File: `json/json_test.go`
```go
package json

import (
	"bytes"
	"compress/gzip"
	"encoding"
	"encoding/json"
	"errors"
	"flag"
	"fmt"
	"io"
	"math"
	"math/big"
	"os"
	"path/filepath"
	"reflect"
	"runtime"
	"strconv"
	"strings"
	"testing"
	"time"
)

// The encoding/json package does not export the msg field of json.SyntaxError,
// so we use this replacement type in tests.
type testSyntaxError struct {
	msg    string
	Offset int64
}

func (e *testSyntaxError) Error() string { return e.msg }

var (
	marshal    func([]byte, any) ([]byte, error)
	unmarshal  func([]byte, any) error
	escapeHTML bool
)

func TestMain(m *testing.M) {
	var pkg string
	flag.StringVar(&pkg, "package", ".", "The name of the package to test (encoding/json, or default to this package)")
	flag.BoolVar(&escapeHTML, "escapehtml", false, "Whether to enable HTML escaping or not")
	flag.Parse()

	switch pkg {
	case "encoding/json":
		buf := &buffer{}
		enc := json.NewEncoder(buf)
		enc.SetEscapeHTML(escapeHTML)

		marshal = func(b []byte, v any) ([]byte, error) {
			buf.data = b
			err := enc.Encode(v)
			return buf.data, err
		}

		unmarshal = json.Unmarshal

	default:
		flags := AppendFlags(0)
		if escapeHTML {
			flags |= EscapeHTML
		}

		marshal = func(b []byte, v any) ([]byte, error) {
			return Append(b, v, flags)
		}

		unmarshal = func(b []byte, v any) error {
			_, err := Parse(b, v, ZeroCopy)
			return err
		}
	}

	os.Exit(m.Run())
}

type point struct {
	X int `json:"x"`
	Y int `json:"y"`
}

type tree struct {
	Value string
	Left  *tree
	Right *tree
}

var (
	// bigPos128 and bigNeg128 are 1<<128 and -1<<128
	// certainly neither is representable using a uint64/int64.
	bigPos128 = new(big.Int).Lsh(big.NewInt(1), 128)
	bigNeg128 = new(big.Int).Neg(bigPos128)
)

var testValues = [...]any{
	// constants
	nil,
	false,
	true,

	// int
	int(0),
	int(1),
	int(42),
	int(-1),
	int(-42),
	int8(math.MaxInt8),
	int8(math.MinInt8),
	int16(math.MaxInt16),
	int16(math.MinInt16),
	int32(math.MaxInt32),
	int32(math.MinInt32),
	int64(math.MaxInt64),
	int64(math.MinInt64),

	// uint
	uint(0),
	uint(1),
	uintptr(0),
	uintptr(1),
	uint8(math.MaxUint8),
	uint16(math.MaxUint16),
	uint32(math.MaxUint32),
	uint64(math.MaxUint64),

	// float
	float32(0),
	float32(0.5),
	float32(math.SmallestNonzeroFloat32),
	float32(math.MaxFloat32),
	float64(0),
	float64(0.5),
	float64(math.SmallestNonzeroFloat64),
	float64(math.MaxFloat64),

	bigPos128,
	bigNeg128,

	// number
	Number("0"),
	Number("1234567890"),
	Number("-0.5"),
	Number("-1e+2"),

	// string
	"",
	"Hello World!",
	"Hello\"World!",
	"Hello\\World!",
	"Hello\nWorld!",
	"Hello\rWorld!",
	"Hello\tWorld!",
	"Hello\bWorld!",
	"Hello\fWorld!",
	"你好",
	"<",
	">",
	"&",
	"\u001944",
	"\u00c2e>",
	"\u00c2V?",
	"\u000e=8",
	"\u001944\u00c2e>\u00c2V?\u000e=8",
	"ir\u001bQJ\u007f\u0007y\u0015)",
	strings.Repeat("A", 32),
	strings.Repeat("A", 250),
	strings.Repeat("A", 1020),

	// bytes
	[]byte(""),
	[]byte("Hello World!"),
	bytes.Repeat([]byte("A"), 250),
	bytes.Repeat([]byte("A"), 1020),

	// time
	time.Unix(0, 0).In(time.UTC),
	time.Unix(1, 42).In(time.UTC),
	time.Unix(17179869184, 999999999).In(time.UTC),
	time.Date(2016, 12, 20, 0, 20, 1, 0, time.UTC),

	// array
	[...]int{},
	[...]int{0, 1, 2, 3, 4, 5, 6, 7, 8, 9},

	// slice
	[]int{},
	[]int{0, 1, 2, 3, 4, 5, 6, 7, 8, 9},
	makeSlice(250),
	makeSlice(1020),
	[]string{"A", "B", "C"},
	[]any{nil, true, false, 0.5, "Hello World!"},

	// map
	makeMapStringBool(0),
	makeMapStringBool(15),
	makeMapStringBool(1020),
	makeMapStringString(0),
	makeMapStringString(15),
	makeMapStringString(1020),
	makeMapStringStringSlice(0),
	makeMapStringStringSlice(15),
	makeMapStringStringSlice(1020),
	makeMapStringInterface(0),
	makeMapStringInterface(15),
	makeMapStringInterface(1020),
	map[int]bool{1: false, 42: true},
	map[textValue]bool{{1, 2}: true, {3, 4}: false},
	map[string]*point{
		"A": {1, 2},
		"B": {3, 4},
		"C": {5, 6},
	},
	map[string]RawMessage{
		"A": RawMessage(`{}`),
		"B": RawMessage(`null`),
		"C": RawMessage(`42`),
	},

	// struct
	struct{}{},
	struct{ A int }{42},
	struct{ A, B, C int }{1, 2, 3},
	struct {
		A int
		T time.Time
		S string
	}{42, time.Date(2016, 12, 20, 0, 20, 1, 0, time.UTC), "Hello World!"},
	// These types are interesting because they fit in a pointer so the compiler
	// puts their value directly into the pointer field of the any that
	// is passed to Marshal.
	struct{ X *int }{},
	struct{ X *int }{new(int)},
	struct{ X **int }{},
	// Struct types with more than one pointer, those exercise the regular
	// pointer handling with code that dereferences the fields.
	struct{ X, Y *int }{},
	struct{ X, Y *int }{new(int), new(int)},
	struct {
		A string         `json:"name"`
		B string         `json:"-"`
		C string         `json:",omitempty"`
		D map[string]any `json:",string"` //nolint:staticcheck // intentional
		e string
	}{A: "Luke", D: map[string]any{"answer": float64(42)}},
	struct{ point }{point{1, 2}},
	tree{
		Value: "T",
		Left:  &tree{Value: "L"},
		Right: &tree{Value: "R", Left: &tree{Value: "R-L"}},
	},

	// pointer
	(*string)(nil),
	new(int),

	// Marshaler/Unmarshaler
	jsonValue{},
	jsonValue{1, 2},

	// encoding.TextMarshaler/encoding.TextUnmarshaler
	textValue{},
	textValue{1, 2},

	// RawMessage
	RawMessage(`{
	"answer": 42,
	"hello": "world"
}`),

	// fixtures
	loadTestdata(filepath.Join(runtime.GOROOT(), "src/encoding/json/testdata/code.json.gz")),
}

var durationTestValues = []any{
	// duration
	time.Nanosecond,
	time.Microsecond,
	time.Millisecond,
	time.Second,
	time.Minute,
	time.Hour,

	// struct with duration
	struct{ D1, D2 time.Duration }{time.Millisecond, time.Hour},
}

func makeSlice(n int) []int {
	s := make([]int, n)
	for i := range s {
		s[i] = i
	}
	return s
}

func makeMapStringBool(n int) map[string]bool {
	m := make(map[string]bool, n)
	for i := range n {
		m[strconv.Itoa(i)] = true
	}
	return m
}

func makeMapStringString(n int) map[string]string {
	m := make(map[string]string, n)
	for i := range n {
		m[strconv.Itoa(i)] = fmt.Sprintf("%d Hello, world!", i)
	}
	return m
}

func makeMapStringStringSlice(n int) map[string][]string {
	m := make(map[string][]string, n)
	for i := range n {
		m[strconv.Itoa(i)] = []string{strconv.Itoa(i), "Hello,", "world!"}
	}
	return m
}

func makeMapStringInterface(n int) map[string]any {
	m := make(map[string]any, n)
	for i := range n {
		m[strconv.Itoa(i)] = nil
	}
	return m
}

func testName(v any) string {
	return fmt.Sprintf("%T", v)
}

type codeResponse2 struct {
	Tree     *codeNode2 `json:"tree"`
	Username string     `json:"username"`
}

type codeNode2 struct {
	Name     string      `json:"name"`
	Kids     []*codeNode `json:"kids"`
	CLWeight float64     `json:"cl_weight"`
	Touches  int         `json:"touches"`
	MinT     int64       `json:"min_t"`
	MaxT     int64       `json:"max_t"`
	MeanT    int64       `json:"mean_t"`
}

func loadTestdata(path string) any {
	f, err := os.Open(path)
	if err != nil {
		return err.Error()
	}
	defer f.Close()

	r, err := gzip.NewReader(f)
	if err != nil {
		return err.Error()
	}
	defer r.Close()

	testdata := new(codeResponse2)
	if err := json.NewDecoder(r).Decode(testdata); err != nil {
		return err.Error()
	}
	return testdata
}

func TestCodec(t *testing.T) {
	for _, v1 := range testValues {
		t.Run(testName(v1), func(t *testing.T) {
			v2 := newValue(v1)

			a, err := json.MarshalIndent(v1, "", "\t")
			if err != nil {
				t.Error(err)
				return
			}
			a = append(a, '\n')

			buf := &bytes.Buffer{}
			enc := NewEncoder(buf)
			enc.SetIndent("", "\t")

			if err := enc.Encode(v1); err != nil {
				t.Error(err)
				return
			}
			b := buf.Bytes()

			if !Valid(b) {
				t.Error("invalid JSON representation")
			}

			if !bytes.Equal(a, b) {
				t.Error("JSON representations mismatch")
				t.Log("expected:", string(a))
				t.Log("found:   ", string(b))
			}

			dec := NewDecoder(bytes.NewBuffer(b))

			if err := dec.Decode(v2.Interface()); err != nil {
				t.Errorf("%T: %v", err, err)
				return
			}

			x1 := v1
			x2 := v2.Elem().Interface()

			if !reflect.DeepEqual(x1, x2) {
				t.Error("values mismatch")
				t.Logf("expected: %#v", x1)
				t.Logf("found:    %#v", x2)
			}

			if b, err := io.ReadAll(dec.Buffered()); err != nil {
				t.Error(err)
			} else if len(b) != 0 {
				t.Errorf("leftover trailing bytes in the decoder: %q", b)
			}
		})
	}
}

// TestCodecDuration isolates testing of time.Duration.  The stdlib un/marshals
// this type as integers whereas this library un/marshals formatted string
// values.  Therefore, plugging durations into TestCodec would cause fail since
// it checks equality on the marshaled strings from the two libraries.
func TestCodecDuration(t *testing.T) {
	for _, v1 := range durationTestValues {
		t.Run(testName(v1), func(t *testing.T) {
			v2 := newValue(v1)

			// encode using stdlib. (will be an int)
			std, err := json.MarshalIndent(v1, "", "\t")
			if err != nil {
				t.Error(err)
				return
			}
			std = append(std, '\n')

			// decode using our decoder. (reads int to duration)
			dec := NewDecoder(bytes.NewBuffer([]byte(std)))

			if err := dec.Decode(v2.Interface()); err != nil {
				t.Errorf("%T: %v", err, err)
				return
			}

			x1 := v1
			x2 := v2.Elem().Interface()

			if !reflect.DeepEqual(x1, x2) {
				t.Error("values mismatch")
				t.Logf("expected: %#v", x1)
				t.Logf("found:    %#v", x2)
			}

			// encoding using our encoder. (writes duration as string)
			buf := &bytes.Buffer{}
			enc := NewEncoder(buf)
			enc.SetIndent("", "\t")

			if err := enc.Encode(v1); err != nil {
				t.Error(err)
				return
			}
			b := buf.Bytes()

			if !Valid(b) {
				t.Error("invalid JSON representation")
			}

			if reflect.DeepEqual(std, b) {
				t.Error("encoded durations should not match stdlib")
				t.Logf("got: %s", b)
			}

			// decode using our decoder. (reads string to duration)
			dec = NewDecoder(bytes.NewBuffer([]byte(std)))

			if err := dec.Decode(v2.Interface()); err != nil {
				t.Errorf("%T: %v", err, err)
				return
			}

			x1 = v1
			x2 = v2.Elem().Interface()

			if !reflect.DeepEqual(x1, x2) {
				t.Error("values mismatch")
				t.Logf("expected: %#v", x1)
				t.Logf("found:    %#v", x2)
			}
		})
	}
}

var numericParseTests = [...]struct {
	name  string
	input string
	flags ParseFlags
	want  any
}{
	{
		name:  "zero_flags_default",
		input: `0`,
		flags: 0,
		want:  float64(0),
	},
	{
		name:  "zero_flags_int_uint_bigint_number",
		input: `0`,
		flags: UseInt64 | UseUint64 | UseBigInt | UseNumber,
		want:  uint64(0),
	},
	{
		name:  "zero_flags_int_bigint_number",
		input: `0`,
		flags: UseInt64 | UseBigInt | UseNumber,
		want:  int64(0),
	},
	{
		name:  "zero_flags_bigint_number",
		input: `0`,
		flags: UseBigInt | UseNumber,
		want:  big.NewInt(0),
	},
	{
		name:  "zero_flags_number",
		input: `0`,
		flags: UseNumber,
		want:  json.Number(`0`),
	},
	{
		name:  "max_uint64_flags_default",
		input: fmt.Sprint(uint64(math.MaxUint64)),
		flags: 0,
		want:  float64(math.MaxUint64),
	},
	{
		name:  "max_uint64_flags_int_uint_bigint_number",
		input: fmt.Sprint(uint64(math.MaxUint64)),
		flags: UseInt64 | UseUint64 | UseBigInt | UseNumber,
		want:  uint64(math.MaxUint64),
	},
	{
		name:  "min_int64_flags_uint_int_bigint_number",
		input: fmt.Sprint(int64(math.MinInt64)),
		flags: UseInt64 | UseBigInt | UseNumber,
		want:  int64(math.MinInt64),
	},
	{
		name:  "max_uint64_flags_int_bigint_number",
		input: fmt.Sprint(uint64(math.MaxUint64)),
		flags: UseInt64 | UseBigInt | UseNumber,
		want:  new(big.Int).SetUint64(math.MaxUint64),
	},
	{
		name:  "overflow_uint64_flags_uint_int_bigint_number",
		input: bigPos128.String(),
		flags: UseUint64 | UseInt64 | UseBigInt | UseNumber,
		want:  bigPos128,
	},
	{
		name:  "underflow_uint64_flags_uint_int_bigint_number",
		input: bigNeg128.String(),
		flags: UseUint64 | UseInt64 | UseBigInt | UseNumber,
		want:  bigNeg128,
	},
	{
		name:  "overflow_uint64_flags_uint_int_number",
		input: bigPos128.String(),
		flags: UseUint64 | UseInt64 | UseNumber,
		want:  json.Number(bigPos128.String()),
	},
	{
		name:  "underflow_uint64_flags_uint_int_number",
		input: bigNeg128.String(),
		flags: UseUint64 | UseInt64 | UseNumber,
		want:  json.Number(bigNeg128.String()),
	},
	{
		name:  "overflow_uint64_flags_uint_int",
		input: bigPos128.String(),
		flags: UseUint64 | UseInt64,
		want:  float64(1 << 128),
	},
	{
		name:  "underflow_uint64_flags_uint_int",
		input: bigNeg128.String(),
		flags: UseUint64 | UseInt64,
		want:  float64(-1 << 128),
	},
}

func TestParse_numeric(t *testing.T) {
	t.Parallel()

	for _, test := range numericParseTests {
		test := test

		t.Run(test.name, func(t *testing.T) {
			t.Parallel()

			var got any

			rem, err := Parse([]byte(test.input), &got, test.flags)
			if err != nil {
				format := "Parse(%#q, ..., %#b) = %q [error], want nil"
				t.Errorf(format, test.input, test.flags, err)
			}

			if len(rem) != 0 {
				format := "Parse(%#q, ..., %#b) = %#q, want zero length"
				t.Errorf(format, test.input, test.flags, rem)
			}

			if !reflect.DeepEqual(got, test.want) {
				format := "Parse(%#q, %#b) -> %T(%#[3]v), want %T(%#[4]v)"
				t.Errorf(format, test.input, test.flags, got, test.want)
			}
		})
	}
}

func newValue(model any) reflect.Value {
	if model == nil {
		return reflect.New(reflect.TypeOf(&model).Elem())
	}
	return reflect.New(reflect.TypeOf(model))
}

func BenchmarkMarshal(b *testing.B) {
	j := make([]byte, 0, 128*1024)

	for _, v := range testValues {
		b.Run(testName(v), func(b *testing.B) {
			if marshal == nil {
				return
			}

			for range b.N {
				j, _ = marshal(j[:0], v)
			}

			b.SetBytes(int64(len(j)))
		})
	}
}

func BenchmarkUnmarshal(b *testing.B) {
	for _, v := range testValues {
		b.Run(testName(v), func(b *testing.B) {
			if unmarshal == nil {
				return
			}

			x := v
			if d, ok := x.(time.Duration); ok {
				x = duration(d)
			}

			j, _ := json.Marshal(x)
			x = newValue(v).Interface()

			for range b.N {
				unmarshal(j, x)
			}

			b.SetBytes(int64(len(j)))
		})
	}
}

type buffer struct{ data []byte }

func (buf *buffer) Write(b []byte) (int, error) {
	buf.data = append(buf.data, b...)
	return len(b), nil
}

func (buf *buffer) WriteString(s string) (int, error) {
	buf.data = append(buf.data, s...)
	return len(s), nil
}

type jsonValue struct {
	x int32
	y int32
}

func (v jsonValue) MarshalJSON() ([]byte, error) {
	return Marshal([2]int32{v.x, v.y})
}

func (v *jsonValue) UnmarshalJSON(b []byte) error {
	var a [2]int32
	err := Unmarshal(b, &a)
	v.x = a[0]
	v.y = a[1]
	return err
}

type textValue struct {
	x int32
	y int32
}

func (v textValue) MarshalText() ([]byte, error) {
	return []byte(fmt.Sprintf("(%d,%d)", v.x, v.y)), nil
}

func (v *textValue) UnmarshalText(b []byte) error {
	_, err := fmt.Sscanf(string(b), "(%d,%d)", &v.x, &v.y)
	return err
}

type duration time.Duration

func (d duration) MarshalJSON() ([]byte, error) {
	return []byte(`"` + time.Duration(d).String() + `"`), nil
}

func (d *duration) UnmarshalJSON(b []byte) error {
	var s string
	if err := json.Unmarshal(b, &s); err != nil {
		return err
	}
	x, err := time.ParseDuration(s)
	*d = duration(x)
	return err
}

var (
	_ Marshaler = jsonValue{}
	_ Marshaler = duration(0)

	_ encoding.TextMarshaler = textValue{}

	_ Unmarshaler = (*jsonValue)(nil)
	_ Unmarshaler = (*duration)(nil)

	_ encoding.TextUnmarshaler = (*textValue)(nil)
)

func TestDecodeStructFieldCaseInsensitive(t *testing.T) {
	b := []byte(`{ "type": "changed" }`)
	s := struct {
		Type string
	}{"unchanged"}

	if err := Unmarshal(b, &s); err != nil {
		t.Error(err)
	}

	if s.Type != "changed" {
		t.Error("s.Type: expected to be changed but found", s.Type)
	}
}

func TestDecodeLines(t *testing.T) {
	tests := []struct {
		desc        string
		reader      io.Reader
		expectCount int
	}{
		// simple

		{
			desc:        "bare object",
			reader:      strings.NewReader("{\"Good\":true}"),
			expectCount: 1,
		},
		{
			desc:        "multiple objects on one line",
			reader:      strings.NewReader("{\"Good\":true}{\"Good\":true}\n"),
			expectCount: 2,
		},
		{
			desc:        "object spanning multiple lines",
			reader:      strings.NewReader("{\n\"Good\":true\n}\n"),
			expectCount: 1,
		},

		// whitespace handling

		{
			desc:        "trailing newline",
			reader:      strings.NewReader("{\"Good\":true}\n{\"Good\":true}\n"),
			expectCount: 2,
		},
		{
			desc:        "multiple trailing newlines",
			reader:      strings.NewReader("{\"Good\":true}\n{\"Good\":true}\n\n"),
			expectCount: 2,
		},
		{
			desc:        "blank lines",
			reader:      strings.NewReader("{\"Good\":true}\n\n{\"Good\":true}"),
			expectCount: 2,
		},
		{
			desc:        "no trailing newline",
			reader:      strings.NewReader("{\"Good\":true}\n{\"Good\":true}"),
			expectCount: 2,
		},
		{
			desc:        "leading whitespace",
			reader:      strings.NewReader("  {\"Good\":true}\n\t{\"Good\":true}"),
			expectCount: 2,
		},

		// multiple reads

		{
			desc: "one object, multiple reads",
			reader: io.MultiReader(
				strings.NewReader("{"),
				strings.NewReader("\"Good\": true"),
				strings.NewReader("}\n"),
			),
			expectCount: 1,
		},

		// EOF reads

		{
			desc:        "one object + EOF",
			reader:      &eofReader{"{\"Good\":true}\n"},
			expectCount: 1,
		},
		{
			desc:        "leading whitespace + EOF",
			reader:      &eofReader{"\n{\"Good\":true}\n"},
			expectCount: 1,
		},
		{
			desc:        "multiple objects + EOF",
			reader:      &eofReader{"{\"Good\":true}\n{\"Good\":true}\n"},
			expectCount: 2,
		},
		{
			desc: "one object + multiple reads + EOF",
			reader: io.MultiReader(
				strings.NewReader("{"),
				strings.NewReader("  \"Good\": true"),
				&eofReader{"}\n"},
			),
			expectCount: 1,
		},
		{
			desc: "multiple objects + multiple reads + EOF",
			reader: io.MultiReader(
				strings.NewReader("{"),
				strings.NewReader("  \"Good\": true}{\"Good\": true}"),
				&eofReader{"\n"},
			),
			expectCount: 2,
		},

		{
			// the 2nd object should be discarded, as 42 cannot be cast to bool
			desc:        "unmarshal error while decoding",
			reader:      strings.NewReader("{\"Good\":true}\n{\"Good\":42}\n{\"Good\":true}\n"),
			expectCount: 2,
		},
		{
			// the 2nd object should be discarded, as 42 cannot be cast to bool
			desc:        "unmarshal error while decoding last object",
			reader:      strings.NewReader("{\"Good\":true}\n{\"Good\":42}\n"),
			expectCount: 1,
		},
	}

	type obj struct {
		Good bool
	}

	for _, test := range tests {
		t.Run(test.desc, func(t *testing.T) {
			d := NewDecoder(test.reader)
			var count int
			for {
				var o obj
				err := d.Decode(&o)
				if err != nil {
					if errors.Is(err, io.EOF) {
						break
					}

					switch err.(type) {
					case *SyntaxError, *UnmarshalTypeError, *UnmarshalFieldError:
						t.Log("unmarshal error", err)
						continue
					}

					t.Error("decode error", err)
					break
				}
				if !o.Good {
					t.Errorf("object was not unmarshaled correctly: %#v", o)
				}
				count++
			}

			if count != test.expectCount {
				t.Errorf("expected %d objects, got %d", test.expectCount, count)
			}
		})
	}
}

// eofReader is a simple io.Reader that reads its full contents _and_ returns
// and EOF in the first call. Subsequent Read calls only return EOF.
type eofReader struct {
	s string
}

func (r *eofReader) Read(p []byte) (n int, err error) {
	n = copy(p, r.s)
	r.s = r.s[n:]
	if r.s == "" {
		err = io.EOF
	}
	return
}

func TestDontMatchCaseIncensitiveStructFields(t *testing.T) {
	b := []byte(`{ "type": "changed" }`)
	s := struct {
		Type string
	}{"unchanged"}

	if _, err := Parse(b, &s, DontMatchCaseInsensitiveStructFields); err != nil {
		t.Error(err)
	}

	if s.Type != "unchanged" {
		t.Error("s.Type: expected to be unchanged but found", s.Type)
	}
}

func TestMarshalFuzzBugs(t *testing.T) {
	tests := []struct {
		value  any
		output string
	}{
		{ // html sequences are escaped even in RawMessage
			value: struct {
				P RawMessage
			}{P: RawMessage(`"<"`)},
			output: "{\"P\":\"\\u003c\"}",
		},
		{ // raw message output is compacted
			value: struct {
				P RawMessage
			}{P: RawMessage(`{"" :{}}`)},
			output: "{\"P\":{\"\":{}}}",
		},
	}

	for _, test := range tests {
		t.Run("", func(t *testing.T) {
			b, err := Marshal(test.value)
			if err != nil {
				t.Fatal(err)
			}

			if string(b) != test.output {
				t.Error("values mismatch")
				t.Logf("expected: %#v", test.output)
				t.Logf("found:    %#v", string(b))
			}
		})
	}
}

func TestUnmarshalFuzzBugs(t *testing.T) {
	tests := []struct {
		input string
		value any
	}{
		{ // non-UTF8 sequences must be converted to the utf8.RuneError character.
			input: "[\"00000\xef\"]",
			value: []any{"00000�"},
		},
		{ // UTF16 surrogate followed by null character
			input: "[\"\\ud800\\u0000\"]",
			value: []any{"�\x00"},
		},
		{ // UTF16 surrogate followed by ascii character
			input: "[\"\\uDF00\\u000e\"]",
			value: []any{"�\x0e"},
		},
		{ // UTF16 surrogate followed by unicode character
			input: "[[\"\\uDF00\\u0800\"]]",
			value: []any{[]any{"�ࠀ"}},
		},
		{ // invalid UTF16 surrogate sequenced followed by a valid UTF16 surrogate sequence
			input: "[\"\\udf00\\udb00\\udf00\"]",
			value: []any{"�\U000d0300"},
		},
		{ // decode single-element slice into []byte field
			input: "{\"f\":[0],\"0\":[0]}",
			value: struct{ F []byte }{F: []byte{0}},
		},
		{ // decode multi-element slice into []byte field
			input: "{\"F\":[3,1,1,1,9,9]}",
			value: struct{ F []byte }{F: []byte{3, 1, 1, 1, 9, 9}},
		},
		{ // decode string with escape sequence into []byte field
			input: "{\"F\":\"0p00\\r\"}",
			value: struct{ F []byte }{F: []byte("ҝ4")},
		},
		{ // decode unicode code points which fold into ascii characters
			input: "{\"ſ\":\"8\"}",
			value: struct {
				S int `json:",string"`
			}{S: 8},
		},
		{ // decode unicode code points which don't fold into ascii characters
			input: "{\"İ\":\"\"}",
			value: struct{ I map[string]string }{I: nil},
		},
		{ // override pointer-to-pointer field clears the inner pointer only
			input: "{\"o\":0,\"o\":null}",
			value: struct{ O **int }{O: new(*int)},
		},
		{ // subsequent occurrences of a map field retain keys previously loaded
			input: "{\"i\":{\"\":null},\"i\":{}}",
			value: struct{ I map[string]string }{I: map[string]string{"": ""}},
		},
		{ // an empty string is an invalid JSON input
			input: "",
		},
		{ // ASCII character below 0x20 are invalid JSON input
			input: "[\"\b\"]",
		},
		{ // random byte before any value
			input: "\xad",
		},
		{ // cloud be the beginning of a false value but not
			input: "f",
			value: false,
		},
		{ // random ASCII character
			input: "}",
			value: []any{},
		},
		{ // random byte after valid JSON, decoded to a nil type
			input: "0\x93",
		},
		{ // random byte after valid JSON, decoded to a int type
			input: "0\x93",
			value: 0,
		},
		{ // random byte after valid JSON, decoded to a slice type
			input: "0\x93",
			value: []any{},
		},
		{ // decode integer into slice
			input: "0",
			value: []any{},
		},
		{ // decode integer with trailing space into slice
			input: "0\t",
			value: []any{},
		},
		{ // decode integer with leading random bytes into slice
			input: "\b0",
			value: []any{},
		},
		{ // decode string into slice followed by number
			input: "\"\"0",
			value: []any{},
		},
		{ // decode what looks like an object followed by a number into a string
			input: "{0",
			value: "",
		},
		{ // decode what looks like an object followed by a number into a map
			input: "{0",
			value: map[string]string{},
		},
		{ // decode string into string with trailing random byte
			input: "\"\"\f",
			value: "",
		},
		{ // decode weird number value into nil
			input: "-00",
		},
		{ // decode an invalid escaped sequence
			input: "\"\\0\"",
			value: "",
		},
		{ // decode what looks like an array followed by a number into a slice
			input: "[9E600",
			value: []any{},
		},
		{ // decode a number which is too large to fit in a float64
			input: "[1e900]",
			value: []any{},
		},
		{ // many nested arrays openings
			input: "[[[[[[",
			value: []any{},
		},
		{ // decode a map with value type mismatch and missing closing character
			input: "{\"\":0",
			value: map[string]string{},
		},
		{ // decode a struct with value type mismatch and missing closing character
			input: "{\"E\":\"\"",
			value: struct{ E uint8 }{},
		},
		{ // decode a map with value type mismatch
			input: "{\"\":0}",
			value: map[string]string{},
		},
		{ // decode number with exponent into integer field
			input: "{\"e\":0e0}",
			value: struct{ E uint8 }{},
		},
		{ // decode invalid integer representation into integer field
			input: "{\"e\":00}",
			value: struct{ E uint8 }{},
		},
		{ // decode unterminated array into byte slice
			input: "{\"F\":[",
			value: struct{ F []byte }{},
		},
		{ // attempt to decode string into in
			input: "{\"S\":\"\"}",
			value: struct {
				S int `json:",string"`
			}{},
		},
		{ // decode object with null key into map
			input: "{null:0}",
			value: map[string]any{},
		},
		{ // decode unquoted integer into struct field with string tag
			input: "{\"S\":0}",
			value: struct {
				S int `json:",string"`
			}{},
		},
		{ // invalid base64 content when decoding string into byte slice
			input: "{\"F\":\"0\"}",
			value: struct{ F []byte }{},
		},
		{ // decode an object with a "null" string as key
			input: "{\"null\":null}",
			value: struct {
				S int `json:",string"`
			}{},
		},
		{ // decode an invalid floating point number representation into an integer field with string tag
			input: "{\"s\":8e800}",
			value: struct {
				S int `json:",string"`
			}{},
		},
		{ // decode a string with leading zeroes into an integer field with string tag
			input: "{\"S\":\"00\"}",
			value: struct {
				S int `json:",string"`
			}{},
		},
		{ // decode a string with invalid leading sign and zeroes into an integer field with string tag
			input: "{\"S\":\"+00\"}",
			value: struct {
				S int `json:",string"`
			}{},
		},
		{ // decode a string with valid leading sign and zeroes into an integer field with string tag
			input: "{\"S\":\"-00\"}",
			value: struct {
				S int `json:",string"`
			}{},
		},
		{ // decode non-ascii string into integer field with string tag
			input: "{\"ſ\":\"\xbf\"}",
			value: struct {
				S int `json:",string"`
			}{},
		},
		{ // decode a valid floating point number representation into an integer field with string tag
			input: "{\"S\":0.0}",
			value: struct {
				S int `json:",string"`
			}{},
		},
		{ // decode string with invalid leading sign to integer field with string tag
			input: "{\"S\":\"+0\"}",
			value: struct {
				S int `json:",string"`
			}{},
		},
		{ // decode string with valid leading sign to integer field with string tag
			input: "{\"S\":\"-0\"}",
			value: struct {
				S int `json:",string"`
			}{},
		},
		{ // decode string with object representation to integer field with string tag
			input: "{\"s\":{}}",
			value: struct {
				S int `json:",string"`
			}{},
		},
		{ // decoding integer with leading zeroes
			input: "{\"o\":00}",
			value: struct{ O **int }{},
		},
		{ // codeding string with invalid float representation into integer field with string tag
			input: "{\"s\":\"0.\"}",
			value: struct {
				S int `json:",string"`
			}{},
		},
		{ // malformed negative integer in object value
			input: "{\"N\":-00}",
			value: struct{ N *int }{},
		},
		{ // integer overflow
			input: "{\"a\":9223372036854775808}",
			value: struct {
				A int `json:",omitempty"`
			}{},
		},
		{ // decode string with number followed by random byte into integer field with string tag
			input: "{\"s\":\"0]\"}",
			value: struct {
				S int `json:",string"`
			}{},
		},
		{ // decode object into integer field
			input: "{\"n\":{}}",
			value: struct{ N *int }{},
		},
		{ // decode negative integer into unsigned type
			input: "{\"E\":-0}",
			value: struct{ E uint8 }{},
		},
		{ // decode string with number followed by random byte into integer field with string tag
			input: "{\"s\":\"03�\"}",
			value: struct {
				S int `json:",string"`
			}{},
		},
		{ // decode string with leading zeroes into integer field with string tag
			input: "{\"s\":\"03\"}",
			value: struct {
				S int `json:",string"`
			}{S: 3},
		},
		{ // decode string containing what looks like an object into integer field with string tag
			input: "{\"S\":\"{}\"}",
			value: struct {
				S int `json:",string"`
			}{},
		},
		{ // decode an empty string followed by the same field with a null value into a byte slice
			input: "{\"F\":\"\",\"F\":null}",
			value: struct{ F []byte }{},
		},
		{ // decode string containing a float into an integer field with string tag
			input: "{\"S\":\"0e0\"}",
			value: struct {
				S int `json:",string"`
			}{},
		},
		{ // decode string with negative sign into a an integer field with string tag
			input: "{\"s\":\"-\"}",
			value: struct {
				S int `json:",string"`
			}{},
		},
		{ // decode string with positive sign into a an integer field with string tag
			input: "{\"s\":\"+\"}",
			value: struct {
				S int `json:",string"`
			}{},
		},
		{ // decode an integer into a json unmarshaler
			input: "{\"q\":0}",
			value: struct {
				Q testMarshaller
			}{},
		},
		// This test fails because it appears that the encoding/json package
		// will decode "q" before "s", so it returns an error about "q" being of
		// the wrong type while this package will prase object keys in the order
		// that they appear in the JSON input, so it detects the error from "s"
		// first.
		//
		//{
		//	input: "{\"s\":0,\"q\":0}",
		//	value: struct {
		//		Q testMarshaller
		//		S int `json:",string"`
		//	}{},
		//},
	}

	for _, test := range tests {
		t.Run("", func(t *testing.T) {
			var ptr1 any
			var ptr2 any

			if test.value != nil {
				ptr1 = reflect.New(reflect.TypeOf(test.value)).Interface()
				ptr2 = reflect.New(reflect.TypeOf(test.value)).Interface()
			}

			err1 := json.Unmarshal([]byte(test.input), ptr1)
			err2 := Unmarshal([]byte(test.input), ptr2)

			if reflect.TypeOf(err1) != reflect.TypeOf(err2) {
				t.Error("errors mismatch")
				t.Logf("expected: %T: %v", err1, err1)
				t.Logf("found:    %T: %v", err2, err2)
			} else if err1 == nil && test.value != nil {
				if value := reflect.ValueOf(ptr2).Elem().Interface(); !reflect.DeepEqual(test.value, value) {
					t.Error("values mismatch")
					t.Logf("expected: %#v", test.value)
					t.Logf("found:    %#v", value)
				}
			}
		})
	}
}

func BenchmarkEasyjsonUnmarshalSmallStruct(b *testing.B) {
	type Hashtag struct {
		Indices []int  `json:"indices"`
		Text    string `json:"text"`
	}

	//easyjson:json
	type Entities struct {
		Hashtags     []Hashtag `json:"hashtags"`
		Urls         []*string `json:"urls"`
		UserMentions []*string `json:"user_mentions"`
	}

	json := []byte(`{"hashtags":[{"indices":[5, 10],"text":"some-text"}],"urls":[],"user_mentions":[]}`)

	for range b.N {
		var value Entities
		if err := Unmarshal(json, &value); err != nil {
			b.Fatal(err)
		}
	}
}

type testMarshaller struct {
	v string
}

func (m *testMarshaller) MarshalJSON() ([]byte, error) {
	return Marshal(m.v)
}

func (m *testMarshaller) UnmarshalJSON(data []byte) error {
	return Unmarshal(data, &m.v)
}

func TestGithubIssue11(t *testing.T) {
	// https://github.com/segmentio/encoding/issues/11
	v := struct{ F float64 }{
		F: math.NaN(),
	}

	_, err := Marshal(v)
	if err == nil {
		t.Error("no error returned when marshalling NaN value")
	} else if s := err.Error(); !strings.Contains(s, "NaN") {
		t.Error("error returned when marshalling NaN value does not mention 'NaN':", s)
	} else {
		t.Log(s)
	}
}

type Issue13 struct {
	Stringer fmt.Stringer
	Field    int `json:"MyInt"`
}

type S string

func (s S) String() string { return string(s) }

func TestGithubIssue13(t *testing.T) {
	// https://github.com/segmentio/encoding/issues/13
	v := Issue13{}

	b, err := Marshal(v)
	if err != nil {
		t.Error("unexpected errror:", err)
	} else {
		t.Log(string(b))
	}

	v = Issue13{Stringer: S("")}
	if err := Unmarshal([]byte(`{"Stringer":null}`), &v); err != nil {
		t.Error("unexpected error:", err)
	}
	if v.Stringer != nil {
		t.Error("Stringer field was not overwritten")
	}

	v = Issue13{}
	if err := Unmarshal([]byte(`{"Stringer":"whatever"}`), &v); err == nil {
		t.Error("expected error but decoding string value into nil fmt.Stringer but got <nil>")
	}

	v = Issue13{Stringer: S("")}
	if err := Unmarshal([]byte(`{"Stringer":"whatever"}`), &v); err == nil {
		t.Error("expected error but decoding string value into non-pointer fmt.Stringer but got <nil>")
	}

	s := S("")
	v = Issue13{Stringer: &s}
	if err := Unmarshal([]byte(`{"Stringer":"whatever"}`), &v); err != nil {
		t.Error("unexpected error decoding string value into pointer fmt.Stringer:", err)
	}
}

func TestGithubIssue15(t *testing.T) {
	// https://github.com/segmentio/encoding/issues/15
	tests := []struct {
		m any
		s string
	}{
		{
			m: map[uint]bool{1: true, 123: true, 333: true, 42: true},
			s: `{"1":true,"123":true,"333":true,"42":true}`,
		},
		{
			m: map[int]bool{-1: true, -123: true, 333: true, 42: true},
			s: `{"-1":true,"-123":true,"333":true,"42":true}`,
		},
	}

	for _, test := range tests {
		b, _ := Marshal(test.m)

		if string(b) != test.s {
			t.Error("map with integer keys must be ordered by their string representation, got", string(b))
		}

	}
}

type sliceA []byte

func (sliceA) MarshalJSON() ([]byte, error) {
	return []byte(`"A"`), nil
}

type sliceB []byte

func (sliceB) MarshalText() ([]byte, error) {
	return []byte("B"), nil
}

type mapA map[string]string

func (mapA) MarshalJSON() ([]byte, error) {
	return []byte(`"A"`), nil
}

type mapB map[string]string

func (mapB) MarshalText() ([]byte, error) {
	return []byte("B"), nil
}

type intPtrA int

func (*intPtrA) MarshalJSON() ([]byte, error) {
	return []byte(`"A"`), nil
}

type intPtrB int

func (*intPtrB) MarshalText() ([]byte, error) {
	return []byte("B"), nil
}

type (
	structA struct{ I intPtrA }
	structB struct{ I intPtrB }
	structC struct{ M Marshaler }
	structD struct{ M encoding.TextMarshaler }
)

func TestGithubIssue16(t *testing.T) {
	// https://github.com/segmentio/encoding/issues/16
	tests := []struct {
		value  any
		output string
	}{
		{value: sliceA(nil), output: `"A"`},
		{value: sliceB(nil), output: `"B"`},
		{value: mapA(nil), output: `"A"`},
		{value: mapB(nil), output: `"B"`},
		{value: intPtrA(1), output: `1`},
		{value: intPtrB(2), output: `2`},
		{value: new(intPtrA), output: `"A"`},
		{value: new(intPtrB), output: `"B"`},
		{value: (*intPtrA)(nil), output: `null`},
		{value: (*intPtrB)(nil), output: `null`},
		{value: structA{I: 1}, output: `{"I":1}`},
		{value: structB{I: 2}, output: `{"I":2}`},
		{value: structC{}, output: `{"M":null}`},
		{value: structD{}, output: `{"M":null}`},
		{value: &structA{I: 1}, output: `{"I":"A"}`},
		{value: &structB{I: 2}, output: `{"I":"B"}`},
		{value: &structC{}, output: `{"M":null}`},
		{value: &structD{}, output: `{"M":null}`},
	}

	for _, test := range tests {
		t.Run(fmt.Sprintf("%T", test.value), func(t *testing.T) {
			if b, _ := Marshal(test.value); string(b) != test.output {
				t.Errorf(`%s != %s`, string(b), test.output)
			}
		})
	}
}

func TestDecoderInputOffset(t *testing.T) {
	checkOffset := func(o, expected int64) {
		if o != expected {
			t.Error("unexpected input offset", o, expected)
		}
	}

	b := []byte(`{"userId": "blah"}{"userId": "blah"}
	{"userId": "blah"}{"num": 0}`)
	d := NewDecoder(bytes.NewReader(b))

	var expected int64
	checkOffset(d.InputOffset(), expected)

	var a struct {
		UserId string `json:"userId"`
	}

	if err := d.Decode(&a); err != nil {
		t.Error("unexpected decode error", err)
	}
	expected = int64(18)
	checkOffset(d.InputOffset(), expected)

	if err := d.Decode(&a); err != nil {
		t.Error("unexpected decode error", err)
	}
	expected = int64(38)
	checkOffset(d.InputOffset(), expected)

	if err := d.Decode(&a); err != nil {
		t.Error("unexpected decode error", err)
	}
	expected = int64(56)
	checkOffset(d.InputOffset(), expected)

	var z struct {
		Num int64 `json:"num"`
	}
	if err := d.Decode(&z); err != nil {
		t.Error("unexpected decode error", err)
	}
	expected = int64(66)
	checkOffset(d.InputOffset(), expected)
}

func TestGithubIssue18(t *testing.T) {
	// https://github.com/segmentio/encoding/issues/18
	b := []byte(`{
	"userId": "blah",
	}`)

	d := NewDecoder(bytes.NewReader(b))

	var a struct {
		UserId string `json:"userId"`
	}
	switch err := d.Decode(&a).(type) {
	case *SyntaxError:
	default:
		t.Error("expected syntax error but found:", err)
	}

	for i := 1; i <= 18; i++ { // up to the invalid ',' character
		d := NewDecoder(bytes.NewReader(b[:i])) // cut somewhere in the middle
		switch err := d.Decode(&a); err {
		case io.ErrUnexpectedEOF:
		default:
			t.Error("expected 'unexpected EOF' error but found:", err)
		}
	}
}

func TestGithubIssue23(t *testing.T) {
	t.Run("marshal-1", func(t *testing.T) {
		type d struct{ S map[string]string }

		b, _ := Marshal(map[string]d{"1": {S: map[string]string{"2": "3"}}})
		if string(b) != `{"1":{"S":{"2":"3"}}}` {
			t.Error(string(b))
		}
	})

	t.Run("marshal-2", func(t *testing.T) {
		type testInner struct {
			InnerMap map[string]string `json:"inner_map"`
		}

		type testOuter struct {
			OuterMap map[string]testInner `json:"outer_map"`
		}

		b, _ := Marshal(testOuter{
			OuterMap: map[string]testInner{
				"outer": {
					InnerMap: map[string]string{"inner": "value"},
				},
			},
		})

		if string(b) != `{"outer_map":{"outer":{"inner_map":{"inner":"value"}}}}` {
			t.Error(string(b))
		}
	})

	t.Run("marshal-3", func(t *testing.T) {
		type A struct{ A map[string]string }
		type B struct{ B map[string]A }
		type C struct{ C map[string]B }

		b, _ := Marshal(C{
			C: map[string]B{
				"1": {
					B: map[string]A{
						"2": {
							A: map[string]string{"3": "!"},
						},
					},
				},
			},
		})

		if string(b) != `{"C":{"1":{"B":{"2":{"A":{"3":"!"}}}}}}` {
			t.Error(string(b))
		}
	})

	t.Run("unmarshal-1", func(t *testing.T) {
		var d struct{ S map[string]string }

		if err := Unmarshal([]byte(`{"1":{"S":{"2":"3"}}}`), &d); err != nil {
			t.Error(err)
		}
	})
}

func TestGithubIssue26(t *testing.T) {
	type interfaceType any

	var value interfaceType
	data := []byte(`{}`)

	if err := Unmarshal(data, &value); err != nil {
		t.Error(err)
	}
}

func TestGithubIssue28(t *testing.T) {
	type A struct {
		Err error `json:"err"`
	}

	if b, err := Marshal(&A{Err: errors.New("ABC")}); err != nil {
		t.Error(err)
	} else if string(b) != `{"err":{}}` {
		t.Error(string(b))
	}
}

func TestGithubIssue41(t *testing.T) {
	expectedString := `{"Zero":0,"Three":3}`
	type M struct {
		One int
		Two int
	}
	type N struct {
		Zero int
		*M
		Three int
	}

	if b, err := Marshal(N{Three: 3}); err != nil {
		t.Error(err)
	} else if string(b) != expectedString {
		t.Error(
			"got: ", string(b),
			"expected: ", expectedString,
		)
	}
}

func TestGithubIssue44(t *testing.T) {
	var out rawJsonString
	if err := Unmarshal([]byte("null"), &out); err != nil {
		t.Fatal(err)
	}
	if out != "null" {
		t.Errorf("wanted \"null\" but got %q", out)
	}
}

type issue107Foo struct {
	Bar *issue107Bar
}

type issue107Bar struct {
	Foo *issue107Foo
}

func TestGithubIssue107(t *testing.T) {
	f := &issue107Foo{}
	b := &issue107Bar{}
	f.Bar = b
	b.Foo = f

	_, err := Marshal(f) // must not crash
	switch err.(type) {
	case *UnsupportedValueError:
	default:
		t.Errorf("marshaling a cycling data structure was expected to return an unsupported value error but got %T", err)
	}
}

type rawJsonString string

func (r *rawJsonString) UnmarshalJSON(b []byte) error {
	if len(b) == 0 {
		*r = "null"
	} else {
		*r = rawJsonString(b)
	}
	return nil
}

func TestSetTrustRawMessage(t *testing.T) {
	buf := &bytes.Buffer{}
	enc := NewEncoder(buf)
	enc.SetTrustRawMessage(true)

	// "Good" values are encoded in the regular way
	m := map[string]json.RawMessage{
		"k": json.RawMessage(`"value"`),
	}
	if err := enc.Encode(m); err != nil {
		t.Error(err)
	}

	b := buf.Bytes()
	exp := []byte(`{"k":"value"}`)
	exp = append(exp, '\n')
	if !bytes.Equal(exp, b) {
		t.Error(
			"unexpected encoding:",
			"expected", exp,
			"got", b,
		)
	}

	// "Bad" values are encoded without checking and throwing an error
	buf.Reset()
	m = map[string]json.RawMessage{
		"k": json.RawMessage(`bad"value`),
	}
	if err := enc.Encode(m); err != nil {
		t.Error(err)
	}

	b = buf.Bytes()
	exp = []byte(`{"k":bad"value}`)
	exp = append(exp, '\n')
	if !bytes.Equal(exp, b) {
		t.Error(
			"unexpected encoding:",
			"expected", exp,
			"got", b,
		)
	}
}

func TestSetAppendNewline(t *testing.T) {
	buf := &bytes.Buffer{}
	enc := NewEncoder(buf)

	m := "value"

	// Default encoding adds an extra newline
	if err := enc.Encode(m); err != nil {
		t.Error(err)
	}
	b := buf.Bytes()
	exp := []byte(`"value"`)
	exp = append(exp, '\n')
	if !bytes.Equal(exp, b) {
		t.Error(
			"unexpected encoding:",
			"expected", exp,
			"got", b,
		)
	}

	// With SetAppendNewline(false), there shouldn't be a newline in the output
	buf.Reset()
	enc.SetAppendNewline(false)
	if err := enc.Encode(m); err != nil {
		t.Error(err)
	}
	b = buf.Bytes()
	exp = []byte(`"value"`)
	if !bytes.Equal(exp, b) {
		t.Error(
			"unexpected encoding:",
			"expected", exp,
			"got", b,
		)
	}
}

func TestEscapeString(t *testing.T) {
	b := Escape(`value`)
	x := []byte(`"value"`)

	if !bytes.Equal(x, b) {
		t.Error(
			"unexpected encoding:",
			"expected", string(x),
			"got", string(b),
		)
	}
}

func TestAppendEscape(t *testing.T) {
	t.Run("basic", func(t *testing.T) {
		b := AppendEscape([]byte{}, `value`, AppendFlags(0))
		exp := []byte(`"value"`)
		if !bytes.Equal(exp, b) {
			t.Error(
				"unexpected encoding:",
				"expected", exp,
				"got", b,
			)
		}
	})

	t.Run("escaped", func(t *testing.T) {
		b := AppendEscape([]byte{}, `"escaped"	<value>`, EscapeHTML)
		exp := []byte(`"\"escaped\"\t\u003cvalue\u003e"`)
		if !bytes.Equal(exp, b) {
			t.Error(
				"unexpected encoding:",
				"expected", exp,
				"got", b,
			)
		}
	})

	t.Run("build", func(t *testing.T) {
		b := []byte{}
		b = append(b, '{')
		b = AppendEscape(b, `key`, EscapeHTML)
		b = append(b, ':')
		b = AppendEscape(b, `"escaped"	<value>`, EscapeHTML)
		b = append(b, '}')
		exp := []byte(`{"key":"\"escaped\"\t\u003cvalue\u003e"}`)
		if !bytes.Equal(exp, b) {
			t.Error(
				"unexpected encoding:",
				"expected", exp,
				"got", b,
			)
		}
	})
}

func TestUnescapeString(t *testing.T) {
	b := Unescape([]byte(`"value"`))
	x := []byte(`value`)

	if !bytes.Equal(x, b) {
		t.Error(
			"unexpected decoding:",
			"expected", string(x),
			"got", string(b),
		)
	}
}

func TestAppendUnescape(t *testing.T) {
	t.Run("basic", func(t *testing.T) {
		out := AppendUnescape([]byte{}, []byte(`"value"`), ParseFlags(0))
		exp := []byte("value")
		if !bytes.Equal(exp, out) {
			t.Error(
				"unexpected decoding:",
				"expected", exp,
				"got", out,
			)
		}
	})

	t.Run("escaped", func(t *testing.T) {
		b := AppendUnescape([]byte{}, []byte(`"\"escaped\"\t\u003cvalue\u003e"`), ParseFlags(0))
		exp := []byte(`"escaped"	<value>`)
		if !bytes.Equal(exp, b) {
			t.Error(
				"unexpected encoding:",
				"expected", exp,
				"got", b,
			)
		}
	})

	t.Run("build", func(t *testing.T) {
		b := []byte{}
		b = append(b, []byte(`{"key":`)...)
		b = AppendUnescape(b, []byte(`"\"escaped\"\t\u003cvalue\u003e"`), ParseFlags(0))
		b = append(b, '}')
		exp := []byte(`{"key":"escaped"	<value>}`)
		if !bytes.Equal(exp, b) {
			t.Error(
				"unexpected encoding:",
				"expected", string(exp),
				"got", string(b),
			)
		}
	})
}

func BenchmarkUnescape(b *testing.B) {
	s := []byte(`"\"escaped\"\t\u003cvalue\u003e"`)
	out := []byte{}
	for range b.N {
		out = Unescape(s)
	}

	b.Log(string(out))
}

func BenchmarkUnmarshalField(b *testing.B) {
	s := []byte(`"\"escaped\"\t\u003cvalue\u003e"`)
	var v string

	for range b.N {
		json.Unmarshal(s, &v)
	}

	b.Log(v)
}

func TestKind(t *testing.T) {
	for _, test := range []struct {
		kind  Kind
		class Kind
	}{
		{kind: 0, class: 0},
		{kind: Null, class: Null},
		{kind: False, class: Bool},
		{kind: True, class: Bool},
		{kind: Num, class: Num},
		{kind: Uint, class: Num},
		{kind: Int, class: Num},
		{kind: Float, class: Num},
		{kind: String, class: String},
		{kind: Unescaped, class: String},
		{kind: Array, class: Array},
		{kind: Object, class: Object},
	} {
		if class := test.kind.Class(); class != test.class {
			t.Errorf("class of kind(%d) mismatch: want=%d got=%d", test.kind, test.class, class)
		}
	}
}
```

## File: `json/parse.go`
```go
package json

import (
	"bytes"
	"encoding/binary"
	"math"
	"math/bits"
	"reflect"
	"unicode"
	"unicode/utf16"
	"unicode/utf8"

	"github.com/segmentio/encoding/ascii"
)

// All spaces characters defined in the json specification.
const (
	sp = ' '
	ht = '\t'
	nl = '\n'
	cr = '\r'
)

func internalParseFlags(b []byte) (flags ParseFlags) {
	// Don't consider surrounding whitespace
	b = skipSpaces(b)
	b = trimTrailingSpaces(b)
	if ascii.ValidPrint(b) {
		flags |= validAsciiPrint
	}
	if bytes.IndexByte(b, '\\') == -1 {
		flags |= noBackslash
	}
	return
}

func skipSpaces(b []byte) []byte {
	if len(b) > 0 && b[0] <= 0x20 {
		b, _ = skipSpacesN(b)
	}
	return b
}

func skipSpacesN(b []byte) ([]byte, int) {
	for i := range b {
		switch b[i] {
		case sp, ht, nl, cr:
		default:
			return b[i:], i
		}
	}
	return nil, 0
}

func trimTrailingSpaces(b []byte) []byte {
	if len(b) > 0 && b[len(b)-1] <= 0x20 {
		b = trimTrailingSpacesN(b)
	}
	return b
}

func trimTrailingSpacesN(b []byte) []byte {
	i := len(b) - 1
loop:
	for ; i >= 0; i-- {
		switch b[i] {
		case sp, ht, nl, cr:
		default:
			break loop
		}
	}
	return b[:i+1]
}

// parseInt parses a decimal representation of an int64 from b.
//
// The function is equivalent to calling strconv.ParseInt(string(b), 10, 64) but
// it prevents Go from making a memory allocation for converting a byte slice to
// a string (escape analysis fails due to the error returned by strconv.ParseInt).
//
// Because it only works with base 10 the function is also significantly faster
// than strconv.ParseInt.
func (d decoder) parseInt(b []byte, t reflect.Type) (int64, []byte, error) {
	var value int64
	var count int

	if len(b) == 0 {
		return 0, b, syntaxError(b, "cannot decode integer from an empty input")
	}

	if b[0] == '-' {
		const max = math.MinInt64
		const lim = max / 10

		if len(b) == 1 {
			return 0, b, syntaxError(b, "cannot decode integer from '-'")
		}

		if len(b) > 2 && b[1] == '0' && '0' <= b[2] && b[2] <= '9' {
			return 0, b, syntaxError(b, "invalid leading character '0' in integer")
		}

		for _, c := range b[1:] {
			if c < '0' || c > '9' {
				if count == 0 {
					b, err := d.inputError(b, t)
					return 0, b, err
				}
				break
			}

			if value < lim {
				return 0, b, unmarshalOverflow(b, t)
			}

			value *= 10
			x := int64(c - '0')

			if value < (max + x) {
				return 0, b, unmarshalOverflow(b, t)
			}

			value -= x
			count++
		}

		count++
	} else {
		if len(b) > 1 && b[0] == '0' && '0' <= b[1] && b[1] <= '9' {
			return 0, b, syntaxError(b, "invalid leading character '0' in integer")
		}

		for ; count < len(b) && b[count] >= '0' && b[count] <= '9'; count++ {
			x := int64(b[count] - '0')
			next := value*10 + x
			if next < value {
				return 0, b, unmarshalOverflow(b, t)
			}
			value = next
		}

		if count == 0 {
			b, err := d.inputError(b, t)
			return 0, b, err
		}
	}

	if count < len(b) {
		switch b[count] {
		case '.', 'e', 'E': // was this actually a float?
			v, r, _, err := d.parseNumber(b)
			if err != nil {
				v, r = b[:count+1], b[count+1:]
			}
			return 0, r, unmarshalTypeError(v, t)
		}
	}

	return value, b[count:], nil
}

// parseUint is like parseInt but for unsigned integers.
func (d decoder) parseUint(b []byte, t reflect.Type) (uint64, []byte, error) {
	var value uint64
	var count int

	if len(b) == 0 {
		return 0, b, syntaxError(b, "cannot decode integer value from an empty input")
	}

	if len(b) > 1 && b[0] == '0' && '0' <= b[1] && b[1] <= '9' {
		return 0, b, syntaxError(b, "invalid leading character '0' in integer")
	}

	for ; count < len(b) && b[count] >= '0' && b[count] <= '9'; count++ {
		x := uint64(b[count] - '0')
		next := value*10 + x
		if next < value {
			return 0, b, unmarshalOverflow(b, t)
		}
		value = next
	}

	if count == 0 {
		b, err := d.inputError(b, t)
		return 0, b, err
	}

	if count < len(b) {
		switch b[count] {
		case '.', 'e', 'E': // was this actually a float?
			v, r, _, err := d.parseNumber(b)
			if err != nil {
				v, r = b[:count+1], b[count+1:]
			}
			return 0, r, unmarshalTypeError(v, t)
		}
	}

	return value, b[count:], nil
}

// parseUintHex parses a hexadecimanl representation of a uint64 from b.
//
// The function is equivalent to calling strconv.ParseUint(string(b), 16, 64) but
// it prevents Go from making a memory allocation for converting a byte slice to
// a string (escape analysis fails due to the error returned by strconv.ParseUint).
//
// Because it only works with base 16 the function is also significantly faster
// than strconv.ParseUint.
func (d decoder) parseUintHex(b []byte) (uint64, []byte, error) {
	const max = math.MaxUint64
	const lim = max / 0x10

	var value uint64
	var count int

	if len(b) == 0 {
		return 0, b, syntaxError(b, "cannot decode hexadecimal value from an empty input")
	}

parseLoop:
	for i, c := range b {
		var x uint64

		switch {
		case c >= '0' && c <= '9':
			x = uint64(c - '0')

		case c >= 'A' && c <= 'F':
			x = uint64(c-'A') + 0xA

		case c >= 'a' && c <= 'f':
			x = uint64(c-'a') + 0xA

		default:
			if i == 0 {
				return 0, b, syntaxError(b, "expected hexadecimal digit but found '%c'", c)
			}
			break parseLoop
		}

		if value > lim {
			return 0, b, syntaxError(b, "hexadecimal value out of range")
		}

		if value *= 0x10; value > (max - x) {
			return 0, b, syntaxError(b, "hexadecimal value out of range")
		}

		value += x
		count++
	}

	return value, b[count:], nil
}

func (d decoder) parseNull(b []byte) ([]byte, []byte, Kind, error) {
	if hasNullPrefix(b) {
		return b[:4], b[4:], Null, nil
	}
	if len(b) < 4 {
		return nil, b[len(b):], Undefined, unexpectedEOF(b)
	}
	return nil, b, Undefined, syntaxError(b, "expected 'null' but found invalid token")
}

func (d decoder) parseTrue(b []byte) ([]byte, []byte, Kind, error) {
	if hasTruePrefix(b) {
		return b[:4], b[4:], True, nil
	}
	if len(b) < 4 {
		return nil, b[len(b):], Undefined, unexpectedEOF(b)
	}
	return nil, b, Undefined, syntaxError(b, "expected 'true' but found invalid token")
}

func (d decoder) parseFalse(b []byte) ([]byte, []byte, Kind, error) {
	if hasFalsePrefix(b) {
		return b[:5], b[5:], False, nil
	}
	if len(b) < 5 {
		return nil, b[len(b):], Undefined, unexpectedEOF(b)
	}
	return nil, b, Undefined, syntaxError(b, "expected 'false' but found invalid token")
}

func (d decoder) parseNumber(b []byte) (v, r []byte, kind Kind, err error) {
	if len(b) == 0 {
		r, err = b, unexpectedEOF(b)
		return
	}

	// Assume it's an unsigned integer at first.
	kind = Uint

	i := 0
	// sign
	if b[i] == '-' {
		kind = Int
		i++
	}

	if i == len(b) {
		r, err = b[i:], syntaxError(b, "missing number value after sign")
		return
	}

	if b[i] < '0' || b[i] > '9' {
		r, err = b[i:], syntaxError(b, "expected digit but got '%c'", b[i])
		return
	}

	// integer part
	if b[i] == '0' {
		i++
		if i == len(b) || (b[i] != '.' && b[i] != 'e' && b[i] != 'E') {
			v, r = b[:i], b[i:]
			return
		}
		if '0' <= b[i] && b[i] <= '9' {
			r, err = b[i:], syntaxError(b, "cannot decode number with leading '0' character")
			return
		}
	}

	for i < len(b) && '0' <= b[i] && b[i] <= '9' {
		i++
	}

	// decimal part
	if i < len(b) && b[i] == '.' {
		kind = Float
		i++
		decimalStart := i

		for i < len(b) {
			if c := b[i]; '0' > c || c > '9' {
				if i == decimalStart {
					r, err = b[i:], syntaxError(b, "expected digit but found '%c'", c)
					return
				}
				break
			}
			i++
		}

		if i == decimalStart {
			r, err = b[i:], syntaxError(b, "expected decimal part after '.'")
			return
		}
	}

	// exponent part
	if i < len(b) && (b[i] == 'e' || b[i] == 'E') {
		kind = Float
		i++

		if i < len(b) {
			if c := b[i]; c == '+' || c == '-' {
				i++
			}
		}

		if i == len(b) {
			r, err = b[i:], syntaxError(b, "missing exponent in number")
			return
		}

		exponentStart := i

		for i < len(b) {
			if c := b[i]; '0' > c || c > '9' {
				if i == exponentStart {
					err = syntaxError(b, "expected digit but found '%c'", c)
					return
				}
				break
			}
			i++
		}
	}

	v, r = b[:i], b[i:]
	return
}

func (d decoder) parseUnicode(b []byte) (rune, int, error) {
	if len(b) < 4 {
		return 0, len(b), syntaxError(b, "unicode code point must have at least 4 characters")
	}

	u, r, err := d.parseUintHex(b[:4])
	if err != nil {
		return 0, 4, syntaxError(b, "parsing unicode code point: %s", err)
	}

	if len(r) != 0 {
		return 0, 4, syntaxError(b, "invalid unicode code point")
	}

	return rune(u), 4, nil
}

func (d decoder) parseString(b []byte) ([]byte, []byte, Kind, error) {
	if len(b) < 2 {
		return nil, b[len(b):], Undefined, unexpectedEOF(b)
	}
	if b[0] != '"' {
		return nil, b, Undefined, syntaxError(b, "expected '\"' at the beginning of a string value")
	}

	var n int
	if len(b) >= 9 {
		// This is an optimization for short strings. We read 8/16 bytes,
		// and XOR each with 0x22 (") so that these bytes (and only
		// these bytes) are now zero. We use the hasless(u,1) trick
		// from https://graphics.stanford.edu/~seander/bithacks.html#ZeroInWord
		// to determine whether any bytes are zero. Finally, we CTZ
		// to find the index of that byte.
		const mask1 = 0x2222222222222222
		const mask2 = 0x0101010101010101
		const mask3 = 0x8080808080808080
		u := binary.LittleEndian.Uint64(b[1:]) ^ mask1
		if mask := (u - mask2) & ^u & mask3; mask != 0 {
			n = bits.TrailingZeros64(mask)/8 + 2
			goto found
		}
		if len(b) >= 17 {
			u = binary.LittleEndian.Uint64(b[9:]) ^ mask1
			if mask := (u - mask2) & ^u & mask3; mask != 0 {
				n = bits.TrailingZeros64(mask)/8 + 10
				goto found
			}
		}
	}
	n = bytes.IndexByte(b[1:], '"') + 2
	if n <= 1 {
		return nil, b[len(b):], Undefined, syntaxError(b, "missing '\"' at the end of a string value")
	}
found:
	if (d.flags.has(noBackslash) || bytes.IndexByte(b[1:n], '\\') < 0) &&
		(d.flags.has(validAsciiPrint) || ascii.ValidPrint(b[1:n])) {
		return b[:n], b[n:], Unescaped, nil
	}

	for i := 1; i < len(b); i++ {
		switch b[i] {
		case '\\':
			if i++; i < len(b) {
				switch b[i] {
				case '"', '\\', '/', 'n', 'r', 't', 'f', 'b':
				case 'u':
					_, n, err := d.parseUnicode(b[i+1:])
					if err != nil {
						return nil, b[i+1+n:], Undefined, err
					}
					i += n
				default:
					return nil, b, Undefined, syntaxError(b, "invalid character '%c' in string escape code", b[i])
				}
			}

		case '"':
			return b[:i+1], b[i+1:], String, nil

		default:
			if b[i] < 0x20 {
				return nil, b, Undefined, syntaxError(b, "invalid character '%c' in string escape code", b[i])
			}
		}
	}

	return nil, b[len(b):], Undefined, syntaxError(b, "missing '\"' at the end of a string value")
}

func (d decoder) parseStringUnquote(b []byte, r []byte) ([]byte, []byte, bool, error) {
	s, b, k, err := d.parseString(b)
	if err != nil {
		return s, b, false, err
	}

	s = s[1 : len(s)-1] // trim the quotes

	if k == Unescaped {
		return s, b, false, nil
	}

	if r == nil {
		r = make([]byte, 0, len(s))
	}

	for len(s) != 0 {
		i := bytes.IndexByte(s, '\\')

		if i < 0 {
			r = appendCoerceInvalidUTF8(r, s)
			break
		}

		r = appendCoerceInvalidUTF8(r, s[:i])
		s = s[i+1:]

		c := s[0]
		switch c {
		case '"', '\\', '/':
			// simple escaped character
		case 'n':
			c = '\n'

		case 'r':
			c = '\r'

		case 't':
			c = '\t'

		case 'b':
			c = '\b'

		case 'f':
			c = '\f'

		case 'u':
			s = s[1:]

			r1, n1, err := d.parseUnicode(s)
			if err != nil {
				return r, b, true, err
			}
			s = s[n1:]

			if utf16.IsSurrogate(r1) {
				if !hasPrefix(s, `\u`) {
					r1 = unicode.ReplacementChar
				} else {
					r2, n2, err := d.parseUnicode(s[2:])
					if err != nil {
						return r, b, true, err
					}
					if r1 = utf16.DecodeRune(r1, r2); r1 != unicode.ReplacementChar {
						s = s[2+n2:]
					}
				}
			}

			r = appendRune(r, r1)
			continue

		default: // not sure what this escape sequence is
			return r, b, false, syntaxError(s, "invalid character '%c' in string escape code", c)
		}

		r = append(r, c)
		s = s[1:]
	}

	return r, b, true, nil
}

func appendRune(b []byte, r rune) []byte {
	n := len(b)
	b = append(b, 0, 0, 0, 0)
	return b[:n+utf8.EncodeRune(b[n:], r)]
}

func appendCoerceInvalidUTF8(b []byte, s []byte) []byte {
	c := [4]byte{}

	for _, r := range string(s) {
		b = append(b, c[:utf8.EncodeRune(c[:], r)]...)
	}

	return b
}

func (d decoder) parseObject(b []byte) ([]byte, []byte, Kind, error) {
	if len(b) < 2 {
		return nil, b[len(b):], Undefined, unexpectedEOF(b)
	}

	if b[0] != '{' {
		return nil, b, Undefined, syntaxError(b, "expected '{' at the beginning of an object value")
	}

	var err error
	a := b
	n := len(b)
	i := 0

	b = b[1:]
	for {
		b = skipSpaces(b)

		if len(b) == 0 {
			return nil, b, Undefined, syntaxError(b, "cannot decode object from empty input")
		}

		if b[0] == '}' {
			j := (n - len(b)) + 1
			return a[:j], a[j:], Object, nil
		}

		if i != 0 {
			if len(b) == 0 {
				return nil, b, Undefined, syntaxError(b, "unexpected EOF after object field value")
			}
			if b[0] != ',' {
				return nil, b, Undefined, syntaxError(b, "expected ',' after object field value but found '%c'", b[0])
			}
			b = skipSpaces(b[1:])
			if len(b) == 0 {
				return nil, b, Undefined, unexpectedEOF(b)
			}
			if b[0] == '}' {
				return nil, b, Undefined, syntaxError(b, "unexpected trailing comma after object field")
			}
		}

		_, b, _, err = d.parseString(b)
		if err != nil {
			return nil, b, Undefined, err
		}
		b = skipSpaces(b)

		if len(b) == 0 {
			return nil, b, Undefined, syntaxError(b, "unexpected EOF after object field key")
		}
		if b[0] != ':' {
			return nil, b, Undefined, syntaxError(b, "expected ':' after object field key but found '%c'", b[0])
		}
		b = skipSpaces(b[1:])

		_, b, _, err = d.parseValue(b)
		if err != nil {
			return nil, b, Undefined, err
		}

		i++
	}
}

func (d decoder) parseArray(b []byte) ([]byte, []byte, Kind, error) {
	if len(b) < 2 {
		return nil, b[len(b):], Undefined, unexpectedEOF(b)
	}

	if b[0] != '[' {
		return nil, b, Undefined, syntaxError(b, "expected '[' at the beginning of array value")
	}

	var err error
	a := b
	n := len(b)
	i := 0

	b = b[1:]
	for {
		b = skipSpaces(b)

		if len(b) == 0 {
			return nil, b, Undefined, syntaxError(b, "missing closing ']' after array value")
		}

		if b[0] == ']' {
			j := (n - len(b)) + 1
			return a[:j], a[j:], Array, nil
		}

		if i != 0 {
			if len(b) == 0 {
				return nil, b, Undefined, syntaxError(b, "unexpected EOF after array element")
			}
			if b[0] != ',' {
				return nil, b, Undefined, syntaxError(b, "expected ',' after array element but found '%c'", b[0])
			}
			b = skipSpaces(b[1:])
			if len(b) == 0 {
				return nil, b, Undefined, unexpectedEOF(b)
			}
			if b[0] == ']' {
				return nil, b, Undefined, syntaxError(b, "unexpected trailing comma after object field")
			}
		}

		_, b, _, err = d.parseValue(b)
		if err != nil {
			return nil, b, Undefined, err
		}

		i++
	}
}

func (d decoder) parseValue(b []byte) ([]byte, []byte, Kind, error) {
	if len(b) == 0 {
		return nil, b, Undefined, syntaxError(b, "unexpected end of JSON input")
	}

	var v []byte
	var k Kind
	var err error

	switch b[0] {
	case '{':
		v, b, k, err = d.parseObject(b)
	case '[':
		v, b, k, err = d.parseArray(b)
	case '"':
		v, b, k, err = d.parseString(b)
	case 'n':
		v, b, k, err = d.parseNull(b)
	case 't':
		v, b, k, err = d.parseTrue(b)
	case 'f':
		v, b, k, err = d.parseFalse(b)
	case '-', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9':
		v, b, k, err = d.parseNumber(b)
	default:
		err = syntaxError(b, "invalid character '%c' looking for beginning of value", b[0])
	}

	return v, b, k, err
}

func hasNullPrefix(b []byte) bool {
	return len(b) >= 4 && string(b[:4]) == "null"
}

func hasTruePrefix(b []byte) bool {
	return len(b) >= 4 && string(b[:4]) == "true"
}

func hasFalsePrefix(b []byte) bool {
	return len(b) >= 5 && string(b[:5]) == "false"
}

func hasPrefix(b []byte, s string) bool {
	return len(b) >= len(s) && s == string(b[:len(s)])
}

func hasLeadingSign(b []byte) bool {
	return len(b) > 0 && (b[0] == '+' || b[0] == '-')
}

func hasLeadingZeroes(b []byte) bool {
	if hasLeadingSign(b) {
		b = b[1:]
	}
	return len(b) > 1 && b[0] == '0' && '0' <= b[1] && b[1] <= '9'
}

func appendToLower(b, s []byte) []byte {
	if ascii.Valid(s) { // fast path for ascii strings
		i := 0

		for j := range s {
			c := s[j]

			if 'A' <= c && c <= 'Z' {
				b = append(b, s[i:j]...)
				b = append(b, c+('a'-'A'))
				i = j + 1
			}
		}

		return append(b, s[i:]...)
	}

	for _, r := range string(s) {
		b = appendRune(b, foldRune(r))
	}

	return b
}

func foldRune(r rune) rune {
	if r = unicode.SimpleFold(r); 'A' <= r && r <= 'Z' {
		r = r + ('a' - 'A')
	}
	return r
}
```

## File: `json/parse_test.go`
```go
package json

import (
	"bytes"
	"strings"
	"testing"
)

func TestParseString(t *testing.T) {
	tests := []struct {
		in  string
		out string
		ext string
		err string
	}{
		{`""`, `""`, ``, ``},
		{`"1234567890"`, `"1234567890"`, ``, ``},
		{`"Hello World!"`, `"Hello World!"`, ``, ``},
		{`"Hello\"World!"`, `"Hello\"World!"`, ``, ``},
		{`"\\"`, `"\\"`, ``, ``},
		{`"\u0061\u0062\u0063"`, `"\u0061\u0062\u0063"`, ``, ``},
		{`"\u0"`, ``, ``, `json: unicode code point must have at least 4 characters: 0"`},
	}

	d := decoder{}
	for _, test := range tests {
		t.Run(test.in, func(t *testing.T) {
			out, ext, _, err := d.parseString([]byte(test.in))

			if test.err == "" {
				if err != nil {
					t.Errorf("%s => %s", test.in, err)
					return
				}
			} else {
				if s := err.Error(); s != test.err {
					t.Error("invalid error")
					t.Logf("expected: %s", test.err)
					t.Logf("found:    %s", s)
				}
			}

			if s := string(out); s != test.out {
				t.Error("invalid output")
				t.Logf("expected: %s", test.out)
				t.Logf("found:    %s", s)
			}

			if s := string(ext); s != test.ext {
				t.Error("invalid extra bytes")
				t.Logf("expected: %s", test.ext)
				t.Logf("found:    %s", s)
			}
		})
	}
}

func TestParseStringUnquote(t *testing.T) {
	tests := []struct {
		in  string
		out string
		ext string
	}{
		{`""`, ``, ``},
		{`"1234567890"`, `1234567890`, ``},
		{`"Hello World!"`, `Hello World!`, ``},
		{`"Hello\"World!"`, `Hello"World!`, ``},
		{`"\\"`, `\`, ``},
		{`"\u0061\u0062\u0063"`, `abc`, ``},
	}

	d := decoder{}
	for _, test := range tests {
		t.Run(test.in, func(t *testing.T) {
			out, ext, _, err := d.parseStringUnquote([]byte(test.in), nil)
			if err != nil {
				t.Errorf("%s => %s", test.in, err)
				return
			}

			if s := string(out); s != test.out {
				t.Error("invalid output")
				t.Logf("expected: %s", test.out)
				t.Logf("found:    %s", s)
			}

			if s := string(ext); s != test.ext {
				t.Error("invalid extra bytes")
				t.Logf("expected: %s", test.ext)
				t.Logf("found:    %s", s)
			}
		})
	}
}

func TestAppendToLower(t *testing.T) {
	tests := []string{
		"",
		"A",
		"a",
		"__segment_internal",
		"someFieldWithALongBName",
		"Hello World!",
		"Hello\"World!",
		"Hello\\World!",
		"Hello\nWorld!",
		"Hello\rWorld!",
		"Hello\tWorld!",
		"Hello\bWorld!",
		"Hello\fWorld!",
		"你好",
		"<",
		">",
		"&",
		"\u001944",
		"\u00c2e>",
		"\u00c2V?",
		"\u000e=8",
		"\u001944\u00c2e>\u00c2V?\u000e=8",
		"ir\u001bQJ\u007f\u0007y\u0015)",
	}

	for _, test := range tests {
		s1 := strings.ToLower(test)
		s2 := string(appendToLower(nil, []byte(test)))

		if s1 != s2 {
			t.Error("lowercase values mismatch")
			t.Log("expected:", s1)
			t.Log("found:   ", s2)
		}
	}
}

func BenchmarkParseString(b *testing.B) {
	s := []byte(`"__segment_internal"`)

	d := decoder{}
	for range b.N {
		d.parseString(s)
	}
}

func BenchmarkToLower(b *testing.B) {
	s := []byte("someFieldWithALongName")

	for range b.N {
		bytes.ToLower(s)
	}
}

func BenchmarkAppendToLower(b *testing.B) {
	a := []byte(nil)
	s := []byte("someFieldWithALongName")

	for range b.N {
		a = appendToLower(a[:0], s)
	}
}

var (
	benchmarkHasPrefixString = []byte("some random string")
	benchmarkHasPrefixResult = false
)

func BenchmarkHasPrefix(b *testing.B) {
	for range b.N {
		benchmarkHasPrefixResult = hasPrefix(benchmarkHasPrefixString, "null")
	}
}

func BenchmarkHasNullPrefix(b *testing.B) {
	for range b.N {
		benchmarkHasPrefixResult = hasNullPrefix(benchmarkHasPrefixString)
	}
}

func BenchmarkHasTruePrefix(b *testing.B) {
	for range b.N {
		benchmarkHasPrefixResult = hasTruePrefix(benchmarkHasPrefixString)
	}
}

func BenchmarkHasFalsePrefix(b *testing.B) {
	for range b.N {
		benchmarkHasPrefixResult = hasFalsePrefix(benchmarkHasPrefixString)
	}
}

func BenchmarkParseStringEscapeNone(b *testing.B) {
	j := []byte(`"` + strings.Repeat(`a`, 1000) + `"`)
	var s string
	b.SetBytes(int64(len(j)))

	for range b.N {
		if err := Unmarshal(j, &s); err != nil {
			b.Fatal(err)
		}
		s = ""
	}
}

func BenchmarkParseStringEscapeOne(b *testing.B) {
	j := []byte(`"` + strings.Repeat(`a`, 998) + `\n"`)
	var s string
	b.SetBytes(int64(len(j)))

	for range b.N {
		if err := Unmarshal(j, &s); err != nil {
			b.Fatal(err)
		}
		s = ""
	}
}

func BenchmarkParseStringEscapeAll(b *testing.B) {
	j := []byte(`"` + strings.Repeat(`\`, 1000) + `"`)
	var s string
	b.SetBytes(int64(len(j)))

	for range b.N {
		if err := Unmarshal(j, &s); err != nil {
			b.Fatal(err)
		}
		s = ""
	}
}
```

## File: `json/reflect.go`
```go
//go:build go1.20
// +build go1.20

package json

import (
	"reflect"
	"unsafe"
)

func extendSlice(t reflect.Type, s *slice, n int) slice {
	arrayType := reflect.ArrayOf(n, t.Elem())
	arrayData := reflect.New(arrayType)
	reflect.Copy(arrayData.Elem(), reflect.NewAt(t, unsafe.Pointer(s)).Elem())
	return slice{
		data: unsafe.Pointer(arrayData.Pointer()),
		len:  s.len,
		cap:  n,
	}
}
```

## File: `json/reflect_optimize.go`
```go
//go:build !go1.20
// +build !go1.20

package json

import (
	"reflect"
	"unsafe"
)

//go:linkname unsafe_NewArray reflect.unsafe_NewArray
func unsafe_NewArray(rtype unsafe.Pointer, length int) unsafe.Pointer

//go:linkname typedslicecopy reflect.typedslicecopy
//go:noescape
func typedslicecopy(elemType unsafe.Pointer, dst, src slice) int

func extendSlice(t reflect.Type, s *slice, n int) slice {
	elemTypeRef := t.Elem()
	elemTypePtr := ((*iface)(unsafe.Pointer(&elemTypeRef))).ptr

	d := slice{
		data: unsafe_NewArray(elemTypePtr, n),
		len:  s.len,
		cap:  n,
	}

	typedslicecopy(elemTypePtr, d, *s)
	return d
}
```

## File: `json/string.go`
```go
package json

import (
	"math/bits"
	"unsafe"
)

const (
	lsb = 0x0101010101010101
	msb = 0x8080808080808080
)

// escapeIndex finds the index of the first char in `s` that requires escaping.
// A char requires escaping if it's outside of the range of [0x20, 0x7F] or if
// it includes a double quote or backslash. If the escapeHTML mode is enabled,
// the chars <, > and & also require escaping. If no chars in `s` require
// escaping, the return value is -1.
func escapeIndex(s string, escapeHTML bool) int {
	chunks := stringToUint64(s)
	for _, n := range chunks {
		// combine masks before checking for the MSB of each byte. We include
		// `n` in the mask to check whether any of the *input* byte MSBs were
		// set (i.e. the byte was outside the ASCII range).
		mask := n | below(n, 0x20) | contains(n, '"') | contains(n, '\\')
		if escapeHTML {
			mask |= contains(n, '<') | contains(n, '>') | contains(n, '&')
		}
		if (mask & msb) != 0 {
			return bits.TrailingZeros64(mask&msb) / 8
		}
	}

	for i := len(chunks) * 8; i < len(s); i++ {
		c := s[i]
		if c < 0x20 || c > 0x7f || c == '"' || c == '\\' || (escapeHTML && (c == '<' || c == '>' || c == '&')) {
			return i
		}
	}

	return -1
}

func escapeByteRepr(b byte) byte {
	switch b {
	case '\\', '"':
		return b
	case '\b':
		return 'b'
	case '\f':
		return 'f'
	case '\n':
		return 'n'
	case '\r':
		return 'r'
	case '\t':
		return 't'
	}

	return 0
}

// below return a mask that can be used to determine if any of the bytes
// in `n` are below `b`. If a byte's MSB is set in the mask then that byte was
// below `b`. The result is only valid if `b`, and each byte in `n`, is below
// 0x80.
func below(n uint64, b byte) uint64 {
	return n - expand(b)
}

// contains returns a mask that can be used to determine if any of the
// bytes in `n` are equal to `b`. If a byte's MSB is set in the mask then
// that byte is equal to `b`. The result is only valid if `b`, and each
// byte in `n`, is below 0x80.
func contains(n uint64, b byte) uint64 {
	return (n ^ expand(b)) - lsb
}

// expand puts the specified byte into each of the 8 bytes of a uint64.
func expand(b byte) uint64 {
	return lsb * uint64(b)
}

func stringToUint64(s string) []uint64 {
	return *(*[]uint64)(unsafe.Pointer(&sliceHeader{
		Data: *(*unsafe.Pointer)(unsafe.Pointer(&s)),
		Len:  len(s) / 8,
		Cap:  len(s) / 8,
	}))
}
```

## File: `json/string_test.go`
```go
package json

import (
	"strings"
	"testing"
)

func BenchmarkEscapeIndex4KB(b *testing.B) {
	benchmarkEscapeIndex(b, strings.Repeat("!foobar!", 512), false)
}

func BenchmarkEscapeIndex4KBEscapeHTML(b *testing.B) {
	benchmarkEscapeIndex(b, strings.Repeat("!foobar!", 512), true)
}

func BenchmarkEscapeIndex1(b *testing.B) {
	benchmarkEscapeIndex(b, "1", false)
}

func BenchmarkEscapeIndex1EscapeHTML(b *testing.B) {
	benchmarkEscapeIndex(b, "1", true)
}

func BenchmarkEscapeIndex7(b *testing.B) {
	benchmarkEscapeIndex(b, "1234567", false)
}

func BenchmarkEscapeIndex7EscapeHTML(b *testing.B) {
	benchmarkEscapeIndex(b, "1234567", true)
}

func benchmarkEscapeIndex(b *testing.B, s string, escapeHTML bool) {
	b.ResetTimer()
	for range b.N {
		escapeIndex(s, escapeHTML)
	}
	b.SetBytes(int64(len(s)))
}
```

## File: `json/token.go`
```go
package json

import (
	"strconv"
	"sync"
	"unsafe"
)

// Tokenizer is an iterator-style type which can be used to progressively parse
// through a json input.
//
// Tokenizing json is useful to build highly efficient parsing operations, for
// example when doing tranformations on-the-fly where as the program reads the
// input and produces the transformed json to an output buffer.
//
// Here is a common pattern to use a tokenizer:
//
//	for t := json.NewTokenizer(b); t.Next(); {
//		switch k := t.Kind(); k.Class() {
//		case json.Null:
//			...
//		case json.Bool:
//			...
//		case json.Num:
//			...
//		case json.String:
//			...
//		case json.Array:
//			...
//		case json.Object:
//			...
//		}
//	}
type Tokenizer struct {
	// When the tokenizer is positioned on a json delimiter this field is not
	// zero. In this case the possible values are '{', '}', '[', ']', ':', and
	// ','.
	Delim Delim

	// This field contains the raw json token that the tokenizer is pointing at.
	// When Delim is not zero, this field is a single-element byte slice
	// continaing the delimiter value. Otherwise, this field holds values like
	// null, true, false, numbers, or quoted strings.
	Value RawValue

	// When the tokenizer has encountered invalid content this field is not nil.
	Err error

	// When the value is in an array or an object, this field contains the depth
	// at which it was found.
	Depth int

	// When the value is in an array or an object, this field contains the
	// position at which it was found.
	Index int

	// This field is true when the value is the key of an object.
	IsKey bool

	// Tells whether the next value read from the tokenizer is a key.
	isKey bool

	// json input for the tokenizer, pointing at data right after the last token
	// that was parsed.
	json []byte

	// Stack used to track entering and leaving arrays, objects, and keys.
	stack *stack

	// Decoder used for parsing.
	decoder
}

// NewTokenizer constructs a new Tokenizer which reads its json input from b.
func NewTokenizer(b []byte) *Tokenizer {
	return &Tokenizer{
		json:    b,
		decoder: decoder{flags: internalParseFlags(b)},
	}
}

// Reset erases the state of t and re-initializes it with the json input from b.
func (t *Tokenizer) Reset(b []byte) {
	if t.stack != nil {
		releaseStack(t.stack)
	}
	// This code is similar to:
	//
	//	*t = Tokenizer{json: b}
	//
	// However, it does not compile down to an invocation of duff-copy.
	t.Delim = 0
	t.Value = nil
	t.Err = nil
	t.Depth = 0
	t.Index = 0
	t.IsKey = false
	t.isKey = false
	t.json = b
	t.stack = nil
	t.decoder = decoder{flags: internalParseFlags(b)}
}

// Next returns a new tokenizer pointing at the next token, or the zero-value of
// Tokenizer if the end of the json input has been reached.
//
// If the tokenizer encounters malformed json while reading the input the method
// sets t.Err to an error describing the issue, and returns false. Once an error
// has been encountered, the tokenizer will always fail until its input is
// cleared by a call to its Reset method.
func (t *Tokenizer) Next() bool {
	if t.Err != nil {
		return false
	}

	// Inlined code of the skipSpaces function, this give a ~15% speed boost.
	i := 0
skipLoop:
	for _, c := range t.json {
		switch c {
		case sp, ht, nl, cr:
			i++
		default:
			break skipLoop
		}
	}

	if i > 0 {
		t.json = t.json[i:]
	}

	if len(t.json) == 0 {
		t.Reset(nil)
		return false
	}

	var kind Kind
	switch t.json[0] {
	case '"':
		t.Delim = 0
		t.Value, t.json, kind, t.Err = t.parseString(t.json)
	case 'n':
		t.Delim = 0
		t.Value, t.json, kind, t.Err = t.parseNull(t.json)
	case 't':
		t.Delim = 0
		t.Value, t.json, kind, t.Err = t.parseTrue(t.json)
	case 'f':
		t.Delim = 0
		t.Value, t.json, kind, t.Err = t.parseFalse(t.json)
	case '-', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9':
		t.Delim = 0
		t.Value, t.json, kind, t.Err = t.parseNumber(t.json)
	case '{', '}', '[', ']', ':', ',':
		t.Delim, t.Value, t.json = Delim(t.json[0]), t.json[:1], t.json[1:]
		switch t.Delim {
		case '{':
			kind = Object
		case '[':
			kind = Array
		}
	default:
		t.Delim = 0
		t.Value, t.json, t.Err = t.json[:1], t.json[1:], syntaxError(t.json, "expected token but found '%c'", t.json[0])
	}

	t.Depth = t.depth()
	t.Index = t.index()
	t.flags = t.flags.withKind(kind)

	if t.Delim == 0 {
		t.IsKey = t.isKey
	} else {
		t.IsKey = false

		switch t.Delim {
		case '{':
			t.isKey = true
			t.push(inObject)
		case '[':
			t.push(inArray)
		case '}':
			t.Err = t.pop(inObject)
			t.Depth--
			t.Index = t.index()
		case ']':
			t.Err = t.pop(inArray)
			t.Depth--
			t.Index = t.index()
		case ':':
			t.isKey = false
		case ',':
			if t.stack == nil || len(t.stack.state) == 0 {
				t.Err = syntaxError(t.json, "found unexpected comma")
				return false
			}
			if t.stack.is(inObject) {
				t.isKey = true
			}
			t.stack.state[len(t.stack.state)-1].len++
		}
	}

	return (t.Delim != 0 || len(t.Value) != 0) && t.Err == nil
}

func (t *Tokenizer) depth() int {
	if t.stack == nil {
		return 0
	}
	return t.stack.depth()
}

func (t *Tokenizer) index() int {
	if t.stack == nil {
		return 0
	}
	return t.stack.index()
}

func (t *Tokenizer) push(typ scope) {
	if t.stack == nil {
		t.stack = acquireStack()
	}
	t.stack.push(typ)
}

func (t *Tokenizer) pop(expect scope) error {
	if t.stack == nil || !t.stack.pop(expect) {
		return syntaxError(t.json, "found unexpected character while tokenizing json input")
	}
	return nil
}

// Kind returns the kind of the value that the tokenizer is currently positioned
// on.
func (t *Tokenizer) Kind() Kind { return t.flags.kind() }

// Bool returns a bool containing the value of the json boolean that the
// tokenizer is currently pointing at.
//
// This method must only be called after checking the kind of the token via a
// call to Kind.
//
// If the tokenizer is not positioned on a boolean, the behavior is undefined.
func (t *Tokenizer) Bool() bool { return t.flags.kind() == True }

// Int returns a byte slice containing the value of the json number that the
// tokenizer is currently pointing at.
//
// This method must only be called after checking the kind of the token via a
// call to Kind.
//
// If the tokenizer is not positioned on an integer, the behavior is undefined.
func (t *Tokenizer) Int() int64 {
	i, _, _ := t.parseInt(t.Value, int64Type)
	return i
}

// Uint returns a byte slice containing the value of the json number that the
// tokenizer is currently pointing at.
//
// This method must only be called after checking the kind of the token via a
// call to Kind.
//
// If the tokenizer is not positioned on a positive integer, the behavior is
// undefined.
func (t *Tokenizer) Uint() uint64 {
	u, _, _ := t.parseUint(t.Value, uint64Type)
	return u
}

// Float returns a byte slice containing the value of the json number that the
// tokenizer is currently pointing at.
//
// This method must only be called after checking the kind of the token via a
// call to Kind.
//
// If the tokenizer is not positioned on a number, the behavior is undefined.
func (t *Tokenizer) Float() float64 {
	f, _ := strconv.ParseFloat(*(*string)(unsafe.Pointer(&t.Value)), 64)
	return f
}

// String returns a byte slice containing the value of the json string that the
// tokenizer is currently pointing at.
//
// This method must only be called after checking the kind of the token via a
// call to Kind.
//
// When possible, the returned byte slice references the backing array of the
// tokenizer. A new slice is only allocated if the tokenizer needed to unescape
// the json string.
//
// If the tokenizer is not positioned on a string, the behavior is undefined.
func (t *Tokenizer) String() []byte {
	if t.flags.kind() == Unescaped && len(t.Value) > 1 {
		return t.Value[1 : len(t.Value)-1] // unquote
	}
	s, _, _, _ := t.parseStringUnquote(t.Value, nil)
	return s
}

// Remaining returns the number of bytes left to parse.
//
// The position of the tokenizer's current Value within the original byte slice
// can be calculated like so:
//
//	end := len(b) - tok.Remaining()
//	start := end - len(tok.Value)
//
// And slicing b[start:end] will yield the tokenizer's current Value.
func (t *Tokenizer) Remaining() int {
	return len(t.json)
}

// RawValue represents a raw json value, it is intended to carry null, true,
// false, number, and string values only.
type RawValue []byte

// String returns true if v contains a string value.
func (v RawValue) String() bool { return len(v) != 0 && v[0] == '"' }

// Null returns true if v contains a null value.
func (v RawValue) Null() bool { return len(v) != 0 && v[0] == 'n' }

// True returns true if v contains a true value.
func (v RawValue) True() bool { return len(v) != 0 && v[0] == 't' }

// False returns true if v contains a false value.
func (v RawValue) False() bool { return len(v) != 0 && v[0] == 'f' }

// Number returns true if v contains a number value.
func (v RawValue) Number() bool {
	if len(v) != 0 {
		switch v[0] {
		case '-', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9':
			return true
		}
	}
	return false
}

// AppendUnquote writes the unquoted version of the string value in v into b.
func (v RawValue) AppendUnquote(b []byte) []byte {
	d := decoder{}
	s, r, _, err := d.parseStringUnquote(v, b)
	if err != nil {
		panic(err)
	}
	if len(r) != 0 {
		panic(syntaxError(r, "unexpected trailing tokens after json value"))
	}
	return append(b, s...)
}

// Unquote returns the unquoted version of the string value in v.
func (v RawValue) Unquote() []byte {
	return v.AppendUnquote(nil)
}

type scope int

const (
	inArray scope = iota
	inObject
)

type state struct {
	typ scope
	len int
}

type stack struct {
	state []state
}

func (s *stack) push(typ scope) {
	s.state = append(s.state, state{typ: typ, len: 1})
}

func (s *stack) pop(expect scope) bool {
	i := len(s.state) - 1

	if i < 0 {
		return false
	}

	if found := s.state[i]; expect != found.typ {
		return false
	}

	s.state = s.state[:i]
	return true
}

func (s *stack) is(typ scope) bool {
	return len(s.state) != 0 && s.state[len(s.state)-1].typ == typ
}

func (s *stack) depth() int {
	return len(s.state)
}

func (s *stack) index() int {
	if len(s.state) == 0 {
		return 0
	}
	return s.state[len(s.state)-1].len - 1
}

func acquireStack() *stack {
	s, _ := stackPool.Get().(*stack)
	if s == nil {
		s = &stack{state: make([]state, 0, 4)}
	} else {
		s.state = s.state[:0]
	}
	return s
}

func releaseStack(s *stack) {
	stackPool.Put(s)
}

var stackPool sync.Pool // *stack
```

## File: `json/token_test.go`
```go
package json

import (
	"bytes"
	"reflect"
	"testing"
)

type token struct {
	delim Delim
	value RawValue
	err   error
	depth int
	index int
	isKey bool
}

func delim(s string, depth, index int) token {
	return token{
		delim: Delim(s[0]),
		value: RawValue(s),
		depth: depth,
		index: index,
	}
}

func key(v string, depth, index int) token {
	return token{
		value: RawValue(v),
		depth: depth,
		index: index,
		isKey: true,
	}
}

func value(v string, depth, index int) token {
	return token{
		value: RawValue(v),
		depth: depth,
		index: index,
	}
}

func tokenize(t *testing.T, b []byte) (tokens []token) {
	tok := NewTokenizer(b)

	for tok.Next() {
		end := len(b) - tok.Remaining()
		start := end - len(tok.Value)
		if end > len(b) {
			t.Fatalf("token position too far [%d:%d], len(b) is %d", start, end, len(b))
		}
		if !bytes.Equal(b[start:end], tok.Value) {
			t.Fatalf("token position is wrong [%d:%d]", start, end)
		}

		tokens = append(tokens, token{
			delim: tok.Delim,
			value: tok.Value,
			err:   tok.Err,
			depth: tok.Depth,
			index: tok.Index,
			isKey: tok.IsKey,
		})
	}

	if tok.Err != nil {
		t.Fatal(tok.Err)
	}

	return
}

func TestTokenizer(t *testing.T) {
	tests := []struct {
		input  []byte
		tokens []token
	}{
		{
			input: []byte(`null`),
			tokens: []token{
				value(`null`, 0, 0),
			},
		},

		{
			input: []byte(`true`),
			tokens: []token{
				value(`true`, 0, 0),
			},
		},

		{
			input: []byte(`false`),
			tokens: []token{
				value(`false`, 0, 0),
			},
		},

		{
			input: []byte(`""`),
			tokens: []token{
				value(`""`, 0, 0),
			},
		},

		{
			input: []byte(`"Hello World!"`),
			tokens: []token{
				value(`"Hello World!"`, 0, 0),
			},
		},

		{
			input: []byte(`-0.1234`),
			tokens: []token{
				value(`-0.1234`, 0, 0),
			},
		},

		{
			input: []byte(` { } `),
			tokens: []token{
				delim(`{`, 0, 0),
				delim(`}`, 0, 0),
			},
		},

		{
			input: []byte(`{ "answer": 42 }`),
			tokens: []token{
				delim(`{`, 0, 0),
				key(`"answer"`, 1, 0),
				delim(`:`, 1, 0),
				value(`42`, 1, 0),
				delim(`}`, 0, 0),
			},
		},

		{
			input: []byte(`{ "sub": { "key-A": 1, "key-B": 2, "key-C": 3 } }`),
			tokens: []token{
				delim(`{`, 0, 0),
				key(`"sub"`, 1, 0),
				delim(`:`, 1, 0),
				delim(`{`, 1, 0),
				key(`"key-A"`, 2, 0),
				delim(`:`, 2, 0),
				value(`1`, 2, 0),
				delim(`,`, 2, 0),
				key(`"key-B"`, 2, 1),
				delim(`:`, 2, 1),
				value(`2`, 2, 1),
				delim(`,`, 2, 1),
				key(`"key-C"`, 2, 2),
				delim(`:`, 2, 2),
				value(`3`, 2, 2),
				delim(`}`, 1, 0),
				delim(`}`, 0, 0),
			},
		},

		{
			input: []byte(` [ ] `),
			tokens: []token{
				delim(`[`, 0, 0),
				delim(`]`, 0, 0),
			},
		},

		{
			input: []byte(`[1, 2, 3]`),
			tokens: []token{
				delim(`[`, 0, 0),
				value(`1`, 1, 0),
				delim(`,`, 1, 0),
				value(`2`, 1, 1),
				delim(`,`, 1, 1),
				value(`3`, 1, 2),
				delim(`]`, 0, 0),
			},
		},
	}

	for _, test := range tests {
		t.Run(string(test.input), func(t *testing.T) {
			tokens := tokenize(t, test.input)

			if !reflect.DeepEqual(tokens, test.tokens) {
				t.Error("tokens mismatch")
				t.Logf("expected: %+v", test.tokens)
				t.Logf("found:    %+v", tokens)
			}
		})
	}
}

// Regression test for syntax that caused panics in Next.
func TestTokenizer_invalidInput(t *testing.T) {
	tests := []struct {
		scenario string
		payload  []byte
	}{
		{
			scenario: "bare comma",
			payload:  []byte(","),
		},
		{
			scenario: "comma after array",
			payload:  []byte("[],"),
		},
		{
			scenario: "comma after object",
			payload:  []byte("{},"),
		},
	}

	for _, test := range tests {
		t.Run(test.scenario, func(t *testing.T) {
			tkn := NewTokenizer(test.payload)

			// This shouldn't panic
			for tkn.Next() {
			}

			if tkn.Err == nil {
				t.Error("expected Err to be set, got nil")
			}
		})
	}
}

func BenchmarkTokenizer(b *testing.B) {
	values := []struct {
		scenario string
		payload  []byte
	}{
		{
			scenario: "null",
			payload:  []byte(`null`),
		},

		{
			scenario: "true",
			payload:  []byte(`true`),
		},

		{
			scenario: "false",
			payload:  []byte(`false`),
		},

		{
			scenario: "number",
			payload:  []byte(`-1.23456789`),
		},

		{
			scenario: "string",
			payload:  []byte(`"1234567890"`),
		},

		{
			scenario: "object",
			payload: []byte(`{
    "timestamp": "2019-01-09T18:59:57.456Z",
    "channel": "server",
    "type": "track",
    "event": "Test",
    "userId": "test-user-whatever",
    "messageId": "test-message-whatever",
    "integrations": {
        "whatever": {
            "debugMode": false
        },
        "myIntegration": {
            "debugMode": true
        }
    },
    "properties": {
        "trait1": 1,
        "trait2": "test",
        "trait3": true
    },
    "settings": {
        "apiKey": "1234567890",
        "debugMode": false,
        "directChannels": [
            "server",
            "client"
        ],
        "endpoint": "https://somewhere.com/v1/integrations/segment"
    }
}`),
		},
	}

	benchmarks := []struct {
		scenario string
		function func(*testing.B, []byte)
	}{
		{
			scenario: "github.com/segmentio/encoding/json",
			function: func(b *testing.B, json []byte) {
				t := NewTokenizer(nil)

				for range b.N {
					t.Reset(json)

					for t.Next() {
						// Does nothing other than iterating over each token to measure the
						// CPU and memory footprint.
					}

					if t.Err != nil {
						b.Error(t.Err)
					}
				}
			},
		},
	}

	for _, bechmark := range benchmarks {
		b.Run(bechmark.scenario, func(b *testing.B) {
			for _, value := range values {
				b.Run(value.scenario, func(b *testing.B) {
					bechmark.function(b, value.payload)
					b.SetBytes(int64(len(value.payload)))
				})
			}
		})
	}
}
```

## File: `json/bugs/issue11/main_test.go`
```go
package main

import (
	"fmt"
	"log"
	"testing"

	"github.com/segmentio/encoding/json"
)

func TestIssue11(t *testing.T) {
	m := map[string]map[string]any{
		"outerkey": {
			"innerkey": "innervalue",
		},
	}

	b, err := json.Marshal(m)
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(string(b))
}
```

## File: `json/bugs/issue136/main_test.go`
```go
package main

import (
	"bytes"
	"testing"

	"github.com/segmentio/encoding/json"
)

func TestIssue136(t *testing.T) {
	input := json.RawMessage(` null`)

	got, err := json.Marshal(input)
	if err != nil {
		t.Fatal(err)
	}

	want := bytes.TrimSpace(input)

	if !bytes.Equal(got, want) {
		t.Fatalf("Marshal(%q) = %q, want %q", input, got, want)
	}
}
```

## File: `json/bugs/issue18/main_test.go`
```go
package main

import (
	"bytes"
	"fmt"
	"testing"

	"github.com/segmentio/encoding/json"
)

func TestIssue18(t *testing.T) {
	b := []byte(`{
	"userId": "blah",
	}`)

	d := json.NewDecoder(bytes.NewReader(b))

	var a struct {
		UserId string `json:"userId"`
	}
	fmt.Println(d.Decode(&a))
	fmt.Println(a)
}
```

## File: `json/bugs/issue84/main_test.go`
```go
package main

import (
	"testing"

	"github.com/segmentio/encoding/json"
)

type Foo struct {
	Source struct {
		Table string
	}
}

func TestUnmarshal(t *testing.T) {
	input := []byte(`{"source": {"table": "1234567"}}`)
	r := &Foo{}
	json.Unmarshal(input, r)
}
```

## File: `json/fuzz/LICENSE`
```
                                 Apache License
                           Version 2.0, January 2004
                        http://www.apache.org/licenses/

   TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

   1. Definitions.

      "License" shall mean the terms and conditions for use, reproduction,
      and distribution as defined by Sections 1 through 9 of this document.

      "Licensor" shall mean the copyright owner or entity authorized by
      the copyright owner that is granting the License.

      "Legal Entity" shall mean the union of the acting entity and all
      other entities that control, are controlled by, or are under common
      control with that entity. For the purposes of this definition,
      "control" means (i) the power, direct or indirect, to cause the
      direction or management of such entity, whether by contract or
      otherwise, or (ii) ownership of fifty percent (50%) or more of the
      outstanding shares, or (iii) beneficial ownership of such entity.

      "You" (or "Your") shall mean an individual or Legal Entity
      exercising permissions granted by this License.

      "Source" form shall mean the preferred form for making modifications,
      including but not limited to software source code, documentation
      source, and configuration files.

      "Object" form shall mean any form resulting from mechanical
      transformation or translation of a Source form, including but
      not limited to compiled object code, generated documentation,
      and conversions to other media types.

      "Work" shall mean the work of authorship, whether in Source or
      Object form, made available under the License, as indicated by a
      copyright notice that is included in or attached to the work
      (an example is provided in the Appendix below).

      "Derivative Works" shall mean any work, whether in Source or Object
      form, that is based on (or derived from) the Work and for which the
      editorial revisions, annotations, elaborations, or other modifications
      represent, as a whole, an original work of authorship. For the purposes
      of this License, Derivative Works shall not include works that remain
      separable from, or merely link (or bind by name) to the interfaces of,
      the Work and Derivative Works thereof.

      "Contribution" shall mean any work of authorship, including
      the original version of the Work and any modifications or additions
      to that Work or Derivative Works thereof, that is intentionally
      submitted to Licensor for inclusion in the Work by the copyright owner
      or by an individual or Legal Entity authorized to submit on behalf of
      the copyright owner. For the purposes of this definition, "submitted"
      means any form of electronic, verbal, or written communication sent
      to the Licensor or its representatives, including but not limited to
      communication on electronic mailing lists, source code control systems,
      and issue tracking systems that are managed by, or on behalf of, the
      Licensor for the purpose of discussing and improving the Work, but
      excluding communication that is conspicuously marked or otherwise
      designated in writing by the copyright owner as "Not a Contribution."

      "Contributor" shall mean Licensor and any individual or Legal Entity
      on behalf of whom a Contribution has been received by Licensor and
      subsequently incorporated within the Work.

   2. Grant of Copyright License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      copyright license to reproduce, prepare Derivative Works of,
      publicly display, publicly perform, sublicense, and distribute the
      Work and such Derivative Works in Source or Object form.

   3. Grant of Patent License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      (except as stated in this section) patent license to make, have made,
      use, offer to sell, sell, import, and otherwise transfer the Work,
      where such license applies only to those patent claims licensable
      by such Contributor that are necessarily infringed by their
      Contribution(s) alone or by combination of their Contribution(s)
      with the Work to which such Contribution(s) was submitted. If You
      institute patent litigation against any entity (including a
      cross-claim or counterclaim in a lawsuit) alleging that the Work
      or a Contribution incorporated within the Work constitutes direct
      or contributory patent infringement, then any patent licenses
      granted to You under this License for that Work shall terminate
      as of the date such litigation is filed.

   4. Redistribution. You may reproduce and distribute copies of the
      Work or Derivative Works thereof in any medium, with or without
      modifications, and in Source or Object form, provided that You
      meet the following conditions:

      (a) You must give any other recipients of the Work or
          Derivative Works a copy of this License; and

      (b) You must cause any modified files to carry prominent notices
          stating that You changed the files; and

      (c) You must retain, in the Source form of any Derivative Works
          that You distribute, all copyright, patent, trademark, and
          attribution notices from the Source form of the Work,
          excluding those notices that do not pertain to any part of
          the Derivative Works; and

      (d) If the Work includes a "NOTICE" text file as part of its
          distribution, then any Derivative Works that You distribute must
          include a readable copy of the attribution notices contained
          within such NOTICE file, excluding those notices that do not
          pertain to any part of the Derivative Works, in at least one
          of the following places: within a NOTICE text file distributed
          as part of the Derivative Works; within the Source form or
          documentation, if provided along with the Derivative Works; or,
          within a display generated by the Derivative Works, if and
          wherever such third-party notices normally appear. The contents
          of the NOTICE file are for informational purposes only and
          do not modify the License. You may add Your own attribution
          notices within Derivative Works that You distribute, alongside
          or as an addendum to the NOTICE text from the Work, provided
          that such additional attribution notices cannot be construed
          as modifying the License.

      You may add Your own copyright statement to Your modifications and
      may provide additional or different license terms and conditions
      for use, reproduction, or distribution of Your modifications, or
      for any such Derivative Works as a whole, provided Your use,
      reproduction, and distribution of the Work otherwise complies with
      the conditions stated in this License.

   5. Submission of Contributions. Unless You explicitly state otherwise,
      any Contribution intentionally submitted for inclusion in the Work
      by You to the Licensor shall be under the terms and conditions of
      this License, without any additional terms or conditions.
      Notwithstanding the above, nothing herein shall supersede or modify
      the terms of any separate license agreement you may have executed
      with Licensor regarding such Contributions.

   6. Trademarks. This License does not grant permission to use the trade
      names, trademarks, service marks, or product names of the Licensor,
      except as required for reasonable and customary use in describing the
      origin of the Work and reproducing the content of the NOTICE file.

   7. Disclaimer of Warranty. Unless required by applicable law or
      agreed to in writing, Licensor provides the Work (and each
      Contributor provides its Contributions) on an "AS IS" BASIS,
      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
      implied, including, without limitation, any warranties or conditions
      of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A
      PARTICULAR PURPOSE. You are solely responsible for determining the
      appropriateness of using or redistributing the Work and assume any
      risks associated with Your exercise of permissions under this License.

   8. Limitation of Liability. In no event and under no legal theory,
      whether in tort (including negligence), contract, or otherwise,
      unless required by applicable law (such as deliberate and grossly
      negligent acts) or agreed to in writing, shall any Contributor be
      liable to You for damages, including any direct, indirect, special,
      incidental, or consequential damages of any character arising as a
      result of this License or out of the use or inability to use the
      Work (including but not limited to damages for loss of goodwill,
      work stoppage, computer failure or malfunction, or any and all
      other commercial damages or losses), even if such Contributor
      has been advised of the possibility of such damages.

   9. Accepting Warranty or Additional Liability. While redistributing
      the Work or Derivative Works thereof, You may choose to offer,
      and charge a fee for, acceptance of support, warranty, indemnity,
      or other liability obligations and/or rights consistent with this
      License. However, in accepting such obligations, You may act only
      on Your own behalf and on Your sole responsibility, not on behalf
      of any other Contributor, and only if You agree to indemnify,
      defend, and hold each Contributor harmless for any liability
      incurred by, or claims asserted against, such Contributor by reason
      of your accepting any such warranty or additional liability.

   END OF TERMS AND CONDITIONS

   APPENDIX: How to apply the Apache License to your work.

      To apply the Apache License to your work, attach the following
      boilerplate notice, with the fields enclosed by brackets "{}"
      replaced with your own identifying information. (Don't include
      the brackets!)  The text should be enclosed in the appropriate
      comment syntax for the file format. We also recommend that a
      file or class name and description of purpose be included on the
      same "printed page" as the copyright notice for easier
      identification within third-party archives.

   Copyright {yyyy} {name of copyright owner}

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
```

## File: `json/fuzz/fuzz.go`
```go
//go:build ignore
// +build ignore

// Copyright 2015 go-fuzz project authors. All rights reserved.
// Use of this source code is governed by Apache 2 LICENSE that can be found in the LICENSE file.

package fuzz

import (
	"bytes"
	encodingJSON "encoding/json"
	"fmt"
	"reflect"

	"github.com/dvyukov/go-fuzz-corpus/fuzz"
	"github.com/segmentio/encoding/json"
)

func fixS(v any) {
	if s, ok := v.(*S); ok {
		if len(s.P) == 0 {
			s.P = []byte(`""`)
		}
	}
}

func Fuzz(data []byte) int {
	score := 0
	for _, ctor := range []func() any{
		func() any { return nil },
		func() any { return new([]any) },
		func() any { m := map[string]string{}; return &m },
		func() any { m := map[string]any{}; return &m },
		func() any { return new(S) },
	} {
		// Note: we modified the test to verify that we behavior like the
		// standard encoding/json package, whether it's right or wrong.
		v1 := ctor()
		v2 := ctor()

		err1 := encodingJSON.Unmarshal(data, v1)
		err2 := json.Unmarshal(data, v2)

		if err1 != nil {
			if err2 != nil {
				// both implementations report an error
				if reflect.TypeOf(err1) != reflect.TypeOf(err2) {
					fmt.Printf("input: %s\n", string(data))
					fmt.Printf("encoding/json.Unmarshal(%T): %T: %s\n", v1, err1, err1)
					fmt.Printf("segmentio/encoding/json.Unmarshal(%T): %T: %s\n", v2, err2, err2)
					panic("error types mismatch")
				}
				continue
			} else {
				fmt.Printf("input: %s\n", string(data))
				fmt.Printf("encoding/json.Unmarshal(%T): %T: %s\n", v1, err1, err1)
				fmt.Printf("segmentio/encoding/json.Unmarshal(%T): <nil>\n")
				panic("error values mismatch")
			}
		} else {
			if err2 != nil {
				fmt.Printf("input: %s\n", string(data))
				fmt.Printf("encoding/json.Unmarshal(%T): <nil>\n")
				fmt.Printf("segmentio/encoding/json.Unmarshal(%T): %T: %s\n", v2, err2, err2)
				panic("error values mismatch")
			} else {
				// both implementations pass
			}
		}

		score = 1
		fixS(v1)
		fixS(v2)
		if !fuzz.DeepEqual(v1, v2) {
			fmt.Printf("input: %s\n", string(data))
			fmt.Printf("encoding/json:      %#v\n", v1)
			fmt.Printf("segmentio/encoding: %#v\n", v2)
			panic("not equal")
		}

		data1, err := encodingJSON.Marshal(v1)
		if err != nil {
			panic(err)
		}
		data2, err := json.Marshal(v2)
		if err != nil {
			panic(err)
		}
		if !bytes.Equal(data1, data2) {
			fmt.Printf("input: %s\n", string(data))
			fmt.Printf("encoding/json:      %s\n", string(data1))
			fmt.Printf("segmentio/encoding: %s\n", string(data2))
			panic("not equal")
		}
	}
	return score
}

type S struct {
	A int    `json:",omitempty"`
	B string `json:"B1,omitempty"`
	C float64
	D bool
	E uint8
	F []byte
	G any
	H map[string]any
	I map[string]string
	J []any
	K []string
	L S1
	M *S1
	N *int
	O **int
	P json.RawMessage
	Q Marshaller
	R int `json:"-"`
	S int `json:",string"`
}

type S1 struct {
	A int
	B string
}

type Marshaller struct {
	v string
}

func (m *Marshaller) MarshalJSON() ([]byte, error) {
	return json.Marshal(m.v)
}

func (m *Marshaller) UnmarshalJSON(data []byte) error {
	return json.Unmarshal(data, &m.v)
}
```

## File: `proto/bool.go`
```go
package proto

import (
	"io"
	"unsafe"
)

var boolCodec = codec{
	wire:   varint,
	size:   sizeOfBool,
	encode: encodeBool,
	decode: decodeBool,
}

func sizeOfBool(p unsafe.Pointer, flags flags) int {
	if p != nil && *(*bool)(p) || flags.has(wantzero) {
		return 1
	}
	return 0
}

func encodeBool(b []byte, p unsafe.Pointer, flags flags) (int, error) {
	if p != nil && *(*bool)(p) || flags.has(wantzero) {
		if len(b) == 0 {
			return 0, io.ErrShortBuffer
		}
		b[0] = 1
		return 1, nil
	}
	return 0, nil
}

func decodeBool(b []byte, p unsafe.Pointer, _ flags) (int, error) {
	if len(b) == 0 {
		return 0, io.ErrUnexpectedEOF
	}
	*(*bool)(p) = b[0] != 0
	return 1, nil
}
```

## File: `proto/bytes.go`
```go
package proto

import (
	"fmt"
	"io"
	"reflect"
	"unsafe"
)

var bytesCodec = codec{
	wire:   varlen,
	size:   sizeOfBytes,
	encode: encodeBytes,
	decode: decodeBytes,
}

func sizeOfBytes(p unsafe.Pointer, flags flags) int {
	if p != nil {
		if v := *(*[]byte)(p); v != nil || flags.has(wantzero) {
			return sizeOfVarlen(len(v))
		}
	}
	return 0
}

func encodeBytes(b []byte, p unsafe.Pointer, flags flags) (int, error) {
	if p != nil {
		if v := *(*[]byte)(p); v != nil || flags.has(wantzero) {
			n, err := encodeVarint(b, uint64(len(v)))
			if err != nil {
				return n, err
			}
			c := copy(b[n:], v)
			n += c
			if c < len(v) {
				err = io.ErrShortBuffer
			}
			return n, err
		}
	}
	return 0, nil
}

func decodeBytes(b []byte, p unsafe.Pointer, _ flags) (int, error) {
	v, n, err := decodeVarlen(b)
	pb := (*[]byte)(p)
	if *pb == nil {
		*pb = make([]byte, 0, len(v))
	}
	*pb = append((*pb)[:0], v...)
	return n, err
}

func makeBytes(p unsafe.Pointer, n int) []byte {
	return *(*[]byte)(unsafe.Pointer(&sliceHeader{
		Data: p,
		Len:  n,
		Cap:  n,
	}))
}

type sliceHeader struct {
	Data unsafe.Pointer
	Len  int
	Cap  int
}

// isZeroBytes is an optimized version of this loop:
//
//	for i := range b {
//		if b[i] != 0 {
//			return false
//		}
//	}
//	return true
//
// This implementation significantly reduces the CPU footprint of checking for
// slices to be zero, especially when the length increases (these cases should
// be rare tho).
//
// name            old time/op  new time/op  delta
// IsZeroBytes0    1.78ns ± 1%  2.29ns ± 4%  +28.65%  (p=0.000 n=8+10)
// IsZeroBytes4    3.17ns ± 3%  2.37ns ± 3%  -25.21%  (p=0.000 n=10+10)
// IsZeroBytes7    3.97ns ± 4%  3.26ns ± 3%  -18.02%  (p=0.000 n=10+10)
// IsZeroBytes64K  14.8µs ± 3%   1.9µs ± 3%  -87.34%  (p=0.000 n=10+10)
func isZeroBytes(b []byte) bool {
	if n := len(b) / 8; n != 0 {
		if !isZeroUint64(*(*[]uint64)(unsafe.Pointer(&sliceHeader{
			Data: unsafe.Pointer(&b[0]),
			Len:  n,
			Cap:  n,
		}))) {
			return false
		}
		b = b[n*8:]
	}
	switch len(b) {
	case 7:
		return bto32(b) == 0 && bto16(b[4:]) == 0 && b[6] == 0
	case 6:
		return bto32(b) == 0 && bto16(b[4:]) == 0
	case 5:
		return bto32(b) == 0 && b[4] == 0
	case 4:
		return bto32(b) == 0
	case 3:
		return bto16(b) == 0 && b[2] == 0
	case 2:
		return bto16(b) == 0
	case 1:
		return b[0] == 0
	default:
		return true
	}
}

func bto32(b []byte) uint32 {
	return *(*uint32)(unsafe.Pointer(&b[0]))
}

func bto16(b []byte) uint16 {
	return *(*uint16)(unsafe.Pointer(&b[0]))
}

func isZeroUint64(b []uint64) bool {
	for i := range b {
		if b[i] != 0 {
			return false
		}
	}
	return true
}

func byteArrayCodecOf(t reflect.Type, seen map[reflect.Type]*codec) *codec {
	n := t.Len()
	c := &codec{
		wire:   varlen,
		size:   byteArraySizeFuncOf(n),
		encode: byteArrayEncodeFuncOf(n),
		decode: byteArrayDecodeFuncOf(n),
	}
	seen[t] = c
	return c
}

func byteArraySizeFuncOf(n int) sizeFunc {
	size := sizeOfVarlen(n)
	return func(p unsafe.Pointer, flags flags) int {
		if p != nil && (flags.has(wantzero) || !isZeroBytes(makeBytes(p, n))) {
			return size
		}
		return 0
	}
}

func byteArrayEncodeFuncOf(n int) encodeFunc {
	return func(b []byte, p unsafe.Pointer, flags flags) (int, error) {
		if p != nil {
			if v := makeBytes(p, n); flags.has(wantzero) || !isZeroBytes(v) {
				return encodeBytes(b, unsafe.Pointer(&v), noflags)
			}
		}
		return 0, nil
	}
}

func byteArrayDecodeFuncOf(n int) decodeFunc {
	return func(b []byte, p unsafe.Pointer, _ flags) (int, error) {
		v, r, err := decodeVarlen(b)
		if err == nil {
			if copy(makeBytes(p, n), v) != n {
				err = fmt.Errorf("cannot decode byte sequence of size %d into byte array of size %d", len(v), n)
			}
		}
		return r, err
	}
}
```

## File: `proto/bytes_test.go`
```go
package proto

import "testing"

func BenchmarkIsZeroBytes0(b *testing.B) {
	benchmarkIsZeroBytes(b, nil)
}

func BenchmarkIsZeroBytes4(b *testing.B) {
	benchmarkIsZeroBytes(b, make([]byte, 4))
}

func BenchmarkIsZeroBytes7(b *testing.B) {
	benchmarkIsZeroBytes(b, make([]byte, 7))
}

func BenchmarkIsZeroBytes64K(b *testing.B) {
	benchmarkIsZeroBytes(b, make([]byte, 64*1024))
}

func benchmarkIsZeroBytes(b *testing.B, slice []byte) {
	for range b.N {
		isZeroBytes(slice)
	}
}
```

## File: `proto/custom.go`
```go
package proto

import (
	"io"
	"reflect"
	"unsafe"
)

func customCodecOf(t reflect.Type) *codec {
	return &codec{
		wire:   varlen,
		size:   customSizeFuncOf(t),
		encode: customEncodeFuncOf(t),
		decode: customDecodeFuncOf(t),
	}
}

func customSizeFuncOf(t reflect.Type) sizeFunc {
	return func(p unsafe.Pointer, flags flags) int {
		if p != nil {
			if m := reflect.NewAt(t, p).Interface().(customMessage); m != nil {
				size := m.Size()
				if flags.has(toplevel) {
					return size
				}
				return sizeOfVarlen(size)
			}
		}
		return 0
	}
}

func customEncodeFuncOf(t reflect.Type) encodeFunc {
	return func(b []byte, p unsafe.Pointer, flags flags) (int, error) {
		if p != nil {
			if m := reflect.NewAt(t, p).Interface().(customMessage); m != nil {
				size := m.Size()

				if flags.has(toplevel) {
					if len(b) < size {
						return 0, io.ErrShortBuffer
					}
					return m.MarshalTo(b)
				}

				vlen := sizeOfVarlen(size)
				if len(b) < vlen {
					return 0, io.ErrShortBuffer
				}

				n1, err := encodeVarint(b, uint64(size))
				if err != nil {
					return n1, err
				}

				n2, err := m.MarshalTo(b[n1:])
				return n1 + n2, err
			}
		}
		return 0, nil
	}
}

func customDecodeFuncOf(t reflect.Type) decodeFunc {
	return func(b []byte, p unsafe.Pointer, flags flags) (int, error) {
		m := reflect.NewAt(t, p).Interface().(customMessage)

		if flags.has(toplevel) {
			return len(b), m.Unmarshal(b)
		}

		v, n, err := decodeVarlen(b)
		if err != nil {
			return n, err
		}

		return n + len(v), m.Unmarshal(v)
	}
}
```

## File: `proto/decode.go`
```go
package proto

import (
	"encoding/binary"
	"errors"
	"io"
	"unsafe"
)

// DecodeTag reverses the encoding applied by EncodeTag.
func DecodeTag(tag uint64) (FieldNumber, WireType) {
	return FieldNumber(tag >> 3), WireType(tag & 7)
}

// DecodeZigZag reverses the encoding applied by EncodeZigZag.
func DecodeZigZag(v uint64) int64 {
	return decodeZigZag64(v)
}

func decodeZigZag64(v uint64) int64 {
	return int64(v>>1) ^ -(int64(v) & 1)
}

func decodeZigZag32(v uint32) int32 {
	return int32(v>>1) ^ -(int32(v) & 1)
}

type decodeFunc = func([]byte, unsafe.Pointer, flags) (int, error)

var errVarintOverflow = errors.New("varint overflowed 64 bits integer")

func decodeVarint(b []byte) (uint64, int, error) {
	if len(b) != 0 && b[0] < 0x80 {
		// Fast-path for decoding the common case of varints that fit on a
		// single byte.
		//
		// This path is ~60% faster than calling binary.Uvarint.
		return uint64(b[0]), 1, nil
	}

	var x uint64
	var s uint

	for i, c := range b {
		if c < 0x80 {
			if i > 9 || i == 9 && c > 1 {
				return 0, i, errVarintOverflow
			}
			return x | uint64(c)<<s, i + 1, nil
		}
		x |= uint64(c&0x7f) << s
		s += 7
	}

	return x, len(b), io.ErrUnexpectedEOF
}

func decodeVarintZigZag(b []byte) (int64, int, error) {
	v, n, err := decodeVarint(b)
	return decodeZigZag64(v), n, err
}

func decodeLE32(b []byte) (uint32, int, error) {
	if len(b) < 4 {
		return 0, 0, io.ErrUnexpectedEOF
	}
	return binary.LittleEndian.Uint32(b), 4, nil
}

func decodeLE64(b []byte) (uint64, int, error) {
	if len(b) < 8 {
		return 0, 0, io.ErrUnexpectedEOF
	}
	return binary.LittleEndian.Uint64(b), 8, nil
}

func decodeTag(b []byte) (f fieldNumber, t wireType, n int, err error) {
	v, n, err := decodeVarint(b)
	return fieldNumber(v >> 3), wireType(v & 7), n, err
}

func decodeVarlen(b []byte) ([]byte, int, error) {
	v, n, err := decodeVarint(b)
	if err != nil {
		return nil, n, err
	}
	if v > uint64(len(b)-n) {
		return nil, n, io.ErrUnexpectedEOF
	}
	return b[n : n+int(v)], n + int(v), nil
}
```

## File: `proto/decode_test.go`
```go
package proto

import (
	"errors"
	"io"
	"testing"
)

func TestUnarshalFromShortBuffer(t *testing.T) {
	m := message{
		A: 1,
		B: 2,
		C: 3,
		S: submessage{
			X: "hello",
			Y: "world",
		},
	}

	b, _ := Marshal(m)

	for i := range b {
		switch i {
		case 0, 2, 4, 6:
			continue // these land on field boundaries, making the input valid
		}
		t.Run("", func(t *testing.T) {
			msg := &message{}
			err := Unmarshal(b[:i], msg)
			if !errors.Is(err, io.ErrUnexpectedEOF) {
				t.Errorf("error mismatch, want io.ErrUnexpectedEOF but got %q", err)
			}
		})
	}
}

func TestUnmarshalFixture(t *testing.T) {
	type Message struct {
		A uint
		B uint32
		C uint64
		D string
	}

	b := loadProtobuf(t, "message.pb")
	m := Message{}

	if err := Unmarshal(b, &m); err != nil {
		t.Fatal(err)
	}

	if m.A != 10 {
		t.Error("m.A mismatch, want 10 but got", m.A)
	}

	if m.B != 20 {
		t.Error("m.B mismatch, want 20 but got", m.B)
	}

	if m.C != 30 {
		t.Error("m.C mismatch, want 30 but got", m.C)
	}

	if m.D != "Hello World!" {
		t.Errorf("m.D mismatch, want \"Hello World!\" but got %q", m.D)
	}
}

func BenchmarkDecodeTag(b *testing.B) {
	c := [8]byte{}
	n, _ := encodeTag(c[:], 1, varint)

	for range b.N {
		decodeTag(c[:n])
	}
}

func BenchmarkDecodeMessage(b *testing.B) {
	data, _ := Marshal(message{
		A: 1,
		B: 100,
		C: 10000,
		S: submessage{
			X: "",
			Y: "Hello World!",
		},
	})

	msg := message{}
	b.SetBytes(int64(len(data)))

	for range b.N {
		if err := Unmarshal(data, &msg); err != nil {
			b.Fatal(err)
		}
		msg = message{}
	}
}

func BenchmarkDecodeMap(b *testing.B) {
	type message struct {
		M map[int]int
	}

	data, _ := Marshal(message{
		M: map[int]int{
			0: 0,
			1: 1,
			2: 2,
			3: 3,
			4: 4,
		},
	})

	msg := message{}
	b.SetBytes(int64(len(data)))

	for range b.N {
		if err := Unmarshal(data, &msg); err != nil {
			b.Fatal(err)
		}
		msg = message{}
	}
}

func BenchmarkDecodeSlice(b *testing.B) {
	type message struct {
		S []int
	}

	data, _ := Marshal(message{
		S: []int{
			0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
		},
	})

	msg := message{}
	b.SetBytes(int64(len(data)))

	for range b.N {
		if err := Unmarshal(data, &msg); err != nil {
			b.Fatal(err)
		}
		msg = message{}
	}
}
```

## File: `proto/encode.go`
```go
package proto

import (
	"encoding/binary"
	"io"
	"unsafe"
)

// EncodeTag encodes a pair of field number and wire type into a protobuf tag.
func EncodeTag(f FieldNumber, t WireType) uint64 {
	return uint64(f)<<3 | uint64(t)
}

// EncodeZigZag returns v as a zig-zag encoded value.
func EncodeZigZag(v int64) uint64 {
	return encodeZigZag64(v)
}

func encodeZigZag64(v int64) uint64 {
	return (uint64(v) << 1) ^ uint64(v>>63)
}

func encodeZigZag32(v int32) uint32 {
	return (uint32(v) << 1) ^ uint32(v>>31)
}

type encodeFunc = func([]byte, unsafe.Pointer, flags) (int, error)

func encodeVarint(b []byte, v uint64) (int, error) {
	n := sizeOfVarint(v)

	if len(b) < n {
		return 0, io.ErrShortBuffer
	}

	switch n {
	case 1:
		b[0] = byte(v)

	case 2:
		b[0] = byte(v) | 0x80
		b[1] = byte(v >> 7)

	case 3:
		b[0] = byte(v) | 0x80
		b[1] = byte(v>>7) | 0x80
		b[2] = byte(v >> 14)

	case 4:
		b[0] = byte(v) | 0x80
		b[1] = byte(v>>7) | 0x80
		b[2] = byte(v>>14) | 0x80
		b[3] = byte(v >> 21)

	case 5:
		b[0] = byte(v) | 0x80
		b[1] = byte(v>>7) | 0x80
		b[2] = byte(v>>14) | 0x80
		b[3] = byte(v>>21) | 0x80
		b[4] = byte(v >> 28)

	case 6:
		b[0] = byte(v) | 0x80
		b[1] = byte(v>>7) | 0x80
		b[2] = byte(v>>14) | 0x80
		b[3] = byte(v>>21) | 0x80
		b[4] = byte(v>>28) | 0x80
		b[5] = byte(v >> 35)

	case 7:
		b[0] = byte(v) | 0x80
		b[1] = byte(v>>7) | 0x80
		b[2] = byte(v>>14) | 0x80
		b[3] = byte(v>>21) | 0x80
		b[4] = byte(v>>28) | 0x80
		b[5] = byte(v>>35) | 0x80
		b[6] = byte(v >> 42)

	case 8:
		b[0] = byte(v) | 0x80
		b[1] = byte(v>>7) | 0x80
		b[2] = byte(v>>14) | 0x80
		b[3] = byte(v>>21) | 0x80
		b[4] = byte(v>>28) | 0x80
		b[5] = byte(v>>35) | 0x80
		b[6] = byte(v>>42) | 0x80
		b[7] = byte(v >> 49)

	case 9:
		b[0] = byte(v) | 0x80
		b[1] = byte(v>>7) | 0x80
		b[2] = byte(v>>14) | 0x80
		b[3] = byte(v>>21) | 0x80
		b[4] = byte(v>>28) | 0x80
		b[5] = byte(v>>35) | 0x80
		b[6] = byte(v>>42) | 0x80
		b[7] = byte(v>>49) | 0x80
		b[8] = byte(v >> 56)

	case 10:
		b[0] = byte(v) | 0x80
		b[1] = byte(v>>7) | 0x80
		b[2] = byte(v>>14) | 0x80
		b[3] = byte(v>>21) | 0x80
		b[4] = byte(v>>28) | 0x80
		b[5] = byte(v>>35) | 0x80
		b[6] = byte(v>>42) | 0x80
		b[7] = byte(v>>49) | 0x80
		b[8] = byte(v>>56) | 0x80
		b[9] = byte(v >> 63)
	}

	return n, nil
}

func encodeVarintZigZag(b []byte, v int64) (int, error) {
	return encodeVarint(b, encodeZigZag64(v))
}

func encodeLE32(b []byte, v uint32) (int, error) {
	if len(b) < 4 {
		return 0, io.ErrShortBuffer
	}
	binary.LittleEndian.PutUint32(b, v)
	return 4, nil
}

func encodeLE64(b []byte, v uint64) (int, error) {
	if len(b) < 8 {
		return 0, io.ErrShortBuffer
	}
	binary.LittleEndian.PutUint64(b, v)
	return 8, nil
}

func encodeTag(b []byte, f fieldNumber, t wireType) (int, error) {
	return encodeVarint(b, uint64(f)<<3|uint64(t))
}
```

## File: `proto/encode_test.go`
```go
package proto

import (
	"errors"
	"io"
	"math"
	"testing"
)

func TestMarshalToShortBuffer(t *testing.T) {
	m := message{
		A: 1,
		B: 2,
		C: 3,
		S: submessage{
			X: "hello",
			Y: "world",
		},
	}

	b, _ := Marshal(m)
	short := make([]byte, len(b))

	for i := range b {
		t.Run("", func(t *testing.T) {
			n, err := MarshalTo(short[:i], m)
			if n != i {
				t.Errorf("byte count mismatch, want %d but got %d", i, n)
			}
			if !errors.Is(err, io.ErrShortBuffer) {
				t.Errorf("error mismatch, want io.ErrShortBuffer but got %q", err)
			}
		})
	}
}

func BenchmarkEncodeVarintShort(b *testing.B) {
	c := [10]byte{}

	for range b.N {
		encodeVarint(c[:], 0)
	}
}

func BenchmarkEncodeVarintLong(b *testing.B) {
	c := [10]byte{}

	for range b.N {
		encodeVarint(c[:], math.MaxUint64)
	}
}

func BenchmarkEncodeTag(b *testing.B) {
	c := [8]byte{}

	for range b.N {
		encodeTag(c[:], 1, varint)
	}
}

func BenchmarkEncodeMessage(b *testing.B) {
	buf := [128]byte{}
	msg := &message{
		A: 1,
		B: 100,
		C: 10000,
		S: submessage{
			X: "",
			Y: "Hello World!",
		},
	}

	size := Size(msg)
	data := buf[:size]
	b.SetBytes(int64(size))

	for range b.N {
		if _, err := MarshalTo(data, msg); err != nil {
			b.Fatal(err)
		}
	}
}

func BenchmarkEncodeMap(b *testing.B) {
	buf := [128]byte{}
	msg := struct {
		M map[string]string
	}{
		M: map[string]string{
			"hello": "world",
		},
	}

	size := Size(msg)
	data := buf[:size]
	b.SetBytes(int64(size))

	for range b.N {
		if _, err := MarshalTo(data, msg); err != nil {
			b.Fatal(err)
		}
	}
}

func BenchmarkEncodeSlice(b *testing.B) {
	buf := [128]byte{}
	msg := struct {
		S []int
	}{
		S: []int{0, 1, 2, 3, 4, 5, 6, 7, 8, 9},
	}

	size := Size(msg)
	data := buf[:size]
	b.SetBytes(int64(size))

	for range b.N {
		if _, err := MarshalTo(data, &msg); err != nil {
			b.Fatal(err)
		}
	}
}
```

## File: `proto/error.go`
```go
package proto

import (
	"errors"
	"fmt"
)

var ErrWireTypeUnknown = errors.New("unknown wire type")

type UnmarshalFieldError struct {
	FieldNumer int
	WireType   int
	Err        error
}

func (e *UnmarshalFieldError) Error() string {
	return fmt.Sprintf("field number %d with wire type %d: %v", e.FieldNumer, e.WireType, e.Err)
}

func (e *UnmarshalFieldError) Unwrap() error { return e.Err }

func fieldError(f fieldNumber, t wireType, err error) error {
	return &UnmarshalFieldError{
		FieldNumer: int(f),
		WireType:   int(t),
		Err:        err,
	}
}
```

## File: `proto/float32.go`
```go
package proto

import (
	"math"
	"unsafe"
)

var float32Codec = codec{
	wire:   fixed32,
	size:   sizeOfFloat32,
	encode: encodeFloat32,
	decode: decodeFloat32,
}

func sizeOfFloat32(p unsafe.Pointer, flags flags) int {
	if p != nil {
		if v := *(*float32)(p); v != 0 || flags.has(wantzero) || math.Signbit(float64(v)) {
			return 4
		}
	}
	return 0
}

func encodeFloat32(b []byte, p unsafe.Pointer, flags flags) (int, error) {
	if p != nil {
		if v := *(*float32)(p); v != 0 || flags.has(wantzero) || math.Signbit(float64(v)) {
			return encodeLE32(b, math.Float32bits(v))
		}
	}
	return 0, nil
}

func decodeFloat32(b []byte, p unsafe.Pointer, _ flags) (int, error) {
	v, n, err := decodeLE32(b)
	*(*float32)(p) = math.Float32frombits(v)
	return n, err
}
```

## File: `proto/float64.go`
```go
package proto

import (
	"math"
	"unsafe"
)

var float64Codec = codec{
	wire:   fixed64,
	size:   sizeOfFloat64,
	encode: encodeFloat64,
	decode: decodeFloat64,
}

func sizeOfFloat64(p unsafe.Pointer, flags flags) int {
	if p != nil {
		if v := *(*float64)(p); v != 0 || flags.has(wantzero) || math.Signbit(v) {
			return 8
		}
	}
	return 0
}

func encodeFloat64(b []byte, p unsafe.Pointer, flags flags) (int, error) {
	if p != nil {
		if v := *(*float64)(p); v != 0 || flags.has(wantzero) || math.Signbit(v) {
			return encodeLE64(b, math.Float64bits(v))
		}
	}
	return 0, nil
}

func decodeFloat64(b []byte, p unsafe.Pointer, _ flags) (int, error) {
	v, n, err := decodeLE64(b)
	*(*float64)(p) = math.Float64frombits(v)
	return n, err
}
```

## File: `proto/int.go`
```go
package proto

import (
	"unsafe"
)

var intCodec = codec{
	wire:   varint,
	size:   sizeOfInt,
	encode: encodeInt,
	decode: decodeInt,
}

func sizeOfInt(p unsafe.Pointer, flags flags) int {
	if p != nil {
		if v := *(*int)(p); v != 0 || flags.has(wantzero) {
			return sizeOfVarint(flags.uint64(int64(v)))
		}
	}
	return 0
}

func encodeInt(b []byte, p unsafe.Pointer, flags flags) (int, error) {
	if p != nil {
		if v := *(*int)(p); v != 0 || flags.has(wantzero) {
			return encodeVarint(b, flags.uint64(int64(v)))
		}
	}
	return 0, nil
}

func decodeInt(b []byte, p unsafe.Pointer, flags flags) (int, error) {
	v, n, err := decodeVarint(b)
	*(*int)(p) = int(flags.int64(v))
	return n, err
}
```

## File: `proto/int32.go`
```go
package proto

import (
	"fmt"
	"math"
	"unsafe"
)

var int32Codec = codec{
	wire:   varint,
	size:   sizeOfInt32,
	encode: encodeInt32,
	decode: decodeInt32,
}

func sizeOfInt32(p unsafe.Pointer, flags flags) int {
	if p != nil {
		if v := *(*int32)(p); v != 0 || flags.has(wantzero) {
			return sizeOfVarint(flags.uint64(int64(v)))
		}
	}
	return 0
}

func encodeInt32(b []byte, p unsafe.Pointer, flags flags) (int, error) {
	if p != nil {
		if v := *(*int32)(p); v != 0 || flags.has(wantzero) {
			return encodeVarint(b, flags.uint64(int64(v)))
		}
	}
	return 0, nil
}

func decodeInt32(b []byte, p unsafe.Pointer, flags flags) (int, error) {
	u, n, err := decodeVarint(b)
	v := flags.int64(u)
	if v < math.MinInt32 || v > math.MaxInt32 {
		return n, fmt.Errorf("integer overflow decoding %v into int32", v)
	}
	*(*int32)(p) = int32(v)
	return n, err
}
```

## File: `proto/int64.go`
```go
package proto

import "unsafe"

var int64Codec = codec{
	wire:   varint,
	size:   sizeOfInt64,
	encode: encodeInt64,
	decode: decodeInt64,
}

func sizeOfInt64(p unsafe.Pointer, flags flags) int {
	if p != nil {
		if v := *(*int64)(p); v != 0 || flags.has(wantzero) {
			return sizeOfVarint(flags.uint64(v))
		}
	}
	return 0
}

func encodeInt64(b []byte, p unsafe.Pointer, flags flags) (int, error) {
	if p != nil {
		if v := *(*int64)(p); v != 0 || flags.has(wantzero) {
			return encodeVarint(b, flags.uint64(v))
		}
	}
	return 0, nil
}

func decodeInt64(b []byte, p unsafe.Pointer, flags flags) (int, error) {
	v, n, err := decodeVarint(b)
	*(*int64)(p) = flags.int64(v)
	return n, err
}
```

## File: `proto/map.go`
```go
package proto

import (
	"io"
	"reflect"
	"sync"
	"unsafe"

	. "github.com/segmentio/encoding/internal/runtime_reflect"
)

const (
	zeroSize = 1 // sizeOfVarint(0)
)

type mapField struct {
	number   uint16
	keyFlags uint8
	valFlags uint8
	keyCodec *codec
	valCodec *codec
}

func mapCodecOf(t reflect.Type, f *mapField, seen map[reflect.Type]*codec) *codec {
	m := new(codec)
	seen[t] = m

	m.wire = varlen
	m.size = mapSizeFuncOf(t, f)
	m.encode = mapEncodeFuncOf(t, f)
	m.decode = mapDecodeFuncOf(t, f, seen)
	return m
}

func mapSizeFuncOf(t reflect.Type, f *mapField) sizeFunc {
	mapTagSize := sizeOfTag(fieldNumber(f.number), varlen)
	keyTagSize := sizeOfTag(1, wireType(f.keyCodec.wire))
	valTagSize := sizeOfTag(2, wireType(f.valCodec.wire))
	return func(p unsafe.Pointer, flags flags) int {
		if p == nil {
			return 0
		}

		if !flags.has(inline) {
			p = *(*unsafe.Pointer)(p)
		}

		n := 0
		m := MapIter{}
		defer m.Done()

		for m.Init(pointer(t), p); m.HasNext(); m.Next() {
			keySize := f.keyCodec.size(m.Key(), wantzero)
			valSize := f.valCodec.size(m.Value(), wantzero)

			if keySize > 0 {
				n += keyTagSize + keySize
				if (f.keyFlags & embedded) != 0 {
					n += sizeOfVarint(uint64(keySize))
				}
			}

			if valSize > 0 {
				n += valTagSize + valSize
				if (f.valFlags & embedded) != 0 {
					n += sizeOfVarint(uint64(valSize))
				}
			}

			n += mapTagSize + sizeOfVarint(uint64(keySize+valSize))
		}

		if n == 0 {
			n = mapTagSize + zeroSize
		}

		return n
	}
}

func mapEncodeFuncOf(t reflect.Type, f *mapField) encodeFunc {
	keyTag := [1]byte{}
	valTag := [1]byte{}
	encodeTag(keyTag[:], 1, f.keyCodec.wire)
	encodeTag(valTag[:], 2, f.valCodec.wire)

	number := fieldNumber(f.number)
	mapTag := make([]byte, sizeOfTag(number, varlen)+zeroSize)
	encodeTag(mapTag, number, varlen)

	zero := mapTag
	mapTag = mapTag[:len(mapTag)-1]

	return func(b []byte, p unsafe.Pointer, flags flags) (int, error) {
		if p == nil {
			return 0, nil
		}

		if !flags.has(inline) {
			p = *(*unsafe.Pointer)(p)
		}

		offset := 0
		m := MapIter{}
		defer m.Done()

		for m.Init(pointer(t), p); m.HasNext(); m.Next() {
			key := m.Key()
			val := m.Value()

			keySize := f.keyCodec.size(key, wantzero)
			valSize := f.valCodec.size(val, wantzero)
			elemSize := keySize + valSize

			if keySize > 0 {
				elemSize += len(keyTag)
				if (f.keyFlags & embedded) != 0 {
					elemSize += sizeOfVarint(uint64(keySize))
				}
			}

			if valSize > 0 {
				elemSize += len(valTag)
				if (f.valFlags & embedded) != 0 {
					elemSize += sizeOfVarint(uint64(valSize))
				}
			}

			n := copy(b[offset:], mapTag)
			offset += n
			if n < len(mapTag) {
				return offset, io.ErrShortBuffer
			}
			n, err := encodeVarint(b[offset:], uint64(elemSize))
			offset += n
			if err != nil {
				return offset, err
			}

			if keySize > 0 {
				n := copy(b[offset:], keyTag[:])
				offset += n
				if n < len(keyTag) {
					return offset, io.ErrShortBuffer
				}

				if (f.keyFlags & embedded) != 0 {
					n, err := encodeVarint(b[offset:], uint64(keySize))
					offset += n
					if err != nil {
						return offset, err
					}
				}

				if (len(b) - offset) < keySize {
					return len(b), io.ErrShortBuffer
				}

				n, err := f.keyCodec.encode(b[offset:offset+keySize], key, wantzero)
				offset += n
				if err != nil {
					return offset, err
				}
			}

			if valSize > 0 {
				n := copy(b[offset:], valTag[:])
				offset += n
				if n < len(valTag) {
					return n, io.ErrShortBuffer
				}

				if (f.valFlags & embedded) != 0 {
					n, err := encodeVarint(b[offset:], uint64(valSize))
					offset += n
					if err != nil {
						return offset, err
					}
				}

				if (len(b) - offset) < valSize {
					return len(b), io.ErrShortBuffer
				}

				n, err := f.valCodec.encode(b[offset:offset+valSize], val, wantzero)
				offset += n
				if err != nil {
					return offset, err
				}
			}
		}

		if offset == 0 {
			if offset = copy(b, zero); offset < len(zero) {
				return offset, io.ErrShortBuffer
			}
		}

		return offset, nil
	}
}

func mapDecodeFuncOf(t reflect.Type, f *mapField, seen map[reflect.Type]*codec) decodeFunc {
	structType := reflect.StructOf([]reflect.StructField{
		{Name: "Key", Type: t.Key()},
		{Name: "Elem", Type: t.Elem()},
	})

	structCodec := codecOf(structType, seen)
	structPool := new(sync.Pool)
	structZero := pointer(reflect.Zero(structType).Interface())

	valueType := t.Elem()
	valueOffset := structType.Field(1).Offset

	mtype := pointer(t)
	stype := pointer(structType)
	vtype := pointer(valueType)

	return func(b []byte, p unsafe.Pointer, _ flags) (int, error) {
		m := (*unsafe.Pointer)(p)
		if *m == nil {
			*m = MakeMap(mtype, 10)
		}
		if len(b) == 0 {
			return 0, nil
		}

		s := pointer(structPool.Get())
		if s == nil {
			s = unsafe.Pointer(reflect.New(structType).Pointer())
		}

		n, err := structCodec.decode(b, s, noflags)
		if err == nil {
			v := MapAssign(mtype, *m, s)
			Assign(vtype, v, unsafe.Pointer(uintptr(s)+valueOffset))
		}

		Assign(stype, s, structZero)
		structPool.Put(s)
		return n, err
	}
}
```

## File: `proto/message.go`
```go
package proto

import (
	"encoding/binary"
	"fmt"
	"io"
	"math"
	"reflect"
	"unsafe"
)

// Message is an interface implemented by types that supported being encoded to
// and decoded from protobuf.
type Message interface {
	// Size is the size of the protobuf representation (in bytes).
	Size() int

	// Marshal writes the message to the byte slice passed as argument.
	Marshal([]byte) error

	// Unmarshal reads the message from the byte slice passed as argument.
	Unmarshal([]byte) error
}

// RawMessage represents a raw protobuf-encoded message.
type RawMessage []byte

// Size satisfies the Message interface.
func (m RawMessage) Size() int { return len(m) }

// Marshal satisfies the Message interface.
func (m RawMessage) Marshal(b []byte) error {
	copy(b, m)
	return nil
}

// Unmarshal satisfies the Message interface.
func (m *RawMessage) Unmarshal(b []byte) error {
	*m = make([]byte, len(b))
	copy(*m, b)
	return nil
}

// Rewrite satisfies the Rewriter interface.
func (m RawMessage) Rewrite(out, _ []byte) ([]byte, error) {
	return append(out, m...), nil
}

// FieldNumber represents a protobuf field number.
type FieldNumber uint

func (f FieldNumber) Bool(v bool) RawMessage {
	var x uint64
	if v {
		x = 1
	}
	return AppendVarint(nil, f, x)
}

func (f FieldNumber) Int(v int) RawMessage {
	return f.Int64(int64(v))
}

func (f FieldNumber) Int32(v int32) RawMessage {
	return f.Int64(int64(v))
}

func (f FieldNumber) Int64(v int64) RawMessage {
	return AppendVarint(nil, f, uint64(v))
}

func (f FieldNumber) Uint(v uint) RawMessage {
	return f.Uint64(uint64(v))
}

func (f FieldNumber) Uint32(v uint32) RawMessage {
	return f.Uint64(uint64(v))
}

func (f FieldNumber) Uint64(v uint64) RawMessage {
	return AppendVarint(nil, f, v)
}

func (f FieldNumber) Fixed32(v uint32) RawMessage {
	return AppendFixed32(nil, f, v)
}

func (f FieldNumber) Fixed64(v uint64) RawMessage {
	return AppendFixed64(nil, f, v)
}

func (f FieldNumber) Float32(v float32) RawMessage {
	return f.Fixed32(math.Float32bits(v))
}

func (f FieldNumber) Float64(v float64) RawMessage {
	return f.Fixed64(math.Float64bits(v))
}

func (f FieldNumber) String(v string) RawMessage {
	return f.Bytes([]byte(v))
}

func (f FieldNumber) Bytes(v []byte) RawMessage {
	return AppendVarlen(nil, f, v)
}

// Value constructs a RawMessage for field number f from v.
func (f FieldNumber) Value(v any) RawMessage {
	switch x := v.(type) {
	case bool:
		return f.Bool(x)
	case int:
		return f.Int(x)
	case int32:
		return f.Int32(x)
	case int64:
		return f.Int64(x)
	case uint:
		return f.Uint(x)
	case uint32:
		return f.Uint32(x)
	case uint64:
		return f.Uint64(x)
	case float32:
		return f.Float32(x)
	case float64:
		return f.Float64(x)
	case string:
		return f.String(x)
	case []byte:
		return f.Bytes(x)
	default:
		panic("cannot rewrite value of unsupported type")
	}
}

// The WireType enumeration represents the different protobuf wire types.
type WireType uint

const (
	Varint  WireType = 0
	Fixed64 WireType = 1
	Varlen  WireType = 2
	Fixed32 WireType = 5
	// Wire types 3 and 4 were used for StartGroup and EndGroup, but are
	// deprecated so we don't expose them here.
	//
	// https://developers.google.com/protocol-buffers/docs/encoding#structure
)

func (wt WireType) String() string {
	return wireType(wt).String()
}

func Append(m RawMessage, f FieldNumber, t WireType, v []byte) RawMessage {
	b := [20]byte{}
	n, _ := encodeVarint(b[:], EncodeTag(f, t))
	if t == Varlen {
		n1, _ := encodeVarint(b[n:], uint64(len(v)))
		n += n1
	}
	m = append(m, b[:n]...)
	m = append(m, v...)
	return m
}

func AppendVarint(m RawMessage, f FieldNumber, v uint64) RawMessage {
	b := [10]byte{}
	n, _ := encodeVarint(b[:], v)
	return Append(m, f, Varint, b[:n])
}

func AppendVarlen(m RawMessage, f FieldNumber, v []byte) RawMessage {
	return Append(m, f, Varlen, v)
}

func AppendFixed32(m RawMessage, f FieldNumber, v uint32) RawMessage {
	b := [4]byte{}
	binary.LittleEndian.PutUint32(b[:], v)
	return Append(m, f, Fixed32, b[:])
}

func AppendFixed64(m RawMessage, f FieldNumber, v uint64) RawMessage {
	b := [8]byte{}
	binary.LittleEndian.PutUint64(b[:], v)
	return Append(m, f, Fixed64, b[:])
}

func Parse(m []byte) (FieldNumber, WireType, RawValue, RawMessage, error) {
	tag, n, err := decodeVarint(m)
	if err != nil {
		return 0, 0, nil, m, fmt.Errorf("decoding protobuf field number: %w", err)
	}
	m = m[n:]
	f, t := DecodeTag(tag)

	switch t {
	case Varint:
		_, n, err := decodeVarint(m)
		if err != nil {
			return f, t, nil, m, fmt.Errorf("decoding varint field %d: %w", f, err)
		}
		if len(m) < n {
			return f, t, nil, m, fmt.Errorf("decoding varint field %d: %w", f, io.ErrUnexpectedEOF)
		}
		return f, t, RawValue(m[:n]), m[n:], nil

	case Varlen:
		l, n, err := decodeVarint(m) // length
		if err != nil {
			return f, t, nil, m, fmt.Errorf("decoding varlen field %d: %w", f, err)
		}
		if uint64(len(m)-n) < l {
			return f, t, nil, m, fmt.Errorf("decoding varlen field %d: %w", f, io.ErrUnexpectedEOF)
		}
		return f, t, RawValue(m[n : n+int(l)]), m[n+int(l):], nil

	case Fixed32:
		if len(m) < 4 {
			return f, t, nil, m, fmt.Errorf("decoding fixed32 field %d: %w", f, io.ErrUnexpectedEOF)
		}
		return f, t, RawValue(m[:4]), m[4:], nil

	case Fixed64:
		if len(m) < 8 {
			return f, t, nil, m, fmt.Errorf("decoding fixed64 field %d: %w", f, io.ErrUnexpectedEOF)
		}
		return f, t, RawValue(m[:8]), m[8:], nil

	default:
		return f, t, nil, m, fmt.Errorf("invalid wire type: %d", t)
	}
}

// Scan calls fn for each protobuf field in the message b.
//
// The iteration stops when all fields have been scanned, fn returns false, or
// an error is seen.
func Scan(b []byte, fn func(FieldNumber, WireType, RawValue) (bool, error)) error {
	for len(b) != 0 {
		f, t, v, m, err := Parse(b)
		if err != nil {
			return err
		}
		if ok, err := fn(f, t, v); !ok {
			return err
		}
		b = m
	}
	return nil
}

// RawValue represents a single protobuf value.
//
// RawValue instances are returned by Parse and share the backing array of the
// RawMessage that they were decoded from.
type RawValue []byte

// Varint decodes v as a varint.
//
// The content of v will always be a valid varint if v was returned by a call to
// Parse and the associated wire type was Varint. In other cases, the behavior
// of Varint is undefined.
func (v RawValue) Varint() uint64 {
	u, _, _ := decodeVarint(v)
	return u
}

// Fixed32 decodes v as a fixed32.
//
// The content of v will always be a valid fixed32 if v was returned by a call
// to Parse and the associated wire type was Fixed32. In other cases, the
// behavior of Fixed32 is undefined.
func (v RawValue) Fixed32() uint32 {
	return binary.LittleEndian.Uint32(v)
}

// Fixed64 decodes v as a fixed64.
//
// The content of v will always be a valid fixed64 if v was returned by a call
// to Parse and the associated wire type was Fixed64. In other cases, the
// behavior of Fixed64 is undefined.
func (v RawValue) Fixed64() uint64 {
	return binary.LittleEndian.Uint64(v)
}

var (
	_ Message  = &RawMessage{}
	_ Rewriter = RawMessage{}
)

func messageCodecOf(t reflect.Type) *codec {
	return &codec{
		wire:   varlen,
		size:   messageSizeFuncOf(t),
		encode: messageEncodeFuncOf(t),
		decode: messageDecodeFuncOf(t),
	}
}

func messageSizeFuncOf(t reflect.Type) sizeFunc {
	return func(p unsafe.Pointer, flags flags) int {
		if p != nil {
			if m := reflect.NewAt(t, p).Interface().(Message); m != nil {
				size := m.Size()
				if flags.has(toplevel) {
					return size
				}
				return sizeOfVarlen(size)
			}
		}
		return 0
	}
}

func messageEncodeFuncOf(t reflect.Type) encodeFunc {
	return func(b []byte, p unsafe.Pointer, flags flags) (int, error) {
		if p != nil {
			if m := reflect.NewAt(t, p).Interface().(Message); m != nil {
				size := m.Size()

				if flags.has(toplevel) {
					if len(b) < size {
						return 0, io.ErrShortBuffer
					}
					return len(b), m.Marshal(b)
				}

				vlen := sizeOfVarlen(size)
				if len(b) < vlen {
					return 0, io.ErrShortBuffer
				}

				n, err := encodeVarint(b, uint64(size))
				if err != nil {
					return n, err
				}

				return vlen, m.Marshal(b[n:])
			}
		}
		return 0, nil
	}
}

func messageDecodeFuncOf(t reflect.Type) decodeFunc {
	return func(b []byte, p unsafe.Pointer, flags flags) (int, error) {
		m := reflect.NewAt(t, p).Interface().(Message)

		if flags.has(toplevel) {
			return len(b), m.Unmarshal(b)
		}

		v, n, err := decodeVarlen(b)
		if err != nil {
			return n, err
		}

		return n + len(v), m.Unmarshal(v)
	}
}
```

## File: `proto/message_test.go`
```go
package proto

import (
	"bytes"
	"math"
	"testing"
)

func TestAppendVarint(t *testing.T) {
	m := AppendVarint(nil, 1, 42)

	f, w, v, r, err := Parse(m)
	if err != nil {
		t.Fatal(err)
	}
	if len(r) != 0 {
		t.Fatal("unexpected trailing bytes:", r)
	}
	if w != Varint {
		t.Fatal("unexpected wire type:", t)
	}
	if f != 1 {
		t.Fatal("unexpected field number:", f)
	}
	if u := v.Varint(); u != 42 {
		t.Fatal("value mismatch, want 42 but got", u)
	}
}

func TestAppendVarlen(t *testing.T) {
	m := AppendVarlen(nil, 1, []byte("Hello World!"))

	f, w, v, r, err := Parse(m)
	if err != nil {
		t.Fatal(err)
	}
	if len(r) != 0 {
		t.Fatal("unexpected trailing bytes:", r)
	}
	if w != Varlen {
		t.Fatal("unexpected wire type:", t)
	}
	if f != 1 {
		t.Fatal("unexpected field number:", f)
	}
	if string(v) != "Hello World!" {
		t.Fatalf("value mismatch, want \"Hello World!\" but got %q", v)
	}
}

func TestAppendFixed32(t *testing.T) {
	m := AppendFixed32(nil, 1, 42)

	f, w, v, r, err := Parse(m)
	if err != nil {
		t.Fatal(err)
	}
	if len(r) != 0 {
		t.Fatal("unexpected trailing bytes:", r)
	}
	if w != Fixed32 {
		t.Fatal("unexpected wire type:", t)
	}
	if f != 1 {
		t.Fatal("unexpected field number:", f)
	}
	if u := v.Fixed32(); u != 42 {
		t.Fatal("value mismatch, want 42 but got", u)
	}
}

func TestAppendFixed64(t *testing.T) {
	m := AppendFixed64(nil, 1, 42)

	f, w, v, r, err := Parse(m)
	if err != nil {
		t.Fatal(err)
	}
	if len(r) != 0 {
		t.Fatal("unexpected trailing bytes:", r)
	}
	if w != Fixed64 {
		t.Fatal("unexpected wire type:", t)
	}
	if f != 1 {
		t.Fatal("unexpected field number:", f)
	}
	if u := v.Fixed64(); u != 42 {
		t.Fatal("value mismatch, want 42 but got", u)
	}
}

func TestDecodeFromAppend(t *testing.T) {
	m := RawMessage(nil)
	m = AppendVarint(m, 1, math.MaxUint64)
	m = AppendVarlen(m, 2, []byte("Hello World!"))
	m = AppendFixed32(m, 3, math.Float32bits(42.0))
	m = AppendFixed64(m, 4, math.Float64bits(1234.0))

	type M struct {
		I   int
		S   string
		F32 float32
		F64 float64
	}

	x := M{}

	if err := Unmarshal(m, &x); err != nil {
		t.Fatal(err)
	}
	if x.I != -1 {
		t.Errorf("x.I=%d", x.I)
	}
	if x.S != "Hello World!" {
		t.Errorf("x.S=%q", x.S)
	}
	if x.F32 != 42 {
		t.Errorf("x.F32=%g", x.F32)
	}
	if x.F64 != 1234 {
		t.Errorf("x.F64=%g", x.F64)
	}
}

func TestDecodeFixture(t *testing.T) {
	m := loadProtobuf(t, "message.pb")
	m = assertParse(t, m, 1, Varint, makeVarint(10))
	m = assertParse(t, m, 2, Varint, makeVarint(20))
	m = assertParse(t, m, 3, Varint, makeVarint(30))
	m = assertParse(t, m, 4, Varlen, []byte("Hello World!"))
	assertEmpty(t, m)
}

func assertParse(t *testing.T, m RawMessage, f FieldNumber, w WireType, b []byte) RawMessage {
	t.Helper()

	f0, w0, b0, m, err := Parse(m)
	if err != nil {
		t.Fatal(err)
	}

	if f0 != f {
		t.Errorf("field number mismatch, want %d but got %d", f, f0)
	}

	if w0 != w {
		t.Errorf("wire type mismatch, want %d but got %d", w, w0)
	}

	if !bytes.Equal(b0, b) {
		t.Errorf("value mismatch, want %v but got %v", b, b0)
	}

	return m
}

func assertEmpty(t *testing.T, m RawMessage) {
	t.Helper()

	if len(m) != 0 {
		t.Errorf("unexpected content remained in the protobuf message: %v", m)
	}
}

func BenchmarkScan(b *testing.B) {
	m, _ := Marshal(&message{
		A: 1,
		B: 2,
		C: 3,
		S: submessage{
			X: "hello",
			Y: "world",
		},
	})

	for range b.N {
		Scan(m, func(f FieldNumber, t WireType, v RawValue) (bool, error) {
			switch f {
			case 1, 2, 3:
				return true, nil
			case 4:
				err := Scan(v, func(f FieldNumber, t WireType, v RawValue) (bool, error) {
					switch f {
					case 1, 2:
						return true, nil
					default:
						b.Error("invalid field number:", f)
						return false, nil
					}
				})
				return err != nil, err
			default:
				b.Error("invalid field number:", f)
				return false, nil
			}
		})
	}
}
```

## File: `proto/pointer.go`
```go
package proto

import (
	"reflect"
	"unsafe"
)

func pointerCodecOf(t reflect.Type, seen map[reflect.Type]*codec) *codec {
	p := new(codec)
	seen[t] = p
	c := codecOf(t.Elem(), seen)
	p.wire = c.wire
	p.size = pointerSizeFuncOf(t, c)
	p.encode = pointerEncodeFuncOf(t, c)
	p.decode = pointerDecodeFuncOf(t, c)
	return p
}

func pointerSizeFuncOf(t reflect.Type, c *codec) sizeFunc {
	return func(p unsafe.Pointer, flags flags) int {
		if p != nil {
			if !flags.has(inline) {
				p = *(*unsafe.Pointer)(p)
			}
			return c.size(p, flags.without(inline).with(wantzero))
		}
		return 0
	}
}

func pointerEncodeFuncOf(t reflect.Type, c *codec) encodeFunc {
	return func(b []byte, p unsafe.Pointer, flags flags) (int, error) {
		if p != nil {
			if !flags.has(inline) {
				p = *(*unsafe.Pointer)(p)
			}
			return c.encode(b, p, flags.without(inline).with(wantzero))
		}
		return 0, nil
	}
}

func pointerDecodeFuncOf(t reflect.Type, c *codec) decodeFunc {
	t = t.Elem()
	return func(b []byte, p unsafe.Pointer, flags flags) (int, error) {
		v := (*unsafe.Pointer)(p)
		if *v == nil {
			*v = unsafe.Pointer(reflect.New(t).Pointer())
		}
		return c.decode(b, *v, flags)
	}
}
```

## File: `proto/proto.go`
```go
package proto

import (
	"fmt"
	"reflect"
	"sync/atomic"
	"unsafe"
)

func Size(v any) int {
	t, p := inspect(v)
	c := cachedCodecOf(t)
	return c.size(p, inline|toplevel)
}

func Marshal(v any) ([]byte, error) {
	t, p := inspect(v)
	c := cachedCodecOf(t)
	b := make([]byte, c.size(p, inline|toplevel))
	_, err := c.encode(b, p, inline|toplevel)
	if err != nil {
		return nil, fmt.Errorf("proto.Marshal(%T): %w", v, err)
	}
	return b, nil
}

func MarshalTo(b []byte, v any) (int, error) {
	t, p := inspect(v)
	c := cachedCodecOf(t)
	n, err := c.encode(b, p, inline|toplevel)
	if err != nil {
		err = fmt.Errorf("proto.MarshalTo: %w", err)
	}
	return n, err
}

func Unmarshal(b []byte, v any) error {
	if len(b) == 0 {
		// An empty input is a valid protobuf message with all fields set to the
		// zero-value.
		reflect.ValueOf(v).Elem().Set(reflect.Zero(reflect.TypeOf(v).Elem()))
		return nil
	}

	t, p := inspect(v)
	t = t.Elem() // Unmarshal must be passed a pointer
	c := cachedCodecOf(t)

	n, err := c.decode(b, p, toplevel)
	if err != nil {
		return err
	}
	if n < len(b) {
		return fmt.Errorf("proto.Unmarshal(%T): read=%d < buffer=%d", v, n, len(b))
	}
	return nil
}

type flags uintptr

const (
	noflags  flags = 0
	inline   flags = 1 << 0
	wantzero flags = 1 << 1
	// Shared with structField.flags in struct.go:
	// zigzag flags = 1 << 2
	toplevel flags = 1 << 3
)

func (f flags) has(x flags) bool {
	return (f & x) != 0
}

func (f flags) with(x flags) flags {
	return f | x
}

func (f flags) without(x flags) flags {
	return f & ^x
}

func (f flags) uint64(i int64) uint64 {
	if f.has(zigzag) {
		return encodeZigZag64(i)
	} else {
		return uint64(i)
	}
}

func (f flags) int64(u uint64) int64 {
	if f.has(zigzag) {
		return decodeZigZag64(u)
	} else {
		return int64(u)
	}
}

type iface struct {
	typ unsafe.Pointer
	ptr unsafe.Pointer
}

func inspect(v any) (reflect.Type, unsafe.Pointer) {
	return reflect.TypeOf(v), pointer(v)
}

func pointer(v any) unsafe.Pointer {
	return (*iface)(unsafe.Pointer(&v)).ptr
}

func inlined(t reflect.Type) bool {
	switch t.Kind() {
	case reflect.Ptr:
		return true
	case reflect.Map:
		return true
	case reflect.Struct:
		return t.NumField() == 1 && inlined(t.Field(0).Type)
	default:
		return false
	}
}

type fieldNumber uint

type wireType uint

const (
	varint  wireType = 0
	fixed64 wireType = 1
	varlen  wireType = 2
	fixed32 wireType = 5
)

func (wt wireType) String() string {
	switch wt {
	case varint:
		return "varint"
	case varlen:
		return "varlen"
	case fixed32:
		return "fixed32"
	case fixed64:
		return "fixed64"
	default:
		return "unknown"
	}
}

type codec struct {
	wire   wireType
	size   sizeFunc
	encode encodeFunc
	decode decodeFunc
}

var codecCache atomic.Value // map[unsafe.Pointer]*codec

func loadCachedCodec(t reflect.Type) (*codec, map[unsafe.Pointer]*codec) {
	cache, _ := codecCache.Load().(map[unsafe.Pointer]*codec)
	return cache[pointer(t)], cache
}

func storeCachedCodec(newCache map[unsafe.Pointer]*codec) {
	codecCache.Store(newCache)
}

func cachedCodecOf(t reflect.Type) *codec {
	c, oldCache := loadCachedCodec(t)
	if c != nil {
		return c
	}

	var p reflect.Type
	isPtr := t.Kind() == reflect.Ptr
	if isPtr {
		p = t
		t = t.Elem()
	} else {
		p = reflect.PtrTo(t)
	}

	seen := make(map[reflect.Type]*codec)
	c1 := codecOf(t, seen)
	c2 := codecOf(p, seen)

	newCache := make(map[unsafe.Pointer]*codec, len(oldCache)+2)
	for p, c := range oldCache {
		newCache[p] = c
	}

	newCache[pointer(t)] = c1
	newCache[pointer(p)] = c2
	storeCachedCodec(newCache)

	if isPtr {
		return c2
	} else {
		return c1
	}
}

func codecOf(t reflect.Type, seen map[reflect.Type]*codec) *codec {
	if c := seen[t]; c != nil {
		return c
	}

	switch {
	case implements(t, messageType):
		return messageCodecOf(t)
	case implements(t, customMessageType) && !implements(t, protoMessageType):
		return customCodecOf(t)
	}

	switch t.Kind() {
	case reflect.Bool:
		return &boolCodec
	case reflect.Int:
		return &intCodec
	case reflect.Int32:
		return &int32Codec
	case reflect.Int64:
		return &int64Codec
	case reflect.Uint:
		return &uintCodec
	case reflect.Uint32:
		return &uint32Codec
	case reflect.Uint64:
		return &uint64Codec
	case reflect.Float32:
		return &float32Codec
	case reflect.Float64:
		return &float64Codec
	case reflect.String:
		return &stringCodec
	case reflect.Array:
		elem := t.Elem()
		switch elem.Kind() {
		case reflect.Uint8:
			return byteArrayCodecOf(t, seen)
		}
	case reflect.Slice:
		elem := t.Elem()
		switch elem.Kind() {
		case reflect.Uint8:
			return &bytesCodec
		}
	case reflect.Struct:
		return structCodecOf(t, seen)
	case reflect.Ptr:
		return pointerCodecOf(t, seen)
	}

	panic("unsupported type: " + t.String())
}

// backward compatibility with gogoproto custom types.
type customMessage interface {
	Size() int
	MarshalTo([]byte) (int, error)
	Unmarshal([]byte) error
}

type protoMessage interface {
	ProtoMessage()
}

var (
	messageType       = reflect.TypeOf((*Message)(nil)).Elem()
	customMessageType = reflect.TypeOf((*customMessage)(nil)).Elem()
	protoMessageType  = reflect.TypeOf((*protoMessage)(nil)).Elem()
)

func implements(t, iface reflect.Type) bool {
	return t.Implements(iface) || reflect.PtrTo(t).Implements(iface)
}
```

## File: `proto/proto_test.go`
```go
package proto

import (
	"encoding/binary"
	"fmt"
	"math"
	"os"
	"reflect"
	"testing"
)

func TestEncodeDecodeVarint(t *testing.T) {
	b := [8]byte{}

	n, err := encodeVarint(b[:], 42)
	if err != nil {
		t.Fatal(err)
	}

	v, n2, err := decodeVarint(b[:n])
	if err != nil {
		t.Fatal(err)
	}
	if v != 42 {
		t.Errorf("decoded value mismatch: want %d, got %d", 42, v)
	}
	if n2 != n {
		t.Errorf("decoded byte count mismatch: want %d, got %d", n, n2)
	}
}

func TestEncodeDecodeVarintZigZag(t *testing.T) {
	b := [8]byte{}

	n, err := encodeVarintZigZag(b[:], -42)
	if err != nil {
		t.Fatal(err)
	}

	v, n2, err := decodeVarintZigZag(b[:n])
	if err != nil {
		t.Fatal(err)
	}
	if v != -42 {
		t.Errorf("decoded value mismatch: want %d, got %d", -42, v)
	}
	if n2 != n {
		t.Errorf("decoded byte count mismatch: want %d, got %d", n, n2)
	}
}

func TestEncodeDecodeTag(t *testing.T) {
	b := [8]byte{}

	n, err := encodeTag(b[:], 1, varint)
	if err != nil {
		t.Fatal(err)
	}

	num, typ, n2, err := decodeTag(b[:n])
	if err != nil {
		t.Fatal(err)
	}
	if num != 1 {
		t.Errorf("decoded field number mismatch: want %d, got %d", 1, num)
	}
	if typ != varint {
		t.Errorf("decoded wire type mismatch: want %d, got %d", varint, typ)
	}
	if n2 != n {
		t.Errorf("decoded byte count mismatch: want %d, got %d", n, n2)
	}
}

type key struct {
	Hi uint64
	Lo uint64
}

type message struct {
	A int
	B int
	C int
	S submessage
}

type submessage struct {
	X string
	Y string
}

type structWithMap struct {
	M map[int]string
}

type custom [16]byte

func (c *custom) Size() int { return len(c) }

func (c *custom) MarshalTo(b []byte) (int, error) {
	return copy(b, c[:]), nil
}

func (c *custom) Unmarshal(b []byte) error {
	copy(c[:], b)
	return nil
}

type messageWithRawMessage struct {
	Raw RawMessage
}

type messageWithCustomField struct {
	Custom custom
}

func TestMarshalUnmarshal(t *testing.T) {
	intVal := 42
	values := []any{
		// bool
		true,
		false,

		// zig-zag varint
		0,
		1,
		1234567890,
		-1,
		-1234567890,

		// sfixed32
		int32(0),
		int32(math.MinInt32),
		int32(math.MaxInt32),

		// sfixed64
		int64(0),
		int64(math.MinInt64),
		int64(math.MaxInt64),

		// varint
		uint(0),
		uint(1),
		uint(1234567890),

		// fixed32
		uint32(0),
		uint32(1234567890),

		// fixed64
		uint64(0),
		uint64(1234567890),

		// float
		float32(0),
		float32(math.Copysign(0, -1)),
		float32(0.1234),

		// double
		float64(0),
		float64(math.Copysign(0, -1)),
		float64(0.1234),

		// string
		"",
		"A",
		"Hello World!",

		// bytes
		([]byte)(nil),
		[]byte(""),
		[]byte("A"),
		[]byte("Hello World!"),

		// messages
		struct{ B bool }{B: false},
		struct{ B bool }{B: true},

		struct{ I int }{I: 0},
		struct{ I int }{I: 1},

		struct{ I32 int32 }{I32: 0},
		struct{ I32 int32 }{I32: -1234567890},

		struct{ I64 int64 }{I64: 0},
		struct{ I64 int64 }{I64: -1234567890},

		struct{ U int }{U: 0},
		struct{ U int }{U: 1},

		struct{ U32 uint32 }{U32: 0},
		struct{ U32 uint32 }{U32: 1234567890},

		struct{ U64 uint64 }{U64: 0},
		struct{ U64 uint64 }{U64: 1234567890},

		struct{ F32 float32 }{F32: 0},
		struct{ F32 float32 }{F32: 0.1234},

		struct{ F64 float64 }{F64: 0},
		struct{ F64 float64 }{F64: 0.1234},

		struct{ S string }{S: ""},
		struct{ S string }{S: "E"},

		struct{ B []byte }{B: nil},
		struct{ B []byte }{B: []byte{}},
		struct{ B []byte }{B: []byte{1, 2, 3}},

		&message{
			A: 1,
			B: 2,
			C: 3,
			S: submessage{
				X: "hello",
				Y: "world",
			},
		},

		struct {
			Min int64 `protobuf:"zigzag64,1,opt,name=min,proto3"`
			Max int64 `protobuf:"zigzag64,2,opt,name=min,proto3"`
		}{Min: math.MinInt64, Max: math.MaxInt64},

		// pointers
		struct{ M *message }{M: nil},
		struct {
			M1 *message
			M2 *message
			M3 *message
		}{
			M1: &message{A: 10, B: 100, C: 1000},
			M2: &message{S: submessage{X: "42"}},
		},

		// byte arrays
		[0]byte{},
		[8]byte{},
		[16]byte{0x0, 0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7, 0x8, 0x9, 0xA, 0xB, 0xC, 0xD, 0xE, 0xF},
		&[...]byte{},
		&[...]byte{3, 2, 1},

		// slices (repeated)
		struct{ S []int }{S: nil},
		struct{ S []int }{S: []int{0}},
		struct{ S []int }{S: []int{0, 0, 0}},
		struct{ S []int }{S: []int{1, 2, 3}},
		struct{ S []string }{S: nil},
		struct{ S []string }{S: []string{""}},
		struct{ S []string }{S: []string{"A", "B", "C"}},
		struct{ K []key }{
			K: []key{
				{Hi: 0, Lo: 0},
				{Hi: 0, Lo: 1},
				{Hi: 0, Lo: 2},
				{Hi: 0, Lo: 3},
				{Hi: 0, Lo: 4},
			},
		},

		// maps (repeated)
		struct{ M map[int]string }{},
		struct{ M map[int]string }{
			M: map[int]string{0: ""},
		},
		struct{ M map[int]string }{
			M: map[int]string{0: "A", 1: "B", 2: "C"},
		},
		&struct{ M map[int]string }{
			M: map[int]string{0: "A", 1: "B", 2: "C"},
		},
		struct {
			M1 map[int]int
			M2 map[string]string
			M3 map[string]message
			M4 map[string]*message
			M5 map[key]uint
		}{
			M1: map[int]int{0: 1},
			M2: map[string]string{"": "A"},
			M3: map[string]message{
				"m0": {},
				"m1": {A: 42},
				"m3": {S: submessage{X: "X", Y: "Y"}},
			},
			M4: map[string]*message{
				"m0": {},
				"m1": {A: 42},
				"m3": {S: submessage{X: "X", Y: "Y"}},
			},
			M5: map[key]uint{
				{Hi: 0, Lo: 0}:                           0,
				{Hi: 1, Lo: 0}:                           1,
				{Hi: 0, Lo: 1}:                           2,
				{Hi: math.MaxUint64, Lo: math.MaxUint64}: 3,
			},
		},

		// more complex inlined types use cases
		struct{ I *int }{},
		struct{ I *int }{I: new(int)},
		struct{ I *int }{I: &intVal},
		struct{ M *message }{},
		struct{ M *message }{M: new(message)},
		struct{ M map[int]int }{},
		struct{ M map[int]int }{M: map[int]int{}},
		struct{ S structWithMap }{
			S: structWithMap{
				M: map[int]string{0: "A", 1: "B", 2: "C"},
			},
		},
		&struct{ S structWithMap }{
			S: structWithMap{
				M: map[int]string{0: "A", 1: "B", 2: "C"},
			},
		},

		// raw messages
		RawMessage(nil),
		RawMessage{0x08, 0x96, 0x01},
		messageWithRawMessage{
			Raw: RawMessage{1, 2, 3, 4},
		},
		struct {
			A int
			B string
			C RawMessage
		}{A: 42, B: "Hello World!", C: RawMessage{1, 2, 3, 4}},

		// custom messages
		custom{},
		custom{0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15},
		messageWithCustomField{
			Custom: custom{1: 42},
		},
		struct {
			A int
			B string
			C custom
		}{A: 42, B: "Hello World!", C: custom{1: 42}},
	}

	for _, v := range values {
		t.Run(fmt.Sprintf("%T/%+v", v, v), func(t *testing.T) {
			n := Size(v)

			b, err := Marshal(v)
			if err != nil {
				t.Fatal(err)
			}
			if n != len(b) {
				t.Fatalf("value size and buffer length mismatch (%d != %d)", n, len(b))
			}

			p := reflect.New(reflect.TypeOf(v))
			if err := Unmarshal(b, p.Interface()); err != nil {
				t.Fatal(err)
			}

			x := p.Elem().Interface()
			if !reflect.DeepEqual(v, x) {
				t.Errorf("values mismatch:\nexpected: %#v\nfound:    %#v", v, x)
			}
		})
	}
}

func loadProtobuf(t *testing.T, fileName string) RawMessage {
	b, err := os.ReadFile("fixtures/protobuf/" + fileName)
	if err != nil {
		t.Fatal(err)
	}
	return RawMessage(b)
}

func makeVarint(v uint64) []byte {
	b := [12]byte{}
	n := binary.PutUvarint(b[:], v)
	return b[:n]
}

func makeFixed32(v uint32) []byte {
	b := [4]byte{}
	binary.LittleEndian.PutUint32(b[:], v)
	return b[:]
}

func makeFixed64(v uint64) []byte {
	b := [8]byte{}
	binary.LittleEndian.PutUint64(b[:], v)
	return b[:]
}
```

## File: `proto/reflect.go`
```go
package proto

import (
	"fmt"
	"reflect"
	"strconv"
	"strings"
	"sync"
	"sync/atomic"
)

// Kind is an enumeration representing the various data types supported by the
// protobuf language.
type Kind int

const (
	Bool Kind = iota
	Int32
	Int64
	Sint32
	Sint64
	Uint32
	Uint64
	Fix32
	Fix64
	Sfix32
	Sfix64
	Float
	Double
	String
	Bytes
	Map
	Struct
)

// Type is an interface similar to reflect.Type. Values implementing this
// interface represent high level protobuf types.
//
// Type values are safe to use concurrently from multiple goroutines.
//
// Types are comparable value.
type Type interface {
	// Returns a human-readable representation of the type.
	String() string

	// Returns the name of the type.
	Name() string

	// Kind returns the kind of protobuf values that are represented.
	Kind() Kind

	// When the Type represents a protobuf map, calling this method returns the
	// type of the map keys.
	//
	// If the Type is not a map type, the method panics.
	Key() Type

	// When the Type represents a protobuf map, calling this method returns the
	// type of the map values.
	//
	// If the Type is not a map type, the method panics.
	Elem() Type

	// Returns the protobuf wire type for the Type it is called on.
	WireType() WireType

	// Returns the number of fields in the protobuf message.
	//
	// If the Type does not represent a struct type, the method returns zero.
	NumField() int

	// Returns the Field at the given in Type.
	//
	// If the Type does not represent a struct type, the method panics.
	Field(int) Field

	// Returns the Field with the given name in Type.
	//
	// If the Type does not represent a struct type, or if the field does not
	// exist, the method panics.
	FieldByName(string) Field

	// Returns the Field with the given number in Type.
	//
	// If the Type does not represent a struct type, or if the field does not
	// exist, the method panics.
	FieldByNumber(FieldNumber) Field

	// For unsigned types, convert to their zig-zag form.
	//
	// The method uses the following table to perform the conversion:
	//
	//  base    | zig-zag
	//	--------+---------
	//	int32   | sint32
	//	int64   | sint64
	//	uint32  | sint32
	//	uint64  | sint64
	//	fixed32 | sfixed32
	//	fixed64 | sfixed64
	//
	// If the type cannot be converted to a zig-zag type, the method panics.
	ZigZag() Type
}

// TypeOf returns the protobuf type used to represent a go type.
//
// The function uses the following table to map Go types to Protobuf:
//
//	Go      | Protobuf
//	--------+---------
//	bool    | bool
//	int     | int64
//	int32   | int32
//	int64   | int64
//	uint    | uint64
//	uint32  | uint32
//	uint64  | uint64
//	float32 | float
//	float64 | double
//	string  | string
//	[]byte  | bytes
//	map     | map
//	struct  | message
//
// Pointer types are also supported and automatically dereferenced.
func TypeOf(t reflect.Type) Type {
	cache, _ := typesCache.Load().(map[reflect.Type]Type)
	if r, ok := cache[t]; ok {
		return r
	}

	typesMutex.Lock()
	defer typesMutex.Unlock()

	cache, _ = typesCache.Load().(map[reflect.Type]Type)
	if r, ok := cache[t]; ok {
		return r
	}

	seen := map[reflect.Type]Type{}
	r := typeOf(t, seen)

	newCache := make(map[reflect.Type]Type, len(cache)+len(seen))
	for t, r := range cache {
		newCache[t] = r
	}

	for t, r := range seen {
		if x, ok := newCache[t]; ok {
			r = x
		} else {
			newCache[t] = r
		}
	}

	if x, ok := newCache[t]; ok {
		r = x
	} else {
		newCache[t] = r
	}

	typesCache.Store(newCache)
	return r
}

func typeOf(t reflect.Type, seen map[reflect.Type]Type) Type {
	if r, ok := seen[t]; ok {
		return r
	}

	switch {
	case implements(t, messageType):
		return &opaqueMessageType{}
	case implements(t, customMessageType) && !implements(t, protoMessageType):
		return &primitiveTypes[Bytes]
	}

	switch t.Kind() {
	case reflect.Bool:
		return &primitiveTypes[Bool]
	case reflect.Int:
		return &primitiveTypes[Int64]
	case reflect.Int32:
		return &primitiveTypes[Int32]
	case reflect.Int64:
		return &primitiveTypes[Int64]
	case reflect.Uint:
		return &primitiveTypes[Uint64]
	case reflect.Uint32:
		return &primitiveTypes[Uint32]
	case reflect.Uint64:
		return &primitiveTypes[Uint64]
	case reflect.Float32:
		return &primitiveTypes[Float]
	case reflect.Float64:
		return &primitiveTypes[Double]
	case reflect.String:
		return &primitiveTypes[String]
	case reflect.Slice, reflect.Array:
		if t.Elem().Kind() == reflect.Uint8 {
			return &primitiveTypes[Bytes]
		}
	case reflect.Map:
		return mapTypeOf(t, seen)
	case reflect.Struct:
		return structTypeOf(t, seen)
	case reflect.Ptr:
		return typeOf(t.Elem(), seen)
	}

	panic(fmt.Errorf("cannot construct protobuf type from go value of type %s", t))
}

var (
	typesMutex sync.Mutex
	typesCache atomic.Value // map[reflect.Type]Type{}
)

type Field struct {
	Index    int
	Number   FieldNumber
	Name     string
	Type     Type
	Repeated bool
}

type primitiveType struct {
	name   string
	kind   Kind
	wire   WireType
	zigzag Kind
}

func (t *primitiveType) String() string {
	return t.name
}

func (t *primitiveType) Name() string {
	return t.name
}

func (t *primitiveType) Kind() Kind {
	return t.kind
}

func (t *primitiveType) Key() Type {
	panic(fmt.Errorf("proto.Type.Key: called on unsupported type: %s", t))
}

func (t *primitiveType) Elem() Type {
	panic(fmt.Errorf("proto.Type.Elem: called on unsupported type: %s", t))
}

func (t *primitiveType) WireType() WireType {
	return t.wire
}

func (t *primitiveType) NumField() int {
	return 0
}

func (t *primitiveType) Field(int) Field {
	panic(fmt.Errorf("proto.Type.Field: called on unsupported type: %s", t))
}

func (t *primitiveType) FieldByName(string) Field {
	panic(fmt.Errorf("proto.Type.FieldByName: called on unsupported type: %s", t))
}

func (t *primitiveType) FieldByNumber(FieldNumber) Field {
	panic(fmt.Errorf("proto.Type.FieldByNumber: called on unsupported type: %s", t))
}

func (t *primitiveType) ZigZag() Type {
	if t.zigzag == 0 {
		panic(fmt.Errorf("proto.Type.ZigZag: called on unsupported type: %s", t))
	}
	return &primitiveTypes[t.zigzag]
}

var primitiveTypes = [...]primitiveType{
	{name: "bool", kind: Bool, wire: Varint},
	{name: "int32", kind: Int32, wire: Varint, zigzag: Sint32},
	{name: "int64", kind: Int64, wire: Varint, zigzag: Sint64},
	{name: "sint32", kind: Sint32, wire: Varint},
	{name: "sint64", kind: Sint64, wire: Varint},
	{name: "uint32", kind: Uint32, wire: Varint, zigzag: Sint32},
	{name: "uint64", kind: Uint64, wire: Varint, zigzag: Sint64},
	{name: "fixed32", kind: Fix32, wire: Fixed32, zigzag: Sfix32},
	{name: "fixed64", kind: Fix64, wire: Fixed64, zigzag: Sfix64},
	{name: "sfixed32", kind: Sfix32, wire: Fixed32},
	{name: "sfixed64", kind: Sfix64, wire: Fixed64},
	{name: "float", kind: Float, wire: Fixed32},
	{name: "double", kind: Double, wire: Fixed64},
	{name: "string", kind: String, wire: Varlen},
	{name: "bytes", kind: Bytes, wire: Varlen},
}

func mapTypeOf(t reflect.Type, seen map[reflect.Type]Type) *mapType {
	mt := &mapType{}
	seen[t] = mt
	mt.key = typeOf(t.Key(), seen)
	mt.elem = typeOf(t.Elem(), seen)
	return mt
}

type mapType struct {
	key  Type
	elem Type
}

func (t *mapType) String() string {
	return fmt.Sprintf("map<%s, %s>", t.key.Name(), t.elem.Name())
}

func (t *mapType) Name() string {
	return t.String()
}

func (t *mapType) Kind() Kind {
	return Map
}

func (t *mapType) Key() Type {
	return t.key
}

func (t *mapType) Elem() Type {
	return t.elem
}

func (t *mapType) WireType() WireType {
	return Varlen
}

func (t *mapType) NumField() int {
	return 0
}

func (t *mapType) Field(int) Field {
	panic(fmt.Errorf("proto.Type.Field: called on unsupported type: %s", t))
}

func (t *mapType) FieldByName(string) Field {
	panic(fmt.Errorf("proto.Type.FieldByName: called on unsupported type: %s", t))
}

func (t *mapType) FieldByNumber(FieldNumber) Field {
	panic(fmt.Errorf("proto.Type.FieldByNumber: called on unsupported type: %s", t))
}

func (t *mapType) ZigZag() Type {
	panic(fmt.Errorf("proto.Type.ZigZag: called on unsupported type: %s", t))
}

func structTypeOf(t reflect.Type, seen map[reflect.Type]Type) *structType {
	st := &structType{
		name:           t.Name(),
		fieldsByName:   make(map[string]int),
		fieldsByNumber: make(map[FieldNumber]int),
	}

	seen[t] = st

	fieldNumber := FieldNumber(0)
	taggedFields := FieldNumber(0)

	for i := range t.NumField() {
		f := t.Field(i)

		if f.PkgPath != "" {
			continue // unexported
		}

		repeated := false
		if f.Type.Kind() == reflect.Slice && f.Type.Elem().Kind() != reflect.Uint8 {
			repeated = true
			f.Type = f.Type.Elem() // for typeOf
		}

		fieldName := f.Name
		fieldType := typeOf(f.Type, seen)

		if tag, ok := f.Tag.Lookup("protobuf"); ok {
			if fieldNumber != taggedFields {
				panic("conflicting use of struct tag and naked fields")
			}
			t, err := parseStructTag(tag)
			if err != nil {
				panic(err)
			}

			fieldName = t.name
			fieldNumber = t.fieldNumber
			taggedFields = t.fieldNumber
			// Because maps are represented as repeated varlen fields on the
			// wire, the generated protobuf code sets the `rep` attribute on
			// the struct fields.
			repeated = t.repeated && f.Type.Kind() != reflect.Map

			if t.zigzag {
				fieldType = fieldType.ZigZag()
			}
		} else if fieldNumber == 0 && len(st.fields) != 0 {
			panic("conflicting use of struct tag and naked fields")
		} else {
			fieldNumber++
		}

		index := len(st.fields)
		st.fields = append(st.fields, Field{
			Index:    index,
			Number:   fieldNumber,
			Name:     fieldName,
			Type:     fieldType,
			Repeated: repeated,
		})
		st.fieldsByName[fieldName] = index
		st.fieldsByNumber[fieldNumber] = index
	}

	return st
}

type structType struct {
	name           string
	fields         []Field
	fieldsByName   map[string]int
	fieldsByNumber map[FieldNumber]int
}

func (t *structType) String() string {
	s := strings.Builder{}
	s.WriteString("message ")

	if t.name != "" {
		s.WriteString(t.name)
		s.WriteString(" ")
	}

	s.WriteString("{")

	for _, f := range t.fields {
		s.WriteString("\n  ")

		if f.Repeated {
			s.WriteString("repeated ")
		} else {
		}

		s.WriteString(f.Type.Name())
		s.WriteString(" ")
		s.WriteString(f.Name)
		s.WriteString(" = ")
		s.WriteString(strconv.Itoa(int(f.Number)))
		s.WriteString(";")
	}

	if len(t.fields) == 0 {
		s.WriteString("}")
	} else {
		s.WriteString("\n}")
	}

	return s.String()
}

func (t *structType) Name() string {
	return t.name
}

func (t *structType) Kind() Kind {
	return Struct
}

func (t *structType) Key() Type {
	panic(fmt.Errorf("proto.Type.Key: called on unsupported type: %s", t.name))
}

func (t *structType) Elem() Type {
	panic(fmt.Errorf("proto.Type.Elem: called on unsupported type: %s", t.name))
}

func (t *structType) WireType() WireType {
	return Varlen
}

func (t *structType) NumField() int {
	return len(t.fields)
}

func (t *structType) Field(index int) Field {
	if index >= 0 && index < len(t.fields) {
		return t.fields[index]
	}
	panic(fmt.Errorf("proto.Type.Field: protobuf message field out of bounds: %d/%d", index, len(t.fields)))
}

func (t *structType) FieldByName(name string) Field {
	i, ok := t.fieldsByName[name]
	if ok {
		return t.fields[i]
	}
	panic(fmt.Errorf("proto.Type.FieldByName: protobuf message has not field named %q", name))
}

func (t *structType) FieldByNumber(number FieldNumber) Field {
	i, ok := t.fieldsByNumber[number]
	if ok {
		return t.fields[i]
	}
	panic(fmt.Errorf("proto.Type.FieldByNumber: protobuf message has no field number %d", number))
}

func (t *structType) ZigZag() Type {
	panic(fmt.Errorf("proto.Type.ZigZag: called on unsupported type: %s", t.name))
}

type structTag struct {
	name        string
	enum        string
	json        string
	version     int
	wireType    WireType
	fieldNumber FieldNumber
	extensions  map[string]string
	repeated    bool
	zigzag      bool
}

func parseStructTag(tag string) (structTag, error) {
	t := structTag{
		version:    2,
		extensions: make(map[string]string),
	}

	for i, f := range splitFields(tag) {
		switch i {
		case 0:
			switch f {
			case "varint":
				t.wireType = Varint
			case "bytes":
				t.wireType = Varlen
			case "fixed32":
				t.wireType = Fixed32
			case "fixed64":
				t.wireType = Fixed64
			case "zigzag32":
				t.wireType = Varint
				t.zigzag = true
			case "zigzag64":
				t.wireType = Varint
				t.zigzag = true
			default:
				return t, fmt.Errorf("unsupported wire type in struct tag %q: %s", tag, f)
			}

		case 1:
			n, err := strconv.Atoi(f)
			if err != nil {
				return t, fmt.Errorf("unsupported field number in struct tag %q: %w", tag, err)
			}
			t.fieldNumber = FieldNumber(n)

		case 2:
			switch f {
			case "opt":
				// not sure what this is for
			case "rep":
				t.repeated = true
			default:
				return t, fmt.Errorf("unsupported field option in struct tag %q: %s", tag, f)
			}

		default:
			name, value := splitNameValue(f)
			switch name {
			case "name":
				t.name = value
			case "enum":
				t.enum = value
			case "json":
				t.json = value
			case "proto3":
				t.version = 3
			default:
				t.extensions[name] = value
			}
		}
	}

	return t, nil
}

func splitFields(s string) []string {
	return strings.Split(s, ",")
}

func splitNameValue(s string) (name, value string) {
	i := strings.IndexByte(s, '=')
	if i < 0 {
		return strings.TrimSpace(s), ""
	} else {
		return strings.TrimSpace(s[:i]), strings.TrimSpace(s[i+1:])
	}
}

type opaqueMessageType struct{}

func (t *opaqueMessageType) String() string {
	return "bytes"
}

func (t *opaqueMessageType) Name() string {
	return "bytes"
}

func (t *opaqueMessageType) Kind() Kind {
	return Struct
}

func (t *opaqueMessageType) Key() Type {
	panic(fmt.Errorf("proto.Type.Key: called on unsupported type: %s", t))
}

func (t *opaqueMessageType) Elem() Type {
	panic(fmt.Errorf("proto.Type.Elem: called on unsupported type: %s", t))
}

func (t *opaqueMessageType) WireType() WireType {
	return Varlen
}

func (t *opaqueMessageType) NumField() int {
	return 0
}

func (t *opaqueMessageType) Field(int) Field {
	panic(fmt.Errorf("proto.Type.Field: called on unsupported type: %s", t))
}

func (t *opaqueMessageType) FieldByName(string) Field {
	panic(fmt.Errorf("proto.Type.FieldByName: called on unsupported type: %s", t))
}

func (t *opaqueMessageType) FieldByNumber(FieldNumber) Field {
	panic(fmt.Errorf("proto.Type.FieldByNumber: called on unsupported type: %s", t))
}

func (t *opaqueMessageType) ZigZag() Type {
	panic(fmt.Errorf("proto.Type.ZigZag: called on unsupported type: %s", t))
}
```

## File: `proto/reflect_test.go`
```go
package proto

import (
	"fmt"
	"reflect"
	"testing"
)

type RecursiveMessage struct {
	Next *RecursiveMessage `protobuf:"bytes,1,opt,name=next,proto3"`
}

func TestTypeOf(t *testing.T) {
	tests := []struct {
		value any
		proto string
	}{
		// primitive types
		{value: true, proto: "bool"},
		{value: int(1), proto: "int64"},
		{value: int32(1), proto: "int32"},
		{value: int64(1), proto: "int64"},
		{value: uint(1), proto: "uint64"},
		{value: uint32(1), proto: "uint32"},
		{value: uint64(1), proto: "uint64"},
		{value: float32(1), proto: "float"},
		{value: float64(1), proto: "double"},
		{value: "hello", proto: "string"},
		{value: []byte("A"), proto: "bytes"},

		// map types
		{value: map[int]string{}, proto: "map<int64, string>"},

		// struct types
		{
			value: struct{}{},
			proto: `message {}`,
		},

		{
			value: struct{ A int }{},
			proto: `message {
  int64 A = 1;
}`,
		},

		{
			value: struct {
				A int    `protobuf:"varint,1,opt,name=hello,proto3"`
				B string `protobuf:"bytes,3,rep,name=world,proto3"`
			}{},
			proto: `message {
  int64 hello = 1;
  repeated string world = 3;
}`,
		},

		{
			value: RecursiveMessage{},
			proto: `message RecursiveMessage {
  RecursiveMessage next = 1;
}`,
		},

		{
			value: struct {
				M RawMessage
			}{},
			proto: `message {
  bytes M = 1;
}`,
		},
	}

	for _, test := range tests {
		t.Run(fmt.Sprintf("%T", test.value), func(t *testing.T) {
			typ := TypeOf(reflect.TypeOf(test.value))
			str := typ.String()

			if str != test.proto {
				t.Error("protobuf representation mismatch")
				t.Log("want:", test.proto)
				t.Log("got: ", str)
			}
		})
	}
}

func TestTypesAreEqual(t *testing.T) {
	if TypeOf(reflect.TypeOf(true)) != TypeOf(reflect.TypeOf(false)) {
		t.Error("type of true is not equal to type of false")
	}
}

func TestTypesAreNotEqual(t *testing.T) {
	if TypeOf(reflect.TypeOf(false)) == TypeOf(reflect.TypeOf(0)) {
		t.Error("type of bool equal type of int")
	}
}

func TestParseStructTag(t *testing.T) {
	tests := []struct {
		str string
		tag structTag
	}{
		{
			str: `bytes,1,rep,name=next,proto3`,
			tag: structTag{
				name:        "next",
				version:     3,
				wireType:    Varlen,
				fieldNumber: 1,
				extensions:  map[string]string{},
				repeated:    true,
			},
		},

		{
			str: `bytes,5,opt,name=key,proto3`,
			tag: structTag{
				name:        "key",
				version:     3,
				wireType:    Varlen,
				fieldNumber: 5,
				extensions:  map[string]string{},
			},
		},

		{
			str: `fixed64,6,opt,name=seed,proto3`,
			tag: structTag{
				name:        "seed",
				version:     3,
				wireType:    Fixed64,
				fieldNumber: 6,
				extensions:  map[string]string{},
			},
		},

		{
			str: `varint,8,opt,name=expire_after,json=expireAfter,proto3`,
			tag: structTag{
				name:        "expire_after",
				json:        "expireAfter",
				version:     3,
				wireType:    Varint,
				fieldNumber: 8,
				extensions:  map[string]string{},
			},
		},

		{
			str: `bytes,17,opt,name=batch_key,json=batchKey,proto3,customtype=U128`,
			tag: structTag{
				name:        "batch_key",
				json:        "batchKey",
				version:     3,
				wireType:    Varlen,
				fieldNumber: 17,
				extensions: map[string]string{
					"customtype": "U128",
				},
			},
		},
	}

	for _, test := range tests {
		t.Run(test.str, func(t *testing.T) {
			tag, err := parseStructTag(test.str)
			if err != nil {
				t.Fatal(err)
			}
			if !reflect.DeepEqual(tag, test.tag) {
				t.Errorf("struct tag mismatch\nwant: %+v\ngot: %+v", test.tag, tag)
			}
		})
	}
}
```

## File: `proto/rewrite.go`
```go
package proto

import (
	"fmt"

	"github.com/segmentio/encoding/json"
)

// Rewriter is an interface implemented by types that support rewriting protobuf
// messages.
type Rewriter interface {
	// The function is expected to append the new content to the byte slice
	// passed as argument. If it wasn't able to perform the rewrite, it must
	// return a non-nil error.
	Rewrite(out, in []byte) ([]byte, error)
}

type identity struct{}

func (identity) Rewrite(out, in []byte) ([]byte, error) {
	return append(out, in...), nil
}

// MultiRewriter constructs a Rewriter which applies all rewriters passed as
// arguments.
func MultiRewriter(rewriters ...Rewriter) Rewriter {
	if len(rewriters) == 1 {
		return rewriters[0]
	}
	m := &multiRewriter{rewriters: make([]Rewriter, len(rewriters))}
	copy(m.rewriters, rewriters)
	return m
}

type multiRewriter struct {
	rewriters []Rewriter
}

func (m *multiRewriter) Rewrite(out, in []byte) ([]byte, error) {
	var err error

	for _, rw := range m.rewriters {
		if out, err = rw.Rewrite(out, in); err != nil {
			return out, err
		}
	}

	return out, nil
}

// RewriteFunc is a function type implementing the Rewriter interface.
type RewriteFunc func([]byte, []byte) ([]byte, error)

// Rewrite satisfies the Rewriter interface.
func (r RewriteFunc) Rewrite(out, in []byte) ([]byte, error) {
	return r(out, in)
}

// MessageRewriter maps field numbers to rewrite rules, satisfying the Rewriter
// interace to support composing rewrite rules.
type MessageRewriter []Rewriter

// Rewrite applies the rewrite rule matching f in r, satisfies the Rewriter
// interface.
func (r MessageRewriter) Rewrite(out, in []byte) ([]byte, error) {
	seen := make(fieldset, 4)

	if n := seen.len(); len(r) >= n {
		seen = makeFieldset(len(r) + 1)
	}

	for len(in) != 0 {
		f, t, v, m, err := Parse(in)
		if err != nil {
			return out, err
		}

		if i := int(f); i >= 0 && i < len(r) && r[i] != nil {
			if !seen.has(i) {
				seen.set(i)
				if out, err = r[i].Rewrite(out, v); err != nil {
					return out, err
				}
			}
		} else {
			out = Append(out, f, t, v)
		}

		in = m
	}

	for i, f := range r {
		if f != nil && !seen.has(i) {
			b, err := r[i].Rewrite(out, nil)
			if err != nil {
				return b, err
			}
			out = b
		}
	}

	return out, nil
}

type fieldset []uint64

func makeFieldset(n int) fieldset {
	if (n % 64) != 0 {
		n = (n + 1) / 64
	} else {
		n /= 64
	}
	return make(fieldset, n)
}

func (f fieldset) len() int {
	return len(f) * 64
}

func (f fieldset) has(i int) bool {
	x, y := f.index(i)
	return ((f[x] >> y) & 1) != 0
}

func (f fieldset) set(i int) {
	x, y := f.index(i)
	f[x] |= 1 << y
}

func (f fieldset) unset(i int) {
	x, y := f.index(i)
	f[x] &= ^(1 << y)
}

func (f fieldset) index(i int) (int, int) {
	return i / 64, i % 64
}

// ParseRewriteTemplate constructs a Rewriter for a protobuf type using the
// given json template to describe the rewrite rules.
//
// The json template contains a representation of the message that is used as the
// source values to overwrite in the protobuf targeted by the resulting rewriter.
//
// The rules are an optional set of RewriterRules that can provide alternative
// Rewriters from the default used for the field type. These rules are given the
// json.RawMessage bytes from the template, and they are expected to create a
// Rewriter to be applied against the target protobuf.
func ParseRewriteTemplate(typ Type, jsonTemplate []byte, rules ...RewriterRules) (Rewriter, error) {
	switch typ.Kind() {
	case Struct:
		return parseRewriteTemplateStruct(typ, 0, jsonTemplate, rules...)
	default:
		return nil, fmt.Errorf("cannot construct a rewrite template from a non-struct type %s", typ.Name())
	}
}

func parseRewriteTemplate(t Type, f FieldNumber, j json.RawMessage, rule any) (Rewriter, error) {
	if rwer, ok := rule.(Rewriterer); ok {
		return rwer.Rewriter(t, f, j)
	}

	switch t.Kind() {
	case Bool:
		return parseRewriteTemplateBool(t, f, j)
	case Int32:
		return parseRewriteTemplateInt32(t, f, j)
	case Int64:
		return parseRewriteTemplateInt64(t, f, j)
	case Sint32:
		return parseRewriteTemplateSint32(t, f, j)
	case Sint64:
		return parseRewriteTemplateSint64(t, f, j)
	case Uint32:
		return parseRewriteTemplateUint64(t, f, j)
	case Uint64:
		return parseRewriteTemplateUint64(t, f, j)
	case Fix32:
		return parseRewriteTemplateFix32(t, f, j)
	case Fix64:
		return parseRewriteTemplateFix64(t, f, j)
	case Sfix32:
		return parseRewriteTemplateSfix32(t, f, j)
	case Sfix64:
		return parseRewriteTemplateSfix64(t, f, j)
	case Float:
		return parseRewriteTemplateFloat(t, f, j)
	case Double:
		return parseRewriteTemplateDouble(t, f, j)
	case String:
		return parseRewriteTemplateString(t, f, j)
	case Bytes:
		return parseRewriteTemplateBytes(t, f, j)
	case Map:
		return parseRewriteTemplateMap(t, f, j)
	case Struct:
		sub, n, ok := [1]RewriterRules{}, 0, false
		if sub[0], ok = rule.(RewriterRules); ok {
			n = 1
		}
		return parseRewriteTemplateStruct(t, f, j, sub[:n]...)
	default:
		return nil, fmt.Errorf("cannot construct a rewriter from type %s", t.Name())
	}
}

func parseRewriteTemplateBool(t Type, f FieldNumber, j json.RawMessage) (Rewriter, error) {
	var v bool
	err := json.Unmarshal(j, &v)
	if !v || err != nil {
		return nil, err
	}
	return f.Bool(v), nil
}

func parseRewriteTemplateInt32(t Type, f FieldNumber, j json.RawMessage) (Rewriter, error) {
	var v int32
	err := json.Unmarshal(j, &v)
	if v == 0 || err != nil {
		return nil, err
	}
	return f.Int32(v), nil
}

func parseRewriteTemplateInt64(t Type, f FieldNumber, j json.RawMessage) (Rewriter, error) {
	var v int64
	err := json.Unmarshal(j, &v)
	if v == 0 || err != nil {
		return nil, err
	}
	return f.Int64(v), nil
}

func parseRewriteTemplateSint32(t Type, f FieldNumber, j json.RawMessage) (Rewriter, error) {
	var v int32
	err := json.Unmarshal(j, &v)
	if v == 0 || err != nil {
		return nil, err
	}
	return f.Uint32(encodeZigZag32(v)), nil
}

func parseRewriteTemplateSint64(t Type, f FieldNumber, j json.RawMessage) (Rewriter, error) {
	var v int64
	err := json.Unmarshal(j, &v)
	if v == 0 || err != nil {
		return nil, err
	}
	return f.Uint64(encodeZigZag64(v)), nil
}

func parseRewriteTemplateUint32(t Type, f FieldNumber, j json.RawMessage) (Rewriter, error) {
	var v uint32
	err := json.Unmarshal(j, &v)
	if v == 0 || err != nil {
		return nil, err
	}
	return f.Uint32(v), nil
}

func parseRewriteTemplateUint64(t Type, f FieldNumber, j json.RawMessage) (Rewriter, error) {
	var v uint64
	err := json.Unmarshal(j, &v)
	if v == 0 || err != nil {
		return nil, err
	}
	return f.Uint64(v), nil
}

func parseRewriteTemplateFix32(t Type, f FieldNumber, j json.RawMessage) (Rewriter, error) {
	var v uint32
	err := json.Unmarshal(j, &v)
	if v == 0 || err != nil {
		return nil, err
	}
	return f.Fixed32(v), nil
}

func parseRewriteTemplateFix64(t Type, f FieldNumber, j json.RawMessage) (Rewriter, error) {
	var v uint64
	err := json.Unmarshal(j, &v)
	if v == 0 || err != nil {
		return nil, err
	}
	return f.Fixed64(v), nil
}

func parseRewriteTemplateSfix32(t Type, f FieldNumber, j json.RawMessage) (Rewriter, error) {
	var v int32
	err := json.Unmarshal(j, &v)
	if v == 0 || err != nil {
		return nil, err
	}
	return f.Fixed32(encodeZigZag32(v)), nil
}

func parseRewriteTemplateSfix64(t Type, f FieldNumber, j json.RawMessage) (Rewriter, error) {
	var v int64
	err := json.Unmarshal(j, &v)
	if v == 0 || err != nil {
		return nil, err
	}
	return f.Fixed64(encodeZigZag64(v)), nil
}

func parseRewriteTemplateFloat(t Type, f FieldNumber, j json.RawMessage) (Rewriter, error) {
	var v float32
	err := json.Unmarshal(j, &v)
	if v == 0 || err != nil {
		return nil, err
	}
	return f.Float32(v), nil
}

func parseRewriteTemplateDouble(t Type, f FieldNumber, j json.RawMessage) (Rewriter, error) {
	var v float64
	err := json.Unmarshal(j, &v)
	if v == 0 || err != nil {
		return nil, err
	}
	return f.Float64(v), nil
}

func parseRewriteTemplateString(t Type, f FieldNumber, j json.RawMessage) (Rewriter, error) {
	var v string
	err := json.Unmarshal(j, &v)
	if v == "" || err != nil {
		return nil, err
	}
	return f.String(v), nil
}

func parseRewriteTemplateBytes(t Type, f FieldNumber, j json.RawMessage) (Rewriter, error) {
	var v string
	err := json.Unmarshal(j, &v)
	if v == "" || err != nil {
		return nil, err
	}
	return f.Bytes([]byte(v)), nil
}

func parseRewriteTemplateMap(t Type, f FieldNumber, j json.RawMessage) (Rewriter, error) {
	st := &structType{
		name: t.Name(),
		fields: []Field{
			{Index: 0, Number: 1, Name: "key", Type: t.Key()},
			{Index: 1, Number: 2, Name: "value", Type: t.Elem()},
		},
		fieldsByName:   make(map[string]int),
		fieldsByNumber: make(map[FieldNumber]int),
	}

	for _, f := range st.fields {
		st.fieldsByName[f.Name] = f.Index
		st.fieldsByNumber[f.Number] = f.Index
	}

	template := map[string]json.RawMessage{}

	if err := json.Unmarshal(j, &template); err != nil {
		return nil, err
	}

	maplist := make([]json.RawMessage, 0, len(template))

	for key, value := range template {
		b, err := json.Marshal(struct {
			Key   string          `json:"key"`
			Value json.RawMessage `json:"value"`
		}{
			Key:   key,
			Value: value,
		})
		if err != nil {
			return nil, err
		}
		maplist = append(maplist, b)
	}

	rewriters := make([]Rewriter, len(maplist))

	for i, b := range maplist {
		r, err := parseRewriteTemplateStruct(st, f, b)
		if err != nil {
			return nil, err
		}
		rewriters[i] = r
	}

	return MultiRewriter(rewriters...), nil
}

func parseRewriteTemplateStruct(t Type, f FieldNumber, j json.RawMessage, rules ...RewriterRules) (Rewriter, error) {
	template := map[string]json.RawMessage{}

	if err := json.Unmarshal(j, &template); err != nil {
		return nil, err
	}

	fieldsByName := map[string]Field{}

	for i := range t.NumField() {
		f := t.Field(i)
		fieldsByName[f.Name] = f
	}

	message := MessageRewriter{}
	rewriters := []Rewriter{}

	for k, v := range template {
		f, ok := fieldsByName[k]
		if !ok {
			return nil, fmt.Errorf("rewrite template contained an invalid field named %q", k)
		}

		var fields []json.RawMessage
		if f.Repeated {
			if err := json.Unmarshal(v, &fields); err != nil {
				return nil, err
			}
		} else {
			fields = []json.RawMessage{v}
		}

		var rule any
		for i := range rules {
			if r, ok := rules[i][f.Name]; ok {
				rule = r
				break
			}
		}

		rewriters = rewriters[:0]

		for _, v := range fields {
			rw, err := parseRewriteTemplate(f.Type, f.Number, v, rule)
			if err != nil {
				return nil, fmt.Errorf("%s: %w", k, err)
			}
			if rw != nil {
				rewriters = append(rewriters, rw)
			}
		}

		if cap(message) <= int(f.Number) {
			m := make(MessageRewriter, f.Number+1)
			copy(m, message)
			message = m
		}

		message[f.Number] = MultiRewriter(rewriters...)
	}

	if f != 0 {
		return &embddedRewriter{number: f, message: message}, nil
	}

	return message, nil
}

type embddedRewriter struct {
	number  FieldNumber
	message MessageRewriter
}

func (f *embddedRewriter) Rewrite(out, in []byte) ([]byte, error) {
	prefix := len(out)

	out, err := f.message.Rewrite(out, in)
	if err != nil {
		return nil, err
	}
	if len(out) == prefix {
		return out, nil
	}

	b := [24]byte{}
	n1, _ := encodeVarint(b[:], EncodeTag(f.number, Varlen))
	n2, _ := encodeVarint(b[n1:], uint64(len(out)-prefix))
	tagAndLen := n1 + n2

	out = append(out, b[:tagAndLen]...)
	copy(out[prefix+tagAndLen:], out[prefix:])
	copy(out[prefix:], b[:tagAndLen])
	return out, nil
}

// RewriterRules defines a set of rules for overriding the Rewriter used for any
// particular field. These maps may be nested for defining rules for struct members.
//
// For example:
//
//	rules := proto.RewriterRules {
//		"flags": proto.BitOr[uint64]{},
//		"nested": proto.RewriterRules {
//			"name": myCustomRewriter,
//		},
//	}
type RewriterRules map[string]any

// Rewriterer is the interface for producing a Rewriter for a given Type, FieldNumber
// and json.RawMessage. The JSON value is the JSON-encoded payload that should be
// decoded to produce the appropriate Rewriter. Implementations of the Rewriterer
// interface are added to the RewriterRules to specify the rules for performing
// custom rewrite logic.
type Rewriterer interface {
	Rewriter(Type, FieldNumber, json.RawMessage) (Rewriter, error)
}

// BitOr implments the Rewriterer interface for providing a bitwise-or rewrite
// logic for integers rather than replacing them. Instances of this type are
// zero-size, carrying only the generic type for creating the appropriate
// Rewriter when requested.
//
// Adding these to a RewriterRules looks like:
//
//	rules := proto.RewriterRules {
//		"flags": proto.BitOr[uint64]{},
//	}
//
// When used as a rule when rewriting from a template, the BitOr expects a JSON-
// encoded integer passed into the Rewriter method. This parsed integer is then
// used to perform a bitwise-or against the protobuf message that is being rewritten.
//
// The above example can then be used like:
//
//	template := []byte(`{"flags": 8}`) // n |= 0b1000
//	rw, err := proto.ParseRewriteTemplate(typ, template, rules)
type BitOr[T integer] struct{}

// integer is the contraint used by the BitOr Rewriterer and the bitOrRW Rewriter.
// Because these perform bitwise-or operations, the types must be integer-like.
type integer interface {
	~int | ~int32 | ~int64 | ~uint | ~uint32 | ~uint64
}

// Rewriter implements the Rewriterer interface. The JSON value provided to this
// method comes from the template used for rewriting. The returned Rewriter will use
// this JSON-encoded integer to perform a bitwise-or against the protobuf message
// that is being rewritten.
func (BitOr[T]) Rewriter(t Type, f FieldNumber, j json.RawMessage) (Rewriter, error) {
	var v T
	err := json.Unmarshal(j, &v)
	if err != nil {
		return nil, err
	}
	return BitOrRewriter(t, f, v)
}

// BitOrRewriter creates a bitwise-or Rewriter for a given field type and number.
// The mask is the value or'ed with values in the target protobuf.
func BitOrRewriter[T integer](t Type, f FieldNumber, mask T) (Rewriter, error) {
	switch t.Kind() {
	case Int32, Int64, Sint32, Sint64, Uint32, Uint64, Fix32, Fix64, Sfix32, Sfix64:
	default:
		return nil, fmt.Errorf("cannot construct a rewriter from type %s", t.Name())
	}
	return bitOrRW[T]{mask: mask, t: t, f: f}, nil
}

// bitOrRW is the Rewriter returned by the BitOr Rewriter method.
type bitOrRW[T integer] struct {
	mask T
	t    Type
	f    FieldNumber
}

// Rewrite implements the Rewriter interface performing a bitwise-or between the
// template value and the input value.
func (r bitOrRW[T]) Rewrite(out, in []byte) ([]byte, error) {
	var v T
	if err := Unmarshal(in, &v); err != nil {
		return nil, err
	}

	v |= r.mask

	switch r.t.Kind() {
	case Int32:
		return r.f.Int32(int32(v)).Rewrite(out, in)
	case Int64:
		return r.f.Int64(int64(v)).Rewrite(out, in)
	case Sint32:
		return r.f.Uint32(encodeZigZag32(int32(v))).Rewrite(out, in)
	case Sint64:
		return r.f.Uint64(encodeZigZag64(int64(v))).Rewrite(out, in)
	case Uint32, Uint64:
		return r.f.Uint64(uint64(v)).Rewrite(out, in)
	case Fix32:
		return r.f.Fixed32(uint32(v)).Rewrite(out, in)
	case Fix64:
		return r.f.Fixed64(uint64(v)).Rewrite(out, in)
	case Sfix32:
		return r.f.Fixed32(encodeZigZag32(int32(v))).Rewrite(out, in)
	case Sfix64:
		return r.f.Fixed64(encodeZigZag64(int64(v))).Rewrite(out, in)
	}

	panic("unreachable") // Kind is validated when creating instances
}
```

## File: `proto/rewrite_test.go`
```go
package proto

import (
	"reflect"
	"testing"
)

func TestRewrite(t *testing.T) {
	type message struct {
		A int
		B float32
		C float64
		D string
		M *message
	}

	tests := []struct {
		scenario string
		in       message
		out      message
		rw       Rewriter
	}{
		{
			scenario: "identity",
			in:       message{A: 42, M: &message{A: 1}},
			out:      message{A: 42, M: &message{A: 1}},
			rw:       MessageRewriter(nil),
		},

		{
			scenario: "rewrite field 1",
			in:       message{A: 21},
			out:      message{A: 42},
			rw: MessageRewriter{
				1: FieldNumber(1).Int(42),
			},
		},

		{
			scenario: "rewrite field 2",
			in:       message{A: 21, B: 0.125},
			out:      message{A: 21, B: -1},
			rw: MessageRewriter{
				2: FieldNumber(2).Float32(-1),
			},
		},

		{
			scenario: "rewrite field 3",
			in:       message{A: 21, B: 0.125, C: 0.0},
			out:      message{A: 21, B: 0.125, C: 1.0},
			rw: MessageRewriter{
				3: FieldNumber(3).Float64(+1),
			},
		},

		{
			scenario: "rewrite field 4",
			in:       message{A: 21, B: 0.125, C: 1.0, D: "A"},
			out:      message{A: 21, B: 0.125, C: 1.0, D: "Hello World!"},
			rw: MessageRewriter{
				4: FieldNumber(4).String("Hello World!"),
			},
		},
	}

	for _, test := range tests {
		t.Run(test.scenario, func(t *testing.T) {
			b, err := Marshal(test.in)
			if err != nil {
				t.Fatal(err)
			}

			b, err = test.rw.Rewrite(nil, b)
			if err != nil {
				t.Fatal(err)
			}

			m := message{}
			if err := Unmarshal(b, &m); err != nil {
				t.Fatal(err)
			}

			if !reflect.DeepEqual(m, test.out) {
				t.Errorf("messages mismatch:\nwant: %+v\ngot:  %+v", test.out, m)
			}
		})
	}
}

func TestParseRewriteTemplate(t *testing.T) {
	type submessage struct {
		Question string `protobuf:"bytes,1,opt,name=question,proto3"`
		Answer   string `protobuf:"bytes,2,opt,name=answer,proto3"`
	}

	type message struct {
		Field1 bool `protobuf:"varint,1,opt,name=field_1,proto3"`

		Field2 int   `protobuf:"varint,2,opt,name=field_2,proto3"`
		Field3 int32 `protobuf:"varint,3,opt,name=field_3,proto3"`
		Field4 int64 `protobuf:"varint,4,opt,name=field_4,proto3"`

		Field5 uint   `protobuf:"varint,5,opt,name=field_5,proto3"`
		Field6 uint32 `protobuf:"varint,6,opt,name=field_6,proto3"`
		Field7 uint64 `protobuf:"varint,7,opt,name=field_7,proto3"`

		Field8 int32 `protobuf:"zigzag32,8,opt,name=field_8,proto3"`
		Field9 int64 `protobuf:"zigzag64,9,opt,name=field_9,proto3"`

		Field10 float32 `protobuf:"fixed32,10,opt,name=field_10,proto3"`
		Field11 float64 `protobuf:"fixed64,11,opt,name=field_11,proto3"`

		Field12 string `protobuf:"bytes,12,opt,name=field_12,proto3"`
		Field13 []byte `protobuf:"bytes,13,opt,name=field_13,proto3"`

		Zero1 bool    `protobuf:"varint,21,opt,name=zero_1,proto3"`
		Zero2 int     `protobuf:"varint,22,opt,name=zero_2,proto3"`
		Zero3 int32   `protobuf:"varint,23,opt,name=zero_3,proto3"`
		Zero4 int64   `protobuf:"varint,24,opt,name=zero_4,proto3"`
		Zero5 uint    `protobuf:"varint,25,opt,name=zero_5,proto3"`
		Zero6 uint32  `protobuf:"varint,26,opt,name=zero_6,proto3"`
		Zero7 uint64  `protobuf:"varint,27,opt,name=zero_7,proto3"`
		Zero8 float32 `protobuf:"fixed32,28,opt,name=zero_8,proto3"`
		Zero9 float64 `protobuf:"fixed64,29,opt,name=zero_9,proto3"`

		Subfield    *submessage  `protobuf:"bytes,99,opt,name=subfield,proto3"`
		Submessages []submessage `protobuf:"bytes,100,rep,name=submessages,proto3"`

		Mapping map[string]int `protobuf:"bytes,200,opt,name=mapping,proto3"`
	}

	original := &message{
		Field1: false,

		Field2: -1,
		Field3: -2,
		Field4: -3,

		Field5: 1,
		Field6: 2,
		Field7: 3,

		Field8: -10,
		Field9: -11,

		Field10: 1.0,
		Field11: 2.0,

		Field12: "field 12",
		Field13: nil,

		Zero1: true,
		Zero2: 102,
		Zero3: 103,
		Zero4: 104,
		Zero5: 105,
		Zero6: 106,
		Zero7: 107,
		Zero8: 0.108,
		Zero9: 0.109,

		Subfield: &submessage{
			Answer: "Good!",
		},

		Submessages: []submessage{
			{Question: "Q1?", Answer: "A1"},
			{Question: "Q2?", Answer: "A2"},
			{Question: "Q3?", Answer: "A3"},
		},

		Mapping: map[string]int{
			"hello": 1,
			"world": 2,
		},
	}

	expected := &message{
		Field1: true,

		Field2: 2,
		Field3: 3,
		Field4: 4,

		Field5: 10,
		Field6: 11,
		Field7: 12,

		Field8: -21,
		Field9: -42,

		Field10: 0.25,
		Field11: 0.5,

		Field12: "Hello!",
		Field13: []byte("World!"),

		Subfield: &submessage{
			Question: "How are you?",
			Answer:   "Good!",
		},

		Submessages: []submessage{
			{Question: "Q1?", Answer: "A1"},
			{Question: "Q2?", Answer: "A2"},
			{Question: "Q3?", Answer: "Hello World!"},
		},

		Mapping: map[string]int{
			"answer": 42,
		},
	}

	rw, err := ParseRewriteTemplate(TypeOf(reflect.TypeOf(original)), []byte(`{
  "field_1": true,

  "field_2": 2,
  "field_3": 3,
  "field_4": 4,

  "field_5": 10,
  "field_6": 11,
  "field_7": 12,

  "field_8": -21,
  "field_9": -42,

  "field_10": 0.25,
  "field_11": 0.5,

  "field_12": "Hello!",
  "field_13": "World!",

  "zero_1": null,
  "zero_2": null,
  "zero_3": null,
  "zero_4": null,
  "zero_5": null,
  "zero_6": null,
  "zero_7": null,
  "zero_8": null,
  "zero_9": null,

  "subfield": {
    "question": "How are you?"
  },

  "submessages": [
    {
      "question": "Q1?",
      "answer": "A1"
    },
    {
      "question": "Q2?",
      "answer": "A2"
    },
    {
      "question": "Q3?",
      "answer": "Hello World!"
    }
  ],

  "mapping": {
    "answer": 42
  }
}`))
	if err != nil {
		t.Fatal(err)
	}

	b1, err := Marshal(original)
	if err != nil {
		t.Fatal(err)
	}

	b2, err := rw.Rewrite(nil, b1)
	if err != nil {
		t.Fatal(err)
	}

	found := &message{}
	if err := Unmarshal(b2, &found); err != nil {
		t.Fatal(err)
	}

	if !reflect.DeepEqual(expected, found) {
		t.Error("messages mismatch after rewrite")
		t.Logf("want:\n%+v", expected)
		t.Logf("got:\n%+v", found)
	}
}

func TestParseRewriteRules(t *testing.T) {
	type submessage struct {
		Flags uint64 `protobuf:"varint,1,opt,name=flags,proto3"`
	}

	type message struct {
		Flags    uint64      `protobuf:"varint,2,opt,name=flags,proto3"`
		Subfield *submessage `protobuf:"bytes,99,opt,name=subfield,proto3"`
	}

	original := &message{
		Flags: 0b00000001,
		Subfield: &submessage{
			Flags: 0b00000010,
		},
	}

	expected := &message{
		Flags: 0b00000001 | 16,
		Subfield: &submessage{
			Flags: 0b00000010 | 32,
		},
	}

	rules := RewriterRules{
		"flags": BitOr[uint64]{},
		"subfield": RewriterRules{
			"flags": BitOr[uint64]{},
		},
	}

	rw, err := ParseRewriteTemplate(TypeOf(reflect.TypeOf(original)), []byte(`{
  "flags": 16,
  "subfield": {
    "flags": 32
  }
}`), rules)
	if err != nil {
		t.Fatal(err)
	}

	b1, err := Marshal(original)
	if err != nil {
		t.Fatal(err)
	}

	b2, err := rw.Rewrite(nil, b1)
	if err != nil {
		t.Fatal(err)
	}

	found := &message{}
	if err := Unmarshal(b2, &found); err != nil {
		t.Fatal(err)
	}

	if !reflect.DeepEqual(expected, found) {
		t.Error("messages mismatch after rewrite")
		t.Logf("want:\n%+v", expected)
		t.Logf("got:\n%+v", found)
	}
}

func BenchmarkRewrite(b *testing.B) {
	type message struct {
		A int
		B float32
		C float64
		D string
	}

	in := message{A: 21, B: 0.125, D: "A"}
	rw := MessageRewriter{
		1: FieldNumber(1).Int(42),
		2: FieldNumber(2).Float32(-1),
		3: FieldNumber(3).Float64(+1),
		4: FieldNumber(4).String("Hello World!"),
	}

	p, err := Marshal(in)
	if err != nil {
		b.Fatal(err)
	}

	out := make([]byte, 0, 2*cap(p))

	for range b.N {
		out, err = rw.Rewrite(out[:0], p)
	}
}

func TestRewriteStructIdentity(t *testing.T) {
	type Node struct {
		Next               []Node   `protobuf:"bytes,1,rep,name=next,proto3" json:"next"`
		Name               string   `protobuf:"bytes,2,opt,name=name,proto3" json:"name"`
		Type               string   `protobuf:"bytes,3,opt,name=type,proto3" json:"type"`
		On                 uint32   `protobuf:"varint,4,opt,name=on,proto3,enum=op.Status" json:"on,omitempty"`
		Key                string   `protobuf:"bytes,5,opt,name=key,proto3" json:"key,omitempty"`
		Seed               uint64   `protobuf:"fixed64,6,opt,name=seed,proto3" json:"seed,omitempty"`
		ScheduleAfter      uint32   `protobuf:"varint,7,opt,name=schedule_after,json=scheduleAfter,proto3" json:"schedule_after,omitempty"`
		ExpireAfter        uint32   `protobuf:"varint,8,opt,name=expire_after,json=expireAfter,proto3" json:"expire_after,omitempty"`
		BackoffCoefficient uint32   `protobuf:"varint,9,opt,name=backoff_coefficient,json=backoffCoefficient,proto3" json:"backoff_coefficient,omitempty"`
		BackoffMinDelay    uint32   `protobuf:"varint,10,opt,name=backoff_min_delay,json=backoffMinDelay,proto3" json:"backoff_min_delay,omitempty"`
		BackoffMaxDelay    uint32   `protobuf:"varint,11,opt,name=backoff_max_delay,json=backoffMaxDelay,proto3" json:"backoff_max_delay,omitempty"`
		ExecutionTimeout   uint32   `protobuf:"varint,12,opt,name=execution_timeout,json=executionTimeout,proto3" json:"execution_timeout,omitempty"`
		NextLength         uint64   `protobuf:"varint,13,opt,name=next_length,json=nextLength,proto3" json:"next_length,omitempty"`
		BatchMaxBytes      uint32   `protobuf:"varint,14,opt,name=batch_max_bytes,json=batchMaxBytes,proto3" json:"batch_max_bytes,omitempty"`
		BatchMaxCount      uint32   `protobuf:"varint,15,opt,name=batch_max_count,json=batchMaxCount,proto3" json:"batch_max_count,omitempty"`
		BatchTimeout       uint32   `protobuf:"varint,16,opt,name=batch_timeout,json=batchTimeout,proto3" json:"batch_timeout,omitempty"`
		BatchKey           [16]byte `protobuf:"bytes,17,opt,name=batch_key,json=batchKey,proto3,customtype=U128" json:"batch_key"`
	}

	type Header struct {
		Flows         string `protobuf:"bytes,1,opt,name=flows,proto3" json:"flows,omitempty"`
		Root          Node   `protobuf:"bytes,2,opt,name=root,proto3" json:"root"`
		TraceContext  []byte `protobuf:"bytes,6,opt,name=trace_context,json=traceContext,proto3" json:"trace_context"`
		ContentLength int64  `protobuf:"varint,7,opt,name=content_length,json=contentLength,proto3" json:"content_length,omitempty"`
		ContentType   string `protobuf:"bytes,8,opt,name=content_type,json=contentType,proto3" json:"content_type"`
	}

	b := []byte{
		0xa, 0xd, 0x66, 0x6c, 0x6f, 0x77, 0x2d, 0x42, 0x3a, 0x66, 0x6c, 0x6f, 0x77, 0x2d, 0x30, 0x12,
		0x7a, 0xa, 0x30, 0x12, 0xc, 0x74, 0x65, 0x73, 0x74, 0x5f, 0x64, 0x69, 0x73, 0x63, 0x61, 0x72,
		0x64, 0x1a, 0x0, 0x20, 0x2, 0x31, 0x69, 0xf2, 0xc9, 0xd0, 0xc1, 0x2f, 0xe0, 0x80, 0x68, 0x65,
		0x8a, 0x1, 0x10, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0,
		0x0, 0x0, 0x0, 0x12, 0x4, 0x74, 0x65, 0x73, 0x74, 0x1a, 0x4, 0x68, 0x74, 0x74, 0x70, 0x31,
		0xa, 0x7f, 0xf5, 0xf8, 0x13, 0x1d, 0xfb, 0x17, 0x38, 0xc1, 0xd, 0x40, 0xff, 0xdb, 0x1, 0x48,
		0xc6, 0xf, 0x50, 0xbd, 0x1b, 0x58, 0x9a, 0xbe, 0x2, 0x60, 0x88, 0x27, 0x68, 0x5d, 0x70, 0x80,
		0x80, 0x4, 0x78, 0xa, 0x80, 0x1, 0xd0, 0xf, 0x8a, 0x1, 0x10, 0x0, 0x0, 0x0, 0x0, 0x0,
		0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x32, 0x1c, 0xa, 0x10, 0x2a, 0x43,
		0x4c, 0xf3, 0x8c, 0x67, 0x48, 0x8f, 0xe, 0xca, 0xe8, 0x28, 0x96, 0x6c, 0x2b, 0xe4, 0x12,
		0x8, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x38, 0x91, 0x66, 0x42, 0x18, 0x61, 0x70,
		0x70, 0x6c, 0x69, 0x63, 0x61, 0x74, 0x69, 0x6f, 0x6e, 0x2f, 0x6f, 0x63, 0x74, 0x65, 0x74, 0x2d,
		0x73, 0x74, 0x72, 0x65, 0x61, 0x6d,
	}

	m := Header{}
	if err := Unmarshal(b, &m); err != nil {
		t.Fatal(err)
	}

	r, err := ParseRewriteTemplate(TypeOf(reflect.TypeOf(m)), []byte(`{"root":{}}`))
	if err != nil {
		t.Fatal(err)
	}

	c, err := r.Rewrite(nil, b)
	if err != nil {
		t.Fatal(err)
	}

	x := Header{}
	if err := Unmarshal(c, &x); err != nil {
		t.Fatal(err)
	}

	if !reflect.DeepEqual(m, x) {
		t.Errorf("messages mismatch")
		t.Logf("want: %+v", m)
		t.Logf("got:  %+v", x)
	}
}
```

## File: `proto/size.go`
```go
package proto

import (
	"math/bits"
	"unsafe"
)

type sizeFunc = func(unsafe.Pointer, flags) int

func sizeOfVarint(v uint64) int {
	return (bits.Len64(v|1) + 6) / 7
}

func sizeOfVarintZigZag(v int64) int {
	return sizeOfVarint((uint64(v) << 1) ^ uint64(v>>63))
}

func sizeOfVarlen(n int) int {
	return sizeOfVarint(uint64(n)) + n
}

func sizeOfTag(f fieldNumber, t wireType) int {
	return sizeOfVarint(uint64(f)<<3 | uint64(t))
}
```

## File: `proto/slice.go`
```go
package proto

import (
	"io"
	"reflect"
	"unsafe"

	. "github.com/segmentio/encoding/internal/runtime_reflect"
)

type repeatedField struct {
	codec       *codec
	fieldNumber fieldNumber
	wireType    wireType
	embedded    bool
}

func sliceCodecOf(t reflect.Type, f structField, seen map[reflect.Type]*codec) *codec {
	s := new(codec)
	seen[t] = s

	r := &repeatedField{
		codec:       f.codec,
		fieldNumber: f.fieldNumber(),
		wireType:    f.wireType(),
		embedded:    f.embedded(),
	}

	s.wire = f.codec.wire
	s.size = sliceSizeFuncOf(t, r)
	s.encode = sliceEncodeFuncOf(t, r)
	s.decode = sliceDecodeFuncOf(t, r)
	return s
}

func sliceSizeFuncOf(t reflect.Type, r *repeatedField) sizeFunc {
	elemSize := alignedSize(t.Elem())
	tagSize := sizeOfTag(r.fieldNumber, r.wireType)
	return func(p unsafe.Pointer, _ flags) int {
		n := 0

		if v := (*Slice)(p); v != nil {
			for i := range v.Len() {
				elem := v.Index(i, elemSize)
				size := r.codec.size(elem, wantzero)
				n += tagSize + size
				if r.embedded {
					n += sizeOfVarint(uint64(size))
				}
			}
		}

		return n
	}
}

func sliceEncodeFuncOf(t reflect.Type, r *repeatedField) encodeFunc {
	elemSize := alignedSize(t.Elem())
	tagSize := sizeOfTag(r.fieldNumber, r.wireType)
	tagData := make([]byte, tagSize)
	encodeTag(tagData, r.fieldNumber, r.wireType)
	return func(b []byte, p unsafe.Pointer, _ flags) (int, error) {
		offset := 0

		if s := (*Slice)(p); s != nil {
			for i := range s.Len() {
				elem := s.Index(i, elemSize)
				size := r.codec.size(elem, wantzero)

				n := copy(b[offset:], tagData)
				offset += n
				if n < len(tagData) {
					return offset, io.ErrShortBuffer
				}

				if r.embedded {
					n, err := encodeVarint(b[offset:], uint64(size))
					offset += n
					if err != nil {
						return offset, err
					}
				}

				if (len(b) - offset) < size {
					return len(b), io.ErrShortBuffer
				}

				n, err := r.codec.encode(b[offset:offset+size], elem, wantzero)
				offset += n
				if err != nil {
					return offset, err
				}
			}
		}

		return offset, nil
	}
}

func sliceDecodeFuncOf(t reflect.Type, r *repeatedField) decodeFunc {
	elemType := t.Elem()
	elemSize := alignedSize(elemType)
	return func(b []byte, p unsafe.Pointer, _ flags) (int, error) {
		s := (*Slice)(p)
		i := s.Len()

		if i == s.Cap() {
			*s = growSlice(elemType, s)
		}

		n, err := r.codec.decode(b, s.Index(i, elemSize), noflags)
		if err == nil {
			s.SetLen(i + 1)
		}
		return n, err
	}
}

func alignedSize(t reflect.Type) uintptr {
	a := t.Align()
	s := t.Size()
	return align(uintptr(a), uintptr(s))
}

func align(align, size uintptr) uintptr {
	if align != 0 && (size%align) != 0 {
		size = ((size / align) + 1) * align
	}
	return size
}

func growSlice(t reflect.Type, s *Slice) Slice {
	cap := 2 * s.Cap()
	if cap == 0 {
		cap = 10
	}
	p := pointer(t)
	d := MakeSlice(p, s.Len(), cap)
	CopySlice(p, d, *s)
	return d
}
```

## File: `proto/string.go`
```go
package proto

import (
	"io"
	"unsafe"
)

var stringCodec = codec{
	wire:   varlen,
	size:   sizeOfString,
	encode: encodeString,
	decode: decodeString,
}

func sizeOfString(p unsafe.Pointer, flags flags) int {
	if p != nil {
		if v := *(*string)(p); v != "" || flags.has(wantzero) {
			return sizeOfVarlen(len(v))
		}
	}
	return 0
}

func encodeString(b []byte, p unsafe.Pointer, flags flags) (int, error) {
	if p != nil {
		if v := *(*string)(p); v != "" || flags.has(wantzero) {
			n, err := encodeVarint(b, uint64(len(v)))
			if err != nil {
				return n, err
			}
			c := copy(b[n:], v)
			n += c
			if c < len(v) {
				err = io.ErrShortBuffer
			}
			return n, err
		}
	}
	return 0, nil
}

func decodeString(b []byte, p unsafe.Pointer, _ flags) (int, error) {
	v, n, err := decodeVarlen(b)
	*(*string)(p) = string(v)
	return n, err
}
```

## File: `proto/struct.go`
```go
package proto

import (
	"fmt"
	"io"
	"reflect"
	"unsafe"
)

const (
	embedded = 1 << 0
	repeated = 1 << 1
	zigzag   = 1 << 2
)

type structField struct {
	number  uint16
	tagsize uint8
	flags   uint8
	offset  uint32
	codec   *codec
}

func (f *structField) String() string {
	return fmt.Sprintf("[%d,%s]", f.fieldNumber(), f.wireType())
}

func (f *structField) fieldNumber() fieldNumber {
	return fieldNumber(f.number)
}

func (f *structField) wireType() wireType {
	return f.codec.wire
}

func (f *structField) embedded() bool {
	return (f.flags & embedded) != 0
}

func (f *structField) repeated() bool {
	return (f.flags & repeated) != 0
}

func (f *structField) pointer(p unsafe.Pointer) unsafe.Pointer {
	return unsafe.Pointer(uintptr(p) + uintptr(f.offset))
}

func (f *structField) makeFlags(base flags) flags {
	return base | flags(f.flags&zigzag)
}

func structCodecOf(t reflect.Type, seen map[reflect.Type]*codec) *codec {
	c := &codec{wire: varlen}
	seen[t] = c

	numField := t.NumField()
	number := fieldNumber(1)
	fields := make([]structField, 0, numField)

	for i := range numField {
		f := t.Field(i)

		if f.PkgPath != "" {
			continue // unexported
		}

		field := structField{
			number: uint16(number),
			offset: uint32(f.Offset),
		}

		if tag, ok := f.Tag.Lookup("protobuf"); ok {
			t, err := parseStructTag(tag)
			if err == nil {
				field.number = uint16(t.fieldNumber)
				if t.repeated {
					field.flags |= repeated
				}
				if t.zigzag {
					field.flags |= zigzag
				}
				switch t.wireType {
				case Fixed32:
					switch baseKindOf(f.Type) {
					case reflect.Uint32:
						field.codec = &fixed32Codec
					case reflect.Float32:
						field.codec = &float32Codec
					}
				case Fixed64:
					switch baseKindOf(f.Type) {
					case reflect.Uint64:
						field.codec = &fixed64Codec
					case reflect.Float64:
						field.codec = &float64Codec
					}
				}
			}
		}

		if field.codec == nil {
			switch baseKindOf(f.Type) {
			case reflect.Struct:
				field.flags |= embedded
				field.codec = codecOf(f.Type, seen)

			case reflect.Slice:
				elem := f.Type.Elem()

				if elem.Kind() == reflect.Uint8 { // []byte
					field.codec = codecOf(f.Type, seen)
				} else {
					if baseKindOf(elem) == reflect.Struct {
						field.flags |= embedded
					}
					field.flags |= repeated
					field.codec = codecOf(elem, seen)
					field.codec = sliceCodecOf(f.Type, field, seen)
				}

			case reflect.Map:
				key, val := f.Type.Key(), f.Type.Elem()
				k := codecOf(key, seen)
				v := codecOf(val, seen)
				m := &mapField{
					number:   field.number,
					keyCodec: k,
					valCodec: v,
				}
				if baseKindOf(key) == reflect.Struct {
					m.keyFlags |= embedded
				}
				if baseKindOf(val) == reflect.Struct {
					m.valFlags |= embedded
				}
				field.flags |= embedded | repeated
				field.codec = mapCodecOf(f.Type, m, seen)

			default:
				field.codec = codecOf(f.Type, seen)
			}
		}

		field.tagsize = uint8(sizeOfTag(fieldNumber(field.number), wireType(field.codec.wire)))
		fields = append(fields, field)
		number++
	}

	c.size = structSizeFuncOf(t, fields)
	c.encode = structEncodeFuncOf(t, fields)
	c.decode = structDecodeFuncOf(t, fields)
	return c
}

func baseKindOf(t reflect.Type) reflect.Kind {
	return baseTypeOf(t).Kind()
}

func baseTypeOf(t reflect.Type) reflect.Type {
	for t.Kind() == reflect.Ptr {
		t = t.Elem()
	}
	return t
}

func structSizeFuncOf(t reflect.Type, fields []structField) sizeFunc {
	inlined := inlined(t)
	var unique, repeated []*structField

	for i := range fields {
		f := &fields[i]
		if f.repeated() {
			repeated = append(repeated, f)
		} else {
			unique = append(unique, f)
		}
	}

	return func(p unsafe.Pointer, flags flags) int {
		if p == nil {
			return 0
		}

		if !inlined {
			flags = flags.without(inline | toplevel)
		} else {
			flags = flags.without(toplevel)
		}
		n := 0

		for _, f := range unique {
			size := f.codec.size(f.pointer(p), f.makeFlags(flags))
			if size > 0 {
				n += int(f.tagsize) + size
				if f.embedded() {
					n += sizeOfVarint(uint64(size))
				}
				flags = flags.without(wantzero)
			}
		}

		for _, f := range repeated {
			size := f.codec.size(f.pointer(p), f.makeFlags(flags))
			if size > 0 {
				n += size
				flags = flags.without(wantzero)
			}
		}

		return n
	}
}

func structEncodeFuncOf(t reflect.Type, fields []structField) encodeFunc {
	inlined := inlined(t)
	var unique, repeated []*structField

	for i := range fields {
		f := &fields[i]
		if f.repeated() {
			repeated = append(repeated, f)
		} else {
			unique = append(unique, f)
		}
	}

	return func(b []byte, p unsafe.Pointer, flags flags) (int, error) {
		if p == nil {
			return 0, nil
		}

		if !inlined {
			flags = flags.without(inline | toplevel)
		} else {
			flags = flags.without(toplevel)
		}
		offset := 0

		for _, f := range unique {
			fieldFlags := f.makeFlags(flags)
			elem := f.pointer(p)
			size := f.codec.size(elem, fieldFlags)

			if size > 0 {
				n, err := encodeTag(b[offset:], f.fieldNumber(), f.wireType())
				offset += n
				if err != nil {
					return offset, err
				}

				if f.embedded() {
					n, err := encodeVarint(b[offset:], uint64(size))
					offset += n
					if err != nil {
						return offset, err
					}
				}

				if (len(b) - offset) < size {
					return len(b), io.ErrShortBuffer
				}

				n, err = f.codec.encode(b[offset:offset+size], elem, fieldFlags)
				offset += n
				if err != nil {
					return offset, err
				}

				flags = flags.without(wantzero)
			}
		}

		for _, f := range repeated {
			n, err := f.codec.encode(b[offset:], f.pointer(p), f.makeFlags(flags))
			offset += n
			if err != nil {
				return offset, err
			}
			if n > 0 {
				flags = flags.without(wantzero)
			}
		}

		return offset, nil
	}
}

func structDecodeFuncOf(t reflect.Type, fields []structField) decodeFunc {
	maxFieldNumber := fieldNumber(0)

	for _, f := range fields {
		if n := f.fieldNumber(); n > maxFieldNumber {
			maxFieldNumber = n
		}
	}

	fieldIndex := make([]*structField, maxFieldNumber+1)

	for i := range fields {
		f := &fields[i]
		fieldIndex[f.fieldNumber()] = f
	}

	return func(b []byte, p unsafe.Pointer, flags flags) (int, error) {
		flags = flags.without(toplevel)
		offset := 0

		for offset < len(b) {
			fieldNumber, wireType, n, err := decodeTag(b[offset:])
			offset += n
			if err != nil {
				return offset, err
			}

			i := int(fieldNumber)
			f := (*structField)(nil)

			if i >= 0 && i < len(fieldIndex) {
				f = fieldIndex[i]
			}

			if f == nil {
				skip := 0
				size := uint64(0)
				switch wireType {
				case varint:
					_, skip, err = decodeVarint(b[offset:])
				case varlen:
					size, skip, err = decodeVarint(b[offset:])
					if err == nil {
						if size > uint64(len(b)-skip) {
							err = io.ErrUnexpectedEOF
						} else {
							skip += int(size)
						}
					}
				case fixed32:
					_, skip, err = decodeLE32(b[offset:])
				case fixed64:
					_, skip, err = decodeLE64(b[offset:])
				default:
					err = ErrWireTypeUnknown
				}
				if (offset + skip) <= len(b) {
					offset += skip
				} else {
					offset, err = len(b), io.ErrUnexpectedEOF
				}
				if err != nil {
					return offset, fieldError(fieldNumber, wireType, err)
				}
				continue
			}

			if wireType != f.wireType() {
				return offset, fieldError(fieldNumber, wireType, fmt.Errorf("expected wire type %d", f.wireType()))
			}

			// `data` will only contain the section of the input buffer where
			// the data for the next field is available. This is necessary to
			// limit how many bytes will be consumed by embedded messages.
			var data []byte
			switch wireType {
			case varint:
				_, n, err := decodeVarint(b[offset:])
				if err != nil {
					return offset, fieldError(fieldNumber, wireType, err)
				}
				data = b[offset : offset+n]

			case varlen:
				l, n, err := decodeVarint(b[offset:])
				if err != nil {
					return offset + n, fieldError(fieldNumber, wireType, err)
				}
				if l > uint64(len(b)-(offset+n)) {
					return len(b), fieldError(fieldNumber, wireType, io.ErrUnexpectedEOF)
				}
				if f.embedded() {
					offset += n
					data = b[offset : offset+int(l)]
				} else {
					data = b[offset : offset+n+int(l)]
				}

			case fixed32:
				if (offset + 4) > len(b) {
					return len(b), fieldError(fieldNumber, wireType, io.ErrUnexpectedEOF)
				}
				data = b[offset : offset+4]

			case fixed64:
				if (offset + 8) > len(b) {
					return len(b), fieldError(fieldNumber, wireType, io.ErrUnexpectedEOF)
				}
				data = b[offset : offset+8]

			default:
				return offset, fieldError(fieldNumber, wireType, ErrWireTypeUnknown)
			}

			n, err = f.codec.decode(data, f.pointer(p), f.makeFlags(flags))
			offset += n
			if err != nil {
				return offset, fieldError(fieldNumber, wireType, err)
			}
		}

		return offset, nil
	}
}
```

## File: `proto/struct_test.go`
```go
package proto

import (
	"testing"
	"unsafe"
)

func TestStructFieldSize(t *testing.T) {
	t.Log("sizeof(structField) =", unsafe.Sizeof(structField{}))
}
```

## File: `proto/uint.go`
```go
package proto

import "unsafe"

var uintCodec = codec{
	wire:   varint,
	size:   sizeOfUint,
	encode: encodeUint,
	decode: decodeUint,
}

func sizeOfUint(p unsafe.Pointer, flags flags) int {
	if p != nil {
		if v := *(*uint)(p); v != 0 || flags.has(wantzero) {
			return sizeOfVarint(uint64(v))
		}
	}
	return 0
}

func encodeUint(b []byte, p unsafe.Pointer, flags flags) (int, error) {
	if p != nil {
		if v := *(*uint)(p); v != 0 || flags.has(wantzero) {
			return encodeVarint(b, uint64(v))
		}
	}
	return 0, nil
}

func decodeUint(b []byte, p unsafe.Pointer, _ flags) (int, error) {
	v, n, err := decodeVarint(b)
	*(*uint)(p) = uint(v)
	return n, err
}
```

## File: `proto/uint32.go`
```go
package proto

import (
	"fmt"
	"math"
	"unsafe"
)

var uint32Codec = codec{
	wire:   varint,
	size:   sizeOfUint32,
	encode: encodeUint32,
	decode: decodeUint32,
}

func sizeOfUint32(p unsafe.Pointer, flags flags) int {
	if p != nil {
		if v := *(*uint32)(p); v != 0 || flags.has(wantzero) {
			return sizeOfVarint(uint64(v))
		}
	}
	return 0
}

func encodeUint32(b []byte, p unsafe.Pointer, flags flags) (int, error) {
	if p != nil {
		if v := *(*uint32)(p); v != 0 || flags.has(wantzero) {
			return encodeVarint(b, uint64(v))
		}
	}
	return 0, nil
}

func decodeUint32(b []byte, p unsafe.Pointer, _ flags) (int, error) {
	v, n, err := decodeVarint(b)
	if v > math.MaxUint32 {
		return n, fmt.Errorf("integer overflow decoding %v into uint32", v)
	}
	*(*uint32)(p) = uint32(v)
	return n, err
}

var fixed32Codec = codec{
	wire:   fixed32,
	size:   sizeOfFixed32,
	encode: encodeFixed32,
	decode: decodeFixed32,
}

func sizeOfFixed32(p unsafe.Pointer, flags flags) int {
	if p != nil {
		if v := *(*uint32)(p); v != 0 || flags.has(wantzero) {
			return 4
		}
	}
	return 0
}

func encodeFixed32(b []byte, p unsafe.Pointer, flags flags) (int, error) {
	if p != nil {
		if v := *(*uint32)(p); v != 0 || flags.has(wantzero) {
			return encodeLE32(b, v)
		}
	}
	return 0, nil
}

func decodeFixed32(b []byte, p unsafe.Pointer, _ flags) (int, error) {
	v, n, err := decodeLE32(b)
	*(*uint32)(p) = v
	return n, err
}
```

## File: `proto/uint64.go`
```go
package proto

import "unsafe"

var uint64Codec = codec{
	wire:   varint,
	size:   sizeOfUint64,
	encode: encodeUint64,
	decode: decodeUint64,
}

func sizeOfUint64(p unsafe.Pointer, flags flags) int {
	if p != nil {
		if v := *(*uint64)(p); v != 0 || flags.has(wantzero) {
			return sizeOfVarint(v)
		}
	}
	return 0
}

func encodeUint64(b []byte, p unsafe.Pointer, flags flags) (int, error) {
	if p != nil {
		if v := *(*uint64)(p); v != 0 || flags.has(wantzero) {
			return encodeVarint(b, v)
		}
	}
	return 0, nil
}

func decodeUint64(b []byte, p unsafe.Pointer, _ flags) (int, error) {
	v, n, err := decodeVarint(b)
	*(*uint64)(p) = uint64(v)
	return n, err
}

var fixed64Codec = codec{
	wire:   fixed64,
	size:   sizeOfFixed64,
	encode: encodeFixed64,
	decode: decodeFixed64,
}

func sizeOfFixed64(p unsafe.Pointer, flags flags) int {
	if p != nil {
		if v := *(*uint64)(p); v != 0 || flags.has(wantzero) {
			return 8
		}
	}
	return 0
}

func encodeFixed64(b []byte, p unsafe.Pointer, flags flags) (int, error) {
	if p != nil {
		if v := *(*uint64)(p); v != 0 || flags.has(wantzero) {
			return encodeLE64(b, v)
		}
	}
	return 0, nil
}

func decodeFixed64(b []byte, p unsafe.Pointer, _ flags) (int, error) {
	v, n, err := decodeLE64(b)
	*(*uint64)(p) = v
	return n, err
}
```

## File: `proto/fixtures/Makefile`
```
%.pb.go: %.proto
	protoc -I=$(dir $@) --go_out=$(dir $@) $<
	@mv $(dir $@)/github.com/segmentio/encoding/proto/fixtures/$@ $@
	@rm -rf $(dir $@)/github.com

protobuf.sources := \
    $(wildcard ./*.proto)

generate: protobuf
	go run ./generate

clean:
	rm -f *.pb.go

protobuf: $(protobuf.sources:.proto=.pb.go)
```

## File: `proto/fixtures/fixtures.pb.go`
```go
// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.23.0
// 	protoc        v3.11.4
// source: fixtures.proto

package fixtures

import (
	proto "github.com/golang/protobuf/proto"
	protoreflect "google.golang.org/protobuf/reflect/protoreflect"
	protoimpl "google.golang.org/protobuf/runtime/protoimpl"
	reflect "reflect"
	sync "sync"
)

const (
	// Verify that this generated code is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(20 - protoimpl.MinVersion)
	// Verify that runtime/protoimpl is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(protoimpl.MaxVersion - 20)
)

// This is a compile-time assertion that a sufficiently up-to-date version
// of the legacy proto package is being used.
const _ = proto.ProtoPackageIsVersion4

type Message struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	A             int64   `protobuf:"varint,1,opt,name=a,proto3" json:"a,omitempty"`
	B             uint32  `protobuf:"varint,2,opt,name=b,proto3" json:"b,omitempty"`
	C             uint64  `protobuf:"varint,3,opt,name=c,proto3" json:"c,omitempty"`
	D             string  `protobuf:"bytes,4,opt,name=d,proto3" json:"d,omitempty"`
	Signed_1      int32   `protobuf:"zigzag32,10,opt,name=signed_1,json=signed1,proto3" json:"signed_1,omitempty"`
	Signed_2      int64   `protobuf:"zigzag64,11,opt,name=signed_2,json=signed2,proto3" json:"signed_2,omitempty"`
	Fixed_1       uint32  `protobuf:"fixed32,20,opt,name=fixed_1,json=fixed1,proto3" json:"fixed_1,omitempty"`
	Fixed_2       uint64  `protobuf:"fixed64,21,opt,name=fixed_2,json=fixed2,proto3" json:"fixed_2,omitempty"`
	SignedFixed_1 int32   `protobuf:"fixed32,30,opt,name=signed_fixed_1,json=signedFixed1,proto3" json:"signed_fixed_1,omitempty"`
	SignedFixed_2 int64   `protobuf:"fixed64,31,opt,name=signed_fixed_2,json=signedFixed2,proto3" json:"signed_fixed_2,omitempty"`
	Float32       float32 `protobuf:"fixed32,40,opt,name=float32,proto3" json:"float32,omitempty"`
	Float64       float64 `protobuf:"fixed64,41,opt,name=float64,proto3" json:"float64,omitempty"`
}

func (x *Message) Reset() {
	*x = Message{}
	if protoimpl.UnsafeEnabled {
		mi := &file_fixtures_proto_msgTypes[0]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *Message) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*Message) ProtoMessage() {}

func (x *Message) ProtoReflect() protoreflect.Message {
	mi := &file_fixtures_proto_msgTypes[0]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use Message.ProtoReflect.Descriptor instead.
func (*Message) Descriptor() ([]byte, []int) {
	return file_fixtures_proto_rawDescGZIP(), []int{0}
}

func (x *Message) GetA() int64 {
	if x != nil {
		return x.A
	}
	return 0
}

func (x *Message) GetB() uint32 {
	if x != nil {
		return x.B
	}
	return 0
}

func (x *Message) GetC() uint64 {
	if x != nil {
		return x.C
	}
	return 0
}

func (x *Message) GetD() string {
	if x != nil {
		return x.D
	}
	return ""
}

func (x *Message) GetSigned_1() int32 {
	if x != nil {
		return x.Signed_1
	}
	return 0
}

func (x *Message) GetSigned_2() int64 {
	if x != nil {
		return x.Signed_2
	}
	return 0
}

func (x *Message) GetFixed_1() uint32 {
	if x != nil {
		return x.Fixed_1
	}
	return 0
}

func (x *Message) GetFixed_2() uint64 {
	if x != nil {
		return x.Fixed_2
	}
	return 0
}

func (x *Message) GetSignedFixed_1() int32 {
	if x != nil {
		return x.SignedFixed_1
	}
	return 0
}

func (x *Message) GetSignedFixed_2() int64 {
	if x != nil {
		return x.SignedFixed_2
	}
	return 0
}

func (x *Message) GetFloat32() float32 {
	if x != nil {
		return x.Float32
	}
	return 0
}

func (x *Message) GetFloat64() float64 {
	if x != nil {
		return x.Float64
	}
	return 0
}

var File_fixtures_proto protoreflect.FileDescriptor

var file_fixtures_proto_rawDesc = []byte{
	0x0a, 0x0e, 0x66, 0x69, 0x78, 0x74, 0x75, 0x72, 0x65, 0x73, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f,
	0x12, 0x08, 0x66, 0x69, 0x78, 0x74, 0x75, 0x72, 0x65, 0x73, 0x22, 0xa9, 0x02, 0x0a, 0x07, 0x4d,
	0x65, 0x73, 0x73, 0x61, 0x67, 0x65, 0x12, 0x0c, 0x0a, 0x01, 0x61, 0x18, 0x01, 0x20, 0x01, 0x28,
	0x03, 0x52, 0x01, 0x61, 0x12, 0x0c, 0x0a, 0x01, 0x62, 0x18, 0x02, 0x20, 0x01, 0x28, 0x0d, 0x52,
	0x01, 0x62, 0x12, 0x0c, 0x0a, 0x01, 0x63, 0x18, 0x03, 0x20, 0x01, 0x28, 0x04, 0x52, 0x01, 0x63,
	0x12, 0x0c, 0x0a, 0x01, 0x64, 0x18, 0x04, 0x20, 0x01, 0x28, 0x09, 0x52, 0x01, 0x64, 0x12, 0x19,
	0x0a, 0x08, 0x73, 0x69, 0x67, 0x6e, 0x65, 0x64, 0x5f, 0x31, 0x18, 0x0a, 0x20, 0x01, 0x28, 0x11,
	0x52, 0x07, 0x73, 0x69, 0x67, 0x6e, 0x65, 0x64, 0x31, 0x12, 0x19, 0x0a, 0x08, 0x73, 0x69, 0x67,
	0x6e, 0x65, 0x64, 0x5f, 0x32, 0x18, 0x0b, 0x20, 0x01, 0x28, 0x12, 0x52, 0x07, 0x73, 0x69, 0x67,
	0x6e, 0x65, 0x64, 0x32, 0x12, 0x17, 0x0a, 0x07, 0x66, 0x69, 0x78, 0x65, 0x64, 0x5f, 0x31, 0x18,
	0x14, 0x20, 0x01, 0x28, 0x07, 0x52, 0x06, 0x66, 0x69, 0x78, 0x65, 0x64, 0x31, 0x12, 0x17, 0x0a,
	0x07, 0x66, 0x69, 0x78, 0x65, 0x64, 0x5f, 0x32, 0x18, 0x15, 0x20, 0x01, 0x28, 0x06, 0x52, 0x06,
	0x66, 0x69, 0x78, 0x65, 0x64, 0x32, 0x12, 0x24, 0x0a, 0x0e, 0x73, 0x69, 0x67, 0x6e, 0x65, 0x64,
	0x5f, 0x66, 0x69, 0x78, 0x65, 0x64, 0x5f, 0x31, 0x18, 0x1e, 0x20, 0x01, 0x28, 0x0f, 0x52, 0x0c,
	0x73, 0x69, 0x67, 0x6e, 0x65, 0x64, 0x46, 0x69, 0x78, 0x65, 0x64, 0x31, 0x12, 0x24, 0x0a, 0x0e,
	0x73, 0x69, 0x67, 0x6e, 0x65, 0x64, 0x5f, 0x66, 0x69, 0x78, 0x65, 0x64, 0x5f, 0x32, 0x18, 0x1f,
	0x20, 0x01, 0x28, 0x10, 0x52, 0x0c, 0x73, 0x69, 0x67, 0x6e, 0x65, 0x64, 0x46, 0x69, 0x78, 0x65,
	0x64, 0x32, 0x12, 0x18, 0x0a, 0x07, 0x66, 0x6c, 0x6f, 0x61, 0x74, 0x33, 0x32, 0x18, 0x28, 0x20,
	0x01, 0x28, 0x02, 0x52, 0x07, 0x66, 0x6c, 0x6f, 0x61, 0x74, 0x33, 0x32, 0x12, 0x18, 0x0a, 0x07,
	0x66, 0x6c, 0x6f, 0x61, 0x74, 0x36, 0x34, 0x18, 0x29, 0x20, 0x01, 0x28, 0x01, 0x52, 0x07, 0x66,
	0x6c, 0x6f, 0x61, 0x74, 0x36, 0x34, 0x42, 0x2e, 0x5a, 0x2c, 0x67, 0x69, 0x74, 0x68, 0x75, 0x62,
	0x2e, 0x63, 0x6f, 0x6d, 0x2f, 0x73, 0x65, 0x67, 0x6d, 0x65, 0x6e, 0x74, 0x69, 0x6f, 0x2f, 0x65,
	0x6e, 0x63, 0x6f, 0x64, 0x69, 0x6e, 0x67, 0x2f, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x2f, 0x66, 0x69,
	0x78, 0x74, 0x75, 0x72, 0x65, 0x73, 0x62, 0x06, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x33,
}

var (
	file_fixtures_proto_rawDescOnce sync.Once
	file_fixtures_proto_rawDescData = file_fixtures_proto_rawDesc
)

func file_fixtures_proto_rawDescGZIP() []byte {
	file_fixtures_proto_rawDescOnce.Do(func() {
		file_fixtures_proto_rawDescData = protoimpl.X.CompressGZIP(file_fixtures_proto_rawDescData)
	})
	return file_fixtures_proto_rawDescData
}

var file_fixtures_proto_msgTypes = make([]protoimpl.MessageInfo, 1)
var file_fixtures_proto_goTypes = []any{
	(*Message)(nil), // 0: fixtures.Message
}
var file_fixtures_proto_depIdxs = []int32{
	0, // [0:0] is the sub-list for method output_type
	0, // [0:0] is the sub-list for method input_type
	0, // [0:0] is the sub-list for extension type_name
	0, // [0:0] is the sub-list for extension extendee
	0, // [0:0] is the sub-list for field type_name
}

func init() { file_fixtures_proto_init() }
func file_fixtures_proto_init() {
	if File_fixtures_proto != nil {
		return
	}
	if !protoimpl.UnsafeEnabled {
		file_fixtures_proto_msgTypes[0].Exporter = func(v any, i int) any {
			switch v := v.(*Message); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
	}
	type x struct{}
	out := protoimpl.TypeBuilder{
		File: protoimpl.DescBuilder{
			GoPackagePath: reflect.TypeOf(x{}).PkgPath(),
			RawDescriptor: file_fixtures_proto_rawDesc,
			NumEnums:      0,
			NumMessages:   1,
			NumExtensions: 0,
			NumServices:   0,
		},
		GoTypes:           file_fixtures_proto_goTypes,
		DependencyIndexes: file_fixtures_proto_depIdxs,
		MessageInfos:      file_fixtures_proto_msgTypes,
	}.Build()
	File_fixtures_proto = out.File
	file_fixtures_proto_rawDesc = nil
	file_fixtures_proto_goTypes = nil
	file_fixtures_proto_depIdxs = nil
}
```

## File: `proto/fixtures/fixtures.proto`
```
syntax = "proto3";

package fixtures;

option go_package = "github.com/segmentio/encoding/proto/fixtures";

message Message {
  int64 a = 1;
  uint32 b = 2;
  uint64 c = 3;
  string d = 4;

  sint32 signed_1 = 10;
  sint64 signed_2 = 11;

  fixed32 fixed_1 = 20;
  fixed64 fixed_2 = 21;

  sfixed32 signed_fixed_1 = 30;
  sfixed64 signed_fixed_2 = 31;

  float float32 = 40;
  double float64 = 41;
}
```

## File: `proto/fixtures/go.mod`
```
module github.com/segmentio/encoding/proto/fixtures

go 1.14

require (
	github.com/golang/protobuf v1.4.2
	google.golang.org/protobuf v1.25.0
)
```

## File: `proto/fixtures/go.sum`
```
cloud.google.com/go v0.26.0/go.mod h1:aQUYkXzVsufM+DwF1aE+0xfcU+56JwCaLick0ClmMTw=
github.com/BurntSushi/toml v0.3.1/go.mod h1:xHWCNGjB5oqiDr8zfno3MHue2Ht5sIBksp03qcyfWMU=
github.com/census-instrumentation/opencensus-proto v0.2.1/go.mod h1:f6KPmirojxKA12rnyqOA5BBL4O983OfeGPqjHWSTneU=
github.com/client9/misspell v0.3.4/go.mod h1:qj6jICC3Q7zFZvVWo7KLAzC3yx5G7kyvSDkc90ppPyw=
github.com/envoyproxy/go-control-plane v0.9.1-0.20191026205805-5f8ba28d4473/go.mod h1:YTl/9mNaCwkRvm6d1a2C3ymFceY/DCBVvsKhRF0iEA4=
github.com/envoyproxy/protoc-gen-validate v0.1.0/go.mod h1:iSmxcyjqTsJpI2R4NaDN7+kN2VEUnK/pcBlmesArF7c=
github.com/golang/glog v0.0.0-20160126235308-23def4e6c14b/go.mod h1:SBH7ygxi8pfUlaOkMMuAQtPIUF8ecWP5IEl/CR7VP2Q=
github.com/golang/mock v1.1.1/go.mod h1:oTYuIxOrZwtPieC+H1uAHpcLFnEyAGVDL/k47Jfbm0A=
github.com/golang/protobuf v1.2.0/go.mod h1:6lQm79b+lXiMfvg/cZm0SGofjICqVBUtrP5yJMmIC1U=
github.com/golang/protobuf v1.3.2/go.mod h1:6lQm79b+lXiMfvg/cZm0SGofjICqVBUtrP5yJMmIC1U=
github.com/golang/protobuf v1.4.0-rc.1/go.mod h1:ceaxUfeHdC40wWswd/P6IGgMaK3YpKi5j83Wpe3EHw8=
github.com/golang/protobuf v1.4.0-rc.1.0.20200221234624-67d41d38c208/go.mod h1:xKAWHe0F5eneWXFV3EuXVDTCmh+JuBKY0li0aMyXATA=
github.com/golang/protobuf v1.4.0-rc.2/go.mod h1:LlEzMj4AhA7rCAGe4KMBDvJI+AwstrUpVNzEA03Pprs=
github.com/golang/protobuf v1.4.0-rc.4.0.20200313231945-b860323f09d0/go.mod h1:WU3c8KckQ9AFe+yFwt9sWVRKCVIyN9cPHBJSNnbL67w=
github.com/golang/protobuf v1.4.0/go.mod h1:jodUvKwWbYaEsadDk5Fwe5c77LiNKVO9IDvqG2KuDX0=
github.com/golang/protobuf v1.4.1/go.mod h1:U8fpvMrcmy5pZrNK1lt4xCsGvpyWQ/VVv6QDs8UjoX8=
github.com/golang/protobuf v1.4.2 h1:+Z5KGCizgyZCbGh1KZqA0fcLLkwbsjIzS4aV2v7wJX0=
github.com/golang/protobuf v1.4.2/go.mod h1:oDoupMAO8OvCJWAcko0GGGIgR6R6ocIYbsSw735rRwI=
github.com/google/go-cmp v0.2.0/go.mod h1:oXzfMopK8JAjlY9xF4vHSVASa0yLyX7SntLO5aqRK0M=
github.com/google/go-cmp v0.3.0/go.mod h1:8QqcDgzrUqlUb/G2PQTWiueGozuR1884gddMywk6iLU=
github.com/google/go-cmp v0.3.1/go.mod h1:8QqcDgzrUqlUb/G2PQTWiueGozuR1884gddMywk6iLU=
github.com/google/go-cmp v0.4.0/go.mod h1:v8dTdLbMG2kIc/vJvl+f65V22dbkXbowE6jgT/gNBxE=
github.com/google/go-cmp v0.5.0/go.mod h1:v8dTdLbMG2kIc/vJvl+f65V22dbkXbowE6jgT/gNBxE=
github.com/prometheus/client_model v0.0.0-20190812154241-14fe0d1b01d4/go.mod h1:xMI15A0UPsDsEKsMN9yxemIoYk6Tm2C1GtYGdfGttqA=
golang.org/x/crypto v0.0.0-20190308221718-c2843e01d9a2/go.mod h1:djNgcEr1/C05ACkg1iLfiJU5Ep61QUkGW8qpdssI0+w=
golang.org/x/exp v0.0.0-20190121172915-509febef88a4/go.mod h1:CJ0aWSM057203Lf6IL+f9T1iT9GByDxfZKAQTCR3kQA=
golang.org/x/lint v0.0.0-20181026193005-c67002cb31c3/go.mod h1:UVdnD1Gm6xHRNCYTkRU2/jEulfH38KcIWyp/GAMgvoE=
golang.org/x/lint v0.0.0-20190227174305-5b3e6a55c961/go.mod h1:wehouNa3lNwaWXcvxsM5YxQ5yQlVC4a0KAMCusXpPoU=
golang.org/x/lint v0.0.0-20190313153728-d0100b6bd8b3/go.mod h1:6SW0HCj/g11FgYtHlgUYUwCkIfeOF89ocIRzGO/8vkc=
golang.org/x/net v0.0.0-20180724234803-3673e40ba225/go.mod h1:mL1N/T3taQHkDXs73rZJwtUhF3w3ftmwwsq0BUmARs4=
golang.org/x/net v0.0.0-20180826012351-8a410e7b638d/go.mod h1:mL1N/T3taQHkDXs73rZJwtUhF3w3ftmwwsq0BUmARs4=
golang.org/x/net v0.0.0-20190213061140-3a22650c66bd/go.mod h1:mL1N/T3taQHkDXs73rZJwtUhF3w3ftmwwsq0BUmARs4=
golang.org/x/net v0.0.0-20190311183353-d8887717615a/go.mod h1:t9HGtf8HONx5eT2rtn7q6eTqICYqUVnKs3thJo3Qplg=
golang.org/x/oauth2 v0.0.0-20180821212333-d2e6202438be/go.mod h1:N/0e6XlmueqKjAGxoOufVs8QHGRruUQn6yWY3a++T0U=
golang.org/x/sync v0.0.0-20180314180146-1d60e4601c6f/go.mod h1:RxMgew5VJxzue5/jJTE5uejpjVlOe/izrB70Jof72aM=
golang.org/x/sync v0.0.0-20181108010431-42b317875d0f/go.mod h1:RxMgew5VJxzue5/jJTE5uejpjVlOe/izrB70Jof72aM=
golang.org/x/sync v0.0.0-20190423024810-112230192c58/go.mod h1:RxMgew5VJxzue5/jJTE5uejpjVlOe/izrB70Jof72aM=
golang.org/x/sys v0.0.0-20180830151530-49385e6e1522/go.mod h1:STP8DvDyc/dI5b8T5hshtkjS+E42TnysNCUPdjciGhY=
golang.org/x/sys v0.0.0-20190215142949-d0b11bdaac8a/go.mod h1:STP8DvDyc/dI5b8T5hshtkjS+E42TnysNCUPdjciGhY=
golang.org/x/text v0.3.0/go.mod h1:NqM8EUOU14njkJ3fqMW+pc6Ldnwhi/IjpwHt7yyuwOQ=
golang.org/x/tools v0.0.0-20190114222345-bf090417da8b/go.mod h1:n7NCudcB/nEzxVGmLbDWY5pfWTLqBcC2KZ6jyYvM4mQ=
golang.org/x/tools v0.0.0-20190226205152-f727befe758c/go.mod h1:9Yl7xja0Znq3iFh3HoIrodX9oNMXvdceNzlUR8zjMvY=
golang.org/x/tools v0.0.0-20190311212946-11955173bddd/go.mod h1:LCzVGOaR6xXOjkQ3onu1FJEFr0SW1gC7cKk1uF8kGRs=
golang.org/x/tools v0.0.0-20190524140312-2c0ae7006135/go.mod h1:RgjU9mgBXZiqYHBnxXauZ1Gv1EHHAz9KjViQ78xBX0Q=
golang.org/x/xerrors v0.0.0-20191204190536-9bdfabe68543/go.mod h1:I/5z698sn9Ka8TeJc9MKroUUfqBBauWjQqLJ2OPfmY0=
google.golang.org/appengine v1.1.0/go.mod h1:EbEs0AVv82hx2wNQdGPgUI5lhzA/G0D9YwlJXL52JkM=
google.golang.org/appengine v1.4.0/go.mod h1:xpcJRLb0r/rnEns0DIKYYv+WjYCduHsrkT7/EB5XEv4=
google.golang.org/genproto v0.0.0-20180817151627-c66870c02cf8/go.mod h1:JiN7NxoALGmiZfu7CAH4rXhgtRTLTxftemlI0sWmxmc=
google.golang.org/genproto v0.0.0-20190819201941-24fa4b261c55/go.mod h1:DMBHOl98Agz4BDEuKkezgsaosCRResVns1a3J2ZsMNc=
google.golang.org/genproto v0.0.0-20200526211855-cb27e3aa2013/go.mod h1:NbSheEEYHJ7i3ixzK3sjbqSGDJWnxyFXZblF3eUsNvo=
google.golang.org/grpc v1.19.0/go.mod h1:mqu4LbDTu4XGKhr4mRzUsmM4RtVoemTSY81AxZiDr8c=
google.golang.org/grpc v1.23.0/go.mod h1:Y5yQAOtifL1yxbo5wqy6BxZv8vAUGQwXBOALyacEbxg=
google.golang.org/grpc v1.27.0/go.mod h1:qbnxyOmOxrQa7FizSgH+ReBfzJrCY1pSN7KXBS8abTk=
google.golang.org/protobuf v0.0.0-20200109180630-ec00e32a8dfd/go.mod h1:DFci5gLYBciE7Vtevhsrf46CRTquxDuWsQurQQe4oz8=
google.golang.org/protobuf v0.0.0-20200221191635-4d8936d0db64/go.mod h1:kwYJMbMJ01Woi6D6+Kah6886xMZcty6N08ah7+eCXa0=
google.golang.org/protobuf v0.0.0-20200228230310-ab0ca4ff8a60/go.mod h1:cfTl7dwQJ+fmap5saPgwCLgHXTUD7jkjRqWcaiX5VyM=
google.golang.org/protobuf v1.20.1-0.20200309200217-e05f789c0967/go.mod h1:A+miEFZTKqfCUM6K7xSMQL9OKL/b6hQv+e19PK+JZNE=
google.golang.org/protobuf v1.21.0/go.mod h1:47Nbq4nVaFHyn7ilMalzfO3qCViNmqZ2kzikPIcrTAo=
google.golang.org/protobuf v1.22.0/go.mod h1:EGpADcykh3NcUnDUJcl1+ZksZNG86OlYog2l/sGQquU=
google.golang.org/protobuf v1.23.0/go.mod h1:EGpADcykh3NcUnDUJcl1+ZksZNG86OlYog2l/sGQquU=
google.golang.org/protobuf v1.23.1-0.20200526195155-81db48ad09cc/go.mod h1:EGpADcykh3NcUnDUJcl1+ZksZNG86OlYog2l/sGQquU=
google.golang.org/protobuf v1.25.0 h1:Ejskq+SyPohKW+1uil0JJMtmHCgJPJ/qWTxr8qp+R4c=
google.golang.org/protobuf v1.25.0/go.mod h1:9JNX74DMeImyA3h4bdi1ymwjUzf21/xIlbajtzgsN7c=
honnef.co/go/tools v0.0.0-20190102054323-c2f93a96b099/go.mod h1:rf3lG4BRIbNafJWhAfAdb/ePZxsR/4RtNHQocxwk9r4=
honnef.co/go/tools v0.0.0-20190523083050-ea95bdfd59fc/go.mod h1:rf3lG4BRIbNafJWhAfAdb/ePZxsR/4RtNHQocxwk9r4=
```

## File: `proto/fixtures/generate/main.go`
```go
package main

import (
	"os"

	"github.com/golang/protobuf/proto"
	"github.com/segmentio/encoding/proto/fixtures"
)

func main() {
	os.Mkdir("protobuf", 0o755)

	tests := []struct {
		name  string
		value fixtures.Message
	}{
		{
			name: "message.pb",
			value: fixtures.Message{
				A: 10,
				B: 20,
				C: 30,
				D: "Hello World!",
			},
		},
	}

	for _, test := range tests {
		b, _ := proto.Marshal(&test.value)
		os.WriteFile("protobuf/"+test.name, b, 0o644)
	}
}
```

## File: `proto/fixtures/protobuf/message.pb`
```

"Hello World!
```

## File: `thrift/binary.go`
```go
package thrift

import (
	"bufio"
	"bytes"
	"encoding/binary"
	"fmt"
	"io"
	"math"
)

// BinaryProtocol is a Protocol implementation for the binary thrift protocol.
//
// https://github.com/apache/thrift/blob/master/doc/specs/thrift-binary-protocol.md
type BinaryProtocol struct {
	NonStrict bool
}

func (p *BinaryProtocol) NewReader(r io.Reader) Reader {
	return &binaryReader{p: p, r: r}
}

func (p *BinaryProtocol) NewWriter(w io.Writer) Writer {
	return &binaryWriter{p: p, w: w}
}

func (p *BinaryProtocol) Features() Features {
	return 0
}

type binaryReader struct {
	p *BinaryProtocol
	r io.Reader
	b [8]byte
}

func (r *binaryReader) Protocol() Protocol {
	return r.p
}

func (r *binaryReader) Reader() io.Reader {
	return r.r
}

func (r *binaryReader) ReadBool() (bool, error) {
	v, err := r.ReadByte()
	return v != 0, err
}

func (r *binaryReader) ReadInt8() (int8, error) {
	b, err := r.ReadByte()
	return int8(b), err
}

func (r *binaryReader) ReadInt16() (int16, error) {
	b, err := r.read(2)
	if len(b) < 2 {
		return 0, err
	}
	return int16(binary.BigEndian.Uint16(b)), nil
}

func (r *binaryReader) ReadInt32() (int32, error) {
	b, err := r.read(4)
	if len(b) < 4 {
		return 0, err
	}
	return int32(binary.BigEndian.Uint32(b)), nil
}

func (r *binaryReader) ReadInt64() (int64, error) {
	b, err := r.read(8)
	if len(b) < 8 {
		return 0, err
	}
	return int64(binary.BigEndian.Uint64(b)), nil
}

func (r *binaryReader) ReadFloat64() (float64, error) {
	b, err := r.read(8)
	if len(b) < 8 {
		return 0, err
	}
	return math.Float64frombits(binary.BigEndian.Uint64(b)), nil
}

func (r *binaryReader) ReadBytes() ([]byte, error) {
	n, err := r.ReadLength()
	if err != nil {
		return nil, err
	}
	b := make([]byte, n)
	_, err = io.ReadFull(r.r, b)
	return b, err
}

func (r *binaryReader) ReadString() (string, error) {
	b, err := r.ReadBytes()
	return unsafeBytesToString(b), err
}

func (r *binaryReader) ReadLength() (int, error) {
	b, err := r.read(4)
	if len(b) < 4 {
		return 0, err
	}
	n := binary.BigEndian.Uint32(b)
	if n > math.MaxInt32 {
		return 0, fmt.Errorf("length out of range: %d", n)
	}
	return int(n), nil
}

func (r *binaryReader) ReadMessage() (Message, error) {
	m := Message{}

	b, err := r.read(4)
	if len(b) < 4 {
		return m, err
	}

	if (b[0] >> 7) == 0 { // non-strict
		n := int(binary.BigEndian.Uint32(b))
		s := make([]byte, n)
		_, err := io.ReadFull(r.r, s)
		if err != nil {
			return m, dontExpectEOF(err)
		}
		m.Name = unsafeBytesToString(s)

		t, err := r.ReadInt8()
		if err != nil {
			return m, dontExpectEOF(err)
		}

		m.Type = MessageType(t & 0x7)
	} else {
		m.Type = MessageType(b[3] & 0x7)

		if m.Name, err = r.ReadString(); err != nil {
			return m, dontExpectEOF(err)
		}
	}

	m.SeqID, err = r.ReadInt32()
	return m, err
}

func (r *binaryReader) ReadField() (Field, error) {
	t, err := r.ReadInt8()
	if err != nil {
		return Field{}, err
	}
	i, err := r.ReadInt16()
	if err != nil {
		return Field{}, err
	}
	return Field{ID: i, Type: Type(t)}, nil
}

func (r *binaryReader) ReadList() (List, error) {
	t, err := r.ReadInt8()
	if err != nil {
		return List{}, err
	}
	n, err := r.ReadInt32()
	if err != nil {
		return List{}, dontExpectEOF(err)
	}
	return List{Size: n, Type: Type(t)}, nil
}

func (r *binaryReader) ReadSet() (Set, error) {
	l, err := r.ReadList()
	return Set(l), err
}

func (r *binaryReader) ReadMap() (Map, error) {
	k, err := r.ReadByte()
	if err != nil {
		return Map{}, err
	}
	v, err := r.ReadByte()
	if err != nil {
		return Map{}, dontExpectEOF(err)
	}
	n, err := r.ReadInt32()
	if err != nil {
		return Map{}, dontExpectEOF(err)
	}
	return Map{Size: n, Key: Type(k), Value: Type(v)}, nil
}

func (r *binaryReader) ReadByte() (byte, error) {
	switch x := r.r.(type) {
	case *bytes.Buffer:
		return x.ReadByte()
	case *bytes.Reader:
		return x.ReadByte()
	case *bufio.Reader:
		return x.ReadByte()
	case io.ByteReader:
		return x.ReadByte()
	default:
		b, err := r.read(1)
		if err != nil {
			return 0, err
		}
		return b[0], nil
	}
}

func (r *binaryReader) read(n int) ([]byte, error) {
	_, err := io.ReadFull(r.r, r.b[:n])
	return r.b[:n], err
}

type binaryWriter struct {
	p *BinaryProtocol
	b [8]byte
	w io.Writer
}

func (w *binaryWriter) Protocol() Protocol {
	return w.p
}

func (w *binaryWriter) Writer() io.Writer {
	return w.w
}

func (w *binaryWriter) WriteBool(v bool) error {
	var b byte
	if v {
		b = 1
	}
	return w.writeByte(b)
}

func (w *binaryWriter) WriteInt8(v int8) error {
	return w.writeByte(byte(v))
}

func (w *binaryWriter) WriteInt16(v int16) error {
	binary.BigEndian.PutUint16(w.b[:2], uint16(v))
	return w.write(w.b[:2])
}

func (w *binaryWriter) WriteInt32(v int32) error {
	binary.BigEndian.PutUint32(w.b[:4], uint32(v))
	return w.write(w.b[:4])
}

func (w *binaryWriter) WriteInt64(v int64) error {
	binary.BigEndian.PutUint64(w.b[:8], uint64(v))
	return w.write(w.b[:8])
}

func (w *binaryWriter) WriteFloat64(v float64) error {
	binary.BigEndian.PutUint64(w.b[:8], math.Float64bits(v))
	return w.write(w.b[:8])
}

func (w *binaryWriter) WriteBytes(v []byte) error {
	if err := w.WriteLength(len(v)); err != nil {
		return err
	}
	return w.write(v)
}

func (w *binaryWriter) WriteString(v string) error {
	if err := w.WriteLength(len(v)); err != nil {
		return err
	}
	return w.writeString(v)
}

func (w *binaryWriter) WriteLength(n int) error {
	if n < 0 {
		return fmt.Errorf("negative length cannot be encoded in thrift: %d", n)
	}
	if n > math.MaxInt32 {
		return fmt.Errorf("length is too large to be encoded in thrift: %d", n)
	}
	return w.WriteInt32(int32(n))
}

func (w *binaryWriter) WriteMessage(m Message) error {
	if w.p.NonStrict {
		if err := w.WriteString(m.Name); err != nil {
			return err
		}
		if err := w.writeByte(byte(m.Type)); err != nil {
			return err
		}
	} else {
		w.b[0] = 1 << 7
		w.b[1] = 0
		w.b[2] = 0
		w.b[3] = byte(m.Type) & 0x7
		binary.BigEndian.PutUint32(w.b[4:], uint32(len(m.Name)))

		if err := w.write(w.b[:8]); err != nil {
			return err
		}
		if err := w.writeString(m.Name); err != nil {
			return err
		}
	}
	return w.WriteInt32(m.SeqID)
}

func (w *binaryWriter) WriteField(f Field) error {
	if err := w.writeByte(byte(f.Type)); err != nil {
		return err
	}
	return w.WriteInt16(f.ID)
}

func (w *binaryWriter) WriteList(l List) error {
	if err := w.writeByte(byte(l.Type)); err != nil {
		return err
	}
	return w.WriteInt32(l.Size)
}

func (w *binaryWriter) WriteSet(s Set) error {
	return w.WriteList(List(s))
}

func (w *binaryWriter) WriteMap(m Map) error {
	if err := w.writeByte(byte(m.Key)); err != nil {
		return err
	}
	if err := w.writeByte(byte(m.Value)); err != nil {
		return err
	}
	return w.WriteInt32(m.Size)
}

func (w *binaryWriter) write(b []byte) error {
	_, err := w.w.Write(b)
	return err
}

func (w *binaryWriter) writeString(s string) error {
	_, err := io.WriteString(w.w, s)
	return err
}

func (w *binaryWriter) writeByte(b byte) error {
	// The special cases are intended to reduce the runtime overheadof testing
	// for the io.ByteWriter interface for common types. Type assertions on a
	// concrete type is just a pointer comparison, instead of requiring a
	// complex lookup in the type metadata.
	switch x := w.w.(type) {
	case *bytes.Buffer:
		return x.WriteByte(b)
	case *bufio.Writer:
		return x.WriteByte(b)
	case io.ByteWriter:
		return x.WriteByte(b)
	default:
		w.b[0] = b
		return w.write(w.b[:1])
	}
}
```

## File: `thrift/compact.go`
```go
package thrift

import (
	"bufio"
	"bytes"
	"encoding/binary"
	"fmt"
	"io"
	"math"
)

// CompactProtocol is a Protocol implementation for the compact thrift protocol.
//
// https://github.com/apache/thrift/blob/master/doc/specs/thrift-compact-protocol.md#integer-encoding
type CompactProtocol struct{}

func (p *CompactProtocol) NewReader(r io.Reader) Reader {
	return &compactReader{protocol: p, binary: binaryReader{r: r}}
}

func (p *CompactProtocol) NewWriter(w io.Writer) Writer {
	return &compactWriter{protocol: p, binary: binaryWriter{w: w}}
}

func (p *CompactProtocol) Features() Features {
	return UseDeltaEncoding | CoalesceBoolFields
}

type compactReader struct {
	protocol *CompactProtocol
	binary   binaryReader
}

func (r *compactReader) Protocol() Protocol {
	return r.protocol
}

func (r *compactReader) Reader() io.Reader {
	return r.binary.Reader()
}

func (r *compactReader) ReadBool() (bool, error) {
	return r.binary.ReadBool()
}

func (r *compactReader) ReadInt8() (int8, error) {
	return r.binary.ReadInt8()
}

func (r *compactReader) ReadInt16() (int16, error) {
	v, err := r.readVarint("int16", math.MinInt16, math.MaxInt16)
	return int16(v), err
}

func (r *compactReader) ReadInt32() (int32, error) {
	v, err := r.readVarint("int32", math.MinInt32, math.MaxInt32)
	return int32(v), err
}

func (r *compactReader) ReadInt64() (int64, error) {
	return r.readVarint("int64", math.MinInt64, math.MaxInt64)
}

func (r *compactReader) ReadFloat64() (float64, error) {
	return r.binary.ReadFloat64()
}

func (r *compactReader) ReadBytes() ([]byte, error) {
	n, err := r.ReadLength()
	if err != nil {
		return nil, err
	}
	b := make([]byte, n)
	_, err = io.ReadFull(r.Reader(), b)
	return b, err
}

func (r *compactReader) ReadString() (string, error) {
	b, err := r.ReadBytes()
	return unsafeBytesToString(b), err
}

func (r *compactReader) ReadLength() (int, error) {
	n, err := r.readUvarint("length", math.MaxInt32)
	return int(n), err
}

func (r *compactReader) ReadMessage() (Message, error) {
	m := Message{}

	b0, err := r.ReadByte()
	if err != nil {
		return m, err
	}
	if b0 != 0x82 {
		return m, fmt.Errorf("invalid protocol id found when reading thrift message: %#x", b0)
	}

	b1, err := r.ReadByte()
	if err != nil {
		return m, dontExpectEOF(err)
	}

	seqID, err := r.readUvarint("seq id", math.MaxInt32)
	if err != nil {
		return m, dontExpectEOF(err)
	}

	m.Type = MessageType(b1) & 0x7
	m.SeqID = int32(seqID)
	m.Name, err = r.ReadString()
	return m, dontExpectEOF(err)
}

func (r *compactReader) ReadField() (Field, error) {
	f := Field{}

	b, err := r.ReadByte()
	if err != nil {
		return f, err
	}

	if Type(b) == STOP {
		return f, nil
	}

	if (b >> 4) != 0 {
		f = Field{ID: int16(b >> 4), Type: Type(b & 0xF), Delta: true}
	} else {
		i, err := r.ReadInt16()
		if err != nil {
			return f, dontExpectEOF(err)
		}
		f = Field{ID: i, Type: Type(b)}
	}

	return f, nil
}

func (r *compactReader) ReadList() (List, error) {
	b, err := r.ReadByte()
	if err != nil {
		return List{}, err
	}
	if (b >> 4) != 0xF {
		return List{Size: int32(b >> 4), Type: Type(b & 0xF)}, nil
	}
	n, err := r.readUvarint("list size", math.MaxInt32)
	if err != nil {
		return List{}, dontExpectEOF(err)
	}
	return List{Size: int32(n), Type: Type(b & 0xF)}, nil
}

func (r *compactReader) ReadSet() (Set, error) {
	l, err := r.ReadList()
	return Set(l), err
}

func (r *compactReader) ReadMap() (Map, error) {
	n, err := r.readUvarint("map size", math.MaxInt32)
	if err != nil {
		return Map{}, err
	}
	if n == 0 { // empty map
		return Map{}, nil
	}
	b, err := r.ReadByte()
	if err != nil {
		return Map{}, dontExpectEOF(err)
	}
	return Map{Size: int32(n), Key: Type(b >> 4), Value: Type(b & 0xF)}, nil
}

func (r *compactReader) ReadByte() (byte, error) {
	return r.binary.ReadByte()
}

func (r *compactReader) readUvarint(typ string, max uint64) (uint64, error) {
	var br io.ByteReader

	switch x := r.Reader().(type) {
	case *bytes.Buffer:
		br = x
	case *bytes.Reader:
		br = x
	case *bufio.Reader:
		br = x
	case io.ByteReader:
		br = x
	default:
		br = &r.binary
	}

	u, err := binary.ReadUvarint(br)
	if err == nil {
		if u > max {
			err = fmt.Errorf("%s varint out of range: %d > %d", typ, u, max)
		}
	}
	return u, err
}

func (r *compactReader) readVarint(typ string, min, max int64) (int64, error) {
	var br io.ByteReader

	switch x := r.Reader().(type) {
	case *bytes.Buffer:
		br = x
	case *bytes.Reader:
		br = x
	case *bufio.Reader:
		br = x
	case io.ByteReader:
		br = x
	default:
		br = &r.binary
	}

	v, err := binary.ReadVarint(br)
	if err == nil {
		if v < min || v > max {
			err = fmt.Errorf("%s varint out of range: %d not in [%d;%d]", typ, v, min, max)
		}
	}
	return v, err
}

type compactWriter struct {
	protocol *CompactProtocol
	binary   binaryWriter
	varint   [binary.MaxVarintLen64]byte
}

func (w *compactWriter) Protocol() Protocol {
	return w.protocol
}

func (w *compactWriter) Writer() io.Writer {
	return w.binary.Writer()
}

func (w *compactWriter) WriteBool(v bool) error {
	return w.binary.WriteBool(v)
}

func (w *compactWriter) WriteInt8(v int8) error {
	return w.binary.WriteInt8(v)
}

func (w *compactWriter) WriteInt16(v int16) error {
	return w.writeVarint(int64(v))
}

func (w *compactWriter) WriteInt32(v int32) error {
	return w.writeVarint(int64(v))
}

func (w *compactWriter) WriteInt64(v int64) error {
	return w.writeVarint(v)
}

func (w *compactWriter) WriteFloat64(v float64) error {
	return w.binary.WriteFloat64(v)
}

func (w *compactWriter) WriteBytes(v []byte) error {
	if err := w.WriteLength(len(v)); err != nil {
		return err
	}
	return w.binary.write(v)
}

func (w *compactWriter) WriteString(v string) error {
	if err := w.WriteLength(len(v)); err != nil {
		return err
	}
	return w.binary.writeString(v)
}

func (w *compactWriter) WriteLength(n int) error {
	if n < 0 {
		return fmt.Errorf("negative length cannot be encoded in thrift: %d", n)
	}
	if n > math.MaxInt32 {
		return fmt.Errorf("length is too large to be encoded in thrift: %d", n)
	}
	return w.writeUvarint(uint64(n))
}

func (w *compactWriter) WriteMessage(m Message) error {
	if err := w.binary.writeByte(0x82); err != nil {
		return err
	}
	if err := w.binary.writeByte(byte(m.Type)); err != nil {
		return err
	}
	if err := w.writeUvarint(uint64(m.SeqID)); err != nil {
		return err
	}
	return w.WriteString(m.Name)
}

func (w *compactWriter) WriteField(f Field) error {
	if f.Type == STOP {
		return w.binary.writeByte(0)
	}
	if f.ID <= 15 {
		return w.binary.writeByte(byte(f.ID<<4) | byte(f.Type))
	}
	if err := w.binary.writeByte(byte(f.Type)); err != nil {
		return err
	}
	return w.WriteInt16(f.ID)
}

func (w *compactWriter) WriteList(l List) error {
	if l.Size <= 14 {
		return w.binary.writeByte(byte(l.Size<<4) | byte(l.Type))
	}
	if err := w.binary.writeByte(0xF0 | byte(l.Type)); err != nil {
		return err
	}
	return w.writeUvarint(uint64(l.Size))
}

func (w *compactWriter) WriteSet(s Set) error {
	return w.WriteList(List(s))
}

func (w *compactWriter) WriteMap(m Map) error {
	if err := w.writeUvarint(uint64(m.Size)); err != nil || m.Size == 0 {
		return err
	}
	return w.binary.writeByte((byte(m.Key) << 4) | byte(m.Value))
}

func (w *compactWriter) writeUvarint(v uint64) error {
	n := binary.PutUvarint(w.varint[:], v)
	return w.binary.write(w.varint[:n])
}

func (w *compactWriter) writeVarint(v int64) error {
	n := binary.PutVarint(w.varint[:], v)
	return w.binary.write(w.varint[:n])
}
```

## File: `thrift/debug.go`
```go
package thrift

import (
	"io"
	"log"
)

func NewDebugReader(r Reader, l *log.Logger) Reader {
	return &debugReader{
		r: r,
		l: l,
	}
}

func NewDebugWriter(w Writer, l *log.Logger) Writer {
	return &debugWriter{
		w: w,
		l: l,
	}
}

type debugReader struct {
	r Reader
	l *log.Logger
}

func (d *debugReader) log(method string, res any, err error) {
	if err != nil {
		d.l.Printf("(%T).%s() → ERROR: %v", d.r, method, err)
	} else {
		d.l.Printf("(%T).%s() → %#v", d.r, method, res)
	}
}

func (d *debugReader) Protocol() Protocol {
	return d.r.Protocol()
}

func (d *debugReader) Reader() io.Reader {
	return d.r.Reader()
}

func (d *debugReader) ReadBool() (bool, error) {
	v, err := d.r.ReadBool()
	d.log("ReadBool", v, err)
	return v, err
}

func (d *debugReader) ReadInt8() (int8, error) {
	v, err := d.r.ReadInt8()
	d.log("ReadInt8", v, err)
	return v, err
}

func (d *debugReader) ReadInt16() (int16, error) {
	v, err := d.r.ReadInt16()
	d.log("ReadInt16", v, err)
	return v, err
}

func (d *debugReader) ReadInt32() (int32, error) {
	v, err := d.r.ReadInt32()
	d.log("ReadInt32", v, err)
	return v, err
}

func (d *debugReader) ReadInt64() (int64, error) {
	v, err := d.r.ReadInt64()
	d.log("ReadInt64", v, err)
	return v, err
}

func (d *debugReader) ReadFloat64() (float64, error) {
	v, err := d.r.ReadFloat64()
	d.log("ReadFloat64", v, err)
	return v, err
}

func (d *debugReader) ReadBytes() ([]byte, error) {
	v, err := d.r.ReadBytes()
	d.log("ReadBytes", v, err)
	return v, err
}

func (d *debugReader) ReadString() (string, error) {
	v, err := d.r.ReadString()
	d.log("ReadString", v, err)
	return v, err
}

func (d *debugReader) ReadLength() (int, error) {
	v, err := d.r.ReadLength()
	d.log("ReadLength", v, err)
	return v, err
}

func (d *debugReader) ReadMessage() (Message, error) {
	v, err := d.r.ReadMessage()
	d.log("ReadMessage", v, err)
	return v, err
}

func (d *debugReader) ReadField() (Field, error) {
	v, err := d.r.ReadField()
	d.log("ReadField", v, err)
	return v, err
}

func (d *debugReader) ReadList() (List, error) {
	v, err := d.r.ReadList()
	d.log("ReadList", v, err)
	return v, err
}

func (d *debugReader) ReadSet() (Set, error) {
	v, err := d.r.ReadSet()
	d.log("ReadSet", v, err)
	return v, err
}

func (d *debugReader) ReadMap() (Map, error) {
	v, err := d.r.ReadMap()
	d.log("ReadMap", v, err)
	return v, err
}

type debugWriter struct {
	w Writer
	l *log.Logger
}

func (d *debugWriter) log(method string, arg any, err error) {
	if err != nil {
		d.l.Printf("(%T).%s(%#v) → ERROR: %v", d.w, method, arg, err)
	} else {
		d.l.Printf("(%T).%s(%#v)", d.w, method, arg)
	}
}

func (d *debugWriter) Protocol() Protocol {
	return d.w.Protocol()
}

func (d *debugWriter) Writer() io.Writer {
	return d.w.Writer()
}

func (d *debugWriter) WriteBool(v bool) error {
	err := d.w.WriteBool(v)
	d.log("WriteBool", v, err)
	return err
}

func (d *debugWriter) WriteInt8(v int8) error {
	err := d.w.WriteInt8(v)
	d.log("WriteInt8", v, err)
	return err
}

func (d *debugWriter) WriteInt16(v int16) error {
	err := d.w.WriteInt16(v)
	d.log("WriteInt16", v, err)
	return err
}

func (d *debugWriter) WriteInt32(v int32) error {
	err := d.w.WriteInt32(v)
	d.log("WriteInt32", v, err)
	return err
}

func (d *debugWriter) WriteInt64(v int64) error {
	err := d.w.WriteInt64(v)
	d.log("WriteInt64", v, err)
	return err
}

func (d *debugWriter) WriteFloat64(v float64) error {
	err := d.w.WriteFloat64(v)
	d.log("WriteFloat64", v, err)
	return err
}

func (d *debugWriter) WriteBytes(v []byte) error {
	err := d.w.WriteBytes(v)
	d.log("WriteBytes", v, err)
	return err
}

func (d *debugWriter) WriteString(v string) error {
	err := d.w.WriteString(v)
	d.log("WriteString", v, err)
	return err
}

func (d *debugWriter) WriteLength(n int) error {
	err := d.w.WriteLength(n)
	d.log("WriteLength", n, err)
	return err
}

func (d *debugWriter) WriteMessage(m Message) error {
	err := d.w.WriteMessage(m)
	d.log("WriteMessage", m, err)
	return err
}

func (d *debugWriter) WriteField(f Field) error {
	err := d.w.WriteField(f)
	d.log("WriteField", f, err)
	return err
}

func (d *debugWriter) WriteList(l List) error {
	err := d.w.WriteList(l)
	d.log("WriteList", l, err)
	return err
}

func (d *debugWriter) WriteSet(s Set) error {
	err := d.w.WriteSet(s)
	d.log("WriteSet", s, err)
	return err
}

func (d *debugWriter) WriteMap(m Map) error {
	err := d.w.WriteMap(m)
	d.log("WriteMap", m, err)
	return err
}
```

## File: `thrift/decode.go`
```go
package thrift

import (
	"bufio"
	"bytes"
	"fmt"
	"io"
	"reflect"
	"sync/atomic"
)

// Unmarshal deserializes the thrift data from b to v using to the protocol p.
//
// The function errors if the data in b does not match the type of v.
//
// The function panics if v cannot be converted to a thrift representation.
//
// As an optimization, the value passed in v may be reused across multiple calls
// to Unmarshal, allowing the function to reuse objects referenced by pointer
// fields of struct values. When reusing objects, the application is responsible
// for resetting the state of v before calling Unmarshal again.
func Unmarshal(p Protocol, b []byte, v any) error {
	br := bytes.NewReader(b)
	pr := p.NewReader(br)

	if err := NewDecoder(pr).Decode(v); err != nil {
		return err
	}

	if n := br.Len(); n != 0 {
		return fmt.Errorf("unexpected trailing bytes at the end of thrift input: %d", n)
	}

	return nil
}

type Decoder struct {
	r Reader
	f flags
}

func NewDecoder(r Reader) *Decoder {
	return &Decoder{r: r, f: decoderFlags(r)}
}

func (d *Decoder) Decode(v any) error {
	t := reflect.TypeOf(v)
	p := reflect.ValueOf(v)

	if t.Kind() != reflect.Ptr {
		panic("thrift.(*Decoder).Decode: expected pointer type but got " + t.String())
	}

	t = t.Elem()
	p = p.Elem()

	cache, _ := decoderCache.Load().(map[typeID]decodeFunc)
	decode := cache[makeTypeID(t)]

	if decode == nil {
		decode = decodeFuncOf(t, make(decodeFuncCache))

		newCache := make(map[typeID]decodeFunc, len(cache)+1)
		newCache[makeTypeID(t)] = decode
		for k, v := range cache {
			newCache[k] = v
		}

		decoderCache.Store(newCache)
	}

	return decode(d.r, p, d.f)
}

func (d *Decoder) Reset(r Reader) {
	d.r = r
	d.f = d.f.without(protocolFlags).with(decoderFlags(r))
}

func (d *Decoder) SetStrict(enabled bool) {
	if enabled {
		d.f = d.f.with(strict)
	} else {
		d.f = d.f.without(strict)
	}
}

func decoderFlags(r Reader) flags {
	return flags(r.Protocol().Features() << featuresBitOffset)
}

var decoderCache atomic.Value // map[typeID]decodeFunc

type decodeFunc func(Reader, reflect.Value, flags) error

type decodeFuncCache map[reflect.Type]decodeFunc

func decodeFuncOf(t reflect.Type, seen decodeFuncCache) decodeFunc {
	f := seen[t]
	if f != nil {
		return f
	}
	switch t.Kind() {
	case reflect.Bool:
		f = decodeBool
	case reflect.Int8:
		f = decodeInt8
	case reflect.Int16:
		f = decodeInt16
	case reflect.Int32:
		f = decodeInt32
	case reflect.Int64, reflect.Int:
		f = decodeInt64
	case reflect.Float32, reflect.Float64:
		f = decodeFloat64
	case reflect.String:
		f = decodeString
	case reflect.Slice:
		if t.Elem().Kind() == reflect.Uint8 { // []byte
			f = decodeBytes
		} else {
			f = decodeFuncSliceOf(t, seen)
		}
	case reflect.Map:
		f = decodeFuncMapOf(t, seen)
	case reflect.Struct:
		f = decodeFuncStructOf(t, seen)
	case reflect.Ptr:
		f = decodeFuncPtrOf(t, seen)
	default:
		panic("type cannot be decoded in thrift: " + t.String())
	}
	seen[t] = f
	return f
}

func decodeBool(r Reader, v reflect.Value, _ flags) error {
	b, err := r.ReadBool()
	if err != nil {
		return err
	}
	v.SetBool(b)
	return nil
}

func decodeInt8(r Reader, v reflect.Value, _ flags) error {
	i, err := r.ReadInt8()
	if err != nil {
		return err
	}
	v.SetInt(int64(i))
	return nil
}

func decodeInt16(r Reader, v reflect.Value, _ flags) error {
	i, err := r.ReadInt16()
	if err != nil {
		return err
	}
	v.SetInt(int64(i))
	return nil
}

func decodeInt32(r Reader, v reflect.Value, _ flags) error {
	i, err := r.ReadInt32()
	if err != nil {
		return err
	}
	v.SetInt(int64(i))
	return nil
}

func decodeInt64(r Reader, v reflect.Value, _ flags) error {
	i, err := r.ReadInt64()
	if err != nil {
		return err
	}
	v.SetInt(int64(i))
	return nil
}

func decodeFloat64(r Reader, v reflect.Value, _ flags) error {
	f, err := r.ReadFloat64()
	if err != nil {
		return err
	}
	v.SetFloat(f)
	return nil
}

func decodeString(r Reader, v reflect.Value, _ flags) error {
	s, err := r.ReadString()
	if err != nil {
		return err
	}
	v.SetString(s)
	return nil
}

func decodeBytes(r Reader, v reflect.Value, _ flags) error {
	b, err := r.ReadBytes()
	if err != nil {
		return err
	}
	v.SetBytes(b)
	return nil
}

func decodeFuncSliceOf(t reflect.Type, seen decodeFuncCache) decodeFunc {
	elem := t.Elem()
	typ := TypeOf(elem)
	dec := decodeFuncOf(elem, seen)

	return func(r Reader, v reflect.Value, flags flags) error {
		l, err := r.ReadList()
		if err != nil {
			return err
		}

		// Sometimes the list type is set to TRUE when the list contains only
		// TRUE values. Thrift does not seem to optimize the encoding by
		// omitting the boolean values that are known to all be TRUE, we still
		// need to decode them.
		switch l.Type {
		case TRUE:
			l.Type = BOOL
		}

		// TODO: implement type conversions?
		if typ != l.Type {
			if flags.have(strict) {
				return &TypeMismatch{item: "list item", Expect: typ, Found: l.Type}
			}
			return nil
		}

		v.Set(reflect.MakeSlice(t, int(l.Size), int(l.Size)))
		flags = flags.only(decodeFlags)

		for i := range int(l.Size) {
			if err := dec(r, v.Index(i), flags); err != nil {
				return with(dontExpectEOF(err), &decodeErrorList{cause: l, index: i})
			}
		}

		return nil
	}
}

func decodeFuncMapOf(t reflect.Type, seen decodeFuncCache) decodeFunc {
	key, elem := t.Key(), t.Elem()
	if elem.Size() == 0 { // map[?]struct{}
		return decodeFuncMapAsSetOf(t, seen)
	}

	mapType := reflect.MapOf(key, elem)
	keyZero := reflect.Zero(key)
	elemZero := reflect.Zero(elem)
	keyType := TypeOf(key)
	elemType := TypeOf(elem)
	decodeKey := decodeFuncOf(key, seen)
	decodeElem := decodeFuncOf(elem, seen)

	return func(r Reader, v reflect.Value, flags flags) error {
		m, err := r.ReadMap()
		if err != nil {
			return err
		}

		v.Set(reflect.MakeMapWithSize(mapType, int(m.Size)))

		if m.Size == 0 { // empty map
			return nil
		}

		// TODO: implement type conversions?
		if keyType != m.Key {
			if flags.have(strict) {
				return &TypeMismatch{item: "map key", Expect: keyType, Found: m.Key}
			}
			return nil
		}

		if elemType != m.Value {
			if flags.have(strict) {
				return &TypeMismatch{item: "map value", Expect: elemType, Found: m.Value}
			}
			return nil
		}

		tmpKey := reflect.New(key).Elem()
		tmpElem := reflect.New(elem).Elem()
		flags = flags.only(decodeFlags)

		for i := range int(m.Size) {
			if err := decodeKey(r, tmpKey, flags); err != nil {
				return with(dontExpectEOF(err), &decodeErrorMap{cause: m, index: i})
			}
			if err := decodeElem(r, tmpElem, flags); err != nil {
				return with(dontExpectEOF(err), &decodeErrorMap{cause: m, index: i})
			}
			v.SetMapIndex(tmpKey, tmpElem)
			tmpKey.Set(keyZero)
			tmpElem.Set(elemZero)
		}

		return nil
	}
}

func decodeFuncMapAsSetOf(t reflect.Type, seen decodeFuncCache) decodeFunc {
	key, elem := t.Key(), t.Elem()
	keyZero := reflect.Zero(key)
	elemZero := reflect.Zero(elem)
	typ := TypeOf(key)
	dec := decodeFuncOf(key, seen)

	return func(r Reader, v reflect.Value, flags flags) error {
		s, err := r.ReadSet()
		if err != nil {
			return err
		}

		// See decodeFuncSliceOf for details about why this type conversion
		// needs to be done.
		switch s.Type {
		case TRUE:
			s.Type = BOOL
		}

		v.Set(reflect.MakeMapWithSize(t, int(s.Size)))

		if s.Size == 0 {
			return nil
		}

		// TODO: implement type conversions?
		if typ != s.Type {
			if flags.have(strict) {
				return &TypeMismatch{item: "list item", Expect: typ, Found: s.Type}
			}
			return nil
		}

		tmp := reflect.New(key).Elem()
		flags = flags.only(decodeFlags)

		for i := range int(s.Size) {
			if err := dec(r, tmp, flags); err != nil {
				return with(dontExpectEOF(err), &decodeErrorSet{cause: s, index: i})
			}
			v.SetMapIndex(tmp, elemZero)
			tmp.Set(keyZero)
		}

		return nil
	}
}

type structDecoder struct {
	fields   []structDecoderField
	union    []int
	minID    int16
	zero     reflect.Value
	required []uint64
}

func (dec *structDecoder) decode(r Reader, v reflect.Value, flags flags) error {
	flags = flags.only(decodeFlags)
	coalesceBoolFields := flags.have(coalesceBoolFields)

	lastField := reflect.Value{}
	union := len(dec.union) > 0
	seen := make([]uint64, 1)
	if len(dec.required) > len(seen) {
		seen = make([]uint64, len(dec.required))
	}

	err := readStruct(r, func(r Reader, f Field) error {
		i := int(f.ID) - int(dec.minID)
		if i < 0 || i >= len(dec.fields) || dec.fields[i].decode == nil {
			return skipField(r, f)
		}
		field := &dec.fields[i]
		seen[i/64] |= 1 << (i % 64)

		// TODO: implement type conversions?
		if f.Type != field.typ && (f.Type != TRUE || field.typ != BOOL) {
			if flags.have(strict) {
				return &TypeMismatch{item: "field value", Expect: field.typ, Found: f.Type}
			}
			return nil
		}

		x := v
		for _, i := range field.index {
			if x.Kind() == reflect.Ptr {
				x = x.Elem()
			}
			if x = x.Field(i); x.Kind() == reflect.Ptr {
				if x.IsNil() {
					x.Set(reflect.New(x.Type().Elem()))
				}
			}
		}

		if union {
			v.Set(dec.zero)
		}

		lastField = x

		if coalesceBoolFields && (f.Type == TRUE || f.Type == FALSE) {
			for x.Kind() == reflect.Ptr {
				if x.IsNil() {
					x.Set(reflect.New(x.Type().Elem()))
				}
				x = x.Elem()
			}
			x.SetBool(f.Type == TRUE)
			return nil
		}

		return field.decode(r, x, flags.with(field.flags))
	})
	if err != nil {
		return err
	}

	for i, required := range dec.required {
		if mask := required & seen[i]; mask != required {
			i *= 64
			for (mask & 1) != 0 {
				mask >>= 1
				i++
			}
			field := &dec.fields[i]
			return &MissingField{Field: Field{ID: field.id, Type: field.typ}}
		}
	}

	if union && lastField.IsValid() {
		v.FieldByIndex(dec.union).Set(lastField.Addr())
	}

	return nil
}

type structDecoderField struct {
	index  []int
	id     int16
	flags  flags
	typ    Type
	decode decodeFunc
}

func decodeFuncStructOf(t reflect.Type, seen decodeFuncCache) decodeFunc {
	dec := &structDecoder{
		zero: reflect.Zero(t),
	}
	decode := dec.decode
	seen[t] = decode

	fields := make([]structDecoderField, 0, t.NumField())
	forEachStructField(t, nil, func(f structField) {
		if f.flags.have(union) {
			dec.union = f.index
		} else {
			fields = append(fields, structDecoderField{
				index:  f.index,
				id:     f.id,
				flags:  f.flags,
				typ:    TypeOf(f.typ),
				decode: decodeFuncStructFieldOf(f, seen),
			})
		}
	})

	minID := int16(0)
	maxID := int16(0)

	for _, f := range fields {
		if f.id < minID || minID == 0 {
			minID = f.id
		}
		if f.id > maxID {
			maxID = f.id
		}
	}

	dec.fields = make([]structDecoderField, (maxID-minID)+1)
	dec.minID = minID
	dec.required = make([]uint64, len(fields)/64+1)

	for _, f := range fields {
		i := f.id - minID
		p := dec.fields[i]
		if p.decode != nil {
			panic(fmt.Errorf("thrift struct field id %d is present multiple times in %s with types %s and %s", f.id, t, p.typ, f.typ))
		}
		dec.fields[i] = f
		if f.flags.have(required) {
			dec.required[i/64] |= 1 << (i % 64)
		}
	}

	return decode
}

func decodeFuncStructFieldOf(f structField, seen decodeFuncCache) decodeFunc {
	if f.flags.have(enum) {
		switch f.typ.Kind() {
		case reflect.Int, reflect.Int8, reflect.Int16, reflect.Int32, reflect.Int64:
			return decodeInt32
		}
	}
	return decodeFuncOf(f.typ, seen)
}

func decodeFuncPtrOf(t reflect.Type, seen decodeFuncCache) decodeFunc {
	elem := t.Elem()
	decode := decodeFuncOf(t.Elem(), seen)
	return func(r Reader, v reflect.Value, f flags) error {
		if v.IsNil() {
			v.Set(reflect.New(elem))
		}
		return decode(r, v.Elem(), f)
	}
}

func readBinary(r Reader, f func(io.Reader) error) error {
	n, err := r.ReadLength()
	if err != nil {
		return err
	}
	return dontExpectEOF(f(io.LimitReader(r.Reader(), int64(n))))
}

func readList(r Reader, f func(Reader, Type) error) error {
	l, err := r.ReadList()
	if err != nil {
		return err
	}

	for i := range int(l.Size) {
		if err := f(r, l.Type); err != nil {
			return with(dontExpectEOF(err), &decodeErrorList{cause: l, index: i})
		}
	}

	return nil
}

func readSet(r Reader, f func(Reader, Type) error) error {
	s, err := r.ReadSet()
	if err != nil {
		return err
	}

	for i := range int(s.Size) {
		if err := f(r, s.Type); err != nil {
			return with(dontExpectEOF(err), &decodeErrorSet{cause: s, index: i})
		}
	}

	return nil
}

func readMap(r Reader, f func(Reader, Type, Type) error) error {
	m, err := r.ReadMap()
	if err != nil {
		return err
	}

	for i := range int(m.Size) {
		if err := f(r, m.Key, m.Value); err != nil {
			return with(dontExpectEOF(err), &decodeErrorMap{cause: m, index: i})
		}
	}

	return nil
}

func readStruct(r Reader, f func(Reader, Field) error) error {
	lastFieldID := int16(0)
	numFields := 0

	for {
		x, err := r.ReadField()
		if err != nil {
			if numFields > 0 {
				err = dontExpectEOF(err)
			}
			return err
		}

		if x.Type == STOP {
			return nil
		}

		if x.Delta {
			x.ID += lastFieldID
			x.Delta = false
		}

		if err := f(r, x); err != nil {
			return with(dontExpectEOF(err), &decodeErrorField{cause: x})
		}

		lastFieldID = x.ID
		numFields++
	}
}

func skip(r Reader, t Type) error {
	var err error
	switch t {
	case TRUE, FALSE:
		_, err = r.ReadBool()
	case I8:
		_, err = r.ReadInt8()
	case I16:
		_, err = r.ReadInt16()
	case I32:
		_, err = r.ReadInt32()
	case I64:
		_, err = r.ReadInt64()
	case DOUBLE:
		_, err = r.ReadFloat64()
	case BINARY:
		err = skipBinary(r)
	case LIST:
		err = skipList(r)
	case SET:
		err = skipSet(r)
	case MAP:
		err = skipMap(r)
	case STRUCT:
		err = skipStruct(r)
	default:
		return fmt.Errorf("skipping unsupported thrift type %d", t)
	}
	return err
}

func skipBinary(r Reader) error {
	n, err := r.ReadLength()
	if err != nil {
		return err
	}
	if n == 0 {
		return nil
	}
	switch x := r.Reader().(type) {
	case *bufio.Reader:
		_, err = x.Discard(int(n))
	default:
		_, err = io.CopyN(io.Discard, x, int64(n))
	}
	return dontExpectEOF(err)
}

func skipList(r Reader) error {
	return readList(r, skip)
}

func skipSet(r Reader) error {
	return readSet(r, skip)
}

func skipMap(r Reader) error {
	return readMap(r, func(r Reader, k, v Type) error {
		if err := skip(r, k); err != nil {
			return dontExpectEOF(err)
		}
		if err := skip(r, v); err != nil {
			return dontExpectEOF(err)
		}
		return nil
	})
}

func skipStruct(r Reader) error {
	return readStruct(r, skipField)
}

func skipField(r Reader, f Field) error {
	return skip(r, f.Type)
}
```

## File: `thrift/decode_test.go`
```go
package thrift_test

import (
	"bytes"
	"io"
	"testing"

	"github.com/segmentio/encoding/thrift"
)

func TestDecodeEOF(t *testing.T) {
	p := thrift.CompactProtocol{}
	d := thrift.NewDecoder(p.NewReader(bytes.NewReader(nil)))
	v := struct{ Name string }{}

	if err := d.Decode(&v); err != io.EOF {
		t.Errorf("unexpected error returned: %v", err)
	}
}
```

## File: `thrift/encode.go`
```go
package thrift

import (
	"bytes"
	"fmt"
	"math"
	"reflect"
	"sort"
	"sync/atomic"
)

// Marshal serializes v into a thrift representation according to the the
// protocol p.
//
// The function panics if v cannot be converted to a thrift representation.
func Marshal(p Protocol, v any) ([]byte, error) {
	buf := new(bytes.Buffer)
	enc := NewEncoder(p.NewWriter(buf))
	err := enc.Encode(v)
	return buf.Bytes(), err
}

type Encoder struct {
	w Writer
	f flags
}

func NewEncoder(w Writer) *Encoder {
	return &Encoder{w: w, f: encoderFlags(w)}
}

func (e *Encoder) Encode(v any) error {
	t := reflect.TypeOf(v)
	cache, _ := encoderCache.Load().(map[typeID]encodeFunc)
	encode := cache[makeTypeID(t)]

	if encode == nil {
		encode = encodeFuncOf(t, make(encodeFuncCache))

		newCache := make(map[typeID]encodeFunc, len(cache)+1)
		newCache[makeTypeID(t)] = encode
		for k, v := range cache {
			newCache[k] = v
		}

		encoderCache.Store(newCache)
	}

	return encode(e.w, reflect.ValueOf(v), e.f)
}

func (e *Encoder) Reset(w Writer) {
	e.w = w
	e.f = e.f.without(protocolFlags).with(encoderFlags(w))
}

func encoderFlags(w Writer) flags {
	return flags(w.Protocol().Features() << featuresBitOffset)
}

var encoderCache atomic.Value // map[typeID]encodeFunc

type encodeFunc func(Writer, reflect.Value, flags) error

type encodeFuncCache map[reflect.Type]encodeFunc

func encodeFuncOf(t reflect.Type, seen encodeFuncCache) encodeFunc {
	f := seen[t]
	if f != nil {
		return f
	}
	switch t.Kind() {
	case reflect.Bool:
		f = encodeBool
	case reflect.Int8:
		f = encodeInt8
	case reflect.Int16:
		f = encodeInt16
	case reflect.Int32:
		f = encodeInt32
	case reflect.Int64, reflect.Int:
		f = encodeInt64
	case reflect.Float32, reflect.Float64:
		f = encodeFloat64
	case reflect.String:
		f = encodeString
	case reflect.Slice:
		if t.Elem().Kind() == reflect.Uint8 {
			f = encodeBytes
		} else {
			f = encodeFuncSliceOf(t, seen)
		}
	case reflect.Map:
		f = encodeFuncMapOf(t, seen)
	case reflect.Struct:
		f = encodeFuncStructOf(t, seen)
	case reflect.Ptr:
		f = encodeFuncPtrOf(t, seen)
	default:
		panic("type cannot be encoded in thrift: " + t.String())
	}
	seen[t] = f
	return f
}

func encodeBool(w Writer, v reflect.Value, _ flags) error {
	return w.WriteBool(v.Bool())
}

func encodeInt8(w Writer, v reflect.Value, _ flags) error {
	return w.WriteInt8(int8(v.Int()))
}

func encodeInt16(w Writer, v reflect.Value, _ flags) error {
	return w.WriteInt16(int16(v.Int()))
}

func encodeInt32(w Writer, v reflect.Value, _ flags) error {
	return w.WriteInt32(int32(v.Int()))
}

func encodeInt64(w Writer, v reflect.Value, _ flags) error {
	return w.WriteInt64(v.Int())
}

func encodeFloat64(w Writer, v reflect.Value, _ flags) error {
	return w.WriteFloat64(v.Float())
}

func encodeString(w Writer, v reflect.Value, _ flags) error {
	return w.WriteString(v.String())
}

func encodeBytes(w Writer, v reflect.Value, _ flags) error {
	return w.WriteBytes(v.Bytes())
}

func encodeFuncSliceOf(t reflect.Type, seen encodeFuncCache) encodeFunc {
	elem := t.Elem()
	typ := TypeOf(elem)
	enc := encodeFuncOf(elem, seen)

	return func(w Writer, v reflect.Value, flags flags) error {
		n := v.Len()
		if n > math.MaxInt32 {
			return fmt.Errorf("slice length is too large to be represented in thrift: %d > max(int32)", n)
		}

		err := w.WriteList(List{
			Size: int32(n),
			Type: typ,
		})
		if err != nil {
			return err
		}

		for i := range n {
			if err := enc(w, v.Index(i), flags); err != nil {
				return err
			}
		}

		return nil
	}
}

func encodeFuncMapOf(t reflect.Type, seen encodeFuncCache) encodeFunc {
	key, elem := t.Key(), t.Elem()
	if elem.Size() == 0 { // map[?]struct{}
		return encodeFuncMapAsSetOf(t, seen)
	}

	keyType := TypeOf(key)
	elemType := TypeOf(elem)
	encodeKey := encodeFuncOf(key, seen)
	encodeElem := encodeFuncOf(elem, seen)

	return func(w Writer, v reflect.Value, flags flags) error {
		n := v.Len()
		if n > math.MaxInt32 {
			return fmt.Errorf("map length is too large to be represented in thrift: %d > max(int32)", n)
		}

		err := w.WriteMap(Map{
			Size:  int32(n),
			Key:   keyType,
			Value: elemType,
		})
		if err != nil {
			return err
		}
		if n == 0 { // empty map
			return nil
		}

		iter := v.MapRange()
		for iter.Next() {
			if err := encodeKey(w, iter.Key(), flags); err != nil {
				return err
			}
			if err := encodeElem(w, iter.Value(), flags); err != nil {
				return err
			}
		}

		return nil
	}
}

func encodeFuncMapAsSetOf(t reflect.Type, seen encodeFuncCache) encodeFunc {
	key := t.Key()
	typ := TypeOf(key)
	enc := encodeFuncOf(key, seen)

	return func(w Writer, v reflect.Value, flags flags) error {
		n := v.Len()
		if n > math.MaxInt32 {
			return fmt.Errorf("map length is too large to be represented in thrift: %d > max(int32)", n)
		}

		err := w.WriteSet(Set{
			Size: int32(n),
			Type: typ,
		})
		if err != nil {
			return err
		}
		if n == 0 { // empty map
			return nil
		}

		iter := v.MapRange()
		for iter.Next() {
			if err := enc(w, iter.Key(), flags); err != nil {
				return err
			}
		}

		return nil
	}
}

type structEncoder struct {
	fields []structEncoderField
	union  bool
}

func dereference(v reflect.Value) reflect.Value {
	for v.Kind() == reflect.Ptr {
		if v.IsNil() {
			return v
		}
		v = v.Elem()
	}
	return v
}

func isTrue(v reflect.Value) bool {
	v = dereference(v)
	return v.IsValid() && v.Kind() == reflect.Bool && v.Bool()
}

func (enc *structEncoder) encode(w Writer, v reflect.Value, flags flags) error {
	useDeltaEncoding := flags.have(useDeltaEncoding)
	coalesceBoolFields := flags.have(coalesceBoolFields)
	numFields := int16(0)
	lastFieldID := int16(0)

encodeFields:
	for _, f := range enc.fields {
		x := v
		for _, i := range f.index {
			if x.Kind() == reflect.Ptr {
				x = x.Elem()
			}
			if x = x.Field(i); x.Kind() == reflect.Ptr {
				if x.IsNil() {
					continue encodeFields
				}
			}
		}

		if !f.flags.have(required) && x.IsZero() {
			continue encodeFields
		}

		field := Field{
			ID:   f.id,
			Type: f.typ,
		}

		if useDeltaEncoding {
			if delta := field.ID - lastFieldID; delta <= 15 {
				field.ID = delta
				field.Delta = true
			}
		}

		skipValue := coalesceBoolFields && field.Type == BOOL
		if skipValue && isTrue(x) {
			field.Type = TRUE
		}

		if err := w.WriteField(field); err != nil {
			return err
		}

		if !skipValue {
			if err := f.encode(w, x, flags); err != nil {
				return err
			}
		}

		numFields++
		lastFieldID = f.id
	}

	if err := w.WriteField(Field{Type: STOP}); err != nil {
		return err
	}

	if numFields > 1 && enc.union {
		return fmt.Errorf("thrift union had more than one field with a non-zero value (%d)", numFields)
	}

	return nil
}

func (enc *structEncoder) String() string {
	if enc.union {
		return "union"
	}
	return "struct"
}

type structEncoderField struct {
	index  []int
	id     int16
	flags  flags
	typ    Type
	encode encodeFunc
}

func encodeFuncStructOf(t reflect.Type, seen encodeFuncCache) encodeFunc {
	enc := &structEncoder{
		fields: make([]structEncoderField, 0, t.NumField()),
	}
	encode := enc.encode
	seen[t] = encode

	forEachStructField(t, nil, func(f structField) {
		if f.flags.have(union) {
			enc.union = true
		} else {
			enc.fields = append(enc.fields, structEncoderField{
				index:  f.index,
				id:     f.id,
				flags:  f.flags,
				typ:    TypeOf(f.typ),
				encode: encodeFuncStructFieldOf(f, seen),
			})
		}
	})

	sort.SliceStable(enc.fields, func(i, j int) bool {
		return enc.fields[i].id < enc.fields[j].id
	})

	for i := len(enc.fields) - 1; i > 0; i-- {
		if enc.fields[i-1].id == enc.fields[i].id {
			panic(fmt.Errorf("thrift struct field id %d is present multiple times", enc.fields[i].id))
		}
	}

	return encode
}

func encodeFuncStructFieldOf(f structField, seen encodeFuncCache) encodeFunc {
	if f.flags.have(enum) {
		switch f.typ.Kind() {
		case reflect.Int, reflect.Int8, reflect.Int16, reflect.Int32, reflect.Int64:
			return encodeInt32
		}
	}
	return encodeFuncOf(f.typ, seen)
}

func encodeFuncPtrOf(t reflect.Type, seen encodeFuncCache) encodeFunc {
	typ := t.Elem()
	enc := encodeFuncOf(typ, seen)
	zero := reflect.Zero(typ)

	return func(w Writer, v reflect.Value, f flags) error {
		if v.IsNil() {
			v = zero
		} else {
			v = v.Elem()
		}
		return enc(w, v, f)
	}
}
```

## File: `thrift/error.go`
```go
package thrift

import (
	"errors"
	"fmt"
	"io"
	"strings"
)

type MissingField struct {
	Field Field
}

func (e *MissingField) Error() string {
	return fmt.Sprintf("missing required field: %s", e.Field)
}

type TypeMismatch struct {
	Expect Type
	Found  Type
	item   string
}

func (e *TypeMismatch) Error() string {
	return fmt.Sprintf("%s type mismatch: expected %s but found %s", e.item, e.Expect, e.Found)
}

type decodeError struct {
	base error
	path []error
}

func (e *decodeError) Error() string {
	s := strings.Builder{}
	s.Grow(256)
	s.WriteString("decoding thrift payload: ")

	if len(e.path) != 0 {
		n := len(e.path) - 1
		for i := n; i >= 0; i-- {
			if i < n {
				s.WriteString(" → ")
			}
			s.WriteString(e.path[i].Error())
		}
		s.WriteString(": ")
	}

	s.WriteString(e.base.Error())
	return s.String()
}

func (e *decodeError) Unwrap() error { return e.base }

func with(base, elem error) error {
	if errors.Is(base, io.EOF) {
		return base
	}
	e, _ := base.(*decodeError)
	if e == nil {
		e = &decodeError{base: base}
	}
	e.path = append(e.path, elem)
	return e
}

type decodeErrorField struct {
	cause Field
}

func (d *decodeErrorField) Error() string {
	return d.cause.String()
}

type decodeErrorList struct {
	cause List
	index int
}

func (d *decodeErrorList) Error() string {
	return fmt.Sprintf("%d/%d:%s", d.index, d.cause.Size, d.cause)
}

type decodeErrorSet struct {
	cause Set
	index int
}

func (d *decodeErrorSet) Error() string {
	return fmt.Sprintf("%d/%d:%s", d.index, d.cause.Size, d.cause)
}

type decodeErrorMap struct {
	cause Map
	index int
}

func (d *decodeErrorMap) Error() string {
	return fmt.Sprintf("%d/%d:%s", d.index, d.cause.Size, d.cause)
}

func dontExpectEOF(err error) error {
	switch err {
	case nil:
		return nil
	case io.EOF:
		return io.ErrUnexpectedEOF
	default:
		return err
	}
}
```

## File: `thrift/protocol.go`
```go
package thrift

import (
	"io"
)

// Features is a bitset describing the thrift encoding features supported by
// protocol implementations.
type Features uint

const (
	// DeltaEncoding is advertised by protocols that allow encoders to apply
	// delta encoding on struct fields.
	UseDeltaEncoding Features = 1 << iota

	// CoalesceBoolFields is advertised by protocols that allow encoders to
	// coalesce boolean values into field types.
	CoalesceBoolFields
)

// The Protocol interface abstracts the creation of low-level thrift readers and
// writers implementing the various protocols that the encoding supports.
//
// Protocol instances must be safe to use concurrently from multiple gourintes.
// However, the readers and writer that they instantiates are intended to be
// used by a single goroutine.
type Protocol interface {
	NewReader(r io.Reader) Reader
	NewWriter(w io.Writer) Writer
	Features() Features
}

// Reader represents a low-level reader of values encoded according to one of
// the thrift protocols.
type Reader interface {
	Protocol() Protocol
	Reader() io.Reader
	ReadBool() (bool, error)
	ReadInt8() (int8, error)
	ReadInt16() (int16, error)
	ReadInt32() (int32, error)
	ReadInt64() (int64, error)
	ReadFloat64() (float64, error)
	ReadBytes() ([]byte, error)
	ReadString() (string, error)
	ReadLength() (int, error)
	ReadMessage() (Message, error)
	ReadField() (Field, error)
	ReadList() (List, error)
	ReadSet() (Set, error)
	ReadMap() (Map, error)
}

// Writer represents a low-level writer of values encoded according to one of
// the thrift protocols.
type Writer interface {
	Protocol() Protocol
	Writer() io.Writer
	WriteBool(bool) error
	WriteInt8(int8) error
	WriteInt16(int16) error
	WriteInt32(int32) error
	WriteInt64(int64) error
	WriteFloat64(float64) error
	WriteBytes([]byte) error
	WriteString(string) error
	WriteLength(int) error
	WriteMessage(Message) error
	WriteField(Field) error
	WriteList(List) error
	WriteSet(Set) error
	WriteMap(Map) error
}
```

## File: `thrift/protocol_test.go`
```go
package thrift_test

import (
	"bytes"
	"reflect"
	"strings"
	"testing"

	"github.com/segmentio/encoding/thrift"
)

var protocolReadWriteTests = [...]struct {
	scenario string
	read     any
	write    any
	values   []any
}{
	{
		scenario: "bool",
		read:     thrift.Reader.ReadBool,
		write:    thrift.Writer.WriteBool,
		values:   []any{false, true},
	},

	{
		scenario: "int8",
		read:     thrift.Reader.ReadInt8,
		write:    thrift.Writer.WriteInt8,
		values:   []any{int8(0), int8(1), int8(-1)},
	},

	{
		scenario: "int16",
		read:     thrift.Reader.ReadInt16,
		write:    thrift.Writer.WriteInt16,
		values:   []any{int16(0), int16(1), int16(-1)},
	},

	{
		scenario: "int32",
		read:     thrift.Reader.ReadInt32,
		write:    thrift.Writer.WriteInt32,
		values:   []any{int32(0), int32(1), int32(-1)},
	},

	{
		scenario: "int64",
		read:     thrift.Reader.ReadInt64,
		write:    thrift.Writer.WriteInt64,
		values:   []any{int64(0), int64(1), int64(-1)},
	},

	{
		scenario: "float64",
		read:     thrift.Reader.ReadFloat64,
		write:    thrift.Writer.WriteFloat64,
		values:   []any{float64(0), float64(1), float64(-1)},
	},

	{
		scenario: "bytes",
		read:     thrift.Reader.ReadBytes,
		write:    thrift.Writer.WriteBytes,
		values: []any{
			[]byte(""),
			[]byte("A"),
			[]byte("1234567890"),
			bytes.Repeat([]byte("qwertyuiop"), 100),
		},
	},

	{
		scenario: "string",
		read:     thrift.Reader.ReadString,
		write:    thrift.Writer.WriteString,
		values: []any{
			"",
			"A",
			"1234567890",
			strings.Repeat("qwertyuiop", 100),
		},
	},

	{
		scenario: "message",
		read:     thrift.Reader.ReadMessage,
		write:    thrift.Writer.WriteMessage,
		values: []any{
			thrift.Message{},
			thrift.Message{Type: thrift.Call, Name: "Hello", SeqID: 10},
			thrift.Message{Type: thrift.Reply, Name: "World", SeqID: 11},
			thrift.Message{Type: thrift.Exception, Name: "Foo", SeqID: 40},
			thrift.Message{Type: thrift.Oneway, Name: "Bar", SeqID: 42},
		},
	},

	{
		scenario: "field",
		read:     thrift.Reader.ReadField,
		write:    thrift.Writer.WriteField,
		values: []any{
			thrift.Field{ID: 101, Type: thrift.TRUE},
			thrift.Field{ID: 102, Type: thrift.FALSE},
			thrift.Field{ID: 103, Type: thrift.I8},
			thrift.Field{ID: 104, Type: thrift.I16},
			thrift.Field{ID: 105, Type: thrift.I32},
			thrift.Field{ID: 106, Type: thrift.I64},
			thrift.Field{ID: 107, Type: thrift.DOUBLE},
			thrift.Field{ID: 108, Type: thrift.BINARY},
			thrift.Field{ID: 109, Type: thrift.LIST},
			thrift.Field{ID: 110, Type: thrift.SET},
			thrift.Field{ID: 111, Type: thrift.MAP},
			thrift.Field{ID: 112, Type: thrift.STRUCT},
			thrift.Field{},
		},
	},

	{
		scenario: "list",
		read:     thrift.Reader.ReadList,
		write:    thrift.Writer.WriteList,
		values: []any{
			thrift.List{},
			thrift.List{Size: 0, Type: thrift.BOOL},
			thrift.List{Size: 1, Type: thrift.I8},
			thrift.List{Size: 1000, Type: thrift.BINARY},
		},
	},

	{
		scenario: "map",
		read:     thrift.Reader.ReadMap,
		write:    thrift.Writer.WriteMap,
		values: []any{
			thrift.Map{},
			thrift.Map{Size: 1, Key: thrift.BINARY, Value: thrift.MAP},
			thrift.Map{Size: 1000, Key: thrift.BINARY, Value: thrift.LIST},
		},
	},
}

var protocols = [...]struct {
	name  string
	proto thrift.Protocol
}{
	{
		name:  "binary(default)",
		proto: &thrift.BinaryProtocol{},
	},

	{
		name: "binary(non-strict)",
		proto: &thrift.BinaryProtocol{
			NonStrict: true,
		},
	},

	{
		name:  "compact",
		proto: &thrift.CompactProtocol{},
	},
}

func TestProtocols(t *testing.T) {
	for _, test := range protocols {
		t.Run(test.name, func(t *testing.T) { testProtocolReadWriteValues(t, test.proto) })
	}
}

func testProtocolReadWriteValues(t *testing.T, p thrift.Protocol) {
	for _, test := range protocolReadWriteTests {
		t.Run(test.scenario, func(t *testing.T) {
			b := new(bytes.Buffer)
			r := p.NewReader(b)
			w := p.NewWriter(b)

			for _, value := range test.values {
				ret := reflect.ValueOf(test.write).Call([]reflect.Value{
					reflect.ValueOf(w),
					reflect.ValueOf(value),
				})
				if err, _ := ret[0].Interface().(error); err != nil {
					t.Fatal("encoding:", err)
				}
			}

			for _, value := range test.values {
				ret := reflect.ValueOf(test.read).Call([]reflect.Value{
					reflect.ValueOf(r),
				})
				if err, _ := ret[1].Interface().(error); err != nil {
					t.Fatal("decoding:", err)
				}
				if res := ret[0].Interface(); !reflect.DeepEqual(value, res) {
					t.Errorf("value mismatch:\nwant: %#v\ngot:  %#v", value, res)
				}
			}

			if b.Len() != 0 {
				t.Errorf("unexpected trailing bytes: %d", b.Len())
			}
		})
	}
}
```

## File: `thrift/struct.go`
```go
package thrift

import (
	"fmt"
	"reflect"
	"strconv"
	"strings"
)

type flags int16

const (
	enum     flags = 1 << 0
	union    flags = 1 << 1
	required flags = 1 << 2
	optional flags = 1 << 3
	strict   flags = 1 << 4

	featuresBitOffset  = 8
	useDeltaEncoding   = flags(UseDeltaEncoding) << featuresBitOffset
	coalesceBoolFields = flags(CoalesceBoolFields) << featuresBitOffset

	structFlags   flags = enum | union | required | optional
	encodeFlags   flags = strict | protocolFlags
	decodeFlags   flags = strict | protocolFlags
	protocolFlags flags = useDeltaEncoding | coalesceBoolFields
)

func (f flags) have(x flags) bool {
	return (f & x) == x
}

func (f flags) only(x flags) flags {
	return f & x
}

func (f flags) with(x flags) flags {
	return f | x
}

func (f flags) without(x flags) flags {
	return f & ^x
}

type structField struct {
	typ   reflect.Type
	index []int
	id    int16
	flags flags
}

func forEachStructField(t reflect.Type, index []int, do func(structField)) {
	for i := range t.NumField() {
		f := t.Field(i)

		if f.PkgPath != "" && !f.Anonymous { // unexported
			continue
		}

		fieldIndex := append(index, i)
		fieldIndex = fieldIndex[:len(fieldIndex):len(fieldIndex)]

		if f.Anonymous {
			fieldType := f.Type

			for fieldType.Kind() == reflect.Ptr {
				fieldType = fieldType.Elem()
			}

			if fieldType.Kind() == reflect.Struct {
				forEachStructField(fieldType, fieldIndex, do)
				continue
			}
		}

		tag := f.Tag.Get("thrift")
		if tag == "" {
			continue
		}
		tags := strings.Split(tag, ",")
		flags := flags(0)

		for _, opt := range tags[1:] {
			switch opt {
			case "enum":
				flags = flags.with(enum)
			case "union":
				flags = flags.with(union)
			case "required":
				flags = flags.with(required)
			case "optional":
				flags = flags.with(optional)
			default:
				panic(fmt.Errorf("thrift struct field contains an unknown tag option %q in `thrift:\"%s\"`", opt, tag))
			}
		}

		if flags.have(optional | required) {
			panic(fmt.Errorf("thrift struct field cannot be both optional and required in `thrift:\"%s\"`", tag))
		}

		if flags.have(union) {
			if f.Type.Kind() != reflect.Interface {
				panic(fmt.Errorf("thrift union tag found on a field which is not an interface type `thrift:\"%s\"`", tag))
			}

			if tags[0] != "" {
				panic(fmt.Errorf("invalid thrift field id on union field `thrift:\"%s\"`", tag))
			}

			do(structField{
				typ:   f.Type,
				index: fieldIndex,
				flags: flags,
			})
		} else {
			if flags.have(enum) {
				switch f.Type.Kind() {
				case reflect.Int, reflect.Int8, reflect.Int16, reflect.Int32, reflect.Int64:
				case reflect.Uint, reflect.Uint8, reflect.Uint16, reflect.Uint32, reflect.Uint64, reflect.Uintptr:
				default:
					panic(fmt.Errorf("thrift enum tag found on a field which is not an integer type `thrift:\"%s\"`", tag))
				}
			}

			if id, err := strconv.ParseInt(tags[0], 10, 16); err != nil {
				panic(fmt.Errorf("invalid thrift field id found in struct tag `thrift:\"%s\"`: %w", tag, err))
			} else if id <= 0 {
				panic(fmt.Errorf("invalid thrift field id found in struct tag `thrift:\"%s\"`: %d <= 0", tag, id))
			} else {
				do(structField{
					typ:   f.Type,
					index: fieldIndex,
					id:    int16(id),
					flags: flags,
				})
			}
		}
	}
}
```

## File: `thrift/thrift.go`
```go
package thrift

import (
	"fmt"
	"reflect"
)

type Message struct {
	Type  MessageType
	Name  string
	SeqID int32
}

type MessageType int8

const (
	Call MessageType = iota
	Reply
	Exception
	Oneway
)

func (m MessageType) String() string {
	switch m {
	case Call:
		return "Call"
	case Reply:
		return "Reply"
	case Exception:
		return "Exception"
	case Oneway:
		return "Oneway"
	default:
		return "?"
	}
}

type Field struct {
	ID    int16
	Type  Type
	Delta bool // whether the field id is a delta
}

func (f Field) String() string {
	return fmt.Sprintf("%d:FIELD<%s>", f.ID, f.Type)
}

type Type int8

const (
	STOP Type = iota
	TRUE
	FALSE
	I8
	I16
	I32
	I64
	DOUBLE
	BINARY
	LIST
	SET
	MAP
	STRUCT
	BOOL = FALSE
)

func (t Type) String() string {
	switch t {
	case STOP:
		return "STOP"
	case TRUE:
		return "TRUE"
	case BOOL:
		return "BOOL"
	case I8:
		return "I8"
	case I16:
		return "I16"
	case I32:
		return "I32"
	case I64:
		return "I64"
	case DOUBLE:
		return "DOUBLE"
	case BINARY:
		return "BINARY"
	case LIST:
		return "LIST"
	case SET:
		return "SET"
	case MAP:
		return "MAP"
	case STRUCT:
		return "STRUCT"
	default:
		return "?"
	}
}

func (t Type) GoString() string {
	return "thrift." + t.String()
}

type List struct {
	Size int32
	Type Type
}

func (l List) String() string {
	return fmt.Sprintf("LIST<%s>", l.Type)
}

type Set List

func (s Set) String() string {
	return fmt.Sprintf("SET<%s>", s.Type)
}

type Map struct {
	Size  int32
	Key   Type
	Value Type
}

func (m Map) String() string {
	return fmt.Sprintf("MAP<%s,%s>", m.Key, m.Value)
}

func TypeOf(t reflect.Type) Type {
	switch t.Kind() {
	case reflect.Bool:
		return BOOL
	case reflect.Int8, reflect.Uint8:
		return I8
	case reflect.Int16, reflect.Uint16:
		return I16
	case reflect.Int32, reflect.Uint32:
		return I32
	case reflect.Int64, reflect.Uint64, reflect.Int, reflect.Uint, reflect.Uintptr:
		return I64
	case reflect.Float32, reflect.Float64:
		return DOUBLE
	case reflect.String:
		return BINARY
	case reflect.Slice:
		if t.Elem().Kind() == reflect.Uint8 { // []byte
			return BINARY
		} else {
			return LIST
		}
	case reflect.Map:
		if t.Elem().Size() == 0 {
			return SET
		} else {
			return MAP
		}
	case reflect.Struct:
		return STRUCT
	case reflect.Ptr:
		return TypeOf(t.Elem())
	default:
		panic("type cannot be represented in thrift: " + t.String())
	}
}
```

## File: `thrift/thrift_test.go`
```go
package thrift_test

import (
	"bytes"
	"math"
	"reflect"
	"strings"
	"testing"

	"github.com/segmentio/encoding/thrift"
)

var marshalTestValues = [...]struct {
	scenario string
	values   []any
}{
	{
		scenario: "bool",
		values:   []any{false, true},
	},

	{
		scenario: "int",
		values: []any{
			int(0),
			int(-1),
			int(1),
		},
	},

	{
		scenario: "int8",
		values: []any{
			int8(0),
			int8(-1),
			int8(1),
			int8(math.MinInt8),
			int8(math.MaxInt8),
		},
	},

	{
		scenario: "int16",
		values: []any{
			int16(0),
			int16(-1),
			int16(1),
			int16(math.MinInt16),
			int16(math.MaxInt16),
		},
	},

	{
		scenario: "int32",
		values: []any{
			int32(0),
			int32(-1),
			int32(1),
			int32(math.MinInt32),
			int32(math.MaxInt32),
		},
	},

	{
		scenario: "int64",
		values: []any{
			int64(0),
			int64(-1),
			int64(1),
			int64(math.MinInt64),
			int64(math.MaxInt64),
		},
	},

	{
		scenario: "string",
		values: []any{
			"",
			"A",
			"1234567890",
			strings.Repeat("qwertyuiop", 100),
		},
	},

	{
		scenario: "[]byte",
		values: []any{
			[]byte(""),
			[]byte("A"),
			[]byte("1234567890"),
			bytes.Repeat([]byte("qwertyuiop"), 100),
		},
	},

	{
		scenario: "[]string",
		values: []any{
			[]string{},
			[]string{"A"},
			[]string{"hello", "world", "!!!"},
			[]string{"0", "1", "3", "4", "5", "6", "7", "8", "9"},
		},
	},

	{
		scenario: "map[string]int",
		values: []any{
			map[string]int{},
			map[string]int{"A": 1},
			map[string]int{"hello": 1, "world": 2, "answer": 42},
		},
	},

	{
		scenario: "map[int64]struct{}",
		values: []any{
			map[int64]struct{}{},
			map[int64]struct{}{0: {}, 1: {}, 2: {}},
		},
	},

	{
		scenario: "[]map[string]struct{}",
		values: []any{
			[]map[string]struct{}{},
			[]map[string]struct{}{{}, {"A": {}, "B": {}, "C": {}}},
		},
	},

	{
		scenario: "struct{}",
		values:   []any{struct{}{}},
	},

	{
		scenario: "Point2D",
		values: []any{
			Point2D{},
			Point2D{X: 1},
			Point2D{Y: 2},
			Point2D{X: 3, Y: 4},
		},
	},

	{
		scenario: "RecursiveStruct",
		values: []any{
			RecursiveStruct{},
			RecursiveStruct{Value: "hello"},
			RecursiveStruct{Value: "hello", Next: &RecursiveStruct{}},
			RecursiveStruct{Value: "hello", Next: &RecursiveStruct{Value: "world", Test: newBool(true)}},
		},
	},

	{
		scenario: "StructWithEnum",
		values: []any{
			StructWithEnum{},
			StructWithEnum{Enum: 1},
			StructWithEnum{Enum: 2},
		},
	},

	{
		scenario: "StructWithPointToPointerToBool",
		values: []any{
			StructWithPointerToPointerToBool{
				Test: newBoolPtr(true),
			},
		},
	},

	{
		scenario: "StructWithEmbeddedStrutPointerWithPointerToPointer",
		values: []any{
			StructWithEmbeddedStrutPointerWithPointerToPointer{
				StructWithPointerToPointerToBool: &StructWithPointerToPointerToBool{
					Test: newBoolPtr(true),
				},
			},
		},
	},

	{
		scenario: "Union",
		values: []any{
			Union{},
			Union{A: true, F: newBool(true)},
			Union{B: 42, F: newInt(42)},
			Union{C: "hello world!", F: newString("hello world!")},
		},
	},
}

type Point2D struct {
	X float64 `thrift:"1,required"`
	Y float64 `thrift:"2,required"`
}

type RecursiveStruct struct {
	Value string           `thrift:"1"`
	Next  *RecursiveStruct `thrift:"2"`
	Test  *bool            `thrift:"3"`
}

type StructWithEnum struct {
	Enum int8 `thrift:"1,enum"`
}

type StructWithPointerToPointerToBool struct {
	Test **bool `thrift:"1"`
}

type StructWithEmbeddedStrutPointerWithPointerToPointer struct {
	*StructWithPointerToPointerToBool
}

type Union struct {
	A bool   `thrift:"1"`
	B int    `thrift:"2"`
	C string `thrift:"3"`
	F any    `thrift:",union"`
}

func newBool(b bool) *bool       { return &b }
func newInt(i int) *int          { return &i }
func newString(s string) *string { return &s }

func newBoolPtr(b bool) **bool {
	p := newBool(b)
	return &p
}

func TestMarshalUnmarshal(t *testing.T) {
	for _, p := range protocols {
		t.Run(p.name, func(t *testing.T) { testMarshalUnmarshal(t, p.proto) })
	}
}

func testMarshalUnmarshal(t *testing.T, p thrift.Protocol) {
	for _, test := range marshalTestValues {
		t.Run(test.scenario, func(t *testing.T) {
			for _, value := range test.values {
				b, err := thrift.Marshal(p, value)
				if err != nil {
					t.Fatal("marshal:", err)
				}

				v := reflect.New(reflect.TypeOf(value))
				if err := thrift.Unmarshal(p, b, v.Interface()); err != nil {
					t.Fatal("unmarshal:", err)
				}

				if result := v.Elem().Interface(); !reflect.DeepEqual(value, result) {
					t.Errorf("value mismatch:\nwant: %#v\ngot:  %#v", value, result)
				}
			}
		})
	}
}

func BenchmarkMarshal(b *testing.B) {
	for _, p := range protocols {
		b.Run(p.name, func(b *testing.B) { benchmarkMarshal(b, p.proto) })
	}
}

type BenchmarkEncodeType struct {
	Name     string               `thrift:"1"`
	Question string               `thrift:"2"`
	Answer   string               `thrift:"3"`
	Sub      *BenchmarkEncodeType `thrift:"4"`
}

func benchmarkMarshal(b *testing.B, p thrift.Protocol) {
	buf := new(bytes.Buffer)
	enc := thrift.NewEncoder(p.NewWriter(buf))
	val := &BenchmarkEncodeType{
		Name:     "Luke",
		Question: "How are you?",
		Answer:   "42",
		Sub: &BenchmarkEncodeType{
			Name:     "Leia",
			Question: "?",
			Answer:   "whatever",
		},
	}

	for range b.N {
		buf.Reset()
		enc.Encode(val)
	}

	b.SetBytes(int64(buf.Len()))
}

func BenchmarkUnmarshal(b *testing.B) {
	for _, p := range protocols {
		b.Run(p.name, func(b *testing.B) { benchmarkUnmarshal(b, p.proto) })
	}
}

type BenchmarkDecodeType struct {
	Name     string               `thrift:"1"`
	Question string               `thrift:"2"`
	Answer   string               `thrift:"3"`
	Sub      *BenchmarkDecodeType `thrift:"4"`
}

func benchmarkUnmarshal(b *testing.B, p thrift.Protocol) {
	buf, _ := thrift.Marshal(p, &BenchmarkDecodeType{
		Name:     "Luke",
		Question: "How are you?",
		Answer:   "42",
		Sub: &BenchmarkDecodeType{
			Name:     "Leia",
			Question: "?",
			Answer:   "whatever",
		},
	})

	rb := bytes.NewReader(nil)
	dec := thrift.NewDecoder(p.NewReader(rb))
	val := &BenchmarkDecodeType{}

	for range b.N {
		rb.Reset(buf)
		dec.Decode(val)
	}

	b.SetBytes(int64(len(buf)))
}
```

## File: `thrift/unsafe.go`
```go
package thrift

import (
	"reflect"
	"unsafe"
)

// typeID is used as key in encoder and decoder caches to enable using
// the optimize runtime.mapaccess2_fast64 function instead of the more
// expensive lookup if we were to use reflect.Type as map key.
//
// typeID holds the pointer to the reflect.Type value, which is unique
// in the program.
type typeID struct{ ptr unsafe.Pointer }

func makeTypeID(t reflect.Type) typeID {
	return typeID{
		ptr: (*[2]unsafe.Pointer)(unsafe.Pointer(&t))[1],
	}
}

func unsafeBytesToString(b []byte) string {
	return *(*string)(unsafe.Pointer(&b))
}
```

