---
id: github.com-peterbourgon-diskv-461e94b3-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:12.101595
---

# KNOWLEDGE EXTRACT: github.com_peterbourgon_diskv_461e94b3
> **Extracted on:** 2026-04-01 09:44:54
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007520414/github.com_peterbourgon_diskv_461e94b3

---

## File: `LICENSE`
```
Copyright (c) 2011-2012 Peter Bourgon

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
```

## File: `README.md`
```markdown
# What is diskv?

Diskv (disk-vee) is a simple, persistent key-value store written in the Go
language. It starts with an incredibly simple API for storing arbitrary data on
a filesystem by key, and builds several layers of performance-enhancing
abstraction on top.  The end result is a conceptually simple, but highly
performant, disk-backed storage system.

[![Build Status][1]][2]

[1]: https://drone.io/github.com/peterbourgon/diskv/status.png
[2]: https://drone.io/github.com/peterbourgon/diskv/latest


# Installing

Install [Go 1][3], either [from source][4] or [with a prepackaged binary][5].
Then,

```bash
$ go get github.com/peterbourgon/diskv/v3
```

[3]: http://golang.org
[4]: http://golang.org/doc/install/source
[5]: http://golang.org/doc/install


# Usage

```go
package main

import (
	"fmt"
	"github.com/peterbourgon/diskv/v3"
)

func main() {
	// Simplest transform function: put all the data files into the base dir.
	flatTransform := func(s string) []string { return []string{} }

	// Initialize a new diskv store, rooted at "my-data-dir", with a 1MB cache.
	d := diskv.New(diskv.Options{
		BasePath:     "my-data-dir",
		Transform:    flatTransform,
		CacheSizeMax: 1024 * 1024,
	})

	// Write three bytes to the key "alpha".
	key := "alpha"
	d.Write(key, []byte{'1', '2', '3'})

	// Read the value back out of the store.
	value, _ := d.Read(key)
	fmt.Printf("%v\n", value)

	// Erase the key+value from the store (and the disk).
	d.Erase(key)
}
```

More complex examples can be found in the "examples" subdirectory.


# Theory

## Basic idea

At its core, diskv is a map of a key (`string`) to arbitrary data (`[]byte`).
The data is written to a single file on disk, with the same name as the key.
The key determines where that file will be stored, via a user-provided
`TransformFunc`, which takes a key and returns a slice (`[]string`)
corresponding to a path list where the key file will be stored. The simplest
TransformFunc,

```go
func SimpleTransform (key string) []string {
    return []string{}
}
```

will place all keys in the same, base directory. The design is inspired by
[Redis diskstore][6]; a TransformFunc which emulates the default diskstore
behavior is available in the content-addressable-storage example.

[6]: http://groups.google.com/group/redis-db/browse_thread/thread/d444bc786689bde9?pli=1

**Note** that your TransformFunc should ensure that one valid key doesn't
transform to a subset of another valid key. That is, it shouldn't be possible
to construct valid keys that resolve to directory names. As a concrete example,
if your TransformFunc splits on every 3 characters, then

```go
d.Write("abcabc", val) // OK: written to <base>/abc/abc/abcabc
d.Write("abc", val)    // Error: attempted write to <base>/abc/abc, but it's a directory
```

This will be addressed in an upcoming version of diskv.

Probably the most important design principle behind diskv is that your data is
always flatly available on the disk. diskv will never do anything that would
prevent you from accessing, copying, backing up, or otherwise interacting with
your data via common UNIX commandline tools.

## Advanced path transformation

If you need more control over the file name written to disk or if you want to support
slashes in your key name or special characters in the keys, you can use the
AdvancedTransform property. You must supply a function that returns
a special PathKey structure, which is a breakdown of a path and a file name. Strings
returned must be clean of any slashes or special characters:

```go
func AdvancedTransformExample(key string) *diskv.PathKey {
	path := strings.Split(key, "/")
	last := len(path) - 1
	return &diskv.PathKey{
		Path:     path[:last],
		FileName: path[last] + ".txt",
	}
}

// If you provide an AdvancedTransform, you must also provide its
// inverse:

func InverseTransformExample(pathKey *diskv.PathKey) (key string) {
	txt := pathKey.FileName[len(pathKey.FileName)-4:]
	if txt != ".txt" {
		panic("Invalid file found in storage folder!")
	}
	return strings.Join(pathKey.Path, "/") + pathKey.FileName[:len(pathKey.FileName)-4]
}

func main() {
	d := diskv.New(diskv.Options{
		BasePath:          "my-data-dir",
		AdvancedTransform: AdvancedTransformExample,
		InverseTransform:  InverseTransformExample,
		CacheSizeMax:      1024 * 1024,
	})
	// Write some text to the key "alpha/beta/gamma".
	key := "alpha/beta/gamma"
	d.WriteString(key, "¡Hola!") // will be stored in "<basedir>/alpha/beta/gamma.txt"
	fmt.Println(d.ReadString("alpha/beta/gamma"))
}
```


## Adding a cache

An in-memory caching layer is provided by combining the BasicStore
functionality with a simple map structure, and keeping it up-to-date as
appropriate. Since the map structure in Go is not threadsafe, it's combined
with a RWMutex to provide safe concurrent access.

## Adding order

diskv is a key-value store and therefore inherently unordered. An ordering
system can be injected into the store by passing something which satisfies the
diskv.Index interface. (A default implementation, using Google's
[btree][7] package, is provided.) Basically, diskv keeps an ordered (by a
user-provided Less function) index of the keys, which can be queried.

[7]: https://github.com/google/btree

## Adding compression

Something which implements the diskv.Compression interface may be passed
during store creation, so that all Writes and Reads are filtered through
a compression/decompression pipeline. Several default implementations,
using stdlib compression algorithms, are provided. Note that data is cached
compressed; the cost of decompression is borne with each Read.

## Streaming

diskv also now provides ReadStream and WriteStream methods, to allow very large
data to be handled efficiently.


# Future plans

 * Needs plenty of robust testing: huge datasets, etc...
 * More thorough benchmarking
 * Your suggestions for use-cases I haven't thought of


# Credits and contributions

Original idea, design and implementation: [Peter Bourgon](https://github.com/peterbourgon)
Other collaborations: [Javier Peletier](https://github.com/jpeletier) ([Epic Labs](https://www.epiclabs.io))
```

