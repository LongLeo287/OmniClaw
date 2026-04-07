---
id: contextio
type: knowledge
owner: OA_Triage
---
# contextio
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
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

### File: example_test.go
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

### File: io.go
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

### File: io_test.go
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

