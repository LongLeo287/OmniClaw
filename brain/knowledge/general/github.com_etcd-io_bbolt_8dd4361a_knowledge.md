---
id: github.com-etcd-io-bbolt-8dd4361a-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:45.845090
---

# KNOWLEDGE EXTRACT: github.com_etcd-io_bbolt_8dd4361a
> **Extracted on:** 2026-04-01 16:09:13
> **Source:** D:/LongLeo/AI OS CORP/AI OS/core/security/QUARANTINE/KI-BATCH-20260331205007524936/github.com_etcd-io_bbolt_8dd4361a

---

## File: `.gitattributes`
```
# ensure that line endings for Windows builds are properly formatted
# see https://github.com/golangci/golangci-lint-action?tab=readme-ov-file#how-to-use
# at "Multiple OS Example" section
*.go text eol=lf
```

## File: `.gitignore`
```
*.prof
*.test
*.swp
/bin/
cover.out
cover-*.out
/.idea
*.iml
/bbolt
/cmd/bbolt/bbolt
.DS_Store

```

## File: `.go-version`
```
1.25.8
```

## File: `.golangci.yaml`
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

## File: `LICENSE`
```
The MIT License (MIT)

Copyright (c) 2013 Ben Johnson

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```

## File: `Makefile`
```
BRANCH=`git rev-parse --abbrev-ref HEAD`
COMMIT=`git rev-parse --short HEAD`
GOLDFLAGS="-X main.branch $(BRANCH) -X main.commit $(COMMIT)"
GOFILES = $(shell find . -name \*.go)
REPOSITORY_ROOT := $(shell git rev-parse --show-toplevel)
GOTOOLCHAIN ?= go$(shell cat $(REPOSITORY_ROOT)/.go-version)

TESTFLAGS_RACE=-race=false
ifdef ENABLE_RACE
	TESTFLAGS_RACE=-race=true
endif

TESTFLAGS_CPU=
ifdef CPU
	TESTFLAGS_CPU=-cpu=$(CPU)
endif
TESTFLAGS = $(TESTFLAGS_RACE) $(TESTFLAGS_CPU) $(EXTRA_TESTFLAGS)

TESTFLAGS_TIMEOUT=30m
ifdef TIMEOUT
	TESTFLAGS_TIMEOUT=$(TIMEOUT)
endif

TESTFLAGS_ENABLE_STRICT_MODE=false
ifdef ENABLE_STRICT_MODE
	TESTFLAGS_ENABLE_STRICT_MODE=$(ENABLE_STRICT_MODE)
endif

.EXPORT_ALL_VARIABLES:
TEST_ENABLE_STRICT_MODE=${TESTFLAGS_ENABLE_STRICT_MODE}

.PHONY: fmt
fmt:
	@echo "Verifying gofmt, failures can be fixed with ./scripts/fix.sh"
	@!(gofmt -l -s -d ${GOFILES} | grep '[a-z]')

	@echo "Verifying goimports, failures can be fixed with ./scripts/fix.sh"
	@!(go tool golang.org/x/tools/cmd/goimports -l -d ${GOFILES} | grep '[a-z]')

.PHONY: lint
lint:
	golangci-lint run ./...

.PHONY: test
test:
	@echo "hashmap freelist test"
	BBOLT_VERIFY=all TEST_FREELIST_TYPE=hashmap go test -v ${TESTFLAGS} -timeout ${TESTFLAGS_TIMEOUT}
	BBOLT_VERIFY=all TEST_FREELIST_TYPE=hashmap go test -v ${TESTFLAGS} ./internal/...
	BBOLT_VERIFY=all TEST_FREELIST_TYPE=hashmap go test -v ${TESTFLAGS} ./cmd/bbolt/...

	@echo "array freelist test"
	BBOLT_VERIFY=all TEST_FREELIST_TYPE=array go test -v ${TESTFLAGS} -timeout ${TESTFLAGS_TIMEOUT}
	BBOLT_VERIFY=all TEST_FREELIST_TYPE=array go test -v ${TESTFLAGS} ./internal/...
	BBOLT_VERIFY=all TEST_FREELIST_TYPE=array go test -v ${TESTFLAGS} ./cmd/bbolt/...

.PHONY: coverage
coverage:
	@echo "hashmap freelist test"
	TEST_FREELIST_TYPE=hashmap go test -v -timeout ${TESTFLAGS_TIMEOUT} \
		-coverprofile cover-freelist-hashmap.out -covermode atomic

	@echo "array freelist test"
	TEST_FREELIST_TYPE=array go test -v -timeout ${TESTFLAGS_TIMEOUT} \
		-coverprofile cover-freelist-array.out -covermode atomic

BOLT_CMD=bbolt

build:
	go build -o bin/${BOLT_CMD} ./cmd/${BOLT_CMD}

.PHONY: clean
clean: # Clean binaries
	rm -f ./bin/${BOLT_CMD}

.PHONY: gofail-enable
gofail-enable:
	go tool go.etcd.io/gofail enable .

.PHONY: gofail-disable
gofail-disable:
	go tool go.etcd.io/gofail disable .

.PHONY: test-failpoint
test-failpoint:
	@echo "[failpoint] hashmap freelist test"
	BBOLT_VERIFY=all TEST_FREELIST_TYPE=hashmap go test -v ${TESTFLAGS} -timeout 30m ./tests/failpoint

	@echo "[failpoint] array freelist test"
	BBOLT_VERIFY=all TEST_FREELIST_TYPE=array go test -v ${TESTFLAGS} -timeout 30m ./tests/failpoint

.PHONY: test-robustness # Running robustness tests requires root permission for now
# TODO: Remove sudo once we fully migrate to the prow infrastructure
test-robustness: gofail-enable build
	sudo env PATH=$$PATH go test -v ${TESTFLAGS} ./tests/dmflakey -test.root
	sudo env PATH=$(PWD)/bin:$$PATH go test -v ${TESTFLAGS} ${ROBUSTNESS_TESTFLAGS} ./tests/robustness -test.root

.PHONY: test-benchmark-compare
# Runs benchmark tests on the current git ref and the given REF, and compares
# the two.
test-benchmark-compare:
	@git fetch
	./scripts/compare_benchmarks.sh $(REF)
```

## File: `OWNERS`
```
# See the OWNERS docs at https://go.k8s.io/owners

approvers:
  - ahrtr           # Benjamin Wang <benjamin.ahrtr@gmail.com> <benjamin.wang@broadcom.com>
  - serathius       # Marek Siarkowicz <siarkowicz@google.com> <marek.siarkowicz@gmail.com>
  - ptabor          # Piotr Tabor <piotr.tabor@gmail.com>
  - spzala          # Sahdev Zala <spzala@us.ibm.com>
reviewers:
  - elbehery        # Mustafa Elbehery <elbeherymustafa@gmail.com>
  - fuweid          # Wei Fu <fuweid89@gmail.com>
  - tjungblu        # Thomas Jungblut <tjungblu@redhat.com>
```

## File: `README.md`
```markdown
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
db.View(func(tx *bolt.Tx) error {
	// Assume bucket exists and has keys
	c := tx.Bucket([]byte("MyBucket")).Cursor()

	prefix := []byte("1234")
	for k, v := c.Seek(prefix); k != nil && bytes.HasPrefix(k, prefix); k, v = c.Next() {
		fmt.Printf("key=%s, value=%s\n", k, v)
	}

	return nil
})
```

#### Range scans

Another common use case is scanning over a range such as a time range. If you
use a sortable time encoding such as RFC3339 then you can query a specific
date range like this:

```go
db.View(func(tx *bolt.Tx) error {
	// Assume our events bucket exists and has RFC3339 encoded time keys.
	c := tx.Bucket([]byte("Events")).Cursor()

	// Our time range spans the 90's decade.
	min := []byte("1990-01-01T00:00:00Z")
	max := []byte("2000-01-01T00:00:00Z")

	// Iterate over the 90's.
	for k, v := c.Seek(min); k != nil && bytes.Compare(k, max) <= 0; k, v = c.Next() {
		fmt.Printf("%s: %s\n", k, v)
	}

	return nil
})
```

Note that, while RFC3339 is sortable, the Golang implementation of RFC3339Nano does not use a fixed number of digits after the decimal point and is therefore not sortable.


#### ForEach()

You can also use the function `ForEach()` if you know you'll be iterating over
all the keys in a bucket:

```go
db.View(func(tx *bolt.Tx) error {
	// Assume bucket exists and has keys
	b := tx.Bucket([]byte("MyBucket"))

	b.ForEach(func(k, v []byte) error {
		fmt.Printf("key=%s, value=%s\n", k, v)
		return nil
	})
	return nil
})
```

Please note that keys and values in `ForEach()` are only valid while
the transaction is open. If you need to use a key or value outside of
the transaction, you must use `copy()` to copy it to another byte
slice.

### Nested buckets

You can also store a bucket in a key to create nested buckets. The API is the
same as the bucket management API on the `DB` object:

```go
func (*Bucket) CreateBucket(key []byte) (*Bucket, error)
func (*Bucket) CreateBucketIfNotExists(key []byte) (*Bucket, error)
func (*Bucket) DeleteBucket(key []byte) error
```

Say you had a multi-tenant application where the root level bucket was the account bucket. Inside of this bucket was a sequence of accounts which themselves are buckets. And inside the sequence bucket you could have many buckets pertaining to the Account itself (Users, Notes, etc) isolating the information into logical groupings.

```go

// createUser creates a new user in the given account.
func createUser(accountID int, u *User) error {
    // Start the transaction.
    tx, err := db.Begin(true)
    if err != nil {
        return err
    }
    defer tx.Rollback()

    // Retrieve the root bucket for the account.
    // Assume this has already been created when the account was set up.
    root := tx.Bucket([]byte(strconv.FormatUint(accountID, 10)))

    // Setup the users bucket.
    bkt, err := root.CreateBucketIfNotExists([]byte("USERS"))
    if err != nil {
        return err
    }

    // Generate an ID for the new user.
    userID, err := bkt.NextSequence()
    if err != nil {
        return err
    }
    u.ID = userID

    // Marshal and save the encoded user.
    if buf, err := json.Marshal(u); err != nil {
        return err
    } else if err := bkt.Put([]byte(strconv.FormatUint(u.ID, 10)), buf); err != nil {
        return err
    }

    // Commit the transaction.
    if err := tx.Commit(); err != nil {
        return err
    }

    return nil
}

```




### Database backups

Bolt is a single file so it's easy to backup. You can use the `Tx.WriteTo()`
function to write a consistent view of the database to a writer. If you call
this from a read-only transaction, it will perform a hot backup and not block
your other database reads and writes.

By default, it will use a regular file handle which will utilize the operating
system's page cache. See the [`Tx`](https://godoc.org/go.etcd.io/bbolt#Tx)
documentation for information about optimizing for larger-than-RAM datasets.

One common use case is to backup over HTTP so you can use tools like `cURL` to
do database backups:

```go
func BackupHandleFunc(w http.ResponseWriter, req *http.Request) {
	err := db.View(func(tx *bolt.Tx) error {
		w.Header().Set("Content-Type", "application/octet-stream")
		w.Header().Set("Content-Disposition", `attachment; filename="my.db"`)
		w.Header().Set("Content-Length", strconv.Itoa(int(tx.Size())))
		_, err := tx.WriteTo(w)
		return err
	})
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
	}
}
```

Then you can backup using this command:

```sh
$ curl http://localhost/backup > my.db
```

Or you can open your browser to `http://localhost/backup` and it will download
automatically.

If you want to backup to another file you can use the `Tx.CopyFile()` helper
function.


### Statistics

The database keeps a running count of many of the internal operations it
performs so you can better understand what's going on. By grabbing a snapshot
of these stats at two points in time we can see what operations were performed
in that time range.

For example, we could start a goroutine to log stats every 10 seconds:

```go
go func() {
	// Grab the initial stats.
	prev := db.Stats()

	for {
		// Wait for 10s.
		time.Sleep(10 * time.Second)

		// Grab the current stats and diff them.
		stats := db.Stats()
		diff := stats.Sub(&prev)

		// Encode stats to JSON and print to STDERR.
		json.NewEncoder(os.Stderr).Encode(diff)

		// Save stats for the next loop.
		prev = stats
	}
}()
```

It's also useful to pipe these stats to a service such as statsd for monitoring
or to provide an HTTP endpoint that will perform a fixed-length sample.


### Read-Only Mode

Sometimes it is useful to create a shared, read-only Bolt database. To this,
set the `Options.ReadOnly` flag when opening your database. Read-only mode
uses a shared lock to allow multiple processes to read from the database but
it will block any processes from opening the database in read-write mode.

```go
db, err := bolt.Open("my.db", 0600, &bolt.Options{ReadOnly: true})
if err != nil {
	log.Fatal(err)
}
```

### Mobile Use (iOS/Android)

Bolt is able to run on mobile devices by leveraging the binding feature of the
[gomobile](https://github.com/golang/mobile) tool. Create a struct that will
contain your database logic and a reference to a `*bolt.DB` with a initializing
constructor that takes in a filepath where the database file will be stored.
Neither Android nor iOS require extra permissions or cleanup from using this method.

```go
func NewBoltDB(filepath string) *BoltDB {
	db, err := bolt.Open(filepath+"/demo.db", 0600, nil)
	if err != nil {
		log.Fatal(err)
	}

	return &BoltDB{db}
}

type BoltDB struct {
	db *bolt.DB
	...
}

func (b *BoltDB) Path() string {
	return b.db.Path()
}

func (b *BoltDB) Close() {
	b.db.Close()
}
```

Database logic should be defined as methods on this wrapper struct.

To initialize this struct from the native language (both platforms now sync
their local storage to the cloud. These snippets disable that functionality for the
database file):

#### Android

```java
String path;
if (android.os.Build.VERSION.SDK_INT >=android.os.Build.VERSION_CODES.LOLLIPOP){
    path = getNoBackupFilesDir().getAbsolutePath();
} else{
    path = getFilesDir().getAbsolutePath();
}
Boltmobiledemo.BoltDB boltDB = Boltmobiledemo.NewBoltDB(path)
```

#### iOS

```objc
- (void)demo {
    NSString* path = [NSSearchPathForDirectoriesInDomains(NSLibraryDirectory,
                                                          NSUserDomainMask,
                                                          YES) objectAtIndex:0];
	GoBoltmobiledemoBoltDB * demo = GoBoltmobiledemoNewBoltDB(path);
	[self addSkipBackupAttributeToItemAtPath:demo.path];
	//Some DB Logic would go here
	[demo close];
}

- (BOOL)addSkipBackupAttributeToItemAtPath:(NSString *) filePathString
{
    NSURL* URL= [NSURL fileURLWithPath: filePathString];
    assert([[NSFileManager defaultManager] fileExistsAtPath: [URL path]]);

    NSError *error = nil;
    BOOL success = [URL setResourceValue: [NSNumber numberWithBool: YES]
                                  forKey: NSURLIsExcludedFromBackupKey error: &error];
    if(!success){
        NSLog(@"Error excluding %@ from backup %@", [URL lastPathComponent], error);
    }
    return success;
}

```

## Resources

For more information on getting started with Bolt, check out the following articles:

* [Intro to BoltDB: Painless Performant Persistence](http://npf.io/2014/07/intro-to-boltdb-painless-performant-persistence/) by [Nate Finch](https://github.com/natefinch).
* [Bolt -- an embedded key/value database for Go](https://www.progville.com/go/bolt-embedded-db-golang/) by Progville


## Comparison with other databases

### Postgres, MySQL, & other relational databases

Relational databases structure data into rows and are only accessible through
the use of SQL. This approach provides flexibility in how you store and query
your data but also incurs overhead in parsing and planning SQL statements. Bolt
accesses all data by a byte slice key. This makes Bolt fast to read and write
data by key but provides no built-in support for joining values together.

Most relational databases (with the exception of SQLite) are standalone servers
that run separately from your application. This gives your systems
flexibility to connect multiple application servers to a single database
server but also adds overhead in serializing and transporting data over the
network. Bolt runs as a library included in your application so all data access
has to go through your application's process. This brings data closer to your
application but limits multi-process access to the data.


### LevelDB, RocksDB

LevelDB and its derivatives (RocksDB, HyperLevelDB) are similar to Bolt in that
they are libraries bundled into the application, however, their underlying
structure is a log-structured merge-tree (LSM tree). An LSM tree optimizes
random writes by using a write ahead log and multi-tiered, sorted files called
SSTables. Bolt uses a B+tree internally and only a single file. Both approaches
have trade-offs.

If you require a high random write throughput (>10,000 w/sec) or you need to use
spinning disks then LevelDB could be a good choice. If your application is
read-heavy or does a lot of range scans then Bolt could be a good choice.

One other important consideration is that LevelDB does not have transactions.
It supports batch writing of key/values pairs and it supports read snapshots
but it will not give you the ability to do a compare-and-swap operation safely.
Bolt supports fully serializable ACID transactions.


### LMDB

Bolt was originally a port of LMDB so it is architecturally similar. Both use
a B+tree, have ACID semantics with fully serializable transactions, and support
lock-free MVCC using a single writer and multiple readers.

The two projects have somewhat diverged. LMDB heavily focuses on raw performance
while Bolt has focused on simplicity and ease of use. For example, LMDB allows
several unsafe actions such as direct writes for the sake of performance. Bolt
opts to disallow actions which can leave the database in a corrupted state. The
only exception to this in Bolt is `DB.NoSync`.

There are also a few differences in API. LMDB requires a maximum mmap size when
opening an `mdb_env` whereas Bolt will handle incremental mmap resizing
automatically. LMDB overloads the getter and setter functions with multiple
flags whereas Bolt splits these specialized cases into their own functions.


## Caveats & Limitations

It's important to pick the right tool for the job and Bolt is no exception.
Here are a few things to note when evaluating and using Bolt:

* Bolt is good for read intensive workloads. Sequential write performance is
  also fast but random writes can be slow. You can use `DB.Batch()` or add a
  write-ahead log to help mitigate this issue.

* Bolt uses a B+tree internally so there can be a lot of random page access.
  SSDs provide a significant performance boost over spinning disks.

* Try to avoid long running read transactions. Bolt uses copy-on-write so
  old pages cannot be reclaimed while an old transaction is using them.

* Byte slices returned from Bolt are only valid during a transaction. Once the
  transaction has been committed or rolled back then the memory they point to
  can be reused by a new page or can be unmapped from virtual memory and you'll
  see an `unexpected fault address` panic when accessing it.

* Bolt uses an exclusive write lock on the database file so it cannot be
  shared by multiple processes.

* Be careful when using `Bucket.FillPercent`. Setting a high fill percent for
  buckets that have random inserts will cause your database to have very poor
  page utilization.

* Use larger buckets in general. Smaller buckets causes poor page utilization
  once they become larger than the page size (typically 4KB).

* Bulk loading a lot of random writes into a new bucket can be slow as the
  page will not split until the transaction is committed. Randomly inserting
  more than 100,000 key/value pairs into a single new bucket in a single
  transaction is not advised.

* Bolt uses a memory-mapped file so the underlying operating system handles the
  caching of the data. Typically, the OS will cache as much of the file as it
  can in memory and will release memory as needed to other processes. This means
  that Bolt can show very high memory usage when working with large databases.
  However, this is expected and the OS will release memory as needed. Bolt can
  handle databases much larger than the available physical RAM, provided its
  memory-map fits in the process virtual address space. It may be problematic
  on 32-bits systems.

* The data structures in the Bolt database are memory mapped so the data file
  will be endian specific. This means that you cannot copy a Bolt file from a
  little endian machine to a big endian machine and have it work. For most
  users this is not a concern since most modern CPUs are little endian.

* Because of the way pages are laid out on disk, Bolt cannot truncate data files
  and return free pages back to the disk. Instead, Bolt maintains a free list
  of unused pages within its data file. These free pages can be reused by later
  transactions. This works well for many use cases as databases generally tend
  to grow. However, it's important to note that deleting large chunks of data
  will not allow you to reclaim that space on disk.

  For more information on page allocation, [see this comment][page-allocation].

* Removing key/values pairs in a bucket during iteration on the bucket using
  cursor may not work properly. Each time when removing a key/value pair, the
  cursor may automatically move to the next position if present. When users
  call `c.Next()` after removing a key, it may skip one key/value pair.
  Refer to https://github.com/etcd-io/bbolt/pull/611 for more detailed info.

* Bolt db can be corrupted during the initialization phase due to abrupt power failure.
  - Please note: This issue can only be reproduced during the very first initialization phase, when there is
  no existing data in bolt database.
  - In normal production environment, it is difficult to reproduce this. Once the database file has been initialized, it can no longer occur.
  - Please refer to this issue for more details: https://github.com/etcd-io/etcd/issues/16596.

[page-allocation]: https://github.com/boltdb/bolt/issues/308#issuecomment-74811638


## Reading the Source

Bolt is a relatively small code base (<5KLOC) for an embedded, serializable,
transactional key/value database so it can be a good starting point for people
interested in how databases work.

The best places to start are the main entry points into Bolt:

- `Open()` - Initializes the reference to the database. It's responsible for
  creating the database if it doesn't exist, obtaining an exclusive lock on the
  file, reading the meta pages, & memory-mapping the file.

- `DB.Begin()` - Starts a read-only or read-write transaction depending on the
  value of the `writable` argument. This requires briefly obtaining the "meta"
  lock to keep track of open transactions. Only one read-write transaction can
  exist at a time so the "rwlock" is acquired during the life of a read-write
  transaction.

- `Bucket.Put()` - Writes a key/value pair into a bucket. After validating the
  arguments, a cursor is used to traverse the B+tree to the page and position
  where the key & value will be written. Once the position is found, the bucket
  materializes the underlying page and the page's parent pages into memory as
  "nodes". These nodes are where mutations occur during read-write transactions.
  These changes get flushed to disk during commit.

- `Bucket.Get()` - Retrieves a key/value pair from a bucket. This uses a cursor
  to move to the page & position of a key/value pair. During a read-only
  transaction, the key and value data is returned as a direct reference to the
  underlying mmap file so there's no allocation overhead. For read-write
  transactions, this data may reference the mmap file or one of the in-memory
  node values.

- `Cursor` - This object is simply for traversing the B+tree of on-disk pages
  or in-memory nodes. It can seek to a specific key, move to the first or last
  value, or it can move forward or backward. The cursor handles the movement up
  and down the B+tree transparently to the end user.

- `Tx.Commit()` - Converts the in-memory dirty nodes and the list of free pages
  into pages to be written to disk. Writing to disk then occurs in two phases.
  First, the dirty pages are written to disk and an `fsync()` occurs. Second, a
  new meta page with an incremented transaction ID is written and another
  `fsync()` occurs. This two phase write ensures that partially written data
  pages are ignored in the event of a crash since the meta page pointing to them
  is never written. Partially written meta pages are invalidated because they
  are written with a checksum.

If you have additional notes that could be helpful for others, please submit
them via pull request.

## Known Issues

- bbolt might run into data corruption issue on Linux when the feature
  [ext4: fast commit](https://lwn.net/Articles/842385/), which was introduced in
  linux kernel version v5.10, is enabled. The fixes to the issue are included in
  stable LTS patchlevels 5.10.94+ and 5.15.17+ (ftruncate tracking), plus
  5.15.27+ (ineligible-commit fallback). Linux 5.17 includes these fixes as
  well, but 5.17 is not an LTS release. Please refer to links below,

  * [ext4: fast commit may miss tracking unwritten range during ftruncate](https://lore.kernel.org/linux-ext4/20211223032337.5198-3-yinxin.x@bytedance.com/)
    * [5.10.94 stable backport](https://lore.kernel.org/stable/20220124184041.063143682@linuxfoundation.org/)
    * [5.15.17 stable backport](https://lore.kernel.org/stable/20220124184125.887304707@linuxfoundation.org/)
  * [ext4: fast commit may not fallback for ineligible commit](https://lore.kernel.org/lkml/202201091544.W5HHEXAp-lkp@intel.com/T/#ma0768815e4b5f671e9e451d578256ef9a76fe30e)
    * [5.15.27 stable backport](https://lore.kernel.org/stable/20220307091703.544901888@linuxfoundation.org/)
  * [ext4 updates for 5.17](https://lore.kernel.org/lkml/YdyxjTFaLWif6BCM@mit.edu/)

  Please also refer to the discussion in https://github.com/etcd-io/bbolt/issues/562.

- Writing a value with a length of 0 will always result in reading back an empty `[]byte{}` value.
  Please refer to [issues/726#issuecomment-2061694802](https://github.com/etcd-io/bbolt/issues/726#issuecomment-2061694802).

## Other Projects Using Bolt

Below is a list of public, open source projects that use Bolt:

* [Algernon](https://github.com/xyproto/algernon) - A HTTP/2 web server with built-in support for Lua. Uses BoltDB as the default database backend.
* [Bazil](https://bazil.org/) - A file system that lets your data reside where it is most convenient for it to reside.
* [bolter](https://github.com/hasit/bolter) - Command-line app for viewing BoltDB file in your terminal.
* [boltcli](https://github.com/spacewander/boltcli) - the redis-cli for boltdb with Lua script support.
* [BoltHold](https://github.com/timshannon/bolthold) - An embeddable NoSQL store for Go types built on BoltDB
* [BoltStore](https://github.com/yosssi/boltstore) - Session store using Bolt.
* [Boltdb Boilerplate](https://github.com/bobintornado/boltdb-boilerplate) - Boilerplate wrapper around bolt aiming to make simple calls one-liners.
* [BoltDbWeb](https://github.com/evnix/boltdbweb) - A web based GUI for BoltDB files.
* [BoltDB Viewer](https://github.com/zc310/rich_boltdb) - A BoltDB Viewer Can run on Windows、Linux、Android system.
* [bleve](http://www.blevesearch.com/) - A pure Go search engine similar to ElasticSearch that uses Bolt as the default storage backend.
* [bstore](https://github.com/mjl-/bstore) - Database library storing Go values, with referential/unique/nonzero constraints, indices, automatic schema management with struct tags, and a query API.
* [btcwallet](https://github.com/btcsuite/btcwallet) - A bitcoin wallet.
* [buckets](https://github.com/joyrexus/buckets) - a bolt wrapper streamlining
  simple tx and key scans.
* [Buildkit](https://github.com/moby/buildkit) - concurrent, cache-efficient, and Dockerfile-agnostic builder toolkit
* [cayley](https://github.com/google/cayley) - Cayley is an open-source graph database using Bolt as optional backend.
* [ChainStore](https://github.com/pressly/chainstore) - Simple key-value interface to a variety of storage engines organized as a chain of operations.
* [🌰 Chestnut](https://github.com/jrapoport/chestnut) - Chestnut is encrypted storage for Go.
* [Consul](https://github.com/hashicorp/consul) - Consul is service discovery and configuration made easy. Distributed, highly available, and datacenter-aware.
* [Containerd](https://github.com/containerd/containerd) - An open and reliable container runtime
* [DVID](https://github.com/janelia-flyem/dvid) - Added Bolt as optional storage engine and testing it against Basho-tuned leveldb.
* [dcrwallet](https://github.com/decred/dcrwallet) - A wallet for the Decred cryptocurrency.
* [drive](https://github.com/odeke-em/drive) - drive is an unofficial Google Drive command line client for \*NIX operating systems.
* [event-shuttle](https://github.com/sclasen/event-shuttle) - A Unix system service to collect and reliably deliver messages to Kafka.
* [Freehold](http://tshannon.bitbucket.org/freehold/) - An open, secure, and lightweight platform for your files and data.
* [Go Report Card](https://goreportcard.com/) - Go code quality report cards as a (free and open source) service.
* [GoWebApp](https://github.com/josephspurrier/gowebapp) - A basic MVC web application in Go using BoltDB.
* [GoShort](https://github.com/pankajkhairnar/goShort) - GoShort is a URL shortener written in Golang and BoltDB for persistent key/value storage and for routing it's using high performent HTTPRouter.
* [gopherpit](https://github.com/gopherpit/gopherpit) - A web service to manage Go remote import paths with custom domains
* [gokv](https://github.com/philippgille/gokv) - Simple key-value store abstraction and implementations for Go (Redis, Consul, etcd, bbolt, BadgerDB, LevelDB, Memcached, DynamoDB, S3, PostgreSQL, MongoDB, CockroachDB and many more)
* [goraphdb](https://github.com/mstrYoda/goraphdb) - A graph database provides Cypher query, fluent builder and management UI.
* [Gitchain](https://github.com/gitchain/gitchain) - Decentralized, peer-to-peer Git repositories aka "Git meets Bitcoin".
* [InfluxDB](https://influxdata.com) - Scalable datastore for metrics, events, and real-time analytics.
* [ipLocator](https://github.com/AndreasBriese/ipLocator) - A fast ip-geo-location-server using bolt with bloom filters.
* [ipxed](https://github.com/kelseyhightower/ipxed) - Web interface and api for ipxed.
* [Ironsmith](https://github.com/timshannon/ironsmith) - A simple, script-driven continuous integration (build - > test -> release) tool, with no external dependencies
* [Kala](https://github.com/ajvb/kala) - Kala is a modern job scheduler optimized to run on a single node. It is persistent, JSON over HTTP API, ISO 8601 duration notation, and dependent jobs.
* [Key Value Access Language (KVAL)](https://github.com/kval-access-language) - A proposed grammar for key-value datastores offering a bbolt binding.
* [LedisDB](https://github.com/siddontang/ledisdb) - A high performance NoSQL, using Bolt as optional storage.
* [lru](https://github.com/crowdriff/lru) - Easy to use Bolt-backed Least-Recently-Used (LRU) read-through cache with chainable remote stores.
* [mbuckets](https://github.com/abhigupta912/mbuckets) - A Bolt wrapper that allows easy operations on multi level (nested) buckets.
* [MetricBase](https://github.com/msiebuhr/MetricBase) - Single-binary version of Graphite.
* [MuLiFS](https://github.com/dankomiocevic/mulifs) - Music Library Filesystem creates a filesystem to organise your music files.
* [NATS](https://github.com/nats-io/nats-streaming-server) - NATS Streaming uses bbolt for message and metadata storage.
* [Portainer](https://github.com/portainer/portainer) - A lightweight service delivery platform for containerized applications that can be used to manage Docker, Swarm, Kubernetes and ACI environments.
* [Prometheus Annotation Server](https://github.com/oliver006/prom_annotation_server) - Annotation server for PromDash & Prometheus service monitoring system.
* [Rain](https://github.com/cenkalti/rain) - BitTorrent client and library.
* [reef-pi](https://github.com/reef-pi/reef-pi) - reef-pi is an award winning, modular, DIY reef tank controller using easy to learn electronics based on a Raspberry Pi.
* [Request Baskets](https://github.com/darklynx/request-baskets) - A web service to collect arbitrary HTTP requests and inspect them via REST API or simple web UI, similar to [RequestBin](http://requestb.in/) service
* [Seaweed File System](https://github.com/chrislusf/seaweedfs) - Highly scalable distributed key~file system with O(1) disk read.
* [stow](https://github.com/djherbis/stow) -  a persistence manager for objects
  backed by boltdb.
* [Storm](https://github.com/asdine/storm) - Simple and powerful ORM for BoltDB.
* [SimpleBolt](https://github.com/xyproto/simplebolt) - A simple way to use BoltDB. Deals mainly with strings.
* [Skybox Analytics](https://github.com/skybox/skybox) - A standalone funnel analysis tool for web analytics.
* [Scuttlebutt](https://github.com/benbjohnson/scuttlebutt) - Uses Bolt to store and process all Twitter mentions of GitHub projects.
* [tentacool](https://github.com/optiflows/tentacool) - REST api server to manage system stuff (IP, DNS, Gateway...) on a linux server.
* [torrent](https://github.com/anacrolix/torrent) - Full-featured BitTorrent client package and utilities in Go. BoltDB is a storage backend in development.
* [Wiki](https://github.com/peterhellberg/wiki) - A tiny wiki using Goji, BoltDB and Blackfriday.

If you are using Bolt in a project please send a pull request to add it to the list.
```

## File: `allocate_test.go`
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

## File: `bolt_aix.go`
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

## File: `bolt_android.go`
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

## File: `bolt_linux.go`
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

## File: `bolt_openbsd.go`
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

## File: `bolt_solaris.go`
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

## File: `bolt_unix.go`
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

## File: `bolt_windows.go`
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

## File: `boltsync_unix.go`
```go
//go:build !windows && !plan9 && !linux && !openbsd

package bbolt

// fdatasync flushes written data to a file descriptor.
func fdatasync(db *DB) error {
	return db.file.Sync()
}
```

## File: `bucket.go`
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
	} else if !b.Writable() {
		return errors.ErrTxNotWritable
	}

	// Move cursor to correct position.
	c := b.Cursor()
	k, _, flags := c.seek(key)

	// Return nil if the key doesn't exist.
	if !bytes.Equal(key, k) {
		return nil
	}

	// Return an error if there is already existing bucket value.
	if (flags & common.BucketLeafFlag) != 0 {
		return errors.ErrIncompatibleValue
	}

	// Delete the node if we have a matching key.
	c.node().del(key)

	return nil
}

// Sequence returns the current integer for the bucket without incrementing it.
func (b *Bucket) Sequence() uint64 {
	return b.InSequence()
}

// SetSequence updates the sequence number for the bucket.
func (b *Bucket) SetSequence(v uint64) error {
	if b.tx.db == nil {
		return errors.ErrTxClosed
	} else if !b.Writable() {
		return errors.ErrTxNotWritable
	}

	// Materialize the root node if it hasn't been already so that the
	// bucket will be saved during commit.
	if b.rootNode == nil {
		_ = b.node(b.RootPage(), nil)
	}

	// Set the sequence.
	b.SetInSequence(v)
	return nil
}

// NextSequence returns an autoincrementing integer for the bucket.
func (b *Bucket) NextSequence() (uint64, error) {
	if b.tx.db == nil {
		return 0, errors.ErrTxClosed
	} else if !b.Writable() {
		return 0, errors.ErrTxNotWritable
	}

	// Materialize the root node if it hasn't been already so that the
	// bucket will be saved during commit.
	if b.rootNode == nil {
		_ = b.node(b.RootPage(), nil)
	}

	// Increment and return the sequence.
	b.IncSequence()
	return b.Sequence(), nil
}

// ForEach executes a function for each key/value pair in a bucket.
// Because ForEach uses a Cursor, the iteration over keys is in lexicographical order.
// If the provided function returns an error then the iteration is stopped and
// the error is returned to the caller. The provided function must not modify
// the bucket; this will result in undefined behavior.
func (b *Bucket) ForEach(fn func(k, v []byte) error) error {
	if b.tx.db == nil {
		return errors.ErrTxClosed
	}
	c := b.Cursor()
	for k, v := c.First(); k != nil; k, v = c.Next() {
		if err := fn(k, v); err != nil {
			return err
		}
	}
	return nil
}

func (b *Bucket) ForEachBucket(fn func(k []byte) error) error {
	if b.tx.db == nil {
		return errors.ErrTxClosed
	}
	c := b.Cursor()
	for k, _, flags := c.first(); k != nil; k, _, flags = c.next() {
		if flags&common.BucketLeafFlag != 0 {
			if err := fn(k); err != nil {
				return err
			}
		}
	}
	return nil
}

// Stats returns stats on a bucket.
func (b *Bucket) Stats() BucketStats {
	var s, subStats BucketStats
	pageSize := b.tx.db.pageSize
	s.BucketN += 1
	if b.RootPage() == 0 {
		s.InlineBucketN += 1
	}
	b.forEachPage(func(p *common.Page, depth int, pgstack []common.Pgid) {
		if p.IsLeafPage() {
			s.KeyN += int(p.Count())

			// used totals the used bytes for the page
			used := common.PageHeaderSize

			if p.Count() != 0 {
				// If page has any elements, add all element headers.
				used += common.LeafPageElementSize * uintptr(p.Count()-1)

				// Add all element key, value sizes.
				// The computation takes advantage of the fact that the position
				// of the last element's key/value equals to the total of the sizes
				// of all previous elements' keys and values.
				// It also includes the last element's header.
				lastElement := p.LeafPageElement(p.Count() - 1)
				used += uintptr(lastElement.Pos() + lastElement.Ksize() + lastElement.Vsize())
			}

			if b.RootPage() == 0 {
				// For inlined bucket just update the inline stats
				s.InlineBucketInuse += int(used)
			} else {
				// For non-inlined bucket update all the leaf stats
				s.LeafPageN++
				s.LeafInuse += int(used)
				s.LeafOverflowN += int(p.Overflow())

				// Collect stats from sub-buckets.
				// Do that by iterating over all element headers
				// looking for the ones with the bucketLeafFlag.
				for i := uint16(0); i < p.Count(); i++ {
					e := p.LeafPageElement(i)
					if (e.Flags() & common.BucketLeafFlag) != 0 {
						// For any bucket element, open the element value
						// and recursively call Stats on the contained bucket.
						subStats.Add(b.openBucket(e.Value()).Stats())
					}
				}
			}
		} else if p.IsBranchPage() {
			s.BranchPageN++

			used := common.PageHeaderSize
			if p.Count() != 0 {
				lastElement := p.BranchPageElement(p.Count() - 1)

				// Add all element headers.
				used += common.BranchPageElementSize * uintptr(p.Count()-1)

				// Add size of all keys and values.
				// Again, use the fact that last element's position equals to
				// the total of key, value sizes of all previous elements.
				used += uintptr(lastElement.Pos() + lastElement.Ksize())
			}

			s.BranchInuse += int(used)
			s.BranchOverflowN += int(p.Overflow())
		}

		// Keep track of maximum page depth.
		if depth+1 > s.Depth {
			s.Depth = depth + 1
		}
	})

	// Alloc stats can be computed from page counts and pageSize.
	s.BranchAlloc = (s.BranchPageN + s.BranchOverflowN) * pageSize
	s.LeafAlloc = (s.LeafPageN + s.LeafOverflowN) * pageSize

	// Add the max depth of sub-buckets to get total nested depth.
	s.Depth += subStats.Depth
	// Add the stats for all sub-buckets
	s.Add(subStats)
	return s
}

// forEachPage iterates over every page in a bucket, including inline pages.
func (b *Bucket) forEachPage(fn func(*common.Page, int, []common.Pgid)) {
	// If we have an inline page then just use that.
	if b.page != nil {
		fn(b.page, 0, []common.Pgid{b.RootPage()})
		return
	}

	// Otherwise traverse the page hierarchy.
	b.tx.forEachPage(b.RootPage(), fn)
}

// forEachPageNode iterates over every page (or node) in a bucket.
// This also includes inline pages.
func (b *Bucket) forEachPageNode(fn func(*common.Page, *node, int)) {
	// If we have an inline page or root node then just use that.
	if b.page != nil {
		fn(b.page, nil, 0)
		return
	}
	b._forEachPageNode(b.RootPage(), 0, fn)
}

func (b *Bucket) _forEachPageNode(pgId common.Pgid, depth int, fn func(*common.Page, *node, int)) {
	var p, n = b.pageNode(pgId)

	// Execute function.
	fn(p, n, depth)

	// Recursively loop over children.
	if p != nil {
		if p.IsBranchPage() {
			for i := 0; i < int(p.Count()); i++ {
				elem := p.BranchPageElement(uint16(i))
				b._forEachPageNode(elem.Pgid(), depth+1, fn)
			}
		}
	} else {
		if !n.isLeaf {
			for _, inode := range n.inodes {
				b._forEachPageNode(inode.Pgid(), depth+1, fn)
			}
		}
	}
}

// spill writes all the nodes for this bucket to dirty pages.
func (b *Bucket) spill() error {
	// Spill all child buckets first.
	for name, child := range b.buckets {
		// If the child bucket is small enough and it has no child buckets then
		// write it inline into the parent bucket's page. Otherwise spill it
		// like a normal bucket and make the parent value a pointer to the page.
		var value []byte
		if child.inlineable() {
			child.free()
			value = child.write()
		} else {
			if err := child.spill(); err != nil {
				return err
			}

			// Update the child bucket header in this bucket.
			value = make([]byte, unsafe.Sizeof(common.InBucket{}))
			var bucket = (*common.InBucket)(unsafe.Pointer(&value[0]))
			*bucket = *child.InBucket
		}

		// Skip writing the bucket if there are no materialized nodes.
		if child.rootNode == nil {
			continue
		}

		// Update parent node.
		var c = b.Cursor()
		k, _, flags := c.seek([]byte(name))
		if !bytes.Equal([]byte(name), k) {
			panic(fmt.Sprintf("misplaced bucket header: %x -> %x", []byte(name), k))
		}
		if flags&common.BucketLeafFlag == 0 {
			panic(fmt.Sprintf("unexpected bucket header flag: %x", flags))
		}
		c.node().put([]byte(name), []byte(name), value, 0, common.BucketLeafFlag)
	}

	// Ignore if there's not a materialized root node.
	if b.rootNode == nil {
		return nil
	}

	// Spill nodes.
	if err := b.rootNode.spill(); err != nil {
		return err
	}
	b.rootNode = b.rootNode.root()

	// Update the root node for this bucket.
	if b.rootNode.pgid >= b.tx.meta.Pgid() {
		panic(fmt.Sprintf("pgid (%d) above high water mark (%d)", b.rootNode.pgid, b.tx.meta.Pgid()))
	}
	b.SetRootPage(b.rootNode.pgid)

	return nil
}

// inlineable returns true if a bucket is small enough to be written inline
// and if it contains no subbuckets. Otherwise, returns false.
func (b *Bucket) inlineable() bool {
	var n = b.rootNode

	// Bucket must only contain a single leaf node.
	if n == nil || !n.isLeaf {
		return false
	}

	// Bucket is not inlineable if it contains subbuckets or if it goes beyond
	// our threshold for inline bucket size.
	var size = common.PageHeaderSize
	for _, inode := range n.inodes {
		size += common.LeafPageElementSize + uintptr(len(inode.Key())) + uintptr(len(inode.Value()))

		if inode.Flags()&common.BucketLeafFlag != 0 {
			return false
		} else if size > b.maxInlineBucketSize() {
			return false
		}
	}

	return true
}

// Returns the maximum total size of a bucket to make it a candidate for inlining.
func (b *Bucket) maxInlineBucketSize() uintptr {
	return uintptr(b.tx.db.pageSize / 4)
}

// write allocates and writes a bucket to a byte slice.
func (b *Bucket) write() []byte {
	// Allocate the appropriate size.
	var n = b.rootNode
	var value = make([]byte, common.BucketHeaderSize+n.size())

	// Write a bucket header.
	var bucket = (*common.InBucket)(unsafe.Pointer(&value[0]))
	*bucket = *b.InBucket

	// Convert byte slice to a fake page and write the root node.
	var p = (*common.Page)(unsafe.Pointer(&value[common.BucketHeaderSize]))
	n.write(p)

	return value
}

// rebalance attempts to balance all nodes.
func (b *Bucket) rebalance() {
	for _, n := range b.nodes {
		n.rebalance()
	}
	for _, child := range b.buckets {
		child.rebalance()
	}
}

// node creates a node from a page and associates it with a given parent.
func (b *Bucket) node(pgId common.Pgid, parent *node) *node {
	common.Assert(b.nodes != nil, "nodes map expected")

	// Retrieve node if it's already been created.
	if n := b.nodes[pgId]; n != nil {
		return n
	}

	// Otherwise create a node and cache it.
	n := &node{bucket: b, parent: parent}
	if parent == nil {
		b.rootNode = n
	} else {
		parent.children = append(parent.children, n)
	}

	// Use the inline page if this is an inline bucket.
	var p = b.page
	if p == nil {
		p = b.tx.page(pgId)
	} else {
		// if p isn't nil, then it's an inline bucket.
		// The pgId must be 0 in this case.
		common.Verify(func() {
			common.Assert(pgId == 0, "The page ID (%d) isn't 0 for an inline bucket", pgId)
		})
	}

	// Read the page into the node and cache it.
	n.read(p)
	b.nodes[pgId] = n

	// Update statistics.
	b.tx.stats.IncNodeCount(1)

	return n
}

// free recursively frees all pages in the bucket.
func (b *Bucket) free() {
	if b.RootPage() == 0 {
		return
	}

	var tx = b.tx
	b.forEachPageNode(func(p *common.Page, n *node, _ int) {
		if p != nil {
			tx.db.freelist.Free(tx.meta.Txid(), p)
		} else {
			n.free()
		}
	})
	b.SetRootPage(0)
}

// dereference removes all references to the old mmap.
func (b *Bucket) dereference() {
	if b.rootNode != nil {
		b.rootNode.root().dereference()
	}

	for _, child := range b.buckets {
		child.dereference()
	}
}

// pageNode returns the in-memory node, if it exists.
// Otherwise, returns the underlying page.
func (b *Bucket) pageNode(id common.Pgid) (*common.Page, *node) {
	// Inline buckets have a fake page embedded in their value so treat them
	// differently. We'll return the rootNode (if available) or the fake page.
	if b.RootPage() == 0 {
		if id != 0 {
			panic(fmt.Sprintf("inline bucket non-zero page access(2): %d != 0", id))
		}
		if b.rootNode != nil {
			return nil, b.rootNode
		}
		return b.page, nil
	}

	// Check the node cache for non-inline buckets.
	if b.nodes != nil {
		if n := b.nodes[id]; n != nil {
			return nil, n
		}
	}

	// Finally lookup the page from the transaction if no node is materialized.
	return b.tx.page(id), nil
}

// BucketStats records statistics about resources used by a bucket.
type BucketStats struct {
	// Page count statistics.
	BranchPageN     int // number of logical branch pages
	BranchOverflowN int // number of physical branch overflow pages
	LeafPageN       int // number of logical leaf pages
	LeafOverflowN   int // number of physical leaf overflow pages

	// Tree statistics.
	KeyN  int // number of keys/value pairs
	Depth int // number of levels in B+tree

	// Page size utilization.
	BranchAlloc int // bytes allocated for physical branch pages
	BranchInuse int // bytes actually used for branch data
	LeafAlloc   int // bytes allocated for physical leaf pages
	LeafInuse   int // bytes actually used for leaf data

	// Bucket statistics
	BucketN           int // total number of buckets including the top bucket
	InlineBucketN     int // total number on inlined buckets
	InlineBucketInuse int // bytes used for inlined buckets (also accounted for in LeafInuse)
}

func (s *BucketStats) Add(other BucketStats) {
	s.BranchPageN += other.BranchPageN
	s.BranchOverflowN += other.BranchOverflowN
	s.LeafPageN += other.LeafPageN
	s.LeafOverflowN += other.LeafOverflowN
	s.KeyN += other.KeyN
	if s.Depth < other.Depth {
		s.Depth = other.Depth
	}
	s.BranchAlloc += other.BranchAlloc
	s.BranchInuse += other.BranchInuse
	s.LeafAlloc += other.LeafAlloc
	s.LeafInuse += other.LeafInuse

	s.BucketN += other.BucketN
	s.InlineBucketN += other.InlineBucketN
	s.InlineBucketInuse += other.InlineBucketInuse
}

// cloneBytes returns a copy of a given slice.
func cloneBytes(v []byte) []byte {
	var clone = make([]byte, len(v))
	copy(clone, v)
	return clone
}

type BucketStructure struct {
	Name     string            `json:"name"`              // name of the bucket
	KeyN     int               `json:"keyN"`              // number of key/value pairs
	Children []BucketStructure `json:"buckets,omitempty"` // child buckets
}
```

## File: `bucket_test.go`
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
	db := btesting.MustCreateDB(t)

	if err := db.Update(func(tx *bolt.Tx) error {
		widgets, err := tx.CreateBucket([]byte("widgets"))
		if err != nil {
			t.Fatal(err)
		}

		foo, err := widgets.CreateBucket([]byte("foo"))
		if err != nil {
			t.Fatal(err)
		}

		bar, err := foo.CreateBucket([]byte("bar"))
		if err != nil {
			t.Fatal(err)
		}
		if err := bar.Put([]byte("baz"), []byte("bat")); err != nil {
			t.Fatal(err)
		}
		if err := tx.Bucket([]byte("widgets")).DeleteBucket([]byte("foo")); err != nil {
			t.Fatal(err)
		}
		return nil
	}); err != nil {
		t.Fatal(err)
	}
}

// Ensure that deleting a bucket causes nested buckets to be deleted after they have been committed.
func TestBucket_DeleteBucket_Nested2(t *testing.T) {
	db := btesting.MustCreateDB(t)

	if err := db.Update(func(tx *bolt.Tx) error {
		widgets, err := tx.CreateBucket([]byte("widgets"))
		if err != nil {
			t.Fatal(err)
		}

		foo, err := widgets.CreateBucket([]byte("foo"))
		if err != nil {
			t.Fatal(err)
		}

		bar, err := foo.CreateBucket([]byte("bar"))
		if err != nil {
			t.Fatal(err)
		}

		if err := bar.Put([]byte("baz"), []byte("bat")); err != nil {
			t.Fatal(err)
		}
		return nil
	}); err != nil {
		t.Fatal(err)
	}

	if err := db.Update(func(tx *bolt.Tx) error {
		widgets := tx.Bucket([]byte("widgets"))
		if widgets == nil {
			t.Fatal("expected widgets bucket")
		}

		foo := widgets.Bucket([]byte("foo"))
		if foo == nil {
			t.Fatal("expected foo bucket")
		}

		bar := foo.Bucket([]byte("bar"))
		if bar == nil {
			t.Fatal("expected bar bucket")
		}

		if v := bar.Get([]byte("baz")); !bytes.Equal(v, []byte("bat")) {
			t.Fatalf("unexpected value: %v", v)
		}
		if err := tx.DeleteBucket([]byte("widgets")); err != nil {
			t.Fatal(err)
		}
		return nil
	}); err != nil {
		t.Fatal(err)
	}

	if err := db.View(func(tx *bolt.Tx) error {
		if tx.Bucket([]byte("widgets")) != nil {
			t.Fatal("expected bucket to be deleted")
		}
		return nil
	}); err != nil {
		t.Fatal(err)
	}
}

// Ensure that deleting a child bucket with multiple pages causes all pages to get collected.
// NOTE: Consistency check in bolt_test.DB.Close() will panic if pages not freed properly.
func TestBucket_DeleteBucket_Large(t *testing.T) {
	db := btesting.MustCreateDB(t)

	if err := db.Update(func(tx *bolt.Tx) error {
		widgets, err := tx.CreateBucket([]byte("widgets"))
		if err != nil {
			t.Fatal(err)
		}

		foo, err := widgets.CreateBucket([]byte("foo"))
		if err != nil {
			t.Fatal(err)
		}

		for i := 0; i < 1000; i++ {
			if err := foo.Put([]byte(fmt.Sprintf("%d", i)), []byte(fmt.Sprintf("%0100d", i))); err != nil {
				t.Fatal(err)
			}
		}
		return nil
	}); err != nil {
		t.Fatal(err)
	}

	if err := db.Update(func(tx *bolt.Tx) error {
		if err := tx.DeleteBucket([]byte("widgets")); err != nil {
			t.Fatal(err)
		}
		return nil
	}); err != nil {
		t.Fatal(err)
	}
}

// Ensure that a simple value retrieved via Bucket() returns a nil.
func TestBucket_Bucket_IncompatibleValue(t *testing.T) {
	db := btesting.MustCreateDB(t)

	if err := db.Update(func(tx *bolt.Tx) error {
		widgets, err := tx.CreateBucket([]byte("widgets"))
		if err != nil {
			t.Fatal(err)
		}

		if err := widgets.Put([]byte("foo"), []byte("bar")); err != nil {
			t.Fatal(err)
		}
		if b := tx.Bucket([]byte("widgets")).Bucket([]byte("foo")); b != nil {
			t.Fatal("expected nil bucket")
		}
		return nil
	}); err != nil {
		t.Fatal(err)
	}
}

// Ensure that creating a bucket on an existing non-bucket key returns an error.
func TestBucket_CreateBucket_IncompatibleValue(t *testing.T) {
	db := btesting.MustCreateDB(t)
	if err := db.Update(func(tx *bolt.Tx) error {
		widgets, err := tx.CreateBucket([]byte("widgets"))
		if err != nil {
			t.Fatal(err)
		}

		if err := widgets.Put([]byte("foo"), []byte("bar")); err != nil {
			t.Fatal(err)
		}
		if _, err := widgets.CreateBucket([]byte("foo")); err != berrors.ErrIncompatibleValue {
			t.Fatalf("unexpected error: %s", err)
		}
		return nil
	}); err != nil {
		t.Fatal(err)
	}
}

// Ensure that deleting a bucket on an existing non-bucket key returns an error.
func TestBucket_DeleteBucket_IncompatibleValue(t *testing.T) {
	db := btesting.MustCreateDB(t)

	if err := db.Update(func(tx *bolt.Tx) error {
		widgets, err := tx.CreateBucket([]byte("widgets"))
		if err != nil {
			t.Fatal(err)
		}
		if err := widgets.Put([]byte("foo"), []byte("bar")); err != nil {
			t.Fatal(err)
		}
		if err := tx.Bucket([]byte("widgets")).DeleteBucket([]byte("foo")); err != berrors.ErrIncompatibleValue {
			t.Fatalf("unexpected error: %s", err)
		}
		return nil
	}); err != nil {
		t.Fatal(err)
	}
}

// Ensure bucket can set and update its sequence number.
func TestBucket_Sequence(t *testing.T) {
	db := btesting.MustCreateDB(t)

	if err := db.Update(func(tx *bolt.Tx) error {
		bkt, err := tx.CreateBucket([]byte("0"))
		if err != nil {
			t.Fatal(err)
		}

		// Retrieve sequence.
		if v := bkt.Sequence(); v != 0 {
			t.Fatalf("unexpected sequence: %d", v)
		}

		// Update sequence.
		if err := bkt.SetSequence(1000); err != nil {
			t.Fatal(err)
		}

		// Read sequence again.
		if v := bkt.Sequence(); v != 1000 {
			t.Fatalf("unexpected sequence: %d", v)
		}

		return nil
	}); err != nil {
		t.Fatal(err)
	}

	// Verify sequence in separate transaction.
	if err := db.View(func(tx *bolt.Tx) error {
		if v := tx.Bucket([]byte("0")).Sequence(); v != 1000 {
			t.Fatalf("unexpected sequence: %d", v)
		}
		return nil
	}); err != nil {
		t.Fatal(err)
	}
}

// Ensure that a bucket can return an autoincrementing sequence.
func TestBucket_NextSequence(t *testing.T) {
	db := btesting.MustCreateDB(t)

	if err := db.Update(func(tx *bolt.Tx) error {
		widgets, err := tx.CreateBucket([]byte("widgets"))
		if err != nil {
			t.Fatal(err)
		}
		woojits, err := tx.CreateBucket([]byte("woojits"))
		if err != nil {
			t.Fatal(err)
		}

		// Make sure sequence increments.
		if seq, err := widgets.NextSequence(); err != nil {
			t.Fatal(err)
		} else if seq != 1 {
			t.Fatalf("unexpecte sequence: %d", seq)
		}

		if seq, err := widgets.NextSequence(); err != nil {
			t.Fatal(err)
		} else if seq != 2 {
			t.Fatalf("unexpected sequence: %d", seq)
		}

		// Buckets should be separate.
		if seq, err := woojits.NextSequence(); err != nil {
			t.Fatal(err)
		} else if seq != 1 {
			t.Fatalf("unexpected sequence: %d", 1)
		}

		return nil
	}); err != nil {
		t.Fatal(err)
	}
}

// Ensure that a bucket will persist an autoincrementing sequence even if its
// the only thing updated on the bucket.
// https://github.com/boltdb/bolt/issues/296
func TestBucket_NextSequence_Persist(t *testing.T) {
	db := btesting.MustCreateDB(t)

	if err := db.Update(func(tx *bolt.Tx) error {
		if _, err := tx.CreateBucket([]byte("widgets")); err != nil {
			t.Fatal(err)
		}
		return nil
	}); err != nil {
		t.Fatal(err)
	}

	if err := db.Update(func(tx *bolt.Tx) error {
		if _, err := tx.Bucket([]byte("widgets")).NextSequence(); err != nil {
			t.Fatal(err)
		}
		return nil
	}); err != nil {
		t.Fatal(err)
	}

	if err := db.Update(func(tx *bolt.Tx) error {
		seq, err := tx.Bucket([]byte("widgets")).NextSequence()
		if err != nil {
			t.Fatalf("unexpected error: %s", err)
		} else if seq != 2 {
			t.Fatalf("unexpected sequence: %d", seq)
		}
		return nil
	}); err != nil {
		t.Fatal(err)
	}
}

// Ensure that retrieving the next sequence on a read-only bucket returns an error.
func TestBucket_NextSequence_ReadOnly(t *testing.T) {
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
		_, err := tx.Bucket([]byte("widgets")).NextSequence()
		if err != berrors.ErrTxNotWritable {
			t.Fatalf("unexpected error: %s", err)
		}
		return nil
	}); err != nil {
		t.Fatal(err)
	}
}

// Ensure that retrieving the next sequence for a bucket on a closed database return an error.
func TestBucket_NextSequence_Closed(t *testing.T) {
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
	if _, err := b.NextSequence(); err != berrors.ErrTxClosed {
		t.Fatal(err)
	}
}

// Ensure a user can loop over all key/value pairs in a bucket.
func TestBucket_ForEach(t *testing.T) {
	db := btesting.MustCreateDB(t)

	type kv struct {
		k []byte
		v []byte
	}

	expectedItems := []kv{
		{k: []byte("bar"), v: []byte("0002")},
		{k: []byte("baz"), v: []byte("0001")},
		{k: []byte("csubbucket"), v: nil},
		{k: []byte("foo"), v: []byte("0000")},
	}

	verifyReads := func(b *bolt.Bucket) {
		var items []kv
		err := b.ForEach(func(k, v []byte) error {
			items = append(items, kv{k: k, v: v})
			return nil
		})
		assert.NoErrorf(t, err, "b.ForEach failed")
		assert.Equal(t, expectedItems, items, "what we iterated (ForEach) is not what we put")
	}

	err := db.Update(func(tx *bolt.Tx) error {
		b, err := tx.CreateBucket([]byte("widgets"))
		require.NoError(t, err, "bucket creation failed")

		require.NoErrorf(t, b.Put([]byte("foo"), []byte("0000")), "put 'foo' failed")
		require.NoErrorf(t, b.Put([]byte("baz"), []byte("0001")), "put 'baz' failed")
		require.NoErrorf(t, b.Put([]byte("bar"), []byte("0002")), "put 'bar' failed")
		_, err = b.CreateBucket([]byte("csubbucket"))
		require.NoErrorf(t, err, "creation of subbucket failed")

		verifyReads(b)

		return nil
	})
	require.NoErrorf(t, err, "db.Update failed")
	err = db.View(func(tx *bolt.Tx) error {
		b := tx.Bucket([]byte("widgets"))
		require.NotNil(t, b, "bucket opening failed")
		verifyReads(b)
		return nil
	})
	assert.NoErrorf(t, err, "db.View failed")
}

func TestBucket_ForEachBucket(t *testing.T) {
	db := btesting.MustCreateDB(t)

	expectedItems := [][]byte{
		[]byte("csubbucket"),
		[]byte("zsubbucket"),
	}

	verifyReads := func(b *bolt.Bucket) {
		var items [][]byte
		err := b.ForEachBucket(func(k []byte) error {
			items = append(items, k)
			return nil
		})
		assert.NoErrorf(t, err, "b.ForEach failed")
		assert.Equal(t, expectedItems, items, "what we iterated (ForEach) is not what we put")
	}

	err := db.Update(func(tx *bolt.Tx) error {
		b, err := tx.CreateBucket([]byte("widgets"))
		require.NoError(t, err, "bucket creation failed")

		require.NoErrorf(t, b.Put([]byte("foo"), []byte("0000")), "put 'foo' failed")
		_, err = b.CreateBucket([]byte("zsubbucket"))
		require.NoErrorf(t, err, "creation of subbucket failed")
		require.NoErrorf(t, b.Put([]byte("baz"), []byte("0001")), "put 'baz' failed")
		require.NoErrorf(t, b.Put([]byte("bar"), []byte("0002")), "put 'bar' failed")
		_, err = b.CreateBucket([]byte("csubbucket"))
		require.NoErrorf(t, err, "creation of subbucket failed")

		verifyReads(b)

		return nil
	})
	assert.NoErrorf(t, err, "db.Update failed")
	err = db.View(func(tx *bolt.Tx) error {
		b := tx.Bucket([]byte("widgets"))
		require.NotNil(t, b, "bucket opening failed")
		verifyReads(b)
		return nil
	})
	assert.NoErrorf(t, err, "db.View failed")
}

func TestBucket_ForEachBucket_NoBuckets(t *testing.T) {
	db := btesting.MustCreateDB(t)

	verifyReads := func(b *bolt.Bucket) {
		var items [][]byte
		err := b.ForEachBucket(func(k []byte) error {
			items = append(items, k)
			return nil
		})
		assert.NoErrorf(t, err, "b.ForEach failed")
		assert.Emptyf(t, items, "what we iterated (ForEach) is not what we put")
	}

	err := db.Update(func(tx *bolt.Tx) error {
		b, err := tx.CreateBucket([]byte("widgets"))
		require.NoError(t, err, "bucket creation failed")

		require.NoErrorf(t, b.Put([]byte("foo"), []byte("0000")), "put 'foo' failed")
		require.NoErrorf(t, err, "creation of subbucket failed")
		require.NoErrorf(t, b.Put([]byte("baz"), []byte("0001")), "put 'baz' failed")
		require.NoErrorf(t, err, "creation of subbucket failed")

		verifyReads(b)

		return nil
	})
	require.NoErrorf(t, err, "db.Update failed")

	err = db.View(func(tx *bolt.Tx) error {
		b := tx.Bucket([]byte("widgets"))
		require.NotNil(t, b, "bucket opening failed")
		verifyReads(b)
		return nil
	})
	assert.NoErrorf(t, err, "db.View failed")
}

// Ensure a database can stop iteration early.
func TestBucket_ForEach_ShortCircuit(t *testing.T) {
	db := btesting.MustCreateDB(t)
	if err := db.Update(func(tx *bolt.Tx) error {
		b, err := tx.CreateBucket([]byte("widgets"))
		if err != nil {
			t.Fatal(err)
		}
		if err := b.Put([]byte("bar"), []byte("0000")); err != nil {
			t.Fatal(err)
		}
		if err := b.Put([]byte("baz"), []byte("0000")); err != nil {
			t.Fatal(err)
		}
		if err := b.Put([]byte("foo"), []byte("0000")); err != nil {
			t.Fatal(err)
		}

		var index int
		if err := tx.Bucket([]byte("widgets")).ForEach(func(k, v []byte) error {
			index++
			if bytes.Equal(k, []byte("baz")) {
				return errors.New("marker")
			}
			return nil
		}); err == nil || err.Error() != "marker" {
			t.Fatalf("unexpected error: %s", err)
		}
		if index != 2 {
			t.Fatalf("unexpected index: %d", index)
		}

		return nil
	}); err != nil {
		t.Fatal(err)
	}
}

// Ensure that looping over a bucket on a closed database returns an error.
func TestBucket_ForEach_Closed(t *testing.T) {
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

	if err := b.ForEach(func(k, v []byte) error { return nil }); err != berrors.ErrTxClosed {
		t.Fatalf("unexpected error: %s", err)
	}
}

// Ensure that an error is returned when inserting with an empty key.
func TestBucket_Put_EmptyKey(t *testing.T) {
	db := btesting.MustCreateDB(t)

	if err := db.Update(func(tx *bolt.Tx) error {
		b, err := tx.CreateBucket([]byte("widgets"))
		if err != nil {
			t.Fatal(err)
		}
		if err := b.Put([]byte(""), []byte("bar")); err != berrors.ErrKeyRequired {
			t.Fatalf("unexpected error: %s", err)
		}
		if err := b.Put(nil, []byte("bar")); err != berrors.ErrKeyRequired {
			t.Fatalf("unexpected error: %s", err)
		}
		return nil
	}); err != nil {
		t.Fatal(err)
	}
}

// Ensure that an error is returned when inserting with a key that's too large.
func TestBucket_Put_KeyTooLarge(t *testing.T) {
	db := btesting.MustCreateDB(t)
	if err := db.Update(func(tx *bolt.Tx) error {
		b, err := tx.CreateBucket([]byte("widgets"))
		if err != nil {
			t.Fatal(err)
		}
		if err := b.Put(make([]byte, 32769), []byte("bar")); err != berrors.ErrKeyTooLarge {
			t.Fatalf("unexpected error: %s", err)
		}
		return nil
	}); err != nil {
		t.Fatal(err)
	}
}

// Ensure that an error is returned when inserting a value that's too large.
func TestBucket_Put_ValueTooLarge(t *testing.T) {
	// Skip this test on DroneCI because the machine is resource constrained.
	if os.Getenv("DRONE") == "true" {
		t.Skip("not enough RAM for test")
	}

	db := btesting.MustCreateDB(t)

	if err := db.Update(func(tx *bolt.Tx) error {
		b, err := tx.CreateBucket([]byte("widgets"))
		if err != nil {
			t.Fatal(err)
		}
		if err := b.Put([]byte("foo"), make([]byte, bolt.MaxValueSize+1)); err != berrors.ErrValueTooLarge {
			t.Fatalf("unexpected error: %s", err)
		}
		return nil
	}); err != nil {
		t.Fatal(err)
	}
}

// Ensure a bucket can calculate stats.
func TestBucket_Stats(t *testing.T) {
	if testing.Short() {
		t.Skip("skipping test in short mode")
	}

	db := btesting.MustCreateDB(t)

	// Add bucket with fewer keys but one big value.
	bigKey := []byte("really-big-value")
	for i := 0; i < 500; i++ {
		if err := db.Update(func(tx *bolt.Tx) error {
			b, err := tx.CreateBucketIfNotExists([]byte("woojits"))
			if err != nil {
				t.Fatal(err)
			}

			if err := b.Put([]byte(fmt.Sprintf("%03d", i)), []byte(strconv.Itoa(i))); err != nil {
				t.Fatal(err)
			}
			return nil
		}); err != nil {
			t.Fatal(err)
		}
	}
	longKeyLength := 10*db.Info().PageSize + 17
	if err := db.Update(func(tx *bolt.Tx) error {
		if err := tx.Bucket([]byte("woojits")).Put(bigKey, []byte(strings.Repeat("*", longKeyLength))); err != nil {
			t.Fatal(err)
		}
		return nil
	}); err != nil {
		t.Fatal(err)
	}

	db.MustCheck()

	pageSize2stats := map[int]bolt.BucketStats{
		4096: {
			BranchPageN:     1,
			BranchOverflowN: 0,
			LeafPageN:       7,
			LeafOverflowN:   10,
			KeyN:            501,
			Depth:           2,
			BranchAlloc:     4096,
			BranchInuse:     149,
			LeafAlloc:       69632,
			LeafInuse: 0 +
				7*16 + // leaf page header (x LeafPageN)
				501*16 + // leaf elements
				500*3 + len(bigKey) + // leaf keys
				1*10 + 2*90 + 3*400 + longKeyLength, // leaf values: 10 * 1digit, 90*2digits, ...
			BucketN:           1,
			InlineBucketN:     0,
			InlineBucketInuse: 0},
		16384: {
			BranchPageN:     1,
			BranchOverflowN: 0,
			LeafPageN:       3,
			LeafOverflowN:   10,
			KeyN:            501,
			Depth:           2,
			BranchAlloc:     16384,
			BranchInuse:     73,
			LeafAlloc:       212992,
			LeafInuse: 0 +
				3*16 + // leaf page header (x LeafPageN)
				501*16 + // leaf elements
				500*3 + len(bigKey) + // leaf keys
				1*10 + 2*90 + 3*400 + longKeyLength, // leaf values: 10 * 1digit, 90*2digits, ...
			BucketN:           1,
			InlineBucketN:     0,
			InlineBucketInuse: 0},
		65536: {
			BranchPageN:     1,
			BranchOverflowN: 0,
			LeafPageN:       2,
			LeafOverflowN:   10,
			KeyN:            501,
			Depth:           2,
			BranchAlloc:     65536,
			BranchInuse:     54,
			LeafAlloc:       786432,
			LeafInuse: 0 +
				2*16 + // leaf page header (x LeafPageN)
				501*16 + // leaf elements
				500*3 + len(bigKey) + // leaf keys
				1*10 + 2*90 + 3*400 + longKeyLength, // leaf values: 10 * 1digit, 90*2digits, ...
			BucketN:           1,
			InlineBucketN:     0,
			InlineBucketInuse: 0},
	}

	if err := db.View(func(tx *bolt.Tx) error {
		stats := tx.Bucket([]byte("woojits")).Stats()
		t.Logf("Stats: %#v", stats)
		if expected, ok := pageSize2stats[db.Info().PageSize]; ok {
			assert.EqualValues(t, expected, stats, "stats differs from expectations")
		} else {
			t.Skipf("No expectations for page size: %d", db.Info().PageSize)
		}
		return nil
	}); err != nil {
		t.Fatal(err)
	}
}

// Ensure a bucket with random insertion utilizes fill percentage correctly.
func TestBucket_Stats_RandomFill(t *testing.T) {
	if testing.Short() {
		t.Skip("skipping test in short mode.")
	} else if os.Getpagesize() != 4096 {
		t.Skip("invalid page size for test")
	}

	db := btesting.MustCreateDB(t)

	// Add a set of values in random order. It will be the same random
	// order so we can maintain consistency between test runs.
	var count int
	rand := rand.New(rand.NewSource(42))
	for _, i := range rand.Perm(1000) {
		if err := db.Update(func(tx *bolt.Tx) error {
			b, err := tx.CreateBucketIfNotExists([]byte("woojits"))
			if err != nil {
				t.Fatal(err)
			}
			b.FillPercent = 0.9
			for _, j := range rand.Perm(100) {
				index := (j * 10000) + i
				if err := b.Put([]byte(fmt.Sprintf("%d000000000000000", index)), []byte("0000000000")); err != nil {
					t.Fatal(err)
				}
				count++
			}
			return nil
		}); err != nil {
			t.Fatal(err)
		}
	}

	db.MustCheck()

	if err := db.View(func(tx *bolt.Tx) error {
		stats := tx.Bucket([]byte("woojits")).Stats()
		if stats.KeyN != 100000 {
			t.Fatalf("unexpected KeyN: %d", stats.KeyN)
		}

		if stats.BranchPageN != 98 {
			t.Fatalf("unexpected BranchPageN: %d", stats.BranchPageN)
		} else if stats.BranchOverflowN != 0 {
			t.Fatalf("unexpected BranchOverflowN: %d", stats.BranchOverflowN)
		} else if stats.BranchInuse != 130984 {
			t.Fatalf("unexpected BranchInuse: %d", stats.BranchInuse)
		} else if stats.BranchAlloc != 401408 {
			t.Fatalf("unexpected BranchAlloc: %d", stats.BranchAlloc)
		}

		if stats.LeafPageN != 3412 {
			t.Fatalf("unexpected LeafPageN: %d", stats.LeafPageN)
		} else if stats.LeafOverflowN != 0 {
			t.Fatalf("unexpected LeafOverflowN: %d", stats.LeafOverflowN)
		} else if stats.LeafInuse != 4742482 {
			t.Fatalf("unexpected LeafInuse: %d", stats.LeafInuse)
		} else if stats.LeafAlloc != 13975552 {
			t.Fatalf("unexpected LeafAlloc: %d", stats.LeafAlloc)
		}
		return nil
	}); err != nil {
		t.Fatal(err)
	}
}

// Ensure a bucket can calculate stats.
func TestBucket_Stats_Small(t *testing.T) {
	db := btesting.MustCreateDB(t)

	if err := db.Update(func(tx *bolt.Tx) error {
		// Add a bucket that fits on a single root leaf.
		b, err := tx.CreateBucket([]byte("whozawhats"))
		if err != nil {
			t.Fatal(err)
		}
		if err := b.Put([]byte("foo"), []byte("bar")); err != nil {
			t.Fatal(err)
		}

		return nil
	}); err != nil {
		t.Fatal(err)
	}

	db.MustCheck()

	if err := db.View(func(tx *bolt.Tx) error {
		b := tx.Bucket([]byte("whozawhats"))
		stats := b.Stats()
		if stats.BranchPageN != 0 {
			t.Fatalf("unexpected BranchPageN: %d", stats.BranchPageN)
		} else if stats.BranchOverflowN != 0 {
			t.Fatalf("unexpected BranchOverflowN: %d", stats.BranchOverflowN)
		} else if stats.LeafPageN != 0 {
			t.Fatalf("unexpected LeafPageN: %d", stats.LeafPageN)
		} else if stats.LeafOverflowN != 0 {
			t.Fatalf("unexpected LeafOverflowN: %d", stats.LeafOverflowN)
		} else if stats.KeyN != 1 {
			t.Fatalf("unexpected KeyN: %d", stats.KeyN)
		} else if stats.Depth != 1 {
			t.Fatalf("unexpected Depth: %d", stats.Depth)
		} else if stats.BranchInuse != 0 {
			t.Fatalf("unexpected BranchInuse: %d", stats.BranchInuse)
		} else if stats.LeafInuse != 0 {
			t.Fatalf("unexpected LeafInuse: %d", stats.LeafInuse)
		}

		if db.Info().PageSize == 4096 {
			if stats.BranchAlloc != 0 {
				t.Fatalf("unexpected BranchAlloc: %d", stats.BranchAlloc)
			} else if stats.LeafAlloc != 0 {
				t.Fatalf("unexpected LeafAlloc: %d", stats.LeafAlloc)
			}
		}

		if stats.BucketN != 1 {
			t.Fatalf("unexpected BucketN: %d", stats.BucketN)
		} else if stats.InlineBucketN != 1 {
			t.Fatalf("unexpected InlineBucketN: %d", stats.InlineBucketN)
		} else if stats.InlineBucketInuse != 16+16+6 {
			t.Fatalf("unexpected InlineBucketInuse: %d", stats.InlineBucketInuse)
		}

		return nil
	}); err != nil {
		t.Fatal(err)
	}
}

func TestBucket_Stats_EmptyBucket(t *testing.T) {
	db := btesting.MustCreateDB(t)

	if err := db.Update(func(tx *bolt.Tx) error {
		// Add a bucket that fits on a single root leaf.
		if _, err := tx.CreateBucket([]byte("whozawhats")); err != nil {
			t.Fatal(err)
		}
		return nil
	}); err != nil {
		t.Fatal(err)
	}

	db.MustCheck()

	if err := db.View(func(tx *bolt.Tx) error {
		b := tx.Bucket([]byte("whozawhats"))
		stats := b.Stats()
		if stats.BranchPageN != 0 {
			t.Fatalf("unexpected BranchPageN: %d", stats.BranchPageN)
		} else if stats.BranchOverflowN != 0 {
			t.Fatalf("unexpected BranchOverflowN: %d", stats.BranchOverflowN)
		} else if stats.LeafPageN != 0 {
			t.Fatalf("unexpected LeafPageN: %d", stats.LeafPageN)
		} else if stats.LeafOverflowN != 0 {
			t.Fatalf("unexpected LeafOverflowN: %d", stats.LeafOverflowN)
		} else if stats.KeyN != 0 {
			t.Fatalf("unexpected KeyN: %d", stats.KeyN)
		} else if stats.Depth != 1 {
			t.Fatalf("unexpected Depth: %d", stats.Depth)
		} else if stats.BranchInuse != 0 {
			t.Fatalf("unexpected BranchInuse: %d", stats.BranchInuse)
		} else if stats.LeafInuse != 0 {
			t.Fatalf("unexpected LeafInuse: %d", stats.LeafInuse)
		}

		if db.Info().PageSize == 4096 {
			if stats.BranchAlloc != 0 {
				t.Fatalf("unexpected BranchAlloc: %d", stats.BranchAlloc)
			} else if stats.LeafAlloc != 0 {
				t.Fatalf("unexpected LeafAlloc: %d", stats.LeafAlloc)
			}
		}

		if stats.BucketN != 1 {
			t.Fatalf("unexpected BucketN: %d", stats.BucketN)
		} else if stats.InlineBucketN != 1 {
			t.Fatalf("unexpected InlineBucketN: %d", stats.InlineBucketN)
		} else if stats.InlineBucketInuse != 16 {
			t.Fatalf("unexpected InlineBucketInuse: %d", stats.InlineBucketInuse)
		}

		return nil
	}); err != nil {
		t.Fatal(err)
	}
}

// Ensure a bucket can calculate stats.
func TestBucket_Stats_Nested(t *testing.T) {
	db := btesting.MustCreateDB(t)

	if err := db.Update(func(tx *bolt.Tx) error {
		b, err := tx.CreateBucket([]byte("foo"))
		if err != nil {
			t.Fatal(err)
		}
		for i := 0; i < 100; i++ {
			if err := b.Put([]byte(fmt.Sprintf("%02d", i)), []byte(fmt.Sprintf("%02d", i))); err != nil {
				t.Fatal(err)
			}
		}

		bar, err := b.CreateBucket([]byte("bar"))
		if err != nil {
			t.Fatal(err)
		}
		for i := 0; i < 10; i++ {
			if err := bar.Put([]byte(strconv.Itoa(i)), []byte(strconv.Itoa(i))); err != nil {
				t.Fatal(err)
			}
		}

		baz, err := bar.CreateBucket([]byte("baz"))
		if err != nil {
			t.Fatal(err)
		}
		for i := 0; i < 10; i++ {
			if err := baz.Put([]byte(strconv.Itoa(i)), []byte(strconv.Itoa(i))); err != nil {
				t.Fatal(err)
			}
		}

		return nil
	}); err != nil {
		t.Fatal(err)
	}

	db.MustCheck()

	if err := db.View(func(tx *bolt.Tx) error {
		b := tx.Bucket([]byte("foo"))
		stats := b.Stats()
		if stats.BranchPageN != 0 {
			t.Fatalf("unexpected BranchPageN: %d", stats.BranchPageN)
		} else if stats.BranchOverflowN != 0 {
			t.Fatalf("unexpected BranchOverflowN: %d", stats.BranchOverflowN)
		} else if stats.LeafPageN != 2 {
			t.Fatalf("unexpected LeafPageN: %d", stats.LeafPageN)
		} else if stats.LeafOverflowN != 0 {
			t.Fatalf("unexpected LeafOverflowN: %d", stats.LeafOverflowN)
		} else if stats.KeyN != 122 {
			t.Fatalf("unexpected KeyN: %d", stats.KeyN)
		} else if stats.Depth != 3 {
			t.Fatalf("unexpected Depth: %d", stats.Depth)
		} else if stats.BranchInuse != 0 {
			t.Fatalf("unexpected BranchInuse: %d", stats.BranchInuse)
		}

		foo := 16            // foo (pghdr)
		foo += 101 * 16      // foo leaf elements
		foo += 100*2 + 100*2 // foo leaf key/values
		foo += 3 + 16        // foo -> bar key/value

		bar := 16      // bar (pghdr)
		bar += 11 * 16 // bar leaf elements
		bar += 10 + 10 // bar leaf key/values
		bar += 3 + 16  // bar -> baz key/value

		baz := 16      // baz (inline) (pghdr)
		baz += 10 * 16 // baz leaf elements
		baz += 10 + 10 // baz leaf key/values

		if stats.LeafInuse != foo+bar+baz {
			t.Fatalf("unexpected LeafInuse: %d", stats.LeafInuse)
		}

		if db.Info().PageSize == 4096 {
			if stats.BranchAlloc != 0 {
				t.Fatalf("unexpected BranchAlloc: %d", stats.BranchAlloc)
			} else if stats.LeafAlloc != 8192 {
				t.Fatalf("unexpected LeafAlloc: %d", stats.LeafAlloc)
			}
		}

		if stats.BucketN != 3 {
			t.Fatalf("unexpected BucketN: %d", stats.BucketN)
		} else if stats.InlineBucketN != 1 {
			t.Fatalf("unexpected InlineBucketN: %d", stats.InlineBucketN)
		} else if stats.InlineBucketInuse != baz {
			t.Fatalf("unexpected InlineBucketInuse: %d", stats.InlineBucketInuse)
		}

		return nil
	}); err != nil {
		t.Fatal(err)
	}
}

func TestBucket_Inspect(t *testing.T) {
	db := btesting.MustCreateDB(t)

	expectedStructure := bolt.BucketStructure{
		Name: "root",
		KeyN: 0,
		Children: []bolt.BucketStructure{
			{
				Name: "b1",
				KeyN: 3,
				Children: []bolt.BucketStructure{
					{
						Name: "b1_1",
						KeyN: 6,
					},
					{
						Name: "b1_2",
						KeyN: 7,
					},
					{
						Name: "b1_3",
						KeyN: 8,
					},
				},
			},
			{
				Name: "b2",
				KeyN: 4,
				Children: []bolt.BucketStructure{
					{
						Name: "b2_1",
						KeyN: 10,
					},
					{
						Name: "b2_2",
						KeyN: 12,
						Children: []bolt.BucketStructure{
							{
								Name: "b2_2_1",
								KeyN: 2,
							},
							{
								Name: "b2_2_2",
								KeyN: 3,
							},
						},
					},
					{
						Name: "b2_3",
						KeyN: 11,
					},
				},
			},
		},
	}

	type bucketItem struct {
		b  *bolt.Bucket
		bs bolt.BucketStructure
	}

	t.Log("Populating the database")
	err := db.Update(func(tx *bolt.Tx) error {
		queue := []bucketItem{
			{
				b:  nil,
				bs: expectedStructure,
			},
		}

		for len(queue) > 0 {
			item := queue[0]
			queue = queue[1:]

			if item.b != nil {
				for i := 0; i < item.bs.KeyN; i++ {
					err := item.b.Put([]byte(fmt.Sprintf("%02d", i)), []byte(fmt.Sprintf("%02d", i)))
					require.NoError(t, err)
				}

				for _, child := range item.bs.Children {
					childBucket, err := item.b.CreateBucket([]byte(child.Name))
					require.NoError(t, err)
					queue = append(queue, bucketItem{b: childBucket, bs: child})
				}
			} else {
				for _, child := range item.bs.Children {
					childBucket, err := tx.CreateBucket([]byte(child.Name))
					require.NoError(t, err)
					queue = append(queue, bucketItem{b: childBucket, bs: child})
				}
			}
		}
		return nil
	})
	require.NoError(t, err)

	t.Log("Inspecting the database")
	_ = db.View(func(tx *bolt.Tx) error {
		actualStructure := tx.Inspect()
		assert.Equal(t, expectedStructure, actualStructure)
		return nil
	})
}

// Ensure a large bucket can calculate stats.
func TestBucket_Stats_Large(t *testing.T) {
	if testing.Short() {
		t.Skip("skipping test in short mode.")
	}

	db := btesting.MustCreateDB(t)

	var index int
	for i := 0; i < 100; i++ {
		// Add bucket with lots of keys.
		if err := db.Update(func(tx *bolt.Tx) error {
			b, err := tx.CreateBucketIfNotExists([]byte("widgets"))
			if err != nil {
				t.Fatal(err)
			}
			for i := 0; i < 1000; i++ {
				if err := b.Put([]byte(strconv.Itoa(index)), []byte(strconv.Itoa(index))); err != nil {
					t.Fatal(err)
				}
				index++
			}
			return nil
		}); err != nil {
			t.Fatal(err)
		}
	}

	db.MustCheck()

	pageSize2stats := map[int]bolt.BucketStats{
		4096: {
			BranchPageN:       13,
			BranchOverflowN:   0,
			LeafPageN:         1196,
			LeafOverflowN:     0,
			KeyN:              100000,
			Depth:             3,
			BranchAlloc:       53248,
			BranchInuse:       25257,
			LeafAlloc:         4898816,
			LeafInuse:         2596916,
			BucketN:           1,
			InlineBucketN:     0,
			InlineBucketInuse: 0},
		16384: {
			BranchPageN:       1,
			BranchOverflowN:   0,
			LeafPageN:         292,
			LeafOverflowN:     0,
			KeyN:              100000,
			Depth:             2,
			BranchAlloc:       16384,
			BranchInuse:       6094,
			LeafAlloc:         4784128,
			LeafInuse:         2582452,
			BucketN:           1,
			InlineBucketN:     0,
			InlineBucketInuse: 0},
		65536: {
			BranchPageN:       1,
			BranchOverflowN:   0,
			LeafPageN:         73,
			LeafOverflowN:     0,
			KeyN:              100000,
			Depth:             2,
			BranchAlloc:       65536,
			BranchInuse:       1534,
			LeafAlloc:         4784128,
			LeafInuse:         2578948,
			BucketN:           1,
			InlineBucketN:     0,
			InlineBucketInuse: 0},
	}

	if err := db.View(func(tx *bolt.Tx) error {
		stats := tx.Bucket([]byte("widgets")).Stats()
		t.Logf("Stats: %#v", stats)
		if expected, ok := pageSize2stats[db.Info().PageSize]; ok {
			assert.EqualValues(t, expected, stats, "stats differs from expectations")
		} else {
			t.Skipf("No expectations for page size: %d", db.Info().PageSize)
		}
		return nil
	}); err != nil {
		t.Fatal(err)
	}
}

// Ensure that a bucket can write random keys and values across multiple transactions.
func TestBucket_Put_Single(t *testing.T) {
	if testing.Short() {
		t.Skip("skipping test in short mode.")
	}

	index := 0
	if err := quick.Check(func(items testdata) bool {
		db := btesting.MustCreateDB(t)
		defer db.MustClose()

		m := make(map[string][]byte)

		if err := db.Update(func(tx *bolt.Tx) error {
			if _, err := tx.CreateBucket([]byte("widgets")); err != nil {
				t.Fatal(err)
			}
			return nil
		}); err != nil {
			t.Fatal(err)
		}

		for _, item := range items {
			if err := db.Update(func(tx *bolt.Tx) error {
				if err := tx.Bucket([]byte("widgets")).Put(item.Key, item.Value); err != nil {
					panic("put error: " + err.Error())
				}
				m[string(item.Key)] = item.Value
				return nil
			}); err != nil {
				t.Fatal(err)
			}

			// Verify all key/values so far.
			if err := db.View(func(tx *bolt.Tx) error {
				i := 0
				for k, v := range m {
					value := tx.Bucket([]byte("widgets")).Get([]byte(k))
					if !bytes.Equal(value, v) {
						t.Logf("value mismatch [run %d] (%d of %d):\nkey: %x\ngot: %x\nexp: %x", index, i, len(m), []byte(k), value, v)
						db.CopyTempFile()
						t.FailNow()
					}
					i++
				}
				return nil
			}); err != nil {
				t.Fatal(err)
			}
		}

		index++
		return true
	}, qconfig()); err != nil {
		t.Error(err)
	}
}

// Ensure that a transaction can insert multiple key/value pairs at once.
func TestBucket_Put_Multiple(t *testing.T) {
	if testing.Short() {
		t.Skip("skipping test in short mode.")
	}

	if err := quick.Check(func(items testdata) bool {
		db := btesting.MustCreateDB(t)
		defer db.MustClose()

		// Bulk insert all values.
		if err := db.Update(func(tx *bolt.Tx) error {
			if _, err := tx.CreateBucket([]byte("widgets")); err != nil {
				t.Fatal(err)
			}
			return nil
		}); err != nil {
			t.Fatal(err)
		}

		if err := db.Update(func(tx *bolt.Tx) error {
			b := tx.Bucket([]byte("widgets"))
			for _, item := range items {
				if err := b.Put(item.Key, item.Value); err != nil {
					t.Fatal(err)
				}
			}
			return nil
		}); err != nil {
			t.Fatal(err)
		}

		// Verify all items exist.
		if err := db.View(func(tx *bolt.Tx) error {
			b := tx.Bucket([]byte("widgets"))
			for _, item := range items {
				value := b.Get(item.Key)
				if !bytes.Equal(item.Value, value) {
					db.CopyTempFile()
					t.Fatalf("exp=%x; got=%x", item.Value, value)
				}
			}
			return nil
		}); err != nil {
			t.Fatal(err)
		}

		return true
	}, qconfig()); err != nil {
		t.Error(err)
	}
}

// Ensure that a transaction can delete all key/value pairs and return to a single leaf page.
func TestBucket_Delete_Quick(t *testing.T) {
	if testing.Short() {
		t.Skip("skipping test in short mode.")
	}

	if err := quick.Check(func(items testdata) bool {
		db := btesting.MustCreateDB(t)
		defer db.MustClose()

		// Bulk insert all values.
		if err := db.Update(func(tx *bolt.Tx) error {
			if _, err := tx.CreateBucket([]byte("widgets")); err != nil {
				t.Fatal(err)
			}
			return nil
		}); err != nil {
			t.Fatal(err)
		}

		if err := db.Update(func(tx *bolt.Tx) error {
			b := tx.Bucket([]byte("widgets"))
			for _, item := range items {
				if err := b.Put(item.Key, item.Value); err != nil {
					t.Fatal(err)
				}
			}
			return nil
		}); err != nil {
			t.Fatal(err)
		}

		// Remove items one at a time and check consistency.
		for _, item := range items {
			if err := db.Update(func(tx *bolt.Tx) error {
				return tx.Bucket([]byte("widgets")).Delete(item.Key)
			}); err != nil {
				t.Fatal(err)
			}
		}

		// Anything before our deletion index should be nil.
		if err := db.View(func(tx *bolt.Tx) error {
			if err := tx.Bucket([]byte("widgets")).ForEach(func(k, v []byte) error {
				t.Fatalf("bucket should be empty; found: %06x", trunc(k, 3))
				return nil
			}); err != nil {
				t.Fatal(err)
			}
			return nil
		}); err != nil {
			t.Fatal(err)
		}

		return true
	}, qconfig()); err != nil {
		t.Error(err)
	}
}

func BenchmarkBucket_CreateBucketIfNotExists(b *testing.B) {
	db := btesting.MustCreateDB(b)
	defer db.MustClose()

	const bucketCount = 1_000_000

	err := db.Update(func(tx *bolt.Tx) error {
		for i := 0; i < bucketCount; i++ {
			bucketName := fmt.Sprintf("bucket_%d", i)
			_, berr := tx.CreateBucket([]byte(bucketName))
			require.NoError(b, berr)
		}
		return nil
	})
	require.NoError(b, err)

	b.ResetTimer()
	b.ReportAllocs()

	for i := 0; i < b.N; i++ {
		err := db.Update(func(tx *bolt.Tx) error {
			_, berr := tx.CreateBucketIfNotExists([]byte("bucket_100"))
			return berr
		})
		require.NoError(b, err)
	}
}

func ExampleBucket_Put() {
	// Open the database.
	db, err := bolt.Open(tempfile(), 0600, nil)
	if err != nil {
		log.Fatal(err)
	}
	defer os.Remove(db.Path())

	// Start a write transaction.
	if err := db.Update(func(tx *bolt.Tx) error {
		// Create a bucket.
		b, err := tx.CreateBucket([]byte("widgets"))
		if err != nil {
			return err
		}

		// Set the value "bar" for the key "foo".
		if err := b.Put([]byte("foo"), []byte("bar")); err != nil {
			return err
		}
		return nil
	}); err != nil {
		log.Fatal(err)
	}

	// Read value back in a different read-only transaction.
	if err := db.View(func(tx *bolt.Tx) error {
		value := tx.Bucket([]byte("widgets")).Get([]byte("foo"))
		fmt.Printf("The value of 'foo' is: %s\n", value)
		return nil
	}); err != nil {
		log.Fatal(err)
	}

	// Close database to release file lock.
	if err := db.Close(); err != nil {
		log.Fatal(err)
	}

	// Output:
	// The value of 'foo' is: bar
}

func ExampleBucket_Delete() {
	// Open the database.
	db, err := bolt.Open(tempfile(), 0600, nil)
	if err != nil {
		log.Fatal(err)
	}
	defer os.Remove(db.Path())

	// Start a write transaction.
	if err := db.Update(func(tx *bolt.Tx) error {
		// Create a bucket.
		b, err := tx.CreateBucket([]byte("widgets"))
		if err != nil {
			return err
		}

		// Set the value "bar" for the key "foo".
		if err := b.Put([]byte("foo"), []byte("bar")); err != nil {
			return err
		}

		// Retrieve the key back from the database and verify it.
		value := b.Get([]byte("foo"))
		fmt.Printf("The value of 'foo' was: %s\n", value)

		return nil
	}); err != nil {
		log.Fatal(err)
	}

	// Delete the key in a different write transaction.
	if err := db.Update(func(tx *bolt.Tx) error {
		return tx.Bucket([]byte("widgets")).Delete([]byte("foo"))
	}); err != nil {
		log.Fatal(err)
	}

	// Retrieve the key again.
	if err := db.View(func(tx *bolt.Tx) error {
		value := tx.Bucket([]byte("widgets")).Get([]byte("foo"))
		if value == nil {
			fmt.Printf("The value of 'foo' is now: nil\n")
		}
		return nil
	}); err != nil {
		log.Fatal(err)
	}

	// Close database to release file lock.
	if err := db.Close(); err != nil {
		log.Fatal(err)
	}

	// Output:
	// The value of 'foo' was: bar
	// The value of 'foo' is now: nil
}

func ExampleBucket_ForEach() {
	// Open the database.
	db, err := bolt.Open(tempfile(), 0600, nil)
	if err != nil {
		log.Fatal(err)
	}
	defer os.Remove(db.Path())

	// Insert data into a bucket.
	if err := db.Update(func(tx *bolt.Tx) error {
		b, err := tx.CreateBucket([]byte("animals"))
		if err != nil {
			return err
		}

		if err := b.Put([]byte("dog"), []byte("fun")); err != nil {
			return err
		}
		if err := b.Put([]byte("cat"), []byte("lame")); err != nil {
			return err
		}
		if err := b.Put([]byte("liger"), []byte("awesome")); err != nil {
			return err
		}

		// Iterate over items in sorted key order.
		if err := b.ForEach(func(k, v []byte) error {
			fmt.Printf("A %s is %s.\n", k, v)
			return nil
		}); err != nil {
			return err
		}

		return nil
	}); err != nil {
		log.Fatal(err)
	}

	// Close database to release file lock.
	if err := db.Close(); err != nil {
		log.Fatal(err)
	}

	// Output:
	// A cat is lame.
	// A dog is fun.
	// A liger is awesome.
}
```

## File: `code-of-conduct.md`
```markdown
# etcd Community Code of Conduct

Please refer to [etcd Community Code of Conduct](https://github.com/etcd-io/etcd/blob/main/code-of-conduct.md).
```

## File: `compact.go`
```go
package bbolt

// Compact will create a copy of the source DB and in the destination DB. This may
// reclaim space that the source database no longer has use for. txMaxSize can be
// used to limit the transactions size of this process and may trigger intermittent
// commits. A value of zero will ignore transaction sizes.
// TODO: merge with: https://github.com/etcd-io/etcd/blob/b7f0f52a16dbf83f18ca1d803f7892d750366a94/mvcc/backend/backend.go#L349
func Compact(dst, src *DB, txMaxSize int64) error {
	// commit regularly, or we'll run out of memory for large datasets if using one transaction.
	var size int64
	tx, err := dst.Begin(true)
	if err != nil {
		return err
	}
	defer func() {
		if tempErr := tx.Rollback(); tempErr != nil {
			err = tempErr
		}
	}()

	if err := walk(src, func(keys [][]byte, k, v []byte, seq uint64) error {
		// On each key/value, check if we have exceeded tx size.
		sz := int64(len(k) + len(v))
		if size+sz > txMaxSize && txMaxSize != 0 {
			// Commit previous transaction.
			if err := tx.Commit(); err != nil {
				return err
			}

			// Start new transaction.
			tx, err = dst.Begin(true)
			if err != nil {
				return err
			}
			size = 0
		}
		size += sz

		// Create bucket on the root transaction if this is the first level.
		nk := len(keys)
		if nk == 0 {
			bkt, err := tx.CreateBucket(k)
			if err != nil {
				return err
			}
			if err := bkt.SetSequence(seq); err != nil {
				return err
			}
			return nil
		}

		// Create buckets on subsequent levels, if necessary.
		b := tx.Bucket(keys[0])
		if nk > 1 {
			for _, k := range keys[1:] {
				b = b.Bucket(k)
			}
		}

		// Fill the entire page for best compaction.
		b.FillPercent = 1.0

		// If there is no value then this is a bucket call.
		if v == nil {
			bkt, err := b.CreateBucket(k)
			if err != nil {
				return err
			}
			if err := bkt.SetSequence(seq); err != nil {
				return err
			}
			return nil
		}

		// Otherwise treat it as a key/value pair.
		return b.Put(k, v)
	}); err != nil {
		return err
	}
	err = tx.Commit()

	return err
}

// walkFunc is the type of the function called for keys (buckets and "normal"
// values) discovered by Walk. keys is the list of keys to descend to the bucket
// owning the discovered key/value pair k/v.
type walkFunc func(keys [][]byte, k, v []byte, seq uint64) error

// walk walks recursively the bolt database db, calling walkFn for each key it finds.
func walk(db *DB, walkFn walkFunc) error {
	return db.View(func(tx *Tx) error {
		return tx.ForEach(func(name []byte, b *Bucket) error {
			return walkBucket(b, nil, name, nil, b.Sequence(), walkFn)
		})
	})
}

func walkBucket(b *Bucket, keypath [][]byte, k, v []byte, seq uint64, fn walkFunc) error {
	// Execute callback.
	if err := fn(keypath, k, v, seq); err != nil {
		return err
	}

	// If this is not a bucket then stop.
	if v != nil {
		return nil
	}

	// Iterate over each child key/value.
	keypath = append(keypath, k)
	return b.ForEach(func(k, v []byte) error {
		if v == nil {
			bkt := b.Bucket(k)
			return walkBucket(bkt, keypath, k, nil, bkt.Sequence(), fn)
		}
		return walkBucket(b, keypath, k, v, b.Sequence(), fn)
	})
}
```

## File: `concurrent_test.go`
```go
package bbolt_test

import (
	"bytes"
	crand "crypto/rand"
	"encoding/hex"
	"encoding/json"
	"fmt"
	"io"
	mrand "math/rand"
	"os"
	"path/filepath"
	"sort"
	"strings"
	"sync"
	"testing"
	"time"
	"unicode/utf8"

	"github.com/stretchr/testify/require"
	"golang.org/x/sync/errgroup"

	bolt "go.etcd.io/bbolt"
)

const (
	bucketPrefix = "bucket"
	keyPrefix    = "key"
	noopTxKey    = "%magic-no-op-key%"

	// TestConcurrentCaseDuration is used as a env variable to specify the
	// concurrent test duration.
	testConcurrentCaseDuration    = "TEST_CONCURRENT_CASE_DURATION"
	defaultConcurrentTestDuration = 30 * time.Second
)

type duration struct {
	min time.Duration
	max time.Duration
}

type bytesRange struct {
	min int
	max int
}

type operationChance struct {
	operation OperationType
	chance    int
}

type concurrentConfig struct {
	bucketCount    int
	keyCount       int
	workInterval   duration
	operationRatio []operationChance
	readInterval   duration   // only used by readOperation
	noopWriteRatio int        // only used by writeOperation
	writeBytes     bytesRange // only used by writeOperation
}

/*
TestConcurrentGenericReadAndWrite verifies:
 1. Repeatable read: a read transaction should always see the same data
    view during its lifecycle.
 2. Any data written by a writing transaction should be visible to any
    following reading transactions (with txid >= previous writing txid).
 3. The txid should never decrease.
*/
func TestConcurrentGenericReadAndWrite(t *testing.T) {
	if testing.Short() {
		t.Skip("skipping test in short mode.")
	}

	testDuration := concurrentTestDuration(t)
	conf := concurrentConfig{
		bucketCount:  5,
		keyCount:     10000,
		workInterval: duration{},
		operationRatio: []operationChance{
			{operation: Read, chance: 60},
			{operation: Write, chance: 20},
			{operation: Delete, chance: 20},
		},
		readInterval: duration{
			min: 50 * time.Millisecond,
			max: 100 * time.Millisecond,
		},
		noopWriteRatio: 20,
		writeBytes: bytesRange{
			min: 200,
			max: 16000,
		},
	}

	testCases := []struct {
		name         string
		workerCount  int
		conf         concurrentConfig
		testDuration time.Duration
	}{
		{
			name:         "1 worker",
			workerCount:  1,
			conf:         conf,
			testDuration: testDuration,
		},
		{
			name:         "10 workers",
			workerCount:  10,
			conf:         conf,
			testDuration: testDuration,
		},
		{
			name:         "50 workers",
			workerCount:  50,
			conf:         conf,
			testDuration: testDuration,
		},
		{
			name:         "100 workers",
			workerCount:  100,
			conf:         conf,
			testDuration: testDuration,
		},
		{
			name:         "200 workers",
			workerCount:  200,
			conf:         conf,
			testDuration: testDuration,
		},
	}

	for _, tc := range testCases {
		tc := tc
		t.Run(tc.name, func(t *testing.T) {
			concurrentReadAndWrite(t,
				tc.workerCount,
				tc.conf,
				tc.testDuration)
		})
	}
}

func concurrentTestDuration(t *testing.T) time.Duration {
	durationInEnv := strings.ToLower(os.Getenv(testConcurrentCaseDuration))
	if durationInEnv == "" {
		t.Logf("%q not set, defaults to %s", testConcurrentCaseDuration, defaultConcurrentTestDuration)
		return defaultConcurrentTestDuration
	}

	d, err := time.ParseDuration(durationInEnv)
	if err != nil {
		t.Logf("Failed to parse %s=%s, error: %v, defaults to %s", testConcurrentCaseDuration, durationInEnv, err, defaultConcurrentTestDuration)
		return defaultConcurrentTestDuration
	}

	t.Logf("Concurrent test duration set by %s=%s", testConcurrentCaseDuration, d)
	return d
}

func concurrentReadAndWrite(t *testing.T,
	workerCount int,
	conf concurrentConfig,
	testDuration time.Duration) {

	t.Log("Preparing db.")
	db := mustCreateDB(t, &bolt.Options{
		PageSize: 4096,
	})
	defer db.Close()
	err := db.Update(func(tx *bolt.Tx) error {
		for i := 0; i < conf.bucketCount; i++ {
			if _, err := tx.CreateBucketIfNotExists(bucketName(i)); err != nil {
				return err
			}
		}
		return nil
	})
	require.NoError(t, err)

	var records historyRecords
	// t.Failed() returns false during panicking. We need to forcibly
	// save data on panicking.
	// Refer to: https://github.com/golang/go/issues/49929
	panicked := true
	defer func() {
		t.Log("Save data if failed.")
		saveDataIfFailed(t, db, records, panicked)
	}()

	t.Log("Starting workers.")
	records = runWorkers(t,
		db,
		workerCount,
		conf,
		testDuration)

	t.Log("Analyzing the history records.")
	if err := validateSequential(records); err != nil {
		t.Errorf("The history records are not sequential:\n %v", err)
	}

	t.Log("Checking database consistency.")
	if err := checkConsistency(t, db); err != nil {
		t.Errorf("The data isn't consistency: %v", err)
	}

	panicked = false
	// TODO (ahrtr):
	//   1. intentionally inject a random failpoint.
}

// mustCreateDB is created in place of `btesting.MustCreateDB`, and it's
// only supposed to be used by the concurrent test case. The purpose is
// to ensure the test case can be executed on old branches or versions,
// e.g. `release-1.3` or `1.3.[5-7]`.
func mustCreateDB(t *testing.T, o *bolt.Options) *bolt.DB {
	f := filepath.Join(t.TempDir(), "db")

	return mustOpenDB(t, f, o)
}

func mustReOpenDB(t *testing.T, db *bolt.DB, o *bolt.Options) *bolt.DB {
	f := db.Path()

	t.Logf("Closing bbolt DB at: %s", f)
	err := db.Close()
	require.NoError(t, err)

	return mustOpenDB(t, f, o)
}

func mustOpenDB(t *testing.T, dbPath string, o *bolt.Options) *bolt.DB {
	t.Logf("Opening bbolt DB at: %s", dbPath)
	if o == nil {
		o = bolt.DefaultOptions
	}

	freelistType := bolt.FreelistArrayType
	if env := os.Getenv("TEST_FREELIST_TYPE"); env == string(bolt.FreelistMapType) {
		freelistType = bolt.FreelistMapType
	}

	o.FreelistType = freelistType

	db, err := bolt.Open(dbPath, 0600, o)
	require.NoError(t, err)

	return db
}

func checkConsistency(t *testing.T, db *bolt.DB) error {
	return db.View(func(tx *bolt.Tx) error {
		cnt := 0
		for err := range tx.Check() {
			t.Errorf("Consistency error: %v", err)
			cnt++
		}
		if cnt > 0 {
			return fmt.Errorf("%d consistency errors found", cnt)
		}
		return nil
	})
}

/*
*********************************************************
Data structures and functions/methods for running concurrent
workers, which execute different operations, including `Read`,
`Write` and `Delete`.
*********************************************************
*/
func runWorkers(t *testing.T,
	db *bolt.DB,
	workerCount int,
	conf concurrentConfig,
	testDuration time.Duration) historyRecords {
	stopCh := make(chan struct{}, 1)
	errCh := make(chan error, workerCount)

	var mu sync.Mutex
	var rs historyRecords

	g := new(errgroup.Group)
	for i := 0; i < workerCount; i++ {
		w := &worker{
			id: i,
			db: db,

			conf: conf,

			errCh:  errCh,
			stopCh: stopCh,
			t:      t,
		}
		g.Go(func() error {
			wrs, err := runWorker(t, w, errCh)
			mu.Lock()
			rs = append(rs, wrs...)
			mu.Unlock()
			return err
		})
	}

	t.Logf("Keep all workers running for about %s.", testDuration)
	select {
	case <-time.After(testDuration):
	case <-errCh:
	}

	close(stopCh)
	t.Log("Waiting for all workers to finish.")
	if err := g.Wait(); err != nil {
		t.Errorf("Received error: %v", err)
	}

	return rs
}

func runWorker(t *testing.T, w *worker, errCh chan error) (historyRecords, error) {
	rs, err := w.run()
	if len(rs) > 0 && err == nil {
		if terr := validateIncrementalTxid(rs); terr != nil {
			txidErr := fmt.Errorf("[%s]: %w", w.name(), terr)
			t.Error(txidErr)
			errCh <- txidErr
			return rs, txidErr
		}
	}
	return rs, err
}

type worker struct {
	id int
	db *bolt.DB

	conf concurrentConfig

	errCh  chan error
	stopCh chan struct{}

	t *testing.T
}

func (w *worker) name() string {
	return fmt.Sprintf("worker-%d", w.id)
}

func (w *worker) run() (historyRecords, error) {
	var rs historyRecords

	ticker := time.NewTicker(1 * time.Second)
	defer ticker.Stop()

	for {
		select {
		case <-w.stopCh:
			return rs, nil
		default:
		}

		err := w.db.Update(func(tx *bolt.Tx) error {
			for {
				op := w.pickOperation()
				bucket, key := w.pickBucket(), w.pickKey()
				rec, eerr := executeOperation(op, tx, bucket, key, w.conf)
				if eerr != nil {
					opErr := fmt.Errorf("[%s: %s]: %w", w.name(), op, eerr)
					w.t.Error(opErr)
					w.errCh <- opErr
					return opErr
				}

				rs = append(rs, rec)
				if w.conf.workInterval != (duration{}) {
					time.Sleep(randomDurationInRange(w.conf.workInterval.min, w.conf.workInterval.max))
				}

				select {
				case <-ticker.C:
					return nil
				case <-w.stopCh:
					return nil
				default:
				}
			}
		})
		if err != nil {
			return rs, err
		}
	}
}

func (w *worker) pickBucket() []byte {
	return bucketName(mrand.Intn(w.conf.bucketCount))
}

func bucketName(index int) []byte {
	bucket := fmt.Sprintf("%s_%d", bucketPrefix, index)
	return []byte(bucket)
}

func (w *worker) pickKey() []byte {
	key := fmt.Sprintf("%s_%d", keyPrefix, mrand.Intn(w.conf.keyCount))
	return []byte(key)
}

func (w *worker) pickOperation() OperationType {
	sum := 0
	for _, op := range w.conf.operationRatio {
		sum += op.chance
	}
	roll := mrand.Int() % sum
	for _, op := range w.conf.operationRatio {
		if roll < op.chance {
			return op.operation
		}
		roll -= op.chance
	}
	panic("unexpected")
}

func executeOperation(op OperationType, tx *bolt.Tx, bucket []byte, key []byte, conf concurrentConfig) (historyRecord, error) {
	switch op {
	case Read:
		return executeRead(tx, bucket, key, conf.readInterval)
	case Write:
		return executeWrite(tx, bucket, key, conf.writeBytes, conf.noopWriteRatio)
	case Delete:
		return executeDelete(tx, bucket, key)
	default:
		panic(fmt.Sprintf("unexpected operation type: %s", op))
	}
}

func executeRead(tx *bolt.Tx, bucket []byte, key []byte, readInterval duration) (historyRecord, error) {
	var rec historyRecord

	b := tx.Bucket(bucket)

	initialVal := b.Get(key)
	time.Sleep(randomDurationInRange(readInterval.min, readInterval.max))
	val := b.Get(key)

	if !bytes.Equal(initialVal, val) {
		return rec, fmt.Errorf("read different values for the same key (%q), value1: %q, value2: %q",
			string(key), formatBytes(initialVal), formatBytes(val))
	}

	clonedVal := make([]byte, len(val))
	copy(clonedVal, val)

	rec = historyRecord{
		OperationType: Read,
		Bucket:        string(bucket),
		Key:           string(key),
		Value:         clonedVal,
		Txid:          tx.ID(),
	}

	return rec, nil
}

func executeWrite(tx *bolt.Tx, bucket []byte, key []byte, writeBytes bytesRange, noopWriteRatio int) (historyRecord, error) {
	var rec historyRecord

	if mrand.Intn(100) < noopWriteRatio {
		// A no-op write transaction has two consequences:
		//    1. The txid increases by 1;
		//    2. Two meta pages point to the same root page.
		rec = historyRecord{
			OperationType: Write,
			Bucket:        string(bucket),
			Key:           noopTxKey,
			Value:         nil,
			Txid:          tx.ID(),
		}
		return rec, nil
	}

	b := tx.Bucket(bucket)

	valueBytes := randomIntInRange(writeBytes.min, writeBytes.max)
	v := make([]byte, valueBytes)
	if _, cErr := crand.Read(v); cErr != nil {
		return rec, cErr
	}

	putErr := b.Put(key, v)
	if putErr == nil {
		rec = historyRecord{
			OperationType: Write,
			Bucket:        string(bucket),
			Key:           string(key),
			Value:         v,
			Txid:          tx.ID(),
		}
	}

	return rec, putErr
}

func executeDelete(tx *bolt.Tx, bucket []byte, key []byte) (historyRecord, error) {
	var rec historyRecord

	b := tx.Bucket(bucket)

	err := b.Delete(key)
	if err == nil {
		rec = historyRecord{
			OperationType: Delete,
			Bucket:        string(bucket),
			Key:           string(key),
			Txid:          tx.ID(),
		}
	}

	return rec, err
}

func randomDurationInRange(min, max time.Duration) time.Duration {
	d := int64(max) - int64(min)
	d = int64(mrand.Intn(int(d))) + int64(min)
	return time.Duration(d)
}

func randomIntInRange(min, max int) int {
	return mrand.Intn(max-min) + min
}

func formatBytes(val []byte) string {
	if utf8.ValidString(string(val)) {
		return string(val)
	}

	return hex.EncodeToString(val)
}

/*
*********************************************************
Functions for persisting test data, including db file
and operation history
*********************************************************
*/
func saveDataIfFailed(t *testing.T, db *bolt.DB, rs historyRecords, force bool) {
	if t.Failed() || force {
		t.Log("Saving data...")
		dbPath := db.Path()
		if err := db.Close(); err != nil {
			t.Errorf("Failed to close db: %v", err)
		}
		backupPath := testResultsDirectory(t)
		backupDB(t, dbPath, backupPath)
		persistHistoryRecords(t, rs, backupPath)
	}
}

func backupDB(t *testing.T, srcPath string, dstPath string) {
	targetFile := filepath.Join(dstPath, "db.bak")
	t.Logf("Saving the DB file to %s", targetFile)
	err := copyFile(srcPath, targetFile)
	require.NoError(t, err)
	t.Logf("DB file saved to %s", targetFile)
}

func copyFile(srcPath, dstPath string) error {
	// Ensure source file exists.
	_, err := os.Stat(srcPath)
	if os.IsNotExist(err) {
		return fmt.Errorf("source file %q not found", srcPath)
	} else if err != nil {
		return err
	}

	// Ensure output file not exist.
	_, err = os.Stat(dstPath)
	if err == nil {
		return fmt.Errorf("output file %q already exists", dstPath)
	} else if !os.IsNotExist(err) {
		return err
	}

	srcDB, err := os.Open(srcPath)
	if err != nil {
		return fmt.Errorf("failed to open source file %q: %w", srcPath, err)
	}
	defer srcDB.Close()
	dstDB, err := os.Create(dstPath)
	if err != nil {
		return fmt.Errorf("failed to create output file %q: %w", dstPath, err)
	}
	defer dstDB.Close()
	written, err := io.Copy(dstDB, srcDB)
	if err != nil {
		return fmt.Errorf("failed to copy database file from %q to %q: %w", srcPath, dstPath, err)
	}

	srcFi, err := srcDB.Stat()
	if err != nil {
		return fmt.Errorf("failed to get source file info %q: %w", srcPath, err)
	}
	initialSize := srcFi.Size()
	if initialSize != written {
		return fmt.Errorf("the byte copied (%q: %d) isn't equal to the initial db size (%q: %d)", dstPath, written, srcPath, initialSize)
	}

	return nil
}

func persistHistoryRecords(t *testing.T, rs historyRecords, path string) {
	recordFilePath := filepath.Join(path, "history_records.json")
	t.Logf("Saving history records to %s", recordFilePath)
	recordFile, err := os.OpenFile(recordFilePath, os.O_RDWR|os.O_CREATE|os.O_TRUNC, 0755)
	require.NoError(t, err)
	defer recordFile.Close()
	encoder := json.NewEncoder(recordFile)
	for _, rec := range rs {
		err := encoder.Encode(rec)
		require.NoError(t, err)
	}
}

func testResultsDirectory(t *testing.T) string {
	resultsDirectory, ok := os.LookupEnv("RESULTS_DIR")
	var err error
	if !ok {
		resultsDirectory, err = os.MkdirTemp("", "*.db")
		require.NoError(t, err)
	}
	resultsDirectory, err = filepath.Abs(resultsDirectory)
	require.NoError(t, err)

	path, err := filepath.Abs(filepath.Join(resultsDirectory, strings.ReplaceAll(t.Name(), "/", "_")))
	require.NoError(t, err)

	err = os.RemoveAll(path)
	require.NoError(t, err)

	err = os.MkdirAll(path, 0700)
	require.NoError(t, err)

	return path
}

/*
*********************************************************
Data structures and functions for analyzing history records
*********************************************************
*/
type OperationType string

const (
	Read   OperationType = "read"
	Write  OperationType = "write"
	Delete OperationType = "delete"
)

type historyRecord struct {
	OperationType OperationType `json:"operationType,omitempty"`
	Txid          int           `json:"txid,omitempty"`
	Bucket        string        `json:"bucket,omitempty"`
	Key           string        `json:"key,omitempty"`
	Value         []byte        `json:"value,omitempty"`
}

type historyRecords []historyRecord

func (rs historyRecords) Len() int {
	return len(rs)
}

func (rs historyRecords) Less(i, j int) bool {
	// Sorted by (bucket, key) firstly: all records in the same
	// (bucket, key) are grouped together.
	bucketCmp := strings.Compare(rs[i].Bucket, rs[j].Bucket)
	if bucketCmp != 0 {
		return bucketCmp < 0
	}
	keyCmp := strings.Compare(rs[i].Key, rs[j].Key)
	if keyCmp != 0 {
		return keyCmp < 0
	}

	// Sorted by txid
	return rs[i].Txid < rs[j].Txid
}

func (rs historyRecords) Swap(i, j int) {
	rs[i], rs[j] = rs[j], rs[i]
}

func validateIncrementalTxid(rs historyRecords) error {
	lastTxid := rs[0].Txid

	for i := 1; i < len(rs); i++ {
		if rs[i].Txid < lastTxid {
			return fmt.Errorf("detected non-incremental txid(%d, %d) in %s mode", lastTxid, rs[i].Txid, rs[i].OperationType)
		}
		lastTxid = rs[i].Txid
	}

	return nil
}

func validateSequential(rs historyRecords) error {
	sort.Stable(rs)

	type bucketAndKey struct {
		bucket string
		key    string
	}
	lastWriteKeyValueMap := make(map[bucketAndKey]*historyRecord)

	for _, rec := range rs {
		bk := bucketAndKey{
			bucket: rec.Bucket,
			key:    rec.Key,
		}
		if v, ok := lastWriteKeyValueMap[bk]; ok {
			if rec.OperationType == Write {
				v.Txid = rec.Txid
				if rec.Key != noopTxKey {
					v.Value = rec.Value
				}
			} else if rec.OperationType == Delete {
				delete(lastWriteKeyValueMap, bk)
			} else {
				if !bytes.Equal(v.Value, rec.Value) {
					return fmt.Errorf("readOperation[txid: %d, bucket: %s, key: %s] read %x, \nbut writer[txid: %d] wrote %x",
						rec.Txid, rec.Bucket, rec.Key, rec.Value, v.Txid, v.Value)
				}
			}
		} else {
			if rec.OperationType == Write && rec.Key != noopTxKey {
				lastWriteKeyValueMap[bk] = &historyRecord{
					OperationType: Write,
					Bucket:        rec.Bucket,
					Key:           rec.Key,
					Value:         rec.Value,
					Txid:          rec.Txid,
				}
			} else if rec.OperationType == Read {
				if len(rec.Value) != 0 {
					return fmt.Errorf("expected the first readOperation[txid: %d, bucket: %s, key: %s] read nil, \nbut got %x",
						rec.Txid, rec.Bucket, rec.Key, rec.Value)
				}
			}
		}
	}

	return nil
}

/*
TestConcurrentRepeatableRead verifies repeatable read. The case
intentionally creates a scenario that read and write transactions
are interleaved. It performs several writing operations after starting
each long-running read transaction to ensure it has a larger txid
than previous read transaction. It verifies that bbolt correctly
releases free pages, and will not pollute (e.g. prematurely release)
any pages which are still being used by any read transaction.
*/
func TestConcurrentRepeatableRead(t *testing.T) {
	if testing.Short() {
		t.Skip("skipping test in short mode.")
	}

	testCases := []struct {
		name           string
		noFreelistSync bool
		freelistType   bolt.FreelistType
	}{
		// [array] freelist
		{
			name:           "sync array freelist",
			noFreelistSync: false,
			freelistType:   bolt.FreelistArrayType,
		},
		{
			name:           "not sync array freelist",
			noFreelistSync: true,
			freelistType:   bolt.FreelistArrayType,
		},
		// [map] freelist
		{
			name:           "sync map freelist",
			noFreelistSync: false,
			freelistType:   bolt.FreelistMapType,
		},
		{
			name:           "not sync map freelist",
			noFreelistSync: true,
			freelistType:   bolt.FreelistMapType,
		},
	}

	for _, tc := range testCases {
		tc := tc
		t.Run(tc.name, func(t *testing.T) {

			t.Log("Preparing db.")
			var (
				bucket = []byte("data")
				key    = []byte("mykey")

				option = &bolt.Options{
					PageSize:       4096,
					NoFreelistSync: tc.noFreelistSync,
					FreelistType:   tc.freelistType,
				}
			)

			db := mustCreateDB(t, option)
			defer func() {
				// The db will be reopened later, so put `db.Close()` in a function
				// to avoid premature evaluation of `db`. Note that the execution
				// of a deferred function is deferred to the moment the surrounding
				// function returns, but the function value and parameters to the
				// call are evaluated as usual and saved anew.
				db.Close()
			}()

			// Create lots of K/V to allocate some pages
			err := db.Update(func(tx *bolt.Tx) error {
				b, err := tx.CreateBucketIfNotExists(bucket)
				if err != nil {
					return err
				}
				for i := 0; i < 1000; i++ {
					k := fmt.Sprintf("key_%d", i)
					if err := b.Put([]byte(k), make([]byte, 1024)); err != nil {
						return err
					}
				}
				return nil
			})
			require.NoError(t, err)

			// Remove all K/V to create some free pages
			err = db.Update(func(tx *bolt.Tx) error {
				b := tx.Bucket(bucket)
				for i := 0; i < 1000; i++ {
					k := fmt.Sprintf("key_%d", i)
					if err := b.Delete([]byte(k)); err != nil {
						return err
					}
				}
				return b.Put(key, []byte("randomValue"))
			})
			require.NoError(t, err)

			// bbolt will not release free pages directly after committing
			// a writing transaction; instead all pages freed are putting
			// into a pending list. Accordingly, the free pages might not
			// be able to be reused by following writing transactions. So
			// we reopen the db to completely release all free pages.
			db = mustReOpenDB(t, db, option)

			var (
				wg                     sync.WaitGroup
				longRunningReaderCount = 10
				stopCh                 = make(chan struct{})
				errCh                  = make(chan error, longRunningReaderCount)
				readInterval           = duration{5 * time.Millisecond, 10 * time.Millisecond}

				writeOperationCountInBetween = 5
				writeBytes                   = bytesRange{10, 20}

				testDuration = 10 * time.Second
			)

			for i := 0; i < longRunningReaderCount; i++ {
				readWorkerName := fmt.Sprintf("reader_%d", i)
				t.Logf("Starting long running read operation: %s", readWorkerName)
				wg.Add(1)
				go func() {
					defer wg.Done()
					rErr := executeLongRunningRead(t, readWorkerName, db, bucket, key, readInterval, stopCh)
					if rErr != nil {
						errCh <- rErr
					}
				}()
				time.Sleep(500 * time.Millisecond)

				t.Logf("Perform %d write operations after starting a long running read operation", writeOperationCountInBetween)
				for j := 0; j < writeOperationCountInBetween; j++ {
					err := db.Update(func(tx *bolt.Tx) error {
						_, eerr := executeWrite(tx, bucket, key, writeBytes, 0)
						return eerr
					})

					require.NoError(t, err)
				}
			}

			t.Log("Perform lots of write operations to check whether the long running read operations will read dirty data")
			wg.Add(1)
			go func() {
				defer wg.Done()
				cnt := longRunningReaderCount * writeOperationCountInBetween
				for i := 0; i < cnt; i++ {
					select {
					case <-stopCh:
						return
					default:
					}
					err := db.Update(func(tx *bolt.Tx) error {
						_, eerr := executeWrite(tx, bucket, key, writeBytes, 0)
						return eerr
					})
					require.NoError(t, err)
				}
			}()

			t.Log("Waiting for result")
			select {
			case err := <-errCh:
				close(stopCh)
				t.Errorf("Detected dirty read: %v", err)
			case <-time.After(testDuration):
				close(stopCh)
			}

			wg.Wait()
		})
	}
}

func executeLongRunningRead(t *testing.T, name string, db *bolt.DB, bucket []byte, key []byte, readInterval duration, stopCh chan struct{}) error {
	err := db.View(func(tx *bolt.Tx) error {
		b := tx.Bucket(bucket)

		initialVal := b.Get(key)

		for {
			select {
			case <-stopCh:
				t.Logf("%q finished.", name)
				return nil
			default:
			}

			time.Sleep(randomDurationInRange(readInterval.min, readInterval.max))
			val := b.Get(key)

			if !bytes.Equal(initialVal, val) {
				dirtyReadErr := fmt.Errorf("read different values for the same key (%q), value1: %q, value2: %q",
					string(key), formatBytes(initialVal), formatBytes(val))
				return dirtyReadErr
			}
		}
	})

	return err
}
```

## File: `cursor.go`
```go
package bbolt

import (
	"bytes"
	"fmt"
	"sort"

	"go.etcd.io/bbolt/errors"
	"go.etcd.io/bbolt/internal/common"
)

// Cursor represents an iterator that can traverse over all key/value pairs in a bucket
// in lexicographical order.
// Cursors see nested buckets with value == nil.
// Cursors can be obtained from a transaction and are valid as long as the transaction is open.
//
// Keys and values returned from the cursor are only valid for the life of the transaction.
//
// Changing data while traversing with a cursor may cause it to be invalidated
// and return unexpected keys and/or values. You must reposition your cursor
// after mutating data.
type Cursor struct {
	bucket *Bucket
	stack  []elemRef
}

// Bucket returns the bucket that this cursor was created from.
func (c *Cursor) Bucket() *Bucket {
	return c.bucket
}

// First moves the cursor to the first item in the bucket and returns its key and value.
// If the bucket is empty then a nil key and value are returned.
// The returned key and value are only valid for the life of the transaction.
func (c *Cursor) First() (key []byte, value []byte) {
	common.Assert(c.bucket.tx.db != nil, "tx closed")
	k, v, flags := c.first()
	if (flags & uint32(common.BucketLeafFlag)) != 0 {
		return k, nil
	}
	return k, v
}

func (c *Cursor) first() (key []byte, value []byte, flags uint32) {
	c.stack = c.stack[:0]
	p, n := c.bucket.pageNode(c.bucket.RootPage())
	c.stack = append(c.stack, elemRef{page: p, node: n, index: 0})
	c.goToFirstElementOnTheStack()

	// If we land on an empty page then move to the next value.
	// https://github.com/boltdb/bolt/issues/450
	if c.stack[len(c.stack)-1].count() == 0 {
		c.next()
	}

	k, v, flags := c.keyValue()
	if (flags & uint32(common.BucketLeafFlag)) != 0 {
		return k, nil, flags
	}
	return k, v, flags
}

// Last moves the cursor to the last item in the bucket and returns its key and value.
// If the bucket is empty then a nil key and value are returned.
// The returned key and value are only valid for the life of the transaction.
func (c *Cursor) Last() (key []byte, value []byte) {
	common.Assert(c.bucket.tx.db != nil, "tx closed")
	c.stack = c.stack[:0]
	p, n := c.bucket.pageNode(c.bucket.RootPage())
	ref := elemRef{page: p, node: n}
	ref.index = ref.count() - 1
	c.stack = append(c.stack, ref)
	c.last()

	// If this is an empty page (calling Delete may result in empty pages)
	// we call prev to find the last page that is not empty
	for len(c.stack) > 1 && c.stack[len(c.stack)-1].count() == 0 {
		c.prev()
	}

	if len(c.stack) == 0 {
		return nil, nil
	}

	k, v, flags := c.keyValue()
	if (flags & uint32(common.BucketLeafFlag)) != 0 {
		return k, nil
	}
	return k, v
}

// Next moves the cursor to the next item in the bucket and returns its key and value.
// If the cursor is at the end of the bucket then a nil key and value are returned.
// The returned key and value are only valid for the life of the transaction.
func (c *Cursor) Next() (key []byte, value []byte) {
	common.Assert(c.bucket.tx.db != nil, "tx closed")
	k, v, flags := c.next()
	if (flags & uint32(common.BucketLeafFlag)) != 0 {
		return k, nil
	}
	return k, v
}

// Prev moves the cursor to the previous item in the bucket and returns its key and value.
// If the cursor is at the beginning of the bucket then a nil key and value are returned.
// The returned key and value are only valid for the life of the transaction.
func (c *Cursor) Prev() (key []byte, value []byte) {
	common.Assert(c.bucket.tx.db != nil, "tx closed")
	k, v, flags := c.prev()
	if (flags & uint32(common.BucketLeafFlag)) != 0 {
		return k, nil
	}
	return k, v
}

// Seek moves the cursor to a given key using a b-tree search and returns it.
// If the key does not exist then the next key is used. If no keys
// follow, a nil key is returned.
// The returned key and value are only valid for the life of the transaction.
func (c *Cursor) Seek(seek []byte) (key []byte, value []byte) {
	common.Assert(c.bucket.tx.db != nil, "tx closed")

	k, v, flags := c.seek(seek)

	// If we ended up after the last element of a page then move to the next one.
	if ref := &c.stack[len(c.stack)-1]; ref.index >= ref.count() {
		k, v, flags = c.next()
	}

	if k == nil {
		return nil, nil
	} else if (flags & uint32(common.BucketLeafFlag)) != 0 {
		return k, nil
	}
	return k, v
}

// Delete removes the current key/value under the cursor from the bucket.
// Delete fails if current key/value is a bucket or if the transaction is not writable.
func (c *Cursor) Delete() error {
	if c.bucket.tx.db == nil {
		return errors.ErrTxClosed
	} else if !c.bucket.Writable() {
		return errors.ErrTxNotWritable
	}

	key, _, flags := c.keyValue()
	// Return an error if current value is a bucket.
	if (flags & common.BucketLeafFlag) != 0 {
		return errors.ErrIncompatibleValue
	}
	c.node().del(key)

	return nil
}

// seek moves the cursor to a given key and returns it.
// If the key does not exist then the next key is used.
func (c *Cursor) seek(seek []byte) (key []byte, value []byte, flags uint32) {
	// Start from root page/node and traverse to correct page.
	c.stack = c.stack[:0]
	c.search(seek, c.bucket.RootPage())

	// If this is a bucket then return a nil value.
	return c.keyValue()
}

// first moves the cursor to the first leaf element under the last page in the stack.
func (c *Cursor) goToFirstElementOnTheStack() {
	for {
		// Exit when we hit a leaf page.
		var ref = &c.stack[len(c.stack)-1]
		if ref.isLeaf() {
			break
		}

		// Keep adding pages pointing to the first element to the stack.
		var pgId common.Pgid
		if ref.node != nil {
			pgId = ref.node.inodes[ref.index].Pgid()
		} else {
			pgId = ref.page.BranchPageElement(uint16(ref.index)).Pgid()
		}
		p, n := c.bucket.pageNode(pgId)
		c.stack = append(c.stack, elemRef{page: p, node: n, index: 0})
	}
}

// last moves the cursor to the last leaf element under the last page in the stack.
func (c *Cursor) last() {
	for {
		// Exit when we hit a leaf page.
		ref := &c.stack[len(c.stack)-1]
		if ref.isLeaf() {
			break
		}

		// Keep adding pages pointing to the last element in the stack.
		var pgId common.Pgid
		if ref.node != nil {
			pgId = ref.node.inodes[ref.index].Pgid()
		} else {
			pgId = ref.page.BranchPageElement(uint16(ref.index)).Pgid()
		}
		p, n := c.bucket.pageNode(pgId)

		var nextRef = elemRef{page: p, node: n}
		nextRef.index = nextRef.count() - 1
		c.stack = append(c.stack, nextRef)
	}
}

// next moves to the next leaf element and returns the key and value.
// If the cursor is at the last leaf element then it stays there and returns nil.
func (c *Cursor) next() (key []byte, value []byte, flags uint32) {
	for {
		// Attempt to move over one element until we're successful.
		// Move up the stack as we hit the end of each page in our stack.
		var i int
		for i = len(c.stack) - 1; i >= 0; i-- {
			elem := &c.stack[i]
			if elem.index < elem.count()-1 {
				elem.index++
				break
			}
		}

		// If we've hit the root page then stop and return. This will leave the
		// cursor on the last element of the last page.
		if i == -1 {
			return nil, nil, 0
		}

		// Otherwise start from where we left off in the stack and find the
		// first element of the first leaf page.
		c.stack = c.stack[:i+1]
		c.goToFirstElementOnTheStack()

		// If this is an empty page then restart and move back up the stack.
		// https://github.com/boltdb/bolt/issues/450
		if c.stack[len(c.stack)-1].count() == 0 {
			continue
		}

		return c.keyValue()
	}
}

// prev moves the cursor to the previous item in the bucket and returns its key and value.
// If the cursor is at the beginning of the bucket then a nil key and value are returned.
func (c *Cursor) prev() (key []byte, value []byte, flags uint32) {
	// Attempt to move back one element until we're successful.
	// Move up the stack as we hit the beginning of each page in our stack.
	for i := len(c.stack) - 1; i >= 0; i-- {
		elem := &c.stack[i]
		if elem.index > 0 {
			elem.index--
			break
		}
		// If we've hit the beginning, we should stop moving the cursor,
		// and stay at the first element, so that users can continue to
		// iterate over the elements in reverse direction by calling `Next`.
		// We should return nil in such case.
		// Refer to https://github.com/etcd-io/bbolt/issues/733
		if len(c.stack) == 1 {
			c.first()
			return nil, nil, 0
		}
		c.stack = c.stack[:i]
	}

	// If we've hit the end then return nil.
	if len(c.stack) == 0 {
		return nil, nil, 0
	}

	// Move down the stack to find the last element of the last leaf under this branch.
	c.last()
	return c.keyValue()
}

// search recursively performs a binary search against a given page/node until it finds a given key.
func (c *Cursor) search(key []byte, pgId common.Pgid) {
	p, n := c.bucket.pageNode(pgId)
	if p != nil && !p.IsBranchPage() && !p.IsLeafPage() {
		panic(fmt.Sprintf("invalid page type: %d: %x", p.Id(), p.Flags()))
	}
	e := elemRef{page: p, node: n}
	c.stack = append(c.stack, e)

	// If we're on a leaf page/node then find the specific node.
	if e.isLeaf() {
		c.nsearch(key)
		return
	}

	if n != nil {
		c.searchNode(key, n)
		return
	}
	c.searchPage(key, p)
}

func (c *Cursor) searchNode(key []byte, n *node) {
	var exact bool
	index := sort.Search(len(n.inodes), func(i int) bool {
		// TODO(benbjohnson): Optimize this range search. It's a bit hacky right now.
		// sort.Search() finds the lowest index where f() != -1 but we need the highest index.
		ret := bytes.Compare(n.inodes[i].Key(), key)
		if ret == 0 {
			exact = true
		}
		return ret != -1
	})
	if !exact && index > 0 {
		index--
	}
	c.stack[len(c.stack)-1].index = index

	// Recursively search to the next page.
	c.search(key, n.inodes[index].Pgid())
}

func (c *Cursor) searchPage(key []byte, p *common.Page) {
	// Binary search for the correct range.
	inodes := p.BranchPageElements()

	var exact bool
	index := sort.Search(int(p.Count()), func(i int) bool {
		// TODO(benbjohnson): Optimize this range search. It's a bit hacky right now.
		// sort.Search() finds the lowest index where f() != -1 but we need the highest index.
		ret := bytes.Compare(inodes[i].Key(), key)
		if ret == 0 {
			exact = true
		}
		return ret != -1
	})
	if !exact && index > 0 {
		index--
	}
	c.stack[len(c.stack)-1].index = index

	// Recursively search to the next page.
	c.search(key, inodes[index].Pgid())
}

// nsearch searches the leaf node on the top of the stack for a key.
func (c *Cursor) nsearch(key []byte) {
	e := &c.stack[len(c.stack)-1]
	p, n := e.page, e.node

	// If we have a node then search its inodes.
	if n != nil {
		index := sort.Search(len(n.inodes), func(i int) bool {
			return bytes.Compare(n.inodes[i].Key(), key) != -1
		})
		e.index = index
		return
	}

	// If we have a page then search its leaf elements.
	inodes := p.LeafPageElements()
	index := sort.Search(int(p.Count()), func(i int) bool {
		return bytes.Compare(inodes[i].Key(), key) != -1
	})
	e.index = index
}

// keyValue returns the key and value of the current leaf element.
func (c *Cursor) keyValue() ([]byte, []byte, uint32) {
	ref := &c.stack[len(c.stack)-1]

	// If the cursor is pointing to the end of page/node then return nil.
	if ref.count() == 0 || ref.index >= ref.count() {
		return nil, nil, 0
	}

	// Retrieve value from node.
	if ref.node != nil {
		inode := &ref.node.inodes[ref.index]
		return inode.Key(), inode.Value(), inode.Flags()
	}

	// Or retrieve value from page.
	elem := ref.page.LeafPageElement(uint16(ref.index))
	return elem.Key(), elem.Value(), elem.Flags()
}

// node returns the node that the cursor is currently positioned on.
func (c *Cursor) node() *node {
	common.Assert(len(c.stack) > 0, "accessing a node with a zero-length cursor stack")

	// If the top of the stack is a leaf node then just return it.
	if ref := &c.stack[len(c.stack)-1]; ref.node != nil && ref.isLeaf() {
		return ref.node
	}

	// Start from root and traverse down the hierarchy.
	var n = c.stack[0].node
	if n == nil {
		n = c.bucket.node(c.stack[0].page.Id(), nil)
	}
	for _, ref := range c.stack[:len(c.stack)-1] {
		common.Assert(!n.isLeaf, "expected branch node")
		n = n.childAt(ref.index)
	}
	common.Assert(n.isLeaf, "expected leaf node")
	return n
}

// elemRef represents a reference to an element on a given page/node.
type elemRef struct {
	page  *common.Page
	node  *node
	index int
}

// isLeaf returns whether the ref is pointing at a leaf page/node.
func (r *elemRef) isLeaf() bool {
	if r.node != nil {
		return r.node.isLeaf
	}
	return r.page.IsLeafPage()
}

// count returns the number of inodes or page elements.
func (r *elemRef) count() int {
	if r.node != nil {
		return len(r.node.inodes)
	}
	return int(r.page.Count())
}
```

## File: `cursor_test.go`
```go
package bbolt_test

import (
	"bytes"
	"encoding/binary"
	"fmt"
	"log"
	"os"
	"reflect"
	"sort"
	"testing"
	"testing/quick"

	"github.com/stretchr/testify/require"

	bolt "go.etcd.io/bbolt"
	"go.etcd.io/bbolt/errors"
	"go.etcd.io/bbolt/internal/btesting"
)

// TestCursor_RepeatOperations verifies that a cursor can continue to
// iterate over all elements in reverse direction when it has already
// reached to the end or beginning.
// Refer to https://github.com/etcd-io/bbolt/issues/733
func TestCursor_RepeatOperations(t *testing.T) {
	testCases := []struct {
		name     string
		testFunc func(t2 *testing.T, bucket *bolt.Bucket)
	}{
		{
			name:     "Repeat NextPrevNext",
			testFunc: testRepeatCursorOperations_NextPrevNext,
		},
		{
			name:     "Repeat PrevNextPrev",
			testFunc: testRepeatCursorOperations_PrevNextPrev,
		},
	}

	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			db := btesting.MustCreateDBWithOption(t, &bolt.Options{PageSize: 4096})

			bucketName := []byte("data")

			_ = db.Update(func(tx *bolt.Tx) error {
				b, _ := tx.CreateBucketIfNotExists(bucketName)
				testCursorRepeatOperations_PrepareData(t, b)
				return nil
			})

			_ = db.View(func(tx *bolt.Tx) error {
				b := tx.Bucket(bucketName)
				tc.testFunc(t, b)
				return nil
			})
		})
	}
}

func testCursorRepeatOperations_PrepareData(t *testing.T, b *bolt.Bucket) {
	// ensure we have at least one branch page.
	for i := 0; i < 1000; i++ {
		k := []byte(fmt.Sprintf("%05d", i))
		err := b.Put(k, k)
		require.NoError(t, err)
	}
}

func testRepeatCursorOperations_NextPrevNext(t *testing.T, b *bolt.Bucket) {
	c := b.Cursor()
	c.First()
	startKey := []byte(fmt.Sprintf("%05d", 2))
	returnedKey, _ := c.Seek(startKey)
	require.Equal(t, startKey, returnedKey)

	// Step 1: verify next
	for i := 3; i < 1000; i++ {
		expectedKey := []byte(fmt.Sprintf("%05d", i))
		actualKey, _ := c.Next()
		require.Equal(t, expectedKey, actualKey)
	}

	// Once we've reached the end, it should always return nil no matter how many times we call `Next`.
	for i := 0; i < 10; i++ {
		k, _ := c.Next()
		require.Equal(t, []byte(nil), k)
	}

	// Step 2: verify prev
	for i := 998; i >= 0; i-- {
		expectedKey := []byte(fmt.Sprintf("%05d", i))
		actualKey, _ := c.Prev()
		require.Equal(t, expectedKey, actualKey)
	}

	// Once we've reached the beginning, it should always return nil no matter how many times we call `Prev`.
	for i := 0; i < 10; i++ {
		k, _ := c.Prev()
		require.Equal(t, []byte(nil), k)
	}

	// Step 3: verify next again
	for i := 1; i < 1000; i++ {
		expectedKey := []byte(fmt.Sprintf("%05d", i))
		actualKey, _ := c.Next()
		require.Equal(t, expectedKey, actualKey)
	}
}

func testRepeatCursorOperations_PrevNextPrev(t *testing.T, b *bolt.Bucket) {
	c := b.Cursor()

	startKey := []byte(fmt.Sprintf("%05d", 998))
	returnedKey, _ := c.Seek(startKey)
	require.Equal(t, startKey, returnedKey)

	// Step 1: verify prev
	for i := 997; i >= 0; i-- {
		expectedKey := []byte(fmt.Sprintf("%05d", i))
		actualKey, _ := c.Prev()
		require.Equal(t, expectedKey, actualKey)
	}

	// Once we've reached the beginning, it should always return nil no matter how many times we call `Prev`.
	for i := 0; i < 10; i++ {
		k, _ := c.Prev()
		require.Equal(t, []byte(nil), k)
	}

	// Step 2: verify next
	for i := 1; i < 1000; i++ {
		expectedKey := []byte(fmt.Sprintf("%05d", i))
		actualKey, _ := c.Next()
		require.Equal(t, expectedKey, actualKey)
	}

	// Once we've reached the end, it should always return nil no matter how many times we call `Next`.
	for i := 0; i < 10; i++ {
		k, _ := c.Next()
		require.Equal(t, []byte(nil), k)
	}

	// Step 3: verify prev again
	for i := 998; i >= 0; i-- {
		expectedKey := []byte(fmt.Sprintf("%05d", i))
		actualKey, _ := c.Prev()
		require.Equal(t, expectedKey, actualKey)
	}
}

// Ensure that a cursor can return a reference to the bucket that created it.
func TestCursor_Bucket(t *testing.T) {
	db := btesting.MustCreateDB(t)
	if err := db.Update(func(tx *bolt.Tx) error {
		b, err := tx.CreateBucket([]byte("widgets"))
		if err != nil {
			t.Fatal(err)
		}
		if cb := b.Cursor().Bucket(); !reflect.DeepEqual(cb, b) {
			t.Fatal("cursor bucket mismatch")
		}
		return nil
	}); err != nil {
		t.Fatal(err)
	}
}

// Ensure that a Tx cursor can seek to the appropriate keys.
func TestCursor_Seek(t *testing.T) {
	db := btesting.MustCreateDB(t)
	if err := db.Update(func(tx *bolt.Tx) error {
		b, err := tx.CreateBucket([]byte("widgets"))
		if err != nil {
			t.Fatal(err)
		}
		if err := b.Put([]byte("foo"), []byte("0001")); err != nil {
			t.Fatal(err)
		}
		if err := b.Put([]byte("bar"), []byte("0002")); err != nil {
			t.Fatal(err)
		}
		if err := b.Put([]byte("baz"), []byte("0003")); err != nil {
			t.Fatal(err)
		}

		if _, err := b.CreateBucket([]byte("bkt")); err != nil {
			t.Fatal(err)
		}
		return nil
	}); err != nil {
		t.Fatal(err)
	}

	if err := db.View(func(tx *bolt.Tx) error {
		c := tx.Bucket([]byte("widgets")).Cursor()

		// Exact match should go to the key.
		if k, v := c.Seek([]byte("bar")); !bytes.Equal(k, []byte("bar")) {
			t.Fatalf("unexpected key: %v", k)
		} else if !bytes.Equal(v, []byte("0002")) {
			t.Fatalf("unexpected value: %v", v)
		}

		// Inexact match should go to the next key.
		if k, v := c.Seek([]byte("bas")); !bytes.Equal(k, []byte("baz")) {
			t.Fatalf("unexpected key: %v", k)
		} else if !bytes.Equal(v, []byte("0003")) {
			t.Fatalf("unexpected value: %v", v)
		}

		// Low key should go to the first key.
		if k, v := c.Seek([]byte("")); !bytes.Equal(k, []byte("bar")) {
			t.Fatalf("unexpected key: %v", k)
		} else if !bytes.Equal(v, []byte("0002")) {
			t.Fatalf("unexpected value: %v", v)
		}

		// High key should return no key.
		if k, v := c.Seek([]byte("zzz")); k != nil {
			t.Fatalf("expected nil key: %v", k)
		} else if v != nil {
			t.Fatalf("expected nil value: %v", v)
		}

		// Buckets should return their key but no value.
		if k, v := c.Seek([]byte("bkt")); !bytes.Equal(k, []byte("bkt")) {
			t.Fatalf("unexpected key: %v", k)
		} else if v != nil {
			t.Fatalf("expected nil value: %v", v)
		}

		return nil
	}); err != nil {
		t.Fatal(err)
	}
}

func TestCursor_Delete(t *testing.T) {
	db := btesting.MustCreateDB(t)

	const count = 1000

	// Insert every other key between 0 and $count.
	if err := db.Update(func(tx *bolt.Tx) error {
		b, err := tx.CreateBucket([]byte("widgets"))
		if err != nil {
			t.Fatal(err)
		}
		for i := 0; i < count; i += 1 {
			k := make([]byte, 8)
			binary.BigEndian.PutUint64(k, uint64(i))
			if err := b.Put(k, make([]byte, 100)); err != nil {
				t.Fatal(err)
			}
		}
		if _, err := b.CreateBucket([]byte("sub")); err != nil {
			t.Fatal(err)
		}
		return nil
	}); err != nil {
		t.Fatal(err)
	}

	if err := db.Update(func(tx *bolt.Tx) error {
		c := tx.Bucket([]byte("widgets")).Cursor()
		bound := make([]byte, 8)
		binary.BigEndian.PutUint64(bound, uint64(count/2))
		for key, _ := c.First(); bytes.Compare(key, bound) < 0; key, _ = c.Next() {
			if err := c.Delete(); err != nil {
				t.Fatal(err)
			}
		}

		c.Seek([]byte("sub"))
		if err := c.Delete(); err != errors.ErrIncompatibleValue {
			t.Fatalf("unexpected error: %s", err)
		}

		return nil
	}); err != nil {
		t.Fatal(err)
	}

	if err := db.View(func(tx *bolt.Tx) error {
		stats := tx.Bucket([]byte("widgets")).Stats()
		if stats.KeyN != count/2+1 {
			t.Fatalf("unexpected KeyN: %d", stats.KeyN)
		}
		return nil
	}); err != nil {
		t.Fatal(err)
	}
}

// Ensure that a Tx cursor can seek to the appropriate keys when there are a
// large number of keys. This test also checks that seek will always move
// forward to the next key.
//
// Related: https://github.com/boltdb/bolt/pull/187
func TestCursor_Seek_Large(t *testing.T) {
	db := btesting.MustCreateDB(t)

	var count = 10000

	// Insert every other key between 0 and $count.
	if err := db.Update(func(tx *bolt.Tx) error {
		b, err := tx.CreateBucket([]byte("widgets"))
		if err != nil {
			t.Fatal(err)
		}

		for i := 0; i < count; i += 100 {
			for j := i; j < i+100; j += 2 {
				k := make([]byte, 8)
				binary.BigEndian.PutUint64(k, uint64(j))
				if err := b.Put(k, make([]byte, 100)); err != nil {
					t.Fatal(err)
				}
			}
		}
		return nil
	}); err != nil {
		t.Fatal(err)
	}

	if err := db.View(func(tx *bolt.Tx) error {
		c := tx.Bucket([]byte("widgets")).Cursor()
		for i := 0; i < count; i++ {
			seek := make([]byte, 8)
			binary.BigEndian.PutUint64(seek, uint64(i))

			k, _ := c.Seek(seek)

			// The last seek is beyond the end of the range so
			// it should return nil.
			if i == count-1 {
				if k != nil {
					t.Fatal("expected nil key")
				}
				continue
			}

			// Otherwise we should seek to the exact key or the next key.
			num := binary.BigEndian.Uint64(k)
			if i%2 == 0 {
				if num != uint64(i) {
					t.Fatalf("unexpected num: %d", num)
				}
			} else {
				if num != uint64(i+1) {
					t.Fatalf("unexpected num: %d", num)
				}
			}
		}

		return nil
	}); err != nil {
		t.Fatal(err)
	}
}

// Ensure that a cursor can iterate over an empty bucket without error.
func TestCursor_EmptyBucket(t *testing.T) {
	db := btesting.MustCreateDB(t)
	if err := db.Update(func(tx *bolt.Tx) error {
		_, err := tx.CreateBucket([]byte("widgets"))
		return err
	}); err != nil {
		t.Fatal(err)
	}

	if err := db.View(func(tx *bolt.Tx) error {
		c := tx.Bucket([]byte("widgets")).Cursor()
		k, v := c.First()
		if k != nil {
			t.Fatalf("unexpected key: %v", k)
		} else if v != nil {
			t.Fatalf("unexpected value: %v", v)
		}
		return nil
	}); err != nil {
		t.Fatal(err)
	}
}

// Ensure that a Tx cursor can reverse iterate over an empty bucket without error.
func TestCursor_EmptyBucketReverse(t *testing.T) {
	db := btesting.MustCreateDB(t)

	if err := db.Update(func(tx *bolt.Tx) error {
		_, err := tx.CreateBucket([]byte("widgets"))
		return err
	}); err != nil {
		t.Fatal(err)
	}
	if err := db.View(func(tx *bolt.Tx) error {
		c := tx.Bucket([]byte("widgets")).Cursor()
		k, v := c.Last()
		if k != nil {
			t.Fatalf("unexpected key: %v", k)
		} else if v != nil {
			t.Fatalf("unexpected value: %v", v)
		}
		return nil
	}); err != nil {
		t.Fatal(err)
	}
}

// Ensure that a Tx cursor can iterate over a single root with a couple elements.
func TestCursor_Iterate_Leaf(t *testing.T) {
	db := btesting.MustCreateDB(t)

	if err := db.Update(func(tx *bolt.Tx) error {
		b, err := tx.CreateBucket([]byte("widgets"))
		if err != nil {
			t.Fatal(err)
		}
		if err := b.Put([]byte("baz"), []byte{}); err != nil {
			t.Fatal(err)
		}
		if err := b.Put([]byte("foo"), []byte{0}); err != nil {
			t.Fatal(err)
		}
		if err := b.Put([]byte("bar"), []byte{1}); err != nil {
			t.Fatal(err)
		}
		return nil
	}); err != nil {
		t.Fatal(err)
	}
	tx, err := db.Begin(false)
	if err != nil {
		t.Fatal(err)
	}
	defer func() { _ = tx.Rollback() }()

	c := tx.Bucket([]byte("widgets")).Cursor()

	k, v := c.First()
	if !bytes.Equal(k, []byte("bar")) {
		t.Fatalf("unexpected key: %v", k)
	} else if !bytes.Equal(v, []byte{1}) {
		t.Fatalf("unexpected value: %v", v)
	}

	k, v = c.Next()
	if !bytes.Equal(k, []byte("baz")) {
		t.Fatalf("unexpected key: %v", k)
	} else if !bytes.Equal(v, []byte{}) {
		t.Fatalf("unexpected value: %v", v)
	}

	k, v = c.Next()
	if !bytes.Equal(k, []byte("foo")) {
		t.Fatalf("unexpected key: %v", k)
	} else if !bytes.Equal(v, []byte{0}) {
		t.Fatalf("unexpected value: %v", v)
	}

	k, v = c.Next()
	if k != nil {
		t.Fatalf("expected nil key: %v", k)
	} else if v != nil {
		t.Fatalf("expected nil value: %v", v)
	}

	k, v = c.Next()
	if k != nil {
		t.Fatalf("expected nil key: %v", k)
	} else if v != nil {
		t.Fatalf("expected nil value: %v", v)
	}

	if err := tx.Rollback(); err != nil {
		t.Fatal(err)
	}
}

// Ensure that a Tx cursor can iterate in reverse over a single root with a couple elements.
func TestCursor_LeafRootReverse(t *testing.T) {
	db := btesting.MustCreateDB(t)

	if err := db.Update(func(tx *bolt.Tx) error {
		b, err := tx.CreateBucket([]byte("widgets"))
		if err != nil {
			t.Fatal(err)
		}
		if err := b.Put([]byte("baz"), []byte{}); err != nil {
			t.Fatal(err)
		}
		if err := b.Put([]byte("foo"), []byte{0}); err != nil {
			t.Fatal(err)
		}
		if err := b.Put([]byte("bar"), []byte{1}); err != nil {
			t.Fatal(err)
		}
		return nil
	}); err != nil {
		t.Fatal(err)
	}
	tx, err := db.Begin(false)
	if err != nil {
		t.Fatal(err)
	}
	c := tx.Bucket([]byte("widgets")).Cursor()

	if k, v := c.Last(); !bytes.Equal(k, []byte("foo")) {
		t.Fatalf("unexpected key: %v", k)
	} else if !bytes.Equal(v, []byte{0}) {
		t.Fatalf("unexpected value: %v", v)
	}

	if k, v := c.Prev(); !bytes.Equal(k, []byte("baz")) {
		t.Fatalf("unexpected key: %v", k)
	} else if !bytes.Equal(v, []byte{}) {
		t.Fatalf("unexpected value: %v", v)
	}

	if k, v := c.Prev(); !bytes.Equal(k, []byte("bar")) {
		t.Fatalf("unexpected key: %v", k)
	} else if !bytes.Equal(v, []byte{1}) {
		t.Fatalf("unexpected value: %v", v)
	}

	if k, v := c.Prev(); k != nil {
		t.Fatalf("expected nil key: %v", k)
	} else if v != nil {
		t.Fatalf("expected nil value: %v", v)
	}

	if k, v := c.Prev(); k != nil {
		t.Fatalf("expected nil key: %v", k)
	} else if v != nil {
		t.Fatalf("expected nil value: %v", v)
	}

	if err := tx.Rollback(); err != nil {
		t.Fatal(err)
	}
}

// Ensure that a Tx cursor can restart from the beginning.
func TestCursor_Restart(t *testing.T) {
	db := btesting.MustCreateDB(t)

	if err := db.Update(func(tx *bolt.Tx) error {
		b, err := tx.CreateBucket([]byte("widgets"))
		if err != nil {
			t.Fatal(err)
		}
		if err := b.Put([]byte("bar"), []byte{}); err != nil {
			t.Fatal(err)
		}
		if err := b.Put([]byte("foo"), []byte{}); err != nil {
			t.Fatal(err)
		}
		return nil
	}); err != nil {
		t.Fatal(err)
	}

	tx, err := db.Begin(false)
	if err != nil {
		t.Fatal(err)
	}
	c := tx.Bucket([]byte("widgets")).Cursor()

	if k, _ := c.First(); !bytes.Equal(k, []byte("bar")) {
		t.Fatalf("unexpected key: %v", k)
	}
	if k, _ := c.Next(); !bytes.Equal(k, []byte("foo")) {
		t.Fatalf("unexpected key: %v", k)
	}

	if k, _ := c.First(); !bytes.Equal(k, []byte("bar")) {
		t.Fatalf("unexpected key: %v", k)
	}
	if k, _ := c.Next(); !bytes.Equal(k, []byte("foo")) {
		t.Fatalf("unexpected key: %v", k)
	}

	if err := tx.Rollback(); err != nil {
		t.Fatal(err)
	}
}

// Ensure that a cursor can skip over empty pages that have been deleted.
func TestCursor_First_EmptyPages(t *testing.T) {
	db := btesting.MustCreateDB(t)

	// Create 1000 keys in the "widgets" bucket.
	if err := db.Update(func(tx *bolt.Tx) error {
		b, err := tx.CreateBucket([]byte("widgets"))
		if err != nil {
			t.Fatal(err)
		}

		for i := 0; i < 1000; i++ {
			if err := b.Put(u64tob(uint64(i)), []byte{}); err != nil {
				t.Fatal(err)
			}
		}

		return nil
	}); err != nil {
		t.Fatal(err)
	}

	// Delete half the keys and then try to iterate.
	if err := db.Update(func(tx *bolt.Tx) error {
		b := tx.Bucket([]byte("widgets"))
		for i := 0; i < 600; i++ {
			if err := b.Delete(u64tob(uint64(i))); err != nil {
				t.Fatal(err)
			}
		}

		c := b.Cursor()
		var n int
		for k, _ := c.First(); k != nil; k, _ = c.Next() {
			n++
		}
		if n != 400 {
			t.Fatalf("unexpected key count: %d", n)
		}

		return nil
	}); err != nil {
		t.Fatal(err)
	}
}

// Ensure that a cursor can skip over empty pages that have been deleted.
func TestCursor_Last_EmptyPages(t *testing.T) {
	db := btesting.MustCreateDB(t)

	// Create 1000 keys in the "widgets" bucket.
	if err := db.Update(func(tx *bolt.Tx) error {
		b, err := tx.CreateBucket([]byte("widgets"))
		if err != nil {
			t.Fatal(err)
		}

		for i := 0; i < 1000; i++ {
			if err := b.Put(u64tob(uint64(i)), []byte{}); err != nil {
				t.Fatal(err)
			}
		}

		return nil
	}); err != nil {
		t.Fatal(err)
	}

	// Delete last 800 elements to ensure last page is empty
	if err := db.Update(func(tx *bolt.Tx) error {
		b := tx.Bucket([]byte("widgets"))
		for i := 200; i < 1000; i++ {
			if err := b.Delete(u64tob(uint64(i))); err != nil {
				t.Fatal(err)
			}
		}

		c := b.Cursor()
		var n int
		for k, _ := c.Last(); k != nil; k, _ = c.Prev() {
			n++
		}
		if n != 200 {
			t.Fatalf("unexpected key count: %d", n)
		}

		return nil
	}); err != nil {
		t.Fatal(err)
	}
}

// Ensure that a Tx can iterate over all elements in a bucket.
func TestCursor_QuickCheck(t *testing.T) {
	f := func(items testdata) bool {
		db := btesting.MustCreateDB(t)
		defer db.MustClose()

		// Bulk insert all values.
		tx, err := db.Begin(true)
		if err != nil {
			t.Fatal(err)
		}
		b, err := tx.CreateBucket([]byte("widgets"))
		if err != nil {
			t.Fatal(err)
		}
		for _, item := range items {
			if err := b.Put(item.Key, item.Value); err != nil {
				t.Fatal(err)
			}
		}
		if err := tx.Commit(); err != nil {
			t.Fatal(err)
		}

		// Sort test data.
		sort.Sort(items)

		// Iterate over all items and check consistency.
		var index = 0
		tx, err = db.Begin(false)
		if err != nil {
			t.Fatal(err)
		}

		c := tx.Bucket([]byte("widgets")).Cursor()
		for k, v := c.First(); k != nil && index < len(items); k, v = c.Next() {
			if !bytes.Equal(k, items[index].Key) {
				t.Fatalf("unexpected key: %v", k)
			} else if !bytes.Equal(v, items[index].Value) {
				t.Fatalf("unexpected value: %v", v)
			}
			index++
		}
		if len(items) != index {
			t.Fatalf("unexpected item count: %v, expected %v", len(items), index)
		}

		if err := tx.Rollback(); err != nil {
			t.Fatal(err)
		}

		return true
	}
	if err := quick.Check(f, qconfig()); err != nil {
		t.Error(err)
	}
}

// Ensure that a transaction can iterate over all elements in a bucket in reverse.
func TestCursor_QuickCheck_Reverse(t *testing.T) {
	f := func(items testdata) bool {
		db := btesting.MustCreateDB(t)
		defer db.MustClose()

		// Bulk insert all values.
		tx, err := db.Begin(true)
		if err != nil {
			t.Fatal(err)
		}
		b, err := tx.CreateBucket([]byte("widgets"))
		if err != nil {
			t.Fatal(err)
		}
		for _, item := range items {
			if err := b.Put(item.Key, item.Value); err != nil {
				t.Fatal(err)
			}
		}
		if err := tx.Commit(); err != nil {
			t.Fatal(err)
		}

		// Sort test data.
		sort.Sort(revtestdata(items))

		// Iterate over all items and check consistency.
		var index = 0
		tx, err = db.Begin(false)
		if err != nil {
			t.Fatal(err)
		}
		c := tx.Bucket([]byte("widgets")).Cursor()
		for k, v := c.Last(); k != nil && index < len(items); k, v = c.Prev() {
			if !bytes.Equal(k, items[index].Key) {
				t.Fatalf("unexpected key: %v", k)
			} else if !bytes.Equal(v, items[index].Value) {
				t.Fatalf("unexpected value: %v", v)
			}
			index++
		}
		if len(items) != index {
			t.Fatalf("unexpected item count: %v, expected %v", len(items), index)
		}

		if err := tx.Rollback(); err != nil {
			t.Fatal(err)
		}

		return true
	}
	if err := quick.Check(f, qconfig()); err != nil {
		t.Error(err)
	}
}

// Ensure that a Tx cursor can iterate over subbuckets.
func TestCursor_QuickCheck_BucketsOnly(t *testing.T) {
	db := btesting.MustCreateDB(t)

	if err := db.Update(func(tx *bolt.Tx) error {
		b, err := tx.CreateBucket([]byte("widgets"))
		if err != nil {
			t.Fatal(err)
		}
		if _, err := b.CreateBucket([]byte("foo")); err != nil {
			t.Fatal(err)
		}
		if _, err := b.CreateBucket([]byte("bar")); err != nil {
			t.Fatal(err)
		}
		if _, err := b.CreateBucket([]byte("baz")); err != nil {
			t.Fatal(err)
		}
		return nil
	}); err != nil {
		t.Fatal(err)
	}

	if err := db.View(func(tx *bolt.Tx) error {
		var names []string
		c := tx.Bucket([]byte("widgets")).Cursor()
		for k, v := c.First(); k != nil; k, v = c.Next() {
			names = append(names, string(k))
			if v != nil {
				t.Fatalf("unexpected value: %v", v)
			}
		}
		if !reflect.DeepEqual(names, []string{"bar", "baz", "foo"}) {
			t.Fatalf("unexpected names: %+v", names)
		}
		return nil
	}); err != nil {
		t.Fatal(err)
	}
}

// Ensure that a Tx cursor can reverse iterate over subbuckets.
func TestCursor_QuickCheck_BucketsOnly_Reverse(t *testing.T) {
	db := btesting.MustCreateDB(t)

	if err := db.Update(func(tx *bolt.Tx) error {
		b, err := tx.CreateBucket([]byte("widgets"))
		if err != nil {
			t.Fatal(err)
		}
		if _, err := b.CreateBucket([]byte("foo")); err != nil {
			t.Fatal(err)
		}
		if _, err := b.CreateBucket([]byte("bar")); err != nil {
			t.Fatal(err)
		}
		if _, err := b.CreateBucket([]byte("baz")); err != nil {
			t.Fatal(err)
		}
		return nil
	}); err != nil {
		t.Fatal(err)
	}

	if err := db.View(func(tx *bolt.Tx) error {
		var names []string
		c := tx.Bucket([]byte("widgets")).Cursor()
		for k, v := c.Last(); k != nil; k, v = c.Prev() {
			names = append(names, string(k))
			if v != nil {
				t.Fatalf("unexpected value: %v", v)
			}
		}
		if !reflect.DeepEqual(names, []string{"foo", "baz", "bar"}) {
			t.Fatalf("unexpected names: %+v", names)
		}
		return nil
	}); err != nil {
		t.Fatal(err)
	}
}

func ExampleCursor() {
	// Open the database.
	db, err := bolt.Open(tempfile(), 0600, nil)
	if err != nil {
		log.Fatal(err)
	}
	defer os.Remove(db.Path())

	// Start a read-write transaction.
	if err := db.Update(func(tx *bolt.Tx) error {
		// Create a new bucket.
		b, err := tx.CreateBucket([]byte("animals"))
		if err != nil {
			return err
		}

		// Insert data into a bucket.
		if err := b.Put([]byte("dog"), []byte("fun")); err != nil {
			log.Fatal(err)
		}
		if err := b.Put([]byte("cat"), []byte("lame")); err != nil {
			log.Fatal(err)
		}
		if err := b.Put([]byte("liger"), []byte("awesome")); err != nil {
			log.Fatal(err)
		}

		// Create a cursor for iteration.
		c := b.Cursor()

		// Iterate over items in sorted key order. This starts from the
		// first key/value pair and updates the k/v variables to the
		// next key/value on each iteration.
		//
		// The loop finishes at the end of the cursor when a nil key is returned.
		for k, v := c.First(); k != nil; k, v = c.Next() {
			fmt.Printf("A %s is %s.\n", k, v)
		}

		return nil
	}); err != nil {
		log.Fatal(err)
	}

	if err := db.Close(); err != nil {
		log.Fatal(err)
	}

	// Output:
	// A cat is lame.
	// A dog is fun.
	// A liger is awesome.
}

func ExampleCursor_reverse() {
	// Open the database.
	db, err := bolt.Open(tempfile(), 0600, nil)
	if err != nil {
		log.Fatal(err)
	}
	defer os.Remove(db.Path())

	// Start a read-write transaction.
	if err := db.Update(func(tx *bolt.Tx) error {
		// Create a new bucket.
		b, err := tx.CreateBucket([]byte("animals"))
		if err != nil {
			return err
		}

		// Insert data into a bucket.
		if err := b.Put([]byte("dog"), []byte("fun")); err != nil {
			log.Fatal(err)
		}
		if err := b.Put([]byte("cat"), []byte("lame")); err != nil {
			log.Fatal(err)
		}
		if err := b.Put([]byte("liger"), []byte("awesome")); err != nil {
			log.Fatal(err)
		}

		// Create a cursor for iteration.
		c := b.Cursor()

		// Iterate over items in reverse sorted key order. This starts
		// from the last key/value pair and updates the k/v variables to
		// the previous key/value on each iteration.
		//
		// The loop finishes at the beginning of the cursor when a nil key
		// is returned.
		for k, v := c.Last(); k != nil; k, v = c.Prev() {
			fmt.Printf("A %s is %s.\n", k, v)
		}

		return nil
	}); err != nil {
		log.Fatal(err)
	}

	// Close the database to release the file lock.
	if err := db.Close(); err != nil {
		log.Fatal(err)
	}

	// Output:
	// A liger is awesome.
	// A dog is fun.
	// A cat is lame.
}
```

## File: `db.go`
```go
package bbolt

import (
	"errors"
	"fmt"
	"io"
	"os"
	"runtime"
	"sync"
	"time"
	"unsafe"

	berrors "go.etcd.io/bbolt/errors"
	"go.etcd.io/bbolt/internal/common"
	fl "go.etcd.io/bbolt/internal/freelist"
)

// The time elapsed between consecutive file locking attempts.
const flockRetryTimeout = 50 * time.Millisecond

// FreelistType is the type of the freelist backend
type FreelistType string

// TODO(ahrtr): eventually we should (step by step)
//  1. default to `FreelistMapType`;
//  2. remove the `FreelistArrayType`, do not export `FreelistMapType`
//     and remove field `FreelistType' from both `DB` and `Options`;
const (
	// FreelistArrayType indicates backend freelist type is array
	FreelistArrayType = FreelistType("array")
	// FreelistMapType indicates backend freelist type is hashmap
	FreelistMapType = FreelistType("hashmap")
)

// DB represents a collection of buckets persisted to a file on disk.
// All data access is performed through transactions which can be obtained through the DB.
// All the functions on DB will return a ErrDatabaseNotOpen if accessed before Open() is called.
type DB struct {
	// When enabled, the database will perform a Check() after every commit.
	// A panic is issued if the database is in an inconsistent state. This
	// flag has a large performance impact so it should only be used for
	// debugging purposes.
	StrictMode bool

	// Setting the NoSync flag will cause the database to skip fsync()
	// calls after each commit. This can be useful when bulk loading data
	// into a database and you can restart the bulk load in the event of
	// a system failure or database corruption. Do not set this flag for
	// normal use.
	//
	// If the package global IgnoreNoSync constant is true, this value is
	// ignored.  See the comment on that constant for more details.
	//
	// THIS IS UNSAFE. PLEASE USE WITH CAUTION.
	NoSync bool

	// When true, skips syncing freelist to disk. This improves the database
	// write performance under normal operation, but requires a full database
	// re-sync during recovery.
	NoFreelistSync bool

	// FreelistType sets the backend freelist type. There are two options. Array which is simple but endures
	// dramatic performance degradation if database is large and fragmentation in freelist is common.
	// The alternative one is using hashmap, it is faster in almost all circumstances
	// but it doesn't guarantee that it offers the smallest page id available. In normal case it is safe.
	// The default type is array
	FreelistType FreelistType

	// When true, skips the truncate call when growing the database.
	// Setting this to true is only safe on non-ext3/ext4 systems.
	// Skipping truncation avoids preallocation of hard drive space and
	// bypasses a truncate() and fsync() syscall on remapping.
	//
	// https://github.com/boltdb/bolt/issues/284
	NoGrowSync bool

	// When `true`, bbolt will always load the free pages when opening the DB.
	// When opening db in write mode, this flag will always automatically
	// set to `true`.
	PreLoadFreelist bool

	// If you want to read the entire database fast, you can set MmapFlag to
	// syscall.MAP_POPULATE on Linux 2.6.23+ for sequential read-ahead.
	MmapFlags int

	// MaxBatchSize is the maximum size of a batch. Default value is
	// copied from DefaultMaxBatchSize in Open.
	//
	// If <=0, disables batching.
	//
	// Do not change concurrently with calls to Batch.
	MaxBatchSize int

	// MaxBatchDelay is the maximum delay before a batch starts.
	// Default value is copied from DefaultMaxBatchDelay in Open.
	//
	// If <=0, effectively disables batching.
	//
	// Do not change concurrently with calls to Batch.
	MaxBatchDelay time.Duration

	// AllocSize is the amount of space allocated when the database
	// needs to create new pages. This is done to amortize the cost
	// of truncate() and fsync() when growing the data file.
	AllocSize int

	// MaxSize is the maximum size (in bytes) allowed for the data file.
	// If a caller's attempt to add data results in the need to grow
	// the data file, an error will be returned and the data file will not grow.
	// <=0 means no limit.
	MaxSize int

	// Mlock locks database file in memory when set to true.
	// It prevents major page faults, however used memory can't be reclaimed.
	//
	// Supported only on Unix via mlock/munlock syscalls.
	Mlock bool

	logger Logger

	path     string
	openFile func(string, int, os.FileMode) (*os.File, error)
	file     *os.File
	// `dataref` isn't used at all on Windows, and the golangci-lint
	// always fails on Windows platform.
	//nolint
	dataref  []byte // mmap'ed readonly, write throws SEGV
	data     *[common.MaxMapSize]byte
	datasz   int
	meta0    *common.Meta
	meta1    *common.Meta
	pageSize int
	opened   bool
	rwtx     *Tx
	stats    *Stats

	freelist     fl.Interface
	freelistLoad sync.Once

	pagePool sync.Pool

	batchMu sync.Mutex
	batch   *batch

	rwlock   sync.Mutex   // Allows only one writer at a time.
	metalock sync.Mutex   // Protects meta page access.
	mmaplock sync.RWMutex // Protects mmap access during remapping.
	statlock sync.RWMutex // Protects stats access.

	ops struct {
		writeAt func(b []byte, off int64) (n int, err error)
	}

	// Read only mode.
	// When true, Update() and Begin(true) return ErrDatabaseReadOnly immediately.
	readOnly bool
}

// Path returns the path to currently open database file.
func (db *DB) Path() string {
	return db.path
}

// GoString returns the Go string representation of the database.
func (db *DB) GoString() string {
	return fmt.Sprintf("bolt.DB{path:%q}", db.path)
}

// String returns the string representation of the database.
func (db *DB) String() string {
	return fmt.Sprintf("DB<%q>", db.path)
}

// Open creates and opens a database at the given path with a given file mode.
// If the file does not exist then it will be created automatically with a given file mode.
// Passing in nil options will cause Bolt to open the database with the default options.
// Note: For read/write transactions, ensure the owner has write permission on the created/opened database file, e.g. 0600
func Open(path string, mode os.FileMode, options *Options) (db *DB, err error) {
	db = &DB{
		opened: true,
	}

	// Set default options if no options are provided.
	if options == nil {
		options = DefaultOptions
	}
	db.NoSync = options.NoSync
	db.NoGrowSync = options.NoGrowSync
	db.MmapFlags = options.MmapFlags
	db.NoFreelistSync = options.NoFreelistSync
	db.PreLoadFreelist = options.PreLoadFreelist
	db.FreelistType = options.FreelistType
	db.Mlock = options.Mlock
	db.MaxSize = options.MaxSize

	// Set default values for later DB operations.
	db.MaxBatchSize = common.DefaultMaxBatchSize
	db.MaxBatchDelay = common.DefaultMaxBatchDelay
	db.AllocSize = common.DefaultAllocSize

	if !options.NoStatistics {
		db.stats = new(Stats)
	}

	if options.Logger == nil {
		db.logger = getDiscardLogger()
	} else {
		db.logger = options.Logger
	}

	lg := db.Logger()
	if lg != discardLogger {
		lg.Infof("Opening db file (%s) with mode %s and with options: %s", path, mode, options)
		defer func() {
			if err != nil {
				lg.Errorf("Opening bbolt db (%s) failed: %v", path, err)
			} else {
				lg.Infof("Opening bbolt db (%s) successfully", path)
			}
		}()
	}

	flag := os.O_RDWR
	if options.ReadOnly {
		flag = os.O_RDONLY
		db.readOnly = true
	} else {
		// always load free pages in write mode
		db.PreLoadFreelist = true
		flag |= os.O_CREATE
	}

	db.openFile = options.OpenFile
	if db.openFile == nil {
		db.openFile = os.OpenFile
	}

	// Open data file and separate sync handler for metadata writes.
	if db.file, err = db.openFile(path, flag, mode); err != nil {
		_ = db.close()
		lg.Errorf("failed to open db file (%s): %v", path, err)
		return nil, err
	}
	db.path = db.file.Name()

	// Lock file so that other processes using Bolt in read-write mode cannot
	// use the database  at the same time. This would cause corruption since
	// the two processes would write meta pages and free pages separately.
	// The database file is locked exclusively (only one process can grab the lock)
	// if !options.ReadOnly.
	// The database file is locked using the shared lock (more than one process may
	// hold a lock at the same time) otherwise (options.ReadOnly is set).
	if err = flock(db, !db.readOnly, options.Timeout); err != nil {
		_ = db.close()
		lg.Errorf("failed to lock db file (%s), readonly: %t, error: %v", path, db.readOnly, err)
		return nil, err
	}

	// Default values for test hooks
	db.ops.writeAt = db.file.WriteAt

	if db.pageSize = options.PageSize; db.pageSize == 0 {
		// Set the default page size to the OS page size.
		db.pageSize = common.DefaultPageSize
	}

	// Initialize the database if it doesn't exist.
	if info, statErr := db.file.Stat(); statErr != nil {
		_ = db.close()
		lg.Errorf("failed to get db file's stats (%s): %v", path, err)
		return nil, statErr
	} else if info.Size() == 0 {
		// Initialize new files with meta pages.
		if err = db.init(); err != nil {
			// clean up file descriptor on initialization fail
			_ = db.close()
			lg.Errorf("failed to initialize db file (%s): %v", path, err)
			return nil, err
		}
	} else {
		// try to get the page size from the metadata pages
		if db.pageSize, err = db.getPageSize(); err != nil {
			_ = db.close()
			lg.Errorf("failed to get page size from db file (%s): %v", path, err)
			return nil, err
		}
	}

	// Initialize page pool.
	db.pagePool = sync.Pool{
		New: func() interface{} {
			return make([]byte, db.pageSize)
		},
	}

	// Memory map the data file.
	if err = db.mmap(options.InitialMmapSize); err != nil {
		_ = db.close()
		lg.Errorf("failed to map db file (%s): %v", path, err)
		return nil, err
	}

	if db.PreLoadFreelist {
		db.loadFreelist()
	}

	if db.readOnly {
		return db, nil
	}

	// Flush freelist when transitioning from no sync to sync so
	// NoFreelistSync unaware boltdb can open the db later.
	if !db.NoFreelistSync && !db.hasSyncedFreelist() {
		tx, txErr := db.Begin(true)
		if tx != nil {
			txErr = tx.Commit()
		}
		if txErr != nil {
			lg.Errorf("starting readwrite transaction failed: %v", txErr)
			_ = db.close()
			return nil, txErr
		}
	}

	// Mark the database as opened and return.
	return db, nil
}

// getPageSize reads the pageSize from the meta pages. It tries
// to read the first meta page firstly. If the first page is invalid,
// then it tries to read the second page using the default page size.
func (db *DB) getPageSize() (int, error) {
	var (
		meta0CanRead, meta1CanRead bool
	)

	// Read the first meta page to determine the page size.
	if pgSize, canRead, err := db.getPageSizeFromFirstMeta(); err != nil {
		// We cannot read the page size from page 0, but can read page 0.
		meta0CanRead = canRead
	} else {
		return pgSize, nil
	}

	// Read the second meta page to determine the page size.
	if pgSize, canRead, err := db.getPageSizeFromSecondMeta(); err != nil {
		// We cannot read the page size from page 1, but can read page 1.
		meta1CanRead = canRead
	} else {
		return pgSize, nil
	}

	// If we can't read the page size from both pages, but can read
	// either page, then we assume it's the same as the OS or the one
	// given, since that's how the page size was chosen in the first place.
	//
	// If both pages are invalid, and (this OS uses a different page size
	// from what the database was created with or the given page size is
	// different from what the database was created with), then we are out
	// of luck and cannot access the database.
	if meta0CanRead || meta1CanRead {
		return db.pageSize, nil
	}

	return 0, berrors.ErrInvalid
}

// getPageSizeFromFirstMeta reads the pageSize from the first meta page
func (db *DB) getPageSizeFromFirstMeta() (int, bool, error) {
	var buf [0x1000]byte
	var metaCanRead bool
	if bw, err := db.file.ReadAt(buf[:], 0); err == nil && bw == len(buf) {
		metaCanRead = true
		if m := db.pageInBuffer(buf[:], 0).Meta(); m.Validate() == nil {
			return int(m.PageSize()), metaCanRead, nil
		}
	}
	return 0, metaCanRead, berrors.ErrInvalid
}

// getPageSizeFromSecondMeta reads the pageSize from the second meta page
func (db *DB) getPageSizeFromSecondMeta() (int, bool, error) {
	var (
		fileSize    int64
		metaCanRead bool
	)

	// get the db file size
	if info, err := db.file.Stat(); err != nil {
		return 0, metaCanRead, err
	} else {
		fileSize = info.Size()
	}

	// We need to read the second meta page, so we should skip the first page;
	// but we don't know the exact page size yet, it's chicken & egg problem.
	// The solution is to try all the possible page sizes, which starts from 1KB
	// and until 16MB (1024<<14) or the end of the db file
	//
	// TODO: should we support larger page size?
	for i := 0; i <= 14; i++ {
		var buf [0x1000]byte
		var pos int64 = 1024 << uint(i)
		if pos >= fileSize-1024 {
			break
		}
		bw, err := db.file.ReadAt(buf[:], pos)
		if (err == nil && bw == len(buf)) || (err == io.EOF && int64(bw) == (fileSize-pos)) {
			metaCanRead = true
			if m := db.pageInBuffer(buf[:], 0).Meta(); m.Validate() == nil {
				return int(m.PageSize()), metaCanRead, nil
			}
		}
	}

	return 0, metaCanRead, berrors.ErrInvalid
}

// loadFreelist reads the freelist if it is synced, or reconstructs it
// by scanning the DB if it is not synced. It assumes there are no
// concurrent accesses being made to the freelist.
func (db *DB) loadFreelist() {
	db.freelistLoad.Do(func() {
		db.freelist = newFreelist(db.FreelistType)
		if !db.hasSyncedFreelist() {
			// Reconstruct free list by scanning the DB.
			db.freelist.Init(db.freepages())
		} else {
			// Read free list from freelist page.
			db.freelist.Read(db.page(db.meta().Freelist()))
		}
		if db.stats != nil {
			db.stats.FreePageN = db.freelist.FreeCount()
		}
	})
}

func (db *DB) hasSyncedFreelist() bool {
	return db.meta().Freelist() != common.PgidNoFreelist
}

func (db *DB) fileSize() (int, error) {
	info, err := db.file.Stat()
	if err != nil {
		return 0, fmt.Errorf("file stat error: %w", err)
	}
	sz := int(info.Size())
	if sz < db.pageSize*2 {
		return 0, fmt.Errorf("file size too small %d", sz)
	}
	return sz, nil
}

// mmap opens the underlying memory-mapped file and initializes the meta references.
// minsz is the minimum size that the new mmap can be.
func (db *DB) mmap(minsz int) (err error) {
	db.mmaplock.Lock()
	defer db.mmaplock.Unlock()

	lg := db.Logger()

	// Ensure the size is at least the minimum size.
	var fileSize int
	fileSize, err = db.fileSize()
	if err != nil {
		lg.Errorf("getting file size failed: %w", err)
		return err
	}
	var size = fileSize
	if size < minsz {
		size = minsz
	}
	size, err = db.mmapSize(size)
	if err != nil {
		lg.Errorf("getting map size failed: %w", err)
		return err
	}

	if db.Mlock {
		// Unlock db memory
		if err := db.munlock(fileSize); err != nil {
			return err
		}
	}

	// Dereference all mmap references before unmapping.
	if db.rwtx != nil {
		db.rwtx.root.dereference()
	}

	// Unmap existing data before continuing.
	if err = db.munmap(); err != nil {
		return err
	}

	// Memory-map the data file as a byte slice.
	// gofail: var mapError string
	// return errors.New(mapError)
	if err = mmap(db, size); err != nil {
		lg.Errorf("[GOOS: %s, GOARCH: %s] mmap failed, size: %d, error: %v", runtime.GOOS, runtime.GOARCH, size, err)
		return err
	}

	// Perform unmmap on any error to reset all data fields:
	// dataref, data, datasz, meta0 and meta1.
	defer func() {
		if err != nil {
			if unmapErr := db.munmap(); unmapErr != nil {
				err = fmt.Errorf("%w; rollback unmap also failed: %v", err, unmapErr)
			}
		}
	}()

	if db.Mlock {
		// Don't allow swapping of data file
		if err := db.mlock(fileSize); err != nil {
			return err
		}
	}

	// Save references to the meta pages.
	db.meta0 = db.page(0).Meta()
	db.meta1 = db.page(1).Meta()

	// Validate the meta pages. We only return an error if both meta pages fail
	// validation, since meta0 failing validation means that it wasn't saved
	// properly -- but we can recover using meta1. And vice-versa.
	err0 := db.meta0.Validate()
	err1 := db.meta1.Validate()
	if err0 != nil && err1 != nil {
		lg.Errorf("both meta pages are invalid, meta0: %v, meta1: %v", err0, err1)
		return err0
	}

	return nil
}

func (db *DB) invalidate() {
	db.dataref = nil
	db.data = nil
	db.datasz = 0

	db.meta0 = nil
	db.meta1 = nil
}

// munmap unmaps the data file from memory.
func (db *DB) munmap() error {
	defer db.invalidate()

	// gofail: var unmapError string
	// return errors.New(unmapError)
	if err := munmap(db); err != nil {
		db.Logger().Errorf("[GOOS: %s, GOARCH: %s] munmap failed, db.datasz: %d, error: %v", runtime.GOOS, runtime.GOARCH, db.datasz, err)
		return fmt.Errorf("unmap error: %w", err)
	}

	return nil
}

// mmapSize determines the appropriate size for the mmap given the current size
// of the database. The minimum size is 32KB and doubles until it reaches 1GB.
// Returns an error if the new mmap size is greater than the max allowed.
func (db *DB) mmapSize(size int) (int, error) {
	// Double the size from 32KB until 1GB.
	for i := uint(15); i <= 30; i++ {
		if size <= 1<<i {
			return 1 << i, nil
		}
	}

	// Verify the requested size is not above the maximum allowed.
	if size > common.MaxMapSize {
		return 0, errors.New("mmap too large")
	}

	// If larger than 1GB then grow by 1GB at a time.
	sz := int64(size)
	if remainder := sz % int64(common.MaxMmapStep); remainder > 0 {
		sz += int64(common.MaxMmapStep) - remainder
	}

	// Ensure that the mmap size is a multiple of the page size.
	// This should always be true since we're incrementing in MBs.
	pageSize := int64(db.pageSize)
	if (sz % pageSize) != 0 {
		sz = ((sz / pageSize) + 1) * pageSize
	}

	// If we've exceeded the max size then only grow up to the max size.
	if sz > common.MaxMapSize {
		sz = common.MaxMapSize
	}

	return int(sz), nil
}

func (db *DB) munlock(fileSize int) error {
	// gofail: var munlockError string
	// return errors.New(munlockError)
	if err := munlock(db, fileSize); err != nil {
		db.Logger().Errorf("[GOOS: %s, GOARCH: %s] munlock failed, fileSize: %d, db.datasz: %d, error: %v", runtime.GOOS, runtime.GOARCH, fileSize, db.datasz, err)
		return fmt.Errorf("munlock error: %w", err)
	}
	return nil
}

func (db *DB) mlock(fileSize int) error {
	// gofail: var mlockError string
	// return errors.New(mlockError)
	if err := mlock(db, fileSize); err != nil {
		db.Logger().Errorf("[GOOS: %s, GOARCH: %s] mlock failed, fileSize: %d, db.datasz: %d, error: %v", runtime.GOOS, runtime.GOARCH, fileSize, db.datasz, err)
		return fmt.Errorf("mlock error: %w", err)
	}
	return nil
}

func (db *DB) mrelock(fileSizeFrom, fileSizeTo int) error {
	if err := db.munlock(fileSizeFrom); err != nil {
		return err
	}
	if err := db.mlock(fileSizeTo); err != nil {
		return err
	}
	return nil
}

// init creates a new database file and initializes its meta pages.
func (db *DB) init() error {
	// Create two meta pages on a buffer.
	buf := make([]byte, db.pageSize*4)
	for i := 0; i < 2; i++ {
		p := db.pageInBuffer(buf, common.Pgid(i))
		p.SetId(common.Pgid(i))
		p.SetFlags(common.MetaPageFlag)

		// Initialize the meta page.
		m := p.Meta()
		m.SetMagic(common.Magic)
		m.SetVersion(common.Version)
		m.SetPageSize(uint32(db.pageSize))
		m.SetFreelist(2)
		m.SetRootBucket(common.NewInBucket(3, 0))
		m.SetPgid(4)
		m.SetTxid(common.Txid(i))
		m.SetChecksum(m.Sum64())
	}

	// Write an empty freelist at page 3.
	p := db.pageInBuffer(buf, common.Pgid(2))
	p.SetId(2)
	p.SetFlags(common.FreelistPageFlag)
	p.SetCount(0)

	// Write an empty leaf page at page 4.
	p = db.pageInBuffer(buf, common.Pgid(3))
	p.SetId(3)
	p.SetFlags(common.LeafPageFlag)
	p.SetCount(0)

	// Write the buffer to our data file.
	if _, err := db.ops.writeAt(buf, 0); err != nil {
		db.Logger().Errorf("writeAt failed: %w", err)
		return err
	}
	if err := fdatasync(db); err != nil {
		db.Logger().Errorf("[GOOS: %s, GOARCH: %s] fdatasync failed: %w", runtime.GOOS, runtime.GOARCH, err)
		return err
	}

	return nil
}

// Close releases all database resources.
// It will block waiting for any open transactions to finish
// before closing the database and returning.
func (db *DB) Close() error {
	db.rwlock.Lock()
	defer db.rwlock.Unlock()

	db.metalock.Lock()
	defer db.metalock.Unlock()

	db.mmaplock.Lock()
	defer db.mmaplock.Unlock()

	return db.close()
}

func (db *DB) close() error {
	if !db.opened {
		return nil
	}

	db.opened = false

	db.freelist = nil

	// Clear ops.
	db.ops.writeAt = nil

	var errs []error
	// Close the mmap.
	if err := db.munmap(); err != nil {
		errs = append(errs, err)
	}

	// Close file handles.
	if db.file != nil {
		// No need to unlock read-only file.
		if !db.readOnly {
			// Unlock the file.
			if err := funlock(db); err != nil {
				errs = append(errs, fmt.Errorf("bolt.Close(): funlock error: %w", err))
			}
		}

		// Close the file descriptor.
		if err := db.file.Close(); err != nil {
			errs = append(errs, fmt.Errorf("db file close: %w", err))
		}
		db.file = nil
	}

	db.path = ""

	if len(errs) > 0 {
		return errs[0]
	}
	return nil
}

// Begin starts a new transaction.
// Multiple read-only transactions can be used concurrently but only one
// write transaction can be used at a time. Starting multiple write transactions
// will cause the calls to block and be serialized until the current write
// transaction finishes.
//
// Transactions should not be dependent on one another. Opening a read
// transaction and a write transaction in the same goroutine can cause the
// writer to deadlock because the database periodically needs to re-mmap itself
// as it grows and it cannot do that while a read transaction is open.
//
// If a long running read transaction (for example, a snapshot transaction) is
// needed, you might want to set DB.InitialMmapSize to a large enough value
// to avoid potential blocking of write transaction.
//
// IMPORTANT: You must close read-only transactions after you are finished or
// else the database will not reclaim old pages.
func (db *DB) Begin(writable bool) (t *Tx, err error) {
	if lg := db.Logger(); lg != discardLogger {
		lg.Debugf("Starting a new transaction [writable: %t]", writable)
		defer func() {
			if err != nil {
				lg.Errorf("Starting a new transaction [writable: %t] failed: %v", writable, err)
			} else {
				lg.Debugf("Starting a new transaction [writable: %t] successfully", writable)
			}
		}()
	}

	if writable {
		return db.beginRWTx()
	}
	return db.beginTx()
}

func (db *DB) Logger() Logger {
	if db == nil || db.logger == nil {
		return getDiscardLogger()
	}
	return db.logger
}

func (db *DB) beginTx() (*Tx, error) {
	// Lock the meta pages while we initialize the transaction. We obtain
	// the meta lock before the mmap lock because that's the order that the
	// write transaction will obtain them.
	db.metalock.Lock()

	// Obtain a read-only lock on the mmap. When the mmap is remapped it will
	// obtain a write lock so all transactions must finish before it can be
	// remapped.
	db.mmaplock.RLock()

	// Exit if the database is not open yet.
	if !db.opened {
		db.mmaplock.RUnlock()
		db.metalock.Unlock()
		return nil, berrors.ErrDatabaseNotOpen
	}

	// Exit if the database is not correctly mapped.
	if db.data == nil {
		db.mmaplock.RUnlock()
		db.metalock.Unlock()
		return nil, berrors.ErrInvalidMapping
	}

	// Create a transaction associated with the database.
	t := &Tx{}
	t.init(db)

	if db.freelist != nil {
		db.freelist.AddReadonlyTXID(t.meta.Txid())
	}

	// Unlock the meta pages.
	db.metalock.Unlock()

	// Update the transaction stats.
	if db.stats != nil {
		db.statlock.Lock()
		db.stats.TxN++
		db.stats.OpenTxN++
		db.statlock.Unlock()
	}

	return t, nil
}

func (db *DB) beginRWTx() (*Tx, error) {
	// If the database was opened with Options.ReadOnly, return an error.
	if db.readOnly {
		return nil, berrors.ErrDatabaseReadOnly
	}

	// Obtain writer lock. This is released by the transaction when it closes.
	// This enforces only one writer transaction at a time.
	db.rwlock.Lock()

	// Once we have the writer lock then we can lock the meta pages so that
	// we can set up the transaction.
	db.metalock.Lock()
	defer db.metalock.Unlock()

	// Exit if the database is not open yet.
	if !db.opened {
		db.rwlock.Unlock()
		return nil, berrors.ErrDatabaseNotOpen
	}

	// Exit if the database is not correctly mapped.
	if db.data == nil {
		db.rwlock.Unlock()
		return nil, berrors.ErrInvalidMapping
	}

	// Create a transaction associated with the database.
	t := &Tx{writable: true}
	t.init(db)
	db.rwtx = t
	db.freelist.ReleasePendingPages()
	return t, nil
}

// removeTx removes a transaction from the database.
func (db *DB) removeTx(tx *Tx) {
	// Release the read lock on the mmap.
	db.mmaplock.RUnlock()

	// Use the meta lock to restrict access to the DB object.
	db.metalock.Lock()

	if db.freelist != nil {
		db.freelist.RemoveReadonlyTXID(tx.meta.Txid())
	}

	// Unlock the meta pages.
	db.metalock.Unlock()

	// Merge statistics.
	if db.stats != nil {
		db.statlock.Lock()
		db.stats.OpenTxN--
		db.stats.TxStats.add(&tx.stats)
		db.statlock.Unlock()
	}
}

// Update executes a function within the context of a read-write managed transaction.
// If no error is returned from the function then the transaction is committed.
// If an error is returned then the entire transaction is rolled back.
// Any error that is returned from the function or returned from the commit is
// returned from the Update() method.
//
// Attempting to manually commit or rollback within the function will cause a panic.
func (db *DB) Update(fn func(*Tx) error) error {
	t, err := db.Begin(true)
	if err != nil {
		return err
	}

	// Make sure the transaction rolls back in the event of a panic.
	defer func() {
		if t.db != nil {
			t.rollback()
		}
	}()

	// Mark as a managed tx so that the inner function cannot manually commit.
	t.managed = true

	// If an error is returned from the function then rollback and return error.
	err = fn(t)
	t.managed = false
	if err != nil {
		_ = t.Rollback()
		return err
	}

	return t.Commit()
}

// View executes a function within the context of a managed read-only transaction.
// Any error that is returned from the function is returned from the View() method.
//
// Attempting to manually rollback within the function will cause a panic.
func (db *DB) View(fn func(*Tx) error) error {
	t, err := db.Begin(false)
	if err != nil {
		return err
	}

	// Make sure the transaction rolls back in the event of a panic.
	defer func() {
		if t.db != nil {
			t.rollback()
		}
	}()

	// Mark as a managed tx so that the inner function cannot manually rollback.
	t.managed = true

	// If an error is returned from the function then pass it through.
	err = fn(t)
	t.managed = false
	if err != nil {
		_ = t.Rollback()
		return err
	}

	return t.Rollback()
}

// Batch calls fn as part of a batch. It behaves similar to Update,
// except:
//
// 1. concurrent Batch calls can be combined into a single Bolt
// transaction.
//
// 2. the function passed to Batch may be called multiple times,
// regardless of whether it returns error or not.
//
// This means that Batch function side effects must be idempotent and
// take permanent effect only after a successful return is seen in
// caller.
//
// The maximum batch size and delay can be adjusted with DB.MaxBatchSize
// and DB.MaxBatchDelay, respectively.
//
// Batch is only useful when there are multiple goroutines calling it.
func (db *DB) Batch(fn func(*Tx) error) error {
	errCh := make(chan error, 1)

	db.batchMu.Lock()
	if (db.batch == nil) || (db.batch != nil && len(db.batch.calls) >= db.MaxBatchSize) {
		// There is no existing batch, or the existing batch is full; start a new one.
		db.batch = &batch{
			db: db,
		}
		db.batch.timer = time.AfterFunc(db.MaxBatchDelay, db.batch.trigger)
	}
	db.batch.calls = append(db.batch.calls, call{fn: fn, err: errCh})
	if len(db.batch.calls) >= db.MaxBatchSize {
		// wake up batch, it's ready to run
		go db.batch.trigger()
	}
	db.batchMu.Unlock()

	err := <-errCh
	if err == trySolo {
		err = db.Update(fn)
	}
	return err
}

type call struct {
	fn  func(*Tx) error
	err chan<- error
}

type batch struct {
	db    *DB
	timer *time.Timer
	start sync.Once
	calls []call
}

// trigger runs the batch if it hasn't already been run.
func (b *batch) trigger() {
	b.start.Do(b.run)
}

// run performs the transactions in the batch and communicates results
// back to DB.Batch.
func (b *batch) run() {
	b.db.batchMu.Lock()
	b.timer.Stop()
	// Make sure no new work is added to this batch, but don't break
	// other batches.
	if b.db.batch == b {
		b.db.batch = nil
	}
	b.db.batchMu.Unlock()

retry:
	for len(b.calls) > 0 {
		var failIdx = -1
		err := b.db.Update(func(tx *Tx) error {
			for i, c := range b.calls {
				if err := safelyCall(c.fn, tx); err != nil {
					failIdx = i
					return err
				}
			}
			return nil
		})

		if failIdx >= 0 {
			// take the failing transaction out of the batch. it's
			// safe to shorten b.calls here because db.batch no longer
			// points to us, and we hold the mutex anyway.
			c := b.calls[failIdx]
			b.calls[failIdx], b.calls = b.calls[len(b.calls)-1], b.calls[:len(b.calls)-1]
			// tell the submitter re-run it solo, continue with the rest of the batch
			c.err <- trySolo
			continue retry
		}

		// pass success, or bolt internal errors, to all callers
		for _, c := range b.calls {
			c.err <- err
		}
		break retry
	}
}

// trySolo is a special sentinel error value used for signaling that a
// transaction function should be re-run. It should never be seen by
// callers.
var trySolo = errors.New("batch function returned an error and should be re-run solo")

type panicked struct {
	reason interface{}
}

func (p panicked) Error() string {
	if err, ok := p.reason.(error); ok {
		return err.Error()
	}
	return fmt.Sprintf("panic: %v", p.reason)
}

func safelyCall(fn func(*Tx) error, tx *Tx) (err error) {
	defer func() {
		if p := recover(); p != nil {
			err = panicked{p}
		}
	}()
	return fn(tx)
}

// Sync executes fdatasync() against the database file handle.
//
// This is not necessary under normal operation, however, if you use NoSync
// then it allows you to force the database file to sync against the disk.
func (db *DB) Sync() (err error) {
	if lg := db.Logger(); lg != discardLogger {
		lg.Debugf("Syncing bbolt db (%s)", db.path)
		defer func() {
			if err != nil {
				lg.Errorf("[GOOS: %s, GOARCH: %s] syncing bbolt db (%s) failed: %v", runtime.GOOS, runtime.GOARCH, db.path, err)
			} else {
				lg.Debugf("Syncing bbolt db (%s) successfully", db.path)
			}
		}()
	}

	return fdatasync(db)
}

// Stats retrieves ongoing performance stats for the database.
// This is only updated when a transaction closes.
func (db *DB) Stats() Stats {
	var s Stats
	if db.stats != nil {
		db.statlock.RLock()
		s = *db.stats
		db.statlock.RUnlock()
	}
	return s
}

// This is for internal access to the raw data bytes from the C cursor, use
// carefully, or not at all.
func (db *DB) Info() *Info {
	common.Assert(db.data != nil, "database file isn't correctly mapped")
	return &Info{uintptr(unsafe.Pointer(&db.data[0])), db.pageSize}
}

// page retrieves a page reference from the mmap based on the current page size.
func (db *DB) page(id common.Pgid) *common.Page {
	pos := id * common.Pgid(db.pageSize)
	return (*common.Page)(unsafe.Pointer(&db.data[pos]))
}

// pageInBuffer retrieves a page reference from a given byte array based on the current page size.
func (db *DB) pageInBuffer(b []byte, id common.Pgid) *common.Page {
	return (*common.Page)(unsafe.Pointer(&b[id*common.Pgid(db.pageSize)]))
}

// meta retrieves the current meta page reference.
func (db *DB) meta() *common.Meta {
	// We have to return the meta with the highest txid which doesn't fail
	// validation. Otherwise, we can cause errors when in fact the database is
	// in a consistent state. metaA is the one with the higher txid.
	metaA := db.meta0
	metaB := db.meta1
	if db.meta1.Txid() > db.meta0.Txid() {
		metaA = db.meta1
		metaB = db.meta0
	}

	// Use higher meta page if valid. Otherwise, fallback to previous, if valid.
	if err := metaA.Validate(); err == nil {
		return metaA
	} else if err := metaB.Validate(); err == nil {
		return metaB
	}

	// This should never be reached, because both meta1 and meta0 were validated
	// on mmap() and we do fsync() on every write.
	panic("bolt.DB.meta(): invalid meta pages")
}

// allocate returns a contiguous block of memory starting at a given page.
func (db *DB) allocate(txid common.Txid, count int) (*common.Page, error) {
	// Allocate a temporary buffer for the page.
	var buf []byte
	if count == 1 {
		buf = db.pagePool.Get().([]byte)
	} else {
		buf = make([]byte, count*db.pageSize)
	}
	p := (*common.Page)(unsafe.Pointer(&buf[0]))
	p.SetOverflow(uint32(count - 1))

	// Use pages from the freelist if they are available.
	p.SetId(db.freelist.Allocate(txid, count))
	if p.Id() != 0 {
		return p, nil
	}

	// Resize mmap() if we're at the end.
	p.SetId(db.rwtx.meta.Pgid())
	var minsz = int((p.Id()+common.Pgid(count))+1) * db.pageSize
	if minsz >= db.datasz {
		if err := db.mmap(minsz); err != nil {
			if err == berrors.ErrMaxSizeReached {
				return nil, err
			} else {
				return nil, fmt.Errorf("mmap allocate error: %s", err)
			}
		}
	}

	// Move the page id high water mark.
	curPgid := db.rwtx.meta.Pgid()
	db.rwtx.meta.SetPgid(curPgid + common.Pgid(count))

	return p, nil
}

// grow grows the size of the database to the given sz.
func (db *DB) grow(sz int) error {
	// Ignore if the new size is less than available file size.
	lg := db.Logger()
	fileSize, err := db.fileSize()
	if err != nil {
		lg.Errorf("getting file size failed: %w", err)
		return err
	}
	if sz <= fileSize {
		return nil
	}

	// If the data is smaller than the alloc size then only allocate what's needed.
	// Once it goes over the allocation size then allocate in chunks.
	if db.datasz <= db.AllocSize {
		sz = db.datasz
	} else {
		sz += db.AllocSize
	}

	if !db.readOnly && db.MaxSize > 0 && sz > db.MaxSize {
		lg.Errorf("[GOOS: %s, GOARCH: %s] maximum db size reached, size: %d, db.MaxSize: %d", runtime.GOOS, runtime.GOARCH, sz, db.MaxSize)
		return berrors.ErrMaxSizeReached
	}

	// Truncate and fsync to ensure file size metadata is flushed.
	// https://github.com/boltdb/bolt/issues/284
	if !db.NoGrowSync && !db.readOnly {
		if runtime.GOOS != "windows" {
			// gofail: var resizeFileError string
			// return errors.New(resizeFileError)
			if err := db.file.Truncate(int64(sz)); err != nil {
				lg.Errorf("[GOOS: %s, GOARCH: %s] truncating file failed, size: %d, db.datasz: %d, error: %v", runtime.GOOS, runtime.GOARCH, sz, db.datasz, err)
				return fmt.Errorf("file resize error: %s", err)
			}
		}
		if err := db.file.Sync(); err != nil {
			lg.Errorf("[GOOS: %s, GOARCH: %s] syncing file failed, db.datasz: %d, error: %v", runtime.GOOS, runtime.GOARCH, db.datasz, err)
			return fmt.Errorf("file sync error: %s", err)
		}
		if db.Mlock {
			// unlock old file and lock new one
			if err := db.mrelock(fileSize, sz); err != nil {
				return fmt.Errorf("mlock/munlock error: %s", err)
			}
		}
	}

	return nil
}

func (db *DB) IsReadOnly() bool {
	return db.readOnly
}

func (db *DB) freepages() []common.Pgid {
	tx, err := db.beginTx()
	defer func() {
		err = tx.Rollback()
		if err != nil {
			panic("freepages: failed to rollback tx")
		}
	}()
	if err != nil {
		panic("freepages: failed to open read only tx")
	}

	reachable := make(map[common.Pgid]*common.Page)
	nofreed := make(map[common.Pgid]bool)
	ech := make(chan error)

	go func() {
		defer close(ech)
		tx.recursivelyCheckBucket(&tx.root, reachable, nofreed, HexKVStringer(), ech)
	}()
	// following for loop will exit once channel is closed in the above goroutine.
	// we don't need to wait explictly with a waitgroup
	for e := range ech {
		panic(fmt.Sprintf("freepages: failed to get all reachable pages (%v)", e))
	}

	// TODO: If check bucket reported any corruptions (ech) we shouldn't proceed to freeing the pages.

	var fids []common.Pgid
	for i := common.Pgid(2); i < db.meta().Pgid(); i++ {
		if _, ok := reachable[i]; !ok {
			fids = append(fids, i)
		}
	}
	return fids
}

func newFreelist(freelistType FreelistType) fl.Interface {
	if freelistType == FreelistMapType {
		return fl.NewHashMapFreelist()
	}
	return fl.NewArrayFreelist()
}

// Options represents the options that can be set when opening a database.
type Options struct {
	// Timeout is the amount of time to wait to obtain a file lock.
	// When set to zero it will wait indefinitely.
	Timeout time.Duration

	// Sets the DB.NoGrowSync flag before memory mapping the file.
	NoGrowSync bool

	// Do not sync freelist to disk. This improves the database write performance
	// under normal operation, but requires a full database re-sync during recovery.
	NoFreelistSync bool

	// PreLoadFreelist sets whether to load the free pages when opening
	// the db file. Note when opening db in write mode, bbolt will always
	// load the free pages.
	PreLoadFreelist bool

	// FreelistType sets the backend freelist type. There are two options. Array which is simple but endures
	// dramatic performance degradation if database is large and fragmentation in freelist is common.
	// The alternative one is using hashmap, it is faster in almost all circumstances
	// but it doesn't guarantee that it offers the smallest page id available. In normal case it is safe.
	// The default type is array
	FreelistType FreelistType

	// Open database in read-only mode. Uses flock(..., LOCK_SH |LOCK_NB) to
	// grab a shared lock (UNIX).
	ReadOnly bool

	// Sets the DB.MmapFlags flag before memory mapping the file.
	MmapFlags int

	// InitialMmapSize is the initial mmap size of the database
	// in bytes. Read transactions won't block write transaction
	// if the InitialMmapSize is large enough to hold database mmap
	// size. (See DB.Begin for more information)
	//
	// If <=0, the initial map size is 0.
	// If initialMmapSize is smaller than the previous database size,
	// it takes no effect.
	//
	// Note: On Windows, due to platform limitations, the database file size
	// will be immediately resized to match `InitialMmapSize` (aligned to page size)
	// when the DB is opened. On non-Windows platforms, the file size will grow
	// dynamically based on the actual amount of written data, regardless of `InitialMmapSize`.
	// Refer to https://github.com/etcd-io/bbolt/issues/378#issuecomment-1378121966.
	InitialMmapSize int

	// PageSize overrides the default OS page size.
	PageSize int

	// MaxSize sets the maximum size of the data file. <=0 means no maximum.
	MaxSize int

	// NoSync sets the initial value of DB.NoSync. Normally this can just be
	// set directly on the DB itself when returned from Open(), but this option
	// is useful in APIs which expose Options but not the underlying DB.
	NoSync bool

	// OpenFile is used to open files. It defaults to os.OpenFile. This option
	// is useful for writing hermetic tests.
	OpenFile func(string, int, os.FileMode) (*os.File, error)

	// Mlock locks database file in memory when set to true.
	// It prevents potential page faults, however
	// used memory can't be reclaimed. (UNIX only)
	Mlock bool

	// Logger is the logger used for bbolt.
	Logger Logger

	// NoStatistics turns off statistics collection, Stats method will
	// return empty structure in this case. This can be beneficial for
	// performance under high-concurrency read-only transactions.
	NoStatistics bool
}

func (o *Options) String() string {
	if o == nil {
		return "{}"
	}

	return fmt.Sprintf("{Timeout: %s, NoGrowSync: %t, NoFreelistSync: %t, PreLoadFreelist: %t, FreelistType: %s, ReadOnly: %t, MmapFlags: %x, InitialMmapSize: %d, PageSize: %d, MaxSize: %d, NoSync: %t, OpenFile: %p, Mlock: %t, Logger: %p, NoStatistics: %t}",
		o.Timeout, o.NoGrowSync, o.NoFreelistSync, o.PreLoadFreelist, o.FreelistType, o.ReadOnly, o.MmapFlags, o.InitialMmapSize, o.PageSize, o.MaxSize, o.NoSync, o.OpenFile, o.Mlock, o.Logger, o.NoStatistics)

}

// DefaultOptions represent the options used if nil options are passed into Open().
// No timeout is used which will cause Bolt to wait indefinitely for a lock.
var DefaultOptions = &Options{
	Timeout:      0,
	NoGrowSync:   false,
	FreelistType: FreelistArrayType,
}

// Stats represents statistics about the database.
type Stats struct {
	// Put `TxStats` at the first field to ensure it's 64-bit aligned. Note
	// that the first word in an allocated struct can be relied upon to be
	// 64-bit aligned. Refer to https://pkg.go.dev/sync/atomic#pkg-note-BUG.
	// Also refer to discussion in https://github.com/etcd-io/bbolt/issues/577.
	TxStats TxStats // global, ongoing stats.

	// Freelist stats
	FreePageN     int // total number of free pages on the freelist
	PendingPageN  int // total number of pending pages on the freelist
	FreeAlloc     int // total bytes allocated in free pages
	FreelistInuse int // total bytes used by the freelist

	// Transaction stats
	TxN     int // total number of started read transactions
	OpenTxN int // number of currently open read transactions
}

// Sub calculates and returns the difference between two sets of database stats.
// This is useful when obtaining stats at two different points and time and
// you need the performance counters that occurred within that time span.
func (s *Stats) Sub(other *Stats) Stats {
	if other == nil {
		return *s
	}
	var diff Stats
	diff.FreePageN = s.FreePageN
	diff.PendingPageN = s.PendingPageN
	diff.FreeAlloc = s.FreeAlloc
	diff.FreelistInuse = s.FreelistInuse
	diff.TxN = s.TxN - other.TxN
	diff.TxStats = s.TxStats.Sub(&other.TxStats)
	return diff
}

type Info struct {
	Data     uintptr
	PageSize int
}
```

## File: `db_test.go`
```go
package bbolt_test

import (
	"bytes"
	"encoding/binary"
	"errors"
	"fmt"
	"hash/fnv"
	"log"
	"math/rand"
	"os"
	"path/filepath"
	"reflect"
	"runtime"
	"strings"
	"sync"
	"testing"
	"time"
	"unsafe"

	"github.com/stretchr/testify/assert"
	"github.com/stretchr/testify/require"

	bolt "go.etcd.io/bbolt"
	berrors "go.etcd.io/bbolt/errors"
	"go.etcd.io/bbolt/internal/btesting"
	"go.etcd.io/bbolt/internal/common"
)

// pageSize is the size of one page in the data file.
const pageSize = 4096

// pageHeaderSize is the size of a page header.
const pageHeaderSize = 16

// meta represents a simplified version of a database meta page for testing.
type meta struct {
	_       uint32
	version uint32
	_       uint32
	_       uint32
	_       [16]byte
	_       uint64
	pgid    uint64
	_       uint64
	_       uint64
}

// Ensure that a database can be opened without error.
func TestOpen(t *testing.T) {
	path := tempfile()
	defer os.RemoveAll(path)

	db, err := bolt.Open(path, 0600, nil)
	if err != nil {
		t.Fatal(err)
	} else if db == nil {
		t.Fatal("expected db")
	}

	if s := db.Path(); s != path {
		t.Fatalf("unexpected path: %s", s)
	}

	if err := db.Close(); err != nil {
		t.Fatal(err)
	}
}

// Regression validation for https://github.com/etcd-io/bbolt/pull/122.
// Tests multiple goroutines simultaneously opening a database.
func TestOpen_MultipleGoroutines(t *testing.T) {
	if testing.Short() {
		t.Skip("skipping test in short mode")
	}

	const (
		instances  = 30
		iterations = 30
	)
	path := tempfile()
	defer os.RemoveAll(path)
	var wg sync.WaitGroup
	errCh := make(chan error, iterations*instances)
	for iteration := 0; iteration < iterations; iteration++ {
		for instance := 0; instance < instances; instance++ {
			wg.Add(1)
			go func() {
				defer wg.Done()
				db, err := bolt.Open(path, 0600, nil)
				if err != nil {
					errCh <- err
					return
				}
				if err := db.Close(); err != nil {
					errCh <- err
					return
				}
			}()
		}
		wg.Wait()
	}
	close(errCh)
	for err := range errCh {
		if err != nil {
			t.Fatalf("error from inside goroutine: %v", err)
		}
	}
}

// Ensure that opening a database with a blank path returns an error.
func TestOpen_ErrPathRequired(t *testing.T) {
	_, err := bolt.Open("", 0600, nil)
	if err == nil {
		t.Fatalf("expected error")
	}
}

// Ensure that opening a database with a bad path returns an error.
func TestOpen_ErrNotExists(t *testing.T) {
	_, err := bolt.Open(filepath.Join(tempfile(), "bad-path"), 0600, nil)
	if err == nil {
		t.Fatal("expected error")
	}
}

// Ensure that opening a file that is not a Bolt database returns ErrInvalid.
func TestOpen_ErrInvalid(t *testing.T) {
	path := tempfile()
	defer os.RemoveAll(path)

	f, err := os.Create(path)
	if err != nil {
		t.Fatal(err)
	}
	if _, err := fmt.Fprintln(f, "this is not a bolt database"); err != nil {
		t.Fatal(err)
	}
	if err := f.Close(); err != nil {
		t.Fatal(err)
	}

	if _, err := bolt.Open(path, 0600, nil); err != berrors.ErrInvalid {
		t.Fatalf("unexpected error: %s", err)
	}
}

// Ensure that opening a file with two invalid versions returns ErrVersionMismatch.
func TestOpen_ErrVersionMismatch(t *testing.T) {
	if pageSize != os.Getpagesize() {
		t.Skip("page size mismatch")
	}

	// Create empty database.
	db := btesting.MustCreateDB(t)
	path := db.Path()

	// Close database.
	if err := db.Close(); err != nil {
		t.Fatal(err)
	}

	// Read data file.
	buf, err := os.ReadFile(path)
	if err != nil {
		t.Fatal(err)
	}

	// Rewrite meta pages.
	meta0 := (*meta)(unsafe.Pointer(&buf[pageHeaderSize]))
	meta0.version++
	meta1 := (*meta)(unsafe.Pointer(&buf[pageSize+pageHeaderSize]))
	meta1.version++
	if err := os.WriteFile(path, buf, 0666); err != nil {
		t.Fatal(err)
	}

	// Reopen data file.
	if _, err := bolt.Open(path, 0600, nil); err != berrors.ErrVersionMismatch {
		t.Fatalf("unexpected error: %s", err)
	}
}

// Ensure that opening a file with two invalid checksums returns ErrChecksum.
func TestOpen_ErrChecksum(t *testing.T) {
	if pageSize != os.Getpagesize() {
		t.Skip("page size mismatch")
	}

	// Create empty database.
	db := btesting.MustCreateDB(t)
	path := db.Path()

	// Close database.
	if err := db.Close(); err != nil {
		t.Fatal(err)
	}

	// Read data file.
	buf, err := os.ReadFile(path)
	if err != nil {
		t.Fatal(err)
	}

	// Rewrite meta pages.
	meta0 := (*meta)(unsafe.Pointer(&buf[pageHeaderSize]))
	meta0.pgid++
	meta1 := (*meta)(unsafe.Pointer(&buf[pageSize+pageHeaderSize]))
	meta1.pgid++
	if err := os.WriteFile(path, buf, 0666); err != nil {
		t.Fatal(err)
	}

	// Reopen data file.
	if _, err := bolt.Open(path, 0600, nil); err != berrors.ErrChecksum {
		t.Fatalf("unexpected error: %s", err)
	}
}

// Ensure that it can read the page size from the second meta page if the first one is invalid.
// The page size is expected to be the OS's page size in this case.
func TestOpen_ReadPageSize_FromMeta1_OS(t *testing.T) {
	// Create empty database.
	db := btesting.MustCreateDB(t)
	path := db.Path()
	// Close the database
	db.MustClose()

	// Read data file.
	buf, err := os.ReadFile(path)
	if err != nil {
		t.Fatal(err)
	}

	// Rewrite first meta page.
	meta0 := (*meta)(unsafe.Pointer(&buf[pageHeaderSize]))
	meta0.pgid++
	if err := os.WriteFile(path, buf, 0666); err != nil {
		t.Fatal(err)
	}

	// Reopen data file.
	db = btesting.MustOpenDBWithOption(t, path, nil)
	require.Equalf(t, os.Getpagesize(), db.Info().PageSize, "check page size failed")
}

// Ensure that it can read the page size from the second meta page if the first one is invalid.
// The page size is expected to be the given page size in this case.
func TestOpen_ReadPageSize_FromMeta1_Given(t *testing.T) {
	// test page size from 1KB (1024<<0) to 16MB(1024<<14)
	for i := 0; i <= 14; i++ {
		givenPageSize := 1024 << uint(i)
		t.Logf("Testing page size %d", givenPageSize)
		// Create empty database.
		db := btesting.MustCreateDBWithOption(t, &bolt.Options{PageSize: givenPageSize})
		path := db.Path()
		// Close the database
		db.MustClose()

		// Read data file.
		buf, err := os.ReadFile(path)
		require.NoError(t, err)

		// Rewrite meta pages.
		if i%3 == 0 {
			t.Logf("#%d: Intentionally corrupt the first meta page for pageSize %d", i, givenPageSize)
			meta0 := (*meta)(unsafe.Pointer(&buf[pageHeaderSize]))
			meta0.pgid++
			err = os.WriteFile(path, buf, 0666)
			require.NoError(t, err)
		}

		// Reopen data file.
		db = btesting.MustOpenDBWithOption(t, path, nil)
		require.Equalf(t, givenPageSize, db.Info().PageSize, "check page size failed")
		db.MustClose()
	}
}

// Ensure that opening a database does not increase its size.
// https://github.com/boltdb/bolt/issues/291
func TestOpen_Size(t *testing.T) {
	// Open a data file.
	db := btesting.MustCreateDB(t)

	pagesize := db.Info().PageSize

	// Insert until we get above the minimum 4MB size.
	err := db.Fill([]byte("data"), 1, 10000,
		func(tx int, k int) []byte { return []byte(fmt.Sprintf("%04d", k)) },
		func(tx int, k int) []byte { return make([]byte, 1000) },
	)
	if err != nil {
		t.Fatal(err)
	}

	path := db.Path()
	db.MustClose()

	sz := fileSize(path)
	if sz == 0 {
		t.Fatalf("unexpected new file size: %d", sz)
	}

	db.MustReopen()
	if err := db.Update(func(tx *bolt.Tx) error {
		if err := tx.Bucket([]byte("data")).Put([]byte{0}, []byte{0}); err != nil {
			t.Fatal(err)
		}
		return nil
	}); err != nil {
		t.Fatal(err)
	}
	if err := db.Close(); err != nil {
		t.Fatal(err)
	}
	newSz := fileSize(path)
	if newSz == 0 {
		t.Fatalf("unexpected new file size: %d", newSz)
	}

	// Compare the original size with the new size.
	// db size might increase by a few page sizes due to the new small update.
	if sz < newSz-5*int64(pagesize) {
		t.Fatalf("unexpected file growth: %d => %d", sz, newSz)
	}
}

// Ensure that opening a database beyond the max step size does not increase its size.
// https://github.com/boltdb/bolt/issues/303
func TestOpen_Size_Large(t *testing.T) {
	if testing.Short() {
		t.Skip("short mode")
	}

	// Open a data file.
	db := btesting.MustCreateDB(t)
	path := db.Path()

	pagesize := db.Info().PageSize

	// Insert until we get above the minimum 4MB size.
	var index uint64
	for i := 0; i < 10000; i++ {
		if err := db.Update(func(tx *bolt.Tx) error {
			b, _ := tx.CreateBucketIfNotExists([]byte("data"))
			for j := 0; j < 1000; j++ {
				if err := b.Put(u64tob(index), make([]byte, 50)); err != nil {
					t.Fatal(err)
				}
				index++
			}
			return nil
		}); err != nil {
			t.Fatal(err)
		}
	}

	// Close database and grab the size.
	if err := db.Close(); err != nil {
		t.Fatal(err)
	}
	sz := fileSize(path)
	if sz == 0 {
		t.Fatalf("unexpected new file size: %d", sz)
	} else if sz < (1 << 30) {
		t.Fatalf("expected larger initial size: %d", sz)
	}

	// Reopen database, update, and check size again.
	db0, err := bolt.Open(path, 0600, nil)
	if err != nil {
		t.Fatal(err)
	}
	if err := db0.Update(func(tx *bolt.Tx) error {
		return tx.Bucket([]byte("data")).Put([]byte{0}, []byte{0})
	}); err != nil {
		t.Fatal(err)
	}
	if err := db0.Close(); err != nil {
		t.Fatal(err)
	}

	newSz := fileSize(path)
	if newSz == 0 {
		t.Fatalf("unexpected new file size: %d", newSz)
	}

	// Compare the original size with the new size.
	// db size might increase by a few page sizes due to the new small update.
	if sz < newSz-5*int64(pagesize) {
		t.Fatalf("unexpected file growth: %d => %d", sz, newSz)
	}
}

// Ensure that a re-opened database is consistent.
func TestOpen_Check(t *testing.T) {
	path := tempfile()
	defer os.RemoveAll(path)

	db, err := bolt.Open(path, 0600, nil)
	if err != nil {
		t.Fatal(err)
	}
	if err = db.View(func(tx *bolt.Tx) error { return <-tx.Check() }); err != nil {
		t.Fatal(err)
	}
	if err = db.Close(); err != nil {
		t.Fatal(err)
	}

	db, err = bolt.Open(path, 0600, nil)
	if err != nil {
		t.Fatal(err)
	}
	if err := db.View(func(tx *bolt.Tx) error { return <-tx.Check() }); err != nil {
		t.Fatal(err)
	}
	if err := db.Close(); err != nil {
		t.Fatal(err)
	}
}

// Ensure that write errors to the meta file handler during initialization are returned.
func TestOpen_MetaInitWriteError(t *testing.T) {
	t.Skip("pending")
}

// Ensure that a database that is too small returns an error.
func TestOpen_FileTooSmall(t *testing.T) {
	path := tempfile()
	defer os.RemoveAll(path)

	db, err := bolt.Open(path, 0600, nil)
	if err != nil {
		t.Fatal(err)
	}
	pageSize := int64(db.Info().PageSize)
	if err = db.Close(); err != nil {
		t.Fatal(err)
	}

	// corrupt the database
	if err = os.Truncate(path, pageSize); err != nil {
		t.Fatal(err)
	}

	_, err = bolt.Open(path, 0600, nil)
	if err == nil || !strings.Contains(err.Error(), "file size too small") {
		t.Fatalf("unexpected error: %s", err)
	}
}

// TestDB_Open_InitialMmapSize tests if having InitialMmapSize large enough
// to hold data from concurrent write transaction resolves the issue that
// read transaction blocks the write transaction and causes deadlock.
// This is a very hacky test since the mmap size is not exposed.
func TestDB_Open_InitialMmapSize(t *testing.T) {
	tests := []struct {
		name       string
		withReadTx bool
	}{
		{
			name:       "with concurrent read transaction",
			withReadTx: true,
		},
		{
			name:       "without concurrent read transaction",
			withReadTx: false,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			path := tempfile()
			defer os.Remove(path)

			initMmapSize := 1 << 30  // 1GB
			testWriteSize := 1 << 27 // 134MB

			db, err := bolt.Open(path, 0600, &bolt.Options{InitialMmapSize: initMmapSize})
			if err != nil {
				t.Fatal(err)
			}
			defer db.Close()

			var rtx *bolt.Tx
			if tt.withReadTx {
				// create a long-running read transaction
				// that never gets closed while writing
				rtx, err = db.Begin(false)
				if err != nil {
					t.Fatal(err)
				}
			}

			// create a write transaction
			wtx, err := db.Begin(true)
			if err != nil {
				t.Fatal(err)
			}

			b, err := wtx.CreateBucket([]byte("test"))
			if err != nil {
				t.Fatal(err)
			}

			// commit a large write
			err = b.Put([]byte("foo"), make([]byte, testWriteSize))
			if err != nil {
				t.Fatal(err)
			}

			done := make(chan error, 1)
			start := time.Now()

			go func() {
				err := wtx.Commit()
				done <- err
			}()

			// Windows needs more time due to immediate file expansion to InitialMmapSize
			timeout := 5 * time.Second
			if runtime.GOOS == "windows" {
				timeout = 15 * time.Second
			}

			select {
			case <-time.After(timeout):
				t.Error("unexpected that the writer is blocked for a long time")
			case err := <-done:
				elapsed := time.Since(start)
				if err != nil {
					t.Fatal(err)
				}
				t.Logf("Write commit completed in %v", elapsed)
			}

			if rtx != nil {
				if err := rtx.Rollback(); err != nil {
					t.Fatal(err)
				}
			}
		})
	}
}

// TestDB_Open_ReadOnly checks a database in read only mode can read but not write.
func TestDB_Open_ReadOnly(t *testing.T) {
	// Create a writable db, write k-v and close it.
	db := btesting.MustCreateDB(t)

	if err := db.Update(func(tx *bolt.Tx) error {
		b, err := tx.CreateBucket([]byte("widgets"))
		if err != nil {
			t.Fatal(err)
		}
		if err := b.Put([]byte("foo"), []byte("bar")); err != nil {
			t.Fatal(err)
		}
		return nil
	}); err != nil {
		t.Fatal(err)
	}
	if err := db.Close(); err != nil {
		t.Fatal(err)
	}

	f := db.Path()
	o := &bolt.Options{ReadOnly: true}
	readOnlyDB, err := bolt.Open(f, 0600, o)
	if err != nil {
		panic(err)
	}

	if !readOnlyDB.IsReadOnly() {
		t.Fatal("expect db in read only mode")
	}

	// Read from a read-only transaction.
	if err := readOnlyDB.View(func(tx *bolt.Tx) error {
		value := tx.Bucket([]byte("widgets")).Get([]byte("foo"))
		if !bytes.Equal(value, []byte("bar")) {
			t.Fatal("expect value 'bar', got", value)
		}
		return nil
	}); err != nil {
		t.Fatal(err)
	}

	// Can't launch read-write transaction.
	if _, err := readOnlyDB.Begin(true); err != berrors.ErrDatabaseReadOnly {
		t.Fatalf("unexpected error: %s", err)
	}

	if err := readOnlyDB.Close(); err != nil {
		t.Fatal(err)
	}
}

func TestDB_Open_ReadOnly_NoCreate(t *testing.T) {
	f := filepath.Join(t.TempDir(), "db")
	_, err := bolt.Open(f, 0600, &bolt.Options{ReadOnly: true})
	require.ErrorIs(t, err, os.ErrNotExist)
}

// TestOpen_BigPage checks the database uses bigger pages when
// changing PageSize.
func TestOpen_BigPage(t *testing.T) {
	pageSize := os.Getpagesize()

	db1 := btesting.MustCreateDBWithOption(t, &bolt.Options{PageSize: pageSize * 2})

	db2 := btesting.MustCreateDBWithOption(t, &bolt.Options{PageSize: pageSize * 4})

	if db1sz, db2sz := fileSize(db1.Path()), fileSize(db2.Path()); db1sz >= db2sz {
		t.Errorf("expected %d < %d", db1sz, db2sz)
	}
}

// TestOpen_RecoverFreeList tests opening the DB with free-list
// write-out after no free list sync will recover the free list
// and write it out.
func TestOpen_RecoverFreeList(t *testing.T) {
	db := btesting.MustCreateDBWithOption(t, &bolt.Options{NoFreelistSync: true})

	// Write some pages.
	tx, err := db.Begin(true)
	if err != nil {
		t.Fatal(err)
	}
	wbuf := make([]byte, 8192)
	for i := 0; i < 100; i++ {
		s := fmt.Sprintf("%d", i)
		b, err := tx.CreateBucket([]byte(s))
		if err != nil {
			t.Fatal(err)
		}
		if err = b.Put([]byte(s), wbuf); err != nil {
			t.Fatal(err)
		}
	}
	if err = tx.Commit(); err != nil {
		t.Fatal(err)
	}

	// Generate free pages.
	if tx, err = db.Begin(true); err != nil {
		t.Fatal(err)
	}
	for i := 0; i < 50; i++ {
		s := fmt.Sprintf("%d", i)
		b := tx.Bucket([]byte(s))
		if b == nil {
			t.Fatal(err)
		}
		if err := b.Delete([]byte(s)); err != nil {
			t.Fatal(err)
		}
	}
	if err := tx.Commit(); err != nil {
		t.Fatal(err)
	}
	db.MustClose()

	// Record freelist count from opening with NoFreelistSync.
	db.MustReopen()
	freepages := db.Stats().FreePageN
	if freepages == 0 {
		t.Fatalf("no free pages on NoFreelistSync reopen")
	}
	db.MustClose()

	// Check free page count is reconstructed when opened with freelist sync.
	db.SetOptions(&bolt.Options{})
	db.MustReopen()
	// One less free page for syncing the free list on open.
	freepages--
	if fp := db.Stats().FreePageN; fp < freepages {
		t.Fatalf("closed with %d free pages, opened with %d", freepages, fp)
	}
}

// Ensure that a database cannot open a transaction when it's not open.
func TestDB_Begin_ErrDatabaseNotOpen(t *testing.T) {
	var db bolt.DB
	if _, err := db.Begin(false); err != berrors.ErrDatabaseNotOpen {
		t.Fatalf("unexpected error: %s", err)
	}
}

// Ensure that a read-write transaction can be retrieved.
func TestDB_BeginRW(t *testing.T) {
	db := btesting.MustCreateDB(t)

	tx, err := db.Begin(true)
	require.NoError(t, err)
	require.NotNil(t, tx, "expected tx")
	defer func() { require.NoError(t, tx.Commit()) }()

	require.True(t, tx.Writable(), "expected writable tx")
	require.Same(t, db.DB, tx.DB())
}

// TestDB_Concurrent_WriteTo checks that issuing WriteTo operations concurrently
// with commits does not produce corrupted db files. It also verifies that all
// readonly transactions, which are created based on the same data view, should
// always read the same data.
func TestDB_Concurrent_WriteTo_and_ConsistentRead(t *testing.T) {
	o := &bolt.Options{
		NoFreelistSync: false,
		PageSize:       4096,
	}
	db := btesting.MustCreateDBWithOption(t, o)

	wtxs, rtxs := 50, 5
	bucketName := []byte("data")

	var dataLock sync.Mutex
	dataCache := make(map[int][]map[string]string)

	var wg sync.WaitGroup
	wg.Add(wtxs * rtxs)
	f := func(round int, tx *bolt.Tx) {
		defer wg.Done()
		time.Sleep(time.Duration(rand.Intn(200)+10) * time.Millisecond)
		f := filepath.Join(t.TempDir(), fmt.Sprintf("%d-bolt-", round))
		err := tx.CopyFile(f, 0600)
		require.NoError(t, err)

		// read all the data
		b := tx.Bucket(bucketName)
		data := make(map[string]string)
		err = b.ForEach(func(k, v []byte) error {
			data[string(k)] = string(v)
			return nil
		})
		require.NoError(t, err)

		// cache the data
		dataLock.Lock()
		dataSlice := dataCache[round]
		dataSlice = append(dataSlice, data)
		dataCache[round] = dataSlice
		dataLock.Unlock()

		err = tx.Rollback()
		require.NoError(t, err)

		copyOpt := *o
		snap := btesting.MustOpenDBWithOption(t, f, &copyOpt)
		defer snap.MustClose()
		snap.MustCheck()
	}

	err := db.Update(func(tx *bolt.Tx) error {
		_, err := tx.CreateBucket(bucketName)
		return err
	})
	require.NoError(t, err)

	for i := 0; i < wtxs; i++ {
		tx, err := db.Begin(true)
		require.NoError(t, err)

		b := tx.Bucket(bucketName)

		for j := 0; j < rtxs; j++ {
			rtx, rerr := db.Begin(false)
			require.NoError(t, rerr)
			go f(i, rtx)

			for k := 0; k < 10; k++ {
				key, value := fmt.Sprintf("key_%d", rand.Intn(10)), fmt.Sprintf("value_%d", rand.Intn(100))
				perr := b.Put([]byte(key), []byte(value))
				require.NoError(t, perr)
			}
		}
		err = tx.Commit()
		require.NoError(t, err)
	}
	wg.Wait()

	// compare the data. The data generated in the same round
	// should be exactly the same.
	for round, dataSlice := range dataCache {
		data0 := dataSlice[0]

		for i := 1; i < len(dataSlice); i++ {
			datai := dataSlice[i]
			same := reflect.DeepEqual(data0, datai)
			require.True(t, same, fmt.Sprintf("found inconsistent data in round %d, data[0]: %v, data[%d] : %v", round, data0, i, datai))
		}
	}
}

// TestDB_WriteTo_and_Overwrite verifies that `(tx *Tx) WriteTo` can still
// work even the underlying file is overwritten between the time a read-only
// transaction is created and the time the file is actually opened
func TestDB_WriteTo_and_Overwrite(t *testing.T) {
	testCases := []struct {
		name      string
		writeFlag int
	}{
		{
			name:      "writeFlag not set",
			writeFlag: 0,
		},
		/* syscall.O_DIRECT not supported on some platforms, i.e. Windows and MacOS
		{
			name:      "writeFlag set",
			writeFlag: syscall.O_DIRECT,
		},*/
	}

	fRead := func(db *bolt.DB, bucketName []byte) map[string]string {
		data := make(map[string]string)
		_ = db.View(func(tx *bolt.Tx) error {
			b := tx.Bucket(bucketName)
			berr := b.ForEach(func(k, v []byte) error {
				data[string(k)] = string(v)
				return nil
			})
			require.NoError(t, berr)
			return nil
		})
		return data
	}

	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			db := btesting.MustCreateDBWithOption(t, &bolt.Options{
				PageSize: 4096,
			})
			filePathOfDb := db.Path()

			var (
				bucketName   = []byte("data")
				dataExpected map[string]string
				dataActual   map[string]string
			)

			t.Log("Populate some data")
			err := db.Update(func(tx *bolt.Tx) error {
				b, berr := tx.CreateBucket(bucketName)
				if berr != nil {
					return berr
				}
				for k := 0; k < 10; k++ {
					key, value := fmt.Sprintf("key_%d", rand.Intn(10)), fmt.Sprintf("value_%d", rand.Intn(100))
					if perr := b.Put([]byte(key), []byte(value)); perr != nil {
						return perr
					}
				}
				return nil
			})
			require.NoError(t, err)

			t.Log("Read all the data before calling WriteTo")
			dataExpected = fRead(db.DB, bucketName)

			t.Log("Create a readonly transaction for WriteTo")
			rtx, rerr := db.Begin(false)
			require.NoError(t, rerr)

			// Some platforms (i.e. Windows) don't support renaming a file
			// when the target file already exist and is opened.
			if runtime.GOOS == "linux" {
				t.Log("Create another empty db file")
				db2 := btesting.MustCreateDBWithOption(t, &bolt.Options{
					PageSize: 4096,
				})
				db2.MustClose()
				filePathOfDb2 := db2.Path()

				t.Logf("Renaming the new empty db file (%s) to the original db path (%s)", filePathOfDb2, filePathOfDb)
				err = os.Rename(filePathOfDb2, filePathOfDb)
				require.NoError(t, err)
			} else {
				t.Log("Ignore renaming step on non-Linux platform")
			}

			t.Logf("Call WriteTo to copy the data of the original db file")
			f := filepath.Join(t.TempDir(), "-backup-db")
			err = rtx.CopyFile(f, 0600)
			require.NoError(t, err)
			require.NoError(t, rtx.Rollback())

			t.Logf("Read all the data from the backup db after calling WriteTo")
			newDB, err := bolt.Open(f, 0600, &bolt.Options{
				ReadOnly: true,
			})
			require.NoError(t, err)
			dataActual = fRead(newDB, bucketName)
			err = newDB.Close()
			require.NoError(t, err)

			t.Log("Compare the dataExpected and dataActual")
			same := reflect.DeepEqual(dataExpected, dataActual)
			require.True(t, same, fmt.Sprintf("found inconsistent data, dataExpected: %v, ddataActual : %v", dataExpected, dataActual))
		})
	}
}

// Ensure that opening a transaction while the DB is closed returns an error.
func TestDB_BeginRW_Closed(t *testing.T) {
	var db bolt.DB
	if _, err := db.Begin(true); err != berrors.ErrDatabaseNotOpen {
		t.Fatalf("unexpected error: %s", err)
	}
}

func TestDB_Close_PendingTx_RW(t *testing.T) { testDB_Close_PendingTx(t, true) }
func TestDB_Close_PendingTx_RO(t *testing.T) { testDB_Close_PendingTx(t, false) }

// Ensure that a database cannot close while transactions are open.
func testDB_Close_PendingTx(t *testing.T, writable bool) {
	db := btesting.MustCreateDB(t)

	// Start transaction.
	tx, err := db.Begin(writable)
	if err != nil {
		t.Fatal(err)
	}

	// Open update in separate goroutine.
	startCh := make(chan struct{}, 1)
	done := make(chan error, 1)
	go func() {
		startCh <- struct{}{}
		err := db.Close()
		done <- err
	}()
	// wait for the above goroutine to get scheduled.
	<-startCh

	// Ensure database hasn't closed.
	time.Sleep(100 * time.Millisecond)
	select {
	case err := <-done:
		if err != nil {
			t.Errorf("error from inside goroutine: %v", err)
		}
		t.Fatal("database closed too early")
	default:
	}

	// Commit/close transaction.
	if writable {
		err = tx.Commit()
	} else {
		err = tx.Rollback()
	}
	if err != nil {
		t.Fatal(err)
	}

	// Ensure database closed now.
	select {
	case err := <-done:
		if err != nil {
			t.Fatalf("error from inside goroutine: %v", err)
		}
	case <-time.After(5 * time.Second):
		t.Fatalf("database did not close")
	}
}

// Ensure a database can provide a transactional block.
func TestDB_Update(t *testing.T) {
	db := btesting.MustCreateDB(t)
	if err := db.Update(func(tx *bolt.Tx) error {
		b, err := tx.CreateBucket([]byte("widgets"))
		if err != nil {
			t.Fatal(err)
		}
		if err := b.Put([]byte("foo"), []byte("bar")); err != nil {
			t.Fatal(err)
		}
		if err := b.Put([]byte("baz"), []byte("bat")); err != nil {
			t.Fatal(err)
		}
		if err := b.Delete([]byte("foo")); err != nil {
			t.Fatal(err)
		}
		return nil
	}); err != nil {
		t.Fatal(err)
	}
	if err := db.View(func(tx *bolt.Tx) error {
		b := tx.Bucket([]byte("widgets"))
		if v := b.Get([]byte("foo")); v != nil {
			t.Fatalf("expected nil value, got: %v", v)
		}
		if v := b.Get([]byte("baz")); !bytes.Equal(v, []byte("bat")) {
			t.Fatalf("unexpected value: %v", v)
		}
		return nil
	}); err != nil {
		t.Fatal(err)
	}
}

// Ensure a closed database returns an error while running a transaction block
func TestDB_Update_Closed(t *testing.T) {
	var db bolt.DB
	if err := db.Update(func(tx *bolt.Tx) error {
		if _, err := tx.CreateBucket([]byte("widgets")); err != nil {
			t.Fatal(err)
		}
		return nil
	}); err != berrors.ErrDatabaseNotOpen {
		t.Fatalf("unexpected error: %s", err)
	}
}

// Ensure a panic occurs while trying to commit a managed transaction.
func TestDB_Update_ManualCommit(t *testing.T) {
	db := btesting.MustCreateDB(t)

	var panicked bool
	if err := db.Update(func(tx *bolt.Tx) error {
		func() {
			defer func() {
				if r := recover(); r != nil {
					panicked = true
				}
			}()

			if err := tx.Commit(); err != nil {
				t.Fatal(err)
			}
		}()
		return nil
	}); err != nil {
		t.Fatal(err)
	} else if !panicked {
		t.Fatal("expected panic")
	}
}

// Ensure a panic occurs while trying to rollback a managed transaction.
func TestDB_Update_ManualRollback(t *testing.T) {
	db := btesting.MustCreateDB(t)

	var panicked bool
	if err := db.Update(func(tx *bolt.Tx) error {
		func() {
			defer func() {
				if r := recover(); r != nil {
					panicked = true
				}
			}()

			if err := tx.Rollback(); err != nil {
				t.Fatal(err)
			}
		}()
		return nil
	}); err != nil {
		t.Fatal(err)
	} else if !panicked {
		t.Fatal("expected panic")
	}
}

// Ensure a panic occurs while trying to commit a managed transaction.
func TestDB_View_ManualCommit(t *testing.T) {
	db := btesting.MustCreateDB(t)

	var panicked bool
	if err := db.View(func(tx *bolt.Tx) error {
		func() {
			defer func() {
				if r := recover(); r != nil {
					panicked = true
				}
			}()

			if err := tx.Commit(); err != nil {
				t.Fatal(err)
			}
		}()
		return nil
	}); err != nil {
		t.Fatal(err)
	} else if !panicked {
		t.Fatal("expected panic")
	}
}

// Ensure a panic occurs while trying to rollback a managed transaction.
func TestDB_View_ManualRollback(t *testing.T) {
	db := btesting.MustCreateDB(t)

	var panicked bool
	if err := db.View(func(tx *bolt.Tx) error {
		func() {
			defer func() {
				if r := recover(); r != nil {
					panicked = true
				}
			}()

			if err := tx.Rollback(); err != nil {
				t.Fatal(err)
			}
		}()
		return nil
	}); err != nil {
		t.Fatal(err)
	} else if !panicked {
		t.Fatal("expected panic")
	}
}

// Ensure a write transaction that panics does not hold open locks.
func TestDB_Update_Panic(t *testing.T) {
	db := btesting.MustCreateDB(t)

	// Panic during update but recover.
	func() {
		defer func() {
			if r := recover(); r != nil {
				t.Log("recover: update", r)
			}
		}()

		if err := db.Update(func(tx *bolt.Tx) error {
			if _, err := tx.CreateBucket([]byte("widgets")); err != nil {
				t.Fatal(err)
			}
			panic("omg")
		}); err != nil {
			t.Fatal(err)
		}
	}()

	// Verify we can update again.
	if err := db.Update(func(tx *bolt.Tx) error {
		if _, err := tx.CreateBucket([]byte("widgets")); err != nil {
			t.Fatal(err)
		}
		return nil
	}); err != nil {
		t.Fatal(err)
	}

	// Verify that our change persisted.
	if err := db.Update(func(tx *bolt.Tx) error {
		if tx.Bucket([]byte("widgets")) == nil {
			t.Fatal("expected bucket")
		}
		return nil
	}); err != nil {
		t.Fatal(err)
	}
}

// Ensure a database can return an error through a read-only transactional block.
func TestDB_View_Error(t *testing.T) {
	db := btesting.MustCreateDB(t)

	if err := db.View(func(tx *bolt.Tx) error {
		return errors.New("xxx")
	}); err == nil || err.Error() != "xxx" {
		t.Fatalf("unexpected error: %s", err)
	}
}

// Ensure a read transaction that panics does not hold open locks.
func TestDB_View_Panic(t *testing.T) {
	db := btesting.MustCreateDB(t)

	if err := db.Update(func(tx *bolt.Tx) error {
		if _, err := tx.CreateBucket([]byte("widgets")); err != nil {
			t.Fatal(err)
		}
		return nil
	}); err != nil {
		t.Fatal(err)
	}

	// Panic during view transaction but recover.
	func() {
		defer func() {
			if r := recover(); r != nil {
				t.Log("recover: view", r)
			}
		}()

		if err := db.View(func(tx *bolt.Tx) error {
			if tx.Bucket([]byte("widgets")) == nil {
				t.Fatal("expected bucket")
			}
			panic("omg")
		}); err != nil {
			t.Fatal(err)
		}
	}()

	// Verify that we can still use read transactions.
	if err := db.View(func(tx *bolt.Tx) error {
		if tx.Bucket([]byte("widgets")) == nil {
			t.Fatal("expected bucket")
		}
		return nil
	}); err != nil {
		t.Fatal(err)
	}
}

// Ensure that DB stats can be returned.
func TestDB_Stats(t *testing.T) {
	db := btesting.MustCreateDB(t)
	if err := db.Update(func(tx *bolt.Tx) error {
		_, err := tx.CreateBucket([]byte("widgets"))
		return err
	}); err != nil {
		t.Fatal(err)
	}

	stats := db.Stats()
	if stats.TxStats.GetPageCount() != 2 {
		t.Fatalf("unexpected TxStats.PageCount: %d", stats.TxStats.GetPageCount())
	} else if stats.FreePageN != 0 {
		t.Fatalf("unexpected FreePageN != 0: %d", stats.FreePageN)
	} else if stats.PendingPageN != 2 {
		t.Fatalf("unexpected PendingPageN != 2: %d", stats.PendingPageN)
	}
}

// Ensure that database pages are in expected order and type.
func TestDB_Consistency(t *testing.T) {
	db := btesting.MustCreateDB(t)
	if err := db.Update(func(tx *bolt.Tx) error {
		_, err := tx.CreateBucket([]byte("widgets"))
		return err
	}); err != nil {
		t.Fatal(err)
	}

	for i := 0; i < 10; i++ {
		if err := db.Update(func(tx *bolt.Tx) error {
			if err := tx.Bucket([]byte("widgets")).Put([]byte("foo"), []byte("bar")); err != nil {
				t.Fatal(err)
			}
			return nil
		}); err != nil {
			t.Fatal(err)
		}
	}

	if err := db.Update(func(tx *bolt.Tx) error {
		if p, _ := tx.Page(0); p == nil {
			t.Fatal("expected page")
		} else if p.Type != "meta" {
			t.Fatalf("unexpected page type: %s", p.Type)
		}

		if p, _ := tx.Page(1); p == nil {
			t.Fatal("expected page")
		} else if p.Type != "meta" {
			t.Fatalf("unexpected page type: %s", p.Type)
		}

		if p, _ := tx.Page(2); p == nil {
			t.Fatal("expected page")
		} else if p.Type != "free" {
			t.Fatalf("unexpected page type: %s", p.Type)
		}

		if p, _ := tx.Page(3); p == nil {
			t.Fatal("expected page")
		} else if p.Type != "free" {
			t.Fatalf("unexpected page type: %s", p.Type)
		}

		if p, _ := tx.Page(4); p == nil {
			t.Fatal("expected page")
		} else if p.Type != "leaf" {
			t.Fatalf("unexpected page type: %s", p.Type)
		}

		if p, _ := tx.Page(5); p == nil {
			t.Fatal("expected page")
		} else if p.Type != "freelist" {
			t.Fatalf("unexpected page type: %s", p.Type)
		}

		if p, _ := tx.Page(6); p != nil {
			t.Fatal("unexpected page")
		}
		return nil
	}); err != nil {
		t.Fatal(err)
	}
}

// Ensure that DB stats can be subtracted from one another.
func TestDBStats_Sub(t *testing.T) {
	var a, b bolt.Stats
	a.TxStats.PageCount = 3
	a.FreePageN = 4
	b.TxStats.PageCount = 10
	b.FreePageN = 14
	diff := b.Sub(&a)
	if diff.TxStats.GetPageCount() != 7 {
		t.Fatalf("unexpected TxStats.PageCount: %d", diff.TxStats.GetPageCount())
	}

	// free page stats are copied from the receiver and not subtracted
	if diff.FreePageN != 14 {
		t.Fatalf("unexpected FreePageN: %d", diff.FreePageN)
	}
}

// Ensure two functions can perform updates in a single batch.
func TestDB_Batch(t *testing.T) {
	db := btesting.MustCreateDB(t)

	if err := db.Update(func(tx *bolt.Tx) error {
		if _, err := tx.CreateBucket([]byte("widgets")); err != nil {
			t.Fatal(err)
		}
		return nil
	}); err != nil {
		t.Fatal(err)
	}

	// Iterate over multiple updates in separate goroutines.
	n := 2
	ch := make(chan error, n)
	for i := 0; i < n; i++ {
		go func(i int) {
			ch <- db.Batch(func(tx *bolt.Tx) error {
				return tx.Bucket([]byte("widgets")).Put(u64tob(uint64(i)), []byte{})
			})
		}(i)
	}

	// Check all responses to make sure there's no error.
	for i := 0; i < n; i++ {
		if err := <-ch; err != nil {
			t.Fatal(err)
		}
	}

	// Ensure data is correct.
	if err := db.View(func(tx *bolt.Tx) error {
		b := tx.Bucket([]byte("widgets"))
		for i := 0; i < n; i++ {
			if v := b.Get(u64tob(uint64(i))); v == nil {
				t.Errorf("key not found: %d", i)
			}
		}
		return nil
	}); err != nil {
		t.Fatal(err)
	}
}

func TestDB_Batch_Panic(t *testing.T) {
	db := btesting.MustCreateDB(t)

	var sentinel int
	var bork = &sentinel
	var problem interface{}
	var err error

	// Execute a function inside a batch that panics.
	func() {
		defer func() {
			if p := recover(); p != nil {
				problem = p
			}
		}()
		err = db.Batch(func(tx *bolt.Tx) error {
			panic(bork)
		})
	}()

	// Verify there is no error.
	if g, e := err, error(nil); g != e {
		t.Fatalf("wrong error: %v != %v", g, e)
	}
	// Verify the panic was captured.
	if g, e := problem, bork; g != e {
		t.Fatalf("wrong error: %v != %v", g, e)
	}
}

func TestDB_BatchFull(t *testing.T) {
	db := btesting.MustCreateDB(t)
	if err := db.Update(func(tx *bolt.Tx) error {
		_, err := tx.CreateBucket([]byte("widgets"))
		return err
	}); err != nil {
		t.Fatal(err)
	}

	const size = 3
	// buffered so we never leak goroutines
	ch := make(chan error, size)
	put := func(i int) {
		ch <- db.Batch(func(tx *bolt.Tx) error {
			return tx.Bucket([]byte("widgets")).Put(u64tob(uint64(i)), []byte{})
		})
	}

	db.MaxBatchSize = size
	// high enough to never trigger here
	db.MaxBatchDelay = 1 * time.Hour

	go put(1)
	go put(2)

	// Give the batch a chance to exhibit bugs.
	time.Sleep(10 * time.Millisecond)

	// not triggered yet
	select {
	case <-ch:
		t.Fatalf("batch triggered too early")
	default:
	}

	go put(3)

	// Check all responses to make sure there's no error.
	for i := 0; i < size; i++ {
		if err := <-ch; err != nil {
			t.Fatal(err)
		}
	}

	// Ensure data is correct.
	if err := db.View(func(tx *bolt.Tx) error {
		b := tx.Bucket([]byte("widgets"))
		for i := 1; i <= size; i++ {
			if v := b.Get(u64tob(uint64(i))); v == nil {
				t.Errorf("key not found: %d", i)
			}
		}
		return nil
	}); err != nil {
		t.Fatal(err)
	}
}

func TestDB_BatchTime(t *testing.T) {
	db := btesting.MustCreateDB(t)
	if err := db.Update(func(tx *bolt.Tx) error {
		_, err := tx.CreateBucket([]byte("widgets"))
		return err
	}); err != nil {
		t.Fatal(err)
	}

	const size = 1
	// buffered so we never leak goroutines
	ch := make(chan error, size)
	put := func(i int) {
		ch <- db.Batch(func(tx *bolt.Tx) error {
			return tx.Bucket([]byte("widgets")).Put(u64tob(uint64(i)), []byte{})
		})
	}

	db.MaxBatchSize = 1000
	db.MaxBatchDelay = 0

	go put(1)

	// Batch must trigger by time alone.

	// Check all responses to make sure there's no error.
	for i := 0; i < size; i++ {
		if err := <-ch; err != nil {
			t.Fatal(err)
		}
	}

	// Ensure data is correct.
	if err := db.View(func(tx *bolt.Tx) error {
		b := tx.Bucket([]byte("widgets"))
		for i := 1; i <= size; i++ {
			if v := b.Get(u64tob(uint64(i))); v == nil {
				t.Errorf("key not found: %d", i)
			}
		}
		return nil
	}); err != nil {
		t.Fatal(err)
	}
}

// TestDBUnmap verifes that `dataref`, `data` and `datasz` must be reset
// to zero values respectively after unmapping the db.
func TestDBUnmap(t *testing.T) {
	db := btesting.MustCreateDB(t)

	require.NoError(t, db.DB.Close())

	// Ignore the following error:
	// Error: copylocks: call of reflect.ValueOf copies lock value: go.etcd.io/bbolt.DB contains sync.Once contains sync.Mutex (govet)
	//nolint:govet
	v := reflect.ValueOf(*db.DB)
	dataref := v.FieldByName("dataref")
	data := v.FieldByName("data")
	datasz := v.FieldByName("datasz")
	assert.True(t, dataref.IsNil())
	assert.True(t, data.IsNil())
	assert.True(t, datasz.IsZero())

	// Set db.DB to nil to prevent MustCheck from panicking.
	db.DB = nil
}

// Convenience function for inserting a bunch of keys with 1000 byte values
func fillDBWithKeys(db *btesting.DB, numKeys int) error {
	return db.Fill([]byte("data"), 1, numKeys,
		func(tx int, k int) []byte { return []byte(fmt.Sprintf("%04d", k)) },
		func(tx int, k int) []byte { return make([]byte, 1000) },
	)
}

// Creates a new database size, forces a specific allocation size jump, and fills it with the number of keys specified
func createFilledDB(t testing.TB, o *bolt.Options, allocSize int, numKeys int) *btesting.DB {
	// Open a data file.
	db := btesting.MustCreateDBWithOption(t, o)
	db.AllocSize = allocSize

	// Insert a reasonable amount of data below the max size.
	err := db.Fill([]byte("data"), 1, numKeys,
		func(tx int, k int) []byte { return []byte(fmt.Sprintf("%04d", k)) },
		func(tx int, k int) []byte { return make([]byte, 1000) },
	)
	if err != nil {
		t.Fatal(err)
	}
	return db
}

// Ensure that a database cannot exceed its maximum size
// https://github.com/etcd-io/bbolt/issues/928
func TestDB_MaxSizeNotExceeded(t *testing.T) {
	testCases := []struct {
		name    string
		options bolt.Options
	}{
		{
			name: "Standard case",
			options: bolt.Options{
				MaxSize:  5 * 1024 * 1024, // 5 MiB
				PageSize: 4096,
			},
		},
		{
			name: "NoGrowSync",
			options: bolt.Options{
				MaxSize:    5 * 1024 * 1024, // 5 MiB
				PageSize:   4096,
				NoGrowSync: true,
			},
		},
	}

	for _, testCase := range testCases {
		t.Run(testCase.name, func(t *testing.T) {
			db := createFilledDB(t,
				&testCase.options,
				4*1024*1024, // adjust allocation jumps to 4 MiB
				2000,
			)

			path := db.Path()

			// The data file should be 4 MiB now (expanded once from zero).
			// It should have space for roughly 16 more entries before trying to grow
			// Keep inserting until grow is required
			err := fillDBWithKeys(db, 100)
			assert.ErrorIs(t, err, berrors.ErrMaxSizeReached)

			newSz := fileSize(path)
			require.Greater(t, newSz, int64(0), "unexpected new file size: %d", newSz)
			assert.LessOrEqual(t, newSz, int64(db.MaxSize), "The size of the data file should not exceed db.MaxSize")

			err = db.Close()
			require.NoError(t, err, "Closing the re-opened database should succeed")
		})
	}
}

// Ensure that opening a database that is beyond the maximum size succeeds
// The maximum size should only apply to growing the data file
// https://github.com/etcd-io/bbolt/issues/928
func TestDB_MaxSizeExceededCanOpen(t *testing.T) {
	// Open a data file.
	db := createFilledDB(t, nil, 4*1024*1024, 2000) // adjust allocation jumps to 4 MiB, fill with 2000, 1KB keys
	path := db.Path()

	// Insert a reasonable amount of data below the max size.
	err := fillDBWithKeys(db, 2000)
	require.NoError(t, err, "fillDbWithKeys should succeed")

	err = db.Close()
	require.NoError(t, err, "Close should succeed")

	// The data file should be 4 MiB now (expanded once from zero).
	minimumSizeForTest := int64(1024 * 1024)
	newSz := fileSize(path)
	require.GreaterOrEqual(t, newSz, minimumSizeForTest, "unexpected new file size: %d. Expected at least %d", newSz, minimumSizeForTest)

	// Now try to re-open the database with an extremely small max size
	t.Logf("Reopening bbolt DB at: %s", path)
	db, err = btesting.OpenDBWithOption(t, path, &bolt.Options{
		MaxSize: 1,
	})
	assert.NoError(t, err, "Should be able to open database bigger than MaxSize")

	err = db.Close()
	require.NoError(t, err, "Closing the re-opened database should succeed")
}

// Ensure that opening a database that is beyond the maximum size succeeds,
// even when InitialMmapSize is above the limit (mmaps should not affect file size)
// This test exists for platforms where Truncate should not be called during mmap
// https://github.com/etcd-io/bbolt/issues/928
func TestDB_MaxSizeExceededCanOpenWithHighMmap(t *testing.T) {
	if runtime.GOOS == "windows" {
		// In Windows, the file must be expanded to the mmap initial size,
		// so this test doesn't run in Windows.
		t.SkipNow()
	}

	// Open a data file.
	db := createFilledDB(t, nil, 4*1024*1024, 2000) // adjust allocation jumps to 4 MiB, fill with 2000 1KB entries
	path := db.Path()

	err := db.Close()
	require.NoError(t, err, "Close should succeed")

	// The data file should be 4 MiB now (expanded once from zero).
	minimumSizeForTest := int64(1024 * 1024)
	newSz := fileSize(path)
	require.GreaterOrEqual(t, newSz, minimumSizeForTest, "unexpected new file size: %d. Expected at least %d", newSz, minimumSizeForTest)

	// Now try to re-open the database with an extremely small max size
	t.Logf("Reopening bbolt DB at: %s", path)
	db, err = btesting.OpenDBWithOption(t, path, &bolt.Options{
		MaxSize:         1,
		InitialMmapSize: int(minimumSizeForTest) * 2,
	})
	assert.NoError(t, err, "Should be able to open database bigger than MaxSize when InitialMmapSize set high")

	err = db.Close()
	require.NoError(t, err, "Closing the re-opened database should succeed")
}

// Ensure that when InitialMmapSize is above the limit, opening a database
// that is beyond the maximum size fails in Windows.
// In Windows, the file must be expanded to the mmap initial size.
// https://github.com/etcd-io/bbolt/issues/928
func TestDB_MaxSizeExceededDoesNotGrow(t *testing.T) {
	if runtime.GOOS != "windows" {
		// This test is only relevant on Windows
		t.SkipNow()
	}

	// Open a data file.
	db := createFilledDB(t, nil, 4*1024*1024, 2000) // adjust allocation jumps to 4 MiB, fill with 2000 1KB entries
	path := db.Path()

	err := db.Close()
	require.NoError(t, err, "Close should succeed")

	// The data file should be 4 MiB now (expanded once from zero).
	minimumSizeForTest := int64(1024 * 1024)
	newSz := fileSize(path)
	assert.GreaterOrEqual(t, newSz, minimumSizeForTest, "unexpected new file size: %d. Expected at least %d", newSz, minimumSizeForTest)

	// Now try to re-open the database with an extremely small max size and
	// an initial mmap size to be greater than the actual file size, forcing an illegal grow on open
	t.Logf("Reopening bbolt DB at: %s", path)
	_, err = btesting.OpenDBWithOption(t, path, &bolt.Options{
		MaxSize:         1,
		InitialMmapSize: int(newSz) * 2,
	})
	assert.Error(t, err, "Opening the DB with InitialMmapSize > MaxSize should cause an error on Windows")
}

func TestDB_HugeValue(t *testing.T) {
	dbPath := filepath.Join(t.TempDir(), "db")
	db, err := bolt.Open(dbPath, 0600, nil)
	require.NoError(t, err)
	defer func() {
		require.NoError(t, db.Close())
	}()

	maxSize := 0xFFFFFFF + 1
	// On 32 bit systems, the MaxAllocSize is 0xFFFFFFF (268435455,
	// roughly 256MB), and the test will fail for sure, so we reduce
	// the maxSize by half in such case.
	if maxSize > common.MaxAllocSize {
		maxSize = maxSize / 2
	}
	data := make([]byte, maxSize)

	_ = db.Update(func(tx *bolt.Tx) error {
		b, err := tx.CreateBucketIfNotExists([]byte("data"))
		require.NoError(t, err)

		err = b.Put([]byte("key"), data)
		require.NoError(t, err)

		return nil
	})
}

func ExampleDB_Update() {
	// Open the database.
	db, err := bolt.Open(tempfile(), 0600, nil)
	if err != nil {
		log.Fatal(err)
	}
	defer os.Remove(db.Path())

	// Execute several commands within a read-write transaction.
	if err := db.Update(func(tx *bolt.Tx) error {
		b, err := tx.CreateBucket([]byte("widgets"))
		if err != nil {
			return err
		}
		if err := b.Put([]byte("foo"), []byte("bar")); err != nil {
			return err
		}
		return nil
	}); err != nil {
		log.Fatal(err)
	}

	// Read the value back from a separate read-only transaction.
	if err := db.View(func(tx *bolt.Tx) error {
		value := tx.Bucket([]byte("widgets")).Get([]byte("foo"))
		fmt.Printf("The value of 'foo' is: %s\n", value)
		return nil
	}); err != nil {
		log.Fatal(err)
	}

	// Close database to release the file lock.
	if err := db.Close(); err != nil {
		log.Fatal(err)
	}

	// Output:
	// The value of 'foo' is: bar
}

func ExampleDB_View() {
	// Open the database.
	db, err := bolt.Open(tempfile(), 0600, nil)
	if err != nil {
		log.Fatal(err)
	}
	defer os.Remove(db.Path())

	// Insert data into a bucket.
	if err := db.Update(func(tx *bolt.Tx) error {
		b, err := tx.CreateBucket([]byte("people"))
		if err != nil {
			return err
		}
		if err := b.Put([]byte("john"), []byte("doe")); err != nil {
			return err
		}
		if err := b.Put([]byte("susy"), []byte("que")); err != nil {
			return err
		}
		return nil
	}); err != nil {
		log.Fatal(err)
	}

	// Access data from within a read-only transactional block.
	if err := db.View(func(tx *bolt.Tx) error {
		v := tx.Bucket([]byte("people")).Get([]byte("john"))
		fmt.Printf("John's last name is %s.\n", v)
		return nil
	}); err != nil {
		log.Fatal(err)
	}

	// Close database to release the file lock.
	if err := db.Close(); err != nil {
		log.Fatal(err)
	}

	// Output:
	// John's last name is doe.
}

func ExampleDB_Begin() {
	// Open the database.
	db, err := bolt.Open(tempfile(), 0600, nil)
	if err != nil {
		log.Fatal(err)
	}
	defer os.Remove(db.Path())

	// Create a bucket using a read-write transaction.
	if err = db.Update(func(tx *bolt.Tx) error {
		_, err := tx.CreateBucket([]byte("widgets"))
		return err
	}); err != nil {
		log.Fatal(err)
	}

	// Create several keys in a transaction.
	tx, err := db.Begin(true)
	if err != nil {
		log.Fatal(err)
	}
	b := tx.Bucket([]byte("widgets"))
	if err = b.Put([]byte("john"), []byte("blue")); err != nil {
		log.Fatal(err)
	}
	if err = b.Put([]byte("abby"), []byte("red")); err != nil {
		log.Fatal(err)
	}
	if err = b.Put([]byte("zephyr"), []byte("purple")); err != nil {
		log.Fatal(err)
	}
	if err = tx.Commit(); err != nil {
		log.Fatal(err)
	}

	// Iterate over the values in sorted key order.
	tx, err = db.Begin(false)
	if err != nil {
		log.Fatal(err)
	}
	c := tx.Bucket([]byte("widgets")).Cursor()
	for k, v := c.First(); k != nil; k, v = c.Next() {
		fmt.Printf("%s likes %s\n", k, v)
	}

	if err = tx.Rollback(); err != nil {
		log.Fatal(err)
	}

	if err = db.Close(); err != nil {
		log.Fatal(err)
	}

	// Output:
	// abby likes red
	// john likes blue
	// zephyr likes purple
}

func BenchmarkDBBatchAutomatic(b *testing.B) {
	db := btesting.MustCreateDB(b)

	if err := db.Update(func(tx *bolt.Tx) error {
		_, err := tx.CreateBucket([]byte("bench"))
		return err
	}); err != nil {
		b.Fatal(err)
	}

	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		start := make(chan struct{})
		var wg sync.WaitGroup

		for round := 0; round < 1000; round++ {
			wg.Add(1)

			go func(id uint32) {
				defer wg.Done()
				<-start

				h := fnv.New32a()
				buf := make([]byte, 4)
				binary.LittleEndian.PutUint32(buf, id)
				_, _ = h.Write(buf[:])
				k := h.Sum(nil)
				insert := func(tx *bolt.Tx) error {
					b := tx.Bucket([]byte("bench"))
					return b.Put(k, []byte("filler"))
				}
				if err := db.Batch(insert); err != nil {
					b.Error(err)
					return
				}
			}(uint32(round))
		}
		close(start)
		wg.Wait()
	}

	b.StopTimer()
	validateBatchBench(b, db)
}

func BenchmarkDBBatchSingle(b *testing.B) {
	db := btesting.MustCreateDB(b)
	if err := db.Update(func(tx *bolt.Tx) error {
		_, err := tx.CreateBucket([]byte("bench"))
		return err
	}); err != nil {
		b.Fatal(err)
	}

	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		start := make(chan struct{})
		var wg sync.WaitGroup

		for round := 0; round < 1000; round++ {
			wg.Add(1)
			go func(id uint32) {
				defer wg.Done()
				<-start

				h := fnv.New32a()
				buf := make([]byte, 4)
				binary.LittleEndian.PutUint32(buf, id)
				_, _ = h.Write(buf[:])
				k := h.Sum(nil)
				insert := func(tx *bolt.Tx) error {
					b := tx.Bucket([]byte("bench"))
					return b.Put(k, []byte("filler"))
				}
				if err := db.Update(insert); err != nil {
					b.Error(err)
					return
				}
			}(uint32(round))
		}
		close(start)
		wg.Wait()
	}

	b.StopTimer()
	validateBatchBench(b, db)
}

func BenchmarkDBBatchManual10x100(b *testing.B) {
	db := btesting.MustCreateDB(b)
	if err := db.Update(func(tx *bolt.Tx) error {
		_, err := tx.CreateBucket([]byte("bench"))
		return err
	}); err != nil {
		b.Fatal(err)
	}

	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		start := make(chan struct{})
		var wg sync.WaitGroup
		errCh := make(chan error, 10)

		for major := 0; major < 10; major++ {
			wg.Add(1)
			go func(id uint32) {
				defer wg.Done()
				<-start

				insert100 := func(tx *bolt.Tx) error {
					h := fnv.New32a()
					buf := make([]byte, 4)
					for minor := uint32(0); minor < 100; minor++ {
						binary.LittleEndian.PutUint32(buf, uint32(id*100+minor))
						h.Reset()
						_, _ = h.Write(buf[:])
						k := h.Sum(nil)
						b := tx.Bucket([]byte("bench"))
						if err := b.Put(k, []byte("filler")); err != nil {
							return err
						}
					}
					return nil
				}
				err := db.Update(insert100)
				errCh <- err
			}(uint32(major))
		}
		close(start)
		wg.Wait()
		close(errCh)
		for err := range errCh {
			if err != nil {
				b.Fatal(err)
			}
		}
	}

	b.StopTimer()
	validateBatchBench(b, db)
}

func validateBatchBench(b *testing.B, db *btesting.DB) {
	var rollback = errors.New("sentinel error to cause rollback")
	validate := func(tx *bolt.Tx) error {
		bucket := tx.Bucket([]byte("bench"))
		h := fnv.New32a()
		buf := make([]byte, 4)
		for id := uint32(0); id < 1000; id++ {
			binary.LittleEndian.PutUint32(buf, id)
			h.Reset()
			_, _ = h.Write(buf[:])
			k := h.Sum(nil)
			v := bucket.Get(k)
			if v == nil {
				b.Errorf("not found id=%d key=%x", id, k)
				continue
			}
			if g, e := v, []byte("filler"); !bytes.Equal(g, e) {
				b.Errorf("bad value for id=%d key=%x: %s != %q", id, k, g, e)
			}
			if err := bucket.Delete(k); err != nil {
				return err
			}
		}
		// should be empty now
		c := bucket.Cursor()
		for k, v := c.First(); k != nil; k, v = c.Next() {
			b.Errorf("unexpected key: %x = %q", k, v)
		}
		return rollback
	}
	if err := db.Update(validate); err != nil && err != rollback {
		b.Error(err)
	}
}

// tempfile returns a temporary file path.
func tempfile() string {
	f, err := os.CreateTemp("", "bolt-")
	if err != nil {
		panic(err)
	}
	if err := f.Close(); err != nil {
		panic(err)
	}
	if err := os.Remove(f.Name()); err != nil {
		panic(err)
	}
	return f.Name()
}

func trunc(b []byte, length int) []byte {
	if length < len(b) {
		return b[:length]
	}
	return b
}

func fileSize(path string) int64 {
	fi, err := os.Stat(path)
	if err != nil {
		return 0
	}
	return fi.Size()
}

// u64tob converts a uint64 into an 8-byte slice.
func u64tob(v uint64) []byte {
	b := make([]byte, 8)
	binary.BigEndian.PutUint64(b, v)
	return b
}
```

## File: `db_whitebox_test.go`
```go
package bbolt

import (
	"path/filepath"
	"testing"

	"github.com/stretchr/testify/assert"
	"github.com/stretchr/testify/require"

	"go.etcd.io/bbolt/errors"
)

func TestOpenWithPreLoadFreelist(t *testing.T) {
	testCases := []struct {
		name                    string
		readonly                bool
		preLoadFreePage         bool
		expectedFreePagesLoaded bool
	}{
		{
			name:                    "write mode always load free pages",
			readonly:                false,
			preLoadFreePage:         false,
			expectedFreePagesLoaded: true,
		},
		{
			name:                    "readonly mode load free pages when flag set",
			readonly:                true,
			preLoadFreePage:         true,
			expectedFreePagesLoaded: true,
		},
		{
			name:                    "readonly mode doesn't load free pages when flag not set",
			readonly:                true,
			preLoadFreePage:         false,
			expectedFreePagesLoaded: false,
		},
	}

	fileName, err := prepareData(t)
	require.NoError(t, err)

	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			db, err := Open(fileName, 0666, &Options{
				ReadOnly:        tc.readonly,
				PreLoadFreelist: tc.preLoadFreePage,
			})
			require.NoError(t, err)

			assert.Equal(t, tc.expectedFreePagesLoaded, db.freelist != nil)

			assert.NoError(t, db.Close())
		})
	}
}

func TestMethodPage(t *testing.T) {
	testCases := []struct {
		name            string
		readonly        bool
		preLoadFreePage bool
		expectedError   error
	}{
		{
			name:            "write mode",
			readonly:        false,
			preLoadFreePage: false,
			expectedError:   nil,
		},
		{
			name:            "readonly mode with preloading free pages",
			readonly:        true,
			preLoadFreePage: true,
			expectedError:   nil,
		},
		{
			name:            "readonly mode without preloading free pages",
			readonly:        true,
			preLoadFreePage: false,
			expectedError:   errors.ErrFreePagesNotLoaded,
		},
	}

	fileName, err := prepareData(t)
	require.NoError(t, err)

	for _, tc := range testCases {
		tc := tc
		t.Run(tc.name, func(t *testing.T) {
			db, err := Open(fileName, 0666, &Options{
				ReadOnly:        tc.readonly,
				PreLoadFreelist: tc.preLoadFreePage,
			})
			require.NoError(t, err)
			defer db.Close()

			tx, err := db.Begin(!tc.readonly)
			require.NoError(t, err)

			_, err = tx.Page(0)
			require.Equal(t, tc.expectedError, err)

			if tc.readonly {
				require.NoError(t, tx.Rollback())
			} else {
				require.NoError(t, tx.Commit())
			}

			require.NoError(t, db.Close())
		})
	}
}

func prepareData(t *testing.T) (string, error) {
	fileName := filepath.Join(t.TempDir(), "db")
	db, err := Open(fileName, 0666, nil)
	if err != nil {
		return "", err
	}
	if err := db.Close(); err != nil {
		return "", err
	}

	return fileName, nil
}
```

## File: `doc.go`
```go
/*
package bbolt implements a low-level key/value store in pure Go. It supports
fully serializable transactions, ACID semantics, and lock-free MVCC with
multiple readers and a single writer. Bolt can be used for projects that
want a simple data store without the need to add large dependencies such as
Postgres or MySQL.

Bolt is a single-level, zero-copy, B+tree data store. This means that Bolt is
optimized for fast read access and does not require recovery in the event of a
system crash. Transactions which have not finished committing will simply be
rolled back in the event of a crash.

The design of Bolt is based on Howard Chu's LMDB database project.

Bolt currently works on Windows, Mac OS X, and Linux.

# Basics

There are only a few types in Bolt: DB, Bucket, Tx, and Cursor. The DB is
a collection of buckets and is represented by a single file on disk. A bucket is
a collection of unique keys that are associated with values.

Transactions provide either read-only or read-write access to the database.
Read-only transactions can retrieve key/value pairs and can use Cursors to
iterate over the dataset sequentially. Read-write transactions can create and
delete buckets and can insert and remove keys. Only one read-write transaction
is allowed at a time.

# Caveats

The database uses a read-only, memory-mapped data file to ensure that
applications cannot corrupt the database, however, this means that keys and
values returned from Bolt cannot be changed. Writing to a read-only byte slice
will cause Go to panic.

Keys and values retrieved from the database are only valid for the life of
the transaction. When used outside the transaction, these byte slices can
point to different data or can point to invalid memory which will cause a panic.
*/
package bbolt
```

## File: `errors.go`
```go
package bbolt

import "go.etcd.io/bbolt/errors"

// These errors can be returned when opening or calling methods on a DB.
var (
	// ErrDatabaseNotOpen is returned when a DB instance is accessed before it
	// is opened or after it is closed.
	//
	// Deprecated: Use the error variables defined in the bbolt/errors package.
	ErrDatabaseNotOpen = errors.ErrDatabaseNotOpen

	// ErrInvalid is returned when both meta pages on a database are invalid.
	// This typically occurs when a file is not a bolt database.
	//
	// Deprecated: Use the error variables defined in the bbolt/errors package.
	ErrInvalid = errors.ErrInvalid

	// ErrInvalidMapping is returned when the database file fails to get mapped.
	//
	// Deprecated: Use the error variables defined in the bbolt/errors package.
	ErrInvalidMapping = errors.ErrInvalidMapping

	// ErrVersionMismatch is returned when the data file was created with a
	// different version of Bolt.
	//
	// Deprecated: Use the error variables defined in the bbolt/errors package.
	ErrVersionMismatch = errors.ErrVersionMismatch

	// ErrChecksum is returned when a checksum mismatch occurs on either of the two meta pages.
	//
	// Deprecated: Use the error variables defined in the bbolt/errors package.
	ErrChecksum = errors.ErrChecksum

	// ErrTimeout is returned when a database cannot obtain an exclusive lock
	// on the data file after the timeout passed to Open().
	//
	// Deprecated: Use the error variables defined in the bbolt/errors package.
	ErrTimeout = errors.ErrTimeout
)

// These errors can occur when beginning or committing a Tx.
var (
	// ErrTxNotWritable is returned when performing a write operation on a
	// read-only transaction.
	//
	// Deprecated: Use the error variables defined in the bbolt/errors package.
	ErrTxNotWritable = errors.ErrTxNotWritable

	// ErrTxClosed is returned when committing or rolling back a transaction
	// that has already been committed or rolled back.
	//
	// Deprecated: Use the error variables defined in the bbolt/errors package.
	ErrTxClosed = errors.ErrTxClosed

	// ErrDatabaseReadOnly is returned when a mutating transaction is started on a
	// read-only database.
	//
	// Deprecated: Use the error variables defined in the bbolt/errors package.
	ErrDatabaseReadOnly = errors.ErrDatabaseReadOnly

	// ErrFreePagesNotLoaded is returned when a readonly transaction without
	// preloading the free pages is trying to access the free pages.
	//
	// Deprecated: Use the error variables defined in the bbolt/errors package.
	ErrFreePagesNotLoaded = errors.ErrFreePagesNotLoaded
)

// These errors can occur when putting or deleting a value or a bucket.
var (
	// ErrBucketNotFound is returned when trying to access a bucket that has
	// not been created yet.
	//
	// Deprecated: Use the error variables defined in the bbolt/errors package.
	ErrBucketNotFound = errors.ErrBucketNotFound

	// ErrBucketExists is returned when creating a bucket that already exists.
	//
	// Deprecated: Use the error variables defined in the bbolt/errors package.
	ErrBucketExists = errors.ErrBucketExists

	// ErrBucketNameRequired is returned when creating a bucket with a blank name.
	//
	// Deprecated: Use the error variables defined in the bbolt/errors package.
	ErrBucketNameRequired = errors.ErrBucketNameRequired

	// ErrKeyRequired is returned when inserting a zero-length key.
	//
	// Deprecated: Use the error variables defined in the bbolt/errors package.
	ErrKeyRequired = errors.ErrKeyRequired

	// ErrKeyTooLarge is returned when inserting a key that is larger than MaxKeySize.
	//
	// Deprecated: Use the error variables defined in the bbolt/errors package.
	ErrKeyTooLarge = errors.ErrKeyTooLarge

	// ErrValueTooLarge is returned when inserting a value that is larger than MaxValueSize.
	//
	// Deprecated: Use the error variables defined in the bbolt/errors package.
	ErrValueTooLarge = errors.ErrValueTooLarge

	// ErrIncompatibleValue is returned when trying create or delete a bucket
	// on an existing non-bucket key or when trying to create or delete a
	// non-bucket key on an existing bucket key.
	//
	// Deprecated: Use the error variables defined in the bbolt/errors package.
	ErrIncompatibleValue = errors.ErrIncompatibleValue
)
```

## File: `go.mod`
```
module go.etcd.io/bbolt

go 1.25.0

toolchain go1.25.8

require (
	github.com/spf13/cobra v1.10.2
	github.com/spf13/pflag v1.0.10
	github.com/stretchr/testify v1.11.1
	go.etcd.io/gofail v0.2.0
	golang.org/x/sync v0.20.0
	golang.org/x/sys v0.42.0
)

require (
	github.com/aclements/go-moremath v0.0.0-20210112150236-f10218a38794 // indirect
	github.com/davecgh/go-spew v1.1.1 // indirect
	github.com/inconshreveable/mousetrap v1.1.0 // indirect
	github.com/pmezard/go-difflib v1.0.0 // indirect
	golang.org/x/mod v0.27.0 // indirect
	golang.org/x/perf v0.0.0-20250813145418-2f7363a06fe1 // indirect
	golang.org/x/tools v0.36.0 // indirect
	gopkg.in/yaml.v3 v3.0.1 // indirect
)

tool (
	go.etcd.io/gofail
	golang.org/x/perf/cmd/benchstat
	golang.org/x/tools/cmd/goimports
)
```

## File: `go.sum`
```
github.com/aclements/go-moremath v0.0.0-20210112150236-f10218a38794 h1:xlwdaKcTNVW4PtpQb8aKA4Pjy0CdJHEqvFbAnvR5m2g=
github.com/aclements/go-moremath v0.0.0-20210112150236-f10218a38794/go.mod h1:7e+I0LQFUI9AXWxOfsQROs9xPhoJtbsyWcjJqDd4KPY=
github.com/cpuguy83/go-md2man/v2 v2.0.6/go.mod h1:oOW0eioCTA6cOiMLiUPZOpcVxMig6NIQQ7OS05n1F4g=
github.com/davecgh/go-spew v1.1.1 h1:vj9j/u1bqnvCEfJOwUhtlOARqs3+rkHYY13jYWTU97c=
github.com/davecgh/go-spew v1.1.1/go.mod h1:J7Y8YcW2NihsgmVo/mv3lAwl/skON4iLHjSsI+c5H38=
github.com/google/go-cmp v0.6.0 h1:ofyhxvXcZhMsU5ulbFiLKl/XBFqE1GSq7atu8tAmTRI=
github.com/google/go-cmp v0.6.0/go.mod h1:17dUlkBOakJ0+DkrSSNjCkIjxS6bF9zb3elmeNGIjoY=
github.com/inconshreveable/mousetrap v1.1.0 h1:wN+x4NVGpMsO7ErUn/mUI3vEoE6Jt13X2s0bqwp9tc8=
github.com/inconshreveable/mousetrap v1.1.0/go.mod h1:vpF70FUmC8bwa3OWnCshd2FqLfsEA9PFc4w1p2J65bw=
github.com/pmezard/go-difflib v1.0.0 h1:4DBwDE0NGyQoBHbLQYPwSUPoCMWR5BEzIk/f1lZbAQM=
github.com/pmezard/go-difflib v1.0.0/go.mod h1:iKH77koFhYxTK1pcRnkKkqfTogsbg7gZNVY4sRDYZ/4=
github.com/russross/blackfriday/v2 v2.1.0/go.mod h1:+Rmxgy9KzJVeS9/2gXHxylqXiyQDYRxCVz55jmeOWTM=
github.com/spf13/cobra v1.10.2 h1:DMTTonx5m65Ic0GOoRY2c16WCbHxOOw6xxezuLaBpcU=
github.com/spf13/cobra v1.10.2/go.mod h1:7C1pvHqHw5A4vrJfjNwvOdzYu0Gml16OCs2GRiTUUS4=
github.com/spf13/pflag v1.0.9/go.mod h1:McXfInJRrz4CZXVZOBLb0bTZqETkiAhM9Iw0y3An2Bg=
github.com/spf13/pflag v1.0.10 h1:4EBh2KAYBwaONj6b2Ye1GiHfwjqyROoF4RwYO+vPwFk=
github.com/spf13/pflag v1.0.10/go.mod h1:McXfInJRrz4CZXVZOBLb0bTZqETkiAhM9Iw0y3An2Bg=
github.com/stretchr/testify v1.11.1 h1:7s2iGBzp5EwR7/aIZr8ao5+dra3wiQyKjjFuvgVKu7U=
github.com/stretchr/testify v1.11.1/go.mod h1:wZwfW3scLgRK+23gO65QZefKpKQRnfz6sD981Nm4B6U=
go.etcd.io/gofail v0.2.0 h1:p19drv16FKK345a09a1iubchlw/vmRuksmRzgBIGjcA=
go.etcd.io/gofail v0.2.0/go.mod h1:nL3ILMGfkXTekKI3clMBNazKnjUZjYLKmBHzsVAnC1o=
go.yaml.in/yaml/v3 v3.0.4/go.mod h1:DhzuOOF2ATzADvBadXxruRBLzYTpT36CKvDb3+aBEFg=
golang.org/x/mod v0.27.0 h1:kb+q2PyFnEADO2IEF935ehFUXlWiNjJWtRNgBLSfbxQ=
golang.org/x/mod v0.27.0/go.mod h1:rWI627Fq0DEoudcK+MBkNkCe0EetEaDSwJJkCcjpazc=
golang.org/x/perf v0.0.0-20250813145418-2f7363a06fe1 h1:stGRioFgvBd3x8HoGVg9bb41lLTWLjBMFT/dMB7f4mQ=
golang.org/x/perf v0.0.0-20250813145418-2f7363a06fe1/go.mod h1:rjfRjhHXb3XNVh/9i5Jr2tXoTd0vOlZN5rzsM8cQE6k=
golang.org/x/sync v0.20.0 h1:e0PTpb7pjO8GAtTs2dQ6jYa5BWYlMuX047Dco/pItO4=
golang.org/x/sync v0.20.0/go.mod h1:9xrNwdLfx4jkKbNva9FpL6vEN7evnE43NNNJQ2LF3+0=
golang.org/x/sys v0.42.0 h1:omrd2nAlyT5ESRdCLYdm3+fMfNFE/+Rf4bDIQImRJeo=
golang.org/x/sys v0.42.0/go.mod h1:4GL1E5IUh+htKOUEOaiffhrAeqysfVGipDYzABqnCmw=
golang.org/x/tools v0.36.0 h1:kWS0uv/zsvHEle1LbV5LE8QujrxB3wfQyxHfhOk0Qkg=
golang.org/x/tools v0.36.0/go.mod h1:WBDiHKJK8YgLHlcQPYQzNCkUxUypCaa5ZegCVutKm+s=
gopkg.in/check.v1 v0.0.0-20161208181325-20d25e280405 h1:yhCVgyC4o1eVCa2tZl7eS0r+SDo693bJlVdllGtEeKM=
gopkg.in/check.v1 v0.0.0-20161208181325-20d25e280405/go.mod h1:Co6ibVJAznAaIkqp8huTwlJQCZ016jof/cbN4VW5Yz0=
gopkg.in/yaml.v3 v3.0.1 h1:fxVm/GzAzEWqLHuvctI91KS9hhNmmWOoWu0XTYJS7CA=
gopkg.in/yaml.v3 v3.0.1/go.mod h1:K4uyk7z7BCEPqu6E+C64Yfv1cQ7kz7rIZviUmN+EgEM=
```

## File: `logger.go`
```go
package bbolt

// See https://github.com/etcd-io/raft/blob/main/logger.go
import (
	"fmt"
	"io"
	"log"
	"os"
)

type Logger interface {
	Debug(v ...interface{})
	Debugf(format string, v ...interface{})

	Error(v ...interface{})
	Errorf(format string, v ...interface{})

	Info(v ...interface{})
	Infof(format string, v ...interface{})

	Warning(v ...interface{})
	Warningf(format string, v ...interface{})

	Fatal(v ...interface{})
	Fatalf(format string, v ...interface{})

	Panic(v ...interface{})
	Panicf(format string, v ...interface{})
}

func getDiscardLogger() Logger {
	return discardLogger
}

var (
	discardLogger = &DefaultLogger{Logger: log.New(io.Discard, "", 0)}
)

const (
	calldepth = 2
)

// DefaultLogger is a default implementation of the Logger interface.
type DefaultLogger struct {
	*log.Logger
	debug bool
}

func (l *DefaultLogger) EnableTimestamps() {
	l.SetFlags(l.Flags() | log.Ldate | log.Ltime)
}

func (l *DefaultLogger) EnableDebug() {
	l.debug = true
}

func (l *DefaultLogger) Debug(v ...interface{}) {
	if l.debug {
		_ = l.Output(calldepth, header("DEBUG", fmt.Sprint(v...)))
	}
}

func (l *DefaultLogger) Debugf(format string, v ...interface{}) {
	if l.debug {
		_ = l.Output(calldepth, header("DEBUG", fmt.Sprintf(format, v...)))
	}
}

func (l *DefaultLogger) Info(v ...interface{}) {
	_ = l.Output(calldepth, header("INFO", fmt.Sprint(v...)))
}

func (l *DefaultLogger) Infof(format string, v ...interface{}) {
	_ = l.Output(calldepth, header("INFO", fmt.Sprintf(format, v...)))
}

func (l *DefaultLogger) Error(v ...interface{}) {
	_ = l.Output(calldepth, header("ERROR", fmt.Sprint(v...)))
}

func (l *DefaultLogger) Errorf(format string, v ...interface{}) {
	_ = l.Output(calldepth, header("ERROR", fmt.Sprintf(format, v...)))
}

func (l *DefaultLogger) Warning(v ...interface{}) {
	_ = l.Output(calldepth, header("WARN", fmt.Sprint(v...)))
}

func (l *DefaultLogger) Warningf(format string, v ...interface{}) {
	_ = l.Output(calldepth, header("WARN", fmt.Sprintf(format, v...)))
}

func (l *DefaultLogger) Fatal(v ...interface{}) {
	_ = l.Output(calldepth, header("FATAL", fmt.Sprint(v...)))
	os.Exit(1)
}

func (l *DefaultLogger) Fatalf(format string, v ...interface{}) {
	_ = l.Output(calldepth, header("FATAL", fmt.Sprintf(format, v...)))
	os.Exit(1)
}

func (l *DefaultLogger) Panic(v ...interface{}) {
	l.Logger.Panic(v...)
}

func (l *DefaultLogger) Panicf(format string, v ...interface{}) {
	l.Logger.Panicf(format, v...)
}

func header(lvl, msg string) string {
	return fmt.Sprintf("%s: %s", lvl, msg)
}
```

## File: `manydbs_test.go`
```go
package bbolt

import (
	"crypto/rand"
	"fmt"
	"os"
	"path/filepath"
	"testing"
)

func createDb(t *testing.T) (*DB, func()) {
	// First, create a temporary directory to be used for the duration of
	// this test.
	tempDirName, err := os.MkdirTemp("", "bboltmemtest")
	if err != nil {
		t.Fatalf("error creating temp dir: %v", err)
	}
	path := filepath.Join(tempDirName, "testdb.db")

	bdb, err := Open(path, 0600, nil)
	if err != nil {
		t.Fatalf("error creating bbolt db: %v", err)
	}

	cleanup := func() {
		bdb.Close()
		os.RemoveAll(tempDirName)
	}

	return bdb, cleanup
}

func createAndPutKeys(t *testing.T) {
	t.Parallel()

	db, cleanup := createDb(t)
	defer cleanup()

	bucketName := []byte("bucket")

	for i := 0; i < 100; i++ {
		err := db.Update(func(tx *Tx) error {
			nodes, err := tx.CreateBucketIfNotExists(bucketName)
			if err != nil {
				return err
			}

			var key [16]byte
			_, rerr := rand.Read(key[:])
			if rerr != nil {
				return rerr
			}
			if err := nodes.Put(key[:], nil); err != nil {
				return err
			}

			return nil
		})
		if err != nil {
			t.Fatal(err)
		}
	}
}

func TestManyDBs(t *testing.T) {
	if testing.Short() {
		t.Skip("skipping test in short mode")
	}

	for i := 0; i < 100; i++ {
		t.Run(fmt.Sprintf("%d", i), createAndPutKeys)
	}
}
```

## File: `mlock_unix.go`
```go
//go:build !windows

package bbolt

import "golang.org/x/sys/unix"

// mlock locks memory of db file
func mlock(db *DB, fileSize int) error {
	sizeToLock := fileSize
	if sizeToLock > db.datasz {
		// Can't lock more than mmaped slice
		sizeToLock = db.datasz
	}
	if err := unix.Mlock(db.dataref[:sizeToLock]); err != nil {
		return err
	}
	return nil
}

// munlock unlocks memory of db file
func munlock(db *DB, fileSize int) error {
	if db.dataref == nil {
		return nil
	}

	sizeToUnlock := fileSize
	if sizeToUnlock > db.datasz {
		// Can't unlock more than mmaped slice
		sizeToUnlock = db.datasz
	}

	if err := unix.Munlock(db.dataref[:sizeToUnlock]); err != nil {
		return err
	}
	return nil
}
```

## File: `mlock_windows.go`
```go
package bbolt

// mlock locks memory of db file
func mlock(_ *DB, _ int) error {
	panic("mlock is supported only on UNIX systems")
}

// munlock unlocks memory of db file
func munlock(_ *DB, _ int) error {
	panic("munlock is supported only on UNIX systems")
}
```

## File: `movebucket_test.go`
```go
package bbolt_test

import (
	crand "crypto/rand"
	"math/rand"
	"os"
	"path/filepath"
	"testing"

	"github.com/stretchr/testify/require"

	"go.etcd.io/bbolt"
	"go.etcd.io/bbolt/errors"
	"go.etcd.io/bbolt/internal/btesting"
)

func TestTx_MoveBucket(t *testing.T) {
	testCases := []struct {
		name                    string
		srcBucketPath           []string
		dstBucketPath           []string
		bucketToMove            string
		bucketExistInSrc        bool
		bucketExistInDst        bool
		hasIncompatibleKeyInSrc bool
		hasIncompatibleKeyInDst bool
		expectedErr             error
	}{
		// normal cases
		{
			name:                    "normal case",
			srcBucketPath:           []string{"sb1", "sb2"},
			dstBucketPath:           []string{"db1", "db2"},
			bucketToMove:            "bucketToMove",
			bucketExistInSrc:        true,
			bucketExistInDst:        false,
			hasIncompatibleKeyInSrc: false,
			hasIncompatibleKeyInDst: false,
			expectedErr:             nil,
		},
		{
			name:                    "the source and target bucket share the same grandparent",
			srcBucketPath:           []string{"grandparent", "sb2"},
			dstBucketPath:           []string{"grandparent", "db2"},
			bucketToMove:            "bucketToMove",
			bucketExistInSrc:        true,
			bucketExistInDst:        false,
			hasIncompatibleKeyInSrc: false,
			hasIncompatibleKeyInDst: false,
			expectedErr:             nil,
		},
		{
			name:                    "bucketToMove is a top level bucket",
			srcBucketPath:           []string{},
			dstBucketPath:           []string{"db1", "db2"},
			bucketToMove:            "bucketToMove",
			bucketExistInSrc:        true,
			bucketExistInDst:        false,
			hasIncompatibleKeyInSrc: false,
			hasIncompatibleKeyInDst: false,
			expectedErr:             nil,
		},
		{
			name:                    "convert bucketToMove to a top level bucket",
			srcBucketPath:           []string{"sb1", "sb2"},
			dstBucketPath:           []string{},
			bucketToMove:            "bucketToMove",
			bucketExistInSrc:        true,
			bucketExistInDst:        false,
			hasIncompatibleKeyInSrc: false,
			hasIncompatibleKeyInDst: false,
			expectedErr:             nil,
		},
		// negative cases
		{
			name:                    "bucketToMove not exist in source bucket",
			srcBucketPath:           []string{"sb1", "sb2"},
			dstBucketPath:           []string{"db1", "db2"},
			bucketToMove:            "bucketToMove",
			bucketExistInSrc:        false,
			bucketExistInDst:        false,
			hasIncompatibleKeyInSrc: false,
			hasIncompatibleKeyInDst: false,
			expectedErr:             errors.ErrBucketNotFound,
		},
		{
			name:                    "bucketToMove exist in target bucket",
			srcBucketPath:           []string{"sb1", "sb2"},
			dstBucketPath:           []string{"db1", "db2"},
			bucketToMove:            "bucketToMove",
			bucketExistInSrc:        true,
			bucketExistInDst:        true,
			hasIncompatibleKeyInSrc: false,
			hasIncompatibleKeyInDst: false,
			expectedErr:             errors.ErrBucketExists,
		},
		{
			name:                    "incompatible key exist in source bucket",
			srcBucketPath:           []string{"sb1", "sb2"},
			dstBucketPath:           []string{"db1", "db2"},
			bucketToMove:            "bucketToMove",
			bucketExistInSrc:        false,
			bucketExistInDst:        false,
			hasIncompatibleKeyInSrc: true,
			hasIncompatibleKeyInDst: false,
			expectedErr:             errors.ErrIncompatibleValue,
		},
		{
			name:                    "incompatible key exist in target bucket",
			srcBucketPath:           []string{"sb1", "sb2"},
			dstBucketPath:           []string{"db1", "db2"},
			bucketToMove:            "bucketToMove",
			bucketExistInSrc:        true,
			bucketExistInDst:        false,
			hasIncompatibleKeyInSrc: false,
			hasIncompatibleKeyInDst: true,
			expectedErr:             errors.ErrIncompatibleValue,
		},
		{
			name:                    "the source and target are the same bucket",
			srcBucketPath:           []string{"sb1", "sb2"},
			dstBucketPath:           []string{"sb1", "sb2"},
			bucketToMove:            "bucketToMove",
			bucketExistInSrc:        true,
			bucketExistInDst:        false,
			hasIncompatibleKeyInSrc: false,
			hasIncompatibleKeyInDst: false,
			expectedErr:             errors.ErrSameBuckets,
		},
		{
			name:                    "both the source and target are the root bucket",
			srcBucketPath:           []string{},
			dstBucketPath:           []string{},
			bucketToMove:            "bucketToMove",
			bucketExistInSrc:        true,
			bucketExistInDst:        false,
			hasIncompatibleKeyInSrc: false,
			hasIncompatibleKeyInDst: false,
			expectedErr:             errors.ErrSameBuckets,
		},
	}

	for _, tc := range testCases {

		t.Run(tc.name, func(*testing.T) {
			db := btesting.MustCreateDBWithOption(t, &bbolt.Options{PageSize: 4096})

			dumpBucketBeforeMoving := filepath.Join(t.TempDir(), "dbBeforeMove")
			dumpBucketAfterMoving := filepath.Join(t.TempDir(), "dbAfterMove")

			t.Log("Creating sample db and populate some data")
			err := db.Update(func(tx *bbolt.Tx) error {
				srcBucket := prepareBuckets(t, tx, tc.srcBucketPath...)
				dstBucket := prepareBuckets(t, tx, tc.dstBucketPath...)

				if tc.bucketExistInSrc {
					_ = createBucketAndPopulateData(t, tx, srcBucket, tc.bucketToMove)
				}

				if tc.bucketExistInDst {
					_ = createBucketAndPopulateData(t, tx, dstBucket, tc.bucketToMove)
				}

				if tc.hasIncompatibleKeyInSrc {
					putErr := srcBucket.Put([]byte(tc.bucketToMove), []byte("bar"))
					require.NoError(t, putErr)
				}

				if tc.hasIncompatibleKeyInDst {
					putErr := dstBucket.Put([]byte(tc.bucketToMove), []byte("bar"))
					require.NoError(t, putErr)
				}

				return nil
			})
			require.NoError(t, err)

			t.Log("Moving bucket")
			err = db.Update(func(tx *bbolt.Tx) error {
				srcBucket := prepareBuckets(t, tx, tc.srcBucketPath...)
				dstBucket := prepareBuckets(t, tx, tc.dstBucketPath...)

				if tc.expectedErr == nil {
					t.Logf("Dump the bucket to %s before moving it", dumpBucketBeforeMoving)
					bk := openBucket(tx, srcBucket, tc.bucketToMove)
					dumpErr := dumpBucket([]byte(tc.bucketToMove), bk, dumpBucketBeforeMoving)
					require.NoError(t, dumpErr)
				}

				mErr := tx.MoveBucket([]byte(tc.bucketToMove), srcBucket, dstBucket)
				require.Equal(t, tc.expectedErr, mErr)

				if tc.expectedErr == nil {
					t.Logf("Dump the bucket to %s after moving it", dumpBucketAfterMoving)
					bk := openBucket(tx, dstBucket, tc.bucketToMove)
					dumpErr := dumpBucket([]byte(tc.bucketToMove), bk, dumpBucketAfterMoving)
					require.NoError(t, dumpErr)
				}

				return nil
			})
			require.NoError(t, err)

			// skip assertion if failure expected
			if tc.expectedErr != nil {
				return
			}

			t.Log("Verifying the bucket should be identical before and after being moved")
			dataBeforeMove, err := os.ReadFile(dumpBucketBeforeMoving)
			require.NoError(t, err)
			dataAfterMove, err := os.ReadFile(dumpBucketAfterMoving)
			require.NoError(t, err)
			require.Equal(t, dataBeforeMove, dataAfterMove)
		})
	}
}

func TestBucket_MoveBucket_DiffDB(t *testing.T) {
	srcBucketPath := []string{"sb1", "sb2"}
	dstBucketPath := []string{"db1", "db2"}
	bucketToMove := "bucketToMove"

	var srcBucket *bbolt.Bucket

	t.Log("Creating source bucket and populate some data")
	srcDB := btesting.MustCreateDBWithOption(t, &bbolt.Options{PageSize: 4096})
	err := srcDB.Update(func(tx *bbolt.Tx) error {
		srcBucket = prepareBuckets(t, tx, srcBucketPath...)
		return nil
	})
	require.NoError(t, err)
	defer func() {
		require.NoError(t, srcDB.Close())
	}()

	t.Log("Creating target bucket and populate some data")
	dstDB := btesting.MustCreateDBWithOption(t, &bbolt.Options{PageSize: 4096})
	err = dstDB.Update(func(tx *bbolt.Tx) error {
		prepareBuckets(t, tx, dstBucketPath...)
		return nil
	})
	require.NoError(t, err)
	defer func() {
		require.NoError(t, dstDB.Close())
	}()

	t.Log("Reading source bucket in a separate RWTx")
	sTx, sErr := srcDB.Begin(true)
	require.NoError(t, sErr)
	defer func() {
		require.NoError(t, sTx.Rollback())
	}()
	srcBucket = prepareBuckets(t, sTx, srcBucketPath...)

	t.Log("Moving the sub-bucket in a separate RWTx")
	err = dstDB.Update(func(tx *bbolt.Tx) error {
		dstBucket := prepareBuckets(t, tx, dstBucketPath...)
		mErr := srcBucket.MoveBucket([]byte(bucketToMove), dstBucket)
		require.Equal(t, errors.ErrDifferentDB, mErr)

		return nil
	})
	require.NoError(t, err)
}

func TestBucket_MoveBucket_DiffTx(t *testing.T) {
	testCases := []struct {
		name            string
		srcBucketPath   []string
		dstBucketPath   []string
		isSrcReadonlyTx bool
		isDstReadonlyTx bool
		bucketToMove    string
		expectedErr     error
	}{
		{
			name:            "src is RWTx and target is RTx",
			srcBucketPath:   []string{"sb1", "sb2"},
			dstBucketPath:   []string{"db1", "db2"},
			isSrcReadonlyTx: true,
			isDstReadonlyTx: false,
			bucketToMove:    "bucketToMove",
			expectedErr:     errors.ErrTxNotWritable,
		},
		{
			name:            "src is RTx and target is RWTx",
			srcBucketPath:   []string{"sb1", "sb2"},
			dstBucketPath:   []string{"db1", "db2"},
			isSrcReadonlyTx: false,
			isDstReadonlyTx: true,
			bucketToMove:    "bucketToMove",
			expectedErr:     errors.ErrTxNotWritable,
		},
	}

	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			var srcBucket *bbolt.Bucket
			var dstBucket *bbolt.Bucket

			t.Log("Creating source and target buckets and populate some data")
			db := btesting.MustCreateDBWithOption(t, &bbolt.Options{PageSize: 4096})
			err := db.Update(func(tx *bbolt.Tx) error {
				srcBucket = prepareBuckets(t, tx, tc.srcBucketPath...)
				dstBucket = prepareBuckets(t, tx, tc.dstBucketPath...)
				return nil
			})
			require.NoError(t, err)
			defer func() {
				require.NoError(t, db.Close())
			}()

			t.Log("Opening source bucket in a separate Tx")
			sTx, sErr := db.Begin(tc.isSrcReadonlyTx)
			require.NoError(t, sErr)
			defer func() {
				require.NoError(t, sTx.Rollback())
			}()
			srcBucket = prepareBuckets(t, sTx, tc.srcBucketPath...)

			t.Log("Opening target bucket in a separate Tx")
			dTx, dErr := db.Begin(tc.isDstReadonlyTx)
			require.NoError(t, dErr)
			defer func() {
				require.NoError(t, dTx.Rollback())
			}()
			dstBucket = prepareBuckets(t, dTx, tc.dstBucketPath...)

			t.Log("Moving the sub-bucket")
			err = db.View(func(tx *bbolt.Tx) error {
				mErr := srcBucket.MoveBucket([]byte(tc.bucketToMove), dstBucket)
				require.Equal(t, tc.expectedErr, mErr)

				return nil
			})
			require.NoError(t, err)
		})
	}
}

// prepareBuckets opens the bucket chain. For each bucket in the chain,
// open it if existed, otherwise create it and populate sample data.
func prepareBuckets(t testing.TB, tx *bbolt.Tx, buckets ...string) *bbolt.Bucket {
	var bk *bbolt.Bucket

	for _, key := range buckets {
		if childBucket := openBucket(tx, bk, key); childBucket == nil {
			bk = createBucketAndPopulateData(t, tx, bk, key)
		} else {
			bk = childBucket
		}
	}
	return bk
}

func openBucket(tx *bbolt.Tx, bk *bbolt.Bucket, bucketToOpen string) *bbolt.Bucket {
	if bk == nil {
		return tx.Bucket([]byte(bucketToOpen))
	}
	return bk.Bucket([]byte(bucketToOpen))
}

func createBucketAndPopulateData(t testing.TB, tx *bbolt.Tx, bk *bbolt.Bucket, bucketName string) *bbolt.Bucket {
	if bk == nil {
		newBucket, err := tx.CreateBucket([]byte(bucketName))
		require.NoError(t, err, "failed to create bucket %s", bucketName)
		populateSampleDataInBucket(t, newBucket, rand.Intn(4096))
		return newBucket
	}

	newBucket, err := bk.CreateBucket([]byte(bucketName))
	require.NoError(t, err, "failed to create bucket %s", bucketName)
	populateSampleDataInBucket(t, newBucket, rand.Intn(4096))
	return newBucket
}

func populateSampleDataInBucket(t testing.TB, bk *bbolt.Bucket, n int) {
	var min, max = 1, 1024

	for i := 0; i < n; i++ {
		// generate rand key/value length
		keyLength := rand.Intn(max-min) + min
		valLength := rand.Intn(max-min) + min

		keyData := make([]byte, keyLength)
		valData := make([]byte, valLength)

		_, err := crand.Read(keyData)
		require.NoError(t, err)

		_, err = crand.Read(valData)
		require.NoError(t, err)

		err = bk.Put(keyData, valData)
		require.NoError(t, err)
	}
}
```

## File: `node.go`
```go
package bbolt

import (
	"bytes"
	"fmt"
	"sort"

	"go.etcd.io/bbolt/internal/common"
)

// node represents an in-memory, deserialized page.
type node struct {
	bucket     *Bucket
	isLeaf     bool
	unbalanced bool
	spilled    bool
	key        []byte
	pgid       common.Pgid
	parent     *node
	children   nodes
	inodes     common.Inodes
}

// root returns the top-level node this node is attached to.
func (n *node) root() *node {
	if n.parent == nil {
		return n
	}
	return n.parent.root()
}

// minKeys returns the minimum number of inodes this node should have.
func (n *node) minKeys() int {
	if n.isLeaf {
		return 1
	}
	return 2
}

// size returns the size of the node after serialization.
func (n *node) size() int {
	sz, elsz := common.PageHeaderSize, n.pageElementSize()
	for i := 0; i < len(n.inodes); i++ {
		item := &n.inodes[i]
		sz += elsz + uintptr(len(item.Key())) + uintptr(len(item.Value()))
	}
	return int(sz)
}

// sizeLessThan returns true if the node is less than a given size.
// This is an optimization to avoid calculating a large node when we only need
// to know if it fits inside a certain page size.
func (n *node) sizeLessThan(v uintptr) bool {
	sz, elsz := common.PageHeaderSize, n.pageElementSize()
	for i := 0; i < len(n.inodes); i++ {
		item := &n.inodes[i]
		sz += elsz + uintptr(len(item.Key())) + uintptr(len(item.Value()))
		if sz >= v {
			return false
		}
	}
	return true
}

// pageElementSize returns the size of each page element based on the type of node.
func (n *node) pageElementSize() uintptr {
	if n.isLeaf {
		return common.LeafPageElementSize
	}
	return common.BranchPageElementSize
}

// childAt returns the child node at a given index.
func (n *node) childAt(index int) *node {
	if n.isLeaf {
		panic(fmt.Sprintf("invalid childAt(%d) on a leaf node", index))
	}
	return n.bucket.node(n.inodes[index].Pgid(), n)
}

// childIndex returns the index of a given child node.
func (n *node) childIndex(child *node) int {
	index := sort.Search(len(n.inodes), func(i int) bool { return bytes.Compare(n.inodes[i].Key(), child.key) != -1 })
	return index
}

// numChildren returns the number of children.
func (n *node) numChildren() int {
	return len(n.inodes)
}

// nextSibling returns the next node with the same parent.
func (n *node) nextSibling() *node {
	if n.parent == nil {
		return nil
	}
	index := n.parent.childIndex(n)
	if index >= n.parent.numChildren()-1 {
		return nil
	}
	return n.parent.childAt(index + 1)
}

// prevSibling returns the previous node with the same parent.
func (n *node) prevSibling() *node {
	if n.parent == nil {
		return nil
	}
	index := n.parent.childIndex(n)
	if index == 0 {
		return nil
	}
	return n.parent.childAt(index - 1)
}

// put inserts a key/value.
func (n *node) put(oldKey, newKey, value []byte, pgId common.Pgid, flags uint32) {
	if pgId >= n.bucket.tx.meta.Pgid() {
		panic(fmt.Sprintf("pgId (%d) above high water mark (%d)", pgId, n.bucket.tx.meta.Pgid()))
	} else if len(oldKey) <= 0 {
		panic("put: zero-length old key")
	} else if len(newKey) <= 0 {
		panic("put: zero-length new key")
	}

	// Find insertion index.
	index := sort.Search(len(n.inodes), func(i int) bool { return bytes.Compare(n.inodes[i].Key(), oldKey) != -1 })

	// Add capacity and shift nodes if we don't have an exact match and need to insert.
	exact := len(n.inodes) > 0 && index < len(n.inodes) && bytes.Equal(n.inodes[index].Key(), oldKey)
	if !exact {
		n.inodes = append(n.inodes, common.Inode{})
		copy(n.inodes[index+1:], n.inodes[index:])
	}

	inode := &n.inodes[index]
	inode.SetFlags(flags)
	inode.SetKey(newKey)
	inode.SetValue(value)
	inode.SetPgid(pgId)
	common.Assert(len(inode.Key()) > 0, "put: zero-length inode key")
}

// del removes a key from the node.
func (n *node) del(key []byte) {
	// Find index of key.
	index := sort.Search(len(n.inodes), func(i int) bool { return bytes.Compare(n.inodes[i].Key(), key) != -1 })

	// Exit if the key isn't found.
	if index >= len(n.inodes) || !bytes.Equal(n.inodes[index].Key(), key) {
		return
	}

	// Delete inode from the node.
	n.inodes = append(n.inodes[:index], n.inodes[index+1:]...)

	// Mark the node as needing rebalancing.
	n.unbalanced = true
}

// read initializes the node from a page.
func (n *node) read(p *common.Page) {
	n.pgid = p.Id()
	n.isLeaf = p.IsLeafPage()
	n.inodes = common.ReadInodeFromPage(p)

	// Save first key, so we can find the node in the parent when we spill.
	if len(n.inodes) > 0 {
		n.key = n.inodes[0].Key()
		common.Assert(len(n.key) > 0, "read: zero-length node key")
	} else {
		n.key = nil
	}
}

// write writes the items onto one or more pages.
// The page should have p.id (might be 0 for meta or bucket-inline page) and p.overflow set
// and the rest should be zeroed.
func (n *node) write(p *common.Page) {
	common.Assert(p.Count() == 0 && p.Flags() == 0, "node cannot be written into a not empty page")

	// Initialize page.
	if n.isLeaf {
		p.SetFlags(common.LeafPageFlag)
	} else {
		p.SetFlags(common.BranchPageFlag)
	}

	if len(n.inodes) >= 0xFFFF {
		panic(fmt.Sprintf("inode overflow: %d (pgid=%d)", len(n.inodes), p.Id()))
	}
	p.SetCount(uint16(len(n.inodes)))

	// Stop here if there are no items to write.
	if p.Count() == 0 {
		return
	}

	common.WriteInodeToPage(n.inodes, p)

	// DEBUG ONLY: n.dump()
}

// split breaks up a node into multiple smaller nodes, if appropriate.
// This should only be called from the spill() function.
func (n *node) split(pageSize uintptr) []*node {
	var nodes []*node

	node := n
	for {
		// Split node into two.
		a, b := node.splitTwo(pageSize)
		nodes = append(nodes, a)

		// If we can't split then exit the loop.
		if b == nil {
			break
		}

		// Set node to b so it gets split on the next iteration.
		node = b
	}

	return nodes
}

// splitTwo breaks up a node into two smaller nodes, if appropriate.
// This should only be called from the split() function.
func (n *node) splitTwo(pageSize uintptr) (*node, *node) {
	// Ignore the split if the page doesn't have at least enough nodes for
	// two pages or if the nodes can fit in a single page.
	if len(n.inodes) <= (common.MinKeysPerPage*2) || n.sizeLessThan(pageSize) {
		return n, nil
	}

	// Determine the threshold before starting a new node.
	var fillPercent = n.bucket.FillPercent
	if fillPercent < minFillPercent {
		fillPercent = minFillPercent
	} else if fillPercent > maxFillPercent {
		fillPercent = maxFillPercent
	}
	threshold := int(float64(pageSize) * fillPercent)

	// Determine split position and sizes of the two pages.
	splitIndex, _ := n.splitIndex(threshold)

	// Split node into two separate nodes.
	// If there's no parent then we'll need to create one.
	if n.parent == nil {
		n.parent = &node{bucket: n.bucket, children: []*node{n}}
	}

	// Create a new node and add it to the parent.
	next := &node{bucket: n.bucket, isLeaf: n.isLeaf, parent: n.parent}
	n.parent.children = append(n.parent.children, next)

	// Split inodes across two nodes.
	next.inodes = n.inodes[splitIndex:]
	n.inodes = n.inodes[:splitIndex]

	// Update the statistics.
	n.bucket.tx.stats.IncSplit(1)

	return n, next
}

// splitIndex finds the position where a page will fill a given threshold.
// It returns the index as well as the size of the first page.
// This is only be called from split().
func (n *node) splitIndex(threshold int) (index, sz uintptr) {
	sz = common.PageHeaderSize

	// Loop until we only have the minimum number of keys required for the second page.
	for i := 0; i < len(n.inodes)-common.MinKeysPerPage; i++ {
		index = uintptr(i)
		inode := n.inodes[i]
		elsize := n.pageElementSize() + uintptr(len(inode.Key())) + uintptr(len(inode.Value()))

		// If we have at least the minimum number of keys and adding another
		// node would put us over the threshold then exit and return.
		if index >= common.MinKeysPerPage && sz+elsize > uintptr(threshold) {
			break
		}

		// Add the element size to the total size.
		sz += elsize
	}

	return
}

// spill writes the nodes to dirty pages and splits nodes as it goes.
// Returns an error if dirty pages cannot be allocated.
func (n *node) spill() error {
	var tx = n.bucket.tx
	if n.spilled {
		return nil
	}

	// Spill child nodes first. Child nodes can materialize sibling nodes in
	// the case of split-merge so we cannot use a range loop. We have to check
	// the children size on every loop iteration.
	sort.Sort(n.children)
	for i := 0; i < len(n.children); i++ {
		if err := n.children[i].spill(); err != nil {
			return err
		}
	}

	// We no longer need the child list because it's only used for spill tracking.
	n.children = nil

	// Split nodes into appropriate sizes. The first node will always be n.
	var nodes = n.split(uintptr(tx.db.pageSize))
	for _, node := range nodes {
		// Add node's page to the freelist if it's not new.
		if node.pgid > 0 {
			tx.db.freelist.Free(tx.meta.Txid(), tx.page(node.pgid))
			node.pgid = 0
		}

		// Allocate contiguous space for the node.
		p, err := tx.allocate((node.size() + tx.db.pageSize - 1) / tx.db.pageSize)
		if err != nil {
			return err
		}

		// Write the node.
		if p.Id() >= tx.meta.Pgid() {
			panic(fmt.Sprintf("pgid (%d) above high water mark (%d)", p.Id(), tx.meta.Pgid()))
		}
		node.pgid = p.Id()
		node.write(p)
		node.spilled = true

		// Insert into parent inodes.
		if node.parent != nil {
			var key = node.key
			if key == nil {
				key = node.inodes[0].Key()
			}

			node.parent.put(key, node.inodes[0].Key(), nil, node.pgid, 0)
			node.key = node.inodes[0].Key()
			common.Assert(len(node.key) > 0, "spill: zero-length node key")
		}

		// Update the statistics.
		tx.stats.IncSpill(1)
	}

	// If the root node split and created a new root then we need to spill that
	// as well. We'll clear out the children to make sure it doesn't try to respill.
	if n.parent != nil && n.parent.pgid == 0 {
		n.children = nil
		return n.parent.spill()
	}

	return nil
}

// rebalance attempts to combine the node with sibling nodes if the node fill
// size is below a threshold or if there are not enough keys.
func (n *node) rebalance() {
	if !n.unbalanced {
		return
	}
	n.unbalanced = false

	// Update statistics.
	n.bucket.tx.stats.IncRebalance(1)

	// Ignore if node is above threshold (25% when FillPercent is set to DefaultFillPercent) and has enough keys.
	var threshold = int(float64(n.bucket.tx.db.pageSize)*n.bucket.FillPercent) / 2
	if n.size() > threshold && len(n.inodes) > n.minKeys() {
		return
	}

	// Root node has special handling.
	if n.parent == nil {
		// If root node is a branch and only has one node then collapse it.
		if !n.isLeaf && len(n.inodes) == 1 {
			// Move root's child up.
			child := n.bucket.node(n.inodes[0].Pgid(), n)
			n.isLeaf = child.isLeaf
			n.inodes = child.inodes[:]
			n.children = child.children

			// Reparent all child nodes being moved.
			for _, inode := range n.inodes {
				if child, ok := n.bucket.nodes[inode.Pgid()]; ok {
					child.parent = n
				}
			}

			// Remove old child.
			child.parent = nil
			delete(n.bucket.nodes, child.pgid)
			child.free()
		}

		return
	}

	// If node has no keys then just remove it.
	if n.numChildren() == 0 {
		n.parent.del(n.key)
		n.parent.removeChild(n)
		delete(n.bucket.nodes, n.pgid)
		n.free()
		n.parent.rebalance()
		return
	}

	common.Assert(n.parent.numChildren() > 1, "parent must have at least 2 children")

	// Merge with right sibling if idx == 0, otherwise left sibling.
	var leftNode, rightNode *node
	var useNextSibling = n.parent.childIndex(n) == 0
	if useNextSibling {
		leftNode = n
		rightNode = n.nextSibling()
	} else {
		leftNode = n.prevSibling()
		rightNode = n
	}

	// If both nodes are too small then merge them.
	// Reparent all child nodes being moved.
	for _, inode := range rightNode.inodes {
		if child, ok := n.bucket.nodes[inode.Pgid()]; ok {
			child.parent.removeChild(child)
			child.parent = leftNode
			child.parent.children = append(child.parent.children, child)
		}
	}

	// Copy over inodes from right node to left node and remove right node.
	leftNode.inodes = append(leftNode.inodes, rightNode.inodes...)
	n.parent.del(rightNode.key)
	n.parent.removeChild(rightNode)
	delete(n.bucket.nodes, rightNode.pgid)
	rightNode.free()

	// Either this node or the sibling node was deleted from the parent so rebalance it.
	n.parent.rebalance()
}

// removes a node from the list of in-memory children.
// This does not affect the inodes.
func (n *node) removeChild(target *node) {
	for i, child := range n.children {
		if child == target {
			n.children = append(n.children[:i], n.children[i+1:]...)
			return
		}
	}
}

// dereference causes the node to copy all its inode key/value references to heap memory.
// This is required when the mmap is reallocated so inodes are not pointing to stale data.
func (n *node) dereference() {
	if n.key != nil {
		key := make([]byte, len(n.key))
		copy(key, n.key)
		n.key = key
		common.Assert(n.pgid == 0 || len(n.key) > 0, "dereference: zero-length node key on existing node")
	}

	for i := range n.inodes {
		inode := &n.inodes[i]

		key := make([]byte, len(inode.Key()))
		copy(key, inode.Key())
		inode.SetKey(key)
		common.Assert(len(inode.Key()) > 0, "dereference: zero-length inode key")

		value := make([]byte, len(inode.Value()))
		copy(value, inode.Value())
		inode.SetValue(value)
	}

	// Recursively dereference children.
	for _, child := range n.children {
		child.dereference()
	}

	// Update statistics.
	n.bucket.tx.stats.IncNodeDeref(1)
}

// free adds the node's underlying page to the freelist.
func (n *node) free() {
	if n.pgid != 0 {
		n.bucket.tx.db.freelist.Free(n.bucket.tx.meta.Txid(), n.bucket.tx.page(n.pgid))
		n.pgid = 0
	}
}

// dump writes the contents of the node to STDERR for debugging purposes.
/*
func (n *node) dump() {
	// Write node header.
	var typ = "branch"
	if n.isLeaf {
		typ = "leaf"
	}
	warnf("[NODE %d {type=%s count=%d}]", n.pgid, typ, len(n.inodes))

	// Write out abbreviated version of each item.
	for _, item := range n.inodes {
		if n.isLeaf {
			if item.flags&bucketLeafFlag != 0 {
				bucket := (*bucket)(unsafe.Pointer(&item.value[0]))
				warnf("+L %08x -> (bucket root=%d)", trunc(item.key, 4), bucket.root)
			} else {
				warnf("+L %08x -> %08x", trunc(item.key, 4), trunc(item.value, 4))
			}
		} else {
			warnf("+B %08x -> pgid=%d", trunc(item.key, 4), item.pgid)
		}
	}
	warn("")
}
*/

func compareKeys(left, right []byte) int {
	return bytes.Compare(left, right)
}

type nodes []*node

func (s nodes) Len() int      { return len(s) }
func (s nodes) Swap(i, j int) { s[i], s[j] = s[j], s[i] }
func (s nodes) Less(i, j int) bool {
	return bytes.Compare(s[i].inodes[0].Key(), s[j].inodes[0].Key()) == -1
}
```

## File: `node_test.go`
```go
package bbolt

import (
	"testing"
	"unsafe"

	"go.etcd.io/bbolt/internal/common"
)

// Ensure that a node can insert a key/value.
func TestNode_put(t *testing.T) {
	m := &common.Meta{}
	m.SetPgid(1)
	n := &node{inodes: make(common.Inodes, 0), bucket: &Bucket{tx: &Tx{meta: m}}}
	n.put([]byte("baz"), []byte("baz"), []byte("2"), 0, 0)
	n.put([]byte("foo"), []byte("foo"), []byte("0"), 0, 0)
	n.put([]byte("bar"), []byte("bar"), []byte("1"), 0, 0)
	n.put([]byte("foo"), []byte("foo"), []byte("3"), 0, common.LeafPageFlag)

	if len(n.inodes) != 3 {
		t.Fatalf("exp=3; got=%d", len(n.inodes))
	}
	if k, v := n.inodes[0].Key(), n.inodes[0].Value(); string(k) != "bar" || string(v) != "1" {
		t.Fatalf("exp=<bar,1>; got=<%s,%s>", k, v)
	}
	if k, v := n.inodes[1].Key(), n.inodes[1].Value(); string(k) != "baz" || string(v) != "2" {
		t.Fatalf("exp=<baz,2>; got=<%s,%s>", k, v)
	}
	if k, v := n.inodes[2].Key(), n.inodes[2].Value(); string(k) != "foo" || string(v) != "3" {
		t.Fatalf("exp=<foo,3>; got=<%s,%s>", k, v)
	}
	if n.inodes[2].Flags() != uint32(common.LeafPageFlag) {
		t.Fatalf("not a leaf: %d", n.inodes[2].Flags())
	}
}

// Ensure that a node can deserialize from a leaf page.
func TestNode_read_LeafPage(t *testing.T) {
	// Create a page.
	var buf [4096]byte
	page := (*common.Page)(unsafe.Pointer(&buf[0]))
	page.SetFlags(common.LeafPageFlag)
	page.SetCount(2)

	// Insert 2 elements at the beginning. sizeof(leafPageElement) == 16
	nodes := page.LeafPageElements()
	//nodes := (*[3]leafPageElement)(unsafe.Pointer(uintptr(unsafe.Pointer(page)) + unsafe.Sizeof(*page)))
	nodes[0] = *common.NewLeafPageElement(0, 32, 3, 4)  // pos = sizeof(leafPageElement) * 2
	nodes[1] = *common.NewLeafPageElement(0, 23, 10, 3) // pos = sizeof(leafPageElement) + 3 + 4

	// Write data for the nodes at the end.
	const s = "barfoozhelloworldbye"
	data := common.UnsafeByteSlice(unsafe.Pointer(uintptr(unsafe.Pointer(page))+unsafe.Sizeof(*page)+common.LeafPageElementSize*2), 0, 0, len(s))
	copy(data, s)

	// Deserialize page into a leaf.
	n := &node{}
	n.read(page)

	// Check that there are two inodes with correct data.
	if !n.isLeaf {
		t.Fatal("expected leaf")
	}
	if len(n.inodes) != 2 {
		t.Fatalf("exp=2; got=%d", len(n.inodes))
	}
	if k, v := n.inodes[0].Key(), n.inodes[0].Value(); string(k) != "bar" || string(v) != "fooz" {
		t.Fatalf("exp=<bar,fooz>; got=<%s,%s>", k, v)
	}
	if k, v := n.inodes[1].Key(), n.inodes[1].Value(); string(k) != "helloworld" || string(v) != "bye" {
		t.Fatalf("exp=<helloworld,bye>; got=<%s,%s>", k, v)
	}
}

// Ensure that a node can serialize into a leaf page.
func TestNode_write_LeafPage(t *testing.T) {
	// Create a node.
	m := &common.Meta{}
	m.SetPgid(1)
	n := &node{isLeaf: true, inodes: make(common.Inodes, 0), bucket: &Bucket{tx: &Tx{db: &DB{}, meta: m}}}
	n.put([]byte("susy"), []byte("susy"), []byte("que"), 0, 0)
	n.put([]byte("ricki"), []byte("ricki"), []byte("lake"), 0, 0)
	n.put([]byte("john"), []byte("john"), []byte("johnson"), 0, 0)

	// Write it to a page.
	var buf [4096]byte
	p := (*common.Page)(unsafe.Pointer(&buf[0]))
	n.write(p)

	// Read the page back in.
	n2 := &node{}
	n2.read(p)

	// Check that the two pages are the same.
	if len(n2.inodes) != 3 {
		t.Fatalf("exp=3; got=%d", len(n2.inodes))
	}
	if k, v := n2.inodes[0].Key(), n2.inodes[0].Value(); string(k) != "john" || string(v) != "johnson" {
		t.Fatalf("exp=<john,johnson>; got=<%s,%s>", k, v)
	}
	if k, v := n2.inodes[1].Key(), n2.inodes[1].Value(); string(k) != "ricki" || string(v) != "lake" {
		t.Fatalf("exp=<ricki,lake>; got=<%s,%s>", k, v)
	}
	if k, v := n2.inodes[2].Key(), n2.inodes[2].Value(); string(k) != "susy" || string(v) != "que" {
		t.Fatalf("exp=<susy,que>; got=<%s,%s>", k, v)
	}
}

// Ensure that a node can split into appropriate subgroups.
func TestNode_split(t *testing.T) {
	// Create a node.
	m := &common.Meta{}
	m.SetPgid(1)
	n := &node{inodes: make(common.Inodes, 0), bucket: &Bucket{tx: &Tx{db: &DB{}, meta: m}}}
	n.put([]byte("00000001"), []byte("00000001"), []byte("0123456701234567"), 0, 0)
	n.put([]byte("00000002"), []byte("00000002"), []byte("0123456701234567"), 0, 0)
	n.put([]byte("00000003"), []byte("00000003"), []byte("0123456701234567"), 0, 0)
	n.put([]byte("00000004"), []byte("00000004"), []byte("0123456701234567"), 0, 0)
	n.put([]byte("00000005"), []byte("00000005"), []byte("0123456701234567"), 0, 0)

	// Split between 2 & 3.
	n.split(100)

	var parent = n.parent
	if len(parent.children) != 2 {
		t.Fatalf("exp=2; got=%d", len(parent.children))
	}
	if len(parent.children[0].inodes) != 2 {
		t.Fatalf("exp=2; got=%d", len(parent.children[0].inodes))
	}
	if len(parent.children[1].inodes) != 3 {
		t.Fatalf("exp=3; got=%d", len(parent.children[1].inodes))
	}
}

// Ensure that a page with the minimum number of inodes just returns a single node.
func TestNode_split_MinKeys(t *testing.T) {
	// Create a node.
	m := &common.Meta{}
	m.SetPgid(1)
	n := &node{inodes: make(common.Inodes, 0), bucket: &Bucket{tx: &Tx{db: &DB{}, meta: m}}}
	n.put([]byte("00000001"), []byte("00000001"), []byte("0123456701234567"), 0, 0)
	n.put([]byte("00000002"), []byte("00000002"), []byte("0123456701234567"), 0, 0)

	// Split.
	n.split(20)
	if n.parent != nil {
		t.Fatalf("expected nil parent")
	}
}

// Ensure that a node that has keys that all fit on a page just returns one leaf.
func TestNode_split_SinglePage(t *testing.T) {
	// Create a node.
	m := &common.Meta{}
	m.SetPgid(1)
	n := &node{inodes: make(common.Inodes, 0), bucket: &Bucket{tx: &Tx{db: &DB{}, meta: m}}}
	n.put([]byte("00000001"), []byte("00000001"), []byte("0123456701234567"), 0, 0)
	n.put([]byte("00000002"), []byte("00000002"), []byte("0123456701234567"), 0, 0)
	n.put([]byte("00000003"), []byte("00000003"), []byte("0123456701234567"), 0, 0)
	n.put([]byte("00000004"), []byte("00000004"), []byte("0123456701234567"), 0, 0)
	n.put([]byte("00000005"), []byte("00000005"), []byte("0123456701234567"), 0, 0)

	// Split.
	n.split(4096)
	if n.parent != nil {
		t.Fatalf("expected nil parent")
	}
}
```

## File: `quick_test.go`
```go
package bbolt_test

import (
	"bytes"
	"flag"
	"fmt"
	"math/rand"
	"os"
	"reflect"
	"testing"
	"testing/quick"
	"time"
)

// testing/quick defaults to 5 iterations and a random seed.
// You can override these settings from the command line:
//
//   -quick.count     The number of iterations to perform.
//   -quick.seed      The seed to use for randomizing.
//   -quick.maxitems  The maximum number of items to insert into a DB.
//   -quick.maxksize  The maximum size of a key.
//   -quick.maxvsize  The maximum size of a value.
//

var qcount, qseed, qmaxitems, qmaxksize, qmaxvsize int

func TestMain(m *testing.M) {
	flag.IntVar(&qcount, "quick.count", 5, "")
	flag.IntVar(&qseed, "quick.seed", int(time.Now().UnixNano())%100000, "")
	flag.IntVar(&qmaxitems, "quick.maxitems", 1000, "")
	flag.IntVar(&qmaxksize, "quick.maxksize", 1024, "")
	flag.IntVar(&qmaxvsize, "quick.maxvsize", 1024, "")
	flag.Parse()
	fmt.Fprintln(os.Stderr, "seed:", qseed)
	fmt.Fprintf(os.Stderr, "quick settings: count=%v, items=%v, ksize=%v, vsize=%v\n", qcount, qmaxitems, qmaxksize, qmaxvsize)

	os.Exit(m.Run())
}

func qconfig() *quick.Config {
	return &quick.Config{
		MaxCount: qcount,
		Rand:     rand.New(rand.NewSource(int64(qseed))),
	}
}

type testdata []testdataitem

func (t testdata) Len() int           { return len(t) }
func (t testdata) Swap(i, j int)      { t[i], t[j] = t[j], t[i] }
func (t testdata) Less(i, j int) bool { return bytes.Compare(t[i].Key, t[j].Key) == -1 }

func (t testdata) Generate(rand *rand.Rand, size int) reflect.Value {
	n := rand.Intn(qmaxitems-1) + 1
	items := make(testdata, n)
	used := make(map[string]bool)
	for i := 0; i < n; i++ {
		item := &items[i]
		// Ensure that keys are unique by looping until we find one that we have not already used.
		for {
			item.Key = randByteSlice(rand, 1, qmaxksize)
			if !used[string(item.Key)] {
				used[string(item.Key)] = true
				break
			}
		}
		item.Value = randByteSlice(rand, 0, qmaxvsize)
	}
	return reflect.ValueOf(items)
}

type revtestdata []testdataitem

func (t revtestdata) Len() int           { return len(t) }
func (t revtestdata) Swap(i, j int)      { t[i], t[j] = t[j], t[i] }
func (t revtestdata) Less(i, j int) bool { return bytes.Compare(t[i].Key, t[j].Key) == 1 }

type testdataitem struct {
	Key   []byte
	Value []byte
}

func randByteSlice(rand *rand.Rand, minSize, maxSize int) []byte {
	n := rand.Intn(maxSize-minSize) + minSize
	b := make([]byte, n)
	for i := 0; i < n; i++ {
		b[i] = byte(rand.Intn(255))
	}
	return b
}
```

## File: `simulation_no_freelist_sync_test.go`
```go
package bbolt_test

import (
	"testing"

	bolt "go.etcd.io/bbolt"
)

func TestSimulateNoFreeListSync_1op_1p(t *testing.T) {
	testSimulate(t, &bolt.Options{NoFreelistSync: true}, 8, 1, 1)
}
func TestSimulateNoFreeListSync_10op_1p(t *testing.T) {
	testSimulate(t, &bolt.Options{NoFreelistSync: true}, 8, 10, 1)
}
func TestSimulateNoFreeListSync_100op_1p(t *testing.T) {
	testSimulate(t, &bolt.Options{NoFreelistSync: true}, 8, 100, 1)
}
func TestSimulateNoFreeListSync_1000op_1p(t *testing.T) {
	testSimulate(t, &bolt.Options{NoFreelistSync: true}, 8, 1000, 1)
}
func TestSimulateNoFreeListSync_10000op_1p(t *testing.T) {
	testSimulate(t, &bolt.Options{NoFreelistSync: true}, 8, 10000, 1)
}
func TestSimulateNoFreeListSync_10op_10p(t *testing.T) {
	testSimulate(t, &bolt.Options{NoFreelistSync: true}, 8, 10, 10)
}
func TestSimulateNoFreeListSync_100op_10p(t *testing.T) {
	testSimulate(t, &bolt.Options{NoFreelistSync: true}, 8, 100, 10)
}
func TestSimulateNoFreeListSync_1000op_10p(t *testing.T) {
	testSimulate(t, &bolt.Options{NoFreelistSync: true}, 8, 1000, 10)
}
func TestSimulateNoFreeListSync_10000op_10p(t *testing.T) {
	testSimulate(t, &bolt.Options{NoFreelistSync: true}, 8, 10000, 10)
}
func TestSimulateNoFreeListSync_100op_100p(t *testing.T) {
	testSimulate(t, &bolt.Options{NoFreelistSync: true}, 8, 100, 100)
}
func TestSimulateNoFreeListSync_1000op_100p(t *testing.T) {
	testSimulate(t, &bolt.Options{NoFreelistSync: true}, 8, 1000, 100)
}
func TestSimulateNoFreeListSync_10000op_100p(t *testing.T) {
	testSimulate(t, &bolt.Options{NoFreelistSync: true}, 8, 10000, 100)
}
func TestSimulateNoFreeListSync_10000op_1000p(t *testing.T) {
	testSimulate(t, &bolt.Options{NoFreelistSync: true}, 8, 10000, 1000)
}
```

## File: `simulation_test.go`
```go
package bbolt_test

import (
	"bytes"
	"fmt"
	"math/rand"
	"sync"
	"sync/atomic"
	"testing"

	bolt "go.etcd.io/bbolt"
	"go.etcd.io/bbolt/internal/btesting"
)

func TestSimulate_1op_1p(t *testing.T)     { testSimulate(t, nil, 1, 1, 1) }
func TestSimulate_10op_1p(t *testing.T)    { testSimulate(t, nil, 1, 10, 1) }
func TestSimulate_100op_1p(t *testing.T)   { testSimulate(t, nil, 1, 100, 1) }
func TestSimulate_1000op_1p(t *testing.T)  { testSimulate(t, nil, 1, 1000, 1) }
func TestSimulate_10000op_1p(t *testing.T) { testSimulate(t, nil, 1, 10000, 1) }

func TestSimulate_10op_10p(t *testing.T)    { testSimulate(t, nil, 1, 10, 10) }
func TestSimulate_100op_10p(t *testing.T)   { testSimulate(t, nil, 1, 100, 10) }
func TestSimulate_1000op_10p(t *testing.T)  { testSimulate(t, nil, 1, 1000, 10) }
func TestSimulate_10000op_10p(t *testing.T) { testSimulate(t, nil, 1, 10000, 10) }

func TestSimulate_100op_100p(t *testing.T)   { testSimulate(t, nil, 1, 100, 100) }
func TestSimulate_1000op_100p(t *testing.T)  { testSimulate(t, nil, 1, 1000, 100) }
func TestSimulate_10000op_100p(t *testing.T) { testSimulate(t, nil, 1, 10000, 100) }

func TestSimulate_10000op_1000p(t *testing.T) { testSimulate(t, nil, 1, 10000, 1000) }

// Randomly generate operations on a given database with multiple clients to ensure consistency and thread safety.
func testSimulate(t *testing.T, openOption *bolt.Options, round, threadCount, parallelism int) {
	if testing.Short() {
		t.Skip("skipping test in short mode.")
	}

	// A list of operations that readers and writers can perform.
	var readerHandlers = []simulateHandler{simulateGetHandler}
	var writerHandlers = []simulateHandler{simulateGetHandler, simulatePutHandler}

	var versions = make(map[int]*QuickDB)
	versions[1] = NewQuickDB()

	db := btesting.MustCreateDBWithOption(t, openOption)

	var mutex sync.Mutex

	for n := 0; n < round; n++ {
		// Run n threads in parallel, each with their own operation.
		var threads = make(chan bool, parallelism)
		var wg sync.WaitGroup

		// counter for how many goroutines were fired
		var opCount int64

		// counter for ignored operations
		var igCount int64

		var errCh = make(chan error, threadCount)

		var i int
		for {
			// this buffered channel will keep accepting booleans
			// until it hits the limit defined by the parallelism
			// argument to testSimulate()
			threads <- true

			// this wait group can only be marked "done" from inside
			// the subsequent goroutine
			wg.Add(1)
			writable := ((rand.Int() % 100) < 20) // 20% writers

			// Choose an operation to execute.
			var handler simulateHandler
			if writable {
				handler = writerHandlers[rand.Intn(len(writerHandlers))]
			} else {
				handler = readerHandlers[rand.Intn(len(readerHandlers))]
			}

			// Execute a thread for the given operation.
			go func(writable bool, handler simulateHandler) {
				defer wg.Done()
				atomic.AddInt64(&opCount, 1)
				// Start transaction.
				tx, err := db.Begin(writable)
				if err != nil {
					errCh <- fmt.Errorf("error tx begin: %v", err)
					return
				}

				// Obtain current state of the dataset.
				mutex.Lock()
				var qdb = versions[tx.ID()]
				if writable {
					qdb = versions[tx.ID()-1].Copy()
				}
				mutex.Unlock()

				// Make sure we commit/rollback the tx at the end and update the state.
				if writable {
					defer func() {
						mutex.Lock()
						versions[tx.ID()] = qdb
						mutex.Unlock()

						if err := tx.Commit(); err != nil {
							errCh <- err
							return
						}
					}()
				} else {
					defer func() { _ = tx.Rollback() }()
				}

				// Ignore operation if we don't have data yet.
				if qdb == nil {
					atomic.AddInt64(&igCount, 1)
					return
				}

				// Execute handler.
				handler(tx, qdb)

				// Release a thread back to the scheduling loop.
				<-threads
			}(writable, handler)

			i++
			if i >= threadCount {
				break
			}
		}

		// Wait until all threads are done.
		wg.Wait()
		t.Logf("transactions:%d ignored:%d", opCount, igCount)
		close(errCh)
		for err := range errCh {
			if err != nil {
				t.Fatalf("error from inside goroutine: %v", err)
			}
		}

		db.MustClose()
		// I have doubts the DB drop is indented here (as 'versions' is not being reset).
		// But I'm preserving for now the original behavior.
		db.MustDeleteFile()
		db.MustReopen()
	}

}

type simulateHandler func(tx *bolt.Tx, qdb *QuickDB)

// Retrieves a key from the database and verifies that it is what is expected.
func simulateGetHandler(tx *bolt.Tx, qdb *QuickDB) {
	// Randomly retrieve an existing exist.
	keys := qdb.Rand()
	if len(keys) == 0 {
		return
	}

	// Retrieve root bucket.
	b := tx.Bucket(keys[0])
	if b == nil {
		panic(fmt.Sprintf("bucket[0] expected: %08x\n", trunc(keys[0], 4)))
	}

	// Drill into nested buckets.
	for _, key := range keys[1 : len(keys)-1] {
		b = b.Bucket(key)
		if b == nil {
			panic(fmt.Sprintf("bucket[n] expected: %v -> %v\n", keys, key))
		}
	}

	// Verify key/value on the final bucket.
	expected := qdb.Get(keys)
	actual := b.Get(keys[len(keys)-1])
	if !bytes.Equal(actual, expected) {
		fmt.Println("=== EXPECTED ===")
		fmt.Println(expected)
		fmt.Println("=== ACTUAL ===")
		fmt.Println(actual)
		fmt.Println("=== END ===")
		panic("value mismatch")
	}
}

// Inserts a key into the database.
func simulatePutHandler(tx *bolt.Tx, qdb *QuickDB) {
	var err error
	keys, value := randKeys(), randValue()

	// Retrieve root bucket.
	b := tx.Bucket(keys[0])
	if b == nil {
		b, err = tx.CreateBucket(keys[0])
		if err != nil {
			panic("create bucket: " + err.Error())
		}
	}

	// Create nested buckets, if necessary.
	for _, key := range keys[1 : len(keys)-1] {
		child := b.Bucket(key)
		if child != nil {
			b = child
		} else {
			b, err = b.CreateBucket(key)
			if err != nil {
				panic("create bucket: " + err.Error())
			}
		}
	}

	// Insert into database.
	if err := b.Put(keys[len(keys)-1], value); err != nil {
		panic("put: " + err.Error())
	}

	// Insert into in-memory database.
	qdb.Put(keys, value)
}

// QuickDB is an in-memory database that replicates the functionality of the
// Bolt DB type except that it is entirely in-memory. It is meant for testing
// that the Bolt database is consistent.
type QuickDB struct {
	sync.RWMutex
	m map[string]interface{}
}

// NewQuickDB returns an instance of QuickDB.
func NewQuickDB() *QuickDB {
	return &QuickDB{m: make(map[string]interface{})}
}

// Get retrieves the value at a key path.
func (db *QuickDB) Get(keys [][]byte) []byte {
	db.RLock()
	defer db.RUnlock()

	m := db.m
	for _, key := range keys[:len(keys)-1] {
		value := m[string(key)]
		if value == nil {
			return nil
		}
		switch value := value.(type) {
		case map[string]interface{}:
			m = value
		case []byte:
			return nil
		}
	}

	// Only return if it's a simple value.
	if value, ok := m[string(keys[len(keys)-1])].([]byte); ok {
		return value
	}
	return nil
}

// Put inserts a value into a key path.
func (db *QuickDB) Put(keys [][]byte, value []byte) {
	db.Lock()
	defer db.Unlock()

	// Build buckets all the way down the key path.
	m := db.m
	for _, key := range keys[:len(keys)-1] {
		if _, ok := m[string(key)].([]byte); ok {
			return // Keypath intersects with a simple value. Do nothing.
		}

		if m[string(key)] == nil {
			m[string(key)] = make(map[string]interface{})
		}
		m = m[string(key)].(map[string]interface{})
	}

	// Insert value into the last key.
	m[string(keys[len(keys)-1])] = value
}

// Rand returns a random key path that points to a simple value.
func (db *QuickDB) Rand() [][]byte {
	db.RLock()
	defer db.RUnlock()
	if len(db.m) == 0 {
		return nil
	}
	var keys [][]byte
	db.rand(db.m, &keys)
	return keys
}

func (db *QuickDB) rand(m map[string]interface{}, keys *[][]byte) {
	i, index := 0, rand.Intn(len(m))
	for k, v := range m {
		if i == index {
			*keys = append(*keys, []byte(k))
			if v, ok := v.(map[string]interface{}); ok {
				db.rand(v, keys)
			}
			return
		}
		i++
	}
	panic("quickdb rand: out-of-range")
}

// Copy copies the entire database.
func (db *QuickDB) Copy() *QuickDB {
	db.RLock()
	defer db.RUnlock()
	return &QuickDB{m: db.copy(db.m)}
}

func (db *QuickDB) copy(m map[string]interface{}) map[string]interface{} {
	clone := make(map[string]interface{}, len(m))
	for k, v := range m {
		switch v := v.(type) {
		case map[string]interface{}:
			clone[k] = db.copy(v)
		default:
			clone[k] = v
		}
	}
	return clone
}

func randKey() []byte {
	var min, max = 1, 1024
	n := rand.Intn(max-min) + min
	b := make([]byte, n)
	for i := 0; i < n; i++ {
		b[i] = byte(rand.Intn(255))
	}
	return b
}

func randKeys() [][]byte {
	var keys [][]byte
	var count = rand.Intn(2) + 2
	for i := 0; i < count; i++ {
		keys = append(keys, randKey())
	}
	return keys
}

func randValue() []byte {
	n := rand.Intn(8192)
	b := make([]byte, n)
	for i := 0; i < n; i++ {
		b[i] = byte(rand.Intn(255))
	}
	return b
}
```

## File: `tx.go`
```go
package bbolt

import (
	"errors"
	"fmt"
	"io"
	"os"
	"runtime"
	"sort"
	"strings"
	"sync/atomic"
	"time"
	"unsafe"

	berrors "go.etcd.io/bbolt/errors"
	"go.etcd.io/bbolt/internal/common"
)

// Tx represents a read-only or read/write transaction on the database.
// Read-only transactions can be used for retrieving values for keys and creating cursors.
// Read/write transactions can create and remove buckets and create and remove keys.
//
// IMPORTANT: You must commit or rollback transactions when you are done with
// them. Pages can not be reclaimed by the writer until no more transactions
// are using them. A long running read transaction can cause the database to
// quickly grow.
type Tx struct {
	writable       bool
	managed        bool
	db             *DB
	meta           *common.Meta
	root           Bucket
	pages          map[common.Pgid]*common.Page
	stats          TxStats
	commitHandlers []func()

	// WriteFlag specifies the flag for write-related methods like WriteTo().
	// Tx opens the database file with the specified flag to copy the data.
	//
	// By default, the flag is unset, which works well for mostly in-memory
	// workloads. For databases that are much larger than available RAM,
	// set the flag to syscall.O_DIRECT to avoid trashing the page cache.
	WriteFlag int
}

// init initializes the transaction.
func (tx *Tx) init(db *DB) {
	tx.db = db
	tx.pages = nil

	// Copy the meta page since it can be changed by the writer.
	tx.meta = &common.Meta{}
	db.meta().Copy(tx.meta)

	// Copy over the root bucket.
	tx.root = newBucket(tx)
	tx.root.InBucket = &common.InBucket{}
	*tx.root.InBucket = *(tx.meta.RootBucket())

	// Increment the transaction id and add a page cache for writable transactions.
	if tx.writable {
		tx.pages = make(map[common.Pgid]*common.Page)
		tx.meta.IncTxid()
	}
}

// ID returns the transaction id.
func (tx *Tx) ID() int {
	if tx == nil || tx.meta == nil {
		return -1
	}
	return int(tx.meta.Txid())
}

// DB returns a reference to the database that created the transaction.
func (tx *Tx) DB() *DB {
	return tx.db
}

// Size returns current database size in bytes as seen by this transaction.
func (tx *Tx) Size() int64 {
	return int64(tx.meta.Pgid()) * int64(tx.db.pageSize)
}

// Writable returns whether the transaction can perform write operations.
func (tx *Tx) Writable() bool {
	return tx.writable
}

// Cursor creates a cursor associated with the root bucket.
// All items in the cursor will return a nil value because all root bucket keys point to buckets.
// The cursor is only valid as long as the transaction is open.
// Do not use a cursor after the transaction is closed.
func (tx *Tx) Cursor() *Cursor {
	return tx.root.Cursor()
}

// Stats retrieves a copy of the current transaction statistics.
func (tx *Tx) Stats() TxStats {
	return tx.stats
}

// Inspect returns the structure of the database.
func (tx *Tx) Inspect() BucketStructure {
	return tx.root.Inspect()
}

// Bucket retrieves a bucket by name.
// Returns nil if the bucket does not exist.
// The bucket instance is only valid for the lifetime of the transaction.
func (tx *Tx) Bucket(name []byte) *Bucket {
	return tx.root.Bucket(name)
}

// CreateBucket creates a new bucket.
// Returns an error if the bucket already exists, if the bucket name is blank, or if the bucket name is too long.
// The bucket instance is only valid for the lifetime of the transaction.
func (tx *Tx) CreateBucket(name []byte) (*Bucket, error) {
	return tx.root.CreateBucket(name)
}

// CreateBucketIfNotExists creates a new bucket if it doesn't already exist.
// Returns an error if the bucket name is blank, or if the bucket name is too long.
// The bucket instance is only valid for the lifetime of the transaction.
func (tx *Tx) CreateBucketIfNotExists(name []byte) (*Bucket, error) {
	return tx.root.CreateBucketIfNotExists(name)
}

// DeleteBucket deletes a bucket.
// Returns an error if the bucket cannot be found or if the key represents a non-bucket value.
func (tx *Tx) DeleteBucket(name []byte) error {
	return tx.root.DeleteBucket(name)
}

// MoveBucket moves a sub-bucket from the source bucket to the destination bucket.
// Returns an error if
//  1. the sub-bucket cannot be found in the source bucket;
//  2. or the key already exists in the destination bucket;
//  3. the key represents a non-bucket value.
//
// If src is nil, it means moving a top level bucket into the target bucket.
// If dst is nil, it means converting the child bucket into a top level bucket.
func (tx *Tx) MoveBucket(child []byte, src *Bucket, dst *Bucket) error {
	if src == nil {
		src = &tx.root
	}
	if dst == nil {
		dst = &tx.root
	}
	return src.MoveBucket(child, dst)
}

// ForEach executes a function for each bucket in the root.
// If the provided function returns an error then the iteration is stopped and
// the error is returned to the caller.
func (tx *Tx) ForEach(fn func(name []byte, b *Bucket) error) error {
	return tx.root.ForEach(func(k, v []byte) error {
		return fn(k, tx.root.Bucket(k))
	})
}

// OnCommit adds a handler function to be executed after the transaction successfully commits.
func (tx *Tx) OnCommit(fn func()) {
	tx.commitHandlers = append(tx.commitHandlers, fn)
}

// Commit writes all changes to disk, updates the meta page and closes the transaction.
// Returns an error if a disk write error occurs, or if Commit is
// called on a read-only transaction.
func (tx *Tx) Commit() (err error) {
	txId := tx.ID()
	lg := tx.db.Logger()
	if lg != discardLogger {
		lg.Debugf("Committing transaction %d", txId)
		defer func() {
			if err != nil {
				lg.Errorf("Committing transaction failed: %v", err)
			} else {
				lg.Debugf("Committing transaction %d successfully", txId)
			}
		}()
	}

	common.Assert(!tx.managed, "managed tx commit not allowed")
	if tx.db == nil {
		return berrors.ErrTxClosed
	} else if !tx.writable {
		return berrors.ErrTxNotWritable
	}

	// TODO(benbjohnson): Use vectorized I/O to write out dirty pages.

	// Rebalance nodes which have had deletions.
	var startTime = time.Now()
	tx.root.rebalance()
	if tx.stats.GetRebalance() > 0 {
		tx.stats.IncRebalanceTime(time.Since(startTime))
	}

	opgid := tx.meta.Pgid()

	// spill data onto dirty pages.
	startTime = time.Now()
	if err = tx.root.spill(); err != nil {
		lg.Errorf("spilling data onto dirty pages failed: %v", err)
		tx.rollback()
		return err
	}
	tx.stats.IncSpillTime(time.Since(startTime))

	// Free the old root bucket.
	tx.meta.RootBucket().SetRootPage(tx.root.RootPage())

	// Free the old freelist because commit writes out a fresh freelist.
	if tx.meta.Freelist() != common.PgidNoFreelist {
		tx.db.freelist.Free(tx.meta.Txid(), tx.db.page(tx.meta.Freelist()))
	}

	if !tx.db.NoFreelistSync {
		err = tx.commitFreelist()
		if err != nil {
			lg.Errorf("committing freelist failed: %v", err)
			return err
		}
	} else {
		tx.meta.SetFreelist(common.PgidNoFreelist)
	}

	// If the high water mark has moved up then attempt to grow the database.
	if tx.meta.Pgid() > opgid {
		_ = errors.New("")
		// gofail: var lackOfDiskSpace string
		// tx.rollback()
		// return errors.New(lackOfDiskSpace)
		if err = tx.db.grow(int(tx.meta.Pgid()+1) * tx.db.pageSize); err != nil {
			lg.Errorf("growing db size failed, pgid: %d, pagesize: %d, error: %v", tx.meta.Pgid(), tx.db.pageSize, err)
			tx.rollback()
			return err
		}
	}

	// Write dirty pages to disk.
	startTime = time.Now()
	if err = tx.write(); err != nil {
		lg.Errorf("writing data failed: %v", err)
		tx.rollback()
		return err
	}

	// If strict mode is enabled then perform a consistency check.
	if tx.db.StrictMode {
		ch := tx.Check()
		var errs []string
		for {
			chkErr, ok := <-ch
			if !ok {
				break
			}
			errs = append(errs, chkErr.Error())
		}
		if len(errs) > 0 {
			panic("check fail: " + strings.Join(errs, "\n"))
		}
	}

	// Write meta to disk.
	if err = tx.writeMeta(); err != nil {
		lg.Errorf("writeMeta failed: %v", err)
		tx.rollback()
		return err
	}
	tx.stats.IncWriteTime(time.Since(startTime))

	// Finalize the transaction.
	tx.close()

	// Execute commit handlers now that the locks have been removed.
	for _, fn := range tx.commitHandlers {
		fn()
	}

	return nil
}

func (tx *Tx) commitFreelist() error {
	// Allocate new pages for the new free list. This will overestimate
	// the size of the freelist but not underestimate the size (which would be bad).
	p, err := tx.allocate((tx.db.freelist.EstimatedWritePageSize() / tx.db.pageSize) + 1)
	if err != nil {
		tx.rollback()
		return err
	}

	tx.db.freelist.Write(p)
	tx.meta.SetFreelist(p.Id())

	return nil
}

// Rollback closes the transaction and ignores all previous updates. Read-only
// transactions must be rolled back and not committed.
func (tx *Tx) Rollback() error {
	common.Assert(!tx.managed, "managed tx rollback not allowed")
	if tx.db == nil {
		return berrors.ErrTxClosed
	}
	tx.nonPhysicalRollback()
	return nil
}

// nonPhysicalRollback is called when user calls Rollback directly, in this case we do not need to reload the free pages from disk.
func (tx *Tx) nonPhysicalRollback() {
	if tx.db == nil {
		return
	}
	if tx.writable {
		tx.db.freelist.Rollback(tx.meta.Txid())
	}
	tx.close()
}

// rollback needs to reload the free pages from disk in case some system error happens like fsync error.
func (tx *Tx) rollback() {
	if tx.db == nil {
		return
	}
	if tx.writable {
		tx.db.freelist.Rollback(tx.meta.Txid())
		// When mmap fails, the `data`, `dataref` and `datasz` may be reset to
		// zero values, and there is no way to reload free page IDs in this case.
		if tx.db.data != nil {
			if !tx.db.hasSyncedFreelist() {
				// Reconstruct free page list by scanning the DB to get the whole free page list.
				// Note: scanning the whole db is heavy if your db size is large in NoSyncFreeList mode.
				tx.db.freelist.NoSyncReload(tx.db.freepages())
			} else {
				// Read free page list from freelist page.
				tx.db.freelist.Reload(tx.db.page(tx.db.meta().Freelist()))
			}
		}
	}
	tx.close()
}

func (tx *Tx) close() {
	if tx.db == nil {
		return
	}
	if tx.writable {
		// Grab freelist stats.
		var freelistFreeN = tx.db.freelist.FreeCount()
		var freelistPendingN = tx.db.freelist.PendingCount()
		var freelistAlloc = tx.db.freelist.EstimatedWritePageSize()

		// Remove transaction ref & writer lock.
		tx.db.rwtx = nil
		tx.db.rwlock.Unlock()

		// Merge statistics.
		if tx.db.stats != nil {
			tx.db.statlock.Lock()
			tx.db.stats.FreePageN = freelistFreeN
			tx.db.stats.PendingPageN = freelistPendingN
			tx.db.stats.FreeAlloc = (freelistFreeN + freelistPendingN) * tx.db.pageSize
			tx.db.stats.FreelistInuse = freelistAlloc
			tx.db.stats.TxStats.add(&tx.stats)
			tx.db.statlock.Unlock()
		}
	} else {
		tx.db.removeTx(tx)
	}

	// Clear all references.
	tx.db = nil
	tx.meta = nil
	tx.root = Bucket{tx: tx}
	tx.pages = nil
}

// Copy writes the entire database to a writer.
// This function exists for backwards compatibility.
//
// Deprecated: Use WriteTo() instead.
func (tx *Tx) Copy(w io.Writer) error {
	_, err := tx.WriteTo(w)
	return err
}

// WriteTo writes the entire database to a writer.
// If err == nil then exactly tx.Size() bytes will be written into the writer.
func (tx *Tx) WriteTo(w io.Writer) (n int64, err error) {
	var f *os.File
	// There is a risk that between the time a read-only transaction
	// is created and the time the file is actually opened, the
	// underlying db file at tx.db.path may have been replaced
	// (e.g. via rename). In that case, opening the file again would
	// unexpectedly point to a different file, rather than the one
	// the transaction was based on.
	//
	// To overcome this, we reuse the already opened file handle when
	// WriteFlag not set. When the WriteFlag is set, we reopen the file
	// but verify that it still refers to the same underlying file
	// (by device and inode). If it does not, we fall back to
	// reusing the existing already opened file handle.
	if tx.WriteFlag != 0 {
		// Attempt to open reader with WriteFlag
		f, err = tx.db.openFile(tx.db.path, os.O_RDONLY|tx.WriteFlag, 0)
		if err != nil {
			return 0, err
		}

		if ok, err := sameFile(tx.db.file, f); !ok {
			lg := tx.db.Logger()
			if cerr := f.Close(); cerr != nil {
				lg.Errorf("failed to close the file (%s): %v", tx.db.path, cerr)
			}
			lg.Warningf("The underlying file has changed, so reuse the already opened file (%s): %v", tx.db.path, err)
			f = tx.db.file
		} else {
			defer func() {
				if cerr := f.Close(); err == nil {
					err = cerr
				}
			}()
		}
	} else {
		f = tx.db.file
	}

	// Generate a meta page. We use the same page data for both meta pages.
	buf := make([]byte, tx.db.pageSize)
	page := (*common.Page)(unsafe.Pointer(&buf[0]))
	page.SetFlags(common.MetaPageFlag)
	*page.Meta() = *tx.meta

	// Write meta 0.
	page.SetId(0)
	page.Meta().SetChecksum(page.Meta().Sum64())
	nn, err := w.Write(buf)
	n += int64(nn)
	if err != nil {
		return n, fmt.Errorf("meta 0 copy: %s", err)
	}

	// Write meta 1 with a lower transaction id.
	page.SetId(1)
	page.Meta().DecTxid()
	page.Meta().SetChecksum(page.Meta().Sum64())
	nn, err = w.Write(buf)
	n += int64(nn)
	if err != nil {
		return n, fmt.Errorf("meta 1 copy: %s", err)
	}

	// Copy data pages using a SectionReader to avoid affecting f's offset.
	dataOffset := int64(tx.db.pageSize * 2)
	dataSize := tx.Size() - dataOffset
	sr := io.NewSectionReader(f, dataOffset, dataSize)

	// Copy data pages.
	wn, err := io.CopyN(w, sr, dataSize)
	n += wn
	if err != nil {
		return n, err
	}

	return n, nil
}

func sameFile(f1, f2 *os.File) (bool, error) {
	fi1, err := f1.Stat()
	if err != nil {
		return false, fmt.Errorf("failed to get fileInfo of the first file (%s): %w", f1.Name(), err)
	}
	fi2, err := f2.Stat()
	if err != nil {
		return false, fmt.Errorf("failed to get fileInfo of the second file (%s): %w", f2.Name(), err)
	}

	return os.SameFile(fi1, fi2), nil
}

// CopyFile copies the entire database to file at the given path.
// A reader transaction is maintained during the copy so it is safe to continue
// using the database while a copy is in progress.
func (tx *Tx) CopyFile(path string, mode os.FileMode) error {
	f, err := tx.db.openFile(path, os.O_RDWR|os.O_CREATE|os.O_TRUNC, mode)
	if err != nil {
		return err
	}

	_, err = tx.WriteTo(f)
	if err != nil {
		_ = f.Close()
		return err
	}
	return f.Close()
}

// allocate returns a contiguous block of memory starting at a given page.
func (tx *Tx) allocate(count int) (*common.Page, error) {
	lg := tx.db.Logger()
	p, err := tx.db.allocate(tx.meta.Txid(), count)
	if err != nil {
		lg.Errorf("allocating failed, txid: %d, count: %d, error: %v", tx.meta.Txid(), count, err)
		return nil, err
	}

	// Save to our page cache.
	tx.pages[p.Id()] = p

	// Update statistics.
	tx.stats.IncPageCount(int64(count))
	tx.stats.IncPageAlloc(int64(count * tx.db.pageSize))

	return p, nil
}

// write writes any dirty pages to disk.
func (tx *Tx) write() error {
	// Sort pages by id.
	lg := tx.db.Logger()
	pages := make(common.Pages, 0, len(tx.pages))
	for _, p := range tx.pages {
		pages = append(pages, p)
	}
	// Clear out page cache early.
	tx.pages = make(map[common.Pgid]*common.Page)
	sort.Sort(pages)

	// Write pages to disk in order.
	for _, p := range pages {
		rem := (uint64(p.Overflow()) + 1) * uint64(tx.db.pageSize)
		offset := int64(p.Id()) * int64(tx.db.pageSize)
		var written uintptr

		// Write out page in "max allocation" sized chunks.
		for {
			sz := rem
			if sz > common.MaxAllocSize-1 {
				sz = common.MaxAllocSize - 1
			}
			buf := common.UnsafeByteSlice(unsafe.Pointer(p), written, 0, int(sz))

			if _, err := tx.db.ops.writeAt(buf, offset); err != nil {
				lg.Errorf("writeAt failed, offset: %d: %w", offset, err)
				return err
			}

			// Update statistics.
			tx.stats.IncWrite(1)

			// Exit inner for loop if we've written all the chunks.
			rem -= sz
			if rem == 0 {
				break
			}

			// Otherwise move offset forward and move pointer to next chunk.
			offset += int64(sz)
			written += uintptr(sz)
		}
	}

	// Ignore file sync if flag is set on DB.
	if !tx.db.NoSync || common.IgnoreNoSync {
		// gofail: var beforeSyncDataPages struct{}
		if err := fdatasync(tx.db); err != nil {
			lg.Errorf("[GOOS: %s, GOARCH: %s] fdatasync failed: %w", runtime.GOOS, runtime.GOARCH, err)
			return err
		}
	}

	// Put small pages back to page pool.
	for _, p := range pages {
		// Ignore page sizes over 1 page.
		// These are allocated using make() instead of the page pool.
		if int(p.Overflow()) != 0 {
			continue
		}

		buf := common.UnsafeByteSlice(unsafe.Pointer(p), 0, 0, tx.db.pageSize)

		// See https://go.googlesource.com/go/+/f03c9202c43e0abb130669852082117ca50aa9b1
		for i := range buf {
			buf[i] = 0
		}
		tx.db.pagePool.Put(buf) //nolint:staticcheck
	}

	return nil
}

// writeMeta writes the meta to the disk.
func (tx *Tx) writeMeta() error {
	// gofail: var beforeWriteMetaError string
	// return errors.New(beforeWriteMetaError)

	// Create a temporary buffer for the meta page.
	lg := tx.db.Logger()
	buf := make([]byte, tx.db.pageSize)
	p := tx.db.pageInBuffer(buf, 0)
	tx.meta.Write(p)

	// Write the meta page to file.
	tx.db.metalock.Lock()
	if _, err := tx.db.ops.writeAt(buf, int64(p.Id())*int64(tx.db.pageSize)); err != nil {
		tx.db.metalock.Unlock()
		lg.Errorf("writeAt failed, pgid: %d, pageSize: %d, error: %v", p.Id(), tx.db.pageSize, err)
		return err
	}
	tx.db.metalock.Unlock()
	if !tx.db.NoSync || common.IgnoreNoSync {
		// gofail: var beforeSyncMetaPage struct{}
		if err := fdatasync(tx.db); err != nil {
			lg.Errorf("[GOOS: %s, GOARCH: %s] fdatasync failed: %w", runtime.GOOS, runtime.GOARCH, err)
			return err
		}
	}

	// Update statistics.
	tx.stats.IncWrite(1)

	return nil
}

// page returns a reference to the page with a given id.
// If page has been written to then a temporary buffered page is returned.
func (tx *Tx) page(id common.Pgid) *common.Page {
	// Check the dirty pages first.
	if tx.pages != nil {
		if p, ok := tx.pages[id]; ok {
			p.FastCheck(id)
			return p
		}
	}

	// Otherwise return directly from the mmap.
	p := tx.db.page(id)
	p.FastCheck(id)
	return p
}

// forEachPage iterates over every page within a given page and executes a function.
func (tx *Tx) forEachPage(pgidnum common.Pgid, fn func(*common.Page, int, []common.Pgid)) {
	stack := make([]common.Pgid, 10)
	stack[0] = pgidnum
	tx.forEachPageInternal(stack[:1], fn)
}

func (tx *Tx) forEachPageInternal(pgidstack []common.Pgid, fn func(*common.Page, int, []common.Pgid)) {
	p := tx.page(pgidstack[len(pgidstack)-1])

	// Execute function.
	fn(p, len(pgidstack)-1, pgidstack)

	// Recursively loop over children.
	if p.IsBranchPage() {
		for i := 0; i < int(p.Count()); i++ {
			elem := p.BranchPageElement(uint16(i))
			tx.forEachPageInternal(append(pgidstack, elem.Pgid()), fn)
		}
	}
}

// Page returns page information for a given page number.
// This is only safe for concurrent use when used by a writable transaction.
func (tx *Tx) Page(id int) (*common.PageInfo, error) {
	if tx.db == nil {
		return nil, berrors.ErrTxClosed
	} else if common.Pgid(id) >= tx.meta.Pgid() {
		return nil, nil
	}

	if tx.db.freelist == nil {
		return nil, berrors.ErrFreePagesNotLoaded
	}

	// Build the page info.
	p := tx.db.page(common.Pgid(id))
	info := &common.PageInfo{
		ID:            id,
		Count:         int(p.Count()),
		OverflowCount: int(p.Overflow()),
	}

	// Determine the type (or if it's free).
	if tx.db.freelist.Freed(common.Pgid(id)) {
		info.Type = "free"
	} else {
		info.Type = p.Typ()
	}

	return info, nil
}

// TxStats represents statistics about the actions performed by the transaction.
type TxStats struct {
	// Page statistics.
	//
	// DEPRECATED: Use GetPageCount() or IncPageCount()
	PageCount int64 // number of page allocations
	// DEPRECATED: Use GetPageAlloc() or IncPageAlloc()
	PageAlloc int64 // total bytes allocated

	// Cursor statistics.
	//
	// DEPRECATED: Use GetCursorCount() or IncCursorCount()
	CursorCount int64 // number of cursors created

	// Node statistics
	//
	// DEPRECATED: Use GetNodeCount() or IncNodeCount()
	NodeCount int64 // number of node allocations
	// DEPRECATED: Use GetNodeDeref() or IncNodeDeref()
	NodeDeref int64 // number of node dereferences

	// Rebalance statistics.
	//
	// DEPRECATED: Use GetRebalance() or IncRebalance()
	Rebalance int64 // number of node rebalances
	// DEPRECATED: Use GetRebalanceTime() or IncRebalanceTime()
	RebalanceTime time.Duration // total time spent rebalancing

	// Split/Spill statistics.
	//
	// DEPRECATED: Use GetSplit() or IncSplit()
	Split int64 // number of nodes split
	// DEPRECATED: Use GetSpill() or IncSpill()
	Spill int64 // number of nodes spilled
	// DEPRECATED: Use GetSpillTime() or IncSpillTime()
	SpillTime time.Duration // total time spent spilling

	// Write statistics.
	//
	// DEPRECATED: Use GetWrite() or IncWrite()
	Write int64 // number of writes performed
	// DEPRECATED: Use GetWriteTime() or IncWriteTime()
	WriteTime time.Duration // total time spent writing to disk
}

func (s *TxStats) add(other *TxStats) {
	s.IncPageCount(other.GetPageCount())
	s.IncPageAlloc(other.GetPageAlloc())
	s.IncCursorCount(other.GetCursorCount())
	s.IncNodeCount(other.GetNodeCount())
	s.IncNodeDeref(other.GetNodeDeref())
	s.IncRebalance(other.GetRebalance())
	s.IncRebalanceTime(other.GetRebalanceTime())
	s.IncSplit(other.GetSplit())
	s.IncSpill(other.GetSpill())
	s.IncSpillTime(other.GetSpillTime())
	s.IncWrite(other.GetWrite())
	s.IncWriteTime(other.GetWriteTime())
}

// Sub calculates and returns the difference between two sets of transaction stats.
// This is useful when obtaining stats at two different points and time and
// you need the performance counters that occurred within that time span.
func (s *TxStats) Sub(other *TxStats) TxStats {
	var diff TxStats
	diff.PageCount = s.GetPageCount() - other.GetPageCount()
	diff.PageAlloc = s.GetPageAlloc() - other.GetPageAlloc()
	diff.CursorCount = s.GetCursorCount() - other.GetCursorCount()
	diff.NodeCount = s.GetNodeCount() - other.GetNodeCount()
	diff.NodeDeref = s.GetNodeDeref() - other.GetNodeDeref()
	diff.Rebalance = s.GetRebalance() - other.GetRebalance()
	diff.RebalanceTime = s.GetRebalanceTime() - other.GetRebalanceTime()
	diff.Split = s.GetSplit() - other.GetSplit()
	diff.Spill = s.GetSpill() - other.GetSpill()
	diff.SpillTime = s.GetSpillTime() - other.GetSpillTime()
	diff.Write = s.GetWrite() - other.GetWrite()
	diff.WriteTime = s.GetWriteTime() - other.GetWriteTime()
	return diff
}

// GetPageCount returns PageCount atomically.
func (s *TxStats) GetPageCount() int64 {
	return atomic.LoadInt64(&s.PageCount)
}

// IncPageCount increases PageCount atomically and returns the new value.
func (s *TxStats) IncPageCount(delta int64) int64 {
	return atomic.AddInt64(&s.PageCount, delta)
}

// GetPageAlloc returns PageAlloc atomically.
func (s *TxStats) GetPageAlloc() int64 {
	return atomic.LoadInt64(&s.PageAlloc)
}

// IncPageAlloc increases PageAlloc atomically and returns the new value.
func (s *TxStats) IncPageAlloc(delta int64) int64 {
	return atomic.AddInt64(&s.PageAlloc, delta)
}

// GetCursorCount returns CursorCount atomically.
func (s *TxStats) GetCursorCount() int64 {
	return atomic.LoadInt64(&s.CursorCount)
}

// IncCursorCount increases CursorCount atomically and return the new value.
func (s *TxStats) IncCursorCount(delta int64) int64 {
	return atomic.AddInt64(&s.CursorCount, delta)
}

// GetNodeCount returns NodeCount atomically.
func (s *TxStats) GetNodeCount() int64 {
	return atomic.LoadInt64(&s.NodeCount)
}

// IncNodeCount increases NodeCount atomically and returns the new value.
func (s *TxStats) IncNodeCount(delta int64) int64 {
	return atomic.AddInt64(&s.NodeCount, delta)
}

// GetNodeDeref returns NodeDeref atomically.
func (s *TxStats) GetNodeDeref() int64 {
	return atomic.LoadInt64(&s.NodeDeref)
}

// IncNodeDeref increases NodeDeref atomically and returns the new value.
func (s *TxStats) IncNodeDeref(delta int64) int64 {
	return atomic.AddInt64(&s.NodeDeref, delta)
}

// GetRebalance returns Rebalance atomically.
func (s *TxStats) GetRebalance() int64 {
	return atomic.LoadInt64(&s.Rebalance)
}

// IncRebalance increases Rebalance atomically and returns the new value.
func (s *TxStats) IncRebalance(delta int64) int64 {
	return atomic.AddInt64(&s.Rebalance, delta)
}

// GetRebalanceTime returns RebalanceTime atomically.
func (s *TxStats) GetRebalanceTime() time.Duration {
	return atomicLoadDuration(&s.RebalanceTime)
}

// IncRebalanceTime increases RebalanceTime atomically and returns the new value.
func (s *TxStats) IncRebalanceTime(delta time.Duration) time.Duration {
	return atomicAddDuration(&s.RebalanceTime, delta)
}

// GetSplit returns Split atomically.
func (s *TxStats) GetSplit() int64 {
	return atomic.LoadInt64(&s.Split)
}

// IncSplit increases Split atomically and returns the new value.
func (s *TxStats) IncSplit(delta int64) int64 {
	return atomic.AddInt64(&s.Split, delta)
}

// GetSpill returns Spill atomically.
func (s *TxStats) GetSpill() int64 {
	return atomic.LoadInt64(&s.Spill)
}

// IncSpill increases Spill atomically and returns the new value.
func (s *TxStats) IncSpill(delta int64) int64 {
	return atomic.AddInt64(&s.Spill, delta)
}

// GetSpillTime returns SpillTime atomically.
func (s *TxStats) GetSpillTime() time.Duration {
	return atomicLoadDuration(&s.SpillTime)
}

// IncSpillTime increases SpillTime atomically and returns the new value.
func (s *TxStats) IncSpillTime(delta time.Duration) time.Duration {
	return atomicAddDuration(&s.SpillTime, delta)
}

// GetWrite returns Write atomically.
func (s *TxStats) GetWrite() int64 {
	return atomic.LoadInt64(&s.Write)
}

// IncWrite increases Write atomically and returns the new value.
func (s *TxStats) IncWrite(delta int64) int64 {
	return atomic.AddInt64(&s.Write, delta)
}

// GetWriteTime returns WriteTime atomically.
func (s *TxStats) GetWriteTime() time.Duration {
	return atomicLoadDuration(&s.WriteTime)
}

// IncWriteTime increases WriteTime atomically and returns the new value.
func (s *TxStats) IncWriteTime(delta time.Duration) time.Duration {
	return atomicAddDuration(&s.WriteTime, delta)
}

func atomicAddDuration(ptr *time.Duration, du time.Duration) time.Duration {
	return time.Duration(atomic.AddInt64((*int64)(unsafe.Pointer(ptr)), int64(du)))
}

func atomicLoadDuration(ptr *time.Duration) time.Duration {
	return time.Duration(atomic.LoadInt64((*int64)(unsafe.Pointer(ptr))))
}
```

## File: `tx_check.go`
```go
package bbolt

import (
	"encoding/hex"
	"fmt"

	"go.etcd.io/bbolt/internal/common"
)

// Check performs several consistency checks on the database for this transaction.
// An error is returned if any inconsistency is found.
//
// It can be safely run concurrently on a writable transaction. However, this
// incurs a high cost for large databases and databases with a lot of subbuckets
// because of caching. This overhead can be removed if running on a read-only
// transaction, however, it is not safe to execute other writer transactions at
// the same time.
//
// It also allows users to provide a customized `KVStringer` implementation,
// so that bolt can generate human-readable diagnostic messages.
func (tx *Tx) Check(options ...CheckOption) <-chan error {
	chkConfig := checkConfig{
		kvStringer: HexKVStringer(),
	}
	for _, op := range options {
		op(&chkConfig)
	}

	ch := make(chan error)
	go func() {
		// Close the channel to signal completion.
		defer close(ch)
		tx.check(chkConfig, ch)
	}()
	return ch
}

func (tx *Tx) check(cfg checkConfig, ch chan error) {
	defer func() {
		if r := recover(); r != nil {
			ch <- panicked{r}
		}
	}()
	// Force loading free list if opened in ReadOnly mode.
	tx.db.loadFreelist()

	// Check if any pages are double freed.
	freed := make(map[common.Pgid]bool)
	all := make([]common.Pgid, tx.db.freelist.Count())
	tx.db.freelist.Copyall(all)
	for _, id := range all {
		if freed[id] {
			ch <- fmt.Errorf("page %d: already freed", id)
		}
		freed[id] = true
	}

	// Track every reachable page.
	reachable := make(map[common.Pgid]*common.Page)
	reachable[0] = tx.page(0) // meta0
	reachable[1] = tx.page(1) // meta1
	if tx.meta.Freelist() != common.PgidNoFreelist {
		for i := uint32(0); i <= tx.page(tx.meta.Freelist()).Overflow(); i++ {
			reachable[tx.meta.Freelist()+common.Pgid(i)] = tx.page(tx.meta.Freelist())
		}
	}

	if cfg.pageId == 0 {
		// Check the whole db file, starting from the root bucket and
		// recursively check all child buckets.
		tx.recursivelyCheckBucket(&tx.root, reachable, freed, cfg.kvStringer, ch)

		// Ensure all pages below high water mark are either reachable or freed.
		for i := common.Pgid(0); i < tx.meta.Pgid(); i++ {
			_, isReachable := reachable[i]
			if !isReachable && !freed[i] {
				ch <- fmt.Errorf("page %d: unreachable unfreed", int(i))
			}
		}
	} else {
		// Check the db file starting from a specified pageId.
		if cfg.pageId < 2 || cfg.pageId >= uint64(tx.meta.Pgid()) {
			ch <- fmt.Errorf("page ID (%d) out of range [%d, %d)", cfg.pageId, 2, tx.meta.Pgid())
			return
		}

		tx.recursivelyCheckPage(common.Pgid(cfg.pageId), reachable, freed, cfg.kvStringer, ch)
	}
}

func (tx *Tx) recursivelyCheckPage(pageId common.Pgid, reachable map[common.Pgid]*common.Page, freed map[common.Pgid]bool,
	kvStringer KVStringer, ch chan error) {
	tx.checkInvariantProperties(pageId, reachable, freed, kvStringer, ch)
	tx.recursivelyCheckBucketInPage(pageId, reachable, freed, kvStringer, ch)
}

func (tx *Tx) recursivelyCheckBucketInPage(pageId common.Pgid, reachable map[common.Pgid]*common.Page, freed map[common.Pgid]bool,
	kvStringer KVStringer, ch chan error) {
	p := tx.page(pageId)

	switch {
	case p.IsBranchPage():
		for i := range p.BranchPageElements() {
			elem := p.BranchPageElement(uint16(i))
			tx.recursivelyCheckBucketInPage(elem.Pgid(), reachable, freed, kvStringer, ch)
		}
	case p.IsLeafPage():
		for i := range p.LeafPageElements() {
			elem := p.LeafPageElement(uint16(i))
			if elem.IsBucketEntry() {
				inBkt := common.NewInBucket(pageId, 0)
				tmpBucket := Bucket{
					InBucket:    &inBkt,
					rootNode:    &node{isLeaf: p.IsLeafPage()},
					FillPercent: DefaultFillPercent,
					tx:          tx,
				}
				if child := tmpBucket.Bucket(elem.Key()); child != nil {
					tx.recursivelyCheckBucket(child, reachable, freed, kvStringer, ch)
				}
			}
		}
	default:
		ch <- fmt.Errorf("unexpected page type (flags: %x) for pgId:%d", p.Flags(), pageId)
	}
}

func (tx *Tx) recursivelyCheckBucket(b *Bucket, reachable map[common.Pgid]*common.Page, freed map[common.Pgid]bool,
	kvStringer KVStringer, ch chan error) {
	// Ignore inline buckets.
	if b.RootPage() == 0 {
		return
	}

	tx.checkInvariantProperties(b.RootPage(), reachable, freed, kvStringer, ch)

	// Check each bucket within this bucket.
	_ = b.ForEachBucket(func(k []byte) error {
		if child := b.Bucket(k); child != nil {
			tx.recursivelyCheckBucket(child, reachable, freed, kvStringer, ch)
		}
		return nil
	})
}

func (tx *Tx) checkInvariantProperties(pageId common.Pgid, reachable map[common.Pgid]*common.Page, freed map[common.Pgid]bool,
	kvStringer KVStringer, ch chan error) {
	tx.forEachPage(pageId, func(p *common.Page, _ int, stack []common.Pgid) {
		verifyPageReachable(p, tx.meta.Pgid(), stack, reachable, freed, ch)
	})

	tx.recursivelyCheckPageKeyOrder(pageId, kvStringer.KeyToString, ch)
}

func verifyPageReachable(p *common.Page, hwm common.Pgid, stack []common.Pgid, reachable map[common.Pgid]*common.Page, freed map[common.Pgid]bool, ch chan error) {
	if p.Id() > hwm {
		ch <- fmt.Errorf("page %d: out of bounds: %d (stack: %v)", int(p.Id()), int(hwm), stack)
	}

	// Ensure each page is only referenced once.
	for i := common.Pgid(0); i <= common.Pgid(p.Overflow()); i++ {
		var id = p.Id() + i
		if _, ok := reachable[id]; ok {
			ch <- fmt.Errorf("page %d: multiple references (stack: %v)", int(id), stack)
		}
		reachable[id] = p
	}

	// We should only encounter un-freed leaf and branch pages.
	if freed[p.Id()] {
		ch <- fmt.Errorf("page %d: reachable freed", int(p.Id()))
	} else if !p.IsBranchPage() && !p.IsLeafPage() {
		ch <- fmt.Errorf("page %d: invalid type: %s (stack: %v)", int(p.Id()), p.Typ(), stack)
	}
}

// recursivelyCheckPageKeyOrder verifies database consistency with respect to b-tree
// key order constraints:
//   - keys on pages must be sorted
//   - keys on children pages are between 2 consecutive keys on the parent's branch page).
func (tx *Tx) recursivelyCheckPageKeyOrder(pgId common.Pgid, keyToString func([]byte) string, ch chan error) {
	tx.recursivelyCheckPageKeyOrderInternal(pgId, nil, nil, nil, keyToString, ch)
}

// recursivelyCheckPageKeyOrderInternal verifies that all keys in the subtree rooted at `pgid` are:
//   - >=`minKeyClosed` (can be nil)
//   - <`maxKeyOpen` (can be nil)
//   - Are in right ordering relationship to their parents.
//     `pagesStack` is expected to contain IDs of pages from the tree root to `pgid` for the clean debugging message.
func (tx *Tx) recursivelyCheckPageKeyOrderInternal(
	pgId common.Pgid, minKeyClosed, maxKeyOpen []byte, pagesStack []common.Pgid,
	keyToString func([]byte) string, ch chan error) (maxKeyInSubtree []byte) {

	p := tx.page(pgId)
	pagesStack = append(pagesStack, pgId)
	switch {
	case p.IsBranchPage():
		// For branch page we navigate ranges of all subpages.
		runningMin := minKeyClosed
		for i := range p.BranchPageElements() {
			elem := p.BranchPageElement(uint16(i))
			verifyKeyOrder(elem.Pgid(), "branch", i, elem.Key(), runningMin, maxKeyOpen, ch, keyToString, pagesStack)

			maxKey := maxKeyOpen
			if i < len(p.BranchPageElements())-1 {
				maxKey = p.BranchPageElement(uint16(i + 1)).Key()
			}
			maxKeyInSubtree = tx.recursivelyCheckPageKeyOrderInternal(elem.Pgid(), elem.Key(), maxKey, pagesStack, keyToString, ch)
			runningMin = maxKeyInSubtree
		}
		return maxKeyInSubtree
	case p.IsLeafPage():
		runningMin := minKeyClosed
		for i := range p.LeafPageElements() {
			elem := p.LeafPageElement(uint16(i))
			verifyKeyOrder(pgId, "leaf", i, elem.Key(), runningMin, maxKeyOpen, ch, keyToString, pagesStack)
			runningMin = elem.Key()
		}
		if p.Count() > 0 {
			return p.LeafPageElement(p.Count() - 1).Key()
		}
	default:
		ch <- fmt.Errorf("unexpected page type (flags: %x) for pgId:%d", p.Flags(), pgId)
	}
	return maxKeyInSubtree
}

/***
 * verifyKeyOrder checks whether an entry with given #index on pgId (pageType: "branch|leaf") that has given "key",
 * is within range determined by (previousKey..maxKeyOpen) and reports found violations to the channel (ch).
 */
func verifyKeyOrder(pgId common.Pgid, pageType string, index int, key []byte, previousKey []byte, maxKeyOpen []byte, ch chan error, keyToString func([]byte) string, pagesStack []common.Pgid) {
	if index == 0 && previousKey != nil && compareKeys(previousKey, key) > 0 {
		ch <- fmt.Errorf("the first key[%d]=(hex)%s on %s page(%d) needs to be >= the key in the ancestor (%s). Stack: %v",
			index, keyToString(key), pageType, pgId, keyToString(previousKey), pagesStack)
	}
	if index > 0 {
		cmpRet := compareKeys(previousKey, key)
		if cmpRet > 0 {
			ch <- fmt.Errorf("key[%d]=(hex)%s on %s page(%d) needs to be > (found <) than previous element (hex)%s. Stack: %v",
				index, keyToString(key), pageType, pgId, keyToString(previousKey), pagesStack)
		}
		if cmpRet == 0 {
			ch <- fmt.Errorf("key[%d]=(hex)%s on %s page(%d) needs to be > (found =) than previous element (hex)%s. Stack: %v",
				index, keyToString(key), pageType, pgId, keyToString(previousKey), pagesStack)
		}
	}
	if maxKeyOpen != nil && compareKeys(key, maxKeyOpen) >= 0 {
		ch <- fmt.Errorf("key[%d]=(hex)%s on %s page(%d) needs to be < than key of the next element in ancestor (hex)%s. Pages stack: %v",
			index, keyToString(key), pageType, pgId, keyToString(previousKey), pagesStack)
	}
}

// ===========================================================================================

type checkConfig struct {
	kvStringer KVStringer
	pageId     uint64
}

type CheckOption func(options *checkConfig)

func WithKVStringer(kvStringer KVStringer) CheckOption {
	return func(c *checkConfig) {
		c.kvStringer = kvStringer
	}
}

// WithPageId sets a page ID from which the check command starts to check
func WithPageId(pageId uint64) CheckOption {
	return func(c *checkConfig) {
		c.pageId = pageId
	}
}

// KVStringer allows to prepare human-readable diagnostic messages.
type KVStringer interface {
	KeyToString([]byte) string
	ValueToString([]byte) string
}

// HexKVStringer serializes both key & value to hex representation.
func HexKVStringer() KVStringer {
	return hexKvStringer{}
}

type hexKvStringer struct{}

func (hexKvStringer) KeyToString(key []byte) string {
	return hex.EncodeToString(key)
}

func (hexKvStringer) ValueToString(value []byte) string {
	return hex.EncodeToString(value)
}
```

## File: `tx_check_test.go`
```go
package bbolt_test

import (
	"fmt"
	"math/rand"
	"testing"

	"github.com/stretchr/testify/require"

	"go.etcd.io/bbolt"
	"go.etcd.io/bbolt/internal/btesting"
	"go.etcd.io/bbolt/internal/common"
	"go.etcd.io/bbolt/internal/guts_cli"
)

func TestTx_Check_CorruptPage(t *testing.T) {
	bucketName := []byte("data")

	t.Log("Creating db file.")
	db := btesting.MustCreateDBWithOption(t, &bbolt.Options{PageSize: 4096})

	// Each page can hold roughly 20 key/values pair, so 100 such
	// key/value pairs will consume about 5 leaf pages.
	err := db.Fill(bucketName, 1, 100,
		func(tx int, k int) []byte { return []byte(fmt.Sprintf("%04d", k)) },
		func(tx int, k int) []byte { return make([]byte, 100) },
	)
	require.NoError(t, err)

	t.Log("Corrupting a random leaf page.")
	victimPageId, validPageIds := corruptRandomLeafPageInBucket(t, db.DB, bucketName)

	t.Log("Running consistency check.")
	vErr := db.View(func(tx *bbolt.Tx) error {
		var cErrs []error

		t.Log("Check corrupted page.")
		errChan := tx.Check(bbolt.WithPageId(uint64(victimPageId)))
		for cErr := range errChan {
			cErrs = append(cErrs, cErr)
		}
		require.Greater(t, len(cErrs), 0)

		t.Log("Check valid pages.")
		cErrs = cErrs[:0]
		for _, pgId := range validPageIds {
			errChan = tx.Check(bbolt.WithPageId(uint64(pgId)))
			for cErr := range errChan {
				cErrs = append(cErrs, cErr)
			}
			require.Equal(t, 0, len(cErrs))
		}
		return nil
	})
	require.NoError(t, vErr)
	t.Log("All check passed")

	// Manually close the db, otherwise the PostTestCleanup will
	// check the db again and accordingly fail the test.
	db.MustClose()
}

func TestTx_Check_WithNestBucket(t *testing.T) {
	parentBucketName := []byte("parentBucket")

	t.Log("Creating db file.")
	db := btesting.MustCreateDBWithOption(t, &bbolt.Options{PageSize: 4096})

	err := db.Update(func(tx *bbolt.Tx) error {
		pb, bErr := tx.CreateBucket(parentBucketName)
		if bErr != nil {
			return bErr
		}

		t.Log("put some key/values under the parent bucket directly")
		for i := 0; i < 10; i++ {
			k, v := fmt.Sprintf("%04d", i), fmt.Sprintf("value_%4d", i)
			if pErr := pb.Put([]byte(k), []byte(v)); pErr != nil {
				return pErr
			}
		}

		t.Log("create a nested bucket and put some key/values under the nested bucket")
		cb, bErr := pb.CreateBucket([]byte("nestedBucket"))
		if bErr != nil {
			return bErr
		}

		for i := 0; i < 2000; i++ {
			k, v := fmt.Sprintf("%04d", i), fmt.Sprintf("value_%4d", i)
			if pErr := cb.Put([]byte(k), []byte(v)); pErr != nil {
				return pErr
			}
		}

		return nil
	})
	require.NoError(t, err)

	// Get the bucket's root page.
	bucketRootPageId := mustGetBucketRootPage(t, db.DB, parentBucketName)

	t.Logf("Running consistency check starting from pageId: %d", bucketRootPageId)
	vErr := db.View(func(tx *bbolt.Tx) error {
		var cErrs []error

		errChan := tx.Check(bbolt.WithPageId(uint64(bucketRootPageId)))
		for cErr := range errChan {
			cErrs = append(cErrs, cErr)
		}
		require.Equal(t, 0, len(cErrs))

		return nil
	})
	require.NoError(t, vErr)
	t.Log("All check passed")

	// Manually close the db, otherwise the PostTestCleanup will
	// check the db again and accordingly fail the test.
	db.MustClose()
}

func TestTx_Check_Panic(t *testing.T) {
	bucketName := []byte("data")
	t.Log("Creating db file.")
	db := btesting.MustCreateDBWithOption(t, &bbolt.Options{PageSize: 4096})

	// Each page can hold roughly 20 key/values pair, so 100 such
	// key/value pairs will consume about 5 leaf pages.
	err := db.Fill(bucketName, 1, 100,
		func(tx int, k int) []byte { return []byte(fmt.Sprintf("%04d", k)) },
		func(tx int, k int) []byte { return make([]byte, 100) },
	)
	require.NoError(t, err)

	corruptRootPage(t, db.DB, bucketName)

	path := db.Path()

	require.NoError(t, db.Close())

	db = btesting.MustOpenDBWithOption(t, path, &bbolt.Options{PageSize: 4096})

	vErr := db.View(func(tx *bbolt.Tx) error {
		errChan := tx.Check()
		for cErr := range errChan {
			fmt.Println("cErr", cErr)
			return cErr
		}
		return nil
	})
	require.Error(t, vErr)
	require.ErrorContains(t, vErr, "has unexpected type/flags: 0")

	// Manually close the db, otherwise the PostTestCleanup will
	// check the db again and accordingly fail the test.
	db.MustClose()
}

// corruptRandomLeafPage corrupts one random leaf page.
func corruptRandomLeafPageInBucket(t testing.TB, db *bbolt.DB, bucketName []byte) (victimPageId common.Pgid, validPageIds []common.Pgid) {
	bucketRootPageId := mustGetBucketRootPage(t, db, bucketName)
	bucketRootPage, _, err := guts_cli.ReadPage(db.Path(), uint64(bucketRootPageId))
	require.NoError(t, err)
	require.True(t, bucketRootPage.IsBranchPage())

	// Retrieve all the leaf pages included in the branch page, and pick up random one from them.
	var bucketPageIds []common.Pgid
	for _, bpe := range bucketRootPage.BranchPageElements() {
		bucketPageIds = append(bucketPageIds, bpe.Pgid())
	}
	randomIdx := rand.Intn(len(bucketPageIds))
	victimPageId = bucketPageIds[randomIdx]
	validPageIds = append(bucketPageIds[:randomIdx], bucketPageIds[randomIdx+1:]...)

	victimPage, victimBuf, err := guts_cli.ReadPage(db.Path(), uint64(victimPageId))
	require.NoError(t, err)
	require.True(t, victimPage.IsLeafPage())
	require.True(t, victimPage.Count() > 1)

	// intentionally make the second key < the first key.
	element := victimPage.LeafPageElement(1)
	key := element.Key()
	key[0] = 0

	// Write the corrupt page to db file.
	err = guts_cli.WritePage(db.Path(), victimBuf)
	require.NoError(t, err)
	return victimPageId, validPageIds
}

func corruptRootPage(t testing.TB, db *bbolt.DB, bucketName []byte) {
	bucketRootPageId := mustGetBucketRootPage(t, db, bucketName)
	bucketRootPage, bucketRootPageBuf, err := guts_cli.ReadPage(db.Path(), uint64(bucketRootPageId))
	require.NoError(t, err)
	require.True(t, bucketRootPage.IsBranchPage())

	bucketRootPage.SetFlags(0)

	err = guts_cli.WritePage(db.Path(), bucketRootPageBuf)
	require.NoError(t, err)
}

// mustGetBucketRootPage returns the root page for the provided bucket.
func mustGetBucketRootPage(t testing.TB, db *bbolt.DB, bucketName []byte) common.Pgid {
	var rootPageId common.Pgid
	_ = db.View(func(tx *bbolt.Tx) error {
		b := tx.Bucket(bucketName)
		require.NotNil(t, b)
		rootPageId = b.RootPage()
		return nil
	})

	return rootPageId
}
```

## File: `tx_stats_test.go`
```go
package bbolt

import (
	"testing"
	"time"

	"github.com/stretchr/testify/assert"
)

func TestTxStats_add(t *testing.T) {
	statsA := TxStats{
		PageCount:     1,
		PageAlloc:     2,
		CursorCount:   3,
		NodeCount:     100,
		NodeDeref:     101,
		Rebalance:     1000,
		RebalanceTime: 1001 * time.Second,
		Split:         10000,
		Spill:         10001,
		SpillTime:     10001 * time.Second,
		Write:         100000,
		WriteTime:     100001 * time.Second,
	}

	statsB := TxStats{
		PageCount:     2,
		PageAlloc:     3,
		CursorCount:   4,
		NodeCount:     101,
		NodeDeref:     102,
		Rebalance:     1001,
		RebalanceTime: 1002 * time.Second,
		Split:         11001,
		Spill:         11002,
		SpillTime:     11002 * time.Second,
		Write:         110001,
		WriteTime:     110010 * time.Second,
	}

	statsB.add(&statsA)
	assert.Equal(t, int64(3), statsB.GetPageCount())
	assert.Equal(t, int64(5), statsB.GetPageAlloc())
	assert.Equal(t, int64(7), statsB.GetCursorCount())
	assert.Equal(t, int64(201), statsB.GetNodeCount())
	assert.Equal(t, int64(203), statsB.GetNodeDeref())
	assert.Equal(t, int64(2001), statsB.GetRebalance())
	assert.Equal(t, 2003*time.Second, statsB.GetRebalanceTime())
	assert.Equal(t, int64(21001), statsB.GetSplit())
	assert.Equal(t, int64(21003), statsB.GetSpill())
	assert.Equal(t, 21003*time.Second, statsB.GetSpillTime())
	assert.Equal(t, int64(210001), statsB.GetWrite())
	assert.Equal(t, 210011*time.Second, statsB.GetWriteTime())
}
```

## File: `tx_test.go`
```go
package bbolt_test

import (
	"bytes"
	"errors"
	"fmt"
	"log"
	"os"
	"runtime"
	"testing"
	"time"

	"github.com/stretchr/testify/assert"
	"github.com/stretchr/testify/require"

	bolt "go.etcd.io/bbolt"
	berrors "go.etcd.io/bbolt/errors"
	"go.etcd.io/bbolt/internal/btesting"
)

// TestTx_Check_ReadOnly tests consistency checking on a ReadOnly database.
func TestTx_Check_ReadOnly(t *testing.T) {
	db := btesting.MustCreateDB(t)
	if err := db.Update(func(tx *bolt.Tx) error {
		b, err := tx.CreateBucket([]byte("widgets"))
		if err != nil {
			t.Fatal(err)
		}
		if err := b.Put([]byte("foo"), []byte("bar")); err != nil {
			t.Fatal(err)
		}
		return nil
	}); err != nil {
		t.Fatal(err)
	}
	if err := db.Close(); err != nil {
		t.Fatal(err)
	}

	readOnlyDB, err := bolt.Open(db.Path(), 0600, &bolt.Options{ReadOnly: true})
	if err != nil {
		t.Fatal(err)
	}
	defer readOnlyDB.Close()

	tx, err := readOnlyDB.Begin(false)
	if err != nil {
		t.Fatal(err)
	}
	// ReadOnly DB will load freelist on Check call.
	numChecks := 2
	errc := make(chan error, numChecks)
	check := func() {
		errc <- <-tx.Check()
	}
	// Ensure the freelist is not reloaded and does not race.
	for i := 0; i < numChecks; i++ {
		go check()
	}
	for i := 0; i < numChecks; i++ {
		if err := <-errc; err != nil {
			t.Fatal(err)
		}
	}
	// Close the view transaction
	err = tx.Rollback()
	if err != nil {
		t.Fatal(err)
	}
}

// Ensure that committing a closed transaction returns an error.
func TestTx_Commit_ErrTxClosed(t *testing.T) {
	db := btesting.MustCreateDB(t)
	tx, err := db.Begin(true)
	if err != nil {
		t.Fatal(err)
	}

	if _, err := tx.CreateBucket([]byte("foo")); err != nil {
		t.Fatal(err)
	}

	if err := tx.Commit(); err != nil {
		t.Fatal(err)
	}

	if err := tx.Commit(); err != berrors.ErrTxClosed {
		t.Fatalf("unexpected error: %s", err)
	}
}

// Ensure that rolling back a closed transaction returns an error.
func TestTx_Rollback_ErrTxClosed(t *testing.T) {
	db := btesting.MustCreateDB(t)

	tx, err := db.Begin(true)
	if err != nil {
		t.Fatal(err)
	}

	if err := tx.Rollback(); err != nil {
		t.Fatal(err)
	}
	if err := tx.Rollback(); err != berrors.ErrTxClosed {
		t.Fatalf("unexpected error: %s", err)
	}
}

// Ensure that committing a read-only transaction returns an error.
func TestTx_Commit_ErrTxNotWritable(t *testing.T) {
	db := btesting.MustCreateDB(t)
	tx, err := db.Begin(false)
	if err != nil {
		t.Fatal(err)
	}
	if err := tx.Commit(); err != berrors.ErrTxNotWritable {
		t.Fatal(err)
	}
	// Close the view transaction
	err = tx.Rollback()
	if err != nil {
		t.Fatal(err)
	}
}

// Ensure that a transaction can retrieve a cursor on the root bucket.
func TestTx_Cursor(t *testing.T) {
	db := btesting.MustCreateDB(t)
	if err := db.Update(func(tx *bolt.Tx) error {
		if _, err := tx.CreateBucket([]byte("widgets")); err != nil {
			t.Fatal(err)
		}

		if _, err := tx.CreateBucket([]byte("woojits")); err != nil {
			t.Fatal(err)
		}

		c := tx.Cursor()
		if k, v := c.First(); !bytes.Equal(k, []byte("widgets")) {
			t.Fatalf("unexpected key: %v", k)
		} else if v != nil {
			t.Fatalf("unexpected value: %v", v)
		}

		if k, v := c.Next(); !bytes.Equal(k, []byte("woojits")) {
			t.Fatalf("unexpected key: %v", k)
		} else if v != nil {
			t.Fatalf("unexpected value: %v", v)
		}

		if k, v := c.Next(); k != nil {
			t.Fatalf("unexpected key: %v", k)
		} else if v != nil {
			t.Fatalf("unexpected value: %v", k)
		}

		return nil
	}); err != nil {
		t.Fatal(err)
	}
}

// Ensure that creating a bucket with a read-only transaction returns an error.
func TestTx_CreateBucket_ErrTxNotWritable(t *testing.T) {
	db := btesting.MustCreateDB(t)
	if err := db.View(func(tx *bolt.Tx) error {
		_, err := tx.CreateBucket([]byte("foo"))
		if err != berrors.ErrTxNotWritable {
			t.Fatalf("unexpected error: %s", err)
		}
		return nil
	}); err != nil {
		t.Fatal(err)
	}
}

// Ensure that creating a bucket on a closed transaction returns an error.
func TestTx_CreateBucket_ErrTxClosed(t *testing.T) {
	db := btesting.MustCreateDB(t)
	tx, err := db.Begin(true)
	if err != nil {
		t.Fatal(err)
	}
	if err := tx.Commit(); err != nil {
		t.Fatal(err)
	}

	if _, err := tx.CreateBucket([]byte("foo")); err != berrors.ErrTxClosed {
		t.Fatalf("unexpected error: %s", err)
	}
}

// Ensure that a Tx can retrieve a bucket.
func TestTx_Bucket(t *testing.T) {
	db := btesting.MustCreateDB(t)
	if err := db.Update(func(tx *bolt.Tx) error {
		if _, err := tx.CreateBucket([]byte("widgets")); err != nil {
			t.Fatal(err)
		}
		if tx.Bucket([]byte("widgets")) == nil {
			t.Fatal("expected bucket")
		}
		return nil
	}); err != nil {
		t.Fatal(err)
	}
}

// Ensure that a Tx retrieving a non-existent key returns nil.
func TestTx_Get_NotFound(t *testing.T) {
	db := btesting.MustCreateDB(t)
	if err := db.Update(func(tx *bolt.Tx) error {
		b, err := tx.CreateBucket([]byte("widgets"))
		if err != nil {
			t.Fatal(err)
		}

		if err := b.Put([]byte("foo"), []byte("bar")); err != nil {
			t.Fatal(err)
		}
		if b.Get([]byte("no_such_key")) != nil {
			t.Fatal("expected nil value")
		}
		return nil
	}); err != nil {
		t.Fatal(err)
	}
}

// Ensure that a bucket can be created and retrieved.
func TestTx_CreateBucket(t *testing.T) {
	db := btesting.MustCreateDB(t)

	// Create a bucket.
	if err := db.Update(func(tx *bolt.Tx) error {
		b, err := tx.CreateBucket([]byte("widgets"))
		if err != nil {
			t.Fatal(err)
		} else if b == nil {
			t.Fatal("expected bucket")
		}
		return nil
	}); err != nil {
		t.Fatal(err)
	}

	// Read the bucket through a separate transaction.
	if err := db.View(func(tx *bolt.Tx) error {
		if tx.Bucket([]byte("widgets")) == nil {
			t.Fatal("expected bucket")
		}
		return nil
	}); err != nil {
		t.Fatal(err)
	}
}

// Ensure that a bucket can be created if it doesn't already exist.
func TestTx_CreateBucketIfNotExists(t *testing.T) {
	db := btesting.MustCreateDB(t)
	if err := db.Update(func(tx *bolt.Tx) error {
		// Create bucket.
		if b, err := tx.CreateBucketIfNotExists([]byte("widgets")); err != nil {
			t.Fatal(err)
		} else if b == nil {
			t.Fatal("expected bucket")
		}

		// Create bucket again.
		if b, err := tx.CreateBucketIfNotExists([]byte("widgets")); err != nil {
			t.Fatal(err)
		} else if b == nil {
			t.Fatal("expected bucket")
		}

		return nil
	}); err != nil {
		t.Fatal(err)
	}

	// Read the bucket through a separate transaction.
	if err := db.View(func(tx *bolt.Tx) error {
		if tx.Bucket([]byte("widgets")) == nil {
			t.Fatal("expected bucket")
		}
		return nil
	}); err != nil {
		t.Fatal(err)
	}
}

// Ensure transaction returns an error if creating an unnamed bucket.
func TestTx_CreateBucketIfNotExists_ErrBucketNameRequired(t *testing.T) {
	db := btesting.MustCreateDB(t)
	if err := db.Update(func(tx *bolt.Tx) error {
		if _, err := tx.CreateBucketIfNotExists([]byte{}); err != berrors.ErrBucketNameRequired {
			t.Fatalf("unexpected error: %s", err)
		}

		if _, err := tx.CreateBucketIfNotExists(nil); err != berrors.ErrBucketNameRequired {
			t.Fatalf("unexpected error: %s", err)
		}

		return nil
	}); err != nil {
		t.Fatal(err)
	}
}

// Ensure that a bucket cannot be created twice.
func TestTx_CreateBucket_ErrBucketExists(t *testing.T) {
	db := btesting.MustCreateDB(t)

	// Create a bucket.
	if err := db.Update(func(tx *bolt.Tx) error {
		if _, err := tx.CreateBucket([]byte("widgets")); err != nil {
			t.Fatal(err)
		}
		return nil
	}); err != nil {
		t.Fatal(err)
	}

	// Create the same bucket again.
	if err := db.Update(func(tx *bolt.Tx) error {
		if _, err := tx.CreateBucket([]byte("widgets")); err != berrors.ErrBucketExists {
			t.Fatalf("unexpected error: %s", err)
		}
		return nil
	}); err != nil {
		t.Fatal(err)
	}
}

// Ensure that a bucket is created with a non-blank name.
func TestTx_CreateBucket_ErrBucketNameRequired(t *testing.T) {
	db := btesting.MustCreateDB(t)
	if err := db.Update(func(tx *bolt.Tx) error {
		if _, err := tx.CreateBucket(nil); err != berrors.ErrBucketNameRequired {
			t.Fatalf("unexpected error: %s", err)
		}
		return nil
	}); err != nil {
		t.Fatal(err)
	}
}

// Ensure that a bucket can be deleted.
func TestTx_DeleteBucket(t *testing.T) {
	db := btesting.MustCreateDB(t)

	// Create a bucket and add a value.
	if err := db.Update(func(tx *bolt.Tx) error {
		b, err := tx.CreateBucket([]byte("widgets"))
		if err != nil {
			t.Fatal(err)
		}
		if err := b.Put([]byte("foo"), []byte("bar")); err != nil {
			t.Fatal(err)
		}
		return nil
	}); err != nil {
		t.Fatal(err)
	}

	// Delete the bucket and make sure we can't get the value.
	if err := db.Update(func(tx *bolt.Tx) error {
		if err := tx.DeleteBucket([]byte("widgets")); err != nil {
			t.Fatal(err)
		}
		if tx.Bucket([]byte("widgets")) != nil {
			t.Fatal("unexpected bucket")
		}
		return nil
	}); err != nil {
		t.Fatal(err)
	}

	if err := db.Update(func(tx *bolt.Tx) error {
		// Create the bucket again and make sure there's not a phantom value.
		b, err := tx.CreateBucket([]byte("widgets"))
		if err != nil {
			t.Fatal(err)
		}
		if v := b.Get([]byte("foo")); v != nil {
			t.Fatalf("unexpected phantom value: %v", v)
		}
		return nil
	}); err != nil {
		t.Fatal(err)
	}
}

// Ensure that deleting a bucket on a closed transaction returns an error.
func TestTx_DeleteBucket_ErrTxClosed(t *testing.T) {
	db := btesting.MustCreateDB(t)
	tx, err := db.Begin(true)
	if err != nil {
		t.Fatal(err)
	}
	if err := tx.Commit(); err != nil {
		t.Fatal(err)
	}
	if err := tx.DeleteBucket([]byte("foo")); err != berrors.ErrTxClosed {
		t.Fatalf("unexpected error: %s", err)
	}
}

// Ensure that deleting a bucket with a read-only transaction returns an error.
func TestTx_DeleteBucket_ReadOnly(t *testing.T) {
	db := btesting.MustCreateDB(t)
	if err := db.View(func(tx *bolt.Tx) error {
		if err := tx.DeleteBucket([]byte("foo")); err != berrors.ErrTxNotWritable {
			t.Fatalf("unexpected error: %s", err)
		}
		return nil
	}); err != nil {
		t.Fatal(err)
	}
}

// Ensure that nothing happens when deleting a bucket that doesn't exist.
func TestTx_DeleteBucket_NotFound(t *testing.T) {
	db := btesting.MustCreateDB(t)
	if err := db.Update(func(tx *bolt.Tx) error {
		if err := tx.DeleteBucket([]byte("widgets")); err != berrors.ErrBucketNotFound {
			t.Fatalf("unexpected error: %s", err)
		}
		return nil
	}); err != nil {
		t.Fatal(err)
	}
}

// Ensure that no error is returned when a tx.ForEach function does not return
// an error.
func TestTx_ForEach_NoError(t *testing.T) {
	db := btesting.MustCreateDB(t)
	if err := db.Update(func(tx *bolt.Tx) error {
		b, err := tx.CreateBucket([]byte("widgets"))
		if err != nil {
			t.Fatal(err)
		}
		if err := b.Put([]byte("foo"), []byte("bar")); err != nil {
			t.Fatal(err)
		}

		if err := tx.ForEach(func(name []byte, b *bolt.Bucket) error {
			return nil
		}); err != nil {
			t.Fatal(err)
		}
		return nil
	}); err != nil {
		t.Fatal(err)
	}
}

// Ensure that an error is returned when a tx.ForEach function returns an error.
func TestTx_ForEach_WithError(t *testing.T) {
	db := btesting.MustCreateDB(t)
	if err := db.Update(func(tx *bolt.Tx) error {
		b, err := tx.CreateBucket([]byte("widgets"))
		if err != nil {
			t.Fatal(err)
		}
		if err := b.Put([]byte("foo"), []byte("bar")); err != nil {
			t.Fatal(err)
		}

		marker := errors.New("marker")
		if err := tx.ForEach(func(name []byte, b *bolt.Bucket) error {
			return marker
		}); err != marker {
			t.Fatalf("unexpected error: %s", err)
		}
		return nil
	}); err != nil {
		t.Fatal(err)
	}
}

// Ensure that Tx commit handlers are called after a transaction successfully commits.
func TestTx_OnCommit(t *testing.T) {
	db := btesting.MustCreateDB(t)

	var x int
	if err := db.Update(func(tx *bolt.Tx) error {
		tx.OnCommit(func() { x += 1 })
		tx.OnCommit(func() { x += 2 })
		if _, err := tx.CreateBucket([]byte("widgets")); err != nil {
			t.Fatal(err)
		}
		return nil
	}); err != nil {
		t.Fatal(err)
	} else if x != 3 {
		t.Fatalf("unexpected x: %d", x)
	}
}

// Ensure that Tx commit handlers are NOT called after a transaction rolls back.
func TestTx_OnCommit_Rollback(t *testing.T) {
	db := btesting.MustCreateDB(t)

	var x int
	if err := db.Update(func(tx *bolt.Tx) error {
		tx.OnCommit(func() { x += 1 })
		tx.OnCommit(func() { x += 2 })
		if _, err := tx.CreateBucket([]byte("widgets")); err != nil {
			t.Fatal(err)
		}
		return errors.New("rollback this commit")
	}); err == nil || err.Error() != "rollback this commit" {
		t.Fatalf("unexpected error: %s", err)
	} else if x != 0 {
		t.Fatalf("unexpected x: %d", x)
	}
}

// Ensure that the database can be copied to a file path.
func TestTx_CopyFile(t *testing.T) {
	db := btesting.MustCreateDB(t)

	path := tempfile()
	if err := db.Update(func(tx *bolt.Tx) error {
		b, err := tx.CreateBucket([]byte("widgets"))
		if err != nil {
			t.Fatal(err)
		}
		if err := b.Put([]byte("foo"), []byte("bar")); err != nil {
			t.Fatal(err)
		}
		if err := b.Put([]byte("baz"), []byte("bat")); err != nil {
			t.Fatal(err)
		}
		return nil
	}); err != nil {
		t.Fatal(err)
	}

	if err := db.View(func(tx *bolt.Tx) error {
		return tx.CopyFile(path, 0600)
	}); err != nil {
		t.Fatal(err)
	}

	db2, err := bolt.Open(path, 0600, nil)
	if err != nil {
		t.Fatal(err)
	}

	if err := db2.View(func(tx *bolt.Tx) error {
		if v := tx.Bucket([]byte("widgets")).Get([]byte("foo")); !bytes.Equal(v, []byte("bar")) {
			t.Fatalf("unexpected value: %v", v)
		}
		if v := tx.Bucket([]byte("widgets")).Get([]byte("baz")); !bytes.Equal(v, []byte("bat")) {
			t.Fatalf("unexpected value: %v", v)
		}
		return nil
	}); err != nil {
		t.Fatal(err)
	}

	if err := db2.Close(); err != nil {
		t.Fatal(err)
	}
}

type failWriterError struct{}

func (failWriterError) Error() string {
	return "error injected for tests"
}

type failWriter struct {
	// fail after this many bytes
	After int
}

func (f *failWriter) Write(p []byte) (n int, err error) {
	n = len(p)
	if n > f.After {
		n = f.After
		err = failWriterError{}
	}
	f.After -= n
	return n, err
}

// Ensure that Copy handles write errors right.
func TestTx_CopyFile_Error_Meta(t *testing.T) {
	db := btesting.MustCreateDB(t)
	if err := db.Update(func(tx *bolt.Tx) error {
		b, err := tx.CreateBucket([]byte("widgets"))
		if err != nil {
			t.Fatal(err)
		}
		if err := b.Put([]byte("foo"), []byte("bar")); err != nil {
			t.Fatal(err)
		}
		if err := b.Put([]byte("baz"), []byte("bat")); err != nil {
			t.Fatal(err)
		}
		return nil
	}); err != nil {
		t.Fatal(err)
	}

	if err := db.View(func(tx *bolt.Tx) error {
		return tx.Copy(&failWriter{})
	}); err == nil || err.Error() != "meta 0 copy: error injected for tests" {
		t.Fatalf("unexpected error: %v", err)
	}
}

// Ensure that Copy handles write errors right.
func TestTx_CopyFile_Error_Normal(t *testing.T) {
	db := btesting.MustCreateDB(t)
	if err := db.Update(func(tx *bolt.Tx) error {
		b, err := tx.CreateBucket([]byte("widgets"))
		if err != nil {
			t.Fatal(err)
		}
		if err := b.Put([]byte("foo"), []byte("bar")); err != nil {
			t.Fatal(err)
		}
		if err := b.Put([]byte("baz"), []byte("bat")); err != nil {
			t.Fatal(err)
		}
		return nil
	}); err != nil {
		t.Fatal(err)
	}

	if err := db.View(func(tx *bolt.Tx) error {
		return tx.Copy(&failWriter{3 * db.Info().PageSize})
	}); err == nil || err.Error() != "error injected for tests" {
		t.Fatalf("unexpected error: %v", err)
	}
}

// TestTx_Rollback ensures there is no error when tx rollback whether we sync freelist or not.
func TestTx_Rollback(t *testing.T) {
	for _, isSyncFreelist := range []bool{false, true} {
		// Open the database.
		db, err := bolt.Open(tempfile(), 0600, nil)
		if err != nil {
			log.Fatal(err)
		}
		defer os.Remove(db.Path())
		db.NoFreelistSync = isSyncFreelist

		tx, err := db.Begin(true)
		if err != nil {
			t.Fatalf("Error starting tx: %v", err)
		}
		bucket := []byte("mybucket")
		if _, err := tx.CreateBucket(bucket); err != nil {
			t.Fatalf("Error creating bucket: %v", err)
		}
		if err := tx.Commit(); err != nil {
			t.Fatalf("Error on commit: %v", err)
		}

		tx, err = db.Begin(true)
		if err != nil {
			t.Fatalf("Error starting tx: %v", err)
		}
		b := tx.Bucket(bucket)
		if err := b.Put([]byte("k"), []byte("v")); err != nil {
			t.Fatalf("Error on put: %v", err)
		}
		// Imagine there is an error and tx needs to be rolled-back
		if err := tx.Rollback(); err != nil {
			t.Fatalf("Error on rollback: %v", err)
		}

		tx, err = db.Begin(false)
		if err != nil {
			t.Fatalf("Error starting tx: %v", err)
		}
		b = tx.Bucket(bucket)
		if v := b.Get([]byte("k")); v != nil {
			t.Fatalf("Value for k should not have been stored")
		}
		if err := tx.Rollback(); err != nil {
			t.Fatalf("Error on rollback: %v", err)
		}

	}
}

// TestTx_releaseRange ensures db.freePages handles page releases
// correctly when there are transaction that are no longer reachable
// via any read/write transactions and are "between" ongoing read
// transactions, which requires they must be freed by
// freelist.releaseRange.
func TestTx_releaseRange(t *testing.T) {
	// Set initial mmap size well beyond the limit we will hit in this
	// test, since we are testing with long running read transactions
	// and will deadlock if db.grow is triggered.
	db := btesting.MustCreateDBWithOption(t, &bolt.Options{InitialMmapSize: os.Getpagesize() * 100})

	bucket := "bucket"

	put := func(key, value string) {
		if err := db.Update(func(tx *bolt.Tx) error {
			b, err := tx.CreateBucketIfNotExists([]byte(bucket))
			if err != nil {
				t.Fatal(err)
			}
			return b.Put([]byte(key), []byte(value))
		}); err != nil {
			t.Fatal(err)
		}
	}

	del := func(key string) {
		if err := db.Update(func(tx *bolt.Tx) error {
			b, err := tx.CreateBucketIfNotExists([]byte(bucket))
			if err != nil {
				t.Fatal(err)
			}
			return b.Delete([]byte(key))
		}); err != nil {
			t.Fatal(err)
		}
	}

	getWithTxn := func(txn *bolt.Tx, key string) []byte {
		return txn.Bucket([]byte(bucket)).Get([]byte(key))
	}

	openReadTxn := func() *bolt.Tx {
		readTx, err := db.Begin(false)
		if err != nil {
			t.Fatal(err)
		}
		return readTx
	}

	checkWithReadTxn := func(txn *bolt.Tx, key string, wantValue []byte) {
		value := getWithTxn(txn, key)
		if !bytes.Equal(value, wantValue) {
			t.Errorf("Wanted value to be %s for key %s, but got %s", wantValue, key, string(value))
		}
	}

	rollback := func(txn *bolt.Tx) {
		if err := txn.Rollback(); err != nil {
			t.Fatal(err)
		}
	}

	put("k1", "v1")
	rtx1 := openReadTxn()
	put("k2", "v2")
	hold1 := openReadTxn()
	put("k3", "v3")
	hold2 := openReadTxn()
	del("k3")
	rtx2 := openReadTxn()
	del("k1")
	hold3 := openReadTxn()
	del("k2")
	hold4 := openReadTxn()
	put("k4", "v4")
	hold5 := openReadTxn()

	// Close the read transactions we established to hold a portion of the pages in pending state.
	rollback(hold1)
	rollback(hold2)
	rollback(hold3)
	rollback(hold4)
	rollback(hold5)

	// Execute a write transaction to trigger a releaseRange operation in the db
	// that will free multiple ranges between the remaining open read transactions, now that the
	// holds have been rolled back.
	put("k4", "v4")

	// Check that all long running reads still read correct values.
	checkWithReadTxn(rtx1, "k1", []byte("v1"))
	checkWithReadTxn(rtx2, "k2", []byte("v2"))
	rollback(rtx1)
	rollback(rtx2)

	// Check that the final state is correct.
	rtx7 := openReadTxn()
	checkWithReadTxn(rtx7, "k1", nil)
	checkWithReadTxn(rtx7, "k2", nil)
	checkWithReadTxn(rtx7, "k3", nil)
	checkWithReadTxn(rtx7, "k4", []byte("v4"))
	rollback(rtx7)
}

func ExampleTx_Rollback() {
	// Open the database.
	db, err := bolt.Open(tempfile(), 0600, nil)
	if err != nil {
		log.Fatal(err)
	}
	defer os.Remove(db.Path())

	// Create a bucket.
	if err := db.Update(func(tx *bolt.Tx) error {
		_, err := tx.CreateBucket([]byte("widgets"))
		return err
	}); err != nil {
		log.Fatal(err)
	}

	// Set a value for a key.
	if err := db.Update(func(tx *bolt.Tx) error {
		return tx.Bucket([]byte("widgets")).Put([]byte("foo"), []byte("bar"))
	}); err != nil {
		log.Fatal(err)
	}

	// Update the key but rollback the transaction so it never saves.
	tx, err := db.Begin(true)
	if err != nil {
		log.Fatal(err)
	}
	b := tx.Bucket([]byte("widgets"))
	if err := b.Put([]byte("foo"), []byte("baz")); err != nil {
		log.Fatal(err)
	}
	if err := tx.Rollback(); err != nil {
		log.Fatal(err)
	}

	// Ensure that our original value is still set.
	if err := db.View(func(tx *bolt.Tx) error {
		value := tx.Bucket([]byte("widgets")).Get([]byte("foo"))
		fmt.Printf("The value for 'foo' is still: %s\n", value)
		return nil
	}); err != nil {
		log.Fatal(err)
	}

	// Close database to release file lock.
	if err := db.Close(); err != nil {
		log.Fatal(err)
	}

	// Output:
	// The value for 'foo' is still: bar
}

func ExampleTx_CopyFile() {
	// Open the database.
	db, err := bolt.Open(tempfile(), 0600, nil)
	if err != nil {
		log.Fatal(err)
	}
	defer os.Remove(db.Path())

	// Create a bucket and a key.
	if err := db.Update(func(tx *bolt.Tx) error {
		b, err := tx.CreateBucket([]byte("widgets"))
		if err != nil {
			return err
		}
		if err := b.Put([]byte("foo"), []byte("bar")); err != nil {
			return err
		}
		return nil
	}); err != nil {
		log.Fatal(err)
	}

	// Copy the database to another file.
	toFile := tempfile()
	if err := db.View(func(tx *bolt.Tx) error {
		return tx.CopyFile(toFile, 0666)
	}); err != nil {
		log.Fatal(err)
	}
	defer os.Remove(toFile)

	// Open the cloned database.
	db2, err := bolt.Open(toFile, 0600, nil)
	if err != nil {
		log.Fatal(err)
	}

	// Ensure that the key exists in the copy.
	if err := db2.View(func(tx *bolt.Tx) error {
		value := tx.Bucket([]byte("widgets")).Get([]byte("foo"))
		fmt.Printf("The value for 'foo' in the clone is: %s\n", value)
		return nil
	}); err != nil {
		log.Fatal(err)
	}

	// Close database to release file lock.
	if err := db.Close(); err != nil {
		log.Fatal(err)
	}

	if err := db2.Close(); err != nil {
		log.Fatal(err)
	}

	// Output:
	// The value for 'foo' in the clone is: bar
}

func TestTxStats_GetAndIncAtomically(t *testing.T) {
	var stats bolt.TxStats

	stats.IncPageCount(1)
	assert.Equal(t, int64(1), stats.GetPageCount())

	stats.IncPageAlloc(2)
	assert.Equal(t, int64(2), stats.GetPageAlloc())

	stats.IncCursorCount(3)
	assert.Equal(t, int64(3), stats.GetCursorCount())

	stats.IncNodeCount(100)
	assert.Equal(t, int64(100), stats.GetNodeCount())

	stats.IncNodeDeref(101)
	assert.Equal(t, int64(101), stats.GetNodeDeref())

	stats.IncRebalance(1000)
	assert.Equal(t, int64(1000), stats.GetRebalance())

	stats.IncRebalanceTime(1001 * time.Second)
	assert.Equal(t, 1001*time.Second, stats.GetRebalanceTime())

	stats.IncSplit(10000)
	assert.Equal(t, int64(10000), stats.GetSplit())

	stats.IncSpill(10001)
	assert.Equal(t, int64(10001), stats.GetSpill())

	stats.IncSpillTime(10001 * time.Second)
	assert.Equal(t, 10001*time.Second, stats.GetSpillTime())

	stats.IncWrite(100000)
	assert.Equal(t, int64(100000), stats.GetWrite())

	stats.IncWriteTime(100001 * time.Second)
	assert.Equal(t, 100001*time.Second, stats.GetWriteTime())

	assert.Equal(t,
		bolt.TxStats{
			PageCount:     1,
			PageAlloc:     2,
			CursorCount:   3,
			NodeCount:     100,
			NodeDeref:     101,
			Rebalance:     1000,
			RebalanceTime: 1001 * time.Second,
			Split:         10000,
			Spill:         10001,
			SpillTime:     10001 * time.Second,
			Write:         100000,
			WriteTime:     100001 * time.Second,
		},
		stats,
	)
}

func TestTxStats_Sub(t *testing.T) {
	statsA := bolt.TxStats{
		PageCount:     1,
		PageAlloc:     2,
		CursorCount:   3,
		NodeCount:     100,
		NodeDeref:     101,
		Rebalance:     1000,
		RebalanceTime: 1001 * time.Second,
		Split:         10000,
		Spill:         10001,
		SpillTime:     10001 * time.Second,
		Write:         100000,
		WriteTime:     100001 * time.Second,
	}

	statsB := bolt.TxStats{
		PageCount:     2,
		PageAlloc:     3,
		CursorCount:   4,
		NodeCount:     101,
		NodeDeref:     102,
		Rebalance:     1001,
		RebalanceTime: 1002 * time.Second,
		Split:         11001,
		Spill:         11002,
		SpillTime:     11002 * time.Second,
		Write:         110001,
		WriteTime:     110010 * time.Second,
	}

	diff := statsB.Sub(&statsA)
	assert.Equal(t, int64(1), diff.GetPageCount())
	assert.Equal(t, int64(1), diff.GetPageAlloc())
	assert.Equal(t, int64(1), diff.GetCursorCount())
	assert.Equal(t, int64(1), diff.GetNodeCount())
	assert.Equal(t, int64(1), diff.GetNodeDeref())
	assert.Equal(t, int64(1), diff.GetRebalance())
	assert.Equal(t, time.Second, diff.GetRebalanceTime())
	assert.Equal(t, int64(1001), diff.GetSplit())
	assert.Equal(t, int64(1001), diff.GetSpill())
	assert.Equal(t, 1001*time.Second, diff.GetSpillTime())
	assert.Equal(t, int64(10001), diff.GetWrite())
	assert.Equal(t, 10009*time.Second, diff.GetWriteTime())
}

// TestTx_TruncateBeforeWrite ensures the file is truncated ahead whether we sync freelist or not.
func TestTx_TruncateBeforeWrite(t *testing.T) {
	if runtime.GOOS == "windows" {
		return
	}
	for _, isSyncFreelist := range []bool{false, true} {
		t.Run(fmt.Sprintf("isSyncFreelist:%v", isSyncFreelist), func(t *testing.T) {
			// Open the database.
			db := btesting.MustCreateDBWithOption(t, &bolt.Options{
				NoFreelistSync: isSyncFreelist,
			})

			bigvalue := make([]byte, db.AllocSize/100)
			count := 0
			for {
				count++
				tx, err := db.Begin(true)
				require.NoError(t, err)
				b, err := tx.CreateBucketIfNotExists([]byte("bucket"))
				require.NoError(t, err)
				err = b.Put([]byte{byte(count)}, bigvalue)
				require.NoError(t, err)
				err = tx.Commit()
				require.NoError(t, err)

				size := fileSize(db.Path())

				if size > int64(db.AllocSize) && size < int64(db.AllocSize)*2 {
					// db.grow expands the file aggresively, that double the size while smaller than db.AllocSize,
					// or increase with a step of db.AllocSize if larger, by which we can test if db.grow has run.
					t.Fatalf("db.grow doesn't run when file size changes. file size: %d", size)
				}
				if size > int64(db.AllocSize) {
					break
				}
			}
			db.MustClose()
			db.MustDeleteFile()
		})
	}
}
```

## File: `unix_test.go`
```go
//go:build !windows

package bbolt_test

import (
	"fmt"
	"testing"

	"golang.org/x/sys/unix"

	bolt "go.etcd.io/bbolt"
	"go.etcd.io/bbolt/internal/btesting"
)

func TestMlock_DbOpen(t *testing.T) {
	// 32KB
	skipOnMemlockLimitBelow(t, 32*1024)

	btesting.MustCreateDBWithOption(t, &bolt.Options{Mlock: true})
}

// Test change between "empty" (16KB) and "non-empty" db
func TestMlock_DbCanGrow_Small(t *testing.T) {
	// 32KB
	skipOnMemlockLimitBelow(t, 32*1024)

	db := btesting.MustCreateDBWithOption(t, &bolt.Options{Mlock: true})

	if err := db.Update(func(tx *bolt.Tx) error {
		b, err := tx.CreateBucketIfNotExists([]byte("bucket"))
		if err != nil {
			t.Fatal(err)
		}

		key := []byte("key")
		value := []byte("value")
		if err := b.Put(key, value); err != nil {
			t.Fatal(err)
		}

		return nil
	}); err != nil {
		t.Fatal(err)
	}

}

// Test crossing of 16MB (AllocSize) of db size
func TestMlock_DbCanGrow_Big(t *testing.T) {
	if testing.Short() {
		t.Skip("skipping test in short mode")
	}

	// 32MB
	skipOnMemlockLimitBelow(t, 32*1024*1024)

	chunksBefore := 64
	chunksAfter := 64

	db := btesting.MustCreateDBWithOption(t, &bolt.Options{Mlock: true})

	for chunk := 0; chunk < chunksBefore; chunk++ {
		insertChunk(t, db, chunk)
	}
	dbSize := fileSize(db.Path())

	for chunk := 0; chunk < chunksAfter; chunk++ {
		insertChunk(t, db, chunksBefore+chunk)
	}
	newDbSize := fileSize(db.Path())

	if newDbSize <= dbSize {
		t.Errorf("db didn't grow: %v <= %v", newDbSize, dbSize)
	}
}

func insertChunk(t *testing.T, db *btesting.DB, chunkId int) {
	chunkSize := 1024

	if err := db.Update(func(tx *bolt.Tx) error {
		b, err := tx.CreateBucketIfNotExists([]byte("bucket"))
		if err != nil {
			t.Fatal(err)
		}

		for i := 0; i < chunkSize; i++ {
			key := []byte(fmt.Sprintf("key-%d-%d", chunkId, i))
			value := []byte("value")
			if err := b.Put(key, value); err != nil {
				t.Fatal(err)
			}
		}

		return nil
	}); err != nil {
		t.Fatal(err)
	}
}

// Main reason for this check is travis limiting mlockable memory to 64KB
// https://github.com/travis-ci/travis-ci/issues/2462
func skipOnMemlockLimitBelow(t *testing.T, memlockLimitRequest uint64) {
	var info unix.Rlimit
	if err := unix.Getrlimit(unix.RLIMIT_MEMLOCK, &info); err != nil {
		t.Fatal(err)
	}

	if info.Cur < memlockLimitRequest {
		t.Skipf(
			"skipping as RLIMIT_MEMLOCK is insufficient: %v < %v",
			info.Cur,
			memlockLimitRequest,
		)
	}
}
```

## File: `utils_test.go`
```go
package bbolt_test

import (
	bolt "go.etcd.io/bbolt"
	"go.etcd.io/bbolt/internal/common"
)

// `dumpBucket` dumps all the data, including both key/value data
// and child buckets, from the source bucket into the target db file.
func dumpBucket(srcBucketName []byte, srcBucket *bolt.Bucket, dstFilename string) error {
	common.Assert(len(srcBucketName) != 0, "source bucket name can't be empty")
	common.Assert(srcBucket != nil, "the source bucket can't be nil")
	common.Assert(len(dstFilename) != 0, "the target file path can't be empty")

	dstDB, err := bolt.Open(dstFilename, 0600, nil)
	if err != nil {
		return err
	}
	defer dstDB.Close()

	return dstDB.Update(func(tx *bolt.Tx) error {
		dstBucket, err := tx.CreateBucket(srcBucketName)
		if err != nil {
			return err
		}
		return cloneBucket(srcBucket, dstBucket)
	})
}

func cloneBucket(src *bolt.Bucket, dst *bolt.Bucket) error {
	return src.ForEach(func(k, v []byte) error {
		if v == nil {
			srcChild := src.Bucket(k)
			dstChild, err := dst.CreateBucket(k)
			if err != nil {
				return err
			}
			if err = dstChild.SetSequence(srcChild.Sequence()); err != nil {
				return err
			}

			return cloneBucket(srcChild, dstChild)
		}

		return dst.Put(k, v)
	})
}
```

## File: `CHANGELOG/CHANGELOG-1.3.md`
```markdown
Note that we start to track changes starting from v1.3.7.

<hr>

## v1.3.13(TBD)

### BoltDB
- Fix [`Bucket.Stats()` panic on branch pages with zero elements](https://github.com/etcd-io/bbolt/pull/1173)

<hr>

## v1.3.12(2025-08-19)

### BoltDB
- [Add protection on meta page when it's being written](https://github.com/etcd-io/bbolt/pull/1006)
- Fix [potential data corruption in `(*Tx)WriteTo` if underlying db file is overwritten](https://github.com/etcd-io/bbolt/pull/1059)

<hr>

## v1.3.11(2024-08-21)

### BoltDB
- Fix [the `freelist.allocs` isn't rollbacked when a tx is rollbacked](https://github.com/etcd-io/bbolt/pull/823).

### CMD
- Add [`-gobench-output` option for bench command to adapt to benchstat](https://github.com/etcd-io/bbolt/pull/802).

### Other
- [Bump go version to 1.22.x](https://github.com/etcd-io/bbolt/pull/822).
- This patch also added `dmflakey` package, which can be reused by other projects. See https://github.com/etcd-io/bbolt/pull/812.

<hr>

## v1.3.10(2024-05-06)

### BoltDB
- [Remove deprecated `UnsafeSlice` and use `unsafe.Slice`](https://github.com/etcd-io/bbolt/pull/717)
- [Stabilize the behaviour of Prev when the cursor already points to the first element](https://github.com/etcd-io/bbolt/pull/744)

### Other
- [Bump go version to 1.21.9](https://github.com/etcd-io/bbolt/pull/713)

<hr>

## v1.3.9(2024-02-24)

### BoltDB
- [Clone the key before operating data in bucket against the key](https://github.com/etcd-io/bbolt/pull/639)

### CMD
- [Fix `bbolt keys` and `bbolt get` to prevent them from panicking when no parameter provided](https://github.com/etcd-io/bbolt/pull/683)

<hr>

## v1.3.8(2023-10-26)

### BoltDB
- Fix [db.close() doesn't unlock the db file if db.munnmap() fails](https://github.com/etcd-io/bbolt/pull/439).
- [Avoid syscall.Syscall use on OpenBSD](https://github.com/etcd-io/bbolt/pull/406).
- Fix [rollback panicking after mlock failed or both meta pages corrupted](https://github.com/etcd-io/bbolt/pull/444).
- Fix [bbolt panicking due to 64bit unaligned on arm32](https://github.com/etcd-io/bbolt/pull/584).

### CMD
- [Update the usage of surgery command](https://github.com/etcd-io/bbolt/pull/411).

<hr>

## v1.3.7(2023-01-31)

### BoltDB
- Add [recursive checker to confirm database consistency](https://github.com/etcd-io/bbolt/pull/225).
- Add [support to get the page size from the second meta page if the first one is invalid](https://github.com/etcd-io/bbolt/pull/294).
- Add [support for loong64 arch](https://github.com/etcd-io/bbolt/pull/303).
- Add [internal iterator to Bucket that goes over buckets](https://github.com/etcd-io/bbolt/pull/356).
- Add [validation on page read and write](https://github.com/etcd-io/bbolt/pull/358).
- Add [PreLoadFreelist option to support loading free pages in readonly mode](https://github.com/etcd-io/bbolt/pull/381).
- Add [(*Tx) CheckWithOption to support generating human-readable diagnostic messages](https://github.com/etcd-io/bbolt/pull/395).
- Fix [Use `golang.org/x/sys/windows` for `FileLockEx`/`UnlockFileEx`](https://github.com/etcd-io/bbolt/pull/283).
- Fix [readonly file mapping on windows](https://github.com/etcd-io/bbolt/pull/307).
- Fix [the "Last" method might return no data due to not skipping the empty pages](https://github.com/etcd-io/bbolt/pull/341).
- Fix [panic on db.meta when rollback](https://github.com/etcd-io/bbolt/pull/362).

### CMD
- Add [support for get keys in sub buckets in `bbolt get` command](https://github.com/etcd-io/bbolt/pull/295).
- Add [support for `--format` flag for `bbolt keys` command](https://github.com/etcd-io/bbolt/pull/306).
- Add [safeguards to bbolt CLI commands](https://github.com/etcd-io/bbolt/pull/354).
- Add [`bbolt page` supports --all and --value-format=redacted formats](https://github.com/etcd-io/bbolt/pull/359).
- Add [`bbolt surgery` commands](https://github.com/etcd-io/bbolt/issues/370).
- Fix [open db file readonly mode for commands which shouldn't update the db file](https://github.com/etcd-io/bbolt/pull/365), see also [pull/292](https://github.com/etcd-io/bbolt/pull/292).

### Other
- [Build bbolt CLI tool, test and format the source code using golang 1.17.13](https://github.com/etcd-io/bbolt/pull/297).
- [Bump golang.org/x/sys to v0.4.0](https://github.com/etcd-io/bbolt/pull/397).

### Summary
Release v1.3.7 contains following critical fixes:
- fix to problem that `Last` method might return incorrect value ([#341](https://github.com/etcd-io/bbolt/pull/341))
- fix of potential panic when performing transaction's rollback ([#362](https://github.com/etcd-io/bbolt/pull/362))

Other changes focused on defense-in-depth ([#358](https://github.com/etcd-io/bbolt/pull/358), [#294](https://github.com/etcd-io/bbolt/pull/294), [#225](https://github.com/etcd-io/bbolt/pull/225), [#395](https://github.com/etcd-io/bbolt/pull/395))

`bbolt` command line tool was expanded to:
- allow fixing simple corruptions by `bbolt surgery` ([#370](https://github.com/etcd-io/bbolt/pull/370))
- be flexible about output formatting ([#306](https://github.com/etcd-io/bbolt/pull/306), [#359](https://github.com/etcd-io/bbolt/pull/359))
- allow accessing data in subbuckets ([#295](https://github.com/etcd-io/bbolt/pull/295))
```

## File: `CHANGELOG/CHANGELOG-1.4.md`
```markdown

<hr>

## v1.4.4(TBD)

### BoltDB
- Fix [`Bucket.Stats()` panic on branch pages with zero elements](https://github.com/etcd-io/bbolt/pull/1172)

<hr>

## v1.4.3(2025-08-19)

### BoltDB
- Fix [potential data corruption in `(*Tx)WriteTo` if underlying db file is overwritten](https://github.com/etcd-io/bbolt/pull/1058)

<hr>

## v1.4.2(2025-06-27)

### BoltDB
- [Fix the compilation issue on aix, android and solaris due to wrong use of `maxMapSize`](https://github.com/etcd-io/bbolt/pull/990)
- [Add protection on meta page when it's being written](https://github.com/etcd-io/bbolt/pull/1005)

<hr>

## v1.4.1(2025-06-10)

### BoltDB
- [Correct the incorrect usage of debug method](https://github.com/etcd-io/bbolt/pull/905)
- [Add clarification on the option `InitialMmapSize`](https://github.com/etcd-io/bbolt/pull/943)
- [Fix the crash when writing huge values](https://github.com/etcd-io/bbolt/pull/978)

<hr>

## v1.4.0(2025-02-05)
There isn't any production code change since v1.4.0-beta.0. Only some dependencies
are bumped, also updated some typos in comment and readme, and removed the legacy
build tag `// +build` in https://github.com/etcd-io/bbolt/pull/879.

<hr>

## v1.4.0-beta.0(2024-11-04)

### BoltDB
- Reorganized the directory structure of freelist source code
  - [Move array related freelist source code into a separate file](https://github.com/etcd-io/bbolt/pull/777)
  - [Move method `freePages` into freelist.go](https://github.com/etcd-io/bbolt/pull/783)
  - [Add an interface for freelist](https://github.com/etcd-io/bbolt/pull/775)
- [Rollback alloc map when a transaction is rollbacked](https://github.com/etcd-io/bbolt/pull/819)
- [No handling freelist as a special case when freeing a page](https://github.com/etcd-io/bbolt/pull/788)
- [Ensure hashmap init method clears the data structures](https://github.com/etcd-io/bbolt/pull/794)
- [Panicking when a write transaction tries to free a page allocated by itself](https://github.com/etcd-io/bbolt/pull/792)

### CMD
- [Add `-gobench-output` flag for `bbolt bench` command](https://github.com/etcd-io/bbolt/pull/765)

### Other
- [Bump go version to 1.23.x](https://github.com/etcd-io/bbolt/pull/821)

<hr>

## v1.4.0-alpha.1(2024-05-06)

### BoltDB
- [Enhance check functionality to support checking starting from a pageId](https://github.com/etcd-io/bbolt/pull/659)
- [Optimize the logger performance for frequent called methods](https://github.com/etcd-io/bbolt/pull/741)
- [Stabilize the behaviour of Prev when the cursor already points to the first element](https://github.com/etcd-io/bbolt/pull/734)

### CMD
- [Fix `bbolt keys` and `bbolt get` to prevent them from panicking when no parameter provided](https://github.com/etcd-io/bbolt/pull/682)
- [Fix surgery freelist command in info logs](https://github.com/etcd-io/bbolt/pull/700)
- [Remove txid references in surgery meta command's comment and description](https://github.com/etcd-io/bbolt/pull/703)
- [Add rnd read capabilities to bbolt bench](https://github.com/etcd-io/bbolt/pull/711)
- [Use `cobra.ExactArgs` to simplify the argument number check](https://github.com/etcd-io/bbolt/pull/728)
- [Migrate `bbolt check` command to cobra style](https://github.com/etcd-io/bbolt/pull/723)
- [Simplify the naming of cobra commands](https://github.com/etcd-io/bbolt/pull/732)
- [Aggregate adding completed ops for read test of the `bbolt bench` command](https://github.com/etcd-io/bbolt/pull/721)
- [Add `--from-page` flag to `bbolt check` command](https://github.com/etcd-io/bbolt/pull/737)

### Document
- [Add document for a known issue on the writing a value with a length of 0](https://github.com/etcd-io/bbolt/pull/730)

### Test
- [Enhance robustness test to cover XFS](https://github.com/etcd-io/bbolt/pull/707)

### Other
- [Bump go toolchain version to 1.22.2](https://github.com/etcd-io/bbolt/pull/712)

<hr>

## v1.4.0-alpha.0(2024-01-12)

### BoltDB
- [Improve the performance of hashmapGetFreePageIDs](https://github.com/etcd-io/bbolt/pull/419)
- [Improve CreateBucketIfNotExists to avoid double searching the same key](https://github.com/etcd-io/bbolt/pull/532)
- [Support Android platform](https://github.com/etcd-io/bbolt/pull/571)
- [Record the count of free page to improve the performance of hashmapFreeCount](https://github.com/etcd-io/bbolt/pull/585)
- [Add logger to bbolt](https://github.com/etcd-io/bbolt/issues/509)
- [Support moving bucket inside the same db](https://github.com/etcd-io/bbolt/pull/635)
- [Support inspecting database structure](https://github.com/etcd-io/bbolt/pull/674)

### CMD
- [Add `surgery clear-page-elements` command](https://github.com/etcd-io/bbolt/pull/417)
- [Add `surgery abandon-freelist` command](https://github.com/etcd-io/bbolt/pull/443)
- [Add `bbolt version` command](https://github.com/etcd-io/bbolt/pull/552)
- [Add `bbolt inspect` command](https://github.com/etcd-io/bbolt/pull/674)
- [Add `--no-sync` option to `bbolt compact` command](https://github.com/etcd-io/bbolt/pull/290)
```

## File: `CHANGELOG/CHANGELOG-1.5.md`
```markdown
<hr>

## v1.5.0(TBD)

### BoltDB
- [Add support for data file size limit](https://github.com/etcd-io/bbolt/pull/929)
- [Remove the unused txs list](https://github.com/etcd-io/bbolt/pull/973)
- [Add option `NoStatistics` to make the statistics optional](https://github.com/etcd-io/bbolt/pull/977)
- [Move panic handling from goroutine to the parent function](https://github.com/etcd-io/bbolt/pull/1153)
- [Recover from panics in tx.check](https://github.com/etcd-io/bbolt/pull/1164)

<hr>
```

## File: `cmd/bbolt/OWNERS`
```
# See the OWNERS docs at https://go.k8s.io/owners

approvers:
  - ahrtr           # Benjamin Wang <benjamin.ahrtr@gmail.com> <benjamin.wang@broadcom.com>
  - elbehery        # Mustafa Elbehery <elbeherymustafa@gmail.com>
  - fuweid          # Wei Fu <fuweid89@gmail.com>
  - serathius       # Marek Siarkowicz <siarkowicz@google.com> <marek.siarkowicz@gmail.com>
  - ptabor          # Piotr Tabor <piotr.tabor@gmail.com>
  - spzala          # Sahdev Zala <spzala@us.ibm.com>
  - tjungblu        # Thomas Jungblut <tjungblu@redhat.com>
reviewers:
  - ivanvc          # Ivan Valdes <ivan@vald.es> 
```

## File: `cmd/bbolt/README.md`
```markdown
# Introduction to bbolt command line

`bbolt` provides a command line utility for inspecting and manipulating bbolt database files. To install bbolt command-line please refer [here](https://github.com/etcd-io/bbolt#installing)

**Note**: [etcd](https://github.com/etcd-io/etcd) uses bbolt as its backend storage engine. In this document, we take etcd as an example to demonstrate the usage of bbolt commands. Refer to [install etcd](https://etcd.io/brain/knowledge/docs_legacy/v3.5/install/) for installing etcd.

1. Start a single member etcd cluster with this command below:

    ```bash
    $etcd
    ```

    It will create a directory `default.etcd` by default under current working directory, and the directory structure will look like this:

    ```bash
    $tree default.etcd
    default.etcd
    └── member
        ├── snap
        │   └── db // this is bbolt database file
        └── wal
            └── 0000000000000000-0000000000000000.wal

    3 directories, 2 files
    ```

2. Put some dummy data using [etcdctl](https://github.com/etcd-io/etcd/tree/main/etcdctl).
3. Stop the etcd instance. Note a bbolt database file can only be opened by one read-write process, because it is exclusively locked when opened.

## Usage

- `bbolt command [arguments]`

### help

- help will print information about that command

  ```bash
  $bbolt help

  The commands are:

      version     prints the current version of bbolt
      bench       run synthetic benchmark against bbolt
      buckets     print a list of buckets
      check       verifies integrity of bbolt database
      compact     copies a bbolt database, compacting it in the process
      dump        print a hexadecimal dump of a single page
      get         print the value of a key in a bucket
      info        print basic info
      keys        print a list of keys in a bucket
      help        print this screen
      page        print one or more pages in human readable format
      pages       print list of pages with their types
      page-item   print the key and value of a page item.
      stats       iterate over all pages and generate usage stats
      surgery     perform surgery on bbolt database
  ```

- you can use `help` with any command: `bbolt [command] -h` for more information about command.

## Analyse bbolt database with bbolt command line

### version

- `version` print the current version information of bbolt command-line.
- usage:
  `bbolt version`

  Example:
  
  ```bash
  $bbolt version
  bbolt version: 1.3.7
  Go Version: go1.21.6
  Go OS/Arch: darwin/arm64
  ```

### info

- `info` print the basic information about the given Bbolt database.
- usage:
  `bbolt info [path to the bbolt database]`

    Example:

    ```bash
    $bbolt info ~/default.etcd/member/snap/db
    Page Size: 4096
    ```

  - **note**: page size is given in bytes
  - Bbolt database is using page size of 4KB

### buckets

- `buckets` print a list of buckets of Bbolt database is currently having. Find more information on buckets [here](https://github.com/etcd-io/bbolt#using-buckets)
- usage:
  `bbolt buckets [path to the bbolt database]`

    Example:

    ```bash
    $bbolt buckets ~/default.etcd/member/snap/db
    alarm
    auth
    authRoles
    authUsers
    cluster
    key
    lease
    members
    members_removed
    meta
    ```

  - It means when you start an etcd, it creates these `10` buckets using bbolt database.

### check

- `check` opens a database at a given `[PATH]` and runs an exhaustive check to verify that all pages are accessible or are marked as freed. It also verifies that no pages are double referenced.
- usage:
  `bbolt check [path to the bbolt database]`

    Example:

    ```bash
    $bbolt check ~/default.etcd/member/snap/db
    ok
    ```

  - It returns `ok` as our database file `db` is not corrupted.

### stats

- To gather essential statistics about the bbolt database: `stats` performs an extensive search of the database to track every page reference. It starts at the current meta page and recursively iterates through every accessible bucket.
- usage:
  `bbolt stats [path to the bbolt database]`

  Example:

  ```bash
  $bbolt stats ~/default.etcd/member/snap/db
  Aggregate statistics for 10 buckets

  Page count statistics
      Number of logical branch pages: 0
      Number of physical branch overflow pages: 0
      Number of logical leaf pages: 0
      Number of physical leaf overflow pages: 0
  Tree statistics
      Number of keys/value pairs: 11
      Number of levels in B+tree: 1
  Page size utilization
      Bytes allocated for physical branch pages: 0
      Bytes actually used for branch data: 0 (0%)
      Bytes allocated for physical leaf pages: 0
      Bytes actually used for leaf data: 0 (0%)
  Bucket statistics
      Total number of buckets: 10
      Total number on inlined buckets: 10 (100%)
      Bytes used for inlined buckets: 780 (0%)
  ```

### inspect
- `inspect` inspect the structure of the database.
- Usage: `bbolt inspect [path to the bbolt database]`

  Example:
```bash
$ ./bbolt inspect ~/default.etcd/member/snap/db
{
    "name": "root",
    "keyN": 0,
    "buckets": [
        {
            "name": "alarm",
            "keyN": 0
        },
        {
            "name": "auth",
            "keyN": 2
        },
        {
            "name": "authRoles",
            "keyN": 1
        },
        {
            "name": "authUsers",
            "keyN": 1
        },
        {
            "name": "cluster",
            "keyN": 1
        },
        {
            "name": "key",
            "keyN": 1285
        },
        {
            "name": "lease",
            "keyN": 2
        },
        {
            "name": "members",
            "keyN": 1
        },
        {
            "name": "members_removed",
            "keyN": 0
        },
        {
            "name": "meta",
            "keyN": 3
        }
    ]
}
```

### pages

- Pages prints a table of pages with their type (meta, leaf, branch, freelist).
- The `meta` will store the metadata information of database.
- The `leaf` and `branch` pages will show a key count in the `items` column.
- The `freelist` will show the number of free pages, which are free for writing again.
- The `overflow` column shows the number of blocks that the page spills over into.
- usage:
  `bbolt pages [path to the bbolt database]`

  Example:

  ```bash
  $bbolt pages ~/default.etcd/member/snap/db
  ID       TYPE       ITEMS  OVRFLW
  ======== ========== ====== ======
  0        meta       0
  1        meta       0
  2        free
  3        leaf       10
  4        freelist   2
  5        free
  ```

### page

- Page prints one or more pages in human readable format.
- usage:

  ```bash
  bolt page [path to the bbolt database] pageid [pageid...]
  or: bolt page --all [path to the bbolt database]

  Additional options include:

  --all
    prints all pages (only skips pages that were considered successful overflow pages)
  --format-value=auto|ascii-encoded|hex|bytes|redacted (default: auto)
    prints values (on the leaf page) using the given format
  ```

  Example:

  ```bash
  $bbolt page ~/default.etcd/member/snap/db 3
  Page ID:    3
  Page Type:  leaf
  Total Size: 4096 bytes
  Overflow pages: 0
  Item Count: 10

  "alarm": <pgid=0,seq=0>
  "auth": <pgid=0,seq=0>
  "authRoles": <pgid=0,seq=0>
  "authUsers": <pgid=0,seq=0>
  "cluster": <pgid=0,seq=0>
  "key": <pgid=0,seq=0>
  "lease": <pgid=0,seq=0>
  "members": <pgid=0,seq=0>
  "members_removed": <pgid=0,seq=0>
  "meta": <pgid=0,seq=0>
  ```

  - It prints information of page `page ID: 3`

### page-item

- page-item prints a page item's key and value.
- usage:

  ```bash
  bolt page-item [options] [path to the bbolt database] <pageId> <itemId>
  Additional options include:

      --key-only
          Print only the key
      --value-only
          Print only the value
      --format
          Output format. One of: auto|ascii-encoded|hex|bytes|redacted (default=auto)
  ```

  Example:

  ```bash
  $bbolt page-item --key-only ~/default.etcd/member/snap/db 3 7
  "members"
  ```

  - It returns the key as `--key-only` flag is passed of `pageID: 3` and `itemID: 7`

### dump

- Dump prints a hexadecimal dump of one or more given pages.
- usage:
  `bolt dump [path to the bbolt database] [pageid...]`

### keys

- Print a list of keys in the given bucket.
- usage:

  ```bash
  bolt keys [path to the bbolt database] [BucketName]

  Additional options include:
  --format
    Output format. One of: auto|ascii-encoded|hex|bytes|redacted (default=auto)
  ```

  Example 1:

  ```bash
  $bbolt keys ~/default.etcd/member/snap/db meta
  confState
  consistent_index
  term
  ```

  - It list all the keys in bucket: `meta`

  Example 2:

  ```bash
  $bbolt keys ~/default.etcd/member/snap/db members
  8e9e05c52164694d
  ```

  - It list all the keys in `members` bucket which is a `memberId` of etcd cluster member.
  - In this case we are running a single member etcd cluster, hence only `one memberId` is present. If we would have run a `3` member etcd cluster then it will return a `3 memberId` as `3 cluster members` would have been present in `members` bucket.

### get

- Print the value of the given key in the given bucket.
- usage:
  
  ```bash
  bolt get [path to the bbolt database] [BucketName] [Key]

  Additional options include:
  --format
    Output format. One of: auto|ascii-encoded|hex|bytes|redacted (default=auto)
  --parse-format
    Input format (of key). One of: ascii-encoded|hex (default=ascii-encoded)"
  ```

  Example 1:

  ```bash
  $bbolt get --format=hex ~/default.etcd/member/snap/db meta term
  0000000000000004
  ```

  - It returns the value present in bucket: `meta` for key: `term` in hexadecimal format.

  Example 2:

  ```bash
  $bbolt get ~/default.etcd/member/snap/db members 8e9e05c52164694d
  {"id":10276657743932975437,"peerURLs":["http://localhost:2380"],"name":"default","clientURLs":["http://localhost:2379"]}
  ```

  - It returns the value present in bucket: `members` for key: `8e9e05c52164694d`.

### compact

- Compact opens a database at given `[Source Path]` and walks it recursively, copying keys as they are found from all buckets, to a newly created database at `[Destination Path]`. The original database is left untouched.
- usage:

  ```bash
  bbolt compact [options] -o [Destination Path] [Source Path]

  Additional options include:

  -tx-max-size NUM
    Specifies the maximum size of individual transactions.
    Defaults to 64KB
  ```

  Example:

  ```bash
  $bbolt compact -o ~/db.compact ~/default.etcd/member/snap/db
  16805888 -> 32768 bytes (gain=512.88x)
  ```

  - It will create a compacted database file: `db.compact` at given path.

### bench

- run synthetic benchmark against bbolt database.
- usage:

    ```bash
    Usage:
    -batch-size int

    -blockprofile string

    -count int
            (default 1000)
    -cpuprofile string

    -fill-percent float
            (default 0.5)
    -key-size int
            (default 8)
    -memprofile string

    -no-sync

    -path string

    -profile-mode string
            (default "rw")
    -read-mode string
            (default "seq")
    -value-size int
            (default 32)
    -work

    -write-mode string
            (default "seq")
    ```

    Example:

    ```bash
    $bbolt bench ~/default.etcd/member/snap/db -batch-size 400 -key-size 16
    # Write	68.523572ms	(68.523µs/op)	(14593 op/sec)
    # Read	1.000015152s	(11ns/op)	(90909090 op/sec)
    ```

  - It runs a benchmark with batch size of `400` and with key size of `16` while for others parameters default value is taken.

### surgery

- `surgery` perform surgery on bbolt database for repair and recovery operations.
- usage:
  `bbolt surgery <subcommand> [arguments]`

  The surgery subcommands are:
  - `revert-meta-page` - revert to previous transaction state
  - `copy-page` - copy page from source to destination
  - `clear-page` - clear all elements from a page
  - `clear-page-elements` - clear specific elements from a page
  - `freelist` - freelist related surgery commands
  - `meta` - meta page related surgery commands

#### surgery revert-meta-page

- `surgery revert-meta-page` reverts to the previous transaction state by replacing the active meta page with the inactive one.
- usage:

  ```bash
  bbolt surgery revert-meta-page [path to the bbolt database] --output [output-file]
  ```

  Example:

  ```bash
  $bbolt surgery revert-meta-page ~/default.etcd/member/snap/db --output reverted.db
  The meta page is reverted.
  ```

  - This is particularly useful when the most recent transaction has corrupted the database and you need to roll back to the previous consistent state.

#### surgery copy-page

- `surgery copy-page` copies content from one page to another.
- usage:

  ```bash
  bbolt surgery copy-page [path to the bbolt database] --output [output-file] --from-page [source-id] --to-page [destination-id]
  ```

  Example:

  ```bash
  $bbolt surgery copy-page ~/default.etcd/member/snap/db --output copied.db --from-page 3 --to-page 2
  The page 3 was successfully copied to page 2
  WARNING: the free list might have changed.
  Please consider executing `./bbolt surgery freelist abandon ...`
  ```

  - This command is useful for recovering data from damaged pages or creating page backups.

#### surgery clear-page

- `surgery clear-page` removes all elements from a branch or leaf page.
- usage:

  ```bash
  bbolt surgery clear-page [path to the bbolt database] --output [output-file] --pageId [page-id]
  ```

  Example:

  ```bash
  $bbolt surgery clear-page ~/default.etcd/member/snap/db --output cleared.db --pageId 3
  The page (3) was cleared
  WARNING: The clearing has abandoned some pages that are not yet referenced from free list.
  Please consider executing `./bbolt surgery freelist abandon ...`
  ```

  - The pageId must be at least 2 (meta pages 0 and 1 cannot be cleared).

#### surgery clear-page-elements

- `surgery clear-page-elements` removes specific elements from a branch or leaf page by index range.
- usage:

  ```bash
  bbolt surgery clear-page-elements [path to the bbolt database] --output [output-file] --pageId [page-id] --from-index [start] --to-index [end]
  ```

  Example:

  ```bash
  $bbolt surgery clear-page-elements ~/default.etcd/member/snap/db --output partial.db --pageId 3 --from-index 1 --to-index 4
  All elements in [1, 4) in page 3 were cleared
  WARNING: The clearing has abandoned some pages that are not yet referenced from free list.
  Please consider executing `./bbolt surgery freelist abandon ...`
  ```

  - Use `--to-index -1` to clear elements to the end of the page.

#### surgery freelist

- `surgery freelist` provides commands for managing the database's free page list.
- usage:

  ```bash
  bbolt surgery freelist <subcommand> [arguments]
  ```

  The freelist subcommands are:

  - `abandon` - remove freelist references from meta pages
  - `rebuild` - rebuild the freelist by scanning the database

##### surgery freelist abandon

- `surgery freelist abandon` removes freelist references from both meta pages, forcing Bbolt to reconstruct the freelist when the database is next opened.
- usage:

  ```bash
  bbolt surgery freelist abandon [path to the bbolt database] --output [output-file]
  ```

  Example:

  ```bash
  $bbolt surgery freelist abandon ~/default.etcd/member/snap/db --output abandoned.db
  The freelist was abandoned in both meta pages.
  It may cause some delay on next startup because bbolt needs to scan the whole db to reconstruct the free list.
  ```

  - This sets the freelist page ID to a special value indicating the freelist is not present.

##### surgery freelist rebuild

- `surgery freelist rebuild` rebuilds the freelist in a database where the freelist has been abandoned.
- usage:

  ```bash
  bbolt surgery freelist rebuild [path to the bbolt database] --output [output-file]
  ```

  Example:

  ```bash
  $bbolt surgery freelist rebuild ~/default.etcd/member/snap/db --output rebuilt.db
  The freelist was successfully rebuilt.
  ```

  - This command opens the database and lets Bbolt automatically reconstruct and sync the freelist.

#### surgery meta

- `surgery meta` provides commands for working with database metadata pages.
- usage:

  ```bash
  bbolt surgery meta <subcommand> [arguments]
  ```
  
  The meta subcommands are:
  - `validate` - validate integrity of meta pages
  - `update` - update specific fields in meta pages

##### surgery meta validate

- `surgery meta validate` validates the integrity of both meta pages in the database.
- usage:

  ```bash
  bbolt surgery meta validate [path to the bbolt database]
  ```

  Example:

  ```bash
  $bbolt surgery meta validate ~/default.etcd/member/snap/db
  The meta page 0 is valid!
  The meta page 1 is valid!
  ```

  - It checks magic number values, version compatibility, checksum integrity, and general metadata validity for both meta pages (0 and 1).

##### surgery meta update

- `surgery meta update` updates specific fields in a meta page for manual repair of corrupted metadata.
- usage:

  ```bash
  bbolt surgery meta update [path to the bbolt database] --output [output-file] --meta-page [0|1] --fields [field:value,...]
  ```

  Supported fields:
  - `pageSize` - Size of database pages
  - `root` - Root bucket page ID
  - `freelist` - Freelist page ID
  - `pgid` - Next page ID to allocate

  Example:

  ```bash
  $bbolt surgery meta update ~/default.etcd/member/snap/db --output fixed.db --meta-page 0 --fields root:16,freelist:8
  The meta page 0 has been updated!
  ```

  - It updates the specified meta page and automatically updates magic number, version, flags, and checksum to ensure consistency.
```

## File: `cmd/bbolt/main.go`
```go
package main

import (
	"fmt"
	"os"

	"go.etcd.io/bbolt/cmd/bbolt/command"
)

func main() {
	rootCmd := command.NewRootCommand()
	if err := rootCmd.Execute(); err != nil {
		if rootCmd.SilenceErrors {
			fmt.Fprintln(os.Stderr, "Error:", err)
		}
		os.Exit(1)
	}
}
```

## File: `cmd/bbolt/command/command_bench.go`
```go
package command

import (
	"encoding/binary"
	"fmt"
	"io"
	"math"
	"math/rand"
	"os"
	"runtime"
	"runtime/pprof"
	"sync/atomic"
	"testing"
	"time"

	"github.com/spf13/cobra"
	"github.com/spf13/pflag"

	bolt "go.etcd.io/bbolt"
	"go.etcd.io/bbolt/internal/common"
)

var benchBucketName = []byte("bench")

type benchOptions struct {
	profileMode     string
	writeMode       string
	readMode        string
	iterations      int64
	batchSize       int64
	keySize         int
	valueSize       int
	cpuProfile      string
	memProfile      string
	blockProfile    string
	fillPercent     float64
	noSync          bool
	work            bool
	path            string
	goBenchOutput   bool
	pageSize        int
	initialMmapSize int
	deleteFraction  float64 // Fraction of keys of last tx to delete during writes. works only with "seq-del" write mode.
}

func (o *benchOptions) AddFlags(fs *pflag.FlagSet) {
	fs.StringVar(&o.profileMode, "profile-mode", "rw", "")
	fs.StringVar(&o.writeMode, "write-mode", "seq", "")
	fs.StringVar(&o.readMode, "read-mode", "seq", "")
	fs.Int64Var(&o.iterations, "count", 1000, "")
	fs.Int64Var(&o.batchSize, "batch-size", 0, "")
	fs.IntVar(&o.keySize, "key-size", 8, "")
	fs.IntVar(&o.valueSize, "value-size", 32, "")
	fs.StringVar(&o.cpuProfile, "cpuprofile", "", "")
	fs.StringVar(&o.memProfile, "memprofile", "", "")
	fs.StringVar(&o.blockProfile, "blockprofile", "", "")
	fs.Float64Var(&o.fillPercent, "fill-percent", bolt.DefaultFillPercent, "")
	fs.BoolVar(&o.noSync, "no-sync", false, "")
	fs.BoolVar(&o.work, "work", false, "")
	fs.StringVar(&o.path, "path", "", "")
	fs.BoolVar(&o.goBenchOutput, "gobench-output", false, "")
	fs.IntVar(&o.pageSize, "page-size", common.DefaultPageSize, "Set page size in bytes.")
	fs.IntVar(&o.initialMmapSize, "initial-mmap-size", 0, "Set initial mmap size in bytes for database file.")
}

// Returns an error if `bench` options are not valid.
func (o *benchOptions) Validate() error {
	// Require that batch size can be evenly divided by the iteration count if set.
	if o.batchSize > 0 && o.iterations%o.batchSize != 0 {
		return ErrBatchNonDivisibleBatchSize
	}

	switch o.writeMode {
	case "seq", "rnd", "seq-nest", "rnd-nest":
	default:
		return ErrBatchInvalidWriteMode
	}

	// Generate temp path if one is not passed in.
	if o.path == "" {
		f, err := os.CreateTemp("", "bolt-bench-")
		if err != nil {
			return fmt.Errorf("temp file: %s", err)
		}
		f.Close()
		os.Remove(f.Name())
		o.path = f.Name()
	}

	return nil
}

// Sets the `bench` option values that are dependent on other options.
func (o *benchOptions) SetOptionValues() error {
	// Generate temp path if one is not passed in.
	if o.path == "" {
		f, err := os.CreateTemp("", "bolt-bench-")
		if err != nil {
			return fmt.Errorf("error creating temp file: %s", err)
		}
		f.Close()
		os.Remove(f.Name())
		o.path = f.Name()
	}

	// Set batch size to iteration size if not set.
	if o.batchSize == 0 {
		o.batchSize = o.iterations
	}

	return nil
}

func newBenchCommand() *cobra.Command {
	var o benchOptions

	benchCmd := &cobra.Command{
		Use:   "bench",
		Short: "run synthetic benchmark against bbolt",
		RunE: func(cmd *cobra.Command, args []string) error {
			if err := o.Validate(); err != nil {
				return err
			}
			if err := o.SetOptionValues(); err != nil {
				return err
			}
			return benchFunc(cmd, &o)
		},
	}

	o.AddFlags(benchCmd.Flags())

	return benchCmd
}

func benchFunc(cmd *cobra.Command, options *benchOptions) error {
	// Remove path if "-work" is not set. Otherwise keep path.
	if options.work {
		fmt.Fprintf(cmd.ErrOrStderr(), "work: %s\n", options.path)
	} else {
		defer os.Remove(options.path)
	}

	// Create database.
	dbOptions := *bolt.DefaultOptions
	dbOptions.PageSize = options.pageSize
	dbOptions.InitialMmapSize = options.initialMmapSize
	db, err := bolt.Open(options.path, 0600, &dbOptions)
	if err != nil {
		return err
	}
	db.NoSync = options.noSync
	defer db.Close()

	r := rand.New(rand.NewSource(time.Now().UnixNano()))

	var writeResults benchResults

	fmt.Fprintf(cmd.ErrOrStderr(), "starting write benchmark.\n")
	keys, err := runWrites(cmd, db, options, &writeResults, r)
	if err != nil {
		return fmt.Errorf("write: %v", err)
	}

	if keys != nil {
		r.Shuffle(len(keys), func(i, j int) {
			keys[i], keys[j] = keys[j], keys[i]
		})
	}

	var readResults benchResults
	fmt.Fprintf(cmd.ErrOrStderr(), "starting read benchmark.\n")
	// Read from the database.
	if err := runReads(cmd, db, options, &readResults, keys); err != nil {
		return fmt.Errorf("bench: read: %s", err)
	}

	// Print results.
	if options.goBenchOutput {
		// below replicates the output of testing.B benchmarks, e.g. for external tooling
		benchWriteName := "BenchmarkWrite"
		benchReadName := "BenchmarkRead"
		maxLen := max(len(benchReadName), len(benchWriteName))
		printGoBenchResult(cmd.OutOrStdout(), writeResults, maxLen, benchWriteName)
		printGoBenchResult(cmd.OutOrStdout(), readResults, maxLen, benchReadName)
	} else {
		fmt.Fprintf(cmd.OutOrStdout(), "# Write\t%v(ops)\t%v\t(%v/op)\t(%v op/sec)\n", writeResults.getCompletedOps(), writeResults.getDuration(), writeResults.opDuration(), writeResults.opsPerSecond())
		fmt.Fprintf(cmd.OutOrStdout(), "# Read\t%v(ops)\t%v\t(%v/op)\t(%v op/sec)\n", readResults.getCompletedOps(), readResults.getDuration(), readResults.opDuration(), readResults.opsPerSecond())
	}
	fmt.Fprintln(cmd.OutOrStdout(), "")

	return nil
}

func runWrites(cmd *cobra.Command, db *bolt.DB, options *benchOptions, results *benchResults, r *rand.Rand) ([]nestedKey, error) {
	// Start profiling for writes.
	if options.profileMode == "rw" || options.profileMode == "w" {
		startProfiling(cmd, options)
	}

	finishChan := make(chan interface{})
	go checkProgress(results, finishChan, cmd.ErrOrStderr())
	defer close(finishChan)

	t := time.Now()

	var keys []nestedKey
	var err error
	switch options.writeMode {
	case "seq":
		keys, err = runWritesSequential(cmd, db, options, results)
	case "rnd":
		keys, err = runWritesRandom(cmd, db, options, results, r)
	case "seq-nest":
		keys, err = runWritesSequentialNested(cmd, db, options, results)
	case "rnd-nest":
		keys, err = runWritesRandomNested(cmd, db, options, results, r)
	case "seq-del":
		options.deleteFraction = 0.1
		keys, err = runWritesSequentialAndDelete(cmd, db, options, results)
	default:
		return nil, fmt.Errorf("invalid write mode: %s", options.writeMode)
	}

	// Save time to write.
	results.setDuration(time.Since(t))

	// Stop profiling for writes only.
	if options.profileMode == "w" {
		stopProfiling(cmd)
	}

	return keys, err
}

func runWritesSequential(cmd *cobra.Command, db *bolt.DB, options *benchOptions, results *benchResults) ([]nestedKey, error) {
	var i = uint32(0)
	return runWritesWithSource(cmd, db, options, results, func() uint32 { i++; return i })
}

func runWritesSequentialAndDelete(cmd *cobra.Command, db *bolt.DB, options *benchOptions, results *benchResults) ([]nestedKey, error) {
	var i = uint32(0)
	return runWritesDeletesWithSource(cmd, db, options, results, func() uint32 { i++; return i })
}

func runWritesRandom(cmd *cobra.Command, db *bolt.DB, options *benchOptions, results *benchResults, r *rand.Rand) ([]nestedKey, error) {
	return runWritesWithSource(cmd, db, options, results, func() uint32 { return r.Uint32() })
}

func runWritesSequentialNested(cmd *cobra.Command, db *bolt.DB, options *benchOptions, results *benchResults) ([]nestedKey, error) {
	var i = uint32(0)
	return runWritesNestedWithSource(cmd, db, options, results, func() uint32 { i++; return i })
}

func runWritesRandomNested(cmd *cobra.Command, db *bolt.DB, options *benchOptions, results *benchResults, r *rand.Rand) ([]nestedKey, error) {
	return runWritesNestedWithSource(cmd, db, options, results, func() uint32 { return r.Uint32() })
}

func runWritesWithSource(cmd *cobra.Command, db *bolt.DB, options *benchOptions, results *benchResults, keySource func() uint32) ([]nestedKey, error) {
	var keys []nestedKey
	if options.readMode == "rnd" {
		keys = make([]nestedKey, 0, options.iterations)
	}

	for i := int64(0); i < options.iterations; i += options.batchSize {
		if err := db.Update(func(tx *bolt.Tx) error {
			b, _ := tx.CreateBucketIfNotExists(benchBucketName)
			b.FillPercent = options.fillPercent

			fmt.Fprintf(cmd.ErrOrStderr(), "Starting write iteration %d\n", i)
			for j := int64(0); j < options.batchSize; j++ {
				key := make([]byte, options.keySize)
				value := make([]byte, options.valueSize)

				// Write key as uint32.
				binary.BigEndian.PutUint32(key, keySource())

				// Insert key/value.
				if err := b.Put(key, value); err != nil {
					return err
				}
				if keys != nil {
					keys = append(keys, nestedKey{nil, key})
				}
				results.addCompletedOps(1)
			}
			fmt.Fprintf(cmd.ErrOrStderr(), "Finished write iteration %d\n", i)

			return nil
		}); err != nil {
			return nil, err
		}
	}
	return keys, nil
}

func runWritesDeletesWithSource(cmd *cobra.Command, db *bolt.DB, options *benchOptions, results *benchResults, keySource func() uint32) ([]nestedKey, error) {
	var keys []nestedKey
	deleteSize := int64(math.Ceil(float64(options.batchSize) * options.deleteFraction))
	var InsertedKeys [][]byte

	for i := int64(0); i < options.iterations; i += options.batchSize {
		if err := db.Update(func(tx *bolt.Tx) error {
			b, _ := tx.CreateBucketIfNotExists(benchBucketName)
			b.FillPercent = options.fillPercent

			fmt.Fprintf(cmd.ErrOrStderr(), "Starting delete iteration %d, deleteSize: %d\n", i, deleteSize)
			for i := int64(0); i < deleteSize && i < int64(len(InsertedKeys)); i++ {
				if err := b.Delete(InsertedKeys[i]); err != nil {
					return err
				}
			}
			InsertedKeys = InsertedKeys[:0]
			fmt.Fprintf(cmd.ErrOrStderr(), "Finished delete iteration %d\n", i)

			fmt.Fprintf(cmd.ErrOrStderr(), "Starting write iteration %d\n", i)
			for j := int64(0); j < options.batchSize; j++ {

				key := make([]byte, options.keySize)
				value := make([]byte, options.valueSize)

				// Write key as uint32.
				binary.BigEndian.PutUint32(key, keySource())
				InsertedKeys = append(InsertedKeys, key)

				// Insert key/value.
				if err := b.Put(key, value); err != nil {
					return err
				}
				if keys != nil {
					keys = append(keys, nestedKey{nil, key})
				}
				results.addCompletedOps(1)
			}
			fmt.Fprintf(cmd.ErrOrStderr(), "Finished write iteration %d\n", i)
			return nil
		}); err != nil {
			return nil, err
		}
	}
	return keys, nil
}

func runWritesNestedWithSource(cmd *cobra.Command, db *bolt.DB, options *benchOptions, results *benchResults, keySource func() uint32) ([]nestedKey, error) {
	var keys []nestedKey
	if options.readMode == "rnd" {
		keys = make([]nestedKey, 0, options.iterations)
	}

	for i := int64(0); i < options.iterations; i += options.batchSize {
		if err := db.Update(func(tx *bolt.Tx) error {
			top, err := tx.CreateBucketIfNotExists(benchBucketName)
			if err != nil {
				return err
			}
			top.FillPercent = options.fillPercent

			// Create bucket key.
			name := make([]byte, options.keySize)
			binary.BigEndian.PutUint32(name, keySource())

			// Create bucket.
			b, err := top.CreateBucketIfNotExists(name)
			if err != nil {
				return err
			}
			b.FillPercent = options.fillPercent

			fmt.Fprintf(cmd.ErrOrStderr(), "Starting write iteration %d\n", i)
			for j := int64(0); j < options.batchSize; j++ {
				var key = make([]byte, options.keySize)
				var value = make([]byte, options.valueSize)

				// Generate key as uint32.
				binary.BigEndian.PutUint32(key, keySource())

				// Insert value into subbucket.
				if err := b.Put(key, value); err != nil {
					return err
				}
				if keys != nil {
					keys = append(keys, nestedKey{name, key})
				}
				results.addCompletedOps(1)
			}
			fmt.Fprintf(cmd.ErrOrStderr(), "Finished write iteration %d\n", i)

			return nil
		}); err != nil {
			return nil, err
		}
	}
	return keys, nil
}

func runReads(cmd *cobra.Command, db *bolt.DB, options *benchOptions, results *benchResults, keys []nestedKey) error {
	// Start profiling for reads.
	if options.profileMode == "r" {
		startProfiling(cmd, options)
	}

	finishChan := make(chan interface{})
	go checkProgress(results, finishChan, cmd.ErrOrStderr())
	defer close(finishChan)

	t := time.Now()

	var err error
	switch options.readMode {
	case "seq":
		switch options.writeMode {
		case "seq-nest", "rnd-nest":
			err = runReadsSequentialNested(cmd, db, options, results)
		default:
			err = runReadsSequential(cmd, db, options, results)
		}
	case "rnd":
		switch options.writeMode {
		case "seq-nest", "rnd-nest":
			err = runReadsRandomNested(cmd, db, options, keys, results)
		default:
			err = runReadsRandom(cmd, db, options, keys, results)
		}
	default:
		return fmt.Errorf("invalid read mode: %s", options.readMode)
	}

	// Save read time.
	results.setDuration(time.Since(t))

	// Stop profiling for reads.
	if options.profileMode == "rw" || options.profileMode == "r" {
		stopProfiling(cmd)
	}

	return err
}

type nestedKey struct{ bucket, key []byte }

func runReadsSequential(cmd *cobra.Command, db *bolt.DB, options *benchOptions, results *benchResults) error {
	return db.View(func(tx *bolt.Tx) error {
		t := time.Now()

		for {
			numReads := int64(0)
			err := func() error {
				defer func() { results.addCompletedOps(numReads) }()

				c := tx.Bucket(benchBucketName).Cursor()
				for k, v := c.First(); k != nil; k, v = c.Next() {
					numReads++
					if v == nil {
						return ErrInvalidValue
					}
				}

				return nil
			}()

			if err != nil {
				return err
			}

			if options.writeMode == "seq" && numReads != options.iterations {
				return fmt.Errorf("read seq: iter mismatch: expected %d, got %d", options.iterations, numReads)
			}

			// Make sure we do this for at least a second.
			if time.Since(t) >= time.Second {
				break
			}
		}

		return nil
	})
}

func runReadsRandom(cmd *cobra.Command, db *bolt.DB, options *benchOptions, keys []nestedKey, results *benchResults) error {
	return db.View(func(tx *bolt.Tx) error {
		t := time.Now()

		for {
			numReads := int64(0)
			err := func() error {
				defer func() { results.addCompletedOps(numReads) }()

				b := tx.Bucket(benchBucketName)
				for _, key := range keys {
					v := b.Get(key.key)
					numReads++
					if v == nil {
						return ErrInvalidValue
					}
				}

				return nil
			}()

			if err != nil {
				return err
			}

			if options.writeMode == "seq" && numReads != options.iterations {
				return fmt.Errorf("read seq: iter mismatch: expected %d, got %d", options.iterations, numReads)
			}

			// Make sure we do this for at least a second.
			if time.Since(t) >= time.Second {
				break
			}
		}

		return nil
	})
}

func runReadsSequentialNested(cmd *cobra.Command, db *bolt.DB, options *benchOptions, results *benchResults) error {
	return db.View(func(tx *bolt.Tx) error {
		t := time.Now()

		for {
			numReads := int64(0)
			var top = tx.Bucket(benchBucketName)
			if err := top.ForEach(func(name, _ []byte) error {
				defer func() { results.addCompletedOps(numReads) }()
				if b := top.Bucket(name); b != nil {
					c := b.Cursor()
					for k, v := c.First(); k != nil; k, v = c.Next() {
						numReads++
						if v == nil {
							return ErrInvalidValue
						}
					}
				}
				return nil
			}); err != nil {
				return err
			}

			if options.writeMode == "seq-nest" && numReads != options.iterations {
				return fmt.Errorf("read seq-nest: iter mismatch: expected %d, got %d", options.iterations, numReads)
			}

			// Make sure we do this for at least a second.
			if time.Since(t) >= time.Second {
				break
			}
		}

		return nil
	})
}

func runReadsRandomNested(cmd *cobra.Command, db *bolt.DB, options *benchOptions, nestedKeys []nestedKey, results *benchResults) error {
	return db.View(func(tx *bolt.Tx) error {
		t := time.Now()

		for {
			numReads := int64(0)
			err := func() error {
				defer func() { results.addCompletedOps(numReads) }()

				var top = tx.Bucket(benchBucketName)
				for _, nestedKey := range nestedKeys {
					if b := top.Bucket(nestedKey.bucket); b != nil {
						v := b.Get(nestedKey.key)
						numReads++
						if v == nil {
							return ErrInvalidValue
						}
					}
				}

				return nil
			}()

			if err != nil {
				return err
			}

			if options.writeMode == "seq-nest" && numReads != options.iterations {
				return fmt.Errorf("read seq-nest: iter mismatch: expected %d, got %d", options.iterations, numReads)
			}

			// Make sure we do this for at least a second.
			if time.Since(t) >= time.Second {
				break
			}
		}

		return nil
	})
}

func checkProgress(results *benchResults, finishChan chan interface{}, stderr io.Writer) {
	ticker := time.Tick(time.Second)
	lastCompleted, lastTime := int64(0), time.Now()
	for {
		select {
		case <-finishChan:
			return
		case t := <-ticker:
			completed, taken := results.getCompletedOps(), t.Sub(lastTime)
			fmt.Fprintf(stderr, "Completed %d requests, %d/s \n",
				completed, ((completed-lastCompleted)*int64(time.Second))/int64(taken),
			)
			lastCompleted, lastTime = completed, t
		}
	}
}

var cpuprofile, memprofile, blockprofile *os.File

func startProfiling(cmd *cobra.Command, options *benchOptions) {
	var err error

	// Start CPU profiling.
	if options.cpuProfile != "" {
		cpuprofile, err = os.Create(options.cpuProfile)
		if err != nil {
			fmt.Fprintf(cmd.ErrOrStderr(), "bench: could not create cpu profile %q: %v\n", options.cpuProfile, err)
			os.Exit(1)
		}
		err = pprof.StartCPUProfile(cpuprofile)
		if err != nil {
			fmt.Fprintf(cmd.ErrOrStderr(), "bench: could not start cpu profile %q: %v\n", options.cpuProfile, err)
			os.Exit(1)
		}
	}

	// Start memory profiling.
	if options.memProfile != "" {
		memprofile, err = os.Create(options.memProfile)
		if err != nil {
			fmt.Fprintf(cmd.ErrOrStderr(), "bench: could not create memory profile %q: %v\n", options.memProfile, err)
			os.Exit(1)
		}
		runtime.MemProfileRate = 4096
	}

	// Start fatal profiling.
	if options.blockProfile != "" {
		blockprofile, err = os.Create(options.blockProfile)
		if err != nil {
			fmt.Fprintf(cmd.ErrOrStderr(), "bench: could not create block profile %q: %v\n", options.blockProfile, err)
			os.Exit(1)
		}
		runtime.SetBlockProfileRate(1)
	}
}

func stopProfiling(cmd *cobra.Command) {
	if cpuprofile != nil {
		pprof.StopCPUProfile()
		cpuprofile.Close()
		cpuprofile = nil
	}

	if memprofile != nil {
		err := pprof.Lookup("heap").WriteTo(memprofile, 0)
		if err != nil {
			fmt.Fprintf(cmd.ErrOrStderr(), "bench: could not write mem profile")
		}
		memprofile.Close()
		memprofile = nil
	}

	if blockprofile != nil {
		err := pprof.Lookup("block").WriteTo(blockprofile, 0)
		if err != nil {
			fmt.Fprintf(cmd.ErrOrStderr(), "bench: could not write block profile")
		}
		blockprofile.Close()
		blockprofile = nil
		runtime.SetBlockProfileRate(0)
	}
}

// benchResults represents the performance results of the benchmark and is thread-safe.
type benchResults struct {
	completedOps int64
	duration     int64
}

func (r *benchResults) addCompletedOps(amount int64) {
	atomic.AddInt64(&r.completedOps, amount)
}

func (r *benchResults) getCompletedOps() int64 {
	return atomic.LoadInt64(&r.completedOps)
}

func (r *benchResults) setDuration(dur time.Duration) {
	atomic.StoreInt64(&r.duration, int64(dur))
}

func (r *benchResults) getDuration() time.Duration {
	return time.Duration(atomic.LoadInt64(&r.duration))
}

// opDuration returns the duration for a single read/write operation.
func (r *benchResults) opDuration() time.Duration {
	if r.getCompletedOps() == 0 {
		return 0
	}
	return r.getDuration() / time.Duration(r.getCompletedOps())
}

// opsPerSecond returns average number of read/write operations that can be performed per second.
func (r *benchResults) opsPerSecond() int {
	var op = r.opDuration()
	if op == 0 {
		return 0
	}
	return int(time.Second) / int(op)
}

func printGoBenchResult(w io.Writer, r benchResults, maxLen int, benchName string) {
	gobenchResult := testing.BenchmarkResult{}
	gobenchResult.T = r.getDuration()
	gobenchResult.N = int(r.getCompletedOps())
	fmt.Fprintf(w, "%-*s\t%s\n", maxLen, benchName, gobenchResult.String())
}
```

## File: `cmd/bbolt/command/command_bench_test.go`
```go
package command_test

import (
	"bytes"
	"fmt"
	"strings"
	"sync"
	"testing"

	"github.com/stretchr/testify/require"

	"go.etcd.io/bbolt/cmd/bbolt/command"
)

type safeWriter struct {
	buf *bytes.Buffer
	mu  sync.Mutex
}

func (w *safeWriter) Write(p []byte) (n int, err error) {
	w.mu.Lock()
	defer w.mu.Unlock()
	return w.buf.Write(p)
}

func (w *safeWriter) String() string {
	w.mu.Lock()
	defer w.mu.Unlock()
	return w.buf.String()
}

func newSafeWriter() *safeWriter {
	return &safeWriter{buf: bytes.NewBufferString("")}
}

// Ensure the "bench" command runs and exits without errors
func TestBenchCommand_Run(t *testing.T) {
	tests := map[string]struct {
		args []string
	}{
		"no-args":    {},
		"100k count": {[]string{"--count", "100000"}},
	}

	for name, test := range tests {
		t.Run(name, func(t *testing.T) {
			// Run the command.
			rootCmd := command.NewRootCommand()

			outputWriter := newSafeWriter()
			rootCmd.SetOut(outputWriter)

			errorWriter := newSafeWriter()
			rootCmd.SetErr(errorWriter)

			args := append([]string{"bench"}, test.args...)
			rootCmd.SetArgs(args)

			err := rootCmd.Execute()
			require.NoError(t, err)

			outStr := outputWriter.String()
			errStr := errorWriter.String()

			if !strings.Contains(errStr, "starting write benchmark.") || !strings.Contains(errStr, "starting read benchmark.") {
				t.Fatal(fmt.Errorf("benchmark result does not contain read/write start output:\n%s", outStr))
			}

			if strings.Contains(errStr, "iter mismatch") {
				t.Fatal(fmt.Errorf("found iter mismatch in stdout:\n%s", outStr))
			}

			if !strings.Contains(outStr, "# Write") || !strings.Contains(outStr, "# Read") {
				t.Fatal(fmt.Errorf("benchmark result does not contain read/write output:\n%s", outStr))
			}
		})
	}
}
```

## File: `cmd/bbolt/command/command_buckets.go`
```go
package command

import (
	"fmt"

	"github.com/spf13/cobra"

	bolt "go.etcd.io/bbolt"
)

func newBucketsCommand() *cobra.Command {
	bucketsCmd := &cobra.Command{
		Use:   "buckets <bbolt-file>",
		Short: "print a list of buckets in bbolt database",
		Args:  cobra.ExactArgs(1),
		RunE: func(cmd *cobra.Command, args []string) error {
			return bucketsFunc(cmd, args[0])
		},
	}

	return bucketsCmd
}

func bucketsFunc(cmd *cobra.Command, dbPath string) error {
	if _, err := checkSourceDBPath(dbPath); err != nil {
		return err
	}

	// Open database.
	db, err := bolt.Open(dbPath, 0600, &bolt.Options{
		ReadOnly:        true,
		PreLoadFreelist: true,
	})
	if err != nil {
		return err
	}
	defer db.Close()

	// Print buckets.
	return db.View(func(tx *bolt.Tx) error {
		return tx.ForEach(func(name []byte, _ *bolt.Bucket) error {
			fmt.Fprintln(cmd.OutOrStdout(), string(name))
			return nil
		})
	})
}
```

## File: `cmd/bbolt/command/command_buckets_test.go`
```go
package command_test

import (
	"bytes"
	"io"
	"testing"

	"github.com/stretchr/testify/require"

	bolt "go.etcd.io/bbolt"
	"go.etcd.io/bbolt/cmd/bbolt/command"
	"go.etcd.io/bbolt/internal/btesting"
)

// Ensure the "buckets" command can print a list of buckets.
func TestBucketsCommand_Run(t *testing.T) {

	testCases := []struct {
		name      string
		args      []string
		expErr    error
		expOutput string
	}{
		{
			name:      "buckets all buckets in bbolt database",
			args:      []string{"buckets", "path"},
			expErr:    nil,
			expOutput: "bar\nbaz\nfoo\n",
		},
	}

	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {

			t.Log("Creating sample DB")
			db := btesting.MustCreateDB(t)
			if err := db.Update(func(tx *bolt.Tx) error {
				for _, name := range []string{"foo", "bar", "baz"} {
					_, err := tx.CreateBucket([]byte(name))
					if err != nil {
						return err
					}
				}
				return nil
			}); err != nil {
				t.Fatal(err)
			}
			db.Close()
			defer requireDBNoChange(t, dbData(t, db.Path()), db.Path())

			t.Log("Running buckets cmd")
			rootCmd := command.NewRootCommand()
			outputBuf := bytes.NewBufferString("")
			rootCmd.SetOut(outputBuf)

			tc.args[1] = db.Path()
			rootCmd.SetArgs(tc.args)
			err := rootCmd.Execute()
			require.Equal(t, tc.expErr, err)

			t.Log("Checking output")
			output, err := io.ReadAll(outputBuf)
			require.NoError(t, err)
			require.Containsf(t, string(output), tc.expOutput, "unexpected stdout:\n\n%s", string(output))
		})
	}
}
```

## File: `cmd/bbolt/command/command_check.go`
```go
package command

import (
	"fmt"

	"github.com/spf13/cobra"
	"github.com/spf13/pflag"

	bolt "go.etcd.io/bbolt"
	"go.etcd.io/bbolt/internal/guts_cli"
)

type checkOptions struct {
	fromPageID uint64
}

func (o *checkOptions) AddFlags(fs *pflag.FlagSet) {
	fs.Uint64VarP(&o.fromPageID, "from-page", "", o.fromPageID, "check db integrity starting from the given page ID")
}

func newCheckCommand() *cobra.Command {
	var o checkOptions
	checkCmd := &cobra.Command{
		Use:   "check <bbolt-file>",
		Short: "verify integrity of bbolt database data",
		Args:  cobra.ExactArgs(1),
		RunE: func(cmd *cobra.Command, args []string) error {
			return checkFunc(cmd, args[0], o)
		},
	}

	o.AddFlags(checkCmd.Flags())
	return checkCmd
}

func checkFunc(cmd *cobra.Command, dbPath string, cfg checkOptions) error {
	if _, err := checkSourceDBPath(dbPath); err != nil {
		return err
	}

	// Open database.
	db, err := bolt.Open(dbPath, 0600, &bolt.Options{
		ReadOnly:        true,
		PreLoadFreelist: true,
	})
	if err != nil {
		return err
	}
	defer db.Close()

	opts := []bolt.CheckOption{bolt.WithKVStringer(CmdKvStringer())}
	if cfg.fromPageID != 0 {
		opts = append(opts, bolt.WithPageId(cfg.fromPageID))
	}
	// Perform consistency check.
	return db.View(func(tx *bolt.Tx) error {
		var count int
		for err := range tx.Check(opts...) {
			fmt.Fprintln(cmd.OutOrStdout(), err)
			count++
		}

		// Print summary of errors.
		if count > 0 {
			fmt.Fprintf(cmd.OutOrStdout(), "%d errors found\n", count)
			return guts_cli.ErrCorrupt
		}

		// Notify user that database is valid.
		fmt.Fprintln(cmd.OutOrStdout(), "OK")
		return nil
	})
}
```

## File: `cmd/bbolt/command/command_check_test.go`
```go
package command_test

import (
	"bytes"
	"io"
	"testing"

	"github.com/stretchr/testify/require"

	"go.etcd.io/bbolt/cmd/bbolt/command"
	"go.etcd.io/bbolt/internal/btesting"
	"go.etcd.io/bbolt/internal/guts_cli"
)

func TestCheckCommand_Run(t *testing.T) {
	testCases := []struct {
		name      string
		args      []string
		expErr    error
		expOutput string
	}{
		{
			name:      "check whole db",
			args:      []string{"check", "path"},
			expErr:    nil,
			expOutput: "OK\n",
		},
		{
			name:      "check valid pageId",
			args:      []string{"check", "path", "--from-page", "3"},
			expErr:    nil,
			expOutput: "OK\n",
		},
		{
			name:      "check invalid pageId",
			args:      []string{"check", "path", "--from-page", "1"},
			expErr:    guts_cli.ErrCorrupt,
			expOutput: "page ID (1) out of range [2, 4)",
		},
	}

	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {

			t.Log("Creating sample DB")
			db := btesting.MustCreateDB(t)
			db.Close()
			defer requireDBNoChange(t, dbData(t, db.Path()), db.Path())

			t.Log("Running check cmd")
			rootCmd := command.NewRootCommand()
			outputBuf := bytes.NewBufferString("") // capture output for assertion
			rootCmd.SetOut(outputBuf)

			tc.args[1] = db.Path() // path to be replaced with db.Path()
			rootCmd.SetArgs(tc.args)
			err := rootCmd.Execute()
			require.Equal(t, tc.expErr, err)

			t.Log("Checking output")
			output, err := io.ReadAll(outputBuf)
			require.NoError(t, err)
			require.Containsf(t, string(output), tc.expOutput, "unexpected stdout:\n\n%s", string(output))
		})
	}
}
```

## File: `cmd/bbolt/command/command_compact.go`
```go
package command

import (
	"errors"
	"fmt"
	"os"

	"github.com/spf13/cobra"
	"github.com/spf13/pflag"

	bolt "go.etcd.io/bbolt"
)

type compactOptions struct {
	dstPath   string
	txMaxSize int64
	dstNoSync bool
}

func newCompactCommand() *cobra.Command {
	var o compactOptions
	var compactCmd = &cobra.Command{
		Use:   "compact [options] -o <dst-bbolt-file> <src-bbolt-file>",
		Short: "creates a compacted copy of the database from source path to the destination path, preserving the original.",
		Long: `compact opens a database at source path and walks it recursively, copying keys
as they are found from all buckets, to a newly created database at the destination path.
The original database is left untouched.`,
		Args: cobra.MinimumNArgs(1),
		RunE: func(cmd *cobra.Command, args []string) error {
			if err := o.Validate(args[0]); err != nil {
				return err
			}
			return o.Run(cmd, args[0])
		},
	}
	o.AddFlags(compactCmd.Flags())

	return compactCmd
}

func (o *compactOptions) AddFlags(fs *pflag.FlagSet) {
	fs.StringVarP(&o.dstPath, "output", "o", "", "")
	fs.Int64Var(&o.txMaxSize, "tx-max-size", 65536, "")
	fs.BoolVar(&o.dstNoSync, "no-sync", false, "")
	_ = cobra.MarkFlagRequired(fs, "output")
}

func (o *compactOptions) Validate(srcPath string) (err error) {
	if o.dstPath == "" {
		return errors.New("output file required")
	}

	return
}

func (o *compactOptions) Run(cmd *cobra.Command, srcPath string) (err error) {

	// ensure source file exists.
	fi, err := checkSourceDBPath(srcPath)
	if err != nil {
		return err
	}
	initialSize := fi.Size()

	// open source database.
	src, err := bolt.Open(srcPath, 0400, &bolt.Options{ReadOnly: true})
	if err != nil {
		return err
	}
	defer src.Close()

	// open destination database.
	dst, err := bolt.Open(o.dstPath, fi.Mode(), &bolt.Options{NoSync: o.dstNoSync})
	if err != nil {
		return err
	}
	defer dst.Close()

	// run compaction.
	if err := bolt.Compact(dst, src, o.txMaxSize); err != nil {
		return err
	}

	// report stats on new size.
	fi, err = os.Stat(o.dstPath)
	if err != nil {
		return err
	} else if fi.Size() == 0 {
		return fmt.Errorf("zero db size")
	}
	fmt.Fprintf(cmd.OutOrStdout(), "%d -> %d bytes (gain=%.2fx)\n", initialSize, fi.Size(), float64(initialSize)/float64(fi.Size()))

	return
}
```

## File: `cmd/bbolt/command/command_compact_test.go`
```go
package command_test

import (
	crypto "crypto/rand"
	"errors"
	"fmt"
	"math/rand"
	"testing"

	"github.com/stretchr/testify/require"

	bolt "go.etcd.io/bbolt"
	"go.etcd.io/bbolt/cmd/bbolt/command"
	"go.etcd.io/bbolt/internal/btesting"
)

// Ensure the "compact" command can print a list of buckets.
func TestCompactCommand_Run(t *testing.T) {
	dstdb := btesting.MustCreateDB(t)
	dstdb.Close()

	t.Log("Creating sample DB")
	db := btesting.MustCreateDB(t)
	if err := db.Update(func(tx *bolt.Tx) error {
		n := 2 + rand.Intn(5)
		for i := 0; i < n; i++ {
			k := []byte(fmt.Sprintf("b%d", i))
			b, err := tx.CreateBucketIfNotExists(k)
			if err != nil {
				return err
			}
			if err := b.SetSequence(uint64(i)); err != nil {
				return err
			}
			if err := fillBucket(b, append(k, '.')); err != nil {
				return err
			}
		}
		return nil
	}); err != nil {
		t.Fatal(err)
	}

	// make the db grow by adding large values, and delete them.
	if err := db.Update(func(tx *bolt.Tx) error {
		b, err := tx.CreateBucketIfNotExists([]byte("large_vals"))
		if err != nil {
			return err
		}
		n := 5 + rand.Intn(5)
		for i := 0; i < n; i++ {
			v := make([]byte, 1000*1000*(1+rand.Intn(5)))
			_, err := crypto.Read(v)
			if err != nil {
				return err
			}
			if err := b.Put([]byte(fmt.Sprintf("l%d", i)), v); err != nil {
				return err
			}
		}
		return nil
	}); err != nil {
		t.Fatal(err)
	}
	if err := db.Update(func(tx *bolt.Tx) error {
		c := tx.Bucket([]byte("large_vals")).Cursor()
		for k, _ := c.First(); k != nil; k, _ = c.Next() {
			if err := c.Delete(); err != nil {
				return err
			}
		}
		return tx.DeleteBucket([]byte("large_vals"))
	}); err != nil {
		t.Fatal(err)
	}
	db.Close()
	dbChk, err := chkdb(db.Path())
	require.NoError(t, err)

	t.Log("Running compact cmd")
	rootCmd := command.NewRootCommand()
	rootCmd.SetArgs([]string{"compact", "-o", dstdb.Path(), db.Path()})
	err = rootCmd.Execute()
	require.NoError(t, err)

	t.Log("Checking output")
	dbChkAfterCompact, err := chkdb(db.Path())
	require.NoError(t, err)
	dstdbChk, err := chkdb(dstdb.Path())
	require.NoError(t, err)
	require.Equal(t, dbChk, dbChkAfterCompact, "the original db has been touched")
	require.Equal(t, dbChk, dstdbChk, "the compacted db data isn't the same than the original db")
}

func TestCompactCommand_NoArgs(t *testing.T) {
	expErr := errors.New("requires at least 1 arg(s), only received 0")
	rootCmd := command.NewRootCommand()
	rootCmd.SetArgs([]string{"compact"})
	err := rootCmd.Execute()
	require.ErrorContains(t, err, expErr.Error())
}
```

## File: `cmd/bbolt/command/command_dump.go`
```go
package command

import (
	"bytes"
	"fmt"
	"io"
	"os"

	"github.com/spf13/cobra"

	"go.etcd.io/bbolt/internal/guts_cli"
)

func newDumpCommand() *cobra.Command {
	dumpCmd := &cobra.Command{
		Use:   "dump <bbolt-file> pageid [pageid...]",
		Short: "prints a hexadecimal dump of one or more pages of bbolt database.",
		Args:  cobra.MinimumNArgs(2),
		RunE: func(cmd *cobra.Command, args []string) error {
			dbPath := args[0]
			pageIDs, err := stringToPages(args[1:])
			if err != nil {
				return err
			} else if len(pageIDs) == 0 {
				return ErrPageIDRequired
			}
			return dumpFunc(cmd, dbPath, pageIDs)
		},
	}

	return dumpCmd
}

func dumpFunc(cmd *cobra.Command, dbPath string, pageIDs []uint64) (err error) {
	if _, err := checkSourceDBPath(dbPath); err != nil {
		return err
	}

	// open database to retrieve page size.
	pageSize, _, err := guts_cli.ReadPageAndHWMSize(dbPath)
	if err != nil {
		return err
	}

	// open database file handler.
	f, err := os.Open(dbPath)
	if err != nil {
		return err
	}
	defer func() { _ = f.Close() }()

	// print each page listed.
	for i, pageID := range pageIDs {
		// print a separator.
		if i > 0 {
			fmt.Fprintln(cmd.OutOrStdout(), "===============================================")
		}

		// print page to stdout.
		if err := dumpPage(cmd.OutOrStdout(), f, pageID, uint64(pageSize)); err != nil {
			return err
		}
	}

	return
}

func dumpPage(w io.Writer, r io.ReaderAt, pageID uint64, pageSize uint64) error {
	const bytesPerLineN = 16

	// read page into buffer.
	buf := make([]byte, pageSize)
	addr := pageID * uint64(pageSize)
	if n, err := r.ReadAt(buf, int64(addr)); err != nil {
		return err
	} else if uint64(n) != pageSize {
		return io.ErrUnexpectedEOF
	}

	// write out to writer in 16-byte lines.
	var prev []byte
	var skipped bool
	for offset := uint64(0); offset < pageSize; offset += bytesPerLineN {
		// retrieve current 16-byte line.
		line := buf[offset : offset+bytesPerLineN]
		isLastLine := (offset == (pageSize - bytesPerLineN))

		// if it's the same as the previous line then print a skip.
		if bytes.Equal(line, prev) && !isLastLine {
			if !skipped {
				fmt.Fprintf(w, "%07x *\n", addr+offset)
				skipped = true
			}
		} else {
			// print line as hexadecimal in 2-byte groups.
			fmt.Fprintf(w, "%07x %04x %04x %04x %04x %04x %04x %04x %04x\n", addr+offset,
				line[0:2], line[2:4], line[4:6], line[6:8],
				line[8:10], line[10:12], line[12:14], line[14:16],
			)

			skipped = false
		}

		// save the previous line.
		prev = line
	}
	fmt.Fprint(w, "\n")

	return nil
}
```

## File: `cmd/bbolt/command/command_dump_test.go`
```go
package command_test

import (
	"bytes"
	"errors"
	"io"
	"strings"
	"testing"

	"github.com/stretchr/testify/require"

	bolt "go.etcd.io/bbolt"
	"go.etcd.io/bbolt/cmd/bbolt/command"
	"go.etcd.io/bbolt/internal/btesting"
)

func TestDumpCommand_Run(t *testing.T) {
	t.Log("Creating database")
	db := btesting.MustCreateDBWithOption(t, &bolt.Options{PageSize: 4096})
	require.NoError(t, db.Close())
	defer requireDBNoChange(t, dbData(t, db.Path()), db.Path())

	t.Log("Running dump command")
	rootCmd := command.NewRootCommand()
	outputBuf := bytes.NewBufferString("")
	rootCmd.SetOut(outputBuf)
	rootCmd.SetArgs([]string{"dump", db.Path(), "0"})
	err := rootCmd.Execute()
	require.NoError(t, err)

	t.Log("Checking output")
	exp := `0000010 edda 0ced 0200 0000 0010 0000 0000 0000`
	output, err := io.ReadAll(outputBuf)
	require.NoError(t, err)
	require.True(t, strings.Contains(string(output), exp), "unexpected stdout:", string(output))
}

func TestDumpCommand_NoArgs(t *testing.T) {
	expErr := errors.New("requires at least 2 arg(s), only received 0")
	rootCmd := command.NewRootCommand()
	rootCmd.SetArgs([]string{"dump"})
	err := rootCmd.Execute()
	require.ErrorContains(t, err, expErr.Error())
}
```

## File: `cmd/bbolt/command/command_get.go`
```go
package command

import (
	"fmt"

	"github.com/spf13/cobra"
	"github.com/spf13/pflag"

	bolt "go.etcd.io/bbolt"
	"go.etcd.io/bbolt/errors"
)

type getOptions struct {
	parseFormat string
	format      string
}

func newGetCommand() *cobra.Command {
	var opts getOptions

	cmd := &cobra.Command{
		Use:   "get PATH [BUCKET..] KEY",
		Short: "get the value of a key from a (sub)bucket in a bbolt database",
		Args:  cobra.MinimumNArgs(3),
		RunE: func(cmd *cobra.Command, args []string) error {
			path := args[0]
			if path == "" {
				return ErrPathRequired
			}

			buckets := args[1 : len(args)-1]
			keyStr := args[len(args)-1]

			// validate input parameters
			if len(buckets) == 0 {
				return fmt.Errorf("bucket is required: %w", ErrBucketRequired)
			}

			key, err := parseBytes(keyStr, opts.parseFormat)
			if err != nil {
				return err
			}

			if len(key) == 0 {
				return fmt.Errorf("key is required: %w", errors.ErrKeyRequired)
			}

			return getFunc(cmd, path, buckets, key, opts)
		},
	}
	opts.AddFlags(cmd.Flags())

	return cmd
}

func (o *getOptions) AddFlags(fs *pflag.FlagSet) {
	fs.StringVar(&o.parseFormat, "parse-format", "ascii-encoded", "Input format one of: ascii-encoded|hex")
	fs.StringVar(&o.format, "format", "auto", "Output format one of: "+FORMAT_MODES+" (default: auto)")
}

// getFunc opens the given bbolt db file and retrieves the key value from the bucket path.
func getFunc(cmd *cobra.Command, path string, buckets []string, key []byte, opts getOptions) error {
	// check if the source DB path is valid
	if _, err := checkSourceDBPath(path); err != nil {
		return err
	}

	// open the database
	db, err := bolt.Open(path, 0600, &bolt.Options{ReadOnly: true})
	if err != nil {
		return err
	}
	defer db.Close()

	// access the database and get the value
	return db.View(func(tx *bolt.Tx) error {
		lastBucket, err := findLastBucket(tx, buckets)
		if err != nil {
			return err
		}
		val := lastBucket.Get(key)
		if val == nil {
			return fmt.Errorf("Error %w for key: %q hex: \"%x\"", ErrKeyNotFound, key, string(key))
		}
		return writelnBytes(cmd.OutOrStdout(), val, opts.format)
	})
}
```

## File: `cmd/bbolt/command/command_get_test.go`
```go
package command_test

import (
	"bytes"
	"encoding/hex"
	"errors"
	"fmt"
	"io"
	"testing"

	"github.com/stretchr/testify/require"

	bolt "go.etcd.io/bbolt"
	"go.etcd.io/bbolt/cmd/bbolt/command"
	"go.etcd.io/bbolt/internal/btesting"
)

func TestGetCommand_Run(t *testing.T) {
	testCases := []struct {
		name          string
		printable     bool
		testBucket    string
		testKey       string
		expectedValue string
	}{
		{
			name:          "printable data",
			printable:     true,
			testBucket:    "foo",
			testKey:       "foo-1",
			expectedValue: "value-foo-1\n",
		},
		{
			name:          "non printable data",
			printable:     false,
			testBucket:    "bar",
			testKey:       "100001",
			expectedValue: hex.EncodeToString(convertInt64IntoBytes(100001)) + "\n",
		},
	}

	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			t.Logf("Creating test database for subtest '%s'", tc.name)
			db := btesting.MustCreateDB(t)

			t.Log("Inserting test data")
			err := db.Update(func(tx *bolt.Tx) error {
				b, err := tx.CreateBucketIfNotExists([]byte(tc.testBucket))
				if err != nil {
					return fmt.Errorf("create bucket %q: %w", tc.testBucket, err)
				}

				if tc.printable {
					return b.Put([]byte(tc.testKey), []byte("value-"+tc.testKey))
				}

				return b.Put([]byte(tc.testKey), convertInt64IntoBytes(100001))
			})
			require.NoError(t, err)
			db.Close()
			defer requireDBNoChange(t, dbData(t, db.Path()), db.Path())

			t.Log("Running get command")
			rootCmd := command.NewRootCommand()
			outputBuf := bytes.NewBufferString("")
			rootCmd.SetOut(outputBuf)
			rootCmd.SetArgs([]string{"get", db.Path(), tc.testBucket, tc.testKey})
			err = rootCmd.Execute()
			require.NoError(t, err)

			t.Log("Checking output")
			output, err := io.ReadAll(outputBuf)
			require.NoError(t, err)
			require.Equalf(t, tc.expectedValue, string(output), "unexpected stdout:\n\n%s", string(output))
		})
	}
}

func TestGetCommand_NoArgs(t *testing.T) {
	expErr := errors.New("requires at least 3 arg(s), only received 0")
	rootCmd := command.NewRootCommand()
	rootCmd.SetArgs([]string{"get"})
	err := rootCmd.Execute()
	require.ErrorContains(t, err, expErr.Error())
}
```

## File: `cmd/bbolt/command/command_info.go`
```go
package command

import (
	"fmt"

	"github.com/spf13/cobra"

	bolt "go.etcd.io/bbolt"
)

func newInfoCommand() *cobra.Command {
	infoCmd := &cobra.Command{
		Use:   "info <bbolt-file>",
		Short: "prints basic information about the bbolt database.",
		Args:  cobra.ExactArgs(1),
		RunE: func(cmd *cobra.Command, args []string) error {
			return infoFunc(cmd, args[0])
		},
	}

	return infoCmd
}

func infoFunc(cmd *cobra.Command, dbPath string) error {
	if _, err := checkSourceDBPath(dbPath); err != nil {
		return err
	}

	// Open database.
	db, err := bolt.Open(dbPath, 0600, &bolt.Options{
		ReadOnly: true,
	})
	if err != nil {
		return err
	}
	defer db.Close()

	// Print basic database info.
	info := db.Info()
	fmt.Fprintf(cmd.OutOrStdout(), "Page Size: %d\n", info.PageSize)

	return nil
}
```

## File: `cmd/bbolt/command/command_info_test.go`
```go
package command_test

import (
	"bytes"
	"errors"
	"io"
	"testing"

	"github.com/stretchr/testify/require"

	"go.etcd.io/bbolt/cmd/bbolt/command"
	"go.etcd.io/bbolt/internal/btesting"
)

// Ensure the "info" command can print information about a database.
func TestInfoCommand_Run(t *testing.T) {
	t.Log("Creating sample DB")
	db := btesting.MustCreateDB(t)
	db.Close()
	defer requireDBNoChange(t, dbData(t, db.Path()), db.Path())

	t.Log("Running info cmd")
	rootCmd := command.NewRootCommand()
	outputBuf := bytes.NewBufferString("")
	rootCmd.SetOut(outputBuf)

	rootCmd.SetArgs([]string{"info", db.Path()})
	err := rootCmd.Execute()
	require.NoError(t, err)

	t.Log("Checking output")
	_, err = io.ReadAll(outputBuf)
	require.NoError(t, err)
}

func TestInfoCommand_NoArgs(t *testing.T) {
	expErr := errors.New("accepts 1 arg(s), received 0")
	rootCmd := command.NewRootCommand()
	rootCmd.SetArgs([]string{"info"})
	err := rootCmd.Execute()
	require.ErrorContains(t, err, expErr.Error())
}
```

## File: `cmd/bbolt/command/command_inspect.go`
```go
package command

import (
	"encoding/json"
	"fmt"
	"os"

	"github.com/spf13/cobra"

	bolt "go.etcd.io/bbolt"
)

func newInspectCommand() *cobra.Command {
	inspectCmd := &cobra.Command{
		Use:   "inspect <bbolt-file>",
		Short: "inspect the structure of the database",
		Args:  cobra.ExactArgs(1),
		RunE: func(cmd *cobra.Command, args []string) error {
			return inspectFunc(args[0])
		},
	}

	return inspectCmd
}

func inspectFunc(srcDBPath string) error {
	if _, err := checkSourceDBPath(srcDBPath); err != nil {
		return err
	}

	db, err := bolt.Open(srcDBPath, 0600, &bolt.Options{ReadOnly: true})
	if err != nil {
		return err
	}
	defer db.Close()

	return db.View(func(tx *bolt.Tx) error {
		bs := tx.Inspect()
		out, err := json.MarshalIndent(bs, "", "    ")
		if err != nil {
			return err
		}
		fmt.Fprintln(os.Stdout, string(out))
		return nil
	})
}
```

## File: `cmd/bbolt/command/command_inspect_test.go`
```go
package command_test

import (
	"testing"

	"github.com/stretchr/testify/require"

	bolt "go.etcd.io/bbolt"
	"go.etcd.io/bbolt/cmd/bbolt/command"
	"go.etcd.io/bbolt/internal/btesting"
)

func TestInspect(t *testing.T) {
	pageSize := 4096
	db := btesting.MustCreateDBWithOption(t, &bolt.Options{PageSize: pageSize})
	srcPath := db.Path()
	db.Close()

	defer requireDBNoChange(t, dbData(t, db.Path()), db.Path())

	rootCmd := command.NewRootCommand()
	rootCmd.SetArgs([]string{
		"inspect", srcPath,
	})
	err := rootCmd.Execute()
	require.NoError(t, err)
}
```

## File: `cmd/bbolt/command/command_keys.go`
```go
package command

import (
	"github.com/spf13/cobra"
	"github.com/spf13/pflag"

	bolt "go.etcd.io/bbolt"
)

type keysOptions struct {
	format string
}

func (o *keysOptions) AddFlags(fs *pflag.FlagSet) {
	fs.StringVarP(&o.format, "format", "f", "auto", "Output format one of: "+FORMAT_MODES)
}

func newKeysCommand() *cobra.Command {
	var o keysOptions

	keysCmd := &cobra.Command{
		Use:   "keys <bbolt-file> <buckets>",
		Short: "print a list of keys in the given (sub)bucket in bbolt database",
		Args:  cobra.MinimumNArgs(2),
		RunE: func(cmd *cobra.Command, args []string) error {
			return keysFunc(cmd, o, args[0], args[1:]...)
		},
	}

	o.AddFlags(keysCmd.Flags())
	return keysCmd
}

func keysFunc(cmd *cobra.Command, cfg keysOptions, dbPath string, buckets ...string) error {
	if _, err := checkSourceDBPath(dbPath); err != nil {
		return err
	}
	// Open database.
	db, err := bolt.Open(dbPath, 0600, &bolt.Options{
		ReadOnly: true,
	})
	if err != nil {
		return err
	}
	defer db.Close()

	// Print keys.
	return db.View(func(tx *bolt.Tx) error {
		// Find bucket.
		lastBucket, err := findLastBucket(tx, buckets)
		if err != nil {
			return err
		}

		// Iterate over each key.
		return lastBucket.ForEach(func(key, _ []byte) error {
			return writelnBytes(cmd.OutOrStdout(), key, cfg.format)
		})
	})
}
```

## File: `cmd/bbolt/command/command_keys_test.go`
```go
package command_test

import (
	"bytes"
	"errors"
	"fmt"
	"io"
	"testing"

	"github.com/stretchr/testify/require"

	bolt "go.etcd.io/bbolt"
	"go.etcd.io/bbolt/cmd/bbolt/command"
	"go.etcd.io/bbolt/internal/btesting"
)

// Ensure the "keys" command can print a list of keys for a bucket.
func TestKeysCommand_Run(t *testing.T) {
	testCases := []struct {
		name       string
		printable  bool
		testBucket string
		expected   string
	}{
		{
			name:       "printable keys",
			printable:  true,
			testBucket: "foo",
			expected:   "foo-0\nfoo-1\nfoo-2\n",
		},
		{
			name:       "non printable keys",
			printable:  false,
			testBucket: "bar",
			expected:   convertInt64KeysIntoHexString(100001, 100002, 100003),
		},
	}

	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			t.Logf("Creating test database for subtest '%s'", tc.name)
			db := btesting.MustCreateDB(t)
			err := db.Update(func(tx *bolt.Tx) error {
				t.Logf("creating test bucket %s", tc.testBucket)
				b, bErr := tx.CreateBucketIfNotExists([]byte(tc.testBucket))
				if bErr != nil {
					return fmt.Errorf("error creating test bucket %q: %v", tc.testBucket, bErr)
				}

				t.Logf("inserting test data into test bucket %s", tc.testBucket)
				if tc.printable {
					for i := 0; i < 3; i++ {
						key := fmt.Sprintf("%s-%d", tc.testBucket, i)
						if pErr := b.Put([]byte(key), []byte{0}); pErr != nil {
							return pErr
						}
					}
				} else {
					for i := 100001; i < 100004; i++ {
						k := convertInt64IntoBytes(int64(i))
						if pErr := b.Put(k, []byte{0}); pErr != nil {
							return pErr
						}
					}
				}
				return nil
			})
			require.NoError(t, err)
			db.Close()
			defer requireDBNoChange(t, dbData(t, db.Path()), db.Path())

			t.Log("Running Keys cmd")
			rootCmd := command.NewRootCommand()
			outputBuf := bytes.NewBufferString("")
			rootCmd.SetOut(outputBuf)
			rootCmd.SetArgs([]string{"keys", db.Path(), tc.testBucket})
			err = rootCmd.Execute()
			require.NoError(t, err)

			t.Log("Checking output")
			output, err := io.ReadAll(outputBuf)
			require.NoError(t, err)
			require.Equalf(t, tc.expected, string(output), "unexpected stdout:\n\n%s", string(output))
		})
	}
}

func TestKeyCommand_NoArgs(t *testing.T) {
	expErr := errors.New("requires at least 2 arg(s), only received 0")
	rootCmd := command.NewRootCommand()
	rootCmd.SetArgs([]string{"keys"})
	err := rootCmd.Execute()
	require.ErrorContains(t, err, expErr.Error())
}
```

## File: `cmd/bbolt/command/command_page.go`
```go
package command

import (
	"fmt"
	"io"

	"github.com/spf13/cobra"
	"github.com/spf13/pflag"

	"go.etcd.io/bbolt/internal/common"
	"go.etcd.io/bbolt/internal/guts_cli"
)

type getPageOptions struct {
	all    bool
	format string
}

func newPageCommand() *cobra.Command {
	var opt getPageOptions
	pageCmd := &cobra.Command{
		Use:   "page <bbolt-file> [pageid...]",
		Short: "page prints one or more pages in human readable format.",
		Args:  cobra.MinimumNArgs(1),
		RunE: func(cmd *cobra.Command, args []string) error {
			dbPath := args[0]
			pageIDs, err := stringToPages(args[1:])
			if err != nil {
				return err
			}
			if len(pageIDs) == 0 && !opt.all {
				return ErrPageIDRequired
			}
			return pageFunc(cmd, opt, dbPath, pageIDs)
		},
	}
	opt.AddFlags(pageCmd.Flags())

	return pageCmd
}

func (o *getPageOptions) AddFlags(fs *pflag.FlagSet) {
	fs.BoolVar(&o.all, "all", false, "List all pages.")
	fs.StringVar(&o.format, "format-value", "auto", "Output format one of: "+FORMAT_MODES+". Applies to values on the leaf page.")
}

func pageFunc(cmd *cobra.Command, cfg getPageOptions, dbPath string, pageIDs []uint64) (err error) {
	if cfg.all && len(pageIDs) != 0 {
		return ErrInvalidPageArgs
	}

	if _, err := checkSourceDBPath(dbPath); err != nil {
		return err
	}

	if cfg.all {
		printAllPages(cmd, dbPath, cfg.format)
	} else {
		printPages(cmd, pageIDs, dbPath, cfg.format)
	}

	return
}

func printPages(cmd *cobra.Command, pageIDs []uint64, path string, formatValue string) {
	// print each page listed.
	for i, pageID := range pageIDs {
		// print a separator.
		if i > 0 {
			fmt.Fprintln(cmd.OutOrStdout(), "===============================================")
		}
		_, pErr := printPage(cmd, path, pageID, formatValue)
		if pErr != nil {
			fmt.Fprintf(cmd.OutOrStdout(), "Prining page %d failed: %s. Continuing...\n", pageID, pErr)
		}
	}
}

// printPage prints given page to cmd.Stdout and returns error or number of interpreted pages.
func printPage(cmd *cobra.Command, path string, pageID uint64, formatValue string) (numPages uint32, reterr error) {
	defer func() {
		if err := recover(); err != nil {
			reterr = fmt.Errorf("%s", err)
		}
	}()

	// retrieve page info and page size.
	p, buf, err := guts_cli.ReadPage(path, pageID)
	if err != nil {
		return 0, err
	}

	// print basic page info.
	stdout := cmd.OutOrStdout()
	fmt.Fprintf(stdout, "Page ID:    %d\n", p.Id())
	fmt.Fprintf(stdout, "Page Type:  %s\n", p.Typ())
	fmt.Fprintf(stdout, "Total Size: %d bytes\n", len(buf))
	fmt.Fprintf(stdout, "Overflow pages: %d\n", p.Overflow())

	// print type-specific data.
	switch p.Typ() {
	case "meta":
		err = pagePrintMeta(stdout, buf)
	case "leaf":
		err = pagePrintLeaf(stdout, buf, formatValue)
	case "branch":
		err = pagePrintBranch(stdout, buf)
	case "freelist":
		err = pagePrintFreelist(stdout, buf)
	}
	if err != nil {
		return 0, err
	}
	return p.Overflow(), nil
}

func printAllPages(cmd *cobra.Command, path string, formatValue string) {
	_, hwm, err := guts_cli.ReadPageAndHWMSize(path)
	if err != nil {
		fmt.Fprintf(cmd.OutOrStdout(), "cannot read number of pages: %v", err)
	}

	// print each page listed.
	for pageID := uint64(0); pageID < uint64(hwm); {
		// print a separator.
		if pageID > 0 {
			fmt.Fprintln(cmd.OutOrStdout(), "===============================================")
		}
		overflow, pErr := printPage(cmd, path, pageID, formatValue)
		if pErr != nil {
			fmt.Fprintf(cmd.OutOrStdout(), "Prining page %d failed: %s. Continuing...\n", pageID, pErr)
			pageID++
		} else {
			pageID += uint64(overflow) + 1
		}
	}
}

// pagePrintMeta prints the data from the meta page.
func pagePrintMeta(w io.Writer, buf []byte) error {
	m := common.LoadPageMeta(buf)
	m.Print(w)
	return nil
}

// pagePrintLeaf prints the data for a leaf page.
func pagePrintLeaf(w io.Writer, buf []byte, formatValue string) error {
	p := common.LoadPage(buf)

	// print number of items.
	fmt.Fprintf(w, "Item Count: %d\n", p.Count())
	fmt.Fprintf(w, "\n")

	// print each key/value.
	for i := uint16(0); i < p.Count(); i++ {
		e := p.LeafPageElement(i)

		// format key as string.
		var k string
		if isPrintable(string(e.Key())) {
			k = fmt.Sprintf("%q", string(e.Key()))
		} else {
			k = fmt.Sprintf("%x", string(e.Key()))
		}

		// format value as string.
		var v string
		var err error
		if e.IsBucketEntry() {
			b := e.Bucket()
			v = b.String()
		} else {
			v, err = formatBytes(e.Value(), formatValue)
			if err != nil {
				return err
			}
		}

		fmt.Fprintf(w, "%s: %s\n", k, v)
	}
	fmt.Fprintf(w, "\n")
	return nil
}

// pagePrintBranch prints the data for a leaf page.
func pagePrintBranch(w io.Writer, buf []byte) error {
	p := common.LoadPage(buf)

	// print number of items.
	fmt.Fprintf(w, "Item Count: %d\n", p.Count())
	fmt.Fprintf(w, "\n")

	// print each key/value.
	for i := uint16(0); i < p.Count(); i++ {
		e := p.BranchPageElement(i)

		// format key as string.
		var k string
		if isPrintable(string(e.Key())) {
			k = fmt.Sprintf("%q", string(e.Key()))
		} else {
			k = fmt.Sprintf("%x", string(e.Key()))
		}

		fmt.Fprintf(w, "%s: <pgid=%d>\n", k, e.Pgid())
	}
	fmt.Fprintf(w, "\n")
	return nil
}

// pagePrintFreelist prints the data for a freelist page.
func pagePrintFreelist(w io.Writer, buf []byte) error {
	p := common.LoadPage(buf)

	// print number of items.
	_, cnt := p.FreelistPageCount()
	fmt.Fprintf(w, "Item Count: %d\n", cnt)
	fmt.Fprintf(w, "Overflow: %d\n", p.Overflow())

	fmt.Fprintf(w, "\n")

	// print each page in the freelist.
	ids := p.FreelistPageIds()
	for _, ids := range ids {
		fmt.Fprintf(w, "%d\n", ids)
	}
	fmt.Fprintf(w, "\n")
	return nil
}
```

## File: `cmd/bbolt/command/command_page_item.go`
```go
package command

import (
	"errors"
	"fmt"
	"io"
	"strconv"

	"github.com/spf13/cobra"
	"github.com/spf13/pflag"

	"go.etcd.io/bbolt/internal/common"
	"go.etcd.io/bbolt/internal/guts_cli"
)

type pageItemOptions struct {
	keyOnly   bool
	valueOnly bool
	format    string
}

func newPageItemCommand() *cobra.Command {
	var opt pageItemOptions
	pageItemCmd := &cobra.Command{
		Use:   "page-item [options] <bbolt-file> pageid itemid",
		Short: "print a page item key and value in a bbolt database",
		Args:  cobra.ExactArgs(3),
		RunE: func(cmd *cobra.Command, args []string) error {
			dbPath := args[0]
			pageID, err := strconv.ParseUint(args[1], 10, 64)
			if err != nil {
				return err
			}
			itemID, err := strconv.ParseUint(args[2], 10, 64)
			if err != nil {
				return err
			}
			return pageItemFunc(cmd, opt, dbPath, pageID, itemID)
		},
	}
	opt.AddFlags(pageItemCmd.Flags())

	return pageItemCmd
}

func (o *pageItemOptions) AddFlags(fs *pflag.FlagSet) {
	fs.BoolVar(&o.keyOnly, "key-only", false, "Print only the key")
	fs.BoolVar(&o.valueOnly, "value-only", false, "Print only the value")
	fs.StringVar(&o.format, "format", "auto", "Output format one of: "+FORMAT_MODES)
}

func pageItemFunc(cmd *cobra.Command, cfg pageItemOptions, dbPath string, pageID, itemID uint64) (err error) {
	if cfg.keyOnly && cfg.valueOnly {
		return errors.New("the --key-only or --value-only flag may be set, but not both")
	}

	if _, err := checkSourceDBPath(dbPath); err != nil {
		return err
	}

	// retrieve page info and page size.
	_, buf, err := guts_cli.ReadPage(dbPath, pageID)
	if err != nil {
		return err
	}

	if !cfg.valueOnly {
		err := pageItemPrintLeafItemKey(cmd.OutOrStdout(), buf, uint16(itemID), cfg.format)
		if err != nil {
			return err
		}
	}
	if !cfg.keyOnly {
		err := pageItemPrintLeafItemValue(cmd.OutOrStdout(), buf, uint16(itemID), cfg.format)
		if err != nil {
			return err
		}
	}

	return
}

func pageItemPrintLeafItemKey(w io.Writer, pageBytes []byte, index uint16, format string) error {
	k, _, err := pageItemLeafPageElement(pageBytes, index)
	if err != nil {
		return err
	}

	return writelnBytes(w, k, format)
}

func pageItemPrintLeafItemValue(w io.Writer, pageBytes []byte, index uint16, format string) error {
	_, v, err := pageItemLeafPageElement(pageBytes, index)
	if err != nil {
		return err
	}
	return writelnBytes(w, v, format)
}

func pageItemLeafPageElement(pageBytes []byte, index uint16) ([]byte, []byte, error) {
	p := common.LoadPage(pageBytes)
	if index >= p.Count() {
		return nil, nil, fmt.Errorf("leafPageElement: expected item index less than %d, but got %d", p.Count(), index)
	}
	if p.Typ() != "leaf" {
		return nil, nil, fmt.Errorf("leafPageElement: expected page type of 'leaf', but got '%s'", p.Typ())
	}

	e := p.LeafPageElement(index)
	return e.Key(), e.Value(), nil
}
```

## File: `cmd/bbolt/command/command_page_item_test.go`
```go
package command_test

import (
	"bytes"
	"encoding/hex"
	"errors"
	"fmt"
	"strings"
	"testing"

	"github.com/stretchr/testify/require"

	bolt "go.etcd.io/bbolt"
	"go.etcd.io/bbolt/cmd/bbolt/command"
	"go.etcd.io/bbolt/internal/btesting"
	"go.etcd.io/bbolt/internal/guts_cli"
)

func TestPageItemCommand_Run(t *testing.T) {
	testCases := []struct {
		name          string
		printable     bool
		itemId        string
		expectedKey   string
		expectedValue string
	}{
		{
			name:          "printable items",
			printable:     true,
			itemId:        "0",
			expectedKey:   "key_0",
			expectedValue: "value_0",
		},
		{
			name:          "non printable items",
			printable:     false,
			itemId:        "0",
			expectedKey:   hex.EncodeToString(convertInt64IntoBytes(0 + 1)),
			expectedValue: hex.EncodeToString(convertInt64IntoBytes(0 + 2)),
		},
	}

	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			db := btesting.MustCreateDBWithOption(t, &bolt.Options{PageSize: 4096})
			srcPath := db.Path()

			t.Log("Inserting some sample data")
			err := db.Update(func(tx *bolt.Tx) error {
				b, bErr := tx.CreateBucketIfNotExists([]byte("data"))
				if bErr != nil {
					return bErr
				}

				for i := 0; i < 100; i++ {
					if tc.printable {
						if bErr = b.Put([]byte(fmt.Sprintf("key_%d", i)), []byte(fmt.Sprintf("value_%d", i))); bErr != nil {
							return bErr
						}
					} else {
						k, v := convertInt64IntoBytes(int64(i+1)), convertInt64IntoBytes(int64(i+2))
						if bErr = b.Put(k, v); bErr != nil {
							return bErr
						}
					}
				}
				return nil
			})
			require.NoError(t, err)
			require.NoError(t, db.Close())
			defer requireDBNoChange(t, dbData(t, srcPath), srcPath)

			meta := readMetaPage(t, srcPath)
			leafPageId := 0
			for i := 2; i < int(meta.Pgid()); i++ {
				p, _, err := guts_cli.ReadPage(srcPath, uint64(i))
				require.NoError(t, err)
				if p.IsLeafPage() && p.Count() > 1 {
					leafPageId = int(p.Id())
				}
			}
			require.NotEqual(t, 0, leafPageId)

			t.Log("Running page-item command")
			rootCmd := command.NewRootCommand()
			outBuf := &bytes.Buffer{}
			rootCmd.SetOut(outBuf)
			rootCmd.SetArgs([]string{"page-item", db.Path(), fmt.Sprintf("%d", leafPageId), tc.itemId})
			err = rootCmd.Execute()
			require.NoError(t, err)

			t.Log("Checking output")
			output := outBuf.String()
			require.True(t, strings.Contains(output, tc.expectedKey), "unexpected output:", output)
			require.True(t, strings.Contains(output, tc.expectedValue), "unexpected output:", output)
		})
	}
}

func TestPageItemCommand_NoArgs(t *testing.T) {
	expErr := errors.New("accepts 3 arg(s), received 0")
	rootCmd := command.NewRootCommand()
	rootCmd.SetArgs([]string{"page-item"})
	err := rootCmd.Execute()
	require.ErrorContains(t, err, expErr.Error())
}
```

## File: `cmd/bbolt/command/command_page_test.go`
```go
package command_test

import (
	"bytes"
	"errors"
	"testing"

	"github.com/stretchr/testify/require"

	bolt "go.etcd.io/bbolt"
	"go.etcd.io/bbolt/cmd/bbolt/command"
	"go.etcd.io/bbolt/internal/btesting"
)

func TestPageCommand_Run(t *testing.T) {
	t.Log("Creating a new database")
	db := btesting.MustCreateDBWithOption(t, &bolt.Options{PageSize: 4096})
	db.Close()

	defer requireDBNoChange(t, dbData(t, db.Path()), db.Path())

	exp := "Page ID:    0\n" +
		"Page Type:  meta\n" +
		"Total Size: 4096 bytes\n" +
		"Overflow pages: 0\n" +
		"Version:    2\n" +
		"Page Size:  4096 bytes\n" +
		"Flags:      00000000\n" +
		"Root:       <pgid=3>\n" +
		"Freelist:   <pgid=2>\n" +
		"HWM:        <pgid=4>\n" +
		"Txn ID:     0\n" +
		"Checksum:   07516e114689fdee\n\n"

	t.Log("Running page command")
	rootCmd := command.NewRootCommand()
	outBuf := &bytes.Buffer{}
	rootCmd.SetOut(outBuf)
	rootCmd.SetArgs([]string{"page", db.Path(), "0"})

	err := rootCmd.Execute()
	require.NoError(t, err)
	require.Equal(t, exp, outBuf.String(), "unexpected stdout")
}

func TestPageCommand_ExclusiveArgs(t *testing.T) {
	testCases := []struct {
		name    string
		pageIds string
		allFlag string
		expErr  error
	}{
		{
			name:    "flag only",
			pageIds: "",
			allFlag: "--all",
			expErr:  nil,
		},
		{
			name:    "pageIds only",
			pageIds: "0",
			allFlag: "",
			expErr:  nil,
		},
		{
			name:    "pageIds and flag",
			pageIds: "0",
			allFlag: "--all",
			expErr:  command.ErrInvalidPageArgs,
		},
	}

	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			t.Log("Creating a new database")
			db := btesting.MustCreateDBWithOption(t, &bolt.Options{PageSize: 4096})
			db.Close()

			defer requireDBNoChange(t, dbData(t, db.Path()), db.Path())

			t.Log("Running page command")
			rootCmd := command.NewRootCommand()
			outBuf := &bytes.Buffer{}
			rootCmd.SetOut(outBuf)
			rootCmd.SetArgs([]string{"page", db.Path(), tc.pageIds, tc.allFlag})

			err := rootCmd.Execute()
			require.Equal(t, tc.expErr, err)
		})
	}
}

func TestPageCommand_NoArgs(t *testing.T) {
	expErr := errors.New("requires at least 1 arg(s), only received 0")
	rootCmd := command.NewRootCommand()
	rootCmd.SetArgs([]string{"page"})
	err := rootCmd.Execute()
	require.ErrorContains(t, err, expErr.Error())
}
```

## File: `cmd/bbolt/command/command_pages.go`
```go
package command

import (
	"fmt"
	"strconv"
	"strings"

	"github.com/spf13/cobra"

	bolt "go.etcd.io/bbolt"
)

type PageError struct {
	ID  int
	Err error
}

func (e *PageError) Error() string {
	return fmt.Sprintf("page error: id=%d, err=%s", e.ID, e.Err)
}

func newPagesCommand() *cobra.Command {
	pagesCmd := &cobra.Command{
		Use:   "pages <bbolt-file>",
		Short: "print a list of pages in bbolt database",
		Long: strings.TrimLeft(`
Pages prints a table of pages with their type (meta, leaf, branch, freelist).
Leaf and branch pages will show a key count in the "items" column while the
freelist will show the number of free pages in the "items" column.

The "overflow" column shows the number of blocks that the page spills over
into. Normally there is no overflow but large keys and values can cause
a single page to take up multiple blocks.
`, "\n"),
		Args: cobra.ExactArgs(1),
		RunE: func(cmd *cobra.Command, args []string) error {
			return pagesFunc(cmd, args[0])
		},
	}

	return pagesCmd
}

func pagesFunc(cmd *cobra.Command, dbPath string) error {
	if _, err := checkSourceDBPath(dbPath); err != nil {
		return err
	}

	// Open database.
	db, err := bolt.Open(dbPath, 0600, &bolt.Options{
		ReadOnly:        true,
		PreLoadFreelist: true,
	})
	if err != nil {
		return err
	}
	defer db.Close()

	// Write header.
	fmt.Fprintln(cmd.OutOrStdout(), "ID       TYPE       ITEMS  OVRFLW")
	fmt.Fprintln(cmd.OutOrStdout(), "======== ========== ====== ======")

	return db.View(func(tx *bolt.Tx) error {
		var id int
		for {
			p, err := tx.Page(id)
			if err != nil {
				return &PageError{ID: id, Err: err}
			} else if p == nil {
				break
			}

			// Only display count and overflow if this is a non-free page.
			var count, overflow string
			if p.Type != "free" {
				count = strconv.Itoa(p.Count)
				if p.OverflowCount > 0 {
					overflow = strconv.Itoa(p.OverflowCount)
				}
			}

			// Print table row.
			fmt.Fprintf(cmd.OutOrStdout(), "%-8d %-10s %-6s %-6s\n", p.ID, p.Type, count, overflow)

			// Move to the next non-overflow page.
			id += 1
			if p.Type != "free" {
				id += p.OverflowCount
			}
		}
		return nil
	})
}
```

## File: `cmd/bbolt/command/command_pages_test.go`
```go
package command_test

import (
	"bytes"
	"errors"
	"fmt"
	"io"
	"testing"

	"github.com/stretchr/testify/require"

	bolt "go.etcd.io/bbolt"
	"go.etcd.io/bbolt/cmd/bbolt/command"
	"go.etcd.io/bbolt/internal/btesting"
)

// Ensure the "pages" command neither panic, nor change the db file.
func TestPagesCommand_Run(t *testing.T) {
	t.Log("Creating sample DB")
	db := btesting.MustCreateDB(t)
	err := db.Update(func(tx *bolt.Tx) error {
		for _, name := range []string{"foo", "bar"} {
			b, err := tx.CreateBucket([]byte(name))
			if err != nil {
				return err
			}
			for i := 0; i < 3; i++ {
				key := fmt.Sprintf("%s-%d", name, i)
				val := fmt.Sprintf("val-%s-%d", name, i)
				if err := b.Put([]byte(key), []byte(val)); err != nil {
					return err
				}
			}
		}
		return nil
	})
	require.NoError(t, err)
	db.Close()
	defer requireDBNoChange(t, dbData(t, db.Path()), db.Path())

	t.Log("Running pages cmd")
	rootCmd := command.NewRootCommand()
	outputBuf := bytes.NewBufferString("")
	rootCmd.SetOut(outputBuf)

	rootCmd.SetArgs([]string{"pages", db.Path()})
	err = rootCmd.Execute()
	require.NoError(t, err)

	t.Log("Checking output")
	_, err = io.ReadAll(outputBuf)
	require.NoError(t, err)
}

func TestPagesCommand_NoArgs(t *testing.T) {
	expErr := errors.New("accepts 1 arg(s), received 0")
	rootCmd := command.NewRootCommand()
	rootCmd.SetArgs([]string{"pages"})
	err := rootCmd.Execute()
	require.ErrorContains(t, err, expErr.Error())
}
```

## File: `cmd/bbolt/command/command_root.go`
```go
package command

import (
	"github.com/spf13/cobra"
)

const (
	cliName        = "bbolt"
	cliDescription = "A simple command line tool for inspecting bbolt databases"
)

func NewRootCommand() *cobra.Command {
	rootCmd := &cobra.Command{
		Use:     cliName,
		Short:   cliDescription,
		Version: "dev",
	}

	rootCmd.AddCommand(
		newVersionCommand(),
		newSurgeryCommand(),
		newInspectCommand(),
		newCheckCommand(),
		newBucketsCommand(),
		newInfoCommand(),
		newCompactCommand(),
		newStatsCommand(),
		newPagesCommand(),
		newKeysCommand(),
		newDumpCommand(),
		newPageItemCommand(),
		newPageCommand(),
		newBenchCommand(),
		newGetCommand(),
	)

	return rootCmd
}
```

## File: `cmd/bbolt/command/command_stats.go`
```go
package command

import (
	"bytes"
	"fmt"
	"strings"

	"github.com/spf13/cobra"

	bolt "go.etcd.io/bbolt"
)

func newStatsCommand() *cobra.Command {
	statsCmd := &cobra.Command{
		Use:   "stats <bbolt-file>",
		Short: "print stats of bbolt database",
		Long: strings.TrimLeft(`
usage: bolt stats PATH

Stats performs an extensive search of the database to track every page
reference. It starts at the current meta page and recursively iterates
through every accessible bucket.

The following errors can be reported:

    already freed
        The page is referenced more than once in the freelist.

    unreachable unfreed
        The page is not referenced by a bucket or in the freelist.

    reachable freed
        The page is referenced by a bucket but is also in the freelist.

    out of bounds
        A page is referenced that is above the high water mark.

    multiple references
        A page is referenced by more than one other page.

    invalid type
        The page type is not "meta", "leaf", "branch", or "freelist".

No errors should occur in your database. However, if for some reason you
experience corruption, please submit a ticket to the etcd-io/bbolt project page:

  https://github.com/etcd-io/bbolt/issues
`, "\n"),
		Args: cobra.RangeArgs(1, 2),
		RunE: func(cmd *cobra.Command, args []string) error {
			prefix := ""
			if len(args) > 1 {
				prefix = args[1]
			}

			return statsFunc(cmd, args[0], prefix)
		},
	}

	return statsCmd
}

func statsFunc(cmd *cobra.Command, dbPath string, prefix string) error {
	if _, err := checkSourceDBPath(dbPath); err != nil {
		return err
	}

	// open database.
	db, err := bolt.Open(dbPath, 0600, &bolt.Options{
		ReadOnly:        true,
		PreLoadFreelist: true,
	})
	if err != nil {
		return err
	}
	defer db.Close()

	return db.View(func(tx *bolt.Tx) error {
		var s bolt.BucketStats
		var count int
		if err := tx.ForEach(func(name []byte, b *bolt.Bucket) error {
			if bytes.HasPrefix(name, []byte(prefix)) {
				s.Add(b.Stats())
				count += 1
			}
			return nil
		}); err != nil {
			return err
		}

		fmt.Fprintf(cmd.OutOrStdout(), "Aggregate statistics for %d buckets\n\n", count)

		fmt.Fprintln(cmd.OutOrStdout(), "Page count statistics")
		fmt.Fprintf(cmd.OutOrStdout(), "\tNumber of logical branch pages: %d\n", s.BranchPageN)
		fmt.Fprintf(cmd.OutOrStdout(), "\tNumber of physical branch overflow pages: %d\n", s.BranchOverflowN)
		fmt.Fprintf(cmd.OutOrStdout(), "\tNumber of logical leaf pages: %d\n", s.LeafPageN)
		fmt.Fprintf(cmd.OutOrStdout(), "\tNumber of physical leaf overflow pages: %d\n", s.LeafOverflowN)

		fmt.Fprintln(cmd.OutOrStdout(), "Tree statistics")
		fmt.Fprintf(cmd.OutOrStdout(), "\tNumber of keys/value pairs: %d\n", s.KeyN)
		fmt.Fprintf(cmd.OutOrStdout(), "\tNumber of levels in B+tree: %d\n", s.Depth)

		fmt.Fprintln(cmd.OutOrStdout(), "Page size utilization")
		fmt.Fprintf(cmd.OutOrStdout(), "\tBytes allocated for physical branch pages: %d\n", s.BranchAlloc)
		var percentage int
		if s.BranchAlloc != 0 {
			percentage = int(float32(s.BranchInuse) * 100.0 / float32(s.BranchAlloc))
		}
		fmt.Fprintf(cmd.OutOrStdout(), "\tBytes actually used for branch data: %d (%d%%)\n", s.BranchInuse, percentage)
		fmt.Fprintf(cmd.OutOrStdout(), "\tBytes allocated for physical leaf pages: %d\n", s.LeafAlloc)
		percentage = 0
		if s.LeafAlloc != 0 {
			percentage = int(float32(s.LeafInuse) * 100.0 / float32(s.LeafAlloc))
		}
		fmt.Fprintf(cmd.OutOrStdout(), "\tBytes actually used for leaf data: %d (%d%%)\n", s.LeafInuse, percentage)

		fmt.Fprintln(cmd.OutOrStdout(), "Bucket statistics")
		fmt.Fprintf(cmd.OutOrStdout(), "\tTotal number of buckets: %d\n", s.BucketN)
		percentage = 0
		if s.BucketN != 0 {
			percentage = int(float32(s.InlineBucketN) * 100.0 / float32(s.BucketN))
		}
		fmt.Fprintf(cmd.OutOrStdout(), "\tTotal number on inlined buckets: %d (%d%%)\n", s.InlineBucketN, percentage)
		percentage = 0
		if s.LeafInuse != 0 {
			percentage = int(float32(s.InlineBucketInuse) * 100.0 / float32(s.LeafInuse))
		}
		fmt.Fprintf(cmd.OutOrStdout(), "\tBytes used for inlined buckets: %d (%d%%)\n", s.InlineBucketInuse, percentage)

		return nil
	})
}
```

## File: `cmd/bbolt/command/command_stats_test.go`
```go
package command_test

import (
	"bytes"
	"errors"
	"io"
	"os"
	"strconv"
	"testing"

	"github.com/stretchr/testify/require"

	bolt "go.etcd.io/bbolt"
	"go.etcd.io/bbolt/cmd/bbolt/command"
	"go.etcd.io/bbolt/internal/btesting"
)

// Ensure the "stats" command executes correctly with an empty database.
func TestStatsCommand_Run_EmptyDatabase(t *testing.T) {
	// ignore
	if os.Getpagesize() != 4096 {
		t.Skip("system does not use 4KB page size")
	}

	t.Log("Creating sample DB")
	db := btesting.MustCreateDB(t)
	db.Close()
	defer requireDBNoChange(t, dbData(t, db.Path()), db.Path())

	// generate expected result.
	exp := "Aggregate statistics for 0 buckets\n\n" +
		"Page count statistics\n" +
		"\tNumber of logical branch pages: 0\n" +
		"\tNumber of physical branch overflow pages: 0\n" +
		"\tNumber of logical leaf pages: 0\n" +
		"\tNumber of physical leaf overflow pages: 0\n" +
		"Tree statistics\n" +
		"\tNumber of keys/value pairs: 0\n" +
		"\tNumber of levels in B+tree: 0\n" +
		"Page size utilization\n" +
		"\tBytes allocated for physical branch pages: 0\n" +
		"\tBytes actually used for branch data: 0 (0%)\n" +
		"\tBytes allocated for physical leaf pages: 0\n" +
		"\tBytes actually used for leaf data: 0 (0%)\n" +
		"Bucket statistics\n" +
		"\tTotal number of buckets: 0\n" +
		"\tTotal number on inlined buckets: 0 (0%)\n" +
		"\tBytes used for inlined buckets: 0 (0%)\n"

	t.Log("Running stats cmd")
	rootCmd := command.NewRootCommand()
	outputBuf := bytes.NewBufferString("")
	rootCmd.SetOut(outputBuf)

	rootCmd.SetArgs([]string{"stats", db.Path()})
	err := rootCmd.Execute()
	require.NoError(t, err)

	t.Log("Checking output")
	output, err := io.ReadAll(outputBuf)
	require.NoError(t, err)
	require.Exactlyf(t, exp, string(output), "unexpected stdout:\n\n%s", string(output))
}

// Ensure the "stats" command can execute correctly.
func TestStatsCommand_Run(t *testing.T) {
	// ignore
	if os.Getpagesize() != 4096 {
		t.Skip("system does not use 4KB page size")
	}

	t.Log("Creating sample DB")
	db := btesting.MustCreateDB(t)
	if err := db.Update(func(tx *bolt.Tx) error {
		// create "foo" bucket.
		b, err := tx.CreateBucket([]byte("foo"))
		if err != nil {
			return err
		}
		for i := 0; i < 10; i++ {
			if err := b.Put([]byte(strconv.Itoa(i)), []byte(strconv.Itoa(i))); err != nil {
				return err
			}
		}

		// create "bar" bucket.
		b, err = tx.CreateBucket([]byte("bar"))
		if err != nil {
			return err
		}
		for i := 0; i < 100; i++ {
			if err := b.Put([]byte(strconv.Itoa(i)), []byte(strconv.Itoa(i))); err != nil {
				return err
			}
		}

		// create "baz" bucket.
		b, err = tx.CreateBucket([]byte("baz"))
		if err != nil {
			return err
		}
		if err := b.Put([]byte("key"), []byte("value")); err != nil {
			return err
		}

		return nil
	}); err != nil {
		t.Fatal(err)
	}
	db.Close()
	defer requireDBNoChange(t, dbData(t, db.Path()), db.Path())

	// generate expected result.
	exp := "Aggregate statistics for 3 buckets\n\n" +
		"Page count statistics\n" +
		"\tNumber of logical branch pages: 0\n" +
		"\tNumber of physical branch overflow pages: 0\n" +
		"\tNumber of logical leaf pages: 1\n" +
		"\tNumber of physical leaf overflow pages: 0\n" +
		"Tree statistics\n" +
		"\tNumber of keys/value pairs: 111\n" +
		"\tNumber of levels in B+tree: 1\n" +
		"Page size utilization\n" +
		"\tBytes allocated for physical branch pages: 0\n" +
		"\tBytes actually used for branch data: 0 (0%)\n" +
		"\tBytes allocated for physical leaf pages: 4096\n" +
		"\tBytes actually used for leaf data: 1996 (48%)\n" +
		"Bucket statistics\n" +
		"\tTotal number of buckets: 3\n" +
		"\tTotal number on inlined buckets: 2 (66%)\n" +
		"\tBytes used for inlined buckets: 236 (11%)\n"

	t.Log("Running stats cmd")
	rootCmd := command.NewRootCommand()
	outputBuf := bytes.NewBufferString("")
	rootCmd.SetOut(outputBuf)

	rootCmd.SetArgs([]string{"stats", db.Path()})
	err := rootCmd.Execute()
	require.NoError(t, err)

	t.Log("Checking output")
	output, err := io.ReadAll(outputBuf)
	require.NoError(t, err)
	require.Exactlyf(t, exp, string(output), "unexpected stdout:\n\n%s", string(output))
}

func TestStatsCommand_NoArgs(t *testing.T) {
	expErr := errors.New("accepts between 1 and 2 arg(s), received 0")
	rootCmd := command.NewRootCommand()
	rootCmd.SetArgs([]string{"stats"})
	err := rootCmd.Execute()
	require.ErrorContains(t, err, expErr.Error())
}
```

## File: `cmd/bbolt/command/command_surgery.go`
```go
package command

import (
	"errors"
	"fmt"
	"os"

	"github.com/spf13/cobra"
	"github.com/spf13/pflag"

	"go.etcd.io/bbolt/internal/common"
	"go.etcd.io/bbolt/internal/guts_cli"
	"go.etcd.io/bbolt/internal/surgeon"
)

func newSurgeryCommand() *cobra.Command {
	surgeryCmd := &cobra.Command{
		Use:   "surgery <subcommand>",
		Short: "surgery related commands",
	}

	surgeryCmd.AddCommand(newSurgeryRevertMetaPageCommand())
	surgeryCmd.AddCommand(newSurgeryCopyPageCommand())
	surgeryCmd.AddCommand(newSurgeryClearPageCommand())
	surgeryCmd.AddCommand(newSurgeryClearPageElementsCommand())
	surgeryCmd.AddCommand(newSurgeryFreelistCommand())
	surgeryCmd.AddCommand(newSurgeryMetaCommand())

	return surgeryCmd
}

type surgeryBaseOptions struct {
	outputDBFilePath string
}

func (o *surgeryBaseOptions) AddFlags(fs *pflag.FlagSet) {
	fs.StringVar(&o.outputDBFilePath, "output", o.outputDBFilePath, "path to the filePath db file")
	_ = cobra.MarkFlagRequired(fs, "output")
}

func (o *surgeryBaseOptions) Validate() error {
	if o.outputDBFilePath == "" {
		return errors.New("output database path wasn't given, specify output database file path with --output option")
	}
	return nil
}

func newSurgeryRevertMetaPageCommand() *cobra.Command {
	var o surgeryBaseOptions
	revertMetaPageCmd := &cobra.Command{
		Use:   "revert-meta-page <bbolt-file>",
		Short: "Revert the meta page to revert the changes performed by the latest transaction",
		Args:  cobra.ExactArgs(1),
		RunE: func(cmd *cobra.Command, args []string) error {
			if err := o.Validate(); err != nil {
				return err
			}
			return surgeryRevertMetaPageFunc(args[0], o)
		},
	}
	o.AddFlags(revertMetaPageCmd.Flags())
	return revertMetaPageCmd
}

func surgeryRevertMetaPageFunc(srcDBPath string, cfg surgeryBaseOptions) error {
	if _, err := checkSourceDBPath(srcDBPath); err != nil {
		return err
	}

	if err := common.CopyFile(srcDBPath, cfg.outputDBFilePath); err != nil {
		return fmt.Errorf("[revert-meta-page] copy file failed: %w", err)
	}

	if err := surgeon.RevertMetaPage(cfg.outputDBFilePath); err != nil {
		return fmt.Errorf("revert-meta-page command failed: %w", err)
	}

	fmt.Fprintln(os.Stdout, "The meta page is reverted.")

	return nil
}

type surgeryCopyPageOptions struct {
	surgeryBaseOptions
	sourcePageId      uint64
	destinationPageId uint64
}

func (o *surgeryCopyPageOptions) AddFlags(fs *pflag.FlagSet) {
	o.surgeryBaseOptions.AddFlags(fs)
	fs.Uint64VarP(&o.sourcePageId, "from-page", "", o.sourcePageId, "source page Id")
	fs.Uint64VarP(&o.destinationPageId, "to-page", "", o.destinationPageId, "destination page Id")
	_ = cobra.MarkFlagRequired(fs, "from-page")
	_ = cobra.MarkFlagRequired(fs, "to-page")
}

func (o *surgeryCopyPageOptions) Validate() error {
	if err := o.surgeryBaseOptions.Validate(); err != nil {
		return err
	}
	if o.sourcePageId == o.destinationPageId {
		return fmt.Errorf("'--from-page' and '--to-page' have the same value: %d", o.sourcePageId)
	}
	return nil
}

func newSurgeryCopyPageCommand() *cobra.Command {
	var o surgeryCopyPageOptions
	copyPageCmd := &cobra.Command{
		Use:   "copy-page <bbolt-file>",
		Short: "Copy page from the source page Id to the destination page Id",
		Args:  cobra.ExactArgs(1),
		RunE: func(cmd *cobra.Command, args []string) error {
			if err := o.Validate(); err != nil {
				return err
			}
			return surgeryCopyPageFunc(args[0], o)
		},
	}
	o.AddFlags(copyPageCmd.Flags())
	return copyPageCmd
}

func surgeryCopyPageFunc(srcDBPath string, cfg surgeryCopyPageOptions) error {
	if _, err := checkSourceDBPath(srcDBPath); err != nil {
		return err
	}

	if err := common.CopyFile(srcDBPath, cfg.outputDBFilePath); err != nil {
		return fmt.Errorf("[copy-page] copy file failed: %w", err)
	}

	if err := surgeon.CopyPage(cfg.outputDBFilePath, common.Pgid(cfg.sourcePageId), common.Pgid(cfg.destinationPageId)); err != nil {
		return fmt.Errorf("copy-page command failed: %w", err)
	}

	meta, err := readMetaPage(srcDBPath)
	if err != nil {
		return err
	}
	if meta.IsFreelistPersisted() {
		fmt.Fprintf(os.Stdout, "WARNING: the free list might have changed.\n")
		fmt.Fprintf(os.Stdout, "Please consider executing `./bbolt surgery freelist abandon ...`\n")
	}

	fmt.Fprintf(os.Stdout, "The page %d was successfully copied to page %d\n", cfg.sourcePageId, cfg.destinationPageId)
	return nil
}

type surgeryClearPageOptions struct {
	surgeryBaseOptions
	pageId uint64
}

func (o *surgeryClearPageOptions) AddFlags(fs *pflag.FlagSet) {
	o.surgeryBaseOptions.AddFlags(fs)
	fs.Uint64VarP(&o.pageId, "pageId", "", o.pageId, "page Id")
	_ = cobra.MarkFlagRequired(fs, "pageId")
}

func (o *surgeryClearPageOptions) Validate() error {
	if err := o.surgeryBaseOptions.Validate(); err != nil {
		return err
	}
	if o.pageId < 2 {
		return fmt.Errorf("the pageId must be at least 2, but got %d", o.pageId)
	}
	return nil
}

func newSurgeryClearPageCommand() *cobra.Command {
	var o surgeryClearPageOptions
	clearPageCmd := &cobra.Command{
		Use:   "clear-page <bbolt-file>",
		Short: "Clears all elements from the given page, which can be a branch or leaf page",
		Args:  cobra.ExactArgs(1),
		RunE: func(cmd *cobra.Command, args []string) error {
			if err := o.Validate(); err != nil {
				return err
			}
			return surgeryClearPageFunc(args[0], o)
		},
	}
	o.AddFlags(clearPageCmd.Flags())
	return clearPageCmd
}

func surgeryClearPageFunc(srcDBPath string, cfg surgeryClearPageOptions) error {
	if _, err := checkSourceDBPath(srcDBPath); err != nil {
		return err
	}

	if err := common.CopyFile(srcDBPath, cfg.outputDBFilePath); err != nil {
		return fmt.Errorf("[clear-page] copy file failed: %w", err)
	}

	needAbandonFreelist, err := surgeon.ClearPage(cfg.outputDBFilePath, common.Pgid(cfg.pageId))
	if err != nil {
		return fmt.Errorf("clear-page command failed: %w", err)
	}

	if needAbandonFreelist {
		fmt.Fprintf(os.Stdout, "WARNING: The clearing has abandoned some pages that are not yet referenced from free list.\n")
		fmt.Fprintf(os.Stdout, "Please consider executing `./bbolt surgery freelist abandon ...`\n")
	}

	fmt.Fprintf(os.Stdout, "The page (%d) was cleared\n", cfg.pageId)
	return nil
}

type surgeryClearPageElementsOptions struct {
	surgeryBaseOptions
	pageId          uint64
	startElementIdx int
	endElementIdx   int
}

func (o *surgeryClearPageElementsOptions) AddFlags(fs *pflag.FlagSet) {
	o.surgeryBaseOptions.AddFlags(fs)
	fs.Uint64VarP(&o.pageId, "pageId", "", o.pageId, "page id")
	fs.IntVarP(&o.startElementIdx, "from-index", "", o.startElementIdx, "start element index (included) to clear, starting from 0")
	fs.IntVarP(&o.endElementIdx, "to-index", "", o.endElementIdx, "end element index (excluded) to clear, starting from 0, -1 means to the end of page")
	_ = cobra.MarkFlagRequired(fs, "pageId")
	_ = cobra.MarkFlagRequired(fs, "from-index")
	_ = cobra.MarkFlagRequired(fs, "to-index")
}

func (o *surgeryClearPageElementsOptions) Validate() error {
	if err := o.surgeryBaseOptions.Validate(); err != nil {
		return err
	}
	if o.pageId < 2 {
		return fmt.Errorf("the pageId must be at least 2, but got %d", o.pageId)
	}
	return nil
}

func newSurgeryClearPageElementsCommand() *cobra.Command {
	var o surgeryClearPageElementsOptions
	clearElementCmd := &cobra.Command{
		Use:   "clear-page-elements <bbolt-file>",
		Short: "Clears elements from the given page, which can be a branch or leaf page",
		Args:  cobra.ExactArgs(1),
		RunE: func(cmd *cobra.Command, args []string) error {
			if err := o.Validate(); err != nil {
				return err
			}
			return surgeryClearPageElementFunc(args[0], o)
		},
	}
	o.AddFlags(clearElementCmd.Flags())
	return clearElementCmd
}

func surgeryClearPageElementFunc(srcDBPath string, cfg surgeryClearPageElementsOptions) error {
	if _, err := checkSourceDBPath(srcDBPath); err != nil {
		return err
	}

	if err := common.CopyFile(srcDBPath, cfg.outputDBFilePath); err != nil {
		return fmt.Errorf("[clear-page-element] copy file failed: %w", err)
	}

	needAbandonFreelist, err := surgeon.ClearPageElements(cfg.outputDBFilePath, common.Pgid(cfg.pageId), cfg.startElementIdx, cfg.endElementIdx, false)
	if err != nil {
		return fmt.Errorf("clear-page-element command failed: %w", err)
	}

	if needAbandonFreelist {
		fmt.Fprintf(os.Stdout, "WARNING: The clearing has abandoned some pages that are not yet referenced from free list.\n")
		fmt.Fprintf(os.Stdout, "Please consider executing `./bbolt surgery freelist abandon ...`\n")
	}

	fmt.Fprintf(os.Stdout, "All elements in [%d, %d) in page %d were cleared\n", cfg.startElementIdx, cfg.endElementIdx, cfg.pageId)
	return nil
}

func readMetaPage(path string) (*common.Meta, error) {
	pageSize, _, err := guts_cli.ReadPageAndHWMSize(path)
	if err != nil {
		return nil, fmt.Errorf("read Page size failed: %w", err)
	}

	m := make([]*common.Meta, 2)
	for i := 0; i < 2; i++ {
		m[i], _, err = ReadMetaPageAt(path, uint32(i), uint32(pageSize))
		if err != nil {
			return nil, fmt.Errorf("read meta page %d failed: %w", i, err)
		}
	}

	if m[0].Txid() > m[1].Txid() {
		return m[0], nil
	}
	return m[1], nil
}
```

## File: `cmd/bbolt/command/command_surgery_freelist.go`
```go
package command

import (
	"fmt"
	"os"

	"github.com/spf13/cobra"

	bolt "go.etcd.io/bbolt"
	"go.etcd.io/bbolt/internal/common"
	"go.etcd.io/bbolt/internal/surgeon"
)

func newSurgeryFreelistCommand() *cobra.Command {
	cmd := &cobra.Command{
		Use:   "freelist <subcommand>",
		Short: "freelist related surgery commands",
	}

	cmd.AddCommand(newSurgeryFreelistAbandonCommand())
	cmd.AddCommand(newSurgeryFreelistRebuildCommand())

	return cmd
}

func newSurgeryFreelistAbandonCommand() *cobra.Command {
	var o surgeryBaseOptions
	abandonFreelistCmd := &cobra.Command{
		Use:   "abandon <bbolt-file>",
		Short: "Abandon the freelist from both meta pages",
		Args:  cobra.ExactArgs(1),
		RunE: func(cmd *cobra.Command, args []string) error {
			if err := o.Validate(); err != nil {
				return err
			}
			return surgeryFreelistAbandonFunc(args[0], o)
		},
	}
	o.AddFlags(abandonFreelistCmd.Flags())

	return abandonFreelistCmd
}

func surgeryFreelistAbandonFunc(srcDBPath string, cfg surgeryBaseOptions) error {
	if _, err := checkSourceDBPath(srcDBPath); err != nil {
		return err
	}

	if err := common.CopyFile(srcDBPath, cfg.outputDBFilePath); err != nil {
		return fmt.Errorf("[freelist abandon] copy file failed: %w", err)
	}

	if err := surgeon.ClearFreelist(cfg.outputDBFilePath); err != nil {
		return fmt.Errorf("abandom-freelist command failed: %w", err)
	}

	fmt.Fprintf(os.Stdout, "The freelist was abandoned in both meta pages.\nIt may cause some delay on next startup because bbolt needs to scan the whole db to reconstruct the free list.\n")
	return nil
}

func newSurgeryFreelistRebuildCommand() *cobra.Command {
	var o surgeryBaseOptions
	rebuildFreelistCmd := &cobra.Command{
		Use:   "rebuild <bbolt-file>",
		Short: "Rebuild the freelist",
		Args:  cobra.ExactArgs(1),
		RunE: func(cmd *cobra.Command, args []string) error {
			if err := o.Validate(); err != nil {
				return err
			}
			return surgeryFreelistRebuildFunc(args[0], o)
		},
	}
	o.AddFlags(rebuildFreelistCmd.Flags())

	return rebuildFreelistCmd
}

func surgeryFreelistRebuildFunc(srcDBPath string, cfg surgeryBaseOptions) error {
	// Ensure source file exists.
	fi, err := checkSourceDBPath(srcDBPath)
	if err != nil {
		return err
	}

	// make sure the freelist isn't present in the file.
	meta, err := readMetaPage(srcDBPath)
	if err != nil {
		return err
	}
	if meta.IsFreelistPersisted() {
		return ErrSurgeryFreelistAlreadyExist
	}

	if err := common.CopyFile(srcDBPath, cfg.outputDBFilePath); err != nil {
		return fmt.Errorf("[freelist rebuild] copy file failed: %w", err)
	}

	// bboltDB automatically reconstruct & sync freelist in write mode.
	db, err := bolt.Open(cfg.outputDBFilePath, fi.Mode(), &bolt.Options{NoFreelistSync: false})
	if err != nil {
		return fmt.Errorf("[freelist rebuild] open db file failed: %w", err)
	}
	err = db.Close()
	if err != nil {
		return fmt.Errorf("[freelist rebuild] close db file failed: %w", err)
	}

	fmt.Fprintf(os.Stdout, "The freelist was successfully rebuilt.\n")
	return nil
}
```

## File: `cmd/bbolt/command/command_surgery_freelist_test.go`
```go
package command_test

import (
	"path/filepath"
	"testing"

	"github.com/stretchr/testify/assert"
	"github.com/stretchr/testify/require"

	bolt "go.etcd.io/bbolt"
	"go.etcd.io/bbolt/cmd/bbolt/command"
	"go.etcd.io/bbolt/internal/btesting"
	"go.etcd.io/bbolt/internal/common"
)

func TestSurgery_Freelist_Abandon(t *testing.T) {
	pageSize := 4096
	db := btesting.MustCreateDBWithOption(t, &bolt.Options{PageSize: pageSize})
	srcPath := db.Path()

	defer requireDBNoChange(t, dbData(t, srcPath), srcPath)

	rootCmd := command.NewRootCommand()
	output := filepath.Join(t.TempDir(), "db")
	rootCmd.SetArgs([]string{
		"surgery", "freelist", "abandon", srcPath,
		"--output", output,
	})
	err := rootCmd.Execute()
	require.NoError(t, err)

	meta0 := loadMetaPage(t, output, 0)
	assert.Equal(t, common.PgidNoFreelist, meta0.Freelist())
	meta1 := loadMetaPage(t, output, 1)
	assert.Equal(t, common.PgidNoFreelist, meta1.Freelist())
}

func TestSurgery_Freelist_Rebuild(t *testing.T) {
	testCases := []struct {
		name          string
		hasFreelist   bool
		expectedError error
	}{
		{
			name:          "normal operation",
			hasFreelist:   false,
			expectedError: nil,
		},
		{
			name:          "already has freelist",
			hasFreelist:   true,
			expectedError: command.ErrSurgeryFreelistAlreadyExist,
		},
	}

	for _, tc := range testCases {
		tc := tc
		t.Run(tc.name, func(t *testing.T) {
			pageSize := 4096
			db := btesting.MustCreateDBWithOption(t, &bolt.Options{
				PageSize:       pageSize,
				NoFreelistSync: !tc.hasFreelist,
			})
			srcPath := db.Path()

			err := db.Update(func(tx *bolt.Tx) error {
				// do nothing
				return nil
			})
			require.NoError(t, err)

			defer requireDBNoChange(t, dbData(t, srcPath), srcPath)

			// Verify the freelist isn't synced in the beginning
			meta := readMetaPage(t, srcPath)
			if tc.hasFreelist {
				if meta.Freelist() <= 1 || meta.Freelist() >= meta.Pgid() {
					t.Fatalf("freelist (%d) isn't in the valid range (1, %d)", meta.Freelist(), meta.Pgid())
				}
			} else {
				require.Equal(t, common.PgidNoFreelist, meta.Freelist())
			}

			// Execute `surgery freelist rebuild` command
			rootCmd := command.NewRootCommand()
			output := filepath.Join(t.TempDir(), "db")
			rootCmd.SetArgs([]string{
				"surgery", "freelist", "rebuild", srcPath,
				"--output", output,
			})
			err = rootCmd.Execute()
			require.Equal(t, tc.expectedError, err)

			if tc.expectedError == nil {
				// Verify the freelist has already been rebuilt.
				meta = readMetaPage(t, output)
				if meta.Freelist() <= 1 || meta.Freelist() >= meta.Pgid() {
					t.Fatalf("freelist (%d) isn't in the valid range (1, %d)", meta.Freelist(), meta.Pgid())
				}
			}
		})
	}
}
```

## File: `cmd/bbolt/command/command_surgery_meta.go`
```go
package command

import (
	"fmt"
	"io"
	"os"
	"strconv"
	"strings"

	"github.com/spf13/cobra"
	"github.com/spf13/pflag"

	"go.etcd.io/bbolt/internal/common"
)

const (
	metaFieldPageSize = "pageSize"
	metaFieldRoot     = "root"
	metaFieldFreelist = "freelist"
	metaFieldPgid     = "pgid"
)

func newSurgeryMetaCommand() *cobra.Command {
	cmd := &cobra.Command{
		Use:   "meta <subcommand>",
		Short: "meta page related surgery commands",
	}

	cmd.AddCommand(newSurgeryMetaValidateCommand())
	cmd.AddCommand(newSurgeryMetaUpdateCommand())

	return cmd
}

func newSurgeryMetaValidateCommand() *cobra.Command {
	metaValidateCmd := &cobra.Command{
		Use:   "validate <bbolt-file>",
		Short: "Validate both meta pages",
		Args:  cobra.ExactArgs(1),
		RunE: func(cmd *cobra.Command, args []string) error {
			return surgeryMetaValidateFunc(args[0])
		},
	}
	return metaValidateCmd
}

func surgeryMetaValidateFunc(srcDBPath string) error {
	if _, err := checkSourceDBPath(srcDBPath); err != nil {
		return err
	}

	var pageSize uint32

	for i := 0; i <= 1; i++ {
		m, _, err := ReadMetaPageAt(srcDBPath, uint32(i), pageSize)
		if err != nil {
			return fmt.Errorf("read meta page %d failed: %w", i, err)
		}
		if mValidateErr := m.Validate(); mValidateErr != nil {
			fmt.Fprintf(os.Stdout, "WARNING: The meta page %d isn't valid: %v!\n", i, mValidateErr)
		} else {
			fmt.Fprintf(os.Stdout, "The meta page %d is valid!\n", i)
		}

		pageSize = m.PageSize()
	}

	return nil
}

type surgeryMetaUpdateOptions struct {
	surgeryBaseOptions
	fields     []string
	metaPageId uint32
}

var allowedMetaUpdateFields = map[string]struct{}{
	metaFieldPageSize: {},
	metaFieldRoot:     {},
	metaFieldFreelist: {},
	metaFieldPgid:     {},
}

// AddFlags sets the flags for `meta update` command.
// Example: --fields root:16,freelist:8 --fields pgid:128
// Result: []string{"root:16", "freelist:8", "pgid:128"}
func (o *surgeryMetaUpdateOptions) AddFlags(fs *pflag.FlagSet) {
	o.surgeryBaseOptions.AddFlags(fs)
	fs.StringSliceVarP(&o.fields, "fields", "", o.fields, "comma separated list of fields (supported fields: pageSize, root, freelist and pgid) to be updated, and each item is a colon-separated key-value pair")
	fs.Uint32VarP(&o.metaPageId, "meta-page", "", o.metaPageId, "the meta page ID to operate on, valid values are 0 and 1")
}

func (o *surgeryMetaUpdateOptions) Validate() error {
	if err := o.surgeryBaseOptions.Validate(); err != nil {
		return err
	}

	if o.metaPageId > 1 {
		return fmt.Errorf("invalid meta page id: %d", o.metaPageId)
	}

	for _, field := range o.fields {
		kv := strings.Split(field, ":")
		if len(kv) != 2 {
			return fmt.Errorf("invalid key-value pair: %s", field)
		}

		if _, ok := allowedMetaUpdateFields[kv[0]]; !ok {
			return fmt.Errorf("field %q isn't allowed to be updated", kv[0])
		}

		if _, err := strconv.ParseUint(kv[1], 10, 64); err != nil {
			return fmt.Errorf("invalid value %q for field %q", kv[1], kv[0])
		}
	}

	return nil
}

func newSurgeryMetaUpdateCommand() *cobra.Command {
	var o surgeryMetaUpdateOptions
	metaUpdateCmd := &cobra.Command{
		Use:   "update <bbolt-file>",
		Short: "Update fields in meta pages",
		Args:  cobra.ExactArgs(1),
		RunE: func(cmd *cobra.Command, args []string) error {
			if err := o.Validate(); err != nil {
				return err
			}
			return surgeryMetaUpdateFunc(args[0], o)
		},
	}
	o.AddFlags(metaUpdateCmd.Flags())
	return metaUpdateCmd
}

func surgeryMetaUpdateFunc(srcDBPath string, cfg surgeryMetaUpdateOptions) error {
	if _, err := checkSourceDBPath(srcDBPath); err != nil {
		return err
	}

	if err := common.CopyFile(srcDBPath, cfg.outputDBFilePath); err != nil {
		return fmt.Errorf("[meta update] copy file failed: %w", err)
	}

	// read the page size from the first meta page if we want to edit the second meta page.
	var pageSize uint32
	if cfg.metaPageId == 1 {
		m0, _, err := ReadMetaPageAt(cfg.outputDBFilePath, 0, pageSize)
		if err != nil {
			return fmt.Errorf("read the first meta page failed: %w", err)
		}
		pageSize = m0.PageSize()
	}

	// update the specified meta page
	m, buf, err := ReadMetaPageAt(cfg.outputDBFilePath, cfg.metaPageId, pageSize)
	if err != nil {
		return fmt.Errorf("read meta page %d failed: %w", cfg.metaPageId, err)
	}
	mChanged := updateMetaField(m, parseFields(cfg.fields))
	if mChanged {
		if err := writeMetaPageAt(cfg.outputDBFilePath, buf, cfg.metaPageId, pageSize); err != nil {
			return fmt.Errorf("[meta update] write meta page %d failed: %w", cfg.metaPageId, err)
		}
	}

	if cfg.metaPageId == 1 && pageSize != m.PageSize() {
		fmt.Fprintf(os.Stdout, "WARNING: The page size (%d) in the first meta page doesn't match the second meta page (%d)\n", pageSize, m.PageSize())
	}

	// Display results
	if !mChanged {
		fmt.Fprintln(os.Stdout, "Nothing changed!")
	}

	if mChanged {
		fmt.Fprintf(os.Stdout, "The meta page %d has been updated!\n", cfg.metaPageId)
	}

	return nil
}

func parseFields(fields []string) map[string]uint64 {
	fieldsMap := make(map[string]uint64)
	for _, field := range fields {
		kv := strings.SplitN(field, ":", 2)
		val, _ := strconv.ParseUint(kv[1], 10, 64)
		fieldsMap[kv[0]] = val
	}
	return fieldsMap
}

func updateMetaField(m *common.Meta, fields map[string]uint64) bool {
	changed := false
	for key, val := range fields {
		switch key {
		case metaFieldPageSize:
			m.SetPageSize(uint32(val))
		case metaFieldRoot:
			m.SetRootBucket(common.NewInBucket(common.Pgid(val), 0))
		case metaFieldFreelist:
			m.SetFreelist(common.Pgid(val))
		case metaFieldPgid:
			m.SetPgid(common.Pgid(val))
		}

		changed = true
	}

	if m.Magic() != common.Magic {
		m.SetMagic(common.Magic)
		changed = true
	}
	if m.Version() != common.Version {
		m.SetVersion(common.Version)
		changed = true
	}
	if m.Flags() != common.MetaPageFlag {
		m.SetFlags(common.MetaPageFlag)
		changed = true
	}

	newChecksum := m.Sum64()
	if m.Checksum() != newChecksum {
		m.SetChecksum(newChecksum)
		changed = true
	}

	return changed
}

func ReadMetaPageAt(dbPath string, metaPageId uint32, pageSize uint32) (*common.Meta, []byte, error) {
	if metaPageId > 1 {
		return nil, nil, fmt.Errorf("invalid metaPageId: %d", metaPageId)
	}

	f, err := os.OpenFile(dbPath, os.O_RDONLY, 0444)
	if err != nil {
		return nil, nil, err
	}
	defer f.Close()

	// The meta page is just 64 bytes, and definitely less than 1024 bytes,
	// so it's fine to only read 1024 bytes. Note we don't care about the
	// pageSize when reading the first meta page, because we always read the
	// file starting from offset 0. Actually the passed pageSize is 0 when
	// reading the first meta page in the `surgery meta update` command.
	buf := make([]byte, 1024)
	n, err := f.ReadAt(buf, int64(metaPageId*pageSize))
	if n == len(buf) && (err == nil || err == io.EOF) {
		return common.LoadPageMeta(buf), buf, nil
	}

	return nil, nil, err
}

func writeMetaPageAt(dbPath string, buf []byte, metaPageId uint32, pageSize uint32) error {
	if metaPageId > 1 {
		return fmt.Errorf("invalid metaPageId: %d", metaPageId)
	}

	f, err := os.OpenFile(dbPath, os.O_RDWR, 0666)
	if err != nil {
		return err
	}
	defer f.Close()

	n, err := f.WriteAt(buf, int64(metaPageId*pageSize))
	if n == len(buf) && (err == nil || err == io.EOF) {
		return nil
	}

	return err
}
```

## File: `cmd/bbolt/command/command_surgery_meta_test.go`
```go
package command_test

import (
	"fmt"
	"path/filepath"
	"strings"
	"testing"

	"github.com/stretchr/testify/require"

	bolt "go.etcd.io/bbolt"
	"go.etcd.io/bbolt/cmd/bbolt/command"
	"go.etcd.io/bbolt/internal/btesting"
	"go.etcd.io/bbolt/internal/common"
)

func TestSurgery_Meta_Validate(t *testing.T) {
	pageSize := 4096
	db := btesting.MustCreateDBWithOption(t, &bolt.Options{PageSize: pageSize})
	srcPath := db.Path()

	defer requireDBNoChange(t, dbData(t, db.Path()), db.Path())

	// validate the meta pages
	rootCmd := command.NewRootCommand()
	rootCmd.SetArgs([]string{
		"surgery", "meta", "validate", srcPath,
	})
	err := rootCmd.Execute()
	require.NoError(t, err)

	// TODD: add one more case that the validation may fail. We need to
	// make the command output configurable, so that test cases can set
	// a customized io.Writer.
}

func TestSurgery_Meta_Update(t *testing.T) {
	testCases := []struct {
		name     string
		root     common.Pgid
		freelist common.Pgid
		pgid     common.Pgid
	}{
		{
			name: "root changed",
			root: 50,
		},
		{
			name:     "freelist changed",
			freelist: 40,
		},
		{
			name: "pgid changed",
			pgid: 600,
		},
		{
			name:     "both root and freelist changed",
			root:     45,
			freelist: 46,
		},
		{
			name:     "both pgid and freelist changed",
			pgid:     256,
			freelist: 47,
		},
		{
			name:     "all fields changed",
			root:     43,
			freelist: 62,
			pgid:     256,
		},
	}

	for _, tc := range testCases {
		for i := 0; i <= 1; i++ {
			tc := tc
			metaPageId := uint32(i)

			t.Run(tc.name, func(t *testing.T) {
				pageSize := 4096
				db := btesting.MustCreateDBWithOption(t, &bolt.Options{PageSize: pageSize})
				srcPath := db.Path()

				defer requireDBNoChange(t, dbData(t, db.Path()), db.Path())

				var fields []string
				if tc.root != 0 {
					fields = append(fields, fmt.Sprintf("root:%d", tc.root))
				}
				if tc.freelist != 0 {
					fields = append(fields, fmt.Sprintf("freelist:%d", tc.freelist))
				}
				if tc.pgid != 0 {
					fields = append(fields, fmt.Sprintf("pgid:%d", tc.pgid))
				}

				rootCmd := command.NewRootCommand()
				output := filepath.Join(t.TempDir(), "db")
				rootCmd.SetArgs([]string{
					"surgery", "meta", "update", srcPath,
					"--output", output,
					"--meta-page", fmt.Sprintf("%d", metaPageId),
					"--fields", strings.Join(fields, ","),
				})
				err := rootCmd.Execute()
				require.NoError(t, err)

				m, _, err := command.ReadMetaPageAt(output, metaPageId, 4096)
				require.NoError(t, err)

				require.Equal(t, common.Magic, m.Magic())
				require.Equal(t, common.Version, m.Version())

				if tc.root != 0 {
					require.Equal(t, tc.root, m.RootBucket().RootPage())
				}
				if tc.freelist != 0 {
					require.Equal(t, tc.freelist, m.Freelist())
				}
				if tc.pgid != 0 {
					require.Equal(t, tc.pgid, m.Pgid())
				}
			})
		}
	}
}
```

## File: `cmd/bbolt/command/command_surgery_test.go`
```go
package command_test

import (
	"fmt"
	"os"
	"path/filepath"
	"testing"

	"github.com/stretchr/testify/assert"
	"github.com/stretchr/testify/require"

	bolt "go.etcd.io/bbolt"
	"go.etcd.io/bbolt/cmd/bbolt/command"
	"go.etcd.io/bbolt/internal/btesting"
	"go.etcd.io/bbolt/internal/common"
	"go.etcd.io/bbolt/internal/guts_cli"
)

func TestSurgery_RevertMetaPage(t *testing.T) {
	pageSize := 4096
	db := btesting.MustCreateDBWithOption(t, &bolt.Options{PageSize: pageSize})
	srcPath := db.Path()

	defer requireDBNoChange(t, dbData(t, db.Path()), db.Path())

	srcFile, err := os.Open(srcPath)
	require.NoError(t, err)
	defer srcFile.Close()

	// Read both meta0 and meta1 from srcFile
	srcBuf0 := readPage(t, srcPath, 0, pageSize)
	srcBuf1 := readPage(t, srcPath, 1, pageSize)
	meta0Page := common.LoadPageMeta(srcBuf0)
	meta1Page := common.LoadPageMeta(srcBuf1)

	// Get the non-active meta page
	nonActiveSrcBuf := srcBuf0
	nonActiveMetaPageId := 0
	if meta0Page.Txid() > meta1Page.Txid() {
		nonActiveSrcBuf = srcBuf1
		nonActiveMetaPageId = 1
	}
	t.Logf("non active meta page id: %d", nonActiveMetaPageId)

	// revert the meta page
	rootCmd := command.NewRootCommand()
	output := filepath.Join(t.TempDir(), "db")
	rootCmd.SetArgs([]string{
		"surgery", "revert-meta-page", srcPath,
		"--output", output,
	})
	err = rootCmd.Execute()
	require.NoError(t, err)

	// read both meta0 and meta1 from dst file
	dstBuf0 := readPage(t, output, 0, pageSize)
	dstBuf1 := readPage(t, output, 1, pageSize)

	// check result. Note we should skip the page ID
	assert.Equal(t, pageDataWithoutPageId(nonActiveSrcBuf), pageDataWithoutPageId(dstBuf0))
	assert.Equal(t, pageDataWithoutPageId(nonActiveSrcBuf), pageDataWithoutPageId(dstBuf1))
}

func TestSurgery_CopyPage(t *testing.T) {
	pageSize := 4096
	db := btesting.MustCreateDBWithOption(t, &bolt.Options{PageSize: pageSize})
	srcPath := db.Path()

	// Insert some sample data
	t.Log("Insert some sample data")
	err := db.Fill([]byte("data"), 1, 20,
		func(tx int, k int) []byte { return []byte(fmt.Sprintf("%04d", k)) },
		func(tx int, k int) []byte { return make([]byte, 10) },
	)
	require.NoError(t, err)

	defer requireDBNoChange(t, dbData(t, srcPath), srcPath)

	// copy page 3 to page 2
	t.Log("copy page 3 to page 2")
	rootCmd := command.NewRootCommand()
	output := filepath.Join(t.TempDir(), "dstdb")
	rootCmd.SetArgs([]string{
		"surgery", "copy-page", srcPath,
		"--output", output,
		"--from-page", "3",
		"--to-page", "2",
	})
	err = rootCmd.Execute()
	require.NoError(t, err)

	// The page 2 should have exactly the same data as page 3.
	t.Log("Verify result")
	srcPageId3Data := readPage(t, srcPath, 3, pageSize)
	dstPageId3Data := readPage(t, output, 3, pageSize)
	dstPageId2Data := readPage(t, output, 2, pageSize)

	assert.Equal(t, srcPageId3Data, dstPageId3Data)
	assert.Equal(t, pageDataWithoutPageId(srcPageId3Data), pageDataWithoutPageId(dstPageId2Data))
}

// TODO(ahrtr): add test case below for `surgery clear-page` command:
//  1. The page is a branch page. All its children should become free pages.
func TestSurgery_ClearPage(t *testing.T) {
	pageSize := 4096
	db := btesting.MustCreateDBWithOption(t, &bolt.Options{PageSize: pageSize})
	srcPath := db.Path()

	// Insert some sample data
	t.Log("Insert some sample data")
	err := db.Fill([]byte("data"), 1, 20,
		func(tx int, k int) []byte { return []byte(fmt.Sprintf("%04d", k)) },
		func(tx int, k int) []byte { return make([]byte, 10) },
	)
	require.NoError(t, err)

	defer requireDBNoChange(t, dbData(t, srcPath), srcPath)

	// clear page 3
	t.Log("clear page 3")
	rootCmd := command.NewRootCommand()
	output := filepath.Join(t.TempDir(), "dstdb")
	rootCmd.SetArgs([]string{
		"surgery", "clear-page", srcPath,
		"--output", output,
		"--pageId", "3",
	})
	err = rootCmd.Execute()
	require.NoError(t, err)

	t.Log("Verify result")
	dstPageId3Data := readPage(t, output, 3, pageSize)

	p := common.LoadPage(dstPageId3Data)
	assert.Equal(t, uint16(0), p.Count())
	assert.Equal(t, uint32(0), p.Overflow())
}

func TestSurgery_ClearPageElements_Without_Overflow(t *testing.T) {
	testCases := []struct {
		name                 string
		from                 int
		to                   int
		isBranchPage         bool
		setEndIdxAsCount     bool
		removeOnlyOneElement bool // only valid when setEndIdxAsCount == true, and startIdx = endIdx -1 in this case.
		expectError          bool
	}{
		// normal range in leaf page
		{
			name: "normal range in leaf page: [4, 8)",
			from: 4,
			to:   8,
		},
		{
			name: "normal range in leaf page: [5, -1)",
			from: 4,
			to:   -1,
		},
		{
			name: "normal range in leaf page: all",
			from: 0,
			to:   -1,
		},
		{
			name: "normal range in leaf page: [0, 7)",
			from: 0,
			to:   7,
		},
		{
			name:             "normal range in leaf page: [3, count)",
			from:             4,
			setEndIdxAsCount: true,
		},
		// normal range in branch page
		{
			name:         "normal range in branch page: [4, 8)",
			from:         4,
			to:           8,
			isBranchPage: true,
		},
		{
			name:         "normal range in branch page: [5, -1)",
			from:         4,
			to:           -1,
			isBranchPage: true,
		},
		{
			name:         "normal range in branch page: all",
			from:         0,
			to:           -1,
			isBranchPage: true,
		},
		{
			name:         "normal range in branch page: [0, 7)",
			from:         0,
			to:           7,
			isBranchPage: true,
		},
		{
			name:             "normal range in branch page: [3, count)",
			from:             4,
			isBranchPage:     true,
			setEndIdxAsCount: true,
		},
		// remove only one element
		{
			name: "one element: the first one",
			from: 0,
			to:   1,
		},
		{
			name: "one element: [6, 7)",
			from: 6,
			to:   7,
		},
		{
			name:                 "one element: the last one",
			setEndIdxAsCount:     true,
			removeOnlyOneElement: true,
		},
		// abnormal range
		{
			name:        "abnormal range: [-1, 4)",
			from:        -1,
			to:          4,
			expectError: true,
		},
		{
			name:        "abnormal range: [-2, 5)",
			from:        -1,
			to:          5,
			expectError: true,
		},
		{
			name:        "abnormal range: [3, 3)",
			from:        3,
			to:          3,
			expectError: true,
		},
		{
			name:        "abnormal range: [5, 3)",
			from:        5,
			to:          3,
			expectError: true,
		},
		{
			name:        "abnormal range: [3, -2)",
			from:        3,
			to:          -2,
			expectError: true,
		},
		{
			name:        "abnormal range: [3, 1000000)",
			from:        -1,
			to:          4,
			expectError: true,
		},
	}
	for _, tc := range testCases {
		tc := tc
		t.Run(tc.name, func(t *testing.T) {
			testSurgeryClearPageElementsWithoutOverflow(t, tc.from, tc.to, tc.isBranchPage, tc.setEndIdxAsCount, tc.removeOnlyOneElement, tc.expectError)
		})
	}
}

func testSurgeryClearPageElementsWithoutOverflow(t *testing.T, startIdx, endIdx int, isBranchPage, setEndIdxAsCount, removeOnlyOne, expectError bool) {
	pageSize := 4096
	db := btesting.MustCreateDBWithOption(t, &bolt.Options{PageSize: pageSize})
	srcPath := db.Path()

	// Generate sample db
	t.Log("Generate some sample data")
	err := db.Fill([]byte("data"), 10, 200,
		func(tx int, k int) []byte { return []byte(fmt.Sprintf("%04d", tx*10000+k)) },
		func(tx int, k int) []byte { return make([]byte, 10) },
	)
	require.NoError(t, err)

	defer requireDBNoChange(t, dbData(t, srcPath), srcPath)

	// find a page with at least 10 elements
	var (
		pageId       uint64 = 2
		elementCount uint16 = 0
	)
	for {
		p, _, err := guts_cli.ReadPage(srcPath, pageId)
		require.NoError(t, err)

		if isBranchPage {
			if p.IsBranchPage() && p.Count() > 10 {
				elementCount = p.Count()
				break
			}
		} else {
			if p.IsLeafPage() && p.Count() > 10 {
				elementCount = p.Count()
				break
			}
		}
		pageId++
	}
	t.Logf("The original element count: %d", elementCount)

	if setEndIdxAsCount {
		t.Logf("Set the endIdx as the element count: %d", elementCount)
		endIdx = int(elementCount)
		if removeOnlyOne {
			startIdx = endIdx - 1
			t.Logf("Set the startIdx as the endIdx-1: %d", startIdx)
		}
	}

	// clear elements [startIdx, endIdx) in the page
	rootCmd := command.NewRootCommand()
	output := filepath.Join(t.TempDir(), "db")
	rootCmd.SetArgs([]string{
		"surgery", "clear-page-elements", srcPath,
		"--output", output,
		"--pageId", fmt.Sprintf("%d", pageId),
		"--from-index", fmt.Sprintf("%d", startIdx),
		"--to-index", fmt.Sprintf("%d", endIdx),
	})
	err = rootCmd.Execute()
	if expectError {
		require.Error(t, err)
		return
	}

	require.NoError(t, err)

	// check the element count again
	expectedCnt := 0
	if endIdx == -1 {
		expectedCnt = startIdx
	} else {
		expectedCnt = int(elementCount) - (endIdx - startIdx)
	}
	p, _, err := guts_cli.ReadPage(output, pageId)
	require.NoError(t, err)
	assert.Equal(t, expectedCnt, int(p.Count()))

	compareDataAfterClearingElement(t, srcPath, output, pageId, isBranchPage, startIdx, endIdx)
}

func compareDataAfterClearingElement(t *testing.T, srcPath, dstPath string, pageId uint64, isBranchPage bool, startIdx, endIdx int) {
	srcPage, _, err := guts_cli.ReadPage(srcPath, pageId)
	require.NoError(t, err)

	dstPage, _, err := guts_cli.ReadPage(dstPath, pageId)
	require.NoError(t, err)

	var dstIdx uint16
	for i := uint16(0); i < srcPage.Count(); i++ {
		// skip the cleared elements
		if dstIdx >= uint16(startIdx) && (dstIdx < uint16(endIdx) || endIdx == -1) {
			continue
		}

		if isBranchPage {
			srcElement := srcPage.BranchPageElement(i)
			dstElement := dstPage.BranchPageElement(dstIdx)

			require.Equal(t, srcElement.Key(), dstElement.Key())
			require.Equal(t, srcElement.Pgid(), dstElement.Pgid())
		} else {
			srcElement := srcPage.LeafPageElement(i)
			dstElement := dstPage.LeafPageElement(dstIdx)

			require.Equal(t, srcElement.Flags(), dstElement.Flags())
			require.Equal(t, srcElement.Key(), dstElement.Key())
			require.Equal(t, srcElement.Value(), dstElement.Value())
		}

		dstIdx++
	}
}

func TestSurgery_ClearPageElements_With_Overflow(t *testing.T) {
	testCases := []struct {
		name             string
		from             int
		to               int
		valueSizes       []int
		expectedOverflow int
	}{
		// big element
		{
			name:             "remove a big element at the end",
			valueSizes:       []int{500, 500, 500, 2600},
			from:             3,
			to:               4,
			expectedOverflow: 0,
		},
		{
			name:             "remove a big element at the begin",
			valueSizes:       []int{2600, 500, 500, 500},
			from:             0,
			to:               1,
			expectedOverflow: 0,
		},
		{
			name:             "remove a big element in the middle",
			valueSizes:       []int{500, 2600, 500, 500},
			from:             1,
			to:               2,
			expectedOverflow: 0,
		},
		// small element
		{
			name:             "remove a small element at the end",
			valueSizes:       []int{500, 500, 3100, 100},
			from:             3,
			to:               4,
			expectedOverflow: 1,
		},
		{
			name:             "remove a small element at the begin",
			valueSizes:       []int{100, 500, 3100, 500},
			from:             0,
			to:               1,
			expectedOverflow: 1,
		},
		{
			name:             "remove a small element in the middle",
			valueSizes:       []int{500, 100, 3100, 500},
			from:             1,
			to:               2,
			expectedOverflow: 1,
		},
		{
			name:             "remove a small element at the end of page with big overflow",
			valueSizes:       []int{500, 500, 4096 * 5, 100},
			from:             3,
			to:               4,
			expectedOverflow: 5,
		},
		{
			name:             "remove a small element at the begin of page with big overflow",
			valueSizes:       []int{100, 500, 4096 * 6, 500},
			from:             0,
			to:               1,
			expectedOverflow: 6,
		},
		{
			name:             "remove a small element in the middle of page with big overflow",
			valueSizes:       []int{500, 100, 4096 * 4, 500},
			from:             1,
			to:               2,
			expectedOverflow: 4,
		},
		// huge element
		{
			name:             "remove a huge element at the end",
			valueSizes:       []int{500, 500, 500, 4096 * 5},
			from:             3,
			to:               4,
			expectedOverflow: 0,
		},
		{
			name:             "remove a huge element at the begin",
			valueSizes:       []int{4096 * 5, 500, 500, 500},
			from:             0,
			to:               1,
			expectedOverflow: 0,
		},
		{
			name:             "remove a huge element in the middle",
			valueSizes:       []int{500, 4096 * 5, 500, 500},
			from:             1,
			to:               2,
			expectedOverflow: 0,
		},
	}

	for _, tc := range testCases {
		tc := tc

		t.Run(tc.name, func(t *testing.T) {
			testSurgeryClearPageElementsWithOverflow(t, tc.from, tc.to, tc.valueSizes, tc.expectedOverflow)
		})
	}
}

func testSurgeryClearPageElementsWithOverflow(t *testing.T, startIdx, endIdx int, valueSizes []int, expectedOverflow int) {
	pageSize := 4096
	db := btesting.MustCreateDBWithOption(t, &bolt.Options{PageSize: pageSize})
	srcPath := db.Path()

	// Generate sample db
	err := db.Update(func(tx *bolt.Tx) error {
		b, _ := tx.CreateBucketIfNotExists([]byte("data"))
		for i, valueSize := range valueSizes {
			key := []byte(fmt.Sprintf("%04d", i))
			val := make([]byte, valueSize)
			if putErr := b.Put(key, val); putErr != nil {
				return putErr
			}
		}
		return nil
	})
	require.NoError(t, err)

	defer requireDBNoChange(t, dbData(t, srcPath), srcPath)

	// find a page with overflow pages
	var (
		pageId       uint64 = 2
		elementCount uint16 = 0
	)
	for {
		p, _, err := guts_cli.ReadPage(srcPath, pageId)
		require.NoError(t, err)

		if p.Overflow() > 0 {
			elementCount = p.Count()
			break
		}
		pageId++
	}
	t.Logf("The original element count: %d", elementCount)

	// clear elements [startIdx, endIdx) in the page
	rootCmd := command.NewRootCommand()
	output := filepath.Join(t.TempDir(), "db")
	rootCmd.SetArgs([]string{
		"surgery", "clear-page-elements", srcPath,
		"--output", output,
		"--pageId", fmt.Sprintf("%d", pageId),
		"--from-index", fmt.Sprintf("%d", startIdx),
		"--to-index", fmt.Sprintf("%d", endIdx),
	})
	err = rootCmd.Execute()
	require.NoError(t, err)

	// check the element count again
	expectedCnt := 0
	if endIdx == -1 {
		expectedCnt = startIdx
	} else {
		expectedCnt = int(elementCount) - (endIdx - startIdx)
	}
	p, _, err := guts_cli.ReadPage(output, pageId)
	require.NoError(t, err)
	assert.Equal(t, expectedCnt, int(p.Count()))

	assert.Equal(t, expectedOverflow, int(p.Overflow()))

	compareDataAfterClearingElement(t, srcPath, output, pageId, false, startIdx, endIdx)
}

func TestSurgeryRequiredFlags(t *testing.T) {
	errMsgFmt := `required flag(s) "%s" not set`
	testCases := []struct {
		name           string
		args           []string
		expectedErrMsg string
	}{
		// --output is required for all surgery commands
		{
			name:           "no output flag for revert-meta-page",
			args:           []string{"surgery", "revert-meta-page", "db"},
			expectedErrMsg: fmt.Sprintf(errMsgFmt, "output"),
		},
		{
			name:           "no output flag for copy-page",
			args:           []string{"surgery", "copy-page", "db", "--from-page", "3", "--to-page", "2"},
			expectedErrMsg: fmt.Sprintf(errMsgFmt, "output"),
		},
		{
			name:           "no output flag for clear-page",
			args:           []string{"surgery", "clear-page", "db", "--pageId", "3"},
			expectedErrMsg: fmt.Sprintf(errMsgFmt, "output"),
		},
		{
			name:           "no output flag for clear-page-element",
			args:           []string{"surgery", "clear-page-elements", "db", "--pageId", "4", "--from-index", "3", "--to-index", "5"},
			expectedErrMsg: fmt.Sprintf(errMsgFmt, "output"),
		},
		{
			name:           "no output flag for freelist abandon",
			args:           []string{"surgery", "freelist", "abandon", "db"},
			expectedErrMsg: fmt.Sprintf(errMsgFmt, "output"),
		},
		{
			name:           "no output flag for freelist rebuild",
			args:           []string{"surgery", "freelist", "rebuild", "db"},
			expectedErrMsg: fmt.Sprintf(errMsgFmt, "output"),
		},
		// --from-page and --to-page are required for 'surgery copy-page' command
		{
			name:           "no from-page flag for copy-page",
			args:           []string{"surgery", "copy-page", "db", "--output", "db", "--to-page", "2"},
			expectedErrMsg: fmt.Sprintf(errMsgFmt, "from-page"),
		},
		{
			name:           "no to-page flag for copy-page",
			args:           []string{"surgery", "copy-page", "db", "--output", "db", "--from-page", "2"},
			expectedErrMsg: fmt.Sprintf(errMsgFmt, "to-page"),
		},
		// --pageId is required for 'surgery clear-page' command
		{
			name:           "no pageId flag for clear-page",
			args:           []string{"surgery", "clear-page", "db", "--output", "db"},
			expectedErrMsg: fmt.Sprintf(errMsgFmt, "pageId"),
		},
		// --pageId, --from-index and --to-index are required for 'surgery clear-page-element' command
		{
			name:           "no pageId flag for clear-page-element",
			args:           []string{"surgery", "clear-page-elements", "db", "--output", "newdb", "--from-index", "3", "--to-index", "5"},
			expectedErrMsg: fmt.Sprintf(errMsgFmt, "pageId"),
		},
		{
			name:           "no from-index flag for clear-page-element",
			args:           []string{"surgery", "clear-page-elements", "db", "--output", "newdb", "--pageId", "2", "--to-index", "5"},
			expectedErrMsg: fmt.Sprintf(errMsgFmt, "from-index"),
		},
		{
			name:           "no to-index flag for clear-page-element",
			args:           []string{"surgery", "clear-page-elements", "db", "--output", "newdb", "--pageId", "2", "--from-index", "3"},
			expectedErrMsg: fmt.Sprintf(errMsgFmt, "to-index"),
		},
	}

	for _, tc := range testCases {
		tc := tc
		t.Run(tc.name, func(t *testing.T) {
			rootCmd := command.NewRootCommand()
			rootCmd.SetArgs(tc.args)
			err := rootCmd.Execute()
			require.ErrorContains(t, err, tc.expectedErrMsg)
		})
	}
}
```

## File: `cmd/bbolt/command/command_version.go`
```go
package command

import (
	"fmt"
	"runtime"

	"github.com/spf13/cobra"

	"go.etcd.io/bbolt/version"
)

func newVersionCommand() *cobra.Command {
	versionCmd := &cobra.Command{
		Use:   "version",
		Short: "print the current version of bbolt",
		Long:  "print the current version of bbolt",
		Run: func(cmd *cobra.Command, args []string) {
			fmt.Printf("bbolt Version: %s\n", version.Version)
			fmt.Printf("Go Version: %s\n", runtime.Version())
			fmt.Printf("Go OS/Arch: %s/%s\n", runtime.GOOS, runtime.GOARCH)
		},
	}

	return versionCmd
}
```

## File: `cmd/bbolt/command/errors.go`
```go
package command

import "errors"

var (
	// ErrBatchInvalidWriteMode is returned when the write mode is other than seq, rnd, seq-nest, or rnd-nest.
	ErrBatchInvalidWriteMode = errors.New("the write mode should be one of seq, rnd, seq-nest, or rnd-nest")

	// ErrBatchNonDivisibleBatchSize is returned when the batch size can't be evenly
	// divided by the iteration count.
	ErrBatchNonDivisibleBatchSize = errors.New("the number of iterations must be divisible by the batch size")

	// ErrBucketRequired is returned when a bucket is not specified.
	ErrBucketRequired = errors.New("bucket required")

	// ErrInvalidPageArgs is returned when Page cmd receives pageIds and all option is true.
	ErrInvalidPageArgs = errors.New("invalid args: either use '--all' or 'pageid...'")

	// ErrInvalidValue is returned when a benchmark reads an unexpected value.
	ErrInvalidValue = errors.New("invalid value")

	// ErrKeyNotFound is returned when a key is not found.
	ErrKeyNotFound = errors.New("key not found")

	// ErrPageIDRequired is returned when a required page id is not specified.
	ErrPageIDRequired = errors.New("page id required")

	// ErrPathRequired is returned when the path to a bbolt database is not specified.
	ErrPathRequired = errors.New("path required")

	// ErrSurgeryFreelistAlreadyExist is returned when a bbolt database file already has a freelist.
	ErrSurgeryFreelistAlreadyExist = errors.New("the file already has freelist, please consider to abandon the freelist to forcibly rebuild it")
)
```

## File: `cmd/bbolt/command/utils.go`
```go
package command

import (
	"crypto/sha256"
	"encoding/hex"
	"fmt"
	"io"
	"os"
	"strconv"
	"unicode"
	"unicode/utf8"

	bolt "go.etcd.io/bbolt"
	berrors "go.etcd.io/bbolt/errors"
)

func checkSourceDBPath(srcPath string) (os.FileInfo, error) {
	fi, err := os.Stat(srcPath)
	if os.IsNotExist(err) {
		return nil, fmt.Errorf("source database file %q doesn't exist", srcPath)
	} else if err != nil {
		return nil, fmt.Errorf("failed to open source database file %q: %v", srcPath, err)
	}
	return fi, nil
}

const FORMAT_MODES = "auto|ascii-encoded|hex|bytes|redacted"

// formatBytes converts bytes into string according to format.
// Supported formats: ascii-encoded, hex, bytes.
func formatBytes(b []byte, format string) (string, error) {
	switch format {
	case "ascii-encoded":
		return fmt.Sprintf("%q", b), nil
	case "hex":
		return fmt.Sprintf("%x", b), nil
	case "bytes":
		return string(b), nil
	case "auto":
		return bytesToAsciiOrHex(b), nil
	case "redacted":
		hash := sha256.New()
		hash.Write(b)
		return fmt.Sprintf("<redacted len:%d sha256:%x>", len(b), hash.Sum(nil)), nil
	default:
		return "", fmt.Errorf("formatBytes: unsupported format: %s", format)
	}
}

func parseBytes(str string, format string) ([]byte, error) {
	switch format {
	case "ascii-encoded":
		return []byte(str), nil
	case "hex":
		return hex.DecodeString(str)
	default:
		return nil, fmt.Errorf("parseBytes: unsupported format: %s", format)
	}
}

// writelnBytes writes the byte to the writer. Supported formats: ascii-encoded, hex, bytes, auto, redacted.
// Terminates the write with a new line symbol;
func writelnBytes(w io.Writer, b []byte, format string) error {
	str, err := formatBytes(b, format)
	if err != nil {
		return err
	}
	_, err = fmt.Fprintln(w, str)
	return err
}

// isPrintable returns true if the string is valid unicode and contains only printable runes.
func isPrintable(s string) bool {
	if !utf8.ValidString(s) {
		return false
	}
	for _, ch := range s {
		if !unicode.IsPrint(ch) {
			return false
		}
	}
	return true
}

func bytesToAsciiOrHex(b []byte) string {
	sb := string(b)
	if isPrintable(sb) {
		return sb
	} else {
		return hex.EncodeToString(b)
	}
}

func stringToPage(str string) (uint64, error) {
	return strconv.ParseUint(str, 10, 64)
}

// stringToPages parses a slice of strings into page ids.
func stringToPages(strs []string) ([]uint64, error) {
	var a []uint64
	for _, str := range strs {
		if len(str) == 0 {
			continue
		}
		i, err := stringToPage(str)
		if err != nil {
			return nil, err
		}
		a = append(a, i)
	}
	return a, nil
}

type cmdKvStringer struct{}

func (cmdKvStringer) KeyToString(key []byte) string {
	return bytesToAsciiOrHex(key)
}

func (cmdKvStringer) ValueToString(value []byte) string {
	return bytesToAsciiOrHex(value)
}

func CmdKvStringer() bolt.KVStringer {
	return cmdKvStringer{}
}

func findLastBucket(tx *bolt.Tx, bucketNames []string) (*bolt.Bucket, error) {
	lastbucket := tx.Bucket([]byte(bucketNames[0]))
	if lastbucket == nil {
		return nil, berrors.ErrBucketNotFound
	}
	for _, bucket := range bucketNames[1:] {
		lastbucket = lastbucket.Bucket([]byte(bucket))
		if lastbucket == nil {
			return nil, berrors.ErrBucketNotFound
		}
	}
	return lastbucket, nil
}
```

## File: `cmd/bbolt/command/utils_test.go`
```go
package command_test

import (
	"bytes"
	crypto "crypto/rand"
	"encoding/binary"
	"encoding/hex"
	"fmt"
	"io"
	"math/rand"
	"os"
	"strings"
	"sync"
	"testing"

	"github.com/stretchr/testify/require"

	bolt "go.etcd.io/bbolt"
	"go.etcd.io/bbolt/internal/common"
	"go.etcd.io/bbolt/internal/guts_cli"
)

func loadMetaPage(t *testing.T, dbPath string, pageID uint64) *common.Meta {
	_, buf, err := guts_cli.ReadPage(dbPath, pageID)
	require.NoError(t, err)
	return common.LoadPageMeta(buf)
}

func readMetaPage(t *testing.T, path string) *common.Meta {
	_, activeMetaPageId, err := guts_cli.GetRootPage(path)
	require.NoError(t, err)
	_, buf, err := guts_cli.ReadPage(path, uint64(activeMetaPageId))
	require.NoError(t, err)
	return common.LoadPageMeta(buf)
}

func readPage(t *testing.T, path string, pageId int, pageSize int) []byte {
	dbFile, err := os.Open(path)
	require.NoError(t, err)
	defer dbFile.Close()

	fi, err := dbFile.Stat()
	require.NoError(t, err)
	require.GreaterOrEqual(t, fi.Size(), int64((pageId+1)*pageSize))

	buf := make([]byte, pageSize)
	byteRead, err := dbFile.ReadAt(buf, int64(pageId*pageSize))
	require.NoError(t, err)
	require.Equal(t, pageSize, byteRead)

	return buf
}

func pageDataWithoutPageId(buf []byte) []byte {
	return buf[8:]
}

type ConcurrentBuffer struct {
	m   sync.Mutex
	buf bytes.Buffer
}

func (b *ConcurrentBuffer) Read(p []byte) (n int, err error) {
	b.m.Lock()
	defer b.m.Unlock()

	return b.buf.Read(p)
}

func (b *ConcurrentBuffer) Write(p []byte) (n int, err error) {
	b.m.Lock()
	defer b.m.Unlock()

	return b.buf.Write(p)
}

func (b *ConcurrentBuffer) String() string {
	b.m.Lock()
	defer b.m.Unlock()

	return b.buf.String()
}

func fillBucket(b *bolt.Bucket, prefix []byte) error {
	n := 10 + rand.Intn(50)
	for i := 0; i < n; i++ {
		v := make([]byte, 10*(1+rand.Intn(4)))
		_, err := crypto.Read(v)
		if err != nil {
			return err
		}
		k := append(prefix, []byte(fmt.Sprintf("k%d", i))...)
		if err := b.Put(k, v); err != nil {
			return err
		}
	}
	// limit depth of subbuckets
	s := 2 + rand.Intn(4)
	if len(prefix) > (2*s + 1) {
		return nil
	}
	n = 1 + rand.Intn(3)
	for i := 0; i < n; i++ {
		k := append(prefix, []byte(fmt.Sprintf("b%d", i))...)
		sb, err := b.CreateBucket(k)
		if err != nil {
			return err
		}
		if err := fillBucket(sb, append(k, '.')); err != nil {
			return err
		}
	}
	return nil
}

func chkdb(path string) ([]byte, error) {
	db, err := bolt.Open(path, 0600, &bolt.Options{ReadOnly: true})
	if err != nil {
		return nil, err
	}
	defer db.Close()
	var buf bytes.Buffer
	err = db.View(func(tx *bolt.Tx) error {
		return tx.ForEach(func(name []byte, b *bolt.Bucket) error {
			return walkBucket(b, name, nil, &buf)
		})
	})
	if err != nil {
		return nil, err
	}
	return buf.Bytes(), nil
}

func walkBucket(parent *bolt.Bucket, k []byte, v []byte, w io.Writer) error {
	if _, err := fmt.Fprintf(w, "%d:%x=%x\n", parent.Sequence(), k, v); err != nil {
		return err
	}

	// not a bucket, exit.
	if v != nil {
		return nil
	}
	return parent.ForEach(func(k, v []byte) error {
		if v == nil {
			return walkBucket(parent.Bucket(k), k, nil, w)
		}
		return walkBucket(parent, k, v, w)
	})
}

func dbData(t *testing.T, filePath string) []byte {
	data, err := os.ReadFile(filePath)
	require.NoError(t, err)
	return data
}

func requireDBNoChange(t *testing.T, oldData []byte, filePath string) {
	newData, err := os.ReadFile(filePath)
	require.NoError(t, err)

	noChange := bytes.Equal(oldData, newData)
	require.True(t, noChange)
}

func convertInt64IntoBytes(num int64) []byte {
	buf := make([]byte, binary.MaxVarintLen64)
	n := binary.PutVarint(buf, num)
	return buf[:n]
}

func convertInt64KeysIntoHexString(nums ...int64) string {
	var res []string
	for _, num := range nums {
		res = append(res, hex.EncodeToString(convertInt64IntoBytes(num)))
	}
	return strings.Join(res, "\n") + "\n" // last newline char
}
```

## File: `errors/errors.go`
```go
// Package errors defines the error variables that may be returned
// during bbolt operations.
package errors

import "errors"

// These errors can be returned when opening or calling methods on a DB.
var (
	// ErrDatabaseNotOpen is returned when a DB instance is accessed before it
	// is opened or after it is closed.
	ErrDatabaseNotOpen = errors.New("database not open")

	// ErrInvalid is returned when both meta pages on a database are invalid.
	// This typically occurs when a file is not a bolt database.
	ErrInvalid = errors.New("invalid database")

	// ErrInvalidMapping is returned when the database file fails to get mapped.
	ErrInvalidMapping = errors.New("database isn't correctly mapped")

	// ErrVersionMismatch is returned when the data file was created with a
	// different version of Bolt.
	ErrVersionMismatch = errors.New("version mismatch")

	// ErrChecksum is returned when a checksum mismatch occurs on either of the two meta pages.
	ErrChecksum = errors.New("checksum error")

	// ErrTimeout is returned when a database cannot obtain an exclusive lock
	// on the data file after the timeout passed to Open().
	ErrTimeout = errors.New("timeout")
)

// These errors can occur when beginning or committing a Tx.
var (
	// ErrTxNotWritable is returned when performing a write operation on a
	// read-only transaction.
	ErrTxNotWritable = errors.New("tx not writable")

	// ErrTxClosed is returned when committing or rolling back a transaction
	// that has already been committed or rolled back.
	ErrTxClosed = errors.New("tx closed")

	// ErrDatabaseReadOnly is returned when a mutating transaction is started on a
	// read-only database.
	ErrDatabaseReadOnly = errors.New("database is in read-only mode")

	// ErrFreePagesNotLoaded is returned when a readonly transaction without
	// preloading the free pages is trying to access the free pages.
	ErrFreePagesNotLoaded = errors.New("free pages are not pre-loaded")
)

// These errors can occur when putting or deleting a value or a bucket.
var (
	// ErrBucketNotFound is returned when trying to access a bucket that has
	// not been created yet.
	ErrBucketNotFound = errors.New("bucket not found")

	// ErrBucketExists is returned when creating a bucket that already exists.
	ErrBucketExists = errors.New("bucket already exists")

	// ErrBucketNameRequired is returned when creating a bucket with a blank name.
	ErrBucketNameRequired = errors.New("bucket name required")

	// ErrKeyRequired is returned when inserting a zero-length key.
	ErrKeyRequired = errors.New("key required")

	// ErrKeyTooLarge is returned when inserting a key that is larger than MaxKeySize.
	ErrKeyTooLarge = errors.New("key too large")

	// ErrValueTooLarge is returned when inserting a value that is larger than MaxValueSize.
	ErrValueTooLarge = errors.New("value too large")

	// ErrMaxSizeReached is returned when the configured maximum size of the data file is reached.
	ErrMaxSizeReached = errors.New("database reached maximum size")

	// ErrIncompatibleValue is returned when trying to create or delete a bucket
	// on an existing non-bucket key or when trying to create or delete a
	// non-bucket key on an existing bucket key.
	ErrIncompatibleValue = errors.New("incompatible value")

	// ErrSameBuckets is returned when trying to move a sub-bucket between
	// source and target buckets, while source and target buckets are the same.
	ErrSameBuckets = errors.New("the source and target are the same bucket")

	// ErrDifferentDB is returned when trying to move a sub-bucket between
	// source and target buckets, while source and target buckets are in different database files.
	ErrDifferentDB = errors.New("the source and target buckets are in different database files")
)
```

## File: `internal/btesting/btesting.go`
```go
package btesting

import (
	"flag"
	"fmt"
	"os"
	"path/filepath"
	"regexp"
	"strings"
	"testing"
	"time"

	"github.com/stretchr/testify/require"

	bolt "go.etcd.io/bbolt"
)

var statsFlag = flag.Bool("stats", false, "show performance stats")

const (
	// TestFreelistType is used as an env variable for test to indicate the backend type.
	TestFreelistType = "TEST_FREELIST_TYPE"
	// TestEnableStrictMode is used to enable strict check by default after opening each DB.
	TestEnableStrictMode = "TEST_ENABLE_STRICT_MODE"
)

// DB is a test wrapper for bolt.DB.
type DB struct {
	*bolt.DB
	f string
	o *bolt.Options
	t testing.TB
}

// MustCreateDB returns a new, open DB at a temporary location.
func MustCreateDB(t testing.TB) *DB {
	return MustCreateDBWithOption(t, nil)
}

// MustCreateDBWithOption returns a new, open DB at a temporary location with given options.
func MustCreateDBWithOption(t testing.TB, o *bolt.Options) *DB {
	f := filepath.Join(t.TempDir(), "db")
	return MustOpenDBWithOption(t, f, o)
}

func MustOpenDBWithOption(t testing.TB, f string, o *bolt.Options) *DB {
	db, err := OpenDBWithOption(t, f, o)
	require.NoError(t, err)
	require.NotNil(t, db)
	return db
}

func OpenDBWithOption(t testing.TB, f string, o *bolt.Options) (*DB, error) {
	t.Logf("Opening bbolt DB at: %s", f)
	if o == nil {
		o = bolt.DefaultOptions
	}

	freelistType := bolt.FreelistArrayType
	if env := os.Getenv(TestFreelistType); env == string(bolt.FreelistMapType) {
		freelistType = bolt.FreelistMapType
	}

	o.FreelistType = freelistType

	db, err := bolt.Open(f, 0600, o)
	if err != nil {
		return nil, err
	}
	resDB := &DB{
		DB: db,
		f:  f,
		o:  o,
		t:  t,
	}
	resDB.strictModeEnabledDefault()
	t.Cleanup(resDB.PostTestCleanup)
	return resDB, nil
}

func (db *DB) PostTestCleanup() {
	// Check database consistency after every test.
	if db.DB != nil {
		db.MustCheck()
		db.MustClose()
	}
}

// Close closes the database but does NOT delete the underlying file.
func (db *DB) Close() error {
	if db.DB != nil {
		// Log statistics.
		if *statsFlag {
			db.PrintStats()
		}
		db.t.Logf("Closing bbolt DB at: %s", db.f)
		err := db.DB.Close()
		if err != nil {
			return err
		}
		db.DB = nil
	}
	return nil
}

// MustClose closes the database but does NOT delete the underlying file.
func (db *DB) MustClose() {
	err := db.Close()
	require.NoError(db.t, err)
}

func (db *DB) MustDeleteFile() {
	err := os.Remove(db.Path())
	require.NoError(db.t, err)
}

func (db *DB) SetOptions(o *bolt.Options) {
	db.o = o
}

// MustReopen reopen the database. Panic on error.
func (db *DB) MustReopen() {
	if db.DB != nil {
		panic("Please call Close() before MustReopen()")
	}
	db.t.Logf("Reopening bbolt DB at: %s", db.f)
	indb, err := bolt.Open(db.Path(), 0600, db.o)
	require.NoError(db.t, err)
	db.DB = indb
	db.strictModeEnabledDefault()
}

// MustCheck runs a consistency check on the database and panics if any errors are found.
func (db *DB) MustCheck() {
	err := db.View(func(tx *bolt.Tx) error {
		// Collect all the errors.
		var errors []error
		for err := range tx.Check() {
			errors = append(errors, err)
			if len(errors) > 10 {
				break
			}
		}

		// If errors occurred, copy the DB and print the errors.
		if len(errors) > 0 {
			var path = filepath.Join(db.t.TempDir(), "db.backup")
			err := tx.CopyFile(path, 0600)
			require.NoError(db.t, err)

			// Print errors.
			fmt.Print("\n\n")
			fmt.Printf("consistency check failed (%d errors)\n", len(errors))
			for _, err := range errors {
				fmt.Println(err)
			}
			fmt.Println("")
			fmt.Println("db saved to:")
			fmt.Println(path)
			fmt.Print("\n\n")
			os.Exit(-1)
		}

		return nil
	})
	require.NoError(db.t, err)
}

// Fill - fills the DB using numTx transactions and numKeysPerTx.
func (db *DB) Fill(bucket []byte, numTx int, numKeysPerTx int,
	keyGen func(tx int, key int) []byte,
	valueGen func(tx int, key int) []byte) error {
	for tr := 0; tr < numTx; tr++ {
		err := db.Update(func(tx *bolt.Tx) error {
			b, _ := tx.CreateBucketIfNotExists(bucket)
			for i := 0; i < numKeysPerTx; i++ {
				if err := b.Put(keyGen(tr, i), valueGen(tr, i)); err != nil {
					return err
				}
			}
			return nil
		})
		if err != nil {
			return err
		}
	}
	return nil
}

func (db *DB) Path() string {
	return db.f
}

// CopyTempFile copies a database to a temporary file.
func (db *DB) CopyTempFile() {
	path := filepath.Join(db.t.TempDir(), "db.copy")
	err := db.View(func(tx *bolt.Tx) error {
		return tx.CopyFile(path, 0600)
	})
	require.NoError(db.t, err)
	fmt.Println("db copied to: ", path)
}

// PrintStats prints the database stats
func (db *DB) PrintStats() {
	var stats = db.Stats()
	fmt.Printf("[db] %-20s %-20s %-20s\n",
		fmt.Sprintf("pg(%d/%d)", stats.TxStats.GetPageCount(), stats.TxStats.GetPageAlloc()),
		fmt.Sprintf("cur(%d)", stats.TxStats.GetCursorCount()),
		fmt.Sprintf("node(%d/%d)", stats.TxStats.GetNodeCount(), stats.TxStats.GetNodeDeref()),
	)
	fmt.Printf("     %-20s %-20s %-20s\n",
		fmt.Sprintf("rebal(%d/%v)", stats.TxStats.GetRebalance(), truncDuration(stats.TxStats.GetRebalanceTime())),
		fmt.Sprintf("spill(%d/%v)", stats.TxStats.GetSpill(), truncDuration(stats.TxStats.GetSpillTime())),
		fmt.Sprintf("w(%d/%v)", stats.TxStats.GetWrite(), truncDuration(stats.TxStats.GetWriteTime())),
	)
}

func truncDuration(d time.Duration) string {
	return regexp.MustCompile(`^(\d+)(\.\d+)`).ReplaceAllString(d.String(), "$1")
}

func (db *DB) strictModeEnabledDefault() {
	strictModeEnabled := strings.ToLower(os.Getenv(TestEnableStrictMode))
	db.StrictMode = strictModeEnabled == "true"
}

func (db *DB) ForceDisableStrictMode() {
	db.StrictMode = false
}
```

## File: `internal/common/bolt_386.go`
```go
package common

// MaxMapSize represents the largest mmap size supported by Bolt.
const MaxMapSize = 0x7FFFFFFF // 2GB

// MaxAllocSize is the size used when creating array pointers.
const MaxAllocSize = 0xFFFFFFF
```

## File: `internal/common/bolt_amd64.go`
```go
package common

// MaxMapSize represents the largest mmap size supported by Bolt.
const MaxMapSize = 0xFFFFFFFFFFFF // 256TB

// MaxAllocSize is the size used when creating array pointers.
const MaxAllocSize = 0x7FFFFFFF
```

## File: `internal/common/bolt_arm.go`
```go
package common

// MaxMapSize represents the largest mmap size supported by Bolt.
const MaxMapSize = 0x7FFFFFFF // 2GB

// MaxAllocSize is the size used when creating array pointers.
const MaxAllocSize = 0xFFFFFFF
```

## File: `internal/common/bolt_arm64.go`
```go
//go:build arm64

package common

// MaxMapSize represents the largest mmap size supported by Bolt.
const MaxMapSize = 0xFFFFFFFFFFFF // 256TB

// MaxAllocSize is the size used when creating array pointers.
const MaxAllocSize = 0x7FFFFFFF
```

## File: `internal/common/bolt_loong64.go`
```go
//go:build loong64

package common

// MaxMapSize represents the largest mmap size supported by Bolt.
const MaxMapSize = 0xFFFFFFFFFFFF // 256TB

// MaxAllocSize is the size used when creating array pointers.
const MaxAllocSize = 0x7FFFFFFF
```

## File: `internal/common/bolt_mips64x.go`
```go
//go:build mips64 || mips64le

package common

// MaxMapSize represents the largest mmap size supported by Bolt.
const MaxMapSize = 0x8000000000 // 512GB

// MaxAllocSize is the size used when creating array pointers.
const MaxAllocSize = 0x7FFFFFFF
```

## File: `internal/common/bolt_mipsx.go`
```go
//go:build mips || mipsle

package common

// MaxMapSize represents the largest mmap size supported by Bolt.
const MaxMapSize = 0x40000000 // 1GB

// MaxAllocSize is the size used when creating array pointers.
const MaxAllocSize = 0xFFFFFFF
```

## File: `internal/common/bolt_ppc.go`
```go
//go:build ppc

package common

// MaxMapSize represents the largest mmap size supported by Bolt.
const MaxMapSize = 0x7FFFFFFF // 2GB

// MaxAllocSize is the size used when creating array pointers.
const MaxAllocSize = 0xFFFFFFF
```

## File: `internal/common/bolt_ppc64.go`
```go
//go:build ppc64

package common

// MaxMapSize represents the largest mmap size supported by Bolt.
const MaxMapSize = 0xFFFFFFFFFFFF // 256TB

// MaxAllocSize is the size used when creating array pointers.
const MaxAllocSize = 0x7FFFFFFF
```

## File: `internal/common/bolt_ppc64le.go`
```go
//go:build ppc64le

package common

// MaxMapSize represents the largest mmap size supported by Bolt.
const MaxMapSize = 0xFFFFFFFFFFFF // 256TB

// MaxAllocSize is the size used when creating array pointers.
const MaxAllocSize = 0x7FFFFFFF
```

## File: `internal/common/bolt_riscv64.go`
```go
//go:build riscv64

package common

// MaxMapSize represents the largest mmap size supported by Bolt.
const MaxMapSize = 0xFFFFFFFFFFFF // 256TB

// MaxAllocSize is the size used when creating array pointers.
const MaxAllocSize = 0x7FFFFFFF
```

## File: `internal/common/bolt_s390x.go`
```go
//go:build s390x

package common

// MaxMapSize represents the largest mmap size supported by Bolt.
const MaxMapSize = 0xFFFFFFFFFFFF // 256TB

// MaxAllocSize is the size used when creating array pointers.
const MaxAllocSize = 0x7FFFFFFF
```

## File: `internal/common/bucket.go`
```go
package common

import (
	"fmt"
	"unsafe"
)

const BucketHeaderSize = int(unsafe.Sizeof(InBucket{}))

// InBucket represents the on-file representation of a bucket.
// This is stored as the "value" of a bucket key. If the bucket is small enough,
// then its root page can be stored inline in the "value", after the bucket
// header. In the case of inline buckets, the "root" will be 0.
type InBucket struct {
	root     Pgid   // page id of the bucket's root-level page
	sequence uint64 // monotonically incrementing, used by NextSequence()
}

func NewInBucket(root Pgid, seq uint64) InBucket {
	return InBucket{
		root:     root,
		sequence: seq,
	}
}

func (b *InBucket) RootPage() Pgid {
	return b.root
}

func (b *InBucket) SetRootPage(id Pgid) {
	b.root = id
}

// InSequence returns the sequence. The reason why not naming it `Sequence`
// is to avoid duplicated name as `(*Bucket) Sequence()`
func (b *InBucket) InSequence() uint64 {
	return b.sequence
}

func (b *InBucket) SetInSequence(v uint64) {
	b.sequence = v
}

func (b *InBucket) IncSequence() {
	b.sequence++
}

func (b *InBucket) InlinePage(v []byte) *Page {
	return (*Page)(unsafe.Pointer(&v[BucketHeaderSize]))
}

func (b *InBucket) String() string {
	return fmt.Sprintf("<pgid=%d,seq=%d>", b.root, b.sequence)
}
```

## File: `internal/common/inode.go`
```go
package common

import "unsafe"

// Inode represents an internal node inside of a node.
// It can be used to point to elements in a page or point
// to an element which hasn't been added to a page yet.
type Inode struct {
	flags uint32
	pgid  Pgid
	key   []byte
	value []byte
}

type Inodes []Inode

func (in *Inode) Flags() uint32 {
	return in.flags
}

func (in *Inode) SetFlags(flags uint32) {
	in.flags = flags
}

func (in *Inode) Pgid() Pgid {
	return in.pgid
}

func (in *Inode) SetPgid(id Pgid) {
	in.pgid = id
}

func (in *Inode) Key() []byte {
	return in.key
}

func (in *Inode) SetKey(key []byte) {
	in.key = key
}

func (in *Inode) Value() []byte {
	return in.value
}

func (in *Inode) SetValue(value []byte) {
	in.value = value
}

func ReadInodeFromPage(p *Page) Inodes {
	inodes := make(Inodes, int(p.Count()))
	isLeaf := p.IsLeafPage()
	for i := 0; i < int(p.Count()); i++ {
		inode := &inodes[i]
		if isLeaf {
			elem := p.LeafPageElement(uint16(i))
			inode.SetFlags(elem.Flags())
			inode.SetKey(elem.Key())
			inode.SetValue(elem.Value())
		} else {
			elem := p.BranchPageElement(uint16(i))
			inode.SetPgid(elem.Pgid())
			inode.SetKey(elem.Key())
		}
		Assert(len(inode.Key()) > 0, "read: zero-length inode key")
	}

	return inodes
}

func WriteInodeToPage(inodes Inodes, p *Page) uint32 {
	// Loop over each item and write it to the page.
	// off tracks the offset into p of the start of the next data.
	off := unsafe.Sizeof(*p) + p.PageElementSize()*uintptr(len(inodes))
	isLeaf := p.IsLeafPage()
	for i, item := range inodes {
		Assert(len(item.Key()) > 0, "write: zero-length inode key")

		// Create a slice to write into of needed size and advance
		// byte pointer for next iteration.
		sz := len(item.Key()) + len(item.Value())
		b := UnsafeByteSlice(unsafe.Pointer(p), off, 0, sz)
		off += uintptr(sz)

		// Write the page element.
		if isLeaf {
			elem := p.LeafPageElement(uint16(i))
			elem.SetPos(uint32(uintptr(unsafe.Pointer(&b[0])) - uintptr(unsafe.Pointer(elem))))
			elem.SetFlags(item.Flags())
			elem.SetKsize(uint32(len(item.Key())))
			elem.SetVsize(uint32(len(item.Value())))
		} else {
			elem := p.BranchPageElement(uint16(i))
			elem.SetPos(uint32(uintptr(unsafe.Pointer(&b[0])) - uintptr(unsafe.Pointer(elem))))
			elem.SetKsize(uint32(len(item.Key())))
			elem.SetPgid(item.Pgid())
			Assert(elem.Pgid() != p.Id(), "write: circular dependency occurred")
		}

		// Write data for the element to the end of the page.
		l := copy(b, item.Key())
		copy(b[l:], item.Value())
	}

	return uint32(off)
}

func UsedSpaceInPage(inodes Inodes, p *Page) uint32 {
	off := unsafe.Sizeof(*p) + p.PageElementSize()*uintptr(len(inodes))
	for _, item := range inodes {
		sz := len(item.Key()) + len(item.Value())
		off += uintptr(sz)
	}

	return uint32(off)
}
```

## File: `internal/common/meta.go`
```go
package common

import (
	"fmt"
	"hash/fnv"
	"io"
	"unsafe"

	"go.etcd.io/bbolt/errors"
)

type Meta struct {
	magic    uint32
	version  uint32
	pageSize uint32
	flags    uint32
	root     InBucket
	freelist Pgid
	pgid     Pgid
	txid     Txid
	checksum uint64
}

// Validate checks the marker bytes and version of the meta page to ensure it matches this binary.
func (m *Meta) Validate() error {
	if m.magic != Magic {
		return errors.ErrInvalid
	} else if m.version != Version {
		return errors.ErrVersionMismatch
	} else if m.checksum != m.Sum64() {
		return errors.ErrChecksum
	}
	return nil
}

// Copy copies one meta object to another.
func (m *Meta) Copy(dest *Meta) {
	*dest = *m
}

// Write writes the meta onto a page.
func (m *Meta) Write(p *Page) {
	if m.root.root >= m.pgid {
		panic(fmt.Sprintf("root bucket pgid (%d) above high water mark (%d)", m.root.root, m.pgid))
	} else if m.freelist >= m.pgid && m.freelist != PgidNoFreelist {
		// TODO: reject pgidNoFreeList if !NoFreelistSync
		panic(fmt.Sprintf("freelist pgid (%d) above high water mark (%d)", m.freelist, m.pgid))
	}

	// Page id is either going to be 0 or 1 which we can determine by the transaction ID.
	p.id = Pgid(m.txid % 2)
	p.SetFlags(MetaPageFlag)

	// Calculate the checksum.
	m.checksum = m.Sum64()

	m.Copy(p.Meta())
}

// Sum64 generates the checksum for the meta.
func (m *Meta) Sum64() uint64 {
	var h = fnv.New64a()
	_, _ = h.Write((*[unsafe.Offsetof(Meta{}.checksum)]byte)(unsafe.Pointer(m))[:])
	return h.Sum64()
}

func (m *Meta) Magic() uint32 {
	return m.magic
}

func (m *Meta) SetMagic(v uint32) {
	m.magic = v
}

func (m *Meta) Version() uint32 {
	return m.version
}

func (m *Meta) SetVersion(v uint32) {
	m.version = v
}

func (m *Meta) PageSize() uint32 {
	return m.pageSize
}

func (m *Meta) SetPageSize(v uint32) {
	m.pageSize = v
}

func (m *Meta) Flags() uint32 {
	return m.flags
}

func (m *Meta) SetFlags(v uint32) {
	m.flags = v
}

func (m *Meta) SetRootBucket(b InBucket) {
	m.root = b
}

func (m *Meta) RootBucket() *InBucket {
	return &m.root
}

func (m *Meta) Freelist() Pgid {
	return m.freelist
}

func (m *Meta) SetFreelist(v Pgid) {
	m.freelist = v
}

func (m *Meta) IsFreelistPersisted() bool {
	return m.freelist != PgidNoFreelist
}

func (m *Meta) Pgid() Pgid {
	return m.pgid
}

func (m *Meta) SetPgid(id Pgid) {
	m.pgid = id
}

func (m *Meta) Txid() Txid {
	return m.txid
}

func (m *Meta) SetTxid(id Txid) {
	m.txid = id
}

func (m *Meta) IncTxid() {
	m.txid += 1
}

func (m *Meta) DecTxid() {
	m.txid -= 1
}

func (m *Meta) Checksum() uint64 {
	return m.checksum
}

func (m *Meta) SetChecksum(v uint64) {
	m.checksum = v
}

func (m *Meta) Print(w io.Writer) {
	fmt.Fprintf(w, "Version:    %d\n", m.version)
	fmt.Fprintf(w, "Page Size:  %d bytes\n", m.pageSize)
	fmt.Fprintf(w, "Flags:      %08x\n", m.flags)
	fmt.Fprintf(w, "Root:       <pgid=%d>\n", m.root.root)
	fmt.Fprintf(w, "Freelist:   <pgid=%d>\n", m.freelist)
	fmt.Fprintf(w, "HWM:        <pgid=%d>\n", m.pgid)
	fmt.Fprintf(w, "Txn ID:     %d\n", m.txid)
	fmt.Fprintf(w, "Checksum:   %016x\n", m.checksum)
	fmt.Fprintf(w, "\n")
}
```

## File: `internal/common/page.go`
```go
package common

import (
	"fmt"
	"os"
	"sort"
	"unsafe"
)

const PageHeaderSize = unsafe.Sizeof(Page{})

const MinKeysPerPage = 2

const BranchPageElementSize = unsafe.Sizeof(branchPageElement{})
const LeafPageElementSize = unsafe.Sizeof(leafPageElement{})
const pgidSize = unsafe.Sizeof(Pgid(0))

const (
	BranchPageFlag   = 0x01
	LeafPageFlag     = 0x02
	MetaPageFlag     = 0x04
	FreelistPageFlag = 0x10
)

const (
	BucketLeafFlag = 0x01
)

type Pgid uint64

type Page struct {
	id       Pgid
	flags    uint16
	count    uint16
	overflow uint32
}

func NewPage(id Pgid, flags, count uint16, overflow uint32) *Page {
	return &Page{
		id:       id,
		flags:    flags,
		count:    count,
		overflow: overflow,
	}
}

// Typ returns a human-readable page type string used for debugging.
func (p *Page) Typ() string {
	if p.IsBranchPage() {
		return "branch"
	} else if p.IsLeafPage() {
		return "leaf"
	} else if p.IsMetaPage() {
		return "meta"
	} else if p.IsFreelistPage() {
		return "freelist"
	}
	return fmt.Sprintf("unknown<%02x>", p.flags)
}

func (p *Page) IsBranchPage() bool {
	return p.flags == BranchPageFlag
}

func (p *Page) IsLeafPage() bool {
	return p.flags == LeafPageFlag
}

func (p *Page) IsMetaPage() bool {
	return p.flags == MetaPageFlag
}

func (p *Page) IsFreelistPage() bool {
	return p.flags == FreelistPageFlag
}

// Meta returns a pointer to the metadata section of the page.
func (p *Page) Meta() *Meta {
	return (*Meta)(UnsafeAdd(unsafe.Pointer(p), unsafe.Sizeof(*p)))
}

func (p *Page) FastCheck(id Pgid) {
	Assert(p.id == id, "Page expected to be: %v, but self identifies as %v", id, p.id)
	// Only one flag of page-type can be set.
	Assert(p.IsBranchPage() ||
		p.IsLeafPage() ||
		p.IsMetaPage() ||
		p.IsFreelistPage(),
		"page %v: has unexpected type/flags: %x", p.id, p.flags)
}

// LeafPageElement retrieves the leaf node by index
func (p *Page) LeafPageElement(index uint16) *leafPageElement {
	return (*leafPageElement)(UnsafeIndex(unsafe.Pointer(p), unsafe.Sizeof(*p),
		LeafPageElementSize, int(index)))
}

// LeafPageElements retrieves a list of leaf nodes.
func (p *Page) LeafPageElements() []leafPageElement {
	if p.count == 0 {
		return nil
	}
	data := UnsafeAdd(unsafe.Pointer(p), unsafe.Sizeof(*p))
	elems := unsafe.Slice((*leafPageElement)(data), int(p.count))
	return elems
}

// BranchPageElement retrieves the branch node by index
func (p *Page) BranchPageElement(index uint16) *branchPageElement {
	return (*branchPageElement)(UnsafeIndex(unsafe.Pointer(p), unsafe.Sizeof(*p),
		unsafe.Sizeof(branchPageElement{}), int(index)))
}

// BranchPageElements retrieves a list of branch nodes.
func (p *Page) BranchPageElements() []branchPageElement {
	if p.count == 0 {
		return nil
	}
	data := UnsafeAdd(unsafe.Pointer(p), unsafe.Sizeof(*p))
	elems := unsafe.Slice((*branchPageElement)(data), int(p.count))
	return elems
}

func (p *Page) FreelistPageCount() (int, int) {
	Assert(p.IsFreelistPage(), fmt.Sprintf("can't get freelist page count from a non-freelist page: %2x", p.flags))

	// If the page.count is at the max uint16 value (64k) then it's considered
	// an overflow and the size of the freelist is stored as the first element.
	var idx, count = 0, int(p.count)
	if count == 0xFFFF {
		idx = 1
		c := *(*Pgid)(UnsafeAdd(unsafe.Pointer(p), unsafe.Sizeof(*p)))
		count = int(c)
		if count < 0 {
			panic(fmt.Sprintf("leading element count %d overflows int", c))
		}
	}

	return idx, count
}

func (p *Page) FreelistPageIds() []Pgid {
	Assert(p.IsFreelistPage(), fmt.Sprintf("can't get freelist page IDs from a non-freelist page: %2x", p.flags))

	idx, count := p.FreelistPageCount()

	if count == 0 {
		return nil
	}

	data := UnsafeIndex(unsafe.Pointer(p), unsafe.Sizeof(*p), pgidSize, idx)
	ids := unsafe.Slice((*Pgid)(data), count)

	return ids
}

// dump writes n bytes of the page to STDERR as hex output.
func (p *Page) hexdump(n int) {
	buf := UnsafeByteSlice(unsafe.Pointer(p), 0, 0, n)
	fmt.Fprintf(os.Stderr, "%x\n", buf)
}

func (p *Page) PageElementSize() uintptr {
	if p.IsLeafPage() {
		return LeafPageElementSize
	}
	return BranchPageElementSize
}

func (p *Page) Id() Pgid {
	return p.id
}

func (p *Page) SetId(target Pgid) {
	p.id = target
}

func (p *Page) Flags() uint16 {
	return p.flags
}

func (p *Page) SetFlags(v uint16) {
	p.flags = v
}

func (p *Page) Count() uint16 {
	return p.count
}

func (p *Page) SetCount(target uint16) {
	p.count = target
}

func (p *Page) Overflow() uint32 {
	return p.overflow
}

func (p *Page) SetOverflow(target uint32) {
	p.overflow = target
}

func (p *Page) String() string {
	return fmt.Sprintf("ID: %d, Type: %s, count: %d, overflow: %d", p.id, p.Typ(), p.count, p.overflow)
}

type Pages []*Page

func (s Pages) Len() int           { return len(s) }
func (s Pages) Swap(i, j int)      { s[i], s[j] = s[j], s[i] }
func (s Pages) Less(i, j int) bool { return s[i].id < s[j].id }

// branchPageElement represents a node on a branch page.
type branchPageElement struct {
	pos   uint32
	ksize uint32
	pgid  Pgid
}

func (n *branchPageElement) Pos() uint32 {
	return n.pos
}

func (n *branchPageElement) SetPos(v uint32) {
	n.pos = v
}

func (n *branchPageElement) Ksize() uint32 {
	return n.ksize
}

func (n *branchPageElement) SetKsize(v uint32) {
	n.ksize = v
}

func (n *branchPageElement) Pgid() Pgid {
	return n.pgid
}

func (n *branchPageElement) SetPgid(v Pgid) {
	n.pgid = v
}

// Key returns a byte slice of the node key.
func (n *branchPageElement) Key() []byte {
	return UnsafeByteSlice(unsafe.Pointer(n), 0, int(n.pos), int(n.pos)+int(n.ksize))
}

// leafPageElement represents a node on a leaf page.
type leafPageElement struct {
	flags uint32
	pos   uint32
	ksize uint32
	vsize uint32
}

func NewLeafPageElement(flags, pos, ksize, vsize uint32) *leafPageElement {
	return &leafPageElement{
		flags: flags,
		pos:   pos,
		ksize: ksize,
		vsize: vsize,
	}
}

func (n *leafPageElement) Flags() uint32 {
	return n.flags
}

func (n *leafPageElement) SetFlags(v uint32) {
	n.flags = v
}

func (n *leafPageElement) Pos() uint32 {
	return n.pos
}

func (n *leafPageElement) SetPos(v uint32) {
	n.pos = v
}

func (n *leafPageElement) Ksize() uint32 {
	return n.ksize
}

func (n *leafPageElement) SetKsize(v uint32) {
	n.ksize = v
}

func (n *leafPageElement) Vsize() uint32 {
	return n.vsize
}

func (n *leafPageElement) SetVsize(v uint32) {
	n.vsize = v
}

// Key returns a byte slice of the node key.
func (n *leafPageElement) Key() []byte {
	i := int(n.pos)
	j := i + int(n.ksize)
	return UnsafeByteSlice(unsafe.Pointer(n), 0, i, j)
}

// Value returns a byte slice of the node value.
func (n *leafPageElement) Value() []byte {
	i := int(n.pos) + int(n.ksize)
	j := i + int(n.vsize)
	return UnsafeByteSlice(unsafe.Pointer(n), 0, i, j)
}

func (n *leafPageElement) IsBucketEntry() bool {
	return n.flags&uint32(BucketLeafFlag) != 0
}

func (n *leafPageElement) Bucket() *InBucket {
	if n.IsBucketEntry() {
		return LoadBucket(n.Value())
	} else {
		return nil
	}
}

// PageInfo represents human readable information about a page.
type PageInfo struct {
	ID            int
	Type          string
	Count         int
	OverflowCount int
}

type Pgids []Pgid

func (s Pgids) Len() int           { return len(s) }
func (s Pgids) Swap(i, j int)      { s[i], s[j] = s[j], s[i] }
func (s Pgids) Less(i, j int) bool { return s[i] < s[j] }

// Merge returns the sorted union of a and b.
func (s Pgids) Merge(b Pgids) Pgids {
	// Return the opposite slice if one is nil.
	if len(s) == 0 {
		return b
	}
	if len(b) == 0 {
		return s
	}
	merged := make(Pgids, len(s)+len(b))
	Mergepgids(merged, s, b)
	return merged
}

// Mergepgids copies the sorted union of a and b into dst.
// If dst is too small, it panics.
func Mergepgids(dst, a, b Pgids) {
	if len(dst) < len(a)+len(b) {
		panic(fmt.Errorf("mergepgids bad len %d < %d + %d", len(dst), len(a), len(b)))
	}
	// Copy in the opposite slice if one is nil.
	if len(a) == 0 {
		copy(dst, b)
		return
	}
	if len(b) == 0 {
		copy(dst, a)
		return
	}

	// Merged will hold all elements from both lists.
	merged := dst[:0]

	// Assign lead to the slice with a lower starting value, follow to the higher value.
	lead, follow := a, b
	if b[0] < a[0] {
		lead, follow = b, a
	}

	// Continue while there are elements in the lead.
	for len(lead) > 0 {
		// Merge largest prefix of lead that is ahead of follow[0].
		n := sort.Search(len(lead), func(i int) bool { return lead[i] > follow[0] })
		merged = append(merged, lead[:n]...)
		if n >= len(lead) {
			break
		}

		// Swap lead and follow.
		lead, follow = follow, lead[n:]
	}

	// Append what's left in follow.
	_ = append(merged, follow...)
}
```

## File: `internal/common/page_test.go`
```go
package common

import (
	"reflect"
	"sort"
	"testing"
	"testing/quick"
)

// Ensure that the page type can be returned in human readable format.
func TestPage_typ(t *testing.T) {
	if typ := (&Page{flags: BranchPageFlag}).Typ(); typ != "branch" {
		t.Fatalf("exp=branch; got=%v", typ)
	}
	if typ := (&Page{flags: LeafPageFlag}).Typ(); typ != "leaf" {
		t.Fatalf("exp=leaf; got=%v", typ)
	}
	if typ := (&Page{flags: MetaPageFlag}).Typ(); typ != "meta" {
		t.Fatalf("exp=meta; got=%v", typ)
	}
	if typ := (&Page{flags: FreelistPageFlag}).Typ(); typ != "freelist" {
		t.Fatalf("exp=freelist; got=%v", typ)
	}
	if typ := (&Page{flags: 20000}).Typ(); typ != "unknown<4e20>" {
		t.Fatalf("exp=unknown<4e20>; got=%v", typ)
	}
}

// Ensure that the hexdump debugging function doesn't blow up.
func TestPage_dump(t *testing.T) {
	(&Page{id: 256}).hexdump(16)
}

func TestPgids_merge(t *testing.T) {
	a := Pgids{4, 5, 6, 10, 11, 12, 13, 27}
	b := Pgids{1, 3, 8, 9, 25, 30}
	c := a.Merge(b)
	if !reflect.DeepEqual(c, Pgids{1, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 25, 27, 30}) {
		t.Errorf("mismatch: %v", c)
	}

	a = Pgids{4, 5, 6, 10, 11, 12, 13, 27, 35, 36}
	b = Pgids{8, 9, 25, 30}
	c = a.Merge(b)
	if !reflect.DeepEqual(c, Pgids{4, 5, 6, 8, 9, 10, 11, 12, 13, 25, 27, 30, 35, 36}) {
		t.Errorf("mismatch: %v", c)
	}
}

func TestPgids_merge_quick(t *testing.T) {
	if err := quick.Check(func(a, b Pgids) bool {
		// Sort incoming lists.
		sort.Sort(a)
		sort.Sort(b)

		// Merge the two lists together.
		got := a.Merge(b)

		// The expected value should be the two lists combined and sorted.
		exp := append(a, b...)
		sort.Sort(exp)

		if !reflect.DeepEqual(exp, got) {
			t.Errorf("\nexp=%+v\ngot=%+v\n", exp, got)
			return false
		}

		return true
	}, nil); err != nil {
		t.Fatal(err)
	}
}
```

## File: `internal/common/types.go`
```go
package common

import (
	"os"
	"runtime"
	"time"
)

// MaxMmapStep is the largest step that can be taken when remapping the mmap.
const MaxMmapStep = 1 << 30 // 1GB

// Version represents the data file format version.
const Version uint32 = 2

// Magic represents a marker value to indicate that a file is a Bolt DB.
const Magic uint32 = 0xED0CDAED

const PgidNoFreelist Pgid = 0xffffffffffffffff

// IgnoreNoSync specifies whether the NoSync field of a DB is ignored when
// syncing changes to a file.  This is required as some operating systems,
// such as OpenBSD, do not have a unified buffer cache (UBC) and writes
// must be synchronized using the msync(2) syscall.
const IgnoreNoSync = runtime.GOOS == "openbsd"

// Default values if not set in a DB instance.
const (
	DefaultMaxBatchSize  int = 1000
	DefaultMaxBatchDelay     = 10 * time.Millisecond
	DefaultAllocSize         = 16 * 1024 * 1024
)

// DefaultPageSize is the default page size for db which is set to the OS page size.
var DefaultPageSize = os.Getpagesize()

// Txid represents the internal transaction identifier.
type Txid uint64
```

## File: `internal/common/unsafe.go`
```go
package common

import (
	"unsafe"
)

func UnsafeAdd(base unsafe.Pointer, offset uintptr) unsafe.Pointer {
	return unsafe.Pointer(uintptr(base) + offset)
}

func UnsafeIndex(base unsafe.Pointer, offset uintptr, elemsz uintptr, n int) unsafe.Pointer {
	return unsafe.Pointer(uintptr(base) + offset + uintptr(n)*elemsz)
}

func UnsafeByteSlice(base unsafe.Pointer, offset uintptr, i, j int) []byte {
	// See: https://github.com/golang/go/wiki/cgo#turning-c-arrays-into-go-slices
	//
	// This memory is not allocated from C, but it is unmanaged by Go's
	// garbage collector and should behave similarly, and the compiler
	// should produce similar code.  Note that this conversion allows a
	// subslice to begin after the base address, with an optional offset,
	// while the URL above does not cover this case and only slices from
	// index 0.  However, the wiki never says that the address must be to
	// the beginning of a C allocation (or even that malloc was used at
	// all), so this is believed to be correct.
	return (*[MaxAllocSize]byte)(UnsafeAdd(base, offset))[i:j:j]
}
```

## File: `internal/common/utils.go`
```go
package common

import (
	"fmt"
	"io"
	"os"
	"unsafe"
)

func LoadBucket(buf []byte) *InBucket {
	return (*InBucket)(unsafe.Pointer(&buf[0]))
}

func LoadPage(buf []byte) *Page {
	return (*Page)(unsafe.Pointer(&buf[0]))
}

func LoadPageMeta(buf []byte) *Meta {
	return (*Meta)(unsafe.Pointer(&buf[PageHeaderSize]))
}

func CopyFile(srcPath, dstPath string) error {
	// Ensure source file exists.
	_, err := os.Stat(srcPath)
	if os.IsNotExist(err) {
		return fmt.Errorf("source file %q not found", srcPath)
	} else if err != nil {
		return err
	}

	// Ensure output file not exist.
	_, err = os.Stat(dstPath)
	if err == nil {
		return fmt.Errorf("output file %q already exists", dstPath)
	} else if !os.IsNotExist(err) {
		return err
	}

	srcDB, err := os.Open(srcPath)
	if err != nil {
		return fmt.Errorf("failed to open source file %q: %w", srcPath, err)
	}
	defer srcDB.Close()
	dstDB, err := os.Create(dstPath)
	if err != nil {
		return fmt.Errorf("failed to create output file %q: %w", dstPath, err)
	}
	defer dstDB.Close()
	written, err := io.Copy(dstDB, srcDB)
	if err != nil {
		return fmt.Errorf("failed to copy database file from %q to %q: %w", srcPath, dstPath, err)
	}

	srcFi, err := srcDB.Stat()
	if err != nil {
		return fmt.Errorf("failed to get source file info %q: %w", srcPath, err)
	}
	initialSize := srcFi.Size()
	if initialSize != written {
		return fmt.Errorf("the byte copied (%q: %d) isn't equal to the initial db size (%q: %d)", dstPath, written, srcPath, initialSize)
	}

	return nil
}
```

## File: `internal/common/verify.go`
```go
// Copied from https://github.com/etcd-io/etcd/blob/main/client/pkg/verify/verify.go
package common

import (
	"fmt"
	"os"
	"strings"
)

const ENV_VERIFY = "BBOLT_VERIFY"

type VerificationType string

const (
	ENV_VERIFY_VALUE_ALL    VerificationType = "all"
	ENV_VERIFY_VALUE_ASSERT VerificationType = "assert"
)

func getEnvVerify() string {
	return strings.ToLower(os.Getenv(ENV_VERIFY))
}

func IsVerificationEnabled(verification VerificationType) bool {
	env := getEnvVerify()
	return env == string(ENV_VERIFY_VALUE_ALL) || env == strings.ToLower(string(verification))
}

// EnableVerifications sets `ENV_VERIFY` and returns a function that
// can be used to bring the original settings.
func EnableVerifications(verification VerificationType) func() {
	previousEnv := getEnvVerify()
	os.Setenv(ENV_VERIFY, string(verification))
	return func() {
		os.Setenv(ENV_VERIFY, previousEnv)
	}
}

// EnableAllVerifications enables verification and returns a function
// that can be used to bring the original settings.
func EnableAllVerifications() func() {
	return EnableVerifications(ENV_VERIFY_VALUE_ALL)
}

// DisableVerifications unsets `ENV_VERIFY` and returns a function that
// can be used to bring the original settings.
func DisableVerifications() func() {
	previousEnv := getEnvVerify()
	os.Unsetenv(ENV_VERIFY)
	return func() {
		os.Setenv(ENV_VERIFY, previousEnv)
	}
}

// Verify performs verification if the assertions are enabled.
// In the default setup running in tests and skipped in the production code.
func Verify(f func()) {
	if IsVerificationEnabled(ENV_VERIFY_VALUE_ASSERT) {
		f()
	}
}

// Assert will panic with a given formatted message if the given condition is false.
func Assert(condition bool, msg string, v ...any) {
	if !condition {
		panic(fmt.Sprintf("assertion failed: "+msg, v...))
	}
}
```

## File: `internal/freelist/array.go`
```go
package freelist

import (
	"fmt"
	"sort"

	"go.etcd.io/bbolt/internal/common"
)

type array struct {
	*shared

	ids []common.Pgid // all free and available free page ids.
}

func (f *array) Init(ids common.Pgids) {
	f.ids = ids
	f.reindex()
}

func (f *array) Allocate(txid common.Txid, n int) common.Pgid {
	if len(f.ids) == 0 {
		return 0
	}

	var initial, previd common.Pgid
	for i, id := range f.ids {
		if id <= 1 {
			panic(fmt.Sprintf("invalid page allocation: %d", id))
		}

		// Reset initial page if this is not contiguous.
		if previd == 0 || id-previd != 1 {
			initial = id
		}

		// If we found a contiguous block then remove it and return it.
		if (id-initial)+1 == common.Pgid(n) {
			// If we're allocating off the beginning then take the fast path
			// and just adjust the existing slice. This will use extra memory
			// temporarily but the append() in free() will realloc the slice
			// as is necessary.
			if (i + 1) == n {
				f.ids = f.ids[i+1:]
			} else {
				copy(f.ids[i-n+1:], f.ids[i+1:])
				f.ids = f.ids[:len(f.ids)-n]
			}

			// Remove from the free cache.
			for i := common.Pgid(0); i < common.Pgid(n); i++ {
				delete(f.cache, initial+i)
			}
			f.allocs[initial] = txid
			return initial
		}

		previd = id
	}
	return 0
}

func (f *array) FreeCount() int {
	return len(f.ids)
}

func (f *array) freePageIds() common.Pgids {
	return f.ids
}

func (f *array) mergeSpans(ids common.Pgids) {
	sort.Sort(ids)
	common.Verify(func() {
		idsIdx := make(map[common.Pgid]struct{})
		for _, id := range f.ids {
			// The existing f.ids shouldn't have duplicated free ID.
			if _, ok := idsIdx[id]; ok {
				panic(fmt.Sprintf("detected duplicated free page ID: %d in existing f.ids: %v", id, f.ids))
			}
			idsIdx[id] = struct{}{}
		}

		prev := common.Pgid(0)
		for _, id := range ids {
			// The ids shouldn't have duplicated free ID. Note page 0 and 1
			// are reserved for meta pages, so they can never be free page IDs.
			if prev == id {
				panic(fmt.Sprintf("detected duplicated free ID: %d in ids: %v", id, ids))
			}
			prev = id

			// The ids shouldn't have any overlap with the existing f.ids.
			if _, ok := idsIdx[id]; ok {
				panic(fmt.Sprintf("detected overlapped free page ID: %d between ids: %v and existing f.ids: %v", id, ids, f.ids))
			}
		}
	})
	f.ids = common.Pgids(f.ids).Merge(ids)
}

func NewArrayFreelist() Interface {
	a := &array{
		shared: newShared(),
		ids:    []common.Pgid{},
	}
	a.Interface = a
	return a
}
```

## File: `internal/freelist/array_test.go`
```go
package freelist

import (
	"reflect"
	"testing"

	"github.com/stretchr/testify/require"

	"go.etcd.io/bbolt/internal/common"
)

// Ensure that a freelist can find contiguous blocks of pages.
func TestFreelistArray_allocate(t *testing.T) {
	f := NewArrayFreelist()
	ids := []common.Pgid{3, 4, 5, 6, 7, 9, 12, 13, 18}
	f.Init(ids)
	if id := int(f.Allocate(1, 3)); id != 3 {
		t.Fatalf("exp=3; got=%v", id)
	}
	if id := int(f.Allocate(1, 1)); id != 6 {
		t.Fatalf("exp=6; got=%v", id)
	}
	if id := int(f.Allocate(1, 3)); id != 0 {
		t.Fatalf("exp=0; got=%v", id)
	}
	if id := int(f.Allocate(1, 2)); id != 12 {
		t.Fatalf("exp=12; got=%v", id)
	}
	if id := int(f.Allocate(1, 1)); id != 7 {
		t.Fatalf("exp=7; got=%v", id)
	}
	if id := int(f.Allocate(1, 0)); id != 0 {
		t.Fatalf("exp=0; got=%v", id)
	}
	if id := int(f.Allocate(1, 0)); id != 0 {
		t.Fatalf("exp=0; got=%v", id)
	}
	if exp := common.Pgids([]common.Pgid{9, 18}); !reflect.DeepEqual(exp, f.freePageIds()) {
		t.Fatalf("exp=%v; got=%v", exp, f.freePageIds())
	}

	if id := int(f.Allocate(1, 1)); id != 9 {
		t.Fatalf("exp=9; got=%v", id)
	}
	if id := int(f.Allocate(1, 1)); id != 18 {
		t.Fatalf("exp=18; got=%v", id)
	}
	if id := int(f.Allocate(1, 1)); id != 0 {
		t.Fatalf("exp=0; got=%v", id)
	}
	if exp := common.Pgids([]common.Pgid{}); !reflect.DeepEqual(exp, f.freePageIds()) {
		t.Fatalf("exp=%v; got=%v", exp, f.freePageIds())
	}
}

func TestInvalidArrayAllocation(t *testing.T) {
	f := NewArrayFreelist()
	// page 0 and 1 are reserved for meta pages, so they should never be free pages.
	ids := []common.Pgid{1}
	f.Init(ids)
	require.Panics(t, func() {
		f.Allocate(common.Txid(1), 1)
	})
}

func Test_Freelist_Array_Rollback(t *testing.T) {
	f := newTestArrayFreelist()

	f.Init([]common.Pgid{3, 5, 6, 7, 12, 13})

	f.Free(100, common.NewPage(20, 0, 0, 1))
	f.Allocate(100, 3)
	f.Free(100, common.NewPage(25, 0, 0, 0))
	f.Allocate(100, 2)

	require.Equal(t, map[common.Pgid]common.Txid{5: 100, 12: 100}, f.allocs)
	require.Equal(t, map[common.Txid]*txPending{100: {
		ids:     []common.Pgid{20, 21, 25},
		alloctx: []common.Txid{0, 0, 0},
	}}, f.pending)

	f.Rollback(100)

	require.Equal(t, map[common.Pgid]common.Txid{}, f.allocs)
	require.Equal(t, map[common.Txid]*txPending{}, f.pending)
}

func newTestArrayFreelist() *array {
	f := NewArrayFreelist()
	return f.(*array)
}
```

## File: `internal/freelist/freelist.go`
```go
package freelist

import (
	"go.etcd.io/bbolt/internal/common"
)

type ReadWriter interface {
	// Read calls Init with the page ids stored in the given page.
	Read(page *common.Page)

	// Write writes the freelist into the given page.
	Write(page *common.Page)

	// EstimatedWritePageSize returns the size in bytes of the freelist after serialization in Write.
	// This should never underestimate the size.
	EstimatedWritePageSize() int
}

type Interface interface {
	ReadWriter

	// Init initializes this freelist with the given list of pages.
	Init(ids common.Pgids)

	// Allocate tries to allocate the given number of contiguous pages
	// from the free list pages. It returns the starting page ID if
	// available; otherwise, it returns 0.
	Allocate(txid common.Txid, numPages int) common.Pgid

	// Count returns the number of free and pending pages.
	Count() int

	// FreeCount returns the number of free pages.
	FreeCount() int

	// PendingCount returns the number of pending pages.
	PendingCount() int

	// AddReadonlyTXID adds a given read-only transaction id for pending page tracking.
	AddReadonlyTXID(txid common.Txid)

	// RemoveReadonlyTXID removes a given read-only transaction id for pending page tracking.
	RemoveReadonlyTXID(txid common.Txid)

	// ReleasePendingPages releases any pages associated with closed read-only transactions.
	ReleasePendingPages()

	// Free releases a page and its overflow for a given transaction id.
	// If the page is already free or is one of the meta pages, then a panic will occur.
	Free(txId common.Txid, p *common.Page)

	// Freed returns whether a given page is in the free list.
	Freed(pgId common.Pgid) bool

	// Rollback removes the pages from a given pending tx.
	Rollback(txId common.Txid)

	// Copyall copies a list of all free ids and all pending ids in one sorted list.
	// f.count returns the minimum length required for dst.
	Copyall(dst []common.Pgid)

	// Reload reads the freelist from a page and filters out pending items.
	Reload(p *common.Page)

	// NoSyncReload reads the freelist from Pgids and filters out pending items.
	NoSyncReload(pgIds common.Pgids)

	// freePageIds returns the IDs of all free pages. Returns an empty slice if no free pages are available.
	freePageIds() common.Pgids

	// pendingPageIds returns all pending pages by transaction id.
	pendingPageIds() map[common.Txid]*txPending

	// release moves all page ids for a transaction id (or older) to the freelist.
	release(txId common.Txid)

	// releaseRange moves pending pages allocated within an extent [begin,end] to the free list.
	releaseRange(begin, end common.Txid)

	// mergeSpans is merging the given pages into the freelist
	mergeSpans(ids common.Pgids)
}
```

## File: `internal/freelist/freelist_test.go`
```go
package freelist

import (
	"fmt"
	"math"
	"math/rand"
	"os"
	"reflect"
	"slices"
	"sort"
	"testing"
	"testing/quick"
	"unsafe"

	"github.com/stretchr/testify/require"

	"go.etcd.io/bbolt/internal/common"
)

// TestFreelistType is used as a env variable for test to indicate the backend type
const TestFreelistType = "TEST_FREELIST_TYPE"

// Ensure that a page is added to a transaction's freelist.
func TestFreelist_free(t *testing.T) {
	f := newTestFreelist()
	f.Free(100, common.NewPage(12, 0, 0, 0))
	if !reflect.DeepEqual([]common.Pgid{12}, f.pendingPageIds()[100].ids) {
		t.Fatalf("exp=%v; got=%v", []common.Pgid{12}, f.pendingPageIds()[100].ids)
	}
}

// Ensure that a page and its overflow is added to a transaction's freelist.
func TestFreelist_free_overflow(t *testing.T) {
	f := newTestFreelist()
	f.Free(100, common.NewPage(12, 0, 0, 3))
	if exp := []common.Pgid{12, 13, 14, 15}; !reflect.DeepEqual(exp, f.pendingPageIds()[100].ids) {
		t.Fatalf("exp=%v; got=%v", exp, f.pendingPageIds()[100].ids)
	}
}

// Ensure that double freeing a page is causing a panic
func TestFreelist_free_double_free_panics(t *testing.T) {
	f := newTestFreelist()
	f.Free(100, common.NewPage(12, 0, 0, 3))
	require.Panics(t, func() {
		f.Free(100, common.NewPage(12, 0, 0, 3))
	})
}

// Ensure that attempting to free the meta page panics
func TestFreelist_free_meta_panics(t *testing.T) {
	f := newTestFreelist()
	require.Panics(t, func() {
		f.Free(100, common.NewPage(0, 0, 0, 0))
	})
	require.Panics(t, func() {
		f.Free(100, common.NewPage(1, 0, 0, 0))
	})
}

func TestFreelist_free_freelist(t *testing.T) {
	f := newTestFreelist()
	f.Free(100, common.NewPage(12, common.FreelistPageFlag, 0, 0))
	pp := f.pendingPageIds()[100]
	require.Equal(t, []common.Pgid{12}, pp.ids)
	require.Equal(t, []common.Txid{0}, pp.alloctx)
}

func TestFreelist_free_freelist_alloctx(t *testing.T) {
	f := newTestFreelist()
	f.Free(100, common.NewPage(12, common.FreelistPageFlag, 0, 0))
	f.Rollback(100)
	require.Empty(t, f.freePageIds())
	require.Empty(t, f.pendingPageIds())
	require.False(t, f.Freed(12))

	f.Free(101, common.NewPage(12, common.FreelistPageFlag, 0, 0))
	require.True(t, f.Freed(12))
	if exp := []common.Pgid{12}; !reflect.DeepEqual(exp, f.pendingPageIds()[101].ids) {
		t.Fatalf("exp=%v; got=%v", exp, f.pendingPageIds()[101].ids)
	}
	f.ReleasePendingPages()
	require.True(t, f.Freed(12))
	require.Empty(t, f.pendingPageIds())
	if exp := common.Pgids([]common.Pgid{12}); !reflect.DeepEqual(exp, f.freePageIds()) {
		t.Fatalf("exp=%v; got=%v", exp, f.freePageIds())
	}
}

// Ensure that a transaction's free pages can be released.
func TestFreelist_release(t *testing.T) {
	f := newTestFreelist()
	f.Free(100, common.NewPage(12, 0, 0, 1))
	f.Free(100, common.NewPage(9, 0, 0, 0))
	f.Free(102, common.NewPage(39, 0, 0, 0))
	f.release(100)
	f.release(101)
	if exp := common.Pgids([]common.Pgid{9, 12, 13}); !reflect.DeepEqual(exp, f.freePageIds()) {
		t.Fatalf("exp=%v; got=%v", exp, f.freePageIds())
	}

	f.release(102)
	if exp := common.Pgids([]common.Pgid{9, 12, 13, 39}); !reflect.DeepEqual(exp, f.freePageIds()) {
		t.Fatalf("exp=%v; got=%v", exp, f.freePageIds())
	}
}

// Ensure that releaseRange handles boundary conditions correctly
func TestFreelist_releaseRange(t *testing.T) {
	type testRange struct {
		begin, end common.Txid
	}

	type testPage struct {
		id       common.Pgid
		n        int
		allocTxn common.Txid
		freeTxn  common.Txid
	}

	var releaseRangeTests = []struct {
		title         string
		pagesIn       []testPage
		releaseRanges []testRange
		wantFree      []common.Pgid
	}{
		{
			title:         "Single pending in range",
			pagesIn:       []testPage{{id: 3, n: 1, allocTxn: 100, freeTxn: 200}},
			releaseRanges: []testRange{{1, 300}},
			wantFree:      []common.Pgid{3},
		},
		{
			title:         "Single pending with minimum end range",
			pagesIn:       []testPage{{id: 3, n: 1, allocTxn: 100, freeTxn: 200}},
			releaseRanges: []testRange{{1, 200}},
			wantFree:      []common.Pgid{3},
		},
		{
			title:         "Single pending outsize minimum end range",
			pagesIn:       []testPage{{id: 3, n: 1, allocTxn: 100, freeTxn: 200}},
			releaseRanges: []testRange{{1, 199}},
			wantFree:      []common.Pgid{},
		},
		{
			title:         "Single pending with minimum begin range",
			pagesIn:       []testPage{{id: 3, n: 1, allocTxn: 100, freeTxn: 200}},
			releaseRanges: []testRange{{100, 300}},
			wantFree:      []common.Pgid{3},
		},
		{
			title:         "Single pending outside minimum begin range",
			pagesIn:       []testPage{{id: 3, n: 1, allocTxn: 100, freeTxn: 200}},
			releaseRanges: []testRange{{101, 300}},
			wantFree:      []common.Pgid{},
		},
		{
			title:         "Single pending in minimum range",
			pagesIn:       []testPage{{id: 3, n: 1, allocTxn: 199, freeTxn: 200}},
			releaseRanges: []testRange{{199, 200}},
			wantFree:      []common.Pgid{3},
		},
		{
			title:         "Single pending and read transaction at 199",
			pagesIn:       []testPage{{id: 3, n: 1, allocTxn: 199, freeTxn: 200}},
			releaseRanges: []testRange{{100, 198}, {200, 300}},
			wantFree:      []common.Pgid{},
		},
		{
			title: "Adjacent pending and read transactions at 199, 200",
			pagesIn: []testPage{
				{id: 3, n: 1, allocTxn: 199, freeTxn: 200},
				{id: 4, n: 1, allocTxn: 200, freeTxn: 201},
			},
			releaseRanges: []testRange{
				{100, 198},
				{200, 199}, // Simulate the ranges db.freePages might produce.
				{201, 300},
			},
			wantFree: []common.Pgid{},
		},
		{
			title: "Out of order ranges",
			pagesIn: []testPage{
				{id: 3, n: 1, allocTxn: 199, freeTxn: 200},
				{id: 4, n: 1, allocTxn: 200, freeTxn: 201},
			},
			releaseRanges: []testRange{
				{201, 199},
				{201, 200},
				{200, 200},
			},
			wantFree: []common.Pgid{},
		},
		{
			title: "Multiple pending, read transaction at 150",
			pagesIn: []testPage{
				{id: 3, n: 1, allocTxn: 100, freeTxn: 200},
				{id: 4, n: 1, allocTxn: 100, freeTxn: 125},
				{id: 5, n: 1, allocTxn: 125, freeTxn: 150},
				{id: 6, n: 1, allocTxn: 125, freeTxn: 175},
				{id: 7, n: 2, allocTxn: 150, freeTxn: 175},
				{id: 9, n: 2, allocTxn: 175, freeTxn: 200},
			},
			releaseRanges: []testRange{{50, 149}, {151, 300}},
			wantFree:      []common.Pgid{4, 9, 10},
		},
	}

	for _, c := range releaseRangeTests {
		t.Run(c.title, func(t *testing.T) {
			f := newTestFreelist()
			var ids []common.Pgid
			for _, p := range c.pagesIn {
				for i := uint64(0); i < uint64(p.n); i++ {
					ids = append(ids, common.Pgid(uint64(p.id)+i))
				}
			}
			f.Init(ids)
			for _, p := range c.pagesIn {
				f.Allocate(p.allocTxn, p.n)
			}

			for _, p := range c.pagesIn {
				f.Free(p.freeTxn, common.NewPage(p.id, 0, 0, uint32(p.n-1)))
			}

			for _, r := range c.releaseRanges {
				f.releaseRange(r.begin, r.end)
			}

			require.Equal(t, common.Pgids(c.wantFree), f.freePageIds())
		})
	}
}

func TestFreeList_init(t *testing.T) {
	buf := make([]byte, 4096)
	f := newTestFreelist()
	f.Init(common.Pgids{5, 6, 8})

	p := common.LoadPage(buf)
	f.Write(p)

	f2 := newTestFreelist()
	f2.Read(p)
	require.Equal(t, common.Pgids{5, 6, 8}, f2.freePageIds())

	// When initializing the freelist with an empty list of page ID,
	// it should reset the freelist page IDs.
	f2.Init([]common.Pgid{})
	require.Equal(t, common.Pgids{}, f2.freePageIds())
}

func TestFreeList_reload(t *testing.T) {
	buf := make([]byte, 4096)
	f := newTestFreelist()
	f.Init(common.Pgids{5, 6, 8})

	p := common.LoadPage(buf)
	f.Write(p)

	f2 := newTestFreelist()
	f2.Read(p)
	require.Equal(t, common.Pgids{5, 6, 8}, f2.freePageIds())

	f2.Free(common.Txid(5), common.NewPage(10, common.LeafPageFlag, 0, 2))

	// reload shouldn't affect the pending list
	f2.Reload(p)

	require.Equal(t, common.Pgids{5, 6, 8}, f2.freePageIds())
	require.Equal(t, []common.Pgid{10, 11, 12}, f2.pendingPageIds()[5].ids)
}

// Ensure that the txIDx swap, less and len are properly implemented
func TestTxidSorting(t *testing.T) {
	require.NoError(t, quick.Check(func(a []uint64) bool {
		var txids []common.Txid
		for _, txid := range a {
			txids = append(txids, common.Txid(txid))
		}

		sort.Sort(txIDx(txids))

		var r []uint64
		for _, txid := range txids {
			r = append(r, uint64(txid))
		}

		if !slices.IsSorted(r) {
			t.Errorf("txids were not sorted correctly=%v", txids)
			return false
		}

		return true
	}, nil))
}

// Ensure that a freelist can deserialize from a freelist page.
func TestFreelist_read(t *testing.T) {
	// Create a page.
	var buf [4096]byte
	page := (*common.Page)(unsafe.Pointer(&buf[0]))
	page.SetFlags(common.FreelistPageFlag)
	page.SetCount(2)

	// Insert 2 page ids.
	ids := (*[3]common.Pgid)(unsafe.Pointer(uintptr(unsafe.Pointer(page)) + unsafe.Sizeof(*page)))
	ids[0] = 23
	ids[1] = 50

	// Deserialize page into a freelist.
	f := newTestFreelist()
	f.Read(page)

	// Ensure that there are two page ids in the freelist.
	if exp := common.Pgids([]common.Pgid{23, 50}); !reflect.DeepEqual(exp, f.freePageIds()) {
		t.Fatalf("exp=%v; got=%v", exp, f.freePageIds())
	}
}

// Ensure that we never read a non-freelist page
func TestFreelist_read_panics(t *testing.T) {
	buf := make([]byte, 4096)
	page := common.LoadPage(buf)
	page.SetFlags(common.BranchPageFlag)
	page.SetCount(2)
	f := newTestFreelist()
	require.Panics(t, func() {
		f.Read(page)
	})
}

// Ensure that a freelist can serialize into a freelist page.
func TestFreelist_write(t *testing.T) {
	// Create a freelist and write it to a page.
	var buf [4096]byte
	f := newTestFreelist()

	f.Init([]common.Pgid{12, 39})
	f.pendingPageIds()[100] = &txPending{ids: []common.Pgid{28, 11}}
	f.pendingPageIds()[101] = &txPending{ids: []common.Pgid{3}}
	p := (*common.Page)(unsafe.Pointer(&buf[0]))
	f.Write(p)

	// Read the page back out.
	f2 := newTestFreelist()
	f2.Read(p)

	// Ensure that the freelist is correct.
	// All pages should be present and in reverse order.
	if exp := common.Pgids([]common.Pgid{3, 11, 12, 28, 39}); !reflect.DeepEqual(exp, f2.freePageIds()) {
		t.Fatalf("exp=%v; got=%v", exp, f2.freePageIds())
	}
}

func TestFreelist_E2E_HappyPath(t *testing.T) {
	f := newTestFreelist()
	f.Init([]common.Pgid{})
	requirePages(t, f, common.Pgids{}, common.Pgids{})

	allocated := f.Allocate(common.Txid(1), 5)
	require.Equal(t, common.Pgid(0), allocated)
	// tx.go may now allocate more space, and eventually we need to delete a page again
	f.Free(common.Txid(2), common.NewPage(5, common.LeafPageFlag, 0, 0))
	f.Free(common.Txid(2), common.NewPage(3, common.LeafPageFlag, 0, 0))
	f.Free(common.Txid(2), common.NewPage(8, common.LeafPageFlag, 0, 0))
	// the above will only mark the pages as pending, so free pages should not return anything
	requirePages(t, f, common.Pgids{}, common.Pgids{3, 5, 8})

	// someone wants to do a read on top of the next tx id
	f.AddReadonlyTXID(common.Txid(3))
	// this should free the above pages for tx 2 entirely
	f.ReleasePendingPages()
	requirePages(t, f, common.Pgids{3, 5, 8}, common.Pgids{})

	// no span of two pages available should yield a zero-page result
	require.Equal(t, common.Pgid(0), f.Allocate(common.Txid(4), 2))
	// we should be able to allocate those pages independently however,
	// map and array differ in the order they return the pages
	expectedPgids := map[common.Pgid]struct{}{3: {}, 5: {}, 8: {}}
	for i := 0; i < 3; i++ {
		allocated = f.Allocate(common.Txid(4), 1)
		require.Contains(t, expectedPgids, allocated, "expected to find pgid %d", allocated)
		require.False(t, f.Freed(allocated))
		delete(expectedPgids, allocated)
	}
	require.Emptyf(t, expectedPgids, "unexpectedly more than one page was still found")
	// no more free pages to allocate
	require.Equal(t, common.Pgid(0), f.Allocate(common.Txid(4), 1))
}

func TestFreelist_E2E_MultiSpanOverflows(t *testing.T) {
	f := newTestFreelist()
	f.Init([]common.Pgid{})
	f.Free(common.Txid(10), common.NewPage(20, common.LeafPageFlag, 0, 1))
	f.Free(common.Txid(10), common.NewPage(25, common.LeafPageFlag, 0, 2))
	f.Free(common.Txid(10), common.NewPage(35, common.LeafPageFlag, 0, 3))
	f.Free(common.Txid(10), common.NewPage(39, common.LeafPageFlag, 0, 2))
	f.Free(common.Txid(10), common.NewPage(45, common.LeafPageFlag, 0, 4))
	requirePages(t, f, common.Pgids{}, common.Pgids{20, 21, 25, 26, 27, 35, 36, 37, 38, 39, 40, 41, 45, 46, 47, 48, 49})
	f.ReleasePendingPages()
	requirePages(t, f, common.Pgids{20, 21, 25, 26, 27, 35, 36, 37, 38, 39, 40, 41, 45, 46, 47, 48, 49}, common.Pgids{})

	// that sequence, regardless of implementation, should always yield the same blocks of pages
	allocSequence := []int{7, 5, 3, 2}
	expectedSpanStarts := []common.Pgid{35, 45, 25, 20}
	for i, pageNums := range allocSequence {
		allocated := f.Allocate(common.Txid(11), pageNums)
		require.Equal(t, expectedSpanStarts[i], allocated)
		// ensure all pages in that span are not considered free anymore
		for i := 0; i < pageNums; i++ {
			require.False(t, f.Freed(allocated+common.Pgid(i)))
		}
	}
}

func TestFreelist_E2E_Rollbacks(t *testing.T) {
	freelist := newTestFreelist()
	freelist.Init([]common.Pgid{})
	freelist.Free(common.Txid(2), common.NewPage(5, common.LeafPageFlag, 0, 1))
	freelist.Free(common.Txid(2), common.NewPage(8, common.LeafPageFlag, 0, 0))
	requirePages(t, freelist, common.Pgids{}, common.Pgids{5, 6, 8})
	freelist.Rollback(common.Txid(2))
	requirePages(t, freelist, common.Pgids{}, common.Pgids{})

	// unknown transaction should not trigger anything
	freelist.Free(common.Txid(4), common.NewPage(13, common.LeafPageFlag, 0, 3))
	requirePages(t, freelist, common.Pgids{}, common.Pgids{13, 14, 15, 16})
	freelist.ReleasePendingPages()
	requirePages(t, freelist, common.Pgids{13, 14, 15, 16}, common.Pgids{})
	freelist.Rollback(common.Txid(1337))
	requirePages(t, freelist, common.Pgids{13, 14, 15, 16}, common.Pgids{})
}

func TestFreelist_E2E_RollbackPanics(t *testing.T) {
	freelist := newTestFreelist()
	freelist.Init([]common.Pgid{5})
	requirePages(t, freelist, common.Pgids{5}, common.Pgids{})

	_ = freelist.Allocate(common.Txid(5), 1)
	require.Panics(t, func() {
		// depending on the verification level, either should panic
		freelist.Free(common.Txid(5), common.NewPage(5, common.LeafPageFlag, 0, 0))
		freelist.Rollback(5)
	})
}

// tests the reloading from another physical page
func TestFreelist_E2E_Reload(t *testing.T) {
	freelist := newTestFreelist()
	freelist.Init([]common.Pgid{})
	freelist.Free(common.Txid(2), common.NewPage(5, common.LeafPageFlag, 0, 1))
	freelist.Free(common.Txid(2), common.NewPage(8, common.LeafPageFlag, 0, 0))
	freelist.ReleasePendingPages()
	requirePages(t, freelist, common.Pgids{5, 6, 8}, common.Pgids{})
	buf := make([]byte, 4096)
	p := common.LoadPage(buf)
	freelist.Write(p)

	freelist.Free(common.Txid(3), common.NewPage(3, common.LeafPageFlag, 0, 1))
	freelist.Free(common.Txid(3), common.NewPage(10, common.LeafPageFlag, 0, 2))
	requirePages(t, freelist, common.Pgids{5, 6, 8}, common.Pgids{3, 4, 10, 11, 12})

	otherBuf := make([]byte, 4096)
	px := common.LoadPage(otherBuf)
	freelist.Write(px)

	loadFreeList := newTestFreelist()
	loadFreeList.Init([]common.Pgid{})
	loadFreeList.Read(px)
	requirePages(t, loadFreeList, common.Pgids{3, 4, 5, 6, 8, 10, 11, 12}, common.Pgids{})
	// restore the original freelist again
	loadFreeList.Reload(p)
	requirePages(t, loadFreeList, common.Pgids{5, 6, 8}, common.Pgids{})

	// reload another page with different free pages to test we are deduplicating the free pages with the pending ones correctly
	freelist = newTestFreelist()
	freelist.Init([]common.Pgid{})
	freelist.Free(common.Txid(5), common.NewPage(5, common.LeafPageFlag, 0, 4))
	freelist.Reload(p)
	requirePages(t, freelist, common.Pgids{}, common.Pgids{5, 6, 7, 8, 9})
}

// tests the loading and reloading from physical pages
func TestFreelist_E2E_SerDe_HappyPath(t *testing.T) {
	freelist := newTestFreelist()
	freelist.Init([]common.Pgid{})
	freelist.Free(common.Txid(2), common.NewPage(5, common.LeafPageFlag, 0, 1))
	freelist.Free(common.Txid(2), common.NewPage(8, common.LeafPageFlag, 0, 0))
	freelist.ReleasePendingPages()
	requirePages(t, freelist, common.Pgids{5, 6, 8}, common.Pgids{})

	freelist.Free(common.Txid(3), common.NewPage(3, common.LeafPageFlag, 0, 1))
	freelist.Free(common.Txid(3), common.NewPage(10, common.LeafPageFlag, 0, 2))
	requirePages(t, freelist, common.Pgids{5, 6, 8}, common.Pgids{3, 4, 10, 11, 12})

	buf := make([]byte, 4096)
	p := common.LoadPage(buf)
	require.Equal(t, 80, freelist.EstimatedWritePageSize())
	freelist.Write(p)

	loadFreeList := newTestFreelist()
	loadFreeList.Init([]common.Pgid{})
	loadFreeList.Read(p)
	requirePages(t, loadFreeList, common.Pgids{3, 4, 5, 6, 8, 10, 11, 12}, common.Pgids{})
}

// tests the loading of a freelist against other implementations with various sizes
func TestFreelist_E2E_SerDe_AcrossImplementations(t *testing.T) {
	testSizes := []int{0, 1, 10, 100, 1000, math.MaxUint16, math.MaxUint16 + 1, math.MaxUint16 * 2}
	for _, size := range testSizes {
		t.Run(fmt.Sprintf("n=%d", size), func(t *testing.T) {
			freelist := newTestFreelist()
			expectedFreePgids := common.Pgids{}
			for i := 0; i < size; i++ {
				pgid := common.Pgid(i + 2)
				freelist.Free(common.Txid(1), common.NewPage(pgid, common.LeafPageFlag, 0, 0))
				expectedFreePgids = append(expectedFreePgids, pgid)
			}
			freelist.ReleasePendingPages()
			requirePages(t, freelist, expectedFreePgids, common.Pgids{})
			buf := make([]byte, freelist.EstimatedWritePageSize())
			p := common.LoadPage(buf)
			freelist.Write(p)

			for n, loadFreeList := range map[string]Interface{
				"hashmap": NewHashMapFreelist(),
				"array":   NewArrayFreelist(),
			} {
				t.Run(n, func(t *testing.T) {
					loadFreeList.Read(p)
					requirePages(t, loadFreeList, expectedFreePgids, common.Pgids{})
				})
			}
		})
	}
}

func requirePages(t *testing.T, f Interface, freePageIds common.Pgids, pendingPageIds common.Pgids) {
	require.Equal(t, f.FreeCount()+f.PendingCount(), f.Count())
	require.Equalf(t, freePageIds, f.freePageIds(), "unexpected free pages")
	require.Equal(t, len(freePageIds), f.FreeCount())

	pp := allPendingPages(f.pendingPageIds())
	require.Equalf(t, pendingPageIds, pp, "unexpected pending pages")
	require.Equal(t, len(pp), f.PendingCount())

	for _, pgid := range f.freePageIds() {
		require.Truef(t, f.Freed(pgid), "expected free page to return true on Freed")
	}

	for _, pgid := range pp {
		require.Truef(t, f.Freed(pgid), "expected pending page to return true on Freed")
	}
}

func allPendingPages(p map[common.Txid]*txPending) common.Pgids {
	pgids := common.Pgids{}
	for _, pending := range p {
		pgids = append(pgids, pending.ids...)
	}
	sort.Sort(pgids)
	return pgids
}

func Benchmark_FreelistRelease10K(b *testing.B)    { benchmark_FreelistRelease(b, 10000) }
func Benchmark_FreelistRelease100K(b *testing.B)   { benchmark_FreelistRelease(b, 100000) }
func Benchmark_FreelistRelease1000K(b *testing.B)  { benchmark_FreelistRelease(b, 1000000) }
func Benchmark_FreelistRelease10000K(b *testing.B) { benchmark_FreelistRelease(b, 10000000) }

func benchmark_FreelistRelease(b *testing.B, size int) {
	ids := randomPgids(size)
	pending := randomPgids(len(ids) / 400)
	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		txp := &txPending{ids: pending}
		f := newTestFreelist()
		f.pendingPageIds()[1] = txp
		f.Init(ids)
		f.release(1)
	}
}

func randomPgids(n int) []common.Pgid {
	pgids := make(common.Pgids, n)
	for i := range pgids {
		pgids[i] = common.Pgid(rand.Int63())
	}
	sort.Sort(pgids)
	return pgids
}

func Test_freelist_ReadIDs_and_getFreePageIDs(t *testing.T) {
	f := newTestFreelist()
	exp := common.Pgids([]common.Pgid{3, 4, 5, 6, 7, 9, 12, 13, 18})

	f.Init(exp)

	if got := f.freePageIds(); !reflect.DeepEqual(exp, got) {
		t.Fatalf("exp=%v; got=%v", exp, got)
	}

	f2 := newTestFreelist()
	exp2 := []common.Pgid{}
	f2.Init(exp2)

	if got2 := f2.freePageIds(); !reflect.DeepEqual(got2, common.Pgids(exp2)) {
		t.Fatalf("exp2=%#v; got2=%#v", exp2, got2)
	}

}

// newTestFreelist get the freelist type from env and initial the freelist
func newTestFreelist() Interface {
	if env := os.Getenv(TestFreelistType); env == "hashmap" {
		return NewHashMapFreelist()
	}

	return NewArrayFreelist()
}
```

## File: `internal/freelist/hashmap.go`
```go
package freelist

import (
	"fmt"
	"reflect"
	"sort"

	"go.etcd.io/bbolt/internal/common"
)

// pidSet holds the set of starting pgids which have the same span size
type pidSet map[common.Pgid]struct{}

type hashMap struct {
	*shared

	freePagesCount uint64                 // count of free pages(hashmap version)
	freemaps       map[uint64]pidSet      // key is the size of continuous pages(span), value is a set which contains the starting pgids of same size
	forwardMap     map[common.Pgid]uint64 // key is start pgid, value is its span size
	backwardMap    map[common.Pgid]uint64 // key is end pgid, value is its span size
}

func (f *hashMap) Init(pgids common.Pgids) {
	// reset the counter when freelist init
	f.freePagesCount = 0
	f.freemaps = make(map[uint64]pidSet)
	f.forwardMap = make(map[common.Pgid]uint64)
	f.backwardMap = make(map[common.Pgid]uint64)

	if len(pgids) == 0 {
		return
	}

	if !sort.SliceIsSorted([]common.Pgid(pgids), func(i, j int) bool { return pgids[i] < pgids[j] }) {
		panic("pgids not sorted")
	}

	size := uint64(1)
	start := pgids[0]

	for i := 1; i < len(pgids); i++ {
		// continuous page
		if pgids[i] == pgids[i-1]+1 {
			size++
		} else {
			f.addSpan(start, size)

			size = 1
			start = pgids[i]
		}
	}

	// init the tail
	if size != 0 && start != 0 {
		f.addSpan(start, size)
	}

	f.reindex()
}

func (f *hashMap) Allocate(txid common.Txid, n int) common.Pgid {
	if n == 0 {
		return 0
	}

	// if we have a exact size match just return short path
	if bm, ok := f.freemaps[uint64(n)]; ok {
		for pid := range bm {
			// remove the span
			f.delSpan(pid, uint64(n))

			f.allocs[pid] = txid

			for i := common.Pgid(0); i < common.Pgid(n); i++ {
				delete(f.cache, pid+i)
			}
			return pid
		}
	}

	// lookup the map to find larger span
	for size, bm := range f.freemaps {
		if size < uint64(n) {
			continue
		}

		for pid := range bm {
			// remove the initial
			f.delSpan(pid, size)

			f.allocs[pid] = txid

			remain := size - uint64(n)

			// add remain span
			f.addSpan(pid+common.Pgid(n), remain)

			for i := common.Pgid(0); i < common.Pgid(n); i++ {
				delete(f.cache, pid+i)
			}
			return pid
		}
	}

	return 0
}

func (f *hashMap) FreeCount() int {
	common.Verify(func() {
		expectedFreePageCount := f.hashmapFreeCountSlow()
		common.Assert(int(f.freePagesCount) == expectedFreePageCount,
			"freePagesCount (%d) is out of sync with free pages map (%d)", f.freePagesCount, expectedFreePageCount)
	})
	return int(f.freePagesCount)
}

func (f *hashMap) freePageIds() common.Pgids {
	count := f.FreeCount()
	if count == 0 {
		return common.Pgids{}
	}

	m := make([]common.Pgid, 0, count)

	startPageIds := make([]common.Pgid, 0, len(f.forwardMap))
	for k := range f.forwardMap {
		startPageIds = append(startPageIds, k)
	}
	sort.Sort(common.Pgids(startPageIds))

	for _, start := range startPageIds {
		if size, ok := f.forwardMap[start]; ok {
			for i := 0; i < int(size); i++ {
				m = append(m, start+common.Pgid(i))
			}
		}
	}

	return m
}

func (f *hashMap) hashmapFreeCountSlow() int {
	count := 0
	for _, size := range f.forwardMap {
		count += int(size)
	}
	return count
}

func (f *hashMap) addSpan(start common.Pgid, size uint64) {
	f.backwardMap[start-1+common.Pgid(size)] = size
	f.forwardMap[start] = size
	if _, ok := f.freemaps[size]; !ok {
		f.freemaps[size] = make(map[common.Pgid]struct{})
	}

	f.freemaps[size][start] = struct{}{}
	f.freePagesCount += size
}

func (f *hashMap) delSpan(start common.Pgid, size uint64) {
	delete(f.forwardMap, start)
	delete(f.backwardMap, start+common.Pgid(size-1))
	delete(f.freemaps[size], start)
	if len(f.freemaps[size]) == 0 {
		delete(f.freemaps, size)
	}
	f.freePagesCount -= size
}

func (f *hashMap) mergeSpans(ids common.Pgids) {
	common.Verify(func() {
		ids1Freemap := f.idsFromFreemaps()
		ids2Forward := f.idsFromForwardMap()
		ids3Backward := f.idsFromBackwardMap()

		if !reflect.DeepEqual(ids1Freemap, ids2Forward) {
			panic(fmt.Sprintf("Detected mismatch, f.freemaps: %v, f.forwardMap: %v", f.freemaps, f.forwardMap))
		}
		if !reflect.DeepEqual(ids1Freemap, ids3Backward) {
			panic(fmt.Sprintf("Detected mismatch, f.freemaps: %v, f.backwardMap: %v", f.freemaps, f.backwardMap))
		}

		sort.Sort(ids)
		prev := common.Pgid(0)
		for _, id := range ids {
			// The ids shouldn't have duplicated free ID.
			if prev == id {
				panic(fmt.Sprintf("detected duplicated free ID: %d in ids: %v", id, ids))
			}
			prev = id

			// The ids shouldn't have any overlap with the existing f.freemaps.
			if _, ok := ids1Freemap[id]; ok {
				panic(fmt.Sprintf("detected overlapped free page ID: %d between ids: %v and existing f.freemaps: %v", id, ids, f.freemaps))
			}
		}
	})
	for _, id := range ids {
		// try to see if we can merge and update
		f.mergeWithExistingSpan(id)
	}
}

// mergeWithExistingSpan merges pid to the existing free spans, try to merge it backward and forward
func (f *hashMap) mergeWithExistingSpan(pid common.Pgid) {
	prev := pid - 1
	next := pid + 1

	preSize, mergeWithPrev := f.backwardMap[prev]
	nextSize, mergeWithNext := f.forwardMap[next]
	newStart := pid
	newSize := uint64(1)

	if mergeWithPrev {
		//merge with previous span
		start := prev + 1 - common.Pgid(preSize)
		f.delSpan(start, preSize)

		newStart -= common.Pgid(preSize)
		newSize += preSize
	}

	if mergeWithNext {
		// merge with next span
		f.delSpan(next, nextSize)
		newSize += nextSize
	}

	f.addSpan(newStart, newSize)
}

// idsFromFreemaps get all free page IDs from f.freemaps.
// used by test only.
func (f *hashMap) idsFromFreemaps() map[common.Pgid]struct{} {
	ids := make(map[common.Pgid]struct{})
	for size, idSet := range f.freemaps {
		for start := range idSet {
			for i := 0; i < int(size); i++ {
				id := start + common.Pgid(i)
				if _, ok := ids[id]; ok {
					panic(fmt.Sprintf("detected duplicated free page ID: %d in f.freemaps: %v", id, f.freemaps))
				}
				ids[id] = struct{}{}
			}
		}
	}
	return ids
}

// idsFromForwardMap get all free page IDs from f.forwardMap.
// used by test only.
func (f *hashMap) idsFromForwardMap() map[common.Pgid]struct{} {
	ids := make(map[common.Pgid]struct{})
	for start, size := range f.forwardMap {
		for i := 0; i < int(size); i++ {
			id := start + common.Pgid(i)
			if _, ok := ids[id]; ok {
				panic(fmt.Sprintf("detected duplicated free page ID: %d in f.forwardMap: %v", id, f.forwardMap))
			}
			ids[id] = struct{}{}
		}
	}
	return ids
}

// idsFromBackwardMap get all free page IDs from f.backwardMap.
// used by test only.
func (f *hashMap) idsFromBackwardMap() map[common.Pgid]struct{} {
	ids := make(map[common.Pgid]struct{})
	for end, size := range f.backwardMap {
		for i := 0; i < int(size); i++ {
			id := end - common.Pgid(i)
			if _, ok := ids[id]; ok {
				panic(fmt.Sprintf("detected duplicated free page ID: %d in f.backwardMap: %v", id, f.backwardMap))
			}
			ids[id] = struct{}{}
		}
	}
	return ids
}

func NewHashMapFreelist() Interface {
	hm := &hashMap{
		shared:      newShared(),
		freemaps:    make(map[uint64]pidSet),
		forwardMap:  make(map[common.Pgid]uint64),
		backwardMap: make(map[common.Pgid]uint64),
	}
	hm.Interface = hm
	return hm
}
```

## File: `internal/freelist/hashmap_test.go`
```go
package freelist

import (
	"math/rand"
	"reflect"
	"sort"
	"testing"

	"github.com/stretchr/testify/require"

	"go.etcd.io/bbolt/internal/common"
)

func TestFreelistHashmap_init_panics(t *testing.T) {
	f := NewHashMapFreelist()
	require.Panics(t, func() {
		// init expects sorted input
		f.Init([]common.Pgid{25, 5})
	})
}

func TestFreelistHashmap_allocate(t *testing.T) {
	f := NewHashMapFreelist()

	ids := []common.Pgid{3, 4, 5, 6, 7, 9, 12, 13, 18}
	f.Init(ids)

	f.Allocate(1, 3)
	if x := f.FreeCount(); x != 6 {
		t.Fatalf("exp=6; got=%v", x)
	}

	f.Allocate(1, 2)
	if x := f.FreeCount(); x != 4 {
		t.Fatalf("exp=4; got=%v", x)
	}
	f.Allocate(1, 1)
	if x := f.FreeCount(); x != 3 {
		t.Fatalf("exp=3; got=%v", x)
	}

	f.Allocate(1, 0)
	if x := f.FreeCount(); x != 3 {
		t.Fatalf("exp=3; got=%v", x)
	}
}

func TestFreelistHashmap_mergeWithExist(t *testing.T) {
	bm1 := pidSet{1: struct{}{}}

	bm2 := pidSet{5: struct{}{}}
	tests := []struct {
		name            string
		ids             common.Pgids
		pgid            common.Pgid
		want            common.Pgids
		wantForwardmap  map[common.Pgid]uint64
		wantBackwardmap map[common.Pgid]uint64
		wantfreemap     map[uint64]pidSet
	}{
		{
			name:            "test1",
			ids:             []common.Pgid{1, 2, 4, 5, 6},
			pgid:            3,
			want:            []common.Pgid{1, 2, 3, 4, 5, 6},
			wantForwardmap:  map[common.Pgid]uint64{1: 6},
			wantBackwardmap: map[common.Pgid]uint64{6: 6},
			wantfreemap:     map[uint64]pidSet{6: bm1},
		},
		{
			name:            "test2",
			ids:             []common.Pgid{1, 2, 5, 6},
			pgid:            3,
			want:            []common.Pgid{1, 2, 3, 5, 6},
			wantForwardmap:  map[common.Pgid]uint64{1: 3, 5: 2},
			wantBackwardmap: map[common.Pgid]uint64{6: 2, 3: 3},
			wantfreemap:     map[uint64]pidSet{3: bm1, 2: bm2},
		},
		{
			name:            "test3",
			ids:             []common.Pgid{1, 2},
			pgid:            3,
			want:            []common.Pgid{1, 2, 3},
			wantForwardmap:  map[common.Pgid]uint64{1: 3},
			wantBackwardmap: map[common.Pgid]uint64{3: 3},
			wantfreemap:     map[uint64]pidSet{3: bm1},
		},
		{
			name:            "test4",
			ids:             []common.Pgid{2, 3},
			pgid:            1,
			want:            []common.Pgid{1, 2, 3},
			wantForwardmap:  map[common.Pgid]uint64{1: 3},
			wantBackwardmap: map[common.Pgid]uint64{3: 3},
			wantfreemap:     map[uint64]pidSet{3: bm1},
		},
	}
	for _, tt := range tests {
		f := newTestHashMapFreelist()
		f.Init(tt.ids)

		f.mergeWithExistingSpan(tt.pgid)

		if got := f.freePageIds(); !reflect.DeepEqual(tt.want, got) {
			t.Fatalf("name %s; exp=%v; got=%v", tt.name, tt.want, got)
		}
		if got := f.forwardMap; !reflect.DeepEqual(tt.wantForwardmap, got) {
			t.Fatalf("name %s; exp=%v; got=%v", tt.name, tt.wantForwardmap, got)
		}
		if got := f.backwardMap; !reflect.DeepEqual(tt.wantBackwardmap, got) {
			t.Fatalf("name %s; exp=%v; got=%v", tt.name, tt.wantBackwardmap, got)
		}
		if got := f.freemaps; !reflect.DeepEqual(tt.wantfreemap, got) {
			t.Fatalf("name %s; exp=%v; got=%v", tt.name, tt.wantfreemap, got)
		}
	}
}

func TestFreelistHashmap_GetFreePageIDs(t *testing.T) {
	f := newTestHashMapFreelist()

	N := int32(100000)
	fm := make(map[common.Pgid]uint64)
	i := int32(0)
	val := int32(0)
	for i = 0; i < N; {
		val = rand.Int31n(1000)
		fm[common.Pgid(i)] = uint64(val)
		i += val
		f.freePagesCount += uint64(val)
	}

	f.forwardMap = fm
	res := f.freePageIds()

	if !sort.SliceIsSorted(res, func(i, j int) bool { return res[i] < res[j] }) {
		t.Fatalf("pgids not sorted")
	}
}

func Test_Freelist_Hashmap_Rollback(t *testing.T) {
	f := newTestHashMapFreelist()

	f.Init([]common.Pgid{3, 5, 6, 7, 12, 13})

	f.Free(100, common.NewPage(20, 0, 0, 1))
	f.Allocate(100, 3)
	f.Free(100, common.NewPage(25, 0, 0, 0))
	f.Allocate(100, 2)

	require.Equal(t, map[common.Pgid]common.Txid{5: 100, 12: 100}, f.allocs)
	require.Equal(t, map[common.Txid]*txPending{100: {
		ids:     []common.Pgid{20, 21, 25},
		alloctx: []common.Txid{0, 0, 0},
	}}, f.pending)

	f.Rollback(100)

	require.Equal(t, map[common.Pgid]common.Txid{}, f.allocs)
	require.Equal(t, map[common.Txid]*txPending{}, f.pending)
}

func Benchmark_freelist_hashmapGetFreePageIDs(b *testing.B) {
	f := newTestHashMapFreelist()
	N := int32(100000)
	fm := make(map[common.Pgid]uint64)
	i := int32(0)
	val := int32(0)
	for i = 0; i < N; {
		val = rand.Int31n(1000)
		fm[common.Pgid(i)] = uint64(val)
		i += val
	}

	f.forwardMap = fm

	b.ReportAllocs()
	b.ResetTimer()
	for n := 0; n < b.N; n++ {
		f.freePageIds()
	}
}

func newTestHashMapFreelist() *hashMap {
	f := NewHashMapFreelist()
	return f.(*hashMap)
}
```

## File: `internal/freelist/shared.go`
```go
package freelist

import (
	"fmt"
	"math"
	"sort"
	"unsafe"

	"go.etcd.io/bbolt/internal/common"
)

type txPending struct {
	ids              []common.Pgid
	alloctx          []common.Txid // txids allocating the ids
	lastReleaseBegin common.Txid   // beginning txid of last matching releaseRange
}

type shared struct {
	Interface

	readonlyTXIDs []common.Txid               // all readonly transaction IDs.
	allocs        map[common.Pgid]common.Txid // mapping of Txid that allocated a pgid.
	cache         map[common.Pgid]struct{}    // fast lookup of all free and pending page ids.
	pending       map[common.Txid]*txPending  // mapping of soon-to-be free page ids by tx.
}

func newShared() *shared {
	return &shared{
		pending: make(map[common.Txid]*txPending),
		allocs:  make(map[common.Pgid]common.Txid),
		cache:   make(map[common.Pgid]struct{}),
	}
}

func (t *shared) pendingPageIds() map[common.Txid]*txPending {
	return t.pending
}

func (t *shared) PendingCount() int {
	var count int
	for _, txp := range t.pending {
		count += len(txp.ids)
	}
	return count
}

func (t *shared) Count() int {
	return t.FreeCount() + t.PendingCount()
}

func (t *shared) Freed(pgId common.Pgid) bool {
	_, ok := t.cache[pgId]
	return ok
}

func (t *shared) Free(txid common.Txid, p *common.Page) {
	if p.Id() <= 1 {
		panic(fmt.Sprintf("cannot free page 0 or 1: %d", p.Id()))
	}

	// Free page and all its overflow pages.
	txp := t.pending[txid]
	if txp == nil {
		txp = &txPending{}
		t.pending[txid] = txp
	}
	allocTxid, ok := t.allocs[p.Id()]
	common.Verify(func() {
		if allocTxid == txid {
			panic(fmt.Sprintf("free: freed page (%d) was allocated by the same transaction (%d)", p.Id(), txid))
		}
	})
	if ok {
		delete(t.allocs, p.Id())
	}

	for id := p.Id(); id <= p.Id()+common.Pgid(p.Overflow()); id++ {
		// Verify that page is not already free.
		if _, ok := t.cache[id]; ok {
			panic(fmt.Sprintf("page %d already freed", id))
		}
		// Add to the freelist and cache.
		txp.ids = append(txp.ids, id)
		txp.alloctx = append(txp.alloctx, allocTxid)
		t.cache[id] = struct{}{}
	}
}

func (t *shared) Rollback(txid common.Txid) {
	// Remove page ids from cache.
	txp := t.pending[txid]
	if txp == nil {
		return
	}
	for i, pgid := range txp.ids {
		delete(t.cache, pgid)
		tx := txp.alloctx[i]
		if tx == 0 {
			continue
		}
		if tx != txid {
			// Pending free aborted; restore page back to alloc list.
			t.allocs[pgid] = tx
		} else {
			// A writing TXN should never free a page which was allocated by itself.
			panic(fmt.Sprintf("rollback: freed page (%d) was allocated by the same transaction (%d)", pgid, txid))
		}
	}
	// Remove pages from pending list and mark as free if allocated by txid.
	delete(t.pending, txid)

	// Remove pgids which are allocated by this txid
	for pgid, tid := range t.allocs {
		if tid == txid {
			delete(t.allocs, pgid)
		}
	}
}

func (t *shared) AddReadonlyTXID(tid common.Txid) {
	t.readonlyTXIDs = append(t.readonlyTXIDs, tid)
}

func (t *shared) RemoveReadonlyTXID(tid common.Txid) {
	for i := range t.readonlyTXIDs {
		if t.readonlyTXIDs[i] == tid {
			last := len(t.readonlyTXIDs) - 1
			t.readonlyTXIDs[i] = t.readonlyTXIDs[last]
			t.readonlyTXIDs = t.readonlyTXIDs[:last]
			break
		}
	}
}

type txIDx []common.Txid

func (t txIDx) Len() int           { return len(t) }
func (t txIDx) Swap(i, j int)      { t[i], t[j] = t[j], t[i] }
func (t txIDx) Less(i, j int) bool { return t[i] < t[j] }

func (t *shared) ReleasePendingPages() {
	// Free all pending pages prior to the earliest open transaction.
	sort.Sort(txIDx(t.readonlyTXIDs))
	minid := common.Txid(math.MaxUint64)
	if len(t.readonlyTXIDs) > 0 {
		minid = t.readonlyTXIDs[0]
	}
	if minid > 0 {
		t.release(minid - 1)
	}
	// Release unused txid extents.
	for _, tid := range t.readonlyTXIDs {
		t.releaseRange(minid, tid-1)
		minid = tid + 1
	}
	t.releaseRange(minid, common.Txid(math.MaxUint64))
	// Any page both allocated and freed in an extent is safe to release.
}

func (t *shared) release(txid common.Txid) {
	m := make(common.Pgids, 0)
	for tid, txp := range t.pending {
		if tid <= txid {
			// Move transaction's pending pages to the available freelist.
			// Don't remove from the cache since the page is still free.
			m = append(m, txp.ids...)
			delete(t.pending, tid)
		}
	}
	t.mergeSpans(m)
}

func (t *shared) releaseRange(begin, end common.Txid) {
	if begin > end {
		return
	}
	m := common.Pgids{}
	for tid, txp := range t.pending {
		if tid < begin || tid > end {
			continue
		}
		// Don't recompute freed pages if ranges haven't updated.
		if txp.lastReleaseBegin == begin {
			continue
		}
		for i := 0; i < len(txp.ids); i++ {
			if atx := txp.alloctx[i]; atx < begin || atx > end {
				continue
			}
			m = append(m, txp.ids[i])
			txp.ids[i] = txp.ids[len(txp.ids)-1]
			txp.ids = txp.ids[:len(txp.ids)-1]
			txp.alloctx[i] = txp.alloctx[len(txp.alloctx)-1]
			txp.alloctx = txp.alloctx[:len(txp.alloctx)-1]
			i--
		}
		txp.lastReleaseBegin = begin
		if len(txp.ids) == 0 {
			delete(t.pending, tid)
		}
	}
	t.mergeSpans(m)
}

// Copyall copies a list of all free ids and all pending ids in one sorted list.
// f.count returns the minimum length required for dst.
func (t *shared) Copyall(dst []common.Pgid) {
	m := make(common.Pgids, 0, t.PendingCount())
	for _, txp := range t.pendingPageIds() {
		m = append(m, txp.ids...)
	}
	sort.Sort(m)
	common.Mergepgids(dst, t.freePageIds(), m)
}

func (t *shared) Reload(p *common.Page) {
	t.Read(p)
	t.NoSyncReload(t.freePageIds())
}

func (t *shared) NoSyncReload(pgIds common.Pgids) {
	// Build a cache of only pending pages.
	pcache := make(map[common.Pgid]struct{})
	for _, txp := range t.pending {
		for _, pendingID := range txp.ids {
			pcache[pendingID] = struct{}{}
		}
	}

	// Check each page in the freelist and build a new available freelist
	// with any pages not in the pending lists.
	a := []common.Pgid{}
	for _, id := range pgIds {
		if _, ok := pcache[id]; !ok {
			a = append(a, id)
		}
	}

	t.Init(a)
}

// reindex rebuilds the free cache based on available and pending free lists.
func (t *shared) reindex() {
	free := t.freePageIds()
	pending := t.pendingPageIds()
	t.cache = make(map[common.Pgid]struct{}, len(free))
	for _, id := range free {
		t.cache[id] = struct{}{}
	}
	for _, txp := range pending {
		for _, pendingID := range txp.ids {
			t.cache[pendingID] = struct{}{}
		}
	}
}

func (t *shared) Read(p *common.Page) {
	if !p.IsFreelistPage() {
		panic(fmt.Sprintf("invalid freelist page: %d, page type is %s", p.Id(), p.Typ()))
	}

	ids := p.FreelistPageIds()

	// Copy the list of page ids from the freelist.
	if len(ids) == 0 {
		t.Init([]common.Pgid{})
	} else {
		// copy the ids, so we don't modify on the freelist page directly
		idsCopy := make([]common.Pgid, len(ids))
		copy(idsCopy, ids)
		// Make sure they're sorted.
		sort.Sort(common.Pgids(idsCopy))

		t.Init(idsCopy)
	}
}

func (t *shared) EstimatedWritePageSize() int {
	n := t.Count()
	if n >= 0xFFFF {
		// The first element will be used to store the count. See freelist.write.
		n++
	}
	return int(common.PageHeaderSize) + (int(unsafe.Sizeof(common.Pgid(0))) * n)
}

func (t *shared) Write(p *common.Page) {
	// Combine the old free pgids and pgids waiting on an open transaction.

	// Update the header flag.
	p.SetFlags(common.FreelistPageFlag)

	// The page.count can only hold up to 64k elements so if we overflow that
	// number then we handle it by putting the size in the first element.
	l := t.Count()
	if l == 0 {
		p.SetCount(uint16(l))
	} else if l < 0xFFFF {
		p.SetCount(uint16(l))
		data := common.UnsafeAdd(unsafe.Pointer(p), unsafe.Sizeof(*p))
		ids := unsafe.Slice((*common.Pgid)(data), l)
		t.Copyall(ids)
	} else {
		p.SetCount(0xFFFF)
		data := common.UnsafeAdd(unsafe.Pointer(p), unsafe.Sizeof(*p))
		ids := unsafe.Slice((*common.Pgid)(data), l+1)
		ids[0] = common.Pgid(l)
		t.Copyall(ids[1:])
	}
}
```

## File: `internal/guts_cli/guts_cli.go`
```go
package guts_cli

// Low level access to pages / data-structures of the bbolt file.

import (
	"errors"
	"fmt"
	"io"
	"os"

	"go.etcd.io/bbolt/internal/common"
)

var (
	// ErrCorrupt is returned when a checking a data file finds errors.
	ErrCorrupt = errors.New("invalid value")
)

// ReadPage reads Page info & full Page data from a path.
// This is not transactionally safe.
func ReadPage(path string, pageID uint64) (*common.Page, []byte, error) {
	// Find Page size.
	pageSize, hwm, err := ReadPageAndHWMSize(path)
	if err != nil {
		return nil, nil, fmt.Errorf("read Page size: %s", err)
	}

	// Open database file.
	f, err := os.Open(path)
	if err != nil {
		return nil, nil, err
	}
	defer f.Close()

	// Read one block into buffer.
	buf := make([]byte, pageSize)
	if n, err := f.ReadAt(buf, int64(pageID*pageSize)); err != nil {
		return nil, nil, err
	} else if n != len(buf) {
		return nil, nil, io.ErrUnexpectedEOF
	}

	// Determine total number of blocks.
	p := common.LoadPage(buf)
	if p.Id() != common.Pgid(pageID) {
		return nil, nil, fmt.Errorf("error: %w due to unexpected Page id: %d != %d", ErrCorrupt, p.Id(), pageID)
	}
	overflowN := p.Overflow()
	if overflowN >= uint32(hwm)-3 { // we exclude 2 Meta pages and the current Page.
		return nil, nil, fmt.Errorf("error: %w, Page claims to have %d overflow pages (>=hwm=%d). Interrupting to avoid risky OOM", ErrCorrupt, overflowN, hwm)
	}

	if overflowN == 0 {
		return p, buf, nil
	}

	// Re-read entire Page (with overflow) into buffer.
	buf = make([]byte, (uint64(overflowN)+1)*pageSize)
	if n, err := f.ReadAt(buf, int64(pageID*pageSize)); err != nil {
		return nil, nil, err
	} else if n != len(buf) {
		return nil, nil, io.ErrUnexpectedEOF
	}
	p = common.LoadPage(buf)
	if p.Id() != common.Pgid(pageID) {
		return nil, nil, fmt.Errorf("error: %w due to unexpected Page id: %d != %d", ErrCorrupt, p.Id(), pageID)
	}

	return p, buf, nil
}

func WritePage(path string, pageBuf []byte) error {
	page := common.LoadPage(pageBuf)
	pageSize, _, err := ReadPageAndHWMSize(path)
	if err != nil {
		return err
	}
	expectedLen := pageSize * (uint64(page.Overflow()) + 1)
	if expectedLen != uint64(len(pageBuf)) {
		return fmt.Errorf("WritePage: len(buf):%d != pageSize*(overflow+1):%d", len(pageBuf), expectedLen)
	}
	f, err := os.OpenFile(path, os.O_WRONLY, 0)
	if err != nil {
		return err
	}
	defer f.Close()
	_, err = f.WriteAt(pageBuf, int64(page.Id())*int64(pageSize))
	return err
}

// ReadPageAndHWMSize reads Page size and HWM (id of the last+1 Page).
// This is not transactionally safe.
func ReadPageAndHWMSize(path string) (uint64, common.Pgid, error) {
	// Open database file.
	f, err := os.Open(path)
	if err != nil {
		return 0, 0, err
	}
	defer f.Close()

	// Read 4KB chunk.
	buf := make([]byte, 4096)
	if _, err := io.ReadFull(f, buf); err != nil {
		return 0, 0, err
	}

	// Read Page size from metadata.
	m := common.LoadPageMeta(buf)
	if m.Magic() != common.Magic {
		return 0, 0, fmt.Errorf("the Meta Page has wrong (unexpected) magic")
	}
	return uint64(m.PageSize()), common.Pgid(m.Pgid()), nil
}

// GetRootPage returns the root-page (according to the most recent transaction).
func GetRootPage(path string) (root common.Pgid, activeMeta common.Pgid, err error) {
	m, id, err := GetActiveMetaPage(path)
	if err != nil {
		return 0, id, err
	}
	return m.RootBucket().RootPage(), id, nil
}

// GetActiveMetaPage returns the active meta page and its page ID (0 or 1).
func GetActiveMetaPage(path string) (*common.Meta, common.Pgid, error) {
	_, buf0, err0 := ReadPage(path, 0)
	if err0 != nil {
		return nil, 0, err0
	}
	m0 := common.LoadPageMeta(buf0)
	_, buf1, err1 := ReadPage(path, 1)
	if err1 != nil {
		return nil, 1, err1
	}
	m1 := common.LoadPageMeta(buf1)
	if m0.Txid() < m1.Txid() {
		return m1, 1, nil
	} else {
		return m0, 0, nil
	}
}
```

## File: `internal/surgeon/surgeon.go`
```go
package surgeon

import (
	"fmt"

	"go.etcd.io/bbolt/internal/common"
	"go.etcd.io/bbolt/internal/guts_cli"
)

func CopyPage(path string, srcPage common.Pgid, target common.Pgid) error {
	p1, d1, err1 := guts_cli.ReadPage(path, uint64(srcPage))
	if err1 != nil {
		return err1
	}
	p1.SetId(target)
	return guts_cli.WritePage(path, d1)
}

func ClearPage(path string, pgId common.Pgid) (bool, error) {
	return ClearPageElements(path, pgId, 0, -1, false)
}

// ClearPageElements supports clearing elements in both branch and leaf
// pages. Note if the ${abandonFreelist} is true, the freelist may be cleaned
// in the meta pages in the following two cases, and bbolt needs to scan the
// db to reconstruct free list. It may cause some delay on next startup,
// depending on the db size.
//  1. Any branch elements are cleared;
//  2. An object saved in overflow pages is cleared;
//
// Usually ${abandonFreelist} defaults to false, it means it will not clear the
// freelist in meta pages automatically. Users will receive a warning message
// to remind them to explicitly execute `bbolt surgery abandom-freelist`
// afterwards; the first return parameter will be true in such case. But if
// the freelist isn't synced at all, no warning message will be displayed.
func ClearPageElements(path string, pgId common.Pgid, start, end int, abandonFreelist bool) (bool, error) {
	// Read the page
	p, buf, err := guts_cli.ReadPage(path, uint64(pgId))
	if err != nil {
		return false, fmt.Errorf("ReadPage failed: %w", err)
	}

	if !p.IsLeafPage() && !p.IsBranchPage() {
		return false, fmt.Errorf("can't clear elements in %q page", p.Typ())
	}

	elementCnt := int(p.Count())

	if elementCnt == 0 {
		return false, nil
	}

	if start < 0 || start >= elementCnt {
		return false, fmt.Errorf("the start index (%d) is out of range [0, %d)", start, elementCnt)
	}

	if (end < 0 || end > elementCnt) && end != -1 {
		return false, fmt.Errorf("the end index (%d) is out of range [0, %d]", end, elementCnt)
	}

	if start > end && end != -1 {
		return false, fmt.Errorf("the start index (%d) is bigger than the end index (%d)", start, end)
	}

	if start == end {
		return false, fmt.Errorf("invalid: the start index (%d) is equal to the end index (%d)", start, end)
	}

	preOverflow := p.Overflow()

	var (
		dataWritten uint32
	)
	if end == int(p.Count()) || end == -1 {
		inodes := common.ReadInodeFromPage(p)
		inodes = inodes[:start]

		p.SetCount(uint16(start))
		// no need to write inode & data again, we just need to get
		// the data size which will be kept.
		dataWritten = common.UsedSpaceInPage(inodes, p)
	} else {
		inodes := common.ReadInodeFromPage(p)
		inodes = append(inodes[:start], inodes[end:]...)

		p.SetCount(uint16(len(inodes)))
		dataWritten = common.WriteInodeToPage(inodes, p)
	}

	pageSize, _, err := guts_cli.ReadPageAndHWMSize(path)
	if err != nil {
		return false, fmt.Errorf("ReadPageAndHWMSize failed: %w", err)
	}
	if dataWritten%uint32(pageSize) == 0 {
		p.SetOverflow(dataWritten/uint32(pageSize) - 1)
	} else {
		p.SetOverflow(dataWritten / uint32(pageSize))
	}

	datasz := pageSize * (uint64(p.Overflow()) + 1)
	if err := guts_cli.WritePage(path, buf[0:datasz]); err != nil {
		return false, fmt.Errorf("WritePage failed: %w", err)
	}

	if preOverflow != p.Overflow() || p.IsBranchPage() {
		if abandonFreelist {
			return false, ClearFreelist(path)
		}
		return true, nil
	}

	return false, nil
}

func ClearFreelist(path string) error {
	if err := clearFreelistInMetaPage(path, 0); err != nil {
		return fmt.Errorf("clearFreelist on meta page 0 failed: %w", err)
	}
	if err := clearFreelistInMetaPage(path, 1); err != nil {
		return fmt.Errorf("clearFreelist on meta page 1 failed: %w", err)
	}
	return nil
}

func clearFreelistInMetaPage(path string, pageId uint64) error {
	_, buf, err := guts_cli.ReadPage(path, pageId)
	if err != nil {
		return fmt.Errorf("ReadPage %d failed: %w", pageId, err)
	}

	meta := common.LoadPageMeta(buf)
	meta.SetFreelist(common.PgidNoFreelist)
	meta.SetChecksum(meta.Sum64())

	if err := guts_cli.WritePage(path, buf); err != nil {
		return fmt.Errorf("WritePage %d failed: %w", pageId, err)
	}

	return nil
}

// RevertMetaPage replaces the newer metadata page with the older.
// It usually means that one transaction is being lost. But frequently
// data corruption happens on the last transaction pages and the
// previous state is consistent.
func RevertMetaPage(path string) error {
	_, activeMetaPage, err := guts_cli.GetRootPage(path)
	if err != nil {
		return err
	}
	if activeMetaPage == 0 {
		return CopyPage(path, 1, 0)
	} else {
		return CopyPage(path, 0, 1)
	}
}
```

## File: `internal/surgeon/surgeon_test.go`
```go
package surgeon_test

import (
	"fmt"
	"testing"

	"github.com/stretchr/testify/assert"

	bolt "go.etcd.io/bbolt"
	"go.etcd.io/bbolt/internal/btesting"
	"go.etcd.io/bbolt/internal/surgeon"
)

func TestRevertMetaPage(t *testing.T) {
	db := btesting.MustCreateDB(t)
	assert.NoError(t,
		db.Fill([]byte("data"), 1, 500,
			func(tx int, k int) []byte { return []byte(fmt.Sprintf("%04d", k)) },
			func(tx int, k int) []byte { return make([]byte, 100) },
		))
	assert.NoError(t,
		db.Update(
			func(tx *bolt.Tx) error {
				b := tx.Bucket([]byte("data"))
				assert.NoError(t, b.Put([]byte("0123"), []byte("new Value for 123")))
				assert.NoError(t, b.Put([]byte("1234b"), []byte("additional object")))
				assert.NoError(t, b.Delete([]byte("0246")))
				return nil
			}))

	assert.NoError(t,
		db.View(
			func(tx *bolt.Tx) error {
				b := tx.Bucket([]byte("data"))
				assert.Equal(t, []byte("new Value for 123"), b.Get([]byte("0123")))
				assert.Equal(t, []byte("additional object"), b.Get([]byte("1234b")))
				assert.Nil(t, b.Get([]byte("0246")))
				return nil
			}))

	db.Close()

	// This causes the whole tree to be linked to the previous state
	assert.NoError(t, surgeon.RevertMetaPage(db.Path()))

	db.MustReopen()
	db.MustCheck()
	assert.NoError(t,
		db.View(
			func(tx *bolt.Tx) error {
				b := tx.Bucket([]byte("data"))
				assert.Equal(t, make([]byte, 100), b.Get([]byte("0123")))
				assert.Nil(t, b.Get([]byte("1234b")))
				assert.Equal(t, make([]byte, 100), b.Get([]byte("0246")))
				return nil
			}))
}
```

## File: `internal/surgeon/xray.go`
```go
package surgeon

// Library contains raw access to bbolt files for sake of testing or fixing of corrupted files.
//
// The library must not be used bbolt btree - just by CLI or tests.
// It's not optimized for performance.

import (
	"bytes"
	"fmt"

	"go.etcd.io/bbolt/internal/common"
	"go.etcd.io/bbolt/internal/guts_cli"
)

type XRay struct {
	path string
}

func NewXRay(path string) XRay {
	return XRay{path}
}

func (n XRay) traverse(stack []common.Pgid, callback func(page *common.Page, stack []common.Pgid) error) error {
	p, data, err := guts_cli.ReadPage(n.path, uint64(stack[len(stack)-1]))
	if err != nil {
		return fmt.Errorf("failed reading page (stack %v): %w", stack, err)
	}
	err = callback(p, stack)
	if err != nil {
		return fmt.Errorf("failed callback for page (stack %v): %w", stack, err)
	}
	switch p.Typ() {
	case "meta":
		{
			m := common.LoadPageMeta(data)
			r := m.RootBucket().RootPage()
			return n.traverse(append(stack, r), callback)
		}
	case "branch":
		{
			for i := uint16(0); i < p.Count(); i++ {
				bpe := p.BranchPageElement(i)
				if err := n.traverse(append(stack, bpe.Pgid()), callback); err != nil {
					return err
				}
			}
		}
	case "leaf":
		for i := uint16(0); i < p.Count(); i++ {
			lpe := p.LeafPageElement(i)
			if lpe.IsBucketEntry() {
				pgid := lpe.Bucket().RootPage()
				if pgid > 0 {
					if err := n.traverse(append(stack, pgid), callback); err != nil {
						return err
					}
				} else {
					inlinePage := lpe.Bucket().InlinePage(lpe.Value())
					if err := callback(inlinePage, stack); err != nil {
						return fmt.Errorf("failed callback for inline page  (stack %v): %w", stack, err)
					}
				}
			}
		}
	case "freelist":
		return nil
		// Free does not have children.
	}
	return nil
}

// FindPathsToKey finds all paths from root to the page that contains the given key.
// As it traverses multiple buckets, so in theory there might be multiple keys with the given name.
// Note: For simplicity it's currently implemented as traversing of the whole reachable tree.
// If key is a bucket name, a page-path referencing the key will be returned as well.
func (n XRay) FindPathsToKey(key []byte) ([][]common.Pgid, error) {
	var found [][]common.Pgid

	rootPage, _, err := guts_cli.GetRootPage(n.path)
	if err != nil {
		return nil, err
	}
	err = n.traverse([]common.Pgid{rootPage},
		func(page *common.Page, stack []common.Pgid) error {
			if page.Typ() == "leaf" {
				for i := uint16(0); i < page.Count(); i++ {
					if bytes.Equal(page.LeafPageElement(i).Key(), key) {
						var copyPath []common.Pgid
						copyPath = append(copyPath, stack...)
						found = append(found, copyPath)
					}
				}
			}
			return nil
		})
	if err != nil {
		return nil, err
	} else {
		return found, nil
	}
}
```

## File: `internal/surgeon/xray_test.go`
```go
package surgeon_test

import (
	"fmt"
	"testing"

	"github.com/stretchr/testify/assert"
	"github.com/stretchr/testify/require"

	"go.etcd.io/bbolt"
	"go.etcd.io/bbolt/internal/btesting"
	"go.etcd.io/bbolt/internal/guts_cli"
	"go.etcd.io/bbolt/internal/surgeon"
)

func TestFindPathsToKey(t *testing.T) {
	db := btesting.MustCreateDB(t)
	assert.NoError(t,
		db.Fill([]byte("data"), 1, 500,
			func(tx int, k int) []byte { return []byte(fmt.Sprintf("%04d", k)) },
			func(tx int, k int) []byte { return make([]byte, 100) },
		))
	assert.NoError(t, db.Close())

	navigator := surgeon.NewXRay(db.Path())
	path1, err := navigator.FindPathsToKey([]byte("0451"))
	assert.NoError(t, err)
	assert.NotEmpty(t, path1)

	page := path1[0][len(path1[0])-1]
	p, _, err := guts_cli.ReadPage(db.Path(), uint64(page))
	assert.NoError(t, err)
	assert.GreaterOrEqual(t, []byte("0451"), p.LeafPageElement(0).Key())
	assert.LessOrEqual(t, []byte("0451"), p.LeafPageElement(p.Count()-1).Key())
}

func TestFindPathsToKey_Bucket(t *testing.T) {
	rootBucket := []byte("data")
	subBucket := []byte("0451A")

	db := btesting.MustCreateDB(t)
	assert.NoError(t,
		db.Fill(rootBucket, 1, 500,
			func(tx int, k int) []byte { return []byte(fmt.Sprintf("%04d", k)) },
			func(tx int, k int) []byte { return make([]byte, 100) },
		))
	require.NoError(t, db.Update(func(tx *bbolt.Tx) error {
		sb, err := tx.Bucket(rootBucket).CreateBucket(subBucket)
		require.NoError(t, err)
		require.NoError(t, sb.Put([]byte("foo"), []byte("bar")))
		return nil
	}))

	assert.NoError(t, db.Close())

	navigator := surgeon.NewXRay(db.Path())
	path1, err := navigator.FindPathsToKey(subBucket)
	assert.NoError(t, err)
	assert.NotEmpty(t, path1)

	page := path1[0][len(path1[0])-1]
	p, _, err := guts_cli.ReadPage(db.Path(), uint64(page))
	assert.NoError(t, err)
	assert.GreaterOrEqual(t, subBucket, p.LeafPageElement(0).Key())
	assert.LessOrEqual(t, subBucket, p.LeafPageElement(p.Count()-1).Key())
}
```

## File: `internal/tests/tx_check_test.go`
```go
package tests_test

import (
	"fmt"
	"testing"

	"github.com/stretchr/testify/require"

	bolt "go.etcd.io/bbolt"
	"go.etcd.io/bbolt/internal/btesting"
	"go.etcd.io/bbolt/internal/guts_cli"
	"go.etcd.io/bbolt/internal/surgeon"
)

func TestTx_RecursivelyCheckPages_MisplacedPage(t *testing.T) {
	db := btesting.MustCreateDB(t)
	db.ForceDisableStrictMode()
	require.NoError(t,
		db.Fill([]byte("data"), 1, 10000,
			func(tx int, k int) []byte { return []byte(fmt.Sprintf("%04d", k)) },
			func(tx int, k int) []byte { return make([]byte, 100) },
		))
	require.NoError(t, db.Close())

	xRay := surgeon.NewXRay(db.Path())

	path1, err := xRay.FindPathsToKey([]byte("0451"))
	require.NoError(t, err, "cannot find page that contains key:'0451'")
	require.Len(t, path1, 1, "Expected only one page that contains key:'0451'")

	path2, err := xRay.FindPathsToKey([]byte("7563"))
	require.NoError(t, err, "cannot find page that contains key:'7563'")
	require.Len(t, path2, 1, "Expected only one page that contains key:'7563'")

	srcPage := path1[0][len(path1[0])-1]
	targetPage := path2[0][len(path2[0])-1]
	require.NoError(t, surgeon.CopyPage(db.Path(), srcPage, targetPage))

	db.MustReopen()
	db.ForceDisableStrictMode()
	require.NoError(t, db.Update(func(tx *bolt.Tx) error {
		// Collect all the errors.
		var errors []error
		for err := range tx.Check() {
			errors = append(errors, err)
		}
		require.Len(t, errors, 1)
		require.ErrorContains(t, errors[0], fmt.Sprintf("leaf page(%v) needs to be >= the key in the ancestor", targetPage))
		return nil
	}))
	require.NoError(t, db.Close())
}

func TestTx_RecursivelyCheckPages_CorruptedLeaf(t *testing.T) {
	db := btesting.MustCreateDB(t)
	db.ForceDisableStrictMode()
	require.NoError(t,
		db.Fill([]byte("data"), 1, 10000,
			func(tx int, k int) []byte { return []byte(fmt.Sprintf("%04d", k)) },
			func(tx int, k int) []byte { return make([]byte, 100) },
		))
	require.NoError(t, db.Close())

	xray := surgeon.NewXRay(db.Path())

	path1, err := xray.FindPathsToKey([]byte("0451"))
	require.NoError(t, err, "cannot find page that contains key:'0451'")
	require.Len(t, path1, 1, "Expected only one page that contains key:'0451'")

	srcPage := path1[0][len(path1[0])-1]
	p, pbuf, err := guts_cli.ReadPage(db.Path(), uint64(srcPage))
	require.NoError(t, err)
	require.Positive(t, p.Count(), "page must be not empty")
	p.LeafPageElement(p.Count() / 2).Key()[0] = 'z'
	require.NoError(t, guts_cli.WritePage(db.Path(), pbuf))

	db.MustReopen()
	db.ForceDisableStrictMode()
	require.NoError(t, db.Update(func(tx *bolt.Tx) error {
		// Collect all the errors.
		var errors []error
		for err := range tx.Check() {
			errors = append(errors, err)
		}
		require.Len(t, errors, 2)
		require.ErrorContains(t, errors[0], fmt.Sprintf("leaf page(%v) needs to be < than key of the next element in ancestor", srcPage))
		require.ErrorContains(t, errors[1], fmt.Sprintf("leaf page(%v) needs to be > (found <) than previous element", srcPage))
		return nil
	}))
	require.NoError(t, db.Close())
}
```

## File: `scripts/compare_benchmarks.sh`
```bash
#!/usr/bin/env bash
# https://github.com/kubernetes/kube-state-metrics/blob/main/tests/compare_benchmarks.sh (originally written by mxinden)

# exit immediately when a command fails
set -e
# only exit with zero if all commands of the pipeline exit successfully
set -o pipefail
# error on unset variables
set -u

[[ "$#" -eq 1 ]] || echo "One argument required, $# provided."

REF_CURRENT="$(git rev-parse --abbrev-ref HEAD)"
BASE_TO_COMPARE=$1

RESULT_CURRENT="$(mktemp)-${REF_CURRENT}"
RESULT_TO_COMPARE="$(mktemp)-${BASE_TO_COMPARE}"

BENCH_COUNT=${BENCH_COUNT:-10}
BENCHSTAT_CONFIDENCE_LEVEL=${BENCHSTAT_CONFIDENCE_LEVEL:-0.9}
BENCHSTAT_FORMAT=${BENCHSTAT_FORMAT:-"text"}
BENCH_PARAMETERS=${BENCH_PARAMETERS:-"--count 2000000 --batch-size 10000"}

if [[ "${BENCHSTAT_FORMAT}" == "csv" ]] && [[ -z "${BENCHSTAT_OUTPUT_FILE}" ]]; then
  echo "BENCHSTAT_FORMAT is set to csv, but BENCHSTAT_OUTPUT_FILE is not set."
  exit 1
fi

function bench() {
  local output_file
  output_file="$1"
  make build

  for _ in $(seq "$BENCH_COUNT"); do
    echo ./bin/bbolt bench --gobench-output --profile-mode n ${BENCH_PARAMETERS}
    # shellcheck disable=SC2086
    ./bin/bbolt bench --gobench-output --profile-mode n ${BENCH_PARAMETERS} >> "${output_file}"
  done
}

function main() {
  echo "### Benchmarking PR ${REF_CURRENT}"
  bench "${RESULT_CURRENT}"
  echo ""
  echo "### Done benchmarking ${REF_CURRENT}"

  echo "### Benchmarking base ${BASE_TO_COMPARE}"
  git checkout "${BASE_TO_COMPARE}"
  bench "${RESULT_TO_COMPARE}"
  echo ""
  echo "### Done benchmarking ${BASE_TO_COMPARE}"

  git checkout -

  echo ""
  echo "### Result"
  echo "BASE=${BASE_TO_COMPARE} HEAD=${REF_CURRENT}"

  if [[ "${BENCHSTAT_FORMAT}" == "csv" ]]; then
    go tool golang.org/x/perf/cmd/benchstat -format=csv -confidence="${BENCHSTAT_CONFIDENCE_LEVEL}" BASE="${RESULT_TO_COMPARE}" HEAD="${RESULT_CURRENT}" 2>/dev/null 1>"${BENCHSTAT_OUTPUT_FILE}"
  else
    if [[ -z "${BENCHSTAT_OUTPUT_FILE}" ]]; then
      go tool golang.org/x/perf/cmd/benchstat -confidence="${BENCHSTAT_CONFIDENCE_LEVEL}" BASE="${RESULT_TO_COMPARE}" HEAD="${RESULT_CURRENT}"
    else
      go tool golang.org/x/perf/cmd/benchstat -confidence="${BENCHSTAT_CONFIDENCE_LEVEL}" BASE="${RESULT_TO_COMPARE}" HEAD="${RESULT_CURRENT}" 1>"${BENCHSTAT_OUTPUT_FILE}"
    fi
  fi
}

main
```

## File: `scripts/fix.sh`
```bash
GO_CMD="go"

# TODO(ptabor): Expand to cover different architectures (GOOS GOARCH), or just list go files.

GOFILES=$(${GO_CMD} list  --f "{{with \$d:=.}}{{range .GoFiles}}{{\$d.Dir}}/{{.}}{{\"\n\"}}{{end}}{{end}}" ./...)
TESTGOFILES=$(${GO_CMD} list  --f "{{with \$d:=.}}{{range .TestGoFiles}}{{\$d.Dir}}/{{.}}{{\"\n\"}}{{end}}{{end}}" ./...)
XTESTGOFILES=$(${GO_CMD} list  --f "{{with \$d:=.}}{{range .XTestGoFiles}}{{\$d.Dir}}/{{.}}{{\"\n\"}}{{end}}{{end}}" ./...)


echo "${GOFILES}" "${TESTGOFILES}" "${XTESTGOFILES}"| xargs -n 100 go tool golang.org/x/tools/cmd/goimports -w -local go.etcd.io

go fmt ./...
go mod tidy
```

## File: `scripts/release.sh`
```bash
#!/usr/bin/env bash

set -o errexit
set -o nounset
set -o pipefail

# === Function Definitions ===
function get_gpg_key {
  local git_email
  local key_id

  git_email=$(git config --get user.email)
  key_id=$(gpg --list-keys --with-colons "${git_email}" | awk -F: '/^pub:/ { print $5 }')
  if [[ -z "${key_id}" ]]; then
    echo "Failed to load gpg key. Is gpg set up correctly for etcd releases?"
    return 2
  fi
  echo "${key_id}"
}

# === Main Script Logic ===
function main {
  VERSION="$1"

  if [ -z "${VERSION}" ]; then
    read -p "Release version (e.g., v1.2.3) " -r VERSION
    if [[ ! "${VERSION}" =~ ^v[0-9]+.[0-9]+.[0-9]+ ]]; then
      echo "Expected 'version' param of the form 'v<major-version>.<minor-version>.<patch-version>' but got '${VERSION}'"
      exit 1
    fi
  fi

  VERSION=v${VERSION#v}
  RELEASE_VERSION="${VERSION#v}"
  MINOR_VERSION=$(echo "${RELEASE_VERSION}" | cut -d. -f 1-2)
  RELEASE_BRANCH="release-${MINOR_VERSION}"

  REPOSITORY=${REPOSITORY:-"git@github.com:etcd-io/bbolt.git"}

  local remote_tag_exists
  remote_tag_exists=$(git ls-remote "${REPOSITORY}" "refs/tags/${VERSION}" | grep -c "${VERSION}" || true)
  if [ "${remote_tag_exists}" -gt 0 ]; then
    echo "Release version tag exists on remote."
    exit 1
  fi

  # Set up release directory.
  local reldir="/tmp/bbolt-release-${VERSION}"
  echo "Preparing temporary directory: ${reldir}"
  if [ ! -d "${reldir}/bbolt" ]; then
    mkdir -p "${reldir}"
    cd "${reldir}"
    git clone "${REPOSITORY}" --branch "${RELEASE_BRANCH}" --depth 1
  fi
  cd "${reldir}/bbolt" || exit 2
  git checkout "${RELEASE_BRANCH}" || exit 2
  git fetch origin
  git reset --hard "origin/${RELEASE_BRANCH}"

  # ensuring the minor-version is identical.
  source_version=$(grep -E "\s+Version\s*=" ./version/version.go | sed -e "s/.*\"\(.*\)\".*/\1/g")
  if [[ "${source_version}" != "${RELEASE_VERSION}" ]]; then
     source_minor_version=$(echo "${source_version}" | cut -d. -f 1-2)
     if [[ "${source_minor_version}" != "${MINOR_VERSION}" ]]; then
       echo "Wrong bbolt minor version in version.go. Expected ${MINOR_VERSION} but got ${source_minor_version}. Aborting."
       exit 1
     fi
  fi

  # bump 'version.go'.
  echo "Updating version from '${source_version}' to '${RELEASE_VERSION}' in 'version.go'"
  if [[ "$OSTYPE" == "darwin"* ]]; then
    sed -i '' "s/${source_version}/${RELEASE_VERSION}/g" ./version/version.go
  else
    sed -i "s/${source_version}/${RELEASE_VERSION}/g" ./version/version.go
  fi

  # push 'version.go' to remote.
  echo "committing 'version.go'"
  git add ./version/version.go
  git commit -s -m "Update version to ${VERSION}"
  git push origin "${RELEASE_BRANCH}"
  echo "'version.go' has been committed to remote repo."

  # create tag and push to remote.
  echo "Creating new tag for '${VERSION}'"
  key_id=$(get_gpg_key) || return 2
  git tag --local-user "${key_id}" --sign "${VERSION}" --message "${VERSION}"
  git push origin "${VERSION}"
  echo "Tag '${VERSION}' has been created and pushed to remote repo."
  echo "SUCCESS"
}

main "$1"
```

## File: `tests/dmflakey/dmflakey.go`
```go
//go:build linux

package dmflakey

import (
	"errors"
	"fmt"
	"os"
	"os/exec"
	"path"
	"path/filepath"
	"strings"
	"time"

	"golang.org/x/sys/unix"
)

type featCfg struct {
	// SyncFS attempts to synchronize filesystem before inject failure.
	syncFS bool
	// interval is used to determine the up time for feature.
	//
	// For AllowWrites, it means that the device is available for `interval` seconds.
	// For Other features, the device exhibits unreliable behaviour for
	// `interval` seconds.
	interval time.Duration
}

// Default values.
const (
	// defaultImgSize is the default size for filesystem image.
	defaultImgSize int64 = 1024 * 1024 * 1024 * 10 // 10 GiB
	// defaultInterval is the default interval for the up time of feature.
	defaultInterval = 2 * time.Minute
)

// defaultFeatCfg is the default setting for flakey feature.
var defaultFeatCfg = featCfg{interval: defaultInterval}

// FeatOpt is used to configure failure feature.
type FeatOpt func(*featCfg)

// WithIntervalFeatOpt updates the up time for the feature.
func WithIntervalFeatOpt(interval time.Duration) FeatOpt {
	return func(cfg *featCfg) {
		cfg.interval = interval
	}
}

// WithSyncFSFeatOpt is to determine if the caller wants to synchronize
// filesystem before inject failure.
func WithSyncFSFeatOpt(syncFS bool) FeatOpt {
	return func(cfg *featCfg) {
		cfg.syncFS = syncFS
	}
}

// Flakey is to inject failure into device.
type Flakey interface {
	// DevicePath returns the flakey device path.
	DevicePath() string

	// Filesystem returns filesystem's type.
	Filesystem() FSType

	// AllowWrites allows write I/O.
	AllowWrites(opts ...FeatOpt) error

	// DropWrites drops all write I/O silently.
	DropWrites(opts ...FeatOpt) error

	// ErrorWrites drops all write I/O and returns error.
	ErrorWrites(opts ...FeatOpt) error

	// Teardown releases the flakey device.
	Teardown() error
}

// FSType represents the filesystem name.
type FSType string

// Supported filesystems.
const (
	FSTypeEXT4 FSType = "ext4"
	FSTypeXFS  FSType = "xfs"
)

// InitFlakey creates an filesystem on a loopback device and returns Flakey on it.
//
// The device-mapper device will be /dev/mapper/$flakeyDevice. And the filesystem
// image will be created at $dataStorePath/$flakeyDevice.img. By default, the
// device is available for 2 minutes and size is 10 GiB.
func InitFlakey(flakeyDevice, dataStorePath string, fsType FSType, mkfsOpt string) (_ Flakey, retErr error) {
	imgPath := filepath.Join(dataStorePath, fmt.Sprintf("%s.img", flakeyDevice))
	if err := createEmptyFSImage(imgPath, fsType, mkfsOpt); err != nil {
		return nil, err
	}
	defer func() {
		if retErr != nil {
			os.RemoveAll(imgPath)
		}
	}()

	loopDevice, err := attachToLoopDevice(imgPath)
	if err != nil {
		return nil, err
	}
	defer func() {
		if retErr != nil {
			_ = detachLoopDevice(loopDevice)
		}
	}()

	imgSize, err := getBlkSize(loopDevice)
	if err != nil {
		return nil, err
	}

	if err := newFlakeyDevice(flakeyDevice, loopDevice, defaultInterval); err != nil {
		return nil, err
	}

	return &flakey{
		fsType:  fsType,
		imgPath: imgPath,
		imgSize: imgSize,

		loopDevice:   loopDevice,
		flakeyDevice: flakeyDevice,
	}, nil
}

type flakey struct {
	fsType  FSType
	imgPath string
	imgSize int64

	loopDevice   string
	flakeyDevice string
}

// DevicePath returns the flakey device path.
func (f *flakey) DevicePath() string {
	return fmt.Sprintf("/dev/mapper/%s", f.flakeyDevice)
}

// Filesystem returns filesystem's type.
func (f *flakey) Filesystem() FSType {
	return f.fsType
}

// AllowWrites allows write I/O.
func (f *flakey) AllowWrites(opts ...FeatOpt) error {
	var o = defaultFeatCfg
	for _, opt := range opts {
		opt(&o)
	}

	// NOTE: Table parameters
	//
	// 0 imgSize flakey <dev path> <offset> <up interval> <down interval> [<num_features> [<feature arguments>]]
	//
	// Mandatory parameters:
	//
	//  <dev path>: Full pathname to the underlying block-device, or a "major:minor" device-number.
	//  <offset>: Starting sector within the device.
	//  <up interval>: Number of seconds device is available.
	//  <down interval>: Number of seconds device returns errors.
	//
	// Optional:
	//
	// If no feature parameters are present, during the periods of unreliability, all I/O returns errors.
	//
	// For AllowWrites, the device will handle data correctly in `interval` seconds.
	//
	// REF: https://docs.kernel.org/admin-guide/device-mapper/dm-flakey.html.
	table := fmt.Sprintf("0 %d flakey %s 0 %d 0",
		f.imgSize, f.loopDevice, int(o.interval.Seconds()))

	return reloadFlakeyDevice(f.flakeyDevice, o.syncFS, table)
}

// DropWrites drops all write I/O silently.
func (f *flakey) DropWrites(opts ...FeatOpt) error {
	var o = defaultFeatCfg
	for _, opt := range opts {
		opt(&o)
	}

	// NOTE: Table parameters
	//
	// 0 imgSize flakey <dev path> <offset> <up interval> <down interval> [<num_features> [<feature arguments>]]
	//
	// Mandatory parameters:
	//
	//  <dev path>: Full pathname to the underlying block-device, or a "major:minor" device-number.
	//  <offset>: Starting sector within the device.
	//  <up interval>: Number of seconds device is available.
	//  <down interval>: Number of seconds device returns errors.
	//
	// Optional:
	//
	// <num_features>: How many arguments (length of <feature_arguments>)
	//
	// For DropWrites,
	//
	// num_features: 1 (there is only one argument)
	// feature_arguments: drop_writes
	//
	// The Device will drop all the writes into disk in `interval` seconds.
	// Read I/O is handled correctly.
	//
	// For example, the application calls fsync, all the dirty pages will
	// be flushed into disk ideally. But during DropWrites, device will
	// ignore all the data and return successfully. It can be used to
	// simulate data-loss after power failure.
	//
	// REF: https://docs.kernel.org/admin-guide/device-mapper/dm-flakey.html.
	table := fmt.Sprintf("0 %d flakey %s 0 0 %d 1 drop_writes",
		f.imgSize, f.loopDevice, int(o.interval.Seconds()))

	return reloadFlakeyDevice(f.flakeyDevice, o.syncFS, table)
}

// ErrorWrites drops all write I/O and returns error.
func (f *flakey) ErrorWrites(opts ...FeatOpt) error {
	var o = defaultFeatCfg
	for _, opt := range opts {
		opt(&o)
	}

	// NOTE: Table parameters
	//
	// 0 imgSize flakey <dev path> <offset> <up interval> <down interval> [<num_features> [<feature arguments>]]
	//
	// Mandatory parameters:
	//
	//  <dev path>: Full pathname to the underlying block-device, or a "major:minor" device-number.
	//  <offset>: Starting sector within the device.
	//  <up interval>: Number of seconds device is available.
	//  <down interval>: Number of seconds device returns errors.
	//
	// Optional:
	//
	// <num_features>: How many arguments (length of <feature_arguments>)
	//
	// For ErrorWrites,
	//
	// num_features: 1 (there is only one argument)
	// feature_arguments: error_writes
	//
	// The Device will drop all the writes into disk in `interval` seconds
	// and return failure to caller. Read I/O is handled correctly.
	//
	// REF: https://docs.kernel.org/admin-guide/device-mapper/dm-flakey.html.
	table := fmt.Sprintf("0 %d flakey %s 0 0 %d 1 error_writes",
		f.imgSize, f.loopDevice, int(o.interval.Seconds()))

	return reloadFlakeyDevice(f.flakeyDevice, o.syncFS, table)
}

// Teardown releases the flakey device.
func (f *flakey) Teardown() error {
	// FIXME(XXX): Even though we umount device successfully, it's still
	// possible to run into `Device or resource busy` issue. It's easy to
	// reproduce it in slow storage or 2-4 cores ARM64 host with xfs. We
	// should retry it to fix transisent issue.
	var derr error
	for i := 0; i < 10; i++ {
		derr = deleteFlakeyDevice(f.flakeyDevice)
		if derr != nil {
			if strings.Contains(derr.Error(), "Device or resource busy") {
				time.Sleep(1 * time.Second)
				continue
			}
			if strings.Contains(derr.Error(), "No such device or address") {
				derr = nil
			}
		}
		break
	}
	if derr != nil {
		return derr
	}

	if err := detachLoopDevice(f.loopDevice); err != nil {
		if !errors.Is(err, unix.ENXIO) {
			return err
		}
	}
	return os.RemoveAll(f.imgPath)
}

// createEmptyFSImage creates empty filesystem on dataStorePath folder with
// default size - 10 GiB.
func createEmptyFSImage(imgPath string, fsType FSType, mkfsOpt string) error {
	if err := validateFSType(fsType); err != nil {
		return err
	}

	mkfs, err := exec.LookPath(fmt.Sprintf("mkfs.%s", fsType))
	if err != nil {
		return fmt.Errorf("failed to ensure mkfs.%s: %w", fsType, err)
	}

	if _, err := os.Stat(imgPath); err == nil {
		return fmt.Errorf("failed to create image because %s already exists", imgPath)
	}

	if err := os.MkdirAll(path.Dir(imgPath), 0600); err != nil {
		return fmt.Errorf("failed to ensure parent directory %s: %w", path.Dir(imgPath), err)
	}

	f, err := os.Create(imgPath)
	if err != nil {
		return fmt.Errorf("failed to create image %s: %w", imgPath, err)
	}

	if err = func() error {
		defer f.Close()

		return f.Truncate(defaultImgSize)
	}(); err != nil {
		return fmt.Errorf("failed to truncate image %s with %v bytes: %w",
			imgPath, defaultImgSize, err)
	}

	args := []string{imgPath}
	if mkfsOpt != "" {
		splitArgs := strings.Split(mkfsOpt, " ")
		args = append(splitArgs, imgPath)
	}

	output, err := exec.Command(mkfs, args...).CombinedOutput()
	if err != nil {
		return fmt.Errorf("failed to mkfs on %s (%s %v) (out: %s): %w",
			imgPath, mkfs, args, string(output), err)
	}
	return nil
}

// validateFSType validates the fs type input.
func validateFSType(fsType FSType) error {
	switch fsType {
	case FSTypeEXT4, FSTypeXFS:
		return nil
	default:
		return fmt.Errorf("unsupported filesystem %s", fsType)
	}
}
```

## File: `tests/dmflakey/dmflakey_test.go`
```go
//go:build linux

package dmflakey

import (
	"errors"
	"flag"
	"fmt"
	"os"
	"os/exec"
	"path/filepath"
	"testing"
	"time"

	"github.com/stretchr/testify/assert"
	"github.com/stretchr/testify/require"
	"golang.org/x/sys/unix"

	testutils "go.etcd.io/bbolt/tests/utils"
)

func TestMain(m *testing.M) {
	flag.Parse()
	testutils.RequiresRoot()
	os.Exit(m.Run())
}

func TestBasic(t *testing.T) {
	for _, fsType := range []FSType{FSTypeEXT4, FSTypeXFS} {
		t.Run(string(fsType), func(t *testing.T) {
			tmpDir := t.TempDir()

			flakey, err := InitFlakey("go-dmflakey", tmpDir, fsType, "")
			require.NoError(t, err, "init flakey")
			defer func() {
				assert.NoError(t, flakey.Teardown())
			}()

			target := filepath.Join(tmpDir, "root")
			require.NoError(t, os.MkdirAll(target, 0600))

			require.NoError(t, mount(target, flakey.DevicePath(), ""))
			defer func() {
				assert.NoError(t, unmount(target))
			}()

			file := filepath.Join(target, "test")
			assert.NoError(t, writeFile(file, []byte("hello, world"), 0600, true))

			assert.NoError(t, unmount(target))

			assert.NoError(t, flakey.Teardown())
		})
	}
}

func TestDropWritesExt4(t *testing.T) {
	flakey, root := initFlakey(t, FSTypeEXT4)

	// commit=1000 is to delay commit triggered by writeback thread
	require.NoError(t, mount(root, flakey.DevicePath(), "commit=1000"))

	// ensure testdir/f1 is synced.
	target := filepath.Join(root, "testdir")
	require.NoError(t, os.MkdirAll(target, 0600))

	f1 := filepath.Join(target, "f1")
	assert.NoError(t, writeFile(f1, []byte("hello, world from f1"), 0600, false))
	require.NoError(t, syncfs(f1))

	// testdir/f2 is created but without fsync
	f2 := filepath.Join(target, "f2")
	assert.NoError(t, writeFile(f2, []byte("hello, world from f2"), 0600, false))

	// simulate power failure
	assert.NoError(t, flakey.DropWrites())
	assert.NoError(t, unmount(root))
	assert.NoError(t, flakey.AllowWrites())
	require.NoError(t, mount(root, flakey.DevicePath(), ""))

	data, err := os.ReadFile(f1)
	assert.NoError(t, err)
	assert.Equal(t, "hello, world from f1", string(data))

	_, err = os.ReadFile(f2)
	assert.True(t, errors.Is(err, os.ErrNotExist))
}

func TestErrorWritesExt4(t *testing.T) {
	flakey, root := initFlakey(t, FSTypeEXT4)

	// commit=1000 is to delay commit triggered by writeback thread
	require.NoError(t, mount(root, flakey.DevicePath(), "commit=1000"))

	// inject IO failure on write
	assert.NoError(t, flakey.ErrorWrites())

	f1 := filepath.Join(root, "f1")
	err := writeFile(f1, []byte("hello, world during failpoint"), 0600, true)
	assert.ErrorContains(t, err, "input/output error")

	// resume
	assert.NoError(t, flakey.AllowWrites())
	err = writeFile(f1, []byte("hello, world"), 0600, true)
	assert.NoError(t, err)

	assert.NoError(t, unmount(root))
	require.NoError(t, mount(root, flakey.DevicePath(), ""))

	data, err := os.ReadFile(f1)
	assert.NoError(t, err)
	assert.Equal(t, "hello, world", string(data))
}

func initFlakey(t *testing.T, fsType FSType) (_ Flakey, root string) {
	tmpDir := t.TempDir()

	target := filepath.Join(tmpDir, "root")
	require.NoError(t, os.MkdirAll(target, 0600))

	flakey, err := InitFlakey("go-dmflakey", tmpDir, fsType, "")
	require.NoError(t, err, "init flakey")

	t.Cleanup(func() {
		assert.NoError(t, unmount(target))
		assert.NoError(t, flakey.Teardown())
	})
	return flakey, target
}

func writeFile(name string, data []byte, perm os.FileMode, sync bool) error {
	f, err := os.OpenFile(name, os.O_WRONLY|os.O_CREATE|os.O_TRUNC, perm)
	if err != nil {
		return err
	}
	defer f.Close()

	if _, err = f.Write(data); err != nil {
		return err
	}

	if sync {
		return f.Sync()
	}
	return nil
}

func syncfs(file string) error {
	f, err := os.Open(file)
	if err != nil {
		return fmt.Errorf("failed to open %s: %w", file, err)
	}
	defer f.Close()

	_, _, errno := unix.Syscall(unix.SYS_SYNCFS, uintptr(f.Fd()), 0, 0)
	if errno != 0 {
		return errno
	}
	return nil
}

func mount(target string, devPath string, opt string) error {
	args := []string{"-o", opt, devPath, target}

	output, err := exec.Command("mount", args...).CombinedOutput()
	if err != nil {
		return fmt.Errorf("failed to mount (args: %v) (out: %s): %w",
			args, string(output), err)
	}
	return nil
}

func unmount(target string) error {
	for i := 0; i < 50; i++ {
		if err := unix.Unmount(target, 0); err != nil {
			switch err {
			case unix.EBUSY:
				time.Sleep(500 * time.Millisecond)
				continue
			case unix.EINVAL:
			default:
				return fmt.Errorf("failed to umount %s: %w", target, err)
			}
		}
		return nil
	}
	return unix.EBUSY
}
```

## File: `tests/dmflakey/dmsetup.go`
```go
//go:build linux

package dmflakey

import (
	"fmt"
	"os"
	"os/exec"
	"time"
	"unsafe"

	"golang.org/x/sys/unix"
)

// newFlakeyDevice creates flakey device.
//
// REF: https://docs.kernel.org/admin-guide/device-mapper/dm-flakey.html
func newFlakeyDevice(flakeyDevice, loopDevice string, interval time.Duration) error {
	loopSize, err := getBlkSize(loopDevice)
	if err != nil {
		return fmt.Errorf("failed to get the size of the loop device %s: %w", loopDevice, err)
	}

	// The flakey device will be available in interval.Seconds().
	table := fmt.Sprintf("0 %d flakey %s 0 %d 0",
		loopSize, loopDevice, int(interval.Seconds()))

	args := []string{"create", flakeyDevice, "--table", table}

	output, err := exec.Command("dmsetup", args...).CombinedOutput()
	if err != nil {
		return fmt.Errorf("failed to create flakey device %s with table %s (out: %s): %w",
			flakeyDevice, table, string(output), err)
	}
	return nil
}

// reloadFlakeyDevice reloads the flakey device with feature table.
func reloadFlakeyDevice(flakeyDevice string, syncFS bool, table string) (retErr error) {
	args := []string{"suspend", "--nolockfs", flakeyDevice}
	if syncFS {
		args[1] = flakeyDevice
		args = args[:len(args)-1]
	}

	output, err := exec.Command("dmsetup", args...).CombinedOutput()
	if err != nil {
		return fmt.Errorf("failed to suspend flakey device %s (out: %s): %w",
			flakeyDevice, string(output), err)
	}

	defer func() {
		output, derr := exec.Command("dmsetup", "resume", flakeyDevice).CombinedOutput()
		if derr != nil {
			derr = fmt.Errorf("failed to resume flakey device %s (out: %s): %w",
				flakeyDevice, string(output), derr)
		}

		if retErr == nil {
			retErr = derr
		}
	}()

	output, err = exec.Command("dmsetup", "load", flakeyDevice, "--table", table).CombinedOutput()
	if err != nil {
		return fmt.Errorf("failed to reload flakey device %s with table (%s) (out: %s): %w",
			flakeyDevice, table, string(output), err)
	}
	return nil
}

// removeFlakeyDevice removes flakey device.
func deleteFlakeyDevice(flakeyDevice string) error {
	output, err := exec.Command("dmsetup", "remove", flakeyDevice).CombinedOutput()
	if err != nil {
		return fmt.Errorf("failed to remove flakey device %s (out: %s): %w",
			flakeyDevice, string(output), err)
	}
	return nil
}

// getBlkSize64 gets device size in bytes (BLKGETSIZE64).
//
// REF: https://man7.org/linux/man-pages/man8/blockdev.8.html
func getBlkSize64(device string) (int64, error) {
	deviceFd, err := os.Open(device)
	if err != nil {
		return 0, fmt.Errorf("failed to open device %s: %w", device, err)
	}
	defer deviceFd.Close()

	var size int64
	if _, _, err := unix.Syscall(unix.SYS_IOCTL, deviceFd.Fd(), unix.BLKGETSIZE64, uintptr(unsafe.Pointer(&size))); err != 0 {
		return 0, fmt.Errorf("failed to get block size: %w", err)
	}
	return size, nil
}

// getBlkSize gets size in 512-byte sectors (BLKGETSIZE64 / 512).
//
// REF: https://man7.org/linux/man-pages/man8/blockdev.8.html
func getBlkSize(device string) (int64, error) {
	size, err := getBlkSize64(device)
	return size / 512, err
}
```

## File: `tests/dmflakey/loopback.go`
```go
//go:build linux

package dmflakey

import (
	"errors"
	"fmt"
	"os"
	"time"

	"golang.org/x/sys/unix"
)

const (
	loopControlDevice = "/dev/loop-control"
	loopDevicePattern = "/dev/loop%d"

	maxRetryToAttach = 50
)

// attachToLoopDevice associates free loop device with backing file.
//
// There might have race condition. It needs to retry when it runs into EBUSY.
//
// REF: https://man7.org/linux/man-pages/man4/loop.4.html
func attachToLoopDevice(backingFile string) (string, error) {
	backingFd, err := os.OpenFile(backingFile, os.O_RDWR, 0)
	if err != nil {
		return "", fmt.Errorf("failed to open loop device's backing file %s: %w",
			backingFile, err)
	}
	defer backingFd.Close()

	for i := 0; i < maxRetryToAttach; i++ {
		loop, err := getFreeLoopDevice()
		if err != nil {
			return "", fmt.Errorf("failed to get free loop device: %w", err)
		}

		err = func() error {
			loopFd, err := os.OpenFile(loop, os.O_RDWR, 0)
			if err != nil {
				return err
			}
			defer loopFd.Close()

			return unix.IoctlSetInt(int(loopFd.Fd()),
				unix.LOOP_SET_FD, int(backingFd.Fd()))
		}()
		if err != nil {
			if errors.Is(err, unix.EBUSY) {
				time.Sleep(500 * time.Millisecond)
				continue
			}
			return "", err
		}
		return loop, nil
	}
	return "", fmt.Errorf("failed to associate free loop device with backing file %s after retry %v",
		backingFile, maxRetryToAttach)
}

// detachLoopDevice disassociates the loop device from any backing file.
//
// REF: https://man7.org/linux/man-pages/man4/loop.4.html
func detachLoopDevice(loopDevice string) error {
	loopFd, err := os.Open(loopDevice)
	if err != nil {
		return fmt.Errorf("failed to open loop %s: %w", loopDevice, err)
	}
	defer loopFd.Close()

	return unix.IoctlSetInt(int(loopFd.Fd()), unix.LOOP_CLR_FD, 0)
}

// getFreeLoopDevice allocates or finds a free loop device for use.
//
// REF: https://man7.org/linux/man-pages/man4/loop.4.html
func getFreeLoopDevice() (string, error) {
	control, err := os.OpenFile(loopControlDevice, os.O_RDWR, 0)
	if err != nil {
		return "", fmt.Errorf("failed to open %s: %w", loopControlDevice, err)
	}

	idx, err := unix.IoctlRetInt(int(control.Fd()), unix.LOOP_CTL_GET_FREE)
	control.Close()
	if err != nil {
		return "", fmt.Errorf("failed to get free loop device number: %w", err)
	}
	return fmt.Sprintf(loopDevicePattern, idx), nil
}
```

## File: `tests/failpoint/db_failpoint_test.go`
```go
package failpoint

import (
	crand "crypto/rand"
	"fmt"
	"path/filepath"
	"testing"
	"time"

	"github.com/stretchr/testify/require"

	bolt "go.etcd.io/bbolt"
	"go.etcd.io/bbolt/errors"
	"go.etcd.io/bbolt/internal/btesting"
	"go.etcd.io/bbolt/internal/common"
	"go.etcd.io/bbolt/internal/guts_cli"
	gofail "go.etcd.io/gofail/runtime"
)

func TestFailpoint_MapFail(t *testing.T) {
	err := gofail.Enable("mapError", `return("map somehow failed")`)
	require.NoError(t, err)
	defer func() {
		err = gofail.Disable("mapError")
		require.NoError(t, err)
	}()

	f := filepath.Join(t.TempDir(), "db")
	_, err = bolt.Open(f, 0600, nil)
	require.Error(t, err)
	require.ErrorContains(t, err, "map somehow failed")
}

// ensures when munmap fails, the flock is unlocked
func TestFailpoint_UnmapFail_DbClose(t *testing.T) {
	//unmap error on db close
	//we need to open the db first, and then enable the error.
	//otherwise the db cannot be opened.
	f := filepath.Join(t.TempDir(), "db")

	err := gofail.Enable("unmapError", `return("unmap somehow failed")`)
	require.NoError(t, err)
	_, err = bolt.Open(f, 0600, nil)
	require.Error(t, err)
	require.ErrorContains(t, err, "unmap somehow failed")
	//disable the error, and try to reopen the db
	err = gofail.Disable("unmapError")
	require.NoError(t, err)

	db, err := bolt.Open(f, 0600, &bolt.Options{Timeout: 30 * time.Second})
	require.NoError(t, err)
	err = db.Close()
	require.NoError(t, err)
}

func TestFailpoint_mLockFail(t *testing.T) {
	err := gofail.Enable("mlockError", `return("mlock somehow failed")`)
	require.NoError(t, err)

	f := filepath.Join(t.TempDir(), "db")
	_, err = bolt.Open(f, 0600, &bolt.Options{Mlock: true})
	require.Error(t, err)
	require.ErrorContains(t, err, "mlock somehow failed")

	// It should work after disabling the failpoint.
	err = gofail.Disable("mlockError")
	require.NoError(t, err)

	_, err = bolt.Open(f, 0600, &bolt.Options{Mlock: true})
	require.NoError(t, err)
}

func TestFailpoint_mLockFail_When_remap(t *testing.T) {
	db := btesting.MustCreateDB(t)
	db.Mlock = true

	err := gofail.Enable("mlockError", `return("mlock somehow failed in allocate")`)
	require.NoError(t, err)

	err = db.Fill([]byte("data"), 1, 10000,
		func(tx int, k int) []byte { return []byte(fmt.Sprintf("%04d", k)) },
		func(tx int, k int) []byte { return make([]byte, 100) },
	)

	require.Error(t, err)
	require.ErrorContains(t, err, "mlock somehow failed in allocate")

	// It should work after disabling the failpoint.
	err = gofail.Disable("mlockError")
	require.NoError(t, err)
	db.MustClose()
	db.MustReopen()

	err = db.Fill([]byte("data"), 1, 10000,
		func(tx int, k int) []byte { return []byte(fmt.Sprintf("%04d", k)) },
		func(tx int, k int) []byte { return make([]byte, 100) },
	)

	require.NoError(t, err)
}

func TestFailpoint_ResizeFileFail(t *testing.T) {
	db := btesting.MustCreateDB(t)

	err := gofail.Enable("resizeFileError", `return("resizeFile somehow failed")`)
	require.NoError(t, err)

	err = db.Fill([]byte("data"), 1, 10000,
		func(tx int, k int) []byte { return []byte(fmt.Sprintf("%04d", k)) },
		func(tx int, k int) []byte { return make([]byte, 100) },
	)

	require.Error(t, err)
	require.ErrorContains(t, err, "resizeFile somehow failed")

	// It should work after disabling the failpoint.
	err = gofail.Disable("resizeFileError")
	require.NoError(t, err)
	db.MustClose()
	db.MustReopen()

	err = db.Fill([]byte("data"), 1, 10000,
		func(tx int, k int) []byte { return []byte(fmt.Sprintf("%04d", k)) },
		func(tx int, k int) []byte { return make([]byte, 100) },
	)

	require.NoError(t, err)
}

func TestFailpoint_LackOfDiskSpace(t *testing.T) {
	db := btesting.MustCreateDB(t)

	err := gofail.Enable("lackOfDiskSpace", `return("grow somehow failed")`)
	require.NoError(t, err)

	tx, err := db.Begin(true)
	require.NoError(t, err)

	err = tx.Commit()
	require.Error(t, err)
	require.ErrorContains(t, err, "grow somehow failed")

	err = tx.Rollback()
	require.Error(t, err)
	require.ErrorIs(t, err, errors.ErrTxClosed)

	// It should work after disabling the failpoint.
	err = gofail.Disable("lackOfDiskSpace")
	require.NoError(t, err)

	tx, err = db.Begin(true)
	require.NoError(t, err)

	err = tx.Commit()
	require.NoError(t, err)

	err = tx.Rollback()
	require.Error(t, err)
	require.ErrorIs(t, err, errors.ErrTxClosed)
}

// TestIssue72 reproduces issue 72.
//
// When bbolt is processing a `Put` invocation, the key might be concurrently
// updated by the application which calls the `Put` API (although it shouldn't).
// It might lead to a situation that bbolt use an old key to find a proper
// position to insert the key/value pair, but actually inserts a new key.
// Eventually it might break the rule that all keys should be sorted. In a
// worse case, it might cause page elements to point to already freed pages.
//
// REF: https://github.com/etcd-io/bbolt/issues/72
func TestIssue72(t *testing.T) {
	db := btesting.MustCreateDBWithOption(t, &bolt.Options{PageSize: 4096})

	bucketName := []byte(t.Name())
	err := db.Update(func(tx *bolt.Tx) error {
		_, txerr := tx.CreateBucket(bucketName)
		return txerr
	})
	require.NoError(t, err)

	// The layout is like:
	//
	//         +--+--+--+
	//  +------+1 |3 |10+---+
	//  |      +-++--+--+   |
	//  |         |         |
	//  |         |         |
	// +v-+--+   +v-+--+  +-v+--+--+
	// |1 |2 |   |3 |4 |  |10|11|12|
	// +--+--+   +--+--+  +--+--+--+
	//
	err = db.Update(func(tx *bolt.Tx) error {
		bk := tx.Bucket(bucketName)

		for _, id := range []int{1, 2, 3, 4, 10, 11, 12} {
			if txerr := bk.Put(idToBytes(id), make([]byte, 1000)); txerr != nil {
				return txerr
			}
		}
		return nil
	})
	require.NoError(t, err)

	require.NoError(t, gofail.Enable("beforeBucketPut", `sleep(5000)`))

	//         +--+--+--+
	//  +------+1 |3 |1 +---+
	//  |      +-++--+--+   |
	//  |         |         |
	//  |         |         |
	// +v-+--+   +v-+--+  +-v+--+--+--+
	// |1 |2 |   |3 |4 |  |1 |10|11|12|
	// +--+--+   +--+--+  +--+--+--+--+
	//
	key := idToBytes(13)
	updatedKey := idToBytes(1)
	err = db.Update(func(tx *bolt.Tx) error {
		bk := tx.Bucket(bucketName)

		go func() {
			time.Sleep(3 * time.Second)
			copy(key, updatedKey)
		}()
		return bk.Put(key, make([]byte, 100))
	})
	require.NoError(t, err)

	require.NoError(t, gofail.Disable("beforeBucketPut"))

	// bbolt inserts 100 into last branch page. Since there are two `1`
	// keys in branch, spill operation will update first `1` pointer and
	// then last one won't be updated and continues to point to freed page.
	//
	//
	//                  +--+--+--+
	//  +---------------+1 |3 |1 +---------+
	//  |               +--++-+--+         |
	//  |                   |              |
	//  |                   |              |
	//  |        +--+--+   +v-+--+   +-----v-----+
	//  |        |1 |2 |   |3 |4 |   |freed page |
	//  |        +--+--+   +--+--+   +-----------+
	//  |
	// +v-+--+--+--+---+
	// |1 |10|11|12|100|
	// +--+--+--+--+---+
	err = db.Update(func(tx *bolt.Tx) error {
		return tx.Bucket(bucketName).Put(idToBytes(100), make([]byte, 100))
	})
	require.NoError(t, err)

	defer func() {
		if r := recover(); r != nil {
			t.Logf("panic info:\n %v", r)
		}
	}()

	// Add more keys to ensure branch node to spill.
	err = db.Update(func(tx *bolt.Tx) error {
		bk := tx.Bucket(bucketName)

		for _, id := range []int{101, 102, 103, 104, 105} {
			if txerr := bk.Put(idToBytes(id), make([]byte, 1000)); txerr != nil {
				return txerr
			}
		}
		return nil
	})
	require.NoError(t, err)
}

func TestTx_Rollback_Freelist(t *testing.T) {
	db := btesting.MustCreateDBWithOption(t, &bolt.Options{PageSize: 4096})

	bucketName := []byte("data")

	t.Log("Populate some data to have at least 5 leaf pages.")
	var keys []string
	err := db.Update(func(tx *bolt.Tx) error {
		b, terr := tx.CreateBucket(bucketName)
		if terr != nil {
			return terr
		}
		for i := 0; i <= 10; i++ {
			k := fmt.Sprintf("t1_k%02d", i)
			keys = append(keys, k)

			v := make([]byte, 1500)
			if _, terr := crand.Read(v); terr != nil {
				return terr
			}

			if terr := b.Put([]byte(k), v); terr != nil {
				return terr
			}
		}
		return nil
	})
	require.NoError(t, err)

	t.Log("Remove some keys to have at least 3 more free pages.")
	err = db.Update(func(tx *bolt.Tx) error {
		b := tx.Bucket(bucketName)
		for i := 0; i < 6; i++ {
			if terr := b.Delete([]byte(keys[i])); terr != nil {
				return terr
			}
		}
		return nil
	})
	require.NoError(t, err)

	t.Log("Close and then reopen the db to release all pending free pages.")
	db.MustClose()
	db.MustReopen()

	t.Log("Enable the `beforeWriteMetaError` failpoint.")
	require.NoError(t, gofail.Enable("beforeWriteMetaError", `return("writeMeta somehow failed")`))
	defer func() {
		t.Log("Disable the `beforeWriteMetaError` failpoint.")
		require.NoError(t, gofail.Disable("beforeWriteMetaError"))
	}()

	beforeFreelistPgids, err := readFreelistPageIds(db.Path())
	require.NoError(t, err)
	require.Greater(t, len(beforeFreelistPgids), 0)

	t.Log("Simulate TXN rollback")
	err = db.Update(func(tx *bolt.Tx) error {
		b := tx.Bucket(bucketName)
		for i := 6; i < len(keys); i++ {
			v := make([]byte, 1500)
			if _, terr := crand.Read(v); terr != nil {
				return terr
			}
			// update the keys
			if terr := b.Put([]byte(keys[i]), v); terr != nil {
				return terr
			}
		}
		return nil
	})
	require.Error(t, err)

	afterFreelistPgids, err := readFreelistPageIds(db.Path())
	require.NoError(t, err)

	require.Equal(t, beforeFreelistPgids, afterFreelistPgids)
}

func idToBytes(id int) []byte {
	return []byte(fmt.Sprintf("%010d", id))
}

func readFreelistPageIds(path string) ([]common.Pgid, error) {
	m, _, err := guts_cli.GetActiveMetaPage(path)
	if err != nil {
		return nil, err
	}

	p, _, err := guts_cli.ReadPage(path, uint64(m.Freelist()))
	if err != nil {
		return nil, err
	}

	return p.FreelistPageIds(), nil
}
```

## File: `tests/robustness/main_test.go`
```go
//go:build linux

package robustness

import (
	"flag"
	"os"
	"testing"

	testutils "go.etcd.io/bbolt/tests/utils"
)

func TestMain(m *testing.M) {
	flag.Parse()
	testutils.RequiresRoot()
	os.Exit(m.Run())
}
```

## File: `tests/robustness/powerfailure_test.go`
```go
//go:build linux

package robustness

import (
	"bytes"
	"crypto/rand"
	"fmt"
	"io"
	"math"
	"math/big"
	"net/http"
	"net/url"
	"os"
	"os/exec"
	"path"
	"path/filepath"
	"strings"
	"testing"
	"time"

	"github.com/stretchr/testify/assert"
	"github.com/stretchr/testify/require"
	"golang.org/x/sys/unix"

	"go.etcd.io/bbolt/tests/dmflakey"
)

var panicFailpoints = []string{
	"beforeSyncDataPages",
	"beforeSyncMetaPage",
	"lackOfDiskSpace",
	"mapError",
	"resizeFileError",
	"unmapError",
}

// TestRestartFromPowerFailureExt4 is to test data after unexpected power failure on ext4.
func TestRestartFromPowerFailureExt4(t *testing.T) {
	for _, tc := range []struct {
		name         string
		du           time.Duration
		fsMountOpt   string
		useFailpoint bool
	}{
		{
			name:         "fp_ext4_commit5s",
			du:           5 * time.Second,
			fsMountOpt:   "commit=5",
			useFailpoint: true,
		},
		{
			name:         "fp_ext4_commit1s",
			du:           10 * time.Second,
			fsMountOpt:   "commit=1",
			useFailpoint: true,
		},
		{
			name:         "fp_ext4_commit1000s",
			du:           10 * time.Second,
			fsMountOpt:   "commit=1000",
			useFailpoint: true,
		},
		{
			name:       "kill_ext4_commit5s",
			du:         5 * time.Second,
			fsMountOpt: "commit=5",
		},
		{
			name:       "kill_ext4_commit1s",
			du:         10 * time.Second,
			fsMountOpt: "commit=1",
		},
		{
			name:       "kill_ext4_commit1000s",
			du:         10 * time.Second,
			fsMountOpt: "commit=1000",
		},
	} {
		t.Run(tc.name, func(t *testing.T) {
			doPowerFailure(t, tc.du, dmflakey.FSTypeEXT4, "", tc.fsMountOpt, tc.useFailpoint)
		})
	}
}

func TestRestartFromPowerFailureXFS(t *testing.T) {
	for _, tc := range []struct {
		name         string
		mkfsOpt      string
		fsMountOpt   string
		useFailpoint bool
	}{
		{
			name:         "xfs_no_opts",
			mkfsOpt:      "",
			fsMountOpt:   "",
			useFailpoint: true,
		},
		{
			name:         "lazy-log",
			mkfsOpt:      "-l lazy-count=1",
			fsMountOpt:   "",
			useFailpoint: true,
		},
		{
			name:         "odd-allocsize",
			mkfsOpt:      "",
			fsMountOpt:   "allocsize=" + fmt.Sprintf("%d", 4096*5),
			useFailpoint: true,
		},
		{
			name:         "nolargeio",
			mkfsOpt:      "",
			fsMountOpt:   "nolargeio",
			useFailpoint: true,
		},
		{
			name:         "odd-alignment",
			mkfsOpt:      "-d sunit=1024,swidth=1024",
			fsMountOpt:   "noalign",
			useFailpoint: true,
		},
		{
			name:    "openshift-sno-options",
			mkfsOpt: "-m bigtime=1,finobt=1,rmapbt=0,reflink=1 -i sparse=1 -l lazy-count=1",
			// openshift also supplies seclabel,relatime,prjquota on RHEL, but that's not supported on our CI
			// prjquota is only unsupported on our ARM runners.
			// You can find more information in either the man page with `man xfs` or `man mkfs.xfs`.
			// Also refer to https://man7.org/linux/man-pages/man8/mkfs.xfs.8.html.
			fsMountOpt:   "rw,attr2,inode64,logbufs=8,logbsize=32k",
			useFailpoint: true,
		},
	} {
		t.Run(tc.name, func(t *testing.T) {
			t.Logf("mkfs opts: %s", tc.mkfsOpt)
			t.Logf("mount opts: %s", tc.fsMountOpt)
			doPowerFailure(t, 5*time.Second, dmflakey.FSTypeXFS, tc.mkfsOpt, tc.fsMountOpt, tc.useFailpoint)
		})
	}
}

func doPowerFailure(t *testing.T, du time.Duration, fsType dmflakey.FSType, mkfsOpt string, fsMountOpt string, useFailpoint bool) {
	flakey := initFlakeyDevice(t, strings.ReplaceAll(t.Name(), "/", "_"), fsType, mkfsOpt, fsMountOpt)
	root := flakey.RootFS()

	dbPath := filepath.Join(root, "boltdb")

	args := []string{"bbolt", "bench",
		"--work", // keep the database
		"--path", dbPath,
		"--count=1000000000",
		"--batch-size=5", // separate total count into multiple truncation
		"--value-size=512",
	}

	logPath := filepath.Join(t.TempDir(), fmt.Sprintf("%s.log", t.Name()))
	require.NoError(t, os.MkdirAll(path.Dir(logPath), 0600))

	logFd, err := os.Create(logPath)
	require.NoError(t, err)
	defer logFd.Close()

	fpURL := "127.0.0.1:12345"

	cmd := exec.Command(args[0], args[1:]...)
	cmd.Stdout = logFd
	cmd.Stderr = logFd
	cmd.Env = append(cmd.Env, "GOFAIL_HTTP="+fpURL)
	t.Logf("start %s", strings.Join(args, " "))
	require.NoError(t, cmd.Start(), "args: %v", args)

	errCh := make(chan error, 1)
	go func() {
		errCh <- cmd.Wait()
	}()

	defer func() {
		if t.Failed() {
			logData, err := os.ReadFile(logPath)
			assert.NoError(t, err)
			t.Logf("dump log:\n: %s", string(logData))
		}
	}()

	time.Sleep(du)
	t.Logf("simulate power failure")

	if useFailpoint {
		fpURL = "http://" + fpURL
		targetFp := panicFailpoints[randomInt(t, math.MaxInt32)%len(panicFailpoints)]
		t.Logf("random pick failpoint: %s", targetFp)
		activeFailpoint(t, fpURL, targetFp, "panic")
	} else {
		t.Log("kill bbolt")
		assert.NoError(t, cmd.Process.Kill())
	}

	select {
	case <-time.After(10 * time.Second):
		t.Log("bbolt is supposed to be already stopped, but actually not yet; forcibly kill it")
		assert.NoError(t, cmd.Process.Kill())
	case err := <-errCh:
		require.Error(t, err)
	}
	require.NoError(t, flakey.PowerFailure(""))

	st, err := os.Stat(dbPath)
	require.NoError(t, err)
	t.Logf("db size: %d", st.Size())

	t.Logf("verify data")
	output, err := exec.Command("bbolt", "check", dbPath).CombinedOutput()
	require.NoError(t, err, "bbolt check output: %s", string(output))
}

// activeFailpoint actives the failpoint by http.
func activeFailpoint(t *testing.T, targetUrl string, fpName, fpVal string) {
	u, err := url.JoinPath(targetUrl, fpName)
	require.NoError(t, err, "parse url %s", targetUrl)

	req, err := http.NewRequest("PUT", u, bytes.NewBuffer([]byte(fpVal)))
	require.NoError(t, err)

	resp, err := http.DefaultClient.Do(req)
	require.NoError(t, err)
	defer resp.Body.Close()

	data, err := io.ReadAll(resp.Body)
	require.NoError(t, err)
	require.Equal(t, 204, resp.StatusCode, "response body: %s", string(data))
}

// FlakeyDevice extends dmflakey.Flakey interface.
type FlakeyDevice interface {
	// RootFS returns root filesystem.
	RootFS() string

	// PowerFailure simulates power failure with drop all the writes.
	PowerFailure(mntOpt string) error

	dmflakey.Flakey
}

// initFlakeyDevice returns FlakeyDevice instance with a given filesystem.
func initFlakeyDevice(t *testing.T, name string, fsType dmflakey.FSType, mkfsOpt string, mntOpt string) FlakeyDevice {
	imgDir := t.TempDir()

	flakey, err := dmflakey.InitFlakey(name, imgDir, fsType, mkfsOpt)
	require.NoError(t, err, "init flakey %s", name)
	t.Cleanup(func() {
		assert.NoError(t, flakey.Teardown())
	})

	rootDir := t.TempDir()
	err = unix.Mount(flakey.DevicePath(), rootDir, string(fsType), 0, mntOpt)
	require.NoError(t, err, "init rootfs on %s", rootDir)

	t.Cleanup(func() { assert.NoError(t, unmountAll(rootDir)) })

	return &flakeyT{
		Flakey: flakey,

		rootDir: rootDir,
		mntOpt:  mntOpt,
	}
}

type flakeyT struct {
	dmflakey.Flakey

	rootDir string
	mntOpt  string
}

// RootFS returns root filesystem.
func (f *flakeyT) RootFS() string {
	return f.rootDir
}

// PowerFailure simulates power failure with drop all the writes.
func (f *flakeyT) PowerFailure(mntOpt string) error {
	if err := f.DropWrites(); err != nil {
		return fmt.Errorf("failed to drop_writes: %w", err)
	}

	if err := unmountAll(f.rootDir); err != nil {
		return fmt.Errorf("failed to unmount rootfs %s: %w", f.rootDir, err)
	}

	if mntOpt == "" {
		mntOpt = f.mntOpt
	}

	if err := f.AllowWrites(); err != nil {
		return fmt.Errorf("failed to allow_writes: %w", err)
	}

	if err := unix.Mount(f.DevicePath(), f.rootDir, string(f.Filesystem()), 0, mntOpt); err != nil {
		return fmt.Errorf("failed to mount rootfs %s (%s): %w", f.rootDir, mntOpt, err)
	}
	return nil
}

func unmountAll(target string) error {
	for i := 0; i < 50; i++ {
		if err := unix.Unmount(target, 0); err != nil {
			switch err {
			case unix.EBUSY:
				time.Sleep(500 * time.Millisecond)
				continue
			case unix.EINVAL:
				return nil
			default:
				return fmt.Errorf("failed to umount %s: %w", target, err)
			}
		}
		continue
	}
	return fmt.Errorf("failed to umount %s: %w", target, unix.EBUSY)
}

func randomInt(t *testing.T, max int) int {
	n, err := rand.Int(rand.Reader, big.NewInt(int64(max)))
	assert.NoError(t, err)
	return int(n.Int64())
}
```

## File: `tests/utils/helpers.go`
```go
package utils

import (
	"flag"
	"fmt"
	"os"
)

var enableRoot bool

func init() {
	flag.BoolVar(&enableRoot, "test.root", false, "enable tests that require root")
}

// RequiresRoot requires root and the test.root flag has been set.
func RequiresRoot() {
	if !enableRoot {
		fmt.Fprintln(os.Stderr, "Skip tests that require root")
		os.Exit(0)
	}

	if os.Getuid() != 0 {
		fmt.Fprintln(os.Stderr, "This test must be run as root.")
		os.Exit(1)
	}
}
```

## File: `version/version.go`
```go
package version

var (
	// Version shows the last bbolt binary version released.
	Version = "1.4.0-alpha.0"
)
```