## File: `basic_test.go`
```go
package diskv

import (
	"bytes"
	"errors"
	"math/rand"
	"regexp"
	"strings"
	"testing"
	"time"
)

func cmpBytes(a, b []byte) bool {
	if len(a) != len(b) {
		return false
	}
	for i := 0; i < len(a); i++ {
		if a[i] != b[i] {
			return false
		}
	}
	return true
}

func (d *Diskv) isCached(key string) bool {
	d.mu.RLock()
	defer d.mu.RUnlock()
	_, ok := d.cache[key]
	return ok
}

func TestWriteReadErase(t *testing.T) {
	d := New(Options{
		BasePath:     "test-data",
		CacheSizeMax: 1024,
	})
	defer d.EraseAll()
	k, v := "a", []byte{'b'}
	if err := d.Write(k, v); err != nil {
		t.Fatalf("write: %s", err)
	}
	if readVal, err := d.Read(k); err != nil {
		t.Fatalf("read: %s", err)
	} else if bytes.Compare(v, readVal) != 0 {
		t.Fatalf("read: expected %s, got %s", v, readVal)
	}
	if err := d.Erase(k); err != nil {
		t.Fatalf("erase: %s", err)
	}
}

func TestWRECache(t *testing.T) {
	d := New(Options{
		BasePath:     "test-data",
		CacheSizeMax: 1024,
	})
	defer d.EraseAll()
	k, v := "xxx", []byte{' ', ' ', ' '}
	if d.isCached(k) {
		t.Fatalf("key cached before Write and Read")
	}
	if err := d.Write(k, v); err != nil {
		t.Fatalf("write: %s", err)
	}
	if d.isCached(k) {
		t.Fatalf("key cached before Read")
	}
	if readVal, err := d.Read(k); err != nil {
		t.Fatalf("read: %s", err)
	} else if bytes.Compare(v, readVal) != 0 {
		t.Fatalf("read: expected %s, got %s", v, readVal)
	}
	for i := 0; i < 10 && !d.isCached(k); i++ {
		time.Sleep(10 * time.Millisecond)
	}
	if !d.isCached(k) {
		t.Fatalf("key not cached after Read")
	}
	if err := d.Erase(k); err != nil {
		t.Fatalf("erase: %s", err)
	}
	if d.isCached(k) {
		t.Fatalf("key cached after Erase")
	}
}

func TestStrings(t *testing.T) {
	d := New(Options{
		BasePath:     "test-data",
		CacheSizeMax: 1024,
	})
	defer d.EraseAll()

	keys := map[string]bool{"a": false, "b": false, "c": false, "d": false}
	v := []byte{'1'}
	for k := range keys {
		if err := d.Write(k, v); err != nil {
			t.Fatalf("write: %s: %s", k, err)
		}
	}

	for k := range d.Keys(nil) {
		if _, present := keys[k]; present {
			t.Logf("got: %s", k)
			keys[k] = true
		} else {
			t.Fatalf("strings() returns unknown key: %s", k)
		}
	}

	for k, found := range keys {
		if !found {
			t.Errorf("never got %s", k)
		}
	}
}

func TestZeroByteCache(t *testing.T) {
	d := New(Options{
		BasePath:     "test-data",
		CacheSizeMax: 0,
	})
	defer d.EraseAll()

	k, v := "a", []byte{'1', '2', '3'}
	if err := d.Write(k, v); err != nil {
		t.Fatalf("Write: %s", err)
	}

	if d.isCached(k) {
		t.Fatalf("key cached, expected not-cached")
	}

	if _, err := d.Read(k); err != nil {
		t.Fatalf("Read: %s", err)
	}

	if d.isCached(k) {
		t.Fatalf("key cached, expected not-cached")
	}
}

func TestOneByteCache(t *testing.T) {
	d := New(Options{
		BasePath:     "test-data",
		CacheSizeMax: 1,
	})
	defer d.EraseAll()

	k1, k2, v1, v2 := "a", "b", []byte{'1'}, []byte{'1', '2'}
	if err := d.Write(k1, v1); err != nil {
		t.Fatal(err)
	}

	if v, err := d.Read(k1); err != nil {
		t.Fatal(err)
	} else if !cmpBytes(v, v1) {
		t.Fatalf("Read: expected %s, got %s", string(v1), string(v))
	}

	for i := 0; i < 10 && !d.isCached(k1); i++ {
		time.Sleep(10 * time.Millisecond)
	}
	if !d.isCached(k1) {
		t.Fatalf("expected 1-byte value to be cached, but it wasn't")
	}

	if err := d.Write(k2, v2); err != nil {
		t.Fatal(err)
	}
	if _, err := d.Read(k2); err != nil {
		t.Fatalf("--> %s", err)
	}

	for i := 0; i < 10 && (!d.isCached(k1) || d.isCached(k2)); i++ {
		time.Sleep(10 * time.Millisecond) // just wait for lazy-cache
	}
	if !d.isCached(k1) {
		t.Fatalf("1-byte value was uncached for no reason")
	}

	if d.isCached(k2) {
		t.Fatalf("2-byte value was cached, but cache max size is 1")
	}
}

func TestStaleCache(t *testing.T) {
	d := New(Options{
		BasePath:     "test-data",
		CacheSizeMax: 1,
	})
	defer d.EraseAll()

	k, first, second := "a", "first", "second"
	if err := d.Write(k, []byte(first)); err != nil {
		t.Fatal(err)
	}

	v, err := d.Read(k)
	if err != nil {
		t.Fatal(err)
	}
	if string(v) != first {
		t.Errorf("expected '%s', got '%s'", first, v)
	}

	if err := d.Write(k, []byte(second)); err != nil {
		t.Fatal(err)
	}

	v, err = d.Read(k)
	if err != nil {
		t.Fatal(err)
	}

	if string(v) != second {
		t.Errorf("expected '%s', got '%s'", second, v)
	}
}

func TestHas(t *testing.T) {
	d := New(Options{
		BasePath:     "test-data",
		CacheSizeMax: 1024,
	})
	defer d.EraseAll()

	for k, v := range map[string]string{
		"a":      "1",
		"foo":    "2",
		"012345": "3",
	} {
		d.Write(k, []byte(v))
	}

	d.Read("foo") // cache one of them
	if !d.isCached("foo") {
		t.Errorf("'foo' didn't get cached")
	}

	for _, tuple := range []struct {
		key      string
		expected bool
	}{
		{"a", true},
		{"b", false},
		{"foo", true},
		{"bar", false},
		{"01234", false},
		{"012345", true},
		{"0123456", false},
	} {
		if expected, got := tuple.expected, d.Has(tuple.key); expected != got {
			t.Errorf("Has(%s): expected %v, got %v", tuple.key, expected, got)
		}
	}
}

type BrokenReader struct{}

func (BrokenReader) Read(p []byte) (n int, err error) {
	return 0, errors.New("failed to read")
}

func TestRemovesIncompleteFiles(t *testing.T) {
	opts := Options{
		BasePath:     "test-data",
		CacheSizeMax: 1024,
	}
	d := New(opts)
	defer d.EraseAll()

	key, stream, sync := "key", BrokenReader{}, false

	if err := d.WriteStream(key, stream, sync); err == nil {
		t.Fatalf("Expected i/o copy error, none received.")
	}

	if _, err := d.Read(key); err == nil {
		t.Fatal("Could read the key, but it shouldn't exist")
	}
}

func TestTempDir(t *testing.T) {
	opts := Options{
		BasePath:     "test-data",
		TempDir:      "test-data-temp",
		CacheSizeMax: 1024,
	}
	d := New(opts)
	defer d.EraseAll()

	k, v := "a", []byte{'b'}
	if err := d.Write(k, v); err != nil {
		t.Fatalf("write: %s", err)
	}
	if readVal, err := d.Read(k); err != nil {
		t.Fatalf("read: %s", err)
	} else if bytes.Compare(v, readVal) != 0 {
		t.Fatalf("read: expected %s, got %s", v, readVal)
	}
	if err := d.Erase(k); err != nil {
		t.Fatalf("erase: %s", err)
	}
}

type CrashingReader struct{}

func (CrashingReader) Read(p []byte) (n int, err error) {
	panic("System has crashed while reading the stream")
}

func TestAtomicWrite(t *testing.T) {
	opts := Options{
		BasePath: "test-data",
		// Test would fail if TempDir is not set here.
		TempDir:      "test-data-temp",
		CacheSizeMax: 1024,
	}
	d := New(opts)
	defer d.EraseAll()

	key := "key"
	func() {
		defer func() {
			recover() // Ignore panicking error
		}()

		stream := CrashingReader{}
		d.WriteStream(key, stream, false)
	}()

	if d.Has(key) {
		t.Fatal("Has key, but it shouldn't exist")
	}
	if _, ok := <-d.Keys(nil); ok {
		t.Fatal("Store isn't empty")
	}
}

const letterBytes = "abcdef0123456789"

func randStringBytes(n int) string {
	b := make([]byte, n)
	for i := range b {
		b[i] = letterBytes[rand.Intn(len(letterBytes))]
	}
	return string(b)
}

func TestHybridStore(t *testing.T) {
	regex := regexp.MustCompile("[0-9a-fA-F]{64}")

	transformFunc := func(s string) *PathKey {

		if regex.MatchString(s) {
			return &PathKey{Path: []string{"objects", s[0:2]},
				FileName: s,
			}
		}

		folders := strings.Split(s, "/")
		lfolders := len(folders)
		if lfolders > 1 {
			return &PathKey{Path: folders[:lfolders-1],
				FileName: folders[lfolders-1],
			}
		}

		return &PathKey{Path: []string{},
			FileName: s,
		}
	}

	inverseTransformFunc := func(pathKey *PathKey) string {

		if regex.MatchString(pathKey.FileName) {
			return pathKey.FileName

		}

		if len(pathKey.Path) == 0 {
			return pathKey.FileName
		}

		return strings.Join(pathKey.Path, "/") + "/" + pathKey.FileName

	}
	opts := Options{
		BasePath:          "test-data",
		CacheSizeMax:      1024,
		AdvancedTransform: transformFunc,
		InverseTransform:  inverseTransformFunc,
	}
	d := New(opts)
	defer d.EraseAll()

	testData := map[string]string{}

	for i := 0; i < 100; i++ {
		testData[randStringBytes(64)] = randStringBytes(100)
	}

	for i := 0; i < 100; i++ {
		testData[randStringBytes(20)] = randStringBytes(100)
	}

	for i := 0; i < 100; i++ {
		numsep := rand.Intn(10) + 1
		key := ""
		for j := 0; j < numsep; j++ {
			key += randStringBytes(10) + "/"
		}
		key += randStringBytes(40)
		testData[key] = randStringBytes(100)
	}

	for k, v := range testData {
		d.WriteString(k, v)
	}

	for k, v := range testData {
		readVal := d.ReadString(k)

		if v != readVal {
			t.Fatalf("read: expected %s, got %s", v, readVal)
		}
	}

}
```

## File: `compression.go`
```go
package diskv

import (
	"compress/flate"
	"compress/gzip"
	"compress/zlib"
	"io"
)

// Compression is an interface that Diskv uses to implement compression of
// data. Writer takes a destination io.Writer and returns a WriteCloser that
// compresses all data written through it. Reader takes a source io.Reader and
// returns a ReadCloser that decompresses all data read through it. You may
// define these methods on your own type, or use one of the NewCompression
// helpers.
type Compression interface {
	Writer(dst io.Writer) (io.WriteCloser, error)
	Reader(src io.Reader) (io.ReadCloser, error)
}

// NewGzipCompression returns a Gzip-based Compression.
func NewGzipCompression() Compression {
	return NewGzipCompressionLevel(flate.DefaultCompression)
}

// NewGzipCompressionLevel returns a Gzip-based Compression with the given level.
func NewGzipCompressionLevel(level int) Compression {
	return &genericCompression{
		wf: func(w io.Writer) (io.WriteCloser, error) { return gzip.NewWriterLevel(w, level) },
		rf: func(r io.Reader) (io.ReadCloser, error) { return gzip.NewReader(r) },
	}
}

// NewZlibCompression returns a Zlib-based Compression.
func NewZlibCompression() Compression {
	return NewZlibCompressionLevel(flate.DefaultCompression)
}

// NewZlibCompressionLevel returns a Zlib-based Compression with the given level.
func NewZlibCompressionLevel(level int) Compression {
	return NewZlibCompressionLevelDict(level, nil)
}

// NewZlibCompressionLevelDict returns a Zlib-based Compression with the given
// level, based on the given dictionary.
func NewZlibCompressionLevelDict(level int, dict []byte) Compression {
	return &genericCompression{
		func(w io.Writer) (io.WriteCloser, error) { return zlib.NewWriterLevelDict(w, level, dict) },
		func(r io.Reader) (io.ReadCloser, error) { return zlib.NewReaderDict(r, dict) },
	}
}

type genericCompression struct {
	wf func(w io.Writer) (io.WriteCloser, error)
	rf func(r io.Reader) (io.ReadCloser, error)
}

func (g *genericCompression) Writer(dst io.Writer) (io.WriteCloser, error) {
	return g.wf(dst)
}

func (g *genericCompression) Reader(src io.Reader) (io.ReadCloser, error) {
	return g.rf(src)
}
```

