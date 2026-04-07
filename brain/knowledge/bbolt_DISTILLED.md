---
id: bbolt
type: knowledge
owner: OA_Triage
---
# bbolt
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
bbolt
=====

[![Go Report Card](https://goreportcard.com/badge/go.etcd.io/bbolt?style=flat-square)](https://goreportcard.com/report/go.etcd.io/bbolt)
[![Go Reference](https://pkg.go.dev/badge/go.etcd.io/bbolt.svg)](https://pkg.go.dev/go.etcd.io/bbolt)
[![Releases](https://img.shields.io/github/release/etcd-io/bbolt/all.svg?style=flat-square)](https://github.com/etcd-io/bbolt/releases)
[![LICENSE](https://img.shields.io/github/license/etcd-io/bbolt.svg?style=flat-square)](https://github.com/etcd-io/bbolt/blob/master/LICENSE)

bbolt is a fork of [Ben Johnson's][gh_ben] [Bolt][bolt] key/value
store. The purpose of this fork is to provide the Go community with an active
maintenance and development target for Bolt; the goal is improved reliability
and stability. bbolt includes bug fixes, performance enhancements, and features
not found in Bolt while preserving backwards compatibility with the Bolt API.

Bolt is a pure Go key/value store inspired by [Howard Chu's][hyc_symas]
[LMDB project][lmdb]. The goal of the project is to provide a simple,
fast, and reliable database for projects that don't require a full database
server such as Postgres or MySQL.

Since Bolt is meant to be used as such a low-level piece of functionality,
simplicity is key. The API will be small and only focus on getting values
and setting values. That's it.

[gh_ben]: https://github.com/benbjohnson
[bolt]: https://github.com/boltdb/bolt
[hyc_symas]: https://twitter.com/hyc_symas
[lmdb]: https://www.symas.com/symas-embedded-database-lmdb

## Project Status

Bolt is stable, the API is fixed, and the file format is fixed. Full unit
test coverage and randomized black box testing are used to ensure database
consistency and thread safety. Bolt is currently used in high-load production
environments serving databases as large as 1TB. Many companies such as
Shopify and Heroku use Bolt-backed services every day.

## Project versioning

bbolt uses [semantic versioning](http://semver.org).
API should not change between patch and minor releases.
New minor versions may add additional features to the API.

## Table of Contents

  - [Getting Started](#getting-started)
    - [Installing](#installing)
    - [Opening a database](#opening-a-database)
    - [Transactions](#transactions)
      - [Read-write transactions](#read-write-transactions)
      - [Read-only transactions](#read-only-transactions)
      - [Batch read-write transactions](#batch-read-write-transactions)
      - [Managing transactions manually](#managing-transactions-manually)
    - [Using buckets](#using-buckets)
    - [Using key/value pairs](#using-keyvalue-pairs)
    - [Autoincrementing integer for the bucket](#autoincrementing-integer-for-the-bucket)
    - [Iterating over keys](#iterating-over-keys)
      - [Prefix scans](#prefix-scans)
      - [Range scans](#range-scans)
      - [ForEach()](#foreach)
    - [Nested buckets](#nested-buckets)
    - [Database backups](#database-backups)
    - [Statistics](#statistics)
    - [Read-Only Mode](#read-only-mode)
    - [Mobile Use (iOS/Android)](#mobile-use-iosandroid)
  - [Resources](#resources)
  - [Comparison with other databases](#comparison-with-other-databases)
    - [Postgres, MySQL, & other relational databases](#postgres-mysql--other-relational-databases)
    - [LevelDB, RocksDB](#leveldb-rocksdb)
    - [LMDB](#lmdb)
  - [Caveats & Limitations](#caveats--limitations)
  - [Reading the Source](#reading-the-source)
  - [Known Issues](#known-issues)
  - [Other Projects Using Bolt](#other-projects-using-bolt)

## Getting Started

### Installing

To start using `bbolt`, install Go and run `go get`:
```sh
$ go get go.etcd.io/bbolt@latest
```

This will retrieve the library and update your `go.mod` and `go.sum` files.

To run the command line utility, execute:
```sh
$ go run go.etcd.io/bbolt/cmd/bbolt@latest
```

Run `go install` to install the `bbolt` command line utility into
your `$GOBIN` path, which defaults to `$GOPATH/bin` or `$HOME/go/bin` if the
`GOPATH` environment variable is not set.
```sh
$ go install go.etcd.io/bbolt/cmd/bbolt@latest
```

### Importing bbolt

To use bbolt as an embedded key-value store, import as:

```go
import bolt "go.etcd.io/bbolt"

db, err := bolt.Open(path, 0600, nil)
if err != nil {
  return err
}
defer db.Close()
```


### Opening a database

The top-level object in Bolt is a `DB`. It is represented as a single file on
your disk and represents a consistent snapshot of your data.

To open your database, simply use the `bolt.Open()` function:

```go
package main

import (
	"log"

	bolt "go.etcd.io/bbolt"
)

func main() {
	// Open the my.db data file in your current directory.
	// It will be created if it doesn't exist.
	db, err := bolt.Open("my.db", 0600, nil)
	if err != nil {
		log.Fatal(err)
	}
	defer db.Close()

	...
}
```

Please note that Bolt obtains a file lock on the data file so multiple processes
cannot open the same database at the same time. Opening an already open Bolt
database will cause it to hang until the other process closes it. To prevent
an indefinite wait you can pass a timeout option to the `Open()` function:

```go
db, err := bolt.Open("my.db", 0600, &bolt.Options{Timeout: 1 * time.Second})
```


### Transactions

Bolt allows only one read-write transaction at a time but allows as many
read-only transactions as you want at a time. Each transaction has a consistent
view of the data as it existed when the transaction started.

Individual transactions and all objects created from them (e.g. buckets, keys)
are not thread safe. To work with data in multiple goroutines you must start
a transaction for each one or use locking to ensure only one goroutine accesses
a transaction at a time. Creating transaction from the `DB` is thread safe.

Transactions should not depend on one another and generally shouldn't be opened
simultaneously in the same goroutine. This can cause a deadlock as the read-write
transaction needs to periodically re-map the data file but it cannot do so while
any read-only transaction is open. Even a nested read-only transaction can cause
a deadlock, as the child transaction can block the parent transaction from releasing
its resources.

#### Read-write transactions

To start a read-write transaction, you can use the `DB.Update()` function:

```go
err := db.Update(func(tx *bolt.Tx) error {
	...
	return nil
})
```

Inside the closure, you have a consistent view of the database. You commit the
transaction by returning `nil` at the end. You can also rollback the transaction
at any point by returning an error. All database operations are allowed inside
a read-write transaction.

Always check the return error as it will report any disk failures that can cause
your transaction to not complete. If you return an error within your closure
it will be passed through.


#### Read-only transactions

To start a read-only transaction, you can use the `DB.View()` function:

```go
err := db.View(func(tx *bolt.Tx) error {
	...
	return nil
})
```

You also get a consistent view of the database within this closure, however,
no mutating operations are allowed within a read-only transaction. You can only
retrieve buckets, retrieve values, and copy the database within a read-only
transaction.


#### Batch read-write transactions

Each `DB.Update()` waits for disk to commit the writes. This overhead
can be minimized by combining multiple updates with the `DB.Batch()`
function:

```go
err := db.Batch(func(tx *bolt.Tx) error {
	...
	return nil
})
```

Concurrent Batch calls are opportunistically combined into larger
transactions. Batch is only useful when there are multiple goroutines
calling it.

The trade-off is that `Batch` can call the given
function multiple times, if parts of the transaction fail. The
function must be idempotent and side effects must take effect only
after a successful return from `DB.Batch()`.

For example: don't display messages from inside the function, instead
set variables in the enclosing scope:

```go
var id uint64
err := db.Batch(func(tx *bolt.Tx) error {
	// Find last key in bucket, decode as bigendian uint64, increment
	// by one, encode back to []byte, and add new key.
	...
	id = newValue
	return nil
})
if err != nil {
	return ...
}
fmt.Println("Allocated ID %d", id)
```


#### Managing transactions manually

The `DB.View()` and `DB.Update()` functions are wrappers around the `DB.Begin()`
function. These helper functions will start the transaction, execute a function,
and then safely close your transaction if an error is returned. This is the
recommended way to use Bolt transactions.

However, sometimes you may want to manually start and end your transactions.
You can use the `DB.Begin()` function directly but **please** be sure to close
the transaction.

```go
// Start a writable transaction.
tx, err := db.Begin(true)
if err != nil {
    return err
}
defer tx.Rollback()

// Use the transaction...
_, err := tx.CreateBucket([]byte("MyBucket"))
if err != nil {
    return err
}

// Commit the transaction and check for error.
if err := tx.Commit(); err != nil {
    return err
}
```

The first argument to `DB.Begin()` is a boolean stating if the transaction
should be writable.


### Using buckets

Buckets are collections of key/value pairs within the database. All keys in a
bucket must be unique. You can create a bucket using the `Tx.CreateBucket()`
function:

```go
db.Update(func(tx *bolt.Tx) error {
	b, err := tx.CreateBucket([]byte("MyBucket"))
	if err != nil {
		return fmt.Errorf("create bucket: %s", err)
	}
	return nil
})
```

You can retrieve an existing bucket using the `Tx.Bucket()` function:
```go
db.Update(func(tx *bolt.Tx) error {
	b := tx.Bucket([]byte("MyBucket"))
	if b == nil {
		return errors.New("bucket does not exist")
	}
	return nil
})
```

You can also create a bucket only if it doesn't exist by using the
`Tx.CreateBucketIfNotExists()` function. It's a common pattern to call this
function for all your top-level buckets after you open your database so you can
guarantee that they exist for future transactions.

To delete a bucket, simply call the `Tx.DeleteBucket()` function.

You can also iterate over all existing top-level buckets with `Tx.ForEach()`:

```go
db.View(func(tx *bolt.Tx) error {
	tx.ForEach(func(name []byte, b *bolt.Bucket) error {
		fmt.Println(string(name))
		return nil
	})
	return nil
})
```

### Using key/value pairs

To save a key/value pair to a bucket, use the `Bucket.Put()` function:

```go
db.Update(func(tx *bolt.Tx) error {
	b := tx.Bucket([]byte("MyBucket"))
	err := b.Put([]byte("answer"), []byte("42"))
	return err
})
```

This will set the value of the `"answer"` key to `"42"` in the `MyBucket`
bucket. To retrieve this value, we can use the `Bucket.Get()` function:

```go
db.View(func(tx *bolt.Tx) error {
	b := tx.Bucket([]byte("MyBucket"))
	v := b.Get([]byte("answer"))
	fmt.Printf("The answer is: %s\n", v)
	return nil
})
```

The `Get()` function does not return an error because its operation is
guaranteed to work (unless there is some kind of system failure). If the key
exists then it will return its byte slice value. If it doesn't exist then it
will return `nil`. It's important to note that you can have a zero-length value
set to a key which is different than the key not existing.

Use the `Bucket.Delete()` function to delete a key from the bucket:

```go
db.Update(func (tx *bolt.Tx) error {
    b := tx.Bucket([]byte("MyBucket"))
    err := b.Delete([]byte("answer"))
    return err
})
```

This will delete the key `answers` from the bucket `MyBucket`.

Please note that values returned from `Get()` are only valid while the
transaction is open. If you need to use a value outside of the transaction
then you must use `copy()` to copy it to another byte slice.


### Autoincrementing integer for the bucket
By using the `NextSequence()` function, you can let Bolt determine a sequence
which can be used as the unique identifier for your key/value pairs. See the
example below.

```go
// CreateUser saves u to the store. The new user ID is set on u once the data is persisted.
func (s *Store) CreateUser(u *User) error {
    return s.db.Update(func(tx *bolt.Tx) error {
        // Retrieve the users bucket.
        // This should be created when the DB is first opened.
        b := tx.Bucket([]byte("users"))

        // Generate ID for the user.
        // This returns an error only if the Tx is closed or not writeable.
        // That can't happen in an Update() call so I ignore the error check.
        id, _ := b.NextSequence()
        u.ID = int(id)

        // Marshal user data into bytes.
        buf, err := json.Marshal(u)
        if err != nil {
            return err
        }

        // Persist bytes to users bucket.
        return b.Put(itob(u.ID), buf)
    })
}

// itob returns an 8-byte big endian representation of v.
func itob(v int) []byte {
    b := make([]byte, 8)
    binary.BigEndian.PutUint64(b, uint64(v))
    return b
}

type User struct {
    ID int
    ...
}
```

### Iterating over keys

Bolt stores its keys in byte-sorted order within a bucket. This makes sequential
iteration over these keys extremely fast. To iterate over keys we'll use a
`Cursor`:

```go
db.View(func(tx *bolt.Tx) error {
	// Assume bucket exists and has keys
	b := tx.Bucket([]byte("MyBucket"))

	c := b.Cursor()

	for k, v := c.First(); k != nil; k, v = c.Next() {
		fmt.Printf("key=%s, value=%s\n", k, v)
	}

	return nil
})
```

The cursor allows you to move to a specific point in the list of keys and move
forward or backward through the keys one at a time.

The following functions are available on the cursor:

```
First()  Move to the first key.
Last()   Move to the last key.
Seek()   Move to a specific key.
Next()   Move to the next key.
Prev()   Move to the previous key.
```

Each of those functions has a return signature of `(key []byte, value []byte)`.
You must seek to a position using `First()`, `Last()`, or `Seek()` before calling
`Next()` or `Prev()`. If you do not seek to a position then these functions will
return a `nil` key.

When you have iterated to the end of the cursor, then `Next()` will return a
`nil` key and the cursor still points to the last element if present. When you
have iterated to the beginning of the cursor, then `Prev()` will return a `nil`
key and the cursor still points to the first element if present.

If you remove key/value pairs during iteration, the cursor may automatically
move to the next position if present in current node each time removing a key.
When you call `c.Next()` after removing a key, it may skip one key/value pair.
Refer to [pull/611](https://github.com/etcd-io/bbolt/pull/611) to get more detailed info.

During iteration, if the key is non-`nil` but the value is `nil`, that means
the key refers to a bucket rather than a value.  Use `Bucket.Bucket()` to
access the sub-bucket.


#### Prefix scans

To iterate over a key prefix, you can combine `Seek()` and `bytes.HasPrefix()`:

```go
db.View(func(tx *bolt.Tx) erro
... [TRUNCATED]
```

### File: .golangci.yaml
```yaml
formatters:
  enable:
    - gci
    - gofmt
    - goimports
  settings: # please keep this alphabetized
    gci:
      sections:
        - standard
        - default
        - prefix(go.etcd.io)
    goimports:
      local-prefixes:
        - go.etcd.io # Put imports beginning with prefix after 3rd-party packages.
issues:
  max-same-issues: 0
linters:
  default: none
  enable: # please keep this alphabetized
    - errcheck
    - govet
    - ineffassign
    - staticcheck
    - unused
  exclusions:
    presets:
      - comments
      - common-false-positives
      - legacy
      - std-error-handling
  settings: # please keep this alphabetized
    staticcheck:
      checks:
        - all
        - -QF1003 # Convert if/else-if chain to tagged switch
        - -QF1010 # Convert slice of bytes to string when printing it
        - -ST1003 # Poorly chosen identifier
        - -ST1005 # Incorrectly formatted error string
        - -ST1012 # Poorly chosen name for error variable
version: "2"

```

### File: allocate_test.go
```go
package bbolt

import (
	"testing"

	"go.etcd.io/bbolt/internal/common"
	"go.etcd.io/bbolt/internal/freelist"
)

func TestTx_allocatePageStats(t *testing.T) {
	for n, f := range map[string]freelist.Interface{"hashmap": freelist.NewHashMapFreelist(), "array": freelist.NewArrayFreelist()} {
		t.Run(n, func(t *testing.T) {
			ids := []common.Pgid{2, 3}
			f.Init(ids)

			tx := &Tx{
				db: &DB{
					freelist: f,
					pageSize: common.DefaultPageSize,
				},
				meta:  &common.Meta{},
				pages: make(map[common.Pgid]*common.Page),
			}

			txStats := tx.Stats()
			prePageCnt := txStats.GetPageCount()
			allocateCnt := f.FreeCount()

			if _, err := tx.allocate(allocateCnt); err != nil {
				t.Fatal(err)
			}

			txStats = tx.Stats()
			if txStats.GetPageCount() != prePageCnt+int64(allocateCnt) {
				t.Errorf("Allocated %d but got %d page in stats", allocateCnt, txStats.GetPageCount())
			}
		})
	}
}

```

### File: boltsync_unix.go
```go
//go:build !windows && !plan9 && !linux && !openbsd

package bbolt

// fdatasync flushes written data to a file descriptor.
func fdatasync(db *DB) error {
	return db.file.Sync()
}

```

### File: bolt_aix.go
```go
//go:build aix

package bbolt

import (
	"fmt"
	"syscall"
	"time"
	"unsafe"

	"golang.org/x/sys/unix"

	"go.etcd.io/bbolt/internal/common"
)

// flock acquires an advisory lock on a file descriptor.
func flock(db *DB, exclusive bool, timeout time.Duration) error {
	var t time.Time
	if timeout != 0 {
		t = time.Now()
	}
	fd := db.file.Fd()
	var lockType int16
	if exclusive {
		lockType = syscall.F_WRLCK
	} else {
		lockType = syscall.F_RDLCK
	}
	for {
		// Attempt to obtain an exclusive lock.
		lock := syscall.Flock_t{Type: lockType}
		err := syscall.FcntlFlock(fd, syscall.F_SETLK, &lock)
		if err == nil {
			return nil
		} else if err != syscall.EAGAIN {
			return err
		}

		// If we timed out then return an error.
		if timeout != 0 && time.Since(t) > timeout-flockRetryTimeout {
			return ErrTimeout
		}

		// Wait for a bit and try again.
		time.Sleep(flockRetryTimeout)
	}
}

// funlock releases an advisory lock on a file descriptor.
func funlock(db *DB) error {
	var lock syscall.Flock_t
	lock.Start = 0
	lock.Len = 0
	lock.Type = syscall.F_UNLCK
	lock.Whence = 0
	return syscall.FcntlFlock(uintptr(db.file.Fd()), syscall.F_SETLK, &lock)
}

// mmap memory maps a DB's data file.
func mmap(db *DB, sz int) error {
	// Map the data file to memory.
	b, err := unix.Mmap(int(db.file.Fd()), 0, sz, syscall.PROT_READ, syscall.MAP_SHARED|db.MmapFlags)
	if err != nil {
		return err
	}

	// Advise the kernel that the mmap is accessed randomly.
	if err := unix.Madvise(b, syscall.MADV_RANDOM); err != nil {
		return fmt.Errorf("madvise: %s", err)
	}

	// Save the original byte slice and convert to a byte array pointer.
	db.dataref = b
	db.data = (*[common.MaxMapSize]byte)(unsafe.Pointer(&b[0]))
	db.datasz = sz
	return nil
}

// munmap unmaps a DB's data file from memory.
func munmap(db *DB) error {
	// Ignore the unmap if we have no mapped data.
	if db.dataref == nil {
		return nil
	}

	// Unmap using the original byte slice.
	err := unix.Munmap(db.dataref)
	db.dataref = nil
	db.data = nil
	db.datasz = 0
	return err
}

```

### File: bolt_android.go
```go
package bbolt

import (
	"fmt"
	"syscall"
	"time"
	"unsafe"

	"golang.org/x/sys/unix"

	"go.etcd.io/bbolt/internal/common"
)

// flock acquires an advisory lock on a file descriptor.
func flock(db *DB, exclusive bool, timeout time.Duration) error {
	var t time.Time
	if timeout != 0 {
		t = time.Now()
	}
	fd := db.file.Fd()
	var lockType int16
	if exclusive {
		lockType = syscall.F_WRLCK
	} else {
		lockType = syscall.F_RDLCK
	}
	for {
		// Attempt to obtain an exclusive lock.
		lock := syscall.Flock_t{Type: lockType}
		err := syscall.FcntlFlock(fd, syscall.F_SETLK, &lock)
		if err == nil {
			return nil
		} else if err != syscall.EAGAIN {
			return err
		}

		// If we timed out then return an error.
		if timeout != 0 && time.Since(t) > timeout-flockRetryTimeout {
			return ErrTimeout
		}

		// Wait for a bit and try again.
		time.Sleep(flockRetryTimeout)
	}
}

// funlock releases an advisory lock on a file descriptor.
func funlock(db *DB) error {
	var lock syscall.Flock_t
	lock.Start = 0
	lock.Len = 0
	lock.Type = syscall.F_UNLCK
	lock.Whence = 0
	return syscall.FcntlFlock(uintptr(db.file.Fd()), syscall.F_SETLK, &lock)
}

// mmap memory maps a DB's data file.
func mmap(db *DB, sz int) error {
	// Map the data file to memory.
	b, err := unix.Mmap(int(db.file.Fd()), 0, sz, syscall.PROT_READ, syscall.MAP_SHARED|db.MmapFlags)
	if err != nil {
		return err
	}

	// Advise the kernel that the mmap is accessed randomly.
	err = unix.Madvise(b, syscall.MADV_RANDOM)
	if err != nil && err != syscall.ENOSYS {
		// Ignore not implemented error in kernel because it still works.
		return fmt.Errorf("madvise: %s", err)
	}

	// Save the original byte slice and convert to a byte array pointer.
	db.dataref = b
	db.data = (*[common.MaxMapSize]byte)(unsafe.Pointer(&b[0]))
	db.datasz = sz
	return nil
}

// munmap unmaps a DB's data file from memory.
func munmap(db *DB) error {
	// Ignore the unmap if we have no mapped data.
	if db.dataref == nil {
		return nil
	}

	// Unmap using the original byte slice.
	err := unix.Munmap(db.dataref)
	db.dataref = nil
	db.data = nil
	db.datasz = 0
	return err
}

```

### File: bolt_linux.go
```go
package bbolt

import (
	"syscall"
)

// fdatasync flushes written data to a file descriptor.
func fdatasync(db *DB) error {
	return syscall.Fdatasync(int(db.file.Fd()))
}

```

### File: bolt_openbsd.go
```go
package bbolt

import (
	"golang.org/x/sys/unix"
)

func msync(db *DB) error {
	return unix.Msync(db.data[:db.datasz], unix.MS_INVALIDATE)
}

func fdatasync(db *DB) error {
	if db.data != nil {
		return msync(db)
	}
	return db.file.Sync()
}

```

### File: bolt_solaris.go
```go
package bbolt

import (
	"fmt"
	"syscall"
	"time"
	"unsafe"

	"golang.org/x/sys/unix"

	"go.etcd.io/bbolt/internal/common"
)

// flock acquires an advisory lock on a file descriptor.
func flock(db *DB, exclusive bool, timeout time.Duration) error {
	var t time.Time
	if timeout != 0 {
		t = time.Now()
	}
	fd := db.file.Fd()
	var lockType int16
	if exclusive {
		lockType = syscall.F_WRLCK
	} else {
		lockType = syscall.F_RDLCK
	}
	for {
		// Attempt to obtain an exclusive lock.
		lock := syscall.Flock_t{Type: lockType}
		err := syscall.FcntlFlock(fd, syscall.F_SETLK, &lock)
		if err == nil {
			return nil
		} else if err != syscall.EAGAIN {
			return err
		}

		// If we timed out then return an error.
		if timeout != 0 && time.Since(t) > timeout-flockRetryTimeout {
			return ErrTimeout
		}

		// Wait for a bit and try again.
		time.Sleep(flockRetryTimeout)
	}
}

// funlock releases an advisory lock on a file descriptor.
func funlock(db *DB) error {
	var lock syscall.Flock_t
	lock.Start = 0
	lock.Len = 0
	lock.Type = syscall.F_UNLCK
	lock.Whence = 0
	return syscall.FcntlFlock(uintptr(db.file.Fd()), syscall.F_SETLK, &lock)
}

// mmap memory maps a DB's data file.
func mmap(db *DB, sz int) error {
	// Map the data file to memory.
	b, err := unix.Mmap(int(db.file.Fd()), 0, sz, syscall.PROT_READ, syscall.MAP_SHARED|db.MmapFlags)
	if err != nil {
		return err
	}

	// Advise the kernel that the mmap is accessed randomly.
	if err := unix.Madvise(b, syscall.MADV_RANDOM); err != nil {
		return fmt.Errorf("madvise: %s", err)
	}

	// Save the original byte slice and convert to a byte array pointer.
	db.dataref = b
	db.data = (*[common.MaxMapSize]byte)(unsafe.Pointer(&b[0]))
	db.datasz = sz
	return nil
}

// munmap unmaps a DB's data file from memory.
func munmap(db *DB) error {
	// Ignore the unmap if we have no mapped data.
	if db.dataref == nil {
		return nil
	}

	// Unmap using the original byte slice.
	err := unix.Munmap(db.dataref)
	db.dataref = nil
	db.data = nil
	db.datasz = 0
	return err
}

```

### File: bolt_unix.go
```go
//go:build !windows && !plan9 && !solaris && !aix && !android

package bbolt

import (
	"fmt"
	"syscall"
	"time"
	"unsafe"

	"golang.org/x/sys/unix"

	"go.etcd.io/bbolt/errors"
	"go.etcd.io/bbolt/internal/common"
)

// flock acquires an advisory lock on a file descriptor.
func flock(db *DB, exclusive bool, timeout time.Duration) error {
	var t time.Time
	if timeout != 0 {
		t = time.Now()
	}
	fd := db.file.Fd()
	flag := syscall.LOCK_NB
	if exclusive {
		flag |= syscall.LOCK_EX
	} else {
		flag |= syscall.LOCK_SH
	}
	for {
		// Attempt to obtain an exclusive lock.
		err := syscall.Flock(int(fd), flag)
		if err == nil {
			return nil
		} else if err != syscall.EWOULDBLOCK {
			return err
		}

		// If we timed out then return an error.
		if timeout != 0 && time.Since(t) > timeout-flockRetryTimeout {
			return errors.ErrTimeout
		}

		// Wait for a bit and try again.
		time.Sleep(flockRetryTimeout)
	}
}

// funlock releases an advisory lock on a file descriptor.
func funlock(db *DB) error {
	return syscall.Flock(int(db.file.Fd()), syscall.LOCK_UN)
}

// mmap memory maps a DB's data file.
func mmap(db *DB, sz int) error {
	// Map the data file to memory.
	b, err := unix.Mmap(int(db.file.Fd()), 0, sz, syscall.PROT_READ, syscall.MAP_SHARED|db.MmapFlags)
	if err != nil {
		return err
	}

	// Advise the kernel that the mmap is accessed randomly.
	err = unix.Madvise(b, syscall.MADV_RANDOM)
	if err != nil && err != syscall.ENOSYS {
		// Ignore not implemented error in kernel because it still works.
		return fmt.Errorf("madvise: %s", err)
	}

	// Save the original byte slice and convert to a byte array pointer.
	db.dataref = b
	db.data = (*[common.MaxMapSize]byte)(unsafe.Pointer(&b[0]))
	db.datasz = sz
	return nil
}

// munmap unmaps a DB's data file from memory.
func munmap(db *DB) error {
	// Ignore the unmap if we have no mapped data.
	if db.dataref == nil {
		return nil
	}

	// Unmap using the original byte slice.
	err := unix.Munmap(db.dataref)
	db.dataref = nil
	db.data = nil
	db.datasz = 0
	return err
}

```

### File: bolt_windows.go
```go
package bbolt

import (
	"fmt"
	"os"
	"syscall"
	"time"
	"unsafe"

	"golang.org/x/sys/windows"

	"go.etcd.io/bbolt/errors"
	"go.etcd.io/bbolt/internal/common"
)

// fdatasync flushes written data to a file descriptor.
func fdatasync(db *DB) error {
	return db.file.Sync()
}

// flock acquires an advisory lock on a file descriptor.
func flock(db *DB, exclusive bool, timeout time.Duration) error {
	var t time.Time
	if timeout != 0 {
		t = time.Now()
	}
	var flags uint32 = windows.LOCKFILE_FAIL_IMMEDIATELY
	if exclusive {
		flags |= windows.LOCKFILE_EXCLUSIVE_LOCK
	}
	for {
		// Fix for https://github.com/etcd-io/bbolt/issues/121. Use byte-range
		// -1..0 as the lock on the database file.
		var m1 uint32 = (1 << 32) - 1 // -1 in a uint32
		err := windows.LockFileEx(windows.Handle(db.file.Fd()), flags, 0, 1, 0, &windows.Overlapped{
			Offset:     m1,
			OffsetHigh: m1,
		})

		if err == nil {
			return nil
		} else if err != windows.ERROR_LOCK_VIOLATION {
			return err
		}

		// If we timed oumercit then return an error.
		if timeout != 0 && time.Since(t) > timeout-flockRetryTimeout {
			return errors.ErrTimeout
		}

		// Wait for a bit and try again.
		time.Sleep(flockRetryTimeout)
	}
}

// funlock releases an advisory lock on a file descriptor.
func funlock(db *DB) error {
	var m1 uint32 = (1 << 32) - 1 // -1 in a uint32
	return windows.UnlockFileEx(windows.Handle(db.file.Fd()), 0, 1, 0, &windows.Overlapped{
		Offset:     m1,
		OffsetHigh: m1,
	})
}

// mmap memory maps a DB's data file.
// Based on: https://github.com/edsrzf/mmap-go
func mmap(db *DB, sz int) error {
	var sizelo, sizehi uint32

	if !db.readOnly {
		if db.MaxSize > 0 && sz > db.MaxSize {
			// The max size only limits future writes; however, we don’t block opening
			// and mapping the database if it already exceeds the limit.
			fileSize, err := db.fileSize()
			if err != nil {
				return fmt.Errorf("could not check existing db file size: %s", err)
			}

			if sz > fileSize {
				return errors.ErrMaxSizeReached
			}
		}

		// Truncate the database to the size of the mmap.
		if err := db.file.Truncate(int64(sz)); err != nil {
			return fmt.Errorf("truncate: %s", err)
		}
		sizehi = uint32(sz >> 32)
		sizelo = uint32(sz)
	}

	// Open a file mapping handle.
	h, errno := syscall.CreateFileMapping(syscall.Handle(db.file.Fd()), nil, syscall.PAGE_READONLY, sizehi, sizelo, nil)
	if h == 0 {
		return os.NewSyscallError("CreateFileMapping", errno)
	}

	// Create the memory map.
	addr, errno := syscall.MapViewOfFile(h, syscall.FILE_MAP_READ, 0, 0, 0)
	if addr == 0 {
		// Do our best and report error returned from MapViewOfFile.
		_ = syscall.CloseHandle(h)
		return os.NewSyscallError("MapViewOfFile", errno)
	}

	// Close mapping handle.
	if err := syscall.CloseHandle(syscall.Handle(h)); err != nil {
		return os.NewSyscallError("CloseHandle", err)
	}

	// Convert to a byte array.
	db.data = (*[common.MaxMapSize]byte)(unsafe.Pointer(addr))
	db.datasz = sz

	return nil
}

// munmap unmaps a pointer from a file.
// Based on: https://github.com/edsrzf/mmap-go
func munmap(db *DB) error {
	if db.data == nil {
		return nil
	}

	addr := (uintptr)(unsafe.Pointer(&db.data[0]))
	var err1 error
	if err := syscall.UnmapViewOfFile(addr); err != nil {
		err1 = os.NewSyscallError("UnmapViewOfFile", err)
	}
	db.data = nil
	db.datasz = 0
	return err1
}

```

### File: bucket.go
```go
package bbolt

import (
	"bytes"
	"fmt"
	"unsafe"

	"go.etcd.io/bbolt/errors"
	"go.etcd.io/bbolt/internal/common"
)

const (
	// MaxKeySize is the maximum length of a key, in bytes.
	MaxKeySize = 32768

	// MaxValueSize is the maximum length of a value, in bytes.
	MaxValueSize = (1 << 31) - 2
)

const (
	minFillPercent = 0.1
	maxFillPercent = 1.0
)

// DefaultFillPercent is the percentage that split pages are filled.
// This value can be changed by setting Bucket.FillPercent.
const DefaultFillPercent = 0.5

// Bucket represents a collection of key/value pairs inside the database.
type Bucket struct {
	*common.InBucket
	tx       *Tx                   // the associated transaction
	buckets  map[string]*Bucket    // subbucket cache
	page     *common.Page          // inline page reference
	rootNode *node                 // materialized node for the root page.
	nodes    map[common.Pgid]*node // node cache

	// Sets the threshold for filling nodes when they split. By default,
	// the bucket will fill to 50% but it can be useful to increase this
	// amount if you know that your write workloads are mostly append-only.
	//
	// This is non-persisted across transactions so it must be set in every Tx.
	FillPercent float64
}

// newBucket returns a new bucket associated with a transaction.
func newBucket(tx *Tx) Bucket {
	var b = Bucket{tx: tx, FillPercent: DefaultFillPercent}
	if tx.writable {
		b.buckets = make(map[string]*Bucket)
		b.nodes = make(map[common.Pgid]*node)
	}
	return b
}

// Tx returns the tx of the bucket.
func (b *Bucket) Tx() *Tx {
	return b.tx
}

// Root returns the root of the bucket.
func (b *Bucket) Root() common.Pgid {
	return b.RootPage()
}

// Writable returns whether the bucket is writable.
func (b *Bucket) Writable() bool {
	return b.tx.writable
}

// Cursor creates a cursor associated with the bucket.
// The cursor is only valid as long as the transaction is open.
// Do not use a cursor after the transaction is closed.
func (b *Bucket) Cursor() *Cursor {
	// Update transaction statistics.
	b.tx.stats.IncCursorCount(1)

	// Allocate and return a cursor.
	return &Cursor{
		bucket: b,
		stack:  make([]elemRef, 0),
	}
}

// Bucket retrieves a nested bucket by name.
// Returns nil if the bucket does not exist.
// The bucket instance is only valid for the lifetime of the transaction.
func (b *Bucket) Bucket(name []byte) *Bucket {
	if b.buckets != nil {
		if child := b.buckets[string(name)]; child != nil {
			return child
		}
	}

	// Move cursor to key.
	c := b.Cursor()
	k, v, flags := c.seek(name)

	// Return nil if the key doesn't exist or it is not a bucket.
	if !bytes.Equal(name, k) || (flags&common.BucketLeafFlag) == 0 {
		return nil
	}

	// Otherwise create a bucket and cache it.
	var child = b.openBucket(v)
	if b.buckets != nil {
		b.buckets[string(name)] = child
	}

	return child
}

// Helper method that re-interprets a sub-bucket value
// from a parent into a Bucket
func (b *Bucket) openBucket(value []byte) *Bucket {
	var child = newBucket(b.tx)

	// Unaligned access requires a copy to be made.
	const unalignedMask = unsafe.Alignof(struct {
		common.InBucket
		common.Page
	}{}) - 1
	unaligned := uintptr(unsafe.Pointer(&value[0]))&unalignedMask != 0
	if unaligned {
		value = cloneBytes(value)
	}

	// If this is a writable transaction then we need to copy the bucket entry.
	// Read-only transactions can point directly at the mmap entry.
	if b.tx.writable && !unaligned {
		child.InBucket = &common.InBucket{}
		*child.InBucket = *(*common.InBucket)(unsafe.Pointer(&value[0]))
	} else {
		child.InBucket = (*common.InBucket)(unsafe.Pointer(&value[0]))
	}

	// Save a reference to the inline page if the bucket is inline.
	if child.RootPage() == 0 {
		child.page = (*common.Page)(unsafe.Pointer(&value[common.BucketHeaderSize]))
	}

	return &child
}

// CreateBucket creates a new bucket at the given key and returns the new bucket.
// Returns an error if the key already exists, if the bucket name is blank, or if the bucket name is too long.
// The bucket instance is only valid for the lifetime of the transaction.
func (b *Bucket) CreateBucket(key []byte) (rb *Bucket, err error) {
	if lg := b.tx.db.Logger(); lg != discardLogger {
		lg.Debugf("Creating bucket %q", key)
		defer func() {
			if err != nil {
				lg.Errorf("Creating bucket %q failed: %v", key, err)
			} else {
				lg.Debugf("Creating bucket %q successfully", key)
			}
		}()
	}
	if b.tx.db == nil {
		return nil, errors.ErrTxClosed
	} else if !b.tx.writable {
		return nil, errors.ErrTxNotWritable
	} else if len(key) == 0 {
		return nil, errors.ErrBucketNameRequired
	}

	// Insert into node.
	// Tip: Use a new variable `newKey` instead of reusing the existing `key` to prevent
	// it from being marked as leaking, and accordingly cannot be allocated on stack.
	newKey := cloneBytes(key)

	// Move cursor to correct position.
	c := b.Cursor()
	k, _, flags := c.seek(newKey)

	// Return an error if there is an existing key.
	if bytes.Equal(newKey, k) {
		if (flags & common.BucketLeafFlag) != 0 {
			return nil, errors.ErrBucketExists
		}
		return nil, errors.ErrIncompatibleValue
	}

	// Create empty, inline bucket.
	var bucket = Bucket{
		InBucket:    &common.InBucket{},
		rootNode:    &node{isLeaf: true},
		FillPercent: DefaultFillPercent,
	}
	var value = bucket.write()

	c.node().put(newKey, newKey, value, 0, common.BucketLeafFlag)

	// Since subbuckets are not allowed on inline buckets, we need to
	// dereference the inline page, if it exists. This will cause the bucket
	// to be treated as a regular, non-inline bucket for the rest of the tx.
	b.page = nil

	return b.Bucket(newKey), nil
}

// CreateBucketIfNotExists creates a new bucket if it doesn't already exist and returns a reference to it.
// Returns an error if the bucket name is blank, or if the bucket name is too long.
// The bucket instance is only valid for the lifetime of the transaction.
func (b *Bucket) CreateBucketIfNotExists(key []byte) (rb *Bucket, err error) {
	if lg := b.tx.db.Logger(); lg != discardLogger {
		lg.Debugf("Creating bucket if not exist %q", key)
		defer func() {
			if err != nil {
				lg.Errorf("Creating bucket if not exist %q failed: %v", key, err)
			} else {
				lg.Debugf("Creating bucket if not exist %q successfully", key)
			}
		}()
	}

	if b.tx.db == nil {
		return nil, errors.ErrTxClosed
	} else if !b.tx.writable {
		return nil, errors.ErrTxNotWritable
	} else if len(key) == 0 {
		return nil, errors.ErrBucketNameRequired
	}

	// Insert into node.
	// Tip: Use a new variable `newKey` instead of reusing the existing `key` to prevent
	// it from being marked as leaking, and accordingly cannot be allocated on stack.
	newKey := cloneBytes(key)

	if b.buckets != nil {
		if child := b.buckets[string(newKey)]; child != nil {
			return child, nil
		}
	}

	// Move cursor to correct position.
	c := b.Cursor()
	k, v, flags := c.seek(newKey)

	// Return an error if there is an existing non-bucket key.
	if bytes.Equal(newKey, k) {
		if (flags & common.BucketLeafFlag) != 0 {
			var child = b.openBucket(v)
			if b.buckets != nil {
				b.buckets[string(newKey)] = child
			}

			return child, nil
		}
		return nil, errors.ErrIncompatibleValue
	}

	// Create empty, inline bucket.
	var bucket = Bucket{
		InBucket:    &common.InBucket{},
		rootNode:    &node{isLeaf: true},
		FillPercent: DefaultFillPercent,
	}
	var value = bucket.write()

	c.node().put(newKey, newKey, value, 0, common.BucketLeafFlag)

	// Since subbuckets are not allowed on inline buckets, we need to
	// dereference the inline page, if it exists. This will cause the bucket
	// to be treated as a regular, non-inline bucket for the rest of the tx.
	b.page = nil

	return b.Bucket(newKey), nil
}

// DeleteBucket deletes a bucket at the given key.
// Returns an error if the bucket does not exist, or if the key represents a non-bucket value.
func (b *Bucket) DeleteBucket(key []byte) (err error) {
	if lg := b.tx.db.Logger(); lg != discardLogger {
		lg.Debugf("Deleting bucket %q", key)
		defer func() {
			if err != nil {
				lg.Errorf("Deleting bucket %q failed: %v", key, err)
			} else {
				lg.Debugf("Deleting bucket %q successfully", key)
			}
		}()
	}

	if b.tx.db == nil {
		return errors.ErrTxClosed
	} else if !b.Writable() {
		return errors.ErrTxNotWritable
	}

	newKey := cloneBytes(key)

	// Move cursor to correct position.
	c := b.Cursor()
	k, _, flags := c.seek(newKey)

	// Return an error if bucket doesn't exist or is not a bucket.
	if !bytes.Equal(newKey, k) {
		return errors.ErrBucketNotFound
	} else if (flags & common.BucketLeafFlag) == 0 {
		return errors.ErrIncompatibleValue
	}

	// Recursively delete all child buckets.
	child := b.Bucket(newKey)
	err = child.ForEachBucket(func(k []byte) error {
		if err := child.DeleteBucket(k); err != nil {
			return fmt.Errorf("delete bucket: %s", err)
		}
		return nil
	})
	if err != nil {
		return err
	}

	// Remove cached copy.
	delete(b.buckets, string(newKey))

	// Release all bucket pages to freelist.
	child.nodes = nil
	child.rootNode = nil
	child.free()

	// Delete the node if we have a matching key.
	c.node().del(newKey)

	return nil
}

// MoveBucket moves a sub-bucket from the source bucket to the destination bucket.
// Returns an error if
//  1. the sub-bucket cannot be found in the source bucket;
//  2. or the key already exists in the destination bucket;
//  3. or the key represents a non-bucket value;
//  4. the source and destination buckets are the same.
func (b *Bucket) MoveBucket(key []byte, dstBucket *Bucket) (err error) {
	lg := b.tx.db.Logger()
	if lg != discardLogger {
		lg.Debugf("Moving bucket %q", key)
		defer func() {
			if err != nil {
				lg.Errorf("Moving bucket %q failed: %v", key, err)
			} else {
				lg.Debugf("Moving bucket %q successfully", key)
			}
		}()
	}

	if b.tx.db == nil || dstBucket.tx.db == nil {
		return errors.ErrTxClosed
	} else if !b.Writable() || !dstBucket.Writable() {
		return errors.ErrTxNotWritable
	}

	if b.tx.db.Path() != dstBucket.tx.db.Path() || b.tx != dstBucket.tx {
		lg.Errorf("The source and target buckets are not in the same db file, source bucket in %s and target bucket in %s", b.tx.db.Path(), dstBucket.tx.db.Path())
		return errors.ErrDifferentDB
	}

	newKey := cloneBytes(key)

	// Move cursor to correct position.
	c := b.Cursor()
	k, v, flags := c.seek(newKey)

	// Return an error if bucket doesn't exist or is not a bucket.
	if !bytes.Equal(newKey, k) {
		return errors.ErrBucketNotFound
	} else if (flags & common.BucketLeafFlag) == 0 {
		lg.Errorf("An incompatible key %s exists in the source bucket", newKey)
		return errors.ErrIncompatibleValue
	}

	// Do nothing (return true directly) if the source bucket and the
	// destination bucket are actually the same bucket.
	if b == dstBucket || (b.RootPage() == dstBucket.RootPage() && b.RootPage() != 0) {
		lg.Errorf("The source bucket (%s) and the target bucket (%s) are the same bucket", b, dstBucket)
		return errors.ErrSameBuckets
	}

	// check whether the key already exists in the destination bucket
	curDst := dstBucket.Cursor()
	k, _, flags = curDst.seek(newKey)

	// Return an error if there is an existing key in the destination bucket.
	if bytes.Equal(newKey, k) {
		if (flags & common.BucketLeafFlag) != 0 {
			return errors.ErrBucketExists
		}
		lg.Errorf("An incompatible key %s exists in the target bucket", newKey)
		return errors.ErrIncompatibleValue
	}

	// remove the sub-bucket from the source bucket
	delete(b.buckets, string(newKey))
	c.node().del(newKey)

	// add te sub-bucket to the destination bucket
	newValue := cloneBytes(v)
	curDst.node().put(newKey, newKey, newValue, 0, common.BucketLeafFlag)

	return nil
}

// Inspect returns the structure of the bucket.
func (b *Bucket) Inspect() BucketStructure {
	return b.recursivelyInspect([]byte("root"))
}

func (b *Bucket) recursivelyInspect(name []byte) BucketStructure {
	bs := BucketStructure{Name: string(name)}

	keyN := 0
	c := b.Cursor()
	for k, _, flags := c.first(); k != nil; k, _, flags = c.next() {
		if flags&common.BucketLeafFlag != 0 {
			childBucket := b.Bucket(k)
			childBS := childBucket.recursivelyInspect(k)
			bs.Children = append(bs.Children, childBS)
		} else {
			keyN++
		}
	}
	bs.KeyN = keyN

	return bs
}

// Get retrieves the value for a key in the bucket.
// Returns a nil value if the key does not exist or if the key is a nested bucket.
// The returned value is only valid for the life of the transaction.
// The returned memory is owned by bbolt and must never be modified; writing to this memory might corrupt the database.
func (b *Bucket) Get(key []byte) []byte {
	k, v, flags := b.Cursor().seek(key)

	// Return nil if this is a bucket.
	if (flags & common.BucketLeafFlag) != 0 {
		return nil
	}

	// If our target node isn't the same key as what's passed in then return nil.
	if !bytes.Equal(key, k) {
		return nil
	}
	return v
}

// Put sets the value for a key in the bucket.
// If the key exist then its previous value will be overwritten.
// Supplied value must remain valid for the life of the transaction.
// Returns an error if the bucket was created from a read-only transaction, if the key is blank, if the key is too large, or if the value is too large.
func (b *Bucket) Put(key []byte, value []byte) (err error) {
	if lg := b.tx.db.Logger(); lg != discardLogger {
		lg.Debugf("Putting key %q", key)
		defer func() {
			if err != nil {
				lg.Errorf("Putting key %q failed: %v", key, err)
			} else {
				lg.Debugf("Putting key %q successfully", key)
			}
		}()
	}
	if b.tx.db == nil {
		return errors.ErrTxClosed
	} else if !b.Writable() {
		return errors.ErrTxNotWritable
	} else if len(key) == 0 {
		return errors.ErrKeyRequired
	} else if len(key) > MaxKeySize {
		return errors.ErrKeyTooLarge
	} else if int64(len(value)) > MaxValueSize {
		return errors.ErrValueTooLarge
	}

	// Insert into node.
	// Tip: Use a new variable `newKey` instead of reusing the existing `key` to prevent
	// it from being marked as leaking, and accordingly cannot be allocated on stack.
	newKey := cloneBytes(key)

	// Move cursor to correct position.
	c := b.Cursor()
	k, _, flags := c.seek(newKey)

	// Return an error if there is an existing key with a bucket value.
	if bytes.Equal(newKey, k) && (flags&common.BucketLeafFlag) != 0 {
		return errors.ErrIncompatibleValue
	}

	// gofail: var beforeBucketPut struct{}

	c.node().put(newKey, newKey, value, 0, 0)

	return nil
}

// Delete removes a key from the bucket.
// If the key does not exist then nothing is done and a nil error is returned.
// Returns an error if the bucket was created from a read-only transaction.
func (b *Bucket) Delete(key []byte) (err error) {
	if lg := b.tx.db.Logger(); lg != discardLogger {
		lg.Debugf("Deleting key %q", key)
		defer func() {
			if err != nil {
				lg.Errorf("Deleting key %q failed: %v", key, err)
			} else {
				lg.Debugf("Deleting key %q successfully", key)
			}
		}()
	}

	if b.tx.db == nil {
		return errors.ErrTxClosed
	} else if !b.W
... [TRUNCATED]
```

### File: bucket_test.go
```go
package bbolt_test

import (
	"bytes"
	"encoding/binary"
	"errors"
	"fmt"
	"log"
	"math/rand"
	"os"
	"strconv"
	"strings"
	"testing"
	"testing/quick"

	"github.com/stretchr/testify/assert"
	"github.com/stretchr/testify/require"

	bolt "go.etcd.io/bbolt"
	berrors "go.etcd.io/bbolt/errors"
	"go.etcd.io/bbolt/internal/btesting"
)

// Ensure that a bucket that gets a non-existent key returns nil.
func TestBucket_Get_NonExistent(t *testing.T) {
	db := btesting.MustCreateDB(t)

	if err := db.Update(func(tx *bolt.Tx) error {
		b, err := tx.CreateBucket([]byte("widgets"))
		if err != nil {
			t.Fatal(err)
		}
		if v := b.Get([]byte("foo")); v != nil {
			t.Fatal("expected nil value")
		}
		return nil
	}); err != nil {
		t.Fatal(err)
	}
}

// Ensure that a bucket can read a value that is not flushed yet.
func TestBucket_Get_FromNode(t *testing.T) {
	db := btesting.MustCreateDB(t)

	if err := db.Update(func(tx *bolt.Tx) error {
		b, err := tx.CreateBucket([]byte("widgets"))
		if err != nil {
			t.Fatal(err)
		}
		if err := b.Put([]byte("foo"), []byte("bar")); err != nil {
			t.Fatal(err)
		}
		if v := b.Get([]byte("foo")); !bytes.Equal(v, []byte("bar")) {
			t.Fatalf("unexpected value: %v", v)
		}
		return nil
	}); err != nil {
		t.Fatal(err)
	}
}

// Ensure that a bucket retrieved via Get() returns a nil.
func TestBucket_Get_IncompatibleValue(t *testing.T) {
	db := btesting.MustCreateDB(t)
	if err := db.Update(func(tx *bolt.Tx) error {
		_, err := tx.CreateBucket([]byte("widgets"))
		if err != nil {
			t.Fatal(err)
		}

		if _, err := tx.Bucket([]byte("widgets")).CreateBucket([]byte("foo")); err != nil {
			t.Fatal(err)
		}

		if tx.Bucket([]byte("widgets")).Get([]byte("foo")) != nil {
			t.Fatal("expected nil value")
		}
		return nil
	}); err != nil {
		t.Fatal(err)
	}
}

// Ensure that a slice returned from a bucket has a capacity equal to its length.
// This also allows slices to be appended to since it will require a realloc by Go.
//
// https://github.com/boltdb/bolt/issues/544
func TestBucket_Get_Capacity(t *testing.T) {
	db := btesting.MustCreateDB(t)

	// Write key to a bucket.
	if err := db.Update(func(tx *bolt.Tx) error {
		b, err := tx.CreateBucket([]byte("bucket"))
		if err != nil {
			return err
		}
		return b.Put([]byte("key"), []byte("val"))
	}); err != nil {
		t.Fatal(err)
	}

	// Retrieve value and attempt to append to it.
	if err := db.Update(func(tx *bolt.Tx) error {
		k, v := tx.Bucket([]byte("bucket")).Cursor().First()

		// Verify capacity.
		if len(k) != cap(k) {
			t.Fatalf("unexpected key slice capacity: %d", cap(k))
		} else if len(v) != cap(v) {
			t.Fatalf("unexpected value slice capacity: %d", cap(v))
		}

		// Ensure slice can be appended to without a segfault.
		k = append(k, []byte("123")...)
		v = append(v, []byte("123")...)
		_, _ = k, v // to pass ineffassign

		return nil
	}); err != nil {
		t.Fatal(err)
	}
}

// Ensure that a bucket can write a key/value.
func TestBucket_Put(t *testing.T) {
	db := btesting.MustCreateDB(t)
	if err := db.Update(func(tx *bolt.Tx) error {
		b, err := tx.CreateBucket([]byte("widgets"))
		if err != nil {
			t.Fatal(err)
		}
		if err := b.Put([]byte("foo"), []byte("bar")); err != nil {
			t.Fatal(err)
		}

		v := tx.Bucket([]byte("widgets")).Get([]byte("foo"))
		if !bytes.Equal([]byte("bar"), v) {
			t.Fatalf("unexpected value: %v", v)
		}
		return nil
	}); err != nil {
		t.Fatal(err)
	}
}

// Ensure that a bucket can rewrite a key in the same transaction.
func TestBucket_Put_Repeat(t *testing.T) {
	db := btesting.MustCreateDB(t)
	if err := db.Update(func(tx *bolt.Tx) error {
		b, err := tx.CreateBucket([]byte("widgets"))
		if err != nil {
			t.Fatal(err)
		}
		if err := b.Put([]byte("foo"), []byte("bar")); err != nil {
			t.Fatal(err)
		}
		if err := b.Put([]byte("foo"), []byte("baz")); err != nil {
			t.Fatal(err)
		}

		value := tx.Bucket([]byte("widgets")).Get([]byte("foo"))
		if !bytes.Equal([]byte("baz"), value) {
			t.Fatalf("unexpected value: %v", value)
		}
		return nil
	}); err != nil {
		t.Fatal(err)
	}
}

// Ensure that a bucket can write a bunch of large values.
func TestBucket_Put_Large(t *testing.T) {
	db := btesting.MustCreateDB(t)

	count, factor := 100, 200
	if err := db.Update(func(tx *bolt.Tx) error {
		b, err := tx.CreateBucket([]byte("widgets"))
		if err != nil {
			t.Fatal(err)
		}
		for i := 1; i < count; i++ {
			if err := b.Put([]byte(strings.Repeat("0", i*factor)), []byte(strings.Repeat("X", (count-i)*factor))); err != nil {
				t.Fatal(err)
			}
		}
		return nil
	}); err != nil {
		t.Fatal(err)
	}

	if err := db.View(func(tx *bolt.Tx) error {
		b := tx.Bucket([]byte("widgets"))
		for i := 1; i < count; i++ {
			value := b.Get([]byte(strings.Repeat("0", i*factor)))
			if !bytes.Equal(value, []byte(strings.Repeat("X", (count-i)*factor))) {
				t.Fatalf("unexpected value: %v", value)
			}
		}
		return nil
	}); err != nil {
		t.Fatal(err)
	}
}

// Ensure that a database can perform multiple large appends safely.
func TestDB_Put_VeryLarge(t *testing.T) {
	if testing.Short() {
		t.Skip("skipping test in short mode.")
	}

	n, batchN := 400000, 200000
	ksize, vsize := 8, 500

	db := btesting.MustCreateDB(t)

	for i := 0; i < n; i += batchN {
		if err := db.Update(func(tx *bolt.Tx) error {
			b, err := tx.CreateBucketIfNotExists([]byte("widgets"))
			if err != nil {
				t.Fatal(err)
			}
			for j := 0; j < batchN; j++ {
				k, v := make([]byte, ksize), make([]byte, vsize)
				binary.BigEndian.PutUint32(k, uint32(i+j))
				if err := b.Put(k, v); err != nil {
					t.Fatal(err)
				}
			}
			return nil
		}); err != nil {
			t.Fatal(err)
		}
	}
}

// Ensure that a setting a value on a key with a bucket value returns an error.
func TestBucket_Put_IncompatibleValue(t *testing.T) {
	db := btesting.MustCreateDB(t)

	if err := db.Update(func(tx *bolt.Tx) error {
		b0, err := tx.CreateBucket([]byte("widgets"))
		if err != nil {
			t.Fatal(err)
		}

		if _, err := tx.Bucket([]byte("widgets")).CreateBucket([]byte("foo")); err != nil {
			t.Fatal(err)
		}
		if err := b0.Put([]byte("foo"), []byte("bar")); err != berrors.ErrIncompatibleValue {
			t.Fatalf("unexpected error: %s", err)
		}
		return nil
	}); err != nil {
		t.Fatal(err)
	}
}

// Ensure that a setting a value while the transaction is closed returns an error.
func TestBucket_Put_Closed(t *testing.T) {
	db := btesting.MustCreateDB(t)
	tx, err := db.Begin(true)
	if err != nil {
		t.Fatal(err)
	}

	b, err := tx.CreateBucket([]byte("widgets"))
	if err != nil {
		t.Fatal(err)
	}

	if err := tx.Rollback(); err != nil {
		t.Fatal(err)
	}

	if err := b.Put([]byte("foo"), []byte("bar")); err != berrors.ErrTxClosed {
		t.Fatalf("unexpected error: %s", err)
	}
}

// Ensure that setting a value on a read-only bucket returns an error.
func TestBucket_Put_ReadOnly(t *testing.T) {
	db := btesting.MustCreateDB(t)

	if err := db.Update(func(tx *bolt.Tx) error {
		if _, err := tx.CreateBucket([]byte("widgets")); err != nil {
			t.Fatal(err)
		}
		return nil
	}); err != nil {
		t.Fatal(err)
	}

	if err := db.View(func(tx *bolt.Tx) error {
		b := tx.Bucket([]byte("widgets"))
		if err := b.Put([]byte("foo"), []byte("bar")); err != berrors.ErrTxNotWritable {
			t.Fatalf("unexpected error: %s", err)
		}
		return nil
	}); err != nil {
		t.Fatal(err)
	}
}

// Ensure that a bucket can delete an existing key.
func TestBucket_Delete(t *testing.T) {
	db := btesting.MustCreateDB(t)

	if err := db.Update(func(tx *bolt.Tx) error {
		b, err := tx.CreateBucket([]byte("widgets"))
		if err != nil {
			t.Fatal(err)
		}
		if err := b.Put([]byte("foo"), []byte("bar")); err != nil {
			t.Fatal(err)
		}
		if err := b.Delete([]byte("foo")); err != nil {
			t.Fatal(err)
		}
		if v := b.Get([]byte("foo")); v != nil {
			t.Fatalf("unexpected value: %v", v)
		}
		return nil
	}); err != nil {
		t.Fatal(err)
	}
}

// Ensure that deleting a large set of keys will work correctly.
func TestBucket_Delete_Large(t *testing.T) {
	db := btesting.MustCreateDB(t)

	if err := db.Update(func(tx *bolt.Tx) error {
		b, err := tx.CreateBucket([]byte("widgets"))
		if err != nil {
			t.Fatal(err)
		}

		for i := 0; i < 100; i++ {
			if err := b.Put([]byte(strconv.Itoa(i)), []byte(strings.Repeat("*", 1024))); err != nil {
				t.Fatal(err)
			}
		}

		return nil
	}); err != nil {
		t.Fatal(err)
	}

	if err := db.Update(func(tx *bolt.Tx) error {
		b := tx.Bucket([]byte("widgets"))
		for i := 0; i < 100; i++ {
			if err := b.Delete([]byte(strconv.Itoa(i))); err != nil {
				t.Fatal(err)
			}
		}
		return nil
	}); err != nil {
		t.Fatal(err)
	}

	if err := db.View(func(tx *bolt.Tx) error {
		b := tx.Bucket([]byte("widgets"))
		for i := 0; i < 100; i++ {
			if v := b.Get([]byte(strconv.Itoa(i))); v != nil {
				t.Fatalf("unexpected value: %v, i=%d", v, i)
			}
		}
		return nil
	}); err != nil {
		t.Fatal(err)
	}
}

// Deleting a very large list of keys will cause the freelist to use overflow.
func TestBucket_Delete_FreelistOverflow(t *testing.T) {
	if testing.Short() {
		t.Skip("skipping test in short mode.")
	}

	db := btesting.MustCreateDB(t)

	k := make([]byte, 16)
	// The bigger the pages - the more values we need to write.
	for i := uint64(0); i < 2*uint64(db.Info().PageSize); i++ {
		if err := db.Update(func(tx *bolt.Tx) error {
			b, err := tx.CreateBucketIfNotExists([]byte("0"))
			if err != nil {
				t.Fatalf("bucket error: %s", err)
			}

			for j := uint64(0); j < 1000; j++ {
				binary.BigEndian.PutUint64(k[:8], i)
				binary.BigEndian.PutUint64(k[8:], j)
				if err := b.Put(k, nil); err != nil {
					t.Fatalf("put error: %s", err)
				}
			}

			return nil
		}); err != nil {
			t.Fatal(err)
		}
	}

	// Delete all of them in one large transaction
	if err := db.Update(func(tx *bolt.Tx) error {
		b := tx.Bucket([]byte("0"))
		c := b.Cursor()
		for k, _ := c.First(); k != nil; k, _ = c.Next() {
			if err := c.Delete(); err != nil {
				t.Fatal(err)
			}
		}
		return nil
	}); err != nil {
		t.Fatal(err)
	}

	// Check more than an overflow's worth of pages are freed.
	stats := db.Stats()
	freePages := stats.FreePageN + stats.PendingPageN
	if freePages <= 0xFFFF {
		t.Fatalf("expected more than 0xFFFF free pages, got %v", freePages)
	}

	// Free page count should be preserved on reopen.
	db.MustClose()
	db.MustReopen()
	if reopenFreePages := db.Stats().FreePageN; freePages != reopenFreePages {
		t.Fatalf("expected %d free pages, got %+v", freePages, db.Stats())
	}
	if reopenPendingPages := db.Stats().PendingPageN; reopenPendingPages != 0 {
		t.Fatalf("expected no pending pages, got %+v", db.Stats())
	}
}

// Ensure that deleting of non-existing key is a no-op.
func TestBucket_Delete_NonExisting(t *testing.T) {
	db := btesting.MustCreateDB(t)

	if err := db.Update(func(tx *bolt.Tx) error {
		b, err := tx.CreateBucket([]byte("widgets"))
		if err != nil {
			t.Fatal(err)
		}

		if _, err = b.CreateBucket([]byte("nested")); err != nil {
			t.Fatal(err)
		}
		return nil
	}); err != nil {
		t.Fatal(err)
	}

	if err := db.Update(func(tx *bolt.Tx) error {
		b := tx.Bucket([]byte("widgets"))
		if err := b.Delete([]byte("foo")); err != nil {
			t.Fatal(err)
		}
		if b.Bucket([]byte("nested")) == nil {
			t.Fatal("nested bucket has been deleted")
		}
		return nil
	}); err != nil {
		t.Fatal(err)
	}
}

// Ensure that accessing and updating nested buckets is ok across transactions.
func TestBucket_Nested(t *testing.T) {
	db := btesting.MustCreateDB(t)

	if err := db.Update(func(tx *bolt.Tx) error {
		// Create a widgets bucket.
		b, err := tx.CreateBucket([]byte("widgets"))
		if err != nil {
			t.Fatal(err)
		}

		// Create a widgets/foo bucket.
		_, err = b.CreateBucket([]byte("foo"))
		if err != nil {
			t.Fatal(err)
		}

		// Create a widgets/bar key.
		if err := b.Put([]byte("bar"), []byte("0000")); err != nil {
			t.Fatal(err)
		}

		return nil
	}); err != nil {
		t.Fatal(err)
	}
	db.MustCheck()

	// Update widgets/bar.
	if err := db.Update(func(tx *bolt.Tx) error {
		b := tx.Bucket([]byte("widgets"))
		if err := b.Put([]byte("bar"), []byte("xxxx")); err != nil {
			t.Fatal(err)
		}
		return nil
	}); err != nil {
		t.Fatal(err)
	}
	db.MustCheck()

	// Cause a split.
	if err := db.Update(func(tx *bolt.Tx) error {
		var b = tx.Bucket([]byte("widgets"))
		for i := 0; i < 10000; i++ {
			if err := b.Put([]byte(strconv.Itoa(i)), []byte(strconv.Itoa(i))); err != nil {
				t.Fatal(err)
			}
		}
		return nil
	}); err != nil {
		t.Fatal(err)
	}
	db.MustCheck()

	// Insert into widgets/foo/baz.
	if err := db.Update(func(tx *bolt.Tx) error {
		var b = tx.Bucket([]byte("widgets"))
		if err := b.Bucket([]byte("foo")).Put([]byte("baz"), []byte("yyyy")); err != nil {
			t.Fatal(err)
		}
		return nil
	}); err != nil {
		t.Fatal(err)
	}
	db.MustCheck()

	// Verify.
	if err := db.View(func(tx *bolt.Tx) error {
		var b = tx.Bucket([]byte("widgets"))
		if v := b.Bucket([]byte("foo")).Get([]byte("baz")); !bytes.Equal(v, []byte("yyyy")) {
			t.Fatalf("unexpected value: %v", v)
		}
		if v := b.Get([]byte("bar")); !bytes.Equal(v, []byte("xxxx")) {
			t.Fatalf("unexpected value: %v", v)
		}
		for i := 0; i < 10000; i++ {
			if v := b.Get([]byte(strconv.Itoa(i))); !bytes.Equal(v, []byte(strconv.Itoa(i))) {
				t.Fatalf("unexpected value: %v", v)
			}
		}
		return nil
	}); err != nil {
		t.Fatal(err)
	}
}

// Ensure that deleting a bucket using Delete() returns an error.
func TestBucket_Delete_Bucket(t *testing.T) {
	db := btesting.MustCreateDB(t)
	if err := db.Update(func(tx *bolt.Tx) error {
		b, err := tx.CreateBucket([]byte("widgets"))
		if err != nil {
			t.Fatal(err)
		}
		if _, err := b.CreateBucket([]byte("foo")); err != nil {
			t.Fatal(err)
		}
		if err := b.Delete([]byte("foo")); err != berrors.ErrIncompatibleValue {
			t.Fatalf("unexpected error: %s", err)
		}
		return nil
	}); err != nil {
		t.Fatal(err)
	}
}

// Ensure that deleting a key on a read-only bucket returns an error.
func TestBucket_Delete_ReadOnly(t *testing.T) {
	db := btesting.MustCreateDB(t)

	if err := db.Update(func(tx *bolt.Tx) error {
		if _, err := tx.CreateBucket([]byte("widgets")); err != nil {
			t.Fatal(err)
		}
		return nil
	}); err != nil {
		t.Fatal(err)
	}

	if err := db.View(func(tx *bolt.Tx) error {
		if err := tx.Bucket([]byte("widgets")).Delete([]byte("foo")); err != berrors.ErrTxNotWritable {
			t.Fatalf("unexpected error: %s", err)
		}
		return nil
	}); err != nil {
		t.Fatal(err)
	}
}

// Ensure that a deleting value while the transaction is closed returns an error.
func TestBucket_Delete_Closed(t *testing.T) {
	db := btesting.MustCreateDB(t)

	tx, err := db.Begin(true)
	if err != nil {
		t.Fatal(err)
	}

	b, err := tx.CreateBucket([]byte("widgets"))
	if err != nil {
		t.Fatal(err)
	}

	if err := tx.Rollback(); err != nil {
		t.Fatal(err)
	}
	if err := b.Delete([]byte("foo")); err != berrors.ErrTxClosed {
		t.Fatalf("unexpected error: %s", err)
	}
}

// Ensure that deleting a bucket causes nested buckets to be deleted.
func TestBucket_DeleteBucket_Nested(t *testing.T) {
	db := btesting.MustCr
... [TRUNCATED]
```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
