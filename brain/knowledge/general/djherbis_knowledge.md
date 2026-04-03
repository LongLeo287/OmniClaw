---
id: djherbis-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:20.353928
---

# KNOWLEDGE EXTRACT: djherbis
> **Extracted on:** 2026-03-30 17:35:58
> **Source:** djherbis

---

## File: `buffer.md`
```markdown
# 📦 djherbis/buffer [🔖 PENDING/APPROVE]
🔗 https://github.com/djherbis/buffer


## Meta
- **Stars:** ⭐ 553 | **Forks:** 🍴 27
- **Language:** Go | **License:** MIT
- **Last updated:** 2026-03-09
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Composable Buffers for Go #golang

## README (trích đầu)
```
Buffer 
==========

[![GoDoc](https://godoc.org/github.com/djherbis/buffer?status.svg)](https://godoc.org/github.com/djherbis/buffer)
[![Release](https://img.shields.io/github/release/djherbis/buffer.svg)](https://github.com/djherbis/buffer/releases/latest)
[![Software License](https://img.shields.io/badge/license-MIT-brightgreen.svg)](LICENSE.txt)
[![go test](https://github.com/djherbis/buffer/actions/workflows/go-test.yml/badge.svg)](https://github.com/djherbis/buffer/actions/workflows/go-test.yml)
[![Coverage Status](https://coveralls.io/repos/djherbis/buffer/badge.svg?branch=master)](https://coveralls.io/r/djherbis/buffer?branch=master)
[![Go Report Card](https://goreportcard.com/badge/github.com/djherbis/buffer)](https://goreportcard.com/report/github.com/djherbis/buffer)

Usage
------------

The following buffers provide simple unique behaviours which when composed can create complex buffering strategies. For use with github.com/djherbis/nio for Buffered io.Pipe and io.Copy implementations.

For example: 

```go
import (
  "github.com/djherbis/buffer"
  "github.com/djherbis/nio"
  
  "io/ioutil"
)

// Buffer 32KB to Memory, after that buffer to 100MB chunked files
buf := buffer.NewUnboundedBuffer(32*1024, 100*1024*1024)
nio.Copy(w, r, buf) // Reads from r, writes to buf, reads from buf writes to w (concurrently).

// Buffer 32KB to Memory, discard overflow
buf = buffer.NewSpill(32*1024, ioutil.Discard)
nio.Copy(w, r, buf)
```

Supported Buffers
------------

#### Bounded Buffers ####

Memory: Wrapper for bytes.Buffer

File: File-based buffering. The file never exceeds Cap() in length, no matter how many times its written/read from. It accomplishes this by "wrapping" around the fixed max-length file when the data gets too long but there is available freed space at the beginning of the file. The caller is responsible for closing and deleting the file when done.

```go
import (
  "ioutil"
  "os"
  
  "github.com/djherbis/buffer"
)

// Create a File-based Buffer with max size 100MB
file, err := ioutil.TempFile("", "buffer")
if err != nil {
	return err
}
defer os.Remove(file.Name())
defer file.Close()

buf := buffer.NewFile(100*1024*1024, file)

// A simpler way:
pool := buffer.NewFilePool(100*1024*1024, "") // "" -- use temp dir
buf, err := pool.Get()   // allocate the buffer
if err != nil {
  return err
}
defer pool.Put(buf) // close and remove the allocated file for the buffer

```

Multi: A fixed length linked-list of buffers. Each buffer reads from the next buffer so that all the buffered data is shifted upwards in the list when reading. Writes are always written to the first buffer in the list whose Len() < Cap().

```go
import (
  "github.com/djherbis/buffer"
)

mem  := buffer.New(32*1024)
file := buffer.NewFile(100*1024*1024, someFileObj)) // you'll need to manage Open(), Close() and Delete someFileObj

// Buffer composed of 32KB of memory, and 100MB of file.
buf := buffer.NewMulti(mem, file)
```

#### Unbounded Buffers ####

Partition: 
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