## File: `compression_test.go`
```go
package diskv

import (
	"compress/flate"
	"fmt"
	"math/rand"
	"os"
	"testing"
	"time"
)

func init() {
	rand.Seed(time.Now().UnixNano())
}

func testCompressionWith(t *testing.T, c Compression, name string) {
	d := New(Options{
		BasePath:     "compression-test",
		CacheSizeMax: 0,
		Compression:  c,
	})
	defer d.EraseAll()

	sz := 4096
	val := make([]byte, sz)
	for i := 0; i < sz; i++ {
		val[i] = byte('a' + rand.Intn(26)) // {a-z}; should compress some
	}

	key := "a"
	if err := d.Write(key, val); err != nil {
		t.Fatalf("write failed: %s", err)
	}

	targetFile := fmt.Sprintf("%s%c%s", d.BasePath, os.PathSeparator, key)
	fi, err := os.Stat(targetFile)
	if err != nil {
		t.Fatalf("%s: %s", targetFile, err)
	}

	if fi.Size() >= int64(sz) {
		t.Fatalf("%s: size=%d, expected smaller", targetFile, fi.Size())
	}
	t.Logf("%s compressed %d to %d", name, sz, fi.Size())

	readVal, err := d.Read(key)
	if len(readVal) != sz {
		t.Fatalf("read: expected size=%d, got size=%d", sz, len(readVal))
	}

	for i := 0; i < sz; i++ {
		if readVal[i] != val[i] {
			t.Fatalf("i=%d: expected %v, got %v", i, val[i], readVal[i])
		}
	}
}

func TestGzipDefault(t *testing.T) {
	testCompressionWith(t, NewGzipCompression(), "gzip")
}

func TestGzipBestCompression(t *testing.T) {
	testCompressionWith(t, NewGzipCompressionLevel(flate.BestCompression), "gzip-max")
}

func TestGzipBestSpeed(t *testing.T) {
	testCompressionWith(t, NewGzipCompressionLevel(flate.BestSpeed), "gzip-min")
}

func TestZlib(t *testing.T) {
	testCompressionWith(t, NewZlibCompression(), "zlib")
}
```

