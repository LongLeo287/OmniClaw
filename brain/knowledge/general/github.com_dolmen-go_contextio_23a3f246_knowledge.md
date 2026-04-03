---
id: github.com-dolmen-go-contextio-23a3f246-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:45.163374
---

# KNOWLEDGE EXTRACT: github.com_dolmen-go_contextio_23a3f246
> **Extracted on:** 2026-04-01 13:19:50
> **Source:** D:/LongLeo/AI OS CORP/AI OS/core/security/QUARANTINE/KI-BATCH-20260331205007522360/github.com_dolmen-go_contextio_23a3f246

---

## File: `.travis.yml`
```yaml
---
language: go
go:
- 1.16.x
- tip
- 1.15.x
- 1.14.x
- 1.13.x
- 1.12.x
- 1.11.x
- 1.10.x
- 1.9.x
- 1.8.x
- 1.7.x
sudo: false

go_import_path: github.com/dolmen-go/contextio

before_install:
- go get -t -v ./...

script:
- go test -coverprofile=coverage.txt -covermode=atomic

after_success:
- bash <(curl -s https://codecov.io/bash)
```

## File: `LICENSE`
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
      boilerplate notice, with the fields enclosed by brackets "[]"
      replaced with your own identifying information. (Don't include
      the brackets!)  The text should be enclosed in the appropriate
      comment syntax for the file format. We also recommend that a
      file or class name and description of purpose be included on the
      same "printed page" as the copyright notice for easier
      identification within third-party archives.

   Copyright [yyyy] [name of copyright owner]

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

## File: `Makefile`
```


go ?= GO111MODULE=on go
export go

tag_prefix :=
go_files = go.mod $(shell $(go) list -f '{{$$Dir := .Dir}}{{range .GoFiles}}{{$$Dir}}/{{.}} {{end}}' ./...)
go_files_last_commit = $(shell git log -1 --format=%H -- $(go_files))

## Show module version as expected by the Go toolchain
go-version: $(go_files)
	@{ git describe --tags --match '$(tag_prefix)v*.*.*' --exact-match 2>/dev/null $(shell git log -1 --format=%H -- $^ ) || TZ=UTC git log -1 '--date=format-local:%Y%m%d%H%M%S' --abbrev=12 '--pretty=tformat:%(describe:tags,match=$(tag_prefix)v*,abbrev=0)-0-%cd-%h' $^ | perl -pE 's/(\d+)(?=-)/$$1+1/e' ; } | sed -e 's!.*/!!'

go-get:
	@echo $(go) get $(shell $(go) list .)@$(shell $(MAKE) -f $(firstword $(MAKEFILE_LIST)) go-version)

```

## File: `README.md`
```markdown
# contextio - Context-aware I/O streams for Go

[![GoDoc](https://img.shields.io/badge/godoc-reference-blue.svg)](https://godoc.org/github.com/dolmen-go/contextio)
[![stability: stable](https://img.shields.io/badge/stability-stable-green.svg)](https://github.com/emersion/stability-badges#stable)
[![codecov](https://codecov.io/gh/dolmen-go/contextio/branch/master/graph/badge.svg)](https://codecov.io/gh/dolmen-go/contextio)
[![Travis-CI](https://api.travis-ci.org/dolmen-go/contextio.svg?branch=master)](https://travis-ci.org/dolmen-go/contextio)
[![Go Report Card](https://goreportcard.com/badge/github.com/dolmen-go/contextio)](https://goreportcard.com/report/github.com/dolmen-go/contextio)

Author: [@dolmen](https://github.com/dolmen)  (Olivier Mengué).

# Example

`go test -run ExampleWriter`

```go
func main() {
	// interrupt context after 500ms
	ctx, cancel := context.WithTimeout(context.Background(), 500*time.Millisecond)
	defer cancel()
	// interrupt context with SIGTERM (CTRL+C)
	sigs := make(chan os.Signal, 1)
	signal.Notify(sigs, os.Interrupt)
	go func() {
		<-sigs
		cancel()
	}()

	f, err := os.OpenFile(os.DevNull, os.O_WRONLY, 0)
	if err != nil {
		log.Fatal(err)
	}
	defer f.Close()

	// Writer that fails when context is canceled
	out := contextio.NewWriter(ctx, f)

	// Infinite loop. Will only be interrupted once write fails.
	for {
		if _, err := out.Write([]byte{'a', 'b', 'c'}); err != nil {
			fmt.Println("Err:", err)
			break
		}
	}

	fmt.Println("Closing.")
}
```

# See Also

* [github.com/jbenet/go-context/io](https://godoc.org/github.com/jbenet/go-context/io) Context-aware reader and writer
* [github.com/northbright/ctx/ctxcopy](https://godoc.org/github.com/northbright/ctx/ctxcopy) Context-aware io.Copy
* [gitlab.com/streamy/concon](https://godoc.org/gitlab.com/streamy/concon) Context-aware net.Conn
```

