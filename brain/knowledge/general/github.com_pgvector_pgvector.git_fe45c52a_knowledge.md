---
id: github.com-pgvector-pgvector.git-fe45c52a-knowledg
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:12.308083
---

# KNOWLEDGE EXTRACT: github.com_pgvector_pgvector.git_fe45c52a
> **Extracted on:** 2026-04-01 10:38:22
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007521006/github.com_pgvector_pgvector.git_fe45c52a

---

## File: `.editorconfig`
```
root = true

[*.{c,h,pl,pm,sql}]
indent_style = tab
indent_size = tab
tab_width = 4
```

## File: `.gitignore`
```
/dist/
/log/
/results/
/tmp_check/
/sql/vector--?.?.?.sql
regression.*
*.o
*.so
*.bc
*.dll
*.dylib
*.obj
*.lib
*.exp
```

## File: `CHANGELOG.md`
```markdown
## 0.8.2 (2026-02-25)

- Fixed buffer overflow with parallel HNSW index build - [more info](https://github.com/pgvector/pgvector/issues/959)
- Improved `install` target on Windows
- Fixed `Index Searches` in `EXPLAIN` output for Postgres 18

## 0.8.1 (2025-09-04)

- Added support for Postgres 18 rc1
- Improved performance of `binary_quantize` function

## 0.8.0 (2024-10-30)

- Added support for iterative index scans
- Added casts for arrays to `sparsevec`
- Improved cost estimation for better index selection when filtering
- Improved performance of HNSW index scans
- Improved performance of HNSW inserts and on-disk index builds
- Dropped support for Postgres 12

## 0.7.4 (2024-08-05)

- Fixed locking for parallel HNSW index builds
- Fixed compilation error with GCC 14 on i386 when SSE2 is not enabled

## 0.7.3 (2024-07-22)

- Fixed `failed to add index item` error with `sparsevec`
- Fixed compilation error with FreeBSD ARM
- Fixed compilation warning with MSVC and Postgres 16

## 0.7.2 (2024-06-11)

- Fixed initialization fork for indexes on unlogged tables

## 0.7.1 (2024-06-03)

- Improved performance of on-disk HNSW index builds
- Fixed `undefined symbol` error with GCC 8
- Fixed compilation error with universal binaries on Mac
- Fixed compilation warning with Clang < 14

## 0.7.0 (2024-04-29)

- Added `halfvec` type
- Added `sparsevec` type
- Added support for indexing `bit` type
- Added support for indexing L1 distance with HNSW
- Added `binary_quantize` function
- Added `hamming_distance` function
- Added `jaccard_distance` function
- Added `l2_normalize` function
- Added `subvector` function
- Added concatenate operator for vectors
- Added CPU dispatching for distance functions on Linux x86-64
- Updated comparison operators to support vectors with different dimensions

## 0.6.2 (2024-03-18)

- Reduced lock contention with parallel HNSW index builds

## 0.6.1 (2024-03-04)

- Fixed error with `ANALYZE` and vectors with different dimensions
- Fixed segmentation fault with `shared_preload_libraries`
- Fixed vector subtraction being marked as commutative

## 0.6.0 (2024-01-29)

If upgrading with Postgres 12 or Docker, see [these notes](https://github.com/pgvector/pgvector#060).

- Added support for parallel index builds for HNSW
- Added validation for GUC parameters
- Changed storage for vector from `extended` to `external`
- Improved performance of HNSW
- Reduced memory usage for HNSW index builds
- Reduced WAL generation for HNSW index builds
- Fixed error with logical replication
- Fixed `invalid memory alloc request size` error with HNSW index builds
- Moved Docker image to `pgvector` org
- Added Docker tags for each supported version of Postgres
- Dropped support for Postgres 11

## 0.5.1 (2023-10-10)

- Improved performance of HNSW index builds
- Added check for MVCC-compliant snapshot for index scans

## 0.5.0 (2023-08-28)

- Added HNSW index type
- Added support for parallel index builds for IVFFlat
- Added `l1_distance` function
- Added element-wise multiplication for vectors
- Added `sum` aggregate
- Improved performance of distance functions
- Fixed out of range results for cosine distance
- Fixed results for NULL and NaN distances for IVFFlat

## 0.4.4 (2023-06-12)

- Improved error message for malformed vector literal
- Fixed segmentation fault with text input
- Fixed consecutive delimiters with text input

## 0.4.3 (2023-06-10)

- Improved cost estimation
- Improved support for spaces with text input
- Fixed infinite and NaN values with binary input
- Fixed infinite values with vector addition and subtraction
- Fixed infinite values with list centers
- Fixed compilation error when `float8` is pass by reference
- Fixed compilation error on PowerPC
- Fixed segmentation fault with index creation on i386

## 0.4.2 (2023-05-13)

- Added notice when index created with little data
- Fixed dimensions check for some direct function calls
- Fixed installation error with Postgres 12.0-12.2

## 0.4.1 (2023-03-21)

- Improved performance of cosine distance
- Fixed index scan count

## 0.4.0 (2023-01-11)

If upgrading with Postgres < 13, see [this note](https://github.com/pgvector/pgvector/blob/v0.4.0/README.md#040).

- Changed text representation for vector elements to match `real`
- Changed storage for vector from `plain` to `extended`
- Increased max dimensions for vector from 1024 to 16000
- Increased max dimensions for index from 1024 to 2000
- Improved accuracy of text parsing for certain inputs
- Added `avg` aggregate for vector
- Added experimental support for Windows
- Dropped support for Postgres 10

## 0.3.2 (2022-11-22)

- Fixed `invalid memory alloc request size` error

## 0.3.1 (2022-11-02)

If upgrading from 0.2.7 or 0.3.0, [recreate](https://github.com/pgvector/pgvector/blob/v0.3.1/README.md#031) all `ivfflat` indexes after upgrading to ensure all data is indexed.

- Fixed issue with inserts silently corrupting `ivfflat` indexes (introduced in 0.2.7)
- Fixed segmentation fault with index creation when lists > 6500

## 0.3.0 (2022-10-15)

- Added support for Postgres 15
- Dropped support for Postgres 9.6

## 0.2.7 (2022-07-31)

- Fixed `unexpected data beyond EOF` error

## 0.2.6 (2022-05-22)

- Improved performance of index creation for Postgres < 12

## 0.2.5 (2022-02-11)

- Reduced memory usage during index creation
- Fixed index creation exceeding `maintenance_work_mem`
- Fixed error with index creation when lists > 1600

## 0.2.4 (2022-02-06)

- Added support for parallel vacuum
- Fixed issue with index not reusing space

## 0.2.3 (2022-01-30)

- Added indexing progress for Postgres 12+
- Improved interrupt handling during index creation

## 0.2.2 (2022-01-15)

- Fixed compilation error on Mac ARM

## 0.2.1 (2022-01-02)

- Fixed `operator is not unique` error

## 0.2.0 (2021-10-03)

- Added support for Postgres 14

## 0.1.8 (2021-09-07)

- Added cast for `vector` to `real[]`

## 0.1.7 (2021-06-13)

- Added cast for `numeric[]` to `vector`

## 0.1.6 (2021-06-09)

- Fixed segmentation fault with `COUNT`

## 0.1.5 (2021-05-25)

- Reduced memory usage during index creation

## 0.1.4 (2021-05-09)

- Fixed kmeans for inner product
- Fixed multiple definition error with GCC 10

## 0.1.3 (2021-05-06)

- Added Dockerfile
- Fixed version

## 0.1.2 (2021-04-26)

- Vectorized distance calculations
- Improved cost estimation

## 0.1.1 (2021-04-25)

- Added binary representation for `COPY`
- Marked functions as `PARALLEL SAFE`

## 0.1.0 (2021-04-20)

- First release
```

## File: `Dockerfile`
```
# syntax=docker/dockerfile:1

ARG PG_MAJOR=17
ARG DEBIAN_CODENAME=bookworm
FROM postgres:$PG_MAJOR-$DEBIAN_CODENAME
ARG PG_MAJOR

ADD https://github.com/pgvector/pgvector.git#v0.8.2 /tmp/pgvector

RUN apt-get update && \
		apt-mark hold locales && \
		apt-get install -y --no-install-recommends build-essential postgresql-server-dev-$PG_MAJOR && \
		cd /tmp/pgvector && \
		make clean && \
		make OPTFLAGS="" && \
		make install && \
		mkdir /usr/share/doc/pgvector && \
		cp LICENSE README.md /usr/share/doc/pgvector && \
		rm -r /tmp/pgvector && \
		apt-get remove -y build-essential postgresql-server-dev-$PG_MAJOR && \
		apt-get autoremove -y && \
		apt-mark unhold locales && \
		rm -rf /var/lib/apt/lists/*
```

## File: `LICENSE`
```
Portions Copyright (c) 1996-2026, PostgreSQL Global Development Group

Portions Copyright (c) 1994, The Regents of the University of California

Permission to use, copy, modify, and distribute this software and its
documentation for any purpose, without fee, and without a written agreement
is hereby granted, provided that the above copyright notice and this
paragraph and the following two paragraphs appear in all copies.

IN NO EVENT SHALL THE UNIVERSITY OF CALIFORNIA BE LIABLE TO ANY PARTY FOR
DIRECT, INDIRECT, SPECIAL, INCIDENTAL, OR CONSEQUENTIAL DAMAGES, INCLUDING
LOST PROFITS, ARISING OUT OF THE USE OF THIS SOFTWARE AND ITS
DOCUMENTATION, EVEN IF THE UNIVERSITY OF CALIFORNIA HAS BEEN ADVISED OF THE
POSSIBILITY OF SUCH DAMAGE.

THE UNIVERSITY OF CALIFORNIA SPECIFICALLY DISCLAIMS ANY WARRANTIES,
INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY
AND FITNESS FOR A PARTICULAR PURPOSE.  THE SOFTWARE PROVIDED HEREUNDER IS
ON AN "AS IS" BASIS, AND THE UNIVERSITY OF CALIFORNIA HAS NO OBLIGATIONS TO
PROVIDE MAINTENANCE, SUPPORT, UPDATES, ENHANCEMENTS, OR MODIFICATIONS.
```

## File: `META.json`
```json
{
	"name": "vector",
	"abstract": "Open-source vector similarity search for Postgres",
	"description": "Supports L2 distance, inner product, and cosine distance",
	"version": "0.8.2",
	"maintainer": [
		"Andrew Kane <andrew@ankane.org>"
	],
	"license": {
		"PostgreSQL": "http://www.postgresql.org/about/licence"
	},
	"prereqs": {
		"runtime": {
			"requires": {
				"PostgreSQL": "13.0.0"
			}
		}
	},
	"provides": {
		"vector": {
			"file": "sql/vector.sql",
			"docfile": "README.md",
			"version": "0.8.2",
			"abstract": "Open-source vector similarity search for Postgres"
		}
	},
	"resources": {
		"homepage": "https://github.com/pgvector/pgvector",
		"bugtracker": {
			"web": "https://github.com/pgvector/pgvector/issues"
		},
		"repository": {
			"url":  "https://github.com/pgvector/pgvector.git",
			"web":  "https://github.com/pgvector/pgvector",
			"type": "git"
		}
	},
	"generated_by": "Andrew Kane",
	"meta-spec": {
		"version": "1.0.0",
		"url": "http://pgxn.org/meta/spec.txt"
	},
	"tags": [
		"vectors",
		"datatype",
		"nearest neighbor search",
		"approximate nearest neighbors"
	]
}
```

## File: `Makefile`
```
EXTENSION = vector
EXTVERSION = 0.8.2

MODULE_big = vector
DATA = $(wildcard sql/*--*--*.sql)
DATA_built = sql/$(EXTENSION)--$(EXTVERSION).sql
OBJS = src/bitutils.o src/bitvec.o src/halfutils.o src/halfvec.o src/hnsw.o src/hnswbuild.o src/hnswinsert.o src/hnswscan.o src/hnswutils.o src/hnswvacuum.o src/ivfbuild.o src/ivfflat.o src/ivfinsert.o src/ivfkmeans.o src/ivfscan.o src/ivfutils.o src/ivfvacuum.o src/sparsevec.o src/vector.o
HEADERS = src/halfvec.h src/sparsevec.h src/vector.h

TESTS = $(wildcard test/sql/*.sql)
REGRESS = $(patsubst test/sql/%.sql,%,$(TESTS))
REGRESS_OPTS = --inputdir=test --load-extension=$(EXTENSION)

# To compile for portability, run: make OPTFLAGS=""
OPTFLAGS = -march=native

# Mac ARM doesn't always support -march=native
ifeq ($(shell uname -s), Darwin)
	ifeq ($(shell uname -p), arm)
		# no difference with -march=armv8.5-a
		OPTFLAGS =
	endif
endif

# PowerPC doesn't support -march=native
ifneq ($(filter ppc64%, $(shell uname -m)), )
	OPTFLAGS =
endif

# RISC-V64 doesn't support -march=native
ifeq ($(shell uname -m), riscv64)
	OPTFLAGS =
endif

# For auto-vectorization:
# - GCC (needs -ftree-vectorize OR -O3) - https://gcc.gnu.org/projects/tree-ssa/vectorization.html
# - Clang (could use pragma instead) - https://llvm.org/docs/Vectorizers.html
PG_CFLAGS += $(OPTFLAGS) -ftree-vectorize -fassociative-math -fno-signed-zeros -fno-trapping-math

# Debug GCC auto-vectorization
# PG_CFLAGS += -fopt-info-vec

# Debug Clang auto-vectorization
# PG_CFLAGS += -Rpass=loop-vectorize -Rpass-analysis=loop-vectorize

all: sql/$(EXTENSION)--$(EXTVERSION).sql

sql/$(EXTENSION)--$(EXTVERSION).sql: sql/$(EXTENSION).sql
	cp $< $@

PG_CONFIG ?= pg_config
PGXS := $(shell $(PG_CONFIG) --pgxs)
include $(PGXS)

# for Mac
ifeq ($(PROVE),)
	PROVE = prove
endif

# for Postgres < 15
PROVE_FLAGS += -I ./test/perl

prove_installcheck:
	rm -rf $(CURDIR)/tmp_check
	cd $(srcdir) && TESTDIR='$(CURDIR)' PATH="$(bindir):$$PATH" PGPORT='6$(DEF_PGPORT)' PG_REGRESS='$(top_builddir)/src/test/regress/pg_regress' $(PROVE) $(PG_PROVE_FLAGS) $(PROVE_FLAGS) $(if $(PROVE_TESTS),$(PROVE_TESTS),test/t/*.pl)

.PHONY: dist

dist:
	mkdir -p dist
	git archive --format zip --prefix=$(EXTENSION)-$(EXTVERSION)/ --output dist/$(EXTENSION)-$(EXTVERSION).zip master

# for Docker
PG_MAJOR ?= 17

.PHONY: docker

docker:
	docker build --pull --no-cache --build-arg PG_MAJOR=$(PG_MAJOR) -t pgvector/pgvector:pg$(PG_MAJOR) -t pgvector/pgvector:$(EXTVERSION)-pg$(PG_MAJOR) .

.PHONY: docker-release

docker-release:
	docker buildx build --push --pull --no-cache --platform linux/amd64,linux/arm64 --build-arg PG_MAJOR=$(PG_MAJOR) --build-arg DEBIAN_CODENAME=bookworm -t pgvector/pgvector:pg$(PG_MAJOR) -t pgvector/pgvector:pg$(PG_MAJOR)-bookworm -t pgvector/pgvector:$(EXTVERSION)-pg$(PG_MAJOR) -t pgvector/pgvector:$(EXTVERSION)-pg$(PG_MAJOR)-bookworm .

.PHONY: docker-release-trixie

docker-release-trixie:
	docker buildx build --push --pull --no-cache --platform linux/amd64,linux/arm64 --build-arg PG_MAJOR=$(PG_MAJOR) --build-arg DEBIAN_CODENAME=trixie -t pgvector/pgvector:pg$(PG_MAJOR)-trixie -t pgvector/pgvector:$(EXTVERSION)-pg$(PG_MAJOR)-trixie .
```

## File: `Makefile.win`
```
EXTENSION = vector
EXTVERSION = 0.8.2

DATA_built = sql\$(EXTENSION)--$(EXTVERSION).sql
OBJS = src\bitutils.obj src\bitvec.obj src\halfutils.obj src\halfvec.obj src\hnsw.obj src\hnswbuild.obj src\hnswinsert.obj src\hnswscan.obj src\hnswutils.obj src\hnswvacuum.obj src\ivfbuild.obj src\ivfflat.obj src\ivfinsert.obj src\ivfkmeans.obj src\ivfscan.obj src\ivfutils.obj src\ivfvacuum.obj src\sparsevec.obj src\vector.obj
HEADERS = src\halfvec.h src\sparsevec.h src\vector.h

REGRESS = bit btree cast copy halfvec hnsw_bit hnsw_halfvec hnsw_sparsevec hnsw_vector ivfflat_bit ivfflat_halfvec ivfflat_vector sparsevec vector_type
REGRESS_OPTS = --inputdir=test --load-extension=$(EXTENSION)

# For /arch flags
# https://learn.microsoft.com/en-us/cpp/build/reference/arch-minimum-cpu-architecture
OPTFLAGS =

# For auto-vectorization:
# - MSVC (needs /O2 /fp:fast) - https://learn.microsoft.com/en-us/cpp/parallel/auto-parallelization-and-auto-vectorization?#auto-vectorizer
PG_CFLAGS = $(PG_CFLAGS) $(OPTFLAGS) /O2 /fp:fast

# Debug MSVC auto-vectorization
# https://learn.microsoft.com/en-us/cpp/error-messages/tool-errors/vectorizer-and-parallelizer-messages
# PG_CFLAGS = $(PG_CFLAGS) /Qvec-report:2

# TODO use pg_config
!ifndef PGROOT
!error PGROOT is not set
!endif
BINDIR = $(PGROOT)\bin
INCLUDEDIR = $(PGROOT)\include
INCLUDEDIR_SERVER = $(PGROOT)\include\server
LIBDIR = $(PGROOT)\lib
PKGLIBDIR = $(PGROOT)\lib
SHAREDIR = $(PGROOT)\share

# Use $(PGROOT)\bin\pg_regress for Postgres < 17
PG_REGRESS = $(LIBDIR)\pgxs\src\test\regress\pg_regress

CFLAGS = /nologo /I"$(INCLUDEDIR_SERVER)\port\win32_msvc" /I"$(INCLUDEDIR_SERVER)\port\win32" /I"$(INCLUDEDIR_SERVER)" /I"$(INCLUDEDIR)"

CFLAGS = $(CFLAGS) $(PG_CFLAGS)

SHLIB = $(EXTENSION).dll

LIBS = "$(LIBDIR)\postgres.lib"

all: $(SHLIB) $(DATA_built)

.c.obj:
	$(CC) $(CFLAGS) /c $< /Fo$@

$(SHLIB): $(OBJS)
	$(CC) $(CFLAGS) $(OBJS) $(LIBS) /link /DLL /OUT:$(SHLIB)

sql\$(EXTENSION)--$(EXTVERSION).sql: sql\$(EXTENSION).sql
	copy sql\$(EXTENSION).sql $@

install: all
	copy $(SHLIB) "$(PKGLIBDIR)"
	copy $(EXTENSION).control "$(SHAREDIR)\extension"
	copy sql\$(EXTENSION)--*.sql "$(SHAREDIR)\extension"
	if not exist "$(INCLUDEDIR_SERVER)\extension\$(EXTENSION)" mkdir "$(INCLUDEDIR_SERVER)\extension\$(EXTENSION)"
	for %f in ($(HEADERS)) do copy %f "$(INCLUDEDIR_SERVER)\extension\$(EXTENSION)"

installcheck:
	"$(PG_REGRESS)" --bindir="$(BINDIR)" $(REGRESS_OPTS) $(REGRESS)

uninstall:
	del /f "$(PKGLIBDIR)\$(SHLIB)"
	del /f "$(SHAREDIR)\extension\$(EXTENSION).control"
	del /f "$(SHAREDIR)\extension\$(EXTENSION)--*.sql"
	del /f "$(INCLUDEDIR_SERVER)\extension\$(EXTENSION)\*.h"
	rmdir "$(INCLUDEDIR_SERVER)\extension\$(EXTENSION)"

clean:
	del /f $(SHLIB) $(EXTENSION).lib $(EXTENSION).exp
	del /f $(DATA_built)
	del /f $(OBJS)
	del /f /s /q results regression.diffs regression.out tmp_check tmp_check_iso log output_iso
```

## File: `README.md`
```markdown
# pgvector

Open-source vector similarity search for Postgres

Store your vectors with the rest of your data. Supports:

- exact and approximate nearest neighbor search
- single-precision, half-precision, binary, and sparse vectors
- L2 distance, inner product, cosine distance, L1 distance, Hamming distance, and Jaccard distance
- any [language](#languages) with a Postgres client

Plus [ACID](https://en.wikipedia.org/wiki/ACID) compliance, point-in-time recovery, JOINs, and all of the other [great features](https://www.postgresql.org/about/) of Postgres

[![Build Status](https://github.com/pgvector/pgvector/actions/workflows/build.yml/badge.svg)](https://github.com/pgvector/pgvector/actions)

## Installation

### Linux and Mac

Compile and install the extension (supports Postgres 13+)

```sh
cd /tmp
git clone --branch v0.8.2 https://github.com/pgvector/pgvector.git
cd pgvector
make
make install # may need sudo
```

See the [installation notes](#installation-notes---linux-and-mac) if you run into issues

You can also install it with [Docker](#docker), [Homebrew](#homebrew), [PGXN](#pgxn), [APT](#apt), [Yum](#yum), [pkg](#pkg), [APK](#apk), or [conda-forge](#conda-forge), and it comes preinstalled with [Postgres.app](#postgresapp) and many [hosted providers](#hosted-postgres). There are also instructions for [GitHub Actions](https://github.com/pgvector/setup-pgvector).

### Windows

Ensure [C++ support in Visual Studio](https://learn.microsoft.com/en-us/cpp/build/building-on-the-command-line?view=msvc-170#download-and-install-the-tools) is installed and run `x64 Native Tools Command Prompt for VS [version]` as administrator. Then use `nmake` to build:

```cmd
set "PGROOT=C:\Program Files\PostgreSQL\18"
cd %TEMP%
git clone --branch v0.8.2 https://github.com/pgvector/pgvector.git
cd pgvector
nmake /F Makefile.win
nmake /F Makefile.win install
```

See the [installation notes](#installation-notes---windows) if you run into issues

You can also install it with [Docker](#docker) or [conda-forge](#conda-forge).

## Getting Started

Enable the extension (do this once in each database where you want to use it)

```tsql
CREATE EXTENSION vector;
```

Create a vector column with 3 dimensions

```sql
CREATE TABLE items (id bigserial PRIMARY KEY, embedding vector(3));
```

Insert vectors

```sql
INSERT INTO items (embedding) VALUES ('[1,2,3]'), ('[4,5,6]');
```

Get the nearest neighbors by L2 distance

```sql
SELECT * FROM items ORDER BY embedding <-> '[3,1,2]' LIMIT 5;
```

Also supports inner product (`<#>`), cosine distance (`<=>`), and L1 distance (`<+>`)

Note: `<#>` returns the negative inner product since Postgres only supports `ASC` order index scans on operators

## Storing

Create a new table with a vector column

```sql
CREATE TABLE items (id bigserial PRIMARY KEY, embedding vector(3));
```

Or add a vector column to an existing table

```sql
ALTER TABLE items ADD COLUMN embedding vector(3);
```

Also supports [half-precision](#half-precision-vectors), [binary](#binary-vectors), and [sparse](#sparse-vectors) vectors

Insert vectors

```sql
INSERT INTO items (embedding) VALUES ('[1,2,3]'), ('[4,5,6]');
```

Or load vectors in bulk using `COPY` ([example](https://github.com/pgvector/pgvector-python/blob/master/examples/loading/example.py))

```sql
COPY items (embedding) FROM STDIN WITH (FORMAT BINARY);
```

Upsert vectors

```sql
INSERT INTO items (id, embedding) VALUES (1, '[1,2,3]'), (2, '[4,5,6]')
    ON CONFLICT (id) DO UPDATE SET embedding = EXCLUDED.embedding;
```

Update vectors

```sql
UPDATE items SET embedding = '[1,2,3]' WHERE id = 1;
```

Delete vectors

```sql
DELETE FROM items WHERE id = 1;
```

## Querying

Get the nearest neighbors to a vector

```sql
SELECT * FROM items ORDER BY embedding <-> '[3,1,2]' LIMIT 5;
```

Supported distance functions are:

- `<->` - L2 distance
- `<#>` - (negative) inner product
- `<=>` - cosine distance
- `<+>` - L1 distance
- `<~>` - Hamming distance (binary vectors)
- `<%>` - Jaccard distance (binary vectors)

Get the nearest neighbors to a row

```sql
SELECT * FROM items WHERE id != 1 ORDER BY embedding <-> (SELECT embedding FROM items WHERE id = 1) LIMIT 5;
```

Get rows within a certain distance

```sql
SELECT * FROM items WHERE embedding <-> '[3,1,2]' < 5;
```

Note: Combine with `ORDER BY` and `LIMIT` to use an index

#### Distances

Get the distance

```sql
SELECT embedding <-> '[3,1,2]' AS distance FROM items;
```

For inner product, multiply by -1 (since `<#>` returns the negative inner product)

```tsql
SELECT (embedding <#> '[3,1,2]') * -1 AS inner_product FROM items;
```

For cosine similarity, use 1 - cosine distance

```sql
SELECT 1 - (embedding <=> '[3,1,2]') AS cosine_similarity FROM items;
```

#### Aggregates

Average vectors

```sql
SELECT AVG(embedding) FROM items;
```

Average groups of vectors

```sql
SELECT category_id, AVG(embedding) FROM items GROUP BY category_id;
```

## Indexing

By default, pgvector performs exact nearest neighbor search, which provides perfect recall.

You can add an index to use approximate nearest neighbor search, which trades some recall for speed. Unlike typical indexes, you will see different results for queries after adding an approximate index.

Supported index types are:

- [HNSW](#hnsw)
- [IVFFlat](#ivfflat)

## HNSW

An HNSW index creates a multilayer graph. It has better query performance than IVFFlat (in terms of speed-recall tradeoff), but has slower build times and uses more memory. Also, an index can be created without any data in the table since there isn’t a training step like IVFFlat.

Add an index for each distance function you want to use.

L2 distance

```sql
CREATE INDEX ON items USING hnsw (embedding vector_l2_ops);
```

Note: Use `halfvec_l2_ops` for `halfvec` and `sparsevec_l2_ops` for `sparsevec` (and similar with the other distance functions)

Inner product

```sql
CREATE INDEX ON items USING hnsw (embedding vector_ip_ops);
```

Cosine distance

```sql
CREATE INDEX ON items USING hnsw (embedding vector_cosine_ops);
```

L1 distance

```sql
CREATE INDEX ON items USING hnsw (embedding vector_l1_ops);
```

Hamming distance

```sql
CREATE INDEX ON items USING hnsw (embedding bit_hamming_ops);
```

Jaccard distance

```sql
CREATE INDEX ON items USING hnsw (embedding bit_jaccard_ops);
```

Supported types are:

- `vector` - up to 2,000 dimensions
- `halfvec` - up to 4,000 dimensions
- `bit` - up to 64,000 dimensions
- `sparsevec` - up to 1,000 non-zero elements

### Index Options

Specify HNSW parameters

- `m` - the max number of connections per layer (16 by default)
- `ef_construction` - the size of the dynamic candidate list for constructing the graph (64 by default)

```sql
CREATE INDEX ON items USING hnsw (embedding vector_l2_ops) WITH (m = 16, ef_construction = 64);
```

A higher value of `ef_construction` provides better recall at the cost of index build time / insert speed.

### Query Options

Specify the size of the dynamic candidate list for search (40 by default)

```sql
SET hnsw.ef_search = 100;
```

A higher value provides better recall at the cost of speed.

Use `SET LOCAL` inside a transaction to set it for a single query

```sql
BEGIN;
SET LOCAL hnsw.ef_search = 100;
SELECT ...
COMMIT;
```

### Index Build Time

Indexes build significantly faster when the graph fits into `maintenance_work_mem`

```sql
SET maintenance_work_mem = '8GB';
```

A notice is shown when the graph no longer fits

```text
NOTICE:  hnsw graph no longer fits into maintenance_work_mem after 100000 tuples
DETAIL:  Building will take significantly more time.
HINT:  Increase maintenance_work_mem to speed up builds.
```

Note: Do not set `maintenance_work_mem` so high that it exhausts the memory on the server

Like other index types, it’s faster to create an index after loading your initial data

You can also speed up index creation by increasing the number of parallel workers (2 by default)

```sql
SET max_parallel_maintenance_workers = 7; -- plus leader
```

For a large number of workers, you may need to increase `max_parallel_workers` (8 by default)

The [index options](#index-options) also have a significant impact on build time (use the defaults unless seeing low recall)

### Indexing Progress

Check [indexing progress](https://www.postgresql.org/docs/current/progress-reporting.html#CREATE-INDEX-PROGRESS-REPORTING)

```sql
SELECT phase, round(100.0 * blocks_done / nullif(blocks_total, 0), 1) AS "%" FROM pg_stat_progress_create_index;
```

The phases for HNSW are:

1. `initializing`
2. `loading tuples`

## IVFFlat

An IVFFlat index divides vectors into lists, and then searches a subset of those lists that are closest to the query vector. It has faster build times and uses less memory than HNSW, but has lower query performance (in terms of speed-recall tradeoff).

Three keys to achieving good recall are:

1. Create the index *after* the table has some data
2. Choose an appropriate number of lists - a good place to start is `rows / 1000` for up to 1M rows and `sqrt(rows)` for over 1M rows
3. When querying, specify an appropriate number of [probes](#query-options) (higher is better for recall, lower is better for speed) - a good place to start is `sqrt(lists)`

Add an index for each distance function you want to use.

L2 distance

```sql
CREATE INDEX ON items USING ivfflat (embedding vector_l2_ops) WITH (lists = 100);
```

Note: Use `halfvec_l2_ops` for `halfvec` (and similar with the other distance functions)

Inner product

```sql
CREATE INDEX ON items USING ivfflat (embedding vector_ip_ops) WITH (lists = 100);
```

Cosine distance

```sql
CREATE INDEX ON items USING ivfflat (embedding vector_cosine_ops) WITH (lists = 100);
```

Hamming distance

```sql
CREATE INDEX ON items USING ivfflat (embedding bit_hamming_ops) WITH (lists = 100);
```

Supported types are:

- `vector` - up to 2,000 dimensions
- `halfvec` - up to 4,000 dimensions
- `bit` - up to 64,000 dimensions

### Query Options

Specify the number of probes (1 by default)

```sql
SET ivfflat.probes = 10;
```

A higher value provides better recall at the cost of speed, and it can be set to the number of lists for exact nearest neighbor search (at which point the planner won’t use the index)

Use `SET LOCAL` inside a transaction to set it for a single query

```sql
BEGIN;
SET LOCAL ivfflat.probes = 10;
SELECT ...
COMMIT;
```

### Index Build Time

Speed up index creation on large tables by increasing the number of parallel workers (2 by default)

```sql
SET max_parallel_maintenance_workers = 7; -- plus leader
```

For a large number of workers, you may also need to increase `max_parallel_workers` (8 by default)

### Indexing Progress

Check [indexing progress](https://www.postgresql.org/docs/current/progress-reporting.html#CREATE-INDEX-PROGRESS-REPORTING)

```sql
SELECT phase, round(100.0 * tuples_done / nullif(tuples_total, 0), 1) AS "%" FROM pg_stat_progress_create_index;
```

The phases for IVFFlat are:

1. `initializing`
2. `performing k-means`
3. `assigning tuples`
4. `loading tuples`

Note: `%` is only populated during the `loading tuples` phase

## Filtering

There are a few ways to index nearest neighbor queries with a `WHERE` clause.

```sql
SELECT * FROM items WHERE category_id = 123 ORDER BY embedding <-> '[3,1,2]' LIMIT 5;
```

A good place to start is creating an index on the filter column. This can provide fast, exact nearest neighbor search in many cases. Postgres has a number of [index types](https://www.postgresql.org/docs/current/indexes-types.html) for this: B-tree (default), hash, GiST, SP-GiST, GIN, and BRIN.

```sql
CREATE INDEX ON items (category_id);
```

For multiple columns, consider a [multicolumn index](https://www.postgresql.org/docs/current/indexes-multicolumn.html).

```sql
CREATE INDEX ON items (location_id, category_id);
```

Exact indexes work well for conditions that match a low percentage of rows. Otherwise, [approximate indexes](#indexing) can work better.

```sql
CREATE INDEX ON items USING hnsw (embedding vector_l2_ops);
```

With approximate indexes, filtering is applied *after* the index is scanned. If a condition matches 10% of rows, with HNSW and the default `hnsw.ef_search` of 40, only 4 rows will match on average. For more rows, increase `hnsw.ef_search`.

```sql
SET hnsw.ef_search = 200;
```

Starting with 0.8.0, you can enable [iterative index scans](#iterative-index-scans), which will automatically scan more of the index when needed.

```sql
SET hnsw.iterative_scan = strict_order;
```

If filtering by only a few distinct values, consider [partial indexing](https://www.postgresql.org/docs/current/indexes-partial.html).

```sql
CREATE INDEX ON items USING hnsw (embedding vector_l2_ops) WHERE (category_id = 123);
```

If filtering by many different values, consider [partitioning](https://www.postgresql.org/docs/current/ddl-partitioning.html).

```sql
CREATE TABLE items (embedding vector(3), category_id int) PARTITION BY LIST(category_id);
```

## Iterative Index Scans

With approximate indexes, queries with filtering can return less results since filtering is applied *after* the index is scanned. Starting with 0.8.0, you can enable iterative index scans, which will automatically scan more of the index until enough results are found (or it reaches `hnsw.max_scan_tuples` or `ivfflat.max_probes`).

Iterative scans can use strict or relaxed ordering.

Strict ensures results are in the exact order by distance

```sql
SET hnsw.iterative_scan = strict_order;
```

Relaxed allows results to be slightly out of order by distance, but provides better recall

```sql
SET hnsw.iterative_scan = relaxed_order;
# or
SET ivfflat.iterative_scan = relaxed_order;
```

With relaxed ordering, you can use a [materialized CTE](https://www.postgresql.org/docs/current/queries-with.html#QUERIES-WITH-CTE-MATERIALIZATION) to get strict ordering

```sql
WITH relaxed_results AS MATERIALIZED (
    SELECT id, embedding <-> '[1,2,3]' AS distance FROM items WHERE category_id = 123 ORDER BY distance LIMIT 5
) SELECT * FROM relaxed_results ORDER BY distance + 0;
```

Note: `+ 0` is needed for Postgres 17+

For queries that filter by distance, use a materialized CTE and place the distance filter outside of it for best performance (due to the [current behavior](https://www.postgresql.org/message-id/flat/CAOdR5yGUoMQ6j7M5hNUXrySzaqZVGf_Ne%2B8fwZMRKTFxU1nbJg%40mail.gmail.com) of the Postgres executor)

```sql
WITH nearest_results AS MATERIALIZED (
    SELECT id, embedding <-> '[1,2,3]' AS distance FROM items ORDER BY distance LIMIT 5
) SELECT * FROM nearest_results WHERE distance < 5 ORDER BY distance;
```

Note: Place any other filters inside the CTE

### Iterative Scan Options

Since scanning a large portion of an approximate index is expensive, there are options to control when a scan ends.

#### HNSW

Specify the max number of tuples to visit (20,000 by default)

```sql
SET hnsw.max_scan_tuples = 20000;
```

Note: This is approximate and does not affect the initial scan

Specify the max amount of memory to use, as a multiple of `work_mem` (1 by default)

```sql
SET hnsw.scan_mem_multiplier = 2;
```

Note: Try increasing this if increasing `hnsw.max_scan_tuples` does not improve recall

#### IVFFlat

Specify the max number of probes

```sql
SET ivfflat.max_probes = 100;
```

Note: If this is lower than `ivfflat.probes`, `ivfflat.probes` will be used

## Half-Precision Vectors

Use the `halfvec` type to store half-precision vectors

```sql
CREATE TABLE items (id bigserial PRIMARY KEY, embedding halfvec(3));
```

## Half-Precision Indexing

Index vectors at half precision for smaller indexes

```sql
CREATE INDEX ON items USING hnsw ((embedding::halfvec(3)) halfvec_l2_ops);
```

Get the nearest neighbors

```sql
SELECT * FROM items ORDER BY embedding::halfvec(3) <-> '[1,2,3]' LIMIT 5;
```

## Binary Vectors

Use the `bit` type to store binary vectors ([example](https://github.com/pgvector/pgvector-python/blob/master/examples/imagehash/example.py))

```sql
CREATE TABLE items (id bigserial PRIMARY KEY, embedding bit(3));
INSERT INTO items (embedding) VALUES ('000'), ('111');
```

Get the nearest neighbors by Hamming distance

```sql
SELECT * FROM items ORDER BY embedding <~> '101' LIMIT 5;
```

Also supports Jaccard distance (`<%>`)

## Binary Quantization

Use expression indexing for binary quantization

```sql
CREATE INDEX ON items USING hnsw ((binary_quantize(embedding)::bit(3)) bit_hamming_ops);
```

Get the nearest neighbors by Hamming distance

```sql
SELECT * FROM items ORDER BY binary_quantize(embedding)::bit(3) <~> binary_quantize('[1,-2,3]') LIMIT 5;
```

Re-rank by the original vectors for better recall

```sql
SELECT * FROM (
    SELECT * FROM items ORDER BY binary_quantize(embedding)::bit(3) <~> binary_quantize('[1,-2,3]') LIMIT 20
) ORDER BY embedding <=> '[1,-2,3]' LIMIT 5;
```

## Sparse Vectors

Use the `sparsevec` type to store sparse vectors

```sql
CREATE TABLE items (id bigserial PRIMARY KEY, embedding sparsevec(5));
```

Insert vectors

```sql
INSERT INTO items (embedding) VALUES ('{1:1,3:2,5:3}/5'), ('{1:4,3:5,5:6}/5');
```

The format is `{index1:value1,index2:value2}/dimensions` and indices start at 1 like SQL arrays

Get the nearest neighbors by L2 distance

```sql
SELECT * FROM items ORDER BY embedding <-> '{1:3,3:1,5:2}/5' LIMIT 5;
```

## Hybrid Search

Use together with Postgres [full-text search](https://www.postgresql.org/docs/current/textsearch-intro.html) for hybrid search.

```sql
SELECT id, content FROM items, plainto_tsquery('hello search') query
    WHERE textsearch @@ query ORDER BY ts_rank_cd(textsearch, query) DESC LIMIT 5;
```

You can use [Reciprocal Rank Fusion](https://github.com/pgvector/pgvector-python/blob/master/examples/hybrid_search/rrf.py) or a [cross-encoder](https://github.com/pgvector/pgvector-python/blob/master/examples/hybrid_search/cross_encoder.py) to combine results.

## Indexing Subvectors

Use expression indexing to index subvectors

```sql
CREATE INDEX ON items USING hnsw ((subvector(embedding, 1, 3)::vector(3)) vector_cosine_ops);
```

Get the nearest neighbors by cosine distance

```sql
SELECT * FROM items ORDER BY subvector(embedding, 1, 3)::vector(3) <=> subvector('[1,2,3,4,5]'::vector, 1, 3) LIMIT 5;
```

Re-rank by the full vectors for better recall

```sql
SELECT * FROM (
    SELECT * FROM items ORDER BY subvector(embedding, 1, 3)::vector(3) <=> subvector('[1,2,3,4,5]'::vector, 1, 3) LIMIT 20
) ORDER BY embedding <=> '[1,2,3,4,5]' LIMIT 5;
```

## Performance

### Tuning

Use a tool like [PgTune](https://pgtune.leopard.in.ua/) to set initial values for Postgres server parameters. For instance, `shared_buffers` should typically be 25% of the server’s memory. You can find the config file with:

```sql
SHOW config_file;
```

And check individual settings with:

```sql
SHOW shared_buffers;
```

Be sure to restart Postgres for changes to take effect.

### Loading

Use `COPY` for bulk loading data ([example](https://github.com/pgvector/pgvector-python/blob/master/examples/loading/example.py)).

```sql
COPY items (embedding) FROM STDIN WITH (FORMAT BINARY);
```

Add any indexes *after* loading the initial data for best performance.

### Indexing

See index build time for [HNSW](#index-build-time) and [IVFFlat](#index-build-time-1).

In production environments, create indexes concurrently to avoid blocking writes.

```sql
CREATE INDEX CONCURRENTLY ...
```

### Querying

Use `EXPLAIN (ANALYZE, BUFFERS)` to debug performance.

```sql
EXPLAIN (ANALYZE, BUFFERS) SELECT * FROM items ORDER BY embedding <-> '[3,1,2]' LIMIT 5;
```

#### Exact Search

To speed up queries without an index, increase `max_parallel_workers_per_gather`.

```sql
SET max_parallel_workers_per_gather = 4;
```

If vectors are normalized to length 1 (like [OpenAI embeddings](https://platform.openai.com/docs/guides/embeddings/which-distance-function-should-i-use)), use inner product for best performance.

```tsql
SELECT * FROM items ORDER BY embedding <#> '[3,1,2]' LIMIT 5;
```

#### Approximate Search

To speed up queries with an IVFFlat index, increase the number of inverted lists (at the expense of recall).

```sql
CREATE INDEX ON items USING ivfflat (embedding vector_l2_ops) WITH (lists = 1000);
```

### Vacuuming

Vacuuming can take a while for HNSW indexes. Speed it up by reindexing first.

```sql
REINDEX INDEX CONCURRENTLY index_name;
VACUUM table_name;
```

## Monitoring

Monitor performance with [pg_stat_statements](https://www.postgresql.org/docs/current/pgstatstatements.html) (be sure to add it to `shared_preload_libraries`).

```sql
CREATE EXTENSION pg_stat_statements;
```

Get the most time-consuming queries with:

```sql
SELECT query, calls, ROUND((total_plan_time + total_exec_time) / calls) AS avg_time_ms,
    ROUND((total_plan_time + total_exec_time) / 60000) AS total_time_min
    FROM pg_stat_statements ORDER BY total_plan_time + total_exec_time DESC LIMIT 20;
```

Monitor recall by comparing results from approximate search with exact search.

```sql
BEGIN;
SET LOCAL enable_indexscan = off; -- use exact search
SELECT ...
COMMIT;
```

## Scaling

Scale pgvector the same way you scale Postgres.

Scale vertically by increasing memory, CPU, and storage on a single instance. Use existing tools to [tune parameters](#tuning) and [monitor performance](#monitoring).

Scale horizontally with [replicas](https://www.postgresql.org/docs/current/hot-standby.html), or use [Citus](https://github.com/citusdata/citus) or another approach for sharding ([example](https://github.com/pgvector/pgvector-python/blob/master/examples/citus/example.py)).

## Languages

Use pgvector from any language with a Postgres client. You can even generate and store vectors in one language and query them in another.

Language | Libraries / Examples
--- | ---
Ada | [pgvector-ada](https://github.com/pgvector/pgvector-ada)
Algol | [pgvector-algol](https://github.com/pgvector/pgvector-algol)
C | [pgvector-c](https://github.com/pgvector/pgvector-c)
C++ | [pgvector-cpp](https://github.com/pgvector/pgvector-cpp)
C#, F#, Visual Basic | [pgvector-dotnet](https://github.com/pgvector/pgvector-dotnet)
COBOL | [pgvector-cobol](https://github.com/pgvector/pgvector-cobol)
Crystal | [pgvector-crystal](https://github.com/pgvector/pgvector-crystal)
D | [pgvector-d](https://github.com/pgvector/pgvector-d)
Dart | [pgvector-dart](https://github.com/pgvector/pgvector-dart)
Elixir | [pgvector-elixir](https://github.com/pgvector/pgvector-elixir)
Erlang | [pgvector-erlang](https://github.com/pgvector/pgvector-erlang)
Fortran | [pgvector-fortran](https://github.com/pgvector/pgvector-fortran)
Gleam | [pgvector-gleam](https://github.com/pgvector/pgvector-gleam)
Go | [pgvector-go](https://github.com/pgvector/pgvector-go)
Haskell | [pgvector-haskell](https://github.com/pgvector/pgvector-haskell)
Java, Kotlin, Groovy, Scala | [pgvector-java](https://github.com/pgvector/pgvector-java)
JavaScript, TypeScript | [pgvector-node](https://github.com/pgvector/pgvector-node)
Julia | [Pgvector.jl](https://github.com/pgvector/Pgvector.jl)
Lisp | [pgvector-lisp](https://github.com/pgvector/pgvector-lisp)
Lua | [pgvector-lua](https://github.com/pgvector/pgvector-lua)
Nim | [pgvector-nim](https://github.com/pgvector/pgvector-nim)
OCaml | [pgvector-ocaml](https://github.com/pgvector/pgvector-ocaml)
Pascal | [pgvector-pascal](https://github.com/pgvector/pgvector-pascal)
Perl | [pgvector-perl](https://github.com/pgvector/pgvector-perl)
PHP | [pgvector-php](https://github.com/pgvector/pgvector-php)
Prolog | [pgvector-prolog](https://github.com/pgvector/pgvector-prolog)
Python | [pgvector-python](https://github.com/pgvector/pgvector-python)
R | [pgvector-r](https://github.com/pgvector/pgvector-r)
Racket | [pgvector-racket](https://github.com/pgvector/pgvector-racket)
Raku | [pgvector-raku](https://github.com/pgvector/pgvector-raku)
Ruby | [pgvector-ruby](https://github.com/pgvector/pgvector-ruby), [Neighbor](https://github.com/ankane/neighbor)
Rust | [pgvector-rust](https://github.com/pgvector/pgvector-rust)
Swift | [pgvector-swift](https://github.com/pgvector/pgvector-swift)
Tcl | [pgvector-tcl](https://github.com/pgvector/pgvector-tcl)
Zig | [pgvector-zig](https://github.com/pgvector/pgvector-zig)

## Frequently Asked Questions

#### How many vectors can be stored in a single table?

A non-partitioned table has a limit of 32 TB by default in Postgres. A partitioned table can have thousands of partitions of that size.

#### Is replication supported?

Yes, pgvector uses the write-ahead log (WAL), which allows for replication and point-in-time recovery.

#### What if I want to index vectors with more than 2,000 dimensions?

You can use [half-precision vectors](#half-precision-vectors) or [half-precision indexing](#half-precision-indexing) to index up to 4,000 dimensions or [binary quantization](#binary-quantization) to index up to 64,000 dimensions. Other options are [indexing subvectors](#indexing-subvectors) (for models that support it) or [dimensionality reduction](https://en.wikipedia.org/wiki/Dimensionality_reduction).

#### Can I store vectors with different dimensions in the same column?

You can use `vector` as the type (instead of `vector(n)`).

```sql
CREATE TABLE embeddings (model_id bigint, item_id bigint, embedding vector, PRIMARY KEY (model_id, item_id));
```

However, you can only create indexes on rows with the same number of dimensions (using [expression](https://www.postgresql.org/docs/current/indexes-expressional.html) and [partial](https://www.postgresql.org/docs/current/indexes-partial.html) indexing):

```sql
CREATE INDEX ON embeddings USING hnsw ((embedding::vector(3)) vector_l2_ops) WHERE (model_id = 123);
```

and query with:

```sql
SELECT * FROM embeddings WHERE model_id = 123 ORDER BY embedding::vector(3) <-> '[3,1,2]' LIMIT 5;
```

#### Can I store vectors with more precision?

You can use the `double precision[]` or `numeric[]` type to store vectors with more precision.

```sql
CREATE TABLE items (id bigserial PRIMARY KEY, embedding double precision[]);

-- use {} instead of [] for Postgres arrays
INSERT INTO items (embedding) VALUES ('{1,2,3}'), ('{4,5,6}');
```

Optionally, add a [check constraint](https://www.postgresql.org/docs/current/ddl-constraints.html) to ensure data can be converted to the `vector` type and has the expected dimensions.

```sql
ALTER TABLE items ADD CHECK (vector_dims(embedding::vector) = 3);
```

Use [expression indexing](https://www.postgresql.org/docs/current/indexes-expressional.html) to index (at a lower precision):

```sql
CREATE INDEX ON items USING hnsw ((embedding::vector(3)) vector_l2_ops);
```

and query with:

```sql
SELECT * FROM items ORDER BY embedding::vector(3) <-> '[3,1,2]' LIMIT 5;
```

#### Do indexes need to fit into memory?

No, but like other index types, you’ll likely see better performance if they do. You can get the size of an index with:

```sql
SELECT pg_size_pretty(pg_relation_size('index_name'));
```

## Troubleshooting

#### Why isn’t a query using an index?

The query needs to have an `ORDER BY` and `LIMIT`, and the `ORDER BY` must be the result of a distance operator (not an expression) in ascending order.

```sql
-- index
ORDER BY embedding <=> '[3,1,2]' LIMIT 5;

-- no index
ORDER BY 1 - (embedding <=> '[3,1,2]') DESC LIMIT 5;
```

You can encourage the planner to use an index for a query with:

```sql
BEGIN;
SET LOCAL enable_seqscan = off;
SELECT ...
COMMIT;
```

Also, if the table is small, a table scan may be faster.

#### Why isn’t a query using a parallel table scan?

The planner doesn’t consider [out-of-line storage](https://www.postgresql.org/docs/current/storage-toast.html) in cost estimates, which can make a serial scan look cheaper. You can reduce the cost of a parallel scan for a query with:

```sql
BEGIN;
SET LOCAL min_parallel_table_scan_size = 1;
SET LOCAL parallel_setup_cost = 1;
SELECT ...
COMMIT;
```

or choose to store vectors inline:

```sql
ALTER TABLE items ALTER COLUMN embedding SET STORAGE PLAIN;
```

#### Why are there less results for a query after adding an HNSW index?

Results are limited by the size of the dynamic candidate list (`hnsw.ef_search`), which is 40 by default. There may be even less results due to dead tuples or filtering conditions in the query. Enabling [iterative index scans](#iterative-index-scans) can help address this.

Also, note that `NULL` vectors are not indexed (as well as zero vectors for cosine distance).

#### Why are there less results for a query after adding an IVFFlat index?

The index was likely created with too little data for the number of lists. Drop the index until the table has more data.

```sql
DROP INDEX index_name;
```

Results can also be limited by the number of probes (`ivfflat.probes`). Enabling [iterative index scans](#iterative-index-scans) can address this.

Also, note that `NULL` vectors are not indexed (as well as zero vectors for cosine distance).

## Reference

- [Vector](#vector-type)
- [Halfvec](#halfvec-type)
- [Bit](#bit-type)
- [Sparsevec](#sparsevec-type)

### Vector Type

Each vector takes `4 * dimensions + 8` bytes of storage. Each element is a single-precision floating-point number (like the `real` type in Postgres), and all elements must be finite (no `NaN`, `Infinity` or `-Infinity`). Vectors can have up to 16,000 dimensions.

### Vector Operators

Operator | Description | Added
--- | --- | ---
\+ | element-wise addition |
\- | element-wise subtraction |
\* | element-wise multiplication | 0.5.0
\|\| | concatenate | 0.7.0
<-> | Euclidean distance |
<#> | negative inner product |
<=> | cosine distance |
<+> | taxicab distance | 0.7.0

### Vector Functions

Function | Description | Added
--- | --- | ---
binary_quantize(vector) → bit | binary quantize | 0.7.0
cosine_distance(vector, vector) → double precision | cosine distance |
inner_product(vector, vector) → double precision | inner product |
l1_distance(vector, vector) → double precision | taxicab distance | 0.5.0
l2_distance(vector, vector) → double precision | Euclidean distance |
l2_normalize(vector) → vector | Normalize with Euclidean norm | 0.7.0
subvector(vector, integer, integer) → vector | subvector | 0.7.0
vector_dims(vector) → integer | number of dimensions |
vector_norm(vector) → double precision | Euclidean norm |

### Vector Aggregate Functions

Function | Description | Added
--- | --- | ---
avg(vector) → vector | average |
sum(vector) → vector | sum | 0.5.0

### Halfvec Type

Each half vector takes `2 * dimensions + 8` bytes of storage. Each element is a half-precision floating-point number, and all elements must be finite (no `NaN`, `Infinity` or `-Infinity`). Half vectors can have up to 16,000 dimensions.

### Halfvec Operators

Operator | Description | Added
--- | --- | ---
\+ | element-wise addition | 0.7.0
\- | element-wise subtraction | 0.7.0
\* | element-wise multiplication | 0.7.0
\|\| | concatenate | 0.7.0
<-> | Euclidean distance | 0.7.0
<#> | negative inner product | 0.7.0
<=> | cosine distance | 0.7.0
<+> | taxicab distance | 0.7.0

### Halfvec Functions

Function | Description | Added
--- | --- | ---
binary_quantize(halfvec) → bit | binary quantize | 0.7.0
cosine_distance(halfvec, halfvec) → double precision | cosine distance | 0.7.0
inner_product(halfvec, halfvec) → double precision | inner product | 0.7.0
l1_distance(halfvec, halfvec) → double precision | taxicab distance | 0.7.0
l2_distance(halfvec, halfvec) → double precision | Euclidean distance | 0.7.0
l2_norm(halfvec) → double precision | Euclidean norm | 0.7.0
l2_normalize(halfvec) → halfvec | Normalize with Euclidean norm | 0.7.0
subvector(halfvec, integer, integer) → halfvec | subvector | 0.7.0
vector_dims(halfvec) → integer | number of dimensions | 0.7.0

### Halfvec Aggregate Functions

Function | Description | Added
--- | --- | ---
avg(halfvec) → halfvec | average | 0.7.0
sum(halfvec) → halfvec | sum | 0.7.0

### Bit Type

Each bit vector takes `dimensions / 8 + 8` bytes of storage. See the [Postgres docs](https://www.postgresql.org/docs/current/datatype-bit.html) for more info.

### Bit Operators

Operator | Description | Added
--- | --- | ---
<~> | Hamming distance | 0.7.0
<%> | Jaccard distance | 0.7.0

### Bit Functions

Function | Description | Added
--- | --- | ---
hamming_distance(bit, bit) → double precision | Hamming distance | 0.7.0
jaccard_distance(bit, bit) → double precision | Jaccard distance | 0.7.0

### Sparsevec Type

Each sparse vector takes `8 * non-zero elements + 16` bytes of storage. Each element is a single-precision floating-point number, and all elements must be finite (no `NaN`, `Infinity` or `-Infinity`). Sparse vectors can have up to 16,000 non-zero elements.

### Sparsevec Operators

Operator | Description | Added
--- | --- | ---
<-> | Euclidean distance | 0.7.0
<#> | negative inner product | 0.7.0
<=> | cosine distance | 0.7.0
<+> | taxicab distance | 0.7.0

### Sparsevec Functions

Function | Description | Added
--- | --- | ---
cosine_distance(sparsevec, sparsevec) → double precision | cosine distance | 0.7.0
inner_product(sparsevec, sparsevec) → double precision | inner product | 0.7.0
l1_distance(sparsevec, sparsevec) → double precision | taxicab distance | 0.7.0
l2_distance(sparsevec, sparsevec) → double precision | Euclidean distance | 0.7.0
l2_norm(sparsevec) → double precision | Euclidean norm | 0.7.0
l2_normalize(sparsevec) → sparsevec | Normalize with Euclidean norm | 0.7.0

## Installation Notes - Linux and Mac

### Postgres Location

If your machine has multiple Postgres installations, specify the path to [pg_config](https://www.postgresql.org/docs/current/app-pgconfig.html) with:

```sh
export PG_CONFIG=/Library/PostgreSQL/18/bin/pg_config
```

Then re-run the installation instructions (run `make clean` before `make` if needed). If `sudo` is needed for `make install`, use:

```sh
sudo --preserve-env=PG_CONFIG make install
```

A few common paths on Mac are:

- EDB installer - `/Library/PostgreSQL/18/bin/pg_config`
- Homebrew (arm64) - `/opt/homebrew/opt/postgresql@18/bin/pg_config`
- Homebrew (x86-64) - `/usr/local/opt/postgresql@18/bin/pg_config`

Note: Replace `18` with your Postgres server version

### Missing Header

If compilation fails with `fatal error: postgres.h: No such file or directory`, make sure Postgres development files are installed on the server.

For Ubuntu and Debian, use:

```sh
sudo apt install postgresql-server-dev-18
```

Note: Replace `18` with your Postgres server version

### Missing SDK

If compilation fails and the output includes `warning: no such sysroot directory` on Mac, your Postgres installation points to a path that no longer exists.

```sh
pg_config --cppflags
```

Reinstall Postgres to fix this.

### Portability

By default, pgvector compiles with `-march=native` on some platforms for best performance. However, this can lead to `Illegal instruction` errors if trying to run the compiled extension on a different machine.

To compile for portability, use:

```sh
make OPTFLAGS=""
```

## Installation Notes - Windows

### Missing Header

If compilation fails with `Cannot open include file: 'postgres.h': No such file or directory`, make sure `PGROOT` is correct.

### Mismatched Architecture

If compilation fails with `error C2196: case value '4' already used`, make sure you’re using the `x64 Native Tools Command Prompt`. Then run `nmake /F Makefile.win clean` and re-run the installation instructions.

### Missing Symbol

If linking fails with `unresolved external symbol float_to_shortest_decimal_bufn` with Postgres 17.0-17.2, upgrade to Postgres 17.3+.

### Permissions

If installation fails with `Access is denied`, re-run the installation instructions as an administrator.

## Additional Installation Methods

### Docker

Get the [Docker image](https://hub.docker.com/r/pgvector/pgvector) with:

```sh
docker pull pgvector/pgvector:pg18-trixie
```

This adds pgvector to the [Postgres image](https://hub.docker.com/_/postgres) (replace `18` with your Postgres server version, and run it the same way).

Supported tags are:

- `pg18-trixie`, `0.8.2-pg18-trixie`
- `pg18-bookworm`, `0.8.2-pg18-bookworm`, `pg18`, `0.8.2-pg18`
- `pg17-trixie`, `0.8.2-pg17-trixie`
- `pg17-bookworm`, `0.8.2-pg17-bookworm`, `pg17`, `0.8.2-pg17`
- `pg16-trixie`, `0.8.2-pg16-trixie`
- `pg16-bookworm`, `0.8.2-pg16-bookworm`, `pg16`, `0.8.2-pg16`
- `pg15-trixie`, `0.8.2-pg15-trixie`
- `pg15-bookworm`, `0.8.2-pg15-bookworm`, `pg15`, `0.8.2-pg15`
- `pg14-trixie`, `0.8.2-pg14-trixie`
- `pg14-bookworm`, `0.8.2-pg14-bookworm`, `pg14`, `0.8.2-pg14`
- `pg13-trixie`, `0.8.2-pg13-trixie`
- `pg13-bookworm`, `0.8.2-pg13-bookworm`, `pg13`, `0.8.2-pg13`

You can also build the image manually:

```sh
git clone --branch v0.8.2 https://github.com/pgvector/pgvector.git
cd pgvector
docker build --pull --build-arg PG_MAJOR=18 -t myuser/pgvector .
```

If you increase `maintenance_work_mem`, make sure `--shm-size` is at least that size to avoid an error with parallel HNSW index builds.

```sh
docker run --shm-size=1g ...
```

### Homebrew

With Homebrew Postgres, you can use:

```sh
brew install pgvector
```

Note: This only adds it to the `postgresql@18` and `postgresql@17` formulas

### PGXN

Install from the [PostgreSQL Extension Network](https://pgxn.org/dist/vector) with:

```sh
pgxn install vector
```

### APT

Debian and Ubuntu packages are available from the [PostgreSQL APT Repository](https://wiki.postgresql.org/wiki/Apt). Follow the [setup instructions](https://wiki.postgresql.org/wiki/Apt#Quickstart) and run:

```sh
sudo apt install postgresql-18-pgvector
```

Note: Replace `18` with your Postgres server version

### Yum

RPM packages are available from the [PostgreSQL Yum Repository](https://yum.postgresql.org/). Follow the [setup instructions](https://www.postgresql.org/download/linux/redhat/) for your distribution and run:

```sh
sudo yum install pgvector_18
# or
sudo dnf install pgvector_18
```

Note: Replace `18` with your Postgres server version

### pkg

Install the FreeBSD package with:

```sh
pkg install postgresql17-pgvector
```

or the port with:

```sh
cd /usr/ports/databases/pgvector
make install
```

### APK

Install the Alpine package with:

```sh
apk add postgresql-pgvector
```

### conda-forge

With Conda Postgres, install from [conda-forge](https://anaconda.org/conda-forge/pgvector) with:

```sh
conda install -c conda-forge pgvector
```

This method is [community-maintained](https://github.com/conda-forge/pgvector-feedstock) by [@mmcauliffe](https://github.com/mmcauliffe)

### Postgres.app

Download the [latest release](https://postgresapp.com/downloads.html) with Postgres 15+.

## Hosted Postgres

pgvector is available on [these providers](https://github.com/pgvector/pgvector/issues/54).

## Upgrading

[Install](#installation) the latest version (use the same method as the original installation). Then in each database you want to upgrade, run:

```sql
ALTER EXTENSION vector UPDATE;
```

You can check the version in the current database with:

```sql
SELECT extversion FROM pg_extension WHERE extname = 'vector';
```

## Thanks

Thanks to:

- [PASE: PostgreSQL Ultra-High-Dimensional Approximate Nearest Neighbor Search Extension](https://dl.acm.org/doi/pdf/10.1145/3318464.3386131)
- [Faiss: A Library for Efficient Similarity Search and Clustering of Dense Vectors](https://github.com/facebookresearch/faiss)
- [Using the Triangle Inequality to Accelerate k-means](https://cdn.aaai.org/ICML/2003/ICML03-022.pdf)
- [k-means++: The Advantage of Careful Seeding](https://theory.stanford.edu/~sergei/papers/kMeansPP-soda.pdf)
- [Concept Decompositions for Large Sparse Text Data using Clustering](https://www.cs.utexas.edu/users/inderjit/public_papers/concept_mlj.pdf)
- [Efficient and Robust Approximate Nearest Neighbor Search using Hierarchical Navigable Small World Graphs](https://arxiv.org/ftp/arxiv/papers/1603/1603.09320.pdf)

## History

View the [changelog](https://github.com/pgvector/pgvector/blob/master/CHANGELOG.md)

## Contributing

Everyone is encouraged to help improve this project. Here are a few ways you can help:

- [Report bugs](https://github.com/pgvector/pgvector/issues)
- Fix bugs and [submit pull requests](https://github.com/pgvector/pgvector/pulls)
- Write, clarify, or fix documentation
- Suggest or add new features

To get started with development:

```sh
git clone https://github.com/pgvector/pgvector.git
cd pgvector
make
make install
```

To run all tests:

```sh
make installcheck        # regression tests
make prove_installcheck  # TAP tests
```

To run single tests:

```sh
make installcheck REGRESS=functions                            # regression test
make prove_installcheck PROVE_TESTS=test/t/001_ivfflat_wal.pl  # TAP test
```

To enable assertions:

```sh
make clean && PG_CFLAGS="-DUSE_ASSERT_CHECKING" make && make install
```

To enable benchmarking:

```sh
make clean && PG_CFLAGS="-DIVFFLAT_BENCH" make && make install
```

To show memory usage:

```sh
make clean && PG_CFLAGS="-DHNSW_MEMORY -DIVFFLAT_MEMORY" make && make install
```

To get k-means metrics:

```sh
make clean && PG_CFLAGS="-DIVFFLAT_KMEANS_DEBUG" make && make install
```

Resources for contributors

- [Extension Building Infrastructure](https://www.postgresql.org/docs/current/extend-pgxs.html)
- [Index Access Method Interface Definition](https://www.postgresql.org/docs/current/indexam.html)
- [Generic WAL Records](https://www.postgresql.org/docs/current/generic-wal.html)
```

## File: `vector.control`
```
comment = 'vector data type and ivfflat and hnsw access methods'
default_version = '0.8.2'
module_pathname = '$libdir/vector'
relocatable = true
```

## File: `sql/vector--0.1.0--0.1.1.sql`
```sql
-- complain if script is sourced in psql, rather than via CREATE EXTENSION
\echo Use "ALTER EXTENSION vector UPDATE TO '0.1.1'" to load this file. \quit

CREATE FUNCTION vector_recv(internal, oid, integer) RETURNS vector
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT;

CREATE FUNCTION vector_send(vector) RETURNS bytea
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT;

ALTER TYPE vector SET ( RECEIVE = vector_recv, SEND = vector_send );

-- functions

ALTER FUNCTION vector_in(cstring, oid, integer) PARALLEL SAFE;
ALTER FUNCTION vector_out(vector) PARALLEL SAFE;
ALTER FUNCTION vector_typmod_in(cstring[]) PARALLEL SAFE;
ALTER FUNCTION vector_recv(internal, oid, integer) PARALLEL SAFE;
ALTER FUNCTION vector_send(vector) PARALLEL SAFE;
ALTER FUNCTION l2_distance(vector, vector) PARALLEL SAFE;
ALTER FUNCTION inner_product(vector, vector) PARALLEL SAFE;
ALTER FUNCTION cosine_distance(vector, vector) PARALLEL SAFE;
ALTER FUNCTION vector_dims(vector) PARALLEL SAFE;
ALTER FUNCTION vector_norm(vector) PARALLEL SAFE;
ALTER FUNCTION vector_add(vector, vector) PARALLEL SAFE;
ALTER FUNCTION vector_sub(vector, vector) PARALLEL SAFE;
ALTER FUNCTION vector_lt(vector, vector) PARALLEL SAFE;
ALTER FUNCTION vector_le(vector, vector) PARALLEL SAFE;
ALTER FUNCTION vector_eq(vector, vector) PARALLEL SAFE;
ALTER FUNCTION vector_ne(vector, vector) PARALLEL SAFE;
ALTER FUNCTION vector_ge(vector, vector) PARALLEL SAFE;
ALTER FUNCTION vector_gt(vector, vector) PARALLEL SAFE;
ALTER FUNCTION vector_cmp(vector, vector) PARALLEL SAFE;
ALTER FUNCTION vector_l2_squared_distance(vector, vector) PARALLEL SAFE;
ALTER FUNCTION vector_negative_inner_product(vector, vector) PARALLEL SAFE;
ALTER FUNCTION vector_spherical_distance(vector, vector) PARALLEL SAFE;
ALTER FUNCTION vector(vector, integer, boolean) PARALLEL SAFE;
ALTER FUNCTION array_to_vector(integer[], integer, boolean) PARALLEL SAFE;
ALTER FUNCTION array_to_vector(real[], integer, boolean) PARALLEL SAFE;
ALTER FUNCTION array_to_vector(double precision[], integer, boolean) PARALLEL SAFE;
```

## File: `sql/vector--0.1.1--0.1.3.sql`
```sql
-- complain if script is sourced in psql, rather than via CREATE EXTENSION
\echo Use "ALTER EXTENSION vector UPDATE TO '0.1.3'" to load this file. \quit
```

## File: `sql/vector--0.1.3--0.1.4.sql`
```sql
-- complain if script is sourced in psql, rather than via CREATE EXTENSION
\echo Use "ALTER EXTENSION vector UPDATE TO '0.1.4'" to load this file. \quit
```

## File: `sql/vector--0.1.4--0.1.5.sql`
```sql
-- complain if script is sourced in psql, rather than via CREATE EXTENSION
\echo Use "ALTER EXTENSION vector UPDATE TO '0.1.5'" to load this file. \quit
```

## File: `sql/vector--0.1.5--0.1.6.sql`
```sql
-- complain if script is sourced in psql, rather than via CREATE EXTENSION
\echo Use "ALTER EXTENSION vector UPDATE TO '0.1.6'" to load this file. \quit
```

## File: `sql/vector--0.1.6--0.1.7.sql`
```sql
-- complain if script is sourced in psql, rather than via CREATE EXTENSION
\echo Use "ALTER EXTENSION vector UPDATE TO '0.1.7'" to load this file. \quit

CREATE FUNCTION array_to_vector(numeric[], integer, boolean) RETURNS vector
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE CAST (numeric[] AS vector)
	WITH FUNCTION array_to_vector(numeric[], integer, boolean) AS IMPLICIT;
```

## File: `sql/vector--0.1.7--0.1.8.sql`
```sql
-- complain if script is sourced in psql, rather than via CREATE EXTENSION
\echo Use "ALTER EXTENSION vector UPDATE TO '0.1.8'" to load this file. \quit

CREATE FUNCTION vector_to_float4(vector, integer, boolean) RETURNS real[]
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE CAST (vector AS real[])
	WITH FUNCTION vector_to_float4(vector, integer, boolean) AS IMPLICIT;
```

## File: `sql/vector--0.1.8--0.2.0.sql`
```sql
-- complain if script is sourced in psql, rather than via CREATE EXTENSION
\echo Use "ALTER EXTENSION vector UPDATE TO '0.2.0'" to load this file. \quit
```

## File: `sql/vector--0.2.0--0.2.1.sql`
```sql
-- complain if script is sourced in psql, rather than via CREATE EXTENSION
\echo Use "ALTER EXTENSION vector UPDATE TO '0.2.1'" to load this file. \quit

DROP CAST (integer[] AS vector);
DROP CAST (real[] AS vector);
DROP CAST (double precision[] AS vector);
DROP CAST (numeric[] AS vector);

CREATE CAST (integer[] AS vector)
	WITH FUNCTION array_to_vector(integer[], integer, boolean) AS ASSIGNMENT;

CREATE CAST (real[] AS vector)
	WITH FUNCTION array_to_vector(real[], integer, boolean) AS ASSIGNMENT;

CREATE CAST (double precision[] AS vector)
	WITH FUNCTION array_to_vector(double precision[], integer, boolean) AS ASSIGNMENT;

CREATE CAST (numeric[] AS vector)
	WITH FUNCTION array_to_vector(numeric[], integer, boolean) AS ASSIGNMENT;
```

## File: `sql/vector--0.2.1--0.2.2.sql`
```sql
-- complain if script is sourced in psql, rather than via CREATE EXTENSION
\echo Use "ALTER EXTENSION vector UPDATE TO '0.2.2'" to load this file. \quit
```

## File: `sql/vector--0.2.2--0.2.3.sql`
```sql
-- complain if script is sourced in psql, rather than via CREATE EXTENSION
\echo Use "ALTER EXTENSION vector UPDATE TO '0.2.3'" to load this file. \quit
```

## File: `sql/vector--0.2.3--0.2.4.sql`
```sql
-- complain if script is sourced in psql, rather than via CREATE EXTENSION
\echo Use "ALTER EXTENSION vector UPDATE TO '0.2.4'" to load this file. \quit
```

## File: `sql/vector--0.2.4--0.2.5.sql`
```sql
-- complain if script is sourced in psql, rather than via CREATE EXTENSION
\echo Use "ALTER EXTENSION vector UPDATE TO '0.2.5'" to load this file. \quit
```

## File: `sql/vector--0.2.5--0.2.6.sql`
```sql
-- complain if script is sourced in psql, rather than via CREATE EXTENSION
\echo Use "ALTER EXTENSION vector UPDATE TO '0.2.6'" to load this file. \quit
```

## File: `sql/vector--0.2.6--0.2.7.sql`
```sql
-- complain if script is sourced in psql, rather than via CREATE EXTENSION
\echo Use "ALTER EXTENSION vector UPDATE TO '0.2.7'" to load this file. \quit
```

## File: `sql/vector--0.2.7--0.3.0.sql`
```sql
-- complain if script is sourced in psql, rather than via CREATE EXTENSION
\echo Use "ALTER EXTENSION vector UPDATE TO '0.3.0'" to load this file. \quit
```

## File: `sql/vector--0.3.0--0.3.1.sql`
```sql
-- complain if script is sourced in psql, rather than via CREATE EXTENSION
\echo Use "ALTER EXTENSION vector UPDATE TO '0.3.1'" to load this file. \quit
```

## File: `sql/vector--0.3.1--0.3.2.sql`
```sql
-- complain if script is sourced in psql, rather than via CREATE EXTENSION
\echo Use "ALTER EXTENSION vector UPDATE TO '0.3.2'" to load this file. \quit
```

## File: `sql/vector--0.3.2--0.4.0.sql`
```sql
-- complain if script is sourced in psql, rather than via CREATE EXTENSION
\echo Use "ALTER EXTENSION vector UPDATE TO '0.4.0'" to load this file. \quit

-- remove this single line for Postgres < 13
ALTER TYPE vector SET (STORAGE = extended);

CREATE FUNCTION vector_accum(double precision[], vector) RETURNS double precision[]
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION vector_avg(double precision[]) RETURNS vector
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION vector_combine(double precision[], double precision[]) RETURNS double precision[]
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE AGGREGATE avg(vector) (
	SFUNC = vector_accum,
	STYPE = double precision[],
	FINALFUNC = vector_avg,
	COMBINEFUNC = vector_combine,
	INITCOND = '{0}',
	PARALLEL = SAFE
);
```

## File: `sql/vector--0.4.0--0.4.1.sql`
```sql
-- complain if script is sourced in psql, rather than via CREATE EXTENSION
\echo Use "ALTER EXTENSION vector UPDATE TO '0.4.1'" to load this file. \quit
```

## File: `sql/vector--0.4.1--0.4.2.sql`
```sql
-- complain if script is sourced in psql, rather than via CREATE EXTENSION
\echo Use "ALTER EXTENSION vector UPDATE TO '0.4.2'" to load this file. \quit
```

## File: `sql/vector--0.4.2--0.4.3.sql`
```sql
-- complain if script is sourced in psql, rather than via CREATE EXTENSION
\echo Use "ALTER EXTENSION vector UPDATE TO '0.4.3'" to load this file. \quit
```

## File: `sql/vector--0.4.3--0.4.4.sql`
```sql
-- complain if script is sourced in psql, rather than via CREATE EXTENSION
\echo Use "ALTER EXTENSION vector UPDATE TO '0.4.4'" to load this file. \quit
```

## File: `sql/vector--0.4.4--0.5.0.sql`
```sql
-- complain if script is sourced in psql, rather than via CREATE EXTENSION
\echo Use "ALTER EXTENSION vector UPDATE TO '0.5.0'" to load this file. \quit

CREATE FUNCTION l1_distance(vector, vector) RETURNS float8
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION vector_mul(vector, vector) RETURNS vector
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE OPERATOR * (
	LEFTARG = vector, RIGHTARG = vector, PROCEDURE = vector_mul,
	COMMUTATOR = *
);

CREATE AGGREGATE sum(vector) (
	SFUNC = vector_add,
	STYPE = vector,
	COMBINEFUNC = vector_add,
	PARALLEL = SAFE
);

CREATE FUNCTION hnswhandler(internal) RETURNS index_am_handler
	AS 'MODULE_PATHNAME' LANGUAGE C;

CREATE ACCESS METHOD hnsw TYPE INDEX HANDLER hnswhandler;

COMMENT ON ACCESS METHOD hnsw IS 'hnsw index access method';

CREATE OPERATOR CLASS vector_l2_ops
	FOR TYPE vector USING hnsw AS
	OPERATOR 1 <-> (vector, vector) FOR ORDER BY float_ops,
	FUNCTION 1 vector_l2_squared_distance(vector, vector);

CREATE OPERATOR CLASS vector_ip_ops
	FOR TYPE vector USING hnsw AS
	OPERATOR 1 <#> (vector, vector) FOR ORDER BY float_ops,
	FUNCTION 1 vector_negative_inner_product(vector, vector);

CREATE OPERATOR CLASS vector_cosine_ops
	FOR TYPE vector USING hnsw AS
	OPERATOR 1 <=> (vector, vector) FOR ORDER BY float_ops,
	FUNCTION 1 vector_negative_inner_product(vector, vector),
	FUNCTION 2 vector_norm(vector);
```

## File: `sql/vector--0.5.0--0.5.1.sql`
```sql
-- complain if script is sourced in psql, rather than via CREATE EXTENSION
\echo Use "ALTER EXTENSION vector UPDATE TO '0.5.1'" to load this file. \quit
```

## File: `sql/vector--0.5.1--0.6.0.sql`
```sql
-- complain if script is sourced in psql, rather than via CREATE EXTENSION
\echo Use "ALTER EXTENSION vector UPDATE TO '0.6.0'" to load this file. \quit

-- remove this single line for Postgres < 13
ALTER TYPE vector SET (STORAGE = external);
```

## File: `sql/vector--0.6.0--0.6.1.sql`
```sql
-- complain if script is sourced in psql, rather than via CREATE EXTENSION
\echo Use "ALTER EXTENSION vector UPDATE TO '0.6.1'" to load this file. \quit

DROP OPERATOR - (vector, vector);

CREATE OPERATOR - (
	LEFTARG = vector, RIGHTARG = vector, PROCEDURE = vector_sub
);

ALTER OPERATOR <= (vector, vector) SET (
	RESTRICT = scalarlesel, JOIN = scalarlejoinsel
);

ALTER OPERATOR >= (vector, vector) SET (
	RESTRICT = scalargesel, JOIN = scalargejoinsel
);
```

## File: `sql/vector--0.6.1--0.6.2.sql`
```sql
-- complain if script is sourced in psql, rather than via CREATE EXTENSION
\echo Use "ALTER EXTENSION vector UPDATE TO '0.6.2'" to load this file. \quit
```

## File: `sql/vector--0.6.2--0.7.0.sql`
```sql
-- complain if script is sourced in psql, rather than via CREATE EXTENSION
\echo Use "ALTER EXTENSION vector UPDATE TO '0.7.0'" to load this file. \quit

CREATE FUNCTION l2_normalize(vector) RETURNS vector
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION binary_quantize(vector) RETURNS bit
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION subvector(vector, int, int) RETURNS vector
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION vector_concat(vector, vector) RETURNS vector
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE OPERATOR <+> (
	LEFTARG = vector, RIGHTARG = vector, PROCEDURE = l1_distance,
	COMMUTATOR = '<+>'
);

CREATE OPERATOR || (
	LEFTARG = vector, RIGHTARG = vector, PROCEDURE = vector_concat
);

CREATE FUNCTION ivfflat_halfvec_support(internal) RETURNS internal
	AS 'MODULE_PATHNAME' LANGUAGE C;

CREATE FUNCTION ivfflat_bit_support(internal) RETURNS internal
	AS 'MODULE_PATHNAME' LANGUAGE C;

CREATE FUNCTION hnsw_halfvec_support(internal) RETURNS internal
	AS 'MODULE_PATHNAME' LANGUAGE C;

CREATE FUNCTION hnsw_bit_support(internal) RETURNS internal
	AS 'MODULE_PATHNAME' LANGUAGE C;

CREATE FUNCTION hnsw_sparsevec_support(internal) RETURNS internal
	AS 'MODULE_PATHNAME' LANGUAGE C;

CREATE OPERATOR CLASS vector_l1_ops
	FOR TYPE vector USING hnsw AS
	OPERATOR 1 <+> (vector, vector) FOR ORDER BY float_ops,
	FUNCTION 1 l1_distance(vector, vector);

CREATE TYPE halfvec;

CREATE FUNCTION halfvec_in(cstring, oid, integer) RETURNS halfvec
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION halfvec_out(halfvec) RETURNS cstring
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION halfvec_typmod_in(cstring[]) RETURNS integer
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION halfvec_recv(internal, oid, integer) RETURNS halfvec
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION halfvec_send(halfvec) RETURNS bytea
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE TYPE halfvec (
	INPUT     = halfvec_in,
	OUTPUT    = halfvec_out,
	TYPMOD_IN = halfvec_typmod_in,
	RECEIVE   = halfvec_recv,
	SEND      = halfvec_send,
	STORAGE   = external
);

CREATE FUNCTION l2_distance(halfvec, halfvec) RETURNS float8
	AS 'MODULE_PATHNAME', 'halfvec_l2_distance' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION inner_product(halfvec, halfvec) RETURNS float8
	AS 'MODULE_PATHNAME', 'halfvec_inner_product' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION cosine_distance(halfvec, halfvec) RETURNS float8
	AS 'MODULE_PATHNAME', 'halfvec_cosine_distance' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION l1_distance(halfvec, halfvec) RETURNS float8
	AS 'MODULE_PATHNAME', 'halfvec_l1_distance' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION vector_dims(halfvec) RETURNS integer
	AS 'MODULE_PATHNAME', 'halfvec_vector_dims' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION l2_norm(halfvec) RETURNS float8
	AS 'MODULE_PATHNAME', 'halfvec_l2_norm' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION l2_normalize(halfvec) RETURNS halfvec
	AS 'MODULE_PATHNAME', 'halfvec_l2_normalize' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION binary_quantize(halfvec) RETURNS bit
	AS 'MODULE_PATHNAME', 'halfvec_binary_quantize' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION subvector(halfvec, int, int) RETURNS halfvec
	AS 'MODULE_PATHNAME', 'halfvec_subvector' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION halfvec_add(halfvec, halfvec) RETURNS halfvec
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION halfvec_sub(halfvec, halfvec) RETURNS halfvec
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION halfvec_mul(halfvec, halfvec) RETURNS halfvec
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION halfvec_concat(halfvec, halfvec) RETURNS halfvec
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION halfvec_lt(halfvec, halfvec) RETURNS bool
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION halfvec_le(halfvec, halfvec) RETURNS bool
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION halfvec_eq(halfvec, halfvec) RETURNS bool
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION halfvec_ne(halfvec, halfvec) RETURNS bool
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION halfvec_ge(halfvec, halfvec) RETURNS bool
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION halfvec_gt(halfvec, halfvec) RETURNS bool
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION halfvec_cmp(halfvec, halfvec) RETURNS int4
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION halfvec_l2_squared_distance(halfvec, halfvec) RETURNS float8
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION halfvec_negative_inner_product(halfvec, halfvec) RETURNS float8
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION halfvec_spherical_distance(halfvec, halfvec) RETURNS float8
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION halfvec_accum(double precision[], halfvec) RETURNS double precision[]
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION halfvec_avg(double precision[]) RETURNS halfvec
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION halfvec_combine(double precision[], double precision[]) RETURNS double precision[]
	AS 'MODULE_PATHNAME', 'vector_combine' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE AGGREGATE avg(halfvec) (
	SFUNC = halfvec_accum,
	STYPE = double precision[],
	FINALFUNC = halfvec_avg,
	COMBINEFUNC = halfvec_combine,
	INITCOND = '{0}',
	PARALLEL = SAFE
);

CREATE AGGREGATE sum(halfvec) (
	SFUNC = halfvec_add,
	STYPE = halfvec,
	COMBINEFUNC = halfvec_add,
	PARALLEL = SAFE
);

CREATE FUNCTION halfvec(halfvec, integer, boolean) RETURNS halfvec
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION halfvec_to_vector(halfvec, integer, boolean) RETURNS vector
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION vector_to_halfvec(vector, integer, boolean) RETURNS halfvec
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION array_to_halfvec(integer[], integer, boolean) RETURNS halfvec
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION array_to_halfvec(real[], integer, boolean) RETURNS halfvec
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION array_to_halfvec(double precision[], integer, boolean) RETURNS halfvec
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION array_to_halfvec(numeric[], integer, boolean) RETURNS halfvec
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION halfvec_to_float4(halfvec, integer, boolean) RETURNS real[]
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE CAST (halfvec AS halfvec)
	WITH FUNCTION halfvec(halfvec, integer, boolean) AS IMPLICIT;

CREATE CAST (halfvec AS vector)
	WITH FUNCTION halfvec_to_vector(halfvec, integer, boolean) AS ASSIGNMENT;

CREATE CAST (vector AS halfvec)
	WITH FUNCTION vector_to_halfvec(vector, integer, boolean) AS IMPLICIT;

CREATE CAST (halfvec AS real[])
	WITH FUNCTION halfvec_to_float4(halfvec, integer, boolean) AS ASSIGNMENT;

CREATE CAST (integer[] AS halfvec)
	WITH FUNCTION array_to_halfvec(integer[], integer, boolean) AS ASSIGNMENT;

CREATE CAST (real[] AS halfvec)
	WITH FUNCTION array_to_halfvec(real[], integer, boolean) AS ASSIGNMENT;

CREATE CAST (double precision[] AS halfvec)
	WITH FUNCTION array_to_halfvec(double precision[], integer, boolean) AS ASSIGNMENT;

CREATE CAST (numeric[] AS halfvec)
	WITH FUNCTION array_to_halfvec(numeric[], integer, boolean) AS ASSIGNMENT;

CREATE OPERATOR <-> (
	LEFTARG = halfvec, RIGHTARG = halfvec, PROCEDURE = l2_distance,
	COMMUTATOR = '<->'
);

CREATE OPERATOR <#> (
	LEFTARG = halfvec, RIGHTARG = halfvec, PROCEDURE = halfvec_negative_inner_product,
	COMMUTATOR = '<#>'
);

CREATE OPERATOR <=> (
	LEFTARG = halfvec, RIGHTARG = halfvec, PROCEDURE = cosine_distance,
	COMMUTATOR = '<=>'
);

CREATE OPERATOR <+> (
	LEFTARG = halfvec, RIGHTARG = halfvec, PROCEDURE = l1_distance,
	COMMUTATOR = '<+>'
);

CREATE OPERATOR + (
	LEFTARG = halfvec, RIGHTARG = halfvec, PROCEDURE = halfvec_add,
	COMMUTATOR = +
);

CREATE OPERATOR - (
	LEFTARG = halfvec, RIGHTARG = halfvec, PROCEDURE = halfvec_sub
);

CREATE OPERATOR * (
	LEFTARG = halfvec, RIGHTARG = halfvec, PROCEDURE = halfvec_mul,
	COMMUTATOR = *
);

CREATE OPERATOR || (
	LEFTARG = halfvec, RIGHTARG = halfvec, PROCEDURE = halfvec_concat
);

CREATE OPERATOR < (
	LEFTARG = halfvec, RIGHTARG = halfvec, PROCEDURE = halfvec_lt,
	COMMUTATOR = > , NEGATOR = >= ,
	RESTRICT = scalarltsel, JOIN = scalarltjoinsel
);

CREATE OPERATOR <= (
	LEFTARG = halfvec, RIGHTARG = halfvec, PROCEDURE = halfvec_le,
	COMMUTATOR = >= , NEGATOR = > ,
	RESTRICT = scalarlesel, JOIN = scalarlejoinsel
);

CREATE OPERATOR = (
	LEFTARG = halfvec, RIGHTARG = halfvec, PROCEDURE = halfvec_eq,
	COMMUTATOR = = , NEGATOR = <> ,
	RESTRICT = eqsel, JOIN = eqjoinsel
);

CREATE OPERATOR <> (
	LEFTARG = halfvec, RIGHTARG = halfvec, PROCEDURE = halfvec_ne,
	COMMUTATOR = <> , NEGATOR = = ,
	RESTRICT = eqsel, JOIN = eqjoinsel
);

CREATE OPERATOR >= (
	LEFTARG = halfvec, RIGHTARG = halfvec, PROCEDURE = halfvec_ge,
	COMMUTATOR = <= , NEGATOR = < ,
	RESTRICT = scalargesel, JOIN = scalargejoinsel
);

CREATE OPERATOR > (
	LEFTARG = halfvec, RIGHTARG = halfvec, PROCEDURE = halfvec_gt,
	COMMUTATOR = < , NEGATOR = <= ,
	RESTRICT = scalargtsel, JOIN = scalargtjoinsel
);

CREATE OPERATOR CLASS halfvec_ops
	DEFAULT FOR TYPE halfvec USING btree AS
	OPERATOR 1 < ,
	OPERATOR 2 <= ,
	OPERATOR 3 = ,
	OPERATOR 4 >= ,
	OPERATOR 5 > ,
	FUNCTION 1 halfvec_cmp(halfvec, halfvec);

CREATE OPERATOR CLASS halfvec_l2_ops
	FOR TYPE halfvec USING ivfflat AS
	OPERATOR 1 <-> (halfvec, halfvec) FOR ORDER BY float_ops,
	FUNCTION 1 halfvec_l2_squared_distance(halfvec, halfvec),
	FUNCTION 3 l2_distance(halfvec, halfvec),
	FUNCTION 5 ivfflat_halfvec_support(internal);

CREATE OPERATOR CLASS halfvec_ip_ops
	FOR TYPE halfvec USING ivfflat AS
	OPERATOR 1 <#> (halfvec, halfvec) FOR ORDER BY float_ops,
	FUNCTION 1 halfvec_negative_inner_product(halfvec, halfvec),
	FUNCTION 3 halfvec_spherical_distance(halfvec, halfvec),
	FUNCTION 4 l2_norm(halfvec),
	FUNCTION 5 ivfflat_halfvec_support(internal);

CREATE OPERATOR CLASS halfvec_cosine_ops
	FOR TYPE halfvec USING ivfflat AS
	OPERATOR 1 <=> (halfvec, halfvec) FOR ORDER BY float_ops,
	FUNCTION 1 halfvec_negative_inner_product(halfvec, halfvec),
	FUNCTION 2 l2_norm(halfvec),
	FUNCTION 3 halfvec_spherical_distance(halfvec, halfvec),
	FUNCTION 4 l2_norm(halfvec),
	FUNCTION 5 ivfflat_halfvec_support(internal);

CREATE OPERATOR CLASS halfvec_l2_ops
	FOR TYPE halfvec USING hnsw AS
	OPERATOR 1 <-> (halfvec, halfvec) FOR ORDER BY float_ops,
	FUNCTION 1 halfvec_l2_squared_distance(halfvec, halfvec),
	FUNCTION 3 hnsw_halfvec_support(internal);

CREATE OPERATOR CLASS halfvec_ip_ops
	FOR TYPE halfvec USING hnsw AS
	OPERATOR 1 <#> (halfvec, halfvec) FOR ORDER BY float_ops,
	FUNCTION 1 halfvec_negative_inner_product(halfvec, halfvec),
	FUNCTION 3 hnsw_halfvec_support(internal);

CREATE OPERATOR CLASS halfvec_cosine_ops
	FOR TYPE halfvec USING hnsw AS
	OPERATOR 1 <=> (halfvec, halfvec) FOR ORDER BY float_ops,
	FUNCTION 1 halfvec_negative_inner_product(halfvec, halfvec),
	FUNCTION 2 l2_norm(halfvec),
	FUNCTION 3 hnsw_halfvec_support(internal);

CREATE OPERATOR CLASS halfvec_l1_ops
	FOR TYPE halfvec USING hnsw AS
	OPERATOR 1 <+> (halfvec, halfvec) FOR ORDER BY float_ops,
	FUNCTION 1 l1_distance(halfvec, halfvec),
	FUNCTION 3 hnsw_halfvec_support(internal);

CREATE FUNCTION hamming_distance(bit, bit) RETURNS float8
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION jaccard_distance(bit, bit) RETURNS float8
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE OPERATOR <~> (
	LEFTARG = bit, RIGHTARG = bit, PROCEDURE = hamming_distance,
	COMMUTATOR = '<~>'
);

CREATE OPERATOR <%> (
	LEFTARG = bit, RIGHTARG = bit, PROCEDURE = jaccard_distance,
	COMMUTATOR = '<%>'
);

CREATE OPERATOR CLASS bit_hamming_ops
	FOR TYPE bit USING ivfflat AS
	OPERATOR 1 <~> (bit, bit) FOR ORDER BY float_ops,
	FUNCTION 1 hamming_distance(bit, bit),
	FUNCTION 3 hamming_distance(bit, bit),
	FUNCTION 5 ivfflat_bit_support(internal);

CREATE OPERATOR CLASS bit_hamming_ops
	FOR TYPE bit USING hnsw AS
	OPERATOR 1 <~> (bit, bit) FOR ORDER BY float_ops,
	FUNCTION 1 hamming_distance(bit, bit),
	FUNCTION 3 hnsw_bit_support(internal);

CREATE OPERATOR CLASS bit_jaccard_ops
	FOR TYPE bit USING hnsw AS
	OPERATOR 1 <%> (bit, bit) FOR ORDER BY float_ops,
	FUNCTION 1 jaccard_distance(bit, bit),
	FUNCTION 3 hnsw_bit_support(internal);

CREATE TYPE sparsevec;

CREATE FUNCTION sparsevec_in(cstring, oid, integer) RETURNS sparsevec
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION sparsevec_out(sparsevec) RETURNS cstring
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION sparsevec_typmod_in(cstring[]) RETURNS integer
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION sparsevec_recv(internal, oid, integer) RETURNS sparsevec
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION sparsevec_send(sparsevec) RETURNS bytea
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE TYPE sparsevec (
	INPUT     = sparsevec_in,
	OUTPUT    = sparsevec_out,
	TYPMOD_IN = sparsevec_typmod_in,
	RECEIVE   = sparsevec_recv,
	SEND      = sparsevec_send,
	STORAGE   = external
);

CREATE FUNCTION l2_distance(sparsevec, sparsevec) RETURNS float8
	AS 'MODULE_PATHNAME', 'sparsevec_l2_distance' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION inner_product(sparsevec, sparsevec) RETURNS float8
	AS 'MODULE_PATHNAME', 'sparsevec_inner_product' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION cosine_distance(sparsevec, sparsevec) RETURNS float8
	AS 'MODULE_PATHNAME', 'sparsevec_cosine_distance' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION l1_distance(sparsevec, sparsevec) RETURNS float8
	AS 'MODULE_PATHNAME', 'sparsevec_l1_distance' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION l2_norm(sparsevec) RETURNS float8
	AS 'MODULE_PATHNAME', 'sparsevec_l2_norm' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION l2_normalize(sparsevec) RETURNS sparsevec
	AS 'MODULE_PATHNAME', 'sparsevec_l2_normalize' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION sparsevec_lt(sparsevec, sparsevec) RETURNS bool
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION sparsevec_le(sparsevec, sparsevec) RETURNS bool
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION sparsevec_eq(sparsevec, sparsevec) RETURNS bool
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION sparsevec_ne(sparsevec, sparsevec) RETURNS bool
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION sparsevec_ge(sparsevec, sparsevec) RETURNS bool
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION sparsevec_gt(sparsevec, sparsevec) RETURNS bool
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION sparsevec_cmp(sparsevec, sparsevec) RETURNS int4
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION sparsevec_l2_squared_distance(sparsevec, sparsevec) RETURNS float8
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION sparsevec_negative_inner_product(sparsevec, sparsevec) RETURNS float8
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION sparsevec(sparsevec, integer, boolean) RETURNS sparsevec
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION vector_to_sparsevec(vector, integer, boolean) RETURNS sparsevec
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION sparsevec_to_vector(sparsevec, integer, boolean) RETURNS vector
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION halfvec_to_sparsevec(halfvec, integer, boolean) RETURNS sparsevec
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION sparsevec_to_halfvec(sparsevec, integer, boolean) RETURNS halfvec
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE CAST (sparsevec AS sparsevec)
	WITH FUNCTION sparsevec(sparsevec, integer, boolean) AS IMPLICIT;

CREATE CAST (sparsevec AS vector)
	WITH FUNCTION sparsevec_to_vector(sparsevec, integer, boolean) AS ASSIGNMENT;

CREATE CAST (vector AS sparsevec)
	WITH FUNCTION vector_to_sparsevec(vector, integer, boolean) AS IMPLICIT;

CREATE CAST (sparsevec AS halfvec)
	WITH FUNCTION sparsevec_to_halfvec(sparsevec, integer, boolean) AS ASSIGNMENT;

CREATE CAST (halfvec AS sparsevec)
	WITH FUNCTION halfvec_to_sparsevec(halfvec, integer, boolean) AS IMPLICIT;

CREATE OPERATOR <-> (
	LEFTARG = sparsevec, RIGHTARG = sparsevec, PROCEDURE = l2_distance,
	COMMUTATOR = '<->'
);

CREATE OPERATOR <#> (
	LEFTARG = sparsevec, RIGHTARG = sparsevec, PROCEDURE = sparsevec_negative_inner_product,
	COMMUTATOR = '<#>'
);

CREATE OPERATOR <=> (
	LEFTARG = sparsevec, RIGHTARG = sparsevec, PROCEDURE = cosine_distance,
	COMMUTATOR = '<=>'
);

CREATE OPERATOR <+> (
	LEFTARG = sparsevec, RIGHTARG = sparsevec, PROCEDURE = l1_distance,
	COMMUTATOR = '<+>'
);

CREATE OPERATOR < (
	LEFTARG = sparsevec, RIGHTARG = sparsevec, PROCEDURE = sparsevec_lt,
	COMMUTATOR = > , NEGATOR = >= ,
	RESTRICT = scalarltsel, JOIN = scalarltjoinsel
);

CREATE OPERATOR <= (
	LEFTARG = sparsevec, RIGHTARG = sparsevec, PROCEDURE = sparsevec_le,
	COMMUTATOR = >= , NEGATOR = > ,
	RESTRICT = scalarlesel, JOIN = scalarlejoinsel
);

CREATE OPERATOR = (
	LEFTARG = sparsevec, RIGHTARG = sparsevec, PROCEDURE = sparsevec_eq,
	COMMUTATOR = = , NEGATOR = <> ,
	RESTRICT = eqsel, JOIN = eqjoinsel
);

CREATE OPERATOR <> (
	LEFTARG = sparsevec, RIGHTARG = sparsevec, PROCEDURE = sparsevec_ne,
	COMMUTATOR = <> , NEGATOR = = ,
	RESTRICT = eqsel, JOIN = eqjoinsel
);

CREATE OPERATOR >= (
	LEFTARG = sparsevec, RIGHTARG = sparsevec, PROCEDURE = sparsevec_ge,
	COMMUTATOR = <= , NEGATOR = < ,
	RESTRICT = scalargesel, JOIN = scalargejoinsel
);

CREATE OPERATOR > (
	LEFTARG = sparsevec, RIGHTARG = sparsevec, PROCEDURE = sparsevec_gt,
	COMMUTATOR = < , NEGATOR = <= ,
	RESTRICT = scalargtsel, JOIN = scalargtjoinsel
);

CREATE OPERATOR CLASS sparsevec_ops
	DEFAULT FOR TYPE sparsevec USING btree AS
	OPERATOR 1 < ,
	OPERATOR 2 <= ,
	OPERATOR 3 = ,
	OPERATOR 4 >= ,
	OPERATOR 5 > ,
	FUNCTION 1 sparsevec_cmp(sparsevec, sparsevec);

CREATE OPERATOR CLASS sparsevec_l2_ops
	FOR TYPE sparsevec USING hnsw AS
	OPERATOR 1 <-> (sparsevec, sparsevec) FOR ORDER BY float_ops,
	FUNCTION 1 sparsevec_l2_squared_distance(sparsevec, sparsevec),
	FUNCTION 3 hnsw_sparsevec_support(internal);

CREATE OPERATOR CLASS sparsevec_ip_ops
	FOR TYPE sparsevec USING hnsw AS
	OPERATOR 1 <#> (sparsevec, sparsevec) FOR ORDER BY float_ops,
	FUNCTION 1 sparsevec_negative_inner_product(sparsevec, sparsevec),
	FUNCTION 3 hnsw_sparsevec_support(internal);

CREATE OPERATOR CLASS sparsevec_cosine_ops
	FOR TYPE sparsevec USING hnsw AS
	OPERATOR 1 <=> (sparsevec, sparsevec) FOR ORDER BY float_ops,
	FUNCTION 1 sparsevec_negative_inner_product(sparsevec, sparsevec),
	FUNCTION 2 l2_norm(sparsevec),
	FUNCTION 3 hnsw_sparsevec_support(internal);

CREATE OPERATOR CLASS sparsevec_l1_ops
	FOR TYPE sparsevec USING hnsw AS
	OPERATOR 1 <+> (sparsevec, sparsevec) FOR ORDER BY float_ops,
	FUNCTION 1 l1_distance(sparsevec, sparsevec),
	FUNCTION 3 hnsw_sparsevec_support(internal);
```

## File: `sql/vector--0.7.0--0.7.1.sql`
```sql
-- complain if script is sourced in psql, rather than via CREATE EXTENSION
\echo Use "ALTER EXTENSION vector UPDATE TO '0.7.1'" to load this file. \quit
```

## File: `sql/vector--0.7.1--0.7.2.sql`
```sql
-- complain if script is sourced in psql, rather than via CREATE EXTENSION
\echo Use "ALTER EXTENSION vector UPDATE TO '0.7.2'" to load this file. \quit
```

## File: `sql/vector--0.7.2--0.7.3.sql`
```sql
-- complain if script is sourced in psql, rather than via CREATE EXTENSION
\echo Use "ALTER EXTENSION vector UPDATE TO '0.7.3'" to load this file. \quit
```

## File: `sql/vector--0.7.3--0.7.4.sql`
```sql
-- complain if script is sourced in psql, rather than via CREATE EXTENSION
\echo Use "ALTER EXTENSION vector UPDATE TO '0.7.4'" to load this file. \quit
```

## File: `sql/vector--0.7.4--0.8.0.sql`
```sql
-- complain if script is sourced in psql, rather than via CREATE EXTENSION
\echo Use "ALTER EXTENSION vector UPDATE TO '0.8.0'" to load this file. \quit

CREATE FUNCTION array_to_sparsevec(integer[], integer, boolean) RETURNS sparsevec
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION array_to_sparsevec(real[], integer, boolean) RETURNS sparsevec
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION array_to_sparsevec(double precision[], integer, boolean) RETURNS sparsevec
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION array_to_sparsevec(numeric[], integer, boolean) RETURNS sparsevec
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE CAST (integer[] AS sparsevec)
	WITH FUNCTION array_to_sparsevec(integer[], integer, boolean) AS ASSIGNMENT;

CREATE CAST (real[] AS sparsevec)
	WITH FUNCTION array_to_sparsevec(real[], integer, boolean) AS ASSIGNMENT;

CREATE CAST (double precision[] AS sparsevec)
	WITH FUNCTION array_to_sparsevec(double precision[], integer, boolean) AS ASSIGNMENT;

CREATE CAST (numeric[] AS sparsevec)
	WITH FUNCTION array_to_sparsevec(numeric[], integer, boolean) AS ASSIGNMENT;
```

## File: `sql/vector--0.8.0--0.8.1.sql`
```sql
-- complain if script is sourced in psql, rather than via CREATE EXTENSION
\echo Use "ALTER EXTENSION vector UPDATE TO '0.8.1'" to load this file. \quit
```

## File: `sql/vector--0.8.1--0.8.2.sql`
```sql
-- complain if script is sourced in psql, rather than via CREATE EXTENSION
\echo Use "ALTER EXTENSION vector UPDATE TO '0.8.2'" to load this file. \quit
```

## File: `sql/vector.sql`
```sql
-- complain if script is sourced in psql, rather than via CREATE EXTENSION
\echo Use "CREATE EXTENSION vector" to load this file. \quit

-- vector type

CREATE TYPE vector;

CREATE FUNCTION vector_in(cstring, oid, integer) RETURNS vector
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION vector_out(vector) RETURNS cstring
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION vector_typmod_in(cstring[]) RETURNS integer
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION vector_recv(internal, oid, integer) RETURNS vector
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION vector_send(vector) RETURNS bytea
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE TYPE vector (
	INPUT     = vector_in,
	OUTPUT    = vector_out,
	TYPMOD_IN = vector_typmod_in,
	RECEIVE   = vector_recv,
	SEND      = vector_send,
	STORAGE   = external
);

-- vector functions

CREATE FUNCTION l2_distance(vector, vector) RETURNS float8
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION inner_product(vector, vector) RETURNS float8
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION cosine_distance(vector, vector) RETURNS float8
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION l1_distance(vector, vector) RETURNS float8
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION vector_dims(vector) RETURNS integer
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION vector_norm(vector) RETURNS float8
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION l2_normalize(vector) RETURNS vector
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION binary_quantize(vector) RETURNS bit
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION subvector(vector, int, int) RETURNS vector
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

-- vector private functions

CREATE FUNCTION vector_add(vector, vector) RETURNS vector
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION vector_sub(vector, vector) RETURNS vector
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION vector_mul(vector, vector) RETURNS vector
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION vector_concat(vector, vector) RETURNS vector
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION vector_lt(vector, vector) RETURNS bool
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION vector_le(vector, vector) RETURNS bool
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION vector_eq(vector, vector) RETURNS bool
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION vector_ne(vector, vector) RETURNS bool
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION vector_ge(vector, vector) RETURNS bool
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION vector_gt(vector, vector) RETURNS bool
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION vector_cmp(vector, vector) RETURNS int4
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION vector_l2_squared_distance(vector, vector) RETURNS float8
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION vector_negative_inner_product(vector, vector) RETURNS float8
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION vector_spherical_distance(vector, vector) RETURNS float8
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION vector_accum(double precision[], vector) RETURNS double precision[]
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION vector_avg(double precision[]) RETURNS vector
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION vector_combine(double precision[], double precision[]) RETURNS double precision[]
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

-- vector aggregates

CREATE AGGREGATE avg(vector) (
	SFUNC = vector_accum,
	STYPE = double precision[],
	FINALFUNC = vector_avg,
	COMBINEFUNC = vector_combine,
	INITCOND = '{0}',
	PARALLEL = SAFE
);

CREATE AGGREGATE sum(vector) (
	SFUNC = vector_add,
	STYPE = vector,
	COMBINEFUNC = vector_add,
	PARALLEL = SAFE
);

-- vector cast functions

CREATE FUNCTION vector(vector, integer, boolean) RETURNS vector
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION array_to_vector(integer[], integer, boolean) RETURNS vector
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION array_to_vector(real[], integer, boolean) RETURNS vector
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION array_to_vector(double precision[], integer, boolean) RETURNS vector
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION array_to_vector(numeric[], integer, boolean) RETURNS vector
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION vector_to_float4(vector, integer, boolean) RETURNS real[]
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

-- vector casts

CREATE CAST (vector AS vector)
	WITH FUNCTION vector(vector, integer, boolean) AS IMPLICIT;

CREATE CAST (vector AS real[])
	WITH FUNCTION vector_to_float4(vector, integer, boolean) AS IMPLICIT;

CREATE CAST (integer[] AS vector)
	WITH FUNCTION array_to_vector(integer[], integer, boolean) AS ASSIGNMENT;

CREATE CAST (real[] AS vector)
	WITH FUNCTION array_to_vector(real[], integer, boolean) AS ASSIGNMENT;

CREATE CAST (double precision[] AS vector)
	WITH FUNCTION array_to_vector(double precision[], integer, boolean) AS ASSIGNMENT;

CREATE CAST (numeric[] AS vector)
	WITH FUNCTION array_to_vector(numeric[], integer, boolean) AS ASSIGNMENT;

-- vector operators

CREATE OPERATOR <-> (
	LEFTARG = vector, RIGHTARG = vector, PROCEDURE = l2_distance,
	COMMUTATOR = '<->'
);

CREATE OPERATOR <#> (
	LEFTARG = vector, RIGHTARG = vector, PROCEDURE = vector_negative_inner_product,
	COMMUTATOR = '<#>'
);

CREATE OPERATOR <=> (
	LEFTARG = vector, RIGHTARG = vector, PROCEDURE = cosine_distance,
	COMMUTATOR = '<=>'
);

CREATE OPERATOR <+> (
	LEFTARG = vector, RIGHTARG = vector, PROCEDURE = l1_distance,
	COMMUTATOR = '<+>'
);

CREATE OPERATOR + (
	LEFTARG = vector, RIGHTARG = vector, PROCEDURE = vector_add,
	COMMUTATOR = +
);

CREATE OPERATOR - (
	LEFTARG = vector, RIGHTARG = vector, PROCEDURE = vector_sub
);

CREATE OPERATOR * (
	LEFTARG = vector, RIGHTARG = vector, PROCEDURE = vector_mul,
	COMMUTATOR = *
);

CREATE OPERATOR || (
	LEFTARG = vector, RIGHTARG = vector, PROCEDURE = vector_concat
);

CREATE OPERATOR < (
	LEFTARG = vector, RIGHTARG = vector, PROCEDURE = vector_lt,
	COMMUTATOR = > , NEGATOR = >= ,
	RESTRICT = scalarltsel, JOIN = scalarltjoinsel
);

CREATE OPERATOR <= (
	LEFTARG = vector, RIGHTARG = vector, PROCEDURE = vector_le,
	COMMUTATOR = >= , NEGATOR = > ,
	RESTRICT = scalarlesel, JOIN = scalarlejoinsel
);

CREATE OPERATOR = (
	LEFTARG = vector, RIGHTARG = vector, PROCEDURE = vector_eq,
	COMMUTATOR = = , NEGATOR = <> ,
	RESTRICT = eqsel, JOIN = eqjoinsel
);

CREATE OPERATOR <> (
	LEFTARG = vector, RIGHTARG = vector, PROCEDURE = vector_ne,
	COMMUTATOR = <> , NEGATOR = = ,
	RESTRICT = eqsel, JOIN = eqjoinsel
);

CREATE OPERATOR >= (
	LEFTARG = vector, RIGHTARG = vector, PROCEDURE = vector_ge,
	COMMUTATOR = <= , NEGATOR = < ,
	RESTRICT = scalargesel, JOIN = scalargejoinsel
);

CREATE OPERATOR > (
	LEFTARG = vector, RIGHTARG = vector, PROCEDURE = vector_gt,
	COMMUTATOR = < , NEGATOR = <= ,
	RESTRICT = scalargtsel, JOIN = scalargtjoinsel
);

-- access methods

CREATE FUNCTION ivfflathandler(internal) RETURNS index_am_handler
	AS 'MODULE_PATHNAME' LANGUAGE C;

CREATE ACCESS METHOD ivfflat TYPE INDEX HANDLER ivfflathandler;

COMMENT ON ACCESS METHOD ivfflat IS 'ivfflat index access method';

CREATE FUNCTION hnswhandler(internal) RETURNS index_am_handler
	AS 'MODULE_PATHNAME' LANGUAGE C;

CREATE ACCESS METHOD hnsw TYPE INDEX HANDLER hnswhandler;

COMMENT ON ACCESS METHOD hnsw IS 'hnsw index access method';

-- access method private functions

CREATE FUNCTION ivfflat_halfvec_support(internal) RETURNS internal
	AS 'MODULE_PATHNAME' LANGUAGE C;

CREATE FUNCTION ivfflat_bit_support(internal) RETURNS internal
	AS 'MODULE_PATHNAME' LANGUAGE C;

CREATE FUNCTION hnsw_halfvec_support(internal) RETURNS internal
	AS 'MODULE_PATHNAME' LANGUAGE C;

CREATE FUNCTION hnsw_bit_support(internal) RETURNS internal
	AS 'MODULE_PATHNAME' LANGUAGE C;

CREATE FUNCTION hnsw_sparsevec_support(internal) RETURNS internal
	AS 'MODULE_PATHNAME' LANGUAGE C;

-- vector opclasses

CREATE OPERATOR CLASS vector_ops
	DEFAULT FOR TYPE vector USING btree AS
	OPERATOR 1 < ,
	OPERATOR 2 <= ,
	OPERATOR 3 = ,
	OPERATOR 4 >= ,
	OPERATOR 5 > ,
	FUNCTION 1 vector_cmp(vector, vector);

CREATE OPERATOR CLASS vector_l2_ops
	DEFAULT FOR TYPE vector USING ivfflat AS
	OPERATOR 1 <-> (vector, vector) FOR ORDER BY float_ops,
	FUNCTION 1 vector_l2_squared_distance(vector, vector),
	FUNCTION 3 l2_distance(vector, vector);

CREATE OPERATOR CLASS vector_ip_ops
	FOR TYPE vector USING ivfflat AS
	OPERATOR 1 <#> (vector, vector) FOR ORDER BY float_ops,
	FUNCTION 1 vector_negative_inner_product(vector, vector),
	FUNCTION 3 vector_spherical_distance(vector, vector),
	FUNCTION 4 vector_norm(vector);

CREATE OPERATOR CLASS vector_cosine_ops
	FOR TYPE vector USING ivfflat AS
	OPERATOR 1 <=> (vector, vector) FOR ORDER BY float_ops,
	FUNCTION 1 vector_negative_inner_product(vector, vector),
	FUNCTION 2 vector_norm(vector),
	FUNCTION 3 vector_spherical_distance(vector, vector),
	FUNCTION 4 vector_norm(vector);

CREATE OPERATOR CLASS vector_l2_ops
	FOR TYPE vector USING hnsw AS
	OPERATOR 1 <-> (vector, vector) FOR ORDER BY float_ops,
	FUNCTION 1 vector_l2_squared_distance(vector, vector);

CREATE OPERATOR CLASS vector_ip_ops
	FOR TYPE vector USING hnsw AS
	OPERATOR 1 <#> (vector, vector) FOR ORDER BY float_ops,
	FUNCTION 1 vector_negative_inner_product(vector, vector);

CREATE OPERATOR CLASS vector_cosine_ops
	FOR TYPE vector USING hnsw AS
	OPERATOR 1 <=> (vector, vector) FOR ORDER BY float_ops,
	FUNCTION 1 vector_negative_inner_product(vector, vector),
	FUNCTION 2 vector_norm(vector);

CREATE OPERATOR CLASS vector_l1_ops
	FOR TYPE vector USING hnsw AS
	OPERATOR 1 <+> (vector, vector) FOR ORDER BY float_ops,
	FUNCTION 1 l1_distance(vector, vector);

-- halfvec type

CREATE TYPE halfvec;

CREATE FUNCTION halfvec_in(cstring, oid, integer) RETURNS halfvec
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION halfvec_out(halfvec) RETURNS cstring
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION halfvec_typmod_in(cstring[]) RETURNS integer
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION halfvec_recv(internal, oid, integer) RETURNS halfvec
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION halfvec_send(halfvec) RETURNS bytea
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE TYPE halfvec (
	INPUT     = halfvec_in,
	OUTPUT    = halfvec_out,
	TYPMOD_IN = halfvec_typmod_in,
	RECEIVE   = halfvec_recv,
	SEND      = halfvec_send,
	STORAGE   = external
);

-- halfvec functions

CREATE FUNCTION l2_distance(halfvec, halfvec) RETURNS float8
	AS 'MODULE_PATHNAME', 'halfvec_l2_distance' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION inner_product(halfvec, halfvec) RETURNS float8
	AS 'MODULE_PATHNAME', 'halfvec_inner_product' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION cosine_distance(halfvec, halfvec) RETURNS float8
	AS 'MODULE_PATHNAME', 'halfvec_cosine_distance' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION l1_distance(halfvec, halfvec) RETURNS float8
	AS 'MODULE_PATHNAME', 'halfvec_l1_distance' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION vector_dims(halfvec) RETURNS integer
	AS 'MODULE_PATHNAME', 'halfvec_vector_dims' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION l2_norm(halfvec) RETURNS float8
	AS 'MODULE_PATHNAME', 'halfvec_l2_norm' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION l2_normalize(halfvec) RETURNS halfvec
	AS 'MODULE_PATHNAME', 'halfvec_l2_normalize' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION binary_quantize(halfvec) RETURNS bit
	AS 'MODULE_PATHNAME', 'halfvec_binary_quantize' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION subvector(halfvec, int, int) RETURNS halfvec
	AS 'MODULE_PATHNAME', 'halfvec_subvector' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

-- halfvec private functions

CREATE FUNCTION halfvec_add(halfvec, halfvec) RETURNS halfvec
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION halfvec_sub(halfvec, halfvec) RETURNS halfvec
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION halfvec_mul(halfvec, halfvec) RETURNS halfvec
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION halfvec_concat(halfvec, halfvec) RETURNS halfvec
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION halfvec_lt(halfvec, halfvec) RETURNS bool
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION halfvec_le(halfvec, halfvec) RETURNS bool
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION halfvec_eq(halfvec, halfvec) RETURNS bool
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION halfvec_ne(halfvec, halfvec) RETURNS bool
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION halfvec_ge(halfvec, halfvec) RETURNS bool
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION halfvec_gt(halfvec, halfvec) RETURNS bool
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION halfvec_cmp(halfvec, halfvec) RETURNS int4
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION halfvec_l2_squared_distance(halfvec, halfvec) RETURNS float8
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION halfvec_negative_inner_product(halfvec, halfvec) RETURNS float8
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION halfvec_spherical_distance(halfvec, halfvec) RETURNS float8
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION halfvec_accum(double precision[], halfvec) RETURNS double precision[]
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION halfvec_avg(double precision[]) RETURNS halfvec
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION halfvec_combine(double precision[], double precision[]) RETURNS double precision[]
	AS 'MODULE_PATHNAME', 'vector_combine' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

-- halfvec aggregates

CREATE AGGREGATE avg(halfvec) (
	SFUNC = halfvec_accum,
	STYPE = double precision[],
	FINALFUNC = halfvec_avg,
	COMBINEFUNC = halfvec_combine,
	INITCOND = '{0}',
	PARALLEL = SAFE
);

CREATE AGGREGATE sum(halfvec) (
	SFUNC = halfvec_add,
	STYPE = halfvec,
	COMBINEFUNC = halfvec_add,
	PARALLEL = SAFE
);

-- halfvec cast functions

CREATE FUNCTION halfvec(halfvec, integer, boolean) RETURNS halfvec
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION halfvec_to_vector(halfvec, integer, boolean) RETURNS vector
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION vector_to_halfvec(vector, integer, boolean) RETURNS halfvec
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION array_to_halfvec(integer[], integer, boolean) RETURNS halfvec
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION array_to_halfvec(real[], integer, boolean) RETURNS halfvec
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION array_to_halfvec(double precision[], integer, boolean) RETURNS halfvec
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION array_to_halfvec(numeric[], integer, boolean) RETURNS halfvec
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION halfvec_to_float4(halfvec, integer, boolean) RETURNS real[]
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

-- halfvec casts

CREATE CAST (halfvec AS halfvec)
	WITH FUNCTION halfvec(halfvec, integer, boolean) AS IMPLICIT;

CREATE CAST (halfvec AS vector)
	WITH FUNCTION halfvec_to_vector(halfvec, integer, boolean) AS ASSIGNMENT;

CREATE CAST (vector AS halfvec)
	WITH FUNCTION vector_to_halfvec(vector, integer, boolean) AS IMPLICIT;

CREATE CAST (halfvec AS real[])
	WITH FUNCTION halfvec_to_float4(halfvec, integer, boolean) AS ASSIGNMENT;

CREATE CAST (integer[] AS halfvec)
	WITH FUNCTION array_to_halfvec(integer[], integer, boolean) AS ASSIGNMENT;

CREATE CAST (real[] AS halfvec)
	WITH FUNCTION array_to_halfvec(real[], integer, boolean) AS ASSIGNMENT;

CREATE CAST (double precision[] AS halfvec)
	WITH FUNCTION array_to_halfvec(double precision[], integer, boolean) AS ASSIGNMENT;

CREATE CAST (numeric[] AS halfvec)
	WITH FUNCTION array_to_halfvec(numeric[], integer, boolean) AS ASSIGNMENT;

-- halfvec operators

CREATE OPERATOR <-> (
	LEFTARG = halfvec, RIGHTARG = halfvec, PROCEDURE = l2_distance,
	COMMUTATOR = '<->'
);

CREATE OPERATOR <#> (
	LEFTARG = halfvec, RIGHTARG = halfvec, PROCEDURE = halfvec_negative_inner_product,
	COMMUTATOR = '<#>'
);

CREATE OPERATOR <=> (
	LEFTARG = halfvec, RIGHTARG = halfvec, PROCEDURE = cosine_distance,
	COMMUTATOR = '<=>'
);

CREATE OPERATOR <+> (
	LEFTARG = halfvec, RIGHTARG = halfvec, PROCEDURE = l1_distance,
	COMMUTATOR = '<+>'
);

CREATE OPERATOR + (
	LEFTARG = halfvec, RIGHTARG = halfvec, PROCEDURE = halfvec_add,
	COMMUTATOR = +
);

CREATE OPERATOR - (
	LEFTARG = halfvec, RIGHTARG = halfvec, PROCEDURE = halfvec_sub
);

CREATE OPERATOR * (
	LEFTARG = halfvec, RIGHTARG = halfvec, PROCEDURE = halfvec_mul,
	COMMUTATOR = *
);

CREATE OPERATOR || (
	LEFTARG = halfvec, RIGHTARG = halfvec, PROCEDURE = halfvec_concat
);

CREATE OPERATOR < (
	LEFTARG = halfvec, RIGHTARG = halfvec, PROCEDURE = halfvec_lt,
	COMMUTATOR = > , NEGATOR = >= ,
	RESTRICT = scalarltsel, JOIN = scalarltjoinsel
);

CREATE OPERATOR <= (
	LEFTARG = halfvec, RIGHTARG = halfvec, PROCEDURE = halfvec_le,
	COMMUTATOR = >= , NEGATOR = > ,
	RESTRICT = scalarlesel, JOIN = scalarlejoinsel
);

CREATE OPERATOR = (
	LEFTARG = halfvec, RIGHTARG = halfvec, PROCEDURE = halfvec_eq,
	COMMUTATOR = = , NEGATOR = <> ,
	RESTRICT = eqsel, JOIN = eqjoinsel
);

CREATE OPERATOR <> (
	LEFTARG = halfvec, RIGHTARG = halfvec, PROCEDURE = halfvec_ne,
	COMMUTATOR = <> , NEGATOR = = ,
	RESTRICT = eqsel, JOIN = eqjoinsel
);

CREATE OPERATOR >= (
	LEFTARG = halfvec, RIGHTARG = halfvec, PROCEDURE = halfvec_ge,
	COMMUTATOR = <= , NEGATOR = < ,
	RESTRICT = scalargesel, JOIN = scalargejoinsel
);

CREATE OPERATOR > (
	LEFTARG = halfvec, RIGHTARG = halfvec, PROCEDURE = halfvec_gt,
	COMMUTATOR = < , NEGATOR = <= ,
	RESTRICT = scalargtsel, JOIN = scalargtjoinsel
);

-- halfvec opclasses

CREATE OPERATOR CLASS halfvec_ops
	DEFAULT FOR TYPE halfvec USING btree AS
	OPERATOR 1 < ,
	OPERATOR 2 <= ,
	OPERATOR 3 = ,
	OPERATOR 4 >= ,
	OPERATOR 5 > ,
	FUNCTION 1 halfvec_cmp(halfvec, halfvec);

CREATE OPERATOR CLASS halfvec_l2_ops
	FOR TYPE halfvec USING ivfflat AS
	OPERATOR 1 <-> (halfvec, halfvec) FOR ORDER BY float_ops,
	FUNCTION 1 halfvec_l2_squared_distance(halfvec, halfvec),
	FUNCTION 3 l2_distance(halfvec, halfvec),
	FUNCTION 5 ivfflat_halfvec_support(internal);

CREATE OPERATOR CLASS halfvec_ip_ops
	FOR TYPE halfvec USING ivfflat AS
	OPERATOR 1 <#> (halfvec, halfvec) FOR ORDER BY float_ops,
	FUNCTION 1 halfvec_negative_inner_product(halfvec, halfvec),
	FUNCTION 3 halfvec_spherical_distance(halfvec, halfvec),
	FUNCTION 4 l2_norm(halfvec),
	FUNCTION 5 ivfflat_halfvec_support(internal);

CREATE OPERATOR CLASS halfvec_cosine_ops
	FOR TYPE halfvec USING ivfflat AS
	OPERATOR 1 <=> (halfvec, halfvec) FOR ORDER BY float_ops,
	FUNCTION 1 halfvec_negative_inner_product(halfvec, halfvec),
	FUNCTION 2 l2_norm(halfvec),
	FUNCTION 3 halfvec_spherical_distance(halfvec, halfvec),
	FUNCTION 4 l2_norm(halfvec),
	FUNCTION 5 ivfflat_halfvec_support(internal);

CREATE OPERATOR CLASS halfvec_l2_ops
	FOR TYPE halfvec USING hnsw AS
	OPERATOR 1 <-> (halfvec, halfvec) FOR ORDER BY float_ops,
	FUNCTION 1 halfvec_l2_squared_distance(halfvec, halfvec),
	FUNCTION 3 hnsw_halfvec_support(internal);

CREATE OPERATOR CLASS halfvec_ip_ops
	FOR TYPE halfvec USING hnsw AS
	OPERATOR 1 <#> (halfvec, halfvec) FOR ORDER BY float_ops,
	FUNCTION 1 halfvec_negative_inner_product(halfvec, halfvec),
	FUNCTION 3 hnsw_halfvec_support(internal);

CREATE OPERATOR CLASS halfvec_cosine_ops
	FOR TYPE halfvec USING hnsw AS
	OPERATOR 1 <=> (halfvec, halfvec) FOR ORDER BY float_ops,
	FUNCTION 1 halfvec_negative_inner_product(halfvec, halfvec),
	FUNCTION 2 l2_norm(halfvec),
	FUNCTION 3 hnsw_halfvec_support(internal);

CREATE OPERATOR CLASS halfvec_l1_ops
	FOR TYPE halfvec USING hnsw AS
	OPERATOR 1 <+> (halfvec, halfvec) FOR ORDER BY float_ops,
	FUNCTION 1 l1_distance(halfvec, halfvec),
	FUNCTION 3 hnsw_halfvec_support(internal);

-- bit functions

CREATE FUNCTION hamming_distance(bit, bit) RETURNS float8
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION jaccard_distance(bit, bit) RETURNS float8
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

-- bit operators

CREATE OPERATOR <~> (
	LEFTARG = bit, RIGHTARG = bit, PROCEDURE = hamming_distance,
	COMMUTATOR = '<~>'
);

CREATE OPERATOR <%> (
	LEFTARG = bit, RIGHTARG = bit, PROCEDURE = jaccard_distance,
	COMMUTATOR = '<%>'
);

-- bit opclasses

CREATE OPERATOR CLASS bit_hamming_ops
	FOR TYPE bit USING ivfflat AS
	OPERATOR 1 <~> (bit, bit) FOR ORDER BY float_ops,
	FUNCTION 1 hamming_distance(bit, bit),
	FUNCTION 3 hamming_distance(bit, bit),
	FUNCTION 5 ivfflat_bit_support(internal);

CREATE OPERATOR CLASS bit_hamming_ops
	FOR TYPE bit USING hnsw AS
	OPERATOR 1 <~> (bit, bit) FOR ORDER BY float_ops,
	FUNCTION 1 hamming_distance(bit, bit),
	FUNCTION 3 hnsw_bit_support(internal);

CREATE OPERATOR CLASS bit_jaccard_ops
	FOR TYPE bit USING hnsw AS
	OPERATOR 1 <%> (bit, bit) FOR ORDER BY float_ops,
	FUNCTION 1 jaccard_distance(bit, bit),
	FUNCTION 3 hnsw_bit_support(internal);

--- sparsevec type

CREATE TYPE sparsevec;

CREATE FUNCTION sparsevec_in(cstring, oid, integer) RETURNS sparsevec
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION sparsevec_out(sparsevec) RETURNS cstring
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION sparsevec_typmod_in(cstring[]) RETURNS integer
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION sparsevec_recv(internal, oid, integer) RETURNS sparsevec
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION sparsevec_send(sparsevec) RETURNS bytea
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE TYPE sparsevec (
	INPUT     = sparsevec_in,
	OUTPUT    = sparsevec_out,
	TYPMOD_IN = sparsevec_typmod_in,
	RECEIVE   = sparsevec_recv,
	SEND      = sparsevec_send,
	STORAGE   = external
);

-- sparsevec functions

CREATE FUNCTION l2_distance(sparsevec, sparsevec) RETURNS float8
	AS 'MODULE_PATHNAME', 'sparsevec_l2_distance' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION inner_product(sparsevec, sparsevec) RETURNS float8
	AS 'MODULE_PATHNAME', 'sparsevec_inner_product' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION cosine_distance(sparsevec, sparsevec) RETURNS float8
	AS 'MODULE_PATHNAME', 'sparsevec_cosine_distance' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION l1_distance(sparsevec, sparsevec) RETURNS float8
	AS 'MODULE_PATHNAME', 'sparsevec_l1_distance' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION l2_norm(sparsevec) RETURNS float8
	AS 'MODULE_PATHNAME', 'sparsevec_l2_norm' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION l2_normalize(sparsevec) RETURNS sparsevec
	AS 'MODULE_PATHNAME', 'sparsevec_l2_normalize' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

-- sparsevec private functions

CREATE FUNCTION sparsevec_lt(sparsevec, sparsevec) RETURNS bool
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION sparsevec_le(sparsevec, sparsevec) RETURNS bool
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION sparsevec_eq(sparsevec, sparsevec) RETURNS bool
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION sparsevec_ne(sparsevec, sparsevec) RETURNS bool
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION sparsevec_ge(sparsevec, sparsevec) RETURNS bool
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION sparsevec_gt(sparsevec, sparsevec) RETURNS bool
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION sparsevec_cmp(sparsevec, sparsevec) RETURNS int4
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION sparsevec_l2_squared_distance(sparsevec, sparsevec) RETURNS float8
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION sparsevec_negative_inner_product(sparsevec, sparsevec) RETURNS float8
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

-- sparsevec cast functions

CREATE FUNCTION sparsevec(sparsevec, integer, boolean) RETURNS sparsevec
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION vector_to_sparsevec(vector, integer, boolean) RETURNS sparsevec
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION sparsevec_to_vector(sparsevec, integer, boolean) RETURNS vector
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION halfvec_to_sparsevec(halfvec, integer, boolean) RETURNS sparsevec
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION sparsevec_to_halfvec(sparsevec, integer, boolean) RETURNS halfvec
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION array_to_sparsevec(integer[], integer, boolean) RETURNS sparsevec
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION array_to_sparsevec(real[], integer, boolean) RETURNS sparsevec
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION array_to_sparsevec(double precision[], integer, boolean) RETURNS sparsevec
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

CREATE FUNCTION array_to_sparsevec(numeric[], integer, boolean) RETURNS sparsevec
	AS 'MODULE_PATHNAME' LANGUAGE C IMMUTABLE STRICT PARALLEL SAFE;

-- sparsevec casts

CREATE CAST (sparsevec AS sparsevec)
	WITH FUNCTION sparsevec(sparsevec, integer, boolean) AS IMPLICIT;

CREATE CAST (sparsevec AS vector)
	WITH FUNCTION sparsevec_to_vector(sparsevec, integer, boolean) AS ASSIGNMENT;

CREATE CAST (vector AS sparsevec)
	WITH FUNCTION vector_to_sparsevec(vector, integer, boolean) AS IMPLICIT;

CREATE CAST (sparsevec AS halfvec)
	WITH FUNCTION sparsevec_to_halfvec(sparsevec, integer, boolean) AS ASSIGNMENT;

CREATE CAST (halfvec AS sparsevec)
	WITH FUNCTION halfvec_to_sparsevec(halfvec, integer, boolean) AS IMPLICIT;

CREATE CAST (integer[] AS sparsevec)
	WITH FUNCTION array_to_sparsevec(integer[], integer, boolean) AS ASSIGNMENT;

CREATE CAST (real[] AS sparsevec)
	WITH FUNCTION array_to_sparsevec(real[], integer, boolean) AS ASSIGNMENT;

CREATE CAST (double precision[] AS sparsevec)
	WITH FUNCTION array_to_sparsevec(double precision[], integer, boolean) AS ASSIGNMENT;

CREATE CAST (numeric[] AS sparsevec)
	WITH FUNCTION array_to_sparsevec(numeric[], integer, boolean) AS ASSIGNMENT;

-- sparsevec operators

CREATE OPERATOR <-> (
	LEFTARG = sparsevec, RIGHTARG = sparsevec, PROCEDURE = l2_distance,
	COMMUTATOR = '<->'
);

CREATE OPERATOR <#> (
	LEFTARG = sparsevec, RIGHTARG = sparsevec, PROCEDURE = sparsevec_negative_inner_product,
	COMMUTATOR = '<#>'
);

CREATE OPERATOR <=> (
	LEFTARG = sparsevec, RIGHTARG = sparsevec, PROCEDURE = cosine_distance,
	COMMUTATOR = '<=>'
);

CREATE OPERATOR <+> (
	LEFTARG = sparsevec, RIGHTARG = sparsevec, PROCEDURE = l1_distance,
	COMMUTATOR = '<+>'
);

CREATE OPERATOR < (
	LEFTARG = sparsevec, RIGHTARG = sparsevec, PROCEDURE = sparsevec_lt,
	COMMUTATOR = > , NEGATOR = >= ,
	RESTRICT = scalarltsel, JOIN = scalarltjoinsel
);

CREATE OPERATOR <= (
	LEFTARG = sparsevec, RIGHTARG = sparsevec, PROCEDURE = sparsevec_le,
	COMMUTATOR = >= , NEGATOR = > ,
	RESTRICT = scalarlesel, JOIN = scalarlejoinsel
);

CREATE OPERATOR = (
	LEFTARG = sparsevec, RIGHTARG = sparsevec, PROCEDURE = sparsevec_eq,
	COMMUTATOR = = , NEGATOR = <> ,
	RESTRICT = eqsel, JOIN = eqjoinsel
);

CREATE OPERATOR <> (
	LEFTARG = sparsevec, RIGHTARG = sparsevec, PROCEDURE = sparsevec_ne,
	COMMUTATOR = <> , NEGATOR = = ,
	RESTRICT = eqsel, JOIN = eqjoinsel
);

CREATE OPERATOR >= (
	LEFTARG = sparsevec, RIGHTARG = sparsevec, PROCEDURE = sparsevec_ge,
	COMMUTATOR = <= , NEGATOR = < ,
	RESTRICT = scalargesel, JOIN = scalargejoinsel
);

CREATE OPERATOR > (
	LEFTARG = sparsevec, RIGHTARG = sparsevec, PROCEDURE = sparsevec_gt,
	COMMUTATOR = < , NEGATOR = <= ,
	RESTRICT = scalargtsel, JOIN = scalargtjoinsel
);

-- sparsevec opclasses

CREATE OPERATOR CLASS sparsevec_ops
	DEFAULT FOR TYPE sparsevec USING btree AS
	OPERATOR 1 < ,
	OPERATOR 2 <= ,
	OPERATOR 3 = ,
	OPERATOR 4 >= ,
	OPERATOR 5 > ,
	FUNCTION 1 sparsevec_cmp(sparsevec, sparsevec);

CREATE OPERATOR CLASS sparsevec_l2_ops
	FOR TYPE sparsevec USING hnsw AS
	OPERATOR 1 <-> (sparsevec, sparsevec) FOR ORDER BY float_ops,
	FUNCTION 1 sparsevec_l2_squared_distance(sparsevec, sparsevec),
	FUNCTION 3 hnsw_sparsevec_support(internal);

CREATE OPERATOR CLASS sparsevec_ip_ops
	FOR TYPE sparsevec USING hnsw AS
	OPERATOR 1 <#> (sparsevec, sparsevec) FOR ORDER BY float_ops,
	FUNCTION 1 sparsevec_negative_inner_product(sparsevec, sparsevec),
	FUNCTION 3 hnsw_sparsevec_support(internal);

CREATE OPERATOR CLASS sparsevec_cosine_ops
	FOR TYPE sparsevec USING hnsw AS
	OPERATOR 1 <=> (sparsevec, sparsevec) FOR ORDER BY float_ops,
	FUNCTION 1 sparsevec_negative_inner_product(sparsevec, sparsevec),
	FUNCTION 2 l2_norm(sparsevec),
	FUNCTION 3 hnsw_sparsevec_support(internal);

CREATE OPERATOR CLASS sparsevec_l1_ops
	FOR TYPE sparsevec USING hnsw AS
	OPERATOR 1 <+> (sparsevec, sparsevec) FOR ORDER BY float_ops,
	FUNCTION 1 l1_distance(sparsevec, sparsevec),
	FUNCTION 3 hnsw_sparsevec_support(internal);
```

## File: `src/bitutils.c`
```c
#include "postgres.h"

#include "bitutils.h"
#include "halfvec.h"			/* for USE_DISPATCH and USE_TARGET_CLONES */
#include "port/pg_bitutils.h"

#if defined(USE_DISPATCH)
#define BIT_DISPATCH
#endif

#ifdef BIT_DISPATCH
#include <immintrin.h>

#if defined(USE__GET_CPUID)
#include <cpuid.h>
#else
#include <intrin.h>
#endif

#ifdef _MSC_VER
#define TARGET_AVX512_POPCOUNT
#else
#define TARGET_AVX512_POPCOUNT __attribute__((target("avx512f,avx512vpopcntdq")))
#endif
#endif

/* Disable for LLVM due to crash with bitcode generation */
#if defined(USE_TARGET_CLONES) && !defined(__POPCNT__) && !defined(__llvm__)
#define BIT_TARGET_CLONES __attribute__((target_clones("default", "popcnt")))
#else
#define BIT_TARGET_CLONES
#endif

/* Use built-ins when possible for inlining */
#if defined(HAVE__BUILTIN_POPCOUNT) && defined(HAVE_LONG_INT_64)
#define popcount64(x) __builtin_popcountl(x)
#elif defined(HAVE__BUILTIN_POPCOUNT) && defined(HAVE_LONG_LONG_INT_64)
#define popcount64(x) __builtin_popcountll(x)
#elif !defined(_MSC_VER)
/* Fails to resolve with MSVC */
#define popcount64(x) pg_popcount64(x)
#endif

uint64		(*BitHammingDistance) (uint32 bytes, unsigned char *ax, unsigned char *bx, uint64 distance);
double		(*BitJaccardDistance) (uint32 bytes, unsigned char *ax, unsigned char *bx, uint64 ab, uint64 aa, uint64 bb);

BIT_TARGET_CLONES static uint64
BitHammingDistanceDefault(uint32 bytes, unsigned char *ax, unsigned char *bx, uint64 distance)
{
#ifdef popcount64
	for (; bytes >= sizeof(uint64); bytes -= sizeof(uint64))
	{
		uint64		axs;
		uint64		bxs;

		/* Ensure aligned */
		memcpy(&axs, ax, sizeof(uint64));
		memcpy(&bxs, bx, sizeof(uint64));

		distance += popcount64(axs ^ bxs);

		ax += sizeof(uint64);
		bx += sizeof(uint64);
	}
#endif

	for (uint32 i = 0; i < bytes; i++)
		distance += pg_number_of_ones[ax[i] ^ bx[i]];

	return distance;
}

#ifdef BIT_DISPATCH
TARGET_AVX512_POPCOUNT static uint64
BitHammingDistanceAvx512Popcount(uint32 bytes, unsigned char *ax, unsigned char *bx, uint64 distance)
{
	__m512i		dist = _mm512_setzero_si512();

	for (; bytes >= sizeof(__m512i); bytes -= sizeof(__m512i))
	{
		__m512i		axs = _mm512_loadu_si512((const __m512i *) ax);
		__m512i		bxs = _mm512_loadu_si512((const __m512i *) bx);

		dist = _mm512_add_epi64(dist, _mm512_popcnt_epi64(_mm512_xor_si512(axs, bxs)));

		ax += sizeof(__m512i);
		bx += sizeof(__m512i);
	}

	distance += _mm512_reduce_add_epi64(dist);

	return BitHammingDistanceDefault(bytes, ax, bx, distance);
}
#endif

BIT_TARGET_CLONES static double
BitJaccardDistanceDefault(uint32 bytes, unsigned char *ax, unsigned char *bx, uint64 ab, uint64 aa, uint64 bb)
{
#ifdef popcount64
	for (; bytes >= sizeof(uint64); bytes -= sizeof(uint64))
	{
		uint64		axs;
		uint64		bxs;

		/* Ensure aligned */
		memcpy(&axs, ax, sizeof(uint64));
		memcpy(&bxs, bx, sizeof(uint64));

		ab += popcount64(axs & bxs);
		aa += popcount64(axs);
		bb += popcount64(bxs);

		ax += sizeof(uint64);
		bx += sizeof(uint64);
	}
#endif

	for (uint32 i = 0; i < bytes; i++)
	{
		ab += pg_number_of_ones[ax[i] & bx[i]];
		aa += pg_number_of_ones[ax[i]];
		bb += pg_number_of_ones[bx[i]];
	}

	if (ab == 0)
		return 1;
	else
		return 1 - (ab / ((double) (aa + bb - ab)));
}

#ifdef BIT_DISPATCH
TARGET_AVX512_POPCOUNT static double
BitJaccardDistanceAvx512Popcount(uint32 bytes, unsigned char *ax, unsigned char *bx, uint64 ab, uint64 aa, uint64 bb)
{
	__m512i		abx = _mm512_setzero_si512();
	__m512i		aax = _mm512_setzero_si512();
	__m512i		bbx = _mm512_setzero_si512();

	for (; bytes >= sizeof(__m512i); bytes -= sizeof(__m512i))
	{
		__m512i		axs = _mm512_loadu_si512((const __m512i *) ax);
		__m512i		bxs = _mm512_loadu_si512((const __m512i *) bx);

		abx = _mm512_add_epi64(abx, _mm512_popcnt_epi64(_mm512_and_si512(axs, bxs)));
		aax = _mm512_add_epi64(aax, _mm512_popcnt_epi64(axs));
		bbx = _mm512_add_epi64(bbx, _mm512_popcnt_epi64(bxs));

		ax += sizeof(__m512i);
		bx += sizeof(__m512i);
	}

	ab += _mm512_reduce_add_epi64(abx);
	aa += _mm512_reduce_add_epi64(aax);
	bb += _mm512_reduce_add_epi64(bbx);

	return BitJaccardDistanceDefault(bytes, ax, bx, ab, aa, bb);
}
#endif

#ifdef BIT_DISPATCH
#define CPU_FEATURE_OSXSAVE         (1 << 27)	/* F1 ECX */
#define CPU_FEATURE_AVX512F         (1 << 16)	/* F7,0 EBX */
#define CPU_FEATURE_AVX512VPOPCNTDQ (1 << 14)	/* F7,0 ECX */

#ifdef _MSC_VER
#define TARGET_XSAVE
#else
#define TARGET_XSAVE __attribute__((target("xsave")))
#endif

TARGET_XSAVE static bool
SupportsAvx512Popcount()
{
	unsigned int exx[4] = {0, 0, 0, 0};

#if defined(USE__GET_CPUID)
	__get_cpuid(1, &exx[0], &exx[1], &exx[2], &exx[3]);
#else
	__cpuid(exx, 1);
#endif

	/* Check OS supports XSAVE */
	if ((exx[2] & CPU_FEATURE_OSXSAVE) != CPU_FEATURE_OSXSAVE)
		return false;

	/* Check XMM, YMM, and ZMM registers are enabled */
	if ((_xgetbv(0) & 0xe6) != 0xe6)
		return false;

#if defined(USE__GET_CPUID)
	__get_cpuid_count(7, 0, &exx[0], &exx[1], &exx[2], &exx[3]);
#else
	__cpuidex(exx, 7, 0);
#endif

	/* Check AVX512F */
	if ((exx[1] & CPU_FEATURE_AVX512F) != CPU_FEATURE_AVX512F)
		return false;

	/* Check AVX512VPOPCNTDQ */
	return (exx[2] & CPU_FEATURE_AVX512VPOPCNTDQ) == CPU_FEATURE_AVX512VPOPCNTDQ;
}
#endif

void
BitvecInit(void)
{
	/*
	 * Could skip pointer when single function, but no difference in
	 * performance
	 */
	BitHammingDistance = BitHammingDistanceDefault;
	BitJaccardDistance = BitJaccardDistanceDefault;

#ifdef BIT_DISPATCH
	if (SupportsAvx512Popcount())
	{
		BitHammingDistance = BitHammingDistanceAvx512Popcount;
		BitJaccardDistance = BitJaccardDistanceAvx512Popcount;
	}
#endif
}
```

## File: `src/bitutils.h`
```c
#ifndef BITUTILS_H
#define BITUTILS_H

#include "postgres.h"

/* Check version in first header */
#if PG_VERSION_NUM < 130000
#error "Requires PostgreSQL 13+"
#endif

extern uint64 (*BitHammingDistance) (uint32 bytes, unsigned char *ax, unsigned char *bx, uint64 distance);
extern double (*BitJaccardDistance) (uint32 bytes, unsigned char *ax, unsigned char *bx, uint64 ab, uint64 aa, uint64 bb);

void		BitvecInit(void);

#endif
```

## File: `src/bitvec.c`
```c
#include "postgres.h"

#include "bitutils.h"
#include "bitvec.h"
#include "fmgr.h"
#include "utils/varbit.h"
#include "vector.h"

#if PG_VERSION_NUM >= 160000
#include "varatt.h"
#endif

/*
 * Allocate and initialize a new bit vector
 */
VarBit *
InitBitVector(int dim)
{
	VarBit	   *result;
	int			size;

	size = VARBITTOTALLEN(dim);
	result = (VarBit *) palloc0(size);
	SET_VARSIZE(result, size);
	VARBITLEN(result) = dim;

	return result;
}

/*
 * Ensure same dimensions
 */
static inline void
CheckDims(VarBit *a, VarBit *b)
{
	if (VARBITLEN(a) != VARBITLEN(b))
		ereport(ERROR,
				(errcode(ERRCODE_DATA_EXCEPTION),
				 errmsg("different bit lengths %u and %u", VARBITLEN(a), VARBITLEN(b))));
}

/*
 * Get the Hamming distance between two bit vectors
 */
FUNCTION_PREFIX PG_FUNCTION_INFO_V1(hamming_distance);
Datum
hamming_distance(PG_FUNCTION_ARGS)
{
	VarBit	   *a = PG_GETARG_VARBIT_P(0);
	VarBit	   *b = PG_GETARG_VARBIT_P(1);

	CheckDims(a, b);

	PG_RETURN_FLOAT8((double) BitHammingDistance(VARBITBYTES(a), VARBITS(a), VARBITS(b), 0));
}

/*
 * Get the Jaccard distance between two bit vectors
 */
FUNCTION_PREFIX PG_FUNCTION_INFO_V1(jaccard_distance);
Datum
jaccard_distance(PG_FUNCTION_ARGS)
{
	VarBit	   *a = PG_GETARG_VARBIT_P(0);
	VarBit	   *b = PG_GETARG_VARBIT_P(1);

	CheckDims(a, b);

	PG_RETURN_FLOAT8(BitJaccardDistance(VARBITBYTES(a), VARBITS(a), VARBITS(b), 0, 0, 0));
}
```

## File: `src/bitvec.h`
```c
#ifndef BITVEC_H
#define BITVEC_H

#include "utils/varbit.h"

VarBit	   *InitBitVector(int dim);

#endif
```

## File: `src/halfutils.c`
```c
#include "postgres.h"

#include <math.h>

#include "halfutils.h"
#include "halfvec.h"

#ifdef HALFVEC_DISPATCH
#include <immintrin.h>

#if defined(USE__GET_CPUID)
#include <cpuid.h>
#else
#include <intrin.h>
#endif

#ifdef _MSC_VER
#define TARGET_F16C
#else
#define TARGET_F16C __attribute__((target("avx,f16c,fma")))
#endif
#endif

float		(*HalfvecL2SquaredDistance) (int dim, half * ax, half * bx);
float		(*HalfvecInnerProduct) (int dim, half * ax, half * bx);
double		(*HalfvecCosineSimilarity) (int dim, half * ax, half * bx);
float		(*HalfvecL1Distance) (int dim, half * ax, half * bx);

static float
HalfvecL2SquaredDistanceDefault(int dim, half * ax, half * bx)
{
	float		distance = 0.0;

	/* Auto-vectorized */
	for (int i = 0; i < dim; i++)
	{
		float		diff = HalfToFloat4(ax[i]) - HalfToFloat4(bx[i]);

		distance += diff * diff;
	}

	return distance;
}

#ifdef HALFVEC_DISPATCH
TARGET_F16C static float
HalfvecL2SquaredDistanceF16c(int dim, half * ax, half * bx)
{
	float		distance;
	int			i;
	float		s[8];
	int			count = (dim / 8) * 8;
	__m256		dist = _mm256_setzero_ps();

	for (i = 0; i < count; i += 8)
	{
		__m128i		axi = _mm_loadu_si128((__m128i *) (ax + i));
		__m128i		bxi = _mm_loadu_si128((__m128i *) (bx + i));
		__m256		axs = _mm256_cvtph_ps(axi);
		__m256		bxs = _mm256_cvtph_ps(bxi);
		__m256		diff = _mm256_sub_ps(axs, bxs);

		dist = _mm256_fmadd_ps(diff, diff, dist);
	}

	_mm256_storeu_ps(s, dist);

	distance = s[0] + s[1] + s[2] + s[3] + s[4] + s[5] + s[6] + s[7];

	for (; i < dim; i++)
	{
		float		diff = HalfToFloat4(ax[i]) - HalfToFloat4(bx[i]);

		distance += diff * diff;
	}

	return distance;
}
#endif

static float
HalfvecInnerProductDefault(int dim, half * ax, half * bx)
{
	float		distance = 0.0;

	/* Auto-vectorized */
	for (int i = 0; i < dim; i++)
		distance += HalfToFloat4(ax[i]) * HalfToFloat4(bx[i]);

	return distance;
}

#ifdef HALFVEC_DISPATCH
TARGET_F16C static float
HalfvecInnerProductF16c(int dim, half * ax, half * bx)
{
	float		distance;
	int			i;
	float		s[8];
	int			count = (dim / 8) * 8;
	__m256		dist = _mm256_setzero_ps();

	for (i = 0; i < count; i += 8)
	{
		__m128i		axi = _mm_loadu_si128((__m128i *) (ax + i));
		__m128i		bxi = _mm_loadu_si128((__m128i *) (bx + i));
		__m256		axs = _mm256_cvtph_ps(axi);
		__m256		bxs = _mm256_cvtph_ps(bxi);

		dist = _mm256_fmadd_ps(axs, bxs, dist);
	}

	_mm256_storeu_ps(s, dist);

	distance = s[0] + s[1] + s[2] + s[3] + s[4] + s[5] + s[6] + s[7];

	for (; i < dim; i++)
		distance += HalfToFloat4(ax[i]) * HalfToFloat4(bx[i]);

	return distance;
}
#endif

static double
HalfvecCosineSimilarityDefault(int dim, half * ax, half * bx)
{
	float		similarity = 0.0;
	float		norma = 0.0;
	float		normb = 0.0;

	/* Auto-vectorized */
	for (int i = 0; i < dim; i++)
	{
		float		axi = HalfToFloat4(ax[i]);
		float		bxi = HalfToFloat4(bx[i]);

		similarity += axi * bxi;
		norma += axi * axi;
		normb += bxi * bxi;
	}

	/* Use sqrt(a * b) over sqrt(a) * sqrt(b) */
	return (double) similarity / sqrt((double) norma * (double) normb);
}

#ifdef HALFVEC_DISPATCH
TARGET_F16C static double
HalfvecCosineSimilarityF16c(int dim, half * ax, half * bx)
{
	float		similarity;
	float		norma;
	float		normb;
	int			i;
	float		s[8];
	int			count = (dim / 8) * 8;
	__m256		sim = _mm256_setzero_ps();
	__m256		na = _mm256_setzero_ps();
	__m256		nb = _mm256_setzero_ps();

	for (i = 0; i < count; i += 8)
	{
		__m128i		axi = _mm_loadu_si128((__m128i *) (ax + i));
		__m128i		bxi = _mm_loadu_si128((__m128i *) (bx + i));
		__m256		axs = _mm256_cvtph_ps(axi);
		__m256		bxs = _mm256_cvtph_ps(bxi);

		sim = _mm256_fmadd_ps(axs, bxs, sim);
		na = _mm256_fmadd_ps(axs, axs, na);
		nb = _mm256_fmadd_ps(bxs, bxs, nb);
	}

	_mm256_storeu_ps(s, sim);
	similarity = s[0] + s[1] + s[2] + s[3] + s[4] + s[5] + s[6] + s[7];

	_mm256_storeu_ps(s, na);
	norma = s[0] + s[1] + s[2] + s[3] + s[4] + s[5] + s[6] + s[7];

	_mm256_storeu_ps(s, nb);
	normb = s[0] + s[1] + s[2] + s[3] + s[4] + s[5] + s[6] + s[7];

	/* Auto-vectorized */
	for (; i < dim; i++)
	{
		float		axi = HalfToFloat4(ax[i]);
		float		bxi = HalfToFloat4(bx[i]);

		similarity += axi * bxi;
		norma += axi * axi;
		normb += bxi * bxi;
	}

	/* Use sqrt(a * b) over sqrt(a) * sqrt(b) */
	return (double) similarity / sqrt((double) norma * (double) normb);
}
#endif

static float
HalfvecL1DistanceDefault(int dim, half * ax, half * bx)
{
	float		distance = 0.0;

	/* Auto-vectorized */
	for (int i = 0; i < dim; i++)
		distance += fabsf(HalfToFloat4(ax[i]) - HalfToFloat4(bx[i]));

	return distance;
}

#ifdef HALFVEC_DISPATCH
/* Does not require FMA, but keep logic simple */
TARGET_F16C static float
HalfvecL1DistanceF16c(int dim, half * ax, half * bx)
{
	float		distance;
	int			i;
	float		s[8];
	int			count = (dim / 8) * 8;
	__m256		dist = _mm256_setzero_ps();
	__m256		sign = _mm256_set1_ps(-0.0);

	for (i = 0; i < count; i += 8)
	{
		__m128i		axi = _mm_loadu_si128((__m128i *) (ax + i));
		__m128i		bxi = _mm_loadu_si128((__m128i *) (bx + i));
		__m256		axs = _mm256_cvtph_ps(axi);
		__m256		bxs = _mm256_cvtph_ps(bxi);

		dist = _mm256_add_ps(dist, _mm256_andnot_ps(sign, _mm256_sub_ps(axs, bxs)));
	}

	_mm256_storeu_ps(s, dist);

	distance = s[0] + s[1] + s[2] + s[3] + s[4] + s[5] + s[6] + s[7];

	for (; i < dim; i++)
		distance += fabsf(HalfToFloat4(ax[i]) - HalfToFloat4(bx[i]));

	return distance;
}
#endif

#ifdef HALFVEC_DISPATCH
#define CPU_FEATURE_FMA     (1 << 12)
#define CPU_FEATURE_OSXSAVE (1 << 27)
#define CPU_FEATURE_AVX     (1 << 28)
#define CPU_FEATURE_F16C    (1 << 29)

#ifdef _MSC_VER
#define TARGET_XSAVE
#else
#define TARGET_XSAVE __attribute__((target("xsave")))
#endif

TARGET_XSAVE static bool
SupportsCpuFeature(unsigned int feature)
{
	unsigned int exx[4] = {0, 0, 0, 0};

#if defined(USE__GET_CPUID)
	__get_cpuid(1, &exx[0], &exx[1], &exx[2], &exx[3]);
#else
	__cpuid(exx, 1);
#endif

	/* Check OS supports XSAVE */
	if ((exx[2] & CPU_FEATURE_OSXSAVE) != CPU_FEATURE_OSXSAVE)
		return false;

	/* Check XMM and YMM registers are enabled */
	if ((_xgetbv(0) & 6) != 6)
		return false;

	/* Now check features */
	return (exx[2] & feature) == feature;
}
#endif

void
HalfvecInit(void)
{
	/*
	 * Could skip pointer when single function, but no difference in
	 * performance
	 */
	HalfvecL2SquaredDistance = HalfvecL2SquaredDistanceDefault;
	HalfvecInnerProduct = HalfvecInnerProductDefault;
	HalfvecCosineSimilarity = HalfvecCosineSimilarityDefault;
	HalfvecL1Distance = HalfvecL1DistanceDefault;

#ifdef HALFVEC_DISPATCH
	if (SupportsCpuFeature(CPU_FEATURE_AVX | CPU_FEATURE_F16C | CPU_FEATURE_FMA))
	{
		HalfvecL2SquaredDistance = HalfvecL2SquaredDistanceF16c;
		HalfvecInnerProduct = HalfvecInnerProductF16c;
		HalfvecCosineSimilarity = HalfvecCosineSimilarityF16c;
		/* Does not require FMA, but keep logic simple */
		HalfvecL1Distance = HalfvecL1DistanceF16c;
	}
#endif
}
```

## File: `src/halfutils.h`
```c
#ifndef HALFUTILS_H
#define HALFUTILS_H

#include <math.h>

#include "common/shortest_dec.h"
#include "halfvec.h"

#ifdef F16C_SUPPORT
#include <immintrin.h>
#endif

extern float (*HalfvecL2SquaredDistance) (int dim, half * ax, half * bx);
extern float (*HalfvecInnerProduct) (int dim, half * ax, half * bx);
extern double (*HalfvecCosineSimilarity) (int dim, half * ax, half * bx);
extern float (*HalfvecL1Distance) (int dim, half * ax, half * bx);

void		HalfvecInit(void);

/*
 * Check if half is NaN
 */
static inline bool
HalfIsNan(half num)
{
#ifdef FLT16_SUPPORT
	return isnan(num);
#else
	return (num & 0x7C00) == 0x7C00 && (num & 0x7FFF) != 0x7C00;
#endif
}

/*
 * Check if half is infinite
 */
static inline bool
HalfIsInf(half num)
{
#ifdef FLT16_SUPPORT
	return isinf(num);
#else
	return (num & 0x7FFF) == 0x7C00;
#endif
}

/*
 * Check if half is zero
 */
static inline bool
HalfIsZero(half num)
{
#ifdef FLT16_SUPPORT
	return num == 0;
#else
	return (num & 0x7FFF) == 0x0000;
#endif
}

/*
 * Convert a half to a float4
 */
static inline float
HalfToFloat4(half num)
{
#if defined(F16C_SUPPORT)
	return _cvtsh_ss(num);
#elif defined(FLT16_SUPPORT)
	return (float) num;
#else
	union
	{
		float		f;
		uint32		i;
	}			swapfloat;

	union
	{
		half		h;
		uint16		i;
	}			swaphalf;

	uint16		bin;
	uint32		exponent;
	uint32		mantissa;
	uint32		result;

	swaphalf.h = num;
	bin = swaphalf.i;
	exponent = (bin & 0x7C00) >> 10;
	mantissa = bin & 0x03FF;

	/* Sign */
	result = (bin & 0x8000) << 16;

	if (unlikely(exponent == 31))
	{
		if (mantissa == 0)
		{
			/* Infinite */
			result |= 0x7F800000;
		}
		else
		{
			/* NaN */
			result |= 0x7FC00000;
		}
	}
	else if (unlikely(exponent == 0))
	{
		/* Subnormal */
		if (mantissa != 0)
		{
			exponent = -14;

			for (int i = 0; i < 10; i++)
			{
				mantissa <<= 1;
				exponent -= 1;

				if ((mantissa >> 10) % 2 == 1)
				{
					mantissa &= 0x03ff;
					break;
				}
			}

			result |= (exponent + 127) << 23;
		}
	}
	else
	{
		/* Normal */
		result |= (exponent - 15 + 127) << 23;
	}

	result |= mantissa << 13;

	swapfloat.i = result;
	return swapfloat.f;
#endif
}

/*
 * Convert a float4 to a half
 */
static inline half
Float4ToHalfUnchecked(float num)
{
#if defined(F16C_SUPPORT)
	return _cvtss_sh(num, 0);
#elif defined(FLT16_SUPPORT)
	return (_Float16) num;
#else
	union
	{
		float		f;
		uint32		i;
	}			swapfloat;

	union
	{
		half		h;
		uint16		i;
	}			swaphalf;

	uint32		bin;
	int			exponent;
	int			mantissa;
	uint16		result;

	swapfloat.f = num;
	bin = swapfloat.i;
	exponent = (bin & 0x7F800000) >> 23;
	mantissa = bin & 0x007FFFFF;

	/* Sign */
	result = (bin & 0x80000000) >> 16;

	if (isinf(num))
	{
		/* Infinite */
		result |= 0x7C00;
	}
	else if (isnan(num))
	{
		/* NaN */
		result |= 0x7E00;
		result |= mantissa >> 13;
	}
	else if (exponent > 98)
	{
		int			m;
		int			gr;
		int			s;

		exponent -= 127;
		s = mantissa & 0x00000FFF;

		/* Subnormal */
		if (exponent < -14)
		{
			int			diff = -exponent - 14;

			mantissa >>= diff;
			mantissa += 1 << (23 - diff);
			s |= mantissa & 0x00000FFF;
		}

		m = mantissa >> 13;

		/* Round */
		gr = (mantissa >> 12) % 4;
		if (gr == 3 || (gr == 1 && s != 0))
			m += 1;

		if (m == 1024)
		{
			m = 0;
			exponent += 1;
		}

		if (exponent > 15)
		{
			/* Infinite */
			result |= 0x7C00;
		}
		else
		{
			if (exponent >= -14)
				result |= (exponent + 15) << 10;

			result |= m;
		}
	}

	swaphalf.i = result;
	return swaphalf.h;
#endif
}

/*
 * Convert a float4 to a half
 */
static inline half
Float4ToHalf(float num)
{
	half		result = Float4ToHalfUnchecked(num);

	if (unlikely(HalfIsInf(result)) && !isinf(num))
	{
		char	   *buf = palloc(FLOAT_SHORTEST_DECIMAL_LEN);

		float_to_shortest_decimal_buf(num, buf);

		ereport(ERROR,
				(errcode(ERRCODE_NUMERIC_VALUE_OUT_OF_RANGE),
				 errmsg("\"%s\" is out of range for type halfvec", buf)));
	}

	return result;
}

#endif
```

## File: `src/halfvec.c`
```c
#include "postgres.h"

#include <math.h>

#include "bitvec.h"
#include "catalog/pg_type.h"
#include "common/shortest_dec.h"
#include "fmgr.h"
#include "halfutils.h"
#include "halfvec.h"
#include "lib/stringinfo.h"
#include "libpq/pqformat.h"
#include "port.h"				/* for strtof() */
#include "sparsevec.h"
#include "utils/array.h"
#include "utils/float.h"
#include "utils/fmgrprotos.h"
#include "utils/lsyscache.h"
#include "utils/varbit.h"
#include "vector.h"

#if PG_VERSION_NUM >= 160000
#include "varatt.h"
#endif

#if PG_VERSION_NUM >= 170000
#include "parser/scansup.h"
#endif

#define STATE_DIMS(x) (ARR_DIMS(x)[0] - 1)
#define CreateStateDatums(dim) palloc(sizeof(Datum) * (dim + 1))

/*
 * Get a half from a message buffer
 */
static half
pq_getmsghalf(StringInfo msg)
{
	union
	{
		half		h;
		uint16		i;
	}			swap;

	swap.i = pq_getmsgint(msg, 2);
	return swap.h;
}

/*
 * Append a half to a StringInfo buffer
 */
static void
pq_sendhalf(StringInfo buf, half h)
{
	union
	{
		half		h;
		uint16		i;
	}			swap;

	swap.h = h;
	pq_sendint16(buf, swap.i);
}

/*
 * Ensure same dimensions
 */
static inline void
CheckDims(HalfVector * a, HalfVector * b)
{
	if (a->dim != b->dim)
		ereport(ERROR,
				(errcode(ERRCODE_DATA_EXCEPTION),
				 errmsg("different halfvec dimensions %d and %d", a->dim, b->dim)));
}

/*
 * Ensure expected dimensions
 */
static inline void
CheckExpectedDim(int32 typmod, int dim)
{
	if (typmod != -1 && typmod != dim)
		ereport(ERROR,
				(errcode(ERRCODE_DATA_EXCEPTION),
				 errmsg("expected %d dimensions, not %d", typmod, dim)));
}

/*
 * Ensure valid dimensions
 */
static inline void
CheckDim(int dim)
{
	if (dim < 1)
		ereport(ERROR,
				(errcode(ERRCODE_DATA_EXCEPTION),
				 errmsg("halfvec must have at least 1 dimension")));

	if (dim > HALFVEC_MAX_DIM)
		ereport(ERROR,
				(errcode(ERRCODE_PROGRAM_LIMIT_EXCEEDED),
				 errmsg("halfvec cannot have more than %d dimensions", HALFVEC_MAX_DIM)));
}

/*
 * Ensure finite element
 */
static inline void
CheckElement(half value)
{
	if (HalfIsNan(value))
		ereport(ERROR,
				(errcode(ERRCODE_DATA_EXCEPTION),
				 errmsg("NaN not allowed in halfvec")));

	if (HalfIsInf(value))
		ereport(ERROR,
				(errcode(ERRCODE_DATA_EXCEPTION),
				 errmsg("infinite value not allowed in halfvec")));
}

/*
 * Allocate and initialize a new half vector
 */
HalfVector *
InitHalfVector(int dim)
{
	HalfVector *result;
	int			size;

	size = HALFVEC_SIZE(dim);
	result = (HalfVector *) palloc0(size);
	SET_VARSIZE(result, size);
	result->dim = dim;

	return result;
}

#if PG_VERSION_NUM >= 170000
#define halfvec_isspace(ch) scanner_isspace(ch)
#else
static inline bool
halfvec_isspace(char ch)
{
	if (ch == ' ' ||
		ch == '\t' ||
		ch == '\n' ||
		ch == '\r' ||
		ch == '\v' ||
		ch == '\f')
		return true;
	return false;
}
#endif

/*
 * Check state array
 */
static float8 *
CheckStateArray(ArrayType *statearray, const char *caller)
{
	if (ARR_NDIM(statearray) != 1 ||
		ARR_DIMS(statearray)[0] < 1 ||
		ARR_HASNULL(statearray) ||
		ARR_ELEMTYPE(statearray) != FLOAT8OID)
		elog(ERROR, "%s: expected state array", caller);
	return (float8 *) ARR_DATA_PTR(statearray);
}

/*
 * Convert textual representation to internal representation
 */
FUNCTION_PREFIX PG_FUNCTION_INFO_V1(halfvec_in);
Datum
halfvec_in(PG_FUNCTION_ARGS)
{
	char	   *lit = PG_GETARG_CSTRING(0);
	int32		typmod = PG_GETARG_INT32(2);
	half		x[HALFVEC_MAX_DIM];
	int			dim = 0;
	char	   *pt = lit;
	HalfVector *result;

	while (halfvec_isspace(*pt))
		pt++;

	if (*pt != '[')
		ereport(ERROR,
				(errcode(ERRCODE_INVALID_TEXT_REPRESENTATION),
				 errmsg("invalid input syntax for type halfvec: \"%s\"", lit),
				 errdetail("Vector contents must start with \"[\".")));

	pt++;

	while (halfvec_isspace(*pt))
		pt++;

	if (*pt == ']')
		ereport(ERROR,
				(errcode(ERRCODE_DATA_EXCEPTION),
				 errmsg("halfvec must have at least 1 dimension")));

	for (;;)
	{
		float		val;
		char	   *stringEnd;

		if (dim == HALFVEC_MAX_DIM)
			ereport(ERROR,
					(errcode(ERRCODE_PROGRAM_LIMIT_EXCEEDED),
					 errmsg("halfvec cannot have more than %d dimensions", HALFVEC_MAX_DIM)));

		while (halfvec_isspace(*pt))
			pt++;

		/* Check for empty string like float4in */
		if (*pt == '\0')
			ereport(ERROR,
					(errcode(ERRCODE_INVALID_TEXT_REPRESENTATION),
					 errmsg("invalid input syntax for type halfvec: \"%s\"", lit)));

		errno = 0;

		/* Postgres sets LC_NUMERIC to C on startup */
		val = strtof(pt, &stringEnd);

		if (stringEnd == pt)
			ereport(ERROR,
					(errcode(ERRCODE_INVALID_TEXT_REPRESENTATION),
					 errmsg("invalid input syntax for type halfvec: \"%s\"", lit)));

		x[dim] = Float4ToHalfUnchecked(val);

		/* Check for range error like float4in */
		if ((errno == ERANGE && isinf(val)) || (HalfIsInf(x[dim]) && !isinf(val)))
			ereport(ERROR,
					(errcode(ERRCODE_NUMERIC_VALUE_OUT_OF_RANGE),
					 errmsg("\"%s\" is out of range for type halfvec", pnstrdup(pt, stringEnd - pt))));

		CheckElement(x[dim]);
		dim++;

		pt = stringEnd;

		while (halfvec_isspace(*pt))
			pt++;

		if (*pt == ',')
			pt++;
		else if (*pt == ']')
		{
			pt++;
			break;
		}
		else
			ereport(ERROR,
					(errcode(ERRCODE_INVALID_TEXT_REPRESENTATION),
					 errmsg("invalid input syntax for type halfvec: \"%s\"", lit)));
	}

	/* Only whitespace is allowed after the closing brace */
	while (halfvec_isspace(*pt))
		pt++;

	if (*pt != '\0')
		ereport(ERROR,
				(errcode(ERRCODE_INVALID_TEXT_REPRESENTATION),
				 errmsg("invalid input syntax for type halfvec: \"%s\"", lit),
				 errdetail("Junk after closing right brace.")));

	CheckDim(dim);
	CheckExpectedDim(typmod, dim);

	result = InitHalfVector(dim);
	for (int i = 0; i < dim; i++)
		result->x[i] = x[i];

	PG_RETURN_POINTER(result);
}

#define AppendChar(ptr, c) (*(ptr)++ = (c))
#define AppendFloat(ptr, f) ((ptr) += float_to_shortest_decimal_bufn((f), (ptr)))

/*
 * Convert internal representation to textual representation
 */
FUNCTION_PREFIX PG_FUNCTION_INFO_V1(halfvec_out);
Datum
halfvec_out(PG_FUNCTION_ARGS)
{
	HalfVector *vector = PG_GETARG_HALFVEC_P(0);
	int			dim = vector->dim;
	char	   *buf;
	char	   *ptr;

	/*
	 * Need:
	 *
	 * dim * (FLOAT_SHORTEST_DECIMAL_LEN - 1) bytes for
	 * float_to_shortest_decimal_bufn
	 *
	 * dim - 1 bytes for separator
	 *
	 * 3 bytes for [, ], and \0
	 */
	buf = (char *) palloc(FLOAT_SHORTEST_DECIMAL_LEN * dim + 2);
	ptr = buf;

	AppendChar(ptr, '[');

	for (int i = 0; i < dim; i++)
	{
		if (i > 0)
			AppendChar(ptr, ',');

		/*
		 * Use shortest decimal representation of single-precision float for
		 * simplicity
		 */
		AppendFloat(ptr, HalfToFloat4(vector->x[i]));
	}

	AppendChar(ptr, ']');
	*ptr = '\0';

	PG_FREE_IF_COPY(vector, 0);
	PG_RETURN_CSTRING(buf);
}

/*
 * Convert type modifier
 */
FUNCTION_PREFIX PG_FUNCTION_INFO_V1(halfvec_typmod_in);
Datum
halfvec_typmod_in(PG_FUNCTION_ARGS)
{
	ArrayType  *ta = PG_GETARG_ARRAYTYPE_P(0);
	int32	   *tl;
	int			n;

	tl = ArrayGetIntegerTypmods(ta, &n);

	if (n != 1)
		ereport(ERROR,
				(errcode(ERRCODE_INVALID_PARAMETER_VALUE),
				 errmsg("invalid type modifier")));

	if (*tl < 1)
		ereport(ERROR,
				(errcode(ERRCODE_INVALID_PARAMETER_VALUE),
				 errmsg("dimensions for type halfvec must be at least 1")));

	if (*tl > HALFVEC_MAX_DIM)
		ereport(ERROR,
				(errcode(ERRCODE_INVALID_PARAMETER_VALUE),
				 errmsg("dimensions for type halfvec cannot exceed %d", HALFVEC_MAX_DIM)));

	PG_RETURN_INT32(*tl);
}

/*
 * Convert external binary representation to internal representation
 */
FUNCTION_PREFIX PG_FUNCTION_INFO_V1(halfvec_recv);
Datum
halfvec_recv(PG_FUNCTION_ARGS)
{
	StringInfo	buf = (StringInfo) PG_GETARG_POINTER(0);
	int32		typmod = PG_GETARG_INT32(2);
	HalfVector *result;
	int16		dim;
	int16		unused;

	dim = pq_getmsgint(buf, sizeof(int16));
	unused = pq_getmsgint(buf, sizeof(int16));

	CheckDim(dim);
	CheckExpectedDim(typmod, dim);

	if (unused != 0)
		ereport(ERROR,
				(errcode(ERRCODE_DATA_EXCEPTION),
				 errmsg("expected unused to be 0, not %d", unused)));

	result = InitHalfVector(dim);
	for (int i = 0; i < dim; i++)
	{
		result->x[i] = pq_getmsghalf(buf);
		CheckElement(result->x[i]);
	}

	PG_RETURN_POINTER(result);
}

/*
 * Convert internal representation to the external binary representation
 */
FUNCTION_PREFIX PG_FUNCTION_INFO_V1(halfvec_send);
Datum
halfvec_send(PG_FUNCTION_ARGS)
{
	HalfVector *vec = PG_GETARG_HALFVEC_P(0);
	StringInfoData buf;

	pq_begintypsend(&buf);
	pq_sendint(&buf, vec->dim, sizeof(int16));
	pq_sendint(&buf, vec->unused, sizeof(int16));
	for (int i = 0; i < vec->dim; i++)
		pq_sendhalf(&buf, vec->x[i]);

	PG_RETURN_BYTEA_P(pq_endtypsend(&buf));
}

/*
 * Convert half vector to half vector
 * This is needed to check the type modifier
 */
FUNCTION_PREFIX PG_FUNCTION_INFO_V1(halfvec);
Datum
halfvec(PG_FUNCTION_ARGS)
{
	HalfVector *vec = PG_GETARG_HALFVEC_P(0);
	int32		typmod = PG_GETARG_INT32(1);

	CheckExpectedDim(typmod, vec->dim);

	PG_RETURN_POINTER(vec);
}

/*
 * Convert array to half vector
 */
FUNCTION_PREFIX PG_FUNCTION_INFO_V1(array_to_halfvec);
Datum
array_to_halfvec(PG_FUNCTION_ARGS)
{
	ArrayType  *array = PG_GETARG_ARRAYTYPE_P(0);
	int32		typmod = PG_GETARG_INT32(1);
	HalfVector *result;
	int16		typlen;
	bool		typbyval;
	char		typalign;
	Datum	   *elemsp;
	int			nelemsp;

	if (ARR_NDIM(array) > 1)
		ereport(ERROR,
				(errcode(ERRCODE_DATA_EXCEPTION),
				 errmsg("array must be 1-D")));

	if (ARR_HASNULL(array) && array_contains_nulls(array))
		ereport(ERROR,
				(errcode(ERRCODE_NULL_VALUE_NOT_ALLOWED),
				 errmsg("array must not contain nulls")));

	get_typlenbyvalalign(ARR_ELEMTYPE(array), &typlen, &typbyval, &typalign);
	deconstruct_array(array, ARR_ELEMTYPE(array), typlen, typbyval, typalign, &elemsp, NULL, &nelemsp);

	CheckDim(nelemsp);
	CheckExpectedDim(typmod, nelemsp);

	result = InitHalfVector(nelemsp);

	if (ARR_ELEMTYPE(array) == INT4OID)
	{
		for (int i = 0; i < nelemsp; i++)
			result->x[i] = Float4ToHalf(DatumGetInt32(elemsp[i]));
	}
	else if (ARR_ELEMTYPE(array) == FLOAT8OID)
	{
		for (int i = 0; i < nelemsp; i++)
			result->x[i] = Float4ToHalf(DatumGetFloat8(elemsp[i]));
	}
	else if (ARR_ELEMTYPE(array) == FLOAT4OID)
	{
		for (int i = 0; i < nelemsp; i++)
			result->x[i] = Float4ToHalf(DatumGetFloat4(elemsp[i]));
	}
	else if (ARR_ELEMTYPE(array) == NUMERICOID)
	{
		for (int i = 0; i < nelemsp; i++)
			result->x[i] = Float4ToHalf(DatumGetFloat4(DirectFunctionCall1(numeric_float4, elemsp[i])));
	}
	else
	{
		ereport(ERROR,
				(errcode(ERRCODE_DATA_EXCEPTION),
				 errmsg("unsupported array type")));
	}

	/*
	 * Free allocation from deconstruct_array. Do not free individual elements
	 * when pass-by-reference since they point to original array.
	 */
	pfree(elemsp);

	/* Check elements */
	for (int i = 0; i < result->dim; i++)
		CheckElement(result->x[i]);

	PG_RETURN_POINTER(result);
}

/*
 * Convert half vector to float4[]
 */
FUNCTION_PREFIX PG_FUNCTION_INFO_V1(halfvec_to_float4);
Datum
halfvec_to_float4(PG_FUNCTION_ARGS)
{
	HalfVector *vec = PG_GETARG_HALFVEC_P(0);
	Datum	   *datums;
	ArrayType  *result;

	datums = (Datum *) palloc(sizeof(Datum) * vec->dim);

	for (int i = 0; i < vec->dim; i++)
		datums[i] = Float4GetDatum(HalfToFloat4(vec->x[i]));

	/* Use TYPALIGN_INT for float4 */
	result = construct_array(datums, vec->dim, FLOAT4OID, sizeof(float4), true, TYPALIGN_INT);

	pfree(datums);

	PG_RETURN_POINTER(result);
}

/*
 * Convert vector to half vec
 */
FUNCTION_PREFIX PG_FUNCTION_INFO_V1(vector_to_halfvec);
Datum
vector_to_halfvec(PG_FUNCTION_ARGS)
{
	Vector	   *vec = PG_GETARG_VECTOR_P(0);
	int32		typmod = PG_GETARG_INT32(1);
	HalfVector *result;

	CheckDim(vec->dim);
	CheckExpectedDim(typmod, vec->dim);

	result = InitHalfVector(vec->dim);

	for (int i = 0; i < vec->dim; i++)
		result->x[i] = Float4ToHalf(vec->x[i]);

	PG_RETURN_POINTER(result);
}

/*
 * Get the L2 distance between half vectors
 */
FUNCTION_PREFIX PG_FUNCTION_INFO_V1(halfvec_l2_distance);
Datum
halfvec_l2_distance(PG_FUNCTION_ARGS)
{
	HalfVector *a = PG_GETARG_HALFVEC_P(0);
	HalfVector *b = PG_GETARG_HALFVEC_P(1);

	CheckDims(a, b);

	PG_RETURN_FLOAT8(sqrt((double) HalfvecL2SquaredDistance(a->dim, a->x, b->x)));
}

/*
 * Get the L2 squared distance between half vectors
 */
FUNCTION_PREFIX PG_FUNCTION_INFO_V1(halfvec_l2_squared_distance);
Datum
halfvec_l2_squared_distance(PG_FUNCTION_ARGS)
{
	HalfVector *a = PG_GETARG_HALFVEC_P(0);
	HalfVector *b = PG_GETARG_HALFVEC_P(1);

	CheckDims(a, b);

	PG_RETURN_FLOAT8((double) HalfvecL2SquaredDistance(a->dim, a->x, b->x));
}

/*
 * Get the inner product of two half vectors
 */
FUNCTION_PREFIX PG_FUNCTION_INFO_V1(halfvec_inner_product);
Datum
halfvec_inner_product(PG_FUNCTION_ARGS)
{
	HalfVector *a = PG_GETARG_HALFVEC_P(0);
	HalfVector *b = PG_GETARG_HALFVEC_P(1);

	CheckDims(a, b);

	PG_RETURN_FLOAT8((double) HalfvecInnerProduct(a->dim, a->x, b->x));
}

/*
 * Get the negative inner product of two half vectors
 */
FUNCTION_PREFIX PG_FUNCTION_INFO_V1(halfvec_negative_inner_product);
Datum
halfvec_negative_inner_product(PG_FUNCTION_ARGS)
{
	HalfVector *a = PG_GETARG_HALFVEC_P(0);
	HalfVector *b = PG_GETARG_HALFVEC_P(1);

	CheckDims(a, b);

	PG_RETURN_FLOAT8((double) -HalfvecInnerProduct(a->dim, a->x, b->x));
}

/*
 * Get the cosine distance between two half vectors
 */
FUNCTION_PREFIX PG_FUNCTION_INFO_V1(halfvec_cosine_distance);
Datum
halfvec_cosine_distance(PG_FUNCTION_ARGS)
{
	HalfVector *a = PG_GETARG_HALFVEC_P(0);
	HalfVector *b = PG_GETARG_HALFVEC_P(1);
	double		similarity;

	CheckDims(a, b);

	similarity = HalfvecCosineSimilarity(a->dim, a->x, b->x);

#ifdef _MSC_VER
	/* /fp:fast may not propagate NaN */
	if (isnan(similarity))
		PG_RETURN_FLOAT8(NAN);
#endif

	/* Keep in range */
	if (similarity > 1)
		similarity = 1;
	else if (similarity < -1)
		similarity = -1;

	PG_RETURN_FLOAT8(1 - similarity);
}

/*
 * Get the distance for spherical k-means
 * Currently uses angular distance since needs to satisfy triangle inequality
 * Assumes inputs are unit vectors (skips norm)
 */
FUNCTION_PREFIX PG_FUNCTION_INFO_V1(halfvec_spherical_distance);
Datum
halfvec_spherical_distance(PG_FUNCTION_ARGS)
{
	HalfVector *a = PG_GETARG_HALFVEC_P(0);
	HalfVector *b = PG_GETARG_HALFVEC_P(1);
	double		distance;

	CheckDims(a, b);

	distance = (double) HalfvecInnerProduct(a->dim, a->x, b->x);

	/* Prevent NaN with acos with loss of precision */
	if (distance > 1)
		distance = 1;
	else if (distance < -1)
		distance = -1;

	PG_RETURN_FLOAT8(acos(distance) / M_PI);
}

/*
 * Get the L1 distance between two half vectors
 */
FUNCTION_PREFIX PG_FUNCTION_INFO_V1(halfvec_l1_distance);
Datum
halfvec_l1_distance(PG_FUNCTION_ARGS)
{
	HalfVector *a = PG_GETARG_HALFVEC_P(0);
	HalfVector *b = PG_GETARG_HALFVEC_P(1);

	CheckDims(a, b);

	PG_RETURN_FLOAT8((double) HalfvecL1Distance(a->dim, a->x, b->x));
}

/*
 * Get the dimensions of a half vector
 */
FUNCTION_PREFIX PG_FUNCTION_INFO_V1(halfvec_vector_dims);
Datum
halfvec_vector_dims(PG_FUNCTION_ARGS)
{
	HalfVector *a = PG_GETARG_HALFVEC_P(0);

	PG_RETURN_INT32(a->dim);
}

/*
 * Get the L2 norm of a half vector
 */
FUNCTION_PREFIX PG_FUNCTION_INFO_V1(halfvec_l2_norm);
Datum
halfvec_l2_norm(PG_FUNCTION_ARGS)
{
	HalfVector *a = PG_GETARG_HALFVEC_P(0);
	half	   *ax = a->x;
	double		norm = 0.0;

	/* Auto-vectorized */
	for (int i = 0; i < a->dim; i++)
	{
		double		axi = (double) HalfToFloat4(ax[i]);

		norm += axi * axi;
	}

	PG_RETURN_FLOAT8(sqrt(norm));
}

/*
 * Normalize a half vector with the L2 norm
 */
FUNCTION_PREFIX PG_FUNCTION_INFO_V1(halfvec_l2_normalize);
Datum
halfvec_l2_normalize(PG_FUNCTION_ARGS)
{
	HalfVector *a = PG_GETARG_HALFVEC_P(0);
	half	   *ax = a->x;
	double		norm = 0;
	HalfVector *result;
	half	   *rx;

	result = InitHalfVector(a->dim);
	rx = result->x;

	/* Auto-vectorized */
	for (int i = 0; i < a->dim; i++)
		norm += (double) HalfToFloat4(ax[i]) * (double) HalfToFloat4(ax[i]);

	norm = sqrt(norm);

	/* Return zero vector for zero norm */
	if (norm > 0)
	{
		for (int i = 0; i < a->dim; i++)
			rx[i] = Float4ToHalfUnchecked(HalfToFloat4(ax[i]) / norm);

		/* Check for overflow */
		for (int i = 0; i < a->dim; i++)
		{
			if (HalfIsInf(rx[i]))
				float_overflow_error();
		}
	}

	PG_RETURN_POINTER(result);
}

/*
 * Add half vectors
 */
FUNCTION_PREFIX PG_FUNCTION_INFO_V1(halfvec_add);
Datum
halfvec_add(PG_FUNCTION_ARGS)
{
	HalfVector *a = PG_GETARG_HALFVEC_P(0);
	HalfVector *b = PG_GETARG_HALFVEC_P(1);
	half	   *ax = a->x;
	half	   *bx = b->x;
	HalfVector *result;
	half	   *rx;

	CheckDims(a, b);

	result = InitHalfVector(a->dim);
	rx = result->x;

	/* Auto-vectorized */
	for (int i = 0, imax = a->dim; i < imax; i++)
	{
#ifdef FLT16_SUPPORT
		rx[i] = ax[i] + bx[i];
#else
		rx[i] = Float4ToHalfUnchecked(HalfToFloat4(ax[i]) + HalfToFloat4(bx[i]));
#endif
	}

	/* Check for overflow */
	for (int i = 0, imax = a->dim; i < imax; i++)
	{
		if (HalfIsInf(rx[i]))
			float_overflow_error();
	}

	PG_RETURN_POINTER(result);
}

/*
 * Subtract half vectors
 */
FUNCTION_PREFIX PG_FUNCTION_INFO_V1(halfvec_sub);
Datum
halfvec_sub(PG_FUNCTION_ARGS)
{
	HalfVector *a = PG_GETARG_HALFVEC_P(0);
	HalfVector *b = PG_GETARG_HALFVEC_P(1);
	half	   *ax = a->x;
	half	   *bx = b->x;
	HalfVector *result;
	half	   *rx;

	CheckDims(a, b);

	result = InitHalfVector(a->dim);
	rx = result->x;

	/* Auto-vectorized */
	for (int i = 0, imax = a->dim; i < imax; i++)
	{
#ifdef FLT16_SUPPORT
		rx[i] = ax[i] - bx[i];
#else
		rx[i] = Float4ToHalfUnchecked(HalfToFloat4(ax[i]) - HalfToFloat4(bx[i]));
#endif
	}

	/* Check for overflow */
	for (int i = 0, imax = a->dim; i < imax; i++)
	{
		if (HalfIsInf(rx[i]))
			float_overflow_error();
	}

	PG_RETURN_POINTER(result);
}

/*
 * Multiply half vectors
 */
FUNCTION_PREFIX PG_FUNCTION_INFO_V1(halfvec_mul);
Datum
halfvec_mul(PG_FUNCTION_ARGS)
{
	HalfVector *a = PG_GETARG_HALFVEC_P(0);
	HalfVector *b = PG_GETARG_HALFVEC_P(1);
	half	   *ax = a->x;
	half	   *bx = b->x;
	HalfVector *result;
	half	   *rx;

	CheckDims(a, b);

	result = InitHalfVector(a->dim);
	rx = result->x;

	/* Auto-vectorized */
	for (int i = 0, imax = a->dim; i < imax; i++)
	{
#ifdef FLT16_SUPPORT
		rx[i] = ax[i] * bx[i];
#else
		rx[i] = Float4ToHalfUnchecked(HalfToFloat4(ax[i]) * HalfToFloat4(bx[i]));
#endif
	}

	/* Check for overflow and underflow */
	for (int i = 0, imax = a->dim; i < imax; i++)
	{
		if (HalfIsInf(rx[i]))
			float_overflow_error();

		if (HalfIsZero(rx[i]) && !(HalfIsZero(ax[i]) || HalfIsZero(bx[i])))
			float_underflow_error();
	}

	PG_RETURN_POINTER(result);
}

/*
 * Concatenate half vectors
 */
FUNCTION_PREFIX PG_FUNCTION_INFO_V1(halfvec_concat);
Datum
halfvec_concat(PG_FUNCTION_ARGS)
{
	HalfVector *a = PG_GETARG_HALFVEC_P(0);
	HalfVector *b = PG_GETARG_HALFVEC_P(1);
	HalfVector *result;
	int			dim = a->dim + b->dim;

	CheckDim(dim);
	result = InitHalfVector(dim);

	for (int i = 0; i < a->dim; i++)
		result->x[i] = a->x[i];

	for (int i = 0; i < b->dim; i++)
		result->x[i + a->dim] = b->x[i];

	PG_RETURN_POINTER(result);
}

/*
 * Quantize a half vector
 */
FUNCTION_PREFIX PG_FUNCTION_INFO_V1(halfvec_binary_quantize);
Datum
halfvec_binary_quantize(PG_FUNCTION_ARGS)
{
	HalfVector *a = PG_GETARG_HALFVEC_P(0);
	half	   *ax = a->x;
	VarBit	   *result = InitBitVector(a->dim);
	unsigned char *rx = VARBITS(result);
	int			i = 0;
	int			count = (a->dim / 8) * 8;

	/* Auto-vectorized on aarch64 */
	for (; i < count; i += 8)
	{
		unsigned char result_byte = 0;

		for (int j = 0; j < 8; j++)
			result_byte |= (HalfToFloat4(ax[i + j]) > 0) << (7 - j);

		rx[i / 8] = result_byte;
	}

	for (; i < a->dim; i++)
		rx[i / 8] |= (HalfToFloat4(ax[i]) > 0) << (7 - (i % 8));

	PG_RETURN_VARBIT_P(result);
}

/*
 * Get a subvector
 */
FUNCTION_PREFIX PG_FUNCTION_INFO_V1(halfvec_subvector);
Datum
halfvec_subvector(PG_FUNCTION_ARGS)
{
	HalfVector *a = PG_GETARG_HALFVEC_P(0);
	int32		start = PG_GETARG_INT32(1);
	int32		count = PG_GETARG_INT32(2);
	int32		end;
	half	   *ax = a->x;
	HalfVector *result;
	int32		dim;

	if (count < 1)
		ereport(ERROR,
				(errcode(ERRCODE_DATA_EXCEPTION),
				 errmsg("halfvec must have at least 1 dimension")));

	/*
	 * Check if (start + count > a->dim), avoiding integer overflow. a->dim
	 * and count are both positive, so a->dim - count won't overflow.
	 */
	if (start > a->dim - count)
		end = a->dim + 1;
	else
		end = start + count;

	/* Indexing starts at 1, like substring */
	if (start < 1)
		start = 1;
	else if (start > a->dim)
		ereport(ERROR,
				(errcode(ERRCODE_DATA_EXCEPTION),
				 errmsg("halfvec must have at least 1 dimension")));

	dim = end - start;
	CheckDim(dim);
	result = InitHalfVector(dim);

	for (int i = 0; i < dim; i++)
		result->x[i] = ax[start - 1 + i];

	PG_RETURN_POINTER(result);
}

/*
 * Internal helper to compare half vectors
 */
static int
halfvec_cmp_internal(HalfVector * a, HalfVector * b)
{
	int			dim = Min(a->dim, b->dim);

	/* Check values before dimensions to be consistent with Postgres arrays */
	for (int i = 0; i < dim; i++)
	{
		if (HalfToFloat4(a->x[i]) < HalfToFloat4(b->x[i]))
			return -1;

		if (HalfToFloat4(a->x[i]) > HalfToFloat4(b->x[i]))
			return 1;
	}

	if (a->dim < b->dim)
		return -1;

	if (a->dim > b->dim)
		return 1;

	return 0;
}

/*
 * Less than
 */
FUNCTION_PREFIX PG_FUNCTION_INFO_V1(halfvec_lt);
Datum
halfvec_lt(PG_FUNCTION_ARGS)
{
	HalfVector *a = PG_GETARG_HALFVEC_P(0);
	HalfVector *b = PG_GETARG_HALFVEC_P(1);

	PG_RETURN_BOOL(halfvec_cmp_internal(a, b) < 0);
}

/*
 * Less than or equal
 */
FUNCTION_PREFIX PG_FUNCTION_INFO_V1(halfvec_le);
Datum
halfvec_le(PG_FUNCTION_ARGS)
{
	HalfVector *a = PG_GETARG_HALFVEC_P(0);
	HalfVector *b = PG_GETARG_HALFVEC_P(1);

	PG_RETURN_BOOL(halfvec_cmp_internal(a, b) <= 0);
}

/*
 * Equal
 */
FUNCTION_PREFIX PG_FUNCTION_INFO_V1(halfvec_eq);
Datum
halfvec_eq(PG_FUNCTION_ARGS)
{
	HalfVector *a = PG_GETARG_HALFVEC_P(0);
	HalfVector *b = PG_GETARG_HALFVEC_P(1);

	PG_RETURN_BOOL(halfvec_cmp_internal(a, b) == 0);
}

/*
 * Not equal
 */
FUNCTION_PREFIX PG_FUNCTION_INFO_V1(halfvec_ne);
Datum
halfvec_ne(PG_FUNCTION_ARGS)
{
	HalfVector *a = PG_GETARG_HALFVEC_P(0);
	HalfVector *b = PG_GETARG_HALFVEC_P(1);

	PG_RETURN_BOOL(halfvec_cmp_internal(a, b) != 0);
}

/*
 * Greater than or equal
 */
FUNCTION_PREFIX PG_FUNCTION_INFO_V1(halfvec_ge);
Datum
halfvec_ge(PG_FUNCTION_ARGS)
{
	HalfVector *a = PG_GETARG_HALFVEC_P(0);
	HalfVector *b = PG_GETARG_HALFVEC_P(1);

	PG_RETURN_BOOL(halfvec_cmp_internal(a, b) >= 0);
}

/*
 * Greater than
 */
FUNCTION_PREFIX PG_FUNCTION_INFO_V1(halfvec_gt);
Datum
halfvec_gt(PG_FUNCTION_ARGS)
{
	HalfVector *a = PG_GETARG_HALFVEC_P(0);
	HalfVector *b = PG_GETARG_HALFVEC_P(1);

	PG_RETURN_BOOL(halfvec_cmp_internal(a, b) > 0);
}

/*
 * Compare half vectors
 */
FUNCTION_PREFIX PG_FUNCTION_INFO_V1(halfvec_cmp);
Datum
halfvec_cmp(PG_FUNCTION_ARGS)
{
	HalfVector *a = PG_GETARG_HALFVEC_P(0);
	HalfVector *b = PG_GETARG_HALFVEC_P(1);

	PG_RETURN_INT32(halfvec_cmp_internal(a, b));
}

/*
 * Accumulate half vectors
 */
FUNCTION_PREFIX PG_FUNCTION_INFO_V1(halfvec_accum);
Datum
halfvec_accum(PG_FUNCTION_ARGS)
{
	ArrayType  *statearray = PG_GETARG_ARRAYTYPE_P(0);
	HalfVector *newval = PG_GETARG_HALFVEC_P(1);
	float8	   *statevalues;
	int16		dim;
	bool		newarr;
	float8		n;
	Datum	   *statedatums;
	half	   *x = newval->x;
	ArrayType  *result;

	/* Check array before using */
	statevalues = CheckStateArray(statearray, "halfvec_accum");
	dim = STATE_DIMS(statearray);
	newarr = dim == 0;

	if (newarr)
		dim = newval->dim;
	else
		CheckExpectedDim(dim, newval->dim);

	n = statevalues[0] + 1.0;

	statedatums = CreateStateDatums(dim);
	statedatums[0] = Float8GetDatum(n);

	if (newarr)
	{
		for (int i = 0; i < dim; i++)
			statedatums[i + 1] = Float8GetDatum((double) HalfToFloat4(x[i]));
	}
	else
	{
		for (int i = 0; i < dim; i++)
		{
			double		v = statevalues[i + 1] + (double) HalfToFloat4(x[i]);

			/* Check for overflow */
			if (isinf(v))
				float_overflow_error();

			statedatums[i + 1] = Float8GetDatum(v);
		}
	}

	/* Use float8 array like float4_accum */
	result = construct_array(statedatums, dim + 1,
							 FLOAT8OID,
							 sizeof(float8), FLOAT8PASSBYVAL, TYPALIGN_DOUBLE);

	pfree(statedatums);

	PG_RETURN_ARRAYTYPE_P(result);
}

/*
 * Average half vectors
 */
FUNCTION_PREFIX PG_FUNCTION_INFO_V1(halfvec_avg);
Datum
halfvec_avg(PG_FUNCTION_ARGS)
{
	ArrayType  *statearray = PG_GETARG_ARRAYTYPE_P(0);
	float8	   *statevalues;
	float8		n;
	uint16		dim;
	HalfVector *result;

	/* Check array before using */
	statevalues = CheckStateArray(statearray, "halfvec_avg");
	n = statevalues[0];

	/* SQL defines AVG of no values to be NULL */
	if (n == 0.0)
		PG_RETURN_NULL();

	/* Create half vector */
	dim = STATE_DIMS(statearray);
	CheckDim(dim);
	result = InitHalfVector(dim);
	for (int i = 0; i < dim; i++)
	{
		result->x[i] = Float4ToHalf(statevalues[i + 1] / n);
		CheckElement(result->x[i]);
	}

	PG_RETURN_POINTER(result);
}

/*
 * Convert sparse vector to half vector
 */
FUNCTION_PREFIX PG_FUNCTION_INFO_V1(sparsevec_to_halfvec);
Datum
sparsevec_to_halfvec(PG_FUNCTION_ARGS)
{
	SparseVector *svec = PG_GETARG_SPARSEVEC_P(0);
	int32		typmod = PG_GETARG_INT32(1);
	HalfVector *result;
	int			dim = svec->dim;
	float	   *values = SPARSEVEC_VALUES(svec);

	CheckDim(dim);
	CheckExpectedDim(typmod, dim);

	result = InitHalfVector(dim);
	for (int i = 0; i < svec->nnz; i++)
		result->x[svec->indices[i]] = Float4ToHalf(values[i]);

	PG_RETURN_POINTER(result);
}
```

## File: `src/halfvec.h`
```c
#ifndef HALFVEC_H
#define HALFVEC_H

#define __STDC_WANT_IEC_60559_TYPES_EXT__

#include <float.h>

/* We use two types of dispatching: intrinsics and target_clones */
/* TODO Move to better place */
#ifndef DISABLE_DISPATCH
/* Only enable for more recent compilers to keep build process simple */
#if defined(__x86_64__) && defined(__GNUC__) && __GNUC__ >= 9
#define USE_DISPATCH
#elif defined(__x86_64__) && defined(__clang_major__) && __clang_major__ >= 7
#define USE_DISPATCH
#elif defined(_M_AMD64) && defined(_MSC_VER) && _MSC_VER >= 1920
#define USE_DISPATCH
#endif
#endif

/* target_clones requires glibc */
#if defined(USE_DISPATCH) && defined(__gnu_linux__) && defined(__has_attribute)
/* Use separate line for portability */
#if __has_attribute(target_clones)
#define USE_TARGET_CLONES
#endif
#endif

/* Apple clang check needed for universal binaries on Mac */
#if defined(USE_DISPATCH) && (defined(HAVE__GET_CPUID) || defined(__apple_build_version__))
#define USE__GET_CPUID
#endif

#if defined(USE_DISPATCH)
#define HALFVEC_DISPATCH
#endif

/* F16C has better performance than _Float16 (on x86-64) */
#if defined(__F16C__)
#define F16C_SUPPORT
#elif defined(__FLT16_MAX__) && !defined(HALFVEC_DISPATCH) && !defined(__FreeBSD__) && (!defined(__i386__) || defined(__SSE2__))
#define FLT16_SUPPORT
#endif

#ifdef FLT16_SUPPORT
#define half _Float16
#define HALF_MAX FLT16_MAX
#else
#define half uint16
#define HALF_MAX 65504
#endif

#define HALFVEC_MAX_DIM 16000

#define HALFVEC_SIZE(_dim)		(offsetof(HalfVector, x) + sizeof(half)*(_dim))
#define DatumGetHalfVector(x)	((HalfVector *) PG_DETOAST_DATUM(x))
#define PG_GETARG_HALFVEC_P(x)	DatumGetHalfVector(PG_GETARG_DATUM(x))
#define PG_RETURN_HALFVEC_P(x)	PG_RETURN_POINTER(x)

typedef struct HalfVector
{
	int32		vl_len_;		/* varlena header (do not touch directly!) */
	int16		dim;			/* number of dimensions */
	int16		unused;			/* reserved for future use, always zero */
	half		x[FLEXIBLE_ARRAY_MEMBER];
}			HalfVector;

HalfVector *InitHalfVector(int dim);

#endif
```

## File: `src/hnsw.c`
```c
#include "postgres.h"

#include <float.h>
#include <limits.h>
#include <math.h>

#include "access/amapi.h"
#include "access/genam.h"
#include "access/reloptions.h"
#include "commands/progress.h"
#include "commands/vacuum.h"
#include "fmgr.h"
#include "hnsw.h"
#include "miscadmin.h"
#include "nodes/pg_list.h"
#include "utils/float.h"
#include "utils/guc.h"
#include "utils/relcache.h"
#include "utils/selfuncs.h"
#include "utils/spccache.h"
#include "vector.h"

#if PG_VERSION_NUM < 150000
#define MarkGUCPrefixReserved(x) EmitWarningsOnPlaceholders(x)
#endif

static const struct config_enum_entry hnsw_iterative_scan_options[] = {
	{"off", HNSW_ITERATIVE_SCAN_OFF, false},
	{"relaxed_order", HNSW_ITERATIVE_SCAN_RELAXED, false},
	{"strict_order", HNSW_ITERATIVE_SCAN_STRICT, false},
	{NULL, 0, false}
};

int			hnsw_ef_search;
int			hnsw_iterative_scan;
int			hnsw_max_scan_tuples;
double		hnsw_scan_mem_multiplier;
int			hnsw_lock_tranche_id;
static relopt_kind hnsw_relopt_kind;

/*
 * Assign a tranche ID for our LWLocks. This only needs to be done by one
 * backend, as the tranche ID is remembered in shared memory.
 *
 * This shared memory area is very small, so we just allocate it from the
 * "slop" that PostgreSQL reserves for small allocations like this. If
 * this grows bigger, we should use a shmem_request_hook and
 * RequestAddinShmemSpace() to pre-reserve space for this.
 */
void
HnswInitLockTranche(void)
{
	int		   *tranche_ids;
	bool		found;

	LWLockAcquire(AddinShmemInitLock, LW_EXCLUSIVE);
	tranche_ids = ShmemInitStruct("hnsw LWLock ids",
								  sizeof(int) * 1,
								  &found);
	if (!found)
	{
#if PG_VERSION_NUM >= 190000
		tranche_ids[0] = LWLockNewTrancheId("HnswBuild");
#else
		tranche_ids[0] = LWLockNewTrancheId();
#endif
	}
	hnsw_lock_tranche_id = tranche_ids[0];
	LWLockRelease(AddinShmemInitLock);

#if PG_VERSION_NUM < 190000
	/* Per-backend registration of the tranche ID */
	LWLockRegisterTranche(hnsw_lock_tranche_id, "HnswBuild");
#endif
}

/*
 * Initialize index options and variables
 */
void
HnswInit(void)
{
	if (!process_shared_preload_libraries_in_progress)
		HnswInitLockTranche();

	hnsw_relopt_kind = add_reloption_kind();
	add_int_reloption(hnsw_relopt_kind, "m", "Max number of connections",
					  HNSW_DEFAULT_M, HNSW_MIN_M, HNSW_MAX_M, AccessExclusiveLock);
	add_int_reloption(hnsw_relopt_kind, "ef_construction", "Size of the dynamic candidate list for construction",
					  HNSW_DEFAULT_EF_CONSTRUCTION, HNSW_MIN_EF_CONSTRUCTION, HNSW_MAX_EF_CONSTRUCTION, AccessExclusiveLock);

	DefineCustomIntVariable("hnsw.ef_search", "Sets the size of the dynamic candidate list for search",
							"Valid range is 1..1000.", &hnsw_ef_search,
							HNSW_DEFAULT_EF_SEARCH, HNSW_MIN_EF_SEARCH, HNSW_MAX_EF_SEARCH, PGC_USERSET, 0, NULL, NULL, NULL);

	DefineCustomEnumVariable("hnsw.iterative_scan", "Sets the mode for iterative scans",
							 NULL, &hnsw_iterative_scan,
							 HNSW_ITERATIVE_SCAN_OFF, hnsw_iterative_scan_options, PGC_USERSET, 0, NULL, NULL, NULL);

	/* This is approximate and does not affect the initial scan */
	DefineCustomIntVariable("hnsw.max_scan_tuples", "Sets the max number of tuples to visit for iterative scans",
							NULL, &hnsw_max_scan_tuples,
							20000, 1, INT_MAX, PGC_USERSET, 0, NULL, NULL, NULL);

	/* Same range as hash_mem_multiplier */
	DefineCustomRealVariable("hnsw.scan_mem_multiplier", "Sets the multiple of work_mem to use for iterative scans",
							 NULL, &hnsw_scan_mem_multiplier,
							 1, 1, 1000, PGC_USERSET, 0, NULL, NULL, NULL);

	MarkGUCPrefixReserved("hnsw");
}

/*
 * Get the name of index build phase
 */
static char *
hnswbuildphasename(int64 phasenum)
{
	switch (phasenum)
	{
		case PROGRESS_CREATEIDX_SUBPHASE_INITIALIZE:
			return "initializing";
		case PROGRESS_HNSW_PHASE_LOAD:
			return "loading tuples";
		default:
			return NULL;
	}
}

/*
 * Estimate the cost of an index scan
 */
static void
hnswcostestimate(PlannerInfo *root, IndexPath *path, double loop_count,
				 Cost *indexStartupCost, Cost *indexTotalCost,
				 Selectivity *indexSelectivity, double *indexCorrelation,
				 double *indexPages)
{
	GenericCosts costs;
	int			m;
	double		ratio;
	double		startupPages;
	double		spc_seq_page_cost;
	Relation	index;

	/* Never use index without order */
	if (path->indexorderbys == NIL)
	{
		*indexStartupCost = get_float8_infinity();
		*indexTotalCost = get_float8_infinity();
		*indexSelectivity = 0;
		*indexCorrelation = 0;
		*indexPages = 0;
#if PG_VERSION_NUM >= 180000
		/* See "On disable_cost" thread on pgsql-hackers */
		path->path.disabled_nodes = 2;
#endif
		return;
	}

	MemSet(&costs, 0, sizeof(costs));

	genericcostestimate(root, path, loop_count, &costs);

	index = index_open(path->indexinfo->indexoid, NoLock);
	HnswGetMetaPageInfo(index, &m, NULL);
	index_close(index, NoLock);

	/*
	 * HNSW cost estimation follows a formula that accounts for the total
	 * number of tuples indexed combined with the parameters that most
	 * influence the duration of the index scan, namely: m - the number of
	 * tuples that are scanned in each step of the HNSW graph traversal
	 * ef_search - which influences the total number of steps taken at layer 0
	 *
	 * The source of the vector data can impact how many steps it takes to
	 * converge on the set of vectors to return to the executor. Currently, we
	 * use a hardcoded scaling factor (HNSWScanScalingFactor) to help
	 * influence that, but this could later become a configurable parameter
	 * based on the cost estimations.
	 *
	 * The tuple estimator formula is below:
	 *
	 * numIndexTuples = entryLevel * m + layer0TuplesMax * layer0Selectivity
	 *
	 * "entryLevel * m" represents the floor of tuples we need to scan to get
	 * to layer 0 (L0).
	 *
	 * "layer0TuplesMax" is the estimated total number of tuples we'd scan at
	 * L0 if we weren't discarding already visited tuples as part of the scan.
	 *
	 * "layer0Selectivity" estimates the percentage of tuples that are scanned
	 * at L0, accounting for previously visited tuples, multiplied by the
	 * "scalingFactor" (currently hardcoded).
	 */
	if (path->indexinfo->tuples > 0)
	{
		double		scalingFactor = 0.55;
		int			entryLevel = (int) (log(path->indexinfo->tuples) * HnswGetMl(m));
		int			layer0TuplesMax = HnswGetLayerM(m, 0) * hnsw_ef_search;
		double		layer0Selectivity = scalingFactor * log(path->indexinfo->tuples) / (log(m) * (1 + log(hnsw_ef_search)));

		ratio = (entryLevel * m + layer0TuplesMax * layer0Selectivity) / path->indexinfo->tuples;

		if (ratio > 1)
			ratio = 1;
	}
	else
		ratio = 1;

	get_tablespace_page_costs(path->indexinfo->reltablespace, NULL, &spc_seq_page_cost);

	/* Startup cost is cost before returning the first row */
	costs.indexStartupCost = costs.indexTotalCost * ratio;

	/* Adjust cost if needed since TOAST not included in seq scan cost */
	startupPages = costs.numIndexPages * ratio;
	if (startupPages > path->indexinfo->rel->pages && ratio < 0.5)
	{
		/* Change all page cost from random to sequential */
		costs.indexStartupCost -= startupPages * (costs.spc_random_page_cost - spc_seq_page_cost);

		/* Remove cost of extra pages */
		costs.indexStartupCost -= (startupPages - path->indexinfo->rel->pages) * spc_seq_page_cost;
	}

	*indexStartupCost = costs.indexStartupCost;
	*indexTotalCost = costs.indexTotalCost;
	*indexSelectivity = costs.indexSelectivity;
	*indexCorrelation = costs.indexCorrelation;
	*indexPages = costs.numIndexPages;
}

/*
 * Parse and validate the reloptions
 */
static bytea *
hnswoptions(Datum reloptions, bool validate)
{
	static const relopt_parse_elt tab[] = {
		{"m", RELOPT_TYPE_INT, offsetof(HnswOptions, m)},
		{"ef_construction", RELOPT_TYPE_INT, offsetof(HnswOptions, efConstruction)},
	};

	return (bytea *) build_reloptions(reloptions, validate,
									  hnsw_relopt_kind,
									  sizeof(HnswOptions),
									  tab, lengthof(tab));
}

/*
 * Validate catalog entries for the specified operator class
 */
static bool
hnswvalidate(Oid opclassoid)
{
	return true;
}

/*
 * Define index handler
 *
 * See https://www.postgresql.org/docs/current/index-api.html
 */
FUNCTION_PREFIX PG_FUNCTION_INFO_V1(hnswhandler);
Datum
hnswhandler(PG_FUNCTION_ARGS)
{
#if PG_VERSION_NUM >= 190000
	static const IndexAmRoutine amroutine = {
		.type = T_IndexAmRoutine,
		.amstrategies = 0,
		.amsupport = 3,
		.amoptsprocnum = 0,
		.amcanorder = false,
		.amcanorderbyop = true,
		.amcanhash = false,
		.amconsistentequality = false,
		.amconsistentordering = false,
		.amcanbackward = false,
		.amcanunique = false,
		.amcanmulticol = false,
		.amoptionalkey = true,
		.amsearcharray = false,
		.amsearchnulls = false,
		.amstorage = false,
		.amclusterable = false,
		.ampredlocks = false,
		.amcanparallel = false,
		.amcanbuildparallel = true,
		.amcaninclude = false,
		.amusemaintenanceworkmem = false,
		.amsummarizing = false,
		.amparallelvacuumoptions = VACUUM_OPTION_PARALLEL_BULKDEL,
		.amkeytype = InvalidOid,

		.ambuild = hnswbuild,
		.ambuildempty = hnswbuildempty,
		.aminsert = hnswinsert,
		.aminsertcleanup = NULL,
		.ambulkdelete = hnswbulkdelete,
		.amvacuumcleanup = hnswvacuumcleanup,
		.amcanreturn = NULL,
		.amcostestimate = hnswcostestimate,
		.amgettreeheight = NULL,
		.amoptions = hnswoptions,
		.amproperty = NULL,
		.ambuildphasename = hnswbuildphasename,
		.amvalidate = hnswvalidate,
		.amadjustmembers = NULL,
		.ambeginscan = hnswbeginscan,
		.amrescan = hnswrescan,
		.amgettuple = hnswgettuple,
		.amgetbitmap = NULL,
		.amendscan = hnswendscan,
		.ammarkpos = NULL,
		.amrestrpos = NULL,
		.amestimateparallelscan = NULL,
		.aminitparallelscan = NULL,
		.amparallelrescan = NULL,
		.amtranslatestrategy = NULL,
		.amtranslatecmptype = NULL,
	};

	PG_RETURN_POINTER(&amroutine);
#else
	IndexAmRoutine *amroutine = makeNode(IndexAmRoutine);

	amroutine->amstrategies = 0;
	amroutine->amsupport = 3;
	amroutine->amoptsprocnum = 0;
	amroutine->amcanorder = false;
	amroutine->amcanorderbyop = true;
#if PG_VERSION_NUM >= 180000
	amroutine->amcanhash = false;
	amroutine->amconsistentequality = false;
	amroutine->amconsistentordering = false;
#endif
	amroutine->amcanbackward = false;	/* can change direction mid-scan */
	amroutine->amcanunique = false;
	amroutine->amcanmulticol = false;
	amroutine->amoptionalkey = true;
	amroutine->amsearcharray = false;
	amroutine->amsearchnulls = false;
	amroutine->amstorage = false;
	amroutine->amclusterable = false;
	amroutine->ampredlocks = false;
	amroutine->amcanparallel = false;
#if PG_VERSION_NUM >= 170000
	amroutine->amcanbuildparallel = true;
#endif
	amroutine->amcaninclude = false;
	amroutine->amusemaintenanceworkmem = false; /* not used during VACUUM */
#if PG_VERSION_NUM >= 160000
	amroutine->amsummarizing = false;
#endif
	amroutine->amparallelvacuumoptions = VACUUM_OPTION_PARALLEL_BULKDEL;
	amroutine->amkeytype = InvalidOid;

	/* Interface functions */
	amroutine->ambuild = hnswbuild;
	amroutine->ambuildempty = hnswbuildempty;
	amroutine->aminsert = hnswinsert;
#if PG_VERSION_NUM >= 170000
	amroutine->aminsertcleanup = NULL;
#endif
	amroutine->ambulkdelete = hnswbulkdelete;
	amroutine->amvacuumcleanup = hnswvacuumcleanup;
	amroutine->amcanreturn = NULL;
	amroutine->amcostestimate = hnswcostestimate;
#if PG_VERSION_NUM >= 180000
	amroutine->amgettreeheight = NULL;
#endif
	amroutine->amoptions = hnswoptions;
	amroutine->amproperty = NULL;	/* TODO AMPROP_DISTANCE_ORDERABLE */
	amroutine->ambuildphasename = hnswbuildphasename;
	amroutine->amvalidate = hnswvalidate;
#if PG_VERSION_NUM >= 140000
	amroutine->amadjustmembers = NULL;
#endif
	amroutine->ambeginscan = hnswbeginscan;
	amroutine->amrescan = hnswrescan;
	amroutine->amgettuple = hnswgettuple;
	amroutine->amgetbitmap = NULL;
	amroutine->amendscan = hnswendscan;
	amroutine->ammarkpos = NULL;
	amroutine->amrestrpos = NULL;

	/* Interface functions to support parallel index scans */
	amroutine->amestimateparallelscan = NULL;
	amroutine->aminitparallelscan = NULL;
	amroutine->amparallelrescan = NULL;

#if PG_VERSION_NUM >= 180000
	amroutine->amtranslatestrategy = NULL;
	amroutine->amtranslatecmptype = NULL;
#endif

	PG_RETURN_POINTER(amroutine);
#endif
}
```

## File: `src/hnsw.h`
```c
#ifndef HNSW_H
#define HNSW_H

#include "postgres.h"

#include <math.h>

#include "access/genam.h"
#include "access/parallel.h"
#include "lib/pairingheap.h"
#include "nodes/execnodes.h"
#include "port.h"				/* for random() */
#include "utils/relptr.h"
#include "utils/sampling.h"
#include "vector.h"

#if PG_VERSION_NUM >= 190000
typedef Pointer Item;
#endif

#define HNSW_MAX_DIM 2000
#define HNSW_MAX_NNZ 1000

/* Support functions */
#define HNSW_DISTANCE_PROC 1
#define HNSW_NORM_PROC 2
#define HNSW_TYPE_INFO_PROC 3

#define HNSW_VERSION	1
#define HNSW_MAGIC_NUMBER 0xA953A953
#define HNSW_PAGE_ID	0xFF90

/* Preserved page numbers */
#define HNSW_METAPAGE_BLKNO	0
#define HNSW_HEAD_BLKNO		1	/* first element page */

/* Must correspond to page numbers since page lock is used */
#define HNSW_UPDATE_LOCK 	0
#define HNSW_SCAN_LOCK		1

/* HNSW parameters */
#define HNSW_DEFAULT_M	16
#define HNSW_MIN_M	2
#define HNSW_MAX_M		100
#define HNSW_DEFAULT_EF_CONSTRUCTION	64
#define HNSW_MIN_EF_CONSTRUCTION	4
#define HNSW_MAX_EF_CONSTRUCTION		1000
#define HNSW_DEFAULT_EF_SEARCH	40
#define HNSW_MIN_EF_SEARCH		1
#define HNSW_MAX_EF_SEARCH		1000

/* Tuple types */
#define HNSW_ELEMENT_TUPLE_TYPE  1
#define HNSW_NEIGHBOR_TUPLE_TYPE 2

/* Make graph robust against non-HOT updates */
#define HNSW_HEAPTIDS 10

#define HNSW_UPDATE_ENTRY_GREATER 1
#define HNSW_UPDATE_ENTRY_ALWAYS 2

/* Build phases */
/* PROGRESS_CREATEIDX_SUBPHASE_INITIALIZE is 1 */
#define PROGRESS_HNSW_PHASE_LOAD		2

#define HNSW_MAX_SIZE (BLCKSZ - MAXALIGN(SizeOfPageHeaderData) - MAXALIGN(sizeof(HnswPageOpaqueData)) - sizeof(ItemIdData))
#define HNSW_TUPLE_ALLOC_SIZE BLCKSZ

#define HNSW_ELEMENT_TUPLE_SIZE(size)	MAXALIGN(offsetof(HnswElementTupleData, data) + (size))
#define HNSW_NEIGHBOR_TUPLE_SIZE(level, m)	MAXALIGN(offsetof(HnswNeighborTupleData, indextids) + ((level) + 2) * (m) * sizeof(ItemPointerData))

#define HNSW_NEIGHBOR_ARRAY_SIZE(lm)	(offsetof(HnswNeighborArray, items) + sizeof(HnswCandidate) * (lm))

#define HnswPageGetOpaque(page)	((HnswPageOpaque) PageGetSpecialPointer(page))
#define HnswPageGetMeta(page)	((HnswMetaPageData *) PageGetContents(page))

#if PG_VERSION_NUM >= 150000
#define RandomDouble() pg_prng_double(&pg_global_prng_state)
#define SeedRandom(seed) pg_prng_seed(&pg_global_prng_state, seed)
#else
#define RandomDouble() (((double) random()) / MAX_RANDOM_VALUE)
#define SeedRandom(seed) srandom(seed)
#endif

#define HnswIsElementTuple(tup) ((tup)->type == HNSW_ELEMENT_TUPLE_TYPE)
#define HnswIsNeighborTuple(tup) ((tup)->type == HNSW_NEIGHBOR_TUPLE_TYPE)

/* 2 * M connections for ground layer */
#define HnswGetLayerM(m, layer) (layer == 0 ? (m) * 2 : (m))

/* Optimal ML from paper */
#define HnswGetMl(m) (1 / log(m))

/* Ensure fits on page and in uint8 */
#define HnswGetMaxLevel(m) Min(((BLCKSZ - MAXALIGN(SizeOfPageHeaderData) - MAXALIGN(sizeof(HnswPageOpaqueData)) - offsetof(HnswNeighborTupleData, indextids) - sizeof(ItemIdData)) / (sizeof(ItemPointerData)) / (m)) - 2, 255)

#define HnswGetSearchCandidate(membername, ptr) pairingheap_container(HnswSearchCandidate, membername, ptr)
#define HnswGetSearchCandidateConst(membername, ptr) pairingheap_const_container(HnswSearchCandidate, membername, ptr)

#define HnswGetValue(base, element) PointerGetDatum(HnswPtrAccess(base, (element)->value))

#if PG_VERSION_NUM < 140005
#define relptr_offset(rp) ((rp).relptr_off - 1)
#endif

/* Pointer macros */
#define HnswPtrAccess(base, hp) ((base) == NULL ? (hp).ptr : relptr_access(base, (hp).relptr))
#define HnswPtrStore(base, hp, value) ((base) == NULL ? (void) ((hp).ptr = (value)) : (void) relptr_store(base, (hp).relptr, value))
#define HnswPtrIsNull(base, hp) ((base) == NULL ? (hp).ptr == NULL : relptr_is_null((hp).relptr))
#define HnswPtrEqual(base, hp1, hp2) ((base) == NULL ? (hp1).ptr == (hp2).ptr : relptr_offset((hp1).relptr) == relptr_offset((hp2).relptr))

/* For code paths dedicated to each type */
#define HnswPtrPointer(hp) (hp).ptr
#define HnswPtrOffset(hp) relptr_offset((hp).relptr)

/* Variables */
extern int	hnsw_ef_search;
extern int	hnsw_iterative_scan;
extern int	hnsw_max_scan_tuples;
extern double hnsw_scan_mem_multiplier;
extern int	hnsw_lock_tranche_id;

typedef enum HnswIterativeScanMode
{
	HNSW_ITERATIVE_SCAN_OFF,
	HNSW_ITERATIVE_SCAN_RELAXED,
	HNSW_ITERATIVE_SCAN_STRICT
}			HnswIterativeScanMode;

typedef struct HnswElementData HnswElementData;
typedef struct HnswNeighborArray HnswNeighborArray;

#define HnswPtrDeclare(type, relptrtype, ptrtype) \
	relptr_declare(type, relptrtype); \
	typedef union { type *ptr; relptrtype relptr; } ptrtype

/* Pointers that can be absolute or relative */
/* Use char for DatumPtr so works with Pointer */
HnswPtrDeclare(HnswElementData, HnswElementRelptr, HnswElementPtr);
HnswPtrDeclare(HnswNeighborArray, HnswNeighborArrayRelptr, HnswNeighborArrayPtr);
HnswPtrDeclare(HnswNeighborArrayPtr, HnswNeighborsRelptr, HnswNeighborsPtr);
HnswPtrDeclare(char, DatumRelptr, DatumPtr);

struct HnswElementData
{
	HnswElementPtr next;
	ItemPointerData heaptids[HNSW_HEAPTIDS];
	uint8		heaptidsLength;
	uint8		level;
	uint8		deleted;
	uint8		version;
	uint32		hash;
	HnswNeighborsPtr neighbors;
	BlockNumber blkno;
	OffsetNumber offno;
	OffsetNumber neighborOffno;
	BlockNumber neighborPage;
	DatumPtr	value;
	LWLock		lock;
};

typedef HnswElementData * HnswElement;

typedef struct HnswCandidate
{
	HnswElementPtr element;
	float		distance;
	bool		closer;
}			HnswCandidate;

struct HnswNeighborArray
{
	int			length;
	bool		closerSet;
	HnswCandidate items[FLEXIBLE_ARRAY_MEMBER];
};

typedef struct HnswSearchCandidate
{
	pairingheap_node c_node;
	pairingheap_node w_node;
	HnswElementPtr element;
	double		distance;
}			HnswSearchCandidate;

/* HNSW index options */
typedef struct HnswOptions
{
	int32		vl_len_;		/* varlena header (do not touch directly!) */
	int			m;				/* number of connections */
	int			efConstruction; /* size of dynamic candidate list */
}			HnswOptions;

typedef struct HnswGraph
{
	/* Graph state */
	slock_t		lock;
	HnswElementPtr head;
	double		indtuples;

	/* Entry state */
	LWLock		entryLock;
	LWLock		entryWaitLock;
	HnswElementPtr entryPoint;

	/* Allocations state */
	LWLock		allocatorLock;
	Size		memoryUsed;
	Size		memoryTotal;

	/* Flushed state */
	LWLock		flushLock;
	bool		flushed;
}			HnswGraph;

typedef struct HnswShared
{
	/* Immutable state */
	Oid			heaprelid;
	Oid			indexrelid;
	bool		isconcurrent;

	/* Worker progress */
	ConditionVariable workersdonecv;

	/* Mutex for mutable state */
	slock_t		mutex;

	/* Mutable state */
	int			nparticipantsdone;
	double		reltuples;
	HnswGraph	graphData;
}			HnswShared;

#define ParallelTableScanFromHnswShared(shared) \
	(ParallelTableScanDesc) ((char *) (shared) + BUFFERALIGN(sizeof(HnswShared)))

typedef struct HnswLeader
{
	ParallelContext *pcxt;
	int			nparticipanttuplesorts;
	HnswShared *hnswshared;
	Snapshot	snapshot;
	char	   *hnswarea;
}			HnswLeader;

typedef struct HnswAllocator
{
	void	   *(*alloc) (Size size, void *state);
	void	   *state;
}			HnswAllocator;

typedef struct HnswTypeInfo
{
	int			maxDimensions;
	Datum		(*normalize) (PG_FUNCTION_ARGS);
	void		(*checkValue) (Pointer v);
}			HnswTypeInfo;

typedef struct HnswSupport
{
	FmgrInfo   *procinfo;
	FmgrInfo   *normprocinfo;
	Oid			collation;
}			HnswSupport;

typedef struct HnswQuery
{
	Datum		value;
}			HnswQuery;

typedef struct HnswBuildState
{
	/* Info */
	Relation	heap;
	Relation	index;
	IndexInfo  *indexInfo;
	ForkNumber	forkNum;
	const		HnswTypeInfo *typeInfo;

	/* Settings */
	int			dimensions;
	int			m;
	int			efConstruction;

	/* Statistics */
	double		indtuples;
	double		reltuples;

	/* Support functions */
	HnswSupport support;

	/* Variables */
	HnswGraph	graphData;
	HnswGraph  *graph;
	double		ml;
	int			maxLevel;

	/* Memory */
	MemoryContext graphCtx;
	MemoryContext tmpCtx;
	HnswAllocator allocator;

	/* Parallel builds */
	HnswLeader *hnswleader;
	HnswShared *hnswshared;
	char	   *hnswarea;
}			HnswBuildState;

typedef struct HnswMetaPageData
{
	uint32		magicNumber;
	uint32		version;
	uint32		dimensions;
	uint16		m;
	uint16		efConstruction;
	BlockNumber entryBlkno;
	OffsetNumber entryOffno;
	int16		entryLevel;
	BlockNumber insertPage;
}			HnswMetaPageData;

typedef HnswMetaPageData * HnswMetaPage;

typedef struct HnswPageOpaqueData
{
	BlockNumber nextblkno;
	uint16		unused;
	uint16		page_id;		/* for identification of HNSW indexes */
}			HnswPageOpaqueData;

typedef HnswPageOpaqueData * HnswPageOpaque;

typedef struct HnswElementTupleData
{
	uint8		type;
	uint8		level;
	uint8		deleted;
	uint8		version;
	ItemPointerData heaptids[HNSW_HEAPTIDS];
	ItemPointerData neighbortid;
	uint16		unused;
	Vector		data;
}			HnswElementTupleData;

typedef HnswElementTupleData * HnswElementTuple;

typedef struct HnswNeighborTupleData
{
	uint8		type;
	uint8		version;
	uint16		count;
	ItemPointerData indextids[FLEXIBLE_ARRAY_MEMBER];
}			HnswNeighborTupleData;

typedef HnswNeighborTupleData * HnswNeighborTuple;

typedef union
{
	struct pointerhash_hash *pointers;
	struct offsethash_hash *offsets;
	struct tidhash_hash *tids;
}			visited_hash;

typedef union
{
	HnswElement element;
	ItemPointerData indextid;
}			HnswUnvisited;

typedef struct HnswScanOpaqueData
{
	const		HnswTypeInfo *typeInfo;
	bool		first;
	List	   *w;
	visited_hash v;
	pairingheap *discarded;
	HnswQuery	q;
	int			m;
	int64		tuples;
	double		previousDistance;
	Size		maxMemory;
	MemoryContext tmpCtx;

	/* Support functions */
	HnswSupport support;
}			HnswScanOpaqueData;

typedef HnswScanOpaqueData * HnswScanOpaque;

typedef struct HnswVacuumState
{
	/* Info */
	Relation	index;
	IndexBulkDeleteResult *stats;
	IndexBulkDeleteCallback callback;
	void	   *callback_state;

	/* Settings */
	int			m;
	int			efConstruction;

	/* Support functions */
	HnswSupport support;

	/* Variables */
	struct tidhash_hash *deleted;
	BufferAccessStrategy bas;
	HnswNeighborTuple ntup;
	HnswElementData highestPoint;

	/* Memory */
	MemoryContext tmpCtx;
}			HnswVacuumState;

/* Methods */
int			HnswGetM(Relation index);
int			HnswGetEfConstruction(Relation index);
FmgrInfo   *HnswOptionalProcInfo(Relation index, uint16 procnum);
void		HnswInitSupport(HnswSupport * support, Relation index);
Datum		HnswNormValue(const HnswTypeInfo * typeInfo, Oid collation, Datum value);
bool		HnswCheckNorm(HnswSupport * support, Datum value);
Buffer		HnswNewBuffer(Relation index, ForkNumber forkNum);
void		HnswInitPage(Buffer buf, Page page);
void		HnswInit(void);
List	   *HnswSearchLayer(char *base, HnswQuery * q, List *ep, int ef, int lc, Relation index, HnswSupport * support, int m, bool inserting, HnswElement skipElement, visited_hash * v, pairingheap **discarded, bool initVisited, int64 *tuples);
HnswElement HnswGetEntryPoint(Relation index);
void		HnswGetMetaPageInfo(Relation index, int *m, HnswElement * entryPoint);
void	   *HnswAlloc(HnswAllocator * allocator, Size size);
HnswElement HnswInitElement(char *base, ItemPointer tid, int m, double ml, int maxLevel, HnswAllocator * alloc);
HnswElement HnswInitElementFromBlock(BlockNumber blkno, OffsetNumber offno);
void		HnswFindElementNeighbors(char *base, HnswElement element, HnswElement entryPoint, Relation index, HnswSupport * support, int m, int efConstruction, bool existing);
HnswSearchCandidate *HnswEntryCandidate(char *base, HnswElement entryPoint, HnswQuery * q, Relation index, HnswSupport * support, bool loadVec);
void		HnswUpdateMetaPage(Relation index, int updateEntry, HnswElement entryPoint, BlockNumber insertPage, ForkNumber forkNum, bool building);
void		HnswSetNeighborTuple(char *base, HnswNeighborTuple ntup, HnswElement e, int m);
void		HnswAddHeapTid(HnswElement element, ItemPointer heaptid);
HnswNeighborArray *HnswInitNeighborArray(int lm, HnswAllocator * allocator);
void		HnswInitNeighbors(char *base, HnswElement element, int m, HnswAllocator * alloc);
bool		HnswInsertTupleOnDisk(Relation index, HnswSupport * support, Datum value, ItemPointer heaptid, bool building);
void		HnswUpdateNeighborsOnDisk(Relation index, HnswSupport * support, HnswElement e, int m, bool checkExisting, bool building);
void		HnswLoadElementFromTuple(HnswElement element, HnswElementTuple etup, bool loadHeaptids, bool loadVec);
void		HnswLoadElement(HnswElement element, double *distance, HnswQuery * q, Relation index, HnswSupport * support, bool loadVec, double *maxDistance);
bool		HnswFormIndexValue(Datum *out, Datum *values, bool *isnull, const HnswTypeInfo * typeInfo, HnswSupport * support);
void		HnswSetElementTuple(char *base, HnswElementTuple etup, HnswElement element);
void		HnswUpdateConnection(char *base, HnswNeighborArray * neighbors, HnswElement newElement, float distance, int lm, int *updateIdx, Relation index, HnswSupport * support);
bool		HnswLoadNeighborTids(HnswElement element, ItemPointerData *indextids, Relation index, int m, int lm, int lc);
void		HnswInitLockTranche(void);
const		HnswTypeInfo *HnswGetTypeInfo(Relation index);
PGDLLEXPORT void HnswParallelBuildMain(dsm_segment *seg, shm_toc *toc);

/* Index access methods */
IndexBuildResult *hnswbuild(Relation heap, Relation index, IndexInfo *indexInfo);
void		hnswbuildempty(Relation index);
bool		hnswinsert(Relation index, Datum *values, bool *isnull, ItemPointer heap_tid, Relation heap, IndexUniqueCheck checkUnique
#if PG_VERSION_NUM >= 140000
					   ,bool indexUnchanged
#endif
					   ,IndexInfo *indexInfo
);
IndexBulkDeleteResult *hnswbulkdelete(IndexVacuumInfo *info, IndexBulkDeleteResult *stats, IndexBulkDeleteCallback callback, void *callback_state);
IndexBulkDeleteResult *hnswvacuumcleanup(IndexVacuumInfo *info, IndexBulkDeleteResult *stats);
IndexScanDesc hnswbeginscan(Relation index, int nkeys, int norderbys);
void		hnswrescan(IndexScanDesc scan, ScanKey keys, int nkeys, ScanKey orderbys, int norderbys);
bool		hnswgettuple(IndexScanDesc scan, ScanDirection dir);
void		hnswendscan(IndexScanDesc scan);

static inline HnswNeighborArray *
HnswGetNeighbors(char *base, HnswElement element, int lc)
{
	HnswNeighborArrayPtr *neighborList = HnswPtrAccess(base, element->neighbors);

	Assert(element->level >= lc);

	return HnswPtrAccess(base, neighborList[lc]);
}

/* Hash tables */
typedef struct TidHashEntry
{
	ItemPointerData tid;
	char		status;
}			TidHashEntry;

#define SH_PREFIX tidhash
#define SH_ELEMENT_TYPE TidHashEntry
#define SH_KEY_TYPE ItemPointerData
#define SH_SCOPE extern
#define SH_DECLARE
#include "lib/simplehash.h"

typedef struct PointerHashEntry
{
	uintptr_t	ptr;
	char		status;
}			PointerHashEntry;

#define SH_PREFIX pointerhash
#define SH_ELEMENT_TYPE PointerHashEntry
#define SH_KEY_TYPE uintptr_t
#define SH_SCOPE extern
#define SH_DECLARE
#include "lib/simplehash.h"

typedef struct OffsetHashEntry
{
	Size		offset;
	char		status;
}			OffsetHashEntry;

#define SH_PREFIX offsethash
#define SH_ELEMENT_TYPE OffsetHashEntry
#define SH_KEY_TYPE Size
#define SH_SCOPE extern
#define SH_DECLARE
#include "lib/simplehash.h"

#endif
```

## File: `src/hnswbuild.c`
```c
/*
 * The HNSW build happens in two phases:
 *
 * 1. In-memory phase
 *
 * In this first phase, the graph is held completely in memory. When the graph
 * is fully built, or we run out of memory reserved for the build (determined
 * by maintenance_work_mem), we materialize the graph to disk (see
 * FlushPages()), and switch to the on-disk phase.
 *
 * In a parallel build, a large contiguous chunk of shared memory is allocated
 * to hold the graph. Each worker process has its own HnswBuildState struct in
 * private memory, which contains information that doesn't change throughout
 * the build, and pointers to the shared structs in shared memory. The shared
 * memory area is mapped to a different address in each worker process, and
 * 'HnswBuildState.hnswarea' points to the beginning of the shared area in the
 * worker process's address space. All pointers used in the graph are
 * "relative pointers", stored as an offset from 'hnswarea'.
 *
 * Each element is protected by an LWLock. It must be held when reading or
 * modifying the element's neighbors or 'heaptids'.
 *
 * In a non-parallel build, the graph is held in backend-private memory. All
 * the elements are allocated in a dedicated memory context, 'graphCtx', and
 * the pointers used in the graph are regular pointers.
 *
 * 2. On-disk phase
 *
 * In the on-disk phase, the index is built by inserting each vector to the
 * index one by one, just like on INSERT. The only difference is that we don't
 * WAL-log the individual inserts. If the graph fit completely in memory and
 * was fully built in the in-memory phase, the on-disk phase is skipped.
 *
 * After we have finished building the graph, we perform one more scan through
 * the index and write all the pages to the WAL.
 */
#include "postgres.h"

#include <limits.h>

#include "access/genam.h"
#include "access/parallel.h"
#include "access/relscan.h"
#include "access/table.h"
#include "access/tableam.h"
#include "access/tupdesc.h"
#include "access/xact.h"
#include "access/xloginsert.h"
#include "catalog/index.h"
#include "catalog/pg_type_d.h"
#include "commands/progress.h"
#include "hnsw.h"
#include "miscadmin.h"
#include "nodes/execnodes.h"
#include "optimizer/optimizer.h"
#include "storage/bufmgr.h"
#include "tcop/tcopprot.h"
#include "utils/datum.h"
#include "utils/memutils.h"
#include "utils/rel.h"
#include "utils/snapmgr.h"

#if PG_VERSION_NUM >= 160000
#include "varatt.h"
#endif

#if PG_VERSION_NUM >= 140000
#include "utils/backend_progress.h"
#else
#include "pgstat.h"
#endif

#if PG_VERSION_NUM >= 140000
#include "utils/backend_status.h"
#include "utils/wait_event.h"
#endif

#define PARALLEL_KEY_HNSW_SHARED		UINT64CONST(0xA000000000000001)
#define PARALLEL_KEY_HNSW_AREA			UINT64CONST(0xA000000000000002)
#define PARALLEL_KEY_QUERY_TEXT			UINT64CONST(0xA000000000000003)

#define HNSW_MAX_GRAPH_MEMORY (SIZE_MAX / 2)

/*
 * Create the metapage
 */
static void
CreateMetaPage(HnswBuildState * buildstate)
{
	Relation	index = buildstate->index;
	ForkNumber	forkNum = buildstate->forkNum;
	Buffer		buf;
	Page		page;
	HnswMetaPage metap;

	buf = HnswNewBuffer(index, forkNum);
	page = BufferGetPage(buf);
	HnswInitPage(buf, page);

	/* Set metapage data */
	metap = HnswPageGetMeta(page);
	metap->magicNumber = HNSW_MAGIC_NUMBER;
	metap->version = HNSW_VERSION;
	metap->dimensions = buildstate->dimensions;
	metap->m = buildstate->m;
	metap->efConstruction = buildstate->efConstruction;
	metap->entryBlkno = InvalidBlockNumber;
	metap->entryOffno = InvalidOffsetNumber;
	metap->entryLevel = -1;
	metap->insertPage = InvalidBlockNumber;
	((PageHeader) page)->pd_lower =
		((char *) metap + sizeof(HnswMetaPageData)) - (char *) page;

	MarkBufferDirty(buf);
	UnlockReleaseBuffer(buf);
}

/*
 * Add a new page
 */
static void
HnswBuildAppendPage(Relation index, Buffer *buf, Page *page, ForkNumber forkNum)
{
	/* Add a new page */
	Buffer		newbuf = HnswNewBuffer(index, forkNum);

	/* Update previous page */
	HnswPageGetOpaque(*page)->nextblkno = BufferGetBlockNumber(newbuf);

	/* Commit */
	MarkBufferDirty(*buf);
	UnlockReleaseBuffer(*buf);

	/* Can take a while, so ensure we can interrupt */
	/* Needs to be called when no buffer locks are held */
	LockBuffer(newbuf, BUFFER_LOCK_UNLOCK);
	CHECK_FOR_INTERRUPTS();
	LockBuffer(newbuf, BUFFER_LOCK_EXCLUSIVE);

	/* Prepare new page */
	*buf = newbuf;
	*page = BufferGetPage(*buf);
	HnswInitPage(*buf, *page);
}

/*
 * Create graph pages
 */
static void
CreateGraphPages(HnswBuildState * buildstate)
{
	Relation	index = buildstate->index;
	ForkNumber	forkNum = buildstate->forkNum;
	Size		maxSize;
	HnswElementTuple etup;
	HnswNeighborTuple ntup;
	BlockNumber insertPage;
	HnswElement entryPoint;
	Buffer		buf;
	Page		page;
	HnswElementPtr iter = buildstate->graph->head;
	char	   *base = buildstate->hnswarea;

	/* Calculate sizes */
	maxSize = HNSW_MAX_SIZE;

	/* Allocate once */
	etup = palloc0(HNSW_TUPLE_ALLOC_SIZE);
	ntup = palloc0(HNSW_TUPLE_ALLOC_SIZE);

	/* Prepare first page */
	buf = HnswNewBuffer(index, forkNum);
	page = BufferGetPage(buf);
	HnswInitPage(buf, page);

	while (!HnswPtrIsNull(base, iter))
	{
		HnswElement element = HnswPtrAccess(base, iter);
		Size		etupSize;
		Size		ntupSize;
		Size		combinedSize;
		Pointer		valuePtr = HnswPtrAccess(base, element->value);

		/* Update iterator */
		iter = element->next;

		/* Zero memory for each element */
		MemSet(etup, 0, HNSW_TUPLE_ALLOC_SIZE);

		/* Calculate sizes */
		etupSize = HNSW_ELEMENT_TUPLE_SIZE(VARSIZE_ANY(valuePtr));
		ntupSize = HNSW_NEIGHBOR_TUPLE_SIZE(element->level, buildstate->m);
		combinedSize = etupSize + ntupSize + sizeof(ItemIdData);

		/* Initial size check */
		if (etupSize > HNSW_TUPLE_ALLOC_SIZE)
			ereport(ERROR,
					(errcode(ERRCODE_PROGRAM_LIMIT_EXCEEDED),
					 errmsg("index tuple too large")));

		HnswSetElementTuple(base, etup, element);

		/* Keep element and neighbors on the same page if possible */
		if (PageGetFreeSpace(page) < etupSize || (combinedSize <= maxSize && PageGetFreeSpace(page) < combinedSize))
			HnswBuildAppendPage(index, &buf, &page, forkNum);

		/* Calculate offsets */
		element->blkno = BufferGetBlockNumber(buf);
		element->offno = OffsetNumberNext(PageGetMaxOffsetNumber(page));
		if (combinedSize <= maxSize)
		{
			element->neighborPage = element->blkno;
			element->neighborOffno = OffsetNumberNext(element->offno);
		}
		else
		{
			element->neighborPage = element->blkno + 1;
			element->neighborOffno = FirstOffsetNumber;
		}

		ItemPointerSet(&etup->neighbortid, element->neighborPage, element->neighborOffno);

		/* Add element */
		if (PageAddItem(page, (Item) etup, etupSize, InvalidOffsetNumber, false, false) != element->offno)
			elog(ERROR, "failed to add index item to \"%s\"", RelationGetRelationName(index));

		/* Add new page if needed */
		if (PageGetFreeSpace(page) < ntupSize)
			HnswBuildAppendPage(index, &buf, &page, forkNum);

		/* Add placeholder for neighbors */
		if (PageAddItem(page, (Item) ntup, ntupSize, InvalidOffsetNumber, false, false) != element->neighborOffno)
			elog(ERROR, "failed to add index item to \"%s\"", RelationGetRelationName(index));
	}

	insertPage = BufferGetBlockNumber(buf);

	/* Commit */
	MarkBufferDirty(buf);
	UnlockReleaseBuffer(buf);

	entryPoint = HnswPtrAccess(base, buildstate->graph->entryPoint);
	HnswUpdateMetaPage(index, HNSW_UPDATE_ENTRY_ALWAYS, entryPoint, insertPage, forkNum, true);

	pfree(etup);
	pfree(ntup);
}

/*
 * Write neighbor tuples
 */
static void
WriteNeighborTuples(HnswBuildState * buildstate)
{
	Relation	index = buildstate->index;
	ForkNumber	forkNum = buildstate->forkNum;
	int			m = buildstate->m;
	HnswElementPtr iter = buildstate->graph->head;
	char	   *base = buildstate->hnswarea;
	HnswNeighborTuple ntup;

	/* Allocate once */
	ntup = palloc0(HNSW_TUPLE_ALLOC_SIZE);

	while (!HnswPtrIsNull(base, iter))
	{
		HnswElement element = HnswPtrAccess(base, iter);
		Buffer		buf;
		Page		page;
		Size		ntupSize = HNSW_NEIGHBOR_TUPLE_SIZE(element->level, m);

		/* Update iterator */
		iter = element->next;

		/* Zero memory for each element */
		MemSet(ntup, 0, HNSW_TUPLE_ALLOC_SIZE);

		/* Can take a while, so ensure we can interrupt */
		/* Needs to be called when no buffer locks are held */
		CHECK_FOR_INTERRUPTS();

		buf = ReadBufferExtended(index, forkNum, element->neighborPage, RBM_NORMAL, NULL);
		LockBuffer(buf, BUFFER_LOCK_EXCLUSIVE);
		page = BufferGetPage(buf);

		HnswSetNeighborTuple(base, ntup, element, m);

		if (!PageIndexTupleOverwrite(page, element->neighborOffno, (Item) ntup, ntupSize))
			elog(ERROR, "failed to add index item to \"%s\"", RelationGetRelationName(index));

		/* Commit */
		MarkBufferDirty(buf);
		UnlockReleaseBuffer(buf);
	}

	pfree(ntup);
}

/*
 * Flush pages
 */
static void
FlushPages(HnswBuildState * buildstate)
{
#ifdef HNSW_MEMORY
	elog(INFO, "memory: %zu MB", buildstate->graph->memoryUsed / (1024 * 1024));
#endif

	CreateMetaPage(buildstate);
	CreateGraphPages(buildstate);
	WriteNeighborTuples(buildstate);

	buildstate->graph->flushed = true;
	MemoryContextReset(buildstate->graphCtx);
}

/*
 * Add a heap TID to an existing element
 */
static bool
AddDuplicateInMemory(HnswElement element, HnswElement dup)
{
	LWLockAcquire(&dup->lock, LW_EXCLUSIVE);

	if (dup->heaptidsLength == HNSW_HEAPTIDS)
	{
		LWLockRelease(&dup->lock);
		return false;
	}

	HnswAddHeapTid(dup, &element->heaptids[0]);

	LWLockRelease(&dup->lock);

	return true;
}

/*
 * Find duplicate element
 */
static bool
FindDuplicateInMemory(char *base, HnswElement element)
{
	HnswNeighborArray *neighbors = HnswGetNeighbors(base, element, 0);
	Datum		value = HnswGetValue(base, element);

	for (int i = 0; i < neighbors->length; i++)
	{
		HnswCandidate *neighbor = &neighbors->items[i];
		HnswElement neighborElement = HnswPtrAccess(base, neighbor->element);
		Datum		neighborValue = HnswGetValue(base, neighborElement);

		/* Exit early since ordered by distance */
		if (!datumIsEqual(value, neighborValue, false, -1))
			return false;

		/* Check for space */
		if (AddDuplicateInMemory(element, neighborElement))
			return true;
	}

	return false;
}

/*
 * Add to element list
 */
static void
AddElementInMemory(char *base, HnswGraph * graph, HnswElement element)
{
	SpinLockAcquire(&graph->lock);
	element->next = graph->head;
	HnswPtrStore(base, graph->head, element);
	SpinLockRelease(&graph->lock);
}

/*
 * Update neighbors
 */
static void
UpdateNeighborsInMemory(char *base, HnswSupport * support, HnswElement e, int m)
{
	for (int lc = e->level; lc >= 0; lc--)
	{
		int			lm = HnswGetLayerM(m, lc);
		Size		neighborsSize = HNSW_NEIGHBOR_ARRAY_SIZE(lm);
		HnswNeighborArray *neighbors = palloc(neighborsSize);

		/* Copy neighbors to local memory */
		LWLockAcquire(&e->lock, LW_SHARED);
		memcpy(neighbors, HnswGetNeighbors(base, e, lc), neighborsSize);
		LWLockRelease(&e->lock);

		for (int i = 0; i < neighbors->length; i++)
		{
			HnswCandidate *hc = &neighbors->items[i];
			HnswElement neighborElement = HnswPtrAccess(base, hc->element);

			/* Keep scan-build happy on Mac x86-64 */
			Assert(neighborElement);

			LWLockAcquire(&neighborElement->lock, LW_EXCLUSIVE);
			HnswUpdateConnection(base, HnswGetNeighbors(base, neighborElement, lc), e, hc->distance, lm, NULL, NULL, support);
			LWLockRelease(&neighborElement->lock);
		}
	}
}

/*
 * Update graph in memory
 */
static void
UpdateGraphInMemory(HnswSupport * support, HnswElement element, int m, HnswElement entryPoint, HnswBuildState * buildstate)
{
	HnswGraph  *graph = buildstate->graph;
	char	   *base = buildstate->hnswarea;

	/* Look for duplicate */
	if (FindDuplicateInMemory(base, element))
		return;

	/* Add element */
	AddElementInMemory(base, graph, element);

	/* Update neighbors */
	UpdateNeighborsInMemory(base, support, element, m);

	/* Update entry point if needed (already have lock) */
	if (entryPoint == NULL || element->level > entryPoint->level)
		HnswPtrStore(base, graph->entryPoint, element);
}

/*
 * Insert tuple in memory
 */
static void
InsertTupleInMemory(HnswBuildState * buildstate, HnswElement element)
{
	HnswGraph  *graph = buildstate->graph;
	HnswSupport *support = &buildstate->support;
	HnswElement entryPoint;
	LWLock	   *entryLock = &graph->entryLock;
	LWLock	   *entryWaitLock = &graph->entryWaitLock;
	int			efConstruction = buildstate->efConstruction;
	int			m = buildstate->m;
	char	   *base = buildstate->hnswarea;

	/* Wait if another process needs exclusive lock on entry lock */
	LWLockAcquire(entryWaitLock, LW_EXCLUSIVE);
	LWLockRelease(entryWaitLock);

	/* Get entry point */
	LWLockAcquire(entryLock, LW_SHARED);
	entryPoint = HnswPtrAccess(base, graph->entryPoint);

	/* Prevent concurrent inserts when likely updating entry point */
	if (entryPoint == NULL || element->level > entryPoint->level)
	{
		/* Release shared lock */
		LWLockRelease(entryLock);

		/* Tell other processes to wait and get exclusive lock */
		LWLockAcquire(entryWaitLock, LW_EXCLUSIVE);
		LWLockAcquire(entryLock, LW_EXCLUSIVE);
		LWLockRelease(entryWaitLock);

		/* Get latest entry point after lock is acquired */
		entryPoint = HnswPtrAccess(base, graph->entryPoint);
	}

	/* Find neighbors for element */
	HnswFindElementNeighbors(base, element, entryPoint, NULL, support, m, efConstruction, false);

	/* Update graph in memory */
	UpdateGraphInMemory(support, element, m, entryPoint, buildstate);

	/* Release entry lock */
	LWLockRelease(entryLock);
}

/*
 * Insert tuple
 */
static bool
InsertTuple(Relation index, Datum *values, bool *isnull, ItemPointer heaptid, HnswBuildState * buildstate)
{
	HnswGraph  *graph = buildstate->graph;
	HnswElement element;
	HnswAllocator *allocator = &buildstate->allocator;
	HnswSupport *support = &buildstate->support;
	Size		valueSize;
	Pointer		valuePtr;
	LWLock	   *flushLock = &graph->flushLock;
	char	   *base = buildstate->hnswarea;
	Datum		value;
	Size		memoryMargin;

	/* Form index value */
	if (!HnswFormIndexValue(&value, values, isnull, buildstate->typeInfo, support))
		return false;

	/* Get datum size */
	valueSize = VARSIZE_ANY(DatumGetPointer(value));

	/* In a parallel build, add a margin so allocations never fail */
	memoryMargin = base == NULL ? 0 : 1024 * 1024;

	/* Ensure graph not flushed when inserting */
	LWLockAcquire(flushLock, LW_SHARED);

	/* Are we in the on-disk phase? */
	if (graph->flushed)
	{
		LWLockRelease(flushLock);

		return HnswInsertTupleOnDisk(index, support, value, heaptid, true);
	}

	/*
	 * In a parallel build, the HnswElement is allocated from the shared
	 * memory area, so we need to coordinate with other processes.
	 */
	LWLockAcquire(&graph->allocatorLock, LW_EXCLUSIVE);

	/*
	 * Check that we have enough memory available for the new element now that
	 * we have the allocator lock, and flush pages if needed.
	 */
	if (graph->memoryUsed + memoryMargin >= graph->memoryTotal)
	{
		LWLockRelease(&graph->allocatorLock);

		LWLockRelease(flushLock);
		LWLockAcquire(flushLock, LW_EXCLUSIVE);

		if (!graph->flushed)
		{
			ereport(NOTICE,
					(errmsg("hnsw graph no longer fits into maintenance_work_mem after " INT64_FORMAT " tuples", (int64) graph->indtuples),
					 errdetail("Building will take significantly more time."),
					 errhint("Increase maintenance_work_mem to speed up builds.")));

			FlushPages(buildstate);
		}

		LWLockRelease(flushLock);

		return HnswInsertTupleOnDisk(index, support, value, heaptid, true);
	}

	/* Ok, we can proceed to allocate the element */
	element = HnswInitElement(base, heaptid, buildstate->m, buildstate->ml, buildstate->maxLevel, allocator);
	valuePtr = HnswAlloc(allocator, valueSize);

	/*
	 * We have now allocated the space needed for the element, so we don't
	 * need the allocator lock anymore. Release it and initialize the rest of
	 * the element.
	 */
	LWLockRelease(&graph->allocatorLock);

	/* Copy the datum */
	memcpy(valuePtr, DatumGetPointer(value), valueSize);
	HnswPtrStore(base, element->value, (char *) valuePtr);

	/* Create a lock for the element */
	LWLockInitialize(&element->lock, hnsw_lock_tranche_id);

	/* Insert tuple */
	InsertTupleInMemory(buildstate, element);

	/* Release flush lock */
	LWLockRelease(flushLock);

	return true;
}

/*
 * Callback for table_index_build_scan
 */
static void
BuildCallback(Relation index, ItemPointer tid, Datum *values,
			  bool *isnull, bool tupleIsAlive, void *state)
{
	HnswBuildState *buildstate = (HnswBuildState *) state;
	HnswGraph  *graph = buildstate->graph;
	MemoryContext oldCtx;

	/* Skip nulls */
	if (isnull[0])
		return;

	/* Use memory context */
	oldCtx = MemoryContextSwitchTo(buildstate->tmpCtx);

	/* Insert tuple */
	if (InsertTuple(index, values, isnull, tid, buildstate))
	{
		/* Update progress */
		SpinLockAcquire(&graph->lock);
		pgstat_progress_update_param(PROGRESS_CREATEIDX_TUPLES_DONE, ++graph->indtuples);
		SpinLockRelease(&graph->lock);
	}

	/* Reset memory context */
	MemoryContextSwitchTo(oldCtx);
	MemoryContextReset(buildstate->tmpCtx);
}

/*
 * Initialize the graph
 */
static void
InitGraph(HnswGraph * graph, char *base, Size memoryTotal)
{
	/* Initialize the lock tranche if needed */
	HnswInitLockTranche();

	HnswPtrStore(base, graph->head, (HnswElement) NULL);
	HnswPtrStore(base, graph->entryPoint, (HnswElement) NULL);
	graph->memoryUsed = 0;
	graph->memoryTotal = Min(memoryTotal, HNSW_MAX_GRAPH_MEMORY);
	graph->flushed = false;
	graph->indtuples = 0;
	SpinLockInit(&graph->lock);
	LWLockInitialize(&graph->entryLock, hnsw_lock_tranche_id);
	LWLockInitialize(&graph->entryWaitLock, hnsw_lock_tranche_id);
	LWLockInitialize(&graph->allocatorLock, hnsw_lock_tranche_id);
	LWLockInitialize(&graph->flushLock, hnsw_lock_tranche_id);
}

/*
 * Initialize an allocator
 */
static void
InitAllocator(HnswAllocator * allocator, void *(*alloc) (Size size, void *state), void *state)
{
	allocator->alloc = alloc;
	allocator->state = state;
}

/*
 * Memory context allocator
 */
static void *
HnswMemoryContextAlloc(Size size, void *state)
{
	HnswBuildState *buildstate = (HnswBuildState *) state;
	void	   *chunk = MemoryContextAlloc(buildstate->graphCtx, size);

	buildstate->graphData.memoryUsed = MemoryContextMemAllocated(buildstate->graphCtx, false);

	return chunk;
}

/*
 * Shared memory allocator
 */
static void *
HnswSharedMemoryAlloc(Size size, void *state)
{
	HnswBuildState *buildstate = (HnswBuildState *) state;
	Size		alignedSize = MAXALIGN(size);
	void	   *chunk;

	if (alignedSize > 1024 * 1024)
		elog(ERROR, "hnsw allocation too large");

	if (buildstate->graph->memoryUsed + alignedSize > buildstate->graph->memoryTotal)
		elog(ERROR, "hnsw allocator out of memory");

	chunk = buildstate->hnswarea + buildstate->graph->memoryUsed;
	buildstate->graph->memoryUsed += alignedSize;
	return chunk;
}

/*
 * Initialize the build state
 */
static void
InitBuildState(HnswBuildState * buildstate, Relation heap, Relation index, IndexInfo *indexInfo, ForkNumber forkNum)
{
	buildstate->heap = heap;
	buildstate->index = index;
	buildstate->indexInfo = indexInfo;
	buildstate->forkNum = forkNum;
	buildstate->typeInfo = HnswGetTypeInfo(index);

	buildstate->m = HnswGetM(index);
	buildstate->efConstruction = HnswGetEfConstruction(index);
	buildstate->dimensions = TupleDescAttr(index->rd_att, 0)->atttypmod;

	/* Disallow varbit since require fixed dimensions */
	if (TupleDescAttr(index->rd_att, 0)->atttypid == VARBITOID)
		ereport(ERROR,
				(errcode(ERRCODE_FEATURE_NOT_SUPPORTED),
				 errmsg("type not supported for hnsw index")));

	/* Require column to have dimensions to be indexed */
	if (buildstate->dimensions < 0)
		ereport(ERROR,
				(errcode(ERRCODE_INVALID_PARAMETER_VALUE),
				 errmsg("column does not have dimensions")));

	if (buildstate->dimensions > buildstate->typeInfo->maxDimensions)
		ereport(ERROR,
				(errcode(ERRCODE_PROGRAM_LIMIT_EXCEEDED),
				 errmsg("column cannot have more than %d dimensions for hnsw index", buildstate->typeInfo->maxDimensions)));

	if (buildstate->efConstruction < 2 * buildstate->m)
		ereport(ERROR,
				(errcode(ERRCODE_INVALID_PARAMETER_VALUE),
				 errmsg("ef_construction must be greater than or equal to 2 * m")));

	buildstate->reltuples = 0;
	buildstate->indtuples = 0;

	/* Get support functions */
	HnswInitSupport(&buildstate->support, index);

	InitGraph(&buildstate->graphData, NULL, (Size) maintenance_work_mem * 1024L);
	buildstate->graph = &buildstate->graphData;
	buildstate->ml = HnswGetMl(buildstate->m);
	buildstate->maxLevel = HnswGetMaxLevel(buildstate->m);

	buildstate->graphCtx = GenerationContextCreate(CurrentMemoryContext,
												   "Hnsw build graph context",
#if PG_VERSION_NUM >= 150000
												   1024 * 1024, 1024 * 1024,
#endif
												   1024 * 1024);
	buildstate->tmpCtx = AllocSetContextCreate(CurrentMemoryContext,
											   "Hnsw build temporary context",
											   ALLOCSET_DEFAULT_SIZES);

	InitAllocator(&buildstate->allocator, &HnswMemoryContextAlloc, buildstate);

	buildstate->hnswleader = NULL;
	buildstate->hnswshared = NULL;
	buildstate->hnswarea = NULL;
}

/*
 * Free resources
 */
static void
FreeBuildState(HnswBuildState * buildstate)
{
	MemoryContextDelete(buildstate->graphCtx);
	MemoryContextDelete(buildstate->tmpCtx);
}

/*
 * Within leader, wait for end of heap scan
 */
static double
ParallelHeapScan(HnswBuildState * buildstate)
{
	HnswShared *hnswshared = buildstate->hnswleader->hnswshared;
	int			nparticipanttuplesorts;
	double		reltuples;

	nparticipanttuplesorts = buildstate->hnswleader->nparticipanttuplesorts;
	for (;;)
	{
		SpinLockAcquire(&hnswshared->mutex);
		if (hnswshared->nparticipantsdone == nparticipanttuplesorts)
		{
			buildstate->graph = &hnswshared->graphData;
			buildstate->hnswarea = buildstate->hnswleader->hnswarea;
			reltuples = hnswshared->reltuples;
			SpinLockRelease(&hnswshared->mutex);
			break;
		}
		SpinLockRelease(&hnswshared->mutex);

		ConditionVariableSleep(&hnswshared->workersdonecv,
							   WAIT_EVENT_PARALLEL_CREATE_INDEX_SCAN);
	}

	ConditionVariableCancelSleep();

	return reltuples;
}

/*
 * Perform a worker's portion of a parallel insert
 */
static void
HnswParallelScanAndInsert(Relation heapRel, Relation indexRel, HnswShared * hnswshared, char *hnswarea, bool progress)
{
	HnswBuildState buildstate;
	TableScanDesc scan;
	double		reltuples;
	IndexInfo  *indexInfo;

	/* Join parallel scan */
	indexInfo = BuildIndexInfo(indexRel);
	indexInfo->ii_Concurrent = hnswshared->isconcurrent;
	InitBuildState(&buildstate, heapRel, indexRel, indexInfo, MAIN_FORKNUM);
	buildstate.graph = &hnswshared->graphData;
	buildstate.hnswarea = hnswarea;
	InitAllocator(&buildstate.allocator, &HnswSharedMemoryAlloc, &buildstate);
	scan = table_beginscan_parallel(heapRel,
									ParallelTableScanFromHnswShared(hnswshared));
	reltuples = table_index_build_scan(heapRel, indexRel, indexInfo,
									   true, progress, BuildCallback,
									   (void *) &buildstate, scan);

	/* Record statistics */
	SpinLockAcquire(&hnswshared->mutex);
	hnswshared->nparticipantsdone++;
	hnswshared->reltuples += reltuples;
	SpinLockRelease(&hnswshared->mutex);

	/* Log statistics */
	if (progress)
		ereport(DEBUG1, (errmsg("leader processed " INT64_FORMAT " tuples", (int64) reltuples)));
	else
		ereport(DEBUG1, (errmsg("worker processed " INT64_FORMAT " tuples", (int64) reltuples)));

	/* Notify leader */
	ConditionVariableSignal(&hnswshared->workersdonecv);

	FreeBuildState(&buildstate);
}

/*
 * Perform work within a launched parallel process
 */
void
HnswParallelBuildMain(dsm_segment *seg, shm_toc *toc)
{
	char	   *sharedquery;
	HnswShared *hnswshared;
	char	   *hnswarea;
	Relation	heapRel;
	Relation	indexRel;
	LOCKMODE	heapLockmode;
	LOCKMODE	indexLockmode;

	/* Set debug_query_string for individual workers first */
	sharedquery = shm_toc_lookup(toc, PARALLEL_KEY_QUERY_TEXT, true);
	debug_query_string = sharedquery;

	/* Report the query string from leader */
	pgstat_report_activity(STATE_RUNNING, debug_query_string);

	/* Look up shared state */
	hnswshared = shm_toc_lookup(toc, PARALLEL_KEY_HNSW_SHARED, false);

	/* Open relations using lock modes known to be obtained by index.c */
	if (!hnswshared->isconcurrent)
	{
		heapLockmode = ShareLock;
		indexLockmode = AccessExclusiveLock;
	}
	else
	{
		heapLockmode = ShareUpdateExclusiveLock;
		indexLockmode = RowExclusiveLock;
	}

	/* Open relations within worker */
	heapRel = table_open(hnswshared->heaprelid, heapLockmode);
	indexRel = index_open(hnswshared->indexrelid, indexLockmode);

	hnswarea = shm_toc_lookup(toc, PARALLEL_KEY_HNSW_AREA, false);

	/* Perform inserts */
	HnswParallelScanAndInsert(heapRel, indexRel, hnswshared, hnswarea, false);

	/* Close relations within worker */
	index_close(indexRel, indexLockmode);
	table_close(heapRel, heapLockmode);
}

/*
 * End parallel build
 */
static void
HnswEndParallel(HnswLeader * hnswleader)
{
	/* Shutdown worker processes */
	WaitForParallelWorkersToFinish(hnswleader->pcxt);

	/* Free last reference to MVCC snapshot, if one was used */
	if (IsMVCCSnapshot(hnswleader->snapshot))
		UnregisterSnapshot(hnswleader->snapshot);
	DestroyParallelContext(hnswleader->pcxt);
	ExitParallelMode();
}

/*
 * Return size of shared memory required for parallel index build
 */
static Size
ParallelEstimateShared(Relation heap, Snapshot snapshot)
{
	return add_size(BUFFERALIGN(sizeof(HnswShared)), table_parallelscan_estimate(heap, snapshot));
}

/*
 * Within leader, participate as a parallel worker
 */
static void
HnswLeaderParticipateAsWorker(HnswBuildState * buildstate)
{
	HnswLeader *hnswleader = buildstate->hnswleader;

	/* Perform work common to all participants */
	HnswParallelScanAndInsert(buildstate->heap, buildstate->index, hnswleader->hnswshared, hnswleader->hnswarea, true);
}

/*
 * Begin parallel build
 */
static void
HnswBeginParallel(HnswBuildState * buildstate, bool isconcurrent, int request)
{
	ParallelContext *pcxt;
	Snapshot	snapshot;
	Size		esthnswshared;
	Size		esthnswarea;
	Size		estother;
	HnswShared *hnswshared;
	char	   *hnswarea;
	HnswLeader *hnswleader = (HnswLeader *) palloc0(sizeof(HnswLeader));
	bool		leaderparticipates = true;
	int			querylen;

#ifdef DISABLE_LEADER_PARTICIPATION
	leaderparticipates = false;
#endif

	/* Enter parallel mode and create context */
	EnterParallelMode();
	Assert(request > 0);
	pcxt = CreateParallelContext("vector", "HnswParallelBuildMain", request);

	/* Get snapshot for table scan */
	if (!isconcurrent)
		snapshot = SnapshotAny;
	else
		snapshot = RegisterSnapshot(GetTransactionSnapshot());

	/* Estimate size of workspaces */
	esthnswshared = ParallelEstimateShared(buildstate->heap, snapshot);
	shm_toc_estimate_chunk(&pcxt->estimator, esthnswshared);

	/* Leave space for other objects in shared memory */
	/* Docker has a default limit of 64 MB for shm_size */
	/* which happens to be the default value of maintenance_work_mem */
	esthnswarea = maintenance_work_mem * 1024L;
	estother = 3 * 1024 * 1024;
	if (esthnswarea > estother)
		esthnswarea -= estother;

	esthnswarea = Min(esthnswarea, HNSW_MAX_GRAPH_MEMORY);

	shm_toc_estimate_chunk(&pcxt->estimator, esthnswarea);
	shm_toc_estimate_keys(&pcxt->estimator, 2);

	/* Finally, estimate PARALLEL_KEY_QUERY_TEXT space */
	if (debug_query_string)
	{
		querylen = strlen(debug_query_string);
		shm_toc_estimate_chunk(&pcxt->estimator, querylen + 1);
		shm_toc_estimate_keys(&pcxt->estimator, 1);
	}
	else
		querylen = 0;			/* keep compiler quiet */

	/* Everyone's had a chance to ask for space, so now create the DSM */
	InitializeParallelDSM(pcxt);

	/* If no DSM segment was available, back out (do serial build) */
	if (pcxt->seg == NULL)
	{
		if (IsMVCCSnapshot(snapshot))
			UnregisterSnapshot(snapshot);
		DestroyParallelContext(pcxt);
		ExitParallelMode();
		return;
	}

	/* Store shared build state, for which we reserved space */
	hnswshared = (HnswShared *) shm_toc_allocate(pcxt->toc, esthnswshared);
	/* Initialize immutable state */
	hnswshared->heaprelid = RelationGetRelid(buildstate->heap);
	hnswshared->indexrelid = RelationGetRelid(buildstate->index);
	hnswshared->isconcurrent = isconcurrent;
	ConditionVariableInit(&hnswshared->workersdonecv);
	SpinLockInit(&hnswshared->mutex);
	/* Initialize mutable state */
	hnswshared->nparticipantsdone = 0;
	hnswshared->reltuples = 0;
	table_parallelscan_initialize(buildstate->heap,
								  ParallelTableScanFromHnswShared(hnswshared),
								  snapshot);

	hnswarea = (char *) shm_toc_allocate(pcxt->toc, esthnswarea);
	InitGraph(&hnswshared->graphData, hnswarea, esthnswarea);

	/*
	 * Avoid base address for relptr for Postgres < 14.5
	 * https://github.com/postgres/postgres/commit/7201cd18627afc64850537806da7f22150d1a83b
	 */
#if PG_VERSION_NUM < 140005
	hnswshared->graphData.memoryUsed += MAXALIGN(1);
#endif

	shm_toc_insert(pcxt->toc, PARALLEL_KEY_HNSW_SHARED, hnswshared);
	shm_toc_insert(pcxt->toc, PARALLEL_KEY_HNSW_AREA, hnswarea);

	/* Store query string for workers */
	if (debug_query_string)
	{
		char	   *sharedquery;

		sharedquery = (char *) shm_toc_allocate(pcxt->toc, querylen + 1);
		memcpy(sharedquery, debug_query_string, querylen + 1);
		shm_toc_insert(pcxt->toc, PARALLEL_KEY_QUERY_TEXT, sharedquery);
	}

	/* Launch workers, saving status for leader/caller */
	LaunchParallelWorkers(pcxt);
	hnswleader->pcxt = pcxt;
	hnswleader->nparticipanttuplesorts = pcxt->nworkers_launched;
	if (leaderparticipates)
		hnswleader->nparticipanttuplesorts++;
	hnswleader->hnswshared = hnswshared;
	hnswleader->snapshot = snapshot;
	hnswleader->hnswarea = hnswarea;

	/* If no workers were successfully launched, back out (do serial build) */
	if (pcxt->nworkers_launched == 0)
	{
		HnswEndParallel(hnswleader);
		return;
	}

	/* Log participants */
	ereport(DEBUG1, (errmsg("using %d parallel workers", pcxt->nworkers_launched)));

	/* Save leader state now that it's clear build will be parallel */
	buildstate->hnswleader = hnswleader;

	/* Join heap scan ourselves */
	if (leaderparticipates)
		HnswLeaderParticipateAsWorker(buildstate);

	/* Wait for all launched workers */
	WaitForParallelWorkersToAttach(pcxt);
}

/*
 * Compute parallel workers
 */
static int
ComputeParallelWorkers(Relation heap, Relation index)
{
	int			parallel_workers;

	/* Make sure it's safe to use parallel workers */
	parallel_workers = plan_create_index_workers(RelationGetRelid(heap), RelationGetRelid(index));
	if (parallel_workers == 0)
		return 0;

	/* Use parallel_workers storage parameter on table if set */
	parallel_workers = RelationGetParallelWorkers(heap, -1);
	if (parallel_workers != -1)
		return Min(parallel_workers, max_parallel_maintenance_workers);

	return max_parallel_maintenance_workers;
}

/*
 * Build graph
 */
static void
BuildGraph(HnswBuildState * buildstate)
{
	int			parallel_workers = 0;

	pgstat_progress_update_param(PROGRESS_CREATEIDX_SUBPHASE, PROGRESS_HNSW_PHASE_LOAD);

	/* Calculate parallel workers */
	if (buildstate->heap != NULL)
		parallel_workers = ComputeParallelWorkers(buildstate->heap, buildstate->index);

	/* Attempt to launch parallel worker scan when required */
	if (parallel_workers > 0)
		HnswBeginParallel(buildstate, buildstate->indexInfo->ii_Concurrent, parallel_workers);

	/* Add tuples to graph */
	if (buildstate->heap != NULL)
	{
		if (buildstate->hnswleader)
			buildstate->reltuples = ParallelHeapScan(buildstate);
		else
			buildstate->reltuples = table_index_build_scan(buildstate->heap, buildstate->index, buildstate->indexInfo,
														   true, true, BuildCallback, (void *) buildstate, NULL);

		buildstate->indtuples = buildstate->graph->indtuples;
	}

	/* Flush pages */
	if (!buildstate->graph->flushed)
		FlushPages(buildstate);

	/* End parallel build */
	if (buildstate->hnswleader)
		HnswEndParallel(buildstate->hnswleader);
}

/*
 * Build the index
 */
static void
BuildIndex(Relation heap, Relation index, IndexInfo *indexInfo,
		   HnswBuildState * buildstate, ForkNumber forkNum)
{
#ifdef HNSW_MEMORY
	SeedRandom(42);
#endif

	InitBuildState(buildstate, heap, index, indexInfo, forkNum);

	BuildGraph(buildstate);

	if (RelationNeedsWAL(index) || forkNum == INIT_FORKNUM)
		log_newpage_range(index, forkNum, 0, RelationGetNumberOfBlocksInFork(index, forkNum), true);

	FreeBuildState(buildstate);
}

/*
 * Build the index for a logged table
 */
IndexBuildResult *
hnswbuild(Relation heap, Relation index, IndexInfo *indexInfo)
{
	IndexBuildResult *result;
	HnswBuildState buildstate;

	BuildIndex(heap, index, indexInfo, &buildstate, MAIN_FORKNUM);

	result = (IndexBuildResult *) palloc(sizeof(IndexBuildResult));
	result->heap_tuples = buildstate.reltuples;
	result->index_tuples = buildstate.indtuples;

	return result;
}

/*
 * Build the index for an unlogged table
 */
void
hnswbuildempty(Relation index)
{
	IndexInfo  *indexInfo = BuildIndexInfo(index);
	HnswBuildState buildstate;

	BuildIndex(NULL, index, indexInfo, &buildstate, INIT_FORKNUM);
}
```

## File: `src/hnswinsert.c`
```c
#include "postgres.h"

#include "access/genam.h"
#include "access/generic_xlog.h"
#include "hnsw.h"
#include "nodes/execnodes.h"
#include "storage/bufmgr.h"
#include "storage/lmgr.h"
#include "utils/datum.h"
#include "utils/memutils.h"
#include "utils/rel.h"

#if PG_VERSION_NUM >= 160000
#include "varatt.h"
#endif

/*
 * Get the insert page
 */
static BlockNumber
GetInsertPage(Relation index)
{
	Buffer		buf;
	Page		page;
	HnswMetaPage metap;
	BlockNumber insertPage;

	buf = ReadBuffer(index, HNSW_METAPAGE_BLKNO);
	LockBuffer(buf, BUFFER_LOCK_SHARE);
	page = BufferGetPage(buf);
	metap = HnswPageGetMeta(page);

	insertPage = metap->insertPage;

	UnlockReleaseBuffer(buf);

	return insertPage;
}

/*
 * Check for a free offset
 */
static bool
HnswFreeOffset(Relation index, Buffer buf, Page page, HnswElement element, Size etupSize, Size ntupSize, Buffer *nbuf, Page *npage, OffsetNumber *freeOffno, OffsetNumber *freeNeighborOffno, BlockNumber *newInsertPage, uint8 *tupleVersion)
{
	OffsetNumber offno;
	OffsetNumber maxoffno = PageGetMaxOffsetNumber(page);

	for (offno = FirstOffsetNumber; offno <= maxoffno; offno = OffsetNumberNext(offno))
	{
		ItemId		eitemid = PageGetItemId(page, offno);
		HnswElementTuple etup = (HnswElementTuple) PageGetItem(page, eitemid);

		/* Skip neighbor tuples */
		if (!HnswIsElementTuple(etup))
			continue;

		if (etup->deleted)
		{
			BlockNumber elementPage = BufferGetBlockNumber(buf);
			BlockNumber neighborPage = ItemPointerGetBlockNumber(&etup->neighbortid);
			OffsetNumber neighborOffno = ItemPointerGetOffsetNumber(&etup->neighbortid);
			ItemId		nitemid;
			Size		pageFree;
			Size		npageFree;

			if (!BlockNumberIsValid(*newInsertPage))
				*newInsertPage = elementPage;

			if (neighborPage == elementPage)
			{
				*nbuf = buf;
				*npage = page;
			}
			else
			{
				*nbuf = ReadBuffer(index, neighborPage);
				LockBuffer(*nbuf, BUFFER_LOCK_EXCLUSIVE);

				/* Skip WAL for now */
				*npage = BufferGetPage(*nbuf);
			}

			nitemid = PageGetItemId(*npage, neighborOffno);

			/* Ensure aligned for space check */
			Assert(etupSize == MAXALIGN(etupSize));
			Assert(ntupSize == MAXALIGN(ntupSize));

			/*
			 * Calculate free space individually since tuples are overwritten
			 * individually (in separate calls to PageIndexTupleOverwrite)
			 */
			pageFree = ItemIdGetLength(eitemid) + PageGetExactFreeSpace(page);
			npageFree = ItemIdGetLength(nitemid);
			if (neighborPage != elementPage)
				npageFree += PageGetExactFreeSpace(*npage);
			else if (pageFree >= etupSize)
				npageFree += pageFree - etupSize;

			/* Check for space */
			if (pageFree >= etupSize && npageFree >= ntupSize)
			{
				*freeOffno = offno;
				*freeNeighborOffno = neighborOffno;
				*tupleVersion = etup->version;
				return true;
			}
			else if (*nbuf != buf)
				UnlockReleaseBuffer(*nbuf);
		}
	}

	return false;
}

/*
 * Add a new page
 */
static void
HnswInsertAppendPage(Relation index, Buffer *nbuf, Page *npage, GenericXLogState *state, Page page, bool building)
{
	/* Add a new page */
	LockRelationForExtension(index, ExclusiveLock);
	*nbuf = HnswNewBuffer(index, MAIN_FORKNUM);
	UnlockRelationForExtension(index, ExclusiveLock);

	/* Init new page */
	if (building)
		*npage = BufferGetPage(*nbuf);
	else
		*npage = GenericXLogRegisterBuffer(state, *nbuf, GENERIC_XLOG_FULL_IMAGE);

	HnswInitPage(*nbuf, *npage);

	/* Update previous buffer */
	HnswPageGetOpaque(page)->nextblkno = BufferGetBlockNumber(*nbuf);
}

/*
 * Add to element and neighbor pages
 */
static void
AddElementOnDisk(Relation index, HnswElement e, int m, BlockNumber insertPage, BlockNumber *updatedInsertPage, bool building)
{
	Buffer		buf;
	Page		page;
	GenericXLogState *state;
	Size		etupSize;
	Size		ntupSize;
	Size		combinedSize;
	Size		maxSize;
	Size		minCombinedSize;
	HnswElementTuple etup;
	BlockNumber currentPage = insertPage;
	HnswNeighborTuple ntup;
	Buffer		nbuf;
	Page		npage;
	OffsetNumber freeOffno = InvalidOffsetNumber;
	OffsetNumber freeNeighborOffno = InvalidOffsetNumber;
	BlockNumber newInsertPage = InvalidBlockNumber;
	uint8		tupleVersion;
	char	   *base = NULL;

	/* Calculate sizes */
	etupSize = HNSW_ELEMENT_TUPLE_SIZE(VARSIZE_ANY(HnswPtrAccess(base, e->value)));
	ntupSize = HNSW_NEIGHBOR_TUPLE_SIZE(e->level, m);
	combinedSize = etupSize + ntupSize + sizeof(ItemIdData);
	maxSize = HNSW_MAX_SIZE;
	minCombinedSize = etupSize + HNSW_NEIGHBOR_TUPLE_SIZE(0, m) + sizeof(ItemIdData);

	/* Prepare element tuple */
	etup = palloc0(etupSize);
	HnswSetElementTuple(base, etup, e);

	/* Prepare neighbor tuple */
	ntup = palloc0(ntupSize);
	HnswSetNeighborTuple(base, ntup, e, m);

	/* Find a page (or two if needed) to insert the tuples */
	for (;;)
	{
		buf = ReadBuffer(index, currentPage);
		LockBuffer(buf, BUFFER_LOCK_EXCLUSIVE);

		if (building)
		{
			state = NULL;
			page = BufferGetPage(buf);
		}
		else
		{
			state = GenericXLogStart(index);
			page = GenericXLogRegisterBuffer(state, buf, 0);
		}

		/* Keep track of first page where element at level 0 can fit */
		if (!BlockNumberIsValid(newInsertPage) && PageGetFreeSpace(page) >= minCombinedSize)
			newInsertPage = currentPage;

		/* First, try the fastest path */
		/* Space for both tuples on the current page */
		/* This can split existing tuples in rare cases */
		if (PageGetFreeSpace(page) >= combinedSize)
		{
			nbuf = buf;
			npage = page;
			break;
		}

		/* Next, try space from a deleted element */
		if (HnswFreeOffset(index, buf, page, e, etupSize, ntupSize, &nbuf, &npage, &freeOffno, &freeNeighborOffno, &newInsertPage, &tupleVersion))
		{
			if (nbuf != buf)
			{
				if (building)
					npage = BufferGetPage(nbuf);
				else
					npage = GenericXLogRegisterBuffer(state, nbuf, 0);
			}

			/* Set tuple version */
			etup->version = tupleVersion;
			ntup->version = tupleVersion;

			break;
		}

		/* Finally, try space for element only if last page */
		/* Skip if both tuples can fit on the same page */
		if (combinedSize > maxSize && PageGetFreeSpace(page) >= etupSize && !BlockNumberIsValid(HnswPageGetOpaque(page)->nextblkno))
		{
			HnswInsertAppendPage(index, &nbuf, &npage, state, page, building);
			break;
		}

		currentPage = HnswPageGetOpaque(page)->nextblkno;

		if (BlockNumberIsValid(currentPage))
		{
			/* Move to next page */
			if (!building)
				GenericXLogAbort(state);
			UnlockReleaseBuffer(buf);
		}
		else
		{
			Buffer		newbuf;
			Page		newpage;

			HnswInsertAppendPage(index, &newbuf, &newpage, state, page, building);

			/* Commit */
			if (building)
				MarkBufferDirty(buf);
			else
				GenericXLogFinish(state);

			/* Unlock previous buffer */
			UnlockReleaseBuffer(buf);

			/* Prepare new buffer */
			buf = newbuf;
			if (building)
			{
				state = NULL;
				page = BufferGetPage(buf);
			}
			else
			{
				state = GenericXLogStart(index);
				page = GenericXLogRegisterBuffer(state, buf, 0);
			}

			/* Create new page for neighbors if needed */
			if (PageGetFreeSpace(page) < combinedSize)
				HnswInsertAppendPage(index, &nbuf, &npage, state, page, building);
			else
			{
				nbuf = buf;
				npage = page;
			}

			break;
		}
	}

	e->blkno = BufferGetBlockNumber(buf);
	e->neighborPage = BufferGetBlockNumber(nbuf);

	/* Added tuple to new page if newInsertPage is not set */
	/* So can set to neighbor page instead of element page */
	if (!BlockNumberIsValid(newInsertPage))
		newInsertPage = e->neighborPage;

	if (OffsetNumberIsValid(freeOffno))
	{
		e->offno = freeOffno;
		e->neighborOffno = freeNeighborOffno;
	}
	else
	{
		e->offno = OffsetNumberNext(PageGetMaxOffsetNumber(page));
		if (nbuf == buf)
			e->neighborOffno = OffsetNumberNext(e->offno);
		else
			e->neighborOffno = FirstOffsetNumber;
	}

	ItemPointerSet(&etup->neighbortid, e->neighborPage, e->neighborOffno);

	/* Add element and neighbors */
	if (OffsetNumberIsValid(freeOffno))
	{
		if (!PageIndexTupleOverwrite(page, e->offno, (Item) etup, etupSize))
			elog(ERROR, "failed to add index item to \"%s\"", RelationGetRelationName(index));

		if (!PageIndexTupleOverwrite(npage, e->neighborOffno, (Item) ntup, ntupSize))
			elog(ERROR, "failed to add index item to \"%s\"", RelationGetRelationName(index));
	}
	else
	{
		if (PageAddItem(page, (Item) etup, etupSize, InvalidOffsetNumber, false, false) != e->offno)
			elog(ERROR, "failed to add index item to \"%s\"", RelationGetRelationName(index));

		if (PageAddItem(npage, (Item) ntup, ntupSize, InvalidOffsetNumber, false, false) != e->neighborOffno)
			elog(ERROR, "failed to add index item to \"%s\"", RelationGetRelationName(index));
	}

	/* Commit */
	if (building)
	{
		MarkBufferDirty(buf);
		if (nbuf != buf)
			MarkBufferDirty(nbuf);
	}
	else
		GenericXLogFinish(state);
	UnlockReleaseBuffer(buf);
	if (nbuf != buf)
		UnlockReleaseBuffer(nbuf);

	/* Update the insert page */
	if (BlockNumberIsValid(newInsertPage) && newInsertPage != insertPage)
		*updatedInsertPage = newInsertPage;
}

/*
 * Load neighbors
 */
static HnswNeighborArray *
HnswLoadNeighbors(HnswElement element, Relation index, int m, int lm, int lc)
{
	char	   *base = NULL;
	HnswNeighborArray *neighbors = HnswInitNeighborArray(lm, NULL);
	ItemPointerData indextids[HNSW_MAX_M * 2];

	if (!HnswLoadNeighborTids(element, indextids, index, m, lm, lc))
		return neighbors;

	for (int i = 0; i < lm; i++)
	{
		ItemPointer indextid = &indextids[i];
		HnswElement e;
		HnswCandidate *hc;

		if (!ItemPointerIsValid(indextid))
			break;

		e = HnswInitElementFromBlock(ItemPointerGetBlockNumber(indextid), ItemPointerGetOffsetNumber(indextid));
		hc = &neighbors->items[neighbors->length++];
		HnswPtrStore(base, hc->element, e);
	}

	return neighbors;
}

/*
 * Load elements for insert
 */
static void
LoadElementsForInsert(HnswNeighborArray * neighbors, HnswQuery * q, int *idx, Relation index, HnswSupport * support)
{
	char	   *base = NULL;

	for (int i = 0; i < neighbors->length; i++)
	{
		HnswCandidate *hc = &neighbors->items[i];
		HnswElement element = HnswPtrAccess(base, hc->element);
		double		distance;

		HnswLoadElement(element, &distance, q, index, support, true, NULL);
		hc->distance = distance;

		/* Prune element if being deleted */
		if (element->heaptidsLength == 0)
		{
			*idx = i;
			break;
		}
	}
}

/*
 * Get update index
 */
static int
GetUpdateIndex(HnswElement element, HnswElement newElement, float distance, int m, int lm, int lc, Relation index, HnswSupport * support, MemoryContext updateCtx)
{
	char	   *base = NULL;
	int			idx = -1;
	HnswNeighborArray *neighbors;
	MemoryContext oldCtx = MemoryContextSwitchTo(updateCtx);

	/*
	 * Get latest neighbors since they may have changed. Do not lock yet since
	 * selecting neighbors can take time. Could use optimistic locking to
	 * retry if another update occurs before getting exclusive lock.
	 */
	neighbors = HnswLoadNeighbors(element, index, m, lm, lc);

	/*
	 * Could improve performance for vacuuming by checking neighbors against
	 * list of elements being deleted to find index. It's important to exclude
	 * already deleted elements for this since they can be replaced at any
	 * time.
	 */

	if (neighbors->length < lm)
		idx = -2;
	else
	{
		HnswQuery	q;

		q.value = HnswGetValue(base, element);

		LoadElementsForInsert(neighbors, &q, &idx, index, support);

		if (idx == -1)
			HnswUpdateConnection(base, neighbors, newElement, distance, lm, &idx, index, support);
	}

	MemoryContextSwitchTo(oldCtx);
	MemoryContextReset(updateCtx);

	return idx;
}

/*
 * Check if connection already exists
 */
static bool
ConnectionExists(HnswElement e, HnswNeighborTuple ntup, int startIdx, int lm)
{
	for (int i = 0; i < lm; i++)
	{
		ItemPointer indextid = &ntup->indextids[startIdx + i];

		if (!ItemPointerIsValid(indextid))
			break;

		if (ItemPointerGetBlockNumber(indextid) == e->blkno && ItemPointerGetOffsetNumber(indextid) == e->offno)
			return true;
	}

	return false;
}

/*
 * Update neighbor
 */
static void
UpdateNeighborOnDisk(HnswElement element, HnswElement newElement, int idx, int m, int lm, int lc, Relation index, bool checkExisting, bool building)
{
	Buffer		buf;
	Page		page;
	GenericXLogState *state;
	HnswNeighborTuple ntup;
	int			startIdx;
	OffsetNumber offno = element->neighborOffno;

	/* Register page */
	buf = ReadBuffer(index, element->neighborPage);
	LockBuffer(buf, BUFFER_LOCK_EXCLUSIVE);
	if (building)
	{
		state = NULL;
		page = BufferGetPage(buf);
	}
	else
	{
		state = GenericXLogStart(index);
		page = GenericXLogRegisterBuffer(state, buf, 0);
	}

	/* Get tuple */
	ntup = (HnswNeighborTuple) PageGetItem(page, PageGetItemId(page, offno));

	/* Calculate index for update */
	startIdx = (element->level - lc) * m;

	/* Check for existing connection */
	if (checkExisting && ConnectionExists(newElement, ntup, startIdx, lm))
		idx = -1;
	else if (idx == -2)
	{
		/* Find free offset if still exists */
		/* TODO Retry updating connections if not */
		for (int j = 0; j < lm; j++)
		{
			if (!ItemPointerIsValid(&ntup->indextids[startIdx + j]))
			{
				idx = startIdx + j;
				break;
			}
		}
	}
	else
		idx += startIdx;

	/* Make robust to issues */
	if (idx >= 0 && idx < ntup->count)
	{
		ItemPointer indextid = &ntup->indextids[idx];

		/* Update neighbor on the buffer */
		ItemPointerSet(indextid, newElement->blkno, newElement->offno);

		/* Commit */
		if (building)
			MarkBufferDirty(buf);
		else
			GenericXLogFinish(state);
	}
	else if (!building)
		GenericXLogAbort(state);

	UnlockReleaseBuffer(buf);
}

/*
 * Update neighbors
 */
void
HnswUpdateNeighborsOnDisk(Relation index, HnswSupport * support, HnswElement e, int m, bool checkExisting, bool building)
{
	char	   *base = NULL;

	/* Use separate memory context to improve performance for larger vectors */
	MemoryContext updateCtx = GenerationContextCreate(CurrentMemoryContext,
													  "Hnsw insert update context",
#if PG_VERSION_NUM >= 150000
													  128 * 1024, 128 * 1024,
#endif
													  128 * 1024);

	for (int lc = e->level; lc >= 0; lc--)
	{
		int			lm = HnswGetLayerM(m, lc);
		HnswNeighborArray *neighbors = HnswGetNeighbors(base, e, lc);

		for (int i = 0; i < neighbors->length; i++)
		{
			HnswCandidate *hc = &neighbors->items[i];
			HnswElement neighborElement = HnswPtrAccess(base, hc->element);
			int			idx;

			idx = GetUpdateIndex(neighborElement, e, hc->distance, m, lm, lc, index, support, updateCtx);

			/* New element was not selected as a neighbor */
			if (idx == -1)
				continue;

			UpdateNeighborOnDisk(neighborElement, e, idx, m, lm, lc, index, checkExisting, building);
		}
	}

	MemoryContextDelete(updateCtx);
}

/*
 * Add a heap TID to an existing element
 */
static bool
AddDuplicateOnDisk(Relation index, HnswElement element, HnswElement dup, bool building)
{
	Buffer		buf;
	Page		page;
	GenericXLogState *state;
	HnswElementTuple etup;
	int			i;

	/* Read page */
	buf = ReadBuffer(index, dup->blkno);
	LockBuffer(buf, BUFFER_LOCK_EXCLUSIVE);
	if (building)
	{
		state = NULL;
		page = BufferGetPage(buf);
	}
	else
	{
		state = GenericXLogStart(index);
		page = GenericXLogRegisterBuffer(state, buf, 0);
	}

	/* Find space */
	etup = (HnswElementTuple) PageGetItem(page, PageGetItemId(page, dup->offno));
	for (i = 0; i < HNSW_HEAPTIDS; i++)
	{
		if (!ItemPointerIsValid(&etup->heaptids[i]))
			break;
	}

	/* Either being deleted or we lost our chance to another backend */
	if (i == 0 || i == HNSW_HEAPTIDS)
	{
		if (!building)
			GenericXLogAbort(state);
		UnlockReleaseBuffer(buf);
		return false;
	}

	/* Add heap TID, modifying the tuple on the page directly */
	etup->heaptids[i] = element->heaptids[0];

	/* Commit */
	if (building)
		MarkBufferDirty(buf);
	else
		GenericXLogFinish(state);
	UnlockReleaseBuffer(buf);

	return true;
}

/*
 * Find duplicate element
 */
static bool
FindDuplicateOnDisk(Relation index, HnswElement element, bool building)
{
	char	   *base = NULL;
	HnswNeighborArray *neighbors = HnswGetNeighbors(base, element, 0);
	Datum		value = HnswGetValue(base, element);

	for (int i = 0; i < neighbors->length; i++)
	{
		HnswCandidate *neighbor = &neighbors->items[i];
		HnswElement neighborElement = HnswPtrAccess(base, neighbor->element);
		Datum		neighborValue = HnswGetValue(base, neighborElement);

		/* Exit early since ordered by distance */
		if (!datumIsEqual(value, neighborValue, false, -1))
			return false;

		if (AddDuplicateOnDisk(index, element, neighborElement, building))
			return true;
	}

	return false;
}

/*
 * Update graph on disk
 */
static void
UpdateGraphOnDisk(Relation index, HnswSupport * support, HnswElement element, int m, HnswElement entryPoint, bool building)
{
	BlockNumber newInsertPage = InvalidBlockNumber;

	/* Look for duplicate */
	if (FindDuplicateOnDisk(index, element, building))
		return;

	/* Add element */
	AddElementOnDisk(index, element, m, GetInsertPage(index), &newInsertPage, building);

	/* Update insert page if needed */
	if (BlockNumberIsValid(newInsertPage))
		HnswUpdateMetaPage(index, 0, NULL, newInsertPage, MAIN_FORKNUM, building);

	/* Update neighbors */
	HnswUpdateNeighborsOnDisk(index, support, element, m, false, building);

	/* Update entry point if needed */
	if (entryPoint == NULL || element->level > entryPoint->level)
		HnswUpdateMetaPage(index, HNSW_UPDATE_ENTRY_GREATER, element, InvalidBlockNumber, MAIN_FORKNUM, building);
}

/*
 * Insert a tuple into the index
 */
bool
HnswInsertTupleOnDisk(Relation index, HnswSupport * support, Datum value, ItemPointer heaptid, bool building)
{
	HnswElement entryPoint;
	HnswElement element;
	int			m;
	int			efConstruction = HnswGetEfConstruction(index);
	LOCKMODE	lockmode = ShareLock;
	char	   *base = NULL;

	/*
	 * Get a shared lock. This allows vacuum to ensure no in-flight inserts
	 * before repairing graph. Use a page lock so it does not interfere with
	 * buffer lock (or reads when vacuuming).
	 */
	LockPage(index, HNSW_UPDATE_LOCK, lockmode);

	/* Get m and entry point */
	HnswGetMetaPageInfo(index, &m, &entryPoint);

	/* Create an element */
	element = HnswInitElement(base, heaptid, m, HnswGetMl(m), HnswGetMaxLevel(m), NULL);
	HnswPtrStore(base, element->value, (char *) DatumGetPointer(value));

	/* Prevent concurrent inserts when likely updating entry point */
	if (entryPoint == NULL || element->level > entryPoint->level)
	{
		/* Release shared lock */
		UnlockPage(index, HNSW_UPDATE_LOCK, lockmode);

		/* Get exclusive lock */
		lockmode = ExclusiveLock;
		LockPage(index, HNSW_UPDATE_LOCK, lockmode);

		/* Get latest entry point after lock is acquired */
		entryPoint = HnswGetEntryPoint(index);
	}

	/* Find neighbors for element */
	HnswFindElementNeighbors(base, element, entryPoint, index, support, m, efConstruction, false);

	/* Update graph on disk */
	UpdateGraphOnDisk(index, support, element, m, entryPoint, building);

	/* Release lock */
	UnlockPage(index, HNSW_UPDATE_LOCK, lockmode);

	return true;
}

/*
 * Insert a tuple into the index
 */
static void
HnswInsertTuple(Relation index, Datum *values, bool *isnull, ItemPointer heaptid)
{
	Datum		value;
	const		HnswTypeInfo *typeInfo = HnswGetTypeInfo(index);
	HnswSupport support;

	HnswInitSupport(&support, index);

	/* Form index value */
	if (!HnswFormIndexValue(&value, values, isnull, typeInfo, &support))
		return;

	HnswInsertTupleOnDisk(index, &support, value, heaptid, false);
}

/*
 * Insert a tuple into the index
 */
bool
hnswinsert(Relation index, Datum *values, bool *isnull, ItemPointer heap_tid,
		   Relation heap, IndexUniqueCheck checkUnique
#if PG_VERSION_NUM >= 140000
		   ,bool indexUnchanged
#endif
		   ,IndexInfo *indexInfo
)
{
	MemoryContext oldCtx;
	MemoryContext insertCtx;

	/* Skip nulls */
	if (isnull[0])
		return false;

	/* Create memory context */
	insertCtx = AllocSetContextCreate(CurrentMemoryContext,
									  "Hnsw insert temporary context",
									  ALLOCSET_DEFAULT_SIZES);
	oldCtx = MemoryContextSwitchTo(insertCtx);

	/* Insert tuple */
	HnswInsertTuple(index, values, isnull, heap_tid);

	/* Delete memory context */
	MemoryContextSwitchTo(oldCtx);
	MemoryContextDelete(insertCtx);

	return false;
}
```

## File: `src/hnswscan.c`
```c
#include "postgres.h"

#include <limits.h>

#include "access/genam.h"
#include "access/relscan.h"
#include "hnsw.h"
#include "lib/pairingheap.h"
#include "miscadmin.h"
#include "nodes/pg_list.h"
#include "pgstat.h"
#include "storage/lmgr.h"
#include "utils/float.h"
#include "utils/memutils.h"
#include "utils/relcache.h"
#include "utils/snapmgr.h"

#if PG_VERSION_NUM >= 160000
#include "varatt.h"
#endif

/*
 * Algorithm 5 from paper
 */
static List *
GetScanItems(IndexScanDesc scan, Datum value)
{
	HnswScanOpaque so = (HnswScanOpaque) scan->opaque;
	Relation	index = scan->indexRelation;
	HnswSupport *support = &so->support;
	List	   *ep;
	List	   *w;
	int			m;
	HnswElement entryPoint;
	char	   *base = NULL;
	HnswQuery  *q = &so->q;

	/* Get m and entry point */
	HnswGetMetaPageInfo(index, &m, &entryPoint);

	q->value = value;
	so->m = m;

	if (entryPoint == NULL)
		return NIL;

	ep = list_make1(HnswEntryCandidate(base, entryPoint, q, index, support, false));

	for (int lc = entryPoint->level; lc >= 1; lc--)
	{
		w = HnswSearchLayer(base, q, ep, 1, lc, index, support, m, false, NULL, NULL, NULL, true, NULL);
		ep = w;
	}

	return HnswSearchLayer(base, q, ep, hnsw_ef_search, 0, index, support, m, false, NULL, &so->v, hnsw_iterative_scan != HNSW_ITERATIVE_SCAN_OFF ? &so->discarded : NULL, true, &so->tuples);
}

/*
 * Resume scan at ground level with discarded candidates
 */
static List *
ResumeScanItems(IndexScanDesc scan)
{
	HnswScanOpaque so = (HnswScanOpaque) scan->opaque;
	Relation	index = scan->indexRelation;
	List	   *ep = NIL;
	char	   *base = NULL;
	int			batch_size = hnsw_ef_search;

	if (pairingheap_is_empty(so->discarded))
		return NIL;

	/* Get next batch of candidates */
	for (int i = 0; i < batch_size; i++)
	{
		HnswSearchCandidate *sc;

		if (pairingheap_is_empty(so->discarded))
			break;

		sc = HnswGetSearchCandidate(w_node, pairingheap_remove_first(so->discarded));

		ep = lappend(ep, sc);
	}

	return HnswSearchLayer(base, &so->q, ep, batch_size, 0, index, &so->support, so->m, false, NULL, &so->v, &so->discarded, false, &so->tuples);
}

/*
 * Get scan value
 */
static Datum
GetScanValue(IndexScanDesc scan)
{
	HnswScanOpaque so = (HnswScanOpaque) scan->opaque;
	Datum		value;

	if (scan->orderByData->sk_flags & SK_ISNULL)
		value = PointerGetDatum(NULL);
	else
	{
		value = scan->orderByData->sk_argument;

		/* Value should not be compressed or toasted */
		Assert(!VARATT_IS_COMPRESSED(DatumGetPointer(value)));
		Assert(!VARATT_IS_EXTENDED(DatumGetPointer(value)));

		/* Normalize if needed */
		if (so->support.normprocinfo != NULL)
			value = HnswNormValue(so->typeInfo, so->support.collation, value);
	}

	return value;
}

#if defined(HNSW_MEMORY)
/*
 * Show memory usage
 */
static void
ShowMemoryUsage(HnswScanOpaque so)
{
	elog(INFO, "memory: %zu KB, tuples: " INT64_FORMAT, MemoryContextMemAllocated(so->tmpCtx, false) / 1024, so->tuples);
}
#endif

/*
 * Prepare for an index scan
 */
IndexScanDesc
hnswbeginscan(Relation index, int nkeys, int norderbys)
{
	IndexScanDesc scan;
	HnswScanOpaque so;
	double		maxMemory;

	scan = RelationGetIndexScan(index, nkeys, norderbys);

	so = (HnswScanOpaque) palloc(sizeof(HnswScanOpaqueData));
	so->typeInfo = HnswGetTypeInfo(index);

	/* Set support functions */
	HnswInitSupport(&so->support, index);

	/*
	 * Use a lower max allocation size than default to allow scanning more
	 * tuples for iterative search before exceeding work_mem
	 */
	so->tmpCtx = AllocSetContextCreate(CurrentMemoryContext,
									   "Hnsw scan temporary context",
									   0, 8 * 1024, 256 * 1024);

	/* Calculate max memory */
	/* Add 256 extra bytes to fill last block when close */
	maxMemory = (double) work_mem * hnsw_scan_mem_multiplier * 1024.0 + 256;
	so->maxMemory = Min(maxMemory, (double) (SIZE_MAX / 2));

	scan->opaque = so;

	return scan;
}

/*
 * Start or restart an index scan
 */
void
hnswrescan(IndexScanDesc scan, ScanKey keys, int nkeys, ScanKey orderbys, int norderbys)
{
	HnswScanOpaque so = (HnswScanOpaque) scan->opaque;

	so->first = true;
	/* v and discarded are allocated in tmpCtx */
	so->v.tids = NULL;
	so->discarded = NULL;
	so->tuples = 0;
	so->previousDistance = -get_float8_infinity();
	MemoryContextReset(so->tmpCtx);

	if (keys && scan->numberOfKeys > 0)
		memmove(scan->keyData, keys, scan->numberOfKeys * sizeof(ScanKeyData));

	if (orderbys && scan->numberOfOrderBys > 0)
		memmove(scan->orderByData, orderbys, scan->numberOfOrderBys * sizeof(ScanKeyData));
}

/*
 * Fetch the next tuple in the given scan
 */
bool
hnswgettuple(IndexScanDesc scan, ScanDirection dir)
{
	HnswScanOpaque so = (HnswScanOpaque) scan->opaque;
	MemoryContext oldCtx = MemoryContextSwitchTo(so->tmpCtx);

	/*
	 * Index can be used to scan backward, but Postgres doesn't support
	 * backward scan on operators
	 */
	Assert(ScanDirectionIsForward(dir));

	if (so->first)
	{
		Datum		value;

		/* Count index scan for stats */
		pgstat_count_index_scan(scan->indexRelation);
#if PG_VERSION_NUM >= 180000
		if (scan->instrument)
			scan->instrument->nsearches++;
#endif

		/* Safety check */
		if (scan->orderByData == NULL)
			elog(ERROR, "cannot scan hnsw index without order");

		/* Requires MVCC-compliant snapshot as not able to maintain a pin */
		/* https://www.postgresql.org/docs/current/index-locking.html */
		if (!IsMVCCSnapshot(scan->xs_snapshot))
			elog(ERROR, "non-MVCC snapshots are not supported with hnsw");

		/* Get scan value */
		value = GetScanValue(scan);

		/*
		 * Get a shared lock. This allows vacuum to ensure no in-flight scans
		 * before marking tuples as deleted.
		 */
		LockPage(scan->indexRelation, HNSW_SCAN_LOCK, ShareLock);

		so->w = GetScanItems(scan, value);

		/* Release shared lock */
		UnlockPage(scan->indexRelation, HNSW_SCAN_LOCK, ShareLock);

		so->first = false;

#if defined(HNSW_MEMORY)
		ShowMemoryUsage(so);
#endif
	}

	for (;;)
	{
		char	   *base = NULL;
		HnswSearchCandidate *sc;
		HnswElement element;
		ItemPointer heaptid;

		if (list_length(so->w) == 0)
		{
			if (hnsw_iterative_scan == HNSW_ITERATIVE_SCAN_OFF)
				break;

			/* Empty index */
			if (so->discarded == NULL)
				break;

			/* Reached max number of tuples or memory limit */
			if (so->tuples >= hnsw_max_scan_tuples || MemoryContextMemAllocated(so->tmpCtx, false) > so->maxMemory)
			{
				if (pairingheap_is_empty(so->discarded))
					break;

				/* Return remaining tuples */
				so->w = lappend(so->w, HnswGetSearchCandidate(w_node, pairingheap_remove_first(so->discarded)));
			}
			else
			{
				/*
				 * Locking ensures when neighbors are read, the elements they
				 * reference will not be deleted (and replaced) during the
				 * iteration.
				 *
				 * Elements loaded into memory on previous iterations may have
				 * been deleted (and replaced), so when reading neighbors, the
				 * element version must be checked.
				 */
				LockPage(scan->indexRelation, HNSW_SCAN_LOCK, ShareLock);

				so->w = ResumeScanItems(scan);

				UnlockPage(scan->indexRelation, HNSW_SCAN_LOCK, ShareLock);

#if defined(HNSW_MEMORY)
				ShowMemoryUsage(so);
#endif
			}

			if (list_length(so->w) == 0)
				break;
		}

		sc = llast(so->w);
		element = HnswPtrAccess(base, sc->element);

		/* Move to next element if no valid heap TIDs */
		if (element->heaptidsLength == 0)
		{
			so->w = list_delete_last(so->w);

			/* Mark memory as free for next iteration */
			if (hnsw_iterative_scan != HNSW_ITERATIVE_SCAN_OFF)
			{
				pfree(element);
				pfree(sc);
			}

			continue;
		}

		heaptid = &element->heaptids[--element->heaptidsLength];

		if (hnsw_iterative_scan == HNSW_ITERATIVE_SCAN_STRICT)
		{
			if (sc->distance < so->previousDistance)
				continue;

			so->previousDistance = sc->distance;
		}

		MemoryContextSwitchTo(oldCtx);

		scan->xs_heaptid = *heaptid;
		scan->xs_recheck = false;
		scan->xs_recheckorderby = false;
		return true;
	}

	MemoryContextSwitchTo(oldCtx);
	return false;
}

/*
 * End a scan and release resources
 */
void
hnswendscan(IndexScanDesc scan)
{
	HnswScanOpaque so = (HnswScanOpaque) scan->opaque;

	MemoryContextDelete(so->tmpCtx);

	pfree(so);
	scan->opaque = NULL;
}
```

## File: `src/hnswutils.c`
```c
#include "postgres.h"

#include <math.h>

#include "access/genam.h"
#include "access/generic_xlog.h"
#include "common/hashfn.h"
#include "fmgr.h"
#include "hnsw.h"
#include "lib/pairingheap.h"
#include "nodes/pg_list.h"
#include "port/atomics.h"
#include "sparsevec.h"
#include "storage/bufmgr.h"
#include "utils/datum.h"
#include "utils/memdebug.h"
#include "utils/rel.h"
#include "vector.h"

#if PG_VERSION_NUM >= 160000
#include "varatt.h"
#endif

#if PG_VERSION_NUM < 170000
static inline uint64
murmurhash64(uint64 data)
{
	uint64		h = data;

	h ^= h >> 33;
	h *= 0xff51afd7ed558ccd;
	h ^= h >> 33;
	h *= 0xc4ceb9fe1a85ec53;
	h ^= h >> 33;

	return h;
}
#endif

/* TID hash table */
static uint32
hash_tid(ItemPointerData tid)
{
	union
	{
		uint64		i;
		ItemPointerData tid;
	}			x;

	/* Initialize unused bytes */
	x.i = 0;
	x.tid = tid;

	return murmurhash64(x.i);
}

#define SH_PREFIX		tidhash
#define SH_ELEMENT_TYPE	TidHashEntry
#define SH_KEY_TYPE		ItemPointerData
#define	SH_KEY			tid
#define SH_HASH_KEY(tb, key)	hash_tid(key)
#define SH_EQUAL(tb, a, b)		ItemPointerEquals(&a, &b)
#define	SH_SCOPE		extern
#define SH_DEFINE
#include "lib/simplehash.h"

/* Pointer hash table */
static uint32
hash_pointer(uintptr_t ptr)
{
#if SIZEOF_VOID_P == 8
	return murmurhash64((uint64) ptr);
#else
	return murmurhash32((uint32) ptr);
#endif
}

#define SH_PREFIX		pointerhash
#define SH_ELEMENT_TYPE	PointerHashEntry
#define SH_KEY_TYPE		uintptr_t
#define	SH_KEY			ptr
#define SH_HASH_KEY(tb, key)	hash_pointer(key)
#define SH_EQUAL(tb, a, b)		(a == b)
#define	SH_SCOPE		extern
#define SH_DEFINE
#include "lib/simplehash.h"

/* Offset hash table */
static uint32
hash_offset(Size offset)
{
#if SIZEOF_SIZE_T == 8
	return murmurhash64((uint64) offset);
#else
	return murmurhash32((uint32) offset);
#endif
}

#define SH_PREFIX		offsethash
#define SH_ELEMENT_TYPE	OffsetHashEntry
#define SH_KEY_TYPE		Size
#define	SH_KEY			offset
#define SH_HASH_KEY(tb, key)	hash_offset(key)
#define SH_EQUAL(tb, a, b)		(a == b)
#define	SH_SCOPE		extern
#define SH_DEFINE
#include "lib/simplehash.h"

/*
 * Get the max number of connections in an upper layer for each element in the index
 */
int
HnswGetM(Relation index)
{
	HnswOptions *opts = (HnswOptions *) index->rd_options;

	if (opts)
		return opts->m;

	return HNSW_DEFAULT_M;
}

/*
 * Get the size of the dynamic candidate list in the index
 */
int
HnswGetEfConstruction(Relation index)
{
	HnswOptions *opts = (HnswOptions *) index->rd_options;

	if (opts)
		return opts->efConstruction;

	return HNSW_DEFAULT_EF_CONSTRUCTION;
}

/*
 * Get proc
 */
FmgrInfo *
HnswOptionalProcInfo(Relation index, uint16 procnum)
{
	if (!OidIsValid(index_getprocid(index, 1, procnum)))
		return NULL;

	return index_getprocinfo(index, 1, procnum);
}

/*
 * Init support functions
 */
void
HnswInitSupport(HnswSupport * support, Relation index)
{
	support->procinfo = index_getprocinfo(index, 1, HNSW_DISTANCE_PROC);
	support->collation = index->rd_indcollation[0];
	support->normprocinfo = HnswOptionalProcInfo(index, HNSW_NORM_PROC);
}

/*
 * Normalize value
 */
Datum
HnswNormValue(const HnswTypeInfo * typeInfo, Oid collation, Datum value)
{
	return DirectFunctionCall1Coll(typeInfo->normalize, collation, value);
}

/*
 * Check if non-zero norm
 */
bool
HnswCheckNorm(HnswSupport * support, Datum value)
{
	return DatumGetFloat8(FunctionCall1Coll(support->normprocinfo, support->collation, value)) > 0;
}

/*
 * New buffer
 */
Buffer
HnswNewBuffer(Relation index, ForkNumber forkNum)
{
	Buffer		buf = ReadBufferExtended(index, forkNum, P_NEW, RBM_NORMAL, NULL);

	LockBuffer(buf, BUFFER_LOCK_EXCLUSIVE);
	return buf;
}

/*
 * Init page
 */
void
HnswInitPage(Buffer buf, Page page)
{
	PageInit(page, BufferGetPageSize(buf), sizeof(HnswPageOpaqueData));
	HnswPageGetOpaque(page)->nextblkno = InvalidBlockNumber;
	HnswPageGetOpaque(page)->page_id = HNSW_PAGE_ID;
}

/*
 * Allocate a neighbor array
 */
HnswNeighborArray *
HnswInitNeighborArray(int lm, HnswAllocator * allocator)
{
	HnswNeighborArray *a = HnswAlloc(allocator, HNSW_NEIGHBOR_ARRAY_SIZE(lm));

	a->length = 0;
	a->closerSet = false;
	return a;
}

/*
 * Allocate neighbors
 */
void
HnswInitNeighbors(char *base, HnswElement element, int m, HnswAllocator * allocator)
{
	int			level = element->level;
	HnswNeighborArrayPtr *neighborList = (HnswNeighborArrayPtr *) HnswAlloc(allocator, sizeof(HnswNeighborArrayPtr) * (level + 1));

	HnswPtrStore(base, element->neighbors, neighborList);

	for (int lc = 0; lc <= level; lc++)
		HnswPtrStore(base, neighborList[lc], HnswInitNeighborArray(HnswGetLayerM(m, lc), allocator));
}

/*
 * Allocate memory from the allocator
 */
void *
HnswAlloc(HnswAllocator * allocator, Size size)
{
	if (allocator)
		return (*(allocator)->alloc) (size, (allocator)->state);

	return palloc(size);
}

/*
 * Allocate an element
 */
HnswElement
HnswInitElement(char *base, ItemPointer heaptid, int m, double ml, int maxLevel, HnswAllocator * allocator)
{
	HnswElement element = HnswAlloc(allocator, sizeof(HnswElementData));

	int			level = (int) (-log(RandomDouble()) * ml);

	/* Cap level */
	if (level > maxLevel)
		level = maxLevel;

	element->heaptidsLength = 0;
	HnswAddHeapTid(element, heaptid);

	element->level = level;
	element->deleted = 0;
	/* Start at one to make it easier to find issues */
	element->version = 1;

	HnswInitNeighbors(base, element, m, allocator);

	HnswPtrStore(base, element->value, (char *) NULL);

	return element;
}

/*
 * Add a heap TID to an element
 */
void
HnswAddHeapTid(HnswElement element, ItemPointer heaptid)
{
	element->heaptids[element->heaptidsLength++] = *heaptid;
}

/*
 * Allocate an element from block and offset numbers
 */
HnswElement
HnswInitElementFromBlock(BlockNumber blkno, OffsetNumber offno)
{
	HnswElement element = palloc(sizeof(HnswElementData));
	char	   *base = NULL;

	element->blkno = blkno;
	element->offno = offno;
	HnswPtrStore(base, element->neighbors, (HnswNeighborArrayPtr *) NULL);
	HnswPtrStore(base, element->value, (char *) NULL);
	return element;
}

/*
 * Get the metapage info
 */
void
HnswGetMetaPageInfo(Relation index, int *m, HnswElement * entryPoint)
{
	Buffer		buf;
	Page		page;
	HnswMetaPage metap;

	buf = ReadBuffer(index, HNSW_METAPAGE_BLKNO);
	LockBuffer(buf, BUFFER_LOCK_SHARE);
	page = BufferGetPage(buf);
	metap = HnswPageGetMeta(page);

	if (unlikely(metap->magicNumber != HNSW_MAGIC_NUMBER))
		elog(ERROR, "hnsw index is not valid");

	if (m != NULL)
		*m = metap->m;

	if (entryPoint != NULL)
	{
		if (BlockNumberIsValid(metap->entryBlkno))
		{
			*entryPoint = HnswInitElementFromBlock(metap->entryBlkno, metap->entryOffno);
			(*entryPoint)->level = metap->entryLevel;
		}
		else
			*entryPoint = NULL;
	}

	UnlockReleaseBuffer(buf);
}

/*
 * Get the entry point
 */
HnswElement
HnswGetEntryPoint(Relation index)
{
	HnswElement entryPoint;

	HnswGetMetaPageInfo(index, NULL, &entryPoint);

	return entryPoint;
}

/*
 * Update the metapage info
 */
static void
HnswUpdateMetaPageInfo(Page page, int updateEntry, HnswElement entryPoint, BlockNumber insertPage)
{
	HnswMetaPage metap = HnswPageGetMeta(page);

	if (updateEntry)
	{
		if (entryPoint == NULL)
		{
			metap->entryBlkno = InvalidBlockNumber;
			metap->entryOffno = InvalidOffsetNumber;
			metap->entryLevel = -1;
		}
		else if (entryPoint->level > metap->entryLevel || updateEntry == HNSW_UPDATE_ENTRY_ALWAYS)
		{
			metap->entryBlkno = entryPoint->blkno;
			metap->entryOffno = entryPoint->offno;
			metap->entryLevel = entryPoint->level;
		}
	}

	if (BlockNumberIsValid(insertPage))
		metap->insertPage = insertPage;
}

/*
 * Update the metapage
 */
void
HnswUpdateMetaPage(Relation index, int updateEntry, HnswElement entryPoint, BlockNumber insertPage, ForkNumber forkNum, bool building)
{
	Buffer		buf;
	Page		page;
	GenericXLogState *state;

	buf = ReadBufferExtended(index, forkNum, HNSW_METAPAGE_BLKNO, RBM_NORMAL, NULL);
	LockBuffer(buf, BUFFER_LOCK_EXCLUSIVE);
	if (building)
	{
		state = NULL;
		page = BufferGetPage(buf);
	}
	else
	{
		state = GenericXLogStart(index);
		page = GenericXLogRegisterBuffer(state, buf, 0);
	}

	HnswUpdateMetaPageInfo(page, updateEntry, entryPoint, insertPage);

	if (building)
		MarkBufferDirty(buf);
	else
		GenericXLogFinish(state);
	UnlockReleaseBuffer(buf);
}

/*
 * Form index value
 */
bool
HnswFormIndexValue(Datum *out, Datum *values, bool *isnull, const HnswTypeInfo * typeInfo, HnswSupport * support)
{
	/* Detoast once for all calls */
	Datum		value = PointerGetDatum(PG_DETOAST_DATUM(values[0]));

	/* Check value */
	if (typeInfo->checkValue != NULL)
		typeInfo->checkValue(DatumGetPointer(value));

	/* Normalize if needed */
	if (support->normprocinfo != NULL)
	{
		if (!HnswCheckNorm(support, value))
			return false;

		value = HnswNormValue(typeInfo, support->collation, value);
	}

	*out = value;

	return true;
}

/*
 * Set element tuple, except for neighbor info
 */
void
HnswSetElementTuple(char *base, HnswElementTuple etup, HnswElement element)
{
	Pointer		valuePtr = HnswPtrAccess(base, element->value);

	etup->type = HNSW_ELEMENT_TUPLE_TYPE;
	etup->level = element->level;
	etup->deleted = 0;
	etup->version = element->version;
	for (int i = 0; i < HNSW_HEAPTIDS; i++)
	{
		if (i < element->heaptidsLength)
			etup->heaptids[i] = element->heaptids[i];
		else
			ItemPointerSetInvalid(&etup->heaptids[i]);
	}
	memcpy(&etup->data, valuePtr, VARSIZE_ANY(valuePtr));
}

/*
 * Set neighbor tuple
 */
void
HnswSetNeighborTuple(char *base, HnswNeighborTuple ntup, HnswElement e, int m)
{
	int			idx = 0;

	ntup->type = HNSW_NEIGHBOR_TUPLE_TYPE;

	for (int lc = e->level; lc >= 0; lc--)
	{
		HnswNeighborArray *neighbors = HnswGetNeighbors(base, e, lc);
		int			lm = HnswGetLayerM(m, lc);

		for (int i = 0; i < lm; i++)
		{
			ItemPointer indextid = &ntup->indextids[idx++];

			if (i < neighbors->length)
			{
				HnswCandidate *hc = &neighbors->items[i];
				HnswElement hce = HnswPtrAccess(base, hc->element);

				ItemPointerSet(indextid, hce->blkno, hce->offno);
			}
			else
				ItemPointerSetInvalid(indextid);
		}
	}

	ntup->count = idx;
	ntup->version = e->version;
}

/*
 * Load an element from a tuple
 */
void
HnswLoadElementFromTuple(HnswElement element, HnswElementTuple etup, bool loadHeaptids, bool loadVec)
{
	element->level = etup->level;
	element->deleted = etup->deleted;
	element->version = etup->version;
	element->neighborPage = ItemPointerGetBlockNumber(&etup->neighbortid);
	element->neighborOffno = ItemPointerGetOffsetNumber(&etup->neighbortid);
	element->heaptidsLength = 0;

	if (loadHeaptids)
	{
		for (int i = 0; i < HNSW_HEAPTIDS; i++)
		{
			/* Can stop at first invalid */
			if (!ItemPointerIsValid(&etup->heaptids[i]))
				break;

			HnswAddHeapTid(element, &etup->heaptids[i]);
		}
	}

	if (loadVec)
	{
		char	   *base = NULL;
		Datum		value = datumCopy(PointerGetDatum(&etup->data), false, -1);

		HnswPtrStore(base, element->value, (char *) DatumGetPointer(value));
	}
}

/*
 * Calculate the distance between values
 */
static inline double
HnswGetDistance(Datum a, Datum b, HnswSupport * support)
{
	return DatumGetFloat8(FunctionCall2Coll(support->procinfo, support->collation, a, b));
}

/*
 * Load an element and optionally get its distance from q
 */
static void
HnswLoadElementImpl(BlockNumber blkno, OffsetNumber offno, double *distance, HnswQuery * q, Relation index, HnswSupport * support, bool loadVec, double *maxDistance, HnswElement * element)
{
	Buffer		buf;
	Page		page;
	HnswElementTuple etup;

	/* Read vector */
	buf = ReadBuffer(index, blkno);
	LockBuffer(buf, BUFFER_LOCK_SHARE);
	page = BufferGetPage(buf);

	etup = (HnswElementTuple) PageGetItem(page, PageGetItemId(page, offno));

	Assert(HnswIsElementTuple(etup));

	/* Calculate distance */
	if (distance != NULL)
	{
		if (DatumGetPointer(q->value) == NULL)
			*distance = 0;
		else
			*distance = HnswGetDistance(q->value, PointerGetDatum(&etup->data), support);
	}

	/* Load element */
	if (distance == NULL || maxDistance == NULL || *distance < *maxDistance)
	{
		if (*element == NULL)
			*element = HnswInitElementFromBlock(blkno, offno);

		HnswLoadElementFromTuple(*element, etup, true, loadVec);
	}

	UnlockReleaseBuffer(buf);
}

/*
 * Load an element and optionally get its distance from q
 */
void
HnswLoadElement(HnswElement element, double *distance, HnswQuery * q, Relation index, HnswSupport * support, bool loadVec, double *maxDistance)
{
	HnswLoadElementImpl(element->blkno, element->offno, distance, q, index, support, loadVec, maxDistance, &element);
}

/*
 * Get the distance for an element
 */
static double
GetElementDistance(char *base, HnswElement element, HnswQuery * q, HnswSupport * support)
{
	Datum		value = HnswGetValue(base, element);

	return HnswGetDistance(q->value, value, support);
}

/*
 * Allocate a search candidate
 */
static HnswSearchCandidate *
HnswInitSearchCandidate(char *base, HnswElement element, double distance)
{
	HnswSearchCandidate *sc = palloc(sizeof(HnswSearchCandidate));

	HnswPtrStore(base, sc->element, element);
	sc->distance = distance;
	return sc;
}

/*
 * Create a candidate for the entry point
 */
HnswSearchCandidate *
HnswEntryCandidate(char *base, HnswElement entryPoint, HnswQuery * q, Relation index, HnswSupport * support, bool loadVec)
{
	bool		inMemory = index == NULL;
	double		distance;

	if (inMemory)
		distance = GetElementDistance(base, entryPoint, q, support);
	else
		HnswLoadElement(entryPoint, &distance, q, index, support, loadVec, NULL);

	return HnswInitSearchCandidate(base, entryPoint, distance);
}

/*
 * Compare candidate distances
 */
static int
CompareNearestCandidates(const pairingheap_node *a, const pairingheap_node *b, void *arg)
{
	if (HnswGetSearchCandidateConst(c_node, a)->distance < HnswGetSearchCandidateConst(c_node, b)->distance)
		return 1;

	if (HnswGetSearchCandidateConst(c_node, a)->distance > HnswGetSearchCandidateConst(c_node, b)->distance)
		return -1;

	return 0;
}

/*
 * Compare discarded candidate distances
 */
static int
CompareNearestDiscardedCandidates(const pairingheap_node *a, const pairingheap_node *b, void *arg)
{
	if (HnswGetSearchCandidateConst(w_node, a)->distance < HnswGetSearchCandidateConst(w_node, b)->distance)
		return 1;

	if (HnswGetSearchCandidateConst(w_node, a)->distance > HnswGetSearchCandidateConst(w_node, b)->distance)
		return -1;

	return 0;
}

/*
 * Compare candidate distances
 */
static int
CompareFurthestCandidates(const pairingheap_node *a, const pairingheap_node *b, void *arg)
{
	if (HnswGetSearchCandidateConst(w_node, a)->distance < HnswGetSearchCandidateConst(w_node, b)->distance)
		return -1;

	if (HnswGetSearchCandidateConst(w_node, a)->distance > HnswGetSearchCandidateConst(w_node, b)->distance)
		return 1;

	return 0;
}

/*
 * Init visited
 */
static inline void
InitVisited(char *base, visited_hash * v, bool inMemory, int ef, int m)
{
	if (!inMemory)
		v->tids = tidhash_create(CurrentMemoryContext, ef * m * 2, NULL);
	else if (base != NULL)
		v->offsets = offsethash_create(CurrentMemoryContext, ef * m * 2, NULL);
	else
		v->pointers = pointerhash_create(CurrentMemoryContext, ef * m * 2, NULL);
}

/*
 * Add to visited
 */
static inline void
AddToVisited(char *base, visited_hash * v, HnswElementPtr elementPtr, bool inMemory, bool *found)
{
	if (!inMemory)
	{
		HnswElement element = HnswPtrAccess(base, elementPtr);
		ItemPointerData indextid;

		ItemPointerSet(&indextid, element->blkno, element->offno);
		tidhash_insert(v->tids, indextid, found);
	}
	else if (base != NULL)
	{
		HnswElement element = HnswPtrAccess(base, elementPtr);

		offsethash_insert_hash(v->offsets, HnswPtrOffset(elementPtr), element->hash, found);
	}
	else
	{
		HnswElement element = HnswPtrAccess(base, elementPtr);

		pointerhash_insert_hash(v->pointers, (uintptr_t) HnswPtrPointer(elementPtr), element->hash, found);
	}
}

/*
 * Count element towards ef
 */
static inline bool
CountElement(HnswElement skipElement, HnswElement e)
{
	if (skipElement == NULL)
		return true;

	/* Ensure does not access heaptidsLength during in-memory build */
	pg_memory_barrier();

	/* Keep scan-build happy on Mac x86-64 */
	Assert(e);

	return e->heaptidsLength != 0;
}

/*
 * Load unvisited neighbors from memory
 */
static void
HnswLoadUnvisitedFromMemory(char *base, HnswElement element, HnswUnvisited * unvisited, int *unvisitedLength, visited_hash * v, int lc, HnswNeighborArray * localNeighborhood, Size neighborhoodSize)
{
	/* Get the neighborhood at layer lc */
	HnswNeighborArray *neighborhood = HnswGetNeighbors(base, element, lc);

	/* Copy neighborhood to local memory */
	LWLockAcquire(&element->lock, LW_SHARED);
	memcpy(localNeighborhood, neighborhood, neighborhoodSize);
	LWLockRelease(&element->lock);

	*unvisitedLength = 0;

	for (int i = 0; i < localNeighborhood->length; i++)
	{
		HnswCandidate *hc = &localNeighborhood->items[i];
		bool		found;

		AddToVisited(base, v, hc->element, true, &found);

		if (!found)
			unvisited[(*unvisitedLength)++].element = HnswPtrAccess(base, hc->element);
	}
}

/*
 * Load neighbor index TIDs
 */
bool
HnswLoadNeighborTids(HnswElement element, ItemPointerData *indextids, Relation index, int m, int lm, int lc)
{
	Buffer		buf;
	Page		page;
	HnswNeighborTuple ntup;
	int			start;

	buf = ReadBuffer(index, element->neighborPage);
	LockBuffer(buf, BUFFER_LOCK_SHARE);
	page = BufferGetPage(buf);

	ntup = (HnswNeighborTuple) PageGetItem(page, PageGetItemId(page, element->neighborOffno));

	/*
	 * Ensure the neighbor tuple has not been deleted or replaced between
	 * index scan iterations
	 */
	if (ntup->version != element->version || ntup->count != (element->level + 2) * m)
	{
		UnlockReleaseBuffer(buf);
		return false;
	}

	/* Copy to minimize lock time */
	start = (element->level - lc) * m;
	memcpy(indextids, ntup->indextids + start, lm * sizeof(ItemPointerData));

	UnlockReleaseBuffer(buf);
	return true;
}

/*
 * Load unvisited neighbors from disk
 */
static void
HnswLoadUnvisitedFromDisk(HnswElement element, HnswUnvisited * unvisited, int *unvisitedLength, visited_hash * v, Relation index, int m, int lm, int lc)
{
	ItemPointerData indextids[HNSW_MAX_M * 2];

	*unvisitedLength = 0;

	if (!HnswLoadNeighborTids(element, indextids, index, m, lm, lc))
		return;

	for (int i = 0; i < lm; i++)
	{
		ItemPointer indextid = &indextids[i];
		bool		found;

		if (!ItemPointerIsValid(indextid))
			break;

		tidhash_insert(v->tids, *indextid, &found);

		if (!found)
			unvisited[(*unvisitedLength)++].indextid = *indextid;
	}
}

/*
 * Algorithm 2 from paper
 */
List *
HnswSearchLayer(char *base, HnswQuery * q, List *ep, int ef, int lc, Relation index, HnswSupport * support, int m, bool inserting, HnswElement skipElement, visited_hash * v, pairingheap **discarded, bool initVisited, int64 *tuples)
{
	List	   *w = NIL;
	pairingheap *C = pairingheap_allocate(CompareNearestCandidates, NULL);
	pairingheap *W = pairingheap_allocate(CompareFurthestCandidates, NULL);
	int			wlen = 0;
	visited_hash vh;
	ListCell   *lc2;
	HnswNeighborArray *localNeighborhood = NULL;
	Size		neighborhoodSize = 0;
	int			lm = HnswGetLayerM(m, lc);
	HnswUnvisited *unvisited = palloc(lm * sizeof(HnswUnvisited));
	int			unvisitedLength;
	bool		inMemory = index == NULL;

	if (v == NULL)
	{
		v = &vh;
		initVisited = true;
	}

	if (initVisited)
	{
		InitVisited(base, v, inMemory, ef, m);

		if (discarded != NULL)
			*discarded = pairingheap_allocate(CompareNearestDiscardedCandidates, NULL);
	}

	/* Create local memory for neighborhood if needed */
	if (inMemory)
	{
		neighborhoodSize = HNSW_NEIGHBOR_ARRAY_SIZE(lm);
		localNeighborhood = palloc(neighborhoodSize);
	}

	/* Add entry points to v, C, and W */
	foreach(lc2, ep)
	{
		HnswSearchCandidate *sc = (HnswSearchCandidate *) lfirst(lc2);
		bool		found;

		if (initVisited)
		{
			AddToVisited(base, v, sc->element, inMemory, &found);

			/* OK to count elements instead of tuples */
			if (tuples != NULL)
				(*tuples)++;
		}

		pairingheap_add(C, &sc->c_node);
		pairingheap_add(W, &sc->w_node);

		/*
		 * Do not count elements being deleted towards ef when vacuuming. It
		 * would be ideal to do this for inserts as well, but this could
		 * affect insert performance.
		 */
		if (CountElement(skipElement, HnswPtrAccess(base, sc->element)))
			wlen++;
	}

	while (!pairingheap_is_empty(C))
	{
		HnswSearchCandidate *c = HnswGetSearchCandidate(c_node, pairingheap_remove_first(C));
		HnswSearchCandidate *f = HnswGetSearchCandidate(w_node, pairingheap_first(W));
		HnswElement cElement;

		if (c->distance > f->distance)
			break;

		cElement = HnswPtrAccess(base, c->element);

		if (inMemory)
			HnswLoadUnvisitedFromMemory(base, cElement, unvisited, &unvisitedLength, v, lc, localNeighborhood, neighborhoodSize);
		else
			HnswLoadUnvisitedFromDisk(cElement, unvisited, &unvisitedLength, v, index, m, lm, lc);

		/* OK to count elements instead of tuples */
		if (tuples != NULL)
			(*tuples) += unvisitedLength;

		for (int i = 0; i < unvisitedLength; i++)
		{
			HnswElement eElement;
			HnswSearchCandidate *e;
			double		eDistance;
			bool		alwaysAdd = wlen < ef;

			f = HnswGetSearchCandidate(w_node, pairingheap_first(W));

			if (inMemory)
			{
				eElement = unvisited[i].element;
				eDistance = GetElementDistance(base, eElement, q, support);
			}
			else
			{
				ItemPointer indextid = &unvisited[i].indextid;
				BlockNumber blkno = ItemPointerGetBlockNumber(indextid);
				OffsetNumber offno = ItemPointerGetOffsetNumber(indextid);

				/* Avoid any allocations if not adding */
				eElement = NULL;
				HnswLoadElementImpl(blkno, offno, &eDistance, q, index, support, inserting, alwaysAdd || discarded != NULL ? NULL : &f->distance, &eElement);

				if (eElement == NULL)
					continue;
			}

			if (!(eDistance < f->distance || alwaysAdd))
			{
				if (discarded != NULL)
				{
					/* Create a new candidate */
					e = HnswInitSearchCandidate(base, eElement, eDistance);
					pairingheap_add(*discarded, &e->w_node);
				}

				continue;
			}

			/* Make robust to issues */
			if (eElement->level < lc)
				continue;

			/* Create a new candidate */
			e = HnswInitSearchCandidate(base, eElement, eDistance);
			pairingheap_add(C, &e->c_node);
			pairingheap_add(W, &e->w_node);

			/*
			 * Do not count elements being deleted towards ef when vacuuming.
			 * It would be ideal to do this for inserts as well, but this
			 * could affect insert performance.
			 */
			if (CountElement(skipElement, eElement))
			{
				wlen++;

				/* No need to decrement wlen */
				if (wlen > ef)
				{
					HnswSearchCandidate *d = HnswGetSearchCandidate(w_node, pairingheap_remove_first(W));

					if (discarded != NULL)
						pairingheap_add(*discarded, &d->w_node);
				}
			}
		}
	}

	/* Add each element of W to w */
	while (!pairingheap_is_empty(W))
	{
		HnswSearchCandidate *sc = HnswGetSearchCandidate(w_node, pairingheap_remove_first(W));

		w = lappend(w, sc);
	}

	return w;
}

/*
 * Compare candidate distances with pointer tie-breaker
 */
static int
CompareCandidateDistances(const ListCell *a, const ListCell *b)
{
	HnswCandidate *hca = lfirst(a);
	HnswCandidate *hcb = lfirst(b);

	if (hca->distance < hcb->distance)
		return 1;

	if (hca->distance > hcb->distance)
		return -1;

	if (HnswPtrPointer(hca->element) < HnswPtrPointer(hcb->element))
		return 1;

	if (HnswPtrPointer(hca->element) > HnswPtrPointer(hcb->element))
		return -1;

	return 0;
}

/*
 * Compare candidate distances with offset tie-breaker
 */
static int
CompareCandidateDistancesOffset(const ListCell *a, const ListCell *b)
{
	HnswCandidate *hca = lfirst(a);
	HnswCandidate *hcb = lfirst(b);

	if (hca->distance < hcb->distance)
		return 1;

	if (hca->distance > hcb->distance)
		return -1;

	if (HnswPtrOffset(hca->element) < HnswPtrOffset(hcb->element))
		return 1;

	if (HnswPtrOffset(hca->element) > HnswPtrOffset(hcb->element))
		return -1;

	return 0;
}

/*
 * Check if an element is closer to q than any element from R
 */
static bool
CheckElementCloser(char *base, HnswCandidate * e, List *r, HnswSupport * support)
{
	HnswElement eElement = HnswPtrAccess(base, e->element);
	Datum		eValue = HnswGetValue(base, eElement);
	ListCell   *lc2;

	foreach(lc2, r)
	{
		HnswCandidate *ri = lfirst(lc2);
		HnswElement riElement = HnswPtrAccess(base, ri->element);
		Datum		riValue = HnswGetValue(base, riElement);
		float		distance = HnswGetDistance(eValue, riValue, support);

		if (distance <= e->distance)
			return false;
	}

	return true;
}

/*
 * Algorithm 4 from paper
 */
static List *
SelectNeighbors(char *base, List *c, int lm, HnswSupport * support, bool *closerSet, HnswCandidate * newCandidate, HnswCandidate * *pruned, bool sortCandidates)
{
	List	   *r = NIL;
	List	   *w = list_copy(c);
	HnswCandidate **wd;
	int			wdlen = 0;
	int			wdoff = 0;
	bool		mustCalculate = !(*closerSet);
	List	   *added = NIL;
	bool		removedAny = false;

	if (list_length(w) <= lm)
		return w;

	wd = palloc(sizeof(HnswCandidate *) * list_length(w));

	/* Ensure order of candidates is deterministic for closer caching */
	if (sortCandidates)
	{
		if (base == NULL)
			list_sort(w, CompareCandidateDistances);
		else
			list_sort(w, CompareCandidateDistancesOffset);
	}

	while (list_length(w) > 0 && list_length(r) < lm)
	{
		/* Assumes w is already ordered desc */
		HnswCandidate *e = llast(w);

		w = list_delete_last(w);

		/* Use previous state of r and wd to skip work when possible */
		if (mustCalculate)
			e->closer = CheckElementCloser(base, e, r, support);
		else if (list_length(added) > 0)
		{
			/* Keep Valgrind happy for in-memory, parallel builds */
			if (base != NULL)
				VALGRIND_MAKE_MEM_DEFINED(&e->closer, 1);

			/*
			 * If the current candidate was closer, we only need to compare it
			 * with the other candidates that we have added.
			 */
			if (e->closer)
			{
				e->closer = CheckElementCloser(base, e, added, support);

				if (!e->closer)
					removedAny = true;
			}
			else
			{
				/*
				 * If we have removed any candidates from closer, a candidate
				 * that was not closer earlier might now be.
				 */
				if (removedAny)
				{
					e->closer = CheckElementCloser(base, e, r, support);
					if (e->closer)
						added = lappend(added, e);
				}
			}
		}
		else if (e == newCandidate)
		{
			e->closer = CheckElementCloser(base, e, r, support);
			if (e->closer)
				added = lappend(added, e);
		}

		/* Keep Valgrind happy for in-memory, parallel builds */
		if (base != NULL)
			VALGRIND_MAKE_MEM_DEFINED(&e->closer, 1);

		if (e->closer)
			r = lappend(r, e);
		else
			wd[wdlen++] = e;
	}

	/* Cached value can only be used in future if sorted deterministically */
	*closerSet = sortCandidates;

	/* Keep pruned connections */
	while (wdoff < wdlen && list_length(r) < lm)
		r = lappend(r, wd[wdoff++]);

	/* Return pruned for update connections */
	if (pruned != NULL)
	{
		if (wdoff < wdlen)
			*pruned = wd[wdoff];
		else
			*pruned = linitial(w);
	}

	return r;
}

/*
 * Add connections
 */
static void
AddConnections(char *base, HnswElement element, List *neighbors, int lc)
{
	ListCell   *lc2;
	HnswNeighborArray *a = HnswGetNeighbors(base, element, lc);

	foreach(lc2, neighbors)
		a->items[a->length++] = *((HnswCandidate *) lfirst(lc2));
}

/*
 * Update connections
 */
void
HnswUpdateConnection(char *base, HnswNeighborArray * neighbors, HnswElement newElement, float distance, int lm, int *updateIdx, Relation index, HnswSupport * support)
{
	HnswCandidate newHc;

	HnswPtrStore(base, newHc.element, newElement);
	newHc.distance = distance;

	if (neighbors->length < lm)
	{
		neighbors->items[neighbors->length++] = newHc;

		/* Track update */
		if (updateIdx != NULL)
			*updateIdx = -2;
	}
	else
	{
		/* Shrink connections */
		List	   *c = NIL;
		HnswCandidate *pruned = NULL;

		/* Add candidates */
		for (int i = 0; i < neighbors->length; i++)
			c = lappend(c, &neighbors->items[i]);
		c = lappend(c, &newHc);

		SelectNeighbors(base, c, lm, support, &neighbors->closerSet, &newHc, &pruned, true);

		/* Should not happen */
		if (pruned == NULL)
			return;

		/* Find and replace the pruned element */
		for (int i = 0; i < neighbors->length; i++)
		{
			if (HnswPtrEqual(base, neighbors->items[i].element, pruned->element))
			{
				neighbors->items[i] = newHc;

				/* Track update */
				if (updateIdx != NULL)
					*updateIdx = i;

				break;
			}
		}
	}
}

/*
 * Remove elements being deleted or skipped
 */
static List *
RemoveElements(char *base, List *w, HnswElement skipElement)
{
	ListCell   *lc2;
	List	   *w2 = NIL;

	/* Ensure does not access heaptidsLength during in-memory build */
	pg_memory_barrier();

	foreach(lc2, w)
	{
		HnswCandidate *hc = (HnswCandidate *) lfirst(lc2);
		HnswElement hce = HnswPtrAccess(base, hc->element);

		/* Skip self for vacuuming update */
		if (skipElement != NULL && hce->blkno == skipElement->blkno && hce->offno == skipElement->offno)
			continue;

		if (hce->heaptidsLength != 0)
			w2 = lappend(w2, hc);
	}

	return w2;
}

/*
 * Precompute hash
 */
static void
PrecomputeHash(char *base, HnswElement element)
{
	HnswElementPtr ptr;

	HnswPtrStore(base, ptr, element);

	if (base == NULL)
		element->hash = hash_pointer((uintptr_t) HnswPtrPointer(ptr));
	else
		element->hash = hash_offset(HnswPtrOffset(ptr));
}

/*
 * Algorithm 1 from paper
 */
void
HnswFindElementNeighbors(char *base, HnswElement element, HnswElement entryPoint, Relation index, HnswSupport * support, int m, int efConstruction, bool existing)
{
	List	   *ep;
	List	   *w;
	int			level = element->level;
	int			entryLevel;
	HnswQuery	q;
	HnswElement skipElement = existing ? element : NULL;
	bool		inMemory = index == NULL;

	q.value = HnswGetValue(base, element);

	/* Precompute hash */
	if (inMemory)
		PrecomputeHash(base, element);

	/* No neighbors if no entry point */
	if (entryPoint == NULL)
		return;

	/* Get entry point and level */
	ep = list_make1(HnswEntryCandidate(base, entryPoint, &q, index, support, true));
	entryLevel = entryPoint->level;

	/* 1st phase: greedy search to insert level */
	for (int lc = entryLevel; lc >= level + 1; lc--)
	{
		w = HnswSearchLayer(base, &q, ep, 1, lc, index, support, m, true, skipElement, NULL, NULL, true, NULL);
		ep = w;
	}

	if (level > entryLevel)
		level = entryLevel;

	/* Add one for existing element */
	if (existing)
		efConstruction++;

	/* 2nd phase */
	for (int lc = level; lc >= 0; lc--)
	{
		int			lm = HnswGetLayerM(m, lc);
		List	   *neighbors;
		List	   *lw = NIL;
		ListCell   *lc2;

		w = HnswSearchLayer(base, &q, ep, efConstruction, lc, index, support, m, true, skipElement, NULL, NULL, true, NULL);

		/* Convert search candidates to candidates */
		foreach(lc2, w)
		{
			HnswSearchCandidate *sc = lfirst(lc2);
			HnswCandidate *hc = palloc(sizeof(HnswCandidate));

			hc->element = sc->element;
			hc->distance = sc->distance;

			lw = lappend(lw, hc);
		}

		/* Elements being deleted or skipped can help with search */
		/* but should be removed before selecting neighbors */
		if (!inMemory)
			lw = RemoveElements(base, lw, skipElement);

		/*
		 * Candidates are sorted, but not deterministically. Could set
		 * sortCandidates to true for in-memory builds to enable closer
		 * caching, but there does not seem to be a difference in performance.
		 */
		neighbors = SelectNeighbors(base, lw, lm, support, &HnswGetNeighbors(base, element, lc)->closerSet, NULL, NULL, false);

		AddConnections(base, element, neighbors, lc);

		ep = w;
	}
}

PGDLLEXPORT Datum l2_normalize(PG_FUNCTION_ARGS);
PGDLLEXPORT Datum halfvec_l2_normalize(PG_FUNCTION_ARGS);
PGDLLEXPORT Datum sparsevec_l2_normalize(PG_FUNCTION_ARGS);

static void
SparsevecCheckValue(Pointer v)
{
	SparseVector *vec = (SparseVector *) v;

	if (vec->nnz > HNSW_MAX_NNZ)
		ereport(ERROR,
				(errcode(ERRCODE_PROGRAM_LIMIT_EXCEEDED),
				 errmsg("sparsevec cannot have more than %d non-zero elements for hnsw index", HNSW_MAX_NNZ)));
}

/*
 * Get type info
 */
const		HnswTypeInfo *
HnswGetTypeInfo(Relation index)
{
	FmgrInfo   *procinfo = HnswOptionalProcInfo(index, HNSW_TYPE_INFO_PROC);

	if (procinfo == NULL)
	{
		static const HnswTypeInfo typeInfo = {
			.maxDimensions = HNSW_MAX_DIM,
			.normalize = l2_normalize,
			.checkValue = NULL
		};

		return (&typeInfo);
	}
	else
		return (const HnswTypeInfo *) DatumGetPointer(FunctionCall0Coll(procinfo, InvalidOid));
}

FUNCTION_PREFIX PG_FUNCTION_INFO_V1(hnsw_halfvec_support);
Datum
hnsw_halfvec_support(PG_FUNCTION_ARGS)
{
	static const HnswTypeInfo typeInfo = {
		.maxDimensions = HNSW_MAX_DIM * 2,
		.normalize = halfvec_l2_normalize,
		.checkValue = NULL
	};

	PG_RETURN_POINTER(&typeInfo);
}

FUNCTION_PREFIX PG_FUNCTION_INFO_V1(hnsw_bit_support);
Datum
hnsw_bit_support(PG_FUNCTION_ARGS)
{
	static const HnswTypeInfo typeInfo = {
		.maxDimensions = HNSW_MAX_DIM * 32,
		.normalize = NULL,
		.checkValue = NULL
	};

	PG_RETURN_POINTER(&typeInfo);
}

FUNCTION_PREFIX PG_FUNCTION_INFO_V1(hnsw_sparsevec_support);
Datum
hnsw_sparsevec_support(PG_FUNCTION_ARGS)
{
	static const HnswTypeInfo typeInfo = {
		.maxDimensions = SPARSEVEC_MAX_DIM,
		.normalize = sparsevec_l2_normalize,
		.checkValue = SparsevecCheckValue
	};

	PG_RETURN_POINTER(&typeInfo);
}
```

## File: `src/hnswvacuum.c`
```c
#include "postgres.h"

#include "access/genam.h"
#include "access/generic_xlog.h"
#include "commands/vacuum.h"
#include "hnsw.h"
#include "nodes/pg_list.h"
#include "storage/bufmgr.h"
#include "storage/lmgr.h"
#include "utils/memutils.h"
#include "utils/rel.h"

#if PG_VERSION_NUM >= 160000
#include "varatt.h"
#endif

#if PG_VERSION_NUM >= 180000
#define vacuum_delay_point() vacuum_delay_point(false)
#endif

/*
 * Check if deleted list contains an index TID
 */
static bool
DeletedContains(tidhash_hash * deleted, ItemPointer indextid)
{
	return tidhash_lookup(deleted, *indextid) != NULL;
}

/*
 * Remove deleted heap TIDs
 *
 * OK to remove for entry point, since always considered for searches and inserts
 */
static void
RemoveHeapTids(HnswVacuumState * vacuumstate)
{
	BlockNumber blkno = HNSW_HEAD_BLKNO;
	HnswElement highestPoint = &vacuumstate->highestPoint;
	Relation	index = vacuumstate->index;
	BufferAccessStrategy bas = vacuumstate->bas;
	HnswElement entryPoint = HnswGetEntryPoint(vacuumstate->index);
	IndexBulkDeleteResult *stats = vacuumstate->stats;

	/* Store separately since highestPoint.level is uint8 */
	int			highestLevel = -1;

	/* Initialize highest point */
	highestPoint->blkno = InvalidBlockNumber;
	highestPoint->offno = InvalidOffsetNumber;

	while (BlockNumberIsValid(blkno))
	{
		Buffer		buf;
		Page		page;
		GenericXLogState *state;
		OffsetNumber offno;
		OffsetNumber maxoffno;
		bool		updated = false;

		vacuum_delay_point();

		buf = ReadBufferExtended(index, MAIN_FORKNUM, blkno, RBM_NORMAL, bas);
		LockBuffer(buf, BUFFER_LOCK_EXCLUSIVE);
		state = GenericXLogStart(index);
		page = GenericXLogRegisterBuffer(state, buf, 0);
		maxoffno = PageGetMaxOffsetNumber(page);

		/* Iterate over nodes */
		for (offno = FirstOffsetNumber; offno <= maxoffno; offno = OffsetNumberNext(offno))
		{
			HnswElementTuple etup = (HnswElementTuple) PageGetItem(page, PageGetItemId(page, offno));
			int			idx = 0;
			bool		itemUpdated = false;

			/* Skip neighbor tuples */
			if (!HnswIsElementTuple(etup))
				continue;

			if (ItemPointerIsValid(&etup->heaptids[0]))
			{
				for (int i = 0; i < HNSW_HEAPTIDS; i++)
				{
					/* Stop at first unused */
					if (!ItemPointerIsValid(&etup->heaptids[i]))
						break;

					if (vacuumstate->callback(&etup->heaptids[i], vacuumstate->callback_state))
					{
						itemUpdated = true;
						stats->tuples_removed++;
					}
					else
					{
						/* Move to front of list */
						etup->heaptids[idx++] = etup->heaptids[i];
						stats->num_index_tuples++;
					}
				}

				if (itemUpdated)
				{
					/* Mark rest as invalid */
					for (int i = idx; i < HNSW_HEAPTIDS; i++)
						ItemPointerSetInvalid(&etup->heaptids[i]);

					updated = true;
				}
			}

			if (!ItemPointerIsValid(&etup->heaptids[0]))
			{
				ItemPointerData ip;
				bool		found;

				/* Add to deleted list */
				ItemPointerSet(&ip, blkno, offno);

				tidhash_insert(vacuumstate->deleted, ip, &found);
				Assert(!found);
			}
			else if (etup->level > highestLevel && !(entryPoint != NULL && blkno == entryPoint->blkno && offno == entryPoint->offno))
			{
				/* Keep track of highest non-entry point */
				highestPoint->blkno = blkno;
				highestPoint->offno = offno;
				highestPoint->level = etup->level;
				highestLevel = etup->level;
			}
		}

		blkno = HnswPageGetOpaque(page)->nextblkno;

		if (updated)
			GenericXLogFinish(state);
		else
			GenericXLogAbort(state);

		UnlockReleaseBuffer(buf);
	}
}

/*
 * Check for deleted neighbors
 */
static bool
NeedsUpdated(HnswVacuumState * vacuumstate, HnswElement element)
{
	Relation	index = vacuumstate->index;
	BufferAccessStrategy bas = vacuumstate->bas;
	Buffer		buf;
	Page		page;
	HnswNeighborTuple ntup;
	bool		needsUpdated = false;

	buf = ReadBufferExtended(index, MAIN_FORKNUM, element->neighborPage, RBM_NORMAL, bas);
	LockBuffer(buf, BUFFER_LOCK_SHARE);
	page = BufferGetPage(buf);
	ntup = (HnswNeighborTuple) PageGetItem(page, PageGetItemId(page, element->neighborOffno));

	Assert(HnswIsNeighborTuple(ntup));

	/* Check neighbors */
	for (int i = 0; i < ntup->count; i++)
	{
		ItemPointer indextid = &ntup->indextids[i];

		if (!ItemPointerIsValid(indextid))
			continue;

		/* Check if in deleted list */
		if (DeletedContains(vacuumstate->deleted, indextid))
		{
			needsUpdated = true;
			break;
		}
	}

	/* Also update if layer 0 is not full */
	/* This could indicate too many candidates being deleted during insert */
	if (!needsUpdated)
	{
		/* Keep clang-tidy happy */
		Assert(ntup->count > 0);

		needsUpdated = !ItemPointerIsValid(&ntup->indextids[ntup->count - 1]);
	}

	UnlockReleaseBuffer(buf);

	return needsUpdated;
}

/*
 * Repair graph for a single element
 */
static void
RepairGraphElement(HnswVacuumState * vacuumstate, HnswElement element, HnswElement entryPoint)
{
	Relation	index = vacuumstate->index;
	HnswSupport *support = &vacuumstate->support;
	Buffer		buf;
	Page		page;
	GenericXLogState *state;
	int			m = vacuumstate->m;
	int			efConstruction = vacuumstate->efConstruction;
	BufferAccessStrategy bas = vacuumstate->bas;
	HnswNeighborTuple ntup = vacuumstate->ntup;
	Size		ntupSize = HNSW_NEIGHBOR_TUPLE_SIZE(element->level, m);
	char	   *base = NULL;

	/* Skip if element is entry point */
	if (entryPoint != NULL && element->blkno == entryPoint->blkno && element->offno == entryPoint->offno)
		return;

	/* Init fields */
	HnswInitNeighbors(base, element, m, NULL);
	element->heaptidsLength = 0;

	/* Find neighbors for element, skipping itself */
	HnswFindElementNeighbors(base, element, entryPoint, index, support, m, efConstruction, true);

	/* Zero memory for each element */
	MemSet(ntup, 0, HNSW_TUPLE_ALLOC_SIZE);

	/* Update neighbor tuple */
	/* Do this before getting page to minimize locking */
	HnswSetNeighborTuple(base, ntup, element, m);

	/* Get neighbor page */
	buf = ReadBufferExtended(index, MAIN_FORKNUM, element->neighborPage, RBM_NORMAL, bas);
	LockBuffer(buf, BUFFER_LOCK_EXCLUSIVE);
	state = GenericXLogStart(index);
	page = GenericXLogRegisterBuffer(state, buf, 0);

	/* Overwrite tuple */
	if (!PageIndexTupleOverwrite(page, element->neighborOffno, (Item) ntup, ntupSize))
		elog(ERROR, "failed to add index item to \"%s\"", RelationGetRelationName(index));

	/* Commit */
	GenericXLogFinish(state);
	UnlockReleaseBuffer(buf);

	/* Update neighbors */
	HnswUpdateNeighborsOnDisk(index, support, element, m, true, false);
}

/*
 * Repair graph entry point
 */
static void
RepairGraphEntryPoint(HnswVacuumState * vacuumstate)
{
	Relation	index = vacuumstate->index;
	HnswSupport *support = &vacuumstate->support;
	HnswElement highestPoint = &vacuumstate->highestPoint;
	HnswElement entryPoint;
	MemoryContext oldCtx = MemoryContextSwitchTo(vacuumstate->tmpCtx);

	if (!BlockNumberIsValid(highestPoint->blkno))
		highestPoint = NULL;

	/*
	 * Repair graph for highest non-entry point. Highest point may be outdated
	 * due to inserts that happen during and after RemoveHeapTids.
	 */
	if (highestPoint != NULL)
	{
		/* Get a shared lock */
		LockPage(index, HNSW_UPDATE_LOCK, ShareLock);

		/* Load element */
		HnswLoadElement(highestPoint, NULL, NULL, index, support, true, NULL);

		/* Repair if needed */
		if (NeedsUpdated(vacuumstate, highestPoint))
			RepairGraphElement(vacuumstate, highestPoint, HnswGetEntryPoint(index));

		/* Release lock */
		UnlockPage(index, HNSW_UPDATE_LOCK, ShareLock);
	}

	/* Prevent concurrent inserts when possibly updating entry point */
	LockPage(index, HNSW_UPDATE_LOCK, ExclusiveLock);

	/* Get latest entry point */
	entryPoint = HnswGetEntryPoint(index);

	if (entryPoint != NULL)
	{
		ItemPointerData epData;

		ItemPointerSet(&epData, entryPoint->blkno, entryPoint->offno);

		if (DeletedContains(vacuumstate->deleted, &epData))
		{
			/*
			 * Replace the entry point with the highest point. If highest
			 * point is outdated and empty, the entry point will be empty
			 * until an element is repaired.
			 */
			HnswUpdateMetaPage(index, HNSW_UPDATE_ENTRY_ALWAYS, highestPoint, InvalidBlockNumber, MAIN_FORKNUM, false);
		}
		else
		{
			/*
			 * Repair the entry point with the highest point. If highest point
			 * is outdated, this can remove connections at higher levels in
			 * the graph until they are repaired, but this should be fine.
			 */
			HnswLoadElement(entryPoint, NULL, NULL, index, support, true, NULL);

			if (NeedsUpdated(vacuumstate, entryPoint))
			{
				/* Reset neighbors from previous update */
				if (highestPoint != NULL)
					HnswPtrStore((char *) NULL, highestPoint->neighbors, (HnswNeighborArrayPtr *) NULL);

				RepairGraphElement(vacuumstate, entryPoint, highestPoint);
			}
		}
	}

	/* Release lock */
	UnlockPage(index, HNSW_UPDATE_LOCK, ExclusiveLock);

	/* Reset memory context */
	MemoryContextSwitchTo(oldCtx);
	MemoryContextReset(vacuumstate->tmpCtx);
}

/*
 * Repair graph for all elements
 */
static void
RepairGraph(HnswVacuumState * vacuumstate)
{
	Relation	index = vacuumstate->index;
	BufferAccessStrategy bas = vacuumstate->bas;
	BlockNumber blkno = HNSW_HEAD_BLKNO;

	/*
	 * Wait for inserts to complete. Inserts before this point may have
	 * neighbors about to be deleted. Inserts after this point will not.
	 */
	LockPage(index, HNSW_UPDATE_LOCK, ExclusiveLock);
	UnlockPage(index, HNSW_UPDATE_LOCK, ExclusiveLock);

	/* Repair entry point first */
	RepairGraphEntryPoint(vacuumstate);

	while (BlockNumberIsValid(blkno))
	{
		Buffer		buf;
		Page		page;
		OffsetNumber offno;
		OffsetNumber maxoffno;
		List	   *elements = NIL;
		ListCell   *lc2;
		MemoryContext oldCtx;

		vacuum_delay_point();

		oldCtx = MemoryContextSwitchTo(vacuumstate->tmpCtx);

		buf = ReadBufferExtended(index, MAIN_FORKNUM, blkno, RBM_NORMAL, bas);
		LockBuffer(buf, BUFFER_LOCK_SHARE);
		page = BufferGetPage(buf);
		maxoffno = PageGetMaxOffsetNumber(page);

		/* Load items into memory to minimize locking */
		for (offno = FirstOffsetNumber; offno <= maxoffno; offno = OffsetNumberNext(offno))
		{
			HnswElementTuple etup = (HnswElementTuple) PageGetItem(page, PageGetItemId(page, offno));
			HnswElement element;

			/* Skip neighbor tuples */
			if (!HnswIsElementTuple(etup))
				continue;

			/* Skip updating neighbors if being deleted */
			if (!ItemPointerIsValid(&etup->heaptids[0]))
				continue;

			/* Create an element */
			element = HnswInitElementFromBlock(blkno, offno);
			HnswLoadElementFromTuple(element, etup, false, true);

			elements = lappend(elements, element);
		}

		blkno = HnswPageGetOpaque(page)->nextblkno;

		UnlockReleaseBuffer(buf);

		/* Update neighbor pages */
		foreach(lc2, elements)
		{
			HnswElement element = (HnswElement) lfirst(lc2);
			HnswElement entryPoint;
			LOCKMODE	lockmode = ShareLock;

			/* Check if any neighbors point to deleted values */
			if (!NeedsUpdated(vacuumstate, element))
				continue;

			/* Get a shared lock */
			LockPage(index, HNSW_UPDATE_LOCK, lockmode);

			/* Refresh entry point for each element */
			entryPoint = HnswGetEntryPoint(index);

			/* Prevent concurrent inserts when likely updating entry point */
			if (entryPoint == NULL || element->level > entryPoint->level)
			{
				/* Release shared lock */
				UnlockPage(index, HNSW_UPDATE_LOCK, lockmode);

				/* Get exclusive lock */
				lockmode = ExclusiveLock;
				LockPage(index, HNSW_UPDATE_LOCK, lockmode);

				/* Get latest entry point after lock is acquired */
				entryPoint = HnswGetEntryPoint(index);
			}

			/* Repair connections */
			RepairGraphElement(vacuumstate, element, entryPoint);

			/*
			 * Update metapage if needed. Should only happen if entry point
			 * was replaced and highest point was outdated.
			 */
			if (entryPoint == NULL || element->level > entryPoint->level)
				HnswUpdateMetaPage(index, HNSW_UPDATE_ENTRY_GREATER, element, InvalidBlockNumber, MAIN_FORKNUM, false);

			/* Release lock */
			UnlockPage(index, HNSW_UPDATE_LOCK, lockmode);
		}

		/* Reset memory context */
		MemoryContextSwitchTo(oldCtx);
		MemoryContextReset(vacuumstate->tmpCtx);
	}
}

/*
 * Mark items as deleted
 */
static void
MarkDeleted(HnswVacuumState * vacuumstate)
{
	BlockNumber blkno = HNSW_HEAD_BLKNO;
	BlockNumber insertPage = InvalidBlockNumber;
	Relation	index = vacuumstate->index;
	BufferAccessStrategy bas = vacuumstate->bas;

	/*
	 * Wait for index scans to complete. Scans before this point may contain
	 * tuples about to be deleted. Scans after this point will not, since the
	 * graph has been repaired.
	 */
	LockPage(index, HNSW_SCAN_LOCK, ExclusiveLock);
	UnlockPage(index, HNSW_SCAN_LOCK, ExclusiveLock);

	while (BlockNumberIsValid(blkno))
	{
		Buffer		buf;
		Page		page;
		GenericXLogState *state;
		OffsetNumber offno;
		OffsetNumber maxoffno;

		vacuum_delay_point();

		buf = ReadBufferExtended(index, MAIN_FORKNUM, blkno, RBM_NORMAL, bas);

		/*
		 * ambulkdelete cannot delete entries from pages that are pinned by
		 * other backends
		 *
		 * https://www.postgresql.org/docs/current/index-locking.html
		 */
		LockBufferForCleanup(buf);

		state = GenericXLogStart(index);
		page = GenericXLogRegisterBuffer(state, buf, 0);
		maxoffno = PageGetMaxOffsetNumber(page);

		/* Update element and neighbors together */
		for (offno = FirstOffsetNumber; offno <= maxoffno; offno = OffsetNumberNext(offno))
		{
			HnswElementTuple etup = (HnswElementTuple) PageGetItem(page, PageGetItemId(page, offno));
			HnswNeighborTuple ntup;
			Buffer		nbuf;
			Page		npage;
			BlockNumber neighborPage;
			OffsetNumber neighborOffno;

			/* Skip neighbor tuples */
			if (!HnswIsElementTuple(etup))
				continue;

			/* Skip deleted tuples */
			if (etup->deleted)
			{
				/* Set to first free page */
				if (!BlockNumberIsValid(insertPage))
					insertPage = blkno;

				continue;
			}

			/* Skip live tuples */
			if (ItemPointerIsValid(&etup->heaptids[0]))
				continue;

			/* Get neighbor page */
			neighborPage = ItemPointerGetBlockNumber(&etup->neighbortid);
			neighborOffno = ItemPointerGetOffsetNumber(&etup->neighbortid);

			if (neighborPage == blkno)
			{
				nbuf = buf;
				npage = page;
			}
			else
			{
				nbuf = ReadBufferExtended(index, MAIN_FORKNUM, neighborPage, RBM_NORMAL, bas);
				LockBuffer(nbuf, BUFFER_LOCK_EXCLUSIVE);
				npage = GenericXLogRegisterBuffer(state, nbuf, 0);
			}

			ntup = (HnswNeighborTuple) PageGetItem(npage, PageGetItemId(npage, neighborOffno));

			/* Overwrite element */
			/* Use memset instead of MemSet to keep clang-tidy happy */
			etup->deleted = 1;
			memset(&etup->data, 0, VARSIZE_ANY(&etup->data));

			/* Overwrite neighbors */
			for (int i = 0; i < ntup->count; i++)
				ItemPointerSetInvalid(&ntup->indextids[i]);

			/* Increment version */
			/* This is used to avoid incorrect reads for iterative scans */
			/* Reserve some bits for future use */
			etup->version++;
			if (etup->version > 15)
				etup->version = 1;
			ntup->version = etup->version;

			/*
			 * We modified the tuples in place, no need to call
			 * PageIndexTupleOverwrite
			 */

			/* Commit */
			GenericXLogFinish(state);
			if (nbuf != buf)
				UnlockReleaseBuffer(nbuf);

			/* Set to first free page */
			if (!BlockNumberIsValid(insertPage))
				insertPage = blkno;

			/* Prepare new xlog */
			state = GenericXLogStart(index);
			page = GenericXLogRegisterBuffer(state, buf, 0);
		}

		blkno = HnswPageGetOpaque(page)->nextblkno;

		GenericXLogAbort(state);
		UnlockReleaseBuffer(buf);
	}

	/* Update insert page last, after everything has been marked as deleted */
	HnswUpdateMetaPage(index, 0, NULL, insertPage, MAIN_FORKNUM, false);
}

/*
 * Initialize the vacuum state
 */
static void
InitVacuumState(HnswVacuumState * vacuumstate, IndexVacuumInfo *info, IndexBulkDeleteResult *stats, IndexBulkDeleteCallback callback, void *callback_state)
{
	Relation	index = info->index;

	if (stats == NULL)
		stats = (IndexBulkDeleteResult *) palloc0(sizeof(IndexBulkDeleteResult));

	vacuumstate->index = index;
	vacuumstate->stats = stats;
	vacuumstate->callback = callback;
	vacuumstate->callback_state = callback_state;
	vacuumstate->efConstruction = HnswGetEfConstruction(index);
	vacuumstate->bas = GetAccessStrategy(BAS_BULKREAD);
	vacuumstate->ntup = palloc0(HNSW_TUPLE_ALLOC_SIZE);
	vacuumstate->tmpCtx = AllocSetContextCreate(CurrentMemoryContext,
												"Hnsw vacuum temporary context",
												ALLOCSET_DEFAULT_SIZES);

	HnswInitSupport(&vacuumstate->support, index);

	/* Get m from metapage */
	HnswGetMetaPageInfo(index, &vacuumstate->m, NULL);

	/* Create hash table */
	vacuumstate->deleted = tidhash_create(CurrentMemoryContext, 256, NULL);
}

/*
 * Free resources
 */
static void
FreeVacuumState(HnswVacuumState * vacuumstate)
{
	tidhash_destroy(vacuumstate->deleted);
	FreeAccessStrategy(vacuumstate->bas);
	pfree(vacuumstate->ntup);
	MemoryContextDelete(vacuumstate->tmpCtx);
}

/*
 * Bulk delete tuples from the index
 */
IndexBulkDeleteResult *
hnswbulkdelete(IndexVacuumInfo *info, IndexBulkDeleteResult *stats,
			   IndexBulkDeleteCallback callback, void *callback_state)
{
	HnswVacuumState vacuumstate;

	InitVacuumState(&vacuumstate, info, stats, callback, callback_state);

	/* Pass 1: Remove heap TIDs */
	RemoveHeapTids(&vacuumstate);

	/* Pass 2: Repair graph */
	RepairGraph(&vacuumstate);

	/* Pass 3: Mark as deleted */
	MarkDeleted(&vacuumstate);

	FreeVacuumState(&vacuumstate);

	return vacuumstate.stats;
}

/*
 * Clean up after a VACUUM operation
 */
IndexBulkDeleteResult *
hnswvacuumcleanup(IndexVacuumInfo *info, IndexBulkDeleteResult *stats)
{
	Relation	rel = info->index;

	if (info->analyze_only)
		return stats;

	/* stats is NULL if ambulkdelete not called */
	/* OK to return NULL if index not changed */
	if (stats == NULL)
		return NULL;

	stats->num_pages = RelationGetNumberOfBlocks(rel);

	return stats;
}
```

## File: `src/ivfbuild.c`
```c
#include "postgres.h"

#include <float.h>

#include "access/genam.h"
#include "access/generic_xlog.h"
#include "access/itup.h"
#include "access/relscan.h"
#include "access/table.h"
#include "access/tableam.h"
#include "access/tupdesc.h"
#include "access/parallel.h"
#include "access/xact.h"
#include "access/xloginsert.h"
#include "catalog/index.h"
#include "catalog/pg_operator_d.h"
#include "catalog/pg_type_d.h"
#include "commands/progress.h"
#include "fmgr.h"
#include "ivfflat.h"
#include "miscadmin.h"
#include "nodes/execnodes.h"
#include "optimizer/optimizer.h"
#include "storage/bufmgr.h"
#include "tcop/tcopprot.h"
#include "utils/memutils.h"
#include "utils/rel.h"
#include "utils/sampling.h"
#include "utils/snapmgr.h"
#include "utils/tuplesort.h"

#if PG_VERSION_NUM >= 160000
#include "varatt.h"
#endif

#if PG_VERSION_NUM >= 140000
#include "utils/backend_progress.h"
#else
#include "pgstat.h"
#endif

#if PG_VERSION_NUM >= 140000
#include "utils/backend_status.h"
#include "utils/wait_event.h"
#endif

#define PARALLEL_KEY_IVFFLAT_SHARED		UINT64CONST(0xA000000000000001)
#define PARALLEL_KEY_TUPLESORT			UINT64CONST(0xA000000000000002)
#define PARALLEL_KEY_IVFFLAT_CENTERS	UINT64CONST(0xA000000000000003)
#define PARALLEL_KEY_QUERY_TEXT			UINT64CONST(0xA000000000000004)

/*
 * Add sample
 */
static void
AddSample(Datum *values, IvfflatBuildState * buildstate)
{
	VectorArray samples = buildstate->samples;
	int			targsamples = samples->maxlen;

	/* Detoast once for all calls */
	Datum		value = PointerGetDatum(PG_DETOAST_DATUM(values[0]));

	/*
	 * Normalize with KMEANS_NORM_PROC since spherical distance function
	 * expects unit vectors
	 */
	if (buildstate->kmeansnormprocinfo != NULL)
	{
		if (!IvfflatCheckNorm(buildstate->kmeansnormprocinfo, buildstate->collation, value))
			return;

		value = IvfflatNormValue(buildstate->typeInfo, buildstate->collation, value);
	}

	if (samples->length < targsamples)
	{
		VectorArraySet(samples, samples->length, DatumGetPointer(value));
		samples->length++;
	}
	else
	{
		if (buildstate->rowstoskip < 0)
			buildstate->rowstoskip = reservoir_get_next_S(&buildstate->rstate, samples->length, targsamples);

		if (buildstate->rowstoskip <= 0)
		{
#if PG_VERSION_NUM >= 150000
			int			k = (int) (targsamples * sampler_random_fract(&buildstate->rstate.randstate));
#else
			int			k = (int) (targsamples * sampler_random_fract(buildstate->rstate.randstate));
#endif

			Assert(k >= 0 && k < targsamples);
			VectorArraySet(samples, k, DatumGetPointer(value));
		}

		buildstate->rowstoskip -= 1;
	}
}

/*
 * Callback for sampling
 */
static void
SampleCallback(Relation index, ItemPointer tid, Datum *values,
			   bool *isnull, bool tupleIsAlive, void *state)
{
	IvfflatBuildState *buildstate = (IvfflatBuildState *) state;
	MemoryContext oldCtx;

	/* Skip nulls */
	if (isnull[0])
		return;

	/* Use memory context since detoast can allocate */
	oldCtx = MemoryContextSwitchTo(buildstate->tmpCtx);

	/* Add sample */
	AddSample(values, buildstate);

	/* Reset memory context */
	MemoryContextSwitchTo(oldCtx);
	MemoryContextReset(buildstate->tmpCtx);
}

/*
 * Sample rows with same logic as ANALYZE
 */
static void
SampleRows(IvfflatBuildState * buildstate)
{
	int			targsamples = buildstate->samples->maxlen;
	BlockNumber totalblocks = RelationGetNumberOfBlocks(buildstate->heap);

	buildstate->rowstoskip = -1;

	BlockSampler_Init(&buildstate->bs, totalblocks, targsamples, RandomInt());

	reservoir_init_selection_state(&buildstate->rstate, targsamples);
	while (BlockSampler_HasMore(&buildstate->bs))
	{
		BlockNumber targblock = BlockSampler_Next(&buildstate->bs);

		table_index_build_range_scan(buildstate->heap, buildstate->index, buildstate->indexInfo,
									 false, true, false, targblock, 1, SampleCallback, (void *) buildstate, NULL);
	}
}

/*
 * Add tuple to sort
 */
static void
AddTupleToSort(ItemPointer tid, Datum *values, IvfflatBuildState * buildstate)
{
	double		distance;
	double		minDistance = DBL_MAX;
	int			closestCenter = 0;
	VectorArray centers = buildstate->centers;
	TupleTableSlot *slot = buildstate->slot;

	/* Detoast once for all calls */
	Datum		value = PointerGetDatum(PG_DETOAST_DATUM(values[0]));

	/* Normalize if needed */
	if (buildstate->normprocinfo != NULL)
	{
		if (!IvfflatCheckNorm(buildstate->normprocinfo, buildstate->collation, value))
			return;

		value = IvfflatNormValue(buildstate->typeInfo, buildstate->collation, value);
	}

	/* Find the list that minimizes the distance */
	for (int i = 0; i < centers->length; i++)
	{
		distance = DatumGetFloat8(FunctionCall2Coll(buildstate->procinfo, buildstate->collation, value, PointerGetDatum(VectorArrayGet(centers, i))));

		if (distance < minDistance)
		{
			minDistance = distance;
			closestCenter = i;
		}
	}

#ifdef IVFFLAT_KMEANS_DEBUG
	buildstate->inertia += minDistance;
	buildstate->listSums[closestCenter] += minDistance;
	buildstate->listCounts[closestCenter]++;
#endif

	/* Create a virtual tuple */
	ExecClearTuple(slot);
	slot->tts_values[0] = Int32GetDatum(closestCenter);
	slot->tts_isnull[0] = false;
	slot->tts_values[1] = PointerGetDatum(tid);
	slot->tts_isnull[1] = false;
	slot->tts_values[2] = value;
	slot->tts_isnull[2] = false;
	ExecStoreVirtualTuple(slot);

	/*
	 * Add tuple to sort
	 *
	 * tuplesort_puttupleslot comment: Input data is always copied; the caller
	 * need not save it.
	 */
	tuplesort_puttupleslot(buildstate->sortstate, slot);

	buildstate->indtuples++;
}

/*
 * Callback for table_index_build_scan
 */
static void
BuildCallback(Relation index, ItemPointer tid, Datum *values,
			  bool *isnull, bool tupleIsAlive, void *state)
{
	IvfflatBuildState *buildstate = (IvfflatBuildState *) state;
	MemoryContext oldCtx;

	/* Skip nulls */
	if (isnull[0])
		return;

	/* Use memory context since detoast can allocate */
	oldCtx = MemoryContextSwitchTo(buildstate->tmpCtx);

	/* Add tuple to sort */
	AddTupleToSort(tid, values, buildstate);

	/* Reset memory context */
	MemoryContextSwitchTo(oldCtx);
	MemoryContextReset(buildstate->tmpCtx);
}

/*
 * Get index tuple from sort state
 */
static inline void
GetNextTuple(Tuplesortstate *sortstate, TupleDesc tupdesc, TupleTableSlot *slot, IndexTuple *itup, int *list)
{
	if (tuplesort_gettupleslot(sortstate, true, false, slot, NULL))
	{
		Datum		value;
		bool		isnull;

		*list = DatumGetInt32(slot_getattr(slot, 1, &isnull));
		value = slot_getattr(slot, 3, &isnull);

		/* Form the index tuple */
		*itup = index_form_tuple(tupdesc, &value, &isnull);
		(*itup)->t_tid = *((ItemPointer) DatumGetPointer(slot_getattr(slot, 2, &isnull)));
	}
	else
		*list = -1;
}

/*
 * Create initial entry pages
 */
static void
InsertTuples(Relation index, IvfflatBuildState * buildstate, ForkNumber forkNum)
{
	int			list;
	IndexTuple	itup = NULL;	/* silence compiler warning */
	int64		inserted = 0;

	TupleTableSlot *slot = MakeSingleTupleTableSlot(buildstate->sortdesc, &TTSOpsMinimalTuple);
	TupleDesc	tupdesc = buildstate->tupdesc;

	pgstat_progress_update_param(PROGRESS_CREATEIDX_SUBPHASE, PROGRESS_IVFFLAT_PHASE_LOAD);

	pgstat_progress_update_param(PROGRESS_CREATEIDX_TUPLES_TOTAL, buildstate->indtuples);

	GetNextTuple(buildstate->sortstate, tupdesc, slot, &itup, &list);

	for (int i = 0; i < buildstate->centers->length; i++)
	{
		Buffer		buf;
		Page		page;
		GenericXLogState *state;
		BlockNumber startPage;
		BlockNumber insertPage;

		/* Can take a while, so ensure we can interrupt */
		/* Needs to be called when no buffer locks are held */
		CHECK_FOR_INTERRUPTS();

		buf = IvfflatNewBuffer(index, forkNum);
		IvfflatInitRegisterPage(index, &buf, &page, &state);

		startPage = BufferGetBlockNumber(buf);

		/* Get all tuples for list */
		while (list == i)
		{
			/* Check for free space */
			Size		itemsz = MAXALIGN(IndexTupleSize(itup));

			if (PageGetFreeSpace(page) < itemsz)
				IvfflatAppendPage(index, &buf, &page, &state, forkNum);

			/* Add the item */
			if (PageAddItem(page, (Item) itup, itemsz, InvalidOffsetNumber, false, false) == InvalidOffsetNumber)
				elog(ERROR, "failed to add index item to \"%s\"", RelationGetRelationName(index));

			pfree(itup);

			pgstat_progress_update_param(PROGRESS_CREATEIDX_TUPLES_DONE, ++inserted);

			GetNextTuple(buildstate->sortstate, tupdesc, slot, &itup, &list);
		}

		insertPage = BufferGetBlockNumber(buf);

		IvfflatCommitBuffer(buf, state);

		/* Set the start and insert pages */
		IvfflatUpdateList(index, buildstate->listInfo[i], insertPage, InvalidBlockNumber, startPage, forkNum);
	}
}

/*
 * Initialize the build state
 */
static void
InitBuildState(IvfflatBuildState * buildstate, Relation heap, Relation index, IndexInfo *indexInfo)
{
	buildstate->heap = heap;
	buildstate->index = index;
	buildstate->indexInfo = indexInfo;
	buildstate->typeInfo = IvfflatGetTypeInfo(index);
	buildstate->tupdesc = RelationGetDescr(index);

	buildstate->lists = IvfflatGetLists(index);
	buildstate->dimensions = TupleDescAttr(index->rd_att, 0)->atttypmod;

	/* Disallow varbit since require fixed dimensions */
	if (TupleDescAttr(index->rd_att, 0)->atttypid == VARBITOID)
		ereport(ERROR,
				(errcode(ERRCODE_FEATURE_NOT_SUPPORTED),
				 errmsg("type not supported for ivfflat index")));

	/* Require column to have dimensions to be indexed */
	if (buildstate->dimensions < 0)
		ereport(ERROR,
				(errcode(ERRCODE_INVALID_PARAMETER_VALUE),
				 errmsg("column does not have dimensions")));

	if (buildstate->dimensions > buildstate->typeInfo->maxDimensions)
		ereport(ERROR,
				(errcode(ERRCODE_PROGRAM_LIMIT_EXCEEDED),
				 errmsg("column cannot have more than %d dimensions for ivfflat index", buildstate->typeInfo->maxDimensions)));

	buildstate->reltuples = 0;
	buildstate->indtuples = 0;

	/* Get support functions */
	buildstate->procinfo = index_getprocinfo(index, 1, IVFFLAT_DISTANCE_PROC);
	buildstate->normprocinfo = IvfflatOptionalProcInfo(index, IVFFLAT_NORM_PROC);
	buildstate->kmeansnormprocinfo = IvfflatOptionalProcInfo(index, IVFFLAT_KMEANS_NORM_PROC);
	buildstate->collation = index->rd_indcollation[0];

	/* Require more than one dimension for spherical k-means */
	if (buildstate->kmeansnormprocinfo != NULL && buildstate->dimensions == 1)
		ereport(ERROR,
				(errcode(ERRCODE_INVALID_PARAMETER_VALUE),
				 errmsg("dimensions must be greater than one for this opclass")));

	/* Create tuple description for sorting */
	buildstate->sortdesc = CreateTemplateTupleDesc(3);
	TupleDescInitEntry(buildstate->sortdesc, (AttrNumber) 1, "list", INT4OID, -1, 0);
	TupleDescInitEntry(buildstate->sortdesc, (AttrNumber) 2, "tid", TIDOID, -1, 0);
	TupleDescInitEntry(buildstate->sortdesc, (AttrNumber) 3, "vector", TupleDescAttr(buildstate->tupdesc, 0)->atttypid, -1, 0);

	buildstate->slot = MakeSingleTupleTableSlot(buildstate->sortdesc, &TTSOpsVirtual);

	buildstate->centers = VectorArrayInit(buildstate->lists, buildstate->dimensions, buildstate->typeInfo->itemSize(buildstate->dimensions));
	buildstate->listInfo = palloc(sizeof(ListInfo) * buildstate->lists);

	buildstate->tmpCtx = AllocSetContextCreate(CurrentMemoryContext,
											   "Ivfflat build temporary context",
											   ALLOCSET_DEFAULT_SIZES);

#ifdef IVFFLAT_KMEANS_DEBUG
	buildstate->inertia = 0;
	buildstate->listSums = palloc0(sizeof(double) * buildstate->lists);
	buildstate->listCounts = palloc0(sizeof(int) * buildstate->lists);
#endif

	buildstate->ivfleader = NULL;
}

/*
 * Free resources
 */
static void
FreeBuildState(IvfflatBuildState * buildstate)
{
	VectorArrayFree(buildstate->centers);
	pfree(buildstate->listInfo);

#ifdef IVFFLAT_KMEANS_DEBUG
	pfree(buildstate->listSums);
	pfree(buildstate->listCounts);
#endif

	MemoryContextDelete(buildstate->tmpCtx);
}

/*
 * Compute centers
 */
static void
ComputeCenters(IvfflatBuildState * buildstate)
{
	int			numSamples;

	pgstat_progress_update_param(PROGRESS_CREATEIDX_SUBPHASE, PROGRESS_IVFFLAT_PHASE_KMEANS);

	/* Target 50 samples per list, with at least 10000 samples */
	/* The number of samples has a large effect on index build time */
	numSamples = buildstate->lists * 50;
	if (numSamples < 10000)
		numSamples = 10000;

	/* Skip samples for unlogged table */
	if (buildstate->heap == NULL)
		numSamples = 1;

	/* Sample rows */
	/* TODO Ensure within maintenance_work_mem */
	buildstate->samples = VectorArrayInit(numSamples, buildstate->dimensions, buildstate->centers->itemsize);
	if (buildstate->heap != NULL)
	{
		SampleRows(buildstate);

		if (buildstate->samples->length < buildstate->lists)
		{
			ereport(NOTICE,
					(errmsg("ivfflat index created with little data"),
					 errdetail("This will cause low recall."),
					 errhint("Drop the index until the table has more data.")));
		}
	}

	/* Calculate centers */
	IvfflatBench("k-means", IvfflatKmeans(buildstate->index, buildstate->samples, buildstate->centers, buildstate->typeInfo));

	/* Free samples before we allocate more memory */
	VectorArrayFree(buildstate->samples);
}

/*
 * Create the metapage
 */
static void
CreateMetaPage(Relation index, int dimensions, int lists, ForkNumber forkNum)
{
	Buffer		buf;
	Page		page;
	GenericXLogState *state;
	IvfflatMetaPage metap;

	buf = IvfflatNewBuffer(index, forkNum);
	IvfflatInitRegisterPage(index, &buf, &page, &state);

	/* Set metapage data */
	metap = IvfflatPageGetMeta(page);
	metap->magicNumber = IVFFLAT_MAGIC_NUMBER;
	metap->version = IVFFLAT_VERSION;
	metap->dimensions = dimensions;
	metap->lists = lists;
	((PageHeader) page)->pd_lower =
		((char *) metap + sizeof(IvfflatMetaPageData)) - (char *) page;

	IvfflatCommitBuffer(buf, state);
}

/*
 * Create list pages
 */
static void
CreateListPages(Relation index, VectorArray centers, int lists,
				ForkNumber forkNum, ListInfo * *listInfo)
{
	Buffer		buf;
	Page		page;
	GenericXLogState *state;
	Size		listSize;
	IvfflatList list;

	listSize = MAXALIGN(IVFFLAT_LIST_SIZE(centers->itemsize));
	list = palloc0(listSize);

	buf = IvfflatNewBuffer(index, forkNum);
	IvfflatInitRegisterPage(index, &buf, &page, &state);

	for (int i = 0; i < lists; i++)
	{
		OffsetNumber offno;

		/* Zero memory for each list */
		MemSet(list, 0, listSize);

		/* Load list */
		list->startPage = InvalidBlockNumber;
		list->insertPage = InvalidBlockNumber;
		memcpy(&list->center, VectorArrayGet(centers, i), VARSIZE_ANY(VectorArrayGet(centers, i)));

		/* Ensure free space */
		if (PageGetFreeSpace(page) < listSize)
			IvfflatAppendPage(index, &buf, &page, &state, forkNum);

		/* Add the item */
		offno = PageAddItem(page, (Item) list, listSize, InvalidOffsetNumber, false, false);
		if (offno == InvalidOffsetNumber)
			elog(ERROR, "failed to add index item to \"%s\"", RelationGetRelationName(index));

		/* Save location info */
		(*listInfo)[i].blkno = BufferGetBlockNumber(buf);
		(*listInfo)[i].offno = offno;
	}

	IvfflatCommitBuffer(buf, state);

	pfree(list);
}

#ifdef IVFFLAT_KMEANS_DEBUG
/*
 * Print k-means metrics
 */
static void
PrintKmeansMetrics(IvfflatBuildState * buildstate)
{
	elog(INFO, "inertia: %.3e", buildstate->inertia);

	/* Calculate Davies-Bouldin index */
	if (buildstate->lists > 1 && !buildstate->ivfleader)
	{
		double		db = 0.0;

		/* Calculate average distance */
		for (int i = 0; i < buildstate->lists; i++)
		{
			if (buildstate->listCounts[i] > 0)
				buildstate->listSums[i] /= buildstate->listCounts[i];
		}

		for (int i = 0; i < buildstate->lists; i++)
		{
			double		max = 0.0;
			double		distance;

			for (int j = 0; j < buildstate->lists; j++)
			{
				if (j == i)
					continue;

				distance = DatumGetFloat8(FunctionCall2Coll(buildstate->procinfo, buildstate->collation, PointerGetDatum(VectorArrayGet(buildstate->centers, i)), PointerGetDatum(VectorArrayGet(buildstate->centers, j))));
				distance = (buildstate->listSums[i] + buildstate->listSums[j]) / distance;

				if (distance > max)
					max = distance;
			}
			db += max;
		}
		db /= buildstate->lists;
		elog(INFO, "davies-bouldin: %.3f", db);
	}
}
#endif

/*
 * Initialize build sort state
 */
static Tuplesortstate *
InitBuildSortState(TupleDesc tupdesc, int memory, SortCoordinate coordinate)
{
	AttrNumber	attNums[] = {1};
	Oid			sortOperators[] = {Int4LessOperator};
	Oid			sortCollations[] = {InvalidOid};
	bool		nullsFirstFlags[] = {false};

	return tuplesort_begin_heap(tupdesc, 1, attNums, sortOperators, sortCollations, nullsFirstFlags, memory, coordinate, false);
}

/*
 * Within leader, wait for end of heap scan
 */
static double
ParallelHeapScan(IvfflatBuildState * buildstate)
{
	IvfflatShared *ivfshared = buildstate->ivfleader->ivfshared;
	int			nparticipanttuplesorts;
	double		reltuples;

	nparticipanttuplesorts = buildstate->ivfleader->nparticipanttuplesorts;
	for (;;)
	{
		SpinLockAcquire(&ivfshared->mutex);
		if (ivfshared->nparticipantsdone == nparticipanttuplesorts)
		{
			buildstate->indtuples = ivfshared->indtuples;
			reltuples = ivfshared->reltuples;
#ifdef IVFFLAT_KMEANS_DEBUG
			buildstate->inertia = ivfshared->inertia;
#endif
			SpinLockRelease(&ivfshared->mutex);
			break;
		}
		SpinLockRelease(&ivfshared->mutex);

		ConditionVariableSleep(&ivfshared->workersdonecv,
							   WAIT_EVENT_PARALLEL_CREATE_INDEX_SCAN);
	}

	ConditionVariableCancelSleep();

	return reltuples;
}

/*
 * Perform a worker's portion of a parallel sort
 */
static void
IvfflatParallelScanAndSort(IvfflatSpool * ivfspool, IvfflatShared * ivfshared, Sharedsort *sharedsort, char *ivfcenters, int sortmem, bool progress)
{
	SortCoordinate coordinate;
	IvfflatBuildState buildstate;
	TableScanDesc scan;
	double		reltuples;
	IndexInfo  *indexInfo;

	/* Initialize local tuplesort coordination state */
	coordinate = palloc0(sizeof(SortCoordinateData));
	coordinate->isWorker = true;
	coordinate->nParticipants = -1;
	coordinate->sharedsort = sharedsort;

	/* Join parallel scan */
	indexInfo = BuildIndexInfo(ivfspool->index);
	indexInfo->ii_Concurrent = ivfshared->isconcurrent;
	InitBuildState(&buildstate, ivfspool->heap, ivfspool->index, indexInfo);
	memcpy(buildstate.centers->items, ivfcenters, buildstate.centers->itemsize * buildstate.centers->maxlen);
	buildstate.centers->length = buildstate.centers->maxlen;
	ivfspool->sortstate = InitBuildSortState(buildstate.sortdesc, sortmem, coordinate);
	buildstate.sortstate = ivfspool->sortstate;
	scan = table_beginscan_parallel(ivfspool->heap,
									ParallelTableScanFromIvfflatShared(ivfshared));
	reltuples = table_index_build_scan(ivfspool->heap, ivfspool->index, indexInfo,
									   true, progress, BuildCallback,
									   (void *) &buildstate, scan);

	/* Execute this worker's part of the sort */
	tuplesort_performsort(ivfspool->sortstate);

	/* Record statistics */
	SpinLockAcquire(&ivfshared->mutex);
	ivfshared->nparticipantsdone++;
	ivfshared->reltuples += reltuples;
	ivfshared->indtuples += buildstate.indtuples;
#ifdef IVFFLAT_KMEANS_DEBUG
	ivfshared->inertia += buildstate.inertia;
#endif
	SpinLockRelease(&ivfshared->mutex);

	/* Log statistics */
	if (progress)
		ereport(DEBUG1, (errmsg("leader processed " INT64_FORMAT " tuples", (int64) reltuples)));
	else
		ereport(DEBUG1, (errmsg("worker processed " INT64_FORMAT " tuples", (int64) reltuples)));

	/* Notify leader */
	ConditionVariableSignal(&ivfshared->workersdonecv);

	/* We can end tuplesorts immediately */
	tuplesort_end(ivfspool->sortstate);

	FreeBuildState(&buildstate);
}

/*
 * Perform work within a launched parallel process
 */
void
IvfflatParallelBuildMain(dsm_segment *seg, shm_toc *toc)
{
	char	   *sharedquery;
	IvfflatSpool *ivfspool;
	IvfflatShared *ivfshared;
	Sharedsort *sharedsort;
	char	   *ivfcenters;
	Relation	heapRel;
	Relation	indexRel;
	LOCKMODE	heapLockmode;
	LOCKMODE	indexLockmode;
	int			sortmem;

	/* Set debug_query_string for individual workers first */
	sharedquery = shm_toc_lookup(toc, PARALLEL_KEY_QUERY_TEXT, true);
	debug_query_string = sharedquery;

	/* Report the query string from leader */
	pgstat_report_activity(STATE_RUNNING, debug_query_string);

	/* Look up shared state */
	ivfshared = shm_toc_lookup(toc, PARALLEL_KEY_IVFFLAT_SHARED, false);

	/* Open relations using lock modes known to be obtained by index.c */
	if (!ivfshared->isconcurrent)
	{
		heapLockmode = ShareLock;
		indexLockmode = AccessExclusiveLock;
	}
	else
	{
		heapLockmode = ShareUpdateExclusiveLock;
		indexLockmode = RowExclusiveLock;
	}

	/* Open relations within worker */
	heapRel = table_open(ivfshared->heaprelid, heapLockmode);
	indexRel = index_open(ivfshared->indexrelid, indexLockmode);

	/* Initialize worker's own spool */
	ivfspool = (IvfflatSpool *) palloc0(sizeof(IvfflatSpool));
	ivfspool->heap = heapRel;
	ivfspool->index = indexRel;

	/* Look up shared state private to tuplesort.c */
	sharedsort = shm_toc_lookup(toc, PARALLEL_KEY_TUPLESORT, false);
	tuplesort_attach_shared(sharedsort, seg);

	ivfcenters = shm_toc_lookup(toc, PARALLEL_KEY_IVFFLAT_CENTERS, false);

	/* Perform sorting */
	sortmem = maintenance_work_mem / ivfshared->scantuplesortstates;
	IvfflatParallelScanAndSort(ivfspool, ivfshared, sharedsort, ivfcenters, sortmem, false);

	/* Close relations within worker */
	index_close(indexRel, indexLockmode);
	table_close(heapRel, heapLockmode);
}

/*
 * End parallel build
 */
static void
IvfflatEndParallel(IvfflatLeader * ivfleader)
{
	/* Shutdown worker processes */
	WaitForParallelWorkersToFinish(ivfleader->pcxt);

	/* Free last reference to MVCC snapshot, if one was used */
	if (IsMVCCSnapshot(ivfleader->snapshot))
		UnregisterSnapshot(ivfleader->snapshot);
	DestroyParallelContext(ivfleader->pcxt);
	ExitParallelMode();
}

/*
 * Return size of shared memory required for parallel index build
 */
static Size
ParallelEstimateShared(Relation heap, Snapshot snapshot)
{
	return add_size(BUFFERALIGN(sizeof(IvfflatShared)), table_parallelscan_estimate(heap, snapshot));
}

/*
 * Within leader, participate as a parallel worker
 */
static void
IvfflatLeaderParticipateAsWorker(IvfflatBuildState * buildstate)
{
	IvfflatLeader *ivfleader = buildstate->ivfleader;
	IvfflatSpool *leaderworker;
	int			sortmem;

	/* Allocate memory and initialize private spool */
	leaderworker = (IvfflatSpool *) palloc0(sizeof(IvfflatSpool));
	leaderworker->heap = buildstate->heap;
	leaderworker->index = buildstate->index;

	/* Perform work common to all participants */
	sortmem = maintenance_work_mem / ivfleader->nparticipanttuplesorts;
	IvfflatParallelScanAndSort(leaderworker, ivfleader->ivfshared,
							   ivfleader->sharedsort, ivfleader->ivfcenters,
							   sortmem, true);
}

/*
 * Begin parallel build
 */
static void
IvfflatBeginParallel(IvfflatBuildState * buildstate, bool isconcurrent, int request)
{
	ParallelContext *pcxt;
	int			scantuplesortstates;
	Snapshot	snapshot;
	Size		estivfshared;
	Size		estsort;
	Size		estcenters;
	IvfflatShared *ivfshared;
	Sharedsort *sharedsort;
	char	   *ivfcenters;
	IvfflatLeader *ivfleader = (IvfflatLeader *) palloc0(sizeof(IvfflatLeader));
	bool		leaderparticipates = true;
	int			querylen;

#ifdef DISABLE_LEADER_PARTICIPATION
	leaderparticipates = false;
#endif

	/* Enter parallel mode and create context */
	EnterParallelMode();
	Assert(request > 0);
	pcxt = CreateParallelContext("vector", "IvfflatParallelBuildMain", request);

	scantuplesortstates = leaderparticipates ? request + 1 : request;

	/* Get snapshot for table scan */
	if (!isconcurrent)
		snapshot = SnapshotAny;
	else
		snapshot = RegisterSnapshot(GetTransactionSnapshot());

	/* Estimate size of workspaces */
	estivfshared = ParallelEstimateShared(buildstate->heap, snapshot);
	shm_toc_estimate_chunk(&pcxt->estimator, estivfshared);
	estsort = tuplesort_estimate_shared(scantuplesortstates);
	shm_toc_estimate_chunk(&pcxt->estimator, estsort);
	estcenters = buildstate->centers->itemsize * buildstate->centers->maxlen;
	shm_toc_estimate_chunk(&pcxt->estimator, estcenters);
	shm_toc_estimate_keys(&pcxt->estimator, 3);

	/* Finally, estimate PARALLEL_KEY_QUERY_TEXT space */
	if (debug_query_string)
	{
		querylen = strlen(debug_query_string);
		shm_toc_estimate_chunk(&pcxt->estimator, querylen + 1);
		shm_toc_estimate_keys(&pcxt->estimator, 1);
	}
	else
		querylen = 0;			/* keep compiler quiet */

	/* Everyone's had a chance to ask for space, so now create the DSM */
	InitializeParallelDSM(pcxt);

	/* If no DSM segment was available, back out (do serial build) */
	if (pcxt->seg == NULL)
	{
		if (IsMVCCSnapshot(snapshot))
			UnregisterSnapshot(snapshot);
		DestroyParallelContext(pcxt);
		ExitParallelMode();
		return;
	}

	/* Store shared build state, for which we reserved space */
	ivfshared = (IvfflatShared *) shm_toc_allocate(pcxt->toc, estivfshared);
	/* Initialize immutable state */
	ivfshared->heaprelid = RelationGetRelid(buildstate->heap);
	ivfshared->indexrelid = RelationGetRelid(buildstate->index);
	ivfshared->isconcurrent = isconcurrent;
	ivfshared->scantuplesortstates = scantuplesortstates;
	ConditionVariableInit(&ivfshared->workersdonecv);
	SpinLockInit(&ivfshared->mutex);
	/* Initialize mutable state */
	ivfshared->nparticipantsdone = 0;
	ivfshared->reltuples = 0;
	ivfshared->indtuples = 0;
#ifdef IVFFLAT_KMEANS_DEBUG
	ivfshared->inertia = 0;
#endif
	table_parallelscan_initialize(buildstate->heap,
								  ParallelTableScanFromIvfflatShared(ivfshared),
								  snapshot);

	/* Store shared tuplesort-private state, for which we reserved space */
	sharedsort = (Sharedsort *) shm_toc_allocate(pcxt->toc, estsort);
	tuplesort_initialize_shared(sharedsort, scantuplesortstates,
								pcxt->seg);

	ivfcenters = shm_toc_allocate(pcxt->toc, estcenters);
	memcpy(ivfcenters, buildstate->centers->items, estcenters);

	shm_toc_insert(pcxt->toc, PARALLEL_KEY_IVFFLAT_SHARED, ivfshared);
	shm_toc_insert(pcxt->toc, PARALLEL_KEY_TUPLESORT, sharedsort);
	shm_toc_insert(pcxt->toc, PARALLEL_KEY_IVFFLAT_CENTERS, ivfcenters);

	/* Store query string for workers */
	if (debug_query_string)
	{
		char	   *sharedquery;

		sharedquery = (char *) shm_toc_allocate(pcxt->toc, querylen + 1);
		memcpy(sharedquery, debug_query_string, querylen + 1);
		shm_toc_insert(pcxt->toc, PARALLEL_KEY_QUERY_TEXT, sharedquery);
	}

	/* Launch workers, saving status for leader/caller */
	LaunchParallelWorkers(pcxt);
	ivfleader->pcxt = pcxt;
	ivfleader->nparticipanttuplesorts = pcxt->nworkers_launched;
	if (leaderparticipates)
		ivfleader->nparticipanttuplesorts++;
	ivfleader->ivfshared = ivfshared;
	ivfleader->sharedsort = sharedsort;
	ivfleader->snapshot = snapshot;
	ivfleader->ivfcenters = ivfcenters;

	/* If no workers were successfully launched, back out (do serial build) */
	if (pcxt->nworkers_launched == 0)
	{
		IvfflatEndParallel(ivfleader);
		return;
	}

	/* Log participants */
	ereport(DEBUG1, (errmsg("using %d parallel workers", pcxt->nworkers_launched)));

	/* Save leader state now that it's clear build will be parallel */
	buildstate->ivfleader = ivfleader;

	/* Join heap scan ourselves */
	if (leaderparticipates)
		IvfflatLeaderParticipateAsWorker(buildstate);

	/* Wait for all launched workers */
	WaitForParallelWorkersToAttach(pcxt);
}

/*
 * Scan table for tuples to index
 */
static void
AssignTuples(IvfflatBuildState * buildstate)
{
	int			parallel_workers = 0;
	SortCoordinate coordinate = NULL;

	pgstat_progress_update_param(PROGRESS_CREATEIDX_SUBPHASE, PROGRESS_IVFFLAT_PHASE_ASSIGN);

	/* Calculate parallel workers */
	if (buildstate->heap != NULL)
		parallel_workers = plan_create_index_workers(RelationGetRelid(buildstate->heap), RelationGetRelid(buildstate->index));

	/* Attempt to launch parallel worker scan when required */
	if (parallel_workers > 0)
		IvfflatBeginParallel(buildstate, buildstate->indexInfo->ii_Concurrent, parallel_workers);

	/* Set up coordination state if at least one worker launched */
	if (buildstate->ivfleader)
	{
		coordinate = (SortCoordinate) palloc0(sizeof(SortCoordinateData));
		coordinate->isWorker = false;
		coordinate->nParticipants = buildstate->ivfleader->nparticipanttuplesorts;
		coordinate->sharedsort = buildstate->ivfleader->sharedsort;
	}

	/* Begin serial/leader tuplesort */
	buildstate->sortstate = InitBuildSortState(buildstate->sortdesc, maintenance_work_mem, coordinate);

	/* Add tuples to sort */
	if (buildstate->heap != NULL)
	{
		if (buildstate->ivfleader)
			buildstate->reltuples = ParallelHeapScan(buildstate);
		else
			buildstate->reltuples = table_index_build_scan(buildstate->heap, buildstate->index, buildstate->indexInfo,
														   true, true, BuildCallback, (void *) buildstate, NULL);

#ifdef IVFFLAT_KMEANS_DEBUG
		PrintKmeansMetrics(buildstate);
#endif
	}
}

/*
 * Create entry pages
 */
static void
CreateEntryPages(IvfflatBuildState * buildstate, ForkNumber forkNum)
{
	/* Assign */
	IvfflatBench("assign tuples", AssignTuples(buildstate));

	/* Sort */
	IvfflatBench("sort tuples", tuplesort_performsort(buildstate->sortstate));

	/* Load */
	IvfflatBench("load tuples", InsertTuples(buildstate->index, buildstate, forkNum));

	/* End sort */
	tuplesort_end(buildstate->sortstate);

	/* End parallel build */
	if (buildstate->ivfleader)
		IvfflatEndParallel(buildstate->ivfleader);
}

/*
 * Build the index
 */
static void
BuildIndex(Relation heap, Relation index, IndexInfo *indexInfo,
		   IvfflatBuildState * buildstate, ForkNumber forkNum)
{
	InitBuildState(buildstate, heap, index, indexInfo);

	ComputeCenters(buildstate);

	/* Create pages */
	CreateMetaPage(index, buildstate->dimensions, buildstate->lists, forkNum);
	CreateListPages(index, buildstate->centers, buildstate->lists, forkNum, &buildstate->listInfo);
	CreateEntryPages(buildstate, forkNum);

	/* Write WAL for initialization fork since GenericXLog functions do not */
	if (forkNum == INIT_FORKNUM)
		log_newpage_range(index, forkNum, 0, RelationGetNumberOfBlocksInFork(index, forkNum), true);

	FreeBuildState(buildstate);
}

/*
 * Build the index for a logged table
 */
IndexBuildResult *
ivfflatbuild(Relation heap, Relation index, IndexInfo *indexInfo)
{
	IndexBuildResult *result;
	IvfflatBuildState buildstate;

#ifdef IVFFLAT_BENCH
	SeedRandom(42);
#endif

	BuildIndex(heap, index, indexInfo, &buildstate, MAIN_FORKNUM);

	result = (IndexBuildResult *) palloc(sizeof(IndexBuildResult));
	result->heap_tuples = buildstate.reltuples;
	result->index_tuples = buildstate.indtuples;

	return result;
}

/*
 * Build the index for an unlogged table
 */
void
ivfflatbuildempty(Relation index)
{
	IndexInfo  *indexInfo = BuildIndexInfo(index);
	IvfflatBuildState buildstate;

	BuildIndex(NULL, index, indexInfo, &buildstate, INIT_FORKNUM);
}
```

## File: `src/ivfflat.c`
```c
#include "postgres.h"

#include <float.h>

#include "access/amapi.h"
#include "access/genam.h"
#include "access/reloptions.h"
#include "commands/progress.h"
#include "commands/vacuum.h"
#include "fmgr.h"
#include "ivfflat.h"
#include "nodes/pg_list.h"
#include "utils/float.h"
#include "utils/guc.h"
#include "utils/relcache.h"
#include "utils/selfuncs.h"
#include "utils/spccache.h"
#include "vector.h"

#if PG_VERSION_NUM < 150000
#define MarkGUCPrefixReserved(x) EmitWarningsOnPlaceholders(x)
#endif

int			ivfflat_probes;
int			ivfflat_iterative_scan;
int			ivfflat_max_probes;
static relopt_kind ivfflat_relopt_kind;

static const struct config_enum_entry ivfflat_iterative_scan_options[] = {
	{"off", IVFFLAT_ITERATIVE_SCAN_OFF, false},
	{"relaxed_order", IVFFLAT_ITERATIVE_SCAN_RELAXED, false},
	{NULL, 0, false}
};

/*
 * Initialize index options and variables
 */
void
IvfflatInit(void)
{
	ivfflat_relopt_kind = add_reloption_kind();
	add_int_reloption(ivfflat_relopt_kind, "lists", "Number of inverted lists",
					  IVFFLAT_DEFAULT_LISTS, IVFFLAT_MIN_LISTS, IVFFLAT_MAX_LISTS, AccessExclusiveLock);

	DefineCustomIntVariable("ivfflat.probes", "Sets the number of probes",
							"Valid range is 1..lists.", &ivfflat_probes,
							IVFFLAT_DEFAULT_PROBES, IVFFLAT_MIN_LISTS, IVFFLAT_MAX_LISTS, PGC_USERSET, 0, NULL, NULL, NULL);

	DefineCustomEnumVariable("ivfflat.iterative_scan", "Sets the mode for iterative scans",
							 NULL, &ivfflat_iterative_scan,
							 IVFFLAT_ITERATIVE_SCAN_OFF, ivfflat_iterative_scan_options, PGC_USERSET, 0, NULL, NULL, NULL);

	/* If this is less than probes, probes is used */
	DefineCustomIntVariable("ivfflat.max_probes", "Sets the max number of probes for iterative scans",
							NULL, &ivfflat_max_probes,
							IVFFLAT_MAX_LISTS, IVFFLAT_MIN_LISTS, IVFFLAT_MAX_LISTS, PGC_USERSET, 0, NULL, NULL, NULL);

	MarkGUCPrefixReserved("ivfflat");
}

/*
 * Get the name of index build phase
 */
static char *
ivfflatbuildphasename(int64 phasenum)
{
	switch (phasenum)
	{
		case PROGRESS_CREATEIDX_SUBPHASE_INITIALIZE:
			return "initializing";
		case PROGRESS_IVFFLAT_PHASE_KMEANS:
			return "performing k-means";
		case PROGRESS_IVFFLAT_PHASE_ASSIGN:
			return "assigning tuples";
		case PROGRESS_IVFFLAT_PHASE_LOAD:
			return "loading tuples";
		default:
			return NULL;
	}
}

/*
 * Estimate the cost of an index scan
 */
static void
ivfflatcostestimate(PlannerInfo *root, IndexPath *path, double loop_count,
					Cost *indexStartupCost, Cost *indexTotalCost,
					Selectivity *indexSelectivity, double *indexCorrelation,
					double *indexPages)
{
	GenericCosts costs;
	int			lists;
	double		ratio;
	double		sequentialRatio = 0.5;
	double		startupPages;
	double		spc_seq_page_cost;
	Relation	index;

	/* Never use index without order */
	if (path->indexorderbys == NIL)
	{
		*indexStartupCost = get_float8_infinity();
		*indexTotalCost = get_float8_infinity();
		*indexSelectivity = 0;
		*indexCorrelation = 0;
		*indexPages = 0;
#if PG_VERSION_NUM >= 180000
		/* See "On disable_cost" thread on pgsql-hackers */
		path->path.disabled_nodes = 2;
#endif
		return;
	}

	MemSet(&costs, 0, sizeof(costs));

	genericcostestimate(root, path, loop_count, &costs);

	index = index_open(path->indexinfo->indexoid, NoLock);
	IvfflatGetMetaPageInfo(index, &lists, NULL);
	index_close(index, NoLock);

	/* Get the ratio of lists that we need to visit */
	ratio = ((double) ivfflat_probes) / lists;
	if (ratio > 1.0)
		ratio = 1.0;

	get_tablespace_page_costs(path->indexinfo->reltablespace, NULL, &spc_seq_page_cost);

	/* Change some page cost from random to sequential */
	costs.indexTotalCost -= sequentialRatio * costs.numIndexPages * (costs.spc_random_page_cost - spc_seq_page_cost);

	/* Startup cost is cost before returning the first row */
	costs.indexStartupCost = costs.indexTotalCost * ratio;

	/* Adjust cost if needed since TOAST not included in seq scan cost */
	startupPages = costs.numIndexPages * ratio;
	if (startupPages > path->indexinfo->rel->pages && ratio < 0.5)
	{
		/* Change rest of page cost from random to sequential */
		costs.indexStartupCost -= (1 - sequentialRatio) * startupPages * (costs.spc_random_page_cost - spc_seq_page_cost);

		/* Remove cost of extra pages */
		costs.indexStartupCost -= (startupPages - path->indexinfo->rel->pages) * spc_seq_page_cost;
	}

	*indexStartupCost = costs.indexStartupCost;
	*indexTotalCost = costs.indexTotalCost;
	*indexSelectivity = costs.indexSelectivity;
	*indexCorrelation = costs.indexCorrelation;
	*indexPages = costs.numIndexPages;
}

/*
 * Parse and validate the reloptions
 */
static bytea *
ivfflatoptions(Datum reloptions, bool validate)
{
	static const relopt_parse_elt tab[] = {
		{"lists", RELOPT_TYPE_INT, offsetof(IvfflatOptions, lists)},
	};

	return (bytea *) build_reloptions(reloptions, validate,
									  ivfflat_relopt_kind,
									  sizeof(IvfflatOptions),
									  tab, lengthof(tab));
}

/*
 * Validate catalog entries for the specified operator class
 */
static bool
ivfflatvalidate(Oid opclassoid)
{
	return true;
}

/*
 * Define index handler
 *
 * See https://www.postgresql.org/docs/current/index-api.html
 */
FUNCTION_PREFIX PG_FUNCTION_INFO_V1(ivfflathandler);
Datum
ivfflathandler(PG_FUNCTION_ARGS)
{
#if PG_VERSION_NUM >= 190000
	static const IndexAmRoutine amroutine = {
		.type = T_IndexAmRoutine,
		.amstrategies = 0,
		.amsupport = 5,
		.amoptsprocnum = 0,
		.amcanorder = false,
		.amcanorderbyop = true,
		.amcanhash = false,
		.amconsistentequality = false,
		.amconsistentordering = false,
		.amcanbackward = false,
		.amcanunique = false,
		.amcanmulticol = false,
		.amoptionalkey = true,
		.amsearcharray = false,
		.amsearchnulls = false,
		.amstorage = false,
		.amclusterable = false,
		.ampredlocks = false,
		.amcanparallel = false,
		.amcanbuildparallel = true,
		.amcaninclude = false,
		.amusemaintenanceworkmem = false,
		.amsummarizing = false,
		.amparallelvacuumoptions = VACUUM_OPTION_PARALLEL_BULKDEL,
		.amkeytype = InvalidOid,

		.ambuild = ivfflatbuild,
		.ambuildempty = ivfflatbuildempty,
		.aminsert = ivfflatinsert,
		.aminsertcleanup = NULL,
		.ambulkdelete = ivfflatbulkdelete,
		.amvacuumcleanup = ivfflatvacuumcleanup,
		.amcanreturn = NULL,
		.amcostestimate = ivfflatcostestimate,
		.amgettreeheight = NULL,
		.amoptions = ivfflatoptions,
		.amproperty = NULL,
		.ambuildphasename = ivfflatbuildphasename,
		.amvalidate = ivfflatvalidate,
		.amadjustmembers = NULL,
		.ambeginscan = ivfflatbeginscan,
		.amrescan = ivfflatrescan,
		.amgettuple = ivfflatgettuple,
		.amgetbitmap = NULL,
		.amendscan = ivfflatendscan,
		.ammarkpos = NULL,
		.amrestrpos = NULL,
		.amestimateparallelscan = NULL,
		.aminitparallelscan = NULL,
		.amparallelrescan = NULL,
		.amtranslatestrategy = NULL,
		.amtranslatecmptype = NULL,
	};

	PG_RETURN_POINTER(&amroutine);
#else
	IndexAmRoutine *amroutine = makeNode(IndexAmRoutine);

	amroutine->amstrategies = 0;
	amroutine->amsupport = 5;
	amroutine->amoptsprocnum = 0;
	amroutine->amcanorder = false;
	amroutine->amcanorderbyop = true;
#if PG_VERSION_NUM >= 180000
	amroutine->amcanhash = false;
	amroutine->amconsistentequality = false;
	amroutine->amconsistentordering = false;
#endif
	amroutine->amcanbackward = false;	/* can change direction mid-scan */
	amroutine->amcanunique = false;
	amroutine->amcanmulticol = false;
	amroutine->amoptionalkey = true;
	amroutine->amsearcharray = false;
	amroutine->amsearchnulls = false;
	amroutine->amstorage = false;
	amroutine->amclusterable = false;
	amroutine->ampredlocks = false;
	amroutine->amcanparallel = false;
#if PG_VERSION_NUM >= 170000
	amroutine->amcanbuildparallel = true;
#endif
	amroutine->amcaninclude = false;
	amroutine->amusemaintenanceworkmem = false; /* not used during VACUUM */
#if PG_VERSION_NUM >= 160000
	amroutine->amsummarizing = false;
#endif
	amroutine->amparallelvacuumoptions = VACUUM_OPTION_PARALLEL_BULKDEL;
	amroutine->amkeytype = InvalidOid;

	/* Interface functions */
	amroutine->ambuild = ivfflatbuild;
	amroutine->ambuildempty = ivfflatbuildempty;
	amroutine->aminsert = ivfflatinsert;
#if PG_VERSION_NUM >= 170000
	amroutine->aminsertcleanup = NULL;
#endif
	amroutine->ambulkdelete = ivfflatbulkdelete;
	amroutine->amvacuumcleanup = ivfflatvacuumcleanup;
	amroutine->amcanreturn = NULL;	/* tuple not included in heapsort */
	amroutine->amcostestimate = ivfflatcostestimate;
#if PG_VERSION_NUM >= 180000
	amroutine->amgettreeheight = NULL;
#endif
	amroutine->amoptions = ivfflatoptions;
	amroutine->amproperty = NULL;	/* TODO AMPROP_DISTANCE_ORDERABLE */
	amroutine->ambuildphasename = ivfflatbuildphasename;
	amroutine->amvalidate = ivfflatvalidate;
#if PG_VERSION_NUM >= 140000
	amroutine->amadjustmembers = NULL;
#endif
	amroutine->ambeginscan = ivfflatbeginscan;
	amroutine->amrescan = ivfflatrescan;
	amroutine->amgettuple = ivfflatgettuple;
	amroutine->amgetbitmap = NULL;
	amroutine->amendscan = ivfflatendscan;
	amroutine->ammarkpos = NULL;
	amroutine->amrestrpos = NULL;

	/* Interface functions to support parallel index scans */
	amroutine->amestimateparallelscan = NULL;
	amroutine->aminitparallelscan = NULL;
	amroutine->amparallelrescan = NULL;

#if PG_VERSION_NUM >= 180000
	amroutine->amtranslatestrategy = NULL;
	amroutine->amtranslatecmptype = NULL;
#endif

	PG_RETURN_POINTER(amroutine);
#endif
}
```

## File: `src/ivfflat.h`
```c
#ifndef IVFFLAT_H
#define IVFFLAT_H

#include "postgres.h"

#include "access/genam.h"
#include "access/generic_xlog.h"
#include "access/parallel.h"
#include "lib/pairingheap.h"
#include "nodes/execnodes.h"
#include "port.h"				/* for random() */
#include "utils/sampling.h"
#include "utils/tuplesort.h"
#include "vector.h"

#if PG_VERSION_NUM >= 160000
#include "varatt.h"
#endif

#if PG_VERSION_NUM >= 150000
#include "common/pg_prng.h"
#endif

#ifdef IVFFLAT_BENCH
#include "portability/instr_time.h"
#endif

#if PG_VERSION_NUM >= 190000
typedef Pointer Item;
#endif

#define IVFFLAT_MAX_DIM 2000

/* Support functions */
#define IVFFLAT_DISTANCE_PROC 1
#define IVFFLAT_NORM_PROC 2
#define IVFFLAT_KMEANS_DISTANCE_PROC 3
#define IVFFLAT_KMEANS_NORM_PROC 4
#define IVFFLAT_TYPE_INFO_PROC 5

#define IVFFLAT_VERSION	1
#define IVFFLAT_MAGIC_NUMBER 0x14FF1A7
#define IVFFLAT_PAGE_ID	0xFF84

/* Preserved page numbers */
#define IVFFLAT_METAPAGE_BLKNO	0
#define IVFFLAT_HEAD_BLKNO		1	/* first list page */

/* IVFFlat parameters */
#define IVFFLAT_DEFAULT_LISTS	100
#define IVFFLAT_MIN_LISTS		1
#define IVFFLAT_MAX_LISTS		32768
#define IVFFLAT_DEFAULT_PROBES	1

/* Build phases */
/* PROGRESS_CREATEIDX_SUBPHASE_INITIALIZE is 1 */
#define PROGRESS_IVFFLAT_PHASE_KMEANS	2
#define PROGRESS_IVFFLAT_PHASE_ASSIGN	3
#define PROGRESS_IVFFLAT_PHASE_LOAD		4

#define IVFFLAT_LIST_SIZE(size)	(offsetof(IvfflatListData, center) + size)

#define IvfflatPageGetOpaque(page)	((IvfflatPageOpaque) PageGetSpecialPointer(page))
#define IvfflatPageGetMeta(page)	((IvfflatMetaPageData *) PageGetContents(page))

#ifdef IVFFLAT_BENCH
#define IvfflatBench(name, code) \
	do { \
		instr_time	start; \
		instr_time	duration; \
		INSTR_TIME_SET_CURRENT(start); \
		(code); \
		INSTR_TIME_SET_CURRENT(duration); \
		INSTR_TIME_SUBTRACT(duration, start); \
		elog(INFO, "%s: %.3f ms", name, INSTR_TIME_GET_MILLISEC(duration)); \
	} while (0)
#else
#define IvfflatBench(name, code) (code)
#endif

#if PG_VERSION_NUM >= 150000
#define RandomDouble() pg_prng_double(&pg_global_prng_state)
#define RandomInt() pg_prng_uint32(&pg_global_prng_state)
#define SeedRandom(seed) pg_prng_seed(&pg_global_prng_state, seed)
#else
#define RandomDouble() (((double) random()) / MAX_RANDOM_VALUE)
#define RandomInt() random()
#define SeedRandom(seed) srandom(seed)
#endif

/* Variables */
extern int	ivfflat_probes;
extern int	ivfflat_iterative_scan;
extern int	ivfflat_max_probes;

typedef enum IvfflatIterativeScanMode
{
	IVFFLAT_ITERATIVE_SCAN_OFF,
	IVFFLAT_ITERATIVE_SCAN_RELAXED
}			IvfflatIterativeScanMode;

typedef struct VectorArrayData
{
	int			length;
	int			maxlen;
	int			dim;
	Size		itemsize;
	char	   *items;
}			VectorArrayData;

typedef VectorArrayData * VectorArray;

typedef struct ListInfo
{
	BlockNumber blkno;
	OffsetNumber offno;
}			ListInfo;

/* IVFFlat index options */
typedef struct IvfflatOptions
{
	int32		vl_len_;		/* varlena header (do not touch directly!) */
	int			lists;			/* number of lists */
}			IvfflatOptions;

typedef struct IvfflatSpool
{
	Tuplesortstate *sortstate;
	Relation	heap;
	Relation	index;
}			IvfflatSpool;

typedef struct IvfflatShared
{
	/* Immutable state */
	Oid			heaprelid;
	Oid			indexrelid;
	bool		isconcurrent;
	int			scantuplesortstates;

	/* Worker progress */
	ConditionVariable workersdonecv;

	/* Mutex for mutable state */
	slock_t		mutex;

	/* Mutable state */
	int			nparticipantsdone;
	double		reltuples;
	double		indtuples;

#ifdef IVFFLAT_KMEANS_DEBUG
	double		inertia;
#endif
}			IvfflatShared;

#define ParallelTableScanFromIvfflatShared(shared) \
	(ParallelTableScanDesc) ((char *) (shared) + BUFFERALIGN(sizeof(IvfflatShared)))

typedef struct IvfflatLeader
{
	ParallelContext *pcxt;
	int			nparticipanttuplesorts;
	IvfflatShared *ivfshared;
	Sharedsort *sharedsort;
	Snapshot	snapshot;
	char	   *ivfcenters;
}			IvfflatLeader;

typedef struct IvfflatTypeInfo
{
	int			maxDimensions;
	Datum		(*normalize) (PG_FUNCTION_ARGS);
	Size		(*itemSize) (int dimensions);
	void		(*updateCenter) (Pointer v, int dimensions, float *x);
	void		(*sumCenter) (Pointer v, float *x);
}			IvfflatTypeInfo;

typedef struct IvfflatBuildState
{
	/* Info */
	Relation	heap;
	Relation	index;
	IndexInfo  *indexInfo;
	const		IvfflatTypeInfo *typeInfo;
	TupleDesc	tupdesc;

	/* Settings */
	int			dimensions;
	int			lists;

	/* Statistics */
	double		indtuples;
	double		reltuples;

	/* Support functions */
	FmgrInfo   *procinfo;
	FmgrInfo   *normprocinfo;
	FmgrInfo   *kmeansnormprocinfo;
	Oid			collation;

	/* Variables */
	VectorArray samples;
	VectorArray centers;
	ListInfo   *listInfo;

#ifdef IVFFLAT_KMEANS_DEBUG
	double		inertia;
	double	   *listSums;
	int		   *listCounts;
#endif

	/* Sampling */
	BlockSamplerData bs;
	ReservoirStateData rstate;
	int			rowstoskip;

	/* Sorting */
	Tuplesortstate *sortstate;
	TupleDesc	sortdesc;
	TupleTableSlot *slot;

	/* Memory */
	MemoryContext tmpCtx;

	/* Parallel builds */
	IvfflatLeader *ivfleader;
}			IvfflatBuildState;

typedef struct IvfflatMetaPageData
{
	uint32		magicNumber;
	uint32		version;
	uint16		dimensions;
	uint16		lists;
}			IvfflatMetaPageData;

typedef IvfflatMetaPageData * IvfflatMetaPage;

typedef struct IvfflatPageOpaqueData
{
	BlockNumber nextblkno;
	uint16		unused;
	uint16		page_id;		/* for identification of IVFFlat indexes */
}			IvfflatPageOpaqueData;

typedef IvfflatPageOpaqueData * IvfflatPageOpaque;

typedef struct IvfflatListData
{
	BlockNumber startPage;
	BlockNumber insertPage;
	Vector		center;
}			IvfflatListData;

typedef IvfflatListData * IvfflatList;

typedef struct IvfflatScanList
{
	pairingheap_node ph_node;
	BlockNumber startPage;
	double		distance;
}			IvfflatScanList;

typedef struct IvfflatScanOpaqueData
{
	const		IvfflatTypeInfo *typeInfo;
	int			probes;
	int			maxProbes;
	int			dimensions;
	bool		first;
	Datum		value;
	MemoryContext tmpCtx;

	/* Sorting */
	Tuplesortstate *sortstate;
	TupleDesc	tupdesc;
	TupleTableSlot *vslot;
	TupleTableSlot *mslot;
	BufferAccessStrategy bas;

	/* Support functions */
	FmgrInfo   *procinfo;
	FmgrInfo   *normprocinfo;
	Oid			collation;
	Datum		(*distfunc) (FmgrInfo *flinfo, Oid collation, Datum arg1, Datum arg2);

	/* Lists */
	pairingheap *listQueue;
	BlockNumber *listPages;
	int			listIndex;
	IvfflatScanList *lists;
}			IvfflatScanOpaqueData;

typedef IvfflatScanOpaqueData * IvfflatScanOpaque;

#define VECTOR_ARRAY_SIZE(_length, _size) (sizeof(VectorArrayData) + (_length) * MAXALIGN(_size))

/* Use functions instead of macros to avoid double evaluation */

static inline Pointer
VectorArrayGet(VectorArray arr, int offset)
{
	return ((char *) arr->items) + (offset * arr->itemsize);
}

static inline void
VectorArraySet(VectorArray arr, int offset, Pointer val)
{
	memcpy(VectorArrayGet(arr, offset), val, VARSIZE_ANY(val));
}

/* Methods */
VectorArray VectorArrayInit(int maxlen, int dimensions, Size itemsize);
void		VectorArrayFree(VectorArray arr);
void		IvfflatKmeans(Relation index, VectorArray samples, VectorArray centers, const IvfflatTypeInfo * typeInfo);
FmgrInfo   *IvfflatOptionalProcInfo(Relation index, uint16 procnum);
Datum		IvfflatNormValue(const IvfflatTypeInfo * typeInfo, Oid collation, Datum value);
bool		IvfflatCheckNorm(FmgrInfo *procinfo, Oid collation, Datum value);
int			IvfflatGetLists(Relation index);
void		IvfflatGetMetaPageInfo(Relation index, int *lists, int *dimensions);
void		IvfflatUpdateList(Relation index, ListInfo listInfo, BlockNumber insertPage, BlockNumber originalInsertPage, BlockNumber startPage, ForkNumber forkNum);
void		IvfflatCommitBuffer(Buffer buf, GenericXLogState *state);
void		IvfflatAppendPage(Relation index, Buffer *buf, Page *page, GenericXLogState **state, ForkNumber forkNum);
Buffer		IvfflatNewBuffer(Relation index, ForkNumber forkNum);
void		IvfflatInitPage(Buffer buf, Page page);
void		IvfflatInitRegisterPage(Relation index, Buffer *buf, Page *page, GenericXLogState **state);
void		IvfflatInit(void);
const		IvfflatTypeInfo *IvfflatGetTypeInfo(Relation index);
PGDLLEXPORT void IvfflatParallelBuildMain(dsm_segment *seg, shm_toc *toc);

/* Index access methods */
IndexBuildResult *ivfflatbuild(Relation heap, Relation index, IndexInfo *indexInfo);
void		ivfflatbuildempty(Relation index);
bool		ivfflatinsert(Relation index, Datum *values, bool *isnull, ItemPointer heap_tid, Relation heap, IndexUniqueCheck checkUnique
#if PG_VERSION_NUM >= 140000
						  ,bool indexUnchanged
#endif
						  ,IndexInfo *indexInfo
);
IndexBulkDeleteResult *ivfflatbulkdelete(IndexVacuumInfo *info, IndexBulkDeleteResult *stats, IndexBulkDeleteCallback callback, void *callback_state);
IndexBulkDeleteResult *ivfflatvacuumcleanup(IndexVacuumInfo *info, IndexBulkDeleteResult *stats);
IndexScanDesc ivfflatbeginscan(Relation index, int nkeys, int norderbys);
void		ivfflatrescan(IndexScanDesc scan, ScanKey keys, int nkeys, ScanKey orderbys, int norderbys);
bool		ivfflatgettuple(IndexScanDesc scan, ScanDirection dir);
void		ivfflatendscan(IndexScanDesc scan);

#endif
```

## File: `src/ivfinsert.c`
```c
#include "postgres.h"

#include <float.h>

#include "access/genam.h"
#include "access/generic_xlog.h"
#include "access/itup.h"
#include "fmgr.h"
#include "ivfflat.h"
#include "nodes/execnodes.h"
#include "storage/bufmgr.h"
#include "storage/lmgr.h"
#include "utils/memutils.h"
#include "utils/rel.h"

/*
 * Find the list that minimizes the distance function
 */
static void
FindInsertPage(Relation index, Datum *values, BlockNumber *insertPage, ListInfo * listInfo)
{
	double		minDistance = DBL_MAX;
	BlockNumber nextblkno = IVFFLAT_HEAD_BLKNO;
	FmgrInfo   *procinfo;
	Oid			collation;

	/* Avoid compiler warning */
	listInfo->blkno = nextblkno;
	listInfo->offno = FirstOffsetNumber;

	procinfo = index_getprocinfo(index, 1, IVFFLAT_DISTANCE_PROC);
	collation = index->rd_indcollation[0];

	/* Search all list pages */
	while (BlockNumberIsValid(nextblkno))
	{
		Buffer		cbuf;
		Page		cpage;
		OffsetNumber maxoffno;

		cbuf = ReadBuffer(index, nextblkno);
		LockBuffer(cbuf, BUFFER_LOCK_SHARE);
		cpage = BufferGetPage(cbuf);
		maxoffno = PageGetMaxOffsetNumber(cpage);

		for (OffsetNumber offno = FirstOffsetNumber; offno <= maxoffno; offno = OffsetNumberNext(offno))
		{
			IvfflatList list;
			double		distance;

			list = (IvfflatList) PageGetItem(cpage, PageGetItemId(cpage, offno));
			distance = DatumGetFloat8(FunctionCall2Coll(procinfo, collation, values[0], PointerGetDatum(&list->center)));

			if (distance < minDistance || !BlockNumberIsValid(*insertPage))
			{
				*insertPage = list->insertPage;
				listInfo->blkno = nextblkno;
				listInfo->offno = offno;
				minDistance = distance;
			}
		}

		nextblkno = IvfflatPageGetOpaque(cpage)->nextblkno;

		UnlockReleaseBuffer(cbuf);
	}
}

/*
 * Insert a tuple into the index
 */
static void
InsertTuple(Relation index, Datum *values, bool *isnull, ItemPointer heap_tid)
{
	const		IvfflatTypeInfo *typeInfo = IvfflatGetTypeInfo(index);
	IndexTuple	itup;
	Datum		value;
	FmgrInfo   *normprocinfo;
	Buffer		buf;
	Page		page;
	GenericXLogState *state;
	Size		itemsz;
	BlockNumber insertPage = InvalidBlockNumber;
	ListInfo	listInfo;
	BlockNumber originalInsertPage;

	/* Detoast once for all calls */
	value = PointerGetDatum(PG_DETOAST_DATUM(values[0]));

	/* Normalize if needed */
	normprocinfo = IvfflatOptionalProcInfo(index, IVFFLAT_NORM_PROC);
	if (normprocinfo != NULL)
	{
		Oid			collation = index->rd_indcollation[0];

		if (!IvfflatCheckNorm(normprocinfo, collation, value))
			return;

		value = IvfflatNormValue(typeInfo, collation, value);
	}

	/* Ensure index is valid */
	IvfflatGetMetaPageInfo(index, NULL, NULL);

	/* Find the insert page - sets the page and list info */
	FindInsertPage(index, &value, &insertPage, &listInfo);
	Assert(BlockNumberIsValid(insertPage));
	originalInsertPage = insertPage;

	/* Form tuple */
	itup = index_form_tuple(RelationGetDescr(index), &value, isnull);
	itup->t_tid = *heap_tid;

	/* Get tuple size */
	itemsz = MAXALIGN(IndexTupleSize(itup));
	Assert(itemsz <= BLCKSZ - MAXALIGN(SizeOfPageHeaderData) - MAXALIGN(sizeof(IvfflatPageOpaqueData)) - sizeof(ItemIdData));

	/* Find a page to insert the item */
	for (;;)
	{
		buf = ReadBuffer(index, insertPage);
		LockBuffer(buf, BUFFER_LOCK_EXCLUSIVE);

		state = GenericXLogStart(index);
		page = GenericXLogRegisterBuffer(state, buf, 0);

		if (PageGetFreeSpace(page) >= itemsz)
			break;

		insertPage = IvfflatPageGetOpaque(page)->nextblkno;

		if (BlockNumberIsValid(insertPage))
		{
			/* Move to next page */
			GenericXLogAbort(state);
			UnlockReleaseBuffer(buf);
		}
		else
		{
			Buffer		newbuf;
			Page		newpage;

			/* Add a new page */
			LockRelationForExtension(index, ExclusiveLock);
			newbuf = IvfflatNewBuffer(index, MAIN_FORKNUM);
			UnlockRelationForExtension(index, ExclusiveLock);

			/* Init new page */
			newpage = GenericXLogRegisterBuffer(state, newbuf, GENERIC_XLOG_FULL_IMAGE);
			IvfflatInitPage(newbuf, newpage);

			/* Update insert page */
			insertPage = BufferGetBlockNumber(newbuf);

			/* Update previous buffer */
			IvfflatPageGetOpaque(page)->nextblkno = insertPage;

			/* Commit */
			GenericXLogFinish(state);

			/* Unlock previous buffer */
			UnlockReleaseBuffer(buf);

			/* Prepare new buffer */
			state = GenericXLogStart(index);
			buf = newbuf;
			page = GenericXLogRegisterBuffer(state, buf, 0);
			break;
		}
	}

	/* Add to next offset */
	if (PageAddItem(page, (Item) itup, itemsz, InvalidOffsetNumber, false, false) == InvalidOffsetNumber)
		elog(ERROR, "failed to add index item to \"%s\"", RelationGetRelationName(index));

	IvfflatCommitBuffer(buf, state);

	/* Update the insert page */
	if (insertPage != originalInsertPage)
		IvfflatUpdateList(index, listInfo, insertPage, originalInsertPage, InvalidBlockNumber, MAIN_FORKNUM);
}

/*
 * Insert a tuple into the index
 */
bool
ivfflatinsert(Relation index, Datum *values, bool *isnull, ItemPointer heap_tid,
			  Relation heap, IndexUniqueCheck checkUnique
#if PG_VERSION_NUM >= 140000
			  ,bool indexUnchanged
#endif
			  ,IndexInfo *indexInfo
)
{
	MemoryContext oldCtx;
	MemoryContext insertCtx;

	/* Skip nulls */
	if (isnull[0])
		return false;

	/*
	 * Use memory context since detoast, IvfflatNormValue, and
	 * index_form_tuple can allocate
	 */
	insertCtx = AllocSetContextCreate(CurrentMemoryContext,
									  "Ivfflat insert temporary context",
									  ALLOCSET_DEFAULT_SIZES);
	oldCtx = MemoryContextSwitchTo(insertCtx);

	/* Insert tuple */
	InsertTuple(index, values, isnull, heap_tid);

	/* Delete memory context */
	MemoryContextSwitchTo(oldCtx);
	MemoryContextDelete(insertCtx);

	return false;
}
```

## File: `src/ivfkmeans.c`
```c
#include "postgres.h"

#include <float.h>
#include <limits.h>
#include <math.h>

#include "access/genam.h"
#include "fmgr.h"
#include "ivfflat.h"
#include "miscadmin.h"
#include "utils/memutils.h"
#include "utils/relcache.h"

#if PG_VERSION_NUM >= 160000
#include "varatt.h"
#endif

/*
 * Initialize with kmeans++
 *
 * https://theory.stanford.edu/~sergei/papers/kMeansPP-soda.pdf
 */
static void
InitCenters(Relation index, VectorArray samples, VectorArray centers, float *lowerBound)
{
	FmgrInfo   *procinfo;
	Oid			collation;
	int64		j;
	float	   *weight = palloc(samples->length * sizeof(float));
	int			numCenters = centers->maxlen;
	int			numSamples = samples->length;

	procinfo = index_getprocinfo(index, 1, IVFFLAT_KMEANS_DISTANCE_PROC);
	collation = index->rd_indcollation[0];

	/* Choose an initial center uniformly at random */
	VectorArraySet(centers, 0, VectorArrayGet(samples, RandomInt() % samples->length));
	centers->length++;

	for (j = 0; j < numSamples; j++)
		weight[j] = FLT_MAX;

	for (int i = 0; i < numCenters; i++)
	{
		double		sum;
		double		choice;

		CHECK_FOR_INTERRUPTS();

		sum = 0.0;

		for (j = 0; j < numSamples; j++)
		{
			Datum		vec = PointerGetDatum(VectorArrayGet(samples, j));
			double		distance;

			/* Only need to compute distance for new center */
			/* TODO Use triangle inequality to reduce distance calculations */
			distance = DatumGetFloat8(FunctionCall2Coll(procinfo, collation, vec, PointerGetDatum(VectorArrayGet(centers, i))));

			/* Set lower bound */
			lowerBound[j * numCenters + i] = distance;

			/* Use distance squared for weighted probability distribution */
			distance *= distance;

			if (distance < weight[j])
				weight[j] = distance;

			sum += weight[j];
		}

		/* Only compute lower bound on last iteration */
		if (i + 1 == numCenters)
			break;

		/* Choose new center using weighted probability distribution. */
		choice = sum * RandomDouble();
		for (j = 0; j < numSamples - 1; j++)
		{
			choice -= weight[j];
			if (choice <= 0)
				break;
		}

		VectorArraySet(centers, i + 1, VectorArrayGet(samples, j));
		centers->length++;
	}

	pfree(weight);
}

/*
 * Norm centers
 */
static void
NormCenters(const IvfflatTypeInfo * typeInfo, Oid collation, VectorArray centers)
{
	MemoryContext normCtx = AllocSetContextCreate(CurrentMemoryContext,
												  "Ivfflat norm temporary context",
												  ALLOCSET_DEFAULT_SIZES);
	MemoryContext oldCtx = MemoryContextSwitchTo(normCtx);

	for (int j = 0; j < centers->length; j++)
	{
		Datum		center = PointerGetDatum(VectorArrayGet(centers, j));
		Datum		newCenter = IvfflatNormValue(typeInfo, collation, center);
		Size		size = VARSIZE_ANY(DatumGetPointer(newCenter));

		if (size > centers->itemsize)
			elog(ERROR, "safety check failed");

		memcpy(DatumGetPointer(center), DatumGetPointer(newCenter), size);
		MemoryContextReset(normCtx);
	}

	MemoryContextSwitchTo(oldCtx);
	MemoryContextDelete(normCtx);
}

/*
 * Quick approach if we have no data
 */
static void
RandomCenters(Relation index, VectorArray centers, const IvfflatTypeInfo * typeInfo)
{
	int			dimensions = centers->dim;
	FmgrInfo   *normprocinfo = IvfflatOptionalProcInfo(index, IVFFLAT_KMEANS_NORM_PROC);
	Oid			collation = index->rd_indcollation[0];
	float	   *x = (float *) palloc(sizeof(float) * dimensions);

	/* Fill with random data */
	while (centers->length < centers->maxlen)
	{
		Pointer		center = VectorArrayGet(centers, centers->length);

		for (int i = 0; i < dimensions; i++)
			x[i] = (float) RandomDouble();

		typeInfo->updateCenter(center, dimensions, x);

		centers->length++;
	}

	if (normprocinfo != NULL)
		NormCenters(typeInfo, collation, centers);
}

#ifdef IVFFLAT_MEMORY
/*
 * Show memory usage
 */
static void
ShowMemoryUsage(MemoryContext context, Size estimatedSize)
{
	elog(INFO, "total memory: %zu MB",
		 MemoryContextMemAllocated(context, true) / (1024 * 1024));
	elog(INFO, "estimated memory: %zu MB", estimatedSize / (1024 * 1024));
}
#endif

/*
 * Sum centers
 */
static void
SumCenters(VectorArray samples, float *agg, int *closestCenters, const IvfflatTypeInfo * typeInfo)
{
	for (int j = 0; j < samples->length; j++)
	{
		float	   *x = agg + ((int64) closestCenters[j] * samples->dim);

		typeInfo->sumCenter(VectorArrayGet(samples, j), x);
	}
}

/*
 * Update centers
 */
static void
UpdateCenters(float *agg, VectorArray centers, const IvfflatTypeInfo * typeInfo)
{
	for (int j = 0; j < centers->length; j++)
	{
		float	   *x = agg + ((int64) j * centers->dim);

		typeInfo->updateCenter(VectorArrayGet(centers, j), centers->dim, x);
	}
}

/*
 * Compute new centers
 */
static void
ComputeNewCenters(VectorArray samples, float *agg, VectorArray newCenters, int *centerCounts, int *closestCenters, FmgrInfo *normprocinfo, Oid collation, const IvfflatTypeInfo * typeInfo)
{
	int			dimensions = newCenters->dim;
	int			numCenters = newCenters->length;
	int			numSamples = samples->length;

	/* Reset sum and count */
	for (int j = 0; j < numCenters; j++)
	{
		float	   *x = agg + ((int64) j * dimensions);

		for (int k = 0; k < dimensions; k++)
			x[k] = 0.0;

		centerCounts[j] = 0;
	}

	/* Increment sum of closest center */
	SumCenters(samples, agg, closestCenters, typeInfo);

	/* Increment count of closest center */
	for (int j = 0; j < numSamples; j++)
		centerCounts[closestCenters[j]] += 1;

	/* Divide sum by count */
	for (int j = 0; j < numCenters; j++)
	{
		float	   *x = agg + ((int64) j * dimensions);

		if (centerCounts[j] > 0)
		{
			/* Double avoids overflow, but requires more memory */
			/* TODO Update bounds */
			for (int k = 0; k < dimensions; k++)
			{
				if (isinf(x[k]))
					x[k] = x[k] > 0 ? FLT_MAX : -FLT_MAX;
			}

			for (int k = 0; k < dimensions; k++)
				x[k] /= centerCounts[j];
		}
		else
		{
			/* TODO Handle empty centers properly */
			for (int k = 0; k < dimensions; k++)
				x[k] = RandomDouble();
		}
	}

	/* Set new centers */
	UpdateCenters(agg, newCenters, typeInfo);

	/* Normalize if needed */
	if (normprocinfo != NULL)
		NormCenters(typeInfo, collation, newCenters);
}

/*
 * Use Elkan for performance. This requires distance function to satisfy triangle inequality.
 *
 * We use L2 distance for L2 (not L2 squared like index scan)
 * and angular distance for inner product and cosine distance
 *
 * https://www.aaai.org/Papers/ICML/2003/ICML03-022.pdf
 */
static void
ElkanKmeans(Relation index, VectorArray samples, VectorArray centers, const IvfflatTypeInfo * typeInfo)
{
	FmgrInfo   *procinfo;
	FmgrInfo   *normprocinfo;
	Oid			collation;
	int			dimensions = centers->dim;
	int			numCenters = centers->maxlen;
	int			numSamples = samples->length;
	VectorArray newCenters;
	float	   *agg;
	int		   *centerCounts;
	int		   *closestCenters;
	float	   *lowerBound;
	float	   *upperBound;
	float	   *s;
	float	   *halfcdist;
	float	   *newcdist;

	/* Calculate allocation sizes */
	Size		samplesSize = VECTOR_ARRAY_SIZE(samples->maxlen, samples->itemsize);
	Size		centersSize = VECTOR_ARRAY_SIZE(centers->maxlen, centers->itemsize);
	Size		newCentersSize = VECTOR_ARRAY_SIZE(numCenters, centers->itemsize);
	Size		aggSize = sizeof(float) * (int64) numCenters * dimensions;
	Size		centerCountsSize = sizeof(int) * numCenters;
	Size		closestCentersSize = sizeof(int) * numSamples;
	Size		lowerBoundSize = sizeof(float) * numSamples * numCenters;
	Size		upperBoundSize = sizeof(float) * numSamples;
	Size		sSize = sizeof(float) * numCenters;
	Size		halfcdistSize = sizeof(float) * numCenters * numCenters;
	Size		newcdistSize = sizeof(float) * numCenters;

	/* Calculate total size */
	Size		totalSize = samplesSize + centersSize + newCentersSize + aggSize + centerCountsSize + closestCentersSize + lowerBoundSize + upperBoundSize + sSize + halfcdistSize + newcdistSize;

	/* Check memory requirements */
	/* Add one to error message to ceil */
	if (totalSize > (Size) maintenance_work_mem * 1024L)
		ereport(ERROR,
				(errcode(ERRCODE_PROGRAM_LIMIT_EXCEEDED),
				 errmsg("memory required is %zu MB, maintenance_work_mem is %d MB",
						totalSize / (1024 * 1024) + 1, maintenance_work_mem / 1024)));

	/* Ensure indexing does not overflow */
	if (numCenters * numCenters > INT_MAX)
		elog(ERROR, "Indexing overflow detected. Please report a bug.");

	/* Set support functions */
	procinfo = index_getprocinfo(index, 1, IVFFLAT_KMEANS_DISTANCE_PROC);
	normprocinfo = IvfflatOptionalProcInfo(index, IVFFLAT_KMEANS_NORM_PROC);
	collation = index->rd_indcollation[0];

	/* Allocate space */
	/* Use float instead of double to save memory */
	agg = palloc(aggSize);
	centerCounts = palloc(centerCountsSize);
	closestCenters = palloc(closestCentersSize);
	lowerBound = palloc_extended(lowerBoundSize, MCXT_ALLOC_HUGE);
	upperBound = palloc(upperBoundSize);
	s = palloc(sSize);
	halfcdist = palloc_extended(halfcdistSize, MCXT_ALLOC_HUGE);
	newcdist = palloc(newcdistSize);

	/* Initialize new centers */
	newCenters = VectorArrayInit(numCenters, dimensions, centers->itemsize);
	newCenters->length = numCenters;

#ifdef IVFFLAT_MEMORY
	ShowMemoryUsage(MemoryContextGetParent(CurrentMemoryContext), totalSize);
#endif

	/* Pick initial centers */
	InitCenters(index, samples, centers, lowerBound);

	/* Assign each x to its closest initial center c(x) = argmin d(x,c) */
	for (int64 j = 0; j < numSamples; j++)
	{
		float		minDistance = FLT_MAX;
		int			closestCenter = 0;

		/* Find closest center */
		for (int64 k = 0; k < numCenters; k++)
		{
			/* TODO Use Lemma 1 in k-means++ initialization */
			float		distance = lowerBound[j * numCenters + k];

			if (distance < minDistance)
			{
				minDistance = distance;
				closestCenter = k;
			}
		}

		upperBound[j] = minDistance;
		closestCenters[j] = closestCenter;
	}

	/* Give 500 iterations to converge */
	for (int iteration = 0; iteration < 500; iteration++)
	{
		int			changes = 0;
		bool		rjreset;

		/* Can take a while, so ensure we can interrupt */
		CHECK_FOR_INTERRUPTS();

		/* Step 1: For all centers, compute distance */
		for (int64 j = 0; j < numCenters; j++)
		{
			Datum		vec = PointerGetDatum(VectorArrayGet(centers, j));

			for (int64 k = j + 1; k < numCenters; k++)
			{
				float		distance = 0.5 * DatumGetFloat8(FunctionCall2Coll(procinfo, collation, vec, PointerGetDatum(VectorArrayGet(centers, k))));

				halfcdist[j * numCenters + k] = distance;
				halfcdist[k * numCenters + j] = distance;
			}
		}

		/* For all centers c, compute s(c) */
		for (int64 j = 0; j < numCenters; j++)
		{
			float		minDistance = FLT_MAX;

			for (int64 k = 0; k < numCenters; k++)
			{
				float		distance;

				if (j == k)
					continue;

				distance = halfcdist[j * numCenters + k];
				if (distance < minDistance)
					minDistance = distance;
			}

			s[j] = minDistance;
		}

		rjreset = iteration != 0;

		for (int64 j = 0; j < numSamples; j++)
		{
			bool		rj;

			/* Step 2: Identify all points x such that u(x) <= s(c(x)) */
			if (upperBound[j] <= s[closestCenters[j]])
				continue;

			rj = rjreset;

			for (int64 k = 0; k < numCenters; k++)
			{
				Datum		vec;
				float		dxcx;

				/* Step 3: For all remaining points x and centers c */
				if (k == closestCenters[j])
					continue;

				if (upperBound[j] <= lowerBound[j * numCenters + k])
					continue;

				if (upperBound[j] <= halfcdist[closestCenters[j] * numCenters + k])
					continue;

				vec = PointerGetDatum(VectorArrayGet(samples, j));

				/* Step 3a */
				if (rj)
				{
					dxcx = DatumGetFloat8(FunctionCall2Coll(procinfo, collation, vec, PointerGetDatum(VectorArrayGet(centers, closestCenters[j]))));

					/* d(x,c(x)) computed, which is a form of d(x,c) */
					lowerBound[j * numCenters + closestCenters[j]] = dxcx;
					upperBound[j] = dxcx;

					rj = false;
				}
				else
					dxcx = upperBound[j];

				/* Step 3b */
				if (dxcx > lowerBound[j * numCenters + k] || dxcx > halfcdist[closestCenters[j] * numCenters + k])
				{
					float		dxc = DatumGetFloat8(FunctionCall2Coll(procinfo, collation, vec, PointerGetDatum(VectorArrayGet(centers, k))));

					/* d(x,c) calculated */
					lowerBound[j * numCenters + k] = dxc;

					if (dxc < dxcx)
					{
						closestCenters[j] = k;

						/* c(x) changed */
						upperBound[j] = dxc;

						changes++;
					}
				}
			}
		}

		/* Step 4: For each center c, let m(c) be mean of all points assigned */
		ComputeNewCenters(samples, agg, newCenters, centerCounts, closestCenters, normprocinfo, collation, typeInfo);

		/* Step 5 */
		for (int j = 0; j < numCenters; j++)
			newcdist[j] = DatumGetFloat8(FunctionCall2Coll(procinfo, collation, PointerGetDatum(VectorArrayGet(centers, j)), PointerGetDatum(VectorArrayGet(newCenters, j))));

		for (int64 j = 0; j < numSamples; j++)
		{
			for (int64 k = 0; k < numCenters; k++)
			{
				float		distance = lowerBound[j * numCenters + k] - newcdist[k];

				if (distance < 0)
					distance = 0;

				lowerBound[j * numCenters + k] = distance;
			}
		}

		/* Step 6 */
		/* We reset r(x) before Step 3 in the next iteration */
		for (int j = 0; j < numSamples; j++)
			upperBound[j] += newcdist[closestCenters[j]];

		/* Step 7 */
		for (int j = 0; j < numCenters; j++)
			VectorArraySet(centers, j, VectorArrayGet(newCenters, j));

		if (changes == 0 && iteration != 0)
			break;
	}
}

/*
 * Ensure no NaN or infinite values
 */
static void
CheckElements(VectorArray centers, const IvfflatTypeInfo * typeInfo)
{
	float	   *scratch = palloc(sizeof(float) * centers->dim);

	for (int i = 0; i < centers->length; i++)
	{
		for (int j = 0; j < centers->dim; j++)
			scratch[j] = 0;

		/* /fp:fast may not propagate NaN with MSVC, but that's alright */
		typeInfo->sumCenter(VectorArrayGet(centers, i), scratch);

		for (int j = 0; j < centers->dim; j++)
		{
			if (isnan(scratch[j]))
				elog(ERROR, "NaN detected. Please report a bug.");

			if (isinf(scratch[j]))
				elog(ERROR, "Infinite value detected. Please report a bug.");
		}
	}
}

/*
 * Ensure no zero vectors for cosine distance
 */
static void
CheckNorms(VectorArray centers, Relation index)
{
	/* Check NORM_PROC instead of KMEANS_NORM_PROC */
	FmgrInfo   *normprocinfo = IvfflatOptionalProcInfo(index, IVFFLAT_NORM_PROC);
	Oid			collation = index->rd_indcollation[0];

	if (normprocinfo == NULL)
		return;

	for (int i = 0; i < centers->length; i++)
	{
		double		norm = DatumGetFloat8(FunctionCall1Coll(normprocinfo, collation, PointerGetDatum(VectorArrayGet(centers, i))));

		if (norm == 0)
			elog(ERROR, "Zero norm detected. Please report a bug.");
	}
}

/*
 * Detect issues with centers
 */
static void
CheckCenters(Relation index, VectorArray centers, const IvfflatTypeInfo * typeInfo)
{
	if (centers->length != centers->maxlen)
		elog(ERROR, "Not enough centers. Please report a bug.");

	CheckElements(centers, typeInfo);
	CheckNorms(centers, index);
}

/*
 * Perform naive k-means centering
 * We use spherical k-means for inner product and cosine
 */
void
IvfflatKmeans(Relation index, VectorArray samples, VectorArray centers, const IvfflatTypeInfo * typeInfo)
{
	MemoryContext kmeansCtx = AllocSetContextCreate(CurrentMemoryContext,
													"Ivfflat kmeans temporary context",
													ALLOCSET_DEFAULT_SIZES);
	MemoryContext oldCtx = MemoryContextSwitchTo(kmeansCtx);

	if (samples->length == 0)
		RandomCenters(index, centers, typeInfo);
	else
		ElkanKmeans(index, samples, centers, typeInfo);

	CheckCenters(index, centers, typeInfo);

	MemoryContextSwitchTo(oldCtx);
	MemoryContextDelete(kmeansCtx);
}
```

## File: `src/ivfscan.c`
```c
#include "postgres.h"

#include <float.h>

#include "access/genam.h"
#include "access/itup.h"
#include "access/relscan.h"
#include "access/tupdesc.h"
#include "catalog/pg_operator_d.h"
#include "catalog/pg_type_d.h"
#include "fmgr.h"
#include "lib/pairingheap.h"
#include "ivfflat.h"
#include "miscadmin.h"
#include "pgstat.h"
#include "storage/bufmgr.h"
#include "utils/memutils.h"
#include "utils/rel.h"
#include "utils/snapmgr.h"
#include "utils/tuplesort.h"

#if PG_VERSION_NUM >= 160000
#include "varatt.h"
#endif

#define GetScanList(ptr) pairingheap_container(IvfflatScanList, ph_node, ptr)
#define GetScanListConst(ptr) pairingheap_const_container(IvfflatScanList, ph_node, ptr)

/*
 * Compare list distances
 */
static int
CompareLists(const pairingheap_node *a, const pairingheap_node *b, void *arg)
{
	if (GetScanListConst(a)->distance > GetScanListConst(b)->distance)
		return 1;

	if (GetScanListConst(a)->distance < GetScanListConst(b)->distance)
		return -1;

	return 0;
}

/*
 * Get lists and sort by distance
 */
static void
GetScanLists(IndexScanDesc scan, Datum value)
{
	IvfflatScanOpaque so = (IvfflatScanOpaque) scan->opaque;
	BlockNumber nextblkno = IVFFLAT_HEAD_BLKNO;
	int			listCount = 0;
	double		maxDistance = DBL_MAX;

	/* Search all list pages */
	while (BlockNumberIsValid(nextblkno))
	{
		Buffer		cbuf;
		Page		cpage;
		OffsetNumber maxoffno;

		cbuf = ReadBuffer(scan->indexRelation, nextblkno);
		LockBuffer(cbuf, BUFFER_LOCK_SHARE);
		cpage = BufferGetPage(cbuf);

		maxoffno = PageGetMaxOffsetNumber(cpage);

		for (OffsetNumber offno = FirstOffsetNumber; offno <= maxoffno; offno = OffsetNumberNext(offno))
		{
			IvfflatList list = (IvfflatList) PageGetItem(cpage, PageGetItemId(cpage, offno));
			double		distance;

			/* Use procinfo from the index instead of scan key for performance */
			distance = DatumGetFloat8(so->distfunc(so->procinfo, so->collation, PointerGetDatum(&list->center), value));

			if (listCount < so->maxProbes)
			{
				IvfflatScanList *scanlist;

				scanlist = &so->lists[listCount];
				scanlist->startPage = list->startPage;
				scanlist->distance = distance;
				listCount++;

				/* Add to heap */
				pairingheap_add(so->listQueue, &scanlist->ph_node);

				/* Calculate max distance */
				if (listCount == so->maxProbes)
					maxDistance = GetScanList(pairingheap_first(so->listQueue))->distance;
			}
			else if (distance < maxDistance)
			{
				IvfflatScanList *scanlist;

				/* Remove */
				scanlist = GetScanList(pairingheap_remove_first(so->listQueue));

				/* Reuse */
				scanlist->startPage = list->startPage;
				scanlist->distance = distance;
				pairingheap_add(so->listQueue, &scanlist->ph_node);

				/* Update max distance */
				maxDistance = GetScanList(pairingheap_first(so->listQueue))->distance;
			}
		}

		nextblkno = IvfflatPageGetOpaque(cpage)->nextblkno;

		UnlockReleaseBuffer(cbuf);
	}

	for (int i = listCount - 1; i >= 0; i--)
		so->listPages[i] = GetScanList(pairingheap_remove_first(so->listQueue))->startPage;

	Assert(pairingheap_is_empty(so->listQueue));
}

/*
 * Get items
 */
static void
GetScanItems(IndexScanDesc scan, Datum value)
{
	IvfflatScanOpaque so = (IvfflatScanOpaque) scan->opaque;
	TupleDesc	tupdesc = RelationGetDescr(scan->indexRelation);
	TupleTableSlot *slot = so->vslot;
	int			batchProbes = 0;

	tuplesort_reset(so->sortstate);

	/* Search closest probes lists */
	while (so->listIndex < so->maxProbes && (++batchProbes) <= so->probes)
	{
		BlockNumber searchPage = so->listPages[so->listIndex++];

		/* Search all entry pages for list */
		while (BlockNumberIsValid(searchPage))
		{
			Buffer		buf;
			Page		page;
			OffsetNumber maxoffno;

			buf = ReadBufferExtended(scan->indexRelation, MAIN_FORKNUM, searchPage, RBM_NORMAL, so->bas);
			LockBuffer(buf, BUFFER_LOCK_SHARE);
			page = BufferGetPage(buf);
			maxoffno = PageGetMaxOffsetNumber(page);

			for (OffsetNumber offno = FirstOffsetNumber; offno <= maxoffno; offno = OffsetNumberNext(offno))
			{
				IndexTuple	itup;
				Datum		datum;
				bool		isnull;
				ItemId		itemid = PageGetItemId(page, offno);

				itup = (IndexTuple) PageGetItem(page, itemid);
				datum = index_getattr(itup, 1, tupdesc, &isnull);

				/*
				 * Add virtual tuple
				 *
				 * Use procinfo from the index instead of scan key for
				 * performance
				 */
				ExecClearTuple(slot);
				slot->tts_values[0] = so->distfunc(so->procinfo, so->collation, datum, value);
				slot->tts_isnull[0] = false;
				slot->tts_values[1] = PointerGetDatum(&itup->t_tid);
				slot->tts_isnull[1] = false;
				ExecStoreVirtualTuple(slot);

				tuplesort_puttupleslot(so->sortstate, slot);
			}

			searchPage = IvfflatPageGetOpaque(page)->nextblkno;

			UnlockReleaseBuffer(buf);
		}
	}

	tuplesort_performsort(so->sortstate);

#if defined(IVFFLAT_MEMORY)
	elog(INFO, "memory: %zu MB", MemoryContextMemAllocated(CurrentMemoryContext, true) / (1024 * 1024));
#endif
}

/*
 * Zero distance
 */
static Datum
ZeroDistance(FmgrInfo *flinfo, Oid collation, Datum arg1, Datum arg2)
{
	return Float8GetDatum(0.0);
}

/*
 * Get scan value
 */
static Datum
GetScanValue(IndexScanDesc scan)
{
	IvfflatScanOpaque so = (IvfflatScanOpaque) scan->opaque;
	Datum		value;

	if (scan->orderByData->sk_flags & SK_ISNULL)
	{
		value = PointerGetDatum(NULL);
		so->distfunc = ZeroDistance;
	}
	else
	{
		value = scan->orderByData->sk_argument;
		so->distfunc = FunctionCall2Coll;

		/* Value should not be compressed or toasted */
		Assert(!VARATT_IS_COMPRESSED(DatumGetPointer(value)));
		Assert(!VARATT_IS_EXTENDED(DatumGetPointer(value)));

		/* Normalize if needed */
		if (so->normprocinfo != NULL)
		{
			MemoryContext oldCtx = MemoryContextSwitchTo(so->tmpCtx);

			value = IvfflatNormValue(so->typeInfo, so->collation, value);

			MemoryContextSwitchTo(oldCtx);
		}
	}

	return value;
}

/*
 * Initialize scan sort state
 */
static Tuplesortstate *
InitScanSortState(TupleDesc tupdesc)
{
	AttrNumber	attNums[] = {1};
	Oid			sortOperators[] = {Float8LessOperator};
	Oid			sortCollations[] = {InvalidOid};
	bool		nullsFirstFlags[] = {false};

	return tuplesort_begin_heap(tupdesc, 1, attNums, sortOperators, sortCollations, nullsFirstFlags, work_mem, NULL, false);
}

/*
 * Prepare for an index scan
 */
IndexScanDesc
ivfflatbeginscan(Relation index, int nkeys, int norderbys)
{
	IndexScanDesc scan;
	IvfflatScanOpaque so;
	int			lists;
	int			dimensions;
	int			probes = ivfflat_probes;
	int			maxProbes;
	MemoryContext oldCtx;

	scan = RelationGetIndexScan(index, nkeys, norderbys);

	/* Get lists and dimensions from metapage */
	IvfflatGetMetaPageInfo(index, &lists, &dimensions);

	if (ivfflat_iterative_scan != IVFFLAT_ITERATIVE_SCAN_OFF)
		maxProbes = Max(ivfflat_max_probes, probes);
	else
		maxProbes = probes;

	if (probes > lists)
		probes = lists;

	if (maxProbes > lists)
		maxProbes = lists;

	so = (IvfflatScanOpaque) palloc(sizeof(IvfflatScanOpaqueData));
	so->typeInfo = IvfflatGetTypeInfo(index);
	so->first = true;
	so->probes = probes;
	so->maxProbes = maxProbes;
	so->dimensions = dimensions;

	/* Set support functions */
	so->procinfo = index_getprocinfo(index, 1, IVFFLAT_DISTANCE_PROC);
	so->normprocinfo = IvfflatOptionalProcInfo(index, IVFFLAT_NORM_PROC);
	so->collation = index->rd_indcollation[0];

	so->tmpCtx = AllocSetContextCreate(CurrentMemoryContext,
									   "Ivfflat scan temporary context",
									   ALLOCSET_DEFAULT_SIZES);

	oldCtx = MemoryContextSwitchTo(so->tmpCtx);

	/* Create tuple description for sorting */
	so->tupdesc = CreateTemplateTupleDesc(2);
	TupleDescInitEntry(so->tupdesc, (AttrNumber) 1, "distance", FLOAT8OID, -1, 0);
	TupleDescInitEntry(so->tupdesc, (AttrNumber) 2, "heaptid", TIDOID, -1, 0);

	/* Prep sort */
	so->sortstate = InitScanSortState(so->tupdesc);

	/* Need separate slots for puttuple and gettuple */
	so->vslot = MakeSingleTupleTableSlot(so->tupdesc, &TTSOpsVirtual);
	so->mslot = MakeSingleTupleTableSlot(so->tupdesc, &TTSOpsMinimalTuple);

	/*
	 * Reuse same set of shared buffers for scan
	 *
	 * See postgres/src/backend/storage/buffer/README for description
	 */
	so->bas = GetAccessStrategy(BAS_BULKREAD);

	so->listQueue = pairingheap_allocate(CompareLists, scan);
	so->listPages = palloc(maxProbes * sizeof(BlockNumber));
	so->listIndex = 0;
	so->lists = palloc(maxProbes * sizeof(IvfflatScanList));

	MemoryContextSwitchTo(oldCtx);

	scan->opaque = so;

	return scan;
}

/*
 * Start or restart an index scan
 */
void
ivfflatrescan(IndexScanDesc scan, ScanKey keys, int nkeys, ScanKey orderbys, int norderbys)
{
	IvfflatScanOpaque so = (IvfflatScanOpaque) scan->opaque;

	so->first = true;
	pairingheap_reset(so->listQueue);
	so->listIndex = 0;

	if (keys && scan->numberOfKeys > 0)
		memmove(scan->keyData, keys, scan->numberOfKeys * sizeof(ScanKeyData));

	if (orderbys && scan->numberOfOrderBys > 0)
		memmove(scan->orderByData, orderbys, scan->numberOfOrderBys * sizeof(ScanKeyData));
}

/*
 * Fetch the next tuple in the given scan
 */
bool
ivfflatgettuple(IndexScanDesc scan, ScanDirection dir)
{
	IvfflatScanOpaque so = (IvfflatScanOpaque) scan->opaque;
	ItemPointer heaptid;
	bool		isnull;

	/*
	 * Index can be used to scan backward, but Postgres doesn't support
	 * backward scan on operators
	 */
	Assert(ScanDirectionIsForward(dir));

	if (so->first)
	{
		Datum		value;

		/* Count index scan for stats */
		pgstat_count_index_scan(scan->indexRelation);
#if PG_VERSION_NUM >= 180000
		if (scan->instrument)
			scan->instrument->nsearches++;
#endif

		/* Safety check */
		if (scan->orderByData == NULL)
			elog(ERROR, "cannot scan ivfflat index without order");

		/* Requires MVCC-compliant snapshot as not able to pin during sorting */
		/* https://www.postgresql.org/docs/current/index-locking.html */
		if (!IsMVCCSnapshot(scan->xs_snapshot))
			elog(ERROR, "non-MVCC snapshots are not supported with ivfflat");

		value = GetScanValue(scan);
		IvfflatBench("GetScanLists", GetScanLists(scan, value));
		IvfflatBench("GetScanItems", GetScanItems(scan, value));
		so->first = false;
		so->value = value;
	}

	while (!tuplesort_gettupleslot(so->sortstate, true, false, so->mslot, NULL))
	{
		if (so->listIndex == so->maxProbes)
			return false;

		IvfflatBench("GetScanItems", GetScanItems(scan, so->value));
	}

	heaptid = (ItemPointer) DatumGetPointer(slot_getattr(so->mslot, 2, &isnull));

	scan->xs_heaptid = *heaptid;
	scan->xs_recheck = false;
	scan->xs_recheckorderby = false;
	return true;
}

/*
 * End a scan and release resources
 */
void
ivfflatendscan(IndexScanDesc scan)
{
	IvfflatScanOpaque so = (IvfflatScanOpaque) scan->opaque;

	/* Free any temporary files */
	tuplesort_end(so->sortstate);

	MemoryContextDelete(so->tmpCtx);

	pfree(so);
	scan->opaque = NULL;
}
```

## File: `src/ivfutils.c`
```c
#include "postgres.h"

#include "access/genam.h"
#include "access/generic_xlog.h"
#include "fmgr.h"
#include "halfutils.h"
#include "halfvec.h"
#include "ivfflat.h"
#include "storage/bufmgr.h"
#include "utils/relcache.h"
#include "utils/varbit.h"
#include "vector.h"

#if PG_VERSION_NUM >= 160000
#include "varatt.h"
#endif

/*
 * Allocate a vector array
 */
VectorArray
VectorArrayInit(int maxlen, int dimensions, Size itemsize)
{
	VectorArray res = palloc(sizeof(VectorArrayData));

	/* Ensure items are aligned to prevent UB */
	itemsize = MAXALIGN(itemsize);

	res->length = 0;
	res->maxlen = maxlen;
	res->dim = dimensions;
	res->itemsize = itemsize;
	res->items = palloc_extended(maxlen * itemsize, MCXT_ALLOC_ZERO | MCXT_ALLOC_HUGE);
	return res;
}

/*
 * Free a vector array
 */
void
VectorArrayFree(VectorArray arr)
{
	pfree(arr->items);
	pfree(arr);
}

/*
 * Get the number of lists in the index
 */
int
IvfflatGetLists(Relation index)
{
	IvfflatOptions *opts = (IvfflatOptions *) index->rd_options;

	if (opts)
		return opts->lists;

	return IVFFLAT_DEFAULT_LISTS;
}

/*
 * Get proc
 */
FmgrInfo *
IvfflatOptionalProcInfo(Relation index, uint16 procnum)
{
	if (!OidIsValid(index_getprocid(index, 1, procnum)))
		return NULL;

	return index_getprocinfo(index, 1, procnum);
}

/*
 * Normalize value
 */
Datum
IvfflatNormValue(const IvfflatTypeInfo * typeInfo, Oid collation, Datum value)
{
	return DirectFunctionCall1Coll(typeInfo->normalize, collation, value);
}

/*
 * Check if non-zero norm
 */
bool
IvfflatCheckNorm(FmgrInfo *procinfo, Oid collation, Datum value)
{
	return DatumGetFloat8(FunctionCall1Coll(procinfo, collation, value)) > 0;
}

/*
 * New buffer
 */
Buffer
IvfflatNewBuffer(Relation index, ForkNumber forkNum)
{
	Buffer		buf = ReadBufferExtended(index, forkNum, P_NEW, RBM_NORMAL, NULL);

	LockBuffer(buf, BUFFER_LOCK_EXCLUSIVE);
	return buf;
}

/*
 * Init page
 */
void
IvfflatInitPage(Buffer buf, Page page)
{
	PageInit(page, BufferGetPageSize(buf), sizeof(IvfflatPageOpaqueData));
	IvfflatPageGetOpaque(page)->nextblkno = InvalidBlockNumber;
	IvfflatPageGetOpaque(page)->page_id = IVFFLAT_PAGE_ID;
}

/*
 * Init and register page
 */
void
IvfflatInitRegisterPage(Relation index, Buffer *buf, Page *page, GenericXLogState **state)
{
	*state = GenericXLogStart(index);
	*page = GenericXLogRegisterBuffer(*state, *buf, GENERIC_XLOG_FULL_IMAGE);
	IvfflatInitPage(*buf, *page);
}

/*
 * Commit buffer
 */
void
IvfflatCommitBuffer(Buffer buf, GenericXLogState *state)
{
	GenericXLogFinish(state);
	UnlockReleaseBuffer(buf);
}

/*
 * Add a new page
 *
 * The order is very important!!
 */
void
IvfflatAppendPage(Relation index, Buffer *buf, Page *page, GenericXLogState **state, ForkNumber forkNum)
{
	/* Get new buffer */
	Buffer		newbuf = IvfflatNewBuffer(index, forkNum);
	Page		newpage = GenericXLogRegisterBuffer(*state, newbuf, GENERIC_XLOG_FULL_IMAGE);

	/* Update the previous buffer */
	IvfflatPageGetOpaque(*page)->nextblkno = BufferGetBlockNumber(newbuf);

	/* Init new page */
	IvfflatInitPage(newbuf, newpage);

	/* Commit */
	GenericXLogFinish(*state);

	/* Unlock */
	UnlockReleaseBuffer(*buf);

	*state = GenericXLogStart(index);
	*page = GenericXLogRegisterBuffer(*state, newbuf, GENERIC_XLOG_FULL_IMAGE);
	*buf = newbuf;
}

/*
 * Get the metapage info
 */
void
IvfflatGetMetaPageInfo(Relation index, int *lists, int *dimensions)
{
	Buffer		buf;
	Page		page;
	IvfflatMetaPage metap;

	buf = ReadBuffer(index, IVFFLAT_METAPAGE_BLKNO);
	LockBuffer(buf, BUFFER_LOCK_SHARE);
	page = BufferGetPage(buf);
	metap = IvfflatPageGetMeta(page);

	if (unlikely(metap->magicNumber != IVFFLAT_MAGIC_NUMBER))
		elog(ERROR, "ivfflat index is not valid");

	if (lists != NULL)
		*lists = metap->lists;

	if (dimensions != NULL)
		*dimensions = metap->dimensions;

	UnlockReleaseBuffer(buf);
}

/*
 * Update the start or insert page of a list
 */
void
IvfflatUpdateList(Relation index, ListInfo listInfo,
				  BlockNumber insertPage, BlockNumber originalInsertPage,
				  BlockNumber startPage, ForkNumber forkNum)
{
	Buffer		buf;
	Page		page;
	GenericXLogState *state;
	IvfflatList list;
	bool		changed = false;

	buf = ReadBufferExtended(index, forkNum, listInfo.blkno, RBM_NORMAL, NULL);
	LockBuffer(buf, BUFFER_LOCK_EXCLUSIVE);
	state = GenericXLogStart(index);
	page = GenericXLogRegisterBuffer(state, buf, 0);
	list = (IvfflatList) PageGetItem(page, PageGetItemId(page, listInfo.offno));

	if (BlockNumberIsValid(insertPage) && insertPage != list->insertPage)
	{
		/* Skip update if insert page is lower than original insert page  */
		/* This is needed to prevent insert from overwriting vacuum */
		if (!BlockNumberIsValid(originalInsertPage) || insertPage >= originalInsertPage)
		{
			list->insertPage = insertPage;
			changed = true;
		}
	}

	if (BlockNumberIsValid(startPage) && startPage != list->startPage)
	{
		list->startPage = startPage;
		changed = true;
	}

	/* Only commit if changed */
	if (changed)
		IvfflatCommitBuffer(buf, state);
	else
	{
		GenericXLogAbort(state);
		UnlockReleaseBuffer(buf);
	}
}

PGDLLEXPORT Datum l2_normalize(PG_FUNCTION_ARGS);
PGDLLEXPORT Datum halfvec_l2_normalize(PG_FUNCTION_ARGS);
PGDLLEXPORT Datum sparsevec_l2_normalize(PG_FUNCTION_ARGS);

static Size
VectorItemSize(int dimensions)
{
	return VECTOR_SIZE(dimensions);
}

static Size
HalfvecItemSize(int dimensions)
{
	return HALFVEC_SIZE(dimensions);
}

static Size
BitItemSize(int dimensions)
{
	return VARBITTOTALLEN(dimensions);
}

static void
VectorUpdateCenter(Pointer v, int dimensions, float *x)
{
	Vector	   *vec = (Vector *) v;

	SET_VARSIZE(vec, VECTOR_SIZE(dimensions));
	vec->dim = dimensions;

	for (int i = 0; i < dimensions; i++)
		vec->x[i] = x[i];
}

static void
HalfvecUpdateCenter(Pointer v, int dimensions, float *x)
{
	HalfVector *vec = (HalfVector *) v;

	SET_VARSIZE(vec, HALFVEC_SIZE(dimensions));
	vec->dim = dimensions;

	for (int i = 0; i < dimensions; i++)
		vec->x[i] = Float4ToHalfUnchecked(x[i]);
}

static void
BitUpdateCenter(Pointer v, int dimensions, float *x)
{
	VarBit	   *vec = (VarBit *) v;
	unsigned char *nx = VARBITS(vec);

	SET_VARSIZE(vec, VARBITTOTALLEN(dimensions));
	VARBITLEN(vec) = dimensions;

	for (uint32 i = 0; i < VARBITBYTES(vec); i++)
		nx[i] = 0;

	for (int i = 0; i < dimensions; i++)
		nx[i / 8] |= (x[i] > 0.5 ? 1 : 0) << (7 - (i % 8));
}

static void
VectorSumCenter(Pointer v, float *x)
{
	Vector	   *vec = (Vector *) v;
	int			dim = vec->dim;

	/* Auto-vectorized */
	for (int i = 0; i < dim; i++)
		x[i] += vec->x[i];
}

static void
HalfvecSumCenter(Pointer v, float *x)
{
	HalfVector *vec = (HalfVector *) v;
	int			dim = vec->dim;

	/* Auto-vectorized on aarch64 */
	for (int i = 0; i < dim; i++)
		x[i] += HalfToFloat4(vec->x[i]);
}

static void
BitSumCenter(Pointer v, float *x)
{
	VarBit	   *vec = (VarBit *) v;

	for (int i = 0; i < VARBITLEN(vec); i++)
		x[i] += (float) (((VARBITS(vec)[i / 8]) >> (7 - (i % 8))) & 0x01);
}

/*
 * Get type info
 */
const		IvfflatTypeInfo *
IvfflatGetTypeInfo(Relation index)
{
	FmgrInfo   *procinfo = IvfflatOptionalProcInfo(index, IVFFLAT_TYPE_INFO_PROC);

	if (procinfo == NULL)
	{
		static const IvfflatTypeInfo typeInfo = {
			.maxDimensions = IVFFLAT_MAX_DIM,
			.normalize = l2_normalize,
			.itemSize = VectorItemSize,
			.updateCenter = VectorUpdateCenter,
			.sumCenter = VectorSumCenter
		};

		return (&typeInfo);
	}
	else
		return (const IvfflatTypeInfo *) DatumGetPointer(FunctionCall0Coll(procinfo, InvalidOid));
}

FUNCTION_PREFIX PG_FUNCTION_INFO_V1(ivfflat_halfvec_support);
Datum
ivfflat_halfvec_support(PG_FUNCTION_ARGS)
{
	static const IvfflatTypeInfo typeInfo = {
		.maxDimensions = IVFFLAT_MAX_DIM * 2,
		.normalize = halfvec_l2_normalize,
		.itemSize = HalfvecItemSize,
		.updateCenter = HalfvecUpdateCenter,
		.sumCenter = HalfvecSumCenter
	};

	PG_RETURN_POINTER(&typeInfo);
}

FUNCTION_PREFIX PG_FUNCTION_INFO_V1(ivfflat_bit_support);
Datum
ivfflat_bit_support(PG_FUNCTION_ARGS)
{
	static const IvfflatTypeInfo typeInfo = {
		.maxDimensions = IVFFLAT_MAX_DIM * 32,
		.normalize = NULL,
		.itemSize = BitItemSize,
		.updateCenter = BitUpdateCenter,
		.sumCenter = BitSumCenter
	};

	PG_RETURN_POINTER(&typeInfo);
}
```

## File: `src/ivfvacuum.c`
```c
#include "postgres.h"

#include "access/genam.h"
#include "access/generic_xlog.h"
#include "access/itup.h"
#include "commands/vacuum.h"
#include "ivfflat.h"
#include "storage/bufmgr.h"
#include "utils/relcache.h"

#if PG_VERSION_NUM >= 180000
#define vacuum_delay_point() vacuum_delay_point(false)
#endif

/*
 * Bulk delete tuples from the index
 */
IndexBulkDeleteResult *
ivfflatbulkdelete(IndexVacuumInfo *info, IndexBulkDeleteResult *stats,
				  IndexBulkDeleteCallback callback, void *callback_state)
{
	Relation	index = info->index;
	BlockNumber blkno = IVFFLAT_HEAD_BLKNO;
	BufferAccessStrategy bas = GetAccessStrategy(BAS_BULKREAD);

	if (stats == NULL)
		stats = (IndexBulkDeleteResult *) palloc0(sizeof(IndexBulkDeleteResult));

	/* Iterate over list pages */
	while (BlockNumberIsValid(blkno))
	{
		Buffer		cbuf;
		Page		cpage;
		OffsetNumber coffno;
		OffsetNumber cmaxoffno;
		BlockNumber listPages[MaxOffsetNumber];
		ListInfo	listInfo;

		cbuf = ReadBuffer(index, blkno);
		LockBuffer(cbuf, BUFFER_LOCK_SHARE);
		cpage = BufferGetPage(cbuf);

		cmaxoffno = PageGetMaxOffsetNumber(cpage);

		/* Iterate over lists */
		for (coffno = FirstOffsetNumber; coffno <= cmaxoffno; coffno = OffsetNumberNext(coffno))
		{
			IvfflatList list = (IvfflatList) PageGetItem(cpage, PageGetItemId(cpage, coffno));

			listPages[coffno - FirstOffsetNumber] = list->startPage;
		}

		listInfo.blkno = blkno;
		blkno = IvfflatPageGetOpaque(cpage)->nextblkno;

		UnlockReleaseBuffer(cbuf);

		for (coffno = FirstOffsetNumber; coffno <= cmaxoffno; coffno = OffsetNumberNext(coffno))
		{
			BlockNumber searchPage = listPages[coffno - FirstOffsetNumber];
			BlockNumber insertPage = InvalidBlockNumber;

			/* Iterate over entry pages */
			while (BlockNumberIsValid(searchPage))
			{
				Buffer		buf;
				Page		page;
				GenericXLogState *state;
				OffsetNumber offno;
				OffsetNumber maxoffno;
				OffsetNumber deletable[MaxOffsetNumber];
				int			ndeletable;

				vacuum_delay_point();

				buf = ReadBufferExtended(index, MAIN_FORKNUM, searchPage, RBM_NORMAL, bas);

				/*
				 * ambulkdelete cannot delete entries from pages that are
				 * pinned by other backends
				 *
				 * https://www.postgresql.org/docs/current/index-locking.html
				 */
				LockBufferForCleanup(buf);

				state = GenericXLogStart(index);
				page = GenericXLogRegisterBuffer(state, buf, 0);

				maxoffno = PageGetMaxOffsetNumber(page);
				ndeletable = 0;

				/* Find deleted tuples */
				for (offno = FirstOffsetNumber; offno <= maxoffno; offno = OffsetNumberNext(offno))
				{
					IndexTuple	itup = (IndexTuple) PageGetItem(page, PageGetItemId(page, offno));
					ItemPointer htup = &(itup->t_tid);

					if (callback(htup, callback_state))
					{
						deletable[ndeletable++] = offno;
						stats->tuples_removed++;
					}
					else
						stats->num_index_tuples++;
				}

				/* Set to first free page */
				/* Must be set before searchPage is updated */
				if (!BlockNumberIsValid(insertPage) && ndeletable > 0)
					insertPage = searchPage;

				searchPage = IvfflatPageGetOpaque(page)->nextblkno;

				if (ndeletable > 0)
				{
					/* Delete tuples */
					PageIndexMultiDelete(page, deletable, ndeletable);
					GenericXLogFinish(state);
				}
				else
					GenericXLogAbort(state);

				UnlockReleaseBuffer(buf);
			}

			/*
			 * Update after all tuples deleted.
			 *
			 * We don't add or delete items from lists pages, so offset won't
			 * change.
			 */
			if (BlockNumberIsValid(insertPage))
			{
				listInfo.offno = coffno;
				IvfflatUpdateList(index, listInfo, insertPage, InvalidBlockNumber, InvalidBlockNumber, MAIN_FORKNUM);
			}
		}
	}

	FreeAccessStrategy(bas);

	return stats;
}

/*
 * Clean up after a VACUUM operation
 */
IndexBulkDeleteResult *
ivfflatvacuumcleanup(IndexVacuumInfo *info, IndexBulkDeleteResult *stats)
{
	Relation	rel = info->index;

	if (info->analyze_only)
		return stats;

	/* stats is NULL if ambulkdelete not called */
	/* OK to return NULL if index not changed */
	if (stats == NULL)
		return NULL;

	stats->num_pages = RelationGetNumberOfBlocks(rel);

	return stats;
}
```

## File: `src/sparsevec.c`
```c
#include "postgres.h"

#include <limits.h>
#include <math.h>

#include "catalog/pg_type.h"
#include "common/shortest_dec.h"
#include "fmgr.h"
#include "halfutils.h"
#include "halfvec.h"
#include "lib/stringinfo.h"
#include "libpq/pqformat.h"
#include "sparsevec.h"
#include "utils/array.h"
#include "utils/builtins.h"
#include "utils/float.h"
#include "utils/fmgrprotos.h"
#include "utils/lsyscache.h"
#include "vector.h"

#if PG_VERSION_NUM >= 160000
#include "varatt.h"
#endif

#if PG_VERSION_NUM >= 170000
#include "parser/scansup.h"
#endif

typedef struct SparseInputElement
{
	int32		index;
	float		value;
}			SparseInputElement;

/*
 * Ensure same dimensions
 */
static inline void
CheckDims(SparseVector * a, SparseVector * b)
{
	if (a->dim != b->dim)
		ereport(ERROR,
				(errcode(ERRCODE_DATA_EXCEPTION),
				 errmsg("different sparsevec dimensions %d and %d", a->dim, b->dim)));
}

/*
 * Ensure expected dimensions
 */
static inline void
CheckExpectedDim(int32 typmod, int dim)
{
	if (typmod != -1 && typmod != dim)
		ereport(ERROR,
				(errcode(ERRCODE_DATA_EXCEPTION),
				 errmsg("expected %d dimensions, not %d", typmod, dim)));
}

/*
 * Ensure valid dimensions
 */
static inline void
CheckDim(int dim)
{
	if (dim < 1)
		ereport(ERROR,
				(errcode(ERRCODE_DATA_EXCEPTION),
				 errmsg("sparsevec must have at least 1 dimension")));

	if (dim > SPARSEVEC_MAX_DIM)
		ereport(ERROR,
				(errcode(ERRCODE_PROGRAM_LIMIT_EXCEEDED),
				 errmsg("sparsevec cannot have more than %d dimensions", SPARSEVEC_MAX_DIM)));
}

/*
 * Ensure valid nnz
 */
static inline void
CheckNnz(int nnz, int dim)
{
	if (nnz < 0)
		ereport(ERROR,
				(errcode(ERRCODE_DATA_EXCEPTION),
				 errmsg("sparsevec cannot have negative number of elements")));

	if (nnz > SPARSEVEC_MAX_NNZ)
		ereport(ERROR,
				(errcode(ERRCODE_PROGRAM_LIMIT_EXCEEDED),
				 errmsg("sparsevec cannot have more than %d non-zero elements", SPARSEVEC_MAX_NNZ)));

	if (nnz > dim)
		ereport(ERROR,
				(errcode(ERRCODE_PROGRAM_LIMIT_EXCEEDED),
				 errmsg("sparsevec cannot have more elements than dimensions")));
}

/*
 * Ensure valid index
 */
static inline void
CheckIndex(int32 *indices, int i, int dim)
{
	int32		index = indices[i];

	if (index < 0 || index >= dim)
	{
		ereport(ERROR,
				(errcode(ERRCODE_DATA_EXCEPTION),
				 errmsg("sparsevec index out of bounds")));
	}

	if (i > 0)
	{
		if (index < indices[i - 1])
			ereport(ERROR,
					(errcode(ERRCODE_DATA_EXCEPTION),
					 errmsg("sparsevec indices must be in ascending order")));

		if (index == indices[i - 1])
			ereport(ERROR,
					(errcode(ERRCODE_DATA_EXCEPTION),
					 errmsg("sparsevec indices must not contain duplicates")));
	}
}

/*
 * Ensure finite element
 */
static inline void
CheckElement(float value)
{
	if (isnan(value))
		ereport(ERROR,
				(errcode(ERRCODE_DATA_EXCEPTION),
				 errmsg("NaN not allowed in sparsevec")));

	if (isinf(value))
		ereport(ERROR,
				(errcode(ERRCODE_DATA_EXCEPTION),
				 errmsg("infinite value not allowed in sparsevec")));
}

/*
 * Allocate and initialize a new sparse vector
 */
SparseVector *
InitSparseVector(int dim, int nnz)
{
	SparseVector *result;
	int			size;

	size = SPARSEVEC_SIZE(nnz);
	result = (SparseVector *) palloc0(size);
	SET_VARSIZE(result, size);
	result->dim = dim;
	result->nnz = nnz;

	return result;
}

#if PG_VERSION_NUM >= 170000
#define sparsevec_isspace(ch) scanner_isspace(ch)
#else
static inline bool
sparsevec_isspace(char ch)
{
	if (ch == ' ' ||
		ch == '\t' ||
		ch == '\n' ||
		ch == '\r' ||
		ch == '\v' ||
		ch == '\f')
		return true;
	return false;
}
#endif

/*
 * Compare indices
 */
static int
CompareIndices(const void *a, const void *b)
{
	if (((SparseInputElement *) a)->index < ((SparseInputElement *) b)->index)
		return -1;

	if (((SparseInputElement *) a)->index > ((SparseInputElement *) b)->index)
		return 1;

	return 0;
}

/*
 * Convert textual representation to internal representation
 */
FUNCTION_PREFIX PG_FUNCTION_INFO_V1(sparsevec_in);
Datum
sparsevec_in(PG_FUNCTION_ARGS)
{
	char	   *lit = PG_GETARG_CSTRING(0);
	int32		typmod = PG_GETARG_INT32(2);
	long		dim;
	char	   *pt = lit;
	char	   *stringEnd;
	SparseVector *result;
	float	   *rvalues;
	SparseInputElement *elements;
	int			maxNnz;
	int			nnz = 0;

	maxNnz = 1;
	while (*pt != '\0')
	{
		if (*pt == ',')
			maxNnz++;

		pt++;
	}

	if (maxNnz > SPARSEVEC_MAX_NNZ)
		ereport(ERROR,
				(errcode(ERRCODE_PROGRAM_LIMIT_EXCEEDED),
				 errmsg("sparsevec cannot have more than %d non-zero elements", SPARSEVEC_MAX_NNZ)));

	elements = palloc(maxNnz * sizeof(SparseInputElement));

	pt = lit;

	while (sparsevec_isspace(*pt))
		pt++;

	if (*pt != '{')
		ereport(ERROR,
				(errcode(ERRCODE_INVALID_TEXT_REPRESENTATION),
				 errmsg("invalid input syntax for type sparsevec: \"%s\"", lit),
				 errdetail("Vector contents must start with \"{\".")));

	pt++;

	while (sparsevec_isspace(*pt))
		pt++;

	if (*pt == '}')
		pt++;
	else
	{
		for (;;)
		{
			long		index;
			float		value;

			if (nnz == maxNnz)
				ereport(ERROR,
						(errcode(ERRCODE_INVALID_TEXT_REPRESENTATION),
						 errmsg("ran out of buffer: \"%s\"", lit)));

			while (sparsevec_isspace(*pt))
				pt++;

			/* Check for empty string like float4in */
			if (*pt == '\0')
				ereport(ERROR,
						(errcode(ERRCODE_INVALID_TEXT_REPRESENTATION),
						 errmsg("invalid input syntax for type sparsevec: \"%s\"", lit)));

			/* Use similar logic as int2vectorin */
			index = strtol(pt, &stringEnd, 10);

			if (stringEnd == pt)
				ereport(ERROR,
						(errcode(ERRCODE_INVALID_TEXT_REPRESENTATION),
						 errmsg("invalid input syntax for type sparsevec: \"%s\"", lit)));

			/* Keep in int range for correct error message later */
			if (index > INT_MAX)
				index = INT_MAX;
			else if (index < INT_MIN + 1)
				index = INT_MIN + 1;

			pt = stringEnd;

			while (sparsevec_isspace(*pt))
				pt++;

			if (*pt != ':')
				ereport(ERROR,
						(errcode(ERRCODE_INVALID_TEXT_REPRESENTATION),
						 errmsg("invalid input syntax for type sparsevec: \"%s\"", lit)));

			pt++;

			while (sparsevec_isspace(*pt))
				pt++;

			errno = 0;

			/* Use strtof like float4in to avoid a double-rounding problem */
			/* Postgres sets LC_NUMERIC to C on startup */
			value = strtof(pt, &stringEnd);

			if (stringEnd == pt)
				ereport(ERROR,
						(errcode(ERRCODE_INVALID_TEXT_REPRESENTATION),
						 errmsg("invalid input syntax for type sparsevec: \"%s\"", lit)));

			/* Check for range error like float4in */
			if (errno == ERANGE && (value == 0 || isinf(value)))
				ereport(ERROR,
						(errcode(ERRCODE_NUMERIC_VALUE_OUT_OF_RANGE),
						 errmsg("\"%s\" is out of range for type sparsevec", pnstrdup(pt, stringEnd - pt))));

			CheckElement(value);

			/* Do not store zero values */
			if (value != 0)
			{
				/* Convert 1-based numbering (SQL) to 0-based (C) */
				elements[nnz].index = index - 1;
				elements[nnz].value = value;
				nnz++;
			}

			pt = stringEnd;

			while (sparsevec_isspace(*pt))
				pt++;

			if (*pt == ',')
				pt++;
			else if (*pt == '}')
			{
				pt++;
				break;
			}
			else
				ereport(ERROR,
						(errcode(ERRCODE_INVALID_TEXT_REPRESENTATION),
						 errmsg("invalid input syntax for type sparsevec: \"%s\"", lit)));
		}
	}

	while (sparsevec_isspace(*pt))
		pt++;

	if (*pt != '/')
		ereport(ERROR,
				(errcode(ERRCODE_INVALID_TEXT_REPRESENTATION),
				 errmsg("invalid input syntax for type sparsevec: \"%s\"", lit),
				 errdetail("Unexpected end of input.")));

	pt++;

	while (sparsevec_isspace(*pt))
		pt++;

	/* Use similar logic as int2vectorin */
	dim = strtol(pt, &stringEnd, 10);

	if (stringEnd == pt)
		ereport(ERROR,
				(errcode(ERRCODE_INVALID_TEXT_REPRESENTATION),
				 errmsg("invalid input syntax for type sparsevec: \"%s\"", lit)));

	/* Keep in int range for correct error message later */
	if (dim > INT_MAX)
		dim = INT_MAX;
	else if (dim < INT_MIN)
		dim = INT_MIN;

	pt = stringEnd;

	/* Only whitespace is allowed after the closing brace */
	while (sparsevec_isspace(*pt))
		pt++;

	if (*pt != '\0')
		ereport(ERROR,
				(errcode(ERRCODE_INVALID_TEXT_REPRESENTATION),
				 errmsg("invalid input syntax for type sparsevec: \"%s\"", lit),
				 errdetail("Junk after closing.")));

	CheckDim(dim);
	CheckExpectedDim(typmod, dim);

	qsort(elements, nnz, sizeof(SparseInputElement), CompareIndices);

	result = InitSparseVector(dim, nnz);
	rvalues = SPARSEVEC_VALUES(result);
	for (int i = 0; i < nnz; i++)
	{
		result->indices[i] = elements[i].index;
		rvalues[i] = elements[i].value;

		CheckIndex(result->indices, i, dim);
	}

	PG_RETURN_POINTER(result);
}

#define AppendChar(ptr, c) (*(ptr)++ = (c))
#define AppendFloat(ptr, f) ((ptr) += float_to_shortest_decimal_bufn((f), (ptr)))

#if PG_VERSION_NUM >= 140000
#define AppendInt(ptr, i) ((ptr) += pg_ltoa((i), (ptr)))
#else
#define AppendInt(ptr, i) \
	do { \
		pg_ltoa(i, ptr); \
		while (*ptr != '\0') \
			ptr++; \
	} while (0)
#endif

/*
 * Convert internal representation to textual representation
 */
FUNCTION_PREFIX PG_FUNCTION_INFO_V1(sparsevec_out);
Datum
sparsevec_out(PG_FUNCTION_ARGS)
{
	SparseVector *sparsevec = PG_GETARG_SPARSEVEC_P(0);
	float	   *values = SPARSEVEC_VALUES(sparsevec);
	char	   *buf;
	char	   *ptr;

	/*
	 * Need:
	 *
	 * nnz * 10 bytes for index (positive integer)
	 *
	 * nnz bytes for :
	 *
	 * nnz * (FLOAT_SHORTEST_DECIMAL_LEN - 1) bytes for
	 * float_to_shortest_decimal_bufn
	 *
	 * nnz - 1 bytes for ,
	 *
	 * 10 bytes for dimensions
	 *
	 * 4 bytes for {, }, /, and \0
	 */
	buf = (char *) palloc((11 + FLOAT_SHORTEST_DECIMAL_LEN) * sparsevec->nnz + 13);
	ptr = buf;

	AppendChar(ptr, '{');

	for (int i = 0; i < sparsevec->nnz; i++)
	{
		if (i > 0)
			AppendChar(ptr, ',');

		/* Convert 0-based numbering (C) to 1-based (SQL) */
		AppendInt(ptr, sparsevec->indices[i] + 1);
		AppendChar(ptr, ':');
		AppendFloat(ptr, values[i]);
	}

	AppendChar(ptr, '}');
	AppendChar(ptr, '/');
	AppendInt(ptr, sparsevec->dim);
	*ptr = '\0';

	PG_FREE_IF_COPY(sparsevec, 0);
	PG_RETURN_CSTRING(buf);
}

/*
 * Convert type modifier
 */
FUNCTION_PREFIX PG_FUNCTION_INFO_V1(sparsevec_typmod_in);
Datum
sparsevec_typmod_in(PG_FUNCTION_ARGS)
{
	ArrayType  *ta = PG_GETARG_ARRAYTYPE_P(0);
	int32	   *tl;
	int			n;

	tl = ArrayGetIntegerTypmods(ta, &n);

	if (n != 1)
		ereport(ERROR,
				(errcode(ERRCODE_INVALID_PARAMETER_VALUE),
				 errmsg("invalid type modifier")));

	if (*tl < 1)
		ereport(ERROR,
				(errcode(ERRCODE_INVALID_PARAMETER_VALUE),
				 errmsg("dimensions for type sparsevec must be at least 1")));

	if (*tl > SPARSEVEC_MAX_DIM)
		ereport(ERROR,
				(errcode(ERRCODE_INVALID_PARAMETER_VALUE),
				 errmsg("dimensions for type sparsevec cannot exceed %d", SPARSEVEC_MAX_DIM)));

	PG_RETURN_INT32(*tl);
}

/*
 * Convert external binary representation to internal representation
 */
FUNCTION_PREFIX PG_FUNCTION_INFO_V1(sparsevec_recv);
Datum
sparsevec_recv(PG_FUNCTION_ARGS)
{
	StringInfo	buf = (StringInfo) PG_GETARG_POINTER(0);
	int32		typmod = PG_GETARG_INT32(2);
	SparseVector *result;
	int32		dim;
	int32		nnz;
	int32		unused;
	float	   *values;

	dim = pq_getmsgint(buf, sizeof(int32));
	nnz = pq_getmsgint(buf, sizeof(int32));
	unused = pq_getmsgint(buf, sizeof(int32));

	CheckDim(dim);
	CheckNnz(nnz, dim);
	CheckExpectedDim(typmod, dim);

	if (unused != 0)
		ereport(ERROR,
				(errcode(ERRCODE_DATA_EXCEPTION),
				 errmsg("expected unused to be 0, not %d", unused)));

	result = InitSparseVector(dim, nnz);
	values = SPARSEVEC_VALUES(result);

	/* Binary representation uses zero-based numbering for indices */
	for (int i = 0; i < nnz; i++)
	{
		result->indices[i] = pq_getmsgint(buf, sizeof(int32));
		CheckIndex(result->indices, i, dim);
	}

	for (int i = 0; i < nnz; i++)
	{
		values[i] = pq_getmsgfloat4(buf);
		CheckElement(values[i]);

		if (values[i] == 0)
			ereport(ERROR,
					(errcode(ERRCODE_DATA_EXCEPTION),
					 errmsg("binary representation of sparsevec cannot contain zero values")));
	}

	PG_RETURN_POINTER(result);
}

/*
 * Convert internal representation to the external binary representation
 */
FUNCTION_PREFIX PG_FUNCTION_INFO_V1(sparsevec_send);
Datum
sparsevec_send(PG_FUNCTION_ARGS)
{
	SparseVector *svec = PG_GETARG_SPARSEVEC_P(0);
	float	   *values = SPARSEVEC_VALUES(svec);
	StringInfoData buf;

	pq_begintypsend(&buf);
	pq_sendint(&buf, svec->dim, sizeof(int32));
	pq_sendint(&buf, svec->nnz, sizeof(int32));
	pq_sendint(&buf, svec->unused, sizeof(int32));

	/* Binary representation uses zero-based numbering for indices */
	for (int i = 0; i < svec->nnz; i++)
		pq_sendint(&buf, svec->indices[i], sizeof(int32));

	for (int i = 0; i < svec->nnz; i++)
		pq_sendfloat4(&buf, values[i]);

	PG_RETURN_BYTEA_P(pq_endtypsend(&buf));
}

/*
 * Convert sparse vector to sparse vector
 * This is needed to check the type modifier
 */
FUNCTION_PREFIX PG_FUNCTION_INFO_V1(sparsevec);
Datum
sparsevec(PG_FUNCTION_ARGS)
{
	SparseVector *svec = PG_GETARG_SPARSEVEC_P(0);
	int32		typmod = PG_GETARG_INT32(1);

	CheckExpectedDim(typmod, svec->dim);

	PG_RETURN_POINTER(svec);
}

/*
 * Convert dense vector to sparse vector
 */
FUNCTION_PREFIX PG_FUNCTION_INFO_V1(vector_to_sparsevec);
Datum
vector_to_sparsevec(PG_FUNCTION_ARGS)
{
	Vector	   *vec = PG_GETARG_VECTOR_P(0);
	int32		typmod = PG_GETARG_INT32(1);
	SparseVector *result;
	int			dim = vec->dim;
	int			nnz = 0;
	float	   *values;
	int			j = 0;

	CheckDim(dim);
	CheckExpectedDim(typmod, dim);

	for (int i = 0; i < dim; i++)
	{
		if (vec->x[i] != 0)
			nnz++;
	}

	result = InitSparseVector(dim, nnz);
	values = SPARSEVEC_VALUES(result);
	for (int i = 0; i < dim; i++)
	{
		if (vec->x[i] != 0)
		{
			/* Safety check */
			if (j >= result->nnz)
				elog(ERROR, "safety check failed");

			result->indices[j] = i;
			values[j] = vec->x[i];
			j++;
		}
	}

	PG_RETURN_POINTER(result);
}

/*
 * Convert half vector to sparse vector
 */
FUNCTION_PREFIX PG_FUNCTION_INFO_V1(halfvec_to_sparsevec);
Datum
halfvec_to_sparsevec(PG_FUNCTION_ARGS)
{
	HalfVector *vec = PG_GETARG_HALFVEC_P(0);
	int32		typmod = PG_GETARG_INT32(1);
	SparseVector *result;
	int			dim = vec->dim;
	int			nnz = 0;
	float	   *values;
	int			j = 0;

	CheckDim(dim);
	CheckExpectedDim(typmod, dim);

	for (int i = 0; i < dim; i++)
	{
		if (!HalfIsZero(vec->x[i]))
			nnz++;
	}

	result = InitSparseVector(dim, nnz);
	values = SPARSEVEC_VALUES(result);
	for (int i = 0; i < dim; i++)
	{
		if (!HalfIsZero(vec->x[i]))
		{
			/* Safety check */
			if (j >= result->nnz)
				elog(ERROR, "safety check failed");

			result->indices[j] = i;
			values[j] = HalfToFloat4(vec->x[i]);
			j++;
		}
	}

	PG_RETURN_POINTER(result);
}

/*
 * Convert array to sparse vector
 */
FUNCTION_PREFIX PG_FUNCTION_INFO_V1(array_to_sparsevec);
Datum
array_to_sparsevec(PG_FUNCTION_ARGS)
{
	ArrayType  *array = PG_GETARG_ARRAYTYPE_P(0);
	int32		typmod = PG_GETARG_INT32(1);
	SparseVector *result;
	int16		typlen;
	bool		typbyval;
	char		typalign;
	Datum	   *elemsp;
	int			nelemsp;
	int			nnz = 0;
	float	   *values;
	int			j = 0;

	if (ARR_NDIM(array) > 1)
		ereport(ERROR,
				(errcode(ERRCODE_DATA_EXCEPTION),
				 errmsg("array must be 1-D")));

	if (ARR_HASNULL(array) && array_contains_nulls(array))
		ereport(ERROR,
				(errcode(ERRCODE_NULL_VALUE_NOT_ALLOWED),
				 errmsg("array must not contain nulls")));

	get_typlenbyvalalign(ARR_ELEMTYPE(array), &typlen, &typbyval, &typalign);
	deconstruct_array(array, ARR_ELEMTYPE(array), typlen, typbyval, typalign, &elemsp, NULL, &nelemsp);

	CheckDim(nelemsp);
	CheckExpectedDim(typmod, nelemsp);

#ifdef _MSC_VER
/* /fp:fast may not propagate +/-Infinity or NaN */
#define IS_NOT_ZERO(v) (isnan((float) (v)) || isinf((float) (v)) || ((float) (v)) != 0)
#else
#define IS_NOT_ZERO(v) (((float) (v)) != 0)
#endif

	if (ARR_ELEMTYPE(array) == INT4OID)
	{
		for (int i = 0; i < nelemsp; i++)
			nnz += IS_NOT_ZERO(DatumGetInt32(elemsp[i]));
	}
	else if (ARR_ELEMTYPE(array) == FLOAT8OID)
	{
		for (int i = 0; i < nelemsp; i++)
			nnz += IS_NOT_ZERO(DatumGetFloat8(elemsp[i]));
	}
	else if (ARR_ELEMTYPE(array) == FLOAT4OID)
	{
		for (int i = 0; i < nelemsp; i++)
			nnz += IS_NOT_ZERO(DatumGetFloat4(elemsp[i]));
	}
	else if (ARR_ELEMTYPE(array) == NUMERICOID)
	{
		for (int i = 0; i < nelemsp; i++)
			nnz += IS_NOT_ZERO(DirectFunctionCall1(numeric_float4, elemsp[i]));
	}
	else
	{
		ereport(ERROR,
				(errcode(ERRCODE_DATA_EXCEPTION),
				 errmsg("unsupported array type")));
	}

	result = InitSparseVector(nelemsp, nnz);
	values = SPARSEVEC_VALUES(result);

#define PROCESS_ARRAY_ELEM(elem) \
	do { \
		float v = (float) (elem); \
		if (IS_NOT_ZERO(v)) { \
			/* Safety check */ \
			if (j >= result->nnz) \
				elog(ERROR, "safety check failed"); \
			result->indices[j] = i; \
			values[j] = v; \
			j++; \
		} \
	} while (0)

	if (ARR_ELEMTYPE(array) == INT4OID)
	{
		for (int i = 0; i < nelemsp; i++)
			PROCESS_ARRAY_ELEM(DatumGetInt32(elemsp[i]));
	}
	else if (ARR_ELEMTYPE(array) == FLOAT8OID)
	{
		for (int i = 0; i < nelemsp; i++)
			PROCESS_ARRAY_ELEM(DatumGetFloat8(elemsp[i]));
	}
	else if (ARR_ELEMTYPE(array) == FLOAT4OID)
	{
		for (int i = 0; i < nelemsp; i++)
			PROCESS_ARRAY_ELEM(DatumGetFloat4(elemsp[i]));
	}
	else if (ARR_ELEMTYPE(array) == NUMERICOID)
	{
		for (int i = 0; i < nelemsp; i++)
			PROCESS_ARRAY_ELEM(DatumGetFloat4(DirectFunctionCall1(numeric_float4, elemsp[i])));
	}
	else
	{
		ereport(ERROR,
				(errcode(ERRCODE_DATA_EXCEPTION),
				 errmsg("unsupported array type")));
	}

#undef PROCESS_ARRAY_ELEM
#undef IS_NOT_ZERO

	/*
	 * Free allocation from deconstruct_array. Do not free individual elements
	 * when pass-by-reference since they point to original array.
	 */
	pfree(elemsp);

	if (j != result->nnz)
		elog(ERROR, "correctness check failed");

	/* Check elements */
	for (int i = 0; i < result->nnz; i++)
		CheckElement(values[i]);

	PG_RETURN_POINTER(result);
}

/*
 * Get the L2 squared distance between sparse vectors
 */
static float
SparsevecL2SquaredDistance(SparseVector * a, SparseVector * b)
{
	float	   *ax = SPARSEVEC_VALUES(a);
	float	   *bx = SPARSEVEC_VALUES(b);
	float		distance = 0.0;
	int			bpos = 0;

	for (int i = 0; i < a->nnz; i++)
	{
		int			ai = a->indices[i];
		int			bi = -1;

		for (int j = bpos; j < b->nnz; j++)
		{
			bi = b->indices[j];

			if (ai == bi)
			{
				float		diff = ax[i] - bx[j];

				distance += diff * diff;
			}
			else if (ai > bi)
				distance += bx[j] * bx[j];

			/* Update start for next iteration */
			if (ai >= bi)
				bpos = j + 1;

			/* Found or passed it */
			if (bi >= ai)
				break;
		}

		if (ai != bi)
			distance += ax[i] * ax[i];
	}

	for (int j = bpos; j < b->nnz; j++)
		distance += bx[j] * bx[j];

	return distance;
}

/*
 * Get the L2 distance between sparse vectors
 */
FUNCTION_PREFIX PG_FUNCTION_INFO_V1(sparsevec_l2_distance);
Datum
sparsevec_l2_distance(PG_FUNCTION_ARGS)
{
	SparseVector *a = PG_GETARG_SPARSEVEC_P(0);
	SparseVector *b = PG_GETARG_SPARSEVEC_P(1);

	CheckDims(a, b);

	PG_RETURN_FLOAT8(sqrt((double) SparsevecL2SquaredDistance(a, b)));
}

/*
 * Get the L2 squared distance between sparse vectors
 * This saves a sqrt calculation
 */
FUNCTION_PREFIX PG_FUNCTION_INFO_V1(sparsevec_l2_squared_distance);
Datum
sparsevec_l2_squared_distance(PG_FUNCTION_ARGS)
{
	SparseVector *a = PG_GETARG_SPARSEVEC_P(0);
	SparseVector *b = PG_GETARG_SPARSEVEC_P(1);

	CheckDims(a, b);

	PG_RETURN_FLOAT8((double) SparsevecL2SquaredDistance(a, b));
}

/*
 * Get the inner product of two sparse vectors
 */
static float
SparsevecInnerProduct(SparseVector * a, SparseVector * b)
{
	float	   *ax = SPARSEVEC_VALUES(a);
	float	   *bx = SPARSEVEC_VALUES(b);
	float		distance = 0.0;
	int			bpos = 0;

	for (int i = 0; i < a->nnz; i++)
	{
		int			ai = a->indices[i];

		for (int j = bpos; j < b->nnz; j++)
		{
			int			bi = b->indices[j];

			/* Only update when the same index */
			if (ai == bi)
				distance += ax[i] * bx[j];

			/* Update start for next iteration */
			if (ai >= bi)
				bpos = j + 1;

			/* Found or passed it */
			if (bi >= ai)
				break;
		}
	}

	return distance;
}

/*
 * Get the inner product of two sparse vectors
 */
FUNCTION_PREFIX PG_FUNCTION_INFO_V1(sparsevec_inner_product);
Datum
sparsevec_inner_product(PG_FUNCTION_ARGS)
{
	SparseVector *a = PG_GETARG_SPARSEVEC_P(0);
	SparseVector *b = PG_GETARG_SPARSEVEC_P(1);

	CheckDims(a, b);

	PG_RETURN_FLOAT8((double) SparsevecInnerProduct(a, b));
}

/*
 * Get the negative inner product of two sparse vectors
 */
FUNCTION_PREFIX PG_FUNCTION_INFO_V1(sparsevec_negative_inner_product);
Datum
sparsevec_negative_inner_product(PG_FUNCTION_ARGS)
{
	SparseVector *a = PG_GETARG_SPARSEVEC_P(0);
	SparseVector *b = PG_GETARG_SPARSEVEC_P(1);

	CheckDims(a, b);

	PG_RETURN_FLOAT8((double) -SparsevecInnerProduct(a, b));
}

/*
 * Get the cosine distance between two sparse vectors
 */
FUNCTION_PREFIX PG_FUNCTION_INFO_V1(sparsevec_cosine_distance);
Datum
sparsevec_cosine_distance(PG_FUNCTION_ARGS)
{
	SparseVector *a = PG_GETARG_SPARSEVEC_P(0);
	SparseVector *b = PG_GETARG_SPARSEVEC_P(1);
	float	   *ax = SPARSEVEC_VALUES(a);
	float	   *bx = SPARSEVEC_VALUES(b);
	float		norma = 0.0;
	float		normb = 0.0;
	double		similarity;

	CheckDims(a, b);

	similarity = SparsevecInnerProduct(a, b);

	/* Auto-vectorized */
	for (int i = 0; i < a->nnz; i++)
		norma += ax[i] * ax[i];

	/* Auto-vectorized */
	for (int i = 0; i < b->nnz; i++)
		normb += bx[i] * bx[i];

	/* Use sqrt(a * b) over sqrt(a) * sqrt(b) */
	similarity /= sqrt((double) norma * (double) normb);

#ifdef _MSC_VER
	/* /fp:fast may not propagate NaN */
	if (isnan(similarity))
		PG_RETURN_FLOAT8(NAN);
#endif

	/* Keep in range */
	if (similarity > 1)
		similarity = 1.0;
	else if (similarity < -1)
		similarity = -1.0;

	PG_RETURN_FLOAT8(1.0 - similarity);
}

/*
 * Get the L1 distance between two sparse vectors
 */
FUNCTION_PREFIX PG_FUNCTION_INFO_V1(sparsevec_l1_distance);
Datum
sparsevec_l1_distance(PG_FUNCTION_ARGS)
{
	SparseVector *a = PG_GETARG_SPARSEVEC_P(0);
	SparseVector *b = PG_GETARG_SPARSEVEC_P(1);
	float	   *ax = SPARSEVEC_VALUES(a);
	float	   *bx = SPARSEVEC_VALUES(b);
	float		distance = 0.0;
	int			bpos = 0;

	CheckDims(a, b);

	for (int i = 0; i < a->nnz; i++)
	{
		int			ai = a->indices[i];
		int			bi = -1;

		for (int j = bpos; j < b->nnz; j++)
		{
			bi = b->indices[j];

			if (ai == bi)
				distance += fabsf(ax[i] - bx[j]);
			else if (ai > bi)
				distance += fabsf(bx[j]);

			/* Update start for next iteration */
			if (ai >= bi)
				bpos = j + 1;

			/* Found or passed it */
			if (bi >= ai)
				break;
		}

		if (ai != bi)
			distance += fabsf(ax[i]);
	}

	for (int j = bpos; j < b->nnz; j++)
		distance += fabsf(bx[j]);

	PG_RETURN_FLOAT8((double) distance);
}

/*
 * Get the L2 norm of a sparse vector
 */
FUNCTION_PREFIX PG_FUNCTION_INFO_V1(sparsevec_l2_norm);
Datum
sparsevec_l2_norm(PG_FUNCTION_ARGS)
{
	SparseVector *a = PG_GETARG_SPARSEVEC_P(0);
	float	   *ax = SPARSEVEC_VALUES(a);
	double		norm = 0.0;

	/* Auto-vectorized */
	for (int i = 0; i < a->nnz; i++)
		norm += (double) ax[i] * (double) ax[i];

	PG_RETURN_FLOAT8(sqrt(norm));
}

/*
 * Normalize a sparse vector with the L2 norm
 */
FUNCTION_PREFIX PG_FUNCTION_INFO_V1(sparsevec_l2_normalize);
Datum
sparsevec_l2_normalize(PG_FUNCTION_ARGS)
{
	SparseVector *a = PG_GETARG_SPARSEVEC_P(0);
	float	   *ax = SPARSEVEC_VALUES(a);
	double		norm = 0;
	SparseVector *result;
	float	   *rx;

	result = InitSparseVector(a->dim, a->nnz);
	rx = SPARSEVEC_VALUES(result);

	/* Auto-vectorized */
	for (int i = 0; i < a->nnz; i++)
		norm += (double) ax[i] * (double) ax[i];

	norm = sqrt(norm);

	/* Return zero vector for zero norm */
	if (norm > 0)
	{
		int			zeros = 0;

		for (int i = 0; i < a->nnz; i++)
		{
			result->indices[i] = a->indices[i];
			rx[i] = ax[i] / norm;

			if (isinf(rx[i]))
				float_overflow_error();

			if (rx[i] == 0)
				zeros++;
		}

		/* Allocate a new vector in the unlikely event there are zeros */
		if (zeros > 0)
		{
			SparseVector *newResult = InitSparseVector(result->dim, result->nnz - zeros);
			float	   *nx = SPARSEVEC_VALUES(newResult);
			int			j = 0;

			for (int i = 0; i < result->nnz; i++)
			{
				if (rx[i] == 0)
					continue;

				/* Safety check */
				if (j >= newResult->nnz)
					elog(ERROR, "safety check failed");

				newResult->indices[j] = result->indices[i];
				nx[j] = rx[i];
				j++;
			}

			pfree(result);

			PG_RETURN_POINTER(newResult);
		}
	}

	PG_RETURN_POINTER(result);
}

/*
 * Internal helper to compare sparse vectors
 */
static int
sparsevec_cmp_internal(SparseVector * a, SparseVector * b)
{
	float	   *ax = SPARSEVEC_VALUES(a);
	float	   *bx = SPARSEVEC_VALUES(b);
	int			nnz = Min(a->nnz, b->nnz);

	/* Check values before dimensions to be consistent with Postgres arrays */
	for (int i = 0; i < nnz; i++)
	{
		if (a->indices[i] < b->indices[i])
			return ax[i] < 0 ? -1 : 1;

		if (a->indices[i] > b->indices[i])
			return bx[i] < 0 ? 1 : -1;

		if (ax[i] < bx[i])
			return -1;

		if (ax[i] > bx[i])
			return 1;
	}

	if (a->nnz < b->nnz && b->indices[nnz] < a->dim)
		return bx[nnz] < 0 ? 1 : -1;

	if (a->nnz > b->nnz && a->indices[nnz] < b->dim)
		return ax[nnz] < 0 ? -1 : 1;

	if (a->dim < b->dim)
		return -1;

	if (a->dim > b->dim)
		return 1;

	return 0;
}

/*
 * Less than
 */
FUNCTION_PREFIX PG_FUNCTION_INFO_V1(sparsevec_lt);
Datum
sparsevec_lt(PG_FUNCTION_ARGS)
{
	SparseVector *a = PG_GETARG_SPARSEVEC_P(0);
	SparseVector *b = PG_GETARG_SPARSEVEC_P(1);

	PG_RETURN_BOOL(sparsevec_cmp_internal(a, b) < 0);
}

/*
 * Less than or equal
 */
FUNCTION_PREFIX PG_FUNCTION_INFO_V1(sparsevec_le);
Datum
sparsevec_le(PG_FUNCTION_ARGS)
{
	SparseVector *a = PG_GETARG_SPARSEVEC_P(0);
	SparseVector *b = PG_GETARG_SPARSEVEC_P(1);

	PG_RETURN_BOOL(sparsevec_cmp_internal(a, b) <= 0);
}

/*
 * Equal
 */
FUNCTION_PREFIX PG_FUNCTION_INFO_V1(sparsevec_eq);
Datum
sparsevec_eq(PG_FUNCTION_ARGS)
{
	SparseVector *a = PG_GETARG_SPARSEVEC_P(0);
	SparseVector *b = PG_GETARG_SPARSEVEC_P(1);

	PG_RETURN_BOOL(sparsevec_cmp_internal(a, b) == 0);
}

/*
 * Not equal
 */
FUNCTION_PREFIX PG_FUNCTION_INFO_V1(sparsevec_ne);
Datum
sparsevec_ne(PG_FUNCTION_ARGS)
{
	SparseVector *a = PG_GETARG_SPARSEVEC_P(0);
	SparseVector *b = PG_GETARG_SPARSEVEC_P(1);

	PG_RETURN_BOOL(sparsevec_cmp_internal(a, b) != 0);
}

/*
 * Greater than or equal
 */
FUNCTION_PREFIX PG_FUNCTION_INFO_V1(sparsevec_ge);
Datum
sparsevec_ge(PG_FUNCTION_ARGS)
{
	SparseVector *a = PG_GETARG_SPARSEVEC_P(0);
	SparseVector *b = PG_GETARG_SPARSEVEC_P(1);

	PG_RETURN_BOOL(sparsevec_cmp_internal(a, b) >= 0);
}

/*
 * Greater than
 */
FUNCTION_PREFIX PG_FUNCTION_INFO_V1(sparsevec_gt);
Datum
sparsevec_gt(PG_FUNCTION_ARGS)
{
	SparseVector *a = PG_GETARG_SPARSEVEC_P(0);
	SparseVector *b = PG_GETARG_SPARSEVEC_P(1);

	PG_RETURN_BOOL(sparsevec_cmp_internal(a, b) > 0);
}

/*
 * Compare sparse vectors
 */
FUNCTION_PREFIX PG_FUNCTION_INFO_V1(sparsevec_cmp);
Datum
sparsevec_cmp(PG_FUNCTION_ARGS)
{
	SparseVector *a = PG_GETARG_SPARSEVEC_P(0);
	SparseVector *b = PG_GETARG_SPARSEVEC_P(1);

	PG_RETURN_INT32(sparsevec_cmp_internal(a, b));
}
```

## File: `src/sparsevec.h`
```c
#ifndef SPARSEVEC_H
#define SPARSEVEC_H

#define SPARSEVEC_MAX_DIM 1000000000
#define SPARSEVEC_MAX_NNZ 16000

#define DatumGetSparseVector(x)		((SparseVector *) PG_DETOAST_DATUM(x))
#define PG_GETARG_SPARSEVEC_P(x)	DatumGetSparseVector(PG_GETARG_DATUM(x))
#define PG_RETURN_SPARSEVEC_P(x)	PG_RETURN_POINTER(x)

/*
 * Indices use 0-based numbering for the on-disk (and binary) format (consistent with C)
 * and are always sorted. Values come after indices.
 */
typedef struct SparseVector
{
	int32		vl_len_;		/* varlena header (do not touch directly!) */
	int32		dim;			/* number of dimensions */
	int32		nnz;			/* number of non-zero elements */
	int32		unused;			/* reserved for future use, always zero */
	int32		indices[FLEXIBLE_ARRAY_MEMBER];
}			SparseVector;

/* Use functions instead of macros to avoid double evaluation */

static inline Size
SPARSEVEC_SIZE(int nnz)
{
	return offsetof(SparseVector, indices) + (nnz * sizeof(int32)) + (nnz * sizeof(float));
}

static inline float *
SPARSEVEC_VALUES(SparseVector * x)
{
	return (float *) (((char *) x) + offsetof(SparseVector, indices) + (x->nnz * sizeof(int32)));
}

SparseVector *InitSparseVector(int dim, int nnz);

#endif
```

## File: `src/vector.c`
```c
#include "postgres.h"

#include <math.h>

#include "bitutils.h"
#include "bitvec.h"
#include "catalog/pg_type.h"
#include "common/shortest_dec.h"
#include "fmgr.h"
#include "halfutils.h"
#include "halfvec.h"
#include "hnsw.h"
#include "ivfflat.h"
#include "lib/stringinfo.h"
#include "libpq/pqformat.h"
#include "port.h"				/* for strtof() */
#include "sparsevec.h"
#include "utils/array.h"
#include "utils/float.h"
#include "utils/fmgrprotos.h"
#include "utils/lsyscache.h"
#include "utils/varbit.h"
#include "vector.h"

#if PG_VERSION_NUM >= 160000
#include "varatt.h"
#endif

#if PG_VERSION_NUM >= 170000
#include "parser/scansup.h"
#endif

#define STATE_DIMS(x) (ARR_DIMS(x)[0] - 1)
#define CreateStateDatums(dim) palloc(sizeof(Datum) * (dim + 1))

#if defined(USE_TARGET_CLONES) && !defined(__FMA__)
#define VECTOR_TARGET_CLONES __attribute__((target_clones("default", "fma")))
#else
#define VECTOR_TARGET_CLONES
#endif

#if PG_VERSION_NUM >= 180000
PG_MODULE_MAGIC_EXT(.name = "vector",.version = "0.8.2");
#else
PG_MODULE_MAGIC;
#endif

/*
 * Initialize index options and variables
 */
PGDLLEXPORT void _PG_init(void);
void
_PG_init(void)
{
	BitvecInit();
	HalfvecInit();
	HnswInit();
	IvfflatInit();
}

/*
 * Ensure same dimensions
 */
static inline void
CheckDims(Vector * a, Vector * b)
{
	if (a->dim != b->dim)
		ereport(ERROR,
				(errcode(ERRCODE_DATA_EXCEPTION),
				 errmsg("different vector dimensions %d and %d", a->dim, b->dim)));
}

/*
 * Ensure expected dimensions
 */
static inline void
CheckExpectedDim(int32 typmod, int dim)
{
	if (typmod != -1 && typmod != dim)
		ereport(ERROR,
				(errcode(ERRCODE_DATA_EXCEPTION),
				 errmsg("expected %d dimensions, not %d", typmod, dim)));
}

/*
 * Ensure valid dimensions
 */
static inline void
CheckDim(int dim)
{
	if (dim < 1)
		ereport(ERROR,
				(errcode(ERRCODE_DATA_EXCEPTION),
				 errmsg("vector must have at least 1 dimension")));

	if (dim > VECTOR_MAX_DIM)
		ereport(ERROR,
				(errcode(ERRCODE_PROGRAM_LIMIT_EXCEEDED),
				 errmsg("vector cannot have more than %d dimensions", VECTOR_MAX_DIM)));
}

/*
 * Ensure finite element
 */
static inline void
CheckElement(float value)
{
	if (isnan(value))
		ereport(ERROR,
				(errcode(ERRCODE_DATA_EXCEPTION),
				 errmsg("NaN not allowed in vector")));

	if (isinf(value))
		ereport(ERROR,
				(errcode(ERRCODE_DATA_EXCEPTION),
				 errmsg("infinite value not allowed in vector")));
}

/*
 * Allocate and initialize a new vector
 */
Vector *
InitVector(int dim)
{
	Vector	   *result;
	int			size;

	size = VECTOR_SIZE(dim);
	result = (Vector *) palloc0(size);
	SET_VARSIZE(result, size);
	result->dim = dim;

	return result;
}

#if PG_VERSION_NUM >= 170000
#define vector_isspace(ch) scanner_isspace(ch)
#else
static inline bool
vector_isspace(char ch)
{
	if (ch == ' ' ||
		ch == '\t' ||
		ch == '\n' ||
		ch == '\r' ||
		ch == '\v' ||
		ch == '\f')
		return true;
	return false;
}
#endif

/*
 * Check state array
 */
static float8 *
CheckStateArray(ArrayType *statearray, const char *caller)
{
	if (ARR_NDIM(statearray) != 1 ||
		ARR_DIMS(statearray)[0] < 1 ||
		ARR_HASNULL(statearray) ||
		ARR_ELEMTYPE(statearray) != FLOAT8OID)
		elog(ERROR, "%s: expected state array", caller);
	return (float8 *) ARR_DATA_PTR(statearray);
}

/*
 * Convert textual representation to internal representation
 */
FUNCTION_PREFIX PG_FUNCTION_INFO_V1(vector_in);
Datum
vector_in(PG_FUNCTION_ARGS)
{
	char	   *lit = PG_GETARG_CSTRING(0);
	int32		typmod = PG_GETARG_INT32(2);
	float		x[VECTOR_MAX_DIM];
	int			dim = 0;
	char	   *pt = lit;
	Vector	   *result;

	while (vector_isspace(*pt))
		pt++;

	if (*pt != '[')
		ereport(ERROR,
				(errcode(ERRCODE_INVALID_TEXT_REPRESENTATION),
				 errmsg("invalid input syntax for type vector: \"%s\"", lit),
				 errdetail("Vector contents must start with \"[\".")));

	pt++;

	while (vector_isspace(*pt))
		pt++;

	if (*pt == ']')
		ereport(ERROR,
				(errcode(ERRCODE_DATA_EXCEPTION),
				 errmsg("vector must have at least 1 dimension")));

	for (;;)
	{
		float		val;
		char	   *stringEnd;

		if (dim == VECTOR_MAX_DIM)
			ereport(ERROR,
					(errcode(ERRCODE_PROGRAM_LIMIT_EXCEEDED),
					 errmsg("vector cannot have more than %d dimensions", VECTOR_MAX_DIM)));

		while (vector_isspace(*pt))
			pt++;

		/* Check for empty string like float4in */
		if (*pt == '\0')
			ereport(ERROR,
					(errcode(ERRCODE_INVALID_TEXT_REPRESENTATION),
					 errmsg("invalid input syntax for type vector: \"%s\"", lit)));

		errno = 0;

		/* Use strtof like float4in to avoid a double-rounding problem */
		/* Postgres sets LC_NUMERIC to C on startup */
		val = strtof(pt, &stringEnd);

		if (stringEnd == pt)
			ereport(ERROR,
					(errcode(ERRCODE_INVALID_TEXT_REPRESENTATION),
					 errmsg("invalid input syntax for type vector: \"%s\"", lit)));

		/* Check for range error like float4in */
		if (errno == ERANGE && isinf(val))
			ereport(ERROR,
					(errcode(ERRCODE_NUMERIC_VALUE_OUT_OF_RANGE),
					 errmsg("\"%s\" is out of range for type vector", pnstrdup(pt, stringEnd - pt))));

		CheckElement(val);
		x[dim++] = val;

		pt = stringEnd;

		while (vector_isspace(*pt))
			pt++;

		if (*pt == ',')
			pt++;
		else if (*pt == ']')
		{
			pt++;
			break;
		}
		else
			ereport(ERROR,
					(errcode(ERRCODE_INVALID_TEXT_REPRESENTATION),
					 errmsg("invalid input syntax for type vector: \"%s\"", lit)));
	}

	/* Only whitespace is allowed after the closing brace */
	while (vector_isspace(*pt))
		pt++;

	if (*pt != '\0')
		ereport(ERROR,
				(errcode(ERRCODE_INVALID_TEXT_REPRESENTATION),
				 errmsg("invalid input syntax for type vector: \"%s\"", lit),
				 errdetail("Junk after closing right brace.")));

	CheckDim(dim);
	CheckExpectedDim(typmod, dim);

	result = InitVector(dim);
	for (int i = 0; i < dim; i++)
		result->x[i] = x[i];

	PG_RETURN_POINTER(result);
}

#define AppendChar(ptr, c) (*(ptr)++ = (c))
#define AppendFloat(ptr, f) ((ptr) += float_to_shortest_decimal_bufn((f), (ptr)))

/*
 * Convert internal representation to textual representation
 */
FUNCTION_PREFIX PG_FUNCTION_INFO_V1(vector_out);
Datum
vector_out(PG_FUNCTION_ARGS)
{
	Vector	   *vector = PG_GETARG_VECTOR_P(0);
	int			dim = vector->dim;
	char	   *buf;
	char	   *ptr;

	/*
	 * Need:
	 *
	 * dim * (FLOAT_SHORTEST_DECIMAL_LEN - 1) bytes for
	 * float_to_shortest_decimal_bufn
	 *
	 * dim - 1 bytes for separator
	 *
	 * 3 bytes for [, ], and \0
	 */
	buf = (char *) palloc(FLOAT_SHORTEST_DECIMAL_LEN * dim + 2);
	ptr = buf;

	AppendChar(ptr, '[');

	for (int i = 0; i < dim; i++)
	{
		if (i > 0)
			AppendChar(ptr, ',');

		AppendFloat(ptr, vector->x[i]);
	}

	AppendChar(ptr, ']');
	*ptr = '\0';

	PG_FREE_IF_COPY(vector, 0);
	PG_RETURN_CSTRING(buf);
}

/*
 * Print vector - useful for debugging
 */
void
PrintVector(char *msg, Vector * vector)
{
	char	   *out = DatumGetPointer(DirectFunctionCall1(vector_out, PointerGetDatum(vector)));

	elog(INFO, "%s = %s", msg, out);
	pfree(out);
}

/*
 * Convert type modifier
 */
FUNCTION_PREFIX PG_FUNCTION_INFO_V1(vector_typmod_in);
Datum
vector_typmod_in(PG_FUNCTION_ARGS)
{
	ArrayType  *ta = PG_GETARG_ARRAYTYPE_P(0);
	int32	   *tl;
	int			n;

	tl = ArrayGetIntegerTypmods(ta, &n);

	if (n != 1)
		ereport(ERROR,
				(errcode(ERRCODE_INVALID_PARAMETER_VALUE),
				 errmsg("invalid type modifier")));

	if (*tl < 1)
		ereport(ERROR,
				(errcode(ERRCODE_INVALID_PARAMETER_VALUE),
				 errmsg("dimensions for type vector must be at least 1")));

	if (*tl > VECTOR_MAX_DIM)
		ereport(ERROR,
				(errcode(ERRCODE_INVALID_PARAMETER_VALUE),
				 errmsg("dimensions for type vector cannot exceed %d", VECTOR_MAX_DIM)));

	PG_RETURN_INT32(*tl);
}

/*
 * Convert external binary representation to internal representation
 */
FUNCTION_PREFIX PG_FUNCTION_INFO_V1(vector_recv);
Datum
vector_recv(PG_FUNCTION_ARGS)
{
	StringInfo	buf = (StringInfo) PG_GETARG_POINTER(0);
	int32		typmod = PG_GETARG_INT32(2);
	Vector	   *result;
	int16		dim;
	int16		unused;

	dim = pq_getmsgint(buf, sizeof(int16));
	unused = pq_getmsgint(buf, sizeof(int16));

	CheckDim(dim);
	CheckExpectedDim(typmod, dim);

	if (unused != 0)
		ereport(ERROR,
				(errcode(ERRCODE_DATA_EXCEPTION),
				 errmsg("expected unused to be 0, not %d", unused)));

	result = InitVector(dim);
	for (int i = 0; i < dim; i++)
	{
		result->x[i] = pq_getmsgfloat4(buf);
		CheckElement(result->x[i]);
	}

	PG_RETURN_POINTER(result);
}

/*
 * Convert internal representation to the external binary representation
 */
FUNCTION_PREFIX PG_FUNCTION_INFO_V1(vector_send);
Datum
vector_send(PG_FUNCTION_ARGS)
{
	Vector	   *vec = PG_GETARG_VECTOR_P(0);
	StringInfoData buf;

	pq_begintypsend(&buf);
	pq_sendint(&buf, vec->dim, sizeof(int16));
	pq_sendint(&buf, vec->unused, sizeof(int16));
	for (int i = 0; i < vec->dim; i++)
		pq_sendfloat4(&buf, vec->x[i]);

	PG_RETURN_BYTEA_P(pq_endtypsend(&buf));
}

/*
 * Convert vector to vector
 * This is needed to check the type modifier
 */
FUNCTION_PREFIX PG_FUNCTION_INFO_V1(vector);
Datum
vector(PG_FUNCTION_ARGS)
{
	Vector	   *vec = PG_GETARG_VECTOR_P(0);
	int32		typmod = PG_GETARG_INT32(1);

	CheckExpectedDim(typmod, vec->dim);

	PG_RETURN_POINTER(vec);
}

/*
 * Convert array to vector
 */
FUNCTION_PREFIX PG_FUNCTION_INFO_V1(array_to_vector);
Datum
array_to_vector(PG_FUNCTION_ARGS)
{
	ArrayType  *array = PG_GETARG_ARRAYTYPE_P(0);
	int32		typmod = PG_GETARG_INT32(1);
	Vector	   *result;
	int16		typlen;
	bool		typbyval;
	char		typalign;
	Datum	   *elemsp;
	int			nelemsp;

	if (ARR_NDIM(array) > 1)
		ereport(ERROR,
				(errcode(ERRCODE_DATA_EXCEPTION),
				 errmsg("array must be 1-D")));

	if (ARR_HASNULL(array) && array_contains_nulls(array))
		ereport(ERROR,
				(errcode(ERRCODE_NULL_VALUE_NOT_ALLOWED),
				 errmsg("array must not contain nulls")));

	get_typlenbyvalalign(ARR_ELEMTYPE(array), &typlen, &typbyval, &typalign);
	deconstruct_array(array, ARR_ELEMTYPE(array), typlen, typbyval, typalign, &elemsp, NULL, &nelemsp);

	CheckDim(nelemsp);
	CheckExpectedDim(typmod, nelemsp);

	result = InitVector(nelemsp);

	if (ARR_ELEMTYPE(array) == INT4OID)
	{
		for (int i = 0; i < nelemsp; i++)
			result->x[i] = DatumGetInt32(elemsp[i]);
	}
	else if (ARR_ELEMTYPE(array) == FLOAT8OID)
	{
		for (int i = 0; i < nelemsp; i++)
			result->x[i] = DatumGetFloat8(elemsp[i]);
	}
	else if (ARR_ELEMTYPE(array) == FLOAT4OID)
	{
		for (int i = 0; i < nelemsp; i++)
			result->x[i] = DatumGetFloat4(elemsp[i]);
	}
	else if (ARR_ELEMTYPE(array) == NUMERICOID)
	{
		for (int i = 0; i < nelemsp; i++)
			result->x[i] = DatumGetFloat4(DirectFunctionCall1(numeric_float4, elemsp[i]));
	}
	else
	{
		ereport(ERROR,
				(errcode(ERRCODE_DATA_EXCEPTION),
				 errmsg("unsupported array type")));
	}

	/*
	 * Free allocation from deconstruct_array. Do not free individual elements
	 * when pass-by-reference since they point to original array.
	 */
	pfree(elemsp);

	/* Check elements */
	for (int i = 0; i < result->dim; i++)
		CheckElement(result->x[i]);

	PG_RETURN_POINTER(result);
}

/*
 * Convert vector to float4[]
 */
FUNCTION_PREFIX PG_FUNCTION_INFO_V1(vector_to_float4);
Datum
vector_to_float4(PG_FUNCTION_ARGS)
{
	Vector	   *vec = PG_GETARG_VECTOR_P(0);
	Datum	   *datums;
	ArrayType  *result;

	datums = (Datum *) palloc(sizeof(Datum) * vec->dim);

	for (int i = 0; i < vec->dim; i++)
		datums[i] = Float4GetDatum(vec->x[i]);

	/* Use TYPALIGN_INT for float4 */
	result = construct_array(datums, vec->dim, FLOAT4OID, sizeof(float4), true, TYPALIGN_INT);

	pfree(datums);

	PG_RETURN_POINTER(result);
}

/*
 * Convert half vector to vector
 */
FUNCTION_PREFIX PG_FUNCTION_INFO_V1(halfvec_to_vector);
Datum
halfvec_to_vector(PG_FUNCTION_ARGS)
{
	HalfVector *vec = PG_GETARG_HALFVEC_P(0);
	int32		typmod = PG_GETARG_INT32(1);
	Vector	   *result;

	CheckDim(vec->dim);
	CheckExpectedDim(typmod, vec->dim);

	result = InitVector(vec->dim);

	for (int i = 0; i < vec->dim; i++)
		result->x[i] = HalfToFloat4(vec->x[i]);

	PG_RETURN_POINTER(result);
}

VECTOR_TARGET_CLONES static float
VectorL2SquaredDistance(int dim, float *ax, float *bx)
{
	float		distance = 0.0;

	/* Auto-vectorized */
	for (int i = 0; i < dim; i++)
	{
		float		diff = ax[i] - bx[i];

		distance += diff * diff;
	}

	return distance;
}

/*
 * Get the L2 distance between vectors
 */
FUNCTION_PREFIX PG_FUNCTION_INFO_V1(l2_distance);
Datum
l2_distance(PG_FUNCTION_ARGS)
{
	Vector	   *a = PG_GETARG_VECTOR_P(0);
	Vector	   *b = PG_GETARG_VECTOR_P(1);

	CheckDims(a, b);

	PG_RETURN_FLOAT8(sqrt((double) VectorL2SquaredDistance(a->dim, a->x, b->x)));
}

/*
 * Get the L2 squared distance between vectors
 * This saves a sqrt calculation
 */
FUNCTION_PREFIX PG_FUNCTION_INFO_V1(vector_l2_squared_distance);
Datum
vector_l2_squared_distance(PG_FUNCTION_ARGS)
{
	Vector	   *a = PG_GETARG_VECTOR_P(0);
	Vector	   *b = PG_GETARG_VECTOR_P(1);

	CheckDims(a, b);

	PG_RETURN_FLOAT8((double) VectorL2SquaredDistance(a->dim, a->x, b->x));
}

VECTOR_TARGET_CLONES static float
VectorInnerProduct(int dim, float *ax, float *bx)
{
	float		distance = 0.0;

	/* Auto-vectorized */
	for (int i = 0; i < dim; i++)
		distance += ax[i] * bx[i];

	return distance;
}

/*
 * Get the inner product of two vectors
 */
FUNCTION_PREFIX PG_FUNCTION_INFO_V1(inner_product);
Datum
inner_product(PG_FUNCTION_ARGS)
{
	Vector	   *a = PG_GETARG_VECTOR_P(0);
	Vector	   *b = PG_GETARG_VECTOR_P(1);

	CheckDims(a, b);

	PG_RETURN_FLOAT8((double) VectorInnerProduct(a->dim, a->x, b->x));
}

/*
 * Get the negative inner product of two vectors
 */
FUNCTION_PREFIX PG_FUNCTION_INFO_V1(vector_negative_inner_product);
Datum
vector_negative_inner_product(PG_FUNCTION_ARGS)
{
	Vector	   *a = PG_GETARG_VECTOR_P(0);
	Vector	   *b = PG_GETARG_VECTOR_P(1);

	CheckDims(a, b);

	PG_RETURN_FLOAT8((double) -VectorInnerProduct(a->dim, a->x, b->x));
}

VECTOR_TARGET_CLONES static double
VectorCosineSimilarity(int dim, float *ax, float *bx)
{
	float		similarity = 0.0;
	float		norma = 0.0;
	float		normb = 0.0;

	/* Auto-vectorized */
	for (int i = 0; i < dim; i++)
	{
		similarity += ax[i] * bx[i];
		norma += ax[i] * ax[i];
		normb += bx[i] * bx[i];
	}

	/* Use sqrt(a * b) over sqrt(a) * sqrt(b) */
	return (double) similarity / sqrt((double) norma * (double) normb);
}

/*
 * Get the cosine distance between two vectors
 */
FUNCTION_PREFIX PG_FUNCTION_INFO_V1(cosine_distance);
Datum
cosine_distance(PG_FUNCTION_ARGS)
{
	Vector	   *a = PG_GETARG_VECTOR_P(0);
	Vector	   *b = PG_GETARG_VECTOR_P(1);
	double		similarity;

	CheckDims(a, b);

	similarity = VectorCosineSimilarity(a->dim, a->x, b->x);

#ifdef _MSC_VER
	/* /fp:fast may not propagate NaN */
	if (isnan(similarity))
		PG_RETURN_FLOAT8(NAN);
#endif

	/* Keep in range */
	if (similarity > 1)
		similarity = 1.0;
	else if (similarity < -1)
		similarity = -1.0;

	PG_RETURN_FLOAT8(1.0 - similarity);
}

/*
 * Get the distance for spherical k-means
 * Currently uses angular distance since needs to satisfy triangle inequality
 * Assumes inputs are unit vectors (skips norm)
 */
FUNCTION_PREFIX PG_FUNCTION_INFO_V1(vector_spherical_distance);
Datum
vector_spherical_distance(PG_FUNCTION_ARGS)
{
	Vector	   *a = PG_GETARG_VECTOR_P(0);
	Vector	   *b = PG_GETARG_VECTOR_P(1);
	double		distance;

	CheckDims(a, b);

	distance = (double) VectorInnerProduct(a->dim, a->x, b->x);

	/* Prevent NaN with acos with loss of precision */
	if (distance > 1)
		distance = 1;
	else if (distance < -1)
		distance = -1;

	PG_RETURN_FLOAT8(acos(distance) / M_PI);
}

/* Does not require FMA, but keep logic simple */
VECTOR_TARGET_CLONES static float
VectorL1Distance(int dim, float *ax, float *bx)
{
	float		distance = 0.0;

	/* Auto-vectorized */
	for (int i = 0; i < dim; i++)
		distance += fabsf(ax[i] - bx[i]);

	return distance;
}

/*
 * Get the L1 distance between two vectors
 */
FUNCTION_PREFIX PG_FUNCTION_INFO_V1(l1_distance);
Datum
l1_distance(PG_FUNCTION_ARGS)
{
	Vector	   *a = PG_GETARG_VECTOR_P(0);
	Vector	   *b = PG_GETARG_VECTOR_P(1);

	CheckDims(a, b);

	PG_RETURN_FLOAT8((double) VectorL1Distance(a->dim, a->x, b->x));
}

/*
 * Get the dimensions of a vector
 */
FUNCTION_PREFIX PG_FUNCTION_INFO_V1(vector_dims);
Datum
vector_dims(PG_FUNCTION_ARGS)
{
	Vector	   *a = PG_GETARG_VECTOR_P(0);

	PG_RETURN_INT32(a->dim);
}

/*
 * Get the L2 norm of a vector
 */
FUNCTION_PREFIX PG_FUNCTION_INFO_V1(vector_norm);
Datum
vector_norm(PG_FUNCTION_ARGS)
{
	Vector	   *a = PG_GETARG_VECTOR_P(0);
	float	   *ax = a->x;
	double		norm = 0.0;

	/* Auto-vectorized */
	for (int i = 0; i < a->dim; i++)
		norm += (double) ax[i] * (double) ax[i];

	PG_RETURN_FLOAT8(sqrt(norm));
}

/*
 * Normalize a vector with the L2 norm
 */
FUNCTION_PREFIX PG_FUNCTION_INFO_V1(l2_normalize);
Datum
l2_normalize(PG_FUNCTION_ARGS)
{
	Vector	   *a = PG_GETARG_VECTOR_P(0);
	float	   *ax = a->x;
	double		norm = 0;
	Vector	   *result;
	float	   *rx;

	result = InitVector(a->dim);
	rx = result->x;

	/* Auto-vectorized */
	for (int i = 0; i < a->dim; i++)
		norm += (double) ax[i] * (double) ax[i];

	norm = sqrt(norm);

	/* Return zero vector for zero norm */
	if (norm > 0)
	{
		for (int i = 0; i < a->dim; i++)
			rx[i] = ax[i] / norm;

		/* Check for overflow */
		for (int i = 0; i < a->dim; i++)
		{
			if (isinf(rx[i]))
				float_overflow_error();
		}
	}

	PG_RETURN_POINTER(result);
}

/*
 * Add vectors
 */
FUNCTION_PREFIX PG_FUNCTION_INFO_V1(vector_add);
Datum
vector_add(PG_FUNCTION_ARGS)
{
	Vector	   *a = PG_GETARG_VECTOR_P(0);
	Vector	   *b = PG_GETARG_VECTOR_P(1);
	float	   *ax = a->x;
	float	   *bx = b->x;
	Vector	   *result;
	float	   *rx;

	CheckDims(a, b);

	result = InitVector(a->dim);
	rx = result->x;

	/* Auto-vectorized */
	for (int i = 0, imax = a->dim; i < imax; i++)
		rx[i] = ax[i] + bx[i];

	/* Check for overflow */
	for (int i = 0, imax = a->dim; i < imax; i++)
	{
		if (isinf(rx[i]))
			float_overflow_error();
	}

	PG_RETURN_POINTER(result);
}

/*
 * Subtract vectors
 */
FUNCTION_PREFIX PG_FUNCTION_INFO_V1(vector_sub);
Datum
vector_sub(PG_FUNCTION_ARGS)
{
	Vector	   *a = PG_GETARG_VECTOR_P(0);
	Vector	   *b = PG_GETARG_VECTOR_P(1);
	float	   *ax = a->x;
	float	   *bx = b->x;
	Vector	   *result;
	float	   *rx;

	CheckDims(a, b);

	result = InitVector(a->dim);
	rx = result->x;

	/* Auto-vectorized */
	for (int i = 0, imax = a->dim; i < imax; i++)
		rx[i] = ax[i] - bx[i];

	/* Check for overflow */
	for (int i = 0, imax = a->dim; i < imax; i++)
	{
		if (isinf(rx[i]))
			float_overflow_error();
	}

	PG_RETURN_POINTER(result);
}

/*
 * Multiply vectors
 */
FUNCTION_PREFIX PG_FUNCTION_INFO_V1(vector_mul);
Datum
vector_mul(PG_FUNCTION_ARGS)
{
	Vector	   *a = PG_GETARG_VECTOR_P(0);
	Vector	   *b = PG_GETARG_VECTOR_P(1);
	float	   *ax = a->x;
	float	   *bx = b->x;
	Vector	   *result;
	float	   *rx;

	CheckDims(a, b);

	result = InitVector(a->dim);
	rx = result->x;

	/* Auto-vectorized */
	for (int i = 0, imax = a->dim; i < imax; i++)
		rx[i] = ax[i] * bx[i];

	/* Check for overflow and underflow */
	for (int i = 0, imax = a->dim; i < imax; i++)
	{
		if (isinf(rx[i]))
			float_overflow_error();

		if (rx[i] == 0 && !(ax[i] == 0 || bx[i] == 0))
			float_underflow_error();
	}

	PG_RETURN_POINTER(result);
}

/*
 * Concatenate vectors
 */
FUNCTION_PREFIX PG_FUNCTION_INFO_V1(vector_concat);
Datum
vector_concat(PG_FUNCTION_ARGS)
{
	Vector	   *a = PG_GETARG_VECTOR_P(0);
	Vector	   *b = PG_GETARG_VECTOR_P(1);
	Vector	   *result;
	int			dim = a->dim + b->dim;

	CheckDim(dim);
	result = InitVector(dim);

	/* Auto-vectorized */
	for (int i = 0, imax = a->dim; i < imax; i++)
		result->x[i] = a->x[i];

	/* Auto-vectorized */
	for (int i = 0, imax = b->dim, start = a->dim; i < imax; i++)
		result->x[i + start] = b->x[i];

	PG_RETURN_POINTER(result);
}

/*
 * Quantize a vector
 */
FUNCTION_PREFIX PG_FUNCTION_INFO_V1(binary_quantize);
Datum
binary_quantize(PG_FUNCTION_ARGS)
{
	Vector	   *a = PG_GETARG_VECTOR_P(0);
	float	   *ax = a->x;
	VarBit	   *result = InitBitVector(a->dim);
	unsigned char *rx = VARBITS(result);
	int			i = 0;
	int			count = (a->dim / 8) * 8;

	/* Auto-vectorized */
	for (; i < count; i += 8)
	{
		unsigned char result_byte = 0;

		for (int j = 0; j < 8; j++)
			result_byte |= (ax[i + j] > 0) << (7 - j);

		rx[i / 8] = result_byte;
	}

	for (; i < a->dim; i++)
		rx[i / 8] |= (ax[i] > 0) << (7 - (i % 8));

	PG_RETURN_VARBIT_P(result);
}

/*
 * Get a subvector
 */
FUNCTION_PREFIX PG_FUNCTION_INFO_V1(subvector);
Datum
subvector(PG_FUNCTION_ARGS)
{
	Vector	   *a = PG_GETARG_VECTOR_P(0);
	int32		start = PG_GETARG_INT32(1);
	int32		count = PG_GETARG_INT32(2);
	int32		end;
	float	   *ax = a->x;
	Vector	   *result;
	int			dim;

	if (count < 1)
		ereport(ERROR,
				(errcode(ERRCODE_DATA_EXCEPTION),
				 errmsg("vector must have at least 1 dimension")));

	/*
	 * Check if (start + count > a->dim), avoiding integer overflow. a->dim
	 * and count are both positive, so a->dim - count won't overflow.
	 */
	if (start > a->dim - count)
		end = a->dim + 1;
	else
		end = start + count;

	/* Indexing starts at 1, like substring */
	if (start < 1)
		start = 1;
	else if (start > a->dim)
		ereport(ERROR,
				(errcode(ERRCODE_DATA_EXCEPTION),
				 errmsg("vector must have at least 1 dimension")));

	dim = end - start;
	CheckDim(dim);
	result = InitVector(dim);

	for (int i = 0; i < dim; i++)
		result->x[i] = ax[start - 1 + i];

	PG_RETURN_POINTER(result);
}

/*
 * Internal helper to compare vectors
 */
int
vector_cmp_internal(Vector * a, Vector * b)
{
	int			dim = Min(a->dim, b->dim);

	/* Check values before dimensions to be consistent with Postgres arrays */
	for (int i = 0; i < dim; i++)
	{
		if (a->x[i] < b->x[i])
			return -1;

		if (a->x[i] > b->x[i])
			return 1;
	}

	if (a->dim < b->dim)
		return -1;

	if (a->dim > b->dim)
		return 1;

	return 0;
}

/*
 * Less than
 */
FUNCTION_PREFIX PG_FUNCTION_INFO_V1(vector_lt);
Datum
vector_lt(PG_FUNCTION_ARGS)
{
	Vector	   *a = PG_GETARG_VECTOR_P(0);
	Vector	   *b = PG_GETARG_VECTOR_P(1);

	PG_RETURN_BOOL(vector_cmp_internal(a, b) < 0);
}

/*
 * Less than or equal
 */
FUNCTION_PREFIX PG_FUNCTION_INFO_V1(vector_le);
Datum
vector_le(PG_FUNCTION_ARGS)
{
	Vector	   *a = PG_GETARG_VECTOR_P(0);
	Vector	   *b = PG_GETARG_VECTOR_P(1);

	PG_RETURN_BOOL(vector_cmp_internal(a, b) <= 0);
}

/*
 * Equal
 */
FUNCTION_PREFIX PG_FUNCTION_INFO_V1(vector_eq);
Datum
vector_eq(PG_FUNCTION_ARGS)
{
	Vector	   *a = PG_GETARG_VECTOR_P(0);
	Vector	   *b = PG_GETARG_VECTOR_P(1);

	PG_RETURN_BOOL(vector_cmp_internal(a, b) == 0);
}

/*
 * Not equal
 */
FUNCTION_PREFIX PG_FUNCTION_INFO_V1(vector_ne);
Datum
vector_ne(PG_FUNCTION_ARGS)
{
	Vector	   *a = PG_GETARG_VECTOR_P(0);
	Vector	   *b = PG_GETARG_VECTOR_P(1);

	PG_RETURN_BOOL(vector_cmp_internal(a, b) != 0);
}

/*
 * Greater than or equal
 */
FUNCTION_PREFIX PG_FUNCTION_INFO_V1(vector_ge);
Datum
vector_ge(PG_FUNCTION_ARGS)
{
	Vector	   *a = PG_GETARG_VECTOR_P(0);
	Vector	   *b = PG_GETARG_VECTOR_P(1);

	PG_RETURN_BOOL(vector_cmp_internal(a, b) >= 0);
}

/*
 * Greater than
 */
FUNCTION_PREFIX PG_FUNCTION_INFO_V1(vector_gt);
Datum
vector_gt(PG_FUNCTION_ARGS)
{
	Vector	   *a = PG_GETARG_VECTOR_P(0);
	Vector	   *b = PG_GETARG_VECTOR_P(1);

	PG_RETURN_BOOL(vector_cmp_internal(a, b) > 0);
}

/*
 * Compare vectors
 */
FUNCTION_PREFIX PG_FUNCTION_INFO_V1(vector_cmp);
Datum
vector_cmp(PG_FUNCTION_ARGS)
{
	Vector	   *a = PG_GETARG_VECTOR_P(0);
	Vector	   *b = PG_GETARG_VECTOR_P(1);

	PG_RETURN_INT32(vector_cmp_internal(a, b));
}

/*
 * Accumulate vectors
 */
FUNCTION_PREFIX PG_FUNCTION_INFO_V1(vector_accum);
Datum
vector_accum(PG_FUNCTION_ARGS)
{
	ArrayType  *statearray = PG_GETARG_ARRAYTYPE_P(0);
	Vector	   *newval = PG_GETARG_VECTOR_P(1);
	float8	   *statevalues;
	int16		dim;
	bool		newarr;
	float8		n;
	Datum	   *statedatums;
	float	   *x = newval->x;
	ArrayType  *result;

	/* Check array before using */
	statevalues = CheckStateArray(statearray, "vector_accum");
	dim = STATE_DIMS(statearray);
	newarr = dim == 0;

	if (newarr)
		dim = newval->dim;
	else
		CheckExpectedDim(dim, newval->dim);

	n = statevalues[0] + 1.0;

	statedatums = CreateStateDatums(dim);
	statedatums[0] = Float8GetDatum(n);

	if (newarr)
	{
		for (int i = 0; i < dim; i++)
			statedatums[i + 1] = Float8GetDatum((double) x[i]);
	}
	else
	{
		for (int i = 0; i < dim; i++)
		{
			double		v = statevalues[i + 1] + x[i];

			/* Check for overflow */
			if (isinf(v))
				float_overflow_error();

			statedatums[i + 1] = Float8GetDatum(v);
		}
	}

	/* Use float8 array like float4_accum */
	result = construct_array(statedatums, dim + 1,
							 FLOAT8OID,
							 sizeof(float8), FLOAT8PASSBYVAL, TYPALIGN_DOUBLE);

	pfree(statedatums);

	PG_RETURN_ARRAYTYPE_P(result);
}

/*
 * Combine vectors or half vectors (also used for halfvec_combine)
 */
FUNCTION_PREFIX PG_FUNCTION_INFO_V1(vector_combine);
Datum
vector_combine(PG_FUNCTION_ARGS)
{
	/* Must also update parameters of halfvec_combine if modifying */
	ArrayType  *statearray1 = PG_GETARG_ARRAYTYPE_P(0);
	ArrayType  *statearray2 = PG_GETARG_ARRAYTYPE_P(1);
	float8	   *statevalues1;
	float8	   *statevalues2;
	float8		n;
	float8		n1;
	float8		n2;
	int16		dim;
	Datum	   *statedatums;
	ArrayType  *result;

	/* Check arrays before using */
	statevalues1 = CheckStateArray(statearray1, "vector_combine");
	statevalues2 = CheckStateArray(statearray2, "vector_combine");

	n1 = statevalues1[0];
	n2 = statevalues2[0];

	if (n1 == 0.0)
	{
		n = n2;
		dim = STATE_DIMS(statearray2);
		statedatums = CreateStateDatums(dim);
		for (int i = 1; i <= dim; i++)
			statedatums[i] = Float8GetDatum(statevalues2[i]);
	}
	else if (n2 == 0.0)
	{
		n = n1;
		dim = STATE_DIMS(statearray1);
		statedatums = CreateStateDatums(dim);
		for (int i = 1; i <= dim; i++)
			statedatums[i] = Float8GetDatum(statevalues1[i]);
	}
	else
	{
		n = n1 + n2;
		dim = STATE_DIMS(statearray1);
		CheckExpectedDim(dim, STATE_DIMS(statearray2));
		statedatums = CreateStateDatums(dim);
		for (int i = 1; i <= dim; i++)
		{
			double		v = statevalues1[i] + statevalues2[i];

			/* Check for overflow */
			if (isinf(v))
				float_overflow_error();

			statedatums[i] = Float8GetDatum(v);
		}
	}

	statedatums[0] = Float8GetDatum(n);

	result = construct_array(statedatums, dim + 1,
							 FLOAT8OID,
							 sizeof(float8), FLOAT8PASSBYVAL, TYPALIGN_DOUBLE);

	pfree(statedatums);

	PG_RETURN_ARRAYTYPE_P(result);
}

/*
 * Average vectors
 */
FUNCTION_PREFIX PG_FUNCTION_INFO_V1(vector_avg);
Datum
vector_avg(PG_FUNCTION_ARGS)
{
	ArrayType  *statearray = PG_GETARG_ARRAYTYPE_P(0);
	float8	   *statevalues;
	float8		n;
	uint16		dim;
	Vector	   *result;

	/* Check array before using */
	statevalues = CheckStateArray(statearray, "vector_avg");
	n = statevalues[0];

	/* SQL defines AVG of no values to be NULL */
	if (n == 0.0)
		PG_RETURN_NULL();

	/* Create vector */
	dim = STATE_DIMS(statearray);
	CheckDim(dim);
	result = InitVector(dim);
	for (int i = 0; i < dim; i++)
	{
		result->x[i] = statevalues[i + 1] / n;
		CheckElement(result->x[i]);
	}

	PG_RETURN_POINTER(result);
}

/*
 * Convert sparse vector to dense vector
 */
FUNCTION_PREFIX PG_FUNCTION_INFO_V1(sparsevec_to_vector);
Datum
sparsevec_to_vector(PG_FUNCTION_ARGS)
{
	SparseVector *svec = PG_GETARG_SPARSEVEC_P(0);
	int32		typmod = PG_GETARG_INT32(1);
	Vector	   *result;
	int			dim = svec->dim;
	float	   *values = SPARSEVEC_VALUES(svec);

	CheckDim(dim);
	CheckExpectedDim(typmod, dim);

	result = InitVector(dim);
	for (int i = 0; i < svec->nnz; i++)
		result->x[svec->indices[i]] = values[i];

	PG_RETURN_POINTER(result);
}
```

## File: `src/vector.h`
```c
#ifndef VECTOR_H
#define VECTOR_H

#define VECTOR_MAX_DIM 16000

#define VECTOR_SIZE(_dim)		(offsetof(Vector, x) + sizeof(float)*(_dim))
#define DatumGetVector(x)		((Vector *) PG_DETOAST_DATUM(x))
#define PG_GETARG_VECTOR_P(x)	DatumGetVector(PG_GETARG_DATUM(x))
#define PG_RETURN_VECTOR_P(x)	PG_RETURN_POINTER(x)

typedef struct Vector
{
	int32		vl_len_;		/* varlena header (do not touch directly!) */
	int16		dim;			/* number of dimensions */
	int16		unused;			/* reserved for future use, always zero */
	float		x[FLEXIBLE_ARRAY_MEMBER];
}			Vector;

Vector	   *InitVector(int dim);
void		PrintVector(char *msg, Vector * vector);
int			vector_cmp_internal(Vector * a, Vector * b);

/* TODO Move to better place */
#if PG_VERSION_NUM >= 160000
#define FUNCTION_PREFIX
#else
#define FUNCTION_PREFIX PGDLLEXPORT
#endif

#endif
```

## File: `test/expected/bit.out`
```
SELECT hamming_distance('111', '111');
 hamming_distance 
------------------
                0
(1 row)

SELECT hamming_distance('111', '110');
 hamming_distance 
------------------
                1
(1 row)

SELECT hamming_distance('111', '100');
 hamming_distance 
------------------
                2
(1 row)

SELECT hamming_distance('111', '000');
 hamming_distance 
------------------
                3
(1 row)

SELECT hamming_distance('10101010101010101010', '01010101010101010101');
 hamming_distance 
------------------
               20
(1 row)

SELECT hamming_distance('101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101', '101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101');
 hamming_distance 
------------------
                0
(1 row)

SELECT hamming_distance('101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101', '010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010');
 hamming_distance 
------------------
              513
(1 row)

SELECT hamming_distance('110000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000011', '100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001');
 hamming_distance 
------------------
                2
(1 row)

SELECT hamming_distance('', '');
 hamming_distance 
------------------
                0
(1 row)

SELECT hamming_distance('111', '00');
ERROR:  different bit lengths 3 and 2
SELECT hamming_distance('111', '000'::varbit(4));
 hamming_distance 
------------------
                3
(1 row)

SELECT hamming_distance('111', '0000'::varbit(4));
ERROR:  different bit lengths 3 and 4
SELECT jaccard_distance('1111', '1111');
 jaccard_distance 
------------------
                0
(1 row)

SELECT jaccard_distance('1111', '1110');
 jaccard_distance 
------------------
             0.25
(1 row)

SELECT jaccard_distance('1111', '1100');
 jaccard_distance 
------------------
              0.5
(1 row)

SELECT jaccard_distance('1111', '1000');
 jaccard_distance 
------------------
             0.75
(1 row)

SELECT jaccard_distance('1111', '0000');
 jaccard_distance 
------------------
                1
(1 row)

SELECT jaccard_distance('1100', '1000');
 jaccard_distance 
------------------
              0.5
(1 row)

SELECT jaccard_distance('10101010101010101010', '01010101010101010101');
 jaccard_distance 
------------------
                1
(1 row)

SELECT jaccard_distance('101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101', '101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101');
 jaccard_distance 
------------------
                0
(1 row)

SELECT jaccard_distance('101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101', '010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010');
 jaccard_distance 
------------------
                1
(1 row)

SELECT jaccard_distance('110000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000011', '100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001');
 jaccard_distance 
------------------
              0.5
(1 row)

SELECT jaccard_distance('', '');
 jaccard_distance 
------------------
                1
(1 row)

SELECT jaccard_distance('1111', '000');
ERROR:  different bit lengths 4 and 3
SELECT jaccard_distance('1111', '0000'::varbit(5));
 jaccard_distance 
------------------
                1
(1 row)

SELECT jaccard_distance('1111', '00000'::varbit(5));
ERROR:  different bit lengths 4 and 5
```

## File: `test/expected/btree.out`
```
SET enable_seqscan = off;
-- vector
CREATE TABLE t (val vector(3));
INSERT INTO t (val) VALUES ('[0,0,0]'), ('[1,2,3]'), ('[1,1,1]'), (NULL);
CREATE INDEX ON t (val);
SELECT * FROM t WHERE val = '[1,2,3]';
   val   
---------
 [1,2,3]
(1 row)

SELECT * FROM t ORDER BY val;
   val   
---------
 [0,0,0]
 [1,1,1]
 [1,2,3]
 
(4 rows)

DROP TABLE t;
-- halfvec
CREATE TABLE t (val halfvec(3));
INSERT INTO t (val) VALUES ('[0,0,0]'), ('[1,2,3]'), ('[1,1,1]'), (NULL);
CREATE INDEX ON t (val);
SELECT * FROM t WHERE val = '[1,2,3]';
   val   
---------
 [1,2,3]
(1 row)

SELECT * FROM t ORDER BY val;
   val   
---------
 [0,0,0]
 [1,1,1]
 [1,2,3]
 
(4 rows)

DROP TABLE t;
-- sparsevec
CREATE TABLE t (val sparsevec(3));
INSERT INTO t (val) VALUES ('{}/3'), ('{1:1,2:2,3:3}/3'), ('{1:1,2:1,3:1}/3'), (NULL);
CREATE INDEX ON t (val);
SELECT * FROM t WHERE val = '{1:1,2:2,3:3}/3';
       val       
-----------------
 {1:1,2:2,3:3}/3
(1 row)

SELECT * FROM t ORDER BY val;
       val       
-----------------
 {}/3
 {1:1,2:1,3:1}/3
 {1:1,2:2,3:3}/3
 
(4 rows)

DROP TABLE t;
```

## File: `test/expected/cast.out`
```
SELECT ARRAY[1,2,3]::vector;
  array  
---------
 [1,2,3]
(1 row)

SELECT ARRAY[1.0,2.0,3.0]::vector;
  array  
---------
 [1,2,3]
(1 row)

SELECT ARRAY[1,2,3]::float4[]::vector;
  array  
---------
 [1,2,3]
(1 row)

SELECT ARRAY[1,2,3]::float8[]::vector;
  array  
---------
 [1,2,3]
(1 row)

SELECT ARRAY[1,2,3]::numeric[]::vector;
  array  
---------
 [1,2,3]
(1 row)

SELECT '[1,2,3]'::vector::real[];
 float4  
---------
 {1,2,3}
(1 row)

SELECT '{1,2,3}'::real[]::vector;
 vector  
---------
 [1,2,3]
(1 row)

SELECT '{1,2,3}'::real[]::vector(3);
 vector  
---------
 [1,2,3]
(1 row)

SELECT '{1,2,3}'::real[]::vector(2);
ERROR:  expected 2 dimensions, not 3
SELECT '{NULL}'::real[]::vector;
ERROR:  array must not contain nulls
SELECT '{NaN}'::real[]::vector;
ERROR:  NaN not allowed in vector
SELECT '{Infinity}'::real[]::vector;
ERROR:  infinite value not allowed in vector
SELECT '{-Infinity}'::real[]::vector;
ERROR:  infinite value not allowed in vector
SELECT '{}'::real[]::vector;
ERROR:  vector must have at least 1 dimension
SELECT '{{1}}'::real[]::vector;
ERROR:  array must be 1-D
SELECT '{1,2,3}'::double precision[]::vector;
 vector  
---------
 [1,2,3]
(1 row)

SELECT '{1,2,3}'::double precision[]::vector(3);
 vector  
---------
 [1,2,3]
(1 row)

SELECT '{1,2,3}'::double precision[]::vector(2);
ERROR:  expected 2 dimensions, not 3
SELECT '{4e38,-4e38}'::double precision[]::vector;
ERROR:  infinite value not allowed in vector
SELECT '{1e-46,-1e-46}'::double precision[]::vector;
 vector 
--------
 [0,-0]
(1 row)

SELECT '[1,2,3]'::vector::halfvec;
 halfvec 
---------
 [1,2,3]
(1 row)

SELECT '[1,2,3]'::vector::halfvec(3);
 halfvec 
---------
 [1,2,3]
(1 row)

SELECT '[1,2,3]'::vector::halfvec(2);
ERROR:  expected 2 dimensions, not 3
SELECT '[65520]'::vector::halfvec;
ERROR:  "65520" is out of range for type halfvec
SELECT '[1e-8]'::vector::halfvec;
 halfvec 
---------
 [0]
(1 row)

SELECT '[1,2,3]'::halfvec::vector;
 vector  
---------
 [1,2,3]
(1 row)

SELECT '[1,2,3]'::halfvec::vector(3);
 vector  
---------
 [1,2,3]
(1 row)

SELECT '[1,2,3]'::halfvec::vector(2);
ERROR:  expected 2 dimensions, not 3
SELECT '{1,2,3}'::real[]::halfvec;
 halfvec 
---------
 [1,2,3]
(1 row)

SELECT '{1,2,3}'::real[]::halfvec(3);
 halfvec 
---------
 [1,2,3]
(1 row)

SELECT '{1,2,3}'::real[]::halfvec(2);
ERROR:  expected 2 dimensions, not 3
SELECT '{65520,-65520}'::real[]::halfvec;
ERROR:  "65520" is out of range for type halfvec
SELECT '{1e-8,-1e-8}'::real[]::halfvec;
 halfvec 
---------
 [0,-0]
(1 row)

SELECT '[0,1.5,0,3.5,0]'::vector::sparsevec;
    sparsevec    
-----------------
 {2:1.5,4:3.5}/5
(1 row)

SELECT '[0,1.5,0,3.5,0]'::vector::sparsevec(5);
    sparsevec    
-----------------
 {2:1.5,4:3.5}/5
(1 row)

SELECT '[0,1.5,0,3.5,0]'::vector::sparsevec(4);
ERROR:  expected 4 dimensions, not 5
SELECT '{2:1.5,4:3.5}/5'::sparsevec::vector;
     vector      
-----------------
 [0,1.5,0,3.5,0]
(1 row)

SELECT '{2:1.5,4:3.5}/5'::sparsevec::vector(5);
     vector      
-----------------
 [0,1.5,0,3.5,0]
(1 row)

SELECT '{2:1.5,4:3.5}/5'::sparsevec::vector(4);
ERROR:  expected 4 dimensions, not 5
SELECT '{}/16001'::sparsevec::vector;
ERROR:  vector cannot have more than 16000 dimensions
SELECT '[0,1.5,0,3.5,0]'::halfvec::sparsevec;
    sparsevec    
-----------------
 {2:1.5,4:3.5}/5
(1 row)

SELECT '[0,1.5,0,3.5,0]'::halfvec::sparsevec(5);
    sparsevec    
-----------------
 {2:1.5,4:3.5}/5
(1 row)

SELECT '[0,1.5,0,3.5,0]'::halfvec::sparsevec(4);
ERROR:  expected 4 dimensions, not 5
SELECT '{2:1.5,4:3.5}/5'::sparsevec::halfvec;
     halfvec     
-----------------
 [0,1.5,0,3.5,0]
(1 row)

SELECT '{2:1.5,4:3.5}/5'::sparsevec::halfvec(5);
     halfvec     
-----------------
 [0,1.5,0,3.5,0]
(1 row)

SELECT '{2:1.5,4:3.5}/5'::sparsevec::halfvec(4);
ERROR:  expected 4 dimensions, not 5
SELECT '{}/16001'::sparsevec::halfvec;
ERROR:  halfvec cannot have more than 16000 dimensions
SELECT '{1:65520}/1'::sparsevec::halfvec;
ERROR:  "65520" is out of range for type halfvec
SELECT '{1:1e-8}/1'::sparsevec::halfvec;
 halfvec 
---------
 [0]
(1 row)

SELECT ARRAY[1,0,2,0,3,0]::sparsevec;
      array      
-----------------
 {1:1,3:2,5:3}/6
(1 row)

SELECT ARRAY[1.0,0.0,2.0,0.0,3.0,0.0]::sparsevec;
      array      
-----------------
 {1:1,3:2,5:3}/6
(1 row)

SELECT ARRAY[1,0,2,0,3,0]::float4[]::sparsevec;
      array      
-----------------
 {1:1,3:2,5:3}/6
(1 row)

SELECT ARRAY[1,0,2,0,3,0]::float8[]::sparsevec;
      array      
-----------------
 {1:1,3:2,5:3}/6
(1 row)

SELECT ARRAY[1,0,2,0,3,0]::numeric[]::sparsevec;
      array      
-----------------
 {1:1,3:2,5:3}/6
(1 row)

SELECT '{1,0,2,0,3,0}'::real[]::sparsevec;
    sparsevec    
-----------------
 {1:1,3:2,5:3}/6
(1 row)

SELECT '{1,0,2,0,3,0}'::real[]::sparsevec(6);
    sparsevec    
-----------------
 {1:1,3:2,5:3}/6
(1 row)

SELECT '{1,0,2,0,3,0}'::real[]::sparsevec(5);
ERROR:  expected 5 dimensions, not 6
SELECT '{NULL}'::real[]::sparsevec;
ERROR:  array must not contain nulls
SELECT '{NaN}'::real[]::sparsevec;
ERROR:  NaN not allowed in sparsevec
SELECT '{Infinity}'::real[]::sparsevec;
ERROR:  infinite value not allowed in sparsevec
SELECT '{-Infinity}'::real[]::sparsevec;
ERROR:  infinite value not allowed in sparsevec
SELECT '{}'::real[]::sparsevec;
ERROR:  sparsevec must have at least 1 dimension
SELECT '{{1}}'::real[]::sparsevec;
ERROR:  array must be 1-D
SELECT array_agg(n)::vector FROM generate_series(1, 16001) n;
ERROR:  vector cannot have more than 16000 dimensions
SELECT array_to_vector(array_agg(n), 16001, false) FROM generate_series(1, 16001) n;
ERROR:  vector cannot have more than 16000 dimensions
-- ensure no error
SELECT ARRAY[1,2,3] = ARRAY[1,2,3];
 ?column? 
----------
 t
(1 row)

```

## File: `test/expected/copy.out`
```
-- vector
CREATE TABLE t (val vector(3));
INSERT INTO t (val) VALUES ('[0,0,0]'), ('[1,2,3]'), ('[1,1,1]'), (NULL);
CREATE TABLE t2 (val vector(3));
\copy t TO 'results/vector.bin' WITH (FORMAT binary)
\copy t2 FROM 'results/vector.bin' WITH (FORMAT binary)
SELECT * FROM t2 ORDER BY val;
   val   
---------
 [0,0,0]
 [1,1,1]
 [1,2,3]
 
(4 rows)

DROP TABLE t;
DROP TABLE t2;
-- halfvec
CREATE TABLE t (val halfvec(3));
INSERT INTO t (val) VALUES ('[0,0,0]'), ('[1,2,3]'), ('[1,1,1]'), (NULL);
CREATE TABLE t2 (val halfvec(3));
\copy t TO 'results/halfvec.bin' WITH (FORMAT binary)
\copy t2 FROM 'results/halfvec.bin' WITH (FORMAT binary)
SELECT * FROM t2 ORDER BY val;
   val   
---------
 [0,0,0]
 [1,1,1]
 [1,2,3]
 
(4 rows)

DROP TABLE t;
DROP TABLE t2;
-- sparsevec
CREATE TABLE t (val sparsevec(3));
INSERT INTO t (val) VALUES ('{}/3'), ('{1:1,2:2,3:3}/3'), ('{1:1,2:1,3:1}/3'), (NULL);
CREATE TABLE t2 (val sparsevec(3));
\copy t TO 'results/sparsevec.bin' WITH (FORMAT binary)
\copy t2 FROM 'results/sparsevec.bin' WITH (FORMAT binary)
SELECT * FROM t2 ORDER BY val;
       val       
-----------------
 {}/3
 {1:1,2:1,3:1}/3
 {1:1,2:2,3:3}/3
 
(4 rows)

DROP TABLE t;
DROP TABLE t2;
```

## File: `test/expected/halfvec.out`
```
SELECT '[1,2,3]'::halfvec;
 halfvec 
---------
 [1,2,3]
(1 row)

SELECT '[-1,-2,-3]'::halfvec;
  halfvec   
------------
 [-1,-2,-3]
(1 row)

SELECT '[1.,2.,3.]'::halfvec;
 halfvec 
---------
 [1,2,3]
(1 row)

SELECT ' [ 1,  2 ,    3  ] '::halfvec;
 halfvec 
---------
 [1,2,3]
(1 row)

SELECT '[1.23456]'::halfvec;
  halfvec   
------------
 [1.234375]
(1 row)

SELECT '[hello,1]'::halfvec;
ERROR:  invalid input syntax for type halfvec: "[hello,1]"
LINE 1: SELECT '[hello,1]'::halfvec;
               ^
SELECT '[NaN,1]'::halfvec;
ERROR:  NaN not allowed in halfvec
LINE 1: SELECT '[NaN,1]'::halfvec;
               ^
SELECT '[Infinity,1]'::halfvec;
ERROR:  infinite value not allowed in halfvec
LINE 1: SELECT '[Infinity,1]'::halfvec;
               ^
SELECT '[-Infinity,1]'::halfvec;
ERROR:  infinite value not allowed in halfvec
LINE 1: SELECT '[-Infinity,1]'::halfvec;
               ^
SELECT '[65519,-65519]'::halfvec;
    halfvec     
----------------
 [65504,-65504]
(1 row)

SELECT '[65520,-65520]'::halfvec;
ERROR:  "65520" is out of range for type halfvec
LINE 1: SELECT '[65520,-65520]'::halfvec;
               ^
SELECT '[1e-8,-1e-8]'::halfvec;
 halfvec 
---------
 [0,-0]
(1 row)

SELECT '[4e38,1]'::halfvec;
ERROR:  "4e38" is out of range for type halfvec
LINE 1: SELECT '[4e38,1]'::halfvec;
               ^
SELECT '[1e-46,1]'::halfvec;
 halfvec 
---------
 [0,1]
(1 row)

SELECT '[1,2,3'::halfvec;
ERROR:  invalid input syntax for type halfvec: "[1,2,3"
LINE 1: SELECT '[1,2,3'::halfvec;
               ^
SELECT '[1,2,3]9'::halfvec;
ERROR:  invalid input syntax for type halfvec: "[1,2,3]9"
LINE 1: SELECT '[1,2,3]9'::halfvec;
               ^
DETAIL:  Junk after closing right brace.
SELECT '1,2,3'::halfvec;
ERROR:  invalid input syntax for type halfvec: "1,2,3"
LINE 1: SELECT '1,2,3'::halfvec;
               ^
DETAIL:  Vector contents must start with "[".
SELECT ''::halfvec;
ERROR:  invalid input syntax for type halfvec: ""
LINE 1: SELECT ''::halfvec;
               ^
DETAIL:  Vector contents must start with "[".
SELECT '['::halfvec;
ERROR:  invalid input syntax for type halfvec: "["
LINE 1: SELECT '['::halfvec;
               ^
SELECT '[ '::halfvec;
ERROR:  invalid input syntax for type halfvec: "[ "
LINE 1: SELECT '[ '::halfvec;
               ^
SELECT '[,'::halfvec;
ERROR:  invalid input syntax for type halfvec: "[,"
LINE 1: SELECT '[,'::halfvec;
               ^
SELECT '[]'::halfvec;
ERROR:  halfvec must have at least 1 dimension
LINE 1: SELECT '[]'::halfvec;
               ^
SELECT '[ ]'::halfvec;
ERROR:  halfvec must have at least 1 dimension
LINE 1: SELECT '[ ]'::halfvec;
               ^
SELECT '[,]'::halfvec;
ERROR:  invalid input syntax for type halfvec: "[,]"
LINE 1: SELECT '[,]'::halfvec;
               ^
SELECT '[1,]'::halfvec;
ERROR:  invalid input syntax for type halfvec: "[1,]"
LINE 1: SELECT '[1,]'::halfvec;
               ^
SELECT '[1a]'::halfvec;
ERROR:  invalid input syntax for type halfvec: "[1a]"
LINE 1: SELECT '[1a]'::halfvec;
               ^
SELECT '[1,,3]'::halfvec;
ERROR:  invalid input syntax for type halfvec: "[1,,3]"
LINE 1: SELECT '[1,,3]'::halfvec;
               ^
SELECT '[1, ,3]'::halfvec;
ERROR:  invalid input syntax for type halfvec: "[1, ,3]"
LINE 1: SELECT '[1, ,3]'::halfvec;
               ^
SELECT '[1,2,3]'::halfvec(3);
 halfvec 
---------
 [1,2,3]
(1 row)

SELECT '[1,2,3]'::halfvec(2);
ERROR:  expected 2 dimensions, not 3
SELECT '[1,2,3]'::halfvec(3, 2);
ERROR:  invalid type modifier
LINE 1: SELECT '[1,2,3]'::halfvec(3, 2);
                          ^
SELECT '[1,2,3]'::halfvec('a');
ERROR:  invalid input syntax for type integer: "a"
LINE 1: SELECT '[1,2,3]'::halfvec('a');
                          ^
SELECT '[1,2,3]'::halfvec(0);
ERROR:  dimensions for type halfvec must be at least 1
LINE 1: SELECT '[1,2,3]'::halfvec(0);
                          ^
SELECT '[1,2,3]'::halfvec(16001);
ERROR:  dimensions for type halfvec cannot exceed 16000
LINE 1: SELECT '[1,2,3]'::halfvec(16001);
                          ^
SELECT unnest('{"[1,2,3]", "[4,5,6]"}'::halfvec[]);
 unnest  
---------
 [1,2,3]
 [4,5,6]
(2 rows)

SELECT '{"[1,2,3]"}'::halfvec(2)[];
ERROR:  expected 2 dimensions, not 3
SELECT '[1,2,3]'::halfvec + '[4,5,6]';
 ?column? 
----------
 [5,7,9]
(1 row)

SELECT '[65519]'::halfvec + '[65519]';
ERROR:  value out of range: overflow
SELECT '[1,2]'::halfvec + '[3]';
ERROR:  different halfvec dimensions 2 and 1
SELECT '[1,2,3]'::halfvec - '[4,5,6]';
  ?column?  
------------
 [-3,-3,-3]
(1 row)

SELECT '[-65519]'::halfvec - '[65519]';
ERROR:  value out of range: overflow
SELECT '[1,2]'::halfvec - '[3]';
ERROR:  different halfvec dimensions 2 and 1
SELECT '[1,2,3]'::halfvec * '[4,5,6]';
 ?column?  
-----------
 [4,10,18]
(1 row)

SELECT '[65519]'::halfvec * '[65519]';
ERROR:  value out of range: overflow
SELECT '[1e-7]'::halfvec * '[1e-7]';
ERROR:  value out of range: underflow
SELECT '[1,2]'::halfvec * '[3]';
ERROR:  different halfvec dimensions 2 and 1
SELECT '[1,2,3]'::halfvec || '[4,5]';
  ?column?   
-------------
 [1,2,3,4,5]
(1 row)

SELECT array_fill(0, ARRAY[16000])::halfvec || '[1]';
ERROR:  halfvec cannot have more than 16000 dimensions
SELECT '[1,2,3]'::halfvec < '[1,2,3]';
 ?column? 
----------
 f
(1 row)

SELECT '[1,2,3]'::halfvec < '[1,2]';
 ?column? 
----------
 f
(1 row)

SELECT '[1,2,3]'::halfvec <= '[1,2,3]';
 ?column? 
----------
 t
(1 row)

SELECT '[1,2,3]'::halfvec <= '[1,2]';
 ?column? 
----------
 f
(1 row)

SELECT '[1,2,3]'::halfvec = '[1,2,3]';
 ?column? 
----------
 t
(1 row)

SELECT '[1,2,3]'::halfvec = '[1,2]';
 ?column? 
----------
 f
(1 row)

SELECT '[1,2,3]'::halfvec != '[1,2,3]';
 ?column? 
----------
 f
(1 row)

SELECT '[1,2,3]'::halfvec != '[1,2]';
 ?column? 
----------
 t
(1 row)

SELECT '[1,2,3]'::halfvec >= '[1,2,3]';
 ?column? 
----------
 t
(1 row)

SELECT '[1,2,3]'::halfvec >= '[1,2]';
 ?column? 
----------
 t
(1 row)

SELECT '[1,2,3]'::halfvec > '[1,2,3]';
 ?column? 
----------
 f
(1 row)

SELECT '[1,2,3]'::halfvec > '[1,2]';
 ?column? 
----------
 t
(1 row)

SELECT halfvec_cmp('[1,2,3]', '[1,2,3]');
 halfvec_cmp 
-------------
           0
(1 row)

SELECT halfvec_cmp('[1,2,3]', '[0,0,0]');
 halfvec_cmp 
-------------
           1
(1 row)

SELECT halfvec_cmp('[0,0,0]', '[1,2,3]');
 halfvec_cmp 
-------------
          -1
(1 row)

SELECT halfvec_cmp('[1,2]', '[1,2,3]');
 halfvec_cmp 
-------------
          -1
(1 row)

SELECT halfvec_cmp('[1,2,3]', '[1,2]');
 halfvec_cmp 
-------------
           1
(1 row)

SELECT halfvec_cmp('[1,2]', '[2,3,4]');
 halfvec_cmp 
-------------
          -1
(1 row)

SELECT halfvec_cmp('[2,3]', '[1,2,3]');
 halfvec_cmp 
-------------
           1
(1 row)

SELECT vector_dims('[1,2,3]'::halfvec);
 vector_dims 
-------------
           3
(1 row)

SELECT round(l2_norm('[1,1]'::halfvec)::numeric, 5);
  round  
---------
 1.41421
(1 row)

SELECT l2_norm('[3,4]'::halfvec);
 l2_norm 
---------
       5
(1 row)

SELECT l2_norm('[0,1]'::halfvec);
 l2_norm 
---------
       1
(1 row)

SELECT l2_norm('[0,0]'::halfvec);
 l2_norm 
---------
       0
(1 row)

SELECT l2_norm('[2]'::halfvec);
 l2_norm 
---------
       2
(1 row)

SELECT l2_distance('[0,0]'::halfvec, '[3,4]');
 l2_distance 
-------------
           5
(1 row)

SELECT l2_distance('[0,0]'::halfvec, '[0,1]');
 l2_distance 
-------------
           1
(1 row)

SELECT l2_distance('[1,2]'::halfvec, '[3]');
ERROR:  different halfvec dimensions 2 and 1
SELECT l2_distance('[1,1,1,1,1,1,1,1,1]'::halfvec, '[1,1,1,1,1,1,1,4,5]');
 l2_distance 
-------------
           5
(1 row)

SELECT '[0,0]'::halfvec <-> '[3,4]';
 ?column? 
----------
        5
(1 row)

SELECT inner_product('[1,2]'::halfvec, '[3,4]');
 inner_product 
---------------
            11
(1 row)

SELECT inner_product('[1,2]'::halfvec, '[3]');
ERROR:  different halfvec dimensions 2 and 1
SELECT inner_product('[65504]'::halfvec, '[65504]');
 inner_product 
---------------
    4290774016
(1 row)

SELECT inner_product('[1,1,1,1,1,1,1,1,1]'::halfvec, '[1,2,3,4,5,6,7,8,9]');
 inner_product 
---------------
            45
(1 row)

SELECT '[1,2]'::halfvec <#> '[3,4]';
 ?column? 
----------
      -11
(1 row)

SELECT cosine_distance('[1,2]'::halfvec, '[2,4]');
 cosine_distance 
-----------------
               0
(1 row)

SELECT cosine_distance('[1,2]'::halfvec, '[0,0]');
 cosine_distance 
-----------------
             NaN
(1 row)

SELECT cosine_distance('[1,1]'::halfvec, '[1,1]');
 cosine_distance 
-----------------
               0
(1 row)

SELECT cosine_distance('[1,0]'::halfvec, '[0,2]');
 cosine_distance 
-----------------
               1
(1 row)

SELECT cosine_distance('[1,1]'::halfvec, '[-1,-1]');
 cosine_distance 
-----------------
               2
(1 row)

SELECT cosine_distance('[1,2]'::halfvec, '[3]');
ERROR:  different halfvec dimensions 2 and 1
SELECT cosine_distance('[1,1]'::halfvec, '[1.1,1.1]');
 cosine_distance 
-----------------
               0
(1 row)

SELECT cosine_distance('[1,1]'::halfvec, '[-1.1,-1.1]');
 cosine_distance 
-----------------
               2
(1 row)

SELECT cosine_distance('[1,2,3,4,5,6,7,8,9]'::halfvec, '[1,2,3,4,5,6,7,8,9]');
 cosine_distance 
-----------------
               0
(1 row)

SELECT cosine_distance('[1,2,3,4,5,6,7,8,9]'::halfvec, '[-1,-2,-3,-4,-5,-6,-7,-8,-9]');
 cosine_distance 
-----------------
               2
(1 row)

SELECT '[1,2]'::halfvec <=> '[2,4]';
 ?column? 
----------
        0
(1 row)

SELECT l1_distance('[0,0]'::halfvec, '[3,4]');
 l1_distance 
-------------
           7
(1 row)

SELECT l1_distance('[0,0]'::halfvec, '[0,1]');
 l1_distance 
-------------
           1
(1 row)

SELECT l1_distance('[1,2]'::halfvec, '[3]');
ERROR:  different halfvec dimensions 2 and 1
SELECT l1_distance('[1,2,3,4,5,6,7,8,9]'::halfvec, '[1,2,3,4,5,6,7,8,9]');
 l1_distance 
-------------
           0
(1 row)

SELECT l1_distance('[1,2,3,4,5,6,7,8,9]'::halfvec, '[0,3,2,5,4,7,6,9,8]');
 l1_distance 
-------------
           9
(1 row)

SELECT '[0,0]'::halfvec <+> '[3,4]';
 ?column? 
----------
        7
(1 row)

SELECT l2_normalize('[3,4]'::halfvec);
      l2_normalize      
------------------------
 [0.60009766,0.7998047]
(1 row)

SELECT l2_normalize('[3,0]'::halfvec);
 l2_normalize 
--------------
 [1,0]
(1 row)

SELECT l2_normalize('[0,0.1]'::halfvec);
 l2_normalize 
--------------
 [0,1]
(1 row)

SELECT l2_normalize('[0,0]'::halfvec);
 l2_normalize 
--------------
 [0,0]
(1 row)

SELECT l2_normalize('[65504]'::halfvec);
 l2_normalize 
--------------
 [1]
(1 row)

SELECT binary_quantize('[1,0,-1]'::halfvec);
 binary_quantize 
-----------------
 100
(1 row)

SELECT binary_quantize('[0,0.1,-0.2,-0.3,0.4,0.5,0.6,-0.7,0.8,-0.9,1]'::halfvec);
 binary_quantize 
-----------------
 01001110101
(1 row)

SELECT binary_quantize('[1,2,3,-4,5,6,-7,8,1,-2,-3,4,5,-6,7,8,-1,2,3]'::halfvec);
   binary_quantize   
---------------------
 1110110110011011011
(1 row)

SELECT subvector('[1,2,3,4,5]'::halfvec, 1, 3);
 subvector 
-----------
 [1,2,3]
(1 row)

SELECT subvector('[1,2,3,4,5]'::halfvec, 3, 2);
 subvector 
-----------
 [3,4]
(1 row)

SELECT subvector('[1,2,3,4,5]'::halfvec, -1, 3);
 subvector 
-----------
 [1]
(1 row)

SELECT subvector('[1,2,3,4,5]'::halfvec, 3, 9);
 subvector 
-----------
 [3,4,5]
(1 row)

SELECT subvector('[1,2,3,4,5]'::halfvec, 1, 0);
ERROR:  halfvec must have at least 1 dimension
SELECT subvector('[1,2,3,4,5]'::halfvec, 3, -1);
ERROR:  halfvec must have at least 1 dimension
SELECT subvector('[1,2,3,4,5]'::halfvec, -1, 2);
ERROR:  halfvec must have at least 1 dimension
SELECT subvector('[1,2,3,4,5]'::halfvec, 2147483647, 10);
ERROR:  halfvec must have at least 1 dimension
SELECT subvector('[1,2,3,4,5]'::halfvec, 3, 2147483647);
 subvector 
-----------
 [3,4,5]
(1 row)

SELECT subvector('[1,2,3,4,5]'::halfvec, -2147483644, 2147483647);
 subvector 
-----------
 [1,2]
(1 row)

SELECT avg(v) FROM unnest(ARRAY['[1,2,3]'::halfvec, '[3,5,7]']) v;
    avg    
-----------
 [2,3.5,5]
(1 row)

SELECT avg(v) FROM unnest(ARRAY['[1,2,3]'::halfvec, '[3,5,7]', NULL]) v;
    avg    
-----------
 [2,3.5,5]
(1 row)

SELECT avg(v) FROM unnest(ARRAY[]::halfvec[]) v;
 avg 
-----
 
(1 row)

SELECT avg(v) FROM unnest(ARRAY['[1,2]'::halfvec, '[3]']) v;
ERROR:  expected 2 dimensions, not 1
SELECT avg(v) FROM unnest(ARRAY['[65504]'::halfvec, '[65504]']) v;
   avg   
---------
 [65504]
(1 row)

SELECT halfvec_avg(array_agg(n)) FROM generate_series(1, 16002) n;
ERROR:  halfvec cannot have more than 16000 dimensions
SELECT sum(v) FROM unnest(ARRAY['[1,2,3]'::halfvec, '[3,5,7]']) v;
   sum    
----------
 [4,7,10]
(1 row)

SELECT sum(v) FROM unnest(ARRAY['[1,2,3]'::halfvec, '[3,5,7]', NULL]) v;
   sum    
----------
 [4,7,10]
(1 row)

SELECT sum(v) FROM unnest(ARRAY[]::halfvec[]) v;
 sum 
-----
 
(1 row)

SELECT sum(v) FROM unnest(ARRAY['[1,2]'::halfvec, '[3]']) v;
ERROR:  different halfvec dimensions 2 and 1
SELECT sum(v) FROM unnest(ARRAY['[65504]'::halfvec, '[65504]']) v;
ERROR:  value out of range: overflow
```

## File: `test/expected/hnsw_bit.out`
```
SET enable_seqscan = off;
-- hamming
CREATE TABLE t (val bit(3));
INSERT INTO t (val) VALUES (B'000'), (B'100'), (B'111'), (NULL);
CREATE INDEX ON t USING hnsw (val bit_hamming_ops);
INSERT INTO t (val) VALUES (B'110');
SELECT * FROM t ORDER BY val <~> B'111';
 val 
-----
 111
 110
 100
 000
(4 rows)

SELECT COUNT(*) FROM (SELECT * FROM t ORDER BY val <~> (SELECT NULL::bit)) t2;
 count 
-------
     4
(1 row)

DROP TABLE t;
-- jaccard
CREATE TABLE t (val bit(4));
INSERT INTO t (val) VALUES (B'0000'), (B'1100'), (B'1111'), (NULL);
CREATE INDEX ON t USING hnsw (val bit_jaccard_ops);
INSERT INTO t (val) VALUES (B'1110');
SELECT * FROM t ORDER BY val <%> B'1111';
 val  
------
 1111
 1110
 1100
 0000
(4 rows)

SELECT COUNT(*) FROM (SELECT * FROM t ORDER BY val <%> (SELECT NULL::bit)) t2;
 count 
-------
     4
(1 row)

DROP TABLE t;
-- varbit
CREATE TABLE t (val varbit(3));
CREATE INDEX ON t USING hnsw (val bit_hamming_ops);
ERROR:  type not supported for hnsw index
CREATE INDEX ON t USING hnsw ((val::bit(3)) bit_hamming_ops);
CREATE INDEX ON t USING hnsw ((val::bit(64001)) bit_hamming_ops);
ERROR:  column cannot have more than 64000 dimensions for hnsw index
DROP TABLE t;
```

## File: `test/expected/hnsw_halfvec.out`
```
SET enable_seqscan = off;
-- L2
CREATE TABLE t (val halfvec(3));
INSERT INTO t (val) VALUES ('[0,0,0]'), ('[1,2,3]'), ('[1,1,1]'), (NULL);
CREATE INDEX ON t USING hnsw (val halfvec_l2_ops);
INSERT INTO t (val) VALUES ('[1,2,4]');
SELECT * FROM t ORDER BY val <-> '[3,3,3]';
   val   
---------
 [1,2,3]
 [1,2,4]
 [1,1,1]
 [0,0,0]
(4 rows)

SELECT COUNT(*) FROM (SELECT * FROM t ORDER BY val <-> (SELECT NULL::halfvec)) t2;
 count 
-------
     4
(1 row)

SELECT COUNT(*) FROM t;
 count 
-------
     5
(1 row)

TRUNCATE t;
SELECT * FROM t ORDER BY val <-> '[3,3,3]';
 val 
-----
(0 rows)

DROP TABLE t;
-- inner product
CREATE TABLE t (val halfvec(3));
INSERT INTO t (val) VALUES ('[0,0,0]'), ('[1,2,3]'), ('[1,1,1]'), (NULL);
CREATE INDEX ON t USING hnsw (val halfvec_ip_ops);
INSERT INTO t (val) VALUES ('[1,2,4]');
SELECT * FROM t ORDER BY val <#> '[3,3,3]';
   val   
---------
 [1,2,4]
 [1,2,3]
 [1,1,1]
 [0,0,0]
(4 rows)

SELECT COUNT(*) FROM (SELECT * FROM t ORDER BY val <#> (SELECT NULL::halfvec)) t2;
 count 
-------
     4
(1 row)

DROP TABLE t;
-- cosine
CREATE TABLE t (val halfvec(3));
INSERT INTO t (val) VALUES ('[0,0,0]'), ('[1,2,3]'), ('[1,1,1]'), (NULL);
CREATE INDEX ON t USING hnsw (val halfvec_cosine_ops);
INSERT INTO t (val) VALUES ('[1,2,4]');
SELECT * FROM t ORDER BY val <=> '[3,3,3]';
   val   
---------
 [1,1,1]
 [1,2,3]
 [1,2,4]
(3 rows)

SELECT COUNT(*) FROM (SELECT * FROM t ORDER BY val <=> '[0,0,0]') t2;
 count 
-------
     3
(1 row)

SELECT COUNT(*) FROM (SELECT * FROM t ORDER BY val <=> (SELECT NULL::halfvec)) t2;
 count 
-------
     3
(1 row)

DROP TABLE t;
-- L1
CREATE TABLE t (val halfvec(3));
INSERT INTO t (val) VALUES ('[0,0,0]'), ('[1,2,3]'), ('[1,1,1]'), (NULL);
CREATE INDEX ON t USING hnsw (val halfvec_l1_ops);
INSERT INTO t (val) VALUES ('[1,2,4]');
SELECT * FROM t ORDER BY val <+> '[3,3,3]';
   val   
---------
 [1,2,3]
 [1,2,4]
 [1,1,1]
 [0,0,0]
(4 rows)

SELECT COUNT(*) FROM (SELECT * FROM t ORDER BY val <+> (SELECT NULL::halfvec)) t2;
 count 
-------
     4
(1 row)

DROP TABLE t;
```

## File: `test/expected/hnsw_sparsevec.out`
```
SET enable_seqscan = off;
-- L2
CREATE TABLE t (val sparsevec(3));
INSERT INTO t (val) VALUES ('{}/3'), ('{1:1,2:2,3:3}/3'), ('{1:1,2:1,3:1}/3'), (NULL);
CREATE INDEX ON t USING hnsw (val sparsevec_l2_ops);
INSERT INTO t (val) VALUES ('{1:1,2:2,3:4}/3');
SELECT * FROM t ORDER BY val <-> '{1:3,2:3,3:3}/3';
       val       
-----------------
 {1:1,2:2,3:3}/3
 {1:1,2:2,3:4}/3
 {1:1,2:1,3:1}/3
 {}/3
(4 rows)

SELECT COUNT(*) FROM (SELECT * FROM t ORDER BY val <-> (SELECT NULL::sparsevec)) t2;
 count 
-------
     4
(1 row)

SELECT COUNT(*) FROM t;
 count 
-------
     5
(1 row)

TRUNCATE t;
SELECT * FROM t ORDER BY val <-> '{1:3,2:3,3:3}/3';
 val 
-----
(0 rows)

DROP TABLE t;
-- inner product
CREATE TABLE t (val sparsevec(3));
INSERT INTO t (val) VALUES ('{}/3'), ('{1:1,2:2,3:3}/3'), ('{1:1,2:1,3:1}/3'), (NULL);
CREATE INDEX ON t USING hnsw (val sparsevec_ip_ops);
INSERT INTO t (val) VALUES ('{1:1,2:2,3:4}/3');
SELECT * FROM t ORDER BY val <#> '{1:3,2:3,3:3}/3';
       val       
-----------------
 {1:1,2:2,3:4}/3
 {1:1,2:2,3:3}/3
 {1:1,2:1,3:1}/3
 {}/3
(4 rows)

SELECT COUNT(*) FROM (SELECT * FROM t ORDER BY val <#> (SELECT NULL::sparsevec)) t2;
 count 
-------
     4
(1 row)

DROP TABLE t;
-- cosine
CREATE TABLE t (val sparsevec(3));
INSERT INTO t (val) VALUES ('{}/3'), ('{1:1,2:2,3:3}/3'), ('{1:1,2:1,3:1}/3'), (NULL);
CREATE INDEX ON t USING hnsw (val sparsevec_cosine_ops);
INSERT INTO t (val) VALUES ('{1:1,2:2,3:4}/3');
SELECT * FROM t ORDER BY val <=> '{1:3,2:3,3:3}/3';
       val       
-----------------
 {1:1,2:1,3:1}/3
 {1:1,2:2,3:3}/3
 {1:1,2:2,3:4}/3
(3 rows)

SELECT COUNT(*) FROM (SELECT * FROM t ORDER BY val <=> '{}/3') t2;
 count 
-------
     3
(1 row)

SELECT COUNT(*) FROM (SELECT * FROM t ORDER BY val <=> (SELECT NULL::sparsevec)) t2;
 count 
-------
     3
(1 row)

DROP TABLE t;
-- L1
CREATE TABLE t (val sparsevec(3));
INSERT INTO t (val) VALUES ('{}/3'), ('{1:1,2:2,3:3}/3'), ('{1:1,2:1,3:1}/3'), (NULL);
CREATE INDEX ON t USING hnsw (val sparsevec_l1_ops);
INSERT INTO t (val) VALUES ('{1:1,2:2,3:4}/3');
SELECT * FROM t ORDER BY val <+> '{1:3,2:3,3:3}/3';
       val       
-----------------
 {1:1,2:2,3:3}/3
 {1:1,2:2,3:4}/3
 {1:1,2:1,3:1}/3
 {}/3
(4 rows)

SELECT COUNT(*) FROM (SELECT * FROM t ORDER BY val <+> (SELECT NULL::sparsevec)) t2;
 count 
-------
     4
(1 row)

DROP TABLE t;
-- non-zero elements
CREATE TABLE t (val sparsevec(1001));
INSERT INTO t (val) VALUES (array_fill(1, ARRAY[1001])::vector::sparsevec);
CREATE INDEX ON t USING hnsw (val sparsevec_l2_ops);
ERROR:  sparsevec cannot have more than 1000 non-zero elements for hnsw index
TRUNCATE t;
CREATE INDEX ON t USING hnsw (val sparsevec_l2_ops);
INSERT INTO t (val) VALUES (array_fill(1, ARRAY[1001])::vector::sparsevec);
ERROR:  sparsevec cannot have more than 1000 non-zero elements for hnsw index
DROP TABLE t;
```

## File: `test/expected/hnsw_vector.out`
```
SET enable_seqscan = off;
-- L2
CREATE TABLE t (val vector(3));
INSERT INTO t (val) VALUES ('[0,0,0]'), ('[1,2,3]'), ('[1,1,1]'), (NULL);
CREATE INDEX ON t USING hnsw (val vector_l2_ops);
INSERT INTO t (val) VALUES ('[1,2,4]');
SELECT * FROM t ORDER BY val <-> '[3,3,3]';
   val   
---------
 [1,2,3]
 [1,2,4]
 [1,1,1]
 [0,0,0]
(4 rows)

SELECT COUNT(*) FROM (SELECT * FROM t ORDER BY val <-> (SELECT NULL::vector)) t2;
 count 
-------
     4
(1 row)

SELECT COUNT(*) FROM t;
 count 
-------
     5
(1 row)

TRUNCATE t;
SELECT * FROM t ORDER BY val <-> '[3,3,3]';
 val 
-----
(0 rows)

DROP TABLE t;
-- inner product
CREATE TABLE t (val vector(3));
INSERT INTO t (val) VALUES ('[0,0,0]'), ('[1,2,3]'), ('[1,1,1]'), (NULL);
CREATE INDEX ON t USING hnsw (val vector_ip_ops);
INSERT INTO t (val) VALUES ('[1,2,4]');
SELECT * FROM t ORDER BY val <#> '[3,3,3]';
   val   
---------
 [1,2,4]
 [1,2,3]
 [1,1,1]
 [0,0,0]
(4 rows)

SELECT COUNT(*) FROM (SELECT * FROM t ORDER BY val <#> (SELECT NULL::vector)) t2;
 count 
-------
     4
(1 row)

DROP TABLE t;
-- cosine
CREATE TABLE t (val vector(3));
INSERT INTO t (val) VALUES ('[0,0,0]'), ('[1,2,3]'), ('[1,1,1]'), (NULL);
CREATE INDEX ON t USING hnsw (val vector_cosine_ops);
INSERT INTO t (val) VALUES ('[1,2,4]');
SELECT * FROM t ORDER BY val <=> '[3,3,3]';
   val   
---------
 [1,1,1]
 [1,2,3]
 [1,2,4]
(3 rows)

SELECT COUNT(*) FROM (SELECT * FROM t ORDER BY val <=> '[0,0,0]') t2;
 count 
-------
     3
(1 row)

SELECT COUNT(*) FROM (SELECT * FROM t ORDER BY val <=> (SELECT NULL::vector)) t2;
 count 
-------
     3
(1 row)

DROP TABLE t;
-- L1
CREATE TABLE t (val vector(3));
INSERT INTO t (val) VALUES ('[0,0,0]'), ('[1,2,3]'), ('[1,1,1]'), (NULL);
CREATE INDEX ON t USING hnsw (val vector_l1_ops);
INSERT INTO t (val) VALUES ('[1,2,4]');
SELECT * FROM t ORDER BY val <+> '[3,3,3]';
   val   
---------
 [1,2,3]
 [1,2,4]
 [1,1,1]
 [0,0,0]
(4 rows)

SELECT COUNT(*) FROM (SELECT * FROM t ORDER BY val <+> (SELECT NULL::vector)) t2;
 count 
-------
     4
(1 row)

DROP TABLE t;
-- iterative
CREATE TABLE t (val vector(3));
INSERT INTO t (val) VALUES ('[0,0,0]'), ('[1,2,3]'), ('[1,1,1]'), (NULL);
CREATE INDEX ON t USING hnsw (val vector_l2_ops);
SET hnsw.iterative_scan = strict_order;
SET hnsw.ef_search = 1;
SELECT * FROM t ORDER BY val <-> '[3,3,3]';
   val   
---------
 [1,2,3]
 [1,1,1]
 [0,0,0]
(3 rows)

SET hnsw.iterative_scan = relaxed_order;
SELECT * FROM t ORDER BY val <-> '[3,3,3]';
   val   
---------
 [1,2,3]
 [1,1,1]
 [0,0,0]
(3 rows)

TRUNCATE t;
SELECT * FROM t ORDER BY val <-> '[3,3,3]';
 val 
-----
(0 rows)

RESET hnsw.iterative_scan;
RESET hnsw.ef_search;
DROP TABLE t;
-- unlogged
CREATE UNLOGGED TABLE t (val vector(3));
INSERT INTO t (val) VALUES ('[0,0,0]'), ('[1,2,3]'), ('[1,1,1]'), (NULL);
CREATE INDEX ON t USING hnsw (val vector_l2_ops);
SELECT * FROM t ORDER BY val <-> '[3,3,3]';
   val   
---------
 [1,2,3]
 [1,1,1]
 [0,0,0]
(3 rows)

DROP TABLE t;
-- options
CREATE TABLE t (val vector(3));
CREATE INDEX ON t USING hnsw (val vector_l2_ops) WITH (m = 1);
ERROR:  value 1 out of bounds for option "m"
DETAIL:  Valid values are between "2" and "100".
CREATE INDEX ON t USING hnsw (val vector_l2_ops) WITH (m = 101);
ERROR:  value 101 out of bounds for option "m"
DETAIL:  Valid values are between "2" and "100".
CREATE INDEX ON t USING hnsw (val vector_l2_ops) WITH (ef_construction = 3);
ERROR:  value 3 out of bounds for option "ef_construction"
DETAIL:  Valid values are between "4" and "1000".
CREATE INDEX ON t USING hnsw (val vector_l2_ops) WITH (ef_construction = 1001);
ERROR:  value 1001 out of bounds for option "ef_construction"
DETAIL:  Valid values are between "4" and "1000".
CREATE INDEX ON t USING hnsw (val vector_l2_ops) WITH (m = 16, ef_construction = 31);
ERROR:  ef_construction must be greater than or equal to 2 * m
SHOW hnsw.ef_search;
 hnsw.ef_search 
----------------
 40
(1 row)

SET hnsw.ef_search = 0;
ERROR:  0 is outside the valid range for parameter "hnsw.ef_search" (1 .. 1000)
SET hnsw.ef_search = 1001;
ERROR:  1001 is outside the valid range for parameter "hnsw.ef_search" (1 .. 1000)
SHOW hnsw.iterative_scan;
 hnsw.iterative_scan 
---------------------
 off
(1 row)

SET hnsw.iterative_scan = on;
ERROR:  invalid value for parameter "hnsw.iterative_scan": "on"
HINT:  Available values: off, relaxed_order, strict_order.
SHOW hnsw.max_scan_tuples;
 hnsw.max_scan_tuples 
----------------------
 20000
(1 row)

SET hnsw.max_scan_tuples = 0;
ERROR:  0 is outside the valid range for parameter "hnsw.max_scan_tuples" (1 .. 2147483647)
SHOW hnsw.scan_mem_multiplier;
 hnsw.scan_mem_multiplier 
--------------------------
 1
(1 row)

SET hnsw.scan_mem_multiplier = 0;
ERROR:  0 is outside the valid range for parameter "hnsw.scan_mem_multiplier" (1 .. 1000)
SET hnsw.scan_mem_multiplier = 1001;
ERROR:  1001 is outside the valid range for parameter "hnsw.scan_mem_multiplier" (1 .. 1000)
DROP TABLE t;
```

## File: `test/expected/ivfflat_bit.out`
```
SET enable_seqscan = off;
-- hamming
CREATE TABLE t (val bit(3));
INSERT INTO t (val) VALUES (B'000'), (B'100'), (B'111'), (NULL);
CREATE INDEX ON t USING ivfflat (val bit_hamming_ops) WITH (lists = 1);
INSERT INTO t (val) VALUES (B'110');
SELECT * FROM t ORDER BY val <~> B'111';
 val 
-----
 111
 110
 100
 000
(4 rows)

SELECT COUNT(*) FROM (SELECT * FROM t ORDER BY val <~> (SELECT NULL::bit)) t2;
 count 
-------
     4
(1 row)

DROP TABLE t;
-- varbit
CREATE TABLE t (val varbit(3));
CREATE INDEX ON t USING ivfflat (val bit_hamming_ops) WITH (lists = 1);
ERROR:  type not supported for ivfflat index
CREATE INDEX ON t USING ivfflat ((val::bit(3)) bit_hamming_ops) WITH (lists = 1);
NOTICE:  ivfflat index created with little data
DETAIL:  This will cause low recall.
HINT:  Drop the index until the table has more data.
CREATE INDEX ON t USING ivfflat ((val::bit(64001)) bit_hamming_ops) WITH (lists = 1);
ERROR:  column cannot have more than 64000 dimensions for ivfflat index
CREATE INDEX ON t USING ivfflat ((val::bit(2)) bit_hamming_ops) WITH (lists = 5);
NOTICE:  ivfflat index created with little data
DETAIL:  This will cause low recall.
HINT:  Drop the index until the table has more data.
DROP TABLE t;
```

## File: `test/expected/ivfflat_halfvec.out`
```
SET enable_seqscan = off;
-- L2
CREATE TABLE t (val halfvec(3));
INSERT INTO t (val) VALUES ('[0,0,0]'), ('[1,2,3]'), ('[1,1,1]'), (NULL);
CREATE INDEX ON t USING ivfflat (val halfvec_l2_ops) WITH (lists = 1);
INSERT INTO t (val) VALUES ('[1,2,4]');
SELECT * FROM t ORDER BY val <-> '[3,3,3]';
   val   
---------
 [1,2,3]
 [1,2,4]
 [1,1,1]
 [0,0,0]
(4 rows)

SELECT COUNT(*) FROM (SELECT * FROM t ORDER BY val <-> (SELECT NULL::halfvec)) t2;
 count 
-------
     4
(1 row)

SELECT COUNT(*) FROM t;
 count 
-------
     5
(1 row)

TRUNCATE t;
NOTICE:  ivfflat index created with little data
DETAIL:  This will cause low recall.
HINT:  Drop the index until the table has more data.
SELECT * FROM t ORDER BY val <-> '[3,3,3]';
 val 
-----
(0 rows)

DROP TABLE t;
-- inner product
CREATE TABLE t (val halfvec(3));
INSERT INTO t (val) VALUES ('[0,0,0]'), ('[1,2,3]'), ('[1,1,1]'), (NULL);
CREATE INDEX ON t USING ivfflat (val halfvec_ip_ops) WITH (lists = 1);
INSERT INTO t (val) VALUES ('[1,2,4]');
SELECT * FROM t ORDER BY val <#> '[3,3,3]';
   val   
---------
 [1,2,4]
 [1,2,3]
 [1,1,1]
 [0,0,0]
(4 rows)

SELECT COUNT(*) FROM (SELECT * FROM t ORDER BY val <#> (SELECT NULL::halfvec)) t2;
 count 
-------
     4
(1 row)

DROP TABLE t;
-- cosine
CREATE TABLE t (val halfvec(3));
INSERT INTO t (val) VALUES ('[0,0,0]'), ('[1,2,3]'), ('[1,1,1]'), (NULL);
CREATE INDEX ON t USING ivfflat (val halfvec_cosine_ops) WITH (lists = 1);
INSERT INTO t (val) VALUES ('[1,2,4]');
SELECT * FROM t ORDER BY val <=> '[3,3,3]';
   val   
---------
 [1,1,1]
 [1,2,3]
 [1,2,4]
(3 rows)

SELECT COUNT(*) FROM (SELECT * FROM t ORDER BY val <=> '[0,0,0]') t2;
 count 
-------
     3
(1 row)

SELECT COUNT(*) FROM (SELECT * FROM t ORDER BY val <=> (SELECT NULL::halfvec)) t2;
 count 
-------
     3
(1 row)

DROP TABLE t;
```

## File: `test/expected/ivfflat_vector.out`
```
SET enable_seqscan = off;
-- L2
CREATE TABLE t (val vector(3));
INSERT INTO t (val) VALUES ('[0,0,0]'), ('[1,2,3]'), ('[1,1,1]'), (NULL);
CREATE INDEX ON t USING ivfflat (val vector_l2_ops) WITH (lists = 1);
INSERT INTO t (val) VALUES ('[1,2,4]');
SELECT * FROM t ORDER BY val <-> '[3,3,3]';
   val   
---------
 [1,2,3]
 [1,2,4]
 [1,1,1]
 [0,0,0]
(4 rows)

SELECT COUNT(*) FROM (SELECT * FROM t ORDER BY val <-> (SELECT NULL::vector)) t2;
 count 
-------
     4
(1 row)

SELECT COUNT(*) FROM t;
 count 
-------
     5
(1 row)

TRUNCATE t;
NOTICE:  ivfflat index created with little data
DETAIL:  This will cause low recall.
HINT:  Drop the index until the table has more data.
SELECT * FROM t ORDER BY val <-> '[3,3,3]';
 val 
-----
(0 rows)

DROP TABLE t;
-- inner product
CREATE TABLE t (val vector(3));
INSERT INTO t (val) VALUES ('[0,0,0]'), ('[1,2,3]'), ('[1,1,1]'), (NULL);
CREATE INDEX ON t USING ivfflat (val vector_ip_ops) WITH (lists = 1);
INSERT INTO t (val) VALUES ('[1,2,4]');
SELECT * FROM t ORDER BY val <#> '[3,3,3]';
   val   
---------
 [1,2,4]
 [1,2,3]
 [1,1,1]
 [0,0,0]
(4 rows)

SELECT COUNT(*) FROM (SELECT * FROM t ORDER BY val <#> (SELECT NULL::vector)) t2;
 count 
-------
     4
(1 row)

DROP TABLE t;
-- cosine
CREATE TABLE t (val vector(3));
INSERT INTO t (val) VALUES ('[0,0,0]'), ('[1,2,3]'), ('[1,1,1]'), (NULL);
CREATE INDEX ON t USING ivfflat (val vector_cosine_ops) WITH (lists = 1);
INSERT INTO t (val) VALUES ('[1,2,4]');
SELECT * FROM t ORDER BY val <=> '[3,3,3]';
   val   
---------
 [1,1,1]
 [1,2,3]
 [1,2,4]
(3 rows)

SELECT COUNT(*) FROM (SELECT * FROM t ORDER BY val <=> '[0,0,0]') t2;
 count 
-------
     3
(1 row)

SELECT COUNT(*) FROM (SELECT * FROM t ORDER BY val <=> (SELECT NULL::vector)) t2;
 count 
-------
     3
(1 row)

DROP TABLE t;
-- iterative
CREATE TABLE t (val vector(3));
INSERT INTO t (val) VALUES ('[0,0,0]'), ('[1,2,3]'), ('[1,1,1]'), (NULL);
CREATE INDEX ON t USING ivfflat (val vector_l2_ops) WITH (lists = 3);
SET ivfflat.iterative_scan = relaxed_order;
SELECT * FROM t ORDER BY val <-> '[3,3,3]';
   val   
---------
 [1,2,3]
 [1,1,1]
 [0,0,0]
(3 rows)

SET ivfflat.max_probes = 1;
SELECT * FROM t ORDER BY val <-> '[3,3,3]';
   val   
---------
 [1,2,3]
(1 row)

SET ivfflat.max_probes = 2;
SELECT * FROM t ORDER BY val <-> '[3,3,3]';
   val   
---------
 [1,2,3]
 [1,1,1]
(2 rows)

TRUNCATE t;
NOTICE:  ivfflat index created with little data
DETAIL:  This will cause low recall.
HINT:  Drop the index until the table has more data.
SELECT * FROM t ORDER BY val <-> '[3,3,3]';
 val 
-----
(0 rows)

RESET ivfflat.iterative_scan;
RESET ivfflat.max_probes;
DROP TABLE t;
-- unlogged
CREATE UNLOGGED TABLE t (val vector(3));
INSERT INTO t (val) VALUES ('[0,0,0]'), ('[1,2,3]'), ('[1,1,1]'), (NULL);
CREATE INDEX ON t USING ivfflat (val vector_l2_ops) WITH (lists = 1);
SELECT * FROM t ORDER BY val <-> '[3,3,3]';
   val   
---------
 [1,2,3]
 [1,1,1]
 [0,0,0]
(3 rows)

DROP TABLE t;
-- options
CREATE TABLE t (val vector(3));
CREATE INDEX ON t USING ivfflat (val vector_l2_ops) WITH (lists = 0);
ERROR:  value 0 out of bounds for option "lists"
DETAIL:  Valid values are between "1" and "32768".
CREATE INDEX ON t USING ivfflat (val vector_l2_ops) WITH (lists = 32769);
ERROR:  value 32769 out of bounds for option "lists"
DETAIL:  Valid values are between "1" and "32768".
SHOW ivfflat.probes;
 ivfflat.probes 
----------------
 1
(1 row)

SET ivfflat.probes = 0;
ERROR:  0 is outside the valid range for parameter "ivfflat.probes" (1 .. 32768)
SET ivfflat.probes = 32769;
ERROR:  32769 is outside the valid range for parameter "ivfflat.probes" (1 .. 32768)
SHOW ivfflat.iterative_scan;
 ivfflat.iterative_scan 
------------------------
 off
(1 row)

SET ivfflat.iterative_scan = on;
ERROR:  invalid value for parameter "ivfflat.iterative_scan": "on"
HINT:  Available values: off, relaxed_order.
SHOW ivfflat.max_probes;
 ivfflat.max_probes 
--------------------
 32768
(1 row)

SET ivfflat.max_probes = 0;
ERROR:  0 is outside the valid range for parameter "ivfflat.max_probes" (1 .. 32768)
SET ivfflat.max_probes = 32769;
ERROR:  32769 is outside the valid range for parameter "ivfflat.max_probes" (1 .. 32768)
DROP TABLE t;
```

## File: `test/expected/sparsevec.out`
```
SELECT '{1:1.5,3:3.5}/5'::sparsevec;
    sparsevec    
-----------------
 {1:1.5,3:3.5}/5
(1 row)

SELECT '{1:-2,3:-4}/5'::sparsevec;
   sparsevec   
---------------
 {1:-2,3:-4}/5
(1 row)

SELECT '{1:2.,3:4.}/5'::sparsevec;
  sparsevec  
-------------
 {1:2,3:4}/5
(1 row)

SELECT ' { 1 : 1.5 ,  3  :  3.5  } / 5 '::sparsevec;
    sparsevec    
-----------------
 {1:1.5,3:3.5}/5
(1 row)

SELECT '{1:1.23456}/1'::sparsevec;
   sparsevec   
---------------
 {1:1.23456}/1
(1 row)

SELECT '{1:hello,2:1}/2'::sparsevec;
ERROR:  invalid input syntax for type sparsevec: "{1:hello,2:1}/2"
LINE 1: SELECT '{1:hello,2:1}/2'::sparsevec;
               ^
SELECT '{1:NaN,2:1}/2'::sparsevec;
ERROR:  NaN not allowed in sparsevec
LINE 1: SELECT '{1:NaN,2:1}/2'::sparsevec;
               ^
SELECT '{1:Infinity,2:1}/2'::sparsevec;
ERROR:  infinite value not allowed in sparsevec
LINE 1: SELECT '{1:Infinity,2:1}/2'::sparsevec;
               ^
SELECT '{1:-Infinity,2:1}/2'::sparsevec;
ERROR:  infinite value not allowed in sparsevec
LINE 1: SELECT '{1:-Infinity,2:1}/2'::sparsevec;
               ^
SELECT '{1:1.5e38,2:-1.5e38}/2'::sparsevec;
        sparsevec         
--------------------------
 {1:1.5e+38,2:-1.5e+38}/2
(1 row)

SELECT '{1:1.5e+38,2:-1.5e+38}/2'::sparsevec;
        sparsevec         
--------------------------
 {1:1.5e+38,2:-1.5e+38}/2
(1 row)

SELECT '{1:1.5e-38,2:-1.5e-38}/2'::sparsevec;
        sparsevec         
--------------------------
 {1:1.5e-38,2:-1.5e-38}/2
(1 row)

SELECT '{1:4e38,2:1}/2'::sparsevec;
ERROR:  "4e38" is out of range for type sparsevec
LINE 1: SELECT '{1:4e38,2:1}/2'::sparsevec;
               ^
SELECT '{1:-4e38,2:1}/2'::sparsevec;
ERROR:  "-4e38" is out of range for type sparsevec
LINE 1: SELECT '{1:-4e38,2:1}/2'::sparsevec;
               ^
SELECT '{1:1e-46,2:1}/2'::sparsevec;
ERROR:  "1e-46" is out of range for type sparsevec
LINE 1: SELECT '{1:1e-46,2:1}/2'::sparsevec;
               ^
SELECT '{1:-1e-46,2:1}/2'::sparsevec;
ERROR:  "-1e-46" is out of range for type sparsevec
LINE 1: SELECT '{1:-1e-46,2:1}/2'::sparsevec;
               ^
SELECT ''::sparsevec;
ERROR:  invalid input syntax for type sparsevec: ""
LINE 1: SELECT ''::sparsevec;
               ^
DETAIL:  Vector contents must start with "{".
SELECT '{'::sparsevec;
ERROR:  invalid input syntax for type sparsevec: "{"
LINE 1: SELECT '{'::sparsevec;
               ^
SELECT '{ '::sparsevec;
ERROR:  invalid input syntax for type sparsevec: "{ "
LINE 1: SELECT '{ '::sparsevec;
               ^
SELECT '{:'::sparsevec;
ERROR:  invalid input syntax for type sparsevec: "{:"
LINE 1: SELECT '{:'::sparsevec;
               ^
SELECT '{,'::sparsevec;
ERROR:  invalid input syntax for type sparsevec: "{,"
LINE 1: SELECT '{,'::sparsevec;
               ^
SELECT '{}'::sparsevec;
ERROR:  invalid input syntax for type sparsevec: "{}"
LINE 1: SELECT '{}'::sparsevec;
               ^
DETAIL:  Unexpected end of input.
SELECT '{}/'::sparsevec;
ERROR:  invalid input syntax for type sparsevec: "{}/"
LINE 1: SELECT '{}/'::sparsevec;
               ^
SELECT '{}/1'::sparsevec;
 sparsevec 
-----------
 {}/1
(1 row)

SELECT '{}/1a'::sparsevec;
ERROR:  invalid input syntax for type sparsevec: "{}/1a"
LINE 1: SELECT '{}/1a'::sparsevec;
               ^
DETAIL:  Junk after closing.
SELECT '{ }/1'::sparsevec;
 sparsevec 
-----------
 {}/1
(1 row)

SELECT '{:}/1'::sparsevec;
ERROR:  invalid input syntax for type sparsevec: "{:}/1"
LINE 1: SELECT '{:}/1'::sparsevec;
               ^
SELECT '{,}/1'::sparsevec;
ERROR:  invalid input syntax for type sparsevec: "{,}/1"
LINE 1: SELECT '{,}/1'::sparsevec;
               ^
SELECT '{1,}/1'::sparsevec;
ERROR:  invalid input syntax for type sparsevec: "{1,}/1"
LINE 1: SELECT '{1,}/1'::sparsevec;
               ^
SELECT '{:1}/1'::sparsevec;
ERROR:  invalid input syntax for type sparsevec: "{:1}/1"
LINE 1: SELECT '{:1}/1'::sparsevec;
               ^
SELECT '{1:}/1'::sparsevec;
ERROR:  invalid input syntax for type sparsevec: "{1:}/1"
LINE 1: SELECT '{1:}/1'::sparsevec;
               ^
SELECT '{1a:1}/1'::sparsevec;
ERROR:  invalid input syntax for type sparsevec: "{1a:1}/1"
LINE 1: SELECT '{1a:1}/1'::sparsevec;
               ^
SELECT '{1:1a}/1'::sparsevec;
ERROR:  invalid input syntax for type sparsevec: "{1:1a}/1"
LINE 1: SELECT '{1:1a}/1'::sparsevec;
               ^
SELECT '{1:1,}/1'::sparsevec;
ERROR:  invalid input syntax for type sparsevec: "{1:1,}/1"
LINE 1: SELECT '{1:1,}/1'::sparsevec;
               ^
SELECT '{1:0,2:1,3:0}/3'::sparsevec;
 sparsevec 
-----------
 {2:1}/3
(1 row)

SELECT '{2:1,1:1}/2'::sparsevec;
  sparsevec  
-------------
 {1:1,2:1}/2
(1 row)

SELECT '{1:1,1:1}/2'::sparsevec;
ERROR:  sparsevec indices must not contain duplicates
LINE 1: SELECT '{1:1,1:1}/2'::sparsevec;
               ^
SELECT '{1:1,2:1,1:1}/2'::sparsevec;
ERROR:  sparsevec indices must not contain duplicates
LINE 1: SELECT '{1:1,2:1,1:1}/2'::sparsevec;
               ^
SELECT '{}/5'::sparsevec;
 sparsevec 
-----------
 {}/5
(1 row)

SELECT '{}/-1'::sparsevec;
ERROR:  sparsevec must have at least 1 dimension
LINE 1: SELECT '{}/-1'::sparsevec;
               ^
SELECT '{}/1000000001'::sparsevec;
ERROR:  sparsevec cannot have more than 1000000000 dimensions
LINE 1: SELECT '{}/1000000001'::sparsevec;
               ^
SELECT '{}/2147483648'::sparsevec;
ERROR:  sparsevec cannot have more than 1000000000 dimensions
LINE 1: SELECT '{}/2147483648'::sparsevec;
               ^
SELECT '{}/-2147483649'::sparsevec;
ERROR:  sparsevec must have at least 1 dimension
LINE 1: SELECT '{}/-2147483649'::sparsevec;
               ^
SELECT '{}/9223372036854775808'::sparsevec;
ERROR:  sparsevec cannot have more than 1000000000 dimensions
LINE 1: SELECT '{}/9223372036854775808'::sparsevec;
               ^
SELECT '{}/-9223372036854775809'::sparsevec;
ERROR:  sparsevec must have at least 1 dimension
LINE 1: SELECT '{}/-9223372036854775809'::sparsevec;
               ^
SELECT '{2147483647:1}/1'::sparsevec;
ERROR:  sparsevec index out of bounds
LINE 1: SELECT '{2147483647:1}/1'::sparsevec;
               ^
SELECT '{2147483648:1}/1'::sparsevec;
ERROR:  sparsevec index out of bounds
LINE 1: SELECT '{2147483648:1}/1'::sparsevec;
               ^
SELECT '{-2147483648:1}/1'::sparsevec;
ERROR:  sparsevec index out of bounds
LINE 1: SELECT '{-2147483648:1}/1'::sparsevec;
               ^
SELECT '{-2147483649:1}/1'::sparsevec;
ERROR:  sparsevec index out of bounds
LINE 1: SELECT '{-2147483649:1}/1'::sparsevec;
               ^
SELECT '{0:1}/1'::sparsevec;
ERROR:  sparsevec index out of bounds
LINE 1: SELECT '{0:1}/1'::sparsevec;
               ^
SELECT '{2:1}/1'::sparsevec;
ERROR:  sparsevec index out of bounds
LINE 1: SELECT '{2:1}/1'::sparsevec;
               ^
SELECT '{}/3'::sparsevec(3);
 sparsevec 
-----------
 {}/3
(1 row)

SELECT '{}/3'::sparsevec(2);
ERROR:  expected 2 dimensions, not 3
SELECT '{}/3'::sparsevec(3, 2);
ERROR:  invalid type modifier
LINE 1: SELECT '{}/3'::sparsevec(3, 2);
                       ^
SELECT '{}/3'::sparsevec('a');
ERROR:  invalid input syntax for type integer: "a"
LINE 1: SELECT '{}/3'::sparsevec('a');
                       ^
SELECT '{}/3'::sparsevec(0);
ERROR:  dimensions for type sparsevec must be at least 1
LINE 1: SELECT '{}/3'::sparsevec(0);
                       ^
SELECT '{}/3'::sparsevec(1000000001);
ERROR:  dimensions for type sparsevec cannot exceed 1000000000
LINE 1: SELECT '{}/3'::sparsevec(1000000001);
                       ^
SELECT '{1:1,2:2,3:3}/3'::sparsevec < '{1:1,2:2,3:3}/3';
 ?column? 
----------
 f
(1 row)

SELECT '{1:1,2:2,3:3}/3'::sparsevec < '{1:1,2:2}/2';
 ?column? 
----------
 f
(1 row)

SELECT '{1:1,2:2,3:3}/3'::sparsevec <= '{1:1,2:2,3:3}/3';
 ?column? 
----------
 t
(1 row)

SELECT '{1:1,2:2,3:3}/3'::sparsevec <= '{1:1,2:2}/2';
 ?column? 
----------
 f
(1 row)

SELECT '{1:1,2:2,3:3}/3'::sparsevec = '{1:1,2:2,3:3}/3';
 ?column? 
----------
 t
(1 row)

SELECT '{1:1,2:2,3:3}/3'::sparsevec = '{1:1,2:2}/2';
 ?column? 
----------
 f
(1 row)

SELECT '{1:1,2:2,3:3}/3'::sparsevec != '{1:1,2:2,3:3}/3';
 ?column? 
----------
 f
(1 row)

SELECT '{1:1,2:2,3:3}/3'::sparsevec != '{1:1,2:2}/2';
 ?column? 
----------
 t
(1 row)

SELECT '{1:1,2:2,3:3}/3'::sparsevec >= '{1:1,2:2,3:3}/3';
 ?column? 
----------
 t
(1 row)

SELECT '{1:1,2:2,3:3}/3'::sparsevec >= '{1:1,2:2}/2';
 ?column? 
----------
 t
(1 row)

SELECT '{1:1,2:2,3:3}/3'::sparsevec > '{1:1,2:2,3:3}/3';
 ?column? 
----------
 f
(1 row)

SELECT '{1:1,2:2,3:3}/3'::sparsevec > '{1:1,2:2}/2';
 ?column? 
----------
 t
(1 row)

SELECT sparsevec_cmp('{1:1,2:2,3:3}/3', '{1:1,2:2,3:3}/3');
 sparsevec_cmp 
---------------
             0
(1 row)

SELECT sparsevec_cmp('{1:1,2:2,3:3}/3', '{}/3');
 sparsevec_cmp 
---------------
             1
(1 row)

SELECT sparsevec_cmp('{}/3', '{1:1,2:2,3:3}/3');
 sparsevec_cmp 
---------------
            -1
(1 row)

SELECT sparsevec_cmp('{1:1,2:2}/2', '{1:1,2:2,3:3}/3');
 sparsevec_cmp 
---------------
            -1
(1 row)

SELECT sparsevec_cmp('{1:1,2:2,3:3}/3', '{1:1,2:2}/2');
 sparsevec_cmp 
---------------
             1
(1 row)

SELECT sparsevec_cmp('{1:1,2:2}/2', '{1:2,2:3,3:4}/3');
 sparsevec_cmp 
---------------
            -1
(1 row)

SELECT sparsevec_cmp('{1:2,2:3}/2', '{1:1,2:2,3:3}/3');
 sparsevec_cmp 
---------------
             1
(1 row)

SELECT round(l2_norm('{1:1,2:1}/2'::sparsevec)::numeric, 5);
  round  
---------
 1.41421
(1 row)

SELECT l2_norm('{1:3,2:4}/2'::sparsevec);
 l2_norm 
---------
       5
(1 row)

SELECT l2_norm('{2:1}/2'::sparsevec);
 l2_norm 
---------
       1
(1 row)

SELECT l2_norm('{1:3e37,2:4e37}/2'::sparsevec)::real;
 l2_norm 
---------
   5e+37
(1 row)

SELECT l2_norm('{}/2'::sparsevec);
 l2_norm 
---------
       0
(1 row)

SELECT l2_norm('{1:2}/1'::sparsevec);
 l2_norm 
---------
       2
(1 row)

SELECT l2_distance('{}/2'::sparsevec, '{1:3,2:4}/2');
 l2_distance 
-------------
           5
(1 row)

SELECT l2_distance('{1:3}/2'::sparsevec, '{2:4}/2');
 l2_distance 
-------------
           5
(1 row)

SELECT l2_distance('{2:4}/2'::sparsevec, '{1:3}/2');
 l2_distance 
-------------
           5
(1 row)

SELECT l2_distance('{1:3,2:4}/2'::sparsevec, '{}/2');
 l2_distance 
-------------
           5
(1 row)

SELECT l2_distance('{}/2'::sparsevec, '{2:1}/2');
 l2_distance 
-------------
           1
(1 row)

SELECT '{}/2'::sparsevec <-> '{1:3,2:4}/2';
 ?column? 
----------
        5
(1 row)

SELECT inner_product('{1:1,2:2}/2'::sparsevec, '{1:2,2:4}/2');
 inner_product 
---------------
            10
(1 row)

SELECT inner_product('{1:1,2:2}/2'::sparsevec, '{1:3}/1');
ERROR:  different sparsevec dimensions 2 and 1
SELECT inner_product('{1:1,3:3}/4'::sparsevec, '{2:2,4:4}/4');
 inner_product 
---------------
             0
(1 row)

SELECT inner_product('{2:2,4:4}/4'::sparsevec, '{1:1,3:3}/4');
 inner_product 
---------------
             0
(1 row)

SELECT inner_product('{1:1,3:3,5:5}/5'::sparsevec, '{2:4,3:6,4:8}/5');
 inner_product 
---------------
            18
(1 row)

SELECT inner_product('{1:1}/2'::sparsevec, '{}/2');
 inner_product 
---------------
             0
(1 row)

SELECT inner_product('{}/2'::sparsevec, '{1:1}/2');
 inner_product 
---------------
             0
(1 row)

SELECT inner_product('{1:3e38}/1'::sparsevec, '{1:3e38}/1');
 inner_product 
---------------
      Infinity
(1 row)

SELECT inner_product('{1:1,3:3,5:5}/5'::sparsevec, '{2:4,3:6,4:8}/5');
 inner_product 
---------------
            18
(1 row)

SELECT '{1:1,2:2}/2'::sparsevec <#> '{1:3,2:4}/2';
 ?column? 
----------
      -11
(1 row)

SELECT cosine_distance('{1:1,2:2}/2'::sparsevec, '{1:2,2:4}/2');
 cosine_distance 
-----------------
               0
(1 row)

SELECT cosine_distance('{1:1,2:2}/2'::sparsevec, '{}/2');
 cosine_distance 
-----------------
             NaN
(1 row)

SELECT cosine_distance('{1:1,2:1}/2'::sparsevec, '{1:1,2:1}/2');
 cosine_distance 
-----------------
               0
(1 row)

SELECT cosine_distance('{1:1}/2'::sparsevec, '{2:2}/2');
 cosine_distance 
-----------------
               1
(1 row)

SELECT cosine_distance('{1:1,2:1}/2'::sparsevec, '{1:-1,2:-1}/2');
 cosine_distance 
-----------------
               2
(1 row)

SELECT cosine_distance('{1:2}/2'::sparsevec, '{2:2}/2');
 cosine_distance 
-----------------
               1
(1 row)

SELECT cosine_distance('{2:2}/2'::sparsevec, '{1:2}/2');
 cosine_distance 
-----------------
               1
(1 row)

SELECT cosine_distance('{1:1,2:2}/2'::sparsevec, '{1:3}/1');
ERROR:  different sparsevec dimensions 2 and 1
SELECT cosine_distance('{1:1,2:1}/2'::sparsevec, '{1:1.1,2:1.1}/2');
 cosine_distance 
-----------------
               0
(1 row)

SELECT cosine_distance('{1:1,2:1}/2'::sparsevec, '{1:-1.1,2:-1.1}/2');
 cosine_distance 
-----------------
               2
(1 row)

SELECT cosine_distance('{1:3e38}/1'::sparsevec, '{1:3e38}/1');
 cosine_distance 
-----------------
             NaN
(1 row)

SELECT cosine_distance('{}/1'::sparsevec, '{}/1');
 cosine_distance 
-----------------
             NaN
(1 row)

SELECT '{1:1,2:2}/2'::sparsevec <=> '{1:2,2:4}/2';
 ?column? 
----------
        0
(1 row)

SELECT l1_distance('{}/2'::sparsevec, '{1:3,2:4}/2');
 l1_distance 
-------------
           7
(1 row)

SELECT l1_distance('{}/2'::sparsevec, '{2:1}/2');
 l1_distance 
-------------
           1
(1 row)

SELECT l1_distance('{1:1,2:2}/2'::sparsevec, '{1:3}/1');
ERROR:  different sparsevec dimensions 2 and 1
SELECT l1_distance('{1:3e38}/1'::sparsevec, '{1:-3e38}/1');
 l1_distance 
-------------
    Infinity
(1 row)

SELECT l1_distance('{1:1,3:3,5:5,7:7}/8'::sparsevec, '{2:2,4:4,6:6,8:8}/8');
 l1_distance 
-------------
          36
(1 row)

SELECT l1_distance('{1:1,3:3,5:5,7:7,9:9}/9'::sparsevec, '{2:2,4:4,6:6,8:8}/9');
 l1_distance 
-------------
          45
(1 row)

SELECT '{}/2'::sparsevec <+> '{1:3,2:4}/2';
 ?column? 
----------
        7
(1 row)

SELECT l2_normalize('{1:3,2:4}/2'::sparsevec);
  l2_normalize   
-----------------
 {1:0.6,2:0.8}/2
(1 row)

SELECT l2_normalize('{1:3}/2'::sparsevec);
 l2_normalize 
--------------
 {1:1}/2
(1 row)

SELECT l2_normalize('{2:0.1}/2'::sparsevec);
 l2_normalize 
--------------
 {2:1}/2
(1 row)

SELECT l2_normalize('{}/2'::sparsevec);
 l2_normalize 
--------------
 {}/2
(1 row)

SELECT l2_normalize('{1:3e38}/1'::sparsevec);
 l2_normalize 
--------------
 {1:1}/1
(1 row)

SELECT l2_normalize('{1:3e38,2:1e-37}/2'::sparsevec);
 l2_normalize 
--------------
 {1:1}/2
(1 row)

SELECT l2_normalize('{2:3e37,4:3e-37,6:4e37,8:4e-37}/9'::sparsevec);
  l2_normalize   
-----------------
 {2:0.6,6:0.8}/9
(1 row)

```

## File: `test/expected/vector_type.out`
```
SELECT '[1,2,3]'::vector;
 vector  
---------
 [1,2,3]
(1 row)

SELECT '[-1,-2,-3]'::vector;
   vector   
------------
 [-1,-2,-3]
(1 row)

SELECT '[1.,2.,3.]'::vector;
 vector  
---------
 [1,2,3]
(1 row)

SELECT ' [ 1,  2 ,    3  ] '::vector;
 vector  
---------
 [1,2,3]
(1 row)

SELECT '[1.23456]'::vector;
  vector   
-----------
 [1.23456]
(1 row)

SELECT '[hello,1]'::vector;
ERROR:  invalid input syntax for type vector: "[hello,1]"
LINE 1: SELECT '[hello,1]'::vector;
               ^
SELECT '[NaN,1]'::vector;
ERROR:  NaN not allowed in vector
LINE 1: SELECT '[NaN,1]'::vector;
               ^
SELECT '[Infinity,1]'::vector;
ERROR:  infinite value not allowed in vector
LINE 1: SELECT '[Infinity,1]'::vector;
               ^
SELECT '[-Infinity,1]'::vector;
ERROR:  infinite value not allowed in vector
LINE 1: SELECT '[-Infinity,1]'::vector;
               ^
SELECT '[1.5e38,-1.5e38]'::vector;
       vector       
--------------------
 [1.5e+38,-1.5e+38]
(1 row)

SELECT '[1.5e+38,-1.5e+38]'::vector;
       vector       
--------------------
 [1.5e+38,-1.5e+38]
(1 row)

SELECT '[1.5e-38,-1.5e-38]'::vector;
       vector       
--------------------
 [1.5e-38,-1.5e-38]
(1 row)

SELECT '[4e38,1]'::vector;
ERROR:  "4e38" is out of range for type vector
LINE 1: SELECT '[4e38,1]'::vector;
               ^
SELECT '[-4e38,1]'::vector;
ERROR:  "-4e38" is out of range for type vector
LINE 1: SELECT '[-4e38,1]'::vector;
               ^
SELECT '[1e-46,1]'::vector;
 vector 
--------
 [0,1]
(1 row)

SELECT '[-1e-46,1]'::vector;
 vector 
--------
 [-0,1]
(1 row)

SELECT '[1,2,3'::vector;
ERROR:  invalid input syntax for type vector: "[1,2,3"
LINE 1: SELECT '[1,2,3'::vector;
               ^
SELECT '[1,2,3]9'::vector;
ERROR:  invalid input syntax for type vector: "[1,2,3]9"
LINE 1: SELECT '[1,2,3]9'::vector;
               ^
DETAIL:  Junk after closing right brace.
SELECT '1,2,3'::vector;
ERROR:  invalid input syntax for type vector: "1,2,3"
LINE 1: SELECT '1,2,3'::vector;
               ^
DETAIL:  Vector contents must start with "[".
SELECT ''::vector;
ERROR:  invalid input syntax for type vector: ""
LINE 1: SELECT ''::vector;
               ^
DETAIL:  Vector contents must start with "[".
SELECT '['::vector;
ERROR:  invalid input syntax for type vector: "["
LINE 1: SELECT '['::vector;
               ^
SELECT '[ '::vector;
ERROR:  invalid input syntax for type vector: "[ "
LINE 1: SELECT '[ '::vector;
               ^
SELECT '[,'::vector;
ERROR:  invalid input syntax for type vector: "[,"
LINE 1: SELECT '[,'::vector;
               ^
SELECT '[]'::vector;
ERROR:  vector must have at least 1 dimension
LINE 1: SELECT '[]'::vector;
               ^
SELECT '[ ]'::vector;
ERROR:  vector must have at least 1 dimension
LINE 1: SELECT '[ ]'::vector;
               ^
SELECT '[,]'::vector;
ERROR:  invalid input syntax for type vector: "[,]"
LINE 1: SELECT '[,]'::vector;
               ^
SELECT '[1,]'::vector;
ERROR:  invalid input syntax for type vector: "[1,]"
LINE 1: SELECT '[1,]'::vector;
               ^
SELECT '[1a]'::vector;
ERROR:  invalid input syntax for type vector: "[1a]"
LINE 1: SELECT '[1a]'::vector;
               ^
SELECT '[1,,3]'::vector;
ERROR:  invalid input syntax for type vector: "[1,,3]"
LINE 1: SELECT '[1,,3]'::vector;
               ^
SELECT '[1, ,3]'::vector;
ERROR:  invalid input syntax for type vector: "[1, ,3]"
LINE 1: SELECT '[1, ,3]'::vector;
               ^
SELECT '[1,2,3]'::vector(3);
 vector  
---------
 [1,2,3]
(1 row)

SELECT '[1,2,3]'::vector(2);
ERROR:  expected 2 dimensions, not 3
SELECT '[1,2,3]'::vector(3, 2);
ERROR:  invalid type modifier
LINE 1: SELECT '[1,2,3]'::vector(3, 2);
                          ^
SELECT '[1,2,3]'::vector('a');
ERROR:  invalid input syntax for type integer: "a"
LINE 1: SELECT '[1,2,3]'::vector('a');
                          ^
SELECT '[1,2,3]'::vector(0);
ERROR:  dimensions for type vector must be at least 1
LINE 1: SELECT '[1,2,3]'::vector(0);
                          ^
SELECT '[1,2,3]'::vector(16001);
ERROR:  dimensions for type vector cannot exceed 16000
LINE 1: SELECT '[1,2,3]'::vector(16001);
                          ^
SELECT unnest('{"[1,2,3]", "[4,5,6]"}'::vector[]);
 unnest  
---------
 [1,2,3]
 [4,5,6]
(2 rows)

SELECT '{"[1,2,3]"}'::vector(2)[];
ERROR:  expected 2 dimensions, not 3
SELECT '[1,2,3]'::vector + '[4,5,6]';
 ?column? 
----------
 [5,7,9]
(1 row)

SELECT '[3e38]'::vector + '[3e38]';
ERROR:  value out of range: overflow
SELECT '[1,2]'::vector + '[3]';
ERROR:  different vector dimensions 2 and 1
SELECT '[1,2,3]'::vector - '[4,5,6]';
  ?column?  
------------
 [-3,-3,-3]
(1 row)

SELECT '[-3e38]'::vector - '[3e38]';
ERROR:  value out of range: overflow
SELECT '[1,2]'::vector - '[3]';
ERROR:  different vector dimensions 2 and 1
SELECT '[1,2,3]'::vector * '[4,5,6]';
 ?column?  
-----------
 [4,10,18]
(1 row)

SELECT '[1e37]'::vector * '[1e37]';
ERROR:  value out of range: overflow
SELECT '[1e-37]'::vector * '[1e-37]';
ERROR:  value out of range: underflow
SELECT '[1,2]'::vector * '[3]';
ERROR:  different vector dimensions 2 and 1
SELECT '[1,2,3]'::vector || '[4,5]';
  ?column?   
-------------
 [1,2,3,4,5]
(1 row)

SELECT array_fill(0, ARRAY[16000])::vector || '[1]';
ERROR:  vector cannot have more than 16000 dimensions
SELECT '[1,2,3]'::vector < '[1,2,3]';
 ?column? 
----------
 f
(1 row)

SELECT '[1,2,3]'::vector < '[1,2]';
 ?column? 
----------
 f
(1 row)

SELECT '[1,2,3]'::vector <= '[1,2,3]';
 ?column? 
----------
 t
(1 row)

SELECT '[1,2,3]'::vector <= '[1,2]';
 ?column? 
----------
 f
(1 row)

SELECT '[1,2,3]'::vector = '[1,2,3]';
 ?column? 
----------
 t
(1 row)

SELECT '[1,2,3]'::vector = '[1,2]';
 ?column? 
----------
 f
(1 row)

SELECT '[1,2,3]'::vector != '[1,2,3]';
 ?column? 
----------
 f
(1 row)

SELECT '[1,2,3]'::vector != '[1,2]';
 ?column? 
----------
 t
(1 row)

SELECT '[1,2,3]'::vector >= '[1,2,3]';
 ?column? 
----------
 t
(1 row)

SELECT '[1,2,3]'::vector >= '[1,2]';
 ?column? 
----------
 t
(1 row)

SELECT '[1,2,3]'::vector > '[1,2,3]';
 ?column? 
----------
 f
(1 row)

SELECT '[1,2,3]'::vector > '[1,2]';
 ?column? 
----------
 t
(1 row)

SELECT vector_cmp('[1,2,3]', '[1,2,3]');
 vector_cmp 
------------
          0
(1 row)

SELECT vector_cmp('[1,2,3]', '[0,0,0]');
 vector_cmp 
------------
          1
(1 row)

SELECT vector_cmp('[0,0,0]', '[1,2,3]');
 vector_cmp 
------------
         -1
(1 row)

SELECT vector_cmp('[1,2]', '[1,2,3]');
 vector_cmp 
------------
         -1
(1 row)

SELECT vector_cmp('[1,2,3]', '[1,2]');
 vector_cmp 
------------
          1
(1 row)

SELECT vector_cmp('[1,2]', '[2,3,4]');
 vector_cmp 
------------
         -1
(1 row)

SELECT vector_cmp('[2,3]', '[1,2,3]');
 vector_cmp 
------------
          1
(1 row)

SELECT vector_dims('[1,2,3]'::vector);
 vector_dims 
-------------
           3
(1 row)

SELECT round(vector_norm('[1,1]')::numeric, 5);
  round  
---------
 1.41421
(1 row)

SELECT vector_norm('[3,4]');
 vector_norm 
-------------
           5
(1 row)

SELECT vector_norm('[0,1]');
 vector_norm 
-------------
           1
(1 row)

SELECT vector_norm('[3e37,4e37]')::real;
 vector_norm 
-------------
       5e+37
(1 row)

SELECT vector_norm('[0,0]');
 vector_norm 
-------------
           0
(1 row)

SELECT vector_norm('[2]');
 vector_norm 
-------------
           2
(1 row)

SELECT l2_distance('[0,0]'::vector, '[3,4]');
 l2_distance 
-------------
           5
(1 row)

SELECT l2_distance('[0,0]'::vector, '[0,1]');
 l2_distance 
-------------
           1
(1 row)

SELECT l2_distance('[1,2]'::vector, '[3]');
ERROR:  different vector dimensions 2 and 1
SELECT l2_distance('[3e38]'::vector, '[-3e38]');
 l2_distance 
-------------
    Infinity
(1 row)

SELECT l2_distance('[1,1,1,1,1,1,1,1,1]'::vector, '[1,1,1,1,1,1,1,4,5]');
 l2_distance 
-------------
           5
(1 row)

SELECT '[0,0]'::vector <-> '[3,4]';
 ?column? 
----------
        5
(1 row)

SELECT inner_product('[1,2]'::vector, '[3,4]');
 inner_product 
---------------
            11
(1 row)

SELECT inner_product('[1,2]'::vector, '[3]');
ERROR:  different vector dimensions 2 and 1
SELECT inner_product('[3e38]'::vector, '[3e38]');
 inner_product 
---------------
      Infinity
(1 row)

SELECT inner_product('[1,1,1,1,1,1,1,1,1]'::vector, '[1,2,3,4,5,6,7,8,9]');
 inner_product 
---------------
            45
(1 row)

SELECT '[1,2]'::vector <#> '[3,4]';
 ?column? 
----------
      -11
(1 row)

SELECT cosine_distance('[1,2]'::vector, '[2,4]');
 cosine_distance 
-----------------
               0
(1 row)

SELECT cosine_distance('[1,2]'::vector, '[0,0]');
 cosine_distance 
-----------------
             NaN
(1 row)

SELECT cosine_distance('[1,1]'::vector, '[1,1]');
 cosine_distance 
-----------------
               0
(1 row)

SELECT cosine_distance('[1,0]'::vector, '[0,2]');
 cosine_distance 
-----------------
               1
(1 row)

SELECT cosine_distance('[1,1]'::vector, '[-1,-1]');
 cosine_distance 
-----------------
               2
(1 row)

SELECT cosine_distance('[1,2]'::vector, '[3]');
ERROR:  different vector dimensions 2 and 1
SELECT cosine_distance('[1,1]'::vector, '[1.1,1.1]');
 cosine_distance 
-----------------
               0
(1 row)

SELECT cosine_distance('[1,1]'::vector, '[-1.1,-1.1]');
 cosine_distance 
-----------------
               2
(1 row)

SELECT cosine_distance('[3e38]'::vector, '[3e38]');
 cosine_distance 
-----------------
             NaN
(1 row)

SELECT cosine_distance('[1,2,3,4,5,6,7,8,9]'::vector, '[1,2,3,4,5,6,7,8,9]');
 cosine_distance 
-----------------
               0
(1 row)

SELECT cosine_distance('[1,2,3,4,5,6,7,8,9]'::vector, '[-1,-2,-3,-4,-5,-6,-7,-8,-9]');
 cosine_distance 
-----------------
               2
(1 row)

SELECT '[1,2]'::vector <=> '[2,4]';
 ?column? 
----------
        0
(1 row)

SELECT l1_distance('[0,0]'::vector, '[3,4]');
 l1_distance 
-------------
           7
(1 row)

SELECT l1_distance('[0,0]'::vector, '[0,1]');
 l1_distance 
-------------
           1
(1 row)

SELECT l1_distance('[1,2]'::vector, '[3]');
ERROR:  different vector dimensions 2 and 1
SELECT l1_distance('[3e38]'::vector, '[-3e38]');
 l1_distance 
-------------
    Infinity
(1 row)

SELECT l1_distance('[1,2,3,4,5,6,7,8,9]'::vector, '[1,2,3,4,5,6,7,8,9]');
 l1_distance 
-------------
           0
(1 row)

SELECT l1_distance('[1,2,3,4,5,6,7,8,9]'::vector, '[0,3,2,5,4,7,6,9,8]');
 l1_distance 
-------------
           9
(1 row)

SELECT '[0,0]'::vector <+> '[3,4]';
 ?column? 
----------
        7
(1 row)

SELECT l2_normalize('[3,4]'::vector);
 l2_normalize 
--------------
 [0.6,0.8]
(1 row)

SELECT l2_normalize('[3,0]'::vector);
 l2_normalize 
--------------
 [1,0]
(1 row)

SELECT l2_normalize('[0,0.1]'::vector);
 l2_normalize 
--------------
 [0,1]
(1 row)

SELECT l2_normalize('[0,0]'::vector);
 l2_normalize 
--------------
 [0,0]
(1 row)

SELECT l2_normalize('[3e38]'::vector);
 l2_normalize 
--------------
 [1]
(1 row)

SELECT binary_quantize('[1,0,-1]'::vector);
 binary_quantize 
-----------------
 100
(1 row)

SELECT binary_quantize('[0,0.1,-0.2,-0.3,0.4,0.5,0.6,-0.7,0.8,-0.9,1]'::vector);
 binary_quantize 
-----------------
 01001110101
(1 row)

SELECT binary_quantize('[1,2,3,-4,5,6,-7,8,1,-2,-3,4,5,-6,7,8,-1,2,3]'::vector);
   binary_quantize   
---------------------
 1110110110011011011
(1 row)

SELECT subvector('[1,2,3,4,5]'::vector, 1, 3);
 subvector 
-----------
 [1,2,3]
(1 row)

SELECT subvector('[1,2,3,4,5]'::vector, 3, 2);
 subvector 
-----------
 [3,4]
(1 row)

SELECT subvector('[1,2,3,4,5]'::vector, -1, 3);
 subvector 
-----------
 [1]
(1 row)

SELECT subvector('[1,2,3,4,5]'::vector, 3, 9);
 subvector 
-----------
 [3,4,5]
(1 row)

SELECT subvector('[1,2,3,4,5]'::vector, 1, 0);
ERROR:  vector must have at least 1 dimension
SELECT subvector('[1,2,3,4,5]'::vector, 3, -1);
ERROR:  vector must have at least 1 dimension
SELECT subvector('[1,2,3,4,5]'::vector, -1, 2);
ERROR:  vector must have at least 1 dimension
SELECT subvector('[1,2,3,4,5]'::vector, 2147483647, 10);
ERROR:  vector must have at least 1 dimension
SELECT subvector('[1,2,3,4,5]'::vector, 3, 2147483647);
 subvector 
-----------
 [3,4,5]
(1 row)

SELECT subvector('[1,2,3,4,5]'::vector, -2147483644, 2147483647);
 subvector 
-----------
 [1,2]
(1 row)

SELECT avg(v) FROM unnest(ARRAY['[1,2,3]'::vector, '[3,5,7]']) v;
    avg    
-----------
 [2,3.5,5]
(1 row)

SELECT avg(v) FROM unnest(ARRAY['[1,2,3]'::vector, '[3,5,7]', NULL]) v;
    avg    
-----------
 [2,3.5,5]
(1 row)

SELECT avg(v) FROM unnest(ARRAY[]::vector[]) v;
 avg 
-----
 
(1 row)

SELECT avg(v) FROM unnest(ARRAY['[1,2]'::vector, '[3]']) v;
ERROR:  expected 2 dimensions, not 1
SELECT avg(v) FROM unnest(ARRAY['[3e38]'::vector, '[3e38]']) v;
   avg   
---------
 [3e+38]
(1 row)

SELECT vector_avg(array_agg(n)) FROM generate_series(1, 16002) n;
ERROR:  vector cannot have more than 16000 dimensions
SELECT sum(v) FROM unnest(ARRAY['[1,2,3]'::vector, '[3,5,7]']) v;
   sum    
----------
 [4,7,10]
(1 row)

SELECT sum(v) FROM unnest(ARRAY['[1,2,3]'::vector, '[3,5,7]', NULL]) v;
   sum    
----------
 [4,7,10]
(1 row)

SELECT sum(v) FROM unnest(ARRAY[]::vector[]) v;
 sum 
-----
 
(1 row)

SELECT sum(v) FROM unnest(ARRAY['[1,2]'::vector, '[3]']) v;
ERROR:  different vector dimensions 2 and 1
SELECT sum(v) FROM unnest(ARRAY['[3e38]'::vector, '[3e38]']) v;
ERROR:  value out of range: overflow
```

## File: `test/perl/PostgreSQL/Test/Cluster.pm`
```
package PostgreSQL::Test::Cluster;

use PostgresNode;

sub new
{
	my ($class, $name) = @_;
	return get_new_node($name);
}

1;
```

## File: `test/perl/PostgreSQL/Test/Utils.pm`
```
package PostgreSQL::Test::Utils;

use TestLib;

1;
```

## File: `test/sql/bit.sql`
```sql
SELECT hamming_distance('111', '111');
SELECT hamming_distance('111', '110');
SELECT hamming_distance('111', '100');
SELECT hamming_distance('111', '000');
SELECT hamming_distance('10101010101010101010', '01010101010101010101');
SELECT hamming_distance('101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101', '101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101');
SELECT hamming_distance('101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101', '010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010');
SELECT hamming_distance('110000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000011', '100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001');
SELECT hamming_distance('', '');
SELECT hamming_distance('111', '00');
SELECT hamming_distance('111', '000'::varbit(4));
SELECT hamming_distance('111', '0000'::varbit(4));

SELECT jaccard_distance('1111', '1111');
SELECT jaccard_distance('1111', '1110');
SELECT jaccard_distance('1111', '1100');
SELECT jaccard_distance('1111', '1000');
SELECT jaccard_distance('1111', '0000');
SELECT jaccard_distance('1100', '1000');
SELECT jaccard_distance('10101010101010101010', '01010101010101010101');
SELECT jaccard_distance('101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101', '101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101');
SELECT jaccard_distance('101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101', '010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010');
SELECT jaccard_distance('110000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000011', '100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001');
SELECT jaccard_distance('', '');
SELECT jaccard_distance('1111', '000');
SELECT jaccard_distance('1111', '0000'::varbit(5));
SELECT jaccard_distance('1111', '00000'::varbit(5));
```

## File: `test/sql/btree.sql`
```sql
SET enable_seqscan = off;

-- vector

CREATE TABLE t (val vector(3));
INSERT INTO t (val) VALUES ('[0,0,0]'), ('[1,2,3]'), ('[1,1,1]'), (NULL);
CREATE INDEX ON t (val);

SELECT * FROM t WHERE val = '[1,2,3]';
SELECT * FROM t ORDER BY val;

DROP TABLE t;

-- halfvec

CREATE TABLE t (val halfvec(3));
INSERT INTO t (val) VALUES ('[0,0,0]'), ('[1,2,3]'), ('[1,1,1]'), (NULL);
CREATE INDEX ON t (val);

SELECT * FROM t WHERE val = '[1,2,3]';
SELECT * FROM t ORDER BY val;

DROP TABLE t;

-- sparsevec

CREATE TABLE t (val sparsevec(3));
INSERT INTO t (val) VALUES ('{}/3'), ('{1:1,2:2,3:3}/3'), ('{1:1,2:1,3:1}/3'), (NULL);
CREATE INDEX ON t (val);

SELECT * FROM t WHERE val = '{1:1,2:2,3:3}/3';
SELECT * FROM t ORDER BY val;

DROP TABLE t;
```

## File: `test/sql/cast.sql`
```sql
SELECT ARRAY[1,2,3]::vector;
SELECT ARRAY[1.0,2.0,3.0]::vector;
SELECT ARRAY[1,2,3]::float4[]::vector;
SELECT ARRAY[1,2,3]::float8[]::vector;
SELECT ARRAY[1,2,3]::numeric[]::vector;

SELECT '[1,2,3]'::vector::real[];

SELECT '{1,2,3}'::real[]::vector;
SELECT '{1,2,3}'::real[]::vector(3);
SELECT '{1,2,3}'::real[]::vector(2);
SELECT '{NULL}'::real[]::vector;
SELECT '{NaN}'::real[]::vector;
SELECT '{Infinity}'::real[]::vector;
SELECT '{-Infinity}'::real[]::vector;
SELECT '{}'::real[]::vector;
SELECT '{{1}}'::real[]::vector;

SELECT '{1,2,3}'::double precision[]::vector;
SELECT '{1,2,3}'::double precision[]::vector(3);
SELECT '{1,2,3}'::double precision[]::vector(2);
SELECT '{4e38,-4e38}'::double precision[]::vector;
SELECT '{1e-46,-1e-46}'::double precision[]::vector;

SELECT '[1,2,3]'::vector::halfvec;
SELECT '[1,2,3]'::vector::halfvec(3);
SELECT '[1,2,3]'::vector::halfvec(2);
SELECT '[65520]'::vector::halfvec;
SELECT '[1e-8]'::vector::halfvec;

SELECT '[1,2,3]'::halfvec::vector;
SELECT '[1,2,3]'::halfvec::vector(3);
SELECT '[1,2,3]'::halfvec::vector(2);

SELECT '{1,2,3}'::real[]::halfvec;
SELECT '{1,2,3}'::real[]::halfvec(3);
SELECT '{1,2,3}'::real[]::halfvec(2);
SELECT '{65520,-65520}'::real[]::halfvec;
SELECT '{1e-8,-1e-8}'::real[]::halfvec;

SELECT '[0,1.5,0,3.5,0]'::vector::sparsevec;
SELECT '[0,1.5,0,3.5,0]'::vector::sparsevec(5);
SELECT '[0,1.5,0,3.5,0]'::vector::sparsevec(4);

SELECT '{2:1.5,4:3.5}/5'::sparsevec::vector;
SELECT '{2:1.5,4:3.5}/5'::sparsevec::vector(5);
SELECT '{2:1.5,4:3.5}/5'::sparsevec::vector(4);
SELECT '{}/16001'::sparsevec::vector;

SELECT '[0,1.5,0,3.5,0]'::halfvec::sparsevec;
SELECT '[0,1.5,0,3.5,0]'::halfvec::sparsevec(5);
SELECT '[0,1.5,0,3.5,0]'::halfvec::sparsevec(4);

SELECT '{2:1.5,4:3.5}/5'::sparsevec::halfvec;
SELECT '{2:1.5,4:3.5}/5'::sparsevec::halfvec(5);
SELECT '{2:1.5,4:3.5}/5'::sparsevec::halfvec(4);
SELECT '{}/16001'::sparsevec::halfvec;
SELECT '{1:65520}/1'::sparsevec::halfvec;
SELECT '{1:1e-8}/1'::sparsevec::halfvec;

SELECT ARRAY[1,0,2,0,3,0]::sparsevec;
SELECT ARRAY[1.0,0.0,2.0,0.0,3.0,0.0]::sparsevec;
SELECT ARRAY[1,0,2,0,3,0]::float4[]::sparsevec;
SELECT ARRAY[1,0,2,0,3,0]::float8[]::sparsevec;
SELECT ARRAY[1,0,2,0,3,0]::numeric[]::sparsevec;

SELECT '{1,0,2,0,3,0}'::real[]::sparsevec;
SELECT '{1,0,2,0,3,0}'::real[]::sparsevec(6);
SELECT '{1,0,2,0,3,0}'::real[]::sparsevec(5);
SELECT '{NULL}'::real[]::sparsevec;
SELECT '{NaN}'::real[]::sparsevec;
SELECT '{Infinity}'::real[]::sparsevec;
SELECT '{-Infinity}'::real[]::sparsevec;
SELECT '{}'::real[]::sparsevec;
SELECT '{{1}}'::real[]::sparsevec;

SELECT array_agg(n)::vector FROM generate_series(1, 16001) n;
SELECT array_to_vector(array_agg(n), 16001, false) FROM generate_series(1, 16001) n;

-- ensure no error
SELECT ARRAY[1,2,3] = ARRAY[1,2,3];
```

## File: `test/sql/copy.sql`
```sql
-- vector

CREATE TABLE t (val vector(3));
INSERT INTO t (val) VALUES ('[0,0,0]'), ('[1,2,3]'), ('[1,1,1]'), (NULL);

CREATE TABLE t2 (val vector(3));

\copy t TO 'results/vector.bin' WITH (FORMAT binary)
\copy t2 FROM 'results/vector.bin' WITH (FORMAT binary)

SELECT * FROM t2 ORDER BY val;

DROP TABLE t;
DROP TABLE t2;

-- halfvec

CREATE TABLE t (val halfvec(3));
INSERT INTO t (val) VALUES ('[0,0,0]'), ('[1,2,3]'), ('[1,1,1]'), (NULL);

CREATE TABLE t2 (val halfvec(3));

\copy t TO 'results/halfvec.bin' WITH (FORMAT binary)
\copy t2 FROM 'results/halfvec.bin' WITH (FORMAT binary)

SELECT * FROM t2 ORDER BY val;

DROP TABLE t;
DROP TABLE t2;

-- sparsevec

CREATE TABLE t (val sparsevec(3));
INSERT INTO t (val) VALUES ('{}/3'), ('{1:1,2:2,3:3}/3'), ('{1:1,2:1,3:1}/3'), (NULL);

CREATE TABLE t2 (val sparsevec(3));

\copy t TO 'results/sparsevec.bin' WITH (FORMAT binary)
\copy t2 FROM 'results/sparsevec.bin' WITH (FORMAT binary)

SELECT * FROM t2 ORDER BY val;

DROP TABLE t;
DROP TABLE t2;
```

## File: `test/sql/halfvec.sql`
```sql
SELECT '[1,2,3]'::halfvec;
SELECT '[-1,-2,-3]'::halfvec;
SELECT '[1.,2.,3.]'::halfvec;
SELECT ' [ 1,  2 ,    3  ] '::halfvec;
SELECT '[1.23456]'::halfvec;
SELECT '[hello,1]'::halfvec;
SELECT '[NaN,1]'::halfvec;
SELECT '[Infinity,1]'::halfvec;
SELECT '[-Infinity,1]'::halfvec;
SELECT '[65519,-65519]'::halfvec;
SELECT '[65520,-65520]'::halfvec;
SELECT '[1e-8,-1e-8]'::halfvec;
SELECT '[4e38,1]'::halfvec;
SELECT '[1e-46,1]'::halfvec;
SELECT '[1,2,3'::halfvec;
SELECT '[1,2,3]9'::halfvec;
SELECT '1,2,3'::halfvec;
SELECT ''::halfvec;
SELECT '['::halfvec;
SELECT '[ '::halfvec;
SELECT '[,'::halfvec;
SELECT '[]'::halfvec;
SELECT '[ ]'::halfvec;
SELECT '[,]'::halfvec;
SELECT '[1,]'::halfvec;
SELECT '[1a]'::halfvec;
SELECT '[1,,3]'::halfvec;
SELECT '[1, ,3]'::halfvec;

SELECT '[1,2,3]'::halfvec(3);
SELECT '[1,2,3]'::halfvec(2);
SELECT '[1,2,3]'::halfvec(3, 2);
SELECT '[1,2,3]'::halfvec('a');
SELECT '[1,2,3]'::halfvec(0);
SELECT '[1,2,3]'::halfvec(16001);

SELECT unnest('{"[1,2,3]", "[4,5,6]"}'::halfvec[]);
SELECT '{"[1,2,3]"}'::halfvec(2)[];

SELECT '[1,2,3]'::halfvec + '[4,5,6]';
SELECT '[65519]'::halfvec + '[65519]';
SELECT '[1,2]'::halfvec + '[3]';

SELECT '[1,2,3]'::halfvec - '[4,5,6]';
SELECT '[-65519]'::halfvec - '[65519]';
SELECT '[1,2]'::halfvec - '[3]';

SELECT '[1,2,3]'::halfvec * '[4,5,6]';
SELECT '[65519]'::halfvec * '[65519]';
SELECT '[1e-7]'::halfvec * '[1e-7]';
SELECT '[1,2]'::halfvec * '[3]';

SELECT '[1,2,3]'::halfvec || '[4,5]';
SELECT array_fill(0, ARRAY[16000])::halfvec || '[1]';

SELECT '[1,2,3]'::halfvec < '[1,2,3]';
SELECT '[1,2,3]'::halfvec < '[1,2]';
SELECT '[1,2,3]'::halfvec <= '[1,2,3]';
SELECT '[1,2,3]'::halfvec <= '[1,2]';
SELECT '[1,2,3]'::halfvec = '[1,2,3]';
SELECT '[1,2,3]'::halfvec = '[1,2]';
SELECT '[1,2,3]'::halfvec != '[1,2,3]';
SELECT '[1,2,3]'::halfvec != '[1,2]';
SELECT '[1,2,3]'::halfvec >= '[1,2,3]';
SELECT '[1,2,3]'::halfvec >= '[1,2]';
SELECT '[1,2,3]'::halfvec > '[1,2,3]';
SELECT '[1,2,3]'::halfvec > '[1,2]';

SELECT halfvec_cmp('[1,2,3]', '[1,2,3]');
SELECT halfvec_cmp('[1,2,3]', '[0,0,0]');
SELECT halfvec_cmp('[0,0,0]', '[1,2,3]');
SELECT halfvec_cmp('[1,2]', '[1,2,3]');
SELECT halfvec_cmp('[1,2,3]', '[1,2]');
SELECT halfvec_cmp('[1,2]', '[2,3,4]');
SELECT halfvec_cmp('[2,3]', '[1,2,3]');

SELECT vector_dims('[1,2,3]'::halfvec);

SELECT round(l2_norm('[1,1]'::halfvec)::numeric, 5);
SELECT l2_norm('[3,4]'::halfvec);
SELECT l2_norm('[0,1]'::halfvec);
SELECT l2_norm('[0,0]'::halfvec);
SELECT l2_norm('[2]'::halfvec);

SELECT l2_distance('[0,0]'::halfvec, '[3,4]');
SELECT l2_distance('[0,0]'::halfvec, '[0,1]');
SELECT l2_distance('[1,2]'::halfvec, '[3]');
SELECT l2_distance('[1,1,1,1,1,1,1,1,1]'::halfvec, '[1,1,1,1,1,1,1,4,5]');
SELECT '[0,0]'::halfvec <-> '[3,4]';

SELECT inner_product('[1,2]'::halfvec, '[3,4]');
SELECT inner_product('[1,2]'::halfvec, '[3]');
SELECT inner_product('[65504]'::halfvec, '[65504]');
SELECT inner_product('[1,1,1,1,1,1,1,1,1]'::halfvec, '[1,2,3,4,5,6,7,8,9]');
SELECT '[1,2]'::halfvec <#> '[3,4]';

SELECT cosine_distance('[1,2]'::halfvec, '[2,4]');
SELECT cosine_distance('[1,2]'::halfvec, '[0,0]');
SELECT cosine_distance('[1,1]'::halfvec, '[1,1]');
SELECT cosine_distance('[1,0]'::halfvec, '[0,2]');
SELECT cosine_distance('[1,1]'::halfvec, '[-1,-1]');
SELECT cosine_distance('[1,2]'::halfvec, '[3]');
SELECT cosine_distance('[1,1]'::halfvec, '[1.1,1.1]');
SELECT cosine_distance('[1,1]'::halfvec, '[-1.1,-1.1]');
SELECT cosine_distance('[1,2,3,4,5,6,7,8,9]'::halfvec, '[1,2,3,4,5,6,7,8,9]');
SELECT cosine_distance('[1,2,3,4,5,6,7,8,9]'::halfvec, '[-1,-2,-3,-4,-5,-6,-7,-8,-9]');
SELECT '[1,2]'::halfvec <=> '[2,4]';

SELECT l1_distance('[0,0]'::halfvec, '[3,4]');
SELECT l1_distance('[0,0]'::halfvec, '[0,1]');
SELECT l1_distance('[1,2]'::halfvec, '[3]');
SELECT l1_distance('[1,2,3,4,5,6,7,8,9]'::halfvec, '[1,2,3,4,5,6,7,8,9]');
SELECT l1_distance('[1,2,3,4,5,6,7,8,9]'::halfvec, '[0,3,2,5,4,7,6,9,8]');
SELECT '[0,0]'::halfvec <+> '[3,4]';

SELECT l2_normalize('[3,4]'::halfvec);
SELECT l2_normalize('[3,0]'::halfvec);
SELECT l2_normalize('[0,0.1]'::halfvec);
SELECT l2_normalize('[0,0]'::halfvec);
SELECT l2_normalize('[65504]'::halfvec);

SELECT binary_quantize('[1,0,-1]'::halfvec);
SELECT binary_quantize('[0,0.1,-0.2,-0.3,0.4,0.5,0.6,-0.7,0.8,-0.9,1]'::halfvec);
SELECT binary_quantize('[1,2,3,-4,5,6,-7,8,1,-2,-3,4,5,-6,7,8,-1,2,3]'::halfvec);

SELECT subvector('[1,2,3,4,5]'::halfvec, 1, 3);
SELECT subvector('[1,2,3,4,5]'::halfvec, 3, 2);
SELECT subvector('[1,2,3,4,5]'::halfvec, -1, 3);
SELECT subvector('[1,2,3,4,5]'::halfvec, 3, 9);
SELECT subvector('[1,2,3,4,5]'::halfvec, 1, 0);
SELECT subvector('[1,2,3,4,5]'::halfvec, 3, -1);
SELECT subvector('[1,2,3,4,5]'::halfvec, -1, 2);
SELECT subvector('[1,2,3,4,5]'::halfvec, 2147483647, 10);
SELECT subvector('[1,2,3,4,5]'::halfvec, 3, 2147483647);
SELECT subvector('[1,2,3,4,5]'::halfvec, -2147483644, 2147483647);

SELECT avg(v) FROM unnest(ARRAY['[1,2,3]'::halfvec, '[3,5,7]']) v;
SELECT avg(v) FROM unnest(ARRAY['[1,2,3]'::halfvec, '[3,5,7]', NULL]) v;
SELECT avg(v) FROM unnest(ARRAY[]::halfvec[]) v;
SELECT avg(v) FROM unnest(ARRAY['[1,2]'::halfvec, '[3]']) v;
SELECT avg(v) FROM unnest(ARRAY['[65504]'::halfvec, '[65504]']) v;
SELECT halfvec_avg(array_agg(n)) FROM generate_series(1, 16002) n;

SELECT sum(v) FROM unnest(ARRAY['[1,2,3]'::halfvec, '[3,5,7]']) v;
SELECT sum(v) FROM unnest(ARRAY['[1,2,3]'::halfvec, '[3,5,7]', NULL]) v;
SELECT sum(v) FROM unnest(ARRAY[]::halfvec[]) v;
SELECT sum(v) FROM unnest(ARRAY['[1,2]'::halfvec, '[3]']) v;
SELECT sum(v) FROM unnest(ARRAY['[65504]'::halfvec, '[65504]']) v;
```

## File: `test/sql/hnsw_bit.sql`
```sql
SET enable_seqscan = off;

-- hamming

CREATE TABLE t (val bit(3));
INSERT INTO t (val) VALUES (B'000'), (B'100'), (B'111'), (NULL);
CREATE INDEX ON t USING hnsw (val bit_hamming_ops);

INSERT INTO t (val) VALUES (B'110');

SELECT * FROM t ORDER BY val <~> B'111';
SELECT COUNT(*) FROM (SELECT * FROM t ORDER BY val <~> (SELECT NULL::bit)) t2;

DROP TABLE t;

-- jaccard

CREATE TABLE t (val bit(4));
INSERT INTO t (val) VALUES (B'0000'), (B'1100'), (B'1111'), (NULL);
CREATE INDEX ON t USING hnsw (val bit_jaccard_ops);

INSERT INTO t (val) VALUES (B'1110');

SELECT * FROM t ORDER BY val <%> B'1111';
SELECT COUNT(*) FROM (SELECT * FROM t ORDER BY val <%> (SELECT NULL::bit)) t2;

DROP TABLE t;

-- varbit

CREATE TABLE t (val varbit(3));
CREATE INDEX ON t USING hnsw (val bit_hamming_ops);
CREATE INDEX ON t USING hnsw ((val::bit(3)) bit_hamming_ops);
CREATE INDEX ON t USING hnsw ((val::bit(64001)) bit_hamming_ops);
DROP TABLE t;
```

## File: `test/sql/hnsw_halfvec.sql`
```sql
SET enable_seqscan = off;

-- L2

CREATE TABLE t (val halfvec(3));
INSERT INTO t (val) VALUES ('[0,0,0]'), ('[1,2,3]'), ('[1,1,1]'), (NULL);
CREATE INDEX ON t USING hnsw (val halfvec_l2_ops);

INSERT INTO t (val) VALUES ('[1,2,4]');

SELECT * FROM t ORDER BY val <-> '[3,3,3]';
SELECT COUNT(*) FROM (SELECT * FROM t ORDER BY val <-> (SELECT NULL::halfvec)) t2;
SELECT COUNT(*) FROM t;

TRUNCATE t;
SELECT * FROM t ORDER BY val <-> '[3,3,3]';

DROP TABLE t;

-- inner product

CREATE TABLE t (val halfvec(3));
INSERT INTO t (val) VALUES ('[0,0,0]'), ('[1,2,3]'), ('[1,1,1]'), (NULL);
CREATE INDEX ON t USING hnsw (val halfvec_ip_ops);

INSERT INTO t (val) VALUES ('[1,2,4]');

SELECT * FROM t ORDER BY val <#> '[3,3,3]';
SELECT COUNT(*) FROM (SELECT * FROM t ORDER BY val <#> (SELECT NULL::halfvec)) t2;

DROP TABLE t;

-- cosine

CREATE TABLE t (val halfvec(3));
INSERT INTO t (val) VALUES ('[0,0,0]'), ('[1,2,3]'), ('[1,1,1]'), (NULL);
CREATE INDEX ON t USING hnsw (val halfvec_cosine_ops);

INSERT INTO t (val) VALUES ('[1,2,4]');

SELECT * FROM t ORDER BY val <=> '[3,3,3]';
SELECT COUNT(*) FROM (SELECT * FROM t ORDER BY val <=> '[0,0,0]') t2;
SELECT COUNT(*) FROM (SELECT * FROM t ORDER BY val <=> (SELECT NULL::halfvec)) t2;

DROP TABLE t;

-- L1

CREATE TABLE t (val halfvec(3));
INSERT INTO t (val) VALUES ('[0,0,0]'), ('[1,2,3]'), ('[1,1,1]'), (NULL);
CREATE INDEX ON t USING hnsw (val halfvec_l1_ops);

INSERT INTO t (val) VALUES ('[1,2,4]');

SELECT * FROM t ORDER BY val <+> '[3,3,3]';
SELECT COUNT(*) FROM (SELECT * FROM t ORDER BY val <+> (SELECT NULL::halfvec)) t2;

DROP TABLE t;
```

## File: `test/sql/hnsw_sparsevec.sql`
```sql
SET enable_seqscan = off;

-- L2

CREATE TABLE t (val sparsevec(3));
INSERT INTO t (val) VALUES ('{}/3'), ('{1:1,2:2,3:3}/3'), ('{1:1,2:1,3:1}/3'), (NULL);
CREATE INDEX ON t USING hnsw (val sparsevec_l2_ops);

INSERT INTO t (val) VALUES ('{1:1,2:2,3:4}/3');

SELECT * FROM t ORDER BY val <-> '{1:3,2:3,3:3}/3';
SELECT COUNT(*) FROM (SELECT * FROM t ORDER BY val <-> (SELECT NULL::sparsevec)) t2;
SELECT COUNT(*) FROM t;

TRUNCATE t;
SELECT * FROM t ORDER BY val <-> '{1:3,2:3,3:3}/3';

DROP TABLE t;

-- inner product

CREATE TABLE t (val sparsevec(3));
INSERT INTO t (val) VALUES ('{}/3'), ('{1:1,2:2,3:3}/3'), ('{1:1,2:1,3:1}/3'), (NULL);
CREATE INDEX ON t USING hnsw (val sparsevec_ip_ops);

INSERT INTO t (val) VALUES ('{1:1,2:2,3:4}/3');

SELECT * FROM t ORDER BY val <#> '{1:3,2:3,3:3}/3';
SELECT COUNT(*) FROM (SELECT * FROM t ORDER BY val <#> (SELECT NULL::sparsevec)) t2;

DROP TABLE t;

-- cosine

CREATE TABLE t (val sparsevec(3));
INSERT INTO t (val) VALUES ('{}/3'), ('{1:1,2:2,3:3}/3'), ('{1:1,2:1,3:1}/3'), (NULL);
CREATE INDEX ON t USING hnsw (val sparsevec_cosine_ops);

INSERT INTO t (val) VALUES ('{1:1,2:2,3:4}/3');

SELECT * FROM t ORDER BY val <=> '{1:3,2:3,3:3}/3';
SELECT COUNT(*) FROM (SELECT * FROM t ORDER BY val <=> '{}/3') t2;
SELECT COUNT(*) FROM (SELECT * FROM t ORDER BY val <=> (SELECT NULL::sparsevec)) t2;

DROP TABLE t;

-- L1

CREATE TABLE t (val sparsevec(3));
INSERT INTO t (val) VALUES ('{}/3'), ('{1:1,2:2,3:3}/3'), ('{1:1,2:1,3:1}/3'), (NULL);
CREATE INDEX ON t USING hnsw (val sparsevec_l1_ops);

INSERT INTO t (val) VALUES ('{1:1,2:2,3:4}/3');

SELECT * FROM t ORDER BY val <+> '{1:3,2:3,3:3}/3';
SELECT COUNT(*) FROM (SELECT * FROM t ORDER BY val <+> (SELECT NULL::sparsevec)) t2;

DROP TABLE t;

-- non-zero elements

CREATE TABLE t (val sparsevec(1001));
INSERT INTO t (val) VALUES (array_fill(1, ARRAY[1001])::vector::sparsevec);
CREATE INDEX ON t USING hnsw (val sparsevec_l2_ops);
TRUNCATE t;
CREATE INDEX ON t USING hnsw (val sparsevec_l2_ops);
INSERT INTO t (val) VALUES (array_fill(1, ARRAY[1001])::vector::sparsevec);
DROP TABLE t;
```

## File: `test/sql/hnsw_vector.sql`
```sql
SET enable_seqscan = off;

-- L2

CREATE TABLE t (val vector(3));
INSERT INTO t (val) VALUES ('[0,0,0]'), ('[1,2,3]'), ('[1,1,1]'), (NULL);
CREATE INDEX ON t USING hnsw (val vector_l2_ops);

INSERT INTO t (val) VALUES ('[1,2,4]');

SELECT * FROM t ORDER BY val <-> '[3,3,3]';
SELECT COUNT(*) FROM (SELECT * FROM t ORDER BY val <-> (SELECT NULL::vector)) t2;
SELECT COUNT(*) FROM t;

TRUNCATE t;
SELECT * FROM t ORDER BY val <-> '[3,3,3]';

DROP TABLE t;

-- inner product

CREATE TABLE t (val vector(3));
INSERT INTO t (val) VALUES ('[0,0,0]'), ('[1,2,3]'), ('[1,1,1]'), (NULL);
CREATE INDEX ON t USING hnsw (val vector_ip_ops);

INSERT INTO t (val) VALUES ('[1,2,4]');

SELECT * FROM t ORDER BY val <#> '[3,3,3]';
SELECT COUNT(*) FROM (SELECT * FROM t ORDER BY val <#> (SELECT NULL::vector)) t2;

DROP TABLE t;

-- cosine

CREATE TABLE t (val vector(3));
INSERT INTO t (val) VALUES ('[0,0,0]'), ('[1,2,3]'), ('[1,1,1]'), (NULL);
CREATE INDEX ON t USING hnsw (val vector_cosine_ops);

INSERT INTO t (val) VALUES ('[1,2,4]');

SELECT * FROM t ORDER BY val <=> '[3,3,3]';
SELECT COUNT(*) FROM (SELECT * FROM t ORDER BY val <=> '[0,0,0]') t2;
SELECT COUNT(*) FROM (SELECT * FROM t ORDER BY val <=> (SELECT NULL::vector)) t2;

DROP TABLE t;

-- L1

CREATE TABLE t (val vector(3));
INSERT INTO t (val) VALUES ('[0,0,0]'), ('[1,2,3]'), ('[1,1,1]'), (NULL);
CREATE INDEX ON t USING hnsw (val vector_l1_ops);

INSERT INTO t (val) VALUES ('[1,2,4]');

SELECT * FROM t ORDER BY val <+> '[3,3,3]';
SELECT COUNT(*) FROM (SELECT * FROM t ORDER BY val <+> (SELECT NULL::vector)) t2;

DROP TABLE t;

-- iterative

CREATE TABLE t (val vector(3));
INSERT INTO t (val) VALUES ('[0,0,0]'), ('[1,2,3]'), ('[1,1,1]'), (NULL);
CREATE INDEX ON t USING hnsw (val vector_l2_ops);

SET hnsw.iterative_scan = strict_order;
SET hnsw.ef_search = 1;
SELECT * FROM t ORDER BY val <-> '[3,3,3]';

SET hnsw.iterative_scan = relaxed_order;
SELECT * FROM t ORDER BY val <-> '[3,3,3]';

TRUNCATE t;
SELECT * FROM t ORDER BY val <-> '[3,3,3]';

RESET hnsw.iterative_scan;
RESET hnsw.ef_search;
DROP TABLE t;

-- unlogged

CREATE UNLOGGED TABLE t (val vector(3));
INSERT INTO t (val) VALUES ('[0,0,0]'), ('[1,2,3]'), ('[1,1,1]'), (NULL);
CREATE INDEX ON t USING hnsw (val vector_l2_ops);

SELECT * FROM t ORDER BY val <-> '[3,3,3]';

DROP TABLE t;

-- options

CREATE TABLE t (val vector(3));
CREATE INDEX ON t USING hnsw (val vector_l2_ops) WITH (m = 1);
CREATE INDEX ON t USING hnsw (val vector_l2_ops) WITH (m = 101);
CREATE INDEX ON t USING hnsw (val vector_l2_ops) WITH (ef_construction = 3);
CREATE INDEX ON t USING hnsw (val vector_l2_ops) WITH (ef_construction = 1001);
CREATE INDEX ON t USING hnsw (val vector_l2_ops) WITH (m = 16, ef_construction = 31);

SHOW hnsw.ef_search;

SET hnsw.ef_search = 0;
SET hnsw.ef_search = 1001;

SHOW hnsw.iterative_scan;

SET hnsw.iterative_scan = on;

SHOW hnsw.max_scan_tuples;

SET hnsw.max_scan_tuples = 0;

SHOW hnsw.scan_mem_multiplier;

SET hnsw.scan_mem_multiplier = 0;
SET hnsw.scan_mem_multiplier = 1001;

DROP TABLE t;
```

## File: `test/sql/ivfflat_bit.sql`
```sql
SET enable_seqscan = off;

-- hamming

CREATE TABLE t (val bit(3));
INSERT INTO t (val) VALUES (B'000'), (B'100'), (B'111'), (NULL);
CREATE INDEX ON t USING ivfflat (val bit_hamming_ops) WITH (lists = 1);

INSERT INTO t (val) VALUES (B'110');

SELECT * FROM t ORDER BY val <~> B'111';
SELECT COUNT(*) FROM (SELECT * FROM t ORDER BY val <~> (SELECT NULL::bit)) t2;

DROP TABLE t;

-- varbit

CREATE TABLE t (val varbit(3));
CREATE INDEX ON t USING ivfflat (val bit_hamming_ops) WITH (lists = 1);
CREATE INDEX ON t USING ivfflat ((val::bit(3)) bit_hamming_ops) WITH (lists = 1);
CREATE INDEX ON t USING ivfflat ((val::bit(64001)) bit_hamming_ops) WITH (lists = 1);
CREATE INDEX ON t USING ivfflat ((val::bit(2)) bit_hamming_ops) WITH (lists = 5);
DROP TABLE t;
```

## File: `test/sql/ivfflat_halfvec.sql`
```sql
SET enable_seqscan = off;

-- L2

CREATE TABLE t (val halfvec(3));
INSERT INTO t (val) VALUES ('[0,0,0]'), ('[1,2,3]'), ('[1,1,1]'), (NULL);
CREATE INDEX ON t USING ivfflat (val halfvec_l2_ops) WITH (lists = 1);

INSERT INTO t (val) VALUES ('[1,2,4]');

SELECT * FROM t ORDER BY val <-> '[3,3,3]';
SELECT COUNT(*) FROM (SELECT * FROM t ORDER BY val <-> (SELECT NULL::halfvec)) t2;
SELECT COUNT(*) FROM t;

TRUNCATE t;
SELECT * FROM t ORDER BY val <-> '[3,3,3]';

DROP TABLE t;

-- inner product

CREATE TABLE t (val halfvec(3));
INSERT INTO t (val) VALUES ('[0,0,0]'), ('[1,2,3]'), ('[1,1,1]'), (NULL);
CREATE INDEX ON t USING ivfflat (val halfvec_ip_ops) WITH (lists = 1);

INSERT INTO t (val) VALUES ('[1,2,4]');

SELECT * FROM t ORDER BY val <#> '[3,3,3]';
SELECT COUNT(*) FROM (SELECT * FROM t ORDER BY val <#> (SELECT NULL::halfvec)) t2;

DROP TABLE t;

-- cosine

CREATE TABLE t (val halfvec(3));
INSERT INTO t (val) VALUES ('[0,0,0]'), ('[1,2,3]'), ('[1,1,1]'), (NULL);
CREATE INDEX ON t USING ivfflat (val halfvec_cosine_ops) WITH (lists = 1);

INSERT INTO t (val) VALUES ('[1,2,4]');

SELECT * FROM t ORDER BY val <=> '[3,3,3]';
SELECT COUNT(*) FROM (SELECT * FROM t ORDER BY val <=> '[0,0,0]') t2;
SELECT COUNT(*) FROM (SELECT * FROM t ORDER BY val <=> (SELECT NULL::halfvec)) t2;

DROP TABLE t;
```

## File: `test/sql/ivfflat_vector.sql`
```sql
SET enable_seqscan = off;

-- L2

CREATE TABLE t (val vector(3));
INSERT INTO t (val) VALUES ('[0,0,0]'), ('[1,2,3]'), ('[1,1,1]'), (NULL);
CREATE INDEX ON t USING ivfflat (val vector_l2_ops) WITH (lists = 1);

INSERT INTO t (val) VALUES ('[1,2,4]');

SELECT * FROM t ORDER BY val <-> '[3,3,3]';
SELECT COUNT(*) FROM (SELECT * FROM t ORDER BY val <-> (SELECT NULL::vector)) t2;
SELECT COUNT(*) FROM t;

TRUNCATE t;
SELECT * FROM t ORDER BY val <-> '[3,3,3]';

DROP TABLE t;

-- inner product

CREATE TABLE t (val vector(3));
INSERT INTO t (val) VALUES ('[0,0,0]'), ('[1,2,3]'), ('[1,1,1]'), (NULL);
CREATE INDEX ON t USING ivfflat (val vector_ip_ops) WITH (lists = 1);

INSERT INTO t (val) VALUES ('[1,2,4]');

SELECT * FROM t ORDER BY val <#> '[3,3,3]';
SELECT COUNT(*) FROM (SELECT * FROM t ORDER BY val <#> (SELECT NULL::vector)) t2;

DROP TABLE t;

-- cosine

CREATE TABLE t (val vector(3));
INSERT INTO t (val) VALUES ('[0,0,0]'), ('[1,2,3]'), ('[1,1,1]'), (NULL);
CREATE INDEX ON t USING ivfflat (val vector_cosine_ops) WITH (lists = 1);

INSERT INTO t (val) VALUES ('[1,2,4]');

SELECT * FROM t ORDER BY val <=> '[3,3,3]';
SELECT COUNT(*) FROM (SELECT * FROM t ORDER BY val <=> '[0,0,0]') t2;
SELECT COUNT(*) FROM (SELECT * FROM t ORDER BY val <=> (SELECT NULL::vector)) t2;

DROP TABLE t;

-- iterative

CREATE TABLE t (val vector(3));
INSERT INTO t (val) VALUES ('[0,0,0]'), ('[1,2,3]'), ('[1,1,1]'), (NULL);
CREATE INDEX ON t USING ivfflat (val vector_l2_ops) WITH (lists = 3);

SET ivfflat.iterative_scan = relaxed_order;
SELECT * FROM t ORDER BY val <-> '[3,3,3]';

SET ivfflat.max_probes = 1;
SELECT * FROM t ORDER BY val <-> '[3,3,3]';

SET ivfflat.max_probes = 2;
SELECT * FROM t ORDER BY val <-> '[3,3,3]';

TRUNCATE t;
SELECT * FROM t ORDER BY val <-> '[3,3,3]';

RESET ivfflat.iterative_scan;
RESET ivfflat.max_probes;
DROP TABLE t;

-- unlogged

CREATE UNLOGGED TABLE t (val vector(3));
INSERT INTO t (val) VALUES ('[0,0,0]'), ('[1,2,3]'), ('[1,1,1]'), (NULL);
CREATE INDEX ON t USING ivfflat (val vector_l2_ops) WITH (lists = 1);

SELECT * FROM t ORDER BY val <-> '[3,3,3]';

DROP TABLE t;

-- options

CREATE TABLE t (val vector(3));
CREATE INDEX ON t USING ivfflat (val vector_l2_ops) WITH (lists = 0);
CREATE INDEX ON t USING ivfflat (val vector_l2_ops) WITH (lists = 32769);

SHOW ivfflat.probes;

SET ivfflat.probes = 0;
SET ivfflat.probes = 32769;

SHOW ivfflat.iterative_scan;

SET ivfflat.iterative_scan = on;

SHOW ivfflat.max_probes;

SET ivfflat.max_probes = 0;
SET ivfflat.max_probes = 32769;

DROP TABLE t;
```

## File: `test/sql/sparsevec.sql`
```sql
SELECT '{1:1.5,3:3.5}/5'::sparsevec;
SELECT '{1:-2,3:-4}/5'::sparsevec;
SELECT '{1:2.,3:4.}/5'::sparsevec;
SELECT ' { 1 : 1.5 ,  3  :  3.5  } / 5 '::sparsevec;
SELECT '{1:1.23456}/1'::sparsevec;
SELECT '{1:hello,2:1}/2'::sparsevec;
SELECT '{1:NaN,2:1}/2'::sparsevec;
SELECT '{1:Infinity,2:1}/2'::sparsevec;
SELECT '{1:-Infinity,2:1}/2'::sparsevec;
SELECT '{1:1.5e38,2:-1.5e38}/2'::sparsevec;
SELECT '{1:1.5e+38,2:-1.5e+38}/2'::sparsevec;
SELECT '{1:1.5e-38,2:-1.5e-38}/2'::sparsevec;
SELECT '{1:4e38,2:1}/2'::sparsevec;
SELECT '{1:-4e38,2:1}/2'::sparsevec;
SELECT '{1:1e-46,2:1}/2'::sparsevec;
SELECT '{1:-1e-46,2:1}/2'::sparsevec;
SELECT ''::sparsevec;
SELECT '{'::sparsevec;
SELECT '{ '::sparsevec;
SELECT '{:'::sparsevec;
SELECT '{,'::sparsevec;
SELECT '{}'::sparsevec;
SELECT '{}/'::sparsevec;
SELECT '{}/1'::sparsevec;
SELECT '{}/1a'::sparsevec;
SELECT '{ }/1'::sparsevec;
SELECT '{:}/1'::sparsevec;
SELECT '{,}/1'::sparsevec;
SELECT '{1,}/1'::sparsevec;
SELECT '{:1}/1'::sparsevec;
SELECT '{1:}/1'::sparsevec;
SELECT '{1a:1}/1'::sparsevec;
SELECT '{1:1a}/1'::sparsevec;
SELECT '{1:1,}/1'::sparsevec;
SELECT '{1:0,2:1,3:0}/3'::sparsevec;
SELECT '{2:1,1:1}/2'::sparsevec;
SELECT '{1:1,1:1}/2'::sparsevec;
SELECT '{1:1,2:1,1:1}/2'::sparsevec;
SELECT '{}/5'::sparsevec;
SELECT '{}/-1'::sparsevec;
SELECT '{}/1000000001'::sparsevec;
SELECT '{}/2147483648'::sparsevec;
SELECT '{}/-2147483649'::sparsevec;
SELECT '{}/9223372036854775808'::sparsevec;
SELECT '{}/-9223372036854775809'::sparsevec;
SELECT '{2147483647:1}/1'::sparsevec;
SELECT '{2147483648:1}/1'::sparsevec;
SELECT '{-2147483648:1}/1'::sparsevec;
SELECT '{-2147483649:1}/1'::sparsevec;
SELECT '{0:1}/1'::sparsevec;
SELECT '{2:1}/1'::sparsevec;

SELECT '{}/3'::sparsevec(3);
SELECT '{}/3'::sparsevec(2);
SELECT '{}/3'::sparsevec(3, 2);
SELECT '{}/3'::sparsevec('a');
SELECT '{}/3'::sparsevec(0);
SELECT '{}/3'::sparsevec(1000000001);

SELECT '{1:1,2:2,3:3}/3'::sparsevec < '{1:1,2:2,3:3}/3';
SELECT '{1:1,2:2,3:3}/3'::sparsevec < '{1:1,2:2}/2';
SELECT '{1:1,2:2,3:3}/3'::sparsevec <= '{1:1,2:2,3:3}/3';
SELECT '{1:1,2:2,3:3}/3'::sparsevec <= '{1:1,2:2}/2';
SELECT '{1:1,2:2,3:3}/3'::sparsevec = '{1:1,2:2,3:3}/3';
SELECT '{1:1,2:2,3:3}/3'::sparsevec = '{1:1,2:2}/2';
SELECT '{1:1,2:2,3:3}/3'::sparsevec != '{1:1,2:2,3:3}/3';
SELECT '{1:1,2:2,3:3}/3'::sparsevec != '{1:1,2:2}/2';
SELECT '{1:1,2:2,3:3}/3'::sparsevec >= '{1:1,2:2,3:3}/3';
SELECT '{1:1,2:2,3:3}/3'::sparsevec >= '{1:1,2:2}/2';
SELECT '{1:1,2:2,3:3}/3'::sparsevec > '{1:1,2:2,3:3}/3';
SELECT '{1:1,2:2,3:3}/3'::sparsevec > '{1:1,2:2}/2';

SELECT sparsevec_cmp('{1:1,2:2,3:3}/3', '{1:1,2:2,3:3}/3');
SELECT sparsevec_cmp('{1:1,2:2,3:3}/3', '{}/3');
SELECT sparsevec_cmp('{}/3', '{1:1,2:2,3:3}/3');
SELECT sparsevec_cmp('{1:1,2:2}/2', '{1:1,2:2,3:3}/3');
SELECT sparsevec_cmp('{1:1,2:2,3:3}/3', '{1:1,2:2}/2');
SELECT sparsevec_cmp('{1:1,2:2}/2', '{1:2,2:3,3:4}/3');
SELECT sparsevec_cmp('{1:2,2:3}/2', '{1:1,2:2,3:3}/3');

SELECT round(l2_norm('{1:1,2:1}/2'::sparsevec)::numeric, 5);
SELECT l2_norm('{1:3,2:4}/2'::sparsevec);
SELECT l2_norm('{2:1}/2'::sparsevec);
SELECT l2_norm('{1:3e37,2:4e37}/2'::sparsevec)::real;
SELECT l2_norm('{}/2'::sparsevec);
SELECT l2_norm('{1:2}/1'::sparsevec);

SELECT l2_distance('{}/2'::sparsevec, '{1:3,2:4}/2');
SELECT l2_distance('{1:3}/2'::sparsevec, '{2:4}/2');
SELECT l2_distance('{2:4}/2'::sparsevec, '{1:3}/2');
SELECT l2_distance('{1:3,2:4}/2'::sparsevec, '{}/2');
SELECT l2_distance('{}/2'::sparsevec, '{2:1}/2');
SELECT '{}/2'::sparsevec <-> '{1:3,2:4}/2';

SELECT inner_product('{1:1,2:2}/2'::sparsevec, '{1:2,2:4}/2');
SELECT inner_product('{1:1,2:2}/2'::sparsevec, '{1:3}/1');
SELECT inner_product('{1:1,3:3}/4'::sparsevec, '{2:2,4:4}/4');
SELECT inner_product('{2:2,4:4}/4'::sparsevec, '{1:1,3:3}/4');
SELECT inner_product('{1:1,3:3,5:5}/5'::sparsevec, '{2:4,3:6,4:8}/5');
SELECT inner_product('{1:1}/2'::sparsevec, '{}/2');
SELECT inner_product('{}/2'::sparsevec, '{1:1}/2');
SELECT inner_product('{1:3e38}/1'::sparsevec, '{1:3e38}/1');
SELECT inner_product('{1:1,3:3,5:5}/5'::sparsevec, '{2:4,3:6,4:8}/5');
SELECT '{1:1,2:2}/2'::sparsevec <#> '{1:3,2:4}/2';

SELECT cosine_distance('{1:1,2:2}/2'::sparsevec, '{1:2,2:4}/2');
SELECT cosine_distance('{1:1,2:2}/2'::sparsevec, '{}/2');
SELECT cosine_distance('{1:1,2:1}/2'::sparsevec, '{1:1,2:1}/2');
SELECT cosine_distance('{1:1}/2'::sparsevec, '{2:2}/2');
SELECT cosine_distance('{1:1,2:1}/2'::sparsevec, '{1:-1,2:-1}/2');
SELECT cosine_distance('{1:2}/2'::sparsevec, '{2:2}/2');
SELECT cosine_distance('{2:2}/2'::sparsevec, '{1:2}/2');
SELECT cosine_distance('{1:1,2:2}/2'::sparsevec, '{1:3}/1');
SELECT cosine_distance('{1:1,2:1}/2'::sparsevec, '{1:1.1,2:1.1}/2');
SELECT cosine_distance('{1:1,2:1}/2'::sparsevec, '{1:-1.1,2:-1.1}/2');
SELECT cosine_distance('{1:3e38}/1'::sparsevec, '{1:3e38}/1');
SELECT cosine_distance('{}/1'::sparsevec, '{}/1');
SELECT '{1:1,2:2}/2'::sparsevec <=> '{1:2,2:4}/2';

SELECT l1_distance('{}/2'::sparsevec, '{1:3,2:4}/2');
SELECT l1_distance('{}/2'::sparsevec, '{2:1}/2');
SELECT l1_distance('{1:1,2:2}/2'::sparsevec, '{1:3}/1');
SELECT l1_distance('{1:3e38}/1'::sparsevec, '{1:-3e38}/1');
SELECT l1_distance('{1:1,3:3,5:5,7:7}/8'::sparsevec, '{2:2,4:4,6:6,8:8}/8');
SELECT l1_distance('{1:1,3:3,5:5,7:7,9:9}/9'::sparsevec, '{2:2,4:4,6:6,8:8}/9');
SELECT '{}/2'::sparsevec <+> '{1:3,2:4}/2';

SELECT l2_normalize('{1:3,2:4}/2'::sparsevec);
SELECT l2_normalize('{1:3}/2'::sparsevec);
SELECT l2_normalize('{2:0.1}/2'::sparsevec);
SELECT l2_normalize('{}/2'::sparsevec);
SELECT l2_normalize('{1:3e38}/1'::sparsevec);
SELECT l2_normalize('{1:3e38,2:1e-37}/2'::sparsevec);
SELECT l2_normalize('{2:3e37,4:3e-37,6:4e37,8:4e-37}/9'::sparsevec);
```

## File: `test/sql/vector_type.sql`
```sql
SELECT '[1,2,3]'::vector;
SELECT '[-1,-2,-3]'::vector;
SELECT '[1.,2.,3.]'::vector;
SELECT ' [ 1,  2 ,    3  ] '::vector;
SELECT '[1.23456]'::vector;
SELECT '[hello,1]'::vector;
SELECT '[NaN,1]'::vector;
SELECT '[Infinity,1]'::vector;
SELECT '[-Infinity,1]'::vector;
SELECT '[1.5e38,-1.5e38]'::vector;
SELECT '[1.5e+38,-1.5e+38]'::vector;
SELECT '[1.5e-38,-1.5e-38]'::vector;
SELECT '[4e38,1]'::vector;
SELECT '[-4e38,1]'::vector;
SELECT '[1e-46,1]'::vector;
SELECT '[-1e-46,1]'::vector;
SELECT '[1,2,3'::vector;
SELECT '[1,2,3]9'::vector;
SELECT '1,2,3'::vector;
SELECT ''::vector;
SELECT '['::vector;
SELECT '[ '::vector;
SELECT '[,'::vector;
SELECT '[]'::vector;
SELECT '[ ]'::vector;
SELECT '[,]'::vector;
SELECT '[1,]'::vector;
SELECT '[1a]'::vector;
SELECT '[1,,3]'::vector;
SELECT '[1, ,3]'::vector;

SELECT '[1,2,3]'::vector(3);
SELECT '[1,2,3]'::vector(2);
SELECT '[1,2,3]'::vector(3, 2);
SELECT '[1,2,3]'::vector('a');
SELECT '[1,2,3]'::vector(0);
SELECT '[1,2,3]'::vector(16001);

SELECT unnest('{"[1,2,3]", "[4,5,6]"}'::vector[]);
SELECT '{"[1,2,3]"}'::vector(2)[];


SELECT '[1,2,3]'::vector + '[4,5,6]';
SELECT '[3e38]'::vector + '[3e38]';
SELECT '[1,2]'::vector + '[3]';

SELECT '[1,2,3]'::vector - '[4,5,6]';
SELECT '[-3e38]'::vector - '[3e38]';
SELECT '[1,2]'::vector - '[3]';

SELECT '[1,2,3]'::vector * '[4,5,6]';
SELECT '[1e37]'::vector * '[1e37]';
SELECT '[1e-37]'::vector * '[1e-37]';
SELECT '[1,2]'::vector * '[3]';

SELECT '[1,2,3]'::vector || '[4,5]';
SELECT array_fill(0, ARRAY[16000])::vector || '[1]';

SELECT '[1,2,3]'::vector < '[1,2,3]';
SELECT '[1,2,3]'::vector < '[1,2]';
SELECT '[1,2,3]'::vector <= '[1,2,3]';
SELECT '[1,2,3]'::vector <= '[1,2]';
SELECT '[1,2,3]'::vector = '[1,2,3]';
SELECT '[1,2,3]'::vector = '[1,2]';
SELECT '[1,2,3]'::vector != '[1,2,3]';
SELECT '[1,2,3]'::vector != '[1,2]';
SELECT '[1,2,3]'::vector >= '[1,2,3]';
SELECT '[1,2,3]'::vector >= '[1,2]';
SELECT '[1,2,3]'::vector > '[1,2,3]';
SELECT '[1,2,3]'::vector > '[1,2]';

SELECT vector_cmp('[1,2,3]', '[1,2,3]');
SELECT vector_cmp('[1,2,3]', '[0,0,0]');
SELECT vector_cmp('[0,0,0]', '[1,2,3]');
SELECT vector_cmp('[1,2]', '[1,2,3]');
SELECT vector_cmp('[1,2,3]', '[1,2]');
SELECT vector_cmp('[1,2]', '[2,3,4]');
SELECT vector_cmp('[2,3]', '[1,2,3]');

SELECT vector_dims('[1,2,3]'::vector);

SELECT round(vector_norm('[1,1]')::numeric, 5);
SELECT vector_norm('[3,4]');
SELECT vector_norm('[0,1]');
SELECT vector_norm('[3e37,4e37]')::real;
SELECT vector_norm('[0,0]');
SELECT vector_norm('[2]');

SELECT l2_distance('[0,0]'::vector, '[3,4]');
SELECT l2_distance('[0,0]'::vector, '[0,1]');
SELECT l2_distance('[1,2]'::vector, '[3]');
SELECT l2_distance('[3e38]'::vector, '[-3e38]');
SELECT l2_distance('[1,1,1,1,1,1,1,1,1]'::vector, '[1,1,1,1,1,1,1,4,5]');
SELECT '[0,0]'::vector <-> '[3,4]';

SELECT inner_product('[1,2]'::vector, '[3,4]');
SELECT inner_product('[1,2]'::vector, '[3]');
SELECT inner_product('[3e38]'::vector, '[3e38]');
SELECT inner_product('[1,1,1,1,1,1,1,1,1]'::vector, '[1,2,3,4,5,6,7,8,9]');
SELECT '[1,2]'::vector <#> '[3,4]';

SELECT cosine_distance('[1,2]'::vector, '[2,4]');
SELECT cosine_distance('[1,2]'::vector, '[0,0]');
SELECT cosine_distance('[1,1]'::vector, '[1,1]');
SELECT cosine_distance('[1,0]'::vector, '[0,2]');
SELECT cosine_distance('[1,1]'::vector, '[-1,-1]');
SELECT cosine_distance('[1,2]'::vector, '[3]');
SELECT cosine_distance('[1,1]'::vector, '[1.1,1.1]');
SELECT cosine_distance('[1,1]'::vector, '[-1.1,-1.1]');
SELECT cosine_distance('[3e38]'::vector, '[3e38]');
SELECT cosine_distance('[1,2,3,4,5,6,7,8,9]'::vector, '[1,2,3,4,5,6,7,8,9]');
SELECT cosine_distance('[1,2,3,4,5,6,7,8,9]'::vector, '[-1,-2,-3,-4,-5,-6,-7,-8,-9]');
SELECT '[1,2]'::vector <=> '[2,4]';

SELECT l1_distance('[0,0]'::vector, '[3,4]');
SELECT l1_distance('[0,0]'::vector, '[0,1]');
SELECT l1_distance('[1,2]'::vector, '[3]');
SELECT l1_distance('[3e38]'::vector, '[-3e38]');
SELECT l1_distance('[1,2,3,4,5,6,7,8,9]'::vector, '[1,2,3,4,5,6,7,8,9]');
SELECT l1_distance('[1,2,3,4,5,6,7,8,9]'::vector, '[0,3,2,5,4,7,6,9,8]');
SELECT '[0,0]'::vector <+> '[3,4]';

SELECT l2_normalize('[3,4]'::vector);
SELECT l2_normalize('[3,0]'::vector);
SELECT l2_normalize('[0,0.1]'::vector);
SELECT l2_normalize('[0,0]'::vector);
SELECT l2_normalize('[3e38]'::vector);

SELECT binary_quantize('[1,0,-1]'::vector);
SELECT binary_quantize('[0,0.1,-0.2,-0.3,0.4,0.5,0.6,-0.7,0.8,-0.9,1]'::vector);
SELECT binary_quantize('[1,2,3,-4,5,6,-7,8,1,-2,-3,4,5,-6,7,8,-1,2,3]'::vector);

SELECT subvector('[1,2,3,4,5]'::vector, 1, 3);
SELECT subvector('[1,2,3,4,5]'::vector, 3, 2);
SELECT subvector('[1,2,3,4,5]'::vector, -1, 3);
SELECT subvector('[1,2,3,4,5]'::vector, 3, 9);
SELECT subvector('[1,2,3,4,5]'::vector, 1, 0);
SELECT subvector('[1,2,3,4,5]'::vector, 3, -1);
SELECT subvector('[1,2,3,4,5]'::vector, -1, 2);
SELECT subvector('[1,2,3,4,5]'::vector, 2147483647, 10);
SELECT subvector('[1,2,3,4,5]'::vector, 3, 2147483647);
SELECT subvector('[1,2,3,4,5]'::vector, -2147483644, 2147483647);

SELECT avg(v) FROM unnest(ARRAY['[1,2,3]'::vector, '[3,5,7]']) v;
SELECT avg(v) FROM unnest(ARRAY['[1,2,3]'::vector, '[3,5,7]', NULL]) v;
SELECT avg(v) FROM unnest(ARRAY[]::vector[]) v;
SELECT avg(v) FROM unnest(ARRAY['[1,2]'::vector, '[3]']) v;
SELECT avg(v) FROM unnest(ARRAY['[3e38]'::vector, '[3e38]']) v;
SELECT vector_avg(array_agg(n)) FROM generate_series(1, 16002) n;

SELECT sum(v) FROM unnest(ARRAY['[1,2,3]'::vector, '[3,5,7]']) v;
SELECT sum(v) FROM unnest(ARRAY['[1,2,3]'::vector, '[3,5,7]', NULL]) v;
SELECT sum(v) FROM unnest(ARRAY[]::vector[]) v;
SELECT sum(v) FROM unnest(ARRAY['[1,2]'::vector, '[3]']) v;
SELECT sum(v) FROM unnest(ARRAY['[3e38]'::vector, '[3e38]']) v;
```

## File: `test/t/001_ivfflat_wal.pl`
```
# Based on postgres/contrib/bloom/t/001_wal.pl

# Test generic xlog record work for ivfflat index replication.
use strict;
use warnings FATAL => 'all';
use PostgreSQL::Test::Cluster;
use PostgreSQL::Test::Utils;
use Test::More;

my $dim = 32;

my $node_primary;
my $node_replica;

# Run few queries on both primary and replica and check their results match.
sub test_index_replay
{
	my ($test_name) = @_;

	# Wait for replica to catch up
	my $applname = $node_replica->name;
	my $caughtup_query = "SELECT pg_current_wal_lsn() <= replay_lsn FROM pg_stat_replication WHERE application_name = '$applname';";
	$node_primary->poll_query_until('postgres', $caughtup_query)
	  or die "Timed out while waiting for replica 1 to catch up";

	my @r = ();
	for (1 .. $dim)
	{
		push(@r, rand());
	}
	my $sql = join(",", @r);

	my $queries = qq(
		SET enable_seqscan = off;
		SELECT * FROM tst ORDER BY v <-> '[$sql]' LIMIT 10;
	);

	# Run test queries and compare their result
	my $primary_result = $node_primary->safe_psql("postgres", $queries);
	my $replica_result = $node_replica->safe_psql("postgres", $queries);

	is($primary_result, $replica_result, "$test_name: query result matches");
	return;
}

# Use ARRAY[random(), random(), random(), ...] over
# SELECT array_agg(random()) FROM generate_series(1, $dim)
# to generate different values for each row
my $array_sql = join(",", ('random()') x $dim);

# Initialize primary node
$node_primary = PostgreSQL::Test::Cluster->new('primary');
$node_primary->init(allows_streaming => 1);
if ($dim > 32)
{
	# TODO use wal_keep_segments for Postgres < 13
	$node_primary->append_conf('postgresql.conf', qq(wal_keep_size = 1GB));
}
if ($dim > 1500)
{
	$node_primary->append_conf('postgresql.conf', qq(maintenance_work_mem = 128MB));
}
$node_primary->start;
my $backup_name = 'my_backup';

# Take backup
$node_primary->backup($backup_name);

# Create streaming replica linking to primary
$node_replica = PostgreSQL::Test::Cluster->new('replica');
$node_replica->init_from_backup($node_primary, $backup_name, has_streaming => 1);
$node_replica->start;

# Create ivfflat index on primary
$node_primary->safe_psql("postgres", "CREATE EXTENSION vector;");
$node_primary->safe_psql("postgres", "CREATE TABLE tst (i int4, v vector($dim));");
$node_primary->safe_psql("postgres",
	"INSERT INTO tst SELECT i % 10, ARRAY[$array_sql] FROM generate_series(1, 100000) i;"
);
$node_primary->safe_psql("postgres", "CREATE INDEX ON tst USING ivfflat (v vector_l2_ops);");

# Test that queries give same result
test_index_replay('initial');

# Run 10 cycles of table modification. Run test queries after each modification.
for my $i (1 .. 10)
{
	$node_primary->safe_psql("postgres", "DELETE FROM tst WHERE i = $i;");
	test_index_replay("delete $i");
	$node_primary->safe_psql("postgres", "VACUUM tst;");
	test_index_replay("vacuum $i");
	my ($start, $end) = (100001 + ($i - 1) * 10000, 100000 + $i * 10000);
	$node_primary->safe_psql("postgres",
		"INSERT INTO tst SELECT i % 10, ARRAY[$array_sql] FROM generate_series($start, $end) i;"
	);
	test_index_replay("insert $i");
}

done_testing();
```

## File: `test/t/002_ivfflat_vacuum.pl`
```
use strict;
use warnings FATAL => 'all';
use PostgreSQL::Test::Cluster;
use PostgreSQL::Test::Utils;
use Test::More;

my $dim = 3;

my $array_sql = join(",", ('random()') x $dim);

# Initialize node
my $node = PostgreSQL::Test::Cluster->new('node');
$node->init;
$node->start;

# Create table and index
$node->safe_psql("postgres", "CREATE EXTENSION vector;");
$node->safe_psql("postgres", "CREATE TABLE tst (i int4, v vector($dim));");
$node->safe_psql("postgres",
	"INSERT INTO tst SELECT i, ARRAY[$array_sql] FROM generate_series(1, 100000) i;"
);
$node->safe_psql("postgres", "CREATE INDEX ON tst USING ivfflat (v vector_l2_ops);");

# Get size
my $size = $node->safe_psql("postgres", "SELECT pg_total_relation_size('tst_v_idx');");

# Store values
$node->safe_psql("postgres", "CREATE TABLE tmp AS SELECT * FROM tst;");

# Delete all, vacuum, and insert same data
$node->safe_psql("postgres", "DELETE FROM tst;");
$node->safe_psql("postgres", "VACUUM tst;");
$node->safe_psql("postgres", "INSERT INTO tst SELECT * FROM tmp;");

# Check size
my $new_size = $node->safe_psql("postgres", "SELECT pg_total_relation_size('tst_v_idx');");
is($size, $new_size, "size does not change");

done_testing();
```

## File: `test/t/003_ivfflat_vector_build_recall.pl`
```
use strict;
use warnings FATAL => 'all';
use PostgreSQL::Test::Cluster;
use PostgreSQL::Test::Utils;
use Test::More;

my $node;
my @queries = ();
my @expected;
my $limit = 20;

sub test_recall
{
	my ($probes, $min, $operator) = @_;
	my $correct = 0;
	my $total = 0;

	my $explain = $node->safe_psql("postgres", qq(
		SET enable_seqscan = off;
		SET ivfflat.probes = $probes;
		EXPLAIN ANALYZE SELECT i FROM tst ORDER BY v $operator '$queries[0]' LIMIT $limit;
	));
	like($explain, qr/Index Scan using idx on tst/);

	for my $i (0 .. $#queries)
	{
		my $actual = $node->safe_psql("postgres", qq(
			SET enable_seqscan = off;
			SET ivfflat.probes = $probes;
			SELECT i FROM tst ORDER BY v $operator '$queries[$i]' LIMIT $limit;
		));
		my @actual_ids = split("\n", $actual);

		my @expected_ids = split("\n", $expected[$i]);
		my %expected_set = map { $_ => 1 } @expected_ids;

		foreach (@actual_ids)
		{
			if (exists($expected_set{$_}))
			{
				$correct++;
			}
		}

		$total += $limit;
	}

	cmp_ok($correct / $total, ">=", $min, $operator);
}

# Initialize node
$node = PostgreSQL::Test::Cluster->new('node');
$node->init;
$node->start;

# Create table
$node->safe_psql("postgres", "CREATE EXTENSION vector;");
$node->safe_psql("postgres", "CREATE TABLE tst (i int4, v vector(3));");
$node->safe_psql("postgres",
	"INSERT INTO tst SELECT i, ARRAY[random(), random(), random()] FROM generate_series(1, 100000) i;"
);

# Generate queries
for (1 .. 20)
{
	my $r1 = rand();
	my $r2 = rand();
	my $r3 = rand();
	push(@queries, "[$r1,$r2,$r3]");
}

# Check each index type
my @operators = ("<->", "<#>", "<=>");
my @opclasses = ("vector_l2_ops", "vector_ip_ops", "vector_cosine_ops");

for my $i (0 .. $#operators)
{
	my $operator = $operators[$i];
	my $opclass = $opclasses[$i];

	# Get exact results
	@expected = ();
	foreach (@queries)
	{
		my $res = $node->safe_psql("postgres", qq(
			WITH top AS (
				SELECT v $operator '$_' AS distance FROM tst ORDER BY distance LIMIT $limit
			)
			SELECT i FROM tst WHERE (v $operator '$_') <= (SELECT MAX(distance) FROM top)
		));
		push(@expected, $res);
	}

	# Build index serially
	$node->safe_psql("postgres", qq(
		SET max_parallel_maintenance_workers = 0;
		CREATE INDEX idx ON tst USING ivfflat (v $opclass);
	));

	# Test approximate results
	if ($operator ne "<#>")
	{
		# TODO Fix test (uniform random vectors all have similar inner product)
		test_recall(1, 0.71, $operator);
		test_recall(10, 0.95, $operator);
	}

	# Test probes equals lists
	if ($operator eq "<=>")
	{
		test_recall(100, 0.9925, $operator);
	}
	else
	{
		test_recall(100, 1.00, $operator);
	}

	$node->safe_psql("postgres", "DROP INDEX idx;");

	# Build index in parallel
	my ($ret, $stdout, $stderr) = $node->psql("postgres", qq(
		SET client_min_messages = DEBUG;
		SET min_parallel_table_scan_size = 1;
		CREATE INDEX idx ON tst USING ivfflat (v $opclass);
	));
	is($ret, 0, $stderr);
	like($stderr, qr/using \d+ parallel workers/);

	# Test approximate results
	if ($operator ne "<#>")
	{
		# TODO Fix test (uniform random vectors all have similar inner product)
		test_recall(1, 0.71, $operator);
		test_recall(10, 0.95, $operator);
	}

	# Test probes equals lists
	if ($operator eq "<=>")
	{
		test_recall(100, 0.9925, $operator);
	}
	else
	{
		test_recall(100, 1.00, $operator);
	}

	$node->safe_psql("postgres", "DROP INDEX idx;");
}

done_testing();
```

## File: `test/t/004_ivfflat_vector_insert_recall.pl`
```
use strict;
use warnings FATAL => 'all';
use PostgreSQL::Test::Cluster;
use PostgreSQL::Test::Utils;
use Test::More;

my $node;
my @queries = ();
my @expected;
my $limit = 20;

sub test_recall
{
	my ($probes, $min, $operator) = @_;
	my $correct = 0;
	my $total = 0;

	my $explain = $node->safe_psql("postgres", qq(
		SET enable_seqscan = off;
		SET ivfflat.probes = $probes;
		EXPLAIN ANALYZE SELECT i FROM tst ORDER BY v $operator '$queries[0]' LIMIT $limit;
	));
	like($explain, qr/Index Scan using idx on tst/);

	for my $i (0 .. $#queries)
	{
		my $actual = $node->safe_psql("postgres", qq(
			SET enable_seqscan = off;
			SET ivfflat.probes = $probes;
			SELECT i FROM tst ORDER BY v $operator '$queries[$i]' LIMIT $limit;
		));
		my @actual_ids = split("\n", $actual);
		my %actual_set = map { $_ => 1 } @actual_ids;

		my @expected_ids = split("\n", $expected[$i]);

		foreach (@expected_ids)
		{
			if (exists($actual_set{$_}))
			{
				$correct++;
			}
			$total++;
		}
	}

	cmp_ok($correct / $total, ">=", $min, $operator);
}

# Initialize node
$node = PostgreSQL::Test::Cluster->new('node');
$node->init;
$node->start;

# Create table
$node->safe_psql("postgres", "CREATE EXTENSION vector;");
$node->safe_psql("postgres", "CREATE TABLE tst (i serial, v vector(3));");

# Generate queries
for (1 .. 20)
{
	my $r1 = rand();
	my $r2 = rand();
	my $r3 = rand();
	push(@queries, "[$r1,$r2,$r3]");
}

# Check each index type
my @operators = ("<->", "<#>", "<=>");
my @opclasses = ("vector_l2_ops", "vector_ip_ops", "vector_cosine_ops");

for my $i (0 .. $#operators)
{
	my $operator = $operators[$i];
	my $opclass = $opclasses[$i];

	# Add index
	$node->safe_psql("postgres", "CREATE INDEX idx ON tst USING ivfflat (v $opclass);");

	# Use concurrent inserts
	$node->pgbench(
		"--no-vacuum --client=10 --transactions=1000",
		0,
		[qr{actually processed}],
		[qr{^$}],
		"concurrent INSERTs",
		{
			"017_ivfflat_insert_recall_$opclass" => "INSERT INTO tst (v) SELECT ARRAY[random(), random(), random()] FROM generate_series(1, 10) i;"
		}
	);

	# Get exact results
	@expected = ();
	foreach (@queries)
	{
		my $res = $node->safe_psql("postgres", qq(
			SET enable_indexscan = off;
			SELECT i FROM tst ORDER BY v $operator '$_' LIMIT $limit;
		));
		push(@expected, $res);
	}

	# Test approximate results
	if ($operator ne "<#>")
	{
		# TODO Fix test (uniform random vectors all have similar inner product)
		test_recall(1, 0.71, $operator);
		test_recall(10, 0.95, $operator);
	}
	# Account for equal distances
	test_recall(100, 0.9925, $operator);

	$node->safe_psql("postgres", "DROP INDEX idx;");
	$node->safe_psql("postgres", "TRUNCATE tst;");
}

done_testing();
```

## File: `test/t/005_ivfflat_query_recall.pl`
```
use strict;
use warnings FATAL => 'all';
use PostgreSQL::Test::Cluster;
use PostgreSQL::Test::Utils;
use Test::More;

# Initialize node
my $node = PostgreSQL::Test::Cluster->new('node');
$node->init;
$node->start;

# Create table
$node->safe_psql("postgres", "CREATE EXTENSION vector;");
$node->safe_psql("postgres", "CREATE TABLE tst (i int4 primary key, v vector(3));");
$node->safe_psql("postgres",
	"INSERT INTO tst SELECT i, ARRAY[random(), random(), random()] FROM generate_series(1, 100000) i;"
);

# Add index
$node->safe_psql("postgres", "CREATE INDEX ON tst USING ivfflat (v vector_l2_ops);");

# Test 100% recall
for (1 .. 20)
{
	my $id = int(rand() * 100000);
	my $query = $node->safe_psql("postgres", "SELECT v FROM tst WHERE i = $id;");
	my $res = $node->safe_psql("postgres", qq(
		SET enable_seqscan = off;
		SELECT v FROM tst ORDER BY v <-> '$query' LIMIT 1;
	));
	is($res, $query);
}

done_testing();
```

## File: `test/t/006_ivfflat_lists.pl`
```
use strict;
use warnings FATAL => 'all';
use PostgreSQL::Test::Cluster;
use PostgreSQL::Test::Utils;
use Test::More;

# Initialize node
my $node = PostgreSQL::Test::Cluster->new('node');
$node->init;
$node->start;

# Create table
$node->safe_psql("postgres", "CREATE EXTENSION vector;");
$node->safe_psql("postgres", "CREATE TABLE tst (v vector(3));");
$node->safe_psql("postgres",
	"INSERT INTO tst SELECT ARRAY[random(), random(), random()] FROM generate_series(1, 100000) i;"
);

$node->safe_psql("postgres", "CREATE INDEX lists50 ON tst USING ivfflat (v vector_l2_ops) WITH (lists = 50);");
$node->safe_psql("postgres", "CREATE INDEX lists100 ON tst USING ivfflat (v vector_l2_ops) WITH (lists = 100);");

# Test prefers more lists
my $res = $node->safe_psql("postgres", "EXPLAIN SELECT v FROM tst ORDER BY v <-> '[0.5,0.5,0.5]' LIMIT 10;");
like($res, qr/lists100/);
unlike($res, qr/lists50/);

# Test errors with too much memory
my ($ret, $stdout, $stderr) = $node->psql("postgres",
	"CREATE INDEX lists10000 ON tst USING ivfflat (v vector_l2_ops) WITH (lists = 10000);"
);
like($stderr, qr/memory required is/);

done_testing();
```

## File: `test/t/007_ivfflat_inserts.pl`
```
use strict;
use warnings FATAL => 'all';
use PostgreSQL::Test::Cluster;
use PostgreSQL::Test::Utils;
use Test::More;

my $dim = 768;

my $array_sql = join(",", ('random()') x $dim);

# Initialize node
my $node = PostgreSQL::Test::Cluster->new('node');
$node->init;
$node->start;

# Create table and index
$node->safe_psql("postgres", "CREATE EXTENSION vector;");
$node->safe_psql("postgres", "CREATE TABLE tst (v vector($dim));");
$node->safe_psql("postgres",
	"INSERT INTO tst SELECT ARRAY[$array_sql] FROM generate_series(1, 10000) i;"
);
$node->safe_psql("postgres", "CREATE INDEX ON tst USING ivfflat (v vector_l2_ops);");

$node->pgbench(
	"--no-vacuum --client=5 --transactions=100",
	0,
	[qr{actually processed}],
	[qr{^$}],
	"concurrent INSERTs",
	{
		"007_ivfflat_inserts" => "INSERT INTO tst SELECT ARRAY[$array_sql] FROM generate_series(1, 10) i;"
	}
);

sub idx_scan
{
	# Stats do not update instantaneously
	# https://www.postgresql.org/docs/current/monitoring-stats.html#MONITORING-STATS-VIEWS
	sleep(1);
	$node->safe_psql("postgres", "SELECT idx_scan FROM pg_stat_user_indexes WHERE indexrelid = 'tst_v_idx'::regclass;");
}

my $expected = 10000 + 5 * 100 * 10;

my $count = $node->safe_psql("postgres", "SELECT COUNT(*) FROM tst;");
is($count, $expected);
is(idx_scan(), 0);

$count = $node->safe_psql("postgres", qq(
	SET enable_seqscan = off;
	SET ivfflat.probes = 100;
	SELECT COUNT(*) FROM (SELECT v FROM tst ORDER BY v <-> (SELECT v FROM tst LIMIT 1)) t;
));
is($count, $expected);
is(idx_scan(), 1);

done_testing();
```

## File: `test/t/008_ivfflat_centers.pl`
```
use strict;
use warnings FATAL => 'all';
use PostgreSQL::Test::Cluster;
use PostgreSQL::Test::Utils;
use Test::More;

# Initialize node
my $node = PostgreSQL::Test::Cluster->new('node');
$node->init;
$node->start;

# Create table
$node->safe_psql("postgres", "CREATE EXTENSION vector;");
$node->safe_psql("postgres", "CREATE TABLE tst (i int4, v vector(3));");
$node->safe_psql("postgres",
	"INSERT INTO tst SELECT i, '[1,2,3]' FROM generate_series(1, 10) i;"
);

sub test_centers
{
	my ($lists, $min) = @_;

	my ($ret, $stdout, $stderr) = $node->psql("postgres", "CREATE INDEX ON tst USING ivfflat (v vector_l2_ops) WITH (lists = $lists);");
	is($ret, 0, $stderr);
}

# Test no error for duplicate centers
test_centers(5);
test_centers(10);

$node->safe_psql("postgres",
	"INSERT INTO tst SELECT i, '[4,5,6]' FROM generate_series(1, 10) i;"
);

# Test no error for duplicate centers
test_centers(10);

done_testing();
```

## File: `test/t/009_ivfflat_filtering.pl`
```
use strict;
use warnings FATAL => 'all';
use PostgreSQL::Test::Cluster;
use PostgreSQL::Test::Utils;
use Test::More;

my $dim = 3;
my $nc = 50;
my $limit = 20;

my $array_sql = join(",", ('random()') x $dim);

# Initialize node
my $node = PostgreSQL::Test::Cluster->new('node');
$node->init;
$node->start;

# Create table and index
$node->safe_psql("postgres", "CREATE EXTENSION vector;");
$node->safe_psql("postgres", "CREATE TABLE tst (i int4, v vector($dim), c int4, t text);");
$node->safe_psql("postgres",
	"INSERT INTO tst SELECT i, ARRAY[$array_sql], i % $nc, 'test ' || i FROM generate_series(1, 10000) i;"
);
$node->safe_psql("postgres", "CREATE INDEX idx ON tst USING ivfflat (v vector_l2_ops) WITH (lists = 100);");
$node->safe_psql("postgres", "ANALYZE tst;");

# Generate query
my @r = ();
for (1 .. $dim)
{
	push(@r, rand());
}
my $query = "[" . join(",", @r) . "]";
my $c = int(rand() * $nc);

# Test attribute filtering
my $explain = $node->safe_psql("postgres", qq(
	EXPLAIN ANALYZE SELECT i FROM tst WHERE c = $c ORDER BY v <-> '$query' LIMIT $limit;
));
# TODO Do not use index
like($explain, qr/Index Scan using idx/);

# Test attribute filtering with few rows removed
$explain = $node->safe_psql("postgres", qq(
	EXPLAIN ANALYZE SELECT i FROM tst WHERE c != $c ORDER BY v <-> '$query' LIMIT $limit;
));
like($explain, qr/Index Scan using idx/);

# Test attribute filtering with few rows removed comparison
$explain = $node->safe_psql("postgres", qq(
	EXPLAIN ANALYZE SELECT i FROM tst WHERE c >= 1 ORDER BY v <-> '$query' LIMIT $limit;
));
like($explain, qr/Index Scan using idx/);

# Test attribute filtering with many rows removed comparison
$explain = $node->safe_psql("postgres", qq(
	EXPLAIN ANALYZE SELECT i FROM tst WHERE c < 1 ORDER BY v <-> '$query' LIMIT $limit;
));
# TODO Do not use index
like($explain, qr/Index Scan using idx/);

# Test attribute filtering with few rows removed like
$explain = $node->safe_psql("postgres", qq(
	EXPLAIN ANALYZE SELECT i FROM tst WHERE t LIKE '%%test%%' ORDER BY v <-> '$query' LIMIT $limit;
));
like($explain, qr/Index Scan using idx/);

# Test attribute filtering with many rows removed like
$explain = $node->safe_psql("postgres", qq(
	EXPLAIN ANALYZE SELECT i FROM tst WHERE t LIKE '%%other%%' ORDER BY v <-> '$query' LIMIT $limit;
));
like($explain, qr/Seq Scan/);

# Test distance filtering
$explain = $node->safe_psql("postgres", qq(
	EXPLAIN ANALYZE SELECT i FROM tst WHERE v <-> '$query' < 1 ORDER BY v <-> '$query' LIMIT $limit;
));
like($explain, qr/Index Scan using idx/);

# Test distance filtering greater than distance
$explain = $node->safe_psql("postgres", qq(
	EXPLAIN ANALYZE SELECT i FROM tst WHERE v <-> '$query' > 1 ORDER BY v <-> '$query' LIMIT $limit;
));
# TODO Do not use index
like($explain, qr/Index Scan using idx/);

# Test distance filtering without order
$explain = $node->safe_psql("postgres", qq(
	EXPLAIN ANALYZE SELECT i FROM tst WHERE v <-> '$query' < 1;
));
like($explain, qr/Seq Scan/);

# Test distance filtering without limit
$explain = $node->safe_psql("postgres", qq(
	EXPLAIN ANALYZE SELECT i FROM tst WHERE v <-> '$query' < 1 ORDER BY v <-> '$query';
));
like($explain, qr/Seq Scan/);

# Test attribute index
$node->safe_psql("postgres", "CREATE INDEX attribute_idx ON tst (c);");
$explain = $node->safe_psql("postgres", qq(
	EXPLAIN ANALYZE SELECT i FROM tst WHERE c = $c ORDER BY v <-> '$query' LIMIT $limit;
));
# TODO Use attribute index
like($explain, qr/Index Scan using idx/);

# Test partial index
$node->safe_psql("postgres", "CREATE INDEX partial_idx ON tst USING ivfflat (v vector_l2_ops) WITH (lists = 5) WHERE (c = $c);");
$explain = $node->safe_psql("postgres", qq(
	EXPLAIN ANALYZE SELECT i FROM tst WHERE c = $c ORDER BY v <-> '$query' LIMIT $limit;
));
like($explain, qr/Index Scan using partial_idx/);

done_testing();
```

## File: `test/t/010_hnsw_wal.pl`
```
# Based on postgres/contrib/bloom/t/001_wal.pl

# Test generic xlog record work for hnsw index replication.
use strict;
use warnings FATAL => 'all';
use PostgreSQL::Test::Cluster;
use PostgreSQL::Test::Utils;
use Test::More;

my $dim = 32;

my $node_primary;
my $node_replica;

# Run few queries on both primary and replica and check their results match.
sub test_index_replay
{
	my ($test_name) = @_;

	# Wait for replica to catch up
	my $applname = $node_replica->name;
	my $caughtup_query = "SELECT pg_current_wal_lsn() <= replay_lsn FROM pg_stat_replication WHERE application_name = '$applname';";
	$node_primary->poll_query_until('postgres', $caughtup_query)
	  or die "Timed out while waiting for replica 1 to catch up";

	my @r = ();
	for (1 .. $dim)
	{
		push(@r, rand());
	}
	my $sql = join(",", @r);

	my $queries = qq(
		SET enable_seqscan = off;
		SELECT * FROM tst ORDER BY v <-> '[$sql]' LIMIT 10;
	);

	# Run test queries and compare their result
	my $primary_result = $node_primary->safe_psql("postgres", $queries);
	my $replica_result = $node_replica->safe_psql("postgres", $queries);

	is($primary_result, $replica_result, "$test_name: query result matches");
	return;
}

# Use ARRAY[random(), random(), random(), ...] over
# SELECT array_agg(random()) FROM generate_series(1, $dim)
# to generate different values for each row
my $array_sql = join(",", ('random()') x $dim);

# Initialize primary node
$node_primary = PostgreSQL::Test::Cluster->new('primary');
$node_primary->init(allows_streaming => 1);
if ($dim > 32)
{
	# TODO use wal_keep_segments for Postgres < 13
	$node_primary->append_conf('postgresql.conf', qq(wal_keep_size = 1GB));
}
if ($dim > 1500)
{
	$node_primary->append_conf('postgresql.conf', qq(maintenance_work_mem = 128MB));
}
$node_primary->start;
my $backup_name = 'my_backup';

# Take backup
$node_primary->backup($backup_name);

# Create streaming replica linking to primary
$node_replica = PostgreSQL::Test::Cluster->new('replica');
$node_replica->init_from_backup($node_primary, $backup_name, has_streaming => 1);
$node_replica->start;

# Create hnsw index on primary
$node_primary->safe_psql("postgres", "CREATE EXTENSION vector;");
$node_primary->safe_psql("postgres", "CREATE TABLE tst (i int4, v vector($dim));");
$node_primary->safe_psql("postgres",
	"INSERT INTO tst SELECT i % 10, ARRAY[$array_sql] FROM generate_series(1, 1000) i;"
);
$node_primary->safe_psql("postgres", "CREATE INDEX ON tst USING hnsw (v vector_l2_ops);");

# Test that queries give same result
test_index_replay('initial');

# Run 10 cycles of table modification. Run test queries after each modification.
for my $i (1 .. 10)
{
	$node_primary->safe_psql("postgres", "DELETE FROM tst WHERE i = $i;");
	test_index_replay("delete $i");
	$node_primary->safe_psql("postgres", "VACUUM tst;");
	test_index_replay("vacuum $i");
	my ($start, $end) = (1001 + ($i - 1) * 100, 1000 + $i * 100);
	$node_primary->safe_psql("postgres",
		"INSERT INTO tst SELECT i % 10, ARRAY[$array_sql] FROM generate_series($start, $end) i;"
	);
	test_index_replay("insert $i");
}

done_testing();
```

## File: `test/t/011_hnsw_vacuum.pl`
```
use strict;
use warnings FATAL => 'all';
use PostgreSQL::Test::Cluster;
use PostgreSQL::Test::Utils;
use Test::More;

my $dim = 3;

my @r = ();
for (1 .. $dim)
{
	my $v = int(rand(1000)) + 1;
	push(@r, "i % $v");
}
my $array_sql = join(", ", @r);

# Initialize node
my $node = PostgreSQL::Test::Cluster->new('node');
$node->init;
$node->start;

# Create table and index
$node->safe_psql("postgres", "CREATE EXTENSION vector;");
$node->safe_psql("postgres", "CREATE TABLE tst (i int4, v vector($dim));");
$node->safe_psql("postgres",
	"INSERT INTO tst SELECT i, ARRAY[$array_sql] FROM generate_series(1, 10000) i;"
);
$node->safe_psql("postgres", "CREATE INDEX ON tst USING hnsw (v vector_l2_ops);");

# Get size
my $size = $node->safe_psql("postgres", "SELECT pg_total_relation_size('tst_v_idx');");

# Delete all, vacuum, and insert same data
$node->safe_psql("postgres", "DELETE FROM tst;");
$node->safe_psql("postgres", "VACUUM tst;");
$node->safe_psql("postgres",
	"INSERT INTO tst SELECT i, ARRAY[$array_sql] FROM generate_series(1, 10000) i;"
);

# Check size
# May increase some due to different levels
my $new_size = $node->safe_psql("postgres", "SELECT pg_total_relation_size('tst_v_idx');");
cmp_ok($new_size, "<=", $size * 1.02, "size does not increase too much");

# Delete all but one
$node->safe_psql("postgres", "DELETE FROM tst WHERE i != 123;");
$node->safe_psql("postgres", "VACUUM tst;");
my $res = $node->safe_psql("postgres", qq(
	SET enable_seqscan = off;
	SELECT i FROM tst ORDER BY v <-> '[0,0,0]' LIMIT 10;
));
is($res, 123);

done_testing();
```

## File: `test/t/012_hnsw_vector_build_recall.pl`
```
use strict;
use warnings FATAL => 'all';
use PostgreSQL::Test::Cluster;
use PostgreSQL::Test::Utils;
use Test::More;

my $node;
my @queries = ();
my @expected;
my $limit = 20;
my $array_sql = join(",", ('random() * random()') x 3);

sub test_recall
{
	my ($min, $operator) = @_;
	my $correct = 0;
	my $total = 0;

	my $explain = $node->safe_psql("postgres", qq(
		SET enable_seqscan = off;
		EXPLAIN ANALYZE SELECT i FROM tst ORDER BY v $operator '$queries[0]' LIMIT $limit;
	));
	like($explain, qr/Index Scan/);

	for my $i (0 .. $#queries)
	{
		my $actual = $node->safe_psql("postgres", qq(
			SET enable_seqscan = off;
			SELECT i FROM tst ORDER BY v $operator '$queries[$i]' LIMIT $limit;
		));
		my @actual_ids = split("\n", $actual);
		my %actual_set = map { $_ => 1 } @actual_ids;

		my @expected_ids = split("\n", $expected[$i]);

		foreach (@expected_ids)
		{
			if (exists($actual_set{$_}))
			{
				$correct++;
			}
			$total++;
		}
	}

	cmp_ok($correct / $total, ">=", $min, $operator);
}

# Initialize node
$node = PostgreSQL::Test::Cluster->new('node');
$node->init;
$node->start;

# Create table
$node->safe_psql("postgres", "CREATE EXTENSION vector;");
$node->safe_psql("postgres", "CREATE TABLE tst (i int4, v vector(3));");
$node->safe_psql("postgres",
	"INSERT INTO tst SELECT i, ARRAY[$array_sql] FROM generate_series(1, 10000) i;"
);

# Generate queries
for (1 .. 20)
{
	my $r1 = rand();
	my $r2 = rand();
	my $r3 = rand();
	push(@queries, "[$r1,$r2,$r3]");
}

# Check each index type
my @operators = ("<->", "<#>", "<=>", "<+>");
my @opclasses = ("vector_l2_ops", "vector_ip_ops", "vector_cosine_ops", "vector_l1_ops");

for my $i (0 .. $#operators)
{
	my $operator = $operators[$i];
	my $opclass = $opclasses[$i];

	# Get exact results
	@expected = ();
	foreach (@queries)
	{
		my $res = $node->safe_psql("postgres", "SELECT i FROM tst ORDER BY v $operator '$_' LIMIT $limit;");
		push(@expected, $res);
	}

	# Build index serially
	$node->safe_psql("postgres", qq(
		SET max_parallel_maintenance_workers = 0;
		CREATE INDEX idx ON tst USING hnsw (v $opclass);
	));

	# Test approximate results
	my $min = $operator eq "<#>" ? 0.97 : 0.99;
	test_recall($min, $operator);

	$node->safe_psql("postgres", "DROP INDEX idx;");

	# Build index in parallel in memory
	my ($ret, $stdout, $stderr) = $node->psql("postgres", qq(
		SET client_min_messages = DEBUG;
		SET min_parallel_table_scan_size = 1;
		CREATE INDEX idx ON tst USING hnsw (v $opclass);
	));
	is($ret, 0, $stderr);
	like($stderr, qr/using \d+ parallel workers/);

	# Test approximate results
	test_recall($min, $operator);

	$node->safe_psql("postgres", "DROP INDEX idx;");

	# Build index in parallel on disk
	# Set parallel_workers on table to use workers with low maintenance_work_mem
	($ret, $stdout, $stderr) = $node->psql("postgres", qq(
		ALTER TABLE tst SET (parallel_workers = 2);
		SET client_min_messages = DEBUG;
		SET maintenance_work_mem = '4MB';
		CREATE INDEX idx ON tst USING hnsw (v $opclass);
		ALTER TABLE tst RESET (parallel_workers);
	));
	is($ret, 0, $stderr);
	like($stderr, qr/using \d+ parallel workers/);
	like($stderr, qr/hnsw graph no longer fits into maintenance_work_mem/);

	$node->safe_psql("postgres", "DROP INDEX idx;");
}

done_testing();
```

## File: `test/t/013_hnsw_vector_insert_recall.pl`
```
use strict;
use warnings FATAL => 'all';
use PostgreSQL::Test::Cluster;
use PostgreSQL::Test::Utils;
use Test::More;

my $node;
my @queries = ();
my @expected;
my $limit = 20;
my $array_sql = join(",", ('random() * random()') x 3);

sub test_recall
{
	my ($min, $operator) = @_;
	my $correct = 0;
	my $total = 0;

	my $explain = $node->safe_psql("postgres", qq(
		SET enable_seqscan = off;
		EXPLAIN ANALYZE SELECT i FROM tst ORDER BY v $operator '$queries[0]' LIMIT $limit;
	));
	like($explain, qr/Index Scan/);

	for my $i (0 .. $#queries)
	{
		my $actual = $node->safe_psql("postgres", qq(
			SET enable_seqscan = off;
			SELECT i FROM tst ORDER BY v $operator '$queries[$i]' LIMIT $limit;
		));
		my @actual_ids = split("\n", $actual);
		my %actual_set = map { $_ => 1 } @actual_ids;

		my @expected_ids = split("\n", $expected[$i]);

		foreach (@expected_ids)
		{
			if (exists($actual_set{$_}))
			{
				$correct++;
			}
			$total++;
		}
	}

	cmp_ok($correct / $total, ">=", $min, $operator);
}

# Initialize node
$node = PostgreSQL::Test::Cluster->new('node');
$node->init;
$node->start;

# Create table
$node->safe_psql("postgres", "CREATE EXTENSION vector;");
$node->safe_psql("postgres", "CREATE TABLE tst (i serial, v vector(3));");

# Generate queries
for (1 .. 20)
{
	my $r1 = rand();
	my $r2 = rand();
	my $r3 = rand();
	push(@queries, "[$r1,$r2,$r3]");
}

# Check each index type
my @operators = ("<->", "<#>", "<=>", "<+>");
my @opclasses = ("vector_l2_ops", "vector_ip_ops", "vector_cosine_ops", "vector_l1_ops");

for my $i (0 .. $#operators)
{
	my $operator = $operators[$i];
	my $opclass = $opclasses[$i];

	# Add index
	$node->safe_psql("postgres", "CREATE INDEX idx ON tst USING hnsw (v $opclass);");

	# Use concurrent inserts
	$node->pgbench(
		"--no-vacuum --client=10 --transactions=1000",
		0,
		[qr{actually processed}],
		[qr{^$}],
		"concurrent INSERTs",
		{
			"013_hnsw_insert_recall_$opclass" => "INSERT INTO tst (v) VALUES (ARRAY[$array_sql]);"
		}
	);

	# Get exact results
	@expected = ();
	foreach (@queries)
	{
		my $res = $node->safe_psql("postgres", qq(
			SET enable_indexscan = off;
			SELECT i FROM tst ORDER BY v $operator '$_' LIMIT $limit;
		));
		push(@expected, $res);
	}

	# Test approximate results
	my $min = $operator eq "<#>" ? 0.97 : 0.99;
	test_recall($min, $operator);

	$node->safe_psql("postgres", "DROP INDEX idx;");
	$node->safe_psql("postgres", "TRUNCATE tst;");
}

done_testing();
```

## File: `test/t/014_hnsw_vector_vacuum_recall.pl`
```
use strict;
use warnings FATAL => 'all';
use PostgreSQL::Test::Cluster;
use PostgreSQL::Test::Utils;
use Test::More;

my $node;
my @queries = ();
my @expected;
my $limit = 20;

sub test_recall
{
	my ($min, $ef_search, $test_name) = @_;
	my $correct = 0;
	my $total = 0;

	my $explain = $node->safe_psql("postgres", qq(
		SET enable_seqscan = off;
		SET hnsw.ef_search = $ef_search;
		EXPLAIN ANALYZE SELECT i FROM tst ORDER BY v <-> '$queries[0]' LIMIT $limit;
	));
	like($explain, qr/Index Scan/);

	for my $i (0 .. $#queries)
	{
		my $actual = $node->safe_psql("postgres", qq(
			SET enable_seqscan = off;
			SET hnsw.ef_search = $ef_search;
			SELECT i FROM tst ORDER BY v <-> '$queries[$i]' LIMIT $limit;
		));
		my @actual_ids = split("\n", $actual);
		my %actual_set = map { $_ => 1 } @actual_ids;

		my @expected_ids = split("\n", $expected[$i]);

		foreach (@expected_ids)
		{
			if (exists($actual_set{$_}))
			{
				$correct++;
			}
			$total++;
		}
	}

	cmp_ok($correct / $total, ">=", $min, $test_name);
}

# Initialize node
$node = PostgreSQL::Test::Cluster->new('node');
$node->init;
$node->start;

# Create table
$node->safe_psql("postgres", "CREATE EXTENSION vector;");
$node->safe_psql("postgres", "CREATE TABLE tst (i int4, v vector(3));");
$node->safe_psql("postgres", "ALTER TABLE tst SET (autovacuum_enabled = false);");
$node->safe_psql("postgres",
	"INSERT INTO tst SELECT i, ARRAY[random(), random(), random()] FROM generate_series(1, 10000) i;"
);

# Add index
$node->safe_psql("postgres", "CREATE INDEX ON tst USING hnsw (v vector_l2_ops) WITH (m = 4, ef_construction = 8);");

# Delete data
$node->safe_psql("postgres", "DELETE FROM tst WHERE i > 2500;");

# Generate queries
for (1 .. 20)
{
	my $r1 = rand();
	my $r2 = rand();
	my $r3 = rand();
	push(@queries, "[$r1,$r2,$r3]");
}

# Get exact results
@expected = ();
foreach (@queries)
{
	my $res = $node->safe_psql("postgres", qq(
		SET enable_indexscan = off;
		SELECT i FROM tst ORDER BY v <-> '$_' LIMIT $limit;
	));
	push(@expected, $res);
}

test_recall(0.18, $limit, "before vacuum");
test_recall(0.93, 100, "before vacuum");

# TODO Test concurrent inserts with vacuum
$node->safe_psql("postgres", "VACUUM tst;");

test_recall(0.95, $limit, "after vacuum");

done_testing();
```

## File: `test/t/015_hnsw_vector_duplicates.pl`
```
use strict;
use warnings FATAL => 'all';
use PostgreSQL::Test::Cluster;
use PostgreSQL::Test::Utils;
use Test::More;

# Initialize node
my $node = PostgreSQL::Test::Cluster->new('node');
$node->init;
$node->start;

# Create table
$node->safe_psql("postgres", "CREATE EXTENSION vector;");
$node->safe_psql("postgres", "CREATE TABLE tst (v vector(3));");

sub insert_vectors
{
	for my $i (1 .. 20)
	{
		$node->safe_psql("postgres", "INSERT INTO tst VALUES ('[1,1,1]');");
	}
}

sub test_duplicates
{
	my $res = $node->safe_psql("postgres", qq(
		SET enable_seqscan = off;
		SET hnsw.ef_search = 1;
		SELECT COUNT(*) FROM (SELECT * FROM tst ORDER BY v <-> '[1,1,1]') t;
	));
	is($res, 10);
}

# Test duplicates with build
insert_vectors();
$node->safe_psql("postgres", "CREATE INDEX idx ON tst USING hnsw (v vector_l2_ops);");
test_duplicates();

# Reset
$node->safe_psql("postgres", "TRUNCATE tst;");

# Test duplicates with inserts
insert_vectors();
test_duplicates();

# Test fallback path for inserts
$node->pgbench(
	"--no-vacuum --client=5 --transactions=100",
	0,
	[qr{actually processed}],
	[qr{^$}],
	"concurrent INSERTs",
	{
		"015_hnsw_duplicates" => "INSERT INTO tst VALUES ('[1,1,1]');"
	}
);

done_testing();
```

## File: `test/t/016_hnsw_inserts.pl`
```
use strict;
use warnings FATAL => 'all';
use PostgreSQL::Test::Cluster;
use PostgreSQL::Test::Utils;
use Test::More;

# Ensures elements and neighbors on both same and different pages
my $dim = 1900;

my $array_sql = join(",", ('random()') x $dim);

# Initialize node
my $node = PostgreSQL::Test::Cluster->new('node');
$node->init;
$node->start;

# Create table and index
$node->safe_psql("postgres", "CREATE EXTENSION vector;");
$node->safe_psql("postgres", "CREATE TABLE tst (v vector($dim));");
$node->safe_psql("postgres", "CREATE INDEX ON tst USING hnsw (v vector_l2_ops);");

sub idx_scan
{
	# Stats do not update instantaneously
	# https://www.postgresql.org/docs/current/monitoring-stats.html#MONITORING-STATS-VIEWS
	sleep(1);
	$node->safe_psql("postgres", "SELECT idx_scan FROM pg_stat_user_indexes WHERE indexrelid = 'tst_v_idx'::regclass;");
}

for my $i (1 .. 20)
{
	$node->pgbench(
		"--no-vacuum --client=10 --transactions=1",
		0,
		[qr{actually processed}],
		[qr{^$}],
		"concurrent INSERTs",
		{
			"014_hnsw_inserts_$i" => "INSERT INTO tst VALUES (ARRAY[$array_sql]);"
		}
	);

	my $count = $node->safe_psql("postgres", qq(
		SET enable_seqscan = off;
		SELECT COUNT(*) FROM (SELECT v FROM tst ORDER BY v <-> (SELECT v FROM tst LIMIT 1)) t;
	));
	is($count, 10);

	$node->safe_psql("postgres", "TRUNCATE tst;");
}

$node->pgbench(
	"--no-vacuum --client=20 --transactions=5",
	0,
	[qr{actually processed}],
	[qr{^$}],
	"concurrent INSERTs",
	{
		"014_hnsw_inserts" => "INSERT INTO tst SELECT ARRAY[$array_sql] FROM generate_series(1, 10) i;"
	}
);

my $count = $node->safe_psql("postgres", qq(
	SET enable_seqscan = off;
	SET hnsw.ef_search = 1000;
	SELECT COUNT(*) FROM (SELECT v FROM tst ORDER BY v <-> (SELECT v FROM tst LIMIT 1)) t;
));
# Elements may lose all incoming connections with the HNSW algorithm
# Vacuuming can fix this if one of the elements neighbors is deleted
cmp_ok($count, ">=", 997);

is(idx_scan(), 21);

done_testing();
```

## File: `test/t/017_hnsw_filtering.pl`
```
use strict;
use warnings FATAL => 'all';
use PostgreSQL::Test::Cluster;
use PostgreSQL::Test::Utils;
use Test::More;

my $dim = 3;
my $nc = 50;
my $limit = 20;

my $array_sql = join(",", ('random()') x $dim);

# Initialize node
my $node = PostgreSQL::Test::Cluster->new('node');
$node->init;
$node->start;

# Create table and index
$node->safe_psql("postgres", "CREATE EXTENSION vector;");
$node->safe_psql("postgres", "CREATE TABLE tst (i int4, v vector($dim), c int4, t text);");
$node->safe_psql("postgres", "CREATE TABLE cat (i int4 PRIMARY KEY, t text, b boolean);");
$node->safe_psql("postgres",
	"INSERT INTO tst SELECT i, ARRAY[$array_sql], i % $nc, 'test ' || i FROM generate_series(1, 10000) i;"
);
$node->safe_psql("postgres",
	"INSERT INTO cat SELECT i, 'cat ' || i, i % 5 = 0 FROM generate_series(1, $nc) i;"
);
$node->safe_psql("postgres", "CREATE INDEX idx ON tst USING hnsw (v vector_l2_ops);");
$node->safe_psql("postgres", "ANALYZE tst;");

# Generate query
my @r = ();
for (1 .. $dim)
{
	push(@r, rand());
}
my $query = "[" . join(",", @r) . "]";
my $c = int(rand() * $nc);

# Test attribute filtering
my $explain = $node->safe_psql("postgres", qq(
	EXPLAIN ANALYZE SELECT i FROM tst WHERE c = $c ORDER BY v <-> '$query' LIMIT $limit;
));
like($explain, qr/Seq Scan/);

# Test attribute filtering with few rows removed
$explain = $node->safe_psql("postgres", qq(
	EXPLAIN ANALYZE SELECT i FROM tst WHERE c != $c ORDER BY v <-> '$query' LIMIT $limit;
));
like($explain, qr/Index Scan using idx/);

# Test attribute filtering with few rows removed comparison
$explain = $node->safe_psql("postgres", qq(
	EXPLAIN ANALYZE SELECT i FROM tst WHERE c >= 1 ORDER BY v <-> '$query' LIMIT $limit;
));
like($explain, qr/Index Scan using idx/);

# Test attribute filtering with many rows removed comparison
$explain = $node->safe_psql("postgres", qq(
	EXPLAIN ANALYZE SELECT i FROM tst WHERE c < 1 ORDER BY v <-> '$query' LIMIT $limit;
));
like($explain, qr/Seq Scan/);

# Test attribute filtering with few rows removed like
$explain = $node->safe_psql("postgres", qq(
	EXPLAIN ANALYZE SELECT i FROM tst WHERE t LIKE '%%test%%' ORDER BY v <-> '$query' LIMIT $limit;
));
like($explain, qr/Index Scan using idx/);

# Test attribute filtering with many rows removed like
$explain = $node->safe_psql("postgres", qq(
	EXPLAIN ANALYZE SELECT i FROM tst WHERE t LIKE '%%other%%' ORDER BY v <-> '$query' LIMIT $limit;
));
like($explain, qr/Seq Scan/);

# Test distance filtering
$explain = $node->safe_psql("postgres", qq(
	EXPLAIN ANALYZE SELECT i FROM tst WHERE v <-> '$query' < 1 ORDER BY v <-> '$query' LIMIT $limit;
));
like($explain, qr/Index Scan using idx/);

# Test distance filtering greater than distance
$explain = $node->safe_psql("postgres", qq(
	EXPLAIN ANALYZE SELECT i FROM tst WHERE v <-> '$query' > 1 ORDER BY v <-> '$query' LIMIT $limit;
));
# TODO Do not use index
like($explain, qr/Index Scan using idx/);

# Test distance filtering without order
$explain = $node->safe_psql("postgres", qq(
	EXPLAIN ANALYZE SELECT i FROM tst WHERE v <-> '$query' < 1;
));
like($explain, qr/Seq Scan/);

# Test distance filtering without limit
$explain = $node->safe_psql("postgres", qq(
	EXPLAIN ANALYZE SELECT i FROM tst WHERE v <-> '$query' < 1 ORDER BY v <-> '$query';
));
like($explain, qr/Seq Scan/);

# Test join
$explain = $node->safe_psql("postgres", qq(
	EXPLAIN ANALYZE SELECT cat.t FROM cat INNER JOIN tst ON cat.i = tst.c ORDER BY v <-> '$query' LIMIT $limit;
));
like($explain, qr/Index Scan using idx/);

# Test join with attribute filtering
$explain = $node->safe_psql("postgres", qq(
	EXPLAIN ANALYZE SELECT cat.t FROM cat INNER JOIN tst ON cat.i = tst.c WHERE cat.b = 't' ORDER BY v <-> '$query' LIMIT $limit;
));
like($explain, qr/Index Scan using idx/);

# Test attribute index
$node->safe_psql("postgres", "CREATE INDEX attribute_idx ON tst (c);");
$explain = $node->safe_psql("postgres", qq(
	EXPLAIN ANALYZE SELECT i FROM tst WHERE c = $c ORDER BY v <-> '$query' LIMIT $limit;
));
# Use attribute index
like($explain, qr/Bitmap Index Scan on attribute_idx/);

# Test partial index
$node->safe_psql("postgres", "CREATE INDEX partial_idx ON tst USING hnsw (v vector_l2_ops) WHERE (c = $c);");
$explain = $node->safe_psql("postgres", qq(
	EXPLAIN ANALYZE SELECT i FROM tst WHERE c = $c ORDER BY v <-> '$query' LIMIT $limit;
));
like($explain, qr/Index Scan using partial_idx/);

done_testing();
```

## File: `test/t/018_aggregates.pl`
```
use strict;
use warnings FATAL => 'all';
use PostgreSQL::Test::Cluster;
use PostgreSQL::Test::Utils;
use Test::More;

# Initialize node
my $node = PostgreSQL::Test::Cluster->new('node');
$node->init;
$node->start;

# Create table
$node->safe_psql("postgres", "CREATE EXTENSION vector;");
$node->safe_psql("postgres", "CREATE TABLE tst (r1 real, r2 real, r3 real, v vector(3));");
$node->safe_psql("postgres", qq(
	INSERT INTO tst SELECT r1, r2, r3, ARRAY[r1, r2, r3] FROM (
		SELECT random() + 1.01 AS r1, random() + 2.01 AS r2, random() + 3.01 AS r3 FROM generate_series(1, 1000000) t
	) i;
));

sub test_aggregate
{
	my ($agg) = @_;

	# Test value
	my $res = $node->safe_psql("postgres", "SELECT $agg(v) FROM tst;");
	like($res, qr/\[1\.5/);
	like($res, qr/,2\.5/);
	like($res, qr/,3\.5/);

	# Test matches real for avg
	# Cannot test sum since sum(real) varies between calls
	if ($agg eq 'avg')
	{
		my $r1 = $node->safe_psql("postgres", "SELECT $agg(r1)::float4 FROM tst;");
		my $r2 = $node->safe_psql("postgres", "SELECT $agg(r2)::float4 FROM tst;");
		my $r3 = $node->safe_psql("postgres", "SELECT $agg(r3)::float4 FROM tst;");
		is($res, "[$r1,$r2,$r3]");
	}

	# Test explain
	my $explain = $node->safe_psql("postgres", "EXPLAIN SELECT $agg(v) FROM tst;");
	like($explain, qr/Partial Aggregate/);

	# Test halfvec
	$res = $node->safe_psql("postgres", "SELECT $agg(v::halfvec) FROM tst;");
	if ($agg eq 'avg')
	{
		like($res, qr/\[1\.5/);
		like($res, qr/,2\.5/);
		like($res, qr/,3\.5/);
	}
	else
	{
		# Does not raise overflow error in this instance due to loss of precision
		is($res, "[24576,24576,49152]");
	}
}

test_aggregate('avg');
test_aggregate('sum');

done_testing();
```

## File: `test/t/019_storage.pl`
```
use strict;
use warnings FATAL => 'all';
use PostgreSQL::Test::Cluster;
use PostgreSQL::Test::Utils;
use Test::More;

my $dim = 1024;

# Initialize node
my $node = PostgreSQL::Test::Cluster->new('node');
$node->init;
$node->start;

# Create table
$node->safe_psql("postgres", "CREATE EXTENSION vector;");
$node->safe_psql("postgres", "CREATE TABLE tst (v1 vector(1024), v2 vector(1024), v3 vector(1024));");

# Test insert succeeds
$node->safe_psql("postgres",
	"INSERT INTO tst SELECT array_agg(n), array_agg(n), array_agg(n) FROM generate_series(1, $dim) n"
);

# Change storage to PLAIN
$node->safe_psql("postgres", "ALTER TABLE tst ALTER COLUMN v1 SET STORAGE PLAIN");
$node->safe_psql("postgres", "ALTER TABLE tst ALTER COLUMN v2 SET STORAGE PLAIN");
$node->safe_psql("postgres", "ALTER TABLE tst ALTER COLUMN v3 SET STORAGE PLAIN");

# Test insert fails
my ($ret, $stdout, $stderr) = $node->psql("postgres",
	"INSERT INTO tst SELECT array_agg(n), array_agg(n), array_agg(n) FROM generate_series(1, $dim) n"
);
like($stderr, qr/row is too big/);

done_testing();
```

## File: `test/t/020_hnsw_bit_build_recall.pl`
```
use strict;
use warnings FATAL => 'all';
use PostgreSQL::Test::Cluster;
use PostgreSQL::Test::Utils;
use Test::More;

my $node;
my @queries = ();
my @expected;
my $limit = 20;
my $dim = 52;
my $max = 2**$dim;

sub test_recall
{
	my ($min, $operator) = @_;
	my $correct = 0;
	my $total = 0;

	my $explain = $node->safe_psql("postgres", qq(
		SET enable_seqscan = off;
		SET hnsw.ef_search = 100;
		EXPLAIN ANALYZE SELECT i FROM tst ORDER BY v $operator $queries[0] LIMIT $limit;
	));
	like($explain, qr/Index Scan/);

	for my $i (0 .. $#queries)
	{
		my $actual = $node->safe_psql("postgres", qq(
			SET enable_seqscan = off;
			SET hnsw.ef_search = 100;
			SELECT i FROM tst ORDER BY v $operator $queries[$i] LIMIT $limit;
		));
		my @actual_ids = split("\n", $actual);

		my @expected_ids = split("\n", $expected[$i]);
		my %expected_set = map { $_ => 1 } @expected_ids;

		foreach (@actual_ids)
		{
			if (exists($expected_set{$_}))
			{
				$correct++;
			}
		}

		$total += $limit;
	}

	cmp_ok($correct / $total, ">=", $min, $operator);
}

# Initialize node
$node = PostgreSQL::Test::Cluster->new('node');
$node->init;
$node->start;

# Create table
$node->safe_psql("postgres", "CREATE EXTENSION vector;");
$node->safe_psql("postgres", "CREATE TABLE tst (i int4, v bit($dim));");
$node->safe_psql("postgres",
	"INSERT INTO tst SELECT i, (random() * $max)::bigint::bit($dim) FROM generate_series(1, 10000) i;"
);

# Generate queries
for (1 .. 20)
{
	my $r = int(rand() * $max);
	push(@queries, "${r}::bigint::bit($dim)");
}

# Check each index type
my @operators = ("<~>", "<\%>");
my @opclasses = ("bit_hamming_ops", "bit_jaccard_ops");

for my $i (0 .. $#operators)
{
	my $operator = $operators[$i];
	my $opclass = $opclasses[$i];

	# Get exact results
	@expected = ();
	foreach (@queries)
	{
		# Handle ties
		my $res = $node->safe_psql("postgres", qq(
			WITH top AS (
				SELECT v $operator $_ AS distance FROM tst ORDER BY distance LIMIT $limit
			)
			SELECT i FROM tst WHERE (v $operator $_) <= (SELECT MAX(distance) FROM top)
		));
		push(@expected, $res);
	}

	# Build index serially
	$node->safe_psql("postgres", qq(
		SET max_parallel_maintenance_workers = 0;
		CREATE INDEX idx ON tst USING hnsw (v $opclass);
	));

	# Test approximate results
	my $min = $operator eq "<\%>" ? 0.95 : 0.98;
	test_recall($min, $operator);

	$node->safe_psql("postgres", "DROP INDEX idx;");

	# Build index in parallel in memory
	my ($ret, $stdout, $stderr) = $node->psql("postgres", qq(
		SET client_min_messages = DEBUG;
		SET min_parallel_table_scan_size = 1;
		CREATE INDEX idx ON tst USING hnsw (v $opclass);
	));
	is($ret, 0, $stderr);
	like($stderr, qr/using \d+ parallel workers/);

	# Test approximate results
	test_recall($min, $operator);

	$node->safe_psql("postgres", "DROP INDEX idx;");

	# Build index in parallel on disk
	# Set parallel_workers on table to use workers with low maintenance_work_mem
	($ret, $stdout, $stderr) = $node->psql("postgres", qq(
		ALTER TABLE tst SET (parallel_workers = 2);
		SET client_min_messages = DEBUG;
		SET maintenance_work_mem = '4MB';
		CREATE INDEX idx ON tst USING hnsw (v $opclass);
		ALTER TABLE tst RESET (parallel_workers);
	));
	is($ret, 0, $stderr);
	like($stderr, qr/using \d+ parallel workers/);
	like($stderr, qr/hnsw graph no longer fits into maintenance_work_mem/);

	$node->safe_psql("postgres", "DROP INDEX idx;");
}

done_testing();
```

## File: `test/t/021_hnsw_bit_insert_recall.pl`
```
use strict;
use warnings FATAL => 'all';
use PostgreSQL::Test::Cluster;
use PostgreSQL::Test::Utils;
use Test::More;

my $node;
my @queries = ();
my @expected;
my $limit = 20;
my $dim = 52;
my $max = 2**$dim;

sub test_recall
{
	my ($min, $operator) = @_;
	my $correct = 0;
	my $total = 0;

	my $explain = $node->safe_psql("postgres", qq(
		SET enable_seqscan = off;
		SET hnsw.ef_search = 100;
		EXPLAIN ANALYZE SELECT i FROM tst ORDER BY v $operator $queries[0] LIMIT $limit;
	));
	like($explain, qr/Index Scan/);

	for my $i (0 .. $#queries)
	{
		my $actual = $node->safe_psql("postgres", qq(
			SET enable_seqscan = off;
			SET hnsw.ef_search = 100;
			SELECT i FROM tst ORDER BY v $operator $queries[$i] LIMIT $limit;
		));
		my @actual_ids = split("\n", $actual);

		my @expected_ids = split("\n", $expected[$i]);
		my %expected_set = map { $_ => 1 } @expected_ids;

		foreach (@actual_ids)
		{
			if (exists($expected_set{$_}))
			{
				$correct++;
			}
		}

		$total += $limit;
	}

	cmp_ok($correct / $total, ">=", $min, $operator);
}

# Initialize node
$node = PostgreSQL::Test::Cluster->new('node');
$node->init;
$node->start;

# Create table
$node->safe_psql("postgres", "CREATE EXTENSION vector;");
$node->safe_psql("postgres", "CREATE TABLE tst (i serial, v bit($dim));");

# Generate queries
for (1 .. 20)
{
	my $r = int(rand() * $max);
	push(@queries, "${r}::bigint::bit($dim)");
}

# Check each index type
my @operators = ("<~>", "<\%>");
my @opclasses = ("bit_hamming_ops", "bit_jaccard_ops");

for my $i (0 .. $#operators)
{
	my $operator = $operators[$i];
	my $opclass = $opclasses[$i];

	# Add index
	$node->safe_psql("postgres", "CREATE INDEX idx ON tst USING hnsw (v $opclass);");

	# Use concurrent inserts
	$node->pgbench(
		"--no-vacuum --client=10 --transactions=1000",
		0,
		[qr{actually processed}],
		[qr{^$}],
		"concurrent INSERTs",
		{
			"023_hnsw_bit_insert_recall_$opclass" => "INSERT INTO tst (v) VALUES ((random() * $max)::bigint::bit($dim));"
		}
	);

	# Get exact results
	@expected = ();
	foreach (@queries)
	{
		# Handle ties
		my $res = $node->safe_psql("postgres", qq(
			SET enable_indexscan = off;
			WITH top AS (
				SELECT v $operator $_ AS distance FROM tst ORDER BY distance LIMIT $limit
			)
			SELECT i FROM tst WHERE (v $operator $_) <= (SELECT MAX(distance) FROM top)
		));
		push(@expected, $res);
	}

	# Test approximate results
	my $min = $operator eq "<\%>" ? 0.95 : 0.98;
	test_recall($min, $operator);

	$node->safe_psql("postgres", "DROP INDEX idx;");
	$node->safe_psql("postgres", "TRUNCATE tst;");
}

done_testing();
```

## File: `test/t/022_hnsw_bit_vacuum_recall.pl`
```
use strict;
use warnings FATAL => 'all';
use PostgreSQL::Test::Cluster;
use PostgreSQL::Test::Utils;
use Test::More;

my $node;
my @queries = ();
my @expected;
my $limit = 20;
my $dim = 52;
my $max = 2**$dim;

sub test_recall
{
	my ($min, $ef_search, $test_name) = @_;
	my $correct = 0;
	my $total = 0;

	my $explain = $node->safe_psql("postgres", qq(
		SET enable_seqscan = off;
		SET hnsw.ef_search = $ef_search;
		EXPLAIN ANALYZE SELECT i FROM tst ORDER BY v <~> $queries[0] LIMIT $limit;
	));
	like($explain, qr/Index Scan/);

	for my $i (0 .. $#queries)
	{
		my $actual = $node->safe_psql("postgres", qq(
			SET enable_seqscan = off;
			SET hnsw.ef_search = $ef_search;
			SELECT i FROM tst ORDER BY v <~> $queries[$i] LIMIT $limit;
		));
		my @actual_ids = split("\n", $actual);

		my @expected_ids = split("\n", $expected[$i]);
		my %expected_set = map { $_ => 1 } @expected_ids;

		foreach (@actual_ids)
		{
			if (exists($expected_set{$_}))
			{
				$correct++;
			}
		}

		$total += $limit;
	}

	cmp_ok($correct / $total, ">=", $min, $test_name);
}

# Initialize node
$node = PostgreSQL::Test::Cluster->new('node');
$node->init;
$node->start;

# Create table
$node->safe_psql("postgres", "CREATE EXTENSION vector;");
$node->safe_psql("postgres", "CREATE TABLE tst (i int4, v bit($dim));");
$node->safe_psql("postgres", "ALTER TABLE tst SET (autovacuum_enabled = false);");
$node->safe_psql("postgres",
	"INSERT INTO tst SELECT i, (random() * $max)::bigint::bit($dim) FROM generate_series(1, 10000) i;"
);

# Add index
$node->safe_psql("postgres", "CREATE INDEX ON tst USING hnsw (v bit_hamming_ops) WITH (m = 4, ef_construction = 8);");

# Delete data
$node->safe_psql("postgres", "DELETE FROM tst WHERE i > 2500;");

# Generate queries
for (1 .. 20)
{
	my $r = int(rand() * $max);
	push(@queries, "${r}::bigint::bit($dim)");
}

# Get exact results
@expected = ();
foreach (@queries)
{
	my $res = $node->safe_psql("postgres", qq(
		SET enable_indexscan = off;
		WITH top AS (
			SELECT v <~> $_ AS distance FROM tst ORDER BY distance LIMIT $limit
		)
		SELECT i FROM tst WHERE (v <~> $_) <= (SELECT MAX(distance) FROM top)
	));
	push(@expected, $res);
}

test_recall(0.35, 100, "before vacuum");

# TODO Test concurrent inserts with vacuum
$node->safe_psql("postgres", "VACUUM tst;");

test_recall(0.80, 100, "after vacuum");

done_testing();
```

## File: `test/t/023_hnsw_bit_duplicates.pl`
```
use strict;
use warnings FATAL => 'all';
use PostgreSQL::Test::Cluster;
use PostgreSQL::Test::Utils;
use Test::More;

# Initialize node
my $node = PostgreSQL::Test::Cluster->new('node');
$node->init;
$node->start;

# Create table
$node->safe_psql("postgres", "CREATE EXTENSION vector;");
$node->safe_psql("postgres", "CREATE TABLE tst (v bit(3));");

sub insert_vectors
{
	for my $i (1 .. 20)
	{
		$node->safe_psql("postgres", "INSERT INTO tst VALUES ('111');");
	}
}

sub test_duplicates
{
	my $res = $node->safe_psql("postgres", qq(
		SET enable_seqscan = off;
		SET hnsw.ef_search = 1;
		SELECT COUNT(*) FROM (SELECT * FROM tst ORDER BY v <~> '111') t;
	));
	is($res, 10);
}

# Test duplicates with build
insert_vectors();
$node->safe_psql("postgres", "CREATE INDEX idx ON tst USING hnsw (v bit_hamming_ops);");
test_duplicates();

# Reset
$node->safe_psql("postgres", "TRUNCATE tst;");

# Test duplicates with inserts
insert_vectors();
test_duplicates();

# Test fallback path for inserts
$node->pgbench(
	"--no-vacuum --client=5 --transactions=100",
	0,
	[qr{actually processed}],
	[qr{^$}],
	"concurrent INSERTs",
	{
		"026_hnsw_bit_duplicates" => "INSERT INTO tst VALUES ('111');"
	}
);

done_testing();
```

## File: `test/t/024_hnsw_halfvec_build_recall.pl`
```
use strict;
use warnings FATAL => 'all';
use PostgreSQL::Test::Cluster;
use PostgreSQL::Test::Utils;
use Test::More;

my $node;
my @queries = ();
my @expected;
my $limit = 20;
my $dim = 10;
my $array_sql = join(",", ('2 * random() * random()') x $dim);

sub test_recall
{
	my ($min, $operator) = @_;
	my $correct = 0;
	my $total = 0;

	my $explain = $node->safe_psql("postgres", qq(
		SET enable_seqscan = off;
		EXPLAIN ANALYZE SELECT i FROM tst ORDER BY v $operator '$queries[0]' LIMIT $limit;
	));
	like($explain, qr/Index Scan/);

	for my $i (0 .. $#queries)
	{
		my $actual = $node->safe_psql("postgres", qq(
			SET enable_seqscan = off;
			SELECT i FROM tst ORDER BY v $operator '$queries[$i]' LIMIT $limit;
		));
		my @actual_ids = split("\n", $actual);
		my %actual_set = map { $_ => 1 } @actual_ids;

		my @expected_ids = split("\n", $expected[$i]);

		foreach (@expected_ids)
		{
			if (exists($actual_set{$_}))
			{
				$correct++;
			}
			$total++;
		}
	}

	cmp_ok($correct / $total, ">=", $min, $operator);
}

# Initialize node
$node = PostgreSQL::Test::Cluster->new('node');
$node->init;
$node->start;

# Create table
$node->safe_psql("postgres", "CREATE EXTENSION vector;");
$node->safe_psql("postgres", "CREATE TABLE tst (i int4, v halfvec($dim));");
$node->safe_psql("postgres",
	"INSERT INTO tst SELECT i, ARRAY[$array_sql] FROM generate_series(1, 10000) i;"
);

# Generate queries
for (1 .. 20)
{
	my @r = ();
	for (1 .. $dim)
	{
		push(@r, rand());
	}
	push(@queries, "[" . join(",", @r) . "]");
}

# Check each index type
my @operators = ("<->", "<#>", "<=>", "<+>");
my @opclasses = ("halfvec_l2_ops", "halfvec_ip_ops", "halfvec_cosine_ops", "halfvec_l1_ops");

for my $i (0 .. $#operators)
{
	my $operator = $operators[$i];
	my $opclass = $opclasses[$i];

	# Get exact results
	@expected = ();
	foreach (@queries)
	{
		my $res = $node->safe_psql("postgres", "SELECT i FROM tst ORDER BY v $operator '$_' LIMIT $limit;");
		push(@expected, $res);
	}

	# Build index serially
	$node->safe_psql("postgres", qq(
		SET max_parallel_maintenance_workers = 0;
		CREATE INDEX idx ON tst USING hnsw (v $opclass);
	));

	# Test approximate results
	my $min = 0.98;
	test_recall($min, $operator);

	$node->safe_psql("postgres", "DROP INDEX idx;");

	# Build index in parallel in memory
	my ($ret, $stdout, $stderr) = $node->psql("postgres", qq(
		SET client_min_messages = DEBUG;
		SET min_parallel_table_scan_size = 1;
		CREATE INDEX idx ON tst USING hnsw (v $opclass);
	));
	is($ret, 0, $stderr);
	like($stderr, qr/using \d+ parallel workers/);

	# Test approximate results
	test_recall($min, $operator);

	$node->safe_psql("postgres", "DROP INDEX idx;");

	# Build index in parallel on disk
	# Set parallel_workers on table to use workers with low maintenance_work_mem
	($ret, $stdout, $stderr) = $node->psql("postgres", qq(
		ALTER TABLE tst SET (parallel_workers = 2);
		SET client_min_messages = DEBUG;
		SET maintenance_work_mem = '4MB';
		CREATE INDEX idx ON tst USING hnsw (v $opclass);
		ALTER TABLE tst RESET (parallel_workers);
	));
	is($ret, 0, $stderr);
	like($stderr, qr/using \d+ parallel workers/);
	like($stderr, qr/hnsw graph no longer fits into maintenance_work_mem/);

	$node->safe_psql("postgres", "DROP INDEX idx;");
}

done_testing();
```

## File: `test/t/025_hnsw_halfvec_insert_recall.pl`
```
use strict;
use warnings FATAL => 'all';
use PostgreSQL::Test::Cluster;
use PostgreSQL::Test::Utils;
use Test::More;

my $node;
my @queries = ();
my @expected;
my $limit = 20;
my $dim = 10;
my $array_sql = join(",", ('2 * random() * random()') x $dim);

sub test_recall
{
	my ($min, $operator) = @_;
	my $correct = 0;
	my $total = 0;

	my $explain = $node->safe_psql("postgres", qq(
		SET enable_seqscan = off;
		EXPLAIN ANALYZE SELECT i FROM tst ORDER BY v $operator '$queries[0]' LIMIT $limit;
	));
	like($explain, qr/Index Scan/);

	for my $i (0 .. $#queries)
	{
		my $actual = $node->safe_psql("postgres", qq(
			SET enable_seqscan = off;
			SELECT i FROM tst ORDER BY v $operator '$queries[$i]' LIMIT $limit;
		));
		my @actual_ids = split("\n", $actual);
		my %actual_set = map { $_ => 1 } @actual_ids;

		my @expected_ids = split("\n", $expected[$i]);

		foreach (@expected_ids)
		{
			if (exists($actual_set{$_}))
			{
				$correct++;
			}
			$total++;
		}
	}

	cmp_ok($correct / $total, ">=", $min, $operator);
}

# Initialize node
$node = PostgreSQL::Test::Cluster->new('node');
$node->init;
$node->start;

# Create table
$node->safe_psql("postgres", "CREATE EXTENSION vector;");
$node->safe_psql("postgres", "CREATE TABLE tst (i serial, v halfvec($dim));");

# Generate queries
for (1 .. 20)
{
	my @r = ();
	for (1 .. $dim)
	{
		push(@r, rand());
	}
	push(@queries, "[" . join(",", @r) . "]");
}

# Check each index type
my @operators = ("<->", "<#>", "<=>", "<+>");
my @opclasses = ("halfvec_l2_ops", "halfvec_ip_ops", "halfvec_cosine_ops", "halfvec_l1_ops");

for my $i (0 .. $#operators)
{
	my $operator = $operators[$i];
	my $opclass = $opclasses[$i];

	# Add index
	$node->safe_psql("postgres", "CREATE INDEX idx ON tst USING hnsw (v $opclass);");

	# Use concurrent inserts
	$node->pgbench(
		"--no-vacuum --client=10 --transactions=1000",
		0,
		[qr{actually processed}],
		[qr{^$}],
		"concurrent INSERTs",
		{
			"024_hnsw_halfvec_insert_recall_$opclass" => "INSERT INTO tst (v) VALUES (ARRAY[$array_sql]);"
		}
	);

	# Get exact results
	@expected = ();
	foreach (@queries)
	{
		my $res = $node->safe_psql("postgres", qq(
			SET enable_indexscan = off;
			SELECT i FROM tst ORDER BY v $operator '$_' LIMIT $limit;
		));
		push(@expected, $res);
	}

	# Test approximate results
	my $min = 0.98;
	test_recall($min, $operator);

	$node->safe_psql("postgres", "DROP INDEX idx;");
	$node->safe_psql("postgres", "TRUNCATE tst;");
}

done_testing();
```

## File: `test/t/026_hnsw_halfvec_vacuum_recall.pl`
```
use strict;
use warnings FATAL => 'all';
use PostgreSQL::Test::Cluster;
use PostgreSQL::Test::Utils;
use Test::More;

my $node;
my @queries = ();
my @expected;
my $limit = 20;

sub test_recall
{
	my ($min, $ef_search, $test_name) = @_;
	my $correct = 0;
	my $total = 0;

	my $explain = $node->safe_psql("postgres", qq(
		SET enable_seqscan = off;
		SET hnsw.ef_search = $ef_search;
		EXPLAIN ANALYZE SELECT i FROM tst ORDER BY v <-> '$queries[0]' LIMIT $limit;
	));
	like($explain, qr/Index Scan/);

	for my $i (0 .. $#queries)
	{
		my $actual = $node->safe_psql("postgres", qq(
			SET enable_seqscan = off;
			SET hnsw.ef_search = $ef_search;
			SELECT i FROM tst ORDER BY v <-> '$queries[$i]' LIMIT $limit;
		));
		my @actual_ids = split("\n", $actual);
		my %actual_set = map { $_ => 1 } @actual_ids;

		my @expected_ids = split("\n", $expected[$i]);

		foreach (@expected_ids)
		{
			if (exists($actual_set{$_}))
			{
				$correct++;
			}
			$total++;
		}
	}

	cmp_ok($correct / $total, ">=", $min, $test_name);
}

# Initialize node
$node = PostgreSQL::Test::Cluster->new('node');
$node->init;
$node->start;

# Create table
$node->safe_psql("postgres", "CREATE EXTENSION vector;");
$node->safe_psql("postgres", "CREATE TABLE tst (i int4, v halfvec(3));");
$node->safe_psql("postgres", "ALTER TABLE tst SET (autovacuum_enabled = false);");
$node->safe_psql("postgres",
	"INSERT INTO tst SELECT i, ARRAY[random(), random(), random()] FROM generate_series(1, 10000) i;"
);

# Add index
$node->safe_psql("postgres", "CREATE INDEX ON tst USING hnsw (v halfvec_l2_ops) WITH (m = 4, ef_construction = 8);");

# Delete data
$node->safe_psql("postgres", "DELETE FROM tst WHERE i > 2500;");

# Generate queries
for (1 .. 20)
{
	my $r1 = rand();
	my $r2 = rand();
	my $r3 = rand();
	push(@queries, "[$r1,$r2,$r3]");
}

# Get exact results
@expected = ();
foreach (@queries)
{
	my $res = $node->safe_psql("postgres", qq(
		SET enable_indexscan = off;
		SELECT i FROM tst ORDER BY v <-> '$_' LIMIT $limit;
	));
	push(@expected, $res);
}

test_recall(0.18, $limit, "before vacuum");
test_recall(0.93, 100, "before vacuum");

# TODO Test concurrent inserts with vacuum
$node->safe_psql("postgres", "VACUUM tst;");

test_recall(0.95, $limit, "after vacuum");

done_testing();
```

## File: `test/t/027_hnsw_halfvec_duplicates.pl`
```
use strict;
use warnings FATAL => 'all';
use PostgreSQL::Test::Cluster;
use PostgreSQL::Test::Utils;
use Test::More;

# Initialize node
my $node = PostgreSQL::Test::Cluster->new('node');
$node->init;
$node->start;

# Create table
$node->safe_psql("postgres", "CREATE EXTENSION vector;");
$node->safe_psql("postgres", "CREATE TABLE tst (v halfvec(3));");

sub insert_vectors
{
	for my $i (1 .. 20)
	{
		$node->safe_psql("postgres", "INSERT INTO tst VALUES ('[1,1,1]');");
	}
}

sub test_duplicates
{
	my $res = $node->safe_psql("postgres", qq(
		SET enable_seqscan = off;
		SET hnsw.ef_search = 1;
		SELECT COUNT(*) FROM (SELECT * FROM tst ORDER BY v <-> '[1,1,1]') t;
	));
	is($res, 10);
}

# Test duplicates with build
insert_vectors();
$node->safe_psql("postgres", "CREATE INDEX idx ON tst USING hnsw (v halfvec_l2_ops);");
test_duplicates();

# Reset
$node->safe_psql("postgres", "TRUNCATE tst;");

# Test duplicates with inserts
insert_vectors();
test_duplicates();

# Test fallback path for inserts
$node->pgbench(
	"--no-vacuum --client=5 --transactions=100",
	0,
	[qr{actually processed}],
	[qr{^$}],
	"concurrent INSERTs",
	{
		"027_hnsw_halfvec_duplicates" => "INSERT INTO tst VALUES ('[1,1,1]');"
	}
);

done_testing();
```

## File: `test/t/028_hnsw_sparsevec_build_recall.pl`
```
use strict;
use warnings FATAL => 'all';
use PostgreSQL::Test::Cluster;
use PostgreSQL::Test::Utils;
use Test::More;

my $node;
my @queries = ();
my @expected;
my $limit = 20;
my $array_sql = join(",", ('random() * random()') x 3);

sub test_recall
{
	my ($min, $operator) = @_;
	my $correct = 0;
	my $total = 0;

	my $explain = $node->safe_psql("postgres", qq(
		SET enable_seqscan = off;
		EXPLAIN ANALYZE SELECT i FROM tst ORDER BY v $operator '$queries[0]' LIMIT $limit;
	));
	like($explain, qr/Index Scan/);

	for my $i (0 .. $#queries)
	{
		my $actual = $node->safe_psql("postgres", qq(
			SET enable_seqscan = off;
			SELECT i FROM tst ORDER BY v $operator '$queries[$i]' LIMIT $limit;
		));
		my @actual_ids = split("\n", $actual);
		my %actual_set = map { $_ => 1 } @actual_ids;

		my @expected_ids = split("\n", $expected[$i]);

		foreach (@expected_ids)
		{
			if (exists($actual_set{$_}))
			{
				$correct++;
			}
			$total++;
		}
	}

	cmp_ok($correct / $total, ">=", $min, $operator);
}

# Initialize node
$node = PostgreSQL::Test::Cluster->new('node');
$node->init;
$node->start;

# Create table
$node->safe_psql("postgres", "CREATE EXTENSION vector;");
$node->safe_psql("postgres", "CREATE TABLE tst (i int4, v sparsevec(3));");
$node->safe_psql("postgres",
	"INSERT INTO tst SELECT i, ARRAY[$array_sql]::vector::sparsevec FROM generate_series(1, 10000) i;"
);

# Generate queries
for (1 .. 20)
{
	my $r1 = rand();
	my $r2 = rand();
	my $r3 = rand();
	push(@queries, "{1:$r1,2:$r2,3:$r3}/3");
}

# Check each index type
my @operators = ("<->", "<#>", "<=>", "<+>");
my @opclasses = ("sparsevec_l2_ops", "sparsevec_ip_ops", "sparsevec_cosine_ops", "sparsevec_l1_ops");

for my $i (0 .. $#operators)
{
	my $operator = $operators[$i];
	my $opclass = $opclasses[$i];

	# Get exact results
	@expected = ();
	foreach (@queries)
	{
		my $res = $node->safe_psql("postgres", "SELECT i FROM tst ORDER BY v $operator '$_' LIMIT $limit;");
		push(@expected, $res);
	}

	# Build index serially
	$node->safe_psql("postgres", qq(
		SET max_parallel_maintenance_workers = 0;
		CREATE INDEX idx ON tst USING hnsw (v $opclass);
	));

	# Test approximate results
	my $min = $operator eq "<#>" ? 0.97 : 0.99;
	test_recall($min, $operator);

	$node->safe_psql("postgres", "DROP INDEX idx;");

	# Build index in parallel in memory
	my ($ret, $stdout, $stderr) = $node->psql("postgres", qq(
		SET client_min_messages = DEBUG;
		SET min_parallel_table_scan_size = 1;
		CREATE INDEX idx ON tst USING hnsw (v $opclass);
	));
	is($ret, 0, $stderr);
	like($stderr, qr/using \d+ parallel workers/);

	# Test approximate results
	test_recall($min, $operator);

	$node->safe_psql("postgres", "DROP INDEX idx;");

	# Build index in parallel on disk
	# Set parallel_workers on table to use workers with low maintenance_work_mem
	($ret, $stdout, $stderr) = $node->psql("postgres", qq(
		ALTER TABLE tst SET (parallel_workers = 2);
		SET client_min_messages = DEBUG;
		SET maintenance_work_mem = '4MB';
		CREATE INDEX idx ON tst USING hnsw (v $opclass);
		ALTER TABLE tst RESET (parallel_workers);
	));
	is($ret, 0, $stderr);
	like($stderr, qr/using \d+ parallel workers/);
	like($stderr, qr/hnsw graph no longer fits into maintenance_work_mem/);

	$node->safe_psql("postgres", "DROP INDEX idx;");
}

done_testing();
```

## File: `test/t/029_hnsw_sparsevec_insert_recall.pl`
```
use strict;
use warnings FATAL => 'all';
use PostgreSQL::Test::Cluster;
use PostgreSQL::Test::Utils;
use Test::More;

my $node;
my @queries = ();
my @expected;
my $limit = 20;
my $array_sql = join(",", ('random() * random()') x 3);

sub test_recall
{
	my ($min, $operator) = @_;
	my $correct = 0;
	my $total = 0;

	my $explain = $node->safe_psql("postgres", qq(
		SET enable_seqscan = off;
		EXPLAIN ANALYZE SELECT i FROM tst ORDER BY v $operator '$queries[0]' LIMIT $limit;
	));
	like($explain, qr/Index Scan/);

	for my $i (0 .. $#queries)
	{
		my $actual = $node->safe_psql("postgres", qq(
			SET enable_seqscan = off;
			SELECT i FROM tst ORDER BY v $operator '$queries[$i]' LIMIT $limit;
		));
		my @actual_ids = split("\n", $actual);
		my %actual_set = map { $_ => 1 } @actual_ids;

		my @expected_ids = split("\n", $expected[$i]);

		foreach (@expected_ids)
		{
			if (exists($actual_set{$_}))
			{
				$correct++;
			}
			$total++;
		}
	}

	cmp_ok($correct / $total, ">=", $min, $operator);
}

# Initialize node
$node = PostgreSQL::Test::Cluster->new('node');
$node->init;
$node->start;

# Create table
$node->safe_psql("postgres", "CREATE EXTENSION vector;");
$node->safe_psql("postgres", "CREATE TABLE tst (i serial, v sparsevec(3));");

# Generate queries
for (1 .. 20)
{
	my $r1 = rand();
	my $r2 = rand();
	my $r3 = rand();
	push(@queries, "{1:$r1,2:$r2,3:$r3}/3");
}

# Check each index type
my @operators = ("<->", "<#>", "<=>", "<+>");
my @opclasses = ("sparsevec_l2_ops", "sparsevec_ip_ops", "sparsevec_cosine_ops", "sparsevec_l1_ops");

for my $i (0 .. $#operators)
{
	my $operator = $operators[$i];
	my $opclass = $opclasses[$i];

	# Add index
	$node->safe_psql("postgres", "CREATE INDEX idx ON tst USING hnsw (v $opclass);");

	# Use concurrent inserts
	$node->pgbench(
		"--no-vacuum --client=10 --transactions=1000",
		0,
		[qr{actually processed}],
		[qr{^$}],
		"concurrent INSERTs",
		{
			"025_hnsw_sparsevec_insert_recall_$opclass" => "INSERT INTO tst (v) VALUES (ARRAY[$array_sql]::vector::sparsevec);"
		}
	);

	# Get exact results
	@expected = ();
	foreach (@queries)
	{
		my $res = $node->safe_psql("postgres", qq(
			SET enable_indexscan = off;
			SELECT i FROM tst ORDER BY v $operator '$_' LIMIT $limit;
		));
		push(@expected, $res);
	}

	# Test approximate results
	my $min = $operator eq "<#>" ? 0.97 : 0.99;
	test_recall($min, $operator);

	$node->safe_psql("postgres", "DROP INDEX idx;");
	$node->safe_psql("postgres", "TRUNCATE tst;");
}

done_testing();
```

## File: `test/t/030_hnsw_sparsevec_vacuum_recall.pl`
```
use strict;
use warnings FATAL => 'all';
use PostgreSQL::Test::Cluster;
use PostgreSQL::Test::Utils;
use Test::More;

my $node;
my @queries = ();
my @expected;
my $limit = 20;

sub test_recall
{
	my ($min, $ef_search, $test_name) = @_;
	my $correct = 0;
	my $total = 0;

	my $explain = $node->safe_psql("postgres", qq(
		SET enable_seqscan = off;
		SET hnsw.ef_search = $ef_search;
		EXPLAIN ANALYZE SELECT i FROM tst ORDER BY v <-> '$queries[0]' LIMIT $limit;
	));
	like($explain, qr/Index Scan/);

	for my $i (0 .. $#queries)
	{
		my $actual = $node->safe_psql("postgres", qq(
			SET enable_seqscan = off;
			SET hnsw.ef_search = $ef_search;
			SELECT i FROM tst ORDER BY v <-> '$queries[$i]' LIMIT $limit;
		));
		my @actual_ids = split("\n", $actual);
		my %actual_set = map { $_ => 1 } @actual_ids;

		my @expected_ids = split("\n", $expected[$i]);

		foreach (@expected_ids)
		{
			if (exists($actual_set{$_}))
			{
				$correct++;
			}
			$total++;
		}
	}

	cmp_ok($correct / $total, ">=", $min, $test_name);
}

# Initialize node
$node = PostgreSQL::Test::Cluster->new('node');
$node->init;
$node->start;

# Create table
$node->safe_psql("postgres", "CREATE EXTENSION vector;");
$node->safe_psql("postgres", "CREATE TABLE tst (i int4, v sparsevec(3));");
$node->safe_psql("postgres", "ALTER TABLE tst SET (autovacuum_enabled = false);");
$node->safe_psql("postgres",
	"INSERT INTO tst SELECT i, ARRAY[random(), random(), random()]::vector::sparsevec(3) FROM generate_series(1, 10000) i;"
);

# Add index
$node->safe_psql("postgres", "CREATE INDEX ON tst USING hnsw (v sparsevec_l2_ops) WITH (m = 4, ef_construction = 8);");

# Delete data
$node->safe_psql("postgres", "DELETE FROM tst WHERE i > 2500;");

# Generate queries
for (1 .. 20)
{
	my $r1 = rand();
	my $r2 = rand();
	my $r3 = rand();
	push(@queries, "{1:$r1,2:$r2,3:$r3}/3");
}

# Get exact results
@expected = ();
foreach (@queries)
{
	my $res = $node->safe_psql("postgres", qq(
		SET enable_indexscan = off;
		SELECT i FROM tst ORDER BY v <-> '$_' LIMIT $limit;
	));
	push(@expected, $res);
}

test_recall(0.18, $limit, "before vacuum");
test_recall(0.93, 100, "before vacuum");

# TODO Test concurrent inserts with vacuum
$node->safe_psql("postgres", "VACUUM tst;");

test_recall(0.95, $limit, "after vacuum");

done_testing();
```

## File: `test/t/031_hnsw_sparsevec_duplicates.pl`
```
use strict;
use warnings FATAL => 'all';
use PostgreSQL::Test::Cluster;
use PostgreSQL::Test::Utils;
use Test::More;

# Initialize node
my $node = PostgreSQL::Test::Cluster->new('node');
$node->init;
$node->start;

# Create table
$node->safe_psql("postgres", "CREATE EXTENSION vector;");
$node->safe_psql("postgres", "CREATE TABLE tst (v sparsevec(3));");

sub insert_vectors
{
	for my $i (1 .. 20)
	{
		$node->safe_psql("postgres", "INSERT INTO tst VALUES ('{1:1,2:1,3:1}/3');");
	}
}

sub test_duplicates
{
	my $res = $node->safe_psql("postgres", qq(
		SET enable_seqscan = off;
		SET hnsw.ef_search = 1;
		SELECT COUNT(*) FROM (SELECT * FROM tst ORDER BY v <-> '{1:1,2:1,3:1}/3') t;
	));
	is($res, 10);
}

# Test duplicates with build
insert_vectors();
$node->safe_psql("postgres", "CREATE INDEX idx ON tst USING hnsw (v sparsevec_l2_ops);");
test_duplicates();

# Reset
$node->safe_psql("postgres", "TRUNCATE tst;");

# Test duplicates with inserts
insert_vectors();
test_duplicates();

# Test fallback path for inserts
$node->pgbench(
	"--no-vacuum --client=5 --transactions=100",
	0,
	[qr{actually processed}],
	[qr{^$}],
	"concurrent INSERTs",
	{
		"028_hnsw_sparsevec_duplicates" => "INSERT INTO tst VALUES ('{1:1,2:1,3:1}/3');"
	}
);

done_testing();
```

## File: `test/t/032_ivfflat_halfvec_build_recall.pl`
```
use strict;
use warnings FATAL => 'all';
use PostgreSQL::Test::Cluster;
use PostgreSQL::Test::Utils;
use Test::More;

my $node;
my @queries = ();
my @expected;
my $limit = 20;
my $dim = 10;
my $array_sql = join(",", ('random()') x $dim);

sub test_recall
{
	my ($probes, $min, $operator) = @_;
	my $correct = 0;
	my $total = 0;

	my $explain = $node->safe_psql("postgres", qq(
		SET enable_seqscan = off;
		SET ivfflat.probes = $probes;
		EXPLAIN ANALYZE SELECT i FROM tst ORDER BY v $operator '$queries[0]' LIMIT $limit;
	));
	like($explain, qr/Index Scan using idx on tst/);

	for my $i (0 .. $#queries)
	{
		my $actual = $node->safe_psql("postgres", qq(
			SET enable_seqscan = off;
			SET ivfflat.probes = $probes;
			SELECT i FROM tst ORDER BY v $operator '$queries[$i]' LIMIT $limit;
		));
		my @actual_ids = split("\n", $actual);

		my @expected_ids = split("\n", $expected[$i]);
		my %expected_set = map { $_ => 1 } @expected_ids;

		foreach (@actual_ids)
		{
			if (exists($expected_set{$_}))
			{
				$correct++;
			}
		}

		$total += $limit;
	}

	cmp_ok($correct / $total, ">=", $min, $operator);
}

# Initialize node
$node = PostgreSQL::Test::Cluster->new('node');
$node->init;
$node->start;

# Create table
$node->safe_psql("postgres", "CREATE EXTENSION vector;");
$node->safe_psql("postgres", "CREATE TABLE tst (i int4, v halfvec($dim));");
$node->safe_psql("postgres",
	"INSERT INTO tst SELECT i, ARRAY[$array_sql] FROM generate_series(1, 100000) i;"
);

# Generate queries
for (1 .. 20)
{
	my @r = ();
	for (1 .. $dim)
	{
		push(@r, rand());
	}
	push(@queries, "[" . join(",", @r) . "]");
}

# Check each index type
my @operators = ("<->", "<#>", "<=>");
my @opclasses = ("halfvec_l2_ops", "halfvec_ip_ops", "halfvec_cosine_ops");

for my $i (0 .. $#operators)
{
	my $operator = $operators[$i];
	my $opclass = $opclasses[$i];

	# Get exact results
	@expected = ();
	foreach (@queries)
	{
		my $res = $node->safe_psql("postgres", qq(
			WITH top AS (
				SELECT v $operator '$_' AS distance FROM tst ORDER BY distance LIMIT $limit
			)
			SELECT i FROM tst WHERE (v $operator '$_') <= (SELECT MAX(distance) FROM top)
		));
		push(@expected, $res);
	}

	# Build index serially
	$node->safe_psql("postgres", qq(
		SET max_parallel_maintenance_workers = 0;
		CREATE INDEX idx ON tst USING ivfflat (v $opclass);
	));

	# Test approximate results
	if ($operator ne "<#>")
	{
		# TODO Fix test (uniform random vectors all have similar inner product)
		test_recall(1, 0.33, $operator);
		test_recall(10, 0.93, $operator);
	}

	# Test probes equals lists
	if ($operator eq "<=>")
	{
		test_recall(100, 0.98, $operator);
	}
	else
	{
		test_recall(100, 1.00, $operator);
	}

	$node->safe_psql("postgres", "DROP INDEX idx;");

	# Build index in parallel
	my ($ret, $stdout, $stderr) = $node->psql("postgres", qq(
		SET client_min_messages = DEBUG;
		SET min_parallel_table_scan_size = 1;
		CREATE INDEX idx ON tst USING ivfflat (v $opclass);
	));
	is($ret, 0, $stderr);
	like($stderr, qr/using \d+ parallel workers/);

	# Test approximate results
	if ($operator ne "<#>")
	{
		# TODO Fix test (uniform random vectors all have similar inner product)
		test_recall(1, 0.33, $operator);
		test_recall(10, 0.93, $operator);
	}

	# Test probes equals lists
	if ($operator eq "<=>")
	{
		test_recall(100, 0.98, $operator);
	}
	else
	{
		test_recall(100, 1.00, $operator);
	}

	$node->safe_psql("postgres", "DROP INDEX idx;");
}

done_testing();
```

## File: `test/t/033_comparison.pl`
```
use strict;
use warnings FATAL => 'all';
use PostgreSQL::Test::Cluster;
use PostgreSQL::Test::Utils;
use Test::More;

my $node;
my $array_sql = join(",", ('floor(random() * 2)::int - 1') x 3);

# Initialize node
$node = PostgreSQL::Test::Cluster->new('node');
$node->init;
$node->start;

# Create table
$node->safe_psql("postgres", "CREATE EXTENSION vector;");
$node->safe_psql("postgres", "CREATE TABLE tst (v real[]);");
$node->safe_psql("postgres",
	"INSERT INTO tst SELECT ARRAY[$array_sql] FROM generate_series(1, 10000) i;"
);

for (1 .. 50)
{
	# Generate query
	my @r = ();
	for (1 .. (int(rand() * 3) + 2))
	{
		push(@r, int(rand() * 2) - 1);
	}
	my $query = "{" . join(",", @r) . "}";

	# Get expected result
	my $expected = $node->safe_psql("postgres", "SELECT btarraycmp(v, '$query') FROM tst");

	# Test vector
	my $actual = $node->safe_psql("postgres", "SELECT vector_cmp(v::vector, '$query'::real[]::vector) FROM tst");
	is($expected, $actual);

	# Test halfvec
	$actual = $node->safe_psql("postgres", "SELECT halfvec_cmp(v::halfvec, '$query'::real[]::halfvec) FROM tst");
	is($expected, $actual);

	# Test sparsevec
	$actual = $node->safe_psql("postgres", "SELECT sparsevec_cmp(v::vector::sparsevec, '$query'::real[]::vector::sparsevec) FROM tst");
	is($expected, $actual);
}

done_testing();
```

## File: `test/t/034_distance_functions.pl`
```
use strict;
use warnings FATAL => 'all';
use PostgreSQL::Test::Cluster;
use PostgreSQL::Test::Utils;
use Test::More;

my $node;
my @queries = ();
my $dim = 5;
my $array_sql = join(",", ('floor(random() * 4)::int - 2') x $dim);

# Initialize node
$node = PostgreSQL::Test::Cluster->new('node');
$node->init;
$node->start;

# Create table
$node->safe_psql("postgres", "CREATE EXTENSION vector;");
$node->safe_psql("postgres", "CREATE TABLE tst (v vector($dim));");
$node->safe_psql("postgres",
	"INSERT INTO tst SELECT ARRAY[$array_sql] FROM generate_series(1, 10000) i;"
);

# Generate queries
for (1 .. 20)
{
	my @r = ();
	for (1 .. $dim)
	{
		push(@r, int(rand() * 4) - 2);
	}
	push(@queries, "[" . join(",", @r) . "]");
}

# Check each distance function
my @functions = ("l2_distance", "inner_product", "cosine_distance", "l1_distance");

for my $function (@functions)
{
	for my $query (@queries)
	{
		my $expected = $node->safe_psql("postgres", "SELECT $function(v, '$query') FROM tst");

		# Test halfvec
		my $actual = $node->safe_psql("postgres", "SELECT $function(v::halfvec, '$query'::vector::halfvec) FROM tst");
		is($expected, $actual, "halfvec $function");

		# Test sparsevec
		$actual = $node->safe_psql("postgres", "SELECT $function(v::sparsevec, '$query'::vector::sparsevec) FROM tst");
		is($expected, $actual, "sparsevec $function");
	}
}

done_testing();
```

## File: `test/t/035_ivfflat_bit_build_recall.pl`
```
use strict;
use warnings FATAL => 'all';
use PostgreSQL::Test::Cluster;
use PostgreSQL::Test::Utils;
use Test::More;

my $node;
my @queries = ();
my @expected;
my $limit = 20;
my $dim = 52;
my $max = 2**$dim;

sub test_recall
{
	my ($probes, $min, $operator) = @_;
	my $correct = 0;
	my $total = 0;

	my $explain = $node->safe_psql("postgres", qq(
		SET enable_seqscan = off;
		SET ivfflat.probes = $probes;
		EXPLAIN ANALYZE SELECT i FROM tst ORDER BY v $operator $queries[0] LIMIT $limit;
	));
	like($explain, qr/Index Scan using idx on tst/);

	for my $i (0 .. $#queries)
	{
		my $actual = $node->safe_psql("postgres", qq(
			SET enable_seqscan = off;
			SET ivfflat.probes = $probes;
			SELECT i FROM tst ORDER BY v $operator $queries[$i] LIMIT $limit;
		));
		my @actual_ids = split("\n", $actual);

		my @expected_ids = split("\n", $expected[$i]);
		my %expected_set = map { $_ => 1 } @expected_ids;

		foreach (@actual_ids)
		{
			if (exists($expected_set{$_}))
			{
				$correct++;
			}
		}

		$total += $limit;
	}

	cmp_ok($correct / $total, ">=", $min, $operator);
}

# Initialize node
$node = PostgreSQL::Test::Cluster->new('node');
$node->init;
$node->start;

# Create table
$node->safe_psql("postgres", "CREATE EXTENSION vector;");
$node->safe_psql("postgres", "CREATE TABLE tst (i int4, v bit($dim));");
$node->safe_psql("postgres",
	"INSERT INTO tst SELECT i, (random() * $max)::bigint::bit($dim) FROM generate_series(1, 100000) i;"
);

# Generate queries
for (1 .. 20)
{
	my $r = int(rand() * $max);
	push(@queries, "${r}::bigint::bit($dim)");
}

# Check each index type
my @operators = ("<~>");
my @opclasses = ("bit_hamming_ops");

for my $i (0 .. $#operators)
{
	my $operator = $operators[$i];
	my $opclass = $opclasses[$i];

	# Get exact results
	@expected = ();
	foreach (@queries)
	{
		my $res = $node->safe_psql("postgres", qq(
			WITH top AS (
				SELECT v $operator $_ AS distance FROM tst ORDER BY distance LIMIT $limit
			)
			SELECT i FROM tst WHERE (v $operator $_) <= (SELECT MAX(distance) FROM top)
		));
		push(@expected, $res);
	}

	# Build index serially
	$node->safe_psql("postgres", qq(
		SET max_parallel_maintenance_workers = 0;
		CREATE INDEX idx ON tst USING ivfflat (v $opclass);
	));

	# Test approximate results
	test_recall(1, 0.08, $operator);
	test_recall(10, 0.50, $operator);

	# Test probes equals lists
	test_recall(100, 1.00, $operator);

	$node->safe_psql("postgres", "DROP INDEX idx;");

	# Build index in parallel
	my ($ret, $stdout, $stderr) = $node->psql("postgres", qq(
		SET client_min_messages = DEBUG;
		SET min_parallel_table_scan_size = 1;
		CREATE INDEX idx ON tst USING ivfflat (v $opclass);
	));
	is($ret, 0, $stderr);
	like($stderr, qr/using \d+ parallel workers/);

	# Test approximate results
	test_recall(1, 0.08, $operator);
	test_recall(10, 0.50, $operator);

	# Test probes equals lists
	test_recall(100, 1.00, $operator);

	$node->safe_psql("postgres", "DROP INDEX idx;");
}

done_testing();
```

## File: `test/t/036_ivfflat_bit_centers.pl`
```
use strict;
use warnings FATAL => 'all';
use PostgreSQL::Test::Cluster;
use PostgreSQL::Test::Utils;
use Test::More;

# Initialize node
my $node = PostgreSQL::Test::Cluster->new('node');
$node->init;
$node->start;

# Create table
$node->safe_psql("postgres", "CREATE EXTENSION vector;");
$node->safe_psql("postgres", "CREATE TABLE tst (i int4, v bit(3));");
$node->safe_psql("postgres",
	"INSERT INTO tst SELECT i, floor(random() * 8)::bigint::bit(3) FROM generate_series(1, 100) i;"
);

my $counts = $node->safe_psql("postgres", "SELECT v, COUNT(*) FROM tst GROUP BY 1 ORDER BY 1");
my @rows = split("\n", $counts);
is(scalar(@rows), 8);

# Create index with more lists than distinct values
$node->safe_psql("postgres", "CREATE INDEX ON tst USING ivfflat (v bit_hamming_ops) WITH (lists = 100);");

for my $row (@rows)
{
	my ($v, $count) = split(/\|/, $row);

	my $actual = $node->safe_psql("postgres", qq(
		SET enable_seqscan = off;
		SELECT i FROM tst ORDER BY v <~> '$v' LIMIT 100;
	));
	my @actual_ids = split("\n", $actual);

	# Test results are always found
	is(scalar(@actual_ids), $count);
}

done_testing();
```

## File: `test/t/037_inputs.pl`
```
use strict;
use warnings FATAL => 'all';
use PostgreSQL::Test::Cluster;
use PostgreSQL::Test::Utils;
use Test::More;

# Initialize node
my $node = PostgreSQL::Test::Cluster->new('node');
$node->init;
$node->start;

# Create extension
$node->safe_psql("postgres", "CREATE EXTENSION vector;");

my @types = ("vector", "halfvec", "sparsevec");
my @inputs = ("[1.23,4.56,7.89]", "[1.23,4.56,7.89]", "{1:1.23,2:4.56,3:7.89}/3");
my @subs = (" ", " ", ",", ":", "-", "1", "9", "\0", "2147483648", "-2147483649");

for my $i (0 .. $#types)
{
	my $type = $types[$i];

	for (1 .. 100)
	{
		my $input = $inputs[$i] . "";

		for (1 .. 1 + int(rand() * 2))
		{
			my $r = int(rand() * length($input));
			my $sub = $subs[int(rand() * scalar(@subs))];
			if ($sub eq "\0")
			{
				# Truncate
				$input = substr($input, 0, $r);
			}
			elsif (rand() > 0.5)
			{
				# Insert
				substr($input, $r, 0) = $sub;
			}
			else
			{
				# Replace
				substr($input, $r, length($sub), $sub);
			}
		}

		my ($ret, $stdout, $stderr) = $node->psql("postgres", "SELECT '$input'::$type;");
		if ($ret != 0)
		{
			# Test for type in error message
			like($stderr, qr/$type/);
		}
		else
		{
			# Count test
			is($ret, 0);
		}
	}
}

done_testing();
```

## File: `test/t/038_hnsw_sparsevec_vacuum_insert.pl`
```
use strict;
use warnings FATAL => 'all';
use PostgreSQL::Test::Cluster;
use PostgreSQL::Test::Utils;
use Test::More;

# Initialize node
my $node = PostgreSQL::Test::Cluster->new('node');
$node->init;
$node->start;

# Create table and index
$node->safe_psql("postgres", "CREATE EXTENSION vector;");
$node->safe_psql("postgres", "CREATE TABLE tst (i serial, v sparsevec(100000));");
$node->safe_psql("postgres", "CREATE INDEX ON tst USING hnsw (v sparsevec_l2_ops);");

for (1 .. 3)
{
	for (1 .. 100)
	{
		my @elements;
		my %indices;
		for (1 .. int(rand() * 100))
		{
			my $index = int(rand() * (100000 - 1)) + 1;
			if (!exists($indices{$index}))
			{
				my $value = rand();
				push(@elements, "$index:$value");
				$indices{$index} = 1;
			}
		}
		my $embedding = "{" . join(",", @elements) . "}/100000";
		$node->safe_psql("postgres", "INSERT INTO tst (v) VALUES ('$embedding');");
	}

	$node->safe_psql("postgres", "DELETE FROM tst WHERE i % 2 = 0;");
	$node->safe_psql("postgres", "VACUUM tst;");
	is(1, 1);
}

done_testing();
```

## File: `test/t/039_hnsw_cost.pl`
```
use strict;
use warnings FATAL => 'all';
use PostgreSQL::Test::Cluster;
use PostgreSQL::Test::Utils;
use Test::More;

my @dims = (384, 1536);
my $limit = 10;

# Initialize node
my $node = PostgreSQL::Test::Cluster->new('node');
$node->init;
$node->start;

$node->safe_psql("postgres", "CREATE EXTENSION vector;");

for my $dim (@dims)
{
	my $array_sql = join(",", ('random()') x $dim);

	# Create table and index
	$node->safe_psql("postgres", "CREATE TABLE tst (i int4, v vector($dim));");
	$node->safe_psql("postgres",
		"INSERT INTO tst SELECT i, ARRAY[$array_sql] FROM generate_series(1, 2000) i;"
	);
	$node->safe_psql("postgres", "CREATE INDEX idx ON tst USING hnsw (v vector_l2_ops);");
	$node->safe_psql("postgres", "ANALYZE tst;");

	# Generate query
	my @r = ();
	for (1 .. $dim)
	{
		push(@r, rand());
	}
	my $query = "[" . join(",", @r) . "]";

	my $explain = $node->safe_psql("postgres", qq(
		EXPLAIN ANALYZE SELECT i FROM tst ORDER BY v <-> '$query' LIMIT $limit;
	));
	like($explain, qr/Index Scan using idx/);

	# 3x the rows are needed for distance filters
	# since the planner uses DEFAULT_INEQ_SEL for the selectivity (should be 1)
	# Recreate index for performance
	$node->safe_psql("postgres", "DROP INDEX idx;");
	$node->safe_psql("postgres",
		"INSERT INTO tst SELECT i, ARRAY[$array_sql] FROM generate_series(2001, 6000) i;"
	);
	$node->safe_psql("postgres", "CREATE INDEX idx ON tst USING hnsw (v vector_l2_ops);");
	$node->safe_psql("postgres", "ANALYZE tst;");

	$explain = $node->safe_psql("postgres", qq(
		EXPLAIN ANALYZE SELECT i FROM tst WHERE v <-> '$query' < 1 ORDER BY v <-> '$query' LIMIT $limit;
	));
	like($explain, qr/Index Scan using idx/);

	$node->safe_psql("postgres", "DROP TABLE tst;");
}

done_testing();
```

## File: `test/t/040_ivfflat_cost.pl`
```
use strict;
use warnings FATAL => 'all';
use PostgreSQL::Test::Cluster;
use PostgreSQL::Test::Utils;
use Test::More;

my @dims = (384, 1536);
my $limit = 10;

# Initialize node
my $node = PostgreSQL::Test::Cluster->new('node');
$node->init;
$node->start;

$node->safe_psql("postgres", "CREATE EXTENSION vector;");

for my $dim (@dims)
{
	my $array_sql = join(",", ('random()') x $dim);

	# Create table and index
	$node->safe_psql("postgres", "CREATE TABLE tst (i int4, v vector($dim));");
	$node->safe_psql("postgres",
		"INSERT INTO tst SELECT i, ARRAY[$array_sql] FROM generate_series(1, 5000) i;"
	);
	$node->safe_psql("postgres", "CREATE INDEX idx ON tst USING ivfflat (v vector_l2_ops) WITH (lists = 5);");
	$node->safe_psql("postgres", "ANALYZE tst;");

	# Generate query
	my @r = ();
	for (1 .. $dim)
	{
		push(@r, rand());
	}
	my $query = "[" . join(",", @r) . "]";

	my $explain = $node->safe_psql("postgres", qq(
		EXPLAIN ANALYZE SELECT i FROM tst ORDER BY v <-> '$query' LIMIT $limit;
	));
	like($explain, qr/Index Scan using idx/);

	$explain = $node->safe_psql("postgres", qq(
		EXPLAIN ANALYZE SELECT i FROM tst WHERE v <-> '$query' < 1 ORDER BY v <-> '$query' LIMIT $limit;
	));
	like($explain, qr/Index Scan using idx/);

	$node->safe_psql("postgres", "DROP TABLE tst;");
}

done_testing();
```

## File: `test/t/041_ivfflat_iterative_scan.pl`
```
use strict;
use warnings FATAL => 'all';
use PostgreSQL::Test::Cluster;
use PostgreSQL::Test::Utils;
use Test::More;

my $dim = 3;
my $array_sql = join(",", ('random()') x $dim);

# Initialize node
my $node = PostgreSQL::Test::Cluster->new('node');
$node->init;
$node->start;

# Create table
$node->safe_psql("postgres", "CREATE EXTENSION vector;");
$node->safe_psql("postgres", "CREATE TABLE tst (i int4 PRIMARY KEY, v vector($dim));");
$node->safe_psql("postgres",
	"INSERT INTO tst SELECT i, ARRAY[$array_sql] FROM generate_series(1, 100000) i;"
);
$node->safe_psql("postgres", "CREATE INDEX ON tst USING ivfflat (v vector_l2_ops);");

my $count = $node->safe_psql("postgres", qq(
	SET enable_seqscan = off;
	SET ivfflat.probes = 10;
	SET ivfflat.iterative_scan = relaxed_order;
	SELECT COUNT(*) FROM (SELECT v FROM tst WHERE i % 10000 = 0 ORDER BY v <-> (SELECT v FROM tst LIMIT 1) LIMIT 11) t;
));
is($count, 10);

foreach ((30, 50, 70))
{
	my $max_probes = $_;
	my $expected = $max_probes / 10;
	my $sum = 0;

	for my $i (1 .. 20)
	{
		$count = $node->safe_psql("postgres", qq(
			SET enable_seqscan = off;
			SET ivfflat.probes = 10;
			SET ivfflat.iterative_scan = relaxed_order;
			SET ivfflat.max_probes = $max_probes;
			SELECT COUNT(*) FROM (SELECT v FROM tst WHERE i % 10000 = 0 ORDER BY v <-> (SELECT v FROM tst WHERE i = $i) LIMIT 11) t;
		));
		$sum += $count;
	}

	my $avg = $sum / 20;
	cmp_ok($avg, '>', $expected - 2);
	cmp_ok($avg, '<', $expected + 2);
}

done_testing();
```

## File: `test/t/042_ivfflat_iterative_scan_recall.pl`
```
use strict;
use warnings FATAL => 'all';
use PostgreSQL::Test::Cluster;
use PostgreSQL::Test::Utils;
use Test::More;

my $node;
my @queries = ();
my @expected;
my $limit = 20;
my @cs = (100, 1000);

sub test_recall
{
	my ($c, $probes, $min, $operator) = @_;
	my $correct = 0;
	my $total = 0;

	my $explain = $node->safe_psql("postgres", qq(
		SET enable_seqscan = off;
		SET ivfflat.probes = $probes;
		SET ivfflat.iterative_scan = relaxed_order;
		EXPLAIN ANALYZE SELECT i FROM tst WHERE i % $c = 0 ORDER BY v $operator '$queries[0]' LIMIT $limit;
	));
	like($explain, qr/Index Scan using idx on tst/);

	for my $i (0 .. $#queries)
	{
		my $actual = $node->safe_psql("postgres", qq(
			SET enable_seqscan = off;
			SET ivfflat.probes = $probes;
			SET ivfflat.iterative_scan = relaxed_order;
			SELECT i FROM tst WHERE i % $c = 0 ORDER BY v $operator '$queries[$i]' LIMIT $limit;
		));
		my @actual_ids = split("\n", $actual);

		my @expected_ids = split("\n", $expected[$i]);
		my %expected_set = map { $_ => 1 } @expected_ids;

		foreach (@actual_ids)
		{
			if (exists($expected_set{$_}))
			{
				$correct++;
			}
		}

		$total += $limit;
	}

	cmp_ok($correct / $total, ">=", $min, "$operator $c");
}

# Initialize node
$node = PostgreSQL::Test::Cluster->new('node');
$node->init;
$node->start;

# Create table
$node->safe_psql("postgres", "CREATE EXTENSION vector;");
$node->safe_psql("postgres", "CREATE TABLE tst (i int4, v vector(3));");
$node->safe_psql("postgres",
	"INSERT INTO tst SELECT i, ARRAY[random(), random(), random()] FROM generate_series(1, 100000) i;"
);

# Generate queries
for (1 .. 20)
{
	my $r1 = rand();
	my $r2 = rand();
	my $r3 = rand();
	push(@queries, "[$r1,$r2,$r3]");
}

# Check each index type
my @operators = ("<->", "<=>");
my @opclasses = ("vector_l2_ops", "vector_cosine_ops");

for my $i (0 .. $#operators)
{
	my $operator = $operators[$i];
	my $opclass = $opclasses[$i];

	$node->safe_psql("postgres", "CREATE INDEX idx ON tst USING ivfflat (v $opclass);");

	foreach (@cs)
	{
		my $c = $_;

		# Get exact results
		@expected = ();
		foreach (@queries)
		{
			my $res = $node->safe_psql("postgres", qq(
				SET enable_indexscan = off;
				WITH top AS (
					SELECT v $operator '$_' AS distance FROM tst WHERE i % $c = 0 ORDER BY distance LIMIT $limit
				)
				SELECT i FROM tst WHERE (v $operator '$_') <= (SELECT MAX(distance) FROM top)
			));
			push(@expected, $res);
		}

		if ($c == 100)
		{
			test_recall($c, 1, 0.57, $operator);
			test_recall($c, 10, 0.98, $operator);
		}
		else
		{
			if ($operator eq "<->")
			{
				test_recall($c, 1, 0.80, $operator);
			}
			else
			{
				test_recall($c, 1, 0.88, $operator);
			}
		}
	}

	$node->safe_psql("postgres", "DROP INDEX idx;");
}

done_testing();
```

## File: `test/t/043_hnsw_iterative_scan.pl`
```
use strict;
use warnings FATAL => 'all';
use PostgreSQL::Test::Cluster;
use PostgreSQL::Test::Utils;
use Test::More;

my $dim = 3;
my $array_sql = join(",", ('random()') x $dim);

# Initialize node
my $node = PostgreSQL::Test::Cluster->new('node');
$node->init;
$node->start;

# Create table
$node->safe_psql("postgres", "CREATE EXTENSION vector;");
$node->safe_psql("postgres", "CREATE TABLE tst (i int4 PRIMARY KEY, v vector($dim));");
$node->safe_psql("postgres",
	"INSERT INTO tst SELECT i, ARRAY[$array_sql] FROM generate_series(1, 100000) i;"
);
$node->safe_psql("postgres", qq(
	SET maintenance_work_mem = '128MB';
	SET max_parallel_maintenance_workers = 2;
	CREATE INDEX ON tst USING hnsw (v vector_l2_ops)
));

my $count = $node->safe_psql("postgres", qq(
	SET enable_seqscan = off;
	SET hnsw.iterative_scan = relaxed_order;
	SET hnsw.max_scan_tuples = 100000;
	SET hnsw.scan_mem_multiplier = 2;
	SELECT COUNT(*) FROM (SELECT v FROM tst WHERE i % 10000 = 0 ORDER BY v <-> (SELECT v FROM tst LIMIT 1) LIMIT 11) t;
));
is($count, 10);

foreach ((30000, 50000, 70000))
{
	my $max_tuples = $_;
	my $expected = $max_tuples / 10000;
	my $sum = 0;

	for my $i (1 .. 20)
	{
		$count = $node->safe_psql("postgres", qq(
			SET enable_seqscan = off;
			SET hnsw.iterative_scan = relaxed_order;
			SET hnsw.max_scan_tuples = $max_tuples;
			SET hnsw.scan_mem_multiplier = 2;
			SELECT COUNT(*) FROM (SELECT v FROM tst WHERE i % 10000 = 0 ORDER BY v <-> (SELECT v FROM tst WHERE i = $i) LIMIT 11) t;
		));
		$sum += $count;
	}

	my $avg = $sum / 20;
	cmp_ok($avg, '>', $expected - 2);
	cmp_ok($avg, '<', $expected + 2);
}

done_testing();
```

## File: `test/t/044_hnsw_iterative_scan_recall.pl`
```
use strict;
use warnings FATAL => 'all';
use PostgreSQL::Test::Cluster;
use PostgreSQL::Test::Utils;
use Test::More;

my $node;
my @queries = ();
my @expected;
my $limit = 20;
my $dim = 3;
my $array_sql = join(",", ('random()') x $dim);
my @cs = (50, 500);

sub test_recall
{
	my ($c, $ef_search, $min, $operator, $mode) = @_;
	my $correct = 0;
	my $total = 0;

	my $explain = $node->safe_psql("postgres", qq(
		SET enable_seqscan = off;
		SET hnsw.ef_search = $ef_search;
		SET hnsw.iterative_scan = $mode;
		EXPLAIN ANALYZE SELECT i FROM tst WHERE i % $c = 0 ORDER BY v $operator '$queries[0]' LIMIT $limit;
	));
	like($explain, qr/Index Scan using idx on tst/);

	for my $i (0 .. $#queries)
	{
		my $actual = $node->safe_psql("postgres", qq(
			SET enable_seqscan = off;
			SET hnsw.ef_search = $ef_search;
			SET hnsw.iterative_scan = $mode;
			SELECT i FROM tst WHERE i % $c = 0 ORDER BY v $operator '$queries[$i]' LIMIT $limit;
		));
		my @actual_ids = split("\n", $actual);

		my @expected_ids = split("\n", $expected[$i]);
		my %expected_set = map { $_ => 1 } @expected_ids;

		foreach (@actual_ids)
		{
			if (exists($expected_set{$_}))
			{
				$correct++;
			}
		}

		$total += $limit;
	}

	cmp_ok($correct / $total, ">=", $min, "$operator $mode $c");
}

# Initialize node
$node = PostgreSQL::Test::Cluster->new('node');
$node->init;
$node->start;

# Create table
$node->safe_psql("postgres", "CREATE EXTENSION vector;");
$node->safe_psql("postgres", "CREATE TABLE tst (i int4, v vector($dim));");
$node->safe_psql("postgres",
	"INSERT INTO tst SELECT i, ARRAY[$array_sql] FROM generate_series(1, 50000) i;"
);

# Generate queries
for (1 .. 20)
{
	my @r = ();
	for (1 .. $dim)
	{
		push(@r, rand());
	}
	push(@queries, "[" . join(",", @r) . "]");
}

# Check each index type
my @operators = ("<->", "<=>");
my @opclasses = ("vector_l2_ops", "vector_cosine_ops");

for my $i (0 .. $#operators)
{
	my $operator = $operators[$i];
	my $opclass = $opclasses[$i];

	$node->safe_psql("postgres", qq(
		SET maintenance_work_mem = '128MB';
		CREATE INDEX idx ON tst USING hnsw (v $opclass);
	));

	foreach (@cs)
	{
		my $c = $_;

		# Get exact results
		@expected = ();
		foreach (@queries)
		{
			my $res = $node->safe_psql("postgres", qq(
				SET enable_indexscan = off;
				WITH top AS (
					SELECT v $operator '$_' AS distance FROM tst WHERE i % $c = 0 ORDER BY distance LIMIT $limit
				)
				SELECT i FROM tst WHERE (v $operator '$_') <= (SELECT MAX(distance) FROM top)
			));
			push(@expected, $res);
		}

		test_recall($c, 40, 0.99, $operator, "strict_order");
		test_recall($c, 40, 0.99, $operator, "relaxed_order");
	}

	$node->safe_psql("postgres", "DROP INDEX idx;");
}

done_testing();
```

## File: `test/t/045_hnsw_low_memory_build.pl`
```
use strict;
use warnings FATAL => 'all';
use PostgreSQL::Test::Cluster;
use PostgreSQL::Test::Utils;
use Test::More;

# Initialize node
my $node = PostgreSQL::Test::Cluster->new('node');
$node->init;
$node->start;

# Create table
$node->safe_psql("postgres", "CREATE EXTENSION vector;");
$node->safe_psql("postgres", "CREATE TABLE tst (v vector(3));");
$node->safe_psql("postgres",
	"INSERT INTO tst SELECT ARRAY[random(), random(), random()] FROM generate_series(1, 1000) i;"
);

my ($ret, $stdout, $stderr) = $node->psql("postgres", qq(
	SET client_min_messages = DEBUG;
	SET maintenance_work_mem = '3073kB';
	ALTER TABLE tst SET (parallel_workers = 1);
	CREATE INDEX ON tst USING hnsw (v vector_l2_ops);
));
is($ret, 0, $stderr);
like($stderr, qr/using \d+ parallel workers/);
like($stderr, qr/hnsw graph no longer fits into maintenance_work_mem after 0 tuples/);

done_testing();
```