## File: `diskv.go`
```go
// Diskv (disk-vee) is a simple, persistent, key-value store.
// It stores all data flatly on the filesystem.

package diskv

import (
	"bytes"
	"errors"
	"fmt"
	"io"
	"io/ioutil"
	"os"
	"path/filepath"
	"strings"
	"sync"
	"syscall"
)

const (
	defaultBasePath             = "diskv"
	defaultFilePerm os.FileMode = 0666
	defaultPathPerm os.FileMode = 0777
)

// PathKey represents a string key that has been transformed to
// a directory and file name where the content will eventually
// be stored
type PathKey struct {
	Path        []string
	FileName    string
	originalKey string
}

var (
	defaultAdvancedTransform = func(s string) *PathKey { return &PathKey{Path: []string{}, FileName: s} }
	defaultInverseTransform  = func(pathKey *PathKey) string { return pathKey.FileName }
	errCanceled              = errors.New("canceled")
	errEmptyKey              = errors.New("empty key")
	errBadKey                = errors.New("bad key")
	errImportDirectory       = errors.New("can't import a directory")
)

// TransformFunction transforms a key into a slice of strings, with each
// element in the slice representing a directory in the file path where the
// key's entry will eventually be stored.
//
// For example, if TransformFunc transforms "abcdef" to ["ab", "cde", "f"],
// the final location of the data file will be <basedir>/ab/cde/f/abcdef
type TransformFunction func(s string) []string

// AdvancedTransformFunction transforms a key into a PathKey.
//
// A PathKey contains a slice of strings, where each element in the slice
// represents a directory in the file path where the key's entry will eventually
// be stored, as well as the filename.
//
// For example, if AdvancedTransformFunc transforms "abcdef/file.txt" to the
// PathKey {Path: ["ab", "cde", "f"], FileName: "file.txt"}, the final location
// of the data file will be <basedir>/ab/cde/f/file.txt.
//
// You must provide an InverseTransformFunction if you use an
// AdvancedTransformFunction.
type AdvancedTransformFunction func(s string) *PathKey

// InverseTransformFunction takes a PathKey and converts it back to a Diskv key.
// In effect, it's the opposite of an AdvancedTransformFunction.
type InverseTransformFunction func(pathKey *PathKey) string

// Options define a set of properties that dictate Diskv behavior.
// All values are optional.
type Options struct {
	BasePath          string
	Transform         TransformFunction
	AdvancedTransform AdvancedTransformFunction
	InverseTransform  InverseTransformFunction
	CacheSizeMax      uint64 // bytes
	PathPerm          os.FileMode
	FilePerm          os.FileMode
	// If TempDir is set, it will enable filesystem atomic writes by
	// writing temporary files to that location before being moved
	// to BasePath.
	// Note that TempDir MUST be on the same device/partition as
	// BasePath.
	TempDir string

	Index     Index
	IndexLess LessFunction

	Compression Compression
}

// Diskv implements the Diskv interface. You shouldn't construct Diskv
// structures directly; instead, use the New constructor.
type Diskv struct {
	Options
	mu        sync.RWMutex
	cache     map[string][]byte
	cacheSize uint64
}

// New returns an initialized Diskv structure, ready to use.
// If the path identified by baseDir already contains data,
// it will be accessible, but not yet cached.
func New(o Options) *Diskv {
	if o.BasePath == "" {
		o.BasePath = defaultBasePath
	}

	if o.AdvancedTransform == nil {
		if o.Transform == nil {
			o.AdvancedTransform = defaultAdvancedTransform
		} else {
			o.AdvancedTransform = convertToAdvancedTransform(o.Transform)
		}
		if o.InverseTransform == nil {
			o.InverseTransform = defaultInverseTransform
		}
	} else {
		if o.InverseTransform == nil {
			panic("You must provide an InverseTransform function in advanced mode")
		}
	}

	if o.PathPerm == 0 {
		o.PathPerm = defaultPathPerm
	}
	if o.FilePerm == 0 {
		o.FilePerm = defaultFilePerm
	}

	d := &Diskv{
		Options:   o,
		cache:     map[string][]byte{},
		cacheSize: 0,
	}

	if d.Index != nil && d.IndexLess != nil {
		d.Index.Initialize(d.IndexLess, d.Keys(nil))
	}

	return d
}

// convertToAdvancedTransform takes a classic Transform function and
// converts it to the new AdvancedTransform
func convertToAdvancedTransform(oldFunc func(s string) []string) AdvancedTransformFunction {
	return func(s string) *PathKey {
		return &PathKey{Path: oldFunc(s), FileName: s}
	}
}

// Write synchronously writes the key-value pair to disk, making it immediately
// available for reads. Write relies on the filesystem to perform an eventual
// sync to physical media. If you need stronger guarantees, see WriteStream.
func (d *Diskv) Write(key string, val []byte) error {
	return d.WriteStream(key, bytes.NewReader(val), false)
}

// WriteString writes a string key-value pair to disk
func (d *Diskv) WriteString(key string, val string) error {
	return d.Write(key, []byte(val))
}

func (d *Diskv) transform(key string) (pathKey *PathKey) {
	pathKey = d.AdvancedTransform(key)
	pathKey.originalKey = key
	return pathKey
}

// WriteStream writes the data represented by the io.Reader to the disk, under
// the provided key. If sync is true, WriteStream performs an explicit sync on
// the file as soon as it's written.
//
// bytes.Buffer provides io.Reader semantics for basic data types.
func (d *Diskv) WriteStream(key string, r io.Reader, sync bool) error {
	if len(key) <= 0 {
		return errEmptyKey
	}

	pathKey := d.transform(key)

	// Ensure keys cannot evaluate to paths that would not exist
	for _, pathPart := range pathKey.Path {
		if strings.ContainsRune(pathPart, os.PathSeparator) {
			return errBadKey
		}
	}

	if strings.ContainsRune(pathKey.FileName, os.PathSeparator) {
		return errBadKey
	}

	d.mu.Lock()
	defer d.mu.Unlock()

	return d.writeStreamWithLock(pathKey, r, sync)
}

// createKeyFileWithLock either creates the key file directly, or
// creates a temporary file in TempDir if it is set.
func (d *Diskv) createKeyFileWithLock(pathKey *PathKey) (*os.File, error) {
	if d.TempDir != "" {
		if err := os.MkdirAll(d.TempDir, d.PathPerm); err != nil {
			return nil, fmt.Errorf("temp mkdir: %s", err)
		}
		f, err := ioutil.TempFile(d.TempDir, "")
		if err != nil {
			return nil, fmt.Errorf("temp file: %s", err)
		}

		if err := os.Chmod(f.Name(), d.FilePerm); err != nil {
			f.Close()           // error deliberately ignored
			os.Remove(f.Name()) // error deliberately ignored
			return nil, fmt.Errorf("chmod: %s", err)
		}
		return f, nil
	}

	mode := os.O_WRONLY | os.O_CREATE | os.O_TRUNC // overwrite if exists
	f, err := os.OpenFile(d.completeFilename(pathKey), mode, d.FilePerm)
	if err != nil {
		return nil, fmt.Errorf("open file: %s", err)
	}
	return f, nil
}

// writeStream does no input validation checking.
func (d *Diskv) writeStreamWithLock(pathKey *PathKey, r io.Reader, sync bool) error {
	if err := d.ensurePathWithLock(pathKey); err != nil {
		return fmt.Errorf("ensure path: %s", err)
	}

	f, err := d.createKeyFileWithLock(pathKey)
	if err != nil {
		return fmt.Errorf("create key file: %s", err)
	}

	wc := io.WriteCloser(&nopWriteCloser{f})
	if d.Compression != nil {
		wc, err = d.Compression.Writer(f)
		if err != nil {
			f.Close()           // error deliberately ignored
			os.Remove(f.Name()) // error deliberately ignored
			return fmt.Errorf("compression writer: %s", err)
		}
	}

	if _, err := io.Copy(wc, r); err != nil {
		f.Close()           // error deliberately ignored
		os.Remove(f.Name()) // error deliberately ignored
		return fmt.Errorf("i/o copy: %s", err)
	}

	if err := wc.Close(); err != nil {
		f.Close()           // error deliberately ignored
		os.Remove(f.Name()) // error deliberately ignored
		return fmt.Errorf("compression close: %s", err)
	}

	if sync {
		if err := f.Sync(); err != nil {
			f.Close()           // error deliberately ignored
			os.Remove(f.Name()) // error deliberately ignored
			return fmt.Errorf("file sync: %s", err)
		}
	}

	if err := f.Close(); err != nil {
		return fmt.Errorf("file close: %s", err)
	}

	fullPath := d.completeFilename(pathKey)
	if f.Name() != fullPath {
		if err := os.Rename(f.Name(), fullPath); err != nil {
			os.Remove(f.Name()) // error deliberately ignored
			return fmt.Errorf("rename: %s", err)
		}
	}

	if d.Index != nil {
		d.Index.Insert(pathKey.originalKey)
	}

	d.bustCacheWithLock(pathKey.originalKey) // cache only on read

	return nil
}

// Import imports the source file into diskv under the destination key. If the
// destination key already exists, it's overwritten. If move is true, the
// source file is removed after a successful import.
func (d *Diskv) Import(srcFilename, dstKey string, move bool) (err error) {
	if dstKey == "" {
		return errEmptyKey
	}

	if fi, err := os.Stat(srcFilename); err != nil {
		return err
	} else if fi.IsDir() {
		return errImportDirectory
	}

	dstPathKey := d.transform(dstKey)

	d.mu.Lock()
	defer d.mu.Unlock()

	if err := d.ensurePathWithLock(dstPathKey); err != nil {
		return fmt.Errorf("ensure path: %s", err)
	}

	if move {
		if err := syscall.Rename(srcFilename, d.completeFilename(dstPathKey)); err == nil {
			d.bustCacheWithLock(dstPathKey.originalKey)
			return nil
		} else if err != syscall.EXDEV {
			// If it failed due to being on a different device, fall back to copying
			return err
		}
	}

	f, err := os.Open(srcFilename)
	if err != nil {
		return err
	}
	defer f.Close()
	err = d.writeStreamWithLock(dstPathKey, f, false)
	if err == nil && move {
		err = os.Remove(srcFilename)
	}
	return err
}

// Read reads the key and returns the value.
// If the key is available in the cache, Read won't touch the disk.
// If the key is not in the cache, Read will have the side-effect of
// lazily caching the value.
func (d *Diskv) Read(key string) ([]byte, error) {
	rc, err := d.ReadStream(key, false)
	if err != nil {
		return []byte{}, err
	}
	defer rc.Close()
	return ioutil.ReadAll(rc)
}

// ReadString reads the key and returns a string value
// In case of error, an empty string is returned
func (d *Diskv) ReadString(key string) string {
	value, _ := d.Read(key)
	return string(value)
}

// ReadStream reads the key and returns the value (data) as an io.ReadCloser.
// If the value is cached from a previous read, and direct is false,
// ReadStream will use the cached value. Otherwise, it will return a handle to
// the file on disk, and cache the data on read.
//
// If direct is true, ReadStream will lazily delete any cached value for the
// key, and return a direct handle to the file on disk.
//
// If compression is enabled, ReadStream taps into the io.Reader stream prior
// to decompression, and caches the compressed data.
func (d *Diskv) ReadStream(key string, direct bool) (io.ReadCloser, error) {

	pathKey := d.transform(key)
	d.mu.RLock()
	defer d.mu.RUnlock()

	if val, ok := d.cache[key]; ok {
		if !direct {
			buf := bytes.NewReader(val)
			if d.Compression != nil {
				return d.Compression.Reader(buf)
			}
			return ioutil.NopCloser(buf), nil
		}

		go func() {
			d.mu.Lock()
			defer d.mu.Unlock()
			d.uncacheWithLock(key, uint64(len(val)))
		}()
	}

	return d.readWithRLock(pathKey)
}

// read ignores the cache, and returns an io.ReadCloser representing the
// decompressed data for the given key, streamed from the disk. Clients should
// acquire a read lock on the Diskv and check the cache themselves before
// calling read.
func (d *Diskv) readWithRLock(pathKey *PathKey) (io.ReadCloser, error) {
	filename := d.completeFilename(pathKey)

	fi, err := os.Stat(filename)
	if err != nil {
		return nil, err
	}
	if fi.IsDir() {
		return nil, os.ErrNotExist
	}

	f, err := os.Open(filename)
	if err != nil {
		return nil, err
	}

	var r io.Reader
	if d.CacheSizeMax > 0 {
		r = newSiphon(f, d, pathKey.originalKey)
	} else {
		r = &closingReader{f}
	}

	var rc = io.ReadCloser(ioutil.NopCloser(r))
	if d.Compression != nil {
		rc, err = d.Compression.Reader(r)
		if err != nil {
			return nil, err
		}
	}

	return rc, nil
}

// closingReader provides a Reader that automatically closes the
// embedded ReadCloser when it reaches EOF
type closingReader struct {
	rc io.ReadCloser
}

func (cr closingReader) Read(p []byte) (int, error) {
	n, err := cr.rc.Read(p)
	if err == io.EOF {
		if closeErr := cr.rc.Close(); closeErr != nil {
			return n, closeErr // close must succeed for Read to succeed
		}
	}
	return n, err
}

// siphon is like a TeeReader: it copies all data read through it to an
// internal buffer, and moves that buffer to the cache at EOF.
type siphon struct {
	f   *os.File
	d   *Diskv
	key string
	buf *bytes.Buffer
}

// newSiphon constructs a siphoning reader that represents the passed file.
// When a successful series of reads ends in an EOF, the siphon will write
// the buffered data to Diskv's cache under the given key.
func newSiphon(f *os.File, d *Diskv, key string) io.Reader {
	return &siphon{
		f:   f,
		d:   d,
		key: key,
		buf: &bytes.Buffer{},
	}
}

// Read implements the io.Reader interface for siphon.
func (s *siphon) Read(p []byte) (int, error) {
	n, err := s.f.Read(p)

	if err == nil {
		return s.buf.Write(p[0:n]) // Write must succeed for Read to succeed
	}

	if err == io.EOF {
		s.d.cacheWithoutLock(s.key, s.buf.Bytes()) // cache may fail
		if closeErr := s.f.Close(); closeErr != nil {
			return n, closeErr // close must succeed for Read to succeed
		}
		return n, err
	}

	return n, err
}

// Erase synchronously erases the given key from the disk and the cache.
func (d *Diskv) Erase(key string) error {
	pathKey := d.transform(key)
	d.mu.Lock()
	defer d.mu.Unlock()

	d.bustCacheWithLock(key)

	// erase from index
	if d.Index != nil {
		d.Index.Delete(key)
	}

	// erase from disk
	filename := d.completeFilename(pathKey)
	if s, err := os.Stat(filename); err == nil {
		if s.IsDir() {
			return errBadKey
		}
		if err = os.Remove(filename); err != nil {
			return err
		}
	} else {
		// Return err as-is so caller can do os.IsNotExist(err).
		return err
	}

	// clean up and return
	d.pruneDirsWithLock(key)
	return nil
}

// EraseAll will delete all of the data from the store, both in the cache and on
// the disk. Note that EraseAll doesn't distinguish diskv-related data from non-
// diskv-related data. Care should be taken to always specify a diskv base
// directory that is exclusively for diskv data.
func (d *Diskv) EraseAll() error {
	d.mu.Lock()
	defer d.mu.Unlock()
	d.cache = make(map[string][]byte)
	d.cacheSize = 0
	if d.TempDir != "" {
		os.RemoveAll(d.TempDir) // errors ignored
	}
	return os.RemoveAll(d.BasePath)
}

// Has returns true if the given key exists.
func (d *Diskv) Has(key string) bool {
	pathKey := d.transform(key)
	d.mu.Lock()
	defer d.mu.Unlock()

	if _, ok := d.cache[key]; ok {
		return true
	}

	filename := d.completeFilename(pathKey)
	s, err := os.Stat(filename)
	if err != nil {
		return false
	}
	if s.IsDir() {
		return false
	}

	return true
}

// Keys returns a channel that will yield every key accessible by the store,
// in undefined order. If a cancel channel is provided, closing it will
// terminate and close the keys channel.
func (d *Diskv) Keys(cancel <-chan struct{}) <-chan string {
	return d.KeysPrefix("", cancel)
}

// KeysPrefix returns a channel that will yield every key accessible by the
// store with the given prefix, in undefined order. If a cancel channel is
// provided, closing it will terminate and close the keys channel. If the
// provided prefix is the empty string, all keys will be yielded.
func (d *Diskv) KeysPrefix(prefix string, cancel <-chan struct{}) <-chan string {
	var prepath string
	if prefix == "" {
		prepath = d.BasePath
	} else {
		prefixKey := d.transform(prefix)
		prepath = d.pathFor(prefixKey)
	}
	c := make(chan string)
	go func() {
		filepath.Walk(prepath, d.walker(c, prefix, cancel))
		close(c)
	}()
	return c
}

// walker returns a function which satisfies the filepath.WalkFunc interface.
// It sends every non-directory file entry down the channel c.
func (d *Diskv) walker(c chan<- string, prefix string, cancel <-chan struct{}) filepath.WalkFunc {
	return func(path string, info os.FileInfo, err error) error {
		if err != nil {
			return err
		}

		relPath, _ := filepath.Rel(d.BasePath, path)
		dir, file := filepath.Split(relPath)
		pathSplit := strings.Split(dir, string(filepath.Separator))
		pathSplit = pathSplit[:len(pathSplit)-1]

		pathKey := &PathKey{
			Path:     pathSplit,
			FileName: file,
		}

		key := d.InverseTransform(pathKey)

		if info.IsDir() || !strings.HasPrefix(key, prefix) {
			return nil // "pass"
		}

		select {
		case c <- key:
		case <-cancel:
			return errCanceled
		}

		return nil
	}
}

// pathFor returns the absolute path for location on the filesystem where the
// data for the given key will be stored.
func (d *Diskv) pathFor(pathKey *PathKey) string {
	return filepath.Join(d.BasePath, filepath.Join(pathKey.Path...))
}

// ensurePathWithLock is a helper function that generates all necessary
// directories on the filesystem for the given key.
func (d *Diskv) ensurePathWithLock(pathKey *PathKey) error {
	return os.MkdirAll(d.pathFor(pathKey), d.PathPerm)
}

// completeFilename returns the absolute path to the file for the given key.
func (d *Diskv) completeFilename(pathKey *PathKey) string {
	return filepath.Join(d.pathFor(pathKey), pathKey.FileName)
}

// cacheWithLock attempts to cache the given key-value pair in the store's
// cache. It can fail if the value is larger than the cache's maximum size.
func (d *Diskv) cacheWithLock(key string, val []byte) error {
	// If the key already exists, delete it.
	d.bustCacheWithLock(key)

	valueSize := uint64(len(val))
	if err := d.ensureCacheSpaceWithLock(valueSize); err != nil {
		return fmt.Errorf("%s; not caching", err)
	}

	// be very strict about memory guarantees
	if (d.cacheSize + valueSize) > d.CacheSizeMax {
		panic(fmt.Sprintf("failed to make room for value (%d/%d)", valueSize, d.CacheSizeMax))
	}

	d.cache[key] = val
	d.cacheSize += valueSize
	return nil
}

// cacheWithoutLock acquires the store's (write) mutex and calls cacheWithLock.
func (d *Diskv) cacheWithoutLock(key string, val []byte) error {
	d.mu.Lock()
	defer d.mu.Unlock()
	return d.cacheWithLock(key, val)
}

func (d *Diskv) bustCacheWithLock(key string) {
	if val, ok := d.cache[key]; ok {
		d.uncacheWithLock(key, uint64(len(val)))
	}
}

func (d *Diskv) uncacheWithLock(key string, sz uint64) {
	d.cacheSize -= sz
	delete(d.cache, key)
}

// pruneDirsWithLock deletes empty directories in the path walk leading to the
// key k. Typically this function is called after an Erase is made.
func (d *Diskv) pruneDirsWithLock(key string) error {
	pathlist := d.transform(key).Path
	for i := range pathlist {
		dir := filepath.Join(d.BasePath, filepath.Join(pathlist[:len(pathlist)-i]...))

		// thanks to Steven Blenkinsop for this snippet
		switch fi, err := os.Stat(dir); true {
		case err != nil:
			return err
		case !fi.IsDir():
			panic(fmt.Sprintf("corrupt dirstate at %s", dir))
		}

		nlinks, err := filepath.Glob(filepath.Join(dir, "*"))
		if err != nil {
			return err
		} else if len(nlinks) > 0 {
			return nil // has subdirs -- do not prune
		}
		if err = os.Remove(dir); err != nil {
			return err
		}
	}

	return nil
}

// ensureCacheSpaceWithLock deletes entries from the cache in arbitrary order
// until the cache has at least valueSize bytes available.
func (d *Diskv) ensureCacheSpaceWithLock(valueSize uint64) error {
	if valueSize > d.CacheSizeMax {
		return fmt.Errorf("value size (%d bytes) too large for cache (%d bytes)", valueSize, d.CacheSizeMax)
	}

	safe := func() bool { return (d.cacheSize + valueSize) <= d.CacheSizeMax }

	for key, val := range d.cache {
		if safe() {
			break
		}

		d.uncacheWithLock(key, uint64(len(val)))
	}

	if !safe() {
		panic(fmt.Sprintf("%d bytes still won't fit in the cache! (max %d bytes)", valueSize, d.CacheSizeMax))
	}

	return nil
}

// nopWriteCloser wraps an io.Writer and provides a no-op Close method to
// satisfy the io.WriteCloser interface.
type nopWriteCloser struct {
	io.Writer
}

func (wc *nopWriteCloser) Write(p []byte) (int, error) { return wc.Writer.Write(p) }
func (wc *nopWriteCloser) Close() error                { return nil }
```