## File: `example_test.go`
```go
package contextio_test

import (
	"context"
	"fmt"
	"io"
	"log"
	"os"
	"os/signal"
	"time"

	"github.com/dolmen-go/contextio"
)

func Example_copy() {
	// interrupt context after 500ms
	ctx, cancel := context.WithTimeout(context.Background(), 500*time.Millisecond)
	defer cancel()
	// interrupt context with SIGTERM (CTRL+C)
	sigs := make(chan os.Signal, 1)
	signal.Notify(sigs, os.Interrupt)
	go func() {
		<-sigs
		cancel()
	}()

	fIn, err := os.Open("/dev/zero")
	if err != nil {
		log.Fatal(err)
	}
	defer fIn.Close()

	fOut, err := os.OpenFile(os.DevNull, os.O_WRONLY, 0)
	if err != nil {
		log.Fatal(err)
	}
	defer fOut.Close()

	// Reader that fails when context is canceled
	in := contextio.NewReader(ctx, fIn)
	// Writer that fails when context is canceled
	out := contextio.NewWriter(ctx, fOut)

	n, err := io.Copy(out, in)
	log.Println(n, "bytes copied.")
	if err != nil {
		fmt.Println("Err:", err)
	}

	fmt.Println("Closing.")

	// Output:
	// Err: context deadline exceeded
	// Closing.
}

func ExampleNewWriter() {
	// interrupt context after 500ms
	ctx, cancel := context.WithTimeout(context.Background(), 500*time.Millisecond)
	defer cancel()
	// interrupt context with SIGTERM (CTRL+C)
	sigs := make(chan os.Signal, 1)
	signal.Notify(sigs, os.Interrupt)
	go func() {
		<-sigs
		cancel()
	}()

	f, err := os.OpenFile(os.DevNull, os.O_WRONLY, 0)
	if err != nil {
		log.Fatal(err)
	}
	defer f.Close()

	// Writer that fails when context is canceled
	out := contextio.NewWriter(ctx, f)

	// Infinite loop. Will only be interrupted once write fails.
	for {
		if _, err := out.Write([]byte{'a', 'b', 'c'}); err != nil {
			fmt.Println("Err:", err)
			break
		}
	}

	fmt.Println("Closing.")

	// Output:
	// Err: context deadline exceeded
	// Closing.
}
```

## File: `go.mod`
```
module github.com/dolmen-go/contextio

go 1.12
```

## File: `io.go`
```go
/*
Copyright 2018 Olivier Mengué

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
*/

// Package contextio provides [io.Writer] and [io.Reader] that stop accepting/providing
// data when an attached context is canceled.
package contextio

import (
	"context"
	"io"
)

type writer struct {
	ctx context.Context
	w   io.Writer
}

type copier struct {
	writer
}

// NewWriter wraps an [io.Writer] to handle context cancellation.
//
// Context state is checked BEFORE every Write.
//
// The returned Writer also implements [io.ReaderFrom] to allow [io.Copy] to select
// the best strategy while still checking the context state before every chunk transfer.
func NewWriter(ctx context.Context, w io.Writer) io.Writer {
	if w, ok := w.(*copier); ok && ctx == w.ctx {
		return w
	}
	return &copier{writer{ctx: ctx, w: w}}
}

// Write implements [io.Writer], but with context awareness.
func (w *writer) Write(p []byte) (n int, err error) {
	select {
	case <-w.ctx.Done():
		return 0, w.ctx.Err()
	default:
		return w.w.Write(p)
	}
}

type reader struct {
	ctx context.Context
	r   io.Reader
}

// NewReader wraps an [io.Reader] to handle context cancellation.
//
// Context state is checked BEFORE every Read.
func NewReader(ctx context.Context, r io.Reader) io.Reader {
	if r, ok := r.(*reader); ok && ctx == r.ctx {
		return r
	}
	return &reader{ctx: ctx, r: r}
}

func (r *reader) Read(p []byte) (n int, err error) {
	select {
	case <-r.ctx.Done():
		return 0, r.ctx.Err()
	default:
		return r.r.Read(p)
	}
}

// ReadFrom implements interface [io.ReaderFrom], but with context awareness.
//
// This should allow efficient copying allowing writer or reader to define the chunk size.
func (w *copier) ReadFrom(r io.Reader) (n int64, err error) {
	if _, ok := w.w.(io.ReaderFrom); ok {
		// Let the original Writer decide the chunk size.
		return io.Copy(w.writer.w, &reader{ctx: w.ctx, r: r})
	}
	select {
	case <-w.ctx.Done():
		return 0, w.ctx.Err()
	default:
		// The original Writer is not a ReaderFrom.
		// Let the Reader decide the chunk size.
		return io.Copy(&w.writer, r)
	}
}

// NewCloser wraps an [io.Reader] to handle context cancellation.
//
// Context state is checked BEFORE any Close.
func NewCloser(ctx context.Context, c io.Closer) io.Closer {
	return &closer{ctx: ctx, c: c}
}

type closer struct {
	ctx context.Context
	c   io.Closer
}

func (c *closer) Close() error {
	select {
	case <-c.ctx.Done():
		return c.ctx.Err()
	default:
		return c.c.Close()
	}
}
```

## File: `io_test.go`
```go
package contextio_test

import (
	"bytes"
	"context"
	"testing"

	"github.com/dolmen-go/contextio"
)

func TestWriter(t *testing.T) {
	var buf bytes.Buffer
	w := contextio.NewWriter(context.Background(), &buf)
	n, err := w.Write([]byte("hello"))
	if err != nil {
		t.Fatal(err)
	}
	if n != 5 {
		t.Fatal("5 bytes written expected")
	}
	if buf.String() != "hello" {
		t.Fatal("Bad content")
	}

	buf.Reset()

	ctx, cancel := context.WithCancel(context.Background())
	defer cancel()
	w = contextio.NewWriter(ctx, &buf)
	n, err = w.Write([]byte("hello"))
	if err != nil {
		t.Fatal(err)
	}
	if n != 5 {
		t.Fatal("5 bytes written expected")
	}
	if buf.String() != "hello" {
		t.Fatal("Bad content")
	}

	cancel()

	n, err = w.Write([]byte(", world"))
	if err != context.Canceled {
		t.Fatal(err)
	}
	if n != 0 {
		t.Fatal("0 bytes written expected")
	}
	if buf.String() != "hello" {
		t.Fatal("Bad content")
	}
}
```

