---
id: lrucache
type: knowledge
owner: OA_Triage
---
# lrucache
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
LruCache [![Build Status](https://github.com/die-net/lrucache/actions/workflows/go-test.yml/badge.svg)](https://github.com/die-net/lrucache/actions/workflows/go-test.yml) [![Coverage Status](https://coveralls.io/repos/github/die-net/lrucache/badge.svg?branch=main)](https://coveralls.io/github/die-net/lrucache?branch=main) [![Go Report Card](https://goreportcard.com/badge/github.com/die-net/lrucache)](https://goreportcard.com/report/github.com/die-net/lrucache)
========

## This project is now archived, since `httpcache.Cache` is itself archived, and I haven't used this in years.

---

LruCache is a thread-safe, in-memory [httpcache.Cache](https://github.com/gregjones/httpcache) implementation that evicts the least recently used entries when a byte size limit or optional max age would be exceeded.

Using the included [TwoTier](https://github.com/die-net/lrucache/tree/main/twotier) wrapper, it could also be used as a small and fast cache for popular objects, falling back to a larger and slower cache (such as [s3cache](https://github.com/sourcegraph/s3cache)) for less popular ones.

Also see the godoc API documentation for [LruCache](https://godoc.org/github.com/die-net/lrucache) or [TwoTier](https://godoc.org/github.com/die-net/lrucache/twotier).

Included are a test suite with close to 100% test coverage and a parallel benchmark suite that shows individual Set, Get, and Delete operations take under 400ns to complete.

License
-------

Copyright 2016 Aaron Hopkins and contributors

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at: http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.

```

### File: lrucache.go
```go
// Package lrucache provides a byte-size-limited implementation of
// httpcache.Cache that stores data in memory.
package lrucache

import (
	"container/list"
	"sync"
	"time"
)

// LruCache is a thread-safe, in-memory httpcache.Cache that evicts the
// least recently used entries from memory when either MaxSize (in bytes)
// limit would be exceeded or (if set) the entries are older than MaxAge (in
// seconds).  Use the New constructor to create one.
type LruCache struct {
	MaxSize int64
	MaxAge  int64

	mu    sync.Mutex
	cache map[string]*list.Element
	lru   *list.List // Front is least-recent
	size  int64
}

// New creates an LruCache that will restrict itself to maxSize bytes of
// memory.  If maxAge > 0, entries will also be expired after maxAge
// seconds.
func New(maxSize, maxAge int64) *LruCache {
	c := &LruCache{
		MaxSize: maxSize,
		MaxAge:  maxAge,
		lru:     list.New(),
		cache:   make(map[string]*list.Element),
	}

	return c
}

// Get returns the []byte representation of a cached response and a bool
// set to true if the key was found.
func (c *LruCache) Get(key string) ([]byte, bool) {
	c.mu.Lock()

	le, ok := c.cache[key]
	if !ok {
		c.mu.Unlock() // Avoiding defer overhead
		return nil, false
	}

	if c.MaxAge > 0 && le.Value.(*entry).expires <= time.Now().Unix() {
		c.deleteElement(le)
		c.maybeDeleteOldest()

		c.mu.Unlock() // Avoiding defer overhead
		return nil, false
	}

	c.lru.MoveToBack(le)
	value := le.Value.(*entry).value

	c.mu.Unlock() // Avoiding defer overhead
	return value, true
}

// Set stores the []byte representation of a response for a given key.
func (c *LruCache) Set(key string, value []byte) {
	c.mu.Lock()

	expires := int64(0)
	if c.MaxAge > 0 {
		expires = time.Now().Unix() + c.MaxAge
	}

	if le, ok := c.cache[key]; ok {
		c.lru.MoveToBack(le)
		e := le.Value.(*entry)
		c.size += int64(len(value)) - int64(len(e.value))
		e.value = value
		e.expires = expires
	} else {
		e := &entry{key: key, value: value, expires: expires}
		c.cache[key] = c.lru.PushBack(e)
		c.size += e.size()
	}

	c.maybeDeleteOldest()

	c.mu.Unlock()
}

// Delete removes the value associated with a key.
func (c *LruCache) Delete(key string) {
	c.mu.Lock()

	if le, ok := c.cache[key]; ok {
		c.deleteElement(le)
	}

	c.mu.Unlock()
}

// Size returns the estimated current memory usage of LruCache.
func (c *LruCache) Size() int64 {
	c.mu.Lock()
	size := c.size
	c.mu.Unlock()

	return size
}

func (c *LruCache) maybeDeleteOldest() {
	for c.size > c.MaxSize {
		le := c.lru.Front()
		if le == nil {
			panic("LruCache: non-zero size but empty lru")
		}
		c.deleteElement(le)
	}

	if c.MaxAge > 0 {
		now := time.Now().Unix()
		for le := c.lru.Front(); le != nil && le.Value.(*entry).expires <= now; le = c.lru.Front() {
			c.deleteElement(le)
		}
	}
}

func (c *LruCache) deleteElement(le *list.Element) {
	c.lru.Remove(le)
	e := le.Value.(*entry)
	delete(c.cache, e.key)
	c.size -= e.size()
}

// Rough estimate of map + entry object + string + byte slice overheads in bytes.
const entryOverhead = 168

type entry struct {
	key     string
	value   []byte
	expires int64
}

func (e *entry) size() int64 {
	return entryOverhead + int64(len(e.key)) + int64(len(e.value))
}

```

### File: lrucache_test.go
```go
package lrucache

import (
	"math/rand"
	"runtime"
	"strconv"
	"testing"
	"time"

	"github.com/gregjones/httpcache"
	"github.com/stretchr/testify/assert"
)

var entries = []struct {
	key   string
	value string
}{
	{"1", "one"},
	{"2", "two"},
	{"3", "three"},
	{"4", "four"},
	{"5", "five"},
}

func TestInterface(t *testing.T) {
	var h httpcache.Cache = New(1000000, 0)
	if assert.NotNil(t, h) {
		_, ok := h.Get("missing")
		assert.False(t, ok)
	}
}

func TestCache(t *testing.T) {
	c := New(1000000, 0)

	for _, e := range entries {
		c.Set(e.key, []byte(e.value))
	}

	c.Delete("missing")
	_, ok := c.Get("missing")
	assert.False(t, ok)

	for _, e := range entries {
		value, ok := c.Get(e.key)
		if assert.True(t, ok) {
			assert.Equal(t, e.value, string(value))
		}
	}

	for _, e := range entries {
		c.Delete(e.key)

		_, ok := c.Get(e.key)
		assert.False(t, ok)
	}
}

func TestSize(t *testing.T) {
	c := New(1000000, 0)
	assert.Equal(t, int64(0), c.size)

	// Check that size is overhead + len(key) + len(value)
	c.Set("some", []byte("text"))
	assert.Equal(t, int64(entryOverhead+8), c.size)

	// Replace key
	c.Set("some", []byte("longer text"))
	assert.Equal(t, int64(entryOverhead+15), c.size)

	assert.Equal(t, c.size, c.Size())

	c.Delete("some")
	assert.Equal(t, int64(0), c.size)
}

func TestMaxSize(t *testing.T) {
	c := New(entryOverhead*2+20, 0)

	for _, e := range entries {
		c.Set(e.key, []byte(e.value))
	}

	// Make sure only the last two entries were kept.
	assert.Equal(t, int64(entryOverhead*2+10), c.size)
}

func TestMaxAge(t *testing.T) {
	c := New(1000000, 86400)

	now := time.Now().Unix()
	expected := now + 86400

	// Add one expired entry
	c.Set("foo", []byte("bar"))
	c.lru.Back().Value.(*entry).expires = now

	// Set a few and verify expiration times
	for _, s := range entries {
		c.Set(s.key, []byte(s.value))
		e := c.lru.Back().Value.(*entry)
		assert.True(t, e.expires >= expected && e.expires <= expected+10)
	}

	// Make sure we can get them all
	for _, s := range entries {
		_, ok := c.Get(s.key)
		assert.True(t, ok)
	}

	// Make sure only non-expired entries are still in the cache
	assert.Equal(t, int64(entryOverhead*5+24), c.size)

	// Expire all entries
	for _, s := range entries {
		le, ok := c.cache[s.key]
		if assert.True(t, ok) {
			le.Value.(*entry).expires = now
		}
	}

	// Get one expired entry, which should clear all expired entries
	_, ok := c.Get("3")
	assert.False(t, ok)
	assert.Equal(t, int64(0), c.size)
}

func TestRace(t *testing.T) {
	c := New(100000, 0)

	for worker := 0; worker < 8; worker++ {
		go testRaceWorker(c)
	}
}

func testRaceWorker(c *LruCache) {
	v := []byte("value")

	for n := 0; n < 1000; n++ {
		c.Set(randKey(100), v)
		_, _ = c.Get(randKey(200))
		c.Delete(randKey(100))
		_ = c.Size()
	}
}

func TestOverhead(t *testing.T) {
	if testing.Short() || !testing.Verbose() {
		t.SkipNow()
	}

	num := int64(1000000)
	c := New(num*1000, 0)

	mem := readMem()

	for n := 0; int64(n) < num; n++ {
		c.Set(strconv.Itoa(n), []byte(randKey(1000000000)))
	}

	mem = readMem() - mem
	stored := c.Size() - num*entryOverhead
	t.Log("entryOverhead =", (mem-stored)/num)
}

func BenchmarkSet(b *testing.B) {
	v := []byte("value")

	c := benchSetup(b, 10000000, 10000)

	b.RunParallel(func(pb *testing.PB) {
		for pb.Next() {
			c.Set(randKey(10000), v)
		}
	})
}

func BenchmarkGet(b *testing.B) {
	c := benchSetup(b, 10000000, 10000)

	b.RunParallel(func(pb *testing.PB) {
		for pb.Next() {
			_, _ = c.Get(randKey(20000))
		}
	})
}

func BenchmarkSize(b *testing.B) {
	c := benchSetup(b, 10000000, 10000)

	b.RunParallel(func(pb *testing.PB) {
		for pb.Next() {
			_ = c.Size()
		}
	})
}

func BenchmarkSetGetDeleteSize(b *testing.B) {
	v := []byte("value")

	c := benchSetup(b, 10000000, 10000)

	b.RunParallel(func(pb *testing.PB) {
		for pb.Next() {
			c.Set(randKey(10000), v)
			_, _ = c.Get(randKey(20000))
			c.Delete(randKey(10000))
			_ = c.Size()
		}
	})
}

func benchSetup(b *testing.B, size int64, entries int) *LruCache {
	c := New(size, 0)

	v := []byte("value")
	for i := 0; i < entries; i++ {
		c.Set(strconv.Itoa(i), v)
	}

	b.ResetTimer()

	return c
}

func randKey(n int32) string {
	return strconv.Itoa(int(rand.Int31n(n)))
}

func readMem() int64 {
	m := runtime.MemStats{}
	runtime.GC()
	runtime.ReadMemStats(&m)
	return int64(m.Alloc)
}

```