## File: `go.mod`
```
module github.com/peterbourgon/diskv/v3

go 1.12

require github.com/google/btree v1.0.0
```

## File: `go.sum`
```
github.com/google/btree v1.0.0 h1:0udJVsspx3VBr5FwtLhQQtuAsVc79tTq0ocGIPAU6qo=
github.com/google/btree v1.0.0/go.mod h1:lNA+9X1NB3Zf8V7Ke586lFgjr2dZNuvo3lPJSGZ5JPQ=
```

## File: `import_test.go`
```go
package diskv_test

import (
	"bytes"
	"io/ioutil"
	"os"

	"github.com/peterbourgon/diskv/v3"

	"testing"
)

func TestImportMove(t *testing.T) {
	b := []byte(`0123456789`)
	f, err := ioutil.TempFile("", "temp-test")
	if err != nil {
		t.Fatal(err)
	}
	if _, err := f.Write(b); err != nil {
		t.Fatal(err)
	}
	f.Close()

	d := diskv.New(diskv.Options{
		BasePath: "test-import-move",
	})
	defer d.EraseAll()

	key := "key"

	if err := d.Write(key, []byte(`TBD`)); err != nil {
		t.Fatal(err)
	}

	if err := d.Import(f.Name(), key, true); err != nil {
		t.Fatal(err)
	}

	if _, err := os.Stat(f.Name()); err == nil || !os.IsNotExist(err) {
		t.Errorf("expected temp file to be gone, but err = %v", err)
	}

	if !d.Has(key) {
		t.Errorf("%q not present", key)
	}

	if buf, err := d.Read(key); err != nil || bytes.Compare(b, buf) != 0 {
		t.Errorf("want %q, have %q (err = %v)", string(b), string(buf), err)
	}
}

func TestImportCopy(t *testing.T) {
	b := []byte(`¡åéîòü!`)

	f, err := ioutil.TempFile("", "temp-test")
	if err != nil {
		t.Fatal(err)
	}
	if _, err := f.Write(b); err != nil {
		t.Fatal(err)
	}
	f.Close()

	d := diskv.New(diskv.Options{
		BasePath: "test-import-copy",
	})
	defer d.EraseAll()

	if err := d.Import(f.Name(), "key", false); err != nil {
		t.Fatal(err)
	}

	if _, err := os.Stat(f.Name()); err != nil {
		t.Errorf("expected temp file to remain, but got err = %v", err)
	}
}
```

## File: `index.go`
```go
package diskv

import (
	"sync"

	"github.com/google/btree"
)

// Index is a generic interface for things that can
// provide an ordered list of keys.
type Index interface {
	Initialize(less LessFunction, keys <-chan string)
	Insert(key string)
	Delete(key string)
	Keys(from string, n int) []string
}

// LessFunction is used to initialize an Index of keys in a specific order.
type LessFunction func(string, string) bool

// btreeString is a custom data type that satisfies the BTree Less interface,
// making the strings it wraps sortable by the BTree package.
type btreeString struct {
	s string
	l LessFunction
}

// Less satisfies the BTree.Less interface using the btreeString's LessFunction.
func (s btreeString) Less(i btree.Item) bool {
	return s.l(s.s, i.(btreeString).s)
}

// BTreeIndex is an implementation of the Index interface using google/btree.
type BTreeIndex struct {
	sync.RWMutex
	LessFunction
	*btree.BTree
}

// Initialize populates the BTree tree with data from the keys channel,
// according to the passed less function. It's destructive to the BTreeIndex.
func (i *BTreeIndex) Initialize(less LessFunction, keys <-chan string) {
	i.Lock()
	defer i.Unlock()
	i.LessFunction = less
	i.BTree = rebuild(less, keys)
}

// Insert inserts the given key (only) into the BTree tree.
func (i *BTreeIndex) Insert(key string) {
	i.Lock()
	defer i.Unlock()
	if i.BTree == nil || i.LessFunction == nil {
		panic("uninitialized index")
	}
	i.BTree.ReplaceOrInsert(btreeString{s: key, l: i.LessFunction})
}

// Delete removes the given key (only) from the BTree tree.
func (i *BTreeIndex) Delete(key string) {
	i.Lock()
	defer i.Unlock()
	if i.BTree == nil || i.LessFunction == nil {
		panic("uninitialized index")
	}
	i.BTree.Delete(btreeString{s: key, l: i.LessFunction})
}

// Keys yields a maximum of n keys in order. If the passed 'from' key is empty,
// Keys will return the first n keys. If the passed 'from' key is non-empty, the
// first key in the returned slice will be the key that immediately follows the
// passed key, in key order.
func (i *BTreeIndex) Keys(from string, n int) []string {
	i.RLock()
	defer i.RUnlock()

	if i.BTree == nil || i.LessFunction == nil {
		panic("uninitialized index")
	}

	if i.BTree.Len() <= 0 {
		return []string{}
	}

	btreeFrom := btreeString{s: from, l: i.LessFunction}
	skipFirst := true
	if len(from) <= 0 || !i.BTree.Has(btreeFrom) {
		// no such key, so fabricate an always-smallest item
		btreeFrom = btreeString{s: "", l: func(string, string) bool { return true }}
		skipFirst = false
	}

	keys := []string{}
	iterator := func(i btree.Item) bool {
		keys = append(keys, i.(btreeString).s)
		return len(keys) < n
	}
	i.BTree.AscendGreaterOrEqual(btreeFrom, iterator)

	if skipFirst && len(keys) > 0 {
		keys = keys[1:]
	}

	return keys
}

// rebuildIndex does the work of regenerating the index
// with the given keys.
func rebuild(less LessFunction, keys <-chan string) *btree.BTree {
	tree := btree.New(2)
	for key := range keys {
		tree.ReplaceOrInsert(btreeString{s: key, l: less})
	}
	return tree
}
```

