---
id: neilotoole-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:29:11.193755
---

# KNOWLEDGE EXTRACT: neilotoole
> **Extracted on:** 2026-03-30 17:49:10
> **Source:** neilotoole

---

## File: `jsoncolor.md`
```markdown
# 📦 neilotoole/jsoncolor [🔖 PENDING/APPROVE]
🔗 https://github.com/neilotoole/jsoncolor


## Meta
- **Stars:** ⭐ 51 | **Forks:** 🍴 6
- **Language:** Go | **License:** MIT
- **Last updated:** 2026-03-04
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Colorized JSON output for Go

## README (trích đầu)
```
[![Actions Status](https://github.com/neilotoole/jsoncolor/workflows/Go/badge.svg)](https://github.com/neilotoole/jsoncolor/actions?query=workflow%3AGo)
[![Go Report Card](https://goreportcard.com/badge/neilotoole/jsoncolor)](https://goreportcard.com/report/neilotoole/jsoncolor)
[![release](https://img.shields.io/badge/release-v0.7.0-green.svg)](https://github.com/neilotoole/jsoncolor/releases/tag/v0.7.0)
[![Go Reference](https://pkg.go.dev/badge/github.com/neilotoole/jsoncolor.svg)](https://pkg.go.dev/github.com/neilotoole/jsoncolor)
[![license](https://img.shields.io/github/license/neilotoole/jsoncolor)](./LICENSE)

# jsoncolor

Package `neilotoole/jsoncolor` is a drop-in replacement for stdlib
[`encoding/json`](https://pkg.go.dev/encoding/json) that outputs colorized JSON.

Why? Well, [`jq`](https://jqlang.github.io/jq/) colorizes its output by default, and color output
is desirable for many Go CLIs. This package performs colorization (and indentation) inline
in the encoder, and is significantly faster than stdlib at indentation.

From the example [`jc`](./cmd/jc/main.go) app:

![jsoncolor-output](./splash.png)

## Usage

Get the package per the normal mechanism (requires Go 1.17+):

```shell
go get -u github.com/neilotoole/jsoncolor
```

Then:

```go
package main

import (
  "fmt"
  "github.com/mattn/go-colorable"
  json "github.com/neilotoole/jsoncolor"
  "os"
)

func main() {
  var enc *json.Encoder

  // Note: this check will fail if running inside Goland (and
  // other IDEs?) as IsColorTerminal will return false.
  if json.IsColorTerminal(os.Stdout) {
    // Safe to use color
    out := colorable.NewColorable(os.Stdout) // needed for Windows
    enc = json.NewEncoder(out)

    // DefaultColors are similar to jq
    clrs := json.DefaultColors()

    // Change some values, just for fun
    clrs.Bool = json.Color("\x1b[36m") // Change the bool color
    clrs.String = json.Color{}         // Disable the string color

    enc.SetColors(clrs)
  } else {
    // Can't use color; but the encoder will still work
    enc = json.NewEncoder(os.Stdout)
  }

  m := map[string]interface{}{
    "a": 1,
    "b": true,
    "c": "hello",
  }

  if err := enc.Encode(m); err != nil {
    fmt.Fprintln(os.Stderr, err)
    os.Exit(1)
  }
}
```

### Configuration

To enable colorization, invoke [`enc.SetColors`](https://pkg.go.dev/github.com/neilotoole/jsoncolor#Encoder.SetColors).

The [`Colors`](https://pkg.go.dev/github.com/neilotoole/jsoncolor#Colors) struct
holds color config. The zero value and `nil` are both safe for use (resulting in no colorization).

The [`DefaultColors`](https://pkg.go.dev/github.com/neilotoole/jsoncolor#DefaultColors) func
returns a `Colors` struct that produces results similar to `jq`:

```go
// DefaultColors returns the default Colors configuration.
// These colors largely follow jq's default colorization,
// with some deviation.
func DefaultColors() *Colors {
  return &Colors{
    Null:   Color("\x1b[2m"),
    Bool:   Color("\x1b[1
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `oncecache.md`
```markdown
# 📦 neilotoole/oncecache [🔖 PENDING/APPROVE]
🔗 https://github.com/neilotoole/oncecache


## Meta
- **Stars:** ⭐ 3 | **Forks:** 🍴 0
- **Language:** Go | **License:** MIT
- **Last updated:** 2024-11-04
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Go on-demand in-memory object cache

## README (trích đầu)
```
# oncecache: on-demand in-memory object cache

[![Go Reference](https://pkg.go.dev/badge/github.com/neilotoole/oncecache.svg)](https://pkg.go.dev/github.com/neilotoole/oncecache)
[![Go Report Card](https://goreportcard.com/badge/neilotoole/oncecache)](https://goreportcard.com/report/neilotoole/oncecache)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/neilotoole/oncecache/blob/master/LICENSE)
![Workflow](https://github.com/neilotoole/oncecache/actions/workflows/go.yml/badge.svg)

`oncecache` is a strongly-typed, concurrency-safe, context-aware,
dependency-free, in-memory, on-demand Golang object cache, focused on write-once,
read-often ergonomics.

The package also provides an event mechanism useful for logging, metrics, or
propagating cache entries between overlapping composite caches.

`oncecache` is targeted at write-once, read-often situations, where a value
corresponding to a key is expensive to compute or fetch, the value is likely to be read
multiple times, and is not expected to change. The cache is not intended for general purpose
caching where values are frequently updated.


## Install

Add to your `go.mod` via `go get`:

```shell
go get github.com/neilotoole/oncecache
```

## Usage

The basic theory of operation is that a [`oncecache.Cache`](https://pkg.go.dev/github.com/neilotoole/oncecache#Cache) is created with a
function that returns the value corresponding to a key. When a key is requested
from the cache, the cache checks if the value is already present. If not, the
cache calls the provided function to compute the value, stores the value, and
returns it. Subsequent requests for the same key return the cached value.

Here's a trivial example that caches computed fibonacci numbers:

```go
func ExampleFibonacci() {
	// Ignore error handling for brevity.
	ctx := context.Background()
	c := oncecache.New[int, int](calcFibonacci)

	key := 6
	val, _ := c.Get(ctx, key) // Cache MISS - calcFibonacci(6) is invoked
	fmt.Println(key, val)
	val, _ = c.Get(ctx, key) // Cache HIT
	fmt.Println(key, val)

	key = 9
	val, _ = c.Get(ctx, key) // Cache MISS - calcFibonacci(9) is invoked
	fmt.Println(key, val)

	// Output:
	// 6 8
	// 6 8
	// 9 34
}

func calcFibonacci(ctx context.Context, n int) (val int, err error) {
	a, b, temp := 0, 1, 0 //nolint:wastedassign
	for i := 0; i < n && ctx.Err() == nil; i++ {
		temp = a
		a = b
		b = temp + a
	}

	if ctx.Err() != nil {
		return 0, ctx.Err()
	}

	return a, nil
}
```

`oncecache.Cache` provides typical operations to interact with the cache, such as
[`Delete`](https://pkg.go.dev/github.com/neilotoole/oncecache#Cache.Delete),
[`Has`](https://pkg.go.dev/github.com/neilotoole/oncecache#Cache.Has),
[`Keys`](https://pkg.go.dev/github.com/neilotoole/oncecache#Cache.Keys), etc.

```go
func ExampleOperations() {
	// Ignore error handling for brevity.
	ctx := context.Background()
	c := oncecache.New[int, int](calcFibonacci)

	for key := 4; key < 7; key++ {
		val, _ := c.Get(ctx, k
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `sq.md`
```markdown
# 📦 neilotoole/sq [🔖 PENDING/APPROVE]
🔗 https://github.com/neilotoole/sq
🌐 https://sq.io

## Meta
- **Stars:** ⭐ 2456 | **Forks:** 🍴 38
- **Language:** Go | **License:** MIT
- **Last updated:** 2026-03-24
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
sq data wrangler

## README (trích đầu)
```
[![Go Reference](https://pkg.go.dev/badge/github.com/neilotoole/sq.svg)](https://pkg.go.dev/github.com/neilotoole/sq)
[![Go Report Card](https://goreportcard.com/badge/neilotoole/sq)](https://goreportcard.com/report/neilotoole/sq)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/neilotoole/sq/blob/master/LICENSE)
![Main pipeline](https://github.com/neilotoole/sq/actions/workflows/main.yml/badge.svg)

# sq data wrangler

`sq` is a command line tool that provides jq-style access to
structured data sources: SQL databases, or document formats like CSV or Excel.
It is the lovechild of sql+jq.

![sq](.images/splash.png)

`sq` executes jq-like [queries](https://sq.io/docs/query), or database-native [SQL](https://sq.io/docs/cmd/sql/).
It can [join](https://sq.io/docs/query#cross-source-joins) across sources: join a CSV file to a Postgres table, or
MySQL with Excel.

`sq` outputs to a multitude of [formats](https://sq.io/docs/output#formats)
including [JSON](https://sq.io/docs/output#json),
[Excel](https://sq.io/docs/output#xlsx), [CSV](https://sq.io/docs/output#csv),
[HTML](https://sq.io/docs/output#html), [Markdown](https://sq.io/docs/output#markdown)
and [XML](https://sq.io/docs/output#xml), and can [insert](https://sq.io/docs/output#insert) query
results directly to a SQL database.

`sq` can also [inspect](https://sq.io/docs/inspect) sources to view metadata about the source structure (tables,
columns, size). You can use [`sq diff`](https://sq.io/docs/diff) to compare tables, or
entire databases. `sq` has commands for common database operations to
[copy](https://sq.io/docs/cmd/tbl-copy), [truncate](https://sq.io/docs/cmd/tbl-truncate),
and [drop](https://sq.io/docs/cmd/tbl-drop) tables.

Find out more at [sq.io](https://sq.io).

> [!TIP]
> The rest of this doc is mainly for `sq` end users and first-timers. Contributors (bug reports, feature requests, pull requests),
> see [CONTRIBUTING.md](./CONTRIBUTING.md).

## Drivers

`sq` knows how to deal with a data source type via a [driver](https://sq.io/docs/drivers)
implementation. To view the installed/supported drivers:

```shell
$ sq driver ls
DRIVER      DESCRIPTION
sqlite3     SQLite
postgres    PostgreSQL
sqlserver   Microsoft SQL Server / Azure SQL Edge
mysql       MySQL
clickhouse  ClickHouse
csv         Comma-Separated Values
tsv         Tab-Separated Values
json        JSON
jsona       JSON Array: LF-delimited JSON arrays
jsonl       JSON Lines: LF-delimited JSON objects
xlsx        Microsoft Excel XLSX
```

> [!NOTE]
> ClickHouse Driver support is currently in beta. Full details of support can be
> found in the [ClickHouse README](../../../README.md).

## Install

### macOS

```shell
brew install sq
```

> [!IMPORTANT]
> `sq` is now a [core brew formula](https://formulae.brew.sh/formula/sq#default). Previously, `sq` was available via `brew install neilotoole/sq/sq`. If you have installed `sq` this way, you should uninstall it (`brew uninstall neilotoole
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `streamcache.md`
```markdown
# 📦 neilotoole/streamcache [🔖 PENDING/APPROVE]
🔗 https://github.com/neilotoole/streamcache


## Meta
- **Stars:** ⭐ 35 | **Forks:** 🍴 0
- **Language:** Go | **License:** MIT
- **Last updated:** 2025-04-06
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Golang in-memory caching stream reader

## README (trích đầu)
```
# streamcache: in-memory caching stream reader

[![Go Reference](https://pkg.go.dev/badge/github.com/neilotoole/streamcache.svg)](https://pkg.go.dev/github.com/neilotoole/streamcache)
[![Go Report Card](https://goreportcard.com/badge/neilotoole/streamcache)](https://goreportcard.com/report/neilotoole/streamcache)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/neilotoole/streamcache/blob/master/LICENSE)
![Workflow](https://github.com/neilotoole/streamcache/actions/workflows/go.yml/badge.svg)


Package [`streamcache`](https://pkg.go.dev/github.com/neilotoole/streamcache)
implements a Go in-memory byte cache mechanism that allows multiple callers to
read some or all of the contents of a source `io.Reader`, while only reading
from the source reader once. When only the final reader remains, the cache is
discarded and the final reader reads directly from the source. This is particularly
useful for scenarios where multiple readers may wish to sample the start of a
stream, but only one reader will read the entire stream.

Let's say we have a program [`typedetect`](./examples/typedetect),
and we're reading from ``stdin``. For example:

```shell
$ cat myfile.ext | typedetect  
```

In this scenario, `typedetect` wants to detect
and print the type of data in the file/pipe, and then print the contents.
That detection sampling could be done in a separate goroutine per sampler type.
The input file could be, let's say, a JSON file, or an XML file.

The obvious approach is to inspect the first few tokens of the
input, and check if the tokens are either valid JSON or valid XML.
After that process, let's say we want to dump out a preview of the file contents.

Package `streamcache` provides a facility to create a `Stream` from an
underlying `io.Reader` (`os.Stdin` in this scenario), and spawn multiple
readers, each of which can operate independently, in their own
goroutines if desired. The underlying source (again, `os.Stdin` in this
scenario) will only once be read from, but its data is available to
multiple readers, because that data is cached in memory.

That is, until there's only one final reader left, (after invoking
`Stream.Seal`), at which point the cache is discarded, and
the final `Reader` reads directly from the underlying source.

## Usage

Add to your `go.mod` via `go get`:

```shell
go get github.com/neilotoole/streamcache
```

Here's a simple [example](./examples/in-out-err) that copies the contents
of `stdin` to `stdout` and `stderr`, and prints the number of bytes read.

```go
package main

import (
    "context"
    "errors"
    "fmt"
    "io"
    "os"

    "github.com/neilotoole/streamcache"
)

// Write stdin to both stdout and stderr.
// Some error handling omitted for brevity.
func main() {
    ctx := context.Background()
    stream := streamcache.New(os.Stdin)

    r1 := stream.NewReader(ctx)
    go func() {
        defer r1.Close()
        io.Copy(os.Stdout, r1)
    }()

    r2 := stream.NewReader(ctx)
   
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `tailbuf.md`
```markdown
# 📦 neilotoole/tailbuf [🔖 PENDING/APPROVE]
🔗 https://github.com/neilotoole/tailbuf


## Meta
- **Stars:** ⭐ 0 | **Forks:** 🍴 0
- **Language:** Go | **License:** MIT
- **Last updated:** 2024-03-14
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
tail, for Go objects

## README (trích đầu)
```
# tailbuf: tail, for Go objects

[![Go Reference](https://pkg.go.dev/badge/github.com/neilotoole/tailbuf.svg)](https://pkg.go.dev/github.com/neilotoole/tailbuf)
[![Go Report Card](https://goreportcard.com/badge/neilotoole/tailbuf)](https://goreportcard.com/report/neilotoole/tailbuf)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/neilotoole/tailbuf/blob/master/LICENSE)
![Workflow](https://github.com/neilotoole/tailbuf/actions/workflows/go.yml/badge.svg)

Package [`neilotoole/tailbuf`](https://pkg.go.dev/github.com/neilotoole/tailbuf) implements a fixed-size object tail buffer that provides a window
on the tail of items written to the buffer.

## Install

Add to your `go.mod` via `go get`:

```shell
go get github.com/neilotoole/tailbuf
```

## Usage

> [!WARNING]  
> Note that `tailbuf` is still in its `v0.0.x` infancy. There's a few things in
> the package API that probably need to be dialed in, so expect some churn.
> [Feedback](https://github.com/neilotoole/tailbuf/issues) is appreciated.

Below we'll create a [`tailbuf.Buf`](https://pkg.go.dev/github.com/neilotoole/tailbuf#Buf)
of type `string` with a capacity of `3`. You write to the buffer using [`buf.Write`](https://pkg.go.dev/github.com/neilotoole/tailbuf#Buf.Write)
or [`buf.WriteAll`](https://pkg.go.dev/github.com/neilotoole/tailbuf#Buf.WriteAll), and
you can access the tail slice using [`Buf.Tail`](https://pkg.go.dev/github.com/neilotoole/tailbuf#Buf.Tail).

```go
package main

import (
    "fmt"
    "github.com/neilotoole/tailbuf"
)

func main() {
    buf := tailbuf.New[string](3)

    buf.WriteAll("a", "b", "c")
    fmt.Println(buf.Tail())   // [a b c]

    buf.WriteAll("d", "e", "f", "g")
    fmt.Println(buf.Tail())   // [e f g]

    fmt.Println("Written:", buf.Written()) // Written: 7
}
```

Note that `Buf.Tail` returns a slice into the buffer's internal storage, so it's
only valid until the next write operation. If you need to retain the tail slice,
you should copy the returned slice, or instead use [`tailbuf.SliceTail`](https://pkg.go.dev/github.com/neilotoole/tailbuf#SliceTail), which
always returns a freshly-allocated slice.

There are various functions for popping, dropping, or peeking into the tail buffer.

```go
  buf := tailbuf.New[string](3)

  buf.WriteAll("a", "b", "c")
  fmt.Println(buf.Peek(0))      // a
  fmt.Println(buf.Peek(1))      // b

  fmt.Println(buf.PopBackN(2))  // [a b]
  fmt.Println(buf.Tail())       // [c]
```

There are also basic methods for interacting with the buffer:

```go
  buf := tailbuf.New[string](3)

  fmt.Println(buf.Cap())                   // 3
  fmt.Println(buf.Len())                   // 0
  buf.WriteAll("a", "b", "c")
  fmt.Println(buf.Len())                   // 3

  buf.WriteAll("d", "e", "f", "g")
  fmt.Println(buf.Len())                   // 3

  fmt.Println("Written:", buf.Written())   // 7
  buf.Reset()                              // Reset the buffer, including "written" count
  fmt.Println(buf.Len(
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