## File: `index_test.go`
```go
package diskv

import (
	"bytes"
	"reflect"
	"testing"
	"time"
)

func strLess(a, b string) bool { return a < b }

func cmpStrings(a, b []string) bool {
	if len(a) != len(b) {
		return false
	}
	for i := 0; i < len(a); i++ {
		if a[i] != b[i] {
			return false
		}
	}
	return true
}

func (d *Diskv) isIndexed(key string) bool {
	if d.Index == nil {
		return false
	}

	for _, got := range d.Index.Keys("", 1000) {
		if got == key {
			return true
		}
	}
	return false
}

func TestIndexOrder(t *testing.T) {
	d := New(Options{
		BasePath:     "index-test",
		CacheSizeMax: 1024,
		Index:        &BTreeIndex{},
		IndexLess:    strLess,
	})
	defer d.EraseAll()

	v := []byte{'1', '2', '3'}
	d.Write("a", v)
	if !d.isIndexed("a") {
		t.Fatalf("'a' not indexed after write")
	}
	d.Write("1", v)
	d.Write("m", v)
	d.Write("-", v)
	d.Write("A", v)

	expectedKeys := []string{"-", "1", "A", "a", "m"}
	keys := []string{}
	for _, key := range d.Index.Keys("", 100) {
		keys = append(keys, key)
	}

	if !cmpStrings(keys, expectedKeys) {
		t.Fatalf("got %s, expected %s", keys, expectedKeys)
	}
}

func TestIndexLoad(t *testing.T) {
	d1 := New(Options{
		BasePath:     "index-test",
		CacheSizeMax: 1024,
	})
	defer d1.EraseAll()

	val := []byte{'1', '2', '3'}
	keys := []string{"a", "b", "c", "d", "e", "f", "g"}
	for _, key := range keys {
		d1.Write(key, val)
	}

	d2 := New(Options{
		BasePath:     "index-test",
		CacheSizeMax: 1024,
		Index:        &BTreeIndex{},
		IndexLess:    strLess,
	})
	defer d2.EraseAll()

	// check d2 has properly loaded existing d1 data
	for _, key := range keys {
		if !d2.isIndexed(key) {
			t.Fatalf("key '%s' not indexed on secondary", key)
		}
	}

	// cache one
	if readValue, err := d2.Read(keys[0]); err != nil {
		t.Fatalf("%s", err)
	} else if bytes.Compare(val, readValue) != 0 {
		t.Fatalf("%s: got %s, expected %s", keys[0], readValue, val)
	}

	// make sure it got cached
	for i := 0; i < 10 && !d2.isCached(keys[0]); i++ {
		time.Sleep(10 * time.Millisecond)
	}
	if !d2.isCached(keys[0]) {
		t.Fatalf("key '%s' not cached", keys[0])
	}

	// kill the disk
	d1.EraseAll()

	// cached value should still be there in the second
	if readValue, err := d2.Read(keys[0]); err != nil {
		t.Fatalf("%s", err)
	} else if bytes.Compare(val, readValue) != 0 {
		t.Fatalf("%s: got %s, expected %s", keys[0], readValue, val)
	}

	// but not in the original
	if _, err := d1.Read(keys[0]); err == nil {
		t.Fatalf("expected error reading from flushed store")
	}
}

func TestIndexKeysEmptyFrom(t *testing.T) {
	d := New(Options{
		BasePath:     "index-test",
		CacheSizeMax: 1024,
		Index:        &BTreeIndex{},
		IndexLess:    strLess,
	})
	defer d.EraseAll()

	for _, k := range []string{"a", "c", "z", "b", "x", "b", "y"} {
		d.Write(k, []byte("1"))
	}

	want := []string{"a", "b", "c", "x", "y", "z"}
	have := d.Index.Keys("", 99)
	if !reflect.DeepEqual(want, have) {
		t.Errorf("want %v, have %v", want, have)
	}
}

func TestBadKeys(t *testing.T) {
	d := New(Options{
		BasePath:     "index-test",
		CacheSizeMax: 1024,
		Index:        &BTreeIndex{},
		IndexLess:    strLess,
	})
	defer d.EraseAll()

	for _, k := range []string{"a/a"} {
		err := d.Write(k, []byte("1"))
		if err != errBadKey {
			t.Errorf("Expected bad key error, got: %v", err)
		}
	}
}
```

## File: `issues_test.go`
```go
package diskv

import (
	"bytes"
	"io/ioutil"
	"math/rand"
	"sync"
	"testing"
	"time"
)

// ReadStream from cache shouldn't panic on a nil dereference from a nonexistent
// Compression :)
func TestIssue2A(t *testing.T) {
	d := New(Options{
		BasePath:     "test-issue-2a",
		CacheSizeMax: 1024,
	})
	defer d.EraseAll()

	input := "abcdefghijklmnopqrstuvwxy"
	key, writeBuf, sync := "a", bytes.NewBufferString(input), false
	if err := d.WriteStream(key, writeBuf, sync); err != nil {
		t.Fatal(err)
	}

	for i := 0; i < 2; i++ {
		began := time.Now()
		rc, err := d.ReadStream(key, false)
		if err != nil {
			t.Fatal(err)
		}
		buf, err := ioutil.ReadAll(rc)
		if err != nil {
			t.Fatal(err)
		}
		if !cmpBytes(buf, []byte(input)) {
			t.Fatalf("read #%d: '%s' != '%s'", i+1, string(buf), input)
		}
		rc.Close()
		t.Logf("read #%d in %s", i+1, time.Since(began))
	}
}

// ReadStream on a key that resolves to a directory should return an error.
func TestIssue2B(t *testing.T) {
	blockTransform := func(s string) []string {
		transformBlockSize := 3
		sliceSize := len(s) / transformBlockSize
		pathSlice := make([]string, sliceSize)
		for i := 0; i < sliceSize; i++ {
			from, to := i*transformBlockSize, (i*transformBlockSize)+transformBlockSize
			pathSlice[i] = s[from:to]
		}
		return pathSlice
	}

	d := New(Options{
		BasePath:     "test-issue-2b",
		Transform:    blockTransform,
		CacheSizeMax: 0,
	})
	defer d.EraseAll()

	v := []byte{'1', '2', '3'}
	if err := d.Write("abcabc", v); err != nil {
		t.Fatal(err)
	}

	_, err := d.ReadStream("abc", false)
	if err == nil {
		t.Fatal("ReadStream('abc') should return error")
	}
	t.Logf("ReadStream('abc') returned error: %v", err)
}

// Ensure ReadStream with direct=true isn't racy.
func TestIssue17(t *testing.T) {
	var (
		basePath = "test-data"
	)

	dWrite := New(Options{
		BasePath:     basePath,
		CacheSizeMax: 0,
	})
	defer dWrite.EraseAll()

	dRead := New(Options{
		BasePath:     basePath,
		CacheSizeMax: 50,
	})

	cases := map[string]string{
		"a": `1234567890`,
		"b": `2345678901`,
		"c": `3456789012`,
		"d": `4567890123`,
		"e": `5678901234`,
	}

	for k, v := range cases {
		if err := dWrite.Write(k, []byte(v)); err != nil {
			t.Fatalf("during write: %s", err)
		}
		dRead.Read(k) // ensure it's added to cache
	}

	var wg sync.WaitGroup
	start := make(chan struct{})
	for k, v := range cases {
		wg.Add(1)
		go func(k, v string) {
			<-start
			dRead.ReadStream(k, true)
			wg.Done()
		}(k, v)
	}
	close(start)
	wg.Wait()
}

// Test for issue #40, where acquiring two stream readers on the same k/v pair
// caused the value to be written into the cache twice, messing up the
// size calculations.
func TestIssue40(t *testing.T) {
	var (
		basePath = "test-data"
	)
	// Simplest transform function: put all the data files into the base dir.
	flatTransform := func(s string) []string { return []string{} }

	// Initialize a new diskv store, rooted at "my-data-dir",
	// with a 100 byte cache.
	d := New(Options{
		BasePath:     basePath,
		Transform:    flatTransform,
		CacheSizeMax: 100,
	})

	defer d.EraseAll()

	// Write a 50 byte value, filling the cache half-way
	k1 := "key1"
	d1 := make([]byte, 50)
	rand.Read(d1)
	d.Write(k1, d1)

	// Get *two* read streams on it. Because the key is not yet in the cache,
	// and will not be in the cache until a stream is fully read, both
	// readers use the 'siphon' object, which always writes to the cache
	// after reading.
	s1, err := d.ReadStream(k1, false)
	if err != nil {
		t.Fatal(err)
	}
	s2, err := d.ReadStream(k1, false)
	if err != nil {
		t.Fatal(err)
	}
	// When each stream is drained, the underlying siphon will write
	// the value into the cache's map and increment the cache size.
	// This means we will have 1 entry in the cache map
	// ("key1" mapping to a 50 byte slice) but the cache size will be 100,
	// because the buggy code does not check if an entry already exists
	// in the map.
	// s1 drains:
	//   cache[k] = v
	//   cacheSize += len(v)
	// s2 drains:
	//   cache[k] = v /* overwrites existing */
	//   cacheSize += len(v) /* blindly adds to the cache size */
	ioutil.ReadAll(s1)
	ioutil.ReadAll(s2)

	// Now write a different k/v pair, with a 60 byte array.
	k2 := "key2"
	d2 := make([]byte, 60)
	rand.Read(d2)
	d.Write(k2, d2)
	// The act of reading the k/v pair back out causes it to be cached.
	// Because the cache is only 100 bytes, it needs to delete existing
	// entries to make room.
	// If the cache is buggy, it will delete the single 50-byte entry
	// from the cache map & decrement cacheSize by 50... but because
	// cacheSize was improperly incremented twice earlier, this will
	// leave us with no entries in the cacheMap but with cacheSize==50.
	// Since CacheSizeMax-cacheSize (100-50) is less than 60, there
	// is no room in the cache for this entry and it panics.
	d.Read(k2)
}
```

## File: `keys_test.go`
```go
package diskv

import (
	"reflect"
	"runtime"
	"strings"
	"testing"
)

var (
	keysTestData = map[string]string{
		"ab01cd01": "When we started building CoreOS",
		"ab01cd02": "we looked at all the various components available to us",
		"ab01cd03": "re-using the best tools",
		"ef01gh04": "and building the ones that did not exist",
		"ef02gh05": "We believe strongly in the Unix philosophy",
		"xxxxxxxx": "tools should be independently useful",
	}

	prefixes = []string{
		"", // all
		"a",
		"ab",
		"ab0",
		"ab01",
		"ab01cd0",
		"ab01cd01",
		"ab01cd01x", // none
		"b",         // none
		"b0",        // none
		"0",         // none
		"01",        // none
		"e",
		"ef",
		"efx", // none
		"ef01gh0",
		"ef01gh04",
		"ef01gh05",
		"ef01gh06", // none
	}
)

func TestKeysFlat(t *testing.T) {
	transform := func(s string) []string {
		if s == "" {
			t.Fatalf(`transform should not be called with ""`)
		}
		return []string{}
	}
	d := New(Options{
		BasePath:  "test-data",
		Transform: transform,
	})
	defer d.EraseAll()

	for k, v := range keysTestData {
		d.Write(k, []byte(v))
	}

	checkKeys(t, d.Keys(nil), keysTestData)
}

func TestKeysNested(t *testing.T) {
	d := New(Options{
		BasePath:  "test-data",
		Transform: blockTransform(2),
	})
	defer d.EraseAll()

	for k, v := range keysTestData {
		d.Write(k, []byte(v))
	}

	checkKeys(t, d.Keys(nil), keysTestData)
}

func TestKeysPrefixFlat(t *testing.T) {
	d := New(Options{
		BasePath: "test-data",
	})
	defer d.EraseAll()

	for k, v := range keysTestData {
		d.Write(k, []byte(v))
	}

	for _, prefix := range prefixes {
		checkKeys(t, d.KeysPrefix(prefix, nil), filterPrefix(keysTestData, prefix))
	}
}

func TestKeysPrefixNested(t *testing.T) {
	d := New(Options{
		BasePath:  "test-data",
		Transform: blockTransform(2),
	})
	defer d.EraseAll()

	for k, v := range keysTestData {
		d.Write(k, []byte(v))
	}

	for _, prefix := range prefixes {
		checkKeys(t, d.KeysPrefix(prefix, nil), filterPrefix(keysTestData, prefix))
	}
}

func TestKeysCancel(t *testing.T) {
	d := New(Options{
		BasePath: "test-data",
	})
	defer d.EraseAll()

	for k, v := range keysTestData {
		d.Write(k, []byte(v))
	}

	var (
		cancel      = make(chan struct{})
		received    = 0
		cancelAfter = len(keysTestData) / 2
	)

	for key := range d.Keys(cancel) {
		received++

		if received >= cancelAfter {
			close(cancel)
			runtime.Gosched() // allow walker to detect cancel
		}

		t.Logf("received %d: %q", received, key)
	}

	if want, have := cancelAfter, received; want != have {
		t.Errorf("want %d, have %d", want, have)
	}
}

func checkKeys(t *testing.T, c <-chan string, want map[string]string) {
	for k := range c {
		if _, ok := want[k]; !ok {
			t.Errorf("%q yielded but not expected", k)
			continue
		}

		delete(want, k)
		t.Logf("%q yielded OK", k)
	}

	if len(want) != 0 {
		t.Errorf("%d expected key(s) not yielded: %s", len(want), strings.Join(flattenKeys(want), ", "))
	}
}

func blockTransform(blockSize int) func(string) []string {
	return func(s string) []string {
		var (
			sliceSize = len(s) / blockSize
			pathSlice = make([]string, sliceSize)
		)
		for i := 0; i < sliceSize; i++ {
			from, to := i*blockSize, (i*blockSize)+blockSize
			pathSlice[i] = s[from:to]
		}
		return pathSlice
	}
}

func filterPrefix(in map[string]string, prefix string) map[string]string {
	out := map[string]string{}
	for k, v := range in {
		if strings.HasPrefix(k, prefix) {
			out[k] = v
		}
	}
	return out
}

func TestFilterPrefix(t *testing.T) {
	input := map[string]string{
		"all":        "",
		"and":        "",
		"at":         "",
		"available":  "",
		"best":       "",
		"building":   "",
		"components": "",
		"coreos":     "",
		"did":        "",
		"exist":      "",
		"looked":     "",
		"not":        "",
		"ones":       "",
		"re-using":   "",
		"started":    "",
		"that":       "",
		"the":        "",
		"to":         "",
		"tools":      "",
		"us":         "",
		"various":    "",
		"we":         "",
		"when":       "",
	}

	for prefix, want := range map[string]map[string]string{
		"a":    map[string]string{"all": "", "and": "", "at": "", "available": ""},
		"al":   map[string]string{"all": ""},
		"all":  map[string]string{"all": ""},
		"alll": map[string]string{},
		"c":    map[string]string{"components": "", "coreos": ""},
		"co":   map[string]string{"components": "", "coreos": ""},
		"com":  map[string]string{"components": ""},
	} {
		have := filterPrefix(input, prefix)
		if !reflect.DeepEqual(want, have) {
			t.Errorf("%q: want %v, have %v", prefix, flattenKeys(want), flattenKeys(have))
		}
	}
}

func flattenKeys(m map[string]string) []string {
	a := make([]string, 0, len(m))
	for k := range m {
		a = append(a, k)
	}
	return a
}
```

## File: `speed_test.go`
```go
package diskv

import (
	"fmt"
	"math/rand"
	"testing"
)

func shuffle(keys []string) {
	ints := rand.Perm(len(keys))
	for i := range keys {
		keys[i], keys[ints[i]] = keys[ints[i]], keys[i]
	}
}

func genValue(size int) []byte {
	v := make([]byte, size)
	for i := 0; i < size; i++ {
		v[i] = uint8((rand.Int() % 26) + 97) // a-z
	}
	return v
}

const (
	keyCount = 1000
)

func genKeys() []string {
	keys := make([]string, keyCount)
	for i := 0; i < keyCount; i++ {
		keys[i] = fmt.Sprintf("%d", i)
	}
	return keys
}

func (d *Diskv) load(keys []string, val []byte) {
	for _, key := range keys {
		d.Write(key, val)
	}
}

func benchRead(b *testing.B, size, cachesz int) {
	b.StopTimer()
	d := New(Options{
		BasePath:     "speed-test",
		CacheSizeMax: uint64(cachesz),
	})
	defer d.EraseAll()

	keys := genKeys()
	value := genValue(size)
	d.load(keys, value)
	shuffle(keys)
	b.SetBytes(int64(size))

	b.StartTimer()
	for i := 0; i < b.N; i++ {
		_, _ = d.Read(keys[i%len(keys)])
	}
	b.StopTimer()
}

func benchWrite(b *testing.B, size int, withIndex bool) {
	b.StopTimer()

	options := Options{
		BasePath:     "speed-test",
		CacheSizeMax: 0,
	}
	if withIndex {
		options.Index = &BTreeIndex{}
		options.IndexLess = strLess
	}

	d := New(options)
	defer d.EraseAll()
	keys := genKeys()
	value := genValue(size)
	shuffle(keys)
	b.SetBytes(int64(size))

	b.StartTimer()
	for i := 0; i < b.N; i++ {
		d.Write(keys[i%len(keys)], value)
	}
	b.StopTimer()
}

func BenchmarkWrite__32B_NoIndex(b *testing.B) {
	benchWrite(b, 32, false)
}

func BenchmarkWrite__1KB_NoIndex(b *testing.B) {
	benchWrite(b, 1024, false)
}

func BenchmarkWrite__4KB_NoIndex(b *testing.B) {
	benchWrite(b, 4096, false)
}

func BenchmarkWrite_10KB_NoIndex(b *testing.B) {
	benchWrite(b, 10240, false)
}

func BenchmarkWrite__32B_WithIndex(b *testing.B) {
	benchWrite(b, 32, true)
}

func BenchmarkWrite__1KB_WithIndex(b *testing.B) {
	benchWrite(b, 1024, true)
}

func BenchmarkWrite__4KB_WithIndex(b *testing.B) {
	benchWrite(b, 4096, true)
}

func BenchmarkWrite_10KB_WithIndex(b *testing.B) {
	benchWrite(b, 10240, true)
}

func BenchmarkRead__32B_NoCache(b *testing.B) {
	benchRead(b, 32, 0)
}

func BenchmarkRead__1KB_NoCache(b *testing.B) {
	benchRead(b, 1024, 0)
}

func BenchmarkRead__4KB_NoCache(b *testing.B) {
	benchRead(b, 4096, 0)
}

func BenchmarkRead_10KB_NoCache(b *testing.B) {
	benchRead(b, 10240, 0)
}

func BenchmarkRead__32B_WithCache(b *testing.B) {
	benchRead(b, 32, keyCount*32*2)
}

func BenchmarkRead__1KB_WithCache(b *testing.B) {
	benchRead(b, 1024, keyCount*1024*2)
}

func BenchmarkRead__4KB_WithCache(b *testing.B) {
	benchRead(b, 4096, keyCount*4096*2)
}

func BenchmarkRead_10KB_WithCache(b *testing.B) {
	benchRead(b, 10240, keyCount*4096*2)
}
```

## File: `stream_test.go`
```go
package diskv

import (
	"bytes"
	"io/ioutil"
	"testing"
)

func TestBasicStreamCaching(t *testing.T) {
	d := New(Options{
		BasePath:     "test-data",
		CacheSizeMax: 1024,
	})
	defer d.EraseAll()

	input := "a1b2c3"
	key, writeBuf, sync := "a", bytes.NewBufferString(input), true
	if err := d.WriteStream(key, writeBuf, sync); err != nil {
		t.Fatal(err)
	}

	if d.isCached(key) {
		t.Fatalf("'%s' cached, but shouldn't be (yet)", key)
	}

	rc, err := d.ReadStream(key, false)
	if err != nil {
		t.Fatal(err)
	}

	readBuf, err := ioutil.ReadAll(rc)
	if err != nil {
		t.Fatal(err)
	}

	if !cmpBytes(readBuf, []byte(input)) {
		t.Fatalf("'%s' != '%s'", string(readBuf), input)
	}

	if !d.isCached(key) {
		t.Fatalf("'%s' isn't cached, but should be", key)
	}
}

func TestReadStreamDirect(t *testing.T) {
	var (
		basePath = "test-data"
	)
	dWrite := New(Options{
		BasePath:     basePath,
		CacheSizeMax: 0,
	})
	defer dWrite.EraseAll()
	dRead := New(Options{
		BasePath:     basePath,
		CacheSizeMax: 1024,
	})

	// Write
	key, val1, val2 := "a", []byte(`1234567890`), []byte(`aaaaaaaaaa`)
	if err := dWrite.Write(key, val1); err != nil {
		t.Fatalf("during first write: %s", err)
	}

	// First, caching read.
	val, err := dRead.Read(key)
	if err != nil {
		t.Fatalf("during initial read: %s", err)
	}
	t.Logf("read 1: %s => %s", key, string(val))
	if !cmpBytes(val1, val) {
		t.Errorf("expected %q, got %q", string(val1), string(val))
	}
	if !dRead.isCached(key) {
		t.Errorf("%q should be cached, but isn't", key)
	}

	// Write a different value.
	if err := dWrite.Write(key, val2); err != nil {
		t.Fatalf("during second write: %s", err)
	}

	// Second read, should hit cache and get the old value.
	val, err = dRead.Read(key)
	if err != nil {
		t.Fatalf("during second (cache-hit) read: %s", err)
	}
	t.Logf("read 2: %s => %s", key, string(val))
	if !cmpBytes(val1, val) {
		t.Errorf("expected %q, got %q", string(val1), string(val))
	}

	// Third, direct read, should get the updated value.
	rc, err := dRead.ReadStream(key, true)
	if err != nil {
		t.Fatalf("during third (direct) read, ReadStream: %s", err)
	}
	defer rc.Close()
	val, err = ioutil.ReadAll(rc)
	if err != nil {
		t.Fatalf("during third (direct) read, ReadAll: %s", err)
	}
	t.Logf("read 3: %s => %s", key, string(val))
	if !cmpBytes(val2, val) {
		t.Errorf("expected %q, got %q", string(val1), string(val))
	}

	// Fourth read, should hit cache and get the new value.
	val, err = dRead.Read(key)
	if err != nil {
		t.Fatalf("during fourth (cache-hit) read: %s", err)
	}
	t.Logf("read 4: %s => %s", key, string(val))
	if !cmpBytes(val2, val) {
		t.Errorf("expected %q, got %q", string(val1), string(val))
	}
}
```

## File: `examples/advanced-transform/advanced-transform.go`
```go
package main

import (
	"fmt"
	"strings"

	"github.com/peterbourgon/diskv/v3"
)

func AdvancedTransformExample(key string) *diskv.PathKey {
	path := strings.Split(key, "/")
	last := len(path) - 1
	return &diskv.PathKey{
		Path:     path[:last],
		FileName: path[last] + ".txt",
	}
}

// If you provide an AdvancedTransform, you must also provide its
// inverse:

func InverseTransformExample(pathKey *diskv.PathKey) (key string) {
	txt := pathKey.FileName[len(pathKey.FileName)-4:]
	if txt != ".txt" {
		panic("Invalid file found in storage folder!")
	}
	return strings.Join(pathKey.Path, "/") + pathKey.FileName[:len(pathKey.FileName)-4]
}

func main() {
	d := diskv.New(diskv.Options{
		BasePath:          "my-data-dir",
		AdvancedTransform: AdvancedTransformExample,
		InverseTransform:  InverseTransformExample,
		CacheSizeMax:      1024 * 1024,
	})
	// Write some text to the key "alpha/beta/gamma".
	key := "alpha/beta/gamma"
	d.WriteString(key, "¡Hola!") // will be stored in "<basedir>/alpha/beta/gamma.txt"
	fmt.Println(d.ReadString("alpha/beta/gamma"))
}
```

## File: `examples/content-addressable-store/cas.go`
```go
package main

import (
	"crypto/md5"
	"fmt"
	"io"

	"github.com/peterbourgon/diskv/v3"
)

const transformBlockSize = 2 // grouping of chars per directory depth

func blockTransform(s string) []string {
	var (
		sliceSize = len(s) / transformBlockSize
		pathSlice = make([]string, sliceSize)
	)
	for i := 0; i < sliceSize; i++ {
		from, to := i*transformBlockSize, (i*transformBlockSize)+transformBlockSize
		pathSlice[i] = s[from:to]
	}
	return pathSlice
}

func main() {
	d := diskv.New(diskv.Options{
		BasePath:     "data",
		Transform:    blockTransform,
		CacheSizeMax: 1024 * 1024, // 1MB
	})

	for _, valueStr := range []string{
		"I am the very model of a modern Major-General",
		"I've information vegetable, animal, and mineral",
		"I know the kings of England, and I quote the fights historical",
		"From Marathon to Waterloo, in order categorical",
		"I'm very well acquainted, too, with matters mathematical",
		"I understand equations, both the simple and quadratical",
		"About binomial theorem I'm teeming with a lot o' news",
		"With many cheerful facts about the square of the hypotenuse",
	} {
		d.Write(md5sum(valueStr), []byte(valueStr))
	}

	var keyCount int
	for key := range d.Keys(nil) {
		val, err := d.Read(key)
		if err != nil {
			panic(fmt.Sprintf("key %s had no value", key))
		}
		fmt.Printf("%s: %s\n", key, val)
		keyCount++
	}
	fmt.Printf("%d total keys\n", keyCount)

	// d.EraseAll() // leave it commented out to see how data is kept on disk
}

func md5sum(s string) string {
	h := md5.New()
	io.WriteString(h, s)
	return fmt.Sprintf("%x", h.Sum(nil))
}
```

## File: `examples/git-like-store/git-like-store.go`
```go
package main

/* This example uses a more advanced transform function that simulates a bit
 how Git stores objects:

* places hash-like keys under the objects directory
* any other key is placed in the base directory. If the key
* contains slashes, these are converted to subdirectories

*/

import (
	"fmt"
	"regexp"
	"strings"

	"github.com/peterbourgon/diskv/v3"
)

var hex40 = regexp.MustCompile("[0-9a-fA-F]{40}")

func hexTransform(s string) *diskv.PathKey {
	if hex40.MatchString(s) {
		return &diskv.PathKey{Path: []string{"objects", s[0:2]},
			FileName: s,
		}
	}

	folders := strings.Split(s, "/")
	lfolders := len(folders)
	if lfolders > 1 {
		return &diskv.PathKey{Path: folders[:lfolders-1],
			FileName: folders[lfolders-1],
		}
	}

	return &diskv.PathKey{Path: []string{},
		FileName: s,
	}
}

func hexInverseTransform(pathKey *diskv.PathKey) string {
	if hex40.MatchString(pathKey.FileName) {
		return pathKey.FileName
	}

	if len(pathKey.Path) == 0 {
		return pathKey.FileName
	}

	return strings.Join(pathKey.Path, "/") + "/" + pathKey.FileName
}

func main() {
	d := diskv.New(diskv.Options{
		BasePath:          "my-data-dir",
		AdvancedTransform: hexTransform,
		InverseTransform:  hexInverseTransform,
		CacheSizeMax:      1024 * 1024,
	})

	// Write some text to the key "alpha/beta/gamma".
	key := "1bd88421b055327fcc8660c76c4894c4ea4c95d7"
	d.WriteString(key, "¡Hola!") // will be stored in "<basedir>/objects/1b/1bd88421b055327fcc8660c76c4894c4ea4c95d7"

	d.WriteString("refs/heads/master", "some text") // will be stored in "<basedir>/refs/heads/master"

	fmt.Println("Enumerating All keys:")
	c := d.Keys(nil)

	for key := range c {
		value := d.ReadString(key)
		fmt.Printf("Key: %s, Value: %s\n", key, value)
	}
}
```

## File: `examples/super-simple-store/super-simple-store.go`
```go
package main

import (
	"fmt"

	"github.com/peterbourgon/diskv/v3"
)

func main() {
	d := diskv.New(diskv.Options{
		BasePath:     "my-diskv-data-directory",
		CacheSizeMax: 1024 * 1024, // 1MB
	})

	key := "alpha"
	if err := d.Write(key, []byte{'1', '2', '3'}); err != nil {
		panic(err)
	}

	value, err := d.Read(key)
	if err != nil {
		panic(err)
	}
	fmt.Printf("%v\n", value)

	if err := d.Erase(key); err != nil {
		panic(err)
	}
}
```

